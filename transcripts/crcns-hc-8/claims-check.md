# crcns-hc-8 · claims-check · run 42569309526

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-8/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,220p docs/protocol.md; cat claims/crcns-hc-8/*.yaml; python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2cada9df-e516-4902-8767-f65e473bb146/tool-results/bmchq43xj.txt"
}
```

```
1	     better fit, p < 0.05") is a method, not a result, and is left out.
2	     Leave the field out when the paper reports no test or interval for the
3	     finding.
4	   - `expected`: each reported number the claim rests on, with a tolerance.
5	     Use the paper's own uncertainty when it gives one (a confidence
6	     interval, or the stated spread); otherwise 10% of the reported value.
7	     For a reported range ("2 to 13%"), the claim holds inside the range
8	     widened by 10% of each bound. Give the reason for any other tolerance.
9	   - `criterion`: how the claim will be judged, for any claim that is not
10	     settled by its expected values alone ("similar", "many", "tended to").
11	     It is written from the paper alone, before anyone analyses the data.
12	   - When a reported number can be read in more than one way (which trials
13	     form the denominator, which subset is meant), list in the criterion the
14	     readings the paper's text plausibly allows, before the analysis. The
15	     claim is reproduced if the result matches under any of them. The
16	     notebook shows every reading, the notes say which ones match, and the
17	     ambiguity is recorded as a deviation.
18	   - Methods come from the paper, never from the author. Every part of a
19	     criterion's method (the selection, the measure, the test, windows,
20	     bins, thresholds, what a measure is compared with) is taken from the
[... 577 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/10.3389-fphys.2016.00425.txt; cat paper/10.3389-fphys.2016.00425.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2cada9df-e516-4902-8767-f65e473bb146/tool-results/b65nnhh09.txt"
}
```

```
1	95786 paper/10.3389-fphys.2016.00425.txt
2	DOI: 10.3389/fphys.2016.00425
3	Version: version of record, PMC5037237 (open access)
4	Source: europepmc fullTextXML
5	Stored: 2026-11-06
6	Extracted: JATS XML flattened
7	------------------------------------------------------------------------
8	Criticality Maximizes Complexity in Neural Tissue
9	
10	## Abstract
11	
12	The analysis of neural systems leverages tools from many different fields. Drawing on techniques from the study of critical phenomena in statistical mechanics, several studies have reported signatures of criticality in neural systems, including power-law distributions, shape collapses, and optimized quantities under tuning. Independently, neural complexity—an information theoretic measure—has been introduced in an effort to quantify the strength of correlations across multiple scales in a neural system. This measure represents an important tool in complex systems research because it allows for the quantification of the complexity of a neural system. In this analysis, we studied the relationships between neural complexity and criticality in neural culture data. We analyzed neural avalanches in 435 recordings from dissociated hippocampal cultures produced from rats, as well as neural avalanches from a cortical branching model. We utilized recently developed maximum likelihood estimation power-law fitting methods that account for doubly truncated power-laws, an automated shape collapse algorithm, and neural complexity and branching ratio calculation methods that account for sub-sampling, all of which are implemented in the freely available Neural Complexity and Criticality MATLAB toolbox. We found evidence that neural systems operate at or near a critical point and that neural complexity is optimized in these neural systems at or near the critical point. Surprisingly, we found evidence that complexity in neural systems is dependent upon avalanche profiles and neuron firing rate, but not precise spiking relati
[... 211 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2cada9df-e516-4902-8767-f65e473bb146/tool-results/b65nnhh09.txt",
 "offset": 224,
 "limit": 200
}
```

```
224	To ensure that complexity and criticality were not trivially related, we used a simple branching or Bethe Lattice model tuned to the critical point (see Section 2.4, Figure 5A ). Using the full model, we found the power-law distributed avalanche sizes (Figure 5B ) and shape collapse (Figure 5C ). We then limited our analysis to only the avalanches that stopped on or before the 8th layer (“small avalanches”). We performed this truncation because the number of neurons grows exponentially with network layer. This growth severely impacted sub-sampling in the complexity calculation. In the original small avalanches, the sizes of the avalanches were power-law distributed and a non-zero complexity was observed (Figure 5D ). We then performed two types of randomizations. First, we randomized the neuron identities in the avalanches (neuron shuffling). This operation preserved the avalanches and their power-law size distributions, but removed the complexity (Figure 5E ). Conversely, when we randomized the order of the network states, but preserved neuron spiking states at each individual time bin (Poisson randomization for the whole network state), the complexity was preserved, but the distribution of avalanche size changed dramatically (Figure 5F ). This difference in behavior under randomization highlights the differences between criticality and complexity analyses. Complexity only focuses on instantaneous correlations between specific neurons, whereas criticality analyses only focus on the time order of the total number of active neurons.
225	
226	Neural complexity and criticality are not trivially related . (A) Bethe Lattice or branching model. Activity spread from layer to layer starting at the leftmost neuron. The likelihood to transmit activity along a connection was p trans = 0.5, yielding a critical model system. (B) The avalanche sizes in the model were power-law distributed, as expected. (C) The avalanches exhibited shape collapse, as expected. (D–F) Analysis o
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 424,1005p /home/runner/.claude/projects/-home-runner-work-encore-encore/2cada9df-e516-4902-8767-f65e473bb146/tool-results/b65nnhh09.txt | awk 'length>25'
```

```
ptrans = 0.3, CN = 0.0023667
Example Sub−Sampling (Susceptibility)
ptrans = 0.26, S = 0.86699
Example Sub−Sampling (SC Curvature)
Figure 1. Cortical branching model example complexity, susceptibility, and shape collapse curvature sub-sampling. In all rows, the left column is from
a sub-critical (ptrans < pcrit) model, the center column is from a near critical (ptrans ≈pcrit) model, and the right column is from a super-critical
(ptrans > pcrit) model. Also, pink arrows represent extrapolated estimates for quantity values in an infinite system. (A) Complexity values. The complexity
sub-sampling fits required a search algorithm to fit large sub-sample sizes due to discontinuous behavior for small transmission probabilities. (B) Susceptibility
values. (C) Shape collapse curvature.
need for an automated shape collapse method and quantitative descriptions of shape collapses in terms of
critical exponents and collapse shape structure (e.g. curvature).
Beyond calculating the critical exponents in the culture data as described above, we also utilized subsampling to estimate the critical exponents in the culture data for systems of infinite or very large size. In
the example shown in Figure 6 we see that the trends in sub-sampled critical exponents were well fit using
a linear function. Furthermore, the extrapolated values of 1/σνz for large or infinite systems are very close
for the average size given duration analysis and for the shape collapse analysis.
Finally, we calculated the complexity for the neurons found in the culture recordings. The complexity
calculation utilized randomized data to correct for sub-sampling and, in some cases, applied a sub-sampling
cut to the data Marshall et al. (2016). We present an example recording that did not require a sub-sampling
Complexity and Recording Length
Figure 2. Cortical branching model recording length affected complexity. Complexity as a function of transmission probability for cortical branching
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "28\|culture" paper/hc-8.data-description.txt | head -20; grep -rn "elsewhere\|with_labels" tools/claims_check.py | head; ls claims | head -40; grep -l "kind: agent" -r claims | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "data\b\|\"data\"\|'data'\|elsewhere" tools/claims_check.py | head -20; tail -25 claims/000011/10.1038-nature17643.yaml
```

```
18:import unicodedata
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
    readings (h1) 1 ms, (h2) 0.1 ms, under both noise readings. Reproduced when, over 100 simulated trials per trial type, the
    modular attractor ends at the instructed fixed point in more than 90% of trials after
    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing (the 90% and
    the 30% to 70% are readings of "restored" and "randomly"; the paper gives no numbers), and the
    modular integrator returns within 10% of its unperturbed trajectory by 2 s after unilateral
    silencing. The FORCE modular network is not specified enough to rebuild and is reported only.
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, convention T. Added that the recorded "late delay" condition of the unilateral experiment ends 0.3 s (Methods naming) or 0 s (Results naming) before the go cue, which the text does not settle; the author reads the times from the trial metadata.
  - fig1d-earlier-photoinhibition-minimal. Added n (5 mice) to the statistics, from the same paragraph and the Extended Data Fig. 3b legend.
  - ed5-photoactivation-recovery. The criterion said the timing was not given; the Results give a 500 ms photostimulus. Added it; only its placement in the trial stays open.
  - ed2e-no-rebound. The criterion applied convention R, which pools lick left and lick right trials, while the legend uses lick right trials with a two-tailed t-test at p < 0.01. Now follows the legend. It judged only the first 400 ms after offset; the legend has two post-offset windows, both now used.
  - fig2b-unilateral-performance. Restricted to photoinhibition at delay onset, as the statement and the Results say ("during the early delay epoch"); the experiment also has a sample epoch condition.
  - fig2b-bilateral-performance. Added n (13 mice) to the statistics, from the Results.
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rh -A1 "^  data:" claims | sort | uniq -c | sort -rn | head; grep -rn "elsewhere" docs/*.md | head -8
```

```
1586 --
    682   data: elsewhere
    468   depends_on:
    411   data: with_labels
    323   data: with_inputs
    171   data: dataset
     92   expected:
     27   where: DANDI:000021 and DANDI:000022 (the paper's Data availability)
     26   where: DANDI 001347
     20   where: Zenodo doi:10.5281/zenodo.15258978 (Data_ICD_Fig1&2&5&6_CognitiveAssay.zip)
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pipeline.md:49:`other_data` (a research paper whose data are elsewhere; `data_in` says where),
docs/pipeline.md:68:aside, are mostly on data elsewhere stops the chain before its checkpoint.
docs/protocol.md:146:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:219:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:228:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:229:     `with_inputs` and `elsewhere` claims are counted apart, each group on
```

**Agent calls Bash**

```bash
cd  sed -n 215,240p docs/protocol.md; grep -rh -B2 -A3 "data: elsewhere" claims | head -30
```

```
file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rln -i "simulation, not\|a simulation" claims | head; grep -rh -B12 -i "criterion: A simulation\|criterion: Simulation" claims | grep -E "data:|where:" | sort | uniq -c | head
```

```
claims/000011/10.1038-nature17643.yaml
claims/000939/10.1038-s41593-024-01588-5.yaml
claims/001687/10.1016-j.neuron.2026.05.027.yaml
claims/000632/10.3390-ijms241310921.yaml
claims/000139/10.1016-j.neuron.2010.09.015.yaml
claims/000140/10.1016-j.neuron.2010.09.015.yaml
claims/000009/10.1038-nature22324.yaml
claims/000016/10.1016-j.neuron.2019.09.045.yaml
claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml
claims/001250/10.1101-2024.12.04.626805.yaml
      5   data: elsewhere
      2   data: with_inputs
      4   where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling); Zenodo
      1   where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling,
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A6 "fig6-modular-models-recover\b" claims/000011/10.1038-nature17643.yaml | head -30; grep -n -A4 "^  data:" claims/crcns-ssc-3/*.yaml | head -20
```

```
913-    recover), for the simple integrator and the transient-input FORCE network. The corrective
914-    feedback and tamed chaos models lack parameters in the text (weights, tuning threshold) and are
915-    reported only if they can be built from the cited methods.
916:- id: fig6-modular-models-recover
917-  statement: Modular networks of two coupled modules (attractor, integrator, trained recurrent
918-    network) recover after silencing of one module; the modular attractor drifts to a random fixed
919-    point when both modules are silenced.
920-  source: Results, Robust model networks, paragraph 2; Figure 6b-d
921-  quote: Selective commissural connections restored activity on the other side after unilateral
922-    transient silencing ( Fig. 6b ). When the two sides are silenced, the network drifts to one of the
--
951-  - ed7-larger-photoinhibition. The statement put the 490 ms and 235 ms recovery times as evidence of "less robust" recovery, which the Results cite to Extended Data Fig. 7e (ROC), and 490 ms is faster than the one-spot 538 ms. Separated them, and the criterion now judges "less robust" by the ROC comparison of Extended Data Fig. 7e with the one-spot ROC; the selectivity-change comparison, which the paper does not cite, is a variant. Added the claims it uses to depends_on.
952-  - cd-captures-selectivity. The criterion referred to a claim fig3-modes that does not exist; now points at fig3d-persistent-mode and fig3e-ramping-mode.
953-  - fig5-callosotomy-no-recovery. Spike rate recovery used only reading (b) of fig2-recordings-recovery, with (a) as a variant, though the two are readings of the same sentence; now either reading, as there.
954:  - fig6-modular-models-recover. The statement gave random drift after bilateral silencing for all modular models; the paper says it of the attractor model only. Marked the 90% and 30% to 70% thresholds as readings.
955-  - Open. ed7e-roc-larger-photoinhibition, the legend prints the bilateral s.e.m. as 0.8
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 922,935p claims/000011/10.1038-nature17643.yaml; grep -n -B2 -A3 "data: elsewhere" claims/000939/*.yaml | head -20
```

```
transient silencing ( Fig. 6b ). When the two sides are silenced, the network drifts to one of the
    fixed points randomly
  criterion: A simulation, not a test on recorded data. Modular attractor with the Methods'
    weights (self 0.5235, within-module -0.5235, between-module 0.3), tau 100 ms, f(x) = g(x) -
    g(0) with g(x) = 1.4 / (1 + exp(-(x - 0.5) / 0.3)), input 0.1 from 0.05 to 0.1 s, tonic 0.5,
    noise variance 0.01; modular integrator with the 8 by 8 matrix printed in the Methods, tau 10
    ms, input 0.04, tonic 40. Integration step and noise scaling with step are not given; standard
    choice 1 ms with Euler-Maruyama. Answered 2026-10-21, not given by the paper; readings (n1)
    white noise of intensity 0.01, Euler-Maruyama increments of sd sqrt(0.01 dt)/tau, (n2) a
    Gaussian sample of variance 0.01 drawn every step and integrated as an input; the outcome must
    hold under both, else methods_underspecified. The integration step is not given either;
    readings (h1) 1 ms, (h2) 0.1 ms, under both noise readings. Reproduced when, over 100 simulated trials per trial type, the
    modular attractor ends at the instructed fixed point in more than 90% of trials after
    unilateral silencing (0.2 to 1.0 s) and in 30% to 70% after bilateral silencing (the 90% and
212-  quote: PoSub-FS cell tuning curves followed the rotated distal landmark in concert with PoSub-HD
213-    cells
214:  data: elsewhere
215-  where: figshare doi:10.6084/m9.figshare.24921252 version 3, Dataset_3.tar.gz (cue rotation, 6
216-    sessions)
217-  criterion: Per the Methods (Analysis of HD cell realignment after cue rotation) and
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a,s.count(a))
    s=s.replace(a,b)
rep("""# (200 um spacing, 30 um electrodes), recorded without stimulation from DIV 6 to 35; 435 recordings
# from 28 cultures (Figure 2B), first 59 min of each,""","""# (200 um spacing, 30 um electrodes), recorded without stimulation from DIV 6 to 35; 435 recordings
# (Methods 2.2; 28 cultures per the data set's description), first 59 min of each,""")
rep("""# readings (a) Benjamini-Hochberg, (b) Benjamini-Yekutieli, over the comparisons of one panel, at
# 0.05.""","""# readings (a) Benjamini-Hochberg, (b) Benjamini-Yekutieli, over the comparisons of one panel, at
# 0.05. The family is not stated either; one panel is used, and all comparisons of the figure are
# shown as a variant.""")
rep("""  - quantity: modal number of neurons per recording
    value: 100
    tolerance: 10""","""  - quantity: typical number of neurons per recording
    value: 100
    tolerance: 10""")
rep(""""Most recordings ... approximately 100" is read as the median number of
    neurons per recording within 10% of 100.""",""""Most recordings ... approximately 100" is read as (a) the median number
    of neurons per recording, (b) the mode of a histogram with Terrell-Scott bins; reproduced when one
    is within 10% of 100.""")
rep("""the range holds when the 5th and 95th percentiles over neurons lie within 0.045 to
    22 Hz (the range widened by 10% of each bound).""","""the range holds when the 5th and 95th percentiles over neurons lie within 0.045 to
    22 Hz (the range widened by 10% of each bound; the percentiles are a choice the paper does not
    make, and the minimum and maximum are reported).""")
rep("""reproduced when the complexity differs from the original by less than 5% (the residue of
    the random subset draws)""","""reproduced when the complexity differs from the original by less than 5% (the residue of
    the random subset draws; 5% is a choice the paper does not make)""")
rep("""curvature has no interior maximum
    within 0.02 of 0.25 and 0.265.""","""curvature has no interior maximum
    within 0.02 of 0.25 and 0.265 (0.02 is a choice the paper does not make).""")
rep("""each mean of
    1/sigma nu z changes by less than 10% between the two analyses.""","""each mean of
    1/sigma nu z changes by less than 10% between the two analyses ("little change" read as 10%, a
    choice the paper does not make).""")
rep("""that method's mean tau or alpha differs from the
    real data's by more than one SD.""","""that method's mean tau or alpha differs from the
    real data's by more than one SD ("different" read as one SD, a choice the paper does not make).""")
rep("""corrected p below 0.05, and Poisson randomization is among the two largest median decreases.""","""corrected p below 0.05, and Poisson randomization is among the two largest median decreases
    (a reading of "most under the strongest forms", which the paper does not quantify).""")
rep("""0.05 and Poisson is among the two largest median decreases.""","""0.05 and Poisson is among the two largest median decreases (read as in
    fig10a-complexity-randomization).""")
rep("""jitter gives a higher median than the real data; the jitter's significance is reported.""","""jitter gives a higher median than the real data; the jitter's significance is reported. The
    Figure 11A,C legend says the ranges decreased under every randomization except 10-bin jitter;
    the direction and corrected p of 1-bin and 100-bin jitter and wrap are reported.""")
rep("""Reproduced when, under one correction reading, for both tau and alpha at least four of
    the five give a higher median with corrected p below 0.05; partially reproduced for two or
    three.""","""Reproduced when, under one correction reading, for both tau and alpha each of the five
    gives a higher median with corrected p below 0.05 (the Figure 11B,D legends name no exception);
    partially reproduced when only some do.""")
rep("""- id: fig8-sigmanuz-methods-agree""","""- id: fig8-exponents-match-literature
  statement: The culture critical exponents from the sub-sampling method agree better with previously
    reported values for neural avalanches (Mazzoni et al. 2007, Pasquale et al. 2008, Friedman et al.
    2012) than those from the search algorithm on the full system.
  source: Results 3.3, paragraph 2; Figure 8
  quote: The exponents found using the sub-sampling method agreed best with previously reported
    values for the critical exponents in neural avalanches
  data: with_inputs
  where: The reference values are not printed in this paper; they are those reported in Mazzoni et
    al. (2007), Pasquale et al. (2008) and Friedman et al. (2012), as cited at Results 3.3,
    paragraph 2.
  depends_on:
  - fig8-subsampling-exponents
  criterion: With the means over recordings of fig8-subsampling-exponents, and for each exponent
    (tau, alpha, 1/sigma nu z) the values the three cited papers report. Which value of each cited
    paper is meant, and how agreement is measured, are not stated; read as the absolute difference of
    the mean from each cited value. Reproduced when, for tau and alpha, the sub-sampling mean is
    closer than the full-system mean to the cited values for most of the cited papers that report
    that exponent; 1/sigma nu z is reported.
- id: fig8-sigmanuz-methods-agree""")
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Corrections applied, and the checker still passes with the new claim. Next I'll add the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml <<'EOF'
checks:
- date: 2026-11-09
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header. The 28 cultures were attributed to Figure 2B, which the header says could not be read; the number comes from the data set's description, and the paper gives only the 435 recordings (Methods 2.2).
  - Header, common detail 3. The family of the false discovery rate correction is not stated in the Figure 10 and 11 legends; named as open, with one panel used and the whole figure as a variant.
  - culture-counts. The expected quantity said modal number of neurons while the criterion judged the median; both are now readings of "most recordings ... approximately 100", as in fig2d-network-isi. Marked the 5th and 95th percentiles of the firing rate range as a choice the paper does not make, with the minimum and maximum reported.
  - fig5f-network-state-poisson-keeps-complexity. Marked the 5% bound for "preserved" as a choice the paper does not make.
  - fig7c-cb-curvature-no-peak. Marked the 0.02 window around the critical point as a choice the paper does not make.
  - fig8-subsampling-exponents. Marked the 10% bound for "little change" in 1/sigma nu z as a choice the paper does not make.
  - eq4-relation-randomized. Marked the one SD bound for "different exponent values" as a choice the paper does not make.
  - fig10a-complexity-randomization and fig10b-susceptibility-randomization. Marked "Poisson among the two largest decreases" as a reading of "most under the strongest forms", which the paper does not quantify.
  - fig11ac-fit-range-randomization. The Figure 11A,C legend says the ranges decreased under every randomization except 10-bin jitter, wider than the Results; the other randomizations are now reported.
  - fig11bd-exponents-randomization. The criterion accepted four of five randomizations, a threshold the paper does not give; the Figure 11B,D legends say the exponents increased under randomization with no exception, so all five are now required, partial when only some.
  - Added fig8-exponents-match-literature. The paper's main findings (Introduction, result 2; Discussion 4.1) include that the exponents agree with previous studies, and Results 3.3 says the sub-sampled exponents agree best with the cited values; no claim covered it. The reference values are in the cited papers, so the claim is data with_inputs.
  - Open. Figure 8 means and SDs, the Figure 10 and 11 significance stars and the Figure 2B exclusions are printed only in the figures, and no PDF of the main article was supplied; claims on them are judged on directions.
  - Open. Methods 2.4 prints p_trans increments of 0.05, which cannot place a peak at 0.265; the grid readings (0.005, 0.01) stand as written in fig7ab-cb-complexity-susceptibility-peak.
  - Open. The threshold for excluding recordings with too few avalanches is not stated (common detail 2).
  - Open. The Figure 7 legend says complexity and susceptibility peak near 0.25, the Results near 0.265; the tolerance of 0.0265 around 0.265 nearly reaches 0.25, so the claim follows the Results.
  - Open. The construction of network states for complexity in the Bethe lattice small avalanches (fig5d-bethe-small-avalanches) and the number of runs are not given in the paper; the criterion follows bethelattice.m as the claims file reads it, which this check could not reread.
EOF
python tools/claims_check.py claims/crcns-hc-8/10.3389-fphys.2016.00425.yaml paper/10.3389-fphys.2016.00425.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The checks entry is added and the file is ready for an attempt. Nothing was committed or pushed.

**Checker result:** `28 claims, 28 quotes, 0 statistical values, 0 problems`. Before my edits it was 27 claims with 0 problems.

**Changes, by claim**
- **Header:** the 28 cultures were credited to Figure 2B, which the header itself says could not be read. That number comes from the dataset's own description; the paper only gives the 435 recordings. Common detail 3 now also says the paper doesn't state which set of comparisons the false discovery rate correction covers. One panel is used, and the whole figure is shown as a variant.
- **culture-counts:** the expected quantity said "modal" but the criterion judged the median. Both are now listed as readings of "most recordings ... approximately 100". The 5th to 95th percentile test of the firing rate range is now marked as a choice the paper doesn't make, and the minimum and maximum are reported.
- **Thresholds the paper doesn't give, now marked as choices:**
  - fig5f-network-state-poisson-keeps-complexity: the 5% bound
  - fig7c-cb-curvature-no-peak: the 0.02 window
  - fig8-subsampling-exponents: the 10% bound
  - eq4-relation-randomized: the one SD bound
  - fig10a-complexity-randomization and fig10b-susceptibility-randomization: "Poisson among the two largest decreases"
- **fig11ac-fit-range-randomization:** the Figure 11A,C legend says the fit ranges fell under every randomization except 10-bin jitter, which is wider than the Results text. The criterion now also reports those other randomizations.
- **fig11bd-exponents-randomization:** the criterion accepted 4 of 5 randomizations, which the paper doesn't say. The legends say the exponents increased under randomization with no exception, so all five are now required, and the result is partial when only some increase.
- **Added fig8-exponents-match-literature:** a main finding with no claim. The paper reports that the sub-sampled exponents agree best with values published by Mazzoni 2007, Pasquale 2008 and Friedman 2012. Those reference values are only in the cited papers, so the claim is marked `data: with_inputs`.

**Still open**
- The Figure 8 means and SDs, the Figure 10 and 11 significance stars, and the Figure 2B exclusions appear only inside the figures. No PDF of the main article was supplied, so those claims are judged on direction only.
- Methods 2.4 prints p_trans steps of 0.05, which can't place a peak at 0.265. The two step-size readings (0.005 and 0.01) stay.
- The paper doesn't say how many avalanches a recording needed to be kept.
- The Figure 7 legend puts the complexity and susceptibility peak near 0.25, while the Results say 0.265. The claim follows the Results.
- In the Bethe lattice claim, the paper doesn't say how network states are built or how many runs were made. The claim relies on the earlier reader's reading of the toolbox file `bethelattice.m`, which I couldn't re-check.

**Ready:** yes (`ready: true`).

## End of run

17 turns, 2 minutes, $1.09 at API prices, result: success.
