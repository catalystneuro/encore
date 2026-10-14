No outcome changed. The verifier agreed with every outcome in round 1, and the re-run with `python tools/entry.py all entries/000625-geiller-2020` passed (0 errors, 452 s). Every number I checked in the new output matches the conclusions. Nothing is committed.

**Added or corrected**
- **Depth and coordinates (fig1-depth, fig2d, s3):** the data check now prints the file layout the verifier asked for. ROI masks have only x, y and a weight, with no z. They are laid out as the 231 cropped frames side by side, so they give no position in the field of view. The imaging plane's origin (0, 0) and grid spacing (50 µm) are placeholders, and there are no reference images. The blocked notes now say this, and I added a finding.
- **Behaviour (fig6):** the full list of acquisition and behaviour series is printed. The files hold only reward and water intervals and no lick record.
- **Session order (s6):** the session IDs and start times put the sessions in different orders, and nothing else in the files dates them (raw image series all start at 0 s, all files were created 2023-11-13). This is now in the data check, the s6 section, a deviation and a finding.
- **Frame-rate fit:** the best score more than 0.1 Hz from the fitted rate is clearly lower in every session (0.51, 0.39, 0.52 against 0.80, 0.72, 0.87), so the fitted rate is unique in the range searched.
- **fig2c-most-positive:** added a per-ROI table of r in each session. The sign changes between sessions in 17 of the 74 subtyped ROIs, 7 of them CCKC. This explains why averaging over sessions makes the all-ROI reading fail. The notes now also say the 0.095 result sits near the edge of its range.
- **s2-lags:** added a variant keeping only ROIs whose sign is the same in every session. It leaves just 1 negatively correlated ROI, too few to test.
- **s2-cck-run-stop:** added per-session means. CCKC give -0.005, 0.024 and -0.023, while every other subtype falls in every session.
- **fig4-fraction-negative:** I reported how the positive and negative field sets overlap and explained why they are coupled. On average 55.8% of ROIs are flagged both, 10.6% negative only and 13.9% positive only. The helper follows the paper's stated rule, so I left the code as it is. Counting negative-only ROIs gives 10.6%, which falls inside the paper's range. I chose that variant after seeing the result and it is not the paper's rule, so the outcome stays not reproduced; the notes say the 66.4% is not comparable to the paper's 12.7%.
- **Record:** round 1 is now under `verifications`, with all 26 claims, the verifier's reasons and my responses.
- **Paper:** saved the PMC7736348 text under `paper/`, which git ignores.

**Not done, and why**
- **fig4e-bic-recurrence:** I kept the reason as `other`, not the verifier's `data_missing`. The protocol gives "too few units under the claim's own rule" as an example of `other`, and the 3 BiC are in the data. The disagreement is recorded in the response.
- **Selection leakage in decoding:** not changed. It could only favour the claim, and the claim fails anyway.
- **Coupling in the place-field code:** not changed, because it is the paper's own rule (explained above).
- **Unexpected files:** untracked files such as `.bashrc`, `.idea` and `scripts/` appeared in the working tree. I did not create them and left them alone.
