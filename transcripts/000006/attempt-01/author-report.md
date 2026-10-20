All six protocol steps are done. The entry passes `check` and runs from a clean environment in 50 s with no errors, and the handover package is in `executed/000006-economo-2018/handover/`. I did not verify my own work and did not commit anything.

I used the abstract only. The paper is paywalled at Nature and has no PubMed Central copy. I also read its public Data availability statement, but only to find the linked data and code.

The pinned version is 0.220126.1855. The paper cites no DANDI version, and this is the only published one. The draft has the same 53 files and sizes and differs only in metadata.

## 1. Outcomes

| Claim | Outcome | Key numbers |
|---|---|---|
| pt-types-transcriptomic | blocked: data missing | |
| pt-types-shared-targets | blocked: data missing | |
| pt-upper-thalamus-projection | blocked: data missing | |
| pt-lower-medulla-projection | blocked: data missing | |
| pt-preparatory-activity | reproduced | 72 of 100 tagged units selective in the delay; shuffle p = 0.001 |
| pt-upper-early-preparatory | reproduced | 27 of 44 PTupper selective in the sample epoch; p = 0.001 |
| pt-upper-persistent | reproduced | late delay 27 of 44; sample/late-delay cosine 0.495, p = 0.016 |
| pt-lower-late-and-motor | partially reproduced | late delay > sample, p = 0.0096; response > sample, p = 0.088 |
| pt-types-differ-in-timing | not reproduced | sample PTupper > PTlower p = 0.134; response goes the opposite way (0.84 against 0.64) |

On the last claim, the paper's own coding-direction measure does point the way the abstract describes (PTupper 0.47, PTlower 0.22; PTupper higher in 83 of 100 bootstraps). I report it as a variant, so it doesn't change the outcome.

## 2. What was found about the dandiset

- **Contents:** 53 files from 12 mice, NWB 2.0.2. Tagged units are labelled PTupper (46 units, 8 mice) or PTlower (71 units, 4 mice). Each mouse has only one type, so a type comparison is also a comparison between groups of animals. There are no duplicate trial tables or spike trains.
- **Spike times are unsorted in 1120 of 1149 units.** They were written as trial start + cue time + time from the cue, trial by trial. I confirmed this exactly for 57 units against the paper's processed data on Figshare. Each trial's spikes cover 6.4 s, and trial starts are 6.4 s apart, so neighbouring trials overlap on the file's clock: 11.7% of baseline-epoch spikes are detectably out of order. The first 10 trials of the checked session are shifted by about 2.7 s.
- **Other format problems:** `stop_time` is NaN in every file, and the trial event times are relative to the trial start without the files saying so.
- **Missing descriptions:** PTupper and PTlower are not described, and their projection targets are named only in the paper's code. Unit quality uses mixed vocabularies with empty values. Sex is unknown, genotype is empty and electrode positions are all zero.
- **Missing data:** the transcriptomic and anatomical data are not in the dandiset.

## 3. Where the protocol was unclear, wrong or missing something

1. **Abstract-only claims have no numbers.** All criteria and tests of chance are my own. I wrote them before any claim analysis and said so in the claims file.
2. **"Abstract only" against other public parts of the paper.** It doesn't say whether the public Data availability statement or the Extended Data legends on the paywalled page may be used. I used the statement only to find the code and data, and nothing else.
3. **A background sentence in the abstract.** It doesn't say whether "preparatory activity has been observed in PT neurons" is a finding of the paper. I included it as a claim and labelled its source as background.
4. **Linked code that ships processed data.** It doesn't say how to treat this case. I used the code for method choices, and read one processed file only in the data check, to explain the spike storage. No claim depends on it, so every claim is `data: dandiset`. Both are listed under `inputs`.
5. **The clock check doesn't cover data that is on the trial clock but has trials overlapping.** I analysed on the file's clock as published, measured the overlap, and added a variant that drops the overlapping spikes the storage order reveals. No outcome changed.
6. **Same neuron across sessions.** The protocol covers analyses that treat a unit as the same across sessions, not the reverse risk of counting one neuron several times. I stated it as an assumption and gave results by animal.
7. **Short sessions in the clock check.** It doesn't say what to do when decoding can't decide. Seven 1-2 unit sessions couldn't be checked; I named them and assumed the clock.
8. **Comparing the two types when each animal has one.** I tested at unit level as the code does, gave animal-level tests as variants, and recorded the confound as a deviation.

## 4. Runtime and failures

- **Runtime:** the notebook runs in 50 s in the clean environment; loading the files takes about 20 s.
- **Fixed during development:** a duplicate-index error in a pandas `concat`, and a `remfile` object that `zipfile` couldn't seek (worked around with a small wrapper).
- **Left alone:** untracked files at the repository root (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others) were not created by me. An empty `.claude/` folder inside the entry comes from the harness and isn't tracked by git.

Files are in `entries/000006-economo-2018/`:
- `reproduce_economo_2018.ipynb`
- `alm.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

Two more files are outside it:
- `claims/000006/10.1038-s41586-018-0642-9.yaml`
- `attempts/000006-economo-2018-01.yaml`
