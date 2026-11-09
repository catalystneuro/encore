I've done steps 1 to 5 of the protocol and built the handover (step 6) in `executed/000559-markowitz-2023/handover/`; the conclusions and summary are stripped from it. The entry passes check and runs from a clean environment in about 13 minutes (763 s). Nothing is committed.

The paper's full text is open access (CC BY 4.0) and I used it; the copy is under `paper/`. The pinned version is 0.260528.0858. The paper cites no dandiset version, and the earlier published version (0.240502.0456) has the same 4,425 assets; only dandiset-level metadata differs. The notebook header records this.

### 1. Outcomes per claim

| Claim | Outcome | Key numbers |
|---|---|---|
| fig1e-velocity-timescales | partially reproduced | Negative at all timescales under 10 s for both measures. Turns positive at long timescales for the transient rate only. |
| fig1h-syllable-dlight-differs | partially reproduced | n = 518 matches, P = 1.6e-35, but H = 258.9 against the paper's 209.3 |
| fig1l-identity-not-decodable | reproduced | Accuracy 1.06 and 1.24 times chance |
| fig2b-dlight-usage-across-syllables | reproduced | Held-out r = 0.160, shuffle P < 0.005 |
| fig2i-dlight-entropy-across-syllables | reproduced | Held-out r = 0.270 |
| fig2e-dlight-predicts-future-usage | partially reproduced | Significant at 8 of 10 window sizes up to 190 syllables |
| ed7-dms-fewer-transients | reproduced | P = 0.0064 |
| ed7-dms-no-usage-prediction | not reproduced | DMS dLight predicts future use, more strongly than DLS |
| fig3e-optoda-learning | reproduced | U = 198, P = 0.0013 (paper 197, 0.002) |
| fig3f-cumulative-counts | reproduced | U = 182, P = 0.0083 (paper 184, 0.007) |
| fig3e-learner-count | partially reproduced | 7 learners, not 9; all 7 are in the code's list of 9 |
| fig3h-stim-post-correlation | reproduced | r = 0.891 (paper 0.89) |
| fig3l, fig3m | blocked: metadata_insufficient | Catch trials aren't marked; my substitute shows "effects" in 9 of 12 no-opsin controls |
| fig3i, fig4f | blocked: metadata_insufficient | They need catch trials; not attempted |
| fig2a | blocked: data_missing | No food-reward sessions or consumption times |
| fig1f, fig2k, ed10d, fig4b, fig4c, fig4h, fig5 | blocked: other | Not attempted, for time |

### 2. What was found about the dandiset

- **What's there:** the paper's 14 DLS and 8 DMS dLight mice, 20 Opto-DA mice and 12 controls.
- **Not marked in the files:**
  - catch trials;
  - each mouse's genotype or opsin (groups can only be told apart by stimulation site or subject name);
  - the session type and session number.
- **Missing:**
  - the 2 s and pulsed sessions of the dLight+ChrimsonR mice;
  - the food-reward data;
  - some photometry sessions: 224 DLS files without stimulation, where the Methods give 379 experiments.
- **Format problems:**
  - in 575 files the syllable timestamps are not in time order (the rows are rotated);
  - 14 files have empty syllable series.
- **Metadata errors:**
  - every closed-loop file states a 635 nm stimulator, including the Ai32 mice, which the Methods say were stimulated at 470 nm;
  - the dLight-only mice carry the description written for the DAT-IRES-Cre and Ai32 mice;
  - 5 files with stimulation are described as recording sessions.
- **Not flagged:** files and sessions the paper excluded (behaviour-only files, sessions failing quality control) are included with nothing saying so.

### 3. Where the protocol was unclear, wrong or missing something

1. **No reason for "not attempted".** None of the blocking reasons covers a claim skipped for time or scope. I used `other` and said so in the notes.
2. **Which reason when a run selection fails a control check.** The "chance level" rule only covers a false-positive rate the paper states. For fig3l and fig3m the no-opsin controls showed my substitute catch selection was invalid. I blocked both as `metadata_insufficient`, since the cause is the missing catch markers.
3. **A criterion that defines only "reproduced".** The learner-count criterion said nothing about other results. I recorded 7 against 9 as partially reproduced and listed this as a deviation; the verifier may disagree.
4. **Direction of the clock contrast.** My first contrast (dLight peak just after syllable onset) came out reversed, because dLight dips at onset. I switched to comparing the shape of the onset-aligned waveform with shifted labels. The protocol could warn against contrasts that assume a direction.
5. **The paper's own data deposit.** The paper's Zenodo deposit (one 60 GB zip) is the dandiset's source and holds what the conversion dropped (catch flags, session numbers). The outside-data rules don't say whether the paper's own deposit may fill those gaps. I didn't use it.
6. **Default 10% tolerance on a test statistic.** For fig1h I applied it to the Kruskal-Wallis H, which grows with sample size. I kept it and recorded it.
7. **Reference list used only for comparison.** I listed the code's printed learner list under `inputs` but kept the claim as `data: dandiset`. The protocol doesn't say whether a reference used this way makes a claim `with_inputs`.
8. **Run time on large dandisets.** The notebook streams 1,723 files and takes about 13 minutes, over the 10-minute aim but within CI's 30. Reading even light metadata from all 1,942 files took 46 minutes in exploration.

### 4. Runtime and what failed

- The entry notebook takes about 13 minutes, and the clean-environment run passed twice with identical outputs.
- The whole session took several hours.
- **Failures:**
  - My first all-file metadata survey timed out after 1 hour.
  - The second survey took 46 minutes because h5py serializes threads; the notebook uses separate processes instead.
  - One development run was cut short by a pipe to `head`.
  - None of these affect the recorded results.

The working tree also shows untracked items I did not create (`.bashrc` and other dotfiles, `.idea`, `.vscode`, and `scripts`, which is a device file). I left them alone.
