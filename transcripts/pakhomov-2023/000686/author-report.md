I've finished the entry, the attempt record and the verifier's handover; all checks pass and the notebook runs from a clean environment in about 7 minutes (413 s on the last run). Four claims were tested, two of them reproduced only by resting on assumptions; the other 16 are blocked. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig5a-trains-stronger | partially reproduced: trains beat packets in the centre (p 0.0036 to 0.044); near e1 only in the mean (p = 0.059); no difference at the e3 end (p = 0.52) |
| fig5a-packet-center-enhanced | not reproduced: the e1 end is above the centre in all 4 dishes, but p = 0.105 to 0.162 under every reading |
| fig5b-rotation-center-peak | reproduced, resting on assumptions (centre from the LOESS fit; unpaired test) |
| fig5c-normalized-contrast | reproduced, resting on assumptions (centre from the LOESS fit; periphery at both ends) |
| fig3-field-simulation | blocked, `data_missing` |
| the four Fig. 4 claims | blocked, `data_missing` |
| the eleven Fig. 6 to 9 claims | blocked, `other` (their data are in DANDI:000875, 001025, 001027 and 001028) |

## 2. The dataset, assumptions and questions

**What the dataset holds.** I pinned version 0.240515.1909, the only published version; the paper cites none. It has 18 files, one stitched YO-PRO-1 image per dish, and they are exactly Fig. 5's four groups at 6.4 kV (4, 4, 5 and 5 dishes). No ROI measurements are deposited, so the profiles are measured from the images, with the ROIs placed by the layout in Methods 2.4. There are no duplicate files: the highest correlation between two images is 0.815, and files with the same dish number come from different dates.

**Metadata problems recorded as findings:**
- The species is given as *Bos taurus*; the paper used CHO-K1 hamster cells. The subject age is P1D, meaningless for a cell line.
- The dandiset summary says 36 subjects; there are 18 subject ids.
- The file description says "six-well plate"; the paper used 35-mm dishes.
- There is no pixel size. 0.65 µm per pixel fits the tile geometry, and then the gap between inner electrode edges is 8.4 to 8.8 mm, matching the paper's 8.4-mm diagonal.
- The electrodes are not labelled. I took e1 as the top-right footprint: it is the brightest in all 8 non-rotated dishes, and it is the mirror image of Fig. 3's top-left electrode, as an inverted microscope sees the dish from below.
- The other monolayer figures sit in four other dandisets that name the paper, but none of the five dandisets points to the others.

**Assumptions** (each also asked of the paper's authors as a `methods_unavailable` finding):
- **Centre value:** taken from the LOESS fit at 0, not the single centre ROI. The two disagree for Fig. 5B and 5C (for 5B, p = 0.073 with the centre ROI).
- **Within-dish comparisons:** unpaired t-test, following the paper's error-bar-gap rule. For Fig. 5B the paired test gives p = 0.051 to 0.080.
- **Fig. 5C periphery:** the mean of the outermost ROIs at both ends.
- **ROI size and background:** the paper gives neither. Background changes no outcome. ROI width moves some p-values across 0.05; a 3-step-wide variant is shown.

**Question to a reader** (`questions/000686.yaml`): should the eleven Fig. 6 to 9 claims be marked `data: elsewhere`, pointing at those four dandisets, so a later run can test them there?

## 3. Where the protocol was unclear or did not fit

1. **Data deposited in sibling dandisets.** The paper's data for Figs. 6 to 9 are public in four other DANDI dandisets, but the claims file says `data: dataset`. The protocol forbids `data_missing` for public data, yet step 4 forbids using outside data the claims file does not name. I blocked them as `other` and asked the reader question above.
2. **Image-only data.** The protocol assumes the measured quantities are in the files. Here the analysis has to rebuild the paper's ROI measurements (finding the electrodes, placing ROIs), which adds method choices the protocol does not anticipate. I recorded each as a deviation or a standard choice.
3. **Checking a shared clock** (author, step 2) does not apply to single images. I said so in the data-check cell.
4. **No "partially reproduced" rule in some criteria.** fig5a-trains-stronger fails at one of its three places under every reading. I used `partially_reproduced` from the protocol's general definition.
5. **Paired and unpaired tests (O6).** For 5B the claims file runs both but only lists O1, O2 and O4 as readings that must all hold. I treated the paired/unpaired split as a choice to settle by assumption, under author step 1.6.
6. **"Do not download to disk" during development.** I kept reduced (8 × 8 block-mean) copies in `$TMPDIR` while building the analysis; the notebook itself only streams.

## 4. Runtime and what failed

- **Wall time:** about 62 minutes, 09:50 to 10:52 UTC.
- **Notebook:** 377 to 413 s per full run, four runs. Streaming uses parallel range requests on the HDF5 chunks, about 20 to 80 s per 600 MB file.
- **What failed:** my first electrode detection was off by up to half a footprint radius. I caught it on the overlay figure and added a refinement step. That changed results: under the centre-ROI reading, 5B and 5C no longer pass, which is what made them depend on the LOESS assumption. All records reflect the corrected geometry.
- **Unchecked by eye:** in the train dishes the e3 footprint lies in a dark area, so its position could not be confirmed visually. The e3-end values are near 1000 a.u. in every dish either way.
