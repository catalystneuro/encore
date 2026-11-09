I've finished steps 1 to 6: the entry is written, locked, checked and run from a clean environment (0 errors), the attempt record is written, and the handover is built. Of 26 claims, 2 are reproduced (one rests on an assumption), 7 partially reproduced, 3 not reproduced and 14 blocked.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-pure-sine-excites-all | partially reproduced (2 kHz excites 27 of 28 neurons, 20 kHz 15 of 17 = 88%, criterion asks 90%) |
| fig1-onset-delay | partially reproduced (latency falls with field in 38 of 38 pairs; median delay 64 ms, criterion asks 90 to 220) |
| fig1-max-rate-ceiling | reproduced, resting on an assumption (59.9 Hz under AP reading a; 42.9 Hz under reading b) |
| fig1-excitation-block | not reproduced (3 of 42 neuron-frequency pairs) |
| fig2d-20khz-twofold-threshold | partially reproduced (all p < 0.0001, but ratios 2.27 to 2.82 against 1.8 to 2.2) |
| fig2d-modulated-thresholds-higher | partially reproduced (1 of 3 pairs significant under reading a, 2 of 3 under b) |
| threshold-2khz-unmodulated | not reproduced (75.6 ± 6.2 V/cm against 57.7 ± 3.6) |
| fig2-modulated-locks-to-beats | partially reproduced (firing locks to the beats; one session ends depolarized) |
| fig2c-pure-more-aps | reproduced (46 of 52 pairs, p = 3e-09) |
| fig3c-sustained-firing-2s | partially reproduced |
| figs1-di8-anepps-control | not reproduced (only 3 of the paper's 8 neurons are deposited; no block under any reading) |
| figs2-ttx-blocks-depolarization | partially reproduced (APs gone in 6 of 6 neurons; only 1 had the sustained depolarization before) |
| fig3b, the four Figure 4 claims, the eight Figure 5/6/S3 claims, threshold-depolarization-estimate | blocked: metadata insufficient |

## 2. Dataset, assumptions, questions

**Dataset version.** Pinned 001274 at 0.250805.1401, the latest published version; the paper cites none, and the earlier version has the same assets. The other dandisets are also pinned at their latest versions and listed under `inputs`.

**What 001274 and 001273 hold.** Raw strobe image stacks only: no ROIs, no field in V/cm, no frame times, no cell shape groups, and nothing linking subjects to the paper's cells C1 to C9. That blocks all Figure 4, 5, 6 and S3 claims. As the claims file asks, I show ROIs rebuilt from the paper's RATIO image as a variant only:
- pulse: 20.6 ± 2.7 %/kV/cm (paper 28 ± 2.5);
- sine: about 5.5 %/kV/cm, 26% of the pulse value (paper 42%).

**Other findings about the dandisets:**
- 001034 is a second deposit of 001032: identical arrays and start times in the 10 pairs compared.
- No 250-ms session is labelled as sodium gluconate, which is why Figure 3B is blocked.
- The tetrodotoxin sessions are described as "caused sustained depolarization". The paper says tetrodotoxin blocked it, and in the data no tetrodotoxin session shows any.
- The voltage calibration factors are "to be reported separately" and are not in the dandisets.
- The images are 16×16 pixels; the paper gives 64×64.
- The first frame of every fast recording is a camera artifact.
- The electrode gap in the descriptions is 140 µm; the paper gives 120 µm.
- 001030 makes one subject per session (17 subjects for 4 neurons).
- 001272 holds 3 neurons; the paper used 8.
- Many 001274 strobe sessions are labelled tetrodotoxin, which the paper does not mention for these figures.

**Assumptions**, each recorded as a question for the paper's authors:
- **Soma ROI:** the whole frame. Its first APs have a median of 11.4% dF against the Methods' typical 11.3%. The brighter half of the frame, run as a variant, changes no outcome.
- **Field:** 36 V/cm times half the peak-to-peak voltage. The full voltage was also run; it changes no outcome.
- **AP reading for the firing-rate ceiling:** reading (a), a peak above 5%, which is how the Methods word it.

**Questions to a reader:** none.

## 3. Protocol gaps

1. **Most claims use other archives' data.** 13 of 26 claims are `data: elsewhere`, on six other dandisets, and the protocol assumes one dataset per entry. I put every dandiset under `related` and `inputs`, and the record names 001274.
2. **Repeated readings.** Step 1.6 has every reading run, and many criteria add their own, so the AP readings, ROIs and field conversions multiply into grids. I chose one adopted reading, showed the others as variants, and recorded an assumption only where the readings changed an outcome.
3. **Readings that disagree on a part that doesn't decide the outcome.** In the Di-8-ANEPPS claim the criterion says to block when readings disagree. They disagree on excitation, but the claim fails the block test under every reading. I recorded it as not reproduced and said why.
4. **Clock check.** "Every data stream shares the clock of the trial tables" doesn't fit image files with no stimulus channel. I used two substitutes: no APs before the stimulus under reading (a), and AP locking to the 20-Hz beats, which drops from 0.90 to 0.10 when the beats are shifted by 25 ms.
5. **No fit for duplicate deposits.** A duplicate across dandisets (001034 of 001032) has no finding kind of its own; I recorded it as `other`.

## 4. Runtime and failures

- The notebook runs in 20.4 minutes from a clean environment. It streams about 1,000 small files plus about 7 GB of strobe stacks.
- The whole session took about 1.5 hours (15:16 to 16:44 UTC).
- An early AP detector counted the shoulder of one AP twice, and noise peaks on the aliased 2-kHz carrier at high fields as APs. I fixed this by merging peaks closer than the paper's 8-ms AP duration.
- A per-cycle reading of the sine regression (reading b in the claims file) was swamped by single-frame noise. I dropped it and say so in the notebook.
- Nothing else failed. Nothing is committed.
