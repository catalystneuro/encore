I've finished steps 1 to 6 for DANDI:000402 and run `handover`. The analysis notebook passes `tools/entry.py all` in 644 s. Of the 36 claims, 13 were tested: 11 reproduced, 2 partially reproduced, none failed. The other 23 are blocked.

I pinned version 0.230307.2132, which the paper cites (its reference 73) and which is the only published version.

**(1) Outcomes**

| Claim | Data | Outcome |
|---|---|---|
| scans-14-p75-p81 | dataset | reproduced (14 scans, 6 days, P75 to P80) |
| scan-configurations | dataset | reproduced (11 / 2 / 1; depth spans 280 to 420 um) |
| masks-125413-somatic-115372 | dataset | reproduced (125,413 and 115,372, exact) |
| unique-neurons-75909, z-drift-under-10um, structural-stack, photodiode-89pct | dataset | blocked: data_missing |
| area-split-half-visp | dataset | blocked: metadata_insufficient |
| stimulus-composition, oracle-same-order, spontaneous-periods | dataset | reproduced |
| stimulus-conserved-across-scans | dataset | partially reproduced (Trippy seed 6831 is shown in both scans 6-4 and 7-5) |
| monet2-directions | dataset | reproduced (directions measured from the stimulus video) |
| fig3f-oracle-reliability, fig3g-direction-tuning | dataset | reproduced, using fluorescence traces |
| behaviour-recorded | dataset | partially reproduced (eye tracking in scan 4-7 ends 968 s early) |
| nuclei-144120 | elsewhere | reproduced (144,120, from a BossDB table) |
| cell-classification | elsewhere | reproduced (89,056 neurons against 82,247, within tolerance; 69,957 exact; SVM precision 95.5%, recall 99.6%) |
| synapse-detection, em-sections | elsewhere | blocked: too_large |
| 3 with_inputs claims and 13 other elsewhere claims | | blocked: other (the CAVE tables need an account token) |

**(2) What the dataset holds, and what is missing**
- It holds all 19 completed scans but does not mark the paper's 14. I read which 14 from the image of Extended Data Table 1 on PubMed Central, because the text in `paper/` has only the table's caption.
- The deconvolved traces, structural stack, stack coordinates, visual area per mask, oracle scores, per-period Monet2 directions and photodiode signal are all absent.
- The EM identifier columns appear in only one of the two fields at each depth (52 of 104 fields), and in no field of 4 of the 19 files.
- Other problems: `imaging_rate` is NaN in every imaging plane, every file gives the same age range, some treadmill and eye time stamps are NaN, and all fields of a scan share one timestamp array.
- Assumptions with `assumed: true`: none. No questions for the paper's authors, and none for a reader.
- The main substitutions are recorded as deviations. Fluorescence stands in for the missing deconvolved traces, and Monet2 directions are measured from the video by phase correlation.
- In 4 of the 560 Monet2 trials, two periods measure 7 to 10 degrees apart. That is within the measurement's error, so those 4 trials are not settled either way. I still recorded the claim as reproduced, and a verifier may disagree with that.
- I checked that the traces and stimulus tables share a clock by shifting the Monet2 analysis windows in time. Tuning reliability peaked at +0.47 s in all 104 fields.

**(3) Where the protocol was unclear, wrong or missing something**
1. No category fits public data behind a free login (CAVE). `data_missing` is forbidden for `elsewhere` claims, and `not_runnable` is about software or time, so I used `other` and explained it in the notes.
2. Outside inputs must be pinned by a DOI or a repository commit. The BossDB S3 objects have neither, so I recorded the URL, ETag and modification date.
3. The claims file names CAVE tables. I used the 2021 BossDB releases of the same tables and recorded that as a deviation.
4. The protocol says to read the PDF only for a garbled table, but there was no PDF. I fetched the table image from PubMed Central.
5. Nothing covers an external stream that times well on a trial but stalls in the entry's run. I dropped that notebook and blocked the claim as `too_large`, saying why.
6. Nothing covers deriving missing metadata from raw data, such as directions from the stimulus video. I treated it as a deviation.
7. There is no rule for an outcome when some expected values can't be measured, such as the subvolume 35 synapse count. The question became moot once synapse-detection was blocked.

**(4) Runtime and failures**
- The run took about 2 h 35 min, from 01:37 to about 04:12 UTC.
- A second notebook streamed the 20 GB v1181 synapse export. It counted 337.3 million rows in 10 minutes in a run while preparing, but stalled in the entry's run and was stopped at the 60 minute cell limit. That cost an hour, so I removed the notebook and blocked synapse-detection. The record does not use the 337.3 million.
- Not my files: device-node dotfiles at the repository root from the sandbox, and an `entries/000402-microns-2025/.claude/.cc-writes` directory the harness created. I left both alone; the second will be committed with the entry unless removed.

Files are in `entries/000402-microns-2025`:
- `reproduce_microns_2025.ipynb`
- `microns.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/000402-microns-2025-01.yaml`.
