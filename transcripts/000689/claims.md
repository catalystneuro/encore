# 000689 · claims · run 39898888376

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000689 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; ls claims/001453/ claims/000689 paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls paper/ claims/001453/ claims/000689 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt claims/001453/*.yaml; head -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; awk '{print NR": "length($0)" "substr($0,1,150)}' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

One long line. I'll split it into sentences to read it.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -w 4000 -s > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; sed -n '1,12p' $TMPDIR/p.txt | cut -c1-200000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	pmc Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC9583860 PMC9583860.1 9583860 9583860 NIHMS1840566 35859170 10.1038/s41586-022-04964-y NIHMS1840566 NIHPA1840566 1 Article Neurotensin orchestrates valence assignment in the amygdala Li Hao 1 * Namburi Praneeth 2 * Olson Jacob M. 2 3 * Borio Matilde 1 2 Lemieux Mackenzie E. 1 2 Beyeler Anna 2 4 Calhoon Gwendolyn G. 2 5 Hitora-Imamura Natsuko 2 6 22 Coley Austin A. 1 Libster Avraham 1 2 Bal Aneesh 1 7 Jin Xin 8 9 Wang Huan 10 Jia Caroline 1 11 Choudhury Sourav R. 9 Shi Xi 9 12 Felix-Ortiz Ada C. 2 de la Fuente Verónica 2 13 Barth Vanessa P. 2 14 King Hunter O. 2 15 Izadmehr Ehsan M. 2 Revanna Jasmin S. 1 16 Batra Kanha 1 17 Fischer Kyle B. 1 Keyes Laurel R. 1 Padilla-Coreano Nancy 1 Siciliano Cody A. 2 18 McCullough Kenneth M. 19 20 Wichmann Romy 1 2 Ressler Kerry J. 19 20 Fiete Ila R. 12 Zhang Feng 9 12 21 Li Yulong 10 Tye Kay M. 1 2 23 24 1 Salk Institute for Biological Studies, La Jolla, CA 92037, USA 2 The Picower Institute for Learning and Memory, Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge, MA 02139, USA 3 Neuroscience Program, Department of Psychology, Volen National Center for Complex Systems, Brandeis University, Waltham, MA 02453, USA 4 University of Bordeaux, Neurocentre Magendie, INSERM 1215, 146 rue Léo Saignat, 33000 Bordeaux, France 5 Neuroscience Program, Bates College, Lewiston, ME 04240, USA 6 Department of Pharmacology, Graduate School of Pharmaceutical Sciences, Hokkaido University, Sapporo, Hokkaido 060-0812, Japan 7 Behavioral neuroscience, Department of Psychology, Michigan State University, East Lansing, MI 48824, USA 8 Society of Fellows, Harvard University, MA 02139, USA 9 Broad Institute of MIT and Harvard, Cambridge, MA 02142, USA 10 State Key Laboratory of Membrane Biology, Peking University School of Life Sciences, Peking-Tsinghua Center for Life Sci
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 14,
 "limit": 13
}
```

```
14	encompassing the eye of the mouse was drawn, and each frame was smoothed using a Gaussian filter. The average intensity of all the pixels within the eye ROI was used as a metric for the size of the eye. To control for background changes in intensity, the reference ROI time course was regressed from the eye ROI time course. The area under the eye blink trace from the onset of the CS to the onset of the US (for every CS-US pairing) was compared using an unpaired t-test. Only animals that showed a significant difference between the first 15 CS-US presentations on the first session and all the CS-US presentations in the second session were considered to have acquired the association between the tone and the airpuff and were used for further analysis. CRISPR-mediated gene cKO The CRISPR-associated endonuclease Cas9 from Streptococcus pyogenes (SpCas9) was used to generate indels in the neurotensin gene ( NC_000076 ). Neurotensin ( Nt ) and Neurotensin receptor 1 ( Ntsr1 ) -specific single guide RNAs were designed on Benchling ( https://benchling.com/ ) using the GRCM38 ( Mus musculus ) reference genome. Based on the computed specificity and efficiency scores, we cloned guides 1 and 2 (GAAGGCTGAGAGAAGATGAG and GCTAAAACCATCCAGAACAA for Nt guides, and GGAGCTGTTGAGGTGCATGG and AGGATGGAGATGATCAGCAT for Ntsr1 guides) to target exon 1 of the reverse strand and exon 3 of the forward strand of the neurotensin coding region, and exon 1 and exon 2 of the neurotensin receptor 1 coding region. Non-targeting negative control guide was designed with a scrambled sequencing with no known targets in the genome (GGAAGAGCGAGCTCTTCT). Each gRNA was cloned into vector PX552 (pAAV-U6-sgRNA_hSyn-GFP-KASH-bGH; Addgene # 60958). The two AAV vectors targeting the same gene were pooled with equal titer prior to the stereotactic injection. Virus construction and packaging: For non-pathway specific CRISPR-mediated Nt gene CRISPR-cKO ( Figure 1 , E3 , E4 ), high-titer AAV9 virions encoding AAV-SpCa
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 27,
 "limit": 15
}
```

```
27	nucleus, ventral part (BLV), basomedial amygdaloid nucleus, anterior part (BMA), basomedial amygdaloid nucleus, posterior part (BMP). These regions are labeled across 6 coronal sections in ( h ). Each circle in ( j ) shows data from an image obtained from one coronal section from a single mouse. The size of the circle represents the anterior-posterior coordinate relative to bregma, and the mapping is shown in the legend at the bottom. N denotes number of mice in each group. Error bars and solid shaded regions around the mean indicate s.e.m. Extended Data Figure 2: MGN:NT, vHPC:NT and PVT:NT populations evokes both EPSCs and IPSCs in BLA neurons, but IPSCs are not monosynaptic. a : Representative images of BLA neurons at lower (left) and higher (right) magnifications used to assay synaptic currents from axon terminals coming from the MGN, the vHPC or the PVT. b : Representative traces of excitatory and inhibitory post-synaptic currents (EPSCs and IPSCs) recorded from putative principal neurons in the BLA upon stimulating ChR2-expressing axon terminals from NT populations in the MGN (left), the vHPC (middle) and the PVT (right). c : The EPSCs had faster onset times than the IPSCs upon stimulation of NT population axon terminals from the MGN (Two-tailed paired t-test, t 11 =3.587, ** P =0.0043), the vHPC (Two-tailed paired t-test, t 4 =3.730, * P =0.0203) and the PVT (Two-tailed paired t-test, t 8 =4.354, ** P =0.0024). d : Light-evoked EPSCs were monosynaptic as they were still evoked upon stimulation of axon terminals from NT populations of all three regions after the application of TTX+4-AP. Monosynaptic EPSCs were significantly reduced by the application of glutamate blockers for AMPA and NMDA receptors, AP5 and NBQX respectively (One-way ANOVA with Holm-Sidak’s multiple comparisons test. The MGN: F (2, 27) =9.613, TTX+4-AP vs. ACSF: t 27 =1.209, P =0.2372, effect size=−31.28 ± 28.87; TTX+4-AP vs. AP5+NBQX: t 27 =3.19, ** P =0.0072, effect size=89.95 ± 28.2; The
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls tools docs; sed -n 1,80p tools/claims_check.py; ls claims | head -50; ls claims | wc -l
```

```
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md

tools:
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200; head -40 claims/000715/*.yaml
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dataset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "dataset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
    "dataset": {
      "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
      "type": "object",
      "additionalProperties": false,
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))" | head -120; grep -rl "000689" --include=*.json --include=*.yaml --include=*.md . 2>/dev/null | head
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(items, dict):
    for k,v in items.items():
        if '000689' in k: print(json.dumps(v,indent=1)[:3000])
else:
    for v in items:
        if '000689' in json.dumps(v)[:200]: print(json.dumps(v,indent=1)[:3000])
EOF
grep -n -B2 -A10 "000689" papers/manifest.yaml
```

```
997-    pdf: false
998-    supplements: 2
999:  000689:
1000-  - doi: 10.1038/s41586-022-04964-y
1001-    status: stored
1002-    version: as served by ncbi_pmc
1003-    source: ncbi_pmc+crossref (paper-text-fetcher)
1004-    pdf: false
1005-    supplements: 0
1006-  000691:
1007-  - doi: 10.1038/s41592-023-01806-1
1008-    status: stored
1009-    version: version of record
```

**Agent calls Bash**

```bash
cd  grep -n -A25 '"000689"' targets/dandisets.json | head -60
```

```
3356:   "dandiset": "000689",
3357-   "name": "Data supporting Neurotensin orchestrates valence  assignment in the amygdala",
3358-   "published_version": "0.240530.1923",
3359-   "asset_count": 85,
3360-   "size_gb": 574.78,
3361-   "data_standards": [
3362-    "Neurodata Without Borders (NWB)"
3363-   ],
3364-   "species": [
3365-    "Mus musculus - House mouse"
3366-   ],
3367-   "approaches": [
3368-    "electrophysiological approach"
3369-   ],
3370-   "papers": [
3371-    {
3372-     "doi": "10.1038/s41586-022-04964-y",
3373-     "title": "Li, H., Namburi, P., Olson, J.M. et al. Neurotensin orchestrates valence assignment in the amygdala. Nature 608, 586-592 (2022).",
3374-     "relation": "IsDescribedBy",
3375-     "resource_type": "JournalArticle",
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000689/versions/0.240530.1923/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'));print(m.get('assetsSummary',{}).get('variableMeasured'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  f=$TMPDIR/p.txt; for s in "We recorded a total of 685" "we clustered BLA neurons into seven" "We found that the CRISPR-Cas9 mediated" "Initially, we observed transient" "NT rapidly facilitated" "we found that pre-incubation" "in which NTSR1 antagonist" "we found that CRISPR-cKO of Ntsr1" "high editing efficiency" "We found that BLA neurons from both" "However, when the classifier" "We found that control mice preferred" "Finally, we observed predominant" "showed significantly enhanced baseline"; do grep -o "$s[^.]*\." $f | head -1; done
```

```
We recorded a total of 685 BLA neurons from 30 mice while they were performing a discrimination task where three types of trials with distinct auditory tones predicting sucrose, shock, or no outcome (Sucrose, Shock, and Neutral CSs) were randomly presented at a 2:1:1 ratio ( Figure 4b ).
we clustered BLA neurons into seven functional groups based on their responses across all task events using unsupervised hierarchical clustering ( Figure 4d , E8h ) and found that the CRISPR-cKO decreased the proportions of CS-responsive neurons and attenuated the magnitude of neural responses to Sucrose and Shock CSs within each task-relevant cluster, compared to the control group ( Figure 4e , E8i ).
We found that the CRISPR-Cas9 mediated conditional knockout (CRISPR-cKO) of Nt gene in the PVT, but not the MGN nor the vHPC, enhanced tone-sucrose association ( Figure 1g ), but not tone-shock association ( Figure 1h ), implicating the PVT:NT population in reward learning.
Initially, we observed transient decreases in NT sensor responses to both sucrose and airpuff during early acquisition trials, suggesting a pause in basal NT innervation to the BLA.
NT rapidly facilitated glutamatergic transmission onto BLA-NAc neurons and suppressed it onto BLA-CeM neurons in an NTSR1-dependent manner ( Figure E9a – g ), consistent with enhanced reward learning and suppressed punishment learning by optogenetic activation of the PVT-BLA:NT projection.
we found that pre-incubation of NT attenuated the amount of plasticity induced onto BLA-NAc, but not BLA-CeM neurons when using a STDP LTP induction protocol 46 ( Figure E9h – l ).
in which NTSR1 antagonist delivered in the BLA 15 minutes before the conditioning session enhanced reward learning but had no effects on punishment learning ( Figure E10a – f ).
we found that CRISPR-cKO of Ntsr1 gene in the BLA suppressed reward learning ( Figure E10g – p ), consistent with the effects of PVT-BLA Nt CRISPR-cKO on reward learning.
high editing efficiency (~9
[... 5 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000689/10.1038-s41586-022-04964-y.yaml",
 "content": "# Claims for Li, Namburi, Olson et al. (2022), \"Neurotensin orchestrates valence assignment in the\n# amygdala\", Nature 608, 586-592, on dandiset 000689.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC9583860, NIHMS1840566), as served\n# by ncbi_pmc: main text, Materials and Methods (with the \"Additional statistical information\"\n# section giving t, P, effect sizes and 95% CIs per panel), the legends of Figures 1 to 5 and of\n# Extended Data Figures 1 to 10. The version of record was not read. The manuscript lists\n# supplementary files (1840566_SD_Fig_1 to 5, SD_ED_1 to 7, the Reporting Summary); these are source\n# data and were not in the text read. No PDF was available, so figure panels (analysis-window\n# shading, cluster numbering, axis values) could not be looked at; where a claim needs them it is\n# said below.\n#\n# Code read: none. The paper links no code (\"All the custom code used to process data shown in this\n# manuscript is available upon request\"). Every method detail below is from the Methods and legends.\n#\n# Dataset, from its title and description on DANDI (version 0.240530.1923): in vivo\n# electrophysiology recordings in the amygdala, the corresponding behavioral videos during the\n# Pavlovian discrimination task, histology, and \"a second cohort\" with fiber photometry data. Which\n# photometry experiment that cohort is (Figure 3d-f, 3j-l or Extended Data Figure 6) is not said.\n#\n# Data the paper used, as it reports them.\n# In vivo electrophysiology (Figures 4, 5, Extended Data Figure 8). Male mice. PVT-BLA Nt\n# CRISPR-cKO: AAV9-pMeCP2-Cas9 into the PVT; into the BLA a cocktail of AAV5-Ef1a-DIO-ChR2-mCherry\n# with two retrograde AAV Nt guide RNAs (CRISPR group) or one scrambled control guide (control\n# group); Cav2-Cre into the CeA or the NAc on the same side, so that ChR2 tags BLA-CeA or BLA-NAc\n# neurons. A 32-micron nichrome wire optrode with a 200-micron fiber in the BLA; Open Ephys at 30 kHz,\n# 300 Hz to 6 kHz; units sorted in Offline Sorter. 685 BLA neurons from 30 mice; units with baseline\n# rate below 0.3 Hz excluded; only the last day of the discrimination task analysed. Task: after 4\n# days of tone-sucrose (120 trials, 2 or 20 kHz, 60 dB, sucrose 15 ul of 30% delivered 2 s after CS\n# onset, tone up to 20 s ending on port entry), 2 days with a 9 kHz neutral tone, one day of\n# tone-shock conditioning (30 trials, 20 s tone, 2 s 0.4 mA shock at tone offset from trial 21) and\n# one recall day, mice ran the three-cue task: sucrose, neutral and shock CS at 50, 25 and 25%,\n# 120 trials, shock now 100 ms of 0.6 mA, for 4 to 5 days. A phototagging session followed a \"fake\"\n# session with the patch cord disconnected: 1 s constant 473 nm light, 10 s of 1 Hz (5 or 10 ms\n# pulses), 2 s of 10 Hz and 100 ms of 100 Hz (5 ms pulses), at least 5 of each. Videos at 15 frames\n# per second, labelled with DeepLabCut at the head, electrode, right ear, left ear and tail.\n# Freely moving behavior of the PVT-BLA cKO cohort (Figure 2c-d, N=17 CRISPR and 19 control for\n# sucrose, 14 and 14 for freezing) and of PVT-BLA:NT photostimulation (Figure 2g-h, NT::Cre mice,\n# ChR2 N=7, mCherry N=8). Port entries by beam break; freezing scored by hand for Figure 2.\n# Head-fixed photometry (Figure 3, Extended Data Figures 6 and 7). Tone-sucrose over 5 to 7\n# sessions (about 60 pairings, CS 4 s, 1 or 8 kHz, about 4 ul of 30% sucrose 2 s after CS onset);\n# tone-airpuff over 2 sessions (about 30 pairings, CS 4 s, 20 psi airpuff of 100 ms 2 s after CS\n# onset); half the CSs unpaired (not analysed). Licks from an infra-red beam digitized at 40 kHz;\n# eye closure from video. PVT-BLA:NT axon-terminal GCaMP6m in NT::Cre mice, fiber in the BLA\n# (N=13 sucrose, 12 airpuff), on a multi-site camera system with 405 and 470 nm excitation; somatic\n# GCaMP6m in MGN, vHPC and PVT NT neurons (Extended Data Figure 6); GRAB-NTS1.0 NT sensor in the BLA\n# of wild-type mice (N=5), Neurophotometrics V2, 470 and 415 nm at 20 Hz each.\n# Other experiments (anatomy, ex vivo patch clamp, sensor validation in HEK cells and neurons,\n# global Nt cKO and Ntsr1 cKO behavior, NTSR1 antagonist pharmacology) are described in the Methods;\n# the dataset description does not name them.\n#\n# Inconsistencies in the text, recorded here and in the claims concerned. Figure 5a reports t(11)\n# for groups of 12 and 14 leave-one-out iterations, and t = 1.224 with P = 0.0002 for the neutral\n# CS. Figure 5b's legend gives P = 0.2122 for control against CRISPR, its statistics section\n# P = 0.1309. The statistics for Figure 2h are printed under \"2f\". Mouse counts differ between\n# panels from the same cohort (30 mice recorded; 12 and 14 leave-one-out iterations; t(28) with\n# N=15 per group in Figure 5f; t(33) in Extended Data Figure 8e; 36 mice in Figure 2c).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000689\"\npaper: doi:10.1038/s41586-022-04964-y\nclaims:\n- id: fig1c-nt-sources\n  statement: NT neurons projecting to the BLA are found in the medial geniculate nucleus (MGN),\n    the ventral hippocampus (vHPC) and the paraventricular nucleus of the thalamus (PVT).\n  source: Results, NT inputs to the BLA co-release glutamate, paragraph 1; Figure 1a-c\n  quote: We observed that the medial geniculate nucleus (MGN), ventral subiculum and ventral CA1 of\n    the hippocampus (vHPC), and the paraventricular nucleus of the thalamus (PVT) had NT neurons\n    (tdTomato expressing) projecting to the BLA\n- id: ed1c-ntsr1-bla-cem\n  statement: Ntsr1 mRNA is more often colocalized with BLA-CeM projectors than with BLA-NAc\n    projectors, while Ntsr2 mRNA does not differ between them.\n  source: Extended Data Figure 1c and 1f\n  quote: Ntsr1 mRNA was predominantly expressed in BLA-CeM neurons compared to BLA-NAc neurons\n  statistics:\n  - about: Ntsr1, colocalization as a fraction of tracer-labelled cells\n    test: unpaired t-test\n    statistic: t(5) = 7.901\n    p: 0.0005\n    ci: {level: 0.95, low: 0.1737, high: 0.3412}\n  - about: Ntsr1, colocalization as a fraction of Ntsr1-positive cells\n    test: unpaired t-test\n    statistic: t(5) = 6.383\n    p: 0.0014\n    ci: {level: 0.95, low: 0.2613, high: 0.6137}\n  - about: Ntsr2, BLA-CeA against BLA-NAc\n    test: unpaired t-test, two-tailed\n    statistic: t(5) = 0.3729\n    p: 0.7245\n    ci: {level: 0.95, low: -0.1202, high: 0.08974}\n- id: ed2-glutamate-corelease\n  statement: Light-evoked EPSCs in BLA neurons from MGN:NT, vHPC:NT and PVT:NT axon terminals\n    persist in TTX and 4-AP (monosynaptic) and are reduced by AMPA and NMDA receptor blockers,\n    while IPSCs are abolished by TTX and 4-AP.\n  source: Results, NT inputs to the BLA co-release glutamate, paragraph 1; Extended Data Figure 2d-e\n  quote: the EPSCs evoked in BLA neurons by stimulating ChR2-expressing axon terminals from all\n    three NT populations were monosynaptic and can be blocked by antagonizing the AMPA and NMDA\n    glutamate receptors ( Figure E2d ), whereas the IPSCs were not\n  statistics:\n  - about: MGN, TTX+4-AP against AP5+NBQX\n    test: one-way ANOVA with Holm-Sidak's multiple comparisons\n    statistic: t(27) = 3.19\n    p: 0.0072\n  - about: PVT, TTX+4-AP against AP5+NBQX\n    test: one-way ANOVA with Holm-Sidak's multiple comparisons\n    statistic: t(39) = 4.585\n    p: 0.0001\n    p_relation: \"<\"\n  - about: vHPC, TTX+4-AP against AP5+NBQX\n    test: one-way ANOVA with Holm-Sidak's multiple comparisons\n    statistic: t(26) = 28.03\n    p: 0.0188\n- id: ed3-editing-efficiency\n  statement: The two Nt guide RNAs with Cas9 produce indel mutations in about 90% of sequenced\n    reads in vivo (90.8% for guide 1 and 80.3% for guide 2 above control tissue).\n  source: Results, Global Nt gene knockout in the PVT promotes reward learning, paragraph 1;\n    Extended Data Figure 3a and 3c\n  quote: We verified that our guide RNAs (guide RNA 1 and guide RNA 2) had high editing efficiency\n    (~90 %) in vivo\n  statistics:\n  - about: guide 1 against control\n    test: unpaired t-test, two-tailed\n    statistic: t(8) = 85.99\n    p: 0.0001\n    p_relation: \"<\"\n    ci: {level: 0.95, low: 88.38, high: 93.25}\n  - about: guide 2 against control\n    test: unpaired t-test, two-tailed\n    statistic: t(7) = 21.20\n    p: 0.0001\n    p_relation: \"<\"\n    ci: {level: 0.95, low: 71.32, high: 89.23}\n  expected:\n  - quantity: indel percentage, guide 1 minus control\n    value: 90.82\n    tolerance: 2.44\n    unit: percent\n  - quantity: indel percentage, guide 2 minus control\n    value: 80.27\n    tolerance: 8.96\n    unit: percent\n- id: ed5f-pvt-bla-cko-validation\n  statement: The PVT-BLA Nt CRISPR-cKO reduces Nt mRNA in guide-positive PVT cells without\n    changing Vglut2 mRNA.\n  source: Extended Data Figure 5f\n  quote: Mice receiving Nt guides injections (CRISPR group) showed significantly reduced Nt mRNA\n    levels in the guide-positive cells compared to mice receiving control guide injections, while\n    Vglut2 mRNA levels were unaffected\n  statistics:\n  - about: Nt mRNA\n    test: unpaired t-test\n    statistic: t(28) = 2.788\n    p: 0.009\n    ci: {level: 0.95, low: -2.18, high: -0.3335}\n  - about: Vglut2 mRNA\n    test: unpaired t-test\n    statistic: t(12) = 0.724\n    p: 0.483\n    ci: {level: 0.95, low: -0.3528, high: 0.7039}\n- id: fig1g-pvt-global-cko-reward\n  statement: Global Nt CRISPR-cKO in the PVT, but not in the MGN or vHPC, increases port entry\n    probability in the last tone-sucrose session.\n  source: Results, Global Nt gene knockout in the PVT promotes reward learning, paragraph 2; Figure\n    1g\n  quote: We found that the CRISPR-Cas9 mediated conditional knockout (CRISPR-cKO) of Nt gene in the\n    PVT, but not the MGN nor the vHPC, enhanced tone-sucrose association\n  statistics:\n  - about: PVT, CRISPR against control\n    test: unpaired t-test, two-tailed\n    statistic: t(26) = 2.611\n    p: 0.0148\n    ci: {level: 0.95, low: 4.363, high: 36.67}\n    n: 15 CRISPR and 13 control mice\n  - about: MGN, CRISPR against control\n    test: unpaired t-test, two-tailed\n    statistic: t(33) = 0.1019\n    p: 0.9195\n    ci: {level: 0.95, low: -16.10, high: 17.80}\n    n: 18 CRISPR and 17 control mice\n  - about: vHPC, CRISPR against control\n    test: unpaired t-test, two-tailed\n    statistic: t(18) = 0.8666\n    p: 0.3976\n    ci: {level: 0.95, low: -9.054, high: 21.77}\n    n: 11 CRISPR and 9 control mice\n  criterion: Port entry probability from the last of 4 days, computed across all trials with 500\n    ms bins for 25 s around CS onset and z-transformed against the 25 s before CS onset (Methods,\n    Pavlovian sucrose association, Data analysis). The analysis window is the shaded region of\n    Figure 1g, which the text does not give; readings are (a) the CS period up to 10 s after\n    onset (the CS lasts up to 10 s in this experiment) and (b) 0 to 25 s after onset. Reproduced\n    when, under every reading, the PVT comparison has p < 0.05 with CRISPR higher and the MGN and\n    vHPC comparisons have p >= 0.05 (two-tailed unpaired t-test, as the legend states).\n- id: fig1h-global-cko-no-shock-effect\n  statement: Global Nt CRISPR-cKO in the MGN, vHPC or PVT does not change freezing in the second\n    session of tone-shock conditioning.\n  source: Figure 1h\n  quote: CRISPR-cKO in none of the regions affected tone-shock acquisition in second session of\n    tone-shock conditioning\n  statistics:\n  - about: MGN\n    test: unpaired t-test, two-tailed\n    statistic: t(24) = 0.8346\n    p: 0.4122\n    ci: {level: 0.95, low: -0.2184, high: 0.09263}\n  - about: vHPC\n    test: unpaired t-test, two-tailed\n    statistic: t(15) = 0.2820\n    p: 0.7818\n    ci: {level: 0.95, low: -0.1962, high: 0.2561}\n  - about: PVT\n    test: unpaired t-test, two-tailed\n    statistic: t(14) = 0.5740\n    p: 0.5751\n    ci: {level: 0.95, low: -0.1585, high: 0.2743}\n  criterion: A claim of absence, judged on the paper's test, a two-tailed unpaired t-test of\n    percent time freezing during the CS, CRISPR against control, per region. Reproduced when none\n    of the three has p < 0.05; the effect sizes are reported either way.\n- id: fig2c-pvt-bla-cko-reduces-reward\n  statement: PVT-BLA projection-specific Nt CRISPR-cKO reduces port entry probability to the\n    sucrose-predictive CS relative to scrambled-guide controls.\n  source: Results, PVT-BLA:NT neurons are a functionally-distinct PVT population, paragraph 1;\n    Figure 2c\n  quote: The CRISPR group showed significantly reduced port entry probability in response to the\n    sucrose-predictive CS\n  statistics:\n  - test: unpaired t-test, two-tailed\n    statistic: t(34) = 2.988\n    p: 0.0052\n    ci: {level: 0.95, low: -1.073, high: -0.2042}\n    n: 17 CRISPR and 19 control mice\n  expected:\n  - quantity: CRISPR minus control port entry measure\n    value: -0.6385\n    tolerance: 0.4344\n  criterion: Port entry probability with 500 ms bins over 25 s before and after CS onset,\n    z-transformed against the 25 s baseline (Methods, Pavlovian sucrose association, Data\n    analysis). Open details the text does not fix, each run. Session, (a) the last of the 4\n    tone-sucrose days (Methods say results are from the last conditioning day for the other\n    sucrose experiments), (b) sucrose trials of the last discrimination-task day. Window (the\n    shaded region of Figure 2c, not legible without the figure), (i) CS onset to 20 s, (ii) 0 to\n    2 s before sucrose delivery, (iii) 0 to 25 s. Measure, the z-score (the effect size near -0.64\n    fits a z-score) and the raw probability as a variant. Reproduced when the two-tailed unpaired\n    t-test gives p < 0.05 with CRISPR lower under every reading of window for some session\n    reading; methods_underspecified when readings disagree.\n- id: fig2d-pvt-bla-cko-increases-freezing\n  statement: PVT-BLA Nt CRISPR-cKO increases freezing to the shock-predictive CS in the tone-shock\n    test session.\n  source: Figure 2d\n  quote: The CRISPR group also showed significantly higher proportion of time spent freezing during\n    the duration of shock-predictive CS in the tone-shock testing session\n  statistics:\n  - test: unpaired t-test, two-tailed\n    statistic: t(26) = 2.167\n    p: 0.0396\n    ci: {level: 0.95, low: 0.01324, high: 0.5002}\n    n: 14 CRISPR and 14 control mice\n  expected:\n    quantity: CRISPR minus control fraction of CS time freezing\n    value: 0.2567\n    tolerance: 0.2435\n  criterion: The paper's freezing for Figure 2 was scored by hand by two people and averaged, so it\n    cannot be recomputed as such. The Methods' automated rule (velocity below 0.3 cm/s from the\n    tracked video, Measurement of fear behavior) is the reading run here, over the 20 s CS of each\n    trial of the recall session. Reproduced when a two-tailed unpaired t-test gives p < 0.05 with\n    CRISPR higher; the substitution of the automated rule for hand scoring is a deviation.\n- id: fig2g-photostim-enhances-reward\n  statement: Photostimulating PVT:NT terminals in the BLA during the tones increases port entry\n    probability to the sucrose-predictive CS relative to mCherry controls.\n  source: Figure 2g\n  quote: The ChR2 group showed significantly enhanced port entry probability in response to\n    sucrose-predictive CS\n  statistics:\n  - test: unpaired t-test, two-tailed\n    statistic: t(13) = 2.706\n    p: 0.018\n    ci: {level: 0.95, low: 0.2156, high: 1.921}\n    n: 7 ChR2 and 8 mCherry mice\n- id: fig2h-photostim-reduces-freezing\n  statement: Photostimulating PVT:NT terminals in the BLA during conditioning reduces freezing to\n    the shock-predictive CS in the tone-shock test session.\n  source: Figure 2h (its statistics are printed under \"2f\" in Methods, Additional statistical\n    information)\n  quote: The ChR2 group showed significantly reduced freezing in the tone-shock testing session\n    during the presentation of shock-predictive CS compared to the control group\n  statistics:\n  - test: unpaired t-test, two-tailed\n    statistic: t(13) = 2.474\n    p: 0.0279\n    ci: {level: 0.95, low: -0.546, high: -0.03698}\n    n: 7 ChR2 and 8 mCherry mice\n- id: fig3bc-head-fixed-learning\n  statement: Head-fixed mice acquire the tasks, with more anticipatory licks to the sucrose tone and\n    more anticipatory eye closure to the airpuff tone in the last session than in the first.\n  source: Figure 3b and 3c\n  quote: averaged anticipatory licks to the sucrose tone for the first 16 trials of first and last\n    tone-sucrose sessions\n  statistics:\n  - about: anticipatory licks, last against first session\n    test: paired t-test, two-tailed\n    statistic: t(12) = 6.497\n    p: 0.0001\n    p_relation: \"<\"\n    ci: {level: 0.95, low: 1.210, high: 2.431}\n    n: 13 mice\n  - about: anticipatory eye closure, last against first session\n    test: paired t-test, two-tailed\n    statistic: t(11) = 2.48\n    p: 0.0306\n    ci: {level: 0.95, low: 0.4852, high: 8.136}\n    n: 12 mice\n  criterion: Per mouse, the mean over the first 16 trials of the first and of the last session of\n    the anticipatory licks (lick count from CS onset to US onset, Methods, Measurement of\n    tone-sucrose association) and of the eye-closure area from CS onset to US onset (Measurement of\n    tone-air puff association). Reproduced when both two-tailed paired t-tests give p < 0.05 with\n    the last session higher.\n- id: fig3e-terminal-sucrose-increase\n  statement: PVT-BLA:NT axon-terminal calcium responses to sucrose delivery increase after\n    tone-sucrose learning, while the CS response does not change significantly.\n  source: Results, PVT-BLA:NT neurons are a functionally-distinct PVT population, paragraph 3;\n    Figure 3e\n  quote: Calcium responses of the PVT-BLA:NT axon terminals to sucrose were significantly enhanced\n    by reward conditioning\n  statistics:\n  - about: US window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(12) = 2.935\n    p: 0.0125\n    ci: {level: 0.95, low: 3.635, high: 24.60}\n    n: 13 mice\n  - about: CS window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(12) = 1.474\n    p: 0.1663\n    ci: {level: 0.95, low: -1.860, high: 9.633}\n    n: 13 mice\n  depends_on:\n  - fig3bc-head-fixed-learning\n  criterion: Photometry processed as the Methods (Fiber photometry, Data analysis) give it, both\n    channels down-sampled to 5 Hz and median-filtered over 200 ms, the reference regressed from the\n    470 nm channel with coefficients fit on the trial average from -5 to 0 s before CS onset, the\n    residuals z-scored against -5 to 0 s. Windows 0 to 2 s (CS) and 2 to 7 s (US) from CS onset\n    (Figure 3 legend). Open details, each run. Early and late, (a) first 16 trials of the first and\n    last sessions, as in Figure 3b, (b) all trials of the first and last sessions. Measure, (i)\n    area under the z-scored trace in the window, (ii) mean z-score in the window. Reproduced when\n    the US comparison has p < 0.05 with late higher under every reading (two-tailed paired t-test);\n    the CS result is reported.\n- id: fig3f-terminal-airpuff-decrease\n  statement: PVT-BLA:NT axon-terminal calcium responses to airpuff decrease after tone-airpuff\n    learning.\n  source: Figure 3f\n  quote: Responses to airpuff were significantly suppressed by punishment conditioning\n  statistics:\n  - about: US window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(11) = 2.896\n    p: 0.0145\n    ci: {level: 0.95, low: -12.46, high: -1.700}\n    n: 12 mice\n  - about: CS window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(11) = 1.472\n    p: 0.169\n    ci: {level: 0.95, low: -5.280, high: 1.047}\n    n: 12 mice\n  depends_on:\n  - fig3bc-head-fixed-learning\n  criterion: As fig3e-terminal-sucrose-increase, for the airpuff sessions (2 sessions, so first and\n    last are sessions 1 and 2). Reproduced when the US comparison has p < 0.05 with late lower under\n    every reading.\n- id: ed6-somatic-no-change\n  statement: Somatic calcium responses of MGN, vHPC and PVT NT neurons from CS to US onset do not\n    change between early and late acquisition of either task.\n  source: Results, PVT-BLA:NT neurons are a functionally-distinct PVT population, paragraph 3;\n    Extended Data Figure 6b-c\n  quote: while somatic calcium responses of the NT three sources including PVT:NT had no\n    learning-induced changes\n  statistics:\n  - about: PVT, tone-sucrose\n    test: paired t-test, two-tailed\n    statistic: t(7) = 1.76\n    p: 0.1218\n    ci: {level: 0.95, low: -10.65, high: 1.56}\n  - about: PVT, tone-airpuff\n    test: paired t-test, two-tailed\n    statistic: t(7) = 0.5676\n    p: 0.588\n    ci: {level: 0.95, low: -4.608, high: 7.519}\n  - about: MGN, tone-sucrose\n    test: paired t-test, two-tailed\n    statistic: t(8) = 0.3214\n    p: 0.7561\n  - about: vHPC, tone-sucrose\n    test: paired t-test, two-tailed\n    statistic: t(7) = 1.615\n    p: 0.1504\n  criterion: A claim of absence, judged on the paper's test, a two-tailed paired t-test of the area\n    under the z-scored curve from CS onset to US onset (Extended Data Figure 6 legend), early\n    against late acquisition, per region and task. Reproduced when none of the six tests has p <\n    0.05. Early and late are not defined; readings as in fig3e-terminal-sucrose-increase.\n- id: fig3h-sensor-specificity\n  statement: The GRAB-NTS1.0 sensor responds to NT and not to 13 other transmitters and\n    neuropeptides in cultured neurons.\n  source: Results, Genetically-encoded fluorescent NT sensor, paragraph 1; Figure 3h\n  quote: validated the sensor to show high sensitivity and specificity for NT\n  statistics:\n  - test: one-way ANOVA with Dunnett's multiple comparisons test\n    statistic: F(13, 28) = 1059\n    p: 0.0001\n    p_relation: \"<\"\n    n: 3 coverslips per compound\n- id: fig3k-nt-sensor-sucrose-increase\n  statement: The BLA NT sensor response to sucrose delivery increases after reward learning.\n  source: Results, Genetically-encoded fluorescent NT sensor, paragraph 1; Figure 3k\n  quote: After learning, we observed an increased NT sensor response to sucrose\n  statistics:\n  - about: US window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(4) = 8.709\n    p: 0.001\n    ci: {level: 0.95, low: 2.744, high: 5.538}\n    n: 5 mice\n  - about: CS window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(4) = 1.788\n    p: 0.1483\n    ci: {level: 0.95, low: -1.523, high: 7.031}\n    n: 5 mice\n  criterion: As fig3e-terminal-sucrose-increase (same processing, with 415 nm as the reference\n    channel and continuous recording; windows 0 to 2 s and 2 to 7 s from CS onset as the Figure 3\n    legend states for these panels). Reproduced when the US comparison has p < 0.05 with late\n    higher under every reading.\n- id: fig3l-nt-sensor-airpuff-decrease\n  statement: The BLA NT sensor response to airpuff decreases after punishment learning.\n  source: Results, Genetically-encoded fluorescent NT sensor, paragraph 1; Figure 3l\n  quote: and a decreased NT sensor response to airpuff\n  statistics:\n  - about: US window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(4) = 3.996\n    p: 0.0162\n    ci: {level: 0.95, low: -6.083, high: -0.9583}\n    n: 5 mice\n  - about: CS window, late against early\n    test: paired t-test, two-tailed\n    statistic: t(4) = 2.137\n    p: 0.0994\n    ci: {level: 0.95, low: -2.585, high: 0.3570}\n    n: 5 mice\n  criterion: As fig3k-nt-sensor-sucrose-increase, for the airpuff sessions. Reproduced when the US\n    comparison has p < 0.05 with late lower under every reading.\n- id: fig3-nt-sensor-early-dip\n  statement: Early in acquisition, the BLA NT sensor signal transiently decreases after both\n    sucrose and airpuff.\n  source: Results, Genetically-encoded fluorescent NT sensor, paragraph 1\n  quote: Initially, we observed transient decreases in NT sensor responses to both sucrose and\n    airpuff during early acquisition trials\n  criterion: The paper reports no test. With the processing and early-trial readings of\n    fig3k-nt-sensor-sucrose-increase, reproduced when the mean z-scored signal over mice in the US\n    window (2 to 7 s from CS onset) is below zero in early trials for both sucrose and airpuff.\n- id: fig4-recording-count\n  statement: 685 BLA neurons were recorded from 30 mice during the three-cue discrimination task,\n    with sucrose, shock and neutral CSs at a 2 to 1 to 1 ratio.\n  source: Results, NT inputs from the PVT amplify BLA representation of learned valences,\n    paragraph 1; Figure 4b\n  quote: We recorded a total of 685 BLA neurons from 30 mice while they were performing a\n    discrimination task\n  expected:\n  - quantity: BLA neurons\n    value: 685\n    tolerance: 68.5\n  - quantity: mice\n    value: 30\n    tolerance: 3\n  criterion: Units from the last discrimination-task session of each mouse, with baseline firing\n    of at least 0.3 Hz (Methods, Analysis for in vivo recordings). Whether 685 is counted before or\n    after that exclusion is not said; both counts are shown and either may match. The degrees of\n    freedom of Extended Data Figure 8d imply 613 untagged, 39 BLA-NAc and 32 BLA-CeA neurons\n    (684 in total, with one BLA-CeA neuron excluded elsewhere); these counts are reported.\n- id: ed8d-reduced-basal-firing\n  statement: In the CRISPR group, untagged BLA neurons and BLA-CeA neurons have lower basal firing\n    rates than in controls, while BLA-NAc neurons do not differ.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Extended Data\n    Figure 8d\n  quote: Both non-tagged BLA neurons and the BLA-CeA neurons showed significantly lower basal\n    firing rates (in Hz) in the CRISPR group compared to the control group\n  statistics:\n  - about: untagged neurons\n    test: unpaired t-test, two-tailed\n    statistic: t(611) = 3.132\n    p: 0.0018\n    ci: {level: 0.95, low: -2.108, high: -0.4834}\n  - about: BLA-CeA neurons\n    test: unpaired t-test, two-tailed\n    statistic: t(30) = 2.429\n    p: 0.021\n    ci: {level: 0.95, low: -6.961, high: -0.6071}\n  - about: BLA-NAc neurons\n    test: unpaired t-test, two-tailed\n    statistic: t(37) = 0.4665\n    p: 0.6436\n    ci: {level: 0.95, low: -6.226, high: 3.896}\n  depends_on:\n  - fig4c-photoidentification\n  criterion: Basal rate per unit, as mean firing rate in a baseline period the text does not\n    define; readings (a) the 1 s before each CS onset averaged over all trials (the PSTH baseline\n    of the Methods), (b) the whole session. Reproduced when, under every reading, untagged and\n    BLA-CeA neurons have p < 0.05 with CRISPR lower and BLA-NAc has p >= 0.05 (two-tailed unpaired\n    t-test across neurons).\n- id: fig4c-photoidentification\n  statement: BLA-NAc and BLA-CeA neurons are identified by short-latency responses to light at the\n    end of each session.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Figure 4c\n  quote: At the end of each session, we optogenetically photoidentified BLA-NAc and BLA-CeA neurons\n    based on previously reported photoresponse latencies\n  criterion: The Methods' rule (Analysis for in vivo recordings). PSTHs of 1 ms bins 50 ms around\n    light onset, z-scored against the 50 ms before it; a unit is photo-responsive when it has a\n    significant excitation (z above 1.98) within 6 ms of onset, no significant response 7 to 50\n    ms after onset with a 6 ms moving average, and no significant response in the fake session.\n    Its projection (BLA-NAc or BLA-CeA) is that of the mouse's Cav2-Cre injection. Which light\n    pulses enter the PSTH is not fixed; readings are (a) all pulse onsets of the 1, 10 and 100 Hz\n    trains and the onset of the 1 s light, (b) the 1 Hz pulses only. When the dataset holds the\n    authors' tag labels they are used and the recomputed labels are compared with them. Reproduced\n    when the identified counts are within 10% of 39 BLA-NAc and 32 BLA-CeA neurons (counts read\n    from the degrees of freedom of Extended Data Figure 8d and 8j) under one reading.\n- id: ed8fg-fewer-responsive-neurons\n  statement: The CRISPR group has smaller proportions of neurons excited or inhibited by each of\n    the three CSs, but the response magnitude of the responsive neurons does not differ from\n    controls.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Extended Data\n    Figure 8f-g\n  quote: CRISPR mice showed overall reduced proportions, but not responsive amplitudes of excited\n    and inhibited neurons to all three cues relative to the control group\n  criterion: PSTHs of 20 ms bins for 1 s before and after CS onset, z-scored against the 1 s\n    before onset; a response is significant at a z-score of plus or minus 1.98 (Methods). How the\n    threshold is applied is not fixed; readings are (a) the mean z-score over 0 to 1 s, (b) any\n    20 ms bin in 0 to 1 s. The paper gives no test for the proportions; reproduced when, under\n    every reading, the CRISPR proportion of excited and of inhibited neurons is lower for all three\n    CSs, and the amplitude comparison (two-tailed unpaired t-test, the paper's default) finds no\n    difference at p < 0.05 for any of the six cue and direction groups.\n- id: fig4d-seven-clusters\n  statement: Unsupervised hierarchical clustering of BLA responses to the sucrose, neutral and\n    shock CSs gives seven functional clusters.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Figure 4d\n  quote: we clustered BLA neurons into seven functional groups based on their responses across all\n    task events using unsupervised hierarchical clustering\n  expected:\n    quantity: number of clusters\n    value: 7\n    tolerance: 0\n  criterion: As the Methods give it (Functional hierarchical clustering). Per neuron, 20 ms PSTHs\n    from 1 s before to 1 s after CS onset, z-scored with the mean and SD of the 1 s baseline,\n    smoothed in time with a Gaussian-weighted moving average of smoothing factor 0.85 (MATLAB\n    smoothdata), the sucrose, neutral and shock CS traces concatenated; all neurons of both groups\n    clustered together. Ward linkage with correlation distance; cut at 35% of the maximum linkage\n    distance. Ward on a correlation distance is not standard, so the readings are (a) Ward linkage\n    on the correlation distance matrix, (b) Ward linkage with Euclidean distance on rows centred\n    and scaled to unit norm (equivalent to correlation). Reproduced when one reading gives seven\n    clusters.\n- id: fig4e-cluster-responses-attenuated\n  statement: Within the task-relevant clusters, the CRISPR group has smaller responses to the\n    sucrose and shock CSs than controls, while neutral-CS responses are largely unchanged.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Figure 4e\n  quote: the CRISPR-cKO decreased the proportions of CS-responsive neurons and attenuated the\n    magnitude of neural responses to Sucrose and Shock CSs within each task-relevant cluster\n  statistics:\n  - about: cluster 1, sucrose CS\n    test: unpaired t-test, two-tailed\n    statistic: t(78) = 2.203\n    p: 0.0303\n  - about: cluster 2, shock CS\n    test: unpaired t-test, two-tailed\n    statistic: t(73) = 2.365\n    p: 0.02\n  - about: cluster 3, sucrose CS\n    test: unpaired t-test, two-tailed\n    statistic: t(50) = 2.071\n    p: 0.0435\n  - about: cluster 3, shock CS\n    test: unpaired t-test, two-tailed\n    statistic: t(50) = 2.076\n    p: 0.043\n  - about: cluster 4, sucrose CS\n    test: unpaired t-test, two-tailed\n    statistic: t(52) = 2.219\n    p: 0.031\n  - about: cluster 4, shock CS\n    test: unpaired t-test, two-tailed\n    statistic: t(52) = 2.225\n    p: 0.03\n  - about: cluster 6, shock CS\n    test: unpaired t-test, two-tailed\n    statistic: t(140) = 2.228\n    p: 0.0276\n  - about: cluster 7, neutral CS\n    test: unpaired t-test, two-tailed\n    statistic: t(167) = 2.924\n    p: 0.003\n  depends_on:\n  - fig4d-seven-clusters\n  criterion: Clusters from fig4d-seven-clusters. Per neuron the response is the mean z-score in a\n    window after CS onset; the window is the shaded region of Figure 4e, not given in the text,\n    and the readings are (a) 0 to 1 s, (b) 0 to 0.5 s. Per cluster and CS, a two-tailed unpaired\n    t-test of CRISPR against control neurons. The paper's cluster numbering cannot be recovered\n    from the text, so clusters are judged as a set. The paper found 7 of the 14 sucrose and shock\n    tests significant, each with a smaller absolute response in CRISPR, and 1 of 7 neutral tests.\n    Reproduced when, under every reading, at least 5 of 14 sucrose and shock tests have p < 0.05\n    with a smaller absolute response in CRISPR and at most 2 of 7 neutral tests do; partially\n    reproduced when 3 or 4 do.\n- id: fig4fg-projector-sucrose-responses\n  statement: In controls BLA-NAc neurons are excited and BLA-CeA neurons inhibited by the sucrose\n    CS; the CRISPR-cKO removes the BLA-NAc excitation and the BLA-CeA inhibition.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Figure 4f-g;\n    Extended Data Figure 8j\n  quote: BLA-NAc and BLA-CeA population in the CRISPR group showed significantly reduced excitation\n    and inhibition to the sucrose CS compared to the control group, respectively\n  statistics:\n  - about: BLA-NAc, sucrose CS, CRISPR against control\n    test: unpaired t-test, two-tailed\n    statistic: t(37) = 2.06\n    p: 0.0465\n    ci: {level: 0.95, low: -4.596, high: -0.0376}\n  - about: BLA-CeA, sucrose CS, CRISPR against control\n    test: unpaired t-test, two-tailed\n    statistic: t(30) = 2.06\n    p: 0.0481\n    ci: {level: 0.95, low: 0.0009, high: 2.042}\n  - about: BLA-NAc, Extended Data Figure 8j\n    test: unpaired t-test, two-tailed\n    statistic: t(37) = 2.043\n    p: 0.0483\n    ci: {level: 0.95, low: -3.209, high: -0.01291}\n  - about: BLA-CeA, Extended Data Figure 8j\n    test: unpaired t-test, two-tailed\n    statistic: t(30) = 2.46\n    p: 0.0199\n    ci: {level: 0.95, low: 0.453, high: 4.882}\n  depends_on:\n  - fig4c-photoidentification\n  criterion: Response per neuron as in fig4e-cluster-responses-attenuated (z-scored 20 ms PSTH,\n    windows (a) 0 to 1 s, (b) 0 to 0.5 s). Extended Data Figure 8j measures a \"valence encoding\n    pattern\" the text does not define; its tests are recorded but not run. Reproduced when, under\n    every reading, the BLA-NAc sucrose response is lower and the BLA-CeA sucrose response higher\n    (less negative) in CRISPR than in control, each with p < 0.05 by a two-tailed unpaired\n    t-test, and the control BLA-NAc mean is above zero and the control BLA-CeA mean below zero.\n    The neutral and shock CS comparisons are reported.\n- id: fig4fg-control-projector-valence\n  statement: In control mice BLA-NAc neurons are predominantly excited by the sucrose CS and BLA-CeA\n    neurons by the shock CS.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 1; Figure 4f-g\n  quote: we replicated our previous reports in control mice showing that BLA-NAc and BLA-CeA\n    neurons are predominantly excited by Sucrose CS and Shock CS, respectively\n  depends_on:\n  - fig4c-photoidentification\n  criterion: The paper reports no test. Control mice only, responses as in\n    fig4fg-projector-sucrose-responses. \"Predominantly excited\" is read as (a) the population mean\n    response to that CS is positive and larger than to the other CS, (b) the proportion of neurons\n    significantly excited (z above 1.98, as in ed8fg-fewer-responsive-neurons) is larger for that\n    CS than for the other. Reproduced when both hold for both populations under every reading.\n- id: fig5a-trajectories-reduced\n  statement: Population trajectories of the CRISPR group are shorter for all three CSs, and the\n    distance between sucrose and shock trajectories is smaller, than in controls.\n  source: Results, NT inputs from the PVT amplify BLA representation, paragraph 2; Figure 5a\n  quote: trajectories in the CRISPR group showed significant decreases in total trajectory length\n    and trajectory distance between sucrose and shock trials compared to the controls\n  statistics:\n  - about: trajectory length, sucrose CS\n    test: unpaired t-test, two-tailed\n    statistic: t(11) = 4.786\n    p: 0.0001\n    p_relation: \"<\"\n    ci: {level: 0.95, low: -9.963, high: -4.284}\n    n: 12 control and 14 CRISPR leave-one-mouse-out iterations\n  - about: trajectory length, neutral CS (printed t = 1.224 with P = 0.0002)\n    test: unpaired t-test, two-tailed\n    statistic: t(11) = 1.224\n    p: 0.0002\n    ci: {level: 0.95, low: -10.37, high: -3.736}\n    n: 12 control and 14 CRISPR leave-one-mouse-out iterations\n  - about: trajectory length, shock CS\n    test: unpaired t-test, two-tailed\n    statistic: t(11) = 14.99\n    p: 0.0001\n    p_relation: \"<\"\n    ci: {level: 0.95, low: -13.15, high: -7.113}\n    n: 12 control and 14 CRISPR leave-one-mouse-out iterations\n  criterion: As the Methods give it (Neural trajectory analysis). Per neuron, mean firing rates in\n    20 ms bins from -1 to 1 s around each CS onset (raw rates, as the legend says). Control neurons\n    randomly subsampled to the number of CRISPR neurons. One PCA for both groups, with the same\n    coefficients for every projection. The text does not say how a single PCA spans two sets of\n    neurons; readings are (a) the two groups' neuron-by-time matrices, of equal neuron count, are\n    stacked along time, so each component weights neuron slots shared by the groups (the reading\n    that lets the same coefficients serve both groups and the cross-group decoder of Figure 5b-c),\n    (b) all neurons of both groups are variables and each group's trajectory uses its own\n    neurons with the other group's entries set to zero. Components explaining 95% of variance;\n    length as the sum of Euclidean distances between adjacent bins; distance between the sucrose\n    and shock trajectories as the bin-by-bin Euclidean distance summed over bins (a mean gives the\n    same comparison). Statistics over leave-one-mouse-out iterations with the PCA coefficients\n    fixed, two-tailed unpaired t-test. The random subsample and the neuron pairing are not fixed\n    and could change the outcome, so each reading is run over 20 random subsamples and the\n    fraction of them reaching p < 0.05 reported. Reproduced when, under every reading, the median\n    subsample gives a shorter CRISPR length for all three CSs and a smaller CRISPR sucrose to shock\n    distance, each with p < 0.05.\n- id: fig5b-within-group-decoding\n  statement: A linear SVM decodes sucrose against shock trials from BLA population activity above\n    label-shuffled chance in both control and CRISPR groups, with no significant difference\n    between the groups.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 2; Figure 5b\n  quote: We found that BLA neurons from both control and CRISPR groups could decode the trial type\n    compared to label-shuffled trials, when the SVM classifier was trained and tested within-group\n  statistics:\n  - about: ANOVA over the four conditions\n    test: one-way ANOVA with Holm-Sidak's multiple comparisons test\n    statistic: F(3, 16) = 668.6\n    p: 0.0001\n    p_relation: \"<\"\n  - about: control against control shuffled\n    test: Holm-Sidak's multiple comparisons\n    statistic: t(16) = 33.45\n    p: 0.0001\n    p_relation: \"<\"\n  - about: CRISPR against CRISPR shuffled\n    test: Holm-Sidak's multiple comparisons\n    statistic: t(16) = 29.78\n    p: 0.0001\n    p_relation: \"<\"\n  - about: control against CRISPR (statistics section; the legend gives P = 0.2122)\n    test: Holm-Sidak's multiple comparisons\n    statistic: t(16) = 1.592\n    p: 0.1309\n  expected:\n    quantity: AUC, within-group minus shuffled\n    value: 0.5025\n    tolerance: 0.05\n  depends_on:\n  - fig5a-trajectories-reduced\n  criterion: As the Methods give it (Support Vector Machine classifier). Single-trial activity\n    projected on the global PCA coefficients of fig5a-trajectories-reduced, first 10 PCs as\n    features, linear SVM, 5-fold cross-validation (80% train, 20% test), sucrose trials subsampled\n    to the shock count 50 times per fold, AUC of the ROC; the same with training labels shuffled.\n    Open details, each run. The neurons were not recorded together, so a single \"trial\" of the\n    population is a pseudo-trial; readings are (a) trial k of a type for every neuron, up to the\n    smallest trial count, (b) one trial drawn at random per neuron for each pseudo-trial. Time,\n    (i) features from activity averaged over 0 to 1 s after CS onset (the legend's \"averaged\n    neural activity of each trial\"), (ii) AUC per 20 ms bin, averaged over 0 to 1 s (the Methods'\n    \"as a function of time\"). Statistics on the 5 fold AUCs by one-way ANOVA with Holm-Sidak\n    comparisons. Reproduced when, under every reading, both within-group AUCs exceed their\n    shuffled AUCs at p < 0.05 and control against CRISPR has p >= 0.05.\n- id: fig5c-cross-group-decoding\n  statement: A decoder trained on CRISPR data decodes control data, but a decoder trained on control\n    data performs significantly worse on CRISPR data.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 2; Figure 5c\n  quote: SVM decoder performance significantly dropped when the model was trained on the control\n    data and tested on the CRISPR data, compared to trained on the CRISPR data and tested on the\n    control data\n  statistics:\n  - about: ANOVA over the conditions\n    test: one-way ANOVA with Holm-Sidak's multiple comparisons test\n    statistic: F(3, 16) = 34196\n    p: 0.0001\n    p_relation: \"<\"\n  - about: trained on CRISPR tested on control, against trained on control tested on CRISPR\n    test: Holm-Sidak's multiple comparisons\n    statistic: t(16) = 181.0\n    p: 0.0001\n    p_relation: \"<\"\n  - about: trained on control tested on CRISPR, against shuffled\n    test: Holm-Sidak's multiple comparisons\n    statistic: t(16) = 277.1\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: AUC, trained on CRISPR tested on control minus trained on control tested on CRISPR\n    value: 0.3114\n    tolerance: 0.031\n  depends_on:\n  - fig5b-within-group-decoding\n  criterion: As fig5b-within-group-decoding, training on one group's pseudo-trials and testing on\n    the other's, in the shared PC space of reading (a) of fig5a-trajectories-reduced (reading (b)\n    gives disjoint features for the two groups, so cross-group decoding is run under (a) only).\n    Reproduced when, under every remaining reading, trained-on-CRISPR AUC exceeds trained-on-control\n    AUC at p < 0.05 and both exceed shuffled.\n- id: ed8e-port-and-freezing\n  statement: CRISPR mice make more port entries at baseline and in the late sucrose-trial period,\n    have a lower baseline-normalized port entry response to the sucrose CS, and freeze more to the\n    shock CS relative to baseline.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 1; Extended Data Figure 8e\n  quote: showed significantly enhanced baseline port entries and reduced port entry specificity\n    during sucrose trials, compared to the control group\n  statistics:\n  - about: sucrose trials, raw port entry probability at baseline\n    test: unpaired t-test, two-tailed\n    statistic: t(33) = 2.37\n    p: 0.012\n    ci: {level: 0.95, low: 0.01974, high: 0.2594}\n  - about: sucrose trials, raw port entry probability 10 to 25 s after sucrose\n    test: unpaired t-test, two-tailed\n    statistic: t(33) = 3.797\n    p: 0.0006\n    ci: {level: 0.95, low: 0.1099, high: 0.3638}\n  - about: sucrose trials, z-scored port entry probability\n    test: unpaired t-test, two-tailed\n    p: 0.0038\n    ci: {level: 0.95, low: -1.067, high: -0.2225}\n  - about: shock trials, z-scored freezing\n    test: unpaired t-test, two-tailed\n    statistic: t(33) = 2.495\n    p: 0.0178\n    ci: {level: 0.95, low: 0.229, high: 2.254}\n  - about: shock trials, raw freezing\n    test: unpaired t-test, two-tailed\n    statistic: t(33) = 0.1401\n    p: 0.8894\n    ci: {level: 0.95, low: -0.0771, high: 0.06722}\n  criterion: Last discrimination-task session. Port entry probability with 500 ms bins over 25 s\n    before and after CS onset, z-scored against the 25 s baseline (Methods). Baseline is the 25 s\n    before CS onset; the late window is 10 to 25 s after sucrose delivery as the statistics say;\n    the window of the z-scored comparison is not given, readings (a) 0 to 10 s and (b) 0 to 25 s\n    after CS onset. Freezing in shock trials by the Methods' velocity rule (below 0.3 cm/s) during\n    the CS, z-scored against the pre-CS period. Reproduced when the four significant comparisons\n    have p < 0.05 in the stated directions under every reading (two-tailed unpaired t-test across\n    mice).\n- id: fig5dh-behavior-clusters\n  statement: Unsupervised trial-by-trial clustering of pose-derived behavior gives seven clusters\n    for sucrose trials and five for shock trials, which separate passive and active strategies.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 3; Figure 5d-e and 5g-h; Methods, Unsupervised trial-based classification of\n    behaviors\n  quote: Following watershed segmentation, we obtained seven clusters for sucrose trials and five\n    clusters for shock trials\n  expected:\n  - quantity: sucrose-trial clusters\n    value: 7\n    tolerance: 0\n  - quantity: shock-trial clusters\n    value: 5\n    tolerance: 0\n  criterion: As the Methods give it. Pose of head, electrode, ears and tail from DeepLabCut; eight\n    measures (velocity, distance to port, direction, direction relative to port, and the change of\n    each) for 300 frames (20 s at 15 fps) after CS onset; tsfresh 0.16.0 features (about 6000);\n    PCA, t-SNE on the top 30 PCs (Extended Data Figure 8k), a kernel density over the t-SNE map\n    (seaborn kdeplot), local maxima as markers for a watershed; sucrose and shock trials separately.\n    The paper's pose estimates or its trained network are needed; if the dataset holds neither, a\n    new network would be the agent's choice and the claim is blocked. t-SNE perplexity, the kernel\n    bandwidth and the random seed are not given; they change the cluster count, so the defaults of\n    scikit-learn and seaborn are used with several seeds and the counts reported. Reproduced when\n    the default settings give 7 and 5 clusters for most seeds.\n- id: fig5fi-active-strategy-preference\n  statement: Control mice show more active-strategy trials than CRISPR mice in both sucrose and\n    shock trials.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 3; Figure 5f and 5i\n  quote: We found that control mice preferred active behavioral strategies during both sucrose and\n    shock trials ... while the PVT-BLA: Nt CRISPR-cKO abolished this behavioral preference to active\n    strategies\n  statistics:\n  - about: sucrose trials\n    test: unpaired t-test, two-tailed\n    statistic: t(28) = 2.25\n    p: 0.0325\n    ci: {level: 0.95, low: -0.3141, high: -0.01474}\n    n: 15 mice per group\n  - about: shock trials\n    test: unpaired t-test, two-tailed\n    statistic: t(28) = 2.366\n    p: 0.0251\n    ci: {level: 0.95, low: -0.6799, high: -0.04895}\n    n: 15 mice per group\n  depends_on:\n  - fig5dh-behavior-clusters\n  criterion: Clusters from fig5dh-behavior-clusters labelled passive or active as the Figure 5\n    legend defines them, sucrose clusters by low or high change in distance moved toward the port\n    after CS onset, shock clusters by high freezing with low darting or low freezing with high\n    darting. The split is not given; readings are (a) clusters above or below the median of the\n    cluster means, (b) above or below the mean over all trials. Shock clusters matching neither\n    pattern are left out. Darting is not defined in the text and freezing in this task is read by\n    the Methods' 0.3 cm/s rule. Per mouse the fraction of active trials; two-tailed unpaired\n    t-test. Reproduced when, under every reading, control mice have a higher fraction for both\n    trial types with p < 0.05.\n- id: ed8os-active-trial-responses\n  statement: BLA responses to the CSs are larger in active trials, and the CRISPR-cKO reduces the\n    responses of untagged BLA neurons in active trials for both sucrose and shock CSs.\n  source: Results, NT inputs from the PVT to the BLA mediates passive-active behavioral strategies,\n    paragraph 3; Extended Data Figure 8o and 8s\n  quote: Finally, we observed predominant BLA neural responses to CSs during the active behavioral\n    trials, which were diminished by the PVT-BLA: Nt CRISPR-cKO\n  statistics:\n  - about: sucrose CS, untagged neurons, active trials, control against CRISPR\n    test: two-way ANOVA with Holm-Sidak's multiple comparisons test\n    statistic: t(1284) = 2.27\n    p: 0.046\n  - about: shock CS, untagged neurons, active trials, control against CRISPR\n    test: two-way ANOVA with Holm-Sidak's multiple comparisons test\n    statistic: t(780) = 2.245\n    p: 0.049\n  - about: sucrose CS, BLA-NAc, group by state interaction\n    test: two-way ANOVA\n    statistic: F(1, 434) = 10.96\n    p: 0.001\n  depends_on:\n  - fig5fi-active-strategy-preference\n  - fig4c-photoidentification\n  criterion: Response per neuron and trial type as in fig4e-cluster-responses-attenuated, computed\n    separately over active and passive trials, with trial numbers matched between the two\n    (Methods). The unit of the ANOVA is not given (its degrees of freedom exceed the neuron\n    counts); readings are (a) neuron by state values, (b) trial by neuron values. Two-way ANOVA of\n    group by state with Holm-Sidak comparisons. Reproduced when, under every reading, untagged\n    neurons in active trials respond less in CRISPR than in control at p < 0.05 for both CSs.\n- id: ed9-nt-acute-epsc\n  statement: Bath-applied NT (10 nM) enhances EPSCs in BLA-NAc neurons and suppresses them in\n    BLA-CeM neurons, and an NTSR1 antagonist abolishes the difference.\n  source: Results, The temporal dynamics of NT are critical for valence assignment, paragraph 1;\n    Extended Data Figure 9f-g\n  quote: At a concentration of 10 nM, NT significantly enhanced EPSCs in BLA-NAc neurons and\n    suppressed EPSCs in BLA-CeM neurons\n  statistics:\n  - about: NT alone, the population with W = -45 (all ranks negative), n = 9\n    test: Wilcoxon signed-rank test\n    statistic: W = -45\n    p: 0.0039\n    n: 9 neurons\n  - about: NT alone, the population with W = 52, n = 12\n    test: Wilcoxon signed-rank test\n    statistic: W = 52\n    p: 0.0425\n    n: 12 neurons\n  - about: with NTSR1 antagonist, n = 8\n    test: Wilcoxon signed-rank test\n    statistic: W = -26\n    p: 0.0781\n    n: 8 neurons\n  - about: with NTSR1 antagonist, n = 9\n    test: Wilcoxon signed-rank test\n    statistic: W = -13\n    p: 0.4961\n    n: 9 neurons\n- id: ed9kl-nt-preincubation-ltp\n  statement: Pre-incubation with NT (10 nM) reduces STDP-induced LTP in BLA-NAc neurons but not in\n    BLA-CeM neurons.\n  source: Results, The temporal dynamics of NT are critical for valence assignment, paragraph 1;\n    Extended Data Figure 9k-l\n  quote: STDP-induced LTP in the presence of NT (10 nM) 10–50 minutes after induction was reduced in\n    BLA-NAc neurons, but unchanged in BLA-CeM neurons compared with the ACSF control\n  statistics:\n  - about: BLA-NAc\n    test: unpaired t-test\n    statistic: t(31) = 2.177\n    p: 0.0367\n    ci: {level: 0.95, low: -0.649, high: -0.022}\n  - about: BLA-CeM\n    test: unpaired t-test\n    statistic: t(25) = 1.193\n    p: 0.2442\n    ci: {level: 0.95, low: -0.1305, high: 0.4896}\n- id: ed10b-ntsr1-antagonist-reward\n  statement: Intra-BLA NTSR1 antagonist before conditioning enhances tone-sucrose learning and does\n    not change freezing in tone-shock conditioning.\n  source: Results, The temporal dynamics of NT are critical for valence assignment, paragraph 1;\n    Extended Data Figure 10b-c\n  quote: NTSR1 antagonist delivered in the BLA 15 minutes before the conditioning session enhanced\n    reward learning but had no effects on punishment learning\n  statistics:\n  - about: sucrose, session 2 normalized response\n    test: unpaired t-test\n    statistic: t(16) = 2.128\n    p: 0.049\n    ci: {level: 0.95, low: 0.0029, high: 1.483}\n  - about: freezing during the tone\n    test: unpaired t-test\n    statistic: t(19) = 1.061\n    p: 0.3021\n    ci: {level: 0.95, low: -7.577, high: 23.15}\n- id: ed10-ntsr1-cko-reward\n  statement: Ntsr1 CRISPR-cKO in BLA-CeA neurons, but not BLA-NAc neurons, reduces port entry to\n    the sucrose CS; global BLA Ntsr1 cKO before acquisition impairs tone-sucrose learning, while\n    cKO after acquisition does not affect recall.\n  source: Results, The temporal dynamics of NT are critical for valence assignment, paragraph 1;\n    Extended Data Figure 10k and 10o\n  quote: we found that CRISPR-cKO of Ntsr1 gene in the BLA suppressed reward learning\n  statistics:\n  - about: BLA-CeA Ntsr1 cKO, port entry\n    test: unpaired t-test, two-tailed\n    statistic: t(16) = 3.577\n    p: 0.0025\n    ci: {level: 0.95, low: -0.7107, high: -0.1818}\n  - about: BLA-NAc Ntsr1 cKO, port entry\n    test: unpaired t-test, two-tailed\n    statistic: t(9) = 0.03604\n    p: 0.972\n    ci: {level: 0.95, low: -0.7141, high: 0.7373}\n  - about: global BLA cKO, control against pre-acquisition cKO\n    test: one-way ANOVA, Holm-Sidak's multiple comparisons test\n    p: 0.019\n"
}
```

```
File created successfully at: claims/000689/10.1038-s41586-022-04964-y.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000689/10.1038-s41586-022-04964-y.yaml paper/10.1038-s41586-022-04964-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000689/10.1038-s41586-022-04964-y.yaml",
 "old_string": "    shock trials ... while the PVT-BLA: Nt CRISPR-cKO abolished this behavioral preference to active\n    strategies",
 "new_string": "    shock trials ... CRISPR-cKO abolished this behavioral preference to active strategies"
}
```

```
The file claims/000689/10.1038-s41586-022-04964-y.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000689/10.1038-s41586-022-04964-y.yaml",
 "old_string": "    trials, which were diminished by the PVT-BLA: Nt CRISPR-cKO",
 "new_string": "    trials, which were diminished by the"
}
```

```
The file claims/000689/10.1038-s41586-022-04964-y.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000689/10.1038-s41586-022-04964-y.yaml paper/10.1038-s41586-022-04964-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000689/10.1038-s41586-022-04964-y.yaml; grep -n "—\|rather" $f; python -c "
import yaml;d=yaml.safe_load(open('$f'));c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c))"
```

```
38 30 26
```

**Agent**

I wrote `claims/000689/10.1038-s41586-022-04964-y.yaml`. The quote checker passes it with 0 problems (38 quotes, 185 statistical values found in the text). Nothing is committed.

**Text read:** the accepted author manuscript in PubMed Central (PMC9583860), as served by ncbi_pmc. It has the main text, the full Methods (including the per-panel "Additional statistical information"), and the legends of Figures 1–5 and Extended Data Figures 1–10. I did not read the version of record. The supplementary files the manuscript lists (source data per figure, Reporting Summary) are not in `paper/`, and no claim needs them. There was no PDF, so I could not look at any figure.

**Code:** none. The paper links no code and says it is "available upon request", so every method detail comes from the Methods and the legends.

**Claims:** 38. All 38 have quotes, 30 record statistics and 26 have criteria. They cover:
- anatomy, glutamate co-release and CRISPR validation (Extended Data 1–5);
- the global and PVT-BLA Nt knockouts and the photostimulation behavior (Figures 1 and 2);
- terminal calcium and NT-sensor photometry (Figure 3, Extended Data 6);
- the electrophysiology: recording count, photoidentification, basal firing, responsive proportions, the 7 clusters, cluster and projector responses (Figure 4, Extended Data 8);
- trajectories, SVM decoding and behavior clustering with active/passive strategies (Figure 5);
- the ex vivo and Ntsr1 pharmacology and knockout results (Extended Data 9–10).

The non-recording claims are included even though the dataset may not hold them.

**Details the paper leaves open, with the readings named:**
- **Analysis windows shown only as figure shading:** Fig 1g (0–10 s or 0–25 s), Fig 2c (0–20 s, 0–2 s or 0–25 s), Fig 4e/f/g (0–1 s or 0–0.5 s), and the z-scored window in Extended Data 8e (0–10 s or 0–25 s).
- **Session for Fig 2c:** the last tone-sucrose day, or the sucrose trials of the discrimination task.
- **Photometry early/late trials:** the first 16 trials, or all trials, of the first and last sessions. The measure can be area under the curve or mean z-score.
- **Responsive-neuron threshold (z ±1.98):** applied to the mean over 0–1 s, or to any 20 ms bin.
- **Basal firing rate:** the 1 s pre-CS baseline, or the whole session.
- **Photoidentification pulses:** all light onsets, or the 1 Hz pulses only. The authors' own labels are used if the dataset has them.
- **Ward clustering on correlation distance:** Ward on the correlation matrix, or Euclidean Ward on normalized rows.
- **Single PCA across two groups of neurons (Fig 5a):** the groups stacked along time with shared neuron slots, or all neurons as variables with the other group zeroed. The random subsample and neuron pairing are run over 20 subsamples.
- **SVM pseudo-trials:** trial-index matching, or random draws per neuron. Features come from activity averaged over 0–1 s, or from AUC per time bin.
- **Active/passive split of behavior clusters:** by the median of cluster means, or by the overall mean. "Darting" is undefined, and freezing is read by the Methods' 0.3 cm/s velocity rule.
- **Unit of the Extended Data 8o/s ANOVA:** neurons, or trials.
- **Whether the 685 neurons are counted before or after the 0.3 Hz exclusion:** both counts are shown.

**Missing or inconsistent, needed by claims:**
- Freezing in Fig 2d/h was scored by hand, so an automated rule stands in for it and that is recorded as a deviation.
- The behavior-cluster claims need the paper's pose estimates or its trained DeepLabCut network. If the dataset holds neither, they are blocked. t-SNE perplexity, kernel bandwidth and seed are not given.
- The text itself disagrees in places:
  - Fig 5a reports t(11) for groups of 12 and 14 leave-one-out iterations, and t = 1.224 with P = 0.0002 for the neutral CS.
  - Fig 5b's P-value is 0.2122 in the legend and 0.1309 in the Methods.
  - The Fig 2h statistics are printed under "2f".
  - Mouse counts differ across panels that come from the same cohort.
- Extended Data 9f–g does not say which Wilcoxon result belongs to BLA-NAc and which to BLA-CeM; I recorded them by n and W.
- Cluster numbering can't be recovered from the text, so the Fig 4e clusters are judged as a set.

## End of run

24 turns, 6 minutes, result: success.
