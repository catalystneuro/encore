# gillespie-2024 · claims · run 45860608136

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims tools; wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
protocol.lock
questions
[... 431 more lines not kept]
```

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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
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
cd  cat claims/fouke-2025.yaml | head -150; cat papers/datasets/gillespie-2024.yaml; head -30 paper/*.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 25,140p claims/fouke-2025.yaml; echo ----; cat papers/datasets/gillespie-2024.yaml; echo ---; wc -c paper/*.txt; head -c 600 paper/*.txt; cat claims/gillespie-2021.yaml | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  fold -w 4000 -s paper/*.txt | head -c 60000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/bzkkxm4w5.txt"
}
```

```
1	DOI: 10.7554/elife.90944
2	Version: version of record
3	Source: find_reuse cache
4	Stored: 2026-11-10
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc eLife Elife eLife eLife 2050-084X eLife Sciences Publications, Ltd 11221834 38958562 90944 10.7554/eLife.90944 Research Article Neuroscience Neurofeedback training can modulate task-relevant memory replay rate in rats Gillespie Anna K https://orcid.org/0000-0003-0980-2408 [removed: an e-mail address] 1 2 Astudillo Maya Daniela 2 Denovellis Eric L https://orcid.org/0000-0003-4606-087X 2 3 Desse Sachi 2 Frank Loren M https://orcid.org/0000-0002-1752-5677 2 3 1 https://ror.org/00cvxb145 Departments of Biological Structure and Lab Medicine & Pathology, University of Washington Seattle United States 2 https://ror.org/043mz5j54 Departments of Physiology and Psychiatry and the Kavli Institute for Fundamental Neuroscience, University of California, San Francisco San Francisco United States 3 https://ror.org/006w34k90 Howard Hughes Medical Institute Chevy Chase United States Colgin Laura L Reviewing Editor https://ror.org/00hj54h04 University of Texas at Austin United States Colgin Laura L Senior Editor https://ror.org/00hj54h04 University of Texas at Austin United States 03 7 2024 2024 12 RP90944 19 7 2023 This manuscript was published as a preprint. 15 7 2023 This manuscript was published as a reviewed preprint. 12 9 2023 The reviewed preprint was revised. 27 3 2024 © 2023, Gillespie et al 2023 Gillespie et al https://creativecommons.org/licenses/by/4.0/ This article is distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use and redistribution provided that the original author and source are credited. Hippocampal replay – the time-compressed, sequential reactivation of ensembles of neurons related to past experience – is a key neural mechanism of memory consolidation. Replay typically coincides with a characteristic pattern of local
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -w 4000 -s paper/*.txt | tail -c +60000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/bs4mu63k7.txt"
}
```

```
1	food restricted to a maximum of 85% of free-feeding weight. All procedures were approved by the Institutional Animal Care and Use Committee at the University of California, San Francisco (Protocol # AN191130). Method details Behavioral training Food-restricted rats first complete two 40 min sessions of training on a linear track to receive liquid food reward (evaporated milk +5% sucrose) from automated, photogated reward ports at each end of the track. Motivated 
2	subjects (>50 rewards on final session) advance to learn a complex spatial memory task. This task takes place on a large, walled maze equipped with reward ports, the same as used in Gillespie et al., 2021 . Pretraining occurs as described in Gillespie et al., 2021 ; briefly, subjects are gradually taught to reliably perform the task, with each trial consisting of an initiation poke at the home port and small (50 µL) reward delivery, then an extended dwell period at whichever of the two central ports illuminates, and finally a visit to one of the arm ports. During pretraining, both center ports require the rat to keep its nose in the port for a delay period, randomly chosen from a range, up to 5–10 s. After the delay is complete, a tone plays and a small reward (50 µL) is delivered. Finally, the subject must choose one arm to visit; only one out of the eight arms will deliver reward at any given time, so the rat must visit different arms over several trials to discover the goal arm. The rat must remember this location and return to it on subsequent trials to receive a large reward (150 µL) at the arm port. After a certain number of rewards earned at the goal arm (10-15), the goal arm will change, causing the rat to need to search among arms to find the new goal location. Later in training, goal locations are changed after 4–12 repeat visits. Any deviation from the trial structure described results in a 30–45 s ‘timeout’ during which all ports deilluminate; no reward will be delivered from any port until 
[... 148 more lines not kept]
```

**Agent**

The full text (version of record, with figure supplement legends) is present. Now reading the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/LorenFrankLab/Gillespie_eLife_2024 && cd Gillespie_eLife_2024 && git log --oneline | head; git rev-parse HEAD; find . -type f -not -path './.git/*' | head -100; cat README* | head -100
```

```
ad5801a updates for reviewer figure
09f2774 Merge branch 'master' of https://github.com/LorenFrankLab/Gillespie_eLife_2024
0f0e603 major cleanup & organization of analysis scripts
3dd1b32 Update README.md
55ac235 add license and readme from main branch
655082a initial commit
ad5801a28a0cf2a0ea97a1e25328db1c8376086c
./dfs_rips_post_incl_trigger.m
./dfs_ripcontent_vsctrlrats.m
./dfa_ripquantpertrial_allphase_NF.m
./dfs_rips_pre_incl_trigger.m
./dfs_rips_post_EXCL_trigger.m
./plot_task_params.m
./dfs_RWsimulation.m
./dfa_positionvariance.m
./dfs_decodequality.m
./dfa_muarate_NF.m
./agplotripraster.m
./dfs_positionvariance.m
./dfs_rips_vsctrlrats_excltrig.m
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gillespie_eLife_2024 && wc -l *.m && cat dfs_rips_vsctrlrats.m
```

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/b7oynap45.txt

Preview (first 2KB):
    81 agplotripraster.m
    82 allrat_lmeplot.m
    17 binnedsemcurve.m
   170 dfa_RWsimulation.m
   158 dfa_muarate_NF.m
   232 dfa_plotripcontent_nf.m
    54 dfa_positionvariance.m
   242 dfa_ripcontent_nf.m
   179 dfa_ripquantpertrial_allphase_NF.m
   240 dfs_RWsimulation.m
   277 dfs_decodequality.m
   176 dfs_muarate.m
    31 dfs_plotripcontent.m
   146 dfs_positionvariance.m
   519 dfs_ripcontent.m
   527 dfs_ripcontent_vsctrlrats.m
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/b7oynap45.txt"
}
```

```
1	    81 agplotripraster.m
2	    82 allrat_lmeplot.m
3	    17 binnedsemcurve.m
4	   170 dfa_RWsimulation.m
5	   158 dfa_muarate_NF.m
6	   232 dfa_plotripcontent_nf.m
7	    54 dfa_positionvariance.m
8	   242 dfa_ripcontent_nf.m
9	   179 dfa_ripquantpertrial_allphase_NF.m
10	   240 dfs_RWsimulation.m
11	   277 dfs_decodequality.m
12	   176 dfs_muarate.m
13	    31 dfs_plotripcontent.m
14	   146 dfs_positionvariance.m
15	   519 dfs_ripcontent.m
16	   527 dfs_ripcontent_vsctrlrats.m
17	   210 dfs_rips_post_EXCL_trigger.m
18	   992 dfs_rips_post_incl_trigger.m
19	  1002 dfs_rips_pre_incl_trigger.m
20	   305 dfs_rips_timecourse.m
[... 654 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gillespie_eLife_2024 && cat dfa_ripquantpertrial_allphase_NF.m allrat_lmeplot.m
```

```
function out = dfa_ripquantpertrial_allphase_NF(index, excludeperiods, rippleskons, trials, pos, varargin)

%  Parse through trials; note size and time of each ripple in each trial phase 
%   Also save whether or not wait trials contain a trigger event (t22) for later exclusion
% For each trial phase, include the trials with no lockout through that phase 
% note: always check that leavehome>0 in order to exclude bug trials

% phases: home, r/w, postr/w, outer(rew/unrew), lockout, other
%  Options:
%       appendindex-- Determines whether index is included in output vector
%           Default: 1
%       trialphase-- what part of the trial to select. options = 1:home, 2:rw, 3:postrw,4:outer
%           Default: 2 (rw)
%       ripthresh-- exclude events based on size (thresh of 2 includes all)
%           Default: 2
%       includelockouts-- 1=lockouts included; 0 = no lockout trials included -1 = include trials with lockouts after rw success -2 = lockout times only
%           Default: 1

% define defaults
appendindex = 1;
[... 242 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gillespie_eLife_2024 && cat dfs_ripcontent_vsctrlrats.m
```

```
<persisted-output>
Output too large (32.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/baryhes41.txt

Preview (first 2KB):
%% rip conditioning: main content analyses
% focus on post-conditioning, since that's when we have good quality decoding
% relationship between behavior and rips/replay goes here, since we have behavior outputs 

animals = {'jaq','roquefort','despereaux','montague','remy','gus','bernard','fievel'}; 

epochfilter{1} = ['(isequal($cond_phase,''plateau'')) & $ripthresh>=0 & $gooddecode==1'];  % for conditioning rats
epochfilter{2} = ['$ripthresh==0 & (isequal($environment,''goal'')) & $forageassist==0 & $gooddecode==1 '];  % for control rats
epochfilter{3} = ['$ripthresh==0 & (isequal($environment,''goal_nodelay'')) & $forageassist==0  & $gooddecode==1'];  % for control rats

% resultant excludeperiods will define times when velocity is high
timefilter{1} = {'ag_get2dstate', '($immobility == 1)','immobility_velocity',4,'immobility_buffer',0};
iterator = 'epochbehaveanal';

f = createfilter('animal',animals,'epochs',epochfilter,'excludetime', timefilter, 'iterator', iterator);
f = setfilterfunction(f, 'dfa_ripcontent_nf', {'ripdecodesv3','trials','pos'});
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4ca2aa8b-9c2a-4856-9fc0-6be9f60fa9e4/tool-results/baryhes41.txt"
}
```

```
1	%% rip conditioning: main content analyses
2	% focus on post-conditioning, since that's when we have good quality decoding
3	% relationship between behavior and rips/replay goes here, since we have behavior outputs 
4	
5	animals = {'jaq','roquefort','despereaux','montague','remy','gus','bernard','fievel'}; 
6	
7	epochfilter{1} = ['(isequal($cond_phase,''plateau'')) & $ripthresh>=0 & $gooddecode==1'];  % for conditioning rats
8	epochfilter{2} = ['$ripthresh==0 & (isequal($environment,''goal'')) & $forageassist==0 & $gooddecode==1 '];  % for control rats
9	epochfilter{3} = ['$ripthresh==0 & (isequal($environment,''goal_nodelay'')) & $forageassist==0  & $gooddecode==1'];  % for control rats
10	
11	% resultant excludeperiods will define times when velocity is high
12	timefilter{1} = {'ag_get2dstate', '($immobility == 1)','immobility_velocity',4,'immobility_buffer',0};
13	iterator = 'epochbehaveanal';
14	
15	f = createfilter('animal',animals,'epochs',epochfilter,'excludetime', timefilter, 'iterator', iterator);
16	f = setfilterfunction(f, 'dfa_ripcontent_nf', {'ripdecodesv3','trials','pos'});
17	f = runfilter(f);
18	
19	%save('/media/anna/whirlwindtemp2/ffresults/NFripcontent_vsctrlrats.mat','f','-v7.3')
20	%load('/media/anna/whirlwindtemp2/ffresults/NFripcontent_vsctrlrats.mat','f')
[... 508 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gillespie_eLife_2024 && cat dfa_ripcontent_nf.m; sed -n 675,849p dfs_rips_vsctrlrats.m | head -60; cat plot_task_params.m | head -40
```

```
function out = dfa_ripcontent(index, excludeperiods, ripdecodes, trials, pos, varargin)

%

% define defaults
appendindex = 0;
box_thresh = .7; % proportion of posterior density in box to be considered box ripple
% process varargin if present and overwrite default values
if (~isempty(varargin))
    assign(varargin{:});
end

d = index(1);
e = index(2);

if isempty(ripdecodes) || length(ripdecodes{d})< e || isempty(ripdecodes{d}{e})
    out.riptsz = [];
    out.trips = [];   
else
    
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python3 -c "import json,sys;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])" 2>/dev/null || ls schemas; grep -l "elsewhere" claims/*.yaml | head -5
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[6000:])"; sed -n 1,80p tools/claims_check.py
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -h -B2 -A1 "^  where:" claims/*.yaml | head -30; grep -l "relation: reuses" papers/datasets/*.yaml | head -5
```

```
of 2038 bp, and that the in-total N50 of the assembled transcripts is 476 bp
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  expected:
--
    showed significant divergence along both PC1 and PC2 axes (15% variance)
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  expected:
--
    to controls than chronic-OA samples
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  depends_on:
--
    conditions ... organelle inner membrane and mitochondrial inner membrane
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  expected:
--
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gillespie_eLife_2024 && sed -n 1,30p dfs_rips_vsctrlrats_excltrig.m; grep -n "%% PART" dfs_rips_vsctrlrats_excltrig.m dfs_rips_timecourse.m dfs_RWsimulation.m; awk '/%% PART 2/,/%% PART 5/' dfs_rips_vsctrlrats_excltrig.m | head -120
```

```
%% Neurofeedback: comparisons between conditioned and control animals

animals = {'jaq','roquefort','despereaux','montague','remy','gus','bernard','fievel'}; 

epochfilter{1} = ['isequal($cond_phase,''plateau'') & isequal($environment,''goal'') '];  %cond rats
epochfilter{2} = ['$ripthresh==0 & (isequal($environment,''goal'')) & $forageassist==0 '];  % for control rats
%epochfilter{4} = ['$ripthresh==0 & (isequal($environment,''goal_nodelay'')) & $forageassist==0 '];  % for control rats

% resultant excludeperiods will define times when velocity is high
timefilter{1} = {'ag_get2dstate', '($immobility == 1)','immobility_velocity',4,'immobility_buffer',0};
iterator = 'epochbehaveanal';
f = createfilter('animal',animals,'epochs',epochfilter,'excludetime', timefilter, 'iterator', iterator);

%args: appendindex (0/1), ripthresh (default 2),
% includelockouts (1/0/-1 include trials with lockouts after rw success/-2 lockouts only/2 outersuccess only) 
% excltrigger: exclude trigger event
% excluderwstart: amount (in seconds) to exclude from beginning of rw phase (trials shorter than exclude amount will be dropped)
% excludepostrwstart: amount (in seconds) to exclude from beginning of POSTrw phase (trials shorter than exclude amount will be dropped)
f = setfilterfunction(f, 'dfa_ripquantpertrial_allphase_NF', {'ca1rippleskons','trials','pos'}, 'excltrigger',1);
f = runfilter(f);
[... 138 more lines not kept]
```

**Agent**

Code read (LorenFrankLab/Gillespie_eLife_2024 at ad5801a, the commit archived in the paper). Writing the claims file now.

**Agent calls Bash**

```bash
cd  grep -o "Figure 2—figure supplement 1C , inset). Instead.\{0,10\}" paper/*.txt | head -2; grep -o "only two out of four subjects.\{0,80\}" paper/*.txt; grep -o "p=0, 2.132x10 –36" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/gillespie-2024.yaml",
 "content": "# Claims for Gillespie, Astudillo Maya, Denovellis, Desse & Frank (2024), \"Neurofeedback training\n# can modulate task-relevant memory replay rate in rats\", eLife 12, RP90944, tested on dandiset\n# 000115.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-26,\n# protocol pilot-19 as stated in docs/protocol.md.\n#\n# Text read: the version of record (eLife RP90944, PMC11221834), in paper/10.7554-elife.90944.txt:\n# Introduction, Results, Discussion, Methods, the legends of Figures 1 to 5 and of the figure\n# supplements (Figure 1-figure supplement 1, Figure 2-figure supplement 1, Figure 4-figure\n# supplement 1, Figure 5-figure supplement 1), which are inline in the text, the eLife assessment,\n# the public reviews and the author response. The PDF was not opened; no claim needed a figure\n# value that the text does not give. The author response is not used for claims.\n#\n# Data the paper used. Eight male Long-Evans rats in two cohorts, each implanted with 30 tetrodes\n# in dorsal CA1, performing the same spatial memory task: a trial starts with a nosepoke at the\n# home port, then a nosepoke held at whichever of two center ports lights until a tone and small\n# reward (the \"pre-reward\" period, reward delivery, then the \"post-reward\" period until the rat\n# leaves the port), then a visit to one of eight arms, one of which (the goal) gives a large\n# reward; the goal changes after a number of rewards.\n#   - Control cohort (rats jaq, roquefort, despereaux and montague, in that order in every legend\n#     according to the code): both center ports impose a random delay. These are the rats of\n#     Gillespie et al. 2021 and are the data of dandiset 000115. The paper uses \"trials from all\n#     days of reliable post-implant task performance\".\n#   - Manipulation (neurofeedback) cohort (remy, gus, bernard and fievel, rat1 to rat4): one center\n#     port is the neurofeedback (NF) port, where reward follows the first online-detected\n#     suprathreshold SWR; the other is a delay port whose delay is drawn from the 8 previous NF\n#     latencies. Only the stable (\"plateau\") period of training is analysed, except Figure 2-figure\n#     supplement 1A and B. These data are in dandiset 000629, which the paper deposited and which\n#     is not the dataset of this record; every claim that needs them is data elsewhere.\n# Measured variables: CA1 LFP and spike marks (30 kHz), online SWR trigger times, port beam breaks,\n# reward delivery, head LED position. Processed outputs are on figshare\n# (doi:10.6084/m9.figshare.24919590.v1); no claim relies on them.\n#\n# Code read: github.com/LorenFrankLab/Gillespie_eLife_2024, commit\n# ad5801a28a0cf2a0ea97a1e25328db1c8376086c (the head, and the revision archived at Software\n# Heritage that the paper cites). MATLAB scripts in the Frank lab filter framework. The README maps\n# figure panels to script parts; for Figure 2-figure supplement 1F to H it is out of date\n# (dfs_rips_vsctrlrats.m part 11 makes 1F, part 9 makes 1G, part 10 makes 1H). The SWR detector,\n# the position processing, the trial parser, label_trial_interval.m and the clusterless decoder\n# are not in the repository (filterframework_shared, trodes2ff_shared, Gillespie_Neuron_2021 and\n# replay_trajectory_classification).\n#\n# Shared methods, settled by the code where the Methods are silent, used by the criteria below:\n#   - Epochs (dfs_rips_vsctrlrats.m). Control cohort, Figures 2 and 3 and their supplements:\n#     run epochs with ripthresh 0, environment \"goal\" and forageassist 0. Figures 4 and 5: the same\n#     with gooddecode 1 (dfs_ripcontent_vsctrlrats.m). Manipulation cohort: cond_phase \"plateau\",\n#     environment \"goal\".\n#   - Trials (dfa_ripquantpertrial_allphase_NF.m): trials with no lockout and leavehome > 0, or with\n#     a successful center port visit followed by a lockout. Pre-reward period from center port\n#     entry (RWstart) to reward delivery (RWend); post-reward period from RWend to leaving the port\n#     (leaveRW). Control trials are all trial types (type >= 1); manipulation type 1 is NF, type 2\n#     delay.\n#   - SWRs: offline consensus detection as in the Methods (150 to 250 Hz, squared, summed over CA1\n#     cell layer tetrodes, 4 ms gaussian, square root, 2 sd above the behavioral epoch mean,\n#     at least 15 ms). The code keeps only SWRs whose start and end both fall in immobility (head\n#     speed below 4 cm/s, ag_get2dstate, no buffer), all sizes (maxthresh > 2). An SWR belongs to a\n#     period when its start time falls inside it. Rate per trial is count over period duration.\n#   - Speed: the per-trial mean of the position structure's smoothed velocity (column 9) over the\n#     period. The smoothing is in the position processing, not in the repository.\n#   - Within-subject NF against delay: Wilcoxon rank-sum per rat, Benjamini-Hochberg over the four\n#     rats (fdr_bh). Cohort comparisons (allrat_lmeplot.m): two separate models, control trials\n#     against NF trials and control trials against delay trials, Variable ~ Cohort + (1|Indiv),\n#     linear (fitglme/fitlme) for rates, durations, sizes and fractions, Poisson for counts; the\n#     p-value is that of the Cohort fixed effect. The bar inset is the mean over rats of each rat's\n#     median, and the code prints the ratios control/NF, control/delay and NF/delay of those means.\n#   - Replay (dfa_ripcontent_nf.m, dfs_ripcontent_vsctrlrats.m): an SWR is replay when its\n#     decode is classed continuous and its largest maze-segment share (arm_prop, box plus 8 arms)\n#     exceeds 0.3; remote when that segment is an arm (the rat is in the box at the center ports).\n#     The Methods state the class as \"the probability of the continuous movement model exceed a 0.8\n#     threshold\"; the code uses max_state == 1, computed upstream. Both readings are named where a\n#     claim depends on them.\n#   - Task phase of a trial: label_trial_interval.m of Gillespie et al. 2021 (search trials have\n#     phase <= 1, repeat trials > 1, error trials a fractional phase below 0.85), as described in\n#     claims/gillespie-2021.yaml.\n# Details none of the sources fix are named in the criteria.\n#\n# A discrepancy the claims do not rest on: the trigger delay is 75, 100, 50 and 50 ms for rat1 to\n# rat4 in the Methods and in the code (ratoffset), and 100, 50, 75 and 75 ms in the Figure 1-figure\n# supplement 1B legend.\nschema_version: 2\npaper: doi:10.7554/elife.90944\nclaims:\n- id: control-cohort-trial-counts\n  kind: link\n  statement: The control cohort data used for the center port analyses comprise 2490, 2629, 2027\n    and 3021 trials for the four control rats.\n  source: Figure 2C legend (the same counts in Figure 1-figure supplement 1C, Figure 2-figure\n    supplement 1E and F)\n  quote: control cohort n=2490, 2629, 2027, and 3021 trials\n  expected:\n  - quantity: jaq trials\n    value: 2490\n    tolerance: 249\n  - quantity: roquefort trials\n    value: 2629\n    tolerance: 263\n  - quantity: despereaux trials\n    value: 2027\n    tolerance: 203\n  - quantity: montague trials\n    value: 3021\n    tolerance: 302\n  criterion: Trials selected as in the header (Shared methods, Epochs and Trials), counting\n    trials with a pre-reward period, per rat in the order jaq, roquefort, despereaux, montague\n    (dfs_rips_vsctrlrats.m). If the dandiset does not mark the epoch flags (ripthresh,\n    environment, forageassist), the readings are (a) all run epochs of the full delay task and\n    (b) those epochs minus any the dandiset or Gillespie et al. 2021 marks as forage assist or no\n    delay. Reproduced when all four counts are within tolerance under one reading; partially\n    reproduced when two or three are.\n- id: control-decode-counts\n  kind: link\n  statement: The control cohort data used for the replay and behavior analyses comprise 24, 32,\n    23 and 33 behavioral epochs, 2058, 2509, 1879 and 2795 trials for remote replay rate, and\n    1458, 1636, 1464 and 2181 trials for the replay GLM.\n  source: Figure 4D, 4E and 4G legends; Figure 5 legend\n  quote: control cohort n=24, 32, 23, and 33 behavioral epochs\n  expected:\n  - quantity: jaq epochs\n    value: 24\n    tolerance: 2.4\n  - quantity: roquefort epochs\n    value: 32\n    tolerance: 3.2\n  - quantity: despereaux epochs\n    value: 23\n    tolerance: 2.3\n  - quantity: montague epochs\n    value: 33\n    tolerance: 3.3\n  - quantity: jaq trials, Figure 4E\n    value: 2058\n    tolerance: 206\n  - quantity: roquefort trials, Figure 4E\n    value: 2509\n    tolerance: 251\n  - quantity: despereaux trials, Figure 4E\n    value: 1879\n    tolerance: 188\n  - quantity: montague trials, Figure 4E\n    value: 2795\n    tolerance: 280\n  - quantity: jaq trials, Figure 4G\n    value: 1458\n    tolerance: 146\n  - quantity: roquefort trials, Figure 4G\n    value: 1636\n    tolerance: 164\n  - quantity: despereaux trials, Figure 4G\n    value: 1464\n    tolerance: 146\n  - quantity: montague trials, Figure 4G\n    value: 2181\n    tolerance: 218\n  criterion: Epochs as in the header (Epochs, with gooddecode 1). Figure 4E trials are\n    trials with a task phase (non-lockout trials with leavehome > 0, dfa_ripcontent_nf.m).\n    Figure 4G trials are those with a task phase and a previous goal (from the second goal block\n    on, Methods, Replay content analysis). If the dandiset does not mark gooddecode, the reading\n    is the epochs of control-cohort-trial-counts, and the epoch counts are then reported as not\n    comparable. Reproduced when the epoch counts and at least one of the two trial-count sets are\n    within tolerance for all four rats; partially reproduced when the trial counts match for\n    at least two rats under either reading.\n- id: fig2s1c-control-prereward-swr-counts\n  statement: The control cohort has 2660, 581, 2192 and 5429 SWRs in the pre-reward period at the\n    center ports.\n  source: Figure 2-figure supplement 1C legend\n  quote: control cohort n=2660, 581, 2192, and 5429 SWRs\n  expected:\n  - quantity: jaq pre-reward SWRs\n    value: 2660\n    tolerance: 266\n  - quantity: roquefort pre-reward SWRs\n    value: 581\n    tolerance: 58\n  - quantity: despereaux pre-reward SWRs\n    value: 2192\n    tolerance: 219\n  - quantity: montague pre-reward SWRs\n    value: 5429\n    tolerance: 543\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: SWRs detected and assigned as in the header (SWRs), summed over the trials of\n    control-cohort-trial-counts (dfs_rips_vsctrlrats_excltrig.m part 2). Open, as the detector is\n    not in the repository and the Methods say only \"2 sd above the behavioral epoch mean\" -\n    whether the mean and sd are taken over the whole epoch or over immobile times. Readings (a)\n    whole epoch, (b) immobile times (speed < 4 cm/s); and, as a variant, SWR detections the\n    dandiset may hold. Reproduced when all four counts are within tolerance under one reading;\n    partially reproduced when at least two are.\n- id: fig2s1a-trigger-size-increase\n  statement: Over neurofeedback training, as the detection threshold rose, manipulation subjects\n    produced increasingly large trigger SWRs at the NF port.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 1; Figure 2-figure supplement 1A\n  quote: subjects in the manipulation cohort successfully produced increasingly large trigger events\n    at the neurofeedback port over the course of training\n  data: elsewhere\n  where: DANDI 000629\n  criterion: Per rat, mean trigger SWR size (sd) of NF trials in the second half of each epoch,\n    over the epochs before the plateau (Figure 2-figure supplement 1A legend;\n    dfs_rips_timecourse.m part 1). Reproduced when the size rises across training (positive\n    Pearson correlation with epoch order) in all four rats.\n- id: fig2s1b-faster-than-predicted\n  statement: Manipulation subjects produced large SWRs much faster than predicted from the\n    prevalence of similar-sized events before and early in training.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 1; Figure 2-figure supplement 1B; Methods, Neurofeedback wait time prediction\n  quote: subjects produced large SWR events much faster than would have been predicted based on the\n    initial prevalence of similarly sized events\n  data: elsewhere\n  where: DANDI 000629\n  criterion: Predicted wait from size-binned occurrence rates at the center ports (pre and post\n    reward) during the first ~7 days of pretraining and early training, bins with at least 10\n    events; actual and predicted waits concatenated over sessions and smoothed with a 200-trial\n    moving average (Methods; dfs_RWsimulation.m). Reproduced when the smoothed actual wait lies\n    below the predicted wait for most of later training in all four rats.\n- id: fig2s1c-swr-size-not-increased\n  statement: SWR size in the pre-reward period was not consistently larger on NF than on delay\n    trials (two of four rats showed very slight significant increases), and neither trial type\n    differed in size from the control cohort.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 3; Figure 2-figure supplement 1C\n  quote: subjects did not consistently increase SWR size ... only two out of four subjects showed\n    very slight but significant increases\n  statistics:\n  - about: NF against delay SWR size, rat1\n    test: ranksum\n    p: 1.734e-16\n    corrected: Benjamini-Hochberg\n    n: 13209 NF and 8716 delay SWRs\n  - about: NF against delay SWR size, rat2\n    test: ranksum\n    p: 7.389e-9\n    corrected: Benjamini-Hochberg\n    n: 3060 NF and 1618 delay SWRs\n  - about: NF against delay SWR size, rat3\n    test: ranksum\n    p: 0.921\n    corrected: Benjamini-Hochberg\n    n: 5369 NF and 2535 delay SWRs\n  - about: NF against delay SWR size, rat4\n    test: ranksum\n    p: 0.921\n    corrected: Benjamini-Hochberg\n    n: 7165 NF and 3855 delay SWRs\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.234\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.184\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig2s1c-control-prereward-swr-counts\n  criterion: SWR size (maximum threshold in sd) of pre-reward SWRs, all suprathreshold events\n    excluded on both trial types (online triggers matched to the SWR containing them, Methods,\n    SWR size quantification; dfa_ripquantpertrial_allphase_NF.m with excltrigger 1). Tests as in\n    the header. Claims of absence, judged on the paper's tests. Reproduced when at most two of\n    the four corrected ranksums have p < 0.05 and neither mixed model finds a cohort effect at\n    p < 0.05; the size differences are reported.\n- id: fig2s1d-twice-events-all-sizes\n  statement: Within the manipulation cohort, NF trials contained roughly twice as many pre-reward\n    SWRs as delay trials per unit time, at every SWR size.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 3; Figure 2-figure supplement 1D\n  quote: neurofeedback trials contained roughly twice as many events relative to delay trials for\n    all SWR sizes\n  data: elsewhere\n  where: DANDI 000629\n  expected:\n    quantity: NF over delay occurrence rate, per size bin\n    value: 2\n    tolerance: 0.5\n  criterion: Per epoch, SWRs of each type binned by size in 1 sd bins from 2 to 30 sd, divided\n    by the summed pre-reward duration of that trial type; fold change NF over delay in bins\n    occupied on both; averaged over epochs (dfs_rips_vsctrlrats_excltrig.m part 4),\n    suprathreshold events excluded. The tolerance (0.5) is for \"roughly\"; a fold change from 1.5\n    to 2.5 reads as roughly twice. Reproduced when the fold change in every bin from 2 to 14 sd\n    (the plotted range) with data lies in that range for all four rats; partially reproduced\n    when it exceeds 1 in every such bin but leaves the range.\n- id: fig2c-prereward-rate\n  statement: In the pre-reward period SWR rate was about twice as high on NF as on delay trials,\n    and both manipulation trial types had higher rates than control cohort trials.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 5; Figure 2C, left\n  quote: during the pre-reward period, SWR rates were approximately twice as high on neurofeedback\n    compared to delay trials, and both trial types from the manipulation cohort had much higher\n    rates than trials from the control cohort\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 4.382e-258\n    corrected: Benjamini-Hochberg\n    n: 1892 NF and 2022 delay trials\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 7.111e-83\n    corrected: Benjamini-Hochberg\n    n: 684 NF and 640 delay trials\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 5.689e-214\n    corrected: Benjamini-Hochberg\n    n: 1157 NF and 1201 delay trials\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 3.285e-191\n    corrected: Benjamini-Hochberg\n    n: 1602 NF and 1552 delay trials\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 1.126e-16\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.009\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  expected:\n    quantity: NF over delay pre-reward SWR rate\n    value: 2\n    tolerance: 0.3\n  criterion: Per-trial pre-reward rate, trigger SWR included (dfs_rips_vsctrlrats.m part 1),\n    tests as in the header. The ratio is the code's inset ratio (mean over rats of per-rat\n    medians, NF over delay); as variants the ratio of means of per-trial rates and the mean of\n    per-rat ratios of medians. Tolerance 0.3 for \"approximately twice\" (1.7 to 2.3 rounds to\n    twice, not to 1.5 or 2.5). Reproduced when all four corrected ranksums have p < 0.05 with NF\n    higher, both mixed models give p < 0.05 with the manipulation trials higher, and the ratio is\n    within tolerance under one reading; partially reproduced when the tests hold and the ratio\n    does not.\n- id: fig2s1e-prereward-rate-excluding-suprathreshold\n  statement: The pre-reward SWR rate effect did not depend on the trigger SWR; excluding\n    suprathreshold events from both NF and delay trials gave the same result.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 5; Figure 2-figure supplement 1E\n  quote: This effect was not dependent on the trigger SWR, as excluding suprathreshold events from\n    both neurofeedback and delay trials did not change the result\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 9.873e-136\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 2.562e-34\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 4.017e-91\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 7.171e-49\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 5.574e-8\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.040\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig2c-prereward-rate\n  criterion: As fig2c-prereward-rate, with suprathreshold events excluded on both trial types\n    (dfs_rips_vsctrlrats_excltrig.m part 1). Reproduced when all six tests give p < 0.05 in the\n    direction of fig2c-prereward-rate.\n- id: fig2c-postreward-rate\n  statement: After reward, SWR rate was slightly but significantly higher on delay than on NF\n    trials, and did not differ between the cohorts.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 6; Figure 2C, middle\n  quote: SWR rate was slightly but significantly higher during delay trials compared to\n    neurofeedback trials in the manipulation cohort subjects but was overall indistinguishable\n    between the cohorts\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 3.646e-127\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 0.038\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 6.538e-11\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 2.768e-23\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.142\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.691\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per-trial post-reward rate (dfs_rips_vsctrlrats.m part 2), tests as in the header.\n    Reproduced when all four corrected ranksums give p < 0.05 with delay higher and neither mixed\n    model finds a cohort effect at p < 0.05 (the absence part judged on the paper's test).\n- id: fig2s1f-rate-change-post-minus-pre\n  statement: Relative to the pre-reward period, SWR rate stayed at a high level after reward on NF\n    trials, while it increased substantially on delay and control trials.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 6; Figure 2-figure supplement 1F\n  quote: Relative to the pre-reward period, SWR rates were maintained at a high level during\n    neurofeedback trials, while they increased substantially during delay and control trials\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 0\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 2.132e-36\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 4.528e-117\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 3.821e-139\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 1.352e-5\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.139\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig2s1f-control-rate-increase\n  criterion: Per-trial post-reward minus pre-reward rate (dfs_rips_vsctrlrats.m part 11), tests\n    as in the header. Reproduced when NF differences are lower than delay differences in all four\n    rats (corrected ranksum p < 0.05), the NF-control mixed model gives p < 0.05, and the median\n    difference is positive on delay and control trials.\n- id: fig2s1f-control-rate-increase\n  statement: In the control cohort, SWR rate increased substantially from the pre-reward to the\n    post-reward period at the center ports.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 6; Figure 2-figure supplement 1F\n  quote: Relative to the pre-reward period, SWR rates were maintained at a high level during\n    neurofeedback trials, while they increased substantially during delay and control trials\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: For each control rat, the per-trial post-reward rate minus pre-reward rate, over\n    the trials of control-cohort-trial-counts (dfs_rips_vsctrlrats.m part 11). The paper reports\n    no test on the control cohort alone; \"substantially\" is not quantified. Reproduced when the\n    median and the mean of the difference are positive in all four control rats; partially\n    reproduced in three. The per-rat median and mean differences are reported.\n- id: fig2b-control-timecourse\n  statement: Control cohort subjects rarely generated SWRs in the pre-reward period and had much\n    higher SWR rates after reward delivery.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 4; Figure 2B, bottom row\n  quote: subjects in the control cohort rarely generated SWRs during the pre-reward period but\n    showed much higher SWR rates than the manipulation cohort after reward delivery\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Rate in 0.5 s bins from -20 to 20 s around reward delivery, each trial's SWR times\n    from center port entry to exit, mean over trials that cover the bin, bins with more than 100\n    contributing trials (Methods, Timewise SWR rate quantification; dfs_rips_vsctrlrats.m part 5).\n    The comparison with the manipulation cohort is in fig2b-manipulation-timecourse. Reproduced\n    when, in all four control rats, the mean over the valid post-reward bins exceeds the mean\n    over the valid pre-reward bins; partially reproduced in three. The ratio of the two means\n    is reported, as the paper does not quantify \"much higher\".\n- id: fig2b-manipulation-timecourse\n  statement: Manipulation cohort subjects showed high, stable SWR rates before reward delivery,\n    higher on NF than on delay trials, while control subjects had much higher rates than the\n    manipulation cohort after reward delivery.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 4; Figure 2B\n  quote: Subjects in the manipulation cohort all showed high, stable SWR rates before reward\n    delivery, with neurofeedback trials showing higher SWR rate than delay trials\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig2b-control-timecourse\n  criterion: Binned rates as in fig2b-control-timecourse, trigger SWR excluded on NF trials\n    (Figure 2B legend). Reproduced when, in all four manipulation rats, the NF curve lies above\n    the delay curve in most valid pre-reward bins, and the control rats' mean over the first 5 s\n    after reward exceeds the manipulation rats' mean over the same bins on both trial types. The\n    5 s window is a choice made here (the paper names none); the full valid post-reward range is\n    shown as a variant.\n- id: fig2c-combined-rate\n  statement: Over the pre- and post-reward periods combined, NF trials still had higher SWR rates\n    than delay trials, but neither trial type differed from the control cohort.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 6; Figure 2C, right\n  quote: the neurofeedback trials still showed higher SWR rates than delay trials within the\n    manipulation cohort, but the differences between each trial type and the control cohort were\n    not significant\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 3.324e-64\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 3.136e-40\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 2.996e-69\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 9.066e-50\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.237\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.504\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per-trial rate over pre plus post (total count over total duration,\n    dfs_rips_vsctrlrats.m part 4), tests as in the header. Reproduced when all four corrected\n    ranksums give p < 0.05 with NF higher and neither mixed model gives p < 0.05.\n- id: fig2d-swr-counts\n  statement: SWR counts matched the rates before reward, but after reward NF trials had fewer\n    SWRs than delay trials and both had far fewer than control trials; over the whole port time\n    the cohorts did not differ.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 7; Figure 2D\n  quote: neurofeedback trials contained fewer SWRs than delay trials, and both trial types\n    contained far fewer SWRs post-reward than trials from the control cohort\n  statistics:\n  - about: pre-reward, manipulation NF against control\n    test: Poisson mixed-effects model\n    p: 6.790e-7\n  - about: pre-reward, manipulation delay against control\n    test: Poisson mixed-effects model\n    p: 0.0018\n  - about: post-reward, NF against delay, rat1\n    test: ranksum\n    p: 1.797e-137\n    corrected: Benjamini-Hochberg\n  - about: post-reward, NF against delay, rat2\n    test: ranksum\n    p: 6.100e-10\n    corrected: Benjamini-Hochberg\n  - about: post-reward, NF against delay, rat3\n    test: ranksum\n    p: 6.688e-13\n    corrected: Benjamini-Hochberg\n  - about: post-reward, NF against delay, rat4\n    test: ranksum\n    p: 2.152e-130\n    corrected: Benjamini-Hochberg\n  - about: post-reward, manipulation NF against control\n    test: Poisson mixed-effects model\n    p: 2.361e-12\n  - about: post-reward, manipulation delay against control\n    test: Poisson mixed-effects model\n    p: 5.820e-9\n  - about: pre plus post, manipulation NF against control\n    test: Poisson mixed-effects model\n    p: 0.366\n  - about: pre plus post, manipulation delay against control\n    test: Poisson mixed-effects model\n    p: 0.299\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per-trial counts (dfs_rips_vsctrlrats.m parts 1, 2 and 4), Poisson mixed models and\n    ranksums as in the header. Reproduced when the post-reward ranksums give p < 0.05 with delay\n    higher in all four rats, both post-reward mixed models give p < 0.05 with control higher, both\n    pre-reward mixed models give p < 0.05 with manipulation higher, and neither pre plus post\n    mixed model gives p < 0.05.\n- id: fig2e-postreward-dwell\n  statement: Post-reward dwell time was slightly but significantly shorter on NF than on delay\n    trials, and manipulation subjects stayed at the port about half as long as control subjects.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraphs 7 and 8; Figure 2E\n  quote: subjects in the manipulation cohort remained at the port for approximately half as long as\n    subjects in the control cohort\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 1.397e-23\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 8.588e-49\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 6.180e-4\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 7.127e-257\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 4.075e-18\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 1.835e-18\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  expected:\n    quantity: manipulation over control post-reward dwell time, each trial type\n    value: 0.5\n    tolerance: 0.1\n  criterion: Per-trial post-reward duration, RWend to leaveRW (dfs_rips_vsctrlrats.m part 3),\n    tests as in the header. The ratio is that of the code's inset means of per-rat medians\n    (NF over control and delay over control); as a variant the ratio of means of per-trial\n    durations. Tolerance 0.1 for \"approximately half\" (0.4 to 0.6). Reproduced when all four\n    corrected ranksums give p < 0.05 with NF shorter, both mixed models give p < 0.05 with control\n    longer, and both ratios are within tolerance under one reading.\n- id: fig2s1h-control-dwell-increases\n  statement: In the control cohort, the time spent at the center port after reward delivery\n    tended to increase as subjects gained experience with the task.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 8; Figure 2-figure supplement 1H\n  quote: For the control cohort, the amount of time spent post reward delivery at the center well\n    tends to increase as subjects gain more experience with the task\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per control rat, the mean post-reward duration of each epoch's trials, against the\n    epoch's order (1 to N over the rat's selected epochs in chronological order), Pearson\n    correlation (dfs_rips_vsctrlrats.m part 10, which prints r squared and p; the sign is that of\n    r). The paper reports no statistic. Reproduced when r is positive in all four rats; partially\n    reproduced in three. Each rat's r and p are reported.\n- id: fig2s1g-no-refractory\n  statement: The slightly lower post-reward SWR rate on NF trials is not explained by a refractory\n    period after the trigger SWR; SWR rate after suprathreshold events on delay trials shows no\n    extended suppression.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 6; Figure 2-figure supplement 1G\n  quote: shows no extended suppression of SWR rate following suprathreshold events\n  data: elsewhere\n  where: DANDI 000629\n  criterion: Delay trials with an online suprathreshold event in the pre-reward period and at\n    least 2 s left before reward; SWR rate in 0.5 s bins from 0 to 10 s after the largest SWR of\n    the trial, bins with more than 10 trials (Figure 2-figure supplement 1G legend;\n    dfs_rips_vsctrlrats.m part 9). \"Extended suppression\" is not defined by the paper. Readings\n    (a) the rate in the 0.5 to 1 s bin is at least half the mean rate over 1 to 2 s; (b) the\n    rate over 0.5 to 2 s is at least half the trials' mean pre-reward rate. Reproduced when all\n    four rats meet one reading.\n- id: fig3a-speed-below-immobility\n  statement: Mean head speed while nosepoked before reward was below the 4 cm/s immobility cutoff\n    for all trial types, and slightly but significantly lower on NF trials than on delay and\n    control trials.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 10; Figure 3A\n  quote: The mean speeds of the head-mounted LEDs while the subjects were nosepoked were below our\n    cutoff for immobility (4 cm/s) for all trial types\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 2.447e-223\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 2.760e-85\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 3.247e-80\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 9.077e-36\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 1.260e-7\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 1.121e-4\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig3a-control-speed\n  criterion: Per-trial mean speed over the pre-reward period (header, Speed;\n    dfs_rips_vsctrlrats.m part 7), tests as in the header. Reproduced when every rat and trial\n    type is below 4 cm/s under a reading of fig3a-control-speed, all four corrected ranksums give\n    p < 0.05 with NF slower, and the NF-control mixed model gives p < 0.05 with NF slower.\n- id: fig3a-control-speed\n  statement: In the control cohort, mean head speed during the pre-reward nosepoke was below the\n    4 cm/s immobility cutoff.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 10; Figure 3A\n  quote: The mean speeds of the head-mounted LEDs while the subjects were nosepoked were below our\n    cutoff for immobility (4 cm/s) for all trial types\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per-trial mean of the smoothed head speed over the pre-reward period\n    (dfa_ripquantpertrial_allphase_NF.m, meanvel). Open - the smoothing of the speed is done\n    upstream and the \"mean speed\" of a rat can be read as (a) the median over trials of the\n    per-trial mean (the box plot centre) or (b) the mean over trials; and the speed as (i) the\n    speed the dandiset provides for the head position or (ii) the speed computed from the head\n    LED position with a standard Gaussian smoothing, named in the notebook. Reproduced when all\n    four control rats are below 4 cm/s under one reading of each pair; the values under every\n    reading are reported.\n- id: fig3bc-speed-matched-rates\n  statement: The quartile of NF trials with the highest mean speeds still had higher pre-reward\n    SWR rates than the slowest quartiles of delay and control trials, so movement does not\n    explain the increase.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 10; Figure 3B and C\n  quote: Even with much higher mean speeds ( Figure 3B ), the neurofeedback trials showed higher\n    SWR rates than control and delay trials ( Figure 3C )\n  statistics:\n  - about: SWR rate, NF against delay, rat1\n    test: ranksum\n    p: 3.923e-11\n    corrected: Benjamini-Hochberg\n  - about: SWR rate, NF against delay, rat2\n    test: ranksum\n    p: 1.155e-8\n    corrected: Benjamini-Hochberg\n  - about: SWR rate, NF against delay, rat3\n    test: ranksum\n    p: 1.902e-18\n    corrected: Benjamini-Hochberg\n  - about: SWR rate, NF against delay, rat4\n    test: ranksum\n    p: 5.081e-6\n    corrected: Benjamini-Hochberg\n  - about: SWR rate, manipulation NF against control\n    test: linear mixed-effects model\n    p: 1.019e-6\n  - about: SWR rate, manipulation delay against control\n    test: linear mixed-effects model\n    p: 7.958e-3\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig3a-speed-below-immobility\n  criterion: Per rat, NF trials with mean speed above their 75th percentile; delay trials, and\n    control trials, below their 25th percentile (dfs_rips_vsctrlrats.m part 8); pre-reward rates\n    and tests as in the header. Expected subset sizes 473, 171, 289 and 400 NF, 505, 160, 300 and\n    388 delay, 624, 794, 423 and 913 control trials (Figure 3B legend). Reproduced when all four\n    corrected ranksums and the NF-control mixed model give p < 0.05 with NF higher.\n- id: trialwise-pre-post-correlation\n  statement: Across single trials, pre-reward and post-reward SWR counts were only weakly\n    correlated, positively in some manipulation subjects and negatively in others.\n  source: Results, Neurofeedback training increases SWR rate during the targeted interval,\n    paragraph 11\n  quote: the correlation coefficients between pre-reward and post-reward SWR counts were positive in\n    some subjects and negative in others, and always very small in magnitude\n  statistics:\n  - about: rat1\n    test: correlation\n    statistic: r = -0.084\n    p: 1.47e-7\n  - about: rat2\n    test: correlation\n    statistic: r = 0.130\n    p: 3.84e-6\n  - about: rat3\n    test: correlation\n    statistic: r = 0.118\n    p: 8.60e-9\n  - about: rat4\n    test: correlation\n    statistic: r = -0.061\n    p: 6.01e-4\n  data: elsewhere\n  where: DANDI 000629\n  expected:\n  - quantity: r, rat1\n    value: -0.084\n    tolerance: 0.0084\n  - quantity: r, rat2\n    value: 0.130\n    tolerance: 0.013\n  - quantity: r, rat3\n    value: 0.118\n    tolerance: 0.0118\n  - quantity: r, rat4\n    value: -0.061\n    tolerance: 0.0061\n  criterion: Pearson correlation of per-trial pre-reward and post-reward SWR counts. The code\n    (dfs_rips_vsctrlrats.m, unnumbered part after part 11) computes it per epoch, epochs with more\n    than 10 trials of each type, and for NF, delay and both trial types; the single r and p per\n    rat in the text imply a pooled value. Readings (a) all trials of both types pooled over\n    epochs; (b) NF trials pooled; (c) the median of the per-epoch r over both types. Reproduced\n    when every |r| is below 0.2 with the signs of the paper under one reading, and the four r\n    values are within tolerance under that reading; partially reproduced when the signs and\n    magnitudes hold but the values do not.\n- id: fig4d-fraction-replay-preserved\n  statement: The fraction of pre-reward SWRs that qualified as replay did not differ between the\n    cohorts, nor consistently between NF and delay trials.\n  source: Results, Neurofeedback training preserves replay content during SWRs, paragraph 3;\n    Figure 4D\n  quote: there was no difference in the fraction of SWRs that qualified as replay between the two\n    cohorts, and within each manipulation cohort subject, there was no consistent difference\n    between neurofeedback and delay trials\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 0.1813\n    corrected: Benjamini-Hochberg\n    n: 37 epochs\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 0.5978\n    corrected: Benjamini-Hochberg\n    n: 14 epochs\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 0.0273\n    corrected: Benjamini-Hochberg\n    n: 18 epochs\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 0.6738\n    corrected: Benjamini-Hochberg\n    n: 26 epochs\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.5523\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.2098\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-decode-counts\n  criterion: Per epoch, replay SWRs over all decoded SWRs in the pre-reward period\n    (dfs_ripcontent_vsctrlrats.m part 1), replay defined under the two readings of the header\n    (Replay); tests as in the header, on epochs. Requires decoding the dandisets with the\n    clusterless state space decoder of Denovellis et al. 2021 as in Gillespie et al. 2021. A\n    claim of absence judged on the paper's tests. Reproduced when neither mixed model gives\n    p < 0.05 and at most one rat's corrected ranksum gives p < 0.05.\n- id: fig4e-remote-replay-prereward\n  statement: Remote replay rate in the pre-reward period was much higher on NF than on delay\n    trials, and low on control cohort trials.\n  source: Results, Neurofeedback training preserves replay content during SWRs, paragraph 4;\n    Figure 4E\n  quote: we find much higher rates of remote replay during the pre-reward period in neurofeedback\n    trials compared to delay trials within the manipulation cohort, and low rates of remote replay\n    during this time in trials from the control cohort\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 6.507e-126\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 9.703e-30\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 2.991e-79\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 6.293e-55\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 9.073e-4\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.4304\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-decode-counts\n  criterion: Per-trial count of remote replay SWRs over pre-reward duration\n    (dfs_ripcontent_vsctrlrats.m part 1), tests as in the header, under the two replay readings.\n    Reproduced when all four corrected ranksums give p < 0.05 with NF higher and the NF-control\n    mixed model gives p < 0.05 with NF higher.\n- id: fig4f-remote-replay-combined\n  statement: Over pre- and post-reward periods combined, remote replay rate did not differ between\n    the cohorts for either trial type, and NF trials had slightly but significantly higher rates\n    than delay trials.\n  source: Results, Neurofeedback training preserves replay content during SWRs, paragraph 4;\n    Figure 4F\n  quote: if we consider both the pre-and post-reward periods combined, we find no difference in\n    remote replay rate between the two cohorts for either trial type\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 7.666e-47\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 1.573e-6\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 1.044e-16\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 5.768e-6\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.6644\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.1477\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig4e-remote-replay-prereward\n  criterion: As fig4e-remote-replay-prereward over pre plus post (dfs_ripcontent_vsctrlrats.m\n    part 2). Reproduced when neither mixed model gives p < 0.05 and all four corrected ranksums\n    give p < 0.05 with NF higher.\n- id: fig4g-control-replay-glm\n  statement: In the control cohort, pre-reward remote replay over-represents the previous goal\n    arm, under-represents the immediately previously visited arm and slightly over-represents the\n    upcoming choice arm.\n  source: Figure 4G; Results, Neurofeedback training preserves replay content during SWRs,\n    paragraph 5\n  inferred: Figure 4G plots the control rats' GLM coefficients, and the Results describe the\n    manipulation cohort's pattern as the one \"previously seen in the control cohort\"; no sentence\n    states the control values. The statement reads the pattern of the manipulation cohort\n    sentence onto the control cohort.\n  depends_on:\n  - control-decode-counts\n  criterion: Per control rat, a Poisson GLM (fitglm) of each arm's remote replay count per trial\n    on three binary predictors (previous arm, counting visits during lockouts; future arm; previous\n    goal arm), one row per arm per trial, search and repeat trials from the second goal block on,\n    pre-reward SWRs; fold change exp(beta) with 99% intervals (coefCI(mdl, .01))\n    (Methods, Replay content analysis; dfs_ripcontent_vsctrlrats.m part 3), under the two replay\n    readings. Reproduced when, in all four rats, the previous goal interval lies above 1 and the\n    previous arm interval below 1, and the future arm fold change exceeds 1; partially reproduced\n    when this holds in three rats or the future arm does not exceed 1. Each fold change and\n    interval is reported.\n- id: fig4g-manipulation-replay-glm\n  statement: Within the manipulation cohort, on both NF and delay trials, pre-reward replay\n    over-represented previous goal locations, under-represented the immediately previously visited\n    arm and slightly over-represented the upcoming choice arm, as in the control cohort.\n  source: Results, Neurofeedback training preserves replay content during SWRs, paragraph 5;\n    Figure 4G\n  quote: we observed consistently enhanced representation of previous goal locations in replay\n    events during the pre-reward period in both neurofeedback and delay trials within the\n    manipulation cohort\n  data: elsewhere\n  where: DANDI 000629\n  depends_on:\n  - fig4g-control-replay-glm\n  criterion: As fig4g-control-replay-glm, separately for NF and delay trials of each manipulation\n    rat (expected trial counts 1661, 392, 866 and 1281 NF and 1705, 367, 894 and 1213 delay,\n    Figure 4G legend). Reproduced when the previous goal interval lies above 1 and the previous\n    arm interval below 1 in all eight rat and trial type fits, and the future arm fold change\n    exceeds 1 in most.\n- id: fig4s1-replay-glm-pre-post\n  statement: The replay GLM results are unchanged when replay during both pre- and post-reward\n    time at the center ports is included.\n  source: Results, Neurofeedback training preserves replay content during SWRs, paragraph 5;\n    Figure 4-figure supplement 1\n  quote: These results also remain unchanged when we analyzed replay events during both pre- and\n    post-reward time at the center ports\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - fig4g-manipulation-replay-glm\n  criterion: As fig4g-control-replay-glm and fig4g-manipulation-replay-glm with pre plus post\n    SWRs (dfs_ripcontent_vsctrlrats.m part 4). Reproduced when every fold change has the same\n    side of 1 as in the pre-reward fits, for all twelve rat and trial type fits. The control\n    cohort part can be run on 000115 alone and is reported separately.\n- id: fig5a-search-efficiency\n  statement: Manipulation subjects showed a slight improvement in search efficiency over control\n    subjects, significant only on delay trials, with no difference between NF and delay trials.\n  source: Results, Neurofeedback does not alter behavioral performance in a trial-by-trial manner,\n    paragraphs 2 and 3; Figure 5A\n  quote: The manipulation cohort subjects show a slight improvement in search efficiency compared to\n    control subjects, which only reached significance on delay trials\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 0.9562\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 0.7509\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 0.7509\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 0.9562\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.5425\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.0069\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-decode-counts\n  criterion: Per epoch, among search trials (task phase <= 1), the fraction that are not errors\n    (dfs_ripcontent_vsctrlrats.m part 5), tests as in the header on epochs. Reproduced when no\n    corrected ranksum gives p < 0.05, the delay-control mixed model gives p < 0.05 with the\n    manipulation cohort higher, and the NF-control mixed model does not.\n- id: fig5s1-control-search-efficiency-increases\n  statement: In the control cohort, search efficiency tends to increase over behavioral epochs.\n  source: Figure 5-figure supplement 1; Results, Neurofeedback does not alter behavioral\n    performance in a trial-by-trial manner, paragraph 2\n  quote: For the control cohort, search efficiency tends to increase over behavioral epochs\n  depends_on:\n  - control-decode-counts\n  criterion: Per control rat, each epoch's fraction of search trials (task phase <= 1) that are\n    not errors (fractional phase below 0.85), against the epoch's order over the selected epochs\n    (gooddecode epochs, as the figure is made from the content analysis output), Pearson\n    correlation (dfs_ripcontent_vsctrlrats.m part 5, which prints r squared and p). The paper\n    reports no statistic; the text calls it \"a subtle but consistent increase\". Reproduced when r\n    is positive in all four rats; partially reproduced in three. As a variant, the epochs of\n    control-cohort-trial-counts.\n- id: fig5b-redundant-search-balanced\n  statement: Redundant search trials were not biased toward either trial type; NF trials made up\n    about half of them in each subject.\n  source: Results, Neurofeedback does not alter behavioral performance in a trial-by-trial manner,\n    paragraph 3; Figure 5B\n  quote: neurofeedback trials accounted for approximately half of redundant search trials for each\n    subject\n  statistics:\n  - about: rat1\n    test: two-sided sign test against 0.5\n    p: 0.1102\n    n: 37 epochs\n  - about: rat2\n    test: two-sided sign test against 0.5\n    p: 0.2668\n    n: 14 epochs\n  - about: rat3\n    test: two-sided sign test against 0.5\n    p: 1\n    n: 18 epochs\n  - about: rat4\n    test: two-sided sign test against 0.5\n    p: 1\n    n: 26 epochs\n  data: elsewhere\n  where: DANDI 000629\n  criterion: Per epoch, the fraction of redundant search trials (search error trials) that are NF\n    trials; sign test against 0.5 (dfs_ripcontent_vsctrlrats.m part 5). A claim of absence judged\n    on the paper's test. Reproduced when no rat gives p < 0.05.\n- id: fig5c-repeat-accuracy-unchanged\n  statement: On repeat trials the fraction of correct goal visits did not differ between the\n    cohorts or between NF and delay trials.\n  source: Results, Neurofeedback does not alter behavioral performance in a trial-by-trial manner,\n    paragraph 4; Figure 5C\n  quote: We also saw no difference between the two cohorts or between neurofeedback and delay trials\n    on this measure\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 0.7202\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 0.7202\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 0.8123\n    corrected: Benjamini-Hochberg\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 0.7202\n    corrected: Benjamini-Hochberg\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 0.6946\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 0.2857\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-decode-counts\n  criterion: Per epoch, among repeat trials (task phase > 1), the fraction that are not errors\n    (dfs_ripcontent_vsctrlrats.m part 5); tests as in the header on epochs. A claim of absence\n    judged on the paper's tests. Reproduced when no test gives p < 0.05.\n- id: fig5d-repeat-errors-balanced\n  statement: Within the manipulation cohort, repeat error trials were equally distributed between\n    NF and delay trials.\n  source: Results, Neurofeedback does not alter behavioral performance in a trial-by-trial manner,\n    paragraph 4; Figure 5D\n  quote: error trials, when subjects do not choose to visit a known goal arm, were equally\n    distributed between neurofeedback and delay trials\n  statistics:\n  - about: rat1\n    test: two-sided sign test\n    p: 0.3770\n  - about: rat2\n    test: two-sided sign test\n    p: 0.7744\n  - about: rat3\n    test: two-sided sign test\n    p: 1\n  - about: rat4\n    test: two-sided sign test\n    p: 0.0227\n  data: elsewhere\n  where: DANDI 000629\n  criterion: Per epoch, the fraction of repeat error trials that are NF trials; sign test against\n    0.5 (dfs_ripcontent_vsctrlrats.m part 5). The paper states equality while one rat's\n    uncorrected p is 0.0227. Judged on the paper's test as printed. Reproduced when the same\n    pattern holds, at most one rat with p < 0.05; the fractions are reported.\n- id: fig1s1c-prereward-dwell-matched\n  statement: Time spent at the center ports before reward was approximately matched between NF\n    and delay trials by the yoked delay design.\n  source: Results, A neurofeedback paradigm to promote SWRs, paragraph 3; Figure 1-figure\n    supplement 1C\n  quote: such that the amount of time spent waiting at each of the center ports was approximately\n    matched\n  statistics:\n  - about: NF against delay, rat1\n    test: ranksum\n    p: 0.228\n  - about: NF against delay, rat2\n    test: ranksum\n    p: 0.690\n  - about: NF against delay, rat3\n    test: ranksum\n    p: 0.005\n  - about: NF against delay, rat4\n    test: ranksum\n    p: 0.002\n  - about: manipulation NF against control\n    test: linear mixed-effects model\n    p: 2.936e-9\n  - about: manipulation delay against control\n    test: linear mixed-effects model\n    p: 2.178e-5\n  data: elsewhere\n  where: DANDI 000629 (manipulation cohort); the control cohort is in 000115\n  depends_on:\n  - control-cohort-trial-counts\n  criterion: Per-trial pre-reward duration, RWstart to RWend (dfs_rips_vsctrlrats.m part 6).\n    \"Approximately matched\" is not quantified; the paper's own tests find differences in two\n    rats. Reproduced when the per-rat median NF and delay durations differ by less than 10% in\n    all four rats (a threshold chosen here, as the paper gives none), with the ranksum and\n    mixed model p-values reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/gillespie-2024.yaml paper/10.7554-elife.90944.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE "^\s+[^#].*: .*: " claims/gillespie-2024.yaml; grep -nE "^\s{4,}[^-#].*: " claims/gillespie-2024.yaml | grep -vE "^\S+:\s+(quantity|value|tolerance|unit|about|test|p|corrected|n|statistic|p_relation): " | head; grep -n "—\|rather" claims/gillespie-2024.yaml
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -n " - " claims/gillespie-2024.yaml
```

```
20:#   - Control cohort (rats jaq, roquefort, despereaux and montague, in that order in every legend
24:#   - Manipulation (neurofeedback) cohort (remy, gus, bernard and fievel, rat1 to rat4): one center
44:#   - Epochs (dfs_rips_vsctrlrats.m). Control cohort, Figures 2 and 3 and their supplements:
48:#   - Trials (dfa_ripquantpertrial_allphase_NF.m): trials with no lockout and leavehome > 0, or with
53:#   - SWRs: offline consensus detection as in the Methods (150 to 250 Hz, squared, summed over CA1
58:#   - Speed: the per-trial mean of the position structure's smoothed velocity (column 9) over the
60:#   - Within-subject NF against delay: Wilcoxon rank-sum per rat, Benjamini-Hochberg over the four
66:#   - Replay (dfa_ripcontent_nf.m, dfs_ripcontent_vsctrlrats.m): an SWR is replay when its
72:#   - Task phase of a trial: label_trial_interval.m of Gillespie et al. 2021 (search trials have
91:  - quantity: jaq trials
94:  - quantity: roquefort trials
97:  - quantity: despereaux trials
100:  - quantity: montague trials
118:  - quantity: jaq epochs
121:  - quantity: roquefort epochs
124:  - quantity: despereaux epochs
127:  - quantity: montague epochs
130:  - quantity: jaq trials, Figure 4E
133:  - quantity: roquefort trials, Figure 4E
136:  - quantity: despereaux trials, Figure 4E
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "only \"2 sd above the behavioral epoch mean\" -" claims/gillespie-2024.yaml; sed -i 's/meanvel). Open - the smoothing/meanvel). Open, as the smoothing/; s/say only "2 sd above the behavioral epoch mean" -$/say only "2 sd above the behavioral epoch mean";/' claims/gillespie-2024.yaml; grep -n "epoch mean\"\|Open, as the smoothing" claims/gillespie-2024.yaml; python tools/claims_check.py claims/gillespie-2024.yaml paper/10.7554-elife.90944.txt 2>&1 | tail -1
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/gillespie-2024.yaml` and did not commit it. The quote checker passes on every quote. It still lists 6 "problems": p-values the paper prints with trailing zeros (for example "6.790 × 10 –7"). I found each one in the text by reading.

**What I read**
- The version of record (eLife RP90944, PMC11221834), in `paper/10.7554-elife.90944.txt`. It holds the main text, Methods, and all figure and figure-supplement legends inline. I did not open the PDF.
- The paper's code: github.com/LorenFrankLab/Gillespie_eLife_2024 at commit ad5801a, the revision the paper cites. Its README map is out of date for Figure 2–figure supplement 1F–H, which I noted in the file.

**Counts**
- 35 claims: 33 findings and 2 `link` checks on the control cohort's trial and epoch counts.
- 34 have quotes. The other one (the control cohort's replay GLM, Fig 4G) is marked `inferred`.
- 27 claims carry statistics (112 values in all), 7 have expected values, and all 35 have criteria.

**Which data the claims need**
- DANDI 000115 holds only the control cohort (jaq, roquefort, despereaux, montague).
- The neurofeedback cohort is in DANDI 000629, which is not this record's dataset. So 26 claims are `data: elsewhere`, with `where:` naming 000629, plus 000115 for the cohort comparisons.
- 9 claims can be tested on 000115 alone:
  - control trial, epoch and SWR counts
  - control SWR rate rising after reward (Fig 2B, Fig 2–S1F)
  - control post-reward dwell time increasing over epochs (Fig 2–S1H)
  - control head speed below 4 cm/s (Fig 3A)
  - control replay GLM (Fig 4G)
  - control search efficiency increasing over epochs (Fig 5–S1)

**Details the paper leaves open, and the readings I named**
- **Control epoch flags** (ripthresh, environment, forageassist, gooddecode): the code fixes them. If the dandiset lacks the flags, the readings are (a) all full-task run epochs, or (b) those minus forage-assist and no-delay epochs.
- **SWR detection baseline**: the mean and sd are taken over (a) the whole epoch or (b) immobile times. The detector itself is not in the repository.
- **Head speed**: (i) the speed the dandiset provides or (ii) speed recomputed from the LED position with standard smoothing; and the per-rat value as (a) the median or (b) the mean over trials.
- **Replay class**: the Methods' "continuous model probability > 0.8" against the code's `max_state == 1`.
- **Trial-wise pre/post SWR-count correlation**: (a) all trials pooled, (b) NF trials pooled, or (c) the median of per-epoch r. The code computes it per epoch; the text gives one r per rat.
- **"No extended suppression"** (Fig 2–S1G): two thresholds named.
- **"Approximately twice" / "half as long"**: the code's inset ratios, with ratio-of-means variants.

**Thresholds I chose because the paper gives none**
- Tolerance 0.3 on "approximately twice" (pre-reward SWR rate), 0.5 on "roughly twice" (per-size fold change), 0.1 on "half as long" (dwell time).
- A 5 s post-reward window for comparing the two cohorts' time courses.
- A 10% median difference for "approximately matched" pre-reward dwell time.

**Missing**
- Nothing the claims need is missing from the paper.
- The SWR detector, position processing, `label_trial_interval.m` and the decoder are not in the paper's repository. The criteria point to Gillespie et al. 2021 for the task-phase labels.
- The trigger delays disagree: the Methods and code give 75/100/50/50 ms, the Figure 1–figure supplement 1B legend 100/50/75/75 ms. I recorded this in the header; no claim rests on it.

## End of run

26 turns, 6 minutes, $2.74 at API prices, result: success.
