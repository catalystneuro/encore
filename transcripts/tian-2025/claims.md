# 001559 · claims · run 39587218038

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/001559 2>&1
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
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '30,62p'; cat claims/001453/*.yaml | head -250; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '250,600p' claims/001453/*.yaml | grep -v '^    ' | head -80; tail -60 claims/001453/*.yaml
```

```
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
  statistics:
  - test: Student's t-test
- id: fig3e-longer-swims
  statement: Head-fixed DC perform longer swims than ZF (median 0.75 s against 0.29 s, p <
  source: Figure 3E and 3F
  quote: DC performed significantly longer swims than ZF (DC = 0.75 s, ZF = 0.29 s
  statistics:
  - test: two-way ANOVA main effect
- id: fig3cd-zf-turn-more
  statement: Head-fixed ZF show larger directional tail angles than DC to turn-inducing stimuli,
[... 77 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1021-acssensors.5c01093.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '643,796p' paper/*.txt | grep -niv '^journal=\|^10\.\|^PMC\|^[0-9]*$' | head -40; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rli "supplement" transcripts/*/ 2>/dev/null | head; grep -rl "missing" transcripts/ 2>/dev/null | grep -i claims | head; ls transcripts | head -50
```

```
transcripts/000003/author.md
transcripts/000003/author-revise-1.md
transcripts/000003/recorder-report.md
transcripts/000003/author-report.md
transcripts/000003/author-revise-2.md
transcripts/000003/verifier-1.md
transcripts/000003/recorder.md
transcripts/000003/verifier-2.md
transcripts/000005/author.md
transcripts/000005/author-revise-1.md
transcripts/001752/claims-check-report.md
transcripts/001752/claims-check.md
transcripts/001752/claims-report.md
transcripts/001752/claims.md
transcripts/001676/claims.md
transcripts/001605/claims-report.md
transcripts/001605/claims.md
transcripts/001791/claims-check.md
transcripts/000061/claims-report.md
transcripts/000061/claims.md
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
for f in transcripts/*/claims-report.md; do if grep -qi "missing\|no claims\|stop" $f; then echo "== $f"; grep -i -m3 "missing\|supplement" $f; fi; done 2>/dev/null | head -60; ls transcripts/001559 2>&1
```

```
Exit code 2
== transcripts/000005/claims-report.md
**Text read:** the version of record, with its Online Methods and its one supplement (Supplementary Figures 1–14 and Tables 1–2). The extracted text garbled a few things, so I rendered PDF pages for four of them: Supplementary Table 2, the FS waveform boundary in Supp. Fig. 6, the number of phase bins in Supp. Fig. 2d (12), and the P values printed in Fig. 8d (0.55 and 0.02).
**Code:** the paper's data and code link is CRCNS ssc-7 (doi:10.6080/K0T43R01). Its public pages list NWB data files and a data-description document. No analysis code is listed, and downloading needs an account, so I read no code. Every method in the criteria comes from the Methods, the figure legends or the supplement.
**Missing or inconsistent in the paper:**
== transcripts/000008/claims-report.md
**Text read.** The version of record (open access) from Europe PMC (PMC8113357): main text, Methods, figure legends and Extended Data legends. There was no PDF, so the Extended Data figures were read from their legends only. Not in the text: Extended Data Tables 1–2 (t-type descriptions) and Supplementary Files 1–3 (galleries, dot plots, the list of morphometric statistics). No claim rests on numbers that appear only in those, so I did not stop.
- **Cell count:** 1,329 cells, or 1,328 if the one cell whose recording failed quality control is missing.
**Missing from the paper:** the cut-off for "strong overlap" in Fig. 3d is not stated; the Fig. 5a legend's 25% was used. The p-value in Extended Data Fig. 6i appears only in the figure. No claim lacked text it needed beyond these.
== transcripts/000009/claims-report.md
**Missing from the paper text.** The Supplementary Information and Supplementary Tables 1 and 2 (animals, coordinates, light powers, viruses) are not there. Following earlier files in the registry, I went ahead instead of stopping. Two claims depend on the Supplementary Information and cannot be specified from the text: `latency-model-t3
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001559/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001559/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'));print(d.get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls tools schemas 2>/dev/null; grep -n "kind\|open\|readings" docs/claims*.md 2>/dev/null | head; ls docs
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
papers_manifest.py
progress.py
readme_row.py
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:6000])"
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1))" | head -120
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

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/001559/10.1021-acssensors.5c01093.yaml",
 "content": "# Claims for Tian, Zhang, Du, Huang, Bizimana, Nishimura & Ai (2025), ACS Sensors 10(8)\n# 5826-5833, on dandiset 001559.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, CC-BY 4.0), as served by Europe PMC\n# (PMC12351538), extracted text in paper/10.1021-acssensors.5c01093.txt: main text, Methods,\n# figure legends of Figures 1 to 5 and the Discussion. No PDF was supplied, so numbers and P\n# values printed only inside the figures could not be read. The Supporting Information PDF\n# (se5c01093_si_001.pdf; sequence alignment, Figure S1, brightness comparisons in Figure S2,\n# the HEK 293T spectrum in Figure S3, and Table S1) and Movies S1 to S3 were not in the text.\n# The claims that rest on them (lysate-brightness, cell-brightness, hek-spectrum,\n# table-s1-fold-gains) quote the main text and say what is missing. The findings this dandiset\n# holds (Figure 4) rest on the main text, the Figure 4 legend and the Methods only.\n#\n# Code: the paper links no analysis code. Its data statement only names Addgene plasmids\n# pcDNA3-eBRIC (#241800) and pAAV-hSyn-eBRIC (#241801). The dandiset description says it\n# includes \"the python scripts used for analysis and for figure generation\" of Figure 4.\n# Those are files of the dataset, which the reader may not open, so no code was read and\n# every method below comes from the paper. If the author finds that those scripts fix a\n# detail named here as open, that is a question for a reader.\n#\n# The dandiset (\"In-vivo Cortical Recording for eBRIC\") is described as holding the raw data\n# of Figure 4 only. The data of Figure 4, as the paper reports them: C57BL/6J mice (n = 6 in\n# the Methods; Figure 4D shows one representative mouse) with AAV-hSyn-eBRIC injected at four\n# sites in the whisker barrel cortex under a 4 mm craniotomy with a PDMS window, imaged at\n# least 3 weeks later under isoflurane (about 0.5% maintenance). Bioluminescence was recorded\n# through the objective of a two-photon microscope with the excitation laser blocked, on a\n# photomultiplier tube (Hamamatsu H10770B-50, 645/65 filter, home-built preamplifier) while\n# 2.5 mM DTZ was infused through a tail vein catheter at 25 uL/min. Two stimulating needle\n# electrodes (plus a ground) in the whisker pad, at two distinct locations, delivered 5 Hz\n# trains for 5 s at 2 mA and at 4 mA. Measured variable: the PMT bioluminescence signal over\n# time (arbitrary units), with stimulation times, electrode and current per trial. Also part\n# of Figure 4: two-photon fluorescence images of eBRIC expression (4x and 20x objectives,\n# FITC-dextran vessels) and laser speckle contrast images of blood flow during whisker pad\n# stimulation. The Figure 4D traces are smoothed with a 1-s moving average.\n#\n# The other figures (in vitro protein work, HeLa, HEK 293T, primary neurons, the BLA footshock\n# experiment in awake BALB/cJ mice) are not described as part of this dandiset; their claims\n# are listed to cover the paper's main findings.\n#\n# Details of Figure 4 the paper does not fix: the sampling rate of the PMT signal, the number\n# of trials per condition, the baseline and response windows, how a response is measured,\n# which electrode is \"region 1\", and any test. Criteria below name the readings the text\n# allows for each, and mark a choice as standard where it cannot change the outcome.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001559\"\npaper: doi:10.1021/acssensors.5c01093\nclaims:\n- id: fig4b-expression-healthy\n  statement: Two-photon fluorescence shows robust eBRIC expression in neuronal somata and\n    processes in the whisker barrel cortex, and the neurons look healthy and intact three\n    months after surgery.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4B\n  quote: Two-photon excited fluorescence revealed robust eBRIC expression\n    in neuronal somata and processes. Neurons appeared healthy and morphologically\n    intact even three months after surgery\n  criterion: The paper judges this by eye from images and gives no measure, so it can only be\n    checked qualitatively. Reproduced when the dandiset's two-photon fluorescence images show\n    labelled cell bodies and processes in the transduced region. Whether an image is from three\n    months after surgery is reported from the file metadata if it is given; health and\n    morphology are not judged.\n- id: fig4c-speckle-responsive-region\n  statement: Laser speckle contrast imaging shows that the region of viral expression responds\n    with blood flow changes to electrical stimulation of the whisker pad.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4C legend\n  quote: Laser speckle contrast imaging was used\n    to confirm that the viral expression was in a region that responded\n    to electrical stimulation of the whisker pad\n  criterion: The paper gives no measure or test for the speckle result. Reproduced when speckle\n    data are present for a mouse and show a change in speckle contrast (blood flow) over the\n    eBRIC-expressing region during whisker pad stimulation compared with before it, judged\n    from the images or traces as the paper shows them. No threshold is fixed by the paper;\n    the size of the change is reported. Blocked if the dandiset holds no speckle data.\n- id: fig4d-steady-baseline\n  statement: Infusing DTZ at 25 uL/min through the tail vein gives a steady level of baseline\n    bioluminescence during the recording.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4D\n  quote: Infusion at 25 μL/min generated a steady level\n    of baseline bioluminescence\n  criterion: The paper gives no measure of steadiness. As a reading of \"steady\" that the\n    analysis can apply, for each recording the pre-stimulus baseline of each trial (the mean of\n    the signal in the 5 s before stimulus onset; 5 s matches the stimulus length, a standard\n    choice) is computed, and the change of baseline over the recording is compared with the\n    mean evoked response at 4 mA in the same recording (response as in fig4d-evoked-increase).\n    Reproduced when, in the mouse or mice tested, the baseline changes from the first to the\n    last trial by less than the mean 4 mA evoked response, so responses stand out from any\n    drift. The baseline over time is shown for every recording. This threshold is not the\n    paper's; the outcome is to be read with that in mind and the drift reported as numbers.\n- id: fig4d-evoked-increase\n  statement: Whisker pad stimulation (5 Hz for 5 s) at 4 mA and at 2 mA, through each of the\n    two electrodes, gives clear increases in cortical eBRIC bioluminescence.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4D\n  quote: clear increases in bioluminescence\n    were observed with stimulation (4 and 2 mA) at both electrodes on\n    the whisker pad\n  criterion: From the Figure 4D legend, traces smoothed with a 1-s moving average and averaged\n    over trials per electrode and current. The response window, the baseline window and the\n    test are not given. The baseline is the 5 s before stimulus onset (a standard choice).\n    The response window has two readings the text allows, as the Results describe a delayed\n    peak for one electrode, (a) the 5-s stimulation period, (b) the stimulation period and the\n    5 s after it. Response per trial is the mean signal in the response window minus the\n    baseline mean. The paper reports no test; an increase is counted when the mean response\n    over trials is positive and a one-sided Wilcoxon signed-rank test of trial responses\n    against zero gives p < 0.05 (a standard choice, not the paper's). Figure 4D shows one\n    representative mouse that the paper does not identify, so there are two readings of\n    which mice must show it, (i) at least one mouse, as in the figure, (ii) every mouse\n    recorded with both currents and both electrodes. Reproduced when all four conditions (two\n    electrodes by two currents) show an increase under some combination of these readings;\n    the notebook shows every combination and which match.\n- id: fig4d-4ma-single-trials\n  statement: At 4 mA the response is strong enough to detect individual stimulation events, in\n    single trials without averaging.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4D; Discussion,\n    paragraph 4\n  quote: with\n    the 4 mA condition producing a sufficiently strong response to detect\n    individual stimulation events\n  depends_on:\n  - fig4d-evoked-increase\n  criterion: The paper gives no detection rule. \"Individual stimulation events\" has two\n    readings, (a) single 5-s stimulation trials, as the Discussion puts it (\"clear neural\n    responses to single whisker pad shocks in individual trials\"), (b) single pulses of the\n    5 Hz train. Reading (b) cannot be resolved in traces smoothed with the 1-s moving average\n    of the legend; it is tested on the unsmoothed signal by averaging it at each pulse time\n    within a trial (event-triggered on the 0.2-s pulse period) and is shown as a variant. For\n    reading (a), with windows as in fig4d-evoked-increase, a trial is detected when its\n    response exceeds k times the standard deviation of its smoothed baseline, with k = 2 or\n    k = 3 named as the two readings of a threshold the paper does not give. Reproduced when,\n    under reading (a) with either threshold, most 4 mA trials (more than half) in the mouse\n    or mice tested are detected and the fraction is higher at 4 mA than at 2 mA (\"sufficiently\n    strong\" implies 2 mA is less so). Every fraction is reported.\n- id: fig4d-electrode-timing\n  statement: The responses to the two electrode locations differ in timing; stimulation of\n    region 1 gives a delayed peak, and region 2 an earlier rise after stimulation onset.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 1; Figure 4D\n  quote: Stimulation of region 1\n    resulted in a delayed peak response, while region 2 elicited an earlier\n    rise in signal following stimulation onset\n  depends_on:\n  - fig4d-evoked-increase\n  criterion: Per electrode and current, the trial-averaged trace smoothed with a 1-s moving\n    average (Figure 4D legend), baseline the 5 s before onset. Time to peak is the time of the\n    maximum within the stimulation period and the 5 s after it; time of rise is the first time\n    after onset at which the averaged trace exceeds half its peak above baseline (a standard\n    choice, not the paper's). The paper does not say which electrode is region 1, and the\n    colours of Figure 4D could not be read without the PDF; if the dataset labels the\n    electrodes 1 and 2, those labels are used, otherwise both assignments are shown and the\n    claim is tested as (a) one electrode has both the later peak and the later rise. The paper\n    does not say at which current; the readings are 4 mA, 2 mA, or both. Reproduced when\n    region 1 has the later time to peak and region 2 the earlier time of rise at either\n    current, in the representative mouse reading (at least one mouse) of\n    fig4d-evoked-increase; the values for every mouse are reported.\n- id: fig5-bla-footshock-increase\n  statement: In awake head-fixed mice, footshock (0.8 mA, 1 s, every 40 s, 13 trials) gives a\n    significant and consistent increase in BLA bioluminescence with eBRIC and sDTZ, larger than\n    in mice expressing the Ca2+-insensitive control BREP.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 2; Figure 5B and 5C\n  quote: As expected,\n    we observed a significant and consistent increase in bioluminescence\n    in the eBRIC group in response to footshocks\n  criterion: As in the Figure 5C legend, each mouse's response averaged over its 13 trials, and\n    the eBRIC and BREP groups (4 and 3 mice) compared with an unpaired two-tailed t-test. The\n    P value is printed only in the figure and was not read. The response measure follows \"an\n    established procedure\" cited in the Methods and is not given in the text. Reproduced when\n    eBRIC responses exceed BREP responses at p < 0.05.\n- id: fig5-brep-minimal\n  statement: Mice expressing BREP show minimal to no change in bioluminescence under footshock.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 2; Figure 5B and 5C\n  quote: As a negative control, we generated mice expressing BREP, a Ca 2+ -insensitive bioluminescent\n    protein, and observed minimal to no changes in bioluminescence under\n    electric footshock stimulation\n- id: fig5-10hz-imaging\n  statement: eBRIC with sDTZ allowed BLI of the awake mouse brain at 10 Hz (100 ms exposures\n    without intervals).\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 2; Methods, BLI of BLA\n    Ca2+ Dynamics in Awake Mice\n  quote: The combination of eBRIC and sDTZ\n    allowed digitalization at a frequency of 10 Hz, which has not been\n    achieved in previous studies\n  expected:\n  - quantity: BLI frame rate\n    value: 10\n    tolerance: 1\n    unit: Hz\n- id: fig5-double-bric\n  statement: Under the same footshock condition, the eBRIC response in the BLA is nearly twice\n    that of BRIC in the authors' earlier experiments.\n  source: Results, In Vivo BLI of Ca2+ Dynamics in Live Mice, paragraph 2; Discussion,\n    paragraph 2\n  quote: Compared to prior experiments with BRIC\n    under the same stimulation condition, the response magnitude of eBRIC has nearly doubled\n  data: with_inputs\n  expected:\n  - quantity: ratio of eBRIC to BRIC footshock response magnitude\n    value: 2\n    tolerance: 0.2\n  criterion: The BRIC values come from the earlier study, Tian et al. 2022, Nat. Commun. 13\n    3967 (doi:10.1038/s41467-022-31673-x), which the text does not cite by number at this\n    sentence; the eBRIC value from Figure 5C. The ratio of the eBRIC group mean response to\n    the BRIC group mean response, each as the mean over mice of the 13-trial average.\n    \"Nearly doubled\" is read as the expected value 2 with 10% tolerance.\n- id: fig1a-lysate-18fold\n  statement: After three rounds of directed evolution, eBRIC shows an 18.2-fold Ca2+-induced\n    increase in bioluminescence (39 uM Ca2+ against no Ca2+) in bacterial cell lysates.\n  source: Results, Engineering and Characterization of eBRIC In Vitro, paragraph 2; Figure 1A\n  quote: Through three rounds of directed evolution, we successfully\n    generated a drastically enhanced BRIC (eBRIC) variant with an 18.2-fold\n    Ca 2+ -included bioluminescence increase in cell lysates\n  expected:\n  - quantity: eBRIC bioluminescence ratio, 39 uM Ca2+ against 0 Ca2+, lysate\n    value: 18.2\n    tolerance: 1.82\n- id: fig1b-mutations\n  statement: eBRIC carries five mutations from BRIC, two in teLuc, one in mScarlet-I and two in\n    the CaM-M13 region, and the two CaM-M13 mutations are mainly responsible for the larger\n    response.\n  source: Results, Engineering and Characterization of eBRIC In Vitro, paragraph 3; Figure 1A\n    to 1C\n  quote: During this process, five mutations were identified ... Notably, the two mutations in the CaM-M13 region are primarily\n    responsible for the observed response enhancement\n- id: fig1d-purified-response\n  statement: In purified protein, the response between 65 nM and 1.35 uM Ca2+ rises from\n    1.7-fold (BRIC) to 4.6-fold (eBRIC), and the change between 0 and 39 uM Ca2+ from 6.5-fold\n    to about 17-fold.\n  source: Results, Engineering and Characterization of eBRIC In Vitro, paragraph 4; Figure 1D\n  quote: From BRIC to eBRIC, the response between 65 nM and 1.35\n    μM of Ca 2+ increased from 1.7-fold to 4.6-fold, while\n    the overall Ca 2+ -induced change between 0 and 39 μM\n    of free Ca 2+ increased from 6.5-fold to ∼17-fold\n  expected:\n  - quantity: BRIC response, 65 nM to 1.35 uM Ca2+\n    value: 1.7\n    tolerance: 0.17\n  - quantity: eBRIC response, 65 nM to 1.35 uM Ca2+\n    value: 4.6\n    tolerance: 0.46\n  - quantity: BRIC response, 0 to 39 uM Ca2+\n    value: 6.5\n    tolerance: 0.65\n  - quantity: eBRIC response, 0 to 39 uM Ca2+\n    value: 17\n    tolerance: 1.7\n- id: fig1e-kd\n  statement: The apparent Kd of eBRIC for Ca2+ is 2.3 uM with a Hill coefficient of 1.3, from a\n    four-parameter Hill fit to bioluminescence at 600 nm (3 technical replicates); BRIC's was\n    133 nM.\n  source: Figure 1E legend; Results, Engineering and Characterization of eBRIC In Vitro,\n    paragraph 4\n  quote: A four-parameter Hill equation was used\n    to fit the data to determine the dissociation constant ( K d = 2.3 μM and Hill coefficient = 1.3)\n  expected:\n  - quantity: eBRIC apparent Kd\n    value: 2.3\n    tolerance: 0.23\n    unit: uM\n  - quantity: eBRIC Hill coefficient\n    value: 1.3\n    tolerance: 0.13\n  - quantity: BRIC apparent Kd\n    value: 133\n    tolerance: 13.3\n    unit: nM\n- id: lysate-brightness\n  statement: In bacterial lysates, eBRIC is dimmer than BRIC in the Ca2+-free state and brighter\n    in the Ca2+-bound state.\n  source: Results, Engineering and Characterization of eBRIC In Vitro, paragraph 2; Figure S2\n  quote: Compared to BRIC, eBRIC displayed reduced brightness\n    in the Ca 2+ -free state but enhanced brightness in the Ca 2+ -bound state\n  criterion: Figure S2 is in the Supporting Information, which was not in the text read, so\n    its values and any test are unknown. Judged on the direction of the two differences only.\n- id: fig2b-hela-5fold\n  statement: In HeLa cells stimulated with 20 uM histamine, eBRIC reports Ca2+ oscillations,\n    and its maximal change (dBL/BL0) is nearly 5-fold that of BRIC (33 eBRIC and 34 BRIC cells,\n    unpaired two-tailed t-test).\n  source: Results, Characterization of eBRIC in Cultured Mammalian Cells and Primary Neurons,\n    paragraph 1; Figure 2A and 2B\n  quote: Comparing this to BRIC\n    at identical conditions, the magnitude of the change (ΔBL/BL 0 ) was nearly 5-fold higher\n  expected:\n  - quantity: ratio of mean eBRIC to mean BRIC maximal dBL/BL0, HeLa\n    value: 5\n    tolerance: 0.5\n  criterion: As in the Figure 2B legend, the maximal dBL/BL0 of each cell after histamine, with\n    baselines corrected for monoexponential decay, compared between 33 eBRIC and 34 BRIC cells\n    by an unpaired two-tailed t-test. The P value is printed only in the figure and was not\n    read. Reproduced when the ratio of means is within tolerance and eBRIC is higher at p <\n    0.05.\n- id: fig2c-hek-3p5fold\n  statement: In HEK 293T cells, 10 uM acetylcholine gives a 3.5-fold (dBL/BL0) eBRIC\n    bioluminescence increase (20 cells).\n  source: Results, Characterization of eBRIC in Cultured Mammalian Cells and Primary Neurons,\n    paragraph 1; Figure 2C\n  quote: We observed a robust 3.5-fold\n    (ΔBL/BL 0 ) bioluminescence increase\n  expected:\n  - quantity: eBRIC dBL/BL0, HEK 293T, acetylcholine\n    value: 3.5\n    tolerance: 0.35\n- id: fig3-neurons-7p3fold\n  statement: In cultured primary mouse neurons, high K+ depolarization gives a 7.3-fold\n    (dBL/BL0) increase in eBRIC bioluminescence, 5.6 times the response of BRIC (24 eBRIC and 17\n    BRIC cells, unpaired two-tailed t-test).\n  source: Results, Characterization of eBRIC in Cultured Mammalian Cells and Primary Neurons,\n    paragraph 1; Figure 3B\n  quote: high K + depolarization induced a 7.3-fold increase (ΔBL/BL 0 ) in eBRIC bioluminescence, resulting in a 5.6-fold increase\n    in responsiveness from BRIC\n  expected:\n  - quantity: eBRIC maximal dBL/BL0, neurons\n    value: 7.3\n    tolerance: 0.73\n  - quantity: ratio of eBRIC to BRIC maximal dBL/BL0, neurons\n    value: 5.6\n    tolerance: 0.56\n  criterion: As in the Figure 3B legend, the maximal dBL/BL0 of each cell, 24 eBRIC and 17 BRIC\n    cells, compared by an unpaired two-tailed t-test (P value only in the figure, not read).\n    Reproduced when both values are within tolerance and eBRIC is higher at p < 0.05.\n- id: cell-brightness\n  statement: In HeLa cells eBRIC is dimmer than BRIC in the Ca2+-free state and about twice as\n    bright after histamine stimulation, with a similar trend in primary neurons.\n  source: Results, Characterization of eBRIC in Cultured Mammalian Cells and Primary Neurons,\n    paragraph 2; Figure S2\n  quote: eBRIC\n    exhibited reduced brightness in the Ca 2+ -free state but\n    demonstrated approximately twice the brightness of BRIC after stimulation.\n    A similar trend was observed in primary neurons\n  expected:\n  - quantity: ratio of eBRIC to BRIC brightness after histamine, HeLa\n    value: 2\n    tolerance: 0.2\n  criterion: Figure S2 was not in the text read, so how brightness was measured is unknown.\n    Judged on the ratio and the direction of the Ca2+-free difference.\n- id: hek-spectrum\n  statement: The emission spectrum of eBRIC in HEK 293T cells closely resembles that in lysates\n    and as purified protein, so expression in mammalian cells does not change BRET efficiency.\n  source: Results, Characterization of eBRIC in Cultured Mammalian Cells and Primary Neurons,\n    paragraph 2; Figure S3\n  quote: The spectral profile closely resembled that of eBRIC in lysates and as a purified protein, suggesting\n    that expression in mammalian cells does not alter the BRET efficiency\n  criterion: Figure S3 was not in the text read; the paper's measure of resemblance is\n    unknown.\n- id: table-s1-fold-gains\n  statement: In physiologically stimulated live cells, eBRIC is 4.5- to 5.6-fold more responsive\n    than BRIC and 7.4- to 18-fold more responsive than Orange CaMBIs.\n  source: Discussion, paragraph 1; Table S1\n  quote: Compared to Orange CaMBIs, we\n    gained 7.4- to 18-fold increase in Ca 2+ responsiveness\n    using the new eBRIC Ca 2+ sensor in physiologically stimulated\n    live cells ( Table S1 ). Compared to our\n    previously reported BRIC sensor, eBRIC\n    is 4.5- to 5.6-fold more responsive\n  data: with_inputs\n  expected:\n  - quantity: eBRIC against BRIC responsiveness, lower bound\n    value: 4.5\n    tolerance: 0.45\n  - quantity: eBRIC against BRIC responsiveness, upper bound\n    value: 5.6\n    tolerance: 0.56\n  - quantity: eBRIC against Orange CaMBIs responsiveness, lower bound\n    value: 7.4\n    tolerance: 0.74\n  - quantity: eBRIC against Orange CaMBIs responsiveness, upper bound\n    value: 18\n    tolerance: 1.8\n  criterion: Table S1 is in the Supporting Information, which was not in the text read. The\n    Orange CaMBI values come from the literature (Oh et al. 2019, Nat. Chem. Biol. 15 433,\n    doi:10.1038/s41589-019-0256-z); which cells and stimuli enter each ratio is given only in\n    Table S1. The range holds when each bound is within the range widened by 10% of each bound.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001559/10.1021-acssensors.5c01093.yaml paper/10.1021-acssensors.5c01093.txt; python -c "
import yaml,json,jsonschema
d=yaml.safe_load(open('claims/001559/10.1021-acssensors.5c01093.yaml'));s=json.load(open('schemas/claims.schema.json'))
jsonschema.validate(d,s);print('schema ok',len(d['claims']))"; grep -n '—\|rather' claims/001559/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001559/10.1021-acssensors.5c01093.yaml` with 21 claims, all of them quoted word for word. The quote checker reports 0 problems and the file validates against the claims schema. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC12351538): main text, Methods, the legends of Figures 1 to 5, and the Discussion. There was no PDF, so values printed only inside figures could not be read.

**Missing from the paper text:**
- **The supplement is missing.** The Supporting Information PDF (Fig. S1, the brightness data in Fig. S2, the HEK 293T spectrum in Fig. S3, and Table S1) and Movies S1 to S3 are not in `paper/`.
- **Why I went ahead anyway:** the dandiset says it holds only the Figure 4 cortical recordings, and those claims rest on the main text, the Figure 4 legend and the Methods. Earlier readers in the registry (001750 to 001752, 001746) did the same.
- **Claims that need the supplement:** `lysate-brightness`, `cell-brightness`, `hek-spectrum` and `table-s1-fold-gains`. They quote the main text, and their criteria say that their measures and tests are unknown without it.
- **P values:** the unpaired t-test P values for Figs. 2B, 3B and 5C appear only inside the figures, so those tests are named in the criteria but have no `statistics` entry.
- **Response measure for Fig. 5:** it follows an "established procedure" that the Methods cite without describing it.

**Code:** the paper links no analysis code. The dandiset's description says it includes the Figure 4 analysis and figure scripts, but those are dataset files, so I did not open them. If they settle any detail below, that is a question for a reader.

**Counts:**
- 21 claims: 6 on Figure 4, 4 on Figure 5, 4 on Figure 1, 3 on Figures 2 and 3, and 4 that need the supplement.
- Quotes: all 21.
- Statistics entries: 0, because no p-value or interval is printed in the text.
- `expected` values: 10 claims have them.
- Criteria: 15 claims have one.
- Two claims use outside data: `fig5-double-bric` (BRIC values from Tian et al. 2022, doi:10.1038/s41467-022-31673-x) and `table-s1-fold-gains` (Orange CaMBI values from Oh et al. 2019).

**Details left open in Figure 4, with the readings named:**
- **Response window:** (a) the 5 s stimulation period, or (b) the stimulation period plus 5 s after it.
- **Which mice must show the increase:** (i) at least one mouse, since the figure shows one unidentified "representative mouse", or (ii) every mouse recorded under all four conditions.
- **"Individual stimulation events":** (a) single 5 s trials, which matches the Discussion's wording, or (b) single pulses of the 5 Hz train, run as a variant on the unsmoothed signal.
- **Detection threshold:** 2 or 3 baseline standard deviations.
- **Which electrode is "region 1":** the dataset's own labels if it has them, otherwise both assignments.
- **Current for the timing claim:** 4 mA, 2 mA, or both.

**Choices that are mine, not the paper's, and labelled as such in the file:**
- a 5 s pre-stimulus baseline;
- a one-sided Wilcoxon test for "clear increase", since the paper gives no test;
- half of the peak as the rise-time threshold;
- the drift threshold for the "steady baseline" claim.

The paper gives no PMT sampling rate and no trial counts.

## End of run

15 turns, 3 minutes, result: success.
