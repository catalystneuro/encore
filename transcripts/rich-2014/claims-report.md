I wrote no claims for rich-2014. Under the Reader section, step 1, the supplement this paper's results rest on is missing, so I stopped there. `claims/rich-2014.yaml` was not created and nothing else changed.

**What was read:** `paper/10.1126-science.1255635.txt`, the version of record of Science 345:814 (2014). It is the main text only: the 4-page report plus the publisher's cover page. Its last page stops at reference 29, so references 30 and 31, the acknowledgments and the supplementary materials list are cut off. The PDF has the same 5 pages and nothing more.

**What is missing:** the Supplementary Materials, at http://www.sciencemag.org/content/suppl/2014/08/13/345.6198.814.DC1.html. That means the Materials and Methods and figs. S1 to S18. The main text has no Methods section, so nothing in hand fixes:
- how cells were selected and isolated in the flanking sleep sessions (fig. S1);
- the track layout and how position was linearized (fig. S2);
- the place field detection criteria (the text gives only the <5 cm/s speed cutoff, in the Fig. 1 legend), and the variants in fig. S15;
- which spikes count toward the analysis windows, given that only the novel sections of each epoch were analyzed;
- how the negative binomial was fit, and how the Kolmogorov-Smirnov and Anderson-Darling tests and the false discovery rate correction were applied;
- how pre-exposure slow-wave sleep firing rates were computed (Fig. 4A);
- the memoryless recruitment analysis (fig. S13).

Several findings are shown only in the supplement: overdispersion and the per-animal recruitment range (fig. S7), the second novel environment (fig. S8), stationarity (fig. S11), pairwise correlations between cells (fig. S12), anatomical modulation (fig. S16) and correlated propensities across environments (fig. S17).

**Other notes:** the paper links no code. The hc-31 data description says the dataset holds 5 rats on the novel 48 m track, a repeat exposure, a second open-field environment and the flanking sleep sessions. That matches the paper. As instructed, I did not look at the data.

**To proceed:** add the supplement's text, or its PDF, under `paper/` and rerun the reader.
