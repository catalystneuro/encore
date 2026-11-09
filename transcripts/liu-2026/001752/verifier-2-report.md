**Verifier report, round 2: Liu et al. 2026, DANDI:001752 (0.260825.0222)**

I read the re-executed notebooks (`reproduce_liu_2026.ipynb` and `elsewhere_liu_2026.ipynb`), the README, the claims file and the attempt record. I did not re-run anything. The claims file has 34 claims, and the record gives an outcome for each: 9 reproduced, 7 partially reproduced, 4 not reproduced and 14 blocked. Nine are the dandiset's claims.

### 1. Outcomes

**The dandiset's claims**

| claim | agree? | comment |
|---|---|---|
| psc-file-labels-link: partially_reproduced | yes | Several parts fail (cells 15, 17, 18, 20). |
| fig5b-sepsc-frequency: blocked | yes, by the criterion | The two readings disagree: at 5 pA p = 0.026, at RMS VENs are higher (cell 27). Reading (b) is the claims file's misreading (see section 3). On 5 pA alone the result would hold, including in the files with noise below 2 pA (p = 0.038, 6 VENs against 4 PCs), though only weakly (p = 0.062 after the opposite-polarity rate is subtracted). |
| fig5b-sipsc-frequency: not_reproduced | it follows the criterion, but the evidence does not support it | Both readings put VENs higher, so the criterion gives not reproduced. But the record's own last finding says the sIPSC frequencies "cannot be measured from these files without the paper's detection settings". The record cannot hold both: if the measurement is invalid, the outcome is closer to blocked (methods_underspecified). |
| fig5b-mepsc-frequency: not_reproduced | yes | Detection is sound here: all files have noise below 2 pA and 94% of injected events are recovered. Neither labelling gives a significant difference (p = 0.61, cell 33). |
| fig5b-mipsc-frequency: blocked | yes, by the criterion | At 5 pA p = 0.0074, which holds in the files with noise below 2 pA (p = 0.0026). At RMS p = 0.24 (cell 36). The block comes only from reading (b). |
| fig5c-sepsc-amplitude: reproduced | yes, fragile | The deciding test gives p = 0.24. The RMS, 30 s and 3×RMS variants all give p < 0.05, VENs smaller (cell 39). |
| fig5c-sipsc-amplitude: reproduced | **no longer** | The record says "the detection does not measure the paper's amplitudes in these recordings". No file has noise below 2 pA, and the amplitudes here are 0.21–0.40× the sheet's (cells 18, 43). A claim of absence cannot be reproduced by a measurement the attempt itself calls invalid. I agreed in round 1, but the new detector check changes my view. |
| fig5c-mepsc-amplitude: reproduced | yes | p = 0.61 under both labellings (cell 45). |
| fig5c-mipsc-amplitude: reproduced | yes | p = 0.46 (cell 48). |

**Claims whose data are elsewhere**

- **I agree with:** ven-map-et-ct, fig3e, fig4j-eepsp-amplitude, fig5-connectivity-total (partial), fig8a (not reproduced), fig8de (partial), fig2d-f (not reproduced), ven-subtypes-similar-physiology (partial), fig6-ven-subtype-morphology (partial) and fig6f-g (partial).
  - fig5-connectivity-by-type is now blocked, which is what its criterion says when the deposit has no annotation.
  - fig6f-g: no reading matches both counts, but the qualitative split holds.
- **patchseq-mapping (assumed: true).** The assumption is stated in the deviations and in cell 8, and it is reasonable: the 33 cells are exactly those the code labels as interneurons (cell 2 crosstab).
- **fig4d-sodium-current (reproduced).** This outcome rests on an assumption that is not flagged. The criterion defines reading (b) as current divided by an area taken from each patch's capacitance. The files hold no capacitance, so (b) was replaced by a single constant area. The deviation states this, but the outcome should carry `assumed: true`, or say that reading (b) could not be formed.
- **fig4ac-ap-width-amplitude (partially_reproduced).** I disagree. On the cells available, neither feature reaches the criterion's p < 0.001. Amplitude does not even reach p < 0.05 (p = 0.073), and with the L5-subclass PCs neither feature is significant (p = 0.22 and 0.35; cell 40). "Partially" rests on direction alone. Not reproduced on the deposited subset, with the subset limitation in the notes, would fit the evidence better.
- **The blocked claims:**
  - scRNA claims: too_large.
  - Model claims: not_runnable.
  - fig3c and fig4j-eepsp-latency: metadata_insufficient.
  - scrna-no-sex-difference and ven-firing-rate-variability: blocked by their criteria.

  All of these are reasonable.

### 2. Sentences the outputs do not support

- **Detector check overstated (main notebook cells 13 and 50, README).**
  - Cell 13 says that in noisier files "the opposite rate approaches or exceeds the forward one (sEPSC with noise of 2 to 4 pA, 7.3 against 13.2 Hz)… so most of what is detected there is noise".
  - Cell 50 says "in the noisier sEPSC files and in every sIPSC file the opposite-polarity peaks approach or exceed the events, so the 5 pA frequencies there are mostly noise".
  - The README says the detector "counts mostly noise in the others, every sIPSC file among them".
  - **The numbers:** in the 2–4 pA sEPSC files the opposite rate is about 55% of the forward rate (cell 12). Per file, in cell 20 it is 0.50–0.73 for 1n7bo55, 16olqir, 1u56rnh, wn6cw2, 15e3e16 and t0bi1r. Two sIPSC files are well below parity: w9b4ds (2.70 against 6.28 Hz) and 1tsbdsc (3.23 against 5.45).
  - The attempt record says the same about the link: "about as many opposite-polarity peaks as events". That holds for sIPSC and for the sEPSC files above about 5 pA, not for the 2–4 pA sEPSC files.
- **Wrong cell type for S02C0321 (attempt record, fig5b-mepsc-frequency deviation).** The deviation says "One VEN of the paper (sheet name S02C0321)". The sheet calls it a PC (cell 17: `sheet_type: PC`), as does the record's own link note. It is a VEN only under the table's flipped labels.
- **Elsewhere notebook, cell 15.** It says "The first cell reads every file of DANDI:001751". Cell 16 reads only the first file of each session ("files read: 56" of 301).
- **Elsewhere notebook, cell 39.** It says DANDI:001746 "holds 68 VENs and 145 L5 PCs". The output (cell 40), cell 41 and the record all give 135.
- **Elsewhere notebook, cell 38.** It says "the data do not support it at the paper's n". The resampling draws from the observed groups, so it assumes the observed difference is the true one. That estimates power; it does not show the data contradict the claim. The record's wording, "the absence holds here only for lack of power", is fine.
- **Everything else matches.** I checked every other number in the "Result" cells, both Summaries, the README and the record notes against the printed outputs.

**My round-1 reasons in the record.** They are stated faithfully and in substance as I gave them, including the figures (0.029/0.027, 1.40 against 1.97 Hz with p 0.032, ρ 0.22, 175–194). The record has no verification entry for fig4i, fig4g, fig4j-eepsp-latency or model-ven-fires-more. My round-1 report did not address those individually, so nothing is misattributed.

### 3. Round-1 points

**Resolved:**
- **2 (noise at 5 pA):** addressed with noise strata, an opposite-polarity null and injected events.
- **3 (mEPSC labels):** the group tests on the sheets' own values are now in cell 25.
- **4 (rank-sum method):** the notebook now uses `psc.ranksum`, exact as MATLAB's is.
- **5 (quality conditions):** shown as variants. The ±4 s.d. stability test is still not applied.
- **8 (link correlation depends on the detector):** the low-noise subset is now shown.
- **9 (fig2d-f extraction):** the extraction is revised, the old one is kept as a variant, and the outcome is unchanged.
- **10 (fig8a table):** now run on MetaboLights, which holds the same values.
- **11 (ven-subtypes power):** outcome changed to partially reproduced.
- **12 (fig5 connectivity):** the deposit was checked, though only one file per session; by-type is now blocked.
- **Blocked claims:** fig4ac, fig6 morphology and fig6f-g are now tested; fig3c is confirmed untestable.
- **6, 7 and 13:** these did not bear on a conclusion.

**Remaining points that bear on a conclusion:**
1. **Reading (b) of the threshold (round-1 point 1).** It is still in the claims file. The detector check confirms it counts noise in every experiment (opposite/forward median ratio 1.05, cell 12). The Methods say "The event detection threshold was set at the maximus root mean squared noise level (5 pA)", which gives one value, not a per-recording threshold. This reading alone blocks fig5b-sepsc and fig5b-mipsc. The author has sent a question to a reader, but it is not settled.
2. **sIPSC frequency and amplitude.** Both outcomes rest on a detection the record itself calls unmeasurable in these files. I recommend blocked (methods_underspecified) for both, or at least that the record reconcile its finding with the outcomes.
3. **fig4ac.** Partially reproduced is not supported by the criterion on the cells tested; see section 1.
4. **fig4d.** The outcome rests on an assumption without `assumed: true`; see section 1.

**Minor points, not affecting an outcome:**
- **Multi-patch annotation:** cell 19 shows inconsistencies the record does not mention.
  - 7 PC→PC connections are typed "Inh".
  - Two rows' `projection` disagrees with their channels: row 368 gives channels 4→1 against "4→3", and row 1310 gives 6→3 against "8→5".
- **Elsewhere notebook, cell 32:** it has 464 tau values for 462 cells, which suggests duplicated rows after the merge. It cannot be traced from the output and could shift the fig4ac and VEN-subtype counts by a cell or two.
