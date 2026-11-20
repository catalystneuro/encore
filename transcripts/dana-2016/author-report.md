I've finished steps 1 to 6 of the Author section. The entry is `entries/dana-2016/`, the record is `attempts/dana-2016-01.yaml`, and the verifier's package is in `executed/dana-2016/handover/`. `entry.py all` passed with 0 errors on a clean run, and the executed notebook's numbers match the conclusions. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| screen-single-mutations-improved (supplementary tables, data elsewhere) | not reproduced: the tables give 230 and 58 improved single mutants, the paper says 353 and 187 |
| culture-jrgeco1a-sensitivity (data elsewhere) | reproduced (ratio 8.57) |
| culture-jrcamp1-sensitivity (data elsewhere) | reproduced (ratios 24.02 and 12.96) |
| fig4-recorded-cells | reproduced (11 cells on 6 dates, 10 cells on 5 dates) |
| fig4d-event-counts | partially reproduced (11 of 18 counts within tolerance) |
| fig4e-jrgeco1a-1ap-detection | reproduced (82.4%) |
| fig4e-jrgeco1a-2ap-detection | reproduced (100%) |
| fig4e-jrcamp1a-detection | reproduced, resting on an assumption (63.0% and 75.3%) |
| fig4df-jrgeco1a-better-than-jrcamp1a | reproduced (all 8 spike counts under the main reading) |
| fig4g-jrgeco1a-faster | reproduced |
| fig4g-kinetics-like-gcamp6 | blocked, `other`: the GCaMP6 reference values were not obtained in readable form |
| 24 culture, purified protein, V1 grating, fly, fish and worm claims | blocked, `data_missing` |

## 2. The dataset, assumptions and questions

**What the dataset holds**
- cai-2 holds only the Figure 4 recordings, in two tar.gz archives under `cai-2/live/`. I streamed them, and their MD5 sums match the published `checksums.md5`.
- I pinned version `unversioned`, since CRCNS does not version data sets; `live/` is the only data copy (`orig/` has just an old description document).
- Two jRCaMP1a files, `data_20150526_cell2_001.mat` and `_002.mat`, are the same recording deposited twice. I counted it once.
- No animal identifiers exist, so I counted mice as recording dates.
- In `data_20150707_cell1_001.mat` the fluorescence shows no relation to the spikes, and `data_20150605_cell7_003.mat` falls just below the shifted-spike null. The shared clock could not be established for these two; the other 44 recordings align within one frame.
- The deposited script calls two functions, `rawf2df_f` and `fit_dynamic_fitting`, that are not in the data set, and there is no script for jRCaMP1a.
- The script disagrees with the Methods in three places: a 1% false-positive threshold where the paper reports 5%, 0.8 s isolation after events where the Methods say more than 1 s, and noise traces taken at gap midpoints. I followed the Methods where they spoke.
- The script's rule reproduces the jRGECO1a event and noise counts exactly, but not the jRCaMP1a counts.

**Assumption:** for jRCaMP1a I applied the jRGECO1a script's frame window. None of the claims file's own segment readings brings the jRCaMP1a single-spike rate within tolerance (at most 41.6%).

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which isolation, noise rule and frame window did the jRCaMP1a analysis use?
- How were the Figure 4g exponentials fitted, which fitting error chose the 16 traces, and how was half rise defined?

A `paper_inconsistency` finding records the gap between the 353/187 counts in the text and the supplementary tables.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. When the paper's own code settles a detail differently from every reading the criterion names, the protocol does not say which reading decides. The claims file's header says the script's reading is the main one, so I used it and still showed every named reading.
2. "Under one reading" across many combinations (up to 288 for fig4df) makes a match easy to find. I always reported the main reading and how many combinations match.
3. The CRCNS section of docs/archives.md covers zip files only. These are tar.gz, so I streamed them with `tarfile` in stream mode over fsspec and computed the MD5 while streaming.
4. For a `data: elsewhere` claim whose outside input is reference numbers in another paper's supplementary PDF, no block reason fits well. I used `other` for fig4g-kinetics-like-gcamp6.
5. The protocol does not say how a notebook should get the claims file's expected values. I read them from `../../claims/dana-2016.yaml` instead of embedding them.

## 4. Runtime and failures

The run took 12:05 to 12:38 UTC. The notebook runs in 3.6 minutes with 485 MB peak memory, almost all of it streaming 2.4 GB. Nothing failed.

Some odd untracked character-device files (`.bashrc`, `.idea`, `scripts` and others) appeared in the repository root at 12:04, before this run started. They look like sandbox artifacts, so I left them alone and didn't create them.
