The claims file for DANDI:000249 is fit for an attempt. I marked the new `checks` entry `ready: true` after making 20 corrections. Nothing is committed, and the only file changed is under `claims/000249/`.

**Checker result:** `claims/000249/10.1038-s41586-020-2807-6.yaml: 44 claims, 44 quotes, 90 statistical values, 0 problems`. It passed before my edits and passes again after them.

**Changes, by claim:**
- **Header:** readings (ii), (iii), (v) and (vi) of the imaging method are method details. A claim's outcome is now the one every reading gives, and it is blocked when they disagree, as the protocol requires.
- **fig1c-warm-vs-cold, fig1c-salient-isis-retrieved, fig1c-slow-and-single-not-retrieved:** the Methods don't say which comparisons form the FDR family; the file had guessed one. The criteria now name two readings: every condition against warm, or the three comparisons the legend reports.
- **Six claims changed from "under one reading" to "under every reading", blocked when they disagree:** fig1f-ev-broader-than-nv, ed6c-tuning-width-groups, fig1g-ipsc-depress-faster, ed6ef-epsc-tuning, ed3m-tones-broader-than-calls-naive and fig4b-ch575-broader-at-575. The open choices there (ANOVA design, Bonferroni family, number of trials, normalization) are method details, not readings of a reported number.
- **ed3m-tones-broader-than-calls-naive:** I rewrote the samples: 5 tone mice against the naive excitatory mice of Fig. 1f. The paper says 5 tone mice here but 4 naive mice in Extended Data Fig. 3k, and doesn't explain the difference.
- **ed3k-tones-no-experience-effect:** the legend gives both mice and neurons without saying which the t-test used. Both are now readings; the file had picked neurons.
- **ed4c-left-broader-than-right:** the legend fixes the unit as mice, so single cells are now only a variant.
- **ed4d-response-tracks-isi-probability:** the legend's "evoked ΔF/Fs" is the paper's term for raw responses. Raw dF/F is now the measure and normalized dF/F a variant.
- **ed4e-dam-broad-tuning:** I added "similar to experienced virgins" from the main text, and said the criterion's bounds are my reading of "similar" and "broad", not the paper's.
- **ed4g-broadening-with-reliable-retrieval:** added the per-session counts that add up to 78 and 52 neurons.
- **fig1g-ipsc-depress-faster:** removed the statistics entry (p < 0.05). The text prints no p for this panel. The test and cell counts are now in the criterion.
- **ed5b-press-count-unchanged:** now uses all the press and session-comparison readings of fig1i-operant-prototypes; it had used only session 1 against session 8.
- **fig2f-nv-mismatched-ei-tuning:** the p < 0.05 entry is not in the text, and "two or more ISIs" and the slope test over single curves were made up. I replaced them with the Extended Data Fig. 6c,d tests the sentence cites (p=0.04 and p=0.29).
- **ed6ef-epsc-tuning:** added that dams and experienced virgins are pooled. Also noted that the Methods list morphs of 125, 225 and 575 ms while the legends use 125, 175, 275 and 575 ms.
- **fig3e-exc-broadens-after-onset:** the cell counts rule out the pooled reading, so I removed it. The statement's claim that excitatory and inhibitory tuning become matched is now tested, from the Fig. 3e legend.
- **fig3h-slopes-sharpen:** the single-cell slopes of Fig. 3i had no claim; they are now reported.
- **fig4c-ch575-retrieve-slow:** the controls are the experienced virgins of Fig. 1c, as the Methods say.
- **fig4d-actx-inhibition-blocks:** the statement says latencies are unaffected, but nothing tested that. The latency test is now in the criterion.
- **fig4e-ot-inhibition-deficits:** the text doesn't say latencies got longer (it gives only p=0.0003). The statement now says latencies change, and the direction is reported.

**Still open:**
- **fig1a-isi-distribution:** the 1% bound used for "essentially never" is not from the paper, and the text offers no number to replace it.
- **ed6d-slopes-negative-in-ev:** the paper doesn't say which mice make up its counts of 7 and 11, against 9 and 12 in Fig. 1f.
- **fig2e-ev-matched-ei-tuning:** the ANOVA design is not given.
- **fig4g-ot-inhibition-narrow-tuning:** the paper doesn't list which mice form the control groups of 14 and 10.
- **ed3bc-neuropil-no-effect:** the two corrected regions are not identified.
- **Figshare data:** the paper's own figshare DOI does not resolve. The outside data come from the collection the dandiset links to, and someone should confirm it is the paper's.

**Ready:** yes.
