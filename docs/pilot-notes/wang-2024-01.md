# dryad-tdz08kq5d, Wang et al. 2024

Twenty-four claims reproduced, four partially, one not reproduced and three
blocked, all on the dataset. It pins version 263142, the only version Dryad's
API lists, which holds a README and one Excel workbook of 16 sheets. The
paper, in Evolution Letters, grows the plant pathogen Ralstonia solanacearum
RS-N with or without phage NNP42 at 25 or 35 degrees C over 12 days in 10
replicate populations per treatment, and reports that phage-exposed clones,
mostly small colony variants (SCVs), are more resistant to the phage and less
virulent in tomato at both temperatures. The claims were written from the
version of record in Europe PMC with its supplement, and from the analysis
code in Zenodo record 8420504, which holds no ANOVA. The bacterial and phage
densities of Figure 1, the colony type frequencies, the resistance, growth,
twitching, biofilm and virulence of the evolved clones in Figure 2, the
adsorption of Figure S3, and the sequencing and RNA-seq claims were tested,
the last on the dataset's processed variant, DESeq2 and KEGG tables, as the
pipelines from raw reads were not re-run. `table1-t2ss-in-35p-scv` is blocked
as `metadata_insufficient`, as the count is 3 or 2 clones with a tolerance of
0, `tables6-pil-mutants-resistant` as `data_missing`, as no sheet holds the
pilB or pilM mutants, and `rnaseq-kegg-enrichment` as
`methods_underspecified`, as exactly the five named pathways have uncorrected
p < 0.05 and none has FDR < 0.05 (smallest 0.1958); a question asks the
reader which the paper used. `sequencing-mutation-count` is not reproduced,
with 10.07 protein-changing variants per clone against 8.5 +- 0.85, and
`fig1d-phage-raises-scv-frequency` is partially reproduced, as the mucoid
share without phage at 25 C is 15.34%, outside 20 +- 2. The author put four
questions to a reader; the answers fixed the OD600 time points as days 2 to
12, named the mean of replicate frequencies and the pooled share as readings
of the 0.24%, set the unit of the Table S3a to S3c ANOVAs as the mean of the
clones of each colony type within each replicate population, which moved
`fig2a-temperature-resistance` and `fig2c-scv-lower-carrying-capacity` from
blocked to reproduced, and made the nine sequencing and RNA-seq claims
`data: dataset`, with no outcome changed. Round 1 gave its own outcome for
each claim and agreed with 30 of 32; the author took its outcomes for
`fig2e-mucoid-biofilm-increased` and `rnaseq-mutated-genes-expression` (from
not reproduced to partially reproduced), and its points led the data check to
print the README and the ancestor block of each Figure 2 sheet, which shows
one ancestor row per sheet. Round 2 agreed with all 32, so there was no third
round; it found six statements the outputs did not support, among them an R
range of 0.21 to 1.12 against 0.1833 to 1.1187 printed, a position for the
RSc3091 deletion that no output printed and a clause crediting Table S4 with
fixing the paper's choices, and these were corrected. Some outcomes rest on
weak ground: `fig1b-phage-effect-diminishes` compares only the last day with
the largest earlier value, while at 25 C the difference falls to 0.049 on day
8 and rises to 0.322 on day 12; in `fig2a-temperature-resistance` mucoid
clones have higher R at 25 C (0.378 against 0.295), so the effect over all
clones comes in part from the colony types each treatment yielded; and
`fig2b-scv-higher-growth-rate` and `fig2c-scv-lower-carrying-capacity` test
the deposited fitted values, as the fits could not be repeated. The work took
about 25 minutes and the notebook runs in about 10 s; earlier runs hit two
bugs, a column-name match and a float `.lower()`, both fixed, and ENA
returned the RNA-seq runs in a different order on each run, so they are now
sorted.

The genome reads are not public: BioProject PRJNA1028400, named in the paper
for the evolved clones, has 28 BioSamples and 14 assemblies and no sequencing
runs, and the variant table gives, per variant and group of four clones, the
number of clones that carry it, not which clones, so per-clone mutation
counts and co-occurrence cannot be read. The RNA-seq reads are public in
PRJNA1032726 (ten runs, 9.1 GB), though the Methods say they are shared on
request. The twitching sheet does not identify its clones: it has no
morphotype column, its four 35_1 rows carry the names of four 35_0 SCV clones
with different values, and in 25_0 the four mucoid names appear twice with
different values, so colony types were read from the design. Its values do
not reproduce Table S3d, with a total sum of squares of 72.28 against 82.08
summed from the table, so no assignment of colony types reproduces it if its
sums of squares are sequential, which the table does not state; every other
ANOVA the paper prints (Tables S1a, S1b, S2, S3a to S3c, S3e, S3f) is
reproduced from the deposited data. The growth curves behind the maximum
growth rates and carrying capacities are not deposited, only one fitted value
per clone, so whether the logistic model of the Methods or the code's best of
four by AIC produced them cannot be checked. The data disagree with the text
in places: every SCV clone forms more biofilm than the ancestor (0.58 to 0.95
against 0.49 OD570), where the text says SCVs retained ancestral-level
biofilm; gspG is upregulated (log2FC 2.04), where the text lists it as
downregulated; phcS has log2FC 0.41, below the threshold under which the text
calls it significantly upregulated; and the 0.24% the text gives as an SCV
frequency is the mucoid frequency of the 25 C +P treatment. Other findings:
the area-under-curve ANOVAs are printed with df (1, 19) for 20 populations,
the phage density time effect is printed in the text as F1,18 = 84.88, which
is its sum of squares, Table S3e prints the temperature sum of squares as
0.346 for 0.3646, and Table 1 places the RSc3091 deletion at C-432461 where
the variant table has 431461; the OD600 values include day 0 and eight
negative values (down to -0.029), so they are blank-corrected, which neither
the README nor the Methods says; the README gives no unit for the growth rate
and does not say adsorption is a proportion; in the carrying capacity sheet
the ancestor's value (1.4355) is headed maxgrowthrate(OD600); the variant
table uses PROKKA gene names that differ from the paper's (phcS is sasA_8,
pilD outO, gspE hxcR, gspF epsF_1), which the gene_blast sheet maps by locus
tag; and the Figure 4B list holds 11 genes where the paper speaks of 13.

The author's points on the protocol: claims marked `elsewhere` whose
processed data are in the dataset have no rule, so they were tested on those
tables and a question was asked; the check forces `inputs` for tested
`elsewhere` claims, though the BioProject metadata read has no version or DOI
to pin; `entry.py`'s local-path check rejects a quoted path under `/tmp`,
where Dryad files are staged; it does not say whether matching the paper's
own printed table may settle a reading, as the claims file assumed six OD
time points where the data hold seven; it has no rule for counts that cannot
be identified from aggregated tables; it says to judge an absence claim on
the paper's test alone, though here that test had its own readings; and it
gives no guidance for rows whose identifiers are wrong.
