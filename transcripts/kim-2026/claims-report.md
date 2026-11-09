I wrote the claims file for DANDI:001868 at `claims/001868/10.1126-sciadv.aef0343.yaml`. It has 42 claims, all with quotes and criteria; 33 have statistics (121 test entries) and 12 have expected values. The quote checker passes apart from two p-values printed in forms it doesn't know ("9.0e-4" in fig. S2E and "2.0 × 10 −4" in Fig. 4I); I read both in the text and they are correct. Nothing is committed.

**Text read:** the version of record (Sci Adv 12, eaef0343, Europe PMC PMC13544205): main text, figure legends, Materials and Methods, and the supplement (legends of figs. S1 to S9; the supplement has no tables). The bioRxiv preprint the dandiset names was in `paper/` but I didn't use it for claims. Nothing the claims needed was missing.

**Code read:** github.com/XieLuanLab/icms-activation-plasticity at commit d1922d1. Its figure scripts read the paper's Zenodo source tables, not the NWB files. It doesn't compute the Fig. 3B counts, the Fig. 2A exponential fit (so that fit isn't tested), or the delta-spikes values and hit and miss firing-rate traces of Fig. 6.

**Coverage:**
- **Behaviour:** detection thresholds, response times, wheel-movement onset.
- **Volumetric imaging:** neuron counts, density, activation radius, at fixed currents and at threshold, and in controls.
- **Cell tracking:** tracked-cell counts, the high-intensity subgroup and its deconvolved spikes, Fig. 3N, the five-frame control.
- **Ephys:** unit counts, waveform separation, modulation and latency for all units, for pyramidal cells and interneurons, and for pulse-locked (PL) and non-pulse-locked (NPL) units. Also pulse-locking stability across currents, cell type by PL status, conduction velocity, peak spike probability, the 120 ms window, controls, tracked units, KL divergence, the hit-miss cluster test and population coupling.

**Settled by the code where the Methods are silent:**
- **Weeks:** week is ceil(days since the animal's first session / 7); early is weeks 0 and 1, late is weeks 2 to 4.
- **Thresholds:** fitted with psignifit (cumulative Gaussian, YesNo), catch trials entered as a 0 µA point.
- **Response filters:** at least 5 recording days per channel, more than 5 trials, a z-score cap.
- **Time to maximum firing rate:** 10 ms bins, Gaussian sigma 20 ms.
- **Pulse-locking index:** its definition, and a null of 100 uniform-random surrogates.
- **KL divergence:** bootstrap settings, and FDR families.
- **Cluster test:** the permutation procedure.
- **Population coupling:** pooled over 4 to 6 µA.
- **Effect size r:** |Z|/√N in MATLAB, rank-biserial in Python.

**Methods and code disagree; the Methods are followed and the code's choice is a variant:**
- **Volumetric activation:** fixed 2 × baseline STD against the code's adaptive per-channel multiplier on trial-averaged data.
- **Bootstrap for Fig. 5C:** 5000 against the code's 500.
- **Sidedness:** the legends say two-sided; `stats_table.py` runs one-sided tests.

**Details left open, with the readings named:**
- **Fig. 2C:** unit of observation is channel × week medians (code) or channel × session values (legend).
- **Fig. 2E:** five mice (code leaves out Mouse 5) or six (legend).
- **Fig. 2B:** the example animal, channel and session aren't named; every animal and channel is tried.
- **Planar activation:** threshold is mean + 2 STD (Methods) or 2 × CV (code).
- **Fig. 3B:** what counts as a tracked neuron, and how activation is counted; the code doesn't compute these counts.
- **Stable tracked cells (n = 226):** activated in all sessions or all but one (text) or in more than N sessions (code).
- **High-intensity subgroup:** each response's last valid session (code) or week 4 (text); early and late samples as per-response phase means or pooled week values.
- **Fig. 3N:** the week-0 group is the subgroup (code) or all tracked neurons (legend).
- **Fig. 3I:** which threshold line.
- **Controls (fig. S2D and E):** the current and late weeks.
- **Fig. S3D:** what one value is (per channel-session or per response).
- **Unit counts:** unit-sessions or unique units.
- **Fig. 4D:** the scope of the PCA.
- **Conduction velocity:** which bins form the "monotonically increasing segment".
- **Fig. S5:** wheel threshold per animal or pooled.
- **120 ms window:** PL labels recomputed or kept from the 700 ms window.
- **Fig. S7 controls:** which currents.
- **Fig. S8:** waveform-distance ratio of means or medians.
- **KL divergence:** the figure script's parameters or the stats table's.
- **Fig. 6D:** bin width 10 or 5 ms; onset taken from the first or the last significant cluster. The tolerance is set to one 10 ms bin.

**Things a claim needed that the paper doesn't give:**
- The bin width and smoothing for the Fig. 6D firing-rate traces.
- How PL latency and jitter are defined for fig. S4.
- The currents used for the controls.

Several weaknesses in the code are noted in the criteria. The KL p-values come from bootstrap replicates used as samples, so their size scales with the number of draws; the criterion judges the medians. The tracked-cell matcher doesn't reliably pick the ROI with the largest overlap, and the Fig. 3N groups overlap. Whether the dataset holds the control animals, the imaging ROIs, the activation calls and the spike waveforms is left for the author to find; the claims that need them say so.
