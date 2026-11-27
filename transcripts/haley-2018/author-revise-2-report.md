No outcome changed in this round, and nothing is proposed for round 3. The verifier agreed with all 30 outcomes: 11 reproduced, 2 partially reproduced, 11 not reproduced and 6 blocked. I re-ran the entry with `python tools/entry.py all entries/haley-2018`. It passed with 0 check errors in 30.6 min, and its numbers match the conclusions and the record. Nothing is committed.

**Sentences corrected to match the printed numbers**
- **fig8b-cross:** 877_121's fraction at 5.5 is 0.40. The 0.59 in the notes was the value with PD bursting alone.
- **Finding 6:** the "0.62 within 5 ms" figure was never printed. It now cites the 1.00 match at a 38 ms lag, and the other channel's 0.13 against 0.15 by chance.
- **fig3a:** 887_005's 0 at 10.4 comes from filling a missing step with 0. The table now shows which preparations have a 10.4 file.
- **fig8b:** 877_141 is rhythmic for most of 5.5 (0.954), not all of it.
- **README and notebook:** the run time and data volume are corrected. The notebook now prints the 63.6 GB read in full alongside the time and peak memory.

**Outputs added**
- **Three more doubtful CG units:** the units the verifier named (887_127 CG1L, 897_041 CG1L, 887_005 CG2L) are now dropped as well, and the CG measures and Figure 8A are re-run on the 7 units left. Main outcomes stay as they are, but these variants now appear in the conclusions and notes:
  - fig7b would be partial without the original four units.
  - fig7d would be partial without all seven.
  - fig7c holds at 10.4 in both variants.
  - fig7e does not change.
  - fig8a fails the three t-tests in every variant. Its conclusion now also gives the ganglion-effect p-values the verifier raised (0.14 at gap factor 2, 0.061 at factor 5).
- **903_052 pH electrode:** a new tagged cell prints each PTX experiment's electrode slope. 903_052's electrode responds at -37.6 mV per pH unit, against -45.2 to -46.7 in the other eight, and its response is linear. This is now a new minor finding, number 13. The fig4a notes also say PD identity in that experiment's 6.7 file is not confirmed.
- **fig2a and fig6:** the notes now say the lvn condition changes the fraction rhythmic only in two preparations at 5.5, and that the fig6 unit was already counting 3.1 times the control height at the control before base.

**Findings**
- Finding 6 (PD and LP channel names swapped in 903_046_0002) is now `critical`, as the verifier rated it. It lists the version it was seen in. The live OSF listing shows no file changed since, so no `fixed_in` applies.
- The new findings entry is added at the end, so the existing numbers still point at the same findings.

Round 2 is recorded under `verifications`, with all 30 claims and the verifier's review of finding 6.

**Not done, and why**
- **Comparison of the state reading with Figure 8B:** it would need values read off the figure, and the entry may not embed numbers taken from a figure.
- **Trace overlays:** the entry has no plotting package. The height histograms and pdn matches already print what the overlays would show.
- **Gastric fallback:** still not attempted. The paper and its code give no threshold for rhythmic or alternating LG and DG bursting. The verifier called the block "arguable", and that disagreement is recorded.
- **Questions file:** I added nothing. The verifier raised no new misreading, and points 4 and 11 are already in `questions/haley-2018.yaml`.
