I've finished steps 1 to 5 of the Author section and run the handover (step 6). The notebook runs from a clean environment in 28 minutes, the entry checks pass with 0 errors, and nothing is committed.

The main fact: **DANDI:001048 holds none of the paper's data.** It contains HEK-cell TIRF recordings from another study and only names the paper as related. I pinned 001048 at 0.250701.1624, its only published version, and ran every claim (all `data: elsewhere`) on the ten dandisets the paper lists, each at its only published version.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| ap-selection | partially reproduced (assumed) |
| fig1-pure-sine-excites-all | partially reproduced |
| fig1-excitation-block | not reproduced |
| fig1-20khz-needs-twice-the-field | partially reproduced |
| fig2d-5ap-above-1ap | reproduced |
| fig2d-modulated-thresholds-higher | partially reproduced |
| fig2-modulated-locks-to-beats | reproduced (assumed) |
| fig2c-pure-more-aps | reproduced |
| fig3b-low-conductivity-halves-threshold | blocked: other (data not deposited) |
| fig3-extrapolated-threshold | blocked: other (depends on fig3b) |
| fig3-not-heating | blocked: methods_underspecified |
| fig3c-sustained-firing-2s | partially reproduced |
| figs1-di8-same-as-fluovolt | partially reproduced (assumed) |
| figs2-ttx-blocks-depolarization | partially reproduced (assumed) |
| fig4-pooled-time-constants | not reproduced (assumed) |
| fig4-orientation-and-poles | blocked: metadata_insufficient |
| fig5-sine-asymmetry | blocked: metadata_insufficient |
| fig5-whole-cell-depolarization | blocked: metadata_insufficient |
| fig6-sine-less-than-pulse | partially reproduced (assumed) |
| threshold-depolarization-estimate | not reproduced (assumed) |

## 2. The dataset, assumptions and questions

**Findings about the data:**
- 001034 is a pixel-identical copy of 001032 (178 recordings under other subject names); it is counted once.
- 001030 says its neurons are mouse, where the paper used rat. 001030 also makes each session a separate subject.
- Stimulus voltages are uncalibrated generator settings; the files say the calibration is "reported separately", and it is in none of the dandisets.
- No low-conductivity 250-ms sessions are deposited (Figures 3A and 3B). Only 3 of the 8 Di-8-ANEPPS neurons are deposited.
- The TTX session descriptions contradict the paper and the dandiset's own description; the vehicle neurons carry no mark of when the vehicle was applied.
- The strobe files hold no ROIs, cell shapes, experiment identities or stimulus waveforms.
- Every file's frame 0 is an artefact, and 59 sessions end before their stimulus does.
- The dandisets also hold stimuli the paper never mentions (20 Hz to 10 kHz sine waves, 100-kHz pulses, TTX strobe sessions).

**Assumptions:**
- The soma ROI is the deposited 16×16 crop. The claims file's Otsu masks are 1 to 39 pixels and twice as noisy; their results are shown alongside.
- The modulated waves start at minimal amplitude, and the sustained-depolarization level is half the neuron's AP height.
- Vehicle neurons are split into before and after at the longest pause between sessions.
- Strobe ROIs are 12×12-pixel boxes, frames are scaled to the image median, and the fields are the paper's 257 and 136 V/cm.
- The field is 36 V/cm per volt of amplitude, and the per-ROI slope is the signed regression.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How the soma ROI was drawn and how APs and their duration were measured.
- The voltage calibration.
- The strobe ROI size, which groups are the 19 Figure 4 experiments, and which cells are C1 to C9.
- The phase of the modulated waves.
- Which field and heat capacity give 2.5 °C.

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. Here the "elsewhere" data are other dandisets in the same archive, while the target dataset holds nothing. I pinned the target's version and listed the ten dandisets under `inputs`.
2. `tools/entry.py check` rejects `data_missing` for `elsewhere` claims, even when the data are in no archive (fig3b). The protocol says such claims should be `data_missing`, but the claims file fixes `data`. I used `other` and explained in the notes.
3. The claims file's header says to block a claim when readings disagree; protocol step 1.6 allows adopting the best-supported reading as an assumption. I followed the protocol.
4. The protocol does not say whether the author may add a reading the claims file lacks. I added the crop ROI (from the paper's "entire cell soma") and showed every reading.
5. The claims file's 5-SD AP reading misses most APs on these noisy masks. I kept it and showed its results.
6. Expected values defined "for each frequency" or "for each type" get only one number under `measured`. I recorded one value and named it in the notes.
7. There is no finding kind for duplicate deposits; I used `other`.
8. No stimulus timing is stored, so the clock check uses the AP rate before onset, during the stimulus and after it, plus sham sessions.
9. The 10-minute runtime target cannot be met with 11 GB of strobe data; the notebook takes 28 minutes, within the 60-minute limit.
10. During development I kept derived traces (not NWB files) in the scratch directory, to avoid re-streaming.

## 4. Runtime and failures

- The run took 03:35 to 05:57 UTC, about 2 h 20 min.
- The notebook takes 28 min, of which about 9 min is Figure 4 and 5 min is Figure 6.
- Nothing failed in the final run. During development I fixed a missing import, a misplaced helper definition and a print-format bug.

The handover package is in `executed/001048-semenov-2025/handover/`.
