I re-ran the entry twice and `python tools/entry.py check entries/keles-2024` reports 0 errors. No outcome changed and nothing is proposed, so no third round is needed. The record still has 28 claims reproduced and 3 blocked (`not_runnable`).

**The main open point (3a): the memory-cell null now runs on rates.**
- **The fix:** the verifier found that the observed test used the code's spike rates (count / 1.5 s) while the permutation null used integer spike counts. Now, wherever two resampled mean counts tie exactly, the null recomputes the difference on the rates the way the code does. I checked it on synthetic cells against a direct copy of the code's `ms_test` using the same random draws: all 1200 null decisions matched. The change is in `bmovie.py`.
- **New p-values:** amygdala 0.0095, hippocampus 0.282, ACC 0.0005, preSMA 0.182, vmPFC 0.022. vmPFC has 14 selective cells against a null 95th percentile of 12, so it stays below 0.05. These are closer to the paper's values (0.015, 0.30, 0.002, 0.17, 0.016).
- **Effect:** the null adds 0.4 to 1.1 cells per area, which confirms the verifier's anti-conservative bias. No decision changes.
- **Comparison:** the old null on counts is printed next to the new one in reproduce [52]. The modality comparison (hfb [24]) uses the new values and the pattern is the same.

**Sentences corrected (section 2 of the report):**
- **LFP clock (hfb [10], hfb Summary, nwb-contents notes):** these now give the printed values before onset (9% micro, 7% macro, 10% units). They say the sweep bounds the offset only to roughly 9.9 to 10.25 s, and that the latency comparison does not show an offset below 100 ms. The claim needs only 10 s against 0 s, which the checks settle.
- **README run times:** about 9 minutes for `reproduce_keles_2024.ipynb`. For `hfb_keles_2024.ipynb`, 30 to 55 minutes (34 in the latest run, 54 earlier).
- **reproduce Summary:** the match now holds "under the readings chosen", and it names the other readings that fall outside tolerance: ISI reading (a), missing gaze reading (b) and the AUC s.d. per participant.
- **Gaze lag sentence:** reworded in the notebook and the notes to "from between 0.737 and 0.834 to between 0.290 and 0.317".
- **Sigma citation:** lines 120, 125 and 130 of `code/ephys_qc/gen_figure3_eyetracking.py` at commit 8c35290 are now quoted in reproduce [36], so a verifier can check them without the code.

**Record:** round 2 is added under `verifications`. All 31 claims are marked agreed, each with the verifier's reason closely paraphrased and my response. The notes and deviations for the memory-cell and modality claims match the new numbers.

**Not done:**
- **Point 3b:** the check of the bootstrap still rests on my own copy of the code, not the original scripts. That is the nature of the check and the verifier did not ask for anything. The new null was also checked only against that copy.
- **Confidence-accuracy wording (B7):** it stays with a reader in `questions/keles-2024.yaml`. No new reader questions came up.
- **Unexpected files:** untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts`, …) appeared at the repo root during the session. I did not create them and left them alone; you may want to check them before the workflow commits.
