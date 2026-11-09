No outcome changed. The verifier agreed with all 22 outcomes, so nothing went under `proposed`. The re-run (`tools/entry.py all`) passed with 0 check errors, and every outcome count it printed is the same as before, so the record's numbers stand.

**Corrected**
- **fig2a-lips-dorsal notes:** these now compare EC2 only (36.6 against 15.6). GP31 has no tongue window in that reading, so it gives no comparison.
- **fig5d split:** cell 59, the notes, the notebook summary and the README now say that two of the claims file's own readings decide the split. With the mean of three feature sets as R, all 120 readings fail. With k-means clusters, all 48 fail, including the 24 with the matching feature set. Every level of baseline, z-scoring, projection and CV set has both reproduced and not reproduced readings. The summary and README no longer say that fig5d's blocked outcome comes from those four details.
- **Cell 10:** EC9 has 23 consonant labels, not 24, matching cell 8.
- **README run time:** cell 3 now prints how much data is streamed (39.0 GB, not the 42 GB the README claimed). The README now says about 21 minutes, about 16 of them streaming 39 GB and computing high gamma. The run printed 967 s for processing and 20.7 min in total.
- **Round-1 record:**
  - The active-electrodes reason now includes the part of B3 it had dropped: the /thi/ split also flips GP31's silhouettes and the fig4ef late-window tests.
  - The round-1 `reviewed` field now says its cell numbers are those of the round-1 notebook.

**Added**
- **Round-2 entry under `verifications`:** for each claim it records agreement, the verifier's outcome, its reason quoted or closely paraphrased, and my response.
- **Three new questions in `questions/000019.yaml`:** these cover the places where the verifier thinks the claims file may misread the paper. They are unanswered.
  - **suppfig13:** whether the 4623 pair count should be a condition for reproduction.
  - **suppfig6:** whether "clear preferred tuning" needs more than grouping by the largest weight gives.
  - **suppfig9:** whether jaw against larynx should be judged at p > 0.05 or at the paper's P > 0.2.

**Not done**
- I did not change any claim, as the rules say; the three points above wait for a reader.
- I left the round-1 "the verifier asked for" sentences as they were. The verifier said that paraphrase was acceptable.
- B2 (GP31 and GP33 identity) and B3 (the /thi/ split) remain open. Nothing in the files can settle them, and they are recorded as a deviation and in the notes.
- Untracked dotfiles and a `scripts` folder appeared at the repo root, which I did not create, and I left them alone. Nothing is committed.
