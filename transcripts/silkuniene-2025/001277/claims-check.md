# 001277 · claims-check · run 39711578338

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001277/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/001277/*.yaml; python tools/claims_check.py claims/001277/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -w 4000 -s paper/*.txt | sed -n 1,200p
```

Result: not kept, because it reads the paper's text.

**Agent**

I'll read it in chunks with the Read tool.

**Agent calls Bash**

```bash
fold -w 3000 -s paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 40
}
```

```
1	DOI: 10.1016/j.bioelechem.2025.109016
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Bioelectrochemistry Bioelectrochemistry 319 nihpa 100953583 Bioelectrochemistry (Amsterdam, Netherlands) 1567-5394 1878-562X pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC12331426 PMC12331426.1 12331426 12331426 NIHMS2087238 40460713 10.1016/j.bioelechem.2025.109016 NIHMS2087238 NIHPA2087238 1 Article MHz compression of pulse packets facilitates remote focusing of electroporation Silkuniene Giedre Silkunas Mantas Pakhomova Olga N. Semenov Iurii Pakhomov Andrei G. * Frank Reidy Research Center for Bioelectrics, Old Dominion University, Norfolk, VA 23508, USA Author contributions A.G.P.: Conceptualization, Methodology, Formal Analysis, Writing - Original Draft, Supervision, Visualization, Funding acquisition G.S.: Methodology, Formal Analysis, Visualization, Data Curation, Software, Validation, Investigation, Writing Original Draft M.S.: Methodology, Formal Analysis, Writing - Original Draft, Visualization, Investigation I.S.: Methodology, Formal Analysis, Writing-Review and Editing O.N.P .: Methodology, Writing-Review and Editing, Resources. * Corresponding author: Andrei G. Pakhomov, Frank Reidy Research Center for Bioelectrics Old Dominion University, 4211 Monarch Way., Suite 300, Norfolk, VA 23508, Fax: +1(757)4511010, [removed: an e-mail address] ; [removed: an e-mail address] , 12 2025 31 5 2025 166 494632 109016 109016 04 06 2025 31 05 2026 31 05 2026 09 08 2025 31 05 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Stimulation by pulsed electric fields (PEFs) normally follows PEF strength and weakens with distance from electrodes. Bipolar cancellation, caused by the electric field reversal, can offset this dependence. Remo
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 40,
 "limit": 89
}
```

```
40	
41	[6] Electrotransfer for nucleic acid and protein delivery. Trends Biotechnol. 2024. 10.1016/j.tibtech.2023.11.009
42	
43	[7] Pulsed electric fields in oncology: a snapshot of current clinical practices and research directions from the 4th world congress of electroporation. Cancers (Basel). 2023. 10.3390/cancers15133340
44	
45	[8] Effect of experimental electrical and biological parameters on gene transfer by electroporation. Syst. Rev. Meta-Analysis, Pharmaceutics. 2022.
46	
47	[9] Gene electrotransfer clinical trials. Adv. Genet.. 2015. 10.1016/bs.adgen.2014.10.006
48	
49	[10] Nano-pulse stimulation is a physical modality that can trigger immunogenic tumor cell death. J. Immunother. Cancer. 2017. 10.1186/s40425-017-0234-5
50	
51	[11] Preclinical studies on electrochemotherapy. 2017.
52	
53	[12] High-frequency irreversible electroporation is an effective tumor ablation strategy that induces immunologic cell death and promotes systemic anti-tumor immunity. Ebiomedicine. 2019. 10.1016/j.ebiom.2019.05.036
54	
55	[13] Gyri-precise head model of transcranial direct current stimulation: improved spatial focality using a ring electrode versus conventional rectangular pad. Brain Stimul.. 2009. 10.1016/j.brs.2009.03.005
56	
57	[14] Finite-element model predicts current density distribution for clinical applications of tDCS and tACS. Front. Psychol.. 2012.
58	
59	[15] Effect of electrode distance in grid electrode: numerical models and in vitro tests. Technol. Cancer Res. Treat.. 2018. 10.1177/1533033818764498
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "range\|low\|high\|tolerance\|p_relation\|checks\|ready" tools/claims_check.py | head -60; ls docs
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
38:    return re.sub(r"\s+", " ", s).strip().lower()
75:    return {f.lower() for f in out}
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
agents
archives.md
conversion-tracker.md
design.md
fixing-conversions.md
pilot-notes.md
pipeline.md
protocol.md
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | grep -n -A40 '"expected"' | head -80; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | grep -n -B2 -A30 '"checks"' | head -60
```

```
104:     "expected": {
105-      "description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.",
106-      "oneOf": [
107-       {
108-        "$ref": "#/$defs/expected"
109-       },
110-       {
111-        "type": "array",
112-        "minItems": 1,
113-        "items": {
114-         "$ref": "#/$defs/expected"
115-        }
116-       }
117-      ]
118-     },
119-     "statistics": {
120-      "description": "The statistical support the paper reports for the finding: one entry per test or interval, as the paper gives it. A record of the paper, not a target with a tolerance (that is `expected`).",
121-      "type": "array",
122-      "minItems": 1,
123-      "items": {
[... 93 more lines not kept]
```

**Agent**

Now the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    expressed in percent; mean and s.e. over the n=5 experiments per duration at each\n    distance, as in Fig. 6C. The paper reports no test; its Methods say significance in the\n    graphs is read from the gap between error bars (a gap longer than the error bars means p\n    < 0.05). Reproduced when at no distance from -5 to 5 mm (the plotted fit range of the\n    legend) do two durations' mean profiles show a gap between their s.e. bars longer than\n    the bars; not reproduced otherwise. ROI spacing readings are 1-mm steps and contiguous ROIs; the outcome is the one both give.",
 "new_string": "    expressed in percent; mean and s.e. over the n=5 experiments per duration at each\n    distance, as in Fig. 6C. The paper reports no test; its Methods say significance in the\n    graphs is read from the gap between error bars (a gap longer than the error bars means p\n    < 0.05). Reproduced when at no compared distance do two durations' mean profiles show a\n    gap between their s.e. bars longer than the bars; not reproduced otherwise. The text\n    does not limit the distances; readings are -5 to 5 mm (the fit range of the Fig. 6\n    legend) and every measured distance. ROI spacing readings are 1-mm steps and contiguous\n    ROIs. The outcome is the one all readings give; blocked as methods_underspecified when\n    they differ."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    free, no offset) fitted by least squares to the background-subtracted YP intensity along\n    the diagonals; FWHM is b. Then a regression of individual FWHM values on pulse duration\n    (15 points, as the n=15 of Fig. 4C), and a two-sided t-test of its slope. Readings are",
 "new_string": "    free, no offset) fitted by least squares to the background-subtracted YP intensity along\n    the diagonals; FWHM is b. Then a regression of FWHM on pulse duration and a two-sided\n    t-test of its slope. The Fig. 6D legend does not say whether the trend was fitted to the\n    15 individual values or to the 3 means; readings are individual values (as Fig. 4C,\n    whose legend gives n=15 for fitting) and the 3 means. Further readings are"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "  statement: FWHM for 600-ns and for 900-ns packets is each significantly smaller than for\n    300-ns packets (p = 0.028 and p = 0.0072, Bonferroni-corrected t-tests).",
 "new_string": "  statement: FWHM for 600-ns and for 900-ns packets is each significantly smaller than for\n    300-ns packets (Bonferroni-corrected t-tests, p = 0.028 for one and p = 0.0072 for the\n    other)."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "  criterion: Diagonal YP profiles per experiment (Fig. 3B; n=3 per CANCAN rate, n=5 controls).\n    Reproduced when, for every CANCAN packet rate, mean YP at 0 mm exceeds mean YP at 6 and\n    at 7 mm (the near-electrode positions the paper names, Fig. 4B), and in controls mean YP\n    at 0 mm is below that at 6 and 7 mm; each comparison read with the Methods' error-bar gap\n    rule (a gap longer than the s.e. bars).",
 "new_string": "  criterion: Diagonal YP profiles per experiment (Fig. 3B; n=3 per CANCAN rate, n=5 controls).\n    The statement is of a peak at the centre; the paper names no positions for this visual\n    reading of Fig. 3A. Reproduced when, for every CANCAN packet rate, mean YP at 0 mm\n    exceeds mean YP at 4 mm (the edge of the Lorentzian fit range, Fig. 3 legend and Results\n    3.1), and in controls mean YP at 0 mm is below that at 4, 6 and 7 mm; each comparison read\n    with the Methods' error-bar gap rule (a gap longer than the s.e. bars). Whether CANCAN YP\n    at 0 mm also exceeds YP at 6 and 7 mm (the near-electrode positions of Fig. 4B) is shown\n    per rate and not judged here, since the paper reports the near-electrode suppression as\n    rate dependent (fig4b-suppression-near-electrodes)."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    each CANCAN rate over -4 to 4 mm. Reproduced when the correlation of fit with data\n    exceeds 0.9 for every rate.",
 "new_string": "    each CANCAN rate over -4 to 4 mm. Reproduced when the correlation of fit with data\n    exceeds 0.9 with p < 0.001 for every rate."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "  source: Results 3.1, paragraphs 2 and 3; Figure 4A and 4B",
 "new_string": "  source: Results 3.1, paragraphs 2 and 4; Figure 4A and 4B"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    not stated; readings are each rate against 1 Hz (as in Fig. 4C) and all pairs.\n    Reproduced when no corrected p is below 0.05; not reproduced when any is. Effect sizes\n    are reported.",
 "new_string": "    not stated; readings are each rate against 1 Hz (as in Fig. 4C) and all pairs.\n    Reproduced when no corrected p is below 0.05 under either reading; not reproduced when\n    some corrected p is below 0.05 under both; blocked as methods_underspecified when the\n    readings differ. Effect sizes are reported."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    packet rate over the 15 experiments below 0.2 MHz. Reproduced when the slope is negative\n    with p < 0.05 and the means are within tolerance; partially reproduced when only the\n    slope holds.",
 "new_string": "    packet rate over the 15 experiments below 0.2 MHz. No further gain at 0.2 MHz is read\n    with the Methods' error-bar gap rule; it holds when mean FWHM at 0.2 MHz is not below the\n    10-kHz mean by a gap longer than the s.e. bars. Reproduced when the slope is negative\n    with p < 0.05, the 0.2-MHz condition holds and the means are within tolerance; partially\n    reproduced when only the slope holds."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    with the coefficients of 0.98 and 0.95 for Lorentzian and Gaussian fits\n  expected:",
 "new_string": "    with the coefficients of 0.98 and 0.95 for Lorentzian and Gaussian fits\n  statistics:\n  - about: significance of each of the four fits\n    test: fit significance\n    p: 0.0001\n    p_relation: \"<\"\n  expected:"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "  criterion: Central YP per experiment regressed linearly on burst number, CT26 without the",
 "new_string": "  criterion: Central YP (0 mm) regressed linearly on burst number, CT26 without the"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    test of the legend. Reproduced when both slopes are positive at p < 0.05. Saturation is",
 "new_string": "    test of the legend. The legend does not say whether individual experiments or means\n    were fitted; readings are both, and the outcome is the one both give (blocked as\n    methods_underspecified when they differ). Reproduced when both slopes are positive at\n    p < 0.05. Saturation is"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    slope is positive at p < 0.05 and the CHO slope is not significant. Fit-range readings as\n    in fig6d-longer-pulses-sharper-peak.",
 "new_string": "    slope is positive at p < 0.05 and the CHO slope is not significant. Fit-range, ROI\n    spacing, pooling and fitted-points (individual values or means) readings as in\n    fig6d-longer-pulses-sharper-peak; blocked as methods_underspecified when they differ."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "    value: 45\n    tolerance: 9.5\n  criterion: Per-experiment FWHM as in fig6d-longer-pulses-sharper-peak; gap is the 15.3-mm\n    diagonal. The ratio range 40 to 50 widened by 10% of each bound is 36 to 55; the",
 "new_string": "    value: 45.5\n    tolerance: 9.5\n  criterion: Per-experiment FWHM as in fig6d-longer-pulses-sharper-peak; gap is the 15.3-mm\n    diagonal. Sharpest means the mean FWHM is below that of every other condition the\n    study fitted (Figs 4C, 6D, 7C and 7F); this is shown and judged. The ratio range 40 to 50\n    widened by 10% of each bound is 36 to 55 (value 45.5, tolerance 9.5); the"
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001277/10.1016-j.bioelechem.2025.109016.yaml",
 "old_string": "  statement: In the worst-case heating protocol (600-ns packets with no interval, up to 6\n    bursts), temperature under the electrodes did not exceed 44 C, though it exceeded 30 C\n    near electrodes.",
 "new_string": "  statement: In the worst-case heating protocol (600-ns packets with no interval, 2 or 6\n    bursts), temperature did not exceed 44 C even near the electrodes; it could exceed 30 C\n    within about 2 mm of the electrodes after 2 bursts and even near the centre after 6\n    bursts."
}
```

```
The file claims/001277/10.1016-j.bioelechem.2025.109016.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/001277/10.1016-j.bioelechem.2025.109016.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig6c-normalized-decline-similar, the -5 to 5 mm limit was the writer's choice (the text says decline sideways with no range); every measured distance added as a reading, with the rule for differing readings.
  - fig6d-longer-pulses-sharper-peak, the Fig. 6D legend does not say whether the trend was fitted to 15 individual FWHM values or to 3 means (only Fig. 4C gives n=15 for fitting); both made readings.
  - fig6d-600-900-differ-from-300, the statement assigned p = 0.028 to 600 ns and p = 0.0072 to 900 ns, which the legend does not do; reworded.
  - fig3-cancan-centre-enhancement, the criterion required centre YP above YP at 6 and 7 mm at every rate, which the text does not state (it reports near-electrode suppression as rate dependent, and data departing from the fit at larger distances at lower rates); now judged as a central peak against 4 mm, the edge of the Fig. 3 fit range, with 6 and 7 mm shown.
  - fig3-lorentzian-decline, added the paper's p < 0.001 to the criterion.
  - fig4b-suppression-near-electrodes, source changed to paragraphs 2 and 4 of Results 3.1, since the rate-dependent decline at 6 and 7 mm is stated in paragraph 4 and not paragraph 3.
  - fig4b-centre-no-rate-effect, the criterion did not say what happens when the two readings of the compared pairs disagree; added.
  - fig4c-fwhm-falls-with-rate, the statement's no further gain at 0.2 MHz was not judged; added an error-bar gap test from Methods 2.5.
  - fig5-yp-lorentzian-pr-gaussian, added the reported fit significance (p < 0.0001, Results 3.2) under statistics.
  - fig7be-burst-number-centre and fig7-fwhm-burst-number, whether the linear fits use individual experiments or means is not stated; both made readings.
  - fig7-sharpest-peak-1-burst-ct26, expected ratio 45 +/- 9.5 gave 35.5 to 54.5, not the 36 to 55 the protocol rule and the criterion give; value set to 45.5. Added the check that it is the smallest FWHM of the study, which the statement asserts.
  - fig2-heating-below-44c, the statement said under the electrodes and dropped the 2-burst and 6-burst detail of Methods 2.3; reworded to the paper's text.
  - Open, fig3-cancan-centre-enhancement, enhanced at the center could also mean centre YP above the control's centre YP; the text sets it against the control's decrease toward the centre, so the central-peak reading was kept.
  - Open, fig7-sharpest-peak-1-burst-ct26, how 2.3% of the array area is computed is not given (a 1.1-mm circle over the array square is 0.8%); reported, not judged.
  - Open, fit range for individual FWHM fits (4, 5 or 6 mm) and ROI spacing remain readings the paper does not settle; carried in the criteria.
EOF
python tools/claims_check.py claims/001277/*.yaml paper/*.txt; grep -n ': .*: ' claims/001277/*.yaml | grep -v '^\S*:#' | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The file is ready for an attempt. I made 12 corrections from the paper, the last entry under `checks` has `ready: true`, and the checker still passes after the edits.

**Checker result:** `17 claims, 17 quotes, 14 statistical values, 0 problems` (13 statistical values before my edits).

**Changes, by claim:**
- **fig6c-normalized-decline-similar:** the -5 to 5 mm range was the writer's choice, since the text gives no range. I added "every measured distance" as a second reading, and the claim is blocked if the readings disagree.
- **fig6d-longer-pulses-sharper-peak:** the Fig. 6D legend doesn't say whether the trend was fitted to the 15 individual FWHM values or the 3 means. Both are now readings.
- **fig6d-600-900-differ-from-300:** the statement tied p = 0.028 to 600 ns and p = 0.0072 to 900 ns. The legend doesn't say which is which, so I reworded it.
- **fig3-cancan-centre-enhancement:** the criterion required centre YP to exceed YP at 6 and 7 mm at every packet rate. The paper doesn't say that; it reports the suppression near the electrodes as depending on rate. It is now judged as a peak at the centre, compared against 4 mm (the edge of the Fig. 3 fit range). The 6 and 7 mm values are shown but not judged.
- **fig3-lorentzian-decline:** added the paper's p < 0.001 to the criterion.
- **fig4b-suppression-near-electrodes:** the source now reads paragraphs 2 and 4. The rate-dependent decline at 6 and 7 mm is stated in paragraph 4, not paragraph 3.
- **fig4b-centre-no-rate-effect:** added what happens when the two readings of which rates are compared disagree (blocked).
- **fig4c-fwhm-falls-with-rate:** the statement's "no further gain at 0.2 MHz" was never tested. It is now checked with the error-bar gap rule from the Methods.
- **fig5-yp-lorentzian-pr-gaussian:** added the reported fit significance (p < 0.0001) under statistics.
- **fig7be-burst-number-centre** and **fig7-fwhm-burst-number:** the paper doesn't say whether the linear fits used individual experiments or means. Both are now readings.
- **fig7-sharpest-peak-1-burst-ct26:**
  - The expected ratio of 45 ± 9.5 covered 35.5 to 54.5, not the 36 to 55 that the protocol's rule gives. I set the value to 45.5.
  - I added a check that this is the smallest FWHM in the study, which the statement claims.
- **fig2-heating-below-44c:** the statement said "under the electrodes" and dropped the 2-burst and 6-burst details. I reworded it to match Methods 2.3.

**Still open (logged in the check entry):**
- **fig3-cancan-centre-enhancement:** "enhanced at the center" could also mean higher centre YP than the control's centre. I kept the reading of a peak at the centre, because the text contrasts it with the control's decrease toward the centre.
- **fig7-sharpest-peak-1-burst-ct26:** the paper doesn't say how it gets 2.3% of the array area. A 1.1-mm circle over the array square gives 0.8%. The figure is reported, not judged.
- **Fitting details:** the fit range for individual FWHM fits (4, 5 or 6 mm) and the spacing of measurement regions along the diagonals are not settled by the paper. They stay as readings in the criteria.

Each of the paper's main findings has a claim, and all claims come from this paper. Nothing was committed or pushed.

## End of run

25 turns, 3 minutes, result: success.
