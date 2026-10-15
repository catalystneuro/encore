# 000004 · verifier-1 · run 38758082243

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs 2>/dev/null; cat *.yaml *.yml *.json 2>/dev/null | head -200
```

```
total 240
drwxr-xr-x 5 runner runner    4096 Oct 15 15:16 .
drwxr-xr-x 7 runner runner    4096 Oct 15 15:16 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 15 15:16 .claude
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.development
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.local
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.production
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.test
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .env.test.local
drwx------ 2 runner runner    4096 Oct 15 15:16 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .github
-rw-r--r-- 1 runner runner       0 Oct 15 15:16 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 15:11 .mcp.json
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p 10.1038-s41597-020-0415-9.yaml; cat recogmem.py; ls .claude; ls -R .claude | head
```

```
responses. The readings of the split are (a) the fixed split of the paper's MATLAB code
    (high is 1 or 6, low is 2 to 5) and (b) the dynamic split of its Python code. Sessions
    without responses in one group are left out and counted. Reproduced when, under one reading,
    high exceeds low with a paired t-test p < 0.001. The unpaired test the code runs is a variant.
- id: vs-cells-proportion
  statement: 343 of the 1863 cells (18.4%) are visually selective, by a one-way ANOVA (P < 0.05) of
    the firing rate in recognition trials, in a 1 s window starting 200 ms after stimulus onset,
    across the 5 visual categories.
  source: Technical Validation, proportion of selective cells; Figure 5f
  expected:
  - quantity: VS cells
    value: 343
    tolerance: 34.3
  - quantity: VS cells, percent of all cells
    value: 18.4
    tolerance: 1.84
    unit: '%'
  criterion: Every unit, Methods' window. Reproduced when both values are within tolerance. The
    code's window, units of duplicated spike trains counted once, and the proportion with the
    category labels shuffled within each session (a null) are variants.
[... 411 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_chandravadia_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--> ', ''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--> ', ''.join(d['text/plain']))
            if 'image/png' in d: print('--> [image]')
        elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1113 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown
2	# Reproducing Chandravadia et al. (2020) from dandiset 000004
3	
4	**Paper.** Chandravadia N, Liang D, Schjetnan AGP, Carlson A, Faraut M, Chung JM, Reed CM, Dichter B,
5	Maoz U, Kalia SK, Valiante TA, Mamelak AN, Rutishauser U (2020). A NWB-based dataset and processing
6	pipeline of human single-neuron activity during a declarative memory task. *Scientific Data* 7, 78.
7	[doi:10.1038/s41597-020-0415-9](https://doi.org/10.1038/s41597-020-0415-9). The article is open
8	access (CC BY 4.0); this attempt used its full text, including Tables 1 and 2 and Online-only Table 1.
9	
10	**Dandiset.** [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852), version
11	0.220126.1852. The paper cites no DANDI version: its data statement points to the Open Science
12	Framework (doi:10.17605/OSF.IO/HV7JA), and the dandiset was created on 2020-03-16, after the paper
13	appeared. The archive has two published versions, 0.220126.1851 and 0.220126.1852, published a
14	minute apart with the same 87 assets (checked in the first data cell) and metadata that differs only
15	in version fields. The most recent is pinned. The draft holds the same files.
16	
17	**What the dandiset holds.** One NWB file per session: 87 sessions of 59 subjects, with the trials
18	table, the TTL event stream, the stimulus images, the spike-sorted units with mean waveforms, and
19	the electrodes table. There are no raw broadband recordings.
20	
[... 682 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 703
}
```

```
703	> The units table holds spike_times, waveform_mean_encoding, waveform_mean_recognition (sampled
704	> at 100 kHz), origClusterID, SNR, IsolDist and electrodes, with one electrode per neuron.
705	=== [28] code
706	needed = {"spike_times", "waveform_mean_encoding", "waveform_mean_recognition", "origClusterID", "SNR", "IsolationDist", "electrodes"}
707	cols_ok = sum(needed <= set(s["unit_columns"]) for s in sessions)
708	one_elec = sum(bool(np.array_equal(s["unit_electrode_index"], np.arange(1, len(s["spikes"]) + 1))) for s in sessions)
709	rates = np.unique(np.concatenate([s["waveform_rate"] for s in sessions]))
710	snr = np.concatenate([s["snr"] for s in sessions]); iso = np.concatenate([s["isolation_distance"] for s in sessions])
711	print("files with every column (IsolDist is named IsolationDist):", cols_ok, "of", len(sessions))
712	print("columns in every file:", sorted(set.intersection(*[set(s["unit_columns"]) for s in sessions])))
713	print("files where every unit links to exactly one electrode:", one_elec, "of", len(sessions))
714	print("stated waveform sampling rate (Hz):", rates, "; waveform samples:", sorted({s["waveform_shape"][1] for s in sessions}))
715	print(f"SNR: {np.isfinite(snr).sum()} of {len(snr)} finite; {np.isinf(snr).sum()} infinite; finite range {np.nanmin(snr[np.isfinite(snr)]):.2f} to {np.nanmax(snr[np.isfinite(snr)]):.2f}")
716	print(f"IsolationDist: {np.isfinite(iso).sum()} of {len(iso)} finite; {np.isnan(iso).sum()} NaN; finite range {np.nanmin(iso):.3g} to {np.nanmax(iso[np.isfinite(iso)]):.3g}; above 1e4: {(iso > 1e4).sum()}")
717	unsorted = [(s["session"], k) for s in sessions for k, sp in enumerate(s["spikes"]) if np.any(np.diff(sp) < 0)]
718	print("units whose spike times are not in increasing order:", len(unsorted), "in sessions", sorted({a for a, _ in unsorted}))
719	for a, k in unsorted:
720	    sp = by_id[a]["spikes"][k]
721	    n_dup = int(np.sum(np.diff(np.sort(sp)) == 0))
722	    if n_dup:
[... 392 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -A "Mozilla/5.0" "https://www.nature.com/articles/s41597-020-0415-9" -o paper/article.html; ls -la paper; python3 -c "
import re,html
t=open('paper/article.html',encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'\s+',' ',t)
open('paper/article.txt','w').write(t); print(len(t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/article.txt').read()
import re
for kw in ['1863','1864','89 sessions','87','200 ms','AUC','asymmetric','343','146','26 cells','bootstrap','Toronto','288','23 sessions','144-140','132-177','3%','100 kHz','first of','0 == ','new_old','Figure 5','Fig. 5','ISI','1 s','1s ']:
  for m in re.finditer(re.escape(kw),t):
    print('##',kw,':',t[max(0,m.start()-250):m.start()+300]); print()
" | head -c 40000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/article.txt').read()
i=t.find('throughout this figure'); print(t[i-100:i+600]); print()
i=t.find('Online-only Table'); 
import re
for m in re.finditer('Online-only Table 1',t): print(m.start())
i=t.find('Subject ID'); print(t[i-300:i+6000])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/article.txt').read()
print(t[47000:51000])
"; grep -o 'href="[^"]*[Tt]able[^"]*"' paper/article.html | sort -u | head; grep -o 'href="[^"]*MOESM[^"]*"' paper/article.html | sort -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; for n in 1 2 3 4; do curl -sL -A "Mozilla/5.0" "https://www.nature.com/articles/s41597-020-0415-9/tables/$n" -o table$n.html; done; python3 -c "
import re,html
for n in [1,2,3,4]:
  t=open(f'table{n}.html',encoding='utf8',errors='ignore').read()
  m=re.search(r'<table.*?</table>',t,re.S)
  if not m: print(n,'none'); continue
  x=m.group(0)
  rows=re.findall(r'<tr.*?</tr>',x,re.S)
  out=[]
  for r in rows:
    cells=[re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',c))).strip() for c in re.findall(r'<t[dh].*?</t[dh]>',r,re.S)]
    out.append('|'.join(cells))
  open(f'table{n}.txt','w').write('\n'.join(out)); print('== table',n,len(out)); print('\n'.join(out[:3]))
"
```

Result: the fetched text is not kept.

**Agent**

Paper text and tables are saved under `paper/`. Next I compare the helper's copy of Online-only Table 1 with the paper's, and then check Table 2.

**Agent calls Bash**

```bash
cd  cat paper/table2.txt; echo; python3 -c "
import recogmem as rm, re
paper=[l.split('|') for l in open('paper/table4.txt').read().splitlines()[1:]]
P={}
for r in paper:
  if len(r)<7: print('row',r); continue
  for s,v in zip(re.findall(r'\d+',r[2]),re.findall(r'\d+',r[3])): P[int(s)]=(r[0],int(v),r[4],r[5],r[6])
T=rm.online_table_1()
H={r.session:(r.table_subject,r.variant,str(r.age),r.sex,r.diagnosis) for r in T.itertuples()}
print(len(P),len(H), set(P)^set(H))
for k in P:
  if P[k]!=H.get(k): print(k,P[k],H.get(k))
subj={}
for r in paper:
  if len(r)>=7: subj[r[0]]=r[5]
from collections import Counter; print(Counter(subj.values()), len(subj))
print(sum(int(r[1]) for r in paper if len(r)>=7))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "import numpy,pandas,scipy;print('ok')"; mkdir -p $TMPDIR/stub; for m in h5py remfile; do echo "" > $TMPDIR/stub/$m.py; done; mkdir -p $TMPDIR/stub/dandi; echo "" > $TMPDIR/stub/dandi/__init__.py; echo "DandiAPIClient=None" > $TMPDIR/stub/dandi/dandiapi.py; PYTHONPATH=$TMPDIR/stub python3 -c "
import recogmem as rm, re
paper=[l.split('|') for l in open('paper/table4.txt').read().splitlines()[1:]]
P={}
for r in paper:
  if len(r)<7: print('row',r); continue
  for s,v in zip(re.findall(r'\d+',r[2]),re.findall(r'\d+',r[3])): P[int(s)]=(r[0],int(v),r[4],r[5],r[6])
T=rm.online_table_1()
H={r.session:(r.table_subject,r.variant,str(r.age),r.sex,r.diagnosis) for r in T.itertuples()}
print(len(P),len(H), set(P)^set(H))
for k in P:
  if P[k]!=H.get(k): print(k,P[k],H.get(k))
subj={}
for r in paper:
  if len(r)>=7: subj[r[0]]=r[5]
from collections import Counter; print(Counter(subj.values()), len(subj))
print('sum Number of Sessions col', sum(int(r[1]) for r in paper if len(r)>=7))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which -a python python3 uv pip conda 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head; python3 -m pip --version 2>&1 | head -2
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/pip
/usr/bin/pip
/bin/pip
/usr/bin/conda
/bin/conda
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy pandas scipy 2>&1 | tail -2; python -c "import scipy; print(scipy.__version__)"
```

```
1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PY=$TMPDIR/v/bin/python; PYTHONPATH=$TMPDIR/stub $PY -c "
import recogmem as rm, re
paper=[l.split('|') for l in open('paper/table4.txt').read().splitlines()[1:]]
P={}
for r in paper:
  if len(r)<7: print('row',r); continue
  for s,v in zip(re.findall(r'\d+',r[2]),re.findall(r'\d+',r[3])): P[int(s)]=(r[0],int(v),r[4],r[5],r[6])
T=rm.online_table_1()
H={r.session:(r.table_subject,r.variant,str(r.age),r.sex,r.diagnosis) for r in T.itertuples()}
print(len(P),len(H), set(P)^set(H))
for k in P:
  if P[k]!=H.get(k): print(k,P[k],H.get(k))
subj={}
for r in paper:
  if len(r)>=7: subj[r[0]]=r[5]
from collections import Counter; print(Counter(subj.values()), len(subj))
print('sum Number of Sessions col', sum(int(r[1]) for r in paper if len(r)>=7))
"
```

Result: not kept, because it reads the paper's text.

**Agent**

Helper's copy of Online-only Table 1 matches the paper exactly (87 sessions, 25 F / 34 M). Now checking the archive for the two blocked claims and the paper's bootstrap code.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/" -o meta.json; curl -s "https://api.dandiarchive.org/api/dandisets/000004/versions/0.220126.1852/assets/?page_size=200" -o assets.json; $TMPDIR/v/bin/python -c "
import json
m=json.load(open('meta.json')); a=json.load(open('assets.json'))
print(m.get('name')); print(m.get('description','')[:1500]); print('assetsSummary',json.dumps(m.get('assetsSummary'))[:800])
print('relatedResource',json.dumps(m.get('relatedResource'),indent=0)[:2000])
print(a['count']); paths=sorted(x['path'] for x in a['results']); print(paths[:5]); print([p for p in paths if '144' in p or 'ses-144' in p])
import re; print(sorted(re.findall(r'ses-(\d+)',' '.join(paths)), key=int)[-15:] if re.findall(r'ses-(\d+)',' '.join(paths)) else paths[-12:])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in $(curl -s "https://api.github.com/repos/rutishauserlab/recogmem-release-NWB/git/trees/1d95162?recursive=1" | $TMPDIR/v/bin/python -c "import json,sys; t=json.load(sys.stdin); [print(x['path']) for x in t.get('tree',[]) if any(k in x['path'] for k in ['bootstrapMeanEqualTest','single_neuron.py','NWB_singleCellAnalysis_release.m','helper.py'])]"); do echo "=== $f"; curl -s "https://raw.githubusercontent.com/rutishauserlab/recogmem-release-NWB/1d95162/$f" > "$(basename $f)"; done; ls; cat bootstrapMeanEqualTest.m 2>/dev/null
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i -E "bootstrap|anova|window|0\.2|1\.7|1700|200|correct|stimCategory|new_old|== *1|recog" NWB_singleCellAnalysis_release.m | head -60; echo ----; grep -n -i -E "bootstrap|f_oneway|window|0\.2|1\.7|1700|correct|new_old|def " single_neuron.py helper.py | head -80
```

```
15:analysisMode = params.analysisMode;   % 1 is recog, 2 is learn  (which part of the task is analyzed)
23:if analysisMode==1
24:    %Recognition part
25:    periods_toProcess = params.periodsRecog;
29:    stimuliCategories = params.stimuliRecog;
31:    recogResponses = params.recogResponses;     % response that was given (1-6)
32:    correctIncorrect=zeros(1,length(recogResponses));
33:    correctIncorrect( find(params.newOldRecogLabels'==0 & params.recogResponses<=3) ) = 1;
34:    correctIncorrect( find(params.newOldRecogLabels'==1 & params.recogResponses>=4) ) = 1;
35:    indsCorrect = find(correctIncorrect==1);  % only trials where ground truth and response correspond
36:    newOldRecogLabels = params.newOldRecogLabels ;  %ground truth - isOld flag. 1 is old, 0 is new
55:    recogResponses=[];
56:    correctIncorrect=[];
57:    newOldRecogLabels=[];
60:indCat1 = find( stimuliCategories == 1 );
72:countStimulus_long = extractPeriodCountsSimple( timestampsOfCell, periods_toProcess, stimOnset+200, stimOnset+1700, normalizeCounts );  % 200 to 1.7s after stim onset
86:% assess category selectivity with ANOVA
88:[pCategory,table,stats] = anovan( countStimulus_long, DVs,'alpha', 0.05,'display','off', 'model', 'interaction');
91:if analysisMode==1
92:    %only correct
[... 89 more lines not kept]
```

**Agent**

The helper's bootstrap matches the paper's `bootstrapMeanEqualTest.m` default (plain mean difference, two-sided). Now testing the helper functions on synthetic inputs.

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/stub $TMPDIR/v/bin/python -c "
import numpy as np, recogmem as rm
from scipy import stats
rng=np.random.default_rng(0)
# window_rates
sp=np.array([0.2,0.21,1.2,1.21,5.5]); print('wr',rm.window_rates(sp,np.array([0.0,5.0]),(0.2,1.2)))
# bootstrap calibration under null & power
ps=[rm.bootstrap_p(rng.poisson(3,50).astype(float),rng.poisson(3,50).astype(float),rng) for _ in range(2000)]
print('boot null frac<0.05',np.mean(np.array(ps)<0.05))
# compare to welch t
z=rng.poisson(3.6,50).astype(float); y=rng.poisson(3,50).astype(float); print('boot vs t',rm.bootstrap_p(z,y,rng),stats.ttest_ind(z,y).pvalue)
# anova null
ps=[rm.anova_p(rng.poisson(2,100).astype(float),np.repeat(np.arange(5),20)) for _ in range(2000)]; print('anova null',np.mean(np.array(ps)<0.05))
# AUC: perfect, chance, equal-variance gaussian d'=1
lab=np.r_[np.ones(50),np.zeros(50)].astype(int)
print('auc perfect',rm.auc(lab,np.r_[np.full(50,6),np.full(50,1)]))
def sim(dp,sig_old,n=50000):
  lab=np.r_[np.ones(n),np.zeros(n)].astype(int)
  x=np.r_[rng.normal(dp,sig_old,n),rng.normal(0,1,n)]
  resp=np.digitize(x,[-1,-0.3,0.3,1,1.6])+1
  return lab,resp
for dp,s in [(0,1),(1,1),(1,1.4)]:
  l,r=sim(dp,s); print('d',dp,'sigold',s,'auc',round(rm.auc(l,r),3),'theory',round(stats.norm.cdf(dp/np.sqrt(1+s**2)),3),'zslope',round(rm.zroc_slope(l,r),3),'expected',round(1/s,3))
# confidence accuracy
l=np.array([1,1,0,0]); r=np.array([6,4,1,5]); print('acc fixed',rm.confidence_accuracy(l,r,'fixed'))
print('isi', rm.isi_fraction(np.array([0,0.001,0.1,0.2])))
"
```

```
wr [2. 1.]
boot null frac<0.05 0.0535
boot vs t 0.137 0.15217318919105097
anova null 0.048
auc perfect 0.9851
d 0 sigold 1 auc 0.499 theory 0.5 zslope 0.999 expected 1.0
d 1 sigold 1 auc 0.749 theory 0.76 zslope 0.992 expected 1.0
d 1 sigold 1.4 auc 0.713 theory 0.719 zslope 0.711 expected 0.714
acc fixed (np.float64(100.0), np.float64(50.0))
isi 0.3333333333333333
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -c "^- id:" 10.1038-s41597-020-0415-9.yaml; $TMPDIR/v/bin/python -c "
import json; a=json.load(open('assets.json')); print([x['path'] for x in a['results'] if 'P28HMH' in x['path'] or 'P44HMH' in x['path'] or 'P48HMH' in x['path']])"
```

```
24
['sub-P28HMH/sub-P28HMH_ses-20100313_ecephys+image.nwb', 'sub-P44HMH/sub-P44HMH_ses-20000101_ecephys+image.nwb', 'sub-P48HMH/sub-P48HMH_ses-20141201_ecephys+image.nwb']
Shell cwd was reset to
```

**Agent**

## Verifier report, round 1: Chandravadia et al. 2020 on dandiset 000004 (0.220126.1852)

Of the 24 claims in the claims file, I find 10 reproduced, 8 partially reproduced, 4 not reproduced and 2 blocked.

What I checked independently:
- The paper's full text and tables are saved in `paper/`.
- The helper's copy of Online-only Table 1 matches the paper's table exactly: 87 sessions, 59 subjects, 25 F and 34 M.
- I tested the helper functions on synthetic data:
  - Under the null, `bootstrap_p` gives 5.4% below 0.05 and `anova_p` gives 4.8%.
  - With equal-variance signals, `zroc_slope` returns about 1.0. With old-item SD 1.4 it returns 0.71, where 0.714 is expected.
  - `auc` matches theory to within the trapezoid bias (0.749 against 0.760).
  - `window_rates` counts spikes in (start, stop].
- I compared `bootstrap_p` with `bootstrapMeanEqualTest.m` at commit 1d95162. That function's default (`varCorrection=0`) uses the plain mean difference, so the helper matches it.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| counts-neurons-subjects | reproduced | Cell 12 counts 1864 unit rows (+1 against 1863) and 59 subjects. With duplicated spike trains counted once the count is 1809, also within tolerance. |
| counts-sessions | reproduced | Cell 14: the 87 (subject, session) pairs in the files equal those in Online-only Table 1. The Methods' "89" does not match. |
| table1-demographics | partially_reproduced | Cell 16: 56 of 59 subjects match on age and sex. C24 and H33 differ in age; H48 differs in age (32 vs 54) and sex. The files give F 26 / M 33 against the table's 25 / 34, which is within tolerance. |
| task-structure | partially_reproduced | Cell 18: 79 of 87 sessions have 100 encoding trials with distinct images. All 87 have 100 recognition trials split 50/50 and 5 categories. |
| new-old-label-coding | not_reproduced | Both tests come out reversed. Cell 20: label-1 images appear in the encoding block (median 1.0, against 0.0 for label 0), and label 1 gets more "old" responses in 86 of 87 sessions. The file description repeats the paper's wrong coding. |
| ttl-codes | partially_reproduced | Cell 22: 78 of 87 files meet every condition. The other 9 contain codes not in Table 1 (0, 4, 22, 23, 98, 99). 17019 of 17047 trials show the sequence in order. |
| experiment-ids | partially_reproduced | Cell 24: 83 of 87 files pass. Sessions 55, 77, 100 and 105 use the ids 82 and 83, or 81 for a learning block. |
| session-dates | partially_reproduced | Cell 26: 86 of 87 files fall on the 1st. Session 48 is dated 2010-03-13. Session 68 is dated 2000-01-01, outside the 2006–2019 span of the other sessions. |
| units-table | partially_reproduced | Cell 28: all columns are present and each unit links to one electrode. The stated waveform rate is 98.4 kHz, within tolerance. SNR is non-finite for 86 units and IsolationDist is NaN for 493. |
| electrodes-table | not_reproduced | Cell 30: `imp` is empty for all 887 electrodes. Coordinates are missing for 99 electrodes in 8 files. |
| isi-criterion | partially_reproduced | Cell 32: 1858 of 1864 units (99.7%) are below 3%, which meets the 95% bar but not "every unit". Two of the six failures (session 58) are caused by every spike time being stored twice. |
| fig5a-mtl-locations | reproduced | Cell 34: all 1864 units are in the amygdala or hippocampus. |
| fig5c-auc-all | reproduced | Cell 36: mean 0.753, SD 0.094 (paper 0.74 ± 0.10). |
| fig5c-auc-sites | reproduced | Cell 38: CS 0.760 ± 0.085 and TWH 0.688 ± 0.138. All four values are within tolerance. Welch p = 0.16. |
| fig5b-roc-asymmetric | reproduced | Cell 40: mean z-ROC slope 0.726, t-test against 1 gives p = 1.6e-9, and 70 of 87 sessions are below 1. |
| fig5d-confidence-accuracy | reproduced | Cell 42, fixed split: 80.1% against 60.9%, paired p = 3.2e-16, over 84 sessions (3 left out). The dynamic split agrees. |
| vs-cells-proportion | reproduced | Cell 46: 332 of 1864 (17.8%), within both tolerances. The shuffled null gives 4.5%, close to the expected 5% (the paper states no chance level). The code's window gives exactly 343 (18.4%). |
| ms-cells-proportion | not_reproduced | Cell 48: the main reading gives 110 (5.9%), outside both tolerances and only just above the shuffled null of 5.3%. The code's choices (correct trials only, 200–1700 ms) give 147 (7.9%), and correct trials only in the Methods window give 143 (7.7%). |
| dual-cells-proportion | not_reproduced | Cell 50: the main reading gives 12 (0.6%), below the 19.6 expected if VS and MS were independent. The code's choices give exactly 26 (1.4%). |
| fig5f-site-proportions | partially_reproduced | Cell 52: no Fisher test finds a site difference (p = 0.36, 0.22, 1.0), but only 1 of 6 values is within tolerance. The code's choices reproduce all six paper values to within 0.1 point. |
| twh-sessions | reproduced | Cell 54: 9 sessions, all with institution "Toronto Western Hospital". |
| fig4-example-vs-neuron | reproduced | Cell 56: the single unit on channel 177 of session 132 (Right Amygdala) has ANOVA p = 1.2e-22, and animals have the highest rate (6.75 Hz against at most 0.85 Hz). |
| previous-release-additions | blocked (metadata_insufficient) | The archive does not mark which sessions were in Faraut 2018. The version metadata's relatedResource lists only OSF and the paper. Only the 9 TWH sessions (8 subjects, 77 units) are new by definition. |
| fig3-example-vs-neuron | blocked (data_missing) | No file has session id 144 (cell 3), and session 144 is not in the paper's Online-only Table 1 either (checked against the saved table). |

### B. Problems

1. [affects a conclusion] **Cells 44, 48, 50, 52: the main reading for MS cells probably differs from how the paper's numbers were computed.** The main reading follows the Methods text (all 50/50 trials, 200–1200 ms). The code's choices (`NWB_singleCellAnalysis_release.m` uses correct trials only and 200–1700 ms) reproduce 343, 147, 26 and every Fig. 5f value almost exactly. The not_reproduced outcomes for ms and dual, and the partial outcome for fig5f, therefore come from the Methods text disagreeing with the code, not from the data. The notebook prints both readings but does not state this.
2. [affects a conclusion] **Cell 48: the main-reading MS proportion is barely above chance.** It is 5.9% against a null of 5.3%, and the null uses only 5 shuffles per unit. Under the Methods' reading, MS selectivity is close to chance at the population level. Cell 50's dual count (12) is below the count expected under independence (19.6).
3. [does not affect a conclusion] **Cell 44: no seed sensitivity check.** One RNG (`rng_ms`) is shared across all bootstrap variants, and no second seed is run. With B = 1000, units near p = 0.05 can flip. That noise is far smaller than the 110 vs 146 gap, but it could matter for the 147 vs 146 match.
4. [does not affect a conclusion] **Cell 9: the shared clock is shown in only 38 of 87 sessions.** For the other 49 sessions (801 units) it is assumed. The population curve (peak 17.8% at +0.2 s, about 5% with shuffled labels) supports it overall.
5. [does not affect a conclusion] **Cell 20: the 8 short-encoding sessions are not commented on.** In these sessions only 52–58% of label-1 images (98% in session 123) appear in the file's learning block. Old images are therefore shown in recognition without an encoding trial in the file. This is a data defect beyond "fewer trials", and the notebook does not mention it.
6. [does not affect a conclusion] **Cell 16: some diagnosis differences are more than coarser coding.** For example, C61 is "Left Lateral Frontal" in the file but "Left Mesial Temporal" in the table, and C56 also differs. The notebook lists these without comment.
7. [does not affect a conclusion] **Cell 22: the TTL check has gaps.** `all_ok` does not check that the response kind matches the trial's phase. It also does not count the 7 files with no 55 marker or the file with three 66 markers.
8. [does not affect a conclusion] **Cell 30: `imp` is reported as "empty" without showing its stored values.** The dtype or a sample of values would show whether it is NaN, an empty string or a placeholder.
9. [does not affect a conclusion] **Cell 36: the "paper's coding" AUC variant is not recomputed.** It is taken as 1 − AUC. That is only approximate under the 0/1 rate adjustment, though the conclusion is unaffected.
10. [does not affect a conclusion] **Cell 40: the two p-values agree exactly.** The Wilcoxon and t-test both print p = 1.6e-9. This is plausible but unusual, and I could not check it without the slopes.
11. [does not affect a conclusion] **Cell 52: the Fisher tests have low power.** With 77 TWH units, "no difference" carries little weight. The claim of comparable proportions rests mostly on the point values.

### C. What I could not check

- **Per-unit and per-session values.** I could not recompute anything from the files themselves (by instruction). A saved table of per-unit p-values (cell 44) and per-session AUC and slope (cell 36) would let me check problems 3 and 10, and confirm 1864 against 1863 unit by unit.
- **The extra unit (1864 against 1863).** The notebook does not show which unit is extra. A per-site and per-session list of units compared with the Fig. 5e counts would show it.
- **fig3-example-vs-neuron.** A weak proxy test is possible but not run. An output listing units on origChannel 140 in the Right Hippocampus, with their phone-category ANOVA, would show whether the Figure 3 neuron exists under another session id.
- **previous-release-additions.** This needs the Faraut 2018 session list (Dryad doi:10.5061/dryad.46st5). The notebook could at least print the TWH portion (9 sessions, 8 subjects, 77 units) as a partial count.
- **The `imp` column.** An output of its dtype and unique values (problem 8).

## End of run

21 turns, 4 minutes, result: success.
