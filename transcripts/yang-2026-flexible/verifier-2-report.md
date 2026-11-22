# Round 2 verifier report: yang-2026-flexible-01

The claims file has 30 claims, and the attempt record has 30 outcomes: 21 reproduced, 2 partially reproduced, 7 blocked.

## 1. Outcomes

I agree with all 30 stated outcomes.

- **split-half-reliability (now reproduced).** I agree. Under seed 0, cell 35 shows 3,598 cells, identical to the paper's list (0 only here, 0 only there). The splits are odd/even 3,112, interleaved 128 and random 358. The within-regime value is 0.1090, chance 0.002581, adjusted 0.1064. Same-pool values are 0.02537, 0.02411 and 0.02011 on 3,276, 3,509 and 3,351 cells. Every value is within the claims file's tolerance.
  - The criterion itself says "random (seed 0)", so using seed 0 is not an assumption.
  - `seed_sensitive: true` is correct: other seeds give pools of 3,256 to 4,100 cells.
- **table2-alignment-ttype and ttype-beyond-cre (partially reproduced).** I agree.
  - Table 2: all A_t have p = 0.0099, and none falls in its tolerance under any of the five seeds.
  - Cre-residual A_t: under the code's own seed-0 draws, long-pulse 0.0113 and brief-pulse 0.0040 are in tolerance; ramp 0.0054 is not.
- **The 7 blocked claims.** I agree they are blocked. `blocked_by: other` is defensible, since the server failed rather than the data being absent. I accept the response on my data_missing label.
- **Assumptions.** Only table1-phenotype-spaces has `assumed: true`. Its two assumptions are stated in its deviations: the meaning of `extract_ok`, and IPFX 2.1.2 through the per-regime functions. Both are reasonable. The cell sets this gives equal the join's regime membership exactly, and the feature lists and k80 equal the paper's (cell 15).

## 2. Sentences the printed outputs do not support

**Notebook**

- **Cell 36:** "The within-regime mean exceeds the three same-pool values under every seed shown (0.1076 to 0.1107 …)". The table in cell 35 includes 0.10714 under the claim's seed, so the range is 0.1071 to 0.1107.
- **Cell 42:**
  - "A_t minus the null mean there, 0.0264, 0.0261 and 0.0161, equals the paper's printed … 0.0264, 0.0266 and 0.0166". Two of the three differ by 0.0005, so "nearly equals" is the most the numbers support.
  - "that changes with the machine's sort of tied ranks". Nothing in the notebook shows any dependence on the machine; this is an inference.
- **Cell 51:** "The files hold two Sst-IRES-Cre lines". The two lines come from the join's `cre_line`, which includes the reporter. In the files' own genotypes, cell 7 counts one Sst-IRES-Cre driver.
- **Cell 10:** the claim quoted for join-link says "Cre line". The claims file's statement says "genotype". The test in cell 11 checks both, so this is wording only.

**Summary (cell 82)**

- "The notebook ran 78 minutes here". Cell 80 prints 74.9 minutes.
- "4,435 NWB files, one cell each". By finding 1, two of these files hold one recording.

**README**

- "4,435 interneurons". The description printed in cell 1 says most are GABAergic interneurons, plus a small number of glutamatergic neurons.
- "about 45 to 78 minutes". Neither figure is printed: the run was 74.9 minutes and the extraction 69.9 (cells 80 and 3).

**Attempt record notes and responses**

- **fig2ab-ttype-structure-within-cre:** "Of the 15 lines tested, 10 have within-Cre A_t with p < 0.05". Cell 50 shows 12, counting the two rows at p = 0.0495.
- **wgcna-mobility-within-type notes, and the responses on all seven blocked claims:** "got a 502 and two time-outs". Cell 80 shows three 502 answers.
- **table2-alignment-ttype notes:** "the first version's run, on another runner, gave 0.0337, 0.0278 and 0.0137".
  - In round 1 I read 0.0336, 0.0276 and 0.0135 in the first version, the same as this run. The record's own verification entry repeats those values.
  - The only evidence offered for machine dependence is therefore contradicted. The residual A_t values (0.0083, 0.0065, 0.0103; ramp seed 2000 −0.0018) are also unchanged between the two runs.
  - The same unsupported claim carries into findings 6 and 7 ("differs between machines", "sort implementation").
- Every other checked sentence matches the printed outputs: the "**Result:**" cells 16–78, the remaining notes, and the counts and ranges.

**Are my round-1 reasons stated in my own words?** Yes, faithfully, as condensed paraphrases. Problems 4, 5 and 7 are folded into the reasons for table1-phenotype-spaces, pair-tag-threshold-sensitivity and fig2ab-ttype-structure-within-cre. Problems 6 and 8 appear in no reason, only in the author's responses. My data_missing labels are kept.

## 3. Round-1 points

**Resolved**

- **Problem 1 (split-half seed):** the seed-0 run reproduces the paper's pool exactly.
- **Problem 3 (WGCNA counts):** 3,906 and 3,902 are now printed (cell 81).
- **Problem 4 (IPFX version):** now printed (2.1.2, cell 1).
- **A_t checks I asked for:** A_t minus null mean is now shown for every seed, and the code's seed-0 draws on both sets of scores (cell 41).
- **Problems 5–8:** answered and acceptable.

**What remains that bears on a conclusion**

- **A_t (table2-alignment-ttype, ttype-beyond-cre).** The code's own draws on the paper's own scores give 0.0368, 0.0318 and 0.0105, against the printed 0.0214, 0.0250 and 0.0213.
  - Why they differ is not shown; "machine sort" is unproven, as above.
  - Under the code's draws, this attempt's A_t minus null mean is 0.0188 for brief-pulse, against the paper's 0.0166 (about 13% off).
  - Neither outcome changes, but the record presents the cause as established when it is an inference.

## 4. Critical findings

Finding **1** is the only one rated `critical`: two files hold the same recording but carry different labels.

- **Do the outputs show it?** Yes.
  - Cell 9: the two files share an identical fingerprint, an identical long-square hash and identical IPFX feature vectors. No other pair of files matches.
  - Cell 11: the join gives them different Cre lines, t-types (Vip Lmo1 Myl1 / Lamp5 Lsp1), layers (VISp2/3 / VISp4) and transcriptomic samples (S010 / S012).
  - The subjects differ by path (cell 7).
  - Not printed: the "all 93 of their IPFX features" count for this particular pair.
- **Is `critical` the right rating?** Yes. One file carries another cell's recording under different metadata, and nothing in the files flags it. The effect on any statistic here is negligible, but the rating depends on the kind of error, not on its effect.

The other findings (format_error, metadata_insufficient: both minor; finding 4: none) are not critical. I did not assess them further.
