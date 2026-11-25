I checked `claims/longcore-2024.yaml` against the paper and corrected six things. It is ready for an attempt, though three questions remain open. Nothing is committed.

**Checker result** (the same before and after my edits): `claims/longcore-2024.yaml: 13 claims, 13 quotes, 18 statistical values, 1 problems`. The one flag is `VALUE NOT FOUND sex-predicted-suppression -2.1`. That value is correct: the paper says "2.1% increase", and the file records it as a suppression of -2.1.

**Changes**
- **Opening comment (the model):** the Methods say the GLM uses a log link. But the Results give model predictions that are negative (males +9.3% activity at 0.01 lx and 1750 K), with 95% CIs centred on the estimate. A log link can't produce either; an identity link can. I added the identity link as a second reading. It is now named in the criteria of `glm-illuminance-cct-interaction`, `sex-predicted-suppression` and `individual-variation`.
- **tukey-illuminance-within-cct:**
  - I removed the statistics entry "p < 0.05". The paper reports no p-value for these comparisons, so 0.05 is a significance cut-off, not a result.
  - I narrowed the statement to comparisons within color temperatures, which is all the quote says.
  - Alpha 0.05 is now labelled a standard choice.
- **cct-0p01-not-significant:** alpha 0.05 is now labelled a standard choice, because the paper gives no alpha for the activity tests.
- **cct-effect-grows-with-intensity:** the measure used (the spread of the three CCT means at each illuminance) is not from the paper. I said so, and added the CCT effect predicted by the GLM as a variant.
- **cfos-no-cct-difference:** the tolerances on the two means were 10%. I changed them to the paper's own s.d. (17.89 and 8.22), since the protocol puts a stated spread ahead of the 10% default.

**Open**
- **Table 1 is missing.** The extracted text has its title but none of its numbers, and there is no PDF. So the four claims that rest on per-treatment means have no expected values. The abstract gives four of the numbers, but claims can't be written from the abstract; someone with the table should add them.
- **The Tukey sentence is ambiguous.** It doesn't say which pairs differ or what "significantly greater" is measured against. I kept both readings in the criterion; the wording "Within color temperatures" favours the first.
- **"Several times" is read as a ratio of at least 2.** The main text gives no number for the illuminance-to-CCT effect ratio; only the abstract does (3.6).

**Ready:** yes (`ready: true`). Every main finding has a claim, and all the claims come from this paper. The missing Table 1 values limit the four claims that rest on it to the direction of the means.
