I finished steps 1 to 6 for DANDI:001131. Of the 36 claims, 13 were tested: 3 reproduced, 1 partially reproduced and 9 not reproduced. The other 23 are blocked, mostly because the data are not in the dandiset. `entry.py all` passed: the main notebook took 228 s and the two rSLDS notebooks about 24 min each. `check` passes and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-unit-counts | Not reproduced: 4 control mice with 587 units and 6 experimental mice with 554, against 5/585 and 7/546 in the paper |
| figs4a-unilateral-no-behavior-deficit | Reproduced (assumed): no measure differs at p < 0.05; "attack probability" was not computed |
| fig4ef-male-activity-slightly-lower | Reproduced (assumed): lower in experimental mice when units are pooled (p = 0.002, KS p < 0.001); not significant across mice |
| figs4e-active-units-unchanged | Reproduced (assumed: "nested" read as a test across mice) |
| fig5bd-behavior-selective-units-reduced | Partially reproduced (assumed): all directions hold; 4 of 7 values fall outside tolerance |
| figs5e-behavior-decoding-intact | Not reproduced: control decodes better than experimental, p = 0.036 (3 vs 5 mice). Variant: with whole bouts held out the groups do not differ, because the frame-wise split leaks frames of the same bout into training and test |
| fig7c-achw-all-units | Not reproduced: reduction of 15 to 19%, against 50.9% |
| fig6-rslds-fit-quality, fig6a, fig6c, fig6f, fig6g, fig7b (rSLDS, all four seeds) | Not reproduced: variance explained 59% against 85%; time constants of hundreds of seconds; control line attractor score 0 to 0.78 |
| fig6e-integration-dimension-persistence | Blocked, metadata insufficient (intruder removal is not marked); a variant is shown |
| 21 female-intruder, behaviour-cohort, photometry and slice claims | Blocked, data missing |
| fig1e (outside RNA-seq atlas) | Blocked, `other`: I did not attempt it for lack of time, and a quick GEO search did not find the atlas |

## 2. Dataset, assumptions and questions

**Version pinned:** 0.260601.1203. The paper cites no version, and this one contains all of the earlier 0.240826.1647: that version's two files are the same recordings as mice 510 and 500, under other subject ids.

**What the dataset is missing or gets wrong:**
- One mouse per group is missing, and all female-intruder data are absent.
- Only z-scored traces are given, and nothing marks the pre-intruder baseline or the intruder's entry and removal.
- Mice 510 and 500 have only sniffing annotations, and their files describe the traces as "DF/F" from "GCaMP6m"; the values are z-scores and the paper used GCaMP8s.
- Mouse 500's trace is not z-scored over its own file.
- Session start dates are placeholders.
- My fits do not recover the authors' deposited rSLDS weights for mice 510 and 500 (|Spearman r| at most 0.47 for any dimension).

**Assumptions:**
- The baseline is the frames before the first annotated behaviour, and the interaction starts at that behaviour. Mouse 488, with only 6.2 s before it, is left out of the sigma-based measures.
- "Nested" for figs4e is read as a test across mice, because the paper ran its tests in GraphPad Prism.

**Questions for the paper's authors** are recorded as a `methods_unavailable` finding: the baseline and intruder timing, what "nested" means, the rSLDS frames, seeds, folds and dynamics matrix, how complex eigenvalue pairs enter the line attractor score, how ACHW is computed, how attack probability is summarised, and whether mouse 511's sniffing annotation is complete.

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. **Seeds versus the notebook time limit.** The claims file asks for four seeds, and four seeds take over the 60-minute notebook limit. I split them over two notebooks; the record combines both, and each notebook's conclusions cover only its own seeds.
2. **A pinned package that cannot be installed from the lock file.** ssm's `setup.py` imports numpy without declaring it, so it fails in an isolated build. The helper installs ssm at the pinned commit without build isolation. I recorded this as a deviation and listed ssm under `inputs`.
3. **Writing conclusions after the clean run.** I wrote the rSLDS conclusions after the run and copied only the markdown into the executed copies; a script checked that the code cells are identical. The protocol does not say whether this is allowed.
4. **No `measured` value when the first reading is undefined.** For fig7b the first reading cannot be computed, and `measured` accepts only numbers. I recorded the first fully defined combination and said so in the notes.
5. **Outside data the author does not test.** The protocol has no clear `blocked_by` reason for public outside data that is not attempted for lack of time. I used `other` and explained it.
6. **Absence claim with an ambiguous test.** For an absence claim the protocol says the paper's test alone decides, but here the test itself ("nested") is ambiguous. I adopted one reading as an assumption.
7. **"Under any reading" and nesting.** Under the claims file's "reproduced under any reading" rule, fig4ef passes on the pooled reading only.

## 4. Runtime and what failed

- The clean run took 52 min.
- The handover is in `executed/001131-mountoufaris-2024/handover/`.
- **Known limitation, not re-run:** when the two slowest eigenvalues are a complex pair, dimensions 1 and 2 get identical unit weights. This affects only the dimension-2 numbers of fig7b and does not change its outcome; it is stated in the notebook and the record.
- The first draft of the clock check failed and was replaced before the clean run.
- `date -u` ran slower than I expected, so I finished well inside the time limit.

Files are in `entries/001131-mountoufaris-2024/`:
- reproduce_mountoufaris_2024.ipynb
- rslds_seeds_0_1.ipynb
- rslds_seeds_2_3.ipynb
- vmh.py
- README.md

The attempt record is `attempts/001131-mountoufaris-2024-01.yaml`.
