# crcns-ia-1 · claims-check · run 41883945244

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/crcns-ia-1/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/crcns-ia-1/*.yaml; python tools/claims_check.py claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml paper/10.3389-neuro.10.003.2008.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md
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
are enough to know which paper and which experiments it is meant to hold. A
data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
documentation) is a longer description, to be read for that alone; it is not
the paper, and no claim comes from it.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml paper/10.3389-neuro.10.003.2008.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml"
}
```

```
1	# Claims for Eyherabide, Rokem, Herz & Samengo (2008), "Burst firing is a neural code in an
2	# insect auditory system", Frontiers in Computational Neuroscience, on CRCNS data set ia-1
3	# (doi:10.6080/K0BG2KWB).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-04, protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record in PubMed Central (PMC2525941, open access), from Europe PMC
8	# full-text XML, as supplied under paper/, with its Materials and Methods, Results, Discussion,
9	# the legends of Figures 1 to 10 and Table 1. No PDF was supplied, so values shown only in
10	# figures (Figure 5, Figure 9B and the population histograms of Figure 7) could not be read.
11	# The paper has no supplement. It links no analysis code, so none was read. Some passages are
12	# garbled in the text and are named in the claims that use them (Results, Quantitative
13	# description, paragraph 7, "no <69%"; Qualitative description, paragraph 5, a ratio of
14	# sigma to itself).
15	#
16	# Data the paper used. Adult Locusta migratoria, intracellular recordings from auditory
17	# receptor axons in the tympanal nerve; 37 receptor cells from 23 animals. Each cell was tested
18	# with two or more stimuli, 132 sessions in all (a session is one cell in one stimulus
19	# condition), of which 86 passed the selection (mean rate near 100 Hz, trial-to-trial SD of the
20	# firing rate below 35 Hz). Stimuli were amplitude-modulated sine carriers at the cell's best
[... 767 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; cat -n paper/10.3389-neuro.10.003.2008.txt | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/eac031e5-0dc6-4429-874a-969af245e096/tool-results/b4t168g46.txt"
}
```

```
1	 99756 paper/10.3389-neuro.10.003.2008.txt
2	 12840 paper/ia-1.data-description.txt
3	112596 total
4	     1	DOI: 10.3389/neuro.10.003.2008
5	     2	Version: version of record, PMC2525941 (open access)
6	     3	Source: europepmc fullTextXML
7	     4	Stored: 2026-11-04
8	     5	Extracted: JATS XML flattened
9	     6	------------------------------------------------------------------------
10	     7	Burst Firing is a Neural Code in an Insect Auditory System
11	     8	
12	     9	Various classes of neurons alternate between high-frequency discharges and silent intervals. This phenomenon is called burst firing. To analyze burst activity in an insect system, grasshopper auditory receptor neurons were recorded in vivo for several distinct stimulus types. The experimental data show that both burst probability and burst characteristics are strongly influenced by temporal modulations of the acoustic stimulus. The tendency to burst, hence, is not only determined by cell-intrinsic processes, but also by their interaction with the stimulus time course. We study this interaction quantitatively and observe that bursts containing a certain number of spikes occur shortly after stimulus deflections of specific intensity and duration. Our findings suggest a sparse neural code where information about the stimulus is represented by the number of spikes per burst, irrespective of the detailed interspike-interval structure within a burst. This compact representation cannot be interpreted as a firing-rate code. An information-theoretical analysis reveals that the number of spikes per burst reliably conveys information about the amplitude and duration of sound transients, whereas their time of occurrence is reflected by the burst onset time. The investigated neurons encode almost half of the total transmitted information in burst activity.
13	    10	
14	    11	## Introduction
15	    12	
16	    13	Tonic and burst firing encode different aspects of the sensory world. Specifically, in thalamic
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '200,400p' paper/10.3389-neuro.10.003.2008.txt | grep -v '^$'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/eac031e5-0dc6-4429-874a-969af245e096/tool-results/b1ikf8ct2.txt",
 "offset": 40
}
```

```
40	Population average of the probability of generating n -bursts, as a function of the stimulus cutoff frequency, for all SD = 6 dB stimuli (A) and as a function of standard deviation, for all stimuli with a cutoff frequency of 200 Hz (B) . Error bars represent the standard deviation in the population. High- n -bursts appear most frequently for stimuli with large amplitude modulations and cutoff frequencies around 100 Hz. Stimulus properties thus have a noticeable influence on the probability of generating bursts.
41	In the present approach, a spike sequence is classified as an n -burst by analyzing the statistical properties of the response. There are no dynamical explanations in terms of specific ionic currents. Actually, though we lack a detailed characterization of the ionic currents involved in action potential generation, previous studies suggest that grasshopper receptors do not burst intrinsically; cells fire tonically for time-independent stimuli (Gollisch et al., 2002 ) and do not show burst activity at the onset of step-like stimuli (Gollisch and Herz, 2004 ). In addition, adaptation effects as well as spike-time variability can be explained on a quantitative level with models that do not contain intrinsic burst mechanisms (Benda et al., 2001 ; Gollisch and Herz, 2004 ; Schaette et al., 2005 ). These results underscore that in the presence of time-dependent stimuli, even cells that do not burst by themselves may generate responses whose statistical properties are highly reminiscent of intrinsically bursting cells. Agüera y Arcas et al. ( 2003 ) and Keat et al. ( 2001 ) present similar examples in simulated data. In these cases, burst-like responses arise as a consequence of the interplay between the dynamical properties of the neuron and particular temporal structures in the stimulus. To assess whether even cells with very simple dynamics can exhibit burst activity when driven by the proper stimulus, we modeled the time evolution of a threshold-linear Poi
[... 53 more lines not kept]
```

**Agent**

The checker passes. I've read the paper and all 26 claims. Next I'm checking the schema for how expected values and statistics are written, then I'll edit.

**Agent calls Bash**

```bash
ls tools/ docs/; grep -n "relation\|bound\|expected" tools/claims_check.py | head -40; ls schema* docs/*schema* 2>/dev/null
```

```
Exit code 2
docs/:
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

tools/:
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | grep -n -A3 '"expected"\|"relation"\|"checks"\|"changes"\|"ready"\|"kind"\|"bound"\|"comparison"' | head -80
```

```
87:     "kind": {
88-      "description": "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.",
89-      "enum": [
90-       "finding",
--
104:     "expected": {
105-      "description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.",
106-      "oneOf": [
107-       {
--
166:        "kind": {
167-         "const": "link"
168-        }
169-       },
--
171:        "kind"
172-       ]
173-      },
174-      "then": {
--
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'] if '\$defs' in s else s.get('definitions'),indent=1))" | sed -n '1,80p'
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
[... 60 more lines not kept]
```

**Agent**

Now the edits. Statistics first: the ANOVA and t-test thresholds in fig8 and fig9 are used to count cells, so they are methods, not results.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    50 exhibit n BTAs whose central peaks were significantly different from one another\n  statistics:\n  - about: nBTAs for n = 1 to 4, per session, frequency domain\n    test: two-way ANOVA (frequency band and burst order) on real and imaginary parts\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: nBTA against each other nBTA at each time point\n    test: Student's t-test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:",
 "new_string": "    50 exhibit n BTAs whose central peaks were significantly different from one another\n  depends_on:"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    diminishes.\n  statistics:\n  - about: nBTA against the convolved 1BTA, per session and n\n    test: two-way ANOVA on real and imaginary Fourier parts\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:",
 "new_string": "    diminishes.\n  depends_on:"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  statement: In every bursting cell the burst-triggered averages for n = 1 to 4 differ\n    significantly, their central peaks growing higher and wider with n; 50 of the 58 bursting\n    sessions show significantly different central peaks in the time domain, the other eight\n    having too few bursts.",
 "new_string": "  statement: In every bursting cell the burst-triggered averages for n = 1 to 4 differ\n    significantly (in the example cell their central peaks grow higher and wider with n); 50\n    of the 58 bursting sessions show significantly different central peaks in the time domain,\n    the other eight having too few bursts."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  - quantity: correlation between the two information rates over sessions\n    value: 0.95\n    tolerance: 0.05",
 "new_string": "  - quantity: correlation between the two information rates over sessions\n    value: 0.95\n    tolerance: 0.095"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "non-bursting sessions treated as all 1-bursts. \"All sessions\" is read as (a) the 86 kept\n    sessions, (b) the bursting sessions. The tolerance of R is 0.05 since 10% would allow\n    values above 1. Reproduced",
 "new_string": "non-bursting sessions treated as all 1-bursts. \"All sessions\" is read as (a) the 86 kept\n    sessions, (b) the bursting sessions. Reproduced"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    Readings for \"systematically\"\n    are (a) tau_n decreasing from n = 1 to n = 4 in the majority of bursting sessions with\n    bursts up to n = 4; (b) the mean over those sessions of tau_n decreasing from n = 1 to 4.\n    Reproduced when both readings hold; partially reproduced when one does.",
 "new_string": "    Readings for \"systematically\"\n    are (a) tau_n decreasing from n = 1 to n = 4 in the majority of bursting sessions with\n    bursts up to n = 4; (b) the mean over those sessions of tau_n decreasing from n = 1 to 4.\n    Reproduced when, under one reading, tau_n decreases from n = 1 to 4; both are shown."
}
```

```
<tool_use_error>String to replace not found in file.
String:     Readings for "systematically"
    are (a) tau_n decreasing from n = 1 to n = 4 in the majority of bursting sessions with
    bursts up to n = 4; (b) the mean over those sessions of tau_n decreasing from n = 1 to 4.
    Reproduced when both readings hold; partially reproduced when one does.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  statement: The standard deviation of the stimuli preceding an n-burst has a minimum about 7 ms\n    before burst onset, at a position nearly the same for all n; over the bursting cells the SD\n    of the minimum's position across n = 1 to 4 averages 0.4 ms (SD 0.7 ms).",
 "new_string": "  statement: The standard deviation of the stimuli preceding an n-burst has a minimum at a\n    position nearly the same for all n (about 7 ms before burst onset in the example cell, with\n    an SD of 0.33 ms across n); over the bursting cells the SD of the minimum's position across\n    n = 1 to 4 averages 0.4 ms (SD 0.7 ms), roughly 0.05 times the inverse cutoff frequency."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    value: 0.4\n    tolerance: 0.7\n    unit: ms\n  criterion: sigma_n(tau) by Eq. 14, its minimum searched over -25 to 0 ms (the window of the\n    nBTA analysis before onset). Sessions with bursts of all four n. Reproduced when the value\n    is within tolerance.",
 "new_string": "    value: 0.4\n    tolerance: 0.7\n    unit: ms\n  - quantity: mean over bursting sessions of the SD across n of the position of the minimum of\n      sigma_n, times the cutoff frequency\n    value: 0.05\n    tolerance: 0.005\n  criterion: sigma_n(tau) by Eq. 14. The window searched for the minimum is not stated;\n    readings (a) -25 to 0 ms, (b) -25 to +15 ms, the window of the nBTA analysis (Methods,\n    Estimation of burst-triggered averages, paragraph 2). Sessions with bursts of all four n.\n    Reproduced when, under one reading, the 0.4 ms value is within tolerance; the 0.05 value\n    (\"roughly\") is reported and judged with it, and the claim is partially reproduced when\n    only one of the two is within tolerance."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  expected:\n    quantity: mean over bursting sessions of the SD across n of the position of the minimum of\n      sigma_n\n    value: 0.4",
 "new_string": "  expected:\n  - quantity: mean over bursting sessions of the SD across n of the position of the minimum of\n      sigma_n\n    value: 0.4"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    Reproduced when both readings hold; partially reproduced when one does.",
 "new_string": "    Reproduced when, under one reading, tau_n decreases from n = 1 to 4; both are shown."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    seven protocols at p < 0.05; reproduced when it is not significant, with the\n    F statistic and p reported. The paper does not say whether the 86 kept sessions or all\n    sessions were tested; the kept sessions are the main reading, as the sentence follows\n    their selection.",
 "new_string": "    seven protocols at p < 0.05; reproduced when it is not significant, with the\n    F statistic and p reported. The paper does not say whether the 86 kept sessions or all\n    132 were tested; the rate sentence comes before the SD selection in paragraph 4, and the\n    paragraph's last sentence counts the 86 as fulfilling both conditions. Readings (a) the 86\n    kept sessions, (b) all sessions; both are shown."
}
```

```
<tool_use_error>String to replace not found in file.
String:     seven protocols at p < 0.05; reproduced when it is not significant, with the
    F statistic and p reported. The paper does not say whether the 86 kept sessions or all
    sessions were tested; the kept sessions are the main reading, as the sentence follows
    their selection.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  - quantity: mean trials per session\n    value: 172\n    tolerance: 17.2",
 "new_string": "  - quantity: mean trials per session\n    value: 172\n    tolerance: 17.2\n  - quantity: population average of the trial-to-trial SD of the firing rate\n    value: 6\n    tolerance: 0.6\n    unit: Hz"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    are read (a) over the 86 kept sessions, (b) over all sessions. Reproduced when every\n    value is within tolerance under one reading.",
 "new_string": "    and the average SD of 6 Hz (paragraph 4, in parentheses) are read (a) over the 86 kept\n    sessions, (b) over all sessions. Reproduced when every value is within tolerance under one\n    reading."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  inferred: The numbers are read from Table 1; no sentence states them.\n  depends_on:\n  - data-sessions-and-trials",
 "new_string": "  inferred: The numbers are read from Table 1; no sentence states them. The legend calls the\n    row recorded sessions; the counts sum to 86, so they are read as the kept sessions.\n  depends_on:\n  - data-sessions-and-trials"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "  criterion: C_s(tau) by Eq. 1, 0.1 ms bins. The paper shows one sample cell tested with the\n    whole set of stimuli, while its Methods say each cell had two stimuli; the cell is not\n    identified. Reproduced when a cell with all seven stimuli is found and its correlation\n    functions show the described ordering (peak height of the first peak over its baseline\n    increasing with SD; more than one peak at 25 Hz, one peak at 100 and 200 Hz, no separable\n    first peak at 400 or 800 Hz under the Burst identification test).",
 "new_string": "  criterion: C_s(tau) by Eq. 1, 0.1 ms bins. The paper shows one sample cell tested with the\n    whole set of stimuli (Methods paragraph 1 says two or more stimuli per cell, paragraph 3\n    two); the cell is not identified. Paragraph 4 names Figures 3 B to D and G as having a\n    separable first peak and 3 A, E and F as unimodal. \"Sharper peaks\" is not defined;\n    readings (a) a higher first peak over its baseline, (b) a narrower first peak. Reproduced\n    when a cell with all seven stimuli is found and, under one reading, its correlation\n    functions show the described ordering (sharper first peak with increasing SD; more than\n    one peak at 25 Hz, a single peak at 100 and 200 Hz, no separable first peak at 3 dB, 400\n    or 800 Hz under the Burst identification test)."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    one reading, P(n = 1) is lowest at 100 Hz among the cutoffs and at 12 dB among the SDs.\n    The figure's values cannot be read from the text, so only this ordering is judged.",
 "new_string": "    one reading, P(n = 1) is lowest at 100 Hz among the cutoffs and at 12 dB among the SDs.\n    The figure's values cannot be read from the text, so only this ordering is judged; the\n    ordering of P(n = 2) and P(n = 3), from the legend's sentence on high-n bursts, is shown."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "sessions were tested; the kept sessions are the main reading, as the sentence follows\n    their selection.",
 "new_string": "sessions were tested; the rate sentence comes before the SD selection in paragraph 4, and\n    the paragraph's last sentence counts the 86 as fulfilling both conditions. Readings (a)\n    the 86 kept sessions, (b) all sessions; both are shown."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    are the filter length T, read as (a) 25 ms (the nBTA window before a burst) and (b) 50 ms,\n    and the filter's scale,",
 "new_string": "    are the filter length, which Eq. 2 writes as T, the symbol the Methods define as the\n    duration of the AM signal, read as (a) T as defined there (the cross-correlation over all\n    lags of the 200 to 1000 ms analysis window) and (b) truncated at 25 ms (the nBTA window\n    before a burst, Methods, Estimation of burst-triggered averages), and the filter's scale,"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    1000 ms (Eq. 10), r_n(t) the trial-averaged rate of n-burst onsets. The Methods do not",
 "new_string": "    1000 ms (Eq. 10), r_n(t) the trial-averaged rate of n-burst onsets. Read literally, Eq. 10\n    gives I_n(1) in bit seconds, while the text says the slopes are in bits and Eq. 3 (the\n    per-event information of Brenner et al., 2000, garbled in the text) carries a factor\n    1 / T; readings for I_n(1) are (i) (1 / T) times the integral of (r_n / rbar_n) log2(r_n /\n    rbar_n), bits per event, (ii) Eq. 10 as printed, differing by the factor T = 0.8 s. The\n    Methods do not"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    log, (c) log10. Significance as in",
 "new_string": "    log, (c) log10. The Figure 7C legend says number of occurrences where the text says\n    frequency of occurrence; on a log scale the two give the same slope. Significance as in"
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "old_string": "    bursting sessions of protocol 5 (6 dB, 100 Hz). Reproduced when the central peak of the\n    average is higher or wider (width at half height) for 2 than for 1 and for 3 than for 2.",
 "new_string": "    bursting sessions of protocol 5 (6 dB, 100 Hz). The paper does not define the width;\n    readings (a) full width at half height, (b) the interval between the two minima flanking\n    the central maximum, as the Methods use for Figure 9. Reproduced when, under one reading,\n    the central peak of the average is higher or wider for 2 than for 1 and for 3 than for 2."
}
```

```
The file claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cat >> claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml <<'EOF'
checks:
- date: 2026-11-04
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig8-nbta-differ, removed the two statistics entries (ANOVA and t-test at p < 0.01); they are significance levels used to count sessions, a method kept in the criterion, not results.
  - fig9-nbta-not-concatenated-1bta, removed the ANOVA statistics entry for the same reason.
  - fig8-nbta-differ, the statement said every bursting cell has central peaks growing higher and wider with n; the paper shows this for the example cell (paragraph 3) and says in paragraph 6 that not all cells do, so the statement now limits it to the example cell.
  - direct-method-comparison, tolerance of R restored to the default 10% (0.095); the stated reason (values above 1) does not justify narrowing the lower side.
  - fig8-latency-decreases, the criterion required both readings to hold; per protocol it is reproduced under any one reading, now so.
  - fig8e-sigma-minimum, the statement gave the 7 ms minimum as a population result; it is the example cell's (Figure 8E, paragraph 4), now said, with that cell's 0.33 ms. Added the paper's second population value (0.05 times the inverse cutoff) as an expected value. The search window for the minimum was presented as fixed; it is not stated, now two readings.
  - firing-rate-uniform, the criterion's reason for the kept-sessions reading was wrong (the rate sentence precedes the SD selection); now both populations are readings.
  - data-sessions-and-trials, added the reported population average of the trial-to-trial rate SD (6 Hz, Methods paragraph 4) as an expected value.
  - table1-sessions-per-protocol, the inferred note now says why the legend's recorded sessions are read as the 86 kept ones (the counts sum to 86).
  - fig3-correlation-shape, the criterion said Methods give two stimuli per cell; paragraph 1 says two or more. Sharper peaks was operationalised as peak height alone; now height or narrowness as readings, and the expected classification per panel is cited from Results paragraph 4, adding 3 dB as unimodal.
  - model-matches-classification, the filter-length readings (25 and 50 ms) were made up; Eq. 2 integrates to T, the symbol the Methods define as the AM signal's duration, now the main reading with the 25 ms truncation as the second.
  - fig7ab-information-per-burst-increases, added the open normalisation of I_n(1) (Eq. 10 as printed against the per-event form of Eq. 3 and Brenner et al., a factor T apart).
  - fig7cd-occurrence-decreases, noted that the Figure 7C legend says number of occurrences, which gives the same slope on a log scale.
  - fig9c-population-nbta, the peak width (half height) was presented as fixed; it is not defined, now two readings.
  - fig5-burst-probability-vs-stimulus, the criterion now shows the n = 2 and 3 ordering that the statement also asserts.
  - Open, the number of bursting sessions differs across the paper (63 in Table 1, 59 for Figure 7, 58 for Figure 8) with no stated reason; the file's detail (4) carries both readings.
  - Open, the partial-reproduction thresholds in several criteria (for example 16 of 19 values in table1-burst-length, 90% in the Figure 7 claims) are the file's judgement rules, not the paper's; left as written.
  - Open, two sentences are garbled in the text (no <69% in fig7gh-information-rate, the sigma ratio in sigma-n-below-sta-sigma); no PDF was supplied to settle them.
EOF
python tools/claims_check.py claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml paper/10.3389-neuro.10.003.2008.txt; grep -n ' — \|rather' claims/crcns-ia-1/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I've checked the claims file and corrected 15 claims. I think it is ready for an attempt, and its last check says so (`ready: true`). Nothing was committed.

**Checker result:** `26 claims, 24 quotes, 1 statistical values, 0 problems`. The first run reported 4 statistical values; I removed 3 of them, as explained below.

**Changes, by claim**
- **fig8-nbta-differ, fig9-nbta-not-concatenated-1bta:** I removed the ANOVA and t-test p < 0.01 entries. They are significance levels used to count sessions, not results. In fig8, the statement no longer says every bursting cell's peaks grow higher and wider with n. The paper shows that for the example cell only, and says in Qualitative description, paragraph 6, that some cells differ.
- **direct-method-comparison:** I put the tolerance on R (0.95) back to the default 10% (0.095). The stated reason for narrowing it, that 10% would allow values above 1, did not hold up.
- **fig8-latency-decreases:** the criterion required both readings to hold. The protocol says any one reading is enough, so I changed it.
- **fig8e-sigma-minimum:** the 7 ms minimum comes from the example cell (with its 0.33 ms), not the population; the statement now says so. I added the paper's second population value (about 0.05 times the inverse cutoff). The window searched for the minimum is not stated in the paper, so it is now two readings.
- **firing-rate-uniform:** the reason given for testing only the kept sessions misread the paragraph order. Both the 86 kept sessions and all 132 are now readings.
- **data-sessions-and-trials:** I added the reported 6 Hz average of the trial-to-trial firing-rate SD.
- **table1-sessions-per-protocol:** the note now says why "recorded sessions" are read as the 86 kept ones: the seven counts add up to 86.
- **fig3-correlation-shape:** the criterion said the Methods give each cell two stimuli; paragraph 1 says two or more. "Sharper peaks" was measured by peak height alone; it now allows height or narrowness. Which panels have a clear first peak is now cited from Results paragraph 4, and 3 dB is added as having none.
- **model-matches-classification:** the 25 and 50 ms filter lengths were made up. Eq. 2 integrates up to T, which the Methods define as the stimulus duration, so that is now the main reading and 25 ms the second.
- **fig7ab-information-per-burst-increases:** I added an open choice. Eq. 10 as printed and the per-event form in Eq. 3 give I_n(1) values that differ by a factor of T.
- **fig7cd-occurrence-decreases:** the Figure 7C legend says "number of occurrences" where the text says "frequency of occurrence". The note says the slope is the same on a log scale.
- **fig9c-population-nbta:** the peak width is not defined in the paper, so it is now two readings.
- **fig5-burst-probability-vs-stimulus:** the order of the n = 2 and 3 probabilities is now shown, since the statement also claims it.

**What remains open**
- The paper gives three different counts of bursting sessions: 63 in Table 1, 59 for Figure 7 and 58 for Figure 8, with no reason given. The file's opening comment already lists both readings.
- Several cut-offs for "partially reproduced" (for example 16 of 19 values, or 90%) are the file's own rules, not the paper's. I left them as written.
- Two sentences are garbled in the text: "no <69%" in fig7gh-information-rate and the sigma ratio in sigma-n-below-sta-sigma. No PDF was supplied to check them.

Every main finding has a claim, and none comes from outside the paper.

## End of run

35 turns, 4 minutes, $1.38 at API prices, result: success.
