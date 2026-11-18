"""The leaky integrate-and-fire network of Burman et al. (2023), Figures 4E to 4H and S7.

A transcription of the paper's simulation gist,
gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b (burman_et_al_2023_neuronal_network_simulation.py),
which the claims file names as the method of the model claims. Every parameter below is the
gist's, and matches the Methods ("Neuronal network simulations", Table 1): 800 excitatory and
200 inhibitory neurons, connection probability 10%, weights 0.1 nS and 1 nS, Vogels
inhibitory plasticity during a balancing set, E_GABA -60 mV then -80 mV in the excitatory
neurons, 100 input patterns of 1 ms pulses (M = 500 pA) every 25 ms, each repeated 100 times
per condition, and lognormal noise (M = 25 pA) changed every 10 ms.

Differences from the gist, none of which changes the model:

- The gist builds the stimulus as one array for the whole run (502,500 by 1,000 values,
  4 GB, copied again when given units), which does not fit the runner's memory with a second
  copy. The stimulus is periodic (the same 100 patterns in every 2,500 ms set), so here the
  TimedArray holds one set and is read at t modulo the set's length. The values each neuron
  receives at each time step are the same.
- Random seeds are fixed, one per run (protocol: fix every seed); the gist sets none. The
  paper does not give its seeds, so runs here are other draws of the same model.
- The gist's coo_matrix is converted to CSR before columns are taken, as the classifier needs
  an indexable matrix; the values are the same.
- As in the gist, the inhibitory neurons read columns 0 to 199 of the stimulus and noise
  arrays, the same columns as the first 200 excitatory neurons.
- The analysis returns the values the gist writes to its CSV (spike count, firing rate,
  entropy, synchrony per excitatory neuron, and the decoding accuracy) as arrays.
- In addition to the gist's accuracy, decoding_ties() reports how often the classifier's five
  nearest neighbours are tied with the sixth, and the accuracy when tied neighbours are chosen
  by other training orders (the spike counts are small integers, so most distances tie).
"""
import time

import brian2 as b2
import numpy as np
from scipy.sparse import coo_matrix
from scipy.stats import entropy as get_entropy
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier, NearestNeighbors

EGABA = (-60, -80)  # mV, shunting then hyperpolarizing (Methods; gist)


def peristimulus_histogram(spike_times, interval, bin_width):
    """The gist's histogram without KDE: bins of bin_width from interval[0]."""
    bins = np.arange(interval[0], interval[1] + bin_width, bin_width)
    indices = np.digitize(spike_times, bins) - 1
    interval_length = interval[1] - interval[0]
    counts = np.bincount(indices[indices >= 0], minlength=interval_length)
    return counts[:interval_length].astype(float)


def histogram_entropy(spike_times, interval, bin_width):
    """Entropy in nats of the normalized peri-stimulus histogram (scipy.stats.entropy)."""
    h = peristimulus_histogram(spike_times, interval, bin_width)
    return get_entropy(h / h.sum())


def decoding_ties(X, y, seed, orders=5):
    """The gist's decoder (5 nearest neighbours, 5-fold shuffled stratified cross-validation
    with the same folds as simulate) examined for ties. Returns the share of test trials whose
    fifth-nearest training trial is at the same distance as the sixth, so that the five
    neighbours are chosen by how ties are broken, and the mean accuracy for each of `orders`
    random orders of the training trials, which break those ties differently."""
    rng = np.random.default_rng(seed)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    tied, acc = 0, np.zeros(orders)
    for train, test in cv.split(X, y):
        d, _ = NearestNeighbors(n_neighbors=6).fit(X[train]).kneighbors(X[test])
        tied += int(np.sum(d[:, 4] == d[:, 5]))
        for k in range(orders):
            p = rng.permutation(train)
            acc[k] += KNeighborsClassifier().fit(X[p], y[p]).score(X[test], y[test]) / 5
    return tied / len(y), acc


def simulate(seed, stimuli=100, repeats=100, verbose=False, periodic=True, spikes=False):
    """One run of the gist's network. Returns a dict per E_GABA value (-60, -80) with the
    per-neuron arrays of the 800 excitatory neurons and the decoding accuracy.

    periodic=False builds the stimulus as the gist does, one array for the whole run (for the
    check that both give the same spikes, on a small network run); spikes=True also returns the
    excitatory spike times and indices."""
    np.random.seed(seed)
    b2.seed(seed)
    b2.start_scope()
    b2.prefs.codegen.target = "cython"

    total_conditions = 2
    total_neurons = 1000
    total_stimuli = stimuli
    total_repeats = total_conditions * repeats
    total_condition_epochs = total_stimuli * repeats
    total_balancing_epochs = total_stimuli
    total_testing_epochs = total_stimuli * total_repeats
    epoch_duration = 25
    balancing_time = total_balancing_epochs * epoch_duration
    testing_time = total_testing_epochs * epoch_duration
    total_time = balancing_time + testing_time
    condition_duration = testing_time / total_conditions
    stimulus_set_duration = total_stimuli * epoch_duration

    stimulus_duration = 1
    stimulus_magnitude = 500
    total_subepochs = int(epoch_duration / stimulus_duration)
    base_stimuli = np.zeros((total_stimuli * total_subepochs, total_neurons))
    base_stimuli[::total_subepochs] = stimulus_magnitude * np.random.lognormal(
        size=(total_stimuli, total_neurons))
    if periodic:
        # one stimulus set, read periodically (see the module docstring)
        I_stimulus_set = b2.TimedArray(-base_stimuli * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = stimulus_set_duration * b2.ms
    else:
        # the gist's array for the whole run; t % set_duration then leaves t unchanged
        stimuli_full = np.vstack([base_stimuli] * (total_repeats + 1))
        I_stimulus_set = b2.TimedArray(-stimuli_full * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = 10 * total_time * b2.ms

    base_stimuli_labels = np.arange(total_stimuli)
    stimuli_labels = np.hstack([base_stimuli_labels] * (total_repeats + 1))

    noise_time_scale = 10.
    noise_magnitude = 25
    arr_noise = noise_magnitude * np.random.lognormal(
        size=(int(total_time / noise_time_scale), total_neurons))
    I_random = b2.TimedArray(-arr_noise * b2.pA, dt=noise_time_scale * b2.ms)

    n_exc, n_inh = int(4 * total_neurons / 5), int(total_neurons / 5)
    values = [np.mean(EGABA)] + repeats * [EGABA[0]] + repeats * [EGABA[1]]
    E_GABA_exc = b2.TimedArray(np.array(values) * b2.mV, dt=stimulus_set_duration * b2.ms)

    ns = dict(I_stimulus_set=I_stimulus_set, set_duration=set_duration, I_random=I_random,
              E_GABA_exc=E_GABA_exc,
              E_L_exc=-60. * b2.mV, V_th_exc=-50. * b2.mV, E_GABA_inh=-60. * b2.mV,
              E_L_inh=-60. * b2.mV, V_th_inh=-50. * b2.mV, C_m=200. * b2.pfarad,
              g_L=10. * b2.nsiemens, E_GLUT=0. * b2.mV, tau_GLUT=5. * b2.ms,
              tau_GABA=10. * b2.ms)
    t_ref = 5. * b2.ms

    exc_neuron_eqs = '''
    dv/dt      = -(I_L + I_GLUT + I_GABA + I_ext)/C_m  : volt (unless refractory)
    I_ext      =  I_stimulus_set(t % set_duration, i) + I_random(t, i) : amp
    I_L        =  g_L    * (v - E_L_exc)               : amp
    I_GLUT     =  g_GLUT * (v - E_GLUT)                : amp
    I_GABA     =  g_GABA * (v - E_GABA_exc(t))         : amp
    dg_GLUT/dt = -g_GLUT / tau_GLUT                    : siemens
    dg_GABA/dt = -g_GABA / tau_GABA                    : siemens
    '''
    inh_neuron_eqs = '''
    dv/dt      = -(I_L + I_GLUT + I_GABA + I_ext)/C_m  : volt (unless refractory)
    I_ext      =  I_stimulus_set(t % set_duration, i) + I_random(t, i) : amp
    I_L        =  g_L    * (v - E_L_inh)               : amp
    I_GLUT     =  g_GLUT * (v - E_GLUT)                : amp
    I_GABA     =  g_GABA * (v - E_GABA_inh)            : amp
    dg_GLUT/dt = -g_GLUT / tau_GLUT                    : siemens
    dg_GABA/dt = -g_GABA / tau_GABA                    : siemens
    '''
    exc = b2.NeuronGroup(n_exc, model=exc_neuron_eqs, threshold='v>V_th_exc',
                         reset='v=E_L_exc', refractory=t_ref, method='euler', namespace=ns)
    inh = b2.NeuronGroup(n_inh, model=inh_neuron_eqs, threshold='v>V_th_inh',
                         reset='v=E_L_inh', refractory=t_ref, method='euler', namespace=ns)
    exc.v = ns["E_L_exc"]
    inh.v = ns["E_L_inh"]

    syn_ns = dict(tau_stdp=20. * b2.ms, gmax=100. * b2.nsiemens,
                  beta=3. * b2.Hz * 20. * b2.ms * 2, eta=0.1)
    static_ex = dict(model='w : siemens', on_pre='g_GLUT_post += w')
    static_in = dict(model='w : siemens', on_pre='g_GABA_post += w')
    vogels = dict(model='''
        w : siemens
        dApre/dt  = -Apre  / tau_stdp : siemens (event-driven)
        dApost/dt = -Apost / tau_stdp : siemens (event-driven)
        ''',
        on_pre='''
        Apre += 1.*nsiemens
        w = clip(w + (Apost - beta * nsiemens) * eta, 0 * nsiemens, gmax)
        g_GABA_post += w''',
        on_post='''
        Apost += 1. * nsiemens
        w = clip(w + Apre * eta, 0 * nsiemens, gmax)
        ''')
    pop = {"exc": exc, "inh": inh}
    conns = {("exc", "exc"): (static_ex, 0.1, 0.1), ("exc", "inh"): (static_ex, 0.1, 0.1),
             ("inh", "inh"): (static_in, 0.1, 1.), ("inh", "exc"): (vogels, 0.1, 1.)}
    synapses = []
    for (a, b_), (model, p, w) in conns.items():
        s = b2.Synapses(pop[a], pop[b_], **model, namespace=syn_ns)
        s.connect(p=p)
        s.w = w * b2.nsiemens
        synapses.append(s)
    mon = b2.SpikeMonitor(exc)
    net = b2.Network(exc, inh, *synapses, mon)

    # the gist's loop runs the balancing set with eta = 0.1, then the test with eta = 0
    # eta_used: the value of eta in the compiled code of the plastic synapses' pre and post
    # pathways after each run, i.e. the value Brian 2 used in that run
    timing, w_sums, eta_used = [], [], []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)
        w_sums.append(float(np.sum(synapses[3].w / b2.nsiemens)))
        eta_used.append([float(getattr(synapses[3], path).codeobj.variables["eta"].get_value())
                         for path in ("pre", "post")])
    if verbose:
        print("run times", timing)

    out = {}
    all_t = np.asarray(mon.t / b2.ms)
    all_i = np.asarray(mon.i)
    for ctr, E_GABA in enumerate(EGABA):
        condition_start = balancing_time + ctr * condition_duration
        condition_stop = condition_start + condition_duration
        valid = (all_t >= condition_start) & (all_t < condition_stop)
        spike_indices = all_i[valid]
        spike_times = all_t[valid] - condition_start

        epoch_indices = (spike_times / epoch_duration).astype(int)
        X = coo_matrix((np.ones_like(spike_times), (epoch_indices, spike_indices)),
                       shape=(total_condition_epochs, n_exc)).tocsr()
        y = stimuli_labels[(total_balancing_epochs + ctr * total_condition_epochs):
                           (total_balancing_epochs + (ctr + 1) * total_condition_epochs)]
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        accuracy = np.mean(cross_val_score(KNeighborsClassifier(), X[:, :50], y, cv=cv))
        tied_share, accuracy_orders = decoding_ties(X[:, :50], y, seed)

        is_valid = (spike_times >= 0) & (spike_times < stimulus_set_duration)
        spike_indices = spike_indices[is_valid]
        spike_times = spike_times[is_valid]
        epoch_indices = epoch_indices[is_valid]
        spike_times = spike_times % epoch_duration
        interval = (0, 12)
        is_valid = (spike_times >= interval[0]) & (spike_times < interval[1])
        spike_times = spike_times[is_valid]
        spike_indices = spike_indices[is_valid]
        epoch_indices = epoch_indices[is_valid]

        spike_counts = np.bincount(spike_indices, minlength=n_exc).astype(float)
        firing_rates = spike_counts / (total_stimuli * (interval[1] - interval[0]) / 1000)

        entropy = np.full(n_exc, np.nan)
        for neuron in np.unique(spike_indices):
            entropy[neuron] = histogram_entropy(spike_times[spike_indices == neuron], interval, 1)

        s_sum = np.zeros(n_exc)
        s_n = np.zeros(n_exc)
        for epoch in range(total_stimuli):
            m = epoch_indices == epoch
            if m.any():
                pr = peristimulus_histogram(spike_times[m], interval, 1)
                pr /= pr.sum()
                idx = (spike_times[m] - interval[0]).astype(int)
                np.add.at(s_sum, spike_indices[m], pr[idx])
                np.add.at(s_n, spike_indices[m], 1)
        synchrony = np.where(s_n > 0, s_sum / np.where(s_n > 0, s_n, 1), np.nan)

        out[E_GABA] = dict(spike_count=spike_counts, firing_rate=firing_rates,
                           entropy=entropy, synchrony=synchrony, accuracy=accuracy,
                           tied_share=tied_share, accuracy_orders=accuracy_orders,
                           total_spikes=int(valid.sum()))
    if spikes:
        out["spikes"] = (all_t, all_i)
    out["run_seconds"] = sum(timing)
    # summed inhibitory-to-excitatory weight (nS) at the start, after balancing and after the
    # test: plasticity acts only during balancing (gist: eta 0.1, then 0)
    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    out["eta_used"] = eta_used
    return out


def run(seed):
    """One full run at the gist's defaults, for a process pool."""
    return simulate(seed)


GIST_URL = ("https://gist.githubusercontent.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f/raw/"
            "f6a05661c10051560aa381e334099efd8521617b/burman_et_al_2023_neuronal_network_simulation.py")


def run_gist(seed, stimuli=10, repeats=5):
    """Run the paper's simulation gist, unmodified, on a small network run, for the check that
    simulate() transcribes it. Returns the gist's module namespace after the run.

    The gist is fetched at its revision and run with its own command-line options (--stimuli,
    --repeats), after np.random.seed(seed) and b2.seed(seed) as in simulate(). Three things
    around it are changed, none in its code: umap, imported for a plot the run does not make, is
    a stand-in; scipy.sparse.coo_matrix returns a CSR matrix while it runs, as the installed
    scipy cannot index a COO matrix (X[:, :50]); and Brian 2's code generation target is cython,
    as in simulate(). Its decoding uses an unseeded shuffle, so its accuracy is not compared.
    """
    import sys
    import types
    import requests
    import scipy.sparse

    src = requests.get(GIST_URL, timeout=60).text
    saved = sys.argv, sys.modules.get("umap"), scipy.sparse.coo_matrix
    coo = scipy.sparse.coo_matrix
    sys.argv = ["burman_et_al_2023_neuronal_network_simulation.py",
                "--stimuli", str(stimuli), "--repeats", str(repeats)]
    sys.modules["umap"] = types.SimpleNamespace(UMAP=None)
    scipy.sparse.coo_matrix = lambda *a, **k: coo(*a, **k).tocsr()
    b2.prefs.codegen.target = "cython"
    np.random.seed(seed)
    b2.seed(seed)
    g = {"__name__": "__main__"}
    try:
        exec(compile(src, "burman_et_al_2023_neuronal_network_simulation.py", "exec"), g)
    finally:
        sys.argv, scipy.sparse.coo_matrix = saved[0], saved[2]
        if saved[1] is None:
            sys.modules.pop("umap", None)
        else:
            sys.modules["umap"] = saved[1]
    return g
