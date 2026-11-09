I tested 18 of the 42 claims: 9 reproduced, 7 partially reproduced and 2 not reproduced. The other 24 are blocked because their data are not in the dandiset. The entry runs cleanly in a fresh environment (`entry.py all`: 0 errors, about 12 min), and the verifier's handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig4d-latency-trough | reproduced (median trough 1.95 ms) |
| figs3cd-gmm-window | reproduced (windows 0.683, 1.139, 1.221, 1.470 ms) |
| fig4h-extent-constant | reproduced (p = 0.317) |
| fig4h-distance-decreases | partially reproduced (tests hold; 25 µA mean 264 µm against 300) |
| fig4h-ks-distinct | not reproduced (5 vs 100 µA adjusted p = 0.11 with the dataset's coordinates) |
| fig4j-drp-increases | reproduced (99 units, F = 12.78) |
| figs3e-early-windows | partially reproduced (effect holds, proportions lower) |
| fig5bc-amplitude-clusters | reproduced (CCC 0.702, silhouette 0.352) |
| fig5ef-polarity-clusters | partially reproduced (bipolar 0.205 against 0.277) |
| fig5-fsrs-proportion | partially reproduced, rests on an assumption |
| fig5j-fs-closer | reproduced, rests on an assumption |
| figs6b-fsrs-early-firing | reproduced, rests on an assumption |
| fig6c-modulation-cortex | partially reproduced (exact under the code's window; no region effect under the Methods' 500–1000 ms window) |
| fig6d-hva-subcortical | not reproduced with the legend's groups (13.91 vs 13.48, p = 0.90) |
| fig6e-circuit-responders | partially reproduced (two values just outside 10%) |
| fig6f-no-propagating-wave | reproduced |
| figs9-state-drp | partially reproduced (direction and tests hold, values about ¼ of the paper's) |
| fig6g-dimensionality-collapse | reproduced |
| 11 evoked-potential claims, 3 claims needing the evoked-potential boundaries, 10 behaviour claims | blocked, `data_missing` |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.260520.1753: the paper cites it and it is the only published version.

**What the dandiset holds.** Ten files; the paper uses nine of them. The tenth, jlh41, has no CCF coordinates and the paper leaves it out.
- Raw AP band, LFP and behaviour are not deposited, which accounts for all 24 blocked claims.
- jlh49v1 is filed under subject jlh48.
- The electrodes table holds placeholder values, so channel coordinates had to be fitted from the units' own coordinates.
- Cathodal pulses are in only 7 of the 9 recordings, though the paper's legends say 9.
- jlh33 has 60 trials per condition, where the Methods say 75.
- There are no waveform-class labels or stability flags; I recomputed both, and my unit counts per condition match the paper code's intermediate table exactly.

**The finding that matters most.** The stimulation-contact coordinates of jlh31 and jlh32 differ from those in the paper's code by 206 and 373 µm. With the code's coordinates every distance result matches the paper exactly, including the KS test. With the dataset's coordinates, fig4h-ks-distinct is not reproduced.

**Code mismatches found.**
- The code's higher-visual-area group for Figure 6D includes 151 superior colliculus and dentate gyrus units.
- Its region mapping drops posteromedial (PM) units because of a name mismatch.

**Assumption.** For the three FS/RS claims I used the classes the paper's code actually computes (a 0.4 ms duration threshold), where the Methods describe k-means. The code's classes give the paper's statistics exactly; the k-means reading is shown alongside.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Were FS and RS assigned by k-means or by the duration threshold?
- Which modulation-index window is meant: the Methods' 500–1000 ms, the legend's, or the code's 0–500 ms?

**Questions to a reader:** none.

## 3. Protocol issues

1. The claims file calls the code's saved evoked-potential boundaries "an outside input for the author to judge", but the protocol says a claim that depends on a blocked claim is blocked. I blocked the three dependent claims and did not use results derived from missing data.
2. The protocol does not say what to do when an outside check (the code's coordinates) flips an outcome. I judged on the dataset, gave the code-coordinate result in the notes, and recorded a `code_mismatch` finding.
3. Reader step 2 (follow the Methods, code as a variant) conflicts with author step 1.6 (adopt the best-supported choice as an assumption) for the FS/RS classes. I followed 1.6 and marked those outcomes `assumed`.
4. The fig6c criterion requires every reading to pass, against the protocol's rule that any matching reading is enough. I followed the criterion, so the outcome is partial.
5. Nothing covers paper software that needs a patch to run on the locked Python 3.13. zetapy 2.7.2's `getZeta` (what the code calls; it matches the paper's cached p-values, r = 0.99) needed a one-line scipy shim, which I applied and noted.
6. Nothing covers running only part of a test for time without blocking it. Running ZETA on all polarities would push the notebook past 30 min, so I ran the cathodal conditions only and showed the full polarity model from the paper's cached p-values as a check.
7. The tool's provenance field name and the prompt's harness string differ slightly. I recorded the harness as "Claude Code".

## 4. Runtime and failures

The work took about 1 h 47 min (17:03 to 18:50 UTC). The notebook takes about 12 min, 9 of them the ZETA tests on four cores. Nothing failed in the final runs. An earlier version used zetatest from zetapy 4.1, which gave lower responder proportions; I replaced it with `getZeta` from zetapy 2.7.2.

Files are in the repo root:
- attempts/000774-hickman-2026-01.yaml
- entries/000774-hickman-2026/ (notebook, `estim.py`, README.md, entry.yaml, requirements files)
