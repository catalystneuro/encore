# 000252 · claims-check · run 39995670687

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000252/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md
```

```
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
     treating a detail as open.
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000252/*.yaml; python tools/claims_check.py claims/000252/*.yaml paper/*.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000252/10.1101-2022.12.07.22283227.yaml"
}
```

```
1	# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
2	# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
7	# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
8	# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
9	# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
10	# their legends; no claim here rests on their numbers, since every analysis window is defined from
11	# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
12	# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
13	#
14	# Code. The paper links no analysis code. It names two Python libraries: the representational
15	# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
16	# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
17	#
18	# Dataset. Its archive title is "Finger_RL: human intracortical recordings during attempted finger
19	# movements of right and left hands", and the paper's Data Availability names dandiset 000252. It is
20	# meant to hold the ten-finger (right and left hand) task; whether it also holds the
[... 592 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000252/*.yaml paper/*.txt | tail -30; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; sed -n 1,120p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,300p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/ca4a7a3d-5f62-40aa-b825-79c9674b56e6/tool-results/b195iahbw.txt"
}
```

```
1	
2	a) Single-trial firing rates for an example N-PPC neuron during movements of different fingers. (top) Markers correspond to the firing rate during each trial (N=120 across 6 conditions). Gapped vertical lines to the right of markers indicate +/- S.D., and each gap indicates the condition mean. (bottom) Firing rates during thumb (T) and index (I) presses were higher than the No-go (X) baseline. Vertical bars indicate bootstrap 95% confidence intervals (CI) of the effect size versus No-go baseline. Half-violin plots indicate bootstrap distributions.
3	
4	b) Mean smoothed firing rates for each finger movement for two example N-PPC neurons. Shaded areas indicate 95% CI.
5	
6	c) Percentage of N-PPC neurons that discriminated between finger movements in each analysis window (q < 0.05, FDR-corrected for 466 neurons). Line (blue) indicates mean across sessions. Markers (gray) indicate individual sessions.
7	
8	d) Complementary empirical cumulative distribution function (cECDF) visualizing the proportion of N-PPC neurons with ANOVA effect sizes (η 2 ) above the corresponding x-axis value. Vertical lines (gray) indicate Cohen’s thresholds [ 51 ] for small (η 2 =0.01), medium (η 2 =0.06), and large (η 2 =0.14) effect sizes.
9	
10	e) Overlap of N-PPC neurons that modulated significantly (q < 0.05) with large effect sizes (η 2 > 0.14) during movement preparation and movement execution.
11	
12	For visual simplicity, we pooled neurons across sessions when calculating and visualizing single-neuron metrics (percentage selective, number of fingers discriminable from No-Go, empirical cumulative distribution functions).
13	
14	To visualize firing rates, spike rasters were smoothed with a Gaussian kernel (50-ms standard-deviation [S.D.]), then averaged across trials to create a peristimulus time histogram (PSTH).
15	
16	## Offline classification with cross-validation
17	
18	We trained a separate linear classifier for each session to predict finger movements from the neural features
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 300,444p paper/*.txt | grep -v "^\s*$" | grep -iv "^\[\?[0-9]\+\]\?\.\? \|doi" | head -120
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes and I've read the paper. Now I'll make the corrections.

**Agent calls Bash**

```bash
cd claims/000252 && python - <<'EOF'
import re
p='10.1101-2022.12.07.22283227.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""# - O10 Features of the retrospective single-array BMI decoder. (a) threshold crossing rates per
#   electrode in [0.5, 1.5] s after the cue, as online; (b) sorted neurons in the same window.
""","""# - O10 Features of the retrospective single-array BMI decoder. (a) threshold crossing rates per
#   electrode in [0.5, 1.5] s after the cue, as online; (b) sorted neurons in the same window.
# - O11 Analysis window of the ten-finger analyses (selectivity, decoding, distances, CCGP). The
#   Results and legends of Figures 7 and 8 do not name it. The Go window is used, as the Feature
#   Extraction default for movement execution and as the Results compare these results with the
#   contralateral-only movement-period results ("Similar to the contralateral-only results"). No
#   other reading is supported by the text.
""")
rep("""  statement: Most neurons discriminate firing rates across the ten fingers in the Go window (N-PPC
    66%, J-PPC 57%, J-MC 78%, q < 0.05).""","""  statement: Most neurons discriminate firing rates across the ten fingers (N-PPC 66%, J-PPC 57%,
    J-MC 78%, q < 0.05).""")
rep("""  criterion: As in Methods, Single-neuron selectivity. Per neuron, a one-way ANOVA of Go-window
    firing rates (200 to 700 ms after Go) across the ten finger conditions;""","""  criterion: As in Methods, Single-neuron selectivity. Per neuron, a one-way ANOVA of Go-window
    firing rates (200 to 700 ms after Go, by O11) across the ten finger conditions;""")
rep("""    held-out folds pooled over all trials of all sessions. Readings O1 x O2. Reproduced when,
    under one reading, all three accuracies are within tolerance; partially reproduced when all
    three exceed 10% chance by a one-sided binomial test at p < 0.05 but not all are within
    tolerance.""","""    held-out folds pooled over all trials of all sessions. Go window by O11. Readings O1 x O2.
    Reproduced when, under one reading, all three accuracies are within tolerance; partially
    reproduced when one or two are.""")
rep("""  criterion: From the N-PPC distances of fig8b-matching-closer averaged over the 10 sessions (Figure
    8a legend), read as the MDS of Figure 8d preserves them. Reproduced when, under one reading,
    in each hand the index-middle and index-ring distances both exceed the middle-ring distance,
    and the ten within-hand distances of the right hand correlate positively with the
    corresponding left-hand distances (Pearson r > 0). The MDS with Generalized Procrustes
    alignment (with scaling) across sessions, as the Methods describe, is shown.""","""  criterion: From the N-PPC distances of fig8b-matching-closer averaged over the 10 sessions (Figure
    8a legend), read as the MDS of Figure 8d preserves them, limited to the index, middle and ring
    fingers as the Results limit them. The paper gives no measure of similarity across hands; the
    criterion reads it as the pattern the sentence names holding in both hands. Reproduced when,
    under one reading, in each hand the index-middle and index-ring distances both exceed the
    middle-ring distance. The MDS with Generalized Procrustes alignment (with scaling) across
    sessions, as the Methods describe, is shown.""")
rep("""  statement: Even at matched neural population size, J-PPC finger-type CCGP is lower than that of
    N-PPC and J-MC, while hand CCGP matches standard accuracy in all three.""","""  statement: Even at matched neural population size, J-PPC finger-type CCGP is lower than that of
    N-PPC and J-MC.""")
rep("""    choice that cannot change the outcome. Reproduced when, at the J-PPC pooled population size
    and at every smaller size from 50 neurons in steps of 50, the mean J-PPC finger-type CCGP is
    below the means of N-PPC and J-MC at that size.""","""    choice that cannot change the outcome. The grid of sizes is not given; sizes from 50 neurons in
    steps of 50 are a standard choice. Reproduced when, at every size up to the smallest of the
    three pooled populations (J-MC, about 260 neurons), the mean J-PPC finger-type CCGP is below
    the means of N-PPC and J-MC at that size.""")
rep("""  criterion: As fig4c-contra-discriminative, in the Delay window (200 to 700 ms after the Delay
    screen) and the Go window. Whether the FDR correction is applied per window or over both is
    not stated; readings (a) per window, (b) over both windows. Reproduced when, under one reading,
    all four values are within tolerance.""","""  criterion: As fig4c-contra-discriminative, in the Delay window (200 to 700 ms after the Delay
    screen) and the Go window. Whether the FDR correction is applied per window or over both is
    not stated; readings (a) per window, (b) over both windows. The N-PPC Go value (43% with q <
    0.05 and eta2 > 0.14) exceeds the 40% with eta2 > 0.14 of fig4c-contra-discriminative, so the
    two cannot share one denominator; readings of the denominator are (i) all neurons pooled over
    sessions, as the Methods pool single-neuron metrics; (ii) the mean over sessions of the
    per-session percentages, as the Figure 4c line shows. Reproduced when, under one reading,
    all four values are within tolerance.""")
rep("""    number. Errors involving No-Go are counted in the denominator and are not adjacent. Reproduced
    when, under one reading of O1 and O2, all six values are within tolerance; partially
    reproduced when the three accuracies are.""","""    number. The paper does not say how errors involving No-Go enter the share; readings (a) all
    errors form the denominator and those involving No-Go are not adjacent; (b) only errors
    between two finger classes form the denominator. Reproduced when, under one reading of O1, O2
    and these, all six values are within tolerance; partially reproduced when the three
    accuracies are.""")
rep("""    run-block M, repeating for all run-blocks in each session. 83% +/- 7% accuracy (chance 17%),
    1488 trials over 8 sessions
  expected:""","""    run-block M, repeating for all run-blocks in each session. 83% +/- 7% accuracy (chance 17%),
    1488 trials over 8 sessions ... Same as (a) using J-MC population activity. 87% +/- 8%
    accuracy (chance 17%), 1488 trials over 8 sessions
  expected:""")
s=s.rstrip('\n')+'\n'+"""checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, added O11. The paper does not name the analysis window of the ten-finger analyses; the Go window is the only reading the text supports, and is now named as such.
  - tenfinger-discriminative-fraction, removed "in the Go window" from the statement, since the paper does not say it; the criterion cites O11.
  - tenfinger-decoding-accuracy, removed the one-sided binomial test from the partial rule, a test the paper does not use; partial is now one or two accuracies within tolerance.
  - fig8a-npcc-index-distinct, removed the Pearson r > 0 over ten within-hand distances, a measure the paper does not use, and limited the check to index, middle and ring, as the Results do.
  - figs11-jppc-lower-matched-size, removed the hand CCGP clause from the statement, as the quote and criterion do not cover it (fig8e-hand-ccgp does); the size range now stops at the smallest pooled population, since J-MC (about 260) is smaller than J-PPC (about 320) and cannot be compared at the J-PPC size; the 50-neuron grid is named as a standard choice.
  - fig4e-plan-vs-move, added readings of the denominator, since the paper's N-PPC 43% strongly tuned in the Go window exceeds its 40% with eta2 > 0.14 and both cannot share one denominator.
  - fig5a-contra-decoding, the rule for errors involving No-Go was a choice the paper does not make; it is now two named readings.
  - figs6-single-array-retrospective, extended the quote to the J-MC legend sentence that gives 87% +/- 8%.
  - Open, O9. The paper gives no margin for "close to" standard accuracy; reading (a), 0.9 of standard accuracy, is a convention not taken from the paper, and only (b) is anchored in the paper's J-PPC contrast.
  - Open, fig8a-npcc-index-distinct. "Similar across hands" has no measure in the paper; the criterion reads it as the named pattern in both hands.
  - Open, fig4c-contra-discriminative. The legend counts 466 N-PPC neurons pooled against 118 x 4 = 472 from the per-session mean, which may mean the per-session counts precede the 0.5 Hz exclusion (O1).
"""
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/000252/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n ": .*: \|—\|rather" claims/000252/*.yaml | sed -n 1,40p | grep -v "^[0-9]*:#" | grep -v 'quote: "' | head; git status --short
```

```
110:    for 2 sessions). We recorded 111 neurons per session (min: 102; max: 119) from N-PPC, 160
111:    neurons per session (min: 159; max: 160) from J-PPC, and 130 neurons per session (min: 120;
176:    (cross-validated classification accuracy, N-PPC: 70%; J-PPC: 66%; J-MC: 75%; chance: 10%)"
231:    CI: [2.74, 5.46]), but this result was not conclusive in J-PPC (mean difference: 0.27, 95% CI:
400:    multiple finger movements (mean number of significant fingers, N-PPC: 2.1; J-PPC: 1.9; J-MC:
402:    (percentage of neurons with η 2 > 0.14, N-PPC: 40%; J-PPC: 25%; J-MC: 64%"
452:    preparation (N-PPC: 24%; J-PPC: 23%) than during movement execution (N-PPC: 43%; J-PPC: 24%)"
485:    84%; chance: 17%). The majority (N-PPC: 75%; J-PPC: 42%; J-MC: 67%) of errors misclassified an
553:    )), although classification accuracy was lower (N-PPC: 66%; J-PPC: 61%; chance: 17%) than
 M claims/000252/10.1101-2022.12.07.22283227.yaml
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
[... 1 more lines not kept]
```

**Agent**

I checked the claims file for DANDI:000252 against the paper, made eight corrections and logged three open problems. The file is ready for an attempt.

**Checker result** (same before and after my edits): `19 claims, 19 quotes, 12 statistical values, 0 problems`

**Changes, by claim**
- **Header:** added open item O11. The paper never says which time window its ten-finger analyses use. The Go window is the only one the text supports, and the file now says that.
- **tenfinger-discriminative-fraction:** removed "in the Go window" from the statement, because the paper does not say it. The criterion now points to O11.
- **tenfinger-decoding-accuracy:** the rule for "partially reproduced" used a one-sided binomial test the paper never uses. It is now "one or two of the three accuracies within tolerance".
- **fig8a-npcc-index-distinct:** removed a Pearson r > 0 test over ten distances, which the paper does not use. The check now covers only the index, middle and ring fingers, as the Results do.
- **figs11-jppc-lower-matched-size:**
  - Removed the hand CCGP clause from the statement, since neither the quote nor the criterion covers it (fig8e-hand-ccgp does).
  - The comparison sizes now stop at the smallest of the three pooled populations. J-MC (about 260 neurons) is smaller than J-PPC (about 320), so the old rule could not compare them at the J-PPC size.
  - The 50-neuron steps are now labelled a standard choice.
- **fig4e-plan-vs-move:** added two readings of the denominator. The paper's N-PPC 43% "strongly tuned" in the Go window is larger than its 40% with η² > 0.14, which should be a superset, so the two numbers cannot use the same denominator.
- **fig5a-contra-decoding:** how errors involving No-Go count was a choice made by the earlier agent, not the paper. It is now two named readings.
- **figs6-single-array-retrospective:** extended the quote to include the J-MC sentence that gives 87% ± 8%.

**Still open** (logged in the `checks` entry)
- **O9:** the paper gives no margin for "close to standard accuracy". Of the two readings, "at least 0.9 of standard accuracy" is a convention, not from the paper. Only the other one rests on the paper's own J-PPC contrast.
- **fig8a:** the paper gives no measure for "similar across hands"; the criterion reads it as the index pattern holding in both hands.
- **fig4c:** the legend's 466 pooled N-PPC neurons do not match 118 × 4 = 472 from the per-session mean. The per-session counts may have been taken before the 0.5 Hz exclusion (O1).

Every claim checks out against the paper apart from these, and each main finding has a claim. Nothing is committed.

## End of run

12 turns, 2 minutes, result: success.
