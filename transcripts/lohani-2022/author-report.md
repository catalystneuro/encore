I finished steps 1 to 6 for dandiset 001172. The final notebook run passed `tools/entry.py all` in 716 s, and the handover is in `executed/001172-lohani-2022/handover/`. I used the paper's full text (the author manuscript, PMC10661869) and pinned version 0.260129.0829: it is the only published version, the paper cites none, and the draft holds the same 32 files.

**1. Outcomes per claim** (26 claims: 13 reproduced, 7 partially reproduced, 1 not reproduced, 5 blocked)

| Claim | Outcome |
|---|---|
| allen-parcel-link | partially reproduced |
| fig2a-r2-differs-across-areas, fig2b-ap-gradient-inverted, fig2c-face-best-predictor-ach, fig2c-face-best-predictor-calcium | reproduced |
| s7-face-onset-transients, s7-locomotion-onset-transients | partially reproduced (calcium above the paper's range) |
| s7-ach-transients-same-across-states, s7-ap-gradient-transients | reproduced |
| s7-calcium-transients-largest-at-locomotion | partially reproduced (larger in all 4 mice, p = 0.078) |
| fig3c-ach-sustained-face, fig3c-ach-locomotion-no-further-increase, fig3d-ach-frontal-above-visual | reproduced (3 mice) |
| fig3c-calcium-sustained, s7-ap-gradient-sustained | partially reproduced (3 mice) |
| the four Figure 4 correlation claims | reproduced (3 mice) |
| fig5-coupling-up-with-face | partially reproduced |
| fig5-coupling-down-frontal-with-locomotion | not reproduced |
| fig3b ECoG, fig3e pharmacology, s3 hemodynamic correction, s2 sensor validation, s8 cholinergic axons | blocked: data missing |

**2. What was found about the dandiset**
- **Missing data:** it holds 4 of the 6 mice in the paper's code (grabAM05 to 08), and no ECoG, drug sessions, control mice or ChAT mice. grabAM07 has no sustained high-face epochs, so the Figure 3c/3d/4/5 claims rest on 3 mice. One air-puff session has no Airpuff table, so I left it out.
- **ΔF/F timing:** the ΔF/F series start 49.9 s too early, because frame 0 is raw frame 499. The raw movies and the alignment of calcium with wheel speed both show this in every session.
- **Behaviour timestamps:** FaceMap and pupil timestamps are spaced 111 ms where the camera pulses are 100 ms apart, and the last two values wrap back to the first pulse. I timed frames by the camera pulses, as the paper's code does.
- **Parcellated series:** it is calcium but is linked to the ACh imaging plane, its masks are transposed, and its start time is 64.9 s early.
- **Descriptions:** the ΔF/F descriptions leave out the hemodynamic correction and atlas registration. The Allen parcels the paper analyses are not in the files; I took them from the paper's code.
- **Tables and units:** the visual stimulus table's columns are shifted by one. The Airpuff tables appear to hold only the puffs without running. Wheel speed and pupil area have unit "unknown".

**3. Where the protocol was unclear, wrong or missing something**
1. My link-claim criterion turned out ambiguous after the analysis: "non-zero pixels in the blue and green movies" can be read per movie or per session. One movie fails the 99.9% bar by 0.3 points, because 263 saturated pixels are zero throughout. Read per movie, the link fails, and the protocol would then block all 21 dependent claims. The protocol has no rule for this case. I chose the per-session reading after seeing the result, and recorded it as a deviation with both readings shown.
2. Parcel masks map pixels to areas but bring no measurements; `with_labels` covers names for codes, not this exactly. I used `with_labels` plus a link claim.
3. With 4 mice the paper's signed-rank tests cannot reach p < 0.05 (the smallest possible p is 0.125). The protocol has no guidance; I fixed "direction in every mouse" in the criteria before the analysis.
4. "Use the paper's own uncertainty" is unclear when the paper gives mean ± SEM. I used one SEM as the tolerance.
5. There is no rule for leaving out a session whose event table is missing, or for how few mice is too few. I left the session out and tested with 3 mice, recording both.
6. The protocol says to trust the data over metadata, but not whose timing convention to use once the file times are shown to be wrong. I followed the paper's code.
7. The 10-minute target cannot hold here: the analysis streams about 85 GB, so the notebook takes about 12 minutes.

**4. Runtime and what failed**
- The notebook takes 712 to 716 s. The whole author run took about 1 h 20 min.
- One development run failed because the helper module was missing from the scratch directory; I fixed that and reran.
- A permission request to delete an empty harness directory, `entries/001172-lohani-2022/.claude/.cc-writes`, was denied. Git will not commit an empty directory.
- Sandbox placeholder files (`.bashrc`, `.mcp.json`, `scripts`, `.idea` and others) show as untracked at the repo root. I did not create them, and the workflow commit should leave them out.
