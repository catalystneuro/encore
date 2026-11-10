There was one question, on `fig1c-head-direction-cells`. I changed the claims file to answer it.

**Question:** the freely moving claims that rest on head pitch and roll are marked `data: dataset`, but the dandiset holds no pitch or roll, and the paper put those data on figshare. Should they be `data: elsewhere`?

**Answer: yes.** The paper's Data availability statement points all its data to figshare. I checked the deposit descriptions, though not their contents. Dataset 1 (doi:10.6084/m9.figshare.13425392.v1) holds the freely moving cells recorded with the inertial sensor, including pitch and roll. Dataset 2 (doi:10.6084/m9.figshare.13425017.v1) holds the freely moving mice tracked without it. I took the question's word that the dandiset has no pitch or roll, since I may not look at the data.

**What changed in `claims/mallory-2021.yaml`:**
- **18 freely moving claims are now `data: elsewhere`,** with the deposits under `where`. These are `fig1b`, the four `fig1c` claims, `fig1d`, the nine `fig2` claims and the three `fig3` claims. The ones on Cohort 1 alone point to Dataset 1. The ones that pool both cohorts or use azimuthal head velocity across them point to Datasets 1 and 2.
- **`supp3`, `supp4`, `supp5` and `supp9` are each split in two,** because each tested freely moving and head-fixed data in one claim. The head part is `elsewhere`, on the figshare deposits. The eye part stays `dataset`, on DANDI:000053. Their old IDs are gone, replaced by `-head-` and `-eye-` versions.
- **Pass rules for the split claims are my own division.** The paper states no rule for either part on its own. For example, `supp5`'s "at least six of seven medians" became "two of three" for the head part and "three of four" for the eye part. `supp9`'s "three of four medians" became "both medians" for each part, which is stricter.
- **The header now names all three figshare deposits** and explains the split.
- **No other statements, quotes or expected values changed.**

The question has its `answer` and `answered: 2026-11-10`. `python tools/claims_check.py` passes the schema and all 46 quotes. It still flags two p-values (`2e-07` and `0.0008`) as not found; the last check had already confirmed both by reading the Supplementary Figure 7 legends.

Only `claims/mallory-2021.yaml` and `questions/mallory-2021.yaml` were edited. Nothing is committed or pushed.
