The dataset holds only the Figure 8 experiment, and all three Figure 8 claims came out not reproduced. The other 15 claims are blocked because their data are not in the dandiset. The entry passes `entry.py check` and `all` (the notebook ran clean in 233 s), and the handover is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4-unipolar-strongest, fig4-bipolar-weaker, fig4-sham-no-uptake, fig4-twenty-fold-cancellation | blocked, data_missing |
| fig5a-trains-stronger-throughout, fig5a-packet-center-peak-e1-stronger, fig5bc-rotation-focuses-center | blocked, data_missing |
| fig6a-more-packets-more-uptake, fig6b-center-to-periphery-by-number, fig6-peak-narrower | blocked, data_missing |
| fig7a-amplitude-scales-uniformly, fig7bd-targeting-independent-of-amplitude, array-size-independence | blocked, data_missing |
| fig8a-equal-center-uptake | not_reproduced: Packet 1's center is 649 a.u. against 388 and 383 for Packets 2 and 3, and it differs from both (p < 0.001) |
| fig8a-more-uptake-near-electrodes | not_reproduced: near the electrodes Packet 3 is below Packet 2 (296 against 481 a.u.), where the claim has it above |
| fig8b-packet2-best-targeting | not_reproduced: the normalized center is 82.8% for Packet 2 and 129.4% for Packet 3, against the paper's 183% and 83% |

Each Figure 8 outcome is the same under every reading of the open details (48, 48 and 96 readings), so none rests on an assumption.

## 2. The dataset

- **Contents.** I pinned version 0.240605.1859, the only published version; the paper cites none and the draft is identical. It holds ten dishes, each one stitched 20480×20480 image: Packet 1 has 3 dishes, Packet 2 has 4 and Packet 3 has 3, all at 4 kV with one rotation. No dish is deposited twice.
- **Which array.** The files give no pixel size. Assuming 0.65 µm per pixel (the paper's camera and 10x objective), the electrode spacing matches the paper's small array: an edge-to-edge diagonal of about 3.5 mm, which fits its ±1.65 mm ROI span.
- **Main finding: Protocol 2 and 3 labels appear swapped.**
  - The files labelled Protocol 3 (with 5-µs delays) show the central focusing the paper reports for Packet 2, and the files labelled Protocol 2 behave like its Packet 3.
  - With the two labels exchanged, the order of Figure 8B appears: fig8b would be partially reproduced in 92 of 96 readings and reproduced in 2.
  - The data alone cannot say whether the files or the paper have them the wrong way round. The outcomes above test the labels as given; the swap is shown as a variant and recorded as a finding.
- **Other findings.**
  - Missing metadata: there is no pixel size, nothing records where the electrodes are or which one is e1, and exposure and gain are not recorded.
  - Imaging day: the Packet 1 dishes were imaged on a different day, and their background is about twice that of the others (308 against 162 a.u.). This alone may account for their higher center value.
  - Smaller metadata errors: the species summary names two hamster species for one cell line, each dish is given an age of "P1D", and dish 10's file names no camera or objective.
- **Assumption.** The 0.65 µm per pixel scale. A placement rule that needs no scale gives the same outcomes.
- **Questions.** None for the paper's authors, since no outcome depends on an open method choice. None for a reader, since the claims file does not misread the paper.

## 3. Where the protocol was unclear or did not fit

1. The step-2 check that every data stream shares a clock does not apply to files holding one image each. I said so in the notebook.
2. The protocol has no finding kind for "the data and the paper disagree about which condition is which, and the data cannot say which is right". I filed it as `metadata_error` and worded it as apparent.
3. It does not say what `measured` should hold when the expected values are the two ends of a range. I recorded the lowest and highest of the per-packet values and said so in the notes.
4. One of the criterion's readings needs to know which electrode is e1, which the files do not record. The protocol has no rule for one unrunnable reading among several, so I showed the values next to each of the four electrodes. None of them would reverse the outcome.
5. With 48 to 96 readings per claim, it is unclear how much of each the notebook should print. I printed the main reading in full and the spread of outcomes and values over all readings.

## 4. Runtime

The run took about 40 minutes (01:14 to 01:55 UTC). Nothing failed.

Files are in `entries/001027-pakhomov-2023/`:
- `reproduce_pakhomov_2023.ipynb`
- `cancan.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/001027-pakhomov-2023-01.yaml`.
