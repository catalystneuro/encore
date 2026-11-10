I ran steps 1 to 5 of the Author section and the handover (step 6), but not verification. The checks report 0 errors. The notebook passed `entry.py all` from a clean environment in 43 min (2558 s), and every outcome in the executed copy is identical to the development run.

## 1. Outcomes (65 claims: 13 reproduced, 9 partially reproduced, 42 not reproduced, 1 blocked; none rests on an assumption)

| Claim | Outcome | Claim | Outcome |
|---|---|---|---|
| fig1e-swr-abundance-genotype | reproduced | fig3b-apa-entrances-day1 | reproduced |
| fig1f-sg-power-genotype | reproduced | figs3-apa-day1-and-probe | partial |
| figs1a-mua-during-swrs | reproduced | apa-40-comparisons | not |
| fig1g-mwm-impaired | reproduced | apa-day2-variance | partial |
| screen-88-comparisons | not | figs3fg-day2-predicts-later | reproduced |
| fig2b, fig2c | not | fig3c, fig3de, fig3g, fig3h | not |
| figs1b, fig2d, fig2g | partial | fig3f, fig3i | not |
| fig2f, figs1d, fig2h, figs1f | not | figs3ij-mwm-predicts-apa | partial |
| fig2e, fig2i (scores) | partial | figs4ab-young-deficits | not |
| screen-features-independent | not | figs4ab-aging-increase | partial |
| all 8 rep-mwm-* claims | not | figs4cd-baseline-sd-swr-band | reproduced |
| fig2n, fig2r, rep-all-replicated | not | figs4ef-ca3-sg-baseline-stable | not |
| cohort-swr-differences | reproduced | figs4g-young-no-deficit | reproduced |
| robust-detection-parameters | not (26 of 36 run) | table-s4-young-no-prediction | blocked, metadata_insufficient |
| robust-single-point | not | fig4bc-swr-not-stable | reproduced |
| age-no-correlation | reproduced | fig4de-ca3-sg-stable | not |
| figs2-nonspatial-no-difference | reproduced | ca3-sg-5-8-vs-13-17 | reproduced |
| nonspatial-not-correlated | not | fig4g, fig4h, figs4h, fig4jk, fig4i, fig4l | not |
| ca1-dg-not-predictive | not | table-s4-30-comparisons, figs4i | not |
| e3-relationships | not | | |

- **Genotype differences reproduce closely.** For example t(27) = 8.21 against the paper's 8.42, and the MWM genotype effect F = 13.08, p = 0.0009, exactly as printed.
- **Screen-cohort correlations are weaker than printed.** For example fig2b gives R = -0.47 with p = 0.066.
- **Replication correlations are near zero.**

## 2. The dataset, assumptions and questions

**Dataset findings:**
- **MUA units.** The descriptor says spike times are in ms; they are in samples at 30 kHz.
- **Prism file.** `All_Figures.pzfx` is Prism's binary format, not the XML its extension names, so it cannot be read without Prism.
- **CA3 site labels.** The deposited labels do not match Table S1. Every screen mouse has CA3 labels (the paper excluded 5). At 13-17 months only 4 E3 and 11 E4 mice have them (the paper has 9 and 14). Labels also change across ages for the same mouse.
- **Missing mice.** Three E4 mice are missing at 5-8 months and one at 9-11 months, so the Figure 4 tests have 8 mice instead of 10 or 11.
- **Unlinkable behavior file.** The 6-9 month water maze file uses its own mouse IDs that no file maps to recorded animals. This is the reason for the one blocked claim.
- **Hot plate.** The sheet lacks four E4 mice.
- **Behavior link checked.** Name-to-ID matches in Cohort 2 correlate r = 0.89 to 0.99 on trial values.
- **Paper inconsistency.** The distance-per-bout column that reproduces the printed U = 30 shows E4 mice moving less far per bout, against the Results text.

**Assumptions and choices:**
- **Readings run both ways.** SG power per session or pooled over sessions, and the z-score population, were each run both ways; neither choice changed an outcome.
- **Distance per bout.** I used the walk-bout column because it matches the printed U = 30; the all-bouts column is shown as a variant.
- **Tapers.** I followed the code's Chronux setting of 5 tapers (time-bandwidth 3), where the claims header says 3 tapers. This choice is stated in `swr.py`, not in the record.

**Questions for the paper's authors** are recorded as a `methods_unavailable` finding: which CA3 mice and sites were used, how the 6-9 month IDs map to recorded mice, which distance-per-bout column was used, how SG power was averaged, and which mice formed the z-score population.

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. docs/archives.md covers zip files read in place. hc-26 is nine tar.gz files totalling 108 GB, which can only be read start to end. I streamed each one once with fsspec and reduced each session as it arrived.
2. aiohttp's default 5-minute total timeout killed my first full run after 10 minutes. I added a stream that reopens at the current byte offset with a Range request. The archive notes should warn about this.
3. "Develop on a subset" fits poorly here: correlations across mice need every mouse. I ran the full 42-minute pass once for development and once in `entry.py all`. The 60-minute notebook limit leaves little margin.
4. Running everything in the foreground blocks the session for 40 minutes. The only concurrency available was calling a subagent alongside the long command.
5. The protocol does not say whether "reproduced" claims include partially reproduced ones when another claim depends on them. I included partial ones in `robust-single-point`.
6. The clock check suggests decoding with shifted labels. For home-cage LFP I used a different contrast instead: how many SWRs fall in immobile time, compared with immobility intervals shifted by 60 and 300 s.

## 4. Runtime and failures

- **Runtime.** About 2 h 30 min in total (23:30 to 01:58 UTC); the executed notebook took 42.5 min.
- **Failed full run.** The first full extraction died from the aiohttp timeout (10 min lost).
- **Behavior parser bug, fixed.** A bug in the behavior parser counted the sheet's average columns as extra trials. I found and fixed it before any outcome was recorded.
- **Not computed.** CA3 SG power for SWRs detected with the 125-250 Hz filter, which is 10 of the 36 correlations in `robust-detection-parameters`.
- **Stray folder.** An empty `entries/jones-2019/.claude` directory was created by the harness. My command to remove it was denied for lack of an approval surface. It holds no files, so git will not track it.

Nothing is committed. The handover package is in `executed/jones-2019/handover/`.
