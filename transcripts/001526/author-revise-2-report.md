No outcome changed. The verifier agreed with all 30 outcomes in round 2 (1 reproduced, 2 partially reproduced, 2 not reproduced, 25 blocked), and I found nothing that should change, so there are no `proposed` entries. The final `python tools/entry.py all` passed (836 s) and `check` reports 0 errors. Nothing is committed.

**Why many of the flagged numbers were already correct.** I re-ran the entry and it printed exactly the figures the text already gave: subsets meeting fig2d 2 and all three claims 1; p = 0.019 and 0.094; p = 0.026; 32.4 and 33.3% with p = 0.051 and 0.109; 2.3%; per-cell-angle p = 0.080 and 0.028; annulus p = 0.045; within-set change 1.15%. The verifier's copy was executed separately and differs in the third decimal. The likely cause is float32 sums rounding differently on another CPU, which can move a traced edge by one sampling step; I could not confirm this with only one machine. I switched `strobe.py` to float64, and on this machine the printed values stayed the same. The round-2 record explains this.

**Corrections the verifier was right about:**
- **Smallest p without c3 and c4:** 0.066 is now 0.067, in the notebook and the record.
- **Background deviation:** the paper's values are about 3 times the unsubtracted readings, not 2.5 (40/13.3 = 3.0, 26.6/8.5 = 3.1). Fixed on all four tested claims.
- **`evaluate()`:** it now labels fig2d "partial" only as the criterion words it. A size within tolerance alongside a pre-exposure set that differs is counted separately: 16 of the 165 subsets under the background recording. The reproduced counts are unchanged.

**Added in reply to the open points:**
- **Background reading chosen after the results:** the record, notebook, summary and README now say plainly that the background recording was adopted after results under both readings were seen. That happened in the revision in which the annulus reading stopped meeting fig2c.
- **Camera offset:** if the darkest pixels are the true offset, fig2c is not met (start 24.0%) and fig2cd is not reproduced (p = 0.038). This is in the notes, the summary and the dark-frame finding.
- **Weak first-set cells:** c4, c8 and c10 have first 150 V/cm sets of only 3.4 to 3.8%, against later means of 5.0 to 15.3%, and c4 has the weakest response of the session. The fig2cd notes now say whether the right cells were picked is still open, and that the result rests on one uncorrected test of 12.
- **fig2d:** the notes now say the 18.7% reading meets neither clause of the criterion literally, and why "partial" is still the closer description.
- **fig4d:** I set `assumed` to false, since the outcome holds under every reading.
- **Round 2 record:** added under `verifications` for all 30 claims, with the verifier's reasons in its own words and my responses.

**Not done:**
- **Fig. 2D "≤20%" legend:** this point is already a question in `questions/001526.yaml`, so I added nothing.
- **Fig. 4D labels:** these remain unchecked by the verifier, which could not render the PDF; no outcome depends on them.
- **`provenance` run URL:** I left it as it was.
