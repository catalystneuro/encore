**1. Outcomes and assumptions** (32 claims in the claims file, 32 outcomes in the record)

I agree with all 32 stated outcomes: 27 reproduced, 1 not_reproduced (ed1-monkey-d-no-change), 4 blocked (fig4c, fig5a-nonsurgical, fig6d, fig6e).

No outcome carries `assumed: true`. fig4b's earlier assumption was correctly dropped after the reader's answer. Five reproduced outcomes do rest on an unstated assumption, though:
- **Affected claims:** fig5a-pre-scc-connectivity, fig5b-scc-decreases, fig5b-scc-increases, ed9-control-hemisphere-changes and ed7-decreases-both-monkeys.
- **Why:** their criteria require the result "under both/every seed-map reading" (per-run and concatenated). Only one version of the seed maps is deposited, so only one reading can be run. The fig5c-* criteria ("all readings") are covered too, if the header's run readings apply to them.
- **What is missing:** the record lists this as a deviation but does not mark these outcomes `assumed: true`. The assumption is that the deposited maps are the ones the paper analysed.
- **Is it reasonable:** yes. The interaction F values match the paper exactly: 186.48 (cell 64), 51.09 (cell 79), 7.36 (cell 103) and 4.58 (cell 106). They should still be flagged and the assumption stated.

**2. Sentences the outputs do not support**

- **Cell 108 (Summary), Tukey-Kramer accuracy:** "agree with the reported ones to about the second digit down to about 1e-6" and "1.1 to 3 times the reported value between 1e-8 and 1e-11". The printed values do not fit either range:
  - Cell 64: HIP 1.34e-5 vs 1.19e-5 and AMY 8.8e-6 vs 7.70e-6, about 13% off, above 1e-6.
  - Cell 64: control MT 1.0e-6 vs 7.85e-7, 28% off.
  - Cell 64: PCC 4.5e-11 vs 8.22e-12, which is 5.5×.
  - Cell 106: monkey D's control insula 1.14e-11 vs 1.37e-12, which is 8.3×.
  - The fig5b deviation in the record says "1.1 to 3 times ... for example PCC 4.5e-11 against 8.22e-12", which contradicts itself. Cell 63 ("up to three times") has the same error.
  - This error started in my round-1 problem 2 and was carried into the record. No outcome depends on it; every affected P is far below 0.05.
- **Cell 22, and the record's ed1-monkey-d notes and response:** two statements go beyond what is printed.
  - "monkey D's rows (group 2) enter only the plotted means" is not shown. Cell 21 prints only script lines 10–20.
  - "The paper therefore ran no test for monkey D" goes further than those lines. They show that this ANOVA excludes group 2, not that the rest of the script runs no test on monkey D.
- **Record, fig6d notes:** "area 25 on the sham side, next to the lead". No output gives the lead location. Area 25 is also the seed ROI itself (claims header), so its rise is not evidence of the local increase at the implant site. The outcome stays blocked either way.
- **Everything else checks out.** I checked every other number in the "Result:" cells, the Summary, the README and the record's notes against the outputs, and found no other mismatch. That includes the ED6 legend values (paper text: 2.93/0.0899, 0.9611), the README's group counts (9+3+1+10+2+5+1+1 = 32) and the 0.3-min run time.
- **My round-1 reasons:** the record states them in my own words and faithfully. Section C notes were merged into the fig4c, fig5a-nonsurgical, fig6c and fig6d reasons, which is accurate. The fig5b reason repeats my "1.1 to 3×" error.

**3. Round-1 points**

Resolved:
- **Problem 1:** a reader is now asked about the LIM reading (b), and the record says the fig6e block does not rest on it.
- **Problems 3, 4 and 5:**
  - Problem 3: the "concatenated" inference was removed; cell 11 shows one value per voxel and session, and a methods_unavailable finding was added.
  - Problems 4 and 5: these needed no change and are recorded as findings.
- **Unchecked items from round 1:**
  - fig4c: cell 55 prints the script lines and the workbook's text cells; no network assignment exists.
  - fig6c: cell 97 shows the pairing of rows by section and field.
  - "concatenated": settled as far as the deposit allows.

Partly resolved:
- **Problem 2:** the limits of SciPy's far-tail P values are now stated, but with the wrong size of discrepancy (see 2).
- **Problem 6:** the script's ANOVA rows are now shown to exclude monkey D. The wider claim that the paper never tested D is not shown.

Remaining points that bear on a conclusion:
- **ed1-monkey-d-no-change:** the not_reproduced outcome is correct under the criterion. Its reading still depends on a test the paper is not shown to have run (claims file, open note). Printing the rest of the FigE1 script, or at least every line that uses group 2 or `mk == 3`, would settle it.
- **Missing `assumed: true`:** five or more seed-map outcomes should be flagged, as set out in section 1.
