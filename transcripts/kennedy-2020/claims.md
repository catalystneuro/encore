# kennedy-2020 · claims · run 42743819919

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/* claims/fouke-2025.yaml
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2728-4.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2728-4.txt",
 "offset": 531,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2728-4.txt",
 "offset": 1030,
 "limit": 430
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The text is complete: the author manuscript (PMC7606611) with Methods and Extended Data legends, plus Supplementary Table 1. Next I'll check the dataset listing and the linked code.

**Agent calls Bash**

```bash
cd  cat papers/datasets/kennedy-2020.yaml 2>/dev/null; grep -rl "001182" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v transcripts | head; ls tools
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41586-020-2728-4
title: Stimulus-specific hypothalamic encoding of a persistent defensive state
datasets:
- archive: dandi
  id: 001182
  relation: primary
./papers/manifest.yaml
./papers/match/001182.yaml
./papers/datasets/kennedy-2020.yaml
./targets/dandisets.json
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/match/001182.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001182' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000])
"
```

```
# Whether each paper DANDI:001182 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: 001182
date: '2026-11-10'
papers:
- doi: 10.1038/s41586-020-2728-4
  relation: IsPartOf
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: partial
  by: agent
  reason: >-
    The dataset holds the microendoscopic calcium imaging experiment (5 mice imaged over three days, GCaMP traces with
    behaviour annotations), so the findings of Figs 2 to 4 and their Extended Data can be tested on it. The paper's
    fiber photometry, optogenetic silencing, rat exposure behaviour, slice and extracellular electrophysiology data
[... 10 more lines not kept]
```

**Agent**

Now the linked code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/DJALab/VMHdm_persistence && cd VMHdm_persistence && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100 && cat README* 2>/dev/null | head -60
```

```
7e5911b28deb10c0327d6b51330534dbafa04469 Mon Nov 15 09:45:43 2021 -0600
./network_models/VMHdm_model_paperversion_sRNN_highG_sandboxing.m
./network_models/makeJBanded.m
./network_models/VMHdm_model_paperversion_peptide.m
./network_models/simStatsAndPlots.m
./network_models/decorrelateWeights.m
./network_models/VMHdm_model_paperversion_sRNN_highG.m
./network_models/VMHdm_model_paperversion_sRNN_highG_longTau.m
./network_models/VMHdm_model_paperversion_sRNN_banded.m
./network_models/VMHdm_model_paperversion_sRNN_lowG.m
./network_models/VMHdm_model_paperversion_RNN_NMDA.m
./README.md
./data_analysis/fiberphotometry/plot_csv_dff4.m
./data_analysis/fiberphotometry/dff_integratorPeakv2.m
./data_analysis/fiberphotometry/plot_csv_control_dff.m
./data_analysis/fiberphotometry/avgCSV.m
./data_analysis/Fig3m_naiveBayes_multiclass.m
./data_analysis/downsampled_MEI_traces.m
./data_analysis/ED7c_representation_separation_spearman.m
# VMHdm_persistence
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHdm_persistence/data_analysis && cat Fig3m_naiveBayes_multiclass.m downsampled_MEI_traces.m ED7c_representation_separation_spearman.m
```

```
stims   = {'rat','male','toy','USS','tone'};
labels  = 1:length(stims);
nstim   = length(stims);
exset   = [1 3 4 5 7];
nTr     = 6;
decodeFromPeak = 0;

clear guess;
for ex = exset
    disp(ex)
    means = [];rMat=[];
    clear resps;
    % for each mouse, compute stim-evoked responses for each trial on each
    % day of imaging
    for s = 1:length(stims)
        count=0;
        for d = 1:3
            day = ['session' num2str(d)];
            for tr = 1:2
                count   = count+1;
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHdm_persistence && wc -l network_models/*.m data_analysis/fiberphotometry/*.m && cat network_models/simStatsAndPlots.m | head -150
```

```
189 network_models/VMHdm_model_paperversion_RNN_NMDA.m
    48 network_models/VMHdm_model_paperversion_peptide.m
   229 network_models/VMHdm_model_paperversion_sRNN_banded.m
   157 network_models/VMHdm_model_paperversion_sRNN_highG.m
   132 network_models/VMHdm_model_paperversion_sRNN_highG_longTau.m
   200 network_models/VMHdm_model_paperversion_sRNN_highG_sandboxing.m
   212 network_models/VMHdm_model_paperversion_sRNN_lowG.m
    44 network_models/decorrelateWeights.m
     7 network_models/makeJBanded.m
    69 network_models/simStatsAndPlots.m
    43 data_analysis/fiberphotometry/avgCSV.m
  2447 data_analysis/fiberphotometry/dff_integratorPeakv2.m
   208 data_analysis/fiberphotometry/plot_csv_control_dff.m
   294 data_analysis/fiberphotometry/plot_csv_dff4.m
  4279 total
function [rMean,rFix,rShuff,PCC,active,overlap,chance,timeDS] = simStatsAndPlots(rIter1,rIter2,time,f,f2,f3,simulated)

dt = time(2)-time(1);
keepCells = find(sum([rIter1(:,sum(time<5):end) rIter2(:,sum(time<5):end)],2)>10);

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHdm_persistence && grep -n "simStatsAndPlots\|f = \|f2 =\|f3 =\|f=@\|f2=@\|f3=@\|corr(" network_models/*.m | head -30; grep -rn "applyMetricToRaster\|computeMetricDiagonal" . | grep -v "simStatsAndPlots.m" | head
```

```
network_models/VMHdm_model_paperversion_RNN_NMDA.m:92:    f = @(x) corr(x);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:93:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_RNN_NMDA.m:94:    f3 = @(x,y) diag(corr(x,y))';
network_models/VMHdm_model_paperversion_RNN_NMDA.m:96:    [rMean,rFix,rShuff,PCC,active,overlap,chance,timeDS] = simStatsAndPlots(rIter1,rIter2,time,f,f2,f3,1);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:97:%     f3 = @(x,y) diag(pdist2(x',y','cosine'))';
network_models/VMHdm_model_paperversion_RNN_NMDA.m:98:%     [~,~,~,cosDist,~,~,~,~] = simStatsAndPlots(rIter1,rIter2,time,f,f2,f3,1);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:138:        Cearly  = [Cearly; corr(sig,tEarly)'];
network_models/VMHdm_model_paperversion_RNN_NMDA.m:139:        Cmid    = [Cmid; corr(sig,tMid)'];
network_models/VMHdm_model_paperversion_RNN_NMDA.m:141:        Cearly_off  = [Cearly_off; corr(sig2,tEarly)'];
network_models/VMHdm_model_paperversion_RNN_NMDA.m:142:        Cmid_off    = [Cmid_off; corr(sig2,tMid)'];
network_models/VMHdm_model_paperversion_RNN_NMDA.m:149:    Cearly_data = corr(data,tEarly);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:150:    Cmid_data   = corr(data,tMid);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:152:    Cearly_off_data = corr(data,tEarly);
network_models/VMHdm_model_paperversion_RNN_NMDA.m:153:    Cmid_off_data = corr(data,tMid);
network_models/VMHdm_model_paperversion_peptide.m:20:    f = @(x) corr(x);
network_models/VMHdm_model_paperversion_peptide.m:21:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_peptide.m:22:    f3 = @(x,y) diag(corr(x,y))';
network_models/VMHdm_model_paperversion_peptide.m:23:    [rMean,rFix,rShuff,PCCtemp,active,overlap,chance,timeDS] = simStatsAndPlots(rIter1,rIter2,time,f,f2,f3,1);
network_models/VMHdm_model_paperversion_sRNN_banded.m:149:        f = @(x) corr(x);
network_models/VMHdm_model_paperversion_sRNN_banded.m:150:        f2 = @(x) zsc
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHdm_persistence && sed -n 110,212p network_models/VMHdm_model_paperversion_sRNN_lowG.m; sed -n 120,189p network_models/VMHdm_model_paperversion_RNN_NMDA.m
```

```
stimTriggeredAutocorr     = cat(3,stimTriggeredAutocorr,rMean);
    manFix      = cat(3,manFix,rFix);
    manShuff    = cat(3,manShuff,rShuff);
    PCCStore    = [PCCStore; PCC];
    activeMean  = [activeMean; active];
    trMean      = [trMean; overlap];
    chanceMean  = [chanceMean; chance];
end

%%

thr         = 0.05;
sig         = smoothts(smoothts(double(rstore{rep,1}),'e',.1/dt),'e',2.5/dt);
response    = max(sig,[],2);
sig         = sig(response > thr,:);
[pks,locs] = max(sig,[],2);
temp = sortrows([locs sig],1);
temp = temp(:,2:end);
temp = bsxfun(@minus,temp,median(temp(:,1:110),2));
temp = bsxfun(@times,temp,1./max(temp,[],2));
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "with_inputs\|with_labels\|elsewhere" docs/*.md | head -20; grep -n "^### 4" -A 30 docs/protocol.md | sed -n 30,80p
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pipeline.md:49:`other_data` (a research paper whose data are elsewhere; `data_in` says where),
docs/pipeline.md:68:aside, are mostly on data elsewhere stops the chain before its checkpoint.
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
docs/protocol.md:161:     recordings of its own, or on other data, are `data: elsewhere` when they
docs/protocol.md:233:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:245:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:267:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:276:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:287:     `data: elsewhere` instead (step 4).
194-Where it is, the reader amends the claim, and the question's `answer` says
195-what changed and why, citing the passage; where it is not, the answer says why
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 230,
 "limit": 60
}
```

```
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference.
233	4. Decide what comes from outside the dataset. Data from elsewhere may be
234	   used only when the claims file says the paper relies on it, it is public,
235	   and it is pinned: a DOI, or a repository at a commit. Record each under
236	   `inputs` in the attempt. A claim whose outside input is not public is
237	   blocked with `data_missing`, and its notes say where you looked.
238	
239	   The registry judges the dataset, so claims that use outside data are
240	   kept apart:
241	   - Each claim says what its test uses: `data: dataset` (the default),
242	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243	     `with_inputs` and `elsewhere` claims are counted apart, each group on
244	     its own; the others count towards what is said about the dataset.
245	   - `with_labels` is for outside sources that only name or map codes the
246	     dataset already holds, such as stimulus names for its stimulus codes.
247	     They bring in no measurements. A link claim must confirm the names, and
248	     the missing names are recorded as a finding (`metadata_insufficient`).
249	   - When outside data has to be matched to the dataset's cells, sessions
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHdm_persistence && grep -rni "score\|similar\|load(" network_models | head; sed -n 1,60p network_models/VMHdm_model_paperversion_sRNN_lowG.m
```

```
network_models/VMHdm_model_paperversion_sRNN_highG_sandboxing.m:104:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_peptide.m:21:    f2 = @(x) zscore(x')';
network_models/simStatsAndPlots.m:29:% compute between-stim similarity measure
network_models/VMHdm_model_paperversion_sRNN_highG.m:105:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_sRNN_highG_longTau.m:94:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_sRNN_banded.m:150:        f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_sRNN_lowG.m:103:    f2 = @(x) zscore(x')';
network_models/VMHdm_model_paperversion_RNN_NMDA.m:93:    f2 = @(x) zscore(x')';

N = 1000; sp = 0.1; thr = 0.1; [w1,w2] = deal(zeros(N,1));

% reset everything to be safe
rng(42);
[doOnline,plotTrial,doOverlap,doStructured,doBanded,doDecorr] = deal(false);

dt      = 0.005;
tau     = 0.1; %membrane potential
time    = dt:dt:120;
tOn     = 2.5;
tOff    = 4.5;
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p tools/claims_check.py | grep -n "def \|key\|allowed\|statistic\|'ci'\|expected\|tolerance\|range" | head -60
```

```
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
92:        for s in c.get("statistics", []):
101:          f"{values} statistical values, {problems} problems")
105:def main() -> int:
```

**Agent calls Bash**

```bash
cd  sed -n 1,120p tools/claims_check.py; grep -l "ci:" claims/*.yaml | head -3; grep -h -A3 " ci:" claims/*.yaml | head -12; grep -h "statistic:" claims/*.yaml | head -5
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

[... 113 more lines not kept]
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
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['properties'].get('checks',{}),indent=1)[:800])"
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
[... 123 more lines not kept]
```

**Agent**

I've read the paper and the linked code (DJALab/VMHdm_persistence at 7e5911b). The dataset holds only the microendoscopic imaging (Figs 2 to 4, ED 7 to 10). Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/kennedy-2020.yaml",
 "content": "# Claims for Kennedy, Kunwar, Li et al. (2020), Nature 586, 730-734, on DANDI:001182.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (version pilot-14). No data of the dataset were seen.\n#\n# Text read: the accepted author manuscript in Europe PMC (PMC7606611, NIHMS1606924), full text,\n# with its Methods, figure legends and Extended Data legends 1 to 10, and Supplementary Table 1\n# (41586_2020_2728_MOESM1_ESM.pdf, the table of statistical tests). The version of record was not\n# read. No main-text PDF was supplied, so no figure was looked at; claims rest on the text, the\n# legends and Supplementary Table 1.\n#\n# Code read: https://github.com/DJALab/VMHdm_persistence at commit 7e5911b28deb10c0327d6b51330534dbafa04469\n# (2021-11-15). It holds MATLAB scripts for the fiber photometry (data_analysis/fiberphotometry), the\n# Fig 3m decoder (Fig3m_naiveBayes_multiclass.m), the population decay fits of Fig 2d and 3b\n# (downsampled_MEI_traces.m), the cross-day correlation of ED Fig 7c\n# (ED7c_representation_separation_spearman.m), and the six network models of Fig 4\n# (network_models). It does not hold the cell extraction, the responsive-cell selection, the peak and\n# half-peak times, the preference index, the PCA, the time-resolved decoders, the autocorrelation of\n# the imaging data, or the two data similarity scores; computeMetricDiagonal and applyMetricToRaster,\n# which the model scripts call, are missing. The scripts read a MATLAB struct `expt` (mice indexed\n# 1, 3, 4, 5 and 7; days session1 to session3; stimuli named rat, male, toy, USS and tone) that is not\n# in the repository.\n#\n# Data the paper describes. Male SF1-Cre mice, 8 to 20 weeks. The dataset (DANDI:001182, GCaMP traces\n# with behaviour annotation, sessions such as sub-M5-session3) is meant to hold the microendoscopic\n# imaging experiment only: 5 mice expressing GCaMP6s in VMHdm/c SF1 neurons, imaged through a GRIN\n# lens with an nVista microscope at 11 Hz (one mouse at 20 Hz), head-fixed on a running wheel, on three\n# consecutive days. Each day each of five stimuli was presented twice for 10 s in pseudorandom order\n# with at least five minutes (ED Fig 7 says ten minutes) between presentations: an awake rat in a wire\n# mesh cage, a male BALB mouse in the cage, a toy rat in the cage, an ultrasonic sweep (USS, 100 ms\n# sweeps of 17 to 20 kHz at 85 dB) and a 2 kHz tone. Traces come from CNMF-E after manual screening;\n# 187.3 cells were imaged per day and cells were registered across the three days (roughly half).\n# Responses are in units of the standard deviation of a 30 s pre-stimulus baseline (Methods, Units of\n# neuronal activation). The fiber photometry (Fig 1, ED 1 and 3), the open field and home cage\n# behaviour with optogenetic silencing or activation (Fig 1i to n, ED 2 and 3), the tetanus toxin\n# photometry (Fig 1o to r), the slice electrophysiology and imaging (ED 4) and the silicon probe\n# recordings (ED 6) are not described as part of the dataset; the paper says its data are available\n# from the corresponding author on request. Their claims are kept, as data the paper recorded.\n#\n# Numbering in the Methods differs from the legends. The Methods place the decoder bar plot in\n# \"Fig 3n\" and its confusion matrix in \"ED 7a\"; the legends place them in Fig 3m and ED Fig 9a. The\n# time-resolved decoders are \"Fig 3o, ED 8b-c\" in the Methods and ED Fig 9b-c in the legends. The\n# preference index is cited for \"Fig 2g and Fig 3i, k\"; the histograms are Fig 2i, 3h and 3j. The\n# legends are followed here.\n#\n# Methods fixed from the paper for the imaging claims (cited in each criterion). Responsive cell\n# (Methods, Identifying stimulus-responsive cells): baseline the 10 s before stimulus onset; a cell\n# responds when the mean of any 1 s window in the first 30 s after onset exceeds the baseline mean by\n# more than four baseline standard deviations, on both trials of that day. Peak time: the first time\n# the trace passes 95% of its maximum; half-peak time: the last time it is above 50% of its maximum\n# relative to the pre-stimulus baseline; per cell and day, averaged over the two trials. Preference:\n# |sa - sb| / (|sa| + |sb|) on the mean response over 45 s from onset, averaged over two trials,\n# per cell and day, for cells responsive to either stimulus.\n#\n# Details left open by the paper and its code, named in the criteria with their readings: whether the\n# 1 s windows of the responsive-cell rule slide or are contiguous bins, and whether the baseline\n# standard deviation is that of frames or of 1 s means; how the 20 Hz mouse is put on the 11 Hz time\n# base; whether cell counts pool cell-days or count tracked cells; the inhibition criterion; the\n# window searched for peaks; the sign convention of the preference histograms; the decoder's response\n# window (code against Methods); which five of six trials the PCA plots; the cells used for the\n# autocorrelation; the frame range of the specificity score; what \"satisfied both conditions\" means\n# for the model scores; and the model parameters where the code and the Methods disagree.\nschema_version: 2\npaper: doi:10.1038/s41586-020-2728-4\nclaims:\n- id: fig1de-rat-persistent\n  statement: In freely moving mice, fiber photometry shows VMHdm SF1 activity rising at the onset of a\n    10 s presentation of an anesthetized rat and persisting for over a minute after its removal, with\n    a decay time constant of 26.7 +/- 2.2 s.\n  source: Main text, paragraph 1; Figure 1d and 1e; Extended Data Fig 1d\n  quote: Remarkably, this activity persisted for over a minute following rat removal (time constant\n    τ decay = 26.7±2.2 seconds\n  expected:\n  - quantity: decay time constant of the rat-evoked photometry response, home cage\n    value: 26.7\n    tolerance: 2.2\n    unit: s\n  criterion: Tolerance is the paper's stated spread (mean +/- SEM, the convention of the legends).\n    The fit is the Methods' difference of exponentials K(t) = A (tau_decay - tau_rise)^-1\n    (exp(-t/tau_rise) - exp(-t/tau_decay)), fit per trial to minimise the mean squared error over the\n    30 s from stimulus onset (Methods, Fitting decay constants). Reproduced when the mean over the 4\n    mice is within tolerance. Fiber photometry, not described as part of the dataset.\n- id: fig1de-toy-weaker\n  statement: A toy rat evokes a weaker and shorter photometry response than the rat in freely moving\n    mice.\n  source: Main text, paragraph 1; Figure 1d and 1e; Supplementary Table 1, Fig 1e\n  quote: In contrast, a toy rat evoked a weaker and shorter response\n  statistics:\n  - about: peak response, rat against toy, home cage\n    test: paired t-test\n    statistic: t = 5.456, DF 7\n    p: 0.0010\n    ci:\n      low: -26.96\n      high: -10.65\n    n: 4 mice\n- id: fig1fgh-headfixed-rat-strongest\n  statement: In head-fixed mice the photometry peak response depends on the caged stimulus, rat above\n    mouse above toy rat, and the rat response decays more slowly than the mouse response.\n  source: Main text, paragraph 1; Figure 1f to 1h; Supplementary Table 1, Fig 1g and 1h\n  quote: VMHdm SF1 peak responses varied by stimuli, with rat responses being strongest and\n    longest-lasting\n  statistics:\n  - about: peak, rat against mouse, head-fixed\n    test: paired t-test\n    statistic: t = 4.344, DF 14\n    p: 0.0007\n    ci:\n      low: -20.15\n      high: -6.829\n    n: 8 mice in Supplementary Table 1 (the Fig 1g legend gives n = 6)\n  - about: peak, rat against toy, head-fixed\n    test: paired t-test\n    statistic: t = 5.443, DF 14\n    p: 0.0001\n    ci:\n      low: -27.16\n      high: -12.11\n    n: 8 mice in Supplementary Table 1\n  - about: peak, mouse against toy, head-fixed\n    test: paired t-test\n    statistic: t = 4.157, DF 15\n    p: 0.0008\n    ci:\n      low: -10.32\n      high: -3.325\n    n: 8 mice in Supplementary Table 1\n  - about: decay constant, rat against mouse, head-fixed\n    test: paired t-test\n    statistic: t = 2.903, DF 13\n    p: 0.0123\n    ci:\n      low: -22.05\n      high: -3.234\n    n: 8 mice in Supplementary Table 1 (the Fig 1h legend gives n = 6)\n- id: ed1-urine-looming\n  statement: VMHdm SF1 neurons respond moderately to rat urine (more than to water, with a shorter\n    decay than to the rat) and weakly to an overhead looming disk.\n  source: Main text, paragraph 1; Extended Data Fig 1f to 1k; Supplementary Table 1, ED 1\n  quote: VMHdm SF1 neurons responded moderately to rat urine, and weakly to an overhead looming disk\n  statistics:\n  - about: peak, rat urine against water\n    test: paired t-test\n    statistic: t = 10.08, DF 11\n    p: 0.0001\n    ci:\n      low: -14.37\n      high: -9.219\n    n: 6 mice, 2 trials per mouse\n  - about: decay constant, rat against rat urine\n    test: t-test\n    statistic: t = 2.39, DF 24\n    p: 0.0250\n    ci:\n      low: -17.94\n      high: -1.315\n    n: 8 mice (rat), 6 mice (urine)\n  - about: peak, rat against toy, home cage\n    test: paired t-test\n    statistic: t = 3.469, DF 3\n    p: 0.0400\n    ci:\n      low: 1.729\n      high: 40.09\n    n: 4 mice, 1 trial per mouse\n  - about: peak, rat against looming disk, home cage\n    test: paired t-test\n    statistic: t = 4.037, DF 3\n    p: 0.0273\n    ci:\n      low: -38.29\n      high: -4.534\n    n: 4 mice, 1 trial per mouse\n- id: fig1km-thigmotaxis\n  statement: After a 15 s exposure to a caged rat in an open field, control mice spend more time in\n    the edge zone (thigmotaxis), and the increase lasts minutes.\n  source: Main text, paragraph 2; Figure 1k to 1m (blue); Extended Data Fig 3a; Supplementary Table 1,\n    Fig 1m and ED 3a\n  quote: Following rat exposure, mice exhibited thigmotaxis, an index of increased anxiety ... lasting\n    minutes\n  statistics:\n  - about: edge-zone time, control, before rat (-1 to 0 min) against after rat (0 to 1 min after removal)\n    test: paired t-test\n    statistic: t = 4.417, DF 11\n    p: 0.0006\n    ci:\n      low: 0.1657\n      high: 0.4948\n    n: 12 control mice\n  - about: edge-zone time, control, before rat against after PS off (3 to 4 min after removal)\n    test: paired t-test\n    statistic: t = 2.812, DF 11\n    p: 0.0074\n    ci:\n      low: 0.05562\n      high: 0.4562\n    n: 12 control mice\n  - about: distance to arena centre, control, before against after rat (ED Fig 3a); printed 1.80E-05\n    test: paired t-test\n    statistic: t = 5.559, DF 11\n    p: 1.8e-05\n    ci:\n      low: 4.675\n      high: 10.8\n    n: 12 control mice\n  criterion: Windows from the Methods (Open field rat exposure assay); edge zone within 4 cm of the\n    walls, time in 30 s chunks. Behaviour, not described as part of the dataset.\n- id: ed2abc-no-lingering-odor\n  statement: Mice introduced into the arena right after the rat was presented there do not show\n    thigmotaxis, so lingering rat odours do not cause it.\n  source: Main text, paragraph 2; Extended Data Fig 2a to 2c\n  quote: Thigmotaxis was not observed if the mouse was introduced after rat presentation, arguing that\n    lingering rat-derived odors are not causative\n  criterion: A claim of absence, for which neither the text nor Supplementary Table 1 names a test.\n    The paper's comparisons of two independent groups use a two-sided t-test (Supplementary Table 1),\n    so the claim is reproduced when that test at p < 0.05 finds no difference between the rat and toy\n    groups (n = 6 each) in fraction of time in the centre zone or distance to centre, and not\n    reproduced when it does; the effect size is given either way. Behaviour, not described as part\n    of the dataset.\n- id: ed2e-chr2-thigmotaxis\n  statement: A 10 s optogenetic activation of VMHdm SF1 neurons evokes persistent thigmotaxis in the\n    open field.\n  source: Main text, paragraph 2; Extended Data Fig 2d and 2e; Supplementary Table 1, ED 2e\n  quote: persistent thigmotaxis could be evoked following optogenetic stimulation of VMHdm SF1 neurons\n  statistics:\n  - about: edge-zone time, 473 nm against mock stimulation\n    test: repeated measures ANOVA\n    statistic: F = 17.15, DFn 1, DFd 14\n    p: 0.0012\n    ci:\n      low: -59.08\n      high: -18.57\n    n: 4 mice, 2 trials per condition\n- id: ed3c-openfield-photometry\n  statement: Fiber photometry shows VMHdm SF1 neurons persistently activated after rat presentation in\n    the open field arena.\n  source: Main text, paragraph 2; Extended Data Fig 3c\n  quote: Fiber photometry confirmed that VMHdm SF1 neurons were persistently activated following rat\n    presentation\n  criterion: Reproduced when the mean trace over the 9 mice stays above its pre-stimulus baseline\n    after the 15 s presentation and the decay constant fitted as in the Methods (Fitting decay\n    constants) exceeds the 15 s presentation; the paper gives no number, so this threshold is set\n    here. Fiber photometry, not described as part of the dataset.\n- id: ed3de-openfield-vs-headfixed\n  statement: Peak and decay constant of the rat-evoked photometry response do not differ between the\n    open field and the head-fixed preparation.\n  source: Extended Data Fig 3d and 3e; Supplementary Table 1, ED 3d and 3e\n  inferred: No sentence states the comparison; read from the ED Fig 3d and 3e legends and the\n    non-significant tests in Supplementary Table 1.\n  statistics:\n  - about: peak, open field against head-fixed\n    test: t-test\n    statistic: t = 0.5964, DF 23\n    p: 0.4681\n    ci:\n      low: -15.82\n      high: 28.64\n    n: 9 mice open field, 8 mice head-fixed\n  - about: decay constant, open field against head-fixed\n    test: t-test\n    statistic: t = 0.9276, DF 23\n    p: 0.3633\n    ci:\n      low: -31.18\n      high: 11.87\n    n: 9 mice open field, 8 mice head-fixed\n  criterion: A claim of absence, judged on the paper's two-sided t-test at p < 0.05.\n- id: ed3fi-kinetics-track-thigmotaxis\n  statement: The decay of VMHdm SF1 activity after rat removal follows the time course of thigmotaxis;\n    within mice activity and distance to centre are correlated, and their times to 50% of peak do not\n    differ.\n  source: Main text, paragraph 2; Extended Data Fig 3f to 3i; Supplementary Table 1, ED 3g\n  quote: with kinetics correlated with thigmotaxis\n  statistics:\n  - about: example mouse 1, dF/F against distance to centre\n    test: linear regression\n    statistic: r = 0.958\n    p: 0.0001\n    p_relation: \"<\"\n  - about: example mouse 2, dF/F against distance to centre\n    test: linear regression\n    statistic: r = 0.808\n    p: 0.0001\n    p_relation: \"<\"\n  - about: time to 50% of peak, distance against dF/F\n    test: paired t-test\n    statistic: t = 0.7985, DF 8\n    p: 0.4476\n    ci:\n      low: -29.79\n      high: 14.46\n    n: 9 mice\n  criterion: Distance to centre as a 30 s moving average (ED Fig 3f legend); decay time as the time\n    to 50% of peak for linearly fitted data (ED Fig 3g legend). The paper does not say whether the\n    correlation is with the distance or its negative; the sign is reported. Photometry and behaviour,\n    not described as part of the dataset.\n- id: fig1j-silencing-reduces-avoidance\n  statement: iC++ silencing of VMHdm SF1 neurons reduces avoidance of a rat in the home cage, raising\n    time spent in the zone near the rat.\n  source: Main text, paragraph 3; Figure 1i and 1j; Supplementary Table 1, Fig 1j\n  quote: First, we confirmed that iC++ -mediated silencing decreased avoidance of a rat in the home cage\n  statistics:\n  - about: percent time in zone 1, control against iC++\n    test: paired t-test\n    statistic: t = 2.703, DF 12\n    p: 0.0192\n    ci:\n      low: 3.599\n      high: 33.50\n    n: 7 iC++ mice and 7 control littermates\n- id: fig1lmn-silencing-before\n  statement: Silencing VMHdm SF1 neurons for three minutes from five seconds before rat exposure\n    prevents the increase in thigmotaxis and in anxiety behaviours.\n  source: Main text, paragraph 3; Figure 1l to 1n (red); Extended Data Fig 3a; Supplementary Table 1\n  quote: Silencing initiated prior to rat exposure prevented the increase in thigmotaxis\n  statistics:\n  - about: edge-zone time course, PS during and after rat against control (Fig 1l)\n    test: repeated measures ANOVA, group against time\n    statistic: F = 9.227, DFn 1, DFd 16\n    p: 0.0078\n    ci:\n      low: 0.06152\n      high: 0.3457\n    n: 12 control mice, 6 mice during+after\n  - about: edge-zone time after rat, control against PS during and after (Fig 1m)\n    test: t-test\n    statistic: t = 3.307, DF 16\n    p: 0.0023\n    ci:\n      low: -0.4967\n      high: -0.1083\n    n: 12 control mice, 6 mice during+after\n  - about: edge-zone time after PS off, control against PS during and after (Fig 1m)\n    test: t-test\n    statistic: t = 2.452, DF 16\n    p: 0.0223\n    ci:\n      low: -0.5823\n      high: -0.4226\n    n: 12 control mice, 6 mice during+after\n  - about: anxiety behaviours, control against PS during and after (Fig 1n)\n    test: repeated measures ANOVA\n    statistic: F = 20.62, DFn 1, DFd 16\n    p: 0.0003\n    ci:\n      low: -0.3065\n      high: -0.1147\n    n: 12 control mice, 6 mice during+after\n  - about: distance to centre after rat, control against PS during and after (ED Fig 3a); printed 5.20E-05\n    test: t-test\n    statistic: t = 5.028, DF 16\n    p: 5.2e-05\n    ci:\n      low: -10.53\n      high: -4.285\n    n: 12 control mice, 6 mice during+after\n  - about: distance to centre after PS off, control against PS during and after (ED Fig 3a)\n    test: t-test\n    statistic: t = 2.5, DF 16\n    p: 0.0240\n    ci:\n      low: -9.611\n      high: -0.7788\n    n: 12 control mice, 6 mice during+after\n- id: fig1lmn-silencing-after\n  statement: Silencing begun right after rat removal leaves an initial increase in thigmotaxis, which\n    returns to baseline faster than in controls.\n  source: Main text, paragraph 3; Figure 1l to 1n (green); Extended Data Fig 3a; Supplementary Table 1\n  quote: When silencing was initiated after rat removal, mice exhibited an initial increase in\n    thigmotaxis, but it returned to baseline faster than in controls\n  statistics:\n  - about: edge-zone time course, PS after rat only against control (Fig 1l)\n    test: repeated measures ANOVA, group against time\n    statistic: F = 6.74, DFn 1, DFd 16\n    p: 0.0321\n    ci:\n      low: 0.04131\n      high: 0.3997\n    n: 12 control mice, 6 mice after-only\n  - about: edge-zone time after PS off, control against PS after only (Fig 1m)\n    test: t-test\n    statistic: t = 3.123, DF 16\n    p: 0.0062\n    ci:\n      low: -0.6622\n      high: -0.1267\n    n: 12 control mice, 6 mice after-only\n  - about: anxiety behaviours, control against PS after only (Fig 1n)\n    test: repeated measures ANOVA\n    statistic: F = 10.94, DFn 1, DFd 16\n    p: 0.0044\n    ci:\n      low: -0.3797\n      high: -0.2018\n    n: 12 control mice, 6 mice after-only\n  - about: distance to centre after rat, control against PS after only (ED Fig 3a)\n    test: t-test\n    statistic: t = 2.731, DF 16\n    p: 0.0250\n    ci:\n      low: -8.007\n      high: -1.009\n    n: 12 control mice, 6 mice after-only\n  - about: distance to centre after PS off, control against PS after only (ED Fig 3a)\n    test: t-test\n    statistic: t = 2.369, DF 16\n    p: 0.0460\n    ci:\n      low: -11.66\n      high: -0.6467\n    n: 12 control mice, 6 mice after-only\n  criterion: The initial increase has no test of its own in Supplementary Table 1; it is shown in the\n    Fig 1l time course. Behaviour, not described as part of the dataset.\n- id: ed3b-velocity-unchanged\n  statement: Photostimulation does not change mean velocity in iC++ or control mice.\n  source: Extended Data Fig 3b; Supplementary Table 1, ED 3b\n  quote: Mean velocity was not altered by photostimulation of iC++ and control\n  statistics:\n  - about: iC++, light off against light on\n    test: paired t-test\n    statistic: t = 1.005, DF 6\n    p: 0.7059\n    ci:\n      low: -0.5391\n      high: 1.291\n    n: 7 mice\n  - about: control, light off against light on\n    test: paired t-test\n    statistic: t = 0.3959, DF 6\n    p: 0.3537\n    ci:\n      low: -0.991\n      high: 1.385\n    n: 7 mice\n  criterion: A claim of absence, judged on the paper's paired t-test at p < 0.05 for each group;\n    velocity averaged over three minutes in the home cage (ED Fig 3b legend).\n- id: ed3j-eyfp-control\n  statement: Against an EYFP-injected SF1-Cre control, iC++ silencing during and after the rat still\n    reduces edge-zone time.\n  source: Extended Data Fig 3j; Supplementary Table 1, ED 3j\n  quote: Additional control for optogenetic loss-of-function experiment\n  statistics:\n  - about: EYFP against iC++\n    test: repeated measures ANOVA\n    statistic: F = 5.525, DFn 1, DFd 9\n    p: 0.0433\n    ci:\n      low: 0.7323\n      high: 38.18\n    n: 5 EYFP mice, 6 iC++ mice\n- id: fig1r-tettox-faster-decay\n  statement: Blocking neurotransmitter release from VMHdm SF1 neurons with tetanus toxin light chain\n    makes the rat-evoked bulk calcium response decay faster.\n  source: Main text, paragraph 4; Figure 1o, 1p and 1r; Supplementary Table 1, Fig 1r\n  quote: TetTox-GFP mice showed significantly faster bulk calcium decay kinetics than control\n    (jRGECO1a/EYFP-injected) mice, following rat exposure\n  statistics:\n  - about: decay time from peak to 50% peak, control against TetTox\n    test: t-test\n    statistic: t = 4.808, DF 18\n    p: 0.0004\n    ci:\n      low: 5.996\n      high: 15.83\n    n: 5 mice per group\n- id: fig1q-tettox-peak-unchanged\n  statement: The peak rat-evoked response is not affected by tetanus toxin light chain.\n  source: Main text, paragraph 4; Figure 1q; Supplementary Table 1, Fig 1q\n  quote: while the peak response was not affected\n  statistics:\n  - about: peak, control against TetTox\n    test: t-test\n    statistic: t = 0.2694, DF 18\n    p: 0.7907\n    ci:\n      low: -4.363\n      high: 3.371\n    n: 5 mice per group\n  criterion: A claim of absence, judged on the paper's two-sided t-test at p < 0.05.\n- id: ed4d-glutamatergic-connectivity\n  statement: Photostimulating a minority of VMHdm SF1 neurons evokes excitatory postsynaptic currents\n    in most recorded SF1 neurons (6 of 7), abolished by glutamate receptor blockade.\n  source: Main text, paragraph 4; Extended Data Fig 4a to 4d; Supplementary Table 1, ED 4d\n  quote: Ex vivo physiology indicated mono- and di-synaptic glutamatergic excitatory connectivity\n    among VMHdm SF1 neurons\n  statistics:\n  - about: evoked EPSC, control against glutamate receptor blockade\n    test: two-tailed paired t-test\n    statistic: t = 4.501, DF 6\n    p: 0.0041\n    ci:\n      low: 8.619\n      high: 29.15\n    n: 7 cells from 5 mice\n  expected:\n  - quantity: connected cells\n    value: 6\n    tolerance: 0\n    unit: of 7 cells\n  - quantity: median evoked EPSC, control\n    value: -20.10\n    tolerance: 2.01\n    unit: pA\n- id: ed4g-follower-cells\n  statement: Electrically stimulating a single VMHdm SF1 neuron in a slice activates several follower\n    cells, a median of 4 per slice.\n  source: Main text, paragraph 4; Extended Data Fig 4e to 4g\n  quote: while electrical stimulation of single VMHdm SF1 neurons activated multiple follower cells\n  expected:\n    quantity: median follower cells per slice (cross-correlation above 0.6)\n    value: 4\n    tolerance: 0.4\n    unit: cells\n- id: ed6-ephys-heterogeneous\n  statement: Silicon probe recordings in VMHdm confirm the heterogeneous rat-evoked dynamics, with\n    peaks and half-peak decays spread over tens of seconds among 370 rat-responsive units; 90% of\n    units fire spontaneously at 13 Hz or less.\n  source: Main text, paragraph 5; Extended Data Fig 6\n  quote: These heterogeneous dynamics were confirmed by in vivo electrophysiological recordings from\n    VMHdm neurons\n  expected:\n  - quantity: rat-responsive units\n    value: 370\n    tolerance: 37\n    unit: units from 5 mice\n  - quantity: spontaneous rate below which 90% of units fall\n    value: 13\n    tolerance: 1.3\n    unit: Hz\n  criterion: Responsive units as the Methods define them (any 1 s window in the first 30 s after\n    onset above the 10 s baseline mean by more than three standard deviations); firing rates in 1 s\n    bins (ED Fig 6d legend). Silicon probe data, not described as part of the dataset.\n- id: imaging-cell-counts\n  statement: Microendoscopic imaging of 5 mice yields 187.3 +/- 8.1 cells per day, and 78 cells are\n    tracked across the three days.\n  source: Main text, paragraph 5; Methods, Microendoscopic imaging data acquisition and processing\n  quote: n=5 mice, 187.3±8.1 cells imaged per day, 78 cells tracked across days\n  expected:\n  - quantity: cells imaged per day\n    value: 187.3\n    tolerance: 8.1\n    unit: cells per mouse per day\n  - quantity: cells tracked across days\n    value: 78\n    tolerance: 7.8\n    unit: cells\n  criterion: Tolerance on the cells per day is the paper's stated spread; 10% for the tracked cells.\n    The cells are those of the dataset's traces (CNMF-E after manual screening). The paper allows\n    two readings of 78, (a) the mean per mouse of cells registered on all three days, which fits\n    \"roughly half of all cells could be registered\" (Methods), and (b) the total over the five mice.\n    Reproduced when the cells per day and one reading of the tracked count are within tolerance.\n- id: fig2cd-population-persistent\n  statement: The VMHdm SF1 population response measured by imaging persists after rat presentation,\n    and its fitted decay constant differs between rat and mouse.\n  source: Main text, paragraph 5; Figure 2c and 2d; Supplementary Table 1, Fig 2d\n  quote: Although downsampled VMHdm SF1 population responses persisted following rat presentation\n  statistics:\n  - about: fitted decay constant, rat against mouse\n    test: paired t-test\n    statistic: t = 3.3452, DF 4\n    p: 0.0287\n    ci:\n      low: 3.136\n      high: 33.757\n    n: 5 mice\n  expected:\n    quantity: difference in decay constant, rat against mouse (midpoint of the paper's interval)\n    value: 18.45\n    tolerance: 15.31\n    unit: s\n  criterion: The tolerance is half the width of the paper's confidence interval, so the claim holds\n    when the mean difference lies in 3.136 to 33.757 s. Per mouse, the population response is the\n    mean over all cells (downsampled_MEI_traces.m, which averages the cells of each trial; the paper\n    does not otherwise say what \"downsampled\" means), on day 1, with the mean before -1 s subtracted.\n    The fit is the Methods' difference of exponentials, over the 30 s from onset (Methods, Fitting\n    decay constants). Trials are open, (a) the first day-1 trial only, as the code does, (b) the mean\n    of the two day-1 trials, (c) each trial fitted and the two constants averaged, as the Methods'\n    \"fit for each trial\" says. The code's fit window of -200 to 550 frames (-18 to 50 s) with a\n    time-offset parameter is a variant. Reproduced when, under one reading, a two-sided paired\n    t-test of the rat and mouse constants over the 5 mice gives p < 0.05 and the mean difference is\n    within tolerance. The text does not state which is longer; the direction is reported.\n- id: fig3ab-uss-persistent\n  statement: The ultrasonic sweep strongly and persistently activates VMHdm SF1 neurons, more than a\n    2 kHz tone.\n  source: Main text, paragraph 6; Figure 3a and 3b\n  quote: The USS strongly and persistently activated VMHdm SF1 neurons\n  criterion: The paper gives no number or test. Population response and fit as in\n    fig2cd-population-persistent, under the same trial readings. Reproduced when the mean over the 5\n    mice of the USS population peak exceeds that of the tone and the fitted USS decay constant\n    exceeds the 10 s stimulus; these thresholds are set here. The USS and rat constants are reported\n    side by side, as Fig 3b shows them.\n- id: fig2jo-diverse-peak-times\n  statement: Individual neurons show diverse but reproducible dynamics; many responsive cells peak at\n    stimulus onset while others reach their peak only after stimulus removal (202 rat-responsive,\n    160 mouse-responsive and 133 USS-responsive cells).\n  source: Main text, paragraph 5; Figure 2e to 2g and 2j to 2o; Figure 3c to 3f\n  quote: While many cells were activated at stimulus onset, others reached their peak only after\n    stimulus removal\n  expected:\n  - quantity: rat-responsive cells\n    value: 202\n    tolerance: 20.2\n    unit: cells from 5 mice across 3 days\n  - quantity: mouse-responsive cells\n    value: 160\n    tolerance: 16\n    unit: cells from 5 mice across 3 days\n  - quantity: USS-responsive cells\n    value: 133\n    tolerance: 13.3\n    unit: cells from 5 mice across 3 days\n  criterion: Responsive cells, peak and half-peak times as the Methods define them (see the opening\n    comment). Open details, each run, (i) the counts as cell-days summed over mice and days, or as\n    distinct tracked cells responsive on at least one day; (ii) the 1 s windows of the responsive\n    rule as sliding windows or contiguous 1 s bins; (iii) the baseline standard deviation of the\n    frames or of the 1 s means; (iv) the peak searched within 0 to 30 s or 0 to 45 s after onset.\n    The 20 Hz mouse is put on the 11 Hz time base by averaging in time, a standard choice. Counts\n    match when within tolerance under one reading. The paper gives no fraction for \"many\" and\n    \"others\"; reproduced when, for the rat, cells peaking within the 10 s presentation and cells\n    peaking after it each make up at least 10% of rat-responsive cells (threshold set here), under\n    the reading that matches the counts or, if none does, under all readings; the same is reported\n    for mouse and USS.\n- id: fig2hi-rat-mouse-overlap\n  statement: Rat and mouse responses are partially overlapping but distinct; among 219 cells\n    responsive to either, some respond to both and others exclusively to one.\n  source: Main text, paragraph 5; Figure 2h and 2i\n  quote: Interestingly, rat and mouse responses were partially overlapping but distinct\n  expected:\n    quantity: cells responsive to rat or mouse\n    value: 219\n    tolerance: 21.9\n    unit: cells from 5 mice across 3 days\n  criterion: Responsive cells as in fig2jo-diverse-peak-times, under the same readings. The Methods'\n    preference |sa - sb| / (|sa| + |sb|) runs from 0 to 1, while the Fig 2i histogram runs from -1\n    to +1; the histogram is drawn with the signed form (sa - sb) / (|sa| + |sb|), sa the rat, on the\n    mean over 45 s from onset averaged over the two trials (Methods, Strength of cell preference).\n    The paper gives no threshold; reproduced when cells responsive to both stimuli and cells\n    responsive to only one each make up at least 10% of the 219 (threshold set here).\n- id: fig3gj-uss-intermingled\n  statement: USS-responsive neurons are spatially intermingled with rat-responsive cells, and some\n    cells respond to both (216 cells responsive to rat or USS, 219 to mouse or USS).\n  source: Main text, paragraph 6; Figure 3g to 3j\n  quote: USS-responsive neurons were spatially intermingled with rat-responsive cells, with some\n    responding to both stimuli\n  expected:\n  - quantity: cells responsive to rat or USS\n    value: 216\n    tolerance: 21.6\n    unit: cells from 5 mice\n  - quantity: cells responsive to mouse or USS\n    value: 219\n    tolerance: 21.9\n    unit: cells from 5 mice\n  criterion: Responsive cells and preference as in fig2hi-rat-mouse-overlap. Reproduced when some\n    cells respond to both rat and USS and the spatial footprints of rat-only and USS-only cells are\n    not segregated; the paper gives no test of mixing, so segregation is judged by whether, in each\n    mouse, the mean distance between rat-only and USS-only centroids is no larger than the mean\n    distance within each group (set here). If the dataset holds no footprints, only the overlap is\n    tested.\n- id: fig3k-few-stimuli-per-cell\n  statement: 74.4% of neurons respond significantly to at least one of the five stimuli; of these\n    43.6% respond to only one, and over 70% respond to two or fewer.\n  source: Main text, paragraph 6; Figure 3k\n  quote: Among neurons responding significantly to at least one stimulus (74.4%), 43.6% responded to\n    only one, and over 70% responded to ≤ 2 of the five tested stimuli\n  expected:\n  - quantity: cells responding to at least one stimulus\n    value: 74.4\n    tolerance: 7.44\n    unit: percent\n  - quantity: of these, responding to only one\n    value: 43.6\n    tolerance: 4.36\n    unit: percent\n  - quantity: responding to two or fewer (a lower bound, holds above 63%)\n    value: 70\n    tolerance: 7\n    unit: percent\n  criterion: Responsive cells as in fig2jo-diverse-peak-times, under the same readings. Further\n    readings, (a) \"responding\" means excited only (the Methods' criterion) or excited or inhibited\n    (Fig 3d and 3l show inhibited cells; inhibition as in fig3l-mostly-excited); (b) the denominator\n    of \"over 70%\" is the responsive cells, or all cells, as the Fig 3k histogram (zero to five) is\n    of all cells; (c) cells pooled over mice and days, or the mean over mice. Reproduced when all\n    three numbers match under one reading.\n- id: fig3l-mostly-excited\n  statement: Most stimulus-responsive VMHdm SF1 neurons are excited, and a few are inhibited.\n  source: Main text, paragraph 6; Figure 3d and 3l; Extended Data Fig 6c\n  quote: Most stimulus-responsive VMHdm SF1 neurons were excited, although a few were inhibited\n  criterion: The Methods define only excitation. Inhibition is open, (a) the mirror rule, the mean of\n    any 1 s window in the first 30 s more than four baseline standard deviations below the baseline\n    mean on both trials, or (b) the mean over the first 30 s below that level. Reproduced when, for\n    every stimulus, excited cells outnumber inhibited cells and at least one stimulus has inhibited\n    cells, under both readings; per-stimulus percentages are reported.\n- id: fig3n-pca\n  statement: The first principal component of time-averaged population activity separates the\n    physical stimuli (rat, mouse, toy) from the auditory ones, and the second declines from initial\n    to later trials.\n  source: Main text, paragraph 6; Figure 3n; Extended Data Fig 7\n  quote: The first principal component (PC) of population activity reflected stimulus class (rat,\n    mouse, or toy vs. auditory stimuli), while the second PC declined from initial to later trials\n  criterion: From the Fig 3n legend, PCA of time-averaged population responses pooled across mice,\n    5 trials per stimulus from 3 days. Pooling is read as concatenating each mouse's tracked cells\n    into one population, trials matched by stimulus and order. Time averaging as in\n    fig3m-decoder (both of its readings). Which 5 of the 6 trials is open, (a) the first five, (b)\n    all six. The paper gives no measure; reproduced when the area under the ROC curve of PC1 scores,\n    physical against auditory trials, is at least 0.9, and the Spearman correlation of PC2 score with\n    presentation order (1 to 6 within stimulus) has magnitude at least 0.5 with p < 0.05 (thresholds\n    and tests set here; the sign of a PC is arbitrary, so PC2 is oriented so that the first trial is\n    positive). Partially reproduced when one of the two holds.\n- id: fig3m-decoder\n  statement: A five-way Naive Bayes decoder predicts stimulus identity from population activity above\n    chance (1/5) in held-out trials across three days of imaging.\n  source: Main text, paragraph 6; Figure 3m; Extended Data Fig 9a; Methods, Decoder analysis\n  quote: A 5-way Naïve Bayes decoder was able to predict stimulus identity with above-chance accuracy\n    in held-out trials, across three days of imaging\n  criterion: Per mouse, the cells tracked across the three days (Methods); 30 trials (5 stimuli, 2 per\n    day, 3 days); fitcnb with leave-one-out cross-validation, as Fig3m_naiveBayes_multiclass.m does.\n    The response is open between the code and the Methods, (a) the code, the mean after onset minus\n    the mean of the 200 frames before it (the window of the struct's rast field is not in the code;\n    downsampled_MEI_traces.m uses -200 to 550 frames, so 0 to 50 s); (b) the Methods, the mean from\n    30 s before to about 60 s after onset. Accuracy per stimulus and mouse as in the code. The paper\n    gives no test; reproduced when the mean over the 5 mice of the overall accuracy exceeds 0.2 under\n    both readings, and as a check the per-stimulus mean accuracies exceed 0.2 for at least four of\n    the five stimuli; a one-sided t-test of the five mice against 0.2 is reported as a variant.\n- id: ed9-persistent-decoding\n  statement: Stimulus identity remains decodable for tens of seconds after stimulus onset.\n  source: Main text, paragraph 6; Extended Data Fig 8 and 9b, 9c; Methods, Decoder analysis\n  quote: Importantly, stimulus identity also remained decodable for tens of seconds after stimulus\n    onset\n  criterion: A separate cross-validated decoder for each 1 s window from 10 s before to 30 s after\n    onset, on the time-averaged activity in that window (Methods), five-way and for each stimulus\n    pair, with the tracked cells and leave-one-out validation of fig3m-decoder. The code for this\n    decoder is not in the repository, so baseline subtraction is open, (a) subtract the mean of the\n    10 s before onset per trial, (b) none. Chance is 1/5 and 1/2. The paper gives no number;\n    reproduced when the five-way accuracy, mean over the 5 mice, exceeds 1/5 in at least 15 of the\n    20 windows from 10 to 30 s (threshold set here), under one reading, the other reported.\n- id: ed7cd-identity-across-days\n  statement: Stimulus identity is maintained by the population across days; a stimulus's population\n    response on one day correlates more with its own response on another day than with the responses\n    to other stimuli.\n  source: Extended Data Fig 7c and 7d\n  quote: stimulus identity is maintained by the population across days ... higher Pearson's correlation\n    of a stimulus with itself than with other stimuli\n  criterion: As ED7c_representation_separation_spearman.m computes it, per mouse, each tracked cell's\n    response averaged over time, the Pearson correlation across cells between day 3 and day 2, the\n    same stimulus averaged over the two trial pairs (trial 1 with 1, 2 with 2) and different stimuli\n    over four combinations; days 1 against 2 and 1 against 3 as ED Fig 7d. The paper gives no test;\n    reproduced when, in the mean over mice for days 2 against 3, each stimulus's same-stimulus\n    correlation exceeds the mean of its correlations with the other four; partially reproduced for\n    three or four stimuli. Whether it exceeds every other stimulus is reported.\n- id: ed7e-strong-cells-stable\n  statement: Cells with strong responses keep their stimulus tuning across days, while weakly\n    responding cells vary more from day to day.\n  source: Main text, paragraph 5; Extended Data Fig 7e\n  quote: The stimulus selectivity of strongly responsive cells remained stable across days\n  criterion: Per tracked cell and day pair (1 and 2, 2 and 3, 1 and 3), the Pearson correlation of\n    its five time-averaged stimulus responses on the two days, against its response to its most\n    preferred stimulus (ED Fig 7e legend), time averaging as in ed7cd-identity-across-days. The paper\n    gives no test; reproduced when the Spearman correlation between the two over all cells and day\n    pairs is positive with p < 0.05 (test set here).\n- id: ed7b-habituation\n  statement: The population response decreases across trials and days, suggesting habituation.\n  source: Main text, paragraphs 1 and 5; Extended Data Fig 7a and 7b\n  quote: Population mean response to different stimuli on each trial across three days of imaging,\n    showing a decrease in the population response across trials and days\n  criterion: Per mouse and trial, the population mean response; its measure is not given, so (a) the\n    mean over 0 to 45 s after onset (the preference window of the Methods) and (b) the peak are run,\n    baseline the 10 s before onset. The paper gives no test; reproduced when, in the mean over mice,\n    the Spearman correlation of response with presentation order (1 to 6) is negative for at least\n    four of the five stimuli under one reading (set here).\n- id: fig4cd-autocorrelation\n  statement: USS-evoked population activity evolves in time; its mean autocorrelation falls with the\n    lag between timepoints over the 45 s after onset.\n  source: Main text, paragraph 7; Figure 4b to 4d; Methods, Stimulus-evoked autocorrelation\n  quote: We then quantified time-evolving dynamics by taking the mean autocorrelation as a function of\n    the lag between timepoints\n  criterion: From the Methods, C is the correlation between all time columns of a cells by time\n    matrix, frames 0 to 45 s from onset at 11 Hz, averaged over the six USS trials of the three days,\n    then over the 5 mice; the mean for lag dt averages C(x, x + dt) for x from 0 to 45 - dt s. Cells\n    are open, (a) all cells imaged that day, (b) the tracked cells. The code's data path\n    (simStatsAndPlots.m, with simulated = 0) smooths with a 1 s box and samples at 1 Hz; that is a\n    variant. The paper gives no number; reproduced when, in each mouse, the mean autocorrelation at\n    lags of 30 to 45 s is below its mean at lags of 0 to 5 s (set here). The curve is kept for\n    fig4e-models-dynamics.\n- id: fig4g-rat-uss-specificity\n  statement: Rat- and USS-evoked population activity are partially correlated during the response and\n    its persistence, so the representations overlap but stay distinct.\n  source: Main text, paragraph 7; Figure 4f and 4g; Extended Data Fig 10d; Methods, Rat/USS\n    Pearson's correlation\n  quote: This specificity was quantified as the time-evolving Pearson's correlation between rat- vs.\n    USS-evoked activity\n  criterion: From the Methods, per mouse, the trial-averaged response of all cells on day 1; at each\n    frame from 10 s before to 30 s after onset at 11 Hz, the Pearson correlation between the rat and\n    USS population vectors. The paper gives no number; ED Fig 10d calls it partial overlap.\n    Reproduced when the mean over the 5 mice from 10 to 30 s after onset lies between 0 and 1 with\n    its mean +/- SEM excluding both 0 and 1 (set here). The curve is kept for fig4h-models-specificity.\n- id: fig4e-models-dynamics\n  statement: Models with slow neuromodulation alone or with NMDA-mediated recurrent excitation alone\n    cannot match the observed autocorrelation dynamics, while slow recurrent network (sRNN) models,\n    except the high-gain one, can.\n  source: Main text, paragraph 7; Figure 4a and 4e; Figure 4i; Methods, model sections and Data\n    similarity score, time-evolving dynamics\n  quote: models that used slow neuromodulatory transmission alone ... could not match the response\n    dynamics we observed in VMHdm SF1 neurons\n  data: with_inputs\n  depends_on:\n  - fig4cd-autocorrelation\n  criterion: Outside input, the model code at https://github.com/DJALab/VMHdm_persistence commit\n    7e5911b. Six models with the Methods' parameters (peptide, tau_p 25 s, 10% of 1000 cells driven;\n    RNN with NMDA, g 1, g_inh 3.8; sRNN low gain g 1, g_inh 8.8, tau_S 6 s; high gain g 6, g_inh 7.8;\n    high tau_S g 2.5, g_inh 4.25, tau_S 20 s; local connectivity sigma 0.7 N), 10 repeat simulations\n    each, spikes convolved with 0.5 s and 1.5 s exponentials and sampled at the 11 Hz frames. Where\n    the code's scripts set other values (the low-gain script uses g 2, g_inh 2.4, tau_m 0.1 s, dt\n    5 ms and drives a quarter of cells), the Methods are followed and the code is a variant. Score as\n    the Methods' Similarity Score dynamics against each mouse's USS curve, averaged over mice. The\n    paper sets no cut-off for \"match\"; two readings, (a) a model matches when its score is within the\n    range of the scores of each mouse against the mean of the other four, (b) the peptide and NMDA\n    models score below the low-gain, high tau_S and local sRNNs. Reproduced when the statement holds\n    under one reading.\n- id: fig4h-models-specificity\n  statement: Raising excitatory gain in the sRNN keeps rat and USS representations specific but breaks\n    the autocorrelation match; a 20 s slow time constant, or distance-dependent connectivity with\n    spatially biased inputs, matches both the dynamics and the specificity.\n  source: Main text, paragraph 7; Figure 4a3, 4a4, 4e and 4h; Extended Data Fig 10\n  quote: Maintaining stimulus specific representations during persistence could be achieved in the\n    sRNN by increasing the gain (strength) of excitatory synapses ... but such models failed to match\n    the autocorrelation dynamics of observed activity ... both temporal dynamics and stimulus\n    specificity could be matched by one of two models\n  data: with_inputs\n  depends_on:\n  - fig4g-rat-uss-specificity\n  - fig4e-models-dynamics\n  criterion: Simulations as in fig4e-models-dynamics; model rat and USS inputs as the Methods give\n    them, with the local model's middle 50% of cells driven by both and the outer 25% by one each.\n    Model correlation over cells firing 10 or more spikes across the two stimuli. Score as the\n    Methods' Similarity Score specificity. Its frames are open, (a) 0 to 45 s after onset as the\n    score's definition says, extending the data correlation past the 30 s of its own definition,\n    (b) 0 to 30 s, where the data correlation is defined. Matching read as in fig4e-models-dynamics,\n    both readings. Reproduced when the high-gain model matches specificity but not dynamics and the\n    high tau_S and local models match both, under one pair of readings.\n- id: fig4ijk-two-models\n  statement: Of the six models, only two (sRNN with a 20 s slow time constant, and sRNN with local\n    connectivity) satisfy both data similarity scores.\n  source: Main text, paragraph 7; Figure 4i to 4k\n  quote: only two models satisfied both conditions\n  data: with_inputs\n  depends_on:\n  - fig4e-models-dynamics\n  - fig4h-models-specificity\n  criterion: Both scores as in fig4e-models-dynamics and fig4h-models-specificity. \"Satisfied\" is not\n    defined; readings (a) within the range of the mice's leave-one-out scores on both, (b) the two\n    named models are the two with the highest minimum of the two scores. Reproduced when exactly the\n    two named models satisfy both under one reading.\n"
}
```

```
File created successfully at: claims/kennedy-2020.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kennedy-2020.yaml paper/10.1038-s41586-020-2728-4.txt; grep -n "—\|rather\|[^ ]: [^ ]" claims/kennedy-2020.yaml | grep -v "^\S*:\s*#" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/kennedy-2020.yaml'))
def walk(x,p=''):
  if isinstance(x,dict):
    [walk(v,p+'/'+k) for k,v in x.items()]
  elif isinstance(x,list):
    [walk(v,p) for v in x]
  elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(p,x[:80])
walk(d)
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
"
```

```
16 29 10
```

**Agent**

I've written `claims/kennedy-2020.yaml`: 39 claims, nothing committed. All 38 quotes pass the checker word for word. It reports two problems, both p-values the table prints as "1.80E‐05" and "5.20E‐05" (`fig1km-thigmotaxis`, `fig1lmn-silencing-before`). The checker doesn't know that number format, and I confirmed both by reading Supplementary Table 1. Because of these two, the checker still exits non-zero.

**Text read.** The accepted author manuscript in Europe PMC (PMC7606611), not the version of record. It has the main text, Methods, figure legends and Extended Data legends 1 to 10, plus Supplementary Table 1 (the statistics table). No main-text PDF was supplied, so I read no figures; the text and legends were enough.

**Code read.** github.com/DJALab/VMHdm_persistence at commit 7e5911b. It has the photometry scripts, the Fig 3m decoder, the Fig 2d/3b decay fits, the ED 7c cross-day correlation and the six network models. It has no code for picking responsive cells, peak times, the preference index, the PCA, the time-resolved decoders, the autocorrelation of the imaging data, or the similarity scores. Two helper functions the model scripts call are also missing.

**Claims.**
- 38 have quotes; one (`ed3de-openfield-vs-headfixed`) is `inferred`, read from legends and the supplement table.
- 16 have statistics, all from Supplementary Table 1 plus the r values in the ED 3h legend.
- 10 have expected values; 29 have criteria.
- 3 model claims are `with_inputs`, with the model code pinned as the outside input.
- 19 claims are on data the dataset doesn't hold: photometry, behaviour, slice and silicon-probe recordings. I kept them as `data: dataset`; the paper says these data are available on request.

**Details the paper leaves open, with the readings named:**
- **Responsive cells:** whether the 1 s windows slide or are fixed bins; whether the baseline SD is over frames or over 1 s means.
- **Cell counts:** cell-days pooled versus distinct tracked cells. The "78 tracked" can be a mean per mouse or a total.
- **The one mouse imaged at 20 Hz:** resampled to 11 Hz by averaging, as a standard choice.
- **Peak-time search window:** 0 to 30 s or 0 to 45 s.
- **Inhibited cells:** the Methods define only excitation, so I named a mirror of the 4-SD rule or a mean below the threshold.
- **Fig 3k:** excited only versus excited or inhibited; denominator of responsive cells or all cells; pooled versus mean over mice.
- **Preference histogram:** the Methods' formula runs 0 to 1 but the histogram runs −1 to +1, so I used the signed form.
- **Fig 2d fit:** which trials are used (the code uses the first trial; the Methods fit each trial), and the fit window (Methods 30 s; code −18 to 50 s, kept as a variant).
- **Decoder response window:** the code's baseline-subtracted mean after onset versus the Methods' −30 to +60 s.
- **Time-resolved decoder:** with or without baseline subtraction.
- **PCA:** the legend plots 5 trials per stimulus out of 6 presented.
- **Autocorrelation:** all cells versus tracked cells; the code's 1 Hz smoothing kept as a variant.
- **Specificity score frames:** 0 to 45 s as the score defines it, or 0 to 30 s where the correlation is defined.
- **"Matching" or "satisfying" the model scores:** no cut-off given; I named the mice's leave-one-out score range, or a ranking.
- **Model parameters:** the code's scripts differ from the Methods (for example, the low-gain script has g 2 and g_inh 2.4 against the Methods' 1 and 8.8). The Methods are followed and the code is a variant.

Many imaging claims say only "many", "most" or "above chance", with no number. For those I set thresholds or tests myself (for example at least 10% of cells, or AUC ≥ 0.9), and each criterion says the threshold is set there, not taken from the paper.

**Missing.** Nothing a claim needed is missing from the paper. The Methods and the legends cite different panel numbers in several places (decoder, confusion matrix, preference histograms); I followed the legends and recorded this in the opening comment. Supplementary Table 1 gives n = 8 mice for Fig 1g/h where the legends say 6; both are recorded.

## End of run

24 turns, 7 minutes, $2.23 at API prices, result: success.
