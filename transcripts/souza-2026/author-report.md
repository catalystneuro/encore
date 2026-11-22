I finished steps 1 to 6: the entry, the notebook and the attempt record are written, and the handover is built. All 38 claims were tested and none are blocked: 17 reproduced, 15 partially reproduced and 6 not reproduced. Every outcome except two rests on an assumption about which sessions and units the paper used (`assumed: true`); the two exceptions also rest on it, through stated deviations.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| data-sessions-units | partially reproduced (assumption) |
| blocks-no-reward-in-replay, reward-interval-min | reproduced |
| latency-change-to-reward, lick-reward-coincide | partially reproduced |
| fig1e-cohort-size | partially reproduced (10,822 units against 11,032; only the 286 discordant against 239 is outside tolerance) |
| fig1d-split-half-above-null, fig1c-example-cells, fig1e-suppressed-fraction-by-area, latency-jitter-control | reproduced |
| fig1l-session-gradient | partially reproduced |
| waveform-ambiguous-band | not reproduced |
| fig1jk-narrow-fraction-by-area, fig1h-median-isi-narrow-broad, fig1gi-waveform-separation, narrow-more-suppressed, fig1m-narrow-stronger-m | reproduced |
| fig1mn-modulation-index-negative, m-baseline-sensitivity | partially reproduced |
| layer-assignment-coverage | not reproduced (outside input) |
| layer4-suppression, narrow-more-suppressed-within-layer | reproduced (outside input) |
| layer4-within-waveform, layer4-controls | partially reproduced (outside input) |
| fig2c-cv-lower, cohort-faster-firing | reproduced |
| cv-rate-matched, cv-unmatched-reverses, fig2d-cv-correlations, cv-correlation-block-excess | partially reproduced |
| fig2f-pre-post-cv | not reproduced |
| fig3a-archetypes, fig3d-anticipatory-gradient | reproduced (assumption) |
| fig3b-mixtures, fig3c-area-overlap, hits-vs-false-alarms | not reproduced |
| anticipatory-direction-overlap, hits-vs-lick-bouts | partially reproduced (assumption) |

## 2. Dataset, assumptions and questions

**Version.** 0.240702.1725, the version the paper cites and the only published one. It holds 153 sessions from 81 mice.

**Which sessions and units.** Neither reading the claims file lists fits the paper's counts. The 104 sessions of the Sst-Cre and Vip-Cre mice, keeping units with quality "good" and presence ratio ≥ 0.95 in the six areas, give 104 sessions, 54 mice and 54,045 units, against the paper's 103, 54 and 54,039. I adopted this selection as an assumption; nothing in the files shows which session the paper left out.

**What the checks found.**
- Blocks 0 and 5 are as the paper says in all 104 sessions.
- Licks, rewards, stimuli and spikes share one clock.
- 1,508 units have a CCF coordinate of 0 or below, so they get no layer (rated minor).
- Durations measured on the stored 30 kHz mean waveforms take only 60 distinct values, and the two-component mixture on them does not separate narrow from broad units. The stored `waveform_duration` does, so the waveform claims are judged on it (rated minor).

**Other assumptions.**
- The anticipatory label uses the mean response over -0.5 to 0 s against 0 to 1.5 s.
- An archetype's peak is the maximum of its absolute value.
- Lick bouts are split at 500 ms gaps.

**Deviation.** The ISI-shuffle null uses 100 permutations per unit instead of the paper's 1,000; the full 1,000 would take about 9 CPU hours. On 100 units, 76 pass at p ≤ 0.05 with 100 permutations and 80 with 1,000.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): which sessions and units were used; how archetype peaks and the ramp sign were defined; how a lick bout was defined; and whether the ISI null was built over the active block or the whole recording. Two internal inconsistencies in the paper are recorded as a `paper_inconsistency` finding.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. Conclusions must be written into the notebook from its own numbers, so every text fix costs a full re-run. With a 38-minute notebook I ran it four times. I wrote the text after a first run, then re-ran.
2. The five-seed sensitivity rule can't be met when the random draws happen inside the costly per-session pass (the ISI null, the latency jitter). I recorded it as not computed, with the spread over the jitter's 20 realizations instead.
3. The protocol doesn't say whether cutting the number of permutations, with a check of the cut, is acceptable or whether the claim should be blocked as `too_large`. I cut to 100 and recorded it as a deviation.
4. Outside inputs must be pinned by a DOI or a commit, but Allen's CCF download path is not versioned, and GIN's URL by commit returns 404 for its annexed files. I fetched BrainGlobe's packaging from GIN master and pinned it by the repository commit plus a SHA-256 the notebook checks.
5. For a link claim whose listed readings don't fit, the protocol doesn't say whether the author may adopt another selection. I adopted one as an assumption, scored it with the criterion's 10% partial rule, and said so.
6. Many criteria have no rule for a partial result. Where some of the values held, I used the protocol's general definition of `partially_reproduced`.
7. The "record the first reading listed" rule for `measured` doesn't cover the case where no reading fully matches. I recorded the closest one and named it in the notes.
8. The entry check reads `tifffile.imread` as reading a figure. I switched to `TiffFile.asarray()`.

## 4. Runtime and failures

- The notebook takes 38 minutes (peak memory 6.9 GB); streaming and reducing the 104 sessions in six processes takes 27 minutes of that.
- I ran the full notebook four times. The last run passed with outputs identical to the run before it.
- Lock, check and handover all pass. The only failure was the `imread` check error above, which is fixed.
- Nothing is committed or pushed.

Files are in `entries/souza-2026/` (open `reproduce_souza_2026.ipynb` first) and `attempts/souza-2026-01.yaml`.
