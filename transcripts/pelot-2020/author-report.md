I finished steps 1 to 5 and the handover (step 6). The entry is at `entries/pelot-2020`, the record at `attempts/pelot-2020-02.yaml`, and the handover in `executed/pelot-2020/handover`. `entry.py lock`, `all` and `check` all pass, the notebook runs from a clean environment in about 6 minutes, and the record validates against the attempt schema. I did not verify my own work, and nothing is committed.

## 1. Outcomes

36 of the 43 claims reproduced, 2 partially, 3 not reproduced, 2 blocked.

| Claim | Outcome |
|---|---|
| rat-sample-set, human-sample-set, pig-mt-sample-set, pig-if-sample-set, mt-micrograph-collections (link claims) | reproduced |
| nerve-diameter-anova | reproduced (assumed: only with the subject variance left unbounded, JMP's default; F 599.6 / 11.05 / 2.45 against the paper's 577.1 / 11.01 / 2.445) |
| human-pig-nerve-diameter-similar, rat-nerve-diameter, rat-ten-times-smaller, nerve-cervical-larger | reproduced |
| fascicle-number-human-pig, rat-subdiaphragmatic-multifascicular, rat-multifascicular-proportions | reproduced |
| fascicle-diameter-anova, rat-fascicle-diameter, cervical-fascicle-diameter-species, subdiaphragmatic-fascicle-diameter-comparable | reproduced |
| fascicles-larger-cervical | reproduced (assumed: with containment degrees of freedom the rat contrast is p = 0.089) |
| rat-diameter-like-fascicle, human-pig-tissue-proportions, pig-if-endoneurium-lower, rat-level-ratios, human-pig-level-ratios, human-variability, pig-oblong-human-round | reproduced |
| perineurium-species-order, perineurium-ratio-decreases, human-, pig- and rat-perineurium-fit (R² 0.749, 0.298, 0.767), perineurium-thicker-larger-fascicles | reproduced |
| sunderland-reanalysis | reproduced (slope 2.750%, R² 0.510) |
| rat-perineurium-near-3-percent, human-pig-perineurium-thicker, pig-if-mt-consistent | reproduced |
| pig-cervical-cell-bodies | reproduced (by eye) |
| peanut-fascicle-counts | partially reproduced (pig cervical: 57 bundles in 24 peanut fascicles, the paper says 25) |
| rat-carotid-sheath-bundles | partially reproduced (by eye; at most 5 bundles counted, the paper says up to 6) |
| perineurium-no-level-difference | not reproduced (cervical and subdiaphragmatic fits differ in human and pig, F ≈ 20, p < 0.0001) |
| no-age-trend | not reproduced (3 of 27 Pearson tests below 0.05, all pig) |
| human-subdiaphragmatic-fatty-tissue | not reproduced (by eye: fat in 29 of 32 human sections, but also in 13 of 45 pig sections; the criterion allows at most 1) |
| literature-comparison-human-pig, rat-literature-comparison | blocked, data_missing (the Supplement 4 literature values are not available) |

## 2. Dataset, assumptions, questions

**What the datasets hold.** The datasets contain the authors' own MATLAB code. Copying what that code does reproduces the deposited human output metrics exactly.

**Findings about the data:**
- **Rat traces changed after version 1 (major).** The sparc-60 rat masks changed between version 1 and version 2, with no changelog entry. The paper's numbers match the current masks; the deposited output-metrics `.mat` file matches version 1.
- **Pig values in that output file are wrong (major).** Its pig fascicle diameters are about 1.40 times what the masks give (and what the paper reports). Its pig fascicle counts come from the version 1 masks of sparc-64.
- **Rat nerve diameter in the output file (minor).** For the three multifascicular rats it uses the connective-tissue boundary. That reading is the one that reproduces the Discussion's 0.68 ratio; the Results' means give 0.52. I recorded this as a paper inconsistency.
- **Inverted masks (minor).** 18 masks are stored as TIFF "MinIsWhite", so tools that read raw bits get them inverted.
- **Other minor metadata errors:**
  - The sparc-60 and sparc-16 readmes say the rats were 65 days old at minimum; the subjects sheets say 75.
  - In sparc-61, C48-2 is filed under the wrong sample, and copies of other micrographs sit in other subjects' folders.
  - A copied scale-bar file in sparc-89.

**Assumptions:**
- Satterthwaite degrees of freedom in place of JMP's Kenward-Roger.
- The claims file's own tests for the two "no difference" / "no trend" claims, since the paper names none.
- My by-eye readings of compressed micrograph derivatives at reduced resolution. They are recorded in `pelot.py`, and the notebook shows the images they were read from.

**Questions for the authors** (recorded as a methods_unavailable finding):
- Which JMP settings were used: variance bounding and the degrees-of-freedom method.
- What test lies behind "did not suggest a difference" between levels in the perineurium fits.
- Whether the age trends in Supplement 6 were tested.
- The rules for counting carotid-sheath bundles and for calling adipose tissue.

I asked a reader nothing. I did not come across any earlier attempt's results.

## 3. Where the protocol was unclear

1. **Pinned version vs the version that matches the paper.** The prompt pins sparc-60 version 5, but the deposited outputs match version 1. I kept version 5, which also matches the paper's own perineurium results, and showed version 1 as a variant. I read version 1 files through the Pennsieve file browser at their object versions.
2. **Claims judged by eye.** The criteria require visual judgement, which conflicts with "compute every result" and "no embedded numbers". I stored my readings in the helper, displayed the images in the notebook, and marked those outcomes as assumed.
3. **Sunderland data labelled "elsewhere".** The claims file says the Sunderland data have no archive, but they are deposited in sparc-65. I tested the claim on that file and listed it under `inputs`.
4. **JMP's Kenward-Roger method is not available.** I used Satterthwaite and showed containment degrees of freedom as a variant.

## 4. Runtime and failures

- Author run from 03:21 to about 04:25 UTC. The notebook takes about 350 s, with 1.15 GB peak memory.
- No step failed.
- A harness folder, `entries/pelot-2020/.claude/.cc-writes`, sits inside the entry directory. I left it alone.
