**Verifier report: Li et al. 2016 (doi:10.1038/nature17643) on DANDI:000011 v0.220126.1907, round 2**

The claims file has 38 claims and the attempt record has 38 outcomes, in the same order. The outcomes are 6 reproduced, 5 partially reproduced, 9 not reproduced, and 18 blocked: 10 data_missing, 4 methods_underspecified and 4 metadata_insufficient. Cell indices refer to the re-executed `reproduce_li_2016.ipynb`.

### 1. Stated outcomes

I agree with all 38 stated outcomes.

- **Changed since round 1, all agreed:**
  - **selective-fraction (not reproduced):** under K1 only 1 of the 4 counts is within tolerance (cell 27), and the criterion has no partial clause.
  - **ed2b (not reproduced):** the VGAT ipsilateral value fails under every reading (cell 44).
  - **cd-stable (blocked, methods_underspecified):** w from all correct control trials gives 0.563/0.588, inside the band; w from the training subset gives 0.534–0.554, outside (cell 63).
- **ed7e and ed8 (partially reproduced):** I said not_reproduced in round 1. The Summary now states one rule for criteria without a partial clause: partial when at least half the parts hold under every reading that must agree. The author applies it to all five such claims. In round 1 I accepted partial for unit-classification, fig2-recordings and fig6, so for consistency I accept it here too: 3 of 4 hold under K1 and 2 of 4 under K2 (cells 69, 93).
  - **Caveat:** the author wrote this rule after round 1, and it is not in the claims file. Read strictly, those five claims would be not_reproduced. The claims file should adopt the rule or reject it.
- **The rest are agreed as before.** This includes ed9f as data_missing: the experiment-2 lick trace rises a median of 0.0013–0.0022, the same as on no-response trials (cell 86).

### 2. Sentences the printed numbers do not support

- **Cell 97 and the attempt-record notes for ed7:** "With end labels the ipsilateral time is 750 ms or more, outside tolerance."
  - The tolerance band is 490 ± 280, i.e. 210–770 ms, so 750 ms is inside it.
  - Cell 96 shows `ipsi_ok` in 8 of 16 readings for drop/bin/end and for drop/delay/end. The end-label combinations fail on the other parts.
  - The outcome does not change.
- **Cell 94:** "bilateral separation is not lower than ipsilateral here." Under K1 with H2 it is lower: 0.616 against 0.672 (cell 93). The outcome does not change.
- **Cell 14:** "the event is logged up to about 2 s after the light". Cell 13 prints a maximum of 1587 ms, about 1.6 s.
- **Cell 79 and the record (fig3e):** "differences within 2 s.e.m. under every reading". This is true for T1 only. Under the T2 variant (drop, H1, g1) the ipsilateral difference is −0.353 against a 2 s.e.m. of 0.294 (cell 78).
- **Cell 76:** gives the lick-left rho as "−0.76 to −0.99", but several rows print −1.000 (cell 75). This is trivial.

Every other sentence I checked against the outputs is supported. That covers the Result paragraphs, the Summary (including the K2 displaced fractions of 3–16%, 6.5–7.5% and 1–4%, and 339 of 931 trials), the README and the record's notes and findings. Examples: the fig1f counts and fractions, the 24-combination tallies for fig1g and fig2e, the ed2e counts, the fig2 ranges, the cd-captures values, the fig3d/3e |ROC − 0.5| values, the ed9f 5 of 26 and 18 of 26, the ed10 counts 331–340 and 81–84, and the behaviour proxies (paired p 0.21/0.16, 0.059, 0.045).

**Round-1 reasons in the attempt record:** all 38 restate my round-1 reasons faithfully in my own terms, including the points from section B that the author folded into them. The `agrees` flags (false for selective-fraction, ed2b, ed7e and ed8) correctly reflect round 1.

### 3. Round-1 points: what is resolved and what remains

**Resolved**
- **B1 (44 units, selective-fraction):** the author's answer holds. Those units have no identifiable control trials, and the variant includes their photoinhibition trials. The variant also fails under K2 (sample count 157), so it would not reproduce either.
- **B2 (fig1f):** now disclosed in the conclusion and the notes. The outcome is reproduced on the reading without exclusion (248 neurons); the reading closest to the paper's counts fails. The criterion allows either.
- **B5 (cd-stable):** now blocked.
- **B7 (E1 with end labels):** I withdraw this point. A bin ending at the go cue is labelled 300 ms after offset, so E1 can return a time inside the tolerance. The NaN values are empirical, not by construction (cell 42).
- **B8:** per-session mode ROCs are printed, and the binomial test decides.
- **B9:** levels above the baseline (0.16, 0.20, 0.25) were added.
- **B10:** partial outcomes now follow a stated rule.
- **Section C requests:** all met (upsampled widths, lick traces, included-neuron tables, size of the K2 artefact, experiment-3 behaviour, mode ROCs).

**Remaining, and bearing on a conclusion**
1. **Partial rule.** The partial outcomes of unit-classification, fig2-recordings, ed7e, ed8 and fig6 rest on a rule the claims file does not contain.
2. **K2 definition (B4, a claims-file issue).** Cell 15 now measures the artefact: in 1–16% of each condition's trials the light falls before its logged time. Because K2 uses events at their logged times, those trials enter the photoinhibition averages without light. This contributes to the K1/K2 disagreements behind the fig1g and ed7 blocks and to the K2 failure in ed2b. ed2b also fails under K1, so its outcome does not depend on this. A question to the reader is pending.
3. **Population sizes (B3).** The included populations are still 2–3 times the paper's: 138–173 neurons against 55, 260–293 against 143, 58–62 against 40, and 24 sessions against 16. No further selection tried reproduces the paper's counts (cell 41). This affects ed4, fig1g, fig2e, ed7 and every claim built on the activity space. It is correctly recorded as selection_undocumented.
4. **cd-captures (B6).** The captured fractions are in-sample. This is disclosed but not tested, since the claims file names no held-out reading; the claim is blocked either way.
5. **Data loading.** I still cannot verify how events and photostimulus records are assigned to trials without re-running. As in round 1, I rely on the clock checks (cells 19–20).
