# strickland-2022 · claims · run 42850095857

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-022-34021-1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/bst-3.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-022-34021-1.txt",
 "offset": 317,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Supplementary (Fig|Table)\\.? ?S?\\d+|Table S|Fig\\. [5-9]",
 "path": "paper/10.1038-s41467-022-34021-1.txt",
 "offset": 20
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Supplementary (Fig|Table)",
 "path": "paper/10.1038-s41467-022-34021-1.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-022-34021-1.txt; sed -n '925,945p;1060,1075p' $f; grep -n "Supplementary Fig. 7\|Fig. 7\|^Supplementary\|Reference" $f | tail -20; sed -n '1355,1370p;1620,1640p;1770,1797p' $f
```

```
16
15
14
13
12
R2 value
0.5
0.0
Supplementary Fig. 5 Brainstem cue firing, split by sex. PC1 for cue firing (inset) and cluster 
contribution to PC1 for units from female rats (a) and male rats (b). Between cluster cue-firing 
correlations for units from female rats (c) and male rats (d), cue subnetwork outlined in magenta.
PC1 and PC2 from principal components analysis for cluster beta weights for units from female
rats (e) and from male rats (f). Abbreviations: d, danger; u, uncertainty; and s, safety. 
PC1 weight
PC2 weight
on
off
probability
behaviour
on
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "crcns" claims/*.yaml | head; grep -rn -i "code" claims/*.yaml | grep -i crcns | head -10; cat papers/datasets/strickland-2022.yaml 2>/dev/null
```

```
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
claims/farrell-2020.yaml
claims/goncalves-2013.yaml
claims/gu-2011.yaml
claims/henze-2000.yaml
claims/holdgraf-2016.yaml
claims/jadhav-2016.yaml
claims/johnson-2017.yaml
claims/gao-2018.yaml:16:# scripts "will be deposited on CRCNS.org" but gives no identifier. No code was read, so every
claims/guo-2017.yaml:17:# Code read: none. The paper links no analysis code. It names the data deposit "CRCNS.ORG in the NWB
claims/henry-2022.yaml:16:# Code: the paper links none. Data and code availability names only the CRCNS deposit, and says
claims/johnson-2017.yaml:20:# code is deposited with the data at CRCNS (http://crcns.org). By the data descriptor it is the
claims/johnson-2019.yaml:15:# Code. The paper's Data Availability says its custom MATLAB code is deposited at CRCNS with the
claims/kim-2020.yaml:12:# CRCNS data set (doi 10.6080/K07H1GSS). The data set's description says it holds a "codes" folder
claims/moaddab-2021.yaml:19:# Code. The paper says its "MATLAB code will be uploaded to http://crcns.org/", which puts it inside
claims/moaddab-2021.yaml:1453:  - Open, not settled. The paper's MATLAB code was not read (said to be deposited on CRCNS with the data), so the open readings named in the file (z-score over three or four trial types, tuning-curve bins from the Methods or the Results, single-trial normalization, sign inversion in Figure 5E, outcome epoch start for clustering) stay open; an author who finds the code in the data set should follow it where it settles one.
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p claims/moaddab-2021.yaml; sed -n 12,30p claims/johnson-2017.yaml
```

```
# Claims for Moaddab & McDannald (2021), Curr Biol 31:2099-2110, "Retrorubral field is a hub for
# diverse threat and aversive outcome signals", on CRCNS data set rrf-1 (doi:10.6080/K04B2ZJ5).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record with its supplemental information, as supplied under paper/
# (PyMuPDF text of the journal PDF): Results, Discussion, figure legends, Table 1, STAR Methods,
# and the supplement (Figures S1 to S6, Tables S1 to S4). The text garbles powers of ten ("2.80 3
# 10�11" is 2.80 x 10^-11, "5.93E�38" is 5.93E-38); p-values below are read from them, and the
# quote checker cannot find these, so they were confirmed by reading (also Table S3's "1.50E-02",
# "1.16E-04", "2.39E-04", and the Figure S4 bound printed "1-.62"). The column layout of Tables
# S1 to S4 and the Figure 6 panels were read from the PDF pages rendered as images: Table S1 rows
# are danger vs. uncertainty then uncertainty vs. safety; Table S2 columns are peak threat
# probability, fear output, then their difference; Table S3 rows are the regressor x bin
# interaction then the main effect of regressor; Table S4 rows are danger, uncertainty shock,
# uncertainty omission, safety. The gray boxes of Figure 6 (the analysed outcome interval) span 0
# to 8 s after shock offset for k1, k3, k5 and k6, and the whole 17.5 s for k2, k4, k7 and k8.
#
# Code. The paper says its "MATLAB code will be uploaded to http://crcns.org/", which puts it inside
# the data set, which the reader may not open; the lab page it names for behavior programs
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
import openpyxl
wb=openpyxl.load_workbook('10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True)
for ws in wb.worksheets:
    rows=list(ws.iter_rows(values_only=True))
    print('==',ws.title,len(rows), max(len(r) for r in rows) if rows else 0)
    for r in rows[:4]: print([c for c in r[:12]])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import openpyxl
ModuleNotFoundError: No module named 'openpyxl'
```

**Agent calls Bash**

```bash
cd paper; grep -n "^#####\|^== \|^Sheet\|^## " 10.1038-s41467-022-34021-1.txt | tail -30; awk 'NR>1640 && length($0)<300' 10.1038-s41467-022-34021-1.txt | head -80
```

```
41:## Brainstem threat probability and behavior signaling.
55:## Brainstem outcome firing.
67:## Brainstem prediction error and shock signaling.
75:## Discussion
91:## Methods
93:## Subjects
97:## Behavioral apparatus
101:## Nose poke acquisition
105:## Fear discrimination
109:## Calculating suppression ratios
113:## Surgery
117:## Data acquisition
121:## Probe retrieval
125:## Histology
129:## Neuron sorting
133:## Analysis
137:## Reporting summary
141:## Supplementary information
157:## Source data
167:## Supplementary information
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import zipfile,re
z=zipfile.ZipFile('10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx')
wb=z.read('xl/workbook.xml').decode()
print(re.findall(r'<sheet [^>]*name="([^"]+)"',wb))
for n in z.namelist():
    if 'worksheets/sheet' in n: print(n, z.getinfo(n).file_size)
E
```

```
['Figure 1c', 'Figure 2a', 'Figure 2b k1', 'Figure 2b k2', 'Figure 2b k3', 'Figure 2b k4', 'Figure 2b k5', 'Figure 2b k6', 'Figure 2b k7', 'Figure 2b k8', 'Figure 2b k9', 'Figure 2b k10', 'Figure 2b k11', 'Figure 2b k12', 'Figure 2b k13', 'Figure 2b k14', 'Figure 2b k15', 'Figure 2b k16', 'Figure 2b k17', 'Figure 2b k18', 'Figure 2b k19', 'Figure 2b k20', 'Figure 2b k21', 'Figure 2c inset', 'Figure 2c', 'Figure 2d', 'Figure 2e', 'Figure 2f', 'Figure 2g', 'Figure 3a k1', 'Figure 3a k2', 'Figure 3a k3', 'Figure 3a k4', 'Figure 3a k5', 'Figure 3a k6', 'Figure 3a k7', 'Figure 3a k8', 'Figure 3a k9', 'Figure 3a k10', 'Figure 3a k11', 'Figure 3a k12', 'Figure 3a k13', 'Figure 3a k14', 'Figure 3a k15', 'Figure 3a k16', 'Figure 3a k17', 'Figure 3a k18', 'Figure 3a k19', 'Figure 3a k20', 'Figure 3a k21', 'Figure 3b middle', 'Figure 3b bottom', 'Figure 3c middle', 'Figure 3c bottom', 'Figure 3d middle', 'Figure 3d bottom', 'Figure 3e left', 'Figure 3e right', 'Figure 4a', 'Figure 4b k1', 'Figure 4b k2', 'Figure 4b k3', 'Figure 4b k4', 'Figure 4b k5', 'Figure 4b k6', 'Figure 4b k7', 'Figure 4b k8', 'Figure 4b k9', 'Figure 4b k10', 'Figure 4b k11', 'Figure 4c', 'Figure 4d', 'Figure 4e left', 'Figure 4e right', 'Figure 4f left', 'Figure 4f right', 'Figure 4g', 'Figure 5a k1', 'Figure 5a k2', 'Figure 5a k3', 'Figure 5a k4', 'Figure 5a k5', 'Figure 5a k6', 'Figure 5a k7', 'Figure 5a k8', 'Figure 5a k9', 'Figure 5a k10', 'Figure 5a k11', 'Figure 5b middle', 'Figure 5b bottom', 'Figure 5c middle', 'Figure 5c bottom', 'Figure 5d middle', 'Figure 5d bottom', 'Figure 5e left', 'Figure 5e right']
xl/worksheets/sheet4.xml 90565
xl/worksheets/sheet72.xml 43645
xl/worksheets/sheet71.xml 6730131
xl/worksheets/sheet70.xml 1125367
xl/worksheets/sheet69.xml 689148
xl/worksheets/sheet73.xml 949715
xl/worksheets/sheet74.xml 2312171
xl/worksheets/sheet75.xml 32252
xl/worksheets/sheet76.xml 74069
xl/worksheets/sheet77.xml 13192
xl/worksheets/sheet78.xml 267641
xl/worksheets/sheet68.xml 658570
xl/w
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; cat > $TMPDIR/sd.py <<'E'
import zipfile,re,sys
z=zipfile.ZipFile('10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx')
wb=z.read('xl/workbook.xml').decode()
rels=z.read('xl/_rels/workbook.xml.rels').decode()
rid={m[0]:m[1] for m in re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"',rels)}
rid.update({m[1]:m[0] for m in re.findall(r'Target="([^"]+)"[^>]*Id="([^"]+)"',rels)})
sheets=re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',wb)
try:
    ss=z.read('xl/sharedStrings.xml').decode()
    strs=[re.sub('<[^>]+>','',s) for s in re.findall(r'<si>(.*?)</si>',ss,re.S)]
except KeyError: strs=[]
def read(name):
    t=dict(sheets)[name]; f='xl/'+rid[t].lstrip('/').replace('xl/','')
    x=z.read(f).decode()
    rows=[]
    for r in re.findall(r'<row[^>]*>(.*?)</row>',x,re.S):
        row=[]
        for c in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)',r,re.S):
            attrs,body=c; v=re.search(r'<v>(.*?)</v>',body or ''); v=v.group(1) if v else ''
            if 't="s"' in attrs and v: v=strs[int(v)]
            row.append(v)
        rows.append(row)
    return rows
E
python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
for n,_ in sheets:
    if n.startswith('Figure 2b') or n.startswith('Figure 4b'):
        r=read(n); print(n,len(r),r[0][:3])
E
```

```
Figure 2b k1 25 ['pre cue', 'pre cue', 'danger']
Figure 2b k2 44 ['pre cue', 'pre cue', 'danger']
Figure 2b k3 27 ['pre cue', 'pre cue', 'danger']
Figure 2b k4 45 ['pre cue', 'pre cue', 'danger']
Figure 2b k5 45 ['pre cue', 'pre cue', 'danger']
Figure 2b k6 73 ['pre cue', 'pre cue', 'danger']
Figure 2b k7 93 ['pre cue', 'pre cue', 'danger']
Figure 2b k8 58 ['pre cue', 'pre cue', 'danger']
Figure 2b k9 104 ['pre cue', 'pre cue', 'danger']
Figure 2b k10 106 ['pre cue', 'pre cue', 'danger']
Figure 2b k11 75 ['pre cue', 'pre cue', 'danger']
Figure 2b k12 47 ['pre cue', 'pre cue', 'danger']
Figure 2b k13 84 ['pre cue', 'pre cue', 'danger']
Figure 2b k14 203 ['pre cue', 'pre cue', 'danger']
Figure 2b k15 56 ['pre cue', 'pre cue', 'danger']
Figure 2b k16 138 ['pre cue', 'pre cue', 'danger']
Figure 2b k17 220 ['pre cue', 'pre cue', 'danger']
Figure 2b k18 90 ['pre cue', 'pre cue', 'danger']
Figure 2b k19 111 ['pre cue', 'pre cue', 'danger']
Figure 2b k20 95 ['pre cue', 'pre cue', 'danger']
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
for n in ['Figure 2c inset','Figure 2c','Figure 2e','Figure 2g','Figure 3b middle','Figure 3e left','Figure 3e right','Figure 4c','Figure 4d','Figure 4e left','Figure 5b middle','Figure 5e right']:
    r=read(n); print('==',n,len(r),max(len(x) for x in r))
    for x in r[:6]: print('  ',[ (v[:7] if len(v)>8 else v) for v in x[:24]])
r=read('Figure 2d'); print('2d',len(r)); print(r[:3]); 
E
```

```
== Figure 2c inset 1813 43
   ['neuron ', 'pre cue', 'pre cue', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'post cue', 'post cue', 'pre cue', 'pre cue', 'uncerta', 'uncerta', 'uncerta', 'uncerta', 'uncerta', 'uncerta', 'uncerta']
   ['1', '-2.4773', '-2.4773', '4.13718', '3.83990', '1.46164', '-2.4773', '0.12386', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '-2.4773', '1.01571', '0.27250', '0.79275', '-2.4773', '-2.4773', '0.12386', '-2.4773']
   ['2', '-0.2335', '0.22184', '3.47948', '3.89982', '2.95405', '2.60377', '2.00829', '1.27269', '1.13258', '0.36195', '0.81732', '0.57213', '1.13258', '0.81732', '0.11676', '-9.3408', '2.14840', '1.76309', '1.22015', '1.88569', '1.46535', '1.36026', '0.85235']
   ['3', '-7.3262', '0.19724', '3.71382', '3.10518', '1.61740', '0.87350', '1.54977', '1.14401', '0.80588', '0.53537', '0.40012', '0.94113', '1.07638', '2.15841', '-5.6355', '-0.1070', '1.92171', '1.27926', '2.02315', '1.48214', '1.17782', '1.21164', '0.94113']
   ['4', '4.92129', '-6.1516', '3.66636', '3.11272', '0.89813', '4.92129', '1.30414', '0.67667', '-0.2091', '-0.2460', '-0.2460', '-0.2091', '-0.2091', '0.27067', '-7.9971', '6.76678', '1.82088', '1.13805', '1.35950', '0.28912', '0.41831', '0.36294', '6.76678']
   ['5', '-0.1558', '0.13183', '2.92602', '3.35748', '3.19312', '2.55620', '1.63165', '1.69329', '1.44674', '0.50165', '0.74820', '0.89201', '1.32347', '0.93311', '9.07428', '-6.3348', '2.46375', '1.71384', '1.47756', '1.91929', '2.02202', '1.93984', '1.28238']
== Figure 2c 22 3
   ['Cluster', 'Value']
   ['1', '0.12148', '']
   ['2', '0.11293']
   ['3', '5.14128']
   ['4', '4.34590']
   ['5', '3.95701']
== Figure 2e 22 43
   ['Cluster', 'pre cue', 'pre cue', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'danger', 'post cue', 'post cue', 'pre cue', 'pre cue', 'uncerta', 'uncerta', 'uncerta', 'uncerta', 'uncerta', 
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
for x in read('Figure 2c'): print(x)
from collections import Counter
r=read('Figure 2d')[1:]; c=Counter(x[0] for x in r); print(sorted(c.items(),key=lambda t:int(t[0])))
import statistics as s
m={k:s.mean(float(x[1]) for x in r if x[0]==k) for k in c}; print({k:round(v) for k,v in sorted(m.items(),key=lambda t:int(t[0]))})
print(read('Figure 2f')[:3], len(read('Figure 2f')))
print(read('Figure 4f left')[:3], len(read('Figure 4f left')))
print(read('Figure 4f right')[:3], len(read('Figure 4f right')))
E
```

```
['Cluster', 'Value']
['1', '0.121484004348999', '']
['2', '0.11293919636003701']
['3', '5.14128344796927E-2']
['4', '4.3459026830448499E-2']
['5', '3.95701626641312E-2']
['6', '2.6820622347392901E-2']
['7', '2.5722946352785801E-2']
['8', '1.76111463236618E-2']
['9', '1.2174175321991E-2']
['10', '6.5231183981285497E-3']
['11', '6.2327524138989301E-3']
['12', '5.1751038091801798E-3']
['13', '3.0370793751406202E-3']
['14', '2.8240169449304199E-3']
['15', '2.3095227617074901E-3']
['16', '1.8962323492964801E-3']
['17', '1.8505689374329001E-3']
['18', '8.1094713632236205E-4']
['19', '-6.1785807917757996E-5']
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
for n in ['Figure 3a k1','Figure 5a k1','Figure 2b k1','Figure 4b k2','Figure 3b middle','Figure 3c middle','Figure 4g','Figure 5e left','Figure 4e right']:
    r=read(n); print('==',n,len(r),[len(x) for x in r[:4]])
    for x in r[:3]: print('  ',x[:6], x[-3:])
E
```

```
== Figure 3a k1 25 [42, 42, 42, 42]
   ['pre cue', 'pre cue', 'danger', 'danger', 'danger', 'danger'] ['safety', 'post cue', 'post cue']
   ['-0.38783607945721299', '-0.40734370998634101', '4.4890715528246297', '3.2600908294896001', '2.8211691425842398', '2.5578161304410201'] ['0.26566954326855302', '-0.465866601573723', '-0.153744513107685']
   ['-0.200112000184622', '-0.44359428177807902', '2.23471081574995', '2.23471081574995', '1.2607816893761199', '1.6260051117662999'] ['-0.32185314098135098', '-0.62620599297317203', '-0.80881770416826504']
== Figure 5a k1 79 [80, 81, 80, 80]
   ['danger', '', '', '', '', ''] ['', '', '']
   ['post shock interval', '1', '2', '3', '4', '5'] ['18', '19', '20']
   ['1.45839469890891', '2.7725926753975401', '1.16635070413366', '0.72828471197078204', '-0.147847272354971', '-0.43989126713022197'] ['-0.43989126713022197', '-1.8252749673453299E-3', '-0.43989126713022197']
== Figure 2b k1 25 [42, 42, 42, 42]
   ['pre cue', 'pre cue', 'danger', 'danger', 'danger', 'danger'] ['safety', 'post cue', 'post cue']
   ['-0.38783607945721299', '-0.40734370998634101', '4.4890715528246297', '3.2600908294896001', '2.8211691425842398', '2.5578161304410201'] ['0.26566954326855302', '-0.465866601573723', '-0.153744513107685']
   ['-0.200112000184622', '-0.44359428177807902', '2.23471081574995', '2.23471081574995', '1.2607816893761199', '1.6260051117662999'] ['-0.32185314098135098', '-0.62620599297317203', '-0.80881770416826504']
== Figure 4b k2 48 [80, 81, 80, 80]
   ['danger', '', '', '', '', ''] ['', '', '']
   ['post shock interval', '1', '2', '3', '4', '5'] ['18', '19', '20']
   ['2.2627520943909101', '2.9744399074774499', '0.72550641812397398', '0.96273568915282104', '0.91528983494705196', '0.67806056391820402'] ['-0.664657110105074', '-0.56027623085238099', '-0.446406180758534']
== Figure 3b middle 23 [29, 41, 29, 29]
   ['Cluster', 'Threat Probability', '', '', '', ''] ['', '', '']
   ['pre-cue', 'pre-cue', 'cue', 'cue', 'cue', 'cue'] ['', '', 
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
import numpy as np
r=read('Figure 1c')[1:]; X=np.array([[float(v) for v in x[1:4]] for x in r]); n=len(X); print(n, X.mean(0))
gm=X.mean(); ss_c=n*((X.mean(0)-gm)**2).sum(); ss_s=3*((X.mean(1)-gm)**2).sum(); ss_t=((X-gm)**2).sum(); ss_e=ss_t-ss_c-ss_s
print('RM F',(ss_c/2)/(ss_e/(2*(n-1))))
ss_w=ss_t-ss_c; print('oneway F',(ss_c/2)/(ss_w/(3*n-3)))
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
r=read('Figure 1c')[1:]; X=[[float(v) for v in x[1:4]] for x in r]; n=len(X)
cm=[sum(x[j] for x in X)/n for j in range(3)]; gm=sum(cm)/3; print(n,cm)
ss_c=n*sum((c-gm)**2 for c in cm); ss_s=3*sum((sum(x)/3-gm)**2 for x in X); ss_t=sum((v-gm)**2 for x in X for v in x); ss_e=ss_t-ss_c-ss_s
print('RM F',(ss_c/2)/(ss_e/(2*(n-1))), 'oneway F',(ss_c/2)/((ss_t-ss_c)/(3*n-3)))
E
```

```
73 [0.9140405467144495, 0.7093580638339362, 0.23042519819579396]
RM F 116.22137577085334 oneway F 95.31791848642034
```

**Agent calls Bash**

```bash
cd paper; sed -n '1180,1360p' 10.1038-s41467-022-34021-1.txt | tr '\n' '|' | head -c 3000; echo; sed -n '1160,1180p' 10.1038-s41467-022-34021-1.txt
```

```
s off|d|us|uos|R2 value|0.5|0.0|1|2|3|4|5|6|7|8|9|10|11|1|2|3|4|5|6|7|8|9 10 11|PC2 weight|PC1 weight|PC2 weight|Cluster #|Cluster #|PC1 weight|s off|s off|a|c|e|b|d|f|R2 value|0.5|0.0|1|2|3|4|5|6|7|8|9|10|11|1|2|3|4|5|6|7|8|9 10 11|Cluster #|Cluster #|PC1 weight|-0.2|0|0.2|PC1 weight|-0.2|0|0.2|-0.50|-0.25|0.00|0.25|0.50|-0.50|-0.25|0.00|0.25|0.50|-0.25|0.00|0.25|0.50|-0.25|0.00|0.25|0.50|error|shock|d|us|uos||   |Subject |Sex |Age (days) |Sessions |Recording termination |Probe use # |Explanted | | | |1 |F |131 |8 |Reached 8 sessions |1 |Yes |2 |F |124 |9 |Reached 9 sessions |2 |Yes |3 |F |127 |10 |Reached 10  sessions |1 |Yes |4 |M |99 |2 |Lost signal  |1 |Yes |5 |M |95 |8 |Reached 8 sessions |1 |Yes |6 |M |115 |1 |Lost signal |1 |Yes |7 |M |115 |10 |Reached 10 sessions |1 |Yes |8 |M |116 |7 |broken headcap |1 |Yes |9 |M |117 |10 |Reached 10 sessions |1 |Yes |10 |F |140 |10 |Reached 10  sessions |1 |Yes |Supplementary Table 1. Recording summary. For each subject: sex, age in days at the |start of recording, the number of recording sessions completed, the reason recording |
d
us
uo
s
d
us
uo
s
d
us
uo
s

Supplemental Fig. 7 Brainstem outcome firing split by sex. Between cluster 
firing correlations for units from female (a) and male (b) rats. PC1 for brainstem 
outcome firing, for units from female (c) and male rats (d). PC1 and PC2 
resulting from principal components for cluster beta weights for units from 
female rats (e) and male rats (f). Abbreviations: d, danger; 
us, uncertainty shock; uo, uncertainty omission, and s, safety.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '1370,1628p' 10.1038-s41467-022-34021-1.txt | tr '\n' '|'
```

```
5 |6 |7 |8 |9 |10 |DPG |13 |  |  |7 |  |  |  |  |112 |13 |DPwh |19 |  |  |2 |  |16 |1 |  |9 |25 |DLPAG |61 |9 |  |  |  |  |28 |  |33 |48 |LPAG |12 |7 |29 |2 |14 |  |  |43 |  |15 |VLPAG |12 |5 |24 |2 |22 |1 |7 |18 |26 |30 |Me5 |  |  |  |  |  |2 |  |  |  |  |DRL |  |  |  |1 |  |  |  |  |  |  |DRD |5 |55 |  |  |  |  |  |  |28 |11 |DRV |17 |41 |  |  |  |  |  |  |150 |  |PDR |7 |  |  |3 |  |  |  |  |  |17 |mlf |11 |9 |  |  |  |  |  |  |  |37 |isRt |  |  |  |  |  |5 |28 |17 |  |  |Pa4 |  |  |  |  |  |3 |1 |17 |  |  |x/scp |11 |  |  |2 |  |  |  |21 |  |  |SPTg |  |  |50 |7 |  |11 |4 |  |  |  |PNO |  |  |38 |  |  |5 |23 |  |  |35 |VTg |  |  |  |6 |  |  |  |  |  |29 |DMTg |  |  |  |  |5 |  |  |  |  |  |ts |  |  |  |  |  |  |24 |79 |  |  |PMnR |  |130 |  |  |11 |  |  |  |51 |44 |MnR |24 |72 |  |  |  |  |  |  |  |  |Total |192 |328 |141 |32 |52 |43 |116 |195 |409 |304 |# units |24 |36.44444 14.1 |16 |6.5 |43 |11.6 |27.85714 40.9 |30.4 |per session  |Supplementary Table 2. Number of units per region, per subject. For each brain region, organized dorsal |
```

**Agent calls Bash**

```bash
cd paper; which pdfinfo pdftotext; pdfinfo *.pdf 2>/dev/null | grep Pages; pdftotext -layout -f 12 -l 14 *MOESM1_ESM.pdf - 2>/dev/null | grep -n -A30 "Pa4\|x/scp" | head -40
```

```
(Bash completed with no output)
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM1_ESM.pdf",
 "pages": "13-14"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
from statistics import mean,correlation
c=[float(x[1]) for x in read('Figure 2c')[1:]]
r=read('Figure 2d')[1:]
lat=[mean(float(x[1]) for x in r if int(x[0])==k) for k in range(1,22)]
print(correlation(c,lat)**2)
sizes=[24,43,26,44,44,72,92,57,103,105,74,46,83,202,55,137,219,89,110,94,93]; print(sum(sizes))
tot=[c*s for c,s in zip(c,sizes)]; print(correlation(tot,lat)**2)
import math
print(correlation([math.log(v) for v in lat],c)**2)
# Fig 2f hub
f=read('Figure 2f')[1:]
for k in range(1,10):
    v=[float(x[1]) for x in f if int(x[0])==k]; print(k,len(v),round(mean(v),3))
E
```

```
0.5078902573807194
1812
0.3945544527321623
0.6459716723455533
1 24 0.424
2 43 0.466
3 26 0.201
4 44 0.259
5 44 0.22
6 72 0.301
7 92 0.276
8 57 0.205
9 103 0.183
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; ls schemas 2>/dev/null; grep -rn "kind:" claims/*.yaml | awk '{print $3}' | sort | uniq -c
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print([k for k in s['properties']])"
```

```
{
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
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
r=read('Figure 5e left'); print(r)
ph=[float(v) for v in r[1][1:]]; to=[float(v) for v in r[2][1:]]
ext=[3,4,5,7,8,9,20]  # DLPAG LPAG VLPAG DRL DRD DRV PMnR (1-based)
print(sum(ph[i-1] for i in ext)/sum(ph), sum(to[i-1] for i in ext)/sum(to), sum(ph),sum(to))
g=read('Figure 4g'); 
for k in range(1,12):
    col=[float(x[k]) if len(x)>k and x[k] not in ('',) else 0 for x in g[2:]]
    print(k, sum(1 for v in col if v>0), round(sum(col),1))
print(read('Figure 5e right'))
print(read('Figure 3e right'))
E
```

```
[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'], ['1_3', '51', '30', '57', '48', '49', '1', '0', '44', '70', '7', '13', '13', '8', '11', '22', '42', '15', '1', '37', '103', '57'], ['6_9', '51', '21', '68', '47', '54', '1', '0', '36', '76', '9', '21', '12', '2', '13', '27', '39', '8', '4', '26', '74', '24']]
0.5463917525773195 0.5791190864600326 679.0 613.0
1 15 100.0
2 10 100.0
3 16 100.0
4 19 100.0
5 18 100.0
6 17 100.0
7 15 100.0
8 16 100.0
9 18 100.0
10 18 100.0
11 19 100.0
[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'], ['0.80869333320519798', '-0.99248727257001601', '2.6982872326879299', '0.59799100010330997', '1.5926405543129101', '1.58567320236313E-2', '0', '-0.60736088720818304', '2.0887640638401699', '0.43726139822741', '1.5111946125551701', '4.3005379276212001E-2', '-0.85193896599691998', '0.50068832632193505', '1.16450878967486', '0.17658633389953199', '-0.90407397886249596', '0.50525314311661695', '-1.2077544224665899', '-3.09758857546483', '-4.4795267966758496']]
[['brain region', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'], ['% k1_k9 vs k10_k21', '5.9268069117546798', '-1.3908353344898401', '0.305589855083444', '7.4120311801646901', '-2.73667305521677', '-0.15302218821729199', '-7.6511094108645802E-2', '3.13210663070898', '-4.65854083495572', '-1.2422068526668999', '0.30589286931753601', '-3.2764929132546001', '-0.75162680766929002', '-1.2602361995954801', '-1.6653662305786801', '-4.0755414485595103E-2', '-0.75617202118069504', '-0.108024574454385', '-2.39002477141364', '2.5331989970228799', '0.890861848235321']]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import sys,os; sys.path.insert(0,os.environ['TMPDIR']); from sd import *
g=read('Figure 4g'); print(g[0]); print([x[0] for x in g[2:]])
sz=[77,46,142,169,245,142,111,171,189,198,322]
ext=[3,4,5,7,8,9,10,20]
def frac(ks):
    tot=0;e=0
    for k in ks:
        col=[float(x[k]) if len(x)>k and x[k]!='' else 0 for x in g[2:]]
        n=[c*sz[k-1]/100 for c in col]; tot+=sum(n); e+=sum(n[i-1] for i in ext)
    return e/tot
print(frac([1,2,3]),frac([6,7,8,9]),frac([1,2,3,4,5]))
E
```

```
['cluster', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
0.5999999999999999 0.5938009787928222 0.5567010309278351
```

**Agent calls Write**

```json
{
 "file_path": "claims/strickland-2022.yaml",
 "content": "# Claims for Strickland & McDannald (2022), Nat Commun 13:6192, \"Brainstem networks construct\n# threat probability and prediction error from neuronal building blocks\", on CRCNS data set bst-3\n# (doi:10.6080/K0Q23XGR).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC9582012, open access, Europe PMC JATS XML flattened), with\n# Results, Discussion, figure legends and Methods, and its Supplementary Information\n# (41467_2022_34021_MOESM1_ESM.pdf as extracted text, publisher's site): Supplementary Methods\n# (head cap, surgery, acquisition, sorting, z-score normalization, heat plots, k-means, PCA,\n# latency, correlations, hubs, regression, lesion PCA, anatomy, chi-square), Supplementary\n# Figures 1 to 7 (legends; the panels are garbled in the extraction) and Supplementary Tables 1\n# and 2 (read from the extracted cells; Table 2's column layout is garbled, its row and subject\n# totals are not). The Source Data workbook (41467_2022_34021_MOESM4_ESM.xlsx) was read with a\n# small XML parser; numbers marked \"Source Data\" below come from it. The supplement PDF could not\n# be rendered (no poppler), so no panel was read as an image. The CRCNS data descriptor\n# (paper/bst-3.data-description.txt) was read only to know what the data set holds; no claim or\n# method comes from it.\n#\n# Code. The paper's Code availability says \"Code for single-unit analyses is available at\n# https://crcns.org/\", which puts it inside the data set (by its descriptor the scripts folder,\n# cubeAnalysis, cueAnalysis, cueRegression, outcomeAnalysis, outcomeRegression, MATLAB). Being\n# among the data set's files, it was not read in this run, and no commit is recorded. Every method\n# below is from the Methods, the Supplementary Methods, the legends or the Source Data. Where those\n# scripts settle a detail named as open below, the author may follow them (protocol, Reader step 2)\n# and should say so.\n#\n# Data the paper used. Ten Long-Evans rats (six male, four female; subjects 1 to 3 and 10 female,\n# Supplementary Table 1), shaped to nose poke for pellets on VI-60 independent of cues and shock,\n# then 12 sessions of probabilistic fear discrimination before a single Neuropixels 1.0 probe was\n# implanted through the brainstem (AP -8.00, ML -2.80, DV -7 to -7.5, 15 degree angle). Each\n# recording session (1 to 10 per rat) has 16 trials, 10-s auditory cues, mean ITI 3 min, random\n# order. 4 danger (shock p = 1), 2 uncertainty shock and 6 uncertainty omission (p = 0.25),\n# 4 safety (p = 0). Shock is 0.5 mA, 0.5 s, starting 2 s after cue offset, so shock offset falls\n# 2.5 s after cue offset (the same time is used on omission and safety trials). Measured variables\n# are spike times of sorted single units (Kilosort 2 or 2.5, Phy, a MATLAB stability screen), cue,\n# shock, pellet and nose-poke times, and each unit's brain region (21 regions, from histology and\n# the Paxinos and Watson atlas). 1812 units from 73 sessions; 965 from females. Supplementary\n# Table 1 lists 8, 9, 10, 2, 8, 1, 10, 7, 10 and 10 sessions for subjects 1 to 10 (75 in total),\n# against 73 in the Results and in Source Data Fig. 1c; the paper does not say which two sessions\n# are not counted. By its title and description the data set holds the 1812 units as one MATLAB\n# file each, with per-trial firing, z-normalized firing, nose pokes, suppression ratios and\n# anatomy (region, coordinates) per unit.\n#\n# Shared method, used by the claims below and cited there as \"shared method\".\n#  - Suppression ratio (Methods, Calculating suppression ratios). Per trial, baseline rate = pokes\n#    in the 20 s before cue onset x 3, cue rate = pokes in the 10-s cue x 6, ratio = (baseline -\n#    cue) / (baseline + cue). Open, (sr-a) a trial with no pokes in either period set to 0, or\n#    (sr-b) left out of means. A session's value for a cue is the mean over its trials of that\n#    cue (uncertainty pooling its 8 trials).\n#  - Normalized firing (Supplementary Methods, Z-score normalization). Per unit and trial, firing\n#    rate in 250-ms bins; the trial's baseline (mean rate over the 2 s before cue onset) is\n#    subtracted; the differential firing is z-scored across all trials and bins of the unit.\n#    Open, (n-a) baseline per trial, or (n-b) the mean baseline of that trial type (\"baseline\n#    firing rate (2 s prior to cue onset) specific to that trial type\"). Open, the epoch is given\n#    both as \"from 20 s prior to cue onset to 20 s following cue offset\" (w-a, 200 bins) and as\n#    \"a total of 240 bins\" (w-b, 60 s from 20 s before cue onset). Mean over trials per trial type,\n#    then 250-ms bins averaged into 1-s intervals (cue) or 500-ms intervals (outcome).\n#  - Cue matrix (Supplementary Methods, K-means clustering and PCA). 1812 x 42, per cue 14 1-s\n#    intervals from 2 s before cue onset to 2 s after cue offset, columns 1-14 danger, 15-28\n#    uncertainty (all 8 trials), 29-42 safety.\n#  - Outcome matrix. 1812 x 80, per trial type 20 500-ms intervals over the 10 s from shock offset,\n#    columns 1-20 danger, 21-40 uncertainty shock, 41-60 uncertainty omission, 61-80 safety.\n#  - K-means (Supplementary Methods, K-means clustering). MATLAB kmeans, number of clusters 21\n#    (cue) and 11 (outcome), chosen by the paper by inspecting solutions for 1 to 25 and 1 to 20\n#    clusters. No option, replicate count or seed is given. Standard choice, MATLAB's defaults\n#    (squared Euclidean distance, k-means++ seeding, one replicate); since one replicate depends\n#    on the seed, a solution's result is reported as the median over 20 seeds, and the best of\n#    20 replicates (lowest summed distance) is shown as a variant.\n#  - Cluster labels, two readings. (L1) The paper's own membership. Source Data sheets\n#    \"Figure 2b k1\" to \"k21\" hold the 42-value cue row of every member unit and \"Figure 4b k1\" to\n#    \"k11\" the 80-value outcome row; each dataset unit is assigned to the sheet whose row it\n#    matches (claim source-data-cluster-link). Their row counts give cue cluster sizes 24, 43, 26,\n#    44, 44, 72, 92, 57, 103, 105, 74, 46, 83, 202, 55, 137, 219, 89, 110, 94, 93 (k1 to k21; k1-k9\n#    sum to 505) and outcome sizes 77, 46, 142, 169, 245, 142, 111, 171, 189, 198, 322 (k1 to k11;\n#    k1-k3 sum to 265, k6-k9 to 613, as the Results give). (L2) The author's own k-means. Cue\n#    clusters are numbered by decreasing PC1 contribution per unit, as the paper's are (Source\n#    Data Fig. 2c falls from 0.121 for k1 to -0.0026 for k21); outcome clusters are matched to the\n#    paper's by largest member overlap with L1 (Hungarian assignment), or, when L1 fails, by\n#    correlation of cluster-mean 80-value profiles with the means of the Source Data Fig. 4b\n#    sheets. Claims that name a cluster need L1 or this matching.\n#  - Networks. Cue subnetwork k1-k9 and supranetwork k10-k21 (Results; Source Data Fig. 3e rows\n#    \"k1_k9\" and \"k10_k21\", Fig. 2f with 505 units). The Supplementary Methods name \"clusters 1-8\"\n#    (hubs, lesion); that is shown as a variant. Phasic outcome network k1-k3 (n = 265) and tonic\n#    k6-k9 (n = 613) (Results). The Supplementary Methods name phasic \"clusters 1-5\" and tonic\n#    \"clusters 7-10\", and Source Data Fig. 5e's row \"1_3\" holds 679 units, the size of k1-k5;\n#    so for Fig. 5c and 5e, phasic is read as (p-a) k1-k3 or (p-b) k1-k5.\n#  - PCA. MATLAB pca with its defaults (columns centred, not scaled), units or clusters as rows;\n#    percent variance explained as the paper's \"% firing variance\" or \"% signaling variance\".\n#    A PC's sign is arbitrary; each criterion fixes the orientation it uses.\n#  - Shuffle, lesion (Supplementary Methods, PCA and 'Lesion' x PCA x linear regression). 1000\n#    iterations. The paper does not say what is permuted. Open, (s-a) each row of the shuffled\n#    clusters permuted independently across its columns, or (s-b) all entries of the shuffled\n#    block permuted together. For averaged PC weights each iteration's PC is sign-aligned to the\n#    intact PC (positive dot product), a choice the paper does not state.\n#  - Regression (Supplementary Methods, Linear regression). Per cluster and interval, MATLAB\n#    regress of firing on two regressors over the 16 trial rows. Cue, threat probability (1 for\n#    the 4 danger rows, 0.25 for the 8 uncertainty rows, 0 for the 4 safety rows) and behaviour\n#    (\"the trial-specific, mean suppression ratio for the cluster\"), 14 1-s intervals. Outcome,\n#    shock (1, 1, 0, 0 for danger, uncertainty shock, uncertainty omission, safety) and prediction\n#    error (0, 0.75, -0.25, 0), 20 500-ms intervals. Open, (r-a) one regression on the cluster's\n#    mean normalized firing per trial row, with behaviour the mean over member units of that row's\n#    suppression ratio, or (r-b) one regression per unit on its own trials and its session's\n#    ratios, betas then averaged within the cluster (the legends call them \"Mean cluster beta\n#    weights\", with SEM); and (i-a) with an intercept column or (i-b) without. Source Data Fig. 3b\n#    middle holds the paper's 21 x 28 cue beta matrix and Fig. 5b middle the outcome matrix; the\n#    reading whose matrix matches them is to be adopted where the readings disagree.\n#  - Mapping (Supplementary Methods, Mapping cluster and network membership). Differential\n#    composition per region = the region's proportion in a network minus the network's overall\n#    proportion, in percentage points.\n#\n# Not claimed. The sex splits (Supplementary Figs. 3, 5, 6, 7) carry no stated finding; Fig. 2a and\n# 4a heat maps and Supplementary Fig. 4 (rat x cluster counts) are descriptive.\nschema_version: 2\npaper: doi:10.1038/s41467-022-34021-1\nclaims:\n- id: source-data-cluster-link\n  kind: link\n  statement: The data set's units can be matched to the rows of the paper's Source Data cluster\n    sheets, which gives the paper's own cue and outcome cluster membership.\n  source: Source Data, sheets Figure 2b k1 to k21 and Figure 4b k1 to k11; Supplementary Methods,\n    Z-score normalization and K-means clustering\n  criterion: For each unit, the 42-value cue row and 80-value outcome row are computed with the\n    shared method, under each normalization reading (n-a, n-b, w-a, w-b), and compared with the\n    rows of the Source Data sheets. A unit matches a row when the largest absolute difference is\n    below 0.01 (a standard tolerance for rounding). The link holds (reproduced) when, under one\n    reading, at least 95% of the 1812 Source Data cue rows and of the 1812 outcome rows each match\n    exactly one unit; partially reproduced for 50% to 95%, using the best Pearson correlation\n    above 0.99 as the match; not reproduced below. The reading that matches is reported, as it\n    settles the normalization readings for the other claims.\n- id: fig1c-suppression-order\n  statement: During recording sessions suppression of rewarded nose poking was high to danger,\n    intermediate to uncertainty and low to safety, with a main effect of cue (F(2,142) = 149.2,\n    p = 1.26 x 10^-35) over 73 sessions.\n  source: Results, paragraph 1; Figure 1c; Source Data Fig. 1c\n  quote: Suppression of rewarded nose poking was high to danger, intermediate to uncertainty, and\n    low to safety (Fig. 1c ; ANOVA main effect of cue [ F (2,142) = 149.2, p = 1.26 × 10 –35 ]\n  statistics:\n  - test: ANOVA, main effect of cue\n    statistic: F(2,142) = 149.2\n    p: 1.26e-35\n    n: 73 recording sessions\n  expected:\n  - quantity: F for the main effect of cue\n    value: 149.2\n    tolerance: 14.92\n  - quantity: mean danger suppression ratio over sessions (Source Data Fig. 1c)\n    value: 0.914\n    tolerance: 0.091\n  - quantity: mean uncertainty suppression ratio over sessions (Source Data Fig. 1c)\n    value: 0.709\n    tolerance: 0.071\n  - quantity: mean safety suppression ratio over sessions (Source Data Fig. 1c)\n    value: 0.230\n    tolerance: 0.023\n  criterion: Session values per cue as in the shared method (suppression ratio). The ANOVA design\n    is not given. Its degrees of freedom, 2 and 142 with 73 sessions, fit (a-a) a cue (within) x\n    sex (between, sessions as subjects) mixed ANOVA, error df 2 x (73 - 2); (a-b) a one-way\n    repeated-measures ANOVA over sessions has df 2 and 144 and is shown as well. On the paper's\n    own Source Data Fig. 1c values (a-b) gives F(2,144) = 116.2, so (a-a) is the leading reading.\n    Reproduced when the session means are ordered danger > uncertainty > safety, each within\n    tolerance, and the cue effect has p < 0.05 with F within tolerance under one reading;\n    partially reproduced when the order and p < 0.05 hold but F or a mean is out of tolerance.\n- id: figs2-each-rat-discriminates\n  statement: Rats showed complete discrimination during the recording sessions, shown rat by rat\n    with 95% bootstrap confidence intervals over sessions.\n  source: Results, paragraph 1; Supplementary Fig. 2 legend\n  quote: Rats showed complete discrimination during recording sessions\n  criterion: Per rat, session suppression ratios per cue (shared method). Supplementary Fig. 2 marks\n    \"+\" where a \"95% bootstrap confidence interval does not contain zero\" but does not say of\n    which quantity, and its marks are not readable in the extracted text. Bootstrap, 10,000\n    resamples of sessions, percentile interval (a standard choice). Readings, (c-a) the intervals\n    of danger minus safety and uncertainty minus safety exclude zero; (c-b) the intervals of danger\n    minus uncertainty and uncertainty minus safety exclude zero; (c-c) the interval of each cue's\n    suppression ratio excludes zero for danger and uncertainty. Rats 4 and 6 (2 and 1 sessions)\n    give no usable interval and are reported by their means. Reproduced when, under one reading,\n    every rat with at least 3 sessions meets it; partially reproduced for at least 6 of those 8.\n- id: units-sessions-subjects\n  statement: 1812 single units were isolated and held over 73 one-hour sessions from ten rats,\n    965 of them from the four females, with per-subject totals of 192, 328, 141, 32, 52, 43, 116,\n    195, 409 and 304 units (subjects 1 to 10).\n  source: Results, paragraph 1; Supplementary Tables 1 and 2\n  quote: We isolated and held 1812 neurons during 73, 1-h recording sessions (965 neurons from the 4\n    females, Supplementary Table S1 )\n  expected:\n  - quantity: single units\n    value: 1812\n    tolerance: 0\n  - quantity: units from female rats\n    value: 965\n    tolerance: 0\n  - quantity: recording sessions\n    value: 73\n    tolerance: 0\n  - quantity: units from subject 1\n    value: 192\n    tolerance: 0\n  - quantity: units from subject 2\n    value: 328\n    tolerance: 0\n  - quantity: units from subject 3\n    value: 141\n    tolerance: 0\n  - quantity: units from subject 4\n    value: 32\n    tolerance: 0\n  - quantity: units from subject 5\n    value: 52\n    tolerance: 0\n  - quantity: units from subject 6\n    value: 43\n    tolerance: 0\n  - quantity: units from subject 7\n    value: 116\n    tolerance: 0\n  - quantity: units from subject 8\n    value: 195\n    tolerance: 0\n  - quantity: units from subject 9\n    value: 409\n    tolerance: 0\n  - quantity: units from subject 10\n    value: 304\n    tolerance: 0\n  criterion: Counts of units, of distinct recording sessions (animal and date in the unit\n    identifier) and of units per animal, with animal sex from Supplementary Table 1. Tolerance 0, as\n    these are counts of a deposited set. How the data set's animal identifiers map to subjects 1 to\n    10 is not given; per-subject totals are compared as a multiset when they cannot be mapped.\n    Sessions are counted both as 73 (Results) and against Supplementary Table 1's 75.\n- id: fig1e-regions\n  statement: The units spanned 21 brainstem regions, from the deep gray layer of the superior\n    colliculus to the median raphe, with the largest counts in the paramedian raphe (236),\n    ventral dorsal raphe (208) and dorsolateral periaqueductal gray (179).\n  source: Results, paragraph 1; Figure 1d and 1e; Supplementary Table 2; Source Data Fig. 3e left\n  quote: Neurons spanned 21 brainstem regions 13 (Fig. 1d ), including subregions and neighboring\n    regions of the superior colliculus, periaqueductal gray, dorsal raphe, and median raphe\n  expected:\n  - quantity: regions with units\n    value: 21\n    tolerance: 0\n  - quantity: units in PMnR (Source Data Fig. 3e left, sum of rows)\n    value: 236\n    tolerance: 23.6\n  - quantity: units in DRV\n    value: 208\n    tolerance: 20.8\n  - quantity: units in DLPAG\n    value: 179\n    tolerance: 17.9\n  - quantity: units in VLPAG\n    value: 147\n    tolerance: 14.7\n  - quantity: units in DPG\n    value: 145\n    tolerance: 14.5\n  criterion: Count of units per region label. Per-region counts are the sums of the two rows of\n    Source Data Fig. 3e left, which agree with the row totals of Supplementary Table 2 except Pa4\n    and x/scp (17 and 38 there, 21 and 34 in the table's extracted cells). Reproduced when 21\n    regions hold units and the five counts are within tolerance.\n- id: fig2b-cue-clusters\n  statement: K-means clustering of cue firing organized brainstem neurons into at least 21\n    functional clusters, of sizes from 24 to 219 (median 83).\n  source: Results, Brainstem cue firing, paragraph 1; Figure 2b; Supplementary Methods, K-means\n    clustering\n  quote: K-means clustering for mean, single-unit firing in 1-s bins from 2-s prior to 2-s\n    following cue presentation (danger, uncertainty, and safety) revealed neurons could be organized\n    into at least 21 functional clusters ... Cluster size varied (min size = 24, max = 219, and\n    median = 83)\n  expected:\n  - quantity: smallest cue cluster\n    value: 24\n    tolerance: 2.4\n  - quantity: largest cue cluster\n    value: 219\n    tolerance: 21.9\n  - quantity: median cue cluster size\n    value: 83\n    tolerance: 8.3\n  criterion: Shared method (cue matrix, k-means, L2) with 21 clusters. The paper's choice of 21 was\n    by inspection and is taken as given; the mean squared distance for 1 to 25 clusters is\n    reported. Reproduced when the median over seeds of the smallest, largest and median cluster\n    sizes are all within tolerance; partially reproduced when two are.\n- id: fig2c-cue-pc1-ordered\n  statement: Across all 1812 neurons, the first principal component of cue firing (29.7% of firing\n    variance) was ordered cue firing, danger > uncertainty > safety.\n  source: Results, Brainstem cue firing, paragraph 1; Figure 2c inset\n  quote: Principal component analysis (PCA) revealed ordered cue firing (danger > uncertainty >\n    safety) to be the primary low-dimensional feature across all brainstem neurons (PC1, explaining\n    29.7% of firing variance\n  expected:\n    quantity: variance explained by PC1 of cue firing\n    value: 29.7\n    tolerance: 2.97\n    unit: percent\n  criterion: PCA of the 1812 x 42 cue matrix (shared method). PC1 oriented so its mean weight over\n    the 10 danger cue intervals is positive. Reproduced when the variance explained is within\n    tolerance and the mean PC1 weight over the 10 cue intervals is ordered danger > uncertainty >\n    safety; partially reproduced when the order holds and the variance is out of tolerance.\n- id: fig2c-pc1-contribution\n  statement: PC1 firing information originated from nine clusters (k1 to k9), a minority of\n    neurons (505 of 1812, 27.9%), with k1 and k2 contributing most per unit.\n  source: Results, Brainstem cue firing, paragraphs 2 and 3; Figure 2c; Source Data Fig. 2c\n  quote: PC1 firing information originated from nine clusters (k1–k9; Fig. 2c and Supplementary\n    Fig. S5 ) composed of a minority of neurons (505/1812, 27.9%)\n  depends_on:\n  - fig2c-cue-pc1-ordered\n  expected:\n  - quantity: neurons in the nine clusters contributing most to PC1\n    value: 505\n    tolerance: 50.5\n  - quantity: PC1 contribution per unit of k1 (Source Data Fig. 2c)\n    value: 0.121\n    tolerance: 0.012\n    unit: percent variance per neuron\n  - quantity: PC1 contribution per unit of k2 (Source Data Fig. 2c)\n    value: 0.113\n    tolerance: 0.011\n    unit: percent variance per neuron\n  criterion: Per cluster, its members' rows of the cue matrix shuffled (readings s-a, s-b), PCA,\n    and the drop in PC1 variance explained from the intact 29.7% averaged over 1000 iterations,\n    divided by the cluster's size (Results; Supplementary Methods, PCA). Under L1, reproduced when\n    the nine largest contributions per unit are those of k1 to k9 and k1 and k2 are the two\n    largest, and the k1 and k2 values are within tolerance; partially reproduced when at most two\n    clusters are out of place. Under L2, the nine clusters with the largest contributions must\n    hold a total within the tolerance of 505. The reading that reproduces the Source Data values\n    is reported.\n- id: fig2d-danger-latency\n  statement: Clusters k1 to k9 showed shorter firing latencies after danger onset, and across all\n    21 clusters danger firing latency correlated negatively with the magnitude of PC1 contribution\n    (R2 = 0.41, p = 0.0017).\n  source: Results, Brainstem cue firing, paragraph 3; Figure 2d; Supplementary Methods, Danger\n    firing latency\n  quote: Clusters k1–k9 showed shorter firing latencies following danger onset, and across all\n    clusters, danger firing latency negatively correlated with the magnitude of PC1 contribution (\n    R 2 = 0.41, p = 0.0017; Fig. 2d )\n  depends_on:\n  - fig2c-pc1-contribution\n  statistics:\n  - test: linear correlation across clusters\n    statistic: R2 = 0.41\n    p: 0.0017\n    n: 21 cue clusters\n  expected:\n    quantity: R2 between cluster mean danger latency and PC1 contribution\n    value: 0.41\n    tolerance: 0.041\n  criterion: Per unit, mean normalized danger firing over the 10-s cue in 10,000 1-ms bins, latency\n    = the bin of greatest change found by MATLAB findchangepts with its defaults (one change point\n    in the mean); the cluster's latency is the mean over its units (Supplementary Methods). Open,\n    (l-a) normalized 1-ms firing built from spike times with the unit's z-score parameters, or (l-b)\n    the 250-ms normalized firing repeated into 1-ms bins; and which units carry no latency (Source\n    Data Fig. 2d lists 1498 of 1812 units; a unit with no change point, such as one silent during\n    danger, is left out). The contribution is read as (c-a) per unit (Results) or (c-b) the\n    cluster total; on the paper's Source Data values (c-a) gives R2 = 0.51 and (c-b) 0.39.\n    Reproduced when, under one reading, the correlation is negative with p < 0.05, R2 within\n    tolerance, and the mean latency of k1 to k9 units is below that of k10 to k21 units; partially\n    reproduced when negative and significant with R2 out of tolerance.\n- id: fig2e-cue-subnetwork\n  statement: Clusters k1 to k9 separated from the rest by cluster-cluster cue firing correlations,\n    forming a functional subnetwork within the larger brainstem network, with k3 the exception\n    showing weak correlations with its fellow clusters.\n  source: Results, Brainstem cue firing, paragraph 3; Figure 2e; Supplementary Methods, Correlated\n    cluster firing\n  quote: Clusters k1–k9 further separated themselves based on cluster-cluster cue firing\n    correlations (Fig. 2e and Supplementary Fig. S5 ), forming a functional subnetwork within the\n    larger brainstem network. An exception was k3, which showed weak firing correlations with fellow\n    clusters.\n  depends_on:\n  - fig2c-pc1-contribution\n  criterion: Pearson correlation between every pair of cluster mean cue profiles. The Methods give\n    36 columns (12 1-s intervals per cue, 2 s pre-cue through the 10-s cue) and Source Data Fig. 2e\n    holds 42 (14 per cue); both are run, and r and r squared both reported (the Methods write\n    \"Pearson's correlation coefficient (R2)\"). No test is given. Reproduced when the mean\n    correlation among the 36 pairs of k1 to k9 exceeds the mean correlation of k1 to k9 with k10\n    to k21, and k3 has the lowest mean correlation with the other eight subnetwork clusters;\n    partially reproduced when only the first holds.\n- id: fig2f-cue-hubs\n  statement: K1 and k2 were hubs of the cue subnetwork, with the greatest PC1 contributions, short\n    danger latencies, and single-unit firing that correlated most strongly with the mean cue firing\n    of their fellow subnetwork clusters.\n  source: Results, Brainstem cue firing, paragraph 3; Figure 2f; Supplementary Methods, Hub\n    identification with single unit x cluster correlations; Source Data Fig. 2f\n  quote: K1 and k2 neurons showed indicators of a subnetwork hub ... Furthermore, k1 and k2\n    single-unit firing correlated most strongly with mean cue firing of their fellow subnetwork\n    clusters\n  depends_on:\n  - fig2c-pc1-contribution\n  statistics:\n  - test: two-tailed independent samples t-test (means) and Levene's test (variances), between\n      clusters\n    p: 0.007\n    p_relation: \"<\"\n    corrected: Bonferroni (0.05/7)\n    n: 505 cue subnetwork units\n  expected:\n  - quantity: mean unit x cluster correlation of k1 (Source Data Fig. 2f)\n    value: 0.424\n    tolerance: 0.042\n  - quantity: mean unit x cluster correlation of k2 (Source Data Fig. 2f)\n    value: 0.466\n    tolerance: 0.047\n  criterion: For each unit of k1 to k9, its danger firing over 14 1-s intervals (from 2 s pre-cue)\n    correlated with the mean danger firing of each other subnetwork cluster, and the coefficients\n    averaged (Supplementary Methods). The Methods say seven other clusters and a threshold of\n    0.05/7; with nine clusters there are eight, so thresholds 0.05/7 and 0.05/8 are both run, and\n    the Methods' eight-cluster subnetwork is a variant. Reproduced when k1 and k2 have the two\n    highest mean coefficients, each within tolerance, and each exceeds every one of k3 to k9 by\n    t-test at the threshold; partially reproduced when they are the two highest and not all tests\n    pass. Levene's tests for lower variance are reported.\n- id: fig2g-cue-anatomy\n  statement: Neurons of every cue cluster were found in at least six brainstem regions, and\n    subnetwork neurons, including the k1 and k2 hubs, were concentrated in the deep layer of the\n    superior colliculus and the subdivisions of the periaqueductal gray.\n  source: Results, Brainstem cue firing, paragraph 3; Figure 2g\n  quote: Neurons from each cluster were observed in at least six brainstem regions (Fig. 2g ).\n    Subnetwork neurons ... were concentrated in the deep layer of the superior colliculus and\n    subdivisions of the periaqueductal gray.\n  depends_on:\n  - fig2c-pc1-contribution\n  criterion: Count of regions holding at least one unit, per cluster. \"Concentrated\" has no measure\n    in the paper; it is read as the proportion of units in DPG, DpWh, DLPAG, LPAG and VLPAG being\n    higher for the subnetwork than for the supranetwork (on Source Data Fig. 3e left, 46% against\n    34%), and the same for k1 and k2 together. Reproduced when all 21 clusters span at least six\n    regions and both proportions are higher; partially reproduced when one part holds.\n- id: fig3a-cluster-signals\n  statement: Linear regression revealed distinct threat probability and fear behaviour signals\n    across the 21 cue clusters, varying in time, with greatest signaling at onset (k5), at offset\n    (k15), sustained over the cue (k10), or peaking mid cue (k6).\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 1; Figure 3a\n  quote: Linear regression revealed unique fear behavior and threat probability signaling across\n    the 21 clusters (Fig. 3a ). Clusters showed considerable temporal variation in signaling prior\n    to and following cue presentation, characterized by greatest signaling at onset (e.g., k5),\n    offset (e.g., k15), sustained over cue presentation (e.g., k10), or even U-shaped signaling\n    peaking mid cue (e.g., k6).\n  data: with_labels\n  depends_on:\n  - source-data-cluster-link\n  criterion: Regression as in the shared method (readings r-a, r-b, i-a, i-b), under L1. The shapes\n    have no measure in the paper; read on the larger of the two betas in absolute value per 1-s\n    interval. Onset (k5), the maximum in the first cue second; offset (k15), the maximum in the\n    last cue second or the first second after the cue; sustained (k10), every cue second at least\n    half of the maximum; mid-cue peak (k6), the maximum in cue seconds 3 to 8 and both the first\n    and the last cue second below it by at least half. Reproduced when all four hold under one\n    reading; partially reproduced for two or three. Source Data's \"Figure 3a\" sheets repeat the\n    Fig. 2b firing rows and give no betas.\n- id: fig3b-signal-pca\n  statement: PCA of cluster beta weights showed PC1 (62.7% of signaling variance) to be a sustained\n    behaviour signal peaking mid cue with lesser, opposing threat probability signaling, and PC2\n    (26.12%) a sustained threat probability signal peaking early in the cue with lesser behaviour\n    signaling.\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 2; Figure 3b;\n    Source Data Fig. 3b\n  quote: PC1 reflected a sustained behavior signal that peaked mid cue presentation, with lesser and\n    opposing threat probability signaling (62.7% of signaling variance; Fig. 3b , middle). PC2\n    reflected a sustained threat probability signal that peaked during early cue presentation, with\n    lesser behavior signaling (26.12% of signaling variance\n  expected:\n  - quantity: variance explained by PC1 of cue beta weights\n    value: 62.7\n    tolerance: 6.27\n    unit: percent\n  - quantity: variance explained by PC2 of cue beta weights\n    value: 26.12\n    tolerance: 2.61\n    unit: percent\n  criterion: PCA of the 21 x 28 matrix of cluster betas (columns 1-14 probability, 15-28 behaviour;\n    shared method, regression and PCA), first on the paper's own matrix in Source Data Fig. 3b\n    middle, then on the recomputed one (L1 and L2). PC1 oriented so its mean behaviour weight over\n    the 10 cue seconds is positive, PC2 so its mean probability weight is positive. Reproduced when\n    both percentages are within tolerance and the shapes hold; PC1 mean absolute behaviour weight\n    over the cue above the probability weight, its behaviour maximum in cue seconds 3 to 8, and\n    its mean probability weight negative; PC2 mean absolute probability weight above the\n    behaviour weight, with its probability maximum in cue seconds 1 to 3. Partially reproduced\n    when the shapes hold and a percentage is out of tolerance.\n- id: fig3c-subnetwork-lesion\n  statement: Lesioning (shuffling) the cue subnetwork left the sustained behaviour signal intact\n    but reduced threat probability signaling, most at cue onset, so sustained threat probability\n    signaling depended more on the subnetwork.\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 4; Figure 3c\n  quote: Lesioning the subnetwork left sustained behavior signaling intact (Fig. 3c , PC1, middle),\n    but reduced threat probability signaling, most apparent at cue onset (Fig. 3c , PC2, bottom).\n  depends_on:\n  - fig3b-signal-pca\n  criterion: Betas of k1 to k9 shuffled (s-a, s-b), PCA, PC1 and PC2 weights averaged over 1000\n    iterations with sign alignment (shared method); the Methods' clusters 1-8 is a variant. The\n    paper gives no measure. Reproduced when the mean PC1 behaviour weight over the 10 cue seconds\n    after this lesion is at least 75% of the intact value (a choice, for \"intact\") and above that\n    after the supranetwork lesion, and the PC2 probability weight in the first cue second is below\n    the intact PC2 value; partially reproduced when one of the two holds.\n- id: fig3d-supranetwork-lesion\n  statement: Lesioning the cue supranetwork diminished the sustained behaviour signal and turned the\n    sustained threat probability signal into a dynamic probability-to-behaviour signal, so\n    sustained behaviour signaling depended more on the supranetwork.\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 4; Figure 3d\n  quote: By contrast, lesioning the supranetwork diminished sustained behavior signaling (Fig. 3d ,\n    PC1, middle), and shifted sustained threat probability signaling to dynamic,\n    probability-to-behavior signaling (Fig. 3d , PC2, bottom).\n  depends_on:\n  - fig3b-signal-pca\n  criterion: As fig3c-subnetwork-lesion, with k10 to k21 shuffled. The paper gives no measure.\n    Reproduced when the mean PC1 behaviour weight over the 10 cue seconds is below the intact value\n    and PC2's probability weights peak (in absolute value) in the first half of the cue while its\n    behaviour weights peak in the second half; partially reproduced when one holds.\n- id: fig3e-network-anatomy\n  statement: Subnetwork and supranetwork neurons were distributed throughout the brainstem, with\n    subtle biases only for the subnetwork, to which the deep layer of the superior colliculus and\n    the lateral periaqueductal gray contributed more.\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 4; Figure 3e;\n    Source Data Fig. 3e right\n  quote: Subtle anatomical biases were only apparent for the cue subnetwork (Fig. 3e ), with the\n    deep layer of the superior colliculus and the lateral subdivision of the periaqueductal gray\n    (also sources of hub neurons) contributing more to the cue subnetwork.\n  depends_on:\n  - fig2c-pc1-contribution\n  expected:\n  - quantity: differential subnetwork composition of DPG (Source Data Fig. 3e right)\n    value: 5.93\n    tolerance: 0.59\n    unit: percentage points\n  - quantity: differential subnetwork composition of LPAG (Source Data Fig. 3e right)\n    value: 7.41\n    tolerance: 0.74\n    unit: percentage points\n  criterion: Differential composition per region (shared method, mapping) for k1 to k9 against the\n    overall 27.9%. No test is given. Reproduced when DPG and LPAG have the two largest positive\n    differentials and both are within tolerance (L1) or, under L2, both are the two largest;\n    partially reproduced when both are positive and among the four largest.\n- id: fig4b-outcome-clusters\n  statement: K-means clustering of mean post-shock firing for the four trial types organized\n    brainstem neurons into at least 11 functional clusters, of sizes from 46 to 322 (median 169).\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 5; Figure 4b;\n    Supplementary Methods, K-means clustering\n  quote: K-means clustering for mean post-shock firing (4 trial types: danger, uncertainty shock,\n    uncertainty omission, and safety) revealed brainstem neurons could be organized into at least 11\n    functional clusters (min size = 46, max = 322, and median = 169\n  expected:\n  - quantity: smallest outcome cluster\n    value: 46\n    tolerance: 4.6\n  - quantity: largest outcome cluster\n    value: 322\n    tolerance: 32.2\n  - quantity: median outcome cluster size\n    value: 169\n    tolerance: 16.9\n  criterion: Shared method (outcome matrix, k-means, L2) with 11 clusters; the mean squared distance\n    for 1 to 20 clusters is reported. Reproduced when the median over seeds of the smallest,\n    largest and median sizes are all within tolerance; partially reproduced when two are.\n- id: fig4c-positive-prediction-error\n  statement: PCA of post-shock firing of all 1812 neurons showed positive prediction error on top\n    of shock responding as PC1 (17.7% of firing variance), with a larger weight for surprising shock\n    on uncertainty trials than for predicted shock on danger trials, and no opposing negative error\n    for surprising omission.\n  source: Results, Brainstem threat probability and behavior signaling, paragraph 5; Figure 4c\n  quote: PCA for mean post-shock firing of all 1812 brainstem neurons revealed positive prediction\n    error, on top of shock responding, to be the primary low-dimensional feature (PC1 explains 17.7%\n    of firing variance ... The prediction error is \"positive\" because the PC1 weight for surprising\n    shock delivery (on uncertainty trials) exceeded the PC1 weight for predicted shock (on danger\n    trials). The prediction error is not \"signed\" because it did not include an opposing, negative\n    error\n  expected:\n    quantity: variance explained by PC1 of outcome firing\n    value: 17.7\n    tolerance: 1.77\n    unit: percent\n  criterion: PCA of the 1812 x 80 outcome matrix (shared method), PC1 oriented so its mean\n    uncertainty shock weight is positive. Weights compared as means over the 20 intervals.\n    Reproduced when the variance is within tolerance, the uncertainty shock weight exceeds the\n    danger weight, the danger weight exceeds the safety weight (shock responding), and the\n    uncertainty omission weight is not below the safety weight; partially reproduced when the\n    weight relations hold and the variance is out of tolerance.\n- id: fig4b-phasic-network\n  statement: Outcome clusters k1 to k3 showed phasic firing changes after shock (k1 the greatest\n    increases to surprising shock, k2 to predicted shock, k3 suppressed regardless of trial type)\n    and by their correlations formed a phasic outcome network.\n  source: Results, Brainstem outcome firing, paragraph 1; Figure 4b and 4d\n  quote: K1 neurons showed the greatest, phasic firing increases to surprising shock, and k2\n    neurons greatest, phasic firing increases to predicted shock, while k3 neurons physically\n    suppressed firing following shock irrespective of trial type (Fig. 4b , left column).\n    Cluster-cluster firing correlations revealed k1–k3 formed a phasic outcome network\n  data: with_labels\n  depends_on:\n  - source-data-cluster-link\n  criterion: Under L1 (and L2 matched to it), cluster mean outcome profiles. Phasic, the Methods'\n    temporal index, |mean normalized firing in the 1 s after shock offset minus that over 5 s|,\n    averaged over danger and uncertainty shock (Supplementary Methods, Determining temporal firing\n    pattern); k1 to k3 must have the three highest indices of the 11 clusters. Profiles, in the\n    first 1 s, k1 uncertainty shock > danger > 0; k2 danger > uncertainty shock > 0; k3 below 0 on\n    both. Network, the mean pairwise Pearson correlation of 80-value cluster profiles among k1 to\n    k3 above their mean correlation with k4 to k11. Reproduced when all hold; partially\n    reproduced when the profiles hold and one other part fails.\n- id: fig4b-tonic-network\n  statement: Outcome clusters k6 to k9 showed sustained firing changes after surprising shock (k6\n    selectively inhibited, k7 and k8 sustained increases maximal to surprising shock) and by their\n    correlations formed a tonic outcome network.\n  source: Results, Brainstem outcome firing, paragraph 1; Figure 4b and 4d\n  quote: K6–k9 neurons showed sustained firing changes following surprising shock (Fig. 4b , right\n    column). K6 neurons selectively inhibited firing to surprising shock, while k7 and k8 neurons\n    showed sustained firing increases that were maximal to surprising shock. Cluster-cluster firing\n    correlations revealed k6–k9 formed a tonic outcome network\n  data: with_labels\n  depends_on:\n  - source-data-cluster-link\n  criterion: Under L1, means over the 10 s after shock offset. K6, uncertainty shock below 0 and\n    below each other trial type; k7 and k8, uncertainty shock above 0 and above each other trial\n    type, with the mean over seconds 5 to 10 above half of the mean over the first second\n    (sustained, a choice); network, the mean pairwise correlation among k6 to k9 above their mean\n    correlation with the other seven clusters. Reproduced when all hold; partially reproduced when\n    the k6 to k8 profiles hold and the network part fails.\n- id: fig4e-network-pca\n  statement: Within the phasic outcome network, PC1 (37.0% of firing variance) was equivalent phasic\n    shock firing on danger and uncertainty trials; within the tonic outcome network, PC1 (29.2%)\n    was selective firing to surprising shock with opposing firing to safety.\n  source: Results, Brainstem outcome firing, paragraph 2; Figure 4e\n  quote: Network-specific PCA for post-shock firing revealed equivalent and phasic shock firing on\n    danger and uncertainty trials to be the primary low-dimensional feature of the phasic outcome\n    network (explaining 37.0% of firing variance; Fig. 4e , left). PCA further revealed selective\n    firing to surprising shock, and opposing firing to safety, to be the primary low-dimensional\n    feature of the tonic outcome network (explaining 29.2% of firing variance\n  depends_on:\n  - fig4b-phasic-network\n  - fig4b-tonic-network\n  expected:\n  - quantity: variance explained by PC1 of the phasic network\n    value: 37.0\n    tolerance: 3.7\n    unit: percent\n  - quantity: variance explained by PC1 of the tonic network\n    value: 29.2\n    tolerance: 2.92\n    unit: percent\n  criterion: PCA of the outcome rows of the 265 phasic (k1 to k3; Source Data Fig. 4e left has 265\n    rows) and the 613 tonic units. Phasic PC1, oriented so its danger weight in the first second\n    is positive; its danger and uncertainty shock weights in the first second both exceed twice\n    their means over seconds 5 to 10, and differ from each other by less than either differs from\n    safety. Tonic PC1, oriented so its uncertainty shock mean is positive; uncertainty shock has\n    the largest mean of the four types and safety a negative mean. The factors (twice, means) are\n    choices, as the paper gives none. Reproduced when both percentages are within tolerance and\n    both shapes hold; partially reproduced when the shapes hold.\n- id: fig4f-outcome-hubs\n  statement: In the phasic outcome network, k1 and k2 single-unit firing correlated better with the\n    population firing of their fellow clusters than k3 did; in the tonic network, k6, the cluster\n    decreasing firing to surprising shock, was the hub, correlating most strongly with its fellow\n    clusters.\n  source: Results, Brainstem outcome firing, paragraph 3; Figure 4f; Supplementary Methods, Hub\n    identification\n  quote: Within the phasic outcome network, k1 and k2 single-unit firing was better correlated with\n    population firing of their fellow network clusters than were k3 neurons (Fig. 4f , left) ...\n    K6 neurons were a hub for the tonic outcome network. K6 neuron firing, the cluster decreasing\n    firing to surprising shock, correlated most strongly with population firing of their fellow\n    tonic outcome clusters\n  data: with_labels\n  depends_on:\n  - fig4b-phasic-network\n  - fig4b-tonic-network\n  statistics:\n  - test: two-tailed independent samples t-test and Levene's test, between clusters\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 265 phasic and 613 tonic units\n  criterion: Per unit, its 80-value outcome row correlated with the mean rows of each other cluster\n    of its network, averaged (Supplementary Methods; the Methods' phasic clusters 1-5 and tonic\n    7-10 are variants). Bonferroni threshold 0.05 divided by the number of between-cluster tests\n    within the network (the paper gives 0.05/7 only for the cue). Reproduced when k1 and k2 each\n    exceed k3 by t-test, and k6 has the highest mean, above each of k7 to k9 by t-test; partially\n    reproduced when the orderings hold without all tests passing. Levene's tests reported.\n- id: fig4g-outcome-anatomy\n  statement: Phasic outcome neurons were more common at the axis extremes (periaqueductal gray\n    subregions, dorsal raphe and paramedian raphe), while tonic outcome neurons, most strikingly the\n    k6 hub, were distributed throughout the brainstem.\n  source: Results, Brainstem outcome firing, paragraph 3; Figure 4g\n  quote: Phasic outcome neurons were more common at axis extremes ... Tonic outcome neurons were\n    distributed throughout the brainstem, a pattern most striking for k6 hub neurons.\n  depends_on:\n  - fig4b-phasic-network\n  - fig4b-tonic-network\n  criterion: The paper gives no measure or test. Read as, the fraction of phasic units in DLPAG,\n    LPAG, VLPAG, DRL, DRD, DRV, PDR and PMnR exceeds the tonic fraction (on Source Data Fig. 4g\n    and the L1 sizes, 0.600 against 0.594), and the tonic network spans at least as many regions\n    as the phasic network. The number of regions holding k6 units is reported beside the other\n    clusters' (17, against 10 to 19, on Source Data Fig. 4g). Reproduced when both conditions\n    hold; not reproduced otherwise. As the paper's own values differ little, the effect size is\n    reported in any case.\n- id: fig5a-outcome-cluster-signals\n  statement: Regression revealed distinct shock and prediction error signals across the 11 outcome\n    clusters; k1 neurons transiently signaled both sensory shock and prediction error, while k6\n    neurons signaled only error.\n  source: Results, Brainstem outcome firing, paragraph 4; Figure 5a\n  quote: First, cluster-specific linear regression revealed unique shock and prediction error\n    signals across the 11 outcome clusters (Fig. 5a ). For example, k1 neurons transiently signaled\n    both sensory shock and prediction error, while k6 neurons exclusively signaled error.\n  data: with_labels\n  depends_on:\n  - source-data-cluster-link\n  criterion: Outcome regression (shared method, readings r-a, r-b, i-a, i-b) under L1. K1, both\n    betas reach their largest absolute values in the first 2 s after shock offset and fall below\n    half of that by seconds 5 to 10 (transient, a choice); k6, the mean absolute prediction error\n    beta over the 10 s at least twice the mean absolute shock beta (exclusive, a choice).\n    Reproduced when both hold under one reading; partially reproduced when one does.\n- id: fig5b-outcome-signal-pca\n  statement: PCA of outcome cluster beta weights showed opposing sensory shock and prediction error\n    signals as PC1 (53.7% of signaling variance) and dynamic sensory shock to prediction error\n    signaling as PC2 (33.4%).\n  source: Results, Brainstem outcome firing, paragraph 4; Figure 5b; Source Data Fig. 5b\n  quote: PCA for shock and prediction error beta coefficients across all clusters (therefore all\n    brainstem neurons) revealed opposing sensory shock and prediction error signals to be the\n    primary low-dimensional feature (PC1, 53.7% of signaling variance; Fig. 5b , middle). PC2\n    reflected dynamic, sensory shock to prediction error signaling (33.4% of signaling variance\n  expected:\n  - quantity: variance explained by PC1 of outcome beta weights\n    value: 53.7\n    tolerance: 5.37\n    unit: percent\n  - quantity: variance explained by PC2 of outcome beta weights\n    value: 33.4\n    tolerance: 3.34\n    unit: percent\n  criterion: PCA of the 11 x 40 matrix of outcome cluster betas (columns 1-20 shock, 21-40\n    prediction error; the Methods' \"21-cluster\" is a slip for 11), first on the paper's matrix\n    from Source Data Fig. 5b middle, then recomputed (L1, L2). PC1 opposing, its mean shock weight\n    and mean prediction error weight over the 20 intervals of opposite sign. PC2 dynamic, its\n    shock weights peak (in absolute value) in the first 2 s and its prediction error weights after\n    the first 2 s. Reproduced when both percentages are within tolerance and both shapes hold;\n    partially reproduced when the shapes hold.\n- id: fig5c-phasic-lesion\n  statement: Lesioning the phasic outcome network left signaling dominated by sustained prediction\n    error (80.0% of signaling variance), with residual sustained shock (16.8%), so rapid sensory\n    shock signaling depended on the phasic network.\n  source: Results, Brainstem prediction error and shock signaling, paragraph 1; Figure 5c\n  quote: Lesioning the phasic outcome network (using a PCA lesion approach identical to the cue\n    networks) left signaling dominated by sustained prediction error (80.0% of signaling variance;\n    Fig. 5c , middle), while the residual reflected sustained shock (16.8% of signaling variance\n  depends_on:\n  - fig5b-outcome-signal-pca\n  expected:\n  - quantity: variance explained by PC1 after the phasic lesion\n    value: 80.0\n    tolerance: 8.0\n    unit: percent\n  - quantity: variance explained by PC2 after the phasic lesion\n    value: 16.8\n    tolerance: 1.68\n    unit: percent\n  criterion: Betas of the phasic clusters shuffled (readings p-a, p-b, s-a, s-b), PCA, percent\n    variance and weights averaged over 1000 iterations (shared method). PC1, mean absolute\n    prediction error weight above the shock weight, with every interval from 1 to 10 s at least\n    half its maximum (sustained, a choice); PC2, mean absolute shock weight above the prediction\n    error weight. Reproduced when both percentages are within tolerance and both shapes hold under\n    one reading; partially reproduced when the shapes hold.\n- id: fig5d-tonic-lesion\n  statement: Lesioning the tonic outcome network left opposing, phasic sensory shock and prediction\n    error signaling as PC1 (61.3% of signaling variance) and dynamic sensory shock to prediction\n    error as PC2 (29.8%), similar to that of all neurons.\n  source: Results, Brainstem prediction error and shock signaling, paragraph 1; Figure 5d\n  quote: By contrast, lesioning the tonic outcome network emphasized opposing, phasic sensory shock\n    and prediction error signaling (61.3% of signaling variance; Fig. 5d , middle). Residual\n    signaling reflected dynamic, sensory shock to prediction error (29.8% of signaling variance\n  depends_on:\n  - fig5b-outcome-signal-pca\n  expected:\n  - quantity: variance explained by PC1 after the tonic lesion\n    value: 61.3\n    tolerance: 6.13\n    unit: percent\n  - quantity: variance explained by PC2 after the tonic lesion\n    value: 29.8\n    tolerance: 2.98\n    unit: percent\n  criterion: Betas of k6 to k9 shuffled (s-a, s-b; the Methods' 7-10 a variant). PC1, mean shock and\n    prediction error weights of opposite sign, both with their largest absolute values in the first\n    2 s (phasic); PC2, as fig5b's PC2 shape, and its Pearson correlation with the intact PC2 above\n    0.5 (similar, a choice). Reproduced when both percentages are within tolerance and the shapes\n    hold; partially reproduced when the shapes hold.\n- id: fig5e-no-anatomical-bias\n  statement: Anatomical biases for phasic and tonic outcome network neurons were absent.\n  source: Results, Brainstem prediction error and shock signaling, paragraph 1; Figure 5e; Source\n    Data Fig. 5e\n  quote: Anatomical biases for phasic and tonic outcome network neurons were absent (Fig. 5e ).\n  depends_on:\n  - fig4b-phasic-network\n  - fig4b-tonic-network\n  criterion: A claim of absence with no test in the paper. Differential composition per region\n    (shared method, mapping) of phasic (p-a, p-b) against tonic units. With no paper threshold,\n    the claim is judged against the paper's own figures; reproduced when no region differs by more\n    than the largest absolute differential of Source Data Fig. 5e right (4.48 percentage points,\n    MnR), and not reproduced when any does by more than 1.5 times that. A chi-square test of\n    region x network is shown as a variant, not as the judge.\n- id: cue-outcome-membership-independent\n  statement: Membership in cue networks did not influence membership in outcome networks; neither\n    the phasic (85/265, 32.1%) nor the tonic (159/613, 25.9%) outcome neurons differed from the\n    27.9% expected in the cue subnetwork.\n  source: Results, Brainstem prediction error and shock signaling, paragraph 2; Supplementary\n    Methods, Relationship between cue network and outcome network membership\n  quote: Chi-squared testing found neither the phasic outcome neurons (85/265, 32.1%; χ 2 = 2.27, p\n    = 0.13) nor the tonic outcome neurons (159/613, 25.9%; χ 2 = 1.17, p = 0.28) differed from the\n    expected proportion of 27.9%.\n  depends_on:\n  - fig2c-pc1-contribution\n  - fig4b-phasic-network\n  - fig4b-tonic-network\n  statistics:\n  - about: phasic outcome units in the cue subnetwork against 27.9%\n    test: chi-squared test\n    statistic: chi2 = 2.27\n    p: 0.13\n    n: 265 phasic outcome units\n  - about: tonic outcome units in the cue subnetwork against 27.9%\n    test: chi-squared test\n    statistic: chi2 = 1.17\n    p: 0.28\n    n: 613 tonic outcome units\n  expected:\n  - quantity: phasic outcome units in the cue subnetwork\n    value: 85\n    tolerance: 8.5\n  - quantity: tonic outcome units in the cue subnetwork\n    value: 159\n    tolerance: 15.9\n  criterion: A claim of absence, judged on the paper's test. A chi-square goodness-of-fit test,\n    1 df, no continuity correction, of the network's count in the cue subnetwork against the\n    proportion 505/1812 (the reported statistics, 2.27 and 1.17, are reproduced by this test from\n    the reported counts). Reproduced when neither test has p < 0.05; not reproduced when either\n    does. Counts, proportions and statistics are reported under L1 and L2.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/strickland-2022.yaml'; s=open(p).read()
rep={
"Results, Brainstem cue firing, paragraph 1; Figure 2b;":"Results, paragraph 2; Figure 2b;",
"Results, Brainstem cue firing, paragraph 1; Figure 2c inset":"Results, paragraph 2; Figure 2c inset",
"Results, Brainstem cue firing, paragraphs 2 and 3; Figure 2c":"Results, paragraphs 3 and 4; Figure 2c",
"Results, Brainstem cue firing, paragraph 3;":"Results, paragraph 4;",
"Results, Brainstem threat probability and behavior signaling, paragraph 1;":"Results, paragraph 5;",
"Results, Brainstem threat probability and behavior signaling, paragraph 2;":"Results, paragraph 6;",
"Results, Brainstem threat probability and behavior signaling, paragraph 4;":"Results, paragraph 8;",
"Results, Brainstem threat probability and behavior signaling, paragraph 5;":"Results, paragraph 9;",
"Results, Brainstem outcome firing, paragraph 1;":"Results, paragraph 10;",
"Results, Brainstem outcome firing, paragraph 2;":"Results, paragraph 10;",
"Results, Brainstem outcome firing, paragraph 3;":"Results, paragraph 11;",
"Results, Brainstem outcome firing, paragraph 4;":"Results, paragraph 12;",
"Results, Brainstem prediction error and shock signaling, paragraph 1;":"Results, paragraph 13;",
"Results, Brainstem prediction error and shock signaling, paragraph 2;":"Results, paragraph 14;",
}
for a,b in rep.items():
    assert a in s,a; s=s.replace(a,b)
open(p,'w').write(s)
E
grep -n "Brainstem cue firing\|Brainstem outcome\|behavior signaling\|shock signaling" claims/strickland-2022.yaml; grep -n "Results, Brainstem" claims/strickland-2022.yaml
python3 - <<'E'
import yaml,re
d=yaml.safe_load(open('claims/strickland-2022.yaml'))
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and (': ' in v): print(c['id'],k,v[:80])
E
grep -n "—\|rather" claims/strickland-2022.yaml
python3 tools/claims_check.py claims/strickland-2022.yaml paper/10.1038-s41467-022-34021-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
p='claims/strickland-2022.yaml'; s=open(p).read()
a="""  quote: K-means clustering for mean post-shock firing (4 trial types: danger, uncertainty shock,
    uncertainty omission, and safety) revealed brainstem neurons could be organized into at least 11
    functional clusters (min size = 46, max = 322, and median = 169"""
b="""  quote: K-means clustering for mean post-shock firing (4 trial types ... revealed brainstem neurons
    could be organized into at least 11 functional clusters (min size = 46, max = 322, and median =
    169"""
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
import yaml
d=yaml.safe_load(s)
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(len(d['claims']))
E
python3 tools/claims_check.py claims/strickland-2022.yaml paper/10.1038-s41467-022-34021-1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/strickland-2022.yaml'))['claims']
print(sum('expected' in c for c in d), sum('criterion' in c for c in d), sum('statistics' in c for c in d), sum(1 for c in d if c.get('kind')=='link'))"; git status --short
```

```
17 30 5 1
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
?? claims/strickland-2022.yaml
?? scripts
```

**Agent**

I've written `claims/strickland-2022.yaml`. The quote checker reports 30 claims, 29 quotes, 6 statistical values and 0 problems. Nothing was committed.

**Text read**
- **Main text:** the version of record (PMC9582012, open access, Europe PMC full-text XML): Results, Discussion, figure legends and Methods.
- **Supplement:** Supplementary Information (MOESM1) as extracted text: Supplementary Methods, the legends of Supplementary Figs 1 to 7, and Supplementary Tables 1 and 2. Table 2's columns are garbled in the extraction, but its row and subject totals are intact.
- **Source Data workbook (MOESM4):** read with a small XML parser.
- **PDF:** could not be rendered because poppler is not installed, so no figure was read as an image.
- **Data descriptor:** read only to know what the data set holds.
- **Code:** not read. The paper puts its code at CRCNS, which means inside the data set's own files, so no commit is recorded.

**Claims**
- 30 claims: 29 findings plus 1 link claim.
- 29 have quotes. The link claim has none and none is inferred.
- 5 claims carry statistics (6 tests), 17 have expected values, and all 30 have a criterion.
- The link claim checks that the data set's units can be matched to the rows of the Source Data cluster sheets. That match recovers the paper's own cluster membership, and the four claims that name individual clusters depend on it (`data: with_labels`).

**Details the paper leaves open, and the readings named**
- **Baseline subtraction:** per trial, or per trial type.
- **Z-score window:** the 50 s stated in words (200 bins), or the "240 bins" also given (60 s).
- **Trials with no pokes:** a suppression ratio of 0, or left out.
- **K-means:** no options, replicates or seed. I used MATLAB's defaults and judge on the median over 20 seeds, with the best of 20 replicates as a variant.
- **Cluster labels:** the paper's own membership from Source Data (L1), or the author's own k-means matched to the paper's clusters (L2). The Source Data show that cue clusters are numbered by PC1 contribution.
- **What is shuffled in the lesion and contribution analyses:** each row on its own, or the whole block. The sign alignment of PCs across shuffles is also unstated.
- **Regression:** on the cluster-mean firing, or per unit and then averaged; with or without an intercept. Source Data Figs 3b and 5b hold the paper's own beta matrices, so whichever reading matches them decides.
- **Suppression ANOVA:** the stated degrees of freedom F(2,142) fit a cue × sex mixed design. A plain repeated-measures ANOVA on the paper's own Source Data gives F(2,144) = 116.2, so that reading is shown but is not the main one.
- **Bootstrap contrasts in Supplementary Fig. 2:** three readings of which quantity's interval must exclude zero.
- **Latency to PC1 contribution correlation:** contribution per unit or per cluster total. On the paper's Source Data these give R² = 0.51 and 0.39, against the reported 0.41. Which units carry no latency is also open: Source Data lists 1498 of the 1812.
- **Correlation matrix width:** 36 columns (Methods) or 42 (Source Data); r or r².
- **Bonferroni divisor for hubs:** 0.05/7 (Methods) or 0.05/8 (nine clusters give eight comparisons).
- **Network membership:** the Results give subnetwork k1–k9, phasic k1–k3 and tonic k6–k9. The Supplementary Methods say clusters 1–8, 1–5 and 7–10, and Source Data Fig. 5e's "phasic" row holds 679 units, the size of k1–k5. So the phasic network for Figs 5c and 5e is read both as k1–k3 and as k1–k5.
- **Thresholds I chose:** the shape claims ("sustained", "peaking mid cue", "intact") and the anatomy claims have no measure in the paper. Each such threshold is named in its criterion as a choice. The claim that anatomical biases were absent (Fig. 5e) has no test, so it is judged against the paper's own Source Data range.

**Inconsistencies in the paper**
- Supplementary Table 1 lists 75 sessions, against 73 in the Results and in Source Data Fig. 1c.
- The Methods say "21-cluster" for the outcome beta matrix, where there are 11 clusters.
- The Source Data sheets for Fig. 3a repeat the Fig. 2b firing values and contain no beta weights.

**Missing:** nothing the claims needed is missing from the paper, apart from the unread code inside the data set. Where those scripts settle one of the open details above, the author may follow them.

## End of run

35 turns, 9 minutes, $2.94 at API prices, result: success.
