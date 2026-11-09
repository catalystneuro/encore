I tested the claims on DANDI:001559, recorded the attempt and built the verifier's handover. The entry is `entries/001559-tian-2025/` and the record is `attempts/001559-tian-2025-01.yaml`. Version 0.250902.2058 is pinned because the paper cites no version and it is the only published one; the draft has the same 35 files.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4b-expression-healthy | reproduced |
| fig4c-speckle-responsive-region | blocked, `metadata_insufficient` |
| fig4d-steady-baseline | partially reproduced (`assumed: true`) |
| fig4d-evoked-increase | blocked, `methods_underspecified` |
| fig4d-4ma-single-trials | blocked, `methods_underspecified` (depends on evoked-increase) |
| fig4d-electrode-timing | blocked, `methods_underspecified` (depends on evoked-increase) |
| 15 claims outside Figure 4 (Figures 1, 2, 3, 5, S2, S3, Table S1) | blocked, `data_missing` |

- **Expression (4B):** the cell stack shows 184 or 91 cell-sized bright objects, depending on the detection scale.
- **Baseline:** in the first stimulated recording the baseline drifts by 18.3 units, more than the mean 4 mA response (17.4 or 14.1 by window). The other three recordings pass.
- **Evoked increase:** three of four sessions respond clearly. The last one (15:04) is significant only with the 0 to 5 s window and the t-test (p = 0.046). The Wilcoxon test gives p = 0.116, and the 0 to 10 s window fails both tests. The criterion blocks the claim when its readings disagree.
- **Single trials and timing:** both analyses ran, and the record and notebook give the results they would have had. Under the assumed current, all 15 trials at 4 mA are detected. The "one electrode has both the later peak and the later rise" condition holds only at 2 mA.

## 2. The dataset, assumptions and questions

**What is in it:**
- Only one mouse; the paper used six.
- Everything is stored as two-photon image series, with no stimulus table.
- The stimulus times exist only as an undescribed image channel 1. Its 5 s pulses measure 4.985 to 4.992 s once the edges are placed within frames.
- Nothing says which electrode or current each session used, or which channel is which detector.
- The three April 7 movies are labelled two-photon but look like multi-exposure laser speckle imaging. They have no stimulus times.
- The stated pixel size (0.028 µm) would make the field 14.4 µm across, which cannot be right.
- The analysis scripts the description mentions are not in the dataset.
- There is no surgery date, and two of the six bioluminescence recordings have no stimulation and are not described.

**Assumptions:**
- Each of the four stimulated sessions is one of the four conditions.
- The two sessions with the larger responses are the 4 mA ones.
- Channel 4 is the 645/65 detector. It shows the red expression without the green-labelled vessels; channel 3 is shown as a variant and gives the same outcomes.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which response window and test establish the Figure 4D increases?
- Which session used which electrode and current, and which channel is the 645/65 detector?
- When was the whisker pad stimulated during the speckle movies?

I asked a reader no questions.

## 3. Protocol issues

1. The rule "a claim that depends on a blocked claim is blocked for the same reason" does not fit here. The single-trial and timing claims depend on evoked-increase only to choose which mice to use, and there is only one mouse. I followed the rule and gave the results they would have had in the notes.
2. The steady-baseline criterion compares the drift with "the 4 mA response in the same recording", but each recording holds one current. I compared with the mean 4 mA response of the same channel and showed the recording's own response as a variant. Both are recorded as deviations.
3. The protocol has no guidance for condition labels that are missing but can be partly inferred from the paper (4 mA gives the stronger response). I adopted that as an assumption and showed all six ways of pairing sessions into currents.
4. There is no guidance for stimulus events stored as an image channel. I treated it as the stimulus marker after checking its pulses against the Methods' 5 s trains.
5. The supplement PDF could not be rendered (no poppler); I read its text with pypdf instead. It holds nothing on Figure 4.

## 4. Runtime and failures

The run took about 63 minutes (03:21 to 04:24 UTC). The notebook runs in about 7.5 minutes (452 s in the clean environment). Lock, check and run passed with 0 errors, and the handover is built. Nothing failed.

Some untracked placeholder files (`.bashrc`, `.idea`, `scripts` and others) sit in the repo root. They were created at 03:19, before the run started, so I left them alone.
