I wrote `claims/001444/10.1038-s41531-025-01070-4.yaml`. The quote checker passes: 40 claims, 40 quotes, 12 statistical values, 0 problems. Nothing is committed.

**Text read.** I used the version of record (npj Parkinson's Disease 11:230, 2025, from Europe PMC): main text, figure legends and Methods. Its title differs from the one in the task; it is the same DOI. The bioRxiv preprint was also supplied, but it is an earlier version with another title, so I took no claims from it. The supplement was not supplied (Supplementary Tables 1 to 3, Supplementary Figs. 1 to 5). I did not stop, because the main text reports every main result from one simulation set, sM1_12-12-2023.

**Code read.** The linked repository is `suny-downstate-medical-center/pd_m1_6ohda`, read at commit 0a1f0e8 (2025-08-20). It holds the NetPyNE simulation, the parameters for the four conditions, and four notebooks. The notebooks map the files -01 to -04 to control rest, parkinsonian rest, control activated and parkinsonian activated. They also show which LFP electrode and which five voltage traces the figures use. The repository has no analysis code: nothing for firing rates, statistical tests, CV, duty cycle, spectrograms, coincidences or unitary events.

**Claims.**
- 40 claims, all with quotes, none marked `inferred`.
- 12 claims carry statistics. Ten are firing-rate p-bounds, and the paper never names their test. Two are joint-surprise tests at p < 0.05.
- All 40 have a criterion, and 30 have expected values. Tolerances are 10%, except a count with zero tolerance, zero rates at ±0.05 (the paper's rounding), and "an order of magnitude" read as a ratio between 3.16 and 31.6.
- All claims use `data: dataset`.

**Details the paper leaves open, and the readings named:**
- **Rate test:** Wilcoxon signed-rank, paired t, Mann-Whitney U or Welch t. Pairing is possible because the four simulations of a set share the same seeds.
- **Rate population:** all neurons, or only neurons that spike.
- **Spectra:** NetPyNE's Morlet spectrogram or a short-time Fourier transform; electrode 0 (the one the notebooks plot) or the mean of the 11 electrodes.
- **Dominant frequency:** the peak searched above 0 Hz or above 5 Hz; the spike-count histogram decides, and the LFP is a variant.
- **CV:** window 2.0 to 4.3 s or the whole 4.3 s; neurons with at least one or at least two ISIs.
- **Duty cycle:** half-height from the whole window or from each period; window 0.25 s or 2.3 s.
- **Coincidence:** within ±1 ms or in the same 1 ms bin; window 2.0–4.3 s, 0.3–4.3 s or 0–4.0 s.
- **Unitary events:** 100 ms windows slid in 1 ms steps or non-overlapping; periodicity from the spectral peak or from the interval between peaks.
- **Bursts:** the paper defines none. The only reading the text offers is its own half-height convention. I flagged the 90% threshold for "continuous" 15 Hz power as my own choice, so it is reported but does not decide the outcome.
- **"Around 15 Hz":** the 15 Hz bin or 14 to 16 Hz.
- **Membrane potential:** the mean or the median of each trace.

**Missing or contradictory in the paper:**
- **Supplement:** Supplementary Table 2 holds the robustness results for the other three simulation sets, so `robustness-four-sets` is blocked until a reader with the supplement completes it. Supplementary Fig. 1 holds the current-injection protocol behind the 64% excitability decrease, so that claim is also unfixable.
- **No detection rule:** the paper gives none for subthreshold oscillations, so `control-subthreshold-oscillations` (57.4% of PT5B neurons) and `pd-no-subthreshold-oscillations` are blocked unless a question to a reader settles it.
- **Activated PT5B rate:** the Results report a significant increase in the parkinsonian condition (p < 0.001), but the Discussion says there was no significant change. The claim follows the Results.
- **Duty-cycle period:** the Methods define a period as running from the rising to the falling crossing, which would make every duty cycle 100%. I followed the Results, where a period runs from one rising crossing to the next.
- **Small mismatches:** IT2/3 activated rate is 6.7 in the legend and 6.6 in the text; the 10% tolerance covers both. In the code, NaT goes up 20-fold, while the Methods call it "a small increase".
