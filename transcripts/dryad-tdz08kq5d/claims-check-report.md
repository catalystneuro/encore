**Checker result:** `claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml: 32 claims, 32 quotes, 32 statistical values, 0 problems`. It gave the same result before and after my edits.

The statistics are all taken from the paper's text and Tables S1 to S3, and none of them are thresholds. I downloaded the paper's R code from Zenodo; its md5 matches the one the file records.

**Changes, by claim:**
- **fig1d-mucoid-lost-with-phage:** The quote stopped just before the 0.24% that the expected value rests on. I extended it to the end of the sentence.
- **auc-phage-reduction-by-temperature:** The paper doesn't say how the area under the curve is taken, so this is an open method detail. The claim now needs all readings to agree and is blocked when they differ. It used to pass under any one reading, which the protocol does not allow.
- **fig1c-phage-density-temperature:** The criterion required phage density to peak at the first sampled time point, which the paper doesn't say. It now asks for a rise from the inoculation density (10^4 PFU/ml, Methods), a peak before the last time point, and a decline after it, as the Results describe.
- **fig2b-scv-higher-growth-rate** (and fig2c, which uses the same fits): Added what the code settles. It fits one curve per replicate and strain combination, on the mean OD600 at each time point.
- **fig2e-mucoid-biofilm-increased:** Removed the one-sample t-tests against the ancestor, a test the paper never uses. Both readings now come from Figure 2E as plotted, and the claim is blocked if they differ.
- **fig2f-mucoid-25p-avirulent:** Noted that the Discussion says all mutants lost virulence completely, and that zero incidence for the four clones is reported alongside.
- **sequencing-mutation-count:** Stated which variants are counted, using the Results' description of the 8.5 nonsynonymous mutations.
- **rnaseq-kegg-enrichment:** The statement now uses the paper's pathway names and says these five are all the enriched pathways. Whether the p-values are corrected is a method detail, so both readings must agree; before, either one was enough.
- **rnaseq-mutated-genes-expression:** Table 1 lists 14 named genes mutated in +P clones, while the paper says 13. The note now says the 13 come from Figure 4B.

**Still open** (recorded in `checks`):
- The unit of analysis for the Table S3a to S3c ANOVAs: neither reading in the file gives their residual df of 15.
- Which comparisons produce F1,18 = 174.5 and F1,6 = 27.22, and what the 0.24% refers to. The file names readings for each.
- Which of the two SRA accessions holds the genomes and which holds the RNA-seq.

Every main finding has a claim, and all claims come from this paper.

**Ready:** yes, recorded as `ready: true`. Nothing was committed or pushed.
