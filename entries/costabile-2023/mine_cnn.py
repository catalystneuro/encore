"""The MINE CNN of Costabile et al. (2023), used here to time a fit on this machine and to fit a
random subsample of the zebrafish components (mine_fits_subsample.ipynb).

The architecture, training and data preparation follow the paper's code, github.com/haesemeyer/mine_pub
at commit 368d756: model.py (ActivityPredictor, get_standard_model: 80 linear convolutional filters
over the 50-step history without bias, two dense layers of 64 swish units, dropout 0.5 after each,
L1 penalty 1e-3 on the filters and dense weights, Adam with learning rate 1e-3, mean squared error;
train_model: 100 epochs), utilities.py (Data.training_data: batch 256, shuffled each epoch;
safe_standardize; modified_gram_schmidt) and rwave_data_fit.py (behavior predictors mean-subtracted,
orthogonalized and z-scored; calcium z-scored and smoothed with a Gaussian of sigma 2.5 frames;
the first two-thirds of the frames for training). Keras' Sequential model replaces the code's
subclassed model; the layers and their order are the same. Seeds come from the claim
(docs/protocol.md, Author, step 3).
"""
from __future__ import annotations

import os

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
import numpy as np
from scipy.ndimage import gaussian_filter1d

HIST = 50  # 10 s at 5 Hz (rwave_data_fit.py)
N_EPOCHS = 100
BATCH = 256


def safe_standardize(x: np.ndarray, epsilon: float = 1e-9) -> np.ndarray:
    y = x - np.mean(x)
    return y / (np.std(y) + epsilon)


def modified_gram_schmidt(col_mat: np.ndarray) -> np.ndarray:
    """utilities.modified_gram_schmidt: orthonormal columns, linearly dependent ones set to 0."""
    v = col_mat.astype(np.float64).copy()
    for j in range(v.shape[1]):
        if np.allclose(v[:, j], 0):
            v[:, j] = 0
            continue
        q = v[:, j] / np.linalg.norm(v[:, j])
        for k in range(j + 1, v.shape[1]):
            v[:, k] = v[:, k] - (q @ v[:, k]) * q
    norms = np.linalg.norm(v, axis=0, keepdims=True)
    norms[norms < 1e-9] = 1e-9
    return v / norms


def prepare_predictors(temp5: np.ndarray, behavior: np.ndarray) -> np.ndarray:
    """Temperature and three behavior rows (5 Hz) -> T x 4 standardized predictor matrix."""
    b = behavior - behavior.mean(axis=1, keepdims=True)
    b = modified_gram_schmidt(b.T).T
    cols = [safe_standardize(temp5)] + [safe_standardize(r) for r in b]
    return np.vstack(cols).T.astype(np.float32)


def prepare_response(ca5: np.ndarray) -> np.ndarray:
    return gaussian_filter1d(safe_standardize(ca5), 2.5).astype(np.float32)


def _model(n_pred: int):
    import tensorflow as tf
    from tensorflow.keras import initializers, layers, regularizers
    reg = regularizers.l1(1e-3)
    g = initializers.GlorotUniform
    return tf.keras.Sequential([
        layers.Input((HIST, n_pred)),
        layers.Conv1D(80, HIST, use_bias=False, kernel_regularizer=reg, kernel_initializer=g()),
        layers.Flatten(), layers.Dropout(0.5),
        layers.Dense(64, activation="swish", kernel_regularizer=reg, kernel_initializer=g()), layers.Dropout(0.5),
        layers.Dense(64, activation="swish", kernel_regularizer=reg, kernel_initializer=g()), layers.Dropout(0.5),
        layers.Dense(1)])


def fit_and_test(X: np.ndarray, y: np.ndarray, seed: int) -> float:
    """Fit on the first two-thirds (windows ending before train_frames, as Data.training_data), return
    the test correlation as rwave_data_fit.py computes it."""
    import tensorflow as tf
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
    tf.keras.backend.clear_session()  # free the previous fit's graph, so memory stays flat over many fits
    tf.keras.utils.set_random_seed(seed % (2 ** 31))
    T = y.size
    train = (T * 2) // 3
    idx = np.arange(HIST - 1, T)
    win = np.stack([X[i - HIST + 1:i + 1] for i in idx])
    yy = y[idx]
    ntr = train - (HIST - 1)
    m = _model(X.shape[1])
    opt = tf.keras.optimizers.Adam(1e-3)
    mse = tf.keras.losses.MeanSquaredError()

    @tf.function
    def step(a, b):
        with tf.GradientTape() as tape:
            loss = mse(b, m(a, training=True)) + tf.add_n(m.losses)
        g = tape.gradient(loss, m.trainable_variables)
        opt.apply_gradients(zip(g, m.trainable_variables))

    ds = tf.data.Dataset.from_tensor_slices((win[:ntr], yy[:ntr])).shuffle(
        ntr, seed=seed % (2 ** 31), reshuffle_each_iteration=True).batch(BATCH, drop_remainder=True)
    for _ in range(N_EPOCHS):
        for a, b in ds:
            step(a, b)
    # rwave_data_fit.py scores p[train_frames:] of the prediction over frames HIST-1 onwards
    # (Data.predict_response), so the test frames start HIST-1 frames after the last training frame.
    pred = m(win[train:], training=False).numpy().ravel()
    return float(np.corrcoef(pred, yy[train:])[0, 1])


def fit_plane_components(asset_id: str, plane: int, comps: np.ndarray, temp5: np.ndarray, behavior: np.ndarray,
                         seeds: np.ndarray, frame_duration: float) -> dict:
    """Fit the CNN to the given components of one plane (CaImAn's calcium, on the 5 Hz base as
    rwave_data_fit.py), one seed per fit. Returns the test correlations and the time of each fit."""
    import time
    import mine_data as md
    with md.open_nwb(asset_id) as f:
        C = f[f"processing/ophys/CaUnitRespones_Z{plane}/data"][:, np.sort(comps)]
    order = np.argsort(np.argsort(comps))
    C = C[:, order]
    ca_t, i_t = md.time_base(C.shape[0], frame_duration)
    X = prepare_predictors(temp5, behavior)
    rs, ts = [], []
    for j in range(len(comps)):
        y = prepare_response(np.interp(i_t, ca_t, C[:, j]))
        t = time.time()
        rs.append(fit_and_test(X, y, int(seeds[j])))
        ts.append(time.time() - t)
    return dict(r=np.array(rs), t=np.array(ts))
