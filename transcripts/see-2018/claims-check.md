# see-2018 · claims-check · run 42947036142

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i see; grep -n "Reader" -A60 docs/protocol.md | head -150; cat claims/see-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; sed -n 43,200p docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/see-2018.yaml; python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt; echo EXIT $?; wc -l claims/see-2018.yaml paper/10.7554-elife.35587.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/see-2018.yaml",
 "offset": 60
}
```

```
60	# - What a cNE event is, once activity crosses threshold, is open. Readings (a) every 10-ms bin
61	#   above threshold; (b) one event per contiguous run of bins above threshold, at its peak.
62	schema_version: 2
63	paper: doi:10.7554/elife.35587
64	claims:
65	- id: fig2bd-pwc-measures-covary
66	  statement: Across all penetrations, the sharpness and peak delay of pairwise correlation (PWC)
67	    functions covaried with the pairs' spike train correlation coefficients, accounting for about
68	    50% of the variance.
69	  source: Results, Heterogeneous functional connectivity between columnar AI neurons, paragraph 2;
70	    Figure 2B to D
71	  quote: Across all penetrations, PWCs were fairly heterogeneous but sharpness and delay covaried
72	    with correlation coefficients, accounting for ~50% of the variance
73	  expected:
74	  - quantity: R2 of PWC sharpness against spike train correlation coefficient
75	    value: 0.5
76	    tolerance: 0.05
77	  - quantity: R2 of PWC peak delay against spike train correlation coefficient
78	    value: 0.5
79	    tolerance: 0.05
[... 665 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports one problem: the 8.7e-12 value isn't in the text. Next I'm reading the rest of the paper to check every claim.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt",
 "offset": 144,
 "limit": 143
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.35587.txt",
 "offset": 287,
 "limit": 190
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "NOT FOUND\|def .*value\|10-\|x 10" tools/claims_check.py | head -40
```

```
64:    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
69:        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
90:                print("QUOTE NOT FOUND", c["id"])
98:                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
```

**Agent calls Bash**

```bash
cd  sed -n 55,100p tools/claims_check.py
```

```
if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import sys; sys.path.insert(0,'tools')
from claims_check import printed_forms, flattenings
t=open('paper/10.7554-elife.35587.txt').read()
for v in [1.60e-59, 8.70e-12]:
  fs=printed_forms(v); print(v, sorted(fs)); print([f for f in fs for x in flattenings(t) if f in x])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    value: 0.2\n    tolerance: 0.13",
 "new_string": "    value: 0.21\n    tolerance: 0.12"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "  - about: each of the other 15 penetrations, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 0.001\n    p_relation: <\n    n: 15 penetrations, from 10 and 104 to 365 and 295 pairs (Supplementary file 1)",
 "new_string": "  - about: other penetration 1, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 3.34e-23\n    n: 137 cNE pairs and 630 non-cNE pairs\n  - about: other penetration 2, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 2.46e-13\n    n: 123 cNE pairs and 362 non-cNE pairs\n  - about: other penetration 3, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 5.03e-49\n    n: 244 cNE pairs and 936 non-cNE pairs\n  - about: other penetration 4, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 3.18e-30\n    n: 162 cNE pairs and 664 non-cNE pairs\n  - about: other penetration 5, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.48e-5\n    n: 10 cNE pairs and 104 non-cNE pairs\n  - about: other penetration 6, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.68e-50\n    n: 283 cNE pairs and 931 non-cNE pairs\n  - about: other penetration 7, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 4.49e-10\n    n: 60 cNE pairs and 156 non-cNE pairs\n  - about: other penetration 8, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 5.44e-12\n    n: 180 cNE pairs and 550 non-cNE pairs\n  - about: other penetration 9, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 2.06e-16\n    n: 63 cNE pairs and 416 non-cNE pairs\n  - about: other penetration 10, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.54e-13\n    n: 170 cNE pairs and 554 non-cNE pairs\n  - about: other penetration 11, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.73e-18\n    n: 365 cNE pairs and 295 non-cNE pairs\n  - about: other penetration 12, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 6.89e-17\n    n: 269 cNE pairs and 523 non-cNE pairs\n  - about: other penetration 13, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.05e-18\n    n: 266 cNE pairs and 534 non-cNE pairs\n  - about: other penetration 14, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.15e-11\n    n: 50 cNE pairs and 262 non-cNE pairs\n  - about: other penetration 15, Figure 6-figure supplement 1\n    test: Mann-Whitney U test\n    p: 1.15e-23\n    n: 212 cNE pairs and 601 non-cNE pairs"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    comment, under which a sign is defined; reading (b) is shown as a variant. Reproduced when\n    the count is within tolerance and more than 90% of member weights are positive.",
 "new_string": "    comment, under which a sign is defined; reading (b) is shown as a variant. Reproduced when\n    the count is within tolerance and more than 90% of member weights are positive; the 90% is a\n    reading of \"vast majority\", not the paper's."
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    MI from the PSTH r(t) and its mean (Brenner et al., 2000), extrapolated to infinite data from\n    20 subsamples at 90 to 100% of the bins; the larger",
 "new_string": "    MI from the PSTH r(t) and its mean (Brenner et al., 2000), extrapolated to infinite data by a\n    line through the means of 20 random subsamples at each of 90, 95, 97.5, 99 and 100% of the\n    time bins against the inverse fraction, the intercept being the MI; the larger"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "  - about: example recordings (Figure 9-figure supplement 2B), each\n    test: Mann-Whitney U-test\n    p: 0.001\n    p_relation: <\n    n: 3 recordings\n  criterion:",
 "new_string": "  - about: example recording 1 (Figure 9-figure supplement 2B), cNE against non-cNE pairs\n    test: Mann-Whitney U-test\n    p: 5.24e-14\n    n: 204 and 261 pairs\n  - about: example recording 2 (Figure 9-figure supplement 2B), cNE against non-cNE pairs\n    test: Mann-Whitney U-test\n    p: 2.75e-49\n    n: 237 and 583 pairs\n  - about: example recording 3 (Figure 9-figure supplement 2B), cNE against non-cNE pairs\n    test: Mann-Whitney U-test\n    p: 3.26e-43\n    n: 329 and 337 pairs\n  criterion:"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent**

Next: the fig9s2 per-recording test, the fig11c Bonferroni family, and the fig11ef data source.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    Reproduced when, under one reading, the paired t-test over recordings gives p < 0.001 with\n    cNE pairs higher; partially reproduced when p < 0.05.",
 "new_string": "    The per-recording medians of cNE and non-cNE pairs go into the paired t-test (legend C). Per\n    recording, a Mann-Whitney U test of cNE against non-cNE pairs (legend B) gives the number of\n    the 16 recordings where cNE pairs are higher with p < 0.001, for the statement's \"in each\".\n    Reproduced when, under one reading, the paired t-test over recordings gives p < 0.001 with\n    cNE pairs higher and all 16 per-recording tests do; partially reproduced when only the\n    paired t-test does, or it gives only p < 0.05."
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    with the STRF of the same recording. Bonferroni over the three model comparisons. Reproduced",
 "new_string": "    with the STRF of the same recording. Bonferroni over the three model comparisons of the\n    panel, a reading, as the paper does not name the family (Figure 11 legend; Supplementary\n    file 1 lists three comparisons per panel). Reproduced"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    of each model; all divided by the real CR. Bins of 10 ms, the detection bin, as the paper\n    names no other. The repeat CR needs",
 "new_string": "    of each model; all divided by the real CR. The CR bin is open; 10 ms, the detection bin, is\n    taken as the paper names no other, and stated as an assumption. Which recordings the groups\n    come from is open: the Methods take real and repeat CRs from presentations of one stimulus,\n    which fits the 15 repeats of the 10-min RN, while the models are defined on the 16\n    recordings. Readings (a) groups from cNEs detected on the repeated RN data, all CRs there;\n    (b) groups from cNEs of the 16 recordings for real and model CRs, repeat CRs from the\n    repeated RN data. The repeat CR needs"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -5 claims/see-2018.yaml; grep -n "^checks" claims/see-2018.yaml
```

```
tolerance: 0.074
  criterion: STRF similarity is the correlation of a unit's model STRF with its real STRF, by
    spike-triggered average; median over all units and iterations. "Close to zero" is read as an
    absolute median below 0.1, a reading not fixed by the paper. Reproduced when the PR median is
    within tolerance and both other medians are below 0.1 in absolute value.
```

**Agent calls Bash**

```bash
cd  grep -n -A8 "^checks" claims/dana-2016.yaml | head -20
```

```
863:checks:
864-- date: '2026-11-11'
865-  kind: agent
866-  model: claude-opus-5-5
867-  ready: true
868-  changes:
869-  - "culture-jrgeco1a-sensitivity: the 0.8 to 1.25 bound for 'similar' is now labelled a choice made here, as the paper gives none."
870-  - "culture-jrcamp1-dynamic-range: the criterion compared 160 with 80 APs, but the text does not list the AP numbers of Figure 2c; now judged as dF/F0 rising with each tested AP number up to 160, named as a choice; noted that 'dynamic range' is defined only in the source-data table, which is not in the text."
871-  - "v1-half-decay: added the test of the mApple against mRuby part of the statement (each mApple value shorter than each mRuby value), which the criterion left untested."
```

**Agent calls Bash**

```bash
cd  cat >> claims/see-2018.yaml <<'EOF'
checks:
- date: '2026-11-11'
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - "fig2eg-distance-weak: expected value 0.2 with tolerance 0.13 gave 0.07 to 0.33, not the 0.09 to 0.33 the criterion states (10 to 30% widened by 10% of each bound); now 0.21 with tolerance 0.12."
  - "fig6j-sharpness-cne-pairs: the 15 other penetrations were one entry with the legend's bound p < 0.001; replaced by one entry per test with the exact p and the pair counts of Supplementary file 1, as the protocol asks one entry per test."
  - "fig9s2-noise-correlations: the three example recordings were one entry with p < 0.001; replaced by one entry each with the exact p and pair counts of Supplementary file 1. The criterion tested only the paired t-test, while the statement says cNE pairs were higher in each of the 16 recordings (legend B, 'All recordings'); a per-recording Mann-Whitney U test from legend B is added."
  - "fig9c-cne-events-more-mi: the extrapolation was given as 20 subsamples at 90 to 100% of the bins; now the Methods' 20 iterations at each of 90, 95, 97.5, 99 and 100% of time bins with a line against the inverse fraction (Materials and methods, MI analysis on 5-s repeats)."
  - "fig7-negative-weights: the 90% bound for 'vast majority' is now labelled a reading, as the paper gives none."
  - "fig11c-models-number: the Bonferroni family (three comparisons per panel) is now labelled a reading, as the paper does not name it."
  - "fig11ef-coincidence-ratios: the 10-ms CR bin is now stated as an assumption; added that the recordings the groups come from are open (the Methods take real and repeat CRs from presentations of one stimulus, which fits the 15 repeats of the 10-min RN, while the models are run on the 16 recordings), with two readings."
  - "Open, not settled: tools/claims_check.py reports fig10s1-random-group-strfs p 8.70e-12 as not found; it is printed in Supplementary file 1 (10 - figure supplement 1E, '8.70 x 10-12'); the checker drops the trailing zero. 1.60e-59 passes only through a spurious match, but is also printed there (10C)."
  - "Open, not settled: the PWC lag bin and range (fig2bd-pwc-measures-covary and the claims that use its sharpness) are not fixed by the paper; the Results name a 10-ms resolution for the correlation analysis, which cannot give the reported ~2 ms median sharpness, so the 1-ms readings rest on an assumption."
EOF
python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/see-2018.yaml",
 "old_string": "    come from is open: the Methods",
 "new_string": "    come from is open; the Methods"
}
```

```
The file claims/see-2018.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s+[^-#'\"].*: " claims/see-2018.yaml | grep -vE "^\s*[0-9]+:\s+(- )?[a-z_]+: " | head; python tools/claims_check.py claims/see-2018.yaml paper/10.7554-elife.35587.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked `claims/see-2018.yaml` against the paper and made seven corrections. The file is ready for an attempt.

**Checker result:** `claims/see-2018.yaml: 31 claims, 31 quotes, 40 statistical values, 1 problems`. All 31 quotes match the text word for word. The one problem is `VALUE NOT FOUND fig10s1-random-group-strfs 8.7e-12`, and it is the checker's fault, not the file's: the paper prints the value as "8.70 x 10-12" (Supplementary file 1, row 10 - figure supplement 1E), and the checker drops the trailing zero when it searches. The 1.60e-59 value has the same issue; it passes only because of an accidental match, and it is also printed there.

**Changes, by claim:**
- **fig2eg-distance-weak:** the expected value 0.2 ± 0.13 covered 0.07 to 0.33, but the range the criterion states is 0.09 to 0.33 (10 to 30%, each bound widened by 10%). Changed to 0.21 ± 0.12.
- **fig6j-sharpness-cne-pairs:** the 15 other penetrations were one entry with the bound p < 0.001. Replaced with one entry per test, using the exact p and pair counts from Supplementary file 1.
- **fig9s2-noise-correlations:**
  - The three example recordings now have their exact p-values and pair counts.
  - The statement says cNE pairs were higher in every recording, but the criterion only tested the paired t-test across recordings. I added the per-recording Mann-Whitney U test from legend B.
- **fig9c-cne-events-more-mi:** the extrapolation step now matches the Methods exactly: 20 iterations at each of 90, 95, 97.5, 99 and 100% of time bins, with a line fitted against the inverse fraction.
- **fig7-negative-weights:** the criterion's 90% cut-off for "vast majority" is now labelled as a reading, since the paper gives no number.
- **fig11c-models-number:** applying Bonferroni across the three comparisons in the panel is now labelled as a reading, since the paper does not say which comparisons the correction covers.
- **fig11ef-coincidence-ratios:**
  - The 10-ms bin for the coincidence ratio is now stated as an assumption.
  - Which recordings the groups come from is now marked open, with two readings. The Methods take real and repeat ratios from presentations of one stimulus, which fits the 15 repeats of the 10-min stimulus, but the models are run on the 16 recordings.

Every other claim matches the paper in its statement, source, statistics and tolerances. The paper's main findings all have claims, and nothing comes from outside the paper.

**Open:**
- The paper does not fix the lag bin or lag range for the pairwise correlation functions. This affects fig2bd and the sharpness claims that build on it. The paper's 10-ms resolution cannot produce the reported ~2 ms median sharpness, so the file's 1-ms readings rest on an assumption.
- The checker's trailing-zero problem above. It is recorded under `checks`, and the file is otherwise clean.

**Ready:** yes, recorded as `ready: true` in a new `checks` entry dated 2026-11-11. Nothing is committed or pushed.

## End of run

25 turns, 3 minutes, $1.31 at API prices, result: success.
