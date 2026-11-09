I tested none of the 33 claims: all are blocked. The dataset holds only the raw images, and nothing in it says which brain region most of them show, so none of the paper's per-region values can be formed. The entry passes its checks and runs cleanly in 73 s, and the verifier's package (`python tools/entry.py handover`) is built.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| wt-no-label | blocked: `data_missing` (the wild-type mice were not imaged) |
| cells-before-plaques, l5-pyramidal-fraction | blocked: `metadata_insufficient` (they depend on blocked claims) |
| The other 30 claims (A1, subiculum, MGB, IC, SOC, nLL, CN and PRNc counts and densities by age, layer, subregion and sex) | blocked: `metadata_insufficient` |

## 2. The dataset, assumptions and questions

**Version.** I pinned 0.261022.1829, the only published version. The paper (2022) is older than the dataset and cites no version; the notebook header says so.

**Contents.** 12,394 single-channel OME-TIFF images of 62 5XFAD mice, as overviews and 100X and 200X fields, with no counts, region boundaries, atlas alignments or areas.

**Why the claims are blocked:**
- Only 864 images (7.0%) have a recorded region, and those come from follow-up rounds in 24 mice.
- 38 of the 62 mice have no region on any image, and the nucleus of the lateral lemniscus is never named.
- None of 20 sampled image headers and sidecars holds a stage position, section number or atlas coordinate.
- The dataset's README says a region without images had no label "judged present". That rule can't be used either, because the region of most images that do exist is unknown.

**Findings recorded:**
- The 25 wild-type controls are missing.
- The dataset has 62 mice against the paper's 61: p120 has 9 mice, and p45 has 3 females and 5 males against the paper's 4 and 4.
- The paper's Methods say "31 females and 30 males", but its own per-age numbers add up to 30 and 31.
- The magnifications are inferred from image content. A seeded nucleus-size check is consistent with the stated scales (about 4.2 and 5.1 µm nuclei at 100X and 200X, and 3.6 times as many per 100X field). The 7,125 images classed as 200X by rule were not checked.
- There are no duplicate files (every SHA-256 is unique), and sex, age and subject label match the original folder names for all 62 mice.

There are no assumptions, no questions for the paper's authors and no questions to a reader.

## 3. Where the protocol was unclear or did not fit

1. **Data check.** The protocol is written for time series: shared clocks and trial tables. This is histology. I checked subjects, scales and bit depth, and replaced the clock check with the region-coverage check.
2. **No tested claims.** The protocol has no shape for a notebook where nothing can be tested. I wrote header, data check, a coverage cell (tagged `coverage`, which every blocked outcome cites as its output) and summary, with no claim sections.
3. **Choosing the block reason.** The images are there but cannot be placed in a region, while the counts and boundaries are missing outright. I used `metadata_insufficient` as the main reason and recorded the missing derived data as a separate `data_missing` finding.
4. **Blocked by dependency.** l5-pyramidal-fraction is blocked through a claim it depends on, so its outside input (the cell atlas the paper cites) was never pinned. I said so in its notes.

## 4. Runtime and failures

The notebook runs in 73 s and the whole author run took about 20 minutes. Nothing failed; one draft sentence and two figures in the notebook text were corrected against the printed outputs before the final run.

Untracked files I did not create are at the repository root (`.bashrc`, `.vscode`, `scripts`, and others). I left them alone; the workflow's commit may pick them up.

Files are in `entries/002035-weible-2022/`, plus `attempts/002035-weible-2022-01.yaml`:
- `amyloid.py`
- `reproduce_weible_2022.ipynb`
- `entry.yaml`
- `README.md`
- `requirements.in` and `requirements.lock.txt`
