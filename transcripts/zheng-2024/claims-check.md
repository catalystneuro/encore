# zheng-2024 · claims-check · run 44697238521

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i zheng; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/zheng-2024.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i zheng; awk '/^## Reader/,/^## Author/' docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/zheng-2024.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/zheng-2024.yaml paper/10.1016-j.celrep.2024.114702.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/zheng-2024.yaml"
}
```

```
1	# Claims for Zheng, Huszar, Hainmueller, Bartos, Williams and Buzsaki (2024), Perpetual step-like
2	# restructuring of hippocampal circuit dynamics, Cell Reports 43, 114702, tested on dandiset 000552.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
4	# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
5	# files; the paper names it as the deposit of its electrophysiological data ("High density CA1
6	# recordings on a figure-8 maze", Huszar et al. 2022, doi:10.48324/dandi.000552/0.230630.2304).
7	#
8	# Text read: the author manuscript in PubMed Central (PMC11485410, NIHMS2025365), full text with
9	# STAR Methods and the main figure legends (Figure 6's legend is printed after the Methods), and the
10	# supplemental information of the version of record (mmc2.pdf, pages 23 to 44, Figures S1 to S15
11	# with legends), both in paper/10.1016-j.celrep.2024.114702.txt. Values printed only inside figure
12	# panels were not read.
13	#
14	# Code read: the paper's Zenodo deposit doi:10.5281/zenodo.13247193, which is
15	# github.com/samdeoxys1/within-session-representationl-drift tag v0.0 (archive folder
16	# samdeoxys1-within-session-representationl-drift-93d6e33). It holds the per-session scripts
17	# (place_variability/code: rate maps fr_map_one_session.py, place fields pf_one_session.py and
18	# pf_recombine_central.py, switch detection switch_detection_one_session.py and test_change_point.py,
19	# step against gradual step_vs_gradual_analysis.py, PV correlation pv_corr_analysis.py, the GLM
20	# behavior_and_switching.py, co-switching test_co_switch.py), shared modules (util_code:
[... 908 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114702.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports 32 claims and 0 problems. I've read the claims file and the main text. Next I'm reading the Methods and supplement legends to check each criterion.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114702.txt",
 "offset": 265,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114702.txt",
 "offset": 684,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls; ls claims | head; grep -rl "data: elsewhere" claims | head -3; grep -rn -B2 -A3 "range .* widened" claims/*.yaml | head -30; grep -n "elsewhere\|data_missing\|on request" docs/protocol.md | head -20
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n -A25 '"expected"' schemas/claims*.json | head -80
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
103:          "expected": {
104-            "description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.",
105-            "oneOf": [
106-              {
107-                "$ref": "#/$defs/expected"
108-              },
109-              {
110-                "type": "array",
111-                "minItems": 1,
112-                "items": {
113-                  "$ref": "#/$defs/expected"
114-                }
115-              }
116-            ]
117-          },
118-          "statistics": {
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/zheng-2024.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""    n: '26'
""","""    n: 26 session and turn units
""")
rep("""    n: '8'
  depends_on:
  - fig1d-pv-decorrelation
  criterion: A claim of absence.""","""    n: 8 session and turn units
  depends_on:
  - fig1d-pv-decorrelation
  criterion: A claim of absence.""")
rep("""by a two-sided Wilcoxon rank-sum test (Figure 1E legend). Reproduced when p < 0.05 with the
    novel slopes more negative; Cohen's d is reported against the expected value.""","""by a two-sided Wilcoxon rank-sum test (Figure 1E legend). Reproduced when p < 0.05 with the
    novel slopes more negative; Cohen's d is reported against the expected value, signed so
    that a more negative novel slope gives a positive d (the legend does not give the order of
    the groups; this is the order that matches the text).""")
rep("""    when the four fractions (switching, ON, OFF per environment) are within tolerance but the
    field counts are not.""","""    when the ON and OFF fractions of both environments (four values) are within tolerance but
    the field counts are not.""")
rep("""    quantity: lowest fraction of place fields better explained by the change-point model, over
      orders 1 to 3
    value: 0.96
    tolerance: 0.0""","""    quantity: lower bound on the fraction of place fields better explained by the change-point
      model, at each order 1 to 3 (the claim holds above it; see criterion)
    value: 0.96
    tolerance: 0.0""")
rep("""    n: '108'""","""    n: 108 session and turn units""")
rep("""    n: '106'
  - about: order 3""","""    n: 106 session and turn units
  - about: order 3""")
rep("""    n: '104'""","""    n: 104 session and turn units""")
rep("""    value: 0.65
    tolerance: 0.065
    unit: range 0.6 to 0.7 widened by 10% of each bound (0.54 to 0.77)""","""    value: 0.655
    tolerance: 0.115
    unit: range 0.6 to 0.7 widened by 10% of each bound (0.54 to 0.77)""")
rep("""    value: 0.76
    tolerance: 0.085
    unit: range 0.75 to 0.77 widened by 10% of each bound (0.675 to 0.847)""","""    value: 0.761
    tolerance: 0.086
    unit: range 0.75 to 0.77 widened by 10% of each bound (0.675 to 0.847)""")
rep("""    is judged on r; reproduced when both r are within tolerance. For Figure S8A and S8B, the
    normalised switch count per arm and trial against the average speed in the arm, Pearson
    correlation (STAR Methods default for linear correlation); the paper reports no value, and r
    and p are reported. Partially reproduced when the speed-trial part holds and a speed-switching
    correlation has |r| above 0.1 with p < 0.05.""","""    is judged on r. For Figure S8A and S8B, the normalised switch count per arm and trial against
    the average speed in the arm, Pearson correlation (STAR Methods default for linear
    correlation); the paper reports no value, and r and p are reported. A clear linear
    relationship is taken as |r| above 0.1 with p < 0.05, a threshold chosen here. Reproduced
    when both speed-trial r are within tolerance and neither speed-switching correlation (ON,
    OFF) is clear; partially reproduced when only the speed-trial part holds.""")
rep("""  criterion: Switch-ON fields, first switch of each field only (Figure S13A). (1) Field width on
    the switch trial against mean speed in that trial, linear regression (Pearson), familiar and
    novel; the paper gives no width definition for a single trial, so readings are (a) the
    detected field's width and (b) the width of the trial rate map above half its peak within the
    field.""","""  criterion: Switch-ON fields, first switch of each field only (Figure S13A). (1) Field width on
    the switch trial against mean speed in that trial, linear regression (Pearson), familiar and
    novel; the paper gives no width definition for a single trial, so readings are (a) the
    detected field's width and (b) the width of the trial rate map above half its peak within the
    field. The Results add that the correlation holds after controlling for position (Figure
    S13B: the same regression within each of ten spatial bins, familiar only); these per-bin
    results are reported.""")
rep("""    signed-rank test against zero; backward is against running direction. (3) Normalised
    within-field peak rate around the switch (trial 0), paired Wilcoxon signed-rank tests between
    neighbouring trials.""","""    signed-rank test against zero; backward is against running direction. (3) Normalised
    within-field peak rate around the switch (trial 0), averaged over fields, paired Wilcoxon
    signed-rank tests between neighbouring trials (Figure S13D). The paper does not say how the
    rate is normalised; readings (a) divided by the field's maximum over trials, (b) divided by
    its mean over trials.""")
rep("""    regressed on the familiar residual, standardised (Figure 5C legend; code metric across fam
    novel notebook, resid_regression). Units read as (a) neurons with each metric averaged over
    fields (Methods) or (b) fields matched across environments by the code's field index. For the""","""    regressed on the familiar residual, standardised (Figure 5C legend; code metric across fam
    novel notebook, resid_regression). Units are neurons with each metric averaged over fields
    (Methods; Figure 5C legend, per dot a neuron, n = 955); fields matched across environments by
    the code's field index are shown as a variant only. For the""")
rep("""  statement: Fields that switched ON have a lower CV of peak rate and less jitter of peak location
    over the five trials after the switch than non-switching fields over five trials from the
    start or middle of the session.""","""  statement: Fields that switched ON have a lower CV of peak rate over the five trials after the
    switch than non-switching fields over five trials from the start or middle of the session, in
    familiar and novel environments; their peak location is also less jittery, except against the
    middle window in the novel environment (p = 0.4).""")
rep("""  - quantity: median CV, non-switching, middle window, novel
    value: 0.46
    tolerance: 0.046
""","""  - quantity: median CV, non-switching, middle window, novel
    value: 0.46
    tolerance: 0.046
  - quantity: median SD of peak location, non-switching, start window, familiar
    value: 2.05
    tolerance: 0.205
  - quantity: median SD of peak location, switch ON, familiar
    value: 1.64
    tolerance: 0.164
  - quantity: median SD of peak location, non-switching, start window, novel
    value: 2.4
    tolerance: 0.24
  - quantity: median SD of peak location, switch ON, novel
    value: 1.95
    tolerance: 0.195
  - quantity: median SD of peak location, non-switching, middle window, familiar
    value: 2.28
    tolerance: 0.228
  - quantity: median SD of peak location, non-switching, middle window, novel
    value: 2.68
    tolerance: 0.268
""")
rep("""    switch, or over the first five trials or five middle trials (the paper does not say which
    five are the middle; the standard choice of the five centred on the session midpoint is used,
    as the choice is unlikely to change the outcome) for non-switching fields; two-sided Wilcoxon
    rank-sum tests. Reproduced when switch-ON CV is lower at p < 0.05 for both windows in familiar
    and in novel and the medians are within tolerance; partially reproduced when the direction and
    significance hold in familiar only. Location results are reported, with the novel middle
    window expected not significant.""","""    switch, or over the first five trials or five middle trials for non-switching fields;
    two-sided Wilcoxon rank-sum tests (Figure S12 legend). The paper does not say which five
    trials are the middle, and with novel p = 0.019 the choice could change the outcome; readings
    (a) the five centred on the session midpoint, (b) the five starting at the midpoint. Reproduced
    when, under a reading, switch-ON CV is lower at p < 0.05 for both windows in familiar and in
    novel, switch-ON location SD is lower at p < 0.05 in familiar (both windows) and in novel
    (start window), and the medians are within tolerance; the novel middle-window location test is
    expected not significant and is reported. Partially reproduced when the CV directions and
    significance hold in familiar only.""")
rep("""  criterion: Selection as in Figure S14 legend (mean within-field rate before the first ON, or after
    the last OFF, below the shuffle threshold of field detection).""","""  criterion: Selection as in Figure S14 legend (mean within-field rate before the first ON, or after
    the last OFF, below the shuffle threshold of field detection); the Results describe the
    selected quantity as the average within-field peak firing rate, which is the other reading.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now I'll append the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/zheng-2024.yaml <<'EOF'
checks:
- date: 2026-11-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - figs4g-population-vectors-gradual, expected value and tolerance changed from 0.65 +- 0.065 to 0.655 +- 0.115, so that they span the stated range 0.54 to 0.77 (0.6 to 0.7 widened by 10% of each bound); the old pair covered only 0.585 to 0.715.
  - fig3k-switch-abrupt, expected value and tolerance changed from 0.76 +- 0.085 to 0.761 +- 0.086, to span the stated range 0.675 to 0.847.
  - figs12-stability-after-switch-on, the statement said switch-ON fields had less location jitter against both windows, but the Figure S12E legend gives novel middle-window p = 0.4; the statement now names that exception.
  - figs12-stability-after-switch-on, added the six location-SD medians of the Figure S12B and S12E legends to expected and made the location results part of the criterion, as the statement rests on them.
  - figs12-stability-after-switch-on, the choice of the five middle trials was called unable to change the outcome; with novel CV p = 0.019 it could, so the criterion now names two readings (centred on, or starting at, the midpoint).
  - fig5c-switchiness-not-intrinsic, fields matched across environments were an equal reading; the Figure 5C legend and the Methods make the unit a neuron (n = 955), so the field-matched analysis from the code is now a variant only.
  - figs13-btsp-signatures, added the Figure S13B control (regression within ten spatial bins, familiar only) that the Results cite for the width-speed correlation, and named the rate normalisation of Figure S13D as open with two readings.
  - figs14-preexisting-fields-ephys, the Results describe the selection on the average within-field peak rate while the Figure S14 legend says mean within-field rate; both are now named as readings.
  - figs8-speed-no-trend, the criterion did not say whether a clear speed-switching correlation prevents reproduction; it now does, and it says that the |r| > 0.1 threshold is chosen here.
  - fig2d-switch-fractions, the partial criterion named "four fractions (switching, ON, OFF per environment)", which is six values; it now names the four ON and OFF fractions.
  - fig3df-step-beats-polynomial-fields, the expected quantity now says that 0.96 is a lower bound, so that the zero tolerance cannot be read as requiring exactly 0.96.
  - fig1e-novel-drift-faster, the criterion now gives the sign convention for Cohen's d, which the legend leaves unstated.
  - fig1e-later-lags-no-difference and figs4g-population-vectors-gradual, n given in words with its unit, as the protocol asks.
  - Open, fig1h-rate-decorrelates-location-stable, the factor of two between the peak-rate and location slopes is chosen by the writer; the paper states the contrast only in words and gives no test.
  - Open, fig6f-switching-asynchronous, "up to 5%" is judged on the 95th percentile of per-trial fractions, a choice the paper does not make (the Figure 6F legend marks means); the maximum is reported.
  - Open, fig3df-polynomial-beats-step-population, fig4-behavior-not-predictive and fig4no-head-scans-not-related, the paper reports no test, so the majority rules, the drop threshold and the default tests are chosen here and labelled as such.
  - Open, the code details cited from the Zenodo repository (segment cut points, trial exclusions, shuffle details) were not checked, as the code is not under paper/.
  - Open, minor findings without a claim, namely Figure S1A and S1B (sleep waveform amplitudes do not differ between switching and stable neurons), Figure S7 (no behavioral or neural signature separates the delay zone) and Figure S11 (multiple-field switching); none is a main finding and none has a reported test except S11 (p = 0.03).
EOF
python tools/claims_check.py claims/zheng-2024.yaml paper/10.1016-j.celrep.2024.114702.txt; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/    S13B: the same regression within each of ten spatial bins, familiar only); these per-bin/    S13B, the same regression within each of ten spatial bins, familiar only); these per-bin/' claims/zheng-2024.yaml; python tools/claims_check.py claims/zheng-2024.yaml paper/10.1016-j.celrep.2024.114702.txt; grep -n '—\|rather' claims/zheng-2024.yaml; grep -nE '^ +[^-#][^:]*[a-z]: ' claims/zheng-2024.yaml | grep -vE '^\s*[0-9]+:\s+(- )?[a-z_]+: ' | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's result line: `claims/zheng-2024.yaml: 32 claims, 32 quotes, 43 statistical values, 0 problems`. It printed the same before and after my edits.

**Changes, by claim:**
- **figs4g-population-vectors-gradual:** the expected value 0.65 ± 0.065 did not cover the stated widened range of 0.54 to 0.77. It is now 0.655 ± 0.115. The n values are now given in words with their unit.
- **fig3k-switch-abrupt:** the expected value is now 0.761 ± 0.086, so it matches the range of 0.675 to 0.847.
- **figs12-stability-after-switch-on:**
  - The statement said switch-ON fields have less location jitter against both windows. The novel middle window has p = 0.4, so the statement now names that exception.
  - I added the six location-SD medians from the legend to `expected`, and the criterion now judges location as well as CV.
  - The criterion said the choice of the five "middle" trials could not change the outcome. That is wrong, since novel CV has p = 0.019. Two readings are now named.
- **fig5c-switchiness-not-intrinsic:** matching fields across environments was listed as an equal reading. The legend and the Methods make the unit a neuron (n = 955), so the field-matched version is now a variant only.
- **figs13-btsp-signatures:** I added the Figure S13B within-position control that the Results cite. The rate normalisation in S13D is now named as open, with two readings.
- **figs14-preexisting-fields-ephys:** the selection quantity differs between the Results (average within-field peak rate) and the legend (mean rate). Both are now named as readings.
- **figs8-speed-no-trend:** the criterion now says whether a clear speed-switching correlation blocks reproduction. It also states that the |r| > 0.1 threshold is chosen here, not taken from the paper.
- **fig2d-switch-fractions:** the partial criterion said "four fractions" but counted six. It now names the four ON and OFF fractions.
- **fig3df-step-beats-polynomial-fields:** the expected quantity now says 0.96 is a lower bound, so its zero tolerance can't be read as "exactly 0.96".
- **fig1e-novel-drift-faster:** I added a sign convention for Cohen's d. **fig1e-later-lags-no-difference:** n is now given in words.

**Still open (recorded in `checks`):**
- Some thresholds are the writer's own choices, labelled as such, because the paper reports no test:
  - fig1h: the "twice as steep" factor.
  - fig6f: the 95th-percentile reading of "up to 5%".
  - fig3df-population, fig4-behavior and fig4no-head-scans: the rules and default tests.
- I could not verify the code details the file cites from the Zenodo repository, because the code is not under `paper/`.
- Figures S1A/B, S7 and S11 have no claim. They are minor control findings, not main ones.

All main findings have a claim, and every claim comes from this paper. The file is ready: `ready: true` is in the new checks entry. Nothing is committed.

## End of run

14 turns, 3 minutes, $1.25 at API prices, result: success.
