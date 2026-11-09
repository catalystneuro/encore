The entry ran clean and the verifier's handover is built in `executed/000034-buccino-2020/handover/`. Only 1 of the 24 claims could be tested, and it reproduced; the other 23 are blocked because the paper's six spike sorters cannot be run here. Nothing is committed.

**1. Outcomes** (`attempts/000034-buccino-2020-01.yaml`)

| Claim | Outcome |
|---|---|
| recordings-as-described (link) | reproduced (all 15 checks hold) |
| fig4a-curators-agree | blocked, not_runnable. It depends on the blocked fig1b-unit-counts. Computed anyway from the two curated files: 226 shared units of 351 (64.39%), exactly the paper's 226 and 351. The paper's 174 needs the Kilosort2 run. |
| fig1b, fig1c, fig1d, fig1s2, fig1s3-s4, fig2c, fig2s1a, fig2s1b, fig2d, fig2e (×3), fig3a, fig3b, fig3c, fig3s1 (×2), fig3d, fig3s2, fig4b, fig4c, fig4d (22 claims) | blocked, not_runnable |

**2. What was found about the dataset.** I pinned 0.211030.0713: the paper cites only the draft, and this is the only published version, with the same six files (same ids and sizes) as the draft.
- **Contents:** all four recordings and both curations are there, with the stated rates, channel counts, durations and 250 ground-truth units. No sorter output is deposited, including the Kilosort2 run the curators worked on.
- **Clocks:** on the first seconds read, the curated and ground-truth spike times line up with spikes in the raw traces (deepest trough at lag 0).
- **Curated files:** spike times only. They have no sampling rate, no unit labels, no link to the Kilosort2 clusters, and nothing says which file is curator 1.
- **Retina recording:** stored as raw 12-bit converter counts (centred near 2048, saturating at 4096), but the file says 1e-6 V per count with no offset. Recorded as a metadata error.
- **Missing descriptions:** electrode location and filtering are placeholders; nothing marks which 2 of the 248 mouse channels are inactive (the paper says 246); the simulated file does not record cell types; the archive's species summary omits the rat.
- **Streaming:** every raw series is stored one channel per chunk, so reading any recording whole would take 6.7 to 20 h.
- **Paper:** 226/351 is 64.39%; the paper prints 64.2%.
- **Questions asked:** none. The one tested claim was fully specified.

**3. Protocol gaps**
1. The rule "a claim that depends on a blocked claim is blocked" forced fig4a to blocked even though its curator counts were computed and match. I followed the rule and put the numbers in the notes. The protocol has no outcome for a claim tested only in part because one of its parts is blocked.
2. When sorting software cannot run, `not_runnable` and `too_large` overlap: streaming alone would also exceed the time limit. I used not_runnable, citing MATLAB/GPU as the main reason and the measured streaming times in the notes.
3. The paper-era libraries (spikecomparison 0.2.6, spikeextractors 0.8.4) do not run on the fixed Python 3.13 with NumPy 2. The protocol says nothing about restoring removed library names. I restored five NumPy aliases (`np.float` and others) to their original meanings, which changes no computation, and recorded it as a deviation. The multi-sorter comparison in the same library also fails under pandas 2 and later, but every claim that uses it needs sorter outputs anyway.
4. The protocol's 10-minute aim is hard to meet when the data check itself needs slow raw reads. I read only the first chunk of each recording.

**4. Runtime and failures.** The notebook ran in 288 s. One exploratory metadata listing timed out at 20 minutes, because walking every electrode column is very slow over the network; targeted reads replaced it. HerdingSpikes 0.3.7 failed to build; Tridesclous 1.6.0 and SpyKING Circus 0.9.7 installed, but SpyKING Circus has no MPI to run with. Some empty device files (`.bashrc`, `scripts` and others) appear as untracked in `git status`; they come from the sandbox, not from me, and I left them alone.

Files are in `entries/000034-buccino-2020/`:
- `reproduce_buccino_2020.ipynb`
- `si000034.py`
- `entry.yaml`
- `requirements.in` and its lock file
- `README.md`
