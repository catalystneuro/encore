# tingley-2019 · claims · run 44277106759

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
encore_science
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
pyproject.toml
[... 388 more lines not kept]
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
3	Version: `pilot-16`. Record this version in the attempt's provenance.
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
 "file_path": "claims/tingley-2019.yaml"
}
```

```
1	# Claims for Tingley and Buzsaki (2019), Routing of hippocampal ripples to subcortical
2	# structures via the lateral septum, Neuron 105, 138-149, on dandiset 000218.
3	# Source: the accepted author manuscript in PubMed Central (PMC6952543), full text, read from
4	# its Results, figure legends and STAR Methods. The supplementary figures were not available,
5	# so claims on Figures S1 to S5 rest on the main text that cites them.
6	#
7	# What the author had seen when writing the criteria. The data check: the file list, the
8	# metadata, electrodes, units and their region labels, sleep states, epochs and trials of every
9	# file, and the per-file counts of LS HFOs and hippocampal ripples from the detector below.
10	# While building the detector, a few outputs of single sessions: in DT9 2017-05-02 the
11	# hippocampal units lock to the ripple band at zero time shift (resultant 0.13) and not at
12	# +-20 ms (the clock check); mean LS HFO and ripple durations and frequencies in two sessions
13	# (DT9 2017-05-02 LS 28.8 ms and 156 Hz, ripples 37.7 ms and 151 Hz; DT7 2017-03-25 LS 21.0 ms
14	# and 156 Hz, ripples 32.2 ms and 159 Hz); HFO-triggered LS firing by state in eight sessions
15	# (an increase before the HFO peak and a dip after it in the DT5 sessions, little or none in
16	# the others); the count of phase-locked LS units in two sessions (27 of 49, 0 of 10); the
17	# CA1-LS phase coherence at the ripple peak in two sessions (0.12 and 0.14, jittered 0.04 and
18	# 0.07); and the HFO-triggered band power by region in DT7 2017-03-25 (6 events; medial septum
19	# channels higher than LS). No claim's analysis had been run over all sessions.
20	#
[... 508 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; head -c 3000 paper/*.txt; cat papers/datasets/tingley-2019.yaml 2>/dev/null; python tools/claims_check.py --help 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me read the full text.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/*.txt > $TMPDIR/t.txt; wc -l $TMPDIR/t.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/t.txt",
 "offset": 10,
 "limit": 300
}
```

```
10	University, New York, NY 10003, USA 4 Lead Contact Author Contributions D.T. and G.B. conceived the project. D.T. conducted the experiments and analysis. D.T. and G.B. wrote the manuscript. * 
11	Correspondence: [removed: an e-mail address] 26 11 2019 08 1 2020 105 1 349554 138 149.e5 04 12 2019 08 01 2021 08 01 2021 11 01 2020 16 06 2024 This file is available for text mining. It may also be 
12	used consistent with the principles of fair use under the copyright law. Summary The mnemonic functions of hippocampal sharp wave ripples (SPW-Rs) have been studied extensively. Because hippocampal 
13	outputs affect not only cortical but also subcortical targets, we examined the impact of SPW-Rs on the firing patterns of lateral septal (LS) neurons in behaving rats. A large fraction of SPW-Rs were 
14	temporally locked to high frequency oscillations (HFOs; 120–180 Hz) in LS, with strongest coupling during NREM sleep, followed by waking immobility. However, coherence and spike-LFP coupling between 
15	the two structures were low, suggesting that HFOs are generated locally within the LS GABAergic population. This hypothesis was supported by optogenetic induction of HFOs in LS. Spiking of LS neurons 
16	was largely independent from the sequential order of spiking in SPW-Rs but, instead, correlated with the magnitude of excitatory synchrony of the hippocampal output. Thus, LS is strongly activated by 
17	SPW-Rs and may convey hippocampal population events to its hypothalamic and brainstem targets. eTOC blurb Tingley and Buzsaki 2019 describe that hippocampal sharp wave ripple-related bursts are 
18	routed to subcortical structures through the lateral septum. pmc-status-qastatus 0 pmc-status-live yes pmc-status-embargo no pmc-status-released yes pmc-prop-open-access no pmc-prop-olf no 
19	pmc-prop-manuscript yes pmc-prop-open-manuscript yes pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no pmc-prop-suppress-copyright no 
20	pmc-
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -o -E "Figure [0-9S]+\.? [A-Z][a-z]+|SUPPLEMENT|Supplement[a-z ]*|KEY RESOURCES|Key Resources" $TMPDIR/t.txt | sed -n '1,400p' | awk -F: '$1>300' | head -80
```

```
413:Figure 2. Localization
423:Figure 4. Temporal
429:Figure 5. State
437:Figure 6. Optogenetic
447:Figure 8. Temporal
450:KEY RESOURCES
685:Supplement
737:Supplemental 
738:Figure S1. Related
838:Figure S2. Related
925:Figure S3. Related
966:Figure S4. Related
966:Figure 6. Optogenetic
1015:Figure S5. Related
1015:Figure 7. Variability
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/t.txt",
 "offset": 403,
 "limit": 60
}
```

```
403	Nádasdy Z , Jandó G , Szabó I , Sik A , and Buzsáki G ( 1995 ). Sharp wave-associated high-frequency oscillation (200 Hz) in the intact hippocampus: network and intracellular mechanisms . J. Neurosci 
404	15 , 30 – 46 . 7823136 10.1523/JNEUROSCI.15-01-00030.1995 PMC6578299 Zahm DS , Becker ML , Freiman AJ , Strauch S , Degarmo B , Geisler S , Meredith GE , and Marinelli M ( 2010 ). Fos after single 
405	and repeated self-administration of cocaine and saline in the rat: Emphasis on the basal forebrain and recalibration of expression . Neuropsychopharmacology 35 , 445 – 463 . 19794406 
406	10.1038/npp.2009.149 PMC2795057 Figure 1. HFO events in LS are synchronized population bursts. (A) Example LS high frequency oscillations (HFOs). Each raw trace is an example event from one animal 
407	(20 kHz). (B) Example power spectrum (wavelet transform) for a single LS HFO event (grey overlay is the raw trace). (C) Average power spectrum across all events (N = 6 animals, 29,955 events). 
408	Overlay: LS HFO event triggered LS spike probability, normalized by number of events (black trace; N = 1,989 neurons). Red line is the average spiking probability for an equivalent number of randomly 
409	selected segments for each recording. Bounds are +/− 3 SEM. (D) For each animal (N = 6), each black dot indicates the resultant magnitude and phase angle preference for a single neuron. 1840 of 1989 
410	neurons were significantly (P < 0.05; Rayleigh test) phase-locked to 120–180 Hz oscillations. Radial axis is 0 to 1 (resultant length). Grey values are the number of significantly phase-locked 
411	neurons for each animal. (E) Left: Histogram of all resultant magnitudes (black) and shuffled control (red). Right: Histogram of mean phase angles (black) and shuffled control (red) for significantly 
412	phase locked neurons (P < 0.05). (F) Histograms of CA1 ripple durations (black) and LS HFO durations (magenta). (G) Histograms of CA1 ripple peak frequencies (black) and LS HFO peak frequen
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/t.txt",
 "offset": 680,
 "limit": 345
}
```

```
680	[106] Sharp wave-associated high-frequency oscillation (200 Hz) in the intact hippocampus: network and intracellular mechanisms. J. Neurosci.. 1995. 10.1523/JNEUROSCI.15-01-00030.1995
681	
682	[107] Fos after single and repeated self-administration of cocaine and saline in the rat: emphasis on the Basal forebrain and recalibration of expression. Neuropsychopharmacology. 2010. 
683	10.1038/npp.2009.149
684	
685	##### Supplement: NIHMS1545124-supplement-1.pdf
686	
687	=== page 1 ===
688	adjusted R squared
689	adjusted R squared
690	Power
691	polynomial order
692	polynomial order
693	Phase-locking
694	1
695	2
696	3
697	4
698	5
699	0.1
[... 324 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/DavidTingley/papers.git 2>&1 | tail -2; cd papers && git log -1 --format='%H %cd' && ls && find . -iname '*2019*' -o -iname '*ripple*' -o -iname '*septum*' | head -30
```

```
9f4cd48a44f211956954558b66d776ccbb74d693 Mon Mar 16 13:13:53 2020 +0100
Dockerfile
LS_phasecoding
README.md
./LS_phasecoding/modeling/dynamicWeightingModel-ripple-interval-range.ipynb
./LS_phasecoding/modeling/.ipynb_checkpoints/dynamicWeightingModel-ripple-interval-range-checkpoint.ipynb
./LS_phasecoding/modeling/.ipynb_checkpoints/dynamicWeightingModel-ripple-checkpoint.ipynb
./LS_phasecoding/modeling/.ipynb_checkpoints/dynamicWeightingModel-ripple-Copy1-checkpoint.ipynb
./LS_phasecoding/modeling/dynamicWeightingModel-ripple.ipynb
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/papers; cat README.md; find . -type f -not -path './.git/*' | head -80; git log --oneline | head -20
```

```
# papers
code used for specific papers/projects. If you have any questions feel free to email me: [removed: an e-mail address]

[Tingley, D. and Buzsáki, G. (2018) Transformation of a Spatial Map across the Hippocampal-Lateral Septal Circuit. Neuron](https://github.com/DavidTingley/papers/tree/master/LS_phasecoding)

./README.md
./LS_phasecoding/todo
./LS_phasecoding/generic_spikedetekt_parameters.prm
./LS_phasecoding/README.md
./LS_phasecoding/showExampleNeurons.m
./LS_phasecoding/makeFig2.m
./LS_phasecoding/makeFig3.m
./LS_phasecoding/makeFig1.m
./LS_phasecoding/makeFig6.m
./LS_phasecoding/makeFig5.m
./LS_phasecoding/modeling/dynamicWeightingModel_wo_thetaSeqs_Binder_Compatible.ipynb
./LS_phasecoding/modeling/compressionResults.pdf
./LS_phasecoding/modeling/dynamicWeightingModel.ipynb
./LS_phasecoding/modeling/environment.yml
./LS_phasecoding/modeling/staticWeightingModel.ipynb
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/buzsakilab/buzcode.git 2>&1|tail -1; cd buzcode && git log -1 --format='%H %cd'; f=$(find . -name bz_FindRipples.m); echo $f; grep -n -E "addParameter|minInterRippleInterval|minRippleDuration|maxRippleDuration|thresholds|EMGThresh|durations|passband|peak|noise" $f | head -60
```

```
e615663b2b100782d1f378580f6d7aaa35c12937 Thu Oct 1 16:00:05 2026 -0400
./analysis/SharpWaveRipples/bz_FindRipples.m
11:%    the peaks, and discarding events with excessive duration.
30:%     'thresholds'  thresholds for ripple beginning/end and peak, in multiples
32:%     'durations'   min inter-ripple interval and max ripple duration, in ms
40:%     'noise'       noisy unfiltered channel used to exclude ripple-
41:%                   like noise (events also present on this channel are
43:%     'passband'    N x 2 matrix of frequencies to filter for ripple detection 
45:%     'EMGThresh'   0-1 threshold of EMG to exclude noise
56:%                   .peaks             Nx1 matrix of peak power timestamps 
58:%                   .noise             candidate ripples that were
59:%                                      identified as noise and removed
60:%                   .peakNormedPower   Nx1 matrix of peak power values
79:addParameter(p,'thresholds',[2 5],@isnumeric)
80:addParameter(p,'durations',[30 100],@isnumeric)
81:addParameter(p,'restrict',[],@isnumeric)
82:addParameter(p,'frequency',1250,@isnumeric)
83:addParameter(p,'stdev',[],@isnumeric)
84:addParameter(p,'show','off',@isstr)
85:addParameter(p,'noise',[],@ismatrix)
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims/*.yaml | head -5; git log -5 --format='%h %s' -- claims/ | cat; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
claims/zhuang-2025.yaml
claims/zhu-2022.yaml
claims/zhong-2026.yaml
claims/zheng-2022.yaml
claims/zhang-2021.yaml
dce30a9 Paper match for DANDI:000218: matched
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
[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; head -30 claims/zhuang-2025.yaml; ls targets | head; grep -rl "000218" targets entries 2>/dev/null | head
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
it=items if isinstance(items,list) else list(items.values())
for x in it:
  if '000218' in json.dumps(x)[:200]:
    print({k:v for k,v in x.items() if k in('identifier','id','name','title','description')})
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,re
s=open('targets/dandisets.json').read()
i=s.find('000218'); print(s[max(0,i-200):i+2500])
E
```

```
lation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "contributor Baker, Cody of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000218",
   "name": "Routing of Hippocampal Ripples to Subcortical Structures via the Lateral Septum",
   "published_version": "0.261110.1911",
   "asset_count": 98,
   "size_gb": 1519.0,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Rattus norvegicus - Norway rat"
[... 81 more lines not kept]
```

**Agent**

Now a quick look at the Figure 8 model notebook so the model claim can cite it.

**Agent calls Bash**

```bash
cd $TMPDIR/papers/LS_phasecoding/modeling; python - <<'E'
import json
nb=json.load(open('dynamicWeightingModel-ripple.ipynb'))
for c in nb['cells']:
    src=''.join(c['source'])
    if c['cell_type']=='code': print('----\n'+src[:1500])
E
```

```
----
# this is a simulation of CA1/CA3 'place field' populations that project onto a single LS neuron. 
# david tingley 2018

%matplotlib inline 
from pyNN.neuron import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import scipy.signal as sig   
from scipy.stats.mstats import zscore
from IPython import display
import time
import neo as neo

def get_cmap(n, name='jet'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)

[... 39 more lines not kept]
```

**Agent**

The paper text is complete: main text, STAR Methods, figure legends, and the supplement (Figures S1 to S5). Next I'll run the checker on the old file to see how quotes are matched against this text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/tingley-2019.yaml paper/10.1016-j.neuron.2019.10.012.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/tingley-2019.yaml",
 "content": "# Claims for Tingley and Buzsaki (2019), Routing of hippocampal ripples to subcortical\n# structures via the lateral septum, Neuron 105, 138-149, tested on dandiset 000218.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-18,\n# protocol pilot-16 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; only its title on the archive was read. This file replaces the version of 2026-10-19,\n# whose opening comment recorded outputs of the data and fixed method choices from them; those\n# are removed, and every method detail below is taken from the paper or its code, or named as open.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC6952543, NIHMS1545124), full\n# text as served by NCBI PMC: Summary, Introduction, Results, Discussion, STAR Methods, figure\n# legends and Key Resources Table, with its one supplement (NIHMS1545124-supplement-1.pdf, Figures\n# S1 to S5 and their legends). The main figures were not available as images, so values printed\n# only inside main figure panels (axis labels of Figure 7E among them) could not be read.\n#\n# Code read. (1) github.com/DavidTingley/papers, commit 9f4cd48 (2020-03-16), the repository the\n# Methods link for \"code specific to figures/analyses in this manuscript\". It holds the figure\n# scripts of Tingley and Buzsaki (2018), not of this paper, and the network model of Figure 8\n# (LS_phasecoding/modeling/dynamicWeightingModel-ripple.ipynb, pyNN with NEURON). No analysis code\n# of Figures 1 to 7 is there. (2) github.com/buzsakilab/buzcode, commit e615663 (the current head,\n# not a version dated to the paper), analysis/SharpWaveRipples/bz_FindRipples.m, the detector the\n# Methods name. Its defaults are 130-200 Hz, thresholds [2 5] SD, a minimum inter-event interval\n# of 30 ms before merging, maximum duration 100 ms, minimum 20 ms, EMG threshold 0.9; the event\n# \"peak\" it returns is the time of the minimum (trough) of the filtered signal within the event,\n# and amplitude the maximum normalized squared signal. Where the Methods give a value (120-200 Hz,\n# 2 and 5 SD, 15 and 250 ms) it is used; the merge interval and EMG threshold are the code's.\n#\n# Data the paper used. Long-Evans rats. Five rats (3 males, 2 females) implanted with silicon\n# probes in LS and the dorsal hippocampus (CA1 or CA3), as in Tingley and Buzsaki (2018), and one\n# rat with a tetrode microdrive in LS (rat 1), used in the phase locking analysis: 6 animals with\n# LS recordings. Two further rats for optogenetics (AAV-DLX-ChR2-mCherry in LS, 200 um optic fibres\n# and 50 um tungsten wires, Gaussian and square light pulses from a PulsePal). Each recording is\n# continuous: pre-behavior home cage (PRE), traversal of one of three linear track mazes (BEHAV),\n# post-behavior home cage (POST). Intan RHD2000, 20 kHz wideband; LFP at 1.25 kHz; units sorted\n# with SpikeDetekt and Klustakwik and curated in Klustaviewa. Position by OptiTrack (120 Hz) in\n# four animals, a 30 Hz camera with head LEDs in one; only ballistic trials were analysed. Brain\n# state (NREM, REM, WAKE) scored with the semi-automated method of Watson et al. (2016), manually\n# curated. Electrode depth within LS was estimated per recording from implantation depth, daily\n# drive turns and histology (Methods, Relative anatomical depth within LS); CA1 neuron depth\n# from waveform amplitude across sites relative to the pyramidal layer centre. Measured variables\n# the claims need are LS and hippocampal LFP, unit spike times with region and shank, probe\n# geometry, sleep states, the three epochs and maze trials and position, and for Figure 6 the\n# light stimulation times and waveforms.\n#\n# Methods common to the claims, from the Methods and buzcode.\n# - Detection of CA1 ripples and LS HFOs (Methods, Ripple detection) is bz_FindRipples.m with\n#   120-200 Hz (Butterworth, order 3) on the 1.25 kHz LFP, the normalized squared signal (NSS),\n#   peak threshold 5 SD and start and stop at 2 SD, durations 15 to 250 ms, and noise events on\n#   a non-ripple channel, or the EMG estimated from the LFP (Schomburg et al., 2014) where there\n#   is none, used to exclude events. Duration is stop minus start; amplitude is the maximum NSS;\n#   instantaneous frequency as the Methods give it (Hilbert phase, unwrapped, median filtered\n#   over +-6 bins, difference at the peak power bin divided by 2 pi). For CA3 recordings the\n#   ripple is detected on a CA1 reference electrode (Methods, Experimental model).\n# - Open details of detection. (i) Which channel is used. The Methods say that the input\n#   parameters are stored with each set of detected events; where the dataset holds the events\n#   or their parameters, they are used (reading a); otherwise the channel with the highest\n#   120-200 Hz power in the structure (reading b, the criterion the Methods use for the CA1\n#   pyramidal layer centre). (ii) Whether the SD is taken over the whole recording or a\n#   restricted epoch; the code's default is the whole signal, used here as a standard choice.\n#   (iii) Merge interval and EMG threshold, the code's defaults (30 ms, 0.9), a standard choice.\n#   (iv) The event time. The Methods call it the \"peak power\" bin; the code's peak is the trough\n#   of the filtered signal. Both are readings where a claim uses event times at ms precision.\n# - States. NREM and WAKE are the scored states; WAKE in Figure 5 is \"the waking immobile state\"\n#   (Results, paragraph on coupling). Whether the WAKE events are restricted to immobility by a\n#   speed criterion is not said; readings are all WAKE and WAKE outside maze trials.\n# - Regions. CA1 and CA3 neurons are pooled as hippocampal (HPC) where the paper merges them\n#   (Methods, Experimental model, \"these recordings were therefore merged\").\nschema_version: 2\npaper: doi:10.1016/j.neuron.2019.10.012\nclaims:\n- id: dataset-composition\n  statement: LS was recorded in 6 rats with 1989 LS neurons in the phase locking analysis; 62\n    recordings had a hippocampal population with LS, 37 with CA1 and 25 with CA3; LS HFO rates\n    come from 89 recordings and CA1 ripple rates from 53; recordings held 8 to 74 LS neurons\n    (mean 29.6).\n  source: Results, paragraph 1; Figure 1C and 1D legends; Figure 5B legend; STAR Methods,\n    Experimental model and subject details, and Phase locking analysis\n  quote: The dataset used for Figure 6 consists of 62 recordings with both CA1 and LS\n    simultaneously recorded (N = 37) or CA3 and LS simultaneously recorded (N = 25)\n  expected:\n  - quantity: animals with LS recordings\n    value: 6\n    tolerance: 0\n  - quantity: LS neurons in the phase locking analysis\n    value: 1989\n    tolerance: 198.9\n  - quantity: recordings with CA1 and LS\n    value: 37\n    tolerance: 3.7\n  - quantity: recordings with CA3 and LS\n    value: 25\n    tolerance: 2.5\n  - quantity: recordings with LS HFO rates\n    value: 89\n    tolerance: 8.9\n  - quantity: recordings with CA1 ripple rates\n    value: 53\n    tolerance: 5.3\n  - quantity: mean LS neurons per recording\n    value: 29.6\n    tolerance: 15.5\n  criterion: Counts from the dataset. The Methods sentence names Figure 6, the optogenetic\n    figure; its content (hippocampal populations merged across CA1 and CA3, ripple depth) is\n    that of Figure 7, so it is read as describing the Figure 7 dataset. The tolerance on the\n    mean neurons per recording is the paper's stated SD (29.6 +- 15.5). Readings for the LS\n    neuron count are (a) LS neurons with more than 50 spikes in high 120-200 Hz power epochs\n    (the selection of the phase locking analysis, STAR Methods), (b) all LS units. Reproduced\n    when the animal count matches and all other counts are within tolerance under one reading\n    each; partially reproduced when the animal count matches and at least four of the six other\n    counts are.\n- id: fig1c-hfo-each-animal\n  statement: Transient 120-180 Hz HFOs occur in LS in each of the 6 animals, with a robust\n    increase in the firing probability of LS neurons at the events.\n  source: Results, paragraph 1; Figure 1A to C and legend\n  quote: we observed transient high frequency oscillations (HFOs) in the 120–180 Hz frequency range\n    in each animal (Figure 1A, B) and an associated robust increase in the firing probability of LS\n    neurons (Figure 1C)\n  criterion: LS HFOs detected as in the opening comment. The spike probability is HFO-triggered\n    and normalized by the number of events, against the same measure at an equal number of\n    randomly selected times per recording, with bounds of +-3 SEM across neurons (Figure 1C\n    legend). The bin and window of the triggered histogram are not given; 1 ms bins over +-100\n    ms are a standard plotting choice, and the comparison is made at the bin of the event time\n    and the +-5 ms around it. Per animal, the median instantaneous frequency of its LS HFOs lies\n    in 120 to 180 Hz, and the mean triggered probability at the event exceeds the random-time\n    mean by more than 3 SEM. Reproduced when this holds in all 6 animals, partially reproduced in\n    3 to 5, not reproduced in fewer.\n- id: fig1c-post-burst-suppression\n  statement: LS HFOs are accompanied by a suppression of LS firing immediately after the\n    population burst.\n  source: Results, paragraph on the local origin of LS HFOs; Figures 1C and 5F\n  quote: LS HFOs were significantly shorter than hippocampal SPW-Rs ( Figure 1F ) and were\n    accompanied by a suppression of firing immediately following the population burst\n  depends_on:\n  - fig1c-hfo-each-animal\n  criterion: On the HFO-triggered LS spike probability of fig1c-hfo-each-animal, the paper gives\n    no test or window for the suppression. Reading, with the figure's +-3 SEM bounds, the mean\n    probability after the burst (the bins from the event stop, or 20 ms after the event time, to\n    50 ms after it; the window is open and both ends are reported) is below the random-time mean\n    by more than 3 SEM. Reproduced when it is, not reproduced when it is not.\n- id: fig1c-event-count\n  statement: Across 6 animals, 29,955 LS HFO events were analysed.\n  source: Figure 1C legend\n  quote: Average power spectrum across all events (N = 6 animals, 29,955 events)\n  expected:\n    quantity: LS HFO events\n    value: 29955\n    tolerance: 2995.5\n  criterion: Count of LS HFOs detected as in the opening comment. Readings for the recordings\n    counted are (a) all recordings with LS electrodes, (b) recordings with LS units. Under\n    detection reading (a) the deposited events are counted. Reproduced when one reading is\n    within tolerance.\n- id: figs1-participation\n  statement: On average 16% of LS neurons take part in a given HFO, firing an average of 0.23\n    spikes per event.\n  source: Results, paragraph 1; Figure S1A, B and legend\n  quote: On average, 16% of LS neurons participated in any given event, firing an average of 0.23\n    spikes per event (Figure S1A, B)\n  expected:\n  - quantity: fraction of LS neurons firing in an HFO\n    value: 0.16\n    tolerance: 0.016\n  - quantity: spikes per LS neuron per HFO\n    value: 0.23\n    tolerance: 0.023\n  criterion: The Figure S1A legend defines the first as the proportion of neurons firing at\n    least one action potential in each LS HFO (N = 8 to 74 neurons per recording). The window\n    counted is not given; readings are (a) between the event's start and stop, (b) +-25 ms of\n    the event time. The averaging is open; readings are (i) the mean over all events pooled, with\n    spikes per event the mean over all neuron and event pairs, (ii) the mean over recordings of\n    per-recording means. Reproduced when both values are within tolerance under one combination;\n    partially reproduced when one is.\n- id: fig1d-phase-locking\n  statement: The vast majority of LS neurons (1840 of 1989, 92%) are significantly\n    phase-locked to the 120-200 Hz band (Rayleigh P < 0.05), with a strong unimodal preference\n    for the trough of each cycle.\n  source: Results, paragraph 1; Figure 1D, E and legend; STAR Methods, Phase locking analysis\n  quote: Across entire recordings, the vast majority of LS neurons (1840 of 1989; 92%) were\n    significantly phase-locked to the 120–200 Hz frequency band, with a strong unimodal phase\n    preference for the trough of each cycle (Figure 1D, E)\n  statistics:\n  - test: Rayleigh test\n    p: 0.05\n    p_relation: \"<\"\n    n: 1989 LS neurons, 6 animals\n  expected:\n    quantity: fraction of LS neurons significantly phase-locked\n    value: 0.925\n    tolerance: 0.0925\n  criterion: As the STAR Methods give it. Epochs where the 120-200 Hz power (4th order\n    Butterworth, 7 ms RMS smoothing) is continuously above 2 SD of its mean; the phase of every\n    spike in them from the Hilbert transform; neurons with more than 50 spikes in these epochs;\n    circular mean and resultant per neuron (CircStat); Rayleigh test at p < 0.05 (Figure 1D\n    legend). The null circularly shifts the LFP phases by a random offset, 10 iterations. Open\n    details. The LFP channel is not named; readings are the LS HFO detection channel and the LS\n    channel nearest the neuron's shank. The band is 120-200 Hz in the Methods and Results and\n    120-180 Hz in the Figure 1D legend; the Methods' band is used and the legend's shown as a\n    variant. The denominator readings are (a) neurons passing the 50 spike selection, (b) all LS\n    neurons. The phase convention is the angle of the analytic signal, trough at 180 degrees.\n    The trough preference holds when the circular mean of the preferred phases of significant\n    neurons is within 45 degrees of 180 and a Rayleigh test over them gives p < 0.05 (the 45\n    degree bound is set here; the paper gives none). Reproduced when the fraction is within\n    tolerance under one reading and the trough preference holds; partially reproduced when one\n    of the two holds.\n- id: fig1f-shorter-than-ripples\n  statement: LS HFOs are shorter than CA1 ripples from the same animals (27 +- 9 against\n    31 +- 14 ms; rank-sum P < 0.01).\n  source: Results, paragraph 1; Figure 1F\n  quote: These events were significantly shorter in duration (27±9 vs 31±14 milliseconds) ... than\n    CA1 ripples recorded from the same animals (Figure 1F, G; rank-sum test; P < 0.01)\n  statistics:\n  - test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: LS HFO duration, mean\n    value: 27\n    tolerance: 9\n    unit: ms\n  - quantity: CA1 ripple duration, mean\n    value: 31\n    tolerance: 14\n    unit: ms\n  criterion: Tolerances are the paper's stated SDs. Durations are stop minus start of events\n    detected as in the opening comment, pooled over the animals with both LS and CA1 channels\n    (readings are events from recordings with both channels, and all events of those animals).\n    Rank-sum test of LS against CA1 durations. Reproduced when both means are within tolerance,\n    LS HFOs are shorter and the test gives p < 0.01; partially reproduced when LS HFOs are\n    significantly shorter but a mean is out of tolerance.\n- id: fig1g-slower-than-ripples\n  statement: LS HFOs are slower in frequency than CA1 ripples (147 +- 5.7 against 159 +- 8 Hz;\n    rank-sum P < 0.01).\n  source: Results, paragraph 1; Figure 1G\n  quote: These events were significantly ... slower in frequency (147±5.7 vs 159±8 Hz) than CA1\n    ripples recorded from the same animals (Figure 1F, G; rank-sum test; P < 0.01)\n  statistics:\n  - test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: LS HFO peak frequency, mean\n    value: 147\n    tolerance: 5.7\n    unit: Hz\n  - quantity: CA1 ripple peak frequency, mean\n    value: 159\n    tolerance: 8\n    unit: Hz\n  depends_on:\n  - fig1f-shorter-than-ripples\n  criterion: Tolerances are the paper's stated SDs. Events as for fig1f-shorter-than-ripples;\n    peak frequency is the instantaneous frequency of the STAR Methods (Ripple detection). The\n    Methods' last step (\"taking the difference between samples nearest the peak power bin ...\n    and dividing by two pi\") does not say whether it is multiplied by the sampling rate to give\n    Hz; it is, as a value in Hz requires. Reproduced when both means are within tolerance, LS\n    HFOs are slower and the rank-sum test gives p < 0.01; partially reproduced when LS HFOs are\n    significantly slower but a mean is out of tolerance.\n- id: fig1h-no-amplitude-frequency-correlation\n  statement: LS HFOs show no significant correlation between event amplitude and peak\n    frequency.\n  source: Results, paragraph 1; Figure 1H\n  quote: However, they showed no significant correlation between event amplitude and peak frequency\n    (Figure 1H)\n  depends_on:\n  - fig1g-slower-than-ripples\n  criterion: A claim of absence. Amplitude is the maximum NSS of the event and frequency as in\n    fig1g-slower-than-ripples, over all LS HFOs pooled (Figure 1H is one scatter plot). The paper\n    names no test; the readings are a Pearson and a Spearman correlation at p < 0.05. Reproduced\n    when the test finds no significant correlation, not reproduced when it does; r is reported\n    either way, with per-animal values as a variant. With some 30,000 events a very small r is\n    significant, so r is given beside p.\n- id: fig2-confined-to-ls\n  statement: HFO events are seen only at recording sites within LS, not at sites in\n    neighbouring structures.\n  source: Results, paragraph 2; Figure 2A to C and legend; Discussion, paragraph 2\n  quote: We only observed HFO events at recording sites that were confined to the LS (Figure 2A–C)\n  criterion: Figure 2C shows 120-180 Hz power during LS HFOs by recording depth, with the borders\n    of LS and of cortex and corpus callosum marked. In recordings where a probe spans LS and\n    another structure (sites placed by the dataset's anatomical labels, which the paper derives\n    from the depth estimate of the STAR Methods), the mean 120-180 Hz power at each site within\n    +-25 ms of the LS HFO times, divided by its mean at random times (the window and the random\n    baseline are set here; the paper gives neither). Reproduced when, in every such recording,\n    the median ratio over LS sites exceeds the median ratio of the sites of every non-hippocampal\n    structure and those sites' ratios are below 1.5 (a site without HFOs); partially reproduced\n    when this holds in most such recordings. The hippocampus is left out, as it has its own\n    ripples.\n- id: fig2ef-intermediate-ls\n  statement: HFO power and the proportion of phase-locked neurons are highest in intermediate\n    LS and taper towards its dorsal and ventral borders; both are best fit by a second order\n    polynomial of depth.\n  source: Results, paragraph 2; Figure 2D to F and legend; Figure S1C, D and legend\n  quote: Both the power of HFOs and the proportion of phase-locked neurons were highest in the\n    intermediate LS and tapered off as recordings approached either the dorsal or ventral border of\n    LS\n  depends_on:\n  - fig1d-phase-locking\n  criterion: Per recording, the average 120-180 Hz power of its LS HFO events (Figure 2E) and the\n    percentage of its LS neurons significantly phase-locked (fig1d-phase-locking; Figure 2F),\n    against the recording's estimated relative depth in LS (STAR Methods, Relative anatomical\n    depth within LS). Polynomials of order 1 to 5 are fit and compared by adjusted R squared\n    (Figure S1C, D). Whether the fit is per animal or over all recordings is open (Figure 2F\n    colours dots by animal and shows one black fit line per panel); both readings are run, and\n    power is compared within animals as raw power is not comparable across them. Reproduced when,\n    for both measures, order 2 has the highest adjusted R squared and the fitted parabola opens\n    downward with its maximum inside the depth range; partially reproduced when this holds for\n    one of the two. Not testable without per-recording depth estimates.\n- id: fig3-travelling-waves\n  statement: LS HFOs are travelling waves, posterior to anterior at 1.01 m/s (4 animals),\n    medial to lateral at 0.53 m/s (1 animal) and dorsal to ventral at 2.19 m/s (4 animals).\n  source: Results, paragraph 2; Figure 3 and legend\n  quote: we estimated that the travel speed was 1.01 meters per second in the posterior-to-anterior\n    direction (N = 4 animals), 0.53 meters per second in the medial-to-lateral direction (N = 1\n    animal), and 2.19 meters per second in the dorsal-to-ventral direction (N = 4 animals)\n  expected:\n  - quantity: posterior to anterior speed\n    value: 1.01\n    tolerance: 0.101\n    unit: m/s\n  - quantity: medial to lateral speed\n    value: 0.53\n    tolerance: 0.053\n    unit: m/s\n  - quantity: dorsal to ventral speed\n    value: 2.19\n    tolerance: 0.219\n    unit: m/s\n  criterion: As the Figure 3 legend gives it. The event-averaged LS HFO on each site (Figure 3B\n    averages events across shanks); for each pair of sites aligned to one axis (AP, ML or DV),\n    20 to 800 um apart, the lag between troughs, against the distance between the sites, from\n    the probe geometry. Open details. The alignment of the average is not stated; it is aligned\n    on the event time of the detection channel (both readings of the event time are run). How\n    the speed follows from lags and distances is not stated; readings are (a) the inverse slope\n    of a regression of lag on distance through the origin, (b) the median over pairs of distance\n    divided by lag. Probe orientation in AP and ML comes from the probe layout of the recording.\n    Reproduced when, under one reading, each speed is within tolerance and the sign of the lag\n    puts posterior before anterior, medial before lateral and dorsal before ventral; partially\n    reproduced when the directions hold and at least one speed is within tolerance.\n- id: fig4b-pre-post-unchanged\n  statement: The co-activation of LS neuron pairs during HFOs (excess correlation) is not\n    modulated by waking experience on a familiar maze (PRE against POST, rank-sum P = 0.36).\n  source: Results, paragraph 3; Figure 4A, B and legend; STAR Methods, Excess correlation analysis\n  quote: It also suggested that the degree of co-activation observed is not modulated by waking\n    experience in a familiar environment (Figure 4B; rank-sum test; P = 0.36; PRE vs POST)\n  statistics:\n  - test: rank-sum test\n    p: 0.36\n    n: 7,172 pairs of LS neurons, 53 sessions\n  expected:\n    quantity: LS neuron pairs across different shanks\n    value: 7172\n    tolerance: 717.2\n  criterion: A claim of absence, judged on the paper's test, a rank-sum test of PRE against POST\n    excess correlations over all pairs, at p < 0.05. From the Methods and Results. Pairs of LS\n    neurons on different shanks; three CCGs per pair from spikes during LS HFOs in PRE, during\n    maze traversal (BEHAV) and during LS HFOs in POST; 1 ms bins over +-200 ms; each CCG\n    convolved with a 5 ms and a 200 ms Gaussian, and the excess correlation is the 5 ms version\n    minus the 200 ms version at the zero bin. Open details, each run under both readings. (i)\n    The inclusion rule \"both neurons fired more than 5 spikes within 200 milliseconds of each\n    other\" is read as (a) the CCG holds more than 5 spike pairs within +-200 ms, (b) each neuron\n    has more than 5 spikes with a partner spike within 200 ms; applied in every epoch. (ii) 5 and\n    200 ms are read as the Gaussian SD and, as a variant, its full width. (iii) The CCG\n    normalization is not stated; readings are raw counts and counts divided by the square root\n    of the product of the two spike counts. (iv) BEHAV spikes are those inside maze trials,\n    with all of BEHAV as a variant. \"During HFOs\" is between start and stop. Edges are handled by\n    dividing by the kernel mass inside the window (a standard choice). Reproduced when the test\n    finds no difference, not reproduced when it does; the effect size is reported either way.\n- id: fig4b-hfo-above-behav\n  statement: Excess correlations during HFOs (PRE and POST) are much greater than chance from\n    spikes jittered by +-200 ms and BEHAV excess correlations slightly greater (P < 0.01), and\n    co-activation during HFOs is higher than during maze traversal (P < 0.001).\n  source: Results, paragraph 3; Figure 4B; Figure S3A and legend\n  quote: By randomly jittering each spike by ±200 milliseconds, we found that the excess\n    correlations for HFOs during the PRE and POST epochs were much greater than expected by chance,\n    while excess correlations during the BEHAV epoch were also slightly greater than chance levels\n    ( Figure S3A ; rank-sum test; P < 0.01). This analysis also revealed that during LS HFOs there\n    is a higher degree of co-activation than observed during behavior or expected given LS firing\n    rates (rank-sum test; P < 0.001 for PRE vs BEHAV and BEHAV vs POST)\n  statistics:\n  - about: PRE, BEHAV and POST excess correlations against jittered spikes\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: PRE against BEHAV and BEHAV against POST\n    test: rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4b-pre-post-unchanged\n  criterion: Same pairs and measure as fig4b-pre-post-unchanged under each of its readings. The\n    jittered value moves every spike by a uniform random amount in +-200 ms and repeats the\n    analysis (STAR Methods); one jitter per pair, as the Methods describe one. Reproduced when PRE\n    and POST each exceed BEHAV by rank-sum p < 0.001 and PRE, POST and BEHAV each exceed their\n    jittered values by rank-sum p < 0.01; partially reproduced when one of the two parts holds.\n- id: fig4-sessions-few-change\n  statement: Only 7 of 53 sessions have significantly different excess correlations in PRE and\n    POST (rank-sum P < 0.01), three with PRE below POST and four with PRE above.\n  source: Results, paragraph 3\n  quote: Only 7 out of 53 sessions had significantly different excess-correlation values for PRE and\n    POST epochs (rank-sum test; P < 0.01), three where PRE was less than POST and four where PRE was\n    greater than POST\n  depends_on:\n  - fig4b-pre-post-unchanged\n  expected:\n  - quantity: sessions with pairs\n    value: 53\n    tolerance: 5.3\n  - quantity: fraction of sessions with PRE different from POST\n    value: 0.132\n    tolerance: 0.0132\n  criterion: Per session, a rank-sum test of PRE against POST excess correlations over its pairs\n    at p < 0.01, under the readings of fig4b-pre-post-unchanged. The paper sets no minimum of\n    pairs per session; every session with pairs is tested. Reproduced when the session count and\n    the fraction are within tolerance and both directions occur; partially reproduced when the\n    fraction is below 0.25 and both directions occur.\n- id: fig4c-temporal-bias\n  statement: The temporal ordering of LS spike pairs during HFOs before and after the maze\n    correlates with the ordering during traversal to a similar degree (P = 0.85).\n  source: Results, paragraph 4; Figure 4C and legend; STAR Methods, Temporal bias analysis\n  quote: the spiking structure during HFOs prior to and after maze performance showed correlations\n    with the spike ordering during maze traversal that were similar (Figure 4C; N = 53 recordings;\n    Two-way T-test; P = 0.85)\n  statistics:\n  - test: Two-way T-test\n    p: 0.85\n    n: 53 recordings\n  depends_on:\n  - fig4b-pre-post-unchanged\n  criterion: A claim of absence, judged on the paper's test at p < 0.05. From the Methods, the\n    temporal bias of a pair in an epoch is the CCG summed over 0 to +200 ms minus that over -200\n    to 0 ms, for pairs across different shanks; per recording, the correlation over pairs of the\n    PRE with the BEHAV biases and of the BEHAV with the POST biases. Open details. The\n    correlation is read as Pearson (Skaggs and McNaughton, 1996, whose analysis the Methods\n    follow), Spearman as a variant. The two-sided t-test of the 53 PRE-BEHAV against the 53\n    BEHAV-POST correlations is read as (a) paired by recording, (b) two-sample. The zero bin is\n    left out of both sums. Pairs as in fig4b-pre-post-unchanged. Reproduced when the test finds no\n    difference, not reproduced when it does; the mean difference is reported either way.\n- id: fig4d-compression\n  statement: Cross-correlograms of LS pairs during HFOs correlate with those during traversal\n    above chance up to about 20-fold temporal compression (P < 0.01), similarly for PRE and\n    POST (P > 0.01 for all compression factors).\n  source: Results, paragraph 4; Figure 4D and legend; Figure S3B, C and legend; STAR Methods,\n    Temporal compression analysis\n  quote: We found correlations significantly higher than chance (up to ~20-fold compression; P <\n    0.01) ... However, the strength of this compression was similar for HFOs recorded prior to, and\n    after, maze traversal (P > 0.01 for all compression factors)\n  statistics:\n  - about: HFO against maze traversal CCG correlations above chance, up to about 20-fold compression\n    p: 0.01\n    p_relation: \"<\"\n  - about: PRE against POST, every compression factor\n    p: 0.01\n    p_relation: \">\"\n  depends_on:\n  - fig4b-pre-post-unchanged\n  criterion: From the Methods. CCGs with 1 ms bins; the BEHAV CCG over +-120 ms; the HFO CCG\n    (PRE or POST) over +-120/c ms for compression factor c, interpolated to 241 points and\n    correlated with the BEHAV CCG; c from 1 (+-120 ms) to 50 (+-2.4 ms). Chance is the same\n    correlation with one CCG circularly permuted (Figure 4D legend). Open details. The factors\n    between 1 and 50 are not listed; every integer from 1 to 50 is used. The interpolation is\n    linear (a standard choice). The correlation is Pearson. The tests are not named; readings for\n    actual against chance over pairs are a Wilcoxon signed-rank and a rank-sum test, and for PRE\n    against POST a rank-sum test. Pairs as in fig4b-pre-post-unchanged. Reproduced when PRE and\n    POST each exceed chance at p < 0.01 at every factor up to 15 and PRE and POST do not differ\n    at p < 0.01 at any factor; the largest factor with p < 0.01 is reported and compared with\n    \"~20\". Partially reproduced when they exceed chance up to at least 5 and one of the other\n    parts fails.\n- id: figs3d-hpc-compression-post\n  statement: For hippocampal cell pairs, compression of behavioural spike patterns during CA1\n    ripples is higher after than before the behavioural session, for compression factors 1 to 7;\n    HPC pairs are the only ones with a PRE to POST difference.\n  source: Results, paragraph 5; Figure S3D and legend\n  quote: Only HPC cell pairs had a significant difference between PRE and POST epochs, when\n    examining the correlation of temporally compressed cross-correlograms\n  depends_on:\n  - fig4d-compression\n  criterion: As fig4d-compression, for pairs of hippocampal neurons (same region, CA1 or CA3, per\n    the Methods) with spikes inside CA1 ripples in PRE and POST. Whether HPC pairs are taken\n    across shanks only is not said; readings are across shanks and all pairs. The PRE against\n    POST test is that of fig4d-compression at p < 0.01, the threshold of Figure S3. Reproduced\n    when POST exceeds PRE at p < 0.01 at most factors from 1 to 7; partially reproduced when it\n    does at one or more of them.\n- id: figs2-post-rate-increase\n  statement: Firing rates increase during post-behavior NREM sleep in CA1, CA3 and LS.\n  source: Results, paragraph 5; Figure S2A, B and legend\n  quote: we observed a systematic increase in firing rates during post-behavior NREM sleep in CA1,\n    as well as CA3 and LS populations\n  expected:\n  - quantity: LS neurons in Figure S2A\n    value: 1754\n    tolerance: 175.4\n  - quantity: CA1 neurons in Figure S2A\n    value: 2315\n    tolerance: 231.5\n  - quantity: CA3 neurons in Figure S2A\n    value: 1373\n    tolerance: 137.3\n  criterion: Per neuron, the firing rate during NREM in PRE, during behavior and during NREM in\n    POST, as a change relative to the neuron's whole session average (Figure S2B legend). The\n    Figure S2 legend gives two-way (two-sided) t-tests at p < 0.05; whether paired over neurons is\n    open, and both readings are run. The three N values printed on Figure S2A are read as LS,\n    CA1 and CA3 in the order of the legend (an inference from the supplement's extracted text;\n    their placement on the panel could not be seen). Reproduced when the POST NREM rate exceeds\n    the PRE NREM rate at p < 0.05 in each of LS, CA1 and CA3; partially reproduced when it does\n    in one or two.\n- id: figs2c-no-ls-reactivation\n  statement: After controlling for the change in firing rate, by rate matching or by bin size,\n    LS-LS pairs show no fast timescale reactivation beyond chance, and HPC and HPC-LS pairs give\n    similar results.\n  source: Results, paragraph 5; Figure S2C and legend; STAR Methods, Reactivation analysis\n  quote: When controlling for this change in overall rate — both by down-sampling to rate match (\n    Giri et al., 2019 ) or increasing bin size — we did not observe fast timescale reactivation of\n    LS-LS cell pairs that exceeded what would be expected by chance, given the observed changes in\n    firing rate ( Figure S2C ). We found similar results for HPC and HPC-LS pairs\n  statistics:\n  - about: explained variance against reverse explained variance, per pair set and bin size\n    test: two-way T-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - figs2-post-rate-increase\n  criterion: From the Methods. Explained variance (EV) and reverse explained variance (REV) as\n    in Kudrimoti et al. (1999) and Pennartz et al. (2004), from pair correlation vectors in PRE\n    NREM ripple epochs, BEHAV and POST NREM ripple epochs, with 25 ms and 1 s bins, before and\n    after rate matching (single spikes removed at random until PRE and POST rates are as close as\n    can be, Giri et al., 2019). Open details. \"NREM ripple epochs\" is read as (a) within CA1\n    ripples in NREM, (b) within LS HFOs in NREM for LS pairs. The test across recordings is a\n    two-sided t-test of EV against REV (Figure S2C legend), paired by recording as a reading and\n    two-sample as the other. The rate matching is repeated 10 times and averaged (a standard\n    choice). Reproduced when, with 25 ms bins after rate matching, EV does not exceed REV at p <\n    0.05 for LS-LS pairs, and the same holds for HPC and HPC-LS pairs; partially reproduced when\n    it holds for LS-LS pairs only. The increase of EV over REV with 1 s bins, which the Methods\n    report for every pair set, is shown.\n- id: fig5b-nrem-and-rates\n  statement: LS HFOs occur primarily during NREM sleep, and their rates are lower than those of\n    hippocampal SPW-Rs.\n  source: Results, paragraph 6; Figure 5A, B and legend\n  quote: Across recordings with sleep and behavioral sessions, we primarily observed HFO events\n    during NREM sleep ( Figure 5A ). While this is similar to the state-dependent occurrence of\n    hippocampal SPW-Rs ( Buzsáki et al., 1983 ), the overall rates of LS HFOs were significantly\n    lower than hippocampal SPW-Rs ( Figure 5B )\n  criterion: Per recording with sleep states, the LS HFO rate in NREM and in WAKE (N = 89\n    recordings in Figure 5B), and the CA1 ripple rate in each state (N = 53). The paper names no\n    test. Readings for \"lower\" are (a) a rank-sum test of the 89 LS against the 53 CA1 rates, (b)\n    a signed-rank test over the recordings with both, at p < 0.05, in NREM and over all time.\n    \"Primarily during NREM\" holds when more than half of all LS HFOs fall in NREM and the NREM\n    rate exceeds the WAKE rate in most recordings (signed-rank p < 0.05). Reproduced when both\n    parts hold under one reading; partially reproduced when one does.\n- id: fig5d-lag\n  statement: LS HFOs are reliably coupled to CA1 ripples, with a median peak-to-peak lag of\n    6.4 +- 4.2 ms, CA1 leading LS.\n  source: Results, paragraph 6; Figure 5C, D and legend\n  quote: Across recordings, we observed a reliable coupling of events across structures ( Figure 5D\n    ) with a median peak-to-peak temporal lag of 6.4 ± 4.2 milliseconds (CA1 leading LS)\n  expected:\n    quantity: median lag of LS HFO after CA1 ripple\n    value: 6.4\n    tolerance: 4.2\n    unit: ms\n  criterion: Tolerance is the paper's stated spread. The lag is the LS HFO time minus the CA1\n    ripple time for pairs of events. Open details, each run. Event time is read as the code's\n    peak (trough of the filtered signal) and as the maximum NSS bin. Pairing is not stated;\n    readings are the nearest CA1 ripple within +-50 ms (the coupling window of the Results, Figure\n    7 paragraph) and within +-25 ms (the Figure 5E inset window). The median is (a) over\n    recordings of per-recording medians, (b) over all pairs pooled. Reliable coupling holds when\n    the pooled CA1-LS cross-correlogram (Figure 5D) peaks within +-25 ms above its mean at 100 to\n    200 ms lags by more than 3 SD of those flanks (bounds set here; the paper gives none).\n    Reproduced when the median is positive and within tolerance under one reading and coupling\n    holds.\n- id: fig5e-state-coupling\n  statement: HPC-LS coupling is stronger in NREM sleep than in waking immobility; the fraction of\n    LS HFOs within +-25 ms of a CA1 ripple is 0.3 in NREM and 0.15 in WAKE (P < 6.6e-6).\n  source: Results, paragraph 6; Figure 5D, E and inset, and legend\n  quote: HPC-LS coupling was significantly stronger during NREM sleep than during the waking\n    immobile state (two-way T-test with Bonferroni correction; P < 0.001; Figure 5D , E ). This\n    state-dependent coupling could also be observed when examining the percentage of LS HFO events\n    that occurred within ±25 milliseconds of a CA1 ripple (NREM = 0.3; WAKE = 0.15; P < 6.6e-6\n    two-way T-test; Figure 5E inset)\n  statistics:\n  - about: CA1 ripple and LS HFO cross-correlogram bins, NREM against WAKE\n    test: two-way T-test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 42 recordings\n  - about: fraction of LS HFOs within ±25 ms of a CA1 ripple, NREM against WAKE\n    test: two-way T-test\n    p: 6.6e-6\n    p_relation: \"<\"\n  expected:\n  - quantity: fraction of LS HFOs with a CA1 ripple within 25 ms, NREM\n    value: 0.3\n    tolerance: 0.03\n  - quantity: fraction of LS HFOs with a CA1 ripple within 25 ms, WAKE\n    value: 0.15\n    tolerance: 0.015\n  - quantity: recordings in the average cross-correlogram\n    value: 42\n    tolerance: 4.2\n  criterion: Recordings with sleep states and CA1 ripples (N = 42 in Figure 5E). Per recording and\n    state, the cross-correlogram of CA1 ripples with LS HFOs, and the fraction of LS HFOs with a\n    CA1 ripple within +-25 ms. Open details. The CCG bin and normalization are not given; 5 ms\n    bins over +-200 ms, normalized by the number of CA1 ripples, are a standard choice. The\n    per-bin test of Figure 5E is a two-sided t-test over recordings, Bonferroni corrected over\n    bins; paired by recording and two-sample are both run. The inset fraction is (a) the mean\n    over recordings, (b) all HFOs pooled. WAKE is read as in the opening comment. Reproduced when\n    some bins near zero lag differ at corrected p < 0.001 with NREM higher, the NREM fraction is\n    higher at p < 6.6e-6 (or p < 0.001 as a partial standard), and both fractions are within\n    tolerance under one reading; partially reproduced when NREM is higher at p < 0.001 but a\n    value is out of tolerance.\n- id: fig5f-ripple-triggered-firing\n  statement: LS firing around CA1 ripples is higher during NREM than during waking.\n  source: Results, paragraph 6; Figure 5F and legend\n  quote: This state-dependent coupling could also be observed ... in the SPW-R triggered LS firing\n    rates (two-way T-test with Bonferroni correction; P < 0.001; Figure 5F )\n  statistics:\n  - test: two-way T-test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 1,313 neurons\n  expected:\n    quantity: LS neurons in the ripple-triggered average\n    value: 1313\n    tolerance: 131.3\n  criterion: Per LS neuron in recordings with sleep states and CA1 ripples, the CA1\n    ripple-triggered firing rate (cross-correlogram) for NREM and WAKE ripples separately (Figure\n    5F legend). Open details. Bin and window are not given; 5 ms bins over +-200 ms are a standard\n    choice. The test is a two-sided t-test per bin over neurons, Bonferroni corrected over bins,\n    paired by neuron and two-sample both run; rates raw and divided by the neuron's mean rate in\n    the state are both run. Reproduced when bins around zero lag (within +-25 ms) show NREM higher\n    at corrected p < 0.001 under one reading; not reproduced otherwise.\n- id: fig5f-no-phase-coherence\n  statement: CA1-LS 120-180 Hz phase coherence around CA1 ripples does not differ from that of\n    randomly jittered windows, so LS does not inherit the ripple wave by wave.\n  source: Results, paragraph on the local origin of LS HFOs; Figure 5F inset and legend\n  quote: phase coherence between HFOs and SPW-Rs was not significantly different from a shuffled\n    distribution ( Figure 5F inset)\n  criterion: A claim of absence, judged on the figure's bounds of +-3 SD. The 120-180 Hz phase\n    coherence of CA1 and LS relative to CA1 ripples, against an equal number of randomly\n    jittered time windows (Figure 5F inset legend). Open details. The coherence measure is read\n    as the phase-locking value across ripples of the CA1 minus LS phase at each lag around the\n    ripple time; the jitter is not given, and is read as +-1 s, with 100 jittered sets (standard\n    choices). Reproduced when the ripple-time value lies within the mean +-3 SD of the jittered\n    values, averaged over recordings; not reproduced when it lies above.\n- id: ls-spikes-not-locked-to-ca1-ripples\n  statement: LS spiking is not phase-locked to the individual waves of hippocampal SPW-Rs.\n  source: Results, paragraph on the local origin of LS HFOs\n  quote: LS spiking activity was not phase-locked to individual waves of hippocampal SPW-Rs\n  criterion: A claim of absence. The paper shows no figure or method for it; the phase locking\n    analysis of the STAR Methods (as in fig1d-phase-locking, Rayleigh p < 0.05, more than 50\n    spikes) is applied with the 120-200 Hz phase of the CA1 ripple channel, inside CA1 ripples\n    (reading a) or inside the Methods' high-power epochs on that channel (reading b). Reproduced\n    when the fraction of LS neurons significantly locked is not above the 5% expected by chance\n    (one-sided binomial test, p < 0.05); not reproduced when it is. The fraction and the mean\n    resultant length are reported either way, beside those of fig1d-phase-locking.\n  depends_on:\n  - fig1d-phase-locking\n- id: fig6-optogenetic-hfos\n  statement: Optogenetic activation of LS GABAergic neurons with a Gaussian light waveform\n    induces local oscillations of about 140 Hz in both animals.\n  source: Results, paragraph on the local origin of LS HFOs; Figure 6 and legend; Figure S4;\n    STAR Methods, Optogenetic experiments\n  quote: Using a Gaussian waveform of blue light (450 nm), mimicking the envelope of\n    SPW-R-induced hippocampal excitation, local oscillations of ~140 Hz could be reliably induced (\n    Figure 6C – E ; S2 )\n  statistics:\n  - about: power spectral density per frequency, stimulation against no stimulation\n    test: two-way T-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 2 rats\n  criterion: As the STAR Methods give it. One second windows of the raw LFP (1.25 kHz) around\n    every Gaussian stimulation and as many one second windows starting one second after each;\n    the log power spectral density per window from 1 to 200 Hz; per frequency, a two-sided t-test\n    of stimulation against no-stimulation windows; significance at p < 0.01 (Figure 6E legend).\n    Open details. The PSD estimator is not named; Welch's method with 256 sample segments is a\n    standard choice. Whether the window is centred on the stimulus or starts at it is not said;\n    both are run. Reproduced when, in each animal, the frequency of the largest significant\n    increase lies within 10% of 140 Hz (126 to 154 Hz); partially reproduced when it does in one\n    animal. Square pulse and Figure S4 durations and powers are shown as variants.\n- id: fig7e-ca1-spikes\n  statement: The number of hippocampal spikes in a SPW-R significantly predicts the number of\n    spikes of 38% of LS neurons.\n  source: Results, Figure 7 paragraph 1; Figure 7D, E and legend\n  quote: For many LS neurons (38%), this measure significantly predicted the number of action\n    potentials elicited in the postsynaptic LS neuron (Figure 7D, E)\n  expected:\n    quantity: percent of LS neurons predicted by the number of hippocampal spikes\n    value: 38\n    tolerance: 3.8\n    unit: percent\n  criterion: From the Figure 7E legend. For each LS neuron and feature, the mean squared error\n    (MSE) of predicting the neuron's firing in each SPW-R from the feature, against a\n    distribution of MSEs from shuffled data for the same neuron; the neuron counts when a\n    two-sided t-test of the shuffled MSEs against the actual MSE gives p < 0.05 (actual lower);\n    chance is one shuffled iteration tested against the rest (red points). Recordings are the 62\n    with a hippocampal population and LS (dataset-composition), CA1 and CA3 merged, with SPW-Rs\n    detected on CA1. Open details, which the paper does not give and which can change the\n    outcome. (i) The prediction model, read as (a) a linear regression of spike count on the\n    feature, (b) a generalized linear model with Poisson noise. (ii) Whether the MSE is in-sample\n    or cross-validated, read as 5-fold cross-validation and in-sample. (iii) What is shuffled, read\n    as the feature across SPW-Rs. (iv) The number of shuffles, 100 (a standard choice). (v) The\n    LS firing window, read as SPW-R start to stop and as +-50 ms of the ripple time. (vi) A\n    minimum firing of the neuron is not stated; none is applied, with 20 spikes in SPW-Rs as a\n    variant. The CA1 spike count is all hippocampal units' spikes between start and stop.\n    Reproduced when the percentage is within tolerance under one combination; partially\n    reproduced when no combination is within tolerance but the percentage exceeds the chance rate\n    (binomial p < 0.05) under one; not reproduced otherwise.\n- id: fig7e-state\n  statement: The brain state (WAKE or NREM) in which a SPW-R occurs significantly predicts the\n    spike count of 26% of LS neurons.\n  source: Results, Figure 7 paragraph 1; Figure 7E\n  quote: the rate of spiking for some LS neurons (26%) was significantly predicted by brain state\n    (Figure 7E)\n  expected:\n    quantity: percent of LS neurons predicted by state\n    value: 26\n    tolerance: 2.6\n    unit: percent\n  depends_on:\n  - fig7e-ca1-spikes\n  criterion: As fig7e-ca1-spikes, with the state (NREM or WAKE, coded 1 and 0) as the feature, over\n    the SPW-Rs in those two states.\n- id: fig7e-duration\n  statement: The duration of hippocampal SPW-Rs significantly predicts the spike count of about\n    20% of LS neurons.\n  source: Results, Figure 7 paragraph 1; Figure 7E\n  quote: The duration of hippocampal events could also be used to significantly predict firing rates\n    for ~20% of the LS neurons (Figure 7E)\n  expected:\n    quantity: percent of LS neurons predicted by ripple duration\n    value: 20\n    tolerance: 2\n    unit: percent\n  depends_on:\n  - fig7e-ca1-spikes\n  criterion: As fig7e-ca1-spikes, with the SPW-R duration (stop minus start) as the feature.\n- id: fig7e-ca1-depth\n  statement: The mean depth within the CA1 pyramidal layer of the neurons active in a SPW-R\n    significantly predicts the spike count of 23% of LS neurons.\n  source: Results, Figure 7 paragraph 1; Figure 7D, E; STAR Methods, Relative anatomical depth\n    within CA1, and Spatiotemporal patterns of population activity\n  quote: For a set of LS neurons (23%), the recording depth of the active CA1 population correlated\n    significantly with the number of action potentials elicited (Figure 7D, E)\n  expected:\n    quantity: percent of LS neurons predicted by ripple depth\n    value: 23\n    tolerance: 2.3\n    unit: percent\n  depends_on:\n  - fig7e-ca1-spikes\n  criterion: As fig7e-ca1-spikes, with the ripple depth as the feature, CA1 recordings only (the\n    Methods do not analyse depth for CA3). Ripple depth is the mean relative depth of all CA1\n    neurons firing at least one spike in the SPW-R; a neuron's depth is the offset between its\n    somatic position (waveform amplitude on the three largest sites, cubic-spline interpolated\n    from 20 to 5 um) and the pyramidal layer centre (the site of peak 120-200 Hz power during\n    SPW-Rs on a shank spanning the layer). Not testable without per-site waveforms or neuron\n    depths and the probe geometry.\n- id: fig7e-replay\n  statement: The sequential content of SPW-Rs, by three replay scores, significantly predicts the\n    firing of only 7.9, 6.6 and 7.1% of LS neurons.\n  source: Results, Figure 7 paragraph 2; Figure 7D, E; STAR Methods, Spatiotemporal patterns of\n    population activity\n  quote: The firing rates of only a minority of LS neurons—7.9, 6.6, and 7.1% respectively—could be\n    significantly predicted by the sequential structure of hippocampal events captured by these\n    methods (Figure 7D, E)\n  expected:\n  - quantity: percent of LS neurons predicted by replay score 1 (rank-order correlation)\n    value: 7.9\n    tolerance: 0.79\n    unit: percent\n  - quantity: percent of LS neurons predicted by replay score 2 (Radon transform)\n    value: 6.6\n    tolerance: 0.66\n    unit: percent\n  - quantity: percent of LS neurons predicted by replay score 3 (weighted correlation)\n    value: 7.1\n    tolerance: 0.71\n    unit: percent\n  depends_on:\n  - fig7e-ca1-spikes\n  criterion: As fig7e-ca1-spikes, with each replay score as the feature. Scores from the Methods\n    and their cited sources. (1) The rank-order correlation of spike order in the SPW-R with the\n    order of place field peaks on the maze (Foster and Wilson, 2006; Diba and Buzsaki, 2007). (2)\n    The maximized integral under the line of best fit through the Bayesian posterior (discrete\n    Radon transform; Davidson et al., 2009). (3) The normalized linear weighted correlation of\n    the posterior (Grosmark and Buzsaki, 2016). Open details, none of which the paper gives.\n    Spatial bin size, decoding time bin, the rate maps (one per running direction or pooled), the\n    correlation type of score 1 and its sign (signed and absolute values are both run), and the\n    decoder (the Key Resources Table names the readout.info decoder of Meyers, 2013; a Bayesian\n    decoder as in Davidson et al., 2009, with 2 cm spatial and 10 ms time bins, is the standard\n    reading). Reproduced when each percentage is below 15% and not above the chance rate by more\n    than the paper's values are (all three under 10%); with values within tolerance reported.\n    Partially reproduced when two of three are below 15%.\n- id: fig7e-seqnmf\n  statement: Template sequences extracted from SPW-Rs without supervision (seqNMF) significantly\n    predict the firing of only 8.1% of LS neurons.\n  source: Results, Figure 7 paragraph 3; Figure 7E; Figure S5\n  quote: we found that the percentage of LS neurons whose action potential firing could be\n    significantly predicted with these templates was small (Figure 7E; 8.1%; P < 0.05)\n  expected:\n    quantity: percent of LS neurons predicted by seqNMF templates\n    value: 8.1\n    tolerance: 0.81\n    unit: percent\n  depends_on:\n  - fig7e-ca1-spikes\n  - figs5-seqnmf-variance\n  criterion: As fig7e-ca1-spikes, with the seqNMF template content of each SPW-R as the feature.\n    Open details. How a template becomes a per-SPW-R feature is not said; readings are (a) the\n    SPW-R's loading (summed H) on its best template, (b) a model with all 40 template loadings\n    as predictors. Reproduced when the percentage is within tolerance under one reading; partially\n    reproduced when it is below 15% under every reading.\n- id: figs5-seqnmf-variance\n  statement: Forty seqNMF templates capture more than 95% of the variance in hippocampal SPW-R\n    spiking (mean 96% over 44 recordings), and 88% for hippocampal population bursts.\n  source: Results, Figure 7 paragraph 3; Figure S5 and legend\n  quote: Across recordings, we were able to capture >95% of the variance in hippocampal SPW-R\n    spiking activity with 40 ‘template sequences’ ( Figure S5 )\n  expected:\n  - quantity: mean total percent variance explained by 40 templates, SPW-Rs\n    value: 96\n    tolerance: 9.6\n    unit: percent\n  - quantity: mean total percent variance explained by 40 templates, population bursts\n    value: 88\n    tolerance: 8.8\n    unit: percent\n  - quantity: recordings\n    value: 44\n    tolerance: 4.4\n  criterion: seqNMF (Mackevicius et al., 2019) with K = 40 templates per recording on hippocampal\n    spiking during SPW-Rs (Figure S5A) and during population bursts (S5B). Open details, none\n    given. The binned input (bin size, how SPW-R segments are concatenated), the template length\n    L and the penalty lambda; readings are 1 ms bins with SPW-Rs concatenated, L of 50 ms, lambda\n    0 and 0.001. How population bursts are detected is not given; the standard reading is\n    summed z-scored hippocampal firing above 3 SD. Variance explained is that of seqNMF's\n    reconstruction. Reproduced when the mean for SPW-Rs exceeds 95% under one reading and the\n    other values are within tolerance; partially reproduced when the SPW-R mean is within\n    tolerance only.\n- id: fig7e-content-independent\n  statement: All spike-content-independent ripple features predict LS firing above chance, while\n    all spike-content-based features (three replay scores and seqNMF) do not.\n  source: Results, Figure 7 paragraph 4; Figure 7E, bottom row\n  quote: The P-values for each of these statistical tests demonstrated that all spike\n    content-independent ripple features were significantly different from chance (left seven\n    columns), while all spike content-based ripple features were not significantly different from\n    chance ( Figure 7E ; right four columns; bottom row)\n  depends_on:\n  - fig7e-ca1-spikes\n  - fig7e-state\n  - fig7e-duration\n  - fig7e-ca1-depth\n  - fig7e-replay\n  - fig7e-seqnmf\n  criterion: Per feature, a rank-sum test of the neurons' actual-against-shuffled values (black\n    points, in SD of the shuffled MSE distribution) against their shuffle-against-shuffled values\n    (red points), at p < 0.05 (Results and Figure 7E legend). The seven content-independent\n    columns are not all named in the text; it names hippocampal spike count, ripple depth,\n    brain state and duration, and the Methods define inter-ripple interval (mean of the intervals\n    before and after) and condition (PRE, BEHAV or POST); the seventh could not be read, as the\n    main figure was not available, and is left out. Reproduced when every named\n    content-independent feature differs from chance and none of the four content-based features\n    does; partially reproduced when at least four of six and three of four do.\n- id: fig7e-coupled-only\n  statement: The Figure 7E results are qualitatively similar when only coupled events, SPW-Rs and\n    LS HFOs within +-50 ms of each other, are examined.\n  source: Results, Figure 7 paragraph 4\n  quote: This analysis yielded qualitatively similar results for all ripple features when only\n    ‘coupled’ events—SPW-Rs and HFOs co-occurring within ±50ms of each other—were examined\n  depends_on:\n  - fig7e-content-independent\n  criterion: As fig7e-content-independent, using only SPW-Rs with an LS HFO within +-50 ms (event\n    times as read in fig5d-lag). Reproduced when each feature's test falls on the same side of p\n    = 0.05 as in fig7e-content-independent; partially reproduced when all but one do.\n- id: discussion-medial-septum\n  statement: Recordings in medial septum show no HFOs, and medial septal firing is mainly\n    suppressed at hippocampal SPW-Rs.\n  source: Discussion, paragraph 2\n  quote: Recordings in medial septum, did not have such HFOs and showed primarily a suppression in\n    firing rates\n  criterion: The paper shows no figure or method for it. In recordings with medial septal sites\n    or units (by the paper's anatomical estimate, as the dataset labels them), (a) the 120-180 Hz\n    power ratio of fig2-confined-to-ls at medial septal sites below that at LS sites, and (b) the\n    CA1 ripple-triggered firing of medial septal units (as fig5f-ripple-triggered-firing, all\n    states) below the neuron's mean rate within +-50 ms of the ripple in most units (signed-rank\n    p < 0.05). The window and test are set here. Reproduced when both hold, partially when one\n    does; not testable without medial septal recordings.\n- id: discussion-cingulate-down-state\n  statement: Recordings in deep layers of anterior cingulate cortex show down-state-coupled\n    activity about 50 ms after the CA1 SPW-R.\n  source: Discussion, paragraph 2\n  quote: Recordings more dorsal, in deep layers of anterior cingulate cortex, showed down\n    state-coupled activity approximately 50 milliseconds after the CA1 SPW-R\n  expected:\n    quantity: delay of cortical down-state activity after the CA1 SPW-R\n    value: 50\n    tolerance: 5\n    unit: ms\n  criterion: The paper gives no method. The CA1 ripple-triggered firing of anterior cingulate\n    units (all cortical units, if the dataset gives no finer label), pooled; the delay is the\n    time of the minimum of the mean triggered rate between 0 and 200 ms (reading a), and the\n    time of the extremum of the ripple-triggered cortical LFP in that window (reading b).\n    Reproduced when the delay is within tolerance under one reading; not testable without\n    cortical recordings.\n- id: fig8-model\n  statement: In a model HPC-LS circuit, forward, reverse and scrambled temporally compressed\n    sequences evoke nearly identical responses of the LS neuron.\n  source: Results, last paragraph; Figure 8C, D and legend; STAR Methods, Spiking model of HPC-LS\n    circuit\n  quote: By providing the model with temporally compressed forward, reverse, or scrambled replay\n    events (Figure 8C), we observed that the response of the postsynaptic model LS neuron was nearly\n    identical for all three event types (Figure 8D)\n  data: elsewhere\n  where: GitHub DavidTingley/papers, commit 9f4cd48, LS_phasecoding/modeling/dynamicWeightingModel-ripple.ipynb\n  criterion: The model as in the STAR Methods and the notebook. 50 CA1 and 50 CA3 Hodgkin-Huxley\n    cells with the stated parameters, each with one synapse onto one LS neuron, the ramping\n    weight matrix, no theta input, about 6 ms between neighbouring cells' spikes; forward,\n    reverse and randomly permuted orders; 200 runs with +-3 ms jitter on each ramp. The paper\n    gives no test of \"nearly identical\"; the reading set here is that the mean LS spike count\n    per event type differs from the mean over the three types by less than 10%, and a one-way\n    ANOVA of the counts over the 200 runs gives p > 0.05. Reproduced when both hold; partially\n    reproduced when one does. The scrambled order uses one permutation per run (the notebook's\n    seed is not fixed; a standard choice).\n"
}
```

```
The file claims/tingley-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing a few awkward criteria and dropping one statistic that was a threshold, not a result.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/tingley-2019.yaml",
 "old_string": "    reading). Reproduced when each percentage is below 15% and not above the chance rate by more\n    than the paper's values are (all three under 10%); with values within tolerance reported.\n    Partially reproduced when two of three are below 15%.",
 "new_string": "    reading). Reproduced when each percentage is within tolerance under one combination;\n    partially reproduced when none is within tolerance under a shared combination but all three\n    are below 15%; not reproduced otherwise."
}
```

```
The file claims/tingley-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/tingley-2019.yaml",
 "old_string": "    some bins near zero lag differ at corrected p < 0.001 with NREM higher, the NREM fraction is\n    higher at p < 6.6e-6 (or p < 0.001 as a partial standard), and both fractions are within\n    tolerance under one reading; partially reproduced when NREM is higher at p < 0.001 but a\n    value is out of tolerance.",
 "new_string": "    some bins within +-25 ms differ at corrected p < 0.001 with NREM higher, the NREM fraction is\n    higher at p < 6.6e-6, and both fractions are within tolerance under one reading; partially\n    reproduced when the NREM fraction is higher at p < 0.001 but the bins, the p bound or a\n    value fails."
}
```

```
The file claims/tingley-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/tingley-2019.yaml",
 "old_string": "    firing rate ( Figure S2C ). We found similar results for HPC and HPC-LS pairs\n  statistics:\n  - about: explained variance against reverse explained variance, per pair set and bin size\n    test: two-way T-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:",
 "new_string": "    firing rate ( Figure S2C ). We found similar results for HPC and HPC-LS pairs\n  depends_on:"
}
```

```
The file claims/tingley-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/tingley-2019.yaml paper/10.1016-j.neuron.2019.10.012.txt 2>&1 | tail -30; grep -n -E "—|rather" claims/tingley-2019.yaml | grep -v "quote" ; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/tingley-2019.yaml'))
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and k!='quote' and ': ' in v: print(c['id'],k)
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
E
```

Result: not kept, because it reads the paper's text.

**Agent**

I rewrote `claims/tingley-2019.yaml` to the current protocol. The quote checker passes: 39 claims, 39 quotes, 13 statistical values, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC6952543): full Results, Discussion, STAR Methods, figure legends and Key Resources Table, plus its one supplement (Figures S1 to S5 with legends). There is no PDF of the main paper, so values printed only inside main figure panels could not be read.

**Code read.**
- `DavidTingley/papers` at commit 9f4cd48. It holds the 2018 paper's figure scripts and the Figure 8 model notebook. It has no analysis code for Figures 1 to 7.
- `buzcode` at commit e615663, `bz_FindRipples.m`, the detector the Methods name. This is the current version, not one dated to the paper.

**Counts.** 39 claims; all 39 have quotes and none needed `inferred`. 10 claims have statistics and all 39 have criteria. One claim, `fig8-model`, is `data: elsewhere`, pointing at the model notebook.

**What changed from the old file.**
- **Header:** removed the record of outputs from the data that an earlier author had seen, and the method choices taken from the data (region labels, state names, epoch names). Every method detail is now cited to the paper or code, or named as open. Added provenance, the code commits and a description of the data the paper used.
- **New claims:**
  - `fig1c-post-burst-suppression`
  - `figs3d-hpc-compression-post`
  - `figs2c-no-ls-reactivation`
  - `ls-spikes-not-locked-to-ca1-ripples`
  - `figs5-seqnmf-variance`
  - `fig7e-coupled-only`
  - `discussion-medial-septum`
  - `discussion-cingulate-down-state`
- **Changed claims:** all ids kept.
  - `fig7e-ca1-depth` now has an expected value of 23%, and `fig7e-replay` and `fig7e-seqnmf` now have expected values.
  - Fig 7E significance now follows the legend: a two-sided t-test of the shuffled errors against the actual error.
  - Sample sizes (7,172 pairs, 42 recordings, 1,313 neurons, the Figure S2A counts) are added as expected values.
  - `fig4b-hfo-above-behav` now includes the result that behaviour-epoch correlations are slightly above chance.
  - `fig2ef-intermediate-ls` now uses the Figure S1C/D polynomial-order test.
  - `fig4-sessions-few-change` drops an invented minimum number of pairs per session.

**Details the paper leaves open, and the readings named:**
- **Detection channel:** the events or parameters stored with the data (the Methods say they are stored), or else the channel with the highest 120-200 Hz power.
- **Event time:** the code's trough, or the peak-power bin.
- **Merge interval and EMG threshold:** the code's defaults, 30 ms and 0.9.
- **WAKE:** all waking, or waking outside maze trials.
- **Phase locking:** which LFP channel; band 120-200 Hz (Methods) or 120-180 Hz (legend); denominator neurons with more than 50 spikes, or all LS neurons.
- **Participation:** counting window, and how the mean is taken.
- **Travelling-wave speed:** regression slope, or median of distance over lag.
- **Excess correlation:** what the "more than 5 spikes" inclusion rule means, kernel SD or full width, how the correlogram is normalized, and which behaviour-epoch spikes count.
- **Temporal bias and other t-tests:** paired or two-sample.
- **Compression:** which factors between 1 and 50, and which tests.
- **Correlogram bins** for Figure 5, and the coherence measure and jitter.
- **Fig 1H:** the test, Pearson or Spearman.
- **Fig 5B:** the test for "lower".
- **Fig 7E:** the regression model, cross-validated or in-sample error, what is shuffled, how many shuffles, and the firing window.
- **Replay scores:** decoder and bin sizes.
- **seqNMF:** template length, penalty and binning, and how a template becomes a per-ripple feature.
- **Opto:** how the spectrum is estimated, and where the window sits on the stimulus.
- **Fig 8:** what "nearly identical" means; I set a 10% bound plus an ANOVA.
- **Medial septum and cingulate claims:** no method at all; the criteria fix one.

**Missing from the paper:**
- **Seventh Figure 7E feature:** the text names only six of the seven ripple features that don't depend on spike content; the seventh is only on the figure axis, which I could not see. `fig7e-content-independent` tests the six named ones.
- **Mislabelled sentence:** the Methods describe "the dataset used for Figure 6", but the content is Figure 7's, so I read it that way.
- **No analysis code** for Figures 1 to 7 exists in the linked repository.
- **Figure S2A neuron counts:** which count belongs to which region is inferred from the order of the legend.

## End of run

25 turns, 6 minutes, $2.03 at API prices, result: success.
