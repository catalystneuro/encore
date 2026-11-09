# 001051 · claims-check · run 39845996935

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001051/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/001051/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001051/10.1016-j.neuron.2024.06.015.yaml"
}
```

```
1	# Claims for Bennett, Ouellette, Ramirez et al. (2024), "SHIELD: Skull-shaped hemispheric implants
2	# enabling large-scale electrophysiology datasets in the mouse brain", Neuron 112, 2869-2885, on
3	# dandiset 001051.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, protocol
5	# pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (PDF supplied by a person, extracted to paper/...txt), main text,
8	# figure legends, STAR Methods (pages e1 to e8) and the supplemental information (legends of Figures
9	# S1 to S6). The supplement holds figure legends only; its numbers are quoted from those legends.
10	#
11	# Code read: https://github.com/AllenInstitute/SHIELD_Dynamic_Gating_Analysis at commit 3c09a0dc
12	# (2024-07-22; Zenodo doi:10.5281/zenodo.11494005 per the paper). It holds
13	#   analysis_notebooks/DynamicGating_ephys_metrics.ipynb (Figures 1C, 4C to 4G, S4A; the list of 87
14	#     sessions passing ephys QC in cell 26, the counts 25 mice, 87 experiments, 467 insertions),
15	#   analysis_notebooks/DynamicGating_4hz_analysis.ipynb (Figures 7B to 7F and 8D to 8F),
16	#   batch_processing/run_4Hz_bursts.py and run_4Hz_analysis.py (alpha-event detection, CCGs, PSTHs,
17	#     pupil and running around events, random times), analysis_utils.py (event detector, CCG),
18	#   make_dg_unit_tensor*.py (spike tensors for image flashes and VISp events), run_im115_responses.py
19	#     (Figure 4G), run_rfs_dg.py (RF metrics via brain_observatory_utilities ReceptiveFieldMapping_VBN),
20	#     dg_plot_firing_rate_drift_over_session.py (Figure S4I counts),
[... 844 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n "0.77\|1.8\|r = \|weakly" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "offset": 200,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "offset": 1,
 "limit": 199
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "offset": 760,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2024.06.015.txt",
 "offset": 1430,
 "limit": 725
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && (which pdftoppm mutool; python -c "import fitz; print(fitz.__doc__)") 2>&1; grep -n "VALUE NOT FOUND\|def \|garbl\|�" tools/claims_check.py | head -40
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
9:checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
98:                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
105:def main() -> int:
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd claims/001051 && python - <<'EOF'
p='10.1016-j.neuron.2024.06.015.yaml'
s=open(p).read()
reps=[
("""  statement: Activity during post-stimulus VISp alpha events is correlated with activity during the
    preceding stimulus (r = 0.77, p = 1.8e-6), as if events replay recent stimulation.""",
"""  statement: Activity during post-stimulus VISp alpha events is weakly but significantly correlated
    with activity during the preceding stimulus (r = 0.77, p = 1.8e-6), as if events replay recent
    stimulation."""),
("""    must show it. A per-unit correlation (S6E) is shown as a variant.""",
"""    must show it. A per-unit correlation (S6E) is shown as a variant. The paper's numbers favour the
    S6F inset: a Pearson r of 0.77 gives p = 1.8e-6 at about 28 points (7 sessions of four), while a
    per-unit correlation over hundreds of units would give a far smaller p. The text prints the p
    value with a garbled minus sign (1.8e?6)."""),
("""  statement: MOp alpha events enhance coherence of MOp with SSp, PO, MRN and the intermediate layers of
    the superior colliculus (SCiw).""",
"""  statement: MOp alpha events enhance coherence of MOp with SSp, PO, MRN and the deep layers of the
    superior colliculus (SCiw)."""),
("""    at 20 Hz (Methods, Optotagging in the midbrain); the test is not named; open. Readings (a)
    Wilcoxon signed-rank across trials of the count in each pulse against an equal pre-train window
    (the Methods' default paired test); (b) the same on the 10 ms after each pulse onset. Reproduced
    when tagged units exist and the deepest is within tolerance.""",
"""    at 20 Hz (Methods, Optotagging in the midbrain); the test is not named; per pulse, the Wilcoxon
    signed-rank test across trials of the spike count in the 10 ms pulse against an equal window
    before the train (the Methods' default paired test). Which trials enter is open, since trials ran
    at several laser powers (50 per power, powers not given). Readings (a) all powers pooled; (b) each
    power separately, a unit tagged when it passes at any power. Reproduced when tagged units exist
    and the deepest is within tolerance."""),
("""    Figure 4E code uses p < 0.05 (cell 58); shown as a variant. A claim of absence; reproduced when
    p >= 0.05 under the Methods threshold.""",
"""    Figure 4E code uses p < 0.05 (cell 58); shown as a variant. A claim of absence; reproduced when
    p >= 0.05 under the Methods threshold. Figure 4E prints p = 0.39 for this panel, the text 0.38;
    both are reported."""),
("""  criterion: Insertions per mouse are the distinct probe insertions with units across the mouse's
    QC-passing sessions (code cell 32, distinct probe_id per mouse_id). Holes per mouse need the
    implant hole of each insertion; no code. Tolerances are the paper's stated SD.""",
"""  criterion: Insertions per mouse are the distinct probe insertions with units (code cell 32, distinct
    probe_id per mouse_id). Which sessions count is open. Readings (a) the 87 QC-passing sessions, as
    the code; (b) all sessions of each mouse, as the S4A legend says "over all recording days". Under
    (a) the mean is at most 467 / 25 = 18.7. Holes per mouse need the implant hole of each insertion;
    no code. Tolerances are the paper's stated SD."""),
("""    changes is not stated; readings (c) mean; (d) median. Reproduced, for each of VISp and MOp, when
    pupil is smaller and running lower at events at p < 0.05 and the VISp change is within tolerance
    under a reading.""",
"""    changes is not stated; readings (c) mean; (d) median. The text gives the 25% for alpha events
    without naming the area; readings (e) VISp events; (f) MOp events; (g) both pooled. Reproduced,
    for each of VISp and MOp, when pupil is smaller and running lower at events at p < 0.05 and the
    change is within tolerance under a reading."""),
("quantity: VISp units with significant RF, day 1","quantity: VISp units in the population response, day 1"),
("quantity: VISp units with significant RF, day 2","quantity: VISp units in the population response, day 2"),
("quantity: VISp units with significant RF, day 3","quantity: VISp units in the population response, day 3"),
("quantity: VISp units with significant RF, day 4","quantity: VISp units in the population response, day 4"),
("""    of image im115_r (run_im115_responses.py;""",
"""    of image im115_r (the Figure 4G legend gives unit counts only, 595, 482, 536 and 446 from 12, 11,
    12 and 11 mice; the selection by significant RF is the code's, run_im115_responses.py;"""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && grep -rn -A8 "^checks:" claims/*/*.yaml | head -30
```

```
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000005/10.1038-nn.4412.yaml-1093-- date: 2026-10-20
claims/000005/10.1038-nn.4412.yaml-1094-  kind: agent
claims/000005/10.1038-nn.4412.yaml-1095-  model: claude-opus-5-5
claims/000005/10.1038-nn.4412.yaml-1096-  ready: true
claims/000005/10.1038-nn.4412.yaml-1097-  changes:
claims/000005/10.1038-nn.4412.yaml-1098-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
claims/000005/10.1038-nn.4412.yaml-1099-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
claims/000005/10.1038-nn.4412.yaml-1100-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
--
claims/000006/10.1038-s41586-018-0642-9.yaml:841:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml-842-- date: "2026-10-20"
claims/000006/10.1038-s41586-018-0642-9.yaml-843-  kind: agent
claims/000006/10.1038-s41586-018-0642-9.yaml-844-  model: claude-opus-5-5
claims/000006/10.1038-s41586-018-0642-9.yaml-845-  ready: true
claims/000006/10.1038-s41586-018-0642-9.yaml-846-  changes:
claims/000006/10.1038-s41586-018-0642-9.yaml-847-  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
claims/000006/10.1038-s41586-018-0642-9.yaml-848-    the zero weight of a neuron with rank-sum p of 1 in DirectionVector, and the epoch means taking time > start
claims/000006/10.1038-s41586-018-0642-9.yaml-849-    and <= end, unlike the CD windows.
--
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/001051/10.1016-j.neuron.2024.06.015.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - figs6-replay. Statement now says "weakly but significantly correlated", as the paper does. Criterion notes that r = 0.77 with p = 1.8e-6 fits about 28 points (the S6F inset, 7 sessions of four), not a per-unit correlation.
  - figs6-replay. The checker did not find p = 1.8e-6; the text prints it as "1.8e" with a garbled minus sign before the 6 (Results, paragraph 5 of the alpha section). Confirmed by reading.
  - fig7f-mop-network. Statement said "intermediate layers" of the superior colliculus; the paper says "deep layers of the superior colliculus (SCiw)".
  - fig6ef-optotagging-mrn. The two readings of the tagging test were the same window (the pulse lasts 10 ms). Replaced them with the open detail the Methods do leave, which trials enter (powers pooled, or each power separately).
  - fig4ef-rf-fraction-stable. Added that Figure 4E prints p = 0.39 for this panel against 0.38 in the text; both are reported.
  - figs4ab-insertions-per-mouse. The S4A legend counts insertions "over all recording days", and 467 insertions over 25 mice give at most 18.7 per mouse. Named the session set as open, readings the 87 QC-passing sessions or all sessions.
  - fig7b-low-arousal. The text gives the 25% pupil change for alpha events without naming the area; the criterion tested VISp only. Added readings VISp, MOp, or both pooled.
  - fig4g-visual-responses-similar. The expected unit counts were labelled as units with significant RF; the Figure 4G legend gives only unit and mouse counts. Relabelled them and said the RF selection is the code's.
  - Open. fig3fh-mri-deformation. Which pairs in Figure 3H carry the asterisk could not be read from the text; the readings stand.
  - Open. fig4d-qc-metrics-comparable. Reading (a), the code's Mann-Whitney test, is significant in the code's own output, so the readings will likely disagree and the claim be methods_underspecified; reading (b), medians within 10%, is a standard choice not taken from the paper.
  - Open. fig7e-lags-straddle-zero. The criterion judges the claim on the code's signed-rank test of lags against zero, whose printed output is significant for all seven pairs; the paper names no test, and its "straddled zero" may describe the spread of lags. Left as written, since the code is the only source of a test.
EOF
python tools/claims_check.py claims/001051/10.1016-j.neuron.2024.06.015.yaml paper/10.1016-j.neuron.2024.06.015.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/    S6F inset: a Pearson r of 0.77/    S6F inset, since a Pearson r of 0.77/' claims/001051/10.1016-j.neuron.2024.06.015.yaml && python tools/claims_check.py claims/001051/10.1016-j.neuron.2024.06.015.yaml paper/10.1016-j.neuron.2024.06.015.txt; python -c "
import yaml,re;d=yaml.safe_load(open('claims/001051/10.1016-j.neuron.2024.06.015.yaml'));print(d['checks'][-1]['ready'],len(d['checks'][-1]['changes']))"
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for DANDI:001051 is ready for an attempt. I corrected eight claims from the paper and left three problems open.

**Checker result:** `45 claims, 45 quotes, 16 statistical values, 1 problems`. The one problem is figs6-replay's p = 1.8e-6. The value is right: the text prints it with a garbled minus sign ("1.8e�6"), and I confirmed it by reading.

**Changes, by claim:**
- **figs6-replay:** The statement now says "weakly but significantly correlated", as the paper does. I added a note to the criterion: r = 0.77 with p = 1.8e-6 fits about 28 points, which matches the S6F inset (7 sessions of four points each). A per-unit correlation over hundreds of units would give a much smaller p.
- **fig7f-mop-network:** The statement said "intermediate layers" of the superior colliculus. The paper says "deep layers of the superior colliculus (SCiw)", so I changed it.
- **fig6ef-optotagging-mrn:** The two readings of the tagging test described the same 10 ms window. I replaced them with a detail the Methods really leave open: which trials enter, since trials ran at several laser powers (all powers pooled, or each power separately).
- **fig4ef-rf-fraction-stable:** Added that Figure 4E prints p = 0.39 where the text says 0.38. Both are reported.
- **figs4ab-insertions-per-mouse:** The Figure S4A legend counts insertions "over all recording days", and 467 insertions over 25 mice give at most 18.7 per mouse, below the paper's 20. Which sessions count is now open, with two readings: the 87 QC-passing sessions, or all sessions.
- **fig7b-low-arousal:** The text gives the ~25% pupil change without naming the area, but the criterion tested VISp only. I added readings for VISp events, MOp events, or both pooled.
- **fig4g-visual-responses-similar:** The expected unit counts were labelled "units with significant RF", but the Figure 4G legend gives only unit and mouse counts. I relabelled them and noted that the RF selection comes from the code.

All changes are recorded under `checks` with their reasons, and the entry has `ready: true`.

**Still open (recorded in the file):**
- **fig3fh-mri-deformation:** The text does not say which pairs in Figure 3H carry the asterisk, and I could not open the figure here. The existing readings stand.
- **fig4d-qc-metrics-comparable:** Reading (a), the code's Mann-Whitney test, is significant in the code's own printed output, so the two readings will probably disagree and the claim end up `methods_underspecified`. Reading (b), medians within 10%, is a standard choice that does not come from the paper.
- **fig7e-lags-straddle-zero:** The paper names no test. The criterion uses the code's signed-rank test, which is significant for all seven pairs in its printed output, while the paper's "straddled zero" may describe the spread of lags. I left it as written because the code is the only source of a test.

I could not read the linked analysis code, so the claims' references to specific code cells are taken on trust. Each of the paper's main findings has a claim, and every claim comes from this paper. Nothing was committed or pushed.

## End of run

14 turns, 2 minutes, result: success.
