# kennedy-2020 · claims-check · run 42745844969

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ claims/ | head; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 103,200p docs/protocol.md; ls paper
```

```
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
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kennedy-2020.yaml paper/10.1038-s41586-020-2728-4.txt; wc -l claims/kennedy-2020.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/kennedy-2020.yaml"
}
```

```
1	# Claims for Kennedy, Kunwar, Li et al. (2020), Nature 586, 730-734, on DANDI:001182.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
3	# protocol as stated in docs/protocol.md (version pilot-14). No data of the dataset were seen.
4	#
5	# Text read: the accepted author manuscript in Europe PMC (PMC7606611, NIHMS1606924), full text,
6	# with its Methods, figure legends and Extended Data legends 1 to 10, and Supplementary Table 1
7	# (41586_2020_2728_MOESM1_ESM.pdf, the table of statistical tests). The version of record was not
8	# read. No main-text PDF was supplied, so no figure was looked at; claims rest on the text, the
9	# legends and Supplementary Table 1.
10	#
11	# Code read: https://github.com/DJALab/VMHdm_persistence at commit 7e5911b28deb10c0327d6b51330534dbafa04469
12	# (2021-11-15). It holds MATLAB scripts for the fiber photometry (data_analysis/fiberphotometry), the
13	# Fig 3m decoder (Fig3m_naiveBayes_multiclass.m), the population decay fits of Fig 2d and 3b
14	# (downsampled_MEI_traces.m), the cross-day correlation of ED Fig 7c
15	# (ED7c_representation_separation_spearman.m), and the six network models of Fig 4
16	# (network_models). It does not hold the cell extraction, the responsive-cell selection, the peak and
17	# half-peak times, the preference index, the PCA, the time-resolved decoders, the autocorrelation of
18	# the imaging data, or the two data similarity scores; computeMetricDiagonal and applyMetricToRaster,
19	# which the model scripts call, are missing. The scripts read a MATLAB struct `expt` (mice indexed
20	# 1, 3, 4, 5 and 7; days session1 to session3; stimuli named rat, male, toy, USS and tone) that is not
[... 833 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2728-4.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2728-4.txt",
 "offset": 531,
 "limit": 530
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker found 2 p-values not in the text (they come from Supplementary Table 1, a PDF). Next I'm reading that table to check the recorded statistics.

**Agent calls Bash**

```bash
cd  tail -n +1061 paper/10.1038-s41586-020-2728-4.txt | grep -v "^\[" | grep -v "^$" | head -20; pdftotext -layout paper/10.1038-s41586-020-2728-4.supp.pdf $TMPDIR/supp.txt && wc -l $TMPDIR/supp.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Supplement: 41586" paper/*.txt; sed -n "$(grep -n 'Supplement: 41586' paper/10.1038-s41586-020-2728-4.txt | cut -d: -f1),\$p" paper/10.1038-s41586-020-2728-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/kennedy-2020.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)

# fig1de-toy-weaker: add the ED1k rat vs toy test
rep("""  source: Main text, paragraph 1; Figure 1d and 1e; Supplementary Table 1, Fig 1e
  quote: In contrast, a toy rat evoked a weaker and shorter response
  statistics:
  - about: peak response, rat against toy, home cage
    test: paired t-test
    statistic: t = 5.456, DF 7
    p: 0.0010
    ci:
      low: -26.96
      high: -10.65
    n: 4 mice
""","""  source: Main text, paragraph 1; Figure 1d and 1e; Extended Data Fig 1j and 1k; Supplementary Table 1,
    Fig 1e and ED 1k
  quote: In contrast, a toy rat evoked a weaker and shorter response
  statistics:
  - about: peak response, rat against toy, home cage
    test: paired t-test
    statistic: t = 5.456, DF 7
    p: 0.0010
    ci:
      low: -26.96
      high: -10.65
    n: 4 mice
  - about: peak, rat against toy, home cage (ED Fig 1k)
    test: paired t-test
    statistic: t = 3.469, DF 3
    p: 0.0400
    ci:
      low: 1.729
      high: 40.09
    n: 4 mice, 1 trial per mouse
""")
# ed1: drop rat vs toy, soften decay direction
rep("""  statement: VMHdm SF1 neurons respond moderately to rat urine (more than to water, with a shorter
    decay than to the rat) and weakly to an overhead looming disk.""",
"""  statement: VMHdm SF1 neurons respond moderately to rat urine (more than to water, with a decay
    constant that differs from that to the rat) and weakly to an overhead looming disk.""")
rep("""  - about: peak, rat against toy, home cage
    test: paired t-test
    statistic: t = 3.469, DF 3
    p: 0.0400
    ci:
      low: 1.729
      high: 40.09
    n: 4 mice, 1 trial per mouse
  - about: peak, rat against looming disk""","""  - about: peak, rat against looming disk""")
rep("""      high: -4.534
    n: 4 mice, 1 trial per mouse
""","""      high: -4.534
    n: 4 mice, 1 trial per mouse
  criterion: The text and legends do not say which of rat and urine decays faster; the sign of the
    Supplementary Table 1 intervals is not a safe guide, since their convention differs between rows
    (ED 1k rat against toy is positive, Fig 1e rat against toy negative). The direction is reported.
    Photometry, not described as part of the dataset.
""")
# ed2abc criterion
rep("""  criterion: A claim of absence, for which neither the text nor Supplementary Table 1 names a test.
    The paper's comparisons of two independent groups use a two-sided t-test (Supplementary Table 1),
    so the claim is reproduced when that test at p < 0.05 finds no difference between the rat and toy
    groups (n = 6 each) in fraction of time in the centre zone or distance to centre, and not
    reproduced when it does; the effect size is given either way. Behaviour, not described as part
    of the dataset.""",
"""  criterion: A claim of absence, for which neither the text, the ED Fig 2 legend nor Supplementary
    Table 1 names a test. The two-sided t-test is a choice made here, on the ground that the paper's
    comparisons of two independent groups use it (Supplementary Table 1), so the outcome rests on that
    assumption. The claim is reproduced when that test at p < 0.05 finds no difference between the
    rat and toy groups (n = 6 each) in fraction of time in the centre zone (ED Fig 2b) or distance to
    centre (ED Fig 2c), and not reproduced when it does; the effect size is given either way. The
    window over which the two measures are averaged is not given; readings (a) the whole recording
    after the mouse is introduced, (b) the first minute, as the "after rat" window of Fig 1m.
    Behaviour, not described as part of the dataset.""")
# ed3fi criterion absence part
rep("""    correlation is with the distance or its negative; the sign is reported. Photometry and behaviour,
    not described as part of the dataset.""",
"""    correlation is with the distance or its negative; the sign is reported. The absence of a
    difference in time to 50% of peak is judged on the paper's two-sided paired t-test at p < 0.05
    (Supplementary Table 1, ED 3g). Photometry and behaviour, not described as part of the dataset.""")
# fig1j statement
rep("""  statement: iC++ silencing of VMHdm SF1 neurons reduces avoidance of a rat in the home cage, raising
    time spent in the zone near the rat.""",
"""  statement: iC++ silencing of VMHdm SF1 neurons reduces avoidance of a rat in the home cage, measured
    as percent time in zone 1 during a 3-minute rat presentation.""")
rep("""    n: 7 iC++ mice and 7 control littermates
""","""    n: 7 iC++ mice and 7 control littermates
  criterion: Where zone 1 lies is not defined in the text, the Methods (Home cage rat exposure assay)
    or the Fig 1j legend; its position relative to the rat is left to the dataset's annotation.
    Behaviour, not described as part of the dataset.
""")
# ed3b swapped p-values
rep("""  criterion: A claim of absence, judged on the paper's paired t-test at p < 0.05 for each group;
    velocity averaged over three minutes in the home cage (ED Fig 3b legend).""",
"""  criterion: A claim of absence, judged on the paper's paired t-test at p < 0.05 for each group;
    velocity averaged over three minutes in the home cage (ED Fig 3b legend). The p-values are recorded
    as Supplementary Table 1 prints them, but they appear swapped between the two rows (t = 1.005 with
    DF 6 gives p near 0.35, t = 0.3959 gives p near 0.71); both are far above 0.05 either way.""")
# ed3j statement
rep("""  statement: Against an EYFP-injected SF1-Cre control, iC++ silencing during and after the rat still
    reduces edge-zone time.""",
"""  statement: Against an EYFP-injected SF1-Cre control given the same photostimulation, iC++ silencing
    in the open field rat exposure assay changes edge-zone time (repeated measures ANOVA).""")
rep("""      high: 38.18
    n: 5 EYFP mice, 6 iC++ mice
""","""      high: 38.18
    n: 5 EYFP mice, 6 iC++ mice
  criterion: The ED Fig 3j legend does not say whether photostimulation began before the rat or after
    it; it marks the period with a green bar, the colour Fig 1l uses for PS after rat only. Both
    timings are readings. Behaviour, not described as part of the dataset.
""")
# ed6
rep("""  statement: Silicon probe recordings in VMHdm confirm the heterogeneous rat-evoked dynamics, with
    peaks and half-peak decays spread over tens of seconds among 370 rat-responsive units; 90% of
    units fire spontaneously at 13 Hz or less.""",
"""  statement: Silicon probe recordings in VMHdm confirm the heterogeneous rat-evoked dynamics seen by
    imaging, in the times to peak and to half-peak of 370 rat-responsive units (ED Fig 6g and 6h);
    90% of units fire spontaneously at 13 Hz or less.""")
rep("""    bins (ED Fig 6d legend). Silicon probe data, not described as part of the dataset.""",
"""    bins (ED Fig 6d legend); spontaneous rate the mean over the 10 s baseline (Methods). Which trials
    enter the responsive rule is open: (a) the mean over the five trials of a session, (b) each
    trial, (c) the ten trials of both sessions. Peak and half-peak times are defined in the Methods for
    imaging only; applying them to the trial-averaged rate is an assumption. The paper gives no
    number for heterogeneity; read as in fig2jo-diverse-peak-times, units peaking within the 10 s
    presentation and units peaking after it each make up at least 10% of rat-responsive units
    (threshold set here). Silicon probe data, not described as part of the dataset.""")
# ed9 source
rep("""  source: Main text, paragraph 6; Extended Data Fig 8 and 9b, 9c; Methods, Decoder analysis""",
"""  source: Main text, paragraph 6; Extended Data Fig 9b and 9c; Methods, Decoder analysis (the text
    also cites ED Fig 8, whose legend shows pairwise Pearson's correlations, not decoders)""")
# fig4e sampling
rep("""    each, spikes convolved with 0.5 s and 1.5 s exponentials and sampled at the 11 Hz frames.""",
"""    each, spikes convolved with 0.5 s and 1.5 s exponentials, correlations computed every 10 ms of
    simulation (Methods, Stimulus-evoked autocorrelation) and read at the 11 Hz frame times from 0 to
    45 s for the score (Methods, Data similarity score); how they are read at those times (nearest
    step or interpolation) is a standard choice that cannot change the outcome.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  grep -n "^checks" claims/kennedy-2020.yaml; cat >> claims/kennedy-2020.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - The two p-values the checker did not find (fig1km-thigmotaxis 1.8e-05, fig1lmn-silencing-before 5.2e-05) were confirmed in Supplementary Table 1, ED 3a, printed 1.80E-05 and 5.20E-05 with a non-ASCII hyphen; every other recorded statistic was checked against the table and matches.
  - ed1-urine-looming, the ED 1k rat against toy test was moved to fig1de-toy-weaker, since the statement is about urine and looming and the test is about the toy; source updated.
  - ed1-urine-looming, "shorter decay than to the rat" changed to a decay that differs; no text or legend gives the direction, and the sign convention of the Supplementary Table 1 intervals differs between rows.
  - ed2abc-no-lingering-odor, the t-test is now stated as a choice made here (the paper names no test for ED 2b and 2c), and the averaging window, which the legend does not give, is named as open with two readings.
  - ed3fi-kinetics-track-thigmotaxis, the absence part (times to 50% of peak) now names the paper's test, the paired t-test of Supplementary Table 1, ED 3g.
  - fig1j-silencing-reduces-avoidance, "raising time spent in the zone near the rat" removed; the paper does not say where zone 1 lies.
  - ed3b-velocity-unchanged, noted that the two printed p-values look swapped between rows given their t and DF; recorded as printed, the outcome is the same either way.
  - ed3j-eyfp-control, "during and after the rat" and "reduces" removed; the ED 3j legend gives neither the timing of photostimulation (its bar is green, the Fig 1l colour for PS after rat only) nor the direction.
  - ed6-ephys-heterogeneous, "spread over tens of seconds" removed as not in the paper; criterion now names the trials entering the responsive rule as open, marks the use of the imaging peak definitions as an assumption, and sets a heterogeneity threshold, as in fig2jo-diverse-peak-times.
  - ed9-persistent-decoding, source changed to ED Fig 9b and 9c; ED Fig 8, cited by the text, shows Pearson's correlations, not decoders.
  - fig4e-models-dynamics, model correlations are computed every 10 ms (Methods), not sampled at 11 Hz; the criterion now says so and reads them at the frame times for the score.
  - Open, not settled. The model code (DJALab/VMHdm_persistence) was not reread here; the criteria's statements about what the scripts do (day 1 and first-trial choices in fig2cd-population-persistent, the decoder window in fig3m-decoder, the cross-day correlation in ed7cd-identity-across-days, the low-gain script parameters in fig4e-models-dynamics) rest on the first reader's reading.
  - Open, not settled. The sample sizes and DF printed in Supplementary Table 1 disagree with the legends in several rows (Fig 1g and 1h, 8 mice against 6; Fig 1e DF 7 for 4 mice; Fig 1q and 1r DF 18 for 5 mice per group); they are recorded as printed.
  - Open, not settled. Many criteria set thresholds of their own where the paper gives no number or test (fig3ab, fig2jo, fig2hi, fig3gj, fig3n, fig3m, ed9, ed7cd, ed7e, ed7b, fig4cd, fig4g, fig4e, fig4h, fig4ijk, ed3c, ed6); each says so, and the outcomes rest on them.
  - Not added as a claim. The text's remark that freezing, jumping and a transient decrease in velocity were not significantly different from controls has no figure or test.
EOF
python tools/claims_check.py claims/kennedy-2020.yaml paper/10.1038-s41586-020-2728-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/enter the responsive rule is open: (a)/enter the responsive rule is open, (a)/' claims/kennedy-2020.yaml; grep -nE '^[^#]*[^"]: [^"]*: ' claims/kennedy-2020.yaml | grep -v "^ *-\? *[a-z_]*: \"" | head; python tools/claims_check.py claims/kennedy-2020.yaml paper/10.1038-s41586-020-2728-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nc "—" claims/kennedy-2020.yaml; grep -nci "rather" claims/kennedy-2020.yaml; git diff --stat
```

```
0
0
 claims/kennedy-2020.yaml | 108 ++++++++++++++++++++++++++++++++++-------------
 1 file changed, 78 insertions(+), 30 deletions(-)
```

**Agent**

I checked the file against the paper and corrected eleven things. The last check marks it ready for an attempt (`ready: true`).

**Checker result:** `claims/kennedy-2020.yaml: 39 claims, 38 quotes, 107 statistical values, 2 problems`. Both problems are p-values the checker could not find in the text: 1.8e-05 in fig1km-thigmotaxis and 5.2e-05 in fig1lmn-silencing-before. I found them by reading Supplementary Table 1, ED 3a, where they are printed as 1.80E-05 and 5.20E-05 with a non-standard hyphen. Every other recorded statistic matches that table.

**Changes, by claim:**
- **fig1de-toy-weaker / ed1-urine-looming:** I moved the ED 1k rat-against-toy test from ed1-urine-looming to fig1de-toy-weaker, since it is about the toy. I also removed "shorter decay than to the rat" from ed1-urine-looming: the paper never gives the direction, and the table's intervals are signed differently from row to row.
- **ed2abc-no-lingering-odor:** the paper names no test, so the t-test is now stated as a choice made here. The averaging window is named as open, with two readings.
- **ed3fi-kinetics-track-thigmotaxis:** the "no difference" part now names the paper's paired t-test (ED 3g).
- **fig1j-silencing-reduces-avoidance:** removed "the zone near the rat"; the paper does not say where zone 1 is.
- **ed3b-velocity-unchanged:** noted that the two printed p-values look swapped, given their t and DF. They are kept as printed; the outcome is the same either way.
- **ed3j-eyfp-control:** removed "during and after the rat" and "reduces"; the legend gives neither the timing nor the direction.
- **ed6-ephys-heterogeneous:** removed "spread over tens of seconds", which the paper does not say. The criterion now names as open which trials count toward a unit being responsive. It marks reusing the imaging peak-time definitions as an assumption, and adds a threshold of its own for "heterogeneous", as fig2jo-diverse-peak-times does.
- **ed9-persistent-decoding:** source changed to ED Fig 9b and 9c. ED Fig 8, which the text cites, shows correlations, not decoders.
- **fig4e-models-dynamics:** the Methods compute model correlations every 10 ms, not at 11 Hz. The criterion now says so and reads them at the frame times for the score.

**Still open (recorded in `checks`):**
- I did not reread the paper's code. What the criteria say the scripts do is the first reader's reading.
- In several rows, sample sizes and DF in Supplementary Table 1 disagree with the figure legends. They are recorded as printed.
- Many criteria set thresholds of their own where the paper gives no number or test. Each says so, and those outcomes rest on them.
- I added no claim for the text's remark that freezing, jumping and slowing did not differ from controls; the paper shows no figure or test for it.

Nothing is committed or pushed.

## End of run

13 turns, 3 minutes, $1.20 at API prices, result: success.
