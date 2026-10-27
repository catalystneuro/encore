# dryad-tdz08kq5d · claims-check · run 40505385610

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/dryad-tdz08kq5d/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/dryad-tdz08kq5d/*.yaml; python tools/claims_check.py claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml paper/10.1093-evlett-qrad056.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml paper/10.1093-evlett-qrad056.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml"
}
```

```
1	# Claims for Wang, Wang, Yang, Lu, Fields, Xu, Shen, Wei & Friman (2024), Evolution Letters,
2	# doi:10.1093/evlett/qrad056, on Dryad dataset doi:10.5061/dryad.tdz08kq5d.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
4	# protocol as stated in docs/protocol.md.
5	#
6	# Text read: the version of record, full text from Europe PMC (PMC10959482, full-text XML), with
7	# Methods, figure legends, Table 1, and the supplement (qrad056_suppl, Supplementary Figures
8	# S1 to S5 and Tables S1 to S6, including the ANOVA tables S1 to S3). The dataset's files were not
9	# opened. Its archive entry names one Excel workbook of the data for all figures and a README.
10	#
11	# Code read: the analysis code the Dryad entry links, Zenodo record 8420504
12	# (doi:10.5281/zenodo.8420504), one file all_r_scripts.R (md5 cff6a1c2e424a2f74ec289cd4888afa8).
13	# It holds plotting code for Figures 1B, 1C, 2 and 3, the growth-curve fits and a summarySE helper.
14	# It holds no ANOVA. What it settles: growth parameters are fitted with grofit gcFitModel at its
15	# default settings, which fit the logistic, Richards, Gompertz and exponential Gompertz models and
16	# keep the one with the lowest AIC (grofit 1.1.1-1 source, grofit.control and gcFitModel); the
17	# Methods say a logistic model, so logistic is the main reading here and the code's AIC choice is a
18	# variant. Failed fits are set to 0 in the code. The ancestral twitching diameter drawn as the
19	# dashed line of Figure 2D is 9.38 cm.
20	#
[... 734 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes on all 32 claims. Now reading the paper to check each claim against it.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-evlett-qrad056.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-evlett-qrad056.txt",
 "offset": 99,
 "limit": 40
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the supplement.

**Agent calls Grep**

```json
{
 "pattern": "^(#|\\[|Table S|Supplementary|Figure S)",
 "path": "paper/10.1093-evlett-qrad056.txt",
 "output_mode": "content",
 "offset": 20
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-evlett-qrad056.txt",
 "offset": 225,
 "limit": 530
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-evlett-qrad056.txt",
 "offset": 754,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1093-evlett-qrad056.txt",
 "offset": 985,
 "limit": 50
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls; find / -name "all_r_scripts*" 2>/dev/null | head; ls transcripts/dryad-tdz08kq5d 2>/dev/null
```

```
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
targets
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://zenodo.org/api/records/8420504 | python -c "import json,sys;d=json.load(sys.stdin);[print(f['key'],f['links']['self']) for f in d['files']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o all_r_scripts.R https://zenodo.org/api/records/8420504/files/all_r_scripts.R/content && md5sum all_r_scripts.R && wc -l all_r_scripts.R && grep -n -i -E "gcFit|grofit|read|mean|summarySE|aov|anova|9.38|<- 0|auc|area" all_r_scripts.R | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 140,190p $TMPDIR/all_r_scripts.R
```

```
#######growth traits including maximum growth rate and maximum density(carrying capacity)########
library(lattice);library(ggplot2);library(grid);library(gridExtra);
library(grofit)
library(bipartite)
library(reshape)
library(lattice)
library(ggplot2)
library(picante)
library(spaa)
library(vegan)
abcd11<-read.table("3510.txt",header=T,sep="\t",dec=".")

abcd11$value<-abcd11$OD600
abcd11$s<-abcd11$strain
abcd11$m<-abcd11$replicate

abcd11.w<-t(as.data.frame(cast(abcd11,time~replicate+strain, mean,margins=c("s", "c","m"))))

param.mat<-mat.or.vec(dim(abcd11.w)[1]-1,3)
colnames(param.mat)<-c("A","mu","lambda")# names for parameters (A: assymptotic growth, mu: max growth rate (h-1), lambda: lag phase)
[... 29 more lines not kept]
```

**Agent**

The checker passes, and the paper's R code from Zenodo matches the md5 the file records. I've found a few things to correct and am now editing the file.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    over the five time points after inoculation, (c) the sum of OD600 over all six time points.\n    The reported df (1, 19) imply 21 values where 20 populations give (1, 18); the F values are\n    not targets. Reproduced when, under one reading, both reductions are within tolerance, the\n    25 degrees C reduction is the larger, and both ANOVAs give p < 0.05.",
 "new_string": "    over the five time points after inoculation, (c) the sum of OD600 over all six time points.\n    The reported df (1, 19) imply 21 values where 20 populations give (1, 18); the F values are\n    not targets. Reproduced when, under every reading, both reductions are within tolerance, the\n    25 degrees C reduction is the larger, and both ANOVAs give p < 0.05; when the readings give\n    different outcomes, the claim is blocked as methods_underspecified."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    three sampled after inoculation, (b) the first three. Reproduced when the temperature and time\n    effects both have p < 0.05, the mean log10 density is higher at 25 degrees C, and at each\n    temperature the mean density is highest at the first sampled time point and lower at the last.",
 "new_string": "    three sampled after inoculation, (b) the first three. Reproduced when the temperature and time\n    effects both have p < 0.05, the mean log10 density is higher at 25 degrees C, and at each\n    temperature the mean density rises from the inoculation density (10^4 PFU/ml, Methods) to its\n    highest value before the last sampled time point and is lower at the last sampled time point\n    than at that highest value."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    phage treatment replicates at 25 °C (Figure 1D; hardly visible in the mean plot due to low frequency\n    of SCVs\n  expected:",
 "new_string": "    phage treatment replicates at 25 °C (Figure 1D; hardly visible in the mean plot due to low frequency\n    of SCVs: 0.24% of all colonies within this treatment)\n  expected:"
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    fits set to 0, is shown as a variant. The Methods speak of 13 time points but list nine; all\n    time points the data hold are used.",
 "new_string": "    fits set to 0, is shown as a variant. The Methods speak of 13 time points but list nine; all\n    time points the data hold are used. The code fits one curve per combination of the growth\n    file's replicate and strain columns, on the mean OD600 at each time point within it; when the\n    replicate column is the technical replicate, a clone's mu and A are the mean of its three fits."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    S3e as in fig2d-scv-twitching-no-exposure-effect. The paper gives no test against the ancestor.\n    Readings for the comparison with the ancestor are (a) as plotted in Figure 2E, the ancestor\n    lies below the interquartile range of the mucoid clones and within that of the SCVs, (b)\n    one-sample t-tests of clone values against the ancestor's value at p < .05, significant and\n    higher for mucoid clones and not significant for SCVs. Reproduced when the colony type effect\n    has p < 0.05 with mucoid higher and the comparison holds under both readings.",
 "new_string": "    S3e as in fig2d-scv-twitching-no-exposure-effect. The paper gives no test against the ancestor;\n    the comparison is read from Figure 2E, which draws the ancestor as a dashed line beside\n    boxplots of the clones. Readings are (a) the ancestor's value lies below the interquartile\n    range of the mucoid clones and within that of the SCVs, (b) it lies below the median of the\n    mucoid clones and within the range of the SCVs. Reproduced when the colony type effect has\n    p < 0.05 with mucoid higher and the comparison holds under both readings; when the readings\n    differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    clones is below that of every -P mucoid group and of the ancestor.",
 "new_string": "    clones is below that of every -P mucoid group and of the ancestor. The Discussion says all\n    mutants showed complete loss of virulence; whether each of the four clones has a disease\n    incidence of 0 is reported alongside."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    CP099581) after FastQC and cutadapt, annotated with PROKKA 1.14.5 (Methods). The paper",
 "new_string": "    CP099581) after FastQC and cutadapt, annotated with PROKKA 1.14.5 (Methods). Counted per clone\n    are variants that change a protein, which the Results say include small deletions, small\n    insertions and SNPs. The paper"
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "  statement: Five KEGG pathways were enriched among the phage-responsive genes, including propanoate\n    metabolism, RNA degradation, ketone body metabolism, bacterial secretion system and valine,\n    leucine and isoleucine degradation.",
 "new_string": "  statement: Five KEGG pathways were enriched in the phage compared to the control treatment, namely\n    propanoate metabolism, RNA degradation, synthesis and degradation of ketone bodies, bacterial\n    secretion system and valine, leucine and isoleucine degradation."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    background set and whether p is corrected are not given; readings are uncorrected and\n    corrected p. Reproduced when the five named pathways are enriched at p < 0.05 under one reading.",
 "new_string": "    background set and whether p is corrected are not given; readings are uncorrected and\n    corrected p. Reproduced when the five named pathways are enriched at p < 0.05 under both\n    readings; when the readings differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "    4B legend (FDR < 0.05, |log2FC| > 1). The 13 genes are those of Figure 4B. Reproduced when phcR",
 "new_string": "    4B legend (FDR < 0.05, |log2FC| > 1). The 13 genes are those of Figure 4B; Table 1 lists 14\n    named genes mutated in +P clones (RSc1174 among them), so the set is read from the figure and\n    not from the table. Reproduced when phcR"
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*/*.yaml | head -1 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml; cat >> $f <<'EOF'
checks:
- date: 2026-10-27
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1d-mucoid-lost-with-phage. Extended the quote to the sentence's end so that it holds the 0.24% the expected value rests on.
  - auc-phage-reduction-by-temperature. The way the area is taken is a method detail the paper leaves open, so the outcome now needs every reading to agree (protocol, Reader step 3) and is blocked when they differ; it was reproduced under any one reading.
  - fig1c-phage-density-temperature. The criterion required the density to be highest at the first sampled time point, which the paper does not say. It now asks for a rise from the inoculation density (10^4 PFU/ml, Methods) to a peak before the last time point and a decline after it, as the Results describe.
  - fig2b-scv-higher-growth-rate. Added what the paper's code settles about the fits (re-read, all_r_scripts.R, md5 as in the header), one fit per replicate and strain combination on mean OD600; fig2c-scv-lower-carrying-capacity uses the same fits.
  - fig2e-mucoid-biofilm-increased. Removed reading (b), one-sample t-tests against the ancestor, a test the paper does not use. Both readings now come from Figure 2E as plotted, and the claim is blocked when they differ.
  - fig2f-mucoid-25p-avirulent. Added that the Discussion says all mutants lost virulence completely, and that zero incidence of the four clones is reported alongside.
  - sequencing-mutation-count. Said which variants are counted, from the Results' description of the 8.5 nonsynonymous mutations.
  - rnaseq-kegg-enrichment. Statement now uses the paper's pathway names and says the five are all the enriched pathways. Whether p is corrected is a method detail, so both readings must agree; it was any one reading.
  - rnaseq-mutated-genes-expression. Noted that Table 1 lists 14 named genes mutated in +P clones, so the 13 genes come from Figure 4B.
  - Open. The unit of the Table S3a to S3c ANOVAs is unresolved; neither reading gives the residual df of 15. Which comparisons give F1,18 = 174.5 and F1,6 = 27.22, and what the 0.24% refers to, also stay open with the readings the file names.
  - Open. The SRA accession that holds the genomes and the one that holds the RNA-seq are not named in the paper.
EOF
python tools/claims_check.py $f paper/10.1093-evlett-qrad056.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The extended quote contains ": ", so it needs quoting.

**Agent calls Read**

```json
{
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "offset": 182,
 "limit": 7
}
```

```
182	    degrees C.
183	  source: Results, Ralstonia solanacearum and phage population density dynamics, paragraph 2;
184	    Figure 1D
185	  quote: We found that ancestral mucoid (M) colony types were lost in the presence of phage at both
186	    temperature treatments and replaced by small non-mucoid colony variants (SCV), except for one
187	    phage treatment replicates at 25 °C (Figure 1D; hardly visible in the mean plot due to low frequency
188	    of SCVs: 0.24% of all colonies within this treatment)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml",
 "old_string": "  quote: We found that ancestral mucoid (M) colony types were lost in the presence of phage at both\n    temperature treatments and replaced by small non-mucoid colony variants (SCV), except for one\n    phage treatment replicates at 25 °C (Figure 1D; hardly visible in the mean plot due to low frequency\n    of SCVs: 0.24% of all colonies within this treatment)",
 "new_string": "  quote: 'We found that ancestral mucoid (M) colony types were lost in the presence of phage at both\n    temperature treatments and replaced by small non-mucoid colony variants (SCV), except for one\n    phage treatment replicates at 25 °C (Figure 1D; hardly visible in the mean plot due to low frequency\n    of SCVs: 0.24% of all colonies within this treatment)'"
}
```

```
The file claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/dryad-tdz08kq5d/10.1093-evlett-qrad056.yaml paper/10.1093-evlett-qrad056.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

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

## End of run

32 turns, 6 minutes, result: success.
