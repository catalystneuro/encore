I wrote the claims file at `claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml`. The quote checker passes with 0 problems; nothing is committed.

**Text read:** the version of record, from Europe PMC (PMC11750374), with the full supplement (Tables S1 to S11 and Fig. S1). The extracted text is missing the model equations and priors from the Methods. The paper's code on Zenodo (doi:10.5281/zenodo.14226724, `Code.zip`, SHA-256 recorded in the file) gives them in full: the Stan model, its priors, the predictors in each model, how year is coded (per decade), and the seeds. From the archive I read only the Dryad title and description. The description says the climate data are already scaled within species, which settles how climate enters the models.

**Claims:** 32, all with quotes (31 findings and one link claim on sample sizes).
- **Quotes:** 32.
- **Statistics:** 10 claims, 58 values in all. These are 95% intervals from the preliminary models, the lambda intervals, and the Table S8 trend intervals with their pMCMC values.
- **Criteria:** 32.
- **Expected values:** 19 claims. The tolerance on each posterior mean is the s.d. the paper reports.
- **Bayesian results:** the main results are probabilities of direction (pd), with "significant" meaning pd of at least 90%. The schema's statistics field can't hold a pd, so pd values are in the statements and criteria.

**Details left open, with the readings named:**
- **Outlier filter:** the Methods remove specimens more than 5 median absolute deviations from the median, but the code applies no filter. Readings:
  - (a) the data as deposited;
  - (b) the filter per species, using R's `mad()` with its default constant;
  - (c) the filter per species and sex;
  - (d) as (b) with the unscaled deviation.
- **Interval in Tables S4 to S6:** either (i) quantiles of the four pooled chains or (ii) the 95% HPD of chain 4. The code prints both.
- **Data for Table S8:** the code reads an object, `envdata3`, that no script defines. Readings: (a) every species-year from 1980 to 2017; (b) only species-years that have specimens.
- **"Climate explains a small amount" of variation:** the paper gives no measure. Readings: (a) every climate coefficient is smaller than the year coefficient; (b) climate's share of the variance in the fitted intercepts is smaller than year's. If they disagree, the claim is blocked as `methods_underspecified`.
- **Standard choices that can't change the outcome:** the pd formula (share of draws with the sign of the median), and a seed for the MCMCglmm runs, which the code leaves unseeded.

**Gaps in the paper:** none that stopped a claim.
- **Phylogeny:** the preliminary models and Table S8 need a phylogeny file, `chitree.rds`. If the deposit lacks it, it has to be rebuilt from BirdTree, and those claims then rely on outside data.
- **Conflict for the author to note:** the Discussion says no model shows a shift in slope over time, but Table 1 reports a negative year effect on the slope for hatch-year birds (pd 92.5%). Both are claimed as the paper states them.
