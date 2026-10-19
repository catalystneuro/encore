**Verifier report, round 2: 000005-yu-2016-01 (doi:10.1038/nn.4412, DANDI 000005 0.220126.1853)**

I downloaded the supplement again, to `paper/nn.4412-S1.pdf`, and extracted its text to `paper/supplement_text.txt`. Counts below come from the claims file (8 claims) and the attempt record (8 outcomes: 5 reproduced, 2 not_reproduced, 1 blocked).

**1. Outcomes**

| Claim | Recorded | I agree? |
|---|---|---|
| vpm-touch | reproduced | Yes. Cell 27: 20 of 24 (0.83); 0.0 with spikes moved to the next trial. |
| vpm-whisking | reproduced | Yes. Cell 30: 21 of 24 (0.88) against a null of 0.12. |
| fs-touch-and-whisking | reproduced | Yes. Cell 33: 0.65 and 0.80, unchanged across tag thresholds; 0.81 and 0.81 without the flagged mice. |
| exc-mainly-touch | not_reproduced | Yes, by the criterion as written (cell 36: p = 0.074 and 0.090). It is weak: without the flagged mice it passes (p = 0.024 and 0.038, or 0.033 when they are also removed from FS). The record says this. |
| fs-suppress-movement-spiking | reproduced | Yes, but weak. Cell 39: 6 of 7, p = 0.016; without anm266945, 3 of 3, p = 0.125. |
| fs-enhance-touch-selectivity | not_reproduced | Yes. Cell 42: lower with light in 2 of 6, p = 0.953; also 14 of 30 in the juxtacellular variant. |
| thalamus-drives-fs | reproduced | Yes. Cell 45: 9 of 9, p = 0.00195; the whisking-period rate also falls in 9 of 9. |
| sensory-input-drives-fs | blocked, metadata_insufficient | Yes. Cell 5 prints the general/ and subject fields; there is no surgery, notes or lesion field and no keyword match. A small gap in that search is listed in section 3. |

**2. Text against the printed outputs**

Sentences the numbers do not support:
- **Cell 16:** "The 80 other cells …". Cell 15 prints 85 "other" cells (2+4+1+4+39+1+11+23), and 22 EXC + 23 FS + 85 = 130.
- **Cell 8:** "sampled at 10 kHz (5.5 s per trial) in files up to August 2015". Cell 7 prints "Last file at 10 kHz (session date): 20150320", and 29 of the 10 kHz files have 5.2 s trials.
- **Attempt record, sampling-rate finding:** "with trials of 5.5 and 5.9 s" leaves out the 29 files with 5.2 s trials (cell 7). The Summary's "up to March 2015" is correct.
- **Cell 25:** "With it, 9 whole-cell cells lack a touch input in these three mice". One of the 9 (anm318532, `vm_touch_n` 0) was never tested (cell 24), so 8 tested cells lack a touch input.
- **Summary, cell 51:** "it changes the result of `exc-mainly-touch`". The variant passes the criterion, but the result stays not reproduced.
- **Summary, cell 51:** "Cells from ION-transected mice … are mixed into both groups" is stated as fact. The data show only that inferred-transected mice contribute 3 EXC and 4 included FS cells (cells 24 and 33).
- **Cell 40 and the fs-suppress notes:** the juxtacellular variant ("24 of 32, p = 0.00042") is presented as support. Neither repeats the claims file's caveat that this selection "is biased toward a rise and does not decide the outcome".
- **Not shown by any output:** "the draft lists the same 148 assets and sizes" (cell 0); "5 s per trial" for the whisker variables (cell 10); and the README's "about four minutes" (only the 116 s load time is printed).

Everything else agrees with the outputs. That covers every "**Result:" conclusion (cells 28, 31, 34, 37, 40, 43, 46 and the cell 49 note) and the Summary table. It also covers the README claim table and data description, and every outcome note and number in the record.

I checked the figures quoted from the supplement against the text I downloaded, and they hold:
- 37 whole-cell L4 excitatory cells (Supp. Fig. 5; Supp. Table 2: 23+5+1+7+1).
- 9 whole-cell excitatory and 10 cell-attached FS cells from ION-cut mice; 38 of 42 cell-attached PV-Cre cells are L4E.
- 3 of 4 PV cells inhibited (Supp. Fig. 13a); a 100 Hz train of 5 ms pulses (Supp. Fig. 9i); an r² cut-off of 0.25.

**My round-1 reasons as recorded:** they are fair paraphrases of my own wording for all 8 claims. The fs-touch reason adds my problem-2 point about ION-cut and L5 cells, which is fair. The thalamus reason drops "6 cells from one [mouse]", which is trivial.

**3. Round-1 points**

Resolved:
- Point 1: the supplement is now read and used, and the reason for the blocked claim is corrected.
- Point 5: the null's excess rate is stated, and an L4 null was added (EXC 0.06, FS 0).
- Point 6: a variant without anm266945 and per-cell spike counts were added.
- Point 7: tag sites are printed, all "vS1" or "VPM and vS1".
- Point 8: an isolated-touch variant was added.
- Point 9: widths by sampling rate are printed.
- Section C items: metadata printed, tag table, example traces, a light-artifact check, behaviour with and without light, and PV-Cre spike counts.

Partly resolved; what remains that bears on a conclusion:
- **Problem 2 (ION-cut and L5 cells in the groups), exc-mainly-touch.** This cannot be fixed from the files. Of the paper's 10 ION-cut FS and 9 ION-cut excitatory cells, only the cells in the 4 flagged mice are found, and the flag was chosen after seeing the values. This is the main reason the not_reproduced outcome is fragile. It does not threaten fs-touch-and-whisking: removing 4 more unresponsive cells would still leave the touch fraction above 0.5.
- **Excitatory proxy purity, exc-mainly-touch.** Supp. Table 2 has 1 whole-cell FS cell in C57BL/6 mice, which cannot be tagged and may sit in the EXC group. The paper's example tagged FS cell is 0.31 ms wide at half height (Supp. Fig. 9g). Here the tagged whole-cell cells measure 0.38 to 0.61 ms, against an EXC cut-off of 0.6 ms. The 0.7 ms variant moves p to 0.112 and 0.126, so the outcome holds.
- **Problems 3 and 4 (selectivity on few spikes; inclusion of the higher-firing cells), exc-mainly-touch and fs-enhance-touch-selectivity.** These are now quantified and disclosed: 8 of 18 cells at 0 or 1; 0, 1 and 13 spikes at the floor in cell 42; the left-out cells fire a median of 1 spike. The measure itself is unchanged, so both outcomes rest on an index that is degenerate for these cells.
- **The metadata search in cell 5.** The keyword check covers only `session_description` and the electrode location. It does not cover `experiment_description`, `keywords` or the optogenetics descriptions. This is unlikely to change the blocked reason, but the check is not complete.
