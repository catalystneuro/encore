I finished steps 1 to 6 for dandiset 000056 on version 0.250624.0430. The entry passes `check` and ran from a clean environment in 6.1 min. I used the full text of the NIH author manuscript in PubMed Central (PMC4376557). The supplementary files could not be downloaded because PMC served a browser check in their place. Nothing is committed.

## 1. Outcomes

| Claim | Outcome | Main number |
|---|---|---|
| hd-cell-fraction | partially reproduced | 378 HD cells (expected 353 ± 35); fraction 0.218 (expected 0.328 ± 0.033) |
| fig2a-rates-preserved | reproduced | waking against SWS r = 0.838, against REM r = 0.891 |
| fig2b-pair-correlations-preserved | reproduced | r = 0.938 (SWS), 0.963 (REM), 1573 pairs |
| fig3a-packet-60-degrees | reproduced | crosses zero at 54.2, 56.9, 55.9 degrees (tolerance 54 to 66) |
| fig2f-sws-tenfold-faster | partially reproduced | median SWS/waking ratio 8.33 (expected 10 ± 1); decoder variant 11.5 |
| fig2f-rem-similar-to-wake | reproduced | median REM/waking ratio 0.87 |
| fig4b-noise-correlations | reproduced | positive at 0°, negative at 60° (p = 5e-19 and 5e-32) |
| decoding-tracks-hd | reproduced | median error 11.7 degrees, all 28 sessions at or below 30 |
| 12 claims comparing ADn and PoS | blocked: metadata_insufficient | none |

## 2. What was found about the dandiset
- **No region for any unit.** The units table holds only spike times: no electrode, shank, region or waveform, and every electrode's location is "unknown". This is why the 12 ADn against PoS claims are blocked. The electrode groups and ripple annotations suggest Mouse24, Mouse25 and Mouse28 are the dual-site mice, but the files don't say so; I used this only for variants.
- **More units than the paper reports.** The files hold 1959 unit rows (103 with no spikes) in 40 sessions. The paper has 1077 cells in 42 sessions, and nothing marks which units or sessions it used.
- **Waking epoch not marked.** The open-field exploration isn't labelled; the "Awake" state also covers time in the home cage. I found it from position.
- **Unsorted spike times.** In 36 of 40 files one unit's spike times are two sorted runs joined at an index of k × 65536 − 1. This looks like a conversion error; the helper sorts them.
- **Clock drift in Mouse12-120808.** Position and spikes drift apart by 1.5 to 3.4 s during the exploration. Every other session lines up within 0.2 s.
- **Smaller metadata problems:**
  - The raw LED positions are labelled meters with a NaN conversion but hold camera pixels.
  - Two sessions lack processed position and one lacks sleep states.
  - The `dow`, `hdD` and `rip` annotation series have no description.
  - The dandiset's link to the paper is malformed: the name is "nternally organized..." and the title is given in place of a DOI.
  - No analysis code is linked by the paper or the dandiset.
- **Version choice.** The paper cites no DANDI version. Both published versions hold the same 40 assets (same ids and sizes), so I pinned the most recent; the notebook header says this.

## 3. Where the protocol was unclear, wrong or missing something
1. **No linked code.** Step 5 assumes there is code to read. I recorded a `methods_unavailable` finding and fixed every open choice in the claims file.
2. **A criterion that turned out wrong after the run.** My first fig4b criterion used a Pearson scaling that contradicts the Methods' own formula. The protocol has no rule for this. I changed it to the Methods' formula before recording the outcome, explained the change in the claims file's opening comment and as a deviation, and kept the first version as a variant. Under the first version the 0° pairs come out negative.
3. **Clock check for continuous sessions.** The suggested check (decoding annotations with shifted labels) doesn't fit spikes plus position plus sleep states. I shifted head direction against the spikes, and the state labels against head speed. Whether spikes and states share a clock is only inferred, and the notebook says so.
4. **A waking epoch that has to be derived.** The protocol doesn't say what to do when a condition the paper uses isn't marked in the data. I fixed a detection rule in the claims file before any claim analysis.
5. **Region inferred only indirectly.** "Show it or state it as an assumption" leaves open whether an inferred region assignment may decide an outcome. I used it only for variants.
6. **One expected value across several conditions.** fig3a has one expected crossing angle but three states. I recorded the lowest (waking) under `measured`.
7. **Reported counts that do not decide.** fig2a's 277 cells is a reported number but not the finding. I listed it under `expected` and stated that it doesn't decide the outcome.
8. **Tolerance for approximate statements.** The default 10% applied to "approximately tenfold" gives a strict 9 to 11, which is what made that claim partial. I kept the default.
9. **Supplementary files.** The protocol doesn't cover open-access supplements that can't be downloaded. I recorded the failure.
10. **Descriptive statements.** Session counts, sleep duration (5 h) and exploration length (30 to 45 min) went into the data check, not into claims.
11. **Seeds.** No step uses random numbers, so there were no seeds to fix; the header says so.

## 4. Runtime and failures
- **Runtime.** The notebook runs in 367 to 374 s, about 189 s of which is streaming. I sped up the cross-correlogram step about 25 times by computing the speed expectation exactly; I checked it against the quadrature on synthetic tuning curves.
- **Failures.**
  - The PMC supplement downloads failed.
  - One loader crash (a file without a behaviour module) was fixed.
  - No notebook errors.
- **Stray files at the repo root.** The sandbox created entries there (.bashrc, .idea, `scripts` and others) that are /dev/null character devices, not files I made. They show up as untracked, so the workflow should not commit them.
- **Handover.** Step 6 is built in `executed/000056-peyrache-2015/handover/`.

Files are in `attempts/` and `claims/000056/`:
- entries/000056-peyrache-2015/reproduce_peyrache_2015.ipynb
- entries/000056-peyrache-2015/hd.py
- entries/000056-peyrache-2015/README.md
- entries/000056-peyrache-2015/entry.yaml
- entries/000056-peyrache-2015/requirements.in
- entries/000056-peyrache-2015/requirements.lock.txt
- attempts/000056-peyrache-2015-01.yaml
- claims/000056/10.1038-nn.3968.yaml
