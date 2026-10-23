I wrote `claims/000673/10.1038-s41586-024-07309-z.yaml`. The quote checker passes with 0 problems: 56 claims, 56 quotes, 113 statistical values found in the text. Nothing is committed.

**Text read.** The version of record (open access) from Europe PMC (PMC11078732), including Results, Methods, figure legends and all nine Extended Data legends. The Supplementary Information was also there: Tables S1–S5 and the Supplementary Discussion. The Peer Review File came through; the Reporting Summary came through empty, and no claim rests on it. Supplementary Table S4's model formula is garbled in the text. Its rows survive and were used, so nothing needed for a claim is missing.

**Code read.** github.com/rutishauserlab/SBCAT-release-NWB at commit a25e8cc3. It is sample code: behaviour metrics, category-cell selection, the LFP phase–amplitude coupling (PAC) comodulogram, the PAC-neuron GLMs for one example neuron, and a simulation of signal and noise axes. It settles several details:
- the category-selection windows and tests;
- the theta and high-gamma frequency bins;
- how PAC neurons are binned and their GLMs fitted;
- RT as the per-session median of correct trials.

It has no code for single-trial PAC, the mixed-effects GLMs, spike-field coherence (SFC), noise correlations on the data, decoding, or cluster statistics.

**Counts.** 56 claims, all with quotes and none inferred. 49 claims carry statistics (113 entries), 52 have criteria and 16 have expected values. All use the dataset's own data; the paper names no outside data.

**Details left open, with the readings named for each:**
- **O1, LFP artefact rejection:** the visual-inspection step can't be repeated, and the span that gets z-scored isn't stated. Readings: the automated steps on the maintenance epochs, or on whole trials.
- **O2, equalising trial counts between loads:** random subsampling, so the seed is a standard choice.
- **O3, which frequency bins form the bands:** settled by the code for high gamma; low gamma is read the same way.
- **O4, the null for the proportion of PAC channels:** one reading is named.
- **O5, single-trial PAC:** not defined in the paper. Readings: raw per-trial modulation index, or the same z-scored within channel.
- **O6, firing-rate units in the tests:** rate in Hz, or percentage change from baseline.
- **O7, minimum incorrect trials per neuron:** at least 1, 2 or 3.
- **O8, size of the SFC surrogate jitter:** spikes redrawn uniformly within the window, or jittered by ±250 ms.
- **O9, scope of the FDR correction in PAC-neuron selection:** per area and load, or per neuron.
- **O10, averaging of noise correlations:** over all trials, or within conditions and then across them.
- **O11, decoding:** intact and shuffled ensembles built separately, or the intact order reused. The Fig. 6c gain measure is taken from the paper's reference 36.

**Open details within single claims:**
- which trials enter the correct-vs-incorrect test and the PAC–firing GLM;
- the slow and fast theta bands of Table S1;
- the test for overlap between PAC and category neurons;
- the encoding presentations used for the Extended Data Fig. 7a decoding;
- the spectral-slope frequency range;
- the n:m ratio for phase–phase coupling;
- the spike minimum for the RT test of cross-regional SFC.

The cluster-forming threshold isn't stated, so FieldTrip's defaults are used, following the paper's citation of FieldTrip.

**Missing from the paper:** nothing a claim needed is absent. The one gap is that the paper never says how single-trial PAC is computed, which affects 3 claims (Fig. 2f, 3h and 4c); readings are named for it.
