I've revised the attempt for every round-1 point and re-run the entry. `python tools/entry.py all` passed (1789 s), the executed numbers match the conclusions, and `check` reports 0 errors. Nothing is committed.

**Outcomes:** none changed, but three now rest on different numbers.
- **fig2cd-nonelectroporating-stable:** kept as not reproduced. The verifier would give partially reproduced; I recorded that disagreement. The reason for keeping it is that the criterion has no partial case: any pre-exposure set that differs means not reproduced. Under the adopted reading 1 of 12 sets differs (p = 0.031).
- **fig2c-1000-within-set:** still reproduced, now 31.7% to 21.0% with p = 0.094. With c4 re-traced, the round-1 match under the annulus fails (p = 0.035).
- **fig2d-lasting-reduction:** still partially reproduced, measured value 27.24%. The verifier's "one literal pass" (annulus, anodic pole, 18.0%) drops to 17.4% with c4 re-traced, outside the tolerance.
- **fig4d-short-pulses-same-limit** stays not reproduced and **fig5b-eq2-sensitivity** stays partially reproduced. The 25 blocked claims are unchanged.
- I set `assumed: true` on fig2d and fig4d as well, since they also rest on the background reading and the choice of cells.

**Fixes and additions:**
- **Background reading:** I changed the adopted reading. It now subtracts each 2025-05-01 cell's own background recording; the files describe these as recordings "in the background region without cells". 2025-05-06 has no such recordings, so it keeps the annulus. I added a fourth reading that subtracts the darkest pixels, as a stand-in for the camera offset; there is no dark frame. The summary now says plainly that no single reading reproduces all three Fig. 2C/D claims.
- **Cell c4:** the new overlay of every traced membrane on its baseline image showed the verifier was right. The trace sat on internal staining (radius 21 px), not the membrane. c4 is now traced with an outermost-edge rule (34 px) and the overlay shows both traces. Applying that rule to every cell pulled other traces onto blebs, so only c4 uses it.
- **Cell selection:** the criteria are now applied without c4, without c3 and c4, without all four cells that break the protocol, and to all 165 ways of choosing 8 of the 11 cells. Without c3 and c4, all three Fig. 2C/D claims are met under the background-recording reading. Across the 165 choices, all three are met together in only 1.
- **Pole angles:** each cell's own pole angle is shown as a variant.
- **Fig. 4D labels:** I extracted the figure image from the PDF, which confirmed the labels used. Their non-proportionality to the volts is now recorded as a finding.
- **fig3-dye-slopes:** an exploratory Di-8-ANEPPS slope is added. It is 6.1 to 6.5% per 100 mV against 9.1 ± 0.91%, but it decides no outcome and the claim stays blocked, because the FluoVolt half has no data.
- **Question for a reader:** `questions/001526.yaml` now asks whether fig2d's tolerance should be one-sided, given the legend's "≤20%" (point 8). It cannot change this attempt's outcome.
- **Record:** I updated the findings, the README and the summary, set runtime to 35 min, and recorded round 1 under `verifications` for all 30 claims.

**Not done:**
- I made no change for points 6 and 7 (one pole angle per session, and points spaced by angle not arc length) beyond the per-cell variant. Both are stated deviations the verifier judged minor.
- c3's trace cuts inside the cell on one side, away from the poles. I noted this in the record and left it as is.
- I could not identify the paper's 8 cells or the camera offset from the data; both stay as questions for the paper's authors.
