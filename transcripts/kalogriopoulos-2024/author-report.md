All 32 claims are blocked. The dataset holds the slice recordings, but no file says which cells got DCZ alone and which got DCZ plus mCherry, or when DCZ was applied. The entry, the attempt record and the verifier handover are done. The entry passes `python tools/entry.py all` (0 errors, notebook runs in 969 s). Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| methods-slice-sample | Blocked, `metadata_insufficient`. The files hold 50 cells from 8 mice; the paper's Rin exclusion keeps 49. The per-condition counts can't be formed. |
| methods-mcherry-preincubation | Blocked, `data_missing` |
| fig4i-rmp-hyperpolarization | Blocked, `metadata_insufficient` (no condition, no DCZ onset time) |
| fig4j-rheobase-increase | Blocked, `metadata_insufficient` |
| ed12b-input-resistance-trend | Blocked, `metadata_insufficient` |
| ed12cd, ed12ef, ed12g (mEGFP correlations) | Blocked, `data_missing` (no mEGFP intensity, images or ROIs) |
| 24 culture, imaging and biochemistry claims | Blocked, `data_missing` |

## 2. Dataset, assumptions, questions

- **Version.** I pinned 0.250312.0036, the only published version; the paper cites none.
- **Missing records.** No file records the condition, the DCZ onset, mEGFP intensity or preincubation time. A scan of every text value finds none, and the conditions appear only in the dandiset's description.
- **Cell counts.** 50 cells from 8 mice, against the paper's 41 cells from 7 and 6 mice. Nothing marks which cells the paper analysed. No recording is deposited twice.
- **Channel 1** is stored as a voltage series ("volts") but holds the injected current in amperes.
- **Stimulus series.** It shows the ramp as a step to +500 pA in every file. The real ramp is only in channel 1, so I read rheobase from there and recorded that as a deviation.
- **Ramp duration.** In 10 of 50 cells the ramp reaches +500 pA after 1.6 or 1.4 s, not the 2 s of the Methods. That makes their absolute rheobase not comparable with the other 40 cells. Every sweep also holds -150 pA for 100 ms before the ramp, which the Methods don't mention.
- **Other mismatches.** The files are sampled at 20 kHz, where the Methods say 10 kHz. Two mice were 101 and 107 days old at recording, older than the Methods' timeline allows (at most 98). Experimenter, lab and institution are "_".
- **Checks that passed.** Voltage and current share the sweep clock. 49 of 50 cells start within 3 mV of -65 mV, as the Methods say they should.
- **Assumptions:** none, since nothing was tested.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which change windows, mixed-model unit, spike detection rule and Rin window they used, and which 41 cells were analysed, in which group.
- **Questions to a reader:** none.

## 3. Protocol gaps

1. The protocol doesn't say what the notebook should hold when every claim is blocked. I kept the data checks and the paper's per-sweep measures and exclusions. I tagged the counts cell `claim:methods-slice-sample` and pointed that blocked outcome at it.
2. "A claim that depends on a blocked claim is blocked for the same reason" clashes when the claim has its own, different reason. For the ed12 claims I gave `data_missing` as the main reason and named the dependency in the notes.
3. The criterion says to read rheobase "from the recorded stimulus", but the stored stimulus is wrong. The protocol doesn't cover a source the claims file names being wrong in the data. I used the current channel and recorded a deviation.
4. Step 1.6 questions for authors normally come out of testing. With everything blocked by missing metadata, I still added the one `methods_unavailable` finding.
5. Condition labels held only by the authors sit between `metadata_insufficient` and `data_missing`. I used `metadata_insufficient` for the labels and onset, and `data_missing` for the mEGFP and preincubation values.
6. "Survey metadata, not data" was slow here: about 600 series per file made the metadata survey take 16 minutes.

## 4. Runtime and failures

- **Session:** 07:36 to about 09:24 UTC, roughly 1 h 50 min.
- **Notebook:** about 16 min (969 s) per full run, peak memory 0.49 GB.
- **Failures:** none in the final run. During development I found a wrong ramp fit and a wrong sentence about early spikes; both were fixed and re-run.
- **Stray files:** untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and others) are in the repository root, and an empty `.claude/.cc-writes` folder is inside the entry. They look like environment artifacts. I left them alone, so they need excluding before the workflow commits.

Files are in `entries/kalogriopoulos-2024/`:
- `README.md`
- `entry.yaml`
- `pager_slice.py`
- `reproduce_kalogriopoulos_2024.ipynb`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/kalogriopoulos-2024-01.yaml`.
