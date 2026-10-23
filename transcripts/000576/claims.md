# 000576 · claims · run 39935841794

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000576 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000576 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -20 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0c8340b1-6d77-4a9d-bb4f-1dbf10cad81e/tool-results/b3vfotlqt.txt"
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
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -15 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the main paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuroimage.2020.116705.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "(?i)supplement|Fig\\. ?S|=== page|github|code avail|data avail",
 "path": "paper/10.1016-j.neuroimage.2020.116705.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 883,1068p paper/10.1016-j.neuroimage.2020.116705.txt | grep -n -i -E "zheng|7\.8" ; grep -rl "000576" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v transcripts | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000576' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A15 "000576" papers/manifest.yaml papers/triage.yaml | head -60
```

```
papers/manifest.yaml-830-    pdf: true
papers/manifest.yaml-831-    supplements: 0
papers/manifest.yaml:832:  '000576':
papers/manifest.yaml-833-  - doi: 10.1016/j.neuroimage.2020.116705
papers/manifest.yaml-834-    status: stored
papers/manifest.yaml-835-    version: version of record
papers/manifest.yaml-836-    source: PDF supplied by a person
papers/manifest.yaml-837-    pdf: true
papers/manifest.yaml-838-    supplements: 0
papers/manifest.yaml-839-  - doi: 10.1038/s41597-020-00790-x
papers/manifest.yaml-840-    status: stored
papers/manifest.yaml-841-    version: as served by europe_pmc
papers/manifest.yaml-842-    source: europe_pmc+crossref (paper-text-fetcher)
papers/manifest.yaml-843-    pdf: false
papers/manifest.yaml-844-    supplements: 0
papers/manifest.yaml-845-  000579:
papers/manifest.yaml-846-  - doi: 10.1016/j.neuron.2022.05.012
papers/manifest.yaml-847-    status: stored
--
papers/triage.yaml-21-    papers:
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A12 '"000576"' targets/dandisets.json | head -40; ls claims | head; ls claims/* | head -30
```

```
2839:   "dandiset": "000576",
2840-   "name": "Dataset of neurons and intracranial EEG from human amygdala during aversive dynamic visual stimulation",
2841-   "published_version": "0.231010.1811",
2842-   "asset_count": 27,
2843-   "size_gb": 2.19,
2844-   "data_standards": [
2845-    "Neurodata Without Borders (NWB)"
2846-   ],
2847-   "species": [
2848-    "Homo sapiens - Human"
2849-   ],
2850-   "approaches": [
2851-    "electrophysiological approach"
000003
000004
000005
000006
000008
000009
000010
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n -E "^\s+[a-z_]+:" claims/*/*.yaml | sed -E 's/.*:\s+([a-z_]+):.*/\1/' | sort | uniq -c | sort -rn | head -40
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

[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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
cd $TMPDIR && python3 -c "
import fitz;d=fitz.open('paper/10.1016-j.neuroimage.2020.116705.pdf')
for i in [1,2,3,4,5]:
  d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -r 110 -f 2 -l 6 -png paper/10.1016-j.neuroimage.2020.116705.pdf pg && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "import pypdfium2" 2>&1; python3 -c "import pdfplumber" 2>&1; python3 -c "import pypdf; print('pypdf')" 2>&1; which mutool gs magick convert 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf; print('pypdf')
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuroimage.2020.116705.pdf",
 "pages": "2-6"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
from scipy.stats import spearmanr, fisher_exact, chi2_contingency, mannwhitneyu, ttest_ind
d=[-0.66,0.26,-0.67,0.35,-0.91,-1.22,-0.33,-1.13,-0.09,-0.39,-0.17,-0.59,-0.82,-0.68]
h=[0.79,-0.57,0.35,-0.66,1.75,0.5,-0.59,1.07,-0.52,0.04,0.25,0.05,-0.44,-0.3]
print(spearmanr(d,h))
soz=[0,1,0,1,0,0,1,0,1,0,1,0,1,1]
hn=[x for x,s in zip(h,soz) if not s]; hs=[x for x,s in zip(h,soz) if s]
dn=[x for x,s in zip(d,soz) if not s]; ds=[x for x,s in zip(d,soz) if s]
print(mannwhitneyu(hn,hs),ttest_ind(hn,hs),mannwhitneyu(dn,ds),ttest_ind(dn,ds))
print(fisher_exact([[7,0],[1,6]]))
from statsmodels.stats.proportion import proportion_confint as pc
for k,n in [(7,7),(6,7),(13,14)]:
  for m in ['beta','wilson','binom_test']: print(k,n,m,pc(k,n,method=m))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import spearmanr, fisher_exact, chi2_contingency, mannwhitneyu, ttest_ind
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Write**

```json
{
 "file_path": "claims/000576/10.1016-j.neuroimage.2020.116705.yaml",
 "content": "# Claims for Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, on dandiset 000576.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF),\n# main text, figure legends, Tables 1 and 2 and Methods. Table 2 was read from the extracted\n# text, in which minus signs print as a replacement glyph; its signs agree with the counts the\n# Results give (12 of 14 negative DELTA MI, HGP MI positive in 7 of 7 nSOZ and negative in 6 of\n# 7 SOZ amygdalae). The PDF pages could not be rendered here. The supplement (Appendix A, online)\n# was not supplied; the text cites it only for Fig. S2 (waveforms and inter-spike intervals of\n# the neurons of each patient), which carries no finding. The Results also cite \"Methods 7.8\"\n# for the other spectral bands; no such section exists in the text, and section 4.8 lists the\n# bands without results.\n# The data descriptor of the same data (Fedele et al. 2021, Sci Data, doi:10.1038/s41597-020-00790-x,\n# in paper/) was read for the layout of the deposited data only; no claim is taken from it.\n#\n# Code: the paper links no analysis code. The data descriptor says scripts for reading the NIX\n# files and for its own Figs 2 and 3 come with the G-Node and OpenNeuro deposits; these are not\n# the paper's analysis and were not read. Every method below is from the paper's Methods (4.7\n# to 4.11), Results and figure legends.\n#\n# Data the paper used (Methods 4.1, Tables 1 and 2). Nine patients with drug-resistant mesial\n# temporal lobe epilepsy, 14 implanted amygdalae: 7 outside the seizure onset zone (nSOZ:\n# patients 1 L, 2 L, 3 L, 4 L, 6 L, 7 L, 8 L) and 7 within it (SOZ, starred in the tables:\n# 1 R, 2 R, 5 R, 6 R, 7 R, 9 L, 9 R). Table 2 numbers the amygdalae 1 to 14 in that order by\n# patient, left before right. Task: silent videos in a block design, blocks of 24 s of dynamic\n# fearful faces (AVERSIVE, eight blocks) or dynamic landscapes (NEUTRAL, nine blocks), each\n# block preceded by a repeated 2 s neutral landscape baseline (Methods 4.4); the data\n# descriptor stores these as trials of 26 s. iEEG from depth macroelectrodes at 4 kHz,\n# down-sampled to 2 kHz, re-referenced to a bipolar montage (one bipolar channel in each\n# amygdala, Fig. 2B). Microwires at the electrode tips at 32 kHz, spike sorted with Combinato;\n# 50 clusters from 9 amygdalae, 41 with firing rate above 1 Hz. Measured variables: delta and\n# high gamma power envelopes of the macro iEEG (DELTA, HGP), high gamma power of the microwire\n# signals (muHGP), spike times per unit, and the BOLD time course of each amygdala from a\n# pre-operative fMRI session (7 of 9 patients, 9 amygdalae with BOLD in Table 2).\n#\n# Outside data (step 4). The BOLD time courses come from the clinical fMRI of these patients,\n# part of the cohort of Schacher et al. (2006, Neurology 66, 81-87). The paper names no public\n# deposit of them, and the data descriptor lists only iEEG, spikes and electrode positions. The\n# claims that use BOLD are marked with_inputs. The muHGP claims need the continuous microwire\n# signals; the data descriptor says only spike times and mean waveforms of the microwire data\n# were shared.\n#\n# Inconsistencies in the paper, recorded here and in the claims that they touch: the abstract\n# says 5 participants had microwires, Results 2.3 says 9 amygdalae, and the MUA column of\n# Table 1 lists 8 amygdalae of 6 patients (1 L and R, 2 L and R, 3 L, 4 L, 5 R, 8 L), three of\n# them SOZ, while Discussion 3.4 says there were no microwire recordings from SOZ amygdalae.\n# Methods 4.4 gives eight AVERSIVE and nine NEUTRAL blocks; the data descriptor, quoting\n# Schacher et al., gives eight of each. The Table 2 legend says BOLD correlated positively\n# with HGP in 5 of 5 amygdalae; the Results and the table's own values give 3 of 5 nSOZ.\n#\n# Method of the iEEG power analysis, from Methods 4.8 and 4.11, used by several claims:\n# bipolar amygdala channel; IIR Butterworth filter of order 2 per band, delta 1-4 Hz, theta\n# 4-8, alpha 8-15, beta 15-30, gamma 30-60, high gamma above 60 Hz; amplitude of the Hilbert\n# analytic signal; smoothed with a 1 s window; baseline corrected with the 1 s before the\n# start of each sequence; z-scored within each trial; time-point by time-point linear mixed\n# model Power ~ condition + (1|Patients) on all single trials; cluster-based permutation over\n# time with 500 permutations of the AVERSIVE and NEUTRAL labels across participants,\n# significance at p < 0.05. Modulation index MI = AVERSIVE minus NEUTRAL time-averaged power\n# over the temporal clusters where the conditions differ significantly. Open details, each\n# with the readings the text allows (the author runs them all):\n# - HGP upper band edge. The text says only \">60 Hz\". Reading (a) high-pass at 60 Hz up to\n#   the Nyquist frequency of the 2 kHz signal; the macro pass-band was 0.5-1000 Hz (Methods 4.7).\n# - Filter direction (one-pass or zero-phase) and the shape of the 1 s smoothing window are\n#   not given; with 1 s smoothing they cannot change the outcome, and a zero-phase filter and a\n#   boxcar window are used as standard choices.\n# - \"z-scored all data within each trial\": (a) mean and SD over the whole 26 s trial\n#   including the baseline; (b) mean and SD of the pre-sequence baseline; (c) over all trials\n#   of the patient. Methods 4.8 also names two baseline variants (the mean of all epochs, the\n#   mean of the previous epoch), reported as quantitatively similar; they are variants.\n# - Which amygdalae enter the group test: (a) the 7 nSOZ amygdalae (Results 2.1, \"In nSOZ\n#   amygdalae\"); (b) all 14 (Fig. 1 legend, \"Over the group of participants\"). Patients with\n#   two amygdalae have one random factor level (the formula names only Patients).\n# - The cluster-forming threshold and cluster statistic are not given: (a) time points with\n#   p < 0.05 for the condition effect, cluster mass as the sum of the t (or F) values, as in\n#   FieldTrip (Oostenveld et al. 2011, which the paper cites for the method); (b) cluster\n#   length in time points.\n# - The group test: Methods 4.11 name the mixed model; Results 2.1 names unpaired t-tests\n#   corrected with random permutations. The mixed model is the main reading, the unpaired\n#   t-test (AVERSIVE against NEUTRAL trials, pooled) a variant.\n# - The MI window: (a) the group-level clusters of Fig. 1B and 1C applied to every amygdala;\n#   (b) clusters found per amygdala. The Results say the window \"occurred at stimulus onset in\n#   HGP and was sustained throughout the trial in DELTA\", which favours (a) but does not fix it.\n#\n# Method of the neuron analyses (Methods 4.11, Fig. 3 legend): Firing Rate Variability FRV =\n# AVERSIVE minus NEUTRAL mean firing rate over the whole time interval of neuronal firing;\n# Spatial Synchronization Index SSI = mean Spearman correlation of a neuron's firing rate with\n# that of each neuron of the same amygdala on a different microwire; correlations are\n# Spearman's; multiple linear regression of the per-neuron firing correlation (with HGP or\n# BOLD) on FRV and SSI. Open details:\n# - The time base of the firing rate correlations is given only per figure: Fig. 3A bins of\n#   100 ms smoothed over 1 s; Fig. 3D a 15 s smoothing window; Methods 4.10 (for BOLD) iEEG\n#   power down-sampled to 1.5 s and smoothed over 5 points (7.5 s). Each claim names which\n#   readings apply.\n# - Whether a correlation is computed over the concatenated time course of the session (or of\n#   one condition's blocks) or per trial and then averaged is not given: (i) concatenated;\n#   (ii) per trial, averaged.\n# - FRV over (a) the 24 s blocks only, or (b) the full 26 s trials.\n# - A neuron with no neighbour on another microwire has no SSI; it is left out of claims that\n#   use SSI, the only reading under which SSI is defined.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000576\"\npaper: doi:10.1016/j.neuroimage.2020.116705\nclaims:\n- id: fig1b-delta-decrease\n  statement: Delta power (1-4 Hz) in the amygdala is lower during AVERSIVE than during NEUTRAL\n    sequences, and the reduction lasts through the AVERSIVE sequence.\n  source: Results 2.1, paragraph 1; Figure 1B\n  quote: In nSOZ amygdalae, DELTA band power was consistently reduced throughout the duration of\n    the AVERSIVE sequence (Fig. 1B)\n  statistics:\n  - test: linear mixed model per time point, cluster-based permutation correction (Fig. 1 legend\n      calls it cluster analysis)\n    p: 0.05\n    p_relation: \"<\"\n  criterion: The iEEG power method of the opening comment (Methods 4.8 and 4.11), run under each\n    reading listed there (z-scoring, amygdala set, cluster statistic, mixed model or the\n    unpaired t-test variant). Reproduced when, under the mixed model, at least one cluster with\n    AVERSIVE below NEUTRAL has permutation p < 0.05 and the AVERSIVE mean delta power is below\n    the NEUTRAL mean over the 24 s block, under every reading of the open details; blocked as\n    methods_underspecified when the readings disagree. The paper gives no number for how much of\n    the block the reduction must cover (\"throughout the duration\"); the extent of the\n    significant clusters is reported, and the claim is partially reproduced when the clusters\n    cover less than half of the 24 s block.\n- id: fig1c-hgp-increase-first-2s\n  statement: High gamma power (above 60 Hz) is higher during AVERSIVE than during NEUTRAL\n    sequences in the first 2 s of the sequence.\n  source: Results 2.1, paragraph 1; Figure 1C\n  quote: The HGP was enhanced in response to aversive stimuli during the first 2 s of the\n    AVERSIVE sequence presentation (Fig. 1C, unpaired t-tests, corrected for multiple comparisons\n    using random permutations, p < 0.05)\n  statistics:\n  - test: unpaired t-tests, corrected for multiple comparisons using random permutations (Results);\n      linear mixed model with cluster-based permutation (Methods 4.11)\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As fig1b-delta-decrease, for HGP. Reproduced when a cluster with AVERSIVE above\n    NEUTRAL with permutation p < 0.05 lies within, or begins within, the first 2 s after sequence\n    onset, under every reading of the open details; the cluster's start and end are reported.\n- id: other-bands-no-effect\n  statement: No AVERSIVE against NEUTRAL difference is found in the theta, alpha, beta and gamma\n    (30-60 Hz) bands.\n  source: Results 2.1, paragraph 1; bands in Methods 4.8\n  quote: Since no effect was observed in the other spectral bands (see Methods 7.8), in the\n    following we focus on DELTA power and HGP\n  criterion: A claim of absence, judged on the paper's test, the mixed model with cluster-based\n    permutation of Methods 4.11 (p < 0.05), run on theta (4-8 Hz), alpha (8-15 Hz), beta (15-30\n    Hz) and gamma (30-60 Hz) as in fig1b-delta-decrease. Reproduced when no band has a cluster\n    with p < 0.05; not reproduced when any does; the cluster p-values and extents are reported.\n    The \"Methods 7.8\" the Results cite is not in the text, so the test cannot be checked against\n    it.\n- id: fig1d-delta-hgp-mi-correlation\n  statement: Across the 14 amygdalae, the DELTA modulation index and the HGP modulation index\n    are negatively correlated.\n  source: Results 2.1, paragraph 2; Figure 1D\n  quote: MI and HGP-MI were negatively correlated across all amygdalae\n  statistics:\n  - test: Spearman correlation\n    statistic: r = -0.67\n    p: 0.01\n    n: 14 amygdalae\n  expected:\n  - quantity: Spearman r between DELTA MI and HGP MI across amygdalae\n    value: -0.67\n    tolerance: 0.067\n  depends_on:\n  - table2-mi-values\n  criterion: MI per amygdala as in table2-mi-values (Methods 4.11), each reading of the MI\n    window. Reproduced when r is within tolerance and p < 0.05 under every reading; partially\n    reproduced when r is negative with p < 0.05 but outside tolerance. The Spearman r of the\n    printed Table 2 values is reported as well.\n- id: table2-mi-values\n  statement: The modulation indices of DELTA and HGP for each of the 14 amygdalae are as printed\n    in Table 2.\n  source: Table 2, columns Modulation index (MI) of iEEG, DELTA and HGP\n  inferred: Values read from Table 2, which no sentence states one by one. Minus signs are\n    garbled in the extracted text; the signs used here agree with the counts the Results give.\n  expected:\n  - {quantity: DELTA MI amygdala 1 (patient 1 L), value: -0.66, tolerance: 0.066}\n  - {quantity: HGP MI amygdala 1 (patient 1 L), value: 0.79, tolerance: 0.079}\n  - {quantity: DELTA MI amygdala 2 (patient 1 R, SOZ), value: 0.26, tolerance: 0.026}\n  - {quantity: HGP MI amygdala 2 (patient 1 R, SOZ), value: -0.57, tolerance: 0.057}\n  - {quantity: DELTA MI amygdala 3 (patient 2 L), value: -0.67, tolerance: 0.067}\n  - {quantity: HGP MI amygdala 3 (patient 2 L), value: 0.35, tolerance: 0.035}\n  - {quantity: DELTA MI amygdala 4 (patient 2 R, SOZ), value: 0.35, tolerance: 0.035}\n  - {quantity: HGP MI amygdala 4 (patient 2 R, SOZ), value: -0.66, tolerance: 0.066}\n  - {quantity: DELTA MI amygdala 5 (patient 3 L), value: -0.91, tolerance: 0.091}\n  - {quantity: HGP MI amygdala 5 (patient 3 L), value: 1.75, tolerance: 0.175}\n  - {quantity: DELTA MI amygdala 6 (patient 4 L), value: -1.22, tolerance: 0.122}\n  - {quantity: HGP MI amygdala 6 (patient 4 L), value: 0.5, tolerance: 0.05}\n  - {quantity: DELTA MI amygdala 7 (patient 5 R, SOZ), value: -0.33, tolerance: 0.033}\n  - {quantity: HGP MI amygdala 7 (patient 5 R, SOZ), value: -0.59, tolerance: 0.059}\n  - {quantity: DELTA MI amygdala 8 (patient 6 L), value: -1.13, tolerance: 0.113}\n  - {quantity: HGP MI amygdala 8 (patient 6 L), value: 1.07, tolerance: 0.107}\n  - {quantity: DELTA MI amygdala 9 (patient 6 R, SOZ), value: -0.09, tolerance: 0.009}\n  - {quantity: HGP MI amygdala 9 (patient 6 R, SOZ), value: -0.52, tolerance: 0.052}\n  - {quantity: DELTA MI amygdala 10 (patient 7 L), value: -0.39, tolerance: 0.039}\n  - {quantity: HGP MI amygdala 10 (patient 7 L), value: 0.04, tolerance: 0.005}\n  - {quantity: DELTA MI amygdala 11 (patient 7 R, SOZ), value: -0.17, tolerance: 0.017}\n  - {quantity: HGP MI amygdala 11 (patient 7 R, SOZ), value: 0.25, tolerance: 0.025}\n  - {quantity: DELTA MI amygdala 12 (patient 8 L), value: -0.59, tolerance: 0.059}\n  - {quantity: HGP MI amygdala 12 (patient 8 L), value: 0.05, tolerance: 0.005}\n  - {quantity: DELTA MI amygdala 13 (patient 9 L, SOZ), value: -0.82, tolerance: 0.082}\n  - {quantity: HGP MI amygdala 13 (patient 9 L, SOZ), value: -0.44, tolerance: 0.044}\n  - {quantity: DELTA MI amygdala 14 (patient 9 R, SOZ), value: -0.68, tolerance: 0.068}\n  - {quantity: HGP MI amygdala 14 (patient 9 R, SOZ), value: -0.3, tolerance: 0.03}\n  criterion: MI = AVERSIVE minus NEUTRAL time-averaged z-scored power envelope over the temporal\n    clusters where the conditions differ significantly (Methods 4.11, Table 2 legend), with the\n    preprocessing and the readings of the opening comment. Tolerance is 10% of each value, and\n    0.005 (half the last printed digit) where 10% is smaller, as the table rounds to two\n    decimals. Reproduced when, under one reading, all 28 values are within tolerance; partially\n    reproduced when the signs of all 28 agree; the number within tolerance is reported for every\n    reading.\n- id: table2-delta-reduced-12-of-14\n  statement: DELTA power is reduced (negative MI) in 12 of the 14 amygdalae, whether inside or\n    outside the SOZ.\n  source: Results 2.1, paragraph 3; Table 2\n  quote: DELTA power was reduced in 12 of 14 amygdalae (negative MI in Table 2), irrespective of\n    whether the amygdalae were within the SOZ or not\n  expected:\n  - quantity: amygdalae with negative DELTA MI\n    value: 12\n    tolerance: 1.2\n  depends_on:\n  - table2-mi-values\n  criterion: Count of negative DELTA MI over the 14 amygdalae of table2-mi-values, under each\n    reading of the MI window. Reproduced when the count is 11 to 13 (12 with 10%) under every\n    reading and amygdalae with negative MI are found both inside and outside the SOZ.\n- id: table2-hgp-mi-positive-nsoz\n  statement: All 7 amygdalae outside the SOZ have a positive HGP MI, while the response is\n    absent in amygdalae within the SOZ (6 of 7 negative).\n  source: Results 2.1, paragraph 3; Table 2 and its legend\n  quote: All amygdalae outside SOZ showed a positive HGP-MI in response to AVERSIVE videos, while\n    this response was absent in amygdalae within the SOZ (p 1⁄4 0.009)\n  statistics:\n  - about: HGP MI, nSOZ against SOZ amygdalae\n    test: not named\n    p: 0.009\n    n: 7 nSOZ and 7 SOZ amygdalae\n  expected:\n  - quantity: nSOZ amygdalae with positive HGP MI\n    value: 7\n    tolerance: 0\n  - quantity: SOZ amygdalae with negative HGP MI\n    value: 6\n    tolerance: 0\n  depends_on:\n  - table2-mi-values\n  criterion: Counts from the HGP MI of table2-mi-values, under each reading of the MI window;\n    counts of 7 amygdalae have no room for a 10% tolerance, so they must match. The test behind\n    p = 0.009 is not named; readings are (a) Wilcoxon rank-sum of HGP MI, nSOZ against SOZ; (b)\n    unpaired t-test of HGP MI (the test the Results name for Fig. 1C); (c) Fisher's exact or\n    chi-square test of the counts of positive MI. Reproduced when both counts match and the\n    difference has p < 0.05 under one of the readings; each reading's p is reported.\n- id: fig1e-hgp-not-delta-distinguishes-soz\n  statement: The HGP MI, but not the DELTA MI, distinguishes amygdalae within the SOZ from those\n    outside it.\n  source: Figure 1E legend\n  quote: HGP but not DELTA distinguishes between amygdalae within SOZ and outside SOZ (p 1⁄4 0.019,\n    not corrected)\n  statistics:\n  - about: HGP MI, SOZ against nSOZ\n    test: not named\n    p: 0.019\n    corrected: not corrected\n    n: 7 nSOZ and 7 SOZ amygdalae\n  depends_on:\n  - table2-mi-values\n  criterion: The legend names no test. Readings are (a) Wilcoxon rank-sum and (b) unpaired\n    t-test, of the MI of table2-mi-values, nSOZ against SOZ, uncorrected, threshold p < 0.05\n    (Methods 4.11). Reproduced when, under a reading, HGP MI differs with p < 0.05 and DELTA MI\n    does not; the DELTA part is a claim of absence judged on the same test. Not reproduced when\n    HGP does not differ or DELTA does under every reading; blocked as methods_underspecified\n    when the readings disagree.\n- id: hgp-soz-sensitivity-specificity\n  statement: HGP enhancement indicates amygdalar functional integrity (outside the SOZ) with\n    sensitivity 7/7 (100%), specificity 6/7 (86%) and accuracy 13/14 (93%).\n  source: Results 2.1, paragraph 3; Methods 4.11, paragraph 4\n  quote: With sensitivity (7/7 1⁄4 100% CI [66–100]%), high specificity (6/7 1⁄4 86% CI [42 99]%) and\n    accuracy 93% (13/14, CI [66–99]%), HGP enhancement indicated amygdalar functional integrity\n  statistics:\n  - about: sensitivity, 7 of 7\n    ci: {level: 0.95, low: 66, high: 100, unit: \"%\"}\n  - about: specificity, 6 of 7\n    ci: {level: 0.95, low: 42, high: 99, unit: \"%\"}\n  - about: accuracy, 13 of 14\n    ci: {level: 0.95, low: 66, high: 99, unit: \"%\"}\n  expected:\n  - quantity: sensitivity, nSOZ amygdalae with the HGP effect\n    value: 7\n    tolerance: 0\n    unit: of 7\n  - quantity: specificity, SOZ amygdalae without the HGP effect\n    value: 6\n    tolerance: 0\n    unit: of 7\n  - quantity: accuracy\n    value: 13\n    tolerance: 0\n    unit: of 14\n  depends_on:\n  - table2-mi-values\n  criterion: The effect is HGP enhancement, a positive HGP MI (Methods 4.11 define TP as the\n    effect in a nSOZ amygdala, FP in a SOZ amygdala, FN its absence in nSOZ, TN its absence in\n    SOZ). Methods 4.11 say the effect was \"either HGP enhancement in the first 2 s or sustained\n    delta decrease\"; the Results apply it to HGP, which is followed here. Counts must match (no\n    tolerance on counts of 7). The 95% confidence intervals used \"the binomial distribution\";\n    the exact (Clopper-Pearson) interval is the reading, and its bounds are reported beside the\n    printed ones.\n- id: fig1f-hgp-more-specific-than-delta\n  statement: The HGP response is more specific than the DELTA response for indicating amygdalar\n    dysfunction within the SOZ, by a chi-square test that is not significant (p about 0.2).\n  source: Figure 1F legend\n  quote: The HGP response exceeds the DELTA response in specificity when indicating the\n    amygdala’s dysfunction within SOZ (p~0.2 HGP 5/5 DELTA 1/5, chi2-test)\n  statistics:\n  - test: chi-square test\n    p: 0.2\n    n: HGP 5/5, DELTA 1/5 (as printed)\n  depends_on:\n  - table2-mi-values\n  criterion: The paper does not say which amygdalae form the printed counts 5/5 and 1/5, and no\n    subset of Table 2 is named that gives them. Readings are (a) the specificity counts as in\n    Methods 4.11 over the 7 SOZ amygdalae, HGP effect absent (HGP MI not positive) against\n    DELTA effect absent (DELTA MI not negative), compared with a chi-square test of the 2 by 2\n    table; (b) the printed counts 5/5 against 1/5 in a chi-square test. Reproduced when HGP\n    specificity exceeds DELTA specificity under reading (a); the chi-square p of both readings\n    is reported against the printed p about 0.2. Blocked as methods_underspecified if the\n    readings disagree on which is more specific.\n- id: fig2-participant4-bold-correlations\n  statement: In the left amygdala of Participant 4, the BOLD time course is negatively correlated\n    with DELTA power and positively correlated with HGP over the video sequence.\n  source: Results 2.2, paragraph 2; Figure 2A and 2C; Table 2, amygdala 6\n  quote: BOLD response and DELTA power were negatively correlated during presentation of video\n    sequence (correlation of BOLDDELTA time-courses r 1⁄4 �0.48 p < 0.01), while BOLD and HGP were\n    positively correlated (correlation BOLD-HGP Spearman’s r 1⁄4 0.41 p < 0.01)\n  statistics:\n  - about: BOLD against DELTA\n    test: Spearman correlation\n    statistic: r = -0.48\n    p: 0.01\n    p_relation: \"<\"\n    corrected: FDR (Table 2 legend)\n  - about: BOLD against HGP\n    test: Spearman correlation\n    statistic: r = 0.41\n    p: 0.01\n    p_relation: \"<\"\n    corrected: FDR (Table 2 legend)\n  expected:\n  - quantity: Spearman r, BOLD against DELTA, patient 4 L\n    value: -0.48\n    tolerance: 0.048\n  - quantity: Spearman r, BOLD against HGP, patient 4 L\n    value: 0.41\n    tolerance: 0.041\n  data: with_inputs\n  criterion: Methods 4.10. The iEEG power envelope (Methods 4.8) is smoothed, down-sampled to the\n    1.5 s BOLD time points and smoothed over 5 time points (7.5 s), then correlated (Spearman)\n    with the BOLD time course of the amygdala VOI over the video sequence. The BOLD time course\n    is outside data, the clinical fMRI of the patient (Methods 4.6), for which the paper names\n    no deposit. The smoothing before down-sampling and the 5-point window shape are not given;\n    the 1 s smoothing of Methods 4.8 and a boxcar are used, standard choices. Whether the iEEG\n    and BOLD time courses are aligned at sequence onset with no lag is not stated beyond the\n    smoothing that \"takes into account the time-lag\"; no lag is the reading. Reproduced when\n    both r are within tolerance with p < 0.01 after FDR.\n- id: table2-bold-correlations-group\n  statement: Across amygdalae with BOLD, DELTA power and BOLD are negatively correlated in 4 of 5\n    nSOZ amygdalae, while HGP and BOLD are positively correlated in 3 of 5 nSOZ and 1 of 4 SOZ\n    amygdalae.\n  source: Results 2.2, paragraph 3; Table 2; Figure 2C\n  quote: DELTA power and BOLD responses showed a negative correlation in 4/5 nSOZ amygdalae, while\n    the correlation of HGP and BOLD was positive in the 3/5 the nSOZ amygdalae and 1/4 SOZ\n    amygdalae (Table 2, Fig. 2C)\n  statistics:\n  - about: per-amygdala Spearman correlations\n    test: Spearman correlation\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 9 amygdalae of 7 patients (5 nSOZ, 4 SOZ)\n  expected:\n  - quantity: nSOZ amygdalae with significant negative BOLD-DELTA correlation\n    value: 4\n    tolerance: 0\n    unit: of 5\n  - quantity: nSOZ amygdalae with significant positive BOLD-HGP correlation\n    value: 3\n    tolerance: 0\n    unit: of 5\n  - quantity: SOZ amygdalae with significant positive BOLD-HGP correlation\n    value: 1\n    tolerance: 0\n    unit: of 4\n  data: with_inputs\n  depends_on:\n  - fig2-participant4-bold-correlations\n  criterion: The correlation of fig2-participant4-bold-correlations, for each of the 9 amygdalae\n    with BOLD in Table 2 (patients 1 R, 2 L, 2 R, 3 L, 4 L, 7 L, 7 R, 8 L, 9 R), p-values FDR\n    corrected across them (Table 2 legend; the family is not given, readings (a) the 9 tests of\n    one band, (b) all 18 tests). Counts of 5 or fewer must match. The Table 2 legend states 5/5\n    positive BOLD-HGP correlations, which the table's own values do not support; the Results'\n    3/5 and 1/4 are the claim.\n- id: bold-hgp-uncorrelated-low-mi\n  statement: The two nSOZ amygdalae without a significant HGP-BOLD correlation have a very low\n    HGP MI.\n  source: Results 2.2, paragraph 3; Table 2 (amygdalae 10 and 12)\n  quote: the two nSOZ amygdalae that did not show a significant correlation between HGB and BOLD,\n    had a remarkably low MI for HGP (MI < 0.05, Table 2)\n  data: with_inputs\n  depends_on:\n  - table2-bold-correlations-group\n  - table2-mi-values\n  criterion: Reproduced when the nSOZ amygdalae without a significant positive HGP-BOLD\n    correlation in table2-bold-correlations-group are the two with the lowest HGP MI among the\n    5 nSOZ amygdalae with BOLD, both MI at most 0.055 (Table 2 prints 0.04 and 0.05, so \"MI <\n    0.05\" is read as below 0.05 within the rounding of the table, with the 10% tolerance).\n- id: neuron-count\n  statement: Spike sorting gave 50 putative neuron clusters from 9 amygdalae, of which 41 had a\n    firing rate above 1 Hz and were analysed.\n  source: Results 2.3, paragraph 1; Methods 4.9\n  quote: We identified 50 putative clusters of neurons (Niediek et al., 2016) from 9 amygdalae and\n    included those with firing rate >1 Hz (N 1⁄4 41 neurons) in further analysis\n  expected:\n  - quantity: clusters with firing rate above 1 Hz\n    value: 41\n    tolerance: 4.1\n  - quantity: putative clusters\n    value: 50\n    tolerance: 5\n  - quantity: amygdalae with clusters\n    value: 9\n    tolerance: 0\n  criterion: Mean firing rate over the recording (the whole task) above 1 Hz. The paper does not\n    give the interval over which the 1 Hz rate is taken; readings (a) all trials, (b) the whole\n    recording, as the dataset allows. Table 1 lists clusters in 8 amygdalae of 6 patients and\n    the abstract says 5 participants; the number of amygdalae and patients with units is\n    reported against all three. The dataset may hold only the clusters above 1 Hz (the data\n    descriptor applies the same 1 Hz rule), in which case 50 cannot be tested.\n- id: fig3a-firing-increase-aversive\n  statement: All 41 neurons fire more during AVERSIVE than during NEUTRAL sequences (FRV 0.26\n    plus or minus 0.15).\n  source: Results 2.3, paragraph 2; Figure 3A\n  quote: All 41 clusters of neurons increased their firing rate during the AVERSIVE condition\n    (Firing Rate Variation, FRV 1⁄4 0.26 �0.15)\n  expected:\n  - quantity: mean FRV across neurons\n    value: 0.26\n    tolerance: 0.15\n    unit: Hz (FRV is a difference of mean firing rates, Methods 4.11)\n  - quantity: neurons with positive FRV\n    value: 41\n    tolerance: 0\n    unit: of 41\n  depends_on:\n  - neuron-count\n  criterion: FRV per neuron is the AVERSIVE minus NEUTRAL mean firing rate over the whole time\n    interval of firing (Methods 4.11), under readings (a) the 24 s blocks, (b) the 26 s trials.\n    Tolerance is the stated spread (0.15). Reproduced when every neuron has FRV > 0 and the mean\n    is within tolerance under one reading; partially reproduced when the mean is within\n    tolerance and most neurons have FRV > 0. \"FRV\" is called Firing Rate Variation here and Firing\n    Rate Variability in Methods 4.11; it is the same measure.\n- id: fig3a-firing-gradual-sustained\n  statement: The neurons' firing rose gradually and stayed enhanced throughout the AVERSIVE\n    sequences, not as an immediate response at onset.\n  source: Results 2.3, paragraph 2; Figure 3A\n  quote: Contrary to our expectation of an immediate spiking onset, the neurons increased their\n    firing gradually and sustained enhanced firing throughout the AVERSIVE video sequences\n  depends_on:\n  - neuron-count\n  criterion: The paper gives no measure or test for this. Population AVERSIVE minus NEUTRAL\n    firing rate across the 41 neurons, time-locked to sequence onset, in 100 ms bins smoothed\n    over 1 s (Fig. 3A legend). The test is open; readings are (a) the difference averaged over\n    the first 2 s is smaller than over 2 to 24 s (gradual), with the difference positive in each\n    of the twelve 2 s bins of the block (sustained); (b) the time of the difference's first\n    peak is later than 2 s and the difference stays positive to 24 s. Reproduced when both\n    readings agree it holds, not reproduced when both agree it does not, blocked as\n    methods_underspecified otherwise. The curve is shown either way.\n- id: fig3b-firing-hgp-no-condition-difference\n  statement: Across neurons, the correlation of firing rate with macro-electrode HGP does not\n    differ between the AVERSIVE and NEUTRAL conditions.\n  source: Results 2.3, paragraph 3; Figure 3B, lower boxplot\n  quote: Across all neurons, the covariation of neuronal firing with HGP was not significantly\n    different between the two experimental conditions (Spearman’s r 1⁄4 0.17 �0.28 in AVERSIVE,\n    0.18 �0.18 in NEUTRAL; Wilcoxon paired test, p > 0.05)\n  statistics:\n  - test: Wilcoxon paired test\n    p: 0.05\n    p_relation: \">\"\n    n: 41 neurons\n  expected:\n  - quantity: mean Spearman r firing rate against HGP, AVERSIVE\n    value: 0.17\n    tolerance: 0.28\n  - quantity: mean Spearman r firing rate against HGP, NEUTRAL\n    value: 0.18\n    tolerance: 0.18\n  depends_on:\n  - neuron-count\n  criterion: A claim of absence, judged on the paper's test, a Wilcoxon signed-rank test of\n    per-neuron Spearman r (AVERSIVE against NEUTRAL) at p < 0.05. HGP is the bipolar macro\n    channel of the neuron's amygdala (Methods 4.8 envelope). Open time base, readings (a) 100 ms\n    bins smoothed over 1 s (Fig. 3A legend), (b) 1.5 s with 5-point smoothing (Methods 4.10),\n    (c) 15 s smoothing (Fig. 3D legend); and (i) concatenated blocks of the condition, (ii) per\n    block and averaged. Reproduced when the test finds no difference, not reproduced when it\n    does; the effect size is reported for every reading. Tolerances on the means are the stated\n    spreads.\n- id: fig3b-firing-muhgp-higher-aversive\n  statement: Across neurons, the correlation of firing rate with microwire high gamma power\n    (muHGP) is higher in the AVERSIVE than in the NEUTRAL condition.\n  source: Results 2.3, paragraph 3; Figure 3B, upper boxplot\n  quote: the covariation of neuronal firing with μHGP was higher during AVERSIVE than during\n    NEUTRAL conditions (Spearman’s r 1⁄4 0.51 �0.18 during AVERSIVE, 0.43 �0.16 during NEUTRAL;\n    Wilcoxon paired test, p < 0.01)\n  statistics:\n  - test: Wilcoxon paired test\n    p: 0.01\n    p_relation: \"<\"\n    n: 41 neurons\n  expected:\n  - quantity: mean Spearman r firing rate against muHGP, AVERSIVE\n    value: 0.51\n    tolerance: 0.18\n  - quantity: mean Spearman r firing rate against muHGP, NEUTRAL\n    value: 0.43\n    tolerance: 0.16\n  depends_on:\n  - neuron-count\n  criterion: As fig3b-firing-hgp-no-condition-difference, with HGP from the microwire signal of\n    the neuron's own microwire (the paper says muHGP is recorded \"locally at the level of the\n    microwires\"; which microwire, the neuron's own or a neighbour, is not stated, reading (a)\n    its own, (b) the mean over the bundle). The paper does not give the microwire LFP filtering;\n    the high gamma method of Methods 4.8 is the reading. Needs the continuous microwire signals.\n    Reproduced when the Wilcoxon signed-rank test gives p < 0.01 with AVERSIVE higher under\n    every reading, and the means are within the stated spreads.\n- id: fig3c-ssi-frv-correlation\n  statement: Across neurons, the spatial synchronization index (SSI) is strongly positively\n    correlated with the firing rate variability (FRV).\n  source: Results 2.3, paragraph 4; Figure 3C; Figure 4A\n  quote: We found a strong positive correlation across all participants between the SSI and FRV\n    (Spearman’s r 1⁄4 0.78, p < 1e-7)\n  statistics:\n  - test: Spearman correlation\n    statistic: r = 0.78\n    p: 1.0e-7\n    p_relation: \"<\"\n    n: neurons with an SSI\n  expected:\n  - quantity: Spearman r, SSI against FRV\n    value: 0.78\n    tolerance: 0.078\n  depends_on:\n  - fig3a-firing-increase-aversive\n  criterion: SSI per neuron is the mean Spearman correlation of its firing rate with each neuron\n    of the same amygdala on a different microwire (Methods 4.11, Fig. 3C legend); FRV as in\n    fig3a-firing-increase-aversive. The firing rate time base and the span (whole session) are\n    open, readings (a) 100 ms bins smoothed over 1 s, (b) 15 s smoothing, over the whole session.\n    Reproduced when r is within tolerance and p < 1e-7 under one reading, and r > 0 with p < 0.05\n    under every reading; partially reproduced when r > 0 with p < 0.05 under every reading but\n    no reading gives the value.\n- id: fig3d-firing-correlations-modalities\n  statement: Across neurons, the ongoing firing rate correlates positively with muHGP (0.27),\n    HGP (0.19) and BOLD (0.23), and the correlation is lowest with HGP.\n  source: Results 2.3, paragraph 5; Figure 3D and its inset\n  quote: Across all neurons and participants, the ongoing firing rate positively correlated with\n    μHGP (Spearman’s r 1⁄4 0.27 �0.15), HGP (Spearman’s r 1⁄4 0.19 � 0.17) and BOLD (Spearman’s r\n    1⁄4 0.23 �0.20) ... Across all recording modalities, the correlation of the firing rate and\n    other measures was lowest with HGP (Wilcoxon’s paired test, p < 1e-2)\n  statistics:\n  - about: correlation with HGP against those with muHGP and with BOLD\n    test: Wilcoxon paired test\n    p: 0.01\n    p_relation: \"<\"\n    n: 41 neurons\n  expected:\n  - quantity: mean Spearman r, firing rate against muHGP\n    value: 0.27\n    tolerance: 0.15\n  - quantity: mean Spearman r, firing rate against HGP\n    value: 0.19\n    tolerance: 0.17\n  - quantity: mean Spearman r, firing rate against BOLD\n    value: 0.23\n    tolerance: 0.2\n  data: with_inputs\n  depends_on:\n  - neuron-count\n  criterion: Per neuron, Spearman r of the firing rate with each measure over the video sequence,\n    15 s smoothing (Fig. 3D legend) as reading (a), the Methods 4.10 time base (1.5 s, 5 points)\n    as reading (b). The HGP part uses the dataset alone and is judged by itself; muHGP needs the\n    microwire signals and BOLD the outside fMRI data. \"Lowest with HGP\" is read as two Wilcoxon\n    signed-rank tests, HGP against muHGP and HGP against BOLD, each p < 0.01. Reproduced when the\n    three means are within their stated spreads and both tests hold; partially reproduced when\n    only the parts testable on the data available hold, which the notes say.\n- id: fig4b-regression-firing-hgp\n  statement: The per-neuron correlation of firing rate with HGP is described by both FRV and SSI\n    in a multiple linear regression.\n  source: Results 2.4, paragraph 1; Figure 4B\n  quote: We found that the co-modulation between neuronal firing and HGP is described by both FVR\n    and SSI (Fig. 4B, r 1⁄4 0.59, p < 1e-4)\n  statistics:\n  - test: multiple linear regression\n    statistic: r = 0.59\n    p: 1.0e-4\n    p_relation: \"<\"\n  expected:\n  - quantity: model r, firing-HGP correlation on FRV and SSI\n    value: 0.59\n    tolerance: 0.059\n  depends_on:\n  - fig3c-ssi-frv-correlation\n  - fig3d-firing-correlations-modalities\n  criterion: Dependent variable the per-neuron Spearman r of firing rate with HGP (as in\n    fig3d-firing-correlations-modalities), independent variables FRV and SSI (Methods 4.11). The\n    paper does not say what r is; readings (a) the multiple correlation R of the least-squares\n    fit, (b) Spearman r of fitted against observed values. \"Described by both\" is read as both\n    coefficients positive with p < 0.05. Reproduced when the model p < 1e-4, r is within\n    tolerance under one reading, and both coefficients hold.\n- id: fig4c-regression-firing-bold\n  statement: The per-neuron correlation of firing rate with BOLD is described by FRV but not by\n    SSI.\n  source: Results 2.4, paragraph 1; Figure 4C\n  quote: while the co-modulation between neuronal firing and BOLD is described by FRV (Fig. 4C,\n    Spearman’s r 1⁄4 0.69, p < 1e-4), but not SSI\n  statistics:\n  - test: multiple linear regression\n    statistic: Spearman's r = 0.69\n    p: 1.0e-4\n    p_relation: \"<\"\n  expected:\n  - quantity: model r, firing-BOLD correlation on FRV and SSI\n    value: 0.69\n    tolerance: 0.069\n  data: with_inputs\n  depends_on:\n  - fig3c-ssi-frv-correlation\n  - fig3d-firing-correlations-modalities\n  criterion: As fig4b-regression-firing-hgp, dependent variable the per-neuron Spearman r of\n    firing rate with BOLD. Reproduced when the model p < 1e-4, r is within tolerance under a\n    reading, the FRV coefficient has p < 0.05 and the SSI coefficient p >= 0.05 (the absence\n    judged at the paper's threshold, p < 0.05, Methods 4.11).\n- id: fig4d-hgp-bold-covariation\n  statement: Across neurons, the correlation of firing with HGP is positively correlated with the\n    correlation of firing with BOLD.\n  source: Results 2.4, paragraph 2; Figure 4D\n  quote: Fig. 4D displays the covariation of neuronal firing with BOLD (x-axis) and HGP (y-axis)\n    (Spearman’s r 1⁄4 0.72, p < 1e-3)\n  statistics:\n  - test: Spearman correlation\n    statistic: r = 0.72\n    p: 1.0e-3\n    p_relation: \"<\"\n    n: 41 neurons\n  expected:\n  - quantity: Spearman r across neurons, firing-BOLD r against firing-HGP r\n    value: 0.72\n    tolerance: 0.072\n  data: with_inputs\n  depends_on:\n  - fig3d-firing-correlations-modalities\n  criterion: Per-neuron correlations of fig3d-firing-correlations-modalities, under each of its\n    readings. Reproduced when r is within tolerance and p < 1e-3 under one reading and r > 0 with\n    p < 0.05 under every reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000576 && python3 - <<'EOF'
import re
p='10.1016-j.neuroimage.2020.116705.yaml'
s=open(p).read()
def rep(m):
    ind=m.group(1); q,v,t=m.group(2),m.group(3),m.group(4)
    return f"{ind}- quantity: {q}\n{ind}  value: {v}\n{ind}  tolerance: {t}"
s=re.sub(r"^(\s*)- \{quantity: (.*?), value: ([-\d.]+), tolerance: ([\d.]+)\}$",rep,s,flags=re.M)
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/000576/10.1016-j.neuroimage.2020.116705.yaml paper/10.1016-j.neuroimage.2020.116705.txt; grep -n -i -E "—|rather" claims/000576/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

That quote runs across a page break with Table 1 in between; I'll split it with "...".

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000576/10.1016-j.neuroimage.2020.116705.yaml",
 "old_string": "    different between the two experimental conditions (Spearman’s r 1⁄4 0.17 �0.28 in AVERSIVE,",
 "new_string": "    different between the two experimental conditions (Spearman’s r 1⁄4 0.17 ... �0.28 in AVERSIVE,"
}
```

```
The file claims/000576/10.1016-j.neuroimage.2020.116705.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000576/10.1016-j.neuroimage.2020.116705.yaml paper/10.1016-j.neuroimage.2020.116705.txt; python3 -c "
import yaml;d=yaml.safe_load(open('claims/000576/10.1016-j.neuroimage.2020.116705.yaml'));c=d['claims']
print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file at `claims/000576/10.1016-j.neuroimage.2020.116705.yaml`, and the quote checker passes with 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (a PDF supplied by a person, read through its extracted text): main text, legends, Tables 1–2 and Methods 4.1–4.11.
- **PDF:** no page renderer is installed here, so I read Table 2 from the text. Minus signs come out garbled there; the signs I used agree with the counts the Results give.
- **Supplement:** not supplied. The text cites it only for Fig. S2 (waveforms and inter-spike intervals per patient), which carries no finding, so I went ahead.
- **Code:** the paper links none. All methods are cited from the Methods, Results and legends.
- **Data descriptor:** I used the Sci Data paper (doi:10.1038/s41597-020-00790-x) only to describe the data layout.

**Counts**
- 23 claims: 22 with quotes and 1 `inferred` (the Table 2 MI values).
- 16 with `statistics` (22 statistical values checked), 16 with `expected`, and all 23 with a criterion.
- 6 claims are `with_inputs` because they need BOLD. The paper names no public deposit for the fMRI time courses (Schacher et al. 2006 cohort).
- The muHGP claims need continuous microwire signals. The data descriptor says only spike times and waveforms were shared.

**Details left open, with the readings named**
- **HGP upper band edge:** only ">60 Hz" is given; the reading is up to the Nyquist frequency.
- **Filter direction and smoothing window shape:** these can't change the outcome, so I used standard choices (zero-phase filter, boxcar window).
- **z-scoring "within each trial":** (a) over the whole 26 s trial, (b) against the baseline, (c) over all of the patient's trials.
- **Amygdalae in the group test:** (a) the 7 nSOZ, as the Results say, or (b) all 14, as the Fig. 1 legend suggests.
- **Cluster threshold and statistic:** (a) cluster mass, or (b) cluster length.
- **Group test:** the Methods say a mixed model; the Results say unpaired t-tests. The mixed model is the main reading and the t-test a variant.
- **MI window:** (a) the group-level clusters applied to every amygdala, or (b) clusters found per amygdala.
- **Tests behind p = 0.009 and p = 0.019 (Fig. 1E):** not named. Readings are rank-sum, t-test, and Fisher or chi-square.
- **Fig. 1F counts:** the source of "5/5 vs 1/5" is not explained; readings are the specificity counts from Table 2, or the counts as printed.
- **Confidence intervals:** the Clopper-Pearson interval is the reading for "the binomial distribution".
- **FDR family for Table 2:** 9 or 18 tests.
- **Time base for firing correlations:** 100 ms bins with 1 s smoothing, 1.5 s with 5-point smoothing, or 15 s smoothing; each computed over the concatenated time course or per trial and averaged.
- **FRV window:** the 24 s blocks or the 26 s trials.
- **Which microwire gives muHGP:** the neuron's own, or the mean over the bundle.
- **Meaning of r in the regressions:** the multiple R, or Spearman of fitted against observed values. "Described by both" is read as both coefficients with p < 0.05.
- **Interval for the 1 Hz unit cutoff:** all trials, or the whole recording.
- **"Gradual and sustained" firing:** the paper gives no measure, so I named two readings.

**Missing from the paper, or inconsistent within it**
- **"Methods 7.8":** cited for the other spectral bands, but no such section exists, so the no-effect claim can't be checked against it.
- **Microwire coverage:**
  - The abstract says 5 participants had microwires.
  - The Results say 9 amygdalae.
  - Table 1 lists 8 amygdalae in 6 patients, three of them in the seizure onset zone.
  - The Limitations section says no microwires were in SOZ amygdalae.
- **Number of blocks:** 8 aversive and 9 neutral in the Methods; 8 of each in the data descriptor.
- **BOLD–HGP count:** the Table 2 legend says 5/5 positive, but the Results and the table's own values give 3/5.
- **Ambiguous figures:**
  - FRV is reported as 0.26 ± 0.15 without saying whether ± is SD or SEM. I used it as the tolerance, since the protocol says to use the stated spread.
  - "MI < 0.05" is set against a printed value of 0.05.

## End of run

23 turns, 5 minutes, result: success.
