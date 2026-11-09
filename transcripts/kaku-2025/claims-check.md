# 001619 · claims-check · run 39607942583

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001619/ paper/; grep -n "Reader" -A80 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 116,220p docs/protocol.md; python tools/claims_check.py claims/001619/10.1101-2025.01.27.635041.yaml paper/10.1101-2025.01.27.635041.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001619/10.1101-2025.01.27.635041.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml"
}
```

```
1	# Claims for Kaku, Liu et al. (2025), "A brainstem map of orofacial rhythms", bioRxiv
2	# doi:10.1101/2025.01.27.635041, on dandiset 001619.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the bioRxiv preprint, version 1 (posted January 27, 2025), as served on its web
7	# page, stored in paper/10.1101-2025.01.27.635041.txt: main text, legends of Figures 1 to 5,
8	# Methods and references, and the supplement "Extended Data Figures" (the legends of Extended
9	# Data Figures 1 to 12, from the supplement PDF, extracted to text). The display equations of
10	# the Methods (the circular Gaussian tuning curve and the VAF) are missing from the text; the
11	# words around them name every term. The Figure 5 legend stops at panel f, although the
12	# Results cite a Figure 5g. No later version was read. Data the dandiset description names: its
13	# title and description only (no data or file was looked at).
14	#
15	# Code read: github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe (2026-06-18). The preprint
16	# says "Code used for analyses will be deposited upon publication"; this repository is the one
17	# the dandiset description names as "the corresponding analysis code", and its README points
18	# at the preprint v1 and at dandiset 001619. It holds process_mat.py (unit quality filter,
19	# trial filter, tongue and inspiration onsets, lick bouts, licking and breathing phase tuning
20	# and modulation index, the lick-to-breath and breath-to-lick timing analyses of Figs 1f-i and
[... 843 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 863
}
```

```
863	    value: 60
864	    tolerance: 6
865	  criterion: Pairs from fig4d-simultaneous-recordings; correlograms by O6. Reproduced when, under
866	    one reading, the four counts are within tolerance; partially reproduced when more than
867	    three quarters of pairs are significant with anticorrelated pairs outnumbering positive
868	    ones.
869	- id: fig4g-symmetric-lags
870	  statement: The cross-correlation was temporally symmetric; breathing units lagged licking units
871	    for 57 pairs, licking units lagged breathing units for 34 pairs, and 12 pairs peaked at zero.
872	  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,
873	    paragraph 4
874	  quote: breathing units lagged licking units for 57 pairs, while other licking units lagged
875	    breathing units for 34 pairs, (the remaining 12 pairs had cross-correlation peak at 0)
876	  depends_on:
877	  - fig4g-licking-breathing-pairs-correlated
878	  expected:
879	  - quantity: pairs with breathing unit lagging
880	    value: 57
881	    tolerance: 6
882	  - quantity: pairs with licking unit lagging
[... 135 more lines not kept]
```

**Agent**

The checker passed: 48 claims, 0 problems. The file has no `checks` section yet. Next I'm reading the paper to check each claim against it.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 221,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Extended Data Fig",
 "path": "paper/10.1101-2025.01.27.635041.txt",
 "output_mode": "content",
 "offset": 0
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.01.27.635041.txt",
 "offset": 600,
 "limit": 307
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git show 42476289 --stat | head; git show 42476289 -- claims/001619 | grep -A40 "^+checks" | head -80; grep -l "kind: link" claims/*/*.yaml | head
```

```
commit 424762893595f60328ee2b79e4bc5338827168b5
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Wed Oct 21 10:10:35 2026 +0000

    Agent run on 001619: claims-check (success)
    
    Run: https://github.com/catalystneuro/reproduction-registry/actions/runs/39582364551
    
    Account: unverified

claims/000004/10.1038-s41597-020-0415-9.yaml
claims/000008/10.1038-s41586-020-2907-3.yaml
claims/000035/10.1038-s41586-020-2907-3.yaml
claims/000067/doi-10.1038-nn.2134.yaml
claims/000114/10.1038-s41586-021-03814-7.yaml
claims/000226/10.1016-j.neuron.2017.03.045.yaml
claims/000718/10.1038-s41586-024-08168-4.yaml
claims/000947/10.1371-journal.pbio.3000829.yaml
claims/001075/10.1038-s41586-023-06683-4.yaml
claims/001084/10.1016-j.neuron.2023.12.011.yaml
```

**Agent calls Bash**

```bash
git show 42476289 --stat | sed -n 8,30p; git log --oneline -6 -- claims/001619 transcripts/001619 2>/dev/null; ls transcripts/001619 2>/dev/null
```

```
Account: unverified

 transcripts/001619/claims-check-report.md | 14 +++++
 transcripts/001619/claims-check.md        | 93 +++++++++++++++++++++++++++++++
 2 files changed, 107 insertions(+)
97e98bb8 Agent run on 001619: claims (success)
42476289 Agent run on 001619: claims-check (success)
cb312e22 Agent run on 001619: claims (success)
claims-check-report.md
claims-check.md
claims-report.md
claims.md
```

**Agent calls Bash**

```bash
grep -n -B1 -A3 "kind: link" claims/*/*.yaml | grep -E "id:|source:" | head -30
```

```
claims/000004/10.1038-s41597-020-0415-9.yaml-364-- id: previous-release-link
claims/000004/10.1038-s41597-020-0415-9.yaml-368-  source: Faraut et al. 2018, Scientific Data 5, 180010 (doi:10.1038/sdata.2018.10), Table 1
claims/000008/10.1038-s41586-020-2907-3.yaml-935-- id: link-metadata-table
claims/000008/10.1038-s41586-020-2907-3.yaml-939-  source: Data availability; the code's data/m1_patchseq_meta_data.csv (mini-atlas at commit
claims/000008/10.1038-s41586-020-2907-3.yaml-951-- id: link-ephys-features
claims/000008/10.1038-s41586-020-2907-3.yaml-955-  source: Methods, Extraction of electrophysiological features; the code's
claims/000035/10.1038-s41586-020-2907-3.yaml-227-- id: link-cells
claims/000035/10.1038-s41586-020-2907-3.yaml-231-  source: Data availability; mini-atlas data/m1_patchseq_phys_temp_meta_data.csv
claims/000035/10.1038-s41586-020-2907-3.yaml-242-- id: link-features
claims/000035/10.1038-s41586-020-2907-3.yaml-246-  source: Methods, "Extraction of electrophysiological features", paragraphs 1 and 12; mini-atlas
claims/000067/doi-10.1038-nn.2134.yaml-47-- id: channel-region-link
claims/000114/10.1038-s41586-021-03814-7.yaml-57-- id: label-link
claims/000226/10.1016-j.neuron.2017.03.045.yaml-56-- id: table-s1-link
claims/000226/10.1016-j.neuron.2017.03.045.yaml-60-  source: Table S1 (Supplemental Information)
claims/000718/10.1038-s41586-024-08168-4.yaml-42-- id: source-data-link
claims/000947/10.1371-journal.pbio.3000829.yaml-45-- id: unit-link
claims/000947/10.1371-journal.pbio.3000829.yaml-49-  source: Data Availability; Dryad doi:10.5061/dryad.0cfxpnvxm, Gaia_Analy.mat and Isis_Analy.mat
claims/001075/10.1038-s41586-023-06683-4.yaml-117-- id: sourcedata-link
claims/001075/10.1038-s41586-023-06683-4.yaml-132-- id: osf-link
claims/001084/10.1016-j.neuron.2023.12.011.yaml-100-- id: fig4-link-published-results
[... 10 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    free-running licking oscillator that sets breath timing reproduces the observed lick-breath\n    relationship, so the two oscillators are bidirectionally coupled.",
 "new_string": "    free-running licking oscillator that sets breath timing reproduces the observed lick-breath\n    relationship, suggesting that the two oscillators are bidirectionally coupled."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    distributions of fig1d-lick-breath-frequencies, Gaussian timing noise SD 10 ms. The fixed\n    latency is the median latency from the last lick to the next inspiration (breathing model)\n    and from the last inspiration to the next lick (licking model) in the data; the number of\n    simulated cycles matches the pooled data. Apply the two peak-difference measures of the\n    header to each simulation. Reproduced when the breathing-driven model gives a Fig 1i\n    difference whose mean is not positive or not significant (two-tailed t-test over simulated\n    sessions of the data's sizes, p >= 0.05) and the licking-driven model fails likewise on\n    the Fig 1g measure, while the data give both differences positive.",
 "new_string": "    distributions of fig1d-lick-breath-frequencies, Gaussian timing noise SD 10 ms. The paper\n    gives no value for the fixed latency or the number of simulated cycles; standard choices,\n    named here, are the median latency from the last lick to the next inspiration (breathing\n    model) and from the last inspiration to the next lick (licking model) in the data, and as\n    many simulated cycles as the pooled data. Apply the two peak-difference measures of the\n    header to each simulation. Reproduced when the breathing-driven model gives a Fig 1i\n    difference whose mean is not positive or not significant (two-tailed t-test over simulated\n    sessions of the data's sizes, p >= 0.05, a standard choice named here since the paper\n    reports no test) and the licking-driven model fails likewise on the Fig 1g measure, while\n    the data give both differences positive."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    in 3.4 ms bins from -0.3 to 0.3 s around swallow onsets and around all expiration onsets\n    (Hilbert phase pi) inside lick bouts.",
 "new_string": "    in 3.4 ms bins from -0.3 to 0.3 s around swallow onsets and around all expiration onsets\n    inside lick bouts. The paper does not define expiration onset; it is taken as the Hilbert\n    phase crossing pi (a standard choice, named here), and the bins and window are plotting\n    choices."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    different breath and lick timing before the swallow, so swallowing interrupted the ongoing\n    rhythms.",
 "new_string": "    different breath and lick timing before the swallow, suggesting that swallowing interrupted\n    the ongoing rhythms."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "  criterion: Phase tuning and MI as in the header, tuned at P < 0.001 and MI > 0.6, readings V2\n    (a) and (b) and V3 (a) and (b). Reproduced when the three counts are within tolerance under\n    one reading; partially reproduced when the counts are not but both-tuned units are under\n    10% of licking-tuned units and under 25% of breathing-tuned units (the proportions the\n    Methods say were robust), under one reading.",
 "new_string": "  criterion: Phase tuning and MI as in the header, tuned at P < 0.001 and MI > 0.6, readings V2\n    (a) and (b) and V3 (a) and (b). The text does not say whether the licking and breathing\n    counts include the 182 units tuned to both; readings (i) they include them; (ii) they\n    exclude them. Reproduced when the three counts are within tolerance under one reading;\n    partially reproduced when the counts are not but both-tuned units are under 10% of\n    licking-tuned units and under 25% of breathing-tuned units, under one reading (a standard\n    choice, named here; the paper's ratios are 5% and 18%, and the Methods say only that the\n    relative proportions were robust to the MI criterion)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    V and IRN, and the pons taken whole (P). Reproduced when the fraction exceeds that of all\n    pons and medulla units in XII, V and IRN",
 "new_string": "    V and IRN, and the pons taken whole (P). Reproduced when the fraction exceeds that of all\n    pons and medulla units in each of XII, V and IRN"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    swallow-modulated unit, the time of the PSTH peak within -0.15 to 0.15 s. Reproduced when the\n    median peak time is negative for units in V and IRN and positive for units in IC and NLL,\n    and the two groups differ by a two-sided Mann-Whitney test at p < 0.05 (a standard choice,\n    named here).",
 "new_string": "    swallow-modulated unit, the time of the PSTH peak within -0.15 to 0.15 s (the paper gives no\n    window or latency measure; a standard choice, named here). Reproduced when the median peak\n    time is negative for units in V and IRN and positive for units in IC and NLL, and the two\n    groups differ by a two-sided Mann-Whitney test at p < 0.05 (a standard choice, named here)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    lags of +-5 bins), readings O8. Reproduced when units whose largest absolute weight is on\n    airflow and units whose largest is on a jaw or tongue regressor are spatially distinct;\n    the median CCF position of the first lies ventral and posterior to that of the second, and\n    the two sets overlap in fewer than 25% of units with VAF > 0.05 (a standard choice, named\n    here).",
 "new_string": "    lags of +-5 bins), readings O8. The paper shows maps of the weights (Extended Data Fig 7c,\n    airflow weights around and below 10N; 7d, jaw and tongue weights in the premotor regions)\n    and gives no measure. Among units with validation VAF > 0.05, each unit is assigned to\n    airflow or to jaw and tongue by its largest absolute weight (threshold and assignment are\n    standard choices, named here). Reproduced when airflow units lie ventral of jaw and tongue\n    units (CCF DV, one-sided Mann-Whitney test, p < 0.05) and the fraction of airflow units\n    near the preBotzinger complex (O3 (a) or (b)) exceeds that of jaw and tongue units\n    (one-sided Fisher exact test, p < 0.05); both tests are standard choices, named here."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "  criterion: Licking units by O1 (b). For each session, the jaw phase at the frame of maximal\n    tongue protrusion in each lick (the frame of largest 3D tongue distance from its onset\n    position) gives the protrusion phase; a unit's preferred phase is compared with its\n    session's median protrusion phase. Reproduced when more than half of licking units prefer\n    a phase within pi/2 of it.",
 "new_string": "  criterion: Licking units by O1 (b). For each session, the jaw phase at the frame of maximal\n    tongue protrusion in each lick (the frame of largest 3D tongue distance from its onset\n    position; the paper does not define full protrusion, a standard choice named here) gives\n    the protrusion phase; a unit's preferred phase is compared with its session's circular\n    median protrusion phase. Reproduced when more than half of licking units prefer a phase\n    within pi/2 of it (a standard choice, named here)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    contours of Extended Data Fig 9a (0.0063 and 0.0019 neurons per mm3); reproduced when the\n    overlap of the two contours is under half of the smaller and lies in IRN dorsal to its DV\n    midpoint.",
 "new_string": "    contours of Extended Data Fig 9a (genioglossus 0.0063 and masseter 0.0019 neurons per mm3);\n    reproduced when the overlap of the two contours is under half of the smaller and lies in\n    IRN dorsal to its DV midpoint (both standard choices, named here)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    mouse then across mice. Reproduced when the mean across mice is within tolerance for each\n    group and licking lasts to the end of the light in most trials (a lick in the last 300 ms).",
 "new_string": "    mouse then across mice (the paper does not say how the rate is taken; a standard choice,\n    named here). Reproduced when the mean across mice is within tolerance for each group and\n    licking lasts to the end of the light in most trials (a lick in the last 300 ms, a standard\n    choice, named here)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    given. Reproduced when the counts are within tolerance and the peak of the mean spectrum of\n    rhythmic sites is within tolerance.",
 "new_string": "    given. The three classes sum to 33 of the 46 sites of Figure 3h; the paper does not say how\n    the other 13 were classed, or whether the 4 transient sites are among the 11. Reproduced\n    when the counts are within tolerance and the peak of the mean spectrum of rhythmic sites is\n    within tolerance."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    n: 11 mice\n  expected:\n    quantity: lick latency after photostimulation onset, mean across mice",
 "new_string": "    n: not stated; the 11 mice of the voluntary latency, or sessions\n  expected:\n    quantity: lick latency after photostimulation onset, mean across mice"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "  criterion: First tongue onset after light onset on photostimulation trials, mean per mouse;\n    paired two-tailed t-test across mice against the Go-cue latencies of\n    fig5b-voluntary-lick-latency. Reproduced when the mean is within tolerance and p < 0.001.",
 "new_string": "  criterion: First tongue onset after light onset on photostimulation trials, mean per mouse.\n    The paper does not give the unit of the paired test; readings (a) the 11 mice, against the\n    Go-cue latencies of fig5b-voluntary-lick-latency; (b) sessions, Go-cue and photostimulation\n    means of the same session. Reproduced when the mean across mice is within tolerance and\n    the paired two-tailed t-test gives p < 0.001 under one reading."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    first tongue protrusion after light onset. The bootstrap comparison is not described;\n    reading, 10,000 paired resamples of trials in both conditions, p the fraction where the\n    induced latency is at least the voluntary one.",
 "new_string": "    first tongue protrusion after light onset. The bootstrap comparison is not described; the\n    reading used is 10,000 resamples of trials with replacement, drawn within each condition,\n    p the fraction where the induced latency is at least the voluntary one (a standard choice,\n    named here; P < 0.0001 needs at least 10,000 resamples)."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -n -A8 "^checks:" claims/001642/*.yaml | head -20
```

```
832:checks:
833-- date: 2026-10-21
834-  kind: agent
835-  model: claude-opus-5-5
836-  ready: true
837-  changes:
838-  - All claims after trials-per-block said "Reproduced when, under one reading" for readings of a method (O1 to O8, windows, tests, pooling). The protocol requires every such reading to give the outcome, else methods_underspecified. Changed to "under every reading", and stated the rule in the opening comment. The "any reading" rule is kept for trial-counts and trials-per-block, whose readings are of what a number counts.
839-  - Opening comment, O6. The Fig. 8 legend's "seven trial events" is not defined (the Methods define E1 to E6 plus E0 and E7). Added readings (i) E1 to E7, (ii) E0 to E6.
840-  - fig2b-extinction-time-course. The CI method is not given. Wilson was the deciding choice and Clopper-Pearson only shown. Both are now readings.
```

**Agent calls Grep**

```json
{
 "pattern": "one reading|a reading|any reading|of O\\d|O\\d \\(",
 "path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "output_mode": "content"
}
```

```
218:    97.5th percentile. Reproduced when, under one reading, all six values are within tolerance;
247:    O4 (a) sessions and (b) mice. Reproduced when the mean is positive with p < 0.001 under a
279:    O4 (a) and (b). Reproduced when the mean is positive with p < 0.001 under a reading.
338:  criterion: Swallow events and ranking as in O5 (a) and (b). For licks and for breaths
354:    in the header, bottom third by O5 (a), the code's selection, pooled across sessions.
356:    when p < 0.05. The mean Delta(1,-1) is reported, and O5 (b), (c) and (d) are shown as
374:  criterion: Delta(0,-1) per swallow event, readings O5 (a) to (d). Reproduced when, under one
377:    reading. Under O5 (a) the selection of the longest cycles 0 favours a positive Delta(0,-1);
389:    Reproduced when p >= 0.05 under O5 (a); not reproduced when p < 0.05. The other readings
488:    exclude them. Reproduced when the three counts are within tolerance under one reading;
490:    licking-tuned units and under 25% of breathing-tuned units, under one reading (a standard
521:    tolerance under one reading.
530:  criterion: The paper shows a map and gives no test. Regions by O3 (a) and (b). Reproduced when
533:    p < 0.05 (a standard choice, named here), under one reading.
561:    one reading; partially reproduced in three or four.
591:    near the preBotzinger complex (O3 (a) or (b)) exceeds that of jaw and tongue units
624:  criterion: As ed7g-cae-better-than-features, for units near the preBotzinger complex (O3 (a)
626:    Reproduced when feature VAF exceeds CAE VAF with P < 0.001 under one reading.
635:  criterion: Preferred phases of the fitted tuning curves (header), breathing units by O1 (b)
636:    as Extended Data Fig 8b states, located by O3 (a) and (b). Inspiration phase is the half
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 484,
 "limit": 80
}
```

```
484	    tolerance: 18
485	  criterion: Phase tuning and MI as in the header, tuned at P < 0.001 and MI > 0.6, readings V2
486	    (a) and (b) and V3 (a) and (b). The text does not say whether the licking and breathing
487	    counts include the 182 units tuned to both; readings (i) they include them; (ii) they
488	    exclude them. Reproduced when the three counts are within tolerance under one reading;
489	    partially reproduced when the counts are not but both-tuned units are under 10% of
490	    licking-tuned units and under 25% of breathing-tuned units, under one reading (a standard
491	    choice, named here; the paper's ratios are 5% and 18%, and the Methods say only that the
492	    relative proportions were robust to the MI criterion). The code's choices (order 5, 100 resamples)
493	    are shown as variants.
494	- id: fig2-swallow-modulated-counts
495	  statement: Of 18,485 units, 427 were modulated by swallowing only, 175 by both licking and
496	    swallowing and 55 by both breathing and swallowing.
497	  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 3; Extended Data
498	    Figure 5e-f
499	  quote: Most units were modulated by swallowing only (427/18485), with a smaller group modulated
500	    by both licking and swallowing (175/18485) (Extended Data Figure 5f). Another small subset of
501	    units with swallowing-related activity were also modulated by breathing (55/18485)
502	  depends_on:
503	  - fig2-licking-breathing-tuned-counts
[... 60 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "#  - Tolerances. A mean +- SD",
 "new_string": "#  - Readings and outcomes. Readings of a method (V2 to V4, O1, O3, O6 to O9, and the readings\n#    of a test, region, selection or shuffle named in a criterion) must all give the outcome;\n#    when they give different outcomes the claim is blocked as methods_underspecified, with\n#    every result shown. \"Under one reading\" applies only to readings of what a reported\n#    number counts or which subset the paper used (O4, O5, denominators, inclusive or\n#    exclusive counts, the unit of a test); with both kinds, the claim holds when, for one\n#    reading of the second kind, every reading of the first gives the outcome.\n#  - Tolerances. A mean +- SD"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    exclude them. Reproduced when the three counts are within tolerance under one reading;\n    partially reproduced when the counts are not but both-tuned units are under 10% of\n    licking-tuned units and under 25% of breathing-tuned units, under one reading (a standard",
 "new_string": "    exclude them. Reproduced when the three counts are within tolerance under (i) or (ii), for\n    every reading of V2 and V3; partially reproduced when the counts are not but both-tuned\n    units are under 10% of licking-tuned units and under 25% of breathing-tuned units, for every\n    reading of V2 and V3 (a standard"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    breathing-tuned; (ii) not licking-tuned. Reproduced when the four numbers are within\n    tolerance under one reading.",
 "new_string": "    breathing-tuned; (ii) not licking-tuned. Reproduced when the four numbers are within\n    tolerance under one combination of (a) or (b) with (i) or (ii), for both readings of V4."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    p < 0.05 (a standard choice, named here), under one reading.",
 "new_string": "    p < 0.05 (a standard choice, named here), under both readings of O3."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    when the fraction exceeds that of all units of the same sessions in all five regions under\n    one reading; partially reproduced in three or four.",
 "new_string": "    when the fraction exceeds that of all units of the same sessions in all five regions under\n    both distance readings; partially reproduced in three or four under both."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent**

Five criteria done; now the rest (ed7, ed7h, ed8i, fig3b, fig4d, fig4g, the lag claim, ed12c, fig4h, fig5c, fig5f).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    near the preBotzinger complex (O3 (a) or (b)) exceeds that of jaw and tongue units\n    (one-sided Fisher exact test, p < 0.05); both tests are standard choices, named here.",
 "new_string": "    near the preBotzinger complex exceeds that of jaw and tongue units (one-sided Fisher exact\n    test, p < 0.05), under every reading of O3 and O8; both tests are standard choices, named\n    here."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    Reproduced when feature VAF exceeds CAE VAF with P < 0.001 under one reading.",
 "new_string": "    Reproduced when feature VAF exceeds CAE VAF with P < 0.001 under every reading of O3 and\n    O8."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 668,
 "limit": 70
}
```

```
668	  source: Results, Brainstem activity maps of orofacial rhythms, paragraph 7; Extended Data
669	    Figure 8g-i
670	  quote: Overall, licking-related neurons showed selectivity for ipsilateral licking (Extended Data
671	    Figure 8i)
672	  depends_on:
673	  - fig2-licking-breathing-tuned-counts
674	  criterion: Lick angle by O9 (a) and (b); spikes from -50 to 100 ms around each lick onset
675	    (Extended Data Fig 8g); left and right licks are those with angle below and above the
676	    midline. Per licking unit (O1 (a)), left-lick rate minus right-lick rate. Reproduced when
677	    this difference is larger for left-hemisphere than right-hemisphere units (CCF medial-
678	    lateral position against the midline) by a one-sided Mann-Whitney test at p < 0.05 (a
679	    standard choice, named here) and each hemisphere's median favours the ipsilateral side,
680	    under one reading.
681	- id: ed4c-licking-map-insensitive-to-sorting
682	  statement: The licking activity map was insensitive to spike-sorting quality; raising the
683	    amplitude threshold from 150 to 500 uV left 2223 of 19,000 units and the same map.
684	  source: Extended Data Figure 4c; Results, Brainstem activity maps of orofacial rhythms,
685	    paragraph 2
686	  quote: Licking activity map was insensitive to the quality of spike sorting. To obtain units with
687	    the highest amplitude, the waveform amplitude quality metric was increased from 150 μV to
[... 50 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    standard choice, named here) and each hemisphere's median favours the ipsilateral side,\n    under one reading.",
 "new_string": "    standard choice, named here) and each hemisphere's median favours the ipsilateral side,\n    under both readings of O9."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    when the inside MIs are higher with rank-sum P < 0.001 under one reading.",
 "new_string": "    when the inside MIs are higher with rank-sum P < 0.001 under both readings."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 860,
 "limit": 100
}
```

```
860	    value: 21
861	    tolerance: 2
862	  criterion: Recordings with two probes, one with licking units (O1) in the posterior-dorsal
863	    IRN/PARN and one with breathing units near the preBotzinger complex (O3). Reproduced when
864	    the counts are within tolerance and the unit ranges per recording are within 1 to 28 and 1
865	    to 12 widened by 10%, under one reading.
866	- id: fig4g-licking-breathing-pairs-correlated
867	  statement: Activity of simultaneously recorded breathing and licking units was significantly
868	    correlated for most pairs compared to trial-shuffled controls (103 of 119 pairs; 43
869	    positively correlated, 60 anticorrelated).
870	  source: Results, Coupled brainstem oscillators autonomously coordinate licking and breathing,
871	    paragraph 4; Figure 4g
872	  quote: Activity was significantly correlated for most pairs compared to trial-shuffled controls
873	    (Figure 4g; 103/119 pairs with significant cross-correlation relative to shuffled control, 43
874	    positively correlated, 60 anticorrelated
875	  depends_on:
876	  - fig4d-simultaneous-recordings
877	  expected:
878	  - quantity: pairs
879	    value: 119
[... 80 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    to 12 widened by 10%, under one reading.",
 "new_string": "    to 12 widened by 10%, under every reading of O1 and O3."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "Reproduced when, under\n    one reading, the four counts are within tolerance; partially reproduced when more than\n    three quarters of pairs are significant with anticorrelated pairs outnumbering positive\n    ones.",
 "new_string": "Reproduced when, under\n    every reading of O6, the four counts are within tolerance; partially reproduced when, under\n    every reading, more than three quarters of pairs are significant with anticorrelated pairs\n    outnumbering positive ones."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    tolerance under one reading; partially reproduced when both lag directions each hold at\n    least a quarter of significant pairs.",
 "new_string": "    tolerance under every reading of O6; partially reproduced when, under every reading, both\n    lag directions each hold at least a quarter of significant pairs."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    more than half of the pairs are significant under one reading of O6.",
 "new_string": "    more than half of the pairs are significant under every reading of O6."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    proportion is lower with p < 0.0001 under one reading; the counts",
 "new_string": "    proportion is lower with p < 0.0001 under (a) or (b), for every reading of O6 and of the\n    continuity correction; the counts"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "offset": 990,
 "limit": 60
}
```

```
990	    tolerance: 19
991	    unit: ms
992	  criterion: Go-cue trials of the cued licking task; breathing phase (Hilbert, header) aligned to
993	    the first lick; test and latency by O7 (a) and (b). Reproduced when, under one reading, the
994	    latency is within tolerance and the phase at lick onset lies in expiration (phase pi to 2
995	    pi).
996	- id: fig5e-photostim-lick-latency-longer
997	  statement: ALM photostimulation evoked licking with a latency of 230.7 +- 31.5 ms, significantly
998	    longer than voluntary licking (paired t-test, two-tailed, p < 0.001).
999	  source: Results, Descending control patterns oscillators at movement initiation, paragraph 3;
1000	    Figure 5e
1001	  quote: Photostimulation evoked licking with a latency of 230.7 ± 31.5 ms (Figure 5e), which was
1002	    significantly longer than voluntarily initiated licking (p<0.001, paired t-test, two-tailed)
1003	  statistics:
1004	  - test: paired t-test, two-tailed
1005	    p: 0.001
1006	    p_relation: "<"
1007	    n: not stated; the 11 mice of the voluntary latency, or sessions
1008	  expected:
1009	    quantity: lick latency after photostimulation onset, mean across mice
[... 37 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "Reproduced when, under one reading, the\n    latency is within tolerance and the phase",
 "new_string": "Reproduced when, under both readings of O7,\n    the latency is within tolerance and the phase"
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    named here; P < 0.0001 needs at least 10,000 resamples). Reproduced when, under one reading of O7, the\n    latency is within tolerance and the comparison gives P < 0.0001.",
 "new_string": "    named here; P < 0.0001 needs at least 10,000 resamples). Reproduced when, under both\n    readings of O7, the latency is within tolerance and the comparison gives P < 0.0001."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -n "\[\]\|.\{101,\}" claims/001619/10.1101-2025.01.27.635041.yaml | head; tail -c 50 claims/001619/10.1101-2025.01.27.635041.yaml
```

```
500:    relative proportions were robust to the MI criterion). The code's choices (order 5, 100 resamples)
in tolerance and the comparison gives P < 0.0001.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001619/10.1101-2025.01.27.635041.yaml",
 "old_string": "    phases are non-uniform by a Rayleigh test at p < 0.05 (a standard choice, named here).",
 "new_string": "    phases are non-uniform by a Rayleigh test at p < 0.05 (a standard choice, named here), under\n    both readings of O3."
}
```

```
The file claims/001619/10.1101-2025.01.27.635041.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/001619/10.1101-2025.01.27.635041.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment. Added the rule for readings. Readings of a method (V2 to V4, O1, O3, O6 to O9, named tests, regions, shuffles) must all give the outcome, else methods_underspecified (protocol, Reader step 3). "Under one reading" is kept only for readings of what a number counts (O4, O5, denominators, units of a test).
  - fig2-licking-breathing-tuned-counts, fig2-swallow-modulated-counts, fig2f-breathing-units-location, fig2h-swallow-units-location, ed7h-prebotc-exception, ed8bc-prebotc-inspiration-phase, ed8i-ipsilateral-lick-selectivity, fig3b-licking-units-in-premotor-regions, fig4d-simultaneous-recordings, fig4g-licking-breathing-pairs-correlated, fig4g-symmetric-lags, ed12c-correlation-without-licking, fig4h-fewer-correlations-outside-oscillator, fig5c-preemptive-breath-adjustment and fig5f-artificial-licking-late-breath-adjustment. Changed "under one reading" of method readings to "under every reading", by the rule above.
  - fig2-licking-breathing-tuned-counts. The 10% and 25% partial thresholds were attributed to the Methods, which say only that the proportions were robust; now named as a standard choice. Added readings (i) and (ii), since the text does not say whether 3551 and 1015 include the 182 units tuned to both.
  - ed1-unidirectional-models-fail and fig1k-rhythms-follow-swallow-at-fixed-latency. The statements said "so" where the paper says "suggest"; now "suggesting". ed1 also now names the fixed latency, the cycle count and the p >= 0.05 test as choices, since the paper gives none.
  - ed7-glm-separate-clusters. The criterion asked whether two sets assigned by largest weight "overlap", but such sets cannot overlap, and it set a posterior position the paper does not give. Rewritten from Extended Data Fig 7c-d (airflow weights around and below 10N), with each choice named.
  - ed1bc-licks-pause-at-swallows, ed6e-swallow-latencies, ed8e-licking-units-protrusion, fig3a-premotor-regions and fig3ce-descending-stimulation-rhythmic-licking. Choices the paper does not give (expiration onset, peak window, full protrusion frame, pi/2 margin, contour overlap rule, lick rate window, last 300 ms) are now named as standard choices.
  - fig2g-licking-units-location. "in XII, V and IRN" was ambiguous; now "in each of", following the statement, which names each region.
  - ed10-site-classes. Noted that the three classes sum to 33 of the 46 sites, and that the paper does not say whether the 4 transient sites are among the 11.
  - fig5e-photostim-lick-latency-longer. The paper does not give n for the paired t-test; the recorded "11 mice" was an inference. n now says so, and the criterion gives readings (a) mice and (b) sessions.
  - fig5f-artificial-licking-late-breath-adjustment. The bootstrap reading said "paired resamples of trials", but voluntary and induced trials are not paired. Now resamples within each condition, named as a choice.
  - Open. The cross-correlation analysis (O6) cites Methods that do not exist, so its readings are reconstructed; fig4g, fig4h and ed12c are likely to be blocked as methods_underspecified if the readings disagree.
  - Open. fig1f-inspiration-between-licks judges "never" by a 5% standard choice and only reports the literal reading.
  - Open. The header's code details (process_mat.py functions, bins, windows) were not checked against the repository in this check; they were taken as the first reader recorded them.
EOF
python tools/claims_check.py claims/001619/10.1101-2025.01.27.635041.yaml paper/10.1101-2025.01.27.635041.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/001619/10.1101-2025.01.27.635041.yaml | grep -n "[^ ]: " | grep -v "^[0-9]*:- date\|kind:\|model:\|ready:\|changes:"; grep -c "—\|rather" claims/001619/10.1101-2025.01.27.635041.yaml; git status --short
```

```
0
 M claims/001619/10.1101-2025.01.27.635041.yaml
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

The claims file for 001619 is ready for an attempt (`ready: true`). I corrected 17 claims and the opening comment; three problems remain open.

**Checker:** `48 claims, 46 quotes, 13 statistical values, 0 problems`, both before and after my changes.

All quotes, sources, p-values and expected values match the paper, and every claim comes from this paper. Every main finding has a claim: lick and breath coordination, swallow pauses, the activity maps, the premotor network and rhythm site, the coupled oscillators, and the descending control at lick onset.

**Changes, by claim**
- **Opening comment:** added the protocol's rule for readings. When a method detail can be read more than one way, every reading must give the same outcome, or the claim is blocked as `methods_underspecified`. "Under one reading" is kept only where the doubt is about what a number counts (O4, O5, denominators, the unit of a test).
- **15 claims** used "under one reading" for method readings, which the protocol does not allow. These now say "under every reading": fig2-licking-breathing-tuned-counts, fig2-swallow-modulated-counts, fig2f, fig2h, ed7h, ed8bc, ed8i, fig3b, fig4d, both fig4g claims, ed12c, fig4h, fig5c, fig5f.
- **fig2-licking-breathing-tuned-counts:** the 10% and 25% thresholds for "partially reproduced" were credited to the Methods, which only say the proportions were robust. They are now named as a standard choice. I also added two readings, because the text doesn't say whether 3551 and 1015 include the 182 units tuned to both.
- **ed1-unidirectional-models-fail, fig1k:** the statements said "so" where the paper says "suggest". ed1 now also names the latency, the cycle count and its test as choices, since the paper gives none.
- **ed7-glm-separate-clusters:** the criterion didn't work. It asked whether two sets "overlap" when the way they were built means they can't, and it added a "posterior" position the paper doesn't give. I rewrote it from Extended Data Fig 7c-d.
- **ed1bc, ed6e, ed8e, fig3a, fig3ce:** methods the paper doesn't give (such as expiration onset, the peak window and the overlap rule) are now named as choices.
- **fig2g:** "in XII, V and IRN" now reads "in each of".
- **ed10-site-classes:** noted that the three site classes add up to 33 of the 46 sites, and that the paper doesn't say whether the 4 transient sites are among the 11.
- **fig5e:** "n: 11 mice" was a guess, since the paper gives no n for the paired test. It now says so, and the criterion offers two readings: mice or sessions.
- **fig5f:** the bootstrap was described as "paired", but those trials aren't paired. It now resamples within each condition.

**Still open**
- The cross-correlation analysis (O6) cites a Methods section that doesn't exist, so its readings are reconstructions. fig4g, fig4h and ed12c are likely to be blocked as `methods_underspecified`.
- fig1f-inspiration-between-licks judges "never" with a 5% threshold that the first reader chose; the literal reading is only reported.
- I didn't check the opening comment's details from the analysis code against the repository; they are as the first reader recorded them.

Nothing is committed or pushed. The only file changed is `claims/001619/10.1101-2025.01.27.635041.yaml`.

## End of run

55 turns, 5 minutes, result: success.
