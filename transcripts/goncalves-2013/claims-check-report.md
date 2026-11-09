I made seven corrections to the claims file and recorded them under `checks`. The file is ready for an attempt (`ready: true`).

**Checker:** `claims/crcns-ssc-8/10.1038-nn.3415.yaml: 28 claims, 28 quotes, 35 statistical values, 0 problems`. It gave the same line before and after my edits.

**Changes, by claim:**
- **Header (correlation measure):** One of the two allowed readings was Spearman rank correlation, which the paper never suggests. The Methods only say "continuous-trace cross-correlations", so I made Spearman a variant that cannot decide a claim. I also noted that zero lag is a choice, because the paper gives no lag window.
- **fig1d-distance-dependent-decorrelation:** The Bonferroni correction over three distance bins is now marked as a reading. It comes from the three corrected p-values the paper prints; the paper does not say how many comparisons were corrected for.
- **wholecell-state-modulation:** The statement said neither genotype changes firing significantly between brain states. The paper only tests WT (p = 0.41). For Fmr1 -/- it reports a "tendency" with no values and no test. The statement and criterion now judge WT on the paper's test and Fmr1 -/- on the direction only.
- **ap-kinetics-similar:** The made-up readings included amplitude and threshold, which are not kinetics. The readings are now spike half-width, or rise and decay times. The measures are marked open, since Suppl. Fig. 2 was not supplied.
- **fig4-updown-properties-similar:** The paper prints the number of cells only for Up state duration. The file now says the same n is assumed for frequency and Up-Down step.
- **fig5c-firing-vs-lh-p14-16** (this also applies to p30-40-firing-vs-lh and fast-imaging-control): The Fmr1 -/- slope must now be positive, since the Results say firing rises with the EEG low/high power ratio.
- **fig5ef-slow-wave-epochs:** The correlation now uses cell pairs within 100 µm, as for Fig. 5d in the same paragraph, with the shared readings. The Pearson version (Suppl. Fig. 3) is a variant.

All other claims match the Results and Online Methods. Each of the three main findings listed in the Discussion has claims (synchrony; firing during Up/Down states and Up-state firing probability; the effect of anesthesia), and every claim comes from this paper.

**Still open:**
- No figure legends or supplement were supplied. Several details therefore stay open, with readings named in the file:
  - how Fig. 1d was binned;
  - the exact correlation measure, which the paper takes from its reference 15;
  - what counts as an "active" cell for peaks of synchrony;
  - how the traces are shuffled.
- The paper's control using the delta/theta EEG power ratio has no claim. It is described only as "similar results (not shown)", with no frequency bands or numbers to test.
