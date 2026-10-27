# figshare-24639285 · author · run 40572290491

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/06cc7bd0-50dd-4f83-bfbd-14649441af02/tool-results/b5c0bcg6j.txt

Preview (first 2KB):
Tue Oct 27 19:49:52 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/06cc7bd0-50dd-4f83-bfbd-14649441af02/tool-results/b5c0bcg6j.txt"
}
```

```
1	Tue Oct 27 19:49:52 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-12`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 618 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/figshare-24639285/ paper/ entries/001453-fouke-2025/ ; cat claims/figshare-24639285/*.yaml; grep -n -i -A40 "^## Figshare" docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/06cc7bd0-50dd-4f83-bfbd-14649441af02/tool-results/bnxlirj61.txt"
}
```

```
1	claims/figshare-24639285/:
2	10.1038-s41597-024-03626-0.yaml
3	
4	entries/001453-fouke-2025/:
5	README.md
6	entry.yaml
7	omr.py
8	reproduce_fouke_2025.ipynb
9	requirements.in
10	requirements.lock.txt
11	
12	paper/:
13	10.1038-s41597-024-03626-0.txt
14	# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,
15	# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).
16	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
17	# protocol pilot-12 as stated in docs/protocol.md (Reader).
18	#
19	# Text read: the version of record from Europe PMC (PMC11271266, full-text XML converted to text)
20	# as supplied under paper/, with Background & Summary, Methods, Data Records, Technical
[... 504 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 170,200p docs/archives.md; cat paper/*.txt | head -c 60000; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol, claims and paper. Now listing the dataset files and looking at the example entry format.

**Agent calls Bash**

```bash
curl -s https://api.figshare.com/v2/articles/24639285/versions/1 | python -c "
import json,sys; d=json.load(sys.stdin)
print(d['title'], d['version'], d['doi'], d.get('published_date'), d.get('modified_date'))
print(d['description'][:3000])
for f in d['files']: print(f['id'], f['name'], f['size'], f['computed_md5'])
"; curl -s https://api.figshare.com/v2/articles/24639285/versions
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fsspec, openpyxl, io
for fid in [43480554, 43480542, 43480551]:
    with fsspec.open(f'https://ndownloader.figshare.com/files/{fid}', block_size=2**20) as f: b=f.read()
    wb=openpyxl.load_workbook(io.BytesIO(b), data_only=True)
    print(fid, wb.sheetnames)
    for ws in wb.worksheets[:2]:
        print('==', ws.title, ws.max_row, ws.max_column)
        for r in ws.iter_rows(values_only=True): print(r)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fsspec, openpyxl, io
ModuleNotFoundError: No module named 'fsspec'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests openpyxl pandas numpy scipy matplotlib 2>&1 | tail -2; python -c "
import fsspec, openpyxl, io
for fid in [43480554, 43480542, 43480551]:
    with fsspec.open(f'https://ndownloader.figshare.com/files/{fid}', block_size=2**20) as f: b=f.read()
    wb=openpyxl.load_workbook(io.BytesIO(b), data_only=True)
    print(fid, wb.sheetnames)
    for ws in wb.worksheets[:2]:
        print('==', ws.title, ws.max_row, ws.max_column)
        for r in ws.iter_rows(values_only=True): print(r)
"
```

```
43480554 ['ss19', 'ss22', 'ss27', 'ss34', 'ss38', 'ss41', 'ss43', 'ss45', 'ss46', 'ss48', 'ss6', 'ss9', 'ss10', 'ss11', 'ss18', 'ss24', 'ss29', 'ss30', 'ss36', 'g2', 'ss8', 'ss39']
== ss19 106 17
('Sample', 'DEMAG', 'Moment(emu)', 'Dec', 'Inc', None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 0, 7.186e-08, 241.8, -13.2, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 0, 7.176e-08, 242.2, -13.7, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 0, 7.143e-08, 243.4, -13.3, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 0, 7.179e-08, 243.7, -13.6, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 0, 7.261e-08, 244.1, -12.9, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '5mT', 7.225e-08, 243.9, -18.9, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '5mT', 7.278e-08, 234.8, -18.7, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '5mT', 7.115e-08, 239.8, -16.9, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '5mT', 7.147e-08, 242, -21, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '5mT', 7.115e-08, 241.6, -20.9, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '10mT', 7.205e-08, 241.8, -16.7, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '10mT', 7.18e-08, 240.7, -14.8, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '10mT', 7.178e-08, 241.7, -16.7, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '10mT', 7.173e-08, 241.4, -136, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', '10mT', 7.165e-08, 242.2, -14.7, None, None, None, None, None, None, None, None, None, None, None, None)
('ss19', 
[... 260 more lines not kept]
```

**Agent**

The data are small (13 workbooks). M590 in Table 1 looks like the magnitude of the single 590.1 measurement. Surveying all sheets now.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, openpyxl, io, json, urllib.request, collections
d=json.load(urllib.request.urlopen('https://api.figshare.com/v2/articles/24639285/versions/1'))
for fl in d['files']:
    if not fl['name'].endswith('xlsx'): continue
    with fsspec.open(f'https://ndownloader.figshare.com/files/{fl[\"id\"]}', block_size=2**20) as f: b=f.read()
    wb=openpyxl.load_workbook(io.BytesIO(b), data_only=True)
    for ws in wb.worksheets:
        rows=list(ws.iter_rows(values_only=True))
        extra=[r for r in rows if any(v is not None for v in r[5:])]
        data=[r for r in rows[1:] if r[0] is not None and r[1] is not None]
        foot=[r[0] for r in rows[1:] if r[0] is not None and r[1] is None]
        names=set(r[0] for r in data)
        steps=collections.Counter(str(r[1]) for r in data)
        print(fl['name'], ws.title, rows[0][:5], names, 'extra cols', len(extra), 'nrows', len(data))
        print('   ', dict(steps))
        print('   foot:', [x for x in foot if 'Field' in x or 'field' in x][-1:])
"
```

```
12021g2.asc.xlsx 12021g2 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'12021g2'} extra cols 0 nrows 10
    {'0': 2, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
12021g3.asc.xlsx 12021g3 ('Sample', 'DEMAG', 'Moment (emu)', 'Dec', 'Inc') {'12021g3'} extra cols 0 nrows 10
    {'0': 2, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
14053g2.asc.xlsx Sheet1 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'14053g2'} extra cols 0 nrows 10
    {'0': 2, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
71055g3.asc.xlsx Sheet1 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'71055g3'} extra cols 0 nrows 9
    {'0': 1, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
71055g1.asc.xlsx Sheet1 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'71055g1'} extra cols 0 nrows 9
    {'0': 1, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
14053g3.asc.xlsx Sheet1 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'14053g3'} extra cols 0 nrows 11
    {'0': 2, '590': 4, '590.1': 1, '590.3': 3, '590.4': 1}
   foot: ['#.4 Field on step at 40 microTesla laboratory field']
14053g1.asc.xlsx Sheet1 ('Sample', 'DEMAG', 'Moment', 'Dec', 'Inc') {'14053g1'} extra cols 0 nrows 16
    {'0': 2, '400': 3, '400.1': 1, '400.3': 2, '590': 3, '590.1': 1, '590.3': 3, '590.4': 1}
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec, openpyxl, io
with fsspec.open('https://ndownloader.figshare.com/files/43480554', block_size=2**20) as f: b=f.read()
open('glass.xlsx','wb').write(b)
wb=openpyxl.load_workbook(io.BytesIO(b), data_only=True)
for name in ['ss48','ss6']:
  ws=wb[name]
  print('==',name, ws.max_row, ws.max_column)
  for i,r in enumerate(ws.iter_rows(values_only=True)):
     r=tuple(v for v in r)
     while r and r[-1] is None: r=r[:-1]
     print(i,r)
"
```

```
== ss48 46 10
0 ('Sample', 'DEMAG', 'CSD', 'Moment(emu)', 'Dec', 'Inc')
1 ('ss48', 0, 0, 1.5429400000000002e-07, 153.648, -46.728)
2 ('ss48', 0, 0, 1.48302e-07, 150.48, -46.256)
3 ('ss48', 0, 0, 1.4231e-07, 152.064, -47.672000000000004)
4 ('ss48', 0, 0, 1.498e-07, 155.232, -45.784)
5 ('ss48', 0, 0, 1.5429400000000002e-07, 163.15200000000002, -48.144000000000005)
6 ('ss48', '5mT', 0, 1.4602e-07, 159.15200000000002, -42.047999999999995)
7 ('ss48', '5mT', 0, 1.5049e-07, 154.28, -42.486)
8 ('ss48', '5mT', None, 1.4751e-07, 155.904, -44.238)
9 ('ss48', '5mT', None, 1.4304e-07, 159.15200000000002, -45.114)
10 ('ss48', '5mT', None, 1.5049e-07, 165.648, -44.675999999999995)
11 ('ss48', '10mT', None, 9.69e-08, 178.705, -35.083999999999996)
12 ('ss48', '10mT', None, 1.02e-07, 166.56, -34.726)
13 ('ss48', '10mT', None, 1.0098e-07, 168.295, -34.01)
14 ('ss48', '10mT', None, 9.996e-08, 171.765, -36.157999999999994)
15 ('ss48', '10mT', None, 1.0302e-07, 173.5, -34.01)
16 ('ss48', 100, None, 4.23948e-09, 159.4, -13.425999999999998)
17 ('ss48', 100, None, 4.28274e-09, 164.18200000000002, -13.837)
18 ('ss48', 100, None, 4.41252e-09, 164.18200000000002, -13.289)
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import fsspec, openpyxl, io, json, urllib.request, collections, numpy as np
d=json.load(urllib.request.urlopen('https://api.figshare.com/v2/articles/24639285/versions/1'))
sheets={}
for fl in d['files']:
    if not fl['name'].endswith('xlsx'): continue
    with fsspec.open(f'https://ndownloader.figshare.com/files/{fl["id"]}', block_size=2**20) as f: b=f.read()
    wb=openpyxl.load_workbook(io.BytesIO(b), data_only=True)
    for ws in wb.worksheets:
        rows=list(ws.iter_rows(values_only=True))
        h=rows[0]; im=[i for i,x in enumerate(h) if x and str(x).startswith('Moment')][0]
        data=[(r[0],str(r[1]),r[im],r[im+1],r[im+2]) for r in rows[1:] if r[0] is not None and r[1] is not None]
        sheets[(fl['name'],ws.title)]=data
def scaled(vals):
    vals=[v for v in vals if v]
    if len(vals)<3: return None
    for base in vals:
        r=np.array(vals)/base
        if np.all(np.abs(r*100-np.round(r*100))<1e-6): return base
    return None
for k,data in sheets.items():
    g=collections.defaultdict(list)
    for s,step,m,dec,inc in data: g[step].append((m,dec,inc))
    flags=[]
    for step,v in g.items():
        v=np.array(v,float)
        for j,nm in enumerate(['m','dec','inc']):
            if scaled(list(v[:,j])) is not None: flags.append(f'{step}:{nm}')
    bad=[(s,step,m,dec,inc) for s,step,m,dec,inc in data if not (-90<=inc<=90 and 0<=dec<=360 and m>0)]
    dup=len(data)-len(set((step,m,dec,inc) for s,step,m,dec,inc in data))
    print(k, 'scaled groups', flags[:8], len(flags), 'bad', bad, 'dup rows', dup)
# rows duplicated across sheets
seen=collections.defaultdict(set)
for k,data in sheets.items():
    for s,step,m,dec,inc in data: seen[(m,dec,inc)].add(k)
print('cross-sheet dup', [(r,v) for r,v in seen.items() if len(v)>1][:20])
EOF
python survey.py
```

```
Exit code 1
('12021g2.asc.xlsx', '12021g2') scaled groups [] 0 bad [] dup rows 0
('12021g3.asc.xlsx', '12021g3') scaled groups [] 0 bad [] dup rows 0
('14053g2.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('71055g3.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('71055g1.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('14053g3.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('14053g1.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('12053g1.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('12053g2.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('12040g3.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('12040g2.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('12040g1.asc.xlsx', 'Sheet1') scaled groups [] 0 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss19') scaled groups ['250:inc'] 1 bad [('ss19', '10mT', 7.173e-08, 241.4, -136)] dup rows 0
('64455lunar_cryodata.xlsx', 'ss22') scaled groups [] 0 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss27') scaled groups ['100:inc', '100.1:inc'] 2 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss34') scaled groups [] 0 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss38') scaled groups [] 0 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss41') scaled groups ['360:inc'] 1 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss43') scaled groups [] 0 bad [] dup rows 2
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> survey.py <<'EOF'
EOF
sed -i 's/bad=\[(s,step,m,dec,inc) for s,step,m,dec,inc in data if not/bad=[(s,step,m,dec,inc) for s,step,m,dec,inc in data if None in (m,dec,inc) or not/' survey.py
cat >> survey.py <<'EOF'
def nsig(x):
    s=f'{x:.15g}'.replace('-','').replace('.','').split('e')[0].strip('0'); return len(s)
for k,data in sheets.items():
    n=sum(1 for r in data for x in r[2:] if x is not None and nsig(x)>6)
    if n: print('long digits', k, n, len(data)*3)
EOF
python survey.py 2>&1 | grep -v "scaled groups \[\] 0 bad \[\] dup rows 0"
```

```
('64455lunar_cryodata.xlsx', 'ss19') scaled groups ['250:inc'] 1 bad [('ss19', '10mT', 7.173e-08, 241.4, -136)] dup rows 0
('64455lunar_cryodata.xlsx', 'ss27') scaled groups ['100:inc', '100.1:inc'] 2 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss38') scaled groups [] 0 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss41') scaled groups ['360:inc'] 1 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss43') scaled groups [] 0 bad [] dup rows 2
('64455lunar_cryodata.xlsx', 'ss45') scaled groups [] 0 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss46') scaled groups ['10mT:dec'] 1 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss48') scaled groups ['0:m', '10mT:m', '10mT:dec', '100:dec', '100.1:m', '175.1:dec', '175.1:inc'] 7 bad [] dup rows 0
('64455lunar_cryodata.xlsx', 'ss6') scaled groups ['250:inc'] 1 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss9') scaled groups ['250:inc'] 1 bad [] dup rows 2
('64455lunar_cryodata.xlsx', 'ss10') scaled groups ['360:inc'] 1 bad [] dup rows 3
('64455lunar_cryodata.xlsx', 'ss11') scaled groups [] 0 bad [] dup rows 3
('64455lunar_cryodata.xlsx', 'ss18') scaled groups [] 0 bad [('ss18', '250', None, None, None)] dup rows 1
('64455lunar_cryodata.xlsx', 'ss24') scaled groups ['500:inc'] 1 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'ss29') scaled groups ['100:inc', '250:inc'] 2 bad [] dup rows 4
('64455lunar_cryodata.xlsx', 'ss36') scaled groups ['175:inc'] 1 bad [] dup rows 1
('64455lunar_cryodata.xlsx', 'g2') scaled groups ['0:m', '0:dec', '0:inc', '100.1:m', '100.1:dec', '100.1:inc', '100:m', '100:dec'] 18 bad [] dup rows 9
('64455lunar_cryodata.xlsx', 'ss8') scaled groups ['100.1:m', '100.1:dec', '100.1:inc', '175.1:m', '175.1:dec', '175.1:inc', '175:m', '175:dec'] 15 bad [('ss8', '0', 8.5082739e-08, 361.692, 6.8340000000000005)] dup rows 14
('64455lunar_cryodata.xlsx', 'ss39') scaled groups ['0:m', '0:dec', '0:inc', '100.1:m', '100.1:dec', '100.1:inc', '100:m', '100:dec'] 15 bad [] dup rows 5
cross-sheet dup [((1.072
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import openpyxl
wb=openpyxl.load_workbook('glass.xlsx', data_only=True)
for n in ['ss39','g2']:
  for r in list(wb[n].iter_rows(values_only=True))[:30]: print(r[:5])
for r in list(wb['ss8'].iter_rows(values_only=True))[:14]: print(r[:5])
"
```

```
('Sample', 'DEMAG', 'Moment(emu)', 'Dec', 'Inc')
('ss39', 0, 2.8898421924e-07, 188.802, 4.896)
('ss39', 0, 2.8615104062e-07, 186.951, 4.848)
('ss39', 0, 2.7198514752e-07, 177.696, 4.608)
('ss39', 0, 2.83317862e-07, 185.1, 4.8)
('ss39', 100.1, 8.9661251932e-09, 174.636, 2.156)
('ss39', 100.1, 9.14910734e-09, 178.2, 2.2)
('ss39', 100.1, 8.9661251932e-09, 174.636, 2.156)
('ss39', 100.1, 8.7831430464e-09, 171.07199999999997, 2.112)
('ss39', 100, 2.2890265199999997e-09, 165.033, -5.643)
('ss39', 100, 2.38151244e-09, 171.701, -5.871)
('ss39', 100, 2.21966208e-09, 160.03199999999998, -5.4719999999999995)
('ss39', 100, 2.35839096e-09, 170.034, -5.814)
('ss39', 100, 2.312148e-09, 166.7, -5.7)
('ss39', 210.1, 3.83110126e-09, 112.11200000000001, 9.995999999999999)
('ss39', 210.1, 3.83110126e-09, 112.11200000000001, 9.995999999999999)
('ss39', 210.1, 3.909287e-09, 114.4, 10.2)
('ss39', 210.1, 3.909287e-09, 114.4, 10.2)
('ss39', 210.1, 3.83110126e-09, 112.11200000000001, 9.995999999999999)
('ss39', 210, 9.385341155399999e-09, 2.254, -6.272)
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md; head -c 2500 entries/001453-fouke-2025/omr.py; ls schemas tools; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
Tue Oct 27 19:52:42 UTC 2026
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A12 "outcome: blocked" attempts/001453-fouke-2025-01.yaml | head -40; grep -n -A60 "^findings:" attempts/001453-fouke-2025-01.yaml | head -50; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
196-    in the dandiset; the measure was chosen here before the analysis.
197-- claim: fig1cef-representative-values
198:  outcome: blocked
199-  blocked_by: metadata_insufficient
200-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
201-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
202-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
203-- claim: fig2d-shared-architecture
204:  outcome: blocked
205-  blocked_by: data_missing
206-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
207-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
208-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
209-- claim: fig2g-dsi-similar
210:  outcome: blocked
211-  blocked_by: data_missing
212-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
213-- claim: fig2h-fewer-motion-responsive
214:  outcome: blocked
215-  blocked_by: data_missing
[... 348 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def \|figshare\|tag\|sanity" tools/entry.py | head -80
```

```
20:- each notebook has a cell tagged `sanity` that prints what was loaded;
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
76:def dataset_id(record: dict) -> str | None:
80:def schema(name: str) -> Draft202012Validator:
84:def load(report: Report, path: Path):
93:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
103:def _plain(value):
114:def code_of(notebook_path: Path) -> str:
121:def check(entry_dir: Path) -> Report:
174:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
175:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
283:            tag = outcome.get("output")
284:            if notebook in present and tag:
286:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
287:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
291:def _local_data(code: str, start: int) -> bool:
298:def _derivation_checks(report: Report, where, code: str) -> None:
312:def lock(entry_dir: Path) -> int:
320:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,66p tools/entry.py; sed -n 121,400p tools/entry.py
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 326 more lines not kept]
```

**Agent**

I have the formats. Next I'm writing the helper module (`apollo.py`) and trying the measures on the data before building the notebook.

**Agent calls Bash**

```bash
mkdir -p entries/figshare-24639285-tarduno-2024 && date -u
```

```
Tue Oct 27 19:53:38 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/figshare-24639285-tarduno-2024/apollo.py",
 "content": "\"\"\"Loading and measures for the Apollo magnetometer data of Figshare item 24639285, version 1.\n\nTarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0. Dataset\ndoi:10.6084/m9.figshare.24639285.v1 (the only version). Files are streamed from Figshare's\ndownload service into memory; nothing is written to disk.\n\nThe deposit holds one workbook of 22 sheets for the Apollo 64455 glass subsamples\n(64455lunar_cryodata.xlsx) and one workbook per single crystal (12 files). Each sheet has columns\nsample, DEMAG (step), moment (emu), declination and inclination (degrees), one row per\nmeasurement, with repeated rows for repeated measurements of a step. Steps: 0 is the NRM, \"<x>mT\"\nan AF step, \"<T>\" or \"<T>.0\" field-off, \"<T>.1\" field-on, \"<T>.2\" a pTRM check (glass), \"<T>.3\"\nthe zero-field alteration check and \"<T>.4\" the 40 uT field-on step (crystals). The glass sheets\ngive the laboratory field in a footnote line (\"Laboratory Field: 18 microTesla\").\n\nWhere the parameters come from:\n\n- TRM gained at a temperature is the vector difference of the field-on and field-off\n  measurements (Methods, Thermal measurements, paragraph 3: \"The TRM is the calculated vector\n  subtraction of field-on and field-off steps\"); NRM is the moment of the field-off measurement\n  (claims file, opening comment).\n- Repeated measurements of one step are combined as the mean vector (`how=\"mean\"`) or the first\n  measurement is used (`how=\"first\"`). The paper does not say which Table 2 used; for the crystals\n  it says the first measurements were used in ref. 1 (Background & Summary, paragraph 7). Both are\n  run wherever they could matter (author, step 1.6).\n- MAD is Kirschvink's (1980) principal component measure: free line (centred), line anchored to\n  the origin (uncentred), or free line on the three-point running mean of the field-off vectors\n  (claims file, opening comment, readings a to c). The running mean is centred, with the two end\n  points averaged over the two points available, a standard choice.\n- Great-circle MAD (fig2-changing-field, reading b) is Kirschvink's plane MAD with the plane\n  through the origin, the standard form of a great circle; a standard choice.\n- pTRM check percentage: the claims file's readings (a) |check pTRM - original pTRM| over the\n  original pTRM, (b) the same difference over the length of the fitted Arai segment (DRAT-like,\n  Selkin & Tauxe 2000), with the check's pTRM taken as the .2 vector minus (i) the field-off\n  vector measured just before it or (ii) the field-off vector at the check's temperature. The\n  difference is of magnitudes, the TRM-gained coordinate of the check on the Arai plot, where\n  Figures 1 and 2 plot the checks (legends: \"red triangles represent partial thermal remanent\n  magnetization checks\").\n- Watson's (1956) test of randomness: p is the fraction of 200000 sets of n uniform random unit\n  vectors whose resultant length is at least R (an exact Monte Carlo form of the test, with a\n  fixed seed per call); the claims file names the test.\n- Magnetometer threshold 8e-11 emu and the max intensity formula: Methods, Magnetometer\n  measurements, and Technical Validation.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport json\nimport re\nimport urllib.request\n\nimport fsspec\nimport numpy as np\nimport openpyxl\nimport pandas as pd\n\nFIGSHARE_ID = \"24639285\"\nFIGSHARE_VERSION = 1\nDATASET_DOI = \"10.6084/m9.figshare.24639285.v1\"\nAPI_URL = f\"https://api.figshare.com/v2/articles/{FIGSHARE_ID}/versions/{FIGSHARE_VERSION}\"\nGLASS_FILE = \"64455lunar_cryodata.xlsx\"\nTHRESHOLD_EMU = 8e-11\n\n\n# --- reading -------------------------------------------------------------------\n\ndef file_list() -> list[dict]:\n    \"\"\"The pinned version's files (id, name, size, computed_md5) from the Figshare API.\"\"\"\n    with urllib.request.urlopen(API_URL) as r:\n        meta = json.load(r)\n    assert meta[\"version\"] == FIGSHARE_VERSION and meta[\"doi\"] == DATASET_DOI, (meta[\"version\"], meta[\"doi\"])\n    return meta[\"files\"]\n\n\ndef read_bytes(file_id: int) -> bytes:\n    url = f\"https://ndownloader.figshare.com/files/{file_id}\"\n    with fsspec.open(url, block_size=2**20) as f:\n        return f.read()\n\n\ndef parse_sheet(ws) -> dict:\n    \"\"\"One sheet: its header, the measurement rows (in sheet order) and its footnote lines.\"\"\"\n    rows = list(ws.iter_rows(values_only=True))\n    header = [h for h in rows[0] if h is not None]\n    i_m = next(i for i, h in enumerate(rows[0]) if h is not None and str(h).startswith(\"Moment\"))\n    records, blank, notes = [], [], []\n    for n, r in enumerate(rows[1:], start=2):\n        if r[0] is not None and r[1] is not None:\n            m, dec, inc = r[i_m], r[i_m + 1], r[i_m + 2]\n            if m is None or dec is None or inc is None:\n                blank.append(n)\n                continue\n            records.append({\"row\": n, \"sample\": str(r[0]), \"step\": str(r[1]),\n                            \"moment\": float(m), \"dec\": float(dec), \"inc\": float(inc)})\n        elif r[0] is not None:\n            notes.append(str(r[0]).strip())\n    df = pd.DataFrame(records)\n    field = None\n    for note in notes:\n        hit = re.search(r\"Laboratory Field:\\s*([\\d.]+)\\s*micro\", note)\n        if hit:\n            field = float(hit.group(1))\n    return {\"header\": header, \"data\": df, \"notes\": notes, \"lab_field_uT\": field, \"incomplete_rows\": blank}\n\n\ndef load_all() -> tuple[list[dict], dict, dict]:\n    \"\"\"(file list, glass sheets by sheet name, crystal sheets by crystal name).\"\"\"\n    files = file_list()\n    glass, crystals = {}, {}\n    for f in files:\n        if not f[\"name\"].endswith(\".xlsx\"):\n            continue\n        wb = openpyxl.load_workbook(io.BytesIO(read_bytes(f[\"id\"])), data_only=True)\n        f[\"sheets\"] = wb.sheetnames\n        for ws in wb.worksheets:\n            sheet = parse_sheet(ws)\n            sheet[\"file\"] = f[\"name\"]\n            if f[\"name\"] == GLASS_FILE:\n                glass[ws.title] = sheet\n            else:\n                crystals[f[\"name\"].split(\".\")[0]] = sheet\n    return files, glass, crystals\n\n\n# --- steps and vectors ---------------------------------------------------------\n\ndef step_kind(step: str) -> tuple[str, float | None]:\n    \"\"\"('nrm' | 'af' | 'off' | 'on' | 'check' | 'alt' | 'on40', temperature or AF field).\"\"\"\n    if step.endswith(\"mT\"):\n        return \"af\", float(step[:-2])\n    value = float(step)\n    if value == 0:\n        return \"nrm\", 0.0\n    temp = float(int(value))\n    code = round((value - temp) * 10)\n    return {0: \"off\", 1: \"on\", 2: \"check\", 3: \"alt\", 4: \"on40\"}[code], temp\n\n\ndef to_xyz(moment, dec, inc) -> np.ndarray:\n    d, i = np.radians(np.asarray(dec, float)), np.radians(np.asarray(inc, float))\n    m = np.asarray(moment, float)\n    return np.stack([m * np.cos(i) * np.cos(d), m * np.cos(i) * np.sin(d), m * np.sin(i)], axis=-1)\n\n\ndef to_dir(v) -> tuple[float, float, float]:\n    v = np.asarray(v, float)\n    m = np.linalg.norm(v)\n    return float(np.degrees(np.arctan2(v[1], v[0])) % 360), float(np.degrees(np.arcsin(v[2] / m))), float(m)\n\n\ndef angle(a, b) -> float:\n    a, b = np.asarray(a, float), np.asarray(b, float)\n    c = np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)\n    return float(np.degrees(np.arccos(np.clip(c, -1, 1))))\n\n\ndef step_table(df: pd.DataFrame, how: str = \"mean\") -> pd.DataFrame:\n    \"\"\"One row per step label in order of first appearance, with its vector (mean or first).\"\"\"\n    out = []\n    for step, g in df.groupby(\"step\", sort=False):\n        xyz = to_xyz(g.moment, g.dec, g.inc)\n        v = xyz.mean(axis=0) if how == \"mean\" else xyz[0]\n        kind, t = step_kind(step)\n        out.append({\"step\": step, \"kind\": kind, \"t\": t, \"n\": len(g), \"x\": v[0], \"y\": v[1], \"z\": v[2],\n                    \"moment\": float(np.linalg.norm(v)), \"order\": int(g.row.min())})\n    return pd.DataFrame(out).sort_values(\"order\").reset_index(drop=True)\n\n\ndef vec(row) -> np.ndarray:\n    return np.array([row[\"x\"], row[\"y\"], row[\"z\"]])\n\n\ndef scaled_copies(values, lo: float = 0.90, hi: float = 1.10, tol: float = 1e-6) -> bool:\n    \"\"\"Whether every value equals one base value times a factor k/100 in [lo, hi] (to tol, relative).\"\"\"\n    v = np.asarray(values, float)\n    if len(v) < 3 or len(np.unique(v)) < 2 or np.any(v == 0):\n        return False\n    for v0 in v:\n        for f0 in np.arange(round(lo * 100), round(hi * 100) + 1) / 100:\n            r = v / (v0 / f0) * 100\n            if np.all(np.abs(r - np.round(r)) < tol * np.abs(r)) and np.all((r >= lo * 100 - 1e-6) & (r <= hi * 100 + 1e-6)):\n                return True\n    return False\n\n\ndef synthetic_steps(df: pd.DataFrame) -> list[str]:\n    \"\"\"Steps whose repeated rows are all one row scaled by factors of 0.90 to 1.10, in moment,\n    declination and inclination alike.\"\"\"\n    return [step for step, g in df.groupby(\"step\", sort=False)\n            if all(scaled_copies(g[c].abs()) for c in (\"moment\", \"dec\", \"inc\"))]\n\n\n# --- Arai and directions -------------------------------------------------------\n\ndef arai(df: pd.DataFrame, how: str = \"mean\") -> pd.DataFrame:\n    \"\"\"Paired thermal steps: NRM (moment of the field-off vector) and TRM gained (|on - off|).\"\"\"\n    st = step_table(df, how)\n    offs = st[st.kind == \"off\"].set_index(\"t\")\n    ons = st[st.kind == \"on\"].set_index(\"t\")\n    rows = []\n    for t in sorted(set(offs.index) & set(ons.index)):\n        off, on = vec(offs.loc[t]), vec(ons.loc[t])\n        rows.append({\"t\": t, \"nrm\": float(np.linalg.norm(off)), \"trm\": float(np.linalg.norm(on - off)),\n                     \"x\": off[0], \"y\": off[1], \"z\": off[2]})\n    return pd.DataFrame(rows)\n\n\ndef in_range(a: pd.DataFrame, t0: float, t1: float) -> pd.DataFrame:\n    return a[(a.t >= t0) & (a.t <= t1)].reset_index(drop=True)\n\n\ndef r2(x, y) -> float:\n    return float(np.corrcoef(x, y)[0, 1] ** 2)\n\n\ndef slope(x, y) -> float:\n    return float(np.polyfit(x, y, 1)[0])\n\n\ndef mad_line(points, anchored: bool = False) -> float:\n    X = np.asarray(points, float)\n    if not anchored:\n        X = X - X.mean(axis=0)\n    w = np.sort(np.linalg.eigvalsh(X.T @ X))[::-1]\n    w = np.clip(w, 0, None)\n    return float(np.degrees(np.arctan(np.sqrt((w[1] + w[2]) / w[0]))))\n\n\ndef mad_plane(points) -> float:\n    \"\"\"Great-circle MAD, plane through the origin.\"\"\"\n    X = np.asarray(points, float)\n    w = np.clip(np.sort(np.linalg.eigvalsh(X.T @ X))[::-1], 0, None)\n    return float(np.degrees(np.arctan(np.sqrt(w[2] / w[1] + w[2] / w[0]))))\n\n\ndef demag_sequence(df: pd.DataFrame, how: str = \"mean\") -> pd.DataFrame:\n    \"\"\"The field-off vectors in demagnetization order: the last NRM or AF step, then the thermal\n    field-off steps by temperature.\"\"\"\n    st = step_table(df, how)\n    start = st[st.kind.isin([\"nrm\", \"af\"])].iloc[[-1]]\n    offs = st[st.kind == \"off\"].sort_values(\"t\")\n    return pd.concat([start, offs]).reset_index(drop=True)\n\n\ndef running_mean3(X) -> np.ndarray:\n    X = np.asarray(X, float)\n    out = np.empty_like(X)\n    for i in range(len(X)):\n        out[i] = X[max(0, i - 1): i + 2].mean(axis=0)\n    return out\n\n\ndef mads(df: pd.DataFrame, t0: float, t1: float, how: str = \"mean\") -> dict:\n    \"\"\"MAD of the field-off vectors from t0 to t1 under readings (a) free, (b) anchored, (c) free\n    on the three-point running mean.\"\"\"\n    seq = demag_sequence(df, how)\n    sel = ((seq.kind == \"off\") & (seq.t >= t0) & (seq.t <= t1)).to_numpy()\n    X = seq[[\"x\", \"y\", \"z\"]].to_numpy()\n    return {\"a_free\": mad_line(X[sel]), \"b_anchored\": mad_line(X[sel], anchored=True),\n            \"c_smoothed\": mad_line(running_mean3(X)[sel])}\n\n\ndef ptrm_checks(df: pd.DataFrame, how: str = \"mean\", seg: tuple[float, float] | None = None) -> pd.DataFrame:\n    \"\"\"Each pTRM check, as a percentage under readings (a)/(b) x (i)/(ii).\"\"\"\n    st = step_table(df, how)\n    offs = st[st.kind == \"off\"].set_index(\"t\")\n    ons = st[st.kind == \"on\"].set_index(\"t\")\n    a = arai(df, how)\n    length = np.nan\n    if seg is not None:\n        s = in_range(a, *seg)\n        if len(s) >= 2:\n            b = slope(s.trm, s.nrm)\n            dx = s.trm.max() - s.trm.min()\n            length = float(np.hypot(dx, b * dx))\n    rows = []\n    for i, r in st[st.kind == \"check\"].iterrows():\n        t = r.t\n        prev = st.iloc[:i][st.iloc[:i].kind == \"off\"]\n        ref_prev = vec(prev.iloc[-1])\n        orig = np.linalg.norm(vec(ons.loc[t]) - vec(offs.loc[t]))\n        for ref_name, ref in ((\"i_prev\", ref_prev), (\"ii_same\", vec(offs.loc[t]))):\n            chk = np.linalg.norm(vec(r) - ref)\n            rows.append({\"t\": t, \"ref\": ref_name, \"prev_off_t\": float(prev.iloc[-1].t),\n                         \"check_trm\": chk, \"orig_trm\": orig,\n                         \"a_pct\": 100 * abs(chk - orig) / orig,\n                         \"b_pct\": 100 * abs(chk - orig) / length if length == length else np.nan})\n    return pd.DataFrame(rows)\n\n\n# --- statistics on directions --------------------------------------------------\n\ndef fisher(xyz) -> dict:\n    u = np.asarray(xyz, float)\n    u = u / np.linalg.norm(u, axis=1, keepdims=True)\n    n = len(u)\n    R = float(np.linalg.norm(u.sum(axis=0)))\n    mean = to_dir(u.sum(axis=0))\n    k = (n - 1) / (n - R) if n > 1 and n - R > 0 else np.nan\n    a95 = np.nan\n    if n > 1:\n        c = 1 - (n - R) / R * ((1 / 0.05) ** (1 / (n - 1)) - 1)\n        a95 = float(np.degrees(np.arccos(c))) if -1 <= c <= 1 else 180.0\n    return {\"n\": n, \"R\": R, \"dec\": mean[0], \"inc\": mean[1], \"k\": k, \"a95\": a95}\n\n\ndef watson_p(n: int, R: float, seed: int, nsim: int = 200_000) -> float:\n    \"\"\"P(resultant of n uniform unit vectors >= R).\"\"\"\n    if n < 2:\n        return np.nan\n    rng = np.random.default_rng(seed)\n    v = rng.normal(size=(nsim, n, 3))\n    v /= np.linalg.norm(v, axis=2, keepdims=True)\n    return float((np.linalg.norm(v.sum(axis=1), axis=1) >= R - 1e-12).mean())\n\n\ndef max_intensity(m590_emu: float, lab_field_uT: float = 20.0) -> float:\n    \"\"\"Technical Validation: threshold / TRM at 590 C x lab field.\"\"\"\n    return THRESHOLD_EMU / m590_emu * lab_field_uT\n"
}
```

```
File created successfully at: entries/figshare-24639285-tarduno-2024/apollo.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024 && . $TMPDIR/dev/bin/activate && python -c "
import apollo as A, pickle, time
t=time.time(); files,g,c=A.load_all(); print(time.time()-t)
pickle.dump((files,g,c),open('$TMPDIR/cache.pkl','wb'))
for k,s in g.items(): print(k, s['lab_field_uT'], s['incomplete_rows'], A.synthetic_steps(s['data']), len(s['data']))
for k,s in c.items(): print(k, A.synthetic_steps(s['data']))
"
```

```
8.100539445877075
ss19 18.0 [] [] 95
ss22 18.0 [] [] 110
ss27 18.0 [] [] 105
ss34 18.0 [] [] 87
ss38 18.0 [] [] 65
ss41 18.0 [] [] 115
ss43 18.0 [] [] 70
ss45 18.0 [] [] 60
ss46 18.0 [] [] 50
ss48 18.0 [] ['0', '5mT', '10mT', '100', '100.1', '175', '175.1'] 35
ss6 15.0 [] [] 99
ss9 15.0 [] [] 116
ss10 15.0 [] [] 122
ss11 15.0 [] [] 125
ss18 15.0 [41] [] 81
ss24 15.0 [] [] 146
ss29 15.0 [] [] 128
ss30 15.0 [] [] 103
ss36 15.0 [] [] 72
[... 15 more lines not kept]
```

**Agent**

The detector is clean: every step of g2, ss8, ss39 and ss48 is synthetic, and no step of any other sheet is. Now computing the Table 2 statistics.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import apollo as A, pickle, numpy as np, pandas as pd
pd.set_option('display.width',250)
files,g,c=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
T2={'ss19':(4,175,450,30.1,0.94,{250:30,450:9}),'ss43':(3,250,400,10.0,0.90,{250:85}),'ss22':(4,250,500,35.4,0.38,{250:22,450:13}),
'ss41':(3,500,580,24.0,0.38,{250:4,400:24}),'ss6':(3,175,360,21.0,0.91,{}),'ss9':(4,250,550,37.6,0.74,{250:21}),'ss10':(3,360,550,42.9,0.15,{250:83}),
'ss30':(4,175,500,12.5,0.59,{450:10}),'ss34':(5,100,450,12.1,0.06,{250:9})}
for s,(n,t0,t1,mad,rr,pt) in T2.items():
  df=g[s]['data']
  for how in ['mean','first']:
    a=A.in_range(A.arai(df,how),t0,t1)
    m=A.mads(df,t0,t1,how)
    p=A.ptrm_checks(df,how,(t0,t1))
    pts=' '.join(f"{int(r.t)}{r.ref[:2]}:{r.a_pct:.0f}/{r.b_pct:.0f}" for _,r in p.iterrows())
    print(s,how,'n',len(a),n,'R2 %.2f/%.2f'%(A.r2(a.trm,a.nrm),rr),'MAD',{k:round(v,1) for k,v in m.items()},mad,'|',pts,'| paper',pt, 'slope*F %.1f'%(abs(A.slope(a.trm,a.nrm))*g[s]['lab_field_uT']))
EOF
python $TMPDIR/t2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 1, in <module>
    import apollo as A, pickle, numpy as np, pandas as pd
ModuleNotFoundError: No module named 'apollo'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/t2.py
```

```
ss19 mean n 4 4 R2 0.96/0.94 MAD {'a_free': 30.1, 'b_anchored': 20.7, 'c_smoothed': 14.9} 30.1 | 250i_:64/24 250ii:106/40 450i_:9/7 450ii:12/10 | paper {250: 30, 450: 9} slope*F 23.0
ss19 first n 4 4 R2 0.96/0.94 MAD {'a_free': 31.1, 'b_anchored': 22.0, 'c_smoothed': 15.9} 30.1 | 250i_:29/13 250ii:87/38 450i_:7/6 450ii:23/20 | paper {250: 30, 450: 9} slope*F 23.7
ss43 mean n 3 3 R2 0.90/0.90 MAD {'a_free': 10.3, 'b_anchored': 27.0, 'c_smoothed': 14.5} 10.0 | 250i_:24/83 250ii:6/21 | paper {250: 85} slope*F 9.6
ss43 first n 3 3 R2 0.99/0.90 MAD {'a_free': 9.9, 'b_anchored': 30.8, 'c_smoothed': 14.1} 10.0 | 250i_:25/86 250ii:6/22 | paper {250: 85} slope*F 8.5
ss22 mean n 4 4 R2 0.38/0.38 MAD {'a_free': 35.4, 'b_anchored': 39.2, 'c_smoothed': 21.4} 35.4 | 250i_:11/24 250ii:22/47 450i_:5/14 450ii:13/40 | paper {250: 22, 450: 13} slope*F 3.5
ss22 first n 4 4 R2 0.44/0.38 MAD {'a_free': 33.2, 'b_anchored': 36.9, 'c_smoothed': 24.3} 35.4 | 250i_:15/35 250ii:21/50 450i_:12/38 450ii:15/49 | paper {250: 22, 450: 13} slope*F 5.2
ss41 mean n 3 3 R2 0.38/0.38 MAD {'a_free': 24.1, 'b_anchored': 26.3, 'c_smoothed': 14.4} 24.0 | 250i_:3/4 250ii:59/77 400i_:16/23 400ii:1/2 | paper {250: 4, 400: 24} slope*F 1.2
ss41 first n 3 3 R2 0.16/0.38 MAD {'a_free': 23.5, 'b_anchored': 26.6, 'c_smoothed': 15.3} 24.0 | 250i_:23/27 250ii:69/79 400i_:13/20 400ii:2/3 | paper {250: 4, 400: 24} slope*F 1.1
ss6 mean n 3 3 R2 0.89/0.91 MAD {'a_free': 21.2, 'b_anchored': 34.7, 'c_smoothed': 18.5} 21.0 |  | paper {} slope*F 3.5
ss6 first n 3 3 R2 0.09/0.91 MAD {'a_free': 24.2, 'b_anchored': 33.2, 'c_smoothed': 19.3} 21.0 |  | paper {} slope*F 0.5
ss9 mean n 4 4 R2 0.89/0.74 MAD {'a_free': 36.8, 'b_anchored': 27.2, 'c_smoothed': 8.3} 37.6 | 250i_:21/47 250ii:16/36 | paper {250: 21} slope*F 1.9
ss9 first n 4 4 R2 0.84/0.74 MAD {'a_free': 30.7, 'b_anchored': 28.5, 'c_smoothed': 7.9} 37.6 | 250i_:24/47 250ii:17/34 | paper {250: 21} slope*F 1.6
ss10 mean n 3 3 R2 0.23/0.15 MAD {'a_free': 33.3, 'b_anchored': 2
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t3.py <<'EOF'
import apollo as A, pickle, numpy as np, pandas as pd
files,g,c=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
NOFIT={'g2':(4,100,400),'ss8':(5,100,450),'ss11':(6,100,550),'ss18':(5,100,450),'ss24':(7,100,550),'ss27':(6,100,550),'ss29':(6,100,550),'ss36':(4,100,450),'ss38':(4,100,360),'ss39':(2,100,210),'ss45':(4,100,360),'ss46':(3,100,250),'ss48':(2,100,175)}
for s,(n,t0,t1) in NOFIT.items():
  a=A.in_range(A.arai(g[s]['data']),t0,t1)
  print(s,len(a),n,[f'{int(t)}:{x:.2e}/{y:.2e}' for t,x,y in zip(a.t,a.trm,a.nrm)])
print('AF')
for s,sh in g.items():
  st=A.step_table(sh['data'])
  af=st[st.kind=='af']
  if len(af)==0: continue
  nrm=st[st.kind=='nrm'].iloc[0]; last=af.iloc[-1]
  print(s, last.step, round(A.angle(A.vec(nrm),A.vec(last)),1), round(last.moment/nrm.moment,3))
print('Watson')
for i,(s,sh) in enumerate(g.items()):
  st=A.step_table(sh['data']); off=st[st.kind=='off']
  f=A.fisher(off[['x','y','z']].to_numpy())
  print(s,f['n'],round(f['R'],2), A.watson_p(f['n'],f['R'],i,20000))
EOF
PYTHONPATH=. python $TMPDIR/t3.py
```

```
g2 4 4 ['100:4.99e-09/2.81e-09', '210:3.81e-09/7.88e-10', '305:2.89e-09/2.13e-09', '400:1.80e-09/1.60e-09']
ss8 5 5 ['100:2.72e-09/2.66e-09', '175:5.96e-10/1.54e-09', '250:1.29e-09/8.97e-10', '360:3.33e-09/2.81e-09', '450:3.98e-09/3.18e-09']
ss11 6 6 ['100:1.20e-08/3.26e-09', '175:1.29e-08/2.09e-09', '250:1.41e-08/3.83e-09', '360:1.40e-08/3.29e-09', '450:2.04e-08/2.36e-09', '550:1.18e-08/3.35e-09']
ss18 5 5 ['100:1.88e-08/3.84e-09', '175:2.16e-08/5.84e-09', '250:1.95e-08/2.02e-09', '360:2.85e-08/9.46e-09', '450:2.24e-08/9.51e-09']
ss24 7 7 ['100:1.19e-07/1.21e-07', '175:2.97e-09/3.94e-09', '250:4.47e-09/1.96e-09', '360:5.95e-09/2.17e-09', '450:5.94e-09/3.14e-09', '500:1.21e-08/2.69e-09', '550:1.36e-08/4.02e-09']
ss27 5 6 ['100:1.15e-09/1.74e-08', '305:5.36e-09/3.50e-08', '400:6.11e-09/3.72e-08', '500:2.48e-08/2.66e-08', '550:1.15e-08/1.56e-08']
ss29 6 6 ['100:5.02e-09/1.20e-09', '175:6.36e-09/3.18e-09', '250:6.32e-09/3.65e-09', '450:6.35e-09/1.42e-09', '500:8.45e-09/3.60e-09', '550:2.23e-08/1.38e-09']
ss36 4 4 ['100:1.31e-08/1.59e-09', '175:1.44e-08/1.14e-09', '250:1.58e-08/1.77e-09', '450:1.68e-08/6.00e-09']
ss38 4 4 ['100:6.96e-09/2.21e-08', '175:8.46e-09/1.47e-08', '250:6.86e-09/9.20e-09', '360:5.87e-09/1.71e-09']
ss39 2 2 ['100:6.71e-09/2.31e-09', '210:1.17e-08/9.67e-09']
ss45 4 4 ['100:1.54e-08/8.12e-09', '175:1.51e-08/6.76e-09', '250:1.95e-08/9.35e-09', '360:1.65e-08/4.87e-09']
ss46 3 3 ['100:3.29e-08/5.12e-09', '175:3.57e-08/1.94e-08', '250:3.29e-08/1.24e-08']
ss48 2 2 ['100:1.94e-08/4.29e-09', '175:3.01e-10/4.21e-10']
AF
ss19 20mT 2.0 0.997
ss22 20mT 2.8 1.011
ss27 10mT 1.5 1.01
ss34 10mT 2.2 1.006
ss38 20mT 2.4 0.488
ss41 10mT 0.3 1.001
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/t4.py <<'EOF'
import apollo as A, pickle, numpy as np, pandas as pd
files,g,c=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
for i,(s,sh) in enumerate(sorted(c.items())):
  df=sh['data']
  def grp(step): 
    x=df[df.step==step]; return A.to_xyz(x.moment,x.dec,x.inc)
  out=[s]
  for st in ['0','590','590.3']:
    X=grp(st); f=A.fisher(X); p=A.watson_p(f['n'],f['R'],i,20000)
    out.append(f"{st}: n{f['n']} k{f['k']:.1f} a95 {f['a95']:.0f} p{p:.3f} m{np.mean(np.linalg.norm(X,axis=1)):.2e}")
  on=grp('590.1')[0]; off=grp('590'); alt=grp('590.3'); on40=grp('590.4')[0]
  m_b=np.linalg.norm(on); m_ai=np.linalg.norm(on-off[0]); m_aii=np.linalg.norm(on-off.mean(0))
  out.append(f"M590 b {m_b:.3e} ai {m_ai:.3e} aii {m_aii:.3e} maxI {A.max_intensity(m_b):.3f} {A.max_intensity(m_ai):.3f}")
  r_i=np.linalg.norm(on40-alt[0])/(2*m_ai); r_ii=np.linalg.norm(on40-alt.mean(0))/(2*m_aii)
  out.append(f"ratio40 {r_i:.2f} {r_ii:.2f}")
  print(' | '.join(out))
EOF
PYTHONPATH=. python $TMPDIR/t4.py
```

```
12021g2 | 0: n2 k600.3 a95 10 p0.001 m8.22e-10 | 590: n3 k1.2 a95 180 p0.637 m4.38e-10 | 590.3: n3 k1.2 a95 180 p0.643 m4.95e-10 | M590 b 7.011e-09 ai 6.625e-09 aii 6.827e-09 maxI 0.228 0.242 | ratio40 0.95 0.93
12021g3 | 0: n2 k213.6 a95 17 p0.005 m7.41e-10 | 590: n3 k1.1 a95 180 p0.764 m5.04e-10 | 590.3: n3 k0.8 a95 180 p0.967 m4.38e-10 | M590 b 6.292e-09 ai 5.956e-09 aii 6.396e-09 maxI 0.254 0.269 | ratio40 0.91 0.86
12040g1 | 0: n2 k981.4 a95 8 p0.001 m7.00e-10 | 590: n3 k1.8 a95 180 p0.340 m2.48e-10 | 590.3: n3 k0.8 a95 180 p0.984 m3.26e-10 | M590 b 8.002e-09 ai 7.842e-09 aii 7.878e-09 maxI 0.200 0.204 | ratio40 0.78 0.79
12040g2 | 0: n3 k22.8 a95 26 p0.003 m5.20e-10 | 590: n3 k1.4 a95 180 p0.547 m4.44e-10 | 590.3: n3 k1.2 a95 180 p0.655 m4.33e-10 | M590 b 6.021e-09 ai 5.669e-09 aii 5.840e-09 maxI 0.266 0.282 | ratio40 0.95 0.93
12040g3 | 0: n2 k1.3 a95 180 p0.630 m3.98e-10 | 590: n3 k0.8 a95 180 p0.983 m4.17e-10 | 590.3: n3 k1.0 a95 180 p0.789 m4.27e-10 | M590 b 6.292e-09 ai 6.675e-09 aii 6.279e-09 maxI 0.254 0.240 | ratio40 0.77 0.80
12053g1 | 0: n2 k9.8 a95 91 p0.101 m5.18e-10 | 590: n3 k0.9 a95 180 p0.909 m3.23e-10 | 590.3: n3 k1.2 a95 180 p0.686 m3.79e-10 | M590 b 5.283e-09 ai 5.019e-09 aii 5.209e-09 maxI 0.303 0.319 | ratio40 1.17 1.14
12053g2 | 0: n3 k37.8 a95 20 p0.001 m7.23e-10 | 590: n3 k0.8 a95 180 p0.987 m5.68e-10 | 590.3: n3 k1.6 a95 180 p0.442 m5.12e-10 | M590 b 7.982e-09 ai 7.758e-09 aii 7.887e-09 maxI 0.200 0.206 | ratio40 1.03 1.02
14053g1 | 0: n2 k3211.3 a95 4 p0.000 m1.24e-09 | 590: n3 k1.0 a95 180 p0.784 m1.16e-10 | 590.3: n3 k0.9 a95 180 p0.954 m2.14e-10 | M590 b 3.203e-09 ai 3.184e-09 aii 3.194e-09 maxI 0.500 0.503 | ratio40 0.94 0.95
14053g2 | 0: n2 k205.7 a95 18 p0.004 m6.08e-10 | 590: n3 k1.4 a95 180 p0.537 m2.98e-10 | 590.3: n3 k1.6 a95 180 p0.440 m3.01e-10 | M590 b 5.294e-09 ai 5.012e-09 aii 5.162e-09 maxI 0.302 0.319 | ratio40 0.86 0.86
14053g3 | 0: n2 k38.0 a95 42 p0.027 m5.49e-10 | 590: n4 k1.2 a95 180 p0.669 m2.76e-10 | 590.3: n3 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python -c "
import pickle; files,g,c=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
print(c['12021g3']['data'].to_string()); print(c['12040g3']['data'].to_string()); print(c['14053g1']['data'].to_string())
d=g['ss27']['data']; print(d[d.step.isin(['100','100.1','305'])].to_string())
d=g['ss10']['data']; print(d[d.step.isin(['250','250.1'])].to_string())
"
```

```
row   sample   step        moment    dec   inc
0    2  12021g3      0  7.392000e-10   73.7 -28.3
1    3  12021g3      0  7.425000e-10   78.2 -21.6
2    4  12021g3    590  5.028000e-10  156.2 -31.8
3    5  12021g3    590  4.922000e-10  305.1  71.0
4    6  12021g3    590  5.182000e-10  287.3  16.3
5    7  12021g3  590.1  6.292000e-09  178.3 -77.0
6    8  12021g3  590.3  4.233000e-10   94.8 -22.4
7    9  12021g3  590.3  4.028000e-10  190.2  41.8
8   10  12021g3  590.3  4.874000e-10  304.4  12.7
9   11  12021g3  590.4  1.099000e-08  182.3 -84.7
   row   sample   step        moment    dec   inc
0    2  12040g3      0  3.927000e-10   15.8 -19.4
1    3  12040g3      0  4.027000e-10  105.3  52.5
2    4  12040g3    590  4.028000e-10  148.3  67.1
3    5  12040g3    590  4.331000e-10  216.1 -43.2
4    6  12040g3    590  4.156000e-10   42.1 -17.5
5    7  12040g3  590.1  6.292000e-09  351.3 -85.3
6    8  12040g3  590.3  4.299000e-10  129.3  51.8
7    9  12040g3  590.3  4.024000e-10  316.2  31.7
[... 82 more lines not kept]
```

**Agent**

Everything needed has been tried. Next I'm writing the notebook, with every result computed from the streamed data.

**Agent calls Bash**

```bash
date -u; . $TMPDIR/dev/bin/activate; python -c "import nbformat, jupytext" 2>&1; uv pip install -q nbformat nbconvert ipykernel 2>&1 | tail -1
```

```
Tue Oct 27 19:56:20 UTC 2026
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import nbformat, jupytext
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat\nfrom nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = new_markdown_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Replicate Apollo sample magnetizations (Tarduno, Cottrell & Zhou 2024) on Figshare 24639285\n\nPaper: J. A. Tarduno, R. D. Cottrell, T. Zhou, \"Dataset of replicate Apollo sample magnetizations\nbearing on impacts and absence of a long-lived lunar dynamo\", Scientific Data (2024),\ndoi:10.1038/s41597-024-03626-0.\n\nDataset: Figshare item 24639285, version 1, doi:10.6084/m9.figshare.24639285.v1. Version 1 is the\nonly published version (the API lists no other), and it is the one the paper cites (ref. 26) and the\nclaims file names, so it is pinned. The cell below prints the MD5 (`computed_md5`) of every file read.\nThe files are streamed from Figshare's download service into memory; nothing is written to disk.\n\nClaims: `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`, written from the version of\nrecord (Europe PMC PMC11271266, full text with Methods, Technical Validation, figure legends and\nTables 1 and 2; the paper has no supplement and no PDF was supplied).\n\n| Claim | Tested here |\n|---|---|\n| glass-specimen-set (link) | tested |\n| glass-success-rate | tested |\n| table2-fit-statistics | tested |\n| table2-no-fit | tested |\n| fig1-linear-components | tested |\n| fig2-changing-field | tested |\n| glass-directions-not-random | tested |\n| glass-af-no-change | tested |\n| table1-max-intensity | tested |\n| baseline-range | tested |\n| example-14053g1-threshold | tested |\n| fig3-nrm-consistent | tested |\n| fig3-590-inconsistent | tested |\n| fig3-alteration-check-inconsistent | tested |\n| crystal-14053g1-400c-stable | tested |\n| no-alteration-recording-efficiency | tested |\n| interpretation-impact-no-dynamo | blocked: an interpretation the claims file says is not tested |\n\nMethod details the claims file leaves open are taken from the paper where it gives them, and cited\nin `apollo.py`. Where the paper does not settle a detail, every reading is run and shown.\n\"\"\")\n\ncode(r\"\"\"\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nimport apollo as A\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_rows\", 200)\n\nfiles, glass, crystals = A.load_all()\nprint(f\"Figshare {A.FIGSHARE_ID} version {A.FIGSHARE_VERSION}, doi:{A.DATASET_DOI}\")\nprint(pd.DataFrame([{k: f[k] for k in (\"id\", \"name\", \"size\", \"computed_md5\")} for f in files]).to_string(index=False))\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nWhat was loaded: every sheet of every workbook, its columns, the number of rows per specimen, step\nkind and replicate, and the ranges and units of moment, declination and inclination. The PDFs\n(plots and a PmagPy readme) are listed but not read. The data are static measurements with no time\naxis, so there is no clock to align; the check of the description is against the step labels, the\nunits, the specimen names and the laboratory field.\n\"\"\")\n\ncode(r\"\"\"\nfor f in files:\n    if f[\"name\"].endswith(\".xlsx\"):\n        print(f\"{f['name']}: sheets {f['sheets']}\")\nprint()\n\ndef summary(name, sheet):\n    df = sheet[\"data\"]\n    kinds = df.step.map(lambda s: A.step_kind(s)[0])\n    reps = df.groupby(\"step\").size()\n    return {\"specimen\": name, \"file\": sheet[\"file\"], \"sample label\": \",\".join(sorted(df[\"sample\"].unique())),\n            \"columns\": \"|\".join(map(str, sheet[\"header\"])), \"rows\": len(df),\n            \"steps\": df.step.nunique(), \"AF steps\": int((kinds == \"af\").sum() > 0) * df[kinds == \"af\"].step.nunique(),\n            \"thermal T\": \",\".join(str(int(t)) for t in sorted({A.step_kind(s)[1] for s in df.step if A.step_kind(s)[0] in (\"off\", \"on\")})),\n            \"replicates min-max\": f\"{reps.min()}-{reps.max()}\", \"lab field uT\": sheet[\"lab_field_uT\"],\n            \"incomplete rows\": sheet[\"incomplete_rows\"]}\n\ngsum = pd.DataFrame([summary(k, v) for k, v in glass.items()])\ncsum = pd.DataFrame([summary(k, v) for k, v in crystals.items()])\nprint(\"Glass, 64455lunar_cryodata.xlsx:\")\nprint(gsum.drop(columns=\"file\").to_string(index=False))\nprint(\"\\nCrystals, one workbook each:\")\nprint(csum.drop(columns=[\"file\", \"lab field uT\", \"AF steps\"]).to_string(index=False))\n\nallrows = pd.concat([v[\"data\"].assign(specimen=k) for d in (glass, crystals) for k, v in d.items()])\nprint(\"\\nRanges over all measurements: moment %.3g to %.3g emu; declination %.1f to %.1f deg; inclination %.1f to %.1f deg\"\n      % (allrows.moment.min(), allrows.moment.max(), allrows.dec.min(), allrows.dec.max(), allrows.inc.min(), allrows.inc.max()))\nbad = allrows[(allrows.inc.abs() > 90) | (allrows.dec < 0) | (allrows.dec > 360) | (allrows.moment <= 0)]\nprint(\"Measurements outside the ranges of a declination (0-360), an inclination (-90 to 90) or a positive moment:\")\nprint(bad[[\"specimen\", \"row\", \"step\", \"moment\", \"dec\", \"inc\"]].to_string(index=False))\nprint(\"Footnotes of the glass sheets:\", sorted({n for v in glass.values() for n in v[\"notes\"]}))\nprint(\"Footnotes of the crystal sheets:\", sorted({n for v in crystals.values() for n in v[\"notes\"]}))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nRepeated measurements of a step should differ by measurement noise. The cell below tests, for every\nstep of every sheet, whether all its rows are one row multiplied by factors k/100 between 0.90 and\n1.10 in moment, declination and inclination alike (`apollo.synthetic_steps`). For four-digit\nmeasurements this cannot happen by chance. It also lists rows repeated exactly within a sheet and\nacross sheets.\n\"\"\")\n\ncode(r\"\"\"\nsyn = {k: A.synthetic_steps(v[\"data\"]) for d in (glass, crystals) for k, v in d.items()}\nfor k, steps in syn.items():\n    n = (glass.get(k) or crystals.get(k))[\"data\"].step.nunique()\n    if steps:\n        print(f\"{k}: {len(steps)} of {n} steps are scaled copies of one row: {steps}\")\nprint(\"Sheets with no such step:\", [k for k, s in syn.items() if not s])\n\ndef factors(df, step):\n    g = df[df.step == step]\n    out = {}\n    for c in (\"moment\", \"dec\", \"inc\"):\n        v = g[c].abs().to_numpy()\n        for v0 in v:\n            for f0 in np.arange(90, 111) / 100:\n                r = v / (v0 / f0)\n                if np.all(np.abs(r * 100 - np.round(r * 100)) < 1e-6 * r * 100):\n                    out[c] = np.round(r, 2).tolist()\n                    break\n            if c in out:\n                break\n    return out\n\nfor k in (\"g2\", \"ss8\", \"ss39\", \"ss48\"):\n    print(f\"{k} NRM rows, factors relative to the base row:\", factors(glass[k][\"data\"], \"0\"))\nprint(glass[\"ss8\"][\"data\"].query(\"step == '0'\")[[\"row\", \"moment\", \"dec\", \"inc\"]].to_string(index=False))\n\ndups = []\nfor k, v in {**glass, **crystals}.items():\n    d = v[\"data\"]\n    n = d.duplicated([\"step\", \"moment\", \"dec\", \"inc\"]).sum()\n    if n:\n        dups.append((k, int(n), k in (\"g2\", \"ss8\", \"ss39\", \"ss48\")))\nprint(\"Rows repeated exactly within a sheet (specimen, count, synthetic sheet):\", dups)\nkey = allrows.set_index([\"moment\", \"dec\", \"inc\"])\ncross = allrows.groupby([\"moment\", \"dec\", \"inc\"]).specimen.nunique()\nprint(\"Rows found in more than one sheet:\")\nprint(allrows.set_index([\"moment\", \"dec\", \"inc\"]).loc[cross[cross > 1].index][[\"specimen\", \"row\", \"step\"]])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nChecks of the description against the data:\n\n- Columns: every sheet has sample, step, moment (emu), declination and inclination, as the Data\n  Records say, except ss48, which has an extra column `CSD` (empty or 0) before the moment. The\n  moment column is found by name.\n- Specimen names: the glass sheet `ss11` is named `s11` in Table 2; the sheet `g2` labels its\n  rows `64455g2`. Twelve crystal workbooks match the twelve names of Table 1.\n- Step labels follow the description (`#.0`, `#.1`, `#.2` for the glass; `#.3`, `#.4` for the\n  crystals); NRM appears as both `0` and `0.0` (ss27, ss38).\n- Laboratory field: the glass sheets give 18 uT (10 sheets), 15 uT (11) or 14.4 uT (g2); the paper\n  gives 18 uT only for Figure 1, whose specimens (ss19, ss43) are 18 uT sheets. The crystal sheets\n  give 20 and 40 uT for `#.1` and `#.4`, as the Methods say.\n- Replicates: each glass step was measured 2 to 19 times, each crystal NRM 1 to 3 times, each 590\n  zero-field step 3 or 4 times, and each crystal field-on step once. The paper does not say how\n  repeated measurements enter Table 2; both the mean vector and the first measurement are run below.\n- Four glass sheets (g2, ss8, ss39, ss48) do not hold repeated measurements: every step's rows are\n  one row times factors near 1. The analysis keeps them, as the deposit presents them, and the\n  results that use them say so; their mean vector is close to the base row.\n- Values out of range: one inclination of -136 deg (ss19, 10 mT, almost certainly -13.6), one\n  declination of 361.7 deg (ss8 NRM, a scaled copy), and an ss18 row at 250 C with no values. The\n  first two are used as they are (converted to vectors, a declination of 361.7 is 1.7 deg); the\n  ss19 value is in an AF step no analysis below uses; the empty row is dropped.\n\"\"\")\n\n# ---- link claim\nmd(r\"\"\"\n## glass-specimen-set (link)\n\n> The deposit holds the measurements of the 22 Apollo 64455 glass subsamples that failed the\n> paleointensity selection criteria, named as in Table 2, and replicate measurements for the twelve\n> single crystals of Table 1.\n\nCriterion: specimens matched by the names of Tables 1 and 2 (s11 may be ss11); each has steps,\nmoments, declinations and inclinations; which glass specimens have AF steps is compared with the\nreading of the Table 2 marks (12 without, 10 with).\n\"\"\")\n\ncode(r\"\"\"\nTABLE2 = [\"ss19\", \"ss43\", \"ss22\", \"ss41\", \"ss6\", \"ss9\", \"ss10\", \"ss30\", \"ss34\", \"g2\", \"ss8\", \"s11\", \"ss18\",\n          \"ss24\", \"ss27\", \"ss29\", \"ss36\", \"ss38\", \"ss39\", \"ss45\", \"ss46\", \"ss48\"]\n# Table 2 marks: the second mark (triangle) read as AF pre-treatment (claims file, opening comment)\nTABLE2_AF_MARK = [\"ss19\", \"ss43\", \"ss22\", \"ss41\", \"ss34\", \"ss27\", \"ss38\", \"ss45\", \"ss46\", \"ss48\"]\nTABLE1 = [\"12021g2\", \"12021g3\", \"12040g1\", \"12040g2\", \"12040g3\", \"12053g1\", \"12053g2\", \"14053g1\", \"14053g2\",\n          \"14053g3\", \"71055g1\", \"71055g3\"]\nSHEET = {n: (\"ss11\" if n == \"s11\" else n) for n in TABLE2}\n\ndef complete(sheet):\n    d = sheet[\"data\"]\n    return len(d) > 0 and d[[\"moment\", \"dec\", \"inc\"]].notna().all().all() and d.step.nunique() > 1\n\nfound_glass = [n for n in TABLE2 if SHEET[n] in glass and complete(glass[SHEET[n]])]\nfound_crystals = [n for n in TABLE1 if n in crystals and complete(crystals[n])]\nextra = sorted(set(glass) - set(SHEET.values())) + sorted(set(crystals) - set(TABLE1))\nhas_af = sorted(n for n in TABLE2 if (glass[SHEET[n]][\"data\"].step.str.endswith(\"mT\")).any())\nprint(f\"Glass specimens of Table 2 found with complete measurements: {len(found_glass)} of {len(TABLE2)}\")\nprint(f\"Crystals of Table 1 found with replicate measurements: {len(found_crystals)} of {len(TABLE1)}\")\nprint(\"Sheets or files not named in the tables:\", extra)\nprint(f\"Glass specimens with AF steps: {len(has_af)} {has_af}; without: {len(TABLE2) - len(has_af)}\")\nprint(\"Same set as the Table 2 marks:\", set(has_af) == set(TABLE2_AF_MARK))\nprint(\"Crystals with more than one NRM, 590.0 and 590.3 measurement:\",\n      {n: [int((crystals[n]['data'].step == s).sum()) for s in ('0', '590', '590.3')] for n in TABLE1})\n\"\"\", tags=[\"claim:glass-specimen-set\"])\n\nmd(r\"\"\"\n**Result: reproduced.** All 22 glass specimens of Table 2 (s11 as sheet ss11) and all 12 crystals\nof Table 1 are in the deposit with steps, moments, declinations and inclinations, and no other\nspecimen is. The 10 glass specimens with AF steps are exactly those carrying the second mark in\nTable 2. Two crystals (71055g1, 71055g3) have a single NRM measurement. Four glass sheets hold\nscaled copies of one measurement in place of replicates (Data check).\n\"\"\")\n\n# ---- success rate\nmd(r\"\"\"\n## glass-success-rate\n\n> Of the Apollo 64455 glass subsamples given thermal paleointensity experiments, 12% passed the\n> selection criteria (3 of 25, 13 run without and 12 with AF pre-treatment).\n\nCriterion: rate = 3 / (3 + failed specimens found here); the AF split is counted from AF steps in\nthe deposit plus the Methods' successful ones (one without, two with AF). Holds when 22 failed\nspecimens are found and 10 have AF steps.\n\"\"\")\n\ncode(r\"\"\"\nn_failed = len(found_glass)\nn_af = len(has_af)\nrate = 100 * 3 / (3 + n_failed)\nprint(f\"Failed specimens in the deposit: {n_failed}; with AF steps {n_af}, without {n_failed - n_af}\")\nprint(f\"Success rate 3 / (3 + {n_failed}) = {rate:.1f}% (expected 12 +- 1.2)\")\nprint(f\"Without AF: {n_failed - n_af} + 1 = {n_failed - n_af + 1} (expected 13); with AF: {n_af} + 2 = {n_af + 2} (expected 12)\")\n\"\"\", tags=[\"claim:glass-success-rate\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 22 failed specimens give 3/25 = 12.0%, and the AF steps split them 12 and\n10, which with the Methods' successful specimens gives 13 without and 12 with AF pre-treatment.\n\"\"\")\n\n# ---- table 2 fit statistics\nmd(r\"\"\"\n## table2-fit-statistics\n\n> For the nine failed glass specimens with a line fit (ss19, ss43, ss22, ss41, ss6, ss9, ss10, ss30,\n> ss34), the number of points, temperature range, MAD, R2 and pTRM check differences are as in\n> Table 2, which lists the criteria each failed.\n\nCriterion: per specimen, the paired steps in the Table 2 range, NRM against TRM gained, R2 of the\nleast-squares line, MAD under readings (a) free, (b) anchored, (c) free on the three-point running\nmean, and pTRM check percentages under readings (a) over the original pTRM, (b) over the length of the\nfitted segment, with the check's pTRM referred to (i) the field-off step just before it or (ii) the\nfield-off step at its temperature. A value matches when one reading puts it within tolerance.\nReproduced when n matches for all nine and at least 80% of the MAD, R2 and pTRM values match;\npartially for 50 to 80%.\n\nThe paper does not say how the repeated measurements of a step are combined. Both the mean vector\nand the first measurement are run; the mean is adopted as an assumption (see the end of this\nsection).\n\"\"\")\n\ncode(r\"\"\"\nT2 = {  # Table 2: n, T range, MAD, R2, pTRM checks {T: %}, failure criteria\n    \"ss19\": (4, 175, 450, 30.1, 0.94, {250: 30, 450: 9}, \"pTRM, MAD, n\"),\n    \"ss43\": (3, 250, 400, 10.0, 0.90, {250: 85}, \"pTRM, n\"),\n    \"ss22\": (4, 250, 500, 35.4, 0.38, {250: 22, 450: 13}, \"pTRM, MAD, R2\"),\n    \"ss41\": (3, 500, 580, 24.0, 0.38, {250: 4, 400: 24}, \"pTRM, MAD, R2, n\"),\n    \"ss6\": (3, 175, 360, 21.0, 0.91, {}, \"MAD, R2, n, no pTRM\"),\n    \"ss9\": (4, 250, 550, 37.6, 0.74, {250: 21}, \"pTRM, MAD, R2\"),\n    \"ss10\": (3, 360, 550, 42.9, 0.15, {250: 83}, \"pTRM, MAD, R2, n\"),\n    \"ss30\": (4, 175, 500, 12.5, 0.59, {450: 10}, \"R2\"),\n    \"ss34\": (5, 100, 450, 12.1, 0.06, {250: 9}, \"R2\"),\n}\nTOL_MAD = {\"ss19\": 3.0, \"ss43\": 1.0, \"ss22\": 3.5, \"ss41\": 2.4, \"ss6\": 2.1, \"ss9\": 3.8, \"ss10\": 4.3, \"ss30\": 1.25, \"ss34\": 1.2}\n\ndef fit_stats(how):\n    rows, checks = [], []\n    for s, (n, t0, t1, mad, rr, pt, fail) in T2.items():\n        df = glass[s][\"data\"]\n        a = A.in_range(A.arai(df, how), t0, t1)\n        m = A.mads(df, t0, t1, how)\n        r = A.r2(a.trm, a.nrm)\n        rows.append({\"specimen\": s, \"how\": how, \"n\": len(a), \"n_T2\": n, \"steps\": \",\".join(str(int(t)) for t in a.t),\n                     \"R2\": r, \"R2_T2\": rr, \"R2_ok\": abs(r - rr) <= 0.1 * rr + 1e-9,\n                     **{f\"MAD_{k}\": v for k, v in m.items()}, \"MAD_T2\": mad,\n                     \"MAD_ok_any\": any(abs(v - mad) <= TOL_MAD[s] + 1e-9 for v in m.values()),\n                     \"MAD_ok_a\": abs(m[\"a_free\"] - mad) <= TOL_MAD[s] + 1e-9})\n        p = A.ptrm_checks(df, how, (t0, t1))\n        for T, pct in pt.items():\n            q = p[p.t == T]\n            vals = {f\"{col[0]}_{ref.split('_')[0]}\": float(q[q.ref == ref][col].iloc[0])\n                    for col in (\"a_pct\", \"b_pct\") for ref in (\"i_prev\", \"ii_same\")}\n            checks.append({\"specimen\": s, \"how\": how, \"T\": T, \"printed\": pct, **{k: round(v, 1) for k, v in vals.items()},\n                           **{f\"ok_{k}\": abs(v / pct - 1) <= 0.1 + 1e-9 for k, v in vals.items()},\n                           \"prev_off_T\": int(q.prev_off_t.iloc[0])})\n    rows, checks = pd.DataFrame(rows), pd.DataFrame(checks)\n    checks[\"ok_any\"] = checks[[c for c in checks if c.startswith(\"ok_\")]].any(axis=1)\n    return rows, checks\n\nfits, chks = {}, {}\nfor how in (\"mean\", \"first\"):\n    fits[how], chks[how] = fit_stats(how)\n    print(f\"--- replicates combined as: {how}\")\n    print(fits[how].round(2).to_string(index=False))\n    print(chks[how].to_string(index=False))\n\"\"\", tags=[\"claim:table2-fit-statistics\"])\n\ncode(r\"\"\"\ndef score(how):\n    f, c = fits[how], chks[how]\n    n_ok = (f.n == f.n_T2).all()\n    mad_ok, r2_ok, pt_ok = int(f.MAD_ok_any.sum()), int(f.R2_ok.sum()), int(c.ok_any.sum())\n    total = len(f) * 2 + len(c)\n    return n_ok, mad_ok, r2_ok, pt_ok, total\n\nfor how in (\"mean\", \"first\"):\n    n_ok, mad_ok, r2_ok, pt_ok, total = score(how)\n    print(f\"{how}: n matches for all nine {n_ok}; MAD {mad_ok}/9, R2 {r2_ok}/9, pTRM {pt_ok}/{len(chks[how])}; \"\n          f\"together {mad_ok + r2_ok + pt_ok}/{total} = {100 * (mad_ok + r2_ok + pt_ok) / total:.0f}%\")\n\n# How often a single reading matches, so that the any-reading count can be judged\nf, c = fits[\"mean\"], chks[\"mean\"]\nfor k in (\"a_free\", \"b_anchored\", \"c_smoothed\"):\n    ok = sum(abs(f[f\"MAD_{k}\"] - f.MAD_T2) <= f.specimen.map(TOL_MAD) + 1e-9)\n    print(f\"mean, MAD reading {k} alone: {ok}/9 within tolerance; median |difference| \"\n          f\"{np.median(np.abs(f[f'MAD_{k}'] - f.MAD_T2)):.1f} deg\")\nfor k in (\"a_i\", \"a_ii\", \"b_i\", \"b_ii\"):\n    print(f\"mean, pTRM reading {k} alone: {int(c[f'ok_{k}'].sum())}/{len(c)} within 10% of the printed value\")\nprint(\"Values outside tolerance under every reading (mean):\")\nprint(f.loc[~f.MAD_ok_any, [\"specimen\", \"MAD_a_free\", \"MAD_b_anchored\", \"MAD_c_smoothed\", \"MAD_T2\"]].round(1).to_string(index=False))\nprint(f.loc[~f.R2_ok, [\"specimen\", \"R2\", \"R2_T2\"]].round(3).to_string(index=False))\nprint(c.loc[~c.ok_any, [\"specimen\", \"T\", \"printed\", \"a_i\", \"a_ii\", \"b_i\", \"b_ii\"]].to_string(index=False))\n\"\"\", tags=[\"claim:table2-fit-statistics\"])\n\ncode(r\"\"\"\n# Failure criteria against the stated thresholds (n >= 4, pTRM within 15%, R2 about 0.9); reported, not judged\nf, c = fits[\"mean\"], chks[\"mean\"]\nrep = []\nfor s, (n, t0, t1, mad, rr, pt, fail) in T2.items():\n    fr = f[f.specimen == s].iloc[0]\n    cs = c[c.specimen == s]\n    rep.append({\"specimen\": s, \"Table 2 failure\": fail, \"n<4\": fr.n < 4, \"R2<0.9\": round(fr.R2, 2) < 0.9,\n                \"pTRM>15% (reading a_i)\": bool((cs.a_i > 15).any()) if len(cs) else None, \"MAD (mean, a)\": round(fr.MAD_a_free, 1)})\nprint(pd.DataFrame(rep).to_string(index=False))\nprint(\"ss6 250.1 holds 19 rows in two groups of directions:\")\nd = glass[\"ss6\"][\"data\"].query(\"step == '250.1'\")\nprint(d.assign(group=np.where(d.inc > 30, \"inc>30\", \"inc<30\")).groupby(\"group\")[[\"moment\", \"dec\", \"inc\"]].agg([\"count\", \"mean\"]).round(10))\n\"\"\", tags=[\"claim:table2-fit-statistics\"])\n\nmd(r\"\"\"\n**Result: reproduced, resting on the assumption that repeated measurements are averaged.** With the\nmean vector of each step's repeated measurements, n matches Table 2 for all nine specimens, and 25\nof the 29 MAD, R2 and pTRM values match under one of the named readings (86%). MAD reading (a), a\nfree line, gives 8 of the 9 printed MADs within tolerance, 6 of them within 0.3 deg. ss10 differs\nin MAD (33.3 against 42.9 deg) and R2 (0.23 against 0.15); ss9 differs in R2 (0.89 against 0.74);\nand ss34's R2 is 0.03 against 0.06, outside a tolerance of 0.006. The matching pTRM checks need\ndifferent readings for different specimens, so no single pTRM definition is confirmed. With the first\nmeasurement of each step, fewer values match (see the counts above).\n\"\"\")\n\n# ---- no fit\nmd(r\"\"\"\n## table2-no-fit\n\n> The other thirteen failed glass specimens (g2, ss8, s11, ss18, ss24, ss27, ss29, ss36, ss38, ss39,\n> ss45, ss46, ss48) gave no fit, most because they did not acquire TRM in a regular fashion and some\n> because their directions trend out of the origin.\n\nCriterion: over each Table 2 range, TRM gained per step; regular acquisition read as (a) TRM gained\nincreasing at every step, or (b) no step falling by more than 15%. Reproduced when, under one reading,\nat least 9 of the 11 specimens marked \"no regular TRM acquisition\" are irregular, and ss36 and ss39\nhave field-off vectors whose distance from the origin grows over the last steps. The pTRM checks are\nreported.\n\"\"\")\n\ncode(r\"\"\"\nNOFIT = {\"g2\": (4, 100, 400, {}), \"ss8\": (5, 100, 450, {}), \"s11\": (6, 100, 550, {250: 22}), \"ss18\": (5, 100, 450, {250: 66}),\n         \"ss24\": (7, 100, 550, {250: 6, 450: 42}), \"ss27\": (6, 100, 550, {305: 1, 400: 54}), \"ss29\": (6, 100, 550, {450: 25}),\n         \"ss36\": (4, 100, 450, {450: 25}), \"ss38\": (4, 100, 360, {250: 9}), \"ss39\": (2, 100, 210, {}),\n         \"ss45\": (4, 100, 360, {250: 120}), \"ss46\": (3, 100, 250, {}), \"ss48\": (2, 100, 175, {})}\nIRREGULAR_LABEL = [s for s in NOFIT if s not in (\"ss36\", \"ss39\")]\nSYNTH = [\"g2\", \"ss8\", \"ss39\", \"ss48\"]\n\ndef regularity(how):\n    rows = []\n    for s, (n, t0, t1, pt) in NOFIT.items():\n        a = A.in_range(A.arai(glass[SHEET[s]][\"data\"], how), t0, t1)\n        trm = a.trm.to_numpy()\n        ratio = trm[1:] / trm[:-1]\n        rows.append({\"specimen\": s, \"how\": how, \"n\": len(a), \"n_T2\": n, \"T\": \",\".join(str(int(t)) for t in a.t),\n                     \"TRM gained (1e-9 emu)\": \" \".join(f\"{x * 1e9:.2f}\" for x in trm),\n                     \"irregular_a\": bool((ratio <= 1).any()), \"irregular_b\": bool((ratio < 0.85).any()),\n                     \"largest fall %\": round(100 * (1 - ratio.min()), 1) if len(ratio) else None,\n                     \"|off| (1e-9 emu)\": \" \".join(f\"{x * 1e9:.2f}\" for x in a.nrm),\n                     \"synthetic sheet\": s in SYNTH})\n    return pd.DataFrame(rows)\n\nfor how in (\"mean\", \"first\"):\n    r = regularity(how)\n    print(f\"--- {how}\")\n    print(r.to_string(index=False))\n    lab = r[r.specimen.isin(IRREGULAR_LABEL)]\n    print(f\"{how}: irregular under (a) {int(lab.irregular_a.sum())}/11, under (b) {int(lab.irregular_b.sum())}/11; \"\n          f\"without the four synthetic sheets (a) {int(lab[~lab['synthetic sheet']].irregular_a.sum())}/{int((~lab['synthetic sheet']).sum())}, \"\n          f\"(b) {int(lab[~lab['synthetic sheet']].irregular_b.sum())}/{int((~lab['synthetic sheet']).sum())}\")\n    for s in (\"ss36\", \"ss39\"):\n        a = A.in_range(A.arai(glass[s][\"data\"], how), *NOFIT[s][1:3])\n        print(f\"  {s}: distance of the field-off vector from the origin over the range \"\n              f\"{[f'{x * 1e9:.2f}' for x in a.nrm]} (1e-9 emu); grows over the last step: {bool(a.nrm.iloc[-1] > a.nrm.iloc[-2])}\")\n\"\"\", tags=[\"claim:table2-no-fit\"])\n\ncode(r\"\"\"\n# A null for the irregularity counts: how often 'irregular' arises from measurement scatter alone.\n# For each step of the non-synthetic specimens, the spread of TRM gained across replicates\n# (the field-on and field-off rows paired in order) is compared with the step-to-step falls.\nrng = np.random.default_rng(2101)\nrows = []\nfor s in IRREGULAR_LABEL:\n    if s in SYNTH:\n        continue\n    df = glass[SHEET[s]][\"data\"]\n    a = A.in_range(A.arai(df, \"mean\"), *NOFIT[s][1:3])\n    sd = []\n    for t in a.t:\n        on = df[df.step == f\"{t:g}.1\"]; off = df[df.step.isin([f\"{t:g}\", f\"{t:g}.0\"])]\n        k = min(len(on), len(off))\n        x = np.linalg.norm(A.to_xyz(on.moment[:k], on.dec[:k], on.inc[:k]) - A.to_xyz(off.moment[:k], off.dec[:k], off.inc[:k]), axis=1)\n        sd.append(x.std(ddof=1) / np.sqrt(k))\n    rows.append({\"specimen\": s, \"median SE of mean TRM gained / mean TRM gained\": round(float(np.median(np.array(sd) / a.trm)), 3)})\nprint(pd.DataFrame(rows).to_string(index=False))\n\nprint(\"pTRM checks of the no-fit specimens (mean, readings a and b over the Table 2 range), against Table 2:\")\nout = []\nfor s, (n, t0, t1, pt) in NOFIT.items():\n    p = A.ptrm_checks(glass[SHEET[s]][\"data\"], \"mean\", (t0, t1))\n    for T, pct in pt.items():\n        q = p[p.t == T]\n        if len(q) == 0:\n            out.append({\"specimen\": s, \"T\": T, \"printed\": pct, \"note\": \"no check at this T in the sheet\"})\n            continue\n        vals = {f\"{c[0]}_{r.split('_')[0]}\": round(float(q[q.ref == r][c].iloc[0]), 1) for c in (\"a_pct\", \"b_pct\") for r in (\"i_prev\", \"ii_same\")}\n        out.append({\"specimen\": s, \"T\": T, \"printed\": pct, **vals,\n                    \"any within 10%\": any(abs(v / pct - 1) <= 0.1 for v in vals.values())})\nout = pd.DataFrame(out)\nprint(out.to_string(index=False))\nprint(f\"pTRM checks matching under some reading: {int(out['any within 10%'].fillna(False).sum())}/{len(out)}\")\n\"\"\", tags=[\"claim:table2-no-fit\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (a), all 11 specimens marked \"no regular TRM acquisition\"\nacquire TRM irregularly (8 of 11 under reading b); ss36 and ss39 have field-off vectors that move away\nfrom the origin over the last step of their ranges. Three of the 11 (g2, ss8, ss48), and ss39, are\nsynthetic sheets. Reading (a) is weak: any fall in TRM gained counts, and the median standard error of\nthe mean TRM gained is printed above as a scale for the smaller falls. The pTRM checks of these\nspecimens are reported only.\n\"\"\")\n\n# ---- fig1\nmd(r\"\"\"\n## fig1-linear-components\n\n> Glass subsamples ss43 and ss19, which failed the reliability criteria, show hints of linear\n> directional components on orthogonal vector plots, from which nominal paleointensities can be\n> calculated with the 18 uT laboratory field.\n\nCriterion: over the Table 2 ranges, MAD and R2 as in table2-fit-statistics, and the nominal\npaleointensity as the absolute slope times 18 uT (Figure 1 legend). Holds when both MADs and R2\nvalues match Table 2 under one reading.\n\"\"\")\n\ncode(r\"\"\"\nfor how in (\"mean\", \"first\"):\n    f = fits[how].set_index(\"specimen\")\n    for s in (\"ss43\", \"ss19\"):\n        n, t0, t1 = T2[s][:3]\n        a = A.in_range(A.arai(glass[s][\"data\"], how), t0, t1)\n        b = A.slope(a.trm, a.nrm)\n        print(f\"{how} {s}: MAD a/b/c {f.loc[s, 'MAD_a_free']:.1f}/{f.loc[s, 'MAD_b_anchored']:.1f}/{f.loc[s, 'MAD_c_smoothed']:.1f} \"\n              f\"(Table 2 {T2[s][3]}), R2 {f.loc[s, 'R2']:.3f} (Table 2 {T2[s][4]}), slope {b:.3f}, \"\n              f\"lab field in sheet {glass[s]['lab_field_uT']} uT, nominal paleointensity |slope| x 18 = {abs(b) * 18:.1f} uT\")\n\nfig, axes = plt.subplots(1, 4, figsize=(15, 3.5))\nlim = []\nfor ax, s in zip(axes, (\"ss43\", \"ss19\", \"ss41\", \"ss22\")):\n    a = A.arai(glass[s][\"data\"], \"mean\")\n    t0, t1 = T2[s][1:3]\n    sel = (a.t >= t0) & (a.t <= t1)\n    ax.plot(a.trm * 1e9, a.nrm * 1e9, \"o-\", color=\"0.6\")\n    ax.plot(a.trm[sel] * 1e9, a.nrm[sel] * 1e9, \"o\", color=\"k\")\n    for t, x, y in zip(a.t, a.trm * 1e9, a.nrm * 1e9):\n        ax.annotate(f\"{t:g}\", (x, y), fontsize=7)\n    ax.set_title(f\"{s} (mean of replicates)\")\n    ax.set_xlabel(\"TRM gained (1e-9 emu)\")\n    ax.set_ylabel(\"NRM remaining (1e-9 emu)\")\n    lim.append((s, a.trm.min() * 1e9, a.trm.max() * 1e9, a.nrm.min() * 1e9, a.nrm.max() * 1e9))\nplt.tight_layout()\nplt.show()\nprint(\"Plotted ranges (x min, x max, y min, y max, 1e-9 emu); all points are inside the axes:\")\nfor r in lim:\n    print(r[0], [round(v, 2) for v in r[1:]])\n\"\"\", tags=[\"claim:fig1-linear-components\"])\n\nmd(r\"\"\"\n**Result: reproduced, resting on the averaging assumption.** With averaged replicates and a free line,\nss43 has MAD 10.3 deg and R2 0.90 (Table 2: 10.0 and 0.90), and ss19 MAD 30.1 deg and R2 0.96 (30.1\nand 0.94). The nominal paleointensities are 9.6 uT for ss43 and 23.0 uT for ss19 (8.5 and 23.7 uT with\nfirst measurements); the figure's values were not available to compare.\n\"\"\")\n\n# ---- fig2\nmd(r\"\"\"\n## fig2-changing-field\n\n> Glass subsamples ss41 and ss22 show field-off directions that change over a temperature interval,\n> consistent with a changing ambient field during magnetization, and curved NRM lost against TRM\n> gained plots.\n\nCriterion: Table 2 ranges (ss41 500 to 580 C, ss22 250 to 500 C). Readings (a) the angle between the\nfirst and last field-off direction of the range exceeds the MAD of a line fit over the range, (b) a\ngreat-circle fit has a smaller MAD than a line fit. Reproduced when both specimens change under one\nreading and R2 is within tolerance of 0.38.\n\"\"\")\n\ncode(r\"\"\"\nfor how in (\"mean\", \"first\"):\n    for s in (\"ss41\", \"ss22\"):\n        t0, t1 = T2[s][1:3]\n        seq = A.demag_sequence(glass[s][\"data\"], how)\n        r = seq[(seq.kind == \"off\") & (seq.t >= t0) & (seq.t <= t1)]\n        X = r[[\"x\", \"y\", \"z\"]].to_numpy()\n        ang = A.angle(X[0], X[-1])\n        line_free, line_anch, plane = A.mad_line(X), A.mad_line(X, anchored=True), A.mad_plane(X)\n        dirs = [tuple(round(v, 1) for v in A.to_dir(x)[:2]) for x in X]\n        r2v = fits[how].set_index(\"specimen\").loc[s, \"R2\"]\n        print(f\"{how} {s}: steps {list(r.t.astype(int))}, directions (dec, inc) {dirs}\")\n        print(f\"   first-last angle {ang:.1f} deg; line MAD free {line_free:.1f}, anchored {line_anch:.1f}; \"\n              f\"great-circle MAD {plane:.1f}; (a) {ang > line_free}, (b) {plane < line_free}; R2 {r2v:.3f} (0.38 +- 0.038)\")\n\"\"\", tags=[\"claim:fig2-changing-field\"])\n\nmd(r\"\"\"\n**Result: reproduced, resting on the averaging assumption.** For both specimens the field-off\ndirection turns by more than the MAD of a line over the range, and a great circle fits better than a\nline (numbers above); R2 is 0.38 for both with averaged replicates. With first measurements ss41's R2\nis 0.16.\n\"\"\")\n\n# ---- directions not random\nmd(r\"\"\"\n## glass-directions-not-random\n\n> The field-off directions of the failed glass specimens, as seen on orthogonal vector plots, are not\n> random, implying the presence of an ambient field.\n\nCriterion (a standard choice, the paper names no test): per specimen, Watson's test of randomness on\nthe field-off directions of its thermal steps (p < 0.05). Reproduced when more than half of the 22\nreject randomness, partially for a quarter to a half. Also given for the steps within each Table 2\nrange.\n\"\"\")\n\ncode(r\"\"\"\nRANGES = {**{s: v[1:3] for s, v in T2.items()}, **{s: v[1:3] for s, v in NOFIT.items()}}\nrows = []\nfor i, n in enumerate(TABLE2):\n    s = SHEET[n]\n    for how in (\"mean\", \"first\"):\n        st = A.step_table(glass[s][\"data\"], how)\n        off = st[st.kind == \"off\"]\n        f = A.fisher(off[[\"x\", \"y\", \"z\"]].to_numpy())\n        p = A.watson_p(f[\"n\"], f[\"R\"], seed=3000 + i)\n        t0, t1 = RANGES[n]\n        o2 = off[(off.t >= t0) & (off.t <= t1)]\n        f2 = A.fisher(o2[[\"x\", \"y\", \"z\"]].to_numpy())\n        p2 = A.watson_p(f2[\"n\"], f2[\"R\"], seed=3100 + i)\n        rows.append({\"specimen\": n, \"how\": how, \"n\": f[\"n\"], \"R\": round(f[\"R\"], 2), \"k\": round(f[\"k\"], 1), \"p\": p,\n                     \"n_range\": f2[\"n\"], \"R_range\": round(f2[\"R\"], 2), \"p_range\": p2, \"synthetic sheet\": n in SYNTH})\nw = pd.DataFrame(rows)\nprint(w.to_string(index=False))\nfor how in (\"mean\", \"first\"):\n    x = w[w.how == how]\n    print(f\"{how}: all thermal field-off steps reject randomness {int((x.p < 0.05).sum())}/22; \"\n          f\"within Table 2 ranges {int((x.p_range < 0.05).sum())}/22 \"\n          f\"(ranges of 2 steps: {int((x.n_range <= 2).sum())}); without synthetic sheets {int((x[~x['synthetic sheet']].p < 0.05).sum())}/18\")\n\"\"\", tags=[\"claim:glass-directions-not-random\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Watson's test rejects randomness of the thermal field-off\ndirections in 8 of 22 specimens with averaged replicates (36%, within the quarter to half band), and\nin fewer within the Table 2 ranges (counts above). The remaining specimens give directions that the\ntest cannot tell from random at these numbers of steps (2 to 9).\n\"\"\")\n\n# ---- AF no change\nmd(r\"\"\"\n## glass-af-no-change\n\n> For nearly all glass samples given AF pre-treatment, AF cleaning did not significantly change the\n> NRM direction or magnitude.\n\nCriterion: per specimen with AF steps, the angle between the NRM and the direction after the last AF\nstep, and the ratio of the moments. Readings (a) angle under 15 deg and moment change under 15%; (b)\nangle under the Table 2 MAD where printed, and moment change under 15%. Reproduced when, under one\nreading, all but at most two show no significant change.\n\"\"\")\n\ncode(r\"\"\"\nMADT2 = {s: v[3] for s, v in T2.items()}\nrows = []\nfor s in has_af:\n    for how in (\"mean\", \"first\"):\n        st = A.step_table(glass[s][\"data\"], how)\n        nrm = st[st.kind == \"nrm\"].iloc[0]\n        last = st[st.kind == \"af\"].iloc[-1]\n        ang = A.angle(A.vec(nrm), A.vec(last))\n        ratio = last.moment / nrm.moment\n        lim = MADT2.get(s, 15.0)\n        rows.append({\"specimen\": s, \"how\": how, \"last AF\": last.step, \"angle\": round(ang, 1), \"moment ratio\": round(ratio, 3),\n                     \"ok_a\": ang < 15 and abs(ratio - 1) < 0.15, \"MAD limit (b)\": lim,\n                     \"ok_b\": ang < lim and abs(ratio - 1) < 0.15, \"synthetic sheet\": s in SYNTH})\naf = pd.DataFrame(rows)\nprint(af.to_string(index=False))\nfor how in (\"mean\", \"first\"):\n    x = af[af.how == how]\n    print(f\"{how}: no significant change under (a) {int(x.ok_a.sum())}/{len(x)}, under (b) {int(x.ok_b.sum())}/{len(x)}\")\nprint(\"ss38 NRM rows ('0' and '0.0'):\")\nprint(glass[\"ss38\"][\"data\"].query(\"step in ['0', '0.0']\")[[\"row\", \"step\", \"moment\", \"dec\", \"inc\"]].to_string(index=False))\n\"\"\", tags=[\"claim:glass-af-no-change\"])\n\nmd(r\"\"\"\n**Result: reproduced.** AF cleaning turns the NRM by at most 2.8 deg and changes its moment by at\nmost 1.1% in 8 of the 10 specimens; ss38 keeps its direction but loses half its moment (ratio 0.49 at\n20 mT) and ss48, a synthetic sheet, turns by 17.5 deg and loses a third. Two exceptions are allowed.\n\"\"\")\n\n# ---- table 1\nmd(r\"\"\"\n## table1-max-intensity\n\n> For each of the twelve single crystals, the maximum field that cannot be excluded, given the\n> magnetometer threshold of 8e-11 emu and the moment acquired at 590 C in a 20 uT field, is as in\n> Table 1, between 0.20 and 0.51 uT.\n\nCriterion: max intensity = 8e-11 emu / M590 x 20 uT. M590 under readings (a) |590.1 - 590.0|, (b)\n|590.1|, with (i) the first 590.0 replicate or (ii) their mean. Reproduced when, under one reading,\nall 24 values are within tolerance; partially when at least 18 are.\n\"\"\")\n\ncode(r\"\"\"\nT1 = {\"12021g2\": (7.011e-9, 0.23), \"12021g3\": (6.292e-9, 0.26), \"12040g1\": (8.002e-9, 0.20), \"12040g2\": (6.021e-9, 0.27),\n      \"12040g3\": (6.292e-9, 0.26), \"12053g1\": (5.283e-9, 0.31), \"12053g2\": (7.982e-9, 0.20), \"14053g1\": (3.203e-9, 0.51),\n      \"14053g2\": (5.294e-9, 0.31), \"14053g3\": (4.523e-9, 0.36), \"71055g1\": (3.883e-9, 0.42), \"71055g3\": (4.202e-9, 0.39)}\n\ndef grp(name, step):\n    d = crystals[name][\"data\"]\n    d = d[d.step == step]\n    return A.to_xyz(d.moment, d.dec, d.inc)\n\ndef m590(name, reading):\n    on = grp(name, \"590.1\")[0]\n    off = grp(name, \"590\")\n    off = off[0] if reading.endswith(\"_i\") else off.mean(axis=0)\n    return float(np.linalg.norm(on - off)) if reading.startswith(\"a\") else float(np.linalg.norm(on))\n\nrows = []\nfor name, (m_t1, i_t1) in T1.items():\n    r = {\"crystal\": name, \"M590 T1\": m_t1, \"max T1\": i_t1}\n    for rd in (\"a_i\", \"a_ii\", \"b_i\", \"b_ii\"):\n        m = m590(name, rd)\n        r[f\"M_{rd}\"] = m\n        r[f\"max_{rd}\"] = round(A.max_intensity(m), 3)\n        r[f\"ok_{rd}\"] = int(abs(m - m_t1) <= 0.1 * m_t1) + int(abs(A.max_intensity(m) - i_t1) <= 0.1 * i_t1 + 1e-9)\n    r[\"T1 formula on own M590\"] = round(A.max_intensity(m_t1), 3)\n    rows.append(r)\nt1 = pd.DataFrame(rows)\nprint(t1.to_string(index=False))\nfor rd in (\"a_i\", \"a_ii\", \"b_i\", \"b_ii\"):\n    print(f\"reading {rd}: {int(t1[f'ok_{rd}'].sum())}/24 values within tolerance\")\nprint(\"Table 1 max intensity equal to the formula on its own M590, to two places:\",\n      int((t1[\"T1 formula on own M590\"].round(2) == t1[\"max T1\"]).sum()), \"/ 12\")\nprint(\"Exact equality of M590 (b) with Table 1 (to 4 significant digits):\",\n      int(sum(float(f\"{m:.4g}\") == mt for m, mt in zip(t1.M_b_i, t1[\"M590 T1\"]))), \"/ 12\")\nprint(\"12021g3 and 12040g3 590.1 rows:\")\nprint(pd.concat([crystals[n][\"data\"].query(\"step == '590.1'\") for n in (\"12021g3\", \"12040g3\")]).to_string(index=False))\n\"\"\", tags=[\"claim:table1-max-intensity\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (b), M590 the magnitude of the single 590.1 measurement, all 24\nvalues are within tolerance: the 12 M590 values equal Table 1 to its four digits and the max\nintensities run from 0.200 to 0.500 uT. Under reading (a) fewer values match (counts above). Table 1's\nmax intensities equal the formula on its own M590 column, to two places, for most crystals (count\nabove); 14053g1 is 0.50 by the formula and 0.51 in the table. The equal M590 of 12021g3 and 12040g3\nis in the data: both 590.1 rows read 6.292e-09 emu, with different directions.\n\"\"\")\n\n# ---- baseline\nmd(r\"\"\"\n## baseline-range\n\n> The maximum fields that the single crystal data cannot exclude define a baseline of about 0.2 to\n> 0.5 uT below which fields cannot be evaluated with these data.\n\nCriterion: the lowest and highest of the twelve values of table1-max-intensity, under the reading\nthat matches there, lie in 0.18 to 0.22 and 0.45 to 0.55 uT.\n\"\"\")\n\ncode(r\"\"\"\nvals = t1.max_b_i\nprint(f\"Reading (b): lowest {vals.min():.3f} uT ({t1.crystal[vals.idxmin()]}), highest {vals.max():.3f} uT ({t1.crystal[vals.idxmax()]})\")\nprint(f\"Within 0.18-0.22: {0.18 <= vals.min() <= 0.22}; within 0.45-0.55: {0.45 <= vals.max() <= 0.55}\")\nfor rd in (\"a_i\", \"a_ii\"):\n    print(f\"Reading {rd} for comparison: {t1[f'max_{rd}'].min():.3f} to {t1[f'max_{rd}'].max():.3f} uT\")\n\"\"\", tags=[\"claim:baseline-range\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The twelve values run from 0.200 to 0.500 uT.\n\"\"\")\n\n# ---- example\nmd(r\"\"\"\n## example-14053g1-threshold\n\n> For crystal 14053g1, the threshold field detection limit computed from the magnetometer sensitivity\n> (8e-14 A m2) and a TRM at 590 C of 8e-12 A m2 in a 20 uT field is 0.2 uT.\n\nCriterion: readings (a) the example as written, for 14053g1; (b) a misprint of the crystal name, the\nnumbers belonging to 12040g1. TRM as in table1-max-intensity (reading b matched there). Reproduced as\nwritten when (a) matches; when only (b) matches, reported as matching the misprint reading.\n\"\"\")\n\ncode(r\"\"\"\nfor name in (\"14053g1\", \"12040g1\"):\n    m_emu = m590(name, \"b_i\")\n    trm_am2 = m_emu * 1e-3   # 1 emu = 1e-3 A m2\n    thr = 8e-14 / trm_am2 * 20\n    print(f\"{name}: TRM at 590 C {trm_am2:.3e} A m2 (expected 8.0e-12 +- 8e-13: {abs(trm_am2 - 8e-12) <= 8e-13}); \"\n          f\"threshold field {thr:.3f} uT (expected 0.2 +- 0.02: {abs(thr - 0.2) <= 0.02})\")\n\"\"\", tags=[\"claim:example-14053g1-threshold\"])\n\nmd(r\"\"\"\n**Result: reproduced under the misprint reading (b).** For 14053g1 the data give a TRM of 3.2e-12 A m2\nand 0.50 uT, not the example's numbers; for 12040g1 they give 8.0e-12 A m2 and 0.200 uT, the example's\nnumbers. The example's crystal name is a misprint for 12040g1.\n\"\"\")\n\n# ---- fig3\nmd(r\"\"\"\n## fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent\n\n> For most crystals the replicate NRM measurements have a consistent direction, as shown on stereonets\n> for 12040g1 and 14053g2. After demagnetization at 590 C in zero field, the replicate directions are\n> inconsistent, consistent with a null magnetization state. The replicate directions after the\n> zero-field alteration check at 590 C are also inconsistent.\n\nCriteria: per crystal, Fisher mean, k and alpha95 of the replicate directions of each step. NRM\nconsistent under (a) k of the NRM replicates above k of the 590.0 replicates, or (b) Watson's test\nrejects randomness of the NRM replicates (p < 0.05). 590.0 (and 590.3) inconsistent under (a) k below\nthe NRM's k, or (b) Watson's test does not reject randomness. Each reproduced when, under one reading,\nmore than half of the twelve crystals qualify, including 12040g1 and 14053g2. A crystal with one NRM\nmeasurement has no k and no test, and counts as not qualifying.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor i, name in enumerate(T1):\n    r = {\"crystal\": name}\n    for step, lab in ((\"0\", \"nrm\"), (\"590\", \"590.0\"), (\"590.3\", \"590.3\"), (\"400\", \"400.0\"), (\"400.3\", \"400.3\")):\n        X = grp(name, step)\n        if len(X) == 0:\n            continue\n        f = A.fisher(X)\n        r[f\"{lab} n\"] = f[\"n\"]\n        r[f\"{lab} k\"] = round(f[\"k\"], 1) if f[\"k\"] == f[\"k\"] else np.nan\n        r[f\"{lab} a95\"] = round(f[\"a95\"], 0) if f[\"a95\"] == f[\"a95\"] else np.nan\n        r[f\"{lab} p\"] = A.watson_p(f[\"n\"], f[\"R\"], seed=4000 + 10 * i + len(r))\n        r[f\"{lab} mean moment\"] = float(np.linalg.norm(X, axis=1).mean())\n        r[f\"{lab} dec,inc\"] = (round(f[\"dec\"], 1), round(f[\"inc\"], 1))\n    rows.append(r)\ncr = pd.DataFrame(rows).set_index(\"crystal\")\ncols = [c for c in cr if c.split()[0] in (\"nrm\", \"590.0\", \"590.3\")]\nprint(cr[cols].to_string())\n\nknrm = cr[\"nrm k\"]\nnrm_a = knrm > cr[\"590.0 k\"]\nnrm_b = cr[\"nrm p\"] < 0.05\nc590_a = cr[\"590.0 k\"] < knrm\nc590_b = cr[\"590.0 p\"] >= 0.05\nc5903_a = cr[\"590.3 k\"] < knrm\nc5903_b = cr[\"590.3 p\"] >= 0.05\nsumm = pd.DataFrame({\"NRM consistent (a)\": nrm_a, \"NRM consistent (b)\": nrm_b, \"590.0 inconsistent (a)\": c590_a,\n                     \"590.0 inconsistent (b)\": c590_b, \"590.3 inconsistent (a)\": c5903_a, \"590.3 inconsistent (b)\": c5903_b})\nprint(summ.to_string())\nprint(\"Counts of 12:\", summ.sum().astype(int).to_dict())\nprint(\"12040g1 and 14053g2:\", summ.loc[[\"12040g1\", \"14053g2\"]].to_dict(\"index\"))\nprint(f\"590.0 mean moments: {cr['590.0 mean moment'].min():.3g} to {cr['590.0 mean moment'].max():.3g} emu; \"\n      f\"above the 8e-11 emu threshold: {int((cr['590.0 mean moment'] > A.THRESHOLD_EMU).sum())}/12; \"\n      f\"single 590.0 measurements above it: {sum(int((np.linalg.norm(grp(n, '590'), axis=1) > A.THRESHOLD_EMU).sum()) for n in T1)}\"\n      f\"/{sum(len(grp(n, '590')) for n in T1)}\")\nprint(f\"590.3 mean moments: {cr['590.3 mean moment'].min():.3g} to {cr['590.3 mean moment'].max():.3g} emu; \"\n      f\"NRM mean moments: {cr['nrm mean moment'].min():.3g} to {cr['nrm mean moment'].max():.3g} emu\")\n\"\"\", tags=[\"claim:fig3-nrm-consistent\", \"claim:fig3-590-inconsistent\", \"claim:fig3-alteration-check-inconsistent\"])\n\nmd(r\"\"\"\n**Result: fig3-nrm-consistent reproduced.** NRM replicates are more tightly grouped than the 590.0\nreplicates in 10 of 12 crystals (reading a; 8 of 12 under reading b), including 12040g1 and 14053g2;\n71055g1 and 71055g3 have one NRM measurement each.\n\n**Result: fig3-590-inconsistent reproduced.** Watson's test does not reject randomness of the 590.0\nreplicates in any of the 12 crystals (reading b), and their k is below the NRM's in the 10 crystals\nwith two or more NRM measurements (reading a). The 590.0 moments, 1.2e-10 to 5.7e-10 emu on average,\nare all above the 8e-11 emu threshold.\n\n**Result: fig3-alteration-check-inconsistent reproduced.** The same holds for the 590.3 replicates: 12\nof 12 under reading (b), 10 of 12 under reading (a).\n\"\"\")\n\n# ---- 14053g1 400\nmd(r\"\"\"\n## crystal-14053g1-400c-stable\n\n> Crystal 14053g1, measured after heating to 400 C during initial tests, held a stable remanence,\n> which was removed by treatment at 590 C.\n\nCriterion: applies if the deposit holds 400 C measurements for 14053g1. (a) the 400 C replicates are\nconsistent under fig3-nrm-consistent's readings and the 590.0 replicates inconsistent; or (b) the 400\nC direction lies within the alpha95 of the Fisher mean of the NRM replicates. Reproduced when the\n590.0 replicates are inconsistent and (a) or (b) holds.\n\"\"\")\n\ncode(r\"\"\"\nr = cr.loc[\"14053g1\"]\nprint(\"14053g1 rows at 400 C:\")\nprint(crystals[\"14053g1\"][\"data\"].query(\"step.str.startswith('400')\").to_string(index=False))\nprint(f\"NRM: n {r['nrm n']}, mean {r['nrm dec,inc']}, k {r['nrm k']}, a95 {r['nrm a95']}, mean moment {r['nrm mean moment']:.3g} emu\")\nprint(f\"400.0: n {r['400.0 n']}, mean {r['400.0 dec,inc']}, k {r['400.0 k']}, a95 {r['400.0 a95']}, Watson p {r['400.0 p']:.4f}, mean moment {r['400.0 mean moment']:.3g}\")\nprint(f\"400.3: n {r['400.3 n']}, mean {r['400.3 dec,inc']}, k {r['400.3 k']}\")\nprint(f\"590.0: n {r['590.0 n']}, k {r['590.0 k']}, Watson p {r['590.0 p']:.3f}, mean moment {r['590.0 mean moment']:.3g}\")\na_k = r[\"400.0 k\"] > r[\"590.0 k\"]\na_w = r[\"400.0 p\"] < 0.05\ninc590 = (r[\"590.0 k\"] < r[\"nrm k\"]) or (r[\"590.0 p\"] >= 0.05)\nm400 = grp(\"14053g1\", \"400\").sum(axis=0)\nmnrm = grp(\"14053g1\", \"0\")\nmnrm = (mnrm / np.linalg.norm(mnrm, axis=1, keepdims=True)).sum(axis=0)\nang = A.angle(m400, mnrm)\nprint(f\"(a) 400 C consistent: k above 590.0's {a_k}, Watson rejects {a_w}; 590.0 inconsistent {inc590}\")\nprint(f\"(b) angle between the 400 C mean and the NRM mean {ang:.1f} deg, NRM alpha95 {r['nrm a95']} deg: within {ang <= r['nrm a95']}\")\nfor i, x in enumerate(grp(\"14053g1\", \"400\")):\n    print(f\"    400 C replicate {i + 1}: {A.angle(x, mnrm):.1f} deg from the NRM mean\")\n\"\"\", tags=[\"claim:crystal-14053g1-400c-stable\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The deposit holds three 400 C measurements of 14053g1 (with a 400.1 and two\n400.3 rows). They are grouped (k above that of the 590.0 replicates, and Watson's test rejects\nrandomness), while the 590.0 replicates are not, so reading (a) holds. Under reading (b) the 400 C\nmean lies outside the NRM's alpha95 (numbers above).\n\"\"\")\n\n# ---- alteration\nmd(r\"\"\"\n## no-alteration-recording-efficiency\n\n> Alteration during the laser heating of the single crystals was not significant; apparent recording\n> efficiencies far above 100% were not observed and the alteration checks did not fail.\n\nCriterion: (a) the 590.3 moment does not exceed the 590.0 moment by more than 8e-11 emu, and the\n590.3 directions are inconsistent; (b) the 590.4 TRM (|590.4 - 590.3|) is no more than about twice the\n590.1 TRM (|590.1 - 590.0|); a ratio of the 590.4 TRM to twice the 590.1 TRM above 2 fails (a choice\nnot from the paper). Reproduced when every crystal passes under one reading.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor name in T1:\n    on, off, alt, on40 = grp(name, \"590.1\")[0], grp(name, \"590\"), grp(name, \"590.3\"), grp(name, \"590.4\")[0]\n    for rep in (\"i\", \"ii\"):\n        o = off[0] if rep == \"i\" else off.mean(axis=0)\n        al = alt[0] if rep == \"i\" else alt.mean(axis=0)\n        m_off = np.linalg.norm(off[0]) if rep == \"i\" else np.linalg.norm(off, axis=1).mean()\n        m_alt = np.linalg.norm(alt[0]) if rep == \"i\" else np.linalg.norm(alt, axis=1).mean()\n        ratio = np.linalg.norm(on40 - al) / (2 * np.linalg.norm(on - o))\n        rows.append({\"crystal\": name, \"replicates\": rep, \"590.3 - 590.0 moment (1e-11 emu)\": round((m_alt - m_off) * 1e11, 1),\n                     \"a_moment_ok\": m_alt - m_off <= A.THRESHOLD_EMU, \"a_dirs_inconsistent\": bool(summ.loc[name, \"590.3 inconsistent (b)\"]),\n                     \"TRM40/(2 TRM20)\": round(ratio, 3), \"b_ok\": ratio <= 2})\nalt = pd.DataFrame(rows)\nalt[\"a_ok\"] = alt.a_moment_ok & alt.a_dirs_inconsistent\nprint(alt.to_string(index=False))\nfor rep in (\"i\", \"ii\"):\n    x = alt[alt.replicates == rep]\n    print(f\"replicates {rep}: pass (a) {int(x.a_ok.sum())}/12, pass (b) {int(x.b_ok.sum())}/12; \"\n          f\"TRM40/(2 TRM20) {x['TRM40/(2 TRM20)'].min():.2f} to {x['TRM40/(2 TRM20)'].max():.2f}\")\n\"\"\", tags=[\"claim:no-alteration-recording-efficiency\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (b) every crystal passes: the TRM acquired in 40 uT is 0.77 to\n1.17 times twice the TRM acquired in 20 uT, close to linear recording and far from the cutoff of 2.\nUnder reading (a) some crystals fail the moment test by a few 1e-11 emu (counts above).\n\"\"\")\n\n# ---- interpretation\nmd(r\"\"\"\n## interpretation-impact-no-dynamo\n\n> Together with ref. 1, the data are consistent with impact plasma magnetization of the 64455 glass\n> and with the absence of a long-lived lunar core dynamo recorded in the 3.9 to 3.2 Ga crystals.\n\nThe claims file says this interpretation is not tested; it rests on ref. 1 and on models of impact\nplasmas. It is recorded as blocked. The outcomes of the four claims it names are: fig2-changing-field\nreproduced, glass-directions-not-random partially reproduced, fig3-590-inconsistent reproduced,\ntable1-max-intensity reproduced.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| glass-specimen-set (link) | reproduced |\n| glass-success-rate | reproduced |\n| table2-fit-statistics | reproduced (assumes averaged replicates) |\n| table2-no-fit | reproduced |\n| fig1-linear-components | reproduced (assumes averaged replicates) |\n| fig2-changing-field | reproduced (assumes averaged replicates) |\n| glass-directions-not-random | partially reproduced |\n| glass-af-no-change | reproduced |\n| table1-max-intensity | reproduced |\n| baseline-range | reproduced |\n| example-14053g1-threshold | reproduced under the misprint reading |\n| fig3-nrm-consistent | reproduced |\n| fig3-590-inconsistent | reproduced |\n| fig3-alteration-check-inconsistent | reproduced |\n| crystal-14053g1-400c-stable | reproduced |\n| no-alteration-recording-efficiency | reproduced |\n| interpretation-impact-no-dynamo | blocked (interpretation, not tested) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and\nthe differences from the paper's method.\n\nHow the analysis differs from the paper's: the paper used PmagPy and gives no formulas; MAD, R2 and\npTRM checks are computed here by the claims file's readings, and repeated measurements are averaged,\nan assumption that reproduces most of Table 2. No test of randomness is named by the paper; Watson's\ntest is the claims file's choice.\n\nWhat was found about the dataset:\n\n- The \"replicates\" of four glass sheets (g2, ss8, ss39, ss48) are one measurement multiplied by\n  factors near 1 (0.95 to 1.03), applied to moment, declination and inclination; they are not\n  repeated measurements.\n- One inclination of -136 deg (ss19, 10 mT), one declination of 361.7 deg (ss8), an empty row (ss18),\n  and an extra column in ss48.\n- The number of repeated measurements varies from 2 to 19 per step, ss6's 250.1 step holds two groups\n  of directions, and the deposit does not say how repeated measurements were combined.\n- The glass laboratory field varies between sheets (14.4, 15 and 18 uT); the paper states only 18 uT.\n- The Technical Validation example for 14053g1 uses the numbers of 12040g1.\n- The crystals' 590 C zero-field moments are all above the 8e-11 emu threshold the paper uses.\n\"\"\")\n\nnb = new_notebook(cells=cells, metadata={\"kernelspec\": {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"},\n                                         \"language_info\": {\"name\": \"python\"}})\nnbformat.write(nb, \"entries/figshare-24639285-tarduno-2024/reproduce_tarduno_2024.ipynb\")\nprint(\"ok\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && cd entries/figshare-24639285-tarduno-2024 && time jupyter nbconvert --to notebook --execute reproduce_tarduno_2024.ipynb --output-dir $TMPDIR/exec --ExecutePreprocessor.timeout=1200 2>&1 | tail -30
```

```
ok
    ss24                                           0.022
    ss27                                           0.035
    ss29                                           0.025
    ss38                                           0.061
    ss45                                           0.009
    ss46                                           0.010
pTRM checks of the no-fit specimens (mean, readings a and b over the Table 2 range), against Table 2:
------------------

[31m---------------------------------------------------------------------------[39m
[31mAttributeError[39m                            Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[10][39m[32m, line 25[39m
[32m     21[39m out = []
[32m     22[39m [38;5;28;01mfor[39;00m s, (n, t0, t1, pt) [38;5;28;01min[39;00m NOFIT.items():
[32m     23[39m     p = A.ptrm_checks(glass[SHEET[s]][[33m"data"[39m], [33m"mean"[39m, (t0, t1))
[32m     24[39m     [38;5;28;01mfor[39;00m T, pct [38;5;28;01min[39;00m pt.items():
[32m---> [39m[32m25[39m         q = p[p.t == T]
[32m     26[39m         [38;5;28;01mif[39;00m len(q) == [32m0[39m:
[32m     27[39m             out.append({[33m"specimen"[39m: s, [33m"T"[39m: T, [33m"printed"[39m: pct, [33m"note"[39m: [33m"no check at this T in the sheet"[39m})
[... 15 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/figshare-24639285-tarduno-2024/apollo.py",
 "old_string": "                         \"b_pct\": 100 * abs(chk - orig) / length if length == length else np.nan})\n    return pd.DataFrame(rows)",
 "new_string": "                         \"b_pct\": 100 * abs(chk - orig) / length if length == length else np.nan})\n    return pd.DataFrame(rows, columns=[\"t\", \"ref\", \"prev_off_t\", \"check_trm\", \"orig_trm\", \"a_pct\", \"b_pct\"])"
}
```

```
The file entries/figshare-24639285-tarduno-2024/apollo.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/figshare-24639285-tarduno-2024 && jupyter nbconvert --to notebook --execute reproduce_tarduno_2024.ipynb --output-dir $TMPDIR/exec --ExecutePreprocessor.timeout=1200 2>&1 | tail -5; jupyter nbconvert --to markdown $TMPDIR/exec/reproduce_tarduno_2024.ipynb --output-dir $TMPDIR/exec >/dev/null 2>&1; wc -l $TMPDIR/exec/reproduce_tarduno_2024.md
```

```
[NbConvertApp] Converting notebook reproduce_tarduno_2024.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 249681 bytes to /tmp/claude-1001/exec/reproduce_tarduno_2024.ipynb
1391 /tmp/claude-1001/exec/reproduce_tarduno_2024.md
```

**Agent calls Bash**

```bash
sed -n 1,400p $TMPDIR/exec/reproduce_tarduno_2024.md | grep -v "^$" | cut -c1-260
```

```
# Replicate Apollo sample magnetizations (Tarduno, Cottrell & Zhou 2024) on Figshare 24639285
Paper: J. A. Tarduno, R. D. Cottrell, T. Zhou, "Dataset of replicate Apollo sample magnetizations
bearing on impacts and absence of a long-lived lunar dynamo", Scientific Data (2024),
doi:10.1038/s41597-024-03626-0.
Dataset: Figshare item 24639285, version 1, doi:10.6084/m9.figshare.24639285.v1. Version 1 is the
only published version (the API lists no other), and it is the one the paper cites (ref. 26) and the
claims file names, so it is pinned. The cell below prints the MD5 (`computed_md5`) of every file read.
The files are streamed from Figshare's download service into memory; nothing is written to disk.
Claims: `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`, written from the version of
record (Europe PMC PMC11271266, full text with Methods, Technical Validation, figure legends and
Tables 1 and 2; the paper has no supplement and no PDF was supplied).
| Claim | Tested here |
|---|---|
| glass-specimen-set (link) | tested |
| glass-success-rate | tested |
| table2-fit-statistics | tested |
| table2-no-fit | tested |
| fig1-linear-components | tested |
| fig2-changing-field | tested |
| glass-directions-not-random | tested |
[... 324 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,1391p $TMPDIR/exec/reproduce_tarduno_2024.md | grep -v "^$" | grep -v "^[a-zA-Z#\[(\"' ]*[=(]" | grep "^    \|^\*\*" | cut -c1-250
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/06cc7bd0-50dd-4f83-bfbd-14649441af02/tool-results/bxynjmlnb.txt

Preview (first 2KB):
            checks.append({"specimen": s, "how": how, "T": T, "printed": pct, **{k: round(v, 1) for k, v in vals.items()},
                           **{f"ok_{k}": abs(v / pct - 1) <= 0.1 + 1e-9 for k, v in vals.items()},
                           "prev_off_T": int(q.prev_off_t.iloc[0])})
    rows, checks = pd.DataFrame(rows), pd.DataFrame(checks)
    checks["ok_any"] = checks[[c for c in checks if c.startswith("ok_")]].any(axis=1)
    return rows, checks
    fits[how], chks[how] = fit_stats(how)
    --- replicates combined as: mean
    specimen  how  n  n_T2               steps   R2  R2_T2  R2_ok  MAD_a_free  MAD_b_anchored  MAD_c_smoothed  MAD_T2  MAD_ok_any  MAD_ok_a
        ss19 mean  4     4     175,250,360,450 0.96   0.94   True       30.10           20.68           14.89    30.1        True      True
        ss43 mean  3     3         250,360,400 0.90   0.90   True       10.25           27.00           14.49    10.0        True      True
        ss22 mean  4     4     250,360,450,500 0.38   0.38   True       35.36           39.19           21.38    35.4        True      True
        ss41 mean  3     3         500,550,580 0.38   0.38   True       24.06           26.25           14.45    24.0        True      True
         ss6 mean  3     3         175,250,360 0.89   0.91   True       21.18           34.71           18.49    21.0        True      True
         ss9 mean  4     4     250,360,450,550 0.89   0.74  False       36.77           27.22            8.33    37.6        True      True
        ss10 mean  3     3         360,450,550 0.23   0.15  False       33.33           23.94           18.13    42.9       False     False
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^    " $TMPDIR/exec/reproduce_tarduno_2024.md | sed -n '/replicates combined as: mean/,$p' | grep -v "^[0-9]*:    [ ]*\(rows\|checks\|vals\|for\|if\|print\|def\|out\|r\[\|r =\|a =\|f =\|m =\|p =\|q =\|x =\|n =\|t0\|s =\|st =\|on\|off\|al\|o =\|lim\|ang\|ratio\|X =\|dirs\|seq\|line\|b =\|ax\|f2\|o2\|p2\|nrm\|last\|m_\|sd\|k =\|trm\|df\|d =\|\*\*\|\"\|return\|mnrm\|thr\|cs\|fr\|rep\)" | cut -c1-240 | head -300
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/06cc7bd0-50dd-4f83-bfbd-14649441af02/tool-results/bog3wieol.txt

Preview (first 2KB):
416:    --- replicates combined as: mean
417:    specimen  how  n  n_T2               steps   R2  R2_T2  R2_ok  MAD_a_free  MAD_b_anchored  MAD_c_smoothed  MAD_T2  MAD_ok_any  MAD_ok_a
418:        ss19 mean  4     4     175,250,360,450 0.96   0.94   True       30.10           20.68           14.89    30.1        True      True
419:        ss43 mean  3     3         250,360,400 0.90   0.90   True       10.25           27.00           14.49    10.0        True      True
420:        ss22 mean  4     4     250,360,450,500 0.38   0.38   True       35.36           39.19           21.38    35.4        True      True
421:        ss41 mean  3     3         500,550,580 0.38   0.38   True       24.06           26.25           14.45    24.0        True      True
422:         ss6 mean  3     3         175,250,360 0.89   0.91   True       21.18           34.71           18.49    21.0        True      True
423:         ss9 mean  4     4     250,360,450,550 0.89   0.74  False       36.77           27.22            8.33    37.6        True      True
424:        ss10 mean  3     3         360,450,550 0.23   0.15  False       33.33           23.94           18.13    42.9       False     False
425:        ss30 mean  4     4     175,250,450,500 0.60   0.59   True       11.49           14.39            8.04    12.5        True      True
426:        ss34 mean  5     5 100,175,250,360,450 0.03   0.06  False       11.95           11.01           10.70    12.1        True      True
427:    specimen  how   T  printed   a_i  a_ii  b_i  b_ii  ok_a_i  ok_a_ii  ok_b_i  ok_b_ii  prev_off_T  ok_any
428:        ss19 mean 250       30  63.6 105.9 23.7  39.5   False    False   False    False         360   False
429:        ss19 mean 450        9   8.7  12.1  7.4  10.3    True    False   Fals
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' > $TMPDIR/out.txt
import nbformat
nb=nbformat.read('/tmp/claude-1001/exec/reproduce_tarduno_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('name')=='stdout': print(f'--- cell {i}'); print(o.text)
EOF
sed -n '/cell 9$/,$p' $TMPDIR/out.txt | cut -c1-230 | head -150
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "^--- cell" $TMPDIR/out.txt; awk '/^--- cell 11/,0' $TMPDIR/out.txt | cut -c1-230 | head -120
```

```
1:--- cell 1
21:--- cell 3
84:--- cell 5
106:--- cell 8
114:--- cell 11
119:--- cell 14
167:--- cell 15
188:--- cell 16
206:--- cell 19
244:--- cell 20
256:--- cell 20
270:--- cell 23
276:--- cell 23
283:--- cell 26
293:--- cell 29
342:--- cell 32
374:--- cell 35
399:--- cell 38
405:--- cell 41
409:--- cell 44
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/^--- cell 19/,0' $TMPDIR/out.txt | sed -n '36,400p' | cut -c1-200
```

```
ss36: distance of the field-off vector from the origin over the range ['1.84', '1.82', '1.82', '6.35'] (1e-9 emu); grows over the last step: True
  ss39: distance of the field-off vector from the origin over the range ['2.29', '9.39'] (1e-9 emu); grows over the last step: True

--- cell 20
specimen  median SE of mean TRM gained / mean TRM gained
     s11                                           0.019
    ss18                                           0.012
    ss24                                           0.022
    ss27                                           0.035
    ss29                                           0.025
    ss38                                           0.061
    ss45                                           0.009
    ss46                                           0.010
pTRM checks of the no-fit specimens (mean, readings a and b over the Table 2 range), against Table 2:

--- cell 20
specimen   T  printed   a_i  a_ii   b_i  b_ii any within 10%                            note
     s11 250       22  12.8  10.8  21.1  17.7           True                             NaN
    ss18 250       66  32.9  60.7  54.2 100.0           True                             NaN
    ss24 250        6  13.1  41.0   0.3   1.1          False                             NaN
[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
rep('''**Result: reproduced, resting on the assumption that repeated measurements are averaged.** With the
mean vector of each step's repeated measurements, n matches Table 2 for all nine specimens, and 25
of the 29 MAD, R2 and pTRM values match under one of the named readings (86%). MAD reading (a), a
free line, gives 8 of the 9 printed MADs within tolerance, 6 of them within 0.3 deg.''',
'''**Result: partially reproduced, resting on the assumption that repeated measurements are averaged.**
With the mean vector of each step's repeated measurements, n matches Table 2 for all nine specimens,
and 23 of the 29 MAD, R2 and pTRM values match under one of the named readings (79%, just under the
80% the criterion asks for): MAD 8 of 9, R2 6 of 9, pTRM checks 9 of 11. MAD reading (a), a free
line, alone gives the 8 matching MADs, 6 of them within 0.3 deg of the printed value.''')
rep('''different readings for different specimens, so no single pTRM definition is confirmed. With the first
measurement of each step, fewer values match (see the counts above).''',
'''different readings for different specimens (no single reading matches more than 5 of 11), so no
single pTRM definition is confirmed. With the first measurement of each step, 11 of 29 values match
(38%), which would make the claim not reproduced; the mean is adopted because it gives the printed
MADs to the printed digit for six specimens. ss6's 250.1 step mixes two groups of directions (19
rows), which lowers its R2 under the mean.''')
rep('''**Result: reproduced.** Under reading (a), all 11 specimens marked "no regular TRM acquisition"
acquire TRM irregularly (8 of 11 under reading b);''','''**Result: reproduced.** Under reading (a), all 11 specimens marked "no regular TRM acquisition"
acquire TRM irregularly (9 of 11 under reading b, and 8 of the 8 not from synthetic sheets under
reading a);''')
rep('''specimens are reported only.''','''specimens are reported only: 6 of 10 match under some reading, and ss36 has no check at 450 C in
the sheet although Table 2 prints one; ss27 has 5 paired steps from 100 to 550 C where Table 2 gives 6.''')
rep('''directions in 8 of 22 specimens with averaged replicates (36%, within the quarter to half band), and
in fewer within the Table 2 ranges (counts above).''','''directions in 8 of 22 specimens with averaged replicates (36%, within the quarter to half band), 9
of 22 with first measurements, and 8 of 22 within the Table 2 ranges.''')
rep('''values are within tolerance: the 12 M590 values equal Table 1 to its four digits and the max
intensities run from 0.200 to 0.500 uT. Under reading (a) fewer values match (counts above). Table 1's
max intensities equal the formula on its own M590 column, to two places, for most crystals (count
above); 14053g1 is 0.50 by the formula and 0.51 in the table.''','''values are within tolerance: the 12 M590 values equal Table 1 to its four digits and the max
intensities run from 0.200 to 0.500 uT. Reading (a) with averaged 590.0 replicates also puts all 24
within tolerance (23 with the first replicate). Table 1's max intensities equal the formula on its
own M590 column, rounded to two places, for only 4 of 12 crystals; rounded up, for 10 of 12, the
exceptions being 14053g1 (0.4995 against 0.51) and 12053g2 (0.2004 against 0.20).''')
rep('''print("Exact equality of M590 (b)''','''import math
print("Table 1 max intensity equal to the formula on its own M590, rounded up to two places:",
      int(sum(math.ceil(round(A.max_intensity(m) * 100, 6)) / 100 == i for m, i in zip(t1["M590 T1"], t1["max T1"]))), "/ 12")
print("Formula on Table 1's own M590, unrounded:", {n: round(A.max_intensity(m), 4) for n, m in zip(t1.crystal, t1["M590 T1"])})
print("Exact equality of M590 (b)''')
rep('''    print(r[0], [round(v, 2) for v in r[1:]])''','''    print(r[0], [round(float(v), 2) for v in r[1:]])''')
rep('''Under reading (a) some crystals fail the moment test by a few 1e-11 emu (counts above).''','''Under reading (a) 11 of 12 pass with first replicates and 10 of 12 with means; 14053g1's 590.3
moment exceeds its 590.0 moment by 1.0e-10 to 1.2e-10 emu, above the 8e-11 emu allowance.''')
rep('''| table2-fit-statistics | reproduced (assumes averaged replicates) |''','''| table2-fit-statistics | partially reproduced (assumes averaged replicates) |''')
open(p,'w').write(s)
EOF
date -u
```

```
Tue Oct 27 20:01:07 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
openpyxl
pandas
requests
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: figshare-24639285-tarduno-2024
type: reproduction
title: Replicate Apollo sample magnetizations (Tarduno, Cottrell and Zhou 2024)
description: Tests the findings of Tarduno, Cottrell and Zhou (2024) on Figshare item 24639285,
  which holds the thermal paleointensity measurements of 22 Apollo 64455 glass subsamples that
  failed the selection criteria and the replicate measurements of twelve single silicate crystals.
  It recomputes the fit statistics of Table 2, the magnetization thresholds of Table 1, the
  consistency of replicate directions and the alteration checks.
license: Apache-2.0
notebooks:
- path: reproduce_tarduno_2024.ipynb
  title: Reproducing Tarduno, Cottrell and Zhou (2024) from Figshare 24639285
  runtime_minutes: 1
helpers:
- apollo.py
related:
- id: figshare:24639285/1
  relation: uses_data
- id: doi:10.1038/s41597-024-03626-0
  relation: reproduces
EOF
cd ../.. && python tools/entry.py lock entries/figshare-24639285-tarduno-2024 && python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -15
```

```
Exit code 1
ok
Traceback (most recent call last):
  File "tools/entry.py", line 53, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q pyyaml jsonschema nbformat && python tools/entry.py lock entries/figshare-24639285-tarduno-2024 && python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -15
```

```
wrote entries/figshare-24639285-tarduno-2024/requirements.lock.txt
Installed kernelspec registry-figshare-24639285-tarduno-2024 in executed/figshare-24639285-tarduno-2024/.venv/share/jupyter/kernels/registry-figshare-24639285-tarduno-2024
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (27 s)
```

**Agent**

The notebook runs in 27 s in a clean environment. Checking the executed copy against the conclusion text.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('executed/figshare-24639285-tarduno-2024/reproduce_tarduno_2024.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        for o in c.outputs:
            if o.get('name')=='stdout':
                for l in o.text.splitlines():
                    if any(k in l for k in ('together','irregular under','reject randomness','reading a_','rounded','unrounded','Counts of 12','pass (a)','pTRM checks matching','Within 0.18')): print(i,l[:300])
            if o.get('output_type')=='error': print('ERROR',i)
EOF
```

```
15 mean: n matches for all nine True; MAD 8/9, R2 6/9, pTRM 9/11; together 23/29 = 79%
15 first: n matches for all nine True; MAD 6/9, R2 1/9, pTRM 4/11; together 11/29 = 38%
15 mean, MAD reading a_free alone: 8/9 within tolerance; median |difference| 0.2 deg
15 mean, pTRM reading a_i alone: 3/11 within 10% of the printed value
15 mean, pTRM reading a_ii alone: 2/11 within 10% of the printed value
16 specimen     Table 2 failure   n<4  R2<0.9 pTRM>15% (reading a_i)  MAD (mean, a)
19 mean: irregular under (a) 11/11, under (b) 9/11; without the four synthetic sheets (a) 8/8, (b) 6/8
19 first: irregular under (a) 11/11, under (b) 9/11; without the four synthetic sheets (a) 8/8, (b) 6/8
20 pTRM checks matching under some reading: 6/10
29 mean: all thermal field-off steps reject randomness 8/22; within Table 2 ranges 8/22 (ranges of 2 steps: 2); without synthetic sheets 7/18
29 first: all thermal field-off steps reject randomness 9/22; within Table 2 ranges 7/22 (ranges of 2 steps: 2); without synthetic sheets 8/18
35 reading a_i: 23/24 values within tolerance
35 reading a_ii: 24/24 values within tolerance
35 Table 1 max intensity equal to the formula on its own M590, rounded up to two places: 10 / 12
35 Formula on Table 1's own M590, unrounded: {'12021g2': 0.2282, '12021g3': 0.2543, '12040g1': 0.2, '12040g2': 0.2657, '12040g3': 0.2543, '12053g1': 0.3029, '12053g2': 0.2005, '14053g1': 0.4995, '14053g2': 0.3022, '14053g3': 0.3537, '71055g1': 0.4121, '71055g3': 0.3808}
38 Within 0.18-0.22: True; within 0.45-0.55: True
44 Counts of 12: {'NRM consistent (a)': 10, 'NRM consistent (b)': 8, '590.0 inconsistent (a)': 10, '590.0 inconsistent (b)': 12, '590.3 inconsistent (a)': 10, '590.3 inconsistent (b)': 12}
50 replicates i: pass (a) 11/12, pass (b) 12/12; TRM40/(2 TRM20) 0.77 to 1.17
50 replicates ii: pass (a) 10/12, pass (b) 12/12; TRM40/(2 TRM20) 0.79 to 1.14
```

**Agent calls Bash**

```bash
sed -i 's/12053g2 (0.2004 against 0.20)/12053g2 (0.2005 against 0.20)/' $TMPDIR/build_nb.py && grep -c "0.2005 against" $TMPDIR/build_nb.py && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py
```

```
1
ok
```

**Agent**

Now the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/figshare-24639285-tarduno-2024/README.md",
 "content": "# Tarduno, Cottrell & Zhou (2024) from Figshare 24639285\n\nTests the findings of [Tarduno, Cottrell & Zhou (2024)](https://doi.org/10.1038/s41597-024-03626-0)\non [Figshare 24639285, version 1](https://doi.org/10.6084/m9.figshare.24639285.v1). The item holds\nmagnetometer measurements of the 22 Apollo 64455 glass subsamples that failed the paleointensity\nselection criteria (one workbook, one sheet per subsample) and the replicate measurements of twelve\nsingle silicate crystals (one workbook each).\n\n| Claim | Outcome |\n|---|---|\n| The deposit holds the 22 failed glass subsamples and the 12 crystals | Reproduced |\n| Success rate of the glass experiments, 12% (3 of 25) | Reproduced |\n| Table 2 fit statistics (n, MAD, R2, pTRM checks) | Partially reproduced (assumes averaged replicates) |\n| Table 2 specimens with no fit acquire TRM irregularly | Reproduced |\n| Figure 1: linear components in ss43 and ss19 | Reproduced (assumes averaged replicates) |\n| Figure 2: changing directions in ss41 and ss22 | Reproduced (assumes averaged replicates) |\n| Glass field-off directions are not random | Partially reproduced |\n| AF cleaning did not change the NRM | Reproduced |\n| Table 1 magnetization thresholds | Reproduced |\n| Baseline of 0.2 to 0.5 uT | Reproduced |\n| Technical Validation example for 14053g1 | Reproduced under the misprint reading (the numbers are 12040g1's) |\n| Crystal NRM replicates consistent, 590 C replicates and alteration checks not | Reproduced (three claims) |\n| 14053g1 stable at 400 C | Reproduced |\n| No alteration of the crystals | Reproduced |\n| Impact magnetization and no long-lived dynamo | Blocked: interpretation, not tested |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe \"replicates\" in four glass sheets (g2, ss8, ss39, ss48) are one measurement multiplied by\nfactors near 1, not repeated measurements. The attempt record, with the reasons and the\ndifferences from the paper's method, is\n[`attempts/figshare-24639285-tarduno-2024-01.yaml`](../../attempts/figshare-24639285-tarduno-2024-01.yaml).\n\n- `reproduce_tarduno_2024.ipynb`: the analysis. It runs in under a minute.\n- `apollo.py`: loading the workbooks from Figshare, the Arai and directional measures (MAD, R2,\n  pTRM checks, Fisher statistics, Watson's test) and the check for scaled copies. Other notebooks\n  on this dataset can import it.\n"
}
```

```
File created successfully at: entries/figshare-24639285-tarduno-2024/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/figshare-24639285-tarduno-2024-01.yaml",
 "content": "schema_version: 2\nid: figshare-24639285-tarduno-2024-01\ndataset:\n  archive: figshare\n  id: \"24639285\"\n  version: \"1\"\n  doi: 10.6084/m9.figshare.24639285.v1\npaper: doi:10.1038/s41597-024-03626-0\ndate: 2026-10-27\nentry: figshare-24639285-tarduno-2024\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40572290491\noutcomes:\n- claim: glass-specimen-set\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:glass-specimen-set\n  measured:\n  - 22\n  - 12\n  notes: All 22 glass specimens of Table 2 are sheets of 64455lunar_cryodata.xlsx (Table 2's s11 is\n    sheet ss11; sheet g2 labels its rows 64455g2), and all 12 crystals of Table 1 have a workbook,\n    each with steps, moments, declinations and inclinations. No other specimen is in the deposit.\n    The 10 glass specimens with AF steps (ss19, ss22, ss27, ss34, ss38, ss41, ss43, ss45, ss46,\n    ss48) are exactly those with the second mark in Table 2, and the other 12 have none, as the\n    claims file's reading of the marks has it. 71055g1 and 71055g3 have one NRM measurement each,\n    the other crystals two or three. Four glass sheets (g2, ss8, ss39, ss48) hold scaled copies of\n    one measurement in place of replicates (see findings).\n- claim: glass-success-rate\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:glass-success-rate\n  measured:\n  - 12.0\n  - 13\n  - 12\n  notes: 22 failed specimens in the deposit give 3 / 25 = 12.0%. 12 have no AF steps and 10 do;\n    with the Methods' one and two successful specimens this gives 13 and 12.\n- claim: table2-fit-statistics\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:table2-fit-statistics\n  measured:\n  - 30.1\n  - 0.96\n  - 10.25\n  - 0.90\n  - 35.36\n  - 0.38\n  - 24.06\n  - 0.38\n  - 21.18\n  - 0.89\n  - 36.77\n  - 0.89\n  - 33.33\n  - 0.23\n  - 11.49\n  - 0.60\n  - 11.95\n  - 0.03\n  - 0.79\n  notes: With the mean vector of each step's repeated measurements, n matches Table 2 for all nine\n    specimens, and 23 of 29 values match under one of the named readings (79%, the criterion asks\n    80% for reproduced and 50 to 80% for partially reproduced), MAD 8 of 9, R2 6 of 9, pTRM checks\n    9 of 11. Measured values are MAD under reading (a), a free line, and R2, in the claims file's\n    order; the last value is the fraction of the 29 values that match. MAD reading (a) alone gives\n    all 8 matching MADs (median difference 0.2 deg, six within 0.3 deg); readings (b) and (c) give\n    2 and 0. Outside tolerance under every reading are ss10's MAD (33.3 against 42.9 deg) and R2\n    (0.23 against 0.15), ss9's R2 (0.89 against 0.74), ss34's R2 (0.03 against 0.06, tolerance\n    0.006), and the pTRM checks of ss19 at 250 C (23.7 to 105.9% against 30%) and ss30 at 450 C (8.2\n    to 43.8% against 10%). The matching pTRM checks need different readings for different specimens;\n    no single reading matches more than 5 of 11. With the first measurement of each step, 11 of 29\n    values match (38%), which would not reproduce the claim. Against the stated thresholds,\n    reported and not judged, ss30 and ss34 have R2 below 0.9 and n of 4 or more, as their single\n    failure \"R2\" says; ss6 has R2 0.89 here, so its listed R2 failure follows here.\n  deviations:\n  - The paper does not say how the repeated measurements of a step (2 to 19 per step) enter Table\n    2. Assumed here that they are averaged as vectors, the usual treatment of repeated measurements\n    and the reading under which the MADs of six specimens match Table 2 to its printed digit. The\n    first measurement of each step is shown as the other reading and gives a different outcome.\n  - MAD is Kirschvink's principal component measure under the claims file's three readings, and\n    the pTRM check difference is taken on the TRM-gained axis, where Figures 1 and 2 plot the checks\n    (legends, \"red triangles represent partial thermal remanent magnetization checks\"). The paper\n    gives no formula for either; it names PmagPy and \"standard paleointensity definitions\"\n    (Technical Validation).\n  - ss6's 250.1 step holds 19 rows in two groups of directions (inclination near 71 and near -13\n    deg); all are averaged, as for every step.\n- claim: table2-no-fit\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:table2-no-fit\n  notes: Under reading (a), TRM gained not increasing at every step, all 11 specimens marked \"no\n    regular TRM acquisition\" are irregular (9 of 11 under reading b, a fall of more than 15%); the\n    same with first measurements. Without the four synthetic sheets (g2, ss8, ss48 among the 11),\n    8 of 8 under (a) and 6 of 8 under (b). ss36 and ss39 have field-off vectors that move away from\n    the origin over the last step of their ranges (ss36 1.77 to 6.00, ss39 2.31 to 9.67, in 1e-9\n    emu). Reading (a) counts any fall; the median standard error of the mean TRM gained is 1 to 6%\n    of the TRM gained for the non-synthetic specimens. The pTRM checks of these specimens, reported\n    only, match Table 2 under some reading for 6 of 10; ss36 has no pTRM check at 450 C in its sheet\n    although Table 2 prints 25%, and ss27 has 5 paired steps from 100 to 550 C where Table 2 gives 6.\n  deviations:\n  - Repeated measurements averaged as in table2-fit-statistics; first measurements give the same\n    counts.\n- claim: fig1-linear-components\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:fig1-linear-components\n  notes: With averaged replicates and MAD reading (a), ss43 has MAD 10.3 deg and R2 0.90 (Table 2\n    10.0 and 0.90) and ss19 MAD 30.1 deg and R2 0.96 (30.1 and 0.94). Nominal paleointensities,\n    |slope| x 18 uT, are 9.6 uT for ss43 and 23.0 uT for ss19 (8.5 and 23.7 uT with first\n    measurements); the figure's values were not available to compare. With first measurements\n    ss43's R2 is 0.99, outside 0.90 plus or minus 0.09.\n  deviations:\n  - Rests on the averaging of repeated measurements assumed in table2-fit-statistics.\n- claim: fig2-changing-field\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:fig2-changing-field\n  notes: With averaged replicates, ss41 (500 to 580 C) turns 33.3 deg between its first and last\n    field-off directions against a line MAD of 24.1 deg, and a great circle fits with MAD 15.1 deg;\n    ss22 (250 to 500 C) turns 107.8 deg against a line MAD of 35.4 deg, great-circle MAD 32.0 deg.\n    Both readings hold for both specimens, also with first measurements. R2 is 0.384 and 0.378\n    (0.38 plus or minus 0.038); with first measurements it is 0.16 and 0.44, outside tolerance.\n  deviations:\n  - Rests on the averaging of repeated measurements assumed in table2-fit-statistics.\n  - The great circle is fit through the origin (Kirschvink's plane MAD), a standard choice; the\n    paper gives no fitting method.\n- claim: glass-directions-not-random\n  outcome: partially_reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:glass-directions-not-random\n  measured: 8\n  notes: Watson's test rejects randomness of the thermal field-off directions (one per step, 2 to 9\n    steps) in 8 of 22 specimens with averaged replicates and 9 of 22 with first measurements,\n    between a quarter and a half. Within the Table 2 ranges, 8 of 22 (7 with first measurements).\n    Without the four synthetic sheets, 7 of 18. ss38 (k 27.9, p 0.0001), ss45, ss9, ss8, ss19,\n    ss41, s11 and ss6 reject; ss39 and ss48 have two thermal steps each.\n  deviations:\n  - The p-value of Watson's test is computed exactly by simulation (200000 sets of uniform\n    directions, fixed seeds), a standard form of the test the claims file names.\n- claim: glass-af-no-change\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:glass-af-no-change\n  measured: 8\n  notes: Under both readings 8 of the 10 AF-treated specimens show no significant change; the\n    direction after the last AF step is within 2.8 deg of the NRM and the moment within 1.1%. ss38\n    keeps its direction (2.4 deg) but its moment falls to 0.49 of the NRM at 20 mT, and ss48, a\n    synthetic sheet, turns 17.5 deg and falls to 0.67. The same counts with first measurements.\n- claim: table1-max-intensity\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:table1-max-intensity\n  measured:\n  - 7.011e-9\n  - 0.228\n  - 6.292e-9\n  - 0.254\n  - 8.002e-9\n  - 0.200\n  - 6.021e-9\n  - 0.266\n  - 6.292e-9\n  - 0.254\n  - 5.283e-9\n  - 0.303\n  - 7.982e-9\n  - 0.200\n  - 3.203e-9\n  - 0.500\n  - 5.294e-9\n  - 0.302\n  - 4.523e-9\n  - 0.354\n  - 3.883e-9\n  - 0.412\n  - 4.202e-9\n  - 0.381\n  notes: Under reading (b), M590 the moment of the single 590.1 measurement, all 24 values are within\n    tolerance and the 12 M590 values equal Table 1 to its four digits; the max intensities run from\n    0.200 to 0.500 uT. Reading (a) with averaged 590.0 replicates also gives 24 of 24, and with the\n    first replicate 23 of 24. Table 1's max intensities equal the formula on its own M590 column\n    rounded to two places for 4 of 12 crystals, and rounded up for 10 of 12; the exceptions are\n    14053g1 (0.4995, printed 0.51) and 12053g2 (0.2005, printed 0.20). The equal M590 of 12021g3\n    and 12040g3 (6.292e-09 emu) is in the data, two 590.1 measurements with different directions.\n- claim: baseline-range\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:baseline-range\n  measured:\n  - 0.200\n  - 0.500\n  notes: The twelve values of table1-max-intensity under reading (b) run from 0.200 uT (12040g1) to\n    0.500 uT (14053g1); under reading (a) from 0.203 or 0.204 to 0.501 or 0.503 uT.\n- claim: example-14053g1-threshold\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:example-14053g1-threshold\n  measured:\n  - 8.002e-12\n  - 0.200\n  notes: Matches under reading (b) only, the misprint reading the criterion names. For 14053g1 the\n    data give a TRM at 590 C of 3.203e-12 A m2 and 0.500 uT, not the example's 8e-12 and 0.2; for\n    12040g1 they give 8.002e-12 A m2 and 0.200 uT, the example's numbers. The values recorded are\n    12040g1's.\n  deviations:\n  - The example's crystal name is read as a misprint for 12040g1, as the criterion's reading (b)\n    allows; as written, for 14053g1, the example does not match the data.\n- claim: fig3-nrm-consistent\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:fig3-nrm-consistent\n  measured: 10\n  notes: Under reading (a) the NRM replicates have a higher Fisher k than the 590.0 replicates in 10\n    of 12 crystals, including 12040g1 (k 981) and 14053g2 (k 206); under reading (b) Watson's test\n    rejects randomness of the NRM replicates in 8 of 12. 71055g1 and 71055g3 have one NRM\n    measurement and count as not consistent. With two or three replicates per crystal, k and the\n    test rest on few directions (12040g3 NRM k 1.3, 12053g1 k 9.8).\n- claim: fig3-590-inconsistent\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:fig3-590-inconsistent\n  measured: 12\n  notes: Under reading (b) Watson's test does not reject randomness of the 590.0 replicates in any of\n    the 12 crystals (p 0.34 to 0.99, k 0.8 to 1.8); under reading (a) their k is below the NRM's in\n    the 10 crystals with more than one NRM measurement. The 590.0 moments average 1.16e-10 to\n    5.68e-10 emu per crystal, and all 37 single 590.0 measurements are above the 8e-11 emu\n    threshold.\n- claim: fig3-alteration-check-inconsistent\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:fig3-alteration-check-inconsistent\n  measured: 12\n  notes: Watson's test does not reject randomness of the 590.3 replicates in any of the 12 crystals\n    (reading b); their k is below the NRM's in 10 of 12 (reading a). Mean 590.3 moments are 2.14e-10\n    to 5.12e-10 emu.\n- claim: crystal-14053g1-400c-stable\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:crystal-14053g1-400c-stable\n  notes: The deposit holds three 400 C zero-field measurements of 14053g1, with one 400.1 and two\n    400.3 rows. The 400 C replicates are grouped (k 78, alpha95 14 deg, Watson p 0.0003) and the\n    590.0 replicates are not (k 1.0, p 0.79), so reading (a) holds. Under reading (b) the 400 C mean\n    is 9.3 deg from the NRM mean, outside the NRM's alpha95 of 4.0 deg (two NRM measurements). The\n    moment falls from 1.24e-09 emu (NRM) to 8.2e-10 (400 C) and 1.2e-10 (590 C).\n- claim: no-alteration-recording-efficiency\n  outcome: reproduced\n  notebook: reproduce_tarduno_2024.ipynb\n  output: claim:no-alteration-recording-efficiency\n  notes: Under reading (b) every crystal passes; the 40 uT TRM is 0.77 to 1.17 times twice the 20 uT\n    TRM (0.79 to 1.14 with averaged 590.0 and 590.3 replicates), against the cutoff of 2. Under\n    reading (a) 11 of 12 pass with first replicates and 10 of 12 with means; 14053g1's 590.3 moment\n    exceeds its 590.0 moment by 9.8e-11 to 1.21e-10 emu, and 14053g3's by 9.9e-11 with means.\n  deviations:\n  - The cutoff of 2 on the ratio is the claims file's, not the paper's; the largest ratio, 1.17, is\n    far from it.\n- claim: interpretation-impact-no-dynamo\n  outcome: blocked\n  blocked_by: other\n  notes: The claims file says this interpretation is not tested, as it rests on ref. 1 and on models\n    of impact plasmas, and is judged from four other claims. Their outcomes here are\n    fig2-changing-field reproduced, glass-directions-not-random partially reproduced,\n    fig3-590-inconsistent reproduced and table1-max-intensity reproduced.\nfindings:\n- kind: other\n  statement: In four glass sheets of 64455lunar_cryodata.xlsx (g2, ss8, ss39, ss48) the rows given\n    as repeated measurements of each step are one row multiplied by factors between 0.95 and 1.03.\n    In g2, ss8 and ss39 the same factor multiplies the moment, the declination and the inclination\n    of a row; in ss48 each column has its own factors. Every step of these sheets is built this way\n    and no step of the other 18 sheets or the 12 crystal files is. These rows are not measurements,\n    and the scaling of a declination has no physical meaning (one ss8 declination becomes 361.7\n    deg). The deposit does not say how they were made.\n- kind: format_error\n  statement: Values outside their ranges or format in 64455lunar_cryodata.xlsx; sheet ss19, 10 mT\n    step, an inclination of -136 deg (likely -13.6); sheet ss8, NRM, a declination of 361.692 deg;\n    sheet ss18, row 41, a 250 C row with no moment, declination or inclination; sheet ss48 has an\n    extra column CSD before the moment, so its columns differ from the Data Records' description.\n- kind: metadata_insufficient\n  statement: The glass sheets hold 2 to 19 repeated measurements per step, and neither the deposit\n    nor the paper says how they were combined for Table 2 and Figures 1 and 2. The mean vector\n    reproduces most of Table 2; the first measurement does not. Sheet ss6's 250.1 step holds 19 rows\n    in two groups of directions (inclination near 71 deg and near -13 deg). NRM is labelled both 0\n    and 0.0 in ss27 and ss38.\n- kind: methods_unavailable\n  statement: Questions for the paper's authors. (1) Were the repeated measurements of each step\n    averaged as vectors for Table 2 and Figures 1 and 2, or was one measurement used? (2) Is MAD a\n    free (unanchored) line fit to the field-off vectors, without the three-point smoothing? A free fit\n    to averaged replicates gives 8 of the 9 printed MADs. (3) How is the pTRM check percentage\n    defined (denominator, and which field-off step the check is referred to)? No single definition\n    tried here gives more than 5 of the 11 printed values. (4) Which measure supports \"consistent\"\n    and \"inconsistent\" for the crystal replicates? (5) Were Table 1's max intensities rounded up?\n    Ten of twelve equal the formula rounded up, not rounded.\n- kind: paper_inconsistency\n  statement: The Technical Validation example of the threshold for 14053g1 uses a TRM of 8e-12 A m2\n    and gives 0.2 uT; the data and Table 1 give 3.2e-12 A m2 and 0.50 to 0.51 uT for 14053g1, and the\n    example's numbers are those of 12040g1. The text before Figure 3 names 12041g1, which is not a\n    specimen of the deposit; the Figure 3 legend has 12040g1.\n- kind: paper_inconsistency\n  statement: Table 2 gives ss36 a pTRM check at 450 C (25%), but its sheet has no pTRM check step,\n    and gives ss27 6 points from 100 to 550 C where its sheet has 5 paired steps (100, 305, 400, 500,\n    550 C).\n- kind: metadata_insufficient\n  statement: The laboratory field of the glass experiments differs between sheets, 18 uT (10\n    sheets), 15 uT (11) and 14.4 uT (g2), given in a footnote of each sheet. The paper states only\n    the 18 uT of Figure 1.\n- kind: other\n  statement: The crystals' moments after zero-field heating to 590 C (37 measurements, 1.0e-10 to\n    5.7e-10 emu per measurement) are all above the 8e-11 emu magnetometer threshold the paper uses\n    for its bound on paleointensity. The directions of these measurements are random by Watson's\n    test in every crystal.\n- kind: metadata_error\n  statement: The item's description lists files named \"SI Figure 1 - Other Thelliers n=18.pdf\" and\n    \"SI Figure 2 - All Stereonets copy.pdf\", while the files are \"SupplFig1 - other Thelliers March\n    2024.pdf\" and \"SuppFig2 - All Stereonet.pdf\". The item's title differs from the paper's.\n"
}
```

```
File created successfully at: attempts/figshare-24639285-tarduno-2024-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=entries/figshare-24639285-tarduno-2024 python -c "
import pickle; files,g,c=pickle.load(open('$TMPDIR/cache.pkl','rb'))
import pandas as pd; d=pd.concat([v['data'] for v in c.values()]); x=d[d.step=='590']; print(len(x), x.moment.min(), x.moment.max())
" && sed -i 's/moment exceeds its 590.0 moment by 1.0e-10 to 1.2e-10 emu, above the 8e-11 emu allowance./moment exceeds its 590.0 moment by 9.8e-11 to 1.21e-10 emu, above the 8e-11 emu allowance./' $TMPDIR/build_nb.py && grep -c "9.8e-11 to 1.21e-10" $TMPDIR/build_nb.py && python $TMPDIR/build_nb.py && python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -4; date -u
```

```
37 1.024e-10 6.029e-10
1
ok
Installed kernelspec registry-figshare-24639285-tarduno-2024 in executed/figshare-24639285-tarduno-2024/.venv/share/jupyter/kernels/registry-figshare-24639285-tarduno-2024
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (27 s)
Tue Oct 27 20:04:43 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/(37 measurements, 1.0e-10 to\n    5.7e-10/X/' attempts/figshare-24639285-tarduno-2024-01.yaml; python - <<'EOF'
p='attempts/figshare-24639285-tarduno-2024-01.yaml'
s=open(p).read()
a="(37 measurements, 1.0e-10 to\n    5.7e-10 emu per measurement)"
assert a in s
s=s.replace(a,"(37 measurements, 1.0e-10 to\n    6.0e-10 emu per measurement)")
open(p,'w').write(s)
EOF
grep -nE "^\s+[^-#].*: " attempts/figshare-24639285-tarduno-2024-01.yaml | grep -vE "^\s*[0-9]+:\s+[a-z_]+: " | head; grep -n "—\|rather\|\*\*" attempts/figshare-24639285-tarduno-2024-01.yaml entries/figshare-24639285-tarduno-2024/README.md entries/figshare-24639285-tarduno-2024/apollo.py | head
```

```
entries/figshare-24639285-tarduno-2024/apollo.py:77:    with fsspec.open(url, block_size=2**20) as f:
entries/figshare-24639285-tarduno-2024/apollo.py:213:    return float(np.corrcoef(x, y)[0, 1] ** 2)
entries/figshare-24639285-tarduno-2024/apollo.py:302:        c = 1 - (n - R) / R * ((1 / 0.05) ** (1 / (n - 1)) - 1)
```

**Agent calls Bash**

```bash
grep -n "—\|rather" $TMPDIR/build_nb.py | head; . $TMPDIR/dev/bin/activate && python tools/entry.py check entries/figshare-24639285-tarduno-2024 && python tools/entry.py handover entries/figshare-24639285-tarduno-2024 && ls executed/figshare-24639285-tarduno-2024/handover; git status --short
```

```
0 error(s)
wrote executed/figshare-24639285-tarduno-2024/handover
10.1038-s41597-024-03626-0.yaml
apollo.py
reproduce_tarduno_2024.ipynb
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
?? attempts/figshare-24639285-tarduno-2024-01.yaml
?? entries/figshare-24639285-tarduno-2024/
?? scripts
```

**Agent calls Bash**

```bash
ls -la .bash_profile .bashrc .gitconfig .profile .ripgreprc .zprofile .zshrc .mcp.json; ls -la .idea .vscode scripts | head -20; ls entries/figshare-24639285-tarduno-2024/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 19:47 scripts
README.md
__pycache__
apollo.py
entry.yaml
reproduce_tarduno_2024.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

The stray dotfiles are sandbox device mounts, not files I created, so I'm leaving them. Removing the `__pycache__` my runs left in the entry.

**Agent calls Bash**

```bash
rm -rf entries/figshare-24639285-tarduno-2024/__pycache__ && ls entries/figshare-24639285-tarduno-2024/ && date -u
```

```
README.md
apollo.py
entry.yaml
reproduce_tarduno_2024.ipynb
requirements.in
requirements.lock.txt
Tue Oct 27 20:05:33 UTC 2026
```

**Agent**

I wrote the entry, the record and the handover package. The notebook runs in 27 s in a clean environment, `entry.py check` reports 0 errors, and nothing was committed. One claim misses its bar narrowly: the Table 2 fit statistics match 23 of 29 values (79%, the criterion asks for 80%), so it is partially reproduced.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| glass-specimen-set (link) | reproduced |
| glass-success-rate | reproduced |
| table2-fit-statistics | partially reproduced, rests on an assumption (23 of 29 values) |
| table2-no-fit | reproduced |
| fig1-linear-components | reproduced, rests on an assumption |
| fig2-changing-field | reproduced, rests on an assumption |
| glass-directions-not-random | partially reproduced (8 of 22 specimens) |
| glass-af-no-change | reproduced (8 of 10 unchanged) |
| table1-max-intensity | reproduced (24 of 24 values) |
| baseline-range | reproduced (0.200 to 0.500 µT) |
| example-14053g1-threshold | reproduced only under the misprint reading (the numbers are 12040g1's) |
| fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent | reproduced |
| crystal-14053g1-400c-stable | reproduced |
| no-alteration-recording-efficiency | reproduced |
| interpretation-impact-no-dynamo | blocked (`other`): the claims file says it is not tested |

**2. Dataset, assumptions and questions**

What the dataset shows:
- **Synthetic replicates.** In four glass sheets (g2, ss8, ss39, ss48), the rows given as repeated measurements are one row multiplied by factors between 0.95 and 1.03. In three of them the same factor scales moment, declination and inclination; one ss8 declination becomes 361.7°. No other sheet has this pattern.
- **Bad values.**
  - ss19 has an inclination of −136.
  - ss18 has an empty row.
  - ss48 has an extra `CSD` column.
- **Undocumented details.**
  - Glass steps were measured 2 to 19 times, with nothing saying how the repeats were combined.
  - ss6's 250.1 step holds two groups of directions.
  - The lab field varies by sheet (14.4, 15 and 18 µT); the paper states only 18 µT.
- **Paper against data.**
  - The Technical Validation example for 14053g1 uses 12040g1's numbers.
  - Table 2 gives ss36 a pTRM check that is not in its sheet, and gives ss27 six points where the sheet has five.
  - Table 1's maximum intensities match the formula rounded up for 10 of 12 crystals, but rounded normally for only 4.
- **Threshold.** All 37 of the crystals' 590 °C zero-field moments are above the 8e-11 emu threshold the paper uses.
- **Item description.** The file names it lists differ from the actual file names.

Assumption: the repeated measurements of each step are averaged as vectors. With the average, a free-line MAD matches 8 of the 9 printed MADs, 6 of them within 0.3°. With the first measurement only 38% of the Table 2 values match, which would make that claim not reproduced.

Questions for the paper's authors, recorded as a `methods_unavailable` finding:
1. Were repeated measurements averaged?
2. Is MAD a free line fit?
3. How is the pTRM check percentage defined? No single definition I tried matches more than 5 of the 11 printed values.
4. What measure supports "consistent" and "inconsistent" for the crystal replicates?
5. Were the Table 1 maximum intensities rounded up?

Questions to a reader: none.

**3. Where the protocol was unclear or missing something**
1. It gives no outcome for a claim the claims file says is "not tested". I used blocked with `other` and listed the outcomes of the four claims it depends on.
2. How repeated measurements are combined was missing from the claims file and changes the outcome. I followed step 1.6: ran both ways and adopted averaging as an assumption.
3. Counting a value as matched "under any reading" inflates matches when there are many readings: each pTRM value has 4 named readings, 8 counting both ways of combining repeats. The protocol does not address this. I also printed how many values each single reading matches.
4. The example claim's criterion does not say what outcome label to give when only the misprint reading matches. I used `reproduced` under the "any reading" rule of reader step 3, and said so in the notes and a deviation.
5. The clock check in step 2 does not apply to static measurements with no time axis. The notebook says so.
6. The duplicate-recording check of step 1.2 does not cover values made up from one measurement. I adapted it to detect scaled copies, and recorded the result under `other` since no finding kind fits.
7. `tools/entry.py` needs `pyyaml`, `jsonschema` and `nbformat`, which the checkout's Python lacked. I installed them in a temporary environment.

**4. Runtime and failures**
The run took about 17 minutes (19:48 to 20:05 UTC). One notebook cell failed on the first execution (a pTRM-check table with no rows); I fixed it in the helper and nothing else failed.

Files are in `entries/figshare-24639285-tarduno-2024/`:
- `reproduce_tarduno_2024.ipynb`
- `apollo.py`
- `README.md`, `entry.yaml`, and the requirements and lock files

The record is `attempts/figshare-24639285-tarduno-2024-01.yaml`, and the verifier's package is in `executed/figshare-24639285-tarduno-2024/handover/`.

## End of run

49 turns, 16 minutes, result: success.
