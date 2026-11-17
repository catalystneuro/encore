# elie-2019 · claims-check · run 42949527978

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ claims/ | head; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 103,200p docs/protocol.md; ls paper; cat claims/elie-2019.yaml
```

```
<persisted-output>
Output too large (50.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2c50dbff-0800-4e36-a66b-253e4595bc3f/tool-results/b4gmprq78.txt

Preview (first 2KB):
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
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
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 130,200p docs/protocol.md; ls -la paper; wc -l claims/elie-2019.yaml
```

```
is chosen), the criterion names the readings the paper's text allows,
     before the analysis, and the notebook runs each of them. The outcome is
     the one they all give; when they give different outcomes, the author
     adopts the reading the paper best supports, as an assumption, or blocks
     the claim as `methods_underspecified` when no choice is defensible
     (author, step 1.6), with every result shown. An outcome that rests on a
     choice the paper does not make is marked as resting on an assumption.
   - For a claim of absence ("no difference", "did not change"), the
     criterion names the test and threshold the paper used. The claim is
     reproduced when that test does not find the effect and not reproduced
     when it does; give the size of the effect either way. The rule for
     several readings does not apply: absence is judged on the paper's test
     alone, as written, even when the test mixes in a condition that does
     not belong (show the cleaner test as a variant).
   - If a criterion turns out unable to decide (two candidates tied), break
     the tie as the paper's methods or code imply, record it as a deviation,
     and show the other result.
   - `data`: what the paper's test of the finding uses, from the paper:
     `dataset` (the default: the data the paper describes recording),
     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
[... 57 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/elie-2019.yaml"
}
```

```
1	# Claims for Elie & Theunissen (2019), PLoS Computational Biology 15(9):e1006698, "Invariant neural
2	# responses for sensory categories revealed by the time-varying information for communication calls",
3	# doi:10.1371/journal.pcbi.1006698, on CRCNS data set aa-4 (doi:10.6080/K00C4T06).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC6762074, open access), as JATS XML flattened to text under
8	# paper/: main text, Methods, Table 1, and the legends of Figures 1 to 10 and of S1 to S7 Fig. The
9	# supplement is the seven figures whose legends are in the text; it has no other file. No PDF was
10	# supplied. The extraction drops every displayed equation: the information formulas, the
11	# coherence-based information (Methods, Time-varying spike rate estimation), the exponential model
12	# of the cumulative information (Results, Time-varying Information for 3 example neurons), the
13	# definition of the CII (Methods, Calculation of the expected value of categorical information) and
14	# the confusion-matrix information. Where the words around an equation or the code fix it, the
15	# criteria say so; where not, the equation is named as open and the reading the text allows is given.
16	# The author may read those equations in the published article (they are not figures). The data
17	# set's description (paper/aa-4.data-description.txt) was read only to know what it holds; no claim
18	# comes from it.
19	#
20	# Code read: https://github.com/julieelie/PoissonTimeVaryingInfo, commit 97802032 (2019-04-01), the
[... 713 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/elie-2019.yaml paper/10.1371-journal.pcbi.1006698.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; grep -n "2.37" paper/10.1371-journal.pcbi.1006698.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker flags one p-value (2.37e-7, fig9b), which is in fact printed in the text as "2.37 10 −7". Now reading the paper in full.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "offset": 150,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "offset": 300,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pcbi.1006698.txt",
 "offset": 420,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "with_inputs\|with_labels" docs/protocol.md | head; python -c "
from scipy.stats import f
for F,a,b in [(8.39,1,195),(8.39,2,195),(9.32,1,195),(9.32,2,195),(8.18,1,195),(8.18,2,195),(2.77,4,185),(2.77,3,185),(28.5,1,213),(120,1,213),(112,1,213),(84,1,213),(675,1,213)]:
  print(F,a,b,f.sf(F,a,b))
from scipy.stats import t; print(2*t.sf(3.49,214))
"; sed -n 540,638p paper/10.1371-journal.pcbi.1006698.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 236,250p docs/protocol.md; python -c "
import mpmath as m
def fsf(F,a,b): return m.betainc(b/2.,a/2.,0,b/(b+a*F),regularized=True)
for F,a,b in [(8.39,1,195),(8.39,2,195),(9.32,1,195),(9.32,2,195),(8.18,1,195),(8.18,2,195),(2.77,4,185),(2.77,3,185),(28.5,1,213)]:
  print(F,a,b,fsf(F,a,b))
"
```

```
Exit code 1
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
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import mpmath as m
ModuleNotFoundError: No module named 'mpmath'
```

**Agent calls Bash**

```bash
python3 -c "
import math
def tsf2(t,df):
    # two-sided p via F(1,df): I_x(df/2,1/2), x=df/(df+t^2); integrate numerically
    x=df/(df+t*t); a=df/2; b=0.5
    n=200000; s=0
    # integral 0..x of u^(a-1)(1-u)^(b-1) ; use substitution, simpson
    h=x/n
    f=lambda u: math.exp((a-1)*math.log(u)+(b-1)*math.log(1-u)) if u>0 else 0
    s=f(0)+f(x)+sum((4 if i%2 else 2)*f(i*h) for i in range(1,n))
    B=math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))
    return s*h/3/B
for F in (8.39,9.32,8.18): print('F1',F,tsf2(math.sqrt(F),195),'F2',(1+2*F/195)**(-195/2))
x=185/(185+4*2.77); a=185/2; print('F4,185',x**a*(1+a*(1-x)))
"
```

```
F1 8.39 0.004203931942257912 F2 0.0003195895504692758
F1 9.32 0.0025829226955202825 F2 0.00013624610683561587
F1 8.18 0.004696808292108034 F2 0.0003878390920762402
F4,185 0.028680059077972393
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "#   rostro-caudal distance from the L2 axis at the site's depth. The regressions report F(2,195) or\n#   F(1,195) degrees of freedom; the printed",
 "new_string": "#   rostro-caudal distance from the L2 axis at the site's depth. The three regressions print F(2,195)\n#   degrees of freedom; the printed"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    paper; the tutorial's model cells are used. Reproduced when the mean absolute difference between\n    KDE and model rates is below 0.02 spikes/ms, the cumulative information of each model neuron\n    reaches at least 1.8 bits (90% of 2 bits) before it ends, and",
 "new_string": "    paper; the tutorial's model cells are used. Reproduced when the mean absolute difference between\n    KDE and model rates is below 0.02 spikes/ms, the cumulative information of each model neuron\n    reaches at least 1.8 bits (90% of 2 bits, a fixed reading of \"approaches\", the paper giving no\n    number) before it ends, and"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    value: 5\n    tolerance: 0.5",
 "new_string": "    value: 5\n    tolerance: 1"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "  source: Results, Avian auditory neurons have approximate Poisson statistics, paragraphs 3 and 5;",
 "new_string": "  source: Results, Avian auditory neurons have approximate Poisson statistics, paragraphs 3 and 4;"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "  criterion: Noise correlation, per unit, the Pearson correlation of the trial deviations from the\n    delete-one KDE mean in successive bins, pooled over pairs of bins and stimuli (Methods, Testing\n    the poisson assumptions, paragraph 3; the code pools the sums of products and of squares,\n    PoissonTestNeuralResponses.m); significance",
 "new_string": "  criterion: Noise correlation, per unit, the Pearson correlation over trials of the spike counts in\n    successive bins for the same stimulus, averaged across pairs of bins and stimuli (Methods,\n    Testing the poisson assumptions, paragraph 3, which come first). Variant, the code's\n    (PoissonTestNeuralResponses.m), trial deviations from the delete-one KDE mean with the sums of\n    products and of squares pooled over pairs of bins and stimuli; significance"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    against category tau gives p < 0.05 with the stimulus mean higher. Partially reproduced when the\n    test holds and one mean is outside tolerance.",
 "new_string": "    against category tau gives p < 0.05 with the stimulus mean higher. Partially reproduced when the\n    test holds and one mean is outside tolerance. The range of tau is reported beside the paper's 100\n    to 600 ms."
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the anatomy claims, the unimodality source, the new S2 claim and the check entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    (about 197, matching the degrees of freedom), (b) all 303 units with a location. Reproduced when\n    the slope is positive with p < 0.05 under one reading of A and of the units; partially when the\n    slope is positive and significant and R2 is outside tolerance.",
 "new_string": "    (about 197, matching the degrees of freedom), (b) all 303 units with a location. Reproduced when\n    the slope is positive with p < 0.05 and the adjusted R2 is within tolerance under one reading of\n    A and of the units; partially when the slope is positive and significant and R2 is outside\n    tolerance."
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "  depends_on:\n  - table1-anatomy-counts\n  criterion: One-way ANOVA",
 "new_string": "  depends_on:\n  - table1-anatomy-counts\n  expected:\n    quantity: adjusted R2\n    value: 0.027\n    tolerance: 0.0027\n  criterion: The printed numbers do not agree with each other; F(4,185) = 2.77 gives p = 0.029, not\n    0.042, and an adjusted R2 near 0.036, not 0.027. The p-value as printed, the adjusted R2 and\n    the F of the run are reported side by side; the test is held to p < 0.05. One-way ANOVA"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    highest.\n- id: fig10-tau-k300-distance",
 "new_string": "    highest. The adjusted R2 is compared with its tolerance and reported; given the inconsistency\n    above, it does not decide the outcome.\n- id: fig10-tau-k300-distance"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "    axis (Methods A), over the well-fitted units with a location. Reproduced when the tau slope is\n    positive and the k300 slope negative, both with p < 0.05, under one reading of A; partially when\n    one of the two holds. R2 values are compared with their tolerances and reported.",
 "new_string": "    axis (Methods A), over the well-fitted units with a location. Reproduced when the tau slope is\n    positive and the k300 slope negative, both with p < 0.05, and both adjusted R2 are within\n    tolerance, under one reading of A; partially when the signs and significance hold for both and\n    an R2 is outside tolerance, or when only one of the two regressions holds."
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/elie-2019.yaml",
 "old_string": "  source: Discussion, paragraph 7",
 "new_string": "  source: Discussion, paragraph 8"
}
```

```
The file claims/elie-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -2 | xargs -I{} sh -c 'grep -n -A8 "^checks:" {}'
```

```
645:checks:
646-- date: 2026-11-10
647-  kind: agent
648-  model: claude-opus-5-5
649-  ready: true
650-  changes:
651-  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
652-  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
653-  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
850:checks:
851-- date: 2026-11-10
852-  kind: agent
853-  model: claude-opus-5-5
854-  ready: true
855-  changes:
856-  - fig3a-spontaneous-reduction. The statement said firing "recovers after light-OFF"; the paper does not say so and ST2 gives pre against OFF as significant in 3C (adjusted p 1.26e-13). Now says the OFF rate is higher than the light-ON rate, which is what ST2 and the criterion test.
857-  - chr2-increase. "returned to baseline" is not in the paper; restated as the Extended Data Fig. 8 test gives it (pre against OFF not significant).
858-  - zero-mg-isolated-bursts. The paper names two different second slices. Extended Data Fig. 9 shows 10F and 9E; the Extended Data Fig. 5 legend shows isolated bursts in 10F and 11G. The claim fixed 10F and 9E and still cited Extended Data Fig. 5g; both pairs are now readings. Said that the peak thresholds and the 1 minute spacing are not from the paper.
```

**Agent calls Bash**

```bash
cd  cat >> claims/elie-2019.yaml <<'EOF'
- id: s2-spike-counts
  statement: Over the 404 units, all stimuli and all 10 ms bins, no bin holds more than 8 spikes, a
    single bin holds 8, and the mean count per bin is 0.108 spikes.
  source: S2 Fig legend; Methods, The instantaneous information, paragraph 1
  quote: Not a single neuron had more than 8 spikes in a 10 ms bins and high spiking events were very
    rare (only one 10ms bin with 8 spikes over all neurons, all time bins and all stimuli). The
    average number of spikes per 10 ms bin was 0.108.
  depends_on:
  - units-404
  expected:
  - quantity: largest spike count in a 10 ms bin
    value: 8
    tolerance: 0
  - quantity: bins with 8 spikes
    value: 1
    tolerance: 0
  - quantity: mean spike count per 10 ms bin
    value: 0.108
    tolerance: 0.0108
  criterion: Spike counts per unit, stimulus, trial and bin, in the 60 bins of Methods B, over the
    call stimuli of Methods B (the search stimuli are not analysed, S4 Fig legend). The two counts
    are held exact, as 10% of 8 and of 1 is below one spike or one bin. Open, whether the mean runs
    over trials or over trial-averaged counts per stimulus; the two give the same mean when every
    stimulus has the same number of trials, and both are reported. Reproduced when the three values
    are within tolerance; partially when the mean is and a count is not.
checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker result. One flag, fig9b-cii-tau-ratio p 2.37e-7 "not found"; the text prints it as "2.37 10 −7" (Results, Analysis of the categorical information, paragraph 3), so the value is right and is kept.
  - Header, Method A. Said the regressions print F(2,195) or F(1,195); all three print F(2,195). Reworded. The reading as F(1,195) is confirmed, the printed p-values (0.0042, 0.00258, 0.0047) and adjusted R2 values match F(1,195) and not F(2,195).
  - fig1-model-neurons. The 1.8 bit threshold for "approaches the maximum" is not from the paper; now named as a fixed reading.
  - fig2a-poisson-test. The tolerance on the count of 5 units was 0.5 while the criterion held it to 1 unit; set to 1 to match the criterion and its stated reason.
  - fig2b-noise-correlations. Source said paragraphs 3 and 5; the stimulus-correlation sentence is paragraph 4 of the section. The criterion followed the code (deviations from the delete-one KDE mean, pooled sums) while the Methods say the Pearson correlation of counts in successive bins averaged across pairs of bins and stimuli; the Methods now come first and the code is a variant (protocol, Reader step 2).
  - fig7a-time-constants. The 100 to 600 ms range in the statement was not used; it is now reported.
  - fig10-cii-distance. The criterion did not say whether the adjusted R2 had to be within tolerance to reproduce, while the partial outcome depended on it; now it must.
  - fig10-cii-area-anova. The statement's adjusted R2 (0.027) had no expected value; added with 10% tolerance. The printed numbers disagree (F(4,185) = 2.77 gives p 0.029 and an adjusted R2 near 0.036, not 0.042 and 0.027); the criterion now says so and holds the test to p < 0.05, with the R2 reported.
  - fig10-tau-k300-distance. The adjusted R2 values were expected but not part of the outcome; now required for reproduced, with the partial cases restated.
  - cii-unimodal. Source said Discussion paragraph 7; the sentence is in paragraph 8.
  - s2-spike-counts. Added; the S2 Fig numbers (at most 8 spikes per bin, one bin with 8, mean 0.108) are reported results with no claim.
  - Not settled. The S1 Fig power and coherence details and the code descriptions (bins 10 to 610 ms, one-tailed p, CICRand, CsteRate) were taken on the first reader's account; the code repository was not opened in this check.
  - Not settled. S3 Fig (Markov chain overestimates and 40 ms running window underestimates the cumulative information, on example neuron 1) has no claim; it is a method comparison on a unit the paper does not identify.
  - Not settled. The ANOVA's printed F, p and adjusted R2 cannot all be right; which one is wrong cannot be told from the text.
EOF
python tools/claims_check.py claims/elie-2019.yaml paper/10.1371-journal.pcbi.1006698.txt; grep -n " — \|rather" claims/elie-2019.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/elie-2019.yaml'));print(len(d['checks'][-1]['changes']))
for c in d['checks'][-1]['changes']:
  assert ': ' not in c, c
"; git status --short
```

```
14
 M claims/elie-2019.yaml
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
?? scripts
```

**Agent**

I checked `claims/elie-2019.yaml` and it is ready for an attempt (`ready: true`). Only that file was changed; nothing was committed or pushed.

**Checker result:** `claims/elie-2019.yaml: 26 claims, 26 quotes, 10 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND fig9b-cii-tau-ratio 2.37e-07`, and it is a false alarm. The text prints the value as "2.37 10 −7" (Results, Analysis of the categorical information, paragraph 3), and the checker doesn't match that format, so the value is right and stays.

**Changes, by claim:**
- **Header, Method A:** said the regressions print F(2,195) or F(1,195); all three print F(2,195). I recomputed the p-values: the printed 0.0042, 0.00258 and 0.0047, and the adjusted R2 values, match F(1,195) and not F(2,195). So the first reader's interpretation (one predictor, about 197 units) holds.
- **fig1-model-neurons:** the 1.8-bit threshold for "approaches the maximum" is not in the paper. It is now labelled a fixed choice.
- **fig2a-poisson-test:** the tolerance on the count of 5 units was 0.5, while the criterion allowed ±1 unit. Set to 1 so they agree.
- **fig2b-noise-correlations:**
  - The source said paragraphs 3 and 5; the stimulus-correlation sentence is in paragraph 4.
  - The criterion followed the code's noise correlation (deviations from the delete-one mean, pooled sums). The Methods say a Pearson correlation of spike counts in successive bins, averaged over bin pairs and stimuli. The Methods version now comes first and the code's is a variant.
- **fig7a-time-constants:** the 100 to 600 ms range in the statement was not tested; it is now reported.
- **fig10-cii-distance:** the adjusted R2 must now be within tolerance for "reproduced". Before, only the partial outcome depended on it.
- **fig10-cii-area-anova:**
  - Added an expected value for the adjusted R2 of 0.027.
  - The printed numbers contradict each other: F(4,185) = 2.77 gives p = 0.029 (not 0.042) and an adjusted R2 near 0.036 (not 0.027). The criterion now says so, holds the test to p < 0.05 and reports all three side by side.
- **fig10-tau-k300-distance:** the adjusted R2 values are now part of the outcome, and the partial cases are restated.
- **cii-unimodal:** the source is Discussion paragraph 8, not 7.
- **s2-spike-counts (new claim):** the S2 Fig results had no claim. They are: no 10 ms bin holds more than 8 spikes, one bin holds 8, and the mean count per bin is 0.108.

Every other claim matched the paper: statements, sources, quotes, statistics and tolerances.

**Still open (recorded in `checks`):**
- I did not open the code repository. The code details in the file (S1 Fig power and coherence steps, bins from 10 to 610 ms, the one-tailed p, CICRand, CsteRate) rest on the first reader's account.
- S3 Fig, a comparison of estimation methods on one example neuron, has no claim. That neuron is not identified in the paper.
- For the area ANOVA, the text cannot show which of the printed F, p and adjusted R2 is wrong.

## End of run

29 turns, 3 minutes, $1.31 at API prices, result: success.
