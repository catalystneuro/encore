Steps 1 to 6 are done. The entry passes `check`, and `all` ran the notebook from a clean environment in 8.3 minutes with no errors. I read the executed copy and its numbers match every conclusion, and the handover package is built. Nothing is committed.

## 1. Outcome per claim (35 claims)

| Claim | Outcome |
|---|---|
| control-cohort-trial-counts (link) | reproduced: 2557, 2663, 2042, 3081 against 2490, 2629, 2027, 3021 (assumption) |
| control-decode-counts (link) | partially reproduced: 3 of 4 rats match; jaq is +15% (assumption) |
| fig2s1h-control-dwell-increases | reproduced (assumption: how "leaving the port" is read) |
| fig3a-control-speed | reproduced under every reading |
| fig5s1-control-search-efficiency-increases | reproduced (assumption): r > 0 in all 4 rats, none significant |
| fig1s1c-prereward-dwell-matched | partially reproduced: 2 of 3 rats within 10% (bernard 10.2%) (assumption) |
| fig2e-postreward-dwell | partially reproduced: tests hold, but NF over control ratio is 0.36 to 0.39, below the 0.4 tolerance (assumption) |
| fig3a-speed-below-immobility | partially reproduced: holds in all 3 testable rats (assumption) |
| fig5a-search-efficiency | not reproduced: no improvement of delay trials over control (p = 0.75) (assumption) |
| fig5b-redundant-search-balanced | not reproduced under the adopted plateau reading: gus p = 0.013 (assumption) |
| fig5c-repeat-accuracy-unchanged | partially reproduced: holds in all 3 testable rats (assumption) |
| fig5d-repeat-errors-balanced | partially reproduced: holds in all 3 testable rats (assumption) |
| 23 claims on SWRs and replay | blocked, too_large |

The last seven rows rest on three of the four neurofeedback rats, because rat 1 (remy) cannot be used.

## 2. Dataset, assumptions and questions

**What was found:**
- **No SWR or replay data.** Both dandisets hold only raw 30 kHz signals, head position, port events and statescript logs. There is no LFP, no SWR detections, no sorted spikes and no decodes. The SWR claims would need about 1.1 TB (control) and 1.9 TB (neurofeedback) streamed at about 2.2 MB/s per stream, so they are blocked as too large.
- **CA1 tetrodes cannot be identified** in 000115: every electrode's location is `None` (major).
- **Epoch flags absent** in 000115: forage assist and decode quality are not marked. jaq has 27 run epochs where the paper's replay analyses use 24 (minor).
- **NaN position timestamps** in 110 of 116 run epochs of 000115 (minor).
- **Corrupted port events in 000629** (major). remy's DIO is corrupted on day 7 and days 14 to 34, and gus's on days 16 and 17. There are thousands of pump onsets per epoch, sleep epochs included. This removes rat 1 from every analysis.
- **Other 000629 metadata problems:**
  - Position conversion factor is 0 (minor).
  - All 29 of remy's sessions start on 1970-01-01 (minor).
  - Nothing marks the neurofeedback phase, the threshold, the plateau or which port is the neurofeedback port; every run task is described as "pretraining" (major).
- **000629 should be listed for this paper.** The paper deposited it, but `papers/datasets/gillespie-2024.yaml` does not list it. I used it as an input.

**Assumptions:**
- **Trial parser.** The lab's parser is not public, so I wrote one from the port events. The trial counts match the paper within 3%.
- **"Leaving the port".** I adopted the last beam-off before the next port visit; the first exit longer than 200 ms is the variant.
- **Redundant search.** Two readings are run.
- **Speed smoothing.** Gaussian sd 0.1, 0.25 and 0.5 s are run, with the same outcome.
- **000629 position scale.** I used 0.2 cm per pixel, taken from 000115.
- **Neurofeedback port.** The R port, shown by the yoked delays (90% of W-port waits match one of the 8 previous R-port waits within 0.1 s, against 8% the other way).
- **Plateau.** The final whole days whose trial counts match the Figure 2C legend within 1% (gus days 26 to 30, bernard 19 to 28, fievel 18 to 29). The Methods' last 7 and last 10 days are run as other readings.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which days and epochs form each rat's plateau? The count match gives 5, 10 and 12 days, where the Methods say 7 to 10.
- How is leaving the port defined after reward, and what counts as a redundant search?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. A dataset the paper deposited but the registry does not list must go under `inputs`, yet `tools/entry.py check` rejects `datasets: ['000629']` on a finding about it. I removed the field and named DANDI:000629 in each finding's statement.
2. The protocol does not say how to judge a claim whose criterion says "all four rats" when one subject is unusable because of the data. I tested the three usable rats and capped the outcome at partially_reproduced when all three hold.
3. The claims file marks these claims `data: elsewhere`, which assumes the data are outside the paper's datasets. The protocol also says a dataset the authors deposited for the paper is one of its own datasets. These two rules overlap for 000629; I followed the claims file for `data` and the protocol for `inputs`.
4. Selecting epochs by matching the paper's published trial counts is not covered: it sits between a link claim and an assumption. I recorded it as an adopted assumption and ran the Methods' readings next to it.
5. `too_large` assumes something was computed. For the SWR claims I measured the streaming rate in the notebook and scaled it up, without running a subset.
6. Every tested claim rests on an analysis-side parser that the trial-count link claims validate. Whether that counts as an "assumption" (`assumed: true`) is unclear; I marked it on all tested claims except fig3a-control-speed, which agrees under every reading.

## 4. Runtime and failures

- **Runtime:** 1 h 20 min (16:56 to 18:16 UTC). The notebook takes 8.3 minutes and peaks at 0.55 GB of memory.
- **Failures:**
  - My attempt to delete a harness folder (`entries/gillespie-2024/.claude/.cc-writes`) and `__pycache__` was denied, because file deletion needs an approval this session cannot give. `__pycache__` is gitignored; `.claude` does not appear as untracked.
  - The repo root shows untracked entries (`.bashrc`, `.idea`, `scripts` and others). They are sandbox device mounts and not mine.

Files are in `entries/gillespie-2024/`:
- README.md
- entry.yaml
- nfbehavior.py
- reproduce_gillespie_2024.ipynb
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/gillespie-2024-01.yaml`.
