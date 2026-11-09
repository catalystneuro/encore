# 000114 · verifier-1 · run 38972882532

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs paper 2>/dev/null; cat *.y*ml *.json 2>/dev/null | head -100
```

```
total 180
drwxr-xr-x 5 runner runner    4096 Oct 16 22:00 .
drwxr-xr-x 7 runner runner    4096 Oct 16 22:00 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 16 22:00 .claude
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.development
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.local
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.production
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.test
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .env.test.local
drwx------ 2 runner runner    4096 Oct 16 22:00 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .github
-rw-r--r-- 1 runner runner       0 Oct 16 22:00 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 16 21:58 .mcp.json
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 100,400p 10.1038-s41586-021-03814-7.yaml
```

```
expected:
  - quantity: Fraction of units activated during shepherding, OT-PVN and PVN pooled (14 of 118)
    value: 11.9
    tolerance: 1.19
    unit: percent
  criterion: Method as in the file header, on all units of the sessions that have at least one
    "Mom agressing" episode, with the 10 s baseline of the Methods. Readings (a) pooled, 14 of
    118 = 11.9%, and (b) PVN only, 9 of 97 = 9.3% (tolerance 0.93). Reproduced when the fraction
    is within tolerance under either reading and the Fisher test gives p < 0.05; partially
    reproduced when p < 0.05 but the fraction is outside both; not reproduced when p >= 0.05.
- id: ed7a-dam-retrieval-fraction
  statement: Spontaneous pup retrieval by the dam, in which the virgin was not involved, activated
    a significant fraction of virgin PVN units (5 of 17 OT-PVN and 10 of 69 PVN units; p = 0.02
    and 0.0007).
  source: Fig. 3b, c; Extended Data Fig. 7a (right); Source Data Fig. 3c
  data: with_labels
  depends_on:
  - label-link
  expected:
  - quantity: Fraction of units activated during dam retrieval, OT-PVN and PVN pooled (15 of 86)
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_carcea_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'===== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
"
```

```
<persisted-output>
Output too large (52.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/65760a94-1b96-42d8-a074-86c2ba4bf2ec/tool-results/b2m76o1z8.txt

Preview (first 2KB):
===== [0] markdown
# Reproducing Carcea et al. (2021) from dandiset 000114

**Paper.** Carcea I, Caraballo NL, Marlin BJ, et al. (2021). Oxytocin neurons enable social
transmission of maternal behaviour. *Nature* 596, 553-557.
[doi:10.1038/s41586-021-03814-7](https://doi.org/10.1038/s41586-021-03814-7). This attempt used
the full text, which is open access (CC BY, PMC8387235), with its Source Data spreadsheets for the
reported numbers.

**Dandiset.** [DANDI:000114](https://dandiarchive.org/dandiset/000114/0.230602.1643), version
0.230602.1643. The paper cites the dandiset without a version (it was published in 2021, before
this version). This is the only published version. The draft holds the same 30 files; each is
240 bytes or 6 KB larger, and the check below finds the same spike times and events in one draft
file. The other draft files were not compared, so the draft is taken to match on that basis.

**What the dandiset holds.** PVN recordings from five virgins co-housed with a dam and litter
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/65760a94-1b96-42d8-a074-86c2ba4bf2ec/tool-results/b2m76o1z8.txt"
}
```

```
1	===== [0] markdown
2	# Reproducing Carcea et al. (2021) from dandiset 000114
3	
4	**Paper.** Carcea I, Caraballo NL, Marlin BJ, et al. (2021). Oxytocin neurons enable social
5	transmission of maternal behaviour. *Nature* 596, 553-557.
6	[doi:10.1038/s41586-021-03814-7](https://doi.org/10.1038/s41586-021-03814-7). This attempt used
7	the full text, which is open access (CC BY, PMC8387235), with its Source Data spreadsheets for the
8	reported numbers.
9	
10	**Dandiset.** [DANDI:000114](https://dandiarchive.org/dandiset/000114/0.230602.1643), version
11	0.230602.1643. The paper cites the dandiset without a version (it was published in 2021, before
12	this version). This is the only published version. The draft holds the same 30 files; each is
13	240 bytes or 6 KB larger, and the check below finds the same spike times and events in one draft
14	file. The other draft files were not compared, so the draft is taken to match on that basis.
15	
16	**What the dandiset holds.** PVN recordings from five virgins co-housed with a dam and litter
17	(V85, V110, V111, V116, V118): raw voltage from a 16-wire bundle, sorted units for four of them in
18	8 of 17 files, and video annotations. Fibre photometry from six non-co-housed virgins during
19	observation of dam retrievals (ROV40 to ROV49). It does not hold the optical tagging that
20	identifies oxytocin (OT-PVN) units, the behaviour of Figure 1, the unit recordings during
[... 733 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "pvn.py"
}
```

```
1	"""Loading and measures for dandiset 000114 (Carcea et al. 2021, Nature 596:553).
2	
3	The dandiset holds three kinds of file:
4	
5	- ``sub-V*_ecephys.nwb``: 12 to 16 h recordings from a 16-wire bundle in the PVN of virgin
6	  mice co-housed with a dam and litter (30 kHz raw voltage), some with a ``units`` table of
7	  sorted spike times and a ``behavioral_events`` table of video annotations;
8	- ``sub-ROV*_ophys.nwb``: fibre photometry of non-co-housed virgins during observation of dam
9	  retrievals ("obs") and their own retrieval tests ("retrieval"), with "Pup out" and
10	  "retrieval" events.
11	
12	Files are streamed from the DANDI Archive with remfile and h5py at the pinned version; the
13	raw voltage is never read. Groups are walked by name, as h5py's ``visititems`` stalls on the
14	large ecephys files.
15	
16	Parameters of the unit analysis, and where they come from:
17	
18	- ``NEST_CAP_S = 40``: nest entry episodes are cut at 40 s (Methods, Spike train analysis).
19	  The paper's code has the cap commented out.
20	- ``GAP_S = 0.5``: the equal-duration baseline ends 0.5 s before the episode
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
cd  B=https://api.dandiarchive.org/api/dandisets/000114/versions/0.230602.1643; curl -s "$B/" > $TMPDIR/meta.json; curl -s "$B/assets/?page_size=100" > $TMPDIR/assets.json; python3 -c "
import json,os
m=json.load(open(os.environ['TMPDIR']+'/meta.json'))
print(m.get('description')); print(m.get('assetsSummary')); print([ (r.get('name'),r.get('url')) for r in m.get('relatedResource',[])])
a=json.load(open(os.environ['TMPDIR']+'/assets.json'))
print(a['count'])
for x in a['results']: print(x['path'], x['size'])
"
```

```
Maternal care, including by non-biological parents, is important for offspring survival. Oxytocin which is released by the hypothalamic paraventricular nucleus (PVN), is a critical maternal hormone. In mice, oxytocin enables neuroplasticity in the auditory cortex for maternal recognition of pup distress. However, it is unclear how initial parental experience promotes hypothalamic signalling and cortical plasticity for reliable maternal care. Here we continuously monitored the behaviour of female virgin mice co-housed with an experienced mother and litter. This documentary approach was synchronized with neural recordings from the virgin PVN, including oxytocin neurons. These cells were activated as virgins were enlisted in maternal care by experienced mothers, who shepherded virgins into the nest and demonstrated pup retrieval. Virgins visually observed maternal retrieval, which activated PVN oxytocin neurons and promoted alloparenting. Thus rodents can acquire maternal behaviour by social transmission, providing a mechanism for adapting the brains of adult caregivers to infant needs via endogenous oxytocin.
{'species': [{'name': 'Mus musculus - House mouse', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_10090'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 387202184927, 'numberOfFiles': 30, 'numberOfSubjects': 11, 'variableMeasured': ['ProcessingModule', 'ElectricalSeries', 'ElectrodeGroup', 'Units'], 'measurementTechnique': [{'name': 'analytical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'spike sorting tec
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC8387235/unicode" -o paper/PMC8387235_bioc.json; ls -la paper; python3 -c "
import json
d=json.load(open('paper/PMC8387235_bioc.json'))
d=d[0] if isinstance(d,list) else d
out=[]
for doc in d['documents']:
  for p in doc['passages']:
    out.append(f\"[{p['infons'].get('section_type','')}] {p['text']}\")
open('paper/PMC8387235.txt','w').write('\n\n'.join(out)); print(len(out))
"; wc -c paper/PMC8387235.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  cat paper/PMC8387235_bioc.json; echo; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8387235/fullTextXML" -o paper/PMC8387235.xml; ls -la paper; head -c 300 paper/PMC8387235.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  rm paper/PMC8387235_bioc.json; python3 -c "
import re,xml.etree.ElementTree as ET
t=ET.parse('paper/PMC8387235.xml').getroot()
txt=' '.join(t.itertext()); txt=re.sub(r'\s+',' ',txt)
open('paper/PMC8387235.txt','w').write(txt); print(len(txt))
"; grep -oiE "[^.]{0,400}(spike train analysis|shepherd|nest entr|40 s|Benjamini|Fisher|shuffl|10 s|dwell|similar in duration)[^.]{0,400}\." paper/PMC8387235.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
t=open('paper/PMC8387235.txt').read()
for key in ['Spike train analysis To analyse','Fig. 1j , we used','once every','0.2 events','Frequency of shepherding events','Extended Data Fig. 8','spontaneous','Note differences between time','chance']:
    i=t.find(key)
    while i!=-1 and key in ('once every','spontaneous','chance','Extended Data Fig. 8'):
        print('>>',key,':',t[max(0,i-300):i+400].replace('\n',' '),'\n'); i=t.find(key,i+1)
        if key=='Extended Data Fig. 8': break
    if i!=-1 and key not in ('once every','spontaneous','chance','Extended Data Fig. 8'):
        print('>>',key,':',t[i:i+2600 if key.startswith('Spike') else i+700],'\n')
E
```

Result: not kept, because it reads the paper's text.

**Agent**

Notebook, helper and paper Methods are read. Next I'm testing the helper's shuffle test on synthetic Poisson units with no response to see its false-positive rate.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import numpy as np, pvn
from statsmodels.stats.multitest import multipletests
rng=np.random.default_rng(0)
# BH check
for _ in range(200):
    p=rng.uniform(0,0.1,30); p[rng.integers(0,30,3)]=np.nan
    ok=~np.isnan(p); ref=np.zeros(30,bool); ref[ok]=multipletests(p[ok],0.05,'fdr_bh')[0]
    assert (ref==pvn.bh(p)).all()
print("bh matches statsmodels")
T=12*3600
def sim(rate, starts, durs, cap, baseline, nunits=30, reps=3):
    act=[];sup=[]
    for r in range(reps):
        st=np.array(starts); en=st+np.array(durs)
        if cap: en=np.minimum(en, st+cap)
        sh=pvn.draw_shifts(rng)
        res=[pvn.shuffle_test(np.sort(rng.uniform(0,T,rng.poisson(rate*T))),st,en,baseline,sh) for _ in range(nunits)]
        p=np.array([x[2] for x in res]); mi=np.array([x[0] for x in res]); s=pvn.bh(p)
        act.append(np.mean(s&(mi>0))); sup.append(np.mean(s&(mi<0)))
    return np.mean(act), np.mean(sup)
# nest-entry-like: 20 long episodes, capped 40 s
st=np.sort(rng.uniform(1000,T-3000,20)); 
for rate in (0.05,0.3,5):
    print("nest cap40 rate",rate, sim(rate, st, np.full(20,1500.), 40,'equal'))
# shepherding-like: 4 short episodes (3 s), pre10
st4=np.sort(rng.uniform(1000,T-1000,4))
for rate in (0.05,0.3,5):
    print("shep 4x3s pre10 rate",rate, sim(rate, st4, np.full(4,3.), None,'pre10'))
st1=np.array([20000.])
for rate in (0.3,5,20):
    print("retrieval 1x5s pre10 rate",rate, sim(rate, st1, [5.], None,'pre10'))
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -d .venv venv 2>/dev/null; which -a python python3 uv pip 2>/dev/null; python3 -m pip --version
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
pip 26.2.1 from /opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy scipy pandas statsmodels h5py remfile dandi 2>&1 | tail -3; python -c "import numpy, scipy, pandas, statsmodels, h5py, remfile, dandi; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'E'
import numpy as np, pvn
from statsmodels.stats.multitest import multipletests
rng=np.random.default_rng(0)
for _ in range(200):
    p=rng.uniform(0,0.1,30); p[rng.integers(0,30,3)]=np.nan
    ok=~np.isnan(p); ref=np.zeros(30,bool); ref[ok]=multipletests(p[ok],0.05,'fdr_bh')[0]
    assert (ref==pvn.bh(p)).all()
print("bh matches statsmodels")
T=12*3600
def sim(rate, starts, durs, cap, baseline, nunits=30, reps=4):
    act=[];sup=[];praw=[]
    for r in range(reps):
        st=np.array(starts,float); en=st+np.array(durs,float)
        if cap: en=np.minimum(en, st+cap)
        sh=pvn.draw_shifts(rng)
        res=[pvn.shuffle_test(np.sort(rng.uniform(0,T,rng.poisson(rate*T))),st,en,baseline,sh) for _ in range(nunits)]
        p=np.array([x[2] for x in res]); mi=np.array([x[0] for x in res]); s=pvn.bh(p)
        act.append(np.mean(s&(mi>0))); sup.append(np.mean(s&(mi<0))); praw.append(np.nanmean((p<0.05)&(mi>0)))
    return f"activated {np.mean(act):.3f} suppressed {np.mean(sup):.3f} raw p<.05 & +: {np.mean(praw):.3f}"
st=np.sort(rng.uniform(1000,T-3000,20))
for rate in (0.05,0.3,5):
    print("nest 20 eps cap40 rate",rate, sim(rate, st, np.full(20,1500.), 40,'equal'))
st4=np.sort(rng.uniform(1000,T-1000,4))
for rate in (0.05,0.3,5):
    print("shep 4x3s pre10 rate",rate, sim(rate, st4, np.full(4,3.), None,'pre10'))
for rate in (0.3,5,20):
    print("retrieval 1x5s pre10 rate",rate, sim(rate, [20000.], [5.], None,'pre10'))
E
```

```
bh matches statsmodels
nest 20 eps cap40 rate 0.05 activated 0.017 suppressed 0.000 raw p<.05 & +: 0.083
nest 20 eps cap40 rate 0.3 activated 0.000 suppressed 0.000 raw p<.05 & +: 0.033
nest 20 eps cap40 rate 5 activated 0.000 suppressed 0.000 raw p<.05 & +: 0.067
shep 4x3s pre10 rate 0.05 activated 0.167 suppressed 0.425 raw p<.05 & +: 0.175
shep 4x3s pre10 rate 0.3 activated 0.000 suppressed 0.042 raw p<.05 & +: 0.025
shep 4x3s pre10 rate 5 activated 0.000 suppressed 0.000 raw p<.05 & +: 0.042
retrieval 1x5s pre10 rate 0.3 activated 0.025 suppressed 0.200 raw p<.05 & +: 0.058
retrieval 1x5s pre10 rate 5 activated 0.000 suppressed 0.000 raw p<.05 & +: 0.058
retrieval 1x5s pre10 rate 20 activated 0.000 suppressed 0.000 raw p<.05 & +: 0.033
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pvn
for k,n in [(6,21),(33,126),(3,194),(4,194),(4,101),(13,132),(42,194)]: print(k,n,round(pvn.fisher_vs_zero(k,n),5))
import numpy as np
s=np.array([1.,2,3]); print(pvn.modulation(np.sort(np.r_[np.linspace(0,9.9,10), np.linspace(10,14.9,20)]), np.array([10.]), np.array([15.]), 'pre10'))
"
```

```
6 21 0.01034
33 126 0.0
3 194 0.12403
4 194 0.06153
4 101 0.06064
13 132 9e-05
42 194 0.0
[56.8627451]
```

**Agent**

**A. Outcomes** (all 19 claims in `10.1038-s41586-021-03814-7.yaml`; no separate attempt record was among my materials)

| Claim | Outcome | Reason |
|---|---|---|
| label-link | reproduced | Cell 15: in V116 03122018, 7 of 7 "Mom agressing" intervals coincide with "Shepherding" and 2 of 2 "Mom retrieval" with "Self gen retrieval". Pooled "Virgin in rest" ≤40 s is 366/499 = 73.3%, inside 63.5–77.6. This passes on V111 (343 of the 499 intervals); V116 and V118 give 9.9% and 0% (problem 6). |
| ed7a-nest-entry-fraction | partially_reproduced | Cell 17: 42/194 = 21.6% activated, Fisher p = 1.9e-14. That is outside both tolerances (23.9–29.2 and 23.6–28.8). 37 of the 42 are in V116. Without the 40 s cap, as in the authors' code, it is 2/194 (cell 18). |
| ed7a-shepherding-fraction | not_reproduced | Cell 20: 3/194 = 1.5%, Fisher p = 0.12 (≥ 0.05). Only the code's equal-duration baseline variant gives p < 0.05 (9/194, 4.6%), and that fraction is still far below 9.3–11.9%. |
| ed7a-dam-retrieval-fraction | partially_reproduced | Cell 22: 13/132 = 9.8%, p = 9e-05, below both tolerance ranges. Nine of the 13 come from one V111 session with a single retrieval episode. With sessions of ≥2 episodes it is 4/101, p = 0.061, which would be not reproduced. |
| fig2j-shepherded-entry | not_reproduced | Cell 24: 128 units, median shepherded − voluntary = 3.9, Wilcoxon p = 0.182. The 5 s and 30 s windows give p = 0.37 and 0.17. Two sessions go in opposite directions (V110 p = 5e-9 one way, V116 03102018 p = 0.007 the other). |
| fig1j-shepherding-rate | partially_reproduced | Cell 26: mean 0.65/h (s.e.m. 0.17, n = 10 sessions), t-test against 0.2 gives p = 0.029, so the t-test part holds. The mean is far outside 3.5 ± 0.9. Per mouse, p = 0.19. |
| ed8a-dam-retrieval-rate | not_reproduced | Cell 28: mean 0.21/h, outside both 0.45–0.55 and 0.31–0.66. Two of the 10 sessions have no "Mom retrieval" events. |
| ot-pvn-units | blocked (data_missing) | The asset list (30 files) has no optical-tagging recordings. The units table has only `spike_times` and `unit_name` (cell 3). The `unit_name` values are never printed (see C). |
| fig2f-virgin-chasing | blocked (metadata_insufficient) | "Virgin Agressing" exists (1 to 15 per session in V110, V111 and V116; cell 7), but nothing defines it. Taking it to mean virgin→dam chases, a test could run, but only on the 3 shepherding-activated units, not the paper's 6. |
| ed6-dam-vs-pup | blocked (data_missing) | There are no 5-min interaction periods and no audio. All acquisition series are 16-channel 30 kHz voltage, too slow for ultrasonic calls. |
| fig1cd-retrieval-onset | blocked (data_missing) | No retrieval-test data for the co-housed cohorts in the asset list. |
| fig2a-dreadd | blocked (data_missing) | No DREADD cohort files. |
| fig3fg-observational-learning | blocked (data_missing) | No observation-cohort retrieval scores. |
| fig3ij-observation-units | blocked (data_missing) | Every ecephys file is a multi-hour home-cage recording; none is an observation session. |
| fig4c-ac-photometry | blocked (data_missing) | No auditory cortex photometry during co-housing and no pup-call times. The ophys events are only "Pup out" and "retrieval". |
| fig4f-pvn-ac-correlation | blocked (data_missing) | No simultaneous units and photometry. |
| fig4i-projection-photometry | blocked (metadata_insufficient) | Partly testable. Responses to the dam's retrievals can be computed for all six ROV animals from their obs files. ROV40 and ROV41 have retrieval-test files with retrievals, so they are probable learners. ROV43/44/45/49 have no test files, so the 3-vs-3 split cannot be formed. Fibre location is "unknown". |
| fig4jk-oxytocin-in-ac | blocked (data_missing) | No infusion or optogenetic cohort files. |
| ed9-colliculus | blocked (data_missing) | No tracing data or stimulation cohort. |

Tally: 1 reproduced, 3 partially_reproduced, 3 not_reproduced, 12 blocked.

**B. Problems**

1. [affects a conclusion] `pvn.shuffle_test` / `pvn.modulation`: on the real episodes, an episode with no spikes in either window is dropped; in the shuffles it counts as 0, as in the authors' code. This inflates significance for sparse units with few short episodes. On synthetic Poisson units with no response (4 episodes of 3 s, 10 s baseline, 0.05 Hz), 17% come out "activated" and 43% "suppressed" after BH. At 0.3 Hz and above it is about 0–4%. V116 medians are 0.23–0.37 Hz (min 0.006), and the shepherding and retrieval tables have values at ±100 and high suppressed counts (V116 03092018: 10/21). The positive results are biased upward, so the not-reproduced outcomes stand, but the suppressed counts are unreliable.
2. [affects a conclusion] Cell 22: 9 of the 13 dam-retrieval activations come from one episode in V111 03032018. V111 units have 86% of spikes coincident with another unit within 0.1 ms (cell 5), so these 9 are probably not independent neurons. The Fisher test treats them as independent.
3. [affects a conclusion] Cells 5 and 17–24: V111's 31 units are probably the same clusters on three days (log spike-count correlation 0.93–0.97). They are counted as 93 units in all fractions and in the fig2j Wilcoxon test. V110 and V111 also have 7–9% of inter-spike intervals under 2 ms and 79–90% coincident spikes. The notebook flags this but keeps them in the headline numbers.
4. [affects a conclusion] Cell 9: the shared-clock test fails in every session (best rank 17/121), and the analysis proceeds anyway. In V116 03102018 the spikes and events run to 13.46 h against 4.46 h of raw voltage, so their clock relation to the raw series is unknown. That session has 17/26 nest-entry activations.
5. [affects a conclusion] Cell 26 / `session_length_s`: the rate denominators assume each session was annotated over its whole length. Annotation coverage is never checked. If only part of each session was scored, both fig1j and ed8a rates are underestimated. The paper's 3.5/h (Extended Data Fig. 3b) also comes from a pups-present vs pups-removed comparison in 4 dyads, a different window from these 12-h recordings.
6. [affects a conclusion] Cell 15: "Virgin in rest" means different things across mice. The median dwell is 5–52 s in V110 and V111 but 800–2500 s in V116, where it lies inside "Virgin in nest" 13/13 times. label-link passes only on the pooled count. Nest-entry results are split the same way: 37/70 in V116 against 4/124 in V110 and V111.
7. [affects a conclusion] Cells 17–18: the nest-entry fraction depends almost entirely on the 40 s cap (42 with it, 2 without). The cap follows the Methods, so the outcome stands, but it is fragile.
8. [does not affect a conclusion] `fisher_vs_zero`: as in the paper, it compares against zero activated units, so any k ≥ 5 of about 100–200 is "significant". The paper's chance level is zero; the notebook's uncorrected positive rate (cell 18, 28.4%) is compared with "about 5%". By my simulation, the pipeline's real false-positive level after BH is about 0–2% for nest entry, but higher in the sparse case of problem 1.
9. [does not affect a conclusion] `shuffle_test` takes the p-value one-sided in the observed direction and then applies BH. This is effectively a two-sided test at 2q, as in the code.
10. [does not affect a conclusion] `_counts` counts both window edges, so a spike exactly at the episode start falls in both the 10 s baseline and the episode. I checked this on a synthetic train.
11. [does not affect a conclusion] `bh` matches statsmodels `fdr_bh` on 200 random inputs that include NaNs. `triggered_change` is defined but never used.

**C. Not checked, and the output that would have allowed it**

- Whether `unit_name` encodes OT-PVN identity or channel. Printing the unique `unit_name` values per session would settle this for ot-pvn-units.
- Annotation coverage. Printing, per session, the first and last annotation of any label and the largest gap between annotations would test the rate denominators (fig1j, ed8a).
- fig4i partial test. Per-animal mean retrieval-triggered photometry change in the obs files (`triggered_change`), and the retrieval-event times in the ROV40/ROV41 test files, would show which animals learned and give a partial learner-group test.
- fig2f. The modulation of the 3 shepherding-activated units during "Virgin Agressing" episodes, plus the per-session onset-time overlap between "Virgin Agressing" and "Mom agressing", would let me judge what the label means.
- Overlap between baseline windows and earlier episodes. A count of capped nest-entry baselines that overlap a preceding "Virgin in rest" or "Mom agressing" interval would show whether the baselines are contaminated.
- Whether the empty-episode exclusion drives the result. The number of real episodes dropped per unit, or the activated counts with empty episodes set to 0 in the real value too, would show this.
- Unit independence. Pairwise spike-train correlation, or coincidence per pair, among the 9 V111 03032018 retrieval-activated units would show whether they are separate neurons.
- Draft vs pinned version: only one file's content was compared (cell 13). I did not re-run anything and read no NWB content myself.

## End of run

16 turns, 4 minutes, result: success.
