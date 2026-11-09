# crcns-rrf-1 · claims · run 42179787682

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^## " docs/protocol.md; ls claims/001453 claims/crcns-rrf-1 paper; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | head -50; ls claims/crcns-* 2>/dev/null | head; cat tools/claims_check.py | head -60
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -t claims/crcns-*/*.yaml | head -3; f=$(ls -t claims/crcns-*/*.yaml | head -1); head -80 "$f"; grep -n "data\|code" schemas/claims.schema.json | head -40
```

```
claims/crcns-pfc-6/10.1038-nn.2337.yaml
claims/crcns-ret-1/10.1242-dev.027912.yaml
claims/crcns-ia-1/10.3389-neuro.10.003.2008.yaml
# Claims for Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009), Nat Neurosci 12:919-926,
# on CRCNS data set pfc-6 (doi:10.6080/K0KH0KH5).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-05,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Results, Discussion, figure legends and Online Methods, and the supplement
# (41593_2009_BFnn2337_MOESM12_ESM.pdf), from which the Supplementary Discussion, the legends of
# Supplementary Figures 2 to 13 and Supplementary Table 1 were read. The legend of
# Supplementary Figure 1 (histology) is not in the extracted text; no claim rests on it. The PDF
# pages could not be rendered here, so no figure was read from the image. The extracted text
# prints some signs as other glyphs. "P o" is P <, "P 4" is P >, "n 1⁄4" is n =, "B" before a
# number is "about", and "10�30" is 10 to the power -30. Quotes keep these glyphs as printed,
# and the p-values below are read from them; the quote checker cannot find p-values printed as
# powers of ten, which were confirmed by reading. The paper links no analysis code, so none was
# read; every method below is from the Online Methods, the figure legends or the supplement.
#
[... 77 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2021.02.055.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2021.02.055.txt",
 "offset": 1001,
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Figure S|Table S|Related to|CI \\[|M = ",
 "path": "paper/10.1016-j.cub.2021.02.055.txt",
 "offset": 20,
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2021.02.055.txt",
 "offset": 2100,
 "limit": 790
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/rrf-1.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -sL -m 20 http://mcdannaldlab.org/resources | sed 's/<[^>]*>/ /g' | tr -s ' \n' | head -c 3000; echo; python -c "import fitz; print(fitz.__doc__)"
```

Result: the fetched text is not kept.

**Agent**

The lab resources page returns 404 and the paper's MATLAB code is deposited only inside the dataset, so no code can be read. Checking the supplementary tables' layout in the PDF.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2021.02.055.pdf",
 "pages": "26-29"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1; which mutool pdftotext qpdf gs 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json;s=json.load(open('schemas/claims.schema.json'))
def walk(d,p=''):
    if isinstance(d,dict):
        if 'properties' in d: print(p, list(d['properties']), d.get('required'))
        for k,v in d.items(): walk(v,p+'/'+k)
    elif isinstance(d,list):
        for i,v in enumerate(d): walk(v,p+f'[{i}]')
walk(s)
E
grep -n '"expected"' -A40 schemas/claims.schema.json | grep -n 'description' | head -20
```

```
['schema_version', 'dataset', 'paper', 'claims', 'checks'] ['schema_version', 'dataset', 'paper', 'claims']
/properties/dataset ['archive', 'id', 'doi'] ['archive', 'id']
/properties/dataset/if ['archive'] None
/properties/dataset/then ['id'] None
/properties/claims/items ['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where'] ['id', 'statement', 'source']
/properties/claims/items/allOf[1]/if ['kind'] ['kind']
/properties/claims/items/allOf[2]/if ['data'] ['data']
/properties/checks/items ['date', 'kind', 'model', 'by', 'ready', 'changes'] ['date', 'kind', 'ready']
/$defs/expected ['quantity', 'value', 'tolerance', 'unit'] ['quantity', 'value']
/$defs/statistic ['about', 'test', 'statistic', 'p', 'p_relation', 'corrected', 'ci', 'n'] None
/$defs/statistic/properties/ci ['level', 'low', 'high', 'unit'] ['low', 'high']
2:105-            "description": "The reported numbers the claim rests on, each with a tolerance: one, or a list.",
17:120-            "description": "The statistical support the paper reports for the finding: one entry per test or interval, as the paper gives it. A record of the paper, not a target with a tolerance (that is `expected`).",
25:128-            "description": "For a claim without a number, how it will be judged. Written before the analysis is run.",
29:132-            "description": "Ids of claims in this file whose result this one uses.",
37:140-            "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
83:285-          "description": "Wh
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/"\$defs"/,$p' schemas/claims.schema.json | head -80
```

```
"$defs": {
    "expected": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "quantity",
        "value"
      ],
      "properties": {
        "quantity": {
          "type": "string"
        },
        "value": {
          "type": "number"
        },
        "tolerance": {
          "type": "number",
          "minimum": 0
        },
        "unit": {
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  pip install --target $TMPDIR/pylib pymupdf -q 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python -c "
import fitz;d=fitz.open('paper/10.1016-j.cub.2021.02.055.pdf');print(len(d))
for i in [8,25,27,28,22,2,7]:
    d[i].get_pixmap(dpi=110).save('$TMPDIR/p%d.png'%(i+1))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz;d=fitz.open('paper/10.1016-j.cub.2021.02.055.pdf');p=d[8];r=p.rect
clip=fitz.Rect(r.x0+r.width*0.2,r.y0+r.height*0.13,r.x0+r.width*0.45,r.y0+r.height*0.92)
p.get_pixmap(dpi=220,clip=clip).save('$TMPDIR/p9a.png')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9a.png"
}
```

Result: no output.

**Agent**

Figure 6's analysis windows read from the rendered page: 0 to 8 s after shock offset for k1, k3, k5, k6, the full 17.5 s for the others. Checking the supplementary table layouts.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p29.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p28.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p26.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent**

Table layouts confirmed (S1: D−U then U−S; S2: PP, FO, PP−FO; S4: D, US, UO, S). Generating the table-derived expected values, then writing the claims file.

**Agent calls Bash**

```bash
cd  python - <<'E'
def t(m,l,u): return round(max(m-l,u-m),3)
S2=dict(pre1=(0.02,-0.02,0.07,-0.01,-0.05,0.03),pre2=(-0.02,-0.07,0.02,0.01,-0.03,0.05),
cue1=(0.46,0.34,0.56,0.06,-0.01,0.14),cue2=(0.45,0.35,0.55,0.12,0.03,0.21),cue3=(0.43,0.33,0.52,0.14,0.06,0.21),
cue4=(0.38,0.29,0.47,0.18,0.10,0.27),cue5=(0.46,0.38,0.55,0.18,0.11,0.26),cue6=(0.50,0.40,0.61,0.17,0.08,0.26),
cue7=(0.56,0.45,0.67,0.10,0.02,0.19),cue8=(0.55,0.45,0.66,0.13,0.03,0.25),cue9=(0.55,0.44,0.65,0.20,0.11,0.29),
cue10=(0.52,0.42,0.62,0.16,0.06,0.25),delay1=(0.44,0.34,0.53,0.17,0.08,0.25),delay2=(0.49,0.39,0.58,0.14,0.04,0.23))
out=[]
for b,v in S2.items():
    out.append(f"  - quantity: peak threat probability beta, {b}\n    value: {v[0]}\n    tolerance: {t(*v[:3])}")
for b,v in S2.items():
    out.append(f"  - quantity: fear output beta, {b}\n    value: {v[3]}\n    tolerance: {t(*v[3:])}")
open('/tmp/claude-1001/s2.yaml','w').write("\n".join(out)+"\n")
ks=['k1','k2','k3','k4','k5','k6','k7','k8']
S4={'danger':[(0.19,0.01,0.37),(0.33,0.28,0.38),(0.07,-0.20,0.30),(0.19,0.14,0.25),(0.04,-0.07,0.14),(-0.17,-0.24,-0.08),(0.29,0.24,0.35),(-0.11,-0.16,-0.05)],
'uncertainty shock':[(0.20,0.03,0.37),(-0.18,-0.25,-0.12),(-0.03,-0.24,0.15),(0.25,0.20,0.31),(-0.05,-0.16,0.03),(-0.32,-0.40,-0.22),(0.42,0.35,0.50),(0.32,0.25,0.39)],
'uncertainty omission':[(-0.02,-0.13,0.10),(-0.05,-0.09,0.003),(0.20,-0.02,0.43),(-0.16,-0.19,-0.12),(0.25,0.17,0.32),(0.02,-0.05,0.07),(0.08,0.03,0.13),(0.18,0.14,0.21)],
'safety':[(0.15,0.05,0.24),(0.06,0.01,0.11),(-0.18,-0.27,-0.07),(0.20,0.15,0.24),(-0.07,-0.14,-0.003),(0.26,0.20,0.33),(-0.28,-0.33,-0.22),(-0.02,-0.06,0.02)]}
for i,k in enumerate(ks):
    o=[]
    for tt,vals in S4.items():
        m,l,u=vals[i]; o.append(f"  - quantity: {k} {tt}, mean normalized firing\n    value: {m}\n    tolerance: {t(m,l,u)}")
    open(f'/tmp/claude-1001/s4_{k}.yaml','w').write("\n".join(o)+"\n")
    print(k, [ (tt,vals[i]) for tt,vals in S4.items()])
S1={'D-U':[(0.51,0.30,0.74),(0.27,0.20,0.33),(0.73,0.37,0.95),(0.01,-0.05,0.07),(0.33,0.20,0.45),(-0.23,-0.30,-0.15),(0.21,0.08,0.33),(-0.45,-0.51,-0.38)],
'U-S':[(0.25,-0.11,0.59),(-0.30,-0.37,-0.23),(0.62,0.38,0.80),(-0.50,-0.56,-0.44),(0.35,0.24,0.44),(-0.37,-0.44,-0.29),(0.27,0.17,0.37),(0.06,-0.01,0.13)]}
for i,k in enumerate(ks):
    print(k,'D-U',S1['D-U'][i],t(*S1['D-U'][i]),'U-S',S1['U-S'][i],t(*S1['U-S'][i]))
E
```

```
k1 [('danger', (0.19, 0.01, 0.37)), ('uncertainty shock', (0.2, 0.03, 0.37)), ('uncertainty omission', (-0.02, -0.13, 0.1)), ('safety', (0.15, 0.05, 0.24))]
k2 [('danger', (0.33, 0.28, 0.38)), ('uncertainty shock', (-0.18, -0.25, -0.12)), ('uncertainty omission', (-0.05, -0.09, 0.003)), ('safety', (0.06, 0.01, 0.11))]
k3 [('danger', (0.07, -0.2, 0.3)), ('uncertainty shock', (-0.03, -0.24, 0.15)), ('uncertainty omission', (0.2, -0.02, 0.43)), ('safety', (-0.18, -0.27, -0.07))]
k4 [('danger', (0.19, 0.14, 0.25)), ('uncertainty shock', (0.25, 0.2, 0.31)), ('uncertainty omission', (-0.16, -0.19, -0.12)), ('safety', (0.2, 0.15, 0.24))]
k5 [('danger', (0.04, -0.07, 0.14)), ('uncertainty shock', (-0.05, -0.16, 0.03)), ('uncertainty omission', (0.25, 0.17, 0.32)), ('safety', (-0.07, -0.14, -0.003))]
k6 [('danger', (-0.17, -0.24, -0.08)), ('uncertainty shock', (-0.32, -0.4, -0.22)), ('uncertainty omission', (0.02, -0.05, 0.07)), ('safety', (0.26, 0.2, 0.33))]
k7 [('danger', (0.29, 0.24, 0.35)), ('uncertainty shock', (0.42, 0.35, 0.5)), ('uncertainty omission', (0.08, 0.03, 0.13)), ('safety', (-0.28, -0.33, -0.22))]
k8 [('danger', (-0.11, -0.16, -0.05)), ('uncertainty shock', (0.32, 0.25, 0.39)), ('uncertainty omission', (0.18, 0.14, 0.21)), ('safety', (-0.02, -0.06, 0.02))]
k1 D-U (0.51, 0.3, 0.74) 0.23 U-S (0.25, -0.11, 0.59) 0.36
k2 D-U (0.27, 0.2, 0.33) 0.07 U-S (-0.3, -0.37, -0.23) 0.07
k3 D-U (0.73, 0.37, 0.95) 0.36 U-S (0.62, 0.38, 0.8) 0.24
k4 D-U (0.01, -0.05, 0.07) 0.06 U-S (-0.5, -0.56, -0.44) 0.06
k5 D-U (0.33, 0.2, 0.45) 0.13 U-S (0.35, 0.24, 0.44) 0.11
k6 D-U (-0.23, -0.3, -0.15) 0.08 U-S (-0.37, -0.44, -0.29) 0.08
k7 D-U (0.21, 0.08, 0.33) 0.13 U-S (0.27, 0.17, 0.37) 0.1
k8 D-U (-0.45, -0.51, -0.38) 0.07 U-S (0.06, -0.01, 0.13) 0.07
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz;d=fitz.open('paper/10.1016-j.cub.2021.02.055.pdf');p=d[8];r=p.rect
clip=fitz.Rect(r.x0+r.width*0.62,r.y0+r.height*0.13,r.x0+r.width*0.85,r.y0+r.height*0.92)
p.get_pixmap(dpi=200,clip=clip).save('$TMPDIR/p9c.png')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9c.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  mkdir -p claims/crcns-rrf-1; grep -n "R2 = 0.48\|Meng\|0.00 for each\|tuning curve peaks\|Single-unit\s*$" paper/10.1016-j.cub.2021.02.055.txt | head; grep -rn "Agent run\|claims-check" docs/archives.md | head -3; grep -n "crcns" docs/archives.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml",
 "content": "# Claims for Moaddab & McDannald (2021), Curr Biol 31:2099-2110, \"Retrorubral field is a hub for\n# diverse threat and aversive outcome signals\", on CRCNS data set rrf-1 (doi:10.6080/K04B2ZJ5).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record with its supplemental information, as supplied under paper/\n# (PyMuPDF text of the journal PDF): Results, Discussion, figure legends, Table 1, STAR Methods,\n# and the supplement (Figures S1 to S6, Tables S1 to S4). The text garbles powers of ten (\"2.80 3\n# 10�11\" is 2.80 x 10^-11, \"5.93E�38\" is 5.93E-38); p-values below are read from them, and the\n# quote checker cannot find these, so they were confirmed by reading. The column layout of Tables\n# S1 to S4 and the Figure 6 panels were read from the PDF pages rendered as images: Table S1 rows\n# are danger vs. uncertainty then uncertainty vs. safety; Table S2 columns are peak threat\n# probability, fear output, then their difference; Table S3 rows are the regressor x bin\n# interaction then the main effect of regressor; Table S4 rows are danger, uncertainty shock,\n# uncertainty omission, safety. The gray boxes of Figure 6 (the analysed outcome interval) span 0\n# to 8 s after shock offset for k1, k3, k5 and k6, and the whole 17.5 s for k2, k4, k7 and k8.\n#\n# Code. The paper says its \"MATLAB code will be uploaded to http://crcns.org/\", which puts it inside\n# the data set, which the reader may not open; the lab page it names for behavior programs\n# (http://mcdannaldlab.org/resources) returned 404 on 2026-11-06. No code was read; every method\n# below is from the STAR Methods, the Results, the figure legends or the supplement.\n#\n# Data the paper used. 11 male Long Evans rats (14 implanted, 3 excluded for placement), 16-wire\n# drivable microelectrode bundles in the retrorubral field (RRF, bregma -6.36 to -7.08). 743 single\n# units over 228 recording sessions; 423 cue-responsive units from 190 sessions. Each session has 16\n# trials: 4 danger (shock p = 1.00), 2 uncertainty shock and 6 uncertainty omission (p = 0.25), and\n# 4 safety (p = 0.00), in random order, mean inter-trial interval 3.5 min. Cues are 10 s; the foot\n# shock (0.5 mA, 0.5 s) starts 2 s after cue offset. Measured variables are spike times and mean\n# waveforms per unit, cue and shock times, and nose pokes (rewarded on VI-60) from which the\n# per-trial suppression ratio is computed (baseline 20 s before cue onset, cue 10 s). The CRCNS data\n# set, by its title and description, holds the 743 sorted units from 228 sessions of the 11 rats,\n# with per-trial firing, nose-poke and suppression-ratio data and waveforms.\n#\n# Shared method (STAR Methods, Z-score normalization). Per unit and trial type, firing rate in 250-ms\n# bins from 20 s before cue onset to 20 s after cue offset (200 bins), averaged over trials; the mean\n# of the 2 s before cue onset of that trial type is subtracted; the result is z-scored across all\n# trial types of the unit. Open, and named where it matters: (z-a) the z-score taken over four trial\n# types (danger, uncertainty shock, uncertainty omission, safety; the Figure 2 heat plot shows four)\n# or (z-b) over three (uncertainty trials pooled, as the cue analyses collapse them). For the cue\n# period uncertainty is the mean over its 8 trials (Methods, Population and single-unit firing\n# analyses; a standard choice where the two subtypes would otherwise be weighted). The outcome period\n# is the 17.5 s after shock offset (12.5 to 30 s after cue onset; Figure 6 legend), the same time on\n# trials without shock.\n#\n# Cluster identity. Claims after kmeans-clusters use the eight clusters k1 to k8. Open is which\n# assignment is used: (c-a) the paper's own cluster labels, where the data set holds them; (c-b) the\n# k-means clusters found here (kmeans-clusters), each matched to the paper's k1 to k8 by its cue\n# firing pattern as described in Results, Diverse cue firing patterns, paragraph 3. Both are run\n# where both exist; outcomes resting on (c-b) alone are marked as resting on that matching.\n#\n# Statistical conventions (STAR Methods). 95% bootstrap CIs are studentized intervals from MATLAB\n# bootci with 1,000 resamples; an effect is observed when the CI excludes zero. ANOVAs report F, p,\n# partial eta squared and observed power (SPSS). The reported effect sizes of Table 1 fit a\n# repeated-measures design with units as subjects and trial type and interval within units (k1,\n# F 4.00 on 110 and 3520 df gives partial eta squared 0.11, as printed), so the per-cluster ANOVAs\n# are run that way; whether a sphericity correction was applied is not stated (uncorrected df are\n# the main reading, Greenhouse-Geisser a variant).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: rrf-1\n  doi: 10.6080/K04B2ZJ5\npaper: doi:10.1016/j.cub.2021.02.055\nclaims:\n- id: units-and-sessions\n  statement: The paper recorded 743 single units from 11 rats over 228 fear discrimination sessions.\n  source: Results, Diverse cue firing patterns, paragraph 1\n  quote: We recorded 743 single units from 11 rats over 228 fear discrimination sessions.\n  expected:\n  - quantity: single units\n    value: 743\n    tolerance: 74\n  - quantity: recording sessions\n    value: 228\n    tolerance: 23\n  - quantity: rats\n    value: 11\n    tolerance: 0\n  criterion: Counts of units, distinct sessions and rats. Reproduced when all three are within\n    tolerance; the rat count must match exactly.\n\n- id: behavior-discrimination\n  statement: In the sessions that yielded cue-responsive units, rats fully discriminated the cues\n    by suppression ratio (danger > uncertainty > safety), with a main effect of cue and 95%\n    bootstrap CIs of every differential suppression ratio excluding zero.\n  source: Results, opening section, paragraph 4; Figure 1B\n  quote: Analysis of variance (ANOVA) for suppression ratio revealed a main effect of cue ... 95%\n    bootstrap CIs for differential suppression ratios did not contain zero for any cue comparison\n  statistics:\n  - about: main effect of cue\n    test: ANOVA\n    statistic: F(2, 20) = 103.57\n    p: 2.80e-11\n    n: 11 rats\n  - about: danger minus uncertainty\n    test: 95% bootstrap CI\n    ci:\n      level: 0.95\n      low: 0.34\n      high: 0.56\n  - about: uncertainty minus safety\n    test: 95% bootstrap CI\n    ci:\n      level: 0.95\n      low: 0.06\n      high: 0.53\n  - about: danger minus safety\n    test: 95% bootstrap CI\n    ci:\n      level: 0.95\n      low: 0.75\n      high: 0.94\n  expected:\n  - quantity: mean differential suppression ratio, danger minus uncertainty\n    value: 0.42\n    tolerance: 0.14\n  - quantity: mean differential suppression ratio, uncertainty minus safety\n    value: 0.40\n    tolerance: 0.34\n  - quantity: mean differential suppression ratio, danger minus safety\n    value: 0.82\n    tolerance: 0.12\n  criterion: Suppression ratio per trial as (baseline poke rate - cue poke rate) / (baseline + cue),\n    baseline the 20 s before cue onset, cue the 10 s cue (STAR Methods, Calculating suppression\n    ratios). Sessions are those with at least one cue-responsive unit (Figure 1B legend; depends on\n    cue-responsive-units), each counted once. Per rat, the mean over those sessions of each cue's\n    mean ratio (uncertainty over its 8 trials); a repeated-measures ANOVA on cue over the 11 rats\n    (the printed df, 2 and 20, fit this). Differences per rat with studentized bootstrap CIs.\n    Tolerances are the distance from the paper's mean to the farther bound of its CI. Open is\n    whether rat values are means over sessions (main reading) or over all pooled trials of those\n    sessions (variant). Reproduced when the cue effect has p < 0.05, all three CIs exclude zero\n    and the three means are within tolerance; partially reproduced when the ANOVA and the order hold\n    but a CI or a mean does not.\n  depends_on:\n  - cue-responsive-units\n\n- id: cue-responsive-units\n  statement: 423 units, from 190 sessions, were cue responsive, with no fewer than 11 per rat.\n  source: Results, Diverse cue firing patterns, paragraphs 1 and 2; Figure S1\n  quote: Four hundred and twenty-three cue-responsive single units were obtained from 190 sessions,\n    and no fewer than 11 single units were identified per rat\n  expected:\n  - quantity: cue-responsive units\n    value: 423\n    tolerance: 42\n  - quantity: sessions with cue-responsive units\n    value: 190\n    tolerance: 19\n  - quantity: fewest cue-responsive units in one rat\n    value: 11\n    tolerance: 1.1\n  criterion: Screen from STAR Methods, Identifying cue-responsive neurons. For each unit and each\n    cue (danger 4 trials, uncertainty 8 trials pooled, safety 4 trials), the raw firing rate in the\n    10 s before cue onset is compared per trial with the mean rate in the first 1 s and in the last\n    5 s of the cue by a paired, two-tailed t test; a unit is cue responsive when any of the six\n    tests has p < 0.05, uncorrected, as the paper states. Reproduced when the three counts are\n    within tolerance. Figure S1 gives per-rat counts (RB01 35, RB03 53, RB04 24, RB06 59, RB07 29,\n    RB09 33, RB10 18, RB11 11, RB12 47, RB13 69, RB14 45), which are reported alongside.\n\n- id: kmeans-elbow\n  statement: In k-means clustering of the 423 cue-responsive units, the mean squared Euclidean\n    distance to the centroid falls as the cluster number rises from 1 to 15, and the decrease\n    diminishes after eight clusters.\n  source: Results, Diverse cue firing patterns, paragraph 2; Figure 1E\n  quote: Euclidean distance from the centroid decreased as cluster number increased, with the\n    amount of decrease diminishing after a cluster number of eight\n  criterion: Matrix of 423 units x 54 epochs of normalized firing (Results; the Methods say \"Firing\n    rate\", so raw rate is a variant), 1-s means of the 250-ms bins; epochs 1-30 the ten 1-s cue\n    intervals for danger, uncertainty and safety, epochs 31-54 six 1-s intervals after shock or\n    omission for danger, uncertainty shock, uncertainty omission and safety (STAR Methods, K-means\n    clustering). MATLAB kmeans defaults (squared Euclidean, k-means++). Open are (e-a) whether the\n    six outcome epochs start at shock onset (12 s after cue onset) or at shock offset (12.5 s, the\n    start of the outcome period in Figure 6), and (e-b) whether \"Clustering was performed 10 times\"\n    means ten replicates per k keeping the best, or ten runs averaged; all four combinations are\n    run. The paper judges the elbow by eye; as a standard choice the claim is reproduced when the\n    curve decreases from k = 1 to 15 and every drop from k to k + 1 for k >= 8 is smaller than the\n    drop from 7 to 8, under the z-a and z-b normalizations alike or one of them.\n  depends_on:\n  - cue-responsive-units\n\n- id: kmeans-clusters\n  statement: Eight k-means clusters were kept, of sizes k1 33, k2 59, k3 18, k4 63, k5 58, k6 61,\n    k7 64 and k8 67.\n  source: Results, Diverse cue firing patterns, paragraph 2; Figure 1F; Figure S2\n  quote: 'All subsequent analyses consider eight clusters: k1, n = 33; k2, n = 59; k3, n = 18; k4,\n    n = 63; k5, n = 58; k6, n = 61; k7, n = 64; and k8, n = 67.'\n  expected:\n  - quantity: k1 size\n    value: 33\n    tolerance: 3.3\n  - quantity: k2 size\n    value: 59\n    tolerance: 5.9\n  - quantity: k3 size\n    value: 18\n    tolerance: 1.8\n  - quantity: k4 size\n    value: 63\n    tolerance: 6.3\n  - quantity: k5 size\n    value: 58\n    tolerance: 5.8\n  - quantity: k6 size\n    value: 61\n    tolerance: 6.1\n  - quantity: k7 size\n    value: 64\n    tolerance: 6.4\n  - quantity: k8 size\n    value: 67\n    tolerance: 6.7\n  criterion: k-means with k = 8 on the matrix of kmeans-elbow, under its readings. Each cluster\n    found is matched to one of the paper's k1 to k8 by its mean danger, uncertainty and safety\n    firing in the intervals of Figure 3A and 3C against the patterns of Results, Diverse cue firing\n    patterns, paragraph 3 (k1 onset danger peak, k3 sustained D > U > S, k5 ramping D > U > S, k7\n    delay D > U > S, k2 uncertainty inhibition, k4 equal danger and uncertainty inhibition, k6\n    danger inhibition with safety excitation, k8 danger inhibition). Reproduced when all eight\n    patterns are found and every size is within tolerance; partially reproduced when all eight\n    patterns are found and at least five sizes are within tolerance. Where the data set holds the\n    paper's labels, their counts and the agreement (adjusted Rand index) between them and the\n    clusters found here are reported.\n  depends_on:\n  - cue-responsive-units\n  - kmeans-elbow\n\n- id: cluster-firing-characteristics\n  statement: Clusters differed in baseline firing rate, coefficient of variance and coefficient of\n    skewness, but not in anterior-posterior location, waveform half-duration or waveform amplitude\n    ratio.\n  source: Results, Diverse cue firing patterns, paragraph 3; Figure 1F; Figure S3\n  quote: found a main effect of cluster for baseline firing rate (F7,415 = 2.48, p = 0.017, hp2 =\n    0.04, op = 0.88), coefficient of variance (F7,415 = 2.28, p = 0.027, hp2 = 0.04, op = 0.84),\n    and coefficient of skewness (F7,415 = 2.65, p = 0.011\n  statistics:\n  - about: baseline firing rate\n    test: multivariate analysis of variance, between-subjects factor cluster\n    statistic: F(7, 415) = 2.48\n    p: 0.017\n  - about: coefficient of variance\n    test: multivariate analysis of variance, between-subjects factor cluster\n    statistic: F(7, 415) = 2.28\n    p: 0.027\n  - about: coefficient of skewness\n    test: multivariate analysis of variance, between-subjects factor cluster\n    statistic: F(7, 415) = 2.65\n    p: 0.011\n  criterion: Measures from STAR Methods, Firing and waveform characteristics. Baseline rate is the\n    mean rate in the 10 s before cue onset; CV is SD/mean and skewness 3 x (mean - median)/SD of the\n    inter-spike intervals in the 20 s before cue onset over the 16 trials; half duration and\n    amplitude ratio from the mean waveform as defined there; anterior-posterior location the\n    recording bregma level. A MANOVA with cluster as between-subjects factor and the six measures,\n    with the univariate tests read for each. Open is whether the inter-spike intervals are pooled\n    over the 16 trials (main reading) or the measure is averaged over trials (variant). Reproduced\n    when baseline rate, CV and skewness have p < 0.05 and location, half duration and amplitude ratio\n    do not; partially reproduced when at least two of the three effects hold and no other measure\n    is significant. Effect sizes are given either way.\n  depends_on:\n  - kmeans-clusters\n\n- id: k1-k3-low-baseline\n  statement: Units of clusters k1 and k3 had lower baseline firing rates than all other clusters.\n  source: Results, Diverse cue firing patterns, paragraph 3; Figure 1F, bottom\n  quote: The single units comprising clusters k1 and k3 had lower baseline firing rates compared to\n    all other clusters (t421 = 3.28, p = 0.001).\n  statistics:\n  - test: independent samples t test\n    statistic: t(421) = 3.28\n    p: 0.001\n    n: 51 k1 and k3 units against 372 others\n  criterion: Baseline rate as in cluster-firing-characteristics; an independent samples t test of\n    k1 and k3 units pooled against all other units. Reproduced when p < 0.05 with k1 and k3 lower.\n  depends_on:\n  - kmeans-clusters\n\n- id: table1-cue-interaction\n  statement: Every cluster showed a significant trial type x interval interaction for cue firing.\n  source: Results, Diverse cue firing patterns, paragraph 4; Table 1 (Cue)\n  quote: found a significant trial type x interval interaction for each cluster (Table 1)\n  statistics:\n  - about: k1\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 4.00\n    p: 5.93e-38\n  - about: k2\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 3.54\n    p: 1.38e-31\n  - about: k3\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 4.91\n    p: 5.57e-49\n  - about: k4\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 7.93\n    p: 2.82e-110\n  - about: k5\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 6.66\n    p: 1.82e-86\n  - about: k6\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 7.34\n    p: 3.75e-99\n  - about: k7\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 4.64\n    p: 2.42e-50\n  - about: k8\n    test: ANOVA, trial type x interval interaction\n    statistic: F = 6.56\n    p: 2.33e-85\n  criterion: Per cluster, normalized firing in 56 250-ms bins (2 s before cue onset, the 10-s cue,\n    the 2-s delay) for danger, uncertainty and safety; a repeated-measures ANOVA with trial type and\n    interval within units (see the header). Reproduced when the interaction has p < 0.05 in all\n    eight clusters; partially reproduced in six or seven.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig3b-excitatory-clusters\n  statement: Clusters k1, k3, k5 and k7 fire more to danger and uncertainty; k1 fires most to danger\n    at cue onset with lower, similar firing to uncertainty and safety; k3 (whole cue and delay), k5\n    (late cue and delay) and k7 (delay) fully differentiate danger > uncertainty > safety.\n  source: Results, Diverse cue firing patterns, paragraph 4; Figure 3A and 3B; Table S1\n  quote: K1 neurons were strongly cue onset responsive, firing maximally to danger but firing at\n    lower and similar levels to uncertainty and safety. K3 neurons sustained differential firing\n    throughout cue presentation and the 2-s delay period ... danger > uncertainty > safety. K5\n    neurons ramped danger and uncertainty firing, fully differentiating the three cues by the last\n    half of cue presentation ... K7 neurons were minimally cue responsive, but showed complete\n    differential cue firing during the 2-s delay period\n  statistics:\n  - about: k1 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.30, high: 0.74}\n  - about: k1 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.11, high: 0.59}\n  - about: k3 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.37, high: 0.95}\n  - about: k3 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.38, high: 0.80}\n  - about: k5 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.20, high: 0.45}\n  - about: k5 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.24, high: 0.44}\n  - about: k7 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.08, high: 0.33}\n  - about: k7 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.17, high: 0.37}\n  expected:\n  - quantity: k1 danger minus uncertainty\n    value: 0.51\n    tolerance: 0.23\n  - quantity: k1 uncertainty minus safety\n    value: 0.25\n    tolerance: 0.36\n  - quantity: k3 danger minus uncertainty\n    value: 0.73\n    tolerance: 0.36\n  - quantity: k3 uncertainty minus safety\n    value: 0.62\n    tolerance: 0.24\n  - quantity: k5 danger minus uncertainty\n    value: 0.33\n    tolerance: 0.13\n  - quantity: k5 uncertainty minus safety\n    value: 0.35\n    tolerance: 0.11\n  - quantity: k7 danger minus uncertainty\n    value: 0.21\n    tolerance: 0.13\n  - quantity: k7 uncertainty minus safety\n    value: 0.27\n    tolerance: 0.10\n  criterion: Per unit, mean normalized firing to each cue in the interval of Figure 3A (k1 first 1\n    s of cue; k3 the 10-s cue plus 2-s delay; k5 last 5 s of cue plus delay; k7 the 2-s delay);\n    per-unit differences danger - uncertainty and uncertainty - safety with studentized bootstrap\n    CIs (Table S1). Tolerances are the distance from the paper's mean to the farther CI bound.\n    Reproduced when every CI agrees with the paper's on whether it excludes zero (and on sign\n    where it does) and every mean is within tolerance; partially reproduced when the CIs agree\n    for at least three of the four clusters.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig3d-inhibitory-clusters\n  statement: Clusters k2, k4, k6 and k8 show sustained inhibition through the cue and delay; k2 is\n    inhibited to uncertainty only, k4 equally to danger and uncertainty, k6 most to danger, less to\n    uncertainty, with excitation to safety, and k8 to danger only.\n  source: Results, Diverse cue firing patterns, paragraph 4; Figure 3C and 3D; Table S1\n  quote: K2 neurons specifically inhibited firing to uncertainty. K4 neurons specifically and\n    equivalently inhibited firing to danger and uncertainty. K6 neurons were maximally inhibited to\n    danger, less strongly inhibited to uncertainty, but showed excitatory firing to safety. K8\n    neurons specifically inhibited firing to danger.\n  statistics:\n  - about: k2 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.20, high: 0.33}\n  - about: k2 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.37, high: -0.23}\n  - about: k4 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.05, high: 0.07}\n  - about: k4 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.56, high: -0.44}\n  - about: k6 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.30, high: -0.15}\n  - about: k6 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.44, high: -0.29}\n  - about: k8 danger minus uncertainty\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.51, high: -0.38}\n  - about: k8 uncertainty minus safety\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.01, high: 0.13}\n  expected:\n  - quantity: k2 danger minus uncertainty\n    value: 0.27\n    tolerance: 0.07\n  - quantity: k2 uncertainty minus safety\n    value: -0.30\n    tolerance: 0.07\n  - quantity: k4 danger minus uncertainty\n    value: 0.01\n    tolerance: 0.06\n  - quantity: k4 uncertainty minus safety\n    value: -0.50\n    tolerance: 0.06\n  - quantity: k6 danger minus uncertainty\n    value: -0.23\n    tolerance: 0.08\n  - quantity: k6 uncertainty minus safety\n    value: -0.37\n    tolerance: 0.08\n  - quantity: k8 danger minus uncertainty\n    value: -0.45\n    tolerance: 0.07\n  - quantity: k8 uncertainty minus safety\n    value: 0.06\n    tolerance: 0.07\n  criterion: As fig3b-excitatory-clusters, over the 10-s cue plus 2-s delay for all four clusters\n    (Figure 3D legend).\n  depends_on:\n  - kmeans-clusters\n\n- id: figs4-onset-and-ramp\n  statement: From cue onset to delay, k1 firing decreases for all three cues (phasic onset firing),\n    k5 firing increases for danger and uncertainty (ramping), and k2 firing increases for danger.\n  source: Figure S4 legend; Results, Diverse cue firing patterns, paragraph 4\n  quote: Danger (M = -1.32 ... uncertainty, (M = -0.95, 95% CI [-1.25, -0.63]), and safety (M =\n    -0.52, 95% CI [-0.73, -0.20]) firing decreases from onset to delay were observed for the\n    phasically responsive k1 neurons. Danger (M = 0.50, 95% CI [0.32, 0.66]) and uncertainty (M =\n    0.23, 95% CI [0.11, 0.35]) firing increases from onset to delay were observed for the ramping k5\n    neurons. A danger (M = 0.18, 95% CI [0.06, 0.31]) firing increase\n  statistics:\n  - about: k1 danger, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -1.62, high: -0.97}\n  - about: k1 uncertainty, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -1.25, high: -0.63}\n  - about: k1 safety, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: -0.73, high: -0.20}\n  - about: k5 danger, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.32, high: 0.66}\n  - about: k5 uncertainty, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.11, high: 0.35}\n  - about: k2 danger, delay minus onset\n    test: 95% bootstrap CI\n    ci: {level: 0.95, low: 0.06, high: 0.31}\n  expected:\n  - quantity: k1 danger, delay minus onset\n    value: -1.32\n    tolerance: 0.35\n  - quantity: k1 uncertainty, delay minus onset\n    value: -0.95\n    tolerance: 0.32\n  - quantity: k1 safety, delay minus onset\n    value: -0.52\n    tolerance: 0.32\n  - quantity: k5 danger, delay minus onset\n    value: 0.50\n    tolerance: 0.18\n  - quantity: k5 uncertainty, delay minus onset\n    value: 0.23\n    tolerance: 0.12\n  - quantity: k2 danger, delay minus onset\n    value: 0.18\n    tolerance: 0.13\n  criterion: Per unit and cue, mean normalized firing in the 2-s delay minus that in the first 1 s\n    of the cue; studentized bootstrap CI per cluster and cue. The k1 danger CI prints as \"[1-.62,\n    -0.97]\", read as [-1.62, -0.97]. Tolerances are the distance from the mean to the farther bound.\n    Reproduced when the six CIs exclude zero with the paper's sign and the means are within\n    tolerance; partially reproduced when the k1 and k5 CIs hold but a mean or the k2 CI does not.\n    The CIs of the other cues and clusters, which the paper shows as including zero, are reported.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig4abc-threat-bias\n  statement: Except for k2, each cluster's uncertainty firing has the direction and time course of\n    its danger firing at lower magnitude, and safety firing tends to oppose danger firing; k4 and\n    k6 are inhibited to danger but excited to safety, k3 and k5 the reverse.\n  source: Results, Uniform firing bias toward threat cues, paragraph 1; Figure 4A to 4C; Figure S5\n  quote: With the exception of cluster k2, the direction and temporal characteristics of each\n    cluster's uncertainty firing were similar to that for danger, only diminished in magnitude.\n    Critically, across all eight clusters, safety firing direction tended to oppose danger firing\n    direction. Clusters k4 and k6 showed considerable firing inhibition to danger, but firing\n    increases to safety. Just the opposite was observed for clusters k3 and k5\n  criterion: The paper shows this in mean traces (Figure 4A to 4C) and per-period bars (Figure S5,\n    onset first 1 s, late cue last 5 s, delay 2 s), with no test. Judged on each cluster's mean\n    normalized firing in the Figure 3A and 3C interval (the paper's per-cluster periods). Reproduced\n    when (1) for k4 and k6 danger mean < 0 and safety mean > 0, and for k3 and k5 danger mean > 0\n    and safety mean < 0; and (2) in at least six of the seven clusters other than k2, the\n    uncertainty mean has the sign of the danger mean and a smaller absolute value. Partially\n    reproduced when (1) holds and (2) holds in four or five. The onset, late cue and delay means of\n    every cluster are reported (Figure S5).\n  depends_on:\n  - kmeans-clusters\n\n- id: fig4def-danger-uncertainty-correlation\n  statement: Across all cue-responsive units, danger and uncertainty firing are positively related at\n    cue onset (R2 = 0.48), late cue (R2 = 0.21) and delay (R2 = 0.21).\n  source: Results, Uniform firing bias toward threat cues, paragraph 2; Figure 4D to 4F\n  quote: there was a positive relationship between danger and uncertainty firing across all\n    clusters during each period\n  statistics:\n  - about: onset\n    test: Pearson correlation\n    statistic: R2 = 0.48\n    p: 3.25e-62\n    n: 423 units\n  - about: late cue\n    test: Pearson correlation\n    statistic: R2 = 0.21\n    p: 8.23e-24\n    n: 423 units\n  - about: delay\n    test: Pearson correlation\n    statistic: R2 = 0.21\n    p: 2.46e-23\n    n: 423 units\n  expected:\n  - quantity: R2 onset\n    value: 0.48\n    tolerance: 0.048\n  - quantity: R2 late cue\n    value: 0.21\n    tolerance: 0.021\n  - quantity: R2 delay\n    value: 0.21\n    tolerance: 0.021\n  criterion: Per unit, mean normalized firing to danger and to uncertainty in the first 1 s of the\n    cue, the last 5 s, and the 2 s after cue offset (Figure 4 legend); Pearson correlation over the\n    423 units. Reproduced when all three correlations are positive with p < 0.05 and R2 within\n    tolerance under z-a or z-b; partially reproduced when all three are positive and significant\n    but an R2 is outside tolerance.\n  depends_on:\n  - cue-responsive-units\n\n- id: fig4ghi-danger-safety-correlation\n  statement: Danger and safety firing are positively related at cue onset (R2 = 0.14) but negatively\n    related in the late cue (R2 = 0.03) and delay (R2 = 0.02).\n  source: Results, Uniform firing bias toward threat cues, paragraph 2; Figure 4G to 4I\n  quote: There was a positive relationship between danger and safety firing at cue onset (R2 =\n    0.14 ... but negative relationships were observed during late cue (R2 = 0.03 ... and delay (R2 =\n    0.02, p = 0.008)\n  statistics:\n  - about: onset\n    test: Pearson correlation\n    statistic: R2 = 0.14\n    p: 7.98e-16\n    n: 423 units\n  - about: late cue\n    test: Pearson correlation\n    statistic: R2 = 0.03\n    p: 1.48e-4\n    n: 423 units\n  - about: delay\n    test: Pearson correlation\n    statistic: R2 = 0.02\n    p: 0.008\n    n: 423 units\n  expected:\n  - quantity: R2 onset\n    value: 0.14\n    tolerance: 0.014\n  - quantity: R2 late cue\n    value: 0.03\n    tolerance: 0.005\n  - quantity: R2 delay\n    value: 0.02\n    tolerance: 0.005\n  criterion: As fig4def-danger-uncertainty-correlation with safety in place of uncertainty. The\n    late cue and delay R2 are printed to two decimals, so their tolerance is the rounding half-step\n    (0.005), wider than 10%. Reproduced when the onset correlation is positive, the late cue and\n    delay correlations negative, all with p < 0.05, and the R2 within tolerance; partially\n    reproduced when the signs and significance hold but an R2 does not.\n  depends_on:\n  - cue-responsive-units\n\n- id: fig4-correlations-differ\n  statement: The danger-uncertainty and danger-safety correlations differ from one another in each\n    period (Z = 7.69 onset, 8.94 late cue, 8.20 delay).\n  source: Results, Uniform firing bias toward threat cues, paragraph 2; Figure 4 legend\n  quote: 'Fisher r-to-z transformation revealed the danger-uncertainty and danger-safety\n    relationships differed from one another during each period: onset (Z = 7.69), late cue (Z =\n    8.94), and delay (Z = 8.20)'\n  statistics:\n  - about: onset\n    test: Fisher r-to-z transformation, Meng's Z-test for correlated correlation coefficients\n    statistic: Z = 7.69\n    p: 0\n  - about: late cue\n    test: Fisher r-to-z transformation, Meng's Z-test for correlated correlation coefficients\n    statistic: Z = 8.94\n    p: 0\n  - about: delay\n    test: Fisher r-to-z transformation, Meng's Z-test for correlated correlation coefficients\n    statistic: Z = 8.20\n    p: 0\n  expected:\n  - quantity: Z onset\n    value: 7.69\n    tolerance: 0.77\n  - quantity: Z late cue\n    value: 8.94\n    tolerance: 0.89\n  - quantity: Z delay\n    value: 8.20\n    tolerance: 0.82\n  criterion: Meng, Rosenthal and Rubin's Z-test for two correlations sharing danger firing, using the\n    uncertainty-safety correlation of the same units (STAR Methods; the MATLAB File Exchange routine\n    the paper names). The test returned 0.00 for p, recorded as 0. Reproduced when each Z is within\n    tolerance with p < 0.05; partially reproduced when all three are significant but a Z is outside\n    tolerance.\n  depends_on:\n  - fig4def-danger-uncertainty-correlation\n  - fig4ghi-danger-safety-correlation\n\n- id: fig5a-tuning-peaks-exaggerated\n  statement: Threat tuning curves of k1, k3 and k5 peak at an uncertainty assignment of 0.375 and k7\n    at 0.500, above the actual shock probability of 0.250 (exaggerated threat probability\n    signaling).\n  source: Results, Exaggerated threat probability signaling, paragraphs 1 and 2; Figure 5A and 5B\n  quote: 'In support, tuning curve peaks exceeded 0.250: k1, k3, and k5 = 0.375 and k7 = 0.500.'\n  expected:\n  - quantity: k1 peak assignment\n    value: 0.375\n    tolerance: 0\n  - quantity: k3 peak assignment\n    value: 0.375\n    tolerance: 0\n  - quantity: k5 peak assignment\n    value: 0.375\n    tolerance: 0\n  - quantity: k7 peak assignment\n    value: 0.5\n    tolerance: 0\n  criterion: Per unit, a regression (MATLAB regress, with a constant) of each trial's normalized\n    firing on the trial's suppression ratio (fear output) and the cue's threat probability (danger\n    1, safety 0, uncertainty set in turn to 0, 0.125 ... 1), over the 16 trials of the unit's\n    session, run in each 1-s bin (STAR Methods, Single-unit linear regression and Threat probability\n    tuning curve; the Methods print 0.025 for 0.375, a typo). The tuning curve is the cluster mean of\n    the threat probability beta per assignment; the peak is the assignment of largest mean. Open\n    are (t-a) which bins are averaged, the 10 cue bins (Methods) or the cluster-specific periods of\n    Figure 3A and 3C (Results), which for k3, k5 and k7 include the 2-s delay; and (t-b) how a\n    single trial's firing is normalized, either the trial's baseline-subtracted rate z-scored with\n    the unit's mean and SD from the shared normalization, or the trial rates z-scored across the\n    unit's 16 trials. All four combinations are run. The grid step (0.125) is larger than 10%, so\n    each peak must match exactly. Reproduced when, under one reading, all four peaks match;\n    partially reproduced when all four exceed 0.250 but not all match.\n  data: dataset\n  depends_on:\n  - kmeans-clusters\n\n- id: fig5a-tuning-peaks-inhibited\n  statement: Among the cue-inhibited clusters, k4 (peak 0.875) and k6 (0.625) show even greater\n    exaggeration of threat probability, while k8 peaks at the actual probability, 0.250, flattening\n    toward 0.000.\n  source: Results, Exaggerated threat probability signaling, paragraph 2; Figure 5A\n  quote: 'Tuning curve peaks for each cluster were k4 = 0.875 and k6 = 0.625, now exceeding even fear\n    output. K8 neurons were more tuned to the actual shock probability, with a peak of 0.250 that\n    flattened toward 0.000.'\n  expected:\n  - quantity: k4 peak assignment\n    value: 0.875\n    tolerance: 0\n  - quantity: k6 peak assignment\n    value: 0.625\n    tolerance: 0\n  - quantity: k8 peak assignment\n    value: 0.25\n    tolerance: 0\n  criterion: As fig5a-tuning-peaks-exaggerated, with the betas of k4, k6 and k8 multiplied by -1\n    (Results). Reproduced when, under one reading, all three peaks match; partially reproduced when\n    k4 and k6 peaks exceed 0.375 and k8 peaks at 0.375 or below.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig5a-tuning-anova\n  statement: The tuning curves differ between clusters (main effect of cluster and cluster x\n    assignment interaction) and show a main effect of assignment.\n  source: Results, Exaggerated threat probability signaling, paragraph 2; Figure 5A\n  quote: ANOVA (factors cluster [7] and assignment [9]) revealed a main effect of cluster\n  inferred: The quote drops the colon the paper prints after \"factors\"; the sentence goes on to give\n    the interaction and the next sentence the main effect of assignment, with the values recorded\n    under statistics.\n  statistics:\n  - about: main effect of cluster\n    test: ANOVA\n    statistic: F(6, 357) = 4.14\n    p: 0.0005\n  - about: cluster x assignment interaction\n    test: ANOVA\n    statistic: F(48, 2856) = 7.22\n    p: 1.16e-43\n  - about: main effect of assignment\n    test: ANOVA\n    statistic: F(8, 2856) = 24.84\n    p: 2.67e-37\n  criterion: Per-unit mean threat probability betas (sign-inverted for k4, k6, k8) at the nine\n    assignments, from fig5a-tuning-peaks-exaggerated under its readings; ANOVA with assignment\n    within units and cluster between (the printed df, 357 = 364 units - 7, fit this). Reproduced\n    when all three effects have p < 0.05 under one reading.\n  depends_on:\n  - fig5a-tuning-peaks-exaggerated\n  - fig5a-tuning-peaks-inhibited\n\n- id: fig5e-peak-probability-over-fear-output\n  statement: With peak threat probability and fear output as regressors, neither is signaled before\n    the cue; peak threat probability is signaled from cue onset through the delay, fear output in\n    every bin but the first 1 s of the cue, and peak threat probability signaling exceeds fear\n    output signaling in every cue and delay bin.\n  source: Results, Exaggerated threat probability signaling, paragraph 3; Figure 5C to 5E; Table S2\n  quote: Neither peak threat probability nor fear output signaling was observed prior to cue onset.\n    Across all seven clusters (Figure 5E), peak threat probability was continuously signaled from\n    cue onset through delay. Fear output was signaled in all bins except for the first 1 s of the\n    cue; however, peak threat probability signaling exceeded fear output signaling at each time\n    point.\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA, within factor regressor, between factors cluster and bin\n    statistic: F(1, 355) = 28.57\n    p: 1.62e-7\n  - about: regressor x bin interaction\n    test: ANOVA\n    statistic: F(13, 4615) = 4.13\n    p: 7.40e-7\n  expected:\n  - quantity: peak threat probability beta, pre1\n    value: 0.02\n    tolerance: 0.05\n  - quantity: peak threat probability beta, pre2\n    value: -0.02\n    tolerance: 0.05\n  - quantity: peak threat probability beta, cue1\n    value: 0.46\n    tolerance: 0.12\n  - quantity: peak threat probability beta, cue2\n    value: 0.45\n    tolerance: 0.1\n  - quantity: peak threat probability beta, cue3\n    value: 0.43\n    tolerance: 0.1\n  - quantity: peak threat probability beta, cue4\n    value: 0.38\n    tolerance: 0.09\n  - quantity: peak threat probability beta, cue5\n    value: 0.46\n    tolerance: 0.09\n  - quantity: peak threat probability beta, cue6\n    value: 0.5\n    tolerance: 0.11\n  - quantity: peak threat probability beta, cue7\n    value: 0.56\n    tolerance: 0.11\n  - quantity: peak threat probability beta, cue8\n    value: 0.55\n    tolerance: 0.11\n  - quantity: peak threat probability beta, cue9\n    value: 0.55\n    tolerance: 0.11\n  - quantity: peak threat probability beta, cue10\n    value: 0.52\n    tolerance: 0.1\n  - quantity: peak threat probability beta, delay1\n    value: 0.44\n    tolerance: 0.1\n  - quantity: peak threat probability beta, delay2\n    value: 0.49\n    tolerance: 0.1\n  - quantity: fear output beta, pre1\n    value: -0.01\n    tolerance: 0.04\n  - quantity: fear output beta, pre2\n    value: 0.01\n    tolerance: 0.04\n  - quantity: fear output beta, cue1\n    value: 0.06\n    tolerance: 0.08\n  - quantity: fear output beta, cue2\n    value: 0.12\n    tolerance: 0.09\n  - quantity: fear output beta, cue3\n    value: 0.14\n    tolerance: 0.08\n  - quantity: fear output beta, cue4\n    value: 0.18\n    tolerance: 0.09\n  - quantity: fear output beta, cue5\n    value: 0.18\n    tolerance: 0.08\n  - quantity: fear output beta, cue6\n    value: 0.17\n    tolerance: 0.09\n  - quantity: fear output beta, cue7\n    value: 0.1\n    tolerance: 0.09\n  - quantity: fear output beta, cue8\n    value: 0.13\n    tolerance: 0.12\n  - quantity: fear output beta, cue9\n    value: 0.2\n    tolerance: 0.09\n  - quantity: fear output beta, cue10\n    value: 0.16\n    tolerance: 0.1\n  - quantity: fear output beta, delay1\n    value: 0.17\n    tolerance: 0.09\n  - quantity: fear output beta, delay2\n    value: 0.14\n    tolerance: 0.1\n  criterion: Per unit of the seven clusters, the regression of fear-output and threat-probability\n    regressors with uncertainty set to the cluster's peak (k1, k3, k5 0.375; k4 0.875; k6 0.625;\n    k7 0.500; k8 0.250, as the paper reports them; the peaks found here are a variant) in 14 1-s\n    bins from 2 s before cue onset through the 2-s delay. Means and studentized bootstrap CIs per\n    bin of each beta and of their difference (Table S2; tolerances are the distance to the farther\n    bound). Open are the trial normalization (t-b of fig5a-tuning-peaks-exaggerated) and (s-a)\n    whether the betas of k4, k6 and k8 are sign-inverted here as for the tuning curves (Figure 5E\n    shows positive values) or left as computed; all readings are run. The ANOVA has regressor\n    within units; the Results name bin a between factor, but the printed df (13 and 4615 = 13 x\n    355) fit bin within units, which is the main reading; 355 error df imply 362 units, not 364,\n    and the units dropped are to be reported. Reproduced when, under one reading, the CI pattern\n    matches (both betas include zero in pre1 and pre2; peak probability excludes zero in all 12 cue\n    and delay bins; fear output excludes zero in all but cue1; the difference excludes zero, peak\n    probability larger, in all 12), the regressor main effect and regressor x bin interaction have\n    p < 0.05, and at least 24 of the 28 means are within tolerance. Partially reproduced when the\n    regressor main effect holds and peak probability exceeds fear output in at least 9 of the 12\n    bins.\n  depends_on:\n  - fig5a-tuning-peaks-exaggerated\n  - fig5a-tuning-peaks-inhibited\n\n- id: fig5-regressor-cluster\n  statement: Signaling varied somewhat between clusters (regressor x cluster interaction) with no\n    regressor x cluster x bin interaction.\n  source: Results, Exaggerated threat probability signaling, paragraph 3; Figure S6; Table S3\n  quote: ANOVA revealed a regressor x cluster interaction (F6,355 = 2.15, p = 0.048, hp2 = 0.04,\n    op = 0.76) but no regressor x cluster x bin interaction (F78,4615 = 1.06, p = 0.33\n  statistics:\n  - about: regressor x cluster interaction\n    test: ANOVA\n    statistic: F(6, 355) = 2.15\n    p: 0.048\n  - about: regressor x cluster x bin interaction\n    test: ANOVA\n    statistic: F(78, 4615) = 1.06\n    p: 0.33\n  criterion: The ANOVA of fig5e-peak-probability-over-fear-output under its readings. The two-way\n    term is a presence and the three-way an absence, judged on this ANOVA at p < 0.05. Reproduced\n    when the regressor x cluster interaction has p < 0.05 and the three-way interaction does not;\n    partially reproduced when only the absence holds. Both effect sizes are reported.\n  depends_on:\n  - fig5e-peak-probability-over-fear-output\n\n- id: table-s3-cluster-regression\n  statement: Within clusters, peak threat probability exceeds fear output (main effect of regressor)\n    in k3, k4, k6, k7 and k8 but not in k1 or k5, and only k7 shows a regressor x bin interaction.\n  source: Table S3; Figure S6\n  inferred: Read from Table S3, whose significant p-values are printed in bold (layout checked on\n    the rendered page); no sentence of the text states the per-cluster results.\n  statistics:\n  - about: k1 main effect of regressor\n    test: ANOVA\n    statistic: F = 0.44\n    p: 0.51\n  - about: k3 main effect of regressor\n    test: ANOVA\n    statistic: F = 9.35\n    p: 0.008\n  - about: k4 main effect of regressor\n    test: ANOVA\n    statistic: F = 6.72\n    p: 0.01\n  - about: k5 main effect of regressor\n    test: ANOVA\n    statistic: F = 2.02\n    p: 0.16\n  - about: k6 main effect of regressor\n    test: ANOVA\n    statistic: F = 6.28\n    p: 0.015\n  - about: k7 main effect of regressor\n    test: ANOVA\n    statistic: F = 16.89\n    p: 1.16e-4\n  - about: k8 main effect of regressor\n    test: ANOVA\n    statistic: F = 4.29\n    p: 0.04\n  - about: k7 regressor x bin interaction\n    test: ANOVA\n    statistic: F = 3.01\n    p: 2.39e-4\n  criterion: Per cluster, the ANOVA of fig5e-peak-probability-over-fear-output without the cluster\n    factor (regressor and bin within units). The other regressor x bin interactions are printed\n    as non-significant (k1 0.07, k3 0.09, k4 0.48, k5 0.79, k6 0.08, k8 0.27). Reproduced when the\n    regressor main effect is significant (p < 0.05) in exactly the five clusters named, with peak\n    probability larger, and the interaction in k7 only; partially reproduced when at least five of\n    the seven clusters agree on both terms.\n  depends_on:\n  - fig5e-peak-probability-over-fear-output\n\n- id: fig5f-fear-output-vs-peak-probability\n  statement: Across units there is a continuous negative relationship between fear output and peak\n    threat probability betas (R2 = 0.43), with signaling biased toward peak threat probability, so\n    the two are not signaled by distinct populations.\n  source: Results, Exaggerated threat probability signaling, paragraph 3; Figure 5F; Figure S6C to\n    S6U\n  quote: and fear output were not discretely signaled by distinct RRF populations. A continuous,\n    negative relationship (R2 = 0.43\n  statistics:\n  - test: Pearson correlation\n    statistic: R2 = 0.43\n    p: 4.18e-46\n  expected:\n  - quantity: R2, fear output beta against peak threat probability beta\n    value: 0.43\n    tolerance: 0.043\n  criterion: Per unit of the seven clusters, the mean of each beta from\n    fig5e-peak-probability-over-fear-output; Pearson correlation across units. Open is which bins\n    are averaged, (f-a) the 10 cue bins (Figure S6B, \"during 10-s cue interval\") or (f-b) all 14\n    bins, together with that claim's readings. Reproduced when, under one reading, r < 0, p < 0.05\n    and R2 within tolerance; partially reproduced when r < 0 with p < 0.05 only. The per-cluster\n    R2 printed in Figure S6 (0.64, 0.46, 0.55, 0.65, 0.55, 0.58, 0.64 in panel order k1, k3, k4,\n    k5, k6, k7, k8) are reported against those found here.\n  depends_on:\n  - fig5e-peak-probability-over-fear-output\n\n- id: table1-outcome-anova\n  statement: Every cluster showed differential firing after shock delivery or omission, a main\n    effect of trial type and/or a trial type x interval interaction.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 1; Table 1 (Aversive outcome)\n  quote: found a main effect of trial type and/ or a trial type x interval interaction for every\n    cluster (Table 1)\n  statistics:\n  - {about: k1 interaction, test: ANOVA, statistic: F = 1.23, p: 0.02}\n  - {about: k2 interaction, test: ANOVA, statistic: F = 2.13, p: 2.21e-18}\n  - {about: k3 interaction, test: ANOVA, statistic: F = 1.20, p: 0.03}\n  - {about: k4 interaction, test: ANOVA, statistic: F = 1.83, p: 5.86e-12}\n  - {about: k5 interaction, test: ANOVA, statistic: F = 2.62, p: 6.98e-31}\n  - {about: k6 interaction, test: ANOVA, statistic: F = 1.11, p: 0.14}\n  - {about: k7 interaction, test: ANOVA, statistic: F = 3.83, p: 1.32e-66}\n  - {about: k8 interaction, test: ANOVA, statistic: F = 2.18, p: 1.09e-19}\n  - {about: k1 main effect of trial type, test: ANOVA, statistic: F = 2.92, p: 0.04}\n  - {about: k2 main effect of trial type, test: ANOVA, statistic: F = 56.62, p: 1.37e-25}\n  - {about: k3 main effect of trial type, test: ANOVA, statistic: F = 2.12, p: 0.11}\n  - {about: k4 main effect of trial type, test: ANOVA, statistic: F = 46.62, p: 1.97e-22}\n  - {about: k5 main effect of trial type, test: ANOVA, statistic: F = 3.90, p: 0.01}\n  - {about: k6 main effect of trial type, test: ANOVA, statistic: F = 48.82, p: 3.88e-23}\n  - {about: k7 main effect of trial type, test: ANOVA, statistic: F = 95.16, p: 2.31e-37}\n  - {about: k8 main effect of trial type, test: ANOVA, statistic: F = 47.25, p: 4.47e-23}\n  criterion: Per cluster, normalized firing in 70 250-ms bins over the 17.5 s after shock offset\n    for danger, uncertainty shock, uncertainty omission and safety; repeated-measures ANOVA with\n    trial type and interval within units (header). Reproduced when every cluster has at least one of\n    the two effects at p < 0.05 and the pattern of significance matches Table 1 (both effects in\n    all but k3, interaction only, and k6, main effect only) in at least 14 of the 16 tests;\n    partially reproduced when every cluster has an effect but fewer tests match.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6a-k1-shock\n  statement: k1 units are generally shock responsive, with equivalent, transient firing after\n    danger and uncertainty shock.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6A; Table S4\n  quote: K1 neurons (Figure 6A, i and ii) were generally shock responsive, showing equivalent and\n    transient responding following danger and uncertainty shock.\n  expected:\n  - quantity: k1 danger, mean normalized firing\n    value: 0.19\n    tolerance: 0.18\n  - quantity: k1 uncertainty shock, mean normalized firing\n    value: 0.2\n    tolerance: 0.17\n  - quantity: k1 uncertainty omission, mean normalized firing\n    value: -0.02\n    tolerance: 0.12\n  - quantity: k1 safety, mean normalized firing\n    value: 0.15\n    tolerance: 0.1\n  criterion: The shared outcome method for Figure 6. Per unit, mean normalized firing per trial type\n    in the gray-box interval of Figure 6 (k1, 0 to 8 s after shock offset, read from the figure);\n    per-cluster studentized bootstrap CIs of each trial type (Table S4) and of the per-unit\n    differences uncertainty shock - danger, uncertainty omission - safety and danger - safety\n    (Figure 6, column ii). Tolerances are the distance from the Table S4 mean to its farther bound.\n    The paper's pattern for k1 is danger and uncertainty shock CIs above zero, uncertainty omission\n    including zero, safety above zero, and of the differences only omission - safety below zero.\n    Reproduced when all seven CIs agree with the paper's on excluding zero and sign, and the four\n    means are within tolerance; partially reproduced when the shock - danger difference includes\n    zero and both shock CIs are above zero.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6b-k2-anti-ppe\n  statement: k2 units fire most to the predicted shock on danger trials and are inhibited by the\n    surprising shock on uncertainty trials, an anti-positive prediction error signal.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6B; Table S4\n  quote: K2 neurons (Figure 6B, i and ii) fired maximally to the fully predicted shock on danger\n    trials but showed firing inhibition to the surprising shock on uncertainty trials, consistent\n    with an anti-positive prediction error signal.\n  expected:\n  - quantity: k2 danger, mean normalized firing\n    value: 0.33\n    tolerance: 0.05\n  - quantity: k2 uncertainty shock, mean normalized firing\n    value: -0.18\n    tolerance: 0.07\n  - quantity: k2 uncertainty omission, mean normalized firing\n    value: -0.05\n    tolerance: 0.053\n  - quantity: k2 safety, mean normalized firing\n    value: 0.06\n    tolerance: 0.05\n  criterion: As fig6a-k1-shock over the whole 17.5 s (gray box of Figure 6B). Paper's pattern is\n    danger above zero, uncertainty shock below, omission including zero, safety above; shock -\n    danger and omission - safety below zero, danger - safety above. Reproduced when all seven CIs\n    agree and the means are within tolerance; partially reproduced when danger is above zero,\n    uncertainty shock below zero and shock - danger below zero.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6c-k3-continued-threat\n  statement: k3 units sharply reduce firing after shock but sustain excitation after omission on\n    uncertainty trials, a continued threat signal.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6C; Table S4\n  quote: K3neurons(Figure 6C, i and ii) sharply reduced firing following shock but sustained\n    excitation of firing following omission on uncertainty trials, revealing a continued threat\n    signal.\n  expected:\n  - quantity: k3 danger, mean normalized firing\n    value: 0.07\n    tolerance: 0.27\n  - quantity: k3 uncertainty shock, mean normalized firing\n    value: -0.03\n    tolerance: 0.21\n  - quantity: k3 uncertainty omission, mean normalized firing\n    value: 0.2\n    tolerance: 0.23\n  - quantity: k3 safety, mean normalized firing\n    value: -0.18\n    tolerance: 0.11\n  criterion: As fig6a-k1-shock over 0 to 8 s after shock offset. Paper's pattern is danger,\n    uncertainty shock and uncertainty omission including zero (the omission CI just does, [-0.02,\n    0.43]), safety below zero; only omission - safety above zero. Reproduced when the seven CIs\n    agree and the means are within tolerance, or when they differ only in the omission CI\n    excluding zero above (the Results call it sustained excitation); partially reproduced when\n    omission - safety is above zero and both shock CIs include zero.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6de-k4-k5-persistent-threat\n  statement: k4 units sustain inhibition and k5 units sustain excitation on uncertainty omission\n    trials, persistent threat signaling through opposite firing directions.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6D and 6E; Table S4\n  quote: K4 neurons (Figure 6D, i and ii) sustained firing inhibition on uncertainty omission\n    trials, whereas k5 neurons (Figure 6E, i and ii) sustained firing increases, revealing similar\n    and persistent threat signaling through opposing firing directions.\n  expected:\n  - quantity: k4 danger, mean normalized firing\n    value: 0.19\n    tolerance: 0.06\n  - quantity: k4 uncertainty shock, mean normalized firing\n    value: 0.25\n    tolerance: 0.06\n  - quantity: k4 uncertainty omission, mean normalized firing\n    value: -0.16\n    tolerance: 0.04\n  - quantity: k4 safety, mean normalized firing\n    value: 0.2\n    tolerance: 0.05\n  - quantity: k5 danger, mean normalized firing\n    value: 0.04\n    tolerance: 0.11\n  - quantity: k5 uncertainty shock, mean normalized firing\n    value: -0.05\n    tolerance: 0.11\n  - quantity: k5 uncertainty omission, mean normalized firing\n    value: 0.25\n    tolerance: 0.08\n  - quantity: k5 safety, mean normalized firing\n    value: -0.07\n    tolerance: 0.067\n  criterion: As fig6a-k1-shock, k4 over the whole 17.5 s and k5 over 0 to 8 s after shock offset.\n    Paper's pattern is k4 danger, shock and safety above zero, omission below, of the differences\n    only omission - safety below zero; k5 danger and shock including zero, omission above, safety\n    below, of the differences only omission - safety above zero. Reproduced when all CIs of both\n    clusters agree and the means are within tolerance; partially reproduced when the omission\n    CI and omission - safety have the paper's sign in both clusters.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6f-k6-ppe-then-valence\n  statement: k6 units show early positive prediction error through firing decreases (more inhibition\n    after uncertainty shock than danger shock), giving way to a sustained valence signal with most\n    firing to safety, little after omission and sustained inhibition after danger and uncertainty\n    shock.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6F; Table S4\n  quote: 'K6 neurons (Figure 6F, i and ii) showed early positive prediction error signaling through\n    firing decreases: greater firing inhibition following shock delivery on uncertainty trials\n    compared to danger trials.'\n  expected:\n  - quantity: k6 danger, mean normalized firing\n    value: -0.17\n    tolerance: 0.09\n  - quantity: k6 uncertainty shock, mean normalized firing\n    value: -0.32\n    tolerance: 0.1\n  - quantity: k6 uncertainty omission, mean normalized firing\n    value: 0.02\n    tolerance: 0.07\n  - quantity: k6 safety, mean normalized firing\n    value: 0.26\n    tolerance: 0.07\n  criterion: As fig6a-k1-shock over 0 to 8 s after shock offset. Paper's pattern is danger and\n    shock below zero, omission including zero, safety above; all three differences below zero. The\n    early-to-late change is shown in the traces only; the 0-8 s window is judged and the means of\n    the full 17.5 s are reported. Reproduced when the seven CIs agree and the means are within\n    tolerance; partially reproduced when shock - danger is below zero and safety is the largest\n    mean.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6g-k7-valence-then-ppe\n  statement: k7 units show initial valence signaling (danger shock = uncertainty shock > omission >\n    safety) giving way to positive prediction error (uncertainty shock > danger shock), and sustain\n    inhibition to safety through the outcome period.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6G; Table S4\n  quote: K7 neurons (Figure 6G, i and ii) showedinitial valence signaling ... that gave way to\n    positive prediction error (uncertainty shock > danger shock). Impressively, k7 neurons\n    sustained firing inhibition to safety throughout the outcome period.\n  expected:\n  - quantity: k7 danger, mean normalized firing\n    value: 0.29\n    tolerance: 0.06\n  - quantity: k7 uncertainty shock, mean normalized firing\n    value: 0.42\n    tolerance: 0.08\n  - quantity: k7 uncertainty omission, mean normalized firing\n    value: 0.08\n    tolerance: 0.05\n  - quantity: k7 safety, mean normalized firing\n    value: -0.28\n    tolerance: 0.06\n  criterion: As fig6a-k1-shock over the whole 17.5 s. Paper's pattern is danger, shock and omission\n    above zero, safety below; all three differences above zero. Reproduced when the seven CIs agree\n    and the means are within tolerance; partially reproduced when shock - danger is above zero and\n    safety is below zero.\n  depends_on:\n  - kmeans-clusters\n\n- id: fig6h-k8-ppe-then-unsigned\n  statement: k8 units show early positive prediction error (uncertainty shock > danger shock) giving\n    way to an unsigned prediction error, with equal firing increases on uncertainty shock and\n    omission trials exceeding those for danger and safety.\n  source: Results, Diverse aversive outcome firing patterns, paragraph 2; Figure 6H; Table S4\n  quote: Finally, k8 neurons (Figure 6H, i and ii) showed early positive prediction error signaling\n    (uncertainty shock > danger shock) that gavewaytoanunsignedpredictionerrorsignalinwhich\n    equivalent firing increases on uncertainty shock and omissiontrials exceeded those for danger\n    and safety.\n  expected:\n  - quantity: k8 danger, mean normalized firing\n    value: -0.11\n    tolerance: 0.06\n  - quantity: k8 uncertainty shock, mean normalized firing\n    value: 0.32\n    tolerance: 0.07\n  - quantity: k8 uncertainty omission, mean normalized firing\n    value: 0.18\n    tolerance: 0.04\n  - quantity: k8 safety, mean normalized firing\n    value: -0.02\n    tolerance: 0.04\n  criterion: As fig6a-k1-shock over the whole 17.5 s. Paper's pattern is danger below zero, shock\n    and omission above, safety including zero; shock - danger and omission - safety above zero,\n    danger - safety below. Reproduced when the seven CIs agree and the means are within tolerance;\n    partially reproduced when shock - danger and omission - safety are above zero.\n  depends_on:\n  - kmeans-clusters\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml",
 "old_string": "  quote: ANOVA (factors cluster [7] and assignment [9]) revealed a main effect of cluster\n  inferred: The quote drops the colon the paper prints after \"factors\"; the sentence goes on to give\n    the interaction and the next sentence the main effect of assignment, with the values recorded\n    under statistics.",
 "new_string": "  quote: 'Consistent with different firing magnitudes and non-identical tuning, ANOVA (factors:\n    cluster [7] and assignment [9]) revealed a main effect of cluster ... and cluster x assignment\n    interaction ... Demonstrative of uncertainty over-responding across clusters, ANOVA found a main\n    effect of assignment'"
}
```

```
The file claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml",
 "old_string": "    partially reproduced when all four exceed 0.250 but not all match.\n  data: dataset\n",
 "new_string": "    partially reproduced when all four exceed 0.250 but not all match.\n"
}
```

```
The file claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml paper/10.1016-j.cub.2021.02.055.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml",
 "old_string": "# quote checker cannot find these, so they were confirmed by reading. The column layout of Tables",
 "new_string": "# quote checker cannot find these, so they were confirmed by reading (also Table S3's \"1.50E-02\",\n# \"1.16E-04\", \"2.39E-04\", and the Figure S4 bound printed \"1-.62\"). The column layout of Tables"
}
```

```
The file claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml paper/10.1016-j.cub.2021.02.055.txt 2>&1 | tail -1; grep -c "criterion:" claims/crcns-rrf-1/*.yaml; grep -n " — \|rather" claims/crcns-rrf-1/*.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file at `claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml`.

**Text read:** the version of record with its full supplement: main text, STAR Methods, Table 1, Figures S1 to S6 and Tables S1 to S4. The extracted text mangles the layout of Tables S1 to S4, so I rendered those pages and Figure 6 from the PDF to read them. Figure 6 is also the only source for each cluster's outcome window.

**Code:** none was read. The paper says its MATLAB code goes to crcns.org, which puts it inside the dataset that readers may not open. The lab page it names, http://mcdannaldlab.org/resources, returns 404. Every method in the file comes from the STAR Methods, the Results, the figure legends or the supplement.

**Counts:** 30 claims. 29 have quotes; 1 (`table-s3-cluster-regression`) is marked inferred because its results appear only in Table S3. 104 statistical values are recorded and all 30 claims have criteria. Every quote passes the checker. The checker still exits with 9 problems, all p-values or CI bounds it cannot match because the text prints them oddly (powers of ten as "3 10�", Table S3's E-notation, the Figure S4 bound "1-.62"). I confirmed each one by reading.

**Details the paper leaves open, and the readings named for each:**
- **Normalization:** the z-score is taken over four trial types or over three (uncertainty pooled).
- **Cluster labels:** use the paper's own labels if the dataset holds them, or redo the k-means and match each cluster to k1 to k8 by its described cue firing pattern.
- **K-means:**
  - The six outcome epochs start at shock onset or at shock offset.
  - "Performed 10 times" means ten replicates per k or ten separate runs.
  - The input is normalized firing (Results) or raw firing rate (Methods).
- **The elbow at eight clusters:** the paper judges it by eye. I set a standard rule (every drop after k = 8 smaller than the drop from 7 to 8) and said that it is one.
- **Tuning curves:**
  - Average the 10 cue bins (Methods) or each cluster's own period from Figure 3 (Results).
  - Normalize each trial with the unit's mean and SD, or z-score across the unit's 16 trials.
- **Peak threat probability regressions:**
  - The sign is flipped for k4, k6 and k8 as it is for the tuning curves, or left as computed.
  - The Results call bin a between-units factor, but the printed df fit a within-units factor, which is the main reading.
  - Those df imply 362 units, not 364; the author is asked to report which units drop out.
- **Figure 5F:** each unit's betas are averaged over the 10 cue bins or over all 14 bins.
- **Behavior:** each rat's value is the mean over sessions or over all pooled trials.
- **Firing characteristics:** inter-spike intervals are pooled over the 16 trials or the measure is averaged over trials.
- **ANOVAs:** the printed partial eta squared values fit repeated measures with units as subjects, so that design is used. Whether a sphericity correction was applied is not stated; uncorrected df are the main reading and Greenhouse-Geisser a variant.

**Missing from the paper:**
- No analysis code was available, as above.
- The paper gives no numbers for the Figure 6 differential CIs. Their signs were read from the figure (the plus signs) and the per-trial-type values come from Table S4.
- The time courses described as early or sustained for k6, k7 and k8 appear only in the traces. Those claims are judged on each cluster's single Figure 6 window.

Nothing is committed.

## End of run

34 turns, 7 minutes, $2.58 at API prices, result: success.
