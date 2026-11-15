None of the 25 claims could be tested: all are blocked as `data_missing`. The published dataset holds raw movies only, with no cells marked or labelled, and the paper's cells were identified by hand. The entry is in `entries/scholl-2015/` and the record is `attempts/scholl-2015-01.yaml`. `entry.py all` passes (the notebook runs in about 6 min) and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claims | Outcome | Reason |
|---|---|---|
| fig1e-pv-tdtomato-colocalization | blocked, data_missing | No histology in the dataset |
| cell-counts-responsive, fig3abc, fig3c, fig3 (MI), mi-per-animal, fig3def, mi-dsi-relation, pv-larger-dff-low-dsi (8 claims) | blocked, data_missing | No masks or PV+/PV- labels for the paper's hand-identified cells |
| fig4ag, fig4d, fig4f decay, fig4f length constant, fig4ef, figs6ab, figs4, fig4i, fig4k, fig4jk, figs6cd (11 claims) | blocked, data_missing | Same; no cells or positions |
| figs3, figs5 | blocked, data_missing | Neither the cells nor the hand-drawn neuropil patches are deposited |
| fig5-camkii-responsive, fig5e, fig5f | blocked, data_missing | The two CaMKIIa mice are not in the dataset |

For the claims on the paper's own cells, the notes give a second reason, `too_large`. Streaming the 252 GB of movies once takes about 6 h at the measured 11 MB/s, against the 1 h notebook limit.

## 2. Dataset

**What is in it.** The published folder `pvc-10/live/` holds:
- green and red movies for 58 planes across 6 mice;
- a stimulus table per plane and a stats file per mouse (stimulus duration and plane shifts);
- 50 unlabelled example masks for one plane (mouse 5, depth 260 µm).

**Findings recorded:**
- **Per-cell data missing.** The descriptor says the dataset contains per-cell traces, peak responses, DSI, preferred disparity and cell positions. None of these are among the published files.
- **Withdrawn files.** The bucket's `original/to_remove/` folder holds November 2014 structs that look like the paper's processed cells (masks, peaks, DSI, positions, neuropil). They cover only mice 7 to 10, and three of the mouse 7 files are truncated and cannot be opened. They are not in the file list or checksums, so I did not use them. The notebook only lists what they hold.
- **Other data the paper used is absent.** The CaMKIIa mice, the neuropil patches and the histology are not in the dataset.
- **Frame size.** The descriptor says 255 × 456 pixels; every file is 256 × 455, as the paper says.
- **Frame rate.** The dataset gives none. At the paper's 30 Hz, stimulus onset intervals fit the Methods' stimulus plus 3 s blank only in mouse 6.
- **Repeats and trials.** Eight planes have fewer than the 6 to 7 repeats the paper states (mouse 10 has 4 or 5). In four planes the last trial runs past the end of the movie. Mouse 10 has a plane at 125 µm, above the paper's "starting around 150 µm".

**Checks that passed:**
- No recording appears to be deposited twice.
- On the example plane, stimulus trials differ from blank trials after onset (2.59% dF/F, shuffle p = 0.005), and the difference shrinks when onsets are shifted. So the stimulus table is consistent with the movie's clock on that plane; the other 57 planes were not checked.

**Assumptions:** none (nothing was tested). **Questions for the paper's authors:** none recorded. **Questions to a reader:** none.

## 3. Where the protocol was unclear or missing something

1. It does not say what to do with unpublished files in the archive's own storage (`original/to_remove/`). I treated them as unpinnable and not published, did not use them, and recorded them as a finding.
2. It says claim-level data are `data_missing` when "not public anywhere else". These withdrawn files are publicly readable, but they cannot be pinned and are incomplete. I kept `data_missing` and said why in the notes.
3. It does not cover a dataset that holds raw movies but not the hand-made annotations (masks and cell types) that every claim depends on. I chose `data_missing` over `metadata_insufficient` because the masks are data the authors produced, not missing labels.
4. The notebook layout assumes some claims are tested. With none, I wrote a short "Claims" section explaining why and kept the "## Summary" heading so the handover strips it correctly.
5. The check tool flagged the string `"/data/"` as a local file path when it was only matching bucket keys. I rewrote the test.

## 4. Runtime and failures

- The run took about 70 minutes (20:59 to 22:08 UTC); each notebook run took about 6 minutes, and I ran it three times.
- Early on, walking every object in one movie file took about 30 minutes; I switched to reading frames by reference.
- Nothing failed in the final run.
