# 001641 · claims-check · run 39610568816

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001641/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001641/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l claims/001641/*.yaml paper/*.txt; cat claims/001641/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.txt",
 "offset": 389,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper read; now reading the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "limit": 450
}
```

```
1	# Claims for Ito & Doya (2009), J Neurosci 29(31):9861-9874, on dandiset 001641.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record, open access, as served by PMC (PMC6666589), stored in
6	# paper/10.1523-jneurosci.6157-08.2009.txt: abstract, Introduction, Materials and Methods,
7	# Results, Discussion, figure legends and Tables 1 to 3. Supplement read: the supplemental
8	# Methods (Supplemental_Material.pdf, 4 pages, the particle filter), extracted in the same
9	# file; its equations are garbled in the extraction and were read only for what the words say.
10	# Not available: supplemental Data 1 (left-choice probability against QL - QR), Data 2 (rasters
11	# of the Fig. 7 neurons and tone responses) and Data 3 (NAc core against shell). The main
12	# findings do not rest on them; the claims that cite them (suppdata1-choice-vs-q-difference,
13	# core-shell-no-difference) say so. No PDF of the main text was available, so the figure panels
14	# could not be read. The display equations of the Methods (conditional probability, Markov
15	# prediction, Q update, choice rule, likelihood, normalized likelihood, parameter drift,
16	# regression models, class borders and mutual information) are images on PMC and are missing
17	# from the text; only the words around them were read. The paper links no code, so no code was
18	# read.
19	#
20	# Data the paper used, as it reports them. Six male Long-Evans rats; 70 recording sessions;
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "offset": 450,
 "limit": 500
}
```

```
450	    tolerance: 0.10
451	  - quantity: F-Q alpha1
452	    value: 0.96
453	    tolerance: 0.096
454	  - quantity: F-Q kappa1
455	    value: 0.99
456	    tolerance: 0.099
457	  - quantity: F-Q kappa2
458	    value: 0.64
459	    tolerance: 0.064
460	  - quantity: F-Q Q0
461	    value: 0.00
462	    tolerance: 0.05
463	  - quantity: DF-Q alpha1
464	    value: 0.52
465	    tolerance: 0.052
466	  - quantity: DF-Q alpha2
467	    value: 0.88
468	    tolerance: 0.088
469	  - quantity: DF-Q kappa1
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "offset": 950,
 "limit": 460
}
```

```
950	- id: fig8b-nac-vp-same-event-coding
951	  statement: The NAc and VP do not differ in the percentages of neurons coding trial type, action
952	    command, chosen action and reward outcome.
953	  source: Results, Neuronal activity in the NAc and VP, paragraph 5; Figure 8B
954	  quote: Comparison of the percentages of coding neurons in the NAc and VP revealed no
955	    differences with trial type, action command, chosen action, and reward outcome (Mann–Whitney
956	    U test, p = 0.59, p = 0.19, p = 0.80, and p = 0.45, respectively)
957	  statistics:
958	  - about: state-coding, NAc against VP
959	    test: Mann–Whitney U test
960	    p: 0.59
961	  - about: action command-coding, NAc against VP
962	    test: Mann–Whitney U test
963	    p: 0.19
964	  - about: action-coding, NAc against VP
965	    test: Mann–Whitney U test
966	    p: 0.80
967	  - about: reward-coding, NAc against VP
968	    test: Mann–Whitney U test
969	    p: 0.45
[... 426 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 589,1421p 10.1523-jneurosci.6157-08.2009.txt | awk 'length($0)>25'
```

```
based on past experiences (1:
to obtain the probability distribution
, and (2) to obtain a predictive 
 based on past experiences (1:
The fundamental idea, from Bayes’ theorem, is as follows: first, we determine the 
probability distribution of 
, as prior knowledge. The prediction of the choice 
2h  are the first and the second components of the parameter vector h 
corresponding to QL and QR, respectively. When the experience e(t=1) is given, the 
posterior distribution of the parameters 
 is obtained using Bayes’ theorem 
 is the likelihood that represents the accuracy of the prediction. The 
result is used in the prediction of the parameters at t=2, namely,  
 is the transient probability of the parameters defined by the 
update rule of the parameters. By using 
, the prediction of the choice at 
The posterior distribution of the parameters 
LP t  for each trial can be obtained sequentially by 
repeating the following procedure:  
Prediction of the parameters 
[... 39 more lines not kept]
```

**Agent**

Particle count (5000) is confirmed. I'll look at the supplement PDF to check the choice rule and the drift equations, since O1 and O5 depend on them.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.6157-08.2009.supp.pdf",
 "pages": "1-4"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import fitz
d=fitz.open('10.1523-jneurosci.6157-08.2009.supp.pdf')
for i,p in enumerate(d):
    p.get_pixmap(dpi=110).save('$TMPDIR/s%d.png'%i)
print(len(d))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
grep -n "corresponding to α1 and α2\|corresponding to κ1\|formula (A)\|first and the second components" 10.1523-jneurosci.6157-08.2009.txt; grep -n "" 10.1523-jneurosci.6157-08.2009.txt | sed -n '1300,1400p' | tr '\n' ' '
```

```
658:2h  are the first and the second components of the parameter vector h 
1241:respectively, are obtained by the updating rule described by the formula (A) in the 
1296:corresponding to α1 and α2, are obtained by  
1328:t , corresponding to κ1 and κ2, are obtained by 
1300:( 1301:1) 1302:i 1303:i 1304:j 1305:j 1306:j 1307:h 1308:t 1309:h 1310:t 1311:ς 1312:= 1313:− 1314:+ 1315: for  1316:{3,4} 1317:j ∈ 1318:. ... (14)  1319:( ) 1320:5 ( ) 1321:i 1322:h 1323:t  and  1324:( ) 1325:6 ( ) 1326:i 1327:h 1328:t , corresponding to κ1 and κ2, are obtained by  1329:( ) 1330:( ) 1331:( ) 1332:( 1333:1) 1334:i 1335:i 1336:j 1337:j 1338:j 1339:h 1340:t 1341:h 1342:t 1343:ξ 1344:= 1345:− 1346:+ 1347: for  1348:{5,6} 1349:j ∈ 1350:... (15)  1351:where  1352:j 1353:ς 1354: and  1355:j 1356:ξ 1357: are noise terms drawn independently from the Gaussian  1358:distributions  1359:) 1360:,0 1361:( 1362:2 1363:α 1364:σ 1365:Ν 1366: and  1367:) 1368:,0 1369:( 1370:2 1371:κ 1372:σ 1373:Ν 1374:, respectively. The approximation of the  1375:prediction of the parameters (formula 6) is then obtained by  1376:( 1377:) 1378:( ) ( ) 1379:1 1380:1 1381:( ) | (1: 1382:1) 1383:( ) 1384:i 1385:N 1386:h 1387:t 1388:i 1389:P h t 1390:e 1391:t 1392:h 1393:N 1394:δ 1395:= 1396:− 1397:= 1398:∑ 1399:. ... (16)  1400:In this way, by repeating the procedures of formulas (9-16), we obtained the prediction
```

**Agent calls Bash**

```bash
sed -n 600,660p 10.1523-jneurosci.6157-08.2009.txt | tr '\n' ' '; echo; sed -n 1225,1260p 10.1523-jneurosci.6157-08.2009.txt | tr '\n' ' '
```

```
P h t e t − , and (2) to obtain a predictive  left-choice probability  ) (t PL  based on past experiences (1: 1) e t − .    The fundamental idea, from Bayes’ theorem, is as follows: first, we determine the  probability distribution of  ( ( 1)) P h t = , as prior knowledge. The prediction of the choice  at t=1 is obtained by  ( ) [ ] 1 2 1 1/{1 exp( ( (1) (1)))} LP E h h = + − −   [ ] 1 2 1/{1 exp( ( (1) (1)))} ( (1)) (1) h h P h dh = + − − ∫ , ... (1)  where  1h  and  2h  are the first and the second components of the parameter vector h  corresponding to QL and QR, respectively. When the experience e(t=1) is given, the  posterior distribution of the parameters  
t + .  ( ) 1 ( ) i h t  and  ( ) 2 ( ) i h t , corresponding to QL and QR,   === page 4 === respectively, are obtained by the updating rule described by the formula (A) in the  manuscript. In this formula,  ( ) 3 ( 1) i h t − ,  ( ) 4 ( 1) i h t − ,  ( ) 5 ( 1) i
```

**Agent**

Choice rule (supplement eq. 1) and the unbounded random walk of the drift equations (14, 15) match the file's O1 and O5. Making corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    block. Reproduced when, under one reading, all four\n    values are within tolerance (the range bounds as whole numbers, so 5 and 12 exactly).",
 "new_string": "    block. Reproduced when, under one reading, all four\n    values are within tolerance (the range bounds are whole numbers, so the fewest blocks must\n    be 5 and the most 11 to 13)."
}
```

```
<tool_use_error>String to replace not found in file.
String:     block. Reproduced when, under one reading, all four
    values are within tolerance (the range bounds as whole numbers, so 5 and 12 exactly).</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    the 0/1 choices that follow each history; reading O8 (b) is shown as a variant. Reproduced\n    when the test does not find a difference, both values are within tolerance, and\n    P(L|L1) < P(L|L1 L1) < P(L|L1 L1 L1) <= P(L|L1 L1 L1 L1) + 0.02 with the last within 0.05 of\n    0.75; the difference is reported either way.",
 "new_string": "    the 0/1 choices that follow each history; reading O8 (b) is shown as a variant. Reproduced\n    when the test does not find a difference, both values are within tolerance, and\n    P(L|L1) < P(L|L1 L1) < P(L|L1 L1 L1 L1), as the paper's own values are (0.68, 0.72, 0.74),\n    with P(L|L1 L1 L1 L1) within 0.075 (10%) of 0.75; P(L|L1 L1 L1) is reported. The difference\n    is reported either way."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    probability is below 0.5 and after each prefix ending in R0 it is above 0.5, with the 99%\n    interval excluding 0.5 in at least six of the eight prefixes.",
 "new_string": "    probability is below 0.5 and after each prefix ending in R0 it is above 0.5. The paper gives\n    no test; the 99% intervals are reported."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    O7. The paper gives no test. Reproduced when, under every reading, P(L|L0 L0) <\n    P(L|L0 L0 L0) <= P(L|L0 L0 L0 L0) (the last within 0.02 allowed) and both P(L|L0 L0 L0)",
 "new_string": "    O7. The paper gives no test. Reproduced when, under every reading, P(L|L0 L0) <\n    P(L|L0 L0 L0) < P(L|L0 L0 L0 L0) (\"gradually increased after two or more\") and both P(L|L0 L0 L0)"
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "  - quantity: F-Q Q0\n    value: 0.00\n    tolerance: 0.05",
 "new_string": "  - quantity: F-Q Q0\n    value: 0.00\n    tolerance: 0.01"
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "  criterion: As fig3-lsq-switching. A reported 0.00 cannot take 10% of itself, so it is given\n    0.05, the step of the table's other values. Readings as O1 (the parameter values depend on\n    the form of the update). Reproduced when, under one reading of O1, all values are within\n    tolerance; partially reproduced when at least 10 of the 14 are.",
 "new_string": "  criterion: As fig3-lsq-switching. A reported 0.00 cannot take 10% of itself, so it is given\n    0.01, one step of the table's printed precision (two decimals). Readings as O1 (the\n    parameter values depend on the form of the update). Reproduced when, under one reading of\n    O1, all values are within tolerance; partially reproduced when at least 10 of the 14 are."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    Reproduced when, under one reading, at least 13 of the 16 values are within tolerance;\n    partially reproduced for 8 to 12. The reading that matches is reported.",
 "new_string": "    Reproduced when, under one reading, all 16 values are within tolerance; partially\n    reproduced when at least 8 are. The reading that matches is reported."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    block; (d) as (c), completed blocks only. Reproduced when, under one reading, all four\n    values are within tolerance (the range bounds as whole numbers, so 5 and 12 exactly).",
 "new_string": "    block; (d) as (c), completed blocks only. Reproduced when, under one reading, all four\n    values are within tolerance (the range bounds are whole numbers, so the fewest blocks must\n    be 5 and the most 11 to 13)."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    other nine models of Fig. 5 (standard Q variable, three constant Q models, local matching\n    law, Markov orders 1 to 4). Readings O1, O3 to O6.",
 "new_string": "    other nine models of Fig. 5 (standard Q variable, three constant Q models, local matching\n    law, Markov orders 1 to 4). The paper does not say whether the tests are one- or\n    two-sided; both are readings. Readings O1, O3 to O6."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    (variable) over the 35 test sessions at p < 0.05, under every reading of O1, O3 to O5.",
 "new_string": "    (variable) over the 35 test sessions at p < 0.05, under every reading of O1, O3 to O5. The\n    paper does not give the side; the test is run two-sided, as a test of no difference with no\n    direction named, and the one-sided p is shown as a variant."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    over all 70 sessions; mean and SD over all choice trials. The tolerance of each mean is\n    its SD (protocol); each SD is also reported against the table. Readings O1, O5, O13.",
 "new_string": "    over all 70 sessions. The paper does not say over what the average and SD are taken;\n    readings are (a) over all choice trials pooled; (b) over sessions, of per-session means.\n    The tolerance of each mean is its SD (protocol); each SD is also reported against the\n    table. Readings O1, O5, O13."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    choice trials in which the rat repeated every rewarded choice and switched after every\n    unrewarded one, as Results describe it. Persevering episode, a run of at least 5\n    consecutive unrewarded choices of the less advantageous side in a (10, 50) or (50, 10)\n    block (Fig. 4B, D, F). Reproduced when, under every reading of O1, O5 and O13, some",
 "new_string": "    choice trials in which the rat repeated every rewarded choice and switched after every\n    unrewarded one, as Results describe it. Persevering episode, a run of consecutive choices\n    of the less advantageous side, rewarded or not, in a (10, 50) or (50, 10) block, as the\n    Results describe Fig. 4B, D, F (\"continued to choose the less advantageous left action\").\n    The paper gives no run length; 5, 10 and 15 trials are readings for both kinds of episode,\n    and the outcome is the one they all give. Reproduced when, under every reading of O1, O5\n    and O13, some"
}
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    (variable) mean per-trial likelihood exceeds that of standard Q (variable). The 25% and\n    the run lengths are fixed here because the paper gives none; the results for 5, 10 and 15\n    trials are shown.",
 "new_string": "    (variable) mean per-trial likelihood exceeds that of standard Q (variable). The 25% reads\n    \"close to\"; the paper gives no bound."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd ..; grep -rn -A8 "^checks:" claims/001642/*.yaml | head -30
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

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "    Reproduced when, under one reading, all 16 values are within tolerance; partially\n    reproduced when at least 8 are. The reading that matches is reported.",
 "new_string": "    O1 is a reading of what the reported values are (the parameterization), O3 to O5 readings\n    of method. Reproduced when, under one reading of O1 and every reading of O3 to O5, all 16\n    values are within tolerance; partially reproduced when at least 8 are. The O1 reading that\n    matches is reported."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001641/10.1523-jneurosci.6157-08.2009.yaml",
 "old_string": "#    normal approximation with tie correction. This is the only reading the words give.",
 "new_string": "#    normal approximation with tie correction. This is the only reading the words give, and it\n#    gives the paper's p-values from the paper's counts (two-sided: 12 of 148 against 12 of 66,\n#    p = 0.03; 11 of 148 against 14 of 66, p = 0.004; 80 of 148 against 33 of 66, p = 0.58)."
}
```

```
The file claims/001641/10.1523-jneurosci.6157-08.2009.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python -c "
from scipy.stats import mannwhitneyu
for a,b in [(12,12),(11,14),(80,33)]:
    x=[1]*a+[0]*(148-a); y=[1]*b+[0]*(66-b)
    print(mannwhitneyu(x,y,alternative='two-sided',use_continuity=False).pvalue)"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import mannwhitneyu
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python -c "
import math
for a,b in [(12,12),(11,14),(80,33)]:
    p=(a+b)/214; se=math.sqrt(p*(1-p)*(1/148+1/66)); z=abs(a/148-b/66)/se
    print(round(math.erfc(z/math.sqrt(2)),4))"
```

```
0.031
0.0038
0.5832
```

**Agent**

The recomputed p-values (0.031, 0.0038, 0.58) confirm O9. Now adding the `checks` entry and rerunning the checker.

**Agent calls Bash**

```bash
cat >> claims/001641/10.1523-jneurosci.6157-08.2009.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - block-structure. The criterion said the range bounds must be 5 and 12 exactly, against its own tolerances (12 with 1.2). Now the most blocks may be 11 to 13, as the tolerance gives.
  - fig2c-reward-effects-fade. The rise allowed a 0.02 slack and the convergence a 0.05 bound, neither from the paper. Now judged on the order of the paper's own values, P(L|L1) < P(L|L1 L1) < P(L|L1 L1 L1 L1) (0.68, 0.72, 0.74), with the last within the default 10% of 0.75.
  - fig2d-switching. The rule that the 99% interval excludes 0.5 in six of eight prefixes was made up; the paper gives no test. Removed; the intervals are reported.
  - fig2e-persevering. The 0.02 slack on the rise was made up. Removed; the rise is strict, as "gradually increased" says.
  - table1-lsq-parameters. The tolerance of the reported 0.00 (F-Q Q0) was 0.05, said to be "the step of the table's other values", but Table 1 is printed to 0.01. Set to 0.01, one step of the printed precision.
  - table2-ml-parameters. Reproduced needed only 13 of 16 values, and "one reading" covered the method readings O3 to O5. Now all 16 values must match, under one reading of O1 (what the values are) and every reading of O3 to O5.
  - fig5-fq-dfq-beat-all-models. The criterion fixed the tests as two-sided; the paper does not say. One- and two-sided are now both readings.
  - fig5-fq-dfq-no-difference. Sidedness not given; the test is run two-sided, the reading for a test of no difference, with the one-sided p shown. Open, since one-sided would make p = 0.067 about half and could find the difference.
  - table3-parameter-averages. Whether the averages are over pooled trials or over sessions is not given. Added both as readings.
  - fig4-strategy-tracking. The persevering episode was a run of unrewarded choices, but the paper describes it as continuing to choose the less advantageous side. Changed to that. The run lengths were fixed by the writer; 5, 10 and 15 are now readings that must all give the outcome.
  - Opening comment, O9. Added that the reading reproduces the paper's p-values from its counts (0.03, 0.004, 0.58 against 0.59).
  - Checked and left as they are. The particle count (5000), the choice rule (supplement equation 1) and the unbounded random walk of the parameters (supplement equations 14 and 15) are in the supplement as the file says. All quotes, sources, p-values and expected values match the text. The paper's main findings each have a claim, and no claim comes from another paper.
  - Open. Thresholds that judge qualitative words in the Fig. 9 claims (within 0.5 s, a fifth of the peak, twice the median), in suppdata1-choice-vs-q-difference (Spearman above 0.9) and in fig4-strategy-tracking (kappa2 within 25% of kappa1) are the writer's readings of words the paper gives no number for.
  - Open. Supplemental Data 1 and 3 are not in the text read, so suppdata1-choice-vs-q-difference and core-shell-no-difference are judged on readings of their missing methods.
EOF
python tools/claims_check.py claims/001641/10.1523-jneurosci.6157-08.2009.yaml paper/10.1523-jneurosci.6157-08.2009.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/001641/*.yaml | grep -n "  - .*: " ; grep -c "—" claims/001641/*.yaml; grep -ci "rather" claims/001641/*.yaml
```

```
0
0
```

**Agent**

I made 11 corrections to the claims file and marked it ready for an attempt (`ready: true`). Nothing was committed or pushed.

**Checker:** `claims/001641/10.1523-jneurosci.6157-08.2009.yaml: 46 claims, 43 quotes, 23 statistical values, 0 problems`. It passes the same way before and after my edits.

**What checked out:**
- All quotes, sources, p-values and expected values match the paper.
- The supplement confirms what the file says about the model: 5000 particles, the choice rule, and parameters that drift with no bounds.
- I recomputed the region-comparison p-values from the paper's neuron counts (0.031, 0.0038, 0.58). They match the paper's 0.03, 0.004 and 0.59, which supports how the file reads that test.
- Each main finding has a claim, and no claim comes from another paper.

**Changes, by claim:**
- **block-structure:** the criterion required the bounds to be exactly 5 and 12, contradicting its own tolerance on 12. Now the most blocks in a session may be 11 to 13.
- **fig2c-reward-effects-fade:** a 0.02 slack and a 0.05 bound were made up. It is now judged on the order of the paper's own values (0.68 < 0.72 < 0.74), with the last within the default 10% of 0.75.
- **fig2d-switching:** a made-up rule (the 99% interval excludes 0.5 in six of eight cases) is removed. The intervals are still reported.
- **fig2e-persevering:** a made-up 0.02 slack is removed, so the rise must be strict, as "gradually increased" says.
- **table1-lsq-parameters:** the tolerance on the reported 0.00 was 0.05, justified by a wrong reason (Table 1 is printed to 0.01). It is now 0.01.
- **table2-ml-parameters:** it counted as reproduced with only 13 of 16 values matching, and the split, search and bounds choices could each be picked to fit. Now all 16 must match, and the outcome must hold under every reading of those three choices.
- **fig5-fq-dfq-beat-all-models:** the paper does not say whether the tests are one- or two-sided, so both are now readings.
- **fig5-fq-dfq-no-difference:** side not given. The test is run two-sided, with the one-sided p shown as a variant.
- **table3-parameter-averages:** the paper does not say what the averages are taken over. Pooled trials and per-session means are now both readings.
- **fig4-strategy-tracking:** a persevering episode was defined as a run of unrewarded choices. It is now a run of choices of the worse side, as the paper describes it. The run lengths (5, 10, 15 trials) are readings that must all agree.
- **Opening comment:** added the p-value recomputation as support for its reading of the region test.

**Still open (recorded in `checks`):**
- **Test side for the no-difference claim:** a one-sided test would roughly halve the paper's p = 0.067, and the difference would then be significant.
- **Thresholds for vague words:** the earlier writer chose these, and the paper gives no number:
  - the information-curve claims: within 0.5 s, a fifth of the peak, twice the median;
  - suppdata1-choice-vs-q-difference: a Spearman correlation above 0.9;
  - fig4-strategy-tracking: kappa2 within 25% of kappa1.
- **Missing supplement data:** Supplemental Data 1 and 3 are not in the text. suppdata1-choice-vs-q-difference and core-shell-no-difference are judged on guesses at their methods.

## End of run

34 turns, 4 minutes, result: success.
