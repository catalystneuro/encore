I wrote `claims/crcns-hc-7/10.1113-jp272231.yaml`, and the quote checker reports 0 problems. Nothing is committed.

**Text read.** The version of record (J Physiol 2016), text extracted from the PDF. It has the Methods, Results, Discussion, the legends of Figs. 1 to 13 and Tables 1 to 4. The paper has no supplement and links no code: its analysis software is named in the Methods but not published. I read the data descriptor only to see what the data set holds: paired recordings for eight connection types under the stimulation protocols.

**Counts.** 43 claims. 42 have quotes; one (`table4-model-parameters`) has an `inferred` note, because its numbers come from Table 4 and the Fig. 11 legend. 19 claims carry 41 statistical entries, all 43 have criteria, and 23 have expected values. Some claims test data the data set is not described as holding. These are clustering and cell features (Fig. 2, Tables 1 and 2), connection probability (Fig. 3), spontaneous IPSCs (Fig. 12) and field-potential and optogenetic ripples (Fig. 13A, C). I wrote them as claims and say so in their criteria.

**Details the paper leaves open, with the readings named:**
- **Failures:** the authors' per-sweep success tables, or a detection at 3 standard deviations of baseline (a standard choice, not the paper's).
- **Which APs count as "single":** the AP 1000 ms before the RIP burst, the 1 Hz train, or both pooled.
- **Amplitude in trains:** the per-sweep tables, or the peak of the averaged trace above a local baseline.
- **Sweeps:** all sweeps are used. A variant drops the first three, for the "steady-state average" the Fig. 5A legend mentions.
- **Bonferroni factor:** not stated; taken as the number of pairwise group comparisons.
- **Unnamed tests behind the asterisks in Figs. 5C, 5Db and 7B:** a Wilcoxon signed-rank test against 1, or a Mann-Whitney test. Correction is uncorrected or Bonferroni.
- **Onset of asynchronous release:** a charge above 2 standard deviations, or the current between APs failing to return to baseline.
- **Window for the decay fit:** 500 ms after the last AP, or the return to baseline.
- **Model fitting:** unweighted squared error or squared error normalised to the first IPSC, with BIC = N ln(SSE/N) + k ln N.
- **Recovery half-time:** the fit has a fixed plateau or a free one, and the value is reported as τ or as τ ln 2.
- **PCA for clustering:** z-scored or raw features, and components kept to 80% of variance or with eigenvalue above 1.
- **"Above 160 Hz":** the 160 and 320 Hz trains pooled, or 320 Hz alone.
- **CCK+BC interneuron comparison group:** the paper prints 4.47 ms here but 3.65 ms elsewhere, so the group is CCK+BC pairs, CCK+DTI pairs, or both pooled.

**Missing from the paper:**
- **Figure values:** the PDF could not be opened as images (no renderer is installed here). Values printed only inside figures are not used, such as the Fig. 4B medians and the Figs. 5, 6, 7, 10 and 12 panels. Those claims rest on the Results and the legends.
- **Table 4:** the extracted text lost its per-type parameter columns, so those values come from the Fig. 11 legend. In the CCK+BC row, I assigned the three values to U0, τf and Imax from the header.
- **Undescribed methods:** the paper does not describe sIPSC or ripple detection, the feature definitions, or the filter type. Where a criterion needs one, a standard choice is used and named as such.
