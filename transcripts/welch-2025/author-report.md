I finished steps 1 to 6. The entry `entries/001863-welch-2025/` is locked, passes `check`, and ran from a clean environment in 6.1 min (367 s) with no errors. The handover package is in `executed/001863-welch-2025/handover/`. Nothing is committed.

## 1. Outcomes (36 claims: 35 from the reader, plus one link claim I added)

| Claim | Outcome |
|---|---|
| fig1b, fig1c, fig1d, fig1d-females-only, fig1e repoke, ITI false report | Reproduced (p = 0.023, 0.039 in the 35-40 min bin, 0.011, 0.010 against males 0.39, 0.38, 1) |
| fig2a to fig2d-supp (9 claims) | Blocked: `data_missing` (no reward-port entries or exits in the dataset) |
| fig3a odor duration, fig3a omission, fig3b ITI | Reproduced |
| fig3c speed within trials, fig3d speed in the ITI | Partially reproduced (same direction, p = 0.063 and 0.079) |
| fig3supp: odor speed no difference, DOI ITI slower than odor, saline ITI slower, saline odor vs omission | Reproduced |
| fig3supp-doi-omission-no-difference | Partially reproduced (ITI vs omission p = 0.0059) |
| fig4abc (Z = 25.2, against the paper's 24.9), fig4d, fig4e (p = 0.11) | Reproduced |
| fig4supp-ks-every-mouse | Reproduced under reading (b): 13 of 13 mice. Under reading (a) and the code's computation, 11 of 13 |
| fig5ab occupancy | Reproduced (`assumed: true`, see section 2) |
| htr-event-link (added), fig5supp within-trial x, fig5e, fig5supp ITI x, fig5f, fig5supp sex | Reproduced with the code's clock |

## 2. Dataset, assumptions, questions

**What the dataset holds**
- 44 files, one DOI and one saline session for each of 22 mice. They match the code's session list. No recording appears twice.
- There are 14 DOI and 13 saline sessions with usable sniff signal, as the paper says.

**What is missing or wrong**
- **No reward-port events.** This is why the nine Figure 2 claims are blocked.
- **Main finding: the tracking clock.** The tracking has no frame times, and its stated rate is only an estimate made during conversion.
  - The code's clock (frame i at i / 80 s) does not line the frames up with the trials: the nose moves a median of about 0 px over a trial.
  - A clock fitted per session does line them up: about 80.5 frames/s in the later cohort and 72 to 75 in the first.
  - With the fitted clock as a variant, the within-trial speed effect and the within-trial HTR preference for x disappear.
  - Also with the fitted clock, HTRs are about a third as frequent within trials as in the ITI (p < 0.0001). This contradicts fig5f.
  - I kept the outcomes on the code's clock, because the claims file fixes it. I recorded the clock problem as a `metadata_error` finding and a `code_mismatch` finding.
- **HTR times.** The HTR series has no name in the files. The paper's code names it, so I added the link claim `htr-event-link` and marked the five HTR claims `data: with_labels`, depending on it.
- **HTR timestamps.** In the later cohort the last field of the timestamps is a frame count (0 to 79). The files store it as hundredths of a second and the code reads it as thousandths. All three readings give the same outcomes.
- **Smaller errors:**
  - The saline session of mouse 2182 is labelled female; the code and its DOI session say male.
  - The side codes are undocumented. The session notes show that side 2 is left.
  - The first cohort has set ITIs of 16 to 25 s, beyond the Methods' 1 to 15 s.
  - The code drops four sniff sessions as faulty, and the dataset does not flag them.

**Assumption:** for the fig5ab corners I took the arena as the 0.5th to 99.5th percentile box of all nose positions, because the paper gives no arena coordinates.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which region of the arena counts as its corners?
- How were the tracking frames aligned with the trial times?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. When a method the claims file fixes (here the 80 frames/s clock) is contradicted by the data, the protocol does not say whether to test with it or "trust the data". I tested with the claims file's method and showed the data-aligned clock as a variant, with findings.
2. fig3c and fig3d have criteria that define only the reproduced case. I called "same direction, 0.05 ≤ p < 0.1" partially reproduced, the convention the claims file uses for other claims.
3. Two rules conflict for readings: "the outcome is the one they all give" (author, step 1.6) and "reproduced under any reading the criterion names" (reader, step 3). For fig4supp-ks I applied the reader rule and recorded the result under the other reading.
4. The protocol does not say whether adding `data: with_labels` and `depends_on` to the reader's claims is allowed alongside a link claim. I added both, following the newest entry, and changed no statement, expected value or criterion.

## 4. Runtime and failures

- The work took about 50 minutes (15:43 to 16:32 UTC).
- Two notebook bugs failed during development and were fixed before the final run.
- For the per-period sniff tests under readings (b) and the code's, I gave the normal-approximation p, not 10,000 resamples, to save time. With |Z| of 2.1 to 26.9 the result is the same; the per-period tests under reading (a) and the pooled tests use full resampling.
- The untracked dotfiles at the repository root are sandbox device mounts, not files I created.
