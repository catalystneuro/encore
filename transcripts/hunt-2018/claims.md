# hunt-2018 · claims · run 42926925798

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-018-0239-5.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-018-0239-5.txt",
 "offset": 241,
 "limit": 440
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/pfc-7.data-description.txt; ls papers/datasets/ | grep -i hunt; cat papers/datasets/hunt-2018.yaml 2>/dev/null; ls claims | grep -i hunt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -l "crcns" claims/*.yaml | head; grep -rn -i "code.*inside the dataset\|scripts.*in the data set\|code is part of the data" claims/*.yaml | head
```

```
claims/asari-2009.yaml
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
claims/farrell-2020.yaml
claims/goncalves-2013.yaml
claims/gu-2011.yaml
claims/henze-2000.yaml
claims/holdgraf-2016.yaml
claims/jadhav-2016.yaml
```

**Agent calls Bash**

```bash
for f in $(grep -l "crcns" claims/*.yaml); do echo "== $f"; head -30 $f | grep -i -n "code\|script\|matlab"; done 2>/dev/null | head -60
```

```
== claims/asari-2009.yaml
2:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4:# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.
15:# Code read: none. The paper links no code; it says all analysis was done in MATLAB.
30:#   reanalysed. The dataset description says ac-1 holds both Wehr's and Asari's data.
== claims/bruno-2017.yaml
3:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
11:# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
12:# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
15:# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
16:# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
25:# and motorneuron test; Analysis/Mapping/ the participation maps; Figures/ the figure scripts.
27:# Method choices the code settles where the Methods are silent, used in the criteria below:
== claims/deweese-2004.yaml
2:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
7:# supplement. It links no analysis code, so none was read. The PDF could not be rendered here,
== claims/eyherabide-2008.yaml
1:# Claims for Eyherabide, Rokem, Herz & Samengo (2008), "Burst firing is a neural code in an
4:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
11:# The paper has no supplement. It links no analysis code, so none was read. Some passages are
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/johnson-2017.yaml; grep -n "^checks\|^- id\|kind:" claims/johnson-2017.yaml | head -40
```

```
# Claims for Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), Current Biology 27,
# 1829-1835, "Bidirectional Frontoparietal Oscillatory Systems Support Working Memory",
# doi:10.1016/j.cub.2017.05.046, on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read: the version of record with its supplemental information, as supplied under paper/
# (PDF extracted to text): main text (Results, Discussion), figure legends 1 to 4, STAR Methods
# (pages e1 to e4), and the supplement (legends of Figures S1 to S4, Tables S1 to S3, read from
# the text). The PDF could not be rendered in this run, so the figures themselves were not read:
# the channel list of the Figure 2 cluster (the PFC region of interest of the PSI analysis) and
# the time courses of Figures 2 to 4 are known only from the text and legends. The extraction
# garbles symbols: "3" stands for the multiplication sign, "/" for an arrow, "%" for less than
# or equal, "R" for greater than or equal, "jZj" for |Z|, and a replacement character for the
# minus sign in exponents. Quotes keep the extracted characters. The CRCNS data descriptor
# (paper/pfc-5.data-description.txt) was read only to know what the data set holds; no claim or
# method comes from it.
#
# Code. The paper's Key Resources Table and Data and Software Availability say the custom MATLAB
# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,135p claims/johnson-2017.yaml; ls tools/ | head -40; grep -rn "kind" docs/*.md | grep -i "claim" | head
```

```
# removal, ICA, channel interpolation, manual trial rejection (on average 187 trials per
# subject kept). Then the surface Laplacian, swapping of channels across the midline for the 7
# right-lesioned patients and 10 randomly chosen controls, so that the lesion is on the left, and
# three segments per trial: pretrial baseline (550 to 50 ms before the start screen), encoding
# and maintenance (1500 ms from first stimulus onset; the second stimulus ends at 400 ms), and
# active processing (900 ms from the offset of the test prompt). Measured variables: accuracy,
# ERPs, baseline power spectra, task-induced power, and phase slope index (PSI) between channels.
# "Lesioned visual hemifield" trials are those whose stimuli went to the hemifield contralateral
# to the lesion (Table S1 note).
#
# Methods shared by the EEG claims below, from STAR Methods (Spectral Decomposition; Phase Slope
# Index; Statistical Bootstrapping; Cluster-Based Permutation Testing), fixed for every criterion
# that cites "the shared methods":
# - Correct trials only, except the baseline spectra (all trials). Each visual hemifield is
#   analysed separately.
# - Power, per subject: time-frequency representations at each frequency 1 to 40 Hz with a
#   Hanning-tapered window of 3 cycles (3/f), 10 ms steps, segments zero-padded to 7500 ms. The
#   baseline power of all correct trials and time points is pooled per channel and frequency;
#   r values are drawn and averaged (r = the subject's trial count), 1000 times; the mean task
#   power is Z scored on that distribution.
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 "^schema_version" claims/asari-2009.yaml claims/johnson-2018.yaml; sed -n 1,60p tools/claims_check.py
```

```
claims/asari-2009.yaml:55:schema_version: 2
claims/asari-2009.yaml-56-paper: doi:10.1152/jn.00577.2009
claims/asari-2009.yaml-57-claims:
claims/asari-2009.yaml-58-- id: methods-recording-counts
--
claims/johnson-2018.yaml:118:schema_version: 2
claims/johnson-2018.yaml-119-dataset:
claims/johnson-2018.yaml-120-  archive: crcns
claims/johnson-2018.yaml-121-  id: fcx-2
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import re
L=open('paper/10.1038-s41593-018-0239-5.txt').read().splitlines()
def tab(a,b):
    v=[int(x) for x in L[a:b] if x.strip().isdigit()]
    rows=[v[i:i+4] for i in range(0,len(v),4)]
    return rows
M=tab(386,503);F=tab(508,605)
for n,r in (('M',M),('F',F)):
    print(n,len(r),[sum(x[k] for x in r) for k in (1,2,3)])
print([sum(x[k] for x in M+F) for k in (1,2,3)])
print(min(sum(x[1:]) for x in M+F),max(sum(x[1:]) for x in M+F))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/hunt-2018.yaml",
 "content": "# Claims for Hunt, Malalasekera, de Berker, Miranda, Farmer, Behrens & Kennerley (2018), Nature\n# Neuroscience 21, 1471-1481, \"Triple dissociation of attention and decision computations across\n# prefrontal cortex\", doi:10.1038/s41593-018-0239-5, on CRCNS data set pfc-7 (doi:10.6080/K0PZ5712).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC6331040, open access, JATS XML flattened to text, under\n# paper/), main text, Discussion and Online Methods, and the supplement\n# (41593_2018_239_MOESM1_ESM.pdf, extracted to text in the same file; legends of Supplementary\n# Figures 1 to 12, Supplementary Table 1 and the Supplementary Note). The flattened main text has\n# no main figure legends, and no PDF of the main article was supplied, so the legends of Figures 1\n# to 8 (their sample sizes, tests and significance marks) were not read. Every claim on a main\n# figure rests on the Results and Methods sentences that cite it. The extraction drops the minus\n# sign in some exponents (\"p<1*10 7\" stands for p < 1e-7); quotes keep the extracted characters.\n# The CRCNS data descriptor (paper/pfc-7.data-description.txt) was read only to know what the\n# data set holds; no claim or method comes from it.\n#\n# Code. The Code Availability statement says the custom MATLAB analysis scripts are deposited with\n# the raw data on CRCNS (dataset pfc-7). By the data descriptor they are among the data set's own\n# files (Fig1_2_S1_behaviour, Fig4_RSA, Fig5_OFC_crosscorrelation, Fig6_ACC_multiplesignals,\n# Fig7_single_neurons_cue2and3, Fig8_single_neuron_coding, InfoGathering_Neurons_* and\n# InfoGathering_Preprocess_Neurons). Being among the data set's files, they were not read in this\n# run, and no commit is recorded. Every method below is from the paper's text. Where those scripts\n# settle a detail named as open below, the author may follow them (protocol, Reader step 2) and\n# should say so; the Methods come first where they disagree.\n#\n# Data the paper used (Online Methods, Subjects, Behavioral Protocol, Task, Neuronal Recordings).\n# Two adult male rhesus monkeys, M and F (7-10 kg, about 4 years old); 32 sessions for M and 25\n# for F (Results, paragraph 2). The data descriptor names the behavioural files \"Miles\" and\n# \"Frank\"; which is M and which F is the author's to confirm. Each session used a set of 10\n# pre-learned picture cues, 5 for reward probability (10, 30, 50, 70, 90%) and 5 for magnitude\n# (0.15 to 0.95 AU); M learnt 13 sets, F 11. Trial: 500 ms central fixation; two options (left and\n# right), each two covered cues (probability and magnitude, one per row, the row counterbalanced);\n# an instructed saccade to cue 1 (300 ms fixation), then an instructed saccade to cue 2 on the same\n# option (\"option\" trial) or to the same attribute on the other option (\"attribute\" trial), 300 ms;\n# then free choice by left/right joystick or further saccades to cue 3 (300 ms) and cue 4; after the\n# choice all cues shown (500 ms F, 1000 ms M) and juice given with the chosen probability and\n# magnitude. Option and attribute trials interleaved in blocks of 50; blocks of 25 \"simultaneous\"\n# trials (all cues shown) between them are not analysed. Eye position at 240 Hz (recorded at 1000\n# Hz by MonkeyLogic), joystick, single units from tungsten electrodes (8-24 per session, Plexon\n# Omniplex at 40 kHz, manual sorting). Areas: ACC (dorsal bank of the cingulate sulcus, AP 27-37\n# mm), DLPFC (banks of the principal sulcus), OFC (between medial and lateral orbital sulci); VMPFC\n# units were recorded too but are not analysed here. Units with mean firing rate below 1 Hz are\n# excluded (9 ACC, 21 DLPFC, 12 OFC), leaving 189 ACC, 135 DLPFC and 183 OFC. Measured variables\n# per trial: trial type, cue identities and values, cue locations and order, saccade times and\n# targets, number of cues viewed, choice (left/right), reaction time, reward; spike times aligned\n# to cue 1, 2, 3 onsets (cue onset is locked to the saccade) and joystick response.\n#\n# Methods shared by the claims below, fixed for every criterion that cites them:\n# - RSA (Methods, Representational similarity analysis): per neuron, mean firing rate 100-500 ms\n#   after cue 1 onset for 20 conditions (5 probability and 5 magnitude cues, by rank, on left and on\n#   right), z-scored across the 20; a neurons x 20 matrix per region (pseudopopulation over\n#   sessions); Pearson correlation between conditions gives the 20 x 20 matrix. Sliding windows of\n#   +/- 100 ms for time courses.\n# - RSA template regression (Methods, RSA template-based regression): OLS of the 400 elements on an\n#   intercept and six templates, each divided by its maximum absolute value: identity; spatial\n#   attention (1 same side, -1 opposite); stimulus identity (1 where |i-j| = 10); attended value\n#   (rank(i) x rank(j), ranks -2 to 2); left/right value (attended value on the same side, 0 across\n#   sides); accept/reject (sign of attended value). CPD as defined in the Methods. T-statistic per\n#   coefficient and between-region F-statistic, each against a null of 10,000 permutations of the\n#   20 cue identities (Methods, Statistical inference on RSA template-based regression model).\n# - GLM (Methods, General linear model): per neuron, OLS of firing rate in 200 ms bins stepped by\n#   10 ms, -100 to 500 ms around cue 1, 2 and 3 onsets and -500 to 100 ms around the response, on\n#   EVs 1-18 exactly as the Methods define them (EVs 11 and 12 the trial-type indicators, which sum\n#   to the constant); trials with fewer than 3 cues viewed excluded. Weights are the T-statistics\n#   of the coefficients. \"250 ms\" is the bin 150-350 ms after the cue (Results, Attention-guided\n#   value comparison in OFC, paragraph 3).\n# - Subspace correlations: Pearson correlation across all neurons of a region between the\n#   T-statistics of two EVs (Methods, Peri-stimulus correlation; Supplementary Figures 2 and 10\n#   name Pearson's correlation). Region differences by Fisher r-to-Z of independent correlations,\n#   n = the neurons of each region.\n#\n# Details the paper leaves open, shared by several criteria (each criterion names those it needs):\n# - O1, sidedness of the Fisher r-to-Z test between regions. Readings (a) two-sided; (b) one-sided\n#   in the predicted direction.\n# - O2, the significance level for counting single neurons (Figures 7 and 8). Not stated in the\n#   text read (the legends are missing). Readings (a) p < 0.05; (b) p < 0.01, each two-sided on the\n#   OLS coefficient or contrast.\n# - O3, the time bin for single-neuron tests at cues 2 and 3 (Figure 7). Readings (a) 250 ms after\n#   the cue, as Figure 5B-F/K; (b) 300 ms after the cue, as Figure 6A.\n# - O4, how trials are split for the projections of Figure 6. The Methods say odd against even\n#   trials, each half used once for weights and once for projection, then averaged; the Results say\n#   \"100 random splits\" into halves, averaged. Readings (a) odd/even; (b) 100 random half splits.\n# - O5, the five reaction-time bins (\"five separate bins depending upon response time from Cue 1\n#   onset\"). Readings (a) quintiles of reaction time within each session; (b) quintiles of the\n#   reaction times of all sessions of the monkey.\n# - O6, the firing rates projected in Figure 6. Readings (a) firing rate in Hz in 200 ms bins as in\n#   the GLM; (b) the same z-scored per neuron. The projection is the OLS regression, at each time\n#   point, of the neurons' rates on the neurons x 2 weight matrix, baseline corrected to cue 1\n#   onset +/- 50 ms (Methods, Projection of ACC activity).\n# - O7, the \"T-statistics of contrasts\" used as weights for belief confirmation (EVs 13 and 14 at\n#   300 ms after cue 2, EVs 15 and 16 at 300 ms after cue 3) and action (EVs 17 and 18 at 200 ms\n#   before response). These come from separate fits. Readings (a) the mean of the T-statistics;\n#   (b) the T-statistic of the mean coefficient, its variance the mean of the variances over the\n#   number of terms.\n# - O8, sidedness of the RSA permutation test of a template. Readings (a) one-sided, positive\n#   coefficient; (b) two-sided on |T|.\n# - O9, the trials used for RSA and the cue 1 regression of Figure 8. The exclusion of trials with\n#   fewer than 3 cues is stated for the GLM only. Readings (a) all completed option and attribute\n#   trials; (b) only those with 3 or more cues viewed.\nschema_version: 2\npaper: doi:10.1038/s41593-018-0239-5\nclaims:\n- id: sessions-and-trials\n  statement: Behaviour comes from 25 sessions of monkey F and 32 of monkey M, 9,863 trials for F\n    and 14,251 for M.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2; Supplementary Figure 1\n    legend\n  quote: Regression models were fit to all trials, collapsed across sessions (n=14,251 trials\n    (subject M), n=9,863 trials (subject F))\n  expected:\n  - quantity: sessions, monkey F\n    value: 25\n    tolerance: 0\n  - quantity: sessions, monkey M\n    value: 32\n    tolerance: 0\n  - quantity: trials, monkey M\n    value: 14251\n    tolerance: 0\n  - quantity: trials, monkey F\n    value: 9863\n    tolerance: 0\n  criterion: Counts are exact, so the tolerance is zero. Which trials \"all trials\" counts is not\n    stated. Readings (a) all completed option and attribute trials (simultaneous trials left out,\n    Methods, Task, last paragraph); (b) the same, also counting aborted trials; (c) the same as (a)\n    with trials of equal expected value left out. Reproduced when the session counts match and one\n    reading gives both trial counts; partially reproduced when the trial counts are within 1%\n    under one reading.\n- id: neuron-counts\n  statement: After excluding units with mean firing rate below 1 Hz (9 ACC, 21 DLPFC, 12 OFC), the\n    analyses use 189 ACC, 135 DLPFC and 183 OFC neurons.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 1; Online\n    Methods, Neuronal Recordings, paragraph 2\n  quote: We excluded neurons with an average firing rate of <1Hz from further analysis (9 units in\n    ACC, 21 in DLPFC, 12 in OFC; n reported in main text are after these units have been removed)\n  expected:\n  - quantity: ACC neurons\n    value: 189\n    tolerance: 0\n  - quantity: DLPFC neurons\n    value: 135\n    tolerance: 0\n  - quantity: OFC neurons\n    value: 183\n    tolerance: 0\n  - quantity: excluded ACC units\n    value: 9\n    tolerance: 0\n  - quantity: excluded DLPFC units\n    value: 21\n    tolerance: 0\n  - quantity: excluded OFC units\n    value: 12\n    tolerance: 0\n  criterion: Units are counted by region, and the mean firing rate of each is computed. Counts are\n    exact, so the tolerance is zero. The paper does not say over what the mean rate is taken.\n    Readings (a) the whole session; (b) all analysed trials, from trial start to response. The\n    per-session counts of Supplementary Table 1 are compared too. Its caption says units above 1 Hz,\n    but its columns sum to 198 ACC, 195 OFC and 156 DLPFC (189 + 9, 183 + 12, 135 + 21), and it\n    lists 29 sessions for M and 24 for F. Reproduced when the region totals match under one\n    reading; the table's agreement with the data is reported either way.\n- id: choice-accuracy-ev\n  statement: Monkeys F and M chose the option with the higher expected value on 76.6% and 79.8% of\n    trials.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2; Figure 1b\n  quote: They chose the option with higher expected value on 76.6% and 79.8% of trials (monkeys F\n    (n=25 sessions) and M (n=32 sessions) respectively)\n  expected:\n  - quantity: choices of the higher expected value, monkey F\n    value: 76.6\n    tolerance: 7.66\n    unit: '%'\n  - quantity: choices of the higher expected value, monkey M\n    value: 79.8\n    tolerance: 7.98\n    unit: '%'\n  criterion: Expected value is probability times magnitude of the option (Methods, Task). Trials\n    are the completed option and attribute trials. The paper does not say how trials of equal\n    expected value count. Readings (a) left out; (b) counted as not choosing the higher. Reproduced\n    when both values are within tolerance under one reading.\n- id: chose-on-partial-information\n  statement: Monkeys F and M chose before seeing all four cues on 85.5% and 71.4% of trials.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2\n  quote: 'subjects chose before all four cues had been evaluated on 85.5%/71.4% of trials (subjects\n    F/M respectively)'\n  expected:\n  - quantity: trials with fewer than four cues viewed, monkey F\n    value: 85.5\n    tolerance: 8.55\n    unit: '%'\n  - quantity: trials with fewer than four cues viewed, monkey M\n    value: 71.4\n    tolerance: 7.14\n    unit: '%'\n- id: choice-accuracy-observed\n  statement: Judged by the pictures observed, choice accuracy was 86.3% for monkey F and 87.4% for\n    monkey M.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2\n  quote: Choice accuracy based upon the pictures observed , rather than the true expected value, was\n    substantially higher (86.3% and 87.4% for monkey F and M respectively)\n  expected:\n  - quantity: accuracy on observed pictures, monkey F\n    value: 86.3\n    tolerance: 8.63\n    unit: '%'\n  - quantity: accuracy on observed pictures, monkey M\n    value: 87.4\n    tolerance: 8.74\n    unit: '%'\n  criterion: The paper does not define the expected value from the pictures observed. Readings (a)\n    each unseen cue set to the middle level of its attribute (50% probability, 0.55 AU magnitude),\n    expected value as probability times magnitude, trials where the observed values tie left out;\n    (b) the same, ties counted as incorrect; (c) the choice judged by the sum of the observed cues'\n    ranks (-2 to 2) per option, ties left out. Reproduced when both values are within tolerance\n    under one reading.\n- id: figs1ab-cue-weights\n  statement: In logistic regressions of choice, both monkeys weighted reward probability and\n    magnitude about equally and used all four viewed cues, and both showed a small bias towards\n    choosing the second side on option trials.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2; Supplementary Figure 1A\n    and 1B\n  quote: Both subjects use all four cues to guide their choices, with a slight upweighting of the\n    antepenultimate cue ... both subjects show a small but significant bias towards choosing the\n    second side on option trials\n  criterion: Per monkey, all trials pooled across sessions (Supplementary Figure 1 legend). Model B\n    regresses choice (left = 1) on left minus right probability and left minus right magnitude,\n    separately for option and attribute trials, with a left bias and a first-side bias. The units of\n    probability and magnitude are not stated; ranks and raw values both step by 0.2, so the ratio of\n    the two weights is the same either way. Model A regresses choice on the final, n-1, n-2 and (on\n    four-cue trials) n-3 viewed pictures. The sign and scale of a picture's regressor are open.\n    Readings (a) its rank (-2 to 2) signed + for the left option, - for the right; (b) its raw\n    value, signed the same way. \"Approximately equal weight\" has two readings, (a) the 95%\n    confidence intervals of the two weights overlap, (b) a Wald test of their difference has p >\n    0.05. Reproduced when, in both monkeys, every picture weight in A is positive with p < 0.05,\n    probability and magnitude weights are positive and approximately equal on both trial types,\n    and the first-side bias on option trials is negative (towards the second side) with p < 0.05.\n- id: figs1cd-fewer-cues-more-accurate\n  statement: Choices were more often optimal on trials where 2 pictures were viewed than on trials\n    with 3 or 4, because trials ended early when the first two cues gave a larger value difference.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 2; Supplementary Figure 1C\n    and 1D\n  quote: Surprisingly, choice accuracy was also higher on trials where subjects sampled fewer pieces\n    of information ( Fig. S1c ). This was because such trials were associated with a higher value\n    difference, and so subjects terminated these trials more quickly ( Fig. S1d ).\n  criterion: Per monkey, the fraction of choices of the higher expected value (as in\n    choice-accuracy-ev, reading (a)) on trials with 2, 3 and 4 cues viewed, and the mean value\n    difference by the number of cues viewed. The value difference is not defined in the text read.\n    Readings (a) the absolute difference of the two options' true expected values; (b) the absolute\n    difference implied by cues 1 and 2 alone, unseen cues at the middle level. Reproduced when in\n    both monkeys accuracy on 2-cue trials exceeds that on 3-cue and on 4-cue trials, and the mean\n    value difference is largest on 2-cue trials under one reading.\n- id: fig2a-sample-the-favourite\n  statement: On attribute trials, the free third saccade went preferentially to the option with the\n    higher value between cue 1 and cue 2.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 3; Figure 2a\n  quote: On ‘attribute’ trials, this saccade was preferentially directed towards the option with the\n    higher relative expected value between cue 1 and cue 2\n  criterion: Attribute trials with a third cue viewed; the third saccade is diagonal (back to the\n    first option) or vertical (to the second option) (Methods, GLM, EVs 7-10). Cue 1 and cue 2 are\n    the same attribute, so their ranks are compared. The paper's test is in the missing legend.\n    Readings (a) a logistic regression of returning to the first option on the rank of cue 1 minus\n    the rank of cue 2, per monkey, slope positive at p < 0.05; (b) the proportion returning to the\n    first option when cue 1 > cue 2 against when cue 1 < cue 2, chi-square at p < 0.05. Reproduced\n    when both monkeys show the effect under one reading; partially reproduced for one monkey.\n- id: fig2b-positive-evidence\n  statement: On option trials, subjects sampled the fewest cues when cues 1 and 2 were highest in\n    value and the most when they were lowest.\n  source: Results, Experimental paradigm and subject behaviour, paragraph 3; Figure 2b\n  quote: On ‘option’ trials, subjects sampled fewest pieces of information when cues 1 and 2 were\n    highest in value, but most information when cues 1 and 2 were lowest in value\n  criterion: Option trials; the number of cues viewed (2, 3 or 4) as a function of the ranks of\n    cues 1 and 2 (a 5 x 5 table, Figure 2b). Readings of \"highest\" and \"lowest\" (a) the corners,\n    both ranks 2 against both ranks -2; (b) the sum of the two ranks, the mean number of cues\n    decreasing with it (Spearman correlation negative at p < 0.05). Whether the monkeys are pooled\n    is not stated; readings (i) each monkey, (ii) pooled. Reproduced when the mean number of cues\n    is lower for the highest than for the lowest values under reading (a), or the correlation is\n    negative under (b), in both monkeys or pooled.\n- id: fig4d-spatial-attention\n  statement: At cue 1, DLPFC representational similarity reflects whether the subject is attending\n    left or right; spatial attention is also represented in OFC and ACC.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 3 and 4;\n    Figure 4a-d\n  quote: DLPFC RSA reflected whether the subject was attending left or right ( Fig. 4d ) ... for\n    example, spatial attention is represented in both OFC and ACC ( Fig. 4d )\n  criterion: The shared RSA and template regression on the 100-500 ms matrix, all neurons of each\n    region; open details O8 and O9. Reproduced when the spatial attention template is significant\n    (permutation p < 0.05) in DLPFC, its CPD is larger in DLPFC than in ACC and OFC, and it is\n    positive in OFC and ACC. The between-region F permutation test is reported.\n- id: fig4e-ofc-stimulus-identity\n  statement: At cue 1, OFC representational similarity reflects the attended stimulus identity\n    irrespective of its spatial position.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 3; Figure 4e\n  quote: OFC representational similarity reflected the currently attended stimulus identity,\n    irrespective of spatial position ( Fig. 4e )\n  criterion: As fig4d-spatial-attention, for the stimulus identity template. Reproduced when it is\n    significant (permutation p < 0.05) in OFC and its CPD is larger in OFC than in ACC and DLPFC.\n- id: fig4f-ofc-attended-value\n  statement: At cue 1, OFC representational similarity is high for cues of similar attended value,\n    consistent with a linear value code.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 3 and 6;\n    Figure 4a and 4f\n  quote: OFC representational similarity reflected the currently attended stimulus identity,\n    irrespective of spatial position ( Fig. 4e ), and was also high for cues of similar attended\n    value ( Fig. 4f )\n  criterion: As fig4d-spatial-attention, for the attended value template. Reproduced when it is\n    significant (permutation p < 0.05) in OFC and its CPD is larger in OFC than in ACC and DLPFC.\n- id: fig4g-left-right-value\n  statement: At cue 1, ACC and DLPFC representational similarity shows a value code modulated by\n    whether the subject attends the left or right option.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 3; Figure 4g\n  quote: ACC and DLPFC RSA showed a value code modulated by whether the subject was currently\n    attending to the left or right option ( Fig. 4g )\n  criterion: As fig4d-spatial-attention, for the left/right value template. Reproduced when it is\n    significant (permutation p < 0.05) in ACC and in DLPFC, and its CPD in each exceeds that in OFC.\n- id: fig4h-acc-accept-reject\n  statement: At cue 1, ACC representational similarity divides high-valued from low-valued cues,\n    best explained as a categorical (accept/reject) function of value.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraphs 3 and 7;\n    Figure 4c and 4h\n  quote: ACC RSA also divided high-valued and low-valued items such that variance in ACC was best\n    explained as a non-linear, categorical function of value ( Fig. 4h\n  criterion: As fig4d-spatial-attention, for the accept/reject template (sign of attended value),\n    which enters the model with the attended value template. Reproduced when it is significant\n    (permutation p < 0.05) in ACC and its CPD in ACC exceeds that of the attended value template in\n    ACC and that of the accept/reject template in DLPFC. Its value in OFC is reported (the\n    latencies give an OFC t75 for it).\n- id: figs2-consistent-across-subjects\n  statement: The triple dissociation of RSA matrices at cue 1 is consistent across the two monkeys.\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 3;\n    Supplementary Figure 2\n  quote: This was consistent across subjects ( Fig. S2 )\n  depends_on:\n  - fig4d-spatial-attention\n  - fig4e-ofc-stimulus-identity\n  - fig4f-ofc-attended-value\n  - fig4g-left-right-value\n  - fig4h-acc-accept-reject\n  criterion: The shared RSA computed on each monkey's neurons separately (Supplementary Figure 2\n    legend). The paper reports no test of consistency. Reproduced when, in each monkey, the template\n    regression coefficients are positive for DLPFC spatial attention, OFC stimulus identity, OFC\n    attended value, ACC and DLPFC left/right value and ACC accept/reject; partially reproduced when\n    four of these six hold in both monkeys.\n- id: figs4-dlpfc-top-bottom\n  statement: Split by top and bottom cue position (40 conditions), the RSA results replicate, and\n    DLPFC similarity is also modulated by top/bottom position, so DLPFC represents spatial position\n    more than left/right action.\n  source: Supplementary Figure 4 legend\n  quote: in DLPFC, representational similarity is modulated by top/bottom stimulus location ... This\n    indicates that DLPFC activity primarily represents spatial position rather than simply\n    left/right action\n  criterion: The shared RSA on 40 conditions (20 conditions by top and bottom position of cue 1),\n    100-500 ms. No test is given. Measure, from the legend's comparison, the mean similarity of\n    pairs of conditions in the same quadrant (top left with top left) against pairs on the same side\n    but different rows (top left with bottom left), excluding the diagonal. Reproduced when this\n    difference is positive in DLPFC and larger there than in ACC and OFC.\n- id: fig4-t75-latencies\n  statement: Spatial attention reached 75% of its peak CPD at about the saccade (24, 72 and 67 ms in\n    ACC, DLPFC, OFC); stimulus identity and attended value in OFC (269, 241 ms) and accept/reject\n    (238 ms ACC, 224 ms OFC) followed; left/right value came later (457 ms ACC, 369 ms DLPFC).\n  source: Results, Triply dissociable PFC population codes at first saccade, paragraph 5;\n    Supplementary Figure 5B\n  quote: Spatial attention affected representational similarity around the time of the saccadic\n    eye-movement (t 75 =24ms in ACC, 72ms in DLPFC, 67ms in OFC) ... coding of stimulus identity and\n    attended value (t 75 =269ms/241ms respectively in OFC) was comparable in latency to accept/reject\n    coding (t 75 =238ms in ACC, 224ms in OFC). By contrast, action value coding emerged significantly\n    later (t 75 =457ms in ACC, 369ms in DLPFC)\n  depends_on:\n  - fig4d-spatial-attention\n  expected:\n  - quantity: t75 spatial attention, ACC\n    value: 24\n    tolerance: 10\n    unit: ms\n  - quantity: t75 spatial attention, DLPFC\n    value: 72\n    tolerance: 10\n    unit: ms\n  - quantity: t75 spatial attention, OFC\n    value: 67\n    tolerance: 10\n    unit: ms\n  - quantity: t75 stimulus identity, OFC\n    value: 269\n    tolerance: 26.9\n    unit: ms\n  - quantity: t75 attended value, OFC\n    value: 241\n    tolerance: 24.1\n    unit: ms\n  - quantity: t75 accept/reject, ACC\n    value: 238\n    tolerance: 23.8\n    unit: ms\n  - quantity: t75 accept/reject, OFC\n    value: 224\n    tolerance: 22.4\n    unit: ms\n  - quantity: t75 left/right value, ACC\n    value: 457\n    tolerance: 45.7\n    unit: ms\n  - quantity: t75 left/right value, DLPFC\n    value: 369\n    tolerance: 36.9\n    unit: ms\n  criterion: The template regression on RSA matrices from +/- 100 ms sliding windows (Methods, RSA\n    template-based regression), cue 1 locked; t75 the first time the CPD reaches 75% of its maximum\n    over time (Methods, last paragraph of that section). The step of the sliding window and the\n    time range are not stated. Readings of the step (a) 10 ms, as the GLM; (b) 1 ms. Range -100 to\n    500 ms after cue 1, as the GLM's stimulus-locked range. Tolerance 10% of each value, but not\n    less than 10 ms, one step of reading (a), for the three spatial attention values. Reproduced\n    when all nine values are within tolerance under one reading; partially reproduced when at least\n    seven are.\n- id: figs5c-latency-order\n  statement: Spatial attention is encoded significantly earlier than stimulus identity, attended\n    value and accept/reject, and left/right value (in ACC and DLPFC) significantly later than the\n    other variables.\n  source: Supplementary Figure 5C legend; Results, Triply dissociable PFC population codes at first\n    saccade, paragraph 5\n  quote: The distributions of t75 for spatial attention do not overlap with those of attended value,\n    accept/reject, or stimulus identity, demonstrating that spatial attention is encoded\n    significantly earlier than other variables. Similarly, left/right value (in ACC and DLPFC) is\n    encoded significantly later than other variables.\n  depends_on:\n  - fig4-t75-latencies\n  criterion: As the Methods give it, 100 noise simulations per region, each adding permuted\n    residuals of the original template regression to the fitted values at each time point and\n    recomputing t75. Which residuals are permuted (within each time point's fit, independently\n    across time, or the same permutation at all time points) is not stated; readings (a) an\n    independent permutation per time point; (b) one permutation shared over time points. In each\n    region, the range of the spatial attention t75 is compared with those of stimulus identity,\n    attended value and accept/reject among the variables S5B keeps for that region (those with CPD\n    of note; a variable whose template is not significant at 100-500 ms is left out). Reproduced\n    when the spatial attention range lies below all of them and, in ACC and DLPFC, the left/right\n    value range lies above all others, under one reading.\n- id: fig5a-ofc-value-cpd\n  statement: Value encoding by OFC neurons peaked about 300 ms after each cue was revealed and stayed\n    above baseline as further cues were attended.\n  source: Results, Attention-guided value comparison in OFC, paragraph 1; Figure 5a\n  quote: This shows that value encoding by OFC neurons peaked approximately 300ms after each cue was\n    revealed but was then sustained above baseline as further cues were attended.\n  expected:\n  - quantity: time of peak CPD for the attended cue's value after its onset, OFC\n    value: 300\n    tolerance: 30\n    unit: ms\n  criterion: The shared GLM, OFC neurons, mean CPD across neurons (Methods, RSA template-based\n    regression, for the CPD definition) for the value EVs of cues 1, 2 and 3, locked to each of\n    cues 1, 2 and 3. How option and attribute EVs are combined is not stated. Readings (a) the mean\n    of the CPDs of the option and attribute EVs of a cue (cue 1, EVs 1 and 5; cue 2, EVs 2 and 6;\n    cue 3, EVs 3, 7 and 9); (b) each trial type separately. Baseline is the cue 1 value CPD at -100\n    ms from cue 1 (the first bin). Reproduced when, under one reading, the peak of each cue's value\n    CPD after its own onset is within tolerance of 300 ms and the cue 1 and cue 2 value CPDs stay\n    above their baseline at every time in the later cue epochs.\n- id: fig5b-stable-attended-value-subspace\n  statement: In OFC, T-statistics for cue 1 value at cue 1 correlate positively across neurons with\n    those for cue 2 value at cue 2, a stable subspace for the currently attended value.\n  source: Results, Attention-guided value comparison in OFC, paragraph 3; Figure 5b\n  quote: we found that single neuron T-statistics for the regression of cue 1 value when cue 1 was\n    attended (ordinate in Fig. 5b ) correlated positively with T-statistics for cue 2 value when\n    cue 2 was attended (abscissa in Fig. 5b )\n  criterion: The shared GLM and subspace correlation, OFC, the 250 ms bins after cue 1 and after\n    cue 2. Option and attribute trials are collapsed (Methods, Peri-stimulus correlation). Readings\n    (a) the mean of the two trial types' T-statistics (cue 1, EVs 1 and 5; cue 2, EVs 2 and 6); (b)\n    the T-statistic of the summed coefficients (EV1 + EV5, as Methods, Projection, write for cue 1).\n    Which test the paper used for a single correlation is in the missing legend; Pearson's test is\n    taken. Reproduced when r > 0 with p < 0.05 under one reading.\n- id: fig5c-attribute-cue2-vs-cue1\n  statement: In OFC, at cue 2 of attribute trials, the attended cue 2 value subspace correlates\n    negatively with the stored cue 1 value subspace (the other option).\n  source: Results, Attention-guided value comparison in OFC, paragraph 4; Figure 5c\n  quote: when cue 2 was attended on ‘attribute’ trials, the currently attended cue 2 value subspace\n    correlated negatively with the stored cue 1 value subspace, representing the other option\n  criterion: The shared GLM and subspace correlation, OFC, cue 2 locked, 250 ms; T-statistics of EV\n    6 against EV 5. Pearson's test. Reproduced when r < 0 with p < 0.05.\n- id: fig5de-option-cue3-vs-stored\n  statement: In OFC, at cue 3 of option trials, the attended cue 3 value subspace correlates\n    negatively with both the stored cue 1 and the stored cue 2 value subspaces.\n  source: Results, Attention-guided value comparison in OFC, paragraph 4; Figure 5d and 5e\n  quote: when cue 3 was attended on ‘option’ trials, the stored cue 1 and stored cue 2 values both\n    represented the other option and were both negatively correlated with currently attended cue 3\n    value subspace\n  criterion: The shared GLM and subspace correlation, OFC, cue 3 locked, 250 ms; T-statistics of EV\n    3 against EV 1 and of EV 3 against EV 2. Pearson's test. Reproduced when both r < 0 with p <\n    0.05; partially reproduced when one is.\n- id: fig5f-option-stored-combined\n  statement: In OFC, at cue 3 of option trials, the stored cue 1 and stored cue 2 value subspaces\n    correlate positively, so the two previously attended cues are combined.\n  source: Results, Attention-guided value comparison in OFC, paragraph 4; Figure 5f\n  quote: However, these two stored subspaces were themselves positively correlated at cue 3 on\n    ‘option’ trials ( Fig. 5f ).\n  criterion: The shared GLM and subspace correlation, OFC, cue 3 locked, 250 ms; T-statistics of EV\n    1 against EV 2. Pearson's test. Reproduced when r > 0 with p < 0.05. The Discussion adds that\n    this did not occur at cue 2 (Figure 5f/h); the same correlation at cue 2, 250 ms, is reported.\n- id: fig5gj-cross-correlation-dynamics\n  statement: Cross-correlating the OFC value subspaces across time shows the same population\n    subspace shifting its value encoding from positive to negative as the subject saccades around\n    the screen.\n  source: Results, Attention-guided value comparison in OFC, paragraph 5; Figure 5g-j\n  quote: This reveals how the same OFC population subspace would dynamically shift its encoding of\n    values from positive to negative as the subject saccaded around the screen.\n  statistics:\n  - test: cluster-based permutation test, cluster-forming threshold |r| > 0.2, 1000 permutations\n    p: 0.001\n    p_relation: <\n    corrected: cluster-level, for multiple comparisons\n  depends_on:\n  - fig5c-attribute-cue2-vs-cue1\n  - fig5de-option-cue3-vs-stored\n  - fig5f-option-stored-combined\n  criterion: The shared GLM; for a pair of EVs, the Pearson correlation across OFC neurons of their\n    T-statistics at every pair of time points over the cue 1, 2 and 3 epochs (Methods,\n    Peri-stimulus correlation); clusters of |r| > 0.2, significance against the 99.9th percentile of\n    the largest cluster in 1000 permutations across neurons of one EV's T-statistics (Methods,\n    Statistical inference on cross-correlation). Which pairs the four panels show is in the missing\n    legend; the text ties 5g to 5c, 5h to 5f and 5i/5j to 5d/5e (Results, paragraph 5, and\n    Discussion, paragraph 4). Reading taken, the cross-correlation of the attended value EV of a\n    trial type with the stored value EVs (attribute trials, EV 6 against EV 5; option trials, EV 3\n    against EV 1, EV 3 against EV 2, EV 1 against EV 2). Reproduced when each of the four maps has a\n    significant cluster, of the sign of its Figure 5c-f correlation, covering the 250 ms point of\n    the relevant cue, and the attended value EV of the first map shows a significant positive\n    cluster with its own stored counterpart at the earlier cue.\n- id: fig5k-ofc-comparison-unique\n  statement: The value comparison correlations of Figure 5c-e are stronger in OFC than in DLPFC\n    (p = 0.040, 0.067, 0.011) and than in ACC (p = 0.003, 0.0003, 0.00013), by Fisher r-to-Z tests.\n  source: Results, Attention-guided value comparison in OFC, paragraph 6; Figure 5k\n  quote: 'revealed significantly stronger population encoding in OFC than in DLPFC (attribute trials:\n    VCue2 vs. VCue1, p = 0.040; option trials: VCue3 vs. VCue1, p = 0.067; VCue3 vs. VCue2, p =\n    0.011; Z-test after Fisher r-to-Z transformation) and in OFC than in ACC (attribute trials:\n    VCue2 vs. VCue1, p = 0.003; option trials: VCue3 vs. VCue1, p = 0.0003; VCue3 vs. VCue2, p =\n    0.00013)'\n  statistics:\n  - about: OFC against DLPFC, attribute trials, cue 2 value against cue 1 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.04\n    n: 183 OFC and 135 DLPFC neurons\n  - about: OFC against DLPFC, option trials, cue 3 value against cue 1 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.067\n    n: 183 OFC and 135 DLPFC neurons\n  - about: OFC against DLPFC, option trials, cue 3 value against cue 2 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.011\n    n: 183 OFC and 135 DLPFC neurons\n  - about: OFC against ACC, attribute trials, cue 2 value against cue 1 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.003\n    n: 183 OFC and 189 ACC neurons\n  - about: OFC against ACC, option trials, cue 3 value against cue 1 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.0003\n    n: 183 OFC and 189 ACC neurons\n  - about: OFC against ACC, option trials, cue 3 value against cue 2 value\n    test: Z-test after Fisher r-to-Z transformation\n    p: 0.00013\n    n: 183 OFC and 189 ACC neurons\n  depends_on:\n  - fig5c-attribute-cue2-vs-cue1\n  - fig5de-option-cue3-vs-stored\n  criterion: The three correlations of fig5c-attribute-cue2-vs-cue1 and fig5de-option-cue3-vs-stored\n    computed in each region, compared OFC against DLPFC and OFC against ACC by the Fisher r-to-Z\n    test of independent correlations (open detail O1). Reproduced when the OFC correlation is more\n    negative than the other region's in all six comparisons and at least five have p < 0.05 under\n    one reading, matching the paper's five of six; partially reproduced when all six go the\n    paper's way and three or four have p < 0.05.\n- id: figs67-no-comparison-acc-dlpfc\n  statement: ACC and DLPFC carry the currently attended value subspace (and stored subspaces) but\n    show no negative correlation between attended and stored value subspaces.\n  source: Results, Attention-guided value comparison in OFC, paragraph 6; Supplementary Figures 6\n    and 7\n  quote: Whilst the currently attended value subspace was present in DLPFC and ACC, value comparison\n    with stored cues was absent in these regions ( Fig 5k ; Figs. S6-7 ).\n  depends_on:\n  - fig5b-stable-attended-value-subspace\n  criterion: The analyses of fig5b, fig5c and fig5de, run on ACC and on DLPFC. The paper's test for a\n    single correlation is in the missing legends (Supplementary Figures 6 and 7 show lines of best\n    fit +/- 95% CI); Pearson's test at p < 0.05 two-sided is taken. Presence holds when the fig5b\n    correlation is positive at p < 0.05 in each region. Absence is judged on that test alone; it\n    holds when none of the three attended-against-stored correlations (EV 6 with EV 5 at cue 2; EV 3\n    with EV 1 and with EV 2 at cue 3) is negative with p < 0.05. Reproduced when presence and\n    absence hold in both regions; the six r values are reported either way.\n- id: fig6a-acc-belief-subspace\n  statement: In ACC the T-statistics of the four belief confirmation regressors (cues 2 and 3,\n    option and attribute trials) correlate positively with each other and with cue 1 value, a stable\n    belief confirmation code not present in OFC or DLPFC.\n  source: Results, Parallel ACC signals, paragraph 2; Figure 6a; Supplementary Figure 10\n  quote: We found that ACC population subspaces for each of these regressors were significantly\n    correlated with each other and also to cue 1 belief confirmation ( Fig. 6a / Fig. S10 ). As all\n    five regressors are defined at different parts of the trial, this reveals a stable population\n    code in ACC for accepting/rejecting the current belief, which was not present in OFC or DLPFC\n  criterion: The shared GLM; T-statistics of EV 13 and EV 14 at 300 ms after cue 2, EV 15 and EV 16\n    at 300 ms after cue 3, and cue 1 value (EV 1 + EV 5, 300 ms after cue 1; readings of the sum as\n    in fig5b) (Methods, Projection of ACC activity, paragraph 1); Pearson correlations across neurons\n    for the 10 pairs, in each region, at p < 0.05. Reproduced when all 10 ACC correlations are\n    positive with p < 0.05 and fewer than half of the 10 are positive with p < 0.05 in OFC and in\n    DLPFC; partially reproduced when all 10 ACC correlations are positive and at least 6 are\n    significant, with the OFC and DLPFC condition holding.\n- id: fig6b-acc-belief-stronger\n  statement: Virtually all belief confirmation correlations are stronger in ACC than in OFC and\n    DLPFC, and most of the individual comparisons are significant by Fisher r-to-Z.\n  source: Results, Parallel ACC signals, paragraph 2; Figure 6b\n  quote: Virtually all of these correlations were stronger in ACC than OFC/DLPFC ( Fig. 6b , right\n    panels), and the majority of individual comparisons were significant ( Fig 6b , left panels).\n  depends_on:\n  - fig6a-acc-belief-subspace\n  criterion: The 10 correlations of fig6a-acc-belief-subspace, ACC against OFC and ACC against\n    DLPFC, Fisher r-to-Z test of independent correlations (open detail O1), 20 comparisons.\n    \"Virtually all\" and \"the majority\" are read as at least 18 of 20 with the ACC correlation the\n    larger, and more than 10 of 20 at p < 0.05. Reproduced when both hold under one reading;\n    partially reproduced when only the first holds.\n- id: fig6c-belief-subspace-rt\n  statement: ACC activity in the belief confirmation subspace separates short from long reaction\n    time trials early in the trial, even at cue 1 presentation.\n  source: Results, Parallel ACC signals, paragraphs 3 and 4; Figure 6c (Methods call the\n    stimulus-locked panel 6B)\n  quote: First, activity in this subspace separated short from long RT trials relatively early\n    during the course of making a choice – even at the time of cue 1 presentation.\n  depends_on:\n  - fig6a-acc-belief-subspace\n  criterion: ACC neurons; the belief confirmation weight vector (open detail O7) from the GLM fit on\n    one half of trials, projected onto the cue 1 locked firing rates of the other half, averaged in\n    five reaction-time bins (open details O4, O5, O6), baseline corrected at cue 1 onset +/- 50 ms\n    (Methods, Projection of ACC activity). The paper gives no test and no window for \"at the time of\n    cue 1 presentation\"; readings of the window (a) 100-500 ms after cue 1, the cue 1 window of the\n    RSA; (b) 0-500 ms after cue 1. The direction is read from Results, paragraph 4 (confirmatory\n    evidence, faster responses), the shortest-RT bin above the longest. Reproduced when, under one\n    reading, the mean projection in the window is higher for the shortest than for the longest RT\n    bin and, with O4 reading (b), in at least 95 of the 100 splits; partially reproduced when the\n    separation appears only after cue 2.\n- id: fig6d-belief-ramp-to-choice\n  statement: Irrespective of reaction time, ACC activity in the belief confirmation subspace ramps up\n    shortly before the joystick movement.\n  source: Results, Parallel ACC signals, paragraph 4; Figure 6d (Methods call the response-locked\n    panel 6C)\n  quote: Second, irrespective of reaction time, ACC activity ramped shortly prior to joystick\n    movement ( Fig. 6d ). Activity within the belief confirmation subspace therefore became prominent\n    immediately prior to commitment to action, on all trials.\n  depends_on:\n  - fig6a-acc-belief-subspace\n  criterion: As fig6c-belief-subspace-rt, response locked, -500 to 100 ms around the response (the\n    GLM's response-locked range). The paper gives no test; \"ramped shortly prior\" is read as the mean\n    projection over -200 to 0 ms exceeding that over -500 to -300 ms. Reproduced when that holds in\n    each of the five RT bins under one reading of O4 to O7; partially reproduced for three or four\n    bins.\n- id: fig6e-action-subspace-ramp\n  statement: ACC activity in the left/right action selection subspace ramps up as evidence is\n    revealed and peaks immediately before the response.\n  source: Results, Parallel ACC signals, paragraph 5; Figure 6e (Methods call it 6D)\n  quote: Activity in the ACC action selection subspace also gradually ramped as evidence was\n    revealed about which option to choose, and peaked immediately prior to action selection ( Fig.\n    6e ).\n  criterion: ACC neurons; the action weight vector (EVs 17 and 18, 200 ms before response; open\n    detail O7) from one half of trials projected onto the other half, by RT bin, baseline corrected\n    at cue 1 onset (O4, O5, O6). The sign of the projection must follow the choice, which the\n    Methods do not spell out. Readings (a) left-choice minus right-choice trials averaged separately\n    per RT bin and differenced; (b) rates of right-choice trials multiplied by -1 before averaging.\n    No test is given. Reproduced when, under one reading, in each RT bin the response-locked\n    projection rises over -500 to 0 ms (mean over -200 to 0 ms above that over -500 to -300 ms) and\n    its maximum over -500 to 100 ms falls between -200 and 100 ms.\n- id: fig7a-ofc-value-difference-neurons\n  statement: At all three time points (cue 2 against cue 1, cue 3 against cue 1, cue 3 against cue\n    2), a greater proportion of single neurons encoded value difference between attended and\n    unattended cues in OFC than in ACC and DLPFC.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    2; Figure 7a\n  quote: At all three relevant timepoints, we found that a greater proportion of single neurons\n    passed these criteria in OFC than in ACC/DLPFC ( Fig. 7a ).\n  criterion: The shared GLM. A neuron passes when the contrast (attended value) - (unattended value)\n    is significant and both coefficients are significant with opposite signs (Results, paragraph 2);\n    open details O2 and O3. The trial type of the cue 3 tests is open; the text says \"at cue 3 of\n    attribute trials\" but cites Figure 5d/e, which are option trials. Readings (a) as Figure 5 (cue 2\n    of attribute trials, EV 6 against EV 5; cue 3 of option trials, EV 3 against EV 1 and EV 3\n    against EV 2); (b) as written, cue 3 of attribute trials with the attended value EV 7 or EV 9 by\n    third saccade, tested against EV 5 and EV 6 separately for each saccade direction, a neuron\n    passing in either. The paper's test between regions is in the missing legend; the direction is\n    judged, and pairwise chi-square tests are reported. Reproduced when the OFC proportion exceeds\n    both the ACC and the DLPFC proportion at all three time points, under one reading of O3 and the\n    trial type, at both readings of O2.\n- id: fig7b-ofc-value-difference-any\n  statement: Collapsed across the three tests, the fraction of neurons passing the value difference\n    criteria at any of the three cues is greater in OFC than in ACC and DLPFC.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    2; Figure 7b\n  quote: We collapsed across these three tests to show the fraction of single neurons passing these\n    criteria at any of the three cues individually ( Fig. 7b ).\n  depends_on:\n  - fig7a-ofc-value-difference-neurons\n  inferred: The sentence describes the panel; that OFC's fraction is the largest is read from the\n    preceding sentence of the paragraph, which the panel summarises.\n  criterion: As fig7a-ofc-value-difference-neurons, a neuron counted when it passes at any of the\n    three time points. Reproduced when the OFC fraction exceeds the ACC and the DLPFC fractions under\n    the reading that fig7a uses.\n- id: fig7c-acc-belief-neurons\n  statement: At all four time points, a greater proportion of single neurons significantly encoded\n    belief confirmation in ACC than in OFC or DLPFC.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    3; Figure 7c\n  quote: At all four timepoints, there was a greater proportion of single neurons significantly\n    encoding belief confirmation in ACC than in OFC or DLPFC ( Fig. 7c ).\n  criterion: The shared GLM; per neuron, whether the coefficient of each of EVs 13, 14 (after cue 2)\n    and 15, 16 (after cue 3) is significant; open details O2 and O3 (the 300 ms reading matches the\n    times the Methods give for these EVs in Figure 6A). The paper's test between regions is in the\n    missing legend; the direction is judged, and pairwise chi-square tests are reported. Reproduced\n    when the ACC proportion exceeds both others for all four EVs under one reading of O3, at both\n    readings of O2; partially reproduced for three of four.\n- id: fig8-cue1-value-all-regions\n  statement: At cue 1, a significant fraction of neurons in all three regions encoded the cue's\n    value irrespective of its attribute, action or spatial position.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    4; Figure 8\n  quote: Across all three regions, a significant fraction of neurons encoded Cue 1’s value,\n    irrespective of the cue’s attribute, action or spatial position ( Fig. 8 ; binomial test, all\n    p<1*10 7 ).\n  statistics:\n  - test: binomial test\n    p: 1.0e-07\n    p_relation: <\n    n: 189 ACC, 135 DLPFC and 183 OFC neurons, each region tested\n  criterion: The cue 1 regression is not described in the Online Methods; the Results say the cue's\n    value, action value, attribute value and spatial value were entered in one model. Its regressors\n    are open. Readings (a) value (rank -2 to 2), value x side (left 1, right -1), value x attribute\n    (probability 1, magnitude -1), value x row (top 1, bottom -1), with the main effects of side,\n    attribute and row and a constant; (b) the four value regressors and a constant only. The window\n    for the fractions of Figure 8a is open; readings (i) 100-500 ms after cue 1, the RSA window; (ii)\n    the 200 ms bin at 250 ms; (iii) the bin at 300 ms. Trials, open detail O9; significance level,\n    O2; the binomial test against a chance rate equal to that level. Reproduced when, under one\n    reading, the fraction significant for value is above chance with p < 1e-7 in each region.\n- id: fig8-action-value-acc-dlpfc\n  statement: About 18% of ACC and DLPFC neurons encoded left/right action value at cue 1, above\n    chance and more than OFC, which encoded action value at chance level.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    5; Figure 8\n  quote: First, a significant subset of ACC and DLPFC neurons (~18%) preferentially responded to the\n    values of either left or right options (binomial test, both p<1*10 -5 ). Both of these\n    populations were significantly greater than OFC, which encoded action value at chance level\n    (pairwise Chi 2 test, ACC vs. OFC: p=0.002, DLPFC vs. OFC: p=0.003).\n  statistics:\n  - about: ACC and DLPFC action value fractions against chance\n    test: binomial test\n    p: 1.0e-05\n    p_relation: <\n  - about: ACC against OFC\n    test: pairwise Chi2 test\n    p: 0.002\n  - about: DLPFC against OFC\n    test: pairwise Chi2 test\n    p: 0.003\n  expected:\n  - quantity: fraction of ACC neurons with action value\n    value: 18\n    tolerance: 1.8\n    unit: '%'\n  - quantity: fraction of DLPFC neurons with action value\n    value: 18\n    tolerance: 1.8\n    unit: '%'\n  depends_on:\n  - fig8-cue1-value-all-regions\n  criterion: The regression and readings of fig8-cue1-value-all-regions, the value x side\n    regressor. Reproduced when, under one reading, both fractions are within tolerance, each is above\n    chance by binomial test at p < 1e-5, each exceeds OFC by chi-square at p < 0.05, and the OFC\n    fraction is not above chance by binomial test at p < 0.05 (the absence is judged on that test).\n    Partially reproduced when all tests hold but a fraction is outside tolerance.\n- id: fig8-spatial-value-dlpfc\n  statement: In DLPFC, top/bottom spatial value neurons are as prevalent as left/right action value\n    neurons, while in ACC they are significantly fewer, so DLPFC encodes value by spatial position\n    and ACC by action.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    6; Figure 8\n  quote: In DLPFC, such a relationship held: an equally prevalent population of top-bottom ‘spatial\n    value’ neurons was observed as left-right ‘action value’ neurons (binomial test, p<1*10 -6 ). In\n    ACC, this population was significantly smaller than the left-right value population (pairwise\n    Chi 2 test p=0.03).\n  statistics:\n  - about: DLPFC spatial value fraction against chance\n    test: binomial test\n    p: 1.0e-06\n    p_relation: <\n  - about: ACC spatial value against action value fractions\n    test: pairwise Chi2 test\n    p: 0.03\n  depends_on:\n  - fig8-action-value-acc-dlpfc\n  criterion: The regression and readings of fig8-cue1-value-all-regions, the value x row regressor\n    against the value x side regressor. Reproduced when, under one reading, the DLPFC spatial value\n    fraction is above chance by binomial test at p < 1e-6 and does not differ from the DLPFC action\n    value fraction by the pairwise chi-square test at p < 0.05 (the absence judged on that test),\n    and the ACC spatial value fraction is smaller than the ACC action value fraction by that test at\n    p < 0.05.\n- id: fig8-attribute-value-ofc\n  statement: About 24% of OFC neurons encoded attribute value at cue 1 (preferring probability or\n    magnitude cues), above chance and more than in ACC or DLPFC.\n  source: Results, Single neuron analyses recapitulate core findings at population level, paragraph\n    7; Figure 8\n  quote: we found a significant proportion of neurons in OFC (~24%) reflected attribute value\n    (binomial test, p<1*10 7 ) ... This proportion was significantly greater than the representation\n    of attribute value coding in either ACC or DLPFC (pairwise Chi 2 tests, OFC vs. ACC: p=0.001,\n    OFC vs. DLPFC: p=0.014).\n  statistics:\n  - about: OFC attribute value fraction against chance\n    test: binomial test\n    p: 1.0e-07\n    p_relation: <\n  - about: OFC against ACC\n    test: pairwise Chi2 test\n    p: 0.001\n  - about: OFC against DLPFC\n    test: pairwise Chi2 test\n    p: 0.014\n  expected:\n  - quantity: fraction of OFC neurons with attribute value\n    value: 24\n    tolerance: 2.4\n    unit: '%'\n  depends_on:\n  - fig8-cue1-value-all-regions\n  criterion: The regression and readings of fig8-cue1-value-all-regions, the value x attribute\n    regressor. Reproduced when, under one reading, the OFC fraction is within tolerance, above chance\n    by binomial test at p < 1e-7, and greater than the ACC and DLPFC fractions by chi-square at p <\n    0.05. Partially reproduced when the tests hold but the fraction is outside tolerance.\n- id: figs9-ev16-correlation\n  statement: The GLM's regressors of interest are decorrelated by design except EV 16, whose mean r2\n    with EVs 7 and 9 is 0.167 and 0.194.\n  source: Online Methods, General linear model, EV 16 paragraph; Supplementary Figure 9\n  quote: there existed some positive correlation between EV16 and EVs 7 and 9 (mean r 2 of 0.167 and\n    0.194 respectively, see Figure S9 )\n  expected:\n  - quantity: mean r2 of EV 16 with EV 7\n    value: 0.167\n    tolerance: 0.0167\n  - quantity: mean r2 of EV 16 with EV 9\n    value: 0.194\n    tolerance: 0.0194\n  criterion: The GLM design (EVs 1-18 on trials with 3 or more cues viewed). Over what the mean is\n    taken is not stated. Readings (a) over sessions; (b) over neurons, each with its own session's\n    trials. The legend's \"most EVs of interest (1-6, 13-18) are decorrelated ... with the exception\n    of EV16\" is judged as every other pair among EVs 1-6 and 13-18 having mean r2 below 0.167.\n    Reproduced when both values are within tolerance and that holds, under one reading.\n- id: figs11-alternative-value-template\n  statement: Replacing the attended value and left/right value templates by a uniform-diagonal form\n    (negative absolute value difference) gives qualitatively the same functional dissociation across\n    OFC, DLPFC and ACC.\n  source: Supplementary Note, paragraph 1; Supplementary Figure 11\n  quote: such a regressor to analyse the data in main Figure 4 yields a similar functional\n    dissociation between OFC, DLPFC and ACC for ‘attended value’ and ‘left/right value’\n  depends_on:\n  - fig4f-ofc-attended-value\n  - fig4g-left-right-value\n  criterion: The template regression of fig4f and fig4g with attended value replaced by -|rank(i) -\n    rank(j)| and left/right value by the same on the same side and 0 across sides (Supplementary\n    Note), normalised by maximum absolute value; permutation test as in the Methods. Reproduced when\n    the outcomes of fig4f-ofc-attended-value and fig4g-left-right-value hold with these templates.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The file failed to parse because three quotes contain a colon followed by a space. I'm putting those three in single quotes.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import re
p='claims/hunt-2018.yaml'
s=open(p).read()
lines=s.split('\n')
out=[];i=0
while i<len(lines):
    l=lines[i]
    m=re.match(r'^(\s*)(quote|statement|criterion|inferred|source): (.*)$',l)
    if m and not m.group(3).startswith(("'",'"')):
        ind=len(m.group(1))
        block=[m.group(3)];j=i+1
        while j<len(lines) and lines[j].startswith(' '*(ind+2)) and not re.match(r'^\s*[a-z_]+: ',lines[j][ind:]) :
            block.append(lines[j]);j+=1
        joined=' '.join(x.strip() for x in block)
        if ': ' in joined or joined.endswith(':'):
            out.append(f"{m.group(1)}{m.group(2)}: '"+block[0].replace("'","''"))
            for b in block[1:-1]: out.append(b.replace("'","''"))
            if len(block)>1: out.append(block[-1].replace("'","''")+"'")
            else: out[-1]+="'"
            print('quoted',m.group(2),'at line',i+1)
            i=j;continue
    out.append(l);i+=1
open(p,'w').write('\n'.join(out))
EOF
python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/hunt-2018.yaml",
 "old_string": "  inferred: The sentence describes the panel; that OFC's fraction is the largest is read from the\n    preceding sentence of the paragraph, which the panel summarises.\n",
 "new_string": ""
}
```

```
The file claims/hunt-2018.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt; grep -n "—\|rather" claims/hunt-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='claims/hunt-2018.yaml'
s=open(p).read()
s=s.replace("Choice accuracy based upon the pictures observed , rather than the true expected value, was\n    substantially higher","Choice accuracy based upon the pictures observed ... was substantially higher")
s=s.replace("This\n    indicates that DLPFC activity primarily represents spatial position rather than simply\n    left/right action","This\n    indicates that DLPFC activity primarily represents spatial position")
open(p,'w').write(s)
EOF
grep -n "rather\|—" claims/hunt-2018.yaml; python tools/claims_check.py claims/hunt-2018.yaml paper/10.1038-s41593-018-0239-5.txt; grep -c "^- id" claims/hunt-2018.yaml; grep -c "criterion:" claims/hunt-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/hunt-2018.yaml`: 40 claims, all with quotes, 39 with criteria and 16 statistics entries. The quote checker passes every quote. It flags two "value not found" problems, which I checked by reading and are not wrong: the extracted text prints "p<1*10 7" for p < 1e-7 (the minus sign was lost). I did not commit.

**Text read.** The version of record (PMC6331040, open access) as text: main text, Discussion and Online Methods. It also had the supplement (Supplementary Figures 1 to 12, Supplementary Table 1 and the Supplementary Note). The data descriptor was read only to learn what the dataset holds.

**Missing from the paper text:**
- **Main figure legends.** The flattened text has no legends for Figures 1 to 8, and no PDF of the main article was supplied. So each figure's tests, significance levels and sample sizes are unknown. Claims on main figures rest on the Results and Methods sentences that cite them, and the gaps are named as open details.
- **Code.** The paper's MATLAB scripts are stored inside the CRCNS dataset, so I did not read them and record no commit. The author may settle open details from them.
- **The Figure 8 cue 1 regression.** The Online Methods do not describe this model.

**Coverage.** The claims cover:
- behaviour: session and trial counts, choice accuracy, cue weights, information sampling biases (Figure 2a/b);
- neuron counts;
- the cue 1 RSA: five templates, consistency across monkeys, the top/bottom split, t75 latencies and their order, the alternative template;
- OFC value subspaces (Figure 5a to 5k, Supplementary Figures 6 and 7);
- the ACC belief-confirmation subspace and the reaction-time, ramp and action projections (Figure 6a to 6e);
- single-neuron fractions (Figures 7 and 8);
- regressor correlations (Supplementary Figure 9).

**Open details and the readings named:**
- **O1, Fisher r-to-Z test:** two-sided, or one-sided in the predicted direction.
- **O2, significance level for counting single neurons:** p < 0.05 or p < 0.01.
- **O3, time bin for single-neuron tests at cues 2 and 3:** 250 ms after the cue (as Figure 5) or 300 ms (as Figure 6a).
- **O4, how trials are split for the Figure 6 projections:** the Methods say odd against even trials; the Results say 100 random half splits.
- **O5, the five reaction-time bins:** quintiles within each session, or quintiles of all of a monkey's sessions.
- **O6, the firing rates projected:** raw rates, or rates z-scored per neuron.
- **O7, the "T-statistics of contrasts" used as weights:** the mean of the T-statistics, or the T-statistic of the mean coefficient.
- **O8, the RSA permutation test:** one-sided or two-sided.
- **O9, trials used for RSA and the Figure 8 regression:** all completed option and attribute trials, or only those with 3 or more cues viewed.

**Open details for single claims:**
- **Figure 8 model:** its regressors (with or without main effects) and its window (100–500 ms, or the bin at 250 ms or 300 ms).
- **Figure 7a trial type:** the text says attribute trials but cites Figure 5d/e, which are option trials. Both are named.
- **Accuracy measures:** how trials of equal value count, and how value is judged from the pictures observed.
- **Cue weights:** what "approximately equal weight" means (overlapping intervals, or a Wald test).
- **Value difference:** true expected value, or that implied by cues 1 and 2.
- **Latencies:** the RSA sliding-window step (10 ms or 1 ms).
- **Supplementary Figure 9:** whether the mean r² is over sessions or over neurons.
- **Figure 6:** the projection windows, and how the action projection is signed.
- **Figure 5g–j:** which pairs of regressors each panel shows.
- **Figure 2b:** whether the monkeys are pooled or analysed separately.

**Inconsistencies recorded in the claims.** Supplementary Table 1 sums to 198 ACC, 195 OFC and 156 DLPFC units, which are the counts before the below-1 Hz exclusion even though its caption says above 1 Hz. It also lists 29 and 24 sessions, against the 32 and 25 behavioural sessions. The Methods and Results label the Figure 6 panels differently.

## End of run

21 turns, 7 minutes, $2.06 at API prices, result: success.
