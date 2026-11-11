# asari-2009 · claims · run 42850060203

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^## \|^# " docs/protocol.md | head -50; ls paper/; ls claims | head
```

Result: not kept, because it reads the paper's text.

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
cat claims/fouke-2025.yaml; cat paper/ac-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/10.1152-jn.00577.2009.txt; cat papers/datasets/asari-2009.yaml 2>/dev/null; ls claims | grep -i machens
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 800,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 1600,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/asari-2009.yaml 2>/dev/null; ls papers/datasets | grep -i -e machens -e asari; ls claims | grep -i machens; grep -n "asari\|machens" papers/keys.yaml; sed -n 1,80p tools/claims_check.py | head -60
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1152/jn.00577.2009
title: Long-Lasting Context Dependence Constrains Neural Encoding Models in Rodent Auditory Cortex
datasets:
- archive: crcns
  id: ac-1
  relation: primary
asari-2009.yaml
225:  10.1152/jn.00577.2009: asari-2009
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"
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
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm; pdftoppm -r 110 -f 10 -l 12 -png paper/10.1152-jn.00577.2009.pdf pg && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1152-jn.00577.2009.pdf')
for i in [9,10,11,13,15,16]:
    d[i].get_pixmap(dpi=110).save(f'pg{i+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

Rendering tools aren't installed; I'll read the PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.pdf",
 "pages": "10-12"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.pdf",
 "pages": "14-17"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -t claims | head -5; head -30 claims/$(ls -t claims | head -1)
```

```
zhuang-2025.yaml
zhu-2022.yaml
yu-2017.yaml
yuan-2025.yaml
yu-2016
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
[... 15 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/asari-2009.yaml",
 "content": "# Claims for Asari & Zador (2009), J Neurophysiol 102:2638-2656, on CRCNS ac-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or\n# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.\n#\n# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with\n# the PDF. The extraction garbles some symbols (Greek letters, \"<\", \">\", \"~\", \"=\" and \"+/-\" print\n# as a replacement glyph); they were read from context, and quotes are cut around them. The PDF\n# pages could not be rendered in this run, so figure axes were not read; every value used here is\n# printed in the text or a legend. The online supplement (Supplemental Figures S1 to S10) was not\n# supplied and was not read. The main findings rest on the main-text Figures 2 to 9 and their\n# legends; the supplement holds example traces (S2 to S10) and the \"silence probe\" analysis (S1),\n# whose one claim (figs1-silence-probe) is quoted from the Methods only.\n#\n# Code read: none. The paper links no code; it says all analysis was done in MATLAB.\n#\n# Data the paper used. Long-Evans rats, 20 to 28 days old, anesthetized with ketamine and\n# medetomidine; in vivo blind patch recordings sampled at 10 kHz.\n# - A1 current clamp (whole cell): 194 cells in 139 animals, of which 123 met the analysis\n#   criterion (at least 4 repeats of a probe tested with at least 2 conditioning stimuli). By\n#   stimulus ensemble, 39 cells with natural sounds, 14 with TORCs, 6 with DMRs, 39 with\n#   modulated harmonic tones (MHT) and 27 with modulated colored noise (MCN). Membrane potential;\n#   spikes clipped with a 10-ms median filter, traces centered to zero mean.\n# - A1 voltage clamp: 42 cells in 17 animals, 14 analysed (natural sounds, 29 probes), three\n#   holding potentials in pseudorandom order, Cs-free internal with QX-314 and BAPTA, 10 test\n#   pulses before the sounds; excitatory and inhibitory conductances derived from the currents.\n# - MGB (ventral division) cell-attached: 16 cells in 5 animals, 14 analysed (93 natural sound\n#   probes, at least 10 repeats). Spikes.\n# - STRF analysis (Figure 4): 20 A1 cells recorded by M. Wehr for Machens et al. (2004),\n#   reanalysed. The dataset description says ac-1 holds both Wehr's and Asari's data.\n# Stimuli: natural sounds (46 animal sounds from two Cornell CDs, mostly 3.5 to 6.5 s), and\n# synthetic ensembles (TORC, DMR, MHT, MCN, 4.0 to 5.5 s) in which one property (amplitude,\n# frequency, AM, FM, or higher-order structure) varies among conditioning stimuli. Sequences of\n# N fragments (typically N = 7) follow a cyclic code so every ordered pair and every fragment\n# after \"silence\" occurs; no gap between fragments, about 6 s between sequences. Each fragment is\n# a probe for the one before it (its context, which may be silence). Table 1 gives the number of\n# probes per ensemble and property.\n#\n# Method details fixed by the paper and used below (Methods, Analysis):\n# - Significance measure. At each 0.1-ms time point of a probe, a Kruskal-Wallis test across\n#   contexts of the trial responses; a time point is significant when P < 0.01 holds for at least\n#   5 ms (50 consecutive points). Noise floor from 1000 shuffles of trials across contexts per\n#   probe, averaged over the population. Population curve is the proportion of probes\n#   significant at each time after probe onset.\n# - Fractional power measure. Eqs. 17 to 20, population averages over probes at each time point;\n#   the denominator (stimulus-related power, Eq. 17) is smoothed by a running mean over [0, 2t]\n#   before taking the ratio Q(t). Response predictability (Fig. 4) is Eq. 43, context-independent\n#   power (Eq. 18) over stimulus-related power (Eq. 17).\n# - Exponential fits (Eq. 44) with MATLAB lsqcurvefit; an exponential is kept only if its size\n#   is at least one tenth of the total size.\n# Details the paper leaves open, used by several claims, are named in each criterion: the time\n# range over which population curves are formed and fitted (probes differ in length), which\n# probes count at a time t past the end of a short probe, whether \"silence\" counts among the\n# contexts of Figures 3 and 4, and the start values and bounds of the fits.\nschema_version: 2\npaper: doi:10.1152/jn.00577.2009\nclaims:\n- id: methods-recording-counts\n  statement: Of 194 A1 cells recorded in current clamp, 123 met the analysis criterion (39 tested\n    with natural sounds, 14 with TORCs, 6 with DMRs, 39 with modulated harmonic tones, 27 with\n    modulated colored noise); 14 of 42 voltage-clamped cells and 14 of 16 MGB cells were analysed.\n  source: Methods, Electrophysiology, paragraphs 2 and 3; Table 1\n  quote: All together, we recorded from 194 cells in 139 animals in current-clamp mode, of which\n    123 cells met our criterion for the analysis ... Of these, 39 cells were examined with natural\n    sound ensembles, 14 cells with ensembles of temporally orthogonal ripple combinations, 6 cells\n    with ensembles of dynamic moving ripples, 39 cells with ensembles of modulated harmonic tones,\n    and 27 cells with ensembles of modulated colored noise ensembles\n  expected:\n  - quantity: A1 current-clamp cells meeting the criterion\n    value: 123\n    tolerance: 0\n  - quantity: A1 cells with natural sound ensembles (current clamp)\n    value: 39\n    tolerance: 0\n  - quantity: natural sound probes in A1 current clamp (Table 1, all properties)\n    value: 305\n    tolerance: 0\n  - quantity: voltage-clamp probes analysed\n    value: 29\n    tolerance: 0\n  - quantity: voltage-clamp cells analysed\n    value: 14\n    tolerance: 0\n  - quantity: MGB probes analysed\n    value: 93\n    tolerance: 0\n  - quantity: MGB cells analysed\n    value: 14\n    tolerance: 0\n  criterion: Counts of cells and probes passing the paper's inclusion rule (Methods, Context\n    dependence at subthreshold voltage level; Table 1 legend), at least two conditioning stimuli\n    each with at least 4 trials (current clamp), at least 2 trials at all three holding\n    potentials (voltage clamp) and at least 10 trials (MGB). Tolerance 0 for counts, as they\n    define the sample; a count that differs is reported with the probes that make the\n    difference. The paper does not say whether \"silence\" counts as one of the two conditioning\n    stimuli; both readings (counted, not counted) are run, and the claim holds under either. The\n    counts per cell for the other ensembles (TORC, DMR, MHT, MCN) and Table 1 rows are reported.\n    Recordings in the dataset that are not in the paper (fewer repeats) are expected and are not\n    a failure.\n\n- id: a1-mgb-firing-rates\n  statement: Firing rates were low in A1 (spontaneous 0.47 +/- 0.61 Hz, evoked 0.57 +/- 0.77 Hz,\n    mean +/- SD, 194 cells) and high in MGB (spontaneous 0.78 +/- 1.25 Hz, evoked 11.4 +/- 16.9\n    Hz, 16 cells).\n  source: Methods, Analysis, paragraphs 2 and 3; Results, Context dependence, paragraph 1;\n    Results, Subcortical contribution to context dependence, paragraph 2\n  quote: Because of the low firing rates in A1 (spontaneous, 0.47 ... 0.61 Hz; evoked, 0.57 ...\n    0.77 Hz ... 194 cells ... Sufficiently high firing rates in MGB allowed us to analyze the\n    context dependence at the spike level (spontaneous, 0.78 ... 1.25 Hz; evoked, 11.4 ... 16.9 Hz\n  expected:\n  - quantity: A1 spontaneous rate, mean over cells\n    value: 0.47\n    tolerance: 0.047\n    unit: Hz\n  - quantity: A1 evoked rate, mean over cells\n    value: 0.57\n    tolerance: 0.057\n    unit: Hz\n  - quantity: MGB spontaneous rate, mean over cells\n    value: 0.78\n    tolerance: 0.078\n    unit: Hz\n  - quantity: MGB evoked rate, mean over cells\n    value: 11.4\n    tolerance: 1.14\n    unit: Hz\n  criterion: Tolerances are 10% of each mean; the printed SDs (0.61, 0.77, 1.25, 16.9 Hz) are the\n    spread over cells, not an uncertainty of the mean, and are reported for comparison (within\n    10% of each). Spikes in MGB are extracted by a high-pass filter and a threshold with spike\n    times at the peaks (Methods, Analysis, paragraph 3). The paper fixes neither the filter\n    cutoff, the threshold, nor how A1 spikes were detected, nor the windows for \"spontaneous\"\n    (readings are the intersequence silence, about 6 s, or a pre-stimulus baseline) and \"evoked\"\n    (readings are all sound periods, or the probe periods analysed). The author runs a standard\n    detector on each reading of the windows; reproduced when the four means are within tolerance\n    under one reading, partially reproduced when the A1 means are below 1 Hz and the MGB evoked\n    mean above 5 Hz but some means fall outside tolerance.\n\n- id: fig2-example-reliability\n  statement: The example A1 neuron of Figure 2 had high trial-to-trial reliability (correlation\n    across trials 0.74 +/- 0.08 for the shown probe and 0.61 +/- 0.07 over the seven natural sound\n    fragments tested), and the mean correlation over the population was 0.31 +/- 0.09.\n  source: Results, Context dependence, paragraph 2; Figure 2A legend\n  quote: the correlation coefficient of the response traces across trials in a given context was\n    0.61 ... 0.07 (mean ... SD) for the seven natural sound fragments tested in this cell. The\n    reliability varied within a given neuron as a function of the stimuli tested and across\n    neurons; the mean correlation coefficient was 0.31 ... 0.09\n  expected:\n  - quantity: population mean trial-to-trial correlation coefficient\n    value: 0.31\n    tolerance: 0.09\n  - quantity: example cell, correlation over its seven natural sound fragments\n    value: 0.61\n    tolerance: 0.07\n  - quantity: example cell, correlation for the shown probe\n    value: 0.74\n    tolerance: 0.08\n  criterion: Tolerances are the stated SDs, as the paper gives them as the spread of the values\n    (protocol, expected). The correlation is between response traces (median-filtered, zero-mean\n    membrane potential) of trials within one context, over a probe. The paper does not say\n    whether the coefficient is the mean over all pairs of trials or the correlation of each trial\n    with the mean of the others, nor what the population mean is taken over (cells, or probes);\n    each reading is run. The example cell is not identified; the author looks for a current-clamp\n    cell tested with seven natural sound fragments over six repeats, and the example values are\n    not tested when no cell can be matched. The population value decides the claim.\n\n- id: fig2-example-long-context\n  statement: In an example A1 neuron, changing the conditioning stimulus changed the response to\n    the probe for about 4 s; responses did not differ between 2 and 4 s after probe onset and\n    diverged again after about 4 s.\n  source: Figure 2B and 2D; Results, Context dependence, paragraph 3\n  quote: Interestingly, context-induced differences could sometimes be intermittent; the three\n    average response traces showed no difference in the interval 2 to 4 s after the onset of the\n    probe, but diverged again after about 4 s\n  statistics:\n  - test: Kruskal-Wallis test at each time point, P < 0.01 for at least 5 ms\n    p: 0.01\n    p_relation: \"<\"\n    n: one cell, one probe in three contexts, 6 trials each\n  criterion: The significance measure of the Methods (Kruskal-Wallis across the three contexts at\n    each time point, significant where P < 0.01 holds for at least 50 consecutive 0.1-ms points).\n    The cell and probe are not identified; the author looks for a current-clamp cell with seven\n    natural sound fragments and a probe tested after silence and two other fragments over six\n    trials. Reproduced when, for the matched probe, significant periods occur both before 2 s and\n    after 4 s and none between 2 and 4 s; not testable when no probe matches. As a weaker check\n    that does not need the example, the number of natural sound probes with a significant period\n    later than 4 s is reported.\n\n- id: fig3a-proportion-significant\n  statement: Of 305 natural sound probes tested in 39 A1 cells with typically five to eight\n    natural sound contexts, 204 (66.9%) showed significant context dependence, and about a quarter\n    (23.7%) of the significant events occurred more than 1 s after probe onset.\n  source: Results, Context dependence, paragraph 6; Figure 3A\n  quote: Of 305 natural sound probe stimuli tested with different ... typically around five to\n    eight ... natural sound contexts in 39 cells, significant effects were observed in 204 probes\n    (66.9%; Fig. 3A), and about a quarter (23.7%) of the events occurred longer than one second\n    after the onset of a probe stimulus\n  expected:\n  - quantity: probes with significant context dependence\n    value: 204\n    tolerance: 20.4\n  - quantity: fraction of probes with significant context dependence\n    value: 0.669\n    tolerance: 0.0669\n  - quantity: fraction of significant events later than 1 s after probe onset\n    value: 0.237\n    tolerance: 0.0237\n  depends_on:\n  - methods-recording-counts\n  criterion: A probe is significant when the significance measure (Methods) finds at least one\n    period with P < 0.01 for at least 5 ms. The late fraction follows the Figure 3A legend, one\n    minus the cumulative probability at 1 s, where the cumulative probability is the running\n    integral of the proportion curve less the noise floor (1000 shuffles per probe), normalized\n    at its peak (4.72 s in the paper). Open and run as readings, whether \"silence\" counts among\n    the contexts (Figure 2B includes it, so the main reading counts it), and whether the\n    proportion at time t is over all 305 probes or over the probes still running at t.\n    Reproduced when, under one reading, all three values are within tolerance; partially\n    reproduced when the count is within tolerance and the late fraction is not.\n\n- id: fig3a-significance-decay\n  statement: The proportion of probes with significant context dependence decays after probe\n    onset as the sum of two exponentials (sizes 0.17 and 0.09, decay constants 0.20 and 0.90 s),\n    above a noise floor of about 2.8 x 10^-3.\n  source: Figure 3A legend, bottom panel; Results, Context dependence, paragraph 7\n  inferred: The fit values are in the Figure 3A legend, where the symbols are garbled in the text\n    extraction (read as alpha1 = 0.17, tau1 = 0.20 s, alpha2 = 0.09, tau2 = 0.90 s, kappa = mean\n    noise floor = 2.8 x 10^-3); the Results restate the long constant as about one second.\n  expected:\n  - quantity: fast decay size alpha1\n    value: 0.17\n    tolerance: 0.017\n  - quantity: fast decay constant tau1\n    value: 0.20\n    tolerance: 0.02\n    unit: s\n  - quantity: slow decay size alpha2\n    value: 0.09\n    tolerance: 0.009\n  - quantity: slow decay constant tau2\n    value: 0.90\n    tolerance: 0.09\n    unit: s\n  - quantity: mean noise floor over time\n    value: 0.0028\n    tolerance: 0.00028\n  depends_on:\n  - fig3a-proportion-significant\n  criterion: Eq. 44 with the constant fixed at the mean noise floor over time, fitted by least\n    squares (lsqcurvefit) to the proportion curve from probe onset, with the paper's rule for the\n    number of exponentials (each size at least a tenth of the total). The fit range is not given;\n    readings are 0 to 4.72 s (the peak of the cumulative curve in the legend) and 0 to 6 s (the\n    plotted range). Start values and bounds are not given; a grid of start values is used and the\n    best fit kept, a standard choice. Reproduced when, under one reading, two exponentials are\n    selected and every value is within tolerance; partially reproduced when two are selected and\n    the slow constant is between 0.5 and 2 s but some values are outside tolerance.\n\n- id: fig3b-fractional-power-decay\n  statement: The context-dependent fraction of the stimulus-related response power, normalized\n    by the smoothed stimulus-related power, decays from about 0.49 with a time constant of about\n    1.04 s.\n  source: Figure 3B legend, bottom panel; Results, Context dependence, paragraph 7\n  quote: For both measures there was a long decay constant of about one second\n  expected:\n  - quantity: decay size alpha1 of the normalized context-dependent power\n    value: 0.49\n    tolerance: 0.049\n  - quantity: decay constant tau1\n    value: 1.04\n    tolerance: 0.104\n    unit: s\n  depends_on:\n  - methods-recording-counts\n  criterion: Q(t) of Eq. 20 from the 305 natural sound probes, numerator Eq. 19 and denominator\n    Eq. 17 averaged over probes at each time point, the denominator smoothed by a running mean over\n    [0, 2t] before the division; one exponential with constant 0 fitted (Figure 3B legend). The\n    same open details as fig3a-proportion-significant (silence as a context; which probes enter\n    the average at time t) and the fit range (0 to 4 s, 0 to 6 s) are run as readings. The\n    printed values in the legend are garbled in the text extraction and read as alpha1 = 0.49,\n    tau1 = 1.04 s with kappa = 0, which the Results (1.04 s) and Figure 4 legend confirm.\n    Reproduced when both are within tolerance under one reading.\n\n- id: timescale-longer-than-membrane\n  statement: The trial-to-trial noise autocorrelation and the autocorrelation of spontaneous\n    activity decay within about 100 ms, much faster than the second-long timescale of context\n    dependence in A1.\n  source: Methods, Analysis, Timescale of intrinsic membrane properties; Results, Context\n    dependence, paragraph 7\n  quote: we found that ... had a sharp peak with a rapid decay (within ... 100 ms; data not shown),\n    much faster than the slow timescale identified in neural responses in area A1\n  criterion: Noise is the residual of each trial from its context mean (Eq. 14), its\n    autocorrelation normalized by the noise variance (Eq. 45), averaged over trials and probes of\n    the natural sound current-clamp data; spontaneous activity is taken from the intersequence\n    intervals, which the paper names as the silent periods. \"Decay\" is not defined; the reading\n    used is the lag at which the mean autocorrelation first falls below 1/e, with the lag where it\n    falls below 0.1 shown as a variant. Reproduced when both lags are under 150 ms for both noise\n    and spontaneous activity under the 1/e reading, and the 1/e lag is below a third of 1.04 s.\n\n- id: fig4-predictability-upper-bound\n  statement: Without knowledge of the context, no model can capture more than about half (0.51)\n    of the predictable response power with a window of about 100 ms; the upper bound approaches\n    one only with a window of seconds (time constant 1.04 s).\n  source: Results, Relation to response predictability, paragraph 4; Figure 4 legend\n  quote: shows that no model can capture more than a half\n  expected:\n  - quantity: upper bound on model performance near probe onset (1 minus alpha1)\n    value: 0.51\n    tolerance: 0.051\n  - quantity: time constant of the approach to one\n    value: 1.04\n    tolerance: 0.104\n    unit: s\n  depends_on:\n  - methods-recording-counts\n  criterion: Eq. 43 at each time after probe onset, context-independent power (Eq. 18) over\n    stimulus-related power (Eq. 17), both averaged over the 305 natural sound probes in 39 cells;\n    the Methods (Eq. 20) say the denominator is smoothed over [0, 2t] before Eq. 43 too, which is\n    the main reading, with the unsmoothed ratio as a variant. One exponential with constant 1\n    fitted (Figure 4 legend, alpha1 = -0.49, tau1 = 1.04 s). The open details of\n    fig3a-proportion-significant and fig3b-fractional-power-decay are run as readings.\n    Reproduced when, under one reading, 1 + alpha1 and tau1 are within tolerance.\n\n- id: fig4-strf-performance-low\n  statement: Linear STRF models of 20 A1 cells from Machens et al. (2004) predicted less than\n    about 20% of the predictable response power, and extending the window from 180 ms to about 4 s\n    did not improve them significantly, with or without a static nonlinearity; the LN model did\n    only slightly better.\n  source: Results, Relation to response predictability, paragraph 5; Figure 4; Discussion, Context\n    dependence and model construction, paragraph 4\n  quote: The performance of STRF-based models was in general unsatisfactory ... consistent with\n    previous work (Ahrens et al. 2008; Machens et al. 2004; Sahani and Linden 2003). The\n    performance did not improve significantly, however, when we extended the window length\n  expected:\n  - quantity: STRF model performance at any window length, upper bound\n    value: 0.2\n    tolerance: 0.02\n  criterion: Per the Methods (Neural encoding models; Model performance), the 20 Wehr cells of\n    Machens et al. (2004), spectrogram (Eq. 47) at 3 bins per octave from 0.40 to 22 kHz (17\n    bins), time bins of 2^k ms for k = 2 to 10 with 45 bins split as the Methods list, giving\n    windows of 180, 324, 548, 884, 1364, 2004, 2772, 3540 and 4052 ms (765 parameters); ridge\n    regression (Eq. 50) with 10-fold cross-validation choosing the ridge parameter on the\n    validation fold; LN by robust lowess (5% span, 5 iterations) on the training set; performance\n    by Eq. 53 on training (upper) and validation (lower) data, averaged over cells. Open, with\n    readings run, the spectrogram window h(t) (readings 10-ms and 20-ms Hann), the response\n    sampling (4-ms bins, the finest time bin, or the 10-kHz trace), the range of ridge values (a\n    log grid wide enough that the best value is interior, a standard choice), and how folds are\n    formed (contiguous blocks, or by stimulus). \"Did not improve significantly\" names no test;\n    the readings are a paired comparison over cells of validation performance at 4052 ms against\n    180 ms by Wilcoxon signed-rank and a one-way repeated-measures test over the nine windows,\n    each at 0.05. Reproduced when, under one reading, the mean validation performance is at most\n    0.22 at every window for STRF and LN and neither test finds an improvement; the mean training\n    performance and the LN gain are reported.\n\n- id: fig5-example-conductances\n  statement: In an example voltage-clamped A1 cell, excitatory and inhibitory conductances evoked\n    by the probe decayed within about 100 ms in all six contexts, yet their variance over contexts\n    lasted long, longer for inhibition than for excitation.\n  source: Results, Context dependence of synaptic conductances, paragraph 2; Figure 5D to 5G\n  quote: In all cases we examined, both excitatory and inhibitory conductances elicited in this\n    cell decayed rapidly within about 100 ms, yet the context dependence measured as the variance\n    of the conductances lasted long, especially for the inhibitory conductance in this example\n  criterion: The cell is not identified; the author looks for a voltage-clamp cell with one probe\n    tested after six contexts at holding potentials near -97, -67 and -37 mV (Figure 5B labels).\n    Conductances as in Methods (Eqs. 22 to 29; Vjp -12 mV, Eexc 0 mV, Einh -85 mV, Rs from the\n    median peak transient of the 10 test pulses, Rin from their steady-state current, baseline\n    as the 90th percentile of each trial's current). Reproduced when, for the matched probe, the\n    variance over contexts (Eq. 30 without population average) of the inhibitory conductance\n    stays above the spontaneous noise variance for longer than that of the excitatory\n    conductance; not testable when no cell matches. The population claim fig6-conductance-decay\n    carries the finding.\n\n- id: fig6-conductance-decay\n  statement: Across 29 probes in 14 voltage-clamped cells, context dependence of both excitatory\n    and inhibitory conductances decayed with a long constant of seconds (1.22 and 2.50 s) and a\n    short one of hundreds of milliseconds (0.14 and 0.13 s).\n  source: Results, Context dependence of synaptic conductances, paragraph 3; Figure 6A and 6B\n  quote: For both excitatory and inhibitory conductances, there was a long decay constant on the\n    order of seconds\n  expected:\n  - quantity: excitation, fast size alpha1\n    value: 0.28\n    tolerance: 0.028\n  - quantity: excitation, fast constant tau1\n    value: 0.14\n    tolerance: 0.014\n    unit: s\n  - quantity: excitation, slow size alpha2\n    value: 0.08\n    tolerance: 0.008\n  - quantity: excitation, slow constant tau2\n    value: 1.22\n    tolerance: 0.122\n    unit: s\n  - quantity: excitation, constant kappa\n    value: 0.02\n    tolerance: 0.002\n  - quantity: inhibition, fast size alpha1\n    value: 0.48\n    tolerance: 0.048\n  - quantity: inhibition, fast constant tau1\n    value: 0.13\n    tolerance: 0.013\n    unit: s\n  - quantity: inhibition, slow size alpha2\n    value: 0.14\n    tolerance: 0.014\n  - quantity: inhibition, slow constant tau2\n    value: 2.50\n    tolerance: 0.25\n    unit: s\n  - quantity: inhibition, constant kappa\n    value: 0.10\n    tolerance: 0.01\n  depends_on:\n  - methods-recording-counts\n  criterion: Per the Methods (Context dependence at synaptic input level), conductances for each\n    context by regression of Eq. 22 across the three holding potentials at each time point, then\n    split by Eqs. 28 and 29; variance over contexts with the n - 1 denominator (Eq. 31) averaged\n    over the 29 probes, less the noise variance from the spontaneous activity (Eq. 30); two\n    exponentials with a free constant fitted (Figure 6 legend; sizes in nS^2, as plotted). Open,\n    with readings run, the period taken as spontaneous (intersequence silence, or the period\n    before the sound after the test pulses), any smoothing of the conductances (none, or a 1-ms\n    mean, a standard choice), and the fit range (0 to 4 s, 0 to 6 s). Reproduced when, under one\n    reading, two exponentials are selected for each and the four decay constants are within\n    tolerance; partially reproduced when both slow constants exceed 1 s and both fast ones are\n    below 0.3 s. The sizes are reported against their values but do not decide the claim, since\n    the Methods say the conductance strengths are biased by the space clamp.\n\n- id: fig8a-proportion-by-property\n  statement: When only one property of synthetic conditioning stimuli varied, context dependence\n    was found in 77 of 95 probes (81.1%, 31 cells) for amplitude, 73 of 110 (35 cells) for\n    frequency, 62 of 96 (64.6%, 27 cells) for AM, 47 of 82 (57.3%, 25 cells) for FM and 59 of 137\n    (43.1%, 27 cells) for higher-order properties.\n  source: Results, Relation to stimulus properties, paragraphs 2 and 3; Figure 8A\n  quote: we observed context-dependent effects in 77 probes (81.1%) of 95 probes (tested in 31\n    cells) and in 73/110 (64.6%; 35 cells), respectively (Fig. 8A) ... Context-dependent effects\n    were observed in 62/96 (64.6%; 27 cells) for AM modulation; in 47/82 (57.3%; 25 cells) for FM\n    modulation; and in 59/137 (43.1%; 27 cells) for colored noise modulation\n  expected:\n  - quantity: amplitude, significant probes of 95\n    value: 77\n    tolerance: 7.7\n  - quantity: frequency, significant probes of 110\n    value: 73\n    tolerance: 7.3\n  - quantity: AM, significant probes of 96\n    value: 62\n    tolerance: 6.2\n  - quantity: FM, significant probes of 82\n    value: 47\n    tolerance: 4.7\n  - quantity: higher-order, significant probes of 137\n    value: 59\n    tolerance: 5.9\n  criterion: The significance measure of the Methods, with only the variants of the varied\n    property as conditioning stimuli for each probe (Methods, Stimulus design, paragraph 2), so\n    \"silence\" and unrelated fragments are left out; natural and synthetic probes combined, as\n    the Results do. The paper's 64.6% for frequency does not match 73/110 (66.4%); the count is\n    tested. Which ensembles form each property row follows Table 1 (amplitude from TORC, DMR, MHT\n    and natural-sound probes, frequency likewise, AM and FM from MHT, higher-order from MCN\n    against natural sounds); the Table 1 row totals differ from the Results counts (for\n    amplitude 23 + 39 + 8 + 25 = 95), and the Results counts are used. Reproduced when all five\n    counts are within tolerance and the order amplitude > frequency, AM > FM > higher-order holds\n    in the proportions; partially reproduced when the order holds and some counts are outside.\n\n- id: fig8b-decay-by-property\n  statement: The normalized context-dependent power decays slowly for amplitude and frequency\n    changes (time constants 0.66 and 0.97 s) and fast for AM, FM and higher-order changes (0.11,\n    0.15 and 0.20 s), so higher-order properties act mainly on a timescale of about 100 ms.\n  source: Figure 8B legend; Results, Relation to stimulus properties, paragraph 3\n  quote: That is, higher-order sound properties contributed to the context dependence mainly on a\n    very short timescale, on the order of about 100 ms (Fig. 8B)\n  expected:\n  - quantity: amplitude, tau1 of normalized power\n    value: 0.66\n    tolerance: 0.066\n    unit: s\n  - quantity: frequency, tau1\n    value: 0.97\n    tolerance: 0.097\n    unit: s\n  - quantity: AM, tau1\n    value: 0.11\n    tolerance: 0.011\n    unit: s\n  - quantity: FM, tau1\n    value: 0.15\n    tolerance: 0.015\n    unit: s\n  - quantity: higher-order, tau1\n    value: 0.20\n    tolerance: 0.02\n    unit: s\n  - quantity: amplitude, alpha1\n    value: 0.57\n    tolerance: 0.057\n  - quantity: frequency, alpha1\n    value: 0.54\n    tolerance: 0.054\n  - quantity: AM, alpha1\n    value: 0.86\n    tolerance: 0.086\n  - quantity: FM, alpha1\n    value: 0.64\n    tolerance: 0.064\n  - quantity: higher-order, alpha1\n    value: 0.52\n    tolerance: 0.052\n  depends_on:\n  - fig8a-proportion-by-property\n  criterion: Q(t) of Eq. 20 per property over the probes of fig8a-proportion-by-property, one\n    exponential with constant 0 (Figure 8B legend), fitted from 0 to 4 s (the plotted range); 0 to\n    the end of the shortest common probe length is a variant. Reproduced when every tau1 is within\n    tolerance; partially reproduced when the amplitude and frequency constants both exceed 0.4 s\n    and the AM, FM and higher-order ones are all below 0.3 s. The sizes are reported.\n\n- id: fig8a-significance-fits\n  statement: The proportion of probes with significant context dependence decays fastest and is\n    smallest for higher-order changes, with fitted (size, time constant) of (0.23, 0.25 s) for\n    amplitude, (0.19, 0.27 s) for frequency, (0.13, 0.17 s) for AM, (0.07, 0.15 s) for FM and\n    (0.04, 0.13 s) for higher-order properties.\n  source: Figure 8A legend\n  inferred: Values only in the Figure 8A legend, whose symbols are garbled in the text extraction\n    (read as [alpha1, tau1, kappa] = [0.23, 0.25, 2.8e-3], [0.19, 0.27, 2.3e-3], [0.13, 0.17,\n    2.3e-3], [0.07, 0.15, 2.1e-3] and [0.04, 0.13, 3.6e-3], top to bottom); no sentence of the\n    Results states them.\n  expected:\n  - quantity: amplitude alpha1, tau1 (s)\n    value: 0.25\n    tolerance: 0.025\n    unit: s\n  - quantity: frequency tau1\n    value: 0.27\n    tolerance: 0.027\n    unit: s\n  - quantity: AM tau1\n    value: 0.17\n    tolerance: 0.017\n    unit: s\n  - quantity: FM tau1\n    value: 0.15\n    tolerance: 0.015\n    unit: s\n  - quantity: higher-order tau1\n    value: 0.13\n    tolerance: 0.013\n    unit: s\n  - quantity: amplitude alpha1\n    value: 0.23\n    tolerance: 0.023\n  - quantity: frequency alpha1\n    value: 0.19\n    tolerance: 0.019\n  - quantity: AM alpha1\n    value: 0.13\n    tolerance: 0.013\n  - quantity: FM alpha1\n    value: 0.07\n    tolerance: 0.007\n  - quantity: higher-order alpha1\n    value: 0.04\n    tolerance: 0.004\n  depends_on:\n  - fig8a-proportion-by-property\n  criterion: As fig3a-significance-decay, one exponential with the constant fixed at the mean\n    noise floor (1000 shuffles per probe) of each property, fitted from 0 to 4 s (the plotted\n    range). Reproduced when the sizes fall in the printed order (amplitude > frequency > AM > FM >\n    higher-order) and at least eight of the ten values are within tolerance; partially\n    reproduced when the order holds.\n\n- id: fig8c-relative-effects\n  statement: Changes in amplitude and frequency of the conditioning stimuli produced context\n    effects as large and long-lasting as natural sound contexts, while AM, FM and higher-order\n    changes produced substantially smaller and shorter effects; A1 is more sensitive to\n    lower-order than to higher-order properties.\n  source: Figure 8C; Results, Relation to stimulus properties, paragraphs 2 to 4\n  quote: The effects were as large and long-lasting as those induced when natural sounds were\n    used as conditioning stimuli (Fig. 8, B and C) ... but the effects were substantially smaller\n    and shorter than the effects induced by the changes in natural sound contexts (Fig. 8C)\n  depends_on:\n  - fig8b-decay-by-property\n  - fig3b-fractional-power-decay\n  criterion: Per the Methods (Eq. 21 and the paragraph after it), the area under Q(t) from 0 to 4\n    s for each property, divided by the area for natural sounds (Figure 3B), with 95% confidence\n    intervals from 200 resamplings of 1000 samples. The paper does not say what a sample is;\n    readings are probes drawn with replacement, and trials drawn with replacement within each\n    probe and context. Reproduced when, under one reading, the intervals for amplitude and\n    frequency include 1 (or lie above it) and those for AM, FM and higher-order lie below 1 and\n    below the lower bounds of amplitude and frequency; partially reproduced when the point\n    estimates fall in that pattern but some intervals do not.\n\n- id: fig8-natural-synthetic-probes-alike\n  statement: Natural and synthetic probes gave no difference in the context effects of the\n    synthetic conditioning stimuli, so they were combined.\n  source: Results, Relation to stimulus properties, paragraph 1\n  quote: We used both natural and synthetic sounds as probe stimuli in these experiments, but\n    found no difference between them and so combined the results in the population analysis\n  depends_on:\n  - fig8a-proportion-by-property\n  criterion: A claim of absence for which the paper names no test or threshold. The test fixed\n    here, before analysis, compares per property the proportion of significant probes between\n    natural and synthetic probes by Fisher's exact test at 0.05, Bonferroni over the properties\n    tested with both probe types. Reproduced when no property shows a difference; the\n    proportions and odds ratios are given either way. As the test is not the paper's, the outcome\n    rests on that assumption.\n\n- id: fig9-mgb-fast-decay\n  statement: In the auditory thalamus (MGB), context dependence of spike responses decayed\n    within a short time (time constant about 80 ms; 93 probes in 14 cells), so the long-lasting\n    component in A1 arises mainly in cortex.\n  source: Results, Subcortical contribution to context dependence, paragraphs 2 and 3; Figure 9D\n    legend\n  quote: We found that the neuronal responses in MGB depended only on a short timescale\n  expected:\n  - quantity: decay size alpha1 of the mean SD of PSTHs\n    value: 15.0\n    tolerance: 1.5\n    unit: spike/s\n  - quantity: decay constant tau1\n    value: 0.080\n    tolerance: 0.008\n    unit: s\n  - quantity: constant kappa\n    value: 2.0\n    tolerance: 0.2\n    unit: spike/s\n  depends_on:\n  - methods-recording-counts\n  criterion: Per the Methods (Context dependence at suprathreshold level), PSTHs in 100-ms bins\n    for k = 0 to 60 after probe onset for each context, SD over contexts with the n - 1\n    denominator (Eq. 42), averaged over the 93 probes in 14 cells; one exponential with a free\n    constant (Figure 9D legend). The time assigned to a bin is open; readings are its start (so\n    the first bin is at 0) and its center. A single exponential fitted to 100-ms bins cannot\n    resolve 80 ms finely, so tau1 is also judged against the paper's 0.1-s bin. Spike detection\n    is open as in a1-mgb-firing-rates. Reproduced when, under one reading, tau1 is within\n    tolerance or below 0.1 s, and the mean SD after 0.5 s is within 25% of kappa (a plateau);\n    not reproduced when tau1 exceeds 0.3 s. The sizes are reported against their values.\n\n- id: fig9-example-first-bin\n  statement: In an example MGB unit, the response to a probe differed between contexts only in\n    the first 100-ms bin of the PSTH.\n  source: Figure 9B legend; Results, Subcortical contribution to context dependence, paragraph 2\n  quote: However, in this example the effect of the conditioning stimulus was limited to the first\n    bin (100 ms) of the poststimulus time histograms\n  criterion: The unit is not identified; Figure 9A uses the same sound sequence as Figure 2, over\n    10 repeats with three contexts (silence and two fragments). Among MGB probes with that\n    design, reproduced when at least one has its SD of PSTHs over contexts (Eq. 42) larger in the\n    first bin than in every later bin by at least a factor of two; the fraction of the 93 probes\n    for which this holds is reported.\n\n- id: fig7-example-frequency-context\n  statement: In an example A1 neuron, a natural sound probe preceded by three DMR contexts that\n    differed only in frequency band gave significant context dependence for about 4 s.\n  source: Figure 7A and 7B legend\n  quote: in which a natural sound stimulus probe was preceded by 3 different synthetic conditioning\n    stimuli with different bandwidths\n  statistics:\n  - test: Kruskal-Wallis test at each time point, P < 0.01 for at least 5 ms\n    p: 0.01\n    p_relation: \"<\"\n    n: one cell, one probe in three contexts\n  criterion: The cell is not identified; the author looks for a DMR frequency-variant cell with\n    contexts in 0.625-2.5, 2.5-10 and 10-40 kHz and a natural sound probe. Reproduced when the\n    significance measure finds a significant period ending later than 3 s after probe onset for\n    the matched probe; not testable when no cell matches.\n\n- id: figs1-silence-probe\n  statement: A subset of cells showed significant context dependence soon after the onset of the\n    intersequence silences, but the response power attributable to the preceding stimulus alone\n    faded within about 1 s after the stimulus ended.\n  source: Methods, Stimulus design, paragraph 2 (Supplemental Figure S1A and S1B, not read)\n  quote: even though a subset of cells showed significant contextdependence effects soon after the\n    onset of intersequence intervals (Supplemental Fig. S1A)\n  criterion: The supplement was not supplied, so its figure and any numbers are not known. From\n    the Methods alone, the significance measure applied with the intersequence silence as the\n    probe and the preceding fragment as the context, over the natural sound current-clamp cells.\n    Reproduced when at least one cell has a significant period starting within 0.5 s of the\n    silence onset, and the population proportion of significant silence probes falls to within\n    twice the noise floor by 1 s after onset. The Methods give \"within ~1 s\" for the power\n    (garbled sign read as about).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/asari-2009.yaml'
s=open(p).read()
s=s.replace("Cs-free internal with QX-314 and BAPTA","internal solution with QX-314 and BAPTA")
s=s.replace("quantity: amplitude alpha1, tau1 (s)","quantity: amplitude tau1")
old="""Which ensembles form each property row follows Table 1 (amplitude from TORC, DMR, MHT
    and natural-sound probes, frequency likewise, AM and FM from MHT, higher-order from MCN
    against natural sounds); the Table 1 row totals differ from the Results counts (for
    amplitude 23 + 39 + 8 + 25 = 95), and the Results counts are used."""
new="""Which probes form each property follows the columns of Table 1, whose sums give the
    Results totals (amplitude 23 natural + 39 TORC + 8 DMR + 25 MHT = 95; frequency 25 + 40 + 20
    + 25 = 110; AM 25 + 71 = 96; FM 25 + 57 = 82; higher-order 63 natural + 74 MCN = 137)."""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n -i "rather\|—" claims/asari-2009.yaml; python tools/claims_check.py claims/asari-2009.yaml paper/10.1152-jn.00577.2009.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/asari-2009.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,f'{path}[{i}]')
    elif isinstance(x,str) and ': ' in x: print(path, x[:80])
walk(d)
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('inferred' in c for c in d['claims']))
EOF
```

```
21 2 2
```

**Agent**

I wrote `claims/asari-2009.yaml`, and the quote checker passes it: 21 claims, 19 quotes, 2 statistical values, 0 problems. Nothing is committed.

**Text read**
- **Version:** the version of record (J Neurophysiol 102:2638–2656), as a text extraction of the PDF, with its Methods and figure legends.
- **Garbled symbols:** the extraction breaks Greek letters, <, >, ~, = and ± into a replacement character. I read them from context and cut quotes around them. The PDF pages could not be rendered here because no rendering tool is installed, so I could not check them against the page images. Every value in the file is printed in the text or a legend.
- **Supplement:** Supplemental Figs. S1–S10 were not supplied and I did not read them. The main findings rest on main-text Figs. 2–9, so I went ahead. The one finding that comes from the supplement (`figs1-silence-probe`, effects after the silent gaps between sequences) is quoted from the Methods only.
- **Code:** the paper links none; it only says the analysis was done in MATLAB.

**Claims**
- **Quotes:** 19 claims have quotes. The other 2 are marked `inferred`: the fit values that appear only in the Fig. 3A and Fig. 8A legends.
- **Statistics:** 2 claims have them. They are the per-time-point Kruskal–Wallis tests (P < 0.01 for at least 5 ms) for the example cells of Figs. 2 and 7. The paper reports almost no tests as results. The 95% intervals of Fig. 8C exist only in the figure.
- **Criteria:** all 21 claims have one.

**Details the paper leaves open, with the readings named**
- **Silence as a context:** whether it counts among the contexts in Figs. 3 and 4. Readings are counted (the main one, since Fig. 2B uses it) and not counted.
- **Population average at time t:** whether it is over all probes or only those still running at t.
- **Exponential fits:** the fit range (0–4 s, 0–4.72 s or 0–6 s). Start values are a standard choice.
- **Trial correlation:** mean over all pairs of trials, or each trial against the mean of the others. Also whether the population mean is over cells or over probes.
- **Firing rates:**
  - Spike detection settings are not given, and the paper never says how A1 spikes were detected.
  - Spontaneous window: the gaps between sequences, or a pre-stimulus baseline.
  - Evoked window: all sound periods, or the probe periods.
- **Synaptic conductances:**
  - Which period counts as spontaneous (needed for the noise variance).
  - Any smoothing of the conductances.
- **MGB:** whether a 100-ms PSTH bin is timed at its start or its centre.
- **STRF models (Fig. 4):**
  - The spectrogram window: 10-ms or 20-ms Hann.
  - The response sampling: 4-ms bins or the raw trace.
  - How the cross-validation folds are formed: contiguous blocks or by stimulus.
  - "Did not improve significantly" names no test. I named a paired Wilcoxon test and a repeated-measures test across the nine windows.
- **Fig. 8C resampling:** what one of the "1,000 samples" is. Readings are probes, or trials within each probe and context.
- **Noise autocorrelation:** "decays within ~100 ms" is undefined. I used the lag where it falls below 1/e, with 0.1 as a variant.
- **Natural against synthetic probes:** the paper reports "no difference" without a test. I fixed Fisher's exact test with Bonferroni correction, and the outcome is marked as resting on that assumption.

**Missing from the paper or inconsistent**
- **Example cells:** the paper gives no identifiers for the example cells of Figs. 2, 5, 7 and 9. Those four claims say how to find a matching recording and are not testable if none matches.
- **Frequency percentage:** the paper prints 64.6% for frequency, but 73/110 is 66.4%. The count is what the claim tests.
- **Supplement:** without Fig. S1, the silence-gap claim has no numbers to match.

## End of run

19 turns, 4 minutes, $1.58 at API prices, result: success.
