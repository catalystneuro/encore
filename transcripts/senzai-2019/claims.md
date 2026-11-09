# 000166 · claims · run 40010666295

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000166/ paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ claims/000166/ paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -200; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ab738558-b1ed-4619-937e-988b89d96b60/tool-results/brka2tloy.txt",
 "limit": 260
}
```

```
File content (39391 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml",
 "limit": 150,
 "offset": 25
}
```

```
25	# pmc.ncbi.nlm.nih.gov).
26	schema_version: 2
27	dataset:
28	  archive: dandi
29	  id: "001453"
30	paper: doi:10.1016/j.cub.2025.04.027
31	claims:
32	- id: stimulus-code-link
33	  kind: link
34	  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
35	    the paper's analysis code and the protocol file of its stimulus software, and the values
36	    computed through that link agree with those the paper's code printed.
37	  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
38	  data: with_labels
39	  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
40	    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41	    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42	    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43	    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44	    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
[... 130 more lines not kept]
```

**Agent**

Read the protocol and the example format. Now reading the paper text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -c 30000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.12.009.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print length($0)}' paper/*.txt | sort -n | tail -5; fold -s -w 200 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 250
}
```

```
1	DOI: 10.1016/j.neuron.2018.12.009
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 2 supplement file(s) from the PMC Open Access cloud data (PMC6367010), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Neuron Neuron 445 elsevierwt 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title Elsevier Sponsored Documents PMC6367010 PMC6367010.2 6367010 6486657 30635232 
8	10.1016/j.neuron.2018.12.009 S0896-6273(18)31085-7 2 Article Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse Senzai Yuta 1 4 5 
9	Fernandez-Ruiz Antonio 1 5 Buzsáki György [removed: an e-mail address] 1 2 3 6 ∗ 1 Neuroscience Institute, New York University, Langone Medical Center, New York, NY 10016, USA 2 Department of Neurology, 
10	Langone Medical Center, New York University, New York, NY 10016, USA 3 Center for Neural Science, New York University, New York, NY 10003, USA ∗ Corresponding author [removed: an e-mail address] 4 
11	Present address: Department of Physiology, University of California, San Francisco, San Francisco, CA 94158, USA 5 These authors contributed equally 6 Lead Contact 06 2 2019 101 3 333446 500 513.e5 5 
12	10 2018 27 11 2018 4 12 2018 06 02 2019 06 05 2019 12 05 2026 6367010 10.1016/j.neuron.2018.12.009 NIHMS1516370 1 08 01 2019 6486657 10.1016/j.neuron.2018.12.009 2 06 02 2019 © 2019 The Authors 2019 
13	https://creativecommons.org/licenses/by/4.0/ This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Summary The relationship between mesoscopic local 
14	field potentials (LFPs) and single-neuron firing in the multi-layered neocortex is poorly understood. Simultaneous recordings from all layers in the primary visual cortex (V1) of the behaving mouse 
15	reveale
[... 235 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 250,
 "limit": 200
}
```

```
250	why more E-I than E-E pairs were identified in our study. Yet our under-sampled population can still be regarded as representative for the relative distribution of the connectivity features. 
251	Surprisingly, most E-I and I-E connections were across layers, including deep-to-superficial and superficial-to-deep links. Layer 2/3 neurons innervated >3 times as many layer 4/5 principal cells and 
252	interneurons as their peers in the home layer. Connection strength tended to cluster around a few hub neurons ( Fujisawa et al., 2008 , English et al., 2017 , Bock et al., 2011 , Song et al., 2005 ). 
253	We also found that reciprocal connections between E and I neurons ( Song et al., 2005 ) varied across layers and were almost twice as frequent in layer 5 compared with other layers. These findings 
254	indicate that cortical connectivity is highly structured, and interlaminar interactions are fundamental to multi-layer cortical operations ( Song et al., 2005 ). The use of higher density, multishank 
255	probes in future experiments will undoubtedly increase the yield of synaptically connected neurons and provide more reliable quantification than we found in the present experiments. This expected 
256	progress is facilitated by the fact that the number of neuron pairs increases as the square of the number of units recorded. Spike transmission probability between superficial and deep layers was 
257	stronger in the waking animal for both E-I and E-E pairs, compared with non-REM sleep. This finding, combined with the suggestion that thalamocortical synapses are not affected by brain state ( 
258	Stoelzel et al., 2009 ), supports the hypothesis of top-down control of visual processing ( Gilbert and Li, 2013 , Bastos et al., 2015 ). In contrast, spike transmission strength increased between 
259	E-E pairs and I-E pairs during non-REM sleep, preserving the E-I balance ( Atallah and Scanziani, 2009 ) even during the UP state of slow oscillation, associated with strong recurr
[... 190 more lines not kept]
```

**Agent**

Main text and STAR Methods read. Now the supplement section of the text.

**Agent calls Bash**

```bash
sed -n 450,600p $TMPDIR/p.txt; grep -n "SUPPLEMENT\|supp1\|supp2\|=====" $TMPDIR/p.txt | head
```

```
https://github.com/cortex-lab/KiloSort
https://github.com/kwikteam/phy
https://sccn.ucsd.edu/eeglab/
http://atoc.colorado.edu/research/wavelets/
https://www.cambridgeneurotech.com/silicon-probes
http://intantech.com/RHD2000_evaluation_system.html
mailto:[removed: an e-mail address]
https://github.com/buzsakilab/buzcode/tree/master/detectors/detectStates/SleepScoreMaster
http://buzsakilab.com
10.1016/j.neuron.2018.12.009

Layer-Specific Physiological Features and Interlaminar Interactions in the Primary Visual Cortex of the Mouse

[1] Functional connectivity between simple cells and complex cells in cat striate cortex. Nat. Neurosci.. 1998. 10.1038/1609

[2] Correlation of synaptic inputs in the visual cortex of awake, behaving mice. Neuron. 2018. 10.1016/j.neuron.2018.08.008

[3] Instantaneous modulation of gamma oscillation frequency by balancing excitation with inhibition. Neuron. 2009. 10.1016/j.neuron.2009.04.027

[4] Characterization of neocortical principal cells and interneurons by network interactions and extracellular features. J. Neurophysiol.. 2004. 10.1152/jn.01170.2003
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 600,640p $TMPDIR/p.txt; grep -n "^\[SUPP\|^===\|^---\|Figure S[0-9]" $TMPDIR/p.txt | head -60
```

```
[69] Laminar analysis of visually evoked activity in the primary visual cortex. Proc. Natl. Acad. Sci. U S A. 2012. 10.1073/pnas.1201478109

##### Supplement: mmc1.pdf

=== page 1 ===
Neuron, Volume 101
Supplemental Information
Layer-Specific Physiological Features
and Interlaminar Interactions in the Primary
Visual Cortex of the Mouse
Yuta Senzai, Antonio Fernandez-Ruiz, and György Buzsáki

=== page 2 ===
mouse 5
mouse 10
*
*
*
*
*
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
for r in 703,716 875,900 988,1009 1185,1203 1300,1315 1387,1398 1419,1433 1534,1556; do sed -n ${r}p $TMPDIR/p.txt; echo ----; done
```

```
=== page 3 ===
 
 
Figure S1: Histological verification of probe location and physiological 
landmarks, related to Figure 1. 
Additional examples of histological verification of probe location along V1 cellular layers 
(A, C, E). Small electrolytical lesions were performed with the two electrodes highlighted 
on the silicon probe sketch. B, D, F) Multi-unit (MUA) spectral power (500 Hz – 5 kHz) 
distribution as a function of depth and average CSD map for DOWN-UP transitions of 
non-REM sleep and for visual stimulation when available. Horizontal dashed lines 
indicate subjective layer borders estimated from the histological sections. 
 
 

----
=== page 5 ===
 
Figure S2: Decomposition of cortical layers by gamma LFPs, related to Figure 2.  
A) Averaged mean-subtracted coherence spectra during waking, non-REM and REM, 
referenced to a recording site in the superficial (top), layer 4 (middle) or deep layer 
[... 135 more lines not kept]
```

**Agent**

Full text, STAR Methods and supplement legends (Figures S1 to S8) are all present. Next: the dataset's archive description and the linked code (buzcode).

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000166/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000166/versions/draft/info/" | python -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/buzsakilab/buzcode.git && cd buzcode && git rev-parse HEAD && git log -1 --format=%cd && ls; ls detectors detectors/*; ls analysis 2>/dev/null | head -50
```

```
e615663b2b100782d1f378580f6d7aaa35c12937
Thu Oct 1 16:00:05 2026 -0400
Contents.m
Export2NWB
GUITools
LICENSE
analysis
compileBuzcode.m
database
detectors
docs
externalPackages
generalComputation
io
preprocessing
readme.txt
tutorials
utilities
visualization
detectors/bz_EMGFromLFP.m
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode; ls analysis/monosynapticPairs analysis/cellTypeClassification analysis/spikes analysis/spikeLFPcoupling; grep -rli "senzai\|V1\b" --include=*.m . | head; grep -rl "cch_conv\|CCG.*Poisson\|poissinv\|0.000001\|1e-6\|99.9999" --include=*.m . | head
```

```
analysis/cellTypeClassification:
BrendonClassificationFromStark2013
bz_CellMetricsSimple.m

analysis/monosynapticPairs:
CCG.m
CCGHeart.c
CCGHeart.mexw64
ProbSynMat.mat
blank.file
bz_GetMonoSynapticallyConnected.m
bz_GetSynapsembles.m
bz_MonoSynConvClick.m
bz_PlotMonoSyn.m
bz_cch_conv.m
bz_fitPoissPlasticity.m
utils

analysis/spikeLFPcoupling:
CircularMean.m_deprecate
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode/analysis/monosynapticPairs; sed -n 1,200p bz_GetMonoSynapticallyConnected.m | grep -v "^\s*$" | head -150; sed -n 1,60p bz_cch_conv.m | grep -v "^\s*$"
```

```
function mono_res = bz_GetMonoSynapticallyConnected(basepath,varargin)
%% Method for estimating likelihood of monosynaptic connectivity based off of relative spike timing
% Based off of Stark and Abeles 2009 and verified for PYR -INT in English et al., 2017
% Assumes network synchrony is low frequency and that synapses induce high
% frequency additive "injected" excess synchrony above that low frequency
% network co-modulation. In addition this model assumes that synaptic
% contribution should be delayed 0.8 -2.8ms (this will change according to
% cell type and inter somatic distance!). 
% to get probabilities derived from English et al., 2017, you must have 'ProbSynMat.mat'
% see bz_MonoSynConvClick 
%%%  OPTIONAL INPUTS:
%%%
%%%  binSize = timebin to compute CCG (in seconds)
%%%
%%%  duration = window to compute CCG (in seconds)
%%%
%%%  epoch = [start end] (in seconds)
%%%
%%%  cells = N x 2 matrix -  [sh celID] to include (NOTE indexing will be
%%%          done on full spikeIDlist
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode; grep -n "addParameter\|binSize\s*=\|conv_w\s*=\|alpha\s*=\|prob\b\|trans" analysis/monosynapticPairs/bz_MonoSynConvClick.m | head -40; ls analysis/monosynapticPairs/utils; grep -rn "function" analysis/cellTypeClassification/bz_CellMetricsSimple.m | head; grep -n "burst\|Burst" analysis/cellTypeClassification/bz_CellMetricsSimple.m | head
```

```
15:%%%  binSize = timebin to compute CCG (in seconds)
24:%%%  conv_w = # of time bins for computing the CI for the CCG.
26:%%%  alpha = type I error for significance testing using convolution
34:%%%  mono_res.alpha = p-value
39:%%%  mono_res.conv_w = convolution windows (ms)
41:%%%  mono_res.binSize = binSize;
74:binSize = .0004; %.4ms
79:conv_w = .010/binSize;  % 10ms window
80:alpha = 0.001; %high frequency cut off, must be .001 for causal p-value matrix
101:            binSize = varargin{i+1};
115:            conv_w = varargin{i+1};
118:            alpha = varargin{i+1};
299:prob = temp./permute(repmat(nn2,1,1,size(ccgR,1)),[3 1 2]);
306:mono_res.prob = prob;
313:mono_res.binSize = binSize;
318:mono_res.conv_w = conv_w;
calculate_X.m
getCubicBSplineBasis.m
nll_poissPlasticity.m
1:function [cell_metrics] = bz_CellMetricsSimple(spikes,sr)
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode; sed -n 120,310p analysis/monosynapticPairs/bz_MonoSynConvClick.m | grep -v "^\s*%\|^\s*$" | head -120
```

```
error('Incorrect value for property ''alpha''');
            end
        case 'plot',
            plotit = varargin{i+1};
            if ~islogical(plotit),
                error('Incorrect value for property ''plot''');
            end
        case 'sorted'
            sorted = varargin{i+1};
        otherwise,
            error(['Unknown property ''' num2str(varargin{i}) ''' (type ''help LoadBinary'' for details).']);
    end
end
if ~sorted
    [spiketimes,b] = sort(spiketimes);
    spikeIDs = spikeIDs(b,:);
end
[status] = InIntervals(spiketimes,epoch);
allID = unique(spikeIDs(:,3));
kp = ismember(spikeIDs(:,1:2),cells,'rows') & status;
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2018.12.009.supp2.pdf')
for i,p in enumerate(d):
    t=p.get_text()
    if 'Figure 7' in t and 'Spike Transmission Probability' in t: print('fig7',i)
    if 'Figure 6' in t and 'Physiological Properties' in t: print('fig6',i)
    if 'Figure 8' in t and 'DOWN State-Active Neurons' in t: print('fig8',i)
    if 'Figure 2' in t and 'Cortical Layer Identification' in t: print('fig2',i)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm pdftotext; pip list 2>/dev/null | grep -i -E "pdf|mupdf"
```

```
(Bash completed with no output)
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.12.009.supp2.pdf",
 "pages": "7-9"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 2230,2360p $TMPDIR/p.txt
```

```
became weaker during non-REM sleep compared with waking
(L2/3 E cells to L5 I cells, p = 0.0012; L2/3 E cells to L4 I cells,
p = 0.0010; and L2/3 E cells to L5 E cells, p = 0.015; signed
rank test; Figures 7D–7F, 7H, and 7I). In contrast, putative E-E
spike transmission in the deep layers (layer 5/6 to layer 5/6
principal cells) significantly increased during non-REM sleep
compared with waking (p = 0.0061, signed rank test; Figures
7G and 7I). These results indicate that communication from su-
perficial to deep layers increases during waking, while excitatory
IC1
IC2
IC3
IC4
IC5
IC6
30
50
100
frequency (Hz)
100
[... 111 more lines not kept]
```

**Agent**

I can't render PDF pages here (no poppler), but the text has every legend and number, so figures aren't needed. Checking which fields the example uses, then writing the claims.

**Agent calls Bash**

```bash
cd  grep -ohE "^\s*-?\s*[a-z_]+:" claims/*/*.yaml | sed 's/^[ -]*//' | sort | uniq -c | sort -rn | head -40; sed -n 1,80p tools/claims_check.py
```

```
7085 value:
   7085 quantity:
   7066 tolerance:
   6752 id:
   6538 statement:
   6538 source:
   6459 quote:
   6135 criterion:
   5606 p:
   5346 test:
   4642 about:
   3096 unit:
   2859 n:
   2684 statistics:
   2655 expected:
   2306 depends_on:
   2134 statistic:
   1518 p_relation:
   1217 data:
    947 corrected:
[... 100 more lines not kept]
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
cd  git show --stat HEAD | head; f=$(git show --name-only --format= HEAD | grep claims/ | head -1); head -40 $f
```

```
commit 16cdb219c9579bb75831bce27ff670dfef44cd2f
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Fri Oct 23 15:20:23 2026 -0400

    Claims for DANDI:000223, checked
    
    From attempt/000223, after its claims check said the file is ready (docs/pipeline.md).

 claims/000223/10.1088-1741-2552-ac8765.yaml | 388 ++++++++++++++++++
 transcripts/000223/claims-check-report.md   |  21 +
# Claims for Xue, Buccino, Saseendran Kumar, Hierlemann & Bartram (2022) on dandiset 000223.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the accepted author manuscript in PubMed Central (PMC7613561, UKPMC funders author
# manuscript), as served by ncbi_pmc, full text with Methods, figure legends and Table 1, and its
# one supplement (EMS152915-supplement, three figure supplements of Figure 1: indicator expression,
# demixing example, burst detection example). The version of record was not read. No PDF of the
# main text was available; none was needed, as Table 1 is legible in the text.
#
[... 30 more lines not kept]
```

**Agent**

I have what I need: the full text, STAR Methods, supplement legends S1 to S8, buzcode, and the dandiset metadata (19 subjects, Units, LFP, electrodes). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000166/10.1016-j.neuron.2018.12.009.yaml",
 "content": "# Claims for Senzai, Fernandez-Ruiz & Buzsaki (2019) on dandiset 000166.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record (Neuron 101, 500-513.e5, 2019, CC BY) as served by Europe PMC\n# (PMC6367010), full text with Results, figure legends and STAR Methods, and its two supplements\n# from the PMC Open Access data: mmc1.pdf (Document S1, legends and panels of Figures S1 to S8) and\n# mmc2.pdf (Document S2, the article plus supplemental information, a PDF copy of the same text).\n# No PDF page was rendered (no renderer was available); every number used here is in the text.\n#\n# Code read: the paper links no analysis code of its own. Its Key Resources Table links buzcode\n# (https://github.com/buzsakilab/buzcode), read at commit e615663b2b100782d1f378580f6d7aaa35c12937\n# (2026-10-01; the commit the paper used is not given). It is the lab's general MATLAB toolbox. The\n# parts that bear on the paper are detectors/detectStates/SleepScoreMaster (brain state scoring, linked\n# by the Methods), detectors/detectEvents/DetectSlowWaves.m (UP and DOWN detection after Levenstein et\n# al., as the Methods describe), analysis/monosynapticPairs (bz_MonoSynConvClick.m, bz_cch_conv.m;\n# CCG convolution baseline after Stark and Abeles 2009 and transmission probability after English et al.\n# 2017) and the EEGLAB runica used for ICA. bz_MonoSynConvClick defaults (0.4 ms bins, a 10 ms window\n# with a hollowed Gaussian, alpha 0.001 with a correction over bins, synaptic window 0.8 to 4 ms) differ\n# from the paper's STAR Methods (0.5 ms bins, 7 ms SD Gaussian, 99.9999th Poisson percentile, two\n# consecutive bins within +1.5 to +4 ms); the Methods are followed and the code is a variant. Its\n# transmission probability is (CCG minus convolution predictor) divided by the presynaptic spike count.\n#\n# Data the paper used: 19 male mice (3 Ai35, 5 PV-Cre::Ai32, 9 VGAT-Cre::Ai32, 1 CaMKII-Cre::Ai35,\n# 1 CaMKII-Cre::Ai32), each with a single-shank 64-site linear silicon probe (Cambridge NeuroTech H3,\n# 20 um spacing) in V1, recorded in the home cage during sleep and free behaviour, wide band at 20 kHz,\n# LFP downsampled to 1.25 kHz. One session per mouse was used for unit clustering (1,472 units, Kilosort\n# then Phy). Brain states (waking, non-REM, REM) were scored with SleepScoreMaster and checked by hand;\n# UP and DOWN states of non-REM were detected from high gamma power (100-400 Hz) and delta (0.5-8 Hz).\n# Light flashes (520 nm, 500 pulses at 0.5 Hz, 400 ms in the Methods, 100 ms in the Results) were given\n# in 13 mice for visual evoked responses; blue light pulses (450 nm, 10 ms, 500 at each of three\n# intensities, 1 Hz) tagged PV and VGAT neurons. Lesions for histology were made in 4 mice. The dandiset\n# (title as the paper, 19 NWB files, 19 subjects) lists LFP, Units and ElectrodeGroup as its measured\n# variables. Whether it holds state intervals, UP and DOWN events, light pulse times or opto tags is the\n# author's to find.\n#\n# Layer groups used throughout. The eight K-means clusters of Figure 5C are numbered 1 to 8 from the\n# surface (Figure 7 legend, \"Neuron groups 1-8 are as in Figure 5C\") and labelled L2, L3, L4, L5?, L5a,\n# L5b, L6s, L6d (Figure 5C axis). Layer 2/3 is clusters 1 and 2, layer 4 cluster 3, layer 5 clusters 4,\n# 5 and 6 (Figure S8B legend, \"clusters 4, 5 and 5 (layer 5)\", read as 4, 5 and 6), layer 6 clusters 7\n# and 8 (Results, \"The bottom two clusters (black and gray) were designated as layer 6 neurons\").\n# Claims on layer groups depend on fig5b-eight-clusters.\n#\n# Unit classes (STAR Methods, Classification of units based on spike waveforms). Positive waveform units\n# and putative fiber units (kurtosis beyond 5 SD) are set aside; of the remaining negative waveform units,\n# trough-to-peak latency above 0.55 ms is a putative E cell and at most 0.55 ms a putative I cell.\n#\n# Monosynaptic connections (STAR Methods, Detection of monosynaptic functional connectiveties). CCGs in\n# 0.5 ms bins, convolved with a Gaussian of 7 ms SD as baseline predictor; a bin is significant above the\n# 99.9999th percentile of the Poisson distribution at the predicted rate (below the 0.0001th for\n# troughs, the symmetric reading for \"negative deviations\"); a connection when at least two consecutive\n# bins within +1.5 to +4 ms pass. Open details, each named in the claims that use them: whether the\n# Gaussian kernel is hollowed (Methods silent; buzcode bz_cch_conv hollows 0.6 of the centre by default),\n# the CCG half width (a standard 50 ms is used; it does not change the bins tested), and whether\n# connections are detected over the whole session or within each state (whole session is read here, as\n# the Results compare the same connections across states).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000166\"\npaper: doi:10.1016/j.neuron.2018.12.009\nclaims:\n- id: fig1f-sink-b-deeper\n  statement: The layer 3/4 border sink of the DOWN-UP transition of non-REM slow oscillations (landmark b)\n    lies slightly but significantly deeper than the early light-evoked sink (b') in the same mice, by 39 ±\n    49 um.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 2; Figure 1F\n  quote: Sink b, associated with the “UP” state of slow oscillation during non-REM sleep, was slightly but\n    significantly deeper than the light-evoked sink b′ in the layer 3/4 border (39 ± 49 μm\n  statistics:\n  - test: signed rank test\n    p: 0.05\n    p_relation: \"<\"\n    n: 13 mice\n  expected:\n  - quantity: depth of sink b below sink b' (mean over mice)\n    value: 39\n    tolerance: 49\n    unit: um\n  criterion: Per mouse with light stimulation, the average CSD of DOWN-UP transitions (onsets from the UP\n    and DOWN detection of the STAR Methods, as in buzcode DetectSlowWaves) and of light onsets, both as\n    the second spatial difference of the LFP along the 64 sites (Figure 1D, 1E). The paper does not fix the\n    time window or how a sink's depth is read from the map; the readings are the depth of the most\n    negative CSD near the layer 3/4 border within (a) 0 to 100 ms after onset (the 100 ms pulse of the\n    Results) and (b) 0 to 50 ms after onset (the early sink). Reproduced when, under a reading, b is deeper\n    than b' with a two-sided Wilcoxon signed-rank p < 0.05 and the mean difference is within tolerance\n    (the paper's SD). CSD spatial smoothing is not given; none is applied (standard choice; it shifts a\n    sink by less than a site).\n  data: dataset\n- id: fig1f-other-landmarks-same-depth\n  statement: The other CSD sinks and sources of slow oscillations (a, d, e) occur at the same depths as the\n    corresponding light-evoked sinks and sources (a', d', e').\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 2; Figure 1F\n  quote: whereas the other sinks and sources occurred at the same depth as those seen with visual\n    stimulation (p > 0.05, signed rank test)\n  statistics:\n  - test: signed rank test\n    p: 0.05\n    p_relation: \">\"\n    n: 13 mice\n  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon signed-rank test per\n    landmark pair (a against a', d against d', e against e') at 0.05, with landmarks read as in\n    fig1f-sink-b-deeper (sources as the most positive CSD near the stated depth). Reproduced when none of\n    the three pairs differs at p < 0.05; not reproduced when any does. The mean differences are reported\n    either way.\n  depends_on:\n  - fig1f-sink-b-deeper\n  data: dataset\n- id: fig1g-landmark-distances-consistent\n  statement: The distances between the five depth landmarks (the MUA power peak c and the CSD landmarks a,\n    b, d, e) vary by less than 100 um from mouse to mouse.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 2; Figure 1G\n  quote: Importantly, the distances between the five landmarks were consistent across animals and varied\n    <100 μm from mouse to mouse ( Figure 1 G; n = 19)\n  expected:\n  - quantity: largest across-mouse range of any inter-landmark distance\n    value: 100\n    tolerance: 10\n    unit: um\n  criterion: Landmark c is the depth of the peak of 500 Hz to 5 kHz power (Figure 1C, STAR Methods, Depth\n    normalization); a, b, d, e are the DOWN-UP CSD landmarks as in fig1f-sink-b-deeper. \"Varied\" can be\n    read as (a) the range (max minus min) across mice of each distance between adjacent landmarks, or (b)\n    each mouse's deviation from the across-mouse mean distance. Reproduced when, under a reading, every\n    adjacent-landmark distance varies by less than 110 um across the 19 mice.\n  depends_on:\n  - fig1f-sink-b-deeper\n  data: dataset\n- id: fig2b-six-coherence-clusters\n  statement: Clustering the 64 sites by their pairwise gamma (30-100 Hz) coherence with a gradient-descent\n    algorithm gives six clusters whose five boundaries are consistent across mice in normalized depth.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 3; Figures 2A, 2B\n  quote: the recording sites were clustered on the basis of their resulting cross-coherence matrix,\n    resulting in six clusters whose five boundaries were consistent across animals when projected into\n    normalized depth coordinates\n  statistics:\n  - test: signed rank test for cluster boundaries across animals\n    p: 0.05\n    p_relation: \">\"\n    n: 19 mice\n  criterion: Coherence 30-100 Hz between all site pairs during waking (Figure 2A), clustered by the\n    energy-gap rule of the STAR Methods (Gamma coherence and gradient descent clustering), from random\n    starts, repeated (the paper says several times; 20 repeats is a standard choice) keeping the lowest\n    energy. The paper does not say how the number of clusters reaches six (the algorithm merges to a local\n    minimum). Readings are (a) the number of clusters at convergence, and (b) six clusters imposed. The\n    boundary consistency test is unclear in what it compares; readings are (a) each boundary's normalized\n    depth against the matching gamma IC boundary in the same mouse, and (b) each mouse's boundary depths\n    against the across-mouse median. Reproduced when, under some reading, six clusters result in most mice\n    (at least 10 of 19 under reading (a)) and no boundary differs at p < 0.05 by the signed-rank test.\n  depends_on:\n  - fig1g-landmark-distances-consistent\n  data: dataset\n- id: fig2b-clusters-same-across-states\n  statement: The depth distribution of the six gamma coherence clusters corresponds roughly to the six\n    cortical layers in each brain state and does not differ between states.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 3; Figure 2B; Figure\n    S2E\n  quote: The depth distribution of the six gamma coherence clusters corresponded roughly to the six cortical\n    layers in each brain state ( Figures 2 B and S2 ; p > 0.05, ANOVA for comparison across different\n    states)\n  statistics:\n  - test: ANOVA for comparison across different states\n    p: 0.05\n    p_relation: \">\"\n    n: 19 mice\n  criterion: A claim of absence, judged on the paper's test, a one-way ANOVA across waking, non-REM and REM\n    of each of the five boundary depths (19 mice per state), at 0.05. Reproduced when no boundary differs\n    across states; not reproduced when any does. The boundary means per state are reported.\n  depends_on:\n  - fig2b-six-coherence-clusters\n  data: dataset\n- id: fig2c-six-gamma-ics\n  statement: ICA of the 30-100 Hz LFP yields six main independent components whose spatial loadings are\n    highly consistent across mice and whose depth distribution is related to the anatomical layers.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 3; Figure 2C\n  quote: ICA yielded six main independent components (ICs) that were highly consistent across animals (p <\n    0.001, Spearman’s correlation for ICs spatial loadings)\n  statistics:\n  - test: Spearman's correlation for ICs spatial loadings\n    p: 0.001\n    p_relation: \"<\"\n    n: 19 mice\n  criterion: Per mouse, the LFP band-passed 30-100 Hz, reduced by PCA to its first ten PCs, then runica\n    (EEGLAB, Bell and Sejnowski; STAR Methods, Independent Component Analysis of LFPs); ICs ranked by\n    variance explained, loadings as the inverse mixing matrix projected on depth. The paper does not say\n    which six of the ten are the main ones or how ICs are matched across mice. Readings are (a) the six\n    with the highest variance, matched by the depth of peak loading, and (b) the six whose loadings are\n    confined in depth (not spread over all sites), matched likewise. The correlation test is (a) each\n    mouse's loading against the across-mouse mean, or (b) all pairs of mice, in normalized depth.\n    Reproduced when, under a reading, the median Spearman correlation is positive with p < 0.001 for each\n    of the six ICs.\n  depends_on:\n  - fig1g-landmark-distances-consistent\n  data: dataset\n- id: ica-volume-conduction-fraction\n  statement: ICA removes volume-conducted currents, which account for 0.34 ± 0.11 of the V1 gamma LFP\n    variance.\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 3\n  quote: This method has the additional advantage of removing volume-conducted currents ( Fernández-Ruiz et\n    al., 2012 ) that accounted for 0.34 ± 0.11 of V1 gamma LFP variance\n  expected:\n  - quantity: fraction of gamma LFP variance from volume-conducted components\n    value: 0.34\n    tolerance: 0.11\n  criterion: The paper does not say which components are volume conducted or how the fraction is formed.\n    Readings are (a) the variance fraction of the components among the ten whose loadings are spread\n    uniformly over depth (Fernandez-Ruiz et al. 2012), and (b) one minus the variance fraction of the six\n    main ICs. Reproduced when, under a reading, the mean over mice is within tolerance (the paper's SD).\n  depends_on:\n  - fig2c-six-gamma-ics\n  data: dataset\n- id: fig2d-superficial-ic-power\n  statement: The three superficial gamma ICs have larger relative power than the three deep ones (0.14 ±\n    0.04 against 0.08 ± 0.03).\n  source: Results, Anchoring Mesoscopic Patterns to Physiological Landmarks, paragraph 3; Figure 2D\n  quote: The superficial gamma ICs had a significantly larger power compared with the deeper ones (top three\n    versus bottom three; Figures 2 D and S4 ; 0.14 ± 0.04 versus 0.08 ± 0.03 relative power for ICs 1–3\n    versus 4–6\n  statistics:\n  - test: rank sum test\n    p: 1.1e-7\n  expected:\n  - quantity: relative power of ICs 1-3\n    value: 0.14\n    tolerance: 0.04\n  - quantity: relative power of ICs 4-6\n    value: 0.08\n    tolerance: 0.03\n  criterion: Relative power is each IC's share of the variance of the gamma LFP (STAR Methods, \"relative\n    power\"), ICs numbered by depth from the surface. Readings for the denominator are (a) the total\n    variance of the band-passed LFP, and (b) the variance of the six main ICs. Values per mouse and IC\n    pooled (57 against 57). Reproduced when, under a reading, both means are within tolerance (the paper's\n    SD) and a two-sided Wilcoxon rank-sum gives p < 0.05 with ICs 1-3 larger.\n  depends_on:\n  - fig2c-six-gamma-ics\n  data: dataset\n- id: fig3c-slow-oscillation-nrem-deep\n  statement: Slow oscillation power (0.5-3 Hz) is dominant in non-REM sleep and largest in the deeper\n    layers.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 1; Figures 3C, S3D\n  quote: Slow oscillation power (0.5–3 Hz) was dominant in non-REM sleep ... especially in deeper layers\n  statistics:\n  - about: across brain states\n    test: Kruskal-Wallis test\n    p: 4.0e-4\n    n: 19 mice\n  - about: across layers\n    test: Kruskal-Wallis test\n    p: 4.1e-5\n  criterion: Per mouse, state and site, LFP power in 0.5-3 Hz (Morlet wavelet, STAR Methods, Spectral\n    analysis). State comparison on each mouse's mean over sites; layer comparison in non-REM on the mean\n    over the sites of each of the six LFP layers (readings, (a) gamma coherence clusters, (b) depth\n    bands of the six ICs). Reproduced when, under a reading, the Kruskal-Wallis test across states gives\n    p < 0.05 with non-REM highest, and across layers p < 0.05 with the largest power in the deepest two\n    layers.\n  depends_on:\n  - fig2b-six-coherence-clusters\n  data: dataset\n- id: fig3d-slow-oscillation-gamma-coupling\n  statement: In non-REM sleep the slow oscillation phase modulates gamma amplitude in superficial layers (69\n    ± 12 Hz, modulation index 2.7 ± 0.5 × 10^-3) and high gamma (>100 Hz) in deep layers (modulation index\n    2.3 ± 0.3 × 10^-3).\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 1; Figure 3D, left\n  quote: Slow oscillation was phase-coupled to gamma frequency power in superficial layers (69 ± 12 Hz;\n    modulation index 2.7 ± 0.5 × 10 −3 ) and to the high-gamma (>100 Hz) band in deep layers\n  expected:\n  - quantity: frequency of peak coupling, superficial layers\n    value: 69\n    tolerance: 12\n    unit: Hz\n  - quantity: modulation index, superficial gamma\n    value: 0.0027\n    tolerance: 0.0005\n  - quantity: modulation index, deep high gamma\n    value: 0.0023\n    tolerance: 0.0003\n  criterion: Phase of the 1-3 Hz band in layer 6 during non-REM (Figure 3D legend; the Results give 0.5-3\n    Hz, a second reading), amplitude by Morlet wavelet on every site, Tort et al. (2008) modulation index\n    with 18 phase bins of 20 degrees (the cited method's setting). Reproduced when, under a reading, the\n    peak frequency and both indices (mean over mice) are within tolerance (the paper's SD).\n  data: dataset\n- id: slow-gamma-superficial-wake\n  statement: Slow gamma (30-60 Hz) dominates in superficial layers, most in waking, then REM, then non-REM\n    sleep.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 1; Figures 3, S3B, S3D\n  quote: Slow gamma oscillations (30–60 Hz) dominated in superficial layers, especially in the waking state\n    followed by REM and non-REM sleep\n  statistics:\n  - test: not named\n    p: 0.028\n  criterion: Mean 30-60 Hz power over superficial-layer sites (gamma clusters 1-3) per mouse and state. The\n    test is not named; the Methods default for three groups is Kruskal-Wallis (reading a), and Figure S3E\n    uses signed-rank tests between states (reading b, waking against REM and REM against non-REM).\n    Reproduced when, under a reading, the order is waking > REM > non-REM in medians and the test gives p\n    < 0.05.\n  depends_on:\n  - fig2b-six-coherence-clusters\n  data: dataset\n- id: fig3c-3-6hz-layer4\n  statement: The most prominent LFP pattern in the waking mouse is a 3-6 Hz oscillation with largest power\n    in layer 4.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 2; Figure 3C, level b\n  quote: The most prominent LFP pattern in the waking mouse was a 3–6 Hz oscillation with largest power in\n    layer 4\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 2.0e-6\n    n: 19 mice\n  criterion: Mean-subtracted 3-6 Hz power in waking (STAR Methods, mean across channels subtracted per\n    session) per mouse and layer (readings as in fig3c-slow-oscillation-nrem-deep). Reproduced when the\n    Kruskal-Wallis test across layers gives p < 0.05 and layer 4 (the layer containing landmark b) has the\n    highest median.\n  depends_on:\n  - fig2b-six-coherence-clusters\n  data: dataset\n- id: fig3d-3-6hz-cross-frequency\n  statement: In waking the 3-6 Hz rhythm is phase-coupled to a 15-25 Hz signal in multiple layers (22 ± 5\n    Hz, modulation index 4.8 ± 1.2 × 10^-4), to high gamma in superficial layers (90 ± 13 Hz, 2.7 ± 0.7 ×\n    10^-4) and to the epsilon band (>100 Hz) in layer 5 (6.4 ± 1.8 × 10^-4).\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 2; Figure 3D, right\n  quote: The 3–6 Hz band was cross-frequency phase-coupled to a 15–25 Hz band signal in multiple layers (22\n    ± 5 Hz, modulation index 4.8 ± 1.2 × 10 −4 )\n  expected:\n  - quantity: frequency of 15-25 Hz coupling\n    value: 22\n    tolerance: 5\n    unit: Hz\n  - quantity: modulation index, 15-25 Hz\n    value: 0.00048\n    tolerance: 0.00012\n  - quantity: frequency of superficial high gamma coupling\n    value: 90\n    tolerance: 13\n    unit: Hz\n  - quantity: modulation index, superficial high gamma\n    value: 0.00027\n    tolerance: 0.00007\n  - quantity: modulation index, layer 5 epsilon band\n    value: 0.00064\n    tolerance: 0.00018\n  criterion: Phase of the 3-6 Hz band recorded in layer 4 in waking (Figure 3D legend), amplitude on all\n    sites, Tort modulation index as in fig3d-slow-oscillation-gamma-coupling. Whether waking means all\n    waking or waking immobility (theta-low, where the rhythm occurs) is open; both are readings.\n    Reproduced when, under a reading, all five values (means over mice) are within tolerance (the paper's\n    SD).\n  data: dataset\n- id: figs2c-3-6hz-theta-anticorrelation\n  statement: The 3-6 Hz rhythm vanishes with movement; its power is negatively correlated with\n    hippocampal theta power.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 3; Figure S2C\n  quote: The antagonism between movement and the 3–6 Hz oscillation was quantified by the negative\n    correlation between its power and the power of theta oscillation (p < 0.01, signed rank test; Figure S2\n    C)\n  statistics:\n  - test: signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Per mouse in waking, the correlation of 3-6 Hz power (layer 4) with 6-9 Hz theta power\n    (volume conducted, Results) over time (power-power comodulation, Figure S2C, with the 10 s windows\n    stepped by 1 s of the state scoring spectrogram as a reading, and 1 s windows as another).\n    Reproduced when, under a reading, the correlations are below zero by a signed-rank test against zero\n    at p < 0.01.\n  data: dataset\n- id: fig3f-units-lock-3-6hz-trough\n  statement: Both principal cells and interneurons are strongly phase-locked to the trough of the layer 4\n    3-6 Hz rhythm.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 2; Figure 3F\n  quote: Both principal cells and interneurons were strongly phase-locked to the trough of the layer\n    4-recorded 3–6 Hz rhythm\n  criterion: Phases of spikes in waking on the 3-6 Hz layer 4 LFP (wavelet phase), units with Rayleigh p <\n    0.05 (Figure 3F legend). Reproduced when, for E cells and for I cells separately, the circular mean of\n    the units' preferred phases lies within 90 degrees of the trough (180 degrees with peaks at 0) and the\n    preferred phases are non-uniform by a Rayleigh test at p < 0.05.\n  data: dataset\n- id: figs2d-visual-offset-rebound\n  statement: Visual stimulation blocks an ongoing 3-6 Hz rhythm, and the offset of a stimulus often induces\n    a short rebound train of 3-6 Hz oscillation.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 3; Figure S2D (cited as S2I)\n  quote: Visual stimulation also blocked an ongoing 3–6 Hz rhythm. However, the offset of visual stimulus\n    often induced a short rebound train 3–6 Hz oscillation\n  criterion: Wavelet amplitude of the layer 4 LFP around light pulses (Figure S2D, 400 ms pulses). The paper\n    gives no test. Reproduced when the mean 3-6 Hz amplitude in the stimulus is below that of the 400 ms\n    before onset, and that of the 500 ms after offset is above the pre-onset level, each across mice by a\n    signed-rank test at p < 0.05 (the Methods' default paired test); the windows are open and the readings\n    are the pulse duration and half of it.\n  data: dataset\n- id: fig3ab-alpha-analogy\n  statement: The waking 3-6 Hz rhythm has spike and wave waveforms and a depth profile similar to the alpha\n    rhythm in monkey V1.\n  source: Results, Brain State-Dependent Features of LFPs, paragraph 2; Figures 3A, 3B\n  quote: in which the waveforms occasionally split into short “spike” and longer “wave” components with a\n    depth profile distribution similar to the depth distribution of alpha waves (8–12 Hz) in monkey V1\n  criterion: The comparison uses monkey data reproduced from Bollimunta et al. (2008) and the paper gives\n    no measure of similarity. The mouse side can be shown (laminar 3-6 Hz traces, CSD profile, Figure 3E);\n    the claim itself is recorded as methods_underspecified.\n  data: elsewhere\n  where: Bollimunta et al. 2008, J. Neurosci. 28, 9976-9988, doi:10.1523/JNEUROSCI.2699-08.2008 (published\n    figure, no deposit)\n- id: fig4a-unit-counts\n  statement: Clustering one session from each of the 19 mice yields 1,472 units, with 251 narrow-waveform\n    putative interneurons and 1,075 wide-waveform putative principal cells.\n  source: Results, Assignment of Neurons to Physiologically Defined Layers, paragraph 1; Figure 4A\n  quote: Unit clustering was performed as described previously ( Fujisawa et al., 2008 ) using one session\n    from each of the 19 mice, yielding a total of 1,472 units\n  expected:\n  - quantity: units\n    value: 1472\n    tolerance: 147\n  - quantity: putative I cells (waveform)\n    value: 251\n    tolerance: 25\n  - quantity: putative E cells (waveform)\n    value: 1075\n    tolerance: 108\n  criterion: Units as sorted in the dataset; classes by the waveform rules of the STAR Methods (the\n    opening comment), trough-to-peak latency from the mean waveform on the peak channel.\n  data: dataset\n- id: fig4a-ccg-classification\n  statement: Short-latency CCG interactions identify 347 E and 100 I cells, and these agree with the\n    waveform classes (97.4% of CCG-based E cells are waveform E cells; 98.0% of CCG-based I cells are\n    waveform I cells).\n  source: Results, Assignment of Neurons to Physiologically Defined Layers, paragraph 1; Figure 4A\n  quote: Using these criteria, 347 and 100 units were classified as CCG-based E and I cells, respectively\n  expected:\n  - quantity: CCG-based E cells\n    value: 347\n    tolerance: 35\n  - quantity: CCG-based I cells\n    value: 100\n    tolerance: 10\n  - quantity: CCG-based E cells that are waveform E cells\n    value: 97.4\n    tolerance: 2.6\n    unit: percent\n  - quantity: CCG-based I cells that are waveform I cells\n    value: 98.0\n    tolerance: 2.0\n    unit: percent\n  criterion: A unit is a CCG-based E (I) cell when it is the presynaptic unit of at least one significant\n    peak (trough) by the monosynaptic rule of the STAR Methods (opening comment). The two agreement\n    percentages carry a tolerance capped at 100% (10% of the value would exceed it), that is, at or above\n    the stated value minus its distance to 100.\n  depends_on:\n  - fig4a-unit-counts\n  data: dataset\n- id: fig4de-optotagging\n  statement: Fourteen of 15 optogenetically identified PV cells and 40 of 52 VGAT cells fall in the\n    narrow-waveform inhibitory group.\n  source: Results, Assignment of Neurons to Physiologically Defined Layers, paragraph 2; Figures 4D, 4E\n  quote: Fourteen of 15 optogenetically identified PV cells (n = 11) and 40 of 52 VGAT cells were part of\n    the inhibitory group defined by the spike waveform criterion\n  expected:\n  - quantity: PV cells tagged\n    value: 15\n    tolerance: 1.5\n  - quantity: PV cells in waveform I group\n    value: 14\n    tolerance: 1.4\n  - quantity: VGAT cells tagged\n    value: 52\n    tolerance: 5.2\n  - quantity: VGAT cells in waveform I group\n    value: 40\n    tolerance: 4\n  criterion: Tagging by the STAR Methods rule (1 ms PSTH bins, mean of the two largest bins in 1-6 ms after\n    the 10 ms pulse above the baseline mean plus 8 SD of -100 to 0 ms), in the 5 PV-Cre::Ai32 and 9\n    VGAT-Cre::Ai32 mice. The \"(n = 11)\" after 15 is unexplained; it is reported, not tested.\n  depends_on:\n  - fig4a-unit-counts\n  data: dataset\n- id: fig5b-eight-clusters\n  statement: K-means clustering of the spike-gamma IC phase-coupling profiles of all units gives eight\n    clusters that largely correspond to the anatomical cell body layers.\n  source: Results, Assignment of Neurons to Physiologically Defined Layers, paragraph 3; Figures 5B, 5C\n  quote: We therefore used the spike-gamma phase coupling profile of all units against the six ICs to\n    perform K-means clustering ( STAR Methods ). This procedure yielded eight clusters\n  expected:\n  - quantity: units clustered\n    value: 1326\n    tolerance: 133\n  - quantity: optimal number of clusters (silhouette)\n    value: 8\n    tolerance: 0\n  criterion: Per unit, mean resultant length of spike phases on each of the six gamma ICs at 20\n    log-spaced wavelet scales from 30 to 100 Hz in waking (STAR Methods, Spectral analysis and Classification\n    of units using spike-LFP phase coupling; Figure 5A is waking). K-means with the cityblock distance and\n    the number of clusters by the silhouette criterion over 2 to 15 clusters (the range is not given; a\n    standard choice). The paper does not say whether K-means runs on the coupling matrix or on its t-SNE\n    embedding (Mahalanobis distance); both are readings. Clusters are numbered by median normalized depth.\n    Reproduced when, under a reading, eight clusters are optimal and their median depths increase in the\n    order of Figure 5C with clusters 1-2 above landmark b, cluster 3 spanning b, clusters 4-6 around c,\n    and 7-8 below d. If the silhouette favours another number, the eight-cluster solution is still used\n    for the layer claims, and this claim is not reproduced. As K-means is random, ten repetitions with the\n    lowest within-cluster sum are kept (standard choice).\n  depends_on:\n  - fig2c-six-gamma-ics\n  - fig4a-unit-counts\n  data: dataset\n- id: fig5a-spike-ic-depth-stratification\n  statement: Unit coupling to the gamma ICs is stratified in depth; above landmark b units couple to slow\n    gamma, in deep layers coupling shifts toward fast gamma.\n  source: Results, Assignment of Neurons to Physiologically Defined Layers, paragraph 3; Figure 5A; Figure\n    S5\n  quote: Around and above depth level b (i.e., layer 3/4 border; first three components), unit-IC coupling\n    of both putative E and I neurons had a peak in the slow gamma range. In deep layers, unit-IC coupling\n    shifted toward the fast gamma band\n  criterion: Preferred frequency (largest mean vector length over the 20 scales) of each significantly\n    modulated unit (Rayleigh p < 0.05). Reproduced when units above landmark b have a median preferred\n    frequency in 30-60 Hz and units below landmark c a median above that of the superficial units, by\n    rank-sum p < 0.05. The paper gives no test; the rank-sum is the Methods default for two groups.\n    The reference IC for each unit is open; the readings are the IC of largest coupling and the IC of the\n    unit's own depth.\n  depends_on:\n  - fig2c-six-gamma-ics\n  data: dataset\n- id: fig6a-firing-rate-layers\n  statement: Principal cell firing rates differ across layers; the fastest groups are in layers 5A and 5B\n    and the slowest in the superficial layers.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 1; Figure 6A\n  quote: The fastest firing group corresponded to those in layers 5A and B ( Figure 6 , red and magenta\n    groups), while the slowest ones were the superficial layers\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 3.7e-83\n  criterion: E cells by group (clusters 1-8). Firing rate in non-REM (Figure 6A legend) or over the whole\n    session (the Results' \"long-term mean firing rates\"); both are readings. Reproduced when, under a\n    reading, the Kruskal-Wallis test gives p < 0.05, clusters 5 and 6 have the two highest medians, and\n    clusters 1 and 2 the two lowest.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6b-deep-wake-higher\n  statement: Deep-layer principal neurons fire more during waking than during non-REM sleep.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 1; Figure 6B\n  quote: Deep-layer neurons were significantly more active during waking compared with non-REM sleep\n  criterion: Per E cell, rate in waking and in non-REM. The test is not named in the legend; readings are\n    a signed-rank test on each cell's two rates (Methods default for paired data) and a rank-sum test (as\n    in the Figure S6 legend for other state pairs). Deep groups are read as clusters 4-8 (layers 5 and\n    6) or clusters 5-8. Reproduced when, under a reading, each deep group has waking > non-REM at p <\n    0.05; partially reproduced when most of them do.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6b-superficial-no-state-change\n  statement: No such state dependence of firing rates is present in superficial neurons.\n  source: Discussion, State Dependence of Firing Patterns and Interlaminar Interactions, paragraph 1;\n    Figure 6B\n  quote: Deep-layer neurons increased their excitability during waking ( Sakata and Harris, 2012 ), as\n    quantified by their firing rates, whereas no such state dependence was present in superficial neurons\n  criterion: A claim of absence, judged on the Figure 6B test at 0.05 for clusters 1 and 2 (layer 2/3),\n    under each test reading of fig6b-deep-wake-higher (the paper does not name it; both are shown).\n    Reproduced when neither group differs between waking and non-REM; not reproduced when either does.\n    The median ratios are reported.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6c-burst-index\n  statement: Superficial-layer principal neurons are the most bursty, followed by layer 6 and layer 4,\n    while layer 5 neurons have the lowest burst indices.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6C\n  quote: In general, superficial layer neurons exhibited more bursting behavior, followed by layer 6 and\n    layer 4 neurons, while layer 5 neurons had the lowest burst indices\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 5.2e-37\n  criterion: The burst index is defined twice. Results, spikes in the 3-10 ms bins of the autocorrelogram\n    divided by spikes in the 200-300 ms bin (reading a); STAR Methods, mean count in the 1.5-13.5 ms bins\n    divided by mean count in the 200-300 ms bins (reading b). Bin width is not given (1 ms, a standard\n    choice for reading b; reading a sums counts). Whole session. Reproduced when, under a reading, the\n    Kruskal-Wallis test across the eight E groups gives p < 0.05 and the layer medians (pooling groups by\n    layer) order as layer 2/3 > layer 6 > layer 4 > layer 5.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6d-transient-steady\n  statement: Deep layer 5 neurons show the strongest transient responses after the UP state onset (largest\n    transient/steady firing ratio).\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6D\n  quote: By this measure, deep layer 5 neurons showed the strongest transient responses\n  statistics:\n  - about: layer difference\n    test: not named (Kruskal-Wallis by the Methods default)\n    p: 5.6e-10\n  criterion: Index as the Results define it, peak rate in 0-200 ms divided by mean rate in 100-200 ms after\n    UP onsets (DOWN-UP transitions). The PETH bin is not given; readings 5, 10 and 20 ms. Reproduced when,\n    under a reading, Kruskal-Wallis across the eight E groups gives p < 0.05 and cluster 6 (L5b) has the\n    highest median.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6e-down-up-latency\n  statement: During the DOWN-UP transition layer 5B neurons fire first, followed by superficial and layer 6\n    neurons.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6E\n  quote: During the DOWN-UP state transition, layer 5B neurons fired first, followed by superficial and\n    layer 6 neurons\n  statistics:\n  - test: not named (Kruskal-Wallis by the Methods default)\n    p: 1.3e-38\n  criterion: Latency of spikes after DOWN-UP transitions; readings are (a) each cell's median latency of\n    its first spike after each transition, and (b) the time of peak of its PETH in 0-300 ms. Reproduced\n    when, under a reading, Kruskal-Wallis across the eight E groups gives p < 0.05 and cluster 6 has the\n    shortest median latency.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6f-3-6hz-phase-layers\n  statement: Spike phase preference during the waking 3-6 Hz rhythm differs systematically across layers.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6F\n  quote: The distribution of spike firing latency during the 3–6 Hz rhythm of waking displayed\n    characteristic laminar differences\n  statistics:\n  - test: not named\n    p: 2.6e-10\n  criterion: Preferred phase of each E cell on the layer 4 3-6 Hz LFP in waking. The test is not named;\n    readings are Kruskal-Wallis on phases (Methods default) and a circular multi-sample test\n    (Watson-Williams). Reproduced when, under a reading, the groups differ at p < 0.05.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6g-3-6hz-modulation-strength\n  statement: Phase locking to the 3-6 Hz rhythm is strongest in superficial layers and weakest in layer 6.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6G\n  quote: The mean vector length of phase locking to the 3–6 Hz rhythm was strongest in the superficial\n    layers and weakest in layer 6\n  statistics:\n  - test: not named (Kruskal-Wallis by the Methods default)\n    p: 7.6e-50\n  criterion: Mean resultant length of each E cell's spike phases on the layer 4 3-6 Hz LFP in waking.\n    Reproduced when Kruskal-Wallis across the eight groups gives p < 0.05, one of clusters 1-2 has the\n    highest median and one of clusters 7-8 the lowest.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig6h-gamma-coupling-wake\n  statement: Spike-gamma (30-100 Hz) coupling is stronger in waking than in non-REM in all layers except\n    layer 5A.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figure 6H\n  quote: Spike-gamma (30–100 Hz) coupling was stronger in the waking animal compared with non-REM in all\n    layers but layer 5A\n  statistics:\n  - test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Mean resultant length of E cell spikes to gamma per state, two-sided rank-sum per group (legend).\n    The reference is open; readings are the IC of the unit's own depth at its preferred frequency, and\n    the largest coupling over the six ICs. Reproduced when, under a reading, waking > non-REM at p < 0.05\n    in each group but cluster 5, and cluster 5 does not differ.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: figs7-strongest-3-6hz-coupling\n  statement: The strongest spike-LFP coupling is in the 3-6 Hz band, followed by the slow gamma (30-60 Hz)\n    band.\n  source: Results, Layer-Specific and Brain State-Dependent Features of Unit Firing, paragraph 2; Figures\n    S7A to S7D\n  quote: The strongest spike-LFP coupling was observed in the 3–6 Hz band ( Figures 3 F and S7 ), followed by\n    the slow gamma (30–60 Hz) band\n  criterion: Per unit in waking, the frequency of largest mean resultant length (preferred frequency, STAR\n    Methods) over log-spaced frequencies; the range is not given below 30 Hz (Figure S7 spans slow\n    oscillation to gamma; 0.5 to 100 Hz is read). Reproduced when the histogram of preferred frequencies\n    of significantly modulated units has its largest mass in 3-6 Hz and its next in 30-60 Hz, among bands\n    0.5-3, 3-6, 6-15, 15-30, 30-60 and 60-100 Hz (standard bands).\n  data: dataset\n- id: fig7-connection-counts\n  statement: Of 102,332 potential neuron pairs, 525 putative excitatory and 323 putative inhibitory\n    monosynaptic connections were identified.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 1\n  quote: Of the 102,332 potential neuron pairs in all mice and sessions, we identified putative excitatory\n    (E, n = 525) and inhibitory (I, n = 323) monosynaptic connections\n  expected:\n  - quantity: potential neuron pairs\n    value: 102332\n    tolerance: 10233\n  - quantity: excitatory connections\n    value: 525\n    tolerance: 53\n  - quantity: inhibitory connections\n    value: 323\n    tolerance: 32\n  criterion: Detection by the STAR Methods rule (opening comment). The pair count can be read as ordered\n    pairs within a session among (a) all units, or (b) E and I units only; and unordered pairs of each.\n    Gaussian baseline unhollowed (Methods) and hollowed 0.6 (buzcode) are both run. Reproduced when, under\n    a reading, all three counts are within tolerance.\n  depends_on:\n  - fig4a-unit-counts\n  data: dataset\n- id: fig7-within-layer-fractions\n  statement: Many connections are within the same layer (E-I 173 of 385, E-E 19 of 90, I-E 98 of 323), but\n    there are also many cross-layer excitatory and inhibitory pairs.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 1; Figures 7A, 7B,\n    S8A\n  quote: Although many identified excitatory connections were detected within the same layer (layers in\n    these calculations refer to IC-based clusters) for both E-I ( Figures 7 A and 7B; n = 173 of 385\n    connections) and E-E (n = 19 of 90) pairs\n  expected:\n  - quantity: E-I connections within layer\n    value: 173\n    tolerance: 17\n  - quantity: E-I connections\n    value: 385\n    tolerance: 39\n  - quantity: E-E connections within layer\n    value: 19\n    tolerance: 2\n  - quantity: E-E connections\n    value: 90\n    tolerance: 9\n  - quantity: I-E connections within layer\n    value: 98\n    tolerance: 10\n  - quantity: I-E connections\n    value: 323\n    tolerance: 32\n  criterion: Pre and post cells typed E or I by waveform; same layer read at the level of (a) the eight\n    clusters, or (b) the four layers (2/3, 4, 5, 6) of the opening comment. The E-I total is given as 385\n    here and 392 two sentences later, and E-I plus E-E (475) falls short of 525; units not typed are the\n    likely gap. Reproduced when, under a layer reading, each within-layer fraction is within 10% of the\n    paper's (0.449, 0.211, 0.303).\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7eg-l23-targets\n  statement: Of the 172 putative excitatory connections of layer 2/3 pyramidal cells, 10 (5.8%) and 39\n    (22.7%) target layer 2/3 and layer 4/5/6 excitatory neurons, and 29 (16.9%) and 94 (54.7%) target layer\n    2/3 and layer 4/5 interneurons.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 1; Figures 7E, 7G\n  quote: Of the 172 putative excitatory connections of L2/3 pyramidal cells, 10 (5.8%) and 39 (22.7%)\n    targeted L2/3 and L4/5/6 excitatory neurons, respectively, in addition to contacting 29 (16.9%) and 94\n    (54.7%) L2/3 and L4/5 interneurons, respectively\n  expected:\n  - quantity: excitatory connections from layer 2/3 E cells\n    value: 172\n    tolerance: 17\n  - quantity: share to layer 2/3 E\n    value: 5.8\n    tolerance: 0.58\n    unit: percent\n  - quantity: share to layer 4/5/6 E\n    value: 22.7\n    tolerance: 2.27\n    unit: percent\n  - quantity: share to layer 2/3 I\n    value: 16.9\n    tolerance: 1.69\n    unit: percent\n  - quantity: share to layer 4/5 I\n    value: 54.7\n    tolerance: 5.47\n    unit: percent\n  criterion: Layer 2/3 is clusters 1-2; layers 4/5/6 clusters 3-8. \"L4/5 interneurons\" is read as (a)\n    clusters 3-6 or (b) clusters 3-8 (the four shares sum to 100%, so layer 6 targets fall in this group).\n    Reproduced when, under a reading, the total and all four shares are within tolerance.\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7c-divergence-convergence\n  statement: Most presynaptic principal neurons have a single target in the recorded population, a few\n    target several; an interneuron typically has one presynaptic partner, a few many, up to 16.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 2; Figures 7B, 7C\n  quote: A typical interneuron typically had one presynaptic partner, but a small fraction many, up to 16\n  expected:\n  - quantity: largest number of presynaptic E partners of one interneuron\n    value: 16\n    tolerance: 1.6\n  criterion: From the E-I connections, the count of targets per presynaptic E cell and of presynaptic E\n    cells per I cell. Reproduced when the mode of both distributions is one and the largest convergence is\n    within tolerance.\n  depends_on:\n  - fig7-connection-counts\n  data: dataset\n- id: figs8b-reciprocal-connections\n  statement: Almost half of E-I connections (168 of 392, 42.9%) have a reciprocal I-E connection, and\n    reciprocal E-I-E connections are almost twice as frequent in layer 5 (60-70%) as in other layers.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 2; Figure S8B (the\n    text cites S7C)\n  quote: Almost half of the E-I connections (168 of 392 [42.9%]) received reciprocal I-E connections when all\n    layers were considered. Reciprocal E-I-E connections were almost twice more frequent in layer 5\n    (60%–70%) than in other layers\n  expected:\n  - quantity: E-I connections with a reciprocal I-E connection\n    value: 42.9\n    tolerance: 4.29\n    unit: percent\n  - quantity: reciprocal fraction in layer 5 clusters (range)\n    value: 65\n    tolerance: 11.5\n    unit: percent\n  criterion: For each E-I connection, whether the same I cell has a significant I-E connection back to the\n    same E cell. Per cluster of the E cell (Figure S8B), the reciprocal fraction. The layer 5 range is 60\n    to 70%, widened by 10% of each bound to 54 to 77% (value and tolerance above). Reproduced when the\n    overall fraction is within tolerance, each of clusters 4-6 lies in 54 to 77%, and their mean is at\n    least 1.5 times the mean of the other clusters (\"almost twice\").\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7d-l23e-l5i-weaker-nrem\n  statement: Spike transmission from layer 2/3 E cells to layer 5 I cells is weaker during non-REM sleep\n    than during waking.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 3; Figure 7D\n  quote: We observed that spike transmission strength between layer 2/3 E cells and deep layer I and E cells\n    became weaker during non-REM sleep compared with waking (L2/3 E cells to L5 I cells, p = 0.0012\n  statistics:\n  - test: signed rank test\n    p: 0.0012\n  criterion: For the E-I connections from clusters 1-2 to I cells in clusters 4-6, transmission in waking\n    and in non-REM from spikes in each state. The measure is named twice; readings are (a) the\n    peak-to-baseline ratio of the CCG (Results; peak in +1.5 to +4 ms over the convolution predictor), and\n    (b) the corrected spike transmission probability of English et al. 2017 (STAP Methods; excess counts\n    over the predictor in +1.5 to +4 ms divided by presynaptic spikes, as in buzcode). Reproduced when,\n    under a reading, waking > non-REM by a two-sided signed-rank test at p < 0.05.\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7e-l23e-l4i-weaker-nrem\n  statement: Spike transmission from layer 2/3 E cells to layer 4 I cells is weaker during non-REM sleep\n    than during waking.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 3; Figure 7E\n  quote: L2/3 E cells to L4 I cells, p = 0.0010\n  statistics:\n  - test: signed rank test\n    p: 0.0010\n  criterion: As fig7d-l23e-l5i-weaker-nrem, for I cells in cluster 3.\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7h-l23e-l5e-weaker-nrem\n  statement: Spike transmission from layer 2/3 E cells to layer 5 E cells is weaker during non-REM sleep\n    than during waking.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 3; Figure 7H\n  quote: L2/3 E cells to L5 E cells, p = 0.015; signed rank test\n  statistics:\n  - test: signed rank test\n    p: 0.015\n  criterion: As fig7d-l23e-l5i-weaker-nrem, for E-E connections to E cells in clusters 4-6.\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig7g-deep-ee-stronger-nrem\n  statement: E-E spike transmission among deep-layer principal cells (layer 5/6 to layer 5/6) is stronger\n    during non-REM sleep than during waking.\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 3; Figures 7G, 7I\n  quote: In contrast, putative E-E spike transmission in the deep layers (layer 5/6 to layer 5/6 principal\n    cells) significantly increased during non-REM sleep compared with waking (p = 0.0061, signed rank test\n  statistics:\n  - test: signed rank test\n    p: 0.0061\n  criterion: As fig7d-l23e-l5i-weaker-nrem, for E-E connections with both cells in clusters 4-8, with\n    non-REM > waking.\n  depends_on:\n  - fig7-connection-counts\n  - fig5b-eight-clusters\n  data: dataset\n- id: figs8f-ie-dip-wake\n  statement: Over all I-E pairs, spike suppression is stronger in waking than in non-REM sleep (dip 24.1%\n    against 22.8% of the CCG baseline).\n  source: Results, Within-Layer and Inter-layer Interactions among Neurons, paragraph 3; Figure S8F\n  quote: When all I-E pairs were considered, spike suppression probability during waking was significantly\n    stronger compared with non-REM (I-E dip wake, 24.1%; non-REM sleep, 22.8% relative to the CCG baseline\n  statistics:\n  - test: signed rank test\n    p: 0.006\n  expected:\n  - quantity: I-E dip, waking\n    value: 24.1\n    tolerance: 2.41\n    unit: percent of CCG baseline\n  - quantity: I-E dip, non-REM\n    value: 22.8\n    tolerance: 2.28\n    unit: percent of CCG baseline\n  criterion: For each I-E connection and state, the dip as (predictor minus CCG) over predictor at the\n    deepest bin in +1.5 to +4 ms. Whether the reported values are means or medians over pairs is not\n    said; both are readings. Reproduced when, under a reading, both values are within tolerance and\n    waking > non-REM by a two-sided signed-rank test at p < 0.05.\n  depends_on:\n  - fig7-connection-counts\n  data: dataset\n- id: figs8c-lognormal-strength\n  statement: Connection strengths are skewed and lognormally distributed, a few strong connections mixed\n    with many weak ones.\n  source: Discussion, State Dependence of Firing Patterns and Interlaminar Interactions, paragraph 2; Figure\n    S8C\n  quote: The magnitude of both spike transmission probability and single neuron-induced excitatory\n    postsynaptic potentials (EPSPs) (in E-I and E-E connections) and IPSPs (I-E connections) showed a\n    lognormal distribution\n  criterion: The paper reports no test or measure of lognormality. The distribution of log transmission\n    probabilities is shown with its skewness, as description; the claim is recorded as\n    methods_underspecified.\n  depends_on:\n  - fig7-connection-counts\n  data: dataset\n- id: fig8-down-active-neurons\n  statement: Five neurons in four mice are specifically active during the DOWN state of non-REM slow\n    oscillation, all in deep layer 6; four have bursty autocorrelograms and one is regular spiking.\n  source: Results, DOWN State-Active Neurons, paragraph 1; Figures 8A, 8B\n  quote: We found five neurons in four mice that were specifically and dominantly active during the DOWN\n    state of non-REM slow oscillation ( Figures 8 A and 8B). All DOWN state-active neurons were found in\n    deep layers 6\n  expected:\n  - quantity: DOWN state-active neurons\n    value: 5\n    tolerance: 1\n  - quantity: mice with DOWN state-active neurons\n    value: 4\n    tolerance: 1\n  criterion: The paper gives no rule for selecting these cells. Readings are (a) units whose mean rate\n    within DOWN states exceeds their rate within UP states, and (b) units whose PETH around DOWN-UP\n    transitions peaks before time zero and falls after it (Figure 8A). The tolerance is one neuron or one\n    mouse, as 10% of the count is less than the smallest step. Reproduced when, under a reading, the counts\n    are within tolerance and all the cells lie in clusters 7-8 or below landmark d.\n  depends_on:\n  - fig5b-eight-clusters\n  data: dataset\n- id: fig8-down-up-rates\n  statement: The DOWN state-active neurons fire at 35.2 ± 23.1 Hz during DOWN states and 4.3 ± 3.1 Hz\n    during UP states.\n  source: Results, DOWN State-Active Neurons, paragraph 1; Figure 8B\n  quote: These five neurons were not only active during the DOWN state but mainly silent during the UP state\n    (35.2 ± 23.1 Hz during DOWN, 4.3 ± 3.1 Hz during UP; p < 0.016, rank sum test)\n  statistics:\n  - test: rank sum test\n    p: 0.016\n    p_relation: \"<\"\n    n: 5 neurons\n  expected:\n  - quantity: rate during DOWN states\n    value: 35.2\n    tolerance: 23.1\n    unit: Hz\n  - quantity: rate during UP states\n    value: 4.3\n    tolerance: 3.1\n    unit: Hz\n  criterion: For the cells of fig8-down-active-neurons, rate within DOWN and within UP intervals; mean over\n    cells. Reproduced when both are within tolerance (the paper's SD) and a two-sided rank-sum test gives p\n    < 0.05.\n  depends_on:\n  - fig8-down-active-neurons\n  data: dataset\n- id: fig8cd-down-active-suppressed\n  statement: DOWN state-active neurons are suppressed during light flashes, when other neurons respond, and\n    during optogenetic activation of PV or VGAT neurons, after which they rebound about 30 ms later while\n    other principal cells are still suppressed.\n  source: Results, DOWN State-Active Neurons, paragraph 1; Figures 8C, 8D\n  quote: During light flash presentation, their spiking activity was further reduced at the time when the\n    remaining neurons robustly responded\n  criterion: PSTHs around light flash onsets and around 10 ms blue pulses (PV-Cre and VGAT-Cre mice). The\n    paper gives no test. Reproduced when, for each DOWN state-active cell recorded with the stimulus, the\n    rate in the stimulus window (flash, the 100 ms after onset; blue pulse, 0-10 ms) is below its\n    baseline (-100 to 0 ms, the Methods' tagging baseline), and the mean rebound at 30-50 ms after the blue\n    pulse exceeds baseline while the mean of other E cells is below it. Windows are open beyond these; the\n    readings use the 30 ms of the text and the pulse lengths of the Methods.\n  depends_on:\n  - fig8-down-active-neurons\n  data: dataset\n- id: fig8eh-down-active-inverse-correlation\n  statement: DOWN state-active neurons are inversely correlated with other principal cells and interneurons\n    in both non-REM sleep and waking.\n  source: Results, DOWN State-Active Neurons, paragraph 1; Figures 8E to 8H\n  quote: Cross-correlation between the DOWN state-active cells and other principal cells showed an inverse\n    correlation not only during non-REM but also in the waking animal\n  criterion: Spike CCGs of each DOWN state-active cell with every other E and I cell of its session, per\n    state. The paper gives no test or window; reading, the mean normalized CCG within ±50 ms (the scale of\n    Figures 8E to 8H is not in the text, a standard choice) below the CCG at ±500 to 1000 ms. Reproduced\n    when the mean over pairs is below baseline in both states for D-E pairs.\n  depends_on:\n  - fig8-down-active-neurons\n  data: dataset\n"
}
```

```
File created successfully at: claims/000166/10.1016-j.neuron.2018.12.009.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -i 's/STAP Methods/STAR Methods/' claims/000166/*.yaml; python tools/claims_check.py claims/000166/10.1016-j.neuron.2018.12.009.yaml paper/10.1016-j.neuron.2018.12.009.txt; grep -n "—\|rather" claims/000166/*.yaml; python - <<'E'
import yaml
d=yaml.safe_load(open('claims/000166/10.1016-j.neuron.2018.12.009.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p,x[:80])
walk(d); print(len(d['claims']))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000166/10.1016-j.neuron.2018.12.009.yaml; python - "$f" <<'E'
import sys
p=sys.argv[1]; s=open(p).read()
reps=[("six clusters result in most mice\n    (at least 10 of 19 under reading (a)) and","six clusters result in every mouse\n    and"),
("    value: 97.4\n    tolerance: 2.6","    value: 97.4\n    tolerance: 9.74"),
("    value: 98.0\n    tolerance: 2.0","    value: 98.0\n    tolerance: 9.8"),
(""" The two agreement
    percentages carry a tolerance capped at 100% (10% of the value would exceed it), that is, at or above
    the stated value minus its distance to 100.""","")]
for a,b in reps:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py $f paper/10.1016-j.neuron.2018.12.009.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000166/10.1016-j.neuron.2018.12.009.yaml'))['claims']
print(sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('criterion' in c for c in d), sum('expected' in c for c in d), [c['id'] for c in d if c.get('data')!='dataset'])"; git status --short
```

```
23 24 47 18 ['fig3ab-alpha-analogy']
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
?? claims/000166/
?? scripts
```

**Agent**

I wrote `claims/000166/10.1016-j.neuron.2018.12.009.yaml` with 47 claims. All 47 quotes pass the checker. The checker still exits non-zero on two p-values, both confirmed by reading: 4.0e-4 and 2.0e-6 are printed in the text as "4.0 × 10 −4" and "2.0 × 10 −6", and it doesn't match the trailing zero. Nothing is committed.

**Text read:** the version of record (Neuron 101:500–513, 2019, from Europe PMC, PMC6367010), with full Results, figure legends and STAR Methods. Both supplements were there: mmc1 (legends for Figures S1–S8) and mmc2 (a PDF copy of the article). No PDF page could be opened because no renderer is installed, but every number used is in the text.

**Code read:** the paper links no analysis code of its own, only the lab's general toolbox buzcode, read at commit e615663 (the commit the paper used is not given). I used it for brain-state scoring, UP/DOWN state detection and the monosynaptic-connection functions. Its monosynaptic defaults differ from the STAR Methods (0.4 against 0.5 ms bins, the baseline kernel, the threshold, and the 0.8–4 against 1.5–4 ms window). The file follows the Methods and names the code as a variant.

**Counts:**
- 47 claims, all with quotes.
- 23 claims carry statistics (24 entries in all).
- 47 criteria.
- 18 claims have expected values.
- 46 claims use the dataset. One, the comparison with monkey alpha rhythm, uses data from elsewhere: a published figure from Bollimunta et al. 2008, with no deposit.

**Details the paper leaves open, and the readings named:**
- **Layer groups:** the eight clusters of Figure 5C map to layers 2/3, 4, 5 and 6. The Figure S8B legend settles that layer 5 is clusters 4–6. "Deep" can mean clusters 4–8 or 5–8, and "L4/5 interneurons" can mean clusters 3–6 or 3–8.
- **Clustering:** K-means can run on the coupling matrix or on its t-SNE embedding.
- **Transmission strength:** the Results use the CCG peak-to-baseline ratio, the Methods use the English et al. 2017 corrected probability. Also open: whether the Gaussian baseline kernel is hollowed (as buzcode does) or not.
- **Burst index:** the Results use 3–10 ms over the 200–300 ms bin, the Methods 1.5–13.5 ms over 200–300 ms.
- **Pair count (102,332):** ordered or unordered pairs, among all units or only E and I units.
- **Light pulse length:** 100 ms in the Results, 400 ms in the Methods. The CSD time window and how a sink's depth is read are also open.
- **Unnamed tests:** Figures 6B, 6D–6G and the slow-gamma p = 0.028. Readings are the Methods' defaults (Kruskal-Wallis, signed-rank or rank-sum) and, for phases, a circular test.
- **ICA:** which six of the ten components are the main ones, how they are matched across mice, how the volume-conducted fraction (0.34) is formed, and the denominator of relative power.
- **Gamma coherence clusters:** what the signed-rank "boundary consistency" test compares, and whether six clusters arise or are imposed.
- **Peri-event bins and windows** for the transient/steady index, DOWN-UP latency, the visual-offset rebound, and the light and optogenetic responses of DOWN-state neurons.
- **Other:** 3–6 Hz coupling in all waking or only waking immobility; slow-oscillation band 1–3 Hz (Figure 3D legend) or 0.5–3 Hz (Results); I-E dip as a mean or a median.

**Missing from the paper:**
- **DOWN-state active neurons:** there is no rule for selecting them. I named two readings: a higher rate in DOWN than in UP states, or a peri-event peak just before the DOWN-UP transition.
- **Two claims have no test or measure at all:** the lognormal spread of connection strengths and the similarity to monkey alpha. Both are recorded as `methods_underspecified`.
- **Inconsistent counts:** the paper gives 385 and also 392 E-I connections, and E-I plus E-E (475) falls short of the 525 excitatory connections. The opto-tagged PV cells are given as "15 (n = 11)", which is unexplained.
- **Mis-cited panels:** the text cites Figure S7C for reciprocal connections, but the panel is S8B; it cites S2I for the visual-offset rebound, but the panel is S2D.

## End of run

32 turns, 7 minutes, result: success.
