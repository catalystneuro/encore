All 11 claims have an outcome, the entry passes `check` and a clean `all` run (1195 s), and the handover package is built in `executed/zhang-2021/handover/`. Nothing is committed. Work ran from 09:59 to 11:29 UTC, well before the 14:14 cutoff.

**(1) Outcomes**

| claim | outcome | key numbers (paper) |
|---|---|---|
| fig1-csi-s2 | reproduced, assumed | 0.740 / 0.718 / 0.676 (0.75 / 0.69 / 0.67); p ≤ 0.001 |
| att-csi-group | reproduced, assumed | 0.665 / 0.729 / 0.525 over 5 subjects (0.66 / 0.74 / 0.53) |
| supp-csi-per-subject | reproduced, assumed | 10 of 12 within tolerance; all significant at p < 0.01 under permutation reading (a) |
| att-passive-lower | not reproduced | 2 or 3 of 5 subjects significant at the bound 1000 permutations allow; 4 needed |
| att-classification | reproduced | 44.4 to 56.3% across the four readings (48.4 ± 7.6); chance under this procedure 7.8 to 9.1% |
| att-weights-cortex | blocked, data_missing | the paper's per-subject ROIs and localizer data are not public |
| game-csi | reproduced | 0.702 / 0.581 with single-state clusters (0.72 / 0.62) |
| game-mutual-negative-projection | reproduced, assumed | all negative, p = 5e-5, with the dataset's column order; Table 1 order fails in S7 |
| fig3b-state-relations | reproduced | under every reading |
| game-classification | partially reproduced | S1 42.8 to 54.6% (32.8 ± 3.8); S7 within tolerance with contiguous folds |
| game-weights-two-groups | blocked, data_missing | no ROIs, and no mapper for S1's game voxels |

**(2) What was found about the dataset**
- The attend-human and attend-vehicle conditions are each z-scored per voxel in the deconvolved files. With the attention state coded -1/0/+1, its regression weight is zero (about 1e-14 in all five subjects). The third axis of the state space is therefore set by rounding, and the CSIs move by up to about 0.1 with it.
- The -1/0/+1 coding of that column is not documented.
- S1's game data hold 65 min, where the paper and the data description say 90 min. S1's game voxels (73,594) match no mapper. S7's game data are not z-scored per voxel, unlike S1's.
- The game state columns are not in Table 1 order.
- No duplicate recordings. Labels and BOLD line up: the attention CSI peaks at lag 0 and the game CSI at 1 TR.
- Version: unversioned, DOI 10.6080/K0668BDF. The MD5 sums of every file read are in the notebook header.

Assumptions:
- The attention third axis is the one the paper's code gives. The 2D plane and random third axes are shown as readings, and R1 (the plane) would change two of the CSI claims.
- The game variables enter the QR in the dataset's column order.
- Two ways of permuting condition labels for att-passive-lower were run (matched by movie frame, and global). Both give the same outcome.

Questions for the paper's authors are recorded as three `methods_unavailable` findings:
- How was the attention dimension defined, given the per-condition z-scoring?
- In what order did the nine game variables enter the QR?
- What exactly did the passive-versus-attentive test compare, and how were labels permuted?

I asked a reader nothing.

**(3) Where the protocol was unclear or missing something**
1. It has no case for a method that is well defined in the paper but undefined on the deposited data (the zero-weight attention axis). I treated it as an assumption with three readings.
2. The claims file says "the author decides whether an outside ROI source can be used". Protocol step 4 allows outside data only when the paper relies on it. I followed the protocol and blocked both cortex claims.
3. It does not say which value goes under `measured` when no reading matches. I used the first reading the criterion lists and said so in the notes.
4. The criteria need at least 1000 permutations (20,000 for the Bonferroni matrix), which puts the run at 20 minutes against the 10-minute aim. Nothing says how to trade these off.
5. Conclusions can only be written after seeing results, and any edit forces a full re-run, so every fix costs another 20 minutes. I developed on a 2-subject subset, ran the full notebook outside the entry, then ran `all` twice.
6. The schema wants `date` as a string, but an unquoted YAML date parses as a date. I kept the existing records' convention.
7. archives.md says CRCNS data sets are mostly zips. This one is plain HDF5 and npy, which streamed fine with fsspec.

**(4) Runtime and failures**
- The notebook takes about 20 minutes with a peak of 3.9 GB.
- I first counted supp-csi-per-subject significance against "exceeds every null value" when the criterion says p < 0.01. I caught it from the printed p-values, fixed it, and re-ran. The outcome changed from partially reproduced to reproduced.
- One generator edit deleted a notebook section by accident. I restored it and checked the diff before re-running.
- One shell command needing approval was denied (reading a saved output file with `sed`); I read the same file with the Read tool.
- The working tree also has untracked dotfiles and folders (`.bashrc`, `.idea`, `.vscode`, `scripts` and others) that I did not create or touch. The workflow may commit them.
