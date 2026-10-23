I wrote `claims/000015/10.1016-j.neuron.2017.05.005.yaml`, and `tools/claims_check.py` reports 0 problems. Nothing is committed.

**Text read:** the version of record (Neuron 94, 866–879), extracted from a PDF a person supplied. It has the main text, the legends of Figures 1–8 and the full STAR Methods. The Supplemental Information (Figures S1–S10 and a movie) is not there. I went ahead, as earlier readers did (e.g. 000009), because the main findings rest on Figures 2 and 4–8 and the Methods, all of which are in the text. The five claims on S1, S4, S5, S7 and S9 are written from the main text alone, and the file says so. I could not open any PDF page because the PDF renderer (poppler) is not installed here, so figures are read from their legends only. The paper links no analysis code, so none was read.

**Claims:** 31. All 31 have quotes and criteria; 1 has statistics: the bootstrap p < 0.01 for the PT-versus-IT onset difference of 1.4 ± 0.6 s. Two claims use the silicon-probe data, marked `elsewhere` at CRCNS doi:10.6080/K0S180F9, the deposit named in the Key Resources Table. One uses the Li et al. (2015) recordings (`with_inputs`); the paper does not say where those are deposited. The dandiset's metadata list two-photon imaging and behaviour from 6 mice.

**Details the paper leaves open, and the readings named:**
- **Time bins:** Figure 3B gives 66.7 ms bins, but imaging was at 14 Hz. Readings: frames as acquired, or resampled to 66.7 ms.
- **ALM/MM border:** the paper gives only the two area centres and a citation. Readings: the dataset's own area label, or the nearer centre. The paper's counts (8,837 ALM, 6,594 MM) check which is right.
- **Depth:** the Methods say deep is ≥ 350 µm, the Results say > 350. Figure 6 uses three bins instead: 100–250, 250–400 and 400–620 µm.
- **Neuron "distinguished trial types" (23% in MM, 31% in ALM):** the rule turning per-bin tests into a per-neuron call is not given. Readings: selective in ≥ 1 bin or ≥ 2 consecutive bins. Window readings: the Figure 8F task window, the whole extracted window, or trial start to 2.5 s after the go cue.
- **Onset (> 6 SD above baseline):** baseline readings are all bins before trial start, or the 0.5 s window used for F0.
- **Figure 6 "appeared first":** no onset measure is defined. Readings: onset of the selective fraction, or of mean |β|.
- **PT-versus-IT onset:** the IT group is open (deep ALM IT, or all ALM IT), and so is the bootstrap (hierarchical as in Figure 8D, or over cells).
- **Variance explained (Figure 8F):** for area and depth, the neurons are open: the three labelled mice, or all six.
- **Electrophysiology epoch selectivity:** readings are any window inside the epoch, a window centred in the epoch, or a whole-epoch count. Response-epoch length readings are 1.2 s or 2.5 s, and units are either all units or putative pyramidal units only.
- **Means of trial counts, early-lick rate and percent correct:** each could be taken per plane, per session, per mouse or pooled.
- **Sign convention:** the Results call CR and EL "lick left trials", but the Methods and the trial names say lick right; I followed the Methods.

**Measures I fixed myself:** for about 12 qualitative claims ("mainly in MM", "approximately uniformly", "outnumbered", "similar whisking", the 2-bootstrap-SD sign tests) the paper gives no test, so I set the measure and threshold. Each criterion says so. The second reader should look at these first, because the protocol says no outcome may rest on an agent's choice.

**Missing from the paper that claims needed:**
- **Supplement:** Figures S1, S4, S5, S7 and S9 are not in the text.
- **Photoinhibition (S9):** its methods, sites and test are not described.
- **Bilateral wide-field imaging (S1):** the main text describes a window over the left cortex only.
- **Li et al. (2015) data:** no location is given for the recordings used in the comparison.
