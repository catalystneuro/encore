I finished steps 1 to 5 for DANDI:000252 against the claims file, and the handover package is built. `python tools/entry.py all` passed with 0 errors, and the executed outputs were identical to my development run. Of the 19 claims, 9 were reproduced, 1 partially reproduced, 1 not reproduced and 8 blocked; two outcomes rest on assumptions. The work is not verified yet, since the verifier comes next, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| tenfinger-recording-counts | reproduced (the paper's counts are those before the 0.5 Hz exclusion) |
| tenfinger-pooled-npcc-neurons | reproduced (1114 units, paper 1111) |
| tenfinger-discriminative-fraction | not reproduced (at most 48.9 / 38.1 / 65.6% against 66 / 57 / 78%) |
| tenfinger-decoding-accuracy | reproduced (72 / 70 / 79% against 70 / 66 / 75%) |
| tenfinger-error-structure | reproduced |
| fig8b-matching-closer | reproduced, resting on an assumption |
| fig8a-npcc-index-distinct | reproduced |
| fig8e-hand-ccgp | reproduced |
| fig8e-finger-ccgp | reproduced under O9 (b); J-MC misses the 0.9 margin of O9 (a) |
| jppc-finger-ccgp-low | partially reproduced, resting on an assumption; p < 0.001 in only 1 of 8 readings |
| figs11-jppc-lower-matched-size | reproduced |
| fig4c, fig4e, fig5a, fig5bcd, fig5e | blocked, data_missing (alternating-cues task not in the dataset) |
| fig6-online-bmi, figs6, figs7 | blocked, data_missing (BMI sessions not in the dataset) |

## 2. Dataset, assumptions, questions

**What the dataset holds.**
- Only the ten-finger task: 10 sessions of participant N and 2 of J, 100 trials each.
- There are no duplicate recordings, and the spikes share a clock with the trial table in all 12 sessions.
- I pinned version 0.230408.2207, the only published version. The draft lists the same assets.

**Findings recorded.**
- **Spike times out of order:** 1509 of 1692 units store their spike times out of time order (format_error).
- **Subject labels:** the files call participant N `P1` and participant J `N1`, with no mapping to the paper's labels.
- **Undescribed trial columns:** five trial columns have no description, and the Delay onset is only implied by `cue_off_time`.
- **Unit counts:** the paper's per-session counts match the units before the 0.5 Hz exclusion. One J-MC session has 139 units against the paper's stated maximum of 130.
- **Related dandiset:** DANDI:000147 seems to hold N's BMI sessions from the paper's ref 46. The claims file doesn't name it as a source, so I didn't use it.

**Assumptions.**
- **fig8b:** the noise precision passed to rsatoolbox is that of each partition's mean, as the toolbox's documentation requires for its list-of-noises input. Without that scaling the differences are about one fifth of the paper's.
- **jppc-finger-ccgp-low:** the standard accuracy that CCGP is compared with is computed on the same pseudo-population, because the Methods call it "an upper bound on CCGP". If it is computed per session instead, J-PPC within-hand accuracy is 69%, inside the paper's 65% tolerance.

**Questions for the paper's authors** (recorded as methods_unavailable findings): how the noise precision was passed to rsatoolbox; which population the standard accuracy uses; what the 1001 label shuffles permuted and how pseudo-trials were matched; and which method gave the selectivity fractions.

**Questions to a reader:** none. I found no misreading in the claims file.

## 3. Protocol issues

1. The claims-file readings O3 and O4 did not cover how the toolbox is called, which changes values about fivefold. I added a reading from the toolbox's documentation, adopted it as an assumption, and showed the unscaled result as a variant.
2. Several criteria count a claim as reproduced "under one reading". That made fig8e-finger reproduced through O9 (b) even though O9 (a) fails, and made jppc partial through a single reading out of eight. I applied the criteria as written and gave every reading's result in the notes.
3. Step 1.4 does not say whether the author should look at a related dandiset the claims file doesn't name, such as 000147, when deciding between data_missing and `elsewhere`. I read only its metadata, did not use it, and kept the claims as data_missing with a note.
4. The protocol has no rule for a pseudo-population null over random pairings. Where trials were matched at random (O6 b), I drew a new matching for each shuffle and recorded this as a deviation.

## 4. Runtime and failures

- The notebook runs in about 6.8 minutes. The whole session took from 12:02 to 12:29 UTC.
- Two errors came up during development and are fixed: a singular noise matrix from units with zero variance (one unit is now dropped and reported), and an early sortedness check that read the wrong array.
- Dotfiles (`.bashrc`, `.idea` and others) and a `scripts` folder are untracked in the repository root. I don't think I created them (`scripts` was already there when I first listed the root) and left them alone.

Files are in `entries/000252-guan-2022/`:
- `reproduce_guan_2022.ipynb`
- `fingers.py`
- `README.md`
- `entry.yaml`

The record is `attempts/000252-guan-2022-01.yaml`, and the handover package is in `executed/000252-guan-2022/handover/`.
