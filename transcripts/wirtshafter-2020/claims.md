# wirtshafter-2020 · claims · run 42934434978

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; cat papers/datasets/wirtshafter-2020.yaml; cat paper/hc-29.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55252.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55252.txt",
 "offset": 162
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text (version of record, PMC7274787, with figure supplements) is present. Next I'll read the linked code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --quiet https://github.com/hsw28/data_analysis 2>&1 | tail -3; cd data_analysis && git log -1 --format='%H %ci' && ls | head -50 && git ls-files | wc -l
```

```
d0ea9e54aff07c5fbb1be7729e57872b2af7426c 2024-02-06 18:53:27 -0600
README.md
hannah-in-use
license.txt
others_analysis_code
5006
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --quiet https://github.com/elifesciences-publications/data_analysis elife_da 2>&1 | tail -3; cd elife_da && git log -1 --format='%H %ci' && ls && cat README.md | head -60; ls hannah-in-use | head -80
```

```
5c6320a9133b8ac551300efdd7abbbc44767c575 2020-06-04 16:47:01 +0100
README.md
hannah-in-use
license.txt
others_analysis_code
# data_analysis
go into specific folders for read mes

This code is associated with the paper from Wirtshafter and Wilson, "Differences in reward biased spatial representations in the lateral septum and hippocampus". eLife, 2020. http://doi.org/10.7554/eLife.55252
README.txt
deprecated
include
inprep
matlab
mwl_steps
other
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use && cat README.txt | head -80; ls matlab | head; find . -iname "*.m" | wc -l; find . -iname "*.m" | grep -iE "bits|skew|frai|field|xcorr|crosscor|placefield|mutual|septum|LS" | head -80
```

```
READ ME LAST UPDATED in EARLY 2018. UPDATES NEEDED

Contents:

MATLAB
FILTERING
deltafilt.m: lowpass filters in the delta band (<4)
filter812.m: filters in 8-12hz
gammafilt.m: bandpass filters in the gamma band (20-100)
hightheta.m: bandpass filters 7-12hz
lowpass4.m: lowerpass filters below 4
lowpass20.m: lowpass filters below 20
lowpass50.m: lowpass filters below 50
lowpass300.m: lowpass filters below 300
lowtheta.m: bandpass filters 3-6
ripfilt.m: bandpass filters in the ripple band (100-300)
thetafilt.m: bandpass filters in the theta band (6-10)

FANCIER FILTERING
findrip.m: takes eeg data from gh_debuffer and returns times of ripple peaks
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use && find . -iname "*.m" | grep -iE "place|skew|frai|cross|center|field|bits|poiss|fake|accur|lap|choice|forced|arm|chunk" ; ls matlab/bulk matlab/decode_pos
```

```
./include/CircStat2012a/circ_skewness.m
./include/pointbinned/CrossSpecMatpb.m
./matlab/centerdirection.m
./matlab/bulk/MASSplacefieldnumDIRECTIONAL_resid.m
./matlab/bulk/MASSCHUNKvelVsFiringRate.m
./matlab/bulk/MASSplacefieldnumDIRECTIONAL.m
./matlab/bulk/MASSplacefieldnum.m
./matlab/bulk/MASSchunkingruns.m
./matlab/bulk/MASS_crosscorrLSHPC3.m
./matlab/bulk/MASS_crosscorrLSHPC.m
./matlab/bulk/MASSplacefieldnumDIRECTIONALtrials.m
./matlab/bulk/MASSCHUNKcorrFiringRate.m
./matlab/bulk/MASSCHUNKaccVsFiringRate.m
./matlab/bulk/MASSplacefieldnum_resid.m
./matlab/STAfake.m
./matlab/filtering/thetaRMS.m
./matlab/spikecrosstabs.m
./matlab/accelVsFiringRateCHUNK.m
./matlab/decode_pos/bitspersec_resid.m
./matlab/decode_pos/bitsperspike_shuff.m
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && cat decode_pos/bitsperspike.m bulk/MASSplacefieldnum.m; grep -rln "skew" --include=*.m . | head; grep -rln "fieldcenter\|placefield(" --include=*.m . | head -20
```

```
function f = bitsperspike(posstructure, clusters, dim)
%outputs name, bits per spike, and mean firing rate normalized by position

%determine how many spikes & pos files
tic

bigXall = [];
bigYall = [];
clustspikenames = (fieldnames(clusters));
spikenum = length(clustspikenames);

posnames = (fieldnames(posstructure));
posnum = length(posnames);
pnames = {};
for s = 1:posnum
  if contains(posnames(s), 'position')==1
    pnames(end+1) = (posnames(s));
  end
end

[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && wc -l bulk/MASSplacefieldnumDIRECTIONAL.m bulk/MASS_crosscorrLSHPC*.m bulk/CCpairs.m bulk/MASSspiketrainCC.m decode_pos/bitsperspike_shuff.m decode_pos/bitspersec.m decode_pos/MASSmutualinfo.m bulk/MASSplacefieldnumDIRECTIONALtrials.m bulk/MASSfiringvdistance.m; diff <(sed -n 1,400p bulk/MASSplacefieldnum.m) bulk/MASSplacefieldnumDIRECTIONAL.m | head -300
```

```
619 bulk/MASSplacefieldnumDIRECTIONAL.m
   378 bulk/MASS_crosscorrLSHPC.m
   557 bulk/MASS_crosscorrLSHPC3.m
   404 bulk/CCpairs.m
    93 bulk/MASSspiketrainCC.m
   218 decode_pos/bitsperspike_shuff.m
   184 decode_pos/bitspersec.m
   113 decode_pos/MASSmutualinfo.m
   515 bulk/MASSplacefieldnumDIRECTIONALtrials.m
   109 bulk/MASSfiringvdistance.m
  3190 total
1c1
< function [f allsizescenters tempz] = MASSplacefieldnum(clusters,posstructure, dim)
---
> function [f allsizescenters shuffledskew] = MASSplacefieldnumDIRECTIONAL(clusters,posstructure, dim)
3c3
<      set(0,'DefaultFigureVisible', 'off');
---
>       %set(0,'DefaultFigureVisible', 'off');
5,6d4
[... 292 more lines not kept]
```

**Agent**

Code read so far: bits/spike and place field detection settle bin sizes, thresholds and location boxes. Now the directional skew and cross-correlation code.

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && sed -n 330,619p bulk/MASSplacefieldnumDIRECTIONAL.m | grep -v "^\s*%" | grep -v "^\s*$" | head -230
```

```
numfields = numfields+1;
        [centerY, centerX] = ind2sub(size(chartmax),cell2mat(CC.PixelIdxList(z)));
        xbins = ceil((xmax)/psize);
        ybins = ceil((ymax)/psize);
        newchart = zeros(size(chart));
        newchart(centerY, centerX) = chart(centerY, centerX);
        M = max(newchart, [], 'all');
        [centerYmax, centerXmax] = find(newchart==M);
        centerYmax = ybins-centerYmax; %here?
        newchart(find(newchart==0))=NaN;
        newspikegraph  = zeros(size(chart));
        newtimegraph  = zeros(size(chart));
        newspikegraph(centerY, centerX) = spikegraph(centerY, centerX);
        newtimegraph(centerY, centerX) = timegraph(centerY, centerX);
        newspikegraph(find(newspikegraph==0))=NaN;
        newtimegraph(find(newtimegraph==0))=NaN;
        centerXmean = nanmean(centerX);
        centerYmean = nanmean(centerY);
        centerYmean = ybins-centerYmean;
        centerXmean = (xmax)./xbins * centerXmean;
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && sed -n 1,40p bulk/CCpairs.m; grep -n "xcorr\|shuff\|randperm\|20\b\|<=20\|<20\|binsize\|\.01\|lag\|function" bulk/CCpairs.m bulk/MASS_crosscorrLSHPC3.m bulk/MASSspiketrainCC.m | head -60
```

```
function f  = CCpairs(fieldchartHPC_dir, fieldchartLS_dir, HPCclusters, LSclusters, posstructure)
%if lag is positive, then Y is delayed relative to x
%makes pairs of LS and HPC cells based on place field proximity and finds CC

test = 0;

figure
HPCfieldchart = fieldchartHPC_dir(2:end, :);
LSfieldchart = fieldchartLS_dir(2:end, :);
HPCfieldnames = (HPCfieldchart(:,1));
LSfieldnames = (LSfieldchart(:,1));
LSnums = [1:1:length(LSfieldnames)];

HPCclustnames = (fieldnames(HPCclusters));
HPCclustnum = length(HPCclustnames);
LSclustnames = (fieldnames(LSclusters));
LSclustnum = length(LSclustnames);

posnames = (fieldnames(posstructure));
posnum = length(posnames);
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && sed -n 60,200p bulk/CCpairs.m
```

```
endminusaverage = [];
endplusaverage = [];
endmaxes = [];
endmaxtime = [];

disALL = [];
for q = 1:length(pnames)
  currentname = char(pnames(q))
  posData = posstructure.(currentname);
  posData = fixpos(posData); %positions, not sure if needed
  posTime = posData(:,1);
  % get date of spike
  date = strsplit(currentname,'date_'); %splitting at year rat12_2018_08_20_time
  date = char(date(1,2));
  date = strsplit(date,'_position'); %rat12_2018_08_20
  date = char(date(1,1));


  %ELIGILE HPC
  HPCcurrentclusts = struct;
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && sed -n 244,330p bulk/CCpairs.m | grep -v "^\s*$"; cat spiketrain.m 2>/dev/null | head -30 || find . -name spiketrain.m
```

```
test = test+1;
  dir(end+1) = currentdir;
  CCshuffled = crosscorr(HPCtrain, LStrain(randperm(length(LStrain))), 'NumLags', binzzz); %bins are 10ms, so 100ms is 10 on each side
  notallaverage(end+1) = nanmean(CCshuffled);
  notminusaverage(end+1) = nanmean(CCshuffled(1:binzzz));
  notplusaverage(end+1) = nanmean(CCshuffled(binzzz:end));
  notmaxes(end+1) = max(CCshuffled);
%no close matches
else
  test = test+1;
  dir(end+1) = NaN;
  allaverage(end+1) = NaN;
  minusaverage(end+1) = NaN;
  plusaverage(end+1) = NaN;
  maxes(end+1) = NaN;
  notallaverage(end+1) = NaN;
  notminusaverage(end+1) = NaN;
  notplusaverage(end+1) = NaN;
  notmaxes(end+1) = NaN;
  maxtime(end+1) = NaN;
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && grep -n "poiss\|rand\|shuff" decode_pos/bitsperspike_shuff.m | head; grep -rln -i "poiss" --include=*.m . | head; sed -n 1,30p bulk/MASSplacefieldnumDIRECTIONALtrials.m | grep -v "^\s*$"; grep -n "15\|20\|lap\|trial" bulk/MASSplacefieldnumDIRECTIONALtrials.m | head -40; grep -rn "dim" decode_pos/MASSmutualinfo.m | head -5; grep -rln "bitsperspike(\|MASSplacefieldnumDIRECTIONAL(" . | head
```

```
1:function f = bitsperspike_shuff(posstructure, clusters, dim)
./makeSpikes.m
function [f mindistall]= MASSplacefieldnumDIRECTIONALtrials(clusters,posstructure, dim, fieldchart)
%outputs location of each spike around field center as defined from MASSplacefieldnumDIRECTIONAL
%fieldchart is output from MASSplacefieldnumDIRECTIONAL
%output is:
% f is a structure for each place cell with each structure (a,b,c) where a is each spike, c is the lap number, and b is time, x pos, y pos, velocity
% mindistall is a (:,4) matrix where columns:
  %1 is the time the animal passes by center as defined by MASSplacefieldnumDIRECTIONAL
  %2 is the distance from the center
  %3 is the X of max spiking for that lap
  %4 is the Y of max spiking for that lap
set(0,'DefaultFigureVisible', 'off');
%determine how many spikes & pos files
allsizes = [];
allcenterXmean = [];
allcenterYmean = [];
allcenterXmax = [];
allcenterYmax = [];
allskew = [];
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/elife_da/hannah-in-use/matlab && sed -n 50,113p decode_pos/MASSmutualinfo.m | grep -v "^\s*$" ; cat mutualinfo.m | grep -v "^\s*$" | head -50
```

```
%Sum of (occprobs * mean firing rate per bin) * log2 (mean firing rate per bin / overall mean rate)
  psize = 3.5 * dim;
  xvals = posData(:,2);
  yvals = posData(:,3);
  xmin = min(posData(:,2));
  ymin = min(posData(:,3));
  xmax = max(posData(:,2));
  ymax = max(posData(:,3));
  xbins = ceil((xmax-xmin)/psize); %number of x
  ybins = ceil((ymax-ymin)/psize); %number of y
  xinc = xmin +(0:xbins)*psize; %makes a vectors of all the x values at each increment
  yinc = ymin +(0:ybins)*psize; %makes a vector of all the y values at each increment
  velthreshold = 12;
  vel = velocity(posData);
  vel(1,:) = smoothdata(vel(1,:), 'gaussian', 30); %originally had this at 30, trying with 15 now
  fastvel = find(vel(1,:) > velthreshold);
  totaltime = length(fastvel)./30;
  posDataFast = posData(fastvel, :);
  xvalsFast = posDataFast(:,2);
  yvalsFast = posDataFast(:,3);
[... 50 more lines not kept]
```

**Agent**

I have what I need from the code (eLife archive copy, commit 5c6320a). Now checking the schema used for a CRCNS dataset before writing.

**Agent calls Bash**

```bash
cd  git log --name-only -5 --format=%s | grep claims; ls claims | wc -l; grep -l "archive: crcns" claims/*.yaml | head -3; f=$(grep -l "archive: crcns" claims/*.yaml | head -1); sed -n 1,40p $f; sed -n 1,60p tools/claims_check.py | head -60
```

```
288
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,80p claims/bruno-2017.yaml; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
# eigenvalue.
#
# Places where the code and the Methods differ, each named again in the claims it touches:
# (1) the Gaussian SD: the Methods give the median ISI divided by 12 (or its square root, if the
# extraction lost it); the code uses the median ISI itself, and computes it from the post-onset
# ISIs of all recordings of the same stimulation number read so far, not of the recording alone;
# (2) the number of PCs: the Methods say at least 80% of variance; the recurrence code keeps the
# PCs whose cumulative variance is at most 80% (sum(prctVar <= 0.8)), the manifold code the
# smallest number reaching at least 80%; (3) the dominant period: the Methods and Figure 2F say
# the mean recurrence time of the dominant peak, the code stores and plots the median;
# (4) P10 decoding: the Methods fit 40 s windows stepped by 1 s with histories 50 to 200 ms; the
# code trains on 50% of the post-33 s series, steps 0.2 s, and tries histories 50 to 250 ms;
# (5) the period-change permutation test: 10000 permutations in the Methods, 100000 in the code,
# which permutes the pooled time and period values and is one-sided in the direction of rho.
# Following the protocol, the Methods are the main reading and the code's choice is a variant.
#
# Data the paper used. Aplysia californica, isolated cerebral, pleural and pedal ganglia (15 to
# 17 C). Voltage-sensitive dye RH-155 imaged with a 464-element photodiode array at 1600 Hz over
# the dorsal pedal ganglion, bandpassed 5 to 100 Hz and spike-sorted by independent component
# analysis. 10 preparations, three evoked bouts of fictive locomotion each (30 evoked population
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(list(s['properties']))"
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
[... 83 more lines not kept]
```

**Agent**

I've read the paper and the code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/wirtshafter-2020.yaml",
 "content": "# Claims for Wirtshafter & Wilson (2020), eLife 9:e55252, \"Differences in reward biased spatial\n# representations in the lateral septum and hippocampus\", doi:10.7554/elife.55252, on CRCNS data set\n# hc-29 (doi:10.6080/K0NG4NV8).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC7274787, open access), as JATS XML flattened to text under\n# paper/: main text, Materials and methods, the legends of Figures 1 to 7 and of all their figure\n# supplements (Figure 2 S1, Figure 3 S1 and S2, Figure 5 S1 to S5, Figure 6 S1 and S2, Figure 7 S1\n# to S3). The paper has no other supplementary file. No PDF was supplied; no claim rests on a\n# number shown only in a figure. The extraction garbles the bits/spike formula (its letters are\n# spaced out) and the FRAI formula (\"FRAI = F1 F2 / (F1+F2)\", the minus sign lost); the code settles\n# the second. The data set's description (paper/hc-29.data-description.txt) was read only to know\n# what it holds: sorted spike times of LS and HPC units, one file per region, labelled by session\n# date, tetrode and cluster, and \"time files for all sessions\". It does not name position data.\n#\n# Code read: https://github.com/elifesciences-publications/data_analysis, commit 5c6320a9\n# (2020-06-04), the eLife archived copy linked from Data and code availability (MATLAB; the live\n# repository github.com/hsw28/data_analysis is at d0ea9e54, 2024-02-06, and was not used). In\n# hannah-in-use/matlab: decode_pos/bitsperspike.m, bitspersec.m and MASSmutualinfo.m (with\n# mutualinfo.m) the information measures; bulk/MASSplacefieldnum.m the place fields, their sizes,\n# centres and location classes; bulk/MASSplacefieldnumDIRECTIONAL.m the fields split by direction\n# of travel, skew, FRAI and the shuffled skew; bulk/MASSplacefieldnumDIRECTIONALtrials.m the lap by\n# lap analysis; bulk/CCpairs.m the HPC-LS pairing and cross-correlations; spiketrain.m the binned\n# trains. No script in the archive generates the Poisson units of Figure 2B or runs the speed and\n# acceleration regression of Figure 3 S1 under a name that says so; makeSpikes.m exists and was not\n# confirmed to be the one used.\n#\n# Method, from the Methods unless the code is named. Position at about 30 Hz (often about 15 Hz\n# from occlusion). Speed is the distance between the positions just before and just after a time\n# point, smoothed with a Gaussian of 1 s SD, in cm/s (Methods; the code smooths with\n# smoothdata(..., 'gaussian', 30), a 30-sample window, a variant). Only occupancy and spikes at\n# speed of 12 cm/s or more are used (the code uses > 12). Rate maps are occupancy-normalised, in\n# 1 cm bins for bits/spike and bits/s and 2 cm bins for place fields, smoothed with a Gaussian of\n# 10 cm SD (code: bins of 3.5 * dim pixels, so 3.5 pixels per cm; empty bins interpolated by\n# chartinterp before ndnanfilter smoothing). Bits/spike = sum_i P_i (R_i/R) log2(R_i/R) and\n# bits/s = sum_i P_i R_i log2(R_i/R), P_i the occupancy probability, R_i the bin rate, R the mean\n# rate (in the code, the mean of the rate map). Cells with mean rate below 0.05 Hz above the speed\n# threshold are dropped. Mutual information as in Ego-Stengel and Wilson 2007; in the code, the\n# mutual information between x and y of the smoothed rate map normalised to a joint distribution.\n# Place field (Results paragraph 4, Methods, MASSplacefieldnum.m): bins of the smoothed 2 cm map\n# with rate at or above mean + 1 SD of the map's bins (the Methods print \"equal to or less than\",\n# which the Results and the code contradict), connected on the four sides, with a peak above mean\n# + 2 SD and a length of at least 15 cm (code: the larger of the field's row and column extents\n# times the bin size, the two arms summed near the corners). The centre is the bin of highest rate.\n# Location classes (code, pixel boxes): forced sides (left and right forced arms and their ends),\n# forced point, centre stem, choice point, choice sides (choice arms and their ends); the forced\n# and choice points are left out of the location counts. Direction (MASSplacefieldnumDIRECTIONAL.m):\n# spikes are split by the sign of the velocity along each arm or the stem, toward reward meaning\n# toward the choice ends; each direction's map uses the direction's spikes over all fast\n# occupancy. A cell with fields in both directions whose centres are less than 20 cm apart is\n# bidirectional. Skew (Methods; code) is the third moment of the field's rate profile along the\n# track, the width averaged, over the cube of its SD. Cross-correlation (Methods; CCpairs.m): each\n# HPC field is matched to the LS field of the same session and direction whose centre is within\n# 20 cm, the one with the closest mean in-field rate if several; spike trains in 10 ms bins over the\n# whole session, MATLAB crosscorr over +-10 lags (+-100 ms); a cross-correlation with a randomly\n# permuted LS train is subtracted; a pair's location is that of the HPC field centre. HPC leads at\n# positive lags (CCpairs.m comment).\n#\n# Places where the code and the Methods differ, each named again where it matters: (1) speed\n# smoothing (above); (2) the Methods drop cells with a maximum rate below 0.05 Hz, the code drops\n# fields of cells with a maximum map rate below 0.5 Hz; (3) the track coverage rule: the Results\n# exclude sessions where the animal did not cover the whole track at 12 cm/s or more; the code\n# keeps a session when its 5 cm occupancy chart has at least 1950 bins, counted as written over all\n# bins, visited or not; (4) in CCpairs.m the per-pair average stored is the mean of the raw\n# cross-correlation, the shuffle-subtracted traces being kept apart, while the Methods subtract the\n# shuffle. The Methods are the main reading; the code's choice is a variant.\n#\n# Data the paper used. Six male Long-Evans rats, each with two 16-tetrode arrays, one in dorsal CA1\n# and one in caudodorsal lateral septum, recorded simultaneously; 452 LS and 178 CA1 units; one\n# 30 min session a day on a double-sided (end to end) T maze with a forced phase (one side of one T\n# blocked) and a free choice phase (the same side of the opposite T rewarded with sucrose and\n# chocolate milk). Measured variables: spike times of sorted units, overhead-camera position at\n# about 30 Hz, and from them speed, direction of travel and arm. The analyses use position for\n# every claim; the data set's description names spikes and time files only, so whether position is\n# held is for the author to find.\nschema_version: 2\npaper: doi:10.7554/elife.55252\nclaims:\n- id: units-recorded\n  statement: 452 caudodorsal LS units and 178 CA1 units were recorded in six rats, of which 165 CA1\n    and 378 LS cells met the spike rate and track coverage criteria.\n  source: Results, opening paragraph; Results, Place fields are less abundant, paragraph 5\n  quote: we recorded the activity of 452 caudodorsal LS units and 178 CA1 hippocampus units in six\n    male Long Evans rats\n  expected:\n  - quantity: LS units recorded\n    value: 452\n    tolerance: 45\n  - quantity: CA1 units recorded\n    value: 178\n    tolerance: 18\n  - quantity: CA1 cells meeting rate and coverage criteria\n    value: 165\n    tolerance: 17\n  - quantity: LS cells meeting rate and coverage criteria\n    value: 378\n    tolerance: 38\n  criterion: Units are counted from the data set's sorted clusters by region. The criteria are a\n    mean rate of at least 0.05 Hz above 12 cm/s and full track coverage (Results paragraph 1 of the\n    first section; Methods, Bits/spike). What full coverage means is open; the readings are\n    (a) the code's rule (a session's 5 cm occupancy chart has at least 1950 bins, as written in\n    bitsperspike.m) and (b) every arm, the stem and both T junctions visited at 12 cm/s or more in\n    the session. Reproduced when the four counts are within tolerance under one reading.\n- id: fig2ab-fraction-spatial\n  statement: 75.2% (124/165) of CA1 cells and 33.6% (127/378) of LS cells reach at least 0.8\n    bits/spike.\n  source: Results, Place fields are less abundant in the LS, paragraph 1; Figure 2A-B\n  quote: We found that 75.2% (124/165) of CA1 cells ( Figure 2A ) and 33.6% (127/378) of LS cells (\n    Figure 2B ) met or exceeded the 0.8bits/spike threshold\n  depends_on:\n  - units-recorded\n  expected:\n  - quantity: fraction of CA1 cells at or above 0.8 bits/spike\n    value: 75.2\n    tolerance: 7.5\n    unit: '%'\n  - quantity: fraction of LS cells at or above 0.8 bits/spike\n    value: 33.6\n    tolerance: 3.4\n    unit: '%'\n  criterion: Bits/spike as in the Methods on 1 cm maps above 12 cm/s, smoothed with a 10 cm SD\n    Gaussian, for the cells of units-recorded. The next paragraph of the Results speaks of \"164 HPC\n    units with bits/spike greater than or equal to 0.8\"; 124 of 165 agrees with 75.2%, so 124 is\n    taken as the count and 164 as a misprint, a reading recorded here before the analysis.\n- id: fig2c-bits-per-spike\n  statement: CA1 cells carry more spatial information per spike than LS cells (mean 1.54 against\n    0.73 bits/spike).\n  source: Results, Place fields are less abundant in the LS, paragraph 1; Figure 2C\n  quote: with the average bits/spike of a CA1 cell significantly higher than the average\n    bits/spike of an LS cell (HPC mean 1.54+−1.2 bits/spike, LS mean 0.73+−0.7 bits/spike,\n    two-tailed two sample t-test t(541)=9.42, p<0.001)\n  statistics:\n  - test: two-tailed two sample t-test\n    statistic: t(541)=9.42\n    p: 0.001\n    p_relation: <\n    n: 165 CA1 and 378 LS cells\n  depends_on:\n  - units-recorded\n  expected:\n  - quantity: mean CA1 bits/spike\n    value: 1.54\n    tolerance: 0.15\n  - quantity: mean LS bits/spike\n    value: 0.73\n    tolerance: 0.07\n  criterion: Tolerances are 10% of the means; the printed +- values (1.2, 0.7) are the SD across\n    cells, not an uncertainty of the mean. Reproduced when both means are within tolerance and a\n    two-tailed two sample t-test of CA1 against LS bits/spike gives p < 0.001 with CA1 higher.\n- id: fig2b-poisson-control\n  statement: Artificial LS units firing as Poisson processes at the recorded LS units' mean rates\n    carry less spatial information than the recorded units (mean 0.43 against 0.73 bits/spike;\n    7.96% above 0.8), and their bits/spike distribution differs from the recorded one.\n  source: Results, Place fields are less abundant in the LS, paragraph 1; Figure 2B inset and legend\n  quote: The distribution of the bits/spike for the artificial units was highly significantly\n    different than the distribution of bits/spike for actual units (KS test, p<10 −15 ), and only\n    7.96% of artificial units had bits/spike measurements of greater than 0.8. The average\n    bits/spike for the artificial units was 0.43\n  statistics:\n  - about: artificial against recorded LS bits/spike distributions\n    test: KS test\n    p: 1.0e-15\n    p_relation: <\n  - about: artificial against recorded LS mean bits/spike\n    test: two-tailed two sample t-test\n    statistic: t(818)=6.72\n    p: 1.0e-10\n    p_relation: <\n    n: 454 artificial units and the recorded LS units\n  depends_on:\n  - fig2c-bits-per-spike\n  expected:\n  - quantity: fraction of artificial units above 0.8 bits/spike\n    value: 7.96\n    tolerance: 0.8\n    unit: '%'\n  - quantity: mean bits/spike of artificial units\n    value: 0.43\n    tolerance: 0.043\n  criterion: The paper says only that 454 artificial units were made \"using Poisson firing and the\n    mean firing rates of the recorded LS units\"; no script for it was found in the code. Open, and\n    could change the outcome. Readings (a) a homogeneous Poisson train at each LS unit's mean rate\n    over the whole session, bits/spike then computed exactly as for recorded units; (b) the same at\n    the unit's mean rate above 12 cm/s, laid over the fast periods only; for 454 units from 378\n    recorded, units are drawn with replacement in either reading. The t-test's df (818) does not\n    match 454 + 378 - 2 = 830; it is noted, not used. Reproduced when, under one reading, both\n    values are within tolerance, the KS test gives p < 1e-15 and the t-test p < 1e-10 with recorded\n    units higher.\n- id: fig2s1-mutual-information\n  statement: Mean mutual information is slightly higher in LS than in CA1, both over all cells\n    (1.29 against 1.20) and over cells at or above 0.8 bits/spike (1.43 against 1.27).\n  source: Figure 2, figure supplement 1, legend A and B\n  quote: Mean mutual information in the hippocampus is 1.20+−0.47, while mutual information in the\n    septum is 1.29+−0.23. These values are significantly different (double sided t-test\n    t(541)=-3.05, p<.005)\n  statistics:\n  - about: all cells\n    test: double sided t-test\n    statistic: t(541)=-3.05\n    p: 0.005\n    p_relation: <\n    n: 165 CA1 and 378 LS cells\n  - about: cells at or above 0.8 bits/spike\n    test: double sided t-test\n    statistic: t(249)=-3.35\n    p: 0.005\n    p_relation: <\n    n: 124 CA1 and 127 LS cells\n  depends_on:\n  - fig2ab-fraction-spatial\n  expected:\n  - quantity: mean CA1 mutual information, all cells\n    value: 1.20\n    tolerance: 0.12\n  - quantity: mean LS mutual information, all cells\n    value: 1.29\n    tolerance: 0.13\n  - quantity: mean CA1 mutual information, cells at or above 0.8 bits/spike\n    value: 1.27\n    tolerance: 0.13\n  - quantity: mean LS mutual information, cells at or above 0.8 bits/spike\n    value: 1.43\n    tolerance: 0.14\n  criterion: Mutual information as in MASSmutualinfo.m and mutualinfo.m (the smoothed fast rate map\n    normalised to sum 1, treated as a joint distribution over x and y bins, log base 2), cited by\n    the paper as Ego-Stengel and Wilson 2007. The bin size is passed as dim; the paper fixes 1 cm\n    for the information measures (Methods, Bits/spike), used here. Reproduced when the four means\n    are within tolerance and both t-tests give p < 0.005 with LS higher.\n- id: fig2f-bits-per-second\n  statement: CA1 cells carry more spatial information per second than LS cells (1.34 against 0.82\n    bits/s).\n  source: Results, Place fields are less abundant in the LS, paragraph 2; Figure 2D-F\n  quote: We found a mean of 1.34+−1.4bits/sec for CA1 cells, and 0.82+−1.1bits/sec for LS cells (\n    Figure 2D–E ). Units in the hippocampus had a significantly greater mean bits/sec than in the LS\n    (two-tailed two sample t-test t(541)=4.57, p<0.001)\n  statistics:\n  - test: two-tailed two sample t-test\n    statistic: t(541)=4.57\n    p: 0.001\n    p_relation: <\n    n: 165 CA1 and 378 LS cells\n  depends_on:\n  - units-recorded\n  expected:\n  - quantity: mean CA1 bits/s\n    value: 1.34\n    tolerance: 0.13\n  - quantity: mean LS bits/s\n    value: 0.82\n    tolerance: 0.08\n  criterion: Bits/s as in the Methods on the same maps as bits/spike. Tolerances are 10% of the\n    means (the +- values are SDs across cells). Reproduced when both are within tolerance and the\n    t-test gives p < 0.001 with CA1 higher.\n- id: fig3ab-field-counts\n  statement: Of CA1 cells at or above 0.8 bits/spike, 104 had at least one place field (63 with\n    one, 33 with two, seven with three, one with four); of LS cells, 100 did (54, 33, six, five\n    with four and two with five).\n  source: Results, Place fields are less abundant in the LS, paragraph 4; Figure 3A-B\n  quote: Of the 164 HPC units with bits/spike greater than or equal to 0.8, 104 units had at least\n    one place field, with 63 of these cells with one field, 33 with two fields, seven with three\n    fields, and a single cell with four fields ... Of the 127 LS cells with bits/spike greater than\n    0.8, 100 had at least one place field, with 54 with one field, 33 with two fields, six with\n    three fields, five with four fields, and two with five fields\n  depends_on:\n  - fig2ab-fraction-spatial\n  expected:\n  - quantity: CA1 cells with at least one field\n    value: 104\n    tolerance: 10\n  - quantity: LS cells with at least one field\n    value: 100\n    tolerance: 10\n  - quantity: CA1 cells with one field\n    value: 63\n    tolerance: 6.3\n  - quantity: CA1 cells with two fields\n    value: 33\n    tolerance: 3.3\n  - quantity: LS cells with one field\n    value: 54\n    tolerance: 5.4\n  - quantity: LS cells with two fields\n    value: 33\n    tolerance: 3.3\n  criterion: Place fields as defined in the header (Results paragraph 4, Methods, Place field\n    analysis, MASSplacefieldnum.m) on 2 cm maps. The minimum rate rule is open between the\n    Methods (maximum rate below 0.05 Hz dropped) and the code (fields dropped when the map's\n    maximum is below 0.5 Hz); both readings are run. Reproduced when, under one reading, the two\n    cell totals and the four one- and two-field counts are within tolerance; the counts of three\n    or more fields (7, 1; 6, 5, 2) are reported and judged as a whole by their sum within 10%\n    (8 and 13).\n- id: fig3-field-number-distribution\n  statement: The distribution of the number of fields per place cell does not differ between CA1\n    and LS.\n  source: Results, Place fields are less abundant in the LS, paragraph 4; Figure 3 legend\n  quote: The distributions of field numbers were not significantly different between CA1 and LS\n    cells (two sample Kolmogorov-Smirnov (KS) test, p>0.5)\n  statistics:\n  - test: two sample Kolmogorov-Smirnov test\n    p: 0.5\n    p_relation: '>'\n    n: 104 CA1 and 100 LS place cells\n  depends_on:\n  - fig3ab-field-counts\n  criterion: A claim of absence, judged on the paper's test, a two sample KS test of fields per cell\n    over the place cells (cells with at least one field) of each region. Reproduced when p > 0.05\n    (the threshold the paper uses for significance elsewhere); not reproduced when p < 0.05. The\n    paper's p > 0.5 is reported against the result, and the two mean field numbers are given.\n- id: fig3s1-speed-acceleration\n  statement: Little spatial firing is explained by speed or acceleration; regressing each spatial\n    bin's firing rate on the bin's mean speed and acceleration, only two cells with place fields\n    have r2 above 0.5 and the median r2 is 0.06.\n  source: Results, Place fields are less abundant in the LS, paragraph 4; Figure 3, figure supplement 1\n  quote: Only two cells with place fields had an r2 of >0.5, with the median r 2 value of 0.06 (\n    Figure 3—figure supplement 1 ), so very little spatial firing could be explained by\n    correlations with speed or acceleration\n  depends_on:\n  - fig3ab-field-counts\n  expected:\n  - quantity: median r2\n    value: 0.06\n    tolerance: 0.006\n  - quantity: cells with place fields with r2 above 0.5\n    value: 2\n    tolerance: 0\n  criterion: A multiple linear regression, per cell, of the bin firing rates on the bins' mean speed\n    and acceleration (Results). Open, no code found for it. The cells are the LS place cells (the\n    supplement's title says \"LS firing rate\"); the bins are read as the 2 cm place field bins\n    above 12 cm/s, which reading (a) takes from the smoothed map and reading (b) from the unsmoothed\n    map; acceleration is the derivative of the smoothed speed. Reproduced when, under one reading,\n    the median r2 is within 0.054 to 0.066 and at most 3 cells exceed 0.5; partially reproduced\n    when the median r2 is below 0.1 and at most 5 cells exceed 0.5.\n- id: place-cell-abundance\n  statement: Place cells (at least 0.8 bits/spike and a place field) are more common in CA1, 104 of\n    165 (63.0%), than in LS, 100 of 378 (26.5%).\n  source: Results, Place fields are less abundant in the LS, paragraph 5\n  quote: out of 165 recorded CA1 cells that met spike rate and track coverage criteria, 104 (63.0%)\n    met or exceeded a bits per spike cut off of 0.8 and had at least one place field ... while out\n    of 378 recorded LS cells meeting spike rate and track coverage criteria, 100 (26.5%) met the same\n    criteria ... Place cells in the CA1 are therefore significantly more abundant than in the cdLS\n    (two-tailed two sample t-test t(541)=8.6, p<0.001)\n  statistics:\n  - test: two-tailed two sample t-test\n    statistic: t(541)=8.6\n    p: 0.001\n    p_relation: <\n    n: 165 CA1 and 378 LS cells\n  depends_on:\n  - fig3ab-field-counts\n  expected:\n  - quantity: fraction of CA1 cells that are place cells\n    value: 63.0\n    tolerance: 6.3\n    unit: '%'\n  - quantity: fraction of LS cells that are place cells\n    value: 26.5\n    tolerance: 2.65\n    unit: '%'\n  criterion: The t-test is read as a two sample t-test on a 0 or 1 place-cell indicator per cell\n    (df 541 = 165 + 378 - 2). Reproduced when both fractions are within tolerance and the test gives\n    p < 0.001 with CA1 higher.\n- id: fig4ab-field-length\n  statement: CA1 and LS place fields have the same mean length, 29.1 and 28.8 cm.\n  source: Results, CA1 and LS place fields have comparable average sizes, paragraph 1; Figure 4A-B\n  quote: The average length of a CA1 place field was 29.1+−14.7 cm ( Figure 4A,C ), while the\n    average length of an LS place field was 28.8+−16.6 cm ( Figure 4B,D ). The average field\n    lengths were not significantly different (two-tailed two sample t-test t(320)=-0.16, p>0.05)\n  statistics:\n  - test: two-tailed two sample t-test\n    statistic: t(320)=-0.16\n    p: 0.05\n    p_relation: '>'\n    n: 154 CA1 and 168 LS fields\n  depends_on:\n  - fig3ab-field-counts\n  expected:\n  - quantity: mean CA1 field length\n    value: 29.1\n    tolerance: 2.9\n    unit: cm\n  - quantity: mean LS field length\n    value: 28.8\n    tolerance: 2.9\n    unit: cm\n  criterion: Field length as in MASSplacefieldnum.m (header). The field totals 154 and 168 follow\n    from the counts per cell in fig3ab-field-counts and from the df. The absence part is judged on\n    the paper's two-tailed two sample t-test over fields; reproduced when both means are within\n    tolerance and p > 0.05; not reproduced when p < 0.05.\n- id: fig4ef-lap-accuracy-change\n  statement: In CA1 the distance of a lap's peak firing from the field centre differs slightly but\n    significantly between lap 1 and lap 30; in LS it does not.\n  source: Figure 4E-F legend; Results, CA1 and LS place fields have comparable average sizes, paragraph 2\n  quote: The average distance from the field center in lap one is slightly but significantly\n    different than the average field distance from the center in lap 30 (two-tailed two sample\n    t-test t(177)=-2.7, p<0.01) ... The average distance from the field center in lap one was not\n    significantly different than the average field distance from the center in lap 30 (two-tailed\n    two sample t-test t(207)=0.2, p>0.05)\n  statistics:\n  - about: CA1, lap 1 against lap 30\n    test: two-tailed two sample t-test\n    statistic: t(177)=-2.7\n    p: 0.01\n    p_relation: <\n  - about: LS, lap 1 against lap 30\n    test: two-tailed two sample t-test\n    statistic: t(207)=0.2\n    p: 0.05\n    p_relation: '>'\n  depends_on:\n  - fig3ab-field-counts\n  criterion: For each pass through a directional field, the distance of the location of the most\n    spiking from the field centre (Results). Fields are included if passed at least 15 times, laps\n    if at least 20 fields have that many laps (Methods, Place field analysis). A pass is taken from\n    MASSplacefieldnumDIRECTIONALtrials.m (passes by the centre within 15 cm, spikes within 20 cm of\n    the centre on either side). Reproduced when the CA1 test gives p < 0.01 and the LS test p >\n    0.05; partially reproduced when only one holds. The LS half is an absence, judged on the same\n    test.\n- id: fig4ef-hpc-more-accurate\n  statement: CA1 fields are slightly more accurate than LS fields, on the first lap (mean distance of\n    peak from centre 2.7 against 4.9 cm) and across all laps (4.70 against 5.12 cm).\n  source: Results, CA1 and LS place fields have comparable average sizes, paragraph 2; Figure 4E-F\n  quote: (On the first lap, HPC has a mean distance of 2.7 cm versus 4.9 cm for the LS, two-tailed\n    two sample t-test t(319)=-3.1, p<0.005. Across all laps, mean distance of 4.70 cm for the HPC\n    versus 5.12 cm for the LS, two-tailed two sample t-test t(6792) = −2.5, p<0.05)\n  statistics:\n  - about: first lap\n    test: two-tailed two sample t-test\n    statistic: t(319)=-3.1\n    p: 0.005\n    p_relation: <\n  - about: all laps\n    test: two-tailed two sample t-test\n    statistic: t(6792)=-2.5\n    p: 0.05\n    p_relation: <\n  depends_on:\n  - fig4ef-lap-accuracy-change\n  expected:\n  - quantity: CA1 mean distance, lap 1\n    value: 2.7\n    tolerance: 0.27\n    unit: cm\n  - quantity: LS mean distance, lap 1\n    value: 4.9\n    tolerance: 0.49\n    unit: cm\n  - quantity: CA1 mean distance, all laps\n    value: 4.70\n    tolerance: 0.47\n    unit: cm\n  - quantity: LS mean distance, all laps\n    value: 5.12\n    tolerance: 0.51\n    unit: cm\n  criterion: As in fig4ef-lap-accuracy-change. The first-lap df (319) is near the number of fields\n    in all (322), the other test (6792) pools field-laps; the first-lap test is read as over all\n    fields, not only those with 15 passes, as a reading named here, the other being the filtered\n    set of fig4ef-lap-accuracy-change. Reproduced when, under one reading, the four means are within\n    tolerance and both tests reach their p bound with CA1 smaller.\n- id: fig4gh-firing-increases\n  statement: Fields in both CA1 and LS increase in-field firing with experience; the rate per cm\n    around the field centre is higher in the last five runs than the first five at nearly all\n    locations.\n  source: Results, CA1 and LS place fields have comparable average sizes, paragraph 2; Figure 4G-H\n  quote: Fields in both the HPC and the LS significantly increase firing in their place field with\n    experience on the track ( Figure 4G–H )\n  statistics:\n  - about: first five against last five runs, per cm from centre\n    test: two-tailed two sample t-test\n    p: 0.05\n    p_relation: <\n  depends_on:\n  - fig4ef-lap-accuracy-change\n  criterion: Spiking per cm in 2 cm steps from -20 to +20 cm around the field centre, averaged over\n    the first five and the last five runs through each field (Figure 4G-H legend; distances from\n    MASSplacefieldnumDIRECTIONALtrials.m). The legend reports differences significant at all\n    offsets but +18 and +20 cm in CA1 and -18 cm in LS (two-tailed two sample t-tests, read at\n    p < 0.05 uncorrected, as the legend gives no correction). Reproduced when the last-five mean is\n    higher at the offsets tested and significantly so at least 80% of them in each region;\n    partially reproduced in one region only.\n- id: fig5abc-skew-direction\n  statement: In CA1, fields are skewed positively when travelling toward reward and negatively when\n    travelling away, a significant difference; in LS the pattern is reversed and not significant.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 1; Figure 5A-C\n  quote: We found that, when travelling toward a reward site, cells in the hippocampus were skewed\n    positively toward the direction of travel, while, when traveling away from a reward site, cells\n    were skewed negatively away from the direction of travel, and this difference was significant\n    (two-tailed two sample t-test t(207)=-2.1, p<0.05) ... though this difference is not significant\n    (two-tailed two sample t-test t(246)=-1.7, p=0.09)\n  statistics:\n  - about: CA1, toward against away\n    test: two-tailed two sample t-test\n    statistic: t(207)=-2.1\n    p: 0.05\n    p_relation: <\n    n: 115 toward and 94 away CA1 fields\n  - about: LS, toward against away\n    test: two-tailed two sample t-test\n    statistic: t(246)=-1.7\n    p: 0.09\n    n: 138 toward and 110 away LS fields\n  depends_on:\n  - fig6-direction-split\n  criterion: Skew of each directional field (header; MASSplacefieldnumDIRECTIONAL.m). Which value is\n    compared is open. The code stores skew in a fixed orientation per arm (allskew) and a sign\n    flipped for the away direction (alldirskew). Readings are (a) the sign-flipped value, which the\n    Results' \"toward the direction of travel\" suggests, and (b) the fixed value. Reproduced when,\n    under one reading, CA1 mean skew is positive toward and negative away with p < 0.05, and the LS\n    means have the opposite signs with p > 0.05.\n- id: fig5s4-uni-bidirectional\n  statement: Skew does not differ between unidirectional and bidirectional fields in either region.\n  source: Figure 5, figure supplement 4; Results, CA1 and LS place fields have different skew,\n    paragraph 1\n  quote: there was no significant difference for values of skew based on whether a place cell was\n    uni or bi directional (both two-tailed two sample t-tests, p>0.05\n  statistics:\n  - about: LS, uni against bi\n    test: two-tailed two sample t-test\n    statistic: t(246)=-0.19\n    p: 0.85\n  - about: LS, uni and bi by travel direction\n    test: one way anova\n    statistic: F(3,244) = 1.05\n    p: 0.05\n    p_relation: '>'\n  - about: CA1, uni against bi\n    test: two-tailed two sample t-test\n    statistic: t(207)=-0.59\n    p: 0.55\n  - about: CA1, uni and bi by travel direction\n    test: one way anova\n    statistic: F(3,205) = 0.29\n    p: 0.05\n    p_relation: '>'\n  depends_on:\n  - fig5abc-skew-direction\n  criterion: A claim of absence, judged on the paper's tests (two-tailed two sample t-test of skew,\n    uni against bi, and a one way ANOVA over the four uni/bi by direction groups, per region), with\n    the skew reading adopted for fig5abc-skew-direction. Reproduced when all four give p > 0.05; not\n    reproduced when any gives p < 0.05.\n- id: fig5s5-skew-frai\n  statement: Skew and the firing rate asymmetry index (FRAI) are strongly linearly related in both\n    CA1 and LS, so skew is not explained by speed.\n  source: Figure 5, figure supplement 5; Results, CA1 and LS place fields have different skew,\n    paragraph 1\n  quote: There is a highly significant relationship between skew and FRAI in HPC cells\n    (f(207)=61.0, p<9 -13 ). ( B ) Same as A but in LS (F(247) = 43.77, p<9 -10 )\n  statistics:\n  - about: CA1\n    test: linear regression F test\n    statistic: f(207)=61.0\n    p: 1.0e-12\n    p_relation: <\n  - about: LS\n    test: linear regression F test\n    statistic: F(247) = 43.77\n    p: 1.0e-9\n    p_relation: <\n  depends_on:\n  - fig5abc-skew-direction\n  criterion: FRAI as in MASSplacefieldnumDIRECTIONAL.m, (F1 - F2)/(F1 + F2) with F1 and F2 the rates\n    (spikes over time) in the parts of the field holding the first and second halves of its spikes,\n    sign flipped for the away direction; the printed formula lost its minus sign. The p bounds print\n    as \"p<9 -13\" and \"p<9 -10\" and are read as 9e-13 and 9e-10 (recorded here as the looser 1e-12\n    and 1e-9). Reproduced when a linear regression of FRAI on skew over directional fields gives\n    p < 1e-9 in CA1 and p < 1e-7 in LS, with the same sign of slope; partially reproduced when both\n    are below 0.001.\n- id: fig5e-reward-proximate-skew\n  statement: For fields in the rewarded arms, skew differs between the two directions of travel in\n    LS but not in CA1; LS fields ramp up firing on reward approach.\n  source: Results, CA1 and LS place fields have different skew, paragraph 2; Figure 5E\n  quote: skew values were not significantly different for hippocampus traveling to and from reward\n    (two sample two sided t-test, t(74)=-0.59 p>0.05), but were significantly different for LS cells\n    to and from reward (two sample two sided t-test, t(108)=-2.10, p<0.05)\n  statistics:\n  - about: CA1, toward against away, rewarded arms\n    test: two sample two sided t-test\n    statistic: t(74)=-0.59\n    p: 0.05\n    p_relation: '>'\n  - about: LS, toward against away, rewarded arms\n    test: two sample two sided t-test\n    statistic: t(108)=-2.10\n    p: 0.05\n    p_relation: <\n  - about: CA1 away from reward against shuffled skew\n    test: two sample two sided t-test\n    statistic: t(301)=-2.05\n    p: 0.05\n    p_relation: <\n  - about: LS away from reward against zero\n    test: one sample two sided t-test\n    statistic: t(58)=-2.0\n    p: 0.05\n  depends_on:\n  - fig5abc-skew-direction\n  criterion: Fields whose centre is in the rewarded (choice) arms, Figure 5D, under the code's\n    choice-side boxes; whether the choice arm ends are included is open, and the readings are with\n    and without them. Skew reading as adopted for fig5abc-skew-direction. Shuffled skew as in Figure\n    5 S3, firing rates shuffled within the field, 500 shuffles. Reproduced when the LS test gives\n    p < 0.05 and the CA1 test p > 0.05 (an absence, on the paper's test); the shuffle and zero tests\n    are reported as secondary.\n- id: fig5s2-skew-distance\n  statement: Across the whole track, skew in CA1 fields correlates with distance to reward when\n    travelling away from reward; neither LS correlation is significant.\n  source: Figure 5, figure supplement 2, legend A and B\n  quote: Bottom - Scatter plot of skewness in HPC place cells versus distance to reward when\n    traveling away from reward. The linear correlation was significant (F statistic(1,92)=7.01,\n    p<0.01, r 2 =0.07). ( B ) Same as A but in the LS. Neither linear correlation was significant\n  statistics:\n  - about: CA1 away from reward\n    test: linear regression F test\n    statistic: F(1,92)=7.01\n    p: 0.01\n    p_relation: <\n  depends_on:\n  - fig5abc-skew-direction\n  expected:\n  - quantity: CA1 away from reward r2\n    value: 0.07\n    tolerance: 0.007\n  criterion: Distance to reward is open; readings are (a) distance along the track from the field\n    centre to the nearer choice arm end, (b) straight-line distance to the nearer reward site.\n    Reproduced when, under one reading, the CA1 away regression gives p < 0.01 and both LS\n    regressions p > 0.05; the r2 is reported against 0.07.\n- id: fig6-location-counts\n  statement: CA1 fields lie 49/154 on the forced sides, 36/154 on the centre stem and 45/154 on the\n    choice sides; LS fields 37/168, 40/168 and 69/168; the two distributions differ.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 3; Figure 6B-E\n  quote: In the hippocampus, 49/154 of place fields occurred on the forced sides, 36/154 on the\n    center stem, and 45/154 on the end of the choice sides ... In the LS, 37/168 of place fields\n    occurred on the forced sides, 40/168 on the center stem, and 69/168 on the end of the choice\n    sides (22 occurred at choice points) ... The distribution of place fields is significantly\n    different between the hippocampus and the lateral septum (Pearson’s chi 2 test, X 2 = 6.03,\n    p<0.05)\n  statistics:\n  - test: Pearson's chi2 test\n    statistic: X2 = 6.03\n    p: 0.05\n    p_relation: <\n    n: 154 CA1 and 168 LS fields\n  depends_on:\n  - fig4ab-field-length\n  expected:\n  - quantity: CA1 fields on forced sides\n    value: 49\n    tolerance: 4.9\n  - quantity: CA1 fields on centre stem\n    value: 36\n    tolerance: 3.6\n  - quantity: CA1 fields on choice sides\n    value: 45\n    tolerance: 4.5\n  - quantity: LS fields on forced sides\n    value: 37\n    tolerance: 3.7\n  - quantity: LS fields on centre stem\n    value: 40\n    tolerance: 4.0\n  - quantity: LS fields on choice sides\n    value: 69\n    tolerance: 6.9\n  criterion: Field centres (bin of highest rate) classified by the code's boxes; forced sides are\n    the forced arms and their ends, choice sides the choice arms and their ends, forced and choice\n    points excluded (24 CA1 and 22 LS fields). The legend gives X2 = 12.7, the Results 6.03; which\n    table was tested is open. Readings are (a) the 2 by 3 table of the three locations, (b) the\n    2 by 4 or 2 by 5 table with the junction points. Reproduced when the six counts are within\n    tolerance and, under one reading, the chi2 test gives p < 0.05.\n- id: fig6de-choice-side-bias\n  statement: LS has proportionally about 1.4 times more fields on the choice side than CA1 (41.1%\n    against 29.2%), and in LS, but not CA1, there are more fields in the choice arms than the forced\n    arms.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 3; Figure 6D-E\n  quote: The LS has about 1.4 times, proportionally, significantly more place fields in the choice\n    side than the HPC (41.1% of total fields in the LS, versus 29.2% of total fields in the HPC,\n    two-tailed two sample t-test t(320)=2.23, p<0.05). In the hippocampus, the number of fields in\n    the choice arms versus the forced arms was not significantly different (two-tailed two sample\n    t-test t(364) = 2.34, p>0.05), while, in the LS, there were significantly more fields in the\n    choice arms compared to the forced arms (two-tailed two sample t-test t(334)=-3.8, p<0.001)\n  statistics:\n  - about: choice-side proportion, LS against CA1\n    test: two-tailed two sample t-test\n    statistic: t(320)=2.23\n    p: 0.05\n    p_relation: <\n  - about: CA1, choice against forced arms\n    test: two-tailed two sample t-test\n    statistic: t(364) = 2.34\n    p: 0.05\n    p_relation: '>'\n  - about: LS, choice against forced arms\n    test: two-tailed two sample t-test\n    statistic: t(334)=-3.8\n    p: 0.001\n    p_relation: <\n  depends_on:\n  - fig6-location-counts\n  expected:\n  - quantity: LS fraction of fields on the choice side\n    value: 41.1\n    tolerance: 4.1\n    unit: '%'\n  - quantity: CA1 fraction of fields on the choice side\n    value: 29.2\n    tolerance: 2.9\n    unit: '%'\n  criterion: The choice-side proportions are over all fields including those at the junction points\n    (69/168 = 41.1%, 45/154 = 29.2%). The LS-CA1 test is read as a two sample t-test on a 0 or 1\n    choice-side indicator per field (df 320). The arm tests have df 364 and 334, near twice the\n    field totals (2 x 154 + ... ); they are read as two sample t-tests of a 0 or 1 indicator for\n    choice and for forced arm, one sample of each per field, over (a) all fields, (b) the fields\n    off the junction points. The paper prints t = 2.34 with p > 0.05 for CA1, which df 364 does not\n    allow; the CA1 half, an absence, is judged at p > 0.05. Reproduced when the proportions are\n    within tolerance, the LS-CA1 test gives p < 0.05, the LS arm test p < 0.001 with choice\n    higher, and the CA1 arm test p > 0.05.\n- id: fig6-direction-split\n  statement: Split by direction of travel there are 209 CA1 fields (115 toward and 94 away from\n    reward; 133 unidirectional, 76 bidirectional) and 248 LS fields (138, 110; 177, 71); field\n    sizes do not differ by direction.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 4\n  quote: This resulted in a total of 209 hippocampal place fields (115 toward reward and 94 away\n    from reward, with, out of the total, 133 being unidirectional and 76 being bi directional) and\n    248 LS place fields (138 toward reward, 110 away from reward, with, out of the total, 177\n    unidirectional and 71 bidirectional\n  statistics:\n  - about: numbers of uni and bidirectional fields, CA1 against LS\n    test: two-tailed two sample t-test\n    statistic: t(461)=1.377\n    p: 0.05\n    p_relation: '>'\n  - about: field sizes by direction, within and across regions\n    test: two-tailed two sample t-test\n    p: 0.05\n    p_relation: '>'\n  depends_on:\n  - fig3ab-field-counts\n  expected:\n  - quantity: CA1 directional fields\n    value: 209\n    tolerance: 21\n  - quantity: CA1 fields toward reward\n    value: 115\n    tolerance: 11.5\n  - quantity: CA1 fields away from reward\n    value: 94\n    tolerance: 9.4\n  - quantity: LS directional fields\n    value: 248\n    tolerance: 25\n  - quantity: LS fields toward reward\n    value: 138\n    tolerance: 13.8\n  - quantity: LS fields away from reward\n    value: 110\n    tolerance: 11\n  - quantity: CA1 bidirectional fields\n    value: 76\n    tolerance: 7.6\n  - quantity: LS bidirectional fields\n    value: 71\n    tolerance: 7.1\n  criterion: Fields found separately in each direction's map (MASSplacefieldnumDIRECTIONAL.m);\n    bidirectional when the cell has fields in both directions with centres less than 20 cm apart\n    (Methods). The counts are judged by their tolerances; the size comparisons (absence) on\n    two-tailed two sample t-tests at p > 0.05.\n- id: fig6g-ls-choice-by-direction\n  statement: In LS the excess of choice-side over forced-side fields is strongest when travelling\n    away from reward and a trend when travelling toward it; in CA1 there are never significantly\n    more fields on the choice side.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 5; Figure 6F-G\n  quote: In the LS, the difference seen in the number of fields on the forced side versus choice\n    side was most stark when the animal was traveling away from reward (two-tailed two sample t-test\n    t(218)=3.8 p<0.001), although there was a clear trend while the animal traveled toward reward\n    (two-tailed two sample t-test t(254)=1.82 p<0.1) ( Figure 6G ). In the hippocampus, there were\n    never significantly more fields on the choice side\n  statistics:\n  - about: LS away from reward, choice against forced\n    test: two-tailed two sample t-test\n    statistic: t(218)=3.8\n    p: 0.001\n    p_relation: <\n  - about: LS toward reward, choice against forced\n    test: two-tailed two sample t-test\n    statistic: t(254)=1.82\n    p: 0.1\n    p_relation: <\n  - about: LS choice-side distribution by direction of travel\n    test: one-tailed two sample t-test\n    statistic: t(102)=-2.15\n    p: 0.05\n    p_relation: <\n  depends_on:\n  - fig6-direction-split\n  criterion: Directional fields located as in fig6-location-counts, tested as in\n    fig6de-choice-side-bias, per direction (df 218 and 254 are near twice the 110 away and 138\n    toward LS fields). Reproduced when the LS away test gives p < 0.001 with choice higher, the LS\n    toward test p < 0.1 with choice higher, and neither CA1 direction gives significantly more\n    choice than forced fields (p > 0.05 or forced higher).\n- id: fig6s2-rate-not-distance\n  statement: Mean in-field firing rate does not scale with distance to reward in either LS or CA1.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 5; Figure 6, figure supplement 2\n  quote: average place field firing rate did not scale with distance to reward in either the LS or\n    the hippocampus ( Figure 6—figure supplement 2 )\n  depends_on:\n  - fig6-direction-split\n  criterion: A claim of absence for which the paper names no test. The nearest test in the paper is\n    the linear regression with an F test used for skew against distance in Figure 5 S2; it is\n    applied here to mean in-field rate against distance to reward, per region and direction, at\n    p < 0.05, with the distance readings of fig5s2-skew-distance. Reproduced when none of the four\n    regressions is significant; not reproduced when any is; the slopes are reported.\n- id: fig6hi-probability-distance\n  statement: In CA1 the probability of a field rises over the last 60 cm of reward approach, with the\n    largest peaks near the forced and choice points (about 200 to 220 and 60 to 80 cm from reward);\n    in LS the forced arms are overrepresented and the probability also rises on reward approach.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 6; Figure 6H-I\n  quote: In the hippocampus, there was an increase in the probability of a spatial firing field in\n    the last 60 cm of reward approach ( Figure 6H ). However, the largest peeks in HPC place field\n    probability were around the forced and choice points of the maze, approximately 200–220 cm and\n    80–60 cm away from reward, respectively\n  depends_on:\n  - fig6-direction-split\n  criterion: Histogram of field-bin distances to the nearer reward site along the track (Figure 6\n    legend note that each field contributes bins per visit); bin width is a plotting choice, 10 cm\n    used as a standard one. The paper gives no test. Reproduced when the CA1 probability in the last\n    60 cm exceeds its mean over the track and the two highest CA1 peaks fall within 180 to 242 cm and\n    54 to 88 cm (the ranges widened by 10%); partially reproduced when only the rise or only the\n    peaks hold. The LS description (choice-side and approach rise) is reported.\n- id: fig7a-crosscorr-choice\n  statement: HPC-LS place cell pairs with fields on the choice side have a higher mean\n    cross-correlation over +-100 ms than pairs on the forced side or the middle arm.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 7; Figure 7A\n  quote: We found that place cell pairs with fields in the choice side of the maze had a\n    significantly higher mean average correlation (over +−100 ms) than place cell pairs with fields\n    in the middle or forced arm ( Figure 7A ) (forced versus choice - two-tailed two sample t-test\n    t(67)=-2.2, p<0.05, middle versus choice - two-tailed two sample t-test t(54)=-2.3, p<0.05)\n  statistics:\n  - about: forced against choice side pairs\n    test: two-tailed two sample t-test\n    statistic: t(67)=-2.2\n    p: 0.05\n    p_relation: <\n  - about: middle arm against choice side pairs\n    test: two-tailed two sample t-test\n    statistic: t(54)=-2.3\n    p: 0.05\n    p_relation: <\n  depends_on:\n  - fig6-direction-split\n  criterion: Pairs, trains and cross-correlation as in the header (Methods, Cross correlation\n    analysis; CCpairs.m); 36 forced-arm pairs per Figure 7 S1, and df 67 and 54 for the other\n    groups. A pair's measure is the mean over the 21 lags of the cross-correlation minus the\n    shuffled one (Methods), with the code's raw mean as a variant. Reproduced when choice-side\n    pairs have the higher mean and both two-tailed two sample t-tests give p < 0.05.\n- id: fig7b-lag\n  statement: For pairs on the choice side the cross-correlation peaks at a mean lag of 20 ms with the\n    HPC leading.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 7; Figure 7B\n  quote: For pairs in the choice arm, the maximum value of the cross correlation happened at a mean\n    lag of 20 ms with the HPC leading\n  depends_on:\n  - fig7a-crosscorr-choice\n  expected:\n  - quantity: lag of the peak of the mean choice-side cross-correlation\n    value: 20\n    tolerance: 10\n    unit: ms\n  criterion: Tolerance is one 10 ms bin, the resolution of the trains (10% of 20 ms is below it).\n    The Results say the choice arm, the legend says \"Mean correlation peak for forced arm\n    correlations was at 20 ms\". Readings are (a) the lag of the peak of the mean trace over\n    choice-side pairs, (b) the mean of the per-pair peak lags, (c) either for forced-arm pairs.\n    Reproduced when under (a) or (b) the choice-side lag is 10 to 30 ms with the HPC leading\n    (positive lag in crosscorr(HPC, LS)); the forced-arm reading is reported.\n- id: fig7s2-ls-rates-by-location\n  statement: Mean and maximum in-field firing rates of LS place cells do not differ between the\n    forced side, middle arm and choice side.\n  source: Figure 7, figure supplement 2; Results, paragraph 7 of CA1 and LS place fields have\n    different skew\n  quote: The means of three distributions were not significantly different (One way anova,\n    F(2,112) = 1.15, p>0.05)\n  statistics:\n  - about: mean in-field rate\n    test: one way anova\n    statistic: F(2,112) = 1.15\n    p: 0.05\n    p_relation: '>'\n  - about: maximum in-field rate\n    test: one way anova\n    statistic: F(2,112) = 1.93\n    p: 0.05\n    p_relation: '>'\n  depends_on:\n  - fig6-location-counts\n  criterion: A claim of absence, judged on the paper's one way ANOVAs over the three locations. The\n    df (115 fields) is fewer than all located LS fields (146); readings are (a) the LS fields of\n    matched HPC-LS pairs, (b) all located LS fields. Reproduced when both ANOVAs give p > 0.05\n    under reading (a), the paper's sample as its df suggests; not reproduced when either gives\n    p < 0.05; reading (b) is shown as a variant.\n- id: fig7s3-pair-distance-control\n  statement: The higher choice-side cross-correlation is not due to closer field centres; forced and\n    choice pairs do not differ in centre distance, and after removing pairs with centres within 3 cm\n    the choice-side cross-correlation is still higher.\n  source: Figure 7, figure supplement 3\n  quote: We found that there was no significant difference between the average distance between LS\n    and HPC pairs in the forced arm versus choice arm (two-tailed two sample t-test, t(67) = 1.8,\n    p>0.05) ... When subsampled as described, the average cross correlation for pairs on the choice\n    side was still significantly higher than the average in either the forced side or middle stem\n  statistics:\n  - about: centre distance, forced against choice pairs\n    test: two-tailed two sample t-test\n    statistic: t(67) = 1.8\n    p: 0.05\n    p_relation: '>'\n  - about: centre distance, choice against middle pairs\n    test: two-tailed two sample t-test\n    statistic: t(51) = 2.2\n    p: 0.03\n  - about: subsampled cross-correlation, forced against choice\n    test: double sided t test\n    statistic: t(51) = 1.96\n    p: 0.05\n    p_relation: <\n  - about: subsampled cross-correlation, middle against choice\n    test: double sided t test\n    statistic: t(51) = 2.2\n    p: 0.05\n    p_relation: <\n  depends_on:\n  - fig7a-crosscorr-choice\n  criterion: Pairs as in fig7a-crosscorr-choice; centre distance between the matched fields'\n    centres. Subsampling drops pairs with centres within 3 cm (the commented-out line in CCpairs.m\n    uses the same 3 cm). Reproduced when the forced-choice distance test gives p > 0.05 and, after\n    subsampling, both cross-correlation tests give p < 0.05 with choice higher.\n- id: fig7s1-above-shuffle\n  statement: Shuffled forced-arm pairs average a cross-correlation of 7.71e-05; of 36 forced-arm\n    pairs, 26 (72%) lie above the shuffled 95% confidence interval.\n  source: Figure 7, figure supplement 1B\n  quote: We shuffled the spike trains of all the HPC and LS pairs on the forced arm and found an\n    average correlation of 7.71e-05, with a 95% confidence interval of [-8.89e-05, 2.43e04]. Out of\n    36 unit pairs on the forced arm, the average of 26 of these pairs (72%) fell above the 95%\n    confidence interval for shuffled data\n  depends_on:\n  - fig7a-crosscorr-choice\n  expected:\n  - quantity: forced-arm pairs\n    value: 36\n    tolerance: 3.6\n  - quantity: fraction of forced-arm pairs above the shuffled 95% interval\n    value: 72\n    tolerance: 7.2\n    unit: '%'\n  criterion: The upper bound prints as \"2.43e04\", read as 2.43e-04. The shuffle is the random\n    permutation of the LS train (CCpairs.m); a pair's average is the mean raw cross-correlation over\n    +-100 ms against the interval of the shuffled averages over the 36 pairs. How the interval is\n    formed is open; readings are (a) the 2.5 and 97.5 percentiles of the shuffled pair averages,\n    (b) mean +- 1.96 SD of them. Reproduced when, under one reading, the count of pairs and the\n    fraction above are within tolerance; the shuffled mean is reported against 7.71e-05.\n- id: fig7c-thirds\n  statement: Cross-correlations of HPC-LS pairs do not change between the first, middle and last\n    third of a session, and reward-proximate pairs are higher than reward-distal pairs in all three.\n  source: Results, CA1 and LS place fields have different skew and location distributions,\n    paragraph 8; Figure 7C\n  quote: there were no significant differences within group (e.g. cross correlation of reward\n    proximate cells in the first third versus the last third of training) (all paired double sided t\n    tests, p>0.05). However, across all three periods of training, cross correlations for reward\n    proximate cells were consistently higher than for more reward-distal cells\n  statistics:\n  - about: within location group across thirds\n    test: paired double sided t test\n    p: 0.05\n    p_relation: '>'\n  depends_on:\n  - fig7a-crosscorr-choice\n  criterion: The session split into three equal parts of its position time base (CCpairs.m), the\n    pair measure computed in each. The absence part is judged on the paper's paired double sided\n    t-tests between thirds within each location group, reproduced when all give p > 0.05. The\n    second part holds when the choice-side mean exceeds the forced and middle means in each third;\n    the legend marks some of these with stars (unpaired two tailed t-tests), reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Fixing two quotes where I replaced a colon, and a stray phrase, then running the checker.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/wirtshafter-2020.yaml'
s=open(p).read()
s=s.replace("""    in the middle or forced arm ( Figure 7A ) (forced versus choice - two-tailed two sample t-test
    t(67)=-2.2, p<0.05, middle versus choice - two-tailed two sample t-test t(54)=-2.3, p<0.05)""",
"""    in the middle or forced arm ( Figure 7A ) (forced versus choice ... two-tailed two sample t-test
    t(67)=-2.2, p<0.05, middle versus choice ... two-tailed two sample t-test t(54)=-2.3, p<0.05)""")
s=s.replace("""  quote: Bottom - Scatter plot of skewness""","""  quote: Scatter plot of skewness""")
s=s.replace("""The arm tests have df 364 and 334, near twice the
    field totals (2 x 154 + ... ); they are read""","""The arm tests have df 364 and 334, near twice the
    field totals; they are read""")
open(p,'w').write(s)
EOF
grep -nE "^\s+[a-z_]+: [^'\"].*: " claims/wirtshafter-2020.yaml | head; grep -nE "^    [^-].*: " claims/wirtshafter-2020.yaml | head; grep -n "—\|rather" claims/wirtshafter-2020.yaml | head
python tools/claims_check.py claims/wirtshafter-2020.yaml paper/10.7554-elife.55252.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes all quotes; two p-values are the garbled "p<9 -13" bounds. I'll record them as printed (9e-13, 9e-10) and swap em dashes in quotes for hyphens (the checker treats them the same).

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/wirtshafter-2020.yaml'
s=open(p).read()
s=s.replace("—","-")
s=s.replace("""    p: 1.0e-12
    p_relation: <""","""    p: 9.0e-13
    p_relation: <""")
s=s.replace("""    p: 1.0e-9
    p_relation: <""","""    p: 9.0e-10
    p_relation: <""")
s=s.replace("""The p bounds print
    as "p<9 -13" and "p<9 -10" and are read as 9e-13 and 9e-10 (recorded here as the looser 1e-12
    and 1e-9). Reproduced when a linear regression of FRAI on skew over directional fields gives
    p < 1e-9 in CA1 and p < 1e-7 in LS, with the same sign of slope;""","""The p bounds print
    as "p<9 -13" and "p<9 -10" and are read as 9e-13 and 9e-10. Reproduced when a linear regression
    of FRAI on skew over directional fields gives p < 9e-13 in CA1 and p < 9e-10 in LS, with a
    positive slope in both;""")
s=s.replace("""Reproduced when the last-five mean is
    higher at the offsets tested and significantly so at least 80% of them in each region;""","""Reproduced when the last-five mean is
    higher and significantly so at no fewer than 17 of the 21 offsets in each region (the paper's
    19 and 20, less 10%);""")
open(p,'w').write(s)
EOF
grep -c "—" claims/wirtshafter-2020.yaml; python tools/claims_check.py claims/wirtshafter-2020.yaml paper/10.7554-elife.55252.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
p='claims/wirtshafter-2020.yaml'
s=open(p).read()
s=s.replace("""p < 9e-13 in CA1 and p < 9e-10 in LS, with a
    positive slope in both;""","""p < 9e-13 in CA1 and p < 9e-10 in LS (the paper gives no
    sign; the slopes are reported);""")
open(p,'w').write(s)
d=yaml.safe_load(s)
def walk(x,path=""):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+"/"+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f"[{i}]")
    elif isinstance(x,str) and ": " in x: print(path, x[:80])
walk(d)
print(len(d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
grep -n "rather" claims/wirtshafter-2020.yaml; python tools/claims_check.py claims/wirtshafter-2020.yaml paper/10.7554-elife.55252.txt | tail -1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/wirtshafter-2020.yaml`: 31 claims. Every claim has a word-for-word quote, 23 carry the paper's statistics (45 values), 17 have expected values and all 31 have a criterion. Nothing was committed.

**Checker:** all 31 quotes are found in the text. It still exits non-zero on two p-values in the Figure 5 S5 legend, which prints them as "p<9 -13" and "p<9 -10". I recorded them as 9e-13 and 9e-10 and confirmed them by reading the passage.

**Text read:** the version of record (PMC7274787, open access) as flattened JATS text. It has the main text, the Methods and the legends of all 7 figures and their 15 figure supplements. The paper has no other supplement, and no PDF was supplied or needed.

**Code read:** the eLife archived copy, `elifesciences-publications/data_analysis` at commit 5c6320a9 (2020-06-04). The code settles:
- bin sizes (3.5 px per cm)
- the field rule (at least mean + 1 SD; the Methods misprint it as "≤")
- the location boxes for each arm
- how direction of travel is split
- the skew computation and the FRAI formula (the extracted text lost its minus sign)
- how HPC and LS cells are paired and cross-correlated

Where the code and the Methods disagree, the Methods are the main reading and the code is a variant:
- speed smoothing (1 s SD Gaussian against a 30-sample window)
- the minimum rate (0.05 Hz against 0.5 Hz)
- the track-coverage rule (the code's "at least 1950 bins" counts all bins, visited or not)
- whether the shuffle is subtracted in the cross-correlation average (the Methods subtract it; the code's stored average does not)

**Details the paper leaves open, with the readings named:**
- **Full track coverage:** the code's 1950-bin rule, or every arm, the stem and both junctions visited above 12 cm/s.
- **Poisson units:** no script found. A constant-rate Poisson train at the unit's session mean rate, or at its rate above 12 cm/s over fast periods only. The reported df (818) also does not match the sample sizes.
- **Speed and acceleration regression (Fig 3 S1):** no code. Bins from the smoothed or the unsmoothed map.
- **Skew (Fig 5):** the value with its sign flipped for the away direction, or the value in a fixed track orientation.
- **Lap-1 accuracy test:** all fields, or only fields passed at least 15 times.
- **Reward-proximate fields:** with or without the choice-arm ends.
- **Distance to reward:** along the track, or in a straight line.
- **Chi² on field location:** the Results give 6.03 and the legend 12.7. Tested on a 3-location table, or one that includes the junction points.
- **Arm-count t-tests:** CA1 is printed as t(364)=2.34 with p>0.05, which that df does not allow. Tested on all fields, or only those off the junction points.
- **Peak lag:** the Results say the choice arm, the legend says the forced arm. The peak of the mean trace, or the mean of per-pair peak lags.
- **Fig 7 S2 sample:** the df (115) suggests matched-pair LS fields, the alternative is all located LS fields.
- **Shuffle 95% interval:** percentiles, or mean ± 1.96 SD.
- **Field firing rate against distance to reward (Fig 6 S2):** the paper names no test, so the linear regression of Fig 5 S2 is borrowed.
- **"164 HPC units"** is read as a misprint for 124.

**Missing from the paper:** nothing that stops a claim. Some things a claim needed are absent, and each is handled by the readings above:
- no code for the Poisson control or the speed regression
- several garbled or contradictory printed values: the FRAI formula, the p bounds, "2.43e04", the two chi² values, the CA1 t(364)
- the data set's description lists only spike times and "time files", not position data. Every claim needs position, so whether it is in the data set is for the author to find.

## End of run

25 turns, 6 minutes, $2.08 at API prices, result: success.
