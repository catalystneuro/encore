I've updated `claims/gao-2018.yaml` to pilot-15. The quote checker passes: 46 claims, 46 quotes, 17 statistical values, 0 problems. Nothing is committed.

**Text read.** The stored text is now the version of record (PMC6212318, open access, Europe PMC XML). It holds the main text, the Methods, the legends of Extended Data Figs. 1 to 10, and the Supplementary Information, including Supplemental Table 1. The last file was written from the NIH author manuscript. `supp2.pdf` is the Nature reporting summary. The paper links no code. The reporting summary says scripts "will be deposited on CRCNS.org" but gives no identifier, so no code was read.

**Missing from the text.** The legends of main Figs. 1 to 4 are not in the stored text, and there is no PDF of the main paper. The previous file took several details from those legends, and I can't check them now:
- the significance marks of Fig. 1d, 1e, 1g and 1h;
- the Fig. 3f neuron count (n = 329) and the Fig. 2d count (197);
- the split of the 912 ALM neurons into fastigial and dentate sessions (446/466);
- the power ranges in the Fig. 3d and 4d legends.

I removed the statistics that came only from those legends (Fig. 1d, 1e, 1g delay, 1h response) and the n = 329 expected value. Where the paper gives no other threshold, the criteria now use the bootstrap at p < 0.05 (the lowest mark in the paper's bootstrap legends), named as a choice. Power ranges now cite the Methods and Extended Data Fig. 5e. If the main figure legends can be supplied, these details can go back in.

**What changed.**
- Every claim now has `datasets: ["000007", crcns-alm-4]`. The opening comment says which experiments each dataset is described as holding: ALM recordings only, with no CN recordings. Claims on the lesions, the CN recordings, the 1.3 s photostimulation, the movement tests, the VGAT behavior and the anatomy are kept; the author blocks them as data_missing if neither dataset has them. The comment also notes that the 6 mice of the 0.5 s fastigial photo-activation behavior are the 6 ALM-recording mice (Supplemental Table 1).
- New claim `ed10b-fastigial-activation-errors-during-recording`: performance drops during the ALM recording sessions (Extended Data Fig. 10b, p < 0.001, 6 mice). I moved that statistic off `ed10d`, where the test was not the finding.
- Sources now give main-text paragraph numbers counted from the opening paragraph. The old numbers were off.
- I removed the old `checks` block, because its "ready" verdict was for the previous version. The file needs a new check.

**Counts.** 46 claims, all with quotes and criteria. 12 claims have statistics (17 entries), and 17 have expected values.

**Details the paper leaves open, with the readings named:**
- **Response-epoch window for selectivity:** 1.3 s from the go cue, or 0 to 1.5 s.
- **Which trials enter selectivity:** correct trials only, or all trials with a lick grouped by instruction.
- **Which trials enter the photostimulation effect test:** all trials, or correct trials only.
- **Window that decides "modulated" for latency:** the photostimulation period, or the whole delay.
- **Lesion test:** mice pooled, or tested one by one.
- **Photostimulus for Fig. 1h, the Fig. 1g dentate bar, and delay photo-inhibition:** 0.455 or 0.5 s, against 1.3 s.
- **Lick bouts:** before against after the lesion, or contra- against ipsilesional.
- **Denominator for preparatory and peri-movement fractions:** all neurons, or selective neurons.
- **Population for the CN averages:** all selective neurons, or those selective in the sample or delay.
- **Lick-modulation t-test:** paired or unpaired.
- **Window for selectivity under photostimulation:** the whole delay, or its last 500 ms.
- **ALM mean-rate test:** all 454 neurons or the 197 modulated, and paired or unpaired.
- **ED10 VGAT percentages:** pooled over trials, or averaged over mice.
- **Comparison for the persistent fastigial effect:** the 1% chance rate, or the bins before the photostimulus.
- **"Collapse" along the coding direction:** not different from zero, or lower than control.
- **Captured fraction:** a ratio of RMS values, or of squared RMS values.

These are fixed as standard choices: the coding-direction trial split, the 200 ms averaging window, the baseline window, and the tests the paper doesn't give (per-mouse bias, the licking absence claims, the endpoint logistic regression).

**Other gaps.** The supplement presents the Extended Data Fig. 10c trials (bilateral ALM photo-inhibition) as an earlier finding citing Li et al. 2016 and Inagaki et al. 2017, so they may not be in either dataset. The paper doesn't say whether the ±3.4% and ±4.2% spreads on the coding-direction figures are s.e.m. or s.d.
