I finished steps 1 to 5 and ran the handover (step 6). All 55 claims have an outcome: 22 reproduced, 18 partially reproduced, 5 not reproduced and 10 blocked. `python tools/entry.py all entries/brinke-2017` reports 0 errors and the notebook passes in 6 min with a peak memory of 1.5 GB. The handover is in `executed/brinke-2017/handover/`. Nothing is committed.

**1. Outcomes**

| Outcome | Claims |
|---|---|
| Reproduced (22) | fig1l, fig1m, fig1no, fig2b (trial correlations), fig2b-lmm, fig2e, fig2f (trial correlations), fig2f-lmm, suppression-smaller-shorter, fig2j, ds2-modulation-proportion, fig4g, fig4s1-cs-peak-cells, fig4h, fig5cd, fig5hi, us-peak-anticorrelates, fig6s1a, us-pause-prevalence, cs-pause-cells-have-us-pause, us-pause-declines, fig6h |
| Partially reproduced (18) | fig1ijk, modulation-absolute-not-rate-dependent, fig2a, fig2d, fig2h, fig2-suppression-properties, fig2n, ds2-stronger-facilitation, fig4b, fig4c, fig6 (US peak prevalence), fig6c, fig6d, us-peak-cooccurs, fig6b, fig7-second-us-peak, fig7-second-peak-dynamics, fig7c |
| Not reproduced (5) | fig2-s1 (correlation-matrix offsets), suppression-same-timing, fig2l, fig2p, fig7b |
| Blocked, data missing (10) | Four claims need recording depth (firing-rate-depth, fig4s1-not-different, fig5ej, fig6g); fig3 (optogenetics); fig5s1 and fig6s1bc (Purkinje cell data); us-only-trials, fig7s1c and fig7fg (US-only trials) |

No outcome is marked as resting on an assumption: every outcome holds under a reading the claims file names.

**2. Dataset, assumptions and questions**

What the data contain:
- **File:** cb-1 has one MATLAB 7.3 file. It streams into memory in about 5 s and matches its published MD5. It holds 372 recordings (270 + 102).
- **Version:** recorded as `unversioned` with the DOI 10.6080/K0B85697, because CRCNS does not version data sets and there is no other version to choose.
- **Missing:** recording depth, US-only trials, optogenetic sessions and Purkinje cell data.

Where the files disagree with their description or the paper:
- **`crAmplitude`:** it is the eyelid position 13 ms before the stated US onset, not at US onset. The match is exact in set 2 and close in set 1.
- **`facilitation`:** in set 2 it follows reading (b) exactly over the whole 0–212 ms interval, not the last 200 ms. Nothing tried reproduces it exactly in set 1.
- **`ephysMean`:** it differs from the mean of the stored trials in 26 recordings.
- **Trial exclusions:** 282 deposited trials have a baseline eyelid at or past half closure, although the Methods say such trials were removed.
- **Mice:** set 1 has 18 mouse IDs, where the paper says 19 (Results) or 22 (Methods).
- **Set 2 timing:** the files give a 212 ms CS-US interval; the paper's Results give 200 ms.

The main reason so many claims are only partial: the classification of cells into facilitation, suppression and no modulation does not give the paper's 60/23/187 under any baseline-correction reading. The three readings give 80/23/167, 62/13/195 and 88/31/151.

Readings run and choices made:
- **Extra baseline-correction reading (a+):** the "mean above-baseline activity" averaged over the above-baseline bins only. The Methods' wording allows it.
- **CS pause rebound:** looked for either inside the window or up to 50 ms after the trough. I first treated this as a standard choice, then found it changes counts, so both are now run as readings.
- **Normality test:** Lilliefors, which the paper does not name. Spearman-only counts are printed beside each count and change no outcome.
- **Trial exclusions:** not re-applied; the deposited trials are taken as the paper's valid trials.

Questions for the paper's authors are in the `methods_unavailable` finding of the record: the baseline correction, the CS pause thresholds, the bootstrap null, the normality test, the cross-correlation lag range and the velocity measure.

**Question to a reader** (`questions/brinke-2017.yaml`): the paper's Source data 1 on eLife has a `Depth` variable for the same 372 cells. Should the four depth claims be `data: elsewhere` or `with_inputs`? I read only that file's variable names, to ask the question, and used none of its values.

**3. Where the protocol was unclear**
1. CRCNS has no versions, but the prompt asks for a pinned published version. I recorded `unversioned` with the DOI and the file MD5s.
2. It does not say whether the author may add a reading the paper allows to the set a criterion names. I added (a+) and labelled it.
3. Data that is public elsewhere but marked `data: dataset` has no rule: `data_missing` is meant for non-public data, and the author cannot change `data`. I blocked the four depth claims as `data_missing` and asked a reader.
4. Some criteria ignore their own expected values (fig1m, fig1no, fig5cd and others), so a claim can be "reproduced" with numbers far off. I followed the criterion and reported the values in the notes.
5. It does not say whether a dependent claim must use the same reading as its parent claim. I took any reading per claim and named which one.
6. The clock check assumes a trial table, but these traces are pre-cut around the CS. I compared responses after the US against the same windows after the CS.
7. It does not say what to do when only part of a claim can be tested (fig4s1-not-different). I blocked it and put the two testable results in the notes.
8. Finding kinds do not fit a count mismatch between the data and the paper. I used `other` with `about: data`.

**4. Runtime and failures**
The run took about 1 h 15 min (01:09 to 02:23 UTC). The notebook runs in about 6 min with 1.5 GB peak memory. Nothing failed in the final run. One mixed-model fit is degenerate (SE 2.08) and is reported as such. Several cross-correlation lags sit at the ±100 ms edge of the lag range; their counts are printed.
