I've done steps 1 to 6 of the Author section. The entry passes `check` and ran clean from a fresh environment (`pass reproduce_alasfour_2024.ipynb (1280 s)`), the record is written, and `handover` built `executed/alasfour-2024/handover/`. Nothing is committed.

**Main caveat.** The paper gives no code and leaves many details open, so every claim runs under a grid of the readings the claims file names: 96 pipelines × 4 chance levels = 384 readings. The criteria accept a match "under one reading". Many claims marked reproduced match in only a few of the 384: fig2-single-band-rois 4, fig5-pre-postcentral 2, all-rois-but-inferior-parietal 2. Under my main reading most of them fail. The notebook and record give the count for every claim, and those outcomes carry `assumed: true`.

## 1. Outcomes (31 claims, including one link claim I added)

| Claim | Outcome |
|---|---|
| roi-projection-link | partially reproduced |
| cohort-selection | reproduced |
| table1-participants | not reproduced |
| fig2-highest-accuracy, fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois | reproduced (assumed) |
| anova-roi-band-effects | reproduced (assumed) |
| anova-no-interaction | reproduced (assumed) |
| posthoc-band-averages, posthoc-roi-averages | reproduced (assumed) |
| fig3-three-class | partially reproduced |
| fig4-not-single-participant | reproduced (assumed) |
| fig4-missing-rois, fig4-participant2-high | partially reproduced |
| fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral | reproduced (assumed) |
| fig5-parietal-temporal-no-gamma, fig5-middle-temporal-tv | partially reproduced |
| inferior-temporal-high-gamma-inconsistent | reproduced |
| all-rois-but-inferior-parietal | reproduced (assumed) |
| fig6-sign-consistency | reproduced (assumed) |
| fig6-examples | partially reproduced |
| fig7-non-additive | reproduced (assumed) |
| fig7-exceeds-group | reproduced (assumed) |
| fig7-participant4-low-gamma, fig7-above-70, discussion-above-80, fig7-best-band-varies | partially reproduced |

No claim is blocked.

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.220127.0436, the only published version; the paper cites none.

**Findings about the dataset:**
- **Clock offset.** In `sub-01 ses-7` and `sub-04 ses-3` the epochs are timed from 19:00, but the ECoG starts at 03:31 and 03:20. Without correcting for this, 223 and 77 labelled blocks fall past the end of the recording. With the offset applied, `sub-01 ses-7` decodes like that participant's other days. `sub-04 ses-3` decodes at 0.460, against 0.71 to 0.82 on days 4 to 6, so its alignment is not established. I kept it in and name it in the record.
- **Good electrodes** change from day to day. Table 1's counts match no rule for combining the days.
- **No sex or age** anywhere in the files or archive metadata, so the "2 male, 3 female" part can't be checked.
- **Block lengths.** 110 of the 3,465 class epochs are not about 2 min long (0.1 to 482 s).
- **Missing values.** NaN values inside labelled blocks; 1,449 ten-second bins were dropped for this.
- **Projection matrices (Figshare).** They agree with the dataset's electrode positions for only 51 to 64% of electrodes, and participant 01's matrix has 98 rows for 94 electrodes.

**Assumptions** (all stated as deviations in the record):
- Electrodes used: those good on every day.
- Blocks used: single-label epochs only; blocks labelled e.g. "Talk, TV" are left out.
- Main reading:
  - artifact rule O4 (a) with the day's SD from the electrodes table;
  - ROI reading O5 (c), which I took from Methods 2.1 and cite;
  - density rule (ii);
  - ROI feature O6 (a) and buffer O7 (a);
  - chance level at alpha 0.05 from all of a participant's test samples, because Figure 2 draws one chance line.

Under this reading the artifact rule drops up to 74% of a participant's blocks.

**Questions for the paper's authors:** nine, recorded as a `methods_unavailable` finding (chance level, artifact rule, ROI threshold and density, ROI feature, buffer, good electrodes, multi-label blocks, Figure 7 validation set and ANOVA, participant numbering).

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Readings versus criteria.** Step 1.6 says the outcome is the one all readings give, or the best-supported reading as an assumption. These criteria say "under one reading". I followed the criteria, marked `assumed: true` and reported counts. With a large grid this makes "reproduced" easy to reach.
2. **`measured` value.** The rule is to record "the first reading the criterion lists", but the criteria name grids, not an ordered list. I recorded the main reading's values, which for fig2-highest-accuracy sits beside a "reproduced" outcome.
3. **Link claim.** Adding it means editing the claims file: I added `roi-projection-link` and put it in `depends_on` of every `with_inputs` claim. Its criterion was written after I had surveyed the matrices, and its notes say so.
4. **Clock check.** The protocol says to name a session whose clock can't be established, not whether to drop it. I kept `sub-04 ses-3` in.
5. **Development cache.** I cached derived features (not raw files) in `$TMPDIR` while developing; the notebook recomputes everything from the stream. The protocol is silent on this.
6. **Size of the reading grid.** There is no guidance. I ran the full grid for the two-class analyses and reduced grids for the three-class analysis (12 readings) and Figure 7 (48).
7. **Harness string.** I used "Claude Code" as the prompt gave, where the example record uses "Claude Code (GitHub Actions)".

## 4. Runtime and failures

- **Notebook:** 21 min. Of that, 16 min is streaming 89 GB in four processes, using a parallel reader of the HDF5 chunk index (h5py's own index lookup took about 200 s per file).
- **Session:** about 1 h 50 min, from 03:37 to about 05:30 UTC.
- **Failures:** my first full extraction crashed after 15 min on a block past the end of a recording, which is how the clock offset turned up. One rerun followed.
- **Other files:** the untracked dotfiles and the empty `scripts/` directory at the repo root are not from this work and were left alone.
