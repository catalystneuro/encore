# 000130 · author · run 38593268430

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts tools
```

```
# Protocol for an attempt

Version: `pilot-6`. Record this version in the attempt's provenance.

This is what an agent, or a person, does to attempt a target and deposit the
result. It is written from the eight pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

There are two roles. The **author** makes the attempt. The **verifier** checks
it and must not be the author: for agents, a separate run with a separate
context that has not seen the author's reasoning.

Agent runs are made with the [Agent run](../.github/workflows/attempt.yml)
workflow, one role at a time: `author`, `verifier-1`, `author-revise-1`,
`verifier-2`, `author-revise-2`, and, when the last of these proposes changes
of outcome, `verifier-3` and `author-revise-3`. Each run's transcript and final report are
kept in [`transcripts/<dandiset>/`](../transcripts).

## Author

[... 369 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls -R entries/001453-fouke-2025 claims/001453; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (52.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6d0fc731-c1c8-445c-be9d-e20fb47e0ca0/tool-results/bxis0ngbr.txt

Preview (first 2KB):
# Reproduction registry (working name)

Agents, and people, try to reproduce the key findings of papers from the open
data on the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6d0fc731-c1c8-445c-be9d-e20fb47e0ca0/tool-results/bxis0ngbr.txt"
}
```

```
1	# Reproduction registry (working name)
2	
3	Agents, and people, try to reproduce the key findings of papers from the open
4	data on the [DANDI Archive](https://dandiarchive.org), and register the result
5	here: the notebooks when it works, and the reason when it does not.
6	
7	- **For the archive:** evidence of whether each dandiset is complete and
8	  accurate enough to support the findings of its paper.
9	- **For analysts:** working notebooks to build new analyses on.
10	
11	Status: pilot. All eight pilot targets have been attempted and checked by an
12	independent agent.
13	
14	**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>
15	
16	## Reading the outcomes
17	
18	An outcome says what one attempt could recover from the data in a dandiset,
19	with the methods available to it. **A "not reproduced" or "partially
20	reproduced" outcome is not a finding that the paper is wrong.** It can come
[... 971 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 ../../claims/001453/*.yaml; echo; sed -n 1,80p omr.py
```

```
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
- id: doi:10.1016/j.cub.2025.04.027
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 30,400p claims/001453/*.yaml | head -150; ls schemas; python -c "
import json,nbformat
nb=nbformat.read('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb',4)
for c in nb.cells[:6]: print(c.cell_type, c.metadata, c.source[:1500]); print('-----')
print([ (c.cell_type,c.metadata.get('tags')) for c in nb.cells])
"
```

```
the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
    across the visual stimuli.
  source: Results, first section; Figure 1D
  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code
    the median over trials of the trial speed in pixels per second; a two-way ANOVA (type II)
    of these values on species, code and their interaction. Reproduced when the species effect
[... 235 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l tools/entry.py; grep -n "def \|conclusion\|Result\|summary\|tag" tools/entry.py | head -80
```

```
378 tools/entry.py
20:- each notebook has a cell tagged `sanity` that prints what was loaded;
31:(docs/protocol.md): the executed notebooks with the conclusions removed (every
32:markdown cell that begins "**Result:" and everything from the "## Summary"
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
75:def schema(name: str) -> Draft202012Validator:
79:def load(report: Report, path: Path):
88:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
98:def _plain(value):
109:def code_of(notebook_path: Path) -> str:
116:def check(entry_dir: Path) -> Report:
166:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
167:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
234:            tag = outcome.get("output")
235:            if notebook in present and tag:
237:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
238:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
242:def _derivation_checks(report: Report, where, code: str) -> None:
256:def lock(entry_dir: Path) -> int:
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py; sed -n 116,310p tools/entry.py
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
- each notebook, or a helper it imports, names the dandiset the entry uses;
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 235 more lines not kept]
```

**Agent**

Now the paper and the dandiset.

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000130/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  for v in 0.220113.0407 0.241017.1448; do echo "== $v"; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/$v/assets/?page_size=100" | python -c "
import json,sys
for a in json.load(sys.stdin)['results']: print(a['asset_id'],a['blob'] if 'blob' in a else '',a['path'],a['size'])"; done; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.241017.1448/" | python -m json.tool > $TMPDIR/meta_new.json; curl -s "https://api.dandiarchive.org/api/dandisets/000130/versions/0.220113.0407/" | python -m json.tool > $TMPDIR/meta_old.json; cat $TMPDIR/meta_new.json; diff $TMPDIR/meta_old.json $TMPDIR/meta_new.json
```

Result: the fetched text is not kept.

**Agent**

Both versions hold the same two blobs, so I'll pin the latest. Now the paper text.

**Agent calls Bash**

```bash
cd  curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.neuron.2019.06.012&format=json&resultType=core" | python -c "
import json,sys
r=json.load(sys.stdin)['resultList']['result']
for x in r: print(x.get('pmid'),x.get('pmcid'),x.get('isOpenAccess'),x.get('inPMC'),x.get('hasPDF'),x.get('title'), [f.get('availabilityCode') for f in x.get('fullTextUrlList',{}).get('fullTextUrl',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6805134/fullTextXML" -o paper/PMC6805134.xml; ls -la paper; python - <<'E'
import re,xml.etree.ElementTree as ET
t=ET.parse('paper/PMC6805134.xml').getroot()
def txt(e): return ''.join(e.itertext())
out=[]
for sec in t.iter():
    if sec.tag in ('title','p','caption'):
        pass
body=t.find('.//body'); 
s=[]
def walk(e,d=0):
    for c in e:
        if c.tag=='sec':
            ti=c.find('title'); s.append('\n'+'#'*(d+1)+' '+(txt(ti) if ti is not None else ''))
            walk(c,d+1)
        elif c.tag=='p': s.append(txt(c))
        elif c.tag=='fig':
            s.append('[FIG] '+' '.join(txt(x) for x in c if x.tag in('label','caption')))
        elif c.tag in ('table-wrap',): s.append('[TABLE] '+txt(c))
ab=t.find('.//abstract'); s.insert(0,'ABSTRACT '+txt(ab))
walk(body)
# also floats-group figures
for f in t.iter('fig'):
    pass
fg=t.find('.//floats-group')
if fg is not None:
    for c in fg: s.append('[FLOAT] '+txt(c))
open('paper/paper.txt','w').write('\n'.join(s))
print(len('\n'.join(s)))
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  cat paper/PMC6805134.xml; echo; curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC6805134/unicode" -o paper/bioc.xml; ls -la paper; head -c 500 paper/bioc.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm paper/PMC6805134.xml; python - <<'E'
import xml.etree.ElementTree as ET
t=ET.parse('paper/bioc.xml').getroot()
s=[]
for p in t.iter('passage'):
    inf={i.get('key'):i.text for i in p.findall('infon')}
    tx=p.findtext('text') or ''
    typ=inf.get('type','')
    if inf.get('section_type')=='REF': continue
    if typ.startswith('title'): s.append('\n## '+tx)
    elif 'caption' in typ: s.append('[FIG '+typ+'] '+tx)
    else: s.append(tx)
open('paper/paper.txt','w').write('\n'.join(s))
print(len('\n'.join(s)))
E
wc -l paper/paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/paper.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text is available (PMC author manuscript). The dandiset is the Neural Latents Benchmark DMFC_RSG set: one monkey (Haydn), one train and one test file. Let me open the files.

**Agent calls Bash**

```bash
cd  uv venv -q --python 3.13 $TMPDIR/ex && uv pip install -q --python $TMPDIR/ex/bin/python dandi h5py remfile numpy pandas pynwb scipy statsmodels scikit-learn matplotlib 2>&1 | tail -3; echo done
```

```
done
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > ex1.py <<'E'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
with DandiAPIClient() as c:
    ds=c.get_dandiset('000130','0.241017.1448')
    for a in ds.get_assets():
        url=a.get_content_url(follow_redirects=1, strip_query=True)
        print('=====',a.path,url)
        f=h5py.File(remfile.File(url),'r')
        def show(name,obj):
            if isinstance(obj,h5py.Dataset):
                print(name,obj.shape,obj.dtype, dict((k,(v.decode() if isinstance(v,bytes) else v)) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
            else:
                at={k:(v.decode() if isinstance(v,bytes) else v) for k,v in obj.attrs.items() if k not in ('object_id',)}
                print(name+'/',at)
        f.visititems(show)
        for k in ['session_description','identifier','session_start_time','general/subject/subject_id','general/subject/species','general/subject/sex','general/subject/age','general/subject/description','general/experiment_description','general/institution','general/lab','general/related_publications','general/notes']:
            if k in f: print(k, f[k][()])
E
$TMPDIR/ex/bin/python ex1.py 2>&1 | head -200
```

```
===== sub-Haydn/sub-Haydn_desc-test_ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/eaf/1fa/eaf1fa97-ce58-477d-b79d-82425cea818f
acquisition/ {}
analysis/ {}
file_create_date (1,) object {}
general/ {}
general/devices/ {}
general/devices/electrode_probe_1/ {'description': 'Linear probe with 24 recording channels', 'manufacturer': 'Plexon Inc.', 'namespace': 'core', 'neurodata_type': 'Device'}
general/devices/electrode_probe_2/ {'description': 'Linear probe with 24 recording channels', 'manufacturer': 'Plexon Inc.', 'namespace': 'core', 'neurodata_type': 'Device'}
general/devices/electrode_probe_3/ {'description': 'Linear probe with 24 recording channels', 'manufacturer': 'Plexon Inc.', 'namespace': 'core', 'neurodata_type': 'Device'}
general/experiment_description () object {}
general/experimenter (1,) object {}
general/extracellular_ephys/ {}
general/extracellular_ephys/electrode_group_1/ {'description': 'Electrodes on a neural probe', 'location': 'Dorsomedial frontal cortex', 'namespace': 'core', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrode_group_2/ {'description': 'Electrodes on a neural probe', 'location': 'Dorsomedial frontal cortex', 'namespace': 'core', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrode_group_3/ {'description': 'Electrodes on a neural probe', 'location': 'Dorsomedial frontal cortex', 'namespace': 'core', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'colnames': array(['x', 'y', 'z', 'imp', 'location', 'filtering', 'group',
       'group_name'], dtype=object), 'description': 'metadata about extracellular electrodes', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTable'}
general/extracellular_ephys/electrodes/filtering (72,) object {'description': 'description of hardware filtering', 'neurodata_type': 'VectorData'}
general/extracellular_ephys/electrodes/group (72,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part 
[... 182 more lines not kept]
```

**Agent**

The train file has the full trial table and 54 units; the test file holds 283 trials with only held-in units and no task variables. Let me look at the trials and the NLB code the dandiset links to.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > ex2.py <<'E'
import h5py, remfile, numpy as np, pandas as pd
from dandi.dandiapi import DandiAPIClient
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
with DandiAPIClient() as c:
    ds=c.get_dandiset('000130','0.241017.1448')
    urls={a.path:a.get_content_url(follow_redirects=1, strip_query=True) for a in ds.get_assets()}
out={}
for p,u in sorted(urls.items()):
    f=h5py.File(remfile.File(u),'r')
    t=f['intervals/trials']
    df=pd.DataFrame({k:(t[k][:] if t[k].dtype!=object else t[k][:].astype(str)) for k in t.attrs['colnames']})
    df['id']=t['id'][:]
    print('====',p); print(df.head(8).to_string()); print(df.describe(include='all').T.to_string())
    print(df.split.value_counts())
    u_=f['units']; idx=u_['spike_times_index'][:]; st=u_['spike_times'][:]
    print('units', len(idx), 'heldout', u_['heldout'][:].sum(), 'ids', u_['id'][:][:60])
    oi=u_['obs_intervals'][:]; oix=u_['obs_intervals_index'][:]
    print('obs_intervals first unit', oi[:oix[0]][:5], oix[:5], 'nint/unit', np.diff(np.r_[0,oix])[:5])
    print('spike range', st.min(), st.max(), 'sorted per unit', all(np.all(np.diff(s)>=0) for s in np.split(st, idx[:-1])))
    for k in ['x','y','z','imp','location','filtering','group_name']:
        v=f['general/extracellular_ephys/electrodes/'+k][:]
        print(k, v[:5], np.unique(v.astype(str)).size)
    print('keywords',f['general/keywords'][:], 'session_id', f['general/session_id'][()], 'experimenter', f['general/experimenter'][:])
    out[p]=(df, np.split(st, idx[:-1]), u_['heldout'][:])
import pickle; pickle.dump(out, open('d.pkl','wb'))
E
$TMPDIR/ex/bin/python ex2.py 2>&1
```

```
==== sub-Haydn/sub-Haydn_desc-test_ecephys.nwb
   start_time  stop_time  go_time split  id
0         0.0        1.7      1.5  test   0
1         1.8        3.5      3.3  test   1
2         3.6        5.3      5.1  test   2
3         5.4        7.1      6.9  test   3
4         7.2        8.9      8.7  test   4
5         9.0       10.7     10.5  test   5
6        10.8       12.5     12.3  test   6
7        12.6       14.3     14.1  test   7
            count unique   top freq   mean         std  min    25%    50%    75%    max
start_time  283.0    NaN   NaN  NaN  253.8  147.310692  0.0  126.9  253.8  380.7  507.6
stop_time   283.0    NaN   NaN  NaN  255.5  147.310692  1.7  128.6  255.5  382.4  509.3
go_time     283.0    NaN   NaN  NaN  255.3  147.310692  1.5  128.4  255.3  382.2  509.1
split         283      1  test  283    NaN         NaN  NaN    NaN    NaN    NaN    NaN
id          283.0    NaN   NaN  NaN  141.0   81.839273  0.0   70.5  141.0  211.5  282.0
split
test    283
Name: count, dtype: int64
units 40 heldout 0 ids [1001 1002 1003 1004 1012 1019 1024 1026 1028 1029 1030 1038 1042 1044
[... 76 more lines not kept]
```

**Agent**

Note: the `iti` column description says 500 ms for Short and 1220 for Long, the reverse of the paper; the data (trial 0, Long, iti 500) follow the paper. Now the NLB code.

**Agent calls Bash**

```bash
cd $TMPDIR; git clone -q https://github.com/neurallatents/nlb_tools.git && cd nlb_tools && git log -1 --format='%H %cd' && ls -R | head -30 && grep -rn -i "dmfc\|rsg" --include=*.py . | head -60
```

```
42f8410b88e12db136910fa2f888b025ea0aa2ae Tue Jan 27 10:07:44 2026 -0500
.:
LICENSE
README.md
data
examples
nlb_tools
pyproject.toml
requirements.txt
setup.py
tests

./data:
eval_data_test.h5

./examples:
baselines
tutorials

./examples/baselines:
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nlb_tools; sed -n 60,130p nlb_tools/make_tensors.py; sed -n 380,460p nlb_tools/evaluation.py; grep -n "def \|resample\|1 ms\|bin_width\|obs_int" nlb_tools/nwb_interface.py | head -50
```

```
'spk_field': 'spikes',
        'hospk_field': 'heldout_spikes',
        'rate_field': 'rates',
        'horate_field': 'heldout_rates',
        'behavior_source': 'data',
        'behavior_field': 'hand_vel',
        'decode_masks': lambda x: np.stack([x.ctr_hold_bump == 0, x.ctr_hold_bump == 1]).T,
        'lag': -20,
        'make_params': {
            'align_field': 'move_onset_time',
            'align_range': (-100, 500),
        },
        'eval_make_params': {
            'align_field': 'move_onset_time',
            'align_range': (-100, 500),
            'allow_overlap': True,
        },
        'fp_len': 200,
        'psth_params': {
            'cond_fields': ['cond_dir', 'ctr_hold_bump'],
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > ex3.py <<'E'
import pickle, numpy as np, pandas as pd
d=pickle.load(open('d.pkl','rb'))
tr,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
te,spk_t,_=d['sub-Haydn/sub-Haydn_desc-test_ecephys.nwb']
ok=tr.split!='none'
print('none trials with go:', (tr[~ok].go_time.notna()).sum(), 'outliers in none', tr[~ok].is_outlier.mean(), 'outliers in train/val', tr[ok].is_outlier.sum())
c=tr[tr.go_time.notna()]
print('ts vs set-ready max abs diff ms', np.nanmax(abs(c.ts-(c.set_time-c.ready_time)*1000)))
print('tp vs go-set', np.nanmax(abs(c.tp-(c.go_time-c.set_time)*1000)))
print('ts values', sorted(tr.ts.unique()), 'by prior', tr.groupby('is_short').ts.unique().to_dict())
print('iti by prior', tr.groupby('is_short').iti.unique().to_dict())
print('theta', tr.theta.unique())
g=c[~c.is_outlier]
print('completed', len(c), 'non-outlier', len(g), 'outlier frac among completed %.3f'%c.is_outlier.mean())
print(pd.crosstab([g.is_eye,g.theta,g.is_short],g.ts))
# units
dur=4809.3
fr=np.array([len(s)/dur for s in spk]); print('FR', np.round(np.sort(fr),2)); print('n >=1 sp/s', (fr>=1).sum())
# duplicates: test trials in train?
from collections import Counter
u=0
isi_tr=np.round(np.diff(spk[0]),4)
s=spk_t[0]; 
hits=0
for k in range(283):
    seg=s[(s>=te.start_time[k])&(s<te.stop_time[k])]
    if len(seg)<4: continue
    pat=np.round(np.diff(seg),4)
    # search
    L=len(pat)
    idx=np.where(isi_tr==pat[0])[0]
    if any(np.array_equal(isi_tr[i:i+L],pat) for i in idx): hits+=1
print('test trials whose unit-1001 ISI sequence occurs in train file:', hits)
# gaps in obs intervals vs trials
print('train start/stop overlap', ((tr.start_time.values[1:]-tr.stop_time.values[:-1])<0).sum())
E
$TMPDIR/ex/bin/python ex3.py
```

```
none trials with go: 23 outliers in none 0.8896103896103896 outliers in train/val 40
ts vs set-ready max abs diff ms 23.500000000140062
tp vs go-set 5322.000000000298
ts values [np.float64(480.0), np.float64(560.0), np.float64(640.0), np.float64(720.0), np.float64(800.0), np.float64(900.0), np.float64(1000.0), np.float64(1100.0), np.float64(1200.0)] by prior {False: array([ 800.,  900., 1200., 1000., 1100.]), True: array([560., 720., 800., 640., 480.])}
iti by prior {False: array([500.]), True: array([1220.])}
theta [  0. 180.]
completed 1029 non-outlier 983 outlier frac among completed 0.045
ts                     480.0   560.0   640.0   ...  1000.0  1100.0  1200.0
is_eye theta is_short                          ...                        
False  0.0   False          0       0       0  ...      30      21      25
             True          21      35      14  ...       0       0       0
       180.0 False          0       0       0  ...      16      16      18
             True          33      21      25  ...       0       0       0
True   0.0   False          0       0       0  ...      23      25      27
             True          24      27      31  ...       0       0       0
       180.0 False          0       0       0  ...      30      29      31
             True          21      28      17  ...       0       0       0

[8 rows x 9 columns]
FR [ 0.39  0.91  0.92  0.93  0.98  0.99  1.22  1.29  1.38  1.58  1.69  1.79
[... 8 more lines not kept]
```

**Agent**

48 of 54 units pass the paper's 1 spike/s rule, the same 48 as the paper's GPFA session count for monkey H. Checking tp and ts against event times more closely.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > ex4.py <<'E'
import pickle, numpy as np, pandas as pd
d=pickle.load(open('d.pkl','rb'))
tr,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
c=tr[tr.go_time.notna()].copy()
c['dtp']=c.tp-(c.go_time-c.set_time)*1000; c['dts']=c.ts-(c.set_time-c.ready_time)*1000
print(c.groupby('is_outlier').dtp.describe()); print(c.dts.describe()); print(np.histogram(c.dts,bins=[-30,-20,-10,-5,5,10,20,30]))
print(c[abs(c.dtp)>50][['ts','tp','set_time','go_time','dtp','is_outlier','split','bad_time']].head(20))
print(c[c.is_outlier][['ts','tp','dtp']].describe())
print(c.groupby('split').is_outlier.mean())
E
$TMPDIR/ex/bin/python ex4.py
```

```
count        mean         std  ...      50%      75%      max
is_outlier                                 ...                           
False       983.0   19.676031   14.219692  ...  17.9060  21.3255  200.597
True         46.0 -180.334022  877.275368  ...  17.4555  20.3560  162.416

[2 rows x 8 columns]
count    1.029000e+03
mean     1.477162e+00
std      6.735462e+00
min     -2.350000e+01
25%     -1.818989e-10
50%      0.000000e+00
75%      3.500000e+00
max      2.350000e+01
Name: dts, dtype: float64
(array([  1,  17, 102, 710,  84, 101,  14]), array([-30, -20, -10,  -5,   5,  10,  20,  30]))
          ts        tp   set_time  ...  is_outlier  split   bad_time
50    1100.0   928.147   203.0530  ...       False  train        NaN
55    1200.0  1046.283   222.3700  ...       False    val        NaN
88    1000.0   609.916   344.9715  ...        True  train        NaN
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; uv pip install -q --python $TMPDIR/ex/bin/python elephant 2>&1 | tail -2; cat > ex5.py <<'E'
import pickle, numpy as np, time, quantities as pq, neo
from elephant.gpfa import GPFA
d=pickle.load(open('d.pkl','rb'))
tr,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
fr=np.array([len(s)/4809.3 for s in spk]); keep=[s for s,f in zip(spk,fr) if f>=1]
g=tr[tr.go_time.notna() & ~tr.is_outlier & tr.is_eye & (tr.theta==0)]
sts=[]
for _,r in g.iterrows():
    a,b=r.ready_time, r.set_time
    sts.append([neo.SpikeTrain((s[(s>=a)&(s<b)]-a)*pq.s, t_start=0*pq.s, t_stop=(b-a)*pq.s) for s in keep])
print(len(sts))
for xd in [4,8]:
    t=time.time(); m=GPFA(bin_size=20*pq.ms, x_dim=xd, em_max_iters=200, verbose=False); m.fit(sts); print(xd, time.time()-t, m.score(sts) if hasattr(m,'score') else None)
E
$TMPDIR/ex/bin/python ex5.py 2>&1 | grep -v Warn | tail -5
```

```
4 21.644527435302734 -173153.27805309795
Initializing parameters using factor analysis...

Fitting GPFA model...
8 29.67946982383728 -172358.05744291496
Shell cwd was reset to
```

**Agent**

GPFA takes about 25 s per fit, so cross-validating over a small set of latent sizes fits the time budget. I have what I need to write the claims before any claim analysis.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -80; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dandiset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "dandiset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "dandiset": {
      "type": "string",
      "pattern": "^[0-9]{6}$"
    },
[... 421 more lines not kept]
```

**Agent**

Writing the claims file now, before any claim analysis.

**Agent calls Write**

```json
{
 "file_path": "claims/000130/10.1016-j.neuron.2019.06.012.yaml",
 "content": "# Claims for Sohn, Narain, Meirhaeghe & Jazayeri (2019) on dandiset 000130.\n# Source: the accepted author manuscript in PubMed Central (PMC6805134), full text, read from its\n# Results, figure legends and STAR Methods. The supplementary tables and figures were not\n# available to this attempt. The paper's analysis code is \"available on request\"; the dandiset\n# links only the Neural Latents Benchmark, whose code (nlb_tools) loads the data and scores\n# models but holds none of the paper's analyses.\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata, the columns of the trial table and their consistency with the event times, the\n# counts of trials per condition, the firing rate of each unit (48 of 54 units reach 1 spike/s),\n# and the time one GPFA fit takes. No claim's analysis had been run.\n#\n# The dandiset holds one recording session (2016-12-11) of monkey H, one of the 17 sessions of H\n# and 29 of both monkeys. Its 54 units were recorded together. A \"dataset\" here, as in the paper,\n# is one effector and target direction (4 in this session; the paper has 8, from two animals).\n#\n# Method choices fixed here, where the Methods leave them open:\n# - Behaviour uses completed trials not flagged by the file's `is_outlier` column (the paper's\n#   mixture model), and the `tp` and `ts` columns.\n# - Units: mean firing rate over the file of at least 1 spike/s and at least 5 trials in every\n#   one of the 40 conditions (prior, ts, effector, direction), as in the Methods.\n# - Firing rates: spike counts in 20 ms bins averaged over trials, in spikes/s, then smoothed with\n#   a Gaussian of SD 40 ms (the Methods' \"kernel width\"). In the estimation epoch each bin\n#   averages the trials whose Set comes after the end of the bin (attrition). In the production\n#   epoch rates are taken from Set to the shortest tp of that ts. Rates are not normalised.\n# - PCA per dataset and epoch, on the trajectories of both priors concatenated, keeping the\n#   fewest components that explain at least 75% of the variance.\n# - The encoding axis u of a prior: the mean of the difference vectors X(ts_max - d) - X(ts_min + d)\n#   for d = 0, 20, 40 ms ... while ts_min + d < ts_max - d, normalised. Xu is the projection of\n#   X(t) on u, every 20 ms from ts_min to ts_max.\n# - The Bayesian observer: continuous uniform prior over each range, Gaussian measurement noise\n#   with SD wm*ts, the posterior mean as te, production noise with SD wp*te and an offset b per\n#   prior; wm, wp, bShort and bLong fit by maximum likelihood per dataset. te(t) is the mean\n#   estimate for ts = t, computed by numerical integration over tm.\n# - Speed of a production trajectory: the mean Euclidean distance between successive 20 ms states\n#   in the production PC space, from Set to the shortest tp of that ts. The Methods' \"divided by\n#   the duration separating Set and the time of Go\" is shown as a variant.\nschema_version: 1\ndandiset: \"000130\"\npaper: doi:10.1016/j.neuron.2019.06.012\nclaims:\n- id: beh-slopes\n  statement: Regression slopes of tp on ts are positive and less than one in every condition,\n    so the animals estimated ts and their responses were biased toward the mean of the prior.\n  source: Results, Task and behavior; Figure 1E and S1; Table S1\n  criterion: For each prior, effector and direction (8 conditions), a weighted linear regression\n    of tp on ts with each trial weighted by 1 over the variance of tp at its ts. Reproduced when\n    all 8 slopes lie between 0 and 1 with 95% confidence intervals that exclude 0 and 1;\n    partially reproduced when all 8 slopes lie between 0 and 1 but some interval includes 0 or\n    1; not reproduced otherwise.\n- id: beh-overlap-prior\n  statement: At the overlapping ts of 800 ms, biases were in opposite directions for the two\n    priors (rank-sum test, p < 1e-43 in animal H over 17 sessions).\n  source: Results, Task and behavior; Figure 1E; Table S2\n  criterion: Trials with ts = 800 ms, pooled over effector and direction. Reproduced when the\n    median of tp - 800 is negative for the Short prior and positive for the Long prior and a\n    two-sided rank-sum test of tp between priors has p < 0.05. The paper's p value pools 17\n    sessions and is not expected here; the p value of this session is reported, and the test is\n    shown per effector and direction.\n- id: beh-sigmoid-increments\n  statement: Increments of tp between neighbouring ts are smaller at the extremes of the prior\n    than near its mean, as the sigmoidal Bayesian estimator predicts (signed-rank test,\n    p < 1e-11 in animal H).\n  source: Results, Task and behavior; Figure 2E and 2F\n  criterion: For each of the 8 conditions, the mean tp at each of the 5 ts; the four increments\n    between neighbours; increment at the extremes = mean of the first and last, in the middle =\n    mean of the second and third. Reproduced when the middle increment exceeds the extreme one\n    in most conditions and a two-sided Wilcoxon signed-rank test over the 8 conditions has\n    p < 0.05.\n- id: beh-long-more-bias\n  statement: Biases are larger for the Long prior than for the Short prior, as scalar\n    variability predicts; regression slopes are smaller for Long.\n  source: Results, Task and behavior; Figure 2G and 2H\n  depends_on:\n  - beh-slopes\n  criterion: With the slopes of beh-slopes, reproduced when the Long slope is below the Short\n    slope in all 4 effector and direction datasets; partially reproduced for 3 of 4; not\n    reproduced otherwise.\n- id: beh-bayes-model\n  statement: A Bayesian observer model with scalar measurement and production noise fit to the\n    behaviour captures the bias and the variance of tp in all conditions.\n  source: Results, Task and behavior; Figure 2C and 2D; Table S3\n  criterion: The model fit per dataset (4 parameters). Across the 10 prior and ts conditions of a\n    dataset, the R2 of the observed mean bias (tp - ts) by the model's predicted bias, and the\n    Pearson correlation of the observed and predicted SD of tp. Reproduced when the bias R2 is\n    at least 0.8 and the SD correlation is positive in all 4 datasets; partially reproduced when\n    only one of the two holds in all 4; not reproduced otherwise. The fitted wm and wp are\n    reported; Table S3 was not available for comparison.\n- id: glm-prior-ts\n  statement: About 30% of neurons were modulated by elapsed time (27% in monkey H) and more than\n    60% were sensitive to the prior (65% in monkey H), by a Poisson GLM of spike counts before\n    Set compared by BIC.\n  source: Results, Single-neuron response profiles; Figure 3E; Methods, Generalized linear model\n  expected:\n  - quantity: Fraction of units sensitive to the prior, monkey H\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  - quantity: Fraction of units sensitive to ts (elapsed time), monkey H\n    value: 27\n    tolerance: 2.7\n    unit: percent\n  criterion: Units as selected above. Counts in the 80 ms before each of the Short prior's ts\n    values (480 to 800 ms after Ready), from every trial whose Set comes after that time\n    (attrition), both priors. Full model log rate = prior + 5 time indicators + effector +\n    direction; prior-dependent when its BIC is below that of the model without the prior. For ts\n    dependence, a model per prior with that prior's 5 time indicators plus effector and direction\n    against the model without the time indicators; ts-dependent when the BIC favours the full\n    model in either prior. Reproduced when both fractions are within tolerance; partially\n    reproduced when one is; not reproduced otherwise. The binomial 95% interval of each fraction\n    is reported.\n- id: dfr-overlap-support\n  statement: At the overlapping ts of 800 ms, firing rates differ between priors, with the\n    largest difference during the support of the prior, between 480 and 800 ms after Ready.\n  source: Results, Single-neuron response profiles; Figure 3C and 3D\n  criterion: Per dataset, units as selected above, ts = 800 trials; per unit the difference of\n    mean rates between priors in 160 ms bins from 320 ms before Ready to 640 ms after Set; the\n    root mean square over units, averaged over the 4 datasets. Reproduced when the largest value\n    falls in a bin within 480 to 800 ms after Ready and exceeds the 95th percentile of the\n    largest value over 200 shuffles of the prior labels among ts = 800 trials; not reproduced\n    otherwise.\n- id: pca-dimensionality\n  statement: Population activity is low dimensional; 3 to 4 principal components in the\n    estimation epoch and 5 to 10 in the production epoch explain about 75% of the variance.\n  source: Results, Geometry and dynamics of population activity; Figure S3\n  criterion: The number of components needed to reach 75% of the variance, per dataset and epoch.\n    The ranges widened by 10% of each bound are 2.7 to 4.4 (3 or 4 components) in the estimation\n    epoch and 4.5 to 11 (5 to 11) in the production epoch. Reproduced when all 8 values fall in\n    their ranges; partially reproduced when at least 4 do; not reproduced otherwise.\n- id: encoding-r2\n  statement: Projections of estimation-epoch neural states onto the encoding axis match the\n    Bayesian estimates from the model fitted to the behaviour (R2 = 0.993 for the Short prior,\n    0.996 for the Long prior, monkey H, Hand Left).\n  source: Results, Encoding Bayesian estimate along curved trajectory; Figure 4C\n  depends_on:\n  - beh-bayes-model\n  expected:\n  - quantity: R2 of Xu by te, Short prior\n    value: 0.993\n    tolerance: 0.0993\n  - quantity: R2 of Xu by te, Long prior\n    value: 0.996\n    tolerance: 0.0996\n  criterion: Weighted linear regression Xu = a + b te over the 20 ms time points of the prior's\n    support, each point weighted by the number of trials it averages. The reported values can be\n    read as (a) the Hand Left dataset, the representative condition of Figure 4C, or (b) the\n    mean over the 4 datasets. Reproduced when, under one reading, both values are within\n    tolerance (R2 at least 0.894 and 0.896); partially reproduced when one is. The R2 for 1000\n    random unit vectors in the same PC space is shown as a reference.\n- id: encoding-bayes-beats-linear\n  statement: Neural projections are better explained by the Bayesian model than by a linear\n    function of ts with the same number of parameters, for both priors (signed-rank test on\n    RMSE, p = 0.008 for each prior).\n  source: Results, Encoding Bayesian estimate along curved trajectory; Figure 4D top\n  depends_on:\n  - encoding-r2\n  criterion: RMSE of the weighted fits Xu = a + b te and Xu = a + b ts, per dataset and prior.\n    The paper's p = 0.008 is the smallest a signed-rank test gives over 8 datasets, so the\n    Bayesian model was better in all 8. Reproduced when the Bayesian RMSE is lower in all 4\n    datasets for both priors; partially reproduced when it is for one prior; not reproduced\n    otherwise.\n- id: short-in-long-control\n  statement: In the Long prior during the period matched to the support of the Short prior\n    (\"Short In Long\"), there is no sigmoidal representation; the Bayesian model is not better\n    than the linear one (signed-rank test, p = 0.74).\n  source: Results, Encoding Bayesian estimate along curved trajectory; Figure 4D top\n  depends_on:\n  - encoding-r2\n  criterion: A claim of absence, judged on the paper's test. Long prior states from 480 to 800 ms\n    after Ready, an axis from the state at 480 to that at 800 ms, compared with the Short prior's\n    te and with ts as above. Reproduced when a two-sided Wilcoxon signed-rank test of the RMSE\n    difference over the 4 datasets has p >= 0.05; not reproduced when p < 0.05. The RMSE\n    difference is reported per dataset.\n- id: neural-long-more-bias\n  statement: Neural projections show more bias for the Long prior than for the Short prior, as a\n    smaller regression slope of Xu on ts (signed-rank test, p = 0.008).\n  source: Results, Encoding Bayesian estimate along curved trajectory; Figure 4D bottom\n  depends_on:\n  - encoding-r2\n  criterion: The slope of the weighted regression of Xu (spikes/s, in the shared PC space of the\n    dataset) on ts (ms), per dataset and prior. Reproduced when the Long slope is below the\n    Short slope in all 4 datasets; partially reproduced for 3; not reproduced otherwise.\n- id: speed-vs-projection\n  statement: Larger projections on the encoding axis at Set are followed by slower neural\n    trajectories in the production epoch (Pearson correlation, rho Short = -0.74, rho Long =\n    -0.51).\n  source: Results, Controlling speed based on Bayesian estimate; Figure 4E\n  depends_on:\n  - encoding-r2\n  expected:\n  - quantity: Pearson correlation of speed and Xu at Set, Short prior\n    value: -0.74\n    tolerance: 0.074\n  - quantity: Pearson correlation of speed and Xu at Set, Long prior\n    value: -0.51\n    tolerance: 0.051\n  criterion: Per prior, Xu at t = ts against the speed of the production trajectory of that ts,\n    pooled over the 4 datasets (20 points). Reproduced when both correlations are within\n    tolerance; partially reproduced when both are negative with p < 0.05 but at least one is\n    outside tolerance, or when only one is within tolerance; not reproduced otherwise.\n    Correlations within each dataset are shown as a variant.\n- id: initial-speed-biased\n  statement: The initial speed of production trajectories (Set to Set + 400 ms) is biased toward\n    the middle of the prior; its dependence on ts is shallower than the unbiased profile\n    proportional to 1/ts (signed-rank test, p < 1e-3 over conditions and animals).\n  source: Results, Controlling speed based on Bayesian estimate; Figure 4F\n  criterion: Per dataset and prior, the mean step distance between Set and Set + 400 ms (trials\n    with tp of at least 400 ms), the slope of its regression on ts, and the slope of the\n    unbiased profile speed(middle ts) x middle ts / ts. Reproduced when the measured slope is\n    shallower (less negative) than the unbiased one in most of the 8 dataset-priors and a\n    two-sided signed-rank test of the difference has p < 0.05; not reproduced otherwise.\n- id: speed-predicts-tp\n  statement: The speed of neural trajectories in the production epoch predicts the mean tp\n    (Pearson correlation, rho Short = -0.58, rho Long = -0.52).\n  source: Results, Controlling speed based on Bayesian estimate; Figure 4G\n  expected:\n  - quantity: Pearson correlation of speed and mean tp, Short prior\n    value: -0.58\n    tolerance: 0.058\n  - quantity: Pearson correlation of speed and mean tp, Long prior\n    value: -0.52\n    tolerance: 0.052\n  criterion: Per prior, the mean tp of each dataset and ts against the speed of that ts, pooled\n    over the 4 datasets (20 points). Same rule as speed-vs-projection. The trial-by-trial\n    correlation within each prior, effector and direction used by the Neural Latents Benchmark\n    is shown as a variant.\n- id: alt-speed-unmodulated\n  statement: Instantaneous speed of neural trajectories in the full neural space is not modulated\n    during the support of each prior (signed-rank test for zero regression slopes, p = 0.64 for\n    Short, p = 0.08 for Long).\n  source: Results, Alternative mechanisms (speed hypothesis); Figure 5B\n  criterion: A claim of absence, judged on the paper's test. Per dataset and prior, the distance\n    between successive 20 ms states of the smoothed rates of all selected units, over the\n    support of the prior (with attrition), regressed on time. Reproduced when a two-sided\n    signed-rank test of the 4 slopes against zero has p >= 0.05 for each prior; not reproduced\n    otherwise. With 4 datasets the test cannot reach p < 0.05; the slopes and their bootstrap\n    intervals over trials are reported as the effect size.\n- id: alt-transient-parallel\n  statement: In the first 200 ms after Set, trajectories for different ts run parallel; their\n    distance to the middle ts trajectory does not change (signed-rank test for zero slopes,\n    p = 0.92 for the shortest ts, p = 0.13 for the longest).\n  source: Results, Alternative mechanisms (transient hypothesis); Figure 5D\n  criterion: A claim of absence, judged on the paper's test. PCA per dataset on Set to Set + 200\n    ms, both priors, at least 75% of variance; per dataset and prior the distance from the\n    shortest and the longest ts trajectory to the middle ts trajectory at each 20 ms bin,\n    regressed on time. Reproduced when a two-sided signed-rank test of the 8 slopes against zero\n    has p >= 0.05 for both the shortest and the longest ts; not reproduced otherwise.\n- id: alt-threshold-monotonic\n  statement: Aligned to the response, distances between trajectories for different ts decrease\n    steadily up to movement initiation, without the converging then diverging pattern a\n    ts-dependent threshold would produce.\n  source: Results, Alternative mechanisms (threshold hypothesis); Figure 5F\n  criterion: PCA per dataset on Go - 800 ms to Go, both priors, keeping the components that\n    explain 60% of the variance (the figure legend's value). Per dataset, prior and non-middle ts\n    (32 curves), the distance to the middle ts trajectory at each 20 ms bin and the time of its\n    minimum. The paper's test (one-tailed signed-rank, p = 1.5e-4) cannot be read unambiguously,\n    so the criterion is fixed here. Reproduced when the median time of the minimum is in the last\n    40 ms before Go; partially reproduced when it is in the last 200 ms; not reproduced otherwise.\n- id: gpfa-variance-inverted-u\n  statement: The variance across single trials of the GPFA neural state at Set projected on the\n    encoding axis has an inverted-U profile over ts, lower at the extremes of each prior\n    (one-tailed signed-rank test on quadratic coefficients, p = 0.0273, monkey H).\n  source: Results, The curved manifold hypothesis captures the variance; Figure 6C\n  criterion: GPFA (20 ms bins) per dataset on single trials from Ready to Set, both priors, units\n    as selected above; the latent dimensionality chosen by 3-fold cross-validated log-likelihood\n    from 4 and 8; orthonormalised latents. Per prior, u from the trial-averaged latents with\n    attrition as above; each trial's latent state in its last bin before Set projected on u; Xu\n    z-scored over the prior's trials; the variance at each ts; the quadratic coefficient of a\n    polynomial fit of variance on ts. Reproduced when a one-tailed signed-rank test (coefficient\n    below zero) over the 8 dataset-priors has p < 0.05; not reproduced otherwise.\n- id: gpfa-mean-sigmoid\n  statement: The mean of the single-trial GPFA projections is sigmoidal (signed-rank test on\n    increments, p = 0.0078) and has a higher slope for the Short prior (one-tailed signed-rank,\n    p = 0.0625).\n  source: Results, The curved manifold hypothesis captures the variance; Figure 6D\n  depends_on:\n  - gpfa-variance-inverted-u\n  criterion: With the GPFA projections of gpfa-variance-inverted-u, not z-scored. The mean Xu at\n    each ts; increments as in beh-sigmoid-increments, compared by a two-sided signed-rank test\n    over the 8 dataset-priors (sigmoidal when middle exceeds extreme with p < 0.05); the slope of\n    mean Xu on ts per dataset and prior (higher for Short in all 4 datasets is the paper's\n    p = 0.0625). Reproduced when both parts hold; partially reproduced when one does.\n- id: rnn-curved-manifold\n  statement: Recurrent neural networks trained on the two-prior task with scalar measurement\n    noise behave like a Bayesian observer and show curved trajectories during the support of the\n    prior, like DMFC.\n  source: Results, Recurrent network models; Figure 7A to 7C and S7\n- id: rnn-perturbation\n  statement: In trained networks, compressing states along the encoding axis increases the\n    regression to the mean of tp, and translating them shifts tp.\n  source: Results, Recurrent network models; Figure 7D and 7E\n- id: monkey-g\n  statement: The behavioural and neural results hold in monkey G as in monkey H.\n  source: Results throughout; Figures 1 to 6 and S1 to S6\n"
}
```

```
File created successfully at: claims/000130/10.1016-j.neuron.2019.06.012.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Claims written. Now the helper module.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python -c "
import elephant, inspect; from elephant.gpfa import GPFA; print(elephant.__version__); print(inspect.signature(GPFA.__init__)); print([m for m in dir(GPFA) if not m.startswith('_')])"; $TMPDIR/ex/bin/python -c "import elephant.gpfa, inspect; src=inspect.getsource(elephant.gpfa.GPFA.transform); print(src[:3000])"
```

```
1.2.1
(self, bin_size=array(20.) * ms, x_dim=3, min_var_frac=0.01, tau_init=array(100.) * ms, eps_init=0.001, em_tol=1e-08, em_max_iters=500, freq_ll=5, verbose=False)
['fit', 'fit_transform', 'get_metadata_routing', 'get_params', 'score', 'set_fit_request', 'set_params', 'set_score_request', 'set_transform_request', 'transform']
    @trials_to_list_of_spiketrainlist
    def transform(
        self,
        spiketrains: Union[
            List[List[neo.core.SpikeTrain]],
            "Trials",
            List[neo.core.spiketrainlist.SpikeTrainList],
        ],
        returned_data: str = ["latent_variable_orth"],
    ) -> "GPFA":
        """
        Obtain trajectories of neural activity in a low-dimensional latent
        variable space by inferring the posterior mean of the obtained GPFA
        model and applying an orthonormalization on the latent variable space.

        Parameters
        ---------- # noqa
[... 56 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "content": "\"\"\"Loading and measures for the Ready-Set-Go data of dandiset 000130.\n\nSohn, Narain, Meirhaeghe & Jazayeri (2019), Neuron, doi:10.1016/j.neuron.2019.06.012.\n\nThe dandiset is the DMFC_RSG set of the Neural Latents Benchmark: one session of monkey H\n(Haydn, 2016-12-11). The train file holds the trial table with every task variable and the\nspike times of 54 units; the test file holds 283 further trials without task variables and\nonly 40 of the units. Analyses use the train file. Files are streamed from the archive at the\npinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- From the paper's STAR Methods: units kept with a mean rate of at least 1 spike/s and at least\n  5 trials per condition (`MIN_RATE`, `MIN_TRIALS`); 20 ms bins and a 40 ms Gaussian kernel for\n  population rates (`BIN_MS`, `SMOOTH_MS`, read here as the kernel's SD); attrition in the\n  estimation epoch; production rates up to the shortest tp of each ts; PCA keeping the\n  components that explain 75% of the variance (`VAR_KEPT`); the encoding axis from difference\n  vectors every 20 ms; the 80 ms GLM window before Set (`GLM_WINDOW_MS`) and BIC comparison;\n  the Bayesian observer with scalar measurement and production noise, a uniform prior, the\n  posterior mean, and an offset per prior; GPFA on single trials with cross-validation.\n- Common choices made here where the Methods leave it open (see the claims file): kernel width\n  read as SD; rates averaged per 20 ms bin and then smoothed; no normalisation of rates before\n  PCA; difference vectors for the encoding axis averaged up to the middle of the support;\n  speed as the mean step between successive 20 ms states; the GPFA latent dimensionality chosen\n  from `GPFA_DIMS` by 3-fold cross-validation, and `GPFA_EM_ITERS` EM iterations.\n- The flag `is_outlier` in the trial table is the paper's mixture-model exclusion and is used as\n  given; `outlier_mixture` refits that model as a check.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy import optimize, stats\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET_ID = \"000130\"\nDANDISET_VERSION = \"0.241017.1448\"\nTRAIN = \"sub-Haydn/sub-Haydn_desc-train_ecephys.nwb\"\nTEST = \"sub-Haydn/sub-Haydn_desc-test_ecephys.nwb\"\n\nMIN_RATE = 1.0         # spikes/s, Methods\nMIN_TRIALS = 5         # per condition, Methods\nBIN_MS = 20            # Methods\nSMOOTH_MS = 40         # Methods, \"Gaussian smoothing kernel width\", read as SD\nVAR_KEPT = 0.75        # Methods\nGLM_WINDOW_MS = 80     # Methods\nGPFA_DIMS = (4, 8)     # choice here; the Methods say only \"with cross validation\"\nGPFA_EM_ITERS = 100    # choice here, to keep the run short\n\nSHORT_TS = (480, 560, 640, 720, 800)\nLONG_TS = (800, 900, 1000, 1100, 1200)\nDATASETS = [(True, 0.0), (True, 180.0), (False, 0.0), (False, 180.0)]\n\n\ndef dataset_name(is_eye: bool, theta: float) -> str:\n    return f\"{'Eye' if is_eye else 'Hand'} {'Right' if theta == 0 else 'Left'}\"\n\n\ndef prior_ts(is_short: bool) -> tuple:\n    return SHORT_TS if is_short else LONG_TS\n\n\n# --- loading -------------------------------------------------------------------------------\n\ndef _str(value):\n    return value.decode() if isinstance(value, bytes) else value\n\n\ndef asset_urls() -> dict:\n    with DandiAPIClient() as client:\n        dandiset = client.get_dandiset(DANDISET_ID, DANDISET_VERSION)\n        return {a.path: a.get_content_url(follow_redirects=1, strip_query=True)\n                for a in dandiset.get_assets()}\n\n\ndef read_file(url: str) -> dict:\n    \"\"\"The trial table, units and descriptive metadata of one NWB file.\"\"\"\n    with h5py.File(remfile.File(url), \"r\") as f:\n        t = f[\"intervals/trials\"]\n        cols = [_str(c) for c in t.attrs[\"colnames\"]]\n        trials = pd.DataFrame({c: (t[c][:].astype(str) if t[c].dtype == object else t[c][:]) for c in cols})\n        descriptions = {c: _str(t[c].attrs.get(\"description\", \"\")) for c in cols}\n        u = f[\"units\"]\n        index = u[\"spike_times_index\"][:]\n        spikes = np.split(u[\"spike_times\"][:], index[:-1])\n        oi_index = u[\"obs_intervals_index\"][:]\n        obs = np.split(u[\"obs_intervals\"][:], oi_index[:-1])\n        electrodes = f[\"general/extracellular_ephys/electrodes\"]\n        meta = {\n            \"session_description\": _str(f[\"session_description\"][()]),\n            \"session_start_time\": _str(f[\"session_start_time\"][()]),\n            \"session_id\": _str(f[\"general/session_id\"][()]),\n            \"subject_id\": _str(f[\"general/subject/subject_id\"][()]),\n            \"species\": _str(f[\"general/subject/species\"][()]),\n            \"age\": _str(f[\"general/subject/age\"][()]),\n            \"related_publications\": [_str(x) for x in f[\"general/related_publications\"][:]],\n            \"electrode_location\": sorted({_str(x) for x in electrodes[\"location\"][:]}),\n            \"electrode_x_all_nan\": bool(np.isnan(electrodes[\"x\"][:]).all()),\n            \"n_electrodes\": len(electrodes[\"id\"][:]),\n        }\n    return {\"trials\": trials, \"descriptions\": descriptions, \"spikes\": spikes,\n            \"unit_ids\": u[\"id\"][:] if False else None, \"obs_intervals\": obs, \"meta\": meta,\n            \"heldout\": None} | _units(url)\n\n\ndef _units(url: str) -> dict:\n    with h5py.File(remfile.File(url), \"r\") as f:\n        return {\"unit_ids\": f[\"units/id\"][:], \"heldout\": f[\"units/heldout\"][:]}\n\n\ndef load() -> dict:\n    \"\"\"Both files of the pinned version, as returned by `read_file`.\"\"\"\n    urls = asset_urls()\n    return {\"train\": read_file(urls[TRAIN]), \"test\": read_file(urls[TEST]), \"urls\": urls}\n\n\ndef completed(trials: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Completed trials (with Set and Go) not flagged as outliers.\"\"\"\n    ok = trials.set_time.notna() & trials.go_time.notna() & ~trials.is_outlier.astype(bool)\n    return trials[ok].copy()\n\n\ndef select_units(session: dict, trials: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:\n    \"\"\"Units kept by the Methods' rule, and a table of rates and trial counts.\"\"\"\n    t0 = min(iv[0, 0] for iv in session[\"obs_intervals\"])\n    t1 = max(iv[-1, 1] for iv in session[\"obs_intervals\"])\n    observed = np.array([np.sum(iv[:, 1] - iv[:, 0]) for iv in session[\"obs_intervals\"]])\n    rate = np.array([len(s) for s in session[\"spikes\"]]) / observed\n    counts = trials.groupby([\"is_short\", \"ts\", \"is_eye\", \"theta\"]).size()\n    n_cond = len(counts)\n    min_trials = int(counts.min())\n    table = pd.DataFrame({\"unit\": session[\"unit_ids\"], \"heldout\": session[\"heldout\"], \"rate\": rate,\n                          \"observed_s\": observed})\n    keep = (rate >= MIN_RATE) & (min_trials >= MIN_TRIALS) & (n_cond == 40)\n    table[\"kept\"] = keep\n    table.attrs.update(conditions=n_cond, min_trials=min_trials, span=(t0, t1))\n    return np.flatnonzero(keep), table\n\n\n# --- spike counts and rates ----------------------------------------------------------------\n\ndef counts(spikes: list, units, align: np.ndarray, start_ms: float, stop_ms: float,\n           bin_ms: float = BIN_MS) -> np.ndarray:\n    \"\"\"Spike counts, trials x bins x units, in bins from start to stop relative to `align` (s).\"\"\"\n    edges = np.arange(start_ms, stop_ms + 1e-9, bin_ms) / 1000.0\n    out = np.empty((len(align), len(edges) - 1, len(units)))\n    for j, u in enumerate(units):\n        s = spikes[u]\n        pos = np.searchsorted(s, align[:, None] + edges[None, :])\n        out[:, :, j] = np.diff(pos, axis=1)\n    return out\n\n\ndef smooth(rate: np.ndarray) -> np.ndarray:\n    \"\"\"Gaussian smoothing along time (axis 0) with SD `SMOOTH_MS`.\"\"\"\n    return gaussian_filter1d(rate, SMOOTH_MS / BIN_MS, axis=0, mode=\"nearest\")\n\n\ndef estimation_rates(spikes, units, trials: pd.DataFrame, t_max: float):\n    \"\"\"Rates from Ready to `t_max` ms with attrition: each bin averages the trials whose Set\n    comes after the end of the bin. Returns rates (bins x units, spikes/s), bin end times (ms\n    after Ready) and the number of trials in each bin.\"\"\"\n    c = counts(spikes, units, trials.ready_time.to_numpy(), 0, t_max)\n    ends = np.arange(BIN_MS, t_max + 1e-9, BIN_MS)\n    elapsed = (trials.set_time - trials.ready_time).to_numpy() * 1000\n    use = elapsed[:, None] >= ends[None, :] - 1e-6\n    n = use.sum(0)\n    mean = np.einsum(\"tb,tbu->bu\", use, c) / np.maximum(n, 1)[:, None]\n    return smooth(mean * 1000 / BIN_MS), ends, n\n\n\ndef aligned_rates(spikes, units, align: np.ndarray, start_ms: float, stop_ms: float):\n    \"\"\"Trial-averaged smoothed rates (bins x units, spikes/s) aligned to `align`.\"\"\"\n    c = counts(spikes, units, align, start_ms, stop_ms)\n    return smooth(c.mean(0) * 1000 / BIN_MS)\n\n\ndef production_rates(spikes, units, trials: pd.DataFrame, stop_ms: float | None = None):\n    \"\"\"Rates from Set to the shortest tp of these trials (or to `stop_ms`).\"\"\"\n    if stop_ms is None:\n        stop_ms = np.floor(trials.tp.min() / BIN_MS) * BIN_MS\n    return aligned_rates(spikes, units, trials.set_time.to_numpy(), 0, stop_ms)\n\n\n# --- population measures -------------------------------------------------------------------\n\nclass PCA:\n    \"\"\"PCA on stacked rate matrices, keeping the components that reach `kept` of the variance.\"\"\"\n\n    def __init__(self, matrices: list, kept: float = VAR_KEPT):\n        data = np.vstack(matrices)\n        self.mean = data.mean(0)\n        _, s, vt = np.linalg.svd(data - self.mean, full_matrices=False)\n        self.explained = s ** 2 / np.sum(s ** 2)\n        self.n = int(np.searchsorted(np.cumsum(self.explained), kept - 1e-12) + 1)\n        self.components = vt[: self.n]\n\n    def __call__(self, x: np.ndarray) -> np.ndarray:\n        return (x - self.mean) @ self.components.T\n\n\ndef encoding_axis(states: np.ndarray, times: np.ndarray, t_min: float, t_max: float) -> np.ndarray:\n    \"\"\"Unit vector from the mean of X(t_max - d) - X(t_min + d), d = 0, 20, 40 ... ms, while\n    t_min + d < t_max - d.\"\"\"\n    vectors = []\n    d = 0.0\n    while t_min + d < t_max - d:\n        i, j = np.argmin(abs(times - (t_min + d))), np.argmin(abs(times - (t_max - d)))\n        vectors.append(states[j] - states[i])\n        d += BIN_MS\n    u = np.mean(vectors, axis=0)\n    return u / np.linalg.norm(u)\n\n\ndef step_speed(states: np.ndarray) -> float:\n    \"\"\"Mean Euclidean distance between successive states.\"\"\"\n    return float(np.mean(np.linalg.norm(np.diff(states, axis=0), axis=1)))\n\n\ndef weighted_fit(x, y, w):\n    \"\"\"Weighted least squares y = a + b x; returns a, b, weighted R2 and RMSE of the fit.\"\"\"\n    x, y, w = map(np.asarray, (x, y, w))\n    design = np.column_stack([np.ones_like(x), x])\n    sw = np.sqrt(w)\n    coef, *_ = np.linalg.lstsq(design * sw[:, None], y * sw, rcond=None)\n    pred = design @ coef\n    ybar = np.sum(w * y) / np.sum(w)\n    r2 = 1 - np.sum(w * (y - pred) ** 2) / np.sum(w * (y - ybar) ** 2)\n    rmse = float(np.sqrt(np.mean((y - pred) ** 2)))\n    return coef[0], coef[1], float(r2), rmse\n\n\ndef increments(means) -> tuple[float, float]:\n    \"\"\"Mean increment at the extremes (first and last) and in the middle (second and third)\n    of five ordered values.\"\"\"\n    d = np.diff(np.asarray(means, float))\n    return (d[0] + d[3]) / 2, (d[1] + d[2]) / 2\n\n\n# --- behaviour -----------------------------------------------------------------------------\n\ndef weighted_slope(ts, tp):\n    \"\"\"Regression of tp on ts with each trial weighted by 1 / variance of tp at its ts. Returns\n    slope, its standard error, and the 95% interval.\"\"\"\n    df = pd.DataFrame({\"ts\": ts, \"tp\": tp})\n    var = df.groupby(\"ts\").tp.transform(\"var\")\n    w = 1 / var\n    x, y = df.ts.to_numpy(), df.tp.to_numpy()\n    design = np.column_stack([np.ones_like(x), x])\n    sw = np.sqrt(w.to_numpy())\n    coef, *_ = np.linalg.lstsq(design * sw[:, None], y * sw, rcond=None)\n    resid = (y - design @ coef) * sw\n    dof = len(y) - 2\n    sigma2 = np.sum(resid ** 2) / dof\n    cov = sigma2 * np.linalg.inv((design * sw[:, None]).T @ (design * sw[:, None]))\n    se = np.sqrt(cov[1, 1])\n    q = stats.t.ppf(0.975, dof)\n    return coef[1], se, (coef[1] - q * se, coef[1] + q * se)\n\n\ndef outlier_mixture(tp: np.ndarray, ts: float, iters: int = 200) -> np.ndarray:\n    \"\"\"Posterior probability of the lapse component for each trial, under a mixture of a\n    Gaussian and a uniform distribution from 0 to 3 ts (Methods).\"\"\"\n    tp = np.asarray(tp, float)\n    mu, sd, p = np.median(tp), max(np.std(tp), 1.0), 0.05\n    lapse = 1 / (3 * ts)\n    for _ in range(iters):\n        g = (1 - p) * stats.norm.pdf(tp, mu, sd)\n        l = p * lapse * ((tp >= 0) & (tp <= 3 * ts))\n        r = l / np.maximum(g + l, 1e-300)\n        w = 1 - r\n        mu = np.sum(w * tp) / np.sum(w)\n        sd = max(np.sqrt(np.sum(w * (tp - mu) ** 2) / np.sum(w)), 1.0)\n        p = np.clip(r.mean(), 1e-6, 0.5)\n    return r\n\n\nclass BayesObserver:\n    \"\"\"Bayesian observer of the Methods: tm ~ N(ts, wm ts), te = posterior mean under a uniform\n    prior on the range of ts, tp ~ N(te + b, wp te), with an offset b per prior.\"\"\"\n\n    GRID = 400\n\n    def __init__(self, wm=0.1, wp=0.08, b_short=0.0, b_long=0.0):\n        self.wm, self.wp, self.b = wm, wp, {True: b_short, False: b_long}\n\n    @staticmethod\n    def estimator(tm: np.ndarray, lo: float, hi: float, wm: float) -> np.ndarray:\n        s = np.linspace(lo, hi, 201)\n        like = np.exp(-0.5 * ((tm[:, None] - s[None, :]) / (wm * s[None, :])) ** 2) / s[None, :]\n        return (like * s).sum(1) / np.maximum(like.sum(1), 1e-300)\n\n    def _grid(self, is_short: bool):\n        ts = prior_ts(is_short)\n        lo, hi = min(ts), max(ts)\n        tm = np.linspace(lo * (1 - 5 * self.wm), hi * (1 + 5 * self.wm), self.GRID)\n        return tm, self.estimator(tm, lo, hi, self.wm)\n\n    def _p_tm(self, tm, ts):\n        p = stats.norm.pdf(tm[None, :], ts[:, None], self.wm * ts[:, None])\n        return p / p.sum(1, keepdims=True)\n\n    def loglik(self, ts, tp, is_short: bool) -> float:\n        tm, te = self._grid(is_short)\n        p_tm = self._p_tm(tm, np.asarray(ts, float))\n        p_tp = stats.norm.pdf(np.asarray(tp, float)[:, None], te[None, :] + self.b[is_short],\n                              self.wp * te[None, :])\n        return float(np.sum(np.log(np.maximum((p_tm * p_tp).sum(1), 1e-300))))\n\n    def moments(self, ts, is_short: bool):\n        \"\"\"Mean te, and mean and SD of tp, for each ts.\"\"\"\n        tm, te = self._grid(is_short)\n        ts = np.asarray(ts, float)\n        p_tm = self._p_tm(tm, ts)\n        mean_te = p_tm @ te\n        mean_tp = mean_te + self.b[is_short]\n        second = p_tm @ (te ** 2 * (1 + self.wp ** 2))\n        sd_tp = np.sqrt(second - mean_te ** 2)\n        return mean_te, mean_tp, sd_tp\n\n    @classmethod\n    def fit(cls, trials: pd.DataFrame) -> \"BayesObserver\":\n        \"\"\"Maximum likelihood fit of wm, wp, b_short and b_long to one dataset's trials.\"\"\"\n        groups = {s: g for s, g in trials.groupby(\"is_short\")}\n\n        def nll(theta):\n            m = cls(*theta)\n            if not (0.01 < m.wm < 0.5 and 0.01 < m.wp < 0.5):\n                return 1e12\n            return -sum(m.loglik(g.ts.to_numpy(), g.tp.to_numpy(), bool(s)) for s, g in groups.items())\n\n        res = optimize.minimize(nll, x0=[0.1, 0.08, 0.0, 0.0], method=\"Nelder-Mead\",\n                                options={\"xatol\": 1e-4, \"fatol\": 1e-3, \"maxiter\": 2000})\n        model = cls(*res.x)\n        model.converged, model.nll = bool(res.success), float(res.fun)\n        return model\n\n\n# --- GPFA ----------------------------------------------------------------------------------\n\ndef estimation_spiketrains(spikes, units, trials: pd.DataFrame):\n    \"\"\"Single-trial spike trains from Ready to Set, as neo objects for elephant's GPFA.\"\"\"\n    import neo\n    import quantities as pq\n    out = []\n    for ready, set_ in zip(trials.ready_time.to_numpy(), trials.set_time.to_numpy()):\n        dur = set_ - ready\n        out.append([neo.SpikeTrain((s[(s >= ready) & (s < set_)] - ready) * pq.s,\n                                   t_start=0 * pq.s, t_stop=dur * pq.s) for s in (spikes[u] for u in units)])\n    return out\n\n\ndef fit_gpfa(spiketrains, rng: np.random.Generator):\n    \"\"\"GPFA with the latent dimensionality from `GPFA_DIMS` chosen by 3-fold cross-validated\n    log-likelihood. Returns the model fit on all trials, the chosen dimensionality and the\n    cross-validated scores.\"\"\"\n    import quantities as pq\n    from elephant.gpfa import GPFA\n    folds = rng.permutation(len(spiketrains)) % 3\n    scores = {}\n    for dim in GPFA_DIMS:\n        total = 0.0\n        for k in range(3):\n            train = [s for s, f in zip(spiketrains, folds) if f != k]\n            test = [s for s, f in zip(spiketrains, folds) if f == k]\n            m = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)\n            m.fit(train)\n            total += m.score(test)\n        scores[dim] = total\n    best = max(scores, key=scores.get)\n    model = GPFA(bin_size=BIN_MS * pq.ms, x_dim=best, em_max_iters=GPFA_EM_ITERS)\n    model.fit(spiketrains)\n    return model, best, scores\n"
}
```

```
File created successfully at: entries/000130-sohn-2019/rsg.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "old_string": "        electrodes = f[\"general/extracellular_ephys/electrodes\"]",
 "new_string": "        unit_ids, heldout = u[\"id\"][:], u[\"heldout\"][:]\n        electrodes = f[\"general/extracellular_ephys/electrodes\"]"
}
```

```
The file entries/000130-sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "old_string": "    return {\"trials\": trials, \"descriptions\": descriptions, \"spikes\": spikes,\n            \"unit_ids\": u[\"id\"][:] if False else None, \"obs_intervals\": obs, \"meta\": meta,\n            \"heldout\": None} | _units(url)\n\n\ndef _units(url: str) -> dict:\n    with h5py.File(remfile.File(url), \"r\") as f:\n        return {\"unit_ids\": f[\"units/id\"][:], \"heldout\": f[\"units/heldout\"][:]}",
 "new_string": "    return {\"trials\": trials, \"descriptions\": descriptions, \"spikes\": spikes, \"unit_ids\": unit_ids,\n            \"heldout\": heldout, \"obs_intervals\": obs, \"meta\": meta}"
}
```

```
The file entries/000130-sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the notebook. I'll generate it from a builder script so I can add the conclusions after seeing the outputs.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "old_string": "    c = counts(spikes, units, trials.ready_time.to_numpy(), 0, t_max)\n    ends = np.arange(BIN_MS, t_max + 1e-9, BIN_MS)\n    elapsed = (trials.set_time - trials.ready_time).to_numpy() * 1000\n    use = elapsed[:, None] >= ends[None, :] - 1e-6\n    n = use.sum(0)\n    mean = np.einsum(\"tb,tbu->bu\", use, c) / np.maximum(n, 1)[:, None]\n    return smooth(mean * 1000 / BIN_MS), ends, n",
 "new_string": "    c = counts(spikes, units, trials.ready_time.to_numpy(), 0, t_max)\n    elapsed = (trials.set_time - trials.ready_time).to_numpy() * 1000\n    return attrition_rates(c, elapsed)\n\n\ndef attrition_rates(c: np.ndarray, elapsed: np.ndarray):\n    \"\"\"`estimation_rates` from counts already taken (trials x bins x units from Ready).\"\"\"\n    ends = np.arange(1, c.shape[1] + 1) * BIN_MS\n    use = elapsed[:, None] >= ends[None, :] - 1e-6\n    n = use.sum(0)\n    mean = np.einsum(\"tb,tbu->bu\", use, c) / np.maximum(n, 1)[:, None]\n    return smooth(mean * 1000 / BIN_MS), ends, n"
}
```

```
The file entries/000130-sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/build_nb.py",
 "content": "\"\"\"Builds entries/000130-sohn-2019/reproduce_sohn_2019.ipynb. Conclusions come from conclusions.py if present.\"\"\"\nimport importlib.util\nimport os\nimport sys\n\nimport nbformat\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nOUT = \"entries/000130-sohn-2019/reproduce_sohn_2019.ipynb\"\nspec = importlib.util.spec_from_file_location(\"cells\", os.path.join(HERE, \"nb_cells.py\"))\ncells_mod = importlib.util.module_from_spec(spec)\nspec.loader.exec_module(cells_mod)\nresults, summary = {}, None\ncpath = os.path.join(HERE, \"conclusions.py\")\nif os.path.exists(cpath) and \"--bare\" not in sys.argv:\n    spec = importlib.util.spec_from_file_location(\"conc\", cpath)\n    conc = importlib.util.module_from_spec(spec)\n    spec.loader.exec_module(conc)\n    results, summary = conc.RESULTS, conc.SUMMARY\n\nnb = nbformat.v4.new_notebook()\nnb.metadata = {\"kernelspec\": {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"},\n               \"language_info\": {\"name\": \"python\"}}\nfor kind, src, tag in cells_mod.CELLS:\n    if kind == \"result\":\n        if tag in results:\n            nb.cells.append(nbformat.v4.new_markdown_cell(results[tag].strip()))\n        continue\n    if kind == \"md\":\n        cell = nbformat.v4.new_markdown_cell(src.strip())\n    else:\n        cell = nbformat.v4.new_code_cell(src.strip())\n    if tag:\n        cell.metadata[\"tags\"] = [tag]\n    nb.cells.append(cell)\nif summary:\n    nb.cells.append(nbformat.v4.new_markdown_cell(summary.strip()))\nnbformat.write(nb, OUT)\nprint(\"wrote\", OUT, len(nb.cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/nb_cells.py",
 "content": "CELLS = []\n\n\ndef md(s, tag=None):\n    CELLS.append((\"md\", s, tag))\n\n\ndef code(s, tag=None):\n    CELLS.append((\"code\", s, tag))\n\n\ndef result(claim):\n    CELLS.append((\"result\", None, claim))\n\n\nmd(r\"\"\"\n# Reproducing Sohn et al. (2019) from dandiset 000130\n\n**Paper.** Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical\nlatent dynamics. *Neuron* 103(5):934-947.\n[doi:10.1016/j.neuron.2019.06.012](https://doi.org/10.1016/j.neuron.2019.06.012). This attempt used\nthe full text of the accepted author manuscript in PubMed Central (PMC6805134). The supplementary\nfigures and tables (Tables S1 to S3) were not available to it.\n\n**Dandiset.** [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version\n0.241017.1448. The paper cites no DANDI version (it predates the dandiset, which was made for the\nNeural Latents Benchmark in 2021). Of the two published versions, 0.220113.0407 and 0.241017.1448,\nthis is the most recent. Both hold the same two files (same asset and blob ids and sizes), and\ntheir metadata differ only in the publication date, the citation and the repository URL's trailing\nslash, so neither matches the paper better.\n\n**What the dandiset holds.** One recording session (2016-12-11) of monkey H (\"Haydn\"), from the\nNeural Latents Benchmark (NLB): a train file with the full trial table and the spikes of 54 units,\nand a test file with 283 further trials of the same session that carry no task variables and only\n40 of the units. The paper analyses 17 sessions of monkey H and 12 of monkey G. Monkey G is not in\nthe dandiset. All results here come from this one session, and a \"dataset\" is one effector and\ntarget direction (4 here; the paper's 8 are 2 animals x 4).\n\n**Code.** The paper's code is \"available from the corresponding author on request\" and was not\nread. The dandiset links the NLB, whose code\n([nlb_tools](https://github.com/neurallatents/nlb_tools) at commit 42f8410b) loads these files,\nbuilds tensors aligned to Go (1500 ms before Go), and scores models by a trial-by-trial correlation\nof neural speed with tp within each prior, effector and direction. It holds none of the paper's\nanalyses; its speed measure (mean step between successive states) matches the one chosen here.\n\n| Claim | Source | Tested here |\n|---|---|---|\n| beh-slopes: slopes of tp on ts between 0 and 1 | Fig. 1E | Tested |\n| beh-overlap-prior: opposite biases at ts = 800 ms | Fig. 1E | Tested |\n| beh-sigmoid-increments: smaller tp increments at the extremes | Fig. 2F | Tested |\n| beh-long-more-bias: smaller slopes for the Long prior | Fig. 2H | Tested |\n| beh-bayes-model: the Bayesian observer captures bias and variance | Fig. 2C, D | Tested |\n| glm-prior-ts: 65% prior-dependent and 27% ts-dependent units (H) | Fig. 3E | Tested |\n| dfr-overlap-support: prior difference at 800 ms peaks during the support | Fig. 3D | Tested |\n| pca-dimensionality: 3-4 PCs (estimation), 5-10 (production) | Fig. S3 | Tested |\n| encoding-r2: projections match the Bayesian estimate (R2 0.993, 0.996) | Fig. 4C | Tested |\n| encoding-bayes-beats-linear: Bayesian better than linear | Fig. 4D | Tested |\n| short-in-long-control: no sigmoid in the matched Long period | Fig. 4D | Tested |\n| neural-long-more-bias: smaller neural slope for Long | Fig. 4D | Tested |\n| speed-vs-projection: larger projection, slower speed | Fig. 4E | Tested |\n| initial-speed-biased: initial speed biased toward the mean | Fig. 4F | Tested |\n| speed-predicts-tp: speed predicts tp | Fig. 4G | Tested |\n| alt-speed-unmodulated: speed constant during the support | Fig. 5B | Tested |\n| alt-transient-parallel: parallel trajectories after Set | Fig. 5D | Tested |\n| alt-threshold-monotonic: distances fall steadily up to Go | Fig. 5F | Tested |\n| gpfa-variance-inverted-u: inverted-U variance of single-trial projections | Fig. 6C | Tested |\n| gpfa-mean-sigmoid: sigmoidal mean, higher Short slope | Fig. 6D | Tested |\n| rnn-curved-manifold, rnn-perturbation: recurrent network models | Fig. 7 | Blocked (no model in the dandiset; code on request) |\n| monkey-g: the results hold in monkey G | throughout | Blocked (monkey G not in the dandiset) |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport statsmodels.api as sm\nfrom scipy import stats\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score\n\nimport rsg\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\ndata = rsg.load()\nS, T = data[\"train\"], data[\"test\"]\ntrials, spikes = S[\"trials\"], S[\"spikes\"]\ngood = rsg.completed(trials)\nunits, unit_table = rsg.select_units(S, good)\nDS = [(e, th, rsg.dataset_name(e, th)) for e, th in rsg.DATASETS]\nprint(f\"loaded dandiset {rsg.DANDISET_ID} version {rsg.DANDISET_VERSION} in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nfor key, f in [(\"train\", S), (\"test\", T)]:\n    print(f\"{key}: {data['urls'][rsg.TRAIN if key == 'train' else rsg.TEST]}\")\n    for k, v in f[\"meta\"].items():\n        print(f\"   {k}: {v}\")\n    print(f\"   trials: {len(f['trials'])}; columns: {list(f['trials'].columns)}\")\n    print(f\"   units: {len(f['unit_ids'])}; held out: {int(f['heldout'].sum())}\")\nprint(\"\\nTest-file units that are in the train file:\", int(np.isin(T[\"unit_ids\"], S[\"unit_ids\"]).sum()), \"of\", len(T[\"unit_ids\"]),\n      \"; train units held out:\", int(S[\"heldout\"].sum()), \"; held-out train units in the test file:\",\n      int(np.isin(S[\"unit_ids\"][S[\"heldout\"]], T[\"unit_ids\"]).sum()))\nprint(\"\\nTrain trials by NLB split:\", trials.split.value_counts().to_dict())\nprint(\"Train trials with Set and Go:\", int((trials.set_time.notna() & trials.go_time.notna()).sum()),\n      \"; of these flagged is_outlier:\", int(trials[trials.set_time.notna() & trials.go_time.notna()].is_outlier.sum()),\n      \"; completed and not outliers (used here):\", len(good))\nprint(\"Used trials by split:\", good.split.value_counts().to_dict())\nprint(\"\\nUsed trials per condition (rows: effector, direction, prior; columns: ts in ms):\")\nprint(pd.crosstab([good.is_eye.map({True: 'Eye', False: 'Hand'}), good.theta.map({0.0: 'Right', 180.0: 'Left'}),\n                   good.is_short.map({True: 'Short', False: 'Long'})], good.ts).to_string())\nprint(\"\\nColumn descriptions (train trial table):\")\nfor c, d in S[\"descriptions\"].items():\n    print(f\"   {c}: {d}\")\n\"\"\", \"sanity\")\n\nmd(\"\"\"\nThe dandiset summary says one subject (Rhesus monkey) and 2 files, which the files confirm. The\ntest file holds 283 trials of the same session (`session_id` 20161211) with only `start_time`,\n`stop_time`, `go_time` and `split`, on its own clock (0 to 509 s), and only the 40 held-in units;\nits task variables and the 14 held-out units are withheld for the benchmark. These trials cannot\nenter any analysis that needs ts, the prior or the effector, so the analyses use the train file's\ntrials. Each condition has at least 14 used trials, so the Methods' rule of at least 5 trials per\ncondition does not remove any unit.\n\"\"\")\n\ncode(r\"\"\"\nc = trials[trials.set_time.notna() & trials.go_time.notna()].copy()\nd_ts = c.ts - (c.set_time - c.ready_time) * 1000\nd_tp = c.tp - (c.go_time - c.set_time) * 1000\nprint(\"ts minus (set_time - ready_time), ms: median %.1f, range %.1f to %.1f; within 5 ms: %.0f%%\"\n      % (d_ts.median(), d_ts.min(), d_ts.max(), 100 * (abs(d_ts) <= 5).mean()))\nfor flag, g in d_tp.groupby(c.is_outlier):\n    print(f\"tp minus (go_time - set_time), ms, is_outlier={flag}: median {g.median():.1f}, 5th to 95th percentile \"\n          f\"{g.quantile(.05):.1f} to {g.quantile(.95):.1f}, range {g.min():.1f} to {g.max():.1f}\")\nprint(\"Distinct ts by prior:\", {('Short' if k else 'Long'): sorted(v) for k, v in trials.groupby('is_short').ts.unique().items()})\nprint(\"iti by prior (ms):\", {('Short' if k else 'Long'): sorted(v) for k, v in trials.groupby('is_short').iti.unique().items()})\nprint(\"Paper: inter-trial intervals of 1220 ms (Short) and 500 ms (Long).\")\nprint(\"theta values:\", sorted(trials.theta.unique()), \"; is_eye values:\", sorted(trials.is_eye.unique()))\nprint(\"tp of used trials, ms: %.0f to %.0f; of uncompleted trials (no Go):\" % (good.tp.min(), good.tp.max()),\n      sorted(trials[trials.go_time.isna()].tp.round().unique())[:6], \"...\")\n\n# Refit of the Methods' mixture model, per prior, ts, effector and direction, on completed trials.\nflags = []\nfor key, g in c[c.tp > 0].groupby([\"is_short\", \"ts\", \"is_eye\", \"theta\"]):\n    r = rsg.outlier_mixture(g.tp.to_numpy(), key[1])\n    flags.append(pd.Series(r > 0.5, index=g.index))\nrefit = pd.concat(flags).reindex(c.index, fill_value=True)\nprint(\"\\nMixture-model refit against is_outlier (completed trials):\")\nprint(pd.crosstab(c.is_outlier.rename(\"is_outlier\"), refit.rename(\"refit lapse\")).to_string())\nprint(f\"Outlier fraction of completed trials: file {c.is_outlier.mean():.2%}, refit {refit.mean():.2%}; paper, monkey H: 3.84%\")\n\"\"\", \"sanity\")\n\nmd(\"\"\"\n`ts` is the nominal interval; the event times give intervals within 23.5 ms of it, consistent with\na 60 Hz display (one frame is 16.7 ms). `tp` is a median 18 ms longer than `go_time - set_time`\nfor used trials, so the two columns do not measure the same interval; the analyses use `tp` for\nbehaviour, as the trial table defines it, and the event times for aligning spikes. The `iti`\nvalues agree with the paper (1220 ms after Short trials, 500 ms after Long ones), and its column\ndescription (500 for Short, 1220 for Long) has them the other way round. The `is_outlier` flag is\nconsistent with the Methods' mixture model, as the refit agreement shows.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Units: rate over the observed intervals, spikes/s\")\nprint(unit_table.rate.describe().round(2).to_string())\nprint(f\"Kept by the Methods' rule (>= {rsg.MIN_RATE} spike/s and >= {rsg.MIN_TRIALS} trials per condition): \"\n      f\"{len(units)} of {len(unit_table)} (held-out units among the kept: {int(unit_table.heldout[unit_table.kept].sum())})\")\nprint(\"Paper: GPFA on 'simultaneously recorded neurons in a single session (N = 48 in H)'.\")\nobs = S[\"obs_intervals\"]\nsame = all(np.array_equal(o, obs[0]) for o in obs)\nprint(\"\\nAll units share the same observation intervals:\", same, \"; intervals:\", np.round(obs[0], 2).tolist())\ngaps = obs[0][1:, 0] - obs[0][:-1, 1]\ninside = [((obs[0][:, 0] <= a) & (obs[0][:, 1] >= b)).any() for a, b in zip(trials.start_time, trials.stop_time)]\nprint(f\"Gaps between intervals: {np.round(gaps, 3).tolist()} s; trials inside one interval: {sum(inside)} of {len(trials)}\")\nprint(\"Spike times sorted within every unit:\", all(np.all(np.diff(s) >= 0) for s in spikes),\n      \"; spikes outside the observation intervals:\",\n      int(sum((~((s[:, None] >= obs[0][:, 0]) & (s[:, None] <= obs[0][:, 1])).any(1)).sum() for s in spikes)))\n\n# Recordings deposited twice: does any test trial reappear in the train file? Compare the\n# inter-spike-interval sequence of each test trial with the whole train recording, for 3 units.\nhits, checked = 0, 0\nfor uid in T[\"unit_ids\"][:3]:\n    s_tr = np.round(np.diff(spikes[int(np.flatnonzero(S[\"unit_ids\"] == uid)[0])]), 4)\n    s_te = T[\"spikes\"][int(np.flatnonzero(T[\"unit_ids\"] == uid)[0])]\n    for a, b in zip(T[\"trials\"].start_time, T[\"trials\"].stop_time):\n        pat = np.round(np.diff(s_te[(s_te >= a) & (s_te < b)]), 4)\n        if len(pat) < 3:\n            continue\n        checked += 1\n        hits += any(np.array_equal(s_tr[i:i + len(pat)], pat) for i in np.flatnonzero(s_tr == pat[0]))\nprint(f\"\\nTest trials whose spike pattern recurs in the train file: {hits} of {checked} checked (3 units)\")\nseg = rsg.counts(spikes, units, good.ready_time.to_numpy(), 0, 400, 400)[:, 0, :]\ndup = pd.DataFrame(seg).duplicated().sum()\nprint(\"Train trials with identical spike counts in all kept units over Ready to Ready + 400 ms:\", int(dup))\n\"\"\", \"sanity\")\n\nmd(\"\"\"\nThe 48 units kept by the Methods' rate rule match the paper's count for the single session of\nmonkey H used for GPFA (Methods, N = 48), which is consistent with this being that session; the\ndandiset does not say so. All units share six observation intervals separated by gaps of 0.1 to\n0.14 s; every trial lies inside one interval. No test trial repeats a stretch of the train file,\nand no two train trials are identical, so no recording is deposited twice. The units carry no\nsingle-unit or multi-unit label, no electrode, and the electrode table has no positions or\nimpedances.\n\"\"\")\n\ncode(r\"\"\"\n# Do spikes share the clock of the trial table? Decode \"before\" against \"after\" an event from the\n# population counts in 200 ms windows, with the event time shifted by an offset. A response\n# locked to the event gives the best decoding at zero offset.\nrng_clock = np.random.default_rng(1)\noffsets = [-400, -200, -100, -50, 0, 50, 100, 200, 400]\nrows = []\nfor event in [\"ready_time\", \"set_time\", \"go_time\"]:\n    for off in offsets:\n        t0 = good[event].to_numpy() + off / 1000\n        pre = rsg.counts(spikes, units, t0, -200, 0, 200)[:, 0, :]\n        post = rsg.counts(spikes, units, t0, 0, 200, 200)[:, 0, :]\n        X = np.sqrt(np.vstack([pre, post]))\n        y = np.r_[np.zeros(len(pre)), np.ones(len(post))]\n        perm = rng_clock.permutation(len(y))\n        acc = cross_val_score(LogisticRegression(max_iter=2000), X[perm], y[perm], cv=5).mean()\n        rows.append({\"event\": event, \"offset_ms\": off, \"accuracy\": acc})\nclock = pd.DataFrame(rows).pivot(index=\"offset_ms\", columns=\"event\", values=\"accuracy\")\nprint(\"Cross-validated accuracy, before against after the event (chance 0.5):\")\nprint(clock.round(3).to_string())\nprint(\"Offset of best decoding:\", clock.idxmax().to_dict())\n\n# Contrast between conditions: decode the prior from the counts in the 400 ms before Ready, with\n# the trial labels as they are and shifted by one block of trials.\npre_ready = np.sqrt(rsg.counts(spikes, units, good.ready_time.to_numpy(), -400, 0, 400)[:, 0, :])\nfor shift in [0, 25, 50]:\n    y = np.roll(good.is_short.to_numpy(), shift)\n    perm = rng_clock.permutation(len(y))\n    acc = cross_val_score(LogisticRegression(max_iter=2000), pre_ready[perm], y[perm], cv=5).mean()\n    print(f\"Prior decoded before Ready, labels shifted by {shift} trials: accuracy {acc:.3f}\")\n\"\"\", \"sanity\")\n\nmd(\"\"\"\nDecoding of \"before against after\" peaks at or near zero offset for Ready, Set and Go, and the\nprior is decoded from activity before Ready only with the labels in place. This is consistent with\nthe spikes and the trial table sharing one clock in the train file. The test file could not be\nchecked this way, as it has no task variables; it is not used.\n\"\"\")\n\n# ---------------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Behaviour\n\n### beh-slopes\n\n> Regression slopes of tp on ts are positive and less than one in every condition, so the animals\n> estimated ts and their responses were biased toward the mean of the prior (Figure 1E).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor e, th, name in DS:\n    for short in [True, False]:\n        g = good[(good.is_eye == e) & (good.theta == th) & (good.is_short == short)]\n        b, se, ci = rsg.weighted_slope(g.ts, g.tp)\n        b_ols = np.polyfit(g.ts, g.tp, 1)[0]\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"trials\": len(g), \"slope\": b,\n                     \"ci_low\": ci[0], \"ci_high\": ci[1], \"slope_unweighted\": b_ols})\nslopes = pd.DataFrame(rows)\nprint(slopes.round(3).to_string(index=False))\ninside = ((slopes.slope > 0) & (slopes.slope < 1)).sum()\nstrict = ((slopes.ci_low > 0) & (slopes.ci_high < 1)).sum()\nprint(f\"\\nSlopes between 0 and 1: {inside} of 8; with the 95% interval excluding 0 and 1: {strict} of 8\")\nprint(\"Slope range: %.3f to %.3f\" % (slopes.slope.min(), slopes.slope.max()))\n\"\"\", \"claim:beh-slopes\")\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 4, figsize=(14, 3.4), sharey=True)\nfor ax, (e, th, name) in zip(axes, DS):\n    for short, col in [(True, \"tab:red\"), (False, \"tab:blue\")]:\n        g = good[(good.is_eye == e) & (good.theta == th) & (good.is_short == short)]\n        m = g.groupby(\"ts\").tp.agg([\"mean\", \"std\"])\n        ax.errorbar(m.index, m[\"mean\"], m[\"std\"], color=col, marker=\"o\", capsize=2)\n    ax.plot([450, 1250], [450, 1250], \"k:\", lw=1)\n    ax.set_title(name)\n    ax.set_xlabel(\"ts (ms)\")\naxes[0].set_ylabel(\"tp (ms), mean and SD\")\nplt.tight_layout()\nplt.show()\nprint(\"Mean tp per prior and ts: %.0f to %.0f ms; all points within the axes.\"\n      % (good.groupby(['is_eye', 'theta', 'is_short', 'ts']).tp.mean().min(), good.groupby(['is_eye', 'theta', 'is_short', 'ts']).tp.mean().max()))\n\"\"\", \"claim:beh-slopes\")\nresult(\"beh-slopes\")\n\nmd(r\"\"\"\n### beh-overlap-prior\n\n> At the overlapping ts of 800 ms, biases were in opposite directions for the two priors (rank-sum\n> test, p < 1e-43 in animal H over 17 sessions).\n\"\"\")\n\ncode(r\"\"\"\no = good[good.ts == 800]\ns_tp, l_tp = o[o.is_short].tp, o[~o.is_short].tp\np = stats.ranksums(s_tp, l_tp).pvalue\nprint(f\"ts = 800 ms: Short n = {len(s_tp)}, median tp - 800 = {s_tp.median() - 800:.1f} ms; \"\n      f\"Long n = {len(l_tp)}, median tp - 800 = {l_tp.median() - 800:.1f} ms; rank-sum p = {p:.2g}\")\nfor e, th, name in DS:\n    g = o[(o.is_eye == e) & (o.theta == th)]\n    a, b = g[g.is_short].tp, g[~g.is_short].tp\n    print(f\"   {name}: Short {a.median() - 800:+.1f} (n={len(a)}), Long {b.median() - 800:+.1f} (n={len(b)}), \"\n          f\"p = {stats.ranksums(a, b).pvalue:.2g}\")\n\"\"\", \"claim:beh-overlap-prior\")\nresult(\"beh-overlap-prior\")\n\nmd(r\"\"\"\n### beh-sigmoid-increments\n\n> Increments of tp between neighbouring ts are smaller at the extremes of the prior than near its\n> mean (signed-rank test, p < 1e-11 in animal H).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor e, th, name in DS:\n    for short in [True, False]:\n        g = good[(good.is_eye == e) & (good.theta == th) & (good.is_short == short)]\n        ext, mid = rsg.increments(g.groupby(\"ts\").tp.mean().loc[list(rsg.prior_ts(short))])\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"extreme\": ext, \"middle\": mid})\ninc = pd.DataFrame(rows)\ninc[\"middle_minus_extreme\"] = inc.middle - inc.extreme\nprint(inc.round(1).to_string(index=False))\nw = stats.wilcoxon(inc.middle, inc.extreme)\nprint(f\"\\nMiddle above extreme in {(inc.middle_minus_extreme > 0).sum()} of 8; median difference \"\n      f\"{inc.middle_minus_extreme.median():.1f} ms; two-sided signed-rank p = {w.pvalue:.4f}\")\n\"\"\", \"claim:beh-sigmoid-increments\")\nresult(\"beh-sigmoid-increments\")\n\nmd(r\"\"\"\n### beh-long-more-bias\n\n> Biases are larger for the Long prior than for the Short prior; regression slopes are smaller for\n> Long (Figure 2H).\n\"\"\")\n\ncode(r\"\"\"\nwide = slopes.pivot(index=\"dataset\", columns=\"prior\", values=\"slope\")\nwide[\"long_below_short\"] = wide.Long < wide.Short\nprint(wide.round(3).to_string())\nprint(f\"\\nLong slope below Short slope in {int(wide.long_below_short.sum())} of 4 datasets; \"\n      f\"mean Short {wide.Short.mean():.3f}, mean Long {wide.Long.mean():.3f}\")\nwu = slopes.pivot(index=\"dataset\", columns=\"prior\", values=\"slope_unweighted\")\nprint(f\"Unweighted slopes: Long below Short in {int((wu.Long < wu.Short).sum())} of 4\")\n\"\"\", \"claim:beh-long-more-bias\")\nresult(\"beh-long-more-bias\")\n\nmd(r\"\"\"\n### beh-bayes-model\n\n> A Bayesian observer model with scalar measurement and production noise fit to the behaviour\n> captures the bias and the variance of tp in all conditions (Figure 2C and 2D).\n\"\"\")\n\ncode(r\"\"\"\nmodels, rows, pred_rows = {}, [], []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    m = rsg.BayesObserver.fit(g)\n    models[name] = m\n    obs_bias, pred_bias, obs_sd, pred_sd = [], [], [], []\n    for short in [True, False]:\n        ts = np.array(rsg.prior_ts(short), float)\n        _, mean_tp, sd_tp = m.moments(ts, short)\n        gg = g[g.is_short == short].groupby(\"ts\").tp.agg([\"mean\", \"std\"]).loc[ts]\n        obs_bias += list(gg[\"mean\"] - ts)\n        pred_bias += list(mean_tp - ts)\n        obs_sd += list(gg[\"std\"])\n        pred_sd += list(sd_tp)\n        for t, ob, pb, os_, ps in zip(ts, gg[\"mean\"] - ts, mean_tp - ts, gg[\"std\"], sd_tp):\n            pred_rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"ts\": t,\n                              \"bias_obs\": ob, \"bias_model\": pb, \"sd_obs\": os_, \"sd_model\": ps})\n    ob, pb = np.array(obs_bias), np.array(pred_bias)\n    r2 = 1 - np.sum((ob - pb) ** 2) / np.sum((ob - ob.mean()) ** 2)\n    r_sd = stats.pearsonr(obs_sd, pred_sd)[0]\n    rows.append({\"dataset\": name, \"wm\": m.wm, \"wp\": m.wp, \"b_short\": m.b[True], \"b_long\": m.b[False],\n                 \"converged\": m.converged, \"bias_R2\": r2, \"sd_r\": r_sd})\nfits = pd.DataFrame(rows)\nprint(fits.round(3).to_string(index=False))\nprint(f\"\\nBias R2 >= 0.8 in {(fits.bias_R2 >= 0.8).sum()} of 4; SD correlation > 0 in {(fits.sd_r > 0).sum()} of 4\")\npred = pd.DataFrame(pred_rows)\nprint(\"\\nObserved and model bias and SD (ms):\")\nprint(pred.round(1).to_string(index=False))\n\"\"\", \"claim:beh-bayes-model\")\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 2, figsize=(8, 3.5))\nfor short, col in [(True, \"tab:red\"), (False, \"tab:blue\")]:\n    p_ = pred[pred.prior == (\"Short\" if short else \"Long\")]\n    axes[0].scatter(p_.bias_model, p_.bias_obs, color=col, s=15)\n    axes[1].scatter(p_.sd_model, p_.sd_obs, color=col, s=15)\nfor ax, lab in zip(axes, [\"bias (ms)\", \"SD of tp (ms)\"]):\n    lim = [min(ax.get_xlim()[0], ax.get_ylim()[0]), max(ax.get_xlim()[1], ax.get_ylim()[1])]\n    ax.plot(lim, lim, \"k:\", lw=1)\n    ax.set_xlabel(\"model \" + lab)\n    ax.set_ylabel(\"observed \" + lab)\nplt.tight_layout()\nplt.show()\nprint(\"Bias: observed %.0f to %.0f, model %.0f to %.0f ms; SD: observed %.0f to %.0f, model %.0f to %.0f ms; all within the axes.\"\n      % (pred.bias_obs.min(), pred.bias_obs.max(), pred.bias_model.min(), pred.bias_model.max(),\n         pred.sd_obs.min(), pred.sd_obs.max(), pred.sd_model.min(), pred.sd_model.max()))\n\"\"\", \"claim:beh-bayes-model\")\nresult(\"beh-bayes-model\")\n\n# ---------------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Single units\n\n### glm-prior-ts\n\n> About 30% of neurons were modulated by elapsed time (27% in monkey H) and more than 60% were\n> sensitive to the prior (65% in monkey H) (Figure 3E).\n\"\"\")\n\ncode(r\"\"\"\ndef glm_rows(trs, ts_values):\n    # One row per trial and time point t (ms after Ready) for which Set came after t (attrition).\n    elapsed = ((trs.set_time - trs.ready_time) * 1000).to_numpy()\n    cnt = np.stack([rsg.counts(spikes, units, trs.ready_time.to_numpy() + t / 1000, -rsg.GLM_WINDOW_MS, 0,\n                               rsg.GLM_WINDOW_MS)[:, 0, :] for t in ts_values], axis=1)\n    rows, ys = [], []\n    for i, (_, r) in enumerate(trs.iterrows()):\n        for k, t in enumerate(ts_values):\n            if elapsed[i] >= t - 1e-6:\n                rows.append({\"t\": k, \"prior\": float(not r.is_short), \"eff\": float(not r.is_eye), \"dir\": float(r.theta == 180)})\n                ys.append(cnt[i, k])\n    return pd.DataFrame(rows), np.array(ys)\n\n\ndef design(df, with_t=True, with_prior=True):\n    cols = [np.ones(len(df)), df.eff.to_numpy(), df[\"dir\"].to_numpy()]\n    if with_prior:\n        cols.append(df.prior.to_numpy())\n    if with_t:\n        cols += [(df.t == k).to_numpy().astype(float) for k in range(1, 5)]\n    return np.column_stack(cols)\n\n\ndef fit(y, X):\n    r = sm.GLM(y, X, family=sm.families.Poisson()).fit()\n    return r.llf, X.shape[1]\n\n\ndef bic(llf, k, n):\n    return -2 * llf + k * np.log(n)\n\n\nres = []\ndf_all, Y_all = glm_rows(good, rsg.SHORT_TS)\nper_prior = {short: glm_rows(good[good.is_short == short], rsg.prior_ts(short)) for short in [True, False]}\nfor j, u in enumerate(units):\n    y = Y_all[:, j]\n    l_full, k_full = fit(y, design(df_all))\n    l_red, k_red = fit(y, design(df_all, with_prior=False))\n    n = len(y)\n    row = {\"unit\": int(S[\"unit_ids\"][u]), \"prior_dBIC\": bic(l_red, k_red, n) - bic(l_full, k_full, n),\n           \"prior_LR_p\": stats.chi2.sf(2 * (l_full - l_red), k_full - k_red)}\n    for short, (dfp, Yp) in per_prior.items():\n        yp = Yp[:, j]\n        lf, kf = fit(yp, design(dfp, with_prior=False))\n        lr, kr = fit(yp, design(dfp, with_t=False, with_prior=False))\n        row[f\"ts_dBIC_{'short' if short else 'long'}\"] = bic(lr, kr, len(yp)) - bic(lf, kf, len(yp))\n        row[f\"ts_LR_p_{'short' if short else 'long'}\"] = stats.chi2.sf(2 * (lf - lr), kf - kr)\n    res.append(row)\nglm = pd.DataFrame(res)\nglm[\"prior_dep\"] = glm.prior_dBIC > 0\nglm[\"ts_dep\"] = (glm.ts_dBIC_short > 0) | (glm.ts_dBIC_long > 0)\n\n\ndef wilson(k, n):\n    lo, hi = sm.stats.proportion_confint(k, n, method=\"wilson\")\n    return f\"{100 * k / n:.1f}% ({k} of {n}; 95% interval {100 * lo:.1f} to {100 * hi:.1f}%)\"\n\n\nprint(\"Rows (trial x time point): all trials\", len(df_all), \"; Short\", len(per_prior[True][0]), \"; Long\", len(per_prior[False][0]))\nprint(\"Prior-dependent (BIC):\", wilson(int(glm.prior_dep.sum()), len(glm)), \"; paper, H: 65%\")\nprint(\"ts-dependent (BIC):   \", wilson(int(glm.ts_dep.sum()), len(glm)), \"; paper, H: 27%\")\nprint(\"Both:\", int((glm.prior_dep & glm.ts_dep).sum()), \"; prior only:\", int((glm.prior_dep & ~glm.ts_dep).sum()),\n      \"; ts only:\", int((~glm.prior_dep & glm.ts_dep).sum()), \"; neither:\", int((~glm.prior_dep & ~glm.ts_dep).sum()))\nprint(\"\\nVariants, likelihood-ratio test in place of BIC:\")\nfor a in [0.05, 0.01]:\n    pd_ = (glm.prior_LR_p < a).sum()\n    td_ = ((glm.ts_LR_p_short < a) | (glm.ts_LR_p_long < a)).sum()\n    print(f\"   p < {a}: prior {100 * pd_ / len(glm):.1f}%, ts {100 * td_ / len(glm):.1f}%\")\nprint(\"ts-dependent in Short only:\", int(((glm.ts_dBIC_short > 0) & ~(glm.ts_dBIC_long > 0)).sum()),\n      \"; Long only:\", int((~(glm.ts_dBIC_short > 0) & (glm.ts_dBIC_long > 0)).sum()),\n      \"; both:\", int(((glm.ts_dBIC_short > 0) & (glm.ts_dBIC_long > 0)).sum()))\n\"\"\", \"claim:glm-prior-ts\")\nresult(\"glm-prior-ts\")\n\nmd(r\"\"\"\n### dfr-overlap-support\n\n> At the overlapping ts of 800 ms, firing rates differ between priors, with the largest difference\n> during the support of the prior, between 480 and 800 ms after Ready (Figure 3D).\n\"\"\")\n\ncode(r\"\"\"\nrng_dfr = np.random.default_rng(3)\nedges = np.arange(-320, 1440 + 1, 160)\ncentres = (edges[:-1] + edges[1:]) / 2\n\n\ndef rms_dfr(cnt, short):\n    d = cnt[short].mean(0) - cnt[~short].mean(0)          # bins x units, counts per 160 ms\n    return np.sqrt(np.mean((d * 1000 / 160) ** 2, axis=1))  # spikes/s\n\n\nper_ds, nulls = {}, []\ncnts = {}\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th) & (good.ts == 800)]\n    cnts[name] = (rsg.counts(spikes, units, g.ready_time.to_numpy(), -320, 1440, 160), g.is_short.to_numpy())\n    per_ds[name] = rms_dfr(*cnts[name])\nmean_rms = np.mean(list(per_ds.values()), axis=0)\nfor _ in range(200):\n    nulls.append(np.mean([rms_dfr(cnt, rng_dfr.permutation(lab)) for cnt, lab in cnts.values()], axis=0))\nnulls = np.array(nulls)\ntab = pd.DataFrame({\"bin_start\": edges[:-1], \"bin_end\": edges[1:], **{k: v for k, v in per_ds.items()},\n                    \"mean\": mean_rms, \"shuffle_mean\": nulls.mean(0), \"shuffle_95\": np.percentile(nulls, 95, axis=0)})\nprint(\"RMS over units of the Short minus Long rate difference at ts = 800 ms (spikes/s), by 160 ms bin from Ready:\")\nprint(tab.round(2).to_string(index=False))\nk = int(np.argmax(mean_rms))\nthr = np.percentile(nulls.max(1), 95)\nprint(f\"\\nLargest mean RMS: {mean_rms[k]:.2f} spikes/s in the bin {edges[k]} to {edges[k + 1]} ms after Ready; \"\n      f\"95th percentile of the shuffled maximum: {thr:.2f}\")\nprint(\"Largest bin per dataset:\", {n: f\"{edges[np.argmax(v)]}-{edges[np.argmax(v) + 1]}\" for n, v in per_ds.items()})\nprint(\"Used trials at ts = 800 ms per dataset (Short, Long):\",\n      {n: (int(l.sum()), int((~l).sum())) for n, (c_, l) in cnts.items()})\n\"\"\", \"claim:dfr-overlap-support\")\n\ncode(r\"\"\"\nplt.figure(figsize=(6, 3.2))\nfor n, v in per_ds.items():\n    plt.plot(centres, v, color=\"0.6\", lw=1)\nplt.plot(centres, mean_rms, \"k\", lw=2, label=\"mean of datasets\")\nplt.fill_between(centres, np.percentile(nulls, 5, axis=0), np.percentile(nulls, 95, axis=0), color=\"tab:green\", alpha=.2, label=\"shuffle 5-95%\")\nplt.axvspan(480, 800, color=\"tab:red\", alpha=.1, label=\"Short support\")\nplt.axvline(0, color=\"k\", ls=\":\")\nplt.axvline(800, color=\"k\", ls=\"--\")\nplt.xlabel(\"time from Ready (ms); Set at 800\")\nplt.ylabel(\"RMS rate difference (spikes/s)\")\nplt.legend(fontsize=7)\nplt.show()\nprint(\"Plotted values: %.2f to %.2f spikes/s; all within the axes.\" % (min(v.min() for v in per_ds.values()), max(v.max() for v in per_ds.values())))\n\"\"\", \"claim:dfr-overlap-support\")\nresult(\"dfr-overlap-support\")\n\n# ---------------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Population trajectories\n\n### pca-dimensionality\n\n> Population activity is low dimensional; 3 to 4 principal components in the estimation epoch and\n> 5 to 10 in the production epoch explain about 75% of the variance (Figure S3).\n\nThe PCA fitted here is used by the claims that follow.\n\"\"\")\n\ncode(r\"\"\"\nEST, PROD, rows = {}, {}, []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    est = {}\n    for short in [True, False]:\n        gg = g[g.is_short == short]\n        rate, ends, n = rsg.estimation_rates(spikes, units, gg, max(rsg.prior_ts(short)))\n        est[short] = {\"rate\": rate, \"t\": ends, \"n\": n}\n    pca_e = rsg.PCA([est[True][\"rate\"], est[False][\"rate\"]])\n    prod = {}\n    for short in [True, False]:\n        for ts in rsg.prior_ts(short):\n            gg = g[(g.is_short == short) & (g.ts == ts)]\n            prod[(short, ts)] = {\"rate\": rsg.production_rates(spikes, units, gg), \"min_tp\": gg.tp.min(),\n                                 \"mean_tp\": gg.tp.mean(), \"n\": len(gg)}\n    pca_p = rsg.PCA([v[\"rate\"] for v in prod.values()])\n    EST[name] = {\"pca\": pca_e, **est}\n    PROD[name] = {\"pca\": pca_p, \"traj\": prod}\n    cum_e, cum_p = np.cumsum(pca_e.explained), np.cumsum(pca_p.explained)\n    rows.append({\"dataset\": name, \"est_PCs_75\": pca_e.n, \"prod_PCs_75\": pca_p.n,\n                 \"est_PCs_70\": int(np.searchsorted(cum_e, .7) + 1), \"est_PCs_80\": int(np.searchsorted(cum_e, .8) + 1),\n                 \"prod_PCs_70\": int(np.searchsorted(cum_p, .7) + 1), \"prod_PCs_80\": int(np.searchsorted(cum_p, .8) + 1),\n                 \"est_var_3PC\": cum_e[2], \"prod_var_5PC\": cum_p[4]})\ndims = pd.DataFrame(rows)\nprint(dims.round(3).to_string(index=False))\nn_ok = dims.est_PCs_75.between(3, 4).sum() + dims.prod_PCs_75.between(5, 11).sum()\nprint(f\"\\nIn range (estimation 3 or 4, production 5 to 11): {n_ok} of 8\")\nprint(\"Shortest tp per ts, used to cut production trajectories (ms):\",\n      {f\"{'S' if k[0] else 'L'}{k[1]}\": round(min(PROD[n]['traj'][k]['min_tp'] for n in PROD)) for k in PROD[DS[0][2]]['traj']})\n\"\"\", \"claim:pca-dimensionality\")\nresult(\"pca-dimensionality\")\n\nmd(r\"\"\"\n### encoding-r2\n\n> Projections of estimation-epoch neural states onto the encoding axis match the Bayesian estimates\n> from the model fitted to the behaviour (R2 = 0.993 for the Short prior, 0.996 for the Long prior,\n> monkey H, Hand Left; Figure 4C).\n\"\"\")\n\ncode(r\"\"\"\nrng_axes = np.random.default_rng(4)\nPROJ, rows = {}, []\nfor e, th, name in DS:\n    E = EST[name]\n    for short in [True, False]:\n        lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))\n        X = E[\"pca\"](E[short][\"rate\"])\n        t = E[short][\"t\"]\n        u = rsg.encoding_axis(X, t, lo, hi)\n        sel = (t >= lo - 1e-6) & (t <= hi + 1e-6)\n        xu, tt, w = X[sel] @ u, t[sel], E[short][\"n\"][sel]\n        te = models[name].moments(tt, short)[0]\n        _, _, r2_b, rmse_b = rsg.weighted_fit(te, xu, w)\n        _, slope_ts, r2_l, rmse_l = rsg.weighted_fit(tt, xu, w)\n        rand = []\n        for _ in range(1000):\n            v = rng_axes.standard_normal(X.shape[1])\n            rand.append(rsg.weighted_fit(te, X[sel] @ (v / np.linalg.norm(v)), w)[2])\n        rand = np.array(rand)\n        PROJ[(name, short)] = {\"t\": tt, \"xu\": xu, \"w\": w, \"te\": te, \"u\": u, \"X\": X, \"tall\": t}\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"points\": int(sel.sum()), \"PCs\": X.shape[1],\n                     \"R2_bayes\": r2_b, \"RMSE_bayes\": rmse_b, \"R2_linear\": r2_l, \"RMSE_linear\": rmse_l,\n                     \"slope_ts\": slope_ts, \"random_R2_median\": np.median(rand),\n                     \"random_R2_95\": np.percentile(rand, 95), \"frac_random_above\": np.mean(rand >= r2_b)})\nenc = pd.DataFrame(rows)\nprint(enc.round(4).to_string(index=False))\nhl = enc[enc.dataset == \"Hand Left\"].set_index(\"prior\").R2_bayes\nmean_r2 = enc.groupby(\"prior\").R2_bayes.mean()\nprint(f\"\\nReading (a), Hand Left: Short R2 = {hl['Short']:.4f}, Long R2 = {hl['Long']:.4f}\")\nprint(f\"Reading (b), mean of 4 datasets: Short R2 = {mean_r2['Short']:.4f}, Long R2 = {mean_r2['Long']:.4f}\")\nprint(\"Tolerance: R2 >= 0.894 (Short) and >= 0.896 (Long)\")\n\"\"\", \"claim:encoding-r2\")\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 4, figsize=(14, 3.2))\nfor ax, (e, th, name) in zip(axes, DS):\n    for short, col in [(True, \"tab:red\"), (False, \"tab:blue\")]:\n        p_ = PROJ[(name, short)]\n        a, b, _, _ = rsg.weighted_fit(p_[\"te\"], p_[\"xu\"], p_[\"w\"])\n        ax.plot(p_[\"t\"], (p_[\"xu\"] - a) / b, \"o\", color=col, ms=3)   # projections mapped onto te by the fit\n        ax.plot(p_[\"t\"], p_[\"te\"], \"-\", color=col)\n    ax.plot([450, 1250], [450, 1250], \"k:\", lw=1)\n    ax.set_title(name)\n    ax.set_xlabel(\"time from Ready = ts (ms)\")\naxes[0].set_ylabel(\"te (line) and mapped Xu (dots), ms\")\nplt.tight_layout()\nplt.show()\nvals = np.concatenate([(PROJ[k][\"xu\"] - rsg.weighted_fit(PROJ[k][\"te\"], PROJ[k][\"xu\"], PROJ[k][\"w\"])[0]) / rsg.weighted_fit(PROJ[k][\"te\"], PROJ[k][\"xu\"], PROJ[k][\"w\"])[1] for k in PROJ])\nprint(\"Mapped projections: %.0f to %.0f ms; all within the axes.\" % (vals.min(), vals.max()))\n\"\"\", \"claim:encoding-r2\")\nresult(\"encoding-r2\")\n\nmd(r\"\"\"\n### encoding-bayes-beats-linear\n\n> Neural projections are better explained by the Bayesian model than by a linear function of ts\n> with the same number of parameters, for both priors (signed-rank test on RMSE, p = 0.008 for each\n> prior; Figure 4D top).\n\"\"\")\n\ncode(r\"\"\"\nenc[\"dRMSE_bayes_minus_linear\"] = enc.RMSE_bayes - enc.RMSE_linear\nprint(enc[[\"dataset\", \"prior\", \"RMSE_bayes\", \"RMSE_linear\", \"dRMSE_bayes_minus_linear\"]].round(3).to_string(index=False))\nfor prior, g in enc.groupby(\"prior\", sort=False):\n    print(f\"{prior}: Bayesian lower in {(g.dRMSE_bayes_minus_linear < 0).sum()} of 4; \"\n          f\"signed-rank p = {stats.wilcoxon(g.RMSE_bayes, g.RMSE_linear).pvalue:.3f} (smallest possible with 4: 0.125)\")\n\"\"\", \"claim:encoding-bayes-beats-linear\")\nresult(\"encoding-bayes-beats-linear\")\n\nmd(r\"\"\"\n### short-in-long-control\n\n> In the Long prior during the period matched to the support of the Short prior (\"Short In Long\"),\n> the Bayesian model is not better than the linear one (signed-rank test, p = 0.74).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor e, th, name in DS:\n    p_ = PROJ[(name, False)]\n    X, t = p_[\"X\"], p_[\"tall\"]\n    u = rsg.encoding_axis(X, t, 480, 800)\n    sel = (t >= 480 - 1e-6) & (t <= 800 + 1e-6)\n    xu, tt = X[sel] @ u, t[sel]\n    w = EST[name][False][\"n\"][sel]\n    te = models[name].moments(tt, True)[0]\n    rows.append({\"dataset\": name, \"RMSE_bayes\": rsg.weighted_fit(te, xu, w)[3], \"RMSE_linear\": rsg.weighted_fit(tt, xu, w)[3],\n                 \"R2_bayes\": rsg.weighted_fit(te, xu, w)[2], \"R2_linear\": rsg.weighted_fit(tt, xu, w)[2]})\nsil = pd.DataFrame(rows)\nsil[\"dRMSE\"] = sil.RMSE_bayes - sil.RMSE_linear\nprint(sil.round(4).to_string(index=False))\np_sil = stats.wilcoxon(sil.RMSE_bayes, sil.RMSE_linear).pvalue\nprint(f\"\\nShort In Long: Bayesian lower in {(sil.dRMSE < 0).sum()} of 4; median dRMSE {sil.dRMSE.median():.3f}; \"\n      f\"signed-rank p = {p_sil:.3f} (smallest possible with 4 datasets: 0.125)\")\nsh = enc[enc.prior == \"Short\"]\nprint(f\"For comparison, Short prior: median dRMSE {sh.dRMSE_bayes_minus_linear.median():.3f}; \"\n      f\"relative dRMSE (dRMSE / RMSE_linear) Short In Long {np.median(sil.dRMSE / sil.RMSE_linear):.3f}, \"\n      f\"Short {np.median(sh.dRMSE_bayes_minus_linear / sh.RMSE_linear):.3f}\")\n\"\"\", \"claim:short-in-long-control\")\nresult(\"short-in-long-control\")\n\nmd(r\"\"\"\n### neural-long-more-bias\n\n> Neural projections show more bias for the Long prior than for the Short prior, as a smaller\n> regression slope of Xu on ts (signed-rank test, p = 0.008; Figure 4D bottom).\n\"\"\")\n\ncode(r\"\"\"\nsl = enc.pivot(index=\"dataset\", columns=\"prior\", values=\"slope_ts\")\nsl[\"long_below_short\"] = sl.Long < sl.Short\nprint(\"Slope of Xu on ts (spikes/s per ms, shared PC space of each dataset):\")\nprint(sl.round(4).to_string())\nprint(f\"\\nLong below Short in {int(sl.long_below_short.sum())} of 4 datasets; ratio Long / Short: \"\n      + \", \".join(f\"{r:.2f}\" for r in sl.Long / sl.Short))\n\"\"\", \"claim:neural-long-more-bias\")\nresult(\"neural-long-more-bias\")\n\nmd(r\"\"\"\n### speed-vs-projection\n\n> Larger projections on the encoding axis at Set are followed by slower neural trajectories in the\n> production epoch (Pearson correlation, rho Short = -0.74, rho Long = -0.51; Figure 4E).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor e, th, name in DS:\n    P = PROD[name]\n    for (short, ts), v in P[\"traj\"].items():\n        states = P[\"pca\"](v[\"rate\"])\n        p_ = PROJ[(name, short)]\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"ts\": ts,\n                     \"xu_at_set\": p_[\"xu\"][np.argmin(abs(p_[\"t\"] - ts))], \"speed\": rsg.step_speed(states),\n                     \"duration_ms\": len(states) * rsg.BIN_MS, \"mean_tp\": v[\"mean_tp\"], \"trials\": v[\"n\"]})\nspd = pd.DataFrame(rows)\nspd[\"speed_per_tp\"] = spd.speed / spd.mean_tp\nprint(spd.round(3).to_string(index=False))\nfor prior in [\"Short\", \"Long\"]:\n    g = spd[spd.prior == prior]\n    r, p = stats.pearsonr(g.xu_at_set, g.speed)\n    rb, pb = stats.pearsonr(g.xu_at_set, g.speed_per_tp)\n    z = g.groupby(\"dataset\").xu_at_set.transform(lambda x: (x - x.mean()) / x.std())\n    rz, pz = stats.pearsonr(z, g.speed)\n    within = [stats.pearsonr(h.xu_at_set, h.speed)[0] for _, h in g.groupby(\"dataset\")]\n    print(f\"{prior}: rho = {r:.3f} (p = {p:.2g}); variant speed / mean tp: rho = {rb:.3f} (p = {pb:.2g}); \"\n          f\"Xu z-scored per dataset: rho = {rz:.3f} (p = {pz:.2g}); within datasets: \" + \", \".join(f\"{x:.2f}\" for x in within))\n\"\"\", \"claim:speed-vs-projection\")\nresult(\"speed-vs-projection\")\n\nmd(r\"\"\"\n### initial-speed-biased\n\n> The initial speed of production trajectories (Set to Set + 400 ms) is biased toward the middle of\n> the prior; its dependence on ts is shallower than the unbiased profile proportional to 1/ts\n> (signed-rank test, p < 1e-3 over conditions and animals; Figure 4F).\n\"\"\")\n\ncode(r\"\"\"\nrows, dropped = [], 0\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    for short in [True, False]:\n        ts_v = np.array(rsg.prior_ts(short), float)\n        sp = []\n        for ts in ts_v:\n            gg = g[(g.is_short == short) & (g.ts == ts)]\n            dropped += int((gg.tp < 400).sum())\n            gg = gg[gg.tp >= 400]\n            sp.append(rsg.step_speed(PROD[name][\"pca\"](rsg.production_rates(spikes, units, gg, 400))))\n        sp = np.array(sp)\n        unbiased = sp[2] * ts_v[2] / ts_v\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", **{f\"speed_{int(t)}\": s for t, s in zip(ts_v, sp)},\n                     \"slope_measured\": np.polyfit(ts_v, sp, 1)[0], \"slope_unbiased\": np.polyfit(ts_v, unbiased, 1)[0]})\nini = pd.DataFrame(rows)\nini[\"measured_minus_unbiased\"] = ini.slope_measured - ini.slope_unbiased\nprint(ini.round(5).to_string(index=False))\nw = stats.wilcoxon(ini.slope_measured, ini.slope_unbiased)\nprint(f\"\\nMeasured shallower than unbiased in {(ini.measured_minus_unbiased > 0).sum()} of 8; \"\n      f\"two-sided signed-rank p = {w.pvalue:.4f}; trials dropped for tp < 400 ms: {dropped}\")\nprint(\"Measured slope negative in\", int((ini.slope_measured < 0).sum()), \"of 8\")\n\"\"\", \"claim:initial-speed-biased\")\nresult(\"initial-speed-biased\")\n\nmd(r\"\"\"\n### speed-predicts-tp\n\n> The speed of neural trajectories in the production epoch predicts the mean tp (Pearson\n> correlation, rho Short = -0.58, rho Long = -0.52; Figure 4G).\n\"\"\")\n\ncode(r\"\"\"\nfor prior in [\"Short\", \"Long\"]:\n    g = spd[spd.prior == prior]\n    r, p = stats.pearsonr(g.speed, g.mean_tp)\n    rb, pb = stats.pearsonr(g.speed_per_tp, g.mean_tp)\n    within = [stats.pearsonr(h.speed, h.mean_tp)[0] for _, h in g.groupby(\"dataset\")]\n    print(f\"{prior}: rho(speed, mean tp) = {r:.3f} (p = {p:.2g}), 20 points; variant speed / mean tp: {rb:.3f} (p = {pb:.2g}); \"\n          \"within datasets: \" + \", \".join(f\"{x:.2f}\" for x in within))\n\n# Variant: the Neural Latents Benchmark's measure, trial by trial within prior, effector and\n# direction; single-trial rates smoothed as above and projected on the production PCs, from Set\n# to the trial's own Go.\nrows = []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    for short in [True, False]:\n        gg = g[g.is_short == short]\n        c_ = rsg.counts(spikes, units, gg.set_time.to_numpy(), 0, 2400)\n        sp = []\n        for i, tp in enumerate(gg.tp.to_numpy()):\n            nb = int(tp // rsg.BIN_MS)\n            sp.append(rsg.step_speed(PROD[name][\"pca\"](rsg.smooth(c_[i, :nb] * 1000 / rsg.BIN_MS))))\n        r, p = stats.pearsonr(sp, gg.tp)\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"trials\": len(gg), \"r\": r, \"p\": p})\nnlb = pd.DataFrame(rows)\nprint(\"\\nTrial-by-trial speed against tp (NLB-style):\")\nprint(nlb.round(3).to_string(index=False))\nprint(f\"Mean r over the 8 conditions: {nlb.r.mean():.3f}\")\n\"\"\", \"claim:speed-predicts-tp\")\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 2, figsize=(9, 3.4))\nfor prior, col in [(\"Short\", \"tab:red\"), (\"Long\", \"tab:blue\")]:\n    g = spd[spd.prior == prior]\n    for n, h in g.groupby(\"dataset\"):\n        axes[0].plot(h.xu_at_set, h.speed, \"o-\", color=col, ms=3, lw=.7)\n        axes[1].plot(h.speed, h.mean_tp, \"o-\", color=col, ms=3, lw=.7)\naxes[0].set_xlabel(\"Xu at Set (spikes/s)\")\naxes[0].set_ylabel(\"speed (spikes/s per 20 ms)\")\naxes[1].set_xlabel(\"speed (spikes/s per 20 ms)\")\naxes[1].set_ylabel(\"mean tp (ms)\")\nplt.tight_layout()\nplt.show()\nprint(\"Xu %.1f to %.1f; speed %.2f to %.2f; mean tp %.0f to %.0f; all within the axes.\"\n      % (spd.xu_at_set.min(), spd.xu_at_set.max(), spd.speed.min(), spd.speed.max(), spd.mean_tp.min(), spd.mean_tp.max()))\n\"\"\", \"claim:speed-predicts-tp\")\nresult(\"speed-predicts-tp\")\n\n# ---------------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Alternative mechanisms\n\n### alt-speed-unmodulated\n\n> Instantaneous speed of neural trajectories in the full neural space is not modulated during the\n> support of each prior (signed-rank test for zero regression slopes, p = 0.64 for Short, p = 0.08\n> for Long; Figure 5B).\n\"\"\")\n\ncode(r\"\"\"\nrng_boot = np.random.default_rng(5)\n\n\ndef support_slope(rate, ends, short):\n    lo, hi = min(rsg.prior_ts(short)), max(rsg.prior_ts(short))\n    sp = np.linalg.norm(np.diff(rate, axis=0), axis=1)\n    t = ends[1:]\n    sel = (t > lo) & (t <= hi + 1e-6)\n    return np.polyfit(t[sel], sp[sel], 1)[0] * 100, sp[sel].mean()   # per 100 ms\n\n\nrows = []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    for short in [True, False]:\n        gg = g[g.is_short == short]\n        t_max = max(rsg.prior_ts(short))\n        c_ = rsg.counts(spikes, units, gg.ready_time.to_numpy(), 0, t_max)\n        el = ((gg.set_time - gg.ready_time) * 1000).to_numpy()\n        rate, ends, _ = rsg.attrition_rates(c_, el)\n        slope, mean_sp = support_slope(rate, ends, short)\n        boots = []\n        for _ in range(200):\n            i = rng_boot.integers(0, len(gg), len(gg))\n            r_, e_, _ = rsg.attrition_rates(c_[i], el[i])\n            boots.append(support_slope(r_, e_, short)[0])\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"mean_speed\": mean_sp, \"slope_per_100ms\": slope,\n                     \"slope_rel_pct\": 100 * slope / mean_sp, \"boot_low\": np.percentile(boots, 2.5), \"boot_high\": np.percentile(boots, 97.5)})\nasp = pd.DataFrame(rows)\nprint(\"Speed in the full space of\", len(units), \"units (spikes/s per 20 ms step); slope per 100 ms, with 95% bootstrap interval over trials:\")\nprint(asp.round(3).to_string(index=False))\nfor prior, g in asp.groupby(\"prior\", sort=False):\n    print(f\"{prior}: signed-rank p = {stats.wilcoxon(g.slope_per_100ms).pvalue:.3f} (smallest possible with 4: 0.125); \"\n          f\"slopes {', '.join(f'{x:+.3f}' for x in g.slope_per_100ms)}; intervals excluding 0: \"\n          f\"{int(((g.boot_low > 0) | (g.boot_high < 0)).sum())} of 4\")\n\"\"\", \"claim:alt-speed-unmodulated\")\nresult(\"alt-speed-unmodulated\")\n\nmd(r\"\"\"\n### alt-transient-parallel\n\n> In the first 200 ms after Set, trajectories for different ts run parallel; their distance to the\n> middle ts trajectory does not change (signed-rank test for zero slopes, p = 0.92 for the shortest\n> ts, p = 0.13 for the longest; Figure 5D).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    traj = {}\n    for short in [True, False]:\n        for ts in rsg.prior_ts(short):\n            gg = g[(g.is_short == short) & (g.ts == ts)]\n            traj[(short, ts)] = rsg.aligned_rates(spikes, units, gg.set_time.to_numpy(), -100, 300)[5:15]  # Set to Set + 200 ms\n    pca_t = rsg.PCA(list(traj.values()))\n    t = np.arange(1, 11) * rsg.BIN_MS\n    for short in [True, False]:\n        ts_v = rsg.prior_ts(short)\n        ref = pca_t(traj[(short, ts_v[2])])\n        for which, ts in [(\"shortest\", ts_v[0]), (\"longest\", ts_v[-1])]:\n            dist = np.linalg.norm(pca_t(traj[(short, ts)]) - ref, axis=1)\n            rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"ts\": which, \"PCs\": pca_t.n,\n                         \"mean_distance\": dist.mean(), \"slope_per_100ms\": np.polyfit(t, dist, 1)[0] * 100})\ntr_ = pd.DataFrame(rows)\ntr_[\"slope_rel_pct\"] = 100 * tr_.slope_per_100ms / tr_.mean_distance\nprint(tr_.round(3).to_string(index=False))\nfor which, g in tr_.groupby(\"ts\"):\n    w = stats.wilcoxon(g.slope_per_100ms)\n    print(f\"{which} ts: signed-rank p = {w.pvalue:.3f}; positive slopes {(g.slope_per_100ms > 0).sum()} of 8; \"\n          f\"median relative slope {g.slope_rel_pct.median():+.1f}% per 100 ms\")\n\"\"\", \"claim:alt-transient-parallel\")\nresult(\"alt-transient-parallel\")\n\nmd(r\"\"\"\n### alt-threshold-monotonic\n\n> Aligned to the response, distances between trajectories for different ts decrease steadily up to\n> movement initiation, without the converging then diverging pattern a ts-dependent threshold would\n> produce (Figure 5F).\n\"\"\")\n\ncode(r\"\"\"\ndef go_curves(kept):\n    rows, curves = [], {}\n    for e, th, name in DS:\n        g = good[(good.is_eye == e) & (good.theta == th)]\n        traj = {}\n        for short in [True, False]:\n            for ts in rsg.prior_ts(short):\n                gg = g[(g.is_short == short) & (g.ts == ts)]\n                traj[(short, ts)] = rsg.aligned_rates(spikes, units, gg.go_time.to_numpy(), -900, 100)[5:45]  # Go - 800 to Go\n        pca_g = rsg.PCA(list(traj.values()), kept) if kept else (lambda x: x)\n        t = np.arange(-39, 1) * rsg.BIN_MS   # bin end times relative to Go\n        for short in [True, False]:\n            ts_v = rsg.prior_ts(short)\n            ref = pca_g(traj[(short, ts_v[2])])\n            for ts in ts_v[:2] + ts_v[3:]:\n                dist = np.linalg.norm(pca_g(traj[(short, ts)]) - ref, axis=1)\n                curves[(name, short, ts)] = dist\n                rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", \"ts\": ts,\n                             \"PCs\": getattr(pca_g, \"n\", len(units)), \"t_min\": t[np.argmin(dist)],\n                             \"d_at_go_over_min\": dist[-1] / dist.min(), \"d_start\": dist[0], \"d_go\": dist[-1]})\n    return pd.DataFrame(rows), curves, t\n\n\nthr_tab, thr_curves, t_go = go_curves(0.60)\nprint(thr_tab.round(3).to_string(index=False))\nprint(f\"\\nMain (60% of variance): median time of the minimum {thr_tab.t_min.median():.0f} ms (bin end, relative to Go); \"\n      f\"minimum in the last 40 ms in {(thr_tab.t_min >= -20).sum()} of {len(thr_tab)} curves; in the last 200 ms in \"\n      f\"{(thr_tab.t_min >= -180).sum()}; distance at Go below that 800 ms earlier in {(thr_tab.d_go < thr_tab.d_start).sum()}\")\nfor kept, lab in [(0.75, \"75% of variance\"), (None, \"full space\")]:\n    v, _, _ = go_curves(kept)\n    print(f\"Variant, {lab}: median time of the minimum {v.t_min.median():.0f} ms; in the last 40 ms {(v.t_min >= -20).sum()} of {len(v)}\")\n\"\"\", \"claim:alt-threshold-monotonic\")\n\ncode(r\"\"\"\nfig, axes = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)\nfor (name, short, ts), d in thr_curves.items():\n    axes[0 if short else 1].plot(t_go, d, color=\"tab:red\" if short else \"tab:blue\", lw=.6, alpha=.6)\nfor ax, lab in zip(axes, [\"Short\", \"Long\"]):\n    ax.set_title(lab)\n    ax.set_xlabel(\"time from Go (ms)\")\naxes[0].set_ylabel(\"distance to middle ts (spikes/s)\")\nplt.tight_layout()\nplt.show()\nallv = np.concatenate(list(thr_curves.values()))\nprint(\"Distances %.1f to %.1f; all within the axes.\" % (allv.min(), allv.max()))\n\"\"\", \"claim:alt-threshold-monotonic\")\nresult(\"alt-threshold-monotonic\")\n\n# ---------------------------------------------------------------------------------------------\nmd(r\"\"\"\n## Single-trial trajectories (GPFA)\n\n### gpfa-variance-inverted-u\n\n> The variance across single trials of the GPFA neural state at Set projected on the encoding axis\n> has an inverted-U profile over ts, lower at the extremes of each prior (one-tailed signed-rank test\n> on quadratic coefficients, p = 0.0273, monkey H; Figure 6C).\n\"\"\")\n\ncode(r\"\"\"\nrng_gpfa = np.random.default_rng(6)\nt_gpfa = time.time()\nGP, rows = {}, []\nfor e, th, name in DS:\n    g = good[(good.is_eye == e) & (good.theta == th)]\n    sts = rsg.estimation_spiketrains(spikes, units, g)\n    model, dim, scores = rsg.fit_gpfa(sts, rng_gpfa)\n    lat = model.transform(sts)\n    GP[name] = {\"lat\": lat, \"trials\": g, \"dim\": dim}\n    print(f\"{name}: {len(g)} trials, latent dimensionality {dim} (cross-validated log-likelihood \"\n          + \", \".join(f\"{k}: {v:.0f}\" for k, v in scores.items()) + \")\")\n    for short in [True, False]:\n        mask = g.is_short.to_numpy() == short\n        L = [lat[i] for i in np.flatnonzero(mask)]\n        nb = max(x.shape[1] for x in L)\n        mean = np.array([np.mean([x[:, k] for x in L if x.shape[1] > k], axis=0) for k in range(nb)])\n        tt = np.arange(1, nb + 1) * rsg.BIN_MS\n        ts_v = rsg.prior_ts(short)\n        u = rsg.encoding_axis(mean, tt, min(ts_v), max(ts_v))\n        xu = np.array([x[:, -1] @ u for x in L])\n        ts_tr = g.ts.to_numpy()[mask]\n        z = (xu - xu.mean()) / xu.std()\n        var = np.array([z[ts_tr == t].var(ddof=1) for t in ts_v])\n        mxu = np.array([xu[ts_tr == t].mean() for t in ts_v])\n        rows.append({\"dataset\": name, \"prior\": \"Short\" if short else \"Long\", **{f\"var_{t}\": v for t, v in zip(ts_v, var)},\n                     \"quad_coef\": np.polyfit(np.array(ts_v, float), var, 2)[0],\n                     \"mean_xu\": mxu, \"slope_xu\": np.polyfit(np.array(ts_v, float), mxu, 1)[0]})\ngp = pd.DataFrame(rows)\nprint(f\"GPFA fits took {time.time() - t_gpfa:.0f} s\")\nprint(gp.drop(columns=[\"mean_xu\"]).round(5).to_string(index=False))\nw = stats.wilcoxon(gp.quad_coef, alternative=\"less\")\nprint(f\"\\nQuadratic coefficient negative in {(gp.quad_coef < 0).sum()} of 8; one-tailed signed-rank p = {w.pvalue:.4f}\")\next_mid = np.array([[v[[0, 4]].mean(), v[[1, 2, 3]].mean()] for v in gp[[c for c in gp.columns if c.startswith('var_')]].to_numpy()]) if False else None\n\"\"\", \"claim:gpfa-variance-inverted-u\")\n\ncode(r\"\"\"\nvar_cols = {True: [f\"var_{t}\" for t in rsg.SHORT_TS], False: [f\"var_{t}\" for t in rsg.LONG_TS]}\nfig, axes = plt.subplots(1, 2, figsize=(8, 3.2), sharey=True)\nallv = []\nfor ax, short in zip(axes, [True, False]):\n    for _, r in gp[gp.prior == (\"Short\" if short else \"Long\")].iterrows():\n        v = r[var_cols[short]].to_numpy(float)\n        allv += list(v)\n        ax.plot(rsg.prior_ts(short), v, \"o-\", color=\"tab:red\" if short else \"tab:blue\", lw=.8, ms=3)\n    ax.set_xlabel(\"ts (ms)\")\naxes[0].set_ylabel(\"variance of z-scored Xu\")\nplt.tight_layout()\nplt.show()\nprint(\"Variances %.2f to %.2f; all within the axes.\" % (min(allv), max(allv)))\n\"\"\", \"claim:gpfa-variance-inverted-u\")\nresult(\"gpfa-variance-inverted-u\")\n\nmd(r\"\"\"\n### gpfa-mean-sigmoid\n\n> The mean of the single-trial GPFA projections is sigmoidal (signed-rank test on increments,\n> p = 0.0078) and has a higher slope for the Short prior (one-tailed signed-rank, p = 0.0625;\n> Figure 6D).\n\"\"\")\n\ncode(r\"\"\"\ninc_g = pd.DataFrame([{\"dataset\": r.dataset, \"prior\": r.prior, **dict(zip([\"extreme\", \"middle\"], rsg.increments(r.mean_xu)))}\n                      for _, r in gp.iterrows()])\nprint(inc_g.round(4).to_string(index=False))\nw = stats.wilcoxon(inc_g.middle, inc_g.extreme)\nprint(f\"\\nMiddle increment above extreme in {(inc_g.middle > inc_g.extreme).sum()} of 8; two-sided signed-rank p = {w.pvalue:.4f}\")\nsg = gp.pivot(index=\"dataset\", columns=\"prior\", values=\"slope_xu\")\nprint(\"\\nSlope of mean Xu on ts (latent units per ms):\")\nprint(sg.round(5).to_string())\nprint(f\"Short slope above Long in {int((sg.Short > sg.Long).sum())} of 4; one-tailed signed-rank p = \"\n      f\"{stats.wilcoxon(sg.Short, sg.Long, alternative='greater').pvalue:.4f}\")\nprint(\"Mean Xu rises with ts (positive slope) in\", int((gp.slope_xu > 0).sum()), \"of 8\")\nprint(f\"\\nTotal run time {time.time() - started:.0f} s\")\n\"\"\", \"claim:gpfa-mean-sigmoid\")\nresult(\"gpfa-mean-sigmoid\")\n"
}
```

```
File created successfully at: /tmp/claude/nb_cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
p='nb_cells.py'; s=open(p).read()
s=s.replace('''ext_mid = np.array([[v[[0, 4]].mean(), v[[1, 2, 3]].mean()] for v in gp[[c for c in gp.columns if c.startswith('var_')]].to_numpy()]) if False else None
''','')
open(p,'w').write(s)
E
cd entries/000130-sohn-2019 && printf 'dandi\nelephant\nh5py\nmatplotlib\nneo\nnumpy\npandas\nquantities\nremfile\nscikit-learn\nscipy\nstatsmodels\n' > requirements.in && python /tmp/claude/build_nb.py && uv pip install -q --python $TMPDIR/ex/bin/python ipykernel nbconvert && echo ok
```

```
wrote entries/000130-sohn-2019/reproduce_sohn_2019.ipynb 58 cells
ok
```

**Agent calls Bash**

```bash
time $TMPDIR/ex/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/run1 reproduce_sohn_2019.ipynb 2>&1 | tail -30
```

```
[NbConvertApp] Making directory /tmp/claude-1001/run1
[NbConvertApp] Converting notebook reproduce_sohn_2019.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 9221868 bytes to /tmp/claude-1001/run1/reproduce_sohn_2019.ipynb

real	7m3.200s
user	21m32.023s
sys	0m6.978s
```

**Agent**

It ran in 7 minutes. Let me read the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > show.py <<'E'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'### cell {i} tags={c.metadata.get("tags")}')
    for o in c.outputs:
        if o.output_type=='stream':
            t=o.text
            if len(t)>6000: t=t[:3000]+'\n...[%d chars]...\n'%len(t)+t[-2500:]
            print(t)
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
        elif 'text/plain' in o.get('data',{}) and 'image/png' not in o.get('data',{}): print(o.data['text/plain'][:2000])
E
$TMPDIR/ex/bin/python show.py run1/reproduce_sohn_2019.ipynb | head -300
```

```
### cell 1 tags=None
loaded dandiset 000130 version 0.241017.1448 in 5 s

### cell 3 tags=['sanity']
train: https://dandiarchive.s3.amazonaws.com/blobs/73a/6f6/73a6f648-8e97-4c90-b323-a15844e4e3d4
   session_description: Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains continuous segments of the full session on 2016-12-11 that can be used for training models for the Neural Latents Benchmark.
   session_start_time: 2016-12-11T00:00:00-05:00
   session_id: 20161211
   subject_id: Haydn
   species: Macaca mulatta
   age: P4Y
   related_publications: ['http://dx.doi.org/10.1016/j.neuron.2019.06.012']
   electrode_location: ['DMFC']
   electrode_x_all_nan: True
   n_electrodes: 72
   trials: 1160; columns: ['start_time', 'stop_time', 'fix_on_time', 'fix_time', 'target_on_time', 'ready_time', 'set_time', 'go_time', 'target_acq_time', 'reward_time', 'bad_time', 'is_short', 'is_eye', 'theta', 'ts', 'tp', 'fix_time_dur', 'target_time_dur', 'iti', 'reward_dur', 'is_outlier', 'split']
   units: 54; held out: 14
test: https://dandiarchive.s3.amazonaws.com/blobs/eaf/1fa/eaf1fa97-ce58-477d-b79d-82425cea818f
   session_description: Data from monkey Haydn performing ready-set-go time interval reproduction task. This file contains segments of trials from the full session on 2016-12-11 that are to be used for evaluating models for the Neural Latents Benchmark.
   session_start_time: 2016-12-11T00:00:00-05:00
[... 286 more lines not kept]
```

**Agent**

Several outputs to note. The Bayesian fit has a bug: the offsets never left 0, because Nelder-Mead's first step for a zero start is tiny. I'll fix that. First the rest of the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python show.py run1/reproduce_sohn_2019.ipynb 2>/dev/null | sed -n 300,520p
```

```
Eye Left Short       6.199        6.726                    -0.526
  Eye Left  Long       1.396        2.131                    -0.735
Hand Right Short       1.003        0.805                     0.199
Hand Right  Long       0.426        0.556                    -0.129
 Hand Left Short       0.388        0.436                    -0.048
 Hand Left  Long       0.209        0.252                    -0.043
Short: Bayesian lower in 3 of 4; signed-rank p = 0.375 (smallest possible with 4: 0.125)
Long: Bayesian lower in 4 of 4; signed-rank p = 0.125 (smallest possible with 4: 0.125)

### cell 36 tags=['claim:short-in-long-control']
   dataset  RMSE_bayes  RMSE_linear  R2_bayes  R2_linear   dRMSE
 Eye Right      1.0988       1.2534    0.9935     0.9916 -0.1545
  Eye Left      1.4872       1.7048    0.9888     0.9853 -0.2176
Hand Right      1.0800       1.1897    0.8732     0.8461 -0.1097
 Hand Left      0.3013       0.2268    0.9947     0.9970  0.0745

Short In Long: Bayesian lower in 3 of 4; median dRMSE -0.132; signed-rank p = 0.250 (smallest possible with 4 datasets: 0.125)
For comparison, Short prior: median dRMSE -0.156; relative dRMSE (dRMSE / RMSE_linear) Short In Long -0.108, Short -0.079

### cell 38 tags=['claim:neural-long-more-bias']
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python - <<'E'
import nbformat
nb=nbformat.read('run1/reproduce_sohn_2019.ipynb',4)
for c in nb.cells[54:]:
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream':
            lines=[l for l in o.text.splitlines() if 'WARNING' not in l and 'warn' not in l and l.strip()]
            print('\n'.join(lines))
        elif o.output_type=='error': print('ERR',o.evalue)
E
```

```
<persisted-output>
Output too large (87.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6d0fc731-c1c8-445c-be9d-e20fb47e0ca0/tool-results/bw2o92yc4.txt

Preview (first 2KB):
/tmp/claude-1001/ex/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 1 last spike(s) of the input spiketrain







/tmp/claude-1001/ex/lib/python3.13/site-packages/elephant/conversion.py:1158: UserWarning: Binning discarded 4 last spike(s) of the input spiketrain







[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v -i "warn\|^\s*$" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6d0fc731-c1c8-445c-be9d-e20fb47e0ca0/tool-results/bw2o92yc4.txt | head -60
```

```
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Eye Right: 276 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -174260, 8: -173782)
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
Fitting GPFA model...
Initializing parameters using factor analysis...
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v -i "warn\|^\s*$\|Initializing\|Fitting GPFA" /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/6d0fc731-c1c8-445c-be9d-e20fb47e0ca0/tool-results/bw2o92yc4.txt | sed -n 5,80p
```

```
GPFA fits took 392 s
   dataset prior  var_480  var_560  var_640  var_720  var_800  quad_coef  slope_xu  var_900  var_1000  var_1100  var_1200
 Eye Right Short  0.76136  0.52216  0.64462  0.79323  0.26468   -0.00001   0.00225      NaN       NaN       NaN       NaN
 Eye Right  Long      NaN      NaN      NaN      NaN  0.98480   -0.00000   0.00141  0.73311   0.93194   0.35270   0.44420
  Eye Left Short  0.48507  0.23071  0.30337  0.37887  0.18899    0.00000   0.00270      NaN       NaN       NaN       NaN
  Eye Left  Long      NaN      NaN      NaN      NaN  0.55700   -0.00001   0.00155  0.91998   0.73910   0.47742   0.40530
Hand Right Short  0.84457  0.95108  1.04073  0.87846  0.61072   -0.00001   0.00055      NaN       NaN       NaN       NaN
Hand Right  Long      NaN      NaN      NaN      NaN  0.63505   -0.00002   0.00037  1.65513   1.37979   0.52164   0.27153
 Hand Left Short  0.90637  1.22513  0.68841  0.48210  0.70261    0.00000   0.00094      NaN       NaN       NaN       NaN
 Hand Left  Long      NaN      NaN      NaN      NaN  1.24085    0.00001   0.00045  1.43434   0.47332   0.70777   0.70577
Quadratic coefficient negative in 5 of 8; one-tailed signed-rank p = 0.1250
Variances 0.19 to 1.66; all within the axes.
   dataset prior  extreme  middle
 Eye Right Short   0.0689  0.2540
 Eye Right  Long  -0.0024  0.2363
  Eye Left Short   0.1258  0.2764
  Eye Left  Long   0.0570  0.2203
Hand Right Short   0.0247  0.0575
Hand Right  Long  -0.0145  0.0719
 Hand Left Short   0.0276  0.1063
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > ex6.py <<'E'
import pickle, numpy as np, pandas as pd
d=pickle.load(open('d.pkl','rb'))
tr,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
c=tr[tr.set_time.notna()&tr.go_time.notna()].copy()
f=c[c.is_outlier]
f=f.assign(ratio=f.tp/f.ts)
print(f[['ts','tp','ratio','is_short','is_eye','theta','split']].sort_values('ratio').to_string())
E
$TMPDIR/ex/bin/python ex6.py
```

```
ts        tp     ratio  is_short  is_eye  theta  split
128    480.0  -960.000 -2.000000      True   False  180.0   none
555   1100.0 -2200.000 -2.000000     False   False  180.0   none
1140   480.0  -960.000 -2.000000      True   False  180.0   none
729    900.0   126.700  0.140778     False   False    0.0  train
618    900.0   187.293  0.208103     False   False  180.0  train
85     640.0   235.260  0.367594      True   False  180.0  train
938    640.0   338.043  0.528192      True   False    0.0    val
21    1100.0   651.812  0.592556     False    True    0.0  train
485   1100.0   660.528  0.600480     False   False  180.0  train
88    1000.0   609.916  0.609916     False    True  180.0  train
340    900.0   557.539  0.619488     False   False    0.0    val
605    800.0   518.174  0.647717      True   False  180.0  train
417   1000.0   724.818  0.724818     False    True    0.0  train
857   1200.0   880.829  0.734024     False    True  180.0  train
262   1100.0   836.371  0.760337     False    True  180.0  train
176    800.0   615.484  0.769355     False    True    0.0  train
291    900.0   705.897  0.784330     False    True    0.0    val
278    800.0   632.999  0.791249     False    True    0.0    val
888   1000.0   799.324  0.799324     False   False    0.0    val
[... 28 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "old_string": "        res = optimize.minimize(nll, x0=[0.1, 0.08, 0.0, 0.0], method=\"Nelder-Mead\",\n                                options={\"xatol\": 1e-4, \"fatol\": 1e-3, \"maxiter\": 2000})\n        model = cls(*res.x)\n        model.converged, model.nll = bool(res.success), float(res.fun)\n        return model",
 "new_string": "        # Nelder-Mead from three starting points, with an explicit first simplex (steps of 0.03\n        # for wm and wp, 20 ms for the offsets); the best fit is kept.\n        best = None\n        for wm0 in (0.05, 0.1, 0.2):\n            x0 = np.array([wm0, 0.08, 0.0, 0.0])\n            simplex = np.vstack([x0, x0 + np.diag([0.03, 0.03, 20.0, 20.0])])\n            res = optimize.minimize(nll, x0=x0, method=\"Nelder-Mead\",\n                                    options={\"initial_simplex\": simplex, \"xatol\": 1e-3, \"fatol\": 1e-3,\n                                             \"maxiter\": 3000})\n            if best is None or res.fun < best.fun:\n                best = res\n        model = cls(*best.x)\n        model.converged, model.nll = bool(best.success), float(best.fun)\n        return model"
}
```

```
The file entries/000130-sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000130-sohn-2019/rsg.py",
 "old_string": "    import quantities as pq\n    from elephant.gpfa import GPFA\n    folds = rng.permutation(len(spiketrains)) % 3\n    scores = {}\n    for dim in GPFA_DIMS:\n        total = 0.0\n        for k in range(3):\n            train = [s for s, f in zip(spiketrains, folds) if f != k]\n            test = [s for s, f in zip(spiketrains, folds) if f == k]\n            m = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)\n            m.fit(train)\n            total += m.score(test)\n        scores[dim] = total\n    best = max(scores, key=scores.get)\n    model = GPFA(bin_size=BIN_MS * pq.ms, x_dim=best, em_max_iters=GPFA_EM_ITERS)\n    model.fit(spiketrains)\n    return model, best, scores",
 "new_string": "    import contextlib\n    import io\n    import logging\n    import warnings\n\n    import quantities as pq\n    from elephant.gpfa import GPFA\n\n    # elephant reports each spike it moves across a bin edge; keep the notebook readable.\n    logging.getLogger(\"elephant\").setLevel(logging.ERROR)\n    folds = rng.permutation(len(spiketrains)) % 3\n    scores = {}\n    with warnings.catch_warnings(), contextlib.redirect_stdout(io.StringIO()):\n        warnings.simplefilter(\"ignore\")\n        for dim in GPFA_DIMS:\n            total = 0.0\n            for k in range(3):\n                train = [s for s, f in zip(spiketrains, folds) if f != k]\n                test = [s for s, f in zip(spiketrains, folds) if f == k]\n                m = GPFA(bin_size=BIN_MS * pq.ms, x_dim=dim, em_max_iters=GPFA_EM_ITERS)\n                m.fit(train)\n                total += m.score(test)\n            scores[dim] = total\n        best = max(scores, key=scores.get)\n        model = GPFA(bin_size=BIN_MS * pq.ms, x_dim=best, em_max_iters=GPFA_EM_ITERS)\n        model.fit(spiketrains)\n    return model, best, scores\n\n\ndef gpfa_transform(model, spiketrains):\n    \"\"\"Orthonormalised latent trajectories (latents x bins) of each trial, quietly.\"\"\"\n    import logging\n    import warnings\n    logging.getLogger(\"elephant\").setLevel(logging.ERROR)\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        return model.transform(spiketrains)"
}
```

```
The file entries/000130-sohn-2019/rsg.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
p='nb_cells.py'; s=open(p).read()
s=s.replace("    lat = model.transform(sts)\n","    lat = rsg.gpfa_transform(model, sts)\n")
s=s.replace('print(gp.drop(columns=["mean_xu"]).round(5).to_string(index=False))','print(gp.drop(columns=["mean_xu"]).to_string(index=False, float_format=lambda x: f"{x:.3g}"))')
open(p,'w').write(s)
E
grep -n "gpfa_transform\|float_format" nb_cells.py; cd $TMPDIR && cat > ex7.py <<'E'
import sys; sys.path.insert(0,'entries/000130-sohn-2019')
import pickle, numpy as np, rsg, time
d=pickle.load(open('d.pkl','rb'))
tr,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
g=rsg.completed(tr); g=g[(g.is_eye)&(g.theta==0)]
t=time.time(); m=rsg.BayesObserver.fit(g); print(time.time()-t, m.wm,m.wp,m.b,m.converged,m.nll)
E
$TMPDIR/ex/bin/python ex7.py
```

```
1023:    lat = rsg.gpfa_transform(model, sts)
1045:print(gp.drop(columns=["mean_xu"]).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
4.262102365493774 0.01326723435627581 0.10622129125917584 {True: np.float64(6.411330385134027), False: np.float64(24.390739570140738)} True 1616.1528760894007
Shell cwd was reset to
```

**Agent**

The fit now moves the offsets (Eye Right: bShort 6 ms, bLong 24 ms, wm 0.013). Re-running the notebook.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && python /tmp/claude/build_nb.py && time $TMPDIR/ex/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output-dir $TMPDIR/run2 reproduce_sohn_2019.ipynb 2>&1 | tail -2; cd $TMPDIR; $TMPDIR/ex/bin/python show.py run2/reproduce_sohn_2019.ipynb 2>/dev/null > run2.txt; ls -la run2/; grep -n "ERROR" run2.txt
```

```
wrote entries/000130-sohn-2019/reproduce_sohn_2019.ipynb 58 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 9113541 bytes to /tmp/claude-1001/run2/reproduce_sohn_2019.ipynb

real	7m1.525s
user	21m14.479s
sys	0m6.871s
total 8908
drwxr-xr-x 2 runner runner    4096 Oct 14 16:31 .
drwx-----T 9 runner runner    4096 Oct 14 16:31 ..
-rw-r--r-- 1 runner runner 9113541 Oct 14 16:31 reproduce_sohn_2019.ipynb
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python -c "
import nbformat
nb=nbformat.read('run2/reproduce_sohn_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        n=sum(len(str(o)) for o in c.outputs); print(i,n) if n>50000 else None
"; sed -n '/claim:beh-bayes-model/,/claim:glm/p' run2.txt | head -30; sed -n '/claim:encoding-r2/,/claim:neural-long/p' run2.txt | head -50
```

```
13 77084
22 54068
27 75305
32 88571
45 78501
52 148489
54 7152980
55 64938
### cell 21 tags=['claim:beh-bayes-model']
   dataset    wm    wp  b_short  b_long  converged  bias_R2  sd_r
 Eye Right 0.013 0.106    6.411  24.391       True    0.122 0.909
  Eye Left 0.025 0.103   40.838   1.691       True    0.671 0.807
Hand Right 0.074 0.104   36.932  50.359       True    0.865 0.277
 Hand Left 0.117 0.090    7.749 -81.479       True    0.978 0.749

Bias R2 >= 0.8 in 2 of 4; SD correlation > 0 in 4 of 4

Observed and model bias and SD (ms):
   dataset prior     ts  bias_obs  bias_model  sd_obs  sd_model
 Eye Right Short  480.0      16.9        11.8    55.1      51.6
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python -c "
import nbformat
nb=nbformat.read('run2/reproduce_sohn_2019.ipynb',4)
c=nb.cells[54]
for o in c.outputs: print(o.output_type, o.get('name'), len(str(o)), str(o.get('text',''))[:300])
" | head; grep -rn "getLogger\|setLevel" $TMPDIR/ex/lib/python3.13/site-packages/elephant/utils.py | head
```

```
stream stderr 238 [2026-10-14 16:24:54,693] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.

stream stderr 238 [2026-10-14 16:24:54,694] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.

stream stderr 238 [2026-10-14 16:24:54,694] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.

stream stderr 238 [2026-10-14 16:24:54,695] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.

stream stderr 238 [2026-10-14 16:24:54,696] utils - WARNING: Correcting 1 rounding errors by shifting the affected spikes into the following bin. You can set tolerance=None to disable this behaviour.

Traceback (most recent call last):
  File "<string>", line 5, in <module>
    for o in c.outputs: print(o.output_type, o.get('name'), len(str(o)), str(o.get('text',''))[:300])
                        ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
BrokenPipeError: [Errno 32] Broken pipe
38:logger = logging.getLogger(__file__)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && python - <<'E'
p='rsg.py'; s=open(p).read()
old='''    # elephant reports each spike it moves across a bin edge; keep the notebook readable.
    logging.getLogger("elephant").setLevel(logging.ERROR)
'''
new='''    _quiet_elephant()
'''
s=s.replace(old,new)
s=s.replace('''    import logging
    import warnings
    logging.getLogger("elephant").setLevel(logging.ERROR)
    with warnings.catch_warnings():''','''    import warnings
    _quiet_elephant()
    with warnings.catch_warnings():''')
s=s.replace('''def fit_gpfa(spiketrains''','''def _quiet_elephant():
    """elephant logs each spike it moves across a bin edge; keep the notebook readable."""
    import logging

    import elephant.utils
    logging.getLogger(elephant.utils.__file__).setLevel(logging.ERROR)


def fit_gpfa(spiketrains''')
open(p,'w').write(s)
E
grep -n "logging\|_quiet" rsg.py; grep -A12 "GPFA fits took" $TMPDIR/run2.txt | head -14; grep -B2 -A12 "Middle increment above extreme in 8" $TMPDIR/run2.txt | tail -12
```

```
366:def _quiet_elephant():
368:    import logging
371:    logging.getLogger(elephant.utils.__file__).setLevel(logging.ERROR)
380:    import logging
386:    _quiet_elephant()
409:    _quiet_elephant()
GPFA fits took 384 s
   dataset prior  var_480  var_560  var_640  var_720  var_800  quad_coef  slope_xu  var_900  var_1000  var_1100  var_1200
 Eye Right Short    0.765    0.524    0.646    0.796    0.263   -6.2e-06   0.00224      NaN       NaN       NaN       NaN
 Eye Right  Long      NaN      NaN      NaN      NaN    0.989  -6.53e-07    0.0014    0.735     0.935     0.353     0.445
  Eye Left Short    0.483     0.23    0.304     0.38    0.188   1.39e-06   0.00271      NaN       NaN       NaN       NaN
  Eye Left  Long      NaN      NaN      NaN      NaN    0.555  -6.76e-06   0.00155    0.921     0.735     0.478     0.406
Hand Right Short    0.844    0.954     1.04    0.874    0.614   -1.1e-05  0.000555      NaN       NaN       NaN       NaN
Hand Right  Long      NaN      NaN      NaN      NaN    0.635  -2.22e-05  0.000377     1.65      1.38     0.521     0.272
 Hand Left Short     0.91     1.22    0.693    0.484    0.688   1.21e-06  0.000947      NaN       NaN       NaN       NaN
 Hand Left  Long      NaN      NaN      NaN      NaN     1.27   5.94e-06  0.000456     1.43     0.466     0.704     0.683

Quadratic coefficient negative in 5 of 8; one-tailed signed-rank p = 0.1250


[... 12 more lines not kept]
```

**Agent**

Results are in. Before writing conclusions, let me check whether monkey G's data or other sessions exist elsewhere on DANDI, for the blocked claim's notes.

**Agent calls Bash**

```bash
for q in Jazayeri "ready-set-go" "Sohn" "DMFC" "interval reproduction"; do echo "== $q"; curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=50&empty=false" | python -c "
import json,sys
for d in json.load(sys.stdin)['results']:
    v=d.get('most_recent_published_version') or d['draft_version']; print(d['identifier'], v['name'][:100])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
p='nb_cells.py'; s=open(p).read()
old='''description (500 for Short, 1220 for Long) has them the other way round. The `is_outlier` flag is
consistent with the Methods' mixture model, as the refit agreement shows.'''
new='''description (500 for Short, 1220 for Long) has them the other way round. The `is_outlier` flag
marks 46 completed trials (4.47%, against 3.84% for monkey H in the paper). A refit of the
Methods' mixture model as read here, per prior, ts, effector and direction, flags only 10 of them
and no other trial; the file flags trials whose tp is within 0.76 to 1.6 times ts, which the refit
keeps. How the flag was computed is not documented beyond "probabilistic mixture model". The
analyses use the file's flag, as the claims file fixes.'''
assert old in s; s=s.replace(old,new)
old='''Decoding of "before against after" peaks at or near zero offset for Ready, Set and Go, and the
prior is decoded from activity before Ready only with the labels in place. This is consistent with
the spikes and the trial table sharing one clock in the train file. The test file could not be
checked this way, as it has no task variables; it is not used.'''
new='''Decoding of "before against after" is best at an offset of +100 ms for Ready, Set and Go, and falls
for negative offsets (at -400 ms, 0.56, 0.68 and 0.73). A best offset of +100 ms is what a response
with a latency of about 100 ms after each event gives, since the "after" window then holds the
response. The prior is decoded from the 400 ms before Ready with accuracy 0.64 with the labels in
place, 0.56 and 0.52 with the labels shifted by 25 and 50 trials. This is consistent with the
spikes and the trial table sharing one clock in the train file; it does not prove it. The test
file could not be checked this way, as it has no task variables; it is not used.'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
E
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
p='nb_cells.py'; s=open(p).read()
old='''print(f"Outlier fraction of completed trials: file {c.is_outlier.mean():.2%}, refit {refit.mean():.2%}; paper, monkey H: 3.84%")'''
new=old+'''
only_file = c[c.is_outlier & ~refit]
print("tp / ts of trials flagged by the file but kept by the refit: %.2f to %.2f (%d trials); of trials flagged by both: %s"
      % ((only_file.tp / only_file.ts).min(), (only_file.tp / only_file.ts).max(), len(only_file),
         np.round(np.sort((c[c.is_outlier & refit].tp / c[c.is_outlier & refit].ts).to_numpy()), 2).tolist()))'''
assert old in s; s=s.replace(old,new)
s=s.replace('''and no other trial; the file flags trials whose tp is within 0.76 to 1.6 times ts, which the refit
keeps.''','''and no other trial; the 36 others have tp between the ratios to ts printed above, which the refit
keeps as part of the Gaussian component.''')
open(p,'w').write(s)
E
cd $TMPDIR && cat > ex8.py <<'E'
import sys; sys.path.insert(0,'entries/000130-sohn-2019')
import pickle, numpy as np, pandas as pd, rsg
d=pickle.load(open('d.pkl','rb'))
trials,spk,ho=d['sub-Haydn/sub-Haydn_desc-train_ecephys.nwb']
c = trials[trials.set_time.notna() & trials.go_time.notna()].copy()
flags = []
for key, g in c[c.tp > 0].groupby(["is_short", "ts", "is_eye", "theta"]):
    r = rsg.outlier_mixture(g.tp.to_numpy(), key[1])
    flags.append(pd.Series(r > 0.5, index=g.index))
refit = pd.concat(flags).reindex(c.index, fill_value=True)
only_file = c[c.is_outlier & ~refit]
print((only_file.tp / only_file.ts).min(), (only_file.tp / only_file.ts).max(), len(only_file))
print(np.sort((c[c.is_outlier & refit].tp / c[c.is_outlier & refit].ts).to_numpy()))
E
$TMPDIR/ex/bin/python ex8.py
```

```
0.5281921875 1.5985583333333333 36
[-2.         -2.         -2.          0.14077778  0.20810333  0.36759375
  0.59255636  0.61948778  2.207445    2.48604222]
Shell cwd was reset to
```

**Agent**

Now the conclusions and summary.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude/conclusions.py",
 "content": "RESULTS = {\n\"beh-slopes\": \"\"\"\n**Result: not reproduced.** Six of the 8 slopes lie between 0 and 1 (0.50 to 0.90), and 5 of 8 have\n95% intervals that exclude both 0 and 1. In the Short prior with the eye, the slopes are 1.11\n(Eye Right, interval 1.01 to 1.21) and 1.01 (Eye Left), so in these two conditions this session\nshows no regression toward the mean. All slopes are positive. The criterion needs all 8 between 0\nand 1. The paper's slopes pool 17 sessions of monkey H and 12 of G; this is one session.\n\"\"\",\n\"beh-overlap-prior\": \"\"\"\n**Result: not reproduced.** At ts = 800 ms the median bias is +28.3 ms in the Short prior and +47.6 ms\nin the Long prior, so both are positive and not of opposite sign; the rank-sum test gives p = 0.073\n(93 and 107 trials). The Long prior gives the longer tp in 3 of 4 datasets, and significantly so\nonly for Hand Right (+29.7 against +96.8 ms, p = 0.00099). In Eye Left the Short tp is the longer\n(+79.1 against +18.6 ms, p = 0.051).\n\"\"\",\n\"beh-sigmoid-increments\": \"\"\"\n**Result: reproduced.** The mean increment of tp between neighbouring ts is larger in the middle of\nthe prior than at its extremes in 7 of 8 conditions (median difference 31.3 ms), two-sided\nsigned-rank p = 0.0156. The exception is Hand Left, Short prior (-10.7 ms).\n\"\"\",\n\"beh-long-more-bias\": \"\"\"\n**Result: reproduced.** The Long prior slope is below the Short prior slope in all 4 datasets (mean\n0.716 against 0.898), weighted or unweighted.\n\"\"\",\n\"beh-bayes-model\": \"\"\"\n**Result: partially reproduced.** The observer model predicts the SD of tp with a positive correlation\nin all 4 datasets (r = 0.28 to 0.91), but its predicted bias reaches R2 >= 0.8 in only 2 of 4\n(R2 = 0.12, 0.67, 0.87 and 0.98). The two eye datasets, whose Short slopes exceed 1 (beh-slopes),\nget very low measurement noise (wm = 0.013 and 0.025) and are the poorly fit ones. Every fit\nconverged. Table S3 was not available, so the fitted parameters are not compared with the paper's.\n\"\"\",\n\"glm-prior-ts\": \"\"\"\n**Result: not reproduced.** By the GLM and BIC rule of the Methods, 75.0% of units are prior-dependent\n(36 of 48, 95% interval 61.2 to 85.1%; paper 65 +/- 6.5%) and 45.8% are ts-dependent (22 of 48,\ninterval 32.6 to 59.7%; paper 27 +/- 2.7%). Both fractions are above the paper's and outside\ntolerance; the interval of the prior fraction includes 65%, that of the ts fraction does not\ninclude 27%. With a likelihood-ratio test in place of BIC the fractions are higher still (prior\n77.1 to 87.5%, ts 66.7 to 77.1%). The paper's fractions pool 536 units over 17 sessions; these 48\ncome from one session.\n\"\"\",\n\"dfr-overlap-support\": \"\"\"\n**Result: reproduced.** At ts = 800 ms, the RMS over units of the Short minus Long rate difference,\naveraged over datasets, is largest in the bin 480 to 640 ms after Ready (6.86 spikes/s), within the\nsupport of the Short prior, and above the 95th percentile of the shuffled maximum (3.11). Before\nReady it is at the shuffle level (2.39 and 2.29 against 95th percentiles of 2.42 and 2.32). Per\ndataset the largest bin is 480-640 (2 datasets), 640-800 and 800-960 ms; the mean is also high just\nafter Set (6.07 in 800 to 960 ms).\n\"\"\",\n\"pca-dimensionality\": \"\"\"\n**Result: not reproduced.** Two components reach 75% of the variance in the estimation epoch in all 4\ndatasets (3 components explain 86 to 90%), and 2, 2, 5 and 4 in the production epoch, so 1 of the\n8 values falls in the paper's ranges. Activity here is lower dimensional than the paper reports.\nThis session has 48 units; the paper's PCA pools up to 536 units recorded over 17 sessions, which\ncan add dimensions.\n\"\"\",\n\"encoding-r2\": \"\"\"\n**Result: reproduced.** Under reading (a), Hand Left, R2 = 0.998 (Short) and 0.996 (Long); under\nreading (b), the mean of the 4 datasets, 0.959 and 0.989. Both readings are within tolerance. The\nestimation trajectories here have only 2 PCs, and projections on random unit vectors in that space\nalso fit te well (median R2 0.73 to 0.98 by dataset and prior). The R2 on u exceeds that of 95% of\nrandom axes in 3 of 8 dataset-priors (Hand Right Long, both Hand Left priors), so in this session the\nfit is specific to u only for those three.\n\"\"\",\n\"encoding-bayes-beats-linear\": \"\"\"\n**Result: partially reproduced.** The Bayesian model has the lower RMSE in all 4 datasets for the\nLong prior and in 3 of 4 for the Short prior (Hand Right Short is the exception, 0.99 against 0.80).\nThe differences are small, 0.04 to 0.57 in units of Xu (spikes/s).\n\"\"\",\n\"short-in-long-control\": \"\"\"\n**Result: reproduced by the paper's test, which cannot detect an effect here.** The signed-rank test\nover the 4 datasets gives p = 0.25; with 4 datasets the smallest attainable p is 0.125, so it could\nnot have found an effect. The effect sizes do not show the contrast the paper describes: in the\ncontrol period the Bayesian model is better in 3 of 4 datasets, with a median relative RMSE\ndifference of -0.089, at least as large as in the Short prior itself (-0.060).\n\"\"\",\n\"neural-long-more-bias\": \"\"\"\n**Result: reproduced.** The slope of Xu on ts is smaller for the Long prior in all 4 datasets (ratios\nLong / Short 0.55, 0.63, 0.34 and 0.97); the Hand Right difference is small.\n\"\"\",\n\"speed-vs-projection\": \"\"\"\n**Result: partially reproduced.** Larger projections at Set are followed by slower production\ntrajectories in both priors, more strongly than the paper reports: rho = -0.941 (Short, p = 6.2e-10)\nand -0.878 (Long, p = 3.7e-07), outside the tolerances around -0.74 and -0.51. Within each dataset\nthe correlations are -0.75 to -1.00, and with Xu z-scored per dataset they are -0.759 and -0.779.\n\"\"\",\n\"initial-speed-biased\": \"\"\"\n**Result: reproduced.** The initial speed falls with ts in all 8 dataset-priors, and its slope is\nshallower than the unbiased 1/ts profile in 7 of 8 (two-sided signed-rank p = 0.039). Eye Right,\nLong is the exception. No trial was dropped for tp < 400 ms.\n\"\"\",\n\"speed-predicts-tp\": \"\"\"\n**Result: partially reproduced.** Faster production trajectories go with shorter mean tp in both\npriors: rho = -0.733 (Short, p = 0.00024) and -0.744 (Long, p = 0.00017) over 20 points, stronger\nthan the paper's -0.58 and -0.52 and outside tolerance. Within datasets the correlations are -0.80\nto -0.99. The benchmark's trial-by-trial variant gives r = -0.195 to -0.740 (mean -0.519), with 7 of\n8 conditions at p < 0.05.\n\"\"\",\n\"alt-speed-unmodulated\": \"\"\"\n**Result: reproduced by the paper's test, which cannot detect an effect here; the data show the\nspeed is modulated.** The signed-rank test over 4 datasets gives p = 0.125 for each prior, the\nsmallest value it can give. All 8 slopes are positive, speed rising by 13 to 24% of its mean per 100\nms during the support, and all 8 bootstrap intervals exclude zero. So in this session the speed in\nthe full neural space increases during the support of each prior; the claim of no modulation holds\nonly in the sense that the paper's test, at this sample size, cannot reject it. The paper's test\nover 8 datasets gave p = 0.08 for Long.\n\"\"\",\n\"alt-transient-parallel\": \"\"\"\n**Result: not reproduced.** For the longest ts, the distance to the middle trajectory changes in the\nfirst 200 ms after Set: 6 of 8 slopes are negative (median -15.3% of the mean distance per 100 ms),\nsigned-rank p = 0.039. For the shortest ts p = 0.078 (6 of 8 positive, median +26.7% per 100 ms).\nThe PCA kept 1 to 4 components, and in Eye Left a single component, where the distance is the\nabsolute difference along one axis.\n\"\"\",\n\"alt-threshold-monotonic\": \"\"\"\n**Result: not reproduced.** With the components that reach 60% of the variance (1 to 3 per dataset),\nthe median time of the minimum distance is 210 ms before Go; the minimum is in the last 40 ms in 6\nof 32 curves and in the last 200 ms in 14. The distance at Go is below that 800 ms earlier in 26 of\n32 curves, so distances do fall overall. The result depends on the number of components: with 75%\nof the variance the median minimum is 80 ms before Go, and in the full space of 48 units 40 ms\nbefore Go, which would meet the criterion. With 1 component (Eye datasets) the distance can reach\nzero where trajectories cross, which moves the minima.\n\"\"\",\n\"gpfa-variance-inverted-u\": \"\"\"\n**Result: not reproduced.** The quadratic coefficient of variance on ts is negative in 5 of 8\ndataset-priors; the one-tailed signed-rank test gives p = 0.125 (paper 0.0273). Cross-validation\nchose 8 latent dimensions in all 4 datasets, the larger of the two candidates.\n\"\"\",\n\"gpfa-mean-sigmoid\": \"\"\"\n**Result: reproduced.** The mean single-trial projection rises with ts in all 8 dataset-priors, its\nmiddle increments exceed those at the extremes in 8 of 8 (two-sided signed-rank p = 0.0078, the\npaper's value), and its slope is higher for the Short prior in 4 of 4 datasets (one-tailed p =\n0.0625, the paper's value).\n\"\"\",\n}\n\nSUMMARY = r\"\"\"\n## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n| Claim | Outcome |\n|---|---|\n| beh-slopes | Not reproduced (6 of 8 slopes between 0 and 1) |\n| beh-overlap-prior | Not reproduced (both biases positive, p = 0.073) |\n| beh-sigmoid-increments | Reproduced (7 of 8, p = 0.0156) |\n| beh-long-more-bias | Reproduced (4 of 4) |\n| beh-bayes-model | Partially reproduced (SD in 4 of 4, bias R2 >= 0.8 in 2 of 4) |\n| glm-prior-ts | Not reproduced (75.0% and 45.8% against 65% and 27%) |\n| dfr-overlap-support | Reproduced (largest at 480 to 640 ms) |\n| pca-dimensionality | Not reproduced (2 PCs in the estimation epoch) |\n| encoding-r2 | Reproduced (0.998 and 0.996, Hand Left), not specific to u in 5 of 8 |\n| encoding-bayes-beats-linear | Partially reproduced (Long 4 of 4, Short 3 of 4) |\n| short-in-long-control | Reproduced by the paper's test, which cannot detect an effect with 4 datasets |\n| neural-long-more-bias | Reproduced (4 of 4) |\n| speed-vs-projection | Partially reproduced (rho -0.94 and -0.88, stronger than reported) |\n| initial-speed-biased | Reproduced (7 of 8, p = 0.039) |\n| speed-predicts-tp | Partially reproduced (rho -0.73 and -0.74, stronger than reported) |\n| alt-speed-unmodulated | Reproduced by the paper's test, which cannot detect an effect; all 8 slopes positive |\n| alt-transient-parallel | Not reproduced (longest ts, p = 0.039) |\n| alt-threshold-monotonic | Not reproduced (median minimum 210 ms before Go with 60% of variance) |\n| gpfa-variance-inverted-u | Not reproduced (5 of 8, p = 0.125) |\n| gpfa-mean-sigmoid | Reproduced (p = 0.0078 and 0.0625, the paper's values) |\n| rnn-curved-manifold, rnn-perturbation | Blocked: model results, no data in the dandiset |\n| monkey-g | Blocked: data missing |\n\n**How the analysis differs from the paper's.** All results come from one session of monkey H, one of\nthe 29 sessions of the paper, with 48 units where the paper pools 536 (H) and 636 (G) units over\nsessions; a \"dataset\" here is one effector and direction in this session (4, against the paper's\n8). The paper's code was not available, so smoothing, the encoding axis, speed, the GLM design with\nattrition and the Bayesian observer fit follow the Methods as read and the choices stated in the\nclaims file. The paper's signed-rank tests over 8 datasets become tests over 4, which cannot reach\np < 0.05; two claims of absence are judged on such tests. The GPFA latent dimensionality was chosen\nfrom 4 and 8 only, with 100 EM iterations. The outlier flag is the file's.\n\n**What was found about the dandiset.** It holds one session of one of the paper's two monkeys, in the\nform prepared for the Neural Latents Benchmark: 283 of the session's trials are in a test file\nwithout task variables and without 14 of the 54 units. The 48 units that pass the Methods' rate rule\nmatch the paper's single-session GPFA count for monkey H, consistent with this being that session.\nThe `iti` description gives the priors' inter-trial intervals the wrong way round, `tp` is a median\n18 ms longer than `go_time - set_time`, the `is_outlier` flag is not reproduced by a refit of the\nMethods' mixture model (10 of 46 flagged), and units have no single-unit or multi-unit label and no\nelectrode, whose table has no positions.\n\"\"\"\n"
}
```

```
File created successfully at: /tmp/claude/conclusions.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
p='conclusions.py'; s=open(p).read()
old='''(93 and 107 trials). The Long prior gives the longer tp in 3 of 4 datasets, and significantly so
only for Hand Right (+29.7 against +96.8 ms, p = 0.00099). In Eye Left the Short tp is the longer
(+79.1 against +18.6 ms, p = 0.051).'''
new='''(93 and 107 trials). The Long prior gives the longer tp in 2 of 4 datasets, Hand Right (+29.7
against +96.8 ms, p = 0.00099) and Hand Left (-61.6 against -2.8 ms, p = 0.069), where the Short
bias is negative. In the eye datasets the Short tp is the longer (Eye Left +79.1 against +18.6 ms,
p = 0.051).'''
assert old in s; s=s.replace(old,new)
s=s.replace("The differences are small, 0.04 to 0.57 in units of Xu (spikes/s).","The differences are small, 0.045 to 0.573 in units of Xu (spikes/s).")
open(p,'w').write(s)
E
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now entry.yaml and README, then lock and run.

**Agent calls Bash**

```bash
cd entries/000130-sohn-2019 && cat > entry.yaml <<'E'
schema_version: 1
name: 000130-sohn-2019
type: reproduction
title: Bayesian computation through cortical latent dynamics (Sohn et al. 2019)
description: Tests the findings of Sohn, Narain, Meirhaeghe and Jazayeri (2019) on dandiset 000130,
  the Neural Latents Benchmark's DMFC_RSG set, which holds one session of monkey H performing the
  Ready-Set-Go task with 54 units from dorsomedial frontal cortex. It tests the behaviour and the
  Bayesian observer model, single-unit sensitivity to the prior and elapsed time, the geometry and
  speed of population trajectories, the alternative mechanisms, and single-trial GPFA trajectories.
  Monkey G and the recurrent network models are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_sohn_2019.ipynb
  title: Reproducing Sohn et al. (2019) from dandiset 000130
  runtime_minutes: 8
helpers:
- rsg.py
related:
- id: dandi:000130/0.241017.1448
  relation: uses_data
- id: doi:10.1016/j.neuron.2019.06.012
  relation: reproduces
E
cat > README.md <<'E'
# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130

Tests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can
be tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), the Neural
Latents Benchmark's DMFC_RSG set. It holds one recording session of monkey H in the Ready-Set-Go
task, with 54 units from dorsomedial frontal cortex. The paper uses 17 sessions of monkey H and 12
of monkey G; monkey G and the recurrent network models are not in the dandiset.

| Claim | Outcome |
|---|---|
| Slopes of tp on ts between 0 and 1 in every condition | Not reproduced |
| Opposite biases of the two priors at ts = 800 ms | Not reproduced |
| Smaller tp increments at the extremes of the prior | Reproduced |
| Smaller slopes for the Long prior | Reproduced |
| The Bayesian observer captures bias and variance | Partially reproduced |
| 65% of units prior-dependent and 27% ts-dependent | Not reproduced |
| Prior difference at 800 ms largest during the support | Reproduced |
| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |
| Projections on the encoding axis match the Bayesian estimate | Reproduced |
| Bayesian model better than linear for the projections | Partially reproduced |
| No sigmoid in the Long prior's matched period | Reproduced (the test cannot detect an effect with 4 datasets) |
| Smaller neural slope for the Long prior | Reproduced |
| Larger projection at Set, slower trajectory | Partially reproduced |
| Initial speed biased toward the mean | Reproduced |
| Speed predicts tp | Partially reproduced |
| Speed unmodulated during the support | Reproduced (the test cannot detect an effect; the speed rises in all 8) |
| Parallel trajectories after Set | Not reproduced |
| Distances fall steadily up to Go | Not reproduced |
| Inverted-U variance of single-trial projections | Not reproduced |
| Sigmoidal mean of single-trial projections | Reproduced |
| Recurrent network models (two claims) | Blocked |
| The results hold in monkey G | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000130-sohn-2019-01.yaml`](../../attempts/000130-sohn-2019-01.yaml).

- `reproduce_sohn_2019.ipynb`: the analysis. It takes about eight minutes, most of it fitting GPFA.
- `rsg.py`: loading the files, unit selection, population rates with attrition, PCA, the encoding
  axis, the Bayesian observer and the GPFA fits. Other notebooks on this dandiset can import it.
E
cd  && python /tmp/claude/build_nb.py && python tools/entry.py lock entries/000130-sohn-2019 && python tools/entry.py check entries/000130-sohn-2019
```

```
wrote entries/000130-sohn-2019/reproduce_sohn_2019.ipynb 79 cells
wrote entries/000130-sohn-2019/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. Running the entry from a clean environment.

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000130-sohn-2019 2>&1 | tail -15
```

```
Installed kernelspec registry-000130-sohn-2019 in executed/000130-sohn-2019/.venv/share/jupyter/kernels/registry-000130-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (399 s)

real	6m42.236s
user	20m32.939s
sys	0m3.001s
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python show.py executed/000130-sohn-2019/reproduce_sohn_2019.ipynb > final.txt 2>/dev/null; wc -c final.txt; ls -la executed/000130-sohn-2019/; diff <(grep -v "loaded dandiset\|took\|run time" run2.txt) <(grep -v "loaded dandiset\|took\|run time" final.txt) | head -80
```

```
34814 final.txt
total 724
drwxr-xr-x 3 runner runner   4096 Oct 14 16:40 .
drwxr-xr-x 3 runner runner   4096 Oct 14 16:34 ..
drwxr-xr-x 5 runner runner   4096 Oct 14 16:34 .venv
-rw-r--r-- 1 runner runner 723171 Oct 14 16:40 reproduce_sohn_2019.ipynb
-rw-r--r-- 1 runner runner    173 Oct 14 16:40 result.json
89a90
> tp / ts of trials flagged by the file but kept by the refit: 0.53 to 1.60 (36 trials); of trials flagged by both: [-2.0, -2.0, -2.0, 0.14, 0.21, 0.37, 0.59, 0.62, 2.21, 2.49]
148c149
< ### cell 15 tags=['claim:beh-overlap-prior']
---
> ### cell 16 tags=['claim:beh-overlap-prior']
155c156
< ### cell 17 tags=['claim:beh-sigmoid-increments']
---
> ### cell 19 tags=['claim:beh-sigmoid-increments']
168c169
< ### cell 19 tags=['claim:beh-long-more-bias']
---
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; diff <(grep -v "loaded dandiset\|took\|run time\|^### cell\|^$" run2.txt) <(grep -v "loaded dandiset\|took\|run time\|^### cell\|^$" final.txt) | grep -v "WARNING\|warn" | head -60; grep -A30 "latent dimensionality" final.txt | head -45
```

```
78a79
> tp / ts of trials flagged by the file but kept by the refit: 0.53 to 1.60 (36 trials); of trials flagged by both: [-2.0, -2.0, -2.0, 0.14, 0.21, 0.37, 0.59, 0.62, 2.21, 2.49]
402,30341c403,406
< Eye Right: 276 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -174269, 8: -173788)
< Eye Left: 260 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -164332, 8: -163784)
< Hand Right: 225 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -124366, 8: -123794)
< Hand Left: 222 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -115292, 8: -114854)
---
> Eye Right: 276 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -174282, 8: -173773)
> Eye Left: 260 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -164338, 8: -163777)
> Hand Right: 225 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -124349, 8: -123811)
> Hand Left: 222 trials, latent dimensionality 8 (cross-validated log-likelihood 4: -115301, 8: -114821)
30343,30350c408,415
<  Eye Right Short    0.765    0.524    0.646    0.796    0.263   -6.2e-06   0.00224      NaN       NaN       NaN       NaN
<  Eye Right  Long      NaN      NaN      NaN      NaN    0.989  -6.53e-07    0.0014    0.735     0.935     0.353     0.445
<   Eye Left Short    0.483     0.23    0.304     0.38    0.188   1.39e-06   0.00271      NaN       NaN       NaN       NaN
<   Eye Left  Long      NaN      NaN      NaN      NaN    0.555  -6.76e-06   0.00155    0.921     0.735     0.478     0.406
< Hand Right Short    0.844    0.954     1.04    0.874    0.614   -1.1e-05  0.000555      NaN       NaN       NaN       NaN
< Hand Right  Long      NaN      NaN      NaN      NaN    0.635  -2.22e-05  0.000377     1.65      1.38     0.521     0.272
<  Hand Left Short     0.91     1.22    0.693    0.484    0.688   1.21e-06  0.000947      NaN       NaN       NaN       NaN
[... 74 more lines not kept]
```

**Agent**

The clean run passed in 399 s, and every number matches the previous run except the GPFA values, which vary in the third significant digit between runs; no outcome changes. Now the attempt record.

**Agent calls Write**

```json
{
 "file_path": "attempts/000130-sohn-2019-01.yaml",
 "content": "schema_version: 1\nid: 000130-sohn-2019-01\ndandiset: \"000130\"\ndandiset_version: 0.241017.1448\npaper: doi:10.1016/j.neuron.2019.06.012\ndate: 2026-10-14\nentry: 000130-sohn-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-6\noutcomes:\n- claim: beh-slopes\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-slopes\n  notes: Six of 8 weighted slopes of tp on ts lie between 0 and 1 (0.50 to 0.90) and 5 of 8 have 95%\n    intervals excluding 0 and 1. The Short prior slopes with the eye are 1.11 (Eye Right, interval\n    1.01 to 1.21) and 1.01 (Eye Left). All 8 are positive, so the animal estimated ts; the part of the\n    statement about bias toward the mean fails in the two eye Short conditions.\n  deviations:\n  - One session of monkey H; the paper's slopes come from 17 sessions of H and 12 of G.\n  - Outliers removed with the file's `is_outlier` flag, which a refit of the Methods' mixture model\n    does not reproduce (see findings).\n- claim: beh-overlap-prior\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-overlap-prior\n  notes: At ts = 800 ms the median bias is +28.3 ms for Short (93 trials) and +47.6 ms for Long (107\n    trials), both positive; rank-sum p = 0.073. The Long tp is the longer in 2 of 4 datasets (Hand\n    Right p = 0.00099, Hand Left p = 0.069, where the Short bias is -61.6 ms); in the eye datasets the\n    Short tp is the longer (Eye Left +79.1 against +18.6 ms, p = 0.051).\n  deviations:\n  - One session; the paper's p < 1e-43 pools 17 sessions of monkey H.\n- claim: beh-sigmoid-increments\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-sigmoid-increments\n  notes: The middle increment of mean tp exceeds the extreme one in 7 of 8 conditions (median\n    difference 31.3 ms), two-sided signed-rank p = 0.0156. Hand Left, Short is the exception (-10.7\n    ms).\n  deviations:\n  - The test is over the 8 conditions of one session; the paper's is over sessions and conditions of\n    both animals.\n- claim: beh-long-more-bias\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-long-more-bias\n  notes: The Long slope is below the Short slope in all 4 datasets (mean 0.716 against 0.898),\n    weighted or unweighted.\n  deviations:\n  - One session.\n- claim: beh-bayes-model\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:beh-bayes-model\n  notes: The predicted SD of tp correlates positively with the observed one in all 4 datasets (r =\n    0.28 to 0.91), but the bias R2 reaches 0.8 in 2 of 4 (0.12, 0.67, 0.87, 0.98). The poorly fit\n    datasets are the eye ones, whose Short slopes exceed 1, with wm = 0.013 and 0.025. All fits\n    converged. Table S3 was not available, so wm and wp (0.09 to 0.11) are not compared.\n  deviations:\n  - Fit to one session per effector and direction; the paper pools sessions.\n  - The prior is taken as continuous uniform over each range, as the Results describe; the task used\n    5 discrete values.\n  - The bias R2 threshold of 0.8 is a choice made here; the paper shows the fit graphically.\n- claim: glm-prior-ts\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:glm-prior-ts\n  measured:\n  - 75.0\n  - 45.8\n  notes: 36 of 48 units are prior-dependent (75.0%, 95% interval 61.2 to 85.1%) and 22 of 48 are\n    ts-dependent (45.8%, interval 32.6 to 59.7%), against 65% and 27% for monkey H. Both are outside\n    tolerance and higher; the interval of the prior fraction includes 65%, that of the ts fraction\n    excludes 27%. A likelihood-ratio test gives higher fractions still (prior 77.1 to 87.5%, ts 66.7\n    to 77.1% at p < 0.01 and 0.05).\n  deviations:\n  - 48 units from one session, where the paper's fractions use 536 units of monkey H over 17\n    sessions.\n  - The GLM design with attrition (rows for every trial whose Set comes after each time point) is\n    read from the Methods; the paper's code was not available.\n- claim: dfr-overlap-support\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:dfr-overlap-support\n  notes: The mean RMS rate difference at ts = 800 ms is largest at 480 to 640 ms after Ready (6.86\n    spikes/s), above the 95th percentile of the shuffled maximum (3.11). Before Ready it is at the\n    shuffle level. Per dataset the largest bin is 480-640 (2 datasets), 640-800 and 800-960 ms, and the\n    mean is also high just after Set (6.07 at 800 to 960 ms).\n  deviations:\n  - The time range (320 ms before Ready to 640 ms after Set) and the shuffle reference are chosen\n    here.\n- claim: pca-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:pca-dimensionality\n  notes: Two components reach 75% of the variance in the estimation epoch in all 4 datasets (3 explain\n    86 to 90%), and 2, 2, 5 and 4 in the production epoch; 1 of 8 values is in range. The activity is\n    lower dimensional than reported.\n  deviations:\n  - 48 simultaneously recorded units, where the paper's trial-averaged PCA pools units over 17\n    sessions; more units can add dimensions.\n  - Rates not normalised before PCA; the Methods do not say.\n- claim: encoding-r2\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-r2\n  measured:\n  - 0.998\n  - 0.996\n  notes: Both readings match. (a) Hand Left R2 = 0.998 (Short) and 0.996 (Long), given as measured; (b)\n    the mean of 4 datasets 0.959 and 0.989. With only 2 PCs in the estimation epoch, random unit axes\n    also fit te well (median R2 0.73 to 0.98); the R2 on u exceeds 95% of random axes in 3 of 8\n    dataset-priors (Hand Right Long and both Hand Left), so the paper's statement that the match is\n    specific to u (Figure S5) holds only for those.\n  deviations:\n  - te comes from the observer model fitted to this session.\n  - The encoding axis averages difference vectors up to the middle of the support, a choice made\n    here.\n- claim: encoding-bayes-beats-linear\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:encoding-bayes-beats-linear\n  notes: The Bayesian RMSE is lower in 4 of 4 datasets for Long and 3 of 4 for Short (Hand Right Short\n    0.99 against 0.80). Differences are 0.045 to 0.573 spikes/s.\n  deviations:\n  - 4 datasets, where the paper had 8; a signed-rank test over 4 cannot reach p < 0.05, so the\n    criterion counts datasets.\n- claim: short-in-long-control\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:short-in-long-control\n  notes: Judged on the paper's test as the claims file fixes; signed-rank p = 0.25 over 4 datasets,\n    where the smallest attainable p is 0.125, so the test could not have found an effect. The effect\n    sizes do not show the control's contrast; the Bayesian model is better in 3 of 4 datasets with a\n    median relative RMSE difference of -0.089, at least as large as in the Short prior (-0.060). This\n    outcome carries no evidence for the absence the paper reports.\n  deviations:\n  - 4 datasets, where the paper had 8.\n- claim: neural-long-more-bias\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:neural-long-more-bias\n  notes: The Long slope of Xu on ts is below the Short slope in 4 of 4 datasets (ratios 0.55, 0.63,\n    0.34, 0.97).\n  deviations:\n  - 4 datasets, where the paper had 8.\n- claim: speed-vs-projection\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-vs-projection\n  measured:\n  - -0.941\n  - -0.878\n  notes: Both correlations are negative and significant (Short p = 6.2e-10, Long p = 3.7e-07) and\n    stronger than reported, outside tolerance. Within datasets -0.75 to -1.00; with Xu z-scored per\n    dataset -0.759 and -0.779, and the speed divided by mean tp gives -0.917 and -0.923.\n  deviations:\n  - 20 points per prior (4 datasets), where the paper had 40.\n  - Speed is the mean step between 20 ms states up to the shortest tp; the Methods' division by the\n    Set to Go duration is shown as a variant.\n- claim: initial-speed-biased\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:initial-speed-biased\n  notes: The initial speed falls with ts in 8 of 8 dataset-priors and is shallower than the 1/ts\n    profile in 7 of 8 (Eye Right Long is the exception), two-sided signed-rank p = 0.039. No trial had\n    tp below 400 ms.\n  deviations:\n  - 8 dataset-priors of one animal, where the paper's test combines 16 over two animals.\n- claim: speed-predicts-tp\n  outcome: partially_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:speed-predicts-tp\n  measured:\n  - -0.733\n  - -0.744\n  notes: Faster trajectories go with shorter mean tp in both priors (Short p = 0.00024, Long p =\n    0.00017), more strongly than reported and outside tolerance. Within datasets -0.80 to -0.99. The\n    Neural Latents Benchmark's trial-by-trial variant gives r = -0.195 to -0.740 (mean -0.519), 7 of 8\n    conditions with p < 0.05.\n  deviations:\n  - 20 points per prior, where the paper had 40.\n- claim: alt-speed-unmodulated\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-speed-unmodulated\n  notes: Judged on the paper's test as the claims file fixes; signed-rank p = 0.125 for each prior,\n    the smallest a test over 4 datasets can give. The data show modulation; all 8 slopes are positive\n    (speed rising 13 to 24% of its mean per 100 ms of the support) and all 8 bootstrap intervals over\n    trials exclude zero. The outcome reflects the test's lack of power at this sample size, not an\n    absence of modulation in this session.\n  deviations:\n  - 4 datasets, where the paper had 8.\n  - Speed from smoothed trial-averaged rates with attrition in 20 ms bins of 48 units; the paper's\n    smoothing for this measure is not stated.\n- claim: alt-transient-parallel\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-transient-parallel\n  notes: For the longest ts the distance to the middle trajectory falls in the first 200 ms after Set\n    in 6 of 8 dataset-priors (median -15.3% of the mean distance per 100 ms), signed-rank p = 0.039;\n    for the shortest ts p = 0.078 (6 of 8 rising, median +26.7%). The PCA kept 1 to 4 components, one\n    in Eye Left.\n  deviations:\n  - 8 dataset-priors of one animal, where the paper's test used 16.\n  - Rates smoothed over 100 ms before to 300 ms after Set and cut to the first 200 ms, a choice made\n    here.\n- claim: alt-threshold-monotonic\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:alt-threshold-monotonic\n  notes: With the components reaching 60% of the variance (1 to 3), the median time of the minimum\n    distance is 210 ms before Go; 6 of 32 curves have their minimum in the last 40 ms and 14 in the\n    last 200 ms. Distances do fall overall (the distance at Go is below that 800 ms earlier in 26 of\n    32). With 75% of the variance the median minimum is 80 ms before Go and in the full space 40 ms,\n    which would meet the criterion, so the outcome depends on the number of components; with one\n    component (eye datasets) the distance reaches zero where trajectories cross.\n  deviations:\n  - The paper's test (one-tailed signed-rank, p = 1.5e-4) cannot be read unambiguously; the criterion\n    on the median time of the minimum was fixed before the analysis.\n  - The 60% of variance follows the figure legend; the 75% of the Methods is shown as a variant.\n- claim: gpfa-variance-inverted-u\n  outcome: not_reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:gpfa-variance-inverted-u\n  notes: The quadratic coefficient is negative in 5 of 8 dataset-priors; one-tailed signed-rank p =\n    0.125 (paper 0.0273). Cross-validation chose 8 latent dimensions in all 4 datasets, the larger\n    candidate. GPFA values vary in the third significant digit between runs; the counts and p values\n    did not change over three runs.\n  deviations:\n  - Latent dimensionality chosen only from 4 and 8, with 100 EM iterations, to keep the run short;\n    the paper's cross-validation range is not stated.\n  - One GPFA per effector and direction with both priors; the paper does not say how trials were\n    grouped.\n- claim: gpfa-mean-sigmoid\n  outcome: reproduced\n  notebook: reproduce_sohn_2019.ipynb\n  output: claim:gpfa-mean-sigmoid\n  notes: Middle increments of the mean projection exceed the extreme ones in 8 of 8 (two-sided\n    signed-rank p = 0.0078) and the Short slope is the higher in 4 of 4 datasets (one-tailed p =\n    0.0625), the paper's values; the mean rises with ts in 8 of 8.\n  deviations:\n  - As for gpfa-variance-inverted-u.\n- claim: rnn-curved-manifold\n  outcome: blocked\n  blocked_by: other\n  notes: The claim is about recurrent networks trained in silico. It uses no recorded data, so the\n    dandiset cannot bear on it, and the trained networks and the training code are not public (the\n    code is available from the corresponding author on request).\n- claim: rnn-perturbation\n  outcome: blocked\n  blocked_by: other\n  notes: As for rnn-curved-manifold; the perturbation experiments are on the trained networks.\n- claim: monkey-g\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds one session of monkey H. A search of the DANDI archive for Jazayeri, Sohn,\n    DMFC and Ready-Set-Go finds no other dandiset with these recordings (only 000620, 000897 and\n    001275 of the same lab, on other tasks). The paper says the data are in the article and the code\n    is available on request.\nfindings:\n- kind: data_missing\n  statement: The dandiset holds one recording session (2016-12-11) of monkey H, with 54 units, where\n    the paper analyses 17 sessions of H and 12 of monkey G (617 and 741 units). The dandiset's\n    description does not say that it holds one session of the paper's 29 or which one. The 48 units\n    that pass the paper's rate rule match its count for the single session of H used for GPFA.\n- kind: data_missing\n  statement: Following the Neural Latents Benchmark design, 283 trials of the session are in the test\n    file without ts, tp, prior, effector or direction and without 14 of the 54 units, on a separate\n    clock. These trials cannot be used for any analysis of the paper.\n- kind: metadata_error\n  statement: The description of the `iti` column says 500 ms after Short prior trials and 1220 ms after\n    Long ones; the values are the reverse (Short 1220, Long 500), as the paper states.\n- kind: metadata_insufficient\n  statement: '`tp` is described as the time between Set and Go, but is a median 17.9 ms longer than\n    go_time minus set_time (5th to 95th percentile 1.1 to 29.8 ms, up to 200.6 ms in used trials).\n    `ts` is the nominal interval, within 23.5 ms of ready_time minus set_time. Neither difference is\n    documented.'\n- kind: selection_undocumented\n  statement: The `is_outlier` flag is described only as a probabilistic mixture model. It flags 46\n    completed trials (4.47%); a refit of the Methods' Gaussian and uniform mixture per prior, ts,\n    effector and direction flags 10 of these and no others, and the other 36 have tp from 0.53 to 1.60\n    times ts.\n- kind: metadata_insufficient\n  statement: Units carry no single-unit or multi-unit label and no electrode or probe; the electrode\n    table has no positions or impedances and gives the filtering as unknown. The paper distinguishes\n    456 single units from 902 multi-units.\n- kind: methods_unavailable\n  statement: The paper's analysis code is available only on request. The code the dandiset links\n    (nlb_tools) loads the data and scores benchmark models, and holds none of the paper's analyses.\n- kind: paper_inconsistency\n  statement: The Results give the GPFA sessions as N = 48 for monkey H and N = 107 for monkey G, the\n    Methods as N = 48 in H and 96 in G.\n"
}
```

```
File created successfully at: attempts/000130-sohn-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml,re
for p in ['attempts/000130-sohn-2019-01.yaml','claims/000130/10.1016-j.neuron.2019.06.012.yaml']:
    d=yaml.safe_load(open(p))
    def walk(x,path=''):
        if isinstance(x,dict):
            for k,v in x.items(): walk(v,path+'/'+str(k))
        elif isinstance(x,list):
            for i,v in enumerate(x): walk(v,path+f'[{i}]')
        elif isinstance(x,str) and (': ' in x): print(p,path,'COLON',x[:80])
    walk(d)
    print(p,'ok')
for p in ['attempts/000130-sohn-2019-01.yaml','claims/000130/10.1016-j.neuron.2019.06.012.yaml','entries/000130-sohn-2019/README.md','entries/000130-sohn-2019/rsg.py','/tmp/claude/nb_cells.py','/tmp/claude/conclusions.py','entries/000130-sohn-2019/entry.yaml']:
    s=open(p).read()
    for w in ['—','rather','**']:
        if w in s and not (w=='**' and p.endswith(('nb_cells.py','conclusions.py'))): print(p,'contains',w)
E
grep -n "\*\*" /tmp/claude/nb_cells.py /tmp/claude/conclusions.py | grep -v "\*\*Result:" | head; grep -n -i "rather" /tmp/claude/*.py entries/000130-sohn-2019/* claims/000130/* attempts/000130* | head
python tools/entry.py check entries/000130-sohn-2019
```

```
attempts/000130-sohn-2019-01.yaml ok
claims/000130/10.1016-j.neuron.2019.06.012.yaml ok
entries/000130-sohn-2019/rsg.py contains **
/tmp/claude/nb_cells.py:19:**Paper.** Sohn H, Narain D, Meirhaeghe N, Jazayeri M (2019). Bayesian computation through cortical
/tmp/claude/nb_cells.py:25:**Dandiset.** [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version
/tmp/claude/nb_cells.py:32:**What the dandiset holds.** One recording session (2016-12-11) of monkey H ("Haydn"), from the
/tmp/claude/nb_cells.py:39:**Code.** The paper's code is "available from the corresponding author on request" and was not
/tmp/claude/nb_cells.py:404:    r2 = 1 - np.sum((ob - pb) ** 2) / np.sum((ob - ob.mean()) ** 2)
/tmp/claude/nb_cells.py:536:    return np.sqrt(np.mean((d * 1000 / 160) ** 2, axis=1))  # spikes/s
/tmp/claude/nb_cells.py:549:tab = pd.DataFrame({"bin_start": edges[:-1], "bin_end": edges[1:], **{k: v for k, v in per_ds.items()},
/tmp/claude/nb_cells.py:608:    EST[name] = {"pca": pca_e, **est}
/tmp/claude/nb_cells.py:805:        rows.append({"dataset": name, "prior": "Short" if short else "Long", **{f"speed_{int(t)}": s for t, s in zip(ts_v, sp)},
/tmp/claude/nb_cells.py:1051:        rows.append({"dataset": name, "prior": "Short" if short else "Long", **{f"var_{t}": v for t, v in zip(ts_v, var)},
grep: entries/000130-sohn-2019/__pycache__: Is a directory
0 error(s)
```

**Agent**

Bold labels in the notebook header and summary break the style rule; removing them and re-running so the executed copy matches.

**Agent calls Bash**

```bash
cd /tmp/claude && python - <<'E'
import re
for p in ['nb_cells.py','conclusions.py']:
    s=open(p).read()
    s=re.sub(r'\*\*((Paper|Dandiset|What the dandiset holds|Code|How the analysis differs from the paper\'s|What was found about the dandiset)\.)\*\*', r'\1', s)
    open(p,'w').write(s)
E
grep -n '\*\*[A-Z]' nb_cells.py conclusions.py | grep -v "Result:" ; rm -rf entries/000130-sohn-2019/__pycache__; cd  && python /tmp/claude/build_nb.py && python tools/entry.py all entries/000130-sohn-2019 2>&1 | tail -3
```

```
wrote entries/000130-sohn-2019/reproduce_sohn_2019.ipynb 79 cells
Installed kernelspec registry-000130-sohn-2019 in executed/000130-sohn-2019/.venv/share/jupyter/kernels/registry-000130-sohn-2019
0 error(s)
pass  reproduce_sohn_2019.ipynb  (397 s)
```

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/ex/bin/python show.py executed/000130-sohn-2019/reproduce_sohn_2019.ipynb > final2.txt 2>/dev/null; diff <(grep -v "loaded dandiset\|took\|run time\|^$" final.txt) <(grep -v "loaded dandiset\|took\|run time\|^$" final2.txt) | grep -v "latent dimensionality" | head -40; grep "Quadratic\|Middle increment above\|Short slope above" final2.txt; cd  && python tools/entry.py handover entries/000130-sohn-2019 && ls -R executed/000130-sohn-2019/handover && git status --short
```

```
433,436c433,436
---
438,445c438,445
<  Eye Right Short    0.761    0.523    0.645    0.794    0.262  -6.26e-06   0.00225      NaN       NaN       NaN       NaN
<  Eye Right  Long      NaN      NaN      NaN      NaN    0.988  -6.71e-07    0.0014    0.733     0.935     0.354     0.444
<   Eye Left Short    0.485     0.23    0.303     0.38    0.188   1.43e-06   0.00271      NaN       NaN       NaN       NaN
<   Eye Left  Long      NaN      NaN      NaN      NaN    0.556  -6.78e-06   0.00155    0.919     0.736      0.48     0.405
< Hand Right Short    0.844     0.95     1.04    0.879    0.615  -1.11e-05  0.000558      NaN       NaN       NaN       NaN
< Hand Right  Long      NaN      NaN      NaN      NaN    0.632  -2.24e-05  0.000374     1.65      1.38     0.517      0.27
<  Hand Left Short     0.91     1.21    0.695    0.485    0.685   1.16e-06  0.000945      NaN       NaN       NaN       NaN
<  Hand Left  Long      NaN      NaN      NaN      NaN     1.27   5.92e-06  0.000455     1.43     0.465     0.705      0.68
---
>  Eye Right Short    0.766    0.524    0.647    0.799    0.262  -6.25e-06   0.00224      NaN       NaN       NaN       NaN
>  Eye Right  Long      NaN      NaN      NaN      NaN    0.988  -6.05e-07    0.0014    0.732     0.932     0.355     0.445
>   Eye Left Short    0.484    0.231    0.306    0.381    0.189   1.36e-06    0.0027      NaN       NaN       NaN       NaN
>   Eye Left  Long      NaN      NaN      NaN      NaN    0.556  -6.79e-06   0.00155     0.92     0.737     0.478     0.405
> Hand Right Short    0.844    0.952     1.04    0.875    0.615   -1.1e-05  0.000557      NaN       NaN       NaN       NaN
> Hand Right  Long      NaN      NaN      NaN      NaN    0.636  -2.22e-05  0.000375     1.65      1.38     0.525     0.273
>  Hand Left Short    0.911     1.21    0.688    0.478    0.693   1.57e-06   0.00094      NaN       NaN       NaN       NaN
>  Hand Left  Long      NaN      NaN      NaN      NaN     1.25   5.78e-06  0.000451     1.44     0.
[... 42 more lines not kept]
```

**Agent**

GPFA counts and p values are unchanged over four runs. Updating that note and running the final check.

**Agent calls Bash**

```bash
sed -i 's/did not change over three runs/did not change over four runs/' attempts/000130-sohn-2019-01.yaml && sed -i 's/runtime_minutes: 8/runtime_minutes: 7/; ' entries/000130-sohn-2019/entry.yaml && sed -i 's/It takes about eight minutes/It takes about seven minutes/' entries/000130-sohn-2019/README.md && python tools/entry.py check entries/000130-sohn-2019 && python tools/entry.py handover entries/000130-sohn-2019 && ls -la .bashrc .gitconfig scripts | head; git check-ignore -v paper executed | head
```

```
0 error(s)
wrote executed/000130-sohn-2019/handover
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 16:00 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 16:00 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 14 16:00 scripts
.gitignore:8:paper/	paper
.gitignore:6:executed/	executed
```

**Agent**

I've finished steps 1 to 6 for dandiset 000130. `entry.py check` reports 0 errors, the notebook passes `entry.py all` from a clean environment in 397 s, and the verifier's package is built in `executed/000130-sohn-2019/handover/`. Nothing is committed.

**Paper text:** I used the full text of the accepted author manuscript (PMC6805134). It is saved under `paper/`. The supplementary tables and figures were not available.

**Version pinned:** 0.241017.1448. The paper cites no DANDI version. The two published versions hold the same two files and differ only in publication metadata, so I pinned the most recent; the notebook header says why.

### 1. Outcome per claim

| Claim | Outcome |
|---|---|
| beh-slopes | Not reproduced: 6 of 8 slopes between 0 and 1; the two Eye Short slopes are 1.11 and 1.01 |
| beh-overlap-prior | Not reproduced: both biases positive (+28 and +48 ms), p = 0.073 |
| beh-sigmoid-increments | Reproduced: 7 of 8, p = 0.016 |
| beh-long-more-bias | Reproduced: 4 of 4 |
| beh-bayes-model | Partially reproduced: SD fits in 4 of 4, bias R2 ≥ 0.8 in only 2 of 4 |
| glm-prior-ts | Not reproduced: 75.0% and 45.8%, against the paper's 65% and 27% |
| dfr-overlap-support | Reproduced: largest at 480 to 640 ms after Ready |
| pca-dimensionality | Not reproduced: 2 PCs reach 75% in the estimation epoch |
| encoding-r2 | Reproduced: 0.998 and 0.996, but random axes beat it in 5 of 8 dataset-priors |
| encoding-bayes-beats-linear | Partially reproduced: Long 4 of 4, Short 3 of 4 |
| short-in-long-control | Reproduced by the paper's test, which cannot detect an effect with 4 datasets |
| neural-long-more-bias | Reproduced: 4 of 4 |
| speed-vs-projection | Partially reproduced: rho −0.94 and −0.88, stronger than reported |
| initial-speed-biased | Reproduced: 7 of 8, p = 0.039 |
| speed-predicts-tp | Partially reproduced: rho −0.73 and −0.74, stronger than reported |
| alt-speed-unmodulated | Reproduced by the paper's test, but the speed rises in all 8 dataset-priors (bootstrap intervals exclude 0) |
| alt-transient-parallel | Not reproduced: longest ts, p = 0.039 |
| alt-threshold-monotonic | Not reproduced: median minimum 210 ms before Go; depends on how many PCs are kept |
| gpfa-variance-inverted-u | Not reproduced: 5 of 8, p = 0.125 |
| gpfa-mean-sigmoid | Reproduced: p = 0.0078 and 0.0625, the paper's exact values |
| rnn-curved-manifold, rnn-perturbation | Blocked (`other`): these concern trained network models, not recorded data |
| monkey-g | Blocked (`data_missing`) |

### 2. What was found about the dandiset
- **One session only.** It is the Neural Latents Benchmark version of a single session of monkey H (2016-12-11), out of the paper's 29 sessions over two monkeys. No other dandiset on the archive holds these recordings.
- **Likely the paper's GPFA session.** 48 of its 54 units pass the paper's 1 spike/s rule, which matches the paper's GPFA count for monkey H. The dandiset does not say this.
- **Test trials unusable.** 283 trials are in the test file with no task variables and without 14 of the 54 units, so no analysis can use them.
- **`iti` description reversed.** It says 500 ms after Short trials and 1220 after Long; the values (and the paper) are the other way round.
- **`tp` does not match the event times.** It is a median 18 ms longer than `go_time − set_time` (up to 200 ms), and this is not documented.
- **`is_outlier` not reproduced.** A refit of the paper's mixture model flags only 10 of the file's 46 outliers.
- **Units under-described.** There is no single-unit or multi-unit label and no electrode assignment, and the electrode table has no positions.
- **Code not public.** The paper's code is available only on request, and the linked benchmark code holds none of its analyses.
- **Paper inconsistency.** The Results give the GPFA counts as 48 and 107 neurons; the Methods give 48 and 96.

### 3. Where the protocol was unclear, wrong or missing something
1. **Claims of absence tested on a subset.** "Judged on the paper's test alone" breaks down when the dandiset holds 4 of the paper's 8 datasets. A signed-rank test over 4 can never give p < 0.05, so two absence claims come out "reproduced" automatically, one of them against clear evidence. I followed the rule and said so in each claim's notes and Result text.
2. **No guidance on adapting the paper's statistics to a subset.** Where the paper's p = 0.008 means "all 8 datasets", I wrote criteria that count datasets (for example, 4 of 4).
3. **The default 10% tolerance fits some measures badly.** For R2 near 1 it accepts anything above 0.894. For a proportion from 48 units, sampling error is larger than 10%. I kept the default and reported binomial intervals.
4. **No blocking reason for model-only claims.** For the recurrent network claims I used `other`.
5. **No place in the record for the code read.** When the linked code is unrelated to the paper's analyses, there is no field for it (`inputs` is for data). I recorded the repository and commit in the notebook header and added a `methods_unavailable` finding.
6. **The suggested clock check confounds latency with offset.** Decoding peaks at +100 ms for every event, which reflects response latency. I reported the check as consistent with a shared clock, not as shown.
7. **Fixed seeds do not make the GPFA fits deterministic.** Values move in the third significant digit between runs (probably multithreaded numerics); counts and p values were unchanged over four runs. I noted this.
8. **Bug fixed after seeing outputs.** The Bayesian observer's optimiser left the offsets at 0 because its first step from a zero start is tiny. I fixed the optimiser after the first run without changing any criterion. The protocol does not say how to record such a fix; it is not in the attempt record.
9. **Ambiguous test in the paper.** The paper's test for the threshold claim (one-tailed, p = 1.5e-4) cannot be read unambiguously. I fixed my own criterion before the analysis and recorded it as a deviation.

### 4. Runtime and failures
- **Runtime.** The notebook takes about 400 s, of which GPFA is about 360 s.
- **Failures.** Europe PMC's full-text XML endpoint returned an HTTP 500, so I used the NCBI BioC API for the same manuscript. The first notebook run had the optimiser bug in point 8. Nothing else failed.
- **Untracked files not created by me.** `git status` shows `.bashrc`, `.gitconfig`, `scripts` and similar at the repo root. They are character devices from the sandbox, not files, and should not be committed.

Files are in the repository root:
- `claims/000130/10.1016-j.neuron.2019.06.012.yaml`
- `attempts/000130-sohn-2019-01.yaml`
- `entries/000130-sohn-2019/`

## End of run

61 turns, 49 minutes, result: success.
