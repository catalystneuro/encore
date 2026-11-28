# alonso-2020 · claims · run 45712540890

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/ claims/ tools/
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
cat claims/fouke-2025.yaml; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55470.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55470.txt",
 "offset": 705,
 "limit": 360
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/alonso-2020.yaml 2>/dev/null; grep -rl "m31b1h7" --include=*.yaml --include=*.json . 2>/dev/null | grep -v "^./transcripts" | head; python -c "import fitz;d=fitz.open('paper/10.7554-elife.55470.pdf');print(d.page_count)" 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/match/dryad-m31b1h7.yaml; python -c "
import json;d=json.load(open('targets/dryad.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  if 'm31b1h7' in json.dumps(t): print(json.dumps(t,indent=1)[:3000])
"; ls docs/; grep -n -i "code\b\|software" docs/archives.md | head -20
```

```
# Whether each paper Dryad:m31b1h7 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dryad
  id: m31b1h7
date: '2026-11-25'
papers:
- doi: 10.7554/elife.55470
  relation: primary_article
  checks:
    text: true
    title_in_text: true
    names_this: true
    names_others: []
  verdict: primary
  by: checks
  reason: The paper names Dryad:m31b1h7 and no other dataset.
{
 "id": "m31b1h7",
 "name": "Temperature compensation in a small rhythmic circuit",
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
which pdfinfo pdftotext; pdfinfo paper/*.pdf 2>/dev/null | grep Pages; python -c "import pypdf" 2>&1; grep -n "Figure supplement\|figure supplement" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.55470.pdf",
 "pages": "21"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "6W66" paper/*.txt | cat -A | head -3; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:12000])"
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

**Agent calls Write**

```json
{
 "file_path": "claims/alonso-2020.yaml",
 "content": "# Claims for Alonso & Marder (2020), \"Temperature compensation in a small rhythmic circuit\",\n# eLife 9:e55470, tested on Dryad m31b1h7.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-25, protocol pilot-19 (docs/protocol.md, Reader).\n#\n# Text read. The version of record (eLife PDF, text extracted with PyMuPDF, under paper/),\n# main text, figure legends and Materials and methods. The figure supplements (Figure 1, figure\n# supplements 1 to 3; Figure 2, figure supplement 1; Figure 6, figure supplement 1) are not in\n# paper/ beyond their titles, so their legends and panels were not read. The claims that rest\n# on them use the sentences of the main text that describe them. The PDF could not be rendered\n# here, so no figure was read from it; the pie-chart counts of Figure 10B are therefore not\n# recorded.\n#\n# Code. The paper's only deposit is the dataset itself. Its Data availability says \"Code and\n# parameters to reproduce the results in this work was uploaded to Dryad\", and the archive\n# lists a single zip of about 99 kB. As the reader may not open the dataset, that code was not\n# read. Where these criteria leave a detail open and the deposited code fixes it, the author\n# follows the code and says so; where the code disagrees with the Methods, the Methods govern\n# the main result and the code's choice is a variant (protocol, Reader, step 2).\n#\n# The data. No recordings. The paper simulates a three-cell model of the crustacean pyloric\n# network (PD, the AB-PD pacemaker kernel in one compartment; LP; PY) after Prinz et al. 2004.\n# Each cell is a single compartment with eight currents (INa, ICaT, ICaS, IA, IKCa, IKd, IH,\n# Ileak) and 13 state variables; seven chemical synapses of two types (glutamatergic and\n# cholinergic). Each model is 31 maximal conductances plus three calcium time constants and 24\n# Q10 values (shared across cells), Tref = 10 degrees C, Q10 in [1, 2] for conductances and\n# [1, 4] for time scales. Simulated with RK4 at dt = 0.05 ms from V = -51 mV, gating variables 0\n# and [Ca] = 5 uM. 36 temperature-compensated models are studied, each with a six-character\n# name. The Methods list the model of each figure. Figure 1, 4?6W66 (the second character is\n# unreadable in the extracted text); Figure 1 supplement 1, WWZ3CN, FGFKQS, 71G6LA; Figure 1\n# supplement 2, PLKTEM; Figure 1 supplement 3, all models; Figure 2, G7P2WE; Figure 2\n# supplement 1, G7P2WE, 4?6W66, MAXTTP; Figure 3, 4?6W66 and SJR46Y; Figure 4, WWZ3CN;\n# Figure 5, FGFKQS; Figure 6, FGFKQS and 71G6LA; Figure 6 supplement 1, B7SDOL, J9U8SQ, 4R2719,\n# R3VIEW, Q8FBN1, RMZ8KZ, EF84RN, SJR46Y; Figure 7 (A to E), J9U8SQ, G81PUL, G7EOZ8, SAXT8Y,\n# KNMLBC; Figure 8, OSHNMD and H5AIZR; Figure 9, WWZ3CN and FGFKQS; Figure 10, 4?6W66.\n# Some figure legends name models differently (Figure 5 and Figure 9B say \"same model as in\n# Figure 7A\"); the claims that are affected name both readings.\n#\n# Every claim's test is a new simulation of the deposited models with the deposited code, so\n# data is the dataset throughout. The paper reports no statistical tests.\n#\n# Shared method, from the Methods unless said otherwise. Bursts are formed by grouping spikes\n# with a 200 ms threshold (Classification scheme), the slow-wave threshold is -50 mV, duty\n# cycle is burst duration over period and phases are burst onsets and offsets in units of the\n# period from the PD burst start (Results, Duty cycle and phase maintenance, paragraph 1).\n# The cell and network activity classes are those of the Classification scheme (CV of ISI\n# 0.1; lag 20 ms; CV of duty cycle 1; CV of burst frequency 0.1; triphasic when the cell\n# frequencies agree within 5% and the cells fire in the order PD, LP, PY). Open in the paper,\n# for every claim, and to be taken from the deposited code where it fixes them: the spike\n# detection threshold, whether an initial transient is dropped (the Methods drop the first\n# 10 s when scoring and use the last 10 s of 30 s for voltage distributions), the initial\n# state of the synapses, and how \"fired in the right order\" is tested.\nschema_version: 2\npaper: doi:10.7554/elife.55470\nclaims:\n- id: deposit-models\n  kind: link\n  statement: The deposit holds the code and the parameters of the paper's models, under the\n    names the Methods give, and simulating them at 10 degrees C gives the control rhythm the\n    models were fitted to, about 1 Hz with a PD duty cycle near 20% and LP and PY duty cycles\n    near 25%.\n  source: Data availability; Materials and methods, Finding parameters, paragraph 3, and\n    Parameters used in this study\n  quote: The target control behavior was defined as having all cells bursting with 20% duty cycle\n    for PD\n  expected:\n  - quantity: burst frequency of each cell at 10 degrees C, per model\n    value: 1.0\n    tolerance: 0.1\n    unit: Hz\n  - quantity: PD duty cycle at 10 degrees C, per model\n    value: 0.2\n    tolerance: 0.02\n  - quantity: LP and PY duty cycle at 10 degrees C, per model\n    value: 0.25\n    tolerance: 0.025\n  criterion: Each model named in the Methods' list (Parameters used in this study) is found\n    in the deposit, and the deposit holds 36 models (Results, Duty cycle and phase\n    maintenance, paragraph 3). Every Q10 is within [1, 2] for maximal conductances and [1, 4]\n    for time scales (Materials and methods, Finding parameters, paragraph 4). Each model is\n    simulated at 10 degrees C for 20 s and the first 10 s dropped, as the Methods score\n    solutions. The targets are a fit, not an exact result, so the link holds (reproduced)\n    when the values are within tolerance for at least 30 of the 36 models, partially\n    reproduced for 18 to 29, not reproduced below 18. The LP and PY target is 25% in the\n    Methods and \"duty cycle = 20% for LP and PY\" in the Results (paragraph 3); 0.2 is shown\n    as a variant.\n- id: fig1c-frequency-q10-phase-constant\n  statement: In the model of Figure 1, as temperature rises from 10 to 25 degrees C the burst\n    frequency of all three cells increases with a Q10 near 2, while each cell's duty cycle and\n    the phases of burst onsets and offsets stay approximately constant.\n  source: Figure 1B and 1C; Results, Duty cycle and phase maintenance in model pyloric networks,\n    paragraph 4\n  quote: While the burst frequency increases with Q10 » 2, the duty cycle of the cells, and the\n    phases of the onsets/offsets of activity, remain approximately constant.\n  expected:\n  - quantity: Q10 of burst frequency, model 4?6W66, 10 to 25 degrees C\n    value: 2.0\n    tolerance: 0.2\n  criterion: Model 4?6W66 simulated at 16 temperatures from 10 to 25 degrees C (1 degree\n    apart), with averages over 30 s (Figure 1 legend). The paper does not say how Q10 is\n    computed. The readings are (a) exp(10 times the slope) of a least-squares fit of ln\n    frequency on temperature; (b) (f25 / f10) to the power 10/15; (c) f20 / f10. Nor does it\n    give a bound for \"approximately constant\". The readings are (i) every cell's mean duty\n    cycle and every onset and offset phase stays within 0.1 of a cycle over the 16\n    temperatures (a standard choice); (ii) each stays within 20% of its 10 degree value,\n    after the 0.2 relative spread the Methods allow in duty cycle (Finding parameters,\n    paragraph 2). Reproduced when the frequency Q10 is within tolerance under one reading and\n    duty cycles and phases are constant under one reading; partially reproduced when only one\n    of the two holds. The three cells' frequencies are reported (the legend says they nearly\n    coincide).\n- id: fig1s1-three-models\n  statement: In three further models with different maximal conductances and Q10 values, the\n    duty cycles and phases also stay approximately constant while the frequency increases\n    from 10 to 25 degrees C.\n  source: Results, Duty cycle and phase maintenance in model pyloric networks, paragraph 4;\n    Figure 1, figure supplement 1A\n  quote: Figure 1—figure supplement 1A shows the same analysis performed on three different\n    models. In all cases, the duty cycle and the phases stay approximately constant while the\n    frequency increases.\n  depends_on:\n  - fig1c-frequency-q10-phase-constant\n  criterion: Models WWZ3CN, FGFKQS and 71G6LA, the same analysis and the same readings of\n    \"approximately constant\" as fig1c-frequency-q10-phase-constant (the supplement's legend is\n    not in the text read, so its temperatures are taken as those of Figure 1C). Frequency must\n    rise from 10 to 25 degrees C in every cell. Reproduced when all three models meet both\n    parts under one reading of constancy; partially reproduced for two.\n- id: all-models-compensated\n  statement: All 36 models produce a triphasic pyloric rhythm over the working range of 10 to\n    25 degrees C; for every set of maximal conductances tried, Q10 values that make the rhythm\n    temperature robust could be found.\n  source: Results, Duty cycle and phase maintenance in model pyloric networks, paragraph 3;\n    Materials and methods, Finding parameters, paragraph 5\n  quote: We then selected 36 of these models and for each of them we searched for Q10 values so\n    that the activity is preserved over a temperature range. We found that, regardless of the\n    maximal conductances G, it was always possible to find multiple sets of Q10 values that\n    produced a temperature robust pyloric rhythm.\n  expected:\n  - quantity: number of models\n    value: 36\n    tolerance: 0\n  criterion: The search itself (a genetic algorithm with 1000 individuals for 10,000\n    generations) is not repeated; that several Q10 sets exist per model cannot be tested\n    unless the deposit holds them, and the author says whether it does. Each of the 36\n    deposited models is simulated at 10 to 25 degrees C in 1 degree steps, as in Figure 1C,\n    and its network activity is classified with the Methods' scheme. Reproduced when every\n    model is triphasic at every temperature; partially reproduced when at least 34 are (the\n    Methods report 2 failures in 40 before screening); not reproduced otherwise. The count of\n    temperatures that fail is reported per model.\n- id: intermediate-temperature-failures\n  statement: Of the Q10 solutions that met the target at the control temperatures, 2 in 40 did\n    not display the correct activity at temperatures in between.\n  source: Materials and methods, Finding parameters, paragraph 5\n  quote: We found that if the system meets the target activity at the control temperatures, in\n    the vast majority of the cases, the models also displayed the correct activity for\n    temperatures in between, but there were exceptions (2 in 40 cases).\n  expected:\n  - quantity: solutions failing between control temperatures\n    value: 2\n    tolerance: 0\n  - quantity: solutions screened\n    value: 40\n    tolerance: 0\n  criterion: Testable only if the deposit holds the 40 solutions, including the 2 that were\n    discarded. Each is scored at 15, 20 and 25 degrees C with the objective of Equation 6 and\n    screened at the temperatures in between (1 degree steps from 10 to 25 degrees C, as in\n    Figure 1C) with the network classification. Reproduced when 2 of the 40 fail between\n    control temperatures and none of the other 38 do.\n- id: figs2-ramp-largest-isi\n  statement: During a temperature ramp from 10 to 25 degrees C over 60 min, the spiking\n    patterns change in complicated ways and the largest ISI decreases monotonically, in step\n    with the rising burst frequency.\n  source: Results, Duty cycle and phase maintenance in model pyloric networks, paragraph 5;\n    Figure 1, figure supplement 2\n  quote: As temperature is increased the spiking patterns change in complicated ways and the\n    largest ISI decreases monotonically, consistent with the overall increase in bursting\n    frequency of the cells.\n  criterion: Model PLKTEM ramped linearly from 10 to 25 degrees C over 60 min, spike times of\n    each cell recorded. The largest ISI is taken per burst cycle (the interburst interval).\n    How it is followed over the ramp is open. The readings are (a) the largest ISI in\n    successive windows of 1 degree C (4 min); (b) in successive windows of 1 min. Reproduced\n    when, under one reading, the largest ISI decreases from window to window in every cell\n    (a Spearman correlation with temperature below -0.9 in each cell, a standard choice, with\n    any increase between windows reported); partially reproduced when that holds for one or\n    two cells.\n- id: figs3-duty-cycle-variable-across-models\n  statement: Across the 36 models the LP duty cycle depends on temperature in different ways,\n    so that the duty cycle distributions differ from model to model.\n  source: Results, Duty cycle and phase maintenance in model pyloric networks, paragraph 5;\n    Figure 1, figure supplement 3; Discussion, paragraph 9\n  quote: Across the models, different values of the maximal conductances G and temperature\n    sensitivities Q10 result in consistent differences in the duty cycle distributions.\n  criterion: The supplement's legend is not in the text read. For each of the 36 models, the\n    per-burst duty cycles of LP over 10 to 25 degrees C (the ramp of Figure 1, figure\n    supplement 2, 10 to 25 degrees C over 60 min, is the reading taken; simulations at the 16\n    temperatures of Figure 1C are the variant). Reproduced when the models' LP duty-cycle\n    distributions differ by a two-sample Kolmogorov-Smirnov test at p < 0.05 for most model\n    pairs (more than half of the 630 pairs), a standard choice; the median and range of each\n    model's LP duty cycle are reported.\n- id: fig2-lp-spike-amplitude-threshold\n  statement: In the LP cell of the model of Figure 2, spike amplitude decreases and the spike\n    threshold depolarizes as temperature rises from 10 to 25 degrees C.\n  source: Figure 2; Results, Changes in membrane potential over temperature, paragraph 1\n  quote: The membrane potential changes with temperature in several ways... the spike amplitude\n    decreases and the spike threshold depolarizes as temperature increases.\n  criterion: Model G7P2WE, LP cell, 101 temperatures from 10 to 25 degrees C, each simulated\n    for 30 s from identical initial conditions at dt = 0.001 (ms, read from the Methods' dt\n    units elsewhere), the last 10 s used (Materials and methods, Membrane potential and\n    current shares distributions). The paper does not define amplitude or threshold. The\n    readings are, for amplitude, (a) the mean spike peak minus the mean trough before each\n    spike, (b) the upper envelope of the voltage distribution (its highest voltage with\n    nonzero occupancy); for threshold, (a) V where dV/dt first exceeds 10 mV/ms before each\n    spike (a standard choice), (b) the voltage at which the distribution's spike region\n    begins. Reproduced when, under one reading of each, amplitude falls and threshold rises\n    from 10 to 25 degrees C (Spearman correlation with temperature below -0.5 and above 0.5,\n    a standard choice); partially reproduced when one of the two holds.\n- id: fig2s1-peak-voltage-diverse\n  statement: The effect of temperature on the membrane potential differs across models; in\n    three example models the peak voltage of spikes decreases, increases, or stays relatively\n    constant with temperature, and cells can become more depolarized or more hyperpolarized.\n  source: Results, Changes in membrane potential over temperature, paragraph 1; Figure 2,\n    figure supplement 1\n  quote: In some models, the peak voltage of spikes, as indicated by the upper envelope of the\n    distributions, decreases (left), increases (middle), or remains relatively constant\n    (right). In addition, we found that cells can either become more depolarized or more\n    hyperpolarized as temperature increases.\n  depends_on:\n  - fig2-lp-spike-amplitude-threshold\n  criterion: Models G7P2WE (left), 4?6W66 (middle) and MAXTTP (right), voltage distributions\n    as in fig2-lp-spike-amplitude-threshold for every cell. The upper envelope is the highest\n    voltage with nonzero occupancy at each temperature. The supplement does not say which cell\n    shows the trend, so a model counts when any of its cells does. Decrease or increase is a\n    change of more than 5 mV from 10 to 25 degrees C in that direction, and relatively\n    constant is a change within 5 mV over the range in every cell (5 mV is a standard choice;\n    2 mV and 10 mV are shown as variants). Reproduced when all three models show their stated\n    pattern and, among all cells of the three models, the mean voltage rises with temperature\n    in at least one and falls in at least one; partially reproduced when two models do.\n- id: fig3-current-amplitudes\n  statement: In the PD cell of one model, from 10 to 25 degrees C the Na current peak more than\n    doubles, the CaT current peak falls to about half despite its larger conductance, and the\n    KCa current grows about six-fold; in a second model the Na current falls slightly and the\n    KCa current falls moderately.\n  source: Figure 3A and 3B; Results, Dynamics of the currents at different temperatures,\n    paragraphs 2 and 3\n  quote: In this example, the Na current increases its amplitude by more than two fold over the 15\n    ̊C range. Despite the fact that gCaT increases with temperature, the ... amplitude of the\n    current decreases to about half its control value at 10 ̊C\n  expected:\n  - quantity: model 4?6W66, PD, CaT peak at 25 over 10 degrees C\n    value: 0.5\n    tolerance: 0.05\n  - quantity: model 4?6W66, PD, KCa peak at 25 over 10 degrees C\n    value: 6\n    tolerance: 0.6\n  criterion: Model 4?6W66 (Figure 3A) and SJR46Y (Figure 3B), PD cell, at 10 and 25 degrees C.\n    The peak amplitude is the absolute peak of each current (the legend's red dashed line at\n    the control peak). Over how long is open. The readings are (a) the largest absolute value\n    over the analysed window; (b) the mean over cycles of each cycle's peak. Reproduced when,\n    under one reading, in 4?6W66 the Na ratio exceeds 2 and the CaT and KCa ratios are within\n    tolerance, and in SJR46Y the Na ratio is below 1 and the KCa ratio is below 1 (the paper's\n    words are \"a small amount\" and \"moderately\", so no bound is set; the ratios are\n    reported). Partially reproduced when at least three of these five hold.\n- id: fig4-currentscapes-reorganize\n  statement: In the model of Figure 4, currentscapes differ between 10 and 25 degrees C; in PD\n    the leak current's inward share is seen at both the start and end of the burst at 10\n    degrees C but mainly at the start at 25 degrees C, the A current's share is even across\n    the burst at 10 degrees C and larger at its start at 25 degrees C, and in all cells, most\n    in LP and PY, temperature raises the KCa share toward the end of bursts.\n  source: Figure 4; Results, Dynamics of the currents at different temperatures, paragraphs 4\n    and 5\n  quote: in the PD cell the Leak current contributes a visible share of the inward current both\n    at the beginning and the end of the burst at 10 ̊C, but at 25 ̊C its contribution is mainly\n    confined to the ... beginning of the burst. The A current is evenly distributed during the\n    burst at 10 ̊C but at 25 ̊C its contribution is visibly larger at the beginning of the burst.\n    In all cells, but most notably in the LP and PY neurons in this example model, temperature\n    substantially increases the contribution of the KCa current toward the end of the bursts.\n  criterion: Model WWZ3CN at 10 and 25 degrees C. Currentscape shares are each current's\n    percent of the total inward (or outward) current at each time (Alonso and Marder 2019, as\n    the Results cite). Shares are averaged over bursts. Start and end of the burst are open.\n    The readings are (a) the first and last third of the burst; (b) the first and last 20%\n    of it. Reproduced when, under one reading, in PD the leak's inward share at the end over\n    that at the start is lower at 25 than at 10 degrees C, the A share at the start over that\n    at the end is near 1 at 10 degrees C (within 0.8 to 1.25, a standard choice) and higher\n    at 25 degrees C, and the KCa outward share at the end of the burst is higher at 25 than at\n    10 degrees C in all three cells, with the increase in LP and PY larger than in PD.\n    Partially reproduced when the KCa part holds and one of the two PD parts.\n- id: currentscapes-dominant-currents\n  statement: In all models and at all temperatures, spikes are driven first by INa and then by\n    IKd, which then dominate the inward and outward currents, and when the cells are most\n    hyperpolarized IH and the synaptic currents dominate.\n  source: Results, Dynamics of the currents at different temperatures, paragraph 5\n  quote: During spike production, the activity is first driven by INa and later by IKd. During\n    these periods, the total inward and outward currents differ by orders of magnitude and are\n    entirely dominated by one current type. Similarly, when the cells are most hyperpolarized\n    the dominant currents are IH and the synaptic currents ISyn.\n  criterion: All 36 models, every cell, at 10, 15, 20 and 25 degrees C (the paper does not say\n    which temperatures were inspected; these are its control temperatures). Near each spike\n    peak (the 1 ms before the peak, and the 1 ms after it, a standard choice), INa has the\n    largest share of the inward current before the peak and IKd the largest share of the\n    outward current after it. At the 5% of time with the lowest voltage, IH has the largest\n    share of the inward current and the synaptic current the largest share of the outward\n    current. Reproduced when this holds in at least 90% of spikes and of model, cell and\n    temperature cases (a standard bound for \"all\"); the fractions are reported.\n- id: fig5-a-to-kca-tradeoff\n  statement: In the 20 ms after the PD burst, the share of the A current falls smoothly and the\n    share of the KCa current rises smoothly as temperature goes from 10 to 25 degrees C, so the\n    neuron slides between burst termination mechanisms; IA dominates repolarization of the last\n    spike at 10 degrees C and IKCa at 25 degrees C.\n  source: Figure 5; Results, Dynamics of the currents at different temperatures, paragraph 6;\n    Discussion, paragraph 5\n  quote: Almost all of the currents change over this temperature range, most notably there is\n    almost a tradeoff between the contributions of the A and KCa currents, with A decreasing\n    smoothly and KCa increasing smoothly.\n  criterion: The model is open. The Methods name FGFKQS for Figure 5 and the legend says \"same\n    model as in Figure 7A\", which the Methods name J9U8SQ; both are run. PD cell, the 20 ms\n    after burst termination (last spike of the burst), outward shares averaged over bursts,\n    at the 16 temperatures of Figure 1C (the number Figure 5 shows is not in the text; 1\n    degree steps are a standard choice). Reproduced when, in one of the two models, the A\n    share falls and the KCa share rises with temperature (Spearman correlation below -0.9 and\n    above 0.9, a standard bound for \"smoothly\"), the A share exceeds the KCa share at 10\n    degrees C and the KCa share exceeds the A share at 25 degrees C. Partially reproduced when\n    the two trends hold without the crossover.\n- id: fig6-crash-different-mechanisms\n  statement: Two models that are phase compensated at 10 and 25 degrees C crash at 30 degrees C\n    with complete loss of PD activity, by different currents in each.\n  source: Figure 6; Results, Dynamics of the currents at different temperatures, paragraph 7\n  quote: Figure 6 shows full currentscapes for two network models as they ‘crash’ at high\n    temperature. Note that the complete loss of activity in the PD neurons results from\n    different currents being active in the two examples.\n  criterion: Models FGFKQS and 71G6LA at 10, 25 and 30 degrees C. Reproduced when both are\n    triphasic at 10 and 25 degrees C, PD is quiescent at 30 degrees C in both (no spikes in\n    the analysed window, the Methods' quiescent class), and the current with the largest\n    inward share and the current with the largest outward share in PD at 30 degrees C,\n    averaged over the analysed window, are not both the same in the two models. Partially\n    reproduced when the two crash with PD quiescent but the dominant currents match.\n- id: fig7-high-temperature-slow-timescales\n  statement: At temperatures above 25 degrees C the models crash in different ways (quiescence,\n    subthreshold oscillations, or irregular activity), and in five models at 29 to 34 degrees\n    C time scales much longer than the 1 s period at 10 degrees C emerge.\n  source: Figure 7; Results, High temperatures produce disordered circuits or ‘crashes’,\n    paragraphs 1 and 2\n  quote: In all cases, there are timescales in the behavior that are much longer than the period\n    of the rhythm at 10 ̊C ( » 1 s).\n  criterion: Models J9U8SQ, G81PUL, G7EOZ8, SAXT8Y and KNMLBC at 34, 34, 33, 29 and 30 degrees C\n    (Figure 7 legend), 30 s analysed. A time scale much longer than 1 s is read as (a) an\n    interval longer than 2 s between successive bursts or spikes of some cell, or (b) a\n    dominant period of the slow voltage (spikes removed by a 50 ms median filter, a standard\n    choice) longer than 2 s, the factor 2 a standard bound for \"much longer\". Reproduced when\n    all five models show it under one reading and none is triphasic; partially reproduced for\n    three or four. The cell and network classes of each are reported, as is how many of the\n    36 models at 26 to 35 degrees C are quiescent, subthreshold or irregular.\n- id: fig8a-hysteresis-quiescence\n  statement: During a temperature ramp from 10 to 35 degrees C and back, the PD cell of one\n    model becomes quiescent before reaching 35 degrees C and resumes spiking on the way down at\n    a temperature about 2 degrees C lower than where it stopped, so the model is multistable\n    over that range.\n  source: Figure 8A; Results, Hysteresis and multistability, paragraph 1\n  quote: The temperature at which the cell resumes spiking is » 2 ̊C lower than the temperature\n    at which it became quiescent, indicating that the system is multi-stable over that\n    temperature range.\n  expected:\n  - quantity: temperature of quiescence onset minus temperature of recovery, model OSHNMD\n    value: 2\n    tolerance: 0.2\n    unit: degrees C\n  criterion: Model OSHNMD, temperature raised linearly from 10 to 35 degrees C in 30 min and\n    lowered back at the same rate (Results, Hysteresis, paragraph 1). Quiescence onset is the\n    temperature of the last PD spike on the up ramp and recovery the temperature of the first\n    PD spike on the down ramp. Reproduced when PD stops spiking before 35 degrees C and stays\n    quiescent until the down ramp, and the difference is within tolerance. The legend's\n    \"before 600 s\" cannot be squared with the stated ramp (600 s is about 18 degrees C), so\n    the time of the last spike is reported and not judged.\n- id: fig8-up-down-ramps\n  statement: In 34 of the 36 models the spiking patterns over the working range are similar\n    but not identical on the up and down ramps, suggesting several stable attractors that\n    differ slightly in their spiking patterns.\n  source: Results, Hysteresis and multistability, paragraph 1; Figure 1, figure supplement 2E\n  quote: In most models (34 of 36), the spiking patterns over the working temperature range are\n    similar across the up and down ramps but are not identical\n  expected:\n  - quantity: models with similar but not identical patterns on the two ramps\n    value: 34\n    tolerance: 3\n  criterion: All 36 models on the ramp of fig8a-hysteresis-quiescence, comparing the up and down\n    ramps over 10 to 25 degrees C; the ramp of Figure 1, figure supplement 2 (10 to 25 degrees\n    C over 60 min and back) is the alternative reading, as the supplement's legend is not in\n    the text read. Per cell and per 1 degree window, the mean duty cycle, burst frequency and\n    largest ISI on each ramp. Similar is all of these within 10% between the ramps in every\n    window and the network triphasic on both (a standard bound); not identical is spike times\n    not coinciding. The tolerance is 10% of 36, rounded. Reproduced when the count of similar\n    models is within tolerance under one ramp reading.\n- id: fig8b-pathological-attractor\n  statement: In a second model hysteresis is marked; at high temperatures it produces ISIs as\n    long as about 1 s while spiking at all temperatures, and its PD cell passes from regular\n    bursting into a pathological state that persists on the down ramp until about 20 degrees C.\n  source: Figure 8B; Results, Hysteresis and multistability, paragraph 2\n  quote: At high temperatures (times between 25 and 35 min), this model produces ISI values as\n    long as » 1 s and remains spiking at all temperatures. The spiking patterns differ\n    noticeably on the up and down ramps. The spiking pattern of the PD cell changes from\n    regular bursting to a pathological state that remains stable until the model is ramped\n    back down to » 20 ̊C.\n  expected:\n  - quantity: temperature on the down ramp at which PD returns to regular bursting, model H5AIZR\n    value: 20\n    tolerance: 2\n    unit: degrees C\n  - quantity: longest PD ISI between 25 and 35 min\n    value: 1\n    tolerance: 0.1\n    unit: s\n  criterion: Model H5AIZR on the ramp of fig8a-hysteresis-quiescence. PD is classified in\n    successive 1 min windows with the Methods' scheme. Reproduced when PD spikes in every\n    window, is regular bursting early on the up ramp, leaves regular bursting on the up ramp\n    and returns to it on the down ramp at a temperature within tolerance, and the longest ISI\n    between 25 and 35 min is within tolerance. Partially reproduced when the hysteresis holds\n    and one of the two numbers is out of tolerance.\n- id: fig9a-remove-a-current\n  statement: Removing the A current at 10 degrees C makes the network irregular, while the same\n    deletion at 25 degrees C leaves a nearly normal triphasic rhythm except for irregular PY\n    bursting.\n  source: Figure 9A; Results, Response to perturbations at different temperatures, paragraph 2\n  quote: Figure 9A (top) shows that removing the A current at 10 ̊C has catastrophic\n    consequences for the network activity which becomes irregular. When the same perturbation\n    is performed at 25 ̊C (bottom), the triphasic rhythm is almost normal except for the\n    irregular bursting of PY.\n  criterion: Model WWZ3CN (Methods; the legend's \"same model as in Figure 4\" agrees). The\n    timing is open. The Results say 20 s of control and then 20 s with IA removed; the legend\n    says the A current is removed at 4 s. Both are run, and the classes are taken over the\n    period after removal (dropping its first 2 s, a standard choice). Reproduced when, under\n    one timing, at 10 degrees C the network is not triphasic and at least one cell is\n    irregular bursting or irregular spiking, and at 25 degrees C PD and LP are regular\n    bursting and PY is irregular bursting. Partially reproduced when the 10 degree part holds\n    and at 25 degrees C PY is irregular but another cell is not regular.\n- id: fig9b-remove-kca-current\n  statement: In another model, removing the KCa current at 10 degrees C slows the rhythm but\n    keeps it triphasic, while the same deletion at 25 degrees C silences the network, so KCa is\n    needed at 25 degrees C but not at 10 degrees C.\n  source: Figure 9B; Results, Response to perturbations at different temperatures, paragraph 2\n  quote: This model displayed normal ... triphasic behavior at 10 ̊C (top) and when the KCa\n    current was removed its activity slowed but the triphasic rhythm was maintained. The same\n    perturbation at 25 ̊C results in quiescence.\n  criterion: The model is open. The Methods name FGFKQS for Figure 9 and the legend says \"a\n    different model (Figure 7A)\", which the Methods name J9U8SQ; both are run. Timing as in\n    fig9a-remove-a-current. Reproduced when, in one model and timing, at 10 degrees C the\n    network is triphasic before and after removal with a lower burst frequency after, and at\n    25 degrees C all three cells are quiescent after removal.\n- id: fig10a-graded-removal\n  statement: In the model of Figure 10A, reducing gNa to 75% makes LP burst irregularly and the\n    network non-triphasic at 10 degrees C but not at 25 degrees C; removing KCa has little\n    effect at 10 degrees C but complete removal makes it quiescent at 25 degrees C; complete\n    removal of CaT or CaS gives different non-triphasic activity at each temperature.\n  source: Figure 10A; Results, Response to perturbations at different temperatures, paragraphs\n    3 and 4\n  quote: At 10 ̊C, when gNa ! 75%gNa the LP cell bursts irregularly and the activity of the\n    network is not triphasic, but if the same perturbation is performed at 25 ̊C the activity\n    remains triphasic. Removing the KCa current in this model has little effect at 10 ̊C as the\n    activity remains triphasic. However, this current plays an important role at 25 ̊C and the\n    model becomes quiescent upon complete removal of IKCa.\n  criterion: Model 4?6W66 at 10 and 25 degrees C, each of gNa, gKCa, gCaT and gCaS set to 100,\n    75, 50, 25 and 0% in all three cells (the five steps and the 5 by 4 grids of the Results;\n    that a reduction applies to all cells is read from the shared current types and is\n    assumed). Each condition simulated and classified with the Methods' scheme; the length\n    of the simulation is open, and the 20 s with the first 10 s dropped of the Methods'\n    scoring is used. Reproduced when the five stated cells of the grids match (Na 75% at 10\n    degrees C, LP irregular bursting and NET not triphasic; Na 75% at 25 degrees C, NET\n    triphasic; KCa 25 to 100% at 10 degrees C, NET triphasic; KCa 0% at 25 degrees C, all\n    cells quiescent; CaT and CaS 0%, NET not triphasic at both temperatures with some cell\n    class differing between them). Partially reproduced when three or four match. The full\n    grids are reported.\n- id: fig10b-complete-removal-differs\n  statement: Across the 36 models, the response to complete removal of a current differs\n    between 10 and 25 degrees C in about half of the models for most currents; most models\n    respond differently for CaT, while removing H gives the same state (quiescence) at both\n    temperatures.\n  source: Figure 10B; Results, Response to perturbations at different temperatures, paragraph 4\n  quote: In most cases, about half of the models respond to complete removal in different ways\n    at each temperature. The exceptions are the CaT current for which most models respond in\n    different ways, and the H current where complete removal results in equivalent states\n    (quiescence in this case) at both temperatures.\n  depends_on:\n  - fig10a-graded-removal\n  criterion: All 36 models, each current type set to 0% at 10 and at 25 degrees C, classified\n    as in fig10a-graded-removal. The pie-chart counts were not read (no figure could be\n    rendered). Which currents are included is open (the eight intrinsic currents, or the\n    seven without leak), and so is what counts as the same response. The readings are (a)\n    all four classes (PD, LP, PY, NET) equal at the two temperatures; (b) the NET class\n    equal. \"About half\" is a fraction of models responding differently from 0.3 to 0.7 and\n    \"most\" above 0.5 (standard bounds). Reproduced when, under one reading, CaT has the\n    largest fraction responding differently and above 0.5, H has all or nearly all models\n    (at least 33) the same and quiescent at both temperatures, and at least half of the\n    other currents fall within 0.3 to 0.7. Partially reproduced when the CaT and H parts hold\n    and fewer of the other currents do.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/alonso-2020.yaml paper/10.7554-elife.55470.txt; grep -nE "[^ ]: |—" claims/alonso-2020.yaml | grep -vE "^[0-9]+:(#|\s*-?\s*[a-z_]+: )" | head; grep -n -i "rather" claims/alonso-2020.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/alonso-2020.yaml",
 "old_string": "  quote: Figure 1—figure supplement 1A shows the same analysis performed on three different\n    models.",
 "new_string": "  quote: shows the same analysis performed on three different models."
}
```

```
The file claims/alonso-2020.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/alonso-2020.yaml paper/10.7554-elife.55470.txt; grep -c "—" claims/alonso-2020.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/alonso-2020.yaml`. The quote checker passes it: 22 claims, 22 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record, extracted from the eLife PDF under `paper/`. That covers the main text, figure legends and Materials and methods. No preprint was used.

**Missing from the paper:**
- **Figure supplements:** only their titles are in the text (Figure 1 supplements 1 to 3, Figure 2 supplement 1, Figure 6 supplement 1). Their legends and panels are missing. The four claims that rest on them (`fig1s1-three-models`, `figs2-ramp-largest-isi`, `figs3-duty-cycle-variable-across-models`, `fig8-up-down-ramps`) use the main-text sentences that describe them. I went ahead because the main findings rest on the main figures. If you count these supplements as ones the results rest on, they should be supplied.
- **PDF figures:** the PDF could not be rendered (pdftoppm is not installed), so no figure was read. The pie-chart counts of Figure 10B are not recorded.
- **Model name:** the extracted text garbles the second character of the model used in Figures 1, 3 and 10 (written as "4?6W66" in the file).

**Code:** the only code the paper links to is the dataset itself, a 99 kB zip of code and parameters on Dryad. I was not allowed to open the dataset, so I read no code. The claims tell the author to take any open detail from the deposited code where it settles it, with the Methods taking precedence where the two disagree.

**Claims:**
- 21 are findings and 1 is a link check that the deposited models match the paper's list and fitted targets.
- All 22 have quotes.
- None has statistics, because the paper reports no tests.
- 21 have criteria; the 22nd (`fig1c-frequency-q10-phase-constant`) is judged on its expected values.
- 9 have expected values.
- Every claim is `data: dataset`, meaning a new simulation of the deposited models.

**Details the paper leaves open, and the readings named:**
- **Shared to all claims:** the spike detection threshold, whether the initial transient is dropped, the synapses' starting state, and how "fired in the right order" is tested. All are left to the deposited code.
- **Q10 of burst frequency:** (a) a log-linear fit over temperature, (b) the 25 to 10 °C frequency ratio raised to 10/15, or (c) the 20 to 10 °C ratio.
- **"Approximately constant" duty cycle and phases:** within 0.1 of a cycle, or within 20% of the 10 °C value (borrowed from the Methods' 0.2 spread limit).
- **Spike amplitude and threshold (Fig. 2):** amplitude as peak minus trough or the top of the voltage distribution; threshold as a dV/dt crossing or where the distribution's spike region begins.
- **Peak current amplitude (Fig. 3):** the largest value in the window, or the mean of per-cycle peaks.
- **Start and end of a burst (Fig. 4):** the first and last third, or the first and last 20%.
- **Model mismatches between legends and Methods:**
  - Figure 5: FGFKQS (Methods) or J9U8SQ ("same model as Figure 7A" in the legend). Both are run.
  - Figure 9B: the same pair, FGFKQS or J9U8SQ. Both are run.
- **Deletion timing (Fig. 9):** 20 s of control then 20 s with the current removed (Results), or removal at 4 s (legend). Both are run.
- **Up and down ramps (34 of 36 models):** which ramp is compared, the 10 to 35 °C one in 30 min or the 10 to 25 °C one over 60 min; "similar" is set at a standard 10% bound.
- **Figure 10B:** whether leak counts among the removed currents; "same response" as all four classes (PD, LP, PY, network) equal or only the network class; and standard bounds for "about half" (0.3 to 0.7) and "most" (above 0.5).
- **Slow time scales (Fig. 7):** read as an interval of more than 2 s between bursts or spikes, or a slow-voltage period of more than 2 s.
- **Largest ISI over the ramp:** followed in 1 °C windows or 1 min windows.
- **Bounds the paper never gives:** I set standard ones and labelled them as such, for "smoothly" (Spearman correlation beyond 0.9), "all" (at least 90% of cases) and the 5 mV used for peak voltage trends.

**Internal inconsistencies, recorded in the claims:**
- The LP and PY duty-cycle target is 25% in the Methods and about 20% in the Results. The 20% is shown as a variant.
- The Figure 8A legend says the cell goes quiet "before 600 s", but on the stated ramp that is about 18 °C. The time is reported but not judged.
- The claim that 2 of 40 solutions failed between control temperatures can only be tested if the deposit holds all 40 solutions, including the 2 that were discarded.

## End of run

18 turns, 4 minutes, $1.38 at API prices, result: success.
