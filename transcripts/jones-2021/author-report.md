## Report: jones-2021 on DANDI:000165 (version 0.211118.1526)

### 1. Outcome per claim (42 claims)

| Outcome | Claims |
|---|---|
| Reproduced (3) | fig3f-swr-frequency-pv, figs2a-swr-size-pv, fig6f-fg-coherence-unchanged |
| Partially reproduced (4) | tables2-rest-sg-pv, fig6g-fg-frequency-sst, figs4h-fg-theta-modulation-pv, tables4-genotype-baseline |
| Not reproduced (28) | fig3b*, fig3c, fig3d, fig3e, swr-longer-100ms-sst, fig3g, tables2-detection-unchanged, ca3-swr-overlap, figs3-ca3-swr-pv*, figs3c, figs3-dentate-spikes*, fig5b, fig5d, fig5e, fig5f, fig5g, fig6b, figs4e (correlation positive, not negative), fig6e, fig6h, figs5-theta-power, figs5-theta-coherence-frequency, the three figs6 claims, running-speed-unchanged, tables6-sex-swr-size, sex-stratified-effects |
| Blocked, data_missing (3) | fig1-tables1-expression, figs1ef-exvivo-cno, tables2-fast-ripples-pv (the LFP is filtered at 300 Hz and sampled at 1 kHz) |
| Blocked, other (4) | fig2ef-csd-sr, fig4d, fig4e, figs2cd. The data are in the dandiset, but these analyses were not written within the run's time. |

\* These outcomes rest on an assumption (`assumed: true`).

### 2. The dataset, assumptions and questions

**What was found about the dataset:**
- **Spike times are off the LFP clock.** MUA peaks around the SWRs, but displaced by a lag that differs per session (median −0.145 s, up to about ±2 s). Only 26 of 261 sessions with a clear peak have it within 20 ms.
- **Four mice have no vehicle sessions.** Beverly, Worf, Picard and Riker have only CNO-labelled sessions (numbered 8 to 17). So 14 PV-Cre and 14 SST-Cre mice are tested, where the paper has 16 each.
- **Cohort 3 treatment is not alternated.** Every mouse has its vehicle sessions before its CNO sessions, while the Methods say alternating. Treatment is therefore confounded with session order: the empty-vector mice change with CNO in 3 rest and 7 run features, and run faster on CNO days.
- **The LFP unit is probably wrong.** It says microvolts, but values reach the int16 limits, and power only matches the paper's order of magnitude when scaled by 0.195 (consistent with ADC units, not shown).
- **Metadata errors:**
  - Track session start times put all of a mouse's sessions minutes apart.
  - Chakotay01 is deposited twice.
  - Session lengths are 25 min, where the Methods give 60 min (home cage) and 30 min (track).
  - Every spike train starts with a spike at 0 s.
  - The electrode-label tokens ("ca1-pyr 1", "mua", "val") are undocumented.

**Assumptions:**
- Event-locked MUA uses each session's spike times shifted to its SWRs.
- SWR boundaries are where the envelope crosses its mean.
- Reading (a) of the log transform logs a feature when within-cell residual skew is above 1; reading (b), which logs every feature, was also run.
- Holm treats comparisons not computed here as ranked after those computed.
- Dentate spike detection follows the Methods literally. It finds about 8.6 events per second, which suggests a step is missing.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- What further step did the dentate spike detection use?
- Which features were log-transformed, and how were SWR start and end defined?
- Which clock alignment did the analysis use for the spike times?

**Questions to a reader:** none.

### 3. Protocol points

1. **The time limits did not fit this paper.** It has 42 claims on 98 GB. One full run takes 47 min, and the 60-min notebook limit forced two notebooks. "Blocked for time" only names `too_large`; I used `other` for analyses that were feasible but not written in time.
2. **No rule for treatment confounded with session order.** I recorded it as a finding and pointed to the empty-vector result.
3. **No rule for a clock offset that varies by session.** I used an aligned reading as an assumption, showed the deposited times as a variant, and left out sessions without a clear peak.
4. **The clock check could not be established for position against the LFP on the track** (79 of 170 sessions). I stated this and used the deposited times.
5. **Tool and schema disagree.** `tools/entry.py lock` writes a `python:` key into entry.yaml, which the entry schema rejects. I removed the key; the working tree's `entry.py` differs from its schema.
6. **Most `holds_on` and family details are underspecified.** Method M's sufficient rule leaves p between 0.05/24 and 0.05 undecided when the family is incomplete. I used Holm with the uncomputed comparisons ranked last.
7. **Unstable LMM p-values on very large features.** One empty-vector p moved from 4e-7 to 0.55 after a small filter change. This is noted in the entry README, and the final runs are deterministic.

### 4. Runtime and failures

- The run took 18:55 to 23:32 UTC.
- The final `entry.py all` passed: rest notebook 35 min, run notebook 12 min, same numbers as the previous run.
- The handover is built in `executed/jones-2021/handover/`.
- No file failed to load. Development hit two code errors, both fixed.

The record is in `attempts/jones-2021-01.yaml`. The entry is in `entries/jones-2021/` and holds `jones2021.py`, the two notebooks and `README.md`.
