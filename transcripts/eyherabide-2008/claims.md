# crcns-ia-1 · claims · run 41882213215

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-ia-1 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
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
cd  wc -l paper/*; cat paper/ia-1.data-description.txt | head -80; grep -n -i crcns docs/archives.md | head -20; ls claims | grep -i crcns;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 30,60p docs/archives.md; ls claims/crcns-ret-1; head -40 claims/crcns-ret-1/*.yaml
```

```
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
  `targets/crcns.json`, written by hand; for now it holds one data set, to test
  the pipeline beyond DANDI.
- **Versions.** CRCNS data sets are not versioned. Record the version as
  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
  notebook header the MD5 sums from the data set's `checksums.md5` for the
  files read, so a later change is detectable.
- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
  us-west-2), under `<id>/`, readable without an account at
  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
  crcns.org asks for a login to download; the bucket does not. Most data sets
  are zip files of MATLAB or other files: open the zip in place with
  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-neuro.10.003.2008.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-neuro.10.003.2008.txt",
 "offset": 242
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text (version of record, PMC2525941) is present with Methods; the paper has no supplement and links no code. Now checking the data descriptor and the ret-1 claims file format.

**Agent calls Bash**

```bash
cd  sed -n 40,75p claims/crcns-ret-1/*.yaml; grep -n "^[a-z_]*:" claims/crcns-ret-1/*.yaml; sed -n 80,255p paper/ia-1.data-description.txt; cat targets/crcns.json; grep -rn "ia-1" targets/ | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; ls schemas 2>/dev/null; grep -rln "claims" schemas docs 2>/dev/null | head
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

**Agent**

The text is complete: version of record, Methods, no supplement, no linked code. Next I'm writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml",
 "content": "# Claims for Eyherabide, Rokem, Herz & Samengo (2008), \"Burst firing is a neural code in an\n# insect auditory system\", Frontiers in Computational Neuroscience, on CRCNS data set ia-1\n# (doi:10.6080/K0BG2KWB).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-04, protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record in PubMed Central (PMC2525941, open access), from Europe PMC\n# full-text XML, as supplied under paper/, with its Materials and Methods, Results, Discussion,\n# the legends of Figures 1 to 10 and Table 1. No PDF was supplied, so values shown only in\n# figures (Figure 5, Figure 9B and the population histograms of Figure 7) could not be read.\n# The paper has no supplement. It links no analysis code, so none was read. Some passages are\n# garbled in the text and are named in the claims that use them (Results, Quantitative\n# description, paragraph 7, \"no <69%\"; Qualitative description, paragraph 5, a ratio of\n# sigma to itself).\n#\n# Data the paper used. Adult Locusta migratoria, intracellular recordings from auditory\n# receptor axons in the tympanal nerve; 37 receptor cells from 23 animals. Each cell was tested\n# with two or more stimuli, 132 sessions in all (a session is one cell in one stimulus\n# condition), of which 86 passed the selection (mean rate near 100 Hz, trial-to-trial SD of the\n# firing rate below 35 Hz). Stimuli were amplitude-modulated sine carriers at the cell's best\n# frequency (3 to 20 kHz), with a Gaussian AM signal, white up to a cutoff frequency. Every cell\n# had the reference stimulus (SD 6 dB, cutoff 200 Hz) and one of six others (SD 6 dB with cutoff\n# 25, 100, 400 or 800 Hz; cutoff 200 Hz with SD 3 or 12 dB); Table 1 lists the seven protocols.\n# Each stimulus lasted 1 s, repeated N = 98 to 503 times (average 172), with 700 ms pauses; the\n# first 200 ms of each trial are discarded in all results. Measured variables: spike times per\n# trial, the stimulus AM signal (in dB), the cell's threshold s_TH and best frequency. The\n# paper's 1 s trials and 0.1 ms time bins are the basis of every analysis.\n#\n# The CRCNS description says the data set holds two sets of spike-time recordings from the\n# same lab, Data1 (2003), which it names as analysed in this paper, and Data2 (2004), which it\n# says is unpublished and used other stimuli. The paper's experiments are those of Data1, with\n# the stimulus files. Which sessions pass the paper's selection, and whether the thresholds\n# s_TH are held, is for the author to find.\n#\n# Method choices common to all claims, from the Methods. Spikes binned at 0.1 ms; the first\n# 200 ms of each trial discarded. Bursts are identified per session from the spike-train\n# correlation function (Eq. 1): a session is bursting when C_s has a first peak below\n# tau = 5 ms bounded on its right by a minimum below 1.25 times the inverse cutoff frequency\n# that differs from the maximum by more than the sum of their error bars (Delta = sigma /\n# sqrt(N)); consecutive spikes with ISI within the peak's domain (0 to the minimum) form one\n# n-burst, dated by its first spike; in a non-bursting session every spike is a 1-burst.\n# Details the Methods leave open, named in the claims that depend on them:\n# (1) the first peak, which must exclude the zero-lag self term; readings (a) the first local\n# maximum of C_s for tau > 0, (b) the largest value of C_s for 0 < tau < 5 ms;\n# (2) the bounding minimum; readings (a) the first local minimum after the peak that differs\n# significantly from the maximum, (b) the lowest value of C_s between the peak and\n# 1.25 / cutoff;\n# (3) sigma and N in Delta; readings (a) sigma the SD of the product terms of Eq. 1 at each tau\n# over trials and times, N their number, (b) the same with N the number of trials;\n# (4) the set of bursting sessions. Table 1 counts 63 sessions with n > 1 (40, 7, 6, 7 and 3),\n# the Results speak of 59 bursting cells (Figure 7B) and of 58 bursting sessions (Figures 8\n# and 9), with no stated reason for the difference. The readings are (a) all sessions the\n# method classifies as bursting, (b) those of them that also have bursts with n > 1 in\n# enough number for the analysis at hand. Population values are reported under both.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ia-1\n  doi: 10.6080/K0BG2KWB\npaper: doi:10.3389/neuro.10.003.2008\nclaims:\n- id: data-sessions-and-trials\n  statement: Thirty-seven receptor cells were recorded from 23 animals, giving 132 sessions,\n    of which 86 met the firing-rate and stationarity conditions; each stimulus was repeated\n    98 to 503 times, 172 on average.\n  source: Materials and Methods, Electrophysiology and stimulus design, paragraphs 1, 4 and 5\n  quote: Thirty-seven receptor cells were recorded, from 23 animals. Each cell was tested with\n    two or more stimuli, resulting in 132 data sets in total ... There were 86 out of 132 data\n    sets that fulfilled these two conditions ... N repetitions of each stimulus were presented,\n    with N ranging between 98 and 503 (average 172)\n  expected:\n  - quantity: receptor cells\n    value: 37\n    tolerance: 3.7\n  - quantity: animals\n    value: 23\n    tolerance: 2.3\n  - quantity: sessions recorded\n    value: 132\n    tolerance: 13.2\n  - quantity: sessions passing the selection\n    value: 86\n    tolerance: 8.6\n  - quantity: fewest trials in a session\n    value: 98\n    tolerance: 9.8\n  - quantity: most trials in a session\n    value: 503\n    tolerance: 50.3\n  - quantity: mean trials per session\n    value: 172\n    tolerance: 17.2\n  criterion: The selection keeps sessions whose trial-to-trial SD of the firing rate is below\n    35 Hz and whose mean rate is about 100 Hz (Methods, paragraph 4). The paper gives no bound\n    for about 100 Hz, nor the window of the per-trial rate. Readings for the rate condition\n    are (a) the SD condition alone; (b) the SD condition and a target rate of 100 Hz where the\n    data record the target. Per-trial rates are taken over 200 to 1000 ms (the paper discards\n    the first 200 ms in all results) and, as a variant, over the whole 1 s. The trial counts\n    are read (a) over the 86 kept sessions, (b) over all sessions. Reproduced when every\n    value is within tolerance under one reading.\n- id: table1-sessions-per-protocol\n  statement: The 86 kept sessions divide among the seven stimulus protocols as 43 (6 dB, 200\n    Hz), 6 (3 dB, 200 Hz), 7 (12 dB, 200 Hz), 7 (6 dB, 25 Hz), 8 (6 dB, 100 Hz), 7 (6 dB, 400\n    Hz) and 8 (6 dB, 800 Hz).\n  source: Table 1, row Recorded sessions\n  inferred: The numbers are read from Table 1; no sentence states them.\n  depends_on:\n  - data-sessions-and-trials\n  expected:\n  - quantity: sessions, protocol 1 (6 dB, 200 Hz)\n    value: 43\n    tolerance: 4.3\n  - quantity: sessions, protocol 2 (3 dB, 200 Hz)\n    value: 6\n    tolerance: 0.6\n  - quantity: sessions, protocol 3 (12 dB, 200 Hz)\n    value: 7\n    tolerance: 0.7\n  - quantity: sessions, protocol 4 (6 dB, 25 Hz)\n    value: 7\n    tolerance: 0.7\n  - quantity: sessions, protocol 5 (6 dB, 100 Hz)\n    value: 8\n    tolerance: 0.8\n  - quantity: sessions, protocol 6 (6 dB, 400 Hz)\n    value: 7\n    tolerance: 0.7\n  - quantity: sessions, protocol 7 (6 dB, 800 Hz)\n    value: 8\n    tolerance: 0.8\n  criterion: Counted over the kept sessions of data-sessions-and-trials, under each of its\n    readings. Reproduced when all seven counts are within tolerance under one reading.\n- id: firing-rate-uniform\n  statement: The kept sessions had a mean firing rate of 113 Hz (SD 16 Hz) that did not differ\n    significantly across stimulus conditions (one-way ANOVA, p = 0.58).\n  source: Materials and Methods, Electrophysiology and stimulus design, paragraph 4\n  quote: The resulting firing rates had a mean of 113 Hz (SD = 16 Hz), and they did not show\n    any significant variation in the different stimulus conditions, as assessed by a one-way\n    ANOVA ( p = 0.58)\n  statistics:\n  - test: one-way ANOVA across stimulus conditions\n    p: 0.58\n  depends_on:\n  - data-sessions-and-trials\n  expected:\n  - quantity: mean firing rate over sessions\n    value: 113\n    tolerance: 16\n    unit: Hz\n  - quantity: SD of the firing rate over sessions\n    value: 16\n    tolerance: 1.6\n    unit: Hz\n  criterion: Per session, the mean firing rate over trials (200 to 1000 ms, and over the whole\n    1 s as a variant). The mean over sessions is within tolerance (the paper's stated SD). A\n    claim of absence, judged on the paper's test, a one-way ANOVA of session rates on the\n    seven stimulus protocols at p < 0.05; reproduced when it is not significant, with the\n    F statistic and p reported. The paper does not say whether the 86 kept sessions or all\n    sessions were tested; the kept sessions are the main reading, as the sentence follows\n    their selection.\n- id: threshold-population\n  statement: The mean threshold of the cells at their best frequency was 58 dB (SD 14 dB).\n  source: Materials and Methods, Electrophysiology and stimulus design, paragraph 2\n  quote: The mean threshold across the population was 58 dB (SD 14 dB)\n  expected:\n    quantity: mean threshold over cells\n    value: 58\n    tolerance: 14\n    unit: dB\n  criterion: The threshold is the minimal intensity of a pure tone at the best frequency\n    that induced spiking (Methods, paragraph 2). Testable only if the data set records the\n    thresholds or the tuning measurements; the mean over cells is within the paper's SD.\n- id: table1-bursting-sessions\n  statement: The number of sessions with bursts of n > 1 depends on the stimulus, from none\n    for 3 dB and for 800 Hz to all 7 for 12 dB and 7 of 8 for 100 Hz; 40 of 43 reference\n    sessions, 6 of 7 at 25 Hz and 3 of 7 at 400 Hz.\n  source: Table 1, row Sessions with n > 1; Results, Stimulus characteristics modulate burst\n    probability, paragraph 8\n  quote: The fraction of bursting sessions, the percentage of isolated spikes (1-bursts), and\n    the maximum n -value depend strongly on the standard deviation and cutoff frequency of the\n    stimulus\n  depends_on:\n  - table1-sessions-per-protocol\n  expected:\n  - quantity: sessions with n > 1, protocol 1 (6 dB, 200 Hz)\n    value: 40\n    tolerance: 4\n  - quantity: sessions with n > 1, protocol 2 (3 dB, 200 Hz)\n    value: 0\n    tolerance: 0\n  - quantity: sessions with n > 1, protocol 3 (12 dB, 200 Hz)\n    value: 7\n    tolerance: 0.7\n  - quantity: sessions with n > 1, protocol 4 (6 dB, 25 Hz)\n    value: 6\n    tolerance: 0.6\n  - quantity: sessions with n > 1, protocol 5 (6 dB, 100 Hz)\n    value: 7\n    tolerance: 0.7\n  - quantity: sessions with n > 1, protocol 6 (6 dB, 400 Hz)\n    value: 3\n    tolerance: 0.3\n  - quantity: sessions with n > 1, protocol 7 (6 dB, 800 Hz)\n    value: 0\n    tolerance: 0\n  criterion: Bursts identified per session by the Methods (Burst identification) under the\n    readings of details (1) to (3) in the opening comment. Reproduced when all seven counts\n    are within tolerance under one combination of readings; partially reproduced when five or\n    six are. The counts under every combination are shown.\n- id: table1-isolated-spikes\n  statement: The percentage of isolated spikes among all bursts of the bursting sessions\n    depends on the stimulus (74, 100, 62, 60, 55, 96 and 100% for protocols 1 to 7), and in\n    every protocol isolated spikes are the most probable burst.\n  source: Table 1, rows % Isolated spikes and Most probable n; Results, Stimulus\n    characteristics modulate burst probability, paragraph 8\n  quote: Notice, however, that in all cases, isolated spikes are more frequent than any other\n    burst of n > 1.\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: isolated spikes, protocol 1\n    value: 74\n    tolerance: 7.4\n    unit: '%'\n  - quantity: isolated spikes, protocol 2\n    value: 100\n    tolerance: 10\n    unit: '%'\n  - quantity: isolated spikes, protocol 3\n    value: 62\n    tolerance: 6.2\n    unit: '%'\n  - quantity: isolated spikes, protocol 4\n    value: 60\n    tolerance: 6\n    unit: '%'\n  - quantity: isolated spikes, protocol 5\n    value: 55\n    tolerance: 5.5\n    unit: '%'\n  - quantity: isolated spikes, protocol 6\n    value: 96\n    tolerance: 9.6\n    unit: '%'\n  - quantity: isolated spikes, protocol 7\n    value: 100\n    tolerance: 10\n    unit: '%'\n  criterion: As the Table 1 legend defines it, the number of 1-bursts over the total number of\n    bursts, pooled over the bursting sessions of each protocol (all sessions where a protocol\n    has none). Reproduced when every value is within tolerance and n = 1 is the most probable\n    n in every protocol. The legend does not say whether counts are pooled before the ratio\n    or ratios averaged over sessions; pooling is the main reading, as the legend says the\n    sessions are pooled for the average n, and the session average is shown as a variant.\n- id: table1-burst-length\n  statement: The highest n and the average n depend on the stimulus; the longest bursts (up to\n    15 spikes, average 2.10 with SD 3.67) occur at 25 Hz, and no bursts occur at 3 dB or at\n    800 Hz.\n  source: Table 1, rows Highest n and Average n\n  inferred: The values are read from Table 1; the sentence of paragraph 8 states the\n    dependence on the stimulus but not the values.\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: highest n, protocols 1 to 7 (9, 1, 8, 15, 9, 3, 1), protocol 1\n    value: 9\n    tolerance: 0.9\n  - quantity: highest n, protocol 2\n    value: 1\n    tolerance: 0.1\n  - quantity: highest n, protocol 3\n    value: 8\n    tolerance: 0.8\n  - quantity: highest n, protocol 4\n    value: 15\n    tolerance: 1.5\n  - quantity: highest n, protocol 5\n    value: 9\n    tolerance: 0.9\n  - quantity: highest n, protocol 6\n    value: 3\n    tolerance: 0.3\n  - quantity: highest n, protocol 7\n    value: 1\n    tolerance: 0.1\n  - quantity: average n, protocol 1\n    value: 1.3\n    tolerance: 0.13\n  - quantity: average n, protocol 2\n    value: 1\n    tolerance: 0.1\n  - quantity: average n, protocol 3\n    value: 1.5\n    tolerance: 0.15\n  - quantity: average n, protocol 4\n    value: 2.1\n    tolerance: 0.21\n  - quantity: average n, protocol 5\n    value: 1.7\n    tolerance: 0.17\n  - quantity: average n, protocol 6\n    value: 1.04\n    tolerance: 0.104\n  - quantity: average n, protocol 7\n    value: 1\n    tolerance: 0.1\n  - quantity: SD of n, protocol 1\n    value: 1.3\n    tolerance: 0.13\n  - quantity: SD of n, protocol 3\n    value: 1.6\n    tolerance: 0.16\n  - quantity: SD of n, protocol 4\n    value: 3.67\n    tolerance: 0.367\n  - quantity: SD of n, protocol 5\n    value: 1.8\n    tolerance: 0.18\n  - quantity: SD of n, protocol 6\n    value: 0.42\n    tolerance: 0.042\n  criterion: As the Table 1 legend defines it, all bursting sessions of a protocol pooled, the\n    probability of each n as the fraction of all bursts, and the mean and SD of n under that\n    probability. The tolerance of the average n is 10% of the value, not the SD the table\n    prints beside it, as that SD is the spread of n over bursts, not an uncertainty of the\n    average. Reproduced when at least 16 of the 19 values are within tolerance under one\n    combination of the burst-identification readings; partially reproduced for 10 to 15.\n- id: fig5-burst-probability-vs-stimulus\n  statement: The probability of generating isolated spikes is lowest, and high-n bursts most\n    frequent, for large amplitude fluctuations (12 dB) and cutoff frequencies around 100 Hz.\n  source: Figure 5; Results, Stimulus characteristics modulate burst probability, paragraph 10\n  quote: The probability of generating isolated spikes is minimal for large amplitude\n    fluctuations and cutoff frequencies around 100 Hz.\n  depends_on:\n  - table1-bursting-sessions\n  criterion: As in the Figure 5 legend, the population average over sessions of the probability\n    of an n-burst (the fraction of all bursts with that n) for n = 1, 2 and 3, against cutoff\n    for the 6 dB stimuli (25, 100, 200, 400, 800 Hz) and against SD for the 200 Hz stimuli (3,\n    6, 12 dB). The legend does not say whether non-bursting sessions (all 1-bursts) enter the\n    average; readings (a) all kept sessions, (b) bursting sessions only. Reproduced when, under\n    one reading, P(n = 1) is lowest at 100 Hz among the cutoffs and at 12 dB among the SDs.\n    The figure's values cannot be read from the text, so only this ordering is judged.\n- id: fig3-correlation-shape\n  statement: For a cell tested with all stimuli, larger stimulus SD gives correlation functions\n    with sharper peaks, and faster stimuli lead from multi-modal (25 Hz) to single-peaked (100,\n    200 Hz) to shallower and broader correlation functions (400, 800 Hz).\n  source: Figure 3; Results, Stimulus characteristics modulate burst probability, paragraph 3\n  quote: Increasing the standard deviation of the amplitude distribution (from Figure 3 A to D\n    to G) results in correlation functions that exhibit progressively sharper peaks ...\n    Decreasing the typical time scale of the stimulus fluctuations (going right from Figure 3\n    B to F) leads from multi-modal (Figure 3 B) to single-peaked (Figures 3 C,D) to\n    increasingly shallower and broader correlation functions (Figures 3 E,F).\n  criterion: C_s(tau) by Eq. 1, 0.1 ms bins. The paper shows one sample cell tested with the\n    whole set of stimuli, while its Methods say each cell had two stimuli; the cell is not\n    identified. Reproduced when a cell with all seven stimuli is found and its correlation\n    functions show the described ordering (peak height of the first peak over its baseline\n    increasing with SD; more than one peak at 25 Hz, one peak at 100 and 200 Hz, no separable\n    first peak at 400 or 800 Hz under the Burst identification test). If no such cell is held,\n    the claim is not testable as stated, and the same ordering on the average over sessions of\n    each protocol's normalised C_s is shown as a variant.\n- id: method-correlation-error\n  statement: The temporal average of the estimated error of the correlation function was on\n    average 3.4% (SD 1.5%) of the span of C_s.\n  source: Materials and Methods, Burst identification, paragraph 6\n  quote: The population mean of the temporal average of this estimated error was 3.4% (SD 1.5%)\n    of the total span of C s (τ) (that is, the difference between the maximum and the\n    minimum)\n  expected:\n    quantity: mean over sessions of the time-averaged error of C_s, as a fraction of its span\n    value: 3.4\n    tolerance: 1.5\n    unit: '%'\n  criterion: Delta = sigma / sqrt(N) at each tau, averaged over tau, divided by max minus min\n    of C_s, averaged over sessions. Readings for sigma and N as detail (3) of the opening\n    comment, and for the tau range (a) 0 to 1.25 / cutoff, (b) the whole range up to the\n    trial length. Reproduced when the value is within tolerance under one reading.\n- id: model-matches-classification\n  statement: A threshold-linear Poisson model with refractoriness and no free parameters\n    classifies sessions as bursting or not in agreement with the real data in 86% of sessions,\n    and where both are bursting their limiting ISIs differ by less than 1 ms in 81% of cases.\n  source: Results, Stimulus characteristics modulate burst probability, paragraph 11; Figure 3\n    middle and lower subpanels\n  quote: When the analysis is extended to the whole population of cells, this agreement is\n    observed in 86% of all sessions. Moreover, in those sessions where both real and simulated\n    data are classified as bursting, the limiting ISI calculated with real and simulated data\n    differ by <1 msec in 81% of the cases.\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: sessions where model and data agree on bursting\n    value: 86\n    tolerance: 8.6\n    unit: '%'\n  - quantity: bursting sessions with limiting ISI within 1 ms\n    value: 81\n    tolerance: 8.1\n    unit: '%'\n  criterion: The model of Eq. 2 per session, as the Methods (Model neurons) give it. The\n    stimulus s(t) is the AM signal in dB, thresholded at s_TH before filtering; h(tau) from the\n    cross-correlation of the spike train with s*(t); t_ref the session's minimal ISI; spikes by\n    an inhomogeneous Poisson process with rate r_s(t), zero for t_ref after each spike, at 0.1\n    ms steps, with as many trials as recorded. s_TH is measured (Methods, paragraph 2); if the\n    data set does not hold it, the claim is not testable as the paper ran it. Open details\n    are the filter length T, read as (a) 25 ms (the nBTA window before a burst) and (b) 50 ms,\n    and the filter's scale, which the cross-correlation does not fix, read as (a) the\n    cross-correlation divided by the variance of s*(t), (b) scaled so the model's mean rate\n    equals the session's. Bursting classification and limiting ISI as for the data. Reproduced\n    when both values are within tolerance under one reading. The linear model of Figure 3\n    (no thresholding) is shown with the same measures.\n- id: fig6-bursts-less-correlated\n  statement: Representing the spike train as n-bursts reduces correlations between time bins;\n    the mean squared Pearson coefficient over t from 200 to 990 ms and tau from 0 to 10 ms is\n    2.89 times larger (SD 1.49) for spikes than for bursts, on average over the bursting\n    sessions (2.94 for the example cell).\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 2; Figure 6\n  quote: For the cell shown in Figure 6 , the mean value of c s 2 ( t , τ ) averaged over all t\n    ∈ [200, 990 msec] and τ ∈ [0, 10 msec] is 2.94 times larger than the corresponding mean of\n    c b 2 ( t , τ ) . The population average of this ratio on all bursting sessions is 2.89\n    (SD 1.49).\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n    quantity: population mean of mean c_s squared over mean c_b squared\n    value: 2.89\n    tolerance: 1.49\n  criterion: c_s(t, tau) and c_b(t, tau) by Eq. 11 over trials, with c set to 0 when numerator\n    and denominator vanish, n(t) the burst count starting in each bin and the spike variable\n    binary. The bin width is not stated for this analysis; readings (a) 0.1 ms, the paper's\n    discretisation (Burst identification, paragraph 2), (b) 0.4 ms, the precision of its direct\n    method. Whether tau = 0 (where c is 1 or 0 for both) enters the average is open; readings\n    include and exclude it. Bursting sessions under detail (4). Reproduced when the population\n    mean is within tolerance and above 1 under one reading; partially reproduced when the ratio\n    exceeds 1 in most bursting sessions but the mean is out of tolerance.\n- id: fig7ab-information-per-burst-increases\n  statement: The information carried by each n-burst increases with n; every bursting session\n    has a significantly positive slope of I_n(1) against n, with an average slope of 1.5 bits\n    (SD 0.7 bits) over 59 bursting cells.\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 5; Figure 7A and 7B\n  quote: All sessions had significantly positive slopes. Figure 7 B shows the distribution of\n    slopes throughout the population. The average slope across the 59 bursting cells was 1.5\n    bits (SD 0.7 bits).\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: mean slope of I_n(1) against n\n    value: 1.5\n    tolerance: 0.7\n    unit: bits\n  - quantity: bursting cells\n    value: 59\n    tolerance: 5.9\n  criterion: I_n(1) = (1 / rbar_n) times the integral of r_n(t) log2(r_n(t) / rbar_n) over 200 to\n    1000 ms (Eq. 10), r_n(t) the trial-averaged rate of n-burst onsets. The Methods do not\n    give the bin width of r_n(t), any smoothing or any bias correction; readings (a) 0.1 ms\n    bins, (b) 0.4 ms bins, both without smoothing or correction. The fit is a straight line of\n    I_n(1) on n over the n values present; the paper says the slope's sign was judged with its\n    estimated error but not how; readings (a) slope greater than one standard error of the fit\n    above zero, (b) slope greater than zero by a t-test at p < 0.05. Reproduced when, under\n    one reading, the mean slope is within tolerance and every bursting session (at least 90%,\n    for partially reproduced) has a significantly positive slope.\n- id: fig7cd-occurrence-decreases\n  statement: High-n bursts are rare; in every session the frequency of occurrence decreases\n    significantly with n, with an average slope of -2.6 (SD 0.7).\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 6; Figure 7C and 7D\n  quote: This result was also observed in all other recorded cells - the frequency of occurrence\n    always decreased significantly with n . The population data in Figure 7 D had an average\n    slope of −2.6, with SD of 0.7.\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n    quantity: mean slope of the frequency of occurrence against n\n    value: -2.6\n    tolerance: 0.7\n  criterion: Frequency of occurrence rbar_n over the sum of rbar_n, per session. The paper does\n    not give the scale of the fit; a slope of -2.6 per unit n is impossible for a fraction on a\n    linear scale, so it is read as a fit to the logarithm, with readings (a) log2, (b) natural\n    log, (c) log10. Significance as in fig7ab-information-per-burst-increases. Reproduced when,\n    under one reading, the mean slope is within tolerance and the slope is significantly\n    negative in every bursting session (at least 90% for partially reproduced).\n- id: fig7ef-jitter-independent-of-n\n  statement: The jitter of the first spike of a burst is roughly independent of n in 80% of the\n    bursting sessions, and the mean slope of jitter against n is -0.03 ms (SD 0.2 ms).\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 6; Figure 7E and 7F\n  quote: At the population level, in 80% of the bursting sessions the amount of jitter was\n    roughly independent from n (the best linear fit had a slope that was not significantly\n    different from 0) ... The mean slope was −0.03 msec (SD 0.2 msec).\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: bursting sessions with no significant slope of jitter on n\n    value: 80\n    tolerance: 8\n    unit: '%'\n  - quantity: mean slope of jitter on n\n    value: -0.03\n    tolerance: 0.2\n    unit: ms\n  criterion: Jitter is the trial-to-trial SD of the time of the first spike of a burst\n    (Methods, Estimation of burst-triggered averages, last paragraph), averaged per n. The\n    paper refers to Rokem et al. (2006) for the definition and does not say how bursts are\n    matched across trials into events; readings (a) events as peaks of the trial-averaged\n    n-burst onset histogram (0.1 ms bins), each event's onsets taken between the troughs on\n    either side, (b) events as the onsets that fall within the first peak domain of the\n    session around an event centre. Slope significance as in\n    fig7ab-information-per-burst-increases. Reproduced when both values are within tolerance\n    under one reading.\n- id: fig7gh-information-rate\n  statement: The information rate of n-bursts decreases with n (average slope -11 bits/s, SD\n    16 bits/s), yet bursts with n > 1 together carry on average 47% of the total information\n    over the bursting cells; in the example cell the total is 220 bits/s.\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 7; Figure 7G and 7H\n  quote: I ′ n strongly decreases with n (Figure 7 G). Similar results were obtained in all\n    other recorded sessions (Figure 7 H), with an average slope of −11 bits/s (SD 16 bits/s)\n    ... The population average of this fraction among all bursting cells was 47%.\n  depends_on:\n  - fig7ab-information-per-burst-increases\n  expected:\n  - quantity: mean slope of I'_n against n\n    value: -11\n    tolerance: 16\n    unit: bits/s\n  - quantity: mean fraction of information carried by n > 1 bursts\n    value: 47\n    tolerance: 4.7\n    unit: '%'\n  criterion: I'_n = I_n / T, with I_n = rbar_n times I_n(1) (Eq. 10) and T = 0.8 s (200 to 1000\n    ms), under the readings of fig7ab-information-per-burst-increases. The fraction is the sum\n    of I'_n over n > 1 over I'. Reproduced when both values are within tolerance under one\n    reading. The text's sentence on the example cell is garbled (\"provide no <69% of the total\n    information\"); it is read as at least 69% and not judged, as the example cell is not\n    identified.\n- id: direct-method-comparison\n  statement: Information rates from the burst code are highly correlated with those of the\n    direct method (R = 0.95), averaging 191 against 222 bits/s, the direct method being higher\n    in all sessions but one by 31 bits/s on average, so the burst code keeps about 85% of the\n    information.\n  source: Results, Quantitative description of the information transmitted by bursts,\n    paragraph 10; Discussion, Comparison with other neural codes, paragraph 3\n  quote: The information measures obtained by our method and by the direct method were highly\n    correlated ( R = 0.95, using all sessions). The population average obtained with the direct\n    method is 222 ± 69 bits/s. With our method, instead, this average was 191 ± 72 bits/s. In\n    all cases but one, the information obtained with the direct method was higher than the one\n    obtained with our method, the average difference being 31 ± 16 bits/s.\n  depends_on:\n  - fig7gh-information-rate\n  expected:\n  - quantity: correlation between the two information rates over sessions\n    value: 0.95\n    tolerance: 0.05\n  - quantity: mean information rate, direct method\n    value: 222\n    tolerance: 69\n    unit: bits/s\n  - quantity: mean information rate, burst code\n    value: 191\n    tolerance: 72\n    unit: bits/s\n  - quantity: mean difference, direct minus burst code\n    value: 31\n    tolerance: 16\n    unit: bits/s\n  - quantity: fraction of the direct-method information lost by the burst code\n    value: 14\n    tolerance: 1.4\n    unit: '%'\n  criterion: The direct method (Strong et al., 1998) on binary words of 0.4 ms bins up to 3.2 ms\n    (8 bins), the entropies bias-corrected with NSB, over 200 to 1000 ms. The paper does not\n    say whether the rate is taken at 3.2 ms or extrapolated to long words; readings (a) the\n    rate at the 3.2 ms word length, (b) a linear extrapolation in the inverse word length over\n    the lengths up to 3.2 ms. The burst-code rate is I' of fig7gh-information-rate, with the\n    non-bursting sessions treated as all 1-bursts. \"All sessions\" is read as (a) the 86 kept\n    sessions, (b) the bursting sessions. The tolerance of R is 0.05 since 10% would allow\n    values above 1. Reproduced when, under one reading, R, the two means and the difference are\n    within tolerance and the direct method is higher in all sessions but at most a few (90%).\n- id: fig8-nbta-differ\n  statement: In every bursting cell the burst-triggered averages for n = 1 to 4 differ\n    significantly, their central peaks growing higher and wider with n; 50 of the 58 bursting\n    sessions show significantly different central peaks in the time domain, the other eight\n    having too few bursts.\n  source: Results, Qualitative description of the information transmitted by bursts,\n    paragraphs 3 and 6; Figure 8D\n  quote: All recorded and simulated bursting cells exhibited significantly different n -BTAs,\n    for n ranging between 1 and 4 ... out of the 58 sessions where bursting cells were found,\n    50 exhibit n BTAs whose central peaks were significantly different from one another\n  statistics:\n  - about: nBTAs for n = 1 to 4, per session, frequency domain\n    test: two-way ANOVA (frequency band and burst order) on real and imaginary parts\n    p: 0.01\n    p_relation: <\n    corrected: Bonferroni\n  - about: nBTA against each other nBTA at each time point\n    test: Student's t-test\n    p: 0.01\n    p_relation: <\n  depends_on:\n  - table1-bursting-sessions\n  expected:\n  - quantity: bursting sessions with significantly different central peaks\n    value: 50\n    tolerance: 5\n  - quantity: bursting sessions\n    value: 58\n    tolerance: 5.8\n  criterion: As the Methods (Estimation of burst-triggered averages, paragraph 2) give it. Each\n    stimulus segment from -25 to +15 ms around a burst onset is Fourier transformed; two-way\n    ANOVAs on the real and on the imaginary parts, factors frequency bin and n (1 to 4), each at\n    0.01 / 2; a session differs when either shows a main effect of n or an interaction. The\n    frequency bins used are not stated; readings (a) all bins of the transform, (b) bins up to\n    the stimulus cutoff. Then, at each time point, independent t-tests of each nBTA against the\n    three others at p < 0.01, a point marked when all three are significant. What \"central\n    peaks significantly different\" requires is not stated; readings (a) at least one marked\n    point within the central peak for every n, (b) most points of each central peak marked (as\n    \"Most of the central peak in each n BTA is significantly different\", paragraph 3). The\n    stimulus is the AM signal in dB. Reproduced when every bursting session with bursts of\n    n = 1 to 4 passes the ANOVA and the time-domain count is within tolerance under one\n    reading.\n- id: fig8-latency-decreases\n  statement: The latency between the stimulus upstroke and burst onset decreases with n, so\n    that high or wide deflections produce prompt responses with high-n bursts.\n  source: Results, Qualitative description of the information transmitted by bursts, paragraph\n    3; Figure 8D; Discussion, Implications for the neural code, paragraph 4\n  quote: Moreover, the mean delay between stimulus upstroke and burst generation decreases\n    systematically with n . This implies that stimulus deflections that are either high or wide\n    tend to produce prompt responses, with high- n bursts.\n  depends_on:\n  - fig8-nbta-differ\n  criterion: tau_n is the time between the maximum of the nBTA and burst onset (Methods, Eq. 13).\n    The paper shows it for one cell and gives no population test. Readings for \"systematically\"\n    are (a) tau_n decreasing from n = 1 to n = 4 in the majority of bursting sessions with\n    bursts up to n = 4; (b) the mean over those sessions of tau_n decreasing from n = 1 to 4.\n    Reproduced when both readings hold; partially reproduced when one does.\n- id: fig8e-sigma-minimum\n  statement: The standard deviation of the stimuli preceding an n-burst has a minimum about 7 ms\n    before burst onset, at a position nearly the same for all n; over the bursting cells the SD\n    of the minimum's position across n = 1 to 4 averages 0.4 ms (SD 0.7 ms).\n  source: Results, Qualitative description of the information transmitted by bursts, paragraph\n    4; Figure 8E\n  quote: The constancy of the location of the minima also holds at the population level ... Its\n    average among all bursting cells is 0.4 msec (SD 0.7 msec) considering 1 ≤ n ≤ 4.\n  depends_on:\n  - fig8-nbta-differ\n  expected:\n    quantity: mean over bursting sessions of the SD across n of the position of the minimum of\n      sigma_n\n    value: 0.4\n    tolerance: 0.7\n    unit: ms\n  criterion: sigma_n(tau) by Eq. 14, its minimum searched over -25 to 0 ms (the window of the\n    nBTA analysis before onset). Sessions with bursts of all four n. Reproduced when the value\n    is within tolerance.\n- id: sigma-n-below-sta-sigma\n  statement: In 98% of bursting cells, for all n, the SD of the stimuli preceding an n-burst is\n    smaller than the SD of the stimuli preceding all spikes, by a ratio of minima of 1.62 on\n    average (SD 0.56).\n  source: Results, Qualitative description of the information transmitted by bursts, paragraph 5\n  quote: For 98% of the bursting cells and for all n -values, σ n (τ) was smaller than the\n    standard deviation σ(τ) of the stimuli preceding all spikes (prior to any classification).\n    The population average of the ratio of the minimum value of σ(τ) to the n -average of the\n    minimum values of σ(τ) was 1.62 (SD 0.56).\n  depends_on:\n  - fig8e-sigma-minimum\n  expected:\n  - quantity: bursting sessions with sigma_n below sigma for all n\n    value: 98\n    tolerance: 9.8\n    unit: '%'\n  - quantity: mean ratio of min sigma to the mean over n of min sigma_n\n    value: 1.62\n    tolerance: 0.56\n  criterion: The second sigma of the quoted ratio is garbled in the text; it is read as sigma_n,\n    as the sentence compares the two. \"Smaller\" is read as (a) the minimum of sigma_n below the\n    minimum of sigma, (b) sigma_n below sigma at every tau in -25 to +15 ms. n from 1 to 4.\n    Reproduced when both values are within tolerance under one reading.\n- id: fig9-nbta-not-concatenated-1bta\n  statement: The nBTA differs from n 1BTAs shifted by the burst's own ISIs and summed; for a\n    large fraction of cells, real and simulated, the difference is significant, the fraction\n    diminishing as n grows; results are similar with shifted STAs.\n  source: Results, Qualitative description of the information transmitted by bursts, paragraphs\n    7 and 8; Figure 9A and 9B\n  quote: A large fraction of the cells show a significant difference, for both real and\n    simulated data. Hence, also at the population level, the n BTAs differ significantly from\n    the convolved 1BTAs. As n increases, the number of sessions with significant differences\n    diminishes.\n  statistics:\n  - about: nBTA against the convolved 1BTA, per session and n\n    test: two-way ANOVA on real and imaginary Fourier parts\n    p: 0.01\n    p_relation: <\n    corrected: Bonferroni\n  depends_on:\n  - fig8-nbta-differ\n  criterion: As the Methods (Estimation of burst-triggered averages, paragraph 3) give it. For\n    each n-burst, f_n(t) is the sum of the 1BTA shifted to each spike of the burst (Eq. 15),\n    averaged over bursts; nBTA against f_n over the interval between the two minima flanking\n    the nBTA's central maximum, by two-way ANOVAs on the real and imaginary Fourier parts at\n    0.01 / 2; then point-by-point t-tests (p < 0.01 per point, as for Figure 8D), counting\n    sessions with significant points over more than 70% of the interval. How each ANOVA's\n    observations are formed is open; readings (a) each burst's stimulus segment against its own\n    f_n, (b) the two collections of segments and convolved functions as two groups. Figure 9B\n    gives the fractions only in a figure the text does not hold; \"a large fraction\" is read\n    as more than half of the bursting sessions for n = 2. Reproduced when, under one reading,\n    more than half differ for n = 2 by the ANOVA, the fraction does not grow from n = 2 to n =\n    4, and the same holds with the STA in place of the 1BTA. The model sessions are shown\n    where model-matches-classification could be run.\n- id: fig9c-population-nbta\n  statement: In the seven cells driven at 100 Hz cutoff and 6 dB, the population-average nBTAs\n    show that bursts with more spikes follow higher or wider stimulus deflections, with large\n    spread across cells.\n  source: Results, Qualitative description of the information transmitted by bursts, paragraph\n    9; Figure 9C\n  quote: Figure 9 C demonstrates that also at the population level, high- n bursts are\n    associated with either higher or wider stimulus deflections (or both).\n  depends_on:\n  - fig8-nbta-differ\n  criterion: As paragraph 9 gives it, each session's 1BTA, 2BTA and 3BTA with the session's mean\n    stimulus subtracted, shifted by tau_n before averaging and back after, averaged over the\n    bursting sessions of protocol 5 (6 dB, 100 Hz). Reproduced when the central peak of the\n    average is higher or wider (width at half height) for 2 than for 1 and for 3 than for 2.\n- id: fig10-burst-n-vs-height\n  statement: The probability of a burst with n spikes after a stimulus maximum depends on its\n    height, low excursions giving no response or an isolated spike and high ones doublets,\n    triplets or 4-bursts; all bursting cells show this.\n  source: Results, Qualitative description of the information transmitted by bursts, paragraph\n    10; Figure 10\n  quote: Whereas fairly low excursions produce either no response (dotted line) or an isolated\n    spike (black, solid line), large deflections are associated with doublets (dark grey),\n    triplets (grey), or bursts with four spikes (light grey line). All cells showing a bursting\n    behavior exhibited this phenomenon.\n  depends_on:\n  - fig8-latency-decreases\n  criterion: P(n | h) as the Methods (Relating burst probabilities to the height of stimulus\n    excursions) give it. Each n-burst shifted back by tau_n; each local maximum of the AM signal\n    at t0 matched to the n-burst whose first spike is closest to t0 within [t0 - T, t0 + T], a\n    burst matched to more than one maximum kept by the nearest; P(n | h) in windows of\n    half-width 5% of the span of h. T is the width of the most prominent STA peak, not further\n    defined; readings (a) between the minima flanking the peak, (b) full width at half maximum.\n    The paper gives no measure of segregation; readings (a) the h at which P(n | h) peaks\n    increases with n for n = 0 to the largest n with bursts (up to 4), (b) the mean of h\n    weighted by P(n | h) increases with n. Reproduced when, under one reading, this holds in\n    every bursting session; partially reproduced when it holds in most.\n- id: firing-rate-no-effect-on-limit\n  statement: The firing rate has practically no effect on the limiting ISI; a 50 Hz increase in\n    rate shifts it by less than 0.4 ms and raises the average n by less than 25%.\n  source: Results, Stimulus characteristics modulate burst probability, paragraph 9\n  quote: More specifically, a 50 Hz increase in firing rate shifts the limiting ISI by <0.4\n    msec, which is comparable to its estimated error bar. The average intra-burst spike count n\n    , in turn, shows an increase of <25%.\n  expected:\n  - quantity: shift of the limiting ISI for a 50 Hz rate increase\n    value: 0.4\n    tolerance: 0.04\n    unit: ms\n  - quantity: increase of the average n for a 50 Hz rate increase\n    value: 25\n    tolerance: 2.5\n    unit: '%'\n  criterion: The paper does not say which recordings or which comparison gave these numbers; the\n    kept sessions all have rates near 100 Hz (SD 16 Hz). Readings (a) the same cell and stimulus\n    recorded at two target rates 50 Hz apart, where the data set holds such pairs; (b) a linear\n    regression over the kept sessions of the limiting ISI and of the average n on the session's\n    rate, scaled to 50 Hz. Reproduced when, under one reading, the shift is below 0.44 ms and the\n    increase below 27.5%. If neither reading can be formed, not testable.\n- id: model-reproduces-coding-trends\n  statement: The threshold-linear model with refractoriness reproduces the coding trends of the\n    data, at single-cell and population level, though it is less precise in time than the real\n    cells.\n  source: Results, Quantitative description of the information transmitted by bursts, paragraph\n    8; Figure 7, right half; Figures 8C and 9D\n  quote: A comparison between the left and right panels of Figure 7 reveals that the model\n    reproduces the general trends observed in the experimental data, both at the single-cell\n    and population level.\n  depends_on:\n  - model-matches-classification\n  - fig7ab-information-per-burst-increases\n  - fig7cd-occurrence-decreases\n  - fig7gh-information-rate\n  criterion: The model sessions of model-matches-classification, under its readings, analysed as\n    in the Figure 7 claims. The \"general trends\" are read as the signs of the population mean\n    slopes of Figure 7 (information per burst rising with n, occurrence and information rate\n    falling with n). Reproduced when all three signs match the data's; partially reproduced for\n    two.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml
python - "$f" <<'EOF'
import sys,re
p=sys.argv[1];s=open(p).read()
s=s.replace("""  quote: This result was also observed in all other recorded cells - the frequency of occurrence
    always decreased significantly with n .""","""  quote: This result was also observed in all other recorded cells ... the frequency of
    occurrence always decreased significantly with n .""")
s=s.replace("highest n, protocols 1 to 7 (9, 1, 8, 15, 9, 3, 1), protocol 1","highest n, protocol 1")
s=s.replace("p_relation: <\n",'p_relation: "<"\n')
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.3389-neuro.10.003.2008.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml; grep -n -e "—" -e "rather" -e ": .*: " $f | head; grep -c "criterion:" $f; git status --short
```

```
26
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/crcns-ia-1/
?? scripts
```

**Agent**

I wrote `claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml`. The quote checker reports 26 claims, 24 quotes, 4 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PMC2525941, open access, from Europe PMC full-text XML): Methods, Results, Discussion, Figure 1 to 10 legends and Table 1. There is no supplement, and the paper links no code, so I read none. No PDF was supplied, so values shown only in figures (Figure 5, Figure 9B, the Figure 7 histograms) could not be read; those claims are judged on direction only. The data descriptor was used only to see which experiments the data set holds: it says Data1 (2003) is the one analysed in this paper.

**Claims.**
- **Quotes:** 24 of the 26 claims have quotes. The two without are Table 1 numbers, so each carries an `inferred` note instead.
- **Statistics:** 3 claims record statistics, 4 entries in all:
  - the one-way ANOVA on firing rate across conditions, p = 0.58;
  - the Fourier-domain two-way ANOVA comparing burst-triggered averages, with Bonferroni correction, p < 0.01;
  - the point-by-point t-test, p < 0.01;
  - the ANOVA comparing each burst-triggered average with summed single-spike averages, p < 0.01.
- **Criteria:** all 26 claims have one.
- **Coverage:** session selection and counts, firing rate, threshold, Table 1 (bursting sessions, isolated spikes, burst length), Figures 3, 5, 6, 7A–H, 8, 9 and 10, the comparison with the direct information method, the model, and the effect of firing rate on the ISI limit.

**Details the paper leaves open, and the readings named:**
- **Burst identification:**
  - Which first peak: the first local maximum after zero lag, or the largest value below 5 ms.
  - Which bounding minimum: the first significant local minimum, or the lowest value before 1.25/cutoff.
  - What σ and N mean in the error Δ = σ/√N: N as all product terms, or as the number of trials.
- **Which sessions count as bursting:** Table 1 implies 63, the Results say 59 cells (Fig 7B) and 58 sessions (Figs 8, 9). Readings: all sessions classified as bursting, or only those with enough bursts.
- **Session selection:** "about 100 Hz" has no bound; readings are the SD < 35 Hz condition alone, or that plus a recorded target rate of 100 Hz. The per-trial rate window is 200–1000 ms, with the full second as a variant.
- **Bin width for information and correlation measures:** 0.1 ms or 0.4 ms. Whether lag zero enters the Fig 6 average: with and without.
- **Slope significance:** within one standard error, or a t-test at p < 0.05. The Fig 7D slope of −2.6 only makes sense on a log scale: log2, ln or log10.
- **Jitter:** how bursts are matched across trials. Readings: peaks of the onset histogram, or windows of the peak domain.
- **Direct method:** rate at the 3.2 ms word length, or extrapolated. "All sessions" is read as the 86 kept sessions, or the bursting ones.
- **Model:** filter length 25 or 50 ms; filter scale as cross-correlation over variance, or matched to the session's mean rate.
- **Burst-triggered-average tests:** frequency bins (all, or up to the cutoff); what "central peaks significantly different" requires (one significant point, or most points); how the ANOVA against summed single-spike averages forms its observations.
- **Figure 10:** STA peak width (between minima, or at half height); the measure of segregation (peak position of P(n|h), or its weighted mean).
- **Latency decreasing "systematically" with n:** within most sessions, or in the population mean.

**Missing from the paper:**
- The Figure 3 example cell, said to be tested with all stimuli, is not identified, and the Methods say each cell had two.
- The firing-rate check behind "a 50 Hz increase shifts the limit by <0.4 ms" names no data or method.
- The model needs each cell's measured threshold, which the data may not hold.
- Two passages are garbled and are read as stated in their claims: "no <69%" is read as "at least 69%", and a ratio prints σ over σ, read as σ over σ_n.
- Figures 5 and 9B give values only in the figures.

## End of run

15 turns, 5 minutes, $1.63 at API prices, result: success.
