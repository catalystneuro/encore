The file is fit for an attempt, and the last check now says `ready: true`.

**Checker result:** `claims/gao-2018.yaml: 46 claims, 46 quotes, 17 statistical values, 0 problems`. It gave the same line before and after my edits.

**Changes, by claim** (each is also recorded under `checks`):
- **fig1e-fastigial-lesion-slow-initiation:** the statement said contralesional first licks come later than ipsilesional ones. The paper only says lesions "slowed initiation of contralesional licking" and does not say compared with what. I restated it as the paper has it. The criterion now names two readings: contralesional licking after against before the lesion, and contralesional against ipsilesional licking after the lesion.
- **fig1h-fastigial-activation-response-contra-bias** and **fig1k-inhibition-response-ipsi-bias:** both criteria required the drop on the other trial type to be not significant, which the paper never states. A bias is now judged as the larger, significant drop on the trial type the paper names. The other drop's significance is reported but does not decide the outcome.
- **ed4g-fastigial-contra-late-delay:** the Extended Data Fig. 4g legend gives p=0.0001 without saying what is compared. The criterion now names both readings (the late delay fraction against one half, or against the first 500 ms). It also says the test for "equal numbers" in the early delay is the file's own choice. I added an `about` to the statistic.
- **fig1j-photoinhibition-silences-fastigial:** the criterion now says the majority rule is the file's choice, since the paper gives no count.
- **fig4g-dentate-effect-recovers:** the comparison with the fastigial fraction had no test. I named a one-sided test of two proportions as the file's choice.
- **Header E3:** it paraphrased the Methods as "qualitatively similar results". The Methods say "qualitatively similar preparatory activity", which says nothing about the response epoch. I quoted the Methods. This is the point raised in the unanswered question in `questions/gao-2018.yaml`.
- **Header, data:** it said all 1309 ALM units came from recordings with CN photo-activation. The Methods say only 9 of the 10 mice were. I removed that wording.

**Still open:**
- The legends of main Figs. 1 to 4 are not in the text, and there is no PDF of the main paper. So the paper's tests and counts for Fig. 1d, 1e, 1g, 1i, 2c, 3f and 4e to 4i are unknown, and the criteria use the hierarchical bootstrap or named choices instead.
- The photostimulus behind Fig. 1g (dentate) and Fig. 1h (delay bias) could be 0.455 s or 1.255 s. The Methods and Supplemental Table 1 disagree, so both readings stay.
- The bilateral ALM photo-inhibition trials in Extended Data Fig. 10a to 10c may come from earlier studies the supplement cites, not from this paper's recordings.
- The header says changes from the 2026-11-10 check were carried over, but the file had no `checks` list, so I could not see that check.
- Two minor legend findings have no claim: Extended Data Fig. 4d (lick modulation does not correlate with preparatory activity) and Extended Data Fig. 8c (glutamatergic fastigial synapses in ALM-projecting thalamus, one case).

Every claim comes from this paper. No ids were changed, and nothing was committed.
