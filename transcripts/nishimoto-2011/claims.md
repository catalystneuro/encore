# nishimoto-2011 · claims · run 42842179851

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml; ls claims | head; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/; ls claims | head -30; ls tools
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/mt-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/nishimoto-2011.yaml 2>/dev/null; wc -l paper/*.txt; head -20 paper/10.1523-jneurosci.6801-10.2011.txt; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6801-10.2011.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6801-10.2011.txt",
 "offset": 829,
 "limit": 320
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims | grep -i -E "nishimoto|kay|david|oliver|willmore"; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)); print(json.dumps(d['properties'].get('checks',{}),indent=1)[:500])"; cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1523-jneurosci.6801-10.2011.pdf')
for i in [2,5,6,7,8,9]:
  d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm pdftotext; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent**

Let me try reading the PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6801-10.2011.pdf",
 "pages": "6-10"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; ls $TMPDIR/pylib | head
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
_yaml
bin
fitz
flatbuffers
flatbuffers-25.12.19.dist-info
google
networkx
networkx-3.7.dist-info
numpy
numpy-2.5.4.dist-info
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1523-jneurosci.6801-10.2011.pdf')
for i in [5,6,7,8,9]:
  d[i].get_pixmap(dpi=120).save(f'p{i+1}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p10.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as f
d=f.open('paper/10.1523-jneurosci.6801-10.2011.pdf')
p=d[5]; r=p.rect
clip=f.Rect(r.width*0.27,r.height*0.28,r.width*0.68,r.height*0.42)
p.get_pixmap(dpi=400,clip=clip).save('fig2b.png')
p=d[6]; p.get_pixmap(dpi=110).save('p7.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig2b.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent**

The full text (version of record, Methods included) is present; J Neurosci 2011 has no supplement beyond Movie 1, and the paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/nishimoto-2011.yaml",
 "content": "# Claims for Nishimoto & Gallant (2011), J Neurosci 31(41):14551-14564, tested on CRCNS mt-2.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (paper/10.1523-jneurosci.6801-10.2011.txt, PyMuPDF extraction\n# of the publisher PDF), main text, Materials and Methods and figure legends. The paper has no\n# supplement other than Movie 1 (stimulus spectra, not a result). Figure 2B, Figure 3, Figure 6\n# and Figure 7 were read from the PDF where the text extraction garbled symbols; the\n# inequality signs of every p-value were read there (p < 0.01, p > 0.10 and so on). The paper\n# links no code, so no repository was read. The dataset's own documentation\n# (paper/mt-2.data-description.txt) was read only to know what the dataset is meant to hold.\n#\n# Data the paper used (Materials and Methods, Physiology; Visual stimuli; Results, opening\n# paragraph). 52 single MT neurons from two adult male macaques (Macaca mulatta) performing a\n# fixation task. Each neuron saw 20,000 to 40,000 frames (mean 27,120) of motion-enhanced\n# natural movies at 83 Hz as training data (the Results say 22,000 to 42,000 frames), and a\n# separate 2000-frame motion-enhanced movie repeated 5 to 20 times as validation data. A subset\n# of 15 neurons also saw a 2000-frame natural movie without motion enhancement, repeated 5 to\n# 20 times, as a second validation set. Measured variable is the spike train, analysed at the\n# 83 Hz frame rate. The CRCNS description says mt-2 holds 45 neurons (not 52), each with the\n# movie frames around its receptive field (about two receptive field widths, 128 x 128\n# pixels), spike counts averaged and binned at 83 Hz (psths), and the frame indices of the\n# training (ranges.crange) and validation (ranges.vrange) stimuli. Whether the 15 natural-movie\n# validation sets, single repeats or trial boundaries are present is for the author to find.\n#\n# The model all the claims rest on (Materials and Methods, The V1 filter bank; Regression by\n# boosting; Tests for nonlinearities). The stimulus (a patch two classical receptive field\n# widths across) is filtered by a bank of 5956 spatiotemporal Gabor filters (Eq. 1) spanning\n# 12 directions, five spatial frequencies log spaced from 0 to 6 cycles per classical\n# receptive field (cRF), six velocities and temporal frequencies log spaced from 0 to 30 Hz;\n# filters tiled on a grid with 2.2 sigma between neighbours, one cycle of the carrier per two\n# sigma of the envelope; simple cell outputs (half-wave rectified, phases 0, 90, 180 and 270\n# degrees) limited to 2 cycles per cRF, and complex cell outputs (quadrature energy, Eq. 4).\n# Optional stages are luminance and contrast normalization of the movie (Eq. 10 to 12), a\n# static nonlinearity of half-wave rectification raised to the power alpha (1.0 linear, 0.5\n# compressive, 2.0 expansive; Eq. 13), and divisive normalization by the summed outputs of\n# all filters, each prenormalized to unit SD, plus a semisaturation constant sigma (Eq. 14).\n# The response is a linear sum of filter outputs over delays up to 10 frames (Eq. 5), fit by\n# coordinate gradient boosting (Eq. 6 to 9) with early stopping, five times with a different\n# 20% of the training data held out, the five weight sets averaged. Validation data are never\n# used in fitting. The validation response is the mean over repeats smoothed with a 12 ms\n# temporal Gaussian; prediction accuracy is the correlation between predicted and observed\n# validation responses. The first 220 ms of each trial's movie overlapped the previous trial\n# and the associated responses were removed before analysis (Visual stimuli, paragraph 3).\n#\n# Details the paper leaves open, for every claim that fits the model (each is a deviation,\n# with the readings named; the notebook runs each that could change an outcome).\n# - Temporal width of the Gabor envelopes, the exact six velocities and the filter count per\n#   scale are not given beyond the totals above; a bank matching the stated ranges and a\n#   total near 5956 is a standard choice.\n# - The cRF size, which sets the filter spatial frequencies. Readings are (a) half the stored\n#   stimulus patch, since the analysis window is two cRF widths and the dataset stores about\n#   two receptive field widths; (b) the full stored patch as the analysis window with no\n#   other rescaling. These are the same if the patch is exactly two cRF widths.\n# - The delays. \"up to 10 frames or 130 ms\" disagree at 83 Hz (10 frames are 120 ms). Readings\n#   are (a) delays 0 to 10 frames (11 delays, 132 ms); (b) delays 1 to 10 frames.\n# - The 12 ms Gaussian may be (a) its SD or (b) its full width at half maximum. At 12 ms\n#   frames the two differ little.\n# - The boosting step size epsilon and the semisaturation constant sigma are not given.\n#   Readings for sigma are (a) chosen on the held-out 20% of the training data, as the early\n#   stopping is; (b) a fixed small constant (1% of the mean pooled response). Step size is a\n#   standard small value (for example 1% of the SD of the response), which changes the\n#   number of iterations more than the result.\n# - How the 20% held-out parts are formed. Readings are (a) five contiguous blocks of the\n#   training frames; (b) five random partitions of frames.\n# - Whether the compressive power applies to complex cell outputs as well as simple cell\n#   outputs. Eq. 13 says \"the output of the linearized Gabor filters\", which reads as all V1\n#   filter outputs X; that reading is taken, with the power on simple cells only as a variant.\n# - The order of divisive normalization and the static nonlinearity is as in Figure 2A (static\n#   nonlinearity first, then divisive normalization).\n# - Where the validation responses of the natural-movie set exist, the paper averages the two\n#   predictions per neuron (Results, Control to identify any bias, paragraph 2). Where the\n#   dataset holds only one validation set, the prediction is that set's correlation, and this\n#   is recorded as a deviation.\nschema_version: 2\npaper: doi:10.1523/jneurosci.6801-10.2011\nclaims:\n- id: fig3b-mean-prediction\n  statement: The compressive and divisive V1 filter model predicts the validation responses of\n    the 52 MT neurons with an average correlation of r = 0.52.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 3; Figure 3B\n  quote: Figure 3B summarizes prediction performance of the compressive/divisive V1 filter model\n    across the entire sample of 52 MT neurons\n  expected:\n  - quantity: mean correlation between predicted and observed validation responses\n    value: 0.52\n    tolerance: 0.052\n  criterion: The model of the opening comment with the compressive nonlinearity (alpha 0.5) and\n    divisive normalization, no luminance and contrast normalization, fit per neuron on the\n    training frames and tested on the validation frames (Materials and Methods, Regression by\n    boosting). Prediction accuracy per neuron is the Pearson correlation of predicted and\n    observed validation responses; the claim is judged on the mean over all neurons in the\n    dataset (45, not the paper's 52). Reproduced when the mean is within tolerance under one\n    of the readings named in the opening comment; the per-neuron distribution is shown against\n    Figure 3B (most neurons between 0.2 and 0.9).\n- id: fig3b-explainable-variance\n  statement: The compressive and divisive model accounts for 35% of the explainable response\n    variance of MT neurons.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 3; Figure 3 legend\n  quote: and the model accounts for 35% of the explainable response variance (David and Gallant,\n    2005)\n  depends_on:\n  - fig3b-mean-prediction\n  expected:\n  - quantity: proportion of explainable variance explained, population\n    value: 35\n    tolerance: 3.5\n    unit: percent\n  criterion: The paper names the measure (explainable variance, after David and Gallant, 2005)\n    and gives no formula. Readings are (a) the mean over neurons of r squared divided by the\n    squared noise ceiling correlation estimated from the validation repeats as in David and\n    Gallant (2005); (b) the mean r squared over neurons divided by the mean squared ceiling.\n    Reproduced when either is within tolerance. Needs the single validation repeats; if the\n    dataset holds only their average, the claim cannot be tested and is blocked as data\n    missing.\n- id: fig3a-example-neuron\n  statement: For one example neuron the correlation between model predictions and observed\n    responses is r = 0.72.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 3; Figure 3A\n  quote: The correlation between model predictions and observed responses for this neuron is\n    quite good\n  depends_on:\n  - fig3b-mean-prediction\n  expected:\n  - quantity: prediction correlation of the example neuron\n    value: 0.72\n    tolerance: 0.072\n  criterion: The paper does not name the neuron, only that its validation movie was repeated 10\n    times. Reproduced when at least one neuron of the dataset has a prediction correlation\n    within tolerance; the neurons that do, and those among them with 10 validation repeats if\n    that can be seen, are listed.\n- id: fig2b-contrast-normalization-no-effect\n  statement: Luminance and contrast normalization of the stimulus does not significantly change\n    prediction accuracy compared with the simplest model (linear half-wave rectification, no\n    normalization stages).\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: Contrast normalization does not have a significant effect on predictions compared with\n    the simplest model\n  statistics:\n  - test: Wilcoxon signed-rank test with Bonferroni correction\n    p: 0.1\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 52 neurons\n  criterion: A claim of absence, judged on the paper's test. Per neuron, the prediction accuracy\n    of the model with luminance and contrast normalization (Eq. 10 to 12), linear static\n    nonlinearity and no divisive normalization, against the simplest model, by a Wilcoxon\n    signed-rank test across neurons with Bonferroni correction. The number of comparisons is\n    not given; readings are (a) 11, the 11 models of Figure 2B compared with the simplest;\n    (b) 5, the comparisons the Results text reports. Reproduced when the corrected p is not\n    below 0.05 under the reading used; the size of the change is given either way. The\n    measure compared (\"predictive power\") is the correlation of the first claim; the\n    readings of the percent change are those of fig2b-compressive-improves.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig2b-compressive-improves\n  statement: A compressive static output nonlinearity consistently increases predictions over\n    the simplest model, by about 16% without and about 19% with divisive normalization.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: The compressive static output nonlinearity consistently increases predictions\n  statistics:\n  - test: Wilcoxon signed-rank test with Bonferroni correction\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 52 neurons\n  expected:\n  - quantity: increase of predictive power, compressive, no divisive normalization, no luminance\n      normalization, read from Figure 2B\n    value: 16\n    tolerance: 4\n    unit: percent\n  - quantity: increase of predictive power, compressive, with divisive normalization, no\n      luminance normalization, read from Figure 2B\n    value: 19\n    tolerance: 4\n    unit: percent\n  criterion: The values are read from the bars of Figure 2B (no number is printed), so the\n    tolerance is 4 percentage points, the reading precision (about 1 point) plus about twice\n    the bootstrap SE shown (about 2 points). The paper does not define \"increase of\n    predictive power\". Readings are (a) the percent change of the mean correlation over\n    neurons relative to the simplest model; (b) the same with mean squared correlation;\n    (c) the mean over neurons of each neuron's percent change in correlation. Significance by\n    a Wilcoxon signed-rank test across neurons against the simplest model, Bonferroni\n    corrected as in fig2b-contrast-normalization-no-effect. Reproduced when, under one reading,\n    both values are within tolerance and both comparisons give corrected p < 0.01; partially\n    reproduced when both are significant increases but a value falls outside tolerance.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig2b-expansive-decreases\n  statement: An expansive static output nonlinearity always decreases predictions relative to\n    the simplest model, by about 36% without and about 24% with divisive normalization.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: while the expansive nonlinearity always decreases predictions\n  statistics:\n  - test: Wilcoxon signed-rank test with Bonferroni correction\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 52 neurons\n  expected:\n  - quantity: change of predictive power, expansive, no divisive normalization, no luminance\n      normalization, read from Figure 2B\n    value: -36\n    tolerance: 4\n    unit: percent\n  - quantity: change of predictive power, expansive, with divisive normalization, no luminance\n      normalization, read from Figure 2B\n    value: -24\n    tolerance: 4\n    unit: percent\n  criterion: As in fig2b-compressive-improves (measure readings, test and the 4 point tolerance\n    for values read from the figure), with alpha 2.0. Reproduced when, under one reading, both\n    values are within tolerance and both decreases have corrected p < 0.01; partially\n    reproduced when both are significant decreases but a value falls outside tolerance.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig2b-divisive-improves\n  statement: Divisive normalization significantly improves predictions over the simplest\n    model, by about 8% with the linear static nonlinearity.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: Divisive normalization also improves predictions significantly\n  statistics:\n  - test: Wilcoxon signed-rank test with Bonferroni correction\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 52 neurons\n  expected:\n  - quantity: increase of predictive power, linear static nonlinearity with divisive\n      normalization, no luminance normalization, read from Figure 2B\n    value: 8\n    tolerance: 4\n    unit: percent\n  criterion: As in fig2b-compressive-improves, for the model with linear static nonlinearity and\n    divisive normalization (Eq. 14) against the simplest model. Reproduced when, under one\n    reading, the value is within tolerance and the corrected p < 0.01; partially reproduced\n    when the increase is significant but outside tolerance.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig2b-compressive-divisive-best\n  statement: The model with both a compressive nonlinearity and divisive normalization predicts\n    significantly better than the model with the compressive nonlinearity alone, and is the\n    simplest model that gives accurate predictions.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: The model that contains both a compressive nonlinearity and divisive normalization has\n    significantly more predictive power than a model that contains only a compressive\n    nonlinearity\n  statistics:\n  - test: Wilcoxon signed-rank test with Bonferroni correction\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 52 neurons\n  criterion: Per neuron, prediction accuracy of the compressive model with divisive\n    normalization against the compressive model without it (both without luminance\n    normalization), Wilcoxon signed-rank test across neurons, Bonferroni corrected as in\n    fig2b-contrast-normalization-no-effect. Reproduced when the corrected p < 0.01 with the\n    divisive model better and, as Figure 2B shows, no model of the 12 has a significantly\n    higher accuracy than it; partially reproduced when the comparison is significant at p <\n    0.05 only.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig2b-no-interaction\n  statement: The effects of the compressive and expansive nonlinearities do not depend on\n    whether divisive normalization is present.\n  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area\n    MT, paragraph 2; Figure 2B\n  quote: Note, however, that the effects of the compressive and expansive nonlinearities do not\n    depend on whether divisive normalization is present or not\n  criterion: The paper reports no test for this. Read from Figure 2B as the same direction and\n    significance of each effect in both panels. Readings of the effect are (a) against the\n    simplest model, as the figure plots; (b) against the linear model of the same divisive\n    normalization condition. Reproduced when, under one reading, the compressive model is\n    better and the expansive model worse, each at corrected p < 0.01 (Wilcoxon signed-rank,\n    Bonferroni as in fig2b-contrast-normalization-no-effect), both with and without divisive\n    normalization.\n  depends_on:\n  - fig2b-compressive-improves\n  - fig2b-expansive-decreases\n- id: complex-cells-dominate\n  statement: Most of the response variance is captured by the model complex cells, and the\n    model simple cells have only a small effect on prediction performance.\n  source: Materials and Methods, The V1 filter bank, paragraph 3 (data not shown)\n  quote: most of the response variance is captured by the model complex cells, and the model\n    simple cells have only small effect on prediction performance (data not shown)\n  criterion: The paper shows no data and names no test. Within the compressive and divisive\n    model, fit (a) the complex cell channels only and (b) the simple cell channels only, with\n    the same procedure. Reproduced when the complex-only model reaches at least half of the\n    full model's mean squared prediction correlation and drops the mean correlation less than\n    the simple-only model does. The threshold of one half is this file's reading of \"most of\n    the response variance\"; the per-neuron values are shown.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig6a-null-on-plane\n  statement: For 150 model MT neurons with random weights, the average excitatory on-plane ratio\n    is 0.36.\n  source: Results, Excitatory spectral receptive fields lie on a plane, paragraph 2; Figure 6A\n    (dashed line); Materials and Methods, Null hypotheses test for on-plane ratio\n  quote: The average on-plane ratio for this null model is 0.36\n  expected:\n  - quantity: mean excitatory on-plane ratio, null model neurons\n    value: 0.36\n    tolerance: 0.036\n  criterion: As the Methods say, 150 model neurons with weights drawn from a normal\n    distribution (mean 0, SD 1) on the compressive and divisive filter outputs, used to filter\n    the experiment's movies, Poisson noise added, receptive fields refit by the same procedure,\n    and the on-plane ratio computed as in fig6a-excitatory-on-plane. Open details, with\n    readings. Which movies, (a) each model neuron assigned the training and validation movies\n    of one recorded neuron in turn, (b) all model neurons on one neuron's movies. How rates\n    are made non-negative and scaled for the Poisson noise, (a) rectified and scaled to the\n    mean spike count of the recorded neuron whose movie is used, (b) offset to non-negative\n    and scaled to the same mean. Whether random weights span all delays, (a) all 5956 filters\n    at every delay, (b) a single delay. Reproduced when the mean is within tolerance under\n    one combination of readings; every combination run is shown.\n  depends_on:\n  - fig6a-excitatory-on-plane\n- id: fig6a-excitatory-on-plane\n  statement: Excitatory spectral receptive fields of MT neurons tend to lie on a single plane in\n    the three-dimensional frequency domain; their average on-plane ratio is 0.59, significantly\n    above the null model's 0.36.\n  source: Results, Excitatory spectral receptive fields lie on a plane, paragraphs 1 and 2;\n    Figure 6A\n  quote: Figure 6A summarizes the onplane ratio for the excitatory receptive fields of all 52 area\n    MT neurons in our sample. The average ratio is 0.59\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    n: 52 neurons against 150 null model neurons\n  expected:\n  - quantity: mean excitatory on-plane ratio\n    value: 0.59\n    tolerance: 0.059\n  criterion: From the compressive and divisive model fit of each neuron. The optimal velocity\n    plane passes through the origin and is set by azimuth (direction) and elevation (speed);\n    it maximizes the summed positive V1 filter weights whose temporal frequency lies within\n    1 octave or 5 Hz of the plane, whichever is larger (maximum coverage), together with the\n    symmetry constraint, the negative of the difference of the weights summed on the two sides\n    of the plane's azimuth (Materials and Methods, Optimal velocity plane). The on-plane ratio\n    is the positive weights near the plane over the total positive weights (Figure 6 legend).\n    Open details, with readings. The balance of the two constraints was set by hand; readings\n    are (a) coverage only, with symmetry breaking ties; (b) coverage and symmetry each scaled\n    by the total positive weight and summed with equal weight. What is summed, (a) the fitted\n    weights, as the Methods and Figure 6 legend say; (b) the weights times each filter's\n    spectral amplitude, as \"proportion of the spectral receptive field\" in the Results\n    suggests. Sign split, (a) per weight at each delay; (b) after summing each filter's\n    weights over delays. Reproduced when, under one combination, the mean is within tolerance\n    and a Wilcoxon rank-sum test against the null model ratios gives p < 0.01 with the real\n    ratios higher.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig6b-suppressive-off-plane\n  statement: Suppressive spectral receptive fields tend to avoid the optimal excitatory plane;\n    their average on-plane ratio is 0.18, significantly below the null model.\n  source: Results, Suppressive spectral receptive fields lie off the optimal excitatory plane;\n    Figure 6B\n  quote: The average ratio is 0.18, which is significantly smaller than the value for the null\n    model described above\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    n: 52 neurons against 150 null model neurons\n  expected:\n  - quantity: mean suppressive on-plane ratio\n    value: 0.18\n    tolerance: 0.018\n  criterion: The on-plane ratio of fig6a-excitatory-on-plane computed on the negative weights,\n    with the plane found from the excitatory weights (Figure 6 legend), under the same\n    readings. The null comparison is the null model of fig6a-null-on-plane; the paper does\n    not say whether the null values here are the excitatory or the suppressive ratios of the\n    model neurons, so both readings are run ((a) the null excitatory ratios, mean 0.36, as\n    \"the null model described above\" suggests; (b) the null suppressive ratios). Reproduced\n    when, under one reading, the mean is within tolerance and the rank-sum test gives p <\n    0.01 with the real ratios lower.\n  depends_on:\n  - fig6a-excitatory-on-plane\n  - fig6a-null-on-plane\n- id: fig7a-partial-ring\n  statement: The horizontal-vertical ratio is distributed continuously; few neurons form a full\n    ring (ratio near 1) or a single spatiotemporal frequency peak (ratio near 0), and most form\n    a partial ring in the optimal plane that avoids low temporal frequencies.\n  source: Results, Excitatory spectral receptive fields of most MT neurons form a partial ring\n    in the plane, paragraphs 1 and 2; Figure 7A; Figures 4 and 5\n  quote: However, the receptive fields of the large majority of MT neurons lie between these\n    extremes, forming a partial ring in the optimal velocity plane and avoiding the region near\n    zero temporal frequency\n  criterion: The optimal plane of fig6a-excitatory-on-plane is divided into four quadrants, two\n    centred on the vertical axis (along the optimal direction) and two on the horizontal axis\n    (in the zero temporal frequency plane); the excitatory spectral amplitudes are integrated\n    in the horizontal and in the vertical quadrants and the ratio horizontal over vertical is\n    taken (Results, same section, paragraph 1). Open details, with readings. Quadrant borders\n    at 45 degrees from each axis (the only symmetric choice, taken as standard). Amplitudes\n    on the plane are those within the near-plane band of fig6a-excitatory-on-plane (a), or\n    all excitatory amplitude projected onto the plane (b). \"Extremes\" are not bounded; Figure\n    7A suggests (a) ratios below 0.2 and from 0.8 to 1.2, or (b) below 0.1 and from 0.9 to\n    1.1. Reproduced when, under one combination, more than half of the neurons fall between\n    the extremes, below the ring value, and fewer than a quarter fall in each extreme.\n  depends_on:\n  - fig6a-excitatory-on-plane\n- id: fig7a-no-corr-prediction-hv\n  statement: Prediction performance is not significantly correlated with the\n    horizontal-vertical ratio.\n  source: Results, Excitatory spectral receptive fields of most MT neurons form a partial ring\n    in the plane, paragraph 2\n  quote: Note that there was no significant correlation between prediction performance and the\n    horizontal–vertical ratio\n  statistics:\n  - p: 0.1\n    p_relation: \">\"\n    n: 52 neurons\n  criterion: A claim of absence. The paper names no test here; the test it names for the\n    correlation of Figure 7C, the t test for a Pearson correlation coefficient, is used,\n    between each neuron's prediction correlation (fig3b-mean-prediction) and its\n    horizontal-vertical ratio (fig7a-partial-ring). Reproduced when p > 0.10, the bound the\n    paper reports; not reproduced when p < 0.05; between the two is reported as partially\n    reproduced. The coefficient is given either way.\n  depends_on:\n  - fig3b-mean-prediction\n  - fig7a-partial-ring\n- id: fig7b-pattern-index\n  statement: Simulated plaid responses give pattern indices that form a continuum, mostly from\n    -6 to 2, with highly pattern-selective neurons rare (the Discussion says none were extremely\n    pattern selective).\n  source: Results, The horizontal-vertical ratio is correlated with simulated pattern\n    selectivity, paragraphs 2 and 3; Figure 7B; Discussion, paragraph 4\n  quote: The pattern index for most neurons ranges from\n  criterion: Each neuron's fitted compressive and divisive model is driven with drifting\n    gratings and plaids, and the pattern index of Smith et al. (2005) is computed (the\n    Fisher-transformed partial correlation with the pattern prediction minus that with the\n    component prediction). The paper gives no stimulus parameters. Open details, with readings.\n    Grating and plaid spatial and temporal frequency, (a) at each neuron's peak excitatory\n    spectral response, (b) one frequency pair for all neurons near the population peak.\n    Plaid component separation, (a) 120 degrees as in Smith et al. (2005) and Rust et al.\n    (2006), (b) 90 degrees. Directions in 12 steps of 30 degrees, matching the filter bank, as\n    a standard choice. Reproduced when, under one combination, more than half of the neurons\n    have indices from -6.6 to 2.2 (the range widened by 10%) and fewer than 10% exceed 2.2\n    (rare is not quantified; 10% is this file's reading, and the count above 1.28, the\n    pattern-cell bound of Smith et al., 2005, is reported as well).\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig7c-hv-pattern-correlation\n  statement: The horizontal-vertical ratio is significantly correlated with the simulated\n    pattern index (r = 0.46).\n  source: Results, The horizontal-vertical ratio is correlated with simulated pattern\n    selectivity, paragraph 3; Figure 7C\n  quote: The correlation between the two indices is significant\n  statistics:\n  - test: t test for correlation coefficients\n    statistic: r = 0.46\n    p: 0.01\n    p_relation: \"<\"\n    n: 52 neurons\n  expected:\n  - quantity: Pearson correlation between horizontal-vertical ratio and pattern index\n    value: 0.46\n    tolerance: 0.046\n  criterion: Pearson correlation across neurons between the ratio of fig7a-partial-ring and the\n    index of fig7b-pattern-index, tested by the t test for a correlation coefficient.\n    Reproduced when, under one combination of the readings of those claims, r is within\n    tolerance and p < 0.01; partially reproduced when r is positive and p < 0.01 but outside\n    tolerance.\n  depends_on:\n  - fig7a-partial-ring\n  - fig7b-pattern-index\n- id: fig7c-no-corr-prediction-pattern\n  statement: Prediction performance is not significantly correlated with the pattern index.\n  source: Results, The horizontal-vertical ratio is correlated with simulated pattern\n    selectivity, paragraph 3\n  quote: There was no significant correlation between prediction performance and the pattern\n    index\n  statistics:\n  - p: 0.1\n    p_relation: \">\"\n    n: 52 neurons\n  criterion: A claim of absence, judged as in fig7a-no-corr-prediction-hv (t test for a Pearson\n    correlation), between prediction correlation and pattern index.\n  depends_on:\n  - fig3b-mean-prediction\n  - fig7b-pattern-index\n- id: natural-movie-control\n  statement: Models fit on motion-enhanced movies predict responses to natural movies without\n    motion enhancement as well as responses to new motion-enhanced movies (mean r = 0.533\n    against 0.537, 15 neurons).\n  source: Results, Control to identify any bias arising from the use of motion-enhanced natural\n    movies, paragraph 2\n  quote: Receptive field models of area MT neurons estimated using motion-enhanced natural movies\n    predicted responses to novel simple natural movies just as well as they predicted responses\n    to novel motion-enhanced natural movies\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.1\n    p_relation: \">\"\n    n: 15 neurons\n  expected:\n  - quantity: mean prediction correlation, natural movies\n    value: 0.533\n    tolerance: 0.053\n  - quantity: mean prediction correlation, motion-enhanced movies\n    value: 0.537\n    tolerance: 0.054\n  criterion: A claim of absence, judged on the paper's test. For the neurons with both\n    validation sets, the compressive and divisive model fit on the motion-enhanced training\n    data predicts each set; per-neuron correlations compared by a Wilcoxon signed-rank test.\n    Reproduced when p is not below 0.05 and both means are within tolerance; partially\n    reproduced when the test finds no difference but a mean is outside tolerance. Needs the\n    natural-movie validation responses of the 15 neurons; if the dataset lacks them, the\n    claim is blocked as data missing.\n  depends_on:\n  - fig3b-mean-prediction\n- id: fig8-recovery-simulated\n  statement: The estimation procedure correctly recovers the spectral receptive fields of three\n    simulated MT neurons, one narrowband, one non-planar with four directions at one frequency,\n    and one with random directions and frequencies that does not avoid low temporal\n    frequencies.\n  source: Results, Control to ensure that the model estimation procedure can recover spectral\n    receptive fields of any shape, paragraph 2; Figure 8\n  quote: These results demonstrate that the receptive field estimation procedure used in this\n    study can characterize arbitrary spectral receptive fields, regardless of their\n    organization within the three-dimensional frequency domain\n  criterion: Three simulated neurons built from the compressive and divisive filter outputs\n    with excitatory weights only (Figure 8 legend), as (A) filters in a narrow band of spatial\n    and temporal frequency, (B) four directions at one spatial and temporal frequency, (C) many\n    filters at random direction and frequency. Their responses to the experiment's movies are\n    refit by the same procedure and spectral receptive fields compared. The paper judges this\n    by eye and gives no noise level, filter counts or measure. Readings for noise are (a)\n    Poisson noise as in the null model of fig6a-null-on-plane, (b) none. Reproduced when, for\n    each simulated neuron, its recovered spectral receptive field correlates better with its\n    own true spectral receptive field than with those of the other two (a measure this file\n    fixes, as the paper names none); the correlations are reported.\n  depends_on:\n  - fig3b-mean-prediction\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/  quote: The pattern index for most neurons ranges from$/  quote: The pattern index for most neurons ranges from ... 6 to 2, and highly pattern-selective\n    neurons are relatively rare/' claims/nishimoto-2011.yaml && grep -n -A2 "pattern index for most" claims/nishimoto-2011.yaml; python tools/claims_check.py claims/nishimoto-2011.yaml paper/10.1523-jneurosci.6801-10.2011.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "—|rather" claims/nishimoto-2011.yaml; grep -n -E "^\s+[a-z_]+: .*: " claims/nishimoto-2011.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/nishimoto-2011.yaml'))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"; git status --short
```

```
11 20 11
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
?? claims/nishimoto-2011.yaml
?? scripts
```

**Agent**

I wrote `claims/nishimoto-2011.yaml`. The quote checker reports 20 claims, 20 quotes, 11 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (`paper/10.1523-jneurosci.6801-10.2011.txt`), with the main text, Materials and Methods and figure legends. The paper has no supplement apart from Movie 1, which shows stimulus spectra and is not a result. I opened the PDF only for:
- the inequality signs of the p-values, which the extraction garbled;
- the bar heights in Figure 2B, which print no numbers.

The paper links no code, so there was no repository or commit to read.

**Claims:** 20. All 20 have quotes, none is inferred, 11 record statistics, 11 have expected values and all 20 have criteria. They cover:
- **Prediction accuracy:** mean r = 0.52; 35% of explainable variance; an example neuron with r = 0.72.
- **Model comparison in Figure 2B:** luminance and contrast normalization has no significant effect; the compressive nonlinearity helps (about +16% and +19%); the expansive one hurts (about −36% and −24%); divisive normalization helps (about +8%); compressive plus divisive beats compressive alone; the effects do not depend on divisive normalization.
- **Complex cells:** they carry most of the response variance (the paper shows no data for this).
- **On-plane ratio:** excitatory 0.59 against a null of 0.36; suppressive 0.18.
- **Ring structure:** most neurons have a horizontal-vertical ratio between the extremes (partial rings).
- **Plaid simulation:** pattern indices mostly from −6 to 2; correlation with the horizontal-vertical ratio r = 0.46.
- **Two absence claims:** prediction performance is not correlated with the horizontal-vertical ratio or with the pattern index.
- **Controls:** the natural-movie control (r = 0.533 against 0.537); recovery of simulated receptive fields in Figure 8.

**Details the paper leaves open, with the readings named:**
- **cRF size:** half the stored patch, or the full patch as the analysis window.
- **Delays:** "10 frames or 130 ms" disagree at 83 Hz, so 0 to 10 frames or 1 to 10.
- **12 ms Gaussian:** its SD or its full width at half maximum.
- **Semisaturation constant:** chosen on held-out training data, or fixed.
- **20% hold-out parts:** contiguous blocks or random frames.
- **Compressive power:** applied to all filter outputs (taken), with simple cells only as a variant.
- **Gabor details:** the temporal width and the exact velocities are not given; I used a standard choice.
- **"Increase of predictive power":** the change in mean r, in mean r², or per-neuron change, averaged.
- **Bonferroni count:** 11 or 5 comparisons.
- **Explainable variance:** two ways of averaging the David and Gallant (2005) noise ceiling.
- **On-plane ratio:**
  - balance of the two constraints, which the authors set by hand: coverage only, or both summed with equal weight;
  - what is summed: weights, or weights times spectral amplitude;
  - where the sign is split: per delay, or after summing over delays.
- **Null model:** which neuron's movies it is driven with, how rates are scaled for the Poisson noise, which delays the random weights span, and whether the suppressive test compares against the null's excitatory or suppressive ratios.
- **Horizontal-vertical ratio:** which amplitudes count as on the plane, and where the "extremes" end (0.2/0.8 or 0.1/0.9).
- **Plaid simulation:** grating and plaid frequencies (per neuron or shared) and component separation (120° or 90°).
- **Figure 8:** noise level, and the comparison measure (the file fixes one, since the paper names none).
- **Thresholds the paper gives as words only:** "most variance" for the complex-cell claim and "rare" for pattern-selective neurons are set by the file and say so.

**What the paper does not give, or contradicts:**
- **No numbers for Figure 2B.** Its values are read from the bars with a 4-point tolerance, and the reason is stated in the file.
- **Contradictions:**
  - The Methods say 20,000 to 40,000 training frames; the Results say 22,000 to 42,000.
  - Figure 2's legend says open bars are models with luminance normalization and filled bars without it; the figure's own key shows the reverse.
- **Possible data gaps, left for the author to check:**
  - The dataset holds 45 neurons; the paper used 52.
  - The explainable-variance claim needs the single validation repeats. The dataset's description lists only averaged PSTHs, so if the repeats are absent that claim is blocked.
  - The natural-movie control needs the second validation set for the 15 neurons; the same applies.

The working tree also shows untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.

## End of run

23 turns, 4 minutes, $1.47 at API prices, result: success.
