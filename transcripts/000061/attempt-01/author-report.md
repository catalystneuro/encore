I finished steps 1 to 6 of the protocol for dandiset 000061: claims, entry, attempt record and verifier handover. Four claims are reproduced, one is not, and one is blocked. The entry passes `check` and runs from a clean environment. Nothing is committed.

The paper is closed access (not in PubMed Central; the HAL record has metadata only), so I used the abstract alone, saved in `paper/`. Every claim is a sentence of the abstract and none has a reported number. I pinned version 0.250624.0426: the two published versions hold identical files and differ only in metadata the analysis does not use.

**1. Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| hpc-bla-reactivation-post-sleep | reproduced | 36 patterns in 15 sessions; post minus pre median 0.0119, 28 of 36 positive, p = 3.6e-05; median positive in all 3 rats |
| reactivation-peaks-at-ripples | reproduced | peak in the ripple bin, 4.4 times the flanks, p = 6e-06; reading (b) also holds, p = 0.0033 |
| bla-ripple-up-subgroup | reproduced | 103 of 822 BLA units (12.5%) against 0.7% chance |
| reactivation-involves-ripple-up-cells | reproduced | up-cells weigh more, 24 of 31 patterns, p = 0.0013 (not in Rat10, 1 of 3) |
| aversive-direction-stronger | not reproduced | median puff minus safe 0.0133, 9 of 15 sessions, p = 0.11; variants p = 0.048 to 0.45 |
| rats-learn-puff-location | blocked: data_missing | no position tracking |

**2. What I found about the dandiset**
- **Wrong time units:** the epochs table is in milliseconds though it says seconds (exactly 1000 times the session length in all 40 files). Video timestamps are also in milliseconds and are not on the session clock.
- **Broken spike index:** in 10 files the index between unit 0 and unit 1 is short by a multiple of 65536 spikes, so unit 1 starts with the end of unit 0. I left both units out in those files.
- **Missing data:** 7 files have no units table, 16 no sleep states, 14 no ripple events. Rat09 has no hippocampal units and no ripples, so the analysis uses 15 sessions from 3 rats.
- **Undescribed labels:** unit region codes (bla, blv, bmp, ladl, den, ven, and others) have no description and some appear in two cases. One file has no labels, and the electrode table says "unknown" for every channel.
- **No position:** there is no position tracking, and the `trials` table is undescribed.
- No recording was deposited twice. The clock checks (ripple rate by sleep state, hippocampal firing at ripples, decoding lap direction, responses to puffs) are consistent with one shared clock.

**3. Where the protocol was unclear or did not fit**
1. With only the abstract there are no reported numbers or tolerances. I made every claim a directional criterion and chose all methods myself, fixed in the claims file before the analysis.
2. Step 5 (read linked code): the dandiset links no code, and I could not see whether the paper does. I recorded this as a `methods_unavailable` finding.
3. The rule for when to block a claim on its unit selection covers a fixed method but not an analysis that drops a whole animal. I excluded Rat09 under the claims file's own session rule and recorded it as a deviation.
4. "Decide which claims are blocked" does not say what to do with an abstract sentence that describes the task setup ("rats learned the location"). I kept it as a claim and blocked it as `data_missing`. I had already looked at lap durations in the data check, so testing a lap-time stand-in would have meant writing its criterion after seeing results.
5. The protocol does not say whether to repair broken data or leave it out. Following "exclude a rare odd input", I left out the two mixed units per file.
6. For the lap-direction clock check, shifting the labels by whole laps would only flip them, because laps alternate. I shifted the laps by half their own length instead.
7. The criteria do not say how to count a lap that starts before the run and ends inside it. I clipped such laps to the run epoch, so the time before the first reward counts as a lap toward that reward.
8. With no reported chance level for the BLA selection, I computed it with my own procedure (windows shifted by 7 s), as the protocol suggests.

**4. Runtime and failures**
- The notebook runs in 605 s: about 6 minutes streaming the 40 files and about 4 minutes of analysis.
- No step failed. Two problems came up during development and were fixed before the analysis: laps that started before the run were dropped, and the mixed units were included.
- `git status` lists dotfiles (`.bashrc`, `.idea`, `scripts` and others) at the repo root. These are sandbox device mounts pointing to `/dev/null`, not files I made, and they should not be committed.

Files are in `entries/000061-girardeau-2017/`:
- reproduce_girardeau_2017.ipynb
- hpcbla.py
- README.md
- entry.yaml
- requirements.in
- requirements.lock.txt

The claims file is `claims/000061/10.1038-nn.4637.yaml`, the attempt record is `attempts/000061-girardeau-2017-01.yaml`, and the verifier's package is in `executed/000061-girardeau-2017/handover/`.
