# 000013 · claims-check · run 39600374723

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000013/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/000013/10.7554-elife.06619.yaml paper/10.7554-elife.06619.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/000013/10.7554-elife.06619.yaml
```

```
<persisted-output>
Output too large (60.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9f8b883e-2c46-4557-8b1f-0de84bf4f111/tool-results/bey382sxp.txt

Preview (first 2KB):
# Claims for Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife 4, e06619, "Low-noise encoding
# of active touch by layer 4 in the somatosensory cortex", on dandiset 000013.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record (PMC4525079) as served by Europe PMC
# (paper/10.7554-elife.06619.txt): Introduction, Results, Discussion, Materials and methods, Table 1,
# the legends of Figures 1 to 6 and of their figure supplements (Figure 1, supplements 1 and 2;
# Figure 2, supplement 1; Figure 3, supplements 1 and 2; Figure 4, supplement 1; Figure 6,
# supplement 1), the decision letter and the author response. eLife has no supplement beyond
# these figure supplements, whose legends are in the text. No PDF was supplied, so the figure
# images were not read. Table 1 came through as one run of text; its columns were read in order
# (9 measures, rows of mean +- s.d., median and range for each of three populations). One cell of
# it is garbled, the L5 "Spikes evoked (touch)" mean printed "24.0-18.6%", read as 24.0 +- 18.6%
# from Results, paragraph on Figure 3C.
#
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000013/10.7554-elife.06619.yaml"
}
```

```
1	# Claims for Hires, Gutnisky, Yu, O'Connor & Svoboda (2015), eLife 4, e06619, "Low-noise encoding
2	# of active touch by layer 4 in the somatosensory cortex", on dandiset 000013.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
4	# pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the version of record (PMC4525079) as served by Europe PMC
7	# (paper/10.7554-elife.06619.txt): Introduction, Results, Discussion, Materials and methods, Table 1,
8	# the legends of Figures 1 to 6 and of their figure supplements (Figure 1, supplements 1 and 2;
9	# Figure 2, supplement 1; Figure 3, supplements 1 and 2; Figure 4, supplement 1; Figure 6,
10	# supplement 1), the decision letter and the author response. eLife has no supplement beyond
11	# these figure supplements, whose legends are in the text. No PDF was supplied, so the figure
12	# images were not read. Table 1 came through as one run of text; its columns were read in order
13	# (9 measures, rows of mean +- s.d., median and range for each of three populations). One cell of
14	# it is garbled, the L5 "Spikes evoked (touch)" mean printed "24.0-18.6%", read as 24.0 +- 18.6%
15	# from Results, paragraph on Figure 3C.
16	#
17	# Code read: the paper links the Janelia Whisker Tracker (openwiki.janelia.org, not code for the
18	# analyses) and https://github.com/hireslab/HLab_Whiskers for the detection of contact periods.
19	# Read at HEAD, commit cdbc9148da6c505ba940b971fbe419b11cb80049 (2020-12-11); the last commit
20	# before publication is 0eb360a (2014-11-19). It holds MATLAB classes for behaviour trials (+Solo),
[... 956 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.06619.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "offset": 977
}
```

```
977	  expected:
978	  - quantity: modulation index by touch order, mean over 31 cells
979	    value: 0.71
980	    tolerance: 0.25
981	  - quantity: modulation index by pre-touch velocity, mean
982	    value: 0.71
983	    tolerance: 0.27
984	  - quantity: modulation index by maximum curvature, mean
985	    value: 0.72
986	    tolerance: 0.23
987	  criterion: Figure 5 legend. Per L4 C2 cell, touches sorted by the property and split into 10
988	    bins with equal numbers of touches; the mean spikes per touch in the cell's spike integration
989	    window (touch spike window) per bin; modulation index (max bin - min bin)/(max bin + min bin).
990	    Properties, order of the touch in its trial; whisker velocity at touch onset (d theta/dt);
991	    maximum curvature change during the touch. Open details, (1) velocity, read as (a) the
992	    velocity at the onset frame or (b) the mean over the 1 to 5 ms before onset; (2) curvature,
993	    read as (a) max |Delta kappa| over the whole touch or (b) over 0 to 20 ms after onset (the
994	    window of the Methods for clustering); (3) touch order, where ties make equal bins
995	    impossible, read as (a) ranks with ties broken at random or (b) bins of whole order values
996	    as near equal as they can be. Reproduced when all three means are within tolerance under all
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.7554-elife.06619.txt').read()
i=t.find('Each neuron was characterized by a curve')
print(t[i:i+16000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "close to 1\|example-cell-phase\|Decision letter\|decision letter" claims/000013/*.yaml | head; grep -n "VALUE NOT FOUND\|def .*p\b\|e-0\|format" tools/claims_check.py | head -40; ls claims/*/ | head -3; grep -rn "kind: agent" claims/ | head -3
```

```
10:# supplement 1), the decision letter and the author response. eLife has no supplement beyond
98:                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
claims/000003/:
10.1016-j.neuron.2016.12.011.yaml

claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml:1296:  kind: agent
claims/001752/10.1038-s41556-026-02009-4.yaml:636:  kind: agent
claims/001676/10.1038-s41586-025-10096-w.yaml:1114:  kind: agent
```

**Agent calls Bash**

```bash
sed -n 60,110p tools/claims_check.py; sed -n 1280,1320p claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml
```

```
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
    return {f.lower() for f in out}


def check(claims_path: Path, paper_paths: list[Path]) -> int:
    doc = yaml.safe_load(claims_path.read_text())
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.7554-elife.06619.txt').read()
i=t.find('Decision letter')
print(len(t), i)
j=t.find('Author response')
print(j)
import re
k=max(i,0)
print(t[k:k+40000])" | fold -w 4000 | head -c 45000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.7554-elife.06619.txt').read()
j=t.find('Author response')
print(t[j:j+60000])" > $TMPDIR/ar.txt; wc -c $TMPDIR/ar.txt; grep -o -i ".\{300\}\(latenc\|shuffl\|velocity\|circular\|optimal threshold\|first touch\|exploration\).\{300\}" $TMPDIR/ar.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker flags only two p-values (2.30e-5, 1.0e-5), and both are printed in the paper with trailing zeros, so the values are correct. Now making corrections.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  criterion: Methods, Spikes accounted by active sensation. Exploration time is whisking epochs\n    with touch epochs, leaving out touches >100 ms. Each spike",
 "new_string": "  criterion: Methods, Spikes accounted by active sensation. Exploration time is whisking epochs\n    with touch epochs, leaving out touches >100 ms, within the sample epoch (Results, paragraph\n    7, \"during whisking or touch in the sample epoch (exploration time)\"). Each spike"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  criterion: As fig3c-touch-spikes-l4c2, with its readings. Cells without a touch latency\n    (latency-determinable) have no touch window and count as 0% of spikes and time. Reproduced\n    when both values",
 "new_string": "  criterion: As fig3c-touch-spikes-l4c2, with its readings. The paper does not say how the touch\n    window is placed for the six cells without a touch latency (latency-determinable). Table 1\n    gives this group a median of 3.6% and a range of 0 to 41.0%, so at most four of the 10 cells\n    are at 0%, and those six were not all set to 0%. Readings, (a) the latency taken as 0 ms\n    (window from touch onset) for cells without one; (b) the latency from the all-touch PCTH where\n    the first-touch PCTH gives none, then (a) for any cell still without one. Both are run; the\n    outcome is the one both give, else methods_underspecified. Setting those cells to 0% is shown\n    as a variant. Reproduced when both values"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "(3) the\n    window searched after onset, read as (a) 0 to 50 ms, the post-touch span of the decoding\n    analysis, or (b) up to the cell's touch response cutoff. All combinations of (1) and (3) are\n    shown; the outcome is the one they all give, else methods_underspecified.",
 "new_string": "(3) the\n    window searched after onset, not given, read as 0 to 50 ms, the post-touch span of the\n    touch-aligned responses in the Methods (Population decoding). The cell's touch response cutoff\n    cannot bound the search, as it is computed from spikes indexed after the latency. Both\n    readings of (1) are shown; the outcome is the one they both give, else\n    methods_underspecified."
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "read as (a) the fraction of touches detected at the best\n    post-touch time point, with the threshold set for equal error, or (b) the percent correct\n    over touch and non-touch samples;",
 "new_string": "read as (a) the fraction of touches detected at the best\n    post-touch time point or (b) the percent correct over touch and non-touch samples, at the\n    best post-touch time point, in both cases with the threshold that maximizes percent correct\n    on the training half (the Methods' \"optimal threshold\");"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "read as (a) the\n    velocity at the onset frame or (b) the mean over the 1 to 5 ms before onset;",
 "new_string": "read as (a) the\n    velocity at the onset frame (\"at touch onset\", Figure 5A legend) or (b) the velocity in the\n    frame before onset (\"just before touch\", Results; \"pretouch velocity\", Methods);"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  criterion: For the cell identified in example-cell-rates, spike counts in 10 ms windows slid in\n    1 ms steps",
 "new_string": "  criterion: Figure 6A and B call this neuron \"an example neuron\" and do not say it is the cell of\n    Figures 1, 3 and 5. Readings, (a) the cell identified in example-cell-rates; (b) any L4 C2\n    cell, the number of cells that match being reported. Spike counts in 10 ms windows slid in\n    1 ms steps"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -n -A10 "Figure 6A and B call" claims/000013/10.7554-elife.06619.yaml
```

```
298:  criterion: Figure 6A and B call this neuron "an example neuron" and do not say it is the cell of
299-    Figures 1, 3 and 5. Readings, (a) the cell identified in example-cell-rates; (b) any L4 C2
300-    cell, the number of cells that match being reported. Spike counts in 10 ms windows slid in
301-    1 ms steps around touch onset (Figure 6B), across touches with inter-contact interval >250 ms
302-    (Methods, Analysis of spike count variance). Reproduced when the mean counts match, the FF
303-    before touch is within 0.1 of 1, and the FF at the window of peak mean count is below 1.
304-    Open detail, the touches used, read as (a) the >250 ms touches pooled or (b) one of the five
305-    clustered groups; both are shown.
306-- id: text-spikes-per-touch
307-  statement: Each touch evoked on the order of one spike (1.51 spikes per first touch, 0.31 per
308-    later touch) with an onset latency of 8 ms.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "    before touch is within 0.1 of 1, and the FF at the window of peak mean count is below 1.\n    Open detail, the touches used, read as (a) the >250 ms touches pooled or (b) one of the five\n    clustered groups; both are shown.",
 "new_string": "    before touch is within 0.1 of 1, and the FF at the window of peak mean count is below 1.\n    Open detail, the touches used, read as (a) the >250 ms touches pooled or (b) one of the five\n    clustered groups; both are shown. Reproduced under reading (a) of the cell when it matches\n    there; otherwise the cells that match under (b) are reported, and the claim is reproduced only\n    if one does, with the difference from the Figure 1 cell recorded."
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  criterion: For the cell identified in example-cell-rates, the variance over its mean of the\n    per-trial spike count in the sample epoch (pole in reach), across trials.",
 "new_string": "  criterion: The variance over the mean of the per-trial spike count in the sample epoch (pole in\n    reach), across trials. The paragraph follows the example cell but does not say whose FF this\n    is, and the L4 C2 population mean for the same count is 6.57 (fig6e-sample-epoch-ff).\n    Readings, (a) the cell identified in example-cell-rates; (b) the mean over all 41 L4 cells;\n    (c) the mean over all 52 cells. Reproduced when the value is within tolerance under one\n    reading; the readings that match are said."
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  criterion: The paper reports no test. From Table 1, the L5 median non-whisking and whisking\n    rates (12.8 and 13.5 spikes/s) are many times those of L4 C2 (0.32 and 0.33). Reproduced when\n    the L5 median is above the L4 C2 median for both rates and a Wilcoxon rank sum (the paper's\n    test for group comparisons) gives p < 0.05 for both.",
 "new_string": "  criterion: The paper reports no test. From Table 1, the L5 median non-whisking and whisking\n    rates (12.8 and 13.5 spikes/s) are many times those of L4 C2 (0.32 and 0.33) and of L4\n    outside C2 (1.10 and 1.31). The sentence compares L5 with the L4 neurons of the paragraph,\n    inside and outside C2. Reproduced when the L5 median is above the median of each L4 group for\n    both rates and a Wilcoxon rank sum (the paper's test for group comparisons) gives p < 0.05\n    for all four comparisons; partially when only those against L4 C2 do."
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "  statement: For the example neuron, the Fano factor of spike counts over the whole sample epoch\n    was large, 7.51.",
 "new_string": "  statement: The Fano factor of spike counts over the whole sample epoch was large, 7.51, in the\n    paragraph on the example neuron, which does not say whose value it is."
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "    quantity: Fano factor of sample-epoch spike counts, example cell",
 "new_string": "    quantity: Fano factor of sample-epoch spike counts"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000013/10.7554-elife.06619.yaml",
 "old_string": "    Open detail, whether whisking periods include touch epochs, read both ways. Reproduced when\n    both values are within tolerance under one reading.\n",
 "new_string": "    Open detail, whether whisking periods include touch epochs, read both ways. Reproduced when\n    both values are within tolerance under one reading.\n- id: example-cell-phase-modulation\n  statement: During exploration the example neuron's spikes are coupled to whisking phase, with a\n    modulation depth close to 1 and near zero spiking at phase 0.\n  source: Results, L4 responses are temporally precise, paragraph 5; Figure 1G-H\n  quote: Yet during active exploration, the timing of spikes was coupled to the phase of rhythmic\n    whisker movement ( Fee et al., 1997 ; Curtis and Kleinfeld, 2009 ), with a modulation depth\n    close to 1\n  depends_on:\n  - example-cell-rates\n  expected:\n    quantity: phase modulation depth, example cell\n    value: 1\n    tolerance: 0.1\n  criterion: Methods, Spike analysis, and Figure 1G-H legends. For the cell identified in\n    example-cell-rates, spikes in whisking bouts (amplitude >2.5 deg) of exploration periods\n    excluding touch, assigned a phase by linear interpolation, in a 12-bin histogram of rate\n    (Figure 3, figure supplement 1C; Figure 1H uses 30 deg bins, the same); fitted with A[1 +\n    cos(theta - phi_pref)] + B, A, B > 0; depth A / (A + B). The tolerance is the protocol's 10%\n    of the paper's value 1. The rate in the bin at phase 0 is reported. Fitting as table1-l4-c2.\n"
}
```

```
The file claims/000013/10.7554-elife.06619.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/000013/10.7554-elife.06619.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. The two values flagged as not found (fig3c-touch-spikes-l5 p = 2.30e-5, fig5-modulation-correlations p = 1.0e-5) are in the text as printed with trailing zeros; both are correct and unchanged.
  - fig3c-touch-spikes-l4c2. Exploration time was not limited to the sample epoch; the Results define it as whisking or touch in the sample epoch. Added.
  - fig3c-touch-spikes-outside (and, through it, fig3c-touch-spikes-l5, fig3d claims and table1 rows). The rule that cells without a latency count as 0% was not in the paper and is contradicted by Table 1 (outside C2 median 3.6% with six of ten cells lacking a latency). Replaced with two readings for the window of such cells; the 0% rule is kept as a variant.
  - latency-determinable. Reading (b) of the search window, up to the touch response cutoff, is circular, as the cutoff is computed after the latency. Removed; the 0 to 50 ms reading remains.
  - fig4a-touch-detection-c2. The "equal error" threshold was not in the paper; the Methods use an optimal threshold found on half the data. Both performance readings now use the threshold that maximizes percent correct on the training half.
  - fig5c-modulation-index. Velocity reading (b), a mean over 1 to 5 ms before onset, was invented. Replaced with the frame before onset, from "just before touch" and "pretouch velocity".
  - example-cell-ff-around-touch. Figure 6 calls its neuron "an example neuron" and does not say it is the Figure 1 cell. Named this open, with the Figure 1 cell as the first reading and any L4 C2 cell as the second.
  - example-cell-sample-ff. The paper does not say whose FF 7.51 is. Statement and expected quantity no longer say example cell; readings (example cell, mean over L4 cells, mean over all cells) added.
  - l5-higher-rates. The sentence compares L5 with L4 inside and outside C2; the criterion compared only with L4 C2. Added L4 outside C2.
  - example-cell-phase-modulation. New claim, the example neuron's phase modulation depth close to 1 (Results, paragraph 5; Figure 1G-H), which had no claim.
  - Open. table1-l4-c2, table1-l4-outside, table1-l5. The counting rules (15 of 18, 13 of 17 values within tolerance) are the claim writer's, not the paper's.
  - Open. fig6s1b-clusters-less-variable. The paper shows the cluster variability test for one example neuron only; judging it on more than half of the cells, and on the first group, is the claim writer's choice.
  - Open. fig6d-not-refractory. The paper compares data and model only in a figure; both comparison rules (s.e.m. separation, sign test) are the claim writer's.
  - Open. fig4a-touch-detection-outside. The 95% bound rule for "poor" is not from the paper.
  - Open. whisking-rate-l4-no-change. The paper names the Wilcoxon signed rank test only for L5 in the sentence; the same test is assumed for L4.
EOF
python tools/claims_check.py claims/000013/10.7554-elife.06619.yaml paper/10.7554-elife.06619.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file, corrected eight claims, added one new claim, and recorded a `checks` entry marking it ready. Nothing was committed.

**Checker result:** `45 claims, 42 quotes, 16 statistical values, 2 problems`. Both problems are formatting, not errors. The paper prints the two p-values as "2.30e-5" (fig3c-touch-spikes-l5) and "1.0e-5" (fig5-modulation-correlations), with trailing zeros the checker doesn't match. Both values are correct and I left them as they are. Every quote matches the text word for word.

**Changes, by claim:**
- **fig3c-touch-spikes-l4c2:** exploration time was not limited to the sample epoch. The Results define it as "whisking or touch in the sample epoch", so I added that limit.
- **fig3c-touch-spikes-outside** (fig3c-touch-spikes-l5, the fig3d claims and the Table 1 rows inherit this): the rule "cells without a latency count as 0%" is made up, and Table 1 contradicts it. Six of the ten L4 cells outside C2 have no latency, yet the group median is 3.6%, so they cannot all be at 0%. I replaced the rule with two readings for where such a cell's window starts, and kept the 0% rule only as a variant.
- **latency-determinable:** one reading searched for the latency up to the touch response cutoff. That is circular, because the cutoff is computed after the latency, so I removed it.
- **fig4a-touch-detection-c2:** the "equal error" threshold is not in the paper. The Methods use an "optimal threshold" found on half the data, which I read as the one maximizing percent correct.
- **fig5c-modulation-index:** the velocity reading "mean over 1 to 5 ms before onset" was invented. I replaced it with the frame before onset, from "just before touch" and "pretouch velocity".
- **example-cell-ff-around-touch:** Figure 6 calls its neuron "an example neuron" and never says it is the Figure 1 cell. I named this as open, with two readings: the Figure 1 cell, or any L4 C2 cell.
- **example-cell-sample-ff:** the paper does not say whose FF = 7.51 is. The statement no longer says it is the example cell's. Three readings are named: the example cell, the mean over the 41 L4 cells, and the mean over all 52 cells.
- **l5-higher-rates:** the paper compares L5 with L4 cells both inside and outside C2, but the criterion only compared with L4 C2. I added L4 outside C2.
- **example-cell-phase-modulation (new):** the example neuron's phase modulation depth "close to 1" (Results, paragraph 5; Figure 1G-H) had no claim. It now has one, with the protocol's default tolerance of 10%.

**Still open** (recorded in the file, not changed):
- **table1-l4-c2, table1-l4-outside, table1-l5:** the pass rules (at least 15 of 18, or 13 of 17, values within tolerance) are the claim writer's, not the paper's.
- **fig6s1b-clusters-less-variable:** the paper shows this test for one example neuron only. Requiring it in more than half the cells, and for the first group, is the claim writer's choice.
- **fig6d-not-refractory:** the paper compares data and model only in a figure. Both comparison rules in the criterion are invented.
- **fig4a-touch-detection-outside:** the rule used to judge detection as "poor" (a 95% bound) is not from the paper.
- **whisking-rate-l4-no-change:** the paper names the Wilcoxon signed-rank test only for L5. The claim assumes the same test for L4.

**Ready:** yes, `ready: true`. The remaining problems are judgement rules on a few secondary claims, and none affects the main findings, which all have claims.

## End of run

26 turns, 3 minutes, result: success.
