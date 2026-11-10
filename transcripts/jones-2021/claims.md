# jones-2021 · claims · run 42835091138

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,192p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/*.txt; cat papers/datasets/jones-2021.yaml 2>/dev/null; ls paper; python -c "print()"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 30,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 30,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The main text and Methods are there; next I'm reading the rest of the Methods and checking that the supplement holds Tables S2 to S7.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 330,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "SUPPLEMENT\|^=====\|^-----\|Table S[0-9]\.\|Figure S[0-9]\.\|^Supplement" paper/*.txt | sed -n 1,80p
```

Result: not kept, because it reads the paper's text.

**Agent**

The main supplement (Figures S1 to S7, Tables S1 to S6) is in the text; only Table S7 (sex stratification, an xlsx) is missing. Reading the supplement now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 510,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  for r in 905,940 1005,1030 1155,1185 1340,1372 1465,1490 1820,1880 2275,2345; do sed -n "${r}p" paper/*.txt; echo ----; done
```

Result: not kept, because it reads the paper's text.

**Agent**

Now Tables S2 and S3, which hold the per-feature statistics.

**Agent calls Bash**

```bash
cd  sed -n 2350,2420p paper/*.txt; echo ......; sed -n 2650,2720p paper/*.txt; echo .....; sed -n 2890,2990p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The supplement gives test statistics but not means, so effect directions come from the Results text. Next, the paper's code on Zenodo (10.5281/zenodo.5618979).

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://zenodo.org/api/records/5618979 | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('related_identifiers')); [print(f['key'], f['size'], f['links']['self']) for f in d.get('files',[])]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && curl -sL -o c.zip "https://zenodo.org/api/records/5618979/files/emilyasterjones/interneurons_modulate_drive-v1.0.0.zip/content" && unzip -oq c.zip && find . -type f | grep -v c.zip | head -100; git ls-remote https://github.com/emilyasterjones/interneurons_modulate_drive v1.0.0 2>&1 | head
```

Result: the fetched text is not kept.

**Agent**

The code is GitHub emilyasterjones/interneurons_modulate_drive, tag v1.0.0, commit 63b1acb. Reading the statistics and feature code.

**Agent calls Bash**

```bash
cd $TMPDIR/code/emil*; cat README.md; wc -l Statistics/*.m "Rest Analysis"/*.m "Run Analysis"/*.m | sort -n | tail -50
```

```
# interneurons_modulate_drive
 MATLAB and IGOR scripts used to generate "Hippocampal GABAergic Interneurons Bidirectionally Modulate Signatures of Internal and External Drive"
 
Preprint: https://www.biorxiv.org/content/10.1101/2021.01.04.425303v1.full

Requires the following libraries:
* NeuroQuery: https://bitbucket.org/mkarlsso/neuroquery/src/master/
* Trodes: https://bitbucket.org/mkarlsso/trodes/src/master/
* Chronux: https://chronux.org/
* plotSpread: https://www.mathworks.com/matlabcentral/fileexchange/37105-plot-spread-points-beeswarm-plot
    18 Rest Analysis/dayprocess_dspikes.m
    18 Statistics/plotsubfig.m
    27 Statistics/HBcorrect.m
    32 Rest Analysis/runRTS.m
    33 Rest Analysis/DSdescript.m
    34 Rest Analysis/runDSdescript.m
    36 Run Analysis/velquant.m
    37 Statistics/plot_figures.m
    38 Run Analysis/contMUA.m
    49 Statistics/calcunpairedLMM.m
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/emil*/Statistics; cat calcLMM.m calcInteraction.m HBcorrect.m; sed -n 1,236p runcalcLMM_figs.m
```

```
function [lme, vehcoeff, cnocoeff] = calcLMM(vehdata,cnodata,logtransform)

bump = 0;
if logtransform
    vehmins = cellfun(@min,vehdata);
    cnomins = cellfun(@min,cnodata);
    datamin = min([vehmins cnomins]);
    if datamin<=0
        bump = -datamin+0.001;
        vehdata = cellfun(@(x) x+bump,vehdata,'UniformOutput',false);
        cnodata = cellfun(@(x) x+bump,cnodata,'UniformOutput',false);
    end
    vehdata = cellfun(@log,vehdata,'UniformOutput',false);
    cnodata = cellfun(@log,cnodata,'UniformOutput',false);
end

%initialize
animal = zeros(length(vehdata{1})+length(cnodata{1}),1);
len = [vehdata{1}; cnodata{1}];
x = NaN(1,3);
[... 316 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*; cat Statistics/calcjointLMM.m; cat "Rest Analysis/getvalidrips.m" "Rest Analysis/calcriprates2.m" "Rest Analysis/RTMUA.m"
```

```
function lme = calcjointLMM(vehdata1,cnodata1,vehdata2,cnodata2,logtransform)

if logtransform
    vehmins = cellfun(@min,vehdata1);
    cnomins = cellfun(@min,cnodata1);
    datamin = min([vehmins cnomins]);
    if datamin<=0
        bump = -datamin+0.001;
        vehdata1 = cellfun(@(x) x+bump,vehdata1,'UniformOutput',false);
        cnodata1 = cellfun(@(x) x+bump,cnodata1,'UniformOutput',false);
    end
    vehdata1 = cellfun(@log,vehdata1,'UniformOutput',false);
    cnodata1 = cellfun(@log,cnodata1,'UniformOutput',false);
    
    vehmins = cellfun(@min,vehdata2);
    cnomins = cellfun(@min,cnodata2);
    datamin = min([vehmins cnomins]);
    if datamin<=0
        bump = -datamin+0.001;
        vehdata2 = cellfun(@(x) x+bump,vehdata2,'UniformOutput',false);
[... 269 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*; grep -n "minstd\|bins'\|'bins\|velocity\|immob\|exclude\|30\b\|interripwin\|win =\|event_window\|chain\|0\.2\|200" "Rest Analysis/runcalcriprates.m" "Rest Analysis/runRTMUA.m" "Rest Analysis/runripdescript.m" "Rest Analysis/ripdescript.m" | head -80
```

```
Rest Analysis/runcalcriprates.m:17:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'};
Rest Analysis/runcalcriprates.m:20:f = createfilter('animal', animals, 'epochs', epochfilter, 'data', datafilter, 'excludetime', timefilter);
Rest Analysis/runcalcriprates.m:23:f = setfilterfunction(f, 'calcriprates2', {'ripples'},'appendindex',2,'bins',binrange);
Rest Analysis/runRTMUA.m:11:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'}; %sleep
Rest Analysis/runRTMUA.m:18:f = createfilter('animal', animals, 'epochs', epochfilter, 'data', datafilter, 'excludetime', timefilter);
Rest Analysis/runRTMUA.m:19:f = setfilterfunction(f, 'RTMUA', {'mua','ripples','chinfo'},'minstd',3,'trig',trigcrit,'probe',probecrit);
Rest Analysis/runripdescript.m:16:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'};
Rest Analysis/runripdescript.m:18:f = createfilter('animal', animals, 'epochs', epochfilter, 'data', datafilter, 'excludetime', timefilter);
Rest Analysis/runripdescript.m:21:f = setfilterfunction(f, 'ripdescript', {'ripples','chinfo'},'minstd',5,'trig',trigcrit,'probe',probecrit);
Rest Analysis/runripdescript.m:42:    excluded{a} = [];
Rest Analysis/runripdescript.m:50:        excluded{a} = [excluded{a}; results{1}{e}.excluded(2)];
Rest Analysis/runripdescript.m:65:    ischain{a} = iri{a}<.2;
Rest Analysis/runripdescript.m:72:    avgexcluded(a) = mean(excluded{a});
Rest Analysis/runripdescript.m:78:avgexcluded'
Rest Analysis/ripdescript.m:1:function out = ripdescript(index, excludeperiods, ripples, chinfo, varargin)
Rest Analysis/ripdescript.m:2:% out = ripdescript(index, excludeperiods, ripples, options)
Rest Analysis/ripdescript.m:5:interripwin = 0;  %eliminate ripples that occur in doublets or triplets
Rest Analysis/ripdescript.m:6:minstd = 5;
Rest Analysis/ripdescript.m:7:win = [.4 .4];   %to exclude rips too close to beginning
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*; sed -n 1,30p "Rest Analysis/runcalcriprates.m"; sed -n 30,104p "Rest Analysis/ripdescript.m"
```

```
% Construct filter
figopt=1;
clearvars -except figopt f

animals = {'Bones', 'Odo', 'Sulu', 'Worf', 'Beverly', 'Chakotay', 'Nerys',...
    'SevenOfNine', 'Rain', 'OBrien', 'Picard', 'Riker', 'Kes', 'Neelix', 'Quark',...
    'Sato', 'Garrett', 'Guinan', 'Keeler', 'Dax', 'TPol', 'Doctor', 'Tuvok', 'Bashir',...
    'Scotty'};

epochfilter = [];
epochfilter{1} = {'task','(contains(lower($env), ''veh'') && ~contains($descript,''FAIL'') && $dur==120)'};

datafilter = [];  %only works with single channel specified
datafilter{1} = {'chinfo','(isequal($area,''ca1'') && contains($layer,''pyr 1''))'};

timefilter = [];
timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'};

binrange = [5 50];
f = createfilter('animal', animals, 'epochs', epochfilter, 'data', datafilter, 'excludetime', timefilter);
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*/"Run Analysis"; cat comod.m; cat continuous_specgram.m; grep -n "velocity\|immob\|get2dstate\|timefilter\|tapers\|movingwin\|fpass\|log\|zscore\|mean(" run_continuous_specgram.m runcomod.m runcontMUA.m runcalccoherence.m runcalcRUNinstfreq.m runvelquant.m | head -60
```

```
function out = comod(index, excludetimes, eeg, varargin)
% how phase of theta modulates power of gamma
% based on dfakk_MI from kenny

%Defaults
srate = 1000;

% Define vector of frequencies whose amplitudes are modulated
% version 1: original
PhaseFreqVector=0:2:50;
AmpFreqVector=10:5:300;
PhaseFreq_BandWidth=4;
AmpFreq_BandWidth=10;

nbin = 18;

%Set options
for option = 1:2:length(varargin)-1
    if isstr(varargin{option})
        switch(varargin{option})
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*/"Run Analysis"; sed -n 1,40p runcomod.m; sed -n 200,262p runcomod.m; sed -n 180,222p run_continuous_specgram.m
```

```
clearvars -except f location

% pre-processing parameters
% version 2: low freq combination
PhaseFreqVector=0:.5:12;
AmpFreqVector=0:5:150;
PhaseFreq_BandWidth=0.5;
AmpFreq_BandWidth=5;

% version 3: single bands
% PhaseFreqVector=5;
% AmpFreqVector=20;
% PhaseFreq_BandWidth=6;
% AmpFreq_BandWidth=30;

% Animal
animals = {'Adobo_LT', 'Caraway_LT', 'Chives_LT', ...
    'Cinnamon_LT', 'Coriander_LT', 'Fenugreek_LT', 'GaramMasala_LT', 'Salt_LT', ...
    'Baharat_LT', 'Cardamom_LT', 'Jerk_LT', 'Mace_LT', 'Mustard_LT', ...
    'Tarragon_LT', 'Vanilla_LT',...
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000165/ | python -c "import json,sys; d=json.load(sys.stdin); print(d['draft_version']['name']); print(d.get('most_recent_published_version'))"; curl -s https://api.dandiarchive.org/api/dandisets/000165/versions/draft/info/ | python -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('description')); print(d.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  sed -n 2720,2890p paper/*.txt | tr '\n' ' ' | sed 's/  */ /g'; echo; sed -n 3327,3340p paper/*.txt; sed -n 4225,4235p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper and supplement are read. Checking the claims schema the checker expects before writing.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; grep -n "KEYS\|allowed\|'kind'\|\"kind\"\|data_values\|DATA" tools/claims_check.py tools/*.py | head -30
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

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
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
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));t=json.dumps(s,indent=1);print(t[5000:11000])"
```

```
`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     },
     "datasets": {
      "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
      "type": "array",
      "items": {
       "type": "string"
      },
      "minItems": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
[... 186 more lines not kept]
```

**Agent**

Writing the claims now: about 35 findings from Figures 2 to 6, S1 to S7 and Tables S1 to S6. First, two more code checks (the unpaired LMM, SWR frequency) and Table S4.

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*; sed -n 25,49p Statistics/calcunpairedLMM.m; grep -n "findpeaks\|diff\|1000\|instfreq\|threshtime\|starttime" "Rest Analysis/calcSWRinstfreq.m" | head -20; cd  sed -n 3340,3700p paper/*.txt | tr '\n' ' ' | sed 's/  */ /g' | head -c 4000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 4225,4583p paper/*.txt | tr '\n' ' ' | sed 's/  */ /g' | grep -o "SWR Size[^A-Z]*\|F test of the LMM[^.]*\.[^.]*\." | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 4225,4583p paper/*.txt | tr '\n' ' ' | sed 's/  */ /g' | grep -o "SWR Size.\{0,80\}"
```

Result: not kept, because it reads the paper's text.

**Agent**

Writing `claims/jones-2021.yaml`.

**Agent calls Write**

```json
{
 "file_path": "claims/jones-2021.yaml",
 "content": "# Claims for Aery Jones, Rao, Zilberter, ..., Huang & Frank (2021), Cell Reports 37, 110159,\n# tested on dandiset 000165.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC9069800, NIHMS1795940), full\n# text with STAR Methods and figure legends, and its main supplement PDF\n# (NIHMS1795940-supplement-Main_supplement.pdf: Figures S1 to S7 and Tables S1 to S6), as\n# stored under paper/. The version of record was not read. Supplementary Table S7 (an xlsx file,\n# effects stratified by sex) is not under paper/ and was not read; only the claim\n# sex-stratified-effects needs it.\n#\n# Code read: github.com/emilyasterjones/interneurons_modulate_drive, tag v1.0.0, commit 63b1acb\n# (archived as Zenodo doi:10.5281/zenodo.5618979), MATLAB. It holds preprocessing (ripple,\n# dentate spike and MUA extraction, position and velocity), rest analyses (ripple rates and\n# descriptors, SWR-triggered MUA, spectrograms, coherence, CSD, SW amplitude, instantaneous\n# frequency, dentate spikes), run analyses (continuous spectrograms, coherence, comodulation,\n# instantaneous frequency, MUA, velocity) and the statistics (calcLMM.m, calcjointLMM.m,\n# calcInteraction.m, calcunpairedLMM.m, HBcorrect.m, runcalcLMM_figs.m). It reads FilterFramework\n# data structures, not the NWB files.\n#\n# Data the paper used (STAR Methods, Method details; Figure legends). PV-Cre, SST-Cre and\n# PV-Cre/SST-Cre mice injected in the DG hilus with AAV5-hSyn-DIO-hM4D(Gi)-mCherry, or with an\n# empty mCherry vector, implanted in right dorsal hippocampus with a 32-site probe. Each mouse\n# had 6 daily sessions alternating vehicle and CNO (2 mg/kg i.p., 1 hour before recording).\n# Cohort 1 (5 PV-Cre, 4 SST-Cre; single-shank 32-site probe with 50 um spacing): home cage, used\n# only for CSD (Figure 2). Cohort 2 (9 PV-Cre, 10 SST-Cre, 6 PV-Cre/SST-Cre; 4-shank probe):\n# home cage (Figure 3). Cohort 3 (8 PV-Cre, 7 SST-Cre, 7 PV-Cre/SST-Cre, 8 empty vector): 30 min\n# linear track sessions (Figures 5, 6), then home cage sessions (Figure 3); 1 PV-Cre and 1\n# SST-Cre died before the home cage sessions. Rest analyses thus use 16 PV-Cre, 16 SST-Cre, 13\n# PV-Cre/SST-Cre and 8 empty vector mice; run analyses 8, 7, 7 and 8. The Methods (Surgery)\n# give the single-shank probe to cohort 3, while the Results and Figure 2A give it to the first,\n# CSD, cohort; the author identifies the probe from the data. Home cage sessions 60 min at 30\n# kHz; linear track sessions 30 min at 20 kHz; video at 30 frames/s. The deposit holds 0-300 Hz\n# LFP, MUA spike times, position, and electrode, mouse and session metadata (Data and Code\n# Availability). Measured variables are LFP and MUA per site in CA1 (pyr, sr, slm), CA3 (pyr,\n# sr) and DG (hilus, granule cell layer), and the mouse's velocity.\n#\n# Method M, shared by the LMM claims (every claim that says \"Method M\"). Each part is cited.\n#  - Periods. Rest is extended immobility, after the Gaussian-smoothed velocity has been below\n#    1 cm/s for 30 s or more (Methods, Analysis of neural data, paragraph 2; code\n#    runcalcriprates.m, get2dstate immobilecutoff 1 and immobilitytime > 30). Run is velocity\n#    above 1 cm/s (Methods, paragraph 7; code runcomod.m, $vel > 1).\n#  - Sites. SWRs detected on the CA1 site closest to the centre of the pyramidal layer; MUA on\n#    the site of the layer with the highest MUA (Methods, paragraphs 2 and 5). Rest SG power in\n#    CA1-sr, CA3 (pyr and sr) and DG (hilus and granule cell layer) (paragraph 3). Run features\n#    in CA1-pyr for the figures (Results, SG during movement, paragraph 1), CA3 (pyr and sr) and\n#    DG (hilus and granule cell layer) (Methods, paragraph 7); a region's value per time bin is\n#    the mean over its sites (code run_continuous_specgram.m, avgSGpwr).\n#  - Events and features as the Methods define them (Analysis of neural data, paragraphs 2 to\n#    7): ripple band 125-200 Hz, Hilbert envelope smoothed with a 4 ms Gaussian, above 3 SD for\n#    at least 15 ms; theta 5-11 Hz, SG 20-50 Hz, FG 50-110 Hz during run; multitaper\n#    spectrograms with a 1 s window during run (code continuous_specgram.m, tapers [3 5]);\n#    instantaneous frequency from interpeak times. The code also drops events within 0.4 s of\n#    the epoch edges and events also crossing 5 SD on 16 or more channels (getvalidrips.m),\n#    followed here as the Methods are silent. The code counts SWRs for rate, length and chains\n#    at 5 SD (runcalcriprates.m binrange [5 50]; runripdescript.m minstd 5) and for MUA at 3 SD\n#    (runRTMUA.m); the Methods say 3 SD, which is the main reading, and the code's 5 SD for\n#    rate, length and chains is a variant.\n#  - Data points of the model are events for SWR features, time bins for continuous measures\n#    (1 min for SWR rate, 100 ms for MUA, 1 s for all others) and peaks for continuous\n#    frequency (Quantification and statistical analysis, paragraph 2).\n#  - Treatment effect, per genotype. A linear mixed model fitted by maximum likelihood,\n#    feature ~ treatment + (treatment|animal), with an F test of the treatment fixed effect\n#    against the intercept-only model (paragraph 2; code calcLMM.m, fitlme and coefTest). The\n#    direction is the sign of the treatment coefficient (CNO minus vehicle).\n#  - Genotype difference (\"PV vs SST\"). Data of the two genotypes pooled; a likelihood ratio\n#    (chi-square) test of feature ~ treatment + (treatment|animal) against the model with\n#    genotype and treatment (paragraph 2; code calcjointLMM.m fits\n#    Measure~Genotype*Treatment+((Genotype*Treatment)|Animal), calcInteraction.m compare()).\n#  - Log transform, open. The Methods log-transform a feature when its errors are not Gaussian\n#    (they were right skewed); the code's figure script sets logtransform = 1 for every\n#    feature, shifting the data to a minimum of 0.001 when they reach 0 or below\n#    (runcalcLMM_figs.m, calcLMM.m). Readings (a) log for features whose residuals are right\n#    skewed, the rest untransformed (Methods, main); (b) log for all features (code). Both are\n#    run.\n#  - Significance. Holm-Bonferroni at alpha 0.05 across an experiment, defined as the 24 rest\n#    comparisons (Figures 2-4, S2-S3) or the 36 run comparisons (Figures 5, 6, S4-S5), within one\n#    genotype or within the between-genotype tests (Quantification, paragraph 3; code\n#    HBcorrect.m). When the full family is not computed, p < 0.05/24 (rest) or 0.05/36 (run)\n#    suffices for significance and p >= 0.05 for its absence, as both hold under Holm whatever\n#    the other p-values are. For Figures S6 and S7 the family is the same set of comparisons for\n#    the double-suppression and empty vector groups (code runcalcLMM_figs.m, Figures 6, S5\n#    section).\n#  - A claimed effect is reproduced when its direction matches and it is significant; a claimed\n#    absence (\"no change\", \"not CA1\") is reproduced when the same test is not significant,\n#    with its p-value and coefficient reported either way.\nschema_version: 2\npaper: doi:10.1016/j.celrep.2021.110159\nclaims:\n- id: fig1-tables1-expression\n  statement: hM4D expression is highly co-localized with PV and SST and extends throughout DG and\n    CA3, with no expression in CA1 or CA2.\n  source: Results, Recording in vivo hippocampal LFP, paragraph 1; Figure 1D, Figure S1A-C, Table S1\n  quote: HM4D expression was highly co-localized with PV and SST expression (Figure S1A–C and Table\n    S1) and extended throughout DG and CA3 from dorsal to ventral hippocampus, with no expression in\n    CA1 or CA2\n  criterion: Histological cell counts (Table S1) are not among the deposited data the paper lists\n    (Data and Code Availability). Where per-animal counts are available, reproduced when the\n    proportions in Table S1 are matched within 10% for each animal.\n- id: figs1ef-exvivo-cno\n  statement: In ex vivo slices CNO hyperpolarizes hM4D-expressing PV+ and SST+ interneurons by 8.6\n    +/- 1.3 mV and changes their input resistance by 31.3 +/- 9.9 MOhm.\n  source: Results, Recording in vivo hippocampal LFP, paragraph 1; Figure S1E-F\n  quote: hyperpolarized resting membrane potentials by 8.6 ± 1.3mV (Figure S1E), and decreased input\n    resistance by 31.3 ± 9.9 MΩ (Figure S1F)\n  statistics:\n  - about: membrane potential change\n    test: 1-sample t test\n    statistic: t(9)=6.57\n    p: 0.0001\n    n: 4 PV-Cre, 4 SST-Cre and 2 PV-Cre/SST-Cre slices\n  - about: input resistance change\n    test: 1-sample Wilcoxon test\n    statistic: W = -55\n    p: 0.002\n    n: 4 PV-Cre, 4 SST-Cre and 2 PV-Cre/SST-Cre slices\n  expected:\n  - quantity: hyperpolarization of resting membrane potential with CNO\n    value: 8.6\n    tolerance: 1.3\n    unit: mV\n  - quantity: magnitude of input resistance change with CNO\n    value: 31.3\n    tolerance: 9.9\n    unit: MOhm\n  criterion: Whole-cell patch-clamp recordings in slices, not among the deposited data. The sign of\n    the resistance change is open in the paper, where the Results say it decreased and the Figure\n    S1F legend says CNO \"increases input resistance\"; either sign matches. Tolerances are the\n    stated spread (mean +/- SEM).\n- id: fig2ef-csd-sr\n  statement: During SWRs, current source density sources and sinks in CA1 stratum radiatum increase\n    when either PV+ or SST+ interneurons are suppressed, with no difference between genotypes.\n  source: Figure 2E-F; Results, SWR signatures, paragraph 2\n  quote: During SWRs, CSD sources and sinks in stratum radiatum – the layer of CA3 input – increased\n    when either PV+ or SST+ interneurons were suppressed (Figure 2C–F)\n  statistics:\n  - about: peak source, PV-Cre treatment\n    test: F test of the LMM\n    p: 0.00062\n    n: 5 PV-Cre mice\n  - about: peak source, SST-Cre treatment\n    test: F test of the LMM\n    p: 4.64e-5\n    n: 4 SST-Cre mice\n  - about: peak source, PV vs SST\n    test: likelihood ratio test\n    p: 1\n  - about: peak sink, PV-Cre treatment\n    test: F test of the LMM\n    p: 0.00013\n    n: 5 PV-Cre mice\n  - about: peak sink, SST-Cre treatment\n    test: F test of the LMM\n    p: 1.24e-14\n    n: 4 SST-Cre mice\n  - about: peak sink, PV vs SST\n    test: likelihood ratio test\n    p: 1\n  criterion: Cohort 1 only. CSD as the second spatial derivative of the LFP after smoothing with a\n    triangular kernel; per SWR, the peak source and the peak sink in CA1-sr within the 100 ms after\n    SWR onset (Methods, Analysis of neural data, paragraph 4). The triangular kernel's width is\n    not given in the Methods; the code's RTCSD.m is followed. Method M. Reproduced when source\n    magnitude and sink magnitude each increase significantly with CNO in both genotypes and the\n    genotype test is not significant; partially reproduced when three of the four treatment\n    effects hold.\n- id: fig3b-mua-during-swr\n  statement: Suppressing either interneuron class increases the recruitment of DG and CA3 MUA to CA1\n    SWRs, but not of CA1 MUA.\n  source: Figure 3B; Results, SWR signatures, paragraph 2\n  quote: suppressing either class increased the extent to which DG and CA3, but not CA1, MUA\n    increased during SWRs (Figure 3B)\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.13\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.46\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00075\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.00076\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 5.5e-6\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 3.4e-5\n  criterion: 16 PV-Cre and 16 SST-Cre mice. Per SWR, the MUA rate between SWR start and end minus\n    the mean MUA rate over all immobility, divided by the SD of the immobility rate in 100 ms bins\n    (code RTMUA.m, normrate; the Methods do not define the normalization). Method M. Reproduced\n    when CA3 and DG increase significantly in both genotypes and CA1 does not change\n    significantly in either; partially reproduced when the CA3 and DG increases hold in one\n    genotype only.\n- id: fig3c-swr-rate-bidirectional\n  statement: Suppressing PV+ interneurons increases CA1 SWR rate while suppressing SST+ interneurons\n    decreases it, and the two effects differ significantly.\n  source: Figure 3C; Results, SWR signatures, paragraph 3\n  quote: Suppressing PV+ interneurons increased SWR rate while suppressing SST+ interneurons\n    decreased SWR rate, and these effects were significantly different between genotypes (Figure\n    3C)\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 1.9e-6\n    n: 16 PV-Cre mice\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 4.6e-5\n    n: 16 SST-Cre mice\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.00098\n  criterion: SWR counts per 1 min bin of immobility (code calcriprates2.m, timecounts). Method M.\n    Reproduced when the PV-Cre effect is a significant increase, the SST-Cre effect a significant\n    decrease and the genotype test significant; partially reproduced when the two significant\n    effects have opposite signs but one of the three tests fails.\n- id: fig3d-swr-chains\n  statement: Suppressing either interneuron class decreases the proportion of SWRs that occur in\n    chains (within 200 ms of another SWR).\n  source: Figure 3D; Results, SWR signatures, paragraph 3\n  quote: There was also a decrease in the proportion of SWRs that participated in chains (Figure 3D)\n    in both genotypes\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 0.001\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 2.5e-5\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.99\n  criterion: A SWR is in a chain when another SWR starts within 200 ms of its end (Methods,\n    paragraph 2; code ripdescript.m), intervals that run into an excluded period not counted.\n    Model data are SWR events with a 0 or 1 chain indicator (Quantification, events for SWRs).\n    Method M. Reproduced when both genotypes show a significant decrease.\n- id: fig3e-swr-length-sst\n  statement: Suppressing SST+ interneurons lengthens CA1 SWRs, an effect not seen with PV+\n    suppression, and the genotypes differ.\n  source: Figure 3E; Results, SWR signatures, paragraph 4\n  quote: SST+ interneuron suppression increased SWR length, an effect not seen following PV+\n    interneuron suppression (Figure 3E)\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 0.033\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 0.0023\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.00034\n  criterion: SWR length from detection start to end, per event (code ripdescript.m). Method M.\n    Reproduced when the SST-Cre effect is a significant increase, the PV-Cre effect not\n    significant after correction, and the genotype test significant. Partially reproduced when\n    the SST-Cre increase holds but one of the other two does not.\n- id: swr-longer-100ms-sst\n  statement: With SST+ suppression the percentage of SWRs longer than 100 ms rises from 38.5% under\n    vehicle to 49.6% under CNO.\n  source: Results, SWR signatures, paragraph 4\n  quote: 'found an increase when SST+ interneurons were suppressed (% of SWRs > 100 ms: vehicle 38.5%\n    vs CNO 49.6%, paired t test, t(15) = 3.67, p = 0.002)'\n  statistics:\n  - test: paired t test\n    statistic: t(15) = 3.67\n    p: 0.002\n    n: 16 SST-Cre mice\n  expected:\n  - quantity: SWRs longer than 100 ms, vehicle, SST-Cre\n    value: 38.5\n    tolerance: 3.85\n    unit: '%'\n  - quantity: SWRs longer than 100 ms, CNO, SST-Cre\n    value: 49.6\n    tolerance: 4.96\n    unit: '%'\n  criterion: Per mouse and treatment, the percentage of CA1 SWRs of 100 ms or longer, pooled over\n    that treatment's sessions; the group values are means over the 16 SST-Cre mice; a paired t\n    test across mice. The code computes the fraction per session with length >= 100 ms\n    (ripdescript.m, riplong), its denominator being all detected events of the session. Readings\n    of the denominator (a) the valid SWRs of Method M; (b) all detected events, as the code. And\n    of pooling (c) pooled over sessions; (d) mean of session fractions. Reproduced when under one\n    reading both values are within tolerance and the paired t test gives p < 0.05 with CNO higher.\n- id: fig3f-swr-frequency-pv\n  statement: PV+, but not SST+, interneuron suppression increases the instantaneous frequency of CA1\n    SWRs.\n  source: Figure 3F; Results, SWR signatures, paragraph 5\n  quote: PV+, but not SST+, interneuron suppression increased the instantaneous frequency of SWRs\n    (Figure 3F)\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 0.0012\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 0.033\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.018\n  criterion: Instantaneous frequency from the intervals between peaks of the ripple-filtered trace\n    within each SWR, averaged per SWR (code calcSWRinstfreq.m, avginstfreqs; Methods, paragraph\n    2). Readings of the model data (a) one mean per SWR (Quantification, events for SWRs); (b)\n    every interpeak value (code instfreqs). Method M. Reproduced when the PV-Cre effect is a\n    significant increase and the SST-Cre effect not significant after correction.\n- id: fig3g-sw-amplitude-pv\n  statement: PV+, but not SST+, suppression increases sharp-wave amplitude in CA1, and the genotypes\n    differ.\n  source: Figure 3G; Results, SWR signatures, paragraph 5\n  quote: PV+, but not SST+, interneuron suppression increased the instantaneous frequency of SWRs\n    (Figure 3F) and sharp-wave (SW) amplitude in CA1 (Figure 3G)\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 6.4e-27\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 0.25\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.005\n  criterion: SW amplitude is the maximum absolute value of the Hilbert envelope of the 0-30 Hz\n    filtered trace during each SWR (Methods, paragraph 2), on the CA1-sr site (code\n    runcalcSWamp.m chooses the site; the Methods do not name the layer). The data-point count\n    for this feature in Table S3 (df 381794 against 112503 for SWR events) suggests one value per\n    SWR and site; readings (a) one value per SWR at one CA1-sr site; (b) one value per SWR per\n    CA1-sr site. Method M. Reproduced when the PV-Cre increase is significant, the SST-Cre effect\n    is not, and the genotype test is significant.\n- id: figs2a-swr-size-pv\n  statement: SWR size is smaller when PV+ interneurons are suppressed, despite no change in CA1 MUA\n    recruitment.\n  source: Figure S2A; Results, SWR signatures, paragraph 5\n  quote: SWR size was smaller when PV+ interneurons were suppressed (Figure S2A) despite no change in\n    CA1 MUA recruitment\n  statistics:\n  - about: PV-Cre treatment\n    test: F test of the LMM\n    p: 0.00048\n  - about: SST-Cre treatment\n    test: F test of the LMM\n    p: 0.07\n  - about: PV vs SST\n    test: likelihood ratio test\n    p: 0.011\n  criterion: SWR size is the peak of the ripple envelope in SD above baseline per SWR (code\n    ripdescript.m, ripstds = maxthresh; Table S3 \"SWR Size (SD)\"). Method M. Reproduced when the\n    PV-Cre effect is a significant decrease.\n- id: tables2-fast-ripples-pv\n  statement: Suppressing PV+ interneurons modestly increases the incidence of rare fast ripples in\n    CA1 (0.0004 to 0.0035 Hz), with no change in SST-Cre mice.\n  source: Results, SWR signatures, paragraph 3; Table S2, Fast Ripple Rate\n  quote: we did detect a modest increase in the incidence of rare fast ripples when PV+\n    interneurons were suppressed (Table S2)\n  statistics:\n  - about: PV-Cre, vehicle against CNO\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 2.93\n    p: 0.003\n    n: 16 PV-Cre mice\n  - about: SST-Cre, vehicle against CNO\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 1.17\n    p: 0.2\n    n: 16 SST-Cre mice\n  expected:\n  - quantity: fast ripple rate, PV-Cre vehicle\n    value: 0.0004\n    tolerance: 0.00004\n    unit: Hz\n  - quantity: fast ripple rate, PV-Cre CNO\n    value: 0.0035\n    tolerance: 0.00035\n    unit: Hz\n  criterion: Fast ripples per the Methods (paragraph 5) data downsampled to 5 kHz, filtered 125-600\n    Hz, events where the smoothed envelope exceeds 3 SD for at least 3 oscillations, classed as\n    fast when their mean frequency is above 250 Hz; rate per mouse over immobility, per treatment\n    averaged over sessions; Wilcoxon matched pairs test across mice (Table S2 note). The paper's\n    test needs signal above 300 Hz. Reproduced when the PV-Cre rates are within tolerance and the\n    PV-Cre test gives p < 0.05 with CNO higher; partially reproduced when the test holds but the\n    rates are outside tolerance.\n- id: tables2-detection-unchanged\n  statement: The SWR rate changes are not due to differences in SWR detection (ripple band mean and\n    SD) or in baseline MUA, which do not change with treatment in either genotype.\n  source: Results, SWR signatures, paragraph 3; Table S2\n  quote: This effect was not due to differences in SWR detection or baseline MUA (Table S2)\n  statistics:\n  - about: ripple band mean, PV-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 1.6\n    p: 0.1\n  - about: ripple band mean, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 1.24\n    p: 0.2\n  - about: ripple band SD, PV-Cre\n    test: paired t test\n    statistic: t = 0.32, df 15\n    p: 0.8\n  - about: ripple band SD, SST-Cre\n    test: paired t test\n    statistic: t = 0.66, df 15\n    p: 0.5\n  - about: rest MUA, CA1-pyr, PV-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = -0.41\n    p: 0.68\n  - about: rest MUA, CA1-pyr, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = -0.16\n    p: 0.88\n  criterion: A claim of absence. Per mouse and treatment, the mean and SD of the CA1-pyr ripple-band\n    (125-200 Hz) envelope over immobility, and the MUA rate over immobility at CA1-pyr, CA3-pyr and\n    DG-gc, each averaged over the mouse's sessions of that treatment. The paper's test per Table\n    S2 is a paired t test when the data are normal by Shapiro-Wilk with similar variances by F\n    test, otherwise a Wilcoxon matched pairs signed rank test (Quantification, paragraph 2, given\n    there for Table S1), at p < 0.05. Reproduced when none of the ripple-band mean, ripple-band SD\n    and the three rest MUA tests is significant in either genotype; not reproduced when any is.\n- id: tables2-rest-sg-pv\n  statement: Suppressing PV+ interneurons raises SG power in CA1 across all rest and raises its\n    variance in CA1, CA3 and DG; suppressing SST+ interneurons does not change baseline SG power.\n  source: Results, SWR-coincident SG, paragraph 2; Table S2, Rest SG Freq. Mean and SD\n  quote: Following suppression of PV+ interneurons, SG power in CA1 was higher across all rest during\n    CNO epochs (Figure 4A) – consistent with increased CA3 drive (Kemere et al., 2013) – and had\n    higher variance in all 3 subregions (Table S3)\n  statistics:\n  - about: SG mean, CA1-sr, PV-Cre\n    test: paired t test\n    statistic: t = 4.03, df 15\n    p: 0.001\n  - about: SG SD, CA1-sr, PV-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 3.52\n    p: 0.0004\n  - about: SG SD, CA3, PV-Cre\n    test: paired t test\n    statistic: t = 3.94, df 15\n    p: 0.001\n  - about: SG SD, DG, PV-Cre\n    test: paired t test\n    statistic: t = 3.47, df 15\n    p: 0.003\n  - about: SG mean, CA1-sr, SST-Cre\n    test: paired t test\n    statistic: t = 1.8, df 15\n    p: 0.09\n  expected:\n  - quantity: CA1-sr rest SG mean, PV-Cre vehicle\n    value: 109.51\n    tolerance: 10.95\n    unit: uV2\n  - quantity: CA1-sr rest SG mean, PV-Cre CNO\n    value: 127.6\n    tolerance: 12.76\n    unit: uV2\n  criterion: The text cites Table S3 for the variance, but the numbers are in Table S2. Per mouse\n    and treatment, the mean and SD over immobility of SG-band (30-50 Hz) power in CA1-sr, CA3 and\n    DG, averaged over the mouse's sessions; paired t test or Wilcoxon test as in Table S2's note,\n    at p < 0.05. Which power the table means (the squared envelope of the 30-50 Hz filtered\n    signal, or multitaper band power) is open; readings (a) squared Hilbert envelope of the\n    SG-filtered trace (Methods, paragraph 3, z-scoring uses the \"SG filtered signal\"); (b)\n    multitaper band power. Reproduced when the PV-Cre CA1 mean rises and the SD rises in all\n    three regions, each at p < 0.05, and the SST-Cre CA1 mean does not change; the expected values\n    apply only to the reading whose units match.\n- id: fig4d-swr-sg-power-pv\n  statement: Suppressing PV+ interneurons increases SWR-coincident SG power in CA1, CA3 and DG,\n    while suppressing SST+ interneurons does not change it; the genotypes differ in CA1.\n  source: Figure 4D, Figure S2B; Results, SWR-coincident SG, paragraph 2\n  quote: Suppressing PV+ interneurons led to greater SWR-coincident SG power in CA1, CA3, and DG ...\n    as suppressing SST+ interneurons did not change SG power either at baseline (Table S2) or\n    during SWRs\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 1.7e-23\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.14\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 0.00099\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 2.0e-5\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.068\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 2.2e-5\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 0.0058\n  criterion: Per SWR and site, SWR-triggered multitaper spectrogram with a 100 ms window; SG power\n    is the mean z-scored power over 30-50 Hz in 0-100 ms after detection; for CNO epochs the\n    z-scoring uses the mean and SD of the SG-filtered signal from the vehicle epoch of the day\n    before (Methods, paragraph 3; Results, paragraph 2). For vehicle epochs the Methods do not\n    say; readings (a) their own mean and SD; (b) the code's (RTspecgram3.m). Regions CA1-sr, CA3,\n    DG. Method M. Reproduced when the PV-Cre increase is significant in all three regions, no\n    SST-Cre effect is significant, and the CA1 genotype test is significant; partially\n    reproduced when the CA1 parts hold.\n- id: fig4e-swr-sg-coherence-pv\n  statement: Only PV+ suppression enhances the increase in SG coherence between CA1 and CA3 and\n    between CA1 and DG during SWRs.\n  source: Figure 4E; Results, SWR-coincident SG, paragraph 2\n  quote: Similarly, only PV+ suppression enhanced the increase in SG coherence between CA1 and CA3 or\n    DG during SWRs, (Figure 4E)\n  statistics:\n  - about: CA1-CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.0011\n  - about: CA1-CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.17\n  - about: CA1-CA3, PV vs SST\n    test: likelihood ratio test\n    p: 9.4e-6\n  - about: CA1-DG, PV-Cre\n    test: F test of the LMM\n    p: 0.00097\n  - about: CA1-DG, SST-Cre\n    test: F test of the LMM\n    p: 0.43\n  - about: CA1-DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.0036\n  criterion: Per SWR and site pair, multitaper SG-band coherence in the 100 ms window after SWR onset\n    minus that in the 100 ms window starting 400 ms before onset, SWRs preceded by a SWR within\n    that window excluded (Methods, paragraph 3). Method M. Reproduced when both PV-Cre increases\n    are significant, neither SST-Cre effect is, and both genotype tests are significant;\n    partially reproduced when the PV-Cre increases hold.\n- id: figs2cd-sg-predicts-sw-frequency\n  statement: Across PV-Cre mice, the CNO-induced change in CA1 SWR-coincident SG power predicts the\n    change in SW amplitude and the change in SWR frequency.\n  source: Figure S2C-D; Results, SWR-coincident SG, paragraph 2\n  quote: the extent of CA1 SWR-coincident SG power increase correlated across animals with the\n    extent of SW amplitude increase and the extent of SWR frequency increase (Figure S3C–D)\n  statistics:\n  - about: SG power change against SW amplitude change\n    test: Pearson correlation\n    statistic: F(1,14) = 17.29\n    p: 0.001\n    n: 16 PV-Cre mice\n  - about: SG power change against SWR frequency change\n    test: Pearson correlation\n    statistic: F(1,14) = 10.97\n    p: 0.0051\n    n: 16 PV-Cre mice\n  criterion: The text cites Figure S3C-D, but the panels are Figure S2C-D. Per PV-Cre mouse, the\n    change CNO minus vehicle of each feature; Pearson correlation across the 16 mice. What a\n    mouse's change is, is open; readings (a) difference of the mouse's means over SWRs; (b)\n    difference of the LMM fitted conditional responses (code calcLMM.m, cnocoeff - vehcoeff, as\n    plotted in Figures S6-S7). Reproduced when under one reading both correlations are positive\n    with p < 0.05.\n- id: ca3-swr-overlap\n  statement: Only a subset of CA3 SWRs, 37.18% averaged over vehicle sessions of PV-Cre and SST-Cre\n    mice, overlap in time with CA1 SWRs.\n  source: Results, local CA3 SWRs and DG spikes, paragraph 1\n  quote: only a subset of CA3 SWRs overlapped in time with CA1 SWRs (37.18%, averaged over all PV-Cre\n    and SST-Cre vehicle sessions)\n  expected:\n    quantity: CA3 SWRs overlapping a CA1 SWR\n    value: 37.18\n    tolerance: 3.72\n    unit: '%'\n  criterion: CA3 SWRs detected on the CA3 site closest to the centre of the pyramidal layer as for\n    CA1 (Methods, paragraph 2); a CA3 SWR overlaps when a valid CA1 SWR midpoint falls within its\n    start and end (code ripdescript.m, probecrit branch). Readings of the average (a) mean over\n    sessions; (b) pooled over all events. Reproduced when one is within tolerance.\n- id: figs3-ca3-swr-pv\n  statement: Suppressing either class increases CA3 MUA recruitment to CA3 SWRs and lengthens CA3\n    SWRs; PV+ suppression decreases CA3 SWR rate and CA3 SWR instantaneous frequency.\n  source: Figure S3B-E; Results, local CA3 SWRs and DG spikes, paragraphs 1-2\n  quote: Suppressing PV+ interneurons decreased CA3 SWR rate, while suppressing SST+ interneurons\n    increased CA3 SWR rate (Figure S3C) ... Suppression of either interneuron type increased CA3\n    SWR length (Figure S3D). Finally, PV+ interneuron suppression decreased CA3 SWR instantaneous\n    frequency (Figure S3E)\n  statistics:\n  - about: CA3 MUA to CA3 SWRs, PV-Cre\n    test: F test of the LMM\n    p: 0.00044\n  - about: CA3 MUA to CA3 SWRs, SST-Cre\n    test: F test of the LMM\n    p: 0.0062\n  - about: CA3 SWR rate, PV-Cre\n    test: F test of the LMM\n    p: 0.00072\n  - about: CA3 SWR length, PV-Cre\n    test: F test of the LMM\n    p: 7.14e-6\n  - about: CA3 SWR length, SST-Cre\n    test: F test of the LMM\n    p: 0.0055\n  - about: CA3 SWR instantaneous frequency, PV-Cre\n    test: F test of the LMM\n    p: 0.00057\n  criterion: CA3 SWRs detected on the CA3 pyramidal-layer site, features as for CA1 SWRs (Methods,\n    paragraph 2); Method M. Reproduced when the five stated effects (MUA up in both, length up in\n    both, PV-Cre rate down, PV-Cre frequency down; six tests) all hold; partially reproduced when\n    at least four of the six do. The SST-Cre increase in CA3 SWR rate is a separate claim.\n- id: figs3c-ca3-swr-rate-sst\n  statement: Suppressing SST+ interneurons increases CA3 SWR rate.\n  source: Results, local CA3 SWRs and DG spikes, paragraph 2; Figure S3C\n  quote: while suppressing SST+ interneurons increased CA3 SWR rate (Figure S3C)\n  statistics:\n  - about: CA3 SWR rate, SST-Cre\n    test: F test of the LMM\n    p: 0.77\n  - about: CA3 SWR rate, PV vs SST\n    test: likelihood ratio test\n    p: 0.28\n  criterion: The text states an increase, but the legend gives p = 0.77 for the SST-Cre effect,\n    which is not significant. Judged as the text states it. CA3 SWR rate per 1 min bin of\n    immobility; Method M. Reproduced when the SST-Cre effect is a significant increase; the\n    coefficient and p-value are reported either way.\n- id: figs3-dentate-spikes\n  statement: DG MUA during dentate spikes does not change; suppressing either class decreases\n    dentate spike rate; PV+ suppression increases dentate spike length and decreases their\n    amplitude, while SST+ suppression has no detectable effect on these.\n  source: Figure S3F-I; Results, local CA3 SWRs and DG spikes, paragraph 3\n  quote: Instead, DS MUA did not change (Figure S3F) ... Suppression of either PV+ or SST+\n    interneurons decreased DS rate (Figure S3G) ... Suppressing PV+ interneurons also increased DS\n    length while decreasing DS amplitude, while suppressing SST+ interneurons had no detectable\n    effect on these features\n  statistics:\n  - about: DS MUA, PV-Cre\n    test: F test of the LMM\n    p: 0.47\n  - about: DS MUA, SST-Cre\n    test: F test of the LMM\n    p: 0.26\n  - about: DS rate, PV-Cre\n    test: F test of the LMM\n    p: 3.0e-19\n  - about: DS rate, SST-Cre\n    test: F test of the LMM\n    p: 0.0027\n  - about: DS length, PV-Cre\n    test: F test of the LMM\n    p: 2.6e-11\n  - about: DS length, SST-Cre\n    test: F test of the LMM\n    p: 0.26\n  - about: DS amplitude, PV-Cre\n    test: F test of the LMM\n    p: 1.6e-7\n  - about: DS amplitude, SST-Cre\n    test: F test of the LMM\n    p: 0.044\n  criterion: Dentate spikes at the DG site with the highest MUA, during immobility; LFP filtered\n    5-100 Hz and z-scored, peaks detected; amplitude from peak to nearest minimum, length between\n    the minima around the peak; log amplitudes z-scored; kept when amplitude > 0.75 and duration\n    5-25 ms (Methods, paragraph 6). Rate per 1 min bin. Method M. Reproduced when all ten parts\n    (two absences of MUA change, two rate decreases, PV-Cre length up and amplitude down, SST-Cre\n    length and amplitude unchanged) hold; partially reproduced when the rate decreases and the\n    PV-Cre length and amplitude effects hold.\n- id: fig5b-mua-run\n  statement: During movement, suppressing either class increases MUA in DG and CA3 but not in CA1.\n  source: Figure 5B; Results, SG during movement, paragraph 2\n  quote: suppressing either class increased MUA during movement in DG and CA3, but not CA1 (Figure\n    5B)\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.72\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.9\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00051\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.005\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.00022\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 0.0063\n  criterion: Cohort 3 linear track sessions, 8 PV-Cre and 7 SST-Cre. MUA rate in 100 ms bins during\n    run at the highest-MUA site of each region (code contMUA.m; Methods, paragraph 5). Method M\n    (run family). Reproduced when CA3 and DG increase significantly in both genotypes and CA1 does\n    not change in either; partially reproduced when the increases hold in one genotype.\n- id: fig5d-sg-power-run\n  statement: During movement, suppressing PV+ interneurons amplifies SG power in CA1 with no effect\n    in DG and CA3, while suppressing SST+ interneurons dampens SG power in DG and CA3 with no effect\n    in CA1; all these effects differ between genotypes.\n  source: Figure 5D, Figure S4A; Results, SG during movement, paragraph 3\n  quote: Suppressing PV+ interneurons in DG and CA3 amplified SG power in CA1, but there was no\n    detectable effect following suppression of SST+ interneurons. By contrast, suppressing PV+\n    interneurons had no detectable effect on SG power in DG and CA3, while suppressing SST+\n    interneurons dampened SG power locally in DG and CA3\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 2.6e-6\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.13\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 4.7e-6\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.15\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 5.2e-5\n  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.00088\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.5\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 1.3e-7\n  - about: DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.00042\n  criterion: SG power (20-50 Hz) per 1 s bin of run from the multitaper spectrogram (1 s window,\n    tapers [3 5], code continuous_specgram.m), mean over the band and over the region's sites.\n    Method M (run family). Reproduced when all nine tests come out as stated (three significant\n    changes in the stated directions, three absences, three significant genotype tests);\n    partially reproduced when the CA1 PV-Cre increase and the DG and CA3 SST-Cre decreases hold.\n- id: fig5e-sg-coherence-run\n  statement: During movement, suppressing PV+ interneurons enhances SG coherence between CA1 and CA3.\n  source: Figure 5E; Results, SG during movement, paragraph 3\n  quote: Relatedly, suppressing PV+ interneurons enhanced SG coherence between CA1 and CA3 (Figure\n    5E)\n  statistics:\n  - about: CA1-CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00028\n  - about: CA1-CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.6\n  - about: CA1-CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.56\n  criterion: Multitaper SG-band coherence between CA1-pyr and CA3 sites during run (Methods,\n    paragraph 7, \"over all run periods\"); model data in 1 s bins (Quantification, paragraph 2).\n    The two passages differ on the bins; readings (a) coherence per 1 s bin; (b) per site pair and\n    session over all run periods (code calccoherence.m decides). Method M (run family). Reproduced\n    when the PV-Cre CA1-CA3 increase is significant.\n- id: fig5f-sg-frequency-pv\n  statement: Suppressing PV+, but not SST+, interneurons reduces SG frequency during movement in\n    CA1, CA3 and DG, and the genotypes differ.\n  source: Figure 5F, Figure S4B; Results, SG during movement, paragraph 3\n  quote: suppressing PV+ interneurons, but not SST+ interneurons, reduced SG frequency throughout the\n    hippocampus (Figure 5F and S4B)\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 2.5e-6\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.56\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 0.0061\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00023\n  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.0025\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.0005\n  - about: DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.00015\n  criterion: Instantaneous frequency from interpeak times of the 20-50 Hz filtered trace during run,\n    one data point per peak (Methods, paragraph 7; Quantification). Method M (run family).\n    Reproduced when the PV-Cre decrease is significant in all three regions and no SST-Cre effect\n    is; partially reproduced when it holds in CA1 only.\n- id: fig5g-sg-theta-modulation\n  statement: Suppressing PV+ interneurons increases theta modulation of SG locally in DG and CA3 but\n    not in CA1, while suppressing SST+ interneurons reduces theta modulation of SG in CA1.\n  source: Figure 5G, Figure S4C; Results, SG during movement, paragraph 3\n  quote: suppressing PV+ interneurons increased theta modulation of SG only locally in DG and CA3,\n    while suppressing SST+ interneurons reduced theta modulation of SG in CA1, and these effects\n    were again detectably different between genotypes\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.12\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.00082\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 0.95\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.0011\n  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.0049\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.0003\n  - about: DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.0054\n  criterion: Theta modulation of SG is the modulation index of the code's comod.m (normalized entropy\n    of mean SG amplitude over theta phase bins, 2 x 18 - 1 = 35 bins), computed per 1 s bin of run,\n    phase band 5-11 Hz and amplitude band 20-50 Hz (the code's single-band setting in runcomod.m;\n    Methods band definitions). Method M (run family). Reproduced when the PV-Cre increases in CA3\n    and DG and the SST-Cre decrease in CA1 are significant and the PV-Cre CA1 effect is not;\n    partially reproduced when two of the three significant effects hold. The genotype tests are\n    reported; the legend's CA1 value (p = 0.95) does not support a difference there.\n- id: fig6b-fg-power-sst\n  statement: Suppressing SST+ interneurons amplifies FG power in CA1 and DG during movement, an\n    effect specific to this class.\n  source: Figure 6B, Figure S4D; Results, FG during movement, paragraph 2\n  quote: Suppressing SST+ interneurons amplified FG power in CA1 and DG, an effect specific to this\n    interneuron class (Figure 6A–B and S5D)\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.27\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 3.3e-5\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 0.00054\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.81\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 1.9e-5\n  - about: DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.0025\n  criterion: The text cites Figure S5D; the DG panel is Figure S4D. FG power (50-110 Hz) per 1 s\n    bin of run as for SG (fig5d-sg-power-run). Method M (run family). Reproduced when the SST-Cre\n    increase is significant in CA1 and DG, the PV-Cre effect is not, and both genotype tests are\n    significant; partially reproduced when the CA1 parts hold.\n- id: figs4e-sg-fg-inverse\n  statement: In DG and CA3 of SST-Cre mice, the CNO-induced change in SG power predicts the change in\n    FG power, animals with the greatest SG suppression showing the greatest FG enhancement.\n  source: Figure S4E; Results, FG during movement, paragraph 2\n  quote: locally in DG and CA3, SG and FG showed an inverse relationship, where animals with the\n    greatest SG suppression showed the greatest FG enhancement and vice versa (Figure S4E)\n  statistics:\n  - about: CA3\n    test: Pearson correlation\n    statistic: F(1,5) = 20.7\n    p: 0.0061\n    n: 7 SST-Cre mice\n  - about: DG\n    test: Pearson correlation\n    statistic: F(1,5) = 26\n    p: 0.0038\n    n: 7 SST-Cre mice\n  criterion: Per SST-Cre mouse (7, linear track), the change CNO minus vehicle of SG power and of FG\n    power in CA3 and in DG; Pearson correlation across mice. Readings of a mouse's change as in\n    figs2cd-sg-predicts-sw-frequency (a) difference of means; (b) difference of the LMM fitted\n    conditional responses. Reproduced when under one reading both correlations are negative with\n    p < 0.05.\n- id: fig6e-sg-fg-ratio\n  statement: SST+ suppression decreases the SG/FG power ratio in CA1, PV+ suppression increases it\n    throughout the hippocampus, and these effects differ between genotypes across the hippocampus.\n  source: Figure 6E, Figure S4F; Results, FG during movement, paragraph 2\n  quote: these bidirectional changes in SG and FG power led to decreased SG/FG power ratios in CA1\n    following SST+ suppression and increased SG/FG power ratios throughout the hippocampus following\n    PV+ suppression. These SG/FG ratio effects were significantly different between genotypes\n    across the hippocampus\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 9.7e-25\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 0.00013\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 7.4e-6\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00036\n  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.002\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.00031\n  - about: DG, PV vs SST\n    test: likelihood ratio test\n    p: 0.00064\n  criterion: Per 1 s bin of run, SG power over FG power, from the band powers of fig5d-sg-power-run\n    (code run_continuous_specgram.m, allSGFGratio, per site; Figure 6C-D averaged over CA1-pyr\n    sites). Method M (run family). Reproduced when the SST-Cre CA1 decrease, the PV-Cre increases\n    in CA1, CA3 and DG, and the three genotype tests are all significant; partially reproduced\n    when the CA1 parts hold.\n- id: fig6f-fg-coherence-unchanged\n  statement: FG coherence between CA1 and CA3 and between CA1 and DG does not change with either\n    suppression.\n  source: Figure 6F; Results, FG during movement, paragraph 2\n  quote: FG coherence, however, did not change (Figure 6F)\n  statistics:\n  - about: CA1-CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.83\n  - about: CA1-CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.2\n  - about: CA1-DG, PV-Cre\n    test: F test of the LMM\n    p: 0.27\n  - about: CA1-DG, SST-Cre\n    test: F test of the LMM\n    p: 0.076\n  criterion: A claim of absence. FG-band coherence as for SG (fig5e-sg-coherence-run, same two\n    readings of the bins). Method M (run family) with its Holm-Bonferroni threshold. Reproduced\n    when none of the four treatment effects is significant; not reproduced when any is.\n- id: fig6g-fg-frequency-sst\n  statement: Suppressing SST+ interneurons increases FG frequency throughout the hippocampus.\n  source: Figure 6G, Figure S4G; Results, FG during movement, paragraph 2\n  quote: suppressing SST+ interneurons increased FG frequency throughout the hippocampus (Figure 6G\n    and S4G)\n  statistics:\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 4.3e-17\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 2.6e-9\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 4.1e-11\n  criterion: Instantaneous frequency of the 50-110 Hz filtered trace from interpeak times, one point\n    per peak (Methods, paragraph 7). Method M (run family). Reproduced when the SST-Cre increase is\n    significant in CA1, CA3 and DG; partially reproduced in one or two regions.\n- id: fig6h-fg-theta-modulation-sst\n  statement: Suppressing SST+ interneurons increases theta modulation of FG in CA1, an effect\n    specific to SST+ interneurons.\n  source: Figure 6H-J; Results, FG during movement, paragraph 2\n  quote: suppressing SST+ interneurons increased theta modulation of FG in CA1 (Figure 6H–J and\n    S4H), an effect specific to SST+ interneurons\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.0098\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 8.0e-20\n  - about: CA1, PV vs SST\n    test: likelihood ratio test\n    p: 0.0001\n  criterion: Modulation index as in fig5g-sg-theta-modulation, amplitude band 50-110 Hz (the Methods'\n    FG band; the code's single-band setting in runcomod.m shows the SG band only). Method M (run\n    family). Reproduced when the SST-Cre CA1 increase and the genotype test are significant. The\n    PV-Cre effect (p = 0.0098 in the legend; the Discussion says FG had \"reduced modulation by\n    theta\" with PV+ suppression) is reported with its sign.\n- id: figs5-theta-power-ca1\n  statement: Suppressing either PV+ or SST+ interneurons increases theta power in CA1 but not in CA3\n    or DG during movement.\n  source: Figure S5B; Results, theta during movement, paragraph 1\n  quote: Contrary to our hypothesis, suppressing either PV+ or SST+ interneurons increased theta\n    power in CA1 but not elsewhere (Figure S5A–B)\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.00032\n  - about: CA1, SST-Cre\n    test: F test of the LMM\n    p: 4.2e-5\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.81\n  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.13\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.12\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 0.0097\n  criterion: Theta (5-11 Hz) power per 1 s bin of run, as for SG power. Method M (run family).\n    Reproduced when both CA1 increases are significant and none of the four CA3 and DG effects is\n    significant after correction; partially reproduced when the CA1 increases hold.\n- id: figs5-theta-coherence-frequency\n  statement: Neither interneuron type modifies theta coherence or theta frequency, except for an\n    increase in theta frequency in DG of PV-Cre mice.\n  source: Figure S5C-D; Results, theta during movement, paragraph 1\n  quote: Neither interneuron type modified theta coherence (Figure S5C) or theta frequency (Figure\n    S5D) save for an increase in theta frequency in PV-Cre mice in DG\n  statistics:\n  - about: theta frequency, DG, PV-Cre\n    test: F test of the LMM\n    p: 0.00061\n  - about: theta frequency, CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.0082\n  - about: theta frequency, CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.0077\n  - about: theta coherence, CA1-CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.047\n  - about: theta coherence, CA1-DG, PV-Cre\n    test: F test of the LMM\n    p: 0.024\n  criterion: Theta coherence and instantaneous frequency as for SG (fig5e, fig5f). Method M (run\n    family). Reproduced when the PV-Cre DG theta frequency increase is significant and none of\n    the other ten tests (two coherences and three frequencies in each genotype, less the one) is;\n    not reproduced when any other is significant. The effect sizes are reported.\n- id: figs6-double-like-pv\n  statement: Suppressing both PV+ and SST+ interneurons cannot be told apart from suppressing PV+\n    interneurons only, except for theta modulation of SG in DG and CA3, which double suppression\n    decreases.\n  source: Figures S6 and S7, Table S5; Results, suppressing both, paragraph 1\n  quote: we were unable to detect a difference between suppressing both interneuron types and\n    suppressing PV+ interneurons only except in the case of comodulation of SG by theta in DG and\n    CA3. In this instance, suppressing both interneuron types decreased theta modulation of SG, an\n    effect not observed when suppressing either type alone\n  statistics:\n  - about: theta modulation of SG, CA3, PV vs P/S\n    test: likelihood ratio test\n    p: 7.3e-5\n  - about: theta modulation of SG, DG, PV vs P/S\n    test: likelihood ratio test\n    p: 0.00018\n  criterion: 13 PV-Cre/SST-Cre mice at rest and 7 on the track, against the PV-Cre mice. For every\n    feature of Figures S6 and S7, the genotype test (PV vs P/S) of Method M, Holm-Bonferroni over\n    the experiment's comparisons. Reproduced when the CA3 and DG theta-SG modulation tests are\n    significant with P/S decreasing, and no other PV vs P/S test is significant; partially\n    reproduced when the exceptions hold and at most two other features differ. Each feature's\n    result is listed.\n- id: figs6-double-unlike-sst\n  statement: Suppressing both interneuron types has largely distinct effects from suppressing SST+\n    interneurons only; the exceptions are FG frequency and CA1 FG power, which follow the direction\n    of SST+ suppression.\n  source: Figures S6 and S7, Table S5; Results, suppressing both, paragraph 1\n  quote: In contrast, suppressing both interneuron types had largely distinct effects from\n    suppressing SST+ interneurons only. The exceptions were FG frequency and CA1 FG power, in which\n    case suppressing both interneuron types followed the direction of suppressing SST+ interneurons\n    alone\n  statistics:\n  - about: SWR rate, SST vs P/S\n    test: likelihood ratio test\n    p: 0.021\n  - about: SWR instantaneous frequency, SST vs P/S\n    test: likelihood ratio test\n    p: 0.0017\n  - about: SW amplitude, SST vs P/S\n    test: likelihood ratio test\n    p: 0.00055\n  - about: CA1 SG power during SWRs, SST vs P/S\n    test: likelihood ratio test\n    p: 0.00089\n  - about: CA1 FG power, P/S treatment\n    test: F test of the LMM\n    p: 1.6e-6\n  - about: CA1 FG power, SST vs P/S\n    test: likelihood ratio test\n    p: 1\n  - about: CA1 FG frequency, P/S treatment\n    test: F test of the LMM\n    p: 0.00012\n  criterion: '\"Largely distinct\" is not given a count. For every feature of Figures S6 and S7, the\n    SST vs P/S genotype test of Method M. Reproduced when the CA1 FG power and FG frequency effects\n    of double suppression are significant increases (the direction of SST+ suppression) and at\n    least half of the features where SST-Cre and P/S treatment effects differ in sign or\n    significance show a significant SST vs P/S test; partially reproduced when the FG exceptions\n    hold but fewer features differ.'\n- id: figs6-empty-vector-control\n  statement: In mice injected with an empty vector, CNO and vehicle epochs do not differ.\n  source: Figures S6 and S7, Table S5; Results, consistency, paragraph 2\n  quote: we treated mice injected with an empty vector as a control and observed no differences\n    between vehicle and CNO treated epochs (Figure S5 and S6 and Table S5)\n  criterion: A claim of absence. 8 empty vector mice, rest and track. For every feature of Figures\n    S6 and S7 (legend p-values for EV range from 0.062 to 1), the treatment test of Method M with\n    Holm-Bonferroni over the experiment's comparisons. Reproduced when no feature is significant;\n    not reproduced when any is, with the features and effect sizes listed.\n- id: running-speed-unchanged\n  statement: Running speed does not differ between vehicle and CNO sessions (4.8 against 5.1 cm/s).\n  source: Results, consistency, paragraph 2\n  quote: differences in LFP during movement were not due to differences in running speed (vehicle\n    4.8 cm/s vs CNO 5.1 cm/s, paired t test, t(29) = 1.31, p = 0.2)\n  statistics:\n  - test: paired t test\n    statistic: t(29) = 1.31\n    p: 0.2\n    n: 30 mice on the linear track\n  expected:\n  - quantity: running speed, vehicle\n    value: 4.8\n    tolerance: 0.48\n    unit: cm/s\n  - quantity: running speed, CNO\n    value: 5.1\n    tolerance: 0.51\n    unit: cm/s\n  criterion: A claim of absence, judged on a paired t test across the 30 track mice (8 PV-Cre, 7\n    SST-Cre, 7 PV-Cre/SST-Cre, 8 empty vector) of each mouse's mean speed per treatment, at p <\n    0.05. Which samples form the mean is open; readings (a) Gaussian-smoothed velocity over run\n    periods (above 1 cm/s); (b) over the whole session. Reproduced when the test is not\n    significant; the values are compared with tolerance under each reading.\n- id: tables4-genotype-baseline\n  statement: During vehicle treatment, PV-Cre mice differ from SST-Cre mice in DG and CA3 SG\n    frequency (lower) and SG/FG ratios (higher).\n  source: Results, consistency, paragraph 2; Table S4\n  quote: We did note, however, that PV-Cre had different DG and CA3 SG frequencies and SG/FG ratios\n    from SST-Cre mice during vehicle treatment (Table S4)\n  statistics:\n  - about: CA3 SG frequency\n    test: F test of the LMM for genotype effects\n    p: 0.00042\n  - about: DG SG frequency\n    test: F test of the LMM for genotype effects\n    p: 0.00025\n  - about: CA3 SG/FG ratio\n    test: F test of the LMM for genotype effects\n    p: 0.00078\n  - about: DG SG/FG ratio\n    test: F test of the LMM for genotype effects\n    p: 0.00071\n  expected:\n  - quantity: CA3 SG frequency, PV-Cre vehicle\n    value: 40.54\n    tolerance: 4.05\n    unit: Hz\n  - quantity: CA3 SG frequency, SST-Cre vehicle\n    value: 41.9\n    tolerance: 4.19\n    unit: Hz\n  - quantity: DG SG frequency, PV-Cre vehicle\n    value: 41.06\n    tolerance: 4.11\n    unit: Hz\n  - quantity: DG SG frequency, SST-Cre vehicle\n    value: 42.4\n    tolerance: 4.24\n    unit: Hz\n  - quantity: CA3 SG/FG ratio, PV-Cre vehicle\n    value: 6.2\n    tolerance: 0.62\n  - quantity: CA3 SG/FG ratio, SST-Cre vehicle\n    value: 3.99\n    tolerance: 0.4\n  - quantity: DG SG/FG ratio, PV-Cre vehicle\n    value: 5.16\n    tolerance: 0.52\n  - quantity: DG SG/FG ratio, SST-Cre vehicle\n    value: 3.4\n    tolerance: 0.34\n  criterion: Vehicle sessions of 8 PV-Cre and 7 SST-Cre track mice; features as in fig5f and fig6e;\n    the group mean is the mean over mice of each mouse's mean (code runcalcLMM_figs.m, Table S3\n    section). The genotype test is an LMM feature ~ group + (group|animal) with an F test\n    (Quantification, paragraph 2; code calcunpairedLMM.m), Holm-Bonferroni over the run features.\n    Reproduced when the four tests are significant in the stated directions; the mean values are\n    compared with tolerance (the 10% tolerance on frequency is wide against a 1.4 Hz difference,\n    so the direction and test decide).\n- id: tables6-sex-swr-size\n  statement: During vehicle treatment, females have slightly larger SWR sizes than males, with no\n    other sex differences.\n  source: Results, consistency, paragraph 1; Table S6\n  quote: Females had slightly larger SWR sizes than males during vehicle treatment epochs (Table S6),\n    but there were otherwise no sex differences\n  statistics:\n  - about: SWR size, females against males\n    test: F test of the LMM for sex effects\n    p: 0.0046\n    n: 26 females and 27 males\n  expected:\n  - quantity: SWR size, females, vehicle\n    value: 6.36\n    tolerance: 0.64\n    unit: SD\n  - quantity: SWR size, males, vehicle\n    value: 5.92\n    tolerance: 0.59\n    unit: SD\n  criterion: All mice of cohorts 2 and 3 (vehicle epochs; cohort 1 left out, Methods, Method\n    details), sex from the subject metadata. For every feature of Table S6, an LMM feature ~ sex +\n    (sex|animal) with an F test (Quantification, paragraph 2; code calcunpairedLMM.m),\n    Holm-Bonferroni over the experiment's features. Reproduced when SWR size is significantly\n    larger in females and no other feature differs significantly by sex; partially reproduced\n    when SWR size holds and one or two other features differ.\n- id: sex-stratified-effects\n  statement: Interneuron suppression has effects of the same direction and magnitude in both sexes\n    on most features; the exceptions are SW amplitude with SST+ suppression (down in females, up in\n    males), FG power with SST+ suppression (larger rise in females), and DG and CA3 MUA during\n    movement (larger rise in females with suppression of either or both classes).\n  source: Results, consistency, paragraph 1; Table S7\n  quote: The effect of suppressing interneurons was in the same direction and magnitude in both sexes\n    on most features (Table S7) with a few exceptions. Suppressing SST+ interneurons decreased SW\n    amplitude in females but had the opposite effect in males, leading to no effect overall, and\n    enhanced FG power to a greater degree in females than in males. Interestingly, suppressing\n    either or both interneuron classes led to a greater increase in DG and CA3 MUA during movement\n    in females\n  criterion: Table S7 (xlsx) was not available to the reader; its p-values and the features it\n    covers are not recorded here. Per genotype, the likelihood ratio test of feature ~ treatment +\n    (treatment|animal) against feature ~ treatment:sex + (treatment:sex|animal) (Quantification,\n    paragraph 2; code runcalcLMM_figs.m Table S6 section, calcInteraction.m on males and\n    females), Holm-Bonferroni per genotype over the features. Reproduced when the named exceptions\n    have a significant sex interaction with the stated signs (females larger, or opposite signs\n    for SST-Cre SW amplitude) and at most a few other features do; the count of other significant\n    interactions is reported. \"FG power\" is read as CA1 FG power, the paper's main FG power\n    feature; CA3 and DG are shown as variants.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/jones-2021.yaml paper/10.1016-j.celrep.2021.110159.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. Checking the style rules (no em dashes, no "rather").

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/jones-2021.yaml; git status --short claims/
```

```
?? claims/jones-2021.yaml
```

**Agent**

Two criteria point to code I hadn't opened (the CSD kernel in RTCSD.m, and the vehicle z-scoring in RTspecgram3.m). Checking them.

**Agent calls Bash**

```bash
cd "$TMPDIR"/code/emil*/"Rest Analysis"; grep -n "triang\|conv\|smooth\|kernel\|diff(" RTCSD.m | head; grep -n "mean\|std\|zscore\|baseline\|veh" RTspecgram3.m | head -20
```

```
48:%smoothing via triangular kernel
50:    %smoothing via triangular kernel
54:    smooth_eeg{i}.data = (a+2*b+c)/4;
59:    %smoothing via triangular kernel
60:    b = smooth_eeg{i}.data;
61:    a = smooth_eeg{i-1}.data;
62:    c = smooth_eeg{i+1}.data;
38:minstd = 5;    %can change minstd!!
54:            case 'minstd'
55:                minstd = varargin{option+1};
80:%get valid times for calculation of baseline pwrspectra for zscoring
91:    [valid, excluded] = getvalidrips(ripples,index,trigindex, excludeperiods, win, minstd, interripwin);
92:    %[valid, excluded] = getnoiserips(ripples,index,trigindex, excludeperiods, win, minstd, interripwin);
94:    ripplestdout = r.maxthresh(valid);
111:        % Compute a z-scored spectrogram using the mean and std for the entire
114:        meanPtrig = mean(Ptrig);
115:        stdPtrig = std(Ptrig);
119:                Strig(i,:,j) = (Strig(i,:,j) - meanPtrig)./stdPtrig;
124:        out.stds{t} = ripplestdout;
125:        out.meanPtrig{t} = meanPtrig;
[... 8 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "SWR onset (Methods, Analysis of neural data, paragraph 4). The triangular kernel's width is\n    not given in the Methods; the code's RTCSD.m is followed. Method M.",
 "new_string": "SWR onset (Methods, Analysis of neural data, paragraph 4). The Methods do not give the kernel;\n    the code's RTCSD.m smooths each site with its neighbours as (a + 2b + c)/4, followed here.\n    Method M."
}
```

```
The file claims/jones-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "before (Methods, paragraph 3; Results, paragraph 2). For vehicle epochs the Methods do not\n    say; readings (a) their own mean and SD; (b) the code's (RTspecgram3.m). Regions CA1-sr, CA3,\n    DG. Method M.",
 "new_string": "before (Methods, paragraph 3; Results, paragraph 2). For vehicle epochs the Methods do not\n    say; they are z-scored by their own mean and SD over valid immobility, as the code does. The\n    code (RTspecgram3.m) z-scores every session, CNO included, by its own spectrogram mean and\n    SD, and uses SWRs of 5 SD; this is a variant, the Methods' z-scoring the main reading.\n    Regions CA1-sr, CA3, DG. Method M."
}
```

```
The file claims/jones-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/jones-2021.yaml paper/10.1016-j.celrep.2021.110159.txt 2>&1 | tail -5; grep -c "criterion:" claims/jones-2021.yaml; grep -c "^  statistics:" claims/jones-2021.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/jones-2021.yaml`. The quote checker passes it with no problems: 41 claims, 41 quotes, 160 statistical values. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC9069800): main text, STAR Methods and figure legends, plus the main supplement PDF (Figures S1 to S7, Tables S1 to S6). I did not read the version of record. I also read the paper's code: github.com/emilyasterjones/interneurons_modulate_drive, tag v1.0.0, commit 63b1acb (Zenodo 10.5281/zenodo.5618979).

**Missing.** Supplementary Table S7 (sex-stratified effects, an xlsx file) is not under `paper/`. Only one claim, `sex-stratified-effects`, needs it. That claim is written from the Results text and has no statistics. The rest of the paper's results do not depend on it.

**Counts.** 41 claims, all quoted, all with criteria; 37 have statistics and 11 have expected values. Most claims are LMM treatment and genotype effects from Figures 2 to 6 and S2 to S7. They share one method, "Method M", set out in the opening comment with each part cited to the Methods or code. Every claim also has its own criterion.

**Details the paper leaves open, with the readings named**
- **Log transform:** (a) only for features whose residuals are right-skewed, as the Methods say (main); (b) every feature, as the code does.
- **SWR threshold:** 3 SD in the Methods (main); the code counts SWRs at 5 SD for rate, length and chains (variant).
- **Holm-Bonferroni family:** 24 rest or 36 run comparisons, as the Methods define. When the whole family isn't computed, p < 0.05/24 or 0.05/36 counts as significant and p ≥ 0.05 as not.
- **SG z-scoring during SWRs:** the Methods z-score CNO sessions by the vehicle session of the day before (main); the code z-scores every session by its own mean and SD (variant).
- **Per-animal change in the correlation claims (Figures S2C-D, S4E):** difference of means, or difference of the LMM fitted responses.
- **Percent of SWRs longer than 100 ms:** denominator is valid SWRs or all detected events; values pooled over sessions or averaged per session.
- **Others:**
  - SWR frequency data points: one mean per SWR, or every interpeak value.
  - SW amplitude: one CA1-sr site, or every CA1-sr site.
  - Run coherence: per 1 s bin, or over all run periods.
  - Rest SG power measure: filtered envelope, or multitaper power.
  - Running speed: averaged over run periods, or over the whole session.
  - CA3 overlap average: over sessions, or pooled over events.
  - Sign of the input resistance change.

**Inconsistencies in the paper, noted in the claims**
- The text says SST+ suppression increased CA3 SWR rate, but the legend gives p = 0.77. It is a separate claim, judged as the text states it.
- The Results say input resistance decreased; the Figure S1F legend says it increased.
- Some cross-references point to the wrong item: "Table S3" should be S2, "Figure S3C–D" should be S2C-D, "S5D" should be S4D.
- Figure 5G's genotype difference has p = 0.95 in CA1, but the text says the effects were "detectably different".
- The Methods give the single-shank probe to cohort 3; the Results give it to cohort 1.

**Data a claim needs that may not be deposited.** The fast-ripple analysis needs signal above 300 Hz, while the deposit is described as 0–300 Hz LFP. Histology and the ex vivo slice recordings are not among the deposited data either.

## End of run

36 turns, 7 minutes, $2.72 at API prices, result: success.
