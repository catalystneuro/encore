I've done steps 1 to 6 of the Author section for DANDI:000055 (pinned at 0.220127.0436) and built the handover. The final `entry.py all` passed: notebook 1 took 16.6 min and the regression notebook 27.3 min, which is close to the 30-minute CI limit. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| subject-days, figshare-event-link, figshare-roi-link (the last two are link claims I added) | reproduced |
| cohort | partially reproduced: 7 subjects have depth electrodes against the paper's 5; sex and age are not in the files |
| fig2-event-counts | reproduced: once the Figshare false positives are dropped, the counts are exactly 151 / 947 / 639.5 |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced: the angle peaks sit at about ±55 to 75°, not within 15° of ±90° |
| fig2-bimanual-skew | blocked, methods_underspecified: the two rejection readings (b1, b3) give different outcomes |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | reproduced (6 of 6) |
| fig2-days-and-waking | partially reproduced: S04's busiest day holds 0.43 of its events, not more than half |
| fig3 (three claims) | reproduced |
| fig4-precentral-subject-variability | partially reproduced: S09 has no HFB increase |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced (21 to 22 of 24) |
| fig5-recording-day-effects | partially reproduced (23 of 24 agree; S10 HFB differs) |
| extfig5-1-baseline-reduces-day-variability | reproduced |
| discussion-day-changes-small | blocked, methods_underspecified: b1 gives not reproduced, b3 gives reproduced |
| fig6-r2, fig6b, fig6c, fig6d (two claims) | reproduced, from only 18 models with R² > 0.05 |
| extfig6-2-angle-most-retained | not reproduced: bimanual ratio is retained most often, not reach angle |

## 2. The dataset and my question

- **False positives are not marked.** The files hold all 8088 events, including the 1157 that the paper's Figshare files flag as false positives. I linked the flags to the events by timestamp (100% match, all features agree).
- **Wrong ECoG clock in three files.** In sub-01 day 7, sub-04 day 3 and sub-06 day 3 the ECoG actually starts at the session start, but its stored starting time is 0. On the stored clock 237 events fall after the ECoG ends. Shifting the ECoG by the session start makes the movement response appear, so I used the shifted clock.
- **Metadata errors:**
  - the session start offset of −05:00 is wrong (sleep labels only fall at night on the UTC clock);
  - the pose is labelled meters but holds pixels;
  - Bimanual_overlap is described as a fraction but holds seconds;
  - electrode positions differ between days for S03 and S12;
  - the stored `low_freq_R2` / `high_freq_R2` columns have no method description. My regression R² correlates with them at 0.74 and 0.71.
- **Zeroed ECoG.** Some segments around events are zeroed and not marked. 42 events kept by the whole-segment rejection have zeroed precentral ECoG in the analysis window.
- **Region projection.** I used the paper's Figshare projection matrices instead of re-projecting from the AAL atlas, which I could not fetch; a link claim checks them against the electrode positions.
- **One question** is in `questions/000055.yaml`: how the paper's PSD rejection ("power <0 dB", Methods) is computed. I ran three readings:
  - b1: Welch PSD averaged over good electrodes;
  - b2: per electrode, which leaves no events in three subjects;
  - b3: b1 plus Morlet power below 0 dB in any time bin of the analysis window.

## 3. Where the protocol was unclear, and what I did

1. **Adding a reading after seeing the data.** I added b3 only after the first run exposed the zeroed segments. Readings are meant to be fixed before analysis, so I recorded this openly in the question and the notebook, and blocked the two claims where b1 and b3 disagree.
2. **No event set in some criteria.** Some criteria (bimanual-skew, reach-shape) don't say which events to use. I applied the reader's several-readings rule, which led to the bimanual-skew block.
3. **Outside data standing in for a method step.** The protocol doesn't cover using the paper's own intermediate output in place of a step (the projection matrices). I added a link claim marked `data: with_inputs`. Also, claims that drop the Figshare false positives still say `data: dataset`, and authors can't change that field; I noted this.
4. **No way to share heavy results between notebooks.** Each notebook has to re-stream about 170 GB of ECoG. The regression's variants (80/20 split, median band power, the b3 events) didn't fit in 30 minutes, so I didn't run them and recorded that as a deviation.
5. **`measured` must be numbers only.** For cohort, two expected values can't be measured, so I left `measured` out and put the values in the notes.
6. **Re-running for conclusions.** It isn't clear whether adding markdown conclusions requires a full re-run (45 min here). I re-ran so the executed copy contains them.
7. **Ties.** In fig4 part 4 under b3, S04 ties for third smallest. The paper gives no tie rule, so I counted ties as included, recorded it as a deviation, and showed the strict-order result. The outcome is partial either way.

## 4. Runtime and failures

The work ran from 15:45 to 19:00 UTC, with three full runs of the entry. No run failed. The two notebooks and the entry files are in `entries/000055-peterson-2021/`, the record is `attempts/000055-peterson-2021-01.yaml`, and the verifier package is in `executed/000055-peterson-2021/handover/`.

The repo root has untracked files I didn't create (`.bashrc`, `.gitconfig`, `.mcp.json`, `scripts`, `.idea`, and others), plus an empty `.claude/.cc-writes` folder inside the entry. I left them alone; make sure they don't get committed with the entry.
