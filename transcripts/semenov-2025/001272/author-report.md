The attempt is written up and handed over; I did not verify it myself. Of 19 claims, 13 were tested and 6 are blocked. `python tools/entry.py all` passes with 0 errors, all three notebooks run cleanly, and their outputs match my development runs exactly. The handover package is in `executed/001272-semenov-2025/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Data | Outcome |
|---|---|---|
| figs1-eight-neurons | 001272 | not reproduced (3 neurons) |
| figs1-aps-as-emission-decrease | 001272 | reproduced |
| figs1-near-threshold-delayed-aps | 001272 | partially reproduced (assumption) |
| figs1-stronger-field-shorter-delay-sustained-firing | 001272 | reproduced (assumption) |
| figs1-culminates-in-sustained-depolarization | 001272 | not reproduced |
| figs1-noisier-than-fluovolt | with_inputs | partially reproduced |
| figs1-effects-same-as-fluovolt | with_inputs | partially reproduced (assumption) |
| fig1-pure-sine-excites-all | 001032/33/35 | not reproduced |
| fig1-20khz-needs-twice-the-field | 001032/33/35 | not reproduced |
| fig2d-modulated-thresholds-higher | 001032/33/35 | not reproduced |
| fig2-modulated-locks-to-beats | 001032/33/35 | partially reproduced (assumption) |
| fig2c-pure-more-aps | 001032/33/35 | reproduced |
| fig3b-low-conductivity-halves-threshold | none | blocked, `other` (no deposit holds these data) |
| fig3c-sustained-firing-2s | 001030 | partially reproduced (assumption) |
| figs2-ttx-blocks-depolarization | 001271 | reproduced (assumption) |
| fig4-pooled-time-constants | 001273 | blocked, metadata insufficient |
| fig4-orientation-and-poles | 001273 | blocked, metadata insufficient |
| fig6-sine-less-than-pulse | 001274 | blocked, `other` (not attempted) |
| threshold-depolarization-estimate | depends on fig6 | blocked, `other` |

**2. What was found**

The dataset:
- **Version:** I pinned 0.250805.1358, the latest published version. The paper cites no version, and the earlier one (0.250701.1622) has the same blobs.
- **Contents:** 3 neurons where the paper reports 8. Frames are 16 x 16, where the Methods say 64 x 64.
- **Missing metadata:** the stimulus onset is not stored, and frame 0 of every file is an artefact.
- **Wrong metadata:** every file calls itself a tetrodotoxin vehicle control, which this experiment was not.
- **Session spacing:** 33 of 62 intervals between sessions are under the 20 s the Methods give.

The other deposits:
- **Duplicate:** 001034 is a byte-identical copy of 001032.
- **Amplitudes:** stated as peak-to-peak in 001032 to 001035, as one polarity in 001030, and unspecified in 001272 and 001271. All use 36 V/cm per volt, and the files say the delivered amplitude is smaller by a calibration that is not deposited. As a result the 2-kHz threshold comes out at about 150 V/cm, against the paper's 57.7.
- **TTX metadata contradicts the data:** the 001271 TTX files say tetrodotoxin "caused sustained depolarization". The data show none (late dF -0.4 to -0.7%), and the paper says it blocked it.
- **Figure 3B data:** no deposit holds the 250-ms sodium gluconate sessions.
- **001273:** the debris ROI used for scaling, the ROIs over the cell poles and the cell-shape labels are not deposited. The files form 22 experiments where the paper reports 19.

Assumptions, each recorded as a deviation:
- The whole 16 x 16 frame is the soma ROI. The claims file's Otsu ROI keeps one membrane edge and detects APs in sham sessions.
- AP height for Di-8-ANEPPS is 5 SD of the pre-stimulus trace.
- "Delayed" means at least 100 ms after onset.
- The 001272 volts are on the same scale as the peak-to-peak volts of 001032 to 001035. The 001271 thresholds support this (p = 0.29).
- In 001271, the vehicle was added at the largest gap between sessions.

These go to the paper's authors as one `methods_unavailable` finding with five questions.

I asked a reader one question, in `questions/001272.yaml`. Header item O3 sets a 2 to 20 ms AP width at half height, but the paper gives an 8-ms total duration, and the FluoVolt APs here are about 2 ms wide at half height. A 1-ms variant changes fig2-modulated-locks-to-beats from 8 of 12 readings meeting its criterion to 4 of 12.

**3. Protocol gaps**
1. A claim marked `elsewhere` whose data are in no archive (fig3b) cannot be `data_missing`, because the checker rejects it. I used `other` and said why.
2. The protocol does not say how far an author should go on `elsewhere` claims that are full targets of their own (001273 and 001274 have 17 and 26 claims). I checked 001273 on one experiment, in its own notebook so the block rests on printed numbers. I did not attempt 001274.
3. When a claims file's standard choice proves unworkable on the data (O1 Otsu, O3 width), the protocol doesn't say whether to add a reading or ask a reader. I added the whole-frame ROI as a reading, ran the 1-ms width as a variant, and asked a reader about the width.
4. Some criteria don't say whether a pattern is judged per neuron or in the representative neuron (fig3c). I judged per neuron and recorded the outcome as partial.
5. Where a criterion names no rule for disagreeing readings, the protocol says to adopt the best-supported choice. I adopted one ROI across claims for consistency; the protocol doesn't say whether that is required.
6. The questions file format is not specified: existing files use `dandiset:` or `dataset:`. I followed the DANDI example.

**4. Runtime and failures**

About 1 h 20 min (14:18 to 15:39 UTC). The notebooks take 201 s, 245 s and 95 s. The first notebook build failed only because nbconvert was missing from my scratch environment; nothing failed in the final runs. The untracked dotfiles in the repo root (`.bashrc`, `scripts` and others) are sandbox placeholders created before this run started; I left them alone.
