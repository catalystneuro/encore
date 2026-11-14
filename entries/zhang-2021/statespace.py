"""Loading and state space measures for CRCNS vim-4 (Zhang, Gao, Cukur & Gallant 2021).

The data set is streamed from the public CRCNS bucket; nothing is written to disk.

Where each method comes from:

- State space: the paper's Methods ("Voxel-Based State Space Modeling") and its
  code, gallantlab/state-space at commit 6ffb3c3, `extract_state_space_positions`
  (claims file, opening comment): OLS of the responses on the task variables
  with an intercept column (pinv of the normal equations), PCA with 24
  components on the [TR x voxel] responses, denoised weights U U^T B^T, the
  first (variables) columns of Q from the QR of the denoised weights, positions
  = responses x those columns, z-scored per dimension over the TRs fitted.
- Computation in PC space (an exact rewrite, not a change of method): every
  denoised weight vector lies in the span of the 24 components C (24 x voxels,
  orthonormal rows), so with Z = Y C^T the OLS coefficients projected on the
  components are pinv(P^T P) P^T Z, the QR of C^T M equals C^T times the QR of
  M, and the positions are Z Q_M. The PCA itself is computed exactly from the
  TR x TR Gram matrix Y Y^T (the eigenvectors of the centred Gram matrix); the
  code's scikit-learn PCA(24) uses a randomized solver for this shape, which
  approximates the same components. The notebook compares the two on one
  subject.
- JSD: the code's `JSD`, a Monte Carlo estimate from 1000 samples of each
  normal, in log base 2; computed here in the log domain (log-sum-exp), which
  gives the same values without the underflow of the code's ratio of
  densities. CSI: the mean JSD over all pairs of clusters (Methods,
  "Quantification of State Space Results", paragraph 1). Cluster normals use
  the sample mean and covariance (ddof 1), a standard choice.
- The JSD between two normals is unchanged by any invertible affine map applied
  to both, so the CSI does not depend on the signs, order or z-scoring of the
  state dimensions, only on the subspace they span.
- Cross-validation: 10 folds, the state space refitted on the training TRs
  (PCA included), held-out TRs projected and assigned to the nearest training
  cluster (Methods, paragraph 2). Folds, distance and z-scoring of held-out TRs
  are readings named in the claims file.
"""
import fsspec
import h5py
import numpy as np
from scipy import linalg

BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
DOI = "10.6080/K0668BDF"
VERSION = "unversioned"
ATT_SUBJECTS = ["S1", "S2", "S3", "S5", "S6"]  # S4 not released (data description)
GAME_SUBJECTS = ["S1", "S7"]
CONDITIONS = ["passive", "human", "vehicle"]  # stacking order of the code's Example.ipynb
N_PCS = 24  # Methods, "Voxel-Based State Space Modeling", paragraph 3
TABLE1_ORDER = ["dead", "round start", "safe explore", "unsafe explore", "kill",
                "engage close", "engage far", "flash", "run away"]
PRESENCE_NAMES = ["neither", "humans only", "vehicles only", "both"]


def _open(path, block_size=2**24):
    return fsspec.open(BASE + path, block_size=block_size).open()


def read_hdf(path, keys=None):
    """Read whole datasets of a small HDF5 file into memory."""
    with _open(path) as f, h5py.File(f, "r") as h:
        keys = list(h.keys()) if keys is None else keys
        return {k: h[k][()] for k in keys}


def hdf_layout(path):
    """Names, shapes and dtypes of every dataset in an HDF5 file (no data read)."""
    out = []
    with _open(path, 2**20) as f, h5py.File(f, "r") as h:
        h.visititems(lambda n, o: out.append((n, o.shape, str(o.dtype)))
                     if isinstance(o, h5py.Dataset) else None)
    return out


def npy_layout(path):
    with _open(path, 2**16) as f:
        np.lib.format.read_magic(f)
        shape, _, dtype = np.lib.format.read_array_header_1_0(f)
    return shape, str(dtype)


def load_attention_states():
    """[TR x 3] states per condition: human presence, vehicle presence, attention."""
    return read_hdf("VisualAttention/Stimuli/states.hdf", CONDITIONS)


def presence_code(states):
    """0 neither, 1 humans only, 2 vehicles only, 3 both (as in Example.ipynb)."""
    return (states[:, 0] + 2 * states[:, 1]).astype(int)


def gram_summary(Y):
    """Gram matrix and per-voxel summaries of a [TR x voxel] array."""
    sd = Y.std(0)
    return {"G": Y @ Y.T, "n_vox": Y.shape[1], "n_zero_vox": int((sd == 0).sum()),
            "vox_mean_range": (float(Y.mean(0).min()), float(Y.mean(0).max())),
            "vox_sd_range": (float(sd[sd > 0].min()), float(sd.max())),
            "n_nan": int(np.isnan(Y).sum())}


def code_positions(X, Y, num_PCs=N_PCS):
    """The paper's code, `extract_state_space_positions` (gallantlab/state-space
    at 6ffb3c3), on the full voxel data, kept as written to check the PC-space
    rewrite."""
    from scipy import stats
    from sklearn.decomposition import PCA
    parameters = np.ones([X.shape[0], X.shape[1] + 1])
    parameters[:, :-1] = X
    covar = parameters.T @ parameters
    coeffs = np.linalg.pinv(covar) @ (parameters.T @ Y)
    pca = PCA(num_PCs, random_state=0)
    pca.fit(Y)
    coeffs_denoised = pca.components_.T @ (pca.components_ @ coeffs.T)
    Q, _ = np.linalg.qr(coeffs_denoised)  # reduced QR: same first columns as 'full'
    return stats.zscore(Y @ Q[:, :X.shape[1]])


def load_attention_gram(subject, X_check=None):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are
    dropped. With X_check, also the positions from the paper's code on the full
    voxel data.
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    if X_check is not None:
        out["code_positions"] = code_positions(X_check, Y)
    del Y
    return out


def load_game(subject):
    """Stream one subject's video game BOLD (npy) and its state labels."""
    with _open(f"VideoGame/Data/{subject}.npy") as f:
        np.lib.format.read_magic(f)
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    out = gram_summary(Y)
    del Y
    st = read_hdf(f"VideoGame/Stimuli/{subject}.hdf")
    out["X"] = st["behavioural_state"].astype(float)
    out["labels"] = [s.decode().strip().lower() for s in st["state_labels"]]
    return out


# ---------------------------------------------------------------- PCA from Gram

def pca_scores(G, train, test=None, k=N_PCS):
    """Scores on the top-k principal components fitted to the training TRs.

    G is Y Y^T over all TRs. Training rows are centred on their own mean, as
    scikit-learn's PCA does; held-out rows are centred with the training mean.
    Returns (Z_train, Z_test or None, fraction of training variance explained).
    """
    train = np.asarray(train)
    Gtt = G[np.ix_(train, train)]
    rs = Gtt.mean(1)
    tot = rs.mean()
    Gc = Gtt - rs[:, None] - rs[None, :] + tot
    n = len(train)
    w, U = linalg.eigh(Gc, subset_by_index=[n - k, n - 1])
    w, U = w[::-1], U[:, ::-1]
    Z_tr = U * np.sqrt(w)
    Z_te = None
    if test is not None:
        test = np.asarray(test)
        Gx = G[np.ix_(test, train)]
        cross = Gx - Gx.mean(1)[:, None] - rs[None, :] + tot
        Z_te = cross @ U / np.sqrt(w)
    return Z_tr, Z_te, float(w.sum() / np.trace(Gc))


# ---------------------------------------------------------------- state space

def state_directions(Z, X):
    """Q_M and R: the QR of the denoised weights in PC coordinates.

    Z [TR x 24] PCA scores, X [TR x d] task variables. The intercept column is
    last, as in the code, so it does not change the first d directions.
    """
    P = np.column_stack([X, np.ones(len(X))])
    coef = np.linalg.pinv(P.T @ P) @ (P.T @ Z)  # (d+1) x 24, = B C^T
    Q, R = np.linalg.qr(coef.T)  # 24 x (d+1)
    d = X.shape[1]
    return Q[:, :d], R[:d, :d]


def positions(Z, X, sign=None):
    """Z-scored state space positions of the fitted TRs.

    sign: None (as the QR returns), "diag" (diagonal of R made positive) or
    "own" (each dimension oriented so its own variable's TRs, X[:, j] > 0, have
    a positive mean position).
    """
    Q, R = state_directions(Z, X)
    if sign == "diag":
        Q = Q * np.sign(np.diag(R))
    pos = Z @ Q
    pos = (pos - pos.mean(0)) / pos.std(0)
    if sign == "own":
        for j in range(X.shape[1]):
            if X[:, j].any() and pos[X[:, j] > 0, j].mean() < 0:
                pos[:, j] *= -1
    return pos


# ---------------------------------------------------------------- JSD and CSI

def _fit_normal(x):
    m = x.mean(0)
    c = np.cov(x, rowvar=False, ddof=1)
    return m, linalg.cholesky(np.atleast_2d(c), lower=True)


def _logpdf(x, m, L):
    sol = linalg.solve_triangular(L, (x - m).T, lower=True)
    d = len(m)
    return -0.5 * (sol ** 2).sum(0) - np.log(np.diag(L)).sum() - 0.5 * d * np.log(2 * np.pi)


def jsd(n1, n2, rng, samples=1000):
    """Monte Carlo JSD (bits) between two fitted normals (m, cholesky)."""
    (m1, L1), (m2, L2) = n1, n2
    d = len(m1)
    s1 = m1 + rng.standard_normal((samples, d)) @ L1.T
    s2 = m2 + rng.standard_normal((samples, d)) @ L2.T
    # log2(p_a / ((p_a + p_b) / 2)) = 1 - log2(1 + p_b / p_a)
    a = 1 - np.logaddexp(0, _logpdf(s1, m2, L2) - _logpdf(s1, m1, L1)) / np.log(2)
    b = 1 - np.logaddexp(0, _logpdf(s2, m1, L1) - _logpdf(s2, m2, L2)) / np.log(2)
    return 0.5 * (a.mean() + b.mean())


def csi(pos, members, rng, samples=1000):
    """Cluster separation index: mean pairwise JSD of the clusters' normals.

    members: list of boolean or index arrays, one per cluster.
    """
    normals = [_fit_normal(pos[m]) for m in members]
    vals = [jsd(normals[i], normals[j], rng, samples)
            for i in range(len(normals)) for j in range(i + 1, len(normals))]
    return float(np.mean(vals))


# ---------------------------------------------------------------- classification

def nearest_cluster(train_pos, train_lab, test_pos, classes, rule):
    """Assign each test point to the nearest training cluster.

    rule "euclid": Euclidean distance to the cluster mean; "density": highest
    density under the cluster's fitted normal.
    """
    if rule == "euclid":
        means = np.array([train_pos[train_lab == c].mean(0) for c in classes])
        d2 = ((test_pos[:, None, :] - means[None]) ** 2).sum(-1)
        return np.asarray(classes)[d2.argmin(1)]
    ll = np.column_stack([_logpdf(test_pos, *_fit_normal(train_pos[train_lab == c]))
                          for c in classes])
    return np.asarray(classes)[ll.argmax(1)]


def folds(n, scheme, rng, k=10):
    """Test indices of k folds: "contig" (contiguous tenths) or "random"."""
    idx = np.arange(n) if scheme == "contig" else rng.permutation(n)
    return np.array_split(idx, k)


def fold_scores(G, test_sets):
    """PCA scores per fold: list of (train, test, Z_train, Z_test)."""
    n = G.shape[0]
    out = []
    for te in test_sets:
        tr = np.setdiff1d(np.arange(n), te)
        Ztr, Zte, _ = pca_scores(G, tr, te)
        out.append((tr, te, Ztr, Zte))
    return out


def project_fold(Ztr, Zte, Xtr):
    """Training and held-out positions; held-out z-scored with training statistics."""
    Q, _ = state_directions(Ztr, Xtr)
    ptr, pte = Ztr @ Q, Zte @ Q
    m, s = ptr.mean(0), ptr.std(0)
    return (ptr - m) / s, (pte - m) / s


# ---------------------------------------------------------------- attention task

def att_positions(Z, X, third, rng=None):
    """Positions in the attention state space under a reading of its third axis.

    In the deposited deconvolved data each attentive condition is z-scored per
    voxel, so the attention variable (-1, 0, +1) has an OLS weight of zero up to
    rounding and the third QR direction is set by rounding noise.
    third: "qr" (as the QR returns it), "2d" (human and vehicle axes only) or
    "random" (a random unit direction in the PC space, orthogonal to the
    first two, drawn from rng).
    """
    Q, _ = state_directions(Z, X)
    if third == "2d":
        Q = Q[:, :2]
    elif third == "random":
        v = rng.standard_normal(Q.shape[0])
        v -= Q[:, :2] @ (Q[:, :2].T @ v)
        Q = np.column_stack([Q[:, :2], v / np.linalg.norm(v)])
    pos = Z @ Q
    return (pos - pos.mean(0)) / pos.std(0)


def cond_slices(n_per=900):
    return [slice(i * n_per, (i + 1) * n_per) for i in range(len(CONDITIONS))]


def att_csis(pos, pcode, rng, members=None):
    """CSI of the four presence clusters within each condition (passive, human, vehicle).

    members: optional list of three index arrays giving each condition's TRs.
    """
    members = cond_slices() if members is None else members
    out = []
    for m in members:
        p, c = pos[m], pcode[m]
        out.append(csi(p, [c == k for k in range(4)], rng))
    return np.array(out)


def shuffle_presence(X, reading, rng):
    """Permuted presence labels: "a" rows of (human, vehicle) shuffled over all
    TRs; "b" circularly shifted by a random lag within each condition."""
    Xp = X.copy()
    if reading == "a":
        Xp[:, :2] = X[rng.permutation(len(X)), :2]
    else:
        for s in cond_slices():
            Xp[s, :2] = np.roll(X[s, :2], rng.integers(1, s.stop - s.start), axis=0)
    return Xp


def shuffle_conditions(n_per, scheme, rng):
    """Permuted condition membership for the passive-against-attentive test.

    Returns three index arrays (passive, human, vehicle). "matched": at each
    movie time point the three TRs showing the same frame are given the three
    conditions in random order, so every condition keeps the same presence
    labels; "global": TRs shuffled across all conditions. A standard choice for
    a detail the claims file does not fix; both are run.
    """
    n = n_per * 3
    if scheme == "global":
        p = rng.permutation(n)
        return [np.sort(p[i * n_per:(i + 1) * n_per]) for i in range(3)]
    order = np.argsort(rng.random((n_per, 3)), axis=1)  # condition of each copy
    t = np.arange(n_per)
    return [np.sort(np.concatenate([c * n_per + t[order[:, c] == k] for c in range(3)]))
            for k in range(3)]


def members_to_X(X, members):
    """State matrix with the attention column set by the permuted membership."""
    Xp = X.copy()
    for value, m in zip([0.0, -1.0, 1.0], members):
        Xp[m, 2] = value
    return Xp


# ---------------------------------------------------------------- video game

def game_matrix(X, labels, order):
    """State matrix with columns in dataset order or Table 1 order; states with
    no TRs are dropped (flash in S7), as Supplementary Figure 4 has no flash
    weights for that subject."""
    names = labels if order == "dataset" else [s for s in TABLE1_ORDER if s in labels]
    cols = [labels.index(s) for s in names]
    keep = [i for i, c in enumerate(cols) if X[:, c].any()]
    return X[:, [cols[i] for i in keep]], [names[i] for i in keep]


def game_members(X, names, reading):
    """Clusters for the video game CSI.

    "a" one per state, a TR in the cluster of every state it has; "b" one per
    state from TRs with exactly one state; "c" safe explore, engage close and
    all other TRs (Figure 3A). Clusters with no more TRs than dimensions are
    left out (no covariance can be fitted).
    """
    d = X.shape[1]
    if reading == "c":
        se, ec = X[:, names.index("safe explore")] > 0, X[:, names.index("engage close")] > 0
        mem, nm = [se, ec, ~se & ~ec], ["safe explore", "engage close", "other"]
    else:
        ok = np.ones(len(X), bool) if reading == "a" else X.sum(1) == 1
        mem = [(X[:, j] > 0) & ok for j in range(d)]
        nm = list(names)
    keep = [i for i, m in enumerate(mem) if m.sum() > d]
    dropped = [(nm[i], int(mem[i].sum())) for i in range(len(mem)) if i not in keep]
    return [mem[i] for i in keep], [nm[i] for i in keep], dropped


def projection_matrix(pos, X):
    """M[i, j]: mean position on dimension j of the TRs that have state i."""
    return np.array([pos[X[:, i] > 0].mean(0) for i in range(X.shape[1])])


def balanced_accuracy(H, pred, classes):
    """Balanced accuracy (Brodersen et al. 2010, cited by the paper): the mean
    recall over the classes present. H [TR x classes] is True where a TR has
    the class (a TR may have several); the recall of class c is the fraction
    of the TRs that have c that are predicted as c."""
    rec = [(pred[H[:, k]] == c).mean() for k, c in enumerate(classes) if H[:, k].any()]
    return float(np.mean(rec))
