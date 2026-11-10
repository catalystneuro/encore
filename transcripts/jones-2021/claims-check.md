# jones-2021 · claims-check · run 42837907600

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i jones; cat claims/jones-2021.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/jones-2021.yaml; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 43,200p docs/protocol.md; python tools/claims_check.py claims/jones-2021.yaml paper/10.1016-j.celrep.2021.110159.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/jones-2021.yaml"
}
```

```
1	# Claims for Aery Jones, Rao, Zilberter, ..., Huang & Frank (2021), Cell Reports 37, 110159,
2	# tested on dandiset 000165.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC9069800, NIHMS1795940), full
7	# text with STAR Methods and figure legends, and its main supplement PDF
8	# (NIHMS1795940-supplement-Main_supplement.pdf: Figures S1 to S7 and Tables S1 to S6), as
9	# stored under paper/. The version of record was not read. Supplementary Table S7 (an xlsx file,
10	# effects stratified by sex) is not under paper/ and was not read; only the claim
11	# sex-stratified-effects needs it.
12	#
13	# Code read: github.com/emilyasterjones/interneurons_modulate_drive, tag v1.0.0, commit 63b1acb
14	# (archived as Zenodo doi:10.5281/zenodo.5618979), MATLAB. It holds preprocessing (ripple,
15	# dentate spike and MUA extraction, position and velocity), rest analyses (ripple rates and
16	# descriptors, SWR-triggered MUA, spectrograms, coherence, CSD, SW amplitude, instantaneous
17	# frequency, dentate spikes), run analyses (continuous spectrograms, coherence, comodulation,
18	# instantaneous frequency, MUA, velocity) and the statistics (calcLMM.m, calcjointLMM.m,
19	# calcInteraction.m, calcunpairedLMM.m, HBcorrect.m, runcalcLMM_figs.m). It reads FilterFramework
20	# data structures, not the NWB files.
[... 980 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/jones-2021.yaml",
 "offset": 1000
}
```

```
1000	  statistics:
1001	  - about: theta frequency, DG, PV-Cre
1002	    test: F test of the LMM
1003	    p: 0.00061
1004	  - about: theta frequency, CA1, PV-Cre
1005	    test: F test of the LMM
1006	    p: 0.0082
1007	  - about: theta frequency, CA3, PV-Cre
1008	    test: F test of the LMM
1009	    p: 0.0077
1010	  - about: theta coherence, CA1-CA3, SST-Cre
1011	    test: F test of the LMM
1012	    p: 0.047
1013	  - about: theta coherence, CA1-DG, PV-Cre
1014	    test: F test of the LMM
1015	    p: 0.024
1016	  criterion: Theta coherence and instantaneous frequency as for SG (fig5e, fig5f). Method M (run
1017	    family). Reproduced when the PV-Cre DG theta frequency increase is significant and none of
1018	    the other ten tests (two coherences and three frequencies in each genotype, less the one) is;
1019	    not reproduced when any other is significant. The effect sizes are reported.
[... 195 more lines not kept]
```

**Agent**

The checker passes (41 claims, 0 problems). Now reading the paper to check each claim.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; grep -n -i "^#\|STAR\|Quantification\|Analysis of neural\|Figure [0-9]\.\|Figure S[0-9]\." paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "limit": 380
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 250,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 837,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Table S[1-6]\|=== page" paper/10.1016-j.celrep.2021.110159.txt | sed -n '1,200p' | awk -F: '$1>1536'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 1826,
 "limit": 55
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 2279,
 "limit": 620
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "elsewhere\|with_labels\|'data'\|\"data\"" tools/claims_check.py | head -20; grep -rn "data: elsewhere" claims/*.yaml | head -5
```

```
claims/azcorra-2023.yaml:729:  data: elsewhere
claims/azcorra-2023.yaml:750:  data: elsewhere
claims/azcorra-2023.yaml:774:  data: elsewhere
claims/azcorra-2023.yaml:782:  data: elsewhere
claims/berg-2020.yaml:208:  data: elsewhere
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 2893,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 3342,
 "limit": 360
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2021.110159.txt",
 "offset": 4224,
 "limit": 360
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q --depth 1 https://github.com/emilyasterjones/interneurons_modulate_drive.git imd 2>&1 | tail -2; ls imd 2>/dev/null | head
```

```
Filters
LICENSE
Preprocessing
README.md
Rest Analysis
Run Analysis
Statistics
Shell cwd was reset to
```

**Agent**

The code repository is reachable, so I'll spot-check the code details the criteria cite.

**Agent calls Bash**

```bash
cd $TMPDIR/imd; git log -1 --format=%H; find . -name "*.m" | wc -l; cat Statistics/calcLMM.m | head -80; echo ----; cat Statistics/calcInteraction.m | head -60; echo ----; cat Statistics/HBcorrect.m
```

```
ba727e43c14479fd497afc06402f58c57ad1e43b
70
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
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/imd; git fetch -q --tags --unshallow 2>&1|tail -1; git tag; git log --oneline | head; git rev-parse v1.0.0 2>/dev/null; git diff --stat 63b1acb HEAD 2>&1 | tail -3
```

```
v1.0.0
ba727e4 Adding DOI badge
63b1acb Adding dentate spike and CSD analysis
13ca6e9 adding preprint
1439c78 Update README.md
a579f7b Moved FR script to correct folder
68ed220 Adding fast ripple detection script
ebed7ec Add LMM scripts
8380977 Initial commit
0a49bd3 Initial commit
63b1acb98fdc13b4c8f7af7b7688dbc788ee5c6c
 README.md | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
Shell cwd was reset to
```

**Agent**

Commit matches. Now checking the specific code citations.

**Agent calls Bash**

```bash
cd $TMPDIR/imd; find . -name "*.m" | sort; echo; grep -n "coefTest\|logtransform *=" -r . | head; grep -rn "binrange\|minstd\|immobilecutoff\|immobilitytime" . | head -20
```

```
./Preprocessing/Dentate Spikes/ag_extractdspikes.m
./Preprocessing/Dentate Spikes/plotdspikes.m
./Preprocessing/EEG/ej_rereference.m
./Preprocessing/EEG/extract_eeg.m
./Preprocessing/EEG/filtereeg2.m
./Preprocessing/Fast Ripples/dayprocess_MATLAB_to_IGOR.m
./Preprocessing/Fast Ripples/extract_eeg_1kHzfilt.m
./Preprocessing/Fast Ripples/hfbtimes_to_FF.m
./Preprocessing/Helpers/findTrackFilePath.m
./Preprocessing/Helpers/getTimeStamps.m
./Preprocessing/Linear Track/calcLinearTrackPerformance.m
./Preprocessing/MUA/countMUA.m
./Preprocessing/MUA/extract_spikes.m
./Preprocessing/Position/ag_addvelocity.m
./Preprocessing/Position/ag_posinterp.m
./Preprocessing/Position/extract_pos.m
./Preprocessing/Ripples/ag_extractripples.m
./Preprocessing/Ripples/ej_rippledayprocess.m
./Preprocessing/dayprocess_trodes.m
./Rest Analysis/DSMUA.m
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd/Rest Analysis"; grep -n "setfilterfunction\|binrange" run*.m; sed -n 1,80p getvalidrips.m
```

```
runDSMUA.m:22:f = setfilterfunction(f, 'DSMUA', {'mua','dspikes','chinfo'},'trig',trigcrit,'probe',probecrit);
runDSdescript.m:21:f = setfilterfunction(f, 'DSdescript', {'dspikes','eeg','chinfo'},'trig',trigcrit);
runRTCSD.m:18:f = setfilterfunction(f, 'RTCSD', {'eeg','ripples','chinfo'},'trig',trigcrit,'minstd',5,'win',[0 0.1],'freqband',[20 50]); %,'freqband',[20 50]
runRTMUA.m:19:f = setfilterfunction(f, 'RTMUA', {'mua','ripples','chinfo'},'minstd',3,'trig',trigcrit,'probe',probecrit);
runRTS.m:26:    f = setfilterfunction(f, 'RTspecgram3', {'eeg','ripples','chinfo'},'minstd',3,'trig',trigcrit,'probe',probecrit,'slidingwin',[.1 .01]);
runRTS.m:32:f = setfilterfunction(f, 'RTspecgram3', {'eeg','ripples','chinfo'},'minstd',5,'trig',trigcrit,'probe',probecrit,'slidingwin',[.1 .1]);
runRTcoh.m:23:f = setfilterfunction(f, 'RTcoh', {'eeg','ripples','chinfo'},'trig',trigcrit,'coh',cohcrit,'probe',probecrit,'minstd',3, 'cwin',[.1 .1]);
runcalcLGinstfreq.m:22:f = setfilterfunction(f, 'calcLGinstfreq3', {'eeg','ripples','chinfo'},'appendindex',1,'probe',probe,'minstd',5);
runcalcSWRinstfreq.m:25:f = setfilterfunction(f, 'calcSWRinstfreq', {'eeg','ripples','chinfo'},'appendindex',1,'probe',probe,'minstd',5);
runcalcSWamp.m:19:f = setfilterfunction(f, 'calcSWamp', {'eeg','ripples','chinfo'}, 'win', [0 0], 'interripwin', 0, 'minstd', 5);
runcalcriprates.m:19:binrange = [5 50];
runcalcriprates.m:23:f = setfilterfunction(f, 'calcriprates2', {'ripples'},'appendindex',2,'bins',binrange);
runcalcriprates.m:42:    binnum = length(binrange)-1;
runripdescript.m:21:f = setfilterfunction(f, 'ripdescript', {'ripples','chinfo'},'minstd',5,'trig',trigcrit,'probe',probecrit);
function [mostvalid, excluded, validdur] = getvalidrips(ripples,index,trigindex,excludeperiods, win, minstd, interripwin)

% getvalidrips runs within DF2.0
% given ripples for appopriate day and trigindex,
% Mostvalid criteria:
% - larger than threshold SD
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd"; grep -n "riplong\|chain\|0.2\|ripstds\|probecrit\|overlap\|>= *0.1\|ripdur" "Rest Analysis/ripdescript.m" | head -30; echo ---CSD; grep -n "conv\|/4\|2\*\|smooth\|diff" "Rest Analysis/RTCSD.m" | head; echo ---MUA; grep -n "normrate\|std\|mean" "Rest Analysis/RTMUA.m" | head -20
```

```
17:                probecrit = varargin{option+1};
37:if exist('probecrit','var')
38:    probeindex = evaluatefilter(chinfo,probecrit);
55:        out.ripstds = NaN;
59:        out.riplong = NaN;
61:        out.ripchains = NaN;
86:ripchains = zeros(1,50);
89:    if interriptimes(i)<0.2
90:        counter = counter+1; %add a rip to the chain
92:        ripchains(counter) = ripchains(counter)+1; %end of chain
98:out.ripstds = r.maxthresh(valid);
102:out.riplong = sum(out.riplength>=100)/length(r.startind);
104:out.ripchains = ripchains;
---CSD
48:%smoothing via triangular kernel
50:    %smoothing via triangular kernel
54:    smooth_eeg{i}.data = (a+2*b+c)/4;
59:    %smoothing via triangular kernel
60:    b = smooth_eeg{i}.data;
61:    a = smooth_eeg{i-1}.data;
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd"; sed -n 50,82p "Rest Analysis/RTMUA.m"; sed -n 80,104p "Rest Analysis/ripdescript.m"
```

```
%     valid = find(~isExcluded(rip.starttime,excludeperiods) & ~isExcluded(rip.endtime,excludeperiods));
    rip.starttime = rip.starttime(valid);
    rip.endtime = rip.endtime(valid);
    triggers = rip.threshtime(valid);
    out.riptimes{t} = triggers;
    
    %iterate through probe channels
    for p = 1:size(probeindex,1)
        pmua = mua{probeindex(p,1)}{probeindex(p,2)}{probeindex(p,3)};
        spiketimes = pmua.spiketimes/spikeFs;
        bins = fulltimes(1):binsize:fulltimes(end);
        validinds = ~isExcluded(spiketimes,excludeperiods);
        
        bininds = ~isExcluded(bins,excludeperiods);
        out.baserate{t}{p} = sum(validinds)/sum(validtimes)*Fs; %FR over all immob
        out.sdbaserate{t}{p} = std(histcounts(spiketimes(validinds),bins(bininds))/binsize);      
        
        bins = win(1):binsize:win(2);
        out.psth{t}{p} = NaN(length(triggers),(length(bins)-1)); %no 10x
        out.wave{t}{p} = NaN(length(triggers),40);
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd"; grep -n "setfilterfunction\|band\|\$vel" "Run Analysis/runcomod.m" | head; grep -n "nbins\|bins\|entropy\|log" "Run Analysis/comod.m" | head; grep -n "probe\|sr\|chinfo" "Rest Analysis/runcalcSWamp.m" | head; grep -n "setfilterfunction\|win\|params" "Run Analysis/runcalccoherence.m" "Run Analysis/calccoherence.m" | head -20
```

```
10:% version 3: single bands
32:timefilter{1} =  {'pos', '($vel > 1)'};
36:f = setfilterfunction(f, 'comod', {'eeg'},'PhaseFreqVector',PhaseFreqVector,'AmpFreqVector',AmpFreqVector,'PhaseFreq_BandWidth',PhaseFreq_BandWidth,'AmpFreq_BandWidth',AmpFreq_BandWidth);
71:        phaseaxis = results{1}.frequency_phase + results{1}.phasefreq_bandwidth/2;
72:        ampaxis = results{1}.frequency_amplitude + results{1}.ampfreq_bandwidth/2;
147:        phaseaxis = results{1}.frequency_phase + results{1}.phasefreq_bandwidth/2;
148:        ampaxis = results{1}.frequency_amplitude + results{1}.ampfreq_bandwidth/2;
205:% only works for a single theta & gamma frequency band
357:        phaseaxis = results{1}.frequency_phase + results{1}.phasefreq_bandwidth/2;
358:        ampaxis = results{1}.frequency_amplitude + results{1}.ampfreq_bandwidth/2;
48:    Comodulogram = zeros(length(PhaseFreqVector),length(AmpFreqVector));
88:            comodindex(jj) = (log(2*nbin-1) + sum(comodphase(jj,:).*log(comodphase(jj,:))))/log(2*nbin-1);
91:        Comodulogram(ii,:) = comodindex;
108:                comodindex(jj) = (log(2*nbin-1) + sum(comodphase(jj,:).*log(comodphase(jj,:))))/log(2*nbin-1);
110:            Comodulogram_bin(b,ii,:) = comodindex;
114:    out.comodulogram{c} = Comodulogram;
117:    out.comodulogram_bin{c} = Comodulogram_bin;
12:datafilter{1} = {'chinfo','((isequal($area,''ca1'') && contains($layer,''pyr 1'')) || (isequal($area,''ca1'') && contains($layer,''sr'')))'};
19:f = setfilterfunction(f, 'calcSWamp', {'eeg','ripples','chinfo'}, 'win', [0 0], 'interripwin', 0, 'minstd', 5);
31:    location = '(isequal($area,''ca1'') && contains($layer,''sr''))';
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd/Run Analysis"; sed -n 10,31p runcomod.m; grep -n "nbin *=" comod.m
```

```
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
    'Basil_LT', 'Cumin_LT', 'Dill_LT', 'Nutmeg_LT', 'Paprika_LT', 'Parsley_LT', 'Sumac_LT',...
    'Pepper_LT', 'Sage_LT', 'Anise_LT', 'Thyme_LT', 'OldBay_LT', 'Rosemary_LT',...
    'Provence_LT', 'Saffron_LT'};

epochfilter = [];
epochfilter{1} = {'task','(contains($env,''LT'') && ~contains($descript,''FAIL'') && isequal($treatment,''veh''))'};

datafilter = [];  % load all channels...use embedded filter in run function to get specific ones
datafilter{1} = {'chinfo','(~isequal($area,''dead''))'};
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd/Rest Analysis"; sed -n 36,79p ripdescript.m
```

```
%if looking at SWR properties in CA3 channels
if exist('probecrit','var')
    probeindex = evaluatefilter(chinfo,probecrit);
    if ~isempty(probeindex)
        out.probeindex = probeindex;
        r1 = ripples{probeindex(1,1)}{probeindex(1,2)}{probeindex(1,3)};
        ripstarts = r1.starttime;
        ripends = r1.endtime;
        CA1rips = r.midtime(valid);
        validprobe = [];
        for b = 1:length(ripstarts) %iterate over all SWRs detected in CA3
            if find(isExcluded(CA1rips,[ripstarts(b) ripends(b)]))
                validprobe = [validprobe b]; %use SWR if it's also detected in CA1
            end
        end
        valid = validprobe;
        r = r1;
    else %if no CA3 channel, return empty 
        out.excluded = NaN;
        out.ripstds = NaN;
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd "$TMPDIR/imd/Statistics"; grep -n "fitlme" *.m
```

```
calcLMM.m:34:lme = fitlme(tbl,'Measure~Treatment+(Treatment|Animal)');
calcjointLMM.m:56:lme = fitlme(tbl,'Measure~Genotype*Treatment+((Genotype*Treatment)|Animal)');
calcunpairedLMM.m:46:lme = fitlme(tbl,'Measure~Sex+(Sex|Animal)');
Shell cwd was reset to
```

**Agent**

I've finished reading the paper and checking the code citations. Making the corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "#    followed here as the Methods are silent. The code counts SWRs for rate, length and chains\n#    at 5 SD (runcalcriprates.m binrange [5 50]; runripdescript.m minstd 5) and for MUA at 3 SD\n#    (runRTMUA.m); the Methods say 3 SD, which is the main reading, and the code's 5 SD for\n#    rate, length and chains is a variant.",
 "new_string": "#    followed here as the Methods are silent. The code keeps SWRs at 5 SD for rate, length,\n#    chains and size (runcalcriprates.m binrange [5 50]; runripdescript.m minstd 5), for\n#    instantaneous frequency (runcalcSWRinstfreq.m), SW amplitude (runcalcSWamp.m), CSD\n#    (runRTCSD.m) and SWR-triggered SG power (runRTS.m, the 100 ms step call), and at 3 SD for\n#    MUA (runRTMUA.m) and coherence (runRTcoh.m); the Methods say 3 SD, which is the main\n#    reading, and the code's 5 SD is a variant wherever it uses it."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "#  - Genotype difference (\"PV vs SST\"). Data of the two genotypes pooled; a likelihood ratio\n#    (chi-square) test of feature ~ treatment + (treatment|animal) against the model with\n#    genotype and treatment (paragraph 2; code calcjointLMM.m fits\n#    Measure~Genotype*Treatment+((Genotype*Treatment)|Animal), calcInteraction.m compare()).",
 "new_string": "#  - Genotype difference (\"PV vs SST\"). Data of the two genotypes pooled; a likelihood ratio\n#    (chi-square) test of feature ~ treatment + (treatment|animal) against feature ~\n#    treatment:genotype + (treatment:genotype|animal) (paragraph 2, the main reading). The code\n#    fits the second model as Measure~Genotype*Treatment+((Genotype*Treatment)|Animal)\n#    (calcjointLMM.m) and compares the two with compare() (calcInteraction.m); this is a variant.\n#    Table S3 gives 9 degrees of freedom for every such test."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  criterion: Histological cell counts (Table S1) are not among the deposited data the paper lists",
 "new_string": "  data: elsewhere\n  criterion: Histological cell counts (Table S1) are not among the deposited data the paper lists"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  criterion: Whole-cell patch-clamp recordings in slices, not among the deposited data. The sign of",
 "new_string": "  data: elsewhere\n  criterion: Whole-cell patch-clamp recordings in slices, not among the deposited data. The sign of"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  criterion: Per mouse and treatment, the percentage of CA1 SWRs of 100 ms or longer, pooled over\n    that treatment's sessions; the group values are means over the 16 SST-Cre mice; a paired t\n    test across mice. The code computes the fraction per session with length >= 100 ms\n    (ripdescript.m, riplong), its denominator being all detected events of the session.",
 "new_string": "  criterion: Per mouse and treatment, the percentage of CA1 SWRs longer than 100 ms (the text's\n    \"> 100 ms\"), pooled over that treatment's sessions; the group values are means over the 16\n    SST-Cre mice; a paired t test across mice. The code computes the fraction per session with\n    length >= 100 ms (ripdescript.m, riplong), its denominator being all detected events of the\n    session; its >= is a variant."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    2). Readings of the model data (a) one mean per SWR (Quantification, events for SWRs); (b)\n    every interpeak value (code instfreqs). Method M.",
 "new_string": "    2). The model data are one mean per SWR (Quantification, events for SWRs; Table S3 gives\n    this feature the same df, 112503, as the other per-SWR features); every interpeak value (code\n    instfreqs) is a variant only. Method M."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  - about: rest MUA, CA1-pyr, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = -0.16\n    p: 0.88\n  criterion: A claim of absence.",
 "new_string": "  - about: rest MUA, CA1-pyr, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = -0.16\n    p: 0.88\n  - about: rest MUA, CA3-pyr, PV-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 1.71\n    p: 0.09\n  - about: rest MUA, CA3-pyr, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 1.6\n    p: 0.11\n  - about: rest MUA, DG-gc, PV-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 0.98\n    p: 0.33\n  - about: rest MUA, DG-gc, SST-Cre\n    test: Wilcoxon matched pairs signed rank test\n    statistic: Z = 0.21\n    p: 0.84\n  criterion: A claim of absence."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  - about: SG mean, CA1-sr, SST-Cre\n    test: paired t test\n    statistic: t = 1.8, df 15\n    p: 0.09\n  expected:",
 "new_string": "  - about: SG mean, CA1-sr, SST-Cre\n    test: paired t test\n    statistic: t = 1.8, df 15\n    p: 0.09\n  - about: SG mean, CA3, SST-Cre\n    test: paired t test\n    statistic: t = 0.6, df 15\n    p: 0.6\n  - about: SG mean, DG, SST-Cre\n    test: paired t test\n    statistic: t = 0.1, df 15\n    p: 0.94\n  expected:"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "three regions, each at p < 0.05, and the SST-Cre CA1 mean does not change; the expected values",
 "new_string": "three regions, each at p < 0.05, and the SST-Cre mean changes in none of CA1, CA3 and DG (the\n    text says SST+ suppression did not change SG power at baseline, without naming a region); the expected values"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent**

Now the correlation claims, CA3 SWR claims, dentate spikes and run claims.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    statistic: F(1,14) = 10.97\n    p: 0.0051\n    n: 16 PV-Cre mice\n  criterion:",
 "new_string": "    statistic: F(1,14) = 10.97\n    p: 0.0051\n    n: 16 PV-Cre mice\n  expected:\n  - quantity: R2, CA1 SG power change against SW amplitude change (Figure S2C)\n    value: 0.55\n    tolerance: 0.055\n  - quantity: R2, CA1 SG power change against SWR frequency change (Figure S2D)\n    value: 0.44\n    tolerance: 0.044\n  criterion:"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    plotted in Figures S6-S7). Reproduced when under one reading both correlations are positive\n    with p < 0.05.",
 "new_string": "    plotted in Figures S6-S7). Reproduced when under one reading both correlations are positive\n    with p < 0.05; the R2 values (printed in the panels, and equal to F/(F + 14) from the legend)\n    are compared with tolerance."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    statistic: F(1,5) = 26\n    p: 0.0038\n    n: 7 SST-Cre mice\n  criterion:",
 "new_string": "    statistic: F(1,5) = 26\n    p: 0.0038\n    n: 7 SST-Cre mice\n  expected:\n  - quantity: R2, SG power change against FG power change, CA3\n    value: 0.81\n    tolerance: 0.081\n  - quantity: R2, SG power change against FG power change, DG\n    value: 0.84\n    tolerance: 0.084\n  criterion:"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    conditional responses. Reproduced when under one reading both correlations are negative with\n    p < 0.05.",
 "new_string": "    conditional responses. Reproduced when under one reading both correlations are negative with\n    p < 0.05; the R2 values (printed in Figure S4E, equal to F/(F + 5) from the legend, which\n    assigns 0.81 to CA3 and 0.84 to DG) are compared with tolerance."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  criterion: CA3 SWRs detected on the CA3 pyramidal-layer site, features as for CA1 SWRs (Methods,\n    paragraph 2); Method M. Reproduced when the five stated effects (MUA up in both, length up in\n    both, PV-Cre rate down, PV-Cre frequency down; six tests) all hold; partially reproduced when\n    at least four of the six do.",
 "new_string": "  criterion: CA3 SWRs detected on the CA3 pyramidal-layer site, features as for CA1 SWRs (Methods,\n    paragraph 2); Method M. Which CA3 SWRs enter is open. The Methods detect SWRs on the CA3 site\n    and say no more; the code (ripdescript.m, probecrit branch) keeps for the CA3 descriptors only\n    CA3 SWRs that contain the midpoint of a valid CA1 SWR. Readings (a) all valid CA3 SWRs\n    (Methods); (b) CA3 SWRs overlapping a CA1 SWR (code). Reproduced when the four stated effects\n    (MUA up in both, length up in both, PV-Cre rate down, PV-Cre frequency down; six tests) all\n    hold; partially reproduced when at least four of the six tests do."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    which is not significant. Judged as the text states it. CA3 SWR rate per 1 min bin of\n    immobility; Method M.",
 "new_string": "    which is not significant. Judged as the text states it. CA3 SWR rate per 1 min bin of\n    immobility, with the two readings of which CA3 SWRs enter given in figs3-ca3-swr-pv; Method M."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "5-25 ms (Methods, paragraph 6). Rate per 1 min bin. Method M. Reproduced when all ten parts",
 "new_string": "5-25 ms (Methods, paragraph 6). Rate per 1 min bin. Method M. Reproduced when all eight parts"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.0025\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.0005\n  - about: DG, PV vs SST",
 "new_string": "  - about: CA3, SST-Cre\n    test: F test of the LMM\n    p: 0.8\n  - about: CA3, PV vs SST\n    test: likelihood ratio test\n    p: 0.0025\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 0.0005\n  - about: DG, SST-Cre\n    test: F test of the LMM\n    p: 0.37\n  - about: DG, PV vs SST"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  statement: Suppressing PV+ interneurons increases theta modulation of SG locally in DG and CA3 but\n    not in CA1, while suppressing SST+ interneurons reduces theta modulation of SG in CA1.",
 "new_string": "  statement: Suppressing PV+ interneurons increases theta modulation of SG locally in DG and CA3 but\n    not in CA1, while suppressing SST+ interneurons reduces theta modulation of SG in CA1, and\n    these effects differ between genotypes."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    Methods band definitions). Method M (run family). Reproduced when the PV-Cre increases in CA3\n    and DG and the SST-Cre decrease in CA1 are significant and the PV-Cre CA1 effect is not;\n    partially reproduced when two of the three significant effects hold. The genotype tests are\n    reported; the legend's CA1 value (p = 0.95) does not support a difference there.",
 "new_string": "    Methods band definitions). Method M (run family). Reproduced when the PV-Cre increases in CA3\n    and DG and the SST-Cre decrease in CA1 are significant, the PV-Cre CA1 effect is not, and the\n    CA3 and DG genotype tests are significant; partially reproduced when two of the three\n    significant treatment effects hold. The text says the effects differ between genotypes\n    without naming a region; the legends support it in CA3 and DG only (CA1 p = 0.95), so the\n    CA1 genotype test is reported and not required."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    family). Reproduced when the PV-Cre DG theta frequency increase is significant and none of\n    the other ten tests (two coherences and three frequencies in each genotype, less the one) is;",
 "new_string": "    family). Reproduced when the PV-Cre DG theta frequency increase is significant and none of\n    the other nine tests (two coherences and three frequencies in each genotype, less the one) is;"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "  - about: CA1 FG frequency, P/S treatment\n    test: F test of the LMM\n    p: 0.00012\n  criterion: '\"Largely distinct\" is not given a count. For every feature of Figures S6 and S7, the\n    SST vs P/S genotype test of Method M. Reproduced when the CA1 FG power and FG frequency effects\n    of double suppression are significant increases (the direction of SST+ suppression) and at\n    least half of the features where SST-Cre and P/S treatment effects differ in sign or\n    significance show a significant SST vs P/S test; partially reproduced when the FG exceptions\n    hold but fewer features differ.'",
 "new_string": "  - about: CA1 FG frequency, P/S treatment\n    test: F test of the LMM\n    p: 0.00012\n  - about: CA3 FG frequency, P/S treatment\n    test: F test of the LMM\n    p: 0.0013\n  - about: DG FG frequency, P/S treatment\n    test: F test of the LMM\n    p: 8.6e-5\n  criterion: '\"Largely distinct\" is not given a count, so the claim is judged against the SST vs\n    P/S tests the legends of Figures S6 and S7 show as significant under Method M (p below 0.05/24\n    at rest, 0.05/36 during run). These are eight: SW amplitude (p = 0.00055), CA1 SWR-coincident\n    SG power (0.00089) and SWR instantaneous frequency (0.0017) at rest; CA1 theta modulation of FG\n    (0.00017), DG FG power (0.00019), CA3 FG power (0.00023), DG SG frequency (0.00055) and CA1\n    SG/FG ratio (0.00086) during run. For every feature of Figures S6 and S7, the SST vs P/S test\n    of Method M. Reproduced when the P/S effects on CA1 FG power and on FG frequency in CA1, CA3\n    and DG are significant increases (the direction of SST+ suppression), and the eight SST vs P/S\n    tests are significant; partially reproduced when the FG exceptions hold and some of the eight\n    are. Every feature''s result is listed.'"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "    (sex|animal) with an F test (Quantification, paragraph 2; code calcunpairedLMM.m),\n    Holm-Bonferroni over the experiment's features. Reproduced when SWR size is significantly\n    larger in females and no other feature differs significantly by sex; partially reproduced\n    when SWR size holds and one or two other features differ.",
 "new_string": "    (sex|animal) with an F test (Quantification, paragraph 2; code calcunpairedLMM.m). The\n    correction behind Table S6 is open, and neither plain reading matches the table. Holm over its\n    22 rest features (Quantification, paragraph 3) would not pass the paper's own p = 0.0046\n    (0.05/22 = 0.0023); no correction would make five other features sex differences (SW\n    amplitude 0.032, CA3 SWR length 0.015, run CA3 and DG MUA 0.04, DG theta power 0.032), which\n    the text denies. Readings (a) Holm over the rest and the run features separately; (b)\n    uncorrected p < 0.05. Reproduced when SWR size is larger in females with p < 0.05 and has the\n    smallest sex p-value of all features, and no feature passes reading (a); every feature's\n    p-value is listed against the table's."
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2021.yaml",
 "old_string": "- id: figs5-theta-power-ca1",
 "new_string": "- id: figs4h-fg-theta-modulation-pv\n  statement: Suppressing PV+ interneurons dampens theta modulation of FG during movement.\n  source: Results, theta during movement, paragraph 2; Figure S4H, Figure 6H; Discussion,\n    paragraph 2\n  quote: Overall, suppressing PV+ interneurons in DG and CA3 increased measures of CA3 coupling onto\n    CA1, including enhancing SG power, coherence, and theta comodulation and dampening FG-theta\n    comodulation\n  statistics:\n  - about: CA1, PV-Cre\n    test: F test of the LMM\n    p: 0.0098\n  - about: CA3, PV-Cre\n    test: F test of the LMM\n    p: 0.00041\n  - about: DG, PV-Cre\n    test: F test of the LMM\n    p: 7.5e-11\n  criterion: The summary sentence and the Discussion (\"FG during movement had reduced modulation by\n    theta\") name no region. Modulation index as in fig6h-fg-theta-modulation-sst, amplitude band\n    50-110 Hz, in CA1, CA3 and DG. Method M (run family). The legends give p below 0.05/36 in CA3\n    and DG and p = 0.0098 in CA1. Reproduced when the PV-Cre effect is a significant decrease in\n    CA3 and DG; the CA1 effect is reported with its sign; partially reproduced when it holds in\n    one of the two.\n- id: figs5-theta-power-ca1"
}
```

```
The file claims/jones-2021.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry.

**Agent calls Bash**

```bash
cd  cat >> claims/jones-2021.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Method M, genotype test. The second model is now the Methods' feature ~ treatment:genotype + (treatment:genotype|animal); the code's Genotype*Treatment model is named as a variant (Quantification, paragraph 2; calcjointLMM.m).
  - Method M, SD threshold. The code's 5 SD also applies to SWR size, instantaneous frequency, SW amplitude, CSD and SWR-coincident SG power, and its 3 SD to coherence (the run*.m scripts); the list named only rate, length, chains and MUA.
  - fig1-tables1-expression, figs1ef-exvivo-cno. Added data elsewhere, as histology and slice recordings are not among the deposited data (Data and Code Availability).
  - swr-longer-100ms. The criterion counted SWRs of 100 ms or longer; the text says "> 100 ms", and the code's >= is now a variant.
  - fig3f-swr-frequency-pv. Reading (b), every interpeak value, is no longer a reading of the model data; Table S3 gives this feature the per-SWR df (112503), so one mean per SWR is the paper's choice.
  - tables2-detection-unchanged. Added the CA3-pyr and DG-gc rest MUA tests of Table S2, which the criterion already requires.
  - tables2-rest-sg-pv. Added the SST-Cre CA3 and DG baseline SG tests of Table S2; the criterion now requires no SST-Cre change in any region, as the text names none.
  - figs2cd-sg-predicts-sw-frequency, figs4e-sg-fg-inverse. Added the R2 values printed in Figures S2C-D (0.55, 0.44) and S4E (0.81 CA3, 0.84 DG) as expected values; each equals F/(F + df) from the legends.
  - figs3-ca3-swr-pv, figs3c-ca3-swr-rate-sst. The code keeps for the CA3 SWR descriptors only CA3 SWRs that hold a valid CA1 SWR midpoint (ripdescript.m, probecrit branch); the Methods do not say this, so the two readings are now named. figs3-ca3-swr-pv also said "five stated effects" for four.
  - figs3-dentate-spikes. The criterion said "all ten parts"; the statement has eight.
  - fig5f-sg-frequency-pv. Added the SST-Cre CA3 and DG tests (Figure S4B legend) that the absence part of the claim rests on.
  - fig5g-sg-theta-modulation. The statement left out the text's "these effects were again detectably different between genotypes"; it is added, and the criterion now requires the CA3 and DG genotype tests, where the legends support it, not CA1 (p = 0.95).
  - figs5-theta-coherence-frequency. The criterion said "the other ten tests"; ten tests less the one are nine.
  - figs6-double-unlike-sst. The criterion's rule (at least half of features whose effects differ) was not from the paper; it is replaced by the eight SST vs P/S tests the S6 and S7 legends show as significant under Method M. Added the CA3 and DG P/S FG frequency tests, as the exception is FG frequency without a region.
  - tables6-sex-swr-size. The criterion applied Holm to Table S6, under which the paper's own p = 0.0046 fails (0.05/22); the correction is now named as open, with two readings.
  - Added claim figs4h-fg-theta-modulation-pv. The Results summary (theta during movement, paragraph 2) and the Discussion state that PV+ suppression dampens FG-theta comodulation, and no claim covered it.
  - Open, the correction behind Table S6. Neither Holm nor no correction reproduces the table's pattern of significance; the claim may come out not reproduced on the paper's own numbers under reading (a).
  - Open, fig5e-sg-coherence-run and fig6f-fg-coherence-unchanged. The code (calccoherence.m) computes coherence both over all run periods and per bin, so it does not settle between the two readings; both stay.
  - Open, the code's HBcorrect.m tests each sorted p against its own Holm threshold without stopping at the first failure, so it can mark more tests than Holm does. Method M's sufficient rule (p < 0.05/24 or 0.05/36) holds under both.
  - Open, sex-stratified-effects. Table S7 is not under paper/; its features and p-values are not recorded.
EOF
python tools/claims_check.py claims/jones-2021.yaml paper/10.1016-j.celrep.2021.110159.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -B2 -A6 "data: elsewhere" claims/berg-2020.yaml | head -20; grep -rn "where" schemas/*claims* 2>/dev/null | head; ls schemas 2>/dev/null
```

```
206-    0.15 mm) is on average 1.16 times greater than the thickness of the entire mouse cortex (1.06 ±
207-    0.01 mm; Fig. 1a ).
208:  data: elsewhere
209-  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
210-    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)
211-  expected:
212-  - quantity: human L2 plus L3 thickness
213-    value: 1.23
214-    tolerance: 0.15
--
238-    times the neuronal density of human (165 ± 24.9 thousand cells/mm 3 ) with a homogeneous
239-    distribution across cortical depth.
240:  data: elsewhere
241-  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
242-    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)
243-  expected:
244-  - quantity: human neuron density
245-    value: 27.7
246-    tolerance: 4.5
--
[... 11 more lines not kept]
```

**Agent**

`elsewhere` in the schema means data deposited in another public archive. The histology and slice data are deposited nowhere, so I'm reverting that change.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/jones-2021.yaml'
s=open(p).read()
assert s.count("  data: elsewhere\n")==2
s=s.replace("  data: elsewhere\n","")
old="  - fig1-tables1-expression, figs1ef-exvivo-cno. Added data elsewhere, as histology and slice recordings are not among the deposited data (Data and Code Availability).\n"
assert old in s
s=s.replace(old,"")
s=s.replace("  - Open, sex-stratified-effects.","  - Open, fig1-tables1-expression and figs1ef-exvivo-cno. Histology and slice recordings are not among the deposited data (Data and Code Availability) and the paper names no other archive for them, so data elsewhere does not apply; the criteria say the data are absent.\n  - Open, sex-stratified-effects.")
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/jones-2021.yaml paper/10.1016-j.celrep.2021.110159.txt; grep -n " — \|rather" claims/jones-2021.yaml | head; python -c "
import yaml;d=yaml.safe_load(open('claims/jones-2021.yaml'));print(len(d['claims']),d['checks'][-1]['ready'],len(d['checks'][-1]['changes']))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/jones-2021.yaml'))
def walk(x,path=""):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+"/"+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f"[{i}]")
    elif isinstance(x,str) and ": " in x: print(path, x[:80])
walk(d)
EOF
```

```
/claims[7]/quote found an increase when SST+ interneurons were suppressed (% of SWRs > 100 ms: ve
/claims[36]/criterion "Largely distinct" is not given a count, so the claim is judged against the SST
```

**Agent**

The checker passes and the file is ready for an attempt.

**Checker:** `claims/jones-2021.yaml: 42 claims, 42 quotes, 173 statistical values, 0 problems` (the first run gave 41 claims, 0 problems).

I read the paper's main text, Methods, legends and Tables S1 to S6. I also cloned the paper's code at the cited commit (63b1acb, tag v1.0.0) and checked the code details the criteria rely on.

**Changes, by claim**
- **Method M (header):**
  - The genotype test now uses the Methods' model, `feature ~ treatment:genotype + (treatment:genotype|animal)`. The code's `Genotype*Treatment` model is named as a variant.
  - The code's 5 SD threshold covered more than the file said. It also applies to SWR size, SWR frequency, SW amplitude, CSD and SWR-coincident SG power, and the code uses 3 SD for coherence.
- **swr-longer-100ms:** the criterion now counts SWRs longer than 100 ms, as the text says; the code's ">=" is a variant.
- **fig3f-swr-frequency-pv:** the model data are one mean per SWR. Table S3's degrees of freedom match the other per-SWR features, so the second reading (every interpeak value) is only a variant now.
- **tables2-detection-unchanged:** added the CA3 and DG rest MUA tests from Table S2, which the criterion already required.
- **tables2-rest-sg-pv:** added the SST-Cre CA3 and DG baseline tests. The text names no region, so the criterion now requires no SST-Cre change in any region.
- **figs2cd-sg-predicts-sw-frequency, figs4e-sg-fg-inverse:** added the R² values printed in the panels as expected values (0.55 and 0.44; 0.81 and 0.84). Each matches F/(F + df) from the legends.
- **figs3-ca3-swr-pv, figs3c-ca3-swr-rate-sst:** the code keeps only CA3 SWRs that overlap a CA1 SWR; the Methods don't say this. Both readings are now named. I also fixed a miscount: the claim has four effects, not "five".
- **figs3-dentate-spikes:** "ten parts" changed to the eight the statement has.
- **fig5f-sg-frequency-pv:** added the SST-Cre CA3 and DG tests that the "not SST+" part rests on.
- **fig5g-sg-theta-modulation:** the statement now includes the genotype difference the text claims. The criterion requires it in CA3 and DG only, since the CA1 legend p is 0.95.
- **figs5-theta-coherence-frequency:** "other ten tests" changed to nine.
- **figs6-double-unlike-sst:** the "at least half" rule was not from the paper. It is replaced by the eight SST vs P/S tests that the Figure S6 and S7 legends show as significant under Holm. Added the CA3 and DG FG-frequency tests for the double-suppression group.
- **tables6-sex-swr-size:** applying Holm to Table S6 would fail the paper's own p = 0.0046. The correction is now marked as open, with two readings.
- **New claim, figs4h-fg-theta-modulation-pv:** PV+ suppression dampens how strongly theta modulates fast gamma. The Results summary and the Discussion state it, and no claim covered it.

**Still open**
- **Table S6 correction:** with Holm, the paper's own SWR-size result fails. With no correction, five other features become sex differences the text denies.
- **Run coherence:** the code computes coherence both over all run periods and per time bin, so it doesn't settle which reading the paper used. Both readings stay.
- **Code's Holm step:** `HBcorrect.m` doesn't stop at the first failing test, so it can mark more tests significant than proper Holm. Method M's simpler threshold holds under both.
- **Histology and slice claims (fig1-tables1-expression, figs1ef-exvivo-cno):** these data are deposited nowhere. The schema's `data: elsewhere` means another public archive, so I tried it and reverted it.
- **sex-stratified-effects:** Table S7 is not under `paper/`, so its features and p-values are not recorded.

All of this is recorded under `checks` with `ready: true`. Nothing is committed.

## End of run

56 turns, 6 minutes, $2.59 at API prices, result: success.
