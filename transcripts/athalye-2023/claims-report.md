I wrote `claims/000404/10.1016-j.cub.2023.06.027.yaml`. The quote checker reports 29 claims, 29 quotes, 55 statistical values and 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript from PubMed Central (PMC10527529), since the version of record is not open access. It includes the full Results, STAR Methods and all figure legends. The supplement was there too: legends of Figures S1 to S6 and Tables S1 and S2. The table columns were jumbled in the text, so I read them from the supplement PDF, pages 15 and 16. I did not use the bioRxiv preprint.

**Code read.** `github.com/pkhanna104/bmi_dynamics_code` at commit `416187366f84f2b7367ac54205aa321480e1acd1`, the same code as Zenodo 10.5281/zenodo.8006653. In the code that wrote the dataset's files, the decoder matrices are commented out, though the paper says decoder parameters were deposited. Most claims need the decoder, so I flagged this for the author.

**Claims.**
- 29 claims, all with a quote and a criterion.
- 21 claims carry statistics, 55 entries in all.
- 20 claims carry expected values, mostly from Table S1. Tolerances are 10% of each value, except two with stated reasons (decoder-null R², Monkey J variance).
- All are `data: dataset`. Figure 6 rests on simulations built from the dynamics fitted to the dataset and the sessions' decoders.

**Details the paper leaves open, and the readings named:**
- **Which commands count:** (a) a command used 15 or more times in at least two conditions, as the Results say; (b) in at least one, as the Figure 3 and 4 code does.
- **Null for Figure 3:** (a) recompute distances on each behavior-preserving shuffle (Methods step list); (b) subsample the matched pool (Statistics Summary and code).
- **Ridge parameter of the shuffle models:** (a) chosen on shuffled data (Methods); (b) the real data's value reused (code).
- **Number of shuffles:** the Methods' 1000 is the main reading. The code uses 10 or 20 for Figures 4D, 4E, 5E, 5F and 5H; that is shown only as a variant, since p < 0.001 cannot be reached with so few.
- **Conditions per session:** counted as (a) any rewarded trial, or (b) at least one command used 15 or more times.
- **The "~7 conditions per command" average:** (a) over commands pooled; (b) the mean of session means.
- **Figure 3E fractions:** the mean of session fractions or the pooled fraction. Neurons are aggregated over all tuples (Methods) or only significant ones (code).
- **Figures 4D to 4F tuples:** all tuples, or only those significant in Figure 3 (code).
- **Figure 5D "~4 dimensions":** the paper gives no rule. Dimensions count when their R² exceeds (a) the full model's R² or (b) the shuffle's 95th percentile; "~4" is read as 3 to 5.
- **Figure S5B pairing:** the paper's N (18 and 8) is twice the session count, while the code pairs one value per session. Readings: (a) per session; (b) per session and task.
- **Words without numbers:** "majority" in Figures 4G and 5F is read as more than half of tuples.
- **Smaller points:**
  - The Methods' "45 and 215 degrees" diagonal in Figure S4G is taken as the code's condition groups.
  - The units of Table S1's single-neuron numbers are Hz, from the code.
  - Where the Methods say nothing, the trial window (go cue to reward) comes from the code.

**Missing.** Nothing a claim needed is missing from the text. Some things are not settled by the code and are noted in the criteria:
- The code splits Figure S3F's model by monkey incorrectly, mixing Monkey J trials into Monkey G's.
- No code gives the "16–17 conditions per session" count or the "~7" average.
- The `NIHMS1910377-supplement-2.pdf` file may not be the only supplement: the PMC numbering suggests a supplement 1 that was not supplied. Nothing cited in the text points to it.
