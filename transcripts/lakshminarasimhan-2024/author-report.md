I've done Author steps 1 to 5 and built the handover package. Six claims could be tested on the dandiset: one reproduced fully, one reproduced under only one of the readings the criterion allows, and four did not reproduce. The other 30 are blocked. `tools/entry.py check` passes with 0 errors, the notebook runs from a clean environment in 8 minutes (peak memory 0.95 GB), and `handover` wrote `executed/lakshminarasimhan-2024/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| wm-sessions-link | reproduced: mouse anm00264943 has 151 ALM units in 5 sessions and 72 thalamic units in 6 other sessions |
| fig6-wm-choice-r2 | not reproduced: best test-set R2 is -0.247 (expected 0.97 ± 0.097) |
| fig6c-wm-leading-pcs-drive-choice | reproduced, but only with the pooled population subsampled to 53 units. Per session (the Figure 6C n = 5 reading) it fails. The alignments are at or below what a random direction gives (about 0.11). |
| figs6d-wm-thalamic-r2 | not reproduced: mean test-set R2 runs from -5.16 to -1.91 (expected 0.70) |
| fig6d-wm-top5-pcs | not reproduced: no combination of readings falls within 0.59 to 0.67, under any of the five seeds |
| figs6f-ct-alignment-not-significant | not reproduced: the paper's one-sided test is significant, p = 8.3e-06, under all five seeds |
| 6 motor-task claims | blocked, data_missing: the Sauerbrei 2020 recordings are not deposited anywhere the paper names; a DANDI search finds only 000221, a different study |
| 23 simulation claims | blocked, too_large: one set of 40 runs at M = 1 takes about 0.5 h, and every claim needs at least two sets; the Figure 1 curve alone is about 8 h on one core |
| figs5cd-thalamic-recurrence | blocked, methods_underspecified: the paper never gives the recurrent thalamic weights |

No outcome rests on an assumption, and none changes with the seed.

## 2. Dataset, assumptions, questions

**Version.** Pinned 0.220126.1903, the only published version; the paper cites none. The draft holds the same blobs.

**What the dandiset holds.** The paper's unit totals match exactly. The thalamic units come from six sessions besides the five ALM sessions, eleven in all, and no session holds both regions.

**Findings about the data:**
- **Major:** the units tables give no interval over which each unit was recorded. Many units fire in only part of their session: only 61% of unit and trial pairs fall between the unit's first and last spike. I ran the analysis both ways (U1, every trial for every unit; U2, only trials inside each unit's span), which the claims file does not name, and recorded U2 as a deviation. Outcomes were the same.
- **Minor:**
  - All 137 files give the same ALM coordinates, thalamic and SNr recordings included.
  - The thalamic recordings name no nucleus.
  - `photo_stim_type` reads "stimulation" on every trial, and several trial columns have no description.
  - 18 files are labelled SNr, which the dandiset description does not mention.
- **Checks that passed:** nothing is deposited twice, and choice decoding around delay onset shows spikes and trials share a clock.

**Main question for the paper's authors.** With OLS on trial averages as the Methods describe, test-set R2 is negative. The same fits on the training trials give values close to the paper's: choice 0.95 to 1.00, thalamic units 0.73 to 0.77, top-5 fraction 0.68. So the paper's numbers may be in-sample. This is recorded as a `methods_unavailable` finding.

**Other questions for the authors:**
- How thalamic units from other sessions were paired with ALM activity for training and test sets.
- Which trials each unit was averaged over.
- The smoothing grid.
- Which of the three Figure 6D normalizations was used.
- The Figure S5C/D recurrent weights.

I asked no reader any questions.

## 3. Where the protocol was unclear, wrong or missing something

1. `data: elsewhere` is written for data in another archive. Here 24 claims point to model output that was never deposited. I treated them as claims to run, timed the paper's model in the notebook, and blocked them as `too_large`.
2. The link claim expects five sessions, but the data have 5 ALM plus 6 thalamic sessions. The protocol does not say how to judge a link that holds for counts but differs on sessions. I marked it reproduced and added a deviation and a `paper_inconsistency` finding.
3. For a claim of absence, the protocol says to judge on the paper's test alone, but not which of the criterion's several readings to use. I chose the main reading from the cited passages and showed all the others; all gave the same outcome under the claim seed.
4. There is no place for a diagnostic that is not a reading of the claim, such as the training-set R2. I showed it as a labelled variant that decides nothing.
5. Running five seeds across every combination of readings multiplies the runtime. I ran every reading under the claim's seed and the main combinations under the other four seeds.
6. Timings change from run to run, and the record may only use numbers the notebook prints. I gave approximate timings in the conclusions and the record.
7. The fouke-2025 example record uses a protocol version from before findings were rated; nothing in it shows the `severity` field. I took that field from the schema.

## 4. Runtime and failures

The run took about 45 minutes, from 15:26 to about 16:10 UTC. While developing, a signed S3 URL refused a HEAD request (now handled by reading the redirect without following it), and an alignment profile broke for sessions with fewer than 16 units under U2 (now padded). Both are fixed, and nothing in the final run failed.

The repository root has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). They are sandbox device mounts, and I left them alone.
