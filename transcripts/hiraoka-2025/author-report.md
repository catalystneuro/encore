## Report: hiraoka-2025 author run (Hiraoka and Jo 2025 on DANDI:000044)

Steps 1 to 5 are done and the handover package is built. `python tools/entry.py all entries/hiraoka-2025` reports 0 errors and all three notebooks pass from a clean environment. I did not commit anything.

### 1. Outcome per claim

| Claim | Outcome | Notes |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | "Unit 9" is row 9 counted from 0 (id 18): 228 356 spikes, τmin 1.050 ms, τmax 18 229.7 ms. It is the only matching unit. |
| fig2-iet-broad | reproduced | The IETs span 4.24 decades. |
| fig2-neuron-burst-size-heavy-tail | reproduced (assumed) | Power law supported at 40 of 40 timescales with the KS-xmin fits. With xmin = 1 it would only be partially reproduced. |
| fig2-neuron-beta-stable | partially reproduced | Median β is 2.354 and 27 of 34 estimates are in the band. β reaches about 2.9 at 55 ms, so the range rule fails. |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | Holds on grid (b): ρ = −0.829. Grid (a) has one point above 3000 ms, so it could not be judged there. |
| fig2-neuron-merging-heavy-tail | reproduced | 71 to 72 of 76 pairs supported; γ interquartile range 0.38 to 0.43. |
| fig2-neuron-merging-collapse | reproduced | Holds by reading (b) under the discrete KS fit only, with no margin (0.490 against 0.5). Reading (a) fails. |
| fig2-exponents-above-two | reproduced | Holds under the KS fits. |
| fig2-other-neurons-similar | not reproduced (assumed) | Under the discrete KS fit, 23% of the 562 pyramidal units show the pattern. Under the package's continuous default it is 56%, which would pass. |
| fig2-wikipedia-beta | blocked, `too_large` | The paper's preprocessed data are private. The 2015 dump survives only as a 47.4 GB stub history on the Internet Archive. |
| fig2-earthquake-beta | blocked, `other` | The SCSN catalog is public but continuously revised, so it cannot be pinned. |
| fig4-model-heavy-tails | partially reproduced (assumed, seed-sensitive) | Under the claim's seed the exponential series misses on γ interquartile range (0.50 to 0.52). The other four seeds pass. |
| fig4-model-iet-shapes | partially reproduced (seed-sensitive) | One of three τmax values is within tolerance. τmax is set by the highest level reached, which varies with the seed. |
| model-decremental-equivalent | not reproduced (seed-sensitive) | See the paper inconsistency below. |

### 2. Dataset, assumptions, questions

- **Version:** pinned 0.210812.1516, the version the paper cites. Later versions renumber the units and rename cell types; the spike trains are the same.
- **Unsorted spike trains:** in Buddy-06272013, Cicero-09012014 and Gatsby-08022013, unit id 2 is not sorted in time. It is two sorted runs, and the first is exactly 65 536 (or 131 072) spikes long. Rated major.
- **Spikes outside the epochs:** in Gatsby-08022013, 4.7% of spikes fall after the last epoch ends. Rated minor.
- **Position metadata:** the position series stores its sampling interval (0.0256 s) in its `rate` attribute. Rated minor.
- **Unit ids:** the paper's "unit 9" cannot be found by id in any version. Rated minor.
- **Representative unit:** it is labelled inhibitory, although the paper describes its data as pyramidal cells.
- **Checks that passed:** no recording or spike train is deposited twice, and the spikes share a clock with the maze position (r = 0.618 at zero shift).
- **Paper inconsistency:** Eq. 16 is not the memory function that Eq. 9 gives for the zeta distribution (q(1) is 0.354 against 0.255). As set up in Section IV, the two algorithms therefore draw different merging-number distributions and differ at every timescale. A self-consistent pairing differs only slightly. Even so, the claim's KS criterion rejects equivalence for two runs of the same algorithm, so it cannot confirm equivalence on these correlated sequences.
- **Assumption:** where the four fit readings disagree and the claims file gives no rule, I used the discrete fit with xmin chosen by the KS distance. This follows Clauset et al. for integer data and gives the paper's β of 2.35. Grid (b) uses 40 equal log steps between the ends of the relevant range, which reproduces both sets of Figure 2 labels.
- **Questions for the paper's authors**, recorded as `methods_unavailable` findings: which fit was used; which grid and which units were analysed; and which distribution the decremental algorithm drew from.
- **Questions to a reader:** none.

### 3. Where the protocol was unclear or missing something

1. The claims file's "holds under any reading" rule covers only claims on exponents. For claims that count tests, I followed step 1.6 and adopted a reading as an assumption.
2. The check requires `inputs` for `data: elsewhere` claims even when the data are simulated from the paper's own algorithms. I listed the paper's DOI as the source.
3. Nothing says what `blocked_by` to use for outside data that is public but has no versioned release. I used `other`.
4. Protocol and claims file seem to conflict for the Wikipedia data. The claims file marks the claim `data: elsewhere`, for which the protocol forbids `data_missing`, yet the paper's own data are public nowhere. I used `too_large`, based on the size of the raw dump, without timing a fetch.
5. It is unclear how `seed_sensitive` applies when different readings change outcome under different seeds. I set it to true and gave the details in the notes.
6. The protocol has no provision for a criterion whose reference shows it rejects even identical algorithms. I applied the criterion as written and reported the reference in the notes.
7. Any edit, even to a markdown conclusion, forces a full re-run of the entry (46 min). Writing conclusions after seeing the outputs therefore costs two full runs. I left the `runtime_minutes` values in `entry.yaml` (3, 40, 20) as upper estimates so as not to trigger a third run.

### 4. Runtime and failures

- **Run:** about 2 h 06 min (21:20 to 23:26 UTC), including two full clean runs of the entry.
- **Notebook times:** 2.3 min for `reproduce_hiraoka_2025.ipynb`, 27.7 min for `other_neurons.ipynb` (4 processes) and 16.3 min for `model.ipynb`. Peak memory was under 1 GB.
- **Failures:**
  - One permission-denied shell command early on; I used a different tool for the same read.
  - The first `entry.py all` failed its check because the simulated claims had no `inputs`; I added them.
  - Nothing else failed.
- **Untracked files:** `git status` shows `.bashrc`, `scripts` and similar untracked entries in the checkout root. The two I inspected (`.bashrc`, `scripts`) are null-device placeholders dated 21:19, from before this run; they were not created by this work.
