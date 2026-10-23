# 001261 · claims · run 39791664985

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/001261 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '60,400p'
```

```
finding.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '25,60p'; cat claims/001453/*.yaml | head -200
```

```
Write `claims/<folder>/<doi with / replaced by ->.yaml`. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p claims/001453/*.yaml; wc -c paper/*; head -60 paper/10.1002-cne.70001.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*; head -40 paper/10.1002-cne.70001.txt; grep -n "^checks\|^  [a-z_]*:" claims/001453/*.yaml | head; tail -60 claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I'll read the paper text in full now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1002-cne.70001.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1002-cne.70001.txt').read()
print(t[51500:80000])"
```

```
± 0.43 ms, p < 0.01), especially evident in the average phase plots (Figures 7B and S7‐1B ). In all, 15 of the 18 electrophysiological features were insignificantly different between macaque and mouse (Figures 7D and S7‐1A,C ). As before, we used dimensionality reduction with PCA to investigate how distinct the two groups were from each other. The resulting 2D UMAP plot is given in Figure 7C . It exhibits a strong separation between groups. 3.4 Morphology of BLA‐Projecting NBM/SI Cholinergic Neurons: Mouse Versus Macaque Next, we compared the morphological features of the proximal neuritic arbor of BLA‐projecting NBM/SI cholinergic neurons in macaque to those in mouse. Reconstructions of all relocalized macaque cholinergic neurons are shown in Figure 8 , with the neurons arrayed along the rostral–caudal axis. As in the mouse, the proximal arbors of macaque BLA‐projecting cholinergic neurons were morphologically diverse, with all neurons appearing to be multipolar and relatively simple. FIGURE 8 Skeletonized renditions of relocalized BLA‐projecting cholinergic neurons within NBM/SI along bregma in macaque. The proximal 100 + µm of the processes emanating from cholinergic somata of macaque were morphologically diverse regardless of location along bregma. Most neurons were multipolar, yet fairly simple ( n = 52). We measured 13 morphological features from macaque neurons (Figures 9D and S9‐1B ) and compared these to the same measurements from mouse neurons. Although many morphological features were similar (Figure S9‐1A ), five of the 13 measured parameters exhibited significant differences. Most notably, those related to convex hull were different (convex hull volume: macaque 2.19 ± 1.63 × 10 3 µm 3 , mouse 0.94 ± 0.77 × 10 3 µm 3 , p < 0.0001; convex hull area: macaque 1.15 ± 0.59 × 10 5 µm 2 , mouse 0.83 ± 0.45 × 10 5 µm 2 , p < 0.05; convex hull sphericity: macaque 0.65 ± 0.08, mouse 0.51 ± 0.09, p < 0.0001). Two representative images of BLA‐projecting NBM/SI choli
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1002-cne.70001.txt').read()
i=t.find('Supplement'); j=t.rfind('Zeisel')
print(t[j:])" | head -c 30000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://zenodo.org/api/records/10975327 | head -c 3000; echo; curl -sL "https://api.dandiarchive.org/api/dandisets/001261/" | head -c 2000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL "https://api.dandiarchive.org/api/dandisets/001261/versions/0.250917.2023/" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('assetsSummary'))"; git clone -q https://github.com/nsdesai/patch_clamp_analysis pca && cd pca && git checkout -q v1.0.1 && git rev-parse HEAD && find . -type f -not -path './.git/*' | head -50
```

Result: the fetched text is not kept.

**Agent**

Dandiset holds current-clamp data only (36 subjects). Now reading the analysis code (nsdesai/patch_clamp_analysis v1.0.1, 17a3265).

**Agent calls Bash**

```bash
cd $TMPDIR/pca && cat README.md && for f in basic_scripts_for_analysis/*.m; do echo "=== $f"; cat "$f"; done
```

```
# patch_clamp_analysis
Analysis software (MATLAB-based) for the Circuits, Synapses, and Molecular Signaling Section (CSMSS) at NINDS

A collection of MATLAB scripts used to analyze patch clamp neurophysiology data collected by CSMSS.
=== basic_scripts_for_analysis/afterhyperpolarization.m
function [ahpamplitude,ahplatency,ahpwidth] = ...
    afterhyperpolarization(inputData,~,Pars,startLoc,stopLoc,rheobaseIdx)
% function [ahpamplitude,ahplatency,ahpwidth] = ...
%         afterhyperpolarization(inputData,outputData,Pars,startLoc,stopLoc)
%
% calculates AHP properties
%
% INPUTS
% inputData         recorded data (mV) in an n x m matrix, where n is the
%                   number of sample points per current step
%                   (=duration * time step) and m is the number of steps
% outputData        current steps (pA) in an n x m matrix, where n is the
%                   number of sample points per step (=duration * time
%                   step) and m is the number of steps
% Pars              a structure variable that contains information about
[... 855 more lines not kept]
```

**Agent**

Code read. Now I'll check the supplement figures in the docx to see which features the paper marks shared vs different (the text doesn't list them all).

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p supp && cd supp && unzip -o -q paper/10.1002-cne.70001.supp.docx && ls -la word/media; grep -o 'r:embed="[^"]*"' word/document.xml; cat word/_rels/document.xml.rels | tr '>' '>\n' | grep image
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image4.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image10.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image11.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
grep -rl "± SD\|mean ± SD\|SEM" claims/*/*.yaml | head; grep -rh -i "tolerance" claims/*/*.yaml | grep -i "sd\|sem\|spread\|standard" | sort | uniq -c | sort -rn | head -20
```

```
claims/000009/10.1038-nature22324.yaml
claims/000016/10.1016-j.neuron.2019.09.045.yaml
claims/000037/10.1038-s41597-023-02214-y.yaml
claims/000121/10.1371-journal.pcbi.1006808.yaml
claims/000147/10.7554-elife.74478.yaml
claims/000218/10.1016-j.neuron.2019.10.012.yaml
claims/000226/10.1016-j.neuron.2017.03.045.yaml
claims/000239/10.1038-s41586-022-04478-7.yaml
claims/000350/10.1016-j.cell.2019.05.050.yaml
claims/000582/10.1126-science.1125572.yaml
      2     which tests this claim on its own data; tolerances are the paper's SEMs.
      1 # spread (plus or minus), the tolerance is that spread; otherwise 10% of the value.
      1 # Tolerances. Where the paper gives mean +- s.d. over mice, the s.d. describes the spread across
      1 # Tolerances. Where the paper gives a spread (plus or minus SEM), the tolerance is that spread;
      1 # Tolerances. Where the paper gives a mean with its SEM printed above zero, the tolerance is
      1 # Tolerances. The default is 10% of the reported value, or the reported SD for a mean. For the
      1 # - Tolerances: the paper's stated spread (SD or IQR) where it gives one, as the protocol asks;
      1 # - Tolerances. Means given with SD and n use 2 SD / sqrt(n) (the paper's spread turned into the
      1 # - Tolerances. 10% of a reported value when the paper gives no spread; the paper's s.e. when
      1 # - Tolerances for values given as mean and SEM are 1.96 times the SEM (the 95% interval of the
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "with_labels\|with_inputs\|elsewhere" docs/*.md | head -20; ls tools/; grep -n "kind" docs/protocol.md | head
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:49:  Elsewhere it may mean "some panels yes, some no". The pilot should show
docs/pilot-notes.md:584:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:596:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:674:tested claims are `with_inputs`, and the dandiset is judged on two. A link
docs/pilot-notes.md:729:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:979:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:983:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pilot-notes.md:1060:protocol to pilot-7 after checking that no claim needed the `elsewhere`
docs/pilot-notes.md:2761:only for comparison makes a claim `with_inputs`; and a notebook that streams
docs/pilot-notes.md:2848:repository of per-mouse figure values counts as data deposited elsewhere; a
docs/pilot-notes.md:3413:data on OSF and data public nowhere, which the rule that elsewhere is never
docs/pilot-notes.md:3514:no blocking reason for a claim on data elsewhere that could be tested but was
docs/pilot-notes.md:3715:masks that name pixels but bring no measurements, which `with_labels` does not
docs/pilot-notes.md:3894:spine and rotation choices are not fully consistent; whether `elsewhere`
docs/pilot-notes.md:4111:dandiset; per-slice summary data classed as `data: elsewhere`; a clock check
docs/pilot-notes.md:4310:that is a partial copy of the paper's own deposit, tested as `elsewhere`; a
docs/pilot-notes.md:4606:elsewhere; and runtime advice that was not enough to keep loading short.
docs/pilot-notes.md:5419:`methods_underspecified` because their data are public elsewhere and the paper
docs/pilot-notes.md:5501:table are neither `with_labels` nor `with_inputs`; it only implies that the
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001262/; head -60 claims/001262/*.yaml; grep -h "^[a-z_]*:" claims/*/*.yaml | sort | uniq -c; grep -h "^  [a-z_]*:" claims/*/*.yaml | sort | uniq -c | sort -rn | head -30; sed -n 1,80p tools/claims_check.py
```

```
10.1038-s41597-024-03259-3.yaml
# Claims for Heeringa (2024), Scientific Data 11, 411, on dandiset 001262.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (open access, PMC11035566), as served by Europe PMC, in
# paper/10.1038-s41597-024-03259-3.txt: Background & Summary, Methods, Data Records, Technical
# Validation, Usage Notes, Code availability, Table 1 and the figure legends. The paper is a
# Data Descriptor and has no supplement. The PDF was not needed.
#
# Code read: the software toolbox the paper links, Zenodo record 10370064
# (doi:10.5281/zenodo.10370064, the only version, published 2024-04-15), 21 MATLAB files:
# check_dataset_metadata.m (Table 1, Fig. 3, metadata.csv), check_dataset_units.m (all panels
# of Figs. 6 and 7), check_dataset_animal.m, checkAN.m (Fig. 4), makePSTH.m (Fig. 5b),
# call_extract_func.m and the analysis functions BFextract_func.m, RLFextract_func.m,
# getDrivenRatesRLF.m, PHextract_func.m, TytoView_calcVS.m, CFextract_func.m, getQ10dB.m,
# Clickextract_func.m, getFSL2bins.m, getFSLpoisson.m, SRextract_func.m, getSpikeCounts.m,
# and bandwidthBF.m, getQ10dB_withCF.m, getRasterData3.m, which no criterion uses.
# Details the code settles, used in the criteria below:
#   - Age groups (both scripts): young adult age <= 365 days, middle aged > 365 and <= 1095
[... 279 more lines not kept]
```

**Agent**

The checker normalizes hyphens, so I can quote with plain ASCII. Checking the schema fields before writing.

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
c=s['properties']['claims']['items']
print(json.dumps(c,indent=1)[:5000])
print(json.dumps(s.get('\$defs',s.get('definitions',{})),indent=1)[:4000])"
```

```
{
 "type": "object",
 "additionalProperties": false,
 "required": [
  "id",
  "statement",
  "source"
 ],
 "properties": {
  "id": {
   "description": "Stable within the file, e.g. fig2b.",
   "type": "string",
   "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
  },
  "statement": {
   "description": "The finding in one or two sentences, in words. Not a copy of the figure.",
   "type": "string",
   "minLength": 1
  },
  "source": {
[... 219 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001261/10.1002-cne.70001.yaml",
 "content": "# Claims for Luo, Jiang, Desai et al. (2024), J. Comp. Neurol. 532, e70001, on dandiset 001261.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, PMC11583843), as served by Europe PMC, in\n# paper/10.1002-cne.70001.txt: Introduction, Materials and Methods, Results, Discussion, Table 1,\n# the figure legends, and the supplement (CNE-532-e70001-s001.docx), whose legends are in the\n# text file. There is no PDF, so the main figures (Figs. 2D, 4D, 7D and 9D, which show which\n# features differ) could not be read. Four supplementary figures were read from the images in\n# paper/10.1002-cne.70001.supp.docx, to see which features they mark as different: S2-2 (AP\n# amplitude ***, CV-ISI **, sag **; AP width, upstroke and downstroke not marked), S4-1B (ten\n# morphological features, none marked), S7-1 (AP amplitude **, CV-ISI ****, sag *, AP width **,\n# upstroke ****, downstroke not marked) and S9-1B (seven morphological features, none marked).\n#\n# Code read: the analysis code the Methods link, doi:10.5281/zenodo.10975327, which is\n# github.com/nsdesai/patch_clamp_analysis tag v1.0.1, commit 17a3265d280392e73916faee31ee9cea30500c7c\n# (last modified 04/15/24). It holds 14 MATLAB functions that extract the electrophysiological\n# features from one recording's current steps (analysis_of_neurophysiology_data.m calls\n# sagpotential.m, inputresistance.m, rheobasecurrent.m, spikeproperties.m,\n# afterhyperpolarization.m, ficurve.m, spikefrequencyadaptation.m), getindices.m (groups\n# neurons by ChAT and BLA labels) and plotting helpers. It holds no code for the resting\n# potential, the statistics, PCA, UMAP, LDA or the morphology. The UMAP is Meehan's MATLAB\n# implementation (File Exchange 71902) and LDA is MATLAB fitcdiscr, both named by the Methods.\n#\n# Data the paper used. Mouse: 27 ChAT-tau-GFP mice (18 male, 9 female, 5 to 14 weeks), red\n# microbeads injected into both BLA; whole-cell current clamp in NBM/SI slices (56 slices) of 48\n# BLA-projecting cholinergic neurons (beads and GFP) and 46 BLA-projecting noncholinergic\n# neurons (beads, no GFP). Macaque: 9 rhesus macaques (7 male, 2 female, 7 to 17 years) with\n# microbeads in the BLA; 52 relocalized BLA-projecting neurons confirmed cholinergic by ChAT\n# immunostaining, of which 46 (from 38 slices) passed quality control, and 11 BLA-projecting\n# noncholinergic neurons. Protocol in both species: 500 ms current steps from -60 to +200 pA in\n# 10 pA increments (Fig. S2-1 legend), at least 10 s apart, from a baseline held at -65 mV by\n# a small bias current, sampled at 10 kHz, filtered at 4 kHz; junction potential (-14 mV) not\n# corrected. Quality control (Methods 2.4): access resistance < 25 MOhm and stable within 20%,\n# offset current within 10% of its initial value, resting potential <= -40 mV. Morphology:\n# neurobiotin fills reconstructed in Imaris from confocal stacks, 13 features and Sholl\n# intersections every 10 um; 31 mouse cholinergic, 44 mouse noncholinergic, 52 macaque\n# cholinergic neurons. The combined analysis (Fig. 10) uses the 46 macaque and 27 mouse\n# cholinergic neurons with both. The dandiset's description says it holds \"the physiology data\n# for the paper\"; whether it holds the morphology and the per-neuron labels (species, ChAT,\n# beads, quality control) is for the author to find. All claims use the paper's own recordings\n# (data: dataset).\n#\n# Feature definitions (F1 to F18), from Methods 2.5, the Fig. S2-1 legend and the code. Common\n# to all, from the code: the first 500 ms of each step is analysed; a spike is a peak found by\n# MATLAB findpeaks with height >= 0 mV, prominence >= 30 mV, width <= 5 ms and >= 5 ms from the\n# previous peak; firing rate is spikes / 0.5 s.\n#   F1 resting membrane potential. Methods, \"measured in the absence of a current injection\".\n#      The code does not compute it (its baselineVm is the potential before the step, at the\n#      held -65 mV). Open; readings (a) a value stored with each recording (potential with no\n#      bias current), (b) the potential of a recorded sweep with no bias and no step current.\n#      If the dataset holds neither, F1 cannot be computed.\n#   F2 sag, -60 pA step (Methods). Code, which settles how: trace median-filtered over 20 ms;\n#      sag = maximum over the second half of the step minus minimum over the first half,\n#      floored at 0; if the -60 pA response saturates, the next step up.\n#   F3 input resistance. Methods, from the response to the -20 pA step: steady-state deflection\n#      (mean of the last 100 ms of the step minus the mean of the 45 ms starting 50 ms before\n#      the step, the code's windows) divided by -20 pA. Variant, the code's choice: slope of the\n#      steady-state deflection against current over the steps from -50 to 0 pA, leaving out\n#      steps that reach -20 mV or deflect more than 50 mV.\n#   F4 membrane time constant. Methods, relaxation to the -20 pA step, fitted as in the code,\n#      a*exp(-t/tau) + c from 2 ms after step onset to the end of the step. Variant, the code's\n#      choice: the same fit on the most negative unsaturated step between -50 and 0 pA.\n#   F5 rheobase, the lowest positive step with at least one spike (code).\n#   F6 spike threshold, first spike of the rheobase step: the trace linearly interpolated to 10\n#      times the sampling rate, dV/dt by central differences, the first sample from 3 ms before\n#      the first peak at which dV/dt exceeds 10 mV/ms (Methods value, code procedure).\n#   F7 spike amplitude, first peak minus threshold.\n#   F8 spike width, full width at the level halfway between threshold and peak (code, the first\n#      two crossings).\n#   F9 spike latency. Methods, step onset to the threshold crossing of the first spike. Variant,\n#      the code's choice: step onset to the first peak.\n#   F10 upstroke, maximum dV/dt from 5 ms before the first peak (code) to the peak.\n#   F11 downstroke, minimum dV/dt \"on the downstroke of the first action potential\" (Methods).\n#      The code's window runs from 5 ms before the first peak to the end of the step (it takes\n#      max(peak - 20 ms, length), which is the step end), so it can include later spikes.\n#      Readings (a) from the first peak to 20 ms after it, (b) the code as written.\n#   F12 AHP amplitude. Methods, rheobase step (the Fig. S2-1 legend says all spike parameters\n#      are assayed at rheobase): threshold minus the minimum potential in the 100 ms after the\n#      threshold crossing of the first spike. Variant, the code's choice: on the first step at or\n#      above rheobase with two or more spikes, threshold of its first spike (no interpolation)\n#      minus the minimum between 0.75 ms before the first peak and 0.75 ms before the second.\n#   F13 AHP latency, time from the threshold crossing to the AHP minimum of F12 (Methods).\n#      Variant, the code's: from 0.75 ms before the first peak.\n#   F14 AHP width, time the potential stays below threshold minus half the AHP amplitude (the\n#      code's level), between its first two crossings; if it does not recross, to the end of\n#      the step (code). Window as in F12 (Methods), the code's as a variant.\n#   F15 f-I slope, least-squares line of firing rate against current, from the last step without\n#      spikes below rheobase to the step with the most spikes (code; Methods \"the initial\n#      linear section\").\n#   F16 maximum firing rate, the largest firing rate over the steps from 0 to 200 pA (Methods,\n#      code). Variant, the Fig. S2-1 legend: the rate on the 200 pA step.\n#   F17 adaptation index, spikes in the second half of the step over spikes in the first half\n#      (Methods, code; NaN with no spike in the first half). Which step is open: Methods \"the\n#      maximal current step\"; the code uses the step with the most spikes (the first if tied).\n#      Readings (a) the 200 pA step, (b) the step with the most spikes.\n#   F18 CV of interspike intervals, SD (n - 1) over mean of the intervals on the step of F17\n#      (both readings); 0 with fewer than 3 spikes (code). The released code stores the intervals\n#      in a square matrix (zeros(n-1)), which makes its CV not a scalar for 3 or more spikes, so\n#      the Methods' definition is used.\n#   Morphological features M1 to M13 and the Sholl counts are the Imaris and TREES measures of\n#   Methods 2.7, as stored with the data; none is recomputed here.\n#\n# Groups. Cholinergic (C): bead-labelled and GFP-positive (mouse) or ChAT-immunopositive\n# (macaque); noncholinergic (NC): bead-labelled and GFP-negative (mouse). The code's\n# getindices.m counts bead-labelled neurons of unknown ChAT status as noncholinergic; this is a\n# reading of NC where the dataset holds such neurons. Only neurons passing quality control.\n#\n# Statistics (S), Methods 2.8: each feature compared between two groups by a Wilcoxon rank-sum\n# test (MATLAB ranksum, two-sided by default), significant at p < 0.05, with no correction for\n# multiple comparisons. Averages are mean +- SD.\n#\n# UMAP procedure (U), Methods 2.8: features z-scored over all neurons in the comparison; PCA;\n# components explaining more than 1% of the variance kept; mapped to two UMAP dimensions with\n# Meehan's run_umap. Its parameters are not given; the package defaults are a standard choice.\n# UMAP is random: 10 seeds (a standard choice), the median result reported with the range.\n# Missing feature values are not addressed (open); readings (a) neurons with any missing value\n# dropped (MATLAB pca's default, 'Rows','complete'), (b) a missing value set to the feature\n# mean (0 after z-scoring). Separation in a UMAP plot is not measured in the paper; the Results\n# speak of neurons \"on the wrong side of the boundary\" (Fig. 2C). The measure is the number of\n# neurons misclassified by a linear boundary fitted in the two UMAP dimensions (fitcdiscr,\n# resubstitution), and its comparison with the same measure after permuting the group labels\n# (1000 permutations, a standard choice).\n#\n# LDA procedure (L): MATLAB fitcdiscr with its defaults (linear, pooled covariance) on all the\n# features of the comparison, missing values as in U. Whether the features are z-scored first\n# is not stated; readings z-scored (as in U) and raw. Separation is the resubstitution accuracy\n# (the paper plots the fitted neurons). The shuffled control is \"when feature values were\n# randomly shuffled\" (Results 3.2); readings (i) group labels permuted, (ii) each feature's\n# values permuted independently across neurons; 1000 shuffles. The \"absolute values of the\n# weighted differences\" (Figs. 5B, 5D, 10C) are open; readings (a) the absolute LDA coefficient\n# of each z-scored feature, (b) the absolute product of that coefficient and the difference of\n# the group means of the z-scored feature.\n#\n# Tolerances. Reported means and SDs are given as mean +- SD over neurons. The SD is the spread\n# of the neurons, not the uncertainty of the mean, and the dataset should hold the same neurons,\n# so the tolerance of a mean or SD is 10% of its absolute value (the protocol's default), not the\n# SD. Counts of features use 10% of the count.\n#\n# Not claimed: the injection sites (Figs. S1-1, S6-2), the bregma positions of the neurons (89%\n# between -0.46 and -0.94 mm in mouse), the reconstructions (Figs. 3, 8, S3-1, S9-2, S9-3), the\n# average phase plots (Figs. 2B, 7B), and the comparison with published firing rates in the\n# Discussion.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001261\"\npaper: doi:10.1002/cne.70001\nclaims:\n- id: sample-sizes\n  statement: >-\n    Electrophysiology was analysed for 48 BLA-projecting cholinergic and 46 BLA-projecting\n    noncholinergic NBM/SI neurons from 27 mice (56 slices) and 46 BLA-projecting cholinergic\n    neurons from nine macaques (38 slices); morphology for 31 mouse cholinergic and 44 mouse\n    noncholinergic neurons.\n  source: Discussion, paragraph 1; Table 1; Results 3.1, paragraph after Figure 1; Results 3.3,\n    paragraph 3\n  quote: >-\n    In total, we obtained complete analyses of 94 BLA-projecting neurons (48 cholinergic and 46\n    noncholinergic for electrophysiology; 31 cholinergic and 44 noncholinergic for morphology)\n    from 27 mice (56 slices) and 46 BLA-projecting cholinergic neurons from nine macaques (38\n    slices)\n  expected:\n  - quantity: mouse cholinergic neurons with electrophysiology\n    value: 48\n    tolerance: 0\n  - quantity: mouse noncholinergic neurons with electrophysiology\n    value: 46\n    tolerance: 0\n  - quantity: macaque cholinergic neurons with electrophysiology\n    value: 46\n    tolerance: 0\n  - quantity: mice\n    value: 27\n    tolerance: 0\n  - quantity: macaques\n    value: 9\n    tolerance: 0\n  criterion: >-\n    Counts of neurons by species and group (Groups, opening comment) and of subjects. Counts\n    are exact, as the dataset should hold the paper's neurons. For NC, both readings of the\n    group (ChAT-negative only; with ChAT-unknown neurons added, as getindices.m does) are\n    counted. Slices and sexes (mouse 18 male, 9 female; macaque 7 male, 2 female, Table 1) are\n    reported where the dataset holds them.\n- id: fig2-mouse-c-nc-15-of-18\n  statement: >-\n    In mouse, BLA-projecting cholinergic and noncholinergic NBM/SI neurons differ in 15 of the\n    18 electrophysiological features; spike width, upstroke and downstroke do not differ.\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D; Figure S2-2C\n  quote: >-\n    Cholinergic and noncholinergic BLA-projecting neurons within the region of the NBM/SI\n    differed electrophysiologically in all but three features\n  statistics:\n  - test: Wilcoxon rank-sum, per feature\n    p: 0.05\n    p_relation: \"<\"\n    n: 48 cholinergic and 46 noncholinergic neurons\n  expected:\n  - quantity: features differing at p < 0.05\n    value: 15\n    tolerance: 1.5\n  criterion: >-\n    F1 to F18 (opening comment), every reading and variant computed; S per feature. Reproduced\n    when, under one set of readings, 14 to 16 features differ. The paper's shared three (Fig.\n    S2-2C, AP width, upstroke and downstroke) are reported with their p-values. F1 is counted\n    only if it can be computed; if not, the count is out of 17 and the range becomes 13 to 15\n    (the paper reports F1 as different).\n- id: fig2d-mouse-max-firing-rate\n  statement: >-\n    Mouse noncholinergic BLA-projecting neurons are more excitable than cholinergic ones, with a\n    maximum firing rate about six times larger (39.0 +- 24.9 against 7.3 +- 4.3 Hz).\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D\n  quote: >-\n    Overall, noncholinergic neurons were much more excitable than cholinergic ones, with a\n    maximum firing rate almost six times larger (cholinergic 7.3 ± 4.3 Hz, noncholinergic 39.0\n    ± 24.9 Hz, p < 0.0001)\n  statistics:\n  - test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 48 cholinergic and 46 noncholinergic neurons\n  expected:\n  - quantity: maximum firing rate, cholinergic, mean\n    value: 7.3\n    tolerance: 0.73\n    unit: Hz\n  - quantity: maximum firing rate, cholinergic, SD\n    value: 4.3\n    tolerance: 0.43\n    unit: Hz\n  - quantity: maximum firing rate, noncholinergic, mean\n    value: 39.0\n    tolerance: 3.9\n    unit: Hz\n  - quantity: maximum firing rate, noncholinergic, SD\n    value: 24.9\n    tolerance: 2.49\n    unit: Hz\n  criterion: >-\n    F16 (Methods and code), S. Reproduced when the rank-sum p < 0.0001 with NC higher and the\n    means are within tolerance. Partially reproduced when the test holds and a mean is outside\n    tolerance. The 200 pA reading (Fig. S2-1 legend) is shown as a variant.\n- id: fig2d-mouse-threshold-rheobase\n  statement: >-\n    Mouse cholinergic BLA-projecting neurons have a more depolarized spike threshold (-33 +-\n    4.6 against -37.1 +- 6.3 mV) and a larger rheobase (64.3 +- 41.2 against 42.2 +- 33.2 pA)\n    than noncholinergic ones.\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D\n  quote: >-\n    spike threshold: cholinergic -33 ± 4.6 mV, noncholinergic -37.1 ± 6.3 mV, p < 0.001;\n    rheobase current: cholinergic 64.3 ± 41.2 pA, noncholinergic 42.2 ± 33.2 pA, p < 0.001\n  statistics:\n  - about: spike threshold\n    test: Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 48 cholinergic and 46 noncholinergic neurons\n  - about: rheobase\n    test: Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 48 cholinergic and 46 noncholinergic neurons\n  expected:\n  - quantity: spike threshold, cholinergic, mean\n    value: -33.0\n    tolerance: 3.3\n    unit: mV\n  - quantity: spike threshold, noncholinergic, mean\n    value: -37.1\n    tolerance: 3.71\n    unit: mV\n  - quantity: rheobase, cholinergic, mean\n    value: 64.3\n    tolerance: 6.43\n    unit: pA\n  - quantity: rheobase, noncholinergic, mean\n    value: 42.2\n    tolerance: 4.22\n    unit: pA\n  criterion: >-\n    F6 and F5, S. Reproduced when both tests give p < 0.001 in the reported direction and the\n    four means are within tolerance; partially reproduced when one feature holds. The SDs\n    (4.6, 6.3, 41.2, 33.2) are reported against the paper's.\n- id: fig2d-mouse-ahp\n  statement: >-\n    Mouse cholinergic BLA-projecting neurons have a larger AHP (28.9 +- 8.3 against 12.4 +- 6.1\n    mV) and a wider AHP (177.9 +- 89.3 against 85.0 +- 118.6 ms) than noncholinergic ones.\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D\n  quote: >-\n    AHP amplitude: cholinergic 28.9 ± 8.3, noncholinergic 12.4 ± 6.1 mV, p < 0.0001; AHP\n    width: cholinergic 177.9 ± 89.3 ms, noncholinergic 85.0 ± 118.6 ms, p < 0.0001\n  statistics:\n  - about: AHP amplitude\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  - about: AHP width\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: AHP amplitude, cholinergic, mean\n    value: 28.9\n    tolerance: 2.89\n    unit: mV\n  - quantity: AHP amplitude, noncholinergic, mean\n    value: 12.4\n    tolerance: 1.24\n    unit: mV\n  - quantity: AHP width, cholinergic, mean\n    value: 177.9\n    tolerance: 17.79\n    unit: ms\n  - quantity: AHP width, noncholinergic, mean\n    value: 85.0\n    tolerance: 8.5\n    unit: ms\n  criterion: >-\n    F12 and F14 with the Methods' window (rheobase step, 100 ms after threshold), S. Reproduced\n    when both tests give p < 0.0001 with cholinergic larger and the four means are within\n    tolerance; partially reproduced when the tests hold and a mean is outside tolerance. The\n    code's window (first step with two spikes) is shown as a variant.\n- id: fig2d-mouse-adaptation\n  statement: >-\n    Mouse cholinergic BLA-projecting neurons have a higher adaptation index than noncholinergic\n    ones (0.83 +- 0.56 against 0.64 +- 0.29).\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D\n  quote: >-\n    with concomitant effects on spike frequency adaptation (adaptation index: cholinergic 0.83\n    ± 0.56, noncholinergic 0.64 ± 0.29, p < 0.05)\n  statistics:\n  - test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: adaptation index, cholinergic, mean\n    value: 0.83\n    tolerance: 0.083\n  - quantity: adaptation index, noncholinergic, mean\n    value: 0.64\n    tolerance: 0.064\n  criterion: >-\n    F17 under both readings of the step (200 pA; the step with the most spikes), S. Reproduced\n    when, under one reading, p < 0.05 with cholinergic higher and both means are within\n    tolerance; partially reproduced when the test holds under a reading and no reading puts\n    both means within tolerance.\n- id: fig2d-mouse-passive\n  statement: >-\n    Mouse cholinergic BLA-projecting neurons have a more depolarized resting potential (-54.4\n    +- 8.4 against -58.7 +- 8.2 mV) and a longer membrane time constant (34.6 +- 14.3 against\n    22.3 +- 9.8 ms) than noncholinergic ones.\n  source: Results 3.1, paragraph after the Figure 2 legend; Figure 2D\n  quote: >-\n    Passive electrophysiological properties, such as resting membrane potential (cholinergic\n    -54.4 ± 8.4 mV, noncholinergic -58.7 ± 8.2 mV, p < 0.05) and membrane time constant tau\n    (cholinergic 34.6 ± 14.3, noncholinergic 22.3 ± 9.8 ms, p < 0.0001), also exhibited\n    significant differences\n  statistics:\n  - about: resting membrane potential\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n  - about: membrane time constant\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: resting membrane potential, cholinergic, mean\n    value: -54.4\n    tolerance: 5.44\n    unit: mV\n  - quantity: resting membrane potential, noncholinergic, mean\n    value: -58.7\n    tolerance: 5.87\n    unit: mV\n  - quantity: membrane time constant, cholinergic, mean\n    value: 34.6\n    tolerance: 3.46\n    unit: ms\n  - quantity: membrane time constant, noncholinergic, mean\n    value: 22.3\n    tolerance: 2.23\n    unit: ms\n  criterion: >-\n    F1 under readings (a) and (b) as the dataset allows, and F4 on the -20 pA step (Methods),\n    S. Each feature is judged alone; reproduced when both hold (test at the reported level in\n    the reported direction, means within tolerance), partially reproduced when one does. If F1\n    cannot be computed, the claim is judged on tau and F1 is reported as untestable. The code's\n    step for tau is shown as a variant.\n- id: figs2-2-mouse-amplitude-cv-sag\n  statement: >-\n    In mouse, spike amplitude, the CV of interspike intervals and sag also differ between\n    cholinergic and noncholinergic BLA-projecting neurons, with cholinergic neurons having\n    larger spikes, a lower CV and a smaller sag.\n  source: Figure S2-2A\n  quote: >-\n    Additional electrophysiological features that distinguish BLA-projecting, cholinergic from\n    noncholinergic neurons and features that are shared in mouse NBM/SI\n  statistics:\n  - about: spike amplitude (***)\n    test: Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n  - about: CV of interspike intervals (**)\n    test: Wilcoxon rank-sum\n    p: 0.01\n    p_relation: \"<\"\n  - about: sag (**)\n    test: Wilcoxon rank-sum\n    p: 0.01\n    p_relation: \"<\"\n  criterion: >-\n    F7, F18 (both step readings) and F2, S. The figure marks the bounds as p <= 0.001, 0.01 and\n    0.01; directions are read from the figure's box plots. Reproduced when each feature differs\n    at its figure level in the stated direction (F18 under one reading); partially reproduced\n    when one or two do.\n- id: fig2c-mouse-umap-separation\n  statement: >-\n    A UMAP of the 18 electrophysiological features separates mouse cholinergic from\n    noncholinergic BLA-projecting neurons almost completely, with only two neurons on the wrong\n    side of the boundary.\n  source: Results 3.1, last paragraph; Figure 2C\n  quote: >-\n    shows almost complete separation between the BLA-projecting cholinergic and noncholinergic\n    neurons within the NBM/SI; only two neurons fall on the \"wrong\" side of the boundary\n  expected:\n  - quantity: neurons on the wrong side of the boundary\n    value: 2\n    tolerance: 0\n  criterion: >-\n    U on F1 to F18 (the readings of F set by fig2-mouse-c-nc-15-of-18, the Methods' choices\n    first) of the 48 C and 46 NC neurons. The boundary is open (opening comment, U); the\n    measure is the number misclassified by a linear boundary in the two UMAP dimensions.\n    Reproduced when, under one reading of missing values, the median over seeds is at most 2\n    and the separation beats every label permutation. The count is reported either way.\n  depends_on:\n  - fig2-mouse-c-nc-15-of-18\n- id: fig4d-mouse-morphology-3-of-13\n  statement: >-\n    Mouse cholinergic and noncholinergic BLA-projecting neurons differ in 3 of 13 morphological\n    features; cholinergic neurons have more branch points (8.1 +- 5.4 against 6.6 +- 5.4), a\n    smaller total process area (4.6 +- 2.7 against 6.6 +- 3.6 x 10^3 um^2) and a smaller\n    centripetal bias (12.9 +- 14.9 against 15.2 +- 10.1).\n  source: Results 3.2, paragraph after the Figure 4 legend; Figure 4D; Figure S4-1B\n  quote: >-\n    Three of the 13 features assayed were statistically significantly different ... cholinergic\n    neurons had more branch points (cholinergic 8.1 ± 5.4, noncholinergic 6.6 ± 5.4, p < 0.05),\n    a smaller total proximal process area ... and a smaller centripetal bias (cholinergic 12.9\n    ± 14.9, noncholinergic 15.2 ± 10.1, p < 0.05)\n  statistics:\n  - about: number of branch points\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n    n: 31 cholinergic and 44 noncholinergic neurons\n  - about: total process area\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n    n: 31 cholinergic and 44 noncholinergic neurons\n  - about: centripetal bias\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n    n: 31 cholinergic and 44 noncholinergic neurons\n  expected:\n  - quantity: morphological features differing at p < 0.05\n    value: 3\n    tolerance: 0\n  - quantity: branch points, cholinergic, mean\n    value: 8.1\n    tolerance: 0.81\n  - quantity: branch points, noncholinergic, mean\n    value: 6.6\n    tolerance: 0.66\n  - quantity: total process area, cholinergic, mean\n    value: 4600\n    tolerance: 460\n    unit: um^2\n  - quantity: total process area, noncholinergic, mean\n    value: 6600\n    tolerance: 660\n    unit: um^2\n  - quantity: centripetal bias, cholinergic, mean\n    value: 12.9\n    tolerance: 1.29\n  - quantity: centripetal bias, noncholinergic, mean\n    value: 15.2\n    tolerance: 1.52\n  criterion: >-\n    The 13 stored morphological features (Methods 2.7), S. Reproduced when exactly these three\n    differ at p < 0.05 and the six means are within tolerance. Partially reproduced when the\n    three differ and other features also differ, or a mean is outside tolerance. The count\n    tolerance is 0 because 10% of 3 is under one feature. The paper's text says the cholinergic\n    centripetal bias is \"smaller\" though its mean branch-point SDs are equal; directions are\n    judged by the means as printed.\n- id: figs4-1a-mouse-sholl-not-different\n  statement: >-\n    Sholl intersections as a function of distance from the soma do not differ between mouse\n    cholinergic and noncholinergic BLA-projecting neurons.\n  source: Results 3.2, paragraph after the Figure 4 legend; Figure S4-1A\n  quote: >-\n    On a standard Sholl analysis of intersections as a function of distance from the soma,\n    cholinergic and noncholinergic neurons were also not significantly different\n  criterion: >-\n    A claim of absence. The paper names no test for the Sholl curves; its only named test is\n    the Wilcoxon rank-sum at p < 0.05 (Methods 2.8). Readings (a) a rank-sum at each 10 um\n    radius from 10 to 200 um (the range of Fig. S4-1A), uncorrected, absence when no radius has\n    p < 0.05; (b) a rank-sum on each neuron's total intersections over those radii. Reproduced\n    when both find no difference, not reproduced when both find one, blocked as\n    methods_underspecified when they disagree. The differences at each radius are reported.\n- id: fig4c-mouse-morphology-umap-similar\n  statement: >-\n    A UMAP of the morphological features does not separate mouse cholinergic from\n    noncholinergic BLA-projecting neurons.\n  source: Results 3.2, paragraph after the Figure 4 legend; Figure 4C\n  quote: >-\n    Dimensionality reduction via PCA and subsequent display via UMAP likewise indicated that\n    proximal neuritic morphology was similar between the two types of mouse BLA-projecting\n    neurons\n  criterion: >-\n    U on the 13 morphological features of the 31 C and 44 NC neurons. The paper gives no test;\n    the measure of U is used. Reproduced when, under each reading of missing values, the\n    separation of the true labels is not better than that of 95% of the label permutations (p\n    >= 0.05); not reproduced when it is, under both. The misclassified count is reported.\n- id: fig5a-mouse-lda-electrophysiology\n  statement: >-\n    A linear discriminant analysis of the electrophysiological features clearly separates mouse\n    cholinergic from noncholinergic BLA-projecting neurons.\n  source: Results 3.2, paragraph before the Figure 5 legend; Figure 5A\n  quote: >-\n    Given the clean separation between these groups on the unsupervised electrophysiological\n    UMAP plot ... supervised LDA revealed a clear separation\n  criterion: >-\n    L on F1 to F18 of the 48 C and 46 NC neurons. Reproduced when the resubstitution accuracy\n    exceeds that of 95% of the shuffles under both shuffle readings, for both scalings.\n    The Fig. 5A legend says the populations separate \"but not from the distribution of\n    shuffled data\", which contradicts the Results and the Fig. 5C legend; the Results are\n    followed. The accuracy, and a 10-fold cross-validated accuracy as a variant, are reported.\n  depends_on:\n  - fig2-mouse-c-nc-15-of-18\n- id: fig5b-mouse-lda-ahp-amplitude-top\n  statement: >-\n    AHP amplitude has the highest weight in the LDA separating mouse cholinergic from\n    noncholinergic BLA-projecting neurons.\n  source: Results 3.2, paragraph before the Figure 5 legend; Figure 5B\n  quote: The feature with the highest weight in the LDA vector was AHP amplitude\n  criterion: >-\n    L on F1 to F18 as in fig5a-mouse-lda-electrophysiology, z-scored. Reproduced when AHP\n    amplitude ranks first under both readings of the weights (a) and (b); not reproduced when\n    it ranks first under neither; methods_underspecified when they disagree. The top five\n    under each reading are reported.\n  depends_on:\n  - fig5a-mouse-lda-electrophysiology\n- id: fig5c-mouse-lda-morphology-fails\n  statement: >-\n    An LDA of the morphological features fails to separate mouse cholinergic from\n    noncholinergic BLA-projecting neurons; the result is like that of shuffled features.\n  source: Results 3.2, paragraph before the Figure 5 legend; Figure 5C\n  quote: >-\n    By contrast, even supervised LDA failed to separate cholinergic and noncholinergic neurons\n    morphologically ... Indeed, the distribution was equivalent to the LDA plots that resulted\n    when feature values were randomly shuffled\n  criterion: >-\n    L on the 13 morphological features of the 31 C and 44 NC neurons. Reproduced when the\n    resubstitution accuracy is not above that of 95% of the shuffles (p >= 0.05) under both\n    shuffle readings; not reproduced when it is under both; methods_underspecified when they\n    disagree.\n- id: fig7d-macaque-more-excitable\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons are more excitable than mouse ones, with a\n    maximum firing rate three times larger (26.3 +- 23.1 against 7.3 +- 4.3 Hz), a rheobase a\n    third as large (23.3 +- 16.5 against 64.3 +- 41.2 pA) and an f-I slope twice as large (0.13\n    +- 0.10 against 0.06 +- 0.03 Hz/pA).\n  source: Results 3.3, paragraph after the Figure 7 legend; Figure 7D\n  quote: >-\n    The maximum firing rate was three times larger (macaque 26.3 ± 23.1 Hz, mouse 7.3 ± 4.3 Hz,\n    p < 0.0001), the rheobase current was only a third as large (macaque 23.3 ± 16.5 pA, mouse\n    64.3 ± 41.2 pA, p < 0.0001), and the slope of the f - I curve was twice as large (macaque\n    0.13 ± 0.10, mouse 0.06 ± 0.03, p < 0.0001)\n  statistics:\n  - about: maximum firing rate\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 macaque and 48 mouse cholinergic neurons\n  - about: rheobase\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 macaque and 48 mouse cholinergic neurons\n  - about: f-I slope\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 macaque and 48 mouse cholinergic neurons\n  expected:\n  - quantity: maximum firing rate, macaque, mean\n    value: 26.3\n    tolerance: 2.63\n    unit: Hz\n  - quantity: rheobase, macaque, mean\n    value: 23.3\n    tolerance: 2.33\n    unit: pA\n  - quantity: f-I slope, macaque, mean\n    value: 0.13\n    tolerance: 0.013\n    unit: Hz/pA\n  - quantity: f-I slope, mouse, mean\n    value: 0.06\n    tolerance: 0.006\n    unit: Hz/pA\n  criterion: >-\n    F16, F5 and F15, S, macaque C against mouse C. The mouse means of firing rate and rheobase\n    are those of fig2d-mouse-max-firing-rate and fig2d-mouse-threshold-rheobase. Reproduced\n    when all three tests give p < 0.0001 in the reported direction and the means are within\n    tolerance; partially reproduced when the tests hold and a mean is outside tolerance, or\n    when two of the three tests hold.\n- id: fig7d-macaque-threshold-ahp\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons have a more hyperpolarized spike threshold\n    (-39.7 +- 5.9 against -33.0 +- 4.6 mV), a smaller AHP (19.1 +- 8.8 against 28.9 +- 8.3 mV)\n    and a narrower AHP (106.6 +- 71.9 against 177.9 +- 89.3 ms) than mouse ones.\n  source: Results 3.3, paragraph after the Figure 7 legend; Figure 7D\n  quote: >-\n    spike threshold: macaque -39.7 ± 5.9 mV, mouse -33.0 ± 4.6 mV, p < 0.0001) and in\n    afterhyperpolarization properties (AHP amplitude: macaque 19.1 ± 8.8 mV, mouse 28.9 ± 8.3\n    mV, p < 0.0001; AHP width: macaque 106.6 ± 71.9 ms, mouse 177.9 ± 89.3 ms, p < 0.0001)\n  statistics:\n  - about: spike threshold\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  - about: AHP amplitude\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  - about: AHP width\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: spike threshold, macaque, mean\n    value: -39.7\n    tolerance: 3.97\n    unit: mV\n  - quantity: AHP amplitude, macaque, mean\n    value: 19.1\n    tolerance: 1.91\n    unit: mV\n  - quantity: AHP width, macaque, mean\n    value: 106.6\n    tolerance: 10.66\n    unit: ms\n  criterion: >-\n    F6, F12 and F14 (Methods' window; the code's as a variant), S, macaque C against mouse C.\n    Reproduced when all three tests give p < 0.0001 in the reported direction and the macaque\n    means are within tolerance; partially reproduced when the tests hold and a mean is outside\n    tolerance, or when two of the three tests hold.\n- id: fig7-macaque-spike-width\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons have wider spikes than mouse ones (1.32 +- 0.45\n    against 1.15 +- 0.43 ms).\n  source: Results 3.3, paragraph after the Figure 7 legend; Figure S7-1C\n  quote: >-\n    Macaque neurons also differed from mouse neurons in basic spike shape (spike width: macaque\n    1.32 ± 0.45 ms, mouse 1.15 ± 0.43 ms, p < 0.01)\n  statistics:\n  - test: Wilcoxon rank-sum\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: spike width, macaque, mean\n    value: 1.32\n    tolerance: 0.132\n    unit: ms\n  - quantity: spike width, mouse, mean\n    value: 1.15\n    tolerance: 0.115\n    unit: ms\n  criterion: >-\n    F8, S. Reproduced when p < 0.01 with macaque wider and both means within tolerance;\n    partially reproduced when the test holds and a mean is outside tolerance.\n- id: figs7-1-macaque-amplitude-cv-sag-upstroke\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons also differ from mouse ones in spike amplitude,\n    CV of interspike intervals, sag and upstroke, each larger in macaque, while the downstroke\n    does not differ.\n  source: Figure S7-1A and C\n  quote: >-\n    Population scatter plus box plots of additional features that differ in the action\n    potential time course of BLA-projecting, NBM/SI cholinergic neurons from macaque ...\n    Population scatter plus box plots showing features of AP width and Upstroke are distinct,\n    but feature of downstroke is shared\n  statistics:\n  - about: spike amplitude (**)\n    test: Wilcoxon rank-sum\n    p: 0.01\n    p_relation: \"<\"\n  - about: CV of interspike intervals (****)\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  - about: sag (*)\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n  - about: upstroke (****)\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: >-\n    F7, F18 (both step readings), F2, F10 and F11 (both readings), S, macaque C against mouse C.\n    The figure marks the bounds as p <= 0.01, 0.0001, 0.05 and 0.0001; directions are read from\n    its box plots. The four differences are reproduced when each holds at its figure level in\n    the stated direction (F18 under one reading); partially reproduced when two or three do.\n    The shared downstroke is a claim of absence on the rank-sum at p < 0.05, judged under both\n    F11 readings (methods_underspecified if they disagree); a downstroke difference makes the\n    claim at most partially reproduced.\n- id: fig7-macaque-mouse-feature-count\n  statement: >-\n    Most of the 18 electrophysiological features differ between macaque and mouse\n    BLA-projecting cholinergic neurons; the text gives the number as 15 of 18, and the figures\n    mark 17 as different.\n  source: Results 3.3, paragraph after the Figure 7 legend; Figure 7D legend; Figure S7-1\n  quote: >-\n    In all, 15 of the 18 electrophysiological features were insignificantly different between\n    macaque and mouse\n  statistics:\n  - test: Wilcoxon rank-sum, per feature\n    p: 0.05\n    p_relation: \"<\"\n    n: 46 macaque and 48 mouse cholinergic neurons\n  criterion: >-\n    The sentence as printed (15 not different, so 3 different) is contradicted by the same\n    paragraph, which reports 7 features that differ; it is read as a slip. Readings of the\n    count of differing features (a) 15, the sentence with \"insignificantly\" read as\n    \"significantly\"; (b) 17, from the legends (12 features \"that distinguish\" in Fig. 7D, 3 in\n    Fig. S7-1A, AP width and upstroke in Fig. S7-1C; downstroke shared). F1 to F18 as in\n    fig2-mouse-c-nc-15-of-18, S. Reproduced when the count is within 10% of either reading (14\n    to 16, or 16 to 18 capped at 18); not reproduced below 14. Fig. 7D itself could not be read\n    (no PDF), so which 12 features it shows is not known; the per-feature p-values are\n    reported.\n  depends_on:\n  - fig2-mouse-c-nc-15-of-18\n- id: fig7d-macaque-input-resistance\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons have a larger input resistance and a smaller\n    rheobase than mouse ones, the opposite of what larger cells would show.\n  source: Discussion 4.2, paragraph 3; Figure 7D\n  quote: >-\n    If macaque neurons were simply larger than mouse neurons, everything else kept constant, one\n    would predict that their input resistances would be smaller and their rheobase currents\n    larger. However, in fact, the opposite is true in both cases\n  criterion: >-\n    F3 (the -20 pA step; the code's slope as a variant) and F5, S. The paper gives no values for\n    input resistance; Fig. 7D, which shows it, could not be read. Reproduced when the macaque\n    input resistance is higher at p < 0.05 and the rheobase lower at p < 0.05; partially\n    reproduced when one holds.\n- id: fig7c-macaque-mouse-umap-separation\n  statement: >-\n    A UMAP of the 18 electrophysiological features shows a strong separation between macaque\n    and mouse BLA-projecting cholinergic neurons.\n  source: Results 3.3, last paragraph; Figure 7C; Discussion 4.3, paragraph 1\n  quote: >-\n    The resulting 2D UMAP plot is given in Figure 7C . It exhibits a strong separation between\n    groups\n  criterion: >-\n    U on F1 to F18 (as in fig2-mouse-c-nc-15-of-18) of the 46 macaque and 48 mouse C neurons.\n    \"Strong\" is not quantified. Readings (a) as clean as the paper's \"almost complete\n    separation\" of Fig. 2C, at most 2 of the 94 neurons misclassified (median over seeds);\n    (b) separation better than every label permutation. Reproduced when (a) and (b) hold under\n    one reading of missing values; methods_underspecified when (b) holds and (a) does not; not\n    reproduced when (b) fails.\n  depends_on:\n  - fig2-mouse-c-nc-15-of-18\n- id: fig9-macaque-convex-hull\n  statement: >-\n    Macaque BLA-projecting cholinergic neurons have a larger convex hull than mouse ones, in\n    volume (2.19 +- 1.63 against 0.94 +- 0.77, units below), area (1.15 +- 0.59 against 0.83 +-\n    0.45 x 10^5 um^2) and sphericity (0.65 +- 0.08 against 0.51 +- 0.09).\n  source: Results 3.4, paragraph after the Figure 8 legend; Figure 9D\n  quote: >-\n    Most notably, those related to convex hull were different (convex hull volume: macaque 2.19\n    ± 1.63 × 10 3 ... convex hull sphericity: macaque 0.65 ± 0.08, mouse 0.51 ± 0.09, p <\n    0.0001)\n  statistics:\n  - about: convex hull volume\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 52 macaque and 31 mouse cholinergic neurons\n  - about: convex hull area\n    test: Wilcoxon rank-sum\n    p: 0.05\n    p_relation: \"<\"\n    n: 52 macaque and 31 mouse cholinergic neurons\n  - about: convex hull sphericity\n    test: Wilcoxon rank-sum\n    p: 0.0001\n    p_relation: \"<\"\n    n: 52 macaque and 31 mouse cholinergic neurons\n  expected:\n  - quantity: convex hull volume, macaque, mean, in the printed multiplier\n    value: 2.19\n    tolerance: 0.219\n    unit: 10^3 um^3 as printed, or 10^6 um^3 (see criterion)\n  - quantity: convex hull volume, mouse, mean, in the printed multiplier\n    value: 0.94\n    tolerance: 0.094\n    unit: 10^3 um^3 as printed, or 10^6 um^3 (see criterion)\n  - quantity: convex hull area, macaque, mean\n    value: 115000\n    tolerance: 11500\n    unit: um^2\n  - quantity: convex hull area, mouse, mean\n    value: 83000\n    tolerance: 8300\n    unit: um^2\n  - quantity: convex hull sphericity, macaque, mean\n    value: 0.65\n    tolerance: 0.065\n  - quantity: convex hull sphericity, mouse, mean\n    value: 0.51\n    tolerance: 0.051\n  criterion: >-\n    Stored convex hull volume, area and sphericity (Methods 2.7), S. The volume's unit is open:\n    the text prints x 10^3 um^3, while the axis of Fig. S4-1B (the same mouse neurons) is x\n    10^6 um^3; both readings are compared. Reproduced when the three tests hold at the reported\n    levels with macaque larger and the means are within tolerance (volume under one reading);\n    partially reproduced when the tests hold and a mean is not.\n- id: fig9-macaque-morphology-feature-count\n  statement: >-\n    Of the 13 morphological features, five (text) or six (Figure 9 legend) differ between\n    macaque and mouse BLA-projecting cholinergic neurons; the other seven are similar.\n  source: Results 3.4, paragraph after the Figure 8 legend; Figure 9 legend; Figure S9-1B\n  quote: >-\n    five of the 13 measured parameters exhibited significant differences\n  statistics:\n  - test: Wilcoxon rank-sum, per feature\n    p: 0.05\n    p_relation: \"<\"\n    n: 52 macaque and 31 mouse cholinergic neurons\n  criterion: >-\n    The 13 stored features, S. The text says five, the Figure 9 legend six (\"differ from those\n    in mouse in six of the 13 morphological parameters\"), and Fig. S9-1B shows seven not\n    marked (centripetal bias, root angle, total process area, primary and first-order process\n    numbers, total process length and its normalized form), which leaves six. Readings 5 and 6.\n    Reproduced when the count is 5 or 6 and none of the seven features of Fig. S9-1B differs;\n    partially reproduced when the count is 5 or 6 but the set differs.\n- id: fig9-macaque-fewer-branch-points\n  statement: >-\n    The proximal arbors of macaque BLA-projecting cholinergic neurons tend to have fewer branch\n    points than those of mouse.\n  source: Discussion, paragraph 2; Figure 9D\n  quote: >-\n    the soma-proximal arbors of macaque BLA-projecting NBM/SI cholinergic neurons tend to have\n    fewer branch points and occupy larger 3D space than those of mouse\n  criterion: >-\n    Stored number of branch points, S. No value or p-value is printed and Fig. 9D could not be\n    read; the claim is that it is among the differing features. Reproduced when macaque has\n    fewer branch points at p < 0.05; not reproduced otherwise. The normalized branch points\n    are reported as well.\n- id: fig9c-morphology-umap-weak\n  statement: >-\n    In a UMAP of the morphological features, macaque neurons tend to cluster away from mouse\n    neurons, but the separation is weak compared with the electrophysiological UMAP.\n  source: Results 3.4, paragraph before Figure 10; Figure 9C\n  quote: >-\n    There was a tendency for macaque neurons to cluster away from mouse neurons ... but the\n    effect of clustering based on morphology alone was weak\n  criterion: >-\n    U on the 13 morphological features of the 52 macaque and 31 mouse neurons, and on the\n    electrophysiological features as in fig7c-macaque-mouse-umap-separation. Reproduced when the\n    morphological separation is better than 95% of label permutations and its misclassified\n    fraction is larger than the electrophysiological one (same seeds, same reading of missing\n    values); partially reproduced when only the second holds.\n  depends_on:\n  - fig7c-macaque-mouse-umap-separation\n- id: fig10-combined-separation\n  statement: >-\n    Combining the 18 electrophysiological and 13 morphological features separates macaque from\n    mouse BLA-projecting cholinergic neurons, in a UMAP and clearly in an LDA, unlike shuffled\n    data.\n  source: Results 3.4, paragraph before Figure 10; Figure 10A and B\n  quote: >-\n    Examination of combined morphoelectric features distinguishes macaque versus mouse basal\n    forebrain neurons despite common projection target, anatomical location, and cholinergic\n    phenotype ... Note the clear separation in clustering of the two populations from one\n    another and its distinct nature from the distribution of shuffled data\n  criterion: >-\n    The 46 macaque and 27 mouse cholinergic neurons with both. LDA (L, both scalings): the\n    resubstitution accuracy exceeds that of 95% of the shuffles under both shuffle readings.\n    UMAP (U): separation better than every label permutation. Reproduced when both hold;\n    partially reproduced when the LDA holds and the UMAP does not.\n  depends_on:\n  - fig2-mouse-c-nc-15-of-18\n- id: fig10c-combined-lda-weights\n  statement: >-\n    The features with the highest LDA weights separating macaque from mouse are convex hull\n    (morphology) and rheobase, AHP width and maximum firing rate (physiology).\n  source: Results 3.4, paragraph before Figure 10; Figure 10C\n  quote: >-\n    The features with the highest weight in the LDA vector analysis differentiating macaque from\n    mouse were convex hull in morphology and rheobase, AHP width, and maximum firing rate in\n    physiology\n  criterion: >-\n    L as in fig10-combined-separation, z-scored. \"Convex hull\" may name any of its three\n    features. Readings of the ranking (i) the four highest weights are rheobase, AHP width,\n    maximum firing rate and one convex hull feature; (ii) the same, with the three convex hull\n    features taken together as one (their largest weight). Each under weights (a) and (b).\n    Reproduced when one ranking reading holds under both weight readings; partially reproduced\n    when it holds under one; not reproduced when under neither. The top eight weights are\n    reported.\n  depends_on:\n  - fig10-combined-separation\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001261/10.1002-cne.70001.yaml",
 "old_string": "    tolerance is 0 because 10% of 3 is under one feature. The paper's text says the cholinergic\n    centripetal bias is \"smaller\" though its mean branch-point SDs are equal; directions are\n    judged by the means as printed.",
 "new_string": "    tolerance is 0 because 10% of 3 is under one feature."
}
```

```
The file claims/001261/10.1002-cne.70001.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001261/10.1002-cne.70001.yaml paper/10.1002-cne.70001.txt; grep -n "[^ ]: [^ ]" claims/001261/10.1002-cne.70001.yaml | grep -v "^[0-9]*:#" | grep -v ">-$" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (28 claims, 28 quotes, 0 problems). Checking plain scalars for ": ", em dashes and "rather".

**Agent calls Bash**

```bash
f=claims/001261/10.1002-cne.70001.yaml; grep -nE "^\s*(- )?[a-z_]+: [^>|\"].*: " $f; grep -nE "^\s{4,}[^ #-].*: " $f | head -40 >/dev/null; grep -n "—\|rather" $f; python3 - <<'E'
import yaml
y=yaml.compose(open('claims/001261/10.1002-cne.70001.yaml').read())
def walk(n):
    if isinstance(n,yaml.ScalarNode):
        if n.style is None and ': ' in n.value: print('PLAIN',n.start_mark.line+1,n.value[:60])
    elif isinstance(n,yaml.MappingNode):
        for k,v in n.value: walk(k);walk(v)
    elif isinstance(n,yaml.SequenceNode):
        for v in n.value: walk(v)
walk(y)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
git status --short
```

```
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
?? claims/001261/
?? scripts
```

**Agent**

I wrote `claims/001261/10.1002-cne.70001.yaml`. The quote checker reports 28 claims, 28 quotes, 31 statistical values and 0 problems. Nothing is committed.

**Text read**
- **Paper:** the version of record (open access, PMC11583843, from Europe PMC), including the Methods, Table 1 and all figure legends.
- **Supplement:** the docx (CNE-532-e70001-s001). Its legends are in the text file. I opened four of its figure images (S2-2, S4-1, S7-1, S9-1) only to see which features they mark as significantly different.
- **Code:** the analysis code the Methods link (Zenodo 10.5281/zenodo.10975327), which is github.com/nsdesai/patch_clamp_analysis v1.0.1, commit 17a3265. It holds MATLAB functions that extract the electrophysiological features. It has no code for resting potential, the statistics, PCA, UMAP, LDA or morphology.
- **Dataset:** the archive description says it holds "the physiology data" (current clamp, 36 subjects).

**Claims**
- 28 claims, all with quotes, none marked `inferred`.
- 24 carry statistics, almost all Wilcoxon rank-sum bounds. For the supplementary panels the bounds come from the figure's significance stars.
- 14 carry expected values. The tolerance is 10% of each value; the opening comment explains why I did not use the SD.
- All 28 have criteria.
- They cover:
  - sample sizes;
  - mouse cholinergic vs noncholinergic electrophysiology, morphology, Sholl, UMAP and LDA (Figs 2, 4, 5, S2-2, S4-1);
  - mouse vs macaque electrophysiology, morphology and UMAP (Figs 7, 9, S7-1, S9-1);
  - the combined UMAP, LDA and LDA weights (Fig 10).

**Details left open, with the readings named**
- **Resting potential:** the code does not compute it. Readings: (a) a value stored with each recording; (b) a sweep with no bias current. If the dataset holds neither, it cannot be computed.
- **Downstroke:** the code's window runs to the end of the step, apparently by a bug. Readings: (a) from the first peak to 20 ms after it; (b) the code as written.
- **Adaptation index and CV of interspike intervals:** the Methods say "maximal current step". Readings: (a) the 200 pA step; (b) the step with the most spikes, as the code does. The released code's CV is not a scalar for 3 or more spikes, so the Methods' definition is used.
- **Noncholinergic group:** ChAT-negative only, or with ChAT-unknown neurons added (as the code's `getindices.m` does).
- **Missing values in UMAP and LDA:** drop the neuron, or use the feature mean.
- **UMAP:** its parameters and seed are not given, so I used the package defaults and 10 seeds. The paper never defines its "boundary"; I measure it with a linear boundary in the two UMAP dimensions plus a label-permutation test.
- **LDA:** z-scored or raw features. The "shuffled" control: permuted labels, or each feature permuted on its own. The "weighted differences": |coefficient|, or |coefficient × difference of group means|.
- **"Strong separation" (Fig 7C):** (a) as clean as Fig 2C (at most 2 of 94 misclassified); (b) better than every permutation.
- **Sholl test:** not named. Readings: (a) a rank-sum at each radius; (b) a rank-sum on total intersections.
- **Methods vs code:** where they disagree (input resistance and time-constant steps, spike latency, AHP window, maximum-rate step), the Methods are the main reading and the code's choice is a variant.

**Inconsistencies in the paper**
- **Feature count, macaque vs mouse:** the text says "15 of the 18 … insignificantly different", but the same paragraph reports 7 features that differ. Readings: 15 differ (the sentence read as "significantly"), or 17 (from the legends).
- **Morphology count:** the text says five of 13 features differ; the Fig 9 legend says six. Fig S9-1 is consistent with six.
- **Convex hull volume units:** the text prints ×10³ µm³, but the Fig S4-1B axis shows ×10⁶ µm³. Both are compared.
- **Fig 5A legend:** it contradicts the Results on the shuffled control. I followed the Results.

**Missing**
- There is no PDF, so the main-figure panels 2D, 4D, 7D and 9D could not be read. Which 12 features Fig 7D shows, and the input-resistance values, are therefore unknown. The claims that depend on them say so.
- The morphology and Fig 10 claims need reconstruction data, which the dataset description suggests it may not hold. Checking that is for the author.

## End of run

27 turns, 7 minutes, result: success.
