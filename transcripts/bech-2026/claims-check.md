# 001847 · claims-check · run 39556182218

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001847/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/001847/10.7554-elife.109717.yaml paper/10.7554-elife.109717.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001847/10.7554-elife.109717.yaml
```

```
<persisted-output>
Output too large (60.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e4c0174a-928e-47d5-9604-02dc03f1a5e5/tool-results/bomxwnkpw.txt

Preview (first 2KB):
# Claims for Bech, Dard, Lebert, Smith, Bisi, Renard, Crochet & Petersen, "Retrosplenial cortex
# enables context-dependent goal-directed sensorimotor transformation", eLife reviewed preprint
# doi:10.7554/eLife.109717, on dandiset 001847.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data
# when these criteria were written; the reader saw only the dandiset's title and description.
#
# Text read: the eLife Reviewed Preprint, version 1 (30 December 2025, "Not revised"), full text as
# served by the publisher's HTML (paper/10.7554-elife.109717.txt): Results, figure legends,
# Discussion, Methods, "Quantification and data analysis" with its figure-specific methods, and the
# legends of the four figure supplements (Figure 1 to 4, figure supplement 1), which the text gives
# under "Supplemental information". No PDF was supplied. The figures themselves were not seen, so
# claims shown only in grid maps are tested on the sentences of the Results that describe them.
#
# Code read. The paper names a "behavior GUI repo", an "NWB converter repo" and an "NWB analysis
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001847/10.7554-elife.109717.yaml"
}
```

```
1	# Claims for Bech, Dard, Lebert, Smith, Bisi, Renard, Crochet & Petersen, "Retrosplenial cortex
2	# enables context-dependent goal-directed sensorimotor transformation", eLife reviewed preprint
3	# doi:10.7554/eLife.109717, on dandiset 001847.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
6	# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data
7	# when these criteria were written; the reader saw only the dandiset's title and description.
8	#
9	# Text read: the eLife Reviewed Preprint, version 1 (30 December 2025, "Not revised"), full text as
10	# served by the publisher's HTML (paper/10.7554-elife.109717.txt): Results, figure legends,
11	# Discussion, Methods, "Quantification and data analysis" with its figure-specific methods, and the
12	# legends of the four figure supplements (Figure 1 to 4, figure supplement 1), which the text gives
13	# under "Supplemental information". No PDF was supplied. The figures themselves were not seen, so
14	# claims shown only in grid maps are tested on the sentences of the Results that describe them.
15	#
16	# Code read. The paper names a "behavior GUI repo", an "NWB converter repo" and an "NWB analysis
17	# repo" without addresses; the dandiset's description names the two analysis repositories, which
18	# name the paper and this dandiset (version 0.260610.1400) in their READMEs:
19	#   github.com/LSENS-BMI-EPFL/Bech_Dard_process_NWB at 212a63103528cdeafb6ebcf90a50235cd2290082
20	#     (2026-06-30), scripts main_analysis/figure1_analysis.py to figure4_analysis.py,
[... 896 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109717.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109717.txt",
 "offset": 390,
 "limit": 443
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109717.txt",
 "offset": 390,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.109717.txt",
 "offset": 450,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR>539 && length($0)>300' paper/10.7554-elife.109717.txt | cut -c1-300; ls; ls tools; git log --oneline -3 -- claims/001847
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "VALUE NOT FOUND" -B40 tools/claims_check.py | grep -n "def \|x 10\|re\.\|format" | head -40
```

```
6:63-def printed_forms(v: float) -> set[str]:
12:69-        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
21:78-def check(claims_path: Path, paper_paths: list[Path]) -> int:
```

**Agent calls Read**

```json
{
 "file_path": "tools/claims_check.py",
 "offset": 55,
 "limit": 30
}
```

```
55	            if i < 0:
56	                break
57	            pos = i + len(f)
58	        else:
59	            return True
60	    return False
61	
62	
63	def printed_forms(v: float) -> set[str]:
64	    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
65	    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
66	    if 0 < abs(v) < 1:
67	        m, e = f"{v:.3e}".split("e")
68	        m, e = f"{float(m):g}", str(int(e))
69	        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
70	        if m == "1":
71	            out.add(f"10{e}")
72	    if 0 < abs(v) < 0.001:
73	        plain = f"{v:.12f}".rstrip("0")
74	        out |= {plain, plain.lstrip("0")}
[... 10 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    none for Figure 1E (plot utils/figure1E.py); for supplement 1E the code runs the Figure 1G\n    test, a paired t-test across mice of the last whisker trial before against the first after\n    the transition, on the Off days (plot utils/figure1_supp.py:85-125), and prints it. The test\n    is open; readings (a) a two-sided paired t-test across the 7 mice of whisker lick probability\n    in W+ against W- blocks on the Off day, (b) the code's supplement 1E test, for each transition\n    direction. Reproduced when every reading gives p >= 0.05, not reproduced when every reading\n    gives p < 0.05 with the W+ blocks higher, and otherwise blocked as methods_underspecified. The\n    W+ minus W- difference on the Off day and on the On days is reported.",
 "new_string": "    none for Figure 1E (plot utils/figure1E.py); for supplement 1E the code runs the Figure 1G\n    test, a paired t-test across mice of the last whisker trial before against the first after\n    the transition, on the Off days (plot utils/figure1_supp.py:85-125), and prints it. That is\n    the only test the paper's material holds, so the absence is judged on it alone (protocol,\n    claims of absence), for each transition direction, two-sided, p < 0.05. Reproduced when both\n    directions give p >= 0.05, not reproduced when either gives p < 0.05 in the direction of the\n    new context. A two-sided paired t-test across the 7 mice of whisker lick probability in W+\n    against W- blocks on the Off day is shown as a variant. The W+ minus W- difference on the Off\n    day and on the On days is reported."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "  criterion: As the Methods (Gradient boosted decision tree model) and the code give it. Sessions\n    are the code's 60 sessions of 21 mice (session_context_expert_behaviour_model.yaml), sessions",
 "new_string": "  criterion: As the Methods (Gradient boosted decision tree model) and the code give it. The\n    Methods say \"all expert sessions\"; the orofacial features exist only for sessions with face\n    video, and the code settles the set. Sessions\n    are the code's 60 sessions of 21 mice (session_context_expert_behaviour_model.yaml), sessions"
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    summary lists wM1/2 and ALM). Reproduced when, under a threshold and null reading, A1 and at\n    least one of wM1, wM2, ALM have a negative effect in both contexts; partially reproduced when\n    this holds in one context only. Similarity across contexts is reported as the W+ and W- mean\n    ΔP at those sites.",
 "new_string": "    summary lists wM1/2 and ALM). Reproduced when A1 and at least one of wM1, wM2, ALM have a\n    negative effect in both contexts; partially reproduced when this holds in one context only.\n    Each threshold and null reading is run; the outcome is the one they all give, otherwise\n    blocked as methods_underspecified. Similarity across contexts is reported as the W+ and W-\n    mean ΔP at those sites."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "  criterion: The opto-map rule, whisker trials. Reproduced when, under a threshold and null reading,\n    wS1, wS2 and at least one of wM1, wM2, ALM have a negative effect in both W+ and W-; partially\n    reproduced when they do in W+ only (where the whisker lick rate is high).",
 "new_string": "  criterion: The opto-map rule, whisker trials. Reproduced when wS1, wS2 and at least one of wM1,\n    wM2, ALM have a negative effect in both W+ and W-; partially reproduced when they do in W+ only\n    (where the whisker lick rate is high). Each threshold and null reading is run; the outcome is\n    the one they all give, otherwise blocked as methods_underspecified."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "  criterion: The opto-map rule, whisker trials. The RSC site is open in the code; readings (-1.5,\n    0.5), the site of Figures 3 and 4, the muscimol and tracing, and (-0.5, 0.5). Reproduced when,\n    under a threshold, null and RSC reading, tjS1 and RSC have a positive effect in W- and neither\n    has a positive effect in W+; partially reproduced when one of the two does. The mean ΔP of\n    each in both contexts is reported.",
 "new_string": "  criterion: The opto-map rule, whisker trials. RSC is the site (-1.5, 0.5); the Methods give the\n    RSC coordinates as 1.5 mm posterior to bregma and 0.5 mm lateral (Pharmacological\n    inactivation), and the tracing used \"the coordinates defined in our optogenetic and imaging\n    experiments\" (Results, paragraph 2 of the Figure 3 section). The code's second \"RSC\" site\n    (-0.5, 0.5) is a variant. Reproduced when tjS1 and RSC have a positive effect in W- and\n    neither has a positive effect in W+; partially reproduced when one of the two does. Each\n    threshold and null reading is run; the outcome is the one they all give, otherwise blocked as\n    methods_underspecified. The mean ΔP of each in both contexts is reported."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    Frontal areas are wM1, wM2 and ALM. Reproduced when, under a threshold reading, at least one\n    frontal site shows an increase passing it in a trial type, and RSC (either site reading) and\n    tjS1 show no change passing it in either trial type; partially reproduced when one of the two\n    parts holds.",
 "new_string": "    Frontal areas are wM1, wM2 and ALM; RSC is (-1.5, 0.5), as fig2e-rsc-tjs1-increase-wminus.\n    Reproduced when at least one frontal site shows an increase passing the threshold in a trial\n    type, and RSC and tjS1 show no change passing it in either trial type; partially reproduced\n    when one of the two parts holds. Each threshold reading is run; the outcome is the one they\n    all give, otherwise blocked as methods_underspecified."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    likelihood and centered on the 250 ms before the stimulus (Methods, Figure 3B). The onset rule\n    differs; readings (a) the Methods (Figure 3C), on each mouse-average trace the first time after\n    the stimulus at which the d' between jaw opening values and the pre-stimulus 250 ms is >= 1,\n    (b) the code, per trial the first time after the stimulus at which |jaw| over its pre-stimulus\n    SD exceeds 3, averaged per session, then mouse (plot utils/figure3_supp.py:602-674, criterion\n    3 in figure_files/figure3.py:34). Which trial types are pooled is open in the text; the code\n    uses auditory and whisker hits. Reproduced when, under a reading, the mean onset is within\n    tolerance (the ± is the paper's, SEM or CI width in the code).",
 "new_string": "    likelihood and centered on the 250 ms before the stimulus (Methods, Figure 3B). The onset rule\n    of the Methods and the code differ, and the Methods decide (protocol, step 2): on each\n    mouse-average trace the first time after the stimulus at which the d' between jaw opening\n    values and the pre-stimulus 250 ms is >= 1 (Methods, Figure 3C). The code's rule, per trial\n    the first time after the stimulus at which |jaw| over its pre-stimulus SD exceeds 3, averaged\n    per session, then mouse (plot utils/figure3_supp.py:602-674, criterion 3 in\n    figure_files/figure3.py:34), is a variant. Which trial types are pooled is open in the text;\n    the code uses auditory and whisker hits. Reproduced when the mean onset is within tolerance\n    (the ± is the paper's, SEM or CI width in the code)."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    exceeds half that peak. Reproduced when similarity holds and, under a reading, A1 comes before\n    RSC, RSC before wM1 or wM2, and these before tjS1 and ALM, in both contexts; partially\n    reproduced when similarity holds and A1 is first. The baseline readings are run.",
 "new_string": "    exceeds half that peak. Reproduced when similarity holds and A1 comes before RSC, RSC before\n    wM1 or wM2, and these before tjS1 and ALM, in both contexts; partially reproduced when\n    similarity holds and A1 is first. Each order and baseline reading is run; the outcome is the\n    one they all give, otherwise blocked as methods_underspecified."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    and without it as a variant. Reproduced when RSC has the earliest time in both the ROI ranking\n    and the pixel version, under every baseline reading; a tie",
 "new_string": "    and without it as a variant. Reproduced when RSC has the earliest time in both the ROI ranking\n    and the pixel version, under every baseline and every exclusion reading (the outcome is the\n    one they all give, otherwise methods_underspecified); a tie"
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "    p < 0.05. Reproduced when, under a reading, W- is higher for all seven pairs; partially\n    reproduced when it is for at least four, including one of each group the quote names.",
 "new_string": "    p < 0.05. Reproduced when W- is higher for all seven pairs; partially reproduced when it is\n    for at least four, including one of each group the quote names. Both readings are run; the\n    outcome is the one they both give, otherwise blocked as methods_underspecified."
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now I'm adding the missing claim on RSC inhibition in catch and auditory trials. First I'll check the schema's `checks` format.

**Agent calls Bash**

```bash
ls schemas; grep -n "checks" -A30 schemas/claims* | head -50; grep -rn "kind: agent" -A8 claims/*/*.yaml | head -20
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
202:    "checks": {
203-      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
204-      "type": "array",
205-      "items": {
206-        "type": "object",
207-        "additionalProperties": false,
208-        "required": [
209-          "date",
210-          "kind",
211-          "ready"
212-        ],
213-        "properties": {
214-          "date": {
215-            "type": "string",
216-            "format": "date"
217-          },
218-          "kind": {
[... 34 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "- id: fig3c-jaw-onset",
 "new_string": "- id: fig2cd-rsc-no-effect-catch-auditory\n  statement: Inhibiting RSC does not change performance in catch or auditory trials, so the effect\n    of RSC inactivation needs the context-sensitive whisker stimulus.\n  source: Results, Optogenetic inhibition drives cortical activity modes predictive of behavior,\n    paragraph 1; Figures 2C and 2D\n  quote: Importantly, inhibition of RSC in catch or auditory trials did not lead to any changes in\n    performance, indicating that the presence of the context-sensitive stimulus is necessary for\n    the effect of RSC inactivation to become apparent.\n  criterion: A claim of absence, judged on the paper's measure for Figures 2C and 2D, the d' of the\n    opto-map rule of the opening comment, 7 VGAT-ChR2 mice, at the RSC site (-1.5, 0.5) as in\n    fig2e-rsc-tjs1-increase-wminus, catch and auditory trials, W+ and W-. The paper fixes no\n    threshold; under each threshold and null reading, reproduced when RSC has no effect of either\n    sign in any of the four trial type and context groups, and not reproduced when it has one.\n    When the readings disagree, blocked as methods_underspecified. The ΔP and d' of RSC in each\n    group are reported, and the site (-0.5, 0.5) is shown as a variant.\n- id: fig3c-jaw-onset"
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/001847/10.7554-elife.109717.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1e-context-off-no-discrimination. The criterion judged the absence on two readings, one of them a test the paper and code never run. For a claim of absence the protocol judges on the paper's test alone; the only test in the paper's material is the code's supplement 1E test, which now decides, and the W+ against W- t-test is a variant.
  - fig1k-model-accuracy. Added that the Methods say "all expert sessions" while the orofacial features exist only for sessions with face video, so the code's list settles the set.
  - fig2d-auditory-a1-frontal, fig2e-whisker-sensory-premotor-reduction, fig2f-latency-frontal-not-rsc, fig3e-auditory-similar-across-contexts, fig4b-wminus-higher-correlation-correct. These said reproduced "under a reading" of the threshold, null, order or test, so any one reading could decide. These are method details that can change the outcome, and the protocol requires that all readings give the outcome, or the claim is blocked as methods_underspecified. Changed to that.
  - fig3h-rsc-first-context-discrimination. Made explicit that both readings of the 20 ms exclusion, as well as every baseline reading, must agree.
  - fig2e-rsc-tjs1-increase-wminus, fig2f-latency-frontal-not-rsc. The RSC site was treated as open. The Methods fix it (Pharmacological inactivation, 1.5 mm posterior and 0.5 mm lateral; the tracing used the coordinates of the optogenetic and imaging experiments), so the site is (-1.5, 0.5) and (-0.5, 0.5) is a variant.
  - fig3c-jaw-onset. Any of two onset rules could decide. The Methods' d' >= 1 rule and the code's 3 SD rule differ, and the protocol puts the Methods first, so the Methods' rule decides and the code's is a variant.
  - fig2cd-rsc-no-effect-catch-auditory. New claim. The Results state that RSC inhibition in catch and auditory trials did not change performance, a finding no claim covered.
  - supp1c-wplus-blocks-longer, supp1d-faster-response-wplus. The checker reports the p-values 2.0e-4 and 6.0e-4 not found because the paper prints "2.0 x 10-4" and "6.0 x 10-4"; read and confirmed, no change.
  - Open. fig2c-catch-little-effect counts "little effect" as at most 3 of 39 sites; the paper gives no measure, and this cut is not the paper's.
  - Open. fig4c-inhibition-propagates-forward and supp4d-photoactivation-control call a decrease a drop below control by more than the control SD over mice; fig4d-trajectories-follow-lick measures closeness as mean squared distance on PC3. The paper gives neither measure.
  - Open. supp2-muscimol-ws1-rsc reads the "non-significant positive trend" as 0.05 <= p < 0.1; the upper bound is not the paper's.
  - Open. fig1f-gradual-further-adaptation (trial +4 at least as close as +2) and fig1h-temporal-integration (the anticipation tests) are readings of statements the paper gives no test for.
EOF
python tools/claims_check.py claims/001847/10.7554-elife.109717.yaml paper/10.7554-elife.109717.txt; grep -n "—\|rather" claims/001847/10.7554-elife.109717.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001847/10.7554-elife.109717.yaml",
 "old_string": "decide (protocol, step 2): on each",
 "new_string": "decide (protocol, step 2), on each"
}
```

```
The file claims/001847/10.7554-elife.109717.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001847/10.7554-elife.109717.yaml paper/10.7554-elife.109717.txt; grep -n "—\|rather" claims/001847/10.7554-elife.109717.yaml | head; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I made 10 changes to the claims file, including one new claim, and marked it ready. Five open problems remain, listed below. Nothing is committed or pushed.

**Checker result:** `claims/001847/10.7554-elife.109717.yaml: 39 claims, 39 quotes, 13 statistical values, 2 problems`. Both problems are the checker missing values the paper prints as "2.0 x 10-4" (supp1c-wplus-blocks-longer) and "6.0 x 10-4" (supp1d-faster-response-wplus). I read both in the supplement legends and they are correct. All 39 quotes pass.

**Changes, by claim:**
- **fig1e-context-off-no-discrimination:** For a claim of absence, the protocol judges on the paper's test alone. The only test in the paper or its code is the code's supplement 1E test, so it now decides, per transition direction. The W+ against W- t-test, which neither the paper nor the code runs, is now a variant.
- **fig1k-model-accuracy:** Added that the Methods say "all expert sessions", but the orofacial features exist only for sessions with face video. The code's list of 60 sessions settles the set.
- **fig2d, fig2e-whisker, fig2f, fig3e, fig4b-wminus:** These said "reproduced under a reading", so any single threshold, null, order or test reading could decide. These details can change the outcome, so all readings must now give the same outcome, otherwise the claim is blocked as `methods_underspecified`.
- **fig3h:** Both readings of the 20 ms exclusion, and every baseline reading, must agree.
- **fig2e-rsc-tjs1-increase-wminus, fig2f:** The file treated the RSC site as open. The Methods fix it at 1.5 mm posterior and 0.5 mm lateral, and the tracing used the same coordinates, so the site is (-1.5, 0.5) and (-0.5, 0.5) is a variant.
- **fig3c-jaw-onset:** Either onset rule could decide. The Methods' rule (d' ≥ 1) now decides and the code's rule (3 SD) is a variant, since the Methods come first.
- **New claim, fig2cd-rsc-no-effect-catch-auditory:** The Results say RSC inhibition in catch and auditory trials did not change performance, and no claim covered this. It is judged as a claim of absence on the opto-map d'.

**Still open** (the paper gives no measure, so these cuts are the first reader's, not the paper's):
- **fig2c:** "little effect" is counted as at most 3 of 39 sites.
- **fig4c and supp4d:** a decrease is a drop below control by more than the control SD over mice.
- **fig4d:** closeness is measured as mean squared distance on PC3.
- **supp2-muscimol:** the "non-significant positive trend" is read as 0.05 ≤ p < 0.1; the 0.1 bound is not the paper's.
- **fig1f and fig1h:** the gradual-adaptation rule and the anticipation tests are readings of statements the paper never tests.

**Ready:** yes, `ready: true` in a new `checks` entry dated 2026-10-21, with one line per change and per open problem. The attempt should record the open items as deviations.

## End of run

28 turns, 3 minutes, result: success.
