# shi-2013 · claims-check · run 42675389665

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i shi; cat claims/shi-2013.yaml; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i shi; wc -l claims/shi-2013.yaml; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; sed -n 1,200p docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/shi-2013.yaml paper/10.1152-jn.00223.2012.txt; wc -l paper/10.1152-jn.00223.2012.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now read the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00223.2012.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/shi-2013.yaml",
 "limit": 400
}
```

```
1	# Claims for Shi, Apker & Buneo (2013), J Neurophysiol 109:2097-2107, on CRCNS data set ppc-1.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
3	# protocol as stated in docs/protocol.md (Reader).
4	#
5	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
6	# with its Methods, Results, Discussion, Table 1 and the legends of Figures 1 to 6. The paper
7	# has no supplement. It links no analysis code, so none was read. The PDF could not be
8	# rendered here, and the extracted text prints the signs =, <, >, ~, plus/minus, minus and
9	# times as a replacement character. They were read from the PDF's font encodings (the
10	# Differences arrays of Universal-GreekwithMathPi and MathematicalPi-One). Every significance
11	# statement prints "P < 0.05"; the example cell's vision and interaction effects are
12	# "P = 0.52; P = 0.64"; values "a +/- b" are mean plus/minus spread; INDX1 means are -13% and
13	# -31%, the tuning split -24% and -40%, INDX2 means -9%, -13% and -13%; Table 1 y values carry
14	# a minus sign where the text shows the glyph; the Fig. 4 outliers are "indexes > 1.5 times the
15	# interquartile range"; the sample sizes are "N = 343" cells and "N = 200" for the bootstrap.
16	#
17	# The paper writes "(test, P < 0.05)" both after significant results and after results it
18	# calls not significant (correlations "identical ... permutation test, P < 0.05"; eye
19	# positions "neither ... differed ... P < 0.05"). Read with the Methods, which give each test
20	# as "(test, P < 0.05)", the bound is the threshold the test used. It is recorded as a
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/shi-2013.yaml",
 "offset": 400,
 "limit": 120
}
```

```
400	    value: 14.93
401	    tolerance: 0.5
402	    unit: cm
403	  - quantity: mean endpoint, monkey B, 135 degrees, z, V
404	    value: 14.89
405	    tolerance: 0.5
406	    unit: cm
407	  - quantity: mean endpoint, monkey B, 180 degrees, x, NV
408	    value: -5.39
409	    tolerance: 0.52
410	    unit: cm
411	  - quantity: mean endpoint, monkey B, 180 degrees, x, V
412	    value: -5.35
413	    tolerance: 0.55
414	    unit: cm
415	  - quantity: mean endpoint, monkey B, 180 degrees, y, NV
416	    value: -0.63
417	    tolerance: 0.46
418	    unit: cm
419	  - quantity: mean endpoint, monkey B, 180 degrees, y, V
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:" claims/shi-2013.yaml
```

```
55:- id: behavior-mean-position-sessions
75:- id: behavior-variability-sessions
102:- id: table1-endpoint-means
503:- id: table1-endpoint-sd
898:- id: fig3-example-neuron
931:- id: movement-epoch-tuning
948:- id: hold-position-main-effect
966:- id: hold-vision-main-effect
981:- id: hold-interaction
996:- id: hold-subepochs
1033:- id: hold-overall-effects
1059:- id: correlation-endpoint-datasets
1086:- id: fig4-indx1-negative
1140:- id: fig4-indx1-means
1161:- id: indx1-tuning-shift
1188:- id: indx2-means
1214:- id: rate-variance-nv-higher
1235:- id: fig5-fano-factor
1263:- id: cv2-larger-nv
1280:- id: fig6-decoding-vv
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml,re
c=yaml.safe_load(open('claims/shi-2013.yaml'))
cl={x['id']:x for x in c['claims']}
lines=open('paper/10.1152-jn.00223.2012.txt').read().split('\n')[547:661]
vals=[]
for l in lines:
    m=re.match(r'^(�?)([\d.]+) �([\d.]+)$',l)
    if m:
        v=float(m.group(2))*(-1 if m.group(1) else 1); vals.append((v,float(m.group(3))))
print(len(vals))
# table rows: per target x NV,V,y NV,V,z NV,V -> same order as yaml
me=[e['value'] for e in cl['table1-endpoint-means']['expected']]
mt=[e['tolerance'] for e in cl['table1-endpoint-means']['expected']]
sd=[e['value'] for e in cl['table1-endpoint-sd']['expected']]
st=[e['tolerance'] for e in cl['table1-endpoint-sd']['expected']]
print(len(me),len(sd))
for i,(v,s) in enumerate(vals):
    if abs(me[i]-v)>1e-9 or abs(mt[i]-s)>1e-9 or abs(sd[i]-s)>1e-9 or abs(st[i]-round(s*0.1,4))>1e-6: print(i,v,s,me[i],mt[i],sd[i],st[i])
d=[abs(me[i]-me[i+1]) for i in range(0,96,2)]
print(max(d))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/shi-2013.yaml",
 "offset": 895,
 "limit": 560
}
```

```
895	    value: 0.56
896	    tolerance: 0.056
897	    unit: cm
898	- id: fig3-example-neuron
899	  statement: An example neuron fired most when the hand was held at the lower left target (225
900	    degrees) in both V and NV; its hold-period rate showed a main effect of position (P < 0.05)
901	    but no effect of vision (P = 0.52) and no interaction (P = 0.64).
902	  source: Results, Neurophysiology, paragraphs 1 and 2; Figure 3
903	  quote: For both the V and NV conditions, discharge was greatest when the animal held its hand
904	    at the target located in the lower left part of the workspace (225
905	  statistics:
906	  - about: main effect of position
907	    test: two-factor ANOVA
908	    p: 0.05
909	    p_relation: "<"
910	    n: one neuron, 8 targets, V and NV trials
911	  - about: main effect of the visual conditions
912	    test: two-factor ANOVA
913	    p: 0.52
914	    n: one neuron
[... 531 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "partial" docs/protocol.md | head; python3 -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
256:     their notes say how the partial link bears on them. A label that
451:  - `partially_reproduced`: the effect is present but weaker, or holds only in
490:If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd  which pdftotext mutool qpdf; python3 -c "import pypdf" 2>&1; python3 -c "import pdfminer" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfminer
ModuleNotFoundError: No module named 'pdfminer'
```

**Agent**

Checker passed with no problems. I'm now checking the glyphs the text garbles, by reading the PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00223.2012.pdf",
 "pages": "3-5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re,zlib
d=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'stream\r?\n(.*?)endstream',d,re.S):
    try: s=zlib.decompress(m.group(1))
    except Exception: continue
    for k in [b'0.52',b'0.64',b'1.5 times',b'6.9',b'343']:
        i=s.find(k)
        while i!=-1:
            print(k, s[max(0,i-150):i+20]); i=s.find(k,i+1)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re,zlib
d=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'stream\r?\n(.*?)endstream',d,re.S):
    try: s=zlib.decompress(m.group(1))
    except Exception: continue
    for k in [b'(0.52)',b'0.52',b'(0.64',b'times)',b'interquartile']:
        i=s.find(k)
        if i!=-1 and b'TJ' in s[i-300:i+50]:
            print(k, s[max(0,i-250):i+40]); print('---')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
d=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'/Differences\s*\[([^\]]*)\]',d):
    print(m.group(1)[:300])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re,zlib
d=open('paper/10.1152-jn.00223.2012.pdf','rb').read()
for m in re.finditer(rb'stream\r?\n(.*?)endstream',d,re.S):
    try: s=zlib.decompress(m.group(1))
    except Exception: continue
    for x in re.finditer(rb'/Differences\s*\[([^\]]*)\]',s): print(x.group(1)[:200])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

Glyphs confirmed from the PDF font tables (\x03 is "=", \x02 "<", \x08 ">", \x06 minus), so the header's readings hold. Checking the `data` field rules before editing.

**Agent calls Bash**

```bash
cd  grep -n "elsewhere\|with_labels\|'data'" tools/claims_check.py | head; grep -n "^checks" -A12 claims/*.yaml | head -30
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
[... 14 more lines not kept]
```

**Agent**

The file mostly holds up. I'm correcting two sources and adding a citation.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/shi-2013.yaml",
 "old_string": "  source: Results, Neurophysiology, paragraphs 1 and 2; Figure 3",
 "new_string": "  source: Results, Neurophysiology, paragraph 1; Figure 3"
}
```

```
The file claims/shi-2013.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/shi-2013.yaml",
 "old_string": "  source: Results, Neurophysiology, paragraphs 4 and 5; Figure 4B, C",
 "new_string": "  source: Results, Neurophysiology, paragraph 4; Figure 4B, C"
}
```

```
The file claims/shi-2013.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/shi-2013.yaml",
 "old_string": "    target, the mean endpoint position (x, y, z) of each trial over the last 800 ms of the hold;\n    V trials",
 "new_string": "    target, the mean endpoint position (x, y, z) of each trial over the last 800 ms of the hold\n    (the unit of Fig. 2, whose legend gives each point as a trial's mean over the 800 ms hold);\n    V trials"
}
```

```
The file claims/shi-2013.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -c 200 claims/shi-2013.yaml | od -c | tail -3; cat >> claims/shi-2013.yaml <<'EOF'
checks:
- date: 2026-11-09
  kind: agent
  model: "claude-opus-5-5"
  ready: true
  changes:
  - fig3-example-neuron, source was "paragraphs 1 and 2"; the 225 degree peak and the ANOVA (P = 0.52, P = 0.64) are both in paragraph 1, which runs onto page 4. Now paragraph 1.
  - fig4-indx1-means, source was "paragraphs 4 and 5"; the -13% and -31% sentences close paragraph 4 (it continues past Fig. 4 on page 5), and paragraph 5 begins "It should be noted". Now paragraph 4.
  - behavior-mean-position-sessions, the trial mean endpoint over the 800 ms hold as the MANOVA's unit was uncited; it now cites the Fig. 2 legend, which gives it.
  - Header, checked the glyph readings against the PDF's own font tables (MathPi Differences, codes 2 "<", 3 "=", 5 plus/minus, 6 minus, 8 ">"); the example cell's "P = 0.52; P = 0.64", the eye position "P < 0.05" and the Fig. 4 outlier "> 1.5 times" are as the header says. Table 1's 96 means and SDs and their signs were checked against the text; all match, and the largest V against NV difference is 0.11 cm as stated. No change.
  - Open, table1-endpoint-means and table1-endpoint-sd use a 90% of values rule, and hold-subepochs a five of six rule with "partially" at three or four; the paper gives no rule for these. Left as judging rules, not methods.
  - Open, longer-hold-no-difference picks its measures and a chi-square test that the paper does not name (it cites only an abstract, Shi and Buneo 2009); the criterion marks this as an assumption. Left.
  - Open, aborted-trials-nv and longer-hold-no-difference rest on sessions from Shi and Buneo (2009) where the window or hold was varied; whether these are among the 343 recording sessions or the extra behavioural files is not said, so `data` is left at the default for the author to settle.
EOF
python tools/claims_check.py claims/shi-2013.yaml paper/10.1152-jn.00223.2012.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked `claims/shi-2013.yaml` against the paper and made three small fixes. The file is ready for an attempt (`ready: true`).

**Checker result line:** `claims/shi-2013.yaml: 28 claims, 26 quotes, 7 statistical values, 0 problems` (same before and after my edits).

**Changes, by claim:**
- **fig3-example-neuron:** the source said paragraphs 1 and 2. The 225 degree peak and the ANOVA P values are both in paragraph 1 of Results, Neurophysiology, so I changed it to paragraph 1.
- **fig4-indx1-means:** the source said paragraphs 4 and 5. The -13% and -31% sentences end paragraph 4 (it carries on past Fig. 4), so I changed it to paragraph 4.
- **behavior-mean-position-sessions:** the criterion used each trial's mean endpoint over the 800 ms hold without citing it. It now cites the Fig. 2 legend, which defines that unit.
- **Header, no change:** the extracted text replaces some signs with a placeholder. I checked them against the PDF's own font tables, and the header's readings are right: "P = 0.52; P = 0.64", the eye-position "P < 0.05", and the Fig. 4 outliers "> 1.5 times" the interquartile range. I also compared all 96 means and SDs of Table 1, with their signs, against the text. They all match, and the largest difference between the two conditions is 0.11 cm, as the claim states.

Every other statement, quote, source, statistic, expected value and tolerance matches the paper. The P < 0.05 thresholds used to count sessions and cells are correctly left out of `statistics`. Every main finding has a claim: behaviour, the ANOVA counts, the correlation test, the two suppression indexes, rate variance, Fano factor, CV2, decoding, and the Discussion controls. None comes from outside the paper.

**Still open (recorded under `checks`):**
- The paper gives no rule for judging many values at once. Two claims use rules it does not state: the Table 1 claims need 90% of values within tolerance, and hold-subepochs needs five of six, with "partial" at three or four. I left these because they decide how a claim is judged; they do not change the analysis.
- **longer-hold-no-difference:** the paper cites only an abstract and names no measure or test. The criterion picks its own measures and a chi-square test, and marks that as an assumption.
- **aborted-trials-nv and longer-hold-no-difference:** these rest on sessions from that same 2009 abstract. The paper does not say whether they are among the 343 recordings. `data` stays at the default for the author to settle.

Nothing is committed or pushed.

## End of run

23 turns, 3 minutes, $1.20 at API prices, result: success.
