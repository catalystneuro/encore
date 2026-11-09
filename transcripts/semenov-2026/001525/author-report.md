The attempt on DANDI:001525 is written up, locked, checked and run (`entry.py all`: 0 errors, notebook passes in 247 s), and the verifier's package is built. Of the 27 claims, 4 could be tested; the other 23 are blocked because their data are not in the dataset or because the test readings disagree. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig7a-test-pulse-cosine-up-to-1000 | reproduced, resting on assumptions; holds in 9 of 18 variants |
| fig7b-test-pulse-unchanged-to-760 | blocked: methods_underspecified (the paired and unpaired t-tests disagree, as the criterion foresees) |
| fig7b-test-pulse-reduced-1200-1400 | not_reproduced: anodic values 73.3% and 50.1% are within tolerance, but the required significance is not reached |
| fig5b-conductivity-calibration | partially_reproduced: 11.87% for a 100-fold rise matches; 1.33% for a 10-fold rise, against about 2% |
| fig7b-conditioning-pulse-below-linear | blocked: data_missing (the Fig. 4B images are not here) |
| fig7c-conductivity-drops-10-fold, fig7c-full-reseal-mild-residual-strong | blocked: data_missing (they depend on the claim above) |
| fig1, fig2 (6), fig3 (2), fig4 (6), fig5a (2), fig5c, fig6 (2) | blocked: data_missing |

## 2. The dataset, assumptions and questions

**What the dataset holds.** Version 0.261006.1856 is pinned: it is the only published version, and the paper cites none. The files hold only the Di-8-ANEPPS two-pulse experiment of Fig. 7: 10 cells, 73 sets of 100 images.
- Six cells (c5 to c10) have the paper's 5-µs interval, where the paper reports n = 5 and does not say which five.
- Four cells (c1 to c4) have a 1-µs interval that the paper does not report.
- Pulses are given in generator volts (50 to 350 V), not in V/cm.
- The files give the electrode gap as 1.00 mm; the paper gives 1.6 mm.
- The shared description lists field strengths and intervals (25 and 125 µs) that the files do not hold.
- The paper's 150/150 benchmark pair does not exist in the files; there is only a single 50 V pulse.
- 70 of 73 files have a dark first image with no laser flash.
- The series description says exposures began 1 µs after the start of recording; the images show the pulse from image 40.
- No recording is deposited twice.

**Assumptions** (all stated in the record, every reading shown in the notebook):
- Volts are mapped to the Fig. 7A labels by rank (100 V is 360 V/cm, up to 350 V for 1400 V/cm).
- The single 50 V pulse stands for the 150/150 benchmark.
- The analysed cell is the largest object in the field.
- The field direction is taken from the data (per-file phases within 6.6° sd).
- The perimeter trace is found automatically, not drawn by hand.
- All six 5-µs cells are used, with every five-cell subset shown.
- The main reading subtracts a background and drops dark frames. Only with a background removed does the dF scale match the paper's (10.9% against 5.0% at 150/150).

**Questions for the paper's authors** (`methods_unavailable` findings):
- Which t-test Fig. 7B used: paired over cells, or unpaired against the control group.
- Whether a background was subtracted from the potentiometric images, and whether images without a laser flash were kept.

**Question for a reader** (`questions/001525.yaml`): the paper reports its "accidental 120%" point at 360 V/cm as p > 0.1. That fits the unpaired test (p = 0.61), not the paired one (p = 0.0038). Should the criterion of fig7b-test-pulse-unchanged-to-760 take the unpaired test? Under that test the claim would be reproduced.

## 3. Where the protocol was unclear or did not fit

1. A second dandiset, 001526, names the same paper and may hold the Fig. 2C-D data. The protocol does not say whether a sibling dataset the paper never names counts as "deposited elsewhere". I did not use it: I blocked those claims as data_missing and mentioned 001526 in their notes.
2. When the dataset has more cells than the paper's n and the extra one cannot be identified, the protocol gives no rule. I used all cells and showed every leave-one-out subset.
3. "A claim that depends on a blocked claim is blocked" also blocked fig7c-full-reseal, although its test-pulse parts are testable from this dataset. I followed the rule and said so in the notes.
4. A criterion can say "methods_underspecified when the readings disagree" even when the paper holds evidence for one reading. The protocol has no path for this other than asking a reader, so I asked one.
5. "measured" for a claim with no matching reading is not defined. I recorded the first pole reading the criterion lists (cathodic).
6. For claims with no recorded data at all (fig5b is pure computation from Eq. 2), the `data` field does not fit well. I left the default.

## 4. Runtime and failures

The run took about 32 minutes (22:23 to 22:55 UTC). The notebook takes about 4 minutes, streaming 2.5 GB. Nothing failed.

The `git status` shows untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.

Files are in `entries/001525-semenov-2026/`:
- `reproduce_semenov_2026.ipynb`
- `strobe.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

Elsewhere:
- `attempts/001525-semenov-2026-01.yaml`
- `questions/001525.yaml`
- `executed/001525-semenov-2026/handover/`
