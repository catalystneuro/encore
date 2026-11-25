# powell-2021 · claims · run 45636960905

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
cat claims/fouke-2025.yaml; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.60454.txt",
 "offset": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/powell-2021.yaml 2>/dev/null; ls papers/ | head; grep -l "runner \"GitHub Actions\"\|GitHub Actions" claims/*.yaml | head -3
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.7554/elife.60454
title: Coupling between fast and slow oscillator circuits in Cancer borealis is temperature-compensated
datasets:
- archive: zenodo
  id: '3924718'
  relation: primary
authors.yaml
datasets
journals.yaml
keys.yaml
manifest.yaml
match
renamed.yaml
triage.yaml
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
```

**Agent calls Bash**

```bash
head -40 claims/andrews-2024.yaml; grep -n "^  [a-z_]*:" claims/*.yaml | awk -F: '{print $3}' | sort | uniq -c | sort -rn | head -30
```

```
# Claims for Andrews, Geng, Voitiuk et al. (2024), Nature Neuroscience 27, 2487-2499,
# doi:10.1038/s41593-024-01782-5, tested on DANDI:001132.
#
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, following docs/protocol.md (Reader). No data of the dandiset were seen; only its
# title and description on the archive ("HD-MEA recordings of human hippocampal brain slices
# obtained from epilepsy patients, including optogenetic stimulus and several
# hyperactivity-provoking conditions of culture medium").
#
# Text read: the NIH author manuscript in PubMed Central (PMC11881784, NIHMS2047739), full text
# with Methods, figure legends, Tables 1 and 2 and Extended Data legends, and its two supplement
# files from PMC: the Inventory of Supplemental Information (Extended Data and video legends)
# and Supplemental_Information.pdf (Supplemental Figs. S1 to S3, Supplemental Tables ST1 to
# ST6). The version of record was not read. The text cross-references its supplementary tables
# inconsistently (Extended Data legends point to ST4, ST5 and ST6 for the firing-rate p-values;
# the p-values are in ST2, ST3 and ST4; the Fig. 6 legend cites ST3 for a z-score that is in
# ST6; the Methods cite "Supplementary Table 2" for the ST5 odds ratios). The claims cite the
# tables by their content.
#
# Code read: https://github.com/braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit
[... 38 more lines not kept]
```

**Agent**

Full text with Methods and figure supplement legends is present. Now the code and the dataset description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/marderlab/gastric && cd gastric && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100
```

```
7a82b1f9a2239f46d73ae86d2cc70de8226d89be Thu Sep 9 12:53:16 2021 -0400 minor fixes
fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2 Tue Nov 17 09:36:37 2020 -0500 fixed a bug where an unpaired t-test was used
e83cf9eceac17e08220c0090f80665336e31b3ae Wed Oct 28 17:14:10 2020 -0400 cleaned up PD_hyp a bit
./mara_data_analysis.m
./spont_vs_evoked.m
./test.m
./dan_data_analysis.m
./stylesheet.xsl
./+gastric/plotLGRasters.m
./+gastric/findStimulationTimes.m
./+gastric/integerCoupling.m
./+gastric/plotSpiketimesISIs.m
./+gastric/q10.m
./+gastric/BurstPeriodsVsTime.m
./+gastric/groupAndPlotErrorBars.m
./+gastric/+model/setup.m
./+gastric/+model/show.m
./+gastric/+model/cost.m
./+gastric/+model/init.m
./+gastric/plotRasterTriggeredBy.m
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://zenodo.org/api/records/3924718 | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['title']);print(m.get('description'));print(m.get('version'));print([f['key'] for f in d.get('files',[])][:20])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && git diff fa07d36 7a82b1f --stat && cat README.md && cat +gastric/q10.m +gastric/integerCoupling.m +gastric/integerness.m +gastric/measurePhase.m
```

````
+gastric/plotIntegerCoupling.m                     |  8 +--
 paper-figures/PD_hyp.m                             |  4 +-
 paper-figures/fig_integer_coupling.m               |  4 +-
 paper-figures/fig_phase_relationships.m            | 76 +++++++++++++++++++++-
 .../fig_within_prep_spont_evoked_comparison.m      |  4 +-
 5 files changed, 84 insertions(+), 12 deletions(-)
# Interactions between two rhythmic circuits with distinct periods are maintained over a range of temperatures


This repo contains code that was used to analyze data for this paper. 

To reproduce figures from the paper, you will need to get this repo and the following repos: 

```bash
git clone https://github.com/sg-s/gastric
git clone https://github.com/sg-s/srinivas.gs_mtools
git clone https://github.com/sg-s/crabsort

```

[... 138 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && git checkout -q fa07d36 && cat paper-figures/fig_burst_period.m +gastric/getEvokedData.m
```

```
%%
% The point of fig 3 is to compare burst periods of PD and LG as temperature is varied. 

clearvars
close all
addpath('../')

colors = gastric.colors;


%% Analysis of gastric and pyloric rhythms at different temperatures
% In this document we look at pyloric and gastric rhtyhms at differnet temperatures.
% This data is from Dan Powell and the experiments that go into this are:

data = gastric.getEvokedData();


% compute burst metrics of all LG neurons
data = crabsort.computePeriods(data,'neurons',{'PD'},'ibis',.18,'min_spikes_per_burst',2);
data = crabsort.computePeriods(data,'neurons',{'LG'},'ibis',1,'min_spikes_per_burst',5);
[... 337 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && cat paper-figures/fig_integer_coupling.m +gastric/plotIntegerCoupling.m +gastric/groupAndPlotErrorBars.m
```

```
%%
% This figure shows that integer coupling persists across temperatures

clearvars
close all
addpath('../')


%% Analysis of gastric and pyloric rhythms at different temperatures
% In this document we look at pyloric and gastric rhythms at different temperatures.
% This data is from Dan Powell and the experiments that go into this are:

data = gastric.getEvokedData();



% compute burst metrics of all LG neurons
data = crabsort.computePeriods(data,'neurons',{'PD'},'ibis',.18,'min_spikes_per_burst',2);
data = crabsort.computePeriods(data,'neurons',{'LG'},'ibis',1,'min_spikes_per_burst',5);
data = crabsort.computePeriods(data,'neurons',{'DG'},'ibis',1,'min_spikes_per_burst',5);
[... 635 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && cat paper-figures/fig_phase_coupling.m
```

```
clearvars
close all
addpath('../')


data = gastric.getEvokedData();


min_temp = 5;
max_temp = 25;



% compute burst metrics of all LG neurons
data = crabsort.computePeriods(data,'neurons',{'PD'},'ibis',.18,'min_spikes_per_burst',2);
data = crabsort.computePeriods(data,'neurons',{'LG'},'ibis',1,'min_spikes_per_burst',5);
data = crabsort.computePeriods(data,'neurons',{'DG'},'ibis',1,'min_spikes_per_burst',5);



[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && git grep -n -i "rtest\|rayleigh\|40\b\|corr(" fa07d36 -- '*.m' | grep -v "outerposition" | head -30; echo ---; git grep -n -i "rtest\|rayleigh\|corr(" 7a82b1f -- '*.m' | head
```

```
fa07d36:+gastric/colors.m:6:C.DG = [40, 87, 41]/255;
fa07d36:+gastric/colors.m:8:C.('LG (PD hyp.)') = [0.9290    0.6940    0.1250];
fa07d36:+gastric/plotIntegerCoupling.m:76:[rho, pval] = corr(all_temp(~rm_this),N_pyloric_gastric(~rm_this),'Type','Spearman');
fa07d36:paper-figures/fig_duty_cycle.m:68:			sh.SizeData = 40;
fa07d36:paper-figures/fig_evoked_slowdown.m:81:		fits(i).r2 = corr(M(~rm_this)',fits(i).ff(time(~rm_this)));
fa07d36:paper-figures/fig_phase_relationships.m:129:[rho,p]=corr(temp_space(2:end-2)',M(2:end-2)','Type','Spearman')
fa07d36:paper-figures/fig_phase_relationships.m:377:ax(4).YLim(2) = ax(4).YLim(2)+40;
fa07d36:paper-figures/fig_phase_relationships.m:405:	[p(i),test_stat(i)]=circ_rtest(DG(i).phases*2*pi);
fa07d36:paper-figures/fig_phase_relationships.m:421:	[p(i),test_stat(i)]=circ_rtest(LG(i).phases*2*pi);
---
7a82b1f:+gastric/plotIntegerCoupling.m:76:[rho, pval] = corr(all_temp(~rm_this),N_pyloric_gastric(~rm_this),'Type','Spearman');
7a82b1f:paper-figures/fig_evoked_slowdown.m:81:		fits(i).r2 = corr(M(~rm_this)',fits(i).ff(time(~rm_this)));
7a82b1f:paper-figures/fig_phase_relationships.m:128:[rho,p]=corr(temp_space(2:end-2)',M(2:end-2)','Type','Spearman')
7a82b1f:paper-figures/fig_phase_relationships.m:404:	[p(i),test_stat(i)]=circ_rtest(DG(i).phases*2*pi);
7a82b1f:paper-figures/fig_phase_relationships.m:420:	[p(i),test_stat(i)]=circ_rtest(LG(i).phases*2*pi);
7a82b1f:paper-figures/fig_phase_relationships.m:438:		[p(i,j), test_stat(i,j)] = circ_rtest(this);
7a82b1f:paper-figures/fig_phase_relationships.m:468:		[p(i,j), test_stat(i,j)] = circ_rtest(this);
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && cat paper-figures/fig_phase_relationships.m; echo ======; git diff fa07d36 7a82b1f -- paper-figures/fig_phase_relationships.m +gastric/plotIntegerCoupling.m paper-figures/fig_integer_coupling.m
```

```
clearvars
close all
addpath('../')

colors = gastric.colors;

data = gastric.getEvokedData();

min_temp = 5;
max_temp = 25;


% make sure spiketimes are sorted
for i = 1:length(data)
	data(i).PD = sort(data(i).PD);
	data(i).LG = sort(data(i).LG);
end


% compute burst metrics of all LG neurons
[... 546 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && cat paper-figures/fig_evoked_slowdown.m | head -120; echo =====; cat paper-figures/PD_hyp.m | head -150
```

```
close all
clearvars -except data
addpath('../')


if ~exist('data','var')
	data = gastric.getEvokedData();
end

data = crabsort.computePeriods(data,'neurons',{'LG'},'ibis',1,'min_spikes_per_burst',7);


c = colormaps.redula(100);
min_temp = 5;
max_temp = 25;

figure('outerposition',[300 300 1200 1001],'PaperUnits','points','PaperSize',[1200 1001]); hold on

ax.burst_periods = subplot(2,2,1); hold on
xlabel('Time since stimulation end (s)')
[... 245 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gastric && grep -n "data_root\|include\|pref\|load\|8[0-9][0-9]_" paper-figures/fig_spont_rhythms.m paper-figures/fig_within_prep_spont_evoked_comparison.m +gastric/plotLGRasters.m | head -30; grep -n "ttest\|signrank\|ranksum" -r . --include=*.m
```

```
paper-figures/fig_spont_rhythms.m:7:% load the example dataset
paper-figures/fig_spont_rhythms.m:14:try data_root = getpref('gastric','data_loc');
paper-figures/fig_spont_rhythms.m:16:	error('You need to tell this script where you data is located using setpref ')
paper-figures/fig_spont_rhythms.m:18:C.path_name = fullfile(fileparts(fileparts(data_root)), 'haddad','830_116_2' );
paper-figures/fig_spont_rhythms.m:34:	C.file_name = ['830_116_' file_names{i} '.crab'];
paper-figures/fig_spont_rhythms.m:36:	C.loadFile;
paper-figures/fig_spont_rhythms.m:83:data_files = {'830_120_1','830_116_2'};
paper-figures/fig_spont_rhythms.m:88:	load([H '.cache'],'-mat')
paper-figures/fig_spont_rhythms.m:159:data_files = {'828_086_2','828_114_2','828_128','830_100','830_116_1','834_022','834_086_2'};
paper-figures/fig_spont_rhythms.m:165:	load([H '.cache'],'-mat')
paper-figures/fig_within_prep_spont_evoked_comparison.m:6:data_root = '/Volumes/DATA/pyloric-data';
paper-figures/fig_within_prep_spont_evoked_comparison.m:60:	C.path_name = fullfile(data_root, 'powell',spont_files{i});
paper-figures/fig_within_prep_spont_evoked_comparison.m:65:		C.loadFile;
paper-figures/fig_within_prep_spont_evoked_comparison.m:68:		C.loadFile;
paper-figures/fig_within_prep_spont_evoked_comparison.m:118:		C.loadFile;
paper-figures/fig_within_prep_spont_evoked_comparison.m:121:		C.loadFile;
./paper-figures/fig_burst_period.m:321:[~,p,~,stats]=ttest([data.Q_PD_mean],[data.Q_LG_mean])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "inferred" -A3 claims/*.yaml | head -12
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

[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"; grep -l "archive: zenodo" claims/*.yaml | head -2
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
[... 128 more lines not kept]
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
cd $TMPDIR/gastric && cat +gastric/BurstPeriodsVsTime.m +gastric/findStimulationTimes.m | head -90; sed -n 150,260p paper-figures/PD_hyp.m
```

```
% measures burst periods vs. time since stimulation end

function results = BurstPeriodsVsTime(data)

temperature = round(data.temperature);

all_stim_times = find(data.mask == 0);
stim_times = find(data.mask == 0);
last_stim  = stim_times(end);
stim_times = stim_times([diff(stim_times); NaN] > 120e3);
stim_times = [stim_times; last_stim];





for j = 1:length(stim_times)

	% figure out the temperature immediately after stim end
	stim_temp = round(mean(data.temperature(stim_times(j):stim_times(j)+5e3)));
[... 170 more lines not kept]
```

**Agent**

Code and text read. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/powell-2021.yaml",
 "content": "# Claims for Powell, Haddad, Gorur-Shandilya & Marder (2021), eLife 10, e60454,\n# doi:10.7554/elife.60454, tested on ZENODO:3924718.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-25, following docs/protocol.md (Reader, protocol version pilot-18). No data of the\n# dataset were seen; only its title and description on the archive (the paper's title and\n# abstract: evoked gastric mill and pyloric rhythms of Cancer borealis recorded from 7 to 23 C).\n#\n# Text read: the version of record as served by Europe PMC (PMC7889077, open access JATS,\n# flattened to paper/10.7554-elife.60454.txt), with Results, Discussion, Materials and methods,\n# the figure legends of Figures 1 to 6 and the legends of the four figure supplements (Figure 2,\n# figure supplement 1; Figure 3, figure supplement 1; Figure 4, figure supplements 1 and 2).\n# The paper has no other supplementary text. The legend of Figure 5f is garbled in the text\n# (\"Ratios of LG to PD cycle period were n across temperature\"); the Results sentence that\n# reports the same test is quoted instead.\n#\n# Code read: https://github.com/marderlab/gastric at commit\n# fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2 (2020-11-17), the commit the paper cites as archived\n# at Software Heritage, and the later head 7a82b1f9a2239f46d73ae86d2cc70de8226d89be\n# (2021-09-09), which differs in fig_phase_relationships.m (a prep-by-prep Rayleigh test on the\n# first 50 burst starts), plotIntegerCoupling.m (the null c.d.f. line commented out) and labels.\n# It holds MATLAB figure scripts (paper-figures/fig_burst_period.m for Figure 4,\n# fig_integer_coupling.m with +gastric/plotIntegerCoupling.m and +gastric/integerCoupling.m for\n# Figure 5, fig_phase_relationships.m with +gastric/measurePhase.m for Figure 6,\n# fig_evoked_slowdown.m with +gastric/BurstPeriodsVsTime.m for Figure 4 supplement 1, PD_hyp.m\n# for Figure 4 supplement 2, fig_spont_rhythms.m for Figure 2, and\n# fig_within_prep_spont_evoked_comparison.m for Figure 3 supplement 1). It relies on the\n# crabsort and srinivas.gs_mtools repositories (burst detection is crabsort.computePeriods),\n# which were not read. The list of the ten evoked preparations is in +gastric/getEvokedData.m\n# (901_005, 901_046, 901_049, 901_052, 901_062, 901_080, 901_086, 901_095, 901_098, 932_151).\n#\n# Data the paper used (Materials and methods). Isolated stomatogastric nervous systems of adult\n# male Cancer borealis, extracellular recordings of lgn, dgn, mvn, lvn and pdn at 10 kHz, with\n# saline temperature recorded on a channel; PD, LG and DG spikes sorted with crabsort. Three\n# sets: (1) nine preparations from crabs caught in July 2013 with spontaneous gastric mill\n# rhythms, temperature raised from 11 to 33 C in 2 C steps held at least 2 min (recordings of\n# Haddad and Marder 2018; the code reads them from a separate \"haddad\" folder); (2) ten\n# preparations from 2017 in which gastric mill rhythms were evoked by bilateral dpon\n# stimulation (ten 6-s trains at 0.6 Hz, 15 Hz within train) at temperature steps of 2 or 4 C\n# from 7 C until no rhythm could be evoked (typically 21 or 23 C); (3) nine preparations from\n# 2020 in which rhythms were evoked twice at 11, 15, 19 and 21 C with the two PD neurons\n# hyperpolarized and not. The dataset description names the evoked experiments; whether it\n# holds sets (1) and (3) is the author's to find.\n#\n# Method details fixed here from the paper's code where the Methods are silent: PD bursts\n# split at inter-spike intervals above 0.18 s with at least 2 spikes (LG and DG at 1 s with\n# at least 5, as the Methods say); the temperature of an event is the temperature channel at\n# the event's time (sampled at 1 kHz in the code); temperature steps are grouped in bins\n# centred on 7, 9, ..., 23 C, an event belonging to a bin when its temperature lies within\n# 1 C of the centre.\nschema_version: 2\npaper: doi:10.7554/elife.60454\nclaims:\n- id: fig2-spontaneous-11-to-30\n  statement: Spontaneous gastric mill activity (LG bursting) occurred at temperatures between\n    11 and 30 C, in nine preparations in total.\n  source: Results, Spontaneous gastric mill rhythms span a physiological range of temperatures,\n    paragraphs 1 and 3; Figure 2 and Figure 2, figure supplement 1\n  quote: We inspected a dataset of extracellular recordings of dgn and lgn during temperature\n    ramps ( Haddad and Marder, 2018 ) and found spontaneous gastric mill activity at temperatures\n    between 11°C and 30°C ... there were a total of nine preparations in which spontaneous\n    rhythms were observed at a variety of different temperatures\n  expected:\n  - quantity: preparations with spontaneous gastric mill rhythms\n    value: 9\n    tolerance: 0\n  - quantity: highest temperature with spontaneous LG bursting\n    value: 30\n    tolerance: 1\n    unit: C\n  criterion: LG bursts detected as the Methods define them (inter-spike interval above 1 s\n    starts a burst, at least 5 spikes). Reproduced when nine preparations of the spontaneous\n    set show LG bursts and, pooled over them, LG bursting occurs at temperature steps from 11 C\n    up to 30 C (the steps are 2 C apart, so 1 C tolerance on the top step; the count is exact\n    because it is a count of recordings). The paper gives no minimum number of bursts that\n    makes activity \"spontaneous gastric mill activity\"; the readings are (a) at least one LG\n    burst at the step, (b) at least two consecutive LG bursts, so that a period exists.\n- id: fig2a-less-regular-at-high-temperature\n  statement: In the example preparation of Figure 2a, spontaneous gastric mill rhythms were\n    relatively regular at lower temperatures and less regular at higher temperatures.\n  source: Results, Spontaneous gastric mill rhythms span a physiological range of temperatures,\n    paragraph 2; Figure 2a\n  quote: While these recordings show relatively regular gastric mill rhythms at lower\n    temperatures, they were less regular at higher temperatures\n  criterion: The example preparation is 830_116_2 in fig_spont_rhythms.m (the traces of Figure 2a\n    and the rasters of preparation 2 in Figure 2b are from the same animal, legend of Figure 2).\n    The paper gives no measure of regularity. Regularity is read as the coefficient of\n    variation of LG burst periods (bursts as in the Methods) at each temperature step with at\n    least three periods. Reproduced when the mean coefficient of variation over the steps above\n    20 C exceeds that over the steps at or below 20 C. The split at 20 C is a choice made here\n    (the paper names no boundary); the Spearman correlation of coefficient of variation with\n    temperature is shown as a variant.\n- id: fig3-evoked-7-to-21-in-9-of-10\n  statement: Gastric mill rhythms could be evoked by dpon stimulation across 7 to 21 C in 9 of\n    10 preparations, and the evoked rhythms remained regular at high temperature.\n  source: Results, Gastric mill rhythms speed up with increased temperature, paragraph 1;\n    Figure 3\n  quote: We were able to evoke gastric rhythms across a temperature range of 7 to 21°C in 9 of\n    10 preparations\n  expected:\n  - quantity: preparations with evoked rhythms at every step from 7 to 21 C\n    value: 9\n    tolerance: 0\n  - quantity: evoked preparations\n    value: 10\n    tolerance: 0\n  criterion: LG bursts as the Methods define them. A rhythm is present at a temperature bin\n    when the preparation has LG bursts in that bin. The paper does not say how many bursts make\n    an evoked rhythm; readings (a) at least one LG burst period, (b) at least 30 LG\n    significands, the minimum plotIntegerCoupling.m uses per preparation and temperature.\n    Reproduced when, under one reading, 9 of the 10 preparations have a rhythm in every bin\n    from 7 to 21 C. Steps were 2 or 4 C (Methods), so \"every bin\" means every bin the\n    preparation was held at; the author reports which bins each preparation has.\n- id: fig3s1-spontaneous-and-evoked-similar\n  statement: In 4 of 10 evoked preparations a spontaneous gastric mill rhythm was seen at 11 C\n    before stimulation; in three of these four the spontaneous and evoked rhythms were similar\n    in LG spike and burst timing and in cycle period.\n  source: Results, Gastric mill rhythms speed up with increased temperature, paragraph 2; Figure\n    3, figure supplement 1\n  quote: Three of the four preparations that had spontaneous and evoked rhythms shared\n    similarities in LG spike and burst timing ( Figure 3—figure supplement 1b ) and rhythm cycle\n    period (mean ± SD; Figure 3—figure supplement 1c )\n  expected:\n  - quantity: preparations with a spontaneous rhythm before stimulation\n    value: 4\n    tolerance: 0\n  - quantity: preparations with similar spontaneous and evoked periods\n    value: 3\n    tolerance: 0\n  criterion: The spontaneous and evoked stretches are those selected in\n    fig_within_prep_spont_evoked_comparison.m. LG burst periods as in the Methods, mean and SD\n    for each stretch (Figure 3, figure supplement 1c). The paper does not define \"similar\".\n    Readings (a) each mean lies within one SD of the other; (b) the mean plus or minus SD\n    intervals overlap. Reproduced when, under one reading, three of the four preparations are\n    similar and one is not.\n- id: fig4b-periods-decrease-all-preps\n  statement: Both LG (gastric mill) and PD (pyloric) burst periods decrease with increasing\n    temperature, a coordinated decrease seen in all 10 preparations.\n  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,\n    paragraphs 2 and 3; Figure 4a and 4b\n  quote: A coordinated decrease in both gastric mill and pyloric cycle periods was observed in\n    all 10 preparations ( Figure 4b )\n  expected:\n    quantity: preparations with decreasing PD and LG periods\n    value: 10\n    tolerance: 0\n  criterion: Burst periods of each burst as in the Methods and code (PD periods above 5 s and LG\n    periods above 50 s removed as outliers, fig_burst_period.m), assigned to the temperature at\n    burst start, averaged per preparation and temperature bin (gastric.groupAndPlotErrorBars).\n    The paper names no test of \"decrease\". Readings (a) for each preparation, the mean period\n    in its warmest bin is below that in its coldest bin, for PD and for LG; (b) for each\n    preparation, the Spearman correlation of bin mean period with bin temperature is negative,\n    for PD and for LG. Reproduced when all 10 preparations decrease under one reading.\n- id: fig4c-q10-about-2\n  statement: Most preparations (8 of 10) had a cycle period Q10 of about 2 for both the\n    pyloric and the gastric mill rhythm.\n  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,\n    paragraph 3; Figure 4c\n  quote: Figure 4c shows that most preparations (8 of 10) exhibited a cycle period Q 10 of ~2\n    for both the pyloric and gastric mill rhythms\n  expected:\n    quantity: preparations with Q10 near 2 for both PD and LG\n    value: 8\n    tolerance: 0.8\n  criterion: Q10 = (f_T / f_11)^(10 / (T - 11)), f the mean burst frequency, 11 C the reference\n    (Methods). The Methods take f_T as the mean frequency at each temperature step, giving one\n    Q10 per step, and average the Q10s per preparation; fig_burst_period.m instead computes a\n    Q10 for every burst against the mean frequency of bursts within 0.1 C of 11 C, drops Q10s\n    above 10, and averages per preparation. The Methods version is the main analysis and the\n    code's is a variant. The paper does not say how close to 2 \"~2\" is; readings (a) within\n    10% of 2 (1.8 to 2.2), the protocol's default tolerance; (b) 1.5 to 2.5. Reproduced when,\n    under one reading, 8 of 10 preparations (tolerance 0.8, so exactly 8) have both mean Q10s\n    in the range. The per-preparation values are reported.\n- id: fig4c-q10-pd-lg-not-different\n  statement: The apparent Q10s of the pyloric (PD) and gastric mill (LG) burst frequencies do\n    not differ (paired t-test, p = 0.235, N = 10, t = 1.27).\n  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,\n    paragraph 3; Figure 4c legend\n  quote: Estimated Q 10 s were not significantly different for LG and PD burst periods (paired\n    t-test, p = 0.235 , N = 10 , t = 1.27 )\n  statistics:\n  - test: paired t-test\n    statistic: t = 1.27\n    p: 0.235\n    n: 10 preparations\n  depends_on:\n  - fig4c-q10-about-2\n  criterion: A claim of absence, judged on the paper's test. Per-preparation mean Q10s of PD and\n    LG as in fig4c-q10-about-2 (Methods version), compared with a two-sided paired t-test over\n    the 10 preparations (Methods; ttest in fig_burst_period.m). Reproduced when p >= 0.05; not\n    reproduced when p < 0.05. The t and p are reported against 1.27 and 0.235 either way, and\n    the code's per-burst Q10 is shown as a variant.\n- id: fig4s1-slowdown-after-stimulation\n  statement: The evoked gastric mill rhythm slows down (LG burst period lengthens) with time\n    since stimulation.\n  source: Results, Gastric mill and pyloric cycle periods are similarly temperature-sensitive,\n    paragraph 2; Figure 4, figure supplement 1\n  quote: despite significant variability in the LG burst period, due to a slowing down ( Figure\n    4—figure supplement 1 ) of the gastric mill rhythm with time since stimulation\n  criterion: As in fig_evoked_slowdown.m and gastric.BurstPeriodsVsTime. Stimulation ends are\n    found from the stimulus artifacts (code's mask), stretches at one temperature held at least\n    120 s; LG burst periods above 30 s removed; time measured from the first LG burst after\n    stimulation; each stretch interpolated at 1 s over 0 to 600 s; mean over all stretches of\n    all preparations at each temperature (7 to 23 C), and a linear fit of mean period on time\n    per temperature (Figure 4, figure supplement 1c and d). The code detects LG bursts with at\n    least 7 spikes here, the Methods with at least 5; both are run. The paper gives no rule for\n    how many temperatures must slow; read here as reproduced when the fitted slope is positive\n    at a majority of the temperatures with data, under one burst rule.\n- id: fig4s2-gastric-without-pyloric-pacemaker\n  statement: With the pyloric pacemaker suppressed by hyperpolarizing both PD neurons, an\n    evoked gastric mill rhythm persists, and its cycle period decreases with increasing\n    temperature as it does with the pacemaker active.\n  source: Results, Gastric mill rhythms can be evoked when the pyloric pacemaker is suppressed,\n    paragraph 2; Figure 4, figure supplement 2c\n  quote: Figure 4—figure supplement 2c shows that the gastric mill rhythm cycle period steadily\n    decreased with increased temperature regardless of pyloric pacemaker activity\n  criterion: Figure 4, figure supplement 2c shows one preparation (999_017 in PD_hyp.m), LG\n    burst period (LG bursts at 1 s and 5 spikes; PD at 0.25 s and 2 spikes in PD_hyp.m) mean\n    and SEM at 11, 15, 19 and 21 C, PD active and hyperpolarized. Reproduced when in that\n    preparation the mean LG period falls monotonically across the temperatures with a rhythm,\n    in both conditions. The same test over all nine preparations is shown as a variant.\n- id: fig4s2-rhythm-counts\n  statement: In all nine preparations a gastric mill rhythm was evoked at 11 and 15 C, with the\n    pacemaker active and with AB/PD hyperpolarized; at 19 and 21 C only a subset produced one.\n  source: Results, Gastric mill rhythms can be evoked when the pyloric pacemaker is suppressed,\n    paragraph 2; Figure 4, figure supplement 2d\n  quote: Figure 4—figure supplement 2d shows that in all nine preparations, the gastric mill\n    rhythm was activated at 11°C and 15°C, whereas at 19°C and 21°C only a subset of preparations\n    produced gastric mill rhythms at these elevated temperatures\n  expected:\n  - quantity: preparations with a rhythm at 11 C, both conditions\n    value: 9\n    tolerance: 0\n  - quantity: preparations with a rhythm at 15 C, both conditions\n    value: 9\n    tolerance: 0\n  criterion: PD_hyp.m keeps a recording when it has at least 100 LG spikes; a rhythm is read as\n    present at a temperature and condition when a recording there has at least 100 LG spikes\n    and LG bursts (1 s, 5 spikes). Reproduced when all nine preparations have a rhythm at 11 and\n    15 C in both conditions and fewer than nine have one at 19 C and at 21 C in at least one\n    condition. The per-temperature counts are reported against the figure.\n- id: fig5a-example-ratios\n  statement: In the example preparation the ratio of LG to PD period is close to an integer at\n    both temperatures, about 10 at 7 C and about 11 at 23 C, and PD bursts end shortly before\n    LG bursts start.\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraph 2; Figure 5a\n  quote: The ratio of LG to PD periods was close to an integer at both temperatures (~10 at 7°C\n    and ~11 at 23°C)\n  expected:\n  - quantity: T_LG / mean T_PD at 7 C (fig_integer_coupling.m label 10.06)\n    value: 10.06\n    tolerance: 1.0\n  - quantity: T_LG / mean T_PD at 23 C (fig_integer_coupling.m label 10.98)\n    value: 10.98\n    tolerance: 1.1\n  criterion: The example is preparation 901_046, files 0006 (7 C) and 0079 (23 C), in\n    fig_integer_coupling.m, which labels T_LG = 9.17 s and mean T_PD = 0.911 s at 7 C, and T_LG\n    = 3.44 s and mean T_PD = 0.313 s at 23 C, for one LG cycle each. The code does not record\n    which LG cycle was drawn (the bars were placed by hand). Readings (a) the LG cycle whose\n    period is closest to the labelled T_LG; (b) the median ratio over all LG cycles of the\n    file. Reproduced when, under one reading, both ratios are within 10% of the labels and\n    within 0.2 of an integer.\n- id: fig5d-lg-pd-integer-coupled\n  statement: LG and PD burst periods are significantly integer-coupled at every temperature\n    from 7 to 21 C (two-sample Kolmogorov-Smirnov test against shuffled periods, p < 1e-5, D >\n    0.24).\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraphs 4 and 5; Figure 5b, 5d and 5e\n  quote: LG and PD were significantly integer-coupled, at temperatures from 7°C to 21°C (p < 10\n    –5 , D > 0.24)\n  statistics:\n  - test: two-sample Kolmogorov-Smirnoff test, observed against shuffled significands, per\n      temperature\n    statistic: D > 0.24\n    p: 0.00001\n    p_relation: \"<\"\n    corrected: Bonferroni over 9 temperature steps (threshold 0.05/9 = 0.0056)\n    n: LG bursts pooled across all 10 preparations at each temperature\n  criterion: Per LG burst, the mean PD period over that LG cycle, as integerCoupling.m computes\n    it (PD burst start nearest the next LG start minus the PD burst start nearest this LG start,\n    over the number of PD cycles between them); mean PD periods above 2 s and LG periods above\n    30 s removed (plotIntegerCoupling.m); significand = fractional part of LG period over mean\n    PD period (Methods). Per temperature bin, pooled over preparations (Methods), a\n    two-sample KS test of the significands against significands from shuffled pairings\n    (Methods). How the shuffle is formed is open; readings (a) as the code, 100 LG periods and\n    100 mean PD periods drawn independently with replacement from the bin; (b) a random\n    permutation of the bin's mean PD periods against its LG periods, same size. Because the\n    shuffle is random, each is repeated 1000 times with a fixed seed and the median p and D\n    reported (a standard choice; the paper used one draw). Reproduced when, under one reading,\n    every bin from 7 to 21 C has p < 0.05/9 with D > 0.24 (10% tolerance, D > 0.216); partially\n    reproduced when every bin is significant but some D or p miss the reported bounds.\n- id: fig5d-dg-pd-not-coupled\n  statement: DG and PD burst periods are not significantly integer-coupled at any temperature\n    (p > 0.02, D < 0.16).\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraphs 4 and 5; Figure 5c, 5d and 5e\n  quote: while DG and PD were not significantly coupled at any temperature (p > 0.02, D < 0.16)\n  statistics:\n  - test: two-sample Kolmogorov-Smirnoff test, observed against shuffled significands, per\n      temperature\n    statistic: D < 0.16\n    p: 0.02\n    p_relation: \">\"\n    corrected: Bonferroni over 9 temperature steps (threshold 0.05/9 = 0.0056)\n  depends_on:\n  - fig5d-lg-pd-integer-coupled\n  criterion: A claim of absence, judged on the paper's test, the same KS test as\n    fig5d-lg-pd-integer-coupled with DG in place of LG (code's shuffle, reading a, median over\n    the repetitions), at the Bonferroni threshold 0.05/9. Reproduced when no temperature bin\n    reaches p < 0.0056; not reproduced when any does. The D and p of every bin are reported\n    against D < 0.16 and p > 0.02, and the permutation shuffle is shown as a variant.\n- id: fig5e-lg-area-exceeds-dg\n  statement: The area between the significand c.d.f. and the diagonal, a measure of integer\n    coupling, is larger for LG/PD than for DG/PD at every temperature, and the DG/PD areas\n    overlap those of shuffled periods.\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraph 5; Figure 5e\n  quote: Areas for LG/PD significands were larger than areas for DG/PD significands at every\n    temperature ( Figure 5e ), suggesting greater integer coupling. Areas for DG/PD significands\n    overlapped with areas computed after shuffling\n  depends_on:\n  - fig5d-lg-pd-integer-coupled\n  criterion: As plotIntegerCoupling.m computes it. For each preparation and temperature bin with\n    at least 30 significands, the area is the mean absolute difference between the empirical\n    c.d.f. (interpolated at 100 points on 0 to 1) and the diagonal, averaged over 100 bootstrap\n    resamples; the shuffled area uses as many significands drawn from the pool of shuffled\n    ratios over all temperatures. Each bin's value is the mean over preparations, with SEM\n    across preparations. Reproduced when the LG mean exceeds the DG mean in every bin where\n    both exist, and the DG mean plus or minus SEM overlaps the shuffled mean plus or minus SEM\n    in most bins. The overlap rule is a reading of \"overlapped\" (the paper gives none).\n- id: fig5f-ratio-independent-of-temperature\n  statement: The ratio of LG to PD cycle period does not change with temperature (Spearman\n    test, p = 0.88, n = 3799).\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraph 5; Figure 5f\n  quote: Ratios of LG to PD cycle period were spread across a similar range of temperatures,\n    even at higher temperatures when integer coupling was less pronounced (p = 0.88, n = 3799 ,\n    PD cycles pooled across all preparations, Spearman test)\n  statistics:\n  - test: Spearman test\n    p: 0.88\n    n: 3799 cycles pooled across all preparations\n  depends_on:\n  - fig5d-lg-pd-integer-coupled\n  criterion: A claim of absence, judged on the paper's test. As plotIntegerCoupling.m, the ratio\n    of each LG period to the mean PD period over that cycle (same filters as\n    fig5d-lg-pd-integer-coupled), against the temperature at the LG burst start, Spearman\n    correlation over all cycles pooled across preparations. Reproduced when p >= 0.05; not\n    reproduced when p < 0.05. Rho and the number of cycles (3799 reported, though the paper\n    calls them PD cycles, the code counts LG cycles) are reported either way; the code's\n    prep-by-prep means per temperature are shown as a variant.\n- id: fig5f-ratio-range\n  statement: At low temperatures the ratios of LG to PD cycle period range widely, from about 5\n    to 25.\n  source: Results, Integer coupling is maintained across a physiological temperature range,\n    paragraph 5; Figure 5f\n  quote: At low temperatures, when integer coupling was particularly strong (as seen from the\n    horizontal banding), these ratios were distributed over a wide range from 5 to 25\n  depends_on:\n  - fig5d-lg-pd-integer-coupled\n  expected:\n    quantity: range of LG to PD period ratios at low temperature\n    value: 5\n    unit: lower bound; upper bound 25\n  criterion: Ratios as in fig5f-ratio-independent-of-temperature. \"Low temperatures\" is not\n    defined; readings (a) the 7 C bin, (b) bins 7 to 11 C. A range of 5 to 25 widened by 10% of\n    each bound is 4.5 to 27.5. Reproduced when, under one reading, the 2.5th to 97.5th\n    percentile of the ratios lies within 4.5 to 27.5 and spans at least 5.5 to 22.5 (the range\n    narrowed by 10% of each bound). The percentiles are a choice made here, as the paper gives\n    the range by eye.\n- id: fig6b-lg-phase-locked\n  statement: LG burst starts are phase-locked to the PD cycle, their distribution in PD phase\n    sharply peaked and significantly non-uniform (Rayleigh test, p < 4e-4, 7.5 < z < 45).\n  source: Results, LG preserves phase locking to PD across physiological temperatures, paragraph\n    2; Figure 6a and 6b\n  quote: LG burst start probabilities were sharply peaked ( Figure 6b ) and were significantly\n    different from a uniform distribution ( Figure 6b , dashed line, p < 4×10 –4 , 7.5<z<45,\n    Rayleigh test for non-uniformity; see Methods for details)\n  statistics:\n  - test: Rayleigh test for non-uniformity, per preparation and temperature\n    statistic: 7.5 < z < 45\n    p: 0.0004\n    p_relation: \"<\"\n  criterion: PD phase of each LG burst start = time since the start of the preceding PD burst\n    over that PD burst's period (Methods; measurePhase.m, which skips the first and last LG\n    burst of each preparation); temperature that at the PD burst start, rounded to a whole\n    degree. The Rayleigh test (circ_rtest of Berens 2009, z = n R^2). Which sample is tested\n    is open, as the Methods, the archived code and the later code differ. Readings (a) Methods,\n    the first 40 LG burst starts of each preparation and temperature, combinations with fewer\n    than 40 excluded; (b) the later code (commit 7a82b1f), the first 50, combinations with\n    fewer than 50 excluded; (c) the archived code, all burst starts of a temperature pooled over\n    preparations, temperatures with fewer than 100 excluded. Under (a) z cannot exceed 40, so\n    the reported z of 45 fits (b) or (c) better. Reproduced when, under one reading, every\n    tested combination has p < 0.05 and the largest p and the range of z agree with p < 4e-4\n    and 7.5 to 45 (widened by 10%, 6.75 to 49.5); partially reproduced when every combination\n    is significant but the p or z bounds are not met.\n- id: fig6b-lg-start-counts\n  statement: A total of 3816 LG burst starts and 3228 DG burst starts across nine temperature\n    points and 10 preparations enter the phase distributions, and about 35% of preparation and\n    temperature combinations have fewer than 40 burst starts.\n  source: Materials and methods, Analysis of distribution of LG/DG burst starts in PD phase,\n    paragraph 2\n  quote: Preparation and temperature combinations where there were <40 burst starts (~35% of\n    data) were excluded. A total of n = 3816 LG burst starts and n = 3228 DG burst starts across\n    nine temperature points and 10 preparations are plotted in Figure 6b,d\n  expected:\n  - quantity: LG burst starts\n    value: 3816\n    tolerance: 381.6\n  - quantity: DG burst starts\n    value: 3228\n    tolerance: 322.8\n  - quantity: fraction of data excluded for fewer than 40 burst starts\n    value: 0.35\n    tolerance: 0.035\n  criterion: Burst starts as in the Methods (LG and DG at 1 s and 5 spikes) with a defined PD\n    phase, in temperature bins 7 to 23 C. 3816 is not a multiple of 40, so the totals are read\n    as all burst starts plotted, not the first-40 subset. The \"~35% of data\" is open; readings\n    (a) the fraction of preparation and temperature combinations, (b) the fraction of burst\n    starts. Reproduced when both totals are within tolerance and the fraction is within\n    tolerance under one reading.\n- id: fig6b-lg-phase-constant\n  statement: From 7 to 21 C, LG bursts start at a phase of about 0.5 in the PD cycle, and this\n    phase does not trend with temperature (Spearman test, p = 0.46, rho = -0.31).\n  source: Results, LG preserves phase locking to PD across physiological temperatures, paragraph\n    2; Figure 6b inset\n  quote: From 7°C to 21°C, LG bursts started at a phase of ~0.5 in the PD cycle ( Figure 6b ,\n    inset), and this phase offset did not significantly trend across this temperature range (p\n    = 0.46, ρ = –0.31, Spearman test)\n  statistics:\n  - test: Spearman test\n    statistic: rho = -0.31\n    p: 0.46\n    n: 8 temperature steps (7 to 21 C), means across preparations\n  expected:\n    quantity: mean LG burst start phase in the PD cycle\n    value: 0.5\n    tolerance: 0.05\n  depends_on:\n  - fig6b-lg-phase-locked\n  criterion: Phases as in fig6b-lg-phase-locked. As fig_phase_relationships.m, the circular mean\n    phase per preparation and temperature bin, then the circular mean over preparations per bin\n    (gastric.groupAndPlotErrorBars with circular means); Spearman correlation of these bin means\n    with temperature over the bins 7 to 21 C. The trend is a claim of absence judged on this\n    test (reproduced when p >= 0.05, rho reported against -0.31). The phase holds when every\n    bin mean from 7 to 21 C lies within 0.5 plus or minus 0.05. Whether all LG burst starts or\n    the first 40 per preparation and temperature (Methods, Figure 6b, e) enter is open; both\n    are run, and the claim holds when both parts hold under one.\n- id: fig6c-lg-spiking-drops-near-pd-end\n  statement: LG spike probability in the PD cycle shows a pronounced decrease at higher\n    temperatures, occurring close to PD burst termination.\n  source: Results, LG preserves phase locking to PD across physiological temperatures, paragraph\n    3; Figure 6c\n  quote: We measured the spike probability of LG conditional on PD phase across this temperature\n    range and found a pronounced decrease in the probability of spiking in LG at higher\n    temperatures ( Figure 6c ). This decrease in LG spike probability occurred close to PD burst\n    termination\n  criterion: As fig_phase_relationships.m, the PD phase of every LG spike (measurePhase.m),\n    grouped by rounded temperature, temperatures with at least 1000 spikes, histogram of 30\n    bins on 0 to 1 normalized as a p.d.f.; the mean PD burst-end phase per temperature. The\n    paper gives no measure of the decrease. It is read here as the p.d.f. in the bin that holds\n    the mean PD burst-end phase (readings (a) that bin, (b) the lowest bin within 0.1 phase of\n    it). Reproduced when, under one reading, this value is below 1 (the uniform level) at the\n    warmest temperature included and its Spearman correlation with temperature across the\n    included temperatures is negative.\n- id: fig6e-dg-not-phase-locked\n  statement: DG bursts are not phase-locked to PD; DG burst starts are not sharply peaked in PD\n    phase, not significantly non-uniform in every preparation and temperature, and the effect\n    is much smaller than for LG (p from 0.001 to 0.85, 0.15 < z < 13).\n  source: Results, LG preserves phase locking to PD across physiological temperatures, paragraph\n    4; Figure 6d and 6e\n  quote: DG burst starts are not sharply peaked in PD phase, and they are not significantly\n    different from a uniform distribution for all preparations at all temperatures ( Figure 6e ,\n    p ∈ [0.001, 0.85], 0.15 < z < 13, Rayleigh test)\n  statistics:\n  - test: Rayleigh test for non-uniformity, per preparation and temperature\n    statistic: 0.15 < z < 13\n    p: 0.001\n    p_relation: \">\"\n  depends_on:\n  - fig6b-lg-phase-locked\n  criterion: The same test and sample readings as fig6b-lg-phase-locked, with DG burst starts.\n    Reproduced when, under the reading that reproduced the LG claim (or any reading if none\n    did), at least one combination has p >= 0.05 and the largest DG z is below the smallest LG\n    z of fig6b-lg-phase-locked. The p and z ranges are reported against 0.001 to 0.85 and 0.15\n    to 13.\n- id: fig6f-dg-spiking-no-drop\n  statement: DG spike probability does not show a noticeable decrease close to the end of PD\n    bursting.\n  source: Results, LG preserves phase locking to PD across physiological temperatures, paragraph\n    4; Figure 6f\n  quote: DG spike probability also does not show a noticeable decrease close to the end of PD\n    bursting\n  depends_on:\n  - fig6c-lg-spiking-drops-near-pd-end\n  criterion: The measure of fig6c-lg-spiking-drops-near-pd-end, applied to DG spikes. The paper\n    reports no test. Reproduced when, under the reading used for LG, the DG p.d.f. at the PD\n    burst-end bin is not below 1 by more than half of the LG drop at the same temperature, at\n    every included temperature. The half is a choice made here.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/powell-2021.yaml",
 "old_string": "  expected:\n    quantity: range of LG to PD period ratios at low temperature\n    value: 5\n    unit: lower bound; upper bound 25\n  criterion",
 "new_string": "  expected:\n  - quantity: lower end of the LG to PD period ratios at low temperature\n    value: 5\n    tolerance: 0.5\n  - quantity: upper end of the LG to PD period ratios at low temperature\n    value: 25\n    tolerance: 2.5\n  criterion"
}
```

```
The file claims/powell-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/powell-2021.yaml paper/10.7554-elife.60454.txt; grep -nE "[^\"']: [^ ]" claims/powell-2021.yaml | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; grep -n "—\|rather" claims/powell-2021.yaml | grep -v "Figure [0-9]—figure"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml
d=yaml.safe_load(open('claims/powell-2021.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
22 7 22 10
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
?? claims/powell-2021.yaml
?? scripts
```

**Agent**

I wrote `claims/powell-2021.yaml`. The quote checker reports 22 claims, 22 quotes, 7 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC7889077, open access JATS). It includes the Results, Discussion, Methods, the legends of Figures 1 to 6 and the legends of all four figure supplements. The paper has no other supplementary text. The Figure 5f legend is garbled ("were n across temperature"), so that claim quotes the matching Results sentence instead. I did not open the PDF.

**Code read:** github.com/marderlab/gastric at the commit the paper cites (`fa07d36`), and the later head (`7a82b1f`), which adds a per-preparation Rayleigh test. I did not read the libraries it depends on, `crabsort` (which does the burst detection) and `srinivas.gs_mtools`.

**Claims:** 22, all with quotes. 7 carry statistics, 10 have expected values and all 22 have a criterion.

What they cover:
- Spontaneous rhythms from 11 to 30 °C, and less regular in the warm example.
- Evoked rhythms from 7 to 21 °C in 9 of 10 preparations.
- Spontaneous and evoked rhythms similar in 3 of 4 preparations.
- Periods shorten with temperature in all 10 preparations.
- Q10 near 2 in 8 of 10 preparations; PD and LG Q10 not different (paired t-test, p = 0.235).
- The gastric rhythm slows with time after stimulation.
- With the PD neurons hyperpolarized, the rhythm persists, and the counts per temperature.
- Example ratios, LG–PD integer coupling (KS test), no DG coupling, coupling areas, and the ratio not changing with temperature (Spearman, p = 0.88) with its range.
- LG phase locking (Rayleigh test), burst start counts, a constant phase near 0.5, LG spiking dropping near the end of the PD burst, and no DG locking and no DG drop.

**Details fixed from the code where the Methods are silent:**
- PD bursts split at gaps over 0.18 s with at least 2 spikes.
- Temperature bins are ±1 °C around 7, 9, …, 23 °C.
- Outlier cut-offs for periods.
- How the mean PD period within an LG cycle is computed.
- How the coupling area and its bootstrap are computed.

**Details left open, with the readings named:**
- **Q10:** the Methods average one Q10 per temperature step; the code computes one per burst and drops values above 10. The Methods version is the main analysis and the code's is a variant. "~2" is read as 1.8–2.2 or 1.5–2.5.
- **KS shuffle:** either the code's 100 independent resamples or a permutation of the same size. Since the shuffle is random, it is repeated over many seeds and the median p reported.
- **Rayleigh sample:** the first 40 per preparation and temperature (Methods), the first 50 (later code), or pooled per temperature (archived code). With 40 burst starts z cannot exceed 40, so the reported z of 45 does not fit the Methods as written.
- **"~35% of data" excluded:** a fraction of preparation–temperature combinations, or of burst starts.
- **Thresholds the paper gives none for:** what counts as a rhythm being present, "similar" for spontaneous against evoked, the test for "decrease" in periods, "low temperatures" for the ratio range, and a measure of the drop in spiking near the PD burst end.
- **Slowdown burst rule:** the code needs 7 spikes per LG burst here, the Methods 5; both are run.
- **Example cycle:** which LG cycle is drawn in Figure 5a.
- **Thresholds I set myself, each marked in its criterion as my choice:** a 20 °C split for regularity, percentiles for the ratio range, and half the LG drop for the DG comparison.

**Nothing missing from the paper.** Two things for the author to confirm in the dataset, since I did not look:
- The spontaneous recordings (2013, first reported in Haddad and Marder 2018) and the PD-hyperpolarization experiments (2020) may not be in the record. The archive description names only the evoked experiments.
- The paper calls the 3799 cycles in the Spearman test "PD cycles", but the code counts LG cycles.

## End of run

26 turns, 4 minutes, $1.83 at API prices, result: success.
