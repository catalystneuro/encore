# 001530 · claims · run 39597256645

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001530 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 152 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-026-73622-y.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41467-026-73622-y.txt').read()
print(t[55700:95000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import textwrap
t=open('paper/10.1038-s41467-026-73622-y.txt').read()
open('$TMPDIR/p.txt','w').write('\n'.join(textwrap.wrap(t,200)))"; wc -l $TMPDIR/p.txt; grep -n "Methods" $TMPDIR/p.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 280,
 "limit": 200
}
```

```
280	with ALM being largest (Supplementary Fig. 18 ). Discussion We developed a novel context-dependent tactile detection task for head-restrained mice in which identical deflections of the C2 whisker were
281	differentially processed to initiate goal-directed licking in the reward-predicting Go-tone context but to withhold licking in a Nogo-tone or a No-tone context. We established distinct contributions
282	of neuronal activity in different cortical regions through spatiotemporally-specific optogenetic inactivation, and we measured neuronal activity through high-density extracellular electrophysiological
283	recordings using Neuropixels probes finding diverse patterns of neuronal activity distributed across cortical areas. The auditory context was a brief pure tone presented 1 s before the whisker
284	deflection. In the late delay period just preceding whisker deflection and in the absence of orofacial movements, context was prominently represented in wM2 and ALM through persistent neuronal firing,
285	especially in the deep cortical layers of wM2 (Figs. 3 – 6 ). This finding is generally in good agreement with several studies showing persistent activity in frontal cortical areas involved in
286	different forms of short-term memory, when mice need either to postpone their response 25 , 48 or to maintain information about a preceding sensory stimulus in a delayed match to sample task 8 .
287	Interestingly, contextual information seems also to be represented in frontal areas in a block-designed rule-switching task in which the context is not explicitly indicated to the mice 31 . The
288	contextual activity we observed during the delay period in wM2 and ALM was involved in correct task performance because optogenetic inactivation of these areas caused a profound reduction in the
289	licking probability during the reporting period in Go-tone Whisker trials (Fig. 2 ). Whereas optogenetic inactivation of A1 and wM2 during the presentation of the Go-tone effectively disru
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 479,
 "limit": 50
}
```

```
479	components (PC1–PC2) to obtain neural trajectories, and focused subsequent analyses on the delay period (0.8–1.0 s after the auditory cue). Within this analysis window, we estimated a vector field of
480	population “velocity” in PC space by pooling observed positions and instantaneous velocities (ΔPC1, ΔPC2 between consecutive time bins) across trials. For each condition, the mean local velocity was
481	computed on a 2D grid using Gaussian distance-weighted averaging of nearby samples, yielding a smooth estimate of the flow field. To compare dynamics between conditions, we computed the angle between
482	the two condition-specific velocity vectors at each grid point (0° = aligned, 180° = opposite) and visualized this as an angle-difference map. To summarize this effect across sessions, we extracted a
483	one-dimensional profile of angle difference along the line connecting the two condition-specific population states, normalized distance so that the two whisker points (Go and Nogo condition)
484	corresponded to 0 and 1, averaged values within a narrow strip around this line, and finally reported the mean ± SEM across sessions for each area. Statistics Data are presented as mean ± SEM unless
485	otherwise indicated. Statistical analyses were conducted using MATLAB (MathWorks). For comparisons between two paired conditions (e.g., decoding accuracy vs. baseline within the same session), we used
486	the Wilcoxon signed-rank test. For unpaired comparisons between different groups (e.g., licking rates across trial types or neuron types), the Wilcoxon rank-sum test was applied. When comparing more
487	than two groups (e.g., modulation indices across cortical regions), the Kruskal–Wallis test was used first, followed by pairwise comparison using a multiple comparison test (Fisher’s least significant
488	difference procedure), where appropriate. We used the chi-squared statistic to compare proportions of neurons across areas. In decoding and ROC analyses that involved tim
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "supplementary" $TMPDIR/p.txt | sed -n '1,100p' | cut -c1-120; tail -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -l -i "supplement" claims/*/*.yaml | head -30; grep -h -i -m3 "supplement.*not\|not.*supplement" claims/*/*.yaml | head -20; ls transcripts | head; ls questions | head
```

```
claims/000003/10.1016-j.neuron.2016.12.011.yaml
claims/000005/10.1038-nn.4412.yaml
claims/000006/10.1038-s41586-018-0642-9.yaml
claims/000008/10.1038-s41586-020-2907-3.yaml
claims/000009/10.1038-nature22324.yaml
claims/000010/10.1038-nature14178.yaml
claims/000041/10.1016-j.neuron.2016.03.036.yaml
claims/000044/10.1126-science.aad1935.yaml
claims/000056/10.1038-nn.3968.yaml
claims/000059/10.1016-j.neuron.2020.05.023.yaml
claims/000061/10.1038-nn.4637.yaml
claims/000067/doi-10.1038-nn.2134.yaml
claims/000070/10.1038-nature11129.yaml
claims/000130/10.1016-j.neuron.2019.06.012.yaml
claims/000147/10.7554-elife.74478.yaml
claims/000207/10.1038-s41593-022-01020-w.yaml
claims/000213/10.1016-j.neuron.2018.04.028.yaml
claims/000218/10.1016-j.neuron.2019.10.012.yaml
claims/000226/10.1016-j.neuron.2017.03.045.yaml
claims/000239/10.1038-s41586-022-04478-7.yaml
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sL -m 30 https://zenodo.org/api/records/17973874 | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('version')); [print(f['key'], f['size']) for f in d.get('files',[])]" 2>&1 | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import urllib.request, struct, zipfile, io
url="https://zenodo.org/api/records/17973874/files/2026_Ghaderi_NCOMMS_Zenodo_data_code.zip/content"
def rng(a,b):
    r=urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}'})
    with urllib.request.urlopen(r,timeout=60) as f: return f.read(), f.headers
size=21212076245
tail,h=rng(size-65536,size-1)
print(h.get('Content-Range'))
i=tail.rfind(b'PK\x05\x06'); j=tail.rfind(b'PK\x06\x06')
print(i,j)
if j>=0:
    off=struct.unpack('<Q',tail[j+48:j+56])[0]; sz=struct.unpack('<Q',tail[j+40:j+48])[0]
else:
    sz,off=struct.unpack('<II',tail[i+12:i+20])
print(sz,off)
cd,_=rng(off,off+sz-1)
open('cd.bin','wb').write(cd)
p=0;names=[]
while p<len(cd) and cd[p:p+4]==b'PK\x01\x02':
    n,e,c=struct.unpack('<HHH',cd[p+28:p+34]); csz,usz=struct.unpack('<II',cd[p+20:p+28]); lo=struct.unpack('<I',cd[p+42:p+46])[0]
    name=cd[p+46:p+46+n].decode('utf8','replace'); names.append((name,usz,csz,lo,cd[p+46+n:p+46+n+e]))
    p+=46+n+e+c
print(len(names))
import pickle; pickle.dump(names,open('names.pkl','wb'))
for nm in names:
    if not nm[0].lower().endswith(('.nwb','.mat','.npy','.h5','.avi','.mp4','.csv','.pkl','.png','.tif','.fig')): print(nm[0],nm[1])
EOF
```

```
<persisted-output>
Output too large (134.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e2a7be1f-0197-4fec-8d91-c6ecc64cb0de/tool-results/b6nrsfdiu.txt

Preview (first 2KB):
bytes 21212010709-21212076244/21212076245
65514 65438
302040 21211774107
1942
data_electrophysiology/ 0
data_helpers/ 0
data_optogenetics/ 0
functions/ 0
functions/.DS_Store 8196
functions/addGloubalCluIsterID.m 333
functions/allenCCF/ 0
functions/allenCCF/.gitignore 31
functions/allenCCF/annotation_10.nrrd 69514309
functions/allenCCF/Browsing Functions/ 0
functions/allenCCF/Browsing Functions/addAllenCtxOutlines.m 1471
functions/allenCCF/Browsing Functions/aggregateAcr.m 5831
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import pickle
n=pickle.load(open('names.pkl','rb'))
for x in n:
  s=x[0]
  if 'allenCCF' in s or 'bombcell' in s.lower() or 'UniversalProbe' in s or 'npy-matlab' in s: continue
  print(s,x[1])
" | grep -v -i "libsvm\|/\.DS\|__MACOSX" | head -300
```

```
data_electrophysiology/ 0
data_electrophysiology/sub-PG019_ses-20200904T224847-processed-behavior.nwb 266001656
data_electrophysiology/sub-PG019_ses-20200906T175456-processed-behavior.nwb 267739400
data_electrophysiology/sub-PG027_ses-20210403T115220-processed-behavior.nwb 383602957
data_electrophysiology/sub-PG027_ses-20210404T111739-processed-behavior.nwb 316176171
data_electrophysiology/sub-PG028_ses-20210318T163504-processed-behavior.nwb 437667950
data_electrophysiology/sub-PG028_ses-20210319T135422-processed-behavior.nwb 439114870
data_electrophysiology/sub-PG030_ses-20210405T163808-processed-behavior.nwb 289685549
data_electrophysiology/sub-PG030_ses-20210406T164509-processed-behavior.nwb 208191618
data_electrophysiology/sub-PG030_ses-20210407T211250-processed-behavior.nwb 209645807
data_electrophysiology/sub-PG030_ses-20210408T223046-processed-behavior.nwb 116244536
data_electrophysiology/sub-PG030_ses-20210410T012800-processed-behavior.nwb 118709015
data_electrophysiology/sub-PG032_ses-20210711T175822-processed-behavior.nwb 247931396
data_electrophysiology/sub-PG032_ses-20210712T185829-processed-behavior.nwb 267837114
data_electrophysiology/sub-PG032_ses-20210715T223447-processed-behavior.nwb 293150152
data_electrophysiology/sub-PG038_ses-20210316T152753-processed-behavior.nwb 234211810
data_electrophysiology/sub-PG038_ses-20210317T180556-processed-behavior.nwb 177172759
data_electrophysiology/sub-PG061_ses-20220211T222307-processed-behavior.nwb 425234112
data_electrophysiology/sub-PG061_ses-20220212T233813-processed-behavior.nwb 389682867
data_electrophysiology/sub-PG062_ses-20220206T200225-processed-behavior.nwb 208634335
[... 286 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import pickle
n=pickle.load(open('names.pkl','rb'))
for x in n:
  s=x[0]
  if s.startswith(('data_','functions/allenCCF','functions/NeurodataWithout','functions/colors')) or 'libsvm' in s.lower() or 'bombcell' in s.lower() or '.DS_Store' in s or '__MACOSX' in s: continue
  print(s,x[1])
"
```

```
<persisted-output>
Output too large (68.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e2a7be1f-0197-4fec-8d91-c6ecc64cb0de/tool-results/bwrkx12oy.txt

Preview (first 2KB):
functions/ 0
functions/addGloubalCluIsterID.m 333
functions/angleBtwNDVectors.m 658
functions/bin_spike_counts.m 1196
functions/classify_layers.m 1076
functions/compute_layer_stats_pg.m 8412
functions/compute_mean_corr.m 1529
functions/costumcolor_shade.m 511
functions/custom_cmap.m 1378
functions/fn_gram_schmidt_process.m 351
functions/hex2rgb.m 2945
functions/legend_just_txt.m 3078
functions/legend_just_txt_bar.m 2754
functions/manual_colormap.asv 889
functions/manual_colormap.m 918
functions/movaverage_pg.m 190
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import pickle
n=pickle.load(open('names.pkl','rb'))
for x in n:
  s=x[0]
  if s.startswith(('data_','functions/')) : continue
  if s.endswith('/') or '.DS_Store' in s: continue
  print(s,x[1])
" | head -200
```

```
Main_figures_codes/Ghaderi2025_Figure1_c_Performance.m 6089
Main_figures_codes/Ghaderi2025_Figure1_d_Movements_AllTrials.m 10478
Main_figures_codes/Ghaderi2025_Figure1_e_Movements_QuietTrials.m 10487
Main_figures_codes/Ghaderi2025_Figure1_f_Movements_Hit.m 10129
Main_figures_codes/Ghaderi2025_Figure2_b_Heatmaps.m 7821
Main_figures_codes/Ghaderi2025_Figure2_c_Brainmaps.m 15729
Main_figures_codes/Ghaderi2025_Figure2_d_Plick_Sessions.m 20056
Main_figures_codes/Ghaderi2025_Figure3_a_brainmap_activity.m 15334
Main_figures_codes/Ghaderi2025_Figure3_b_PSTH_brainareas.m 10077
Main_figures_codes/Ghaderi2025_Figure3_c_roc_hit.m 10098
Main_figures_codes/Ghaderi2025_Figure3_d_PSTH_depth.ipynb 41193
Main_figures_codes/Ghaderi2025_Figure4_a&b_heatmaps_psths.ipynb 41801
Main_figures_codes/Ghaderi2025_Figure5_a_SingleNeuron.m 15487
Main_figures_codes/Ghaderi2025_Figure5_b_Decoding.m 9918
Main_figures_codes/Ghaderi2025_Figure5_c_Dropcluster11.m 6638
Main_figures_codes/Ghaderi2025_Figure5_c_DropoutClusters_heatmap.m 5828
Main_figures_codes/Ghaderi2025_Figure5_d_DecodingSubspaces.m 10783
Main_figures_codes/Ghaderi2025_Figure6_a_pca.m 13113
Main_figures_codes/Ghaderi2025_Figure6_b_CD_context.m 7975
Main_figures_codes/Ghaderi2025_Figure6_c_temporalCorrelation.m 8266
[... 174 more lines not kept]
```

**Agent**

The code is in the Zenodo record (21 GB zip with data); I'll extract only the analysis scripts by range requests, without opening any data files.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p code && python3 - <<'EOF'
import urllib.request, struct, zlib, pickle, os
url="https://zenodo.org/api/records/17973874/files/2026_Ghaderi_NCOMMS_Zenodo_data_code.zip/content"
def rng(a,b):
    r=urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}'})
    with urllib.request.urlopen(r,timeout=120) as f: return f.read()
names=pickle.load(open('names.pkl','rb'))
for name,usz,csz,lo,extra in names:
    if not (name.startswith(('Main_figures_codes','processed_data_code','Supplementary_figures_codes')) or name in ('README.txt','functions/compute_layer_stats_pg.m','functions/compute_mean_corr.m','functions/bin_spike_counts.m','functions/classify_layers.m','functions/fn_gram_schmidt_process.m')): continue
    if name.endswith('/'): continue
    # zip64 extra
    p=0
    while p<len(extra):
        hid,hl=struct.unpack('<HH',extra[p:p+4]); d=extra[p+4:p+4+hl]
        if hid==1:
            vals=[];q=0
            if usz==0xFFFFFFFF: usz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if csz==0xFFFFFFFF: csz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if lo==0xFFFFFFFF: lo=struct.unpack('<Q',d[q:q+8])[0];q+=8
        p+=4+hl
    h=rng(lo,lo+29)
    meth=struct.unpack('<H',h[8:10])[0]; n,e=struct.unpack('<HH',h[26:30])
    data=rng(lo+30+n+e, lo+30+n+e+csz-1) if csz else b''
    if meth==8: data=zlib.decompress(data,-15)
    out=os.path.join('code',name); os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'wb').write(data)
print('done')
EOF
ls -R code | head; cat code/README.txt
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
  File "<stdin>", line 5, in rng
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 533, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 466, in _call_chain
    result = func(*args)
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/urllib/request.py", line 613, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 429: TOO MANY REQUESTS
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import urllib.request, urllib.error, struct, zlib, pickle, os, time
url="https://zenodo.org/api/records/17973874/files/2026_Ghaderi_NCOMMS_Zenodo_data_code.zip/content"
def rng(a,b):
    for k in range(20):
        try:
            r=urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}'})
            with urllib.request.urlopen(r,timeout=120) as f: return f.read()
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(15); continue
            raise
names=pickle.load(open('names.pkl','rb'))
for name,usz,csz,lo,extra in names:
    if not (name.startswith(('Main_figures_codes','processed_data_code','Supplementary_figures_codes')) or name in ('README.txt','functions/compute_layer_stats_pg.m','functions/compute_mean_corr.m','functions/bin_spike_counts.m','functions/classify_layers.m','functions/fn_gram_schmidt_process.m')): continue
    out=os.path.join('code',name)
    if name.endswith('/') or (os.path.exists(out) and os.path.getsize(out)>0): continue
    p=0
    while p<len(extra):
        hid,hl=struct.unpack('<HH',extra[p:p+4]); d=extra[p+4:p+4+hl]
        if hid==1:
            q=0
            if usz==0xFFFFFFFF: usz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if csz==0xFFFFFFFF: csz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if lo==0xFFFFFFFF: lo=struct.unpack('<Q',d[q:q+8])[0];q+=8
        p+=4+hl
    h=rng(lo,lo+29)
    meth=struct.unpack('<H',h[8:10])[0]; n,e=struct.unpack('<HH',h[26:30])
    data=rng(lo+30+n+e, lo+30+n+e+csz-1) if csz else b''
    if meth==8: data=zlib.decompress(data,-15)
    os.makedirs(os.path.dirname(out),exist_ok=True)
    open(out,'wb').write(data); time.sleep(1)
print('done')
EOF
find code -type f | wc -l; cat code/README.txt
```

```
done
90
*************************************************
*************************************************
*************************************************
DATA AND CODE FOR
Contextual gating of whisker-evoked responses by frontal cortex supports flexible decision making.
Nature Communications 2026
doi https://doi.org/10.1038/s41467-026-73622-y

Written by Parviz Ghaderi, Sylvain Crochet and Carl C.H. Petersen
2026.04.20
Laboratory of Sensory Processing
Brain Mind Institute
Ecole Polytechnique Federale de Lausanne (EPFL)
Switzerland.
*************************************************
*************************************************
*************************************************

[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat processed_data_code/psth_10ms.m
```

```
%% =========================================================================
% psth_10ms.m
% =========================================================================
% 
% This script processes NWB files to extract PSTH data with 10ms time bins
% for the manuscript "Contextual gating of whisker-evoked responses by frontal cortex supports flexible decision making" 
% (Parviz Ghaderi, Sylvain Crochet, Carl Petersen, 2025)
% 
% Code Author: Parviz Ghaderi
% Email: [removed: an e-mail address]
% Date: 2025
%
% Description: This script loads NWB files, extracts behavioral and neural data,
% calculates PSTHs with 10ms bins, identifies quiet trials, and organizes data
% into a structured format for further analysis.
%
% Dependencies: 
%   - matnwb package (for reading NWB files)
%   - PSTHBehavior.m (for behavioral PSTH calculation)
%   - nwb_findQuietTrial.m (for quiet trial identification)
[... 234 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import pickle
n=pickle.load(open('names.pkl','rb'))
for x in n:
  s=x[0]
  if s.startswith('functions/') and s.count('/')==1: print(s,x[1])
  if 'subspaceID' in s and s.endswith(('.m','.md')): print(s,x[1])
"
```

```
<persisted-output>
Output too large (41.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/e2a7be1f-0197-4fec-8d91-c6ecc64cb0de/tool-results/bojxmsecw.txt

Preview (first 2KB):
functions/ 0
functions/.DS_Store 8196
functions/addGloubalCluIsterID.m 333
functions/angleBtwNDVectors.m 658
functions/bin_spike_counts.m 1196
functions/classify_layers.m 1076
functions/compute_layer_stats_pg.m 8412
functions/compute_mean_corr.m 1529
functions/costumcolor_shade.m 511
functions/custom_cmap.m 1378
functions/fn_gram_schmidt_process.m 351
functions/hex2rgb.m 2945
functions/legend_just_txt.m 3078
functions/legend_just_txt_bar.m 2754
functions/manual_colormap.asv 889
functions/manual_colormap.m 918
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import urllib.request, urllib.error, struct, zlib, pickle, os, time
url="https://zenodo.org/api/records/17973874/files/2026_Ghaderi_NCOMMS_Zenodo_data_code.zip/content"
def rng(a,b):
    for k in range(20):
        try:
            r=urllib.request.Request(url,headers={'Range':f'bytes={a}-{b}'})
            with urllib.request.urlopen(r,timeout=120) as f: return f.read()
        except urllib.error.HTTPError as e:
            if e.code==429: time.sleep(15); continue
            raise
names=pickle.load(open('names.pkl','rb'))
want=['nwb_findQuietTrial.m','pg_decompose.m','PSTHBehavior.m','PSTH_Simple.m','P_value.m','selectivity_index_calculation.m','trial_typeMaker.m']
for name,usz,csz,lo,extra in names:
    if not (name.startswith('functions/') and name.count('/')==1 and name.endswith('.m')): continue
    out=os.path.join('code',name)
    if os.path.exists(out): continue
    p=0
    while p<len(extra):
        hid,hl=struct.unpack('<HH',extra[p:p+4]); d=extra[p+4:p+4+hl]
        if hid==1:
            q=0
            if usz==0xFFFFFFFF: usz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if csz==0xFFFFFFFF: csz=struct.unpack('<Q',d[q:q+8])[0];q+=8
            if lo==0xFFFFFFFF: lo=struct.unpack('<Q',d[q:q+8])[0];q+=8
        p+=4+hl
    h=rng(lo,lo+29)
    meth=struct.unpack('<H',h[8:10])[0]; n,e=struct.unpack('<HH',h[26:30])
    data=rng(lo+30+n+e, lo+30+n+e+csz-1) if csz else b''
    if meth==8: data=zlib.decompress(data,-15)
    open(out,'wb').write(data); time.sleep(1)
EOF
ls code/functions; cd code/functions; cat nwb_findQuietTrial.m PSTH_Simple.m P_value.m selectivity_index_calculation.m; ls | grep -i trial
```

```
PSTHBehavior.m
PSTH_Simple.m
P_value.m
SC_Scale2Color.m
addGloubalCluIsterID.m
angleBtwNDVectors.m
bin_spike_counts.m
classify_layers.m
compute_layer_stats_pg.m
compute_mean_corr.m
costumcolor_shade.m
custom_cmap.m
fn_gram_schmidt_process.m
hex2rgb.m
legend_just_txt.m
legend_just_txt_bar.m
manual_colormap.m
movaverage_pg.m
movsum_pg.m
nwb_findQuietTrial.m
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat functions/trial_typeMaker.m; grep -v "^\s*%" Main_figures_codes/Ghaderi2025_Figure1_c_Performance.m | grep -v "^\s*$" | head -150
```

```
function trial_type=trial_typeMaker(whisker_stim,context)

for itrail=1:length(whisker_stim)
stim=whisker_stim(itrail);
tone=context(itrail);

if stim==1 & strcmp(tone,'go_tone')
  trial_type(itrail)  =1;
end

if stim==0 & strcmp(tone,'go_tone')
  trial_type(itrail)  =2;
end

if stim==1 & strcmp(tone,'nogo_tone')
  trial_type(itrail)  =3;
end

if stim==0 & strcmp(tone,'nogo_tone')
  trial_type(itrail)  =4;
[... 85 more lines not kept]
```

**Agent**

Fig. 1c code read (per-session P(lick) over completed trials, all trials, mean ± SEM). Continuing with Fig. 1f and the optogenetics code.

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(" ; }; s Main_figures_codes/Ghaderi2025_Figure1_f_Movements_Hit.m | head -120
```

```
clear all
close all
clc
change_name = 0;
newname = 'Figure3_4_1';
fullname = mfilename('fullpath');
inds = regexp(fullname, '\', 'all');
name = fullname(inds(end)+1:end);
if change_name
    movefile([name '.m'], [newname '.m']);
end
CurrentDir=pwd;
directory=[CurrentDir];
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
close all;
parent = figure('Position', [100 100 600 800]);
h = tight_subplot(1, 1, [.15 .15], [.1 .1], [.1 .1]);
axs = findall(gcf, 'type', 'axes');
axs = flipud(axs);
params.QuietState = 'Quiet_(jaw & whisker)';  % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(" ; }; s Main_figures_codes/Ghaderi2025_Figure1_f_Movements_Hit.m | sed -n '120,200p'; echo ======; s Supplementary_figures_codes/Ghaderi2025_Sup_Figure1_b_SpoutReactionTime.m | sed -n '20,120p'
```

```
numberoftrials{icond, 1} = num2str(size(signal2plot, 2));
    end % End condition loop
end % End signal loop
xline(axs(1), 1);
plot(h(1), [1.03 1.03], [-0.2 1.2], '--', 'color', [0.5 0.5 0.5], 'linewidth', 1);
xticklabels(h(1), XTickLabel);
yticklabels(get(h(1), 'YTick'));
    'Xoffset', 1, 'Yoffset', 8, 'relX', 0, 'relY', 0.02, 'type', 'line');
    'PointSize', 3, 'GeneralFontSize', 12);
directory=[CurrentDir filesep 'Main_figures_pdf' filesep];
======
params.completion_state = 'completed_trials';  % Options: 'early_licks', 'completed_trials'
params.TrialType = [1, 2, 3, 4, 5];  % 1: gotone/whisker, 2: gotone/nowhisker, 3: nogotone/whisker, 4: nogotone/nowhisker, 5: notone/whisker
trialtype_names = {'Go-tone Whisker'; 'Go-tone'; 'Nogo-tone Whisker'; 'Nogo-tone'; 'Whisker'};
xtick = [1:5];
colorcodes = [0 0 1; 0 .8 1; 1 0 0; 1 .5 0; .5 .5 .5];
params.colortype = {'wS1'; 'wS2'; 'CR2'; 'ALM'; 'CR4'; 'wM2'; 'FA2'; 'FA3'; 'FA4'; 'FA5'; 'Lick'; 'NoLick'; 'A1'; 'tjM1'};
shift_y_values = [0, 10, 20, 40, 65];
[unique_session_names, unique_session_ids] = unique([psth_mat.session_id]);
for icond = 1:length(params.TrialType)
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n -i "20\b\|0\.2\|max\|latency\|onset" Supplementary_figures_codes/Ghaderi2025_Sup_Figure1_d_DeeplabCut.m | head -40
```

```
299:    prettify_addScaleBars(.5, 20, '500 ms', '20', [], [], [], [], [], axs(1));
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(" ; }; s processed_data_code/Optoinhibition_mat.m; echo =====; s Main_figures_codes/Ghaderi2025_Figure2_d_Plick_Sessions.m
```

```
clear all
close all
clc
CurrentDir=pwd;
directory=[CurrentDir];
directory=[CurrentDir filesep 'data_optogenetics' filesep];
rng(0)
Iprb = 1;                                 % Probe counter
optomat = [];                             % Initialize output structure
nwb_file_address = dir([directory '\*.nwb']);
for ind_nwb = 1:length(nwb_file_address)
    curr_nwbfile = (nwb_file_address(ind_nwb).name);
    nwb = nwbRead([nwb_file_address(ind_nwb).folder '\' nwb_file_address(ind_nwb).name]);
    trials_table = nwb.intervals_trials.toTable;
    columnname_trial = fieldnames(trials_table);
    columnname_trial = columnname_trial(2:end-3);
    currarea_name = unique(trials_table.opto_area);
    currarea_name(strcmp(currarea_name, 'nan')) = [];  % Remove NaN values
    optomat(Iprb).session_id{:} = [nwb.identifier];
    optomat(Iprb).fiber_location = cell2mat(currarea_name);
[... 306 more lines not kept]
```

**Agent**

The optogenetics code uses 10,000 bootstrap iterations where the Methods say 1,000; the reported p-values (minimum 0.0003) fit 10,000. Checking whether the code holds the wM2 vs ALM comparison.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -rln "chi2\|crosstab\|chi-squared\|chisq" . ; grep -rn "ttest2" . | head; grep -rln "wM2.*ALM\|0.009" Main_figures_codes Supplementary_figures_codes | head
```

```
./Main_figures_codes/Ghaderi2025_Figure3_c_roc_hit.m
./functions/compute_layer_stats_pg.m:133:        [~, p_val, ~, stats_struct] = ttest2(data1, data2, 'Vartype','equal');
Main_figures_codes/Ghaderi2025_Figure8_b_SpontLick_CD_LickvsNolick.m
Main_figures_codes/Ghaderi2025_Figure8_a_CD_LickvsNolick.m
Main_figures_codes/Ghaderi2025_Figure7_d_ContextDecoding_WS.m
Main_figures_codes/Ghaderi2025_Figure7_c_StimCD.m
Main_figures_codes/Ghaderi2025_Figure7_b_DeltaFR.m
Main_figures_codes/Ghaderi2025_Figure7_a_WhiskerEvoked_psths.m
Main_figures_codes/Ghaderi2025_Figure6_c_temporalCorrelation.m
Main_figures_codes/Ghaderi2025_Figure6_b_CD_context.m
Main_figures_codes/Ghaderi2025_Figure6_a_pca.m
Main_figures_codes/Ghaderi2025_Figure5_d_DecodingSubspaces.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(" ; }; s processed_data_code/Modulation.m; echo ====; s Main_figures_codes/Ghaderi2025_Figure3_c_roc_hit.m
```

```
clear all
close all
clc
CurrentDir=pwd;
directory=[CurrentDir];
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
rng(0)
params.QuietState = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.BaselineSubtraction = 0;
params.completion_state = 'completed_trials';   % Options: 'early_licks', 'completed_trials'
params.TrialType = [1];   % 1: gotone/whisker
params.LickState = [1];  % lick 1: lick
params.CellType = 'All';           % Options: 'RS', 'FS', 'RS_FS', 'All'
params.regionlist = {'A1', 'wS1', 'ALM', 'wM2', 'wS2'};
t_start = -1;  % Start time (seconds)
t_end = 2;     % End time (seconds)
bin_width = 0.01;  % 10ms bins
XTickLabel = {'-1'; '0'; '1'; '2'};
xtick = [-1; 0; 1; 2];
window_name = {'audio', 'delay', 'whisker', 'lick'};
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat functions/compute_layer_stats_pg.m functions/classify_layers.m | grep -v "^\s*$"; python3 -c "
import json
nb=json.load(open('Main_figures_codes/Ghaderi2025_Figure3_d_PSTH_depth.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code': print(''.join(c['source'])[:3000]); print('-----')
" | grep -v "^\s*$" | grep -v -i "ax\.\|plt\.\|color\|fontsize" | head -300
```

```
function [layer_activity_results, statistical_results, summary_table, comparison_table] = ...
    compute_layer_stats_pg(psth_hz, area_all, layer_class, bin_sz)
% COMPUTE_LAYER_STATS_PG
%   MATLAB version of your Python layer-specific statistics.
%
% Inputs:
%   psth_hz      : [N_neurons x N_timebins] firing rates (Hz)
%   area_all     : {N_neurons x 1} area names ('A1','wS1','wS2','wM2','ALM',...)
%   layer_class  : {N_neurons x 1} 'supragranular'/'granular'/'infragranular'
%   bin_sz       : scalar, bin width in seconds (e.g. 0.01)
%
% Outputs:
%   layer_activity_results : struct(area).(layer) -> vector of neuron means
%   statistical_results    : struct(area).comparison -> stats (t,p,d,means,n)
%   summary_table          : table with mean ± SEM per layer & region
%   comparison_table       : table with t, p, d, significance for each pair
%% Time window for analysis (1.8–2.0 s)
time_window_start = 1.8;   % seconds
time_window_end   = 2.0;   % seconds
% Approximate bin indices (similar spirit to Python code)
[... 518 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(" ; }; s processed_data_code/Neuronal_data_10ms.m | grep -v "case\|Qind =\|completion_state =\|CelltypeInd =\|switch\|end$\|early_licks_all\|lick_time =" | head -120
```

```
clear all
close all
clc
CurrentDir=pwd;
directory=[CurrentDir];
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
load([directory filesep 'data_helpers' filesep 'Area_list.mat'])
rng(0)
params.QuietState = 'Quiet_(whisker_speed)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.normalization = 0;                     % Enable normalization (0: disabled, 1: enabled)
baselinesubtraction=1
params.TrialType = [1, 2, 3, 4, 5];            % 1: gotone/whisker, 2: gotone/nowhisker, 3: nogotone/whisker, 4: nogotone/nowhisker, 5: notone/whisker
params.LickState = [1, 0, 0, 0, 0];            % lick 1: lick, 0: nolick
params.CellType = 'All';                        % Options: 'RS', 'FS', 'RS_FS', 'All'
params.regionlist = {'A1', 'wM2', 'wS1', 'ALM', 'wS2'};  % Brain regions to analyze
params.min_cells_per_session = 5;              % Minimum cells required per session
params.min_trials_per_condition = 3;           % Minimum trials required per condition
t_start = -1;  % Start time (seconds)
t_end = 2;     % End time (seconds)
bin_width = 0.01;  % 10ms bins
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf" ; }; s processed_data_code/Decoding_delay.m | grep -v "case '\|Qind = \|CelltypeInd = \|early_licks_all\|lick_time = "
```

```
clear all
close all
clc
CurrentDir=pwd;
directory=[CurrentDir];
load([directory filesep 'data_helpers' filesep 'area_list.mat'])
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
rng(0)
params.quietstate = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.BaselineSubtraction = 0;  % 0: no baseline subtraction
params.completion_state = 'completed_trials';   % Options: 'early_licks', 'completed_trials'
params.TrialType = [1, 2, 3, 4, 5];   % 1: gotone/whisker, 2: gotone/nowhisker, 3: nogotone/whisker, 4: nogotone/nowhisker, 5: notone/whisker
params.LickState = [1, 0, 0, 0, 0];  % lick 1: lick, 0: nolick
params.celltype = 'All';           % Options: 'RS', 'FS', 'RS_FS', 'All'
params.regionlist = {'A1', 'wM2', 'wS1', 'ALM', 'wS2'};       % Brain regions to analyze
params.t_start = -1;  % Start time (seconds)
params.t_end = 2;     % End time (seconds)
params.bin_width = 0.01;  % 10ms bins
params.XTickLabel = {'-1'; '0'; '1'; '2'};
params.xtick = [-1; 0; 1; 2];
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf" ; }; diff <(s processed_data_code/Decoding_delay.m) <(s processed_data_code/Decoding_NbNeurons5_50.m); echo ====; s Main_figures_codes/Ghaderi2025_Figure5_b_Decoding.m | sed -n '10,200p'
```

```
38c38
<     session_counter = 0;
---
>     session_counter = 1;
40c40
<         session_counter = session_counter + 1;
---
>         session_counter;
79,81d78
<         if sum(CurrCellInd) < 5   % For condition in FS there is one session which has just 1 FS cell
<             continue
<         end
83,97c80,86
<         Currsig_CurrCellInd = Currsig(:, :, CurrCellInd);
<         classnames = fieldnames(Ind);
<         for iClass = 1:length(classnames)
<             theseIndices = Ind.(cell2mat(classnames(iClass)));
<             Value.(cell2mat(classnames(iClass))) = Currsig_CurrCellInd(:, theseIndices, :);
<         end
<         for iBin = 1:size(Value.Class1(:, :, :), 1)
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf\|mySMOTE\|dataset\|tabulate\|uniqueLabels\|labelCounts\|table2array" ; }; s processed_data_code/Decoding_clusters_random_dropout.m | sed -n '1,200p' | grep -v "case '\|Qind = \|CelltypeInd = \|early_licks_all\|lick_time = " | sed -n '18,120p'
```

```
params.TrialType = [1, 2, 3, 4, 5];   % 1: gotone/whisker, 2: gotone/nowhisker, 3: nogotone/whisker, 4: nogotone/nowhisker, 5: notone/whisker
    params.LickState = [1, 0, 0, 0, 0];  % lick 1: lick, 0: nolick
    params.celltype = 'All';           % Options: 'RS', 'FS', 'RS_FS', 'All'
    params.regionlist = {'A1', 'wM2', 'wS1', 'ALM', 'wS2'};       % Brain regions to analyze
    params.t_start = -1;  % Start time (seconds)
    params.t_end = 2;     % End time (seconds)
    params.bin_width = 0.01;  % 10ms bins
    params.XTickLabel = {'-1'; '0'; '1'; '2'};
    params.xtick = [-1; 0; 1; 2];
    params.balance_method = 'downsample';
    params.mintrial = 5;
    params.Folds = 10;
    params.preTime = -1;
    params.postTime = 2;
    params.BinSize = 0.01;
    params.BinStep = 0.01;
    params.normalization = 0;
    params.zscoring = 1;  % Do zscore on feature matrix
    params.Separation = 0;
    params.spikecount = 1;    % 1: spike count, 0: rate
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf" ; }; head -c 1500 processed_data_code/Decoding_clusters_random_dropout.m | tail -c 900; s processed_data_code/Decoding_clusters_random_dropout.m | sed -n '1,17p'; s processed_data_code/Decoding_clusters_random_dropout.m | tail -20; echo =====; s Main_figures_codes/Ghaderi2025_Figure5_c_Dropcluster11.m | sed -n '10,100p'
```

```
decoding using SVM
% with cluster-based random dropout analysis. It systematically removes
% specific clusters of neurons and evaluates decoding performance, comparing
% it to random dropout scenarios. The analysis includes both original cluster
% dropout and random selection dropout for validation.
%
% Dependencies: 
%   - psth_10ms.mat (contains trial data)
%   - area_list.mat (contains brain area information)
%   - Data_Clustering.mat (contains cluster information)
%   - mySMOTE.m (for data balancing)
%   - svmtrain/svmpredict (LIBSVM functions)
%
% Input: Processed PSTH data and cluster information
% Output: Decoding accuracy results saved to Decoding_clusters_dropout_mndropout.mat
%         and Decoding_clusters_random_dropout.mat
% =========================================================================

%%
clear all
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 30 https://api.dandiarchive.org/api/dandisets/001530/ | python3 -c "import json,sys; d=json.load(sys.stdin); v=d.get('most_recent_published_version') or d.get('draft_version'); print(v)"; curl -s -m 30 https://api.dandiarchive.org/api/dandisets/001530/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(m.get('assetsSummary',{}).get('numberOfFiles'), m.get('assetsSummary',{}).get('numberOfSubjects'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/LSENS-BMI-EPFL/Ghaderi_et_al_NCOMMS_2026.git gh 2>&1 | tail -2; cd gh && git log -1 --format="%H %cd" && ls && find . -name "*.m" -o -name "*.ipynb" | wc -l && for f in $(cd ../code && find Main_figures_codes processed_data_code -type f); do [ -f "$f" ] && (cmp -s "$f" "../code/$f" || echo "DIFF $f") || echo "MISSING $f"; done 2>/dev/null | head
```

```
20cf10c7b95069c12f762b7dd89817beedcc382f Fri Jun 5 15:51:26 2026 +0200
Main_figures_codes
Main_figures_pdf
README.md
Supplementary_figures_codes
Supplementary_figures_pdf
data_electrophysiology
data_helpers
data_optogenetics
functions
processed_data
processed_data_code
926
Shell cwd was reset to
```

**Agent**

GitHub repo (commit 20cf10c) holds the same analysis code as Zenodo. Continuing with Figs. 5d to 8.

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf\|mySMOTE\|dataset\|tabulate\|uniqueLabels\|labelCounts\|table2array\|case '\|Qind = \|CelltypeInd = \|early_licks_all\|lick_time = " ; }; s processed_data_code/Movement_subspace_Define.m | sed -n '5,200p'; echo ====; diff <(s processed_data_code/Decoding_delay.m) <(s processed_data_code/Movement_subspace_Decoding_null.m) | head -80
```

```
directory=[CurrentDir];
load([directory filesep 'data_helpers' filesep 'area_list.mat'])
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
rng(0)
[filepath, ~, ~] = fileparts(mfilename('fullpath'));
cd(filepath);
change_name = 0;
newname = 'Figure3_4_1';
fullname = mfilename('fullpath');
inds = regexp(fullname, '\', 'all');
name = fullname(inds(end) + 1:end);
if change_name
    movefile([name '.m'], [newname '.m']);
end
params.QuietState = 'All_trials';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.BaselineSubtraction = 0;
params.completion_state = 'completed_trials';   % Options: 'early_licks', 'completed_trials'
params.TrialType = [1, 3];   % 1: gotone/whisker, 3: nogotone/whisker
params.LickState = [1, 0];  % lick 1: lick, 0: nolick
params.CellType = 'All';           % Options: 'RS', 'FS', 'RS_FS', 'All'
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*$" functions/pg_decompose.m | grep -v "^\s*%" | head -90; grep -n "Win\|signrank\|P_value" Main_figures_codes/Ghaderi2025_Figure5_d_DecodingSubspaces.m | head
```

```
function [rez]=pg_decompose(Data)
manoptPath = pwd; % path to manopt 
addpath(genpath(fullfile(manoptPath,'manopt')))
nBins = size(Data.seq,1);
nTrials = size(Data.seq,2);
nNeurons = size(Data.seq,3);
temp = reshape(Data.seq,nBins*nTrials,nNeurons);
N.full_cat = zscore(temp); % (time bins * nTrials, nNeurons)
N.full= reshape(N.full_cat,nBins,nTrials,nNeurons); % (time bins, nTrials, nNeurons)
moveMask = Data.moveMask(:); %(time bins * nTrials)
N.null = N.full_cat(~moveMask,:);
N.potent = N.full_cat(moveMask,:);
rez.N = N; % put data into a results struct
rez.cov.null = cov(N.null);
rez.cov.potent = cov(N.potent);
rez.dNull = 10;
rez.dPotent = 10;
rez.dMax = max([rez.dNull, rez.dPotent]);
rng(101) % for reproducibility
alpha = 0; % regularization hyperparam (+ve->discourage sparity, -ve->encourage sparsity)
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && s(){ grep -v "^\s*%" "$1" | grep -v "^\s*$" | grep -v -i "prettify\|xlabel\|ylabel\|xlim\|ylim\|xticks\|yticks\|colormap\|set(\|title(\|legend\|exportgraphics\|text(\|hold(\|colorbar\|axis(\|plot(\|scatter(\|errorbar(\|fill(\|bar(\|pie(\|fprintf\|case '\|Qind = \|CelltypeInd = \|early_licks_all\|lick_time = " ; }; s processed_data_code/Coding_direction_10ms.m | sed -n '6,400p'
```

```
load([directory filesep 'data_helpers' filesep 'area_list.mat'])
load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
params.quietstate = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trial'
params.BaselineSubtraction = 0;
params.completion_state = 'completed_trial';   % Options: 'early_licks', 'completed_trial'
params.trialType = [1, 2, 3, 4, 5];   % 1: gotone/whisker, 2: gotone/nowhisker, 3: nogotone/whisker, 4: nogotone/nowhisker, 5: notone/whisker
params.lickState = [1, 0, 0, 0, 0];  % lick 1: lick, 0: nolick
params.celltype = 'All';           % Options: 'RS', 'FS', 'RS-FS', 'All'
params.regionlist = {'ALM', 'wM2', 'wS2', 'wS1', 'A1'};       % Brain regions to analyze
params.t_start = -1;  % Start time (seconds)
params.t_end = 2;     % End time (seconds)
params.bin_width = 0.01;  % 10ms bins
params.XTickLabel = {'-1'; '0'; '1'; '2'};
params.xtick = [-1; 0; 1; 2];
params.balance_method = 'downsample';
params.mintrial = 5;
params.Folds = 10;
params.preTime = -1;
params.postTime = 2;
params.BinSize = 0.01; % 0.005 ????
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "CDcontext\|ProjContext(\|coding_direction_context =\|HoldOut" processed_data_code/Coding_direction_10ms.m processed_data_code/Coding_direction_5ms.m processed_data_code/Coding_direction_SpontLick.m | head -30
```

```
processed_data_code/Coding_direction_10ms.m:171:        cv = cvpartition(size(id1, 1), 'HoldOut', 0.7); idx = cv.test; id1Train = id1(~idx, :); id1Test = id1(idx, :);
processed_data_code/Coding_direction_10ms.m:172:        cv = cvpartition(size(id2, 1), 'HoldOut', 0.7); idx = cv.test; id2Train = id2(~idx, :); id2Test = id2(idx, :);
processed_data_code/Coding_direction_10ms.m:173:        cv = cvpartition(size(id3, 1), 'HoldOut', 0.7); idx = cv.test; id3Train = id3(~idx, :); id3Test = id3(idx, :);
processed_data_code/Coding_direction_10ms.m:174:        cv = cvpartition(size(id4, 1), 'HoldOut', 0.7); idx = cv.test; id4Train = id4(~idx, :); id4Test = id4(idx, :);
processed_data_code/Coding_direction_10ms.m:175:        cv = cvpartition(size(id5, 1), 'HoldOut', 0.7); idx = cv.test; id5Train = id5(~idx, :); id5Test = id5(idx, :);
processed_data_code/Coding_direction_10ms.m:179:        CDcontext = [];
processed_data_code/Coding_direction_10ms.m:183:            CDcontext(ind_bin, :) = (mean(X1) - mean(X2));
processed_data_code/Coding_direction_10ms.m:198:        coding_direction_context = nanmean(CDcontext(WContextFirstBin:WContextLasttBin, :), 1);
processed_data_code/Coding_direction_10ms.m:199:        coding_direction_context = coding_direction_context ./ norm(coding_direction_context);
processed_data_code/Coding_direction_10ms.m:218:        coding_direction_context = v(:, 1)';
processed_data_code/Coding_direction_10ms.m:227:            ProjContext(:, itrial) = curr * coding_direction_context';
processed_data_code/Coding_direction_10ms.m:230:        ProjContext(:, id_training_context) = nan;
processed_data_code/Coding_direction_5ms.m:185:        cv = cvpartition(size(id1, 1), 'HoldOut', 0.7); idx = cv.test; id1Train = id1(~idx, :); id1Test = id1(idx, :);
processed_data_code/Coding_direction_5ms.m:186:        cv = cvpartition(size(id2, 1), 'HoldOut', 0.7); idx = cv.test; id2Train = id2(~idx, :); id2Test = id2(idx, :);
processed_data_code/Coding_direction_5ms.m:187:        c
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in Main_figures_codes/Ghaderi2025_Figure6_b_CD_context.m Main_figures_codes/Ghaderi2025_Figure6_c_temporalCorrelation.m; do echo "=== $f"; grep -n "Win\|signrank\|P_value\|bonf\|\*\s*[0-9]\|Class\|expr\|trial ==\|QuietState\|quiet\|mean(\|load(" $f | grep -v "^\s*%" | head -50; done
```

```
=== Main_figures_codes/Ghaderi2025_Figure6_b_CD_context.m
49:load([directory filesep 'processed_data' filesep 'Coding_direction_10ms.mat'])
61:params.Win1 = [-1,0];  % Window 1 for statistical comparison
62:params.Win2 = [.8,1];  % Window 2 for statistical comparison
126:                conext_baseline = mean(current_context(1:100,:),1);
128:                context_concat = [context_concat,nanmean(current_context,2)];
130:                context_concat = [context_concat,nanmean(current_context,2)];
137:        meansig = nanmean(signal2plot,2);
152:        [a,b] = min(abs(windowCenters-params.Win1(1))); W1FirstBin = (b);
153:        [a,b] = min(abs(windowCenters-params.Win1(2))); W1LastBin = (b);
154:        [a,b] = min(abs(windowCenters-params.Win2(1))); W2FirstBin = (b);
155:        [a,b] = min(abs(windowCenters-params.Win2(2))); W2LastBin = (b);
157:        V1 = mean(context_concat(W1FirstBin:W1LastBin,:),1);
158:        V2 = mean(context_concat(W2FirstBin:W2LastBin,:),1);
163:        bar(axs(ind_figures(2,ind_area)),[flg],nanmean(V2),'FaceColor',colorcodes(ind_cond,:));
164:        errorbar(axs(ind_figures(2,ind_area)),[flg],[nanmean(V2)],[nanstd(V2,0)]/sqrt(length(V2)),'-k','CapSize',3,'Linewidth',1,'MarkerSize',4);
170:        P(ind_area,flg) = P_value(mean_values{ind_area}(:,1),mean_values{ind_area}(:,flg));
176:    P_Corr=P*3;
=== Main_figures_codes/Ghaderi2025_Figure6_c_temporalCorrelation.m
48:load([directory filesep 'processed_data' filesep 'Temporal_corrrelation_10ms.mat'])
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 60,135p Main_figures_codes/Ghaderi2025_Figure6_b_CD_context.m | grep -v "^\s*$"; echo ====; sed -n 55,130p Main_figures_codes/Ghaderi2025_Figure6_c_temporalCorrelation.m | grep -v "^\s*$"
```

```
params.arealist = {'A1','wS1','wS2','wM2','ALM'};  % Brain regions
params.Win1 = [-1,0];  % Window 1 for statistical comparison
params.Win2 = [.8,1];  % Window 2 for statistical comparison
colorcodes = [[0 0 1]; % GoTone+W Hit
    [1 0 0]; % NogoTone+W CR
    [0 0.7 0.7]; % GoTone CR
    [0.5 0 0.8]]; % GoTone+W Miss
params.trialtypes = {'Ind=[ trial==1 & lick==1]';'Ind=[ trial==3 & lick==0]';'Ind=[ trial==2 & lick==0]';'Ind=[ trial==1 & lick==0]'};
params.baseline_win = [-1,0];
XTickLabel = {'-1';'0';'1';'2'};
xtick = [-1;0;1;2];
axs = findall(gcf, 'type', 'axes');
axs = flipud(axs);
%% Define baseline subtraction parameter
baselinesubtraction = 0;
%% Define subplot indices
ind_figures = [reshape([1:10]',5,2)]';
%% Process each brain area
for ind_area = 1:length(params.arealist)
    currentarea = cell2mat(params.arealist(ind_area));
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "quiet\|Quiet\|trialtype\|trial ==\|corr(\|min\|< 5\|<= 20\|zscore" processed_data_code/Temporal_corrrelation_10ms.m | grep -v "^\s*[0-9]*:\s*%" | head -30; cat functions/compute_mean_corr.m | grep -v "^\s*$" | head -40
```

```
48:params.trialtype_names = {'gotone_whisker'; 'gotone'; 'nogotone_whisker'; 'nogotone'; 'whisker'; ...
53:params.QuietState = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
95:            switch params.QuietState
96:                case 'Quiet_(whisker_speed)'
97:                    Qind = psth_mat(ind_probes).quiet_trial_whisker_speed;
98:                case 'Quiet_(jaw_movement)'
99:                    Qind = psth_mat(ind_probes).quiet_trial_jaw_movement;
100:                case 'Quiet_(jaw & whisker)'
101:                    Qind = psth_mat(ind_probes).quiet_trial_jaw_movement & psth_mat(ind_probes).quiet_trial_whisker_speed;
102:                case 'Non_quiet'
103:                    Qind = ~(psth_mat(ind_probes).quiet_trial_jaw_movement & psth_mat(ind_probes).quiet_trial_whisker_speed);
212:        correlation_matrix.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = R2_all;
213:        correlation_matrix_shuffled.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = R2_all_shuffled;
216:        angle_matrix.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = angle_all;
219:        pvalue_matrix.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = Pvalue_all;
222:        neuronal_activity.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = mean_activity;
223:        neuronal_activity_shuffled.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = mean_activity_shuffled;
226:        active_cells_percentage.(cell2mat(params.trialtype_names(ind_cond))).(curr_area) = active_cells;
function [lags, mean_correlations, sem_correlations] = compute_mean_corr(mat, start_bin, end_bin, max_lag)
% compute_mean_corr calculates mean correlations and SEM along diagonals
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 45,60p processed_data_code/Temporal_corrrelation_10ms.m; sed -n 104,210p processed_data_code/Temporal_corrrelation_10ms.m | grep -v "^\s*%" | grep -v "^\s*$"
```

```
params.LickState = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1];

% Trial type names based on combination of trial types and lick states
params.trialtype_names = {'gotone_whisker'; 'gotone'; 'nogotone_whisker'; 'nogotone'; 'whisker'; ...
                          'gotone_whisker_lick'; 'gotone_lick'; 'nogotone_whisker_lick'; 'nogotone_lick'; 'whisker_lick'};

% Analysis parameters
params.completion_state = 'completed_trials';
params.QuietState = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.CellType = 'All';  % Options: 'RS', 'FS', 'FS_RS', 'All'

% Time parameters
trial_time = psth_mat(1).trial_timestamps;
bin_width = 1;   % Window length (number of bins to concatenate)

%% Main analysis loop across trial conditions and brain regions
                case 'All_trials'
                    Qind = ones(length(trial), 1);
            end
            ind_trials = trial & lick & Qind & completed_trials_ind;
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in Main_figures_codes/Ghaderi2025_Figure7_b_DeltaFR.m Main_figures_codes/Ghaderi2025_Figure7_c_StimCD.m Main_figures_codes/Ghaderi2025_Figure7_d_ContextDecoding_WS.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -n "Win\|signrank\|ranksum\|P_value\|mafdr\|bonf\|trial==\|trial ==\|Quiet\|baseline\|load(\|bins\|t_start\|t_end\|0\.05\|ttest\|kruskal\|multcompare" | head -40; done
```

```
=== Main_figures_codes/Ghaderi2025_Figure7_b_DeltaFR.m
19:load([directory filesep 'processed_data' filesep 'psth_5ms.mat'])
20:load([directory filesep 'data_helpers' filesep 'Area_list.mat'])
29:WindowCenters = [-1+0.005:0.005:2]';
30:params.QuietState = 'Quiet_(jaw & whisker)'; % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
74:            switch params.QuietState
75:                case 'Quiet_(whisker_speed)'
77:                case 'Quiet_(jaw_movement)'
79:                case 'Quiet_(jaw & whisker)'
106:            [a,b] = min(abs(WindowCenters-t1)); baselineFirstBin = (b);
107:            [a,b] = min(abs(WindowCenters-t2)); baselineLastBin = (b);
109:            baseline_mean = repmat(mean(curr_sp_trials_cells(baselineFirstBin:baselineLastBin,:),1),size(curr_sp_trials_cells,1),1);
112:                curr_sp_trials_cells = curr_sp_trials_cells - baseline_mean;
120:        time2plot = WindowCenters;
135:        P(ind_area,ind_bin) = signrank(current_diff_sp(ind_bin,:));
140:pvalues_area_corrected = mafdr(pvalues(:), 'BHFDR', 'True');
142:pvalues_corrected((0.05 <= pvalues_corrected)) = nan;
144:h_map = heatmap(pvalues_corrected,'YLabel','Areas','XLabel','Time','XDisplayLabels',WindowCenters(391:420),'YDisplayLabels',params.regionlist);
164:xLabels = WindowCenters(391:420);
236:legend_just_txt(axs(1),params.regionlist,'Xoffset',1.1,'Yoffset',2,'relX',0,'relY',0.05,'type','line');
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && f=Main_figures_codes/Ghaderi2025_Figure7_b_DeltaFR.m; grep -v "^\s*%" $f | sed -n '25,145p' | grep -v "^\s*$" | grep -v "case 'Quiet\|case 'Non\|case 'All\|case 'RS\|case 'FS\|CelltypeInd = \|Qind = "; echo; f=Main_figures_codes/Ghaderi2025_Figure7_d_ContextDecoding_WS.m; grep -v "^\s*%" $f | sed -n '20,150p' | grep -v "^\s*$" | grep -iv "plot\|color\|axs\|xlabel\|ylabel\|legend\|fill"
```

```
h = tight_subplot(1,1,[0.1 .1],[.2 .1],[0.08 0.08]);
axs = findall(gcf, 'type', 'axes');
axs = flipud(axs);
WindowCenters = [-1+0.005:0.005:2]';
params.QuietState = 'Quiet_(jaw & whisker)'; % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
params.BaselineSubtraction = 1;
params.completion_state = 'completed_trials';
params.TrialType = [1,3];
params.LickState = [1,0];
params.TrialType_name = {'Go-tone context';'Nogo-tone context'};
params.CellType = 'All';
params.regionlist = {'A1','wS1','wS2','wM2','ALM'};
bin_width = 0.005;
XTickLabel = {'0.95';'1';'1.05';'1.1'};
xtick = [0.95;1;1.05;1.1];
t_show = [0.95,1.1];
params.colormap = {'#0008FF';'#228B22';'#00C3FF';'#FF0000';'#FF7F00';'#000000';'#00C3FF';'#FF7F00';'#FF7F00';'#808080';'#6B3686';'#74B99A';'#A020F0';'#FFD700'};
params.colortype = {'wS1';'wS2';'CR2';'ALM';'CR4';'wM2';'FA2';'FA3';'FA4';'FA5';'Lick';'NoLick';'A1';'tjM1'};
params.Map = horzcat(params.colortype,params.colormap);
diff_sp = struct();
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && f=processed_data_code/Decoding_afterwhisker_runX.m; grep -v "^\s*%" $f | grep -n "psth_\|load(\|baseline\|Baseline\|rng\|quiet\|Class\|svmtrain\|cvpartition\|NbNeurons\|randperm\|< 5\|zscore\|t1\|t2\|Win" | head -40
```

```
9:load([directory filesep 'data_helpers' filesep 'area_list.mat'])
10:load([directory filesep 'processed_data' filesep 'psth_5ms.mat'])
14:    clearvars -except psth_mat run area_list
16:    rng(run)
18:    params.quietstate = 'Quiet_(jaw & whisker)';   % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
19:    params.BaselineSubtraction = 1;  % 1: subtract baseline, 0: no baseline subtraction
40:    params.zscoring = 1;  % Do zscore on feature matrix
45:    baselinelist = [0.955:0.005:1];  % Baseline time windows for subtraction
46:    class_expr1 = 'Ind.Class1 = [trial == 1 & lick == 1];';   % Go-tone with whisker and lick
47:    class_expr2 = 'Ind.Class2 = [trial == 3 & lick == 0];';   % No-go-tone with whisker, no lick
51:        list_probes = find(strcmp(currentarea, [psth_mat.probe_location]));
57:            trial = psth_mat(ind_probe).trial_type;
58:            lick = psth_mat(ind_probe).lick_flag;
62:                    completed_trials_ind = ~psth_mat(ind_probe).early_lick;
64:                    early_licks_all = psth_mat(ind_probe).early_lick;
65:                    lick_time = 0 < (psth_mat(ind_probe).lick_time - psth_mat(ind_probe).start_time);
69:            switch params.quietstate
71:                    Qind = psth_mat(ind_probe).quiet_trial_whisker_speed;
73:                    Qind = psth_mat(ind_probe).quiet_trial_jaw_movement;
75:                    Qind = psth_mat(ind_probe).quiet_trial_jaw_movement & psth_mat(ind_probe).quiet_trial_whisker_speed;
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && f=processed_data_code/Decoding_afterwhisker_runX.m; grep -v "^\s*%" $f | sed -n '104,140p;185,240p' | grep -v "^\s*$" | grep -v -i "smote\|dataset\|tabulate\|Labels\|labelCounts\|table2array\|Xc =\|yc ="
```

```
end
            for ibase = 1:length(baselinelist)
                Currsig = psth_mat(ind_probe).spike_counts;
                Currsig_CurrCellInd = Currsig(:, :, CurrCellInd);
                normalized_data = [];
                if params.BaselineSubtraction
                    t1 = baselinelist(ibase);
                    t2 = baselinelist(ibase);
                    [a, b] = min(abs(params.windowCenters - t1)); baselineFirstBin = (b);
                    [a, b] = min(abs(params.windowCenters - t2)); baselineLastBin = (b);
                    for neuron = 1:size(Currsig_CurrCellInd, 3)
                        neuron_data = Currsig_CurrCellInd(:, :, neuron);
                        sub_data = neuron_data(baselineFirstBin:baselineLastBin, :);  % size: (end_bin-start_bin+1) x 18
                        baseline_mean = mean(sub_data, 1);  % scalar value
                        normalized_data(:, :, neuron) = neuron_data - repmat(baseline_mean, 600, 1);
                    end
                    Currsig_CurrCellInd = normalized_data;
                end
                Currsig_CurrCellInd = Currsig_CurrCellInd(391:420, :, :);
                classnames = fieldnames(Ind);
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && f=Main_figures_codes/Ghaderi2025_Figure8_b_SpontLick_CD_LickvsNolick.m; grep -v "^\s*%" $f | grep -n "Win\|kruskal\|multcompare\|trial==\|trial ==\|Quiet\|baseline\|load(\|signrank\|ranksum\|P_value\|lick==\|ind_\w* = \[" | head -40; f=processed_data_code/Coding_direction_SpontLick.m; grep -v "^\s*%" $f | grep -n "Win_\|0\.5\|bout\|Lick_times\|lick_onset\|pre\|post\|HoldOut\|gram" | head -40
```

```
20:load([directory filesep 'processed_data' filesep 'Coding_direction_SpontLick.mat'])
21:load([directory filesep 'data_helpers' filesep 'Area_list.mat'])
32:params.Win1 = [-1,0];  % Window 1 for statistical comparison
33:params.Win2 = [1.03,1.03];  % Window 2 for statistical comparison
34:params.Win3 = [1.2,1.4];  % Window 3 for statistical comparison
42:params.trialtypes = {'Ind=[ trial==1 & lick==1];';'Ind=[ trial==3 & lick==1];';'Ind=[ trial==5 & lick==1];';'Ind=[ trial==1 & lick==0];';'Ind=[ trial==3 & lick==0];';'Ind=[ trial==5 & lick==0];'};
44:params.baseline_win = [-1,0];
67:                Quietind = coding_direction_matrix.(currentarea)(ind_session).index.Quiet;
71:                trial_indecis = Ind & Quietind & Completed;
84:ind_figuers = [reshape([1:10]',5,2)]';
114:                Quietind = coding_direction_matrix.(currentarea)(ind_session).index.Quiet;
118:                trial_indecis = Ind & Quietind & Completed;
148:        [a,b] = min(abs(windowCenters-params.Win1(1))); W1FirstBin = (b);
149:        [a,b] = min(abs(windowCenters-params.Win1(2))); W1LastBin = (b);
151:        [a,b] = min(abs(windowCenters-params.Win2(1))); W2FirstBin = (b);
152:        [a,b] = min(abs(windowCenters-params.Win2(2))); W2LastBin = (b);
154:        [a,b] = min(abs(windowCenters-params.Win3(1))); W3FirstBin = (b);
155:        [a,b] = min(abs(windowCenters-params.Win3(2))); W3LastBin = (b);
175:    [P_KWT,~,stats2] = kruskalwallis(V2_values(:,1),V2_values(:,2),'off');
176:    [c2,m,h,gnames] = multcompare(stats2,'Display','off','CriticalValueType','lsd');
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && f=processed_data_code/Coding_direction_SpontLick.m; grep -v "^\s*%" $f | sed -n '150,300p' | grep -v "^\s*$"; grep -v "^\s*%" Main_figures_codes/Ghaderi2025_Figure8_b_SpontLick_CD_LickvsNolick.m | sed -n '156,200p'
```

```
lick_mask = lick_times(i_prob).lick_mask;
        video_timestamps = lick_times(i_prob).video_timestamp_continues;
        spontaneous_licks = [];
        n_outside_trials = 0;
        n_filtered_by_duration = 0;
        n_filtered_by_quality = 0;
        jaw_continuous = lick_times(i_prob).jaw_movement_continues;
        time_continuous_jaw = lick_times(i_prob).video_timestamp_continues;
        for ilick = 1:length(lick_times_all)
            lick_t = lick_times_all(ilick);
            in_any_trial = false;
            for itrial = 1:length(start_times)
                if lick_t >= start_times(itrial) && lick_t <= (start_times(itrial) + 6)
                    in_any_trial = true;
                    break;
                end
            end
            if ~in_any_trial
                n_outside_trials = n_outside_trials + 1;
                lick_passes_duration_filter = false;
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "BinSize\|lick_quality_ratio\|windowCenters =\|psth_\w*.mat\|lick_times_all =\|start_times =" processed_data_code/Coding_direction_SpontLick.m | head; grep -n "trialtypes\|Win\|kruskal\|multcompare\|BinSize" Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m Main_figures_codes/Ghaderi2025_Figure8_a_CD_LickvsNolick.m | head -20
```

```
18:%   - psth_10ms.mat (contains trial data with 10ms bins)
33:load([directory filesep 'processed_data' filesep 'psth_5ms.mat'])
56:params.BinSize = 0.005;
58:params.windowCenters = [-1 + params.BinSize:params.BinSize:2];
70:params.lick_quality_ratio = 3;  % After/Before ratio threshold (mean_after should be > 1.2 * mean_before)
199:        lick_times_all = lick_times(i_prob).lick_time;
200:        start_times = psth_mat(i_prob).start_time(:);
280:                    if mean_after > params.lick_quality_ratio * mean_before
362:                [SpikeRates, ~, SpikeCounts] = PSTH_Simple(SpikeTimes, lick_t, PreTime, PostTime, params.BinSize, params.BinStep);
372:                [SpikeRates, ~, SpikeCounts] = PSTH_Simple(SpikeTimes, lick_t, PreTime, PostTime, params.BinSize, params.BinStep);
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:65:params.Win1 = [-1,0];  % Window 1 for statistical comparison
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:66:params.Win2 = [1.03,1.03];  % Window 2 for statistical comparison
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:79:params.trialtypes = {'Ind=[ trial==1 & lick==1]';'Ind=[ trial==3 & lick==1]';'Ind=[ trial==5 & lick==1]';'Ind=[ trial==1 & lick==0]';'Ind=[ trial==3 & lick==0]';'Ind=[ trial==5 & lick==0]'};
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:92:    session2drop.(currentarea) = zeros(size(coding_direction_matrix.(currentarea),2),length(params.trialtypes));
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:94:    for ind_cond = 1:length(params.trialtypes)
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:96:        current_cond_name = cell2mat(params.trialtypes(ind_cond));
Supplementary_figures_codes/Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m:141:    for ind_cond = 1:length(params.trialtypes)
Supplementary_figures_codes/Ghaderi
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" processed_data_code/pc_projections.m | grep -n "Quiet\|trial ==\|TrialType\|LickState\|pca(\|explained\|movsum\|0\.05\|bin\|normaliz\|min\|max" | head -30; grep -n "explained\|pca(" Main_figures_codes/Ghaderi2025_Figure6_a_pca.m | head
```

```
14:params.QuietState = 'Quiet_(jaw & whisker)'; %All_trials  Quiet_(jaw & whisker)
16:params.TrialType = [1,3];  % 1: gotone/whisker (Hit trials)
17:params.LickState = [1,0];  % 1: lick
21:min_trials_per_session = 5;  % Minimum trials needed per session
25:    pca_endbin = 600;       % PCA calculation end bin (30 bins × 100ms = 3 seconds
28:    pca_endbin = 300;       % PCA calculation end bin (30 bins × 100ms = 3 seconds)
45:        for icond = 1:length(params.TrialType)
47:            IndTrialType = Trial == params.TrialType(icond);
48:            IndLickstate = Lick == params.LickState(icond);
58:            switch params.QuietState
59:                case 'Quiet_(whisker_speed)'
61:                case 'Quiet_(jaw_movement)'
63:                case 'Quiet_(jaw & whisker)'
71:            CurrTrialInd = [Qind & completion_state & IndLickstate & IndTrialType];
104:                [~,b] = min(abs(WindowCenters-t1)); baselineFirstBin = b;
105:                [~,b] = min(abs(WindowCenters-t2)); baselineLastBin = b;
117:        n_timebins = size(concat_all_trials_data, 2);
130:        [coeff_neuron, ~, ~, ~, explained_neuron, mu_neuron] = pca(data_for_neuron_pca);
132:        fprintf('    -> Neuron-space PCA: PC1: %.1f%%, PC2: %.1f%%\n', explained_neuron(1), explained_neuron(2));
136:            trial_data = concat_all_trials_data(:, :, itrial)';  % timebins × neurons
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" Main_figures_codes/Ghaderi2025_Figure6_a_pca.m | sed -n '15,140p' | grep -v "^\s*$" | grep -iv "plot\|color\|axs\|xlabel\|ylabel\|legend\|fill\|title\|scatter\|xlim\|ylim"
```

```
newname = 'Figure6A_pca';
fullname = mfilename('fullpath');
inds = regexp(fullname,'\','all');
name = fullname(inds(end)+1:end);
if change_name
    movefile([name '.m'],[newname '.m']);
end
parent = figure('Position', [100 100 1400 400]);
params.QuietState = 'Quiet_(jaw & whisker)';  % 'Quiet_(whisker_speed)' 'Quiet_(jaw_movement)' 'Quiet_(jaw & whisker)' 'Non_quiet' 'All_trials'
params.normalization = 1;
params.completion_state = 'completed_trials';  % Options: 'early_licks' 'completed_trials'
params.TrialType = [1,3,2,1];  % 1: gotone/whisker  2: gotone/nowhisker 3: nogotone/whisker  4: nogotone/nowhisker  5: notone/whisker
params.LickState = [1,0,0,0];  % lick 1: lick  0:nolick
params.CellType = 'All';  % 'R' 'FS' 'RS_FS' 'All'
regionlist = {'A1','wS1','wS2','wM2','ALM'};  % Brain regions
t_start = -1;  % Start time
t_end = 2;     % End time
bin_width = 0.01;
XTickLabel = {'-1';'0';'1';'2'};
xtick = [-1;0;1;2];
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" Main_figures_codes/Ghaderi2025_Figure6_a_pca.m | sed -n '140,245p' | grep -v "^\s*$" | grep -iv "plot\|color\|axs\|xlabel\|ylabel\|legend\|fill\|title\|scatter\|xlim\|ylim"
```

```
t1 = -1;
            t2 = 0;
            [a,b] = min(abs(WindowCenters-t1)); baselineFirstBin = (b);
            [a,b] = min(abs(WindowCenters-t2)); baselineLastBin = (b);
            baseline_mean = repmat(mean(CurrSp_CurrTrialInd_CurrCellInd(baselineFirstBin:baselineLastBin,:),1),size(CurrSp_CurrTrialInd_CurrCellInd,1),1);
            CurrSp_CurrTrialInd_CurrCellInd = (CurrSp_CurrTrialInd_CurrCellInd - baseline_mean);
            Concatsig = [Concatsig,CurrSp_CurrTrialInd_CurrCellInd];
        end % End of probe loop
        Neurons_activity_condition = [Neurons_activity_condition,Concatsig(1:pca_endbin,:)'];
        trial_type_size = size(Concatsig(1:pca_endbin,:),1);
    end % End of condition loop
    Neurons_activity_condition_area = [Neurons_activity_condition];
    if params.normalization
        max_mat = max(Neurons_activity_condition_area,[],2);
        min_mat = min(Neurons_activity_condition_area,[],2);
        Min_Max_Diff=max_mat-min_mat;
        Unit_Ind=~isnan(Min_Max_Diff./Min_Max_Diff);
        Neurons_activity_condition_area=Neurons_activity_condition_area(Unit_Ind,:);
        max_mat = max(Neurons_activity_condition_area,[],2);
        min_mat = min(Neurons_activity_condition_area,[],2);        
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && python3 -c "
import json
nb=json.load(open('processed_data_code/Data_Clustering.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    src=''.join(c['source'])
    print(src[:2500]); print('-----')
" | grep -v "^\s*$" | grep -iv "plt\.\|ax\.\|color\|print(" | head -150
```

```
# Import required libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat
from scipy.stats import ttest_1samp
from scipy.spatial.distance import pdist, squareform
from scipy.linalg import eigh
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.metrics import pairwise_distances
import joblib
import os
from scipy.spatial.distance import pdist, squareform as scipy_squareform
from scipy.linalg import eigh
from sklearn.decomposition import PCA
from scipy.stats import ttest_1samp
# Set matplotlib backend and parameters for publication-quality figures
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && diff <(grep -v "^\s*%" processed_data_code/Neuronal_data_10ms.m) <(grep -v "^\s*%" processed_data_code/Neuronal_data_100ms.m) | head -30; python3 -c "
import json
nb=json.load(open('processed_data_code/Data_Clustering.ipynb'))
for c in nb['cells']:
  src=''.join(c['source'])
  if 'def A6_GMM' in src or 'def A4_spectral' in src: print(src[:4000])
" | grep -iv "plt\.\|ax\.\|print(" | grep -v "^\s*$" | head -120
```

```
2a3
> 
16,17c17
< params.normalization = 0;                     % Enable normalization (0: disabled, 1: enabled)
< baselinesubtraction=1
---
> params.normalization = 1;                     % Enable normalization (0: disabled, 1: enabled)
34a35,36
> params.movement_baselineSubtraction = 1;  % Enable baseline subtraction for movement signals
> params.movement_normalization = 0;       % Disable normalization for movement signals
41c43
< resolution_change = 0;  % Enable temporal smoothing to 100ms resolution
---
> resolution_change = 1;  % Enable temporal smoothing to 100ms resolution
156c158,159
<             end 
---
>             end
>             
157a161,164
[... 85 more lines not kept]
```

**Agent**

I have the code details for all main figures. Two more checks (Fig. 5a single-neuron ROC and Supp. Fig. 18), then I'll write the file.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" Main_figures_codes/Ghaderi2025_Figure5_a_SingleNeuron.m | grep -n "load(\|windows\|bins\|TrialType\|LickState\|Quiet\|0\.05\|selectivity\|perm\|Roc\|roc_mat" | head -20; grep -v "^\s*%" processed_data_code/Roc_hit_cr3.m | grep -n "windows\|bins\|TrialType\|LickState\|QuietState\|selectivity\|label" | head; grep -v "^\s*%" Supplementary_figures_codes/Ghaderi2025_Sup_Figure18_SpontLick_CD_LickvsNolick_200mswindow.m | grep -n "Win\|kruskal\|cohen\|effect\|ranksum\|signrank\|trialtypes" | head
```

```
18:load([directory filesep 'processed_data' filesep 'psth_10ms.mat'])
19:load([directory filesep 'processed_data' filesep 'Roc_hit_cr3.mat'])
20:load([directory filesep 'data_helpers' filesep 'Area_list.mat'])
28:params.QuietState = 'Quiet_(jaw & whisker)';  % Options: 'Quiet_(whisker_speed)', 'Quiet_(jaw_movement)', 'Quiet_(jaw & whisker)', 'Non_quiet', 'All_trials'
31:params.TrialType = [1,3];  % 1: gotone/whisker, 3: nogotone/whisker
32:params.LickState = [1,0];  % 1: lick, 0: nolick
64:for ind_cond = 1:length(params.TrialType)
75:            IndTrialType = Trial == params.TrialType(ind_cond);
76:            IndLickstate = Lick == params.LickState(ind_cond);
87:            switch params.QuietState
88:                case 'Quiet_(whisker_speed)'
90:                case 'Quiet_(jaw_movement)'
92:                case 'Quiet_(jaw & whisker)'
100:            current_trial_ind = [Qind & completion_state & IndLickstate & IndTrialType];
222:        current_roc_diff = roc_mat(ind_probe).diff_fr;
223:        current_discrimination_index = roc_mat(ind_probe).discrimination_index;
224:        curent_pvalue = roc_mat(ind_probe).pvalue;
239:    ind_pos = [(0 < concat_discrimination_index) & (concat_pval < 0.05)];
240:    ind_neg = [(concat_discrimination_index < 0) & (concat_pval < 0.05)];
241:    ind_nan = [0.05 <= concat_pval];
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; ls claims/001535/; head -60 claims/001535/*.yaml
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

[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,200p claims/001535/*.yaml; python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:5000])"
```

```
#     (reach and rotate, wall task) with a fixed biLSTM decoder over up to 210 PnP days, then a
#     recalibration.
#   - The biLSTM was trained on all collected open-loop and closed-loop data from the hDoF
#     experiments, about 14 h 48 min before augmentation and segmentation, as segments of
#     low-frequency (below 25 Hz) and high-gamma activity on all 128 channels of B1.
#
# The dandiset's own description (title and description on the archive only; its files were not
# opened): long-term ECoG training trials from the 128-channel grid of one tetraplegic participant
# trying to access 7 directional targets (6 axial directions and the origin), collated from
# several BCI contexts (virtual environment, physical robot, open and closed loop), with high-gamma
# amplitude (70 to 150 Hz) and low-frequency motor potentials (below 25 Hz) down-sampled to 100 Hz.
# That is the B1 RNN training set. The Figure 1 task, B3, the 200 ms band-power features (delta,
# beta, high gamma) that the MLP and autoencoder analyses use, the online decoder outputs and the
# robot task outcomes may not be in it; which claims it can test is the author's to establish.
#
# Statements of tolerance. Where the paper gives an interval for a value, the tolerance is the
# larger of the two distances from the value to the bounds of that interval; where it gives a
# spread (plus or minus), the tolerance is that spread; otherwise 10% of the value.
#
# A paper inconsistency to note: Results, Plug-and-play control, paragraph 3 reports the same
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)); print(json.dumps(d['properties']['claims']['items']['properties'].get('where'),indent=1)); print([k for k in d['properties']])"
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
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && python3 -c "
import json
nb=json.load(open('processed_data_code/Data_Clustering.ipynb'))
for c in nb['cells']:
  src=''.join(c['source'])
  if 'def A6_GMM' in src or 'def A4_spectral' in src:
    i=src.find('def A6_GMM'); print(src[i:i+3000] if i>=0 else '')
    j=src.find('def A4_spectral'); print(src[j:j+2500] if j>=0 else '')
" | grep -v "^\s*$" | grep -iv "plt\.\|ax\.\|print(\|\"\"\"" | head -90
```

```
def A6_GMM_grid_search(Spectral_Data, Path, Seed,Run):
    Perform a grid search to find the best Gaussian Mixture Model (GMM) based on BIC.
    Args:
        Spectral_Data (dict): Dictionary with 'spectral_Data' containing the dataset.
        Path (str): Path to save the results.
        Seed (int): Random seed for reproducibility.
    Returns:
        GaussianMixture: The best GMM model based on BIC.
    np.random.seed(Seed)
    X = Spectral_Data['spectral_Data']
    k = list(range(10, 25, 5)) + list(range(25, 45, 1)) + list(range(45, 56, 5))  # Number of components to test
    Sigma = ['diag']  # Covariance types to test   diagonal or full
    SharedCovariance = [False]  # Shared covariance (not directly in sklearn)
    RegularizationValue = 0  # Regularization for GMM
    MaxIter = 1000
    Replicates =1000  # Number of initializations
    nK = len(k)
    nSigma = len(Sigma)
    nSC = len(SharedCovariance)
    # Preallocate results
[... 71 more lines not kept]
```

**Agent**

I have everything needed. Writing the claims file now.

**Agent calls Bash**

```bash
mkdir -p claims/001530; grep -o "Licking was assessed online[^.]*\." paper/*.txt | head -2; grep -o "rejects around half of the recorded trials" paper/*.txt; grep -o "Decoding in the baseline period was at chance level[^.]*\." paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001530/10.1038-s41467-026-73622-y.yaml",
 "content": "# Claims for Ghaderi, Crochet & Petersen (2026), \"Contextual gating of whisker-evoked responses by\n# frontal cortex supports flexible decision making\", Nature Communications 17, 5982, on dandiset\n# 001530.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record as served by Europe PMC (PMC13346651), corrected publication\n# (a correction, doi:10.1038/s41467-026-75986-7, is noted in the text; its content was not\n# supplied): main text, figure legends, Methods, Data and Code availability\n# (paper/10.1038-s41467-026-73622-y.txt). No PDF was supplied. The Supplementary Information\n# (Supplementary Figures 1 to 19), the Reporting Summary, the peer review file and the Source Data\n# file were not in the text and were not read. Every claim below rests on a sentence of the main\n# text or a main figure legend; where the main text cites a supplementary figure for a finding\n# (Supplementary Figs. 3, 17, 18), the claim is written from the main-text sentence and its\n# method from the code that draws that supplementary figure.\n#\n# Code read: the paper's Zenodo record doi:10.5281/zenodo.17973874 (one archive,\n# 2026_Ghaderi_NCOMMS_Zenodo_data_code.zip, 21212076245 bytes, holding the data, the processed\n# data and the code). Only its code files were read (README.txt, processed_data_code/,\n# Main_figures_codes/, Supplementary_figures_codes/, functions/*.m), by range requests; no data\n# file was opened. The same code is on GitHub at LSENS-BMI-EPFL/Ghaderi_et_al_NCOMMS_2026, commit\n# 20cf10c7b95069c12f762b7dd89817beedcc382f (2026-06-05); its processed_data_code and\n# Main_figures_codes files are byte-identical to the Zenodo copies. The code is MATLAB (libsvm,\n# matnwb, subspaceID of Hasnain et al., manopt) and two Python notebooks (clustering, layer\n# analysis). It reads the 35 ephys NWB files (data_electrophysiology/*-processed-behavior.nwb),\n# the 91 optogenetics NWB files (data_optogenetics/*-opto-behavior.nwb) and three helper files\n# (data_helpers/Area_list.mat, the Allen CCF acronyms that make up each of the five areas;\n# Area_Top_Coordinates.mat; Lick_times.mat, spontaneous lick times, a lick mask and the continuous\n# jaw trace per session). Criteria cite it as \"code, <file>\".\n#\n# Conventions the code fixes for every claim unless the claim says otherwise (code,\n# psth_10ms.m, psth_5ms.m, nwb_findQuietTrial.m, trial_typeMaker.m):\n#   - Time zero is the trial start (auditory cue onset, or its expected time on No-tone trials);\n#     the whisker stimulus is at 1.0 s. Spike counts are binned from -1 to 2 s in 10 ms (or 5 ms)\n#     bins; a bin labelled t holds spikes in (t - bin, t].\n#   - Trial types 1 to 5 are Go-tone Whisker, Go-tone No-Whisker, Nogo-tone Whisker, Nogo-tone\n#     No-Whisker, No-tone Whisker. Correct trials are Hit (type 1 with lick) and correct\n#     rejections (types 2 to 5 without lick); Miss is type 1 without lick; False Alarm is a lick\n#     in types 2 to 5. Early-lick (aborted) trials are always excluded.\n#   - Quiet trials (Methods, Quantification of orofacial movements): per session and signal, the\n#     mean of the signal over 0.8 to 1.0 s is at or below the median plus one MAD of the per-trial\n#     means over -1 to 0 s, taken over all trials of the session; whisker speed (absolute\n#     frame-to-frame change of C2 whisker angle) and jaw displacement (distance from the modal jaw\n#     position) must both pass. The code calls MATLAB mad() with its default, the mean absolute\n#     deviation, where the Methods say median absolute deviation. Every claim that uses quiet\n#     trials is run under both (a) median absolute deviation (Methods) and (b) mean absolute\n#     deviation (code).\n#   - A neuron belongs to an area when it was recorded on a probe targeted to that area and its\n#     own CCF label is one of the area's CCF acronyms (code, Area_list.mat); sessions with fewer\n#     than 5 such neurons are skipped in population analyses. \"Sessions\" in the paper's n are\n#     area-by-session recordings.\n#\n# Where the Methods and the code disagree (Methods followed, code as variant, unless the claim\n# says why not):\n#   - Optogenetics bootstrap: Methods and Fig. 2 legend say 1,000 iterations; the code uses\n#     10,000 (Ghaderi2025_Figure2_d_Plick_Sessions.m). With 1,000 the smallest attainable p is\n#     0.002 before FDR, so the reported 0.0003 and 0.0004 fit the code's 10,000.\n#   - Clustering: the Methods describe 10 ms PSTHs (1500 bins) and a Gaussian similarity\n#     exp(-d^2/2 sigma^2); the code clusters 100 ms PSTHs (Neuronal_data_100ms.m, 150 bins), uses\n#     exp(-d/sigma) and labels sigma = 0.07975 as its 100 ms value. The reported sigma is the\n#     100 ms one, so the code is what produced the 29 clusters.\n#   - Context coding direction: Methods say it is computed from 20% of trials; the code\n#     (Coding_direction_10ms.m, Coding_direction_5ms.m) trains on 30% (cvpartition HoldOut 0.7,\n#     the held-out 70% projected).\n#   - Decoding: Methods name a grid search of SVM parameters with nested cross-validation and a\n#     baseline of -1 to 0 s; the code trains libsvm nu-SVC (\"-s 1 -t 0\", default nu 0.5) with no\n#     search, z-scores the balanced trial matrix before the 5 folds, and takes the baseline over\n#     -0.8 to 0 s.\n#   - Fig. 6a legend says the PCs are computed on correct Go-tone Whisker and Nogo-tone Whisker\n#     trials and other trials projected; the Methods and the code compute them on all four\n#     conditions (Hit, Nogo CR, Go-tone No-Whisker CR, Miss) concatenated.\n#\n# A paper inconsistency: the Results and Fig. 1c give 35 recording sessions in 14 mice and the\n# Zenodo record holds 35 ephys files; the Methods say \"Across 34 sessions in 14 mice\" and list\n# 12 + 3 + 1 + 16 + 2 = 34 sessions.\n#\n# The data the paper used, as it reports them:\n#   - Mice: VGAT-ChR2 (Slc32a1-COP4*H134R/EYFP) for optogenetics, some reused for recordings, and\n#     C57BL/6 for recordings only; male and female, at least 6 weeks old. Go-tone 4 or 8 kHz\n#     (100 ms) per mouse, delay 1 s, right C2 whisker deflection (5 ms), 1 s response window,\n#     five equiprobable trial types.\n#   - Optogenetics: 470 nm light (100 Hz, 50% duty, 12 to 15 mW) on one area per session (A1 9\n#     mice, wS1 10, wS2 10, wM2 9, ALM 8, fpS1 8), 30% of trials, in one of three windows\n#     (Auditory -0.05 to 0.3 s; Delay 0.4 to 0.85 s; Whisker 0.95 to 1.2 s; each plus a 100 ms\n#     ramp). 91 sessions on Zenodo.\n#   - Electrophysiology: Neuropixels Phase 3A, 2 to 5 probes per session, 35 sessions in 14 mice,\n#     10,294 units after Kilosort 2.0, Bombcell and CCF registration (A1 780, wS1 1938, wS2 2064,\n#     wM2 2749, ALM 2763); RS (> 0.46 ms), FS (< 0.36 ms) and unclassified by spike width; layer\n#     and depth from the Allen CCF.\n#   - Behaviour: piezo lick sensor (2 kHz), 200 Hz video (100 Hz in mouse PG019) with\n#     DeepLabCut tracking of C2 whisker angle, jaw, tongue and snout.\n#\n# The dandiset's own description (title and description on the archive only; its files were not\n# opened): \"Data related to the publication Ghaderi et al., Nature Communications, 2026\", 196\n# assets from 21 subjects, about 2.6 TB, pointing to the same Zenodo record and GitHub repository\n# for processed data and code. Which recordings and variables it holds is the author's to find.\n#\n# Outside data. Claims about named clusters (cluster 1, 4, 11, 25, 29) need the paper's cluster\n# labels, which a new clustering would not number the same way; those labels are on Zenodo\n# (doi:10.5281/zenodo.17973874, processed_data/Data_Clustering.mat, Cluster_Counter_Ordered and\n# Id_Ordered, keyed to the code's global unit index built from the order of probes in\n# psth_10ms.m), so those claims are data with_inputs. The lick coding direction (Fig. 8b,\n# Supplementary Fig. 18) uses spontaneous lick times and the continuous jaw trace from\n# data_helpers/Lick_times.mat on the same record; whether the dandiset holds them is the\n# author's to find.\n#\n# Tolerances. Where the paper gives a spread (plus or minus SEM), the tolerance is that spread;\n# otherwise 10% of the value.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001530\"\npaper: doi:10.1038/s41467-026-73622-y\nclaims:\n- id: fig1c-lick-probabilities\n  statement: Mice lick in the response window on 78 +/- 2% of Go-tone Whisker trials and withhold\n    licking in the other trial types (Go-tone No-Whisker 10 +/- 1%, Nogo-tone Whisker 13 +/- 2%,\n    Nogo-tone No-Whisker 1 +/- 0.3%, No-tone Whisker 15 +/- 2%), mean +/- SEM over 35 recording\n    sessions in 14 mice.\n  source: Results, A short-term memory context-dependent whisker detection task, paragraph 1;\n    Figure 1c\n  quote: 'Mice learned to lick correctly in the reward-predicting trials including the Go-tone and whisker deflection (probability of licking correctly in the reporting window, P(lick) = 78 ± 2%, mean ± standard error of the mean, SEM, n = 35 sessions across N = 14 mice during electrophysiological recordings described later) ... i) Go-tone without whisker deflection, P(lick) = 10 ± 1%; ii) Nogo-tone with whisker deflection, P(lick) = 13 ± 2%; iii) Nogo-tone without whisker deflection, P(lick) = 1 ± 0.3%; and iv) No-tone with whisker deflection, P(lick) = 15 ± 2%'\n  expected:\n  - quantity: P(lick), Go-tone Whisker\n    value: 78\n    tolerance: 2\n    unit: percent\n  - quantity: P(lick), Go-tone No-Whisker\n    value: 10\n    tolerance: 1\n    unit: percent\n  - quantity: P(lick), Nogo-tone Whisker\n    value: 13\n    tolerance: 2\n    unit: percent\n  - quantity: P(lick), Nogo-tone No-Whisker\n    value: 1\n    tolerance: 0.3\n    unit: percent\n  - quantity: P(lick), No-tone Whisker\n    value: 15\n    tolerance: 2\n    unit: percent\n  criterion: As code, Ghaderi2025_Figure1_c_Performance.m. Per recording session and trial type,\n    the fraction of completed (non early-lick) trials with a lick in the response window (the\n    NWB lick flag, first lick within 1 s after the whisker time, Methods Behavioral data\n    analysis), all trials (no quiet selection); mean and SEM over the 35 sessions. Reproduced\n    when all five means are within tolerance; partially reproduced when the Go-tone Whisker mean\n    exceeds every other trial type's by at least 50 points but some value is out of tolerance.\n- id: fig1f-movement-latencies\n  statement: In quiet Hit trials the whisker deflection is followed by whisker protraction (time to\n    20% of maximum 58 +/- 8 ms), jaw opening (115 +/- 17 ms) and tongue protrusion (231 +/- 29\n    ms), and tongue-spout contact at 330 +/- 20 ms.\n  source: Results, A short-term memory context-dependent whisker detection task, paragraph 3;\n    Figure 1f\n  quote: 'In quiet Hit trials, following the whisker deflection in Go-tone trials, mice rapidly initiated a sequence of movements starting with whisker protraction after ~30 ms (time to 20% max = 58 ± 8 ms), followed by jaw opening (115 ± 17 ms) and then protrusion of the tongue (231 ± 29 ms) (Fig. 1f ) resulting in tongue-spout contact triggering water reward delivery with latency 330 ± 20 ms ( n = 35 sessions during electrophysiological recordings)'\n  expected:\n  - quantity: whisker time to 20% of maximum after whisker stimulus\n    value: 58\n    tolerance: 8\n    unit: ms\n  - quantity: jaw time to 20% of maximum\n    value: 115\n    tolerance: 17\n    unit: ms\n  - quantity: tongue time to 20% of maximum\n    value: 231\n    tolerance: 29\n    unit: ms\n  - quantity: first tongue-spout contact latency\n    value: 330\n    tolerance: 20\n    unit: ms\n  criterion: Movement traces as code, Ghaderi2025_Figure1_f_Movements_Hit.m (quiet, completed Hit\n    trials; whisker speed, jaw and tongue displacement in 10 ms bins, each trial minus its mean\n    over 0.8 to 1.0 s, averaged per session). The lick latency as code,\n    Ghaderi2025_Sup_Figure1_b_SpoutReactionTime.m (first lick time minus 1 s, licks outside 1 to\n    2 s dropped, mean per session over completed Hit trials, all trials; mean and SEM over\n    sessions). Open detail, none of the code computes \"time to 20% max\". Readings (a) per session,\n    the first bin after 1.0 s where the session-mean trace reaches 20% of its maximum over 1.0 to\n    1.2 s, then mean and SEM over sessions; (b) the same on each trial, averaged per session.\n    Reproduced when, under a reading, the three movement latencies and the lick latency are within\n    tolerance; partially reproduced when the order whisker, jaw, tongue, spout contact holds but a\n    value is out of tolerance. Since the reading is a measure detail, the outcome is the one both\n    readings give; if they differ, blocked as methods_underspecified.\n- id: quiet-trials-half\n  statement: Selecting quiet trials (no whisker or jaw movement in the last 200 ms of the delay)\n    rejects about half of the recorded trials.\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 5\n  quote: This precludes the involvement of orofacial motor or sensory reafference signals from\n    contributing to our decoding analyses, but rejects around half of the recorded trials\n  expected:\n    quantity: fraction of completed trials that are not quiet, over all sessions\n    value: 50\n    tolerance: 5\n    unit: percent\n  criterion: The quiet rule of the header, under readings (a) and (b) of the MAD. The fraction of\n    completed trials failing it, pooled over the 35 sessions and also as the median over\n    sessions. Reproduced when the pooled fraction is within tolerance under a reading; partially\n    reproduced when it lies between 30% and 70%. The tolerance is 10% of the value.\n- id: fig2-auditory-window\n  statement: Inactivation during the Auditory epoch reduces licking on Go-tone Whisker trials most\n    for A1 (39 +/- 4%), and also for wM2 (33 +/- 6%), wS2 (26 +/- 4%) and wS1 (19 +/- 6%), while\n    ALM and fpS1 inactivation causes no significant decrease.\n  source: Results, Spatiotemporally-specific optogenetic inactivation, paragraph 3; Figure 2b-d\n  quote: 'For Go-tone Whisker trials, the largest impact of inactivation during the Auditory epoch was found for A1 (39 ± 4% reduction in lick probability, p = 0.0004, n = 17 sessions across N = 9 mice), but significant reductions were also found for inactivation of wM2 (33 ± 6% reduction in lick probability, p = 0.0004, n = 14 sessions across N = 9 mice), wS2 (26 ± 4% reduction in lick probability, p = 0.0004, n = 18 sessions across N = 10 mice) and wS1 (19 ± 6% reduction in lick probability, p = 0.002, n = 16 sessions across N = 10 mice). Importantly, inactivation of either ALM or fpS1 during the Auditory window did not cause any significant decrease in licking during the reporting period.'\n  statistics:\n  - about: A1, light against no light\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 17 sessions, 9 mice\n  - about: wM2\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 14 sessions, 9 mice\n  - about: wS2\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 18 sessions, 10 mice\n  - about: wS1\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.002\n    corrected: FDR\n    n: 16 sessions, 10 mice\n  expected:\n  - quantity: reduction in Go-tone Whisker P(lick), A1, Auditory window\n    value: 39\n    tolerance: 4\n    unit: percent\n  - quantity: reduction, wM2, Auditory window\n    value: 33\n    tolerance: 6\n    unit: percent\n  - quantity: reduction, wS2, Auditory window\n    value: 26\n    tolerance: 4\n    unit: percent\n  - quantity: reduction, wS1, Auditory window\n    value: 19\n    tolerance: 6\n    unit: percent\n  criterion: The optogenetic test of code, Ghaderi2025_Figure2_d_Plick_Sessions.m, used by all\n    three window claims. Per session, P(lick) over completed Go-tone Whisker trials with no light\n    and with light in the window. The reduction is the mean over sessions of no-light minus light\n    P(lick), in percentage points. Test (Methods and code), on paired sessions, draw 9 sessions\n    with replacement (9 is the minimum session count over areas and windows), take the\n    difference of means, p = (number of draws on the wrong side of zero + 1) / iterations,\n    two-tailed as 2 min(p, 1 - p); Benjamini-Hochberg FDR over the six areas within each window,\n    significant at 0.05. Iterations 1,000 (Methods) with 10,000 (code) as variant. Open details.\n    (1) The plus-or-minus spread is SEM over sessions (Results, \"Data are presented as mean ±\n    SEM\") or SD (Fig. 2d legend); both are reported, the value is judged on the mean. (2) The\n    reduction may be relative (percent of the no-light P(lick)); readings (a) absolute points,\n    (b) relative percent. Reproduced when under a reading of (2) the four means are within\n    tolerance, the four areas are significant and ALM and fpS1 are not; partially reproduced when\n    the pattern of significance holds and a value is out of tolerance, or when one area's\n    significance differs.\n- id: fig2-delay-window\n  statement: Inactivation during the Delay epoch reduces Go-tone Whisker licking strongly for wM2\n    (45 +/- 7%) and ALM (32 +/- 5%), more modestly for wS1 (16 +/- 3%), and not significantly for\n    A1, wS2 or fpS1.\n  source: Results, Spatiotemporally-specific optogenetic inactivation, paragraph 3; Figure 2b-d\n  quote: 'Inactivation during the Delay epoch of Go-tone Whisker trials caused a significant and large reduction in lick probability during the reporting window for wM2 (45 ± 7% reduction in lick probability, p = 0.0004, n = 14 sessions across N = 9 mice) and ALM (32 ± 5% reduction in lick probability, p = 0.0004, n = 9 sessions across N = 8 mice). Inactivation of wS1 also appeared to significantly, albeit more modestly, reduce licking (16 ± 3% reduction in lick probability, p = 0.0004, n = 16 sessions across N = 10 mice). On the other hand, inactivation of A1, wS2 or fpS1 during the Delay epoch did not significantly change lick probability in the reporting window.'\n  statistics:\n  - about: wM2, light against no light\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 14 sessions, 9 mice\n  - about: ALM\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 9 sessions, 8 mice\n  - about: wS1\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0004\n    corrected: FDR\n    n: 16 sessions, 10 mice\n  expected:\n  - quantity: reduction in Go-tone Whisker P(lick), wM2, Delay window\n    value: 45\n    tolerance: 7\n    unit: percent\n  - quantity: reduction, ALM, Delay window\n    value: 32\n    tolerance: 5\n    unit: percent\n  - quantity: reduction, wS1, Delay window\n    value: 16\n    tolerance: 3\n    unit: percent\n  criterion: As fig2-auditory-window, for the Delay window. Reproduced when under a reading the\n    three means are within tolerance, wM2, ALM and wS1 are significant and A1, wS2 and fpS1 are\n    not; partially reproduced as in fig2-auditory-window.\n- id: fig2-whisker-window\n  statement: Inactivation during the Whisker epoch reduces Go-tone Whisker licking for every area\n    except fpS1, most for ALM (52 +/- 4%) and wM2 (48 +/- 4%), then wS1 (38 +/- 3%), wS2 (35 +/-\n    4%) and A1 (13 +/- 3%).\n  source: Results, Spatiotemporally-specific optogenetic inactivation, paragraph 3; Figure 2b-d\n  quote: 'Finally, all tested cortical regions, except fpS1, showed a significant reduction in licking probability when inactivation occurred during the Whisker stimulus epoch. The largest effects were found for inactivation of ALM (52 ± 4% reduction in lick probability, p = 0.0003, n = 9 sessions across N = 8 mice) and wM2 (48 ± 4% reduction in lick probability, p = 0.0003, n = 14 sessions across N = 9 mice), followed by wS1 (38 ± 3% reduction in lick probability, p = 0.0003, n = 20 sessions across N = 10 mice), wS2 (35 ± 4% reduction in lick probability, p = 0.0003, n = 18 sessions across N = 10 mice), and A1 (13 ± 3% reduction in lick probability, p = 0.01, n = 17 sessions across N = 9 mice).'\n  statistics:\n  - about: ALM, light against no light\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0003\n    corrected: FDR\n    n: 9 sessions, 8 mice\n  - about: wM2\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0003\n    corrected: FDR\n    n: 14 sessions, 9 mice\n  - about: wS1\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0003\n    corrected: FDR\n    n: 20 sessions, 10 mice\n  - about: wS2\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.0003\n    corrected: FDR\n    n: 18 sessions, 10 mice\n  - about: A1\n    test: paired bootstrap resampling, FDR within stimulation window\n    p: 0.01\n    corrected: FDR\n    n: 17 sessions, 9 mice\n  expected:\n  - quantity: reduction in Go-tone Whisker P(lick), ALM, Whisker window\n    value: 52\n    tolerance: 4\n    unit: percent\n  - quantity: reduction, wM2, Whisker window\n    value: 48\n    tolerance: 4\n    unit: percent\n  - quantity: reduction, wS1, Whisker window\n    value: 38\n    tolerance: 3\n    unit: percent\n  - quantity: reduction, wS2, Whisker window\n    value: 35\n    tolerance: 4\n    unit: percent\n  - quantity: reduction, A1, Whisker window\n    value: 13\n    tolerance: 3\n    unit: percent\n  criterion: As fig2-auditory-window, for the Whisker window. Reproduced when under a reading the\n    five means are within tolerance, those five areas are significant and fpS1 is not; partially\n    reproduced as in fig2-auditory-window.\n- id: fig2-wm2-vs-alm-auditory\n  statement: Inactivation during the auditory window reduces licking significantly more for wM2\n    than for ALM (33 +/- 6% against 8 +/- 5%).\n  source: Results, Spatiotemporally-specific optogenetic inactivation, paragraph 3\n  quote: 'The effect of inactivation during the auditory window was significantly stronger for wM2 than ALM (reduction in lick probabilities for wM2 = 33 ± 6 % vs ALM = 8 ± 5 %; bootstrap comparison, FDR-corrected, p = 0.009).'\n  statistics:\n  - test: bootstrap comparison\n    p: 0.009\n    corrected: FDR\n  expected:\n  - quantity: reduction, wM2, Auditory window\n    value: 33\n    tolerance: 6\n    unit: percent\n  - quantity: reduction, ALM, Auditory window\n    value: 8\n    tolerance: 5\n    unit: percent\n  depends_on:\n  - fig2-auditory-window\n  criterion: Reductions as fig2-auditory-window. The code does not hold this comparison and the\n    paper does not describe it beyond \"bootstrap comparison, FDR-corrected\". Readings (a) an\n    unpaired bootstrap of the difference of the two areas' per-session reductions (sessions\n    resampled with replacement within each area, 9 per area as in the Methods' subsampling),\n    two-tailed as in the code's p rule; (b) the same with all sessions of each area resampled.\n    The family for FDR is not given; the uncorrected p is reported with each reading, and FDR over\n    the 15 area pairs of the Auditory window as a variant. Reproduced when both means are within\n    tolerance and both readings give p < 0.05 with wM2 larger; blocked as methods_underspecified\n    if the readings disagree.\n- id: fig2-other-trial-types\n  statement: Inactivation has little impact on licking in the trial types other than Go-tone\n    Whisker.\n  source: Results, Spatiotemporally-specific optogenetic inactivation, paragraph 2\n  quote: whereas inactivation had little impact upon other trial types\n  criterion: The finding is shown in Supplementary Fig. 3, which was not read; its code\n    (Ghaderi2025_Sup_Figure3_a_Heatmaps.m, Sup_Figure3_b_Brainmaps.m) draws per-area, per-window\n    changes in P(lick) for the other four trial types without a test. Measure as\n    fig2-auditory-window for trial types 2 to 5. Reproduced when, over the 6 areas, 3 windows and\n    4 trial types, no change in P(lick) exceeds 13 points (the smallest reduction the paper calls\n    significant on Go-tone Whisker trials, A1 in the Whisker window); partially reproduced when at\n    most 3 of the 72 changes exceed it. The bootstrap test of fig2-auditory-window is reported for\n    each as well.\n- id: units-recorded\n  statement: Across 35 sessions in 14 mice, 10,294 well-isolated units were recorded in the five\n    areas (A1 780, wS1 1938, wS2 2064, wM2 2749, ALM 2763).\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 1\n  quote: 'Altogether, across 35 sessions in 14 mice, we recorded 10,294 well-isolated units located in: i) A1 - 780 units across 14 sessions in 6 mice; ii) wS1 - 1938 units across 24 sessions in 12 mice; iii) wS2 - 2064 units across 24 sessions in 11 mice; iv) wM2 - 2749 units across 18 sessions in 8 mice; and v) ALM - 2763 units across 16 sessions in 6 mice.'\n  expected:\n  - quantity: units, all five areas\n    value: 10294\n    tolerance: 1029\n  - quantity: units, A1\n    value: 780\n    tolerance: 78\n  - quantity: units, wS1\n    value: 1938\n    tolerance: 194\n  - quantity: units, wS2\n    value: 2064\n    tolerance: 206\n  - quantity: units, wM2\n    value: 2749\n    tolerance: 275\n  - quantity: units, ALM\n    value: 2763\n    tolerance: 276\n  criterion: Units the dataset marks as included (Bombcell single somatic units, well isolated),\n    assigned to areas as in the header (probe target area and CCF label in the area's acronyms).\n    The session and mouse counts per area (A1 14 and 6, wS1 24 and 12, wS2 24 and 11, wM2 18 and\n    8, ALM 16 and 6) are reported against the paper. Reproduced when all six unit counts are\n    within tolerance; a count that matches only without the CCF filter is reported as such.\n- id: fig3b-delay-and-response-psth\n  statement: In grand-average PSTHs of correct quiet trials, firing in wM2 and ALM is elevated\n    during the delay of Go-tone trials compared with Nogo-tone trials, and after the whisker\n    stimulus activity rises in Go-tone Whisker Hit trials compared with all other trial types in\n    wS1, wS2, wM2 and ALM.\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 3; Figure 3b\n  quote: 'there were two obvious differences comparing Go-tone and Nogo-tone trials: i) there was a prominent elevation in firing rate in wM2 and ALM during the delay period of Go-tone trials compared to Nogo-tone trials; and ii) after the whisker stimulus there was a clear increase of activity in correct Go-tone Whisker trials compared to all other trial types in wS1, wS2, wM2 and ALM'\n  criterion: PSTHs as code, Ghaderi2025_Figure3_b_PSTH_brainareas.m and Neuronal_data_10ms.m,\n    per neuron, the mean over quiet, correct trials of each type, baseline (-1 to 0 s)\n    subtracted. The figure carries no test, so the test is fixed from the paper's Statistics\n    section (paired comparisons by Wilcoxon signed-rank over neurons). (i) For wM2 and ALM, the\n    per-neuron mean over 0.8 to 1.0 s, Go-tone (types 1 and 2 pooled, and type 1 alone) against\n    Nogo-tone (types 3 and 4 pooled, and type 3 alone); (ii) for wS1, wS2, wM2 and ALM, the mean\n    over 1.0 to 1.5 s, Hit against each of the four other correct trial types. Reproduced when\n    every comparison of (i) and (ii) is higher in the Go-tone (or Hit) condition with p < 0.05;\n    partially reproduced when (i) holds and (ii) fails for one area. The quiet rule follows the\n    code of each figure (whisker speed only in Neuronal_data_10ms.m) as a variant.\n- id: fig3c-delay-modulation-wm2-alm\n  statement: In the last 200 ms of the delay of quiet Hit trials, more wM2 than ALM neurons are\n    up-modulated relative to baseline (16.0% against 14.2%, p = 0.0499) and fewer are\n    down-modulated (14.3% against 17.0%, p = 0.0062), by chi-squared tests.\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 4; Figure 3c\n  quote: 'The fraction of up-modulated neurons was slightly but significantly higher in wM2 (16.0%) than in ALM (14.2%) ( p = 0.0499, chi-squared test), whereas the fraction of down-modulated neurons was significantly lower in wM2 (14.3 %) compared to ALM (17.0 %) ( p = 0.0062, chi-squared test).'\n  statistics:\n  - about: up-modulated fraction, wM2 against ALM\n    test: chi-squared test\n    p: 0.0499\n    n: all wM2 and ALM neurons\n  - about: down-modulated fraction, wM2 against ALM\n    test: chi-squared test\n    p: 0.0062\n  expected:\n  - quantity: up-modulated fraction, wM2\n    value: 16.0\n    tolerance: 1.6\n    unit: percent\n  - quantity: up-modulated fraction, ALM\n    value: 14.2\n    tolerance: 1.42\n    unit: percent\n  - quantity: down-modulated fraction, wM2\n    value: 14.3\n    tolerance: 1.43\n    unit: percent\n  - quantity: down-modulated fraction, ALM\n    value: 17.0\n    tolerance: 1.7\n    unit: percent\n  criterion: As code, Modulation.m and Ghaderi2025_Figure3_c_roc_hit.m. Per neuron, over quiet\n    completed Hit trials, the spike count in 0.8 to 1.0 s against the count in -0.2 to 0 s of\n    the same trials (two samples, labels window and baseline), AUC by perfcurve, selectivity\n    index 2(AUC - 0.5); p is the fraction of 200 label permutations with |SI| at least the\n    observed; up-modulated when SI > 0 and p < 0.05, down-modulated when SI < 0 and p < 0.05.\n    Fractions over all neurons of the area; 2 x 2 Pearson chi-squared without continuity\n    correction (MATLAB crosstab) for up against not-up and down against not-down. Reproduced\n    when the four fractions are within tolerance and both tests give p < 0.05 in the stated\n    directions; partially reproduced when both directions hold but a test or a value fails (the\n    up-modulation p is near 0.05, so the result of each permutation seed is reported).\n- id: fig3d-wm2-infragranular-delay\n  statement: During the late delay of Go-tone Whisker trials, wM2 infragranular neurons change\n    their firing more than supragranular neurons (1.2 +/- 0.1 Hz against 0.03 +/- 0.10 Hz, p = 1.7 x\n    10^-7, two-sample t-test), while no layer difference is detected in A1, wS2 or ALM.\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 5; Figure 3d\n  quote: 'Statistical tests indicated that neuronal activity during the late delay period of Go-tone trials differed significantly across cortical layers in wM2, with infragranular neurons having larger changes in firing rates than supragranular neurons (1.2 ± 0.1 Hz vs 0.03 ± 0.10 Hz; two-sample t-test, p = 1.7 × 10⁻⁷), whereas no significant differences were detected in A1, wS2, or ALM.'\n  statistics:\n  - about: wM2 infragranular against supragranular\n    test: two-sample t-test\n    p: 1.7e-7\n  expected:\n  - quantity: change in firing, wM2 infragranular, late delay\n    value: 1.2\n    tolerance: 0.1\n    unit: Hz\n  - quantity: change in firing, wM2 supragranular, late delay\n    value: 0.03\n    tolerance: 0.1\n    unit: Hz\n  criterion: As code, Neuronal_data_10ms.m, Ghaderi2025_Figure3_d_PSTH_depth.ipynb and\n    compute_layer_stats_pg.m. Per neuron, the mean 10 ms PSTH over quiet completed Hit trials\n    (the code's quiet rule here is whisker speed only; jaw and whisker is a variant), minus its\n    mean over -1 to 0 s, averaged over 0.8 to 1.0 s, in Hz. Layers from the CCF label, layer 1\n    and 2/3 supragranular, 4 granular, 5 and 6 infragranular. Unpaired equal-variance t-tests\n    between the three layer pairs in each area. Reproduced when the two wM2 values are within\n    tolerance, the wM2 infragranular against supragranular test gives p < 0.05, and no layer pair\n    in A1, wS2 or ALM gives p < 0.05; partially reproduced when the wM2 result holds and one layer\n    pair elsewhere is significant. The claim of no difference in A1, wS2 and ALM is judged by the\n    same t-test at 0.05, uncorrected, as the code runs it.\n- id: fig4-29-clusters\n  statement: Clustering all 10,294 neurons on their average activity in the five correct trial\n    types (PCA, spectral embedding, Gaussian mixture model) gives 29 clusters at the minimum of\n    the Bayesian Information Criterion.\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 6; Figure 4a; Methods,\n    Clustering of neuronal responses\n  quote: The BIC analysis indicated that 29 clusters provided the best trade-off between accuracy\n    and parsimony.\n  expected:\n    quantity: number of clusters at the BIC minimum\n    value: 29\n    tolerance: 3\n  criterion: As code, Neuronal_data_100ms.m and Data_Clustering.ipynb, which produced the reported\n    sigma. Per neuron, the mean over quiet (whisker speed) correct trials of each of the five\n    types in 100 ms bins over -1 to 2 s, baseline (-1 to 0 s) subtracted, sessions with fewer\n    than 3 trials of a type or 5 neurons skipped, the five PSTHs concatenated and divided by\n    their range; neurons mean-centred; PCs kept when their variance exceeds the mean of 1000 row\n    shuffles with Bonferroni p < 0.05/N (17 in the paper); similarity exp(-d/0.07975) on\n    Euclidean distances; normalized Laplacian eigenvectors 2 to 17; diagonal-covariance GMM\n    (1000 initializations, seed 0) for k in 10, 15, 20, 25 to 44, 45, 50, 55; the k of lowest\n    BIC. The Methods' 10 ms version (exp(-d^2/2 sigma^2), sigma tuned to a mean similarity of\n    0.5) is a variant. Reproduced when the BIC minimum is within tolerance (10% of 29, rounded);\n    partially reproduced when it is between 20 and 38.\n- id: fig4b-named-clusters\n  statement: Some clusters represent sensory responses (cluster 1, fast auditory response, mostly\n    A1 neurons; cluster 29, fast whisker response, mostly wS1 and wS2), clusters 11 and 25 fire\n    during the delay only on Go-tone trials and consist mainly of wM2 and ALM neurons, and cluster\n    4 decreases its firing during the Go-tone delay and is spread over the five areas.\n  source: Results, Spatiotemporal dynamics of neocortical activity, paragraph 7; Figure 4a-b\n  quote: 'Cluster #1 had a large and fast response to the auditory cue and mostly consisted of neurons in A1, whereas Cluster #29 responded strongly and rapidly to whisker deflection and mostly consisted of neurons in wS1 and wS2. A few clusters showed strong context-dependent firing selectivity comparing Go-tone and Nogo-tone trials, most notably Clusters #11 and #25, which showed prominent delay period firing only in Go-tone trials and mainly consisted of neurons in wM2 and ALM ( Fig. 4b ). Interestingly, another cluster, Cluster #4, showed a prominent decrease in firing rate during the delay period selectively for Go-tone trials and neurons in this cluster were widely distributed across the five recorded cortical areas'\n  data: with_inputs\n  criterion: Cluster membership from the paper's labels (Zenodo doi:10.5281/zenodo.17973874,\n    processed_data/Data_Clustering.mat), linked to the dataset's units by the code's global unit\n    index; the author adds the link claim. PSTHs as fig3b-delay-and-response-psth. Reproduced\n    when (1) cluster 1 has its largest share of neurons in A1 and a mean response over 0 to 30 ms\n    above its baseline; (2) cluster 29 has more than half its neurons in wS1 and wS2 together and\n    a mean response over 1.0 to 1.03 s above baseline; (3) clusters 11 and 25 each have more\n    than half their neurons in wM2 and ALM together and a higher mean over 0.8 to 1.0 s in Hit\n    than in Nogo-tone Whisker CR trials; (4) cluster 4 has a lower mean over 0.8 to 1.0 s in Hit\n    than in Nogo CR trials and at least 5% of its neurons in each area. \"Mostly\" and \"widely\n    distributed\" are read as these thresholds, as the paper gives none; the fractions are\n    reported. Partially reproduced when three of the four parts hold.\n- id: fig5a-single-neuron-context\n  statement: Comparing Hit with Nogo-tone Whisker correct rejection trials in the last 200 ms of\n    the delay, wM2 has the highest proportion of context-modulated neurons (20% increase firing by\n    8 Hz on average, 14% decrease by 3 Hz), followed by ALM (17% increase by 8 Hz, 16% decrease by\n    3 Hz).\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 1;\n    Figure 5a\n  quote: 'Overall, we found the highest proportion of significantly modulated neurons in wM2 (20% of neurons increased firing on average by 8 Hz and 14% decreased firing by 3 Hz) and ALM (17% increased firing by 8 Hz and 16% decreased firing by 3 Hz). Thus, wM2 contained the largest proportion of Go-tone excited neurons during the delay period.'\n  expected:\n  - quantity: wM2 fraction with higher firing in Hit\n    value: 20\n    tolerance: 2\n    unit: percent\n  - quantity: wM2 mean increase of those neurons\n    value: 8\n    tolerance: 0.8\n    unit: Hz\n  - quantity: wM2 fraction with lower firing in Hit\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  - quantity: wM2 mean decrease of those neurons\n    value: 3\n    tolerance: 0.3\n    unit: Hz\n  - quantity: ALM fraction higher\n    value: 17\n    tolerance: 1.7\n    unit: percent\n  - quantity: ALM mean increase\n    value: 8\n    tolerance: 0.8\n    unit: Hz\n  - quantity: ALM fraction lower\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  - quantity: ALM mean decrease\n    value: 3\n    tolerance: 0.3\n    unit: Hz\n  criterion: As code, Roc_hit_cr3.m and Ghaderi2025_Figure5_a_SingleNeuron.m. Per neuron, spike\n    counts in 0.8 to 1.0 s on quiet completed Hit trials against Nogo-tone Whisker CR trials;\n    AUC, SI and 200-permutation p as in fig3c-delay-modulation-wm2-alm; modulated when p < 0.05;\n    the change in firing is the Hit minus CR mean rate (Hz). Reproduced when the eight values are\n    within tolerance and the wM2 up-modulated fraction is the largest of the five areas;\n    partially reproduced when the wM2 fraction is the largest and some value is out of tolerance.\n- id: fig5b-context-decoding-delay\n  statement: With 50 neurons per area, context (Hit against Nogo-tone Whisker CR) is decoded in the\n    last 200 ms of the delay above baseline in every area, but far better in wM2 (64 +/- 1%) and\n    ALM (61 +/- 1%) than in A1 (52 +/- 1%), wS1 (52 +/- 1%) and wS2 (52 +/- 0.4%).\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 2;\n    Figure 5b\n  quote: 'Focusing on the last 200 ms of the delay period, during which orofacial movements are absent, the auditory context could be decoded from the firing of 50 neurons in each area with accuracy varying across cortical regions: i) A1, 52 ± 1%, p = 0.008, n = 8 sessions across N = 6 mice; ii) wS1, 52 ± 1%, p = 0.0003, n = 17 sessions across N = 9 mice; iii) wS2, 52 ± 0.4%, p = 0.0003, n = 19 sessions across N = 9 mice; iv) wM2, 64 ± 1%, p = 0.0002, n = 18 sessions across N = 8 mice; and v) ALM, 61 ± 1%, p = 0.0004, n = 16 sessions across N = 6 mice.'\n  statistics:\n  - about: A1, delay against baseline accuracy\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.008\n    n: 8 sessions, 6 mice\n  - about: wS1\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0003\n    n: 17 sessions, 9 mice\n  - about: wS2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0003\n    n: 19 sessions, 9 mice\n  - about: wM2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0002\n    n: 18 sessions, 8 mice\n  - about: ALM\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0004\n    n: 16 sessions, 6 mice\n  expected:\n  - quantity: decoding accuracy, A1, 0.8 to 1.0 s\n    value: 52\n    tolerance: 1\n    unit: percent\n  - quantity: decoding accuracy, wS1\n    value: 52\n    tolerance: 1\n    unit: percent\n  - quantity: decoding accuracy, wS2\n    value: 52\n    tolerance: 0.4\n    unit: percent\n  - quantity: decoding accuracy, wM2\n    value: 64\n    tolerance: 1\n    unit: percent\n  - quantity: decoding accuracy, ALM\n    value: 61\n    tolerance: 1\n    unit: percent\n  criterion: As Methods (Population decoding) and code, Decoding_NbNeurons5_50.m and\n    Ghaderi2025_Figure5_b_Decoding.m. Area-sessions with at least 50 neurons; quiet completed Hit\n    against Nogo-tone Whisker CR trials; per 10 ms bin a linear SVM on spike counts, majority\n    class randomly undersampled, features z-scored, 5-fold stratified cross-validation, accuracy\n    the mean over folds; 100 random subsets of 50 neurons (seed = repetition), averaged. Delay\n    accuracy is the mean over bins in 0.8 to 1.0 s; baseline the mean over -1 to 0 s (Methods),\n    with -0.8 to 0 s (code) as variant; two-sided Wilcoxon signed-rank over sessions. The SVM is\n    libsvm nu-SVC with default nu (code) with a C-SVM whose C is chosen by nested 5-fold grid\n    search over 10^-3 to 10^3 (Methods) as variant. Reproduced when the five accuracies are\n    within tolerance, all five tests give p < 0.05, and wM2 and ALM each exceed A1, wS1 and wS2;\n    partially reproduced when the ordering and the tests hold and a value is out of tolerance.\n- id: fig5b-decoding-time-course\n  statement: Context decoding is at chance in the baseline, highest in A1 right after the cue, and\n    during the delay falls in A1, wS1 and wS2 but rises in wM2 and ALM; with fewer neurons\n    accuracy drops but wM2 and ALM stay above A1, wS1 and wS2.\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 2;\n    Figure 5b left and right\n  quote: Decoding in the baseline period was at chance level (50%) for all cortical regions, as\n    expected. Immediately, upon presentation of the auditory contextual cue, the decoding of Go vs\n    Nogo trials was highest in A1, but context could also be decoded from all other recorded\n    cortical regions. The ability to decode context during the delay period rapidly decreased in\n    A1, wS1 and wS2, but increased for wM2 and ALM. ... Decreasing the number of neurons per\n    cortical region through further subsampling reduced decoding accuracy but maintained the\n    overall conclusion that wM2 and ALM more strongly encode context compared to A1, wS1 and wS2.\n  depends_on:\n  - fig5b-context-decoding-delay\n  criterion: Decoding as fig5b-context-decoding-delay, for 5, 10, ..., 50 neurons. Reproduced when\n    (1) the mean baseline accuracy (-1 to 0 s) of each area is within 50 +/- 2%; (2) the mean\n    accuracy over 0 to 0.2 s is highest in A1; (3) for A1, wS1 and wS2 the mean over 0.8 to 1.0\n    s is lower than over 0 to 0.2 s, and for wM2 and ALM it is higher than over 0.3 to 0.5 s;\n    (4) at every neuron count from 10 to 50 the wM2 and ALM delay accuracies exceed those of A1,\n    wS1 and wS2. The windows of (2) and (3) are not given by the paper and are read here from\n    \"immediately\" and \"rapidly\"; the full time courses are shown. Partially reproduced when (1),\n    (2) and (4) hold and (3) fails for one area.\n- id: fig5c-cluster-removal\n  statement: Removing cluster 11 reduces late-delay context decoding in wM2 (by 3.8 +/- 1.0%) and\n    ALM (4.5 +/- 1.4%) with no significant effect in A1, wS1 and wS2; removing cluster 25 also\n    reduces it in wM2 (1.6 +/- 0.6%) and ALM (2.0 +/- 0.6%); removing any other cluster does not\n    significantly decrease decoding.\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 3;\n    Figure 5c\n  quote: 'Removal of Cluster #11 reduced decoding accuracy by 3.8 ± 1.0% ( p = 0.008) for wM2 and by 4.5 ± 1.4% ( p = 0.008) for ALM, with no significant effect upon A1, wS1 and wS2. Removal of Cluster #25 also reduced significantly the decoding accuracy by 1.6 ± 0.6% ( p = 0.03) for wM2 and by 2.0 ± 0.6% ( p = 0.03) for ALM.'\n  statistics:\n  - about: cluster 11, wM2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.008\n    corrected: FDR\n    n: 18 sessions\n  - about: cluster 11, ALM\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.008\n    corrected: FDR\n    n: 16 sessions\n  - about: cluster 25, wM2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.03\n    corrected: FDR\n  - about: cluster 25, ALM\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.03\n    corrected: FDR\n  expected:\n  - quantity: decrease in accuracy, cluster 11 removed, wM2\n    value: 3.8\n    tolerance: 1.0\n    unit: percentage points\n  - quantity: decrease, cluster 11, ALM\n    value: 4.5\n    tolerance: 1.4\n    unit: percentage points\n  - quantity: decrease, cluster 25, wM2\n    value: 1.6\n    tolerance: 0.6\n    unit: percentage points\n  - quantity: decrease, cluster 25, ALM\n    value: 2.0\n    tolerance: 0.6\n    unit: percentage points\n  data: with_inputs\n  depends_on:\n  - fig4b-named-clusters\n  criterion: Cluster labels as fig4b-named-clusters. As code, Decoding_delay.m,\n    Decoding_clusters_random_dropout.m and Ghaderi2025_Figure5_c_Dropcluster11.m. Decoding as\n    fig5b-context-decoding-delay but with all neurons of each area-session (at least 5; 14 A1, 24\n    wS1, 19 wS2, 18 wM2, 16 ALM sessions), once with all and once without the cluster's neurons;\n    the change is without minus with, averaged over 0.8 to 1.0 s; two-sided Wilcoxon\n    signed-rank against zero over sessions, Benjamini-Hochberg FDR over the five areas for each\n    cluster. Reproduced when the four decreases are within tolerance and significant, cluster 11\n    is not significant in A1, wS1 or wS2, and no cluster other than 11 and 25 gives a significant\n    decrease in any area; partially reproduced when clusters 11 and 25 behave as stated and up to\n    two other cluster-area pairs are significant.\n- id: fig5d-null-space-decoding\n  statement: Using only movement-null-space activity of all trials, context is decoded in the\n    late delay much better in wM2 (74 +/- 2%) and ALM (71 +/- 3%) than in A1 (52 +/- 0.8%, not\n    significant), wS1 (52 +/- 0.4%) and wS2 (53 +/- 0.5%).\n  source: Results, Decoding context from neuronal activity during the delay period, paragraph 4;\n    Figure 5d\n  quote: 'During the late delay period, in the 200 ms before whisker stimulus and using only ‘null’ space neuronal activity, we were again able to decode the context with varying success across cortical regions: i) A1, 52 ± 0.8%, p = 0.09; ii) wS1, 52 ± 0.4%, p = 0.0003; iii) wS2, 53 ± 0.5%, p = 0.0004; iv) wM2, 74 ± 2%, p = 0.0002; and v) ALM, 71 ± 3%, p = 0.0004.'\n  statistics:\n  - about: A1, delay against baseline\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.09\n    n: 12 sessions\n  - about: wS1\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0003\n    n: 23 sessions\n  - about: wS2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0004\n    n: 19 sessions\n  - about: wM2\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0002\n    n: 18 sessions\n  - about: ALM\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0004\n    n: 16 sessions\n  expected:\n  - quantity: null-space decoding accuracy, A1\n    value: 52\n    tolerance: 0.8\n    unit: percent\n  - quantity: wS1\n    value: 52\n    tolerance: 0.4\n    unit: percent\n  - quantity: wS2\n    value: 53\n    tolerance: 0.5\n    unit: percent\n  - quantity: wM2\n    value: 74\n    tolerance: 2\n    unit: percent\n  - quantity: ALM\n    value: 71\n    tolerance: 3\n    unit: percent\n  criterion: As Methods and code, Movement_subspace_Define.m, pg_decompose.m,\n    Movement_subspace_Decoding_null.m and Ghaderi2025_Figure5_d_DecodingSubspaces.m.\n    Area-sessions with more than 20 neurons; all completed trials (no quiet selection); spike\n    counts in 10 ms bins z-scored per neuron over all bins and trials; a bin is movement when\n    whisker speed exceeds the session's mean plus one SD over -1 to 0 s; orthogonal 10-dimensional\n    potent and null subspaces from the movement and non-movement covariances (subspaceID\n    orthogonal_subspaces, alpha 0, seed 101); decoding of Hit against Nogo-tone Whisker CR on the\n    10 null dimensions as fig5b-context-decoding-delay, without neuron subsampling; delay 0.8 to\n    1.0 s against baseline (-1 to 0 s Methods, -0.8 to 0 s code). Reproduced when the five\n    accuracies are within tolerance, wS1, wS2, wM2 and ALM give p < 0.05 and A1 does not;\n    partially reproduced when wM2 and ALM exceed 60% and every other area is below 56% but a\n    value or a test differs.\n- id: fig6a-pca-delay-states\n  statement: In the first two PCs, A1, wS1 and wS2 activity returns near its start by the end of\n    the delay, while in correct Go-tone trials wM2 and ALM settle within about 200 ms into a state\n    far from the origin, reached with and without the whisker stimulus; Nogo correct rejections\n    return to baseline and Miss trials fail to reach the Go-tone state. PC1 explains 11% (A1, wS1,\n    wS2), 17% (wM2) and 14% (ALM) of variance, PC2 6% (A1, wS1, wS2) and 8% (wM2, ALM).\n  source: Results, Context-dependent neuronal dynamics during the delay period, paragraph 1;\n    Figure 6a\n  quote: 'Neuronal activity in each cortical area exhibited a rapid response after tone onset in PC1 (explained variance: A1, 11%; wS1, 11%; wS2, 11%; wM2, 17%; and ALM 14%) and PC2 (explained variance: A1, 6%; wS1, 6%; wS2, 6%; wM2, 8%; and ALM 8%). Activity in A1, wS1 and wS2 followed an apparently cyclic trajectory, returning near to the start point by the end of the delay period. However, in correct Go-tone trials, neuronal activity in wM2 and ALM settled rapidly (within ~200 ms) into an apparent fixed point far from the origin ... Interestingly, in error trials where the mouse did not lick in response to the whisker stimulus preceded by a Go-tone (i.e., Miss trials), the neural activity in wM2 and ALM failed to reach the apparent attractor state of correct Go-tone trials.'\n  expected:\n  - quantity: PC1 explained variance, A1\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: PC1, wS1\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: PC1, wS2\n    value: 11\n    tolerance: 1.1\n    unit: percent\n  - quantity: PC1, wM2\n    value: 17\n    tolerance: 1.7\n    unit: percent\n  - quantity: PC1, ALM\n    value: 14\n    tolerance: 1.4\n    unit: percent\n  - quantity: PC2, A1\n    value: 6\n    tolerance: 0.6\n    unit: percent\n  - quantity: PC2, wS1\n    value: 6\n    tolerance: 0.6\n    unit: percent\n  - quantity: PC2, wS2\n    value: 6\n    tolerance: 0.6\n    unit: percent\n  - quantity: PC2, wM2\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  - quantity: PC2, ALM\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  criterion: As code, Ghaderi2025_Figure6_a_pca.m. Per area, a pseudo-population of all its\n    neurons; per neuron, the mean over quiet completed trials of Hit, Nogo-tone Whisker CR,\n    Go-tone No-Whisker CR and Miss in 50 ms bins over -1 to 2 s, baseline (-1 to 0 s) subtracted,\n    the four conditions' first 60 bins concatenated, neurons with zero range dropped, each neuron\n    divided by its range; PCA with time bins as observations; explained variance of PC1 and PC2.\n    The legend's reading (PCs fitted on Hit and Nogo CR only, the other two projected) is a\n    variant. The state at the end of the delay is the mean of PC1 and PC2 over 0.8 to 1.0 s; its\n    distance from the baseline point (mean over -1 to 0 s) is compared across conditions.\n    Reproduced when the ten values are within tolerance and, for wM2 and ALM, the end-of-delay\n    distance of Hit and Go-tone No-Whisker CR each exceeds that of Nogo CR and Miss, while for A1,\n    wS1 and wS2 the Hit distance at 1.0 s is below half its maximum over 0 to 1 s. Partially\n    reproduced when the geometry holds and some explained variances are out of tolerance.\n- id: fig6b-context-coding-direction\n  statement: Projected on a context coding direction, late-delay activity in wM2 and ALM is high in\n    Hit trials and significantly lower in Nogo-tone, Go-tone No-Whisker and Miss trials.\n  source: Results, Context-dependent neuronal dynamics during the delay period, paragraph 2;\n    Figure 6b\n  quote: Activity in the context coding dimension was high in wM2 and ALM throughout the delay\n    period in correct Go-tone Hit trials, but strongly reduced in the incorrect Go-tone Miss\n    trials.\n  statistics:\n  - about: wM2, Hit against Nogo, NoW and Miss\n    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area\n    p: 0.0006\n    corrected: Bonferroni\n    n: 18 sessions\n  - about: wM2, Hit against NoW\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.001\n    corrected: Bonferroni\n  - about: ALM, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.001\n    corrected: Bonferroni\n    n: 16 sessions\n  - about: ALM, Hit against NoW\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.002\n    corrected: Bonferroni\n  - about: ALM, Hit against Miss\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.001\n    corrected: Bonferroni\n  - about: A1, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.002\n    corrected: Bonferroni\n    n: 14 sessions\n  - about: wS1, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test\n    p: 6.0e-5\n    corrected: Bonferroni\n    n: 24 sessions\n  - about: wS2, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0006\n    corrected: Bonferroni\n    n: 19 sessions\n  criterion: As Methods (Principal component analysis and coding directions) and code,\n    Coding_direction_10ms.m and Ghaderi2025_Figure6_b_CD_context.m. Per area-session (at least 5\n    neurons), quiet completed trials in 10 ms bins; CD context is the mean over 0.8 to 1.0 s of\n    the per-bin difference of Hit and Nogo CR mean spike-count vectors, from a random 20% of each\n    class's trials (Methods; 30% in the code, a variant), unit length, Gram-Schmidt orthogonalized\n    with the whisker and lick directions after it (the context direction first, so unchanged);\n    the held-out trials are projected; per session, the mean projection over 0.8 to 1.0 s for Hit,\n    Nogo CR, Go-tone No-Whisker CR and Miss; two-sided Wilcoxon signed-rank Hit against each, p\n    times 3. Reproduced when in wM2 and ALM all three comparisons give corrected p < 0.05 with Hit\n    higher; partially reproduced when two of three hold in each. The legend's p-values for the\n    other areas are reported against the result, not judged.\n- id: fig6c-temporal-correlation\n  statement: In wM2 and ALM the Go-tone induces a long-lasting increase in correlated population\n    activity during the delay in Hit and Go-tone No-Whisker trials, absent in Nogo-tone and Miss\n    trials, while in A1, wS1 and wS2 the cue evokes only a brief increase.\n  source: Results, Context-dependent neuronal dynamics during the delay period, paragraph 3;\n    Figure 6c\n  quote: Presentation of the auditory cue evoked a brief increase in correlated neuronal activity\n    in A1, wS1 and wS2. However, in wM2 and ALM, the Go-tone induced a long-lasting increase in\n    correlated neuronal activity during the delay period in both Hit and Go-tone No-Whisker Correct\n    Rejection trials. In contrast, presentation of the Nogo-tone failed to induce network states\n    with high temporal correlation. Importantly, the highly-correlated network state during the\n    delay period was also absent in Miss trials\n  statistics:\n  - about: wM2, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area\n    p: 0.0006\n    corrected: Bonferroni\n    n: 18 sessions\n  - about: wM2, Hit against NoW\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.02\n    corrected: Bonferroni\n  - about: wM2, Hit against Miss\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0009\n    corrected: Bonferroni\n  - about: ALM, Hit against Nogo\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.002\n    corrected: Bonferroni\n    n: 16 sessions\n  - about: ALM, Hit against NoW\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.001\n    corrected: Bonferroni\n  - about: ALM, Hit against Miss\n    test: two-sided Wilcoxon signed-rank test\n    p: 0.0004\n    corrected: Bonferroni\n  criterion: As Methods (Temporal correlation analysis) and code, Temporal_corrrelation_10ms.m and\n    Ghaderi2025_Figure6_c_temporalCorrelation.m. Per area-session and quiet completed trial, the\n    300 x 300 Pearson correlation matrix of the population spike-count vectors of 10 ms bins over\n    -1 to 2 s; averaged over trials of a type; minus the mean of the off-diagonal entries of the\n    baseline block (-1 to 0 s); the mean over the delay block (0 to 1 s by 0 to 1 s, bins 100 to\n    200 as in the code) per session; Hit against Nogo CR, Go-tone No-Whisker CR and Miss by\n    two-sided Wilcoxon signed-rank, p times 3. The code drops one A1 Hit session (the fourth) by\n    hand; the result is given with and without it. Reproduced when in wM2 and ALM all three\n    comparisons give corrected p < 0.05 with Hit higher; partially reproduced when the Nogo and\n    Miss comparisons hold in both areas. The legend's other p-values (wS1 Hit against Miss 0.006,\n    wS2 Hit against Nogo 0.047) are reported, not judged.\n- id: fig7b-early-whisker-response\n  statement: Whisker-evoked activity in the Go-tone context is transiently reduced in wS1 and wS2\n    around 15 ms after the deflection and higher from about 30 ms on in most areas, compared with\n    the Nogo-tone context.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 1; Figure 7b\n  quote: we found significant changes in evoked activity, with an early transient reduction in the\n    whisker response in wS1 and wS2 for Go-tone trials, followed by an overall increased activity\n    in most cortical regions at later times\n  criterion: As code, psth_5ms.m and Ghaderi2025_Figure7_b_DeltaFR.m. Per neuron, the mean 5 ms\n    PSTH over quiet completed Hit trials and over Nogo-tone Whisker CR trials, each minus its mean\n    over 0.95 to 1.0 s, in Hz; the Hit minus CR difference per bin from 0.955 to 1.1 s; two-sided\n    Wilcoxon signed-rank against zero over the area's neurons. FDR (Benjamini-Hochberg) is\n    applied for each area as the legend says, with the code's FDR over all 5 areas x 30 bins as\n    variant. Reproduced when wS1 and wS2 each have a significant negative bin between 1.010 and\n    1.020 s, and at least three of the five areas have significant positive bins from 1.030 s\n    onward; partially reproduced when only one of wS1 and wS2 shows the early reduction.\n- id: fig7c-no-whisker-cd-change\n  statement: Activity projected on a whisker coding direction, defined from the first 30 ms of\n    No-tone Whisker responses, shows no significant difference between Go-tone and Nogo-tone\n    contexts.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 1; Figure 7c\n  quote: However, no significant context differences were found in analyses of a whisker sensory\n    response coding direction based on the 30 ms of activity evoked by whisker stimuli without a\n    preceding tone cue and without subsequent licking\n  criterion: A claim of absence. As code, Coding_direction_5ms.m and Ghaderi2025_Figure7_c_StimCD.m.\n    Per area-session (at least 5 neurons), 5 ms bins; CD whisker is the mean over 1.0 to 1.03 s\n    minus the mean over -1 to 0 s of the No-tone Whisker CR trial-averaged population vector, from\n    30% of those trials, Gram-Schmidt orthogonalized to CD context and unit length; held-out quiet\n    completed Hit and Nogo-tone Whisker CR trials projected; per session the mean projection in\n    the bin at 1.03 s; the code's test, Kruskal-Wallis of Hit against CR over sessions followed by\n    LSD comparisons, at 0.05. Reproduced when the test does not find a difference in any area;\n    not reproduced when it does in some area. The difference and the paired Wilcoxon signed-rank\n    p are given for each area either way.\n- id: fig7d-context-decoding-after-whisker\n  statement: Decoding context from baseline-subtracted activity in 5 ms bins after the whisker\n    stimulus, significant decoding appears transiently in A1 and wS2 at 15 ms for one bin, and\n    persistently in wM2 from 20 ms and in ALM from 25 ms after the stimulus.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 2; Figure 7d\n  quote: we found that significant context-dependent sensory processing transiently appeared in A1\n    and wS2 at 15 ms after whisker stimulus for a single 5 ms-time bin; and appeared in a more\n    lasting manner in wM2 at 20 ms after whisker stimulus (and all later time bins) and in ALM at\n    25 ms after whisker stimulus (and all later times)\n  criterion: As code, Decoding_afterwhisker_runX.m and Ghaderi2025_Figure7_d_ContextDecoding_WS.m.\n    Per area-session (at least 5 neurons, all neurons), quiet completed Hit against Nogo-tone\n    Whisker CR trials in 5 ms bins from 0.955 to 1.1 s; each trial's counts minus its count in one\n    baseline bin, repeated for each of the 10 bins from 0.955 to 1.0 s and the accuracies averaged;\n    SVM, balancing and folds as fig5b-context-decoding-delay; 5 runs (seeds 1 to 5) averaged.\n    Per bin, accuracy against the mean over 0.955 to 1.0 s by two-sided Wilcoxon signed-rank over\n    sessions, FDR over the area's bins (legend), with the code's FDR over all areas and bins as\n    variant. Reproduced when the first bin of wM2 after which every bin up to 1.1 s is significant\n    is at 1.015 to 1.025 s, the same for ALM is 5 to 10 ms later than wM2, and no such persistent\n    run starts before 1.03 s in A1, wS1 or wS2; partially reproduced when wM2 precedes ALM but\n    the onsets differ from the paper by more than one bin. The single-bin results in A1 and wS2\n    are reported.\n- id: fig8a-wm2-lick-divergence\n  statement: In the first 30 ms after the whisker stimulus, only wM2 activity diverges into\n    separate states for lick and no-lick trials, mainly along the context coding direction, and at\n    30 ms distinguishes lick from no-lick trials both in correct Go-tone and error Nogo-tone\n    conditions; ALM shows a weaker effect and A1, wS1 and wS2 none.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 3; Figure 8a\n  quote: Only wM2 showed a clear divergence of trajectories into two distinct states corresponding\n    to lick vs no-lick outcomes. This separation was primarily along the context coding direction.\n    Single-session analyses confirmed that wM2 activity at 30 ms significantly distinguished lick\n    from no-lick trials both in correct Go-tone and error Nogo-tone conditions ( Supplementary Fig.\n    17 ). ALM showed a weaker effect, and no significant differences were observed in A1, wS1, or\n    wS2.\n  depends_on:\n  - fig7c-no-whisker-cd-change\n  criterion: The test is in Supplementary Fig. 17, not read; its code\n    (Ghaderi2025_Sup_Figure17_Context_CD_LickvsNolick.m with Coding_direction_5ms.m) fixes it.\n    Per area-session, held-out quiet completed trials projected on CD context (5 ms bins, as\n    fig6b-context-coding-direction at 5 ms) and averaged per trial group, Go-tone Whisker lick and\n    no lick, Nogo-tone Whisker lick and no lick, No-tone Whisker lick and no lick; the value in\n    the bin at 1.03 s; Kruskal-Wallis over the six groups across sessions, then LSD comparisons.\n    Reproduced when in wM2 the Kruskal-Wallis p < 0.05 and both Go-tone lick against no lick and\n    Nogo-tone lick against no lick are significant with lick higher, while A1, wS1 and wS2 show no\n    significant lick against no lick comparison; partially reproduced when wM2 holds for one of the\n    two contexts. ALM's comparisons are reported.\n- id: fig8b-lick-coding-direction\n  statement: At 30 ms after the whisker stimulus, activity along a lick coding direction defined\n    from spontaneous licking separates lick from no-lick trials in wM2 for Go-tone, Nogo-tone (false\n    alarm) and No-tone trials, in ALM only for correct trials, and not in A1, wS1 or wS2.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 4; Figure 8b\n  quote: Projecting neuronal activity in the lick coding direction revealed separation between lick\n    and no-lick trials for both correct and false alarm cases in wM2 at 30 ms after delivery of the\n    whisker stimulus ( Fig. 8b ). The lick coding direction did not separate between lick and\n    no-lick trials in A1, wS1 or wS2 at this early time point. Neuronal activity in ALM was higher\n    in the lick coding direction only for correct trials, but false alarm lick trials were not\n    different from no-lick trials at 30 ms post whisker stimulus time.\n  statistics:\n  - about: wM2, six trial groups\n    test: Kruskal-Wallis test\n    p: 0.001\n    n: 10 to 12 sessions\n  - about: wM2, Go-tone lick against no-lick trials (three comparisons)\n    test: LSD-corrected post hoc paired comparisons\n    p: 0.02\n    p_relation: \"<\"\n  - about: wM2, Nogo-tone lick against no-lick trials (three comparisons)\n    test: LSD-corrected post hoc paired comparisons\n    p: 0.005\n    p_relation: \"<\"\n  - about: wM2, No-tone lick against no-lick trials (three comparisons)\n    test: LSD-corrected post hoc paired comparisons\n    p: 0.04\n    p_relation: \"<\"\n  criterion: As Methods and code, Coding_direction_SpontLick.m and\n    Ghaderi2025_Figure8_b_SpontLick_CD_LickvsNolick.m. Spontaneous licks are licks outside 0 to 6\n    s of any trial start, in bouts (lick mask, from Lick_times.mat) longer than 0.5 s, whose mean\n    jaw position over 0 to 0.1 s after the lick exceeds 3 times its mean over -1 to 0 s;\n    sessions with fewer than 2 such licks are dropped. CD lick is the mean over spontaneous\n    licks and neurons' 5 ms counts in 0.2 to 0.5 s minus those in -1 to -0.5 s, unit length.\n    Quiet completed trials are projected and averaged per session in six groups (Go-tone, Nogo-tone\n    and No-tone Whisker, each lick and no lick); the value in the bin at 1.03 s; Kruskal-Wallis\n    over the six groups across sessions, then Fisher LSD comparisons (MATLAB multcompare on the\n    Kruskal-Wallis ranks). The legend's three p-values per context are read as that context's\n    lick group against the three no-lick groups, which the paper does not state. Reproduced when\n    in wM2 the Kruskal-Wallis p < 0.05 and each context's lick group exceeds that context's no-lick\n    group significantly; in ALM the Go-tone lick group exceeds no lick and the Nogo-tone lick group\n    does not; and A1, wS1 and wS2 show no significant lick against no-lick comparison. Partially\n    reproduced when wM2 holds for two of the three contexts.\n- id: figs18-later-lick-coding\n  statement: Later, at 0.2 to 0.4 s after the whisker stimulus, the lick coding direction\n    separates lick from no-lick trials in ALM, wM2, wS2 and wS1, with the effect largest in ALM and\n    ranked in that order.\n  source: Results, Context-dependent processing of the whisker stimulus, paragraph 4\n    (Supplementary Fig. 18)\n  quote: at later times, neuronal activity in the lick coding direction showed significant\n    differentiation between lick and no-lick trials in ALM, wM2, wS2 and wS1 ranked according to\n    the effect size quantified at 0.2-0.4 s after the whisker stimulus with ALM being largest\n  depends_on:\n  - fig8b-lick-coding-direction\n  criterion: Supplementary Fig. 18 was not read; its code\n    (Ghaderi2025_Sup_Figure18_SpontLick_CD_LickvsNolick_200mswindow.m) takes the projection of\n    fig8b-lick-coding-direction averaged over 1.2 to 1.4 s with the same Kruskal-Wallis and LSD\n    test. The effect size is not defined in the paper or the code. Readings (a) the difference of\n    the mean projection of all lick groups and all no-lick groups divided by their pooled SD over\n    sessions (Cohen's d); (b) the Kruskal-Wallis chi-squared statistic. Reproduced when ALM, wM2,\n    wS2 and wS1 each give Kruskal-Wallis p < 0.05 with at least one lick group above its no-lick\n    group, and under both readings ALM has the largest effect; the full ranking is reported. If\n    the readings disagree on which area is largest, blocked as methods_underspecified.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now fix the Fig. 6b and 8b statistics entries to one per test as printed, then run the checker.

**Agent calls Bash**

```bash
cd claims/001530 && python3 - <<'EOF'
p='10.1038-s41467-026-73622-y.yaml'
t=open(p).read()
old6b=t[t.index("  - about: wM2, Hit against Nogo, NoW and Miss"):t.index("  criterion: As Methods (Principal component analysis and coding directions)")]
new6b='''  - about: wM2, Hit against Nogo
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.0006
    corrected: Bonferroni
    n: 18 sessions
  - about: wM2, Hit against NoW
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.001
    corrected: Bonferroni
    n: 18 sessions
  - about: wM2, Hit against Miss
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.0006
    corrected: Bonferroni
    n: 18 sessions
  - about: ALM, Hit against Nogo
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.001
    corrected: Bonferroni
    n: 16 sessions
  - about: ALM, Hit against NoW
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.002
    corrected: Bonferroni
    n: 16 sessions
  - about: ALM, Hit against Miss
    test: two-sided Wilcoxon signed-rank test, Bonferroni for each area
    p: 0.001
    corrected: Bonferroni
    n: 16 sessions
'''
t=t.replace(old6b,new6b)
old8b=t[t.index("  - about: wM2, Go-tone lick against no-lick trials (three comparisons)"):t.index("  criterion: As Methods and code, Coding_direction_SpontLick.m")]
new=''
for ctx,ps in [('Go-tone',['0.01','0.006','0.02']),('Nogo-tone',['0.004','0.002','0.005']),('No-tone',['0.03','0.02','0.04'])]:
    for i,pv in enumerate(ps,1):
        new+=f'''  - about: wM2, {ctx} lick against no-lick trials, comparison {i} of 3
    test: Kruskal-Wallis followed by LSD-corrected post hoc paired comparisons
    p: {pv}
    n: 10 to 12 sessions
'''
t=t.replace(old8b,new)
open(p,'w').write(t)
EOF
cd ../.. && python tools/claims_check.py claims/001530/10.1038-s41467-026-73622-y.yaml paper/10.1038-s41467-026-73622-y.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes. Now checking the style rules (no ": " in plain scalars, no em dashes, no "rather").

**Agent calls Bash**

```bash
cd claims/001530 && grep -n "—\|rather" *.yaml; python3 - <<'EOF'
import yaml
p='10.1038-s41467-026-73622-y.yaml'
# find plain (unquoted) scalar values containing ': ' using the yaml event stream
for ev in yaml.parse(open(p)):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and (': ' in ev.value or ' #' in ev.value):
        print('PLAIN', ev.start_mark.line+1, ev.value[:80])
d=yaml.safe_load(open(p))
print(len(d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
```

```
28 12 28 16
```

**Agent**

Style rules pass. One criterion (fig2-other-trial-types) rests on a threshold I chose alone; I'll recast it as two named readings, and label the SVM grid as a standard choice.

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
p='claims/001530/10.1038-s41467-026-73622-y.yaml'
t=open(p).read()
a=t.index("  criterion: The finding is shown in Supplementary Fig. 3")
b=t.index("- id: units-recorded")
t=t[:a]+'''  criterion: The finding is shown in Supplementary Fig. 3, which was not read; its code
    (Ghaderi2025_Sup_Figure3_a_Heatmaps.m, Sup_Figure3_b_Brainmaps.m) draws per-area, per-window
    changes in P(lick) for the other four trial types and runs no test. Measure as
    fig2-auditory-window for trial types 2 to 5 (6 areas, 3 windows, 4 trial types, 72 changes).
    "Little impact" is not defined. Readings (a) the bootstrap test of fig2-auditory-window, FDR
    within each window and trial type, finds no significant change in more than 7 of the 72 (10%);
    (b) no change exceeds 13 points, the smallest reduction the paper calls significant on Go-tone
    Whisker trials (A1, Whisker window). Reproduced when both readings hold; not reproduced when
    neither does; blocked as methods_underspecified when they differ. Every change and its p are
    reported.
'''+t[b:]
t=t.replace("C-SVM whose C is chosen by nested 5-fold grid\n    search over 10^-3 to 10^3 (Methods) as variant.","C-SVM whose C is chosen by nested 5-fold grid\n    search (Methods; the grid, 10^-3 to 10^3, is a standard choice, the paper gives none) as\n    variant.")
open(p,'w').write(t)
EOF
grep -n "standard choice, the paper" claims/001530/*.yaml; python tools/claims_check.py claims/001530/10.1038-s41467-026-73622-y.yaml paper/10.1038-s41467-026-73622-y.txt; python3 -c "
import yaml
for ev in yaml.parse(open('claims/001530/10.1038-s41467-026-73622-y.yaml')):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and (': ' in ev.value or ' #' in ev.value): print(ev.value[:60])"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001530/10.1038-s41467-026-73622-y.yaml`. The quote checker reports 28 claims, 28 quotes, 52 statistical values and 0 problems. Nothing was committed.

**Text read.** The version of record from Europe PMC (PMC13346651), marked as corrected. It has the main text, figure legends and Methods. Missing: the Supplementary Information (Supp. Figs. 1–19), the Source Data and the text of the correction notice, and there was no PDF. I went ahead because every main finding is stated with its numbers in the main text, as earlier claims files in this repo did. For the three findings the main text cites to supplementary figures (Supp. Figs. 3, 17, 18), the claim is written from the main-text sentence and its method from the code that draws that figure.

**Code read.** Only the code files of the paper's Zenodo record (doi:10.5281/zenodo.17973874), pulled out of the 21 GB zip by range requests, without opening any data file. The GitHub copy (LSENS-BMI-EPFL/Ghaderi_et_al_NCOMMS_2026, commit 20cf10c) is byte-identical for the analysis code.

**Claims.**
- **Coverage:** behaviour (Fig. 1c, 1f, the quiet-trial fraction), optogenetics (Fig. 2: three windows, wM2 against ALM, other trial types), unit counts, Figs. 3 to 8 and Supp. Fig. 18.
- **Quotes:** all 28 have one.
- **Statistics:** 12 claims have them (52 values).
- **Expected values:** 16 claims have them; tolerances are the paper's ± SEM where given, otherwise 10%.
- **Criteria:** all 28 have one.
- **Outside data:** 2 claims (fig4b, fig5c) are `with_inputs`. They need the paper's cluster labels (Zenodo `processed_data/Data_Clustering.mat`), because a new clustering would not number the clusters the same way. The lick-direction claims use `Lick_times.mat` from the same record; whether the dandiset holds those lick times is the author's to check.

**Where the paper and its code disagree.** Methods first, code as a variant, unless noted:
- **Quiet-trial threshold:** Methods say median absolute deviation; the code's `mad()` default is the mean absolute deviation. Both are run.
- **Optogenetics bootstrap:** 1,000 iterations in the Methods, 10,000 in the code. Only 10,000 can produce the reported p = 0.0003.
- **Clustering:** Methods describe 10 ms bins and a Gaussian similarity; the code uses 100 ms bins and exp(−d/σ). The reported σ is the code's 100 ms value, so I followed the code there.
- **Context coding direction:** trained on 20% of trials (Methods) against 30% (code).
- **SVM:** the Methods name a grid search; the code uses libsvm nu-SVC with no search. The baseline is −1 to 0 s (Methods) against −0.8 to 0 s (code).
- **PCA (Fig. 6a):** the legend says the PCs are fitted on two trial types; the Methods and code use four.
- **FDR families (Figs. 7b, 7d):** per area in the legends, pooled over all areas in the code.
- **Session count (paper inconsistency):** the Results say 35 sessions; the Methods say 34.

**Details the paper leaves open, with the readings named:**
- **Movement latency, "time to 20% max" (Fig. 1f):** no code computes it. Readings: per-session mean trace, or per trial.
- **Opto "reduction":** absolute percentage points or relative percent; and whether the ± is SEM or SD.
- **wM2 against ALM opto comparison:** not in the code. Readings: 9 sessions resampled per area, or all sessions; the FDR family is unknown.
- **"Little impact" on other trial types:** the paper's bootstrap test, or a 13-point threshold taken from the smallest significant effect.
- **Fig. 8b pairwise p-values:** which three comparisons each context's three p-values are is not stated; I read them as that context's lick group against the three no-lick groups.
- **Supp. Fig. 18 "effect size":** Cohen's d, or the Kruskal-Wallis statistic.
- **Vague wording:** "mostly" and "widely distributed" (cluster composition) and "immediately" and "rapidly" (decoding time course) are given explicit thresholds in the criteria.

## End of run

66 turns, 13 minutes, result: success.
