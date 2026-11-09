**A. Outcomes**

The claims file holds 52 claims. I did not have the attempt record, so the per-claim block reasons come from the table in notebook cell 0.

| Claim id | Outcome | Reason |
|---|---|---|
| rnn-training-data-amount | reproduced (fragile) | Under reading (a), all 9737 stored trials total 837.4 min (cell 11), which is inside 888 ± 88.8 (the floor is 799.2). It stays inside without targets 8 and 9 (814.3) and when duration is taken as last minus first timestamp (835.7). The match depends on keeping the 1886 robot trials: virtual trials alone total 540.0 min, which fails (see B1). |
| fig1g, fig1h, fig1ij, figs2, fig1kl, fig1mn (6) | blocked, data_missing | The file holds only B1's 9-target BCI trials. The Figure 1 imagined-movement task and participant B3 are absent (cells 3 and 4, and the archive). |
| Figures 2, 3, S3–S6 claims except figs3-spatial-pooling (20) | blocked, metadata_insufficient / data_missing | They need session, day, OL/CL1/CL2 labels, B3 data or 200 ms delta/beta/high-gamma power. The trial table has only target_id, is_virtual and is_robot. Start and stop times are DUMMY placeholders and there is a single session date (cell 3). I agree these are blocked. |
| figs3-spatial-pooling | blocked, but the reason should be metadata_insufficient, and part of it could have been tried | Right-thumb trials are present: target 1 is right thumb under both the Methods map and the OSF code map in the claims header. The high-gamma channels are present too. What is missing is the grid layout (no electrodes table), and the features are amplitude normalized per trial, not 200 ms power. See B5. |
| figs7b, figs7cd, figs7i (3) | blocked, data_missing | There are no ReFit-KF decodes or kinematics. |
| fig4b, fig4cd ×2, figs8ab, fig4fg, fig4i (6) | blocked, metadata_insufficient | No day labels, no B3. |
| fig5abc, fig5def, fig5-equal, figs8cde, fig5-bitrate, fig5ghi (6) | blocked, data_missing | No online decoder outputs or task outcomes. |
| fig6g ×2, figs8hi, figs8g (4) | blocked, data_missing | No kinematics or perturbation labels. figs8g also needs coactivation labels; nothing names targets 8 and 9. |
| fig7de, fig7ij, fig7k ×2, fig7kl (5) | blocked, data_missing | No robot task outcomes or times. |

I checked the archive directly. Version 0.260608.0617 has one asset, `sub-BRAVO1/sub-BRAVO1.nwb` (asset fa402651…, 4773567412 bytes). The draft and 0.250714.1218 hold the same asset. The asset metadata has no session or day information beyond a single acquisition session dated 2021-06-01. The dandiset description says 7 targets. Nothing in the archive unblocks any claim other than the figs3 variant.

No claim here states a chance level for a selection. Cell 8 is the notebook's own label-alignment check, and its chance level (0.139, largest class) is computed correctly.

**B. Problems**

1. [affects a conclusion] Cell 11, rnn-training-data-amount: the match exists only if the robot trials are counted. The Methods paragraph has two relevant parts:
   - The 14 h 48 min includes "practice with the Kinova Jaco in the real-world using the MLP".
   - The same paragraph then says the RNN was "created … from the virtual environment data" and afterwards fine-tuned on "multiple blocks of open-loop and closed-loop center-out and stop data with the physical robot".

   Nothing in the file says which of these the 1886 robot trials (297 min) are. If they are fine-tuning trials, the total is 540 min and the claim is not reproduced. The claims file treats with/without robot as display-only and accepts a match "under one reading". So by the criterion this is reproduced, but the claims file underweights this ambiguity in the paper. I am reporting that, not correcting it. The notebook does not discuss this in cell 10.

2. [does not affect a conclusion] Cell 10: reading (b), the active portion only, is not run, and the bound "(b) ≤ (a)" leaves (b) only 38 min (4.6%) above the tolerance floor. One argument is unused: each trial has an L2 norm of exactly 1 per 128-column block (cell 5), and lengths vary from 1.8 to 11.1 s. That suggests the stored trials are already the extracted LSTM epochs (OSF get_lstm_features.m: states 2–3 plus padding), in which case (a) ≈ (b). The notebook neither makes nor checks this argument. The criterion needs only one reading, so the outcome stands.

3. [does not affect a conclusion] Cells 3 and 11: targets 8 and 9 (264 trials, about 23 min, all virtual) are unexplained, while the dandiset description says 7 targets. They might be the Figure S6 wrist rotations, but that cannot be checked. Excluding them still matches (814.3 min).

4. [does not affect a conclusion] The cell 4 data check notes the age mismatch (paper 41, file P38Y) and leaves it unresolved. That is acceptable. `file_metadata` checks only that no series exists after the last id. It does not check for other non-trial series in `acquisition`, which could add data. All ids from 1 to 9737 were read, so the tested total is unaffected.

5. [affects a conclusion: a block reason, and possibly testable] Cell 0 table, figs3-spatial-pooling: this is filed under "data missing". Right-thumb trials and the 128 high-gamma channels are in the file. A variance variant was runnable under a stated assumption of row-major 8×16 channel order: bin to 200 ms, apply a 1 s running average, pool 2×2 to 32 channels, then a Mann-Whitney test. The outcome is nearly mechanical, because averaging lowers variance whatever the layout. The correct reason is metadata_insufficient (grid layout) plus a feature mismatch (per-trial L2-normalized amplitude in place of session-z-scored power). Neither is shown in the notebook.

6. [does not affect a conclusion] Cell 6 infers the column order (high gamma first) from the signs of the values and labels it an inference, which is correct. The tested claim does not use the column order.

7. [does not affect a conclusion] Cell 8 has minor issues:
   - Labels shifted by ±1 trial still score 0.175, above chance at 0.139. This reflects block ordering and does not weaken the alignment conclusion.
   - Folds mix trials from the same session, which is acceptable for an alignment check.
   - The duplicate checks in cell 5 find only exact copies. A trial deposited twice with different trimming would not be caught.

8. [does not affect a conclusion] I reviewed the code in `bci._summarise` and `trial_summaries` by hand:
   - The block norms are Frobenius norms over the trial, matching the Methods' "L2 norm of 1" per matrix.
   - The `ids[k::workers]` split covers every id; I checked this in Python.
   - The results are re-sorted by id, and cell 3 confirms they align with the table.

   I could not run the helper on a synthetic HDF5 file because h5py is not installed here.

**C. What I could not check**

- **The attempt record.** It was not available, so I could not see the per-claim block reasons or the author's outcome. The notebook's cell 0 table groups the 51 blocked claims (6+21+3+6+6+4+5) and gives no reason per claim.
- **Whether the robot trials belong to the 14 h 48 min.** Nothing in the file or archive settles this. Two outputs would help:
  - durations per context and target, alongside any block or ordering structure (for example, whether robot trials come after all virtual trials in id order);
  - a scan of trial-id order against context, which could suggest whether robot trials are a late fine-tuning set.
- **Whether the stored trials are already active-portion epochs.** A plot of the mean feature time course aligned to trial start and end, split by context, would show whether there is a pre-cue baseline.
- **Whether `acquisition` holds only `trial_<n>` series.** An output listing the count of names in the acquisition group, even if slow, would confirm this.
- **The helper on synthetic input.** h5py is not installed in this environment.
