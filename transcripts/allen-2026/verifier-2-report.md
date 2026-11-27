**Verification report, round 2: Allen, Yan, Kuan et al. 2026 (doi:10.1038/s42003-025-09506-6), Dryad rjdfn2zqz v439366**

The claims file has 31 claims, and the attempt record has 31 outcomes with the same IDs: 22 reproduced, 3 partially reproduced, 2 not reproduced, 4 blocked. These match my round-1 outcomes claim for claim.

### 1. Outcomes

I agree with all 31 stated outcomes. Comments:

- **fig4a-pca** is the only outcome with `assumed: true`. The assumption is stated in the deviation, the result text (cell 64) and a question to the authors. Reading the control "spread" as the range is reasonable: the paper says "significant divergence" on PC2, and 2 of the 3 chronic-OA samples lie inside the control PC2 range (control −0.72 to 28.91, chronic-OA 4.42, −7.30, 2.47; cell 63). The SD reading would also be defensible, and the record says so. One point the record leaves out: this criterion defines no "partially reproduced" condition, so calling the outcome partially reproduced under the range reading is a judgement. I accept it, because the variances, the acute-OA position and the PC1 separation all hold.
- **sfig3-prey-velocity-unchanged** (partially reproduced) and **fig2g-attack-willingness** (reproduced on the F2G counts) now match my round-1 view (cells 35–37 and 45–47).
- **rnaseq-assembly** is partially reproduced. Like fig4a, its criterion defines no partial condition, and the mapping rate is untestable. I agree.
- **fig4b-shared-down-sets** and **fig4fgh-chronic-up** are now reproduced under readings that the claims file added after this attempt's questions. The claims file shows the additions: reading (a) for fig4b and reading (b) for fig4fgh. Both follow the deposited script, and the record and notebook state what the outcome was before the additions (cells 73 and 86).

### 2. Sentences the printed outputs do not support

- **Cell 50:** "In control and acute-OA the ratio stays near 1 to 45 or 50 Hz and falls to 0.28 to 0.51 above 50 Hz". Cell 49 shows acute-OA at 1.062 at 57.5 Hz.
- **Cell 50:** "Their SD is 0 or missing, so every squid's peak fell in the same bin". For control at 10–40 Hz every SD is missing (cell 49). A missing SD does not show that several squid shared a bin, and cell 49 itself prints "SD missing where only one squid?". The fig3c notes in the record then use the opposite inference ("fails partly on single-squid means (rows without an SD)") while also saying "The file gives no n per mean". Neither inference is shown, and they contradict each other.
- **Cell 67:** "Its distances are about 2.5 times larger because it is computed on `vst`, a VST whose lowest value is 0.005 ... so that low counts spread further". From cell 66 the ratios are 2.54 (acute to control), 2.09 (chronic to control) and 2.31 (control to control). The causal explanation is never tested. The sfig5b notes in the record repeat it ("its distances are larger because vst has a lowest value of 0.005").
- **Cell 93 (Summary):** "the Welch W for pH and PCO2 ... differ from those Supplementary Table 2 prints". The [HCO3-] W differs as well: 42.839 against 39.545 (cell 20).
- **Cell 93 (Summary):** the "What was found about the dataset" paragraph leaves out the count-matrix column shift, which is critical finding 1. The README and the record include it.
- **Finding 1:** "the expression filter gives 67,088 or 66,006". No cell prints 67,088. 66,006 is printed in cell 59 for the "first header names" reading, not the read.csv reading.
- **Finding 1 and README:** "mislabelled when read as the authors' script reads it (read.csv with row.names = 1)". No cell prints the script line. The read.csv behaviour is emulated in `squidoa.read_count_matrix("r")`, not shown from the Rmd.
- **fig1e notes:** "Fold changes and tests are the same under either scale". No test is run on the formula-scale values. Cell 11 shows that the ratio between the two scales varies from 9.997 to 10.049, so they are nearly the same, not identical.
- **fig2d (cell 32 and record):** the figure tables "hold one row per squid in parallel". That the rows of F2D and F2C line up is assumed. Cell 30 shows only that one acute-OA row has a zone value and no distance, and that this value equals the squid left out. The choice is plausible but rests on that assumption, and the text should say so.
- **README:** "It takes about a minute". Cell 94 prints 111 s.
- **Cell 12:** "fall by 0.25 to 0.9 mmol/l" is loose. Cell 11 gives drops of 0.30, 0.45 and 0.78.

Every other "**Result:**" sentence and record note I checked matches the outputs (cells 14–92).

The verifications block states my round-1 reasons accurately and close to my own wording, and each of my problems 1–11 is attached to the right claim. One item from my section C is missing: the fig2g question of whether the workspace holds a per-squid source for the 11 missing chronic-OA squid. In practice the workspace listing in cell 9 answers it, since no object there holds per-squid prey-capture data.

### 3. Round-1 points

**Resolved:**
- 1: the agreement-not-recomputation statement is in place, and cell 69 shows matching designs, counts and size factors (difference 1.1e-15).
- 2: cells 46–47.
- 4: cells 35–37.
- 5: cell 30.
- 6: cell 20 prints p = 0.0217.
- 7: cell 11.
- 9: cell 60.
- 10: cell 0.
- 11: a batch-coding bug was found and corrected (cells 62–63).
- C, blocked claims: cell 9 lists every workspace object.
- C, DESeq2 provenance: cell 69.

**Remaining, bearing on a conclusion:**
- **fig4a:** the outcome depends on the undefined "spread", and the criterion has no partial condition. This is a question for the reader. The analysis handles it correctly.
- **fig3c:** the n per mean cannot be checked, and the cell 50 inferences quoted above need correcting. The outcome stands either way, because acute-OA fails at 57.5 Hz (1.062) and chronic-OA fails at 47 Hz (1.039), which is not just bin quantization.
- **GSEA claims (fig4b to optic-lobe-no-ion-regulation):** these still rest on the authors' saved results. This is disclosed and cannot be fixed in this environment.

**Remaining, not bearing on a conclusion:** the wording problems in section 2 (cells 50, 67, 93, finding 1, README).

### 4. Critical findings

- **Finding 1 (count-matrix columns), cell 58.** Cell 58 shows a 16-name header against 15 values per row. Value columns 2–15 equal workspace samples Ct_8.1_1 to Re_8.1_2, and Re_8.1_3 has no match. That value column 1 is the gill sample is inferred from its header position: the output shows only that it matches no workspace sample. The shifted labels under the read.csv naming are shown, through the helper's emulation. The filter counts are not in cell 58: 66,006 is in cell 59 and 67,088 is printed nowhere. `critical` is right: a gill sample gets labelled as a control optic lobe, and a standard reader shifts the names silently. No `versions` or `fixed_in` given.
- **Finding 2 (prey shrimp duplicate column), cell 45.** Cell 45 prints "identical: True" for the two 10–20 min columns, with 8 values each, while the legend gives 11 CO2 shrimp. Cells 3 and 9 support "only copy". `critical` is right: control values are filed under the CO2 label with nothing marking it, and a two-way ANOVA that takes them as given builds in "no effect". This is the same kind of problem as one recording deposited as two. No `versions` or `fixed_in` given.
