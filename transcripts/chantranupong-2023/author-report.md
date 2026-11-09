I've done Author steps 1 to 6 for DANDI:001767. The entry ran clean twice (19 min each, identical outputs), `entry.py check` reports 0 errors, and the handover is built in `executed/001767-chantranupong-2023/handover/`. Nothing is committed.

**1. Outcomes** (48 claims: 47 from the paper plus one link claim I added)

| Claim | Outcome |
|---|---|
| link-manuscript-sessions | reproduced |
| ed1b, fig1e-post, fig1e-lda, fig1f, fig1g, fig1h-no-history, fig1h-approach | reproduced |
| fig1e-not-pre | reproduced, rests on an assumption (window W1) |
| ed1hj, ed3, ed4bc, ed2op | not reproduced |
| fig2d, fig2e, ed6b | reproduced |
| fig2a, fig2fg | partially reproduced |
| ed6c | not reproduced |
| fig3e | reproduced |
| ed8g | reproduced, rests on an assumption (ΔF/F0 reading) |
| fig3f, ed9jm, ed7e | not reproduced |
| ed11e | reproduced |
| fig4g-ach, fig4g-da, ed11fh, ed11i | not reproduced |
| ed11j | not reproduced, rests on an assumption (sessions resampled, as the paper's code does) |
| fig5d | reproduced |
| fig5c, ed13 | partially reproduced |
| fig5b, fig5ef-specific | not reproduced |
| ed5-base | blocked, methods underspecified: per-mouse pooling matches 0.206, pooling all sessions gives 0.13 to 0.17 |
| ed5f, ed5-history, fig2h, ed11-cko-glm | blocked, methods underspecified (depend on ed5-base; fig2h and ed11-cko-glm not run) |
| ed8f | blocked, methods underspecified: dLight1.1 and rDAh give opposite outcomes |
| fig3c, fig4ef, fig5a, fig3g, fig4bc, fig3d | blocked, data missing |
| fig5ef-dampens | blocked, data missing: the cortex part holds; the thalamic mCherry mice have no raw traces |

Totals: 16 reproduced, 4 partially reproduced, 15 not reproduced, 13 blocked.

**2. What was found about the dataset**
- I pinned 0.260318.1448, the only published version; the paper cites none.
- The files have no figure, cohort or genotype labels, and every subject reads age P0D, sex U. Cohorts come from `manuscript_sessions.csv` in the export repository the dandiset links (pinned commit f9a4ca9). It matches all 379 sessions, and 97% of virus codes agree with the files.
- The trials tables' times are not on the photometry clock (offsets from -125 to +1.2 s). Their sample indices are correct.
- In a median 17% of trials per session, the centre-exit index comes after side entry.
- The laser columns are all False, but the laser channel shows the stimulation.
- 193 named channels have no raw trace and 30 have no z-scored trace either.
- `baseline_f0` is about 0.07 times the raw trace, so it is not usable as F0.
- Four mice have virus codes in the sensor field; three viruses are given only as numbers (216, 222, 390).
- Nothing marks the cue-omission sessions.
- About half the sessions use a high-port probability other than the stated 95%.
- The slice, histology, head-fixed and DAN-inhibition data and the dLight mutant are absent. So are 21 mice and 64 sessions that the export table lists.
- **Assumptions:**
  - Window W1 for fig1e-not-pre.
  - The ΔF/F0 reading for ed8g.
  - Session resampling for ed11j.
  - The unnamed virus 222 is TelC.
  - A shrinkage LDA stands in for MATLAB's fitcdiscr.
  - The RFLR is fitted with Nelder-Mead.
  - Decision time and ITI are taken from the trials table.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how the GLMs were pooled and which predictors they used; which DA sensor ED 8f shows; whether ED 11d plots ∆Ach or mean Ach (mean Ach separates the genotypes, ∆Ach does not); whether the side-entry sample is inside the windows; whether the ED 11j bootstrap resamples sessions or trials.
- **Questions to a reader:** none.

**3. Where the protocol was unclear**
1. Outside data is allowed only if the claims file says the paper relies on it. The cohort labels come from the depositors' own linked repository, which the claims file does not mention. I used them anyway: listed under `inputs`, added a link claim, and marked 34 claims `data: with_labels` with `depends_on`.
2. Absence claims are judged "on the paper's test alone", but the claims file's own window readings disagreed for fig1e-not-pre. I adopted W1 as an assumption and showed W2.
3. There is no rule for a claim whose data is only partly present. I blocked fig5ef-dampens because the missing half could decide it. I recorded ed2op as not reproduced because the part I could test already fails.
4. Several criteria ask for every reading to hold, but some readings cannot be formed from the data (ed9jm (b) and (c), ed7e (a)). I decided on the readings that could run and said so in the notes.
5. Claims that depend on a blocked claim are blocked, so fig2h and ed11-cko-glm were not run even though they could be.
6. The schema rejects `inferred` on a link claim; the protocol text does not say this. I removed it.
7. The aim of under 10 minutes cannot be met: streaming the 379 files alone takes 8 minutes. The notebook takes 19 minutes.
8. The protocol's own notebook structure uses bold labels, which the prompt's style rules forbid. I removed them.

**4. Runtime and failures**
The run took about 2 h (15:12 to about 17:07 UTC). All claims were analysed; none was cut short for time. While developing, an S3 HEAD request returned 403, which I fixed. One action was denied: removing an empty harness folder, `entries/001767-chantranupong-2023/.claude/.cc-writes`, needed approval and was refused. Git does not track empty folders, so it should not be committed.
