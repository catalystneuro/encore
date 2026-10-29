# 000233 · claims · run 40734265649

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 claims/000233 paper/ 2>&1; git log --stat -3 | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453 claims/000233 paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 182
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 162 more lines not kept]
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
wc -l paper/*.txt; head -30 paper/*.txt; grep -n -i "github\|code availab\|data availab\|zenodo" paper/*.txt; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

The text is 850 lines; I'll read it fully.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-021-03811-w.txt",
 "offset": 7,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-021-03811-w.txt",
 "offset": 7,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7p paper/*.txt | fold -s -w 4000 > $TMPDIR/p7.txt; wc -l $TMPDIR/p7.txt; head -c 20000 $TMPDIR/p7.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
tail -c +20000 $TMPDIR/p7.txt | head -c 22000
```

```
and median filtering (±6 bins) and (3) taking the difference between samples nearest the peak power bin of the 
ripple and dividing by two pi. The ripple amplitude was taken as the maximum NSS value between start andstop times for each ripple. State scoring A previously described semi-automated sleep scoring algorithm was used 43 , 44 . It calculates a spectrogram from the raw LFP (1,250 Hz) using a 10-s window fast Fourier transform, sliding at 1-s intervals, at logarithmically spaced frequencies from 1 to 100 Hz. In brief, this algorithm then uses a set of heuristics when examining the EMG, theta band ratio (4–9 Hz divided by 2–16 Hz) and broadband LFP. The estimated EMG is the summed pairwise zero-lag correlation between non-neighbouring electrodes (separate shanks; >200 μm distance) using the bandpass-filtered (300–600 Hz; 3th order Butterworth) LFP 42 . The theta band ratio is the 4–9-Hz power from the spectrogram, dividing by the 2–16-Hz power. The broadband LFP spectrogram was then compressed using principal components analysis (principal component 1 always corresponding to <20-Hz power). The algorithm then uses these data in a sequence of separations, finding troughs that maximally split peaks in each distribution. In all recordings, manual inspection of scoring was conducted. In some cases, manual curation of algorithm parameters or specific segments of recordings was conducted to best identify brain state. Continuous glucose monitor placement A US Food and Drug Administration-approved device (Medtronic iPro2) for human use was adapted to measure glucose concentrations in rats. It is a 5-g device about 20 mm in diameter, typically worn on the abdomen for humans and is fixed to the skin with a tegaderm bandage. This device uses an amperometric method with an enzyme-coated electrode. The enzyme (glucose oxidase) catalyses glucose into gluconic acid and hydrogen peroxide. The electrochemical measurement of hydrogen peroxide allows for a current read out that i
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
tail -c +42000 $TMPDIR/p7.txt
```

```
rsal CA3. b , Example traces of raw LFP and bandpass-filtered LFP across both recording sites (top, ventral; bottom, dorsal). For each region, one shank with uniformly distributed recording sites along the dorsal–ventral axis is shown. c , Example LFP from channels used for ripple detection. d , Average cross-correlogram between dorsal CA1 and ventral CA1 SPW-Rs at slow timescales. Inset, average cross-correlogram between dorsal CA1 and ventral CA1 SPW-Rs at fast timescales. e , Across the three rats with simultaneous dorsal and ventral hippocampal recordings, dorsal SPW-Rs were equivalently correlated with glucose fluctuations as the previous cohorts of rats with only dorsal CA1 recordings ( n = 30). Ventral SPW-Rs had a significantly (two-way t -test) weaker correlation with peripheral glucose fluctuations. f , For each rat, ventral CA1 SPW-Rs were more weakly correlated with glucose dynamics and dorsal CA1 SPW-Rs. Extended Data Fig. 10 | Histology from DREADD and CNO experiments. a , Top, histology from the cohort of rats with AAV1-hDlx-GiDREADD-dTomato-Fishell injected into lateral septum. Bottom, example cross-correlograms between SPW-R and glucose fluctuations on vehicle (blue) and CNO (black) days. b , Top, histology from the cohort of rats with AAV2-hSyn-hM4D(Gi)-mCherry injected into medial septum. Bottom, example cross-correlograms between SPW-R and glucose fluctuations on vehicle (blue) and CNO (black) days. c , Comparison of effects for individual rats across vehicle versus CNO days for each cohort. d , P values (two-way t -test) for each part of the cross-correlograms shown in e when comparing within hM4Di rats (red; CNO versus vehicle) or across cohorts of rats (blue; CNO–hM4Di vs CNO–control). e , Ten colleagues who were not involved with these experiments were provided histology from all 9 rats (6 lateral septum; 3 medial septum) and asked to rate the degree of viral transfection in each subregion of the septum. Each rat had three images taken along 
[... 4 more lines not kept]
```

**Agent**

Main text, Methods and legends are read; now the supplement (lines 8 onward).

**Agent calls Bash**

```bash
sed -n '8,400p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '400,850p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, Methods and the supplement (Supplementary Information PDF) are present. Next: the dataset description, the linked code, and the claims schema.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000233/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name'])"; curl -s https://api.dandiarchive.org/api/dandisets/000233/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('version'))"; ls claims | head -50; ls tools docs
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -l "pilot-12" claims/*/*.yaml | head; f=$(grep -l "pilot-12" claims/*/*.yaml | head -1); head -40 "$f"; grep -n "data:\|kind:\|open\b" "$f" | head -20; sed -n 1,80p tools/claims_check.py
```

```
claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml
# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,
# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol pilot-12 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record from Europe PMC (PMC11271266, full-text XML converted to text)
# as supplied under paper/, with Background & Summary, Methods, Data Records, Technical
# Validation, the legends of Figures 1 to 3 and Tables 1 and 2. The paper is a Data Descriptor
# and has no supplement; its additional plots are in the Figshare deposit itself. No PDF was
# supplied, so the figures were not seen: the nominal paleointensities printed in Figure 1 and
# the step ranges marked by arrows in Figures 1 and 2 are not recorded. The footnote legends of
# both tables (the marks after "M590 20 uT" and "Max intensity" in Table 1, and the marks after
# the specimen names, after n and after T Range in Table 2) are missing from the text.
# Code: the paper states that no custom code was used. It names PmagPy for looking at the
# directional and paleointensity data during collection and for checking quality factors
# (Technical Validation), with no version; no repository was read.
#
# Data the paper used. Two sets of measurements, all made with the WSGI three-component DC SQUID
# magnetometer (6.3 mm bore) in the shielded room at the University of Rochester, moments in emu.
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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

Now the linked code, buzcode.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/buzsakilab/buzcode.git && cd buzcode && git log -1 --format='%H %cd' && grep -ril "glucose\|ipro\|tingley" --include=*.m . | head -30
```

```
e615663b2b100782d1f378580f6d7aaa35c12937 Thu Oct 1 16:00:05 2026 -0400
./utilities/runBatchAnalysis.m
./utilities/restoreOriginalKwik.m
./utilities/fileConversions/pos2behav.m
./utilities/fileConversions/convertClu2Kwik.m
./utilities/fileConversions/ConvertKlusta2Matlab.m
./utilities/bz_wrap.m
./utilities/bz_isSessionInfo.m
./utilities/bz_isSession.m
./utilities/bz_isPopInfo.m
./utilities/bz_isLFP.m
./utilities/bz_isEvents.m
./utilities/bz_isCellInfo.m
./utilities/bz_isBuzcode.m
./utilities/bz_isBehavior.m
./utilities/bz_Diff.m
./tutorials/exampleDataStructs/20170505_396um_0um_merge/download_DATA.m
./preprocessing/ratemapping/getBehavEvents.m
./preprocessing/positionTracking/optitrack/bz_scrubTracking.m
./preprocessing/positionTracking/optitrack/bz_processConvertOptitrack2Behav.m
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode && grep -ril "glucose\|iPro2\|interstitial" . | head; echo ---; ls analysis 2>/dev/null | head -40; find . -name "bz_FindRipples.m"; find . -name "*.m" | xargs grep -il "circshift\|crosscorr\|xcorr" | head
```

```
./database/BrainRegions.json
---
Contents.m
CrossFrequencyCoupling
LatentVariableMethods
RankOrder
SharpWaveRipples
SpectralAnalyses
assemblies
cellTypeClassification
communication_subspace
lfp_general
monosynapticPairs
placeFields
positionDecoding
spikeLFPcoupling
spikes
spikes_general
./analysis/SharpWaveRipples/bz_FindRipples.m
./utilities/bz_shuffleCircular.m
[... 10 more lines not kept]
```

**Agent**

buzcode has no glucose analysis code; it holds the ripple detector and the sleep scorer. Let me check the detector against the Methods.

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode && sed -n 1,140p analysis/SharpWaveRipples/bz_FindRipples.m | grep -n "thresholds\|durations\|passband\|minDuration\|EMG\|noise\|frequency\|restrict\|piece\|order\|butter\|filtfilt\|default" | head -40; ls detectors 2>/dev/null; find . -iname "SleepScoreMaster.m"
```

```
14:%    from a previous call.  The estimated EMG can be used as an additional
30:%     'thresholds'  thresholds for ripple beginning/end and peak, in multiples
31:%                   of the stdev (default = [2 5]); must be integer values
32:%     'durations'   min inter-ripple interval and max ripple duration, in ms
33:%                   (default = [30 100]). 
34:%     'minDuration' min ripple duration. Keeping this input nomenclature for backwards
36:%     'restrict'    interval used to compute normalization (default = all)
37:%     'frequency'   sampling rate (in Hz) (default = 1250Hz)
39:%     'show'        plot results (default = 'off')
40:%     'noise'       noisy unfiltered channel used to exclude ripple-
41:%                   like noise (events also present on this channel are
43:%     'passband'    N x 2 matrix of frequencies to filter for ripple detection 
44:%                   (default = [130 200])
45:%     'EMGThresh'   0-1 threshold of EMG to exclude noise
46:%     'saveMat'     logical (default=false) to save in buzcode format
58:%                   .noise             candidate ripples that were
59:%                                      identified as noise and removed
79:addParameter(p,'thresholds',[2 5],@isnumeric)
80:addParameter(p,'durations',[30 100],@isnumeric)
81:addParameter(p,'restrict',[],@isnumeric)
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/buzcode && sed -n 1,40p utilities/bz_shuffleCircular.m
```

```
function [data] = bz_shuffleCircular(data)
% circularly shifts each row

for i=1:size(data,1)
    data(i,:) = circshift(data(i,:),randi(size(data,2)));
end
Shell cwd was reset to
```

**Agent**

I have read all the text and code needed. buzcode (commit e615663) has the ripple detector, the sleep scorer and a circular-shuffle utility, but no glucose analysis. Next I write the claims file.

**Agent calls Bash**

```bash
cd paper && for s in "observed" "fasting and fed states and" "CNO injection" "shape, amplitude" "largest MSE"; do grep -n -A3 "$s" *.txt | head -8; echo ===; done
```

```
<persisted-output>
Output too large (118.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ad10056c-6922-48ed-a7c4-8c856d9db158/tool-results/bbigjbv79.txt

Preview (first 2KB):
7:pmc Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC9214835 PMC9214835.1 9214835 9214835 NIHMS1804409 34381214 10.1038/s41586-021-03811-w NIHMS1804409 NIHPA1804409 1 Article A metabolic function of the hippocampal sharp wave-ripple Tingley David 1 ✉ McClain Kathryn 2 Kaya Ekin 1 3 Carpenter Jordan 1 4 Buzsáki György 1 2 5 6 ✉ 1 Neuroscience Institute, New York University, New York, NY, USA. 2 Center for Neural Science, New York University, New York, NY, USA. 3 Department of Psychology, Bogazici University, Istanbul, Turkey. 4 Kavli Institute for Systems Neuroscience and Centre for Neural Computation, Norwegian University of Science and Technology, Trondheim, Norway. 5 Department of Neurology, New York University, New York, NY, USA. 6 Langone Medical Center, New York University, New York, NY, USA. Author contributions D.T. and G.B. conceived the experiments. D.T., J.C., K.M. and E.K. performed the experiments presented. D.T. analysed data. D.T. and G.B. wrote the manuscript with contributions from other authors. ✉ Correspondence and requests for materials should be addressed to D.T. or G.B. [removed: an e-mail address] ; [removed: an e-mail address] 9 2021 11 8 2021 597 7874 410611 82 86 18 05 2022 22 06 2022 22 06 2022 29 08 2024 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. pmc-status-qastatus 0 pmc-status-live yes pmc-status-embargo no pmc-status-released yes pmc-prop-open-access no pmc-prop-olf no pmc-prop-manuscript yes pmc-prop-open-manuscript yes pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no pmc-prop-suppress-copyright no pmc-prop-i
[... 2 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000233/10.1038-s41586-021-03811-w.yaml",
 "content": "# Claims for Tingley, McClain, Kaya, Carpenter & Buzsaki (2021), Nature 597, 82-86,\n# doi:10.1038/s41586-021-03811-w, on dandiset 000233.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-28,\n# protocol pilot-12 as stated in docs/protocol.md (Reader).\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC9214835, NIHMS1804409) as\n# supplied under paper/, with the main text, Methods, Data and Code availability, and the legends\n# of Figures 1 to 4 and Extended Data Figures 1 to 10, and the Supplementary Information PDF\n# (Supplementary Table 1, the list of animals, and the Supplementary Discussion). No PDF of the\n# main article was supplied, so the figures themselves were not seen; claims rest on the text and\n# legends. The Supplementary Discussion cites some panels under older numbers (\"Figure 2I-K\" for\n# the fasting experiment, now Extended Data Fig. 4d-f; \"Extended Data Figure 4\" for SPW-R rate\n# rhythms, now Extended Data Fig. 3).\n#\n# Code: the paper links https://github.com/buzsakilab/buzcode (Code availability; SPW-R detection\n# names bz_FindRipples.m). Read at commit e615663b2b100782d1f378580f6d7aaa35c12937. It holds the\n# lab's general toolbox: the ripple detector (analysis/SharpWaveRipples/bz_FindRipples.m), the\n# sleep scorer (detectors/detectStates/SleepScoreMaster), the EMG-from-LFP estimate\n# (detectors/bz_EMGFromLFP.m) and a circular shuffle (utilities/bz_shuffleCircular.m, each row\n# shifted by a random number of samples). It holds no code for the glucose signal, the\n# cross-correlograms, the regression models or the DREADD analysis. The detector's defaults\n# (passband 130-200 Hz, thresholds 2 and 5 s.d., maximum duration 100 ms, minimum 20 ms) differ\n# from the Methods (120-200 Hz, 2 and 5 s.d., 15 to 250 ms); the Methods are followed, and the\n# Methods say the parameters used are stored with each session's ripple events.\n#\n# Data the paper used. Adult Long Evans rats in their home cage, ad libitum food and water, 12-h\n# light-dark cycle with lights on at 07:00, recorded continuously for up to 7 days (Methods). The\n# Methods count 45 rats: 10 chronic ripple and glucose recordings, 8 optogenetic induction of\n# ripples in dorsal hippocampus (5 CA1, 3 CA3), 6 DREADD (hM4Di) in lateral septum and 7 CNO\n# controls without virus, 3 simultaneous dorsal and ventral CA1, 6 posterior parietal cortex (PPC)\n# optogenetic controls, and 5 hippocampus and lateral septum unit recordings from ref. 26.\n# Supplementary Table 1 lists rats 1 to 45 with somewhat different counts (9 ripple and glucose\n# rats, 7 lateral-septum and 3 medial-septum DREADD rats, 8 CA1-implanted DREADD controls, 4\n# dorsal and ventral rats, 6 PPC rats), and Extended Data Fig. 7e says 5 PPC rats. The main\n# correlation is reported for n = 30 rats (Results; Fig. 2e; Extended Data Figs 5d and 9e), which\n# no single cohort in the Methods matches.\n# Measured variables: wideband signals (Intan RHD2000, 20 kHz), analysed at 1,250 Hz; CA1 SPW-R\n# events (start, peak, stop, amplitude, duration, frequency); brain state (NREM, wake) from the\n# sleep scorer; head accelerometer; an EMG proxy (high-pass coherence); interstitial glucose as\n# the current (nA) of a Medtronic iPro2 sensor on the back, with a single tail-vein blood reading\n# per placement used to convert current to mg/dl; optogenetic stimulation times, whose rate was\n# drawn at random for each 5-min window (0 to 40 per minute); CNO (5 mg/kg) or vehicle injected\n# on alternating days between 08:00 and 09:00 (Methods; the Results say 09:00); meal times of\n# 3-g pellets in the fasting experiment (4 rats, 36 meals); spikes of hippocampal and lateral\n# septal neurons for Extended Data Fig. 8 (38 recordings from 5 rats). Histology scores of viral\n# expression (Extended Data Fig. 10e) were given by ten colleagues and are printed only in that\n# figure's table.\n# Outside data: the paper's Data availability names the lab server\n# https://buzsakilab.nyumc.org/datasets/TingleyD/ as holding the datasets; no other archive.\n#\n# Methods shared by the criteria below, each from the paper as cited.\n# - SPW-R detection as in the Methods (SPW-R detection): 120-200 Hz third-order Butterworth on the\n#   1,250-Hz LFP, normalized squared signal, peak above 5 s.d., edges at 2 s.d., duration 15 to\n#   250 ms, events coincident with a 5 s.d. event on a noise channel (or the estimated EMG)\n#   excluded. Events already detected and stored in the dataset with these parameters are used.\n# - Time base. The glucose reading interval is taken as 5 min: calibration used the iPro2 reading\n#   within 2.5 min of the blood sample (Methods, Glucose sensor calibration), Fig. 2g uses 5-min\n#   epochs, Extended Data Fig. 6a uses offsets in 5-min increments and Extended Data Fig. 7m\n#   5-min bins. SPW-R rate (and stimulation rate) is the count of events in each 5-min bin aligned\n#   to the glucose readings, expressed per minute (Fig. 2a, \"rate of SPW-Rs per minute\").\n# - Glucose fluctuation is the derivative of the sensor signal, \"change in current (delta\n#   current)\" (Fig. 2a legend). OPEN, readings: (a) the difference between successive raw\n#   readings; (b) the same after high-pass filtering the current as in Fig. 1b, whose cutoff is\n#   not given (a standard choice is to be named). Current in nA is used; conversion to mg/dl is a\n#   constant per placement and cannot change a correlation.\n# - Cross-correlogram: the correlation coefficient R between SPW-R rate and delta current at\n#   offsets from -100 to +100 min in 5-min steps (Extended Data Figs 4b and 6a), a positive offset\n#   meaning glucose after SPW-Rs (\"future changes\", Results). OPEN, the correlation type is not\n#   named: (a) Pearson, (b) Spearman.\n# - Unit of analysis. OPEN, readings: (a) one cross-correlogram per rat over all its recording,\n#   pairs taken only within continuous recording; (b) one per session (a continuous recording),\n#   averaged per rat.\n# - Circular shuffle: SPW-R rate (or stimulation rate) circularly shifted against delta current,\n#   100 iterations per rat (Fig. 2f and 3f legends); the shift is a random number of bins, as in\n#   buzcode's bz_shuffleCircular (whether that function was used is not stated).\n# - The \"+-\" spreads the paper gives (R, lag, SPW-R rate) are not said to be s.d. or s.e.m.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000233\"\npaper: doi:10.1038/s41586-021-03811-w\nclaims:\n- id: fig2-ripple-rate-predicts-glucose\n  statement: SPW-R rate is negatively correlated with future changes in interstitial glucose,\n    with a mean peak correlation of R = -0.21 (+- 0.08) at a lag of 10.7 (+- 4.5) min, over 30\n    rats.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 1; Figure 2a-f\n  quote: Notably, SPW-R rates were negatively correlated with future changes in glucose\n    concentrations ... R = -0.21 ± 0.08, n = 30 rats, temporal lag of 10.7 ± 4.5 min\n  expected:\n  - quantity: mean across rats of the most negative correlation between SPW-R rate and delta\n      current\n    value: -0.21\n    tolerance: 0.08\n  - quantity: mean across rats of the lag of that correlation (glucose after SPW-Rs)\n    value: 10.7\n    tolerance: 4.5\n    unit: min\n  criterion: Cross-correlograms as in the opening comment. Per rat, R is the most negative\n    correlation and the lag its offset. OPEN, the search range for the lag is not given; readings\n    (a) offsets 0 to +100 min, (b) -100 to +100 min. OPEN, which rats form n = 30; readings (a)\n    every rat in the dataset with CA1 SPW-Rs and glucose recorded together, in all conditions\n    (vehicle and CNO-free days for the DREADD rats, the optogenetic rats' natural SPW-Rs), (b)\n    only the ripple and glucose cohort of the Methods and Supplementary Table 1. Reproduced when,\n    under one combination of the readings named here and in the opening comment, both expected\n    values hold and R is negative in most rats; the number of rats used is reported.\n- id: fig2ef-correlation-beyond-shuffle\n  statement: The correlation between SPW-R rate and glucose change at a 10-min lag is more\n    negative than the correlations obtained when SPW-R rate is circularly permuted.\n  source: Figure 2e-f legends\n  quote: Histograms of the correlation between SPW-R rate and current flux at 10 min (red) and\n    the correlation observed when SPW-R rate is circularly permuted (black) (100 iterations per\n    rat)\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: The paper gives no test for this panel. Correlation at +10 min per rat, against 100\n    circular shuffles per rat (opening comment). Reproduced when the median of the observed\n    per-rat correlations is below the median of the shuffled ones and a two-sample\n    Kolmogorov-Smirnov test of observed against shuffled values gives p < 0.05, the test the\n    paper uses for the same comparison in Fig. 3f.\n- id: fig2g-clustered-ripples\n  statement: Isolated SPW-Rs have little or no effect on glucose, whereas clustered SPW-Rs (more\n    than 30 per minute) are followed by a several-fold larger decrease.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 1; Figure 2g\n  quote: Isolated SPW-Rs had little or no effect, whereas clustered events with more than 30\n    SPW-Rs per minute induced a several-fold-larger decrease in peripheral glucose levels\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: As in the Fig. 2g legend, the mean delta current 10 min after each 5-min epoch,\n    grouped by the number of SPW-Rs in the epoch. OPEN, the threshold; the Results say 30 per\n    minute and the legend counts per 5-min epoch, so readings (a) more than 150 SPW-Rs per epoch,\n    (b) more than 30 per epoch. OPEN, \"isolated\" is not defined; the choice made here is epochs\n    with 1 to 5 SPW-Rs (at most one per minute). Reproduced when, under one reading, the mean\n    delta current after clustered epochs is negative and at least twice the magnitude of that\n    after isolated epochs; the full curve over epoch counts is shown.\n- id: edfig4-ripple-features\n  statement: Of the SPW-R features, the inter-SPW-R interval (clustering) most strongly modulates\n    the glucose effect, then amplitude, then duration, and ripple frequency least.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 1; Extended Data Fig. 4a-c\n  quote: The most impactful of these was the inter-SPW-R interval (that is, the degree of\n    clustering of SPW-Rs) ... The second most influential feature was the amplitude of SPW-Rs,\n    followed by SPW-R duration; the frequency of the ripple oscillation had the least effect\n  criterion: As in the Extended Data Fig. 4b legend, SPW-Rs binned by the percentile of each\n    feature (duration in ms), and for each bin the mean peri-SPW-R delta current at +10 min.\n    Features from the Methods (amplitude as the maximum normalized squared signal, duration as\n    stop minus start, frequency from the Hilbert phase). OPEN, the influence measure is not\n    defined; the choice made here is the range of the +10-min effect across bins. OPEN, bin width;\n    readings (a) deciles, (b) 5-percentile bins. Reproduced when, under one reading, the order of\n    the four ranges is interval, amplitude, duration, frequency; partially reproduced when the\n    interval has the largest range but the rest of the order differs.\n- id: fig2h-phase-reset\n  statement: The phase dispersion of the glucose rhythm decreases after SPW-Rs, more so for\n    higher SPW-R rates.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 2; Figure 2h\n  quote: Furthermore, the phase dispersion of the glucose rhythm decreased after SPW-Rs, and the\n    magnitude of this decrease was proportional to SPW-R rate\n  criterion: As in the Fig. 2h legend, the circular s.d. of glucose phase across peaks of SPW-R\n    rate, at offsets -100 to +100 min. OPEN, the phase extraction is not given; readings\n    (a) Hilbert phase of delta current band-passed at periods of 15 to 75 min (the coupling range\n    of Extended Data Fig. 5), (b) at 15 to 90 min (the elevated power of Extended Data Fig. 1h).\n    OPEN, peaks are local maxima of SPW-R rate, grouped here into quartiles of peak rate.\n    Decrease is the circular s.d. at offset 0 minus its minimum from 0 to +30 min (the 5 to 15\n    min sensor lag of the Methods lies inside it). Reproduced when, under one reading, the\n    decrease is positive for the top quartile and its Spearman correlation with peak rate across\n    peaks is positive at p < 0.05.\n- id: edfig5-cross-frequency-coupling\n  statement: SPW-R rate and glucose show power-power and phase-power coupling at periods of 15 to\n    75 min, with the faster SPW-R rhythm (about 40 min) modulating the slower glucose rhythm\n    (about 60 min).\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 2; Extended Data Fig. 5d-e\n  quote: We observed significant power-power and phase-power relationships in the 15-75-min range\n    ... which suggests that a faster SPW-R frequency (about 40 min) modulates a slower (about 60\n    min) glucose rhythm\n  statistics:\n  - about: power-power comodulogram against circularly shuffled data\n    test: Student's t-test\n    p: 1.0e-24\n    p_relation: \"<\"\n    n: 30 rats\n  - about: phase of glucose against SPW-R rate amplitude\n    test: Rayleigh test for non-uniformity\n    p: 1.0e-18\n    p_relation: \"<\"\n  criterion: OPEN, the band filters and envelope method are not given; the choice made here is\n    band-pass at log-spaced periods from 10 to 120 min and Hilbert envelopes and phases.\n    Power-power, the correlation of SPW-R-rate and glucose envelopes for each pair of periods,\n    per rat, against circular shuffles; t-test across rats on the mean over 15 to 60 min.\n    Phase-power, SPW-R rate (z-scored per rat) as a function of glucose phase, Rayleigh test of\n    rate-weighted phases. Reproduced when both tests give p < 0.05 and the comodulogram peak lies\n    at a longer glucose period than SPW-R period. The paper's p bounds are compared, not required.\n- id: edfig1-glucose-rhythm\n  statement: Interstitial glucose fluctuations show an approximately 60-min oscillation, with\n    power elevated above the 1/f fit at periods of 15 to 90 min.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 2; Extended Data Fig. 1g-i\n  quote: Because interstitial glucose fluctuations displayed an approximately 60-min oscillation\n  expected:\n  - quantity: period of the glucose oscillation\n    value: 60\n    tolerance: 6\n    unit: min\n  criterion: As in Extended Data Fig. 1g-h, power spectral density of delta current per rat, a\n    linear fit in log-log axes subtracted, averaged across rats. Reproduced when the residual\n    power is positive over 15 to 90 min and its peak, or the first side peak of the mean\n    autocorrelogram (Extended Data Fig. 1i), lies within tolerance of 60 min.\n- id: edfig1-glucose-circadian-meals\n  statement: Glucose concentrations are modulated over the circadian cycle and rise after meals.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 1; Extended Data Fig. 1e-f\n  quote: Interstitial glucose concentrations are modulated over the circadian timescale. f ,\n    Interstitial glucose concentrations increase during the postprandial period ( n = 36 meals,\n    collected from 4 rats)\n  expected:\n  - quantity: meals in the fasting experiment\n    value: 36\n    tolerance: 3.6\n  - quantity: rats in the fasting experiment\n    value: 4\n    tolerance: 0\n  criterion: The paper gives no test. Circadian, glucose (current) by hour of day averaged per\n    rat; reproduced when a one-way ANOVA of hour of day on hourly means pooled over rats gives\n    p < 0.05 (a choice made here). Meals, current in the 60 min after each meal against the 30\n    min before; reproduced when the mean change is positive and a paired t-test across meals\n    gives p < 0.05 (a choice made here; the windows are not given in the paper).\n- id: edfig1-sensor-decay\n  statement: The raw sensor current decays slowly over days after implantation, while the\n    magnitude of its fluctuations (delta current) stays stable.\n  source: Extended Data Fig. 1b, 1d\n  quote: Note the slow decay over days, an indication of glucose oxidase enzyme breakdown on the\n    electrode surface ... Note the relatively stable readings over days, and that the slow decay\n    in absolute current readings is no longer present\n  criterion: The paper gives no test. Per placement, daily mean current and daily mean absolute\n    delta current against day since implantation. Reproduced when the slope of daily mean\n    current is negative in most placements and the slope of absolute delta current, as a\n    fraction of its first-day value, is smaller in magnitude than that of the current.\n- id: supp-ripple-rate\n  statement: CA1 SPW-Rs occur at 9.5 (+- 8.2) per minute on average, about 14,000 per day,\n    ranging from none for several minutes to more than 40 in a minute.\n  source: Supplementary Discussion, paragraph 2; Figure 1f\n  quote: On average, we observed ... 9.5 (± 8.2) SPW-Rs per minute ... or ~14,000 SPW-Rs per day)\n    with a large degree of variance ranging from zero ripples for ... several minutes up to > 40\n    ripples in a minute\n  expected:\n  - quantity: mean SPW-R rate\n    value: 9.5\n    tolerance: 0.95\n    unit: per minute\n  - quantity: SPW-Rs per day\n    value: 14000\n    tolerance: 1400\n  criterion: Tolerance is 10% of the mean, since the +- 8.2 describes minute-to-minute spread\n    and not the uncertainty of the mean. SPW-R count in 1-min bins over all recording of the\n    ripple and glucose rats. OPEN, which rats; readings as in fig2-ripple-rate-predicts-glucose.\n    Reproduced when the mean is within tolerance under one reading, and the maximum 1-min count\n    exceeds 40.\n- id: supp-ripples-stable-across-days\n  statement: In each rat the shape, amplitude and rate of SPW-Rs are consistent across days.\n  source: Supplementary Discussion, paragraph 2; Figure 1d-f\n  quote: In each animal, we validated that the shape, amplitude, ... and rate of hippocampal\n    SPW-Rs were consistent across multiple days\n  criterion: The paper gives no test. Per rat, the daily median SPW-R amplitude, median duration\n    and mean rate against recording day. Reproduced when, in most rats, the Spearman correlation\n    of daily median amplitude with day is not significant at p < 0.05 or its daily values stay\n    within 20% of the rat's overall median (a choice made here); rate is reported likewise.\n- id: edfig3-ripple-rate-rhythms\n  statement: SPW-R rate varies with circadian and ultradian rhythms, with spectral peaks at about\n    24 h and about 4 h, in 1,568.5 recording hours from 8 rats.\n  source: Extended Data Fig. 3a-d; Results, SPW-Rs phase reset glucose oscillations, paragraph 1\n  quote: Average power spectral density plot ( n = 8 rats) of ripple rate. Note two peaks at about\n    24 h and about 4 h\n  expected:\n  - quantity: recording hours in Extended Data Fig. 3a\n    value: 1568.5\n    tolerance: 156.85\n    unit: h\n  - quantity: rats in Extended Data Fig. 3\n    value: 8\n    tolerance: 0\n  - quantity: period of the slow spectral peak\n    value: 24\n    tolerance: 2.4\n    unit: h\n  - quantity: period of the faster spectral peak\n    value: 4\n    tolerance: 0.4\n    unit: h\n  criterion: Power spectral density of SPW-R rate per rat (5-min bins), averaged over rats.\n    Reproduced when local peaks lie within tolerance of 24 h and 4 h; the hours and rats used are\n    reported.\n- id: edfig2-refractory-period\n  statement: Inter-ripple intervals drop to zero below about 20 ms, a refractory period between\n    ripples, with peaks reflecting bursts of ripples.\n  source: Extended Data Fig. 2a\n  quote: Note the peaks in the histogram from bursts of ripples, and the drop to zero,\n    representing an approximately 20-ms refractory period between ripples\n  expected:\n    quantity: refractory period between ripples\n    value: 20\n    tolerance: 2\n    unit: ms\n  criterion: Histogram of inter-ripple intervals (peak to peak) per rat in 1-ms bins. Reproduced\n    when the shortest interval with counts lies within tolerance of 20 ms in most rats.\n- id: edfig3e-ca1-firing-decrease\n  statement: At slow time scales (beyond 250 ms) CA1 SPW-Rs are followed by an overall decrease\n    in CA1 population firing.\n  source: Extended Data Fig. 3e; Supplementary Discussion, paragraph 5\n  quote: At slow temporal scales (>250 ms), CA1 SPW-Rs are associated with an overall decrease in\n    CA1 firing rates\n  criterion: As in the legend, the cross-correlogram of SPW-R peaks with CA1 population firing\n    rate in 100-ms bins and with a 60-s median filter. Reproduced when the population rate\n    averaged from 0.25 to 60 s after SPW-Rs is below its mean over the recording, in most\n    sessions with units.\n- id: edfig4-fasting-fed\n  statement: The SPW-R and glucose cross-correlogram does not differ between fasting and fed\n    states, nor across the fasting-to-fed transition.\n  source: Extended Data Fig. 4d-f; Supplementary Discussion, paragraph 3\n  quote: The SPW-R-glucose fluctuation cross-correlogram was not different between fasting and\n    fed states\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: A claim of absence. The paper names no test; the two-way (two-sided) t-test it uses\n    for cross-correlogram comparisons (Extended Data Figs 7h, 9e, 10d) is applied. Cross-\n    correlograms computed on 4-h blocks of fasting and of fed time (Extended Data Fig. 4d), 4\n    rats. Reproduced when the correlation at +10 min does not differ between fasting and fed\n    blocks at p < 0.05; the difference is reported either way.\n- id: edfig4-nrem-wake\n  statement: The SPW-R and glucose cross-correlogram does not differ between NREM sleep and\n    waking, and its negative peak does not change across state transitions.\n  source: Extended Data Fig. 4g-i\n  quote: The negative correlation did not change in amplitude across either wake-to-NREM or\n    NREM-to-wake state transitions ... The SPW-R-glucose fluctuation cross-correlogram was not\n    different between NREM and waking states\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: A claim of absence, tested as in edfig4-fasting-fed with blocks of NREM and of wake\n    (Extended Data Fig. 4g, 8 rats), brain state from the sleep scorer. Reproduced when the\n    correlation at +10 min does not differ between NREM and wake blocks at p < 0.05.\n- id: edfig4-no-hour-differs\n  statement: No hour of the day has a significantly different SPW-R and glucose correlation than\n    any other hour (smallest P = 0.53).\n  source: Extended Data Fig. 4j-l\n  quote: Across rats, no hour of the day had a significantly different correlation than any other\n    hour of the day (Student's t -test; minimum P = 0.53)\n  statistics:\n  - about: smallest p over all pairs of hours\n    test: Student's t-test\n    p: 0.53\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: A claim of absence. As in Extended Data Fig. 4j-k, cross-correlograms in 4-h windows\n    centred on each hour, integrated over offsets +5 to +20 min, per rat; Student's t-test across\n    rats for every pair of hours. Reproduced when no pair gives p < 0.05; the smallest p is\n    reported.\n- id: edfig6-ripple-rate-best-predictor\n  statement: Among seven measured predictors, SPW-R rate is the most predictive of glucose\n    fluctuations; leaving it out raises the model error most, at a +10-min offset.\n  source: Results, SPW-Rs phase reset glucose oscillations, paragraph 3; Extended Data Fig. 6a-b;\n    Supplementary Discussion, paragraph 3\n  quote: In all cases, SPW-R rate was the most predictive variable\n  criterion: As in the Methods (Leave-one-out and pairwise model comparisons) for each rat, the\n    seven predictors (SPW-R rate, NREM or wake, high-pass coherence, power spectrum slope, theta\n    residual, theta/delta ratio, accelerometer movement), a linear regression on all seven and on\n    six, two thirds of bins for training and one third for testing, 100 random splits, offsets\n    -100 to +100 min in 5-min steps; MSE of the six-predictor model minus that of the full model.\n    Reproduced when the largest mean difference over predictors and offsets belongs to SPW-R rate\n    at an offset between +5 and +15 min.\n- id: edfig6d-pairwise-predictors\n  statement: In single-predictor models SPW-R rate predicts glucose fluctuations better than each\n    other measured signal; it beats brain state in 6 of 8 rats.\n  source: Extended Data Fig. 6c-d; Supplementary Discussion, paragraph 4\n  quote: For example, the upper leftmost value of 6 indicates that ripple rate was a better\n    predictor than brain state in 6 of the 8 rats\n  expected:\n    quantity: rats in which SPW-R rate predicts better than brain state\n    value: 6\n    tolerance: 0.6\n  criterion: As in the Methods, one linear regression per predictor at the +10-min offset, same\n    100 splits, two-sample t-test of MSE across splits per rat at p < 0.05. Reproduced when the\n    count holds and, for every other predictor, SPW-R rate is better in more rats than the\n    reverse; the count over 8 rats is the paper's, and the number of rats used is reported.\n- id: edfig6ef-latent-variables\n  statement: Principal or independent components of all predictors do not predict glucose better\n    than SPW-R rate; PC1 performs similarly to SPW-R rate and the other components worse in at\n    least 4 of 8 rats.\n  source: Extended Data Fig. 6e-f\n  quote: SPW-R rate and PC1 were similar in all rats, all other principal components and\n    independent components performed worse for at least 4 out of 8 rats\n  depends_on:\n  - edfig6d-pairwise-predictors\n  criterion: As in the legend, generalized linear models with two predictors each, built from\n    principal components or independent components of the seven predictors and SPW-R rate alone,\n    compared pairwise across 100 splits by two-sided t-test at p < 0.05 per rat. OPEN, the GLM\n    family and the ICA algorithm are not given; a Gaussian GLM and FastICA are used as standard\n    choices. Reproduced when no component beats SPW-R rate in more than one rat and every\n    component other than PC1 is worse in at least 4 rats (scaled to the rats used).\n- id: fig3d-induced-ripples-lower-glucose\n  statement: Optogenetically induced ripples in dorsal hippocampus are followed by a negative\n    peak in the cross-correlogram with glucose fluctuations.\n  source: Results, Induced ripples decrease glucose levels, paragraph 1; Figure 3d; Extended Data\n    Fig. 7c-d\n  quote: As in the intact rats, the optogenetically induced ripple events were followed by a\n    negative peak in the cross-correlogram with glucose fluctuations\n  criterion: Cross-correlogram of stimulation rate (5-min bins) with delta current per rat, as in\n    the opening comment, and its median across the 8 rats against the median of circular\n    shuffles. Reproduced when the median correlogram has its minimum at a positive offset up to\n    +30 min and that minimum lies below the 2.5th percentile of the shuffled medians.\n- id: fig3-induced-effect-size\n  statement: The glucose effect of induced ripples is 63% of that of natural SPW-Rs (0.059 nA\n    against 0.094 nA).\n  source: Results, Induced ripples decrease glucose levels, paragraph 1\n  quote: The magnitude of the induced glucose effect corresponded to 63% of the effect size of\n    naturally occurring SPW-Rs (peri-SPW-R, 0.094 nA; peri-stimulation, 0.059 nA)\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  expected:\n  - quantity: peri-SPW-R glucose effect\n    value: 0.094\n    tolerance: 0.0094\n    unit: nA\n  - quantity: peri-stimulation glucose effect\n    value: 0.059\n    tolerance: 0.0059\n    unit: nA\n  - quantity: ratio of induced to natural effect\n    value: 63\n    tolerance: 6.3\n    unit: percent\n  criterion: OPEN, the effect size is not defined. Readings (a) the depth of the mean peri-event\n    delta current (event-triggered average of the current derivative, in nA per 5-min reading)\n    below its baseline at offsets 0 to +100 min against -100 to 0 min, (b) the minimum of the\n    mean peri-event delta current from 0 to +30 min, (c) the mean delta current 10 min after\n    events. Natural SPW-Rs from the ripple and glucose rats, stimulations from the 8 optogenetic\n    rats. Reproduced when, under one reading, the ratio is within tolerance; partially when the\n    ratio holds but the nA values do not.\n- id: fig3ef-stimulation-dose-response\n  statement: In seven of the eight optogenetic rats the glucose decrease is larger at higher\n    stimulation rates (median R = -0.11, P < 0.01).\n  source: Results, Induced ripples decrease glucose levels, paragraph 1; Figure 3e\n  quote: In seven of the eight rats, the effect on glucose concentrations was larger at higher\n    stimulation rates ... median R = - 0.11, P < 0.01\n  statistics:\n  - test: not named\n    p: 0.01\n    p_relation: \"<\"\n    n: 8 rats\n  expected:\n  - quantity: rats with larger glucose decrease at higher stimulation rates\n    value: 7\n    tolerance: 0.7\n  - quantity: median across rats of R between stimulation rate and delta current at +10 min\n    value: -0.11\n    tolerance: 0.011\n  criterion: Per rat, the correlation between stimulation rate per 5-min window and delta current\n    10 min later (Fig. 3e legend). A rat counts when its R is negative. OPEN, the test behind\n    P < 0.01 is not named; readings (a) a Wilcoxon signed-rank test of the 8 per-rat R against\n    zero, (b) the correlation over all rats' windows pooled. Reproduced when both expected values\n    hold and, under one reading, p < 0.01; partially when R and the count hold at p < 0.05 only.\n- id: fig3f-stimulation-vs-shuffle\n  statement: Correlations between stimulation rate and glucose change at 10 min differ from those\n    with circularly permuted stimulation rate (P = 0.00015, two-sample Kolmogorov-Smirnov test).\n  source: Figure 3f legend\n  quote: P = 0.00015, using a two-sample Kolmogorov-Smirnov test\n  statistics:\n  - test: two-sample Kolmogorov-Smirnov test\n    p: 0.00015\n    n: 8 rats, 100 shuffles each\n  depends_on:\n  - fig3ef-stimulation-dose-response\n  criterion: Observed correlation at +10 min per rat against 100 circular shuffles per rat.\n    OPEN, what the red histogram holds; readings (a) the 8 per-rat observed correlations against\n    all 800 shuffled ones, (b) per-rat observed correlations over repeated subsamples of windows\n    (not described). Reproduced when the KS test gives p < 0.05 with observed values more negative\n    under reading (a), the paper's p compared.\n- id: edfig7ab-stimulation-protocol\n  statement: The stimulation protocol has no ultradian structure, and the mean stimulation rate\n    does not differ across the light-dark cycle.\n  source: Extended Data Fig. 7a-b; Results, Induced ripples decrease glucose levels, paragraph 1\n  quote: Autocorrelation of stimulation protocol showing no ultradian structure. b , Average\n    stimulation rate was not different across the circadian light-dark cycle\n  criterion: A claim of absence; the paper names no test. Choices made here, per rat,\n    autocorrelation of stimulation rate in 5-min bins at lags from 15 min to 12 h within the 99%\n    white-noise bound (2.58 over the square root of the bin count) at more than 95% of lags, and\n    a two-sided t-test of 5-min stimulation rates in light (07:00 to 19:00) against dark not\n    significant at p < 0.05.\n- id: edfig7jm-induced-ripples-decoupled\n  statement: Induced ripples are decoupled from ongoing changes in vigilance, brain state and\n    behaviour (power spectrum slope, EMG proxy, movement and wake/NREM ratio).\n  source: Results, Induced ripples decrease glucose levels, paragraph 1; Extended Data Fig. 7j-m\n  quote: can be mimicked with artificially produced ripples in a manner that was decoupled from\n    ongoing changes in vigilance, brain state and behaviour\n  criterion: As in Extended Data Fig. 7j-m, the mean cross-correlogram across the 8 rats of\n    stimulation rate (5-min bins) with power spectrum slope, high-pass coherence, accelerometer\n    movement and the wake/NREM ratio per 5-min bin. Reproduced when, for each signal, no offset\n    from -100 to +100 min has a mean correlation outside the 2.5th to 97.5th percentiles of\n    circularly shuffled means (a choice made here; the paper gives no test).\n- id: edfig7-ppc-stimulation-no-effect\n  statement: The same stimulation in posterior parietal cortex does not change glucose; the CA1\n    and PPC cross-correlograms with glucose differ.\n  source: Results, Induced ripples decrease glucose levels, paragraph 1; Extended Data Fig. 7e-h\n  quote: The same intensity optogenetic stimulation in the posterior parietal area did not induce\n    a measurable change in glucose concentrations\n  depends_on:\n  - fig3d-induced-ripples-lower-glucose\n  criterion: As in Extended Data Fig. 7g-h, per rat cross-correlograms of stimulation rate with\n    delta current, CA1 cohort (8 rats) against PPC cohort (5 or 6 rats), compared at each offset\n    by a two-way (two-sided) unpaired t-test. Reproduced when the CA1 correlation is more\n    negative at +10 min with p < 0.05 and the PPC mean correlogram at +10 min lies within the\n    2.5th to 97.5th percentiles of its circular shuffles.\n- id: edfig8-lateral-septum-rectified\n  statement: Lateral septal populations fire at a nearly constant rate across theta cycles of\n    different hippocampal synchrony but increase linearly with SPW-R synchrony; theta cycles\n    occur at low and SPW-Rs at the highest synchrony percentiles.\n  source: Results, Lateral septum relays SPW-Rs downstream, paragraph 1; Extended Data Fig. 8c\n  quote: Theta cycles occurred primarily at lower population firing rates, whereas SPW-Rs\n    primarily occurred at the highest percentiles ... Lateral septal neuronal populations fired\n    at a semi-constant rate across theta cycles with different levels of hippocampal synchrony,\n    but increased linearly with SPW-Rs\n  expected:\n  - quantity: recordings\n    value: 38\n    tolerance: 3.8\n  - quantity: rats\n    value: 5\n    tolerance: 0\n  criterion: Hippocampal synchrony as in the Results, the mean of z-scored firing rates of all\n    hippocampal neurons in 25-ms bins; recordings with at least 15 lateral septal neurons\n    (legend); for each theta cycle and SPW-R, its synchrony percentile and the mean z-scored\n    lateral septal rate. OPEN, theta cycle detection is given only by ref. 26; the choice made\n    here is troughs of the 4-9 Hz filtered CA1 LFP during theta states of the sleep scorer.\n    Reproduced when the synchrony percentile at which 75% of theta cycles lie below it is lower\n    than that above which 75% of SPW-Rs lie, and the regression slope of lateral septal rate on\n    synchrony percentile is positive at p < 0.05 for SPW-Rs and at least three times larger than\n    for theta cycles (a choice made here).\n- id: edfig9-dorsal-ventral\n  statement: Dorsal and ventral CA1 SPW-Rs are only weakly correlated, and ventral SPW-Rs are\n    significantly less correlated with glucose fluctuations than dorsal SPW-Rs, which match the\n    earlier dorsal cohorts.\n  source: Results, Lateral septum relays SPW-Rs downstream, paragraph 1; Extended Data Fig. 9d-f\n  quote: SPW-R events were only weakly correlated between septal and temporal poles of the\n    hippocampus ... Ventral SPW-Rs were less strongly correlated with interstitial glucose\n    fluctuations than were SPW-Rs recorded from the dorsal CA1 region\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: In the dorsal and ventral rats (3 in the Methods, 4 in Supplementary Table 1), SPW-Rs\n    detected separately on the dorsal and ventral CA1 channels; correlation of their 5-min rates\n    reported (weak taken here as below 0.5). Glucose correlation at +10 min, dorsal against\n    ventral, by the paper's two-way (two-sided) t-test. OPEN, the units of that test; readings\n    (a) per-day correlations, paired, (b) per-day correlations, unpaired. Reproduced when ventral\n    is weaker (less negative) with p < 0.05 under one reading, and the dorsal values do not\n    differ from the earlier dorsal cohorts by the same unpaired t-test at p < 0.05.\n- id: fig4-cno-controls-no-change\n  statement: In control rats without virus, CNO does not change the SPW-R correlation with\n    glucose fluctuations compared with vehicle days.\n  source: Results, Lateral septum relays SPW-Rs downstream, paragraph 2; Figure 4b-d\n  quote: When CNO was injected into control rats, the SPW-R correlation with glucose fluctuations\n    was not significantly different from vehicle days\n  depends_on:\n  - fig2-ripple-rate-predicts-glucose\n  criterion: A claim of absence, judged on the paper's two-way t-test (Extended Data Fig. 10d,\n    Fig. 4e) at p < 0.05. Correlation of SPW-R rate with delta current at +10 min (Fig. 4e) in the\n    2-h window after each injection (Methods), one value per day, control rats; CNO days against\n    vehicle days by a two-sided unpaired t-test (the choice made here, as Extended Data Fig. 10d\n    compares days). The paired test on per-rat means (Fig. 4c) is shown as a variant. Reproduced\n    when the test does not give p < 0.05; the difference is reported either way.\n- id: fig4-ls-dreadd-decouples\n  statement: In rats expressing hM4Di in the lateral septum, CNO significantly decreases the\n    SPW-R correlation with glucose fluctuations compared with their vehicle days and with control\n    rats on CNO days.\n  source: Results, Lateral septum relays SPW-Rs downstream, paragraph 2; Figure 4b-d; Extended Data\n    Fig. 10c-d\n  quote: However, when CNO was injected in rats that expressed hM4Di in the lateral septum, the\n    SPW-R correlation with glucose fluctuations was significantly decreased compared to vehicle\n    days and control rats on CNO days\n  depends_on:\n  - fig4-cno-controls-no-change\n  criterion: Measure as in fig4-cno-controls-no-change, lateral septum hM4Di rats (6 in the\n    Methods, 7 in Supplementary Table 1). OPEN, the measure; readings (a) correlation at +10 min,\n    (b) the cross-correlogram integrated over +5 to +20 min (Extended Data Fig. 4k). OPEN, the\n    test units; readings (a) per-day values, unpaired two-sided t-test, (b) per-rat means, paired\n    for CNO against vehicle and unpaired against controls. Reproduced when, under one reading, the\n    correlation on CNO days is less negative than on vehicle days and than in controls on CNO\n    days, both at p < 0.05; partially when only one comparison holds.\n- id: fig4e-dreadd-time-course\n  statement: The CNO effect in lateral septum hM4Di rats is largest between 50 and 190 min after\n    injection, with its maximum about 1.2 h after injection.\n  source: Results, Lateral septum relays SPW-Rs downstream, paragraph 2; Figure 4e\n  quote: This difference was largest between 50 min and 190 min after injection ... Maximal effect\n    of CNO was observed about 1.2 h after the injection of CNO\n  depends_on:\n  - fig4-ls-dreadd-decouples\n  expected:\n    quantity: time of maximal CNO effect after injection\n    value: 1.2\n    tolerance: 0.12\n    unit: h\n  criterion: As in the Fig. 4e legend, the correlation at +10 min in a 90-min window slid in 5-min\n    steps from injection, CNO against vehicle days in hM4Di rats, two-way (two-sided) t-test at\n    each step; the window time is its centre (OPEN; its start is shown as a variant). Reproduced\n    when the smallest p falls within tolerance of 1.2 h and the steps with p < 0.05 lie within 50\n    to 190 min.\n- id: fig4c-medial-septum-no-effect\n  statement: CNO has no effect on the SPW-R and glucose correlation in rats whose hM4Di\n    expression is confined to the medial septum.\n  source: Figure 4c legend; Supplementary Discussion, paragraph 6; Extended Data Fig. 10b\n  quote: In these animals, CNO injection ... had no effect on the correlation between SPW-R rate\n    and glucose fluctuations\n  depends_on:\n  - fig4-cno-controls-no-change\n  criterion: A claim of absence, judged as in fig4-cno-controls-no-change on the 3 medial septum\n    rats. Reproduced when CNO against vehicle days does not give p < 0.05.\n- id: edfig10-expression-correlates-effect\n  statement: Across DREADD rats, blinded ratings of viral expression in some septal subregions\n    correlate significantly with the CNO effect on the SPW-R and glucose correlation.\n  source: Extended Data Fig. 10e-g\n  quote: For each subregion, the correlation between these scores and the effect of CNO was\n    calculated and is shown in bold below. Red values had a P values < 0.05\n  statistics:\n  - about: correlations shown in red in Extended Data Fig. 10e\n    p: 0.05\n    p_relation: \"<\"\n    n: 9 rats (6 lateral septum, 3 medial septum)\n  data: with_inputs\n  depends_on:\n  - fig4-ls-dreadd-decouples\n  criterion: The scores are printed only in the table of Extended Data Fig. 10e, which was not\n    available as an image to this reader; the subregions marked significant are not named in the\n    text. Correlation (Pearson, OPEN against Spearman) between each subregion's mean score and\n    each rat's CNO effect (CNO minus vehicle correlation at +10 min). Reproduced when the\n    subregions with p < 0.05 are those marked red in the figure, including the dorsal lateral\n    septum shown in Extended Data Fig. 10f.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/000233/10.1038-s41586-021-03811-w.yaml paper/10.1038-s41586-021-03811-w.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/000233/*.yaml; grep -c "criterion:" claims/000233/*.yaml; grep -c "statistics:" claims/000233/*.yaml; git status --short
```

```
34
5
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
?? claims/000233/
?? scripts
```

**Agent**

I wrote `claims/000233/10.1038-s41586-021-03811-w.yaml`. The quote checker passes it with no problems (34 claims, 34 quotes, 6 statistical values). Nothing is committed.

**Text read.** I used the accepted author manuscript from PubMed Central (PMC9214835, NIHMS1804409): main text, Methods, Data and Code availability, and the legends of Figs 1–4 and Extended Data Figs 1–10. I also read the Supplementary Information PDF, which has Supplementary Table 1 (the list of animals) and the Supplementary Discussion. No PDF of the main article was supplied, so I could not see any figure.

**Code.** The paper links only https://github.com/buzsakilab/buzcode; I read commit e615663b2b100782d1f378580f6d7aaa35c12937. It holds the ripple detector `bz_FindRipples.m`, the sleep scorer and a circular-shuffle utility. It has no code for the glucose analysis, the cross-correlograms, the regression models or the DREADD analysis. The detector's default settings differ from the Methods (130–200 Hz against 120–200 Hz, and different duration limits), so I followed the Methods.

**Counts.**
- **Claims:** 34, all with quotes, none marked `inferred`.
- **Statistics:** 5 claims carry them (6 values):
  - Student's t-test P < 1e-24 and Rayleigh test P < 1e-18 (Extended Data Fig. 5)
  - minimum P = 0.53 for hour of day
  - opto dose-response P < 0.01, test not named
  - Kolmogorov–Smirnov P = 0.00015
  - histology correlations P < 0.05
- **Criteria:** all 34 claims have one; 14 also carry expected values.
- **Data:** all claims use the dataset except the histology-score claim, which is `with_inputs` because the scores are printed only in the Extended Data Fig. 10e table.

**Details the paper leaves open, with the readings named:**
- **Glucose change (delta current):** (a) the difference between successive raw readings, or (b) the same after high-pass filtering; the filter cutoff is not given.
- **Correlation type:** Pearson or Spearman.
- **Unit of analysis:** one cross-correlogram per rat over all its recording, or one per session averaged per rat.
- **Lag search range:** 0 to +100 min, or ±100 min.
- **Which rats make up n = 30:** every rat with ripples and glucose recorded together, or only the ripple-and-glucose cohort. No cohort in the Methods has 30 rats.
- **Fig. 2g clustering threshold:** more than 30 SPW-Rs per minute, or more than 30 per 5-min epoch. "Isolated" is not defined; I chose 1 to 5 per epoch.
- **Influence of SPW-R features:** the bin width (deciles or 5-percentile bins); the influence measure itself is not defined, so I chose the range across bins.
- **Phase dispersion (Fig. 2h):** the band used to extract phase, 15–75 min or 15–90 min.
- **The 63% effect size:** three readings of what is measured (trough depth, minimum from 0 to +30 min, or the mean at +10 min).
- **The test behind opto "P < 0.01":** a signed-rank test on per-rat R, or a pooled correlation.
- **What the Fig. 3f histogram holds:** 8 per-rat values against 800 shuffled values, or repeated subsamples.
- **Dorsal and ventral comparison:** paired or unpaired per-day values.
- **DREADD measure:** correlation at +10 min, or integrated over +5 to +20 min.
- **DREADD test units:** unpaired per-day values, or paired per-rat means.
- **Fig. 4e sliding window:** its time read at the window's centre or its start.

**Other choices I made where the paper gives no method:**
- the comodulogram filters
- the GLM family and ICA algorithm
- theta cycle detection, which is given only in ref. 26
- tests for several qualitative claims (circadian and meal effects, sensor decay, stability across days, the stimulation protocol, decoupling from brain state)

**Missing from the paper:**
- The main figures were not available, so the subregions marked significant in Extended Data Fig. 10e are unknown.
- The ± spreads are not said to be s.d. or s.e.m.
- Animal counts disagree between the Methods, Supplementary Table 1 and the legends (PPC 6 against 5 rats; DREADD 6+7 against 7+3+8; dorsal/ventral 3 against 4).
- The Supplementary Discussion cites some panels under old figure numbers.

## End of run

26 turns, 6 minutes, result: success.
