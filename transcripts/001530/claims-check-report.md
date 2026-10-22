I checked the claims file for 001530 against the paper and it is ready for an attempt. I corrected nine claims, added one, and recorded six problems I could not settle.

**Checker result:** `claims/001530/10.1038-s41467-026-73622-y.yaml: 29 claims, 29 quotes, 52 statistical values, 0 problems` (before my edits it reported 28 claims and 0 problems). All quotes match word for word, and all p-values match the paper's numbers.

**Changes, by claim**
- **Quiet-trial rule (file header):** the paper's Methods and its code use different deviation measures, and the file had no rule for which one decides the outcome. The Methods version now decides it and the code's is shown as a variant, as the protocol requires.
- **fig4-29-clusters:** the code's clustering (100 ms bins, a different similarity formula) was the main reading. I swapped it so the Methods' version (10 ms bins, Gaussian similarity, 17 PCs) decides, with the code's number of clusters still reported.
- **fig3d-wm2-infragranular-delay:** it used the code's quiet rule (whisker only) as main. It now uses the Methods' rule (jaw and whisker).
- **fig5b-context-decoding-delay, and the four claims that decode the same way (fig5b time course, fig5c, fig5d, fig7d):** the code's SVM was main, and the Methods' parameter search used a grid the first reader made up. The paper gives no grid, so both versions are now run; the outcome is what both give, and the claim is blocked as `methods_underspecified` if they differ.
- **fig3b-delay-and-response-psth:** the 1.0 to 1.5 s window after the whisker stimulus was made up. It is now the paper's own licking window (1.3 to 1.5 s), with the old window as a variant.
- **fig4b-named-clusters:** "mostly" was read two different ways for different clusters. Both readings now apply to every cluster, and the outcome is what both give.
- **fig5a-single-neuron-context:**
  - The statement had wM2 ahead of ALM overall, but the paper ranks wM2 first only for neurons excited by the Go-tone. The statement now says that.
  - The criterion now also requires wM2 and ALM to have more modulated neurons than the other three areas.
  - The two 3 Hz tolerances go from 0.3 to 0.5 Hz, because the paper prints whole numbers.
- **fig5b-decoding-time-course:** the time windows and the chance band were made up. The early window now has two readings (the paper's 0 to 0.03 s Auditory window and 0 to 0.2 s), and chance uses the 10% default. The check now covers every neuron count, including 5.
- **quiet-trials-half:** whether "recorded trials" means completed trials or all trials is now named as open.
- **fig6c-temporal-correlation:** the brief cue response in A1, wS1 and wS2 had no rule. The criterion now says it is shown and not judged.
- **New claim, fig3a-activity-maps:** the Fig. 3a findings had no claim. The paper does not give the length of the baseline before the whisker stimulus, so two readings are named.

**Still open (recorded under `checks`)**
- I could not see the paper's code, so the first reader's code citations are unverified. That includes whether the Fig. 3a script fixes the baselines for the new claim.
- Three claims rest on measures the first reader chose because the paper gives none:
  - fig6a-pca-delay-states: the distances and half-maximum rule.
  - fig2-other-trial-types: the thresholds for "little impact".
  - figs18-later-lick-coding: the effect-size readings.
- Paragraph numbers in sources could not be checked, because the paper text has no paragraph breaks.
- The Supplementary Information was not supplied. Claims resting on Supplementary Figs. 3, 17 and 18 use the main-text sentence and the code.

Nothing was committed or pushed.
