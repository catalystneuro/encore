# 000350 · author · run 39026746060

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls entries claims attempts | head -50
```

```
# Protocol for an attempt

Version: `pilot-7`. Record this version in the attempt's provenance.

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

[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md; ls entries/001453-fouke-2025/ claims/001453/; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (57.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d2460b76-cf9f-4e58-a635-25e9dd1a3d2c/tool-results/b36nnev6p.txt

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

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md 2>/dev/null; ls entries/001453-fouke-2025/; ls targets | head; grep -rl 000350 targets tools | head
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 261 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d2460b76-cf9f-4e58-a635-25e9dd1a3d2c/tool-results/b36nnev6p.txt"
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
[... 1004 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000350/ | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/000350/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for v in 0.221219.1506 0.240822.1759; do echo "== $v"; curl -s "https://api.dandiarchive.org/api/dandisets/000350/versions/$v/assets/?page_size=100" | python -c "
import json,sys
d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'], a['path'], a['size'], a['modified'])
"; done; curl -s "https://api.dandiarchive.org/api/dandisets/000350/versions/0.240822.1759/" > meta.json; python -m json.tool meta.json | head -300
```

Result: the fetched text is not kept.

**Agent**

Dandiset 000350 holds 12 whole-brain light-sheet sessions, 150 to 940 GB each, so everything must be streamed selectively. Checking the rest of the metadata and opening one file.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import json;d=json.load(open('meta.json'))
for k in ['assetsSummary','relatedResource','ethicsApproval','wasGeneratedBy']: print(k, json.dumps(d.get(k),indent=1)[:3000])
"; python -c "import h5py, remfile, pynwb, dandi; print('ok')"; which uv
```

```
assetsSummary {
 "species": [
  {
   "name": "Danio rerio - Zebra fish",
   "schemaKey": "SpeciesType",
   "identifier": "http://purl.obolibrary.org/obo/NCBITaxon_7955"
  }
 ],
 "approach": [
  {
   "name": "microscopy approach; cell population imaging",
   "schemaKey": "ApproachType"
  }
 ],
 "schemaKey": "AssetsSummary",
 "dataStandard": [
  {
   "name": "Neurodata Without Borders (NWB)",
   "schemaKey": "StandardsType",
   "identifier": "RRID:SCR_015242"
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q h5py remfile pynwb dandi numpy scipy pandas matplotlib statsmodels 2>&1 | tail -2; python -c "import h5py,remfile;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > list.py <<'EOF'
import h5py, remfile, sys
url=f"https://api.dandiarchive.org/api/assets/{sys.argv[1]}/download/"
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print('D',name,obj.shape,obj.dtype,obj.chunks,dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else:
        print('G',name,dict((k,v) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
f.visititems(show)
EOF
time python list.py 4f898ff7-6084-4e84-a449-f05811c1d951 2>&1 | grep -v "^G specifications" | grep -v specifications | head -200
```

```
G acquisition {}
G acquisition/BaselineStimulusVelocitySignal {'comments': 'no comments', 'description': 'Raw signal for drift speed of visual grating presented to the subject.', 'neurodata_type': 'TimeSeries'}
D acquisition/BaselineStimulusVelocitySignal/data (27339900,) float64 (13350,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
D acquisition/BaselineStimulusVelocitySignal/starting_time () float64 None {'rate': np.float64(5989.6), 'unit': 'seconds'}
G acquisition/FrameCaptureTTLSignal {'comments': 'no comments', 'description': 'Raw synchronization signal detecting shutter activation for the optical physiology camera. Forms the basis of the timestamps for the TwoPhotonSeries and corresponding Fluorescence. Values of the TTL signal significantly above 3.5 indicate start of volume scan; values significantly close to 3.5 indicate the scan of a single plane.\n', 'neurodata_type': 'TimeSeries'}
D acquisition/FrameCaptureTTLSignal/data (27339900,) float64 (13350,) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
D acquisition/FrameCaptureTTLSignal/starting_time () float64 None {'rate': np.float64(5989.6), 'unit': 'seconds'}
G acquisition/NeuronOnePhotonSeries {'comments': 'no comments', 'description': 'Full resolution of images from whole-brain calcium imaging.', 'neurodata_type': 'TwoPhotonSeries'}
D acquisition/NeuronOnePhotonSeries/data (3065, 888, 2048, 29) int16 (1, 888, 2048, 1) {'conversion': np.float64(1.0), 'offset': np.float64(0.0), 'resolution': np.float64(-1.0), 'unit': 'a.u.'}
D acquisition/NeuronOnePhotonSeries/dimension (3,) int32 None {}
D acquisition/NeuronOnePhotonSeries/timestamps (3065,) float64 (1533,) {'interval': np.int64(1), 'unit': 'seconds'}
G acquisition/StimulusGainSignal {'comments': 'no comments', 'description': 'Raw signal tracking the gain of the visual stimulus.', 'neurodata_type': 'TimeSeries'}
D acquisition/StimulusG
[... 89 more lines not kept]
```

**Agent**

The file holds raw swim signals (6 kHz), swim intervals, activity states, and neuron ΔF/F for ~93k ROIs (12050 × 93344). No glia channel visible yet. Now fetching the paper.

**Agent calls Bash**

```bash
mkdir -p paper; curl -s "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.cell.2019.05.050&format=json&resultType=core" | python -c "
import json,sys;d=json.load(sys.stdin)
for r in d['resultList']['result']: print(r.get('pmid'),r.get('pmcid'),r.get('isOpenAccess'),r.get('inEPMC'),r.get('title'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -sL -A "Mozilla/5.0" -o els.html "https://www.cell.com/cell/fulltext/S0092-8674(19)30621-X" ; ls -la; grep -o "<title>[^<]*" els.html | head; curl -sL -A "Mozilla/5.0" -o bior.json "https://api.biorxiv.org/details/biorxiv/10.1101/510214"; head -c 1500 bior.json
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -s "https://api.unpaywall.org/v2/10.1016/j.cell.2019.05.050?email=[removed: an e-mail address]" | python -m json.tool | grep -E "url|is_oa|oa_status|license|host_type|version" | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -s -m 30 -w "%{http_code}\n" "https://api.unpaywall.org/v2/10.1016/j.cell.2019.05.050?email=[removed: an e-mail address]" | head -c 3000; echo; curl -s -m 30 "https://api.crossref.org/works/10.1016/j.cell.2019.05.050" | python -c "import json,sys;d=json.load(sys.stdin)['message'];print(d.get('license'));print([l['URL'] for l in d.get('link',[])])"
```

Result: the fetched text is not kept.

**Agent**

It is open access (CC BY-NC-ND). Fetching the full text.

**Agent calls Bash**

```bash
cd paper; curl -sL -m 60 -A "Mozilla/5.0" -o mu2019.pdf "http://www.cell.com/article/S009286741930621X/pdf"; file mu2019.pdf; curl -sL -m 60 -o mu2019.txt "https://api.elsevier.com/content/article/PII:S009286741930621X?httpAccept=text/plain"; wc -c mu2019.txt; head -c 1500 mu2019.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; for u in "https://api.elsevier.com/content/article/doi/10.1016/j.cell.2019.05.050?httpAccept=text/xml" "https://www.sciencedirect.com/science/article/pii/S009286741930621X" "https://pubmed.ncbi.nlm.nih.gov/31230713/"; do curl -sL -m 60 -A "Mozilla/5.0" -o t.out -w "%{http_code} " "$u"; wc -c t.out; head -c 300 t.out; echo; done
```

```
200 1931 t.out
<full-text-retrieval-response xmlns="http://www.elsevier.com/xml/svapi/article/dtd" xmlns:bk="http://www.elsevier.com/xml/bk/dtd" xmlns:cals="http://www.elsevier.com/xml/common/cals/dtd" xmlns:ce="http://www.elsevier.com/xml/common/dtd" xmlns:ja="http://www.elsevier.com/xml/ja/dtd" xmlns:mml="http:/
403 832804 t.out
<!DOCTYPE html>
<html lang='en-us'>
<head>
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" >
  <meta content="IE=edge" http-equiv="X-UA-Compatible" >
  <meta content="1" name="tdm-reservation" >
  <meta content="https://www.elsevier.com/tdm/tdmrep-policy.json" name="tdm-policy" 
203 5591 t.out
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>pubmed.ncbi.nlm.nih.gov</title>
  <style>
    html, body {
      min-height: 100%;
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o "STAR Methods\|futility-induced passivity\|Quantification and Statistical" t.out | sort | uniq -c; grep -o '<title>[^<]*' t.out
```

```
<title>pubmed.ncbi.nlm.nih.gov
```

**Agent calls Bash**

```bash
cd paper; curl -sL -m 60 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36" -H "Accept: text/html" -o sd.html -w "%{http_code}\n" "https://www.sciencedirect.com/science/article/pii/S009286741930621X"; grep -c "STAR" sd.html; grep -o "futil[a-z]*" sd.html | sort | uniq -c | head
```

Result: the fetched text is not kept.

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```

Result: no output.

**Agent calls WebSearch**

```json
{
 "query": "\"Glia Accumulate Evidence that Actions Are Futile\" pdf"
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; curl -sL -m 120 -A "Mozilla/5.0" -o mu2019.pdf "https://www.mulab.org/s/1_Mu_2019Cell-ysy2.pdf"; file mu2019.pdf; ls -la mu2019.pdf; rm -f t.out sd.html els.html bior.json mu2019.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; which pdftotext || (. $TMPDIR/env/bin/activate && uv pip install -q pypdf); (pdftotext -layout mu2019.pdf mu2019.txt 2>/dev/null) || ( . $TMPDIR/env/bin/activate && python -c "
import pypdf;r=pypdf.PdfReader('mu2019.pdf');open('mu2019.txt','w').write('\n\n=====PAGE=====\n'.join(p.extract_text() for p in r.pages))"); wc -l mu2019.txt; grep -n "Supplementa\|Supplemental Information" mu2019.txt | head
```

```
2207 mu2019.txt
1452:Supplemental Information can be found online at https://doi.org/10.1016/j.
```

**Agent calls Read**

```json
{
 "file_path": "paper/mu2019.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/mu2019.txt",
 "offset": 700,
 "limit": 760
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/mu2019.txt",
 "offset": 1460,
 "limit": 750
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/mu2019.txt",
 "offset": 1460,
 "limit": 380
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/mu2019.txt",
 "offset": 1840,
 "limit": 370
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, json, sys, numpy as np, requests
from concurrent.futures import ThreadPoolExecutor
V="0.240822.1759"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000350/versions/{V}/assets/?page_size=100").json()['results']
def s(x):
    v=x[()]
    return v.decode() if isinstance(v,bytes) else (str(v) if not hasattr(v,'shape') or v.shape==() else [i.decode() if isinstance(i,bytes) else i for i in v])
def probe(a):
    out={'path':a['path']}
    try:
        f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
        g=f['general']
        for k in ['session_description','experiment_description','lab','institution','experimenter','keywords','related_publications']:
            out[k]=s(g[k]) if k in g else s(f[k]) if k in f else None
        out['session_description']=s(f['session_description']); out['identifier']=s(f['identifier']); out['start']=s(f['session_start_time'])
        out['subject']={k:s(v) for k,v in g['subject'].items()}
        out['optophys']={}
        for ip,grp in g['optophysiology'].items():
            out['optophys'][ip]={k:(s(v) if isinstance(v,h5py.Dataset) else {kk:s(vv) for kk,vv in v.items()}) for k,v in grp.items()}
        out['acq']={k:(f['acquisition'][k]['data'].shape) for k in f['acquisition']}
        o=f['processing/ophys']
        out['ophys']={}
        for k in o:
            for k2 in o[k]:
                d=o[k][k2]
                out['ophys'][k+'/'+k2]={kk:(d[kk].shape if isinstance(d[kk],h5py.Dataset) else None) for kk in d}
                if 'timestamps' in d:
                    t=d['timestamps'][:]; out['ophys'][k+'/'+k2]['t']=[float(t[0]),float(t[-1]),float(np.median(np.diff(t)))]
                    out['ophys'][k+'/'+k2]['desc']=d.attrs.get('description')
        for k in f['acquisition']:
            if 'timestamps' in f['acquisition'][k]:
                t=f['acquisition'][k]['timestamps'][:]; out['acq_t_'+k]=[float(t[0]),float(t[-1]),float(np.median(np.diff(t))),len(t)]
        b=f['processing/behavior']
        st=[x.decode() if isinstance(x,bytes) else x for x in b['ActivityStates/state_type'][:]]
        out['states']={u:st.count(u) for u in set(st)}
        out['state_span']=[float(b['ActivityStates/start_time'][0]),float(b['ActivityStates/stop_time'][-1])]
        out['nswim']=b['SwimIntervals/start_time'].shape[0]
        out['burst']=[s(b['BurstEvents/label']), s(b['BurstEvents/event_description'])]
        out['beh_keys']=list(b.keys())
        out['rate']=float(f['acquisition/SwimSignals/starting_time'].attrs['rate']); out['t0']=float(f['acquisition/SwimSignals/starting_time'][()])
        out['stim_keys']=list(f['stimulus/presentation'].keys())+list(f['stimulus/templates'].keys())
        out['analysis']=list(f['analysis'].keys())
    except Exception as e:
        out['err']=repr(e)
    return out
with ThreadPoolExecutor(12) as ex:
    res=list(ex.map(probe,r))
json.dump(res,open('probe.json','w'),indent=1,default=str)
print(json.dumps(res,indent=1,default=str))
EOF
time python probe.py > probe.out 2>&1; tail -5 probe.out; wc -l probe.out
```

```
real	0m34.256s
user	0m2.480s
sys	0m0.261s
  "t0": 0.0,
  "stim_keys": [],
  "analysis": []
 }
]
2015 probe.out
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import json;R=json.load(open('probe.json'))
r=R[0]
for k in ['session_description','experiment_description','lab','institution','experimenter','keywords','related_publications','subject','optophys']: print(k,':',r[k])
print()
for r in R:
  print(r['path'], r.get('err'))
  print('  subj',r['subject']); print('  start',r['start'],'id',r['identifier'][:40])
  print('  sess',r['session_description'][:300])
  print('  opt',{k:(v.get('indicator'),v.get('location'),v.get('description')[:80] if v.get('description') else None,v.get('excitation_lambda')) for k,v in r['optophys'].items()})
  print('  acq',r['acq'], {k:v for k,v in r.items() if k.startswith('acq_t')})
  print('  ophys',r['ophys'])
  print('  states',r['states'],r['state_span'],'nswim',r['nswim'],'rate',r['rate'],r['burst'],r['beh_keys'])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 12, in <module>
    print('  ophys',r['ophys'])
                    ~^^^^^^^^^
KeyError: 'ophys'
session_description : A single-color optic channel recording of either a neuron or a glia population.
experiment_description : When a behavior repeatedly fails to achieve its goal, animals often give up and become passive, which can be strategic for preserving energy or regrouping between attempts. It is unknown how the brain identifies behavioral failures and mediates this behavioral-state switch. In larval zebrafish swimming in virtual reality, visual feedback can be withheld so that swim attempts fail to trigger expected visual flow. After tens of seconds of such motor futility, animals became passive for similar durations. Whole-brain calcium imaging revealed noradrenergic neurons that responded specifically to failed swim attempts and radial astrocytes whose calcium levels accumulated with increasing numbers of failed attempts. Using cell ablation and optogenetic or chemogenetic activation, we found that noradrenergic neurons progressively activated brainstem radial astrocytes, which then suppressed swimming. Thus, radial astrocytes perform a computation critical for behavior; they accumulate evidence that current actions are ineffective and consequently drive changes in behavioral states.

lab : Ahrens Lab
institution : Janelia Research Campus
experimenter : ['Mu, Yu', 'Bennett, Davis V.', 'Rubinov, Mikail', 'Narayan, Sujatha', 'Yang, Chao-Tsung', 'Tanimoto, Masashi', 'Mensh, Brett D.', 'Looger, Loren L.', 'Ahrens, Misha B.']
keywords : ['neuroscience', 'glia', 'astrocytes', 'norepinephrine', 'noradrenaline', 'learned helplessness', 'zebrafish', 'neuromodulation', 'behavioral states', 'evidence accumulation']
related_publications : ['https://doi.org/10.1016/j.cell.2019.05.050']
subject : {'age': 'P6D', 'description': 'Zebrafish in a virtual reality environment.', 'sex': 'U', 'species': 'Danio re
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import json;R=json.load(open('probe.json'))
for r in sorted(R,key=lambda r:r['path']):
  print(r['path'].split('/')[0], 'ERR' if r.get('err') else '')
  print('  subj',r['subject']['subject_id'],r['subject']['age'],'start',r['start'])
  print('  opt',{k:(v.get('indicator'),v.get('excitation_lambda'),{kk:vv for kk,vv in v.items() if isinstance(vv,dict) and vv}) for k,v in r['optophys'].items()})
  print('  acq',{k:v for k,v in r['acq'].items() if 'Series' in k}, 'nsamp',r['acq'].get('SwimSignals'))
  print('  ophys',r.get('ophys'))
  print('  states',r.get('states'),r.get('state_span'),'nswim',r.get('nswim'),'rate',r.get('rate'),r.get('burst'))
"
```

```
sub-20161022-1 ERR
  subj 20161022_1 P6D start 2016-10-22T15:10:03-04:00
  opt {'GliaVolume': ('GCaMP6f', '488.0', {'GliaOpticalChannel': {'description': 'Detection filter (Semrock).', 'emission_lambda': '537.5'}})}
  acq {'GliaOnePhotonSeries': [8650, 940, 2048, 31]} nsamp [20968915, 2]
  ophys None
  states None None nswim None rate None None
sub-20161109-2 
  subj 20161109_2 P6D start 2016-11-09T21:19:50-05:00
  opt {'GliaVolume': ('GCaMP6f', '561.0', {'GliaOpticalChannel': {'description': 'Detection filter (Chroma).', 'emission_lambda': '660.0'}}), 'NeuronVolume': ('GCaMP6f', '488.0', {'NeuronOpticalChannel': {'description': 'Detection filter (Semrock).', 'emission_lambda': '537.5'}})}
  acq {'GliaOnePhotonSeries': [12500, 1024, 2048, 24], 'NeuronOnePhotonSeries': [12500, 1024, 2048, 24]} nsamp [26633200, 2]
  ophys {'DfOverF/GliaDfOverF': {'data': [12500, 100840], 'rois': [100840], 'timestamps': [12500], 't': [0.005676505943635635, 4363.245625751302, 0.34910511553357537], 'desc': 'Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.'}, 'DfOverF/NeuronDfOverF': {'data': [12500, 109918], 'rois': [109918], 'timestamps': [12500], 't': [0.005676505943635635, 4363.245625751302, 0.34910511553357537], 'desc': 'Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.'}, 'Fluorescence/GliaFluorescence': {'data': [12500, 100840], 'rois': [100840], 'timestamps': [12500], 't': [0.005676505943635635, 4363.245625751302, 0.34910511553357537], 'desc': 'Segmented regions of interest (ROIs) and detrended activity for the glia indicator type.'}, 'Fluorescence/NeuronFluorescence': {'data': [12500, 109918], 'rois': [109918], 'timestamps': [12500], 't': [0.005676505943635635, 4363.245625751302, 0.34910511553357537], 'desc': 'Segmented regions of interest (ROIs) and detrended activity for the neuron indicator type.'}, 'VolumeSegmentation/GliaVolumeSegmentation': {'id': [100840], 'imaging_plane': None, 'reference_ima
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p2.py <<'EOF'
import h5py, remfile, numpy as np, time
from concurrent.futures import ThreadPoolExecutor
ids={'20161022-1':'8fc5cb83-a88f-4455-992e-308c27360cd2','20161206-1':'05c64266-4424-4b8b-813f-4b292852480f','20161206-2':'2fc82995-03de-40cb-9657-67fd24d51cf7','20170111-1':'ee89e7b9-d3d0-444e-b8ca-1ef0ab3c0d98'}
def op(a): return h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a}/download/"),'r')
def p(kv):
    k,a=kv; f=op(a); return k, list(f.keys()), list(f['processing'].keys()) if 'processing' in f else None, list(f['acquisition'].keys()), {kk:f['acquisition'][kk]['timestamps'].shape for kk in f['acquisition'] if 'timestamps' in f['acquisition'][kk]}
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(p, ids.items()): print(r)
f=op('4f898ff7-6084-4e84-a449-f05811c1d951')
t=time.time(); g=f['acquisition/StimulusGainSignal/data'][:]; print('gain read s',time.time()-t, g.nbytes/1e6,'MB')
fs=5989.6
gd=g[::int(fs)]
print('unique gain (rounded)', np.unique(np.round(g[::600],3), return_counts=True))
# segments
ch=np.flatnonzero(np.diff(np.round(gd,3))!=0)
print('change seconds', ch[:50], len(ch))
b=f['processing/behavior']
st=b['ActivityStates/start_time'][:]; sp=b['ActivityStates/stop_time'][:]; ty=[x.decode() if isinstance(x,bytes) else x for x in b['ActivityStates/state_type'][:]]
for i in range(15): print(round(st[i],2),round(sp[i],2),ty[i], round(sp[i]-st[i],2))
s0=b['SwimIntervals/start_time'][:]; s1=b['SwimIntervals/stop_time'][:]; pw=b['SwimIntervals/power'][:]; w=b['SwimIntervals/width'][:]
print('swims', s0[:10], s1[:10]-s0[:10], pw[:10], w[:10])
print('swim range', s0.min(), s0.max(), np.percentile(s1-s0,[5,50,95]), np.percentile(pw,[5,50,95]), np.percentile(w,[5,50,95]))
be=b['BurstEvents/event_times'][:]; print('bursts', be[:10], len(be))
for k in ['BaselineStimulusVelocitySignal','StimulusTypeSignal','TotalStimulusVelocitySignal']:
    x=f[f'acquisition/{k}/data'][:int(fs*1200):600]; print(k, np.unique(np.round(x,2))[:20], x.min(), x.max())
x=f['acquisition/StimulusParameterSignals/data'][:int(fs*1200):600,:]; print('param', [np.unique(np.round(x[:,j],2))[:10] for j in range(3)])
EOF
time python p2.py
```

```
('20161022-1', ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], ['behavior'], ['BaselineStimulusVelocitySignal', 'FrameCaptureTTLSignal', 'GliaOnePhotonSeries', 'StimulusGainSignal', 'StimulusParameterSignals', 'StimulusTypeSignal', 'SwimSignals', 'TotalStimulusVelocitySignal'], {'GliaOnePhotonSeries': (8650,)})
('20161206-1', ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], ['behavior'], ['BaselineStimulusVelocitySignal', 'FrameCaptureTTLSignal', 'GliaOnePhotonSeries', 'StimulusGainSignal', 'StimulusParameterSignals', 'StimulusTypeSignal', 'SwimSignals', 'TotalStimulusVelocitySignal'], {'GliaOnePhotonSeries': (9000,)})
('20161206-2', ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], ['behavior'], ['BaselineStimulusVelocitySignal', 'FrameCaptureTTLSignal', 'GliaOnePhotonSeries', 'StimulusGainSignal', 'StimulusParameterSignals', 'StimulusTypeSignal', 'SwimSignals', 'TotalStimulusVelocitySignal'], {'GliaOnePhotonSeries': (8499,)})
('20170111-1', ['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'], ['behavior'], ['BaselineStimulusVelocitySignal', 'FrameCaptureTTLSignal', 'NeuronOnePhotonSeries', 'StimulusGainSignal', 'StimulusParameterSignals', 'StimulusTypeSignal', 'SwimSignals', 'TotalStimulusVelocitySignal'], {'NeuronOnePhotonSeries': (10050,)})
gain read s 0.969653844833374 218.7192 MB
unique gain (rounded) (array([0.   , 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008,
       0.009, 0.01 , 0.011, 0.01
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p3.py <<'EOF'
import h5py, remfile, numpy as np, json, requests
from concurrent.futures import ThreadPoolExecutor
V="0.240822.1759"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000350/versions/{V}/assets/?page_size=100").json()['results']
fs=5989.6
def rle(x):
    out=[];i=0
    while i<len(x):
        j=i
        while j<len(x) and x[j]==x[i]: j+=1
        out.append((x[i],i,j-i)); i=j
    return out
def p(a):
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    A=f['acquisition']; n=A['StimulusGainSignal/data'].shape[0]
    step=int(round(fs/2))
    g=A['StimulusGainSignal/data'][:][::step]; v=A['BaselineStimulusVelocitySignal/data'][:][::step]
    ty=A['StimulusTypeSignal/data'][:][::step]; pr=A['StimulusParameterSignals/data'][:][::step]
    np.savez(f"prot_{a['path'].split('/')[0]}.npz",g=g,v=v,ty=ty,pr=pr)
    lab=[f"g{gg:.3f}|v{vv:.1f}|p{int(p0)}" for gg,vv,p0 in zip(g,v,pr[:,0])]
    return a['path'].split('/')[0], n/fs, rle(lab)
with ThreadPoolExecutor(6) as ex:
    for name,dur,rl in ex.map(p,r):
        print('==',name,'dur s',round(dur,1),'segments',len(rl))
        # merge print: show first 60 segments with t in s
        print('  ', ' '.join(f"{l}@{s/2:.0f}+{d/2:.0f}" for l,s,d in rl[:70]))
EOF
time python p3.py 2>&1 | cut -c1-3000
```

```
== sub-20161022-1 dur s 3500.9 segments 150
   g0.012|v1.0|p22@0+24 g0.036|v1.0|p23@24+24 g0.012|v1.0|p22@49+24 g0.036|v1.0|p23@73+24 g0.012|v1.0|p22@98+24 g0.036|v1.0|p23@122+24 g0.012|v1.0|p22@146+24 g0.036|v1.0|p23@170+24 g0.012|v1.0|p22@194+24 g0.036|v1.0|p23@218+24 g0.012|v1.0|p22@243+24 g0.036|v1.0|p23@268+24 g0.012|v1.0|p22@292+24 g0.036|v1.0|p23@316+24 g0.012|v1.0|p22@340+21 g0.000|v0.5|p32@361+3 g0.000|v1.0|p33@364+0 g0.000|v0.5|p32@364+40 g0.000|v1.0|p33@404+0 g0.000|v0.5|p32@405+40 g0.000|v1.0|p33@445+0 g0.000|v0.5|p32@446+40 g0.000|v1.0|p32@486+0 g0.000|v0.5|p32@486+120 g0.000|v1.0|p33@606+0 g0.000|v0.5|p32@607+40 g0.000|v1.0|p33@647+0 g0.000|v0.5|p32@648+40 g0.000|v1.0|p33@688+0 g0.000|v0.5|p32@688+40 g0.000|v1.0|p33@728+0 g0.000|v0.5|p32@728+40 g0.000|v1.0|p33@768+0 g0.000|v0.5|p32@769+40 g0.000|v1.0|p33@809+0 g0.000|v0.5|p32@810+40 g0.000|v1.0|p33@850+0 g0.000|v0.5|p32@850+40 g0.000|v1.0|p33@890+0 g0.000|v0.5|p32@890+40 g0.000|v1.0|p33@930+0 g0.000|v0.5|p32@931+40 g0.000|v1.0|p32@971+0 g0.000|v0.5|p32@972+120 g0.000|v1.0|p33@1092+0 g0.000|v0.5|p32@1092+40 g0.000|v1.0|p33@1132+0 g0.000|v0.5|p32@1133+40 g0.000|v1.0|p33@1173+0 g0.000|v0.5|p32@1174+40 g0.000|v1.0|p33@1214+0 g0.000|v0.5|p32@1214+40 g0.000|v1.0|p33@1254+0 g0.000|v0.5|p32@1254+40 g0.000|v1.0|p33@1294+0 g0.000|v0.5|p32@1295+40 g0.000|v1.0|p33@1335+0 g0.000|v0.5|p32@1336+40 g0.000|v1.0|p33@1376+0 g0.000|v0.5|p32@1376+40 g0.000|v1.0|p33@1416+0 g0.000|v0.5|p32@1416+120 g0.000|v1.0|p33@1537+0 g0.000|v0.5|p32@1538+40 g0.000|v1.0|p33@1578+0 g0.000|v0.5|p32@1578+40 g0.000|v1.0|p33@1618+0 g0.000|v0.5|p32@1618+40 g0.000|v1.0|p33@1658+0 g0.000|v0.5|p32@1659+40
== sub-20161206-2 dur s 3281.9 segments 183
   g0.000|v0.5|p32@0+0 g0.020|v1.0|p22@0+15 g0.020|v0.0|p23@16+12 g0.020|v1.0|p22@27+16 g0.020|v0.0|p23@42+12 g0.020|v1.0|p22@54+16 g0.020|v0.0|p23@70+12 g0.020|v1.0|p22@81+16 g0.020|v0.0|p23@96+12 g0.020|v1.0|p22@108+16 g0.020|v0.0|p23@124+12 g0.020|v1.0|p22@135+16 g0.020|v0.0|p23@150+12 g0.020|v1.0|p2
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/mikarubi/segmentation seg && cd seg && git log -1 --format="%H %ad" && ls -R | head -50
```

```
18ae157e1961b4e2c3f75c7212723b19bceebeff Mon Oct 12 22:16:55 2026 -0500
.:
Dockerfile
LICENSE
README-docker.md
README.md
app
docs
iac
pyproject.toml
requirements-docker.txt
requirements.txt
src
tests

./app:
__init__.py
app.py

./docs:
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p4.py <<'EOF'
import h5py, remfile, numpy as np, time
f=h5py.File(remfile.File("https://api.dandiarchive.org/api/assets/4f898ff7-6084-4e84-a449-f05811c1d951/download/"),'r')
d=f['processing/ophys/DfOverF/NeuronDfOverF/data']; F=f['processing/ophys/Fluorescence/NeuronFluorescence/data']
print(d.shape,d.chunks, d.compression, d.id.get_storage_size()/1e9)
t=time.time(); x=d[:, :931*4]; print('read 4 colblocks s', time.time()-t, x.nbytes/1e6)
y=F[:, :931]; print('fluor==dff', np.array_equal(x[:,:931],y), np.nanmax(np.abs(x[:,:931]-y)))
print('dff pct', np.nanpercentile(x,[0,1,5,50,95,99,100]), np.isnan(x).mean())
m=x.mean(1); print('mean trace pct', np.percentile(m,[0,5,50,95,100]))
print('first rows', x[:3,:5])
ts=f['processing/ophys/DfOverF/NeuronDfOverF/timestamps'][:]; print(ts[:5], np.diff(ts)[:5], ts[-3:])
rt=f['acquisition/NeuronOnePhotonSeries/timestamps'][:]; print('raw ts', rt[:5], rt[-3:], len(rt))
print(dict(f['acquisition/NeuronOnePhotonSeries'].attrs), f['acquisition/NeuronOnePhotonSeries/dimension'][:])
vm=f['processing/ophys/VolumeSegmentation/NeuronVolumeSegmentation/voxel_mask'][:2000]; print(vm[:5], vm['x'].max(),vm['y'].max(),vm['z'].max())
EOF
time python p4.py
```

```
(12050, 93344) (133, 931) gzip 8.092296943
read 4 colblocks s 24.62609577178955 358.9936
fluor==dff False 2.0554278562830026
dff pct [0.484414   0.88350182 0.94738905 0.99637991 1.05573364 1.17750254
 5.36951909] 0.0
mean trace pct [0.97720009 0.98442798 0.9967667  1.02674452 1.07041957]
first rows [[0.97717603 0.98146889 0.99313278 1.00290315 0.98436551]
 [0.9713291  0.97820905 0.99089544 0.99757041 0.98373075]
 [0.97422308 0.97971234 0.98510561 0.99420804 0.98726453]]
[0.00534259 0.37164418 0.73811273 1.10458127 1.47088286] [0.36630159 0.36646855 0.36646855 0.36630159 0.36646855] [4413.92246561 4414.2887672  4414.65523574]
raw ts [3292.03202217 3292.39832376 3292.76479231 3293.1310939  3293.49756244] [4413.92246561 4414.2887672  4414.65523574] 3065
{'comments': 'no comments', 'description': 'Full resolution of images from whole-brain calcium imaging.', 'namespace': 'core', 'neurodata_type': 'TwoPhotonSeries', 'object_id': '00164978-ae7c-4a5b-b498-a483042cb0f9'} [2048  888   29]
[(206, 383, 10, 1.) (207, 384, 10, 1.) (208, 383, 10, 1.)
 (209, 382, 10, 1.) (209, 384, 10, 1.)] 233 388 20

real	1m12.002s
user	0m5.376s
sys	0m1.190s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/seg && nproc && cat README.md | head -60 && ls src/* && git log --format="%h %ad %s" --date=short | tail -5 && git log --format="%h %ad %s" --date=short --before=2019-07-01 | head -5
```

```
4
# Volumetric Segmentation Pipeline

Reference: [DOI: 10.1016/j.cell.2019.05.050](https://doi.org/10.1016/j.cell.2019.05.050)

Mu Y*, Bennett DV*, Rubinov M*, Narayan S, Yang CT, Tanimoto M, Mensh BD, Looger LL, Ahrens MB.

Glia accumulate evidence that actions are futile and suppress unsuccessful behavior. Cell 2019 178:27-43.

Contact: Mika Rubinov, `mika.rubinov at vanderbilt.edu`

## Run from Docker Container

Instructions [here](https://github.com/mikarubi/voluseg/blob/master/README-docker.md).

## Dependencies

- `h5py`, `dask`, `scipy`, `scikit-image`, `scikit-learn`, `matplotlib`, `nibabel`, `requests`, `numpy`, `pandas`, `pydantic>=2.8.0`, `pynwb`, `tifffile`
- Advanced Normalization Tools (ANTs) for registration (can install via conda)

[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/seg && git checkout -q 54d1907 && git rev-parse HEAD && ls -R | grep -v "^$" | head -40 && grep -rn "percentile\|baseline\|offset\|dff\|cell_timeseries\|Cell_timeseries" --include=*.py . | head -60
```

```
54d1907b1d911ad6445428f8a79ca44875ed42b1
.:
LICENSE
README.md
z0_preliminaries.py
z1_alignment.py
z2_brain_mask.py
z3_cell_detect.py
z4_cell_collect.py
z5_cell_clean.py
z6_components.py
z__main.py
z__parameters.py
zfun.py
zfun_cell.py
./zfun.py:51:def detrend_dynamic_baseline(timesers, poly_ordr=2):
./zfun.py:52:    '''estimation of dynamic baseline for input timeseries'''
./zfun.py:55:    # baseline_tau:  timescale constant for baseline estimation (in seconds)
./zfun.py:62:    # length of interval of dynamic baseline time-scales
./zfun.py:63:    ltau = (np.round(baseline_tau * freq_stack / 2) * 2 + 1).astype(int)
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/seg && sed -n 1,80p z6_components.py && sed -n 40,100p zfun.py && cat z__parameters.py | sed -n 1,80p && sed -n 100,150p z5_cell_clean.py
```

```
def z6():
    global brain_mask, censor_tau
    os.environ['MKL_NUM_THREADS'] = str(multiprocessing.cpu_count())
        
    if nmf_algorithm:
        for frame_i in range(imageframe_nmbr):
            if os.path.isfile(output_dir + 'Cells' + str(frame_i) + '_clust.hdf5'):
                if batch_mode:
                    continue
                else:
                    try:
                        cell_reset = eval(input('Reset cell clustering? [0, no]; 1, yes. '))
                    except SyntaxError:
                        cell_reset = 0
                    
                    if not cell_reset:
                        continue
            
            with h5py.File(output_dir + 'Cells' + str(frame_i) + '_clean.hdf5', 'r') as file_handle:
                Cell_timesers1 = file_handle['Cell_timesers1'][()].astype(float)
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p5.py <<'EOF'
import h5py, remfile, numpy as np, requests, json
from concurrent.futures import ThreadPoolExecutor
f=h5py.File(remfile.File("https://api.dandiarchive.org/api/assets/4f898ff7-6084-4e84-a449-f05811c1d951/download/"),'r')
x=f['processing/ophys/DfOverF/NeuronDfOverF/data'][:,:200]; y=f['processing/ophys/Fluorescence/NeuronFluorescence/data'][:,:200]
print('F pct',np.percentile(y,[0,1,50,99,100]))
print('dff mean per roi',np.percentile(x.mean(0),[0,50,100]))
r=x/(y/y.mean(0)); print('ratio dff/(F/meanF)', np.percentile(r,[1,50,99]))
for k in [0,1,2]:
    print(k, np.corrcoef(x[:,k],y[:,k])[0,1], x[:3,k], y[:3,k])
# versions
def meta(v):
    r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000350/versions/{v}/assets/?page_size=100").json()['results']
    return {a['path']:a for a in r}
A=meta('0.221219.1506'); B=meta('0.240822.1759')
def info(a):
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    out={}
    def s(v):
        v=v[()]; return v.decode() if isinstance(v,bytes) else str(v)
    out['subject']={k:s(v) for k,v in f['general/subject'].items()}
    out['opt']={ip:{k:(s(v) if isinstance(v,h5py.Dataset) else None) for k,v in g.items()} for ip,g in f['general/optophysiology'].items()}
    out['sess']=s(f['session_description']); out['start']=s(f['session_start_time'])
    def walk(name,obj):
        if isinstance(obj,h5py.Dataset) and not name.startswith('specifications'): out[name]=(obj.shape,str(obj.dtype))
    for g in ['processing','acquisition']: f[g].visititems(lambda n,o: walk(g+'/'+n,o))
    b=f['processing/behavior']
    out['st_sum']=float(b['ActivityStates/start_time'][:].sum()) if 'ActivityStates' in b else None
    out['sw_sum']=float(b['SwimIntervals/start_time'][:].sum()) if 'SwimIntervals' in b else None
    return out
def comp(p):
    a=info(A[p]); b=info(B[p])
    diffs={k:(a.get(k),b.get(k)) for k in set(a)|set(b) if a.get(k)!=b.get(k)}
    return p, A[p]['size'], B[p]['size'], diffs
with ThreadPoolExecutor(6) as ex:
    for p,sa,sb,d in ex.map(comp, sorted(B)):
        print(p.split('/')[0], sa-sb, json.dumps(d,default=str)[:1500])
EOF
time python p5.py
```

```
Exit code 143
Command timed out after 1h 0m 0s
```

**Agent**

That hung on recursive listing of 24 remote files and lost an hour. Redoing it with only targeted fields and a hard timeout.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p5.py <<'EOF'
import h5py, remfile, numpy as np, requests, json
from concurrent.futures import ThreadPoolExecutor
f=h5py.File(remfile.File("https://api.dandiarchive.org/api/assets/4f898ff7-6084-4e84-a449-f05811c1d951/download/"),'r')
x=f['processing/ophys/DfOverF/NeuronDfOverF/data'][:,:200]; y=f['processing/ophys/Fluorescence/NeuronFluorescence/data'][:,:200]
print('F pct',np.percentile(y,[0,1,50,99,100]))
print('dff mean per roi',np.percentile(x.mean(0),[0,50,100]))
for k in [0,1,2]:
    print(k, np.corrcoef(x[:,k],y[:,k])[0,1], x[:3,k], y[:3,k])
EOF
timeout 600 python -u p5.py
```

```
F pct [0.66869062 0.76007634 0.91762107 0.99082005 1.0081983 ]
dff mean per roi [1. 1. 1.]
0 0.6529201538187528 [0.97717603 0.9713291  0.97422308] [0.96764855 0.96764917 0.96764979]
1 0.4619731292244559 [0.98146889 0.97820905 0.97971234] [0.97704945 0.97705018 0.97705091]
2 0.8762656728137909 [0.99313278 0.99089544 0.98510561] [0.98505809 0.9850551  0.98505212]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p6.py <<'EOF'
import h5py, remfile, numpy as np, requests, json
from concurrent.futures import ThreadPoolExecutor
def meta(v):
    r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000350/versions/{v}/assets/?page_size=100").json()['results']
    return {a['path']:a for a in r}
A=meta('0.221219.1506'); B=meta('0.240822.1759')
def s(v):
    v=v[()]; return v.decode() if isinstance(v,bytes) else str(v)
def info(a):
    f=h5py.File(remfile.File(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"),'r')
    out={'subject':{k:s(v) for k,v in f['general/subject'].items()},
         'opt':{ip:{k:s(v) for k,v in g.items() if isinstance(v,h5py.Dataset)} for ip,g in f['general/optophysiology'].items()},
         'start':s(f['session_start_time']),'acq':sorted(f['acquisition'].keys()),
         'proc':{m:sorted(f['processing'][m].keys()) for m in f['processing']}}
    b=f['processing/behavior']
    for t in ['ActivityStates','SwimIntervals']:
        if t in b: out[t]=[b[t+'/start_time'].shape[0], float(b[t+'/start_time'][:].sum()), list(b[t].attrs.get('colnames'))]
    if 'ophys' in f['processing']:
        for k in f['processing/ophys/DfOverF']:
            d=f['processing/ophys/DfOverF'][k]; out[k]=[d['data'].shape, float(d['timestamps'][:].sum()), float(d['data'][100,:50].sum())]
    out['ttl']=float(f['acquisition/FrameCaptureTTLSignal/data'][:100000].sum())
    return out
def comp(p):
    a=info(A[p]); b=info(B[p])
    return p, A[p]['size']-B[p]['size'], {k:(a.get(k),b.get(k)) for k in set(a)|set(b) if a.get(k)!=b.get(k)}
with ThreadPoolExecutor(12) as ex:
    for p,ds,d in ex.map(comp, sorted(B)):
        print(p.split('/')[0], ds, json.dumps(d,default=str)[:800], flush=True)
EOF
timeout 900 python -u p6.py
```

```
sub-20161022-1 5728 {"acq": [["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal", "TwoPhotonSeries"], ["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "GliaOnePhotonSeries", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal"]], "opt": [{"NeuronVolume": {"description": "Whole-brain optical imaging for the neuron filter.", "excitation_lambda": "488.0", "indicator": "GCaMP6f", "location": "whole-brain", "reference_frame": "dorsal"}}, {"GliaVolume": {"description": "Whole-brain optical imaging.", "excitation_lambda": "488.0", "indicator": "GCaMP6f", "location": "whole-brain"}}]}
sub-20161109-2 -352 {"acq": [["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "GliaTwoPhotonSeries", "NeuronTwoPhotonSeries", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal"], ["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "GliaOnePhotonSeries", "NeuronOnePhotonSeries", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal"]]}
sub-20161206-1 5744 {"acq": [["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal", "TwoPhotonSeries"], ["BaselineStimulusVelocitySignal", "FrameCaptureTTLSignal", "GliaOnePhotonSeries", "StimulusGainSignal", "StimulusParameterSignals", "StimulusTypeSignal", "SwimSignals", "TotalStimulusVelocitySignal"]], "opt": [{"NeuronVolume": {"description": "Whole-brain optical imaging for the neuron filter.", "excitation_lambda": "488.0", "indicator": "GCaMP6f", "location": "whole-brain", "reference_frame": "dorsal"}}, {"GliaVolume": {"description": "Whole-brain optical imaging.", "excitation_lambda": "488.0", "i
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import numpy as np,glob
for fn in sorted(glob.glob('prot_*.npz')):
    d=np.load(fn); g=d['g'];v=d['v'];p=d['pr'][:,0]
    cl=g>1e-4
    out={'CLmove':(cl&(v>0)).sum()/2,'CLstat':(cl&(v==0)).sum()/2,'OLmove':(~cl&(v>0)).sum()/2,'OLstat':(~cl&(v==0)).sum()/2}
    codes={int(c):int((p==c).sum()/2) for c in np.unique(p)}
    # contiguous OL moving segments lengths
    m=(~cl&(v>0)).astype(int); e=np.flatnonzero(np.diff(np.r_[0,m,0])); L=(e[1::2]-e[::2])/2
    print(fn[5:-4], out, codes, 'OLseg n',len(L),'median',np.median(L) if len(L) else 0,'max',L.max() if len(L) else 0, 'velvals',np.unique(v))
"
```

```
sub-20161022-1 {'CLmove': np.float64(531.5), 'CLstat': np.float64(190.0), 'OLmove': np.float64(2779.5), 'OLstat': np.float64(0.0)} {22: 361, 23: 360, 32: 2752, 33: 27} OLseg n 2 median 1389.75 max 1803.0 velvals [0.  0.5 1. ]
sub-20161109-2 {'CLmove': np.float64(666.0), 'CLstat': np.float64(145.5), 'OLmove': np.float64(3351.5), 'OLstat': np.float64(283.5)} {22: 698, 23: 688, 32: 3031, 33: 29} OLseg n 32 median 10.5 max 1566.5 velvals [0.  0.5 1.  2. ]
sub-20161206-1 {'CLmove': np.float64(829.5), 'CLstat': np.float64(611.5), 'OLmove': np.float64(2296.0), 'OLstat': np.float64(0.0)} {22: 828, 23: 612, 32: 2273, 33: 22} OLseg n 2 median 1148.0 max 1394.5 velvals [0.  0.5 1. ]
sub-20161206-2 {'CLmove': np.float64(753.5), 'CLstat': np.float64(545.0), 'OLmove': np.float64(1983.5), 'OLstat': np.float64(0.0)} {22: 753, 23: 545, 32: 1965, 33: 18} OLseg n 3 median 961.5 max 1021.5 velvals [0.  0.5 1.  1.5]
sub-20170111-1 {'CLmove': np.float64(1360.5), 'CLstat': np.float64(0.0), 'OLmove': np.float64(2511.0), 'OLstat': np.float64(0.0)} {22: 92, 23: 88, 32: 1008, 33: 13, 51: 1180, 53: 1489} OLseg n 19 median 84.5 max 1022.0 velvals [0.5 1.  1.5]
sub-20170113-2 {'CLmove': np.float64(865.5), 'CLstat': np.float64(0.0), 'OLmove': np.float64(3990.0), 'OLstat': np.float64(0.0)} {22: 286, 23: 315, 32: 2392, 33: 12, 51: 264, 53: 1586} OLseg n 14 median 124.5 max 1311.5 velvals [0.5 1.  1.5]
sub-20170113-3 {'CLmove': np.float64(1041.0), 'CLstat': np.float64(0.0), 'OLmove': np.float64(2571.0), 'OLstat': np.float64(0.0)} {22: 212, 23: 209, 32: 1373, 33: 14, 51: 619, 53: 1183} OLseg n 19 median 73.5 max 1021.5 velvals [0.5 1.  1.5]
sub-20170113-4 {'CLmove': np.float64(1945.0), 'CLstat': np.float64(0.0), 'OLmove': np.float64(2619.5), 'OLstat': np.float64(0.0)} {22: 191, 23: 182, 32: 1057, 33: 8, 51: 1056, 52: 515, 53: 1554} OLseg n 31 median 37.0 max 906.0 velvals [0.5 1.  1.5]
sub-20170127-1 {'CLmove': np.float64(1774.5), 'CLstat': np.float64(728.5), 'OLmove': np.float64(1502.5), 'OLstat': n
[... 4 more lines not kept]
```

**Agent**

I have enough of the data check to write the criteria before running any claim's analysis. Writing the claims file now.

**Agent calls Bash**

```bash
sed -n 1,80p entries/001453-fouke-2025/omr.py; python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1500]); print('-----')
print(len(nb['cells']))
EOF
ls schemas tools; sed -n 1,60p schemas/claims.schema.json 2>/dev/null | head -80
```

```
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
- The names of the stimulus codes combine the protocol file sevenrep_twentyonestim.hdf of the
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "def \|install\|sanity\|claim:\|Result\|embedded\|tag" tools/entry.py | head -80; python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][-4:]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:800]); print('-----')
EOF
```

```
20:- each notebook has a cell tagged `sanity` that prints what was loaded;
25:notebook through a Jupyter kernel installed in that environment, in the entry
32:markdown cell that begins "**Result:" and everything from the "## Summary"
59:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
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
252:            tag = outcome.get("output")
253:            if notebook in present and tag:
255:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
256:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
260:def _derivation_checks(report: Report, where, code: str) -> None:
274:def lock(entry_dir: Path) -> int:
[... 53 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000350/10.1016-j.cell.2019.05.050.yaml",
 "content": "# Claims for Mu, Bennett, Rubinov et al. (2019), Cell 178, 27-43, on dandiset 000350.\n# Source: the full text (open access, CC BY-NC-ND), main text and STAR Methods, read from the PDF\n# posted on the first author's lab site. The Supplemental Information (Figures S1 to S6, Tables S1\n# to S3, videos) was not read.\n#\n# When these criteria were written, the author had seen the data check only: the file list and\n# metadata, the groups and table columns of every file, the imaging plane metadata, the shapes and\n# timestamps of the imaging series, the counts of rows in each ActivityStates table and the first\n# 15 rows of one, percentiles of swim duration and power in one file, the values of the DfOverF\n# series in 200 to 3724 ROIs of one file, and the time each fish spends in each stimulus condition\n# (gain above or at zero, grating moving or stationary). No claim's analysis had been run.\n#\n# The dandiset holds 12 light-sheet sessions with fictive swimming in virtual reality: 4 with\n# neurons and radial astrocytes imaged together (two colours), 4 with neurons only and processed\n# cell traces, 1 with neurons only and raw images only, and 3 with radial astrocytes only and raw\n# images only. All 12 hold the swim signals, swim bouts and stimulus signals. None of the\n# perturbation experiments (Figures 4 to 7) is in it.\n#\n# Choices fixed here for all claims, where the Methods leave them open:\n# - Closed loop is time when the stimulus gain signal is above 0 and the grating moves (baseline\n#   velocity signal above 0); open loop is time when the gain is 0 and the grating moves (Methods:\n#   \"In open loop, the gain was zero\"). Periods of stationary grating are left out of both.\n# - Swim bouts are the rows of SwimIntervals. A passive epoch is a gap of 5 s or more between the\n#   end of one bout and the start of the next; an active epoch is a chain of bouts separated by\n#   gaps under 5 s whose first start and last end are more than 5 s apart (Methods). Epochs are\n#   taken within one continuous closed- or open-loop period, and those cut by its edges are left\n#   out. Passivity onset is the end of the last bout of an active epoch that is followed by a\n#   passive epoch in open loop.\n# - The whole-brain signal of a cell type is the mean over ROIs of the DfOverF series, from a\n#   fixed, evenly spaced subset of ROI blocks (the full tables are 6 to 10 GB each). The series\n#   is each ROI's trace divided by its mean (see the data check), so changes are in units of that\n#   mean.\n# - Each fish's value is the mean over its epochs or events; group statistics are over fish.\n# - Tolerances for values given as mean and SEM are 1.96 times the SEM (the 95% interval of the\n#   mean); the paper states \"Error bars, SEM in all figures\".\nschema_version: 1\ndandiset: \"000350\"\npaper: doi:10.1016/j.cell.2019.05.050\nclaims:\n- id: fig1h-epoch-durations\n  statement: In prolonged open loop, fish cycle between passive epochs lasting 24.4 +/- 2.5 s and\n    active epochs lasting 36.1 +/- 4.2 s (mean +/- SEM, n = 74 fish), swimming 29 +/- 6 times per\n    active epoch.\n  source: Figure 1H; Results, first section; STAR Methods, Futility-induced passivity behavioral\n    analysis\n  expected:\n  - quantity: Mean duration of passive epochs\n    value: 24.4\n    tolerance: 4.9\n    unit: s\n  - quantity: Mean duration of active epochs\n    value: 36.1\n    tolerance: 8.2\n    unit: s\n  - quantity: Swim bouts per active epoch\n    value: 29\n    tolerance: 11.8\n    unit: bouts\n  criterion: The mean over fish of each fish's mean, in open loop. Readings, listed before the\n    analysis; (a) epochs built from SwimIntervals by the Methods' rule; (b) the active and passive\n    rows of the dandiset's ActivityStates table, over the whole recording, as the table does not\n    say which condition they belong to; (c) as (a), with all epochs pooled over fish. Reproduced\n    when, under one reading, all three values are within tolerance; partially reproduced when\n    two are. The 12 fish here are a subset of the paper's 74.\n- id: methods-isi\n  statement: In closed loop fish swim in discrete bouts about once per second (inter-swim interval\n    1.2 +/- 0.05 s, n = 74), and within active epochs of open loop the interval is 1.19 +/- 0.047 s\n    against 24.4 s in passive epochs.\n  source: STAR Methods, Futility-induced passivity behavioral analysis\n  expected:\n  - quantity: Inter-swim interval in closed loop\n    value: 1.2\n    tolerance: 0.098\n    unit: s\n  - quantity: Inter-swim interval in active epochs of open loop\n    value: 1.19\n    tolerance: 0.092\n    unit: s\n  criterion: Per fish the mean interval between successive bouts, then the mean over fish. The\n    interval can be read as (a) start to start of successive bouts, or (b) end of one bout to the\n    start of the next; and in closed loop as (i) intervals under 5 s, or (ii) all intervals.\n    Reproduced when both values are within tolerance under one reading; partially reproduced\n    when one is.\n- id: fig1j-open-loop-passivity\n  statement: Fish spend much more time in the passive state when swimming produces no visual\n    feedback (open loop) than in closed loop with a naturalistic gain, where passivity is rare.\n  source: Figure 1J; Figure 1C to E; Results, first section\n  criterion: Per fish, the fraction of time in passive epochs (gaps of 5 s or more between bouts)\n    in closed loop and in open loop. Reproduced when the open-loop fraction is higher by a\n    one-sided Wilcoxon signed-rank test over fish at p < 0.05 and the median closed-loop fraction\n    is below 10%; partially reproduced when only the test holds.\n- id: fig1c-vigor-open-loop-onset\n  statement: When switched from closed to open loop, fish first swim with higher vigor, then\n    stop swimming.\n  source: Figure 1C; Results, first section\n  criterion: For each switch from closed to open loop, the mean power (SwimIntervals) of the bouts\n    from the switch to the first passive epoch, over the mean power of the bouts in the 30 s of\n    closed loop before the switch. Per fish the median log ratio over switches. Reproduced when\n    the log ratio is above 0 by a one-sided Wilcoxon signed-rank test over fish at p < 0.05.\n    Switches with fewer than 3 bouts on either side are left out.\n- id: fig1i-isi-before-passivity\n  statement: Before the switch to passivity the inter-swim interval increases progressively, and\n    fish swim more vigorously and less frequently in the seconds before passivity.\n  source: Figure 1I (n = 61 fish); Results, first section\n  criterion: For each passivity onset whose active epoch holds at least 10 bouts, the start-to-start\n    intervals numbered back from the last one (k = 1 is the interval ending at the last bout) and\n    the power of the bouts numbered back from the last. Per fish the mean at each k. Reproduced\n    when the interval at k = 1 is longer than at k = 7 (one-sided Wilcoxon over fish, p < 0.05),\n    the Spearman correlation between k and the mean over fish for k = 1 to 7 is negative, and the\n    mean power of the last 3 bouts is higher than that of bouts 8 to 10 before onset (one-sided\n    Wilcoxon over fish, p < 0.05). Partially reproduced when the interval part holds and the\n    power part does not, or the reverse.\n- id: fig2bc-neurons-lower-in-passivity\n  statement: Whole-brain average neuronal activity is higher during active behavior than during\n    passivity, and decays after passivity onset.\n  source: Figure 2B and 2C; Results, second section\n  criterion: In the 8 files with processed neuronal traces, per fish the mean of the whole-brain\n    neuronal signal over open-loop passive epochs minus that over open-loop active epochs.\n    Reproduced when it is below 0 by a one-sided Wilcoxon signed-rank test over fish at p < 0.05.\n    The change after onset (5 to 10 s after, minus 10 to 5 s before) is reported per fish.\n- id: fig2c-glia-rise-at-passivity\n  statement: Whole-brain average radial astrocyte calcium increases before passivity onset and\n    peaks soon after it.\n  source: Figure 2B and 2C (one example fish, 64 events); Figure 2G and 2I; Results, second section\n  criterion: In the 4 files with processed glial traces, per passivity onset the glial signal\n    averaged over 1 to 4 s after onset minus its mean over 10 to 5 s before (the paper's\n    reliability windows), and the mean over 2 to 0 s before onset minus the same baseline. Per\n    fish, one-tailed Wilcoxon signed-rank tests over onsets. Reproduced when, in at least 3 of the\n    4 fish, both the after-onset increase and the before-onset increase have p < 0.05 and the\n    peak of the onset-triggered average lies between 0 and 10 s after onset. Partially\n    reproduced when only the after-onset increase holds in at least 3 fish. The number of onsets\n    per fish is compared with the 64 events of the paper's example.\n- id: figs2a-open-loop-higher\n  statement: Whole-brain average neuronal and glial calcium are higher and fluctuate more strongly\n    in open loop than in closed loop.\n  source: Results, second section; Figure S2A (not read)\n  criterion: Per fish, the mean and the standard deviation of the whole-brain signal over open-loop\n    time and over closed-loop time, leaving out the first 30 s after each switch. Neurons (8 fish);\n    one-sided Wilcoxon signed-rank tests over fish for open above closed at p < 0.05. Glia (4\n    fish); open above closed in all 4 (a Wilcoxon test over 4 fish cannot reach p < 0.05).\n    Reproduced when both measures hold for both cell types; partially reproduced when at least\n    one measure holds for one cell type.\n- id: fig2h-glia-weaker-closed-loop-pauses\n  statement: When fish in closed loop stop swimming because the stimulus stops moving, glial\n    calcium signals are weaker than during futility-induced passivity.\n  source: Figure 2H and 2M; Results, second section\n  criterion: In the 4 files with processed glial traces, closed-loop pauses are gaps of 5 s or more\n    between bouts that start in closed-loop time or in stationary-grating time with gain above 0.\n    Response as in fig2c-glia-rise-at-passivity (1 to 4 s after onset minus 10 to 5 s before).\n    Per fish, a one-sided Mann-Whitney test of closed-loop pause responses against open-loop\n    passivity responses. Fish with fewer than 3 closed-loop pauses are left out; the claim is\n    blocked (other) when fewer than 2 fish remain. Reproduced when the pause responses are smaller\n    with p < 0.05 in every remaining fish; partially reproduced when they are smaller in median in\n    every remaining fish.\n- id: fig2dg-nmf-components\n  statement: Non-negative matrix factorization of neurons and radial astrocytes gives components\n    consistent across fish; glial component 1, in the lateral medulla oblongata (L-MO), is the most\n    reliable, rising before and peaking after passivity onset (n = 5 neuron fish, 6 glia fish).\n  source: Figure 2D to 2G\n- id: fig2kl-lmo-glia-most-consistent\n  statement: Of all brain regions, radial astrocytes in L-MO show the most consistent increases at\n    passivity onset, with ramping signals before it.\n  source: Figure 2K, 2L and 2M\n- id: fig1k-passive-unresponsive\n  statement: Passive fish are less responsive to visual motion than active fish (p = 4.2e-7, n = 11).\n  source: Figure 1K\n- id: fig1f-replay\n  statement: Replaying in open loop the visual motion recorded in closed loop also induces\n    passivity.\n  source: Figure 1F\n- id: fig4-glia-necessary\n  statement: Ablating radial astrocytes, or blocking their IP3 receptors, halves futility-induced\n    passivity, while random neuronal ablation does not change it.\n  source: Figure 4\n- id: fig5-glia-sufficient\n  statement: Activating radial astrocytes with TRPV1, CoChR or Opto-alpha1-AR suppresses swimming,\n    and astrocyte activation drives GABAergic neurons at the edge of L-MO.\n  source: Figure 5\n- id: fig6a-ne-ramp\n  statement: The neuronal population whose activity rises fastest before passivity overlaps the\n    noradrenergic neurons of the medulla oblongata (NE-MO).\n  source: Figure 6A\n- id: fig6-ne-drives-glia\n  statement: NE-MO activity precedes astrocyte activity at passivity, NE-MO ablation reduces\n    passivity, and NE-MO stimulation activates radial astrocytes through alpha1B receptors.\n  source: Figure 6B to 6N\n- id: fig7-ne-mismatch\n  statement: NE-MO neurons respond to swims without visual feedback, encoding sensory-motor\n    mismatch.\n  source: Figure 7A to 7G\n- id: fig7-glia-accumulate\n  statement: Radial astrocyte calcium grows with the number of consecutive failed swims and with\n    the probability that a swim fails.\n  source: Figure 7H to 7K\n"
}
```

```
File created successfully at: claims/000350/10.1016-j.cell.2019.05.050.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Now the helper module. First a quick look at the TTL signal to see whether volume starts can be matched to the imaging timestamps.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > p7.py <<'EOF'
import h5py, remfile, numpy as np
f=h5py.File(remfile.File("https://api.dandiarchive.org/api/assets/4f898ff7-6084-4e84-a449-f05811c1d951/download/"),'r')
x=f['acquisition/FrameCaptureTTLSignal/data'][:]
fs=5989.6
print(np.percentile(x,[0,1,10,50,90,99,99.9,100]))
h,e=np.histogram(x,bins=40); print(list(zip(np.round(e[:-1],2),h)))
ts=f['processing/ophys/DfOverF/NeuronDfOverF/timestamps'][:]
for thr in [3.0,3.8,4.5]:
    up=np.flatnonzero((x[1:]>thr)&(x[:-1]<=thr))/fs
    print(thr,len(up), up[:5], np.median(np.diff(up)))
EOF
timeout 600 python -u p7.py
```

```
[-2.59711407e-02 -1.50225814e-02 -1.08363675e-02 -5.52309630e-03
  1.56126590e-03  3.49820614e+00  3.99251413e+00  4.00555611e+00]
[(np.float64(-0.03), np.int64(25172246)), (np.float64(0.07), np.int64(310)), (np.float64(0.18), np.int64(209)), (np.float64(0.28), np.int64(168)), (np.float64(0.38), np.int64(126)), (np.float64(0.48), np.int64(118)), (np.float64(0.58), np.int64(86)), (np.float64(0.68), np.int64(92)), (np.float64(0.78), np.int64(87)), (np.float64(0.88), np.int64(98)), (np.float64(0.98), np.int64(73)), (np.float64(1.08), np.int64(69)), (np.float64(1.18), np.int64(75)), (np.float64(1.28), np.int64(84)), (np.float64(1.39), np.int64(67)), (np.float64(1.49), np.int64(73)), (np.float64(1.59), np.int64(50)), (np.float64(1.69), np.int64(63)), (np.float64(1.79), np.int64(60)), (np.float64(1.89), np.int64(59)), (np.float64(1.99), np.int64(64)), (np.float64(2.09), np.int64(72)), (np.float64(2.19), np.int64(67)), (np.float64(2.29), np.int64(67)), (np.float64(2.39), np.int64(88)), (np.float64(2.49), np.int64(73)), (np.float64(2.59), np.int64(75)), (np.float64(2.7), np.int64(95)), (np.float64(2.8), np.int64(94)), (np.float64(2.9), np.int64(109)), (np.float64(3.0), np.int64(105)), (np.float64(3.1), np.int64(158)), (np.float64(3.2), np.int64(174)), (np.float64(3.3), np.int64(295)), (np.float64(3.4), np.int64(2063774)), (np.float64(3.5), np.int64(28214)), (np.float64(3.6), np.int64(7)), (np.float64(3.7), np.int64(6)), (np.float64(3.8), np.int64(15)), (np.float64(3.9), np.int64(72135))]
3.0 361510 [0.00534259 0.01502605 0.0247095  0.03439295 0.0440764 ] 0.009683451315595448
3.8 12051 [0.00534259 0.37164418 0.73811273 1.10458127 1.47088286] 0.36646854547871044
/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862: RuntimeWarning: Mean of empty slice
  return _methods._mean(a, axis=axis, dtype=dtype,
/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret
[... 2 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000350-mu-2019/fictive.py",
 "content": "\"\"\"Loading and behavioural measures for the light-sheet fictive-swimming sessions of dandiset 000350.\n\nMu, Bennett, Rubinov et al. (2019), Cell 178, 27-43, doi:10.1016/j.cell.2019.05.050.\n\nEach NWB file holds one paralysed larval zebrafish swimming fictively in a one-dimensional virtual\nreality while its brain is imaged with a light-sheet microscope. Every file holds the raw signals\nof the rig at 5989.6 Hz (two swim channels, the stimulus gain, the grating's baseline velocity,\nthe stimulus type and parameters, and the camera trigger), the swim bouts (`SwimIntervals`) and\na table of behavioural states (`ActivityStates`). Eight files also hold segmented cell traces\n(`processing/ophys/DfOverF`), of neurons, of radial astrocytes (\"glia\"), or of both. Files are\nstreamed from the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Passive and active epochs follow the STAR Methods (\"Futility-induced passivity behavioral\n  analysis\"): a passive epoch is a pause of `PASSIVE_GAP_S` (5 s) or more; an active epoch is a\n  chain of bouts separated by pauses under 5 s whose first start and last end are more than 5 s\n  apart. The pause is measured from the end of one bout to the start of the next, a choice made\n  here (the Methods say \"did not swim for at least 5 s\").\n- Open loop is gain 0 (Methods: \"In open loop, the gain was zero\"); closed loop is gain above 0.\n  Both require the grating to move (baseline velocity above 0); `GAIN_EPS` and the 10 Hz grid of\n  the condition signals (`COND_HZ`) are common choices made here.\n- The windows of the onset analyses (baseline 10 to 5 s before onset, response 1 to 4 s after)\n  are those of the Methods (\"Analysis of component and cell activity around passivity onset\").\n- The whole-brain signal is the mean of the DfOverF series over an evenly spaced subset of ROI\n  blocks (`N_ROI_BLOCKS` blocks of the file's chunk width); reading every ROI of every file\n  would take far longer than the notebook's time limit. This is a choice made here.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport os\nfrom concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET_ID = \"000350\"\nDANDISET_VERSION = \"0.240822.1759\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nCOND_HZ = 10.0          # grid for the condition signals (gain, grating velocity)\nGAIN_EPS = 1e-4         # gain at or below this is taken as 0 (open loop)\nPASSIVE_GAP_S = 5.0     # Methods: passive if the fish did not swim for 5 s or more\nMIN_SEGMENT_S = 10.0    # shorter condition periods are left out\nN_ROI_BLOCKS = 8        # ROI blocks read per imaging series for the whole-brain signal\nBASELINE = (-10.0, -5.0)  # Methods: baseline 10 to 5 s before passivity onset\nRESPONSE = (1.0, 4.0)     # Methods: reliability from 1 to 4 s after onset\n\n\ndef assets(version: str = DANDISET_VERSION) -> list[dict]:\n    \"\"\"Every asset of the dandiset at a version, sorted by path.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=100\"\n    out = []\n    while url:\n        page = requests.get(url, timeout=60)\n        page.raise_for_status()\n        page = page.json()\n        out += page[\"results\"]\n        url = page[\"next\"]\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef open_asset(asset_id: str) -> h5py.File:\n    return h5py.File(remfile.File(f\"{API}/assets/{asset_id}/download/\"), \"r\")\n\n\ndef _text(value) -> str:\n    value = value[()] if hasattr(value, \"shape\") else value\n    return value.decode() if isinstance(value, bytes) else str(value)\n\n\ndef _decimate(dataset, step: int, column: int | None = None) -> np.ndarray:\n    data = dataset[:] if column is None else dataset[:, column]\n    return data[::step]\n\n\ndef load_session(asset: dict) -> dict:\n    \"\"\"Metadata, behaviour, conditions and imaging layout of one file (no cell traces).\"\"\"\n    f = open_asset(asset[\"asset_id\"])\n    g = f[\"general\"]\n    s = {\"path\": asset[\"path\"], \"asset_id\": asset[\"asset_id\"], \"fish\": asset[\"path\"].split(\"/\")[0][4:]}\n    s[\"subject\"] = {k: _text(v) for k, v in g[\"subject\"].items()}\n    s[\"session_start\"] = _text(f[\"session_start_time\"])\n    s[\"session_description\"] = _text(f[\"session_description\"])\n    s[\"planes\"] = {name: {k: _text(v) for k, v in grp.items() if isinstance(v, h5py.Dataset)}\n                   | {\"channel\": {k: _text(v) for k, v in grp[c].items()}\n                      for c in grp if isinstance(grp[c], h5py.Group)}.get(\"channel\", None)\n                   | {\"channel_emission\": next((_text(grp[c][\"emission_lambda\"]) for c in grp\n                                                if isinstance(grp[c], h5py.Group)), None)}\n                   for name, grp in g[\"optophysiology\"].items()}\n    acq = f[\"acquisition\"]\n    rate = float(acq[\"SwimSignals/starting_time\"].attrs[\"rate\"])\n    s[\"rate\"] = rate\n    s[\"n_samples\"] = acq[\"SwimSignals/data\"].shape[0]\n    s[\"duration_s\"] = s[\"n_samples\"] / rate\n    s[\"raw_series\"] = {k: {\"shape\": acq[k][\"data\"].shape, \"neurodata_type\": _text(acq[k].attrs[\"neurodata_type\"]),\n                           \"t\": acq[k][\"timestamps\"][:]}\n                       for k in acq if \"Series\" in k}\n    step = int(round(rate / COND_HZ))\n    s[\"cond_t\"] = np.arange(0, s[\"n_samples\"], step) / rate\n    s[\"gain\"] = _decimate(acq[\"StimulusGainSignal/data\"], step)\n    s[\"velocity\"] = _decimate(acq[\"BaselineStimulusVelocitySignal/data\"], step)\n    s[\"protocol_code\"] = _decimate(acq[\"StimulusParameterSignals/data\"], step, 0)\n    ttl = acq[\"FrameCaptureTTLSignal/data\"][:]\n    s[\"ttl_volume_starts\"] = np.flatnonzero((ttl[1:] > 3.8) & (ttl[:-1] <= 3.8)) / rate\n    s[\"ttl_range\"] = (float(ttl.min()), float(ttl.max()))\n    b = f[\"processing/behavior\"]\n    s[\"swims\"] = pd.DataFrame({k: b[\"SwimIntervals\"][k][:] for k in [\"start_time\", \"stop_time\", \"power\", \"width\"]})\n    s[\"states\"] = pd.DataFrame({\"start\": b[\"ActivityStates/start_time\"][:], \"stop\": b[\"ActivityStates/stop_time\"][:],\n                                \"type\": [_text(x) for x in b[\"ActivityStates/state_type\"][:]]})\n    s[\"n_burst_events\"] = b[\"BurstEvents/event_times\"].shape[0]\n    s[\"behavior_units\"] = {\"SwimSignals\": _text(acq[\"SwimSignals/data\"].attrs[\"unit\"]),\n                           \"StimulusGainSignal\": _text(acq[\"StimulusGainSignal/data\"].attrs[\"unit\"])}\n    s[\"imaging\"] = {}\n    if \"ophys\" in f[\"processing\"]:\n        for name, series in f[\"processing/ophys/DfOverF\"].items():\n            d = series[\"data\"]\n            s[\"imaging\"][name] = {\"shape\": d.shape, \"chunks\": d.chunks, \"t\": series[\"timestamps\"][:],\n                                  \"unit\": _text(d.attrs[\"unit\"]), \"description\": _text(series.attrs[\"description\"])}\n    f.close()\n    return s\n\n\ndef load_all(version: str = DANDISET_VERSION) -> list[dict]:\n    with ThreadPoolExecutor(6) as ex:\n        return list(ex.map(load_session, [a for a in assets(version) if a[\"path\"].endswith(\".nwb\")]))\n\n\n# --- conditions and epochs -----------------------------------------------------------------\n\ndef condition_masks(s: dict) -> dict[str, np.ndarray]:\n    \"\"\"Boolean masks on `cond_t`: closed loop, open loop (both with the grating moving), and\n    any time with gain above 0.\"\"\"\n    moving = s[\"velocity\"] > 0\n    gain_on = s[\"gain\"] > GAIN_EPS\n    return {\"closed\": gain_on & moving, \"open\": ~gain_on & moving, \"gain_on\": gain_on}\n\n\ndef segments(t: np.ndarray, mask: np.ndarray, min_len: float = MIN_SEGMENT_S) -> list[tuple[float, float]]:\n    \"\"\"Contiguous periods where `mask` holds, as (start, stop) in seconds.\"\"\"\n    edges = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))\n    dt = t[1] - t[0]\n    out = [(t[a], t[b - 1] + dt) for a, b in zip(edges[::2], edges[1::2])]\n    return [(a, b) for a, b in out if b - a >= min_len]\n\n\ndef epochs_in_segment(swims: pd.DataFrame, seg: tuple[float, float], gap: float = PASSIVE_GAP_S) -> dict:\n    \"\"\"Passive and active epochs inside one condition period, by the Methods' rule.\n\n    Passive epochs are pauses of `gap` or more between two bouts inside the period. Active epochs\n    are chains of bouts separated by pauses under `gap`, longer than `gap` from first start to last\n    end, and bounded on both sides by a pause of `gap` or more (a period edge counts as a pause\n    only if the time to it is `gap` or more). Returns the epochs and every pause of `gap` or more,\n    including those cut by the period's edges (for fractions of time).\n    \"\"\"\n    a, b = seg\n    w = swims[(swims.start_time >= a) & (swims.stop_time <= b)].sort_values(\"start_time\")\n    st, sp, pw = w.start_time.to_numpy(), w.stop_time.to_numpy(), w.power.to_numpy()\n    if len(st) == 0:\n        return {\"passive\": [], \"active\": [], \"pauses\": [(a, b)], \"seg\": seg}\n    gaps = st[1:] - sp[:-1]\n    passive = [(sp[i], st[i + 1]) for i in np.flatnonzero(gaps >= gap)]\n    pauses = list(passive)\n    if st[0] - a >= gap:\n        pauses.append((a, st[0]))\n    if b - sp[-1] >= gap:\n        pauses.append((sp[-1], b))\n    breaks = np.flatnonzero(gaps >= gap)\n    starts = np.r_[0, breaks + 1]\n    stops = np.r_[breaks, len(st) - 1]\n    active = []\n    for i0, i1 in zip(starts, stops):\n        before = st[i0] - (sp[i0 - 1] if i0 > 0 else a)\n        after = (st[i1 + 1] if i1 + 1 < len(st) else b) - sp[i1]\n        if sp[i1] - st[i0] > gap and before >= gap and after >= gap:\n            active.append({\"start\": st[i0], \"stop\": sp[i1], \"n_bouts\": i1 - i0 + 1,\n                           \"bout_starts\": st[i0:i1 + 1], \"bout_powers\": pw[i0:i1 + 1],\n                           \"followed_by_passive\": i1 + 1 < len(st)})\n    return {\"passive\": passive, \"active\": active, \"pauses\": pauses, \"seg\": seg}\n\n\ndef session_epochs(s: dict, condition: str) -> list[dict]:\n    m = condition_masks(s)[condition]\n    return [epochs_in_segment(s[\"swims\"], seg) for seg in segments(s[\"cond_t\"], m)]\n\n\ndef passivity_onsets(s: dict) -> np.ndarray:\n    \"\"\"End of the last bout of each open-loop active epoch followed by a passive epoch.\"\"\"\n    return np.array(sorted(e[\"stop\"] for seg in session_epochs(s, \"open\") for e in seg[\"active\"]\n                           if e[\"followed_by_passive\"]))\n\n\ndef closed_loop_pause_onsets(s: dict) -> np.ndarray:\n    \"\"\"Starts of pauses of 5 s or more that begin while the gain is above 0 (closed loop with the\n    grating moving or stationary), between two bouts.\"\"\"\n    sw = s[\"swims\"].sort_values(\"start_time\")\n    st, sp = sw.start_time.to_numpy(), sw.stop_time.to_numpy()\n    on = sp[:-1][(st[1:] - sp[:-1]) >= PASSIVE_GAP_S]\n    gain_on = condition_masks(s)[\"gain_on\"]\n    idx = np.clip(np.searchsorted(s[\"cond_t\"], on), 0, len(gain_on) - 1)\n    # the gain must stay above 0 over the response window as well\n    idx_end = np.clip(np.searchsorted(s[\"cond_t\"], on + RESPONSE[1]), 0, len(gain_on) - 1)\n    return on[gain_on[idx] & gain_on[idx_end]]\n\n\n# --- imaging -------------------------------------------------------------------------------\n\ndef roi_blocks(n_rois: int, width: int, n_blocks: int = N_ROI_BLOCKS, offset: float = 0.0) -> list[tuple[int, int]]:\n    \"\"\"Evenly spaced blocks of `width` ROIs (the file's chunk width), `offset` in units of the\n    spacing (0 for the main subset; 0.5 gives a disjoint subset).\"\"\"\n    total = int(np.ceil(n_rois / width))\n    spacing = total / n_blocks\n    idx = sorted({int((i + offset) * spacing) for i in range(n_blocks)})\n    return [(i * width, min((i + 1) * width, n_rois)) for i in idx]\n\n\ndef _block_sum(args):\n    asset_id, name, lo, hi = args\n    os.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\n    with open_asset(asset_id) as f:\n        d = f[f\"processing/ophys/DfOverF/{name}/data\"][:, lo:hi]\n    return asset_id, name, d.sum(1), hi - lo\n\n\ndef whole_brain_means(jobs: list[tuple[dict, str, float]], workers: int = 4) -> dict:\n    \"\"\"Mean DfOverF over the ROI subset, per (fish, series, offset). Each block is read in its own\n    process, as h5py reads one chunk at a time.\"\"\"\n    tasks, keys = [], []\n    for s, name, offset in jobs:\n        info = s[\"imaging\"][name]\n        for lo, hi in roi_blocks(info[\"shape\"][1], info[\"chunks\"][1], offset=offset):\n            tasks.append((s[\"asset_id\"], name, lo, hi))\n            keys.append((s[\"fish\"], name, offset))\n    sums, counts = {}, {}\n    with ProcessPoolExecutor(workers) as ex:\n        for key, (_, _, total, n) in zip(keys, ex.map(_block_sum, tasks)):\n            sums[key] = sums.get(key, 0) + total\n            counts[key] = counts.get(key, 0) + n\n    return {k: (sums[k] / counts[k], counts[k]) for k in sums}\n\n\ndef event_windows(t: np.ndarray, y: np.ndarray, onsets: np.ndarray, lags: np.ndarray) -> np.ndarray:\n    \"\"\"y interpolated at onset + lag, one row per onset (NaN outside the recording).\"\"\"\n    grid = onsets[:, None] + lags[None, :]\n    out = np.interp(grid, t, y)\n    out[(grid < t[0]) | (grid > t[-1])] = np.nan\n    return out\n\n\ndef window_mean(t: np.ndarray, y: np.ndarray, onsets: np.ndarray, window: tuple[float, float]) -> np.ndarray:\n    \"\"\"Mean of y over [onset + window[0], onset + window[1]] for each onset (NaN if empty).\"\"\"\n    out = np.full(len(onsets), np.nan)\n    for i, o in enumerate(onsets):\n        sel = (t >= o + window[0]) & (t <= o + window[1])\n        if sel.any():\n            out[i] = y[sel].mean()\n    return out\n\n\ndef mean_in_intervals(t: np.ndarray, y: np.ndarray, intervals) -> float:\n    sel = np.zeros(len(t), bool)\n    for a, b in intervals:\n        sel |= (t >= a) & (t < b)\n    return float(y[sel].mean()) if sel.any() else np.nan\n\n\ndef swim_rate(s: dict, t: np.ndarray) -> np.ndarray:\n    \"\"\"Number of bout starts in each imaging frame interval of `t`.\"\"\"\n    edges = np.r_[t, t[-1] + np.median(np.diff(t))]\n    return np.histogram(s[\"swims\"].start_time.to_numpy(), bins=edges)[0].astype(float)\n"
}
```

```
File created successfully at: entries/000350-mu-2019/fictive.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000350-mu-2019/fictive.py",
 "old_string": "    s[\"planes\"] = {name: {k: _text(v) for k, v in grp.items() if isinstance(v, h5py.Dataset)}\n                   | {\"channel\": {k: _text(v) for k, v in grp[c].items()}\n                      for c in grp if isinstance(grp[c], h5py.Group)}.get(\"channel\", None)\n                   | {\"channel_emission\": next((_text(grp[c][\"emission_lambda\"]) for c in grp\n                                                if isinstance(grp[c], h5py.Group)), None)}\n                   for name, grp in g[\"optophysiology\"].items()}",
 "new_string": "    s[\"planes\"] = {}\n    for name, grp in g[\"optophysiology\"].items():\n        plane = {k: _text(v) for k, v in grp.items() if isinstance(v, h5py.Dataset)}\n        for c in grp:\n            if isinstance(grp[c], h5py.Group) and \"emission_lambda\" in grp[c]:\n                plane[\"emission_lambda\"] = _text(grp[c][\"emission_lambda\"])\n                plane[\"filter\"] = _text(grp[c][\"description\"])\n        s[\"planes\"][name] = plane"
}
```

```
The file entries/000350-mu-2019/fictive.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000350-mu-2019 && . $TMPDIR/env/bin/activate && cat > $TMPDIR/t1.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'.')
import fictive as fv, numpy as np
t=time.time(); S=fv.load_all(); print('load', time.time()-t)
pickle.dump(S, open(sys.argv[1],'wb'))
for s in S:
    on=fv.passivity_onsets(s); ep=fv.session_epochs(s,'open')
    pas=[b-a for e in ep for a,b in e['passive']]; act=[e['stop']-e['start'] for x in ep for e in x['active']]
    print(s['fish'], len(s['swims']), 'onsets',len(on), 'passive n',len(pas), 'act n', len(act), 'cl pauses', len(fv.closed_loop_pause_onsets(s)), 'ttl', len(s['ttl_volume_starts']), {k:v['shape'] for k,v in s['imaging'].items()})
EOF
timeout 900 python -u $TMPDIR/t1.py $TMPDIR/S.pkl
```

```
load 62.762635946273804
20161022-1 446 onsets 31 passive n 71 act n 32 cl pauses 25 ttl 8651 {}
20161109-2 2550 onsets 26 passive n 32 act n 26 cl pauses 30 ttl 12501 {'GliaDfOverF': (12500, 100840), 'NeuronDfOverF': (12500, 109918)}
20161206-1 1295 onsets 33 passive n 41 act n 34 cl pauses 51 ttl 9001 {}
20161206-2 1437 onsets 38 passive n 60 act n 38 cl pauses 53 ttl 8501 {}
20170111-1 1014 onsets 37 passive n 44 act n 44 cl pauses 38 ttl 10051 {}
20170113-2 1126 onsets 97 passive n 147 act n 104 cl pauses 21 ttl 9751 {'NeuronDfOverF': (7616, 85452)}
20170113-3 1177 onsets 23 passive n 43 act n 32 cl pauses 28 ttl 9814 {'NeuronDfOverF': (9813, 90705)}
20170113-4 1453 onsets 27 passive n 49 act n 35 cl pauses 60 ttl 12051 {'NeuronDfOverF': (12050, 93344)}
20170127-1 1656 onsets 24 passive n 29 act n 25 cl pauses 75 ttl 10823 {'NeuronDfOverF': (10822, 99377)}
20170203-1 1525 onsets 46 passive n 96 act n 50 cl pauses 43 ttl 8501 {'GliaDfOverF': (8500, 100159), 'NeuronDfOverF': (8500, 111235)}
20170228-3 559 onsets 67 passive n 129 act n 68 cl pauses 13 ttl 6068 {'GliaDfOverF': (6067, 126467), 'NeuronDfOverF': (6067, 111378)}
20170228-4 2793 onsets 108 passive n 142 act n 108 cl pauses 33 ttl 7201 {'GliaDfOverF': (7200, 122296), 'NeuronDfOverF': (7200, 124078)}
```

**Agent**

Epochs and onsets look sensible for all 12 fish. Another finding: sub-20170113-2 has 9751 camera triggers but only 7616 imaging volumes. Now timing the whole-brain means (12 series × 8 ROI blocks).

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/t2.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'.')
import fictive as fv
if __name__=='__main__':
    S=pickle.load(open(sys.argv[1],'rb'))
    jobs=[(s,n,0.0) for s in S for n in s['imaging']]
    t=time.time(); W=fv.whole_brain_means(jobs); print('means', time.time()-t)
    pickle.dump(W, open(sys.argv[2],'wb'))
    for k,(m,n) in W.items(): print(k, n, m[:3], m.mean())
EOF
timeout 3000 python -u $TMPDIR/t2.py $TMPDIR/S.pkl $TMPDIR/W.pkl
```

```
means 371.75964736938477
('20161109-2', 'GliaDfOverF', 0.0) 11264 [-2.6142685e-05 -2.6142685e-05 -2.6142685e-05] -2.6142121e-05
('20161109-2', 'NeuronDfOverF', 0.0) 11264 [-0.00013426 -0.00013426 -0.00013426] -0.00013426102
('20170113-2', 'NeuronDfOverF', 0.0) 9328 [0.99079589 0.99409653 0.99622024] 1.0
('20170113-3', 'NeuronDfOverF', 0.0) 8424 [0.99189971 0.99167328 0.99720528] 1.0
('20170113-4', 'NeuronDfOverF', 0.0) 7448 [1.01122632 1.01194959 1.00989067] 1.0
('20170127-1', 'NeuronDfOverF', 0.0) 8424 [0.97294709 0.99499672 0.99838465] 1.0
('20170203-1', 'GliaDfOverF', 0.0) 13200 [-3.954317e-05 -3.954317e-05 -3.954317e-05] -3.95432e-05
('20170203-1', 'NeuronDfOverF', 0.0) 14352 [-1.1059204e-05 -1.1059204e-05 -1.1059204e-05] -1.1059188e-05
('20170228-3', 'GliaDfOverF', 0.0) 17760 [-0.00011551 -0.00011551 -0.00011551] -0.00011551198
('20170228-3', 'NeuronDfOverF', 0.0) 16848 [-4.8088717e-05 -4.8088717e-05 -4.8088717e-05] -4.8088317e-05
('20170228-4', 'GliaDfOverF', 0.0) 16000 [-4.7501806e-05 -4.7501806e-05 -4.7501806e-05] -4.7502155e-05
('20170228-4', 'NeuronDfOverF', 0.0) 16456 [-9.713514e-06 -9.713514e-06 -9.713514e-06] -9.7129905e-06
```

**Agent**

The dual-colour files behave differently: their whole-brain mean is about −1e-5 and looks constant in time. Inspecting their values before going further.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/t3.py <<'EOF'
import h5py, remfile, numpy as np
f=h5py.File(remfile.File("https://api.dandiarchive.org/api/assets/dd92d978-b9ea-4c6e-83f7-c0b261897928/download/"),'r')
for n in ['GliaDfOverF','NeuronDfOverF']:
    d=f['processing/ophys/DfOverF/'+n+'/data']; print(n, d.shape, d.chunks, d.dtype, d.compression)
    x=d[:, :2000]
    print(' pct', np.percentile(x,[0,1,25,50,75,99,100]))
    print(' per-roi std pct', np.percentile(x.std(0),[0,25,50,75,100]), 'per roi mean', np.percentile(x.mean(0),[0,50,100]))
    print(' frac zero', (x==0).mean())
    i=np.argmax(x.std(0)); print(' top roi', i, x[:10,i], x.std(0)[i])
    F=f['processing/ophys/Fluorescence/'+n.replace('DfOverF','Fluorescence')+'/data'][:, :50]
    print(' F pct', np.percentile(F,[0,50,100]), F[:3,:3])
EOF
timeout 900 python -u $TMPDIR/t3.py
```

```
GliaDfOverF (7200, 122296) (125, 2000) float32 gzip
 pct [-3.19091797e-01 -2.96783447e-02 -4.81796265e-03 -9.30309296e-04
  2.83622742e-03  4.80957031e-02  1.42773438e+00]
 per-roi std pct [0.00321097 0.00508908 0.00810143 0.01204409 0.08375735] per roi mean [-5.48038282e-04 -2.76208748e-05  1.00703898e-03]
 frac zero 1.0069444444444445e-05
 top roi 1298 [0.00011194 0.00011194 0.00011194 0.00011194 0.00011194 0.00011194
 0.00011194 0.00011194 0.00011194 0.00011194] 0.08375735
 F pct [-0.1673584  -0.03735352  0.00087881] [[-2.2232533e-05 -1.7321110e-04 -1.0371208e-05]
 [-2.2232533e-05 -1.7321110e-04 -1.0371208e-05]
 [-2.2232533e-05 -1.7321110e-04 -1.0371208e-05]]
NeuronDfOverF (7200, 124078) (121, 2057) float32 gzip
 pct [-0.14245605 -0.02854919 -0.00629425 -0.00097942  0.00466919  0.043396
  0.70556641]
 per-roi std pct [0.00392938 0.0061799  0.00841984 0.01372343 0.05485004] per roi mean [-1.18730310e-03 -5.71515011e-06  8.70785327e-04]
 frac zero 2.8819444444444443e-05
 top roi 1173 [-0.00014341 -0.00014341 -0.00014341 -0.00014341 -0.00014341 -0.00014341
 -0.00014341 -0.00014341 -0.00014341 -0.00014341] 0.054850042
 F pct [-3.77807617e-02 -2.16827393e-02  2.98619270e-05] [[-3.2901764e-05 -2.9742718e-05 -5.3644180e-07]
 [-3.2901764e-05 -2.9742718e-05 -5.3644180e-07]
 [-3.2901764e-05 -2.9742718e-05 -5.3644180e-07]]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/a1.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'.')
import fictive as fv
from scipy import stats
S=pickle.load(open(sys.argv[1],'rb'))
rows=[]
for s in S:
    ep=fv.session_epochs(s,'open')
    pas=[b-a for e in ep for a,b in e['passive']]; act=[e['stop']-e['start'] for x in ep for e in x['active']]; nb=[e['n_bouts'] for x in ep for e in x['active']]
    st=s['states']; 
    rows.append(dict(fish=s['fish'], n_pas=len(pas), pas=np.mean(pas), n_act=len(act), act=np.mean(act), bouts=np.mean(nb),
      tab_pas=st[st.type=='passive'].eval('stop-start').mean(), tab_act=st[st.type=='active'].eval('stop-start').mean(),
      tab_act_gt5=(st[st.type=='active'].eval('stop-start')>5).mean()))
    # ISI
    for cond in ['closed','open']:
        ss=[];ee=[];ss5=[];ee5=[]
        for seg in fv.segments(s['cond_t'], fv.condition_masks(s)[cond]):
            w=s['swims'][(s['swims'].start_time>=seg[0])&(s['swims'].stop_time<=seg[1])].sort_values('start_time')
            a=np.diff(w.start_time.values); b=w.start_time.values[1:]-w.stop_time.values[:-1]
            ss+=list(a); ee+=list(b)
        rows[-1][cond+'_ss_all']=np.mean(ss); rows[-1][cond+'_ss_lt5']=np.mean([x for x,y in zip(ss,ee) if y<5]); rows[-1][cond+'_ee_lt5']=np.mean([y for y in ee if y<5])
    # isi within active epochs open
    a=[np.diff(e['bout_starts']) for x in ep for e in x['active']]; rows[-1]['act_isi_ss']=np.mean(np.concatenate(a))
    # passive fraction
    for cond in ['closed','open']:
        E=fv.session_epochs(s,cond); tot=sum(e['seg'][1]-e['seg'][0] for e in E); p=sum(b-a for e in E for a,b in e['pauses'])
        rows[-1]['frac_'+cond]=p/tot; rows[-1]['T_'+cond]=tot
df=pd.DataFrame(rows); pd.set_option('display.width',250)
print(df.round(3).to_string())
print(df.mean(numeric_only=True).round(3))
print('wilcoxon frac', stats.wilcoxon(df.frac_open, df.frac_closed, alternative='greater'))
EOF
timeout 900 python -u $TMPDIR/a1.py $TMPDIR/S.pkl
```

```
fish  n_pas     pas  n_act     act   bouts  tab_pas  tab_act  tab_act_gt5  closed_ss_all  closed_ss_lt5  closed_ee_lt5  open_ss_all  open_ss_lt5  open_ee_lt5  act_isi_ss  frac_closed  T_closed  frac_open    T_open
0   20161022-1     71  32.544     32   8.520   6.312   12.550    5.976        1.000          3.236          1.281          1.080        8.595        1.436        0.984       1.501        0.740   530.535      0.859  2779.586
1   20161109-2     32  30.730     26  64.149  64.769   28.623   60.187        0.811          2.445          0.955          0.840        1.401        0.980        0.752       1.002        0.736   637.043      0.321  3349.924
2   20161206-1     41  36.647     34  19.644  17.500    3.506    9.906        1.000          0.927          0.916          0.745        3.514        1.176        0.942       1.177        0.197   823.355      0.695  2296.253
3   20161206-2     60   9.676     38  29.277  19.789    6.379    9.077        1.000          1.420          1.351          1.225        2.001        1.468        1.208       1.528        0.142   744.250      0.293  1983.432
4   20170111-1     44  21.578     44  19.291  16.750   22.551   15.439        0.889         13.695          1.743          1.581        2.153        1.183        0.903       1.207        0.968  1360.091      0.565  2511.268
5   20170113-2    147  18.300    104   7.313   4.096   19.007    6.465        0.835          1.237          0.909          0.707        6.620        1.160        0.445       1.243        0.409   864.858      0.741  3990.967
6   20170113-3     43  18.137     32  26.691  20.844   27.626   19.381        0.700          2.693          1.191          1.088        2.037        1.285        0.931       1.331        0.808  1040.569      0.517  2571.472
7   20170113-4     49  16.652     35  20.030  16.486   22.726   14.343        0.754          2.858          1.063          0.786        2.053        1.238        0.804       1.247        0.766  1943.030      0.517  261
[... 25 more lines not kept]
```

**Agent**

Behaviour results are in. Before the imaging analyses, prototyping the vigor-at-switch and ISI-before-passivity claims.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/a2.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'.')
import fictive as fv
from scipy import stats
S=pickle.load(open(sys.argv[1],'rb'))
rows=[]; K=[]
for s in S:
    m=fv.condition_masks(s); t=s['cond_t']
    # switches: closed (any time) -> open : index where closed[i-1] and open[i]
    sw=t[1:][m['closed'][:-1] & m['open'][1:]]
    sws=s['swims'].sort_values('start_time')
    lr=[]
    for t0 in sw:
        pre=sws[(sws.start_time>=t0-30)&(sws.stop_time<=t0)]
        # require closed for whole 30 s
        idx=(t>=t0-30)&(t<t0)
        if not m['closed'][idx].all(): continue
        post=sws[sws.start_time>=t0]
        st=post.start_time.values; sp=post.stop_time.values
        g=np.flatnonzero(st[1:]-sp[:-1]>=5)
        if len(st)==0 or st[0]-t0>=5: continue  # passive at once
        n=(g[0]+1) if len(g) else len(st)
        post=post.iloc[:n]
        # must stay open
        endt=post.stop_time.values[-1]; idx2=(t>=t0)&(t<=endt)
        if not m['open'][idx2].all(): continue
        if len(pre)<3 or len(post)<3: continue
        lr.append(np.log(post.power.mean()/pre.power.mean()))
    rows.append(dict(fish=s['fish'], n_switch=len(sw), n_used=len(lr), med_lr=np.median(lr) if lr else np.nan))
    # ISI before passivity
    ep=fv.session_epochs(s,'open')
    isis=[];pws=[]
    for x in ep:
        for e in x['active']:
            if e['followed_by_passive'] and e['n_bouts']>=10:
                d=np.diff(e['bout_starts'])[::-1][:7]; isis.append(d); pws.append(e['bout_powers'][::-1][:10])
    if isis:
        I=np.mean(isis,0); P=np.mean(pws,0)
        K.append(dict(fish=s['fish'], n=len(isis), **{f'isi{k+1}':I[k] for k in range(7)}, pow_last3=P[:3].mean(), pow_8_10=P[7:10].mean()))
df=pd.DataFrame(rows); print(df.round(3)); d=df.med_lr.dropna(); print(stats.wilcoxon(d, alternative='greater'), np.exp(d.median()))
k=pd.DataFrame(K); print(k.round(3)); print(stats.wilcoxon(k.isi1,k.isi7,alternative='greater'), stats.spearmanr(range(1,8), k[[f'isi{i}' for i in range(1,8)]].mean().values), stats.wilcoxon(k.pow_last3,k.pow_8_10,alternative='greater'))
EOF
timeout 900 python -u $TMPDIR/a2.py $TMPDIR/S.pkl
```

```
/tmp/claude-1001/a2.py:28: RuntimeWarning: invalid value encountered in scalar divide
  lr.append(np.log(post.power.mean()/pre.power.mean()))
          fish  n_switch  n_used  med_lr
0   20161022-1         1       0     NaN
1   20161109-2         3       0     NaN
2   20161206-1         1       0     NaN
3   20161206-2         2       0     NaN
4   20170111-1        19       0     NaN
5   20170113-2        14       2   2.556
6   20170113-3        19       4   1.918
7   20170113-4        31      10   1.249
8   20170127-1         2       0     NaN
9   20170203-1        18       9     NaN
10  20170228-3         4       0     NaN
11  20170228-4         3       0     NaN
WilcoxonResult(statistic=np.float64(6.0), pvalue=np.float64(0.125)) 6.804660910365719
          fish   n   isi1   isi2  ...   isi6   isi7  pow_last3  pow_8_10
0   20161022-1   2  1.495  1.891  ...  1.539  2.031      2.082     2.014
1   20161109-2  25  1.283  1.272  ...  1.114  1.171      0.505     0.451
2   20161206-1  25  1.538  1.198  ...  1.256  1.289      0.290     0.304
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && cat > $TMPDIR/a3.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'.')
import fictive as fv
from scipy import stats
S={s['fish']:s for s in pickle.load(open(sys.argv[1],'rb'))}; W=pickle.load(open(sys.argv[2],'rb'))
for s in S.values(): print(s['fish'], 'power nan', s['swims'].power.isna().sum(), (s['swims'].power==0).sum())
def clean(t,y):
    y=y.astype(float).copy(); i=0
    while i<len(y)-1 and y[i+1]==y[0]: i+=1
    if i>0: y[:i+1]=np.nan
    j=len(y)-1
    while j>0 and y[j-1]==y[-1]: j-=1
    if j<len(y)-1: y[j:]=np.nan
    return y
R=[]
for (fish,name,off),(m,n) in W.items():
    s=S[fish]; t=s['imaging'][name]['t']; y=clean(t,m)
    ok=np.isfinite(y)
    ep=fv.session_epochs(s,'open')
    pas=[p for e in ep for p in e['passive']]; act=[(a['start'],a['stop']) for e in ep for a in e['active']]
    on=fv.passivity_onsets(s)
    base=fv.window_mean(t[ok],y[ok],on,fv.BASELINE); resp=fv.window_mean(t[ok],y[ok],on,fv.RESPONSE); pre=fv.window_mean(t[ok],y[ok],on,(-2,0)); late=fv.window_mean(t[ok],y[ok],on,(5,10))
    r=resp-base; p_=pre-base; good=np.isfinite(r)&np.isfinite(p_)
    lags=np.arange(-15,20,0.5); E=fv.event_windows(t[ok],y[ok],on,lags); avg=np.nanmean(E-base[:,None],0)
    # clock check: xcorr swim rate vs signal
    rate=fv.swim_rate(s,t)[ok]; yy=y[ok]
    dt=np.median(np.diff(t)); L=int(10/dt); cc=[np.corrcoef(rate[max(0,-l):len(rate)-max(0,l)], yy[max(0,l):len(yy)-max(0,-l)])[0,1] for l in range(-L,L+1)]
    pk=(np.argmax(cc)-L)*dt
    # cl pauses
    cp=fv.closed_loop_pause_onsets(s); rc=fv.window_mean(t[ok],y[ok],cp,fv.RESPONSE)-fv.window_mean(t[ok],y[ok],cp,fv.BASELINE)
    R.append(dict(fish=fish, name=name[:5], n_on=int(good.sum()), pas_minus_act=fv.mean_in_intervals(t[ok],y[ok],pas)-fv.mean_in_intervals(t[ok],y[ok],act),
        resp=np.nanmedian(r), p_resp=stats.wilcoxon(r[good],alternative='greater').pvalue, pre=np.nanmedian(p_), p_pre=stats.wilcoxon(p_[good],alternative='greater').pvalue,
        late=np.nanmedian(late-base), peak_lag=lags[np.nanargmax(avg)], xc_peak_lag=pk, xc_max=max(cc),
        n_cp=int(np.isfinite(rc).sum()), cp_resp=np.nanmedian(rc), p_cp=stats.mannwhitneyu(rc[np.isfinite(rc)], r[good], alternative='less').pvalue if np.isfinite(rc).sum()>2 else np.nan))
df=pd.DataFrame(R); pd.set_option('display.width',250); print(df.to_string(float_format=lambda v:f'{v:.3g}'))
EOF
timeout 900 python -u $TMPDIR/a3.py $TMPDIR/S.pkl $TMPDIR/W.pkl
```

```
20161022-1 power nan 0 0
20161109-2 power nan 0 0
20161206-1 power nan 0 0
20161206-2 power nan 0 0
20170111-1 power nan 0 0
20170113-2 power nan 0 0
20170113-3 power nan 0 0
20170113-4 power nan 0 0
20170127-1 power nan 0 0
20170203-1 power nan 0 70
20170228-3 power nan 0 0
20170228-4 power nan 0 279
          fish   name  n_on  pas_minus_act      resp   p_resp       pre    p_pre      late  peak_lag  xc_peak_lag  xc_max  n_cp   cp_resp     p_cp
0   20161109-2  GliaD    26       -0.00158  -0.00145        1 -0.000187     0.48   -0.0014         0        0.349   0.326    26 -0.000215    0.782
1   20161109-2  Neuro    26       -0.00541  -0.00151    0.986 -9.96e-05    0.146   -0.0029         0        0.349   0.162    26 -0.000893    0.218
2   20170113-2  Neuro    64        -0.0214    0.0121 1.79e-08     0.044 2.03e-12 -0.000767      -0.5         4.76   0.219     7   0.00475  0.00697
3   20170113-3  Neuro    23        -0.0269   -0.0126        1   0.00341    0.355   -0.0213         0          2.2   0.339    28  7.46e-05    0.999
4   20170113-4  Neuro    21        -0.0135   -0.0131        1  -0.00153    0.831   -0.0184         0          4.4   0.294    60   0.00109        1
5   20170127-1  Neuro    24         -0.013  -0.00551        1   0.00596   0.0135   -0.0154         0        0.369   0.421    75     -0.01    0.374
6   20170203-1  GliaD    46       -0.00139 -0.000694        1  0.000669 0.000551 -0.000943        -4         1.18   0.358    43 -9.71e-05    0.982
[... 5 more lines not kept]
```

**Agent**

Prototypes done. Neurons are lower in passive than active epochs in all 8 fish; the glial rise at passivity onset shows in 2 of 4 dual-colour fish. Building the notebook now.

**Agent calls Bash**

```bash
cat >> entries/000350-mu-2019/fictive.py <<'EOF'


def condition_labels(s: dict) -> np.ndarray:
    """Per `cond_t` sample: 1 closed loop, 2 open loop, 0 other (stationary grating)."""
    m = condition_masks(s)
    return np.where(m["closed"], 1, np.where(m["open"], 2, 0))


def seconds_since_switch(s: dict, t: np.ndarray) -> np.ndarray:
    """For times `t`, the time since the condition label last changed."""
    lab = condition_labels(s)
    changes = s["cond_t"][1:][np.diff(lab) != 0]
    changes = np.r_[s["cond_t"][0], changes]
    last = changes[np.clip(np.searchsorted(changes, t, side="right") - 1, 0, None)]
    return t - last


def label_at(s: dict, t: np.ndarray) -> np.ndarray:
    idx = np.clip(np.searchsorted(s["cond_t"], t), 0, len(s["cond_t"]) - 1)
    return condition_labels(s)[idx]


def censored(y: np.ndarray) -> np.ndarray:
    """Frames at the start or end of a trace that repeat its first or last value exactly; the
    segmentation code (z6_components.py, `censor_tau`) sets such frames to a constant."""
    out = np.zeros(len(y), bool)
    i = 0
    while i < len(y) - 1 and y[i + 1] == y[0]:
        i += 1
    if i > 0:
        out[:i + 1] = True
    j = len(y) - 1
    while j > 0 and y[j - 1] == y[-1]:
        j -= 1
    if j < len(y) - 1:
        out[j:] = True
    return out


def plane_summary(version: str) -> pd.DataFrame:
    """Imaging plane names and indicators, and raw series names, of every file at a version."""
    def one(a):
        with open_asset(a["asset_id"]) as f:
            planes = f["general/optophysiology"]
            return {"fish": a["path"].split("/")[0][4:], "version": version,
                    "planes": ", ".join(f"{n} ({_text(planes[n]['indicator'])}, {_text(planes[n]['excitation_lambda'])} nm)"
                                        for n in planes),
                    "raw_series": ", ".join(k for k in f["acquisition"] if "Series" in k),
                    "swim_bouts": f["processing/behavior/SwimIntervals/start_time"].shape[0],
                    "sum_swim_starts": float(f["processing/behavior/SwimIntervals/start_time"][:].sum()),
                    "dfof_series": ", ".join(f"{k} {f['processing/ophys/DfOverF'][k]['data'].shape}"
                                             for k in (f["processing/ophys/DfOverF"] if "ophys" in f["processing"] else []))}
    with ThreadPoolExecutor(6) as ex:
        return pd.DataFrame(list(ex.map(one, [a for a in assets(version) if a["path"].endswith(".nwb")])))


def dfof_sample(asset_id: str, name: str, n_rois: int = 200) -> dict:
    """The first `n_rois` columns of a DfOverF series and of the matching Fluorescence series."""
    with open_asset(asset_id) as f:
        d = f[f"processing/ophys/DfOverF/{name}/data"]
        fl = f[f"processing/ophys/Fluorescence/{name.replace('DfOverF', 'Fluorescence')}/data"]
        return {"dfof": d[:, :n_rois].astype(float), "fluorescence": fl[:, :n_rois].astype(float),
                "dtype": str(d.dtype), "unit": _text(d.attrs["unit"])}
EOF
cd entries/000350-mu-2019 && . $TMPDIR/env/bin/activate && python -c "import fictive"
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\n\nRESULTS = {}\nexec(open(sys.argv[2]).read()) if len(sys.argv) > 2 else None\ndef result(cid):\n    return RESULTS.get(cid, \"**Result: pending.**\")\n\nmd(r\"\"\"\n# Reproducing Mu et al. (2019) from dandiset 000350\n\n**Paper.** Mu Y, Bennett DV, Rubinov M, Narayan S, Yang C-T, Tanimoto M, Mensh BD, Looger LL,\nAhrens MB (2019). Glia accumulate evidence that actions are futile and suppress unsuccessful\nbehavior. *Cell* 178, 27-43. [doi:10.1016/j.cell.2019.05.050](https://doi.org/10.1016/j.cell.2019.05.050).\nThe paper is open access (CC BY-NC-ND). This attempt used its full text (main text and STAR\nMethods); the Supplemental Information was not read.\n\n**Dandiset.** [DANDI:000350](https://dandiarchive.org/dandiset/000350/0.240822.1759), version\n0.240822.1759. The paper cites no dandiset version (it predates the dandiset). Two versions are\npublished, 0.221219.1506 and 0.240822.1759. The later one is pinned: it is the most recent, and\nit corrects the imaging plane of the three files with radial astrocytes only, which the earlier\nversion names `NeuronVolume` (\"for the neuron filter\"). The data the analysis uses (swim bouts,\ncell traces) are the same in both; the data check shows this.\n\n**What the dandiset holds.** 12 light-sheet sessions of paralysed larval zebrafish swimming\nfictively in virtual reality, each with the swim and stimulus signals of the rig, the detected\nswim bouts and a table of behavioural states. Eight files also hold segmented cell traces: 4 of\nneurons and radial astrocytes imaged together, 4 of neurons only. The other 4 hold raw images\nonly. None of the perturbation experiments of Figures 4 to 7 is in it.\n\n**Code.** The paper links its cell segmentation code, https://github.com/mikarubi/segmentation\n(now `voluseg`), read at commit 54d1907b1d911ad6445428f8a79ca44875ed42b1 (27 June 2019, the last\nbefore publication). It holds motion correction, brain masking, cell detection, baseline\nestimation and the first NMF of cell traces (`z6_components.py`), with `censor_tau = [30, 30]`\nand `baseline_tau = 300` s. It holds no behavioural analysis, no passivity detection, no\nclustering of components across fish and no onset analysis, so every choice below on those comes\nfrom the Methods or is made here and stated.\n\n| Claim | Tested here | Data |\n|---|---|---|\n| fig1h-epoch-durations: passive 24.4 s, active 36.1 s, 29 bouts per active epoch | tested | 12 fish |\n| methods-isi: inter-swim interval 1.2 s (closed loop), 1.19 s (active epochs) | tested | 12 fish |\n| fig1j-open-loop-passivity: more passivity in open than closed loop | tested | 12 fish |\n| fig1c-vigor-open-loop-onset: higher vigor after the switch to open loop | tested | 12 fish |\n| fig1i-isi-before-passivity: intervals and vigor rise before passivity | tested | 12 fish |\n| fig2bc-neurons-lower-in-passivity | tested | 8 fish |\n| fig2c-glia-rise-at-passivity | tested | 4 fish |\n| figs2a-open-loop-higher | tested | 8 and 4 fish |\n| fig2h-glia-weaker-closed-loop-pauses | tested | 4 fish |\n| fig2dg-nmf-components | blocked: data missing | |\n| fig2kl-lmo-glia-most-consistent | blocked: metadata insufficient | |\n| fig1k-passive-unresponsive, fig1f-replay | blocked: data missing | |\n| fig4-glia-necessary, fig5-glia-sufficient | blocked: data missing | |\n| fig6a-ne-ramp | blocked: metadata insufficient | |\n| fig6-ne-drives-glia, fig7-ne-mismatch, fig7-glia-accumulate | blocked: data missing | |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport fictive as fv\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nsessions = fv.load_all()\nS = {s[\"fish\"]: s for s in sessions}\nprint(f\"loaded {len(sessions)} files from dandiset {fv.DANDISET_ID} version {fv.DANDISET_VERSION} \"\n      f\"in {time.time() - started:.0f} s\")\n\n# Whole-brain signal: mean DfOverF over an evenly spaced subset of ROI blocks, for every processed\n# series; and, for one fish, a disjoint subset to check that the subset does not matter.\nt0 = time.time()\njobs = [(s, name, 0.0) for s in sessions for name in s[\"imaging\"]]\njobs += [(S[\"20170113-4\"], \"NeuronDfOverF\", 0.5), (S[\"20170228-4\"], \"GliaDfOverF\", 0.5)]\nWB = fv.whole_brain_means(jobs)\nprint(f\"whole-brain signals of {len(WB)} series in {time.time() - t0:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    rows.append({\n        \"fish\": s[\"fish\"], \"subject_id\": s[\"subject\"][\"subject_id\"], \"age\": s[\"subject\"][\"age\"],\n        \"species\": s[\"subject\"][\"species\"], \"start\": s[\"session_start\"][:19],\n        \"minutes\": round(s[\"duration_s\"] / 60, 1),\n        \"planes\": \"; \".join(f\"{n}: {p.get('indicator')} ex {p.get('excitation_lambda')} em {p.get('emission_lambda')}\"\n                            for n, p in s[\"planes\"].items()),\n        \"raw_series\": \"; \".join(f\"{k} {v['shape'][0]} vols ({v['neurodata_type']})\" for k, v in s[\"raw_series\"].items()),\n        \"dfof_series\": \"; \".join(f\"{k} {v['shape']}\" for k, v in s[\"imaging\"].items()) or \"none\",\n        \"bouts\": len(s[\"swims\"]), \"state_rows\": len(s[\"states\"]), \"burst_events\": s[\"n_burst_events\"]})\ninfo = pd.DataFrame(rows)\nprint(info.to_string(index=False))\nprint(\"\\nsession_description (same in all files):\", {s[\"session_description\"] for s in sessions})\nprint(\"Distinct session start times:\", info.start.nunique(), \"of\", len(info))\nkinds = info.dfof_series.map(lambda x: \"neurons and glia\" if \"Glia\" in x and \"Neuron\" in x\n                             else \"neurons\" if \"Neuron\" in x else \"glia\" if \"Glia\" in x else \"raw images only\")\nprint(\"\\nFiles by processed traces:\", kinds.value_counts().to_dict())\nprint(\"Raw-only files and their imaging plane:\", {f: p for f, p, k in zip(info.fish, info.planes, kinds) if k == \"raw images only\"})\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe files hold 12 fish aged 6 to 8 days, as in the Methods (5 to 7 dpf for behaviour, one at P8D).\nThe Methods (Figure 2D and 2E) used 5 fish with neuronal GCaMP6f and 6 with glial GCaMP6f in\nseparate lines. Here the neuron-only GCaMP6f files are 5 (4 with traces, 1 with raw images only),\nand the glia-only GCaMP6f files are 3, all with raw images only. The 4 two-colour files label both\nplanes GCaMP6f, but their glial plane is excited at 561 nm and detected at 660 nm, which is the\njRGECO1b channel of the Methods (Tg(gfap:jRGECO1b); Tg(elavl3:GCaMP6f), the line of Figure 2B\nand 2C). The data disagree with the indicator stated for the glial plane of these files. The raw\nseries are stored as `TwoPhotonSeries` and the archive lists \"two-photon microscopy technique\",\nwhile the Methods describe a one-photon light-sheet microscope.\n\"\"\")\n\ncode(r\"\"\"\nolder = fv.plane_summary(\"0.221219.1506\")\nnewer = fv.plane_summary(fv.DANDISET_VERSION)\nboth = older.merge(newer, on=\"fish\", suffixes=(\"_0.221219\", \"_0.240822\"))\nfor col in [\"planes\", \"raw_series\", \"swim_bouts\", \"sum_swim_starts\", \"dfof_series\"]:\n    same = (both[f\"{col}_0.221219\"] == both[f\"{col}_0.240822\"])\n    print(f\"{col}: same in {same.sum()} of {len(both)} files\")\n    if not same.all():\n        print(both.loc[~same, [\"fish\", f\"{col}_0.221219\", f\"{col}_0.240822\"]].to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nBetween the two published versions, only the names change: the raw series (`TwoPhotonSeries`\nto `NeuronOnePhotonSeries` or `GliaOnePhotonSeries`) and, in the three glia-only files, the imaging\nplane (`NeuronVolume` to `GliaVolume`). Swim bouts and processed traces are the same.\n\"\"\")\n\ncode(r\"\"\"\n# Duplicate recordings: compare bout times between every pair of files.\ndup = []\nfish_list = list(S)\nfor i, a in enumerate(fish_list):\n    for b in fish_list[i + 1:]:\n        x, y = S[a][\"swims\"].start_time.to_numpy(), S[b][\"swims\"].start_time.to_numpy()\n        n = min(len(x), len(y), 200)\n        dup.append({\"a\": a, \"b\": b, \"same_first_200_starts\": bool(np.allclose(x[:n], y[:n])),\n                    \"same_n_samples\": S[a][\"n_samples\"] == S[b][\"n_samples\"]})\ndup = pd.DataFrame(dup)\nprint(\"Pairs of files with the same first bout times:\", int(dup.same_first_200_starts.sum()), \"of\", len(dup))\nprint(\"Pairs with the same number of rig samples:\", int(dup.same_n_samples.sum()))\n\n# Units and ranges of the behavioural data.\nrows = []\nfor s in sessions:\n    sw = s[\"swims\"]\n    rows.append({\"fish\": s[\"fish\"], \"rate_hz\": s[\"rate\"], \"bouts\": len(sw),\n                 \"dur_med_s\": sw.eval(\"stop_time - start_time\").median(), \"width_minus_dur_max\": (sw.width - sw.eval(\"stop_time - start_time\")).abs().max(),\n                 \"power_p5\": sw.power.quantile(0.05), \"power_med\": sw.power.median(), \"power_p95\": sw.power.quantile(0.95),\n                 \"power_zero\": int((sw.power == 0).sum()),\n                 \"gain_values\": np.unique(np.round(s[\"gain\"], 3)).size, \"gain_max\": round(s[\"gain\"].max(), 3),\n                 \"velocity_values\": sorted(set(np.round(s[\"velocity\"], 2))),\n                 \"protocol_codes\": sorted(set(s[\"protocol_code\"].astype(int)))})\nbeh = pd.DataFrame(rows)\nprint(\"\\n\", beh.round(3).to_string(index=False))\nprint(\"\\nStated units:\", sessions[0][\"behavior_units\"])\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nNo two files share bout times or length, so each recording is counted once. Swim bout `width`\nequals stop minus start (in seconds), though the table describes it as \"Estimated width spanned by\nthe swim event\". Swim power and the stimulus signals are in arbitrary units, as stated. In two\nfiles (20170203-1 and 20170228-4) some bouts have a power of exactly 0. The gain signal takes\nvalues from 0 to 0.036 (arbitrary units; the Methods give none for the gain), and the grating's\nbaseline velocity takes 0, 0.5, 1, 1.5 or 2 (arbitrary units, against 2.86 mm/s in the Methods).\nThe first column of `StimulusParameterSignals` holds protocol codes (22/23 closed-loop blocks,\n32/33 prolonged open loop, 51/52/53 alternating blocks); no file describes them, and the analysis\nuses the gain and velocity signals instead.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    m = fv.condition_masks(s)\n    dt = 1 / fv.COND_HZ\n    rows.append({\"fish\": s[\"fish\"], \"closed_loop_s\": m[\"closed\"].sum() * dt, \"open_loop_s\": m[\"open\"].sum() * dt,\n                 \"stationary_gain_on_s\": (m[\"gain_on\"] & ~m[\"closed\"]).sum() * dt,\n                 \"stationary_gain_0_s\": (~m[\"gain_on\"] & ~m[\"open\"]).sum() * dt,\n                 \"closed_periods\": len(fv.segments(s[\"cond_t\"], m[\"closed\"])),\n                 \"open_periods\": len(fv.segments(s[\"cond_t\"], m[\"open\"])),\n                 \"first_open_s\": s[\"cond_t\"][np.argmax(m[\"open\"])]})\ncond = pd.DataFrame(rows)\nprint(\"Time per condition (closed loop: gain above 0, grating moving; open loop: gain 0, grating moving):\")\nprint(cond.round(1).to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nEvery fish has closed-loop time (gain above 0) and open-loop time (gain 0), with the open loop\nfirst starting 3 to 10 minutes into the session, as in the Methods' protocol. Several sessions\nalso alternate closed and open loop later on, and several closed-loop blocks alternate with\nstationary grating.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    st = s[\"states\"]\n    dur = st.stop - st.start\n    act = st[st.type == \"active\"]\n    trans = st[st.type == \"transient\"]\n    same_as_active = trans.merge(act, on=[\"start\", \"stop\"]).shape[0]\n    rows.append({\"fish\": s[\"fish\"], \"rows\": len(st), \"types\": dict(st.type.value_counts()),\n                 \"first_s\": round(st.start.min(), 1), \"last_s\": round(st.stop.max(), 1),\n                 \"first_open_s\": round(cond.set_index(\"fish\").first_open_s[s[\"fish\"]], 1),\n                 \"active_under_5s\": int((act.stop - act.start <= 5).sum()), \"active_rows\": len(act),\n                 \"transient_rows_also_active\": f\"{same_as_active} of {len(trans)}\",\n                 \"passive_under_5s\": int(((st.type == \"passive\") & (dur < 5)).sum())})\nstates = pd.DataFrame(rows)\nprint(states.to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe `ActivityStates` table is described only as \"Classified periods of activity (passive, active,\nor transient)\". It starts at 262 to 1218 s into each session, after the first open loop in some\nfiles and well before it in others, so it covers closed- and open-loop time alike and does not\nsay which. Its \"transient\" rows are not defined in the paper, and in most files every transient row\nis also listed, with the same times, as an active row. Many active rows last 5 s or less, which\nthe Methods' definition of an active epoch excludes. The table is therefore not the Methods'\nclassification as written; the claims use epochs built from the swim bouts by the Methods' rule,\nand the table as a variant.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    for name, im in s[\"imaging\"].items():\n        t = im[\"t\"]\n        ttl = s[\"ttl_volume_starts\"]\n        raw_name = name.replace(\"DfOverF\", \"OnePhotonSeries\")\n        raw_t = s[\"raw_series\"][raw_name][\"t\"]\n        y = WB[(s[\"fish\"], name, 0.0)][0]\n        cens = fv.censored(y)\n        rows.append({\"fish\": s[\"fish\"], \"series\": name, \"volumes\": len(t), \"rois\": im[\"shape\"][1],\n                     \"rois_used\": WB[(s[\"fish\"], name, 0.0)][1], \"dtype_unit\": im[\"unit\"],\n                     \"vol_hz\": round(1 / np.median(np.diff(t)), 2), \"ttl_starts\": len(ttl),\n                     \"t_matches_ttl\": bool(np.allclose(t, ttl[:len(t)], atol=1e-3)),\n                     \"raw_vols\": len(raw_t), \"raw_first_s\": round(raw_t[0], 1), \"dfof_last_s\": round(t[-1], 1),\n                     \"session_s\": round(s[\"duration_s\"], 1),\n                     \"trace_mean\": float(np.mean(y[~cens])), \"censored_start_s\": round(t[np.argmin(cens)] - t[0], 1) if cens[0] else 0.0,\n                     \"censored_end_s\": round(t[-1] - t[len(cens) - 1 - np.argmin(cens[::-1])], 1) if cens[-1] else 0.0})\nimg = pd.DataFrame(rows)\nprint(img.to_string(index=False))\n\nsamples = {k: fv.dfof_sample(S[f][\"asset_id\"], k) for f, k in [(\"20170113-4\", \"NeuronDfOverF\"), (\"20170228-4\", \"GliaDfOverF\")]}\nfor k, d in samples.items():\n    x, F = d[\"dfof\"], d[\"fluorescence\"]\n    print(f\"\\n{k} (first 200 ROIs, stored as {d['dtype']}, unit {d['unit']}): DfOverF median {np.median(x):.4f}, \"\n          f\"range {x.min():.3f} to {x.max():.3f}, per-ROI mean {x.mean(0).min():.4f} to {x.mean(0).max():.4f}\")\n    print(f\"  Fluorescence median {np.median(F):.4f}, range {F.min():.3f} to {F.max():.3f}; \"\n          f\"median absolute change between frames {np.median(np.abs(np.diff(F, axis=0))):.2e} \"\n          f\"(DfOverF {np.median(np.abs(np.diff(x, axis=0))):.2e})\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\n- The imaging timestamps equal the rising edges of the camera trigger (`FrameCaptureTTLSignal`\n  above 3.8), so imaging and behaviour share the rig's clock. In 20170113-2 the trigger has 9751\n  volume starts but the imaging series only 7616: the last 2135 volumes are not in the file.\n- The volume rate is 1.6 to 2.9 Hz, against \"3 volumes/second\" in the Methods; the two-colour\n  sessions are the slowest.\n- In 20170113-4 the raw image series holds 3065 volumes, starting at 3292 s, while the traces\n  cover 12050 volumes from the start; in 20170228-4 the raw series holds 5776 volumes against 7200\n  traces. Raw images are missing for part of these sessions.\n- The series called `DfOverF` is not a ΔF/F as the Methods define it (baseline-subtracted and\n  divided by the baseline, so near 0 at rest). In the single-colour files it is each ROI's trace\n  divided by its mean (every ROI mean is 1, float64); in the two-colour files it is centred near 0\n  (float32) with its first and last frames held constant, as the code's `censor_tau = [30, 30]`\n  does. The two groups were processed differently. The `Fluorescence` series changes by about\n  1e-6 per frame, which is consistent with a slowly varying baseline, not raw fluorescence; its\n  description is the same as that of `DfOverF`. The analysis therefore compares the whole-brain\n  signal only within a fish, against a baseline window or between conditions, and drops the\n  censored frames.\n\"\"\")\n\ncode(r\"\"\"\n# Does the ROI subset matter? Correlate the whole-brain signal from two disjoint subsets.\nfor fish, name in [(\"20170113-4\", \"NeuronDfOverF\"), (\"20170228-4\", \"GliaDfOverF\")]:\n    a, na = WB[(fish, name, 0.0)]\n    b, nb = WB[(fish, name, 0.5)]\n    ok = ~fv.censored(a)\n    print(f\"{fish} {name}: subsets of {na} and {nb} ROIs, correlation {np.corrcoef(a[ok], b[ok])[0, 1]:.3f}\")\n\n# Clock check: whole-brain neuronal signal against the swim rate, with the true bout times and\n# with the bouts shifted by 60 to 600 s (circularly), for every file with neuronal traces.\nrng = np.random.default_rng(0)\nrows = []\nfor s in sessions:\n    if \"NeuronDfOverF\" not in s[\"imaging\"]:\n        continue\n    t = s[\"imaging\"][\"NeuronDfOverF\"][\"t\"]\n    y = WB[(s[\"fish\"], \"NeuronDfOverF\", 0.0)][0]\n    ok = ~fv.censored(y)\n    t, y = t[ok], y[ok]\n    rate = fv.swim_rate(s, t)\n    dt = np.median(np.diff(t))\n    lags = np.arange(-int(10 / dt), int(10 / dt) + 1)\n    def best(r):\n        cc = [np.corrcoef(r[max(0, -l):len(r) - max(0, l)], y[max(0, l):len(y) - max(0, -l)])[0, 1] for l in lags]\n        return np.max(cc), lags[np.argmax(cc)] * dt\n    true_cc, true_lag = best(rate)\n    null = [best(np.roll(rate, int(sh / dt)))[0] for sh in rng.uniform(60, 600, 20) * rng.choice([-1, 1], 20)]\n    rows.append({\"fish\": s[\"fish\"], \"peak_corr\": true_cc, \"peak_lag_s\": true_lag,\n                 \"shifted_max\": np.max(null), \"shifted_median\": np.median(null)})\nclock = pd.DataFrame(rows)\nprint(\"\\nNeuronal whole-brain signal against swim rate (positive lag: signal after swims):\")\nprint(clock.round(3).to_string(index=False))\nprint(\"Files where the true peak correlation exceeds every shifted one:\", int((clock.peak_corr > clock.shifted_max).sum()), \"of\", len(clock))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe whole-brain signal from two disjoint ROI subsets is nearly the same, so the subset stands for\nthe whole brain. In every file with neuronal traces, the neuronal signal follows swimming more\nclosely with the true bout times than with any of 20 shifted copies, with its peak 0.3 to 5 s after\nthe swims, which is consistent with the stated shared clock. The four raw-only files are used\nfor behaviour only, which is on the rig's clock by construction.\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(\"\"\"\n## Epochs used by the claims\n\nPassive and active epochs are built from the swim bouts by the Methods' rule (see `fictive.py`),\nwithin each closed- or open-loop period; epochs cut by a period's edge are left out.\n\"\"\")\n\ncode(r\"\"\"\nEP = {s[\"fish\"]: {c: fv.session_epochs(s, c) for c in [\"closed\", \"open\"]} for s in sessions}\nON = {s[\"fish\"]: fv.passivity_onsets(s) for s in sessions}\nrows = []\nfor f, e in EP.items():\n    rows.append({\"fish\": f, **{f\"{c}_{k}\": sum(len(x[k]) for x in e[c]) for c in [\"closed\", \"open\"] for k in [\"passive\", \"active\"]},\n                 \"passivity_onsets\": len(ON[f])})\nprint(pd.DataFrame(rows).to_string(index=False))\n\"\"\")\n\nmd(\"\"\"\n## fig1h-epoch-durations\n\n> In prolonged open loop, fish cycle between passive epochs lasting 24.4 +/- 2.5 s and active\n> epochs lasting 36.1 +/- 4.2 s (mean +/- SEM, n = 74 fish), swimming 29 +/- 6 times per active\n> epoch.\n\nReadings fixed in the claims file: (a) epochs from the swim bouts in open loop, mean over fish of\neach fish's mean; (b) the dandiset's `ActivityStates` rows; (c) as (a), pooled over epochs.\nTolerances 1.96 SEM: 24.4 +/- 4.9 s, 36.1 +/- 8.2 s, 29 +/- 11.8 bouts.\n\"\"\")\n\ncode(r\"\"\"\nEXPECTED = {\"passive_s\": (24.4, 4.9), \"active_s\": (36.1, 8.2), \"bouts\": (29, 11.8)}\nrows, pooled = [], {\"passive_s\": [], \"active_s\": [], \"bouts\": []}\nfor s in sessions:\n    f = s[\"fish\"]\n    pas = [b - a for x in EP[f][\"open\"] for a, b in x[\"passive\"]]\n    act = [e[\"stop\"] - e[\"start\"] for x in EP[f][\"open\"] for e in x[\"active\"]]\n    nb = [e[\"n_bouts\"] for x in EP[f][\"open\"] for e in x[\"active\"]]\n    st = s[\"states\"]\n    tab = st.assign(d=st.stop - st.start)\n    rows.append({\"fish\": f, \"n_passive\": len(pas), \"passive_s\": np.mean(pas), \"n_active\": len(act), \"active_s\": np.mean(act),\n                 \"bouts\": np.mean(nb), \"table_passive_s\": tab[tab.type == \"passive\"].d.mean(),\n                 \"table_active_s\": tab[tab.type == \"active\"].d.mean(),\n                 \"table_active_over_5s\": tab[(tab.type == \"active\") & (tab.d > 5)].d.mean()})\n    pooled[\"passive_s\"] += pas; pooled[\"active_s\"] += act; pooled[\"bouts\"] += nb\nfig1h = pd.DataFrame(rows)\nprint(fig1h.round(2).to_string(index=False))\n\nreadings = {\n    \"(a) bouts, mean of fish means\": {k: fig1h[k].mean() for k in EXPECTED},\n    \"(b) ActivityStates table, mean of fish means\": {\"passive_s\": fig1h.table_passive_s.mean(), \"active_s\": fig1h.table_active_s.mean(), \"bouts\": np.nan},\n    \"(c) bouts, pooled epochs\": {k: np.mean(v) for k, v in pooled.items()},\n}\nprint()\nfor name, vals in readings.items():\n    ok = {k: abs(vals[k] - EXPECTED[k][0]) <= EXPECTED[k][1] for k in EXPECTED}\n    print(f\"{name}: \" + \"; \".join(f\"{k} {vals[k]:.2f} ({'within' if ok[k] else 'outside'} {EXPECTED[k][0]} +/- {EXPECTED[k][1]})\" for k in EXPECTED)\n          + f\" -> {sum(ok.values())} of 3 within\")\nprint(f\"\\nSEM over fish under (a): passive {fig1h.passive_s.sem():.2f} s, active {fig1h.active_s.sem():.2f} s, bouts {fig1h.bouts.sem():.2f}\")\nprint(f\"Table variant with active rows over 5 s only: active {fig1h.table_active_over_5s.mean():.2f} s\")\nprint(f\"Range over fish (a): passive {fig1h.passive_s.min():.1f} to {fig1h.passive_s.max():.1f} s, active {fig1h.active_s.min():.1f} to {fig1h.active_s.max():.1f} s\")\n\n# Variant: the threshold of 5 s is the paper's; show 4 and 6 s.\nfor gap in [4.0, 6.0]:\n    p, a = [], []\n    for s in sessions:\n        ep = [fv.epochs_in_segment(s[\"swims\"], seg, gap) for seg in fv.segments(s[\"cond_t\"], fv.condition_masks(s)[\"open\"])]\n        p.append(np.mean([y - x for e in ep for x, y in e[\"passive\"]]))\n        a.append(np.mean([e[\"stop\"] - e[\"start\"] for x in ep for e in x[\"active\"]]))\n    print(f\"Pause threshold {gap:.0f} s: passive {np.nanmean(p):.2f} s, active {np.nanmean(a):.2f} s (mean of fish means)\")\n\"\"\", [\"claim:fig1h-epoch-durations\"])\nmd(result(\"fig1h-epoch-durations\"))\n\nmd(\"\"\"\n## methods-isi\n\n> In closed loop fish swim in discrete bouts about once per second (inter-swim interval 1.2 +/-\n> 0.05 s, n = 74), and within active epochs of open loop the interval is 1.19 +/- 0.047 s.\n\nReadings: (a) start to start, (b) end to start; in closed loop (i) intervals under 5 s, (ii) all.\nTolerances 1.96 SEM: 1.2 +/- 0.098 s and 1.19 +/- 0.092 s.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    f = s[\"fish\"]\n    r = {\"fish\": f}\n    for c in [\"closed\"]:\n        ss, ee = [], []\n        for seg in fv.segments(s[\"cond_t\"], fv.condition_masks(s)[c]):\n            w = s[\"swims\"][(s[\"swims\"].start_time >= seg[0]) & (s[\"swims\"].stop_time <= seg[1])].sort_values(\"start_time\")\n            ss += list(np.diff(w.start_time.to_numpy()))\n            ee += list(w.start_time.to_numpy()[1:] - w.stop_time.to_numpy()[:-1])\n        ss, ee = np.array(ss), np.array(ee)\n        r.update({\"closed_a_i\": ss[ee < 5].mean(), \"closed_a_ii\": ss.mean(), \"closed_b_i\": ee[ee < 5].mean(), \"closed_b_ii\": ee.mean(),\n                  \"closed_n\": len(ss)})\n    act = [e for x in EP[f][\"open\"] for e in x[\"active\"]]\n    r[\"active_a\"] = np.mean(np.concatenate([np.diff(e[\"bout_starts\"]) for e in act]))\n    sw = s[\"swims\"].set_index(\"start_time\")\n    gaps = []\n    for e in act:\n        b = s[\"swims\"][(s[\"swims\"].start_time >= e[\"start\"]) & (s[\"swims\"].stop_time <= e[\"stop\"])].sort_values(\"start_time\")\n        gaps += list(b.start_time.to_numpy()[1:] - b.stop_time.to_numpy()[:-1])\n    r[\"active_b\"] = np.mean(gaps)\n    rows.append(r)\nisi = pd.DataFrame(rows)\nprint(isi.round(3).to_string(index=False))\nprint()\nfor cl, op in [(\"closed_a_i\", \"active_a\"), (\"closed_a_ii\", \"active_a\"), (\"closed_b_i\", \"active_b\"), (\"closed_b_ii\", \"active_b\")]:\n    c, o = isi[cl].mean(), isi[op].mean()\n    ok_c, ok_o = abs(c - 1.2) <= 0.098, abs(o - 1.19) <= 0.092\n    print(f\"{cl} / {op}: closed loop {c:.3f} s ({'within' if ok_c else 'outside'} 1.2 +/- 0.098), \"\n          f\"active epochs {o:.3f} s ({'within' if ok_o else 'outside'} 1.19 +/- 0.092); SEM {isi[cl].sem():.3f} and {isi[op].sem():.3f}\")\nprint(f\"\\nRange over fish, closed_a_i {isi.closed_a_i.min():.2f} to {isi.closed_a_i.max():.2f} s; active_a {isi.active_a.min():.2f} to {isi.active_a.max():.2f} s\")\n\"\"\", [\"claim:methods-isi\"])\nmd(result(\"methods-isi\"))\n\nmd(\"\"\"\n## fig1j-open-loop-passivity\n\n> Fish spend much more time in the passive state when swimming produces no visual feedback (open\n> loop) than in closed loop with a naturalistic gain, where passivity is rare.\n\nCriterion: fraction of time in pauses of 5 s or more, open against closed loop, one-sided Wilcoxon\nover fish at p < 0.05, and median closed-loop fraction below 10%.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    f = s[\"fish\"]\n    r = {\"fish\": f}\n    for c in [\"closed\", \"open\"]:\n        tot = sum(x[\"seg\"][1] - x[\"seg\"][0] for x in EP[f][c])\n        r[f\"{c}_s\"] = tot\n        r[f\"{c}_passive_frac\"] = sum(b - a for x in EP[f][c] for a, b in x[\"pauses\"]) / tot\n    # Variant: closed loop before the first open loop only.\n    first_open = cond.set_index(\"fish\").first_open_s[f]\n    pre = [x for x in EP[f][\"closed\"] if x[\"seg\"][1] <= first_open]\n    tot = sum(x[\"seg\"][1] - x[\"seg\"][0] for x in pre)\n    r[\"closed_before_first_open_frac\"] = sum(b - a for x in pre for a, b in x[\"pauses\"]) / tot if tot else np.nan\n    r[\"closed_before_first_open_s\"] = tot\n    rows.append(r)\nfrac = pd.DataFrame(rows)\nprint(frac.round(3).to_string(index=False))\nw = stats.wilcoxon(frac.open_passive_frac, frac.closed_passive_frac, alternative=\"greater\")\nprint(f\"\\nOpen loop: median {frac.open_passive_frac.median():.3f}; closed loop: median {frac.closed_passive_frac.median():.3f}; \"\n      f\"open higher in {(frac.open_passive_frac > frac.closed_passive_frac).sum()} of {len(frac)} fish; Wilcoxon p = {w.pvalue:.3g}\")\nv = frac.dropna(subset=[\"closed_before_first_open_frac\"])\nw2 = stats.wilcoxon(v.open_passive_frac, v.closed_before_first_open_frac, alternative=\"greater\")\nprint(f\"Variant, closed loop before the first open loop: median {v.closed_before_first_open_frac.median():.3f}; \"\n      f\"open higher in {(v.open_passive_frac > v.closed_before_first_open_frac).sum()} of {len(v)} fish; Wilcoxon p = {w2.pvalue:.3g}\")\n# By gain level in closed loop.\nrows = []\nfor s in sessions:\n    m = fv.condition_masks(s)\n    for g in np.unique(np.round(s[\"gain\"][m[\"closed\"]], 3)):\n        mask = m[\"closed\"] & (np.round(s[\"gain\"], 3) == g)\n        segs = fv.segments(s[\"cond_t\"], mask)\n        tot = sum(b - a for a, b in segs)\n        if tot < 60:\n            continue\n        ep = [fv.epochs_in_segment(s[\"swims\"], seg) for seg in segs]\n        rows.append({\"fish\": s[\"fish\"], \"gain\": g, \"seconds\": tot, \"passive_frac\": sum(b - a for e in ep for a, b in e[\"pauses\"]) / tot})\nprint(\"\\nClosed-loop passive fraction by gain level (levels with 60 s or more):\")\nprint(pd.DataFrame(rows).round(3).to_string(index=False))\n\"\"\", [\"claim:fig1j-open-loop-passivity\"])\nmd(result(\"fig1j-open-loop-passivity\"))\n\nmd(\"\"\"\n## fig1c-vigor-open-loop-onset\n\n> When switched from closed to open loop, fish first swim with higher vigor, then stop swimming.\n\nCriterion: per switch, mean power of the bouts from the switch to the first passive epoch over the\nmean power of the closed-loop bouts in the 30 s before; per fish the median log ratio; one-sided\nWilcoxon over fish. Switches with fewer than 3 bouts on either side are left out.\n\"\"\")\n\ncode(r\"\"\"\ndef switch_ratios(s, strict=False):\n    m = fv.condition_masks(s)\n    t = s[\"cond_t\"]\n    sw = s[\"swims\"].sort_values(\"start_time\")\n    out = []\n    switches = t[1:][m[\"closed\"][:-1] & m[\"open\"][1:]]\n    for t0 in switches:\n        before = sw[(sw.start_time >= t0 - 30) & (sw.stop_time <= t0)]\n        before = before[fv.label_at(s, before.start_time.to_numpy()) == 1]\n        if strict and not m[\"closed\"][(t >= t0 - 30) & (t < t0)].all():\n            continue\n        after = sw[sw.start_time >= t0]\n        st, sp = after.start_time.to_numpy(), after.stop_time.to_numpy()\n        if len(st) == 0 or st[0] - t0 >= fv.PASSIVE_GAP_S:\n            out.append({\"t\": t0, \"n_before\": len(before), \"n_after\": 0, \"log_ratio\": np.nan})\n            continue\n        g = np.flatnonzero(st[1:] - sp[:-1] >= fv.PASSIVE_GAP_S)\n        after = after.iloc[:(g[0] + 1) if len(g) else len(st)]\n        after = after[fv.label_at(s, after.start_time.to_numpy()) == 2]\n        ok = len(before) >= 3 and len(after) >= 3 and before.power.mean() > 0\n        out.append({\"t\": t0, \"n_before\": len(before), \"n_after\": len(after),\n                    \"log_ratio\": np.log(after.power.mean() / before.power.mean()) if ok else np.nan})\n    return pd.DataFrame(out)\n\nrows = []\nfor s in sessions:\n    r = switch_ratios(s)\n    rs = switch_ratios(s, strict=True)\n    rows.append({\"fish\": s[\"fish\"], \"switches\": len(r), \"used\": int(r.log_ratio.notna().sum()) if len(r) else 0,\n                 \"median_log_ratio\": r.log_ratio.median() if len(r) else np.nan,\n                 \"strict_used\": int(rs.log_ratio.notna().sum()) if len(rs) else 0,\n                 \"strict_median_log_ratio\": rs.log_ratio.median() if len(rs) else np.nan})\nvig = pd.DataFrame(rows)\nvig[\"median_ratio\"] = np.exp(vig.median_log_ratio)\nprint(vig.round(3).to_string(index=False))\nd = vig.median_log_ratio.dropna()\nw = stats.wilcoxon(d, alternative=\"greater\")\nprint(f\"\\n{len(d)} fish with a usable switch; ratio above 1 in {(d > 0).sum()}; median ratio {np.exp(d.median()):.2f} \"\n      f\"(range {np.exp(d.min()):.2f} to {np.exp(d.max()):.2f}); Wilcoxon p = {w.pvalue:.3g}\")\nds = vig.strict_median_log_ratio.dropna()\nif len(ds) > 1:\n    print(f\"Variant requiring 30 s of closed loop before the switch: {len(ds)} fish, ratio above 1 in {(ds > 0).sum()}, \"\n          f\"median ratio {np.exp(ds.median()):.2f}, Wilcoxon p = {stats.wilcoxon(ds, alternative='greater').pvalue:.3g}\")\n\"\"\", [\"claim:fig1c-vigor-open-loop-onset\"])\nmd(result(\"fig1c-vigor-open-loop-onset\"))\n\nmd(\"\"\"\n## fig1i-isi-before-passivity\n\n> Before the switch to passivity the inter-swim interval increases progressively, and fish swim\n> more vigorously and less frequently in the seconds before passivity.\n\nCriterion: in active epochs of 10 or more bouts that end in passivity (open loop), intervals\nk = 1 (last) to 7 back and bout powers; interval at k = 1 longer than at k = 7 (one-sided\nWilcoxon over fish), negative Spearman correlation of k with the group mean, and the last 3 bouts\nmore powerful than bouts 8 to 10 back (one-sided Wilcoxon).\n\"\"\")\n\ncode(r\"\"\"\ndef before_passivity(min_bouts):\n    rows = []\n    for s in sessions:\n        isis, pws = [], []\n        for x in EP[s[\"fish\"]][\"open\"]:\n            for e in x[\"active\"]:\n                if e[\"followed_by_passive\"] and e[\"n_bouts\"] >= min_bouts:\n                    isis.append(np.diff(e[\"bout_starts\"])[::-1][:7])\n                    pws.append(e[\"bout_powers\"][::-1][:10])\n        if isis:\n            I, P = np.mean(isis, 0), np.mean(pws, 0)\n            rows.append({\"fish\": s[\"fish\"], \"epochs\": len(isis), **{f\"isi_k{k + 1}\": I[k] for k in range(7)},\n                         \"power_last3\": P[:3].mean(), \"power_8to10\": P[7:10].mean()})\n    return pd.DataFrame(rows)\n\ndef judge(df, label):\n    w_isi = stats.wilcoxon(df.isi_k1, df.isi_k7, alternative=\"greater\")\n    means = df[[f\"isi_k{k}\" for k in range(1, 8)]].mean()\n    rho = stats.spearmanr(np.arange(1, 8), means.to_numpy())\n    w_pow = stats.wilcoxon(df.power_last3, df.power_8to10, alternative=\"greater\")\n    print(f\"{label}: {len(df)} fish; mean interval k=1 {df.isi_k1.mean():.3f} s, k=7 {df.isi_k7.mean():.3f} s, \"\n          f\"k=1 longer in {(df.isi_k1 > df.isi_k7).sum()} fish, Wilcoxon p = {w_isi.pvalue:.3g}; \"\n          f\"Spearman rho (k, mean) = {rho.statistic:.3f}; power last 3 {df.power_last3.mean():.3f} against bouts 8-10 back \"\n          f\"{df.power_8to10.mean():.3f}, higher in {(df.power_last3 > df.power_8to10).sum()} fish, Wilcoxon p = {w_pow.pvalue:.3g}\")\n    return means\n\nbp = before_passivity(10)\nprint(bp.round(3).to_string(index=False))\nprint()\nmeans = judge(bp, \"Main (10 or more bouts)\")\nprint(\"Mean interval by k (1 = last):\", means.round(3).to_dict())\njudge(before_passivity(8), \"Variant (8 or more bouts)\")\njudge(before_passivity(15), \"Variant (15 or more bouts)\")\n\"\"\", [\"claim:fig1i-isi-before-passivity\"])\nmd(result(\"fig1i-isi-before-passivity\"))\n\nmd(\"\"\"\n## Signals around passivity onset\n\nThe whole-brain signal of each cell type around each passivity onset, against the baseline 10 to\n5 s before onset (in the units of the stored series; see the data check).\n\"\"\")\n\ncode(r\"\"\"\nLAGS = np.arange(-15, 20.01, 0.5)\nTRACES, rows = {}, []\nfor s in sessions:\n    for name in s[\"imaging\"]:\n        f = s[\"fish\"]\n        t = s[\"imaging\"][name][\"t\"]\n        y = WB[(f, name, 0.0)][0].astype(float)\n        ok = ~fv.censored(y)\n        t, y = t[ok], y[ok]\n        on = ON[f]\n        base = fv.window_mean(t, y, on, fv.BASELINE)\n        E = fv.event_windows(t, y, on, LAGS) - base[:, None]\n        TRACES[(f, name)] = (t, y, on, base, E)\n        rows.append({\"fish\": f, \"series\": name, \"onsets\": len(on), \"trace_sd\": y.std()})\nprint(pd.DataFrame(rows).round(5).to_string(index=False))\n\nfig, axes = plt.subplots(1, 2, figsize=(11, 3.5))\nfor ax, name in zip(axes, [\"NeuronDfOverF\", \"GliaDfOverF\"]):\n    for (f, n), (t, y, on, base, E) in TRACES.items():\n        if n == name:\n            avg = np.nanmean(E, 0) / y.std()\n            ax.plot(LAGS, avg, label=f)\n            print(f\"{name} {f}: onset-triggered mean in SD units ranges {np.nanmin(avg):.2f} to {np.nanmax(avg):.2f}\")\n    ax.axvline(0, color=\"k\", lw=0.5); ax.axhline(0, color=\"k\", lw=0.5)\n    ax.set_xlabel(\"time from passivity onset (s)\"); ax.set_ylabel(\"change from baseline (SD of trace)\")\n    ax.set_title(name.replace(\"DfOverF\", \"\") + \" whole-brain signal\"); ax.legend(fontsize=7)\nplt.tight_layout(); plt.show()\n\"\"\")\n\nmd(\"\"\"\n## fig2bc-neurons-lower-in-passivity\n\n> Whole-brain average neuronal activity is higher during active behavior than during passivity,\n> and decays after passivity onset.\n\nCriterion: per fish, mean neuronal signal over open-loop passive epochs minus that over open-loop\nactive epochs; below 0 by a one-sided Wilcoxon over the 8 fish.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    if \"NeuronDfOverF\" not in s[\"imaging\"]:\n        continue\n    f = s[\"fish\"]\n    t, y, on, base, E = TRACES[(f, \"NeuronDfOverF\")]\n    pas = [p for x in EP[f][\"open\"] for p in x[\"passive\"]]\n    act = [(e[\"start\"], e[\"stop\"]) for x in EP[f][\"open\"] for e in x[\"active\"]]\n    diff = fv.mean_in_intervals(t, y, pas) - fv.mean_in_intervals(t, y, act)\n    late = fv.window_mean(t, y, on, (5, 10)) - base\n    good = np.isfinite(late)\n    rows.append({\"fish\": f, \"passive_minus_active\": diff, \"in_trace_sd\": diff / y.std(), \"onsets\": int(good.sum()),\n                 \"after_5to10_minus_base\": np.nanmean(late), \"p_decrease\": stats.wilcoxon(late[good], alternative=\"less\").pvalue})\nneu = pd.DataFrame(rows)\nprint(neu.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nw = stats.wilcoxon(neu.passive_minus_active, alternative=\"less\")\nprint(f\"\\nPassive below active in {(neu.passive_minus_active < 0).sum()} of {len(neu)} fish; Wilcoxon p = {w.pvalue:.3g}; \"\n      f\"effect {neu.in_trace_sd.min():.2f} to {neu.in_trace_sd.max():.2f} SD of the trace\")\nprint(f\"Decrease 5 to 10 s after onset (p < 0.05 within fish) in {(neu.p_decrease < 0.05).sum()} of {len(neu)} fish\")\n# Variant: ActivityStates rows in place of the Methods' epochs.\nv = []\nfor s in sessions:\n    if \"NeuronDfOverF\" not in s[\"imaging\"]:\n        continue\n    t, y = TRACES[(s[\"fish\"], \"NeuronDfOverF\")][:2]\n    st = s[\"states\"]\n    v.append(fv.mean_in_intervals(t, y, st[st.type == \"passive\"][[\"start\", \"stop\"]].to_numpy())\n             - fv.mean_in_intervals(t, y, st[st.type == \"active\"][[\"start\", \"stop\"]].to_numpy()))\nv = np.array(v)\nprint(f\"Variant with ActivityStates rows: passive below active in {(v < 0).sum()} of {len(v)} fish, Wilcoxon p = {stats.wilcoxon(v, alternative='less').pvalue:.3g}\")\n\"\"\", [\"claim:fig2bc-neurons-lower-in-passivity\"])\nmd(result(\"fig2bc-neurons-lower-in-passivity\"))\n\nmd(\"\"\"\n## fig2c-glia-rise-at-passivity\n\n> Whole-brain average radial astrocyte calcium increases before passivity onset and peaks soon\n> after it.\n\nCriterion: per fish, 1 to 4 s after onset and 2 to 0 s before onset, each against 10 to 5 s\nbefore (one-tailed Wilcoxon over onsets), and the peak of the triggered average between 0 and\n10 s; reproduced when all hold in at least 3 of 4 fish, partially when the after-onset increase\nholds in at least 3.\n\"\"\")\n\ncode(r\"\"\"\ndef onset_tests(f, name, onsets=None):\n    t, y, on, base, E = TRACES[(f, name)]\n    if onsets is not None:\n        on = onsets\n        base = fv.window_mean(t, y, on, fv.BASELINE)\n        E = fv.event_windows(t, y, on, LAGS) - base[:, None]\n    resp = fv.window_mean(t, y, on, fv.RESPONSE) - base\n    pre = fv.window_mean(t, y, on, (-2, 0)) - base\n    good = np.isfinite(resp) & np.isfinite(pre)\n    avg = np.nanmean(E, 0)\n    return {\"fish\": f, \"onsets\": int(good.sum()), \"after_1to4\": np.median(resp[good]) / y.std(),\n            \"p_after\": stats.wilcoxon(resp[good], alternative=\"greater\").pvalue,\n            \"before_2to0\": np.median(pre[good]) / y.std(),\n            \"p_before\": stats.wilcoxon(pre[good], alternative=\"greater\").pvalue,\n            \"peak_lag_s\": LAGS[np.nanargmax(avg)]}\n\nglia = pd.DataFrame([onset_tests(s[\"fish\"], \"GliaDfOverF\") for s in sessions if \"GliaDfOverF\" in s[\"imaging\"]])\nglia[\"after_ok\"] = glia.p_after < 0.05\nglia[\"all_ok\"] = glia.after_ok & (glia.p_before < 0.05) & glia.peak_lag_s.between(0, 10)\nprint(\"Medians in SD units of each fish's trace:\")\nprint(glia.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nprint(f\"\\nAfter-onset increase in {glia.after_ok.sum()} of 4 fish; all three parts in {glia.all_ok.sum()} of 4 fish\")\nprint(\"Onsets per fish:\", glia.set_index(\"fish\").onsets.to_dict(), \"(paper's example fish: 64 events)\")\n\n# Variant: ActivityStates passive rows that start in open loop, as onsets.\nrows = []\nfor s in sessions:\n    if \"GliaDfOverF\" not in s[\"imaging\"]:\n        continue\n    st = s[\"states\"]\n    on = st[st.type == \"passive\"].start.to_numpy()\n    on = on[fv.label_at(s, on) == 2]\n    rows.append(onset_tests(s[\"fish\"], \"GliaDfOverF\", on))\nprint(\"\\nVariant with ActivityStates passive rows in open loop as onsets:\")\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\n# Neurons in the same two-colour fish, for comparison.\nprint(\"\\nNeurons in the two-colour fish, same tests:\")\nprint(pd.DataFrame([onset_tests(s[\"fish\"], \"NeuronDfOverF\") for s in sessions if \"GliaDfOverF\" in s[\"imaging\"]]).to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\n\"\"\", [\"claim:fig2c-glia-rise-at-passivity\"])\nmd(result(\"fig2c-glia-rise-at-passivity\"))\n\nmd(\"\"\"\n## figs2a-open-loop-higher\n\n> Whole-brain average neuronal and glial calcium are higher and fluctuate more strongly in open\n> loop than in closed loop.\n\nCriterion: per fish, mean and SD of the whole-brain signal in open and closed loop, leaving out\n30 s after each switch; neurons by one-sided Wilcoxon over 8 fish, glia in all 4 fish.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (f, name), (t, y, on, base, E) in TRACES.items():\n    s = S[f]\n    lab = fv.label_at(s, t)\n    keep = fv.seconds_since_switch(s, t) >= 30\n    r = {\"fish\": f, \"series\": name}\n    for c, code_ in [(\"closed\", 1), (\"open\", 2)]:\n        sel = keep & (lab == code_)\n        r[f\"{c}_frames\"] = int(sel.sum())\n        r[f\"{c}_mean\"] = y[sel].mean() / y.std()\n        r[f\"{c}_sd\"] = y[sel].std() / y.std()\n    rows.append(r)\ns2a = pd.DataFrame(rows)\ns2a[\"mean_higher_open\"] = s2a.open_mean > s2a.closed_mean\ns2a[\"sd_higher_open\"] = s2a.open_sd > s2a.closed_sd\nprint(\"Means and SDs in units of each fish's whole-trace SD:\")\nprint(s2a.round(3).to_string(index=False))\nfor name in [\"NeuronDfOverF\", \"GliaDfOverF\"]:\n    d = s2a[s2a.series == name]\n    pm = stats.wilcoxon(d.open_mean, d.closed_mean, alternative=\"greater\").pvalue\n    ps = stats.wilcoxon(d.open_sd, d.closed_sd, alternative=\"greater\").pvalue\n    print(f\"{name}: mean higher in open loop in {d.mean_higher_open.sum()} of {len(d)} fish (Wilcoxon p = {pm:.3g}, \"\n          f\"median difference {np.median(d.open_mean - d.closed_mean):.2f} SD); SD higher in {d.sd_higher_open.sum()} of {len(d)} \"\n          f\"(p = {ps:.3g}, median ratio {np.median(d.open_sd / d.closed_sd):.2f})\")\n\"\"\", [\"claim:figs2a-open-loop-higher\"])\nmd(result(\"figs2a-open-loop-higher\"))\n\nmd(\"\"\"\n## fig2h-glia-weaker-closed-loop-pauses\n\n> When fish in closed loop stop swimming because the stimulus stops moving, glial calcium signals\n> are weaker than during futility-induced passivity.\n\nCriterion: closed-loop pauses (5 s or more, starting while the gain is above 0) against open-loop\npassivity onsets, response 1 to 4 s after minus 10 to 5 s before; one-sided Mann-Whitney per fish\nwith 3 or more pauses.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor s in sessions:\n    if \"GliaDfOverF\" not in s[\"imaging\"]:\n        continue\n    f = s[\"fish\"]\n    t, y, on, base, E = TRACES[(f, \"GliaDfOverF\")]\n    r_open = fv.window_mean(t, y, on, fv.RESPONSE) - base\n    cp = fv.closed_loop_pause_onsets(s)\n    r_cl = fv.window_mean(t, y, cp, fv.RESPONSE) - fv.window_mean(t, y, cp, fv.BASELINE)\n    r_open, r_cl = r_open[np.isfinite(r_open)], r_cl[np.isfinite(r_cl)]\n    stationary = np.mean(s[\"velocity\"][np.clip(np.searchsorted(s[\"cond_t\"], cp), 0, len(s[\"cond_t\"]) - 1)] == 0) if len(cp) else np.nan\n    rows.append({\"fish\": f, \"closed_pauses\": len(r_cl), \"share_in_stationary\": stationary, \"open_onsets\": len(r_open),\n                 \"closed_median\": np.median(r_cl) / y.std() if len(r_cl) else np.nan, \"open_median\": np.median(r_open) / y.std(),\n                 \"p\": stats.mannwhitneyu(r_cl, r_open, alternative=\"less\").pvalue if len(r_cl) >= 3 else np.nan})\nh = pd.DataFrame(rows)\nh[\"smaller_median\"] = h.closed_median < h.open_median\nprint(\"Medians in units of each fish's trace SD:\")\nprint(h.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))\nkept = h[h.closed_pauses >= 3]\nprint(f\"\\n{len(kept)} fish with 3 or more closed-loop pauses; pause response smaller with p < 0.05 in {(kept.p < 0.05).sum()}, \"\n      f\"smaller in median in {kept.smaller_median.sum()}\")\n\"\"\", [\"claim:fig2h-glia-weaker-closed-loop-pauses\"])\nmd(result(\"fig2h-glia-weaker-closed-loop-pauses\"))\n\nmd(RESULTS.get(\"summary\", \"## Summary\\n\\npending\"))\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Running the notebook in the scratch environment before locking.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && uv pip install -q nbformat nbconvert ipykernel 2>&1 | tail -1; python $TMPDIR/build_nb.py reproduce_mu_2019.ipynb && time timeout 3000 jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=2400 reproduce_mu_2019.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -20
```

```
[32m     10[39m         [38;5;28;01mif[39;00m isis:
[32m---> [39m[32m11[39m             I, P = np.mean(isis, [32m0[39m), np.mean(pws, [32m0[39m)
[32m     12[39m             rows.append({"fish": s["fish"], "epochs": len(isis), **{f"isi_k{k + 1}": I[k] for k in range(7)},
[32m     13[39m                          [33m"power_last3"[39m: P[:[32m3[39m].mean(), [33m"power_8to10"[39m: P[[32m7[39m:[32m10[39m].mean()})
[32m     14[39m     [38;5;28;01mreturn[39;00m pd.DataFrame(rows)

[36mFile [39m[32m/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/fromnumeric.py:3862[39m, in [36mmean[39m[34m(a, axis, dtype, out, keepdims, where)[39m
[32m   3859[39m     [38;5;28;01melse[39;00m:
[32m   3860[39m         [38;5;28;01mreturn[39;00m mean(axis=axis, dtype=dtype, out=out, **kwargs)
[32m-> [39m[32m3862[39m [38;5;28;01mreturn[39;00m [30;43m_methods[39;49m[30;43m.[39;49m[30;43m_mean[39;49m[30;43m([39;49m[30;43ma[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43maxis[39;49m[30;43m=[39;49m[30;43maxis[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mdtype[39;49m[30;43m=[39;49m[30;43mdtype[39;49m[30;43m,[39;49m
[32m   3863[39m [30;43m                      [39;49m[30;43mout[39;49m[30;43m=[39;49m[30;43mout[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43mkwargs[39;49m[30;43m)[39;49m

[36mFile [39m[32m/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/_methods.py:116[39m, in [36m_mean[39m[34m(a, axis, dtype, out, keepdims, where)[39m
[32m    115[39m [38;5;28;01mdef[39;00m[38;5;250m [39m[34m_mean[39m(a, axis=[38;5;28;01mNone[39;00m, dtype=[38;5;28;01mNone[39;00m, out=[38;5;28;01mNone[39;00m, keepdims=[38;5;28;01mFalse[39;00m, *, where=[38;5;28;01mTrue[39;00m):
[32m--> [39m[32m116[39m     arr = [30;43masanyarray[39;49m[30;43m([39;49m[30;43ma[39;49m[30;43m)[39;49m
[32m    118[39m     is_float16_result = [38;5;28;01mFa
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'
s=open(p).read()
s=s.replace('''                    isis.append(np.diff(e["bout_starts"])[::-1][:7])
                    pws.append(e["bout_powers"][::-1][:10])''','''                    isis.append(np.diff(e["bout_starts"])[::-1][:7])
                    pw = e["bout_powers"][::-1][:10]
                    pws.append(np.r_[pw, np.full(10 - len(pw), np.nan)])''')
s=s.replace('''            I, P = np.mean(isis, 0), np.mean(pws, 0)''','''            I, P = np.mean(isis, 0), np.nanmean(pws, 0)''')
open(p,'w').write(s)
EOF
cd entries/000350-mu-2019 && . $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py reproduce_mu_2019.ipynb && time timeout 3000 jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=2400 reproduce_mu_2019.ipynb --output $TMPDIR/out.ipynb 2>&1 | tail -3
```

```
[NbConvertApp] Converting notebook reproduce_mu_2019.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 262383 bytes to /tmp/claude-1001/out.ipynb

real	9m49.597s
user	2m3.592s
sys	0m18.977s
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import json
nb=json.load(open('/tmp/claude-1001/out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print(f'--- cell {i}'); print(''.join(o['text'])[:7000])
        elif o['output_type']=='error': print(f'!!! cell {i}', o['ename'], o['evalue'])
EOF
```

```
<persisted-output>
Output too large (35.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d2460b76-cf9f-4e58-a635-25e9dd1a3d2c/tool-results/br2biamak.txt

Preview (first 2KB):
--- cell 1
loaded 12 files from dandiset 000350 version 0.240822.1759 in 63 s

--- cell 1
whole-brain signals of 14 series in 419 s

--- cell 3
      fish subject_id age     species               start  minutes                                                                         planes                                                                                           raw_series                                                dfof_series  bouts  state_rows  burst_events
20161022-1 20161022_1 P6D Danio rerio 2016-10-22T15:10:03     58.3                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 8650 vols (TwoPhotonSeries)                                                       none    446           3          5729
20161109-2 20161109_2 P6D Danio rerio 2016-11-09T21:19:50     74.1 GliaVolume: GCaMP6f ex 561.0 em 660.0; NeuronVolume: GCaMP6f ex 488.0 em 537.5 GliaOnePhotonSeries 12500 vols (TwoPhotonSeries); NeuronOnePhotonSeries 12500 vols (TwoPhotonSeries) GliaDfOverF (12500, 100840); NeuronDfOverF (12500, 109918)   2550          80         14122
20161206-1 20161206_1 P6D Danio rerio 2016-12-06T12:35:01     62.3                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 9000 vols (TwoPhotonSeries)                                                       none   1295           3          6261
20161206-2 20161206_2 P6D Danio rerio 2016-12-06T16:11:11     54.7                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 8499 vols (TwoPhotonSeries)        
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d2460b76-cf9f-4e58-a635-25e9dd1a3d2c/tool-results/br2biamak.txt"
}
```

```
1	--- cell 1
2	loaded 12 files from dandiset 000350 version 0.240822.1759 in 63 s
3	
4	--- cell 1
5	whole-brain signals of 14 series in 419 s
6	
7	--- cell 3
8	      fish subject_id age     species               start  minutes                                                                         planes                                                                                           raw_series                                                dfof_series  bouts  state_rows  burst_events
9	20161022-1 20161022_1 P6D Danio rerio 2016-10-22T15:10:03     58.3                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 8650 vols (TwoPhotonSeries)                                                       none    446           3          5729
10	20161109-2 20161109_2 P6D Danio rerio 2016-11-09T21:19:50     74.1 GliaVolume: GCaMP6f ex 561.0 em 660.0; NeuronVolume: GCaMP6f ex 488.0 em 537.5 GliaOnePhotonSeries 12500 vols (TwoPhotonSeries); NeuronOnePhotonSeries 12500 vols (TwoPhotonSeries) GliaDfOverF (12500, 100840); NeuronDfOverF (12500, 109918)   2550          80         14122
11	20161206-1 20161206_1 P6D Danio rerio 2016-12-06T12:35:01     62.3                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 9000 vols (TwoPhotonSeries)                                                       none   1295           3          6261
12	20161206-2 20161206_2 P6D Danio rerio 2016-12-06T16:11:11     54.7                                          GliaVolume: GCaMP6f ex 488.0 em 537.5                                                      GliaOnePhotonSeries 8499 vols (TwoPhotonSeries)                                                       none   1437           3          9094
13	20170111-1 20170111_1 P6D Danio rerio 2017-01-11T12:33:55     64.5                                        NeuronVolume: GCaMP6f ex 
[... 374 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000350-mu-2019 && python - <<'EOF'
p='fictive.py'; s=open(p).read()
old='''def seconds_since_switch(s: dict, t: np.ndarray) -> np.ndarray:
    """For times `t`, the time since the condition label last changed."""
    lab = condition_labels(s)
    changes = s["cond_t"][1:][np.diff(lab) != 0]'''
new='''def seconds_since_switch(s: dict, t: np.ndarray) -> np.ndarray:
    """For times `t`, the time since the last switch between closed and open loop (periods of
    stationary grating carry the label of the condition before them)."""
    lab = pd.Series(condition_labels(s)).replace(0, np.nan).ffill().fillna(0).to_numpy()
    changes = s["cond_t"][1:][np.diff(lab) != 0]'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
old='''                 "first_open_s": s["cond_t"][np.argmax(m["open"])]})'''
new='''                 "first_open_s": fv.segments(s["cond_t"], m["open"])[0][0]})'''
assert old in s; s=s.replace(old,new)
old='''        r[f"{c}_mean"] = y[sel].mean() / y.std()
        r[f"{c}_sd"] = y[sel].std() / y.std()'''
new='''        r[f"{c}_mean"] = (y[sel].mean() - y.mean()) / y.std()
        r[f"{c}_sd"] = y[sel].std() / y.std()'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    pm = stats.wilcoxon(d.open_mean, d.closed_mean, alternative="greater").pvalue
    ps = stats.wilcoxon(d.open_sd, d.closed_sd, alternative="greater").pvalue''','''    d = d.dropna(subset=["closed_mean"])
    pm = stats.wilcoxon(d.open_mean, d.closed_mean, alternative="greater").pvalue
    ps = stats.wilcoxon(d.open_sd, d.closed_sd, alternative="greater").pvalue''')
s=s.replace('''    w_pow = stats.wilcoxon(df.power_last3, df.power_8to10, alternative="greater")''','''    w_pow = stats.wilcoxon(df.power_last3, df.power_8to10, alternative="greater", nan_policy="omit")''')
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && cat > $TMPDIR/a4.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'.')
import fictive as fv
from scipy import stats
S={s['fish']:s for s in pickle.load(open(sys.argv[1],'rb'))}; W=pickle.load(open(sys.argv[2],'rb'))
rows=[]
for (f,name,off),(y,n) in W.items():
    s=S[f]; t=s['imaging'][name]['t']; y=y.astype(float); ok=~fv.censored(y); t,y=t[ok],y[ok]
    lab=fv.label_at(s,t); keep=fv.seconds_since_switch(s,t)>=30
    r={'fish':f,'series':name}
    for c,k in [('closed',1),('open',2)]:
        sel=keep&(lab==k); r[c+'_frames']=int(sel.sum()); r[c+'_mean']=(y[sel].mean()-y.mean())/y.std(); r[c+'_sd']=y[sel].std()/y.std()
    rows.append(r)
d=pd.DataFrame(rows); print(d.round(3).to_string())
for name in ['NeuronDfOverF','GliaDfOverF']:
    x=d[d.series==name].dropna(subset=['closed_mean'])
    print(name, len(x), (x.open_mean>x.closed_mean).sum(), stats.wilcoxon(x.open_mean,x.closed_mean,alternative='greater').pvalue, (x.open_sd>x.closed_sd).sum(), stats.wilcoxon(x.open_sd,x.closed_sd,alternative='greater').pvalue, np.median(x.open_mean-x.closed_mean), np.median(x.open_sd/x.closed_sd))
EOF
timeout 900 python -u $TMPDIR/a4.py $TMPDIR/S.pkl $TMPDIR/W.pkl
```

```
fish         series  closed_frames  closed_mean  closed_sd  open_frames  open_mean  open_sd
0   20161109-2    GliaDfOverF           1643       -0.265      0.842         9262      0.106    0.954
1   20161109-2  NeuronDfOverF           1643       -0.403      0.393         9262      0.057    0.889
2   20170113-2  NeuronDfOverF            746       -0.101      0.291         5557      0.050    1.075
3   20170113-3  NeuronDfOverF           1290       -0.694      0.244         5473      0.242    1.024
4   20170113-4  NeuronDfOverF           2857       -0.494      0.608         4216      0.261    0.934
5   20170127-1  NeuronDfOverF           4542        0.102      0.798         3853      0.072    1.176
6   20170203-1    GliaDfOverF           1244        0.092      1.051         4106     -0.004    0.933
7   20170203-1  NeuronDfOverF           1244       -0.073      1.135         4106     -0.003    0.900
8   20170228-3    GliaDfOverF            213       -1.190      0.117         5477      0.028    0.670
9   20170228-3  NeuronDfOverF            213        0.011      0.251         5477      0.000    1.025
10  20170228-4    GliaDfOverF            356       -0.965      0.181         6085      0.122    0.907
11  20170228-4  NeuronDfOverF            356       -0.141      0.266         6085      0.048    1.023
NeuronDfOverF 8 6 0.01953125 7 0.0078125 0.16981139822048208 2.9758156556211057
GliaDfOverF 4 3 0.125 3 0.1875 0.7291794831736071 3.0647418048851973
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
old_start = s.index('The `ActivityStates` table is described only as')
old_end = s.index('and the table as a variant.\n') + len('and the table as a variant.\n')
s = s[:old_start] + '''The `ActivityStates` table is described only as "Classified periods of activity (passive, active,
or transient)". In the three glia-only files it holds 3 rows; in the others it starts at or after
the first open loop, and in sessions that later alternate closed and open loop it runs through both
without saying which. Its "transient" rows are not defined in the paper, and in every file but
one each transient row is also listed, with the same times, as an active row. Many active rows
last 5 s or less, which the Methods' definition of an active epoch excludes. The table is therefore
not the Methods' classification as written; the claims use epochs built from the swim bouts by
the Methods' rule, and the table as a variant.
''' + s[old_end:]
old = '''  divided by its mean (every ROI mean is 1, float64); in the two-colour files it is centred near 0
  (float32) with its first and last frames held constant, as the code's `censor_tau = [30, 30]`
  does. The two groups were processed differently. The `Fluorescence` series changes by about
  1e-6 per frame, which is consistent with a slowly varying baseline, not raw fluorescence; its
  description is the same as that of `DfOverF`.'''
new = '''  divided by its mean (every ROI mean is 1, float64); in the two-colour files it is centred near 0
  (float32) with its first 60 s held constant, as the code's censoring (`censor_tau`) does. The two
  groups were processed differently. The `Fluorescence` series changes by about 2e-6 per frame in
  the single-colour file and not at all from frame to frame in the median ROI of the two-colour
  file, which is consistent with a slowly varying baseline, not raw fluorescence; its description
  is the same as that of `DfOverF`.'''
assert old in s; s = s.replace(old, new)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results.py",
 "content": "RESULTS[\"fig1h-epoch-durations\"] = \"\"\"**Result: partially reproduced.** Under reading (a), epochs built from the swim bouts in open\nloop, passive epochs last 20.47 s on average over the 12 fish (within 24.4 +/- 4.9) and active\nepochs hold 19.06 bouts (within 29 +/- 11.8), but active epochs last 22.36 s, outside 36.1 +/- 8.2.\nReadings (b), the `ActivityStates` table (18.19 and 15.77 s), and (c), pooled epochs (18.81 s,\n19.66 s, 15.99 bouts), put none of the values within tolerance. Fish differ widely (active epochs\n7.3 to 64.1 s). With a pause threshold of 6 s the means are 21.46 and 25.31 s.\"\"\"\n\nRESULTS[\"methods-isi\"] = \"\"\"**Result: partially reproduced.** Read as start to start, over intervals under 5 s, the\nclosed-loop inter-swim interval is 1.143 s (within 1.2 +/- 0.098), but within active epochs of open\nloop it is 1.332 s, outside 1.19 +/- 0.092. No other reading puts both values within tolerance;\nend-to-start intervals give 0.981 and 0.881 s, and all closed-loop intervals 2.886 s.\"\"\"\n\nRESULTS[\"fig1j-open-loop-passivity\"] = \"\"\"**Result: not reproduced.** Over all closed-loop time the fish spend a median 0.546 of the\ntime in pauses of 5 s or more, against 0.551 in open loop; open loop is higher in 7 of 12 fish\n(Wilcoxon p = 0.285), and the closed-loop median is far above 10%. Much of the closed-loop\npassivity falls in closed-loop blocks that follow open loop, and at some gain levels. Restricted to\nclosed loop before the first open loop (a variant), the median is 0.110 and open loop is higher in\n7 of 9 fish (p = 0.0195).\"\"\"\n\nRESULTS[\"fig1c-vigor-open-loop-onset\"] = \"\"\"**Result: reproduced.** In the 9 fish with a usable switch from closed to open loop, bouts\nafter the switch are more powerful than closed-loop bouts in the 30 s before in 7 fish, with a\nmedian ratio of 3.49 (0.78 to 10.30), Wilcoxon p = 0.0195. Requiring 30 s of uninterrupted closed\nloop before the switch leaves 4 fish (median ratio 4.87, p = 0.125).\"\"\"\n\nRESULTS[\"fig1i-isi-before-passivity\"] = \"\"\"**Result: not reproduced.** In active epochs of 10 or more bouts that end in passivity (11\nfish), the last interval (1.506 s) is longer than the seventh from last (1.312 s) in 8 fish, but\nnot significantly (Wilcoxon p = 0.103), though the mean interval falls with distance from onset\n(Spearman rho = -0.536). The last 3 bouts are not more powerful than bouts 8 to 10 back (0.636\nagainst 0.575, higher in 6 fish, p = 0.16). With epochs of 8 or more bouts (p = 0.00806) or 15 or\nmore (p = 0.00195) the interval part holds; the power part fails in every variant.\"\"\"\n\nRESULTS[\"fig2bc-neurons-lower-in-passivity\"] = \"\"\"**Result: reproduced.** The whole-brain neuronal signal is lower in open-loop passive epochs\nthan in active epochs in all 8 fish (Wilcoxon p = 0.00391), by 0.64 to 1.96 SD of each fish's\ntrace. It falls 5 to 10 s after passivity onset, against the baseline, with p < 0.05 in 7 of 8\nfish. The `ActivityStates` rows give the same (8 of 8).\"\"\"\n\nRESULTS[\"fig2c-glia-rise-at-passivity\"] = \"\"\"**Result: not reproduced.** The whole-brain glial signal rises before passivity onset and\npeaks after it in 2 of the 4 two-colour fish (20170228-3 and 20170228-4: 1 to 4 s after onset\n0.61 and 0.53 SD above baseline, p = 8.0e-13 and 1.1e-14; 2 to 0 s before, p = 1.7e-11 and\n3.6e-17; peaks 3.5 and 2.5 s after onset). In the other two it falls after onset (-0.91 and\n-0.64 SD, p = 1 for an increase). The criterion needed 3 of 4. One of the matching fish has 67\nonsets, close to the 64 events of the paper's example fish. In 20161109-2 the open loop alternates\nwith stationary grating every 10 s, so its onsets mix the two.\"\"\"\n\nRESULTS[\"figs2a-open-loop-higher\"] = \"\"\"**Result: partially reproduced.** For neurons, the whole-brain signal is higher in open than\nclosed loop in 6 of 8 fish (Wilcoxon p = 0.0195) and fluctuates more in 7 of 8 (p = 0.0078,\nmedian SD ratio 2.98). For glia, both hold in 3 of the 4 fish, not in all 4 as the criterion\nrequired; 20170203-1 is the exception.\"\"\"\n\nRESULTS[\"fig2h-glia-weaker-closed-loop-pauses\"] = \"\"\"**Result: not reproduced.** The glial response to closed-loop pauses is smaller than to\nopen-loop passivity onsets in 2 of 4 fish (20170228-3 and 20170228-4, Mann-Whitney p = 1.1e-05\nand 5.0e-11), the two fish whose glia rise at passivity. In the other two, glia fall after\npassivity onset, and the pause response is not smaller (p = 0.78 and 0.98).\"\"\"\n\nRESULTS[\"summary\"] = \"\"\"## Summary\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\n| Claim | Data | Outcome |\n|---|---|---|\n| fig1h-epoch-durations | dandiset, 12 fish | partially reproduced |\n| methods-isi | dandiset, 12 fish | partially reproduced |\n| fig1j-open-loop-passivity | dandiset, 12 fish | not reproduced |\n| fig1c-vigor-open-loop-onset | dandiset, 9 fish | reproduced |\n| fig1i-isi-before-passivity | dandiset, 11 fish | not reproduced |\n| fig2bc-neurons-lower-in-passivity | dandiset, 8 fish | reproduced |\n| fig2c-glia-rise-at-passivity | dandiset, 4 fish | not reproduced |\n| figs2a-open-loop-higher | dandiset, 8 and 4 fish | partially reproduced |\n| fig2h-glia-weaker-closed-loop-pauses | dandiset, 4 fish | not reproduced |\n| fig2dg-nmf-components | | blocked: data missing |\n| fig2kl-lmo-glia-most-consistent | | blocked: metadata insufficient |\n| fig1k-passive-unresponsive | | blocked: data missing |\n| fig1f-replay | | blocked: data missing |\n| fig4-glia-necessary | | blocked: data missing |\n| fig5-glia-sufficient | | blocked: data missing |\n| fig6a-ne-ramp | | blocked: metadata insufficient |\n| fig6-ne-drives-glia | | blocked: data missing |\n| fig7-ne-mismatch | | blocked: data missing |\n| fig7-glia-accumulate | | blocked: data missing |\n\n**How the analysis differs from the paper's.**\n\n- The behavioural claims use the 12 imaged fish; the paper's behavioural numbers come from 74\n  (61 for Figure 1I). The Methods' epoch rule is applied to the dandiset's swim bouts, with\n  pauses measured from the end of one bout to the start of the next; the dandiset's own state\n  table is shown as a variant.\n- Closed and open loop are read from the gain signal, and stationary-grating time is left out;\n  the protocol codes in the files have no description.\n- The cell traces are used as stored. They are not ΔF/F as the Methods define it, and the two\n  groups of files were processed differently, so every imaging comparison is made within a fish\n  and scaled by the SD of that fish's trace.\n- The whole-brain signal is the mean over about 8 to 18% of ROIs (8 evenly spaced blocks); two\n  disjoint subsets agree (correlation 0.981 and 0.998).\n- The paper's glial claims rest on NMF components clustered across fish and registered to a\n  template, mostly in a lateral hindbrain region (L-MO); here only the whole-brain average is\n  tested, as the paper shows for its two-colour example fish (Figure 2C).\n- Glia were tested in the 4 two-colour fish, whose glia carry jRGECO1b; the paper's NMF analysis\n  used 6 fish with glial GCaMP6f, of which the dandiset holds 3 without processed traces.\n\n**What was found about the dandiset.**\n\n- It holds the 12 imaging sessions of the paper's Figure 2 and related panels, with behaviour,\n  but none of the perturbation, NE imaging or probabilistic-feedback experiments of Figures 4 to 7.\n- Four files have raw images only; three of them are the only glia-only GCaMP6f recordings.\n- The glial plane of the two-colour files is labelled GCaMP6f but excited at 561 nm and detected\n  at 660 nm (jRGECO1b). The raw images are typed `TwoPhotonSeries` from a light-sheet microscope.\n- The `DfOverF` series are not ΔF/F (mean-normalised in 4 files, zero-centred and partly censored\n  in the other 4), and the `Fluorescence` series look like baselines, with the same description.\n- Imaging is missing for part of three sessions (20170113-2: 2135 of 9751 triggered volumes;\n  raw images of 20170113-4 and 20170228-4).\n- The `ActivityStates` table is undocumented, does not follow the Methods' definition (active rows\n  of 5 s or less, transient rows duplicating active rows) and has 3 rows in the glia-only files.\n- The protocol codes, gain and velocity signals carry no units or descriptions.\n\"\"\"\n"
}
```

```
File created successfully at: /tmp/claude-1001/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/about 8 to 18% of ROIs/about 8 to 15% of ROIs/' /tmp/claude-1001/results.py
cd entries/000350-mu-2019
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000350-mu-2019
type: reproduction
title: Futility-induced passivity and whole-brain neuronal and glial activity in zebrafish (Mu et al. 2019)
description: Tests the findings of Mu, Bennett, Rubinov et al. (2019) that dandiset 000350 can test.
  The dandiset holds 12 light-sheet sessions of paralysed larval zebrafish swimming fictively in
  virtual reality, with swim bouts, stimulus signals and, in 8 of them, segmented neuronal or
  neuronal and glial traces. The entry measures passive and active epochs, swim intervals and vigor
  in closed and open loop, and whole-brain neuronal and glial activity around passivity onset. The
  perturbation and noradrenergic imaging experiments of Figures 4 to 7 are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_mu_2019.ipynb
  title: Reproducing Mu et al. (2019) from dandiset 000350
  runtime_minutes: 11
helpers:
- fictive.py
related:
- id: dandi:000350/0.240822.1759
  relation: uses_data
- id: doi:10.1016/j.cell.2019.05.050
  relation: reproduces
EOF
printf "h5py\nmatplotlib\nnumpy\npandas\nremfile\nrequests\nscipy\n" > requirements.in
. $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py reproduce_mu_2019.ipynb $TMPDIR/results.py && cd ../.. && python tools/entry.py lock entries/000350-mu-2019 2>&1 | tail -3 && python tools/entry.py check entries/000350-mu-2019 2>&1 | tail -10
```

```
wrote entries/000350-mu-2019/requirements.lock.txt
0 error(s)
```

**Agent**

Checks pass. Running the full lock-check-run from a clean environment (about 11 minutes).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000350-mu-2019 2>&1 | tail -15; ls executed/000350-mu-2019/
```

```
Installed kernelspec registry-000350-mu-2019 in executed/000350-mu-2019/.venv/share/jupyter/kernels/registry-000350-mu-2019
0 error(s)
pass  reproduce_mu_2019.ipynb  (599 s)

real	10m7.319s
user	2m15.713s
sys	0m21.031s
reproduce_mu_2019.ipynb
result.json
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000350-mu-2019/reproduce_mu_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    if i in (1,) or any(t.startswith('claim:') for t in tags) or i==9:
        for o in c.get('outputs',[]):
            if o['output_type']=='stream': print(f'--- cell {i} {tags}'); print(''.join(o['text'])[-2500:])
            elif o['output_type']=='error': print('ERR', o['evalue'])
EOF
```

```
--- cell 1 []
loaded 12 files from dandiset 000350 version 0.240822.1759 in 65 s

--- cell 1 []
whole-brain signals of 14 series in 424 s

--- cell 9 ['sanity']
Time per condition (closed loop: gain above 0, grating moving; open loop: gain 0, grating moving):
      fish  closed_loop_s  open_loop_s  stationary_gain_on_s  stationary_gain_0_s  closed_periods  open_periods  first_open_s
20161022-1          530.5       2779.4                 190.8                  0.0               8             2         360.7
20161109-2          666.8       3352.4                 144.7                282.4              10            29         565.6
20161206-1          828.4       2296.1                 612.3                  0.0              50             2         601.1
20161206-2          753.4       1983.4                 544.9                  0.0              48             2         601.1
20170111-1         1360.0       2511.1                   0.0                  0.0              20            19         180.4
20170113-2          864.8       3990.7                   0.0                  0.0              14            14         300.6
20170113-3         1040.5       2571.3                   0.0                  0.0              19            19         300.6
20170113-4         1944.5       2619.7                   0.0                  0.1              30            32         193.1
20170127-1         1775.8       1501.8                 727.7                  0.1              68             3        1217.6
20170203-1         1006.9       2121.8                 213.6                  0.0              17            17         601.1
20170228-3          192.3       3306.4                  82.2                  0.0              15             2         250.0
[... 204 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/results.py'; s=open(p).read()
old='''closed loop before the first open loop (a variant), the median is 0.110 and open loop is higher in
7 of 9 fish (p = 0.0195)."""'''
new='''closed loop before the first open loop (a variant), the median is 0.104 and open loop is higher in
8 of 10 fish (p = 0.0137)."""'''
assert old in s; s=s.replace(old,new)
old='''against 0.575, higher in 6 fish, p = 0.16). With epochs of 8 or more bouts (p = 0.00806) or 15 or
more (p = 0.00195) the interval part holds; the power part fails in every variant."""'''
new='''against 0.575, higher in 6 fish, p = 0.16). The outcome depends on the minimum epoch length,
which the paper does not state: with epochs of 8 or more bouts both parts hold (intervals
p = 0.00806, rho = -0.286; power p = 0.0269), and with 15 or more the interval part holds
(p = 0.00195) and the power part does not (p = 0.423)."""'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
old='''Every fish has closed-loop time (gain above 0) and open-loop time (gain 0), with the open loop
first starting 3 to 10 minutes into the session, as in the Methods' protocol.'''
new='''Every fish has closed-loop time (gain above 0) and open-loop time (gain 0), with the open loop
first starting 3 to 20 minutes into the session.'''
assert old in s; s=s.replace(old,new)
old='''Its "transient" rows are not defined in the paper, and in every file but
one each transient row is also listed, with the same times, as an active row.'''
new='''Its "transient" rows are not defined in the paper, and in the files with more
than 3 rows all of them, or all but one, are also listed with the same times as active rows.'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd entries/000350-mu-2019 && . $TMPDIR/env/bin/activate && python $TMPDIR/build_nb.py reproduce_mu_2019.ipynb $TMPDIR/results.py && deactivate && cd ../.. && time python tools/entry.py all entries/000350-mu-2019 2>&1 | tail -3
```

```
Installed kernelspec registry-000350-mu-2019 in executed/000350-mu-2019/.venv/share/jupyter/kernels/registry-000350-mu-2019
0 error(s)
pass  reproduce_mu_2019.ipynb  (609 s)

real	10m18.292s
user	2m14.727s
sys	0m20.667s
```

**Agent**

Run passed in 609 s. Spot-checking that the numbers the conclusions quote are unchanged.

**Agent calls Bash**

```bash
python - <<'EOF'
import json,re
nb=json.load(open('executed/000350-mu-2019/reproduce_mu_2019.ipynb'))
txt='\n'.join(''.join(o.get('text','')) for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]))
for pat in ['Files where the true peak','-> \\d of 3 within','within 1.2','Wilcoxon p = 0.285','before the first open loop: median','9 fish with a usable','Main \\(10','Variant \\(8','Passive below active in','After-onset increase','NeuronDfOverF: mean higher','GliaDfOverF: mean higher','4 fish with 3 or more','correlation 0.9']:
    for l in txt.splitlines():
        if re.search(pat,l): print(l[:260])
EOF
```

```
Files where the true peak correlation exceeds every shifted one: 8 of 8
(a) bouts, mean of fish means: passive_s 20.47 (within 24.4 +/- 4.9); active_s 22.36 (outside 36.1 +/- 8.2); bouts 19.06 (within 29 +/- 11.8) -> 2 of 3 within
(b) ActivityStates table, mean of fish means: passive_s 18.19 (outside 24.4 +/- 4.9); active_s 15.77 (outside 36.1 +/- 8.2); bouts nan (outside 29 +/- 11.8) -> 0 of 3 within
(c) bouts, pooled epochs: passive_s 18.81 (outside 24.4 +/- 4.9); active_s 19.66 (outside 36.1 +/- 8.2); bouts 15.99 (outside 29 +/- 11.8) -> 0 of 3 within
closed_a_i / active_a: closed loop 1.143 s (within 1.2 +/- 0.098), active epochs 1.332 s (outside 1.19 +/- 0.092); SEM 0.074 and 0.100
Open loop: median 0.551; closed loop: median 0.546; open higher in 7 of 12 fish; Wilcoxon p = 0.285
Variant, closed loop before the first open loop: median 0.104; open higher in 8 of 10 fish; Wilcoxon p = 0.0137
9 fish with a usable switch; ratio above 1 in 7; median ratio 3.49 (range 0.78 to 10.30); Wilcoxon p = 0.0195
Main (10 or more bouts): 11 fish; mean interval k=1 1.506 s, k=7 1.312 s, k=1 longer in 8 fish, Wilcoxon p = 0.103; Spearman rho (k, mean) = -0.536; power last 3 0.636 against bouts 8-10 back 0.575, higher in 6 fish, Wilcoxon p = 0.16
Variant (8 or more bouts): 12 fish; mean interval k=1 1.502 s, k=7 1.249 s, k=1 longer in 10 fish, Wilcoxon p = 0.00806; Spearman rho (k, mean) = -0.286; power last 3 0.692 against bouts 8-10 back 0.539, higher in 7 fish, Wilcoxon p = 0.0269
Passive below active in 8 of 8 fish; Wilcoxon p = 0.00391; effect -1.96 to -0.64 SD of the trace
After-onset increase in 2 of 4 fish; all three parts in 2 of 4 fish
NeuronDfOverF: mean higher in open loop in 6 of 8 fish (Wilcoxon p = 0.0195, median difference 0.17 SD); SD higher in 7 of 8 (p = 0.00781, median ratio 2.98)
GliaDfOverF: mean higher in open loop in 3 of 4 fish (Wilcoxon p = 0.125, median difference 0.73 SD); SD higher in 3 of 4 (p = 0.188, median ratio 3.06)
4 fish with 3 or more closed-
[... 2 more lines not kept]
```

**Agent**

Conclusions match the executed outputs. Writing the README and the attempt record.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(s['required']);print(list(s['properties']));o=s['properties']['outcomes']['items'];print(o.get('required'),list(o['properties']))
print(json.dumps(s['properties'].get('inputs'))[:600])"
```

```
['schema_version', 'id', 'dandiset', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'dandiset', 'dandiset_version', 'paper', 'date', 'entry', 'provenance', 'outcomes', 'verifications', 'findings', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'proposed']
{"description": "Everything the attempt used that is not in the dandiset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
```

**Agent calls Write**

```json
{
 "file_path": "entries/000350-mu-2019/README.md",
 "content": "# Mu, Bennett, Rubinov et al. (2019) from dandiset 000350\n\nTests the findings of [Mu et al. (2019)](https://doi.org/10.1016/j.cell.2019.05.050) that can be\ntested on [DANDI:000350](https://dandiarchive.org/dandiset/000350/0.240822.1759), which holds 12\nlight-sheet sessions of paralysed larval zebrafish swimming fictively in virtual reality: swim and\nstimulus signals for all 12, and segmented cell traces for 8 (4 of neurons and radial astrocytes,\n4 of neurons only). The perturbation, noradrenergic imaging and probabilistic-feedback experiments\nof Figures 4 to 7 are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Passive and active epochs in open loop last 24.4 and 36.1 s, with 29 bouts per active epoch | Partially reproduced |\n| Inter-swim interval 1.2 s in closed loop and 1.19 s in active epochs | Partially reproduced |\n| Fish are passive more in open loop than in closed loop | Not reproduced |\n| Swim vigor rises after the switch to open loop | Reproduced |\n| Intervals and vigor rise before passivity | Not reproduced |\n| Whole-brain neuronal activity is lower during passivity | Reproduced |\n| Whole-brain glial calcium rises before and peaks after passivity onset | Not reproduced |\n| Neuronal and glial calcium are higher and fluctuate more in open loop | Partially reproduced |\n| Glial calcium is weaker at closed-loop pauses than at futility-induced passivity | Not reproduced |\n| NMF components and the L-MO astrocytes (Figure 2D to 2G, 2K, 2L) | Blocked: data missing, metadata insufficient |\n| Neuronal ramp overlapping NE-MO (Figure 6A) | Blocked: metadata insufficient |\n| Figures 1F, 1K, 4, 5, 6B to 6N and 7 (eight claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/000350-mu-2019-01.yaml`](../../attempts/000350-mu-2019-01.yaml).\n\n- `reproduce_mu_2019.ipynb`: the analysis. It takes about ten minutes, most of it reading cell\n  traces from a subset of ROIs.\n- `fictive.py`: loading the files, the closed- and open-loop conditions, passive and active epochs\n  by the Methods' rule, and the whole-brain signal. Other notebooks on this dandiset can import it.\n"
}
```

```
File created successfully at: entries/000350-mu-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000350-mu-2019-01.yaml",
 "content": "schema_version: 1\nid: 000350-mu-2019-01\ndandiset: \"000350\"\ndandiset_version: 0.240822.1759\npaper: doi:10.1016/j.cell.2019.05.050\ndate: 2026-10-17\nentry: 000350-mu-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-7\ninputs:\n- what: The paper's cell segmentation code, read (not run) to interpret the stored traces; its\n    censoring of the first and last frames (censor_tau = [30, 30]) and baseline settings\n    (baseline_tau = 300 s). No data or parameters from it enter a result.\n  source: https://github.com/mikarubi/segmentation at commit 54d1907b1d911ad6445428f8a79ca44875ed42b1\noutcomes:\n- claim: fig1h-epoch-durations\n  outcome: partially_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig1h-epoch-durations\n  measured:\n  - 20.47\n  - 22.36\n  - 19.06\n  notes: Under reading (a), epochs from the swim bouts in open loop, the mean over 12 fish is 20.47 s\n    for passive epochs (within 24.4 +/- 4.9) and 19.06 bouts per active epoch (within 29 +/- 11.8),\n    but 22.36 s for active epochs (outside 36.1 +/- 8.2). Reading (b), the ActivityStates table,\n    gives 18.19 and 15.77 s; reading (c), pooled epochs, 18.81 s, 19.66 s and 15.99 bouts; neither\n    puts any value within tolerance. Active epochs range from 7.3 to 64.1 s over fish. With a pause\n    threshold of 6 s the means are 21.46 and 25.31 s.\n  deviations:\n  - 12 imaged fish, where the paper's numbers come from 74.\n  - Pauses are measured from the end of one bout to the start of the next; the Methods say only\n    that the fish did not swim for 5 s.\n  - Open loop is read from the gain signal (gain 0, grating moving); epochs cut by the edges of an\n    open-loop period are left out, as the protocol alternates closed and open loop in 8 fish.\n  - The tolerance is 1.96 times the stated SEM, not the SEM.\n- claim: methods-isi\n  outcome: partially_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:methods-isi\n  measured:\n  - 1.143\n  - 1.332\n  notes: Read as start to start over intervals under 5 s, the closed-loop interval is 1.143 s (within\n    1.2 +/- 0.098) and the interval within open-loop active epochs is 1.332 s (outside 1.19 +/-\n    0.092). End-to-start intervals give 0.981 and 0.881 s, and all closed-loop intervals 2.886 s\n    (start to start); no reading puts both values within tolerance.\n  deviations:\n  - The paper does not say how the interval is measured or which closed-loop intervals count; four\n    readings are shown and one matches the closed-loop value.\n  - 12 fish, against 74.\n- claim: fig1j-open-loop-passivity\n  outcome: not_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig1j-open-loop-passivity\n  notes: Over all closed-loop time the median fraction of time in pauses of 5 s or more is 0.546,\n    against 0.551 in open loop; open loop is higher in 7 of 12 fish (Wilcoxon p = 0.285), and the\n    closed-loop median is far above the 10% the criterion allowed. Closed-loop passivity is high in\n    blocks that follow open loop and at some gain levels (for example 0.937 at gain 0.030 in\n    20170127-1). Restricted to closed loop before the first open loop, a variant, the median is\n    0.104 and open loop is higher in 8 of 10 fish (p = 0.0137).\n  deviations:\n  - The paper's Figure 1J varies the gain in 6 dedicated fish; here closed loop is all time with gain\n    above 0 in the imaging sessions, which includes closed-loop blocks between open-loop blocks.\n- claim: fig1c-vigor-open-loop-onset\n  outcome: reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig1c-vigor-open-loop-onset\n  notes: In 9 fish with a usable switch, bouts after the switch to open loop are more powerful than the\n    closed-loop bouts of the 30 s before in 7, median ratio 3.49 (0.78 to 10.30), Wilcoxon p = 0.0195.\n    Requiring 30 s of uninterrupted closed loop before the switch leaves 4 fish (median ratio 4.87,\n    p = 0.125). 3 fish have no usable switch.\n  deviations:\n  - The paper shows this with example traces; the measure (power ratio of bouts) and its test were\n    fixed here before the analysis.\n- claim: fig1i-isi-before-passivity\n  outcome: not_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig1i-isi-before-passivity\n  notes: In active epochs of 10 or more bouts ending in passivity (11 fish), the last interval (1.506 s)\n    is longer than the seventh from last (1.312 s) in 8 fish, Wilcoxon p = 0.103, Spearman rho of k\n    against the mean -0.536. The last 3 bouts are not more powerful than bouts 8 to 10 back (0.636\n    against 0.575, 6 fish, p = 0.16). The outcome depends on the minimum epoch length, which the\n    paper does not state; with 8 or more bouts both parts hold (p = 0.00806, rho = -0.286; power\n    p = 0.0269), and with 15 or more the interval part holds (p = 0.00195) and the power part does\n    not (p = 0.423).\n  deviations:\n  - The minimum of 10 bouts per epoch and the comparison of k = 1 with k = 7 were chosen here; the\n    paper plots the interval against the number of swims before passivity for 61 fish.\n- claim: fig2bc-neurons-lower-in-passivity\n  outcome: reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig2bc-neurons-lower-in-passivity\n  notes: The whole-brain neuronal signal is lower in open-loop passive epochs than in active epochs in\n    all 8 fish (Wilcoxon p = 0.00391), by 0.64 to 1.96 SD of each fish's trace, and falls 5 to 10 s\n    after passivity onset with p < 0.05 in 7 of 8 fish. The ActivityStates rows give 8 of 8.\n  deviations:\n  - The whole-brain signal is the mean of the stored DfOverF over 8 to 15% of ROIs, in units of the\n    stored series, which is not ΔF/F as the Methods define it.\n  - The paper shows this in one example fish; it was tested here over 8.\n- claim: fig2c-glia-rise-at-passivity\n  outcome: not_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig2c-glia-rise-at-passivity\n  notes: The whole-brain glial signal rises before passivity onset and peaks after it in 2 of 4\n    two-colour fish (20170228-3 and 20170228-4; 1 to 4 s after onset 0.61 and 0.53 SD above\n    baseline, p = 8.0e-13 and 1.1e-14; 2 to 0 s before, p = 1.7e-11 and 3.6e-17; peaks 3.5 and\n    2.5 s after onset). In 20161109-2 and 20170203-1 it falls after onset (-0.91 and -0.64 SD,\n    p = 1 for an increase). The criterion needed 3 of 4. 20170228-3 has 67 onsets, close to the 64\n    events of the paper's example fish (Figure 2B), so it may be that fish. In 20161109-2 the open\n    loop alternates with a stationary grating every 10 s. The ActivityStates variant gives the same\n    split.\n  deviations:\n  - Whole-brain average of glia, as in the paper's Figure 2C, not the L-MO component of Figure 2G\n    and 2I, which needs the cross-fish clustering and template registration.\n  - The glia of these fish carry jRGECO1b; the paper's component analysis used GCaMP6f.\n- claim: figs2a-open-loop-higher\n  outcome: partially_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:figs2a-open-loop-higher\n  notes: For neurons the whole-brain signal is higher in open than closed loop in 6 of 8 fish (Wilcoxon\n    p = 0.0195, median difference 0.17 SD) and fluctuates more in 7 of 8 (p = 0.00781, median SD\n    ratio 2.98). For glia both hold in 3 of 4 fish (median difference 0.73 SD, SD ratio 3.06), not in\n    all 4 as the criterion required; 20170203-1 is the exception for both.\n  deviations:\n  - Figure S2A was not read; the claim is taken from the Results text.\n  - Switches are those between closed and open loop; stationary-grating periods carry the label of\n    the condition before them.\n- claim: fig2h-glia-weaker-closed-loop-pauses\n  outcome: not_reproduced\n  notebook: reproduce_mu_2019.ipynb\n  output: claim:fig2h-glia-weaker-closed-loop-pauses\n  notes: The glial response to closed-loop pauses is smaller than to open-loop passivity onsets in 2 of\n    4 fish (20170228-3 and 20170228-4, Mann-Whitney p = 1.1e-05 and 5.0e-11), the two whose glia rise\n    at passivity. In 20161109-2 and 20170203-1 the glia fall after passivity onset, and the pause\n    response is not smaller (p = 0.78 and 0.98). 26 to 54% of the pauses start during a stationary\n    grating.\n  deviations:\n  - Closed-loop pauses include those with the grating moving, as the dandiset gives no stimulus\n    labels beyond the velocity signal and stationary periods are 2 to 18 s long.\n- claim: fig2dg-nmf-components\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The paper's glial components come from 6 fish with glial GCaMP6f; the dandiset holds 3 such\n    fish, with raw images only (8499 to 9000 volumes of about 2 GB each, 0.39 to 0.42 TB per file),\n    and no processed traces. Repeating the segmentation on them does not fit the time limit\n    (too_large). The clustering of components across fish was tuned by hand and the registration\n    template is not public (methods_underspecified).\n- claim: fig2kl-lmo-glia-most-consistent\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The ROIs have voxel masks in each fish's own image space, with no registration to a reference\n    brain, no region labels and no stated orientation of the axes, so L-MO cannot be located\n    without the paper's template.\n- claim: fig1k-passive-unresponsive\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The protocol of brief static and forward stimuli (11 fish) is not in any session; the\n    protocol codes in the files are 12, 22, 23, 32, 33, 51, 52 and 53, and none has the brief\n    stimuli.\n- claim: fig1f-replay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No session replays recorded visual motion; no separate behavioural dataset is on the archive.\n- claim: fig4-glia-necessary\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The ablation, nitroreductase and xestospongin experiments are not in the dandiset, and no\n    other dandiset of this paper was found on the archive.\n- claim: fig5-glia-sufficient\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The TRPV1, CoChR, Opto-alpha1-AR and GABAergic activation experiments are not in the dandiset.\n- claim: fig6a-ne-ramp\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The neuronal traces are there (4 fish with processed GCaMP6f traces of the paper's 5), but\n    locating NE-MO needs the registration to a reference brain and the noradrenergic labels, neither\n    of which is in the files.\n- claim: fig6-ne-drives-glia\n  outcome: blocked\n  blocked_by: data_missing\n  notes: No session images noradrenergic neurons (Tg(th-P2A-Gal4); Tg(UAS:GCaMP6s)) or stimulates NE-MO,\n    and the ablation and pharmacology experiments are not in the dandiset.\n- claim: fig7-ne-mismatch\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The randomised-gain mismatch protocol and the NE-MO imaging are not in the dandiset.\n- claim: fig7-glia-accumulate\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The protocols with 1 to 16 failed bouts and with probabilistic feedback (14 fish) are not in\n    any session.\nfindings:\n- kind: data_missing\n  statement: The dandiset holds the 12 light-sheet sessions behind Figure 2 and its supplement, with\n    behaviour, but none of the perturbation, noradrenergic imaging, mismatch or probabilistic-feedback\n    experiments of Figures 1F, 1K and 4 to 7, nor the behavioural recordings of the other 62 of the\n    74 fish of Figure 1. No other dandiset of the paper was found.\n- kind: data_missing\n  statement: Four files have raw images only and no cell traces, among them the only three\n    glia-only GCaMP6f recordings (the paper's glial NMF used 6). Raw images are missing for part of\n    20170113-4 (3065 of 12050 volumes) and 20170228-4 (5776 of 7200), and 20170113-2 holds 7616\n    imaging volumes against 9751 camera triggers.\n- kind: metadata_error\n  statement: The glial imaging plane of the four two-colour files is labelled GCaMP6f but excited at\n    561 nm and detected at 660 nm, the jRGECO1b channel of the Methods (Tg(gfap:jRGECO1b)). The raw\n    images are typed TwoPhotonSeries and the archive lists two-photon microscopy, though the\n    microscope is a one-photon light sheet; the device is described as Zeiss confocal microscopes.\n- kind: metadata_error\n  statement: The DfOverF series are not ΔF/F. In the four single-colour files each ROI trace is divided\n    by its mean (float64, mean 1); in the four two-colour files traces are centred near 0 (float32)\n    with the first 60 s held constant. The Fluorescence series vary by about 1e-6 per frame or not at\n    all, consistent with baselines, and carry the same description as DfOverF.\n- kind: metadata_insufficient\n  statement: The ActivityStates table is described only as classified periods of activity. It does not\n    follow the Methods' definition (many active rows of 5 s or less), its transient rows are undefined\n    and duplicate active rows, it holds 3 rows in the glia-only files, and it does not say which\n    condition each row belongs to.\n- kind: metadata_insufficient\n  statement: The stimulus signals have no units or descriptions beyond their names, and the protocol\n    codes in StimulusParameterSignals (12, 22, 23, 32, 33, 51, 52, 53) are not described. Closed and\n    open loop can be read only from the gain signal.\n- kind: identifier_missing\n  statement: The ROIs are in each fish's own image space, with no registration to a reference brain\n    and no region labels, so the paper's region-level results (L-MO, NE-MO) cannot be located.\n- kind: other\n  statement: The two groups of files were processed differently (trace scaling, data type, censoring,\n    chunking), and the volume rate is 1.6 to 2.9 Hz against the 3 volumes per second of the Methods.\n- kind: metadata_error\n  statement: The SwimIntervals width column is described as the estimated width spanned by the swim\n    event but equals the bout duration in seconds.\n"
}
```

```
File created successfully at: attempts/000350-mu-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/000350-mu-2019-01.yaml'; s=open(p).read()
s=s.replace("fish, with raw images only (8499 to 9000 volumes of about 2 GB each, 0.39 to 0.42 TB per file),","fish, with raw images only (8499 to 9000 volumes, 0.39 to 0.42 TB per file),")
s=s.replace("- kind: identifier_missing\n  statement: The ROIs are in each","- kind: metadata_insufficient\n  statement: The ROIs are in each")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/000350-mu-2019 && python tools/entry.py handover entries/000350-mu-2019 && ls executed/000350-mu-2019/handover && git status --short
```

```
0 error(s)
wrote executed/000350-mu-2019/handover
10.1016-j.cell.2019.05.050.yaml
fictive.py
reproduce_mu_2019.ipynb
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
?? attempts/000350-mu-2019-01.yaml
?? claims/000350/
?? entries/000350-mu-2019/
?? scripts
```

**Agent calls Bash**

```bash
ls -a entries/000350-mu-2019; git check-ignore -v paper executed 2>&1 | head
```

```
.
..
.claude
README.md
__pycache__
entry.yaml
fictive.py
reproduce_mu_2019.ipynb
requirements.in
requirements.lock.txt
.gitignore:8:paper/	paper
.gitignore:6:executed/	executed
```

**Agent calls Bash**

```bash
ls -a entries/000350-mu-2019/.claude; git check-ignore -v entries/000350-mu-2019/__pycache__ entries/000350-mu-2019/.claude; rm -rf entries/000350-mu-2019/__pycache__
```

```
.
..
.cc-writes
.gitignore:1:__pycache__/	entries/000350-mu-2019/__pycache__
```

**Agent calls Bash**

```bash
find entries/000350-mu-2019/.claude | head; git status --short entries/ | head
```

```
entries/000350-mu-2019/.claude
entries/000350-mu-2019/.claude/.cc-writes
?? entries/000350-mu-2019/
```

**Agent**

I did steps 1 to 6 for dandiset 000350 and handed over for verification. The entry passes `check`, and the notebook ran from a clean environment in 609 s. The handover package is in `executed/000350-mu-2019/handover/`. I did not verify my own work and did not commit.

The paper is open access (CC BY-NC-ND), so I used the full text: main text and STAR Methods, from the PDF on the first author's lab site (Cell's own site blocked the download). It is saved under `paper/`. The Supplemental Information was not read.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| fig1h-epoch-durations (passive 24.4 s, active 36.1 s, 29 bouts per active epoch) | partially reproduced: 20.5 s and 19.1 bouts within tolerance, active 22.4 s outside |
| methods-isi (1.2 s closed loop, 1.19 s in active epochs) | partially reproduced: 1.143 s within, 1.332 s outside |
| fig1j-open-loop-passivity | not reproduced (median 0.551 open against 0.546 closed, p = 0.285) |
| fig1c-vigor-open-loop-onset | reproduced (9 fish, median power ratio 3.49, p = 0.0195) |
| fig1i-isi-before-passivity | not reproduced (p = 0.103 and 0.16; holds with a different minimum epoch length) |
| fig2bc-neurons-lower-in-passivity | reproduced (8 of 8 fish, p = 0.0039) |
| fig2c-glia-rise-at-passivity | not reproduced (2 of 4 fish; the criterion needed 3) |
| figs2a-open-loop-higher | partially reproduced (neurons both measures; glia 3 of 4 fish) |
| fig2h-glia-weaker-closed-loop-pauses | not reproduced (2 of 4 fish) |
| fig2dg-nmf-components | blocked: data_missing |
| fig2kl-lmo-glia-most-consistent, fig6a-ne-ramp | blocked: metadata_insufficient |
| fig1k, fig1f, fig4, fig5, fig6-ne-drives-glia, fig7-ne-mismatch, fig7-glia-accumulate | blocked: data_missing |

## 2. What was found about the dandiset

- **Contents:** 12 light-sheet sessions (150 to 940 GB each), all with swim and stimulus signals. Only 8 have cell traces: 4 with neurons and glia imaged together, 4 with neurons only. The other 4 are raw images only, and they include the only 3 glia-only GCaMP6f fish (the paper's glial analysis used 6). Nothing from Figures 4 to 7 is in it.
- **Mislabelled indicator:** the glial plane of the two-colour files says GCaMP6f, but it is excited at 561 nm and detected at 660 nm, which is jRGECO1b. The raw images are typed `TwoPhotonSeries`, but the microscope is a one-photon light sheet.
- **`DfOverF` is not ΔF/F:**
  - In 4 files each ROI's trace is divided by its own mean (mean 1).
  - In the other 4 the traces are centred on 0 and the first 60 s are held constant.
  - `Fluorescence` looks like a slow baseline, and has the same description as `DfOverF`.
- **Missing imaging:**
  - sub-20170113-2 has 7616 imaging volumes against 9751 camera triggers.
  - Raw images are missing for part of sub-20170113-4 (3065 of 12050 volumes) and sub-20170228-4 (5776 of 7200).
- **Undocumented tables and signals:**
  - `ActivityStates` does not follow the Methods' definition: many "active" rows last 5 s or less, the "transient" rows duplicate active rows, and the glia-only files have only 3 rows.
  - The stimulus protocol codes, gain and velocity signals have no units or descriptions.
- **No anatomy:** there is no registration to a reference brain and no region labels, so L-MO and NE-MO cannot be located.
- **Clock:** imaging timestamps equal the camera-trigger edges, and the neuronal signal follows swimming with a 0.3 to 5 s lag. This is consistent with one shared clock.
- **Version pinned:** 0.240822.1759. The paper cites no version. Compared with 0.221219.1506, it renames the imaging series and fixes the plane name of the 3 glia-only files. The behaviour and traces are identical in both.

## 3. Where the protocol was unclear, wrong or missing something

1. **SEM as tolerance.** The protocol says to use "the paper's own uncertainty", but the paper gives SEMs over 74 fish. I used 1.96 × SEM and gave the reason in the claims file.
2. **Code that does not cover the analysis.** The linked code (segmentation only, commit 54d1907) covers none of the behaviour or onset analyses. The protocol assumes the code settles open choices; here I could only follow the Methods and record my own choices.
3. **No rule for normalisation.** The protocol has no rule for traces whose scaling differs between files. I compared only within each fish, scaled by that fish's trace SD.
4. **No rule for reading a subset.** The full trace tables (6 to 10 GB per series, gzip) do not fit the time limit. I used a fixed 8 to 15% subset of ROIs, and showed two disjoint subsets agree (correlation 0.98 and 1.00).
5. **Sample size of a subset.** The paper's behavioural numbers come from 74 fish; the dandiset has 12 of them. I recorded this as a deviation without changing tolerances.
6. **Untested criterion choices.** The fig1i result flips with the minimum epoch length (10 bouts fails, 8 bouts passes). The protocol fixes the choice before analysis, which I followed. It gives no way to say a criterion was fragile except to show variants, which I did.
7. **Which blocking reason to choose.** For the NMF claim several apply: part of the data is missing (3 of 6 fish), the rest is raw only (too large), and the clustering was tuned by hand. I recorded data_missing and named the others in the notes.

## 4. Runtime and what failed

- The notebook takes 609 s; 424 s of that is reading traces.
- About an hour was lost when a version-comparison script that walked every dataset of 24 remote files hung until the 60-minute timeout. I redid it with targeted reads and a hard timeout.
- Two notebook runs needed fixes before the final run:
  - a ragged-array error in the 8-bout variant;
  - the open/closed-loop comparison counted stationary-grating changes as switches and divided an uncentred mean by the SD.

Both are fixed in the final run.

## End of run

74 turns, 135 minutes, result: success.
