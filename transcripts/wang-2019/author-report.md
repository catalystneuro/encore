I tested 13 of the 25 claims, and the entry passes its checks and a clean run (0 errors, notebook runs in 11 s). The other 12 are blocked: the dataset has no optical maps, and the model claims need MATLAB. The handover is built in `executed/wang-2019/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig1a-rabbit-hr-increase | reproduced (p = 0.0011, 5 of 5 hearts) |
| fig1d-mouse-hr-increase | reproduced (p = 0.0033, 5 of 5) |
| fig1bc-rabbit-ap-cat-response | reproduced, rests on an assumption (tested on the first 20 s of the Fig. 2 series) |
| fig1ef-mouse-ap-cat-response | reproduced, rests on an assumption (same substitution) |
| fig2a-rabbit-monotonic | partially reproduced: rabbit heart rate peaks at 20 s and falls (50→60 s, p = 0.047); CaTD is lowest at 25 s, then rises |
| fig2d-mouse-biphasic-apd | reproduced: 50.52 / 61.18 / 49.54 ms at 0 / 15 / 60 s, all within tolerance; peak at 15 s in every heart |
| fig2cf-cat-amplitude-similar | reproduced under similarity reading (b); reading (a) fails at 5 to 15 s |
| fig3abc-tyramine-na-mimic-sns | partially reproduced: with noradrenaline, heart rate falls after 30 s |
| fig3d-propranolol-abolishes | not reproduced: one unadjusted paired t-test (APD80 at 10 s, +1.4 ms) gives p = 0.010; nothing survives the adjusted comparisons |
| fig3e-rate-step-biphasic | reproduced (reading a) |
| fig3f-constant-pacing-sns-prolongs | reproduced, rests on an assumption (column pairing) |
| fig4g-5f-rabbit-base-apex | reproduced (p = 0.048) |
| fig7f-mouse-base-apex | reproduced (p = 0.0019) |
| fig4ab, fig4cd, fig4e, fig5c, fig6ab, fig6e, fig6fh, fig7c | blocked, `data_missing` |
| fig8e, fig8f, fig8ij, fig9 | blocked, `not_runnable` (MATLAB models) |

**2. The dataset, assumptions and questions**

- **What it holds:** the files are only 3.5 MB. The useful part is one workbook with per-heart summary tables for Figures 1 (heart rate only), 2, 3B to 3F, 5F and 7F, plus four CSV files that repeat the Fig 2 sheet exactly. There are no maps, traces or ECG, and no table says which animal a column is.
- **Metadata problems:**
  - The metadata declare 0 subjects and call the dataset a modelling dataset, but the workbook holds measurements from real hearts.
  - The deposited mouse APD80 at 60 s is 49.54 ± 4.94 ms; the Abstract reports 46.5 ± 9.1.
  - The Fig 3F no-SNS series has 4 hearts where the legend says 5.
  - In Fig 3E, every heart's no-SNS value at 5 s repeats its 0 s value.
  - The tyramine and noradrenaline tables label time "SNS Time" although those hearts were not stimulated, and each has an unlabelled column.
  - The Fig 1 heart rates have no unit.
- **Model code:** the MATLAB models for Figure 8 are in the dataset itself, not only on the lab pages.
- **Pinned version:** version 1 is the only one, and the paper cites none.
- **Assumptions:**
  - The first 20 s of the 60 s SNS series stands for the paper's 20 s SNS experiments (fig1bc, fig1ef).
  - In Fig 3F, the no-SNS and SNS columns are the same hearts in the same order. That outcome depends on it: unpaired tests find no difference.
- **Standard choices:** Holm-Sidak comparisons after the repeated measures ANOVA; I used the authors' own base and apex regions; and the Fig 3E record ends at 35 s, not 60 s.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Which test and which follow-up comparison give each "*p<0.05 vs. time 0"?
  - Is the Fig 3F pairing right, and why is one no-SNS column empty?
- **Questions to a reader:** none.

**3. Where the protocol was unclear**

1. **Substitute data.** The protocol does not say whether a claim may be tested on the same paper's data from a different experiment of the same protocol (Fig 2 standing in for Fig 1). I tested it, recorded a deviation and set `assumed: true`.
2. **Model code inside the dataset.** For `data: elsewhere` claims whose code is also in the dataset, the protocol gives no guidance. I blocked them as `not_runnable` and noted that the code is in the dataset.
3. **Summary-only datasets.** Step 2's clock check (do the data streams share one clock?) does not apply when the data are only tabulated values at fixed time points. I said so in the notebook.
4. **Absence claims.** The rule "absence is judged on the paper's test alone" conflicts with a claims file that names two tests and fails the claim if either finds an effect. I followed the claims file.
5. **Which archive files to read.** `docs/archives.md` does not say whether to skip the root `manifest.json` entry, which has no `s3VersionId`. I read only the versioned manifest key and refused files without a version id.

**4. Runtime and failures**

- About 20 minutes of work (12:40 to about 12:52 UTC by the clock); the notebook runs in 11 s.
- Nothing failed. The one stumble was that `tools/entry.py` must be run with the system `python3`, not the scratch environment.
- Untracked dotfiles and a `scripts/` folder were already in the checkout when I started. I left them alone.

Files are in `entries/wang-2019/`:
- reproduce_wang_2019.ipynb
- sns.py
- entry.yaml
- requirements.in
- requirements.lock.txt
- README.md

The record is `attempts/wang-2019-01.yaml`.
