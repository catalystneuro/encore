I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all entries/001751-liu-2026`: 0 check errors, and the notebook passes in 209 s. All conclusions, notes and the summary now match the new outputs, and round 1 is recorded under `verifications` for all 35 claims.

**Outcome changes**
- **fig5-ven-outputs-absent**: changed from not reproduced to partially reproduced, as the verifier gave it. VENs have no connections to VENs (0 of 59) or to interneurons (0 of 54), but the code table annotates one VEN-to-PC connection, so the claim holds for two of its three partner classes.
- **Kept, with the disagreement recorded:**
  - **fig4d-sodium-current** stays reproduced, still marked as resting on an assumption. I took the peak after a 1 kHz low-pass, which matches the paper's code's own per-patch values (r = 0.99). With it, p = 0.0010 whichever peak window is used, and any filter from 500 Hz to 2 kHz gives p ≤ 0.004. Only the unfiltered peaks split on the window, and that split is what the verifier's partially reproduced rests on.
  - **fig8a-metabolite-gradient** stays partially reproduced (the verifier would give not reproduced). The claim's pattern holds under every reading: more metabolites differ between AIC and V1 than between AIC and parietal cortex. The AIC-V1 count misses its tolerance under every reading.
  - **patchseq-mapping** stays blocked (the verifier would give partially reproduced). Every value that can be tested is within tolerance, and the fourth, the inhibitory-type count, is not in the saved results.

**Corrected or added**
- **Code table reading:** the file name is now filled only within each presynaptic block. Of the 10 blocks with no file name, 8 are matched to a file by the channel that fires. The other 2 (13 rows, no connections) have no file in the dandiset; they are left out of the counts and shown as a variant. The new numbers:
  - 1,403 linked pairs (1,416 with the unmatched rows), 298 cells, no duplicate pairs, 5 cells given two types, 5 files the table does not list.
  - PC-to-VEN pairs 139, PC-to-IN 83, Fig. 5i rates 2.42, 2.41, 0.72 and 4.65%.
  - None of these changes an outcome.
- **Firing-channel rule:** now follows the claim's criterion, excluding only empty channels; the extra −30 mV condition is shown as a variant. The table's presynaptic channel now fires in 294 of 296 files (289 under the stricter rule).
- **What the files hold:** every group and field of all 301 files and every electrode value are printed. The "no positions" result is now checked in the notebook instead of being printed as a fixed string. Electrode location reads "Soma" in every case.
- **fig8a and fig8de:** now tested on the MetaboLights MTBLS13927 deposit (revision 01, pinned by sha256). The deposit holds the same 558 metabolites as the code's table, so the 23 missing from the paper's 581 are not in it either. Recorded as findings, including two V1 sample labels swapped between the deposit and the code table.
- **Other outputs the verifier asked for:**
  - A flag for peaks on the first sample of the response window (likely artefacts).
  - Annotation checks: "Inh" connections from PCs, sign against peak, holding potential by connection type.
  - Responses on the channels named by the two mismatched projection labels.
  - The code notebook cell that names the clusters, and counts compared with their tolerances.
  - Header rows of the eEPSP and peak-index tables.
  - The Fig. 3e legend's group sizes: the table holds more cells than the paper analysed, for example 32 VENs against 22.
  - The 9-sweep file noted against the legend's "more than 20", and a statement that the two neuron counts disagree.
- **Question for a reader** in `questions/001751.yaml`: whether Supplementary Table 5 gives different pair and neuron counts. The claims affected say in their notes that it is asked.

**Not done**
- **fig5c:** the median reading of event amplitudes was not run, because it needs events detected again from DANDI:001752.
- **Supplementary Table 5:** I could not read it. The supplementary table PDFs have no extractable text and no renderer is available here, which is why it went to a reader as a question.
- **fig4j-eepsp-latency:** kept as blocked "other", not data_missing as the verifier wrote. The claim's data are in another archive, and the protocol does not allow data_missing for such a claim.

Nothing is committed or pushed.
