I wrote `claims/gillespie-2024.yaml` and did not commit it. The quote checker passes on every quote. It still lists 6 "problems": p-values the paper prints with trailing zeros (for example "6.790 × 10 –7"). I found each one in the text by reading.

**What I read**
- The version of record (eLife RP90944, PMC11221834), in `paper/10.7554-elife.90944.txt`. It holds the main text, Methods, and all figure and figure-supplement legends inline. I did not open the PDF.
- The paper's code: github.com/LorenFrankLab/Gillespie_eLife_2024 at commit ad5801a, the revision the paper cites. Its README map is out of date for Figure 2–figure supplement 1F–H, which I noted in the file.

**Counts**
- 35 claims: 33 findings and 2 `link` checks on the control cohort's trial and epoch counts.
- 34 have quotes. The other one (the control cohort's replay GLM, Fig 4G) is marked `inferred`.
- 27 claims carry statistics (112 values in all), 7 have expected values, and all 35 have criteria.

**Which data the claims need**
- DANDI 000115 holds only the control cohort (jaq, roquefort, despereaux, montague).
- The neurofeedback cohort is in DANDI 000629, which is not this record's dataset. So 26 claims are `data: elsewhere`, with `where:` naming 000629, plus 000115 for the cohort comparisons.
- 9 claims can be tested on 000115 alone:
  - control trial, epoch and SWR counts
  - control SWR rate rising after reward (Fig 2B, Fig 2–S1F)
  - control post-reward dwell time increasing over epochs (Fig 2–S1H)
  - control head speed below 4 cm/s (Fig 3A)
  - control replay GLM (Fig 4G)
  - control search efficiency increasing over epochs (Fig 5–S1)

**Details the paper leaves open, and the readings I named**
- **Control epoch flags** (ripthresh, environment, forageassist, gooddecode): the code fixes them. If the dandiset lacks the flags, the readings are (a) all full-task run epochs, or (b) those minus forage-assist and no-delay epochs.
- **SWR detection baseline**: the mean and sd are taken over (a) the whole epoch or (b) immobile times. The detector itself is not in the repository.
- **Head speed**: (i) the speed the dandiset provides or (ii) speed recomputed from the LED position with standard smoothing; and the per-rat value as (a) the median or (b) the mean over trials.
- **Replay class**: the Methods' "continuous model probability > 0.8" against the code's `max_state == 1`.
- **Trial-wise pre/post SWR-count correlation**: (a) all trials pooled, (b) NF trials pooled, or (c) the median of per-epoch r. The code computes it per epoch; the text gives one r per rat.
- **"No extended suppression"** (Fig 2–S1G): two thresholds named.
- **"Approximately twice" / "half as long"**: the code's inset ratios, with ratio-of-means variants.

**Thresholds I chose because the paper gives none**
- Tolerance 0.3 on "approximately twice" (pre-reward SWR rate), 0.5 on "roughly twice" (per-size fold change), 0.1 on "half as long" (dwell time).
- A 5 s post-reward window for comparing the two cohorts' time courses.
- A 10% median difference for "approximately matched" pre-reward dwell time.

**Missing**
- Nothing the claims need is missing from the paper.
- The SWR detector, position processing, `label_trial_interval.m` and the decoder are not in the paper's repository. The criteria point to Gillespie et al. 2021 for the task-phase labels.
- The trigger delays disagree: the Methods and code give 75/100/50/50 ms, the Figure 1–figure supplement 1B legend 100/50/75/75 ms. I recorded this in the header; no claim rests on it.
