# 000947 · verifier-1 · run 39106507854

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs paper 2>/dev/null; cat *.yaml *.json 2>/dev/null | head -200
```

```
total 292
drwxr-xr-x 5 runner runner    4096 Oct 18 07:25 .
drwxr-xr-x 7 runner runner    4096 Oct 18 07:25 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 18 07:25 .claude
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.development
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.local
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.production
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.test
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .env.test.local
drwx------ 2 runner runner    4096 Oct 18 07:25 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .github
-rw-r--r-- 1 runner runner       0 Oct 18 07:25 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 18 07:06 .mcp.json
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p 10.1371-journal.pbio.3000829.yaml; ls .claude
```

```
tolerance: 9
    unit: ms
  criterion: All detected increases and decreases pooled per area (Fig2_3_S8_S9.m, "ALL
    RESPONSES"). Reproduced when GPi onsets are later than VLa onsets by a rank sum test (p < 0.05)
    and both medians are within tolerance; partially reproduced when only the significant
    difference holds.
- id: fig3b-gpi-decr-lag-vla-incr
  statement: GPi decreases lag behind VLa increases (median onsets -27 and -88 ms; rank sum p =
    4.9e-4), against the gating prediction.
  source: Results, third section; Fig 3B
  expected:
  - quantity: GPi decrease median onset
    value: -27
    tolerance: 2.7
    unit: ms
  - quantity: VLa increase median onset
    value: -88
    tolerance: 8.8
    unit: ms
  criterion: As fig3a-vla-leads-gpi, on GPi decreases against VLa increases.
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_schwab_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:5000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:5000])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1401 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown
2	# Reproducing Schwab et al. (2020) from dandiset 000947
3	
4	**Paper.** Schwab BC, Kase D, Zimnik A, Rosenbaum R, Codianni MG, Rubin JE, Turner RS (2020). Neural
5	activity during a simple reaching task in macaques is counter to gating and rebound in basal
6	ganglia-thalamic communication. *PLOS Biology* 18(10): e3000829.
7	[doi:10.1371/journal.pbio.3000829](https://doi.org/10.1371/journal.pbio.3000829). The paper is open
8	access and this attempt used its full text.
9	
10	**Dandiset.** [DANDI:000947](https://dandiarchive.org/dandiset/000947/0.240510.2211), version
11	0.240510.2211. The paper predates the dandiset and cites no DANDI version (its data statement points
12	to Dryad). 0.240510.2211 is the only published version, so it is pinned; the draft lists the same
13	378 files.
14	
15	**What the dandiset holds.** Single-unit recordings from two monkeys (Gaia, "NHP G", and Isis,
16	"NHP I") in GPi, VL thalamus, motor cortex and other areas, before and after MPTP, with trial
17	tables and raw and filtered traces. The paper uses the pre-MPTP GPi and VLa recordings. EMG,
18	the stimulation mapping of Fig 1 and the simulations of Fig 6 are not in the dandiset.
19	
20	**Outside inputs.** The paper's Dryad deposit (doi:10.5061/dryad.0cfxpnvxm, read here from its
[... 877 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 898
}
```

```
898	        x = df[df.area == a].integrated
899	        w = stats.wilcoxon(x)
900	        print(f"  {a}: mean {x.mean():.2f} spikes (SD {x.std():.2f}), median {x.median():.2f}, n {len(x)}; signed rank p = {w.pvalue:.2g}; "
901	              f"range {x.min():.1f} to {x.max():.1f}")
902	    print("  by animal:", df.groupby(["area", "subject"]).integrated.mean().round(2).to_dict())
903	--OUT--
904	Dandiset rule
905	  GPi: mean 3.07 spikes (SD 11.20), median 3.21, n 531; signed rank p = 1.1e-10; range -35.4 to 41.7
906	  VLa: mean 1.50 spikes (SD 4.34), median 0.78, n 552; signed rank p = 3.7e-18; range -10.9 to 38.2
907	  by animal: {('GPi', 'Gaia'): 4.22, ('GPi', 'Isis'): 1.87, ('VLa', 'Gaia'): 2.48, ('VLa', 'Isis'): 1.12}
908	Variant, the paper's records
909	  GPi: mean 3.42 spikes (SD 10.10), median 2.64, n 395; signed rank p = 4.9e-12; range -35.4 to 41.7
910	  VLa: mean 1.97 spikes (SD 5.45), median 1.22, n 329; signed rank p = 2.6e-11; range -9.3 to 38.2
911	  by animal: {('GPi', 'Gaia'): 4.41, ('GPi', 'Isis'): 2.5, ('VLa', 'Gaia'): 3.95, ('VLa', 'Isis'): 0.83}
912	
913	=== [34] markdown
914	## fig3a-vla-leads-gpi
915	
916	> Peri-movement changes begin later in GPi than in VLa (median onsets -47 and -90 ms).
917	=== [35] code
[... 485 more lines not kept]
```

**Agent**

Notebook read: 18 claims tested, 3 blocked. Now reading the helper module.

**Agent calls Read**

```json
{
 "file_path": "gpivla.py"
}
```

```
1	"""Loading and measures for the pre-MPTP GPi and VLa recordings of dandiset 000947.
2	
3	Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020), PLOS Biology,
4	doi:10.1371/journal.pbio.3000829.
5	
6	Each NWB file holds one recording block of one monkey (Gaia or Isis): a trials table (cue onset,
7	movement onset and end, target, and in some files error onset), the curated single units in
8	`units` (spike times in seconds, a location label, channel id and sort letter), all sorted
9	clusters in `processing/ecephys/units`, and raw and 200 Hz high-pass filtered traces. Files are
10	streamed from the archive at the pinned version; nothing is written to disk. Only the curated
11	`units` table and the trials are read, except for the action potential width, which reads one
12	chunk of the filtered traces per unit.
13	
14	Where the parameters come from:
15	
16	- Paper's Methods: valid trials exclude errors and outliers in reaction time or movement duration
17	  (more than 6 median absolute differences from the mean); a unit needs at least 10 valid trials
18	  (applied here per direction); its mean rate over the recording must be at least 30 spikes/s in
19	  GPi and 1 spike/s in VLa; spike density functions (SDF) use a Gaussian kernel of 25 ms at 1 ms
20	  resolution; decreases are detected on the interspike interval (ISI) function, the current ISI
[... 479 more lines not kept]
```

**Agent**

Helper module read. Next, fetching the paper's full text to check methods.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL "https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.3000829&type=manuscript" -o paper/schwab2020.pdf; file paper/schwab2020.pdf; ls -la paper
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; mv schwab2020.pdf schwab2020.xml; python3 -c "
import re
from xml.etree import ElementTree as ET
t=ET.parse('schwab2020.xml'); r=t.getroot()
body=r.find('.//body')
out=[]
for sec in r.iter():
    pass
def txt(e): return ''.join(e.itertext())
for p in r.iter():
    if p.tag in ('title','p','caption','th','td'):
        out.append(('## ' if p.tag=='title' else '')+re.sub(r'\s+',' ',txt(p)).strip())
open('schwab2020.txt','w').write('\n'.join(out))
"; wc -c schwab2020.txt; grep -n -i -E "^## " schwab2020.txt | head -80
```

```
162794 schwab2020.txt
4:## Introduction
9:## Results
10:## Basic approach, database, and activity at rest
14:## 
20:## Database and basic properties of neurons.
134:## 
136:## Task performance
138:## Movement-related increases in firing are common in both GPi and VLa
145:## Response onset latencies in GPi and VLa are incompatible with gating and rebound
148:## 
155:## Correlated activity in GPi-VLa cell pairs is rare and unbiased
158:## 
161:## Cell-pair interactions between GPi and VLa.
187:## VLa activity decreases with bursts and pauses in GPi activity
190:## VLa activity relative to GPi bursts and pauses.
195:## Simulations suggest GPi-VLa communication scales with GPi synchrony and convergence
198:## GPi synchrony and anatomical convergence determine correlations between GPi and VLa.
201:## Discussion
204:## Overview.
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 9,160p schwab2020.txt | cut -c1-3000
```

```
<persisted-output>
Output too large (35.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4a9a15e2-b884-435f-a2c0-e24b0d0702e0/tool-results/bfs6lqz9f.txt

Preview (first 2KB):
## Results
## Basic approach, database, and activity at rest
We studied the single-unit activity of neurons sampled from connected regions of the GPi and VLa. The spiking activity of isolated single units was recorded from both areas simultaneously in macaque monkeys while the animals performed a two-choice reaction time reaching task for food reward [48; 49]. In short, animals were trained to hold their left hand at a home-position located immediately to the left of the animal at waist height. Two visual targets were located 14 cm apart at shoulder height on a vertically mounted response panel positioned 30 cm in front of the animal. After a randomized home-position hold period, one of the targets (chosen pseudorandomly trial-to-trial) was lit and the animal had to move the left hand swiftly to that target (distance: approximately 37 cm) and then hold there to obtain a reward. The right arm was restrained in a padded splint throughout a data collection session. Multiple microelectrodes or 16-contact linear probes were positioned acutely in the arm-related regions of both nuclei [50].
...
</persisted-output>
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/4a9a15e2-b884-435f-a2c0-e24b0d0702e0/tool-results/bfs6lqz9f.txt"
}
```

```
1	## Results
2	## Basic approach, database, and activity at rest
3	We studied the single-unit activity of neurons sampled from connected regions of the GPi and VLa. The spiking activity of isolated single units was recorded from both areas simultaneously in macaque monkeys while the animals performed a two-choice reaction time reaching task for food reward [48; 49]. In short, animals were trained to hold their left hand at a home-position located immediately to the left of the animal at waist height. Two visual targets were located 14 cm apart at shoulder height on a vertically mounted response panel positioned 30 cm in front of the animal. After a randomized home-position hold period, one of the targets (chosen pseudorandomly trial-to-trial) was lit and the animal had to move the left hand swiftly to that target (distance: approximately 37 cm) and then hold there to obtain a reward. The right arm was restrained in a padded splint throughout a data collection session. Multiple microelectrodes or 16-contact linear probes were positioned acutely in the arm-related regions of both nuclei [50].
4	We used a combination of electrophysiologic techniques to ensure that recordings were obtained from anatomically connected regions of GPi and VLa. Consistent with previous observations [34; 51], the location of the VLa nucleus was distinguished from surrounding thalamic regions—and from the cerebellar-recipient ventrolateral posterior nucleus (VLp) in particular—by the presence of a short-latency inhibition of spiking in response to electrical stimulation of the GPi and the absence of short-latency excitation in response to stimulation of the superior cerebellar peduncle (SCP, Fig 1B). This electrophysiologic localization of the VLa/VLp border was performed during initial mapping studies prior to formal data collection. Across multiple parallel electrode tracks, thalamic neurons inhibited by GPi stimulation (yellow tick marks in Fig 1A, examples 1 and 2 in Fig 1B) were always e
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 161,200p schwab2020.txt | cut -c1-4000; echo ----; sed -n 253,298p schwab2020.txt
```

```
<persisted-output>
Output too large (43.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4a9a15e2-b884-435f-a2c0-e24b0d0702e0/tool-results/bsx7by8q6.txt

Preview (first 2KB):
## Cell-pair interactions between GPi and VLa.

Cross-correlations
Noise correlations
Burst/pause influences
Number of GPi-VLa pairs
Whole recordings:427During rest:183During movement:172
During rest:332During movement:372
Burst onsets:163Burst offsets:167Pause onsets:153
Fraction of significant pairs(total number)
Whole recordings:3.5% (15)
During rest: 5.4% (18)44% positive (8)56% negative (10)
Burst onsets: 11.6% (19)74% decreases (14)26% increases (5)

During rest:2.2% (4)During movement:5.2% (9)
During movement: 7.2% (27)41% positive (11)59% negative (16)
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=161 && NR<=200 && length($0)<6000' schwab2020.txt | grep -v "^(A" ; echo ----; awk 'NR>=253 && NR<=297' schwab2020.txt
```

```
<persisted-output>
Output too large (42.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4a9a15e2-b884-435f-a2c0-e24b0d0702e0/tool-results/bhkjx6nvb.txt

Preview (first 2KB):
## Cell-pair interactions between GPi and VLa.

Cross-correlations
Noise correlations
Burst/pause influences
Number of GPi-VLa pairs
Whole recordings:427During rest:183During movement:172
During rest:332During movement:372
Burst onsets:163Burst offsets:167Pause onsets:153
Fraction of significant pairs(total number)
Whole recordings:3.5% (15)
During rest: 5.4% (18)44% positive (8)56% negative (10)
Burst onsets: 11.6% (19)74% decreases (14)26% increases (5)

During rest:2.2% (4)During movement:5.2% (9)
During movement: 7.2% (27)41% positive (11)59% negative (16)
[... 7 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/4a9a15e2-b884-435f-a2c0-e24b0d0702e0/tool-results/bhkjx6nvb.txt",
 "offset": 20
}
```

```
20	Significant burst/pause influences: pairs with average VLa firing rates 0–100 ms after GPi burst/pause onset/offset above/below 97.5% of their baseline firing.
21	Abbreviations: CCF, cross-correlation function; GPi, globus pallidus-internus; VLa, ventrolateral anterior nucleus
22	Among the small number of individual CCFs that did exceed the threshold for significance, none showed features consistent with being the product of strong monosynaptic GPi-to-VLa inhibition. Contrary to the expectation that GPi-to-VLa CCF effects would be predominantly inhibitory (i.e., negative), roughly equal numbers of the CCF peaks detected as significant were positive and negative (8 versus 7, respectively; p = 0.79, chi-squared test; S10D–S10F Fig). Only two CCFs showed a long-lasting (>5 ms) reduction in VLa firing following the GPi spike (S10D Fig, first and third examples). Those two effects showed features consistent with a slow rhythmic GPi-VLa synchronization at 25 Hz (approximately 40-ms cycle length). Slow rhythmic synchronizations at frequencies <25 Hz were also present in some individual raw CCFs, but those effects were removed implicitly by subtracting the average jitter control CCF (see Materials and methods). The magnitude of individual CCF peaks correlated closely with the width of the CCF’s 95% CI (whole recordings: r = 0.82, p < 10−10; during rest: r = 0.62, p < 10−10; during movement: r = 0.61, p < 10−10), which reflects how noisy the estimate of the CCF was (S10G–S10I Fig). In other words, the narrower the 95% CI, the smaller the estimation noise and, incidentally, the smaller the detected CCF peak. This was true even for CCF peaks that were detected as significant (red X’s in S10G–S10I Fig), thus reinforcing the view that the CCF peaks detected here as significant may in fact have been false-positive noise events. Together, these observations suggest that short-time-scale spike-to-spike interactions between GPi and VLa unit pairs, if present, were too small and/o
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  B=https://api.dandiarchive.org/api/dandisets/000947/versions/0.240510.2211; curl -s "$B/" | python3 -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',d); print(json.dumps(m.get('assetsSummary'),indent=0)[:2000]); print(m.get('description','')[:2000])"; curl -s "$B/assets/?page_size=1000" | python3 -c "
import json,sys,collections; d=json.load(sys.stdin); print(d['count']); r=d['results']
c=collections.Counter(); 
for a in r: c[a['path'].split('/')[0]+' '+('pre' if 'pre-MPTP' in a['path'] else 'post')]+=1
print(c); print([a['path'] for a in r][:5]); json.dump(r,open('$TMPDIR/assets.json','w'))"
```

```
{
"species": [
{
"name": "Macaca mulatta - Rhesus monkey",
"schemaKey": "SpeciesType",
"identifier": "http://purl.obolibrary.org/obo/NCBITaxon_9544"
}
],
"approach": [
{
"name": "electrophysiological approach",
"schemaKey": "ApproachType"
}
],
"schemaKey": "AssetsSummary",
"dataStandard": [
{
"name": "Neurodata Without Borders (NWB)",
"schemaKey": "StandardsType",
"identifier": "RRID:SCR_015242"
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json,os,requests,collections
from concurrent.futures import ThreadPoolExecutor
r=json.load(open(os.environ['TMPDIR']+'/assets.json'))
pre=[a for a in r if 'pre-MPTP' in a['path']]
def get(a):
    return requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/",timeout=60).json()
with ThreadPoolExecutor(16) as ex: ms=list(ex.map(get,pre))
vm=collections.Counter(); keys=collections.Counter()
for m in ms:
    for v in m.get('variableMeasured',[]): vm[v.get('value')]+=1
    for k in m.get('wasGeneratedBy',[]):
        keys[k.get('name','')[:40]]+=1
print(vm); print(keys.most_common(5))
print(json.dumps(ms[0],indent=0)[:3000])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null | head; which -a python python3; python3 -c "import numpy, scipy, pandas; print('ok')"
```

```
Exit code 1
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipx
pipx_bin
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
Traceback (most recent call last):
  File "<string>", line 1, in <module>
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  /usr/bin/python3 -c "import numpy, scipy, pandas; print('ok')" 2>&1; python3 -m venv $TMPDIR/venv && $TMPDIR/venv/bin/pip install -q numpy scipy pandas requests 2>&1 | tail -2; $TMPDIR/venv/bin/python -c "import numpy,scipy,pandas,requests;print('ok')"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
ok
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/bin/python - <<'EOF'
import json,os,requests,collections
from concurrent.futures import ThreadPoolExecutor
r=json.load(open(os.environ['TMPDIR']+'/assets.json'))
pre=[a for a in r if 'pre-MPTP' in a['path']]
def get(a):
    return requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/",timeout=60).json()
with ThreadPoolExecutor(16) as ex: ms=list(ex.map(get,pre))
vm=collections.Counter()
for m in ms:
    for v in m.get('variableMeasured',[]): vm[v.get('value')]+=1
print(vm)
m=ms[0]; print(json.dumps({k:m[k] for k in m if k not in ('digest','contentUrl')},indent=0)[:2500])
EOF
curl -s "https://zenodo.org/api/records/4000719" | $TMPDIR/venv/bin/python -c "import json,sys; d=json.load(sys.stdin); print([f['key'] for f in d.get('files',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -A3 "Reach-related modulations in muscle activity began" schwab2020.txt | cut -c1-2500; grep -n -i "Fig 2 shows\|S6 Fig\b" schwab2020.txt | head -3; grep -n -A2 "^## Relationship between neural responses and movement directions" schwab2020.txt | cut -c1-2000
```

```
307:Reach-related modulations in muscle activity began well in advance of the mechanically detected onset of movement. Rectified low-pass filtered EMG from proximal arm muscles was collected during a subset of data collection sessions (n = 667 and 476 trials in NHPs G and I, respectively). Signals from each muscle were averaged across trials separately for reaches to left and right targets (blue and green traces, respectively). The width of each trace reflects the SEM. The earliest reach-related modulation in EMG in both animals consisted of a reduction in triceps resting activity followed soon thereafter by increases in two agonist muscles (anterior deltoid and biceps; red vertical dashed lines), which occurred at similar premovement timing in both animals (−123 and −135 ms in NHPs G and I). For reference, red tick marks at the bottom of each panel indicate the times on individual trials of go-cue presentation and target touch at the end of the reach. EMG from pectoralis was not available for NHP I because of poor signal quality. Data and code to reproduce this figure can be found in https://doi.org/10.5061/dryad.0cfxpnvxm (FigS3.m). EMG, electromyography; NHP, nonhuman primate; SEM, standard error of the mean. (TIF)
308:## Reach-related modulations in muscle activity began well in advance of the mechanically detected onset of movement.
309-Rectified low-pass filtered EMG from proximal arm muscles was collected during a subset of data collection sessions (n = 667 and 476 trials in NHPs G and I, respectively). Signals from each muscle were averaged across trials separately for reaches to left and right targets (blue and green traces, respectively). The width of each trace reflects the SEM. The earliest reach-related modulation in EMG in both animals consisted of a reduction in triceps resting activity followed soon thereafter by increases in two agonist muscles (anterior deltoid and biceps; red vertical dashed lines), which occurred at similar premovement timing in 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t1.py <<'EOF'
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, pandas as pd, gpivla as g
rng=np.random.default_rng(0)
# 1. detect(): synthetic SDF with step at known onset
for onset_true in (-150,-50,50):
  res=[]
  for rep in range(50):
    ntr=60; T=3000.0
    trials=[]; spikes=[]
    for k in range(ntr):
        a=10+k*5.0
        trials.append(a)
    trials=np.array(trials)
    # inhomogeneous poisson: base 20 Hz, 60 Hz after onset until +300
    t=np.sort(rng.uniform(0,T,int(20*T*1.2)))
    t=t[rng.random(len(t))<20/24]
    extra=[]
    for a in trials:
        n=rng.poisson(40*0.3); extra+=list(a+onset_true/1000+rng.uniform(0,0.3,n))
    sp=np.sort(np.r_[t,extra])
    tr=pd.DataFrame({"movement_start_time":trials,"cue_onset_time":trials-0.25,"target":"Left"})
    tr["rt"]=0.25; tr["valid"]=True
    d=g.unit_direction([(sp,tr)],"Left")
    res.append((d["inc_onset"],d["dec_onset"]))
  r=np.array(res); print("true",onset_true,"inc onset median",np.nanmedian(r[:,0]),"detected",np.isfinite(r[:,0]).mean(),"spurious dec",np.isfinite(r[:,1]).mean())
# null: no response
fp=[]
for rep in range(100):
    trials=10+np.arange(60)*5.0
    sp=np.sort(rng.uniform(0,320,int(20*320)))
    tr=pd.DataFrame({"movement_start_time":trials,"cue_onset_time":trials-0.25,"target":"Left","rt":0.25,"valid":True})
    d=g.unit_direction([(sp,tr)],"Left"); fp.append((np.isfinite(d["inc_onset"]),np.isfinite(d["dec_onset"]),d["slope_sig"]))
fp=np.array(fp); print("null: inc FP",fp[:,0].mean(),"dec FP",fp[:,1].mean(),"slope_sig rate",fp[:,2].mean())
# integrated / rest
print("rest rate (expect ~20):",d["rest_rate"],"integrated (expect ~0):",d["integrated"])
EOF
$TMPDIR/venv/bin/python $TMPDIR/t1.py
```

```
true -150 inc onset median -175.0 detected 1.0 spurious dec 0.18
true -50 inc onset median -73.0 detected 1.0 spurious dec 0.32
true 50 inc onset median 26.0 detected 1.0 spurious dec 0.06
null: inc FP 0.06 dec FP 0.29 slope_sig rate 0.82
rest rate (expect ~20): 20.226562791243353 integrated (expect ~0): -0.7508867139847073
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t2.py <<'EOF'
exec(open('/dev/stdin').read()) if False else None
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, pandas as pd, gpivla as g
rng=np.random.default_rng(1)
for rate in (5,13,70):
  for ntr in (30,60):
    inc,dec,on,sl=[],[],[],[]
    for rep in range(100):
        trials=10+np.arange(ntr)*5.0
        T=trials[-1]+10
        sp=np.sort(rng.uniform(0,T,rng.poisson(rate*T)))
        rt=rng.uniform(0.2,0.3,ntr)
        tr=pd.DataFrame({"movement_start_time":trials,"cue_onset_time":trials-rt,"target":"Left","rt":rt,"valid":True})
        d=g.unit_direction([(sp,tr)],"Left")
        inc.append(np.isfinite(d["inc_onset"])); dec.append(np.isfinite(d["dec_onset"])); sl.append(d["slope_sig"])
        if np.isfinite(d["dec_onset"]): on.append(d["dec_onset"])
        if np.isfinite(d["inc_onset"]): on.append(d["inc_onset"])
    print(f"rate {rate} trials {ntr}: inc FP {np.mean(inc):.2f} dec FP {np.mean(dec):.2f} any {np.mean(np.array(inc)|np.array(dec)):.2f} slope_sig {np.mean(sl):.2f} median spurious onset {np.median(on) if on else np.nan}")
EOF
$TMPDIR/venv/bin/python $TMPDIR/t2.py
```

```
rate 5 trials 30: inc FP 0.10 dec FP 0.34 any 0.44 slope_sig 0.88 median spurious onset 88.0
rate 5 trials 60: inc FP 0.07 dec FP 0.37 any 0.44 slope_sig 0.85 median spurious onset 2.0
rate 13 trials 30: inc FP 0.12 dec FP 0.28 any 0.40 slope_sig 0.85 median spurious onset -31.5
rate 13 trials 60: inc FP 0.11 dec FP 0.33 any 0.44 slope_sig 0.86 median spurious onset 73.5
rate 70 trials 30: inc FP 0.10 dec FP 0.20 any 0.30 slope_sig 0.89 median spurious onset 67.5
rate 70 trials 60: inc FP 0.05 dec FP 0.17 any 0.22 slope_sig 0.84 median spurious onset 126.5
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t3.py <<'EOF'
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, gpivla as g
from scipy import stats
for grid in (False, True):
  ps=[]
  for rep in range(6):
    rng=np.random.default_rng(100+rep)
    peaks, ctrls, sig = [], [], 0
    for p in range(80):
        T=200.0
        a=np.sort(rng.uniform(0,T,rng.poisson(70*T))); b=np.sort(rng.uniform(0,T,rng.poisson(12*T)))
        if grid: a=np.unique(np.round(a,3))+1000.0; b=np.unique(np.round(b,3))+1000.0
        r=g.ccf_test(a,b,max(a[-1],b[-1])-min(a[0],b[0]),rng,400)
        peaks.append(r["peak"]); ctrls.append(r["ctrl_peaks"]); sig+=r["significant"]
    ps.append(g.ks_permutation(np.array(peaks),np.vstack(ctrls)))
    print("grid",grid,"rep",rep,"KS p",round(ps[-1],3),"sig frac",sig/80, flush=True)
EOF
$TMPDIR/venv/bin/python $TMPDIR/t3.py
```

```
grid False rep 0 KS p 0.667 sig frac 0.05
grid False rep 1 KS p 0.255 sig frac 0.05
grid False rep 2 KS p 0.968 sig frac 0.0
grid False rep 3 KS p 0.978 sig frac 0.05
grid False rep 4 KS p 0.94 sig frac 0.0375
grid False rep 5 KS p 0.275 sig frac 0.1125
grid True rep 0 KS p 0.0 sig frac 1.0
grid True rep 1 KS p 0.0 sig frac 1.0
grid True rep 2 KS p 0.0 sig frac 1.0
grid True rep 3 KS p 0.0 sig frac 1.0
grid True rep 4 KS p 0.0 sig frac 1.0
grid True rep 5 KS p 0.0 sig frac 1.0
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t4.py <<'EOF'
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, gpivla as g
rng=np.random.default_rng(3)
T=200.0
a=np.sort(rng.uniform(0,T,rng.poisson(70*T))); b=np.sort(rng.uniform(0,T,rng.poisson(12*T)))
for off,grid in ((0,False),(0,True),(1000,True)):
    x=np.unique(np.round(a,3))+off if grid else a; y=np.unique(np.round(b,3))+off if grid else b
    r=g.ccf_test(x,y,T,rng,100)
    print(off,grid,"ccf-meanctrl:",np.round(r["ccf"][18:30],2), "peak",round(r["peak"],3),"thr",round(r["thr95"],3))
    d_=(y[None,:200]-x[:,None]).ravel(); d_=d_[np.abs(d_)<0.005]
    k=np.floor(d_*1000).astype(int); print("  frac of integer-ms lags floored down:", np.mean(np.abs(d_*1000-np.round(d_*1000))<1e-6) , np.mean(k!=np.round(d_*1000)))
EOF
$TMPDIR/venv/bin/python $TMPDIR/t4.py
```

```
0 False ccf-meanctrl: [ 0.09  0.09  0.05  0.02 -0.01 -0.03 -0.01  0.05 -0.01  0.06  0.09 -0.11] peak 0.109 thr 0.111
  frac of integer-ms lags floored down: 0.0 0.5231788079470199
0 True ccf-meanctrl: [-0.07 -0.24 -0.09  0.3  -0.07 -0.02  0.24 -0.22 -0.11  0.28 -0.05 -0.01] peak 0.168 thr 0.119
  frac of integer-ms lags floored down: 1.0 0.4315068493150685
1000 True ccf-meanctrl: [-0.07 -0.12  0.4   0.44 -0.09 -0.1  -0.05 -0.07 -0.11 -0.06 -0.05  0.32] peak 0.418 thr 0.115
  frac of integer-ms lags floored down: 1.0 0.47770700636942676
```

**Agent calls Bash**

```bash
cd  sed -e 's/if grid: a=np.unique(np.round(a,3))+1000.0; b=np.unique(np.round(b,3))+1000.0/if grid: fs=24414.0625; a=np.unique(np.round(a*fs))\/fs; b=np.unique(np.round(b*fs))\/fs/' -e 's/for grid in (False, True)/for grid in (True,)/' $TMPDIR/t3.py > $TMPDIR/t5.py; grep -n "fs=" $TMPDIR/t5.py; $TMPDIR/venv/bin/python $TMPDIR/t5.py
```

```
16:        if grid: fs=24414.0625; a=np.unique(np.round(a*fs))/fs; b=np.unique(np.round(b*fs))/fs
grid True rep 0 KS p 0.978 sig frac 0.05
grid True rep 1 KS p 0.355 sig frac 0.025
grid True rep 2 KS p 0.87 sig frac 0.025
grid True rep 3 KS p 0.775 sig frac 0.05
grid True rep 4 KS p 0.005 sig frac 0.05
grid True rep 5 KS p 0.51 sig frac 0.025
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t6.py <<'EOF'
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, gpivla as g
rng=np.random.default_rng(7)
T=300.0
base=np.sort(rng.uniform(0,T,rng.poisson(70*T)))
print("pure Poisson 70 Hz: bursts/min", len(g.bursts(base,70))/5, "mean dur ms", np.mean([1e3*(e-s) for s,e in g.bursts(base,70)]))
starts=np.sort(rng.uniform(1,T-1,300))
ins=np.concatenate([s+np.arange(6)*0.003 for s in starts])   # 6 spikes over 15 ms
sp=np.sort(np.r_[base,ins]); rate=len(sp)/T
b=g.bursts(sp,rate)
dur=np.array([1e3*(e-s) for s,e in b])
hit=np.mean([np.any([(s<=st+0.016) and (e>=st) for s,e in b]) for st in starts[:100]])
print("with 300 inserted 15-ms bursts: detected",len(b),"mean dur ms",dur.mean().round(1),"median",np.median(dur).round(1),"inserted found",hit)
EOF
$TMPDIR/venv/bin/python $TMPDIR/t6.py
```

```
pure Poisson 70 Hz: bursts/min 170.8 mean dur ms 13.179723172266353
with 300 inserted 15-ms bursts: detected 980 mean dur ms 16.5 median 7.8 inserted found 0.95
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t7.py <<'EOF'
import sys, types
for m in ("h5py","remfile"): sys.modules[m]=types.ModuleType(m)
d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=object
sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da
sys.path.insert(0,'.')
import numpy as np, gpivla as g
for rep in range(4):
    rng=np.random.default_rng(50+rep)
    peaks,ctrls,sig,off=[],[],0,[]
    for p in range(150):
        T=600.0
        a=np.sort(rng.uniform(0,T,rng.poisson(70*T))); b=np.sort(rng.uniform(0,T,rng.poisson(15*T)))
        mv=5+np.arange(110)*5.0+rng.uniform(0,1,110)
        win=np.c_[mv-0.2,mv+0.3]
        x,y=a[g._in_windows(a,win)],b[g._in_windows(b,win)]
        r=g.ccf_test(x,y,float(np.sum(win[:,1]-win[:,0])),rng,400)
        peaks.append(r["peak"]); ctrls.append(r["ctrl_peaks"]); sig+=r["significant"]; off.append(r["ccf"].mean())
    print("rep",rep,"KS p",round(g.ks_permutation(np.array(peaks),np.vstack(ctrls)),3),"sig",round(sig/150,3),"mean(real-ctrl) offset",round(np.mean(off),4),flush=True)
EOF
$TMPDIR/venv/bin/python $TMPDIR/t7.py
```

```
rep 0 KS p 0.775 sig 0.06 mean(real-ctrl) offset 0.0036
rep 1 KS p 0.455 sig 0.053 mean(real-ctrl) offset 0.0039
rep 2 KS p 0.175 sig 0.053 mean(real-ctrl) offset 0.0035
rep 3 KS p 0.568 sig 0.08 mean(real-ctrl) offset 0.0027
```

**Agent**

**A. Outcomes**

The claims file lists 21 claims. The notebook tests 18 and marks 3 blocked; no separate attempt record was in the directory. My outcomes: 6 reproduced, 5 partially reproduced, 7 not reproduced, 3 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| unit-link | reproduced | 364 of 394 records found (92.4%). SDF r > 0.9 for 94.6% of 724 unit-directions (cell 17). Trial counts are equal for only 62.6%, and 25 of the matched paper-VLa units are labelled "Thalamus". |
| table1-unit-counts | not_reproduced | 268 GPi and 279 VLa units, against 209 and 185 or 218, all outside 10% (cell 19). Counting one unit per file counts a neuron recorded across several files more than once. The channel-per-day variant gives 132 and 186. |
| table1-rest-rate | reproduced | GPi 75.65 (tolerance band 63.1–77.1) and VLa 12.78 (12.15–14.85) spikes/s; rank sum p = 1e-171 (cell 21). The two animals differ in GPi (p = 0.04), where the paper says they are consistent. |
| table1-ap-width | reproduced | 0.247 and 0.509 ms, both in tolerance; p = 2.9e-37 (cell 23). |
| hold-period-ramps | partially_reproduced | The fractions, 98.5% and 98.6%, are in tolerance. The slopes differ between areas (rank sum p = 0.0415; means −0.60 and +0.23 against the paper's −0.05 and −0.14), which fails the no-difference condition (cell 25). The fraction also sits at its own chance level (problem 2). |
| mvt-responsive-fraction | reproduced | GPi 98.5%; VLa 97.5% is outside 88.1 ± 8.8 but inside the text's 94 ± 9.4, and either reading counts (cell 27). The chance level is high (problem 1). |
| increases-most-common | partially_reproduced | Monophasic increase is the most common form in both areas, and increases exceed 50% of changes. VLa monophasic increases (50.9 against 65.3) and VLa increases as a share of changes (60.2 against 68.8) are outside tolerance (cell 29). |
| monophasic-more-in-vla | not_reproduced | VLa 76.7% is outside 88.9 ± 8.9, and the difference is not significant (chi-squared p = 0.051, cell 31). The paper's-records variant would pass (69.0 against 81.2, p = 3.6e-4). |
| integrated-change-positive | partially_reproduced | Both means are significantly positive (p = 1e-10 and 4e-18), but 3.07 and 1.50 spikes are outside 3.89 ± 0.39 and 1.75 ± 0.18 (cell 33). |
| fig3a-vla-leads-gpi | not_reproduced | GPi −48 ms is in tolerance; VLa −67 ms is outside (−99 to −81). Two-sided p = 0.079 (cell 35). In Gaia the medians are equal. |
| fig3b-gpi-decr-lag-vla-incr | reproduced | −29.5 ms (band −29.7 to −24.3) and −84 ms, p = 2.1e-4 (cell 37). This is fragile: the GPi median is 0.2 ms from the edge, Isis alone gives p = 0.055, and the p-value is inflated (problem 3). |
| fig3c-vla-decr-lead-gpi-incr | not_reproduced | The order is reversed: VLa decreases at −19 ms against the paper's −108, GPi increases at −69 ms, p = 0.17 (cell 39). The paper's-records variant is not significant either (p = 0.2). |
| gating-conflict-fraction | reproduced | 95.4% conflicting, within 96 ± 9.6 (cell 41). Shuffling onsets across unit-directions gives 95.1%, so the figure equals its chance level. The paper states no chance level for it. |
| directional-units | partially_reproduced | 46.2% and 24.3% are outside tolerance; GPi is directional more often than VLa (chi-squared p = 1.7e-7, cell 43). Chance at p < 0.005 is 0.5%, so both are far above it. |
| fig4-ccf-rare | not_reproduced | KS permutation p = 0.003 for whole recordings and 0.045 for movement, 0.705 for rest (cell 47). The paper's chance level of 5% significant pairs holds (5.6%, 3.4%, 6.5%; binomial tests not significant). Significant peaks are mostly positive (+15/−4). |
| fig4-noise-corr-rare | not_reproduced | KS p < 0.0025 in both periods. 10.1% and 10.8% of pair-targets are significant, about twice the paper's 5% chance level (cell 49). |
| fig5-vla-decrease-after-gpi-bursts | not_reproduced | For all three event types the population average never falls below the corrected band (dips of −1.9 to −2.5%, cell 51). Bursts last 67 ms against the paper's 24 ms, so this is weak evidence. |
| behavior-rt-mt | partially_reproduced | The movement-duration part holds: right longer, G slower, both p ≈ 0. Reaction time has an animal effect (p = 1e-4, cell 53). |
| figs3-emg-onset | blocked (methods_underspecified) | I agree. The S3 legend and Methods give no onset criterion. The EMG is in the Zenodo mirror (S3_EMGdata_NHP_G/I.mat) and not in the dandiset. A qualitative "onset before movement" could be tested there with any detector, but not the −123 and −135 ms values. |
| fig1-vla-localization | blocked (data_missing) | Confirmed in the archive. The asset metadata list only ElectricalSeries, ElectrodeGroup, ProcessingModule and Units, and no stimulation files are on Zenodo. A proxy (VLa- against VLp-labelled electrodes in electrode coordinates) is possible only if the electrode table has coordinates, which the notebook never shows. |
| fig6-simulation | blocked (other) | `Data_Fig6.mat` (the simulation output) is on Zenodo. The growth with c, the decline with N, and the fit to ((N−1)/N)c + 1/N could be checked on that stored output; that is a re-analysis of the authors' output, not a reproduction. |

**B. Problems**

1. [affects a conclusion] `detect` / `unit_direction` have a high false-positive rate. On synthetic stationary Poisson trains (5–70 spikes/s, 30–60 trials), the increase detector fires on 5–12% of unit-directions, the ISI decrease detector on 17–37%, and either one on 22–44%. The spurious onsets fall late (median between +2 and +127 ms). With two directions per unit, the chance level of "responsive" is roughly 40–70%. The notebook never measures it. This weakens mvt-responsive-fraction and the form claims, and probably explains late VLa decreases such as Gaia's +12.5 ms median. The notebook's decrease detector is also more liberal than the paper's stored output (330 against 286 decreases, 80.7% agreement, cell 17).
2. [affects a conclusion] `control_fit`: the OLS confidence interval on a smoothed, autocorrelated SDF calls 82–89% of slopes significant on stationary synthetic input. The 98.5% / 98.6% in hold-period-ramps is therefore indistinguishable from chance.
3. [affects a conclusion] Pseudo-replication (cell 13 onward). One unit per file, while 97 of the paper's records span 2–5 files. Both directions of a unit, and every pair built from a shared unit, are treated as independent. The counts are inflated (547 units against 394) and the p-values of all rank-sum, chi-squared and KS tests are anti-conservative. This bears on the borderline calls: fig3b p = 2e-4, monophasic p = 0.051, CCF movement p = 0.045.
4. [affects a conclusion] Cell 47 leaves out the Methods' exclusion of pairs with c0 > 0.3, so it runs on 338/298/306 pairs against the paper's 427/183/172. The lag and timing of the mostly positive significant peaks are never checked for shared artefacts.
5. [affects a conclusion] Cell 49 does not control for slow drift across the session, which trial shuffling destroys and which inflates |r|. Its significance band is pooled across pair-targets with different trial counts, not set per pair-target.
6. [affects a conclusion] Cell 51 / `bursts`: bursts come out 67 ms long against the paper's 24 ms. The choice of natural log was made partly because it moved durations toward the paper's (helper docstring). The paper's `Fig5_S14.m` is in the deposit but is not cited as read. Per-pair "significant" fractions of 44–51% against the paper's 8–12% suggest the per-pair test also differs from the paper's.
7. [affects a conclusion] Cell 53 runs the ANOVA on all 250 pre-MPTP files with trials, including M1, SMA and VLp-only files. The paper's degrees of freedom (452) imply about 228 sessions, so the reaction-time animal effect may come from file selection. Movement durations exist for only 32 Gaia files.
8. [does not affect a conclusion] `_lag_counts` bins with `np.floor(d*1000)` on floating-point differences. With ms-quantized spike times this makes every independent pair significant (my synthetic test: 100% significant, KS p = 0). Sample-resolution (24414 Hz) and continuous times behave correctly. The observed 5.6% suggests the dandiset's times are not ms-quantized, but the notebook never shows their resolution.
9. [does not affect a conclusion] Windowed CCFs (cell 47): jittered spikes can leave the 500 ms analysis windows. Synthetically this adds an offset of +0.0035, and 4 null runs gave non-significant KS tests.
10. [does not affect a conclusion] `valid_trials`: errors cannot be excluded in the files without `error_onset_time`, about half of them (cells 7–8).
11. [does not affect a conclusion] `ap_widths`: widths of 0.000 ms are kept in the means, 15 units are NaN, the 1.2 ms post-window caps the width, and the trace is 200 Hz filtered against the paper's 300 Hz. The channel-to-series match takes the first series with exactly one matching electrode and is not checked for channel ids repeated across probes.
12. [does not affect a conclusion] fig3a uses two-sided p = 0.079; one-sided (z = 1.75) would be p = 0.04 and make it partially reproduced. The paper's own z = 3.31 with p = 2.4e-5 is internally inconsistent.
13. [does not affect a conclusion] gating-conflict-fraction reproduces, but its value equals the shuffle reference (95.1%), so it carries no information about gating (cell 41).
14. [does not affect a conclusion] The clock check could not confirm 34 of the 163 files (cell 11). The rate criterion uses the span from first to last spike, not the recording length.

**C. What I could not check, and the output that would have settled it**

- Spike-time resolution: the fraction of `spikes*1000` that are integers, per file. This settles problem 8.
- Chance level of response detection on the real data: `detect` run on alignments to random times in the hold period, or on trial-shuffled data, reported as a chance responsive fraction and a chance onset distribution.
- Effect of pseudo-replication: every test re-run with one record per neuron, merging consecutive-file units with the same channel and sort letter, or using the paper's records.
- CCF artefacts: the lag of each significant peak, and the count of identical spike times in GPi–VLa pairs.
- Noise-correlation drift: the correlation of trial counts with trial index, and r after detrending.
- Electrode channel mapping for AP widths: the number of electrodes sharing a channel id per file.
- A fig1 proxy: the electrode-table columns, to see whether coordinates exist.
- Behaviour: the ANOVA restricted to the paper's files.
- Burst detector: a side-by-side of the helper's `bursts` with the code in `Fig5_S14.m`.

The paper's full text (PLOS JATS XML and a text extract) is saved under `paper/`.

## End of run

27 turns, 9 minutes, result: success.
