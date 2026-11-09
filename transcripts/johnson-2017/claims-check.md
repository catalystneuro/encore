# johnson-2017 · claims-check · run 42680191429

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i johnson; cat claims/johnson-2017.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/johnson-2017.yaml"
}
```

```
1	# Claims for Johnson, Dewar, Solbakk, Endestad, Meling & Knight (2017), Current Biology 27,
2	# 1829-1835, "Bidirectional Frontoparietal Oscillatory Systems Support Working Memory",
3	# doi:10.1016/j.cub.2017.05.046, on CRCNS data set pfc-5 (doi:10.6080/K0ZC811B).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record with its supplemental information, as supplied under paper/
8	# (PDF extracted to text): main text (Results, Discussion), figure legends 1 to 4, STAR Methods
9	# (pages e1 to e4), and the supplement (legends of Figures S1 to S4, Tables S1 to S3, read from
10	# the text). The PDF could not be rendered in this run, so the figures themselves were not read:
11	# the channel list of the Figure 2 cluster (the PFC region of interest of the PSI analysis) and
12	# the time courses of Figures 2 to 4 are known only from the text and legends. The extraction
13	# garbles symbols: "3" stands for the multiplication sign, "/" for an arrow, "%" for less than
14	# or equal, "R" for greater than or equal, "jZj" for |Z|, and a replacement character for the
15	# minus sign in exponents. Quotes keep the extracted characters. The CRCNS data descriptor
16	# (paper/pfc-5.data-description.txt) was read only to know what the data set holds; no claim or
17	# method comes from it.
18	#
19	# Code. The paper's Key Resources Table and Data and Software Availability say the custom MATLAB
20	# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the
[... 622 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/ | grep -iE 'johnson|pfc'; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; sed -n 43,140p docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 140,220p docs/protocol.md; python tools/claims_check.py claims/johnson-2017.yaml paper/10.1016-j.cub.2017.05.046.txt; wc paper/10.1016-j.cub.2017.05.046.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.txt",
 "offset": 767,
 "limit": 640
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "p_relation\|<=\|≤" tools/claims_check.py | head -30; grep -rn "checks:" -A12 claims/*.yaml | head -40
```

```
claims/armstrong-2026.yaml:843:checks:
claims/armstrong-2026.yaml-844-- date: 2026-10-21
claims/armstrong-2026.yaml-845-  kind: agent
claims/armstrong-2026.yaml-846-  model: claude-opus-5-5
claims/armstrong-2026.yaml-847-  ready: true
claims/armstrong-2026.yaml-848-  changes:
claims/armstrong-2026.yaml-849-  - Header. Added that Table S1 assigns Fig. 2I and 2L to animal 480, Fig. 3E, F, Q, R to 489 and Fig. S12 to 589; the header listed 573 alone for Fig. 2I.
claims/armstrong-2026.yaml-850-  - fig1lm-staged-modulation. The epoch 1 window (-1 to 0 s) was stated as fixed; the paper gives only t < 0. Named the readings -1 to 0 s and -0.5 to 0 s, as fig1n-epoch-rates has them.
claims/armstrong-2026.yaml-851-  - fig1o-trial-end-ramp. Ramp onset was defined as the suppression minimum without saying the paper does not define it. It now takes the two onset readings of fig4b-ddm-matches-ramp.
claims/armstrong-2026.yaml-852-  - figs1-running-speed. The SI (Animal preparation) gives the same 21 ± 4 cm/s for habituation day 3. Added this as reading (d), usable only if the dataset holds habituation sessions.
claims/armstrong-2026.yaml-853-  - fig2a-success-rate. Lateral position relative to t = 0 was stated as fixed; the paper does not set the zero. Named it open, with the readings of fig2b-lateral-spread.
claims/armstrong-2026.yaml-854-  - fig2i-ft-rt. Table S1 assigns Fig. 2I to 480 ("2IL") as well as 573 ("2EFI"); the criterion named 573 only. Added readings 573, 480 and both pooled.
claims/armstrong-2026.yaml-855-  - fig2jk-glm-mixed-tuning. The criterion listed 12 variables as "13 regressors plus V_wall". The SI says 13 regressors and then "additionally" V_wall, and names 12 variables with the Results. The criterion now says so, leaves a 13th variable open and fits the 12 named plus V_wall. "Among the strongest" was defined one way only; added the largest mean log likelihood ratio as a second reading.
--
claims/ashworth-2025.yaml:1205:checks:
claims/ashworth-2025.yaml-1206-
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "relation" tools/claims_check.py tools/*.py | grep -i "p_rel\|'<'\|\"<\"" | head; grep -rhn "p_relation:" claims/ | sort | uniq -c | sort -rn | head
```

```
tools/build_site.py:920:        parts.append(f'p {s.get("p_relation", "=")} {p_text(s["p"])}')
      8 443:    p_relation: "<"
      7 408:    p_relation: "<"
      7 258:    p_relation: "<"
      7 236:    p_relation: "<"
      7 231:    p_relation: "<"
      7 184:    p_relation: "<"
      7 150:    p_relation: "<"
      6 715:    p_relation: "<"
      6 599:    p_relation: "<"
      6 589:    p_relation: "<"
```

**Agent calls Bash**

```bash
cd  grep -rhoE "p_relation: .*" claims/ | sort | uniq -c; grep -rn "p_relation" tools/ schema* docs/*.md 2>/dev/null | head
```

```
1795 p_relation: "<"
      1 p_relation: "="
    312 p_relation: ">"
      8 p_relation: '>'
    125 p_relation: <
tools/build_site.py:920:        parts.append(f'p {s.get("p_relation", "=")} {p_text(s["p"])}')
schemas/claims.schema.json:304:          "description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.",
schemas/claims.schema.json:309:        "p_relation": {
docs/protocol.md:97:     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
```

**Agent calls Bash**

```bash
cd  sed -n 300,320p schemas/claims.schema.json
```

```
"description": "The test statistic as reported, e.g. 't(14) = 3.2', 'F(2, 40) = 5.1', 'r = 0.38'.",
          "type": "string"
        },
        "p": {
          "description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.",
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "p_relation": {
          "description": "How p was reported: exactly (the default) or as a bound.",
          "enum": [
            "=",
            "<",
            ">"
          ]
        },
        "corrected": {
          "description": "The correction for multiple comparisons the paper applied, e.g. 'Bonferroni', 'FDR'.",
          "type": "string"
[... 1 more lines not kept]
```

**Agent**

The checker found one problem (a garbled p-value in patients-above-chance). The PDF may show Figure 2's channel cluster, which would settle O6, so I'm checking it.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2017.05.046.pdf",
 "pages": "5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz;d=fitz.open('paper/10.1016-j.cub.2017.05.046.pdf')
for i in [4,5]:
  p=d[i]; p.get_pixmap(dpi=150).save('$TMPDIR/p%d.png'%i)
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
from scipy import stats
print(stats.f.sf(16.77,1,202), stats.t.sf(15.43,13), stats.t.sf(13.89,13), stats.f.sf(4.70,1,196))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
import math
def tsf(t,n):
  # regularized incomplete beta via numeric integration of density
  c=math.gamma((n+1)/2)/(math.sqrt(n*math.pi)*math.gamma(n/2))
  f=lambda x:c*(1+x*x/n)**(-(n+1)/2)
  # integrate t..t+200 with substitution
  N=200000; a=t; b=t+400; h=(b-a)/N
  return sum(f(a+(i+0.5)*h) for i in range(N))*h
print(tsf(15.43,13), tsf(13.89,13), 2*tsf(math.sqrt(16.77),202))"
```

```
4.868198529416856e-10 1.7752011182163292e-09 6.1024138266869956e-05
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "    condition. Reproduced when, under one reading, every test gives t above 13.89 (15.43 less\n    10%) and one-tailed p < 5 x 10^-10.",
 "new_string": "    condition. Reproduced when, under one reading, every test gives t above 13.89 (15.43 less\n    10%). The one-tailed p of each test is reported; the paper's p < 5 x 10^-10 is the p of t =\n    15.43 with 13 degrees of freedom (4.9 x 10^-10), so it is not a separate requirement."
}
```

```
The file claims/johnson-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "  criterion: The model is from STAR Methods, Behavioral Analysis, and Table S3. Its rows are",
 "new_string": "  criterion: The model is from STAR Methods, Behavioral Analysis, and Table S3. The Results\n    sentence puts group p < 7 x 10^-5 after the full model, but Table S3 gives the full model's\n    group effect p = 0.03 and its legend ties p < 7 x 10^-5 to the re-submitted models; F(1,202)\n    = 16.77 of the group-only model gives p = 6.1 x 10^-5, so the bound is that model's. Its rows are"
}
```

```
The file claims/johnson-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "    controls that includes P6, P8, P10 or PO8 (the POSTERIOR channels of Figure S2A), and one\n    of opposite sign to the controls' ERP in lesioned-hemisphere anterior channels among F5,\n    F7, FC5, FT7, C3, C5 and T7.",
 "new_string": "    controls that includes P6, P8, P10 or PO8 (the POSTERIOR channels of Figure S2A), and one\n    in lesioned-hemisphere anterior channels among F5, F7, FC5, FT7, C3, C5 and T7 in which the\n    patients' mean ERP has the opposite sign to the controls' (\"reversed-polarity\")."
}
```

```
The file claims/johnson-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "    100 ms (one time step) of the stated edges; partially reproduced when only the processing\n    effects hold.",
 "new_string": "    100 ms (one time step) of the stated edges; partially reproduced when only the processing\n    effects hold. The sign of each cluster is reported; the next sentence of the paragraph says\n    controls showed greater PFC leads than patients to widespread central-posterior sites."
}
```

```
The file claims/johnson-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "    leaving the channel (out-degree, signed); (b) the count of true connections\n    leaving the channel.",
 "new_string": "    leaving the channel (out-degree, signed); (b) the count of true connections\n    leaving the channel; (c) the sum of |Z| over all true connections of the channel, in\n    either direction (\"between each channel and all other channels\")."
}
```

```
<tool_use_error>String to replace not found in file.
String:     leaving the channel (out-degree, signed); (b) the count of true connections
    leaving the channel.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "(b) the count of true connections leaving the\n    channel. ",
 "new_string": "(b) the count of true connections leaving the\n    channel; (c) the sum of |Z| over all true connections of the channel, in either direction\n    (\"between each channel and all other channels\")."
}
```

```
<tool_use_error>String to replace not found in file.
String: (b) the count of true connections leaving the
    channel. </tool_use_error>
```

**Agent calls Grep**

```json
{
 "pattern": "count of true",
 "path": "claims/johnson-2017.yaml",
 "output_mode": "content",
 "-A": 1
}
```

```
604:    connections leaving the channel (out-degree, signed); (b) the count of true connections
605-    leaving the channel. Group cluster test with the shared methods on channels by time. Open
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/johnson-2017.yaml",
 "old_string": "(b) the count of true connections\n    leaving the channel. Group",
 "new_string": "(b) the count of true connections\n    leaving the channel; (c) the sum of |Z| over all true connections of the channel, in either\n    direction (the Methods say \"between each channel and all other channels\"). Group"
}
```

```
The file claims/johnson-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/johnson-2017.yaml <<'EOF'
checks:
- date: 2026-11-09
  kind: agent
  model: "claude-opus-5-5"
  ready: true
  changes:
  - patients-above-chance, the checker's one problem (5e-10 not found) is the garbled exponent of "one-tailed p < 5 3 10�10" (Results, Behavior, paragraph 2); the value is right. No change to the statistic.
  - patients-above-chance, the criterion asked for t above 13.89 and also one-tailed p < 5 x 10^-10, but t = 13.89 with 13 degrees of freedom gives p = 1.8 x 10^-9, which made the 10% tolerance void. The p is now reported, not required; the paper's bound is the p of t = 15.43 (4.9 x 10^-10).
  - accuracy-patients-impaired, the criterion now says why p < 7 x 10^-5 is the group-only model's though the Results sentence follows the full model; Table S3 gives the full model's group p = 0.03, its legend ties the bound to the re-submitted models, and F(1,202) = 16.77 gives p = 6.1 x 10^-5.
  - erp-lesioned-maintenance, "one of opposite sign to the controls' ERP" was unclear about what has the opposite sign; it now asks for a cluster in which the patients' mean ERP has the opposite sign to the controls', as "reversed-polarity" says.
  - psi-deltatheta-group-clusters, the sign of the clusters is now reported, as the next sentence of the paragraph says controls showed greater PFC leads than patients to central-posterior sites; the claim had no direction for these effects.
  - psi-network-degree, added reading (c) for degree, the sum of |Z| over true connections in either direction; the Methods define degree as the weight of true connections "between each channel and all other channels" and do not say out-going only.
  - psi-network-degree, the paper prints pcluster as at most 0.01; the schema has no "<=" relation, so "<" stays with the note under about.
  - Checked against the text and found right, with no change. Cohort, trial counts and demographics (Results paragraph 1, STAR Methods); the Table S2 terms and degrees of freedom; the Table S1 range 0.65 to 0.98 and patient mean 0.87 recomputed from it; the Table S3 degrees of freedom (196, 202, 200) and the 204-row reading; ERP channel lists and p values; Figure S2, S3 and S4 channel sets; PSI windows and Z bounds; all p values against the text and legends.
  - Open, not settled. O6, the channels of the Figure 2 cluster, which define the PFC region of the PSI time courses; the PDF could not be rendered in this run either (no poppler or PyMuPDF), so the figure was not read. The two readings stand.
  - Open, not settled. accuracy-no-hemifield-condition-effect is judged on the third model of Table S3; the Results sentence could also refer to the full model, whose visual hemifield and condition effects have p = 0.06 but whose visual hemifield by condition interaction has p = 0.03. The full model is shown as a variant, as the criterion says.
  - Open, not settled. The deposited analysis_scripts were not read (they are among the data set's files); they may settle O1 to O5 and the degree definition, and the author should record which.
EOF
python tools/claims_check.py claims/johnson-2017.yaml paper/10.1016-j.cub.2017.05.046.txt; grep -n ' — \|rather' claims/johnson-2017.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I made five corrections to `claims/johnson-2017.yaml`, added the checks entry, and marked the file ready for an attempt. Nothing is committed.

**Checker result:** `claims/johnson-2017.yaml: 22 claims, 21 quotes, 33 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND patients-above-chance 5e-10`. The value is correct; the text extraction garbled the exponent in "one-tailed p < 5 3 10�10" (Results, Behavior, paragraph 2), so the checker can't match it.

**Changes, by claim:**
- **patients-above-chance:** the criterion asked for t above 13.89 (the paper's 15.43 less 10%) and also p < 5 x 10^-10. But t = 13.89 with 13 df gives p = 1.8 x 10^-9, so the p requirement cancelled the tolerance. The p is now reported, not required. The paper's bound is simply the p of t = 15.43, which is 4.9 x 10^-10.
- **accuracy-patients-impaired:** the criterion now explains why p < 7 x 10^-5 belongs to the group-only model, though the Results sentence places it after the full model. Table S3 gives the full model's group effect p = 0.03, its legend ties the bound to the re-run models, and F(1,202) = 16.77 gives p = 6.1 x 10^-5.
- **erp-lesioned-maintenance:** "reversed polarity" now has a clear test: a cluster in which the patients' mean ERP has the opposite sign to the controls'.
- **psi-deltatheta-group-clusters:** the sign of each cluster is now reported. The next sentence of the paper says controls showed greater PFC leads than patients, and the claim had given no direction.
- **psi-network-degree:** added a third reading of network degree: the sum of |Z| over true connections in either direction. The Methods say "between each channel and all other channels", not outgoing only. The paper prints the cluster p as at most 0.01; the schema has no "<=", so it stays "<" with a note.

Everything else matches the paper, including the cohort figures, Tables S1 to S3, the channel lists, the time windows, the Z bounds and every p-value. Every main finding has a claim, and no claim comes from outside the paper.

**Still open:**
- **PFC channels for the PSI analysis (O6):** they are only shown in Figure 2, and I couldn't render the PDF here (neither poppler nor PyMuPDF is installed). The claims file's two readings stand.
- **accuracy-no-hemifield-condition-effect:** it is judged on the third model in Table S3. The Results sentence could also mean the full model, where the hemifield by condition interaction has p = 0.03. That model is shown as a variant.
- **Analysis code:** the paper's analysis scripts are deposited with the dataset, so they weren't read here. They may settle the open details O1 to O5 and how network degree is defined; the author should record what they find.

## End of run

25 turns, 3 minutes, $1.26 at API prices, result: success.
