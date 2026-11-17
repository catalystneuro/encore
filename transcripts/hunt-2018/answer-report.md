I answered both questions, and both claims changed. Only `claims/hunt-2018.yaml` and `questions/hunt-2018.yaml` were edited, and nothing is committed.

The paper's MATLAB scripts are among the dataset's files, so I could not read them. Where an answer relies on a script, it relies on the question's description of it, and each answer says so.

1. **figs1cd-fewer-cues-more-accurate: changed.** The criterion now accepts two accuracy measures: the choice of the higher true expected value, or the choice of the higher expected value of the pictures seen (as in choice-accuracy-observed). The claim holds under either. The paper's text supports both:
   - The Supplementary Figure 1 legend says subjects "were more likely to choose optimally".
   - The Results sentence "choice accuracy was also higher..." comes right after the sentence on accuracy "based upon the pictures observed".

   Trials are still pooled over sessions, because the legend gives n as a count of trials. The per-session average the question reports from the script is listed as a variant.

2. **fig7a-ofc-value-difference-neurons: changed.** The paper says only that the tests must "be significant", with no level given, and the Figure 7 legend is missing from the text. Requiring OFC to come out largest at both p < 0.05 and p < 0.01 asked for more than that. The claim now holds at any one significance level, the same rule used for the other open details. The script's threshold of |T| > 1.64, as reported in the question, is added as a third reading.

**Quote check:** `python tools/claims_check.py` passes every quote. It exits with two "VALUE NOT FOUND" warnings, both for the p < 1e-7 value in the two Figure 8 claims. Those come from the text extraction dropping the minus sign, which the claims file already records, and are not from these edits.

**Not changed:** fig7c-acc-belief-neurons also requires both significance levels. No question was asked about it, so I left it as it is.
