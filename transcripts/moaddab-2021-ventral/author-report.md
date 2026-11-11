All 45 claims were tested and none is blocked: 29 reproduced, 14 partially reproduced, 2 not reproduced. The entry check gives 0 errors, the notebook runs in 16 s from a clean environment, and the handover is built in `executed/crcns-bf-3-moaddab-2021/handover/`. Nothing is committed.

The data set includes the authors' own MATLAB scripts (`cubeScriptPR25.m`, `vpAnalysis.m`). The paper does not link them, and its own code link no longer resolves. I used them as the paper's code: where the Methods leave a detail open, the scripts settle it; where the two disagree, the Methods' version is the main result and the scripts' version is shown as a variant.

## 1. Outcomes

A1, A2 and A3 are the assumptions listed in section 2.

| Claim | Outcome |
|---|---|
| recorded-units | partially reproduced (435 neurons and 14 rats match; 195 sessions, not 194) |
| cue-responsive-screen | reproduced (271/160 with the Methods' rates; exactly 257/153 with the scripts' floored rates) |
| fig1f-suppression-cue-effect, fig1f-differential-suppression, ancova-inhibited-baseline-effect | reproduced |
| fig2-excited-inhibited-split, ancova-excited-no-baseline-effect | reproduced (A1) |
| kmeans-three-clusters, clusters-by-rat | reproduced (A1, A2) |
| clusters-differ-in-cue-firing | partially reproduced: Low vs Intermediate p = 0.035, the paper has p < 0.005 |
| fig3a, fig3c, fig4a (×3), fig4b, fig4d, fig4e (×2), fig4f, fig4h, fig4-low-int-combined, fig5a, fig5bc, fig5 Fisher comparisons, fig5g-i | reproduced (A1, A2) |
| fig3b (×2), fig3d (×2), fig4c, fig5d-f | partially reproduced (A1, A2) |
| supp5-low-cue-correlations, fig4g-int-early-late-betas | not reproduced (A1, A2) |
| supp6-low-nosepoke-pauses | reproduced (A1, A2, A3) |
| fig6a, fig6d, fig6ef | reproduced (A1) |
| supp9-excited-nosepoke-pauses | reproduced (A1, A3) |
| fig6b, supp8, fig6-excited-assignment-050, fig6c, fig6g, fig6-excited-peak-cue-vs-reward | partially reproduced (A1) |

Most partial outcomes have the same cause. The Methods normalize firing as trial averages minus a 10 s baseline. The scripts instead Z-score single trials after subtracting a 2 s baseline rounded down to a whole rate. The scripts' version reproduces the paper's printed numbers almost exactly (Low early/late betas -0.57, 0.05, 0.20, -0.51 against the paper's -0.57, 0.06, 0.20, -0.51). The Methods' version gives values about twice as large. Following the protocol, the Methods' version decides the outcome and the scripts' version is shown as a variant.

## 2. What was found about the data set

- **Recording was paused between trials.** Spikes, pokes and pellets exist only from 20 s before each cue to 31.5 s after it. The data descriptor does not say this.
- **Event channels undocumented.** The descriptor does not name the event channels or the cue channel of each behavior program; only the scripts do. I checked the mapping against the shocks and it holds.
- **Descriptor errors.** It says `poke.base` covers 2 s before the cue; it covers 20 s. The cube lacks the waveform fields the descriptor lists. Each unit has one waveform, not one per trial type.
- **Session count.** The files hold 195 sessions; the paper reports 194.
- **Possible duplicate units.** Four pairs of units recorded in the same session share 70 to 88% of their spikes, possibly one neuron counted twice.
- **The paper's clusters are a local optimum.** The scripts run k-means once after `rng(1)`. I repeated that run in Python and got exactly Low 74 / Intermediate 34 / High 18, with all five cluster F values matching the paper. With more restarts, k-means finds a better partition (58/46/22).
- **Scripts and Methods disagree** on the firing normalization, on rounding rates in the screen, and on the reward baseline window.

**Assumptions:**
- A1: the neuron groups are those the scripts produce; they match every count the paper reports.
- A2: the k-means clusters come from the scripts' single start with seed 1.
- A3: a nose-poke pause is a gap of more than 2 s between pokes, as the scripts define it.

**Questions for the authors** (recorded as `methods_unavailable` findings):
- Was the single k-means start intended, and do the cluster results hold on the better partition?
- Do the scripts' pause definition and the 5 s cue window match Supplementary Figs. 5, 6, 8 and 9?

**Questions for a reader:** none.

## 3. Where the protocol was unclear or missing something

1. Data-set scripts the paper does not link have no defined status. I treated them as the paper's code (Methods first, scripts as the variant or tiebreak) and said so in the notebook header.
2. The rule to follow the Methods for the main result left the main normalization unable to give the paper's numbers, which the scripts give exactly. I kept the Methods' version as decisive and recorded a `code_mismatch` finding.
3. The protocol gives no guidance on choosing analysis groups that the claims depend on. I used the scripts' groups (exactly the paper's 257/131/126/74/34/18) as assumptions A1 and A2, and showed the Methods-based groups as a variant.
4. The claims file called 100 k-means restarts a choice that cannot change the outcome; it does. I followed the Methods' default (one start) with the scripts' seed and recorded it as assumed.
5. The "count each recording once" rule does not fit units that only partly share spikes. I kept them, as the paper does, and recorded a finding.
6. The per-rat breakdown rule is hard to apply to around 45 claims. I added one by-rat table covering the main neuron-level measures.
7. A suggested clock check (shifting events into the inter-trial interval) cannot work here because those periods were not recorded. I used a danger vs safety contrast in time bins instead.
8. Run time: the start was given as 03:55, but `date -u` read 04:00 at the start.

## 4. Runtime and failures

Work ran from about 04:00 to 04:29 UTC. Nothing failed in the final run. During development two bugs were fixed before the final run: a pause table judged a different bootstrap draw than it printed, and the t-test handled the zero-variance case differently from Matlab.

Files are in `entries/crcns-bf-3-moaddab-2021/`; the attempt record is `attempts/crcns-bf-3-moaddab-2021-01.yaml`.
