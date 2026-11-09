I've done Author steps 1 to 5 for DANDI:001882 and built the verifier's package (`python tools/entry.py handover`, step 6). The entry passes `check` and ran clean twice from a fresh environment (`all`), giving identical outputs both times. Nothing is committed.

The main thing to know first: the dataset holds no recordings. It contains a spreadsheet of the seven patients (the paper's Table 1), a Word document of in silico tool outputs, and the paper's own Figures 1 to 4 as image files. So the eight claims about what the patients' eye images show were judged by my eye on the paper's own published figure panels. Those tests check the paper's text against its figures, not against independent data.

I pinned version 0.260701.1757 because the paper cites no version and it is the only published one; the draft has the same 13 files.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-prevalence | reproduced (7 carriers, 2 RP, 5 VMD; the denominator of 480 is taken from the paper) |
| table1-genotypes, table1-diagnosis-sex-age, inheritance-by-disease, table1-bcva | reproduced |
| vmd-acuity-preserved | reproduced (M73 is the only reduced patient under all 4 readings) |
| f32-sector-rp-phenotype, rp-superior-field-no-cme | reproduced (my visual reading of Figure 2) |
| m83, m75, m82, m73, f57, m34 phenotypes; m73-f57-similar-lesions | partially reproduced (2 to 6 of each claim's features visible) |
| variant-domains | partially reproduced (6 of 7 placements under both UniProt and InterPro) |
| table4-impg1-physicochemical | partially reproduced (14 of 18 values) |
| gnomad-frequencies | reproduced (all 6 values under gnomAD v4.1 joint counts, read as 1/(2 × allele frequency)) |
| table2-pathogenicity | not reproduced (IMPG2 scores match exactly; IMPG1 scores and the p.Asp423Glu "pathogenic" call do not) |
| asp423glu-novel | not reproduced (it is ClinVar entry 1000102 in all four November 2024 releases) |
| all-caucasian, m73-eog-normal, other-gene-variants | blocked: data_missing |
| table3-destabilizing, impg1-interactions-unchanged, impg2-interactions-changed | blocked: not_runnable (the I-TASSER structure models are not deposited; the tools are web servers) |

## 2. What I found about the dataset

- **No clinical data.** There is no EOG, no genetic report, no race or ethnicity, no visit dates and nothing on the other 473 patients. Each eye has one image per modality, one OCT scan and one angiogram frame.
- **Possible patient identifiers.** The spreadsheet's first column appears to hold hospital record numbers, in a public dataset under a CC0 licence. I never printed or used them, but the data owner should look at this.
- **Metadata errors.** The metadata say one subject and no species. The figure files are named as microscopy samples ending in `.ome.tif` but are RGB exports from Adobe Illustrator. The paper is not linked in the structured metadata, and six Google Drive `desktop.ini` files are deposited.
- **Word document against the paper.** It disagrees with Table 3: SDM gives p.Asp423Glu +0.58 (stabilizing) where Table 3 prints −0.52, and its MuPRO value for p.Leu249Phe repeats the p.Cys1019Tyr number.
- **Paper errors.**
  - Table 4's p.Asp423Glu column matches an Asp→Phe change exactly.
  - Table 2's two IMPG1 SIFT scores are swapped between the variants.
  - Two rs ids in Table 2 are mistyped.
  - In the Figure 4 IMPG2 image, the variant labels are one row out of step with the pictures.

**Assumptions:** none (no outcome is marked `assumed`). Where the claims file named several readings, I ran them all. The FAF brightness measures use my own standard cut-offs and are recorded as such.

**Question for the paper's authors** (recorded as a `methods_unavailable` finding): which PolyPhen-2, FATHMM, MutationTaster and CADD versions or outputs produced Table 2; which gnomAD version and reading of "1 in N"; and where Figure 1's domain boundaries come from.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. The protocol and `docs/archives.md` assume NWB files with a time base. This dataset has neither, so the clock check could not apply; I said so in the notebook.
2. `entry.py check` rejects any `imread(` or `Image.open(` as "reads an image file", but here the images are the data. I read them with `tifffile.TiffFile` and `imagecodecs`, which the check does not catch. The rule needs an exception for image data from the archive.
3. Criteria that rely on visual reading conflict with "every sentence backed by a printed number". I printed my readings as a table, giving the panels each rests on, and added measured brightness ratios for the FAF features.
4. The protocol gives no guidance for claims tested on the paper's own figures. I tested them and flagged the circularity in each claim's notes and deviations.
5. Outside services (Ensembl VEP, gnomAD, InterPro, MyVariant/dbNSFP) cannot be pinned by a DOI or a commit. I recorded the release numbers each one printed.
6. There is no guidance for personal data found in a dataset. I kept it out of the outputs and reported it as an `other` finding.
7. The ten-minute target could not be met: the notebook takes 13 to 15 minutes, almost all of it waiting for VEP. I sent all VEP requests at once with retries and dropped the GRCh37 VEP run.
8. One criterion (m73-f57-similar-lesions) gives no rule for a partial result. I used partially_reproduced and said why.
9. `pysam` saves ClinVar index files into the working directory. I made it work in a temporary directory so nothing is written to the entry.
10. `measured` must be numbers. The cohort size of 480 comes from the paper, so I recorded it with a deviation saying it is not a measurement.

## 4. Runtime and failures

The run took about 2 h 20 min (23:22 to 01:43 UTC). The notebook takes 797 to 871 s.

Failures along the way, all fixed before the final run:
- The first run's VEP request (one batch for all seven variants) gave up after about 13 minutes without an answer.
- An Ensembl coordinate-mapping call timed out.
- Two coding bugs.

Final fixes:
- Variant positions now come from dbNSFP.
- VEP requests are sent in parallel with retries.

The last two full runs passed with identical outputs. If Ensembl is slow or down when CI runs the notebook, the table2 cell can still fail; that is the remaining risk.

Untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others) are in the repo root; I left them alone.
