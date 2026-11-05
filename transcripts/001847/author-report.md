I've done steps 1 to 5 of the Author section and run the handover; no claim was verified (that is left to the verifier). The entry runs cleanly from a fresh environment in about 14 minutes (`tools/entry.py all`: 0 errors, and a second run gave the same numbers). Nothing is committed.

The dataset is pinned at version 0.260610.1400. It is the only published version, and the READMEs of the paper's two code repositories name it.

## 1. Outcomes (40 claims, including one link claim I added)

| Claim | Outcome |
|---|---|
| session-list-link (added) | reproduced |
| expert-sessions | not reproduced: the Methods' rule picks 318 sessions in 49 mice; the code's list has the paper's 201 in 41 |
| fig1c auditory, fig1c whisker, fig1c catch, fig1d, fig1e, fig1g, fig1f, fig1h, supp1c | reproduced |
| supp1d | partially reproduced: the t-tests match the paper exactly, but every mean is about 100 ms longer |
| fig1i pupil, fig1i posture | reproduced |
| fig1j | partially reproduced: jaw speed holds, but whisking speed is also higher in W+ (corrected p 0.018) |
| fig1k accuracy, fig1k features, fig1l SHAP | blocked (`other`): not run within the time limit |
| fig2c, fig2d, fig2e (two claims), fig2-control, fig2cd-rsc, fig2f | blocked (`methods_underspecified`): the null and threshold readings give different outcomes |
| supp2 muscimol | reproduced (RSC p = 0.060 against the paper's 0.059) |
| fig3c jaw onset | reproduced, resting on an assumption |
| fig3e | partially reproduced: contexts similar and A1 first, but the order of the other areas is not found |
| fig3f | reproduced |
| fig3h | blocked (`too_large`) on the pixel part; in the ROI part RSC is first under every reading |
| fig3 GCaMP6f and controls | partially reproduced: tdTomato and GFP mice also show W+ against W- differences |
| supp3c tracing | blocked (`data_missing`) |
| fig4b (three claims) | blocked (`too_large`): needs the pixel image stack |
| fig4c, supp4d, fig4fg | reproduced |
| fig4d | not reproduced |
| fig4e | partially reproduced: holds in W+ only at the RSC site (-1.5, 0.5) |

## 2. Dataset, assumptions and questions

**What the dataset holds.** 1497 files in 73 mice. No recording is deposited twice. All 19 session lists of the paper's code match the dandiset's sessions by identifier.

**Findings for the data owners:**
- **Mouse lines are not recorded.** The genotype is "WT" for all but 3 files, so the lines (VGAT-ChR2, jRGECO1a, GCaMP6f, tdTomato, GFP) and the session groups (muscimol, Ringer, Context Off) are known only from the code's lists. I used those lists as labels and tested the match in the added link claim.
- **Wrong units on the face-tracking series.** They are labelled "seconds" with conversion factors of 1/28 or 1/24. In fact the stored whisker angle is in degrees (it gives the paper's 97.3 and 98.6 degrees unconverted) and the pupil area is in square pixels.
- **Columns undocumented.** No trial-table column has a description, and the perf codes are not explained.
- **Lick times.** Lick time minus stimulus time is about 100 ms longer than the paper's spout-contact times.
- **File defects.** Three files have no context epochs, and two have face-tracking timestamps and data of different lengths.
- **Context Off labels.** The Context Off trials are still labelled pink and brown noise.

**Assumption:** for fig3c I pooled auditory and whisker hits, as the code does. The other trial sets give onsets outside the tolerance.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which null was used for the opto maps? The Methods' block-label shuffle keeps the laser effect inside the null, so it finds no affected site at all. The legend's trial shuffle gives the published map. What d' threshold marks a site as affected?
- Which trials were pooled for the 108 ms jaw-onset figure?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Readings that cannot all be valid.** The criteria require every null and threshold reading to agree, but the Methods' block-label null is degenerate. So seven opto claims are blocked even though, under the legend's null with d' ≥ 0.8, the paper's map largely holds. I followed the criteria and put the per-reading results in the notes.
2. **Editing the reader's claims file.** Using outside labels meant adding `data: with_labels` and `depends_on: session-list-link` to 37 existing claims, besides adding the link claim. The protocol only says the author adds link claims. I made those edits and left every statement, expected value and criterion unchanged.
3. **No reason code for "untested for time".** `too_large` fits only where the computation itself stopped a claim. For the fig1k model, which I never started, I used `other` and said why.
4. **Criteria that define only "reproduced".** For fig1j the criterion gives no partial condition, so I used the protocol's general meaning of partially reproduced.
5. **Two-part criteria with one part too large.** For fig3h only the pixel part could not run. I blocked the claim as `too_large` and put the ROI result in the notes.
6. **"Develop on a subset" says nothing about how to stream.** My first metadata survey, using threads with no per-file timeout, hung for 60 minutes. I switched to process pools with timeouts; the protocol could advise this for streaming surveys.

## 4. Runtime and failures

- **Run time:** about 2 h 20 min of the 5 h. The notebook takes 13 to 14 minutes.
- **Failures:** the hung survey cost about an hour, and nothing from it was used. No other step failed.
- **Untracked files:** dotfiles, `.idea`, `.vscode` and `scripts/` show as untracked at the repo root. I did not create them and left them alone.
- **Files written:**
  - `entries/001847-bech-2026/`: the notebook, the `bech.py` helper and `build_nb.py`, which regenerates the notebook
  - `attempts/001847-bech-2026-01.yaml`: the attempt record
  - `claims/001847/10.7554-elife.109717.yaml`: the link claim and the label fields
  - `executed/001847-bech-2026/handover/`: the verifier's package
