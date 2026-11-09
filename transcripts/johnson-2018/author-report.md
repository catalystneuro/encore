I tested all 21 claims on fcx-2. Five are reproduced and 16 are not; none are blocked. The entry passes `check`, the full notebook ran in 35.5 minutes from a clean environment, and the handover package is built. Nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| behavior-proficient | reproduced (accuracy 0.792 to 0.967) |
| behavior-no-difficulty-difference | not reproduced (response time differs by condition) |
| electrode-counts | reproduced (36, 116, 102; 9 and 7 subjects) |
| correct-trial-counts | reproduced |
| erp-no-condition-difference | not reproduced (1 of 254 electrodes significant; the criterion allows none) |
| power-theta-sustained | not reproduced (0 subjects in any region) |
| power-condition-exclusions | not reproduced (12 electrodes in 5 subjects, against 8 in 4) |
| plv-theta-peak | reproduced (the rule is weak: one subject per group is enough) |
| psi-theta-shift | not reproduced, rests on an assumption (it holds only under the code's own PSI) |
| crossspectral-shift | not reproduced (shift in 1 of 7 systems; 2 of 7 under the code's PSI) |
| phase-directing-counts | not reproduced (0 units with the Methods' PSI; 1 of 7 counts within 10% with the code's) |
| crossspectral-equal-strength | not reproduced, rests on an assumption |
| theta-peak-bands | not reproduced (4 of 10 subjects match the paper's bands) |
| 8 PAC claims | all not reproduced, all rest on an assumption |

## 2. What was found about the dataset

- **Pinned version:** the live files (descriptor version 0.61). CRCNS does not version data sets, so it is recorded as `unversioned` with the MD5 sums in the notebook header; `orig/ver_0_6` holds only documents and scripts.
- **1.5 s timing conflict:** the trial table and the descriptor place the task events 1.5 s earlier than the time axes of the derived data, which the authors' code follows. I matched a derived trial of s8 against the raw recording to confirm where it starts. No task-locked response in the data settles which is right, so the analysis follows the code. All windowed outcomes depend on this.
- **Response times:** the per-subject response times in `summary_file.csv` differ from the trial tables in 7 of 10 subjects. The paper's condition means are the `summary_file.csv` ones.
- **s10:** its trial table is not on the derived data's sample grid.
- **Analysis code:** the deposited `psianalysis.m` omits the complex conjugate, and its form of PSI inflates z. Three PAC scripts cannot run as given (an empty temporal condition, an undefined variable, a wrong number of arguments).
- **Paper:** the Methods' 3-cycle PSI windows cannot fit a 900 ms segment at 3 Hz. The behaviour models are described with 3 condition levels but reported as F(1,28).

**Assumptions:**
- The code's single Hanning window for PSI.
- PAC units are selected with the code's form of PSI, since the Methods' PSI selects none.
- Empirical logit for accuracy.
- A peak at 1.5–4 or 6–10 Hz is mapped to the nearest of the paper's bands for PAC.

**Question for the authors** (recorded as a finding): which PSI form and window produced the reported values, and where stimulus onset lies on the derived time axes.

**Question for a reader** (`questions/crcns-fcx-2.yaml`): the behaviour criterion leaves out condition as a single numeric term. That reading matches the paper's F(1,28) and gives its p > 0.12 for response time; under it the claim would be reproduced.

## 3. Where the protocol was unclear

1. Clock check: the derived data's time axes and the trial table disagree, and the data have no task-locked response. I did not shift every window, which would have doubled a 35-minute run. I recorded it as a finding and as a deviation on each windowed claim.
2. Methods and code disagree on a method that the Methods describe in a way that cannot run (sliding windows). I used the code's window as the stated assumption and ran the sliding windows as a variant.
3. A claim depends on a selection that is empty under the main reading (no phase-directing units, so no PAC). The protocol does not say whether that blocks the claim or allows another reading. I tested on the code-form units and marked `assumed: true`.
4. archives.md says to use `fsspec`, but the files are `.tar.gz`, not zip. Streaming the tar with `requests` was about 5 times faster (46 against 10 MB/s), so I used it.
5. Dev cache: to develop without re-streaming 14 GB, I kept per-subject results (not raw data) in `$TMPDIR`. One 210 MB member was briefly saved to disk while exploring and then deleted.
6. Absence claims with ambiguous tests (the behaviour F(1,28)): the protocol says to judge on "the paper's test alone", but the paper's test is unclear. I applied the criterion's readings and asked a reader.

## 4. Runtime and failures

The development run took 35 minutes and the final run 35.5 minutes, with peak memory 5.9 GB. Nothing failed in the final run. The notebook exceeds the 10-minute aim because all 14 GB must be streamed and the cluster permutations and PAC surrogates are run in full.

Files are in `entries/crcns-fcx-2-johnson-2018/`:
- `reproduce_johnson_2018.ipynb`
- `fcx2.py`

The record and question are `attempts/crcns-fcx-2-johnson-2018-01.yaml` and `questions/crcns-fcx-2.yaml`.
