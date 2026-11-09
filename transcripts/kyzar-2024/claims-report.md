I wrote `claims/000469/10.1038-s41597-024-02943-8.yaml`. It has 20 claims, all 20 with word-for-word quotes, and the quote checker reports 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10796636), full text with Methods, Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has no supplement. Its Methods say they are shortened from refs 15 and 20 (Kaminski 2017 and 2020). Those two papers are also under `paper/`, but I did not use them, since the protocol takes methods only from this paper and its code.

**Code read:** `rutishauserlab/workingmem-release-NWB` at commit f8594e0. Its code is the same as tag v1.0.0 (4a98f46); only the README and citation file differ. A rewrite for another dataset was added and reverted the same day, and I ignored it. The Methods name permutation tests; the code runs ordinary parametric tests (ANOVA, paired one-sided t-tests) and keeps permutation versions only in comments. Following the protocol, the Methods give the main criteria and the code's tests are variants. The code also has three bugs:
- **Trial masks:** the masks for preferred and non-preferred trials pick every trial and no trial. As written, the code cannot produce the paper's persistent-activity numbers, and its extra maintenance test for concept cells cannot run.
- **Wrong window:** its "preferred vs non-preferred" rates come from the first encoding window, not the maintenance period the paper names.
- **Encoding 3:** the probe test counts the Encoding 2 window a second time in place of Encoding 3.

**Statistics and criteria:**
- **Statistics:** two claims record a statistic. These are the load effect on reaction time (F(2,40) = 7.92, p = 0.0013) and the persistent-activity test (p = 1.38e-21).
- **Expected numbers:** 19 claims have them, all with a 10% tolerance. The exception is the subject and session counts, which have zero tolerance.
- **Criteria:** all 20 claims have one.

**Details the paper leaves open, and the readings I named:**
- **Second step of the concept-cell test:** two-sided (as the code does it) or one-sided "larger" (as the Methods word it). This applies to both the screening and Sternberg claims and the Fig. 4 and 5 example units.
- **Permutation design** (maintenance and probe cells): shuffling trial labels (the code's commented-out version) or a paired sign flip. Neither source gives the number of permutations; I used the code comment's 2000 as a standard choice.
- **"Non-preferred trials" for concept cells in the maintenance test:** trials whose first image is not the preferred one (what the code intends), or trials where the preferred image was not shown in any encoding period.
- **Encoding rate in the probe test:** pooled over all encoding periods in the trial (what the code intends), or Encoding 1 only.
- **Persistent activity, which cells:** the 94 MTL concept cells, or all concept cells in any area (as the code tests).
- **Persistent activity, which trials count as preferred:** the preferred image in any encoding period, or in Encoding 1 only. The code's comparison in the encoding window is shown as a variant.
- **Refractory-period violations:** the text says all units; the code averages only units whose value is below 4%.
- **Signal-to-noise ratio:** the sentence describes the peak SNR but cites Fig. 3g and h, so both the peak and the mean SNR are named.
- **Settled by the code, not left open:** reaction times use correct trials only; the concept-cell window is Encoding 1 only; all trials are used for selectivity.

**Inconsistencies in the paper (nothing a claim needed is missing):**
- **Screening MTL count:** the text says 449 MTL units in screening. The screening percentages (32.78% for 138 cells, 5.35% for 26) imply about 421 MTL and 486 MFC units. Both 449 and 421 are named as readings.
- **Ages:** the text gives 17 to 71, while Table 1 lists 17 to 70.
- **Figure citation:** the projection distance is cited as Fig. 3g, but the legend puts it in panel i.
