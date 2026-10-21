# 001605 · claims-check · run 39584209421

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001605/ paper/; grep -n "Reader" -A40 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 76,200p docs/protocol.md; python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l claims/001605/*.yaml paper/*.txt; cat claims/001605/10.1038-nn.4390.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001605/10.1038-nn.4390.yaml"
}
```

```
1	# Claims for Funamizu, Kuhn & Doya (2016), Nat Neurosci 19(12):1682-1689, on dandiset 001605.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (Nature Neuroscience, December 2016), from the PDF supplied by
6	# hand, stored as paper/10.1038-nn.4390.txt: main text, figure legends, Online Methods, and the
7	# supplement (41593_2016_BFnn4390_MOESM16_ESM.pdf: Supplementary Figs. 1 to 14 and Supplementary
8	# Table 1). The display equations of the Methods are garbled in the text; the words around them
9	# were read. PDF pages were rendered only to read Figure 1c, Figure 2c,d, Figure 4 and
10	# Supplementary Table 1 (columns), which the text garbles. Code: the paper says its Matlab scripts
11	# are "available from corresponding author upon request"; it links no code, so none was read.
12	# Data availability in the paper points to https://groups.oist.jp/ncu/data.
13	#
14	# Data the paper used, as it reports them.
15	#  - Imaging: eight male C57BL/6N mice, 94 sessions (one per day, one imaging plane), mouse 1 to 8
16	#    with 2, 10, 5, 14, 15, 15, 12 and 21 sessions. Areas PPC (LPtA, about 1.7 mm posterior and
17	#    1.6 mm lateral of bregma) and PM (V2ML, with some V2MM or MM), right hemisphere, layers 2, 3
18	#    and 5. PPC: 17, 15 and 14 sessions in layers 2, 3, 5; PM: 16, 15 and 17. 41,031 active
19	#    neurons (PPC 8,371, 7,108, 4,859; PM 7,788, 7,005, 5,900). Two-photon imaging at 30.9 Hz,
20	#    GCaMP6f with TurboRFP; signal is the green/red ratio R(t), and dR/R = (R - mean R)/mean R with
[... 906 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "offset": 926
}
```

```
926	    sound zones than in no-sound zones.
927	  source: Supplementary Figure 11c; Results, Distance prediction with dynamic Bayesian inference,
928	    paragraph 3
929	  quote: Decoding errors decreased with sound and increased without sound (Mann-Whitney U test, P =
930	    0.00295 to 1.56 × 10−6, z = 2.97 to 4.80; Supplementary Fig. 11)
931	  statistics:
932	  - about: PPC layers 2, 3, 5
933	    test: Mann-Whitney U-test
934	    statistic: z = 4.23, 2.97, 4.80
935	    p: 0.00295
936	  - about: PM layer 5 (not significant)
937	    test: Mann-Whitney U-test
938	    statistic: z = 1.32
939	    p: 0.188
940	  depends_on:
941	  - neuron-classes
942	  criterion: Supplementary Fig. 11. Per session, the difference of median RMSE between each
943	    intermittent condition and the continuous condition in 0.42-cm bins; linear regression of
944	    that difference on distance within each zone; slopes of sound zones against no-sound zones,
945	    Mann-Whitney U over zones (n = 4 zones per session, as the legend's 68 = 17 x 4). The four
[... 188 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1210
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1210,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1770,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's five "not found" values all sit in the supplement, where the "×" sign is garbled; I confirmed each by reading. Next I'll render several figures to settle bin layouts and value orders.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
for p in [1,2,3,5]:
    d[p].get_pixmap(dpi=150).save(f'm{p+1}.png')
s=fitz.open('paper/10.1038-nn.4390.supp.pdf')
print(len(s))
for p in range(len(s)):
    if 'Supplementary Figure 8' in s[p].get_text() or 'Supplementary Figure 11' in s[p].get_text(): s[p].get_pixmap(dpi=130).save(f's{p+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm; python -c "import pypdfium2" 2>&1; pdftoppm -r 130 -f 2 -l 6 -png paper/10.1038-nn.4390.pdf m && pdftoppm -r 130 -f 8 -l 9 -png paper/10.1038-nn.4390.supp.pdf s && pdftoppm -r 130 -f 12 -l 12 -png paper/10.1038-nn.4390.supp.pdf s; ls
```

Result: not kept, because it reads the paper's text.

**Agent**

Read can open PDFs directly; I'll use it for the figure pages.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.pdf",
 "pages": "6"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet pymupdf 2>&1 | tail -2; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
pip install pymupdf 2>&1 | tail -3; python -m pip --version; python -c "import pymupdf"
```

```
Exit code 1

[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
pip 26.2.1 from /opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/pip (python 3.13)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent calls Bash**

```bash
pip install --target $TMPDIR/py pymupdf 2>&1 | tail -3; PYTHONPATH=$TMPDIR/py python -c "import fitz; print('ok')"
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
[0;93m2026-10-21 10:27:34.925607069 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/py/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
for p in [1,3,5]:
    d[p].get_pixmap(dpi=160).save(f'm{p+1}.png')
s=fitz.open('paper/10.1038-nn.4390.supp.pdf')
for p in [7,11]:
    s[p].get_pixmap(dpi=130).save(f's{p+1}.png')
" 2>/dev/null; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m2.png"
}
```

Result: no output.

**Agent**

Fig. 1c shows boxes about 4.2 cm wide, with comparison brackets that span more than one box. I'll zoom in to read them.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
p=d[1]; r=p.rect
clip=fitz.Rect(r.width*0.49,r.height*0.29,r.width*0.71,r.height*0.49)
p.get_pixmap(dpi=500,clip=clip).save('f1c.png')
clip=fitz.Rect(r.width*0.23,r.height*0.49,r.width*0.65,r.height*0.64)
p.get_pixmap(dpi=400,clip=clip).save('f1f.png')
" 2>/dev/null; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f1c.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/m6.png"
}
```

Result: no output.

**Agent**

Fig. 5b lists zones in the order 25.1-8.4 then 8.4-0 cm, which confirms the PM layer 5 entry. Fig. 5c marks significant uncertainty decreases at 8.4-0 cm in every PPC layer. Now Fig. 2d.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
p=d[2]; r=p.rect
clip=fitz.Rect(0,r.height*0.05,r.width,r.height*0.75)
p.get_pixmap(dpi=170,clip=clip).save('f2.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f2.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s12.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
p=d[2]; r=p.rect
p.get_pixmap(dpi=110,clip=fitz.Rect(0,r.height*0.7,r.width,r.height)).save('p3.png')
p=d[3]; p.get_pixmap(dpi=110).save('p4.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent**

"During sound omissions" is not indented, so it continues paragraph 2. The muscimol paragraph is therefore paragraph 3. Now page 4's paragraph layout.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent**

Paragraph numbers in "Goal-distance representation" are off by one throughout: the 41,031-neuron sentence is in paragraph 1, not 2. I'll check the Methods pages for the same problem.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
for i in [6,8,10]:
    d[i].get_pixmap(dpi=100).save(f'q{i+1}.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/q9.png"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/q11.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/q7.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-nn.4390.pdf')
p=d[5]; r=p.rect
p.get_pixmap(dpi=400,clip=fitz.Rect(r.width*0.5,r.height*0.17,r.width*0.93,r.height*0.53)).save('f5c.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f5c.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
cd claims/001605 && python - <<'EOF'
import re
f='10.1038-nn.4390.yaml'
s=open(f).read()
reps=[
("Online Methods, Behavioral training, paragraph 4","Online Methods, Behavioral training, paragraph 5"),
("Online Methods, Probabilistic decoding of goal distance, paragraph 7","Online Methods, Probabilistic decoding of goal distance, paragraph 8"),
]
for a,b in reps:
    assert s.count(a)==1,a; s=s.replace(a,b)
# Results paragraph shifts, applied per section with exact text
def sh(sec, old, new):
    global s
    pat=re.compile(re.escape(sec)+r'(,\s+)paragraph '+str(old)+r'\b')
    s,n=pat.subn(lambda m: sec+m.group(1)+'paragraph '+str(new), s)
    return n
print('lick p3->2', sh('Licking indicates action-dependent distance estimation',3,2))
print('lick p4->3', sh('Licking indicates action-dependent distance estimation',4,3))
for o,n in [(2,1),(3,2),(5,4),(7,6),(8,6)]:
    print('goal',o,sh('Goal-distance representation in PPC and PM',o,n))
for o,n in [(3,2),(4,3)]:
    print('pred',o,sh('Distance prediction with dynamic Bayesian inference',o,n))
open(f,'w').write(s)
EOF
grep -n "paragraph" 10.1038-nn.4390.yaml | grep -v "^.*#" | head -60
```

```
lick p3->2 1
lick p4->3 4
goal 2 2
goal 3 1
goal 5 4
goal 7 1
goal 8 2
pred 3 5
pred 4 6
131:    paragraph 1
167:  source: Results, Goal-distance representation in PPC and PM, paragraph 1; Supplementary Table 1
201:  source: Online Methods, Behavioral training, paragraph 5
222:  source: Results, Licking indicates action-dependent distance estimation, paragraph 2; Figure 1b;
246:  source: Figure 1c; Results, Licking indicates action-dependent distance estimation, paragraph 2
278:    paragraph 2
300:  source: Figure 1d; Results, Licking indicates action-dependent distance estimation, paragraph 3
314:  source: Figure 1e; Results, Licking indicates action-dependent distance estimation, paragraph 3
338:  source: Figure 1f,g; Results, Licking indicates action-dependent distance estimation, paragraph 3
369:    paragraph 3
391:  source: Online Methods, Muscimol injection, paragraph 2
[... 29 more lines not kept]
```

**Agent**

One source, neuron-classes, breaks the section name across a line, so the regex missed it. I'll fix it by hand.

**Agent calls Read**

```json
{
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "offset": 449,
 "limit": 4
}
```

```
449	    after-reaching neurons; per session, on average 65.6, 70.3 and 34.5 in PPC and 37.6, 31.9 and
450	    7.59 in PM were goal-distance neurons.
451	  source: Figure 2d; Figure 3c legend; Supplementary Figure 6 legend; Results, Distance prediction
452	    with dynamic Bayesian inference, paragraph 3
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    with dynamic Bayesian inference, paragraph 3",
 "new_string": "    with dynamic Bayesian inference, paragraph 2"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "#  - Muscimol: three further mice, bilateral PPC injection of muscimol or PBS on alternate days,\n#    12 sessions, no imaging (Fig. 1d-g, Supplementary Fig. 2).",
 "new_string": "#  - Muscimol: three further mice, bilateral PPC injection of muscimol or PBS on alternate days,\n#    no imaging (Fig. 1d-g, Supplementary Fig. 2). Fig. 1f gives \"12 sessions, 3 mice\"; its\n#    signed-rank w reaches 78 = 12 x 13 / 2 for both muscimol and PBS, so 12 sessions of each."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "# 0 cm\", where the figures use 25.1 cm. Fig. 4c legend calls RMSE \"the expected squared\n# deviation\", while its name and the Methods take the root.",
 "new_string": "# 0 cm\", where the figures use 25.1 cm. Fig. 4c legend calls RMSE \"the expected squared\n# deviation\", while its name and the Methods take the root. The Results give positive PM slopes\n# in no-sound zones as \"P = 2.40 x 10-4 to 0, z = 3.67 to 9.59\", while Supplementary Fig. 8a\n# gives PM without sound as \"P = 0.497 to 9.97 x 10-10, z = 0.679 to 6.11\"."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent**

Now lick-goal-correlation and fig1c.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: The Methods define the correlation used to select sessions as start-to-lick distance\n    against start-to-goal distance,",
 "new_string": "  criterion: The Results do not name the two variables of r. They are read as those of the\n    Methods' session selection, since every reported P is below its 0.01 threshold. The Methods\n    define that correlation as start-to-lick distance against start-to-goal distance,"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  statement: Licking increased as mice approached the goal in all conditions, and in the\n    intermittent conditions it increased even in the no-sound zone around the goal.",
 "new_string": "  statement: Licking increased as mice approached the goal in all conditions, and in both\n    intermittent conditions it increased even within the no-sound zones (41.9-25.1 and 8.4-0 cm\n    in intermittent 1, 25.1-8.4 cm in intermittent 2)."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    statistic: z = 2.14, 5.44, 6.19, 8.41\n    p: 0.0160\n    n: 94 sessions\n  criterion: Licks per trial in goal-distance bins, mean per session, for each condition (Fig. 1c).\n    The bins and the pairs compared are not stated. The figure shows boxes about 4.2 cm wide and\n    four marked bins nearest the goal per condition. Bin readings (a) 4.2 cm, (b) 8.4 cm\n    (the half-zones of Fig. 1g); comparison readings (i) each of the four bins nearest the goal\n    against the bin before it, (ii) each against the bin 67 to 62.8 cm from the goal (or 67 to\n    58.6 cm under (a)/(b) respectively), where licking is near zero. One-sided signed-rank test\n    over sessions at the Bonferroni threshold P < 0.01 (Statistics). Reproduced when, under\n    every reading, in intermittent 1 licking rises significantly in every bin between 8.4 and\n    0 cm (the no-sound zone), and in continuous in all four bins.",
 "new_string": "    statistic: z = 2.14, 5.44, 6.19, 8.41\n    p: 0.0160\n    n: 94 sessions\n  - about: the four no-sound comparisons of both intermittent conditions (range 4.87e-8 to\n      1.22e-15)\n    test: one-sided Wilcoxon signed-rank test\n    p: 4.87e-8\n    n: 94 sessions\n  criterion: Licks per trial in goal-distance bins, mean per session, for each condition (Fig. 1c).\n    The text does not state the bins or the pairs compared; they are read from the figure. The\n    boxes are 4.2 cm wide (32 from 134 to 0 cm), and each of the four brackets compares a bin\n    with the bin 8.4 cm (two boxes) farther from the goal. The tested bins are 29.3-25.1,\n    20.9-16.7, 12.6-8.4 and 4.2-0 cm. The text confirms this. Its no-sound range, P = 4.87e-8 to\n    1.22e-15, is exactly the set of the first and fourth intermittent 1 values and the second\n    and third intermittent 2 values, the comparisons whose tested bin is silent. Bin edges at\n    multiples of 4.2 cm from the goal are a standard choice read from the figure. One-sided\n    signed-rank test over the 94 sessions (tested bin higher), at the Bonferroni threshold\n    P < 0.01 (Statistics; the legend marks P < 1e-7). Reproduced when licking rises with\n    P < 0.01 in the four no-sound comparisons (intermittent 1, first and fourth; intermittent 2,\n    second and third) and in all four continuous comparisons. The other comparisons are shown."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent**

Next, the muscimol claims.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    n: muscimol and PBS sessions of 3 mice (12 sessions)",
 "new_string": "    n: muscimol against PBS sessions of 3 mice (12 of each, read from Fig. 1f)"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  statement: After muscimol the increase of licking in no-sound zones was lost, while after PBS\n    licking increased toward the goal in every condition.",
 "new_string": "  statement: After muscimol, licking no longer increased significantly in the no-sound zones of\n    the intermittent conditions, while after PBS it did. The increase of licks between adjacent\n    bins in those no-sound zones was smaller after muscimol than after PBS."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: Fig. 1f, licks per trial per bin as in fig1c-licking-without-sound (both bin and\n    comparison readings) over the 50 to 0 cm range, separately for muscimol and PBS sessions,\n    one-sided signed-rank test over sessions, P < 0.01. Fig. 1g, per trial, the increase of lick\n    count between the adjacent bins 25-17 and 17-8.4 cm and between 17-8.4 and 8.4-0 cm, PBS\n    against muscimol trials, Mann-Whitney U, P < 0.01. Reproduced when, under every reading, no\n    no-sound bin of intermittent 1 (8.4-0 cm) or intermittent 2 (25.1-8.4 cm) shows a\n    significant increase after muscimol, and the Fig. 1g increase is larger after PBS with\n    P < 0.01 for intermittent 1 at 17-8.4 to 8.4-0 cm and intermittent 2 at 25-17 to 17-8.4 cm.",
 "new_string": "  criterion: Fig. 1f, licks per trial in 4.2-cm bins and the same four comparisons as\n    fig1c-licking-without-sound (each tested bin against the bin 8.4 cm farther from the goal;\n    the figure draws the same brackets), separately for the 12 muscimol and the 12 PBS sessions,\n    one-sided signed-rank test over sessions, P < 0.01 (legend). The text's muscimol range for\n    no-sound zones, P = 0.485 to 0.0212, is again the first and fourth intermittent 1 values and\n    the second and third intermittent 2 values. Fig. 1g, per trial, the change of lick count\n    from the 8.4-cm bin 25.1-16.7 cm to 16.7-8.4 cm and from 16.7-8.4 cm to 8.4-0 cm (the\n    legend's 25-17, 17-8.4 and 8.4-0 cm), PBS against muscimol trials, Mann-Whitney U, P < 0.01.\n    Reproduced when none of the four no-sound comparisons has P < 0.01 after muscimol, all four\n    have P < 0.01 after PBS (the paper's largest is 0.00464), and the Fig. 1g increase is larger\n    after PBS with P < 0.01 for intermittent 1 at 17-8.4 to 8.4-0 cm and intermittent 2 at 25-17\n    to 17-8.4 cm."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  - about: continuous\n    test: Mann-Whitney U-test\n    statistic: z = 4.09\n    p: 4.26e-5\n  - about: intermittent 1\n    test: Mann-Whitney U-test\n    statistic: z = 7.96\n    p: 1.79e-15\n  - about: intermittent 2\n    test: Mann-Whitney U-test\n    statistic: z = 2.29\n    p: 0.0221",
 "new_string": "  - about: continuous\n    test: Mann-Whitney U-test\n    statistic: z = 4.09\n    p: 4.26e-5\n    n: 1,407 PBS and 1,188 muscimol trials\n  - about: intermittent 1\n    test: Mann-Whitney U-test\n    statistic: z = 7.96\n    p: 1.79e-15\n    n: 293 PBS and 240 muscimol trials\n  - about: intermittent 2\n    test: Mann-Whitney U-test\n    statistic: z = 2.29\n    p: 0.0221\n    n: 259 PBS and 230 muscimol trials"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: Per trial mean locomotion speed and lick count from start to goal, muscimol against\n    PBS trials, Mann-Whitney U (two-sided, Statistics); intermittent 1 and 2 pooled as the text\n    reports one test. The no-change parts are claims of absence, judged at P < 0.05. Reproduced\n    when continuous speed is lower and licking higher after muscimol with P < 0.05, and neither\n    differs with P < 0.05 in intermittent trials.",
 "new_string": "  criterion: Per trial, muscimol against PBS trials, Mann-Whitney U (two-sided, Statistics);\n    intermittent 1 and 2 pooled, as the text reports one test. The paper does not define the\n    measures. Readings for speed, (a) mean speed from start to goal, (b) mean speed from start\n    to reward. Readings for licking, (a) lick count from start to goal, (b) lick count from\n    start to reward. The no-change parts are claims of absence, judged at P < 0.05. Reproduced\n    when, under every reading, continuous speed is lower and licking higher after muscimol with\n    P < 0.05, and neither differs with P < 0.05 in intermittent trials."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent**

Now the Fig. 2 claims and neuron-classes.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    over session counts. This claim selects the neurons other claims use.",
 "new_string": "    over session counts. Fig. 2d also gives goal-distance or reward neurons (1,745, 1,456 and\n    651 in PPC; 816, 625 and 183 in PM), so reward neurons are 629, 402, 168; 215, 146, 54.\n    These are shown, not judged. This claim selects the neurons other claims use."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    neurons, which fit reading (b) within 2%).",
 "new_string": "    neurons, which over the active counts give 41.8, 33.4, 21.5, 19.7, 16.8 and 5.37%, so the\n    reported values are probably per-session means, reading (a); all are within tolerance under\n    either reading except PPC layer 5 under (b) at the edge)."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    neurons, which over the active counts give 41.8, 33.4, 21.5, 19.7, 16.8 and 5.37%, so the\n    reported values are probably per-session means, reading (a); all are within tolerance under\n    either reading except PPC layer 5 under (b) at the edge).",
 "new_string": "    neurons, which over the active counts give 41.8, 33.4, 21.5, 19.7, 16.8 and 5.37%. These\n    differ from the reported values by up to 1.5 percentage points, so the reported values are\n    probably per-session means, reading (a); the pooled values still lie within tolerance)."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: Per-session proportion of goal-distance neurons among active neurons, PPC against PM\n    per layer, Mann-Whitney U over sessions. Reproduced when, under every reading of O1 to O3,",
 "new_string": "  criterion: Per session, goal-distance neurons, PPC against PM per layer, Mann-Whitney U over\n    sessions. Whether counts or proportions of active neurons are compared is not said;\n    readings (a) proportion of active neurons, (b) count. Reproduced when, under every reading\n    of O1 to O3 and of the measure,"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  statement: In both PPC and PM, goal-distance neurons in layers 3 and 5 preferred distances closer\n    to the goal than those in layer 2; layers 3 and 5 did not differ.",
 "new_string": "  statement: In both PPC and PM, goal-distance neurons in layers 3 and 5 preferred distances closer\n    to the goal than those in layer 2."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent**

Next, supp8a, supp8c and supp9.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    statistic: z = 0.679 to 6.11\n    p: 0.497\n  depends_on:\n  - neuron-classes\n  criterion: Slopes as in fig3c-continuous-ramp, PM after-reaching neurons, no-sound zones\n    (intermittent 1, 8.4-0 cm; intermittent 2, 25.1-8.4 cm), signed-rank against zero, P < 0.01\n    (the legend's threshold). Reproduced when, under every reading, at least one PM no-sound test\n    is positive with P < 0.01 in intermittent 2, and in intermittent 1 at least one PM layer is\n    not significantly positive. Per layer results are shown.",
 "new_string": "    statistic: z = 0.679 to 6.11\n    p: 0.497\n  - about: PM, no-sound zones with positive slopes (Results; range 2.40e-4 to 0)\n    test: Wilcoxon signed-rank test\n    statistic: z = 3.67 to 9.59\n    p: 2.40e-4\n  depends_on:\n  - neuron-classes\n  criterion: Slopes as in fig3c-continuous-ramp, PM after-reaching neurons, no-sound zones\n    (intermittent 1, 8.4-0 cm; intermittent 2, 25.1-8.4 cm), signed-rank against zero per\n    layer, P < 0.01 (the legend's threshold). Supplementary Fig. 8a marks all three PM layers\n    significant in intermittent 2 at 25.1-8.4 cm and none in intermittent 1 at 8.4-0 cm.\n    Reproduced when, under every reading, all three PM intermittent 2 no-sound tests are\n    positive with P < 0.01 and no PM intermittent 1 no-sound test is (the latter a claim of\n    absence, judged by the paper's test). Per layer results are shown."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    (the only order under which the legend supports the text's layers 2 and 3). Reproduced when, under every",
 "new_string": "    (the only order under which the legend supports the text's layers 2 and 3). The figure\n    confirms it: in each zone the red intermittent 1 pair is drawn first, and the stars fall on\n    the no-sound pairs as read. Reproduced when, under every"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: Per goal-distance neuron, the absolute difference between its distance preference\n    (O4) in continuous trials and in intermittent 1 (and 2) trials;",
 "new_string": "  criterion: Per goal-distance neuron, the difference between its distance preference (O4) in\n    continuous trials and in intermittent 1 (and 2) trials. The legend says only \"difference\";\n    readings (i) absolute difference, (ii) signed difference, intermittent minus continuous;"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "continuous trials and in intermittent 1 (and 2) trials. The legend says only \"difference\";\n    readings (i) absolute difference, (ii) signed difference, intermittent minus continuous;",
 "new_string": "continuous trials and in intermittent 1 (and 2) trials. The legend says only \"difference\";\n    it is read as the absolute difference, the only reading under which a smaller value means\n    a better preserved preference (signed differences are shown);"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "id: supp11",
 "path": "claims/001605/10.1038-nn.4390.yaml",
 "output_mode": "content",
 "-A": 28
}
```

```
963:- id: supp11-sound-reduces-error
964-  statement: Decoding errors decreased with sound and increased without it, so RMSE was lower in
965-    sound zones than in no-sound zones.
966-  source: Supplementary Figure 11c; Results, Distance prediction with dynamic Bayesian inference,
967-    paragraph 2
968-  quote: Decoding errors decreased with sound and increased without sound (Mann-Whitney U test, P =
969-    0.00295 to 1.56 × 10−6, z = 2.97 to 4.80; Supplementary Fig. 11)
970-  statistics:
971-  - about: PPC layers 2, 3, 5
972-    test: Mann-Whitney U-test
973-    statistic: z = 4.23, 2.97, 4.80
974-    p: 0.00295
975-  - about: PM layer 5 (not significant)
976-    test: Mann-Whitney U-test
977-    statistic: z = 1.32
978-    p: 0.188
979-  depends_on:
980-  - neuron-classes
981-  criterion: Supplementary Fig. 11. Per session, the difference of median RMSE between each
982-    intermittent condition and the continuous condition in 0.42-cm bins; linear regression of
[... 9 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  statement: Decoding errors decreased with sound and increased without it, so RMSE was lower in\n    sound zones than in no-sound zones.\n  source: Supplementary Figure 11c;",
 "new_string": "  statement: Decoding errors decreased with sound and increased without it. Within zones, the\n    change per cm of the RMSE difference (intermittent minus continuous) was lower in sound zones\n    than in no-sound zones, in all PPC layers and in PM layers 2 and 3.\n  source: Supplementary Figure 11b,c;"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "  criterion: Supplementary Fig. 11. Per session, the difference of median RMSE between each\n    intermittent condition and the continuous condition in 0.42-cm bins; linear regression of\n    that difference on distance within each zone; slopes of sound zones against no-sound zones,\n    Mann-Whitney U over zones (n = 4 zones per session, as the legend's 68 = 17 x 4). The four\n    zones are read as the two zones of Fig. 5b,d in each intermittent condition. Reproduced when, under every\n    reading, RMSE rises more steeply (or falls less) without sound with P < 0.01 in all PPC\n    layers.",
 "new_string": "  criterion: Supplementary Fig. 11b,c. Per session, dRMSE, the difference of median RMSE (over\n    trials) between each intermittent condition and the continuous condition in 0.42-cm bins.\n    Linear regression of dRMSE on distance within each zone, y = b0 - b1 distance, so b1 is the\n    rise per cm of approach (Fig. 11c axis, \"dRMSE per cm\"). Then b1 of sound zones against b1\n    of no-sound zones, Mann-Whitney U. Fig. 11b shows four zones per intermittent condition\n    (58.6-41.9, 41.9-25.1, 25.1-8.4 and 8.4-0 cm). The legend's \"n = 68 (that is, 17 sessions\n    times 4)\" allows two readings. (a) Four sound and four no-sound zones per session, n = 68 per\n    group. (b) 68 zones in all, the zones 25.1-8.4 and 8.4-0 cm of both conditions, two sound and\n    two no-sound per session. Decoder sessions exclude the 3 with no goal-distance neurons, which\n    fits PM layer 5's 14 sessions. Reproduced when, under every reading, b1 is lower with sound\n    with P < 0.01 in all PPC layers. PM is shown."
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent**

Next, the SVM criterion and the new Fig. 5c claim.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    validated as the probabilistic decoder; the shuffled set permutes each neuron's activity\n    across training trials at the same goal distance. Kernel, classes and error measure are not\n    given;",
 "new_string": "    validated as the probabilistic decoder. The paper says only \"shuffled data\" (refs. 49, 50);\n    the shuffle is read as the standard one of those references, each neuron's activity\n    permuted independently across training trials at the same goal distance (4.2-cm bin).\n    Kernel, classes and error measure are not given;"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "^- id: lognormal-decoder-better",
 "path": "claims/001605/10.1038-nn.4390.yaml",
 "output_mode": "content",
 "-B": 8
}
```

```
1119-    p: 0.00285
1120-  depends_on:
1121-  - neuron-classes
1122-  criterion: Per trial s.d.-of-posterior slopes (decrease per cm, equation 10) in the zones
1123-    25.1-8.4 and 8.4-0 cm, sound trials against no-sound trials per zone as in
1124-    fig5b-map-slope-lower-without-sound, Mann-Whitney U. Reproduced when, under every reading,
1125-    the decrease is larger with sound with P < 0.05 in all six PPC comparisons. PM results are
1126-    shown (the paper reports them mixed).
1127:- id: lognormal-decoder-better
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "    shown (the paper reports them mixed).\n- id: lognormal-decoder-better",
 "new_string": "    shown (the paper reports them mixed).\n- id: fig5c-uncertainty-decreases-with-sound\n  statement: In all PPC layers, the uncertainty of the decoded distance (s.d. of the posterior)\n    decreased during sound presentation between 8.4 and 0 cm.\n  source: Figure 5c and legend\n  quote: Uncertainty decreased during sound presentations in PPC between 8.4 cm and 0 cm.\n  depends_on:\n  - neuron-classes\n  criterion: Per trial s.d.-of-posterior slope (decrease per cm, equation 10) in the zone 8.4-0\n    cm, signed-rank test against zero over trials per area, layer and condition, P < 0.01 (Fig.\n    5c, \"Data presentation as in a\"). The legend gives only the range over all Fig. 5c tests\n    (P = 0.892 to 0), so no statistic is recorded. Fig. 5c marks, in the 8.4-0 cm zone of each\n    PPC layer, the continuous and intermittent 2 tests, the two conditions with sound there.\n    Reproduced when, under every reading of O7 and O8, the decrease is positive with P < 0.01 in\n    all six (three PPC layers, continuous and intermittent 2). PM and intermittent 1 are shown.\n- id: lognormal-decoder-better"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt; grep -n "checks" claims/001605/*.yaml; grep -rn "checks:" claims/*/*.yaml | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/    confirms it: in each zone the red intermittent 1 pair/    confirms it, since in each zone the red intermittent 1 pair/' claims/001605/10.1038-nn.4390.yaml && grep -nE "^\s+\S.*\S: " claims/001605/10.1038-nn.4390.yaml | grep -vE "^\s*[0-9]+:\s*(- )?[a-z_]+: " | head; python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt; sed -n 1092,1110p claims/000005/10.1038-nn.4412.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/001605/10.1038-nn.4390.yaml; tail -3 claims/001605/10.1038-nn.4390.yaml
```

```
absolute error. One-sided signed-rank test (recorded better) over frames per setting.
    Reproduced when, under every reading, no more than one of the 18 settings shows the recorded
    SVM better with P < 0.01; not reproduced when more do.
```

**Agent calls Bash**

```bash
cat >> claims/001605/10.1038-nn.4390.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker result 40 claims, 40 quotes, 78 statistical values, 6 problems. All six are values printed with a garbled "x 10-n" in the supplement text (supp1 1.27e-4 and 9.81e-8, supp2d 4.26e-5, supp8c 2.15e-7, supp13 8.60e-4) or in the Results (supp8a 2.40e-4, line "P = 2.40 x 10-4 to 0"). Each was confirmed by reading.
  - Sources. Several paragraph numbers were off by one. "During sound omissions" continues Results paragraph 2 of the licking section (no indent in the PDF), so supp1 is paragraph 2 and the muscimol claims are paragraph 3. In "Goal-distance representation" the 41,031-neuron sentence is in paragraph 1, so session-counts and neuron-counts are paragraph 1, sound-responsive 2, the Fig. 2d claims 4, and fig3b, supp6 and tuning-similar 6. In "Distance prediction" the comparison of PPC and PM is paragraph 2 (neuron-classes, the fig4 claims, supp11), and the Fig. 5 text is paragraph 3. Behaviour timing is Behavioral training paragraph 5; the SVM text is decoding paragraph 8.
  - fig1c-licking-without-sound. The statement put the intermittent 2 no-sound zone around the goal, where intermittent 2 has sound; it now names each condition's no-sound zones. The criterion's bin and comparison readings (adjacent 4.2-cm bins, or a baseline at 67 cm) did not match Fig. 1c. The figure's brackets compare 4.2-cm bins 8.4 cm apart, the tested bins being 29.3-25.1, 20.9-16.7, 12.6-8.4 and 4.2-0 cm. The text's no-sound P range is exactly the set of comparisons whose tested bin is silent under this layout. The criterion now uses it and tests intermittent 2 as well. Added the no-sound range as a statistic.
  - fig1fg-muscimol-no-sound-licking. The statement said PBS licking increased "in every condition", but two PBS comparisons have P > 0.01. It now says what the text and legend support, that PBS licking still increased in the no-sound zones. The criterion uses the Fig. 1c layout (the muscimol no-sound range again matches those comparisons) and checks the PBS no-sound comparisons.
  - fig1d-muscimol-correlation and header. The n "12 sessions" was read as the total. Fig. 1f's signed-rank w reaches 78 = 12 x 13 / 2 for both muscimol and PBS, so 12 sessions of each.
  - supp2d-muscimol-overrun. Added the legend's trial numbers as n.
  - muscimol-locomotion. The criterion fixed speed and licking measures (start to goal) that the paper does not give. They are now named as open, with readings.
  - lick-goal-correlation. Said that the Results do not name the variables of r, and why the Methods' selection correlation is the reading.
  - fig2d-task-relevant-proportions. The note said the pooled Fig. 2d counts fit the reported percentages "within 2%". They differ by up to 1.5 percentage points (PPC layer 5, 21.5 against 20.0%). Corrected.
  - fig2d-goal-distance-ppc-more. The criterion fixed proportions where the paper does not say whether counts or proportions were compared; both are now readings.
  - fig2d-layer-distance-preference. Removed "layers 3 and 5 did not differ" from the statement. The legend gives those P values but the paper states no such finding, and the criterion does not test it.
  - neuron-classes. Added the Fig. 2d goal-distance-or-reward counts as values shown, not judged.
  - supp8a-pm-no-sound. Supplementary Fig. 8a marks all three PM layers significant at 25.1-8.4 cm in intermittent 2 and none at 8.4-0 cm in intermittent 1. The criterion asked only for one of each, which is weaker than the paper. Tightened. Added the Results range for positive PM slopes (P = 2.40e-4 to 0), which conflicts with the legend's range; the conflict is noted in the header.
  - supp8c-ppc-steeper-than-pm. Noted that the figure confirms the order of the legend's P values that the criterion assumed.
  - supp9-preserved-representation. The criterion took "difference" as absolute without saying so. It now says this is a reading, and why.
  - supp11-sound-reduces-error. The statement said RMSE was lower in sound zones. Supplementary Fig. 11c compares slopes of dRMSE per cm, not RMSE levels, so the statement was restated. The criterion read n = 68 as two zones per condition. Fig. 11b shows four zones per condition, so both readings of n are now named.
  - svm-correlations. The shuffle method was stated as fact; the paper says only "shuffled data". It is now named as a reading.
  - Added claim fig5c-uncertainty-decreases-with-sound, the Fig. 5c legend's finding that uncertainty decreased with sound in PPC between 8.4 and 0 cm. This is the within-condition side of the updating result and had no claim.
  - Open. The Fig. 1c and 1f bin edges and pairs are read from the figure, and the text's P ranges support that reading. The paper states neither in words.
  - Open. Fig. 1d plots sessions 1 to 10, while Fig. 1f's w values imply 12 sessions per injection type. The number of sessions behind the Fig. 1d test cannot be settled from the paper.
  - Open. The Results and Supplementary Fig. 8a give incompatible ranges for PM no-sound slopes (z up to 9.59 against 6.11). The criterion follows the legend's per-layer marks.
EOF
python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt | tail -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/001605/10.1038-nn.4390.yaml | grep -n "  - .*: " ; git status --short
```

```
M claims/001605/10.1038-nn.4390.yaml
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

I checked the claims file against the paper, fixed what was wrong, and added the new `checks` entry. The file is ready for an attempt (`ready: true`). Nothing is committed.

**Checker:** `40 claims, 40 quotes, 78 statistical values, 6 problems`. All six are p-values where the text extraction garbled the "× 10⁻ⁿ" (supp1 ×2, supp2d, supp8c, supp13, supp8a). I found each one printed in the paper. The quotes all pass.

PyMuPDF wasn't installed and the system install failed, so I installed it into `$TMPDIR` to render figures. The untracked files in the repo root were already there; I didn't touch them.

**Changes, by claim**
- **Sources (about 25 claims):** many paragraph numbers were off by one. The PDF's indentation shows "During sound omissions" continues paragraph 2, and the 41,031-neuron sentence is in paragraph 1 of its section. The Methods references for behaviour timing (now paragraph 5) and the SVM (now paragraph 8) are also fixed.
- **fig1c-licking-without-sound:**
  - The statement put intermittent 2's no-sound zone around the goal, where that condition actually has sound. It now names each condition's no-sound zones.
  - The criterion's bin and comparison readings were invented and didn't match the figure. Fig. 1c compares 4.2-cm bins 8.4 cm apart. This layout makes the text's no-sound P range (4.87e-8 to 1.22e-15) come out exactly. The criterion now uses it and also tests intermittent 2.
- **fig1fg-muscimol-no-sound-licking:** the statement said PBS licking rose "in every condition", but two PBS comparisons have P > 0.01. Rewritten to what the paper supports, and the criterion now uses the Fig. 1c layout (the muscimol no-sound range matches it too).
- **fig1d-muscimol-correlation** and the header: n is 12 muscimol and 12 PBS sessions, not 12 in total. Fig. 1f's signed-rank w reaches 78 = 12×13/2 for both groups.
- **supp2d-muscimol-overrun:** added the trial numbers (n).
- **muscimol-locomotion:** the speed and lick measures were made up; they are now listed as open, with readings.
- **lick-goal-correlation:** now says the Results don't name what r correlates, and why the Methods' session-selection correlation is the reading.
- **fig2d-task-relevant-proportions:** the note said pooled counts fit "within 2%"; they differ by up to 1.5 percentage points. Corrected.
- **fig2d-goal-distance-ppc-more:** whether counts or proportions were compared is now an open reading.
- **fig2d-layer-distance-preference:** removed "layers 3 and 5 did not differ" from the statement. The paper never states it and the criterion doesn't test it.
- **neuron-classes:** added the Fig. 2d goal-distance-or-reward counts, shown but not judged.
- **supp8a-pm-no-sound:** the criterion was weaker than the paper. Supplementary Fig. 8a marks all three PM layers significant in intermittent 2 and none in intermittent 1; the criterion now requires that. I also added the Results' P range for PM.
- **supp8c-ppc-steeper-than-pm:** noted that the figure confirms the order of P values the criterion assumed.
- **supp9-preserved-representation:** "absolute difference" was presented as given; it is now marked as a reading, with the reason.
- **supp11-sound-reduces-error:** Supplementary Fig. 11c compares slopes of the RMSE difference, not RMSE levels, so the statement is restated. The legend's n = 68 allows two readings, and both are now named.
- **svm-correlations:** the shuffle method was stated as fact; it is now a named reading.
- **New claim, fig5c-uncertainty-decreases-with-sound:** PPC uncertainty falls with sound between 8.4 and 0 cm (Fig. 5c). This was a main updating finding with no claim.

**Still open**
- The Fig. 1c and 1f bins and the pairs compared come from the figures. The paper's P ranges support that reading, but no sentence states it.
- Fig. 1d plots sessions 1 to 10, while Fig. 1f implies 12 sessions per injection type. The paper doesn't settle which sessions the Fig. 1d test used.
- For PM no-sound slopes, the Results give z up to 9.59 and Supplementary Fig. 8a up to 6.11; the two can't both be right. The criterion follows the figure's per-layer marks, and the header records the conflict.

## End of run

68 turns, 9 minutes, result: success.
