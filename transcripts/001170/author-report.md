I've done steps 1 to 5 for dandiset 001170 and ran the step 6 handover. The entry passes `check` and runs from a clean environment, and the handover package is in `executed/001170-ling-2023/handover/`. Nothing is committed.

Paper: I used the open-access full text of bioRxiv v2 (2024-02-23), saved under `paper/`. Two tables in it are images I couldn't fetch. The preprint was later published in iScience (2026) as "Conserved post-odor dynamics in the olfactory systems of mice and locusts"; the claims are the preprint's, since that is what the dandiset names. Pinned version: 0.260528.1016, the latest published. The paper cites no version, and the other published version holds identical assets.

### 1. Outcome per claim

| Claim | Data | Outcome |
|---|---|---|
| mouse-sessions (7 sessions, 4 mice, median 215 ROIs) | dandiset | reproduced (7, 4, 210) |
| figshare-trace-link | with_inputs | reproduced (within-trial r 0.968, same ROI order) |
| fig2h-onoff-angle-mouse | dandiset | partially (mean 127.9 against 121.8 ± 2.98; all 28 above 90°) |
| fig2f-onoff-anticorrelated-mouse | dandiset | not reproduced (median r +0.48, 0 of 28 negative) |
| fig4b-reference-odor-mouse | dandiset | partially (holds for ace only; als goes the other way) |
| fig4d-clustering-mouse | dandiset | not reproduced (0 of 7 sessions) |
| fig6e-contrast-msc | dandiset | not reproduced (p = 0.39) |
| fig6e-contrast-ace | dandiset | blocked: data_missing |
| fig7d-persistent-anticorrelation | dandiset | not reproduced (r positive in every bin) |
| fig7h-iti-knn-mouse | dandiset | partially (45%, above the null but below 50%) |
| fig7j-iti-timebin-mouse | dandiset | reproduced (72 to 89%); a control undercuts the odor-memory reading |
| figs7e-ibi-chance | dandiset | blocked: methods_underspecified |
| figs8e-random-order-decline | dandiset | partially |
| figs2-pid-decay | dandiset | blocked: data_missing |
| fig1g-onoff-angle-locust | elsewhere | partially (104.9 against 106.7 ± 0.84) |
| figs4a-reference-odor-locust | elsewhere | reproduced (4 against 5 ± 1) |
| fig5e-contrast-locust | elsewhere | reproduced (p = 0.0055) |
| fig7f-iti-knn-locust | elsewhere | reproduced (100%) |
| fig7i-iti-timebin-locust | elsewhere | partially (29% against 40 ± 4) |

### 2. What was found about the dandiset
- **It holds the paper's mouse data.** The seven block-protocol sessions from four mice match the paper. The raw traces of the 198-ROI session match the array the paper deposited on Figshare.
- **The normalisation decides several outcomes.** The traces are raw F with no description of extraction or normalisation. The paper's deposited arrays are close to per-trial z-scores. With z-scoring, the ON/OFF anticorrelation, its persistence after offset and the contrast enhancement appear. With dF/F relative to the 2 s before the odor, they don't.
- **The ON/OFF angle above 90° comes from centring.** The code's centring over the ON+OFF window makes the mean ON and OFF vectors exactly opposite (cosine −1 in every case).
- **The time-bin classifier names the block, not only the odor.** The same classifier, run on stretches of the 15-min gaps between blocks where no odor is given, still names the preceding block at 70 to 97%.
- **The IBI method in the paper's Methods can't give its number.** k = 50 on 60 bins has its own null of 10.8%, not the 25% chance level. With k = 20 the gaps between blocks are classified at 73 to 95%.
- **Missing data:**
  - In three files the raw two-photon movie holds half the frames of the traces.
  - No odor pair ends in acetophenone.
  - There are no PID recordings.
  - The paper's random-order session is absent.
- **Metadata problems:**
  - The trials table is undocumented 1-s valve rows; "Empty" rows appear in some sessions only.
  - Concentration has no unit and is 0.0 for two odorants in three sessions.
  - Two odor names differ from the paper's.
  - Genotype and age are missing, and every session starts at 00:00.
  - The dandiset mixes in five random-order sessions, apparently from a second study, without saying which sessions belong to which paper.
- **The paper's code counts frames at 16 per second** while sessions run at 13.7 to 17.8 Hz.

### 3. Where the protocol was unclear, wrong or missing something
1. **Preprint later published under a new title.** Nothing says which version is the target. I used preprint v2, which the dandiset names.
2. **Code location.** The paper's code and data are in a Figshare record for the published version, which neither the preprint nor the dandiset links. I treated it as the code the paper links to, since the preprint promised a Figshare deposit.
3. **A standalone link claim.** The protocol frames link claims as serving dependent claims. I added one with no dependents to test whether the dandiset holds the paper's traces.
4. **Data from another species and lab.** The locust data were never expected in this mouse dandiset. The protocol requires testing "elsewhere" claims, so I tested five, and did not record their absence as a dandiset finding.
5. **Criterion against the chance-level rule.** For figs7e the criterion literally passes (3.8% ≤ 38.3%), but the procedure's null is far from the paper's chance. I applied the chance-level rule and blocked the claim.
6. **Deposited data as a source for method choices.** The protocol ranks Methods, then code, then other software; it doesn't cover arrays the paper deposited. Those imply z-scoring, so I kept dF/F as the main choice and show z-scored results as variants.
7. **Variants added after seeing results.** The z-scored and pseudo-trial variants were added after the main results. The protocol allows variants but says nothing about disclosing their timing; the claims file's opening comment covers only what I had seen before writing criteria.
8. **SEM as tolerance.** The rule to use the paper's own uncertainty gives very tight tolerances when that uncertainty is an SEM (± 2.98 and ± 0.84). I followed the rule.
9. **10% of a count of 5.** That tolerance can't apply to integers, so I used ± 1 and gave the reason.
10. **Clock check in a block design.** Shifted-label decoding isn't clean when consecutive trials share an odor. I used response latency, plus label decoding in the random-order sessions.
11. **Criterion passes but the reading fails.** For fig7j the criterion decides "reproduced", and the notes say the odor-memory reading isn't supported.

### 4. Runtime and failures
- The notebook runs in about 2.5 minutes; `tools/entry.py all` takes about 2.7 minutes.
- **Figshare** returned HTTP 500 to rapid downloads. The helper now retries; each file is checked against its md5.
- **bioRxiv** table images couldn't be fetched.
- **GitHub search** needed authentication, so I didn't use it.
- **Untracked device files** (`.bashrc`, `.gitconfig`, `scripts` and others) appear in the repo root. The sandbox created them; don't commit them.
