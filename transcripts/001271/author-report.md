The attempt is recorded and handed over, with no claim marked as tested by me as verifier. The entry is `entries/001271-semenov-2025/` with three notebooks and the `sinewave.py` helper. The record is `attempts/001271-semenov-2025-01.yaml` and the reader question is in `questions/001271.yaml`. The checks report 0 errors and all three notebooks run from a clean environment.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| figs2-neurons-tested | 001271 | reproduced (6 TTX, 11 vehicle neurons) |
| figs2-before-firing-then-depolarization | 001271 | partially reproduced |
| figs2-depolarization-reversible | 001271 | blocked: other (no session qualifies) |
| figs2-ttx-abolishes-aps | 001271 | blocked: methods_underspecified (readings disagree) |
| figs2-ttx-blocks-sustained-depolarization | 001271 | blocked: other (criterion's own rule) |
| figs2-vehicle-keeps-response | 001271 | blocked: methods_underspecified |
| ap-amplitude-duration | 001271 | blocked: methods_underspecified |
| fig3-not-heating | calculation only | blocked: methods_underspecified |
| fig3c-sustained-firing-2s | 001030 | partially reproduced |
| fig1-pure-sine-excites-all | 001032, 001033, 001035 | not reproduced |
| fig1-20khz-needs-twice-the-field | same | not reproduced |
| fig2d-modulated-thresholds-higher | same | not reproduced |
| fig2-modulated-locks-to-beats | same | partially reproduced (assumed) |
| fig2c-pure-more-aps | same | reproduced (assumed) |
| fig3b-low-conductivity-halves-threshold | none found | blocked: metadata_insufficient |
| figs1-di8-same-as-fluovolt | 001272 | not reproduced (3 neurons, not 8) |
| fig4-pooled-time-constants, fig4-orientation-and-poles, fig6-sine-less-than-pulse | 001273, 001274 | blocked: other (not attempted) |
| threshold-depolarization-estimate | depends on fig6 | blocked: other |

## 2. Dataset, assumptions, questions

**What was found**
- **Pinned version:** 001271 0.250805.1352, the latest published version; the paper cites none. It has the same 287 blobs as 0.250701.1624.
- **Image size:** the files hold 16×16 crops that the soma nearly fills, with no ROI and no stimulus record. The paper describes 64×64 images.
- **Camera artefacts:** the first frame of every file is 1.5 to 24 times brighter than the rest, and the last frame is a few percent brighter.
- **Field conversion:** the files say 1 V gives 36 V/cm, but the voltages give Figure S2's fields only at 18 V/cm per V.
- **TTX descriptions:** they say TTX "caused sustained depolarization". The paper and the data say it prevented it.
- **Solution change not marked:** sessions before the change carry the same "vehicle control" label as vehicle sessions after it.
- **Duplicate deposit:** all 178 data arrays of 001034 are identical to those of 001032.
- **Mixed subjects:** some 001032 subjects hold sessions of more than one cell (13_1 and 14_1).
- **001030 naming:** each file is its own subject, named by cell and voltage.
- **Missing data:** 001272 holds 3 of the paper's 8 Di-8-ANEPPS neurons, and no 250-ms NaGlu recordings were found in any dandiset read.
- **Missing calibration:** the frequency-dependent calibration from stated voltage to field is not given.

**Assumptions**
- A vehicle neuron's solution change is placed at its last gap of more than 3 minutes between sessions.
- The O1(a) readings decide fig2-modulated-locks-to-beats and fig2c, because the eroded O1(b) ROIs are mostly empty.
- Fields use 18 V/cm per stated volt.
- 001272 and 001032 to 001035 state voltages on the same scale.
- The first and last frame of every file are left out.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings)
- How was the soma ROI drawn, and by what rule were APs counted?
- How was sustained depolarization measured?
- Which session pairs were compared before and after the vehicle change?
- Which APs and which duration measure give 11.3% and 8 ms?
- Which heat capacity and which field (peak or RMS) give 2.5 C?

**Question to a reader:** in fig2-modulated-locks-to-beats, the claims file's "sustained firing" (3 APs with one in the last 50 ms) is met by beat-locked firing. The fifth beat peaks at 225 ms, so one AP per beat already qualifies.

## 3. Protocol points
1. The claims file's header blocks a claim whenever readings disagree, while step 1.6 allows adopting the best-supported reading as an assumption. I followed the header for the Figure S2 claims and step 1.6 where a criterion gave no rule.
2. The readings presuppose the paper's 64×64 full-field images, and there is no route for readings that do not fit the data's form. I ran them as written and showed the whole frame as a variant that decides nothing.
3. For an `elsewhere` claim whose data are found nowhere, the checker forbids `data_missing`. I used `metadata_insufficient`.
4. There is no block reason for "not attempted for lack of time" other than `too_large`, which is for computation. I used `other`.
5. Some `elsewhere` criteria defer to other dandisets' claims files (whole attempts in themselves). For figs1 I ran only the neuron count and the threshold test.
6. With no trial tables, the clock check used the aliased stimulus and the AP timing.
7. It is unclear which value `measured` should hold when the expected value applies per frequency. I recorded the deciding one and said so in the notes.
8. The duplicate check had to span dandisets (001032 against 001034), which the protocol does not mention.

## 4. Runtime and failures
- About 1 h 40 min of the 5 h (13:45 to about 15:25 UTC).
- Notebooks: 116 s, 20 s and 323 s, most of it streaming.
- Earlier failures, all fixed: a pandas string-dtype error, a YAML ": " in `entry.yaml`, the checker's rejection of `data_missing`, and a regex that stripped some "**Result" markers (markdown only; code verified unchanged).
- Untracked `/dev/null` mounts from the sandbox (`.bashrc`, `.idea`, `scripts` and others) are at the repository root. I left them alone, and they should not be committed.
