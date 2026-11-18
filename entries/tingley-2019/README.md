# Tingley and Buzsaki (2019) on DANDI:000218

Tests the findings of Tingley D. and Buzsaki G. (2019), "Routing of hippocampal ripples to subcortical structures via the lateral septum", Neuron 105, 138-149 (doi:10.1016/j.neuron.2019.10.012), on dandiset 000218, version 0.261110.1911, streamed from the DANDI Archive.

- `reproduce_tingley_2019.ipynb`: the claims that use spikes, the lab's LS HFO and CA1 ripple tables, sleep states and trials (Figures 1, 4, 5, S1 to S3, and two Discussion statements). About 20 minutes.
- `lfp_tingley_2019.ipynb`: the claims that need the LFP (phase locking, locking to the CA1 ripple band, event times at the maximum NSS, CA1-LS coherence, HFO power by recording site). About 52 minutes.
- `fig7e_tingley_2019.ipynb`: LS spike counts in SPW-Rs predicted from the hippocampal spike count, brain state and SPW-R duration (Figure 7E). About 25 minutes.
- `shanks_tingley_2019.ipynb`: phase locking of the LS neurons whose shank lies outside the detection channel's storage block to a site on their own shank (fig1d-phase-locking). About 15 minutes.
- `tingley2019.py`: loading and shared measures; its docstrings say where each parameter comes from.

Claims on the optogenetic rats, on electrode geometry and on depth within LS cannot be tested from the dandiset; replay, seqNMF and the network model were not attempted within the run's time.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
