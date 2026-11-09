I wrote `claims/001882/10.3390-genes16010043.yaml`. The quote checker reports 25 claims, 23 quotes, 0 statistical values and 0 problems.

**Text read:** the version of record (open access, Europe PMC PMC11764596), including the Introduction, Methods, Results, Discussion, the legends of Figures 1 to 4, and Tables 1 to 4 inline. There was no PDF, but the tables were legible in the text. The paper names no supplement and links no code, so no code was read. Its Data Availability Statement says "No new data were created or analyzed", even though the dandiset is described by this paper.

**Claims:** 25 in total.
- **Quotes:** 23 have a quote. The other 2 have an `inferred` note: Table 1 sex, age and diagnosis, and Table 1 visual acuity (BCVA).
- **Statistics:** none. The paper reports no tests or intervals.
- **Expected values:** 5 claims have them: prevalence counts and percentages, Table 2 scores, Table 3 ΔΔG values, Table 4 ProtParam values, and gnomAD frequencies.
- **Criteria:** every claim has one.
- **Data:** 6 claims use outside tools or databases (`with_inputs`): pathogenicity scores, the novelty of p.Asp423Glu, stability, the two interatomic-interaction claims, and physicochemical properties. Two more (gnomAD frequencies and the novelty check against ClinVar) need public databases. The rest are clinical claims on the dataset: prevalence, ancestry, genotypes, inheritance, BCVA, the seven per-patient imaging phenotypes, the Discussion's findings, M73's EOG, and other gene variants.

**Details the paper leaves open, with the readings named:**
- **Imaging features:** the paper grades them by eye only, with no measure. The criterion is to inspect each modality and eye against the places the figure arrows mark. This is the only method the paper allows, and it is recorded as a deviation.
- **Text and legend disagree on autofluorescence:**
  - M75's left eye: hyper-autofluorescent in the text, hypo in the legend.
  - M34: faint hyper in the text, hypo in the legend.
  - Either reading counts.
- **Arg131's lost van der Waals partner:** the text names Gln1236 in one place and His135 in another. Either counts.
- **When ages were taken:** at the most recent visit, or at data collection in 2024.
- **Which BCVA visit:** the most recent, or any recorded visit.
- **"Not significantly reduced" acuity:** the text places the threshold between 20/40 and 20/50, and any value there sorts the patients the same way.
- **Table 2 scores:** the genome build (GRCh37 or GRCh38), the transcript (MANE Select), and the CADD version (v1.6 or v1.7) are not given.
- **Table 3, "largest destabilizing" for p.Leu249Phe:**
  - Readings: the mean over the five tools, a majority of tools, or every tool.
  - The table itself fails the "every tool" reading: SDM and iMutant each rank another variant larger.
- **Structural models:** I-TASSER models underlie the structure-based stability tools and DynaMut. They were not deposited, so they must be re-predicted.
- **Protein sequence:** the paper names none. The readings are the canonical UniProt entry (IMPG1 Q17R60, IMPG2 Q9BZV3), with or without the signal peptide for ProtParam.
- **gnomAD:** the version is not given; the readings are v3.1.2, or v4.1 joint, exomes or genomes. "1 in N" is not defined; the readings are 1/allele frequency or 1/(2 × allele frequency).
- **Database releases:** the ClinVar release is not given; the reading is the one current in November 2024.
- **EOG:** the paper gives no normal range and no method.

**Inconsistencies in the paper, noted in the criteria:**
- The prevalence percentages are truncated (7/480 is 1.458%, printed as 1.45%). Both readings fall within tolerance.
- In Table 4, the p.Asp423Glu row (+32 Da, +7 atoms) does not match a single Asp to Glu change (+14 Da, +3 atoms).
- The Discussion credits the higher pI and instability index to p.Leu740Phe, which Table 4 contradicts.
- Table 1 misspells IMPG1 as "IMGP1".

**Missing from the paper:** nothing a claim needed to be written. The EOG values, the tool versions and the structural models are absent, and the claims that use them name this as open.
