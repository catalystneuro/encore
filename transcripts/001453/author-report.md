I did steps 1 to 6 of the protocol for dandiset 001453. The entry passes `entry.py all` with 0 errors and runs in 225 s, and the handover package is built. Of 20 claims, 6 were reproduced, 1 partially and 2 not, with 1 more reproduced (the link) and 10 blocked. Nothing was committed or pushed.

**Paper text:** I used the full text of the accepted author manuscript in PubMed Central (PMC12218792), saved under `paper/`. The published version itself is not open access.

**Version:** pinned 0.250518.1950, the only published version. The paper cites no DANDI version. The draft has the same 37 files and only adds metadata, as the notebook header explains.

**Outside inputs:** the stimulus codes have no names in the dandiset. The names come from the paper's analysis notebook on GitLab (commit 33a5c29) and the protocol file of its stimulus software, pandastim (commit 7d9d161). Claims that rely on them are marked "with inputs" and depend on a link claim.

### 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| stimulus-code-link | with inputs | reproduced (17 of 18 speed medians within 10% of the values the paper's code printed) |
| fig1d-dc-faster-all-codes | dandiset | reproduced (94.0 vs 55.2 px/s, p = 6e-18) |
| fig1d-median-velocity | with inputs | reproduced (9.87 and 6.41 vs 9.8 and 6.4 mm/s) |
| fig1d-zf-forward-faster-than-static | with inputs | reproduced (4.84 and 8.78 vs 5.0 and 8.8) |
| fig1d-dc-no-modulation | with inputs | not reproduced (3 DC pairs differ in the Tukey test, all involving "static") |
| fig1d-dc-faster-oblique | with inputs | reproduced under one of the two readings of "oblique" |
| fig1g-follow-direction | with inputs | partially reproduced (holds for zebrafish, p = 1e-6; not for Danionella, p = 0.15) |
| fig1h-zf-higher-angular-acceleration | with inputs | not reproduced (by the Methods' definition Danionella are higher for all 9 stimuli) |
| figs1e-dc-respond-less-monocular | with inputs | reproduced (the lateral part only nominally) |
| fig1c-continuous-vs-bouts | dandiset | reproduced (0.31 vs 0.91, p = 5e-5) |
| fig1cef-representative-values | dandiset | blocked: metadata_insufficient |
| 9 claims on imaging and head-fixed tail tracking (Figures 2 to 4) | dandiset | blocked: data_missing |

### 2. What was found about the dandiset

- **Missing data:** it holds only the freely swimming tracking behind Figure 1 and Figure S1. The paper's GitLab "data" repository holds notebooks only.
- **Fish count:** 25 zebrafish (the paper says 26; the paper's code and the dandiset both have 25) and 12 Danionella.
- **Subject IDs:** IDs 0 to 11 are each reused for one fish of each species. The archive summary says 25 subjects and lists only zebrafish.
- **Stimulus codes:** codes 0 to 20 have no names. The paper's code and the stimulus software swap codes 9 and 11 (lateral right and left).
- **Wrong units:** `f0_vtheta` is per frame, not radians/s, and `f0_vx`/`f0_vy` are per frame, not pixels/s.
- **Frame rates:** 18 of 25 zebrafish files and 1 Danionella file are sampled at 32 to 35 Hz. The Methods say above 150 Hz.
- **Spatial scale:** none is given. Positions fit the code's 10 px per mm, except one Danionella file (sub-5) whose positions reach 1490 px.
- **Export differences:** the two species were exported differently. Danionella files hold only trial frames plus an extra `dist` series.
- **Code bug behind Figure 1H:** the code divides each frame's heading change by the file's mean frame interval. In Danionella files that interval includes the gaps between trials (8.7 times the frame interval), so only this quantity shows zebrafish higher.
- **Code test mismatch:** the code runs a Kolmogorov-Smirnov test where the paper states Kruskal-Wallis, and its loop tests the same stimulus nine times.
- **Selection:** the dandiset holds only the fish kept after exclusion, without saying so.
- **No duplicate recordings.**

### 3. Where the protocol was unclear, wrong or missing something

1. **Labels as outside data.** The code-to-name table is a label, not data, yet without it nearly every claim needs outside input. I treated it as an outside input, marked 7 claims "with inputs", and made a link claim.
2. **No identifier for a link claim.** The protocol expects records to be matched by an identifier, but fish can't be matched here. I matched stimulus codes by integer and compared the per-stimulus medians with the paper's printed code outputs.
3. **Clock check doesn't fit.** Labels sit on the same timestamps as positions, so they share a clock by construction. I used a turning contrast over time with true and shifted labels. It supports zebrafish; for Danionella it could not establish the timing, and I said so.
4. **Several conflicting sources.** The Methods, the analysis code and the stimulus software disagree with each other (Figure 1H quantity, codes 9 and 11, the test used). The protocol's rule covers only Methods versus code. I followed the Methods for the main result where it is explicit and the figure code otherwise, and showed the others as variants.
5. **Absence claim that mixes conditions.** The paper's test for "DC lack modulation" includes the static condition, which is not a direction. I judged it as written (not reproduced) and showed directions-only as a variant, where no DC pair differs.
6. **Representative-trial numbers.** The protocol has no category for these. I blocked them as metadata_insufficient.
7. **Choosing the `measured` value.** When every reading matches, the protocol doesn't say which to record. I recorded reading (b) and listed all four in the notes.
8. **Stale example entry.** The example entry is from protocol pilot-0 (no `data`, `inputs` or provenance fields), so I took field names from `schemas/` instead.

### 4. Runtime and failures

- **Runtime:** the notebook takes 225 s, about 190 s of it streaming the files. The whole session took about 1.5 hours.
- **Failures:** Europe PMC returned HTTP 500 and the NCBI BioC API returned 429, so I fetched the paper through NCBI efetch.
- **Odd files in `git status`:** it lists `.bashrc`, `.mcp.json`, `scripts` and similar at the repo root. These are `/dev/null` placeholders the sandbox mounts, not files I created; the workflow should not commit them.
