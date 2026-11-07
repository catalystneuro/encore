I've finished steps 1 to 6: the entry is written, locked and checked, it ran from a clean environment in 13 min, and the handover package is built. All 41 claims were tested and none is blocked: 12 reproduced, 15 partially reproduced, 14 not reproduced. I did not verify my own work, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| table1-dataset-counts | partially reproduced (51 WAKE-SLEEP cycles, not 54) |
| ma-statistics | not reproduced |
| packet-duration | reproduced |
| fig2a-pe-rate-distribution | partially reproduced |
| fig2b-wake-nrem-slope | reproduced |
| fig2a-fraction-above-2hz | reproduced |
| burst-index-by-state | partially reproduced |
| fig2c-autocorrelogram | partially reproduced |
| synchrony-skew | reproduced |
| updown-durations | reproduced |
| fig1e-up-state-dynamics | not reproduced |
| fig2de-fast-before-slow | reproduced |
| fig2f-rate-group-correlations | not reproduced |
| fig3ab-population-rate-declines | reproduced |
| first-last-packet-mean-rate | reproduced |
| post-sleep-wake-lower | partially reproduced |
| fig3d-first-last-packet-slope | reproduced |
| fig3b-sextile-changes | reproduced |
| cv-decreases-over-sleep | not reproduced |
| fig3c-spindles-over-sleep | partially reproduced |
| fig3c-updown-over-sleep | not reproduced |
| fig3f-within-up-changes | partially reproduced |
| figs3a-first-last-rem-ma-slopes | partially reproduced |
| fig3e-wake-before-after-sextiles | not reproduced |
| fig4-lfp-within-nrem | partially reproduced (assumed) |
| fig4-updown-within-packets | reproduced |
| fig4-spindles-within-nrem | partially reproduced |
| fig4e-late-packet-sigma | reproduced |
| fig4-sextiles-within-nrem | partially reproduced |
| fig4cd-packet-rate-lfp-correlations | partially reproduced (assumed) |
| fig4e-within-up-sextiles | not reproduced |
| figs5-within-wake-rem | not reproduced |
| fig5b-ma-nrem-ma | not reproduced (assumed) |
| figs5d-rem-nrem-rem | not reproduced (assumed) |
| fig5c-sigma-ma-change | not reproduced (assumed) |
| fig5b-wake-between-packets | partially reproduced (assumed) |
| fig5b-ma-between-packets | partially reproduced (assumed) |
| fig5b-rem-between-packets | not reproduced (assumed) |
| fig5c-delta-change-slow-cells | not reproduced |
| figs2d-interneurons-unchanged | not reproduced |
| sleep-homogenizes-rates | partially reproduced |

A verifier may question four calls where I applied the criterion loosely:
- **fig4cd:** only 3 of 6 correlations meet the paper's bounds; the other 3 have the right sign at p < 0.05. Strictly the criterion's partial threshold is 4.
- **fig4-spindles:** the criterion's condition for reproduced holds, but I called it partial because spindle frequency does change within packets (p = 0.0096), where the paper says it does not.
- **fig2a:** five of six medians hold and the range test fails only in nonREM; I called it partial.
- **fig5b-wake-between-packets:** the partial call rests on a correlation over only 7 triplets, with the motion signal z-scored (see assumptions).

## 2. Dataset, assumptions, questions

**Version.** CRCNS data sets are unversioned, so the record says `unversioned` with the data set's DOI. The files read are pinned by the MD5 sums in `checksums.md5`, printed in the notebook. Only `live/` exists, so that is the version used; the header says why.

**What matches.** The counts match the paper exactly: 995 pE and 126 pI cells, 27 sessions, 11 rats, 43230 UP states, 86839 DOWN states and 5203 spindles. A clock check with time-shifted state labels peaks at lag 0 in every session.

**Findings about the data set:**
- There are 51 WAKE-SLEEP cycles, not 54.
- 434 microarousals lie inside SLEEP, against 790 in the paper. The files also hold 345 wake interruptions inside SLEEP that are shorter than the 40 s minimum the description gives; counted with the microarousals they make 779.
- One nonREM packet is 14 s long, below Table S1's 20 s minimum.
- The motion signal is described as z-scored but is not: it is non-negative, per-session means run from 0.55 to 4076, and one session (BWRat19_032513) contains NaN values.
- `RecordingFileIntervals` ends at infinity in three sessions, and the UP/DOWN file name differs from the description.
- Spindle incidence in the data (2.85 per minute) matches Table S1 (2.94), not the Results (1.94).
- Scored WAKE exists only as the WAKE of a cycle, so the paper's "5 min of WAKE after sleep" is missing or hours away for most cycles.
- Each session is one tar.gz and the order of files inside differs between sessions, so the notebook has to stream the whole archive (about 90 GB) on every run.

**Assumptions** (each marked `assumed: true`):
- Triplets are built from adjacent scored intervals with gaps of at most 2 s.
- The motion signal is z-scored per session, as the description says it is.
- Band power is log-transformed before z-scoring.

**Readings I added** beyond the claims file:
- A per-spike burst index, taken from the Results' wording "fraction of spikes with ISIs below 15 ms".
- A second way of normalizing time over SLEEP and episodes, by concatenated nonREM time.

**Questions for the paper's authors**, recorded as a `methods_unavailable` finding:
- What one sample is in the correlations against normalized time, and how SLEEP is normalized.
- Whether the burst index counts ISIs or spikes.
- What model the autocorrelogram decay exponent comes from.
- How triplets are formed, including which WAKE gives the 24 triplets.
- Whether motion was z-scored.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something
1. The prompt asks for a pinned published version, but archives.md says CRCNS is unversioned. I recorded `unversioned` with the MD5 sums.
2. The files are tar.gz, not zip as archives.md assumes, so fsspec plus zipfile cannot open them in place. I streamed each tar sequentially over parallel range requests and decompressed in memory.
3. The protocol has no guidance for a notebook that must re-stream about 90 GB on every run. It fits the 60 min limit (13 min), so I did it.
4. When the claims file's readings match each other on outcome but none matches the expected values, it is unclear whether a reading the author adds from the paper's wording counts as a reading or a variant. I ran the burst index's added reading and cited the passage.
5. Criteria with a fixed partial threshold do not say how to count sub-tests that are themselves partial under M4 (fig4cd). I counted them and said so in the notes.
6. The time-shifted label check covers continuous sessions only; nothing says how to check the clock of a derived signal such as the motion file. I checked its sampling against the recording length.
7. Protocol step 1.6 asks for a question to the authors on every assumption, but the record has only one finding kind for this. I put all five questions in one `methods_unavailable` finding.

## 4. Runtime and failures
- The run took about 1 h 30 min, from 07:53 to 09:23 UTC; each full notebook run took 13 min, and peak memory stayed under 1.5 GB per process.
- Two bugs were found and fixed during development: a partial-frame read of the LFP, and a 9.6 ms bin size where 8 ms was meant.
- Not run: a new UP/DOWN or spindle detection. Those criteria are judged on the deposited detections, which their readings allow.
- `git status` shows untracked dotfiles at the repository root (`.bashrc`, `.profile` and others) and a `scripts/` folder. I did not create them; check them before the workflow commits.

Files are in `entries/crcns-fcx-1-watson-2016`:
- reproduce_watson_2016.ipynb
- fcx.py
- README.md

The record is `attempts/crcns-fcx-1-watson-2016-01.yaml`. The handover package is in `executed/crcns-fcx-1-watson-2016/handover/`.
