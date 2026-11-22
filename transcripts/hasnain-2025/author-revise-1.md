# hasnain-2025 · author-revise-1 · run 44988838682

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/hasnain-2025/verifier-1-report.md; ls entries/hasnain-2025 entries/hasnain-2025/*
```

```
Sun Nov 22 05:24:02 UTC 2026
**Verifier report, round 1: Hasnain, Han & Economo 2025 on DANDI:000363 (0.231012.2129)**

The claims file has 19 claims. 11 rest on the paper's own recordings and 8 on the MAP data. Cells 21 and 31 still contain the author's result text. I read them but reached the outcomes below on my own from the printed outputs.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| own-recordings-cohort, fig1i-selectivity-proportions, fig2c-subspace-variance, fig2e-potent-only-units, fig2f-letn-preference-like-un, fig2gh-letn-span-subspaces, ed2f-false-negatives, fig3c-network-beats-linear, fig3d-letn-un-movement-encoding, ed3-letn-fast-switch, ed3a-cd-early-un-not-letn (11) | blocked (data_missing) | I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174 files in every version). Searching the archive for "Hasnain", "Economo", "extratelencephalic" and "movement-null" finds no dataset with the paper's own recordings. All 11 need phototagged L-ETNs or the paper's videos, so no part can be tested on MAP. |
| map-session-selection | not_reproduced | Cell 12: 17 bilateral sessions from 9 mice (tolerance 20 ± 2). ALM and medulla: 5 sessions from 4 mice, against 11 (Methods) or 16 (Results). Unit counts: ALM 300 (paper 604), medulla 340 (paper 724), right ALM 858 (paper 961 ± 96.1). Only left ALM (1001) is within tolerance. |
| fig4b-medulla-selectivity | partially_reproduced | Cell 16, Bonferroni, E1 reading: sample 34.1%, delay 52.9%, response 86.5%, against 7 / 21 / 49. The order holds (response highest, sample lowest), which the criterion counts as partial, but every value is 2 to 5 times the paper's, under every seed and alpha. |
| fig4c-alm-null-potent-similar | partially_reproduced | Cell 18: the absence holds under every main reading (p 0.13 to 0.26, n = 5). Means are out of tolerance (V1 54.5 / 77.3; V2 null 24.0, below the 28.6 floor). Only the example.m z-score, which M3 calls a "variant"
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md; ls docs tools questions | head -50
```

```
779 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,240p docs/protocol.md; sed -n 470,640p docs/protocol.md; sed -n 726,779p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 289 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 240,470p docs/protocol.md
```

```
kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
     claims are the registry's checks, not findings of the paper, so the
     author adds them to the claims file; they are the only claims the
     author writes. A link claim says how
     records are matched (an identifier, or, where there is none, summary
     values the paper or its code published, such as per-condition medians),
     what fraction match, and whether the matched records agree on what both
     describe, such as counts, layers, or the paper's own per-cell tables. A
     dataset that cannot be linked to the data it was published with is a
     finding about the dataset. Every claim that needs the match lists the
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep hasnain; wc -l attempts/hasnain-2025-01.yaml entries/hasnain-2025/*; ls claims 2>/dev/null | grep hasnain; ls papers/claims 2>/dev/null| grep hasnain; cat questions/hasnain-2025.yaml 2>/dev/null; ls executed/hasnain-2025 2>/dev/null; ls paper
```

```
hasnain-2025-01.yaml
   293 attempts/hasnain-2025-01.yaml
    32 entries/hasnain-2025/README.md
    23 entries/hasnain-2025/entry.yaml
   459 entries/hasnain-2025/map_subspace.py
  1135 entries/hasnain-2025/reproduce_hasnain_2025.ipynb
    10 entries/hasnain-2025/requirements.in
  2934 entries/hasnain-2025/requirements.lock.txt
  4886 total
hasnain-2025.yaml
reproduce_hasnain_2025.ipynb
result.json
10.1101-2025.10.17.682917.txt
```

**Agent calls Bash**

```bash
cat attempts/hasnain-2025-01.yaml; cat entries/hasnain-2025/entry.yaml
```

```
schema_version: 3
id: hasnain-2025-01
datasets:
- archive: dandi
  id: "000363"
  version: 0.231012.2129
  doi: 10.48324/dandi.000363/0.231012.2129
  relation: reuses
paper: doi:10.1101/2025.10.17.682917
date: 2026-11-22
entry: hasnain-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python -c "
import json;nb=json.load(open('reproduce_hasnain_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== cell',i,c['cell_type'],c['metadata'].get('tags',''));print(''.join(c['source']))
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt; cat README.md
```

```
790 /tmp/claude-1001/nb.txt
# Hasnain, Han & Economo (2025) from dandiset 000363

Tests the findings of [Hasnain, Han and Economo (2025)](https://doi.org/10.1101/2025.10.17.682917)
that can be tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the
Mesoscale Activity Map recordings (Chen et al. 2024) that the paper reuses for its Figure 4. The
paper's own cell-type-specific recordings (Figures 1 to 3) are not public.

| Claim | Outcome |
|---|---|
| The paper's selection gives 20 bilateral ALM and 16 (or 11) ALM and medulla sessions | Not reproduced |
| Medullary units are selective, most in the response epoch (7, 21, 49%) | Partially reproduced |
| In ALM, null and potent subspaces explain comparable variance | Partially reproduced |
| In the medulla, the null subspace explains less variance than the potent | Reproduced, resting on one reading |
| ALM predicts medullary null activity nearly as well as the other ALM | Not reproduced |
| Medulla predicts ALM less well than ALM predicts the medulla | Not reproduced |
| The medullary null subspace has lower dimensionality than ALM's | Not reproduced |
| Medullary units do not span ALM's null activity patterns (UMAP) | Partially reproduced |
| Eleven claims on the paper's own recordings | Blocked: data missing |

[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== cell 0 markdown 
2	# Hasnain, Han & Economo (2025) on the MAP dataset, DANDI:000363
3	
4	Paper: Hasnain M. A., Han Y. & Economo M. N., "Mapping neural subspace dynamics onto the structure
5	of the mouse descending motor system", bioRxiv doi:10.1101/2025.10.17.682917 (preprint version 1).
6	The claims file `claims/hasnain-2025.yaml` was written from the preprint's full text (PMC12632980);
7	it fixes what is tested.
8	
9	Dataset: DANDI:000363 (Mesoscale Activity Map Dataset, Chen et al. 2024), version **0.231012.2129**,
10	streamed from the archive. The paper cites the dandiset without a version
11	("https://dandiarchive.org/dandiset/000363"), so the most recent published version is pinned. The
12	earlier versions hold the same 174 sessions; the versions before 0.231012.2129 total 19 to 67 GB and
13	this one 65.7 TB, as it adds the raw recordings. The cell "Version check" compares the units of one
14	session between this version and 0.230822.0128.
15	
16	The paper reuses the MAP data for Figure 4 only. Its own recordings (Figures 1 to 3, Extended Data
17	Figures 2 and 3) are not public, so those eleven claims are blocked.
18	
19	| Claim | Tested here |
20	|---|---|
[... 771 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/hasnain-2025/map_subspace.py"
}
```

```
1	"""Loading and measures for the MAP recordings of dandiset 000363, as Hasnain, Han & Economo (2025)
2	use them for Figure 4 (bioRxiv doi:10.1101/2025.10.17.682917).
3	
4	Each NWB file holds one session: units with spike times, a quality label (`unit_quality`, good or
5	multi), a classification (`classification`, good or unlabelled) and a CCF annotation (`anno_name`,
6	filled only for units classified good); electrodes whose `location` JSON names the probe's target
7	("left ALM", "right Medulla"); a trial table; go cue times (`go_start_times`); and side-camera
8	keypoint tracking of the jaw and nose (about 294 Hz, one segment per trial). Files are streamed from
9	the archive at the pinned version; nothing is written to disk.
10	
11	Where the parameters come from. "Claims" is the claims file `claims/hasnain-2025.yaml`, whose header
12	items M1 to M10 cite the paper; "Methods" is a passage of the paper's Methods.
13	
14	- Session and unit selection (M1, M2; Methods, "Curation of Mesoscale Activity Map Dataset"): units
15	  classified 'good' whose CCF label is MOs on a probe described as targeting ALM, and units in IRN,
16	  GRN or PARN; sessions with at least 30 such units in each region of interest.
17	- Trials. "X moving and X stationary contained data from all correct and error trials" (Methods,
18	  "Subspace identification"): outcome hit or miss. Ignore trials, photostimulation trials and
19	  early-lick trials are left out: an assumption, as the paper's own task has no photostimulation and
20	  the paper does not say how MAP's early-lick and photostimulation trials were treated.
[... 440 more lines not kept]
```

**Agent**

Now the claims file and the executed outputs.

**Agent calls Bash**

```bash
cd  sed -n 1,200p claims/hasnain-2025.yaml
```

```
# Claims for Hasnain, Han & Economo (2025), "Mapping neural subspace dynamics onto the structure
# of the mouse descending motor system", bioRxiv doi:10.1101/2025.10.17.682917, tested on
# DANDI:000363 (Mesoscale Activity Map Dataset), which the paper reuses.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-22,
# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The preprint (version 1, posted 2025-10-17), full text from PMC (PMC12632980), in
# paper/10.1101-2025.10.17.682917.txt: Abstract, Introduction, Results, Discussion, Methods, the
# legends of Extended Data Figures 1 to 3, and the legends of Figures 1 to 4. The paper has no
# separate supplement (PMC lists none); the Extended Data legends are in the text. No PDF was
# supplied, so no figure was read; every claim rests on the text.
#
# Code read. github.com/economolab/subspaceID, commit d593949fef8a39fe0a6eb54a21fc05cbca7bae84,
# the only code the paper links ("Code for identifying movement-null and movement-potent
# subspaces"). It holds orthogonal_subspaces.m (the manopt optimization of the Methods'
# objective, each term normalized by the sum of the top-d eigenvalues of its covariance, with a
# regularization weight alpha that example.m sets to 0), example.m (z-scores each neuron over all
# bins and trials, takes the covariance of stationary and of moving bins, fixes 15 dimensions per
# subspace, rng(101)), and a Python port (funcs.py, example.ipynb). It holds none of the paper's
# other analyses (session selection, movement masks, dimensionality, variance explained,
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id: map-session" claims/hasnain-2025.yaml; awk '/^- id: map-session-selection/,0' claims/hasnain-2025.yaml | grep -v "^  quote" | grep -nE "id:|criterion|^    [a-zA-Z(]" | head -0; awk '/^- id: map-session-selection/,0' claims/hasnain-2025.yaml | grep -A12 -E "^  criterion|^- id"
```

```
330:- id: map-session-selection
- id: map-session-selection
  statement: In the MAP dataset, the paper's selection gives 20 bilateral ALM sessions from 10 mice (961
    right and 1055 left ALM units) and ALM and medulla sessions with 604 ALM units and 724 medullary
    reticular nucleus units.
  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is
    found downstream of motor cortex, paragraphs 1 and 4
  quote: For simultaneous bilateral ALM recordings, we included 20 sessions from 10 mice, consisting of 2016
    units (961 from right ALM and 1055 from left ALM). For simultaneous ALM and medulla recordings, we
    included 11 sessions from 7 mice, consisting of 1328 units (604 from ALM and 724 from medulla).
  expected:
  - quantity: bilateral ALM sessions
    value: 20
    tolerance: 2
--
  criterion: Sessions and units selected as in M1 and M2. The ALM and medulla session count is open between
    (S1) 16 (Results and Figure 4) and (S2) 11 (Methods); the bilateral ALM unit count between 2016
    (Methods) and 1116 (Results). Reproduced when, under one reading of M2, the session counts match one
    of the readings and every unit count is within tolerance; partially reproduced when the session
    counts match and some unit counts do not. The count of mice is reported.
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat executed/hasnain-2025/result.json | head -30; python -c "
import json;nb=json.load(open('executed/hasnain-2025/reproduce_hasnain_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i)
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        print(''.join(t)[:6000])
" > $TMPDIR/out.txt; wc -l $TMPDIR/out.txt
```

```
{
 "entry": "hasnain-2025",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_hasnain_2025.ipynb",
   "ok": true,
   "seconds": 2077,
   "error": null
  }
 ]
}
472 /tmp/claude-1001/out.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt"
}
```

```
1	=== cell 1
2	=== cell 3
3	files: 174  subjects: 28
4	units: 272227
5	classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, ('missing', 'multi'): 651, ('missing', 'good'): 1201}
6	(classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, ('missing', False): 1852}
7	sessions per probe target: {'right Striatum': 57, 'left Striatum': 54, 'right ALM': 103, 'left ALM': 108, 'right Midbrain': 68, 'right Thalamus': 36, 'left Midbrain': 68, 'left Thalamus': 45, 'right Medulla': 24, 'left Medulla': 23, 'right ECT': 14, 'left ECT': 18, 'left BLA': 9, 'right BLA': 8}
8	sessions with probes in both ALMs: 60 from 18 mice
9	sessions with an ALM and a medulla probe: 36 from 8 mice
10	units in the medullary nuclei of M2: {'Intermediate reticular nucleus': 279, 'Gigantocellular reticular nucleus': 704, 'Parvicellular reticular nucleus': 190}
11	units labelled MOs (any probe): 7346
12	units labelled MOs on probes not targeting ALM: 0
13	
14	=== cell 5
15	assets in 0.230822.0128: 174  same paths as pinned: 103  same sessions: 174
16	example path there: sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+ogen.nwb
17	
18	              units    spikes good                                       first_spikes                                        acquisition
19	0.231012.2129  1205  24087958  279  [0.000342, 0.051943, 0.078377, 0.116145, 0.130...  [BehavioralEvents, BehavioralTimeSeries, Elect...
20	0.230822.0128  1205  24087958  279  [0.000342, 0.051943, 0.078377, 0.116145, 0.130...           [BehavioralEvents, BehavioralTimeSeries]
[... 453 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/hasnain-2025/.venv/bin | head; date -u; cat > $TMPDIR/probe.py <<'EOF'
import sys; sys.path.insert(0,'entries/hasnain-2025')
import map_subspace as ms, numpy as np, json
from dandi.dandiapi import DandiAPIClient
ds = DandiAPIClient().get_dandiset(ms.DANDISET_ID, ms.DANDISET_VERSION)
p="sub-460436/sub-460436_ses-20200109T111437_behavior+ecephys+image+ogen.nwb"
a=ds.get_asset_by_path(p); url=a.get_content_url(follow_redirects=1, strip_query=True)
f=ms.open_file(url)
el=f["general/extracellular_ephys/electrodes"]
print(list(el.keys()))
for k in el.keys():
    d=el[k]
    try: print(k, d.shape, d.dtype, d[:3], d.attrs.get('description'))
    except Exception as e: print(k, e)
u=f["units"]; print(list(u.keys()))
for k in u.keys():
    print(k, u[k].shape, u[k].dtype, u[k].attrs.get('description'))
tr=f["intervals/trials"]; print(list(tr.keys()))
for k in ("outcome","photostim_duration","early_lick","trial_instruction"):
    print(k, sorted(set(ms._dec(tr[k][:]))))
for k in tr.keys():
    print(k, tr[k].shape, tr[k][:3])
print(list(f["acquisition/BehavioralEvents"].keys()))
EOF
executed/hasnain-2025/.venv/bin/python $TMPDIR/probe.py
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
bids-validator-deno
bst
Sun Nov 22 05:24:55 UTC 2026
['electrode', 'filtering', 'group', 'group_name', 'id', 'imp', 'location', 'rel_x', 'rel_y', 'rel_z', 'shank', 'shank_col', 'shank_row', 'x', 'y', 'z']
electrode (1155,) int64 [1 2 3] electrode index, starts at 0
filtering (1155,) object [b'' b'' b''] description of hardware filtering, including the filter name and frequency cutoffs
group (1155,) object [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>] a reference to the ElectrodeGroup this electrode is a part of
group_name (1155,) object [b'19011116163 1-96; 1281-1376; 2561-2656; 3841-3936'
 b'19011116163 1-96; 1281-1376; 2561-2656; 3841-3936'
 b'19011116163 1-96; 1281-1376; 2561-2656; 3841-3936'] the name of the ElectrodeGroup this electrode is a part of
id (1155,) int64 [0 1 2] None
imp (1155,) float64 [-1. -1. -1.] the impedance of the electrode, in ohms
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/survey2.py <<'EOF'
import sys, pickle, time; sys.path.insert(0,'entries/hasnain-2025')
import map_subspace as ms, numpy as np, json
from concurrent.futures import ThreadPoolExecutor
t0=time.time()
def ut(url):
    f = ms.open_file(url)
    e = f["general/extracellular_ephys/electrodes"]
    loc = ms._dec(e["location"][:])
    xyz = np.c_[e["x"][:], e["y"][:], e["z"][:]]
    u = f["units"]
    el = u["electrodes"][:]; idx = u["electrodes_index"][:]
    first = el[np.r_[0, idx[:-1]]]
    target = [json.loads(loc[i])["brain_regions"] for i in first]
    anno = [a if isinstance(a, str) else "" for a in ms._dec(u["anno_name"][:])]
    cl = [c if isinstance(c, str) else "missing" for c in ms._dec(u["classification"][:])]
    return dict(target=target, classification=cl, quality=ms._dec(u["unit_quality"][:]), anno=anno,
                elec=first, xyz=xyz[first], subject=f["general/subject/subject_id"][()].decode())
assets = ms.asset_urls()
with ThreadPoolExecutor(8) as ex:
    tabs = list(ex.map(lambda pa: ut(pa[1]), assets))
pickle.dump({p:t for (p,_),t in zip(assets,tabs)}, open(sys.argv[1],'wb'))
print("done", time.time()-t0)
EOF
executed/hasnain-2025/.venv/bin/python $TMPDIR/survey2.py $TMPDIR/survey.pkl
```

```
done 303.97355127334595
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/explore.py <<'EOF'
import sys, pickle, collections; sys.path.insert(0,'entries/hasnain-2025')
import numpy as np, map_subspace as ms
T=pickle.load(open(sys.argv[1],'rb'))
# consistency: same xyz -> same anno among good units
agree=dis=0; dists=[]
for p,t in T.items():
    xyz=np.array(t['xyz']); anno=np.array(t['anno']); cl=np.array(t['classification']); tg=np.array(t['target'])
    g=cl=='good'
    for target in set(tg):
        m=tg==target
        lab=np.where(g&m)[0]; unl=np.where(~g&m)[0]
        if len(lab)==0: continue
        # leave-one-out nearest labelled neighbour agreement among labelled
        X=xyz[lab]
        D=np.linalg.norm(X[:,None]-X[None],axis=2); np.fill_diagonal(D,np.inf)
        nn=D.argmin(1)
        agree+=np.sum(anno[lab][nn]==anno[lab]); dis+=np.sum(anno[lab][nn]!=anno[lab])
        if len(unl):
            Du=np.linalg.norm(xyz[unl][:,None]-X[None],axis=2)
            dists+=list(Du.min(1))
print("LOO nearest-labelled agreement", agree, dis, agree/(agree+dis))
d=np.array(dists); print("dist of unlabelled to nearest labelled unit (um) pct 50,90,99:", np.percentile(d,[50,90,99]), "frac 0:", np.mean(d==0))
EOF
executed/hasnain-2025/.venv/bin/python $TMPDIR/explore.py $TMPDIR/survey.pkl
```

```
LOO nearest-labelled agreement 67609 1844 0.9734496710005327
dist of unlabelled to nearest labelled unit (um) pct 50,90,99: [nan nan nan] frac 0: 0.49386329023203035
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/explore2.py <<'EOF'
import sys, pickle, collections; sys.path.insert(0,'entries/hasnain-2025')
import numpy as np, map_subspace as ms
T=pickle.load(open(sys.argv[1],'rb'))
nanfrac=np.mean([np.isnan(np.array(t['xyz'])).any(1).mean() for t in T.values()]); print("mean frac units with nan xyz per file", nanfrac)
print("files with any nan xyz:", sum(np.isnan(np.array(t['xyz'])).any() for t in T.values()))
def transfer(t, maxd):
    xyz=np.array(t['xyz'],float); anno=np.array(t['anno'],object); cl=np.array(t['classification']); tg=np.array(t['target'])
    out=anno.copy(); dist=np.zeros(len(anno))
    g=(cl=='good')
    for target in set(tg):
        m=tg==target
        lab=np.where(g&m&np.isfinite(xyz).all(1))[0]; unl=np.where(~g&m)[0]
        if len(unl)==0: continue
        if len(lab)==0:
            out[unl]=""; continue
        Du=np.linalg.norm(xyz[unl][:,None]-xyz[lab][None],axis=2)
        Du=np.where(np.isnan(Du),np.inf,Du)
        j=Du.argmin(1); dmin=Du.min(1)
        out[unl]=np.where(dmin<=maxd, anno[lab][j], "")
    return out
for maxd in (0, 20, 40, 100):
  for mode in ("quality good","all"):
    cnt={}
    bil=[];am=[]
    for p,t in T.items():
        an=transfer(t,maxd)
        q=np.array(t['quality']); 
        keep=(q=='good') if mode=="quality good" else np.ones(len(q),bool)
        regs=collections.Counter()
        for k,(tg,a) in enumerate(zip(t['target'],an)):
            if not keep[k]: continue
            r=ms.region_of(tg,a)
            if r: regs[r]+=1
        if regs['left ALM']>=30 and regs['right ALM']>=30: bil.append((p,regs['right ALM'],regs['left ALM']))
        alm=[r for r in ('left ALM','right ALM') if regs[r]>=30]
        if regs['medulla']>=30 and alm: am.append((p,sum(regs[r] for r in alm),regs['medulla']))
    print(f"maxd {maxd} {mode}: bilateral {len(bil)} sessions {len({b[0].split('/')[0] for b in bil})} mice R {sum(b[1] for b in bil)} L {sum(b[2] for b in bil)}; ALM+med {len(am)} sessions {len({b[0].split('/')[0] for b in am})} mice ALM {sum(b[1] for b in am)} med {sum(b[2] for b in am)}")
EOF
executed/hasnain-2025/.venv/bin/python $TMPDIR/explore2.py $TMPDIR/survey.pkl
```

```
mean frac units with nan xyz per file 0.010552560884466655
files with any nan xyz: 97
maxd 0 quality good: bilateral 28 sessions 11 mice R 2136 L 2352; ALM+med 13 sessions 6 mice ALM 832 med 1051
maxd 0 all: bilateral 35 sessions 13 mice R 3651 L 4181; ALM+med 26 sessions 8 mice ALM 2589 med 2514
maxd 20 quality good: bilateral 31 sessions 12 mice R 2767 L 2830; ALM+med 19 sessions 7 mice ALM 1501 med 1745
maxd 20 all: bilateral 44 sessions 15 mice R 5230 L 5868; ALM+med 28 sessions 8 mice ALM 3646 med 3577
maxd 40 quality good: bilateral 35 sessions 12 mice R 3071 L 3402; ALM+med 22 sessions 8 mice ALM 1908 med 2105
maxd 40 all: bilateral 48 sessions 15 mice R 5873 L 6782; ALM+med 28 sessions 8 mice ALM 4018 med 4178
maxd 100 quality good: bilateral 37 sessions 12 mice R 3376 L 3665; ALM+med 24 sessions 8 mice ALM 2222 med 2444
maxd 100 all: bilateral 51 sessions 16 mice R 6437 L 7400; ALM+med 29 sessions 8 mice ALM 4511 med 4810
```

**Agent calls Bash**

```bash
cd  sed -n 330,375p claims/hasnain-2025.yaml | grep -A3 quantity
```

```
- quantity: bilateral ALM sessions
    value: 20
    tolerance: 2
  - quantity: right ALM units
    value: 961
    tolerance: 96.1
  - quantity: left ALM units
    value: 1055
    tolerance: 105.5
  - quantity: ALM units in ALM and medulla sessions
    value: 604
    tolerance: 60.4
  - quantity: medulla units in ALM and medulla sessions
    value: 724
    tolerance: 72.4
  criterion: Sessions and units selected as in M1 and M2. The ALM and medulla session count is open between
--
  - quantity: medulla units selective in sample epoch
    value: 7
    tolerance: 0.7
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
s=open('map_subspace.py').read()
s=s.replace('''    target = [json.loads(loc[i])["brain_regions"] for i in first]
    anno = [a if isinstance(a, str) else "" for a in _dec(u["anno_name"][:])]
    tr = f["intervals/trials"]
    classification = [c if isinstance(c, str) else "missing" for c in _dec(u["classification"][:])]
    return dict(target=target, classification=classification,
                quality=_dec(u["unit_quality"][:]), anno=anno,''','''    target = [json.loads(loc[i])["brain_regions"] for i in first]
    el_tab = f["general/extracellular_ephys/electrodes"]
    xyz = np.c_[el_tab["x"][:], el_tab["y"][:], el_tab["z"][:]][first]
    anno = [a if isinstance(a, str) else "" for a in _dec(u["anno_name"][:])]
    tr = f["intervals/trials"]
    classification = [c if isinstance(c, str) else "missing" for c in _dec(u["classification"][:])]
    return dict(target=target, classification=classification,
                quality=_dec(u["unit_quality"][:]), anno=anno, xyz=xyz,''')
s=s.replace('''def select_sessions(tables, min_units=MIN_UNITS):
    """Sessions and units under M1 and M2 (U1): units classified good with a CCF region."""
    bilateral, alm_med = {}, {}
    for path, t in tables.items():
        regions = {}
        for i, (tg, cl, an) in enumerate(zip(t["target"], t["classification"], t["anno"])):
            if cl != "good":
                continue
            r = region_of(tg, an)''','''def transfer_labels(t, max_dist=TRANSFER_DIST):
    """CCF label per unit: `anno_name` for units classified good; for the others, the label of the
    nearest unit classified good on the same probe, by the CCF coordinates (x, y, z) of the units'
    electrodes, when it is within `max_dist` um, else empty (an assumption, see the module docstring)."""
    xyz = np.asarray(t["xyz"], float)
    anno = np.array(t["anno"], dtype=object)
    good = np.array(t["classification"]) == "good"
    target = np.array(t["target"])
    out = anno.copy()
    for tg in set(target):
        on = target == tg
        lab = np.where(good & on & np.isfinite(xyz).all(1))[0]
        unl = np.where(~good & on)[0]
        if len(unl) == 0:
            continue
        if len(lab) == 0:
            out[unl] = ""
            continue
        d = np.linalg.norm(xyz[unl][:, None] - xyz[lab][None], axis=2)
        d = np.where(np.isnan(d), np.inf, d)
        out[unl] = np.where(d.min(1) <= max_dist, anno[lab][d.argmin(1)], "")
    return list(out)


def select_sessions(tables, min_units=MIN_UNITS, label="classification", max_dist=TRANSFER_DIST):
    """Sessions and units under M1 and M2. `label`: 'classification' (G1, U1: units classified good,
    with their own CCF label), 'quality' (G2: `unit_quality` good, labels from `transfer_labels`) or
    'all' (U2: every unit, labels from `transfer_labels`)."""
    bilateral, alm_med = {}, {}
    for path, t in tables.items():
        regions = {}
        if label == "classification":
            keep, annos = [c == "good" for c in t["classification"]], t["anno"]
        else:
            annos = transfer_labels(t, max_dist)
            keep = [q == "good" for q in t["quality"]] if label == "quality" else [True] * len(annos)
        for i, (tg, k, an) in enumerate(zip(t["target"], keep, annos)):
            if not k:
                continue
            r = region_of(tg, an)''')
s=s.replace('''TRACK_SMOOTH_FRAMES = 3   # Gaussian s.d. in frames (about 10 ms) on keypoint positions
''','''TRACK_SMOOTH_FRAMES = 3   # Gaussian s.d. in frames (about 10 ms) on keypoint positions
TRANSFER_DIST = 20.0      # um, nearest labelled unit for reading G2 (about one electrode row)
''')
s=s.replace('''  GRN or PARN; sessions with at least 30 such units in each region of interest.
''','''  GRN or PARN; sessions with at least 30 such units in each region of interest. This is reading G1
  of 'good'. Reading G2 takes `unit_quality` good. Only units classified good carry a CCF label, so
  under G2 (and under U2, all units) a unit takes the label of the nearest unit classified good on
  the same probe, by the CCF coordinates of their electrodes (electrodes table x, y, z), within 20
  um (`TRANSFER_DIST`, about one electrode row): an assumption. Among units classified good, the
  nearest other such unit has the same label for 97% of units (shown in the notebook).
''')
s=s.replace('''    trials = {k: _dec(tr[k][:]) for k in ("outcome", "trial_instruction", "early_lick", "photostim_duration")}''','''    trials = {k: _dec(tr[k][:]) for k in ("outcome", "trial_instruction", "early_lick", "photostim_duration")}
    trials["sample"] = f["acquisition/BehavioralEvents/sample_start_times/timestamps"][:]''')
# B9: total covariance from tracked bins only
s=s.replace('''    cs, cm, c = cov(xs), cov(xm), cov(x)''','''    cs, cm, c = cov(xs), cov(xm), cov(x[m >= 0])''')
s=s.replace('''    mask (trials, bins). `dims` reuses (d_null, d_pot) from the shuffle; else they are estimated."""''','''    mask (trials, bins). `dims` reuses (d_null, d_pot) from the shuffle; else they are estimated.
    The total covariance C of the variance explained is taken over the bins with tracking."""''')
# ridge: span denominator and per-bin outputs
s=s.replace('''def ridge_r2(src, tgt, train, test, bins, standardize, pooled, lam=None):
    """R2 on the test trials at each bin (claims, M8). src, tgt: (trials, bins, dims)."""
    lam = RIDGE_LAMBDA if lam is None else lam
    xl = lagged(src)
    r2 = np.empty(len(bins))
    for k, t in enumerate(bins):''','''def ridge_r2(src, tgt, train, test, bins, standardize, pooled, lam=None, span=False):
    """R2 on the test trials at each bin (claims, M8). src, tgt: (trials, bins, dims).
    With `span`, also the R2 over the whole span: residuals summed over bins, over the variance of the
    test targets about their mean over all bins and trials (a variant; it keeps time-locked variance)."""
    lam = RIDGE_LAMBDA if lam is None else lam
    xl = lagged(src)
    r2 = np.empty(len(bins))
    res_all = np.zeros(tgt.shape[2])
    for k, t in enumerate(bins):''')
s=s.replace('''        r2[k] = 1 - res.sum() / tot.sum() if pooled else np.mean(1 - res / tot)
    return r2''','''        r2[k] = 1 - res.sum() / tot.sum() if pooled else np.mean(1 - res / tot)
        res_all += res
    if not span:
        return r2
    y = tgt[test][:, bins].astype(np.float64).reshape(-1, tgt.shape[2])
    tot_all = ((y - y.mean(0)) ** 2).sum(0)
    r2_span = 1 - res_all.sum() / tot_all.sum() if pooled else np.mean(1 - res_all / tot_all)
    return r2, r2_span''')
# selectivity: faster shuffles, optional blocks
s=s.replace('''def selectivity_p(x, is_right, rng, n_shuffle=1000):
    """AUROC and the share of label shuffles at least as far from 0.5 (Methods)."""
    from scipy.stats import rankdata
    r = rankdata(x)
    n1 = int(is_right.sum())
    n2 = len(x) - n1
    obs = (r[is_right].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)
    perms = np.array([rng.permutation(len(x)) for _ in range(n_shuffle)])
    lab = is_right[perms]''','''def selectivity_p(x, is_right, rng, n_shuffle=1000, blocks=None):
    """AUROC and the share of label shuffles at least as far from 0.5 (Methods). With `blocks` (a
    block number per trial), labels are shuffled only within blocks of trials (a check for slow drift
    over the session, not the paper's test)."""
    from scipy.stats import rankdata
    r = rankdata(x)
    n1 = int(is_right.sum())
    n2 = len(x) - n1
    obs = (r[is_right].sum() - n1 * (n1 + 1) / 2) / (n1 * n2)
    if blocks is None:
        lab = rng.permuted(np.tile(is_right, (n_shuffle, 1)), axis=1)
    else:
        lab = np.tile(is_right, (n_shuffle, 1))
        for b in np.unique(blocks):
            cols = np.where(blocks == b)[0]
            lab[:, cols] = rng.permuted(lab[:, cols], axis=1)''')
open('map_subspace.py','w').write(s)
EOF
grep -n "TRANSFER_DIST\|permuted\|span" map_subspace.py | head -20
```

```
20:  um (`TRANSFER_DIST`, about one electrode row): an assumption. Among units classified good, the
89:TRANSFER_DIST = 20.0      # um, nearest labelled unit for reading G2 (about one electrode row)
141:def transfer_labels(t, max_dist=TRANSFER_DIST):
165:def select_sessions(tables, min_units=MIN_UNITS, label="classification", max_dist=TRANSFER_DIST):
440:def ridge_r2(src, tgt, train, test, bins, standardize, pooled, lam=None, span=False):
442:    With `span`, also the R2 over the whole span: residuals summed over bins, over the variance of the
461:    if not span:
465:    r2_span = 1 - res_all.sum() / tot_all.sum() if pooled else np.mean(1 - res_all / tot_all)
466:    return r2, r2_span
479:        lab = rng.permuted(np.tile(is_right, (n_shuffle, 1)), axis=1)
484:            lab[:, cols] = rng.permuted(lab[:, cols], axis=1)
```

**Agent**

Now the notebook edits. I'll restructure `cell 9` into a reusable loader, add the requested outputs, and put reading G2 in a second notebook so each stays under the 60-minute limit.

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
s=open('map_subspace.py').read()
s=s.replace('''    trials["sample"] = f["acquisition/BehavioralEvents/sample_start_times/timestamps"][:]''','''    bev = f["acquisition/BehavioralEvents"]
    trials["sample"] = bev["sample_start_times/timestamps"][:] if "sample_start_times" in bev else np.array([])''')
open('map_subspace.py','w').write(s)
EOF
date -u
```

```
Sun Nov 22 05:33:08 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/edit1.py <<'PYEOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a[:60]); put(i,s.replace(a,b))
# cell 9: loader function, trial labels, sample cue
rep(9,'''urls = dict(assets)
W = ms.WINDOWS["W1"]
sessions = {}
check_rows = []
rng_check = np.random.default_rng(seed("map-session-selection"))
for p in list(alm_med) + list(bilateral):
    if p in sessions:
        continue
    regions = alm_med[p] if p in alm_med else bilateral[p]
    ids = sorted(set(sum((v for k, v in regions.items() if k != "alm_sides"), [])))
    s = ms.load_session(urls[p], ids)''','''urls = dict(assets)
W = ms.WINDOWS["W1"]
sessions = {}
check_rows = []
labels_seen = collections.defaultdict(collections.Counter)
rng_check = np.random.default_rng(seed("map-session-selection"))
for p in list(alm_med) + list(bilateral):
    if p in sessions:
        continue
    regions = alm_med[p] if p in alm_med else bilateral[p]
    ids = sorted(set(sum((v for k, v in regions.items() if k != "alm_sides"), [])))
    s = ms.load_session(urls[p], ids)
    for k in ("outcome", "photostim_duration", "early_lick", "trial_instruction"):
        labels_seen[k].update(s["trials"][k])''')
rep(9,'''    go = gos[keep]
    speed''','''    go = gos[keep]
    smp = s["trials"]["sample"]
    j = np.searchsorted(smp, go) - 1
    sample_rel = np.where(j >= 0, smp[np.maximum(j, 0)] - go, np.nan)
    speed''')
rep(9,'''                           lick_lat_ms=round(1000 * np.nanmedian(lick_lat)),''','''                           lick_lat_ms=round(1000 * np.nanmedian(lick_lat)),
                           sample_from_go_s=round(float(np.nanmedian(sample_rel)), 3),
                           sample_min=round(float(np.nanmin(sample_rel)), 3), sample_max=round(float(np.nanmax(sample_rel)), 3),''')
rep(9,'''print("trials kept per session: %d to %d" % (checks.kept.min(), checks.kept.max()))''','''print("trials kept per session: %d to %d" % (checks.kept.min(), checks.kept.max()))
print("trial labels over the selected sessions:", {k: dict(v) for k, v in labels_seen.items()})
print("sample cue onset relative to the go cue, kept trials: median per session %.3f to %.3f s, over all trials %.3f to %.3f s"
      % (checks.sample_from_go_s.min(), checks.sample_from_go_s.max(), checks.sample_min.min(), checks.sample_max.max()))
print("baseline window", ms.BASELINE, "s: ends before the earliest sample onset:", ms.BASELINE[1] < checks.sample_min.min())''')
# cell 12 : G2 / U2 readings
rep(12,'''# thresholds on the count of good units: sessions selected''','''# label transfer for readings G2 and U2: among units classified good, does the nearest other such
# unit on the same probe (electrode CCF coordinates) carry the same CCF label?
agree = n_lab = 0
for t in tables.values():
    xyz, an = np.asarray(t["xyz"], float), np.array(t["anno"], dtype=object)
    g, tgs = np.array(t["classification"]) == "good", np.array(t["target"])
    for tg in set(tgs):
        lab = np.where(g & (tgs == tg) & np.isfinite(xyz).all(1))[0]
        if len(lab) < 2:
            continue
        d = np.linalg.norm(xyz[lab][:, None] - xyz[lab][None], axis=2)
        np.fill_diagonal(d, np.inf)
        agree += int((an[lab][d.argmin(1)] == an[lab]).sum())
        n_lab += len(lab)
print(f"nearest unit classified good has the same CCF label: {agree} of {n_lab} ({100 * agree / n_lab:.1f}%)")
g_rows = []
for label, dist in [("classification", None), ("quality", 0.0), ("quality", 20.0), ("quality", 40.0), ("all", 20.0)]:
    b2, a2 = ms.select_sessions(tables, label=label, max_dist=dist if dist is not None else ms.TRANSFER_DIST)
    g_rows.append(dict(reading={"classification": "G1", "quality": "G2", "all": "U2"}[label], transfer_um=dist,
                       bilateral=len(b2), bilateral_mice=len({p.split("/")[0] for p in b2}),
                       right_ALM=sum(len(v["right ALM"]) for v in b2.values()),
                       left_ALM=sum(len(v["left ALM"]) for v in b2.values()),
                       alm_med=len(a2), alm_med_mice=len({p.split("/")[0] for p in a2}),
                       ALM=sum(len(v["ALM"]) for v in a2.values()), medulla=sum(len(v["medulla"]) for v in a2.values())))
print(pd.DataFrame(g_rows).to_string())
print("paper: bilateral 20 sessions from 10 mice, 961 right and 1055 left; ALM and medulla 16 (or 11 from 7 mice), 604 ALM and 724 medulla")

# thresholds on the count of good units: sessions selected''')
# cell 15: prepare takes a session dict; proj for every reading; moving fraction per epoch
rep(15,'''def prepare(p, region_ids, reading, keep_mask=None):
    v = sessions[p]
    s, go''','''def prepare(p, region_ids, reading, store=None):
    v = (sessions if store is None else store)[p]
    s, go''')
rep(15,'''            fit["moving_frac"] = float((mv == 1).sum() / (mv >= 0).sum())''','''            fit["moving_frac"] = float((mv == 1).sum() / (mv >= 0).sum())
            fit["proj"] = (z @ fit["qn"]).astype(np.float32)''')
rep(15,'''print("peak memory %.0f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))''','''print("peak memory %.0f MB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))

# moving bins by epoch (share of tracked bins), readings B1 and B2, and bins without tracking
tax_w1 = ms.WINDOWS["W1"][0] + ms.BIN * np.arange(fits[(next(iter(alm_med)), "ALM", "main")]["mv"].shape[1])
ep_spans = {"baseline": ms.BASELINE, "sample": (-1.8, -1.2), "delay": (-1.2, 0.0), "response": (0.0, 1.5)}
mrows = []
for p in alm_med:
    for B in ("B1", "B2"):
        mv = ms.movement_mask(sessions[p]["speed"], sessions[p]["log_thr"], short_runs_move=B == "B2")
        row = dict(session=p.split("/")[1][:30], reading=B, untracked=round(float((mv < 0).mean()), 3))
        for ep, (a, b) in ep_spans.items():
            m = mv[:, (tax_w1 >= a) & (tax_w1 < b)]
            row[ep] = round(float((m == 1).sum() / max((m >= 0).sum(), 1)), 3)
        mrows.append(row)
print(pd.DataFrame(mrows).to_string())''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit1.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/edit2.py <<'PYEOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a[:60]); put(i,s.replace(a,b))
# selectivity: blocks
rep(17,'''def selectivity(rng):
    out = []''','''def selectivity(rng, block_trials=None):
    out = []''')
rep(17,'''        is_right = np.r_[np.ones(n, bool), np.zeros(n, bool)]''','''        is_right = np.r_[np.ones(n, bool), np.zeros(n, bool)]
        blocks = None if block_trials is None else pick // block_trials''')
rep(17,'''                auc, pv = ms.selectivity_p(x, is_right, rng)''','''                auc, pv = ms.selectivity_p(x, is_right, rng, blocks=blocks)''')
rep(17,'''print(by_sess.round(1).to_string())''','''print(by_sess.round(1).to_string())

# slow drift: the share of right trials (correct, kept) by fifth of the session, and the same test
# with labels shuffled only within blocks of 30 consecutive kept trials (a check, not the paper's test)
pos_rows = []
for p in alm_med:
    v = sessions[p]
    out_arr = np.array(v["sess"]["trials"]["outcome"])[v["keep"]]
    instr = np.array(v["sess"]["trials"]["trial_instruction"])[v["keep"]]
    hit_idx = np.where(out_arr == "hit")[0]
    fifths = np.array_split(hit_idx, 5)
    pos_rows.append(dict(session=p.split("/")[1][:30],
                         **{f"right share, fifth {k + 1}": round(float(np.mean(instr[f] == "right")), 2) for k, f in enumerate(fifths)}))
print(pd.DataFrame(pos_rows).to_string())
sel_block = selectivity(np.random.default_rng(seed("fig4b-medulla-selectivity", 1)), block_trials=30)
print("labels shuffled within blocks of 30 kept trials (claim seed plus 1):")
print(pd.Series(summarize_sel(sel_block, 0.01)).round(1).to_string())''')
# bilateral fits: Zall too
rep(28,'''for p, s in bilateral.items():
    for reg in ("right ALM", "left ALM"):
        z, mv, nfb = prepare(p, s[reg], READINGS["main"])
        fit = ms.fit_region(z, mv, rng_sub)
        fit["proj"] = (z @ fit["qn"]).astype(np.float32)
        fit["n_fallback"] = nfb
        fits[(p, reg, "main")] = fit''','''for p, s in bilateral.items():
    for reg in ("right ALM", "left ALM"):
        for rname in ("main", "Zall"):
            z, mv, nfb = prepare(p, s[reg], READINGS[rname])
            fit = ms.fit_region(z, mv, rng_sub)
            fit["proj"] = (z @ fit["qn"]).astype(np.float32)
            fit["n_fallback"] = nfb
            fit["z_absmax"] = float(np.abs(z).max())
            fits[(p, reg, rname)] = fit''')
rep(28,'''for p, s in alm_med.items():
    for reg in ("ALM", "medulla"):
        f0 = fits[(p, reg, "main")]
        f0["proj"] = (f0["z"] @ f0["qn"]).astype(np.float32)
''','''''')
rep(28,'''Main reading only (W1, B1, D1, baseline z-score); each hemisphere's subspaces from its own units.''','''XX''') if False else None
# decoding
rep(30,'''def decode(rng, readings):''','''def decode(rng, readings, zread="main", keep_bins=False):''')
rep(30,'''                    xs, xt = fits[(p, src, "main")]["proj"], fits[(p, tgt, "main")]["proj"]
                    for stdz, pooled in readings:
                        r2 = ms.ridge_r2(xs, xt, train, test, bins, stdz, pooled)
                        rows.append(dict(kind=kind, session=p, T=T, src=src, tgt=tgt,
                                         std=stdz, R="R1" if pooled else "R2", r2=100 * r2.mean(),
                                         d_src=xs.shape[2], d_tgt=xt.shape[2], n_train=len(train)))''','''                    xs, xt = fits[(p, src, zread)]["proj"], fits[(p, tgt, zread)]["proj"]
                    for stdz, pooled in readings:
                        r2, r2_span = ms.ridge_r2(xs, xt, train, test, bins, stdz, pooled, span=True)
                        rows.append(dict(kind=kind, session=p, T=T, src=src, tgt=tgt,
                                         std=stdz, R="R1" if pooled else "R2", r2=100 * r2.mean(),
                                         r2_span=100 * r2_span, r2_median=100 * np.median(r2),
                                         d_src=xs.shape[2], d_tgt=xt.shape[2], n_train=len(train),
                                         **({"r2_bins": r2, "tgt_var": xt[test][:, bins].var(0).mean(1)} if keep_bins else {})))''')
rep(30,'''def dec_summary(df):
    out = []''','''def dec_summary(df, col="r2"):
    df = df.assign(r2=df[col])
    out = []''')
rep(30,'''dec_main = decode(np.random.default_rng(seed("fig4d-alm-predicts-medulla-null")), ALL_READ)''','''dec_main = decode(np.random.default_rng(seed("fig4d-alm-predicts-medulla-null")), ALL_READ, keep_bins=True)''')
rep(30,'''print(dec_main[(dec_main["T"] == "T1") & (~dec_main["std"]) & (dec_main.R == "R1")][
    ["kind", "session", "src", "tgt", "d_src", "d_tgt", "n_train", "r2"]].round(1).to_string())''','''print(dec_main[(dec_main["T"] == "T1") & (~dec_main["std"]) & (dec_main.R == "R1")][
    ["kind", "session", "src", "tgt", "d_src", "d_tgt", "n_train", "r2", "r2_median", "r2_span"]].round(1).to_string())''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/edit3.py <<'PYEOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def mk(kind, s, tags=None):
    c={"cell_type":kind,"metadata":{} ,"source":s.splitlines(True)}
    if tags: c["metadata"]["tags"]=tags
    if kind=="code": c["outputs"]=[]; c["execution_count"]=None
    return c
assert ''.join(C[31]['source']).startswith('seed_dec = []')
md = mk("markdown", '''Readings of the R2 and of the z-score, and where the negative values come from. The same splits
(claim seed) under: R2 over the whole span (residuals summed over bins, over the variance of the
test targets about their mean over all bins and trials, which keeps the time-locked variance that
the per-bin R2 removes; not in the claims file's M8, a variant); the median over bins next to the
mean; and the subspaces of the example.m z-score (claims, M3 variant), whose rates have lighter
tails. Then, per session, the per-bin R2 by epoch and the across-trial variance of the test targets
at each bin (T1, unstandardized, R1, main reading).''')
code = mk("code", '''TAGS = ["T", "std", "R"]
show = ["T", "std", "R", "ALM_to_med", "med_to_ALM", "p_asym", "ALM_ALM_A1", "R_to_L", "L_to_R"]
print("main reading, R2 over the whole span:")
print(dec_summary(dec_main, "r2_span")[show].round(2).to_string())
print("main reading, median over bins of the per-bin R2:")
print(dec_summary(dec_main, "r2_median")[show].round(2).to_string())
dec_z = decode(np.random.default_rng(seed("fig4d-alm-predicts-medulla-null")), ALL_READ, zread="Zall")
print("example.m z-score, per-bin R2 averaged:")
print(dec_summary(dec_z)[show].round(2).to_string())
print("example.m z-score, R2 over the whole span:")
print(dec_summary(dec_z, "r2_span")[show].round(2).to_string())
zmax = {(p, r): f["z_absmax"] if "z_absmax" in f else float(np.abs(f["z"]).max())
        for (p, r, rn), f in fits.items() if rn == "main"}
zmax_all = {(p, r): f["z_absmax"] for (p, r, rn), f in fits.items() if rn == "Zall" and "z_absmax" in f}
print("largest |z| over regions: baseline z-score %.0f to %.0f; example.m z-score (bilateral) %.0f to %.0f"
      % (min(zmax.values()), max(zmax.values()), min(zmax_all.values()), max(zmax_all.values())))

# per-bin R2 by epoch, main reading, T1, unstandardized, R1
sel = dec_main[(dec_main["T"] == "T1") & (~dec_main["std"]) & (dec_main.R == "R1")]
tb = ms.WINDOWS["W1"][0] + ms.BIN * bins
ep_masks = {"sample": (tb < -1.2), "delay": (tb >= -1.2) & (tb < 0), "response": tb >= 0}
brows = []
for _, r in sel.iterrows():
    row = dict(kind=r.kind, session=r.session.split("/")[1][:30], src=r.src, z_absmax_src=round(zmax[(r.session, r.src)]),
               r2_mean=round(r.r2, 1), r2_median=round(r.r2_median, 1),
               bins_below_minus1=round(float(np.mean(r.r2_bins < -1)), 2), worst_bin=round(100 * float(r.r2_bins.min())))
    for ep, m in ep_masks.items():
        row[f"R2 {ep}"] = round(100 * float(r.r2_bins[m].mean()), 1)
        row[f"var {ep}"] = round(float(r.tgt_var[m].mean()), 3)
    brows.append(row)
bin_df = pd.DataFrame(brows)
print(bin_df.to_string())
print("across sessions and directions, Spearman correlation of mean R2 with the source's largest |z|: %.2f"
      % stats.spearmanr(bin_df.r2_mean, bin_df.z_absmax_src).correlation)
fig, ax = plt.subplots(1, 2, figsize=(11, 3.2))
for _, r in sel[sel.kind == "ALM-medulla"].iterrows():
    ax[0].plot(tb, 100 * np.clip(r.r2_bins, -5, 1), lw=0.6, label=f"{r.session.split('_')[1][4:12]} {r.src}")
    ax[1].plot(tb, r.tgt_var, lw=0.6)
ax[0].set(xlabel="time from go cue (s)", ylabel="R2 (%), clipped at -500", title="per-bin R2, ALM and medulla sessions")
ax[1].set(xlabel="time from go cue (s)", ylabel="across-trial variance of target", yscale="log", title="test targets")
ax[0].legend(fontsize=5)
plt.tight_layout()
print("per-bin R2 below -500%% (clipped in the plot): %d of %d bins"
      % (sum(int((r.r2_bins < -5).sum()) for _, r in sel[sel.kind == "ALM-medulla"].iterrows()), len(bins) * (sel.kind == "ALM-medulla").sum()))
print("elapsed %.0f s" % (time.time() - T0))''', ['claim:fig4d-alm-predicts-medulla-null', 'claim:fig4d-decoding-asymmetry'])
C[32:32]=[md, code]
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit3.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/edit4.py <<'PYEOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a[:60]); put(i,s.replace(a,b))
i=38; assert src(i).startswith('import umap')
rep(i,'''def umap_run(rng, random_state):
    train_rows, test_rows, region = [], [], []
    for p, s in alm_med.items():''','''def umap_run(rng, random_state, exclude=()):
    train_rows, test_rows, region, sess = [], [], [], []
    for p, s in alm_med.items():
        if p in exclude:
            continue''')
rep(i,'''            region += [reg] * tr.shape[1]''','''            region += [reg] * tr.shape[1]
            sess += [p.split("/")[1][:30]] * tr.shape[1]''')
rep(i,'''    return model.transform(Xte), np.array(region)''','''    return model.transform(Xte), np.array(region), np.array(sess)''')
rep(i,'''def nn_stats(emb, region, rng, k=10, n_shuffle=1000):''','''def nn_stats(emb, region, rng, k=10, n_shuffle=1000, within=None):
    """Observed shares, and the null with region labels shuffled over all units or, with `within`
    (a session label per unit), within each session."""''')
rep(i,'''    obs = frac(region)
    null = np.array([frac(rng.permutation(region)) for _ in range(n_shuffle)])
    return obs, null''','''    def shuffled():
        if within is None:
            return rng.permutation(region)
        lab = region.copy()
        for s_ in np.unique(within):
            m = within == s_
            lab[m] = rng.permutation(region[m])
        return lab

    obs = frac(region)
    null = np.array([frac(shuffled()) for _ in range(n_shuffle)])
    return obs, null''')
rep(i,'''    emb, region = umap_run(rng_u, random_state=sd_ % (2 ** 31))
    obs, null = nn_stats(emb, region, rng_u)
    umap_res[k] = (emb, region, obs, null)
    print(f"seed offset {k}: ALM units with no medulla unit among 10 neighbours {100 * obs[0]:.1f}% "
          f"(shuffled labels {100 * null[:, 0].mean():.1f}%, 95th pct {100 * np.percentile(null[:, 0], 95):.1f}%); "
          f"medulla units with an ALM neighbour {100 * obs[1]:.1f}% (shuffled {100 * null[:, 1].mean():.1f}%)")
emb, region, obs, null = umap_res[0]
fig, ax = plt.subplots(figsize=(5, 4.5))
for reg, c in (("ALM", "tab:blue"), ("medulla", "tab:orange")):
    ax.scatter(*emb[region == reg].T, s=6, c=c, label=f"{reg} ({(region == reg).sum()})", alpha=0.7)
ax.legend()
ax.set(title="Test-set UMAP of movement-null reconstructions", xlabel="UMAP 1", ylabel="UMAP 2")''','''    emb, region, sess = umap_run(rng_u, random_state=sd_ % (2 ** 31))
    obs, null = nn_stats(emb, region, rng_u)
    _, null_w = nn_stats(emb, region, rng_u, within=sess)
    umap_res[k] = (emb, region, sess, obs, null, null_w)
    print(f"seed offset {k}: ALM units with no medulla unit among 10 neighbours {100 * obs[0]:.1f}% "
          f"(labels shuffled over all units {100 * null[:, 0].mean():.1f}%, within session {100 * null_w[:, 0].mean():.1f}%, "
          f"95th pct {100 * np.percentile(null_w[:, 0], 95):.1f}%); "
          f"medulla units with an ALM neighbour {100 * obs[1]:.1f}% (over all {100 * null[:, 1].mean():.1f}%, "
          f"within session {100 * null_w[:, 1].mean():.1f}%, 5th pct {100 * np.percentile(null_w[:, 1], 5):.1f}%)")
emb, region, sess, obs, null, null_w = umap_res[0]
fig, ax = plt.subplots(1, 2, figsize=(10, 4.5))
for reg, c in (("ALM", "tab:blue"), ("medulla", "tab:orange")):
    ax[0].scatter(*emb[region == reg].T, s=6, c=c, label=f"{reg} ({(region == reg).sum()})", alpha=0.7)
ax[0].legend()
ax[0].set(title="Test-set UMAP of movement-null reconstructions", xlabel="UMAP 1", ylabel="UMAP 2")
for k_, s_ in enumerate(np.unique(sess)):
    for reg, mk_ in (("ALM", "o"), ("medulla", "^")):
        m = (sess == s_) & (region == reg)
        ax[1].scatter(*emb[m].T, s=8, marker=mk_, color=plt.cm.tab10(k_), alpha=0.7,
                      label=f"{s_[:19]} {reg}")
ax[1].legend(fontsize=5)
ax[1].set(title="by session (circles ALM, triangles medulla)", xlabel="UMAP 1", ylabel="UMAP 2")
plt.tight_layout()
ext = []
for s_ in np.unique(sess):
    p_ = next(p for p in alm_med if s_ in p)
    for reg in ("ALM", "medulla"):
        e = emb[(sess == s_) & (region == reg)]
        ext.append(dict(session=s_, region=reg, units=len(e), d_null=fits[(p_, reg, "main")]["d"][0],
                        x_lo=round(float(e[:, 0].min()), 2), x_hi=round(float(e[:, 0].max()), 2),
                        y_lo=round(float(e[:, 1].min()), 2), y_hi=round(float(e[:, 1].max()), 2),
                        spread=round(float(np.linalg.norm(e - e.mean(0), axis=1).mean()), 2)))
print(pd.DataFrame(ext).to_string())''')
rep(i,'''print("elapsed %.0f s, peak memory %.0f MB"''','''# variant: without the session whose medulla has d_null = 1 (all its units lie on one line)
low = [p for p in alm_med if fits[(p, "medulla", "main")]["d"][0] < 2 or fits[(p, "ALM", "main")]["d"][0] < 2]
rng_u = np.random.default_rng(seed("fig4f-medulla-null-not-spanning-alm", 1))
emb_x, region_x, sess_x = umap_run(rng_u, random_state=seed("fig4f-medulla-null-not-spanning-alm", 1) % (2 ** 31), exclude=low)
obs_x, null_x = nn_stats(emb_x, region_x, rng_u, within=sess_x)
grid_x = np.floor((emb_x - emb_x.min(0)) / ((emb_x.max(0) - emb_x.min(0)) / 10 + 1e-12)).astype(int)
ca = {tuple(g) for g, r in zip(grid_x, region_x) if r == "ALM"}
cm_ = {tuple(g) for g, r in zip(grid_x, region_x) if r == "medulla"}
print("without", [p.split("/")[1][:30] for p in low], "(claim seed plus 1):",
      f"ALM units with no medulla neighbour {100 * obs_x[0]:.1f}% (within-session shuffle {100 * null_x[:, 0].mean():.1f}%), "
      f"medulla units with an ALM neighbour {100 * obs_x[1]:.1f}% (within-session shuffle {100 * null_x[:, 1].mean():.1f}%); "
      f"grid cells with ALM {len(ca)}, of which without medulla {len(ca - cm_)}; medulla cells outside ALM cells {len(cm_ - ca)} of {len(cm_)}")
for reg in ("ALM", "medulla"):
    e = emb_x[region_x == reg]
    print(" ", reg, "5th to 95th percentile: x %.2f to %.2f, y %.2f to %.2f" % (*np.percentile(e[:, 0], [5, 95]), *np.percentile(e[:, 1], [5, 95])))
print("elapsed %.0f s, peak memory %.0f MB"''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit4.py && echo ok; date -u
```

```
ok
Sun Nov 22 05:34:41 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/mkdev.py <<'PYEOF'
import json,sys
nb=json.load(open(sys.argv[1]))
out=["import matplotlib; matplotlib.use('Agg')\nimport pickle\n"]
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    s=''.join(c['source'])
    if i==3:
        s=s.replace("tables = ms.survey(assets)","tables = pickle.load(open('%s','rb'))" % sys.argv[3])
    if i==1:
        s=s.replace("SEED_OFFSETS = [0, 1000, 2000, 3000, 4000]","SEED_OFFSETS = [0, 1000]")
    out.append(f"print('##### cell {i}', flush=True)\n"+s+"\n")
    if i==7:
        out.append("alm_med = {k: alm_med[k] for k in list(alm_med)[:2]}\nbilateral = {k: bilateral[k] for k in list(bilateral)[:2]}\n")
open(sys.argv[2],'w').write('\n'.join(out))
PYEOF
python $TMPDIR/mkdev.py reproduce_hasnain_2025.ipynb $TMPDIR/dev.py $TMPDIR/survey.pkl; cd entries/hasnain-2025 && /usr/bin/time -v ../../executed/hasnain-2025/.venv/bin/python $TMPDIR/dev.py > $TMPDIR/dev.log 2> $TMPDIR/dev.err; tail -5 $TMPDIR/dev.err; grep -E "Maximum resident|Elapsed" $TMPDIR/dev.err
```

```
Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 1
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.49
	Maximum resident set size (kbytes): 161056
```

**Agent calls Bash**

```bash
head -30 $TMPDIR/dev.err; tail -5 $TMPDIR/dev.log
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 17, in <module>
    import map_subspace as ms
ModuleNotFoundError: No module named 'map_subspace'
Command exited with non-zero status 1
	Command being timed: "../../executed/hasnain-2025/.venv/bin/python /tmp/claude-1001/dev.py"
	User time (seconds): 1.34
	System time (seconds): 0.13
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.49
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 161056
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 2
	Minor (reclaiming a frame) page faults: 29683
	Voluntary context switches: 402
	Involuntary context switches: 38
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
PYTHONPATH=. /usr/bin/time -v ../../executed/hasnain-2025/.venv/bin/python $TMPDIR/dev.py > $TMPDIR/dev.log 2> $TMPDIR/dev.err; grep -v Warning $TMPDIR/dev.err | grep -B2 -A12 Traceback | head -40; grep -E "Maximum resident|Elapsed" $TMPDIR/dev.err
```

```
Elapsed (wall clock) time (h:mm:ss or m:ss): 4:27.00
	Maximum resident set size (kbytes): 1854812
```

**Agent calls Bash**

```bash
cut -c1-250 $TMPDIR/dev.log | grep -v "^$" | sed -n '1,400p' | grep -v "^ *[0-9]* *sub-4.*bilateral ALM\|^ *[0-9]* *ALM-ALM"
```

```
<persisted-output>
Output too large (31.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/556cf469-9403-4389-8318-d36013353b01/tool-results/bhqhlz8cb.txt

Preview (first 2KB):
##### cell 1
##### cell 3
files: 174  subjects: 28
units: 272227
classification x unit_quality: {('unlabelled', 'multi'): 108153, ('good', 'good'): 60978, ('unlabelled', 'good'): 92769, ('good', 'multi'): 8475, ('missing', 'multi'): 651, ('missing', 'good'): 1201}
(classification, has CCF annotation): {('unlabelled', False): 200922, ('good', True): 69453, ('missing', False): 1852}
sessions per probe target: {'left Striatum': 54, 'right ALM': 103, 'left ALM': 108, 'right Striatum': 57, 'right Midbrain': 68, 'right Thalamus': 36, 'left Thalamus': 45, 'left Midbrain': 68, 'right Medulla': 24, 'left Medulla': 23, 'left ECT': 18, '
sessions with probes in both ALMs: 60 from 18 mice
sessions with an ALM and a medulla probe: 36 from 8 mice
units in the medullary nuclei of M2: {'Intermediate reticular nucleus': 279, 'Gigantocellular reticular nucleus': 704, 'Parvicellular reticular nucleus': 190}
units labelled MOs (any probe): 7346
units labelled MOs on probes not targeting ALM: 0
##### cell 5
assets in 0.230822.0128: 174  same paths as pinned: 103  same sessions: 174
example path there: sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+ogen.nwb
              units    spikes good                                       first_spikes                                        acquisition
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-260 $TMPDIR/dev.log | grep -v "^$" | awk '/##### cell 9/,0' | grep -v "ALM-ALM\|bilateral ALM" | head -150
```

```
##### cell 9
                          session  trials  kept  hits  right  go_in_trial  speed_thr  tongue_lat_ms  tongue_pre_go  lick_lat_ms  sample_from_go_s  sample_min  sample_max  acc -2.0  acc -2.0 shuffled  acc -1.0  acc -1.0 shuffled  acc -0.4  acc -0.4 shuffled  ac
0  sub-456774_ses-20191022T133136     570   149   123     83          570       24.5            271          0.003          422             -1.85       -2.45       -0.95      0.58               0.44      0.79               0.51      0.75               0.55    
1  sub-460436_ses-20200109T111437     517   313   272    120          517       30.0            120          0.047          323             -1.85       -2.45       -0.95      0.68               0.52      0.70               0.52      0.76               0.56    
2  sub-440956_ses-20190208T133600     480   334   312    156          480       35.0             90          0.000          200             -1.85       -1.85       -1.85      0.48               0.47      0.51               0.53      0.50               0.44    
3  sub-440956_ses-20190207T120657     368   225   121    128          368       27.8            105          0.000          246             -1.85       -1.85       -1.85      0.55               0.52      0.62               0.49      0.58               0.51    
trials kept per session: 149 to 334
trial labels over the selected sessions: {'outcome': {'ignore': 499, 'hit': 1143, 'miss': 293}, 'photostim_duration': {'N/A': 1517, '0.5000': 418}, 'early_lick': {'no early': 1808, 'early': 127}, 'trial_instruction': {'right': 1058, 'left': 877}}
sample cue onset relative to the go cue, kept trials: median per session -1.850 to -1.850 s, over all trials -2.450 to -0.950 s
baseline window (-2.1, -1.85) s: ends before the earliest sample onset: False
median tongue latency over sessions: 112 ms; first lick 284 ms
elapsed 66 s
##### cell 10
mean speed range over sessions and bins: 8.9 to 163.0 pixels/s
speed in sub-456774_ses-20191022T133136 
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-300 $TMPDIR/dev.log | grep -v "^$" | awk '/##### cell 28/,0' | grep -v "^ *[0-9]* *ALM-ALM" | head -120
```

```
##### cell 28
sub-440956_ses-20190208T133600 [(6, 5), (8, 8)] elapsed 203 s
sub-440956_ses-20190207T120657 [(6, 6), (1, 2)] elapsed 212 s
peak memory 1299 MB
##### cell 30
    T    std   R  ALM_to_med      sem1  med_to_ALM      sem2  p_asym  ALM_ALM_A1        sem3      R_to_L      L_to_R
0  T1  False  R1   -381.1546  382.1582   -409.0269  411.9426  0.5211 -29183.1075  29060.7675 -21688.7377 -36677.4773
1  T1  False  R2   -486.3762  487.3798   -464.0606  466.1601  0.4840 -44199.8952  44077.0507 -30330.5266 -58069.2638
2  T1   True  R1   -303.6473  304.7932   -338.3218  341.2793  0.5162 -15980.0298  15862.4763  -8442.7254 -23517.3342
3  T1   True  R2   -391.2125  392.3584   -385.1878  387.3305  0.4427 -24058.3770  23940.3393 -12709.9117 -35406.8423
4  T2  False  R1   -107.1540  106.9709   -207.8888  210.0222  0.5072 -32945.8766  30647.3954 -23778.4190 -42113.3341
5  T2  False  R2   -133.2894  133.1063   -231.8484  232.6341  0.5031 -49866.0852  47566.5725 -37263.5370 -62468.6334
6  T2   True  R1   -106.0145  106.0958   -204.6886  206.8871  0.5068 -13723.0179  11801.9771 -10747.3866 -16698.6492
7  T2   True  R2   -131.9041  131.9854   -228.1808  229.0346  0.5025 -22435.4372  20513.3899 -18760.3035 -26110.5710
expected ALM to medulla 40 +- 8.1, ALM to ALM 54 +- 7.0, medulla to ALM 21 +- 6.7 (p = 1.2e-4)
per session, T1, unstandardized, R1:
           kind                                                                    session        src        tgt  d_src  d_tgt  n_train       r2  r2_median  r2_span
0   ALM-medulla  sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb        ALM    medulla     11     12      104   -763.3     -610.2   -455.8
4   ALM-medulla  sub-456774/sub-456774_ses-20191022T133136_behavior+ecephys+image+ogen.nwb    medulla        ALM     12     11      104   -821.0     -634.1   -611.4
16  ALM-medulla  sub-460436/sub-460436_ses-20200109T111437_behavior+ecephys+image+ogen.nwb        ALM    medulla      4      1      219      1.0    
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -A12 "Cross-region decoding" paper/*.txt | head -60; grep -n -i "baseline\|-2.1\|sample epoch\|delay epoch" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
t=open('paper/10.1101-2025.10.17.682917.txt').read()
import re
for key in ["Cross-region decoding","delay epoch","1.2 s delay","variable"]:
    for m in re.finditer(key,t):
        print('----',key,m.start()); print(t[max(0,m.start()-200):m.start()+900].replace('\n',' '))
        break
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1101-2025.10.17.682917.txt').read(); i=t.find('This produced a predictor matrix'); print(t[i:i+1500])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/smp.py <<'EOF'
import sys, pickle, collections; sys.path.insert(0,'entries/hasnain-2025')
import numpy as np, map_subspace as ms
T=pickle.load(open(sys.argv[1],'rb'))
b,a=ms.select_sessions(T); b2,a2=ms.select_sessions(T,label="quality")
urls=dict(ms.asset_urls())
for p in list(a)+[x for x in a2 if x not in a][:6]:
    f=ms.open_file(urls[p]); bev=f["acquisition/BehavioralEvents"]
    tr=f["intervals/trials"]
    st,sp=tr["start_time"][:],tr["stop_time"][:]
    go=bev["go_start_times/timestamps"][:]; smp=bev["sample_start_times/timestamps"][:]; dl=bev["delay_start_times/timestamps"][:]
    s={"trials":{"start_time":st,"stop_time":sp},"go":go}
    g=ms.go_times(s)
    j=np.searchsorted(smp,g)-1; rel=np.round(smp[j]-g,2)
    j2=np.searchsorted(dl,g)-1; reld=np.round(dl[j2]-g,2)
    print(p.split('/')[1][:30], 'G1' if p in a else 'G2', "sample rel go:", collections.Counter(rel).most_common(6), "delay start rel go:", collections.Counter(reld).most_common(4), "protocol", collections.Counter(tr["task_protocol"][:]).most_common(3))
EOF
executed/hasnain-2025/.venv/bin/python $TMPDIR/smp.py $TMPDIR/survey.pkl
```

```
sub-456774_ses-20191022T133136 G1 sample rel go: [(np.float64(-1.85), 525), (np.float64(-2.45), 23), (np.float64(-0.95), 16), (np.float64(-2.13), 1), (np.float64(-3.32), 1), (np.float64(-2.29), 1)] delay start rel go: [(np.float64(-1.2), 531), (np.float64(-1.8), 23), (np.float64(-0.3), 16)] protocol [(np.int64(1), 570)]
sub-460436_ses-20200109T111437 G1 sample rel go: [(np.float64(-1.85), 430), (np.float64(-0.95), 16), (np.float64(-2.45), 8), (np.float64(-3.06), 3), (np.float64(-3.18), 2), (np.float64(-2.57), 2)] delay start rel go: [(np.float64(-1.2), 483), (np.float64(-1.8), 18), (np.float64(-0.3), 16)] protocol [(np.int64(1), 517)]
sub-460436_ses-20200110T142717 G1 sample rel go: [(np.float64(-1.85), 431), (np.float64(-2.45), 23), (np.float64(-0.95), 17), (np.float64(-4.27), 3), (np.float64(-3.11), 1), (np.float64(-2.29), 1)] delay start rel go: [(np.float64(-1.2), 459), (np.float64(-1.8), 24), (np.float64(-0.3), 17)] protocol [(np.int64(1), 500)]
sub-484676_ses-20210419T130102 G1 sample rel go: [(np.float64(-1.85), 477), (np.float64(-0.95), 27), (np.float64(-2.45), 24), (np.float64(-3.01), 3), (np.float64(-2.7), 2), (np.float64(-3.24), 2)] delay start rel go: [(np.float64(-1.2), 546), (np.float64(-1.8), 27), (np.float64(-0.3), 27)] protocol [(np.int64(1), 600)]
sub-484677_ses-20210418T132006 G1 sample rel go: [(np.float64(-1.85), 611), (np.float64(-0.95), 37), (np.float64(-2.45), 30), (np.float64(-4.33), 2), (np.float64(-2.65), 2), (np.float64(-1.98), 1)] delay start rel go: [(np.float64(-1.2), 646), (np.float64(-1.8), 37), (np.float64(-0.3), 37)] protocol [(np.int64(1), 720)]
sub-456773_ses-20191002T143533 G2 sample rel go: [(np.float64(-1.85), 487), (np.float64(-0.95), 34), (np.float64(-2.45), 17), (np.float64(-3.59), 2), (np.float64(-3.1), 2), (np.float64(-3.21), 2)] delay start rel go: [(np.float64(-1.2), 523), (np.float64(-0.3), 35), (np.float64(-1.8), 23)] protocol [(np.int64(1), 581)]
sub-456773_ses-20191004T143720 G2 sample rel go: [(np.float64(-1.85), 4
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/hasnain-2025; grep -n "def trial_mask" -A8 map_subspace.py
```

```
Sun Nov 22 05:40:44 UTC 2026
234:def trial_mask(sess, correct_only=False):
235-    t = sess["trials"]
236-    out = np.array(t["outcome"])
237-    ok = np.isin(out, ["hit"] if correct_only else ["hit", "miss"])
238-    ok &= np.array(t["photostim_duration"]) == "N/A"
239-    ok &= np.array(t["early_lick"]) == "no early"
240-    ok &= np.isfinite(go_times(sess))
241-    return ok
242-
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
s=open('map_subspace.py').read()
s=s.replace('''    ok &= np.isfinite(go_times(sess))
    return ok''','''    go = go_times(sess)
    ok &= np.isfinite(go)
    ok &= np.abs(sample_onset(sess, go) - SAMPLE_ONSET) < 0.02
    return ok


def sample_onset(sess, go):
    """Onset of the last sample cue before each go cue, relative to it (s); NaN where none."""
    smp = sess["trials"]["sample"]
    j = np.searchsorted(smp, np.nan_to_num(go, nan=-np.inf)) - 1
    return np.where((j >= 0) & np.isfinite(go), smp[np.maximum(j, 0)] - go, np.nan)''')
s=s.replace('''TRANSFER_DIST = 20.0''','''SAMPLE_ONSET = -1.85     # s from the go cue: 0.65 s sample and the 1.2 s delay of the paper's task
TRANSFER_DIST = 20.0''')
s=s.replace('''  the paper does not say how MAP's early-lick and photostimulation trials were treated.
''','''  the paper does not say how MAP's early-lick and photostimulation trials were treated. Trials whose
  sample cue does not start 1.85 s before the go cue (the 1.2 s delay of the paper's task) are left
  out too: in the ALM and medulla sessions about 8% of trials have a 1.8 s or 0.3 s delay, which
  would put the sample cue in the baseline window or the delay epoch (an assumption).
''')
open('map_subspace.py','w').write(s)
EOF
grep -n "Trials. \|1.85 s before" map_subspace.py
```

```
22:- Trials. "X moving and X stationary contained data from all correct and error trials" (Methods,
26:  sample cue does not start 1.85 s before the go cue (the 1.2 s delay of the paper's task) are left
31:- Z-scoring: baseline -2.1 to -1.85 s before the go cue (Methods, "Subspace identification"); mean and
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; cat > $TMPDIR/edit5.py <<'PYEOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a[:60]); put(i,s.replace(a,b))
rep(9,'''    smp = s["trials"]["sample"]
    j = np.searchsorted(smp, go) - 1
    sample_rel = np.where(j >= 0, smp[np.maximum(j, 0)] - go, np.nan)
''','''    onset_all = ms.sample_onset(s, gos)
    other_delay = (np.isin(np.array(s["trials"]["outcome"]), ["hit", "miss"]) & (np.array(s["trials"]["photostim_duration"]) == "N/A")
                   & (np.array(s["trials"]["early_lick"]) == "no early") & np.isfinite(gos) & ~(np.abs(onset_all - ms.SAMPLE_ONSET) < 0.02))
    sample_rel = onset_all[keep]
''')
rep(9,'''                           sample_from_go_s=round(float(np.nanmedian(sample_rel)), 3),''','''                           other_delay=int(other_delay.sum()),
                           other_delay_onsets=",".join(f"{x:.2f}" for x, _ in collections.Counter(np.round(onset_all[other_delay], 2)).most_common(2)),
                           sample_from_go_s=round(float(np.nanmedian(sample_rel)), 3),''')
rep(9,'''print("sample cue onset relative to the go cue, kept trials: median per session''','''print("correct and error trials left out for a sample onset other than -1.85 s (other delay): %d to %d per session, %d in all"
      % (checks.other_delay.min(), checks.other_delay.max(), checks.other_delay.sum()))
print("sample cue onset relative to the go cue, kept trials: median per session''')
i=next(k for k,c in enumerate(C) if ''.join(c['source']).startswith('TAGS = ['))
rep(i,'''               r2_mean=round(r.r2, 1),''','''               predictors_per_train_trial=round(9 * r.d_src / r.n_train, 2), r2_mean=round(r.r2, 1),''')
rep(i,'''print("across sessions and directions, Spearman correlation of mean R2 with the source's largest |z|: %.2f"
      % stats.spearmanr(bin_df.r2_mean, bin_df.z_absmax_src).correlation)''','''print("across sessions and directions, Spearman correlation of mean R2 with the source's largest |z|: %.2f, "
      "with the predictors per training trial: %.2f"
      % (stats.spearmanr(bin_df.r2_mean, bin_df.z_absmax_src).correlation,
         stats.spearmanr(bin_df.r2_mean, bin_df.predictors_per_train_trial).correlation))
allr = dec_main[(dec_main["T"] == "T1") & (~dec_main["std"]) & (dec_main.R == "R1")].assign(ppt=lambda d: 9 * d.d_src / d.n_train)
print("all sessions and directions (incl. ALM to ALM), Spearman correlation of mean R2 with predictors per training trial: %.2f; "
      "R2 above 0 in %d of %d, all with predictors per trial below %.2f"
      % (stats.spearmanr(allr.r2, allr.ppt).correlation, (allr.r2 > 0).sum(), len(allr),
         allr[allr.r2 > 0].ppt.max() if (allr.r2 > 0).any() else np.nan))''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit5.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P))
for c in nb['cells']:
    s=''.join(c['source'])
    if '"R2 above 0 in %d of %d, all with predictors per trial below %.2f"' in s:
        s=s.replace('"R2 above 0 in %d of %d, all with predictors per trial below %.2f"','"R2 above 0 in %d of %d, whose largest predictors per trial is %.2f"')
        c['source']=s.splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
sed -n 1,12p reproduce_hasnain_2025.ipynb; git diff --stat
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f00bfdd3",
   "metadata": {},
   "source": [
    "# Hasnain, Han & Economo (2025) on the MAP dataset, DANDI:000363\n",
    "\n",
    "Paper: Hasnain M. A., Han Y. & Economo M. N., \"Mapping neural subspace dynamics onto the structure\n",
    "of the mouse descending motor system\", bioRxiv doi:10.1101/2025.10.17.682917 (preprint version 1).\n",
    "The claims file `claims/hasnain-2025.yaml` was written from the preprint's full text (PMC12632980);\n",
 entries/hasnain-2025/map_subspace.py              | 109 +++++++--
 entries/hasnain-2025/reproduce_hasnain_2025.ipynb | 277 +++++++++++++++++++---
 2 files changed, 331 insertions(+), 55 deletions(-)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/g2.py",
 "content": "# %% [markdown]\n# # Hasnain, Han & Economo (2025) on DANDI:000363: reading G2 of 'good'\n#\n# A second notebook for the same entry. It repeats the tests of the Figure 4 claims on the ALM and\n# medulla sessions under reading G2 of the unit selection, where the main notebook\n# (`reproduce_hasnain_2025.ipynb`) uses reading G1. The paper selects \"sessions with at least 30\n# units classified as 'good' in each region of interest\" (Methods, \"Curation of Mesoscale Activity\n# Map Dataset\"). The units table has two 'good' labels: `classification` (G1) and `unit_quality`\n# (G2). Only units classified good carry a CCF label, so under G2 a unit takes the label of the\n# nearest unit classified good on the same probe, by the CCF coordinates of their electrodes, within\n# 20 um (`map_subspace.transfer_labels`; an assumption). The main notebook gives the session and unit\n# counts under both readings and the check of the label transfer.\n#\n# Dataset: DANDI:000363, version 0.231012.2129, streamed. Claims tested here, under G2:\n# fig4b-medulla-selectivity, fig4c-alm-null-potent-similar, fig4c-medulla-null-smaller,\n# fig4d-decoding-asymmetry and fig4e-medulla-null-lower-dimension. fig4d-alm-predicts-medulla-null\n# and fig4f-medulla-null-not-spanning-alm are tested in the main notebook only (the first needs the\n# bilateral sessions, 31 under G2; the second a UMAP that the main notebook shows to be dominated by\n# session). Methods, readings and seeds are those of the main notebook; the readings run here are the\n# main reading (W1, B1, D1, baseline z-score) and B2, on which fig4c-medulla-null-smaller rests in\n# the main notebook.\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"2\")\nimport collections\nimport resource\nimport time\nimport zlib\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport map_subspace as ms\n\nT0 = time.time()\nKEY = \"hasnain-2025\"\n\n\ndef seed(claim, k=0):\n    return zlib.crc32(f\"{KEY}/{claim}\".encode()) + k\n\n\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\n\n# %% [markdown]\n# ## Data check\n#\n# Units tables of every file, the G2 selection, and for each selected session the trials kept, the\n# movement threshold and the clock checks of the main notebook (tongue latency after the go cue; lick\n# direction decoded from spike counts 0.8 to 1.0 s after the go cue against shuffled labels).\n\n# %%  tags=[\"sanity\"]\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import cross_val_score\n\nassets = ms.asset_urls()\ntables = ms.survey(assets)\nurls = dict(assets)\nbil_g2, alm_med = ms.select_sessions(tables, label=\"quality\")\nprint(\"G2: bilateral sessions %d; ALM and medulla sessions %d from %d mice, %d ALM and %d medulla units\"\n      % (len(bil_g2), len(alm_med), len({p.split(\"/\")[0] for p in alm_med}),\n         sum(len(v[\"ALM\"]) for v in alm_med.values()), sum(len(v[\"medulla\"]) for v in alm_med.values())))\n_, alm_med_g1 = ms.select_sessions(tables)\nprint(\"ALM and medulla sessions also selected under G1:\", sum(p in alm_med_g1 for p in alm_med))\n\nW = ms.WINDOWS[\"W1\"]\nsessions, rows = {}, []\nlabels_seen = collections.defaultdict(collections.Counter)\nrng_check = np.random.default_rng(seed(\"map-session-selection\", 1))\nfor p, regions in alm_med.items():\n    ids = sorted(set(regions[\"ALM\"]) | set(regions[\"medulla\"]))\n    s = ms.load_session(urls[p], ids)\n    for k in (\"outcome\", \"photostim_duration\", \"early_lick\"):\n        labels_seen[k].update(s[\"trials\"][k])\n    gos = ms.go_times(s)\n    keep = ms.trial_mask(s)\n    go = gos[keep]\n    speed = ms.speed_bins(s, go, W)\n    finite = speed[np.isfinite(speed) & (speed > 0)]\n    log_thr = ms.otsu_threshold(np.log10(finite))\n    f = ms.open_file(urls[p])\n    tg = f[\"acquisition/BehavioralTimeSeries/Camera0_side_TongueTracking\"]\n    tts, tlik = tg[\"timestamps\"][:], tg[\"data\"][:, 2]\n    hit = np.array(s[\"trials\"][\"outcome\"])[keep] == \"hit\"\n    lat = []\n    for g in go[hit]:\n        lo, hi = np.searchsorted(tts, [g, g + 1.0])\n        k = np.where(tlik[lo:hi] > 0.9)[0]\n        lat.append(tts[lo + k[0]] - g if len(k) else np.nan)\n    right = np.array(s[\"trials\"][\"trial_instruction\"])[keep] == \"right\"\n    X = np.stack([np.diff(np.searchsorted(s[\"spikes\"][i], np.c_[go + 0.8, go + 1.0]), axis=1)[:, 0] for i in ids], axis=1)\n    clf = LogisticRegression(C=0.1, max_iter=2000)\n    acc = cross_val_score(clf, X, right, cv=5).mean()\n    acc_sh = cross_val_score(clf, X, rng_check.permutation(right), cv=5).mean()\n    sessions[p] = dict(sess=s, keep=keep, go=go, speed=speed, log_thr=log_thr)\n    rows.append(dict(session=p.split(\"/\")[1][:30], G1=p in alm_med_g1, ALM=len(regions[\"ALM\"]),\n                     ALM_side=\"+\".join(regions[\"alm_sides\"]), medulla=len(regions[\"medulla\"]),\n                     trials=len(keep), kept=int(keep.sum()), hits=int(hit.sum()), speed_thr=round(10 ** log_thr, 1),\n                     tongue_lat_ms=round(1000 * np.nanmedian(lat)), acc_go_08=round(acc, 2), acc_shuffled=round(acc_sh, 2)))\n    del f\nsel_df = pd.DataFrame(rows)\nprint(sel_df.to_string())\nprint(\"trial labels:\", {k: dict(v) for k, v in labels_seen.items()})\nprint(\"decoding above shuffled labels in %d of %d sessions; tongue latency %d to %d ms\"\n      % ((sel_df.acc_go_08 > sel_df.acc_shuffled + 0.1).sum(), len(sel_df), sel_df.tongue_lat_ms.min(), sel_df.tongue_lat_ms.max()))\nprint(\"elapsed %.0f s, peak memory %.0f MB\" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n\n# %% [markdown]\n# ## Claim fig4b-medulla-selectivity, reading G2\n#\n# > Medullary reticular nucleus units are selective for lick direction in each epoch, most in the\n# > response epoch (sample 7%, delay 21%, response 49% of 724 units).\n#\n# As in the main notebook (M7): correct trials, equal random samples of right and left trials,\n# AUROC per epoch, 1000 label shuffles, readings E1 and E2, Bonferroni (p < 0.01) and p < 0.05.\n\n# %%  tags=[\"claim:fig4b-medulla-selectivity\"]\ndef selectivity(rng):\n    out = []\n    for p, s in alm_med.items():\n        v = sessions[p]\n        trials = v[\"sess\"][\"trials\"]\n        out_arr = np.array(trials[\"outcome\"])[v[\"keep\"]]\n        instr = np.array(trials[\"trial_instruction\"])[v[\"keep\"]]\n        r_idx = np.where((out_arr == \"hit\") & (instr == \"right\"))[0]\n        l_idx = np.where((out_arr == \"hit\") & (instr == \"left\"))[0]\n        n = min(len(r_idx), len(l_idx))\n        pick = np.r_[rng.choice(r_idx, n, replace=False), rng.choice(l_idx, n, replace=False)]\n        is_right = np.r_[np.ones(n, bool), np.zeros(n, bool)]\n        r = ms.rates([v[\"sess\"][\"spikes\"][i] for i in s[\"medulla\"]], v[\"go\"][pick], ms.WINDOWS[\"W1\"])\n        tax = ms.WINDOWS[\"W1\"][0] + ms.BIN * np.arange(r.shape[1])\n        for j in range(r.shape[2]):\n            row = dict(session=p.split(\"/\")[1][:30], unit=s[\"medulla\"][j], n_per_side=n)\n            for ep, (a, b) in ms.EPOCHS.items():\n                row[ep] = ms.selectivity_p(r[:, (tax >= a) & (tax < b), j].mean(1), is_right, rng)[1]\n            out.append(row)\n    return pd.DataFrame(out)\n\n\ndef summarize_sel(df, alpha):\n    sig = {ep: df[ep] < alpha for ep in ms.EPOCHS}\n    e1 = {\"sample\": sig[\"sample\"], \"delay\": sig[\"early_delay\"] | sig[\"late_delay\"],\n          \"response\": sig[\"early_response\"] | sig[\"late_response\"]}\n    res = {f\"E1 {k}\": 100 * v.mean() for k, v in e1.items()}\n    res.update({f\"E2 {k}\": 100 * v.mean() for k, v in sig.items()})\n    return res\n\n\nsel_runs = {k: selectivity(np.random.default_rng(seed(\"fig4b-medulla-selectivity\", k))) for k in SEED_OFFSETS}\nprint(\"medulla units:\", len(sel_runs[0]))\ntab = pd.DataFrame({(off, a): summarize_sel(df, a) for off, df in sel_runs.items() for a in (0.01, 0.05)}).T\ntab.index.names = [\"seed offset\", \"alpha\"]\nprint(tab.round(1).to_string())\nprint(\"expected: sample 7 +- 0.7, delay 21 +- 2.1, response 49 +- 4.9\")\nprint(\"by session (claim seed, Bonferroni, E1):\")\nprint(sel_runs[0].groupby(\"session\").apply(lambda d: pd.Series(summarize_sel(d, 0.01))).iloc[:, :3].round(1).to_string())\nprint(\"elapsed %.0f s\" % (time.time() - T0))\n\n# %% [markdown]\n# ## Per-region subspaces, reading G2\n#\n# Main reading and B2, the subspace generator seeded as in the main notebook. Then the variance\n# explained (M6, V1 to V3) and the paired t tests of fig4c, and the dimensionality of fig4e.\n\n# %%\ndef prepare(p, region_ids, short_runs_move):\n    v = sessions[p]\n    r = ms.rates([v[\"sess\"][\"spikes\"][i] for i in region_ids], v[\"go\"], W)\n    z, nfb = ms.zscore(r, W)\n    return z, ms.movement_mask(v[\"speed\"], v[\"log_thr\"], short_runs_move=short_runs_move), nfb\n\n\nfits, fit_rows = {}, []\nrng_sub = np.random.default_rng(seed(\"fig4c-alm-null-potent-similar\"))\nfor p, s in alm_med.items():\n    for reg in (\"ALM\", \"medulla\"):\n        for rname in (\"main\", \"B2\"):\n            z, mv, nfb = prepare(p, s[reg], rname == \"B2\")\n            fit = ms.fit_region(z, mv, rng_sub)\n            fit[\"proj\"] = (z @ fit[\"qn\"]).astype(np.float32)\n            fits[(p, reg, rname)] = fit\n            ve = ms.ve_readings(fit)\n            fit_rows.append(dict(session=p.split(\"/\")[1][:30], region=reg, reading=rname, units=z.shape[2],\n                                 d_null=fit[\"d\"][0], d_pot=fit[\"d\"][1], d_null_raw=fit[\"d_raw\"][0],\n                                 moving=round(float((mv == 1).sum() / (mv >= 0).sum()), 2), fallback=nfb,\n                                 z_absmax=round(float(np.abs(z).max())),\n                                 **{f\"{k} {n}\": 100 * x for k, vv in ve.items() for n, x in zip((\"null\", \"pot\"), vv[:2])}))\n    print(p.split(\"/\")[1][:30], \"done, elapsed %.0f s\" % (time.time() - T0))\nfit_df = pd.DataFrame(fit_rows)\nprint(fit_df.round(1).to_string())\nprint(\"peak memory %.0f MB\" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n\n# %% [markdown]\n# ## Claims fig4c-alm-null-potent-similar and fig4c-medulla-null-smaller, reading G2\n#\n# > In MAP ALM the movement-null and movement-potent subspaces explain comparable variance (36.0 +-\n# > 7.40% and 37.1 +- 8.70%; paired t test p = 0.15, 16 sessions).\n#\n# > In the medullary reticular nuclei the movement-null subspace explains less variance than the\n# > movement-potent subspace (26.4 +- 3.90% against 44.8 +- 7.12%; p = 1.9e-9, 16 sessions).\n\n# %%  tags=[\"claim:fig4c-alm-null-potent-similar\", \"claim:fig4c-medulla-null-smaller\"]\nve_rows = []\nfor (rname, reg), d in fit_df.groupby([\"reading\", \"region\"]):\n    for V in (\"V1\", \"V2\", \"V3\"):\n        a, b = d[f\"{V} null\"].values, d[f\"{V} pot\"].values\n        t, pv = stats.ttest_rel(a, b)\n        ve_rows.append(dict(region=reg, reading=rname, V=V, n=len(a), null_mean=a.mean(), null_sd=a.std(ddof=1),\n                            pot_mean=b.mean(), pot_sd=b.std(ddof=1), diff=(a - b).mean(), t=t, p=pv,\n                            null_below_pot=int((a < b).sum())))\nve_tab = pd.DataFrame(ve_rows)\nprint(ve_tab.round(3).to_string())\nprint(\"expected ALM null 36.0 +- 7.4, potent 37.1 +- 8.7 (p = 0.15); medulla null 26.4 +- 3.9, potent 44.8 +- 7.12 (p = 1.9e-9)\")\nalm_ok = ve_tab[(ve_tab.region == \"ALM\") & (abs(ve_tab.null_mean - 36.0) <= 7.4) & (abs(ve_tab.pot_mean - 37.1) <= 8.7)]\nmed_ok = ve_tab[(ve_tab.region == \"medulla\") & (abs(ve_tab.null_mean - 26.4) <= 3.9) & (abs(ve_tab.pot_mean - 44.8) <= 7.12)]\nprint(\"ALM readings with both means in tolerance:\", alm_ok[[\"reading\", \"V\", \"null_mean\", \"pot_mean\", \"p\"]].round(4).values.tolist())\nprint(\"medulla readings with both means in tolerance:\", med_ok[[\"reading\", \"V\", \"null_mean\", \"pot_mean\", \"p\"]].round(4).values.tolist())\n\n# %% [markdown]\n# Seed check: the main reading and B2 again under the claim's seed plus 1000 to 4000.\n\n# %%  tags=[\"claim:fig4c-alm-null-potent-similar\", \"claim:fig4c-medulla-null-smaller\", \"claim:fig4e-medulla-null-lower-dimension\"]\nseed_rows = []\nfor k in SEED_OFFSETS[1:]:\n    rng_k = np.random.default_rng(seed(\"fig4c-alm-null-potent-similar\", k))\n    for p, s in alm_med.items():\n        for reg in (\"ALM\", \"medulla\"):\n            for rname in (\"main\", \"B2\"):\n                z, mv, _ = prepare(p, s[reg], rname == \"B2\")\n                fit = ms.fit_region(z, mv, rng_k)\n                ve = ms.ve_readings(fit)\n                seed_rows.append(dict(offset=k, reading=rname, session=p, region=reg, d_null_raw=fit[\"d_raw\"][0],\n                                      **{f\"{V} {n}\": 100 * x for V, vv in ve.items() for n, x in zip((\"null\", \"pot\"), vv[:2])}))\n    print(\"offset\", k, \"elapsed %.0f s\" % (time.time() - T0))\nseed_df = pd.concat([pd.DataFrame(seed_rows),\n                     fit_df.assign(offset=0, session=[next(p for p in alm_med if r in p) for r in fit_df.session])])\nsrows = []\nfor (off, rname, reg), d in seed_df.groupby([\"offset\", \"reading\", \"region\"]):\n    for V in (\"V1\", \"V2\", \"V3\"):\n        t, pv = stats.ttest_rel(d[f\"{V} null\"], d[f\"{V} pot\"])\n        srows.append(dict(offset=off, reading=rname, region=reg, V=V, null=d[f\"{V} null\"].mean(), pot=d[f\"{V} pot\"].mean(), p=pv))\nprint(pd.DataFrame(srows).round(4).to_string())\nfor (off, rname), d in seed_df.groupby([\"offset\", \"reading\"]):\n    d = d.sort_values(\"session\")\n    a, b = d[d.region == \"ALM\"].d_null_raw.values, d[d.region == \"medulla\"].d_null_raw.values\n    print(f\"offset {off} {rname}: N1 medulla {b.mean():.1f}, ALM {a.mean():.1f}, p = {stats.ttest_rel(b, a).pvalue:.3g}\")\nprint(\"elapsed %.0f s\" % (time.time() - T0))\n\n# %% [markdown]\n# ## Claim fig4e-medulla-null-lower-dimension, reading G2\n#\n# > The movement-null subspace has lower dimensionality in the medullary reticular nuclei than in ALM\n# > (paired t test, p = 7.4e-5).\n#\n# N1 (shuffle dimension of the stationary activity) and N2 (participation ratio of the\n# movement-null covariance), main reading and B2.\n\n# %%  tags=[\"claim:fig4e-medulla-null-lower-dimension\"]\ndim_rows = []\nfor p, s in alm_med.items():\n    for rname in (\"main\", \"B2\"):\n        row = dict(session=p.split(\"/\")[1][:30], reading=rname)\n        for reg in (\"ALM\", \"medulla\"):\n            fit = fits[(p, reg, rname)]\n            row[f\"{reg} units\"] = len(s[reg])\n            row[f\"{reg} N1\"] = fit[\"d_raw\"][0]\n            row[f\"{reg} N2\"] = ms.participation_ratio(fit[\"qn\"].T @ fit[\"C\"] @ fit[\"qn\"])\n        dim_rows.append(row)\ndim_df = pd.DataFrame(dim_rows)\nprint(dim_df.round(2).to_string())\nfor rname, d in dim_df.groupby(\"reading\"):\n    for m in (\"N1\", \"N2\"):\n        t, pv = stats.ttest_rel(d[f\"medulla {m}\"], d[f\"ALM {m}\"])\n        print(f\"{rname} {m}: medulla mean {d[f'medulla {m}'].mean():.2f}, ALM mean {d[f'ALM {m}'].mean():.2f}, t = {t:.2f}, \"\n              f\"p = {pv:.3g}, medulla lower in {(d[f'medulla {m}'] < d[f'ALM {m}']).sum()} of {len(d)}\")\n\n# %% [markdown]\n# ## Claim fig4d-decoding-asymmetry, reading G2\n#\n# > Prediction is asymmetric; ALM movement-null activity is predicted less well from the medulla (21\n# > +- 6.7%) than the medulla from ALM (paired t test p = 1.2e-4, 16 sessions).\n#\n# As in the main notebook (M8): ridge with lambda 0.01, readings T1 and T2, R1 and R2, predictors\n# standardized or not; main-reading subspaces; under the claim's seed and four more.\n\n# %%  tags=[\"claim:fig4d-decoding-asymmetry\"]\nbins = np.arange(int(round((ms.TASK_SPAN[0] - W[0]) / ms.BIN)), int(round((ms.TASK_SPAN[1] - W[0]) / ms.BIN)))\nALL_READ = [(s_, p_) for s_ in (False, True) for p_ in (True, False)]\n\n\ndef decode(rng, readings):\n    out = []\n    for p in alm_med:\n        v = sessions[p]\n        hit = np.array(v[\"sess\"][\"trials\"][\"outcome\"])[v[\"keep\"]] == \"hit\"\n        for T in (\"T1\", \"T2\"):\n            idx = np.arange(len(hit)) if T == \"T1\" else np.where(hit)[0]\n            perm = rng.permutation(idx)\n            ntr = int(round(0.7 * len(perm)))\n            for src, tgt in ((\"ALM\", \"medulla\"), (\"medulla\", \"ALM\")):\n                xs, xt = fits[(p, src, \"main\")][\"proj\"], fits[(p, tgt, \"main\")][\"proj\"]\n                for stdz, pooled in readings:\n                    r2 = ms.ridge_r2(xs, xt, perm[:ntr], perm[ntr:], bins, stdz, pooled)\n                    out.append(dict(session=p, T=T, src=src, std=stdz, R=\"R1\" if pooled else \"R2\", r2=100 * r2.mean(),\n                                    ppt=9 * xs.shape[2] / ntr))\n    return pd.DataFrame(out)\n\n\ndef dec_summary(df):\n    res = []\n    for (T, stdz, R), d in df.groupby([\"T\", \"std\", \"R\"]):\n        am_ = d[d.src == \"ALM\"].set_index(\"session\").r2\n        ma_ = d[d.src == \"medulla\"].set_index(\"session\").r2\n        res.append(dict(T=T, std=stdz, R=R, ALM_to_med=am_.mean(), med_to_ALM=ma_.mean(),\n                        sem=ma_.std(ddof=1) / np.sqrt(len(ma_)), p_asym=stats.ttest_rel(am_, ma_.loc[am_.index]).pvalue,\n                        sessions_above_0=int((ma_ > 0).sum())))\n    return pd.DataFrame(res)\n\n\ndec_runs = {k: decode(np.random.default_rng(seed(\"fig4d-alm-predicts-medulla-null\", k)), ALL_READ if k == 0 else ALL_READ[::2])\n            for k in SEED_OFFSETS}\nprint(dec_summary(dec_runs[0]).round(4).to_string())\nprint(\"expected medulla to ALM 21 +- 6.7, below ALM to medulla (p = 1.2e-4)\")\nfor k in SEED_OFFSETS[1:]:\n    print(\"offset\", k)\n    print(dec_summary(dec_runs[k]).round(4).to_string())\nd0 = dec_runs[0][(dec_runs[0][\"T\"] == \"T1\") & (~dec_runs[0][\"std\"]) & (dec_runs[0].R == \"R1\")]\nprint(\"T1, unstandardized, R1, per session: R2 above 0 in %d of %d; Spearman correlation of R2 with predictors per training trial %.2f\"\n      % ((d0.r2 > 0).sum(), len(d0), stats.spearmanr(d0.r2, d0.ppt).correlation))\nprint(\"elapsed %.0f s, peak memory %.0f MB\" % (time.time() - T0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3))\n"
}
```

```
File created successfully at: /tmp/claude-1001/g2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; sed -e "s#tables = ms.survey(assets)#import pickle; tables = pickle.load(open('$TMPDIR/survey.pkl','rb'))#" -e 's#^_, alm_med_g1 = ms.select_sessions(tables)#alm_med = {k: alm_med[k] for k in list(alm_med)[:3]}\n_, alm_med_g1 = ms.select_sessions(tables)#' -e 's#SEED_OFFSETS = \[0, 1000, 2000, 3000, 4000\]#SEED_OFFSETS = [0, 1000]#' $TMPDIR/g2.py > $TMPDIR/g2dev.py; echo "import matplotlib; matplotlib.use('Agg')" | cat - $TMPDIR/g2dev.py > $TMPDIR/g2dev2.py; PYTHONPATH=. /usr/bin/time -v ../../executed/hasnain-2025/.venv/bin/python $TMPDIR/g2dev2.py > $TMPDIR/g2.log 2> $TMPDIR/g2.err; grep -B2 -A10 Traceback $TMPDIR/g2.err | head; grep -E "Maximum resident|Elapsed" $TMPDIR/g2.err; cut -c1-250 $TMPDIR/g2.log
```

```
Elapsed (wall clock) time (h:mm:ss or m:ss): 4:37.68
	Maximum resident set size (kbytes): 1612828
G2: bilateral sessions 31; ALM and medulla sessions 19 from 7 mice, 1501 ALM and 1745 medulla units
ALM and medulla sessions also selected under G1: 0
                          session     G1  ALM  ALM_side  medulla  trials  kept  hits  speed_thr  tongue_lat_ms  acc_go_08  acc_shuffled
0  sub-456773_ses-20191002T143533  False   50  left ALM      167     581   334   293       25.6             98       0.84          0.46
1  sub-456773_ses-20191004T143720  False   34  left ALM      215     491   284   243       27.0             85       0.87          0.45
2  sub-456774_ses-20191021T142044  False   58  left ALM       59     440   208   167       26.4            113       0.83          0.47
trial labels: {'outcome': {'hit': 1169, 'miss': 222, 'ignore': 121}, 'photostim_duration': {'N/A': 1210, '0.5000': 302}, 'early_lick': {'early': 194, 'no early': 1318}}
decoding above shuffled labels in 3 of 3 sessions; tongue latency 85 to 113 ms
elapsed 46 s, peak memory 1232 MB
medulla units: 441
                   E1 sample  E1 delay  E1 response  E2 sample  E2 early_delay  E2 late_delay  E2 early_response  E2 late_response
seed offset alpha                                                                                                                 
0           0.01        12.7      22.9         50.1       12.7            16.1           15.0               39.0              32.4
            0.05        20.0      32.7         60.8       20.0            24.3           21.5               46.9              42.0
1000        0.01        11.8      22.9         51.5       11.8            15.9           14.7               39.7              34.5
            0.05        20.2      33.8         60.8       20.2            23.8           23.6               47.6              42.2
expected: sample 7 +- 0.7, delay 21 +- 2.1, response 49 +- 4.9
by session (claim seed, Bonferroni, E1):
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
s=open('map_subspace.py').read()
a='''    xs = x.copy()
    for s in range(n_shuffle):
        for j in range(x.shape[1]):
            xs[:, j] = x[rng.permutation(len(x)), j]
        null[s] = eig_desc(cov(xs))'''
assert a in s
s=s.replace(a,'''    for s in range(n_shuffle):
        null[s] = eig_desc(cov(rng.permuted(x, axis=0)))''')
open('map_subspace.py','w').write(s)
EOF
cat > $TMPDIR/tfit.py <<'EOF'
import numpy as np, time, map_subspace as ms
rng=np.random.default_rng(0)
x=rng.standard_normal((300*730,215)).astype(np.float32)
x[:, :5] += rng.standard_normal((300*730,1)).astype(np.float32)*3
t=time.time(); d,_=ms.shuffle_dimension(x,rng); print("dim",d,"time",time.time()-t)
EOF
OMP_NUM_THREADS=2 PYTHONPATH=. ../../executed/hasnain-2025/.venv/bin/python $TMPDIR/tfit.py
```

```
dim 1 time 16.565292835235596
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import os
p=os.environ['TMPDIR']+'/g2.py'
s=open(p).read()
s=s.replace('''# Seed check: the main reading and B2 again under the claim's seed plus 1000 to 4000.''','''# Seed check: the main reading again under the claim's seed plus 1000 to 4000 (dimension shuffles and
# the optimizer's start). B2 is run under the claim's seed only, to keep the notebook within the time
# limit; in the main notebook B2 moved the t test p by less than 0.004 over the five seeds.''')
s=s.replace('''            for rname in ("main", "B2"):
                z, mv, _ = prepare(p, s[reg], rname == "B2")
                fit = ms.fit_region(z, mv, rng_k)''','''            for rname in ("main",):
                z, mv, _ = prepare(p, s[reg], rname == "B2")
                fit = ms.fit_region(z, mv, rng_k)''')
open(p,'w').write(s)
# convert to ipynb
import json, uuid, re
cells=[]
for chunk in re.split(r'^# %%', s, flags=re.M)[1:]:
    head, _, body = chunk.partition('\n')
    tags=re.findall(r'"([^"]+)"', head.split('tags=')[1]) if 'tags=' in head else []
    if head.strip().startswith('[markdown]'):
        src='\n'.join(l[2:] if l.startswith('# ') else l[1:] if l.startswith('#') else l for l in body.strip('\n').split('\n'))
        c={"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":src.splitlines(True)}
    else:
        c={"cell_type":"code","execution_count":None,"id":uuid.uuid4().hex[:8],"metadata":{"tags":tags} if tags else {},"outputs":[],"source":body.strip('\n').splitlines(True)}
    cells.append(c)
main=json.load(open('reproduce_hasnain_2025.ipynb'))
nb={"cells":cells,"metadata":main["metadata"],"nbformat":4,"nbformat_minor":5}
json.dump(nb,open('reproduce_hasnain_2025_g2.ipynb','w'),indent=1,ensure_ascii=False); open('reproduce_hasnain_2025_g2.ipynb','a').write('\n')
# ids for main notebook new cells
for c in main['cells']:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
json.dump(main,open('reproduce_hasnain_2025.ipynb','w'),indent=1,ensure_ascii=False); open('reproduce_hasnain_2025.ipynb','a').write('\n')
print(len(cells), main['nbformat'], main['nbformat_minor'])
EOF
python -c "
import json;nb=json.load(open('reproduce_hasnain_2025_g2.ipynb'))
for c in nb['cells']: print(c['cell_type'], c['metadata'], ''.join(c['source'])[:80].replace(chr(10),' | '))"
```

```
16 4 5
markdown {} # Hasnain, Han & Economo (2025) on DANDI:000363: reading G2 of 'good' |  | A second 
code {} import os | os.environ.setdefault("OMP_NUM_THREADS", "2") | import collections | impor
markdown {} ## Data check |  | Units tables of every file, the G2 selection, and for each select
code {'tags': ['sanity']} from sklearn.linear_model import LogisticRegression | from sklearn.model_selection
markdown {} ## Claim fig4b-medulla-selectivity, reading G2 |  | > Medullary reticular nucleus un
code {'tags': ['claim:fig4b-medulla-selectivity']} def selectivity(rng): |     out = [] |     for p, s in alm_med.items(): |         v = 
markdown {} ## Per-region subspaces, reading G2 |  | Main reading and B2, the subspace generator
code {} def prepare(p, region_ids, short_runs_move): |     v = sessions[p] |     r = ms.rate
markdown {} ## Claims fig4c-alm-null-potent-similar and fig4c-medulla-null-smaller, reading 
code {'tags': ['claim:fig4c-alm-null-potent-similar', 'claim:fig4c-medulla-null-smaller']} ve_rows = [] | for (rname, reg), d in fit_df.groupby(["reading", "region"]): |     f
markdown {} Seed check: the main reading again under the claim's seed plus 1000 to 4000 (dim
code {'tags': ['claim:fig4c-alm-null-potent-similar', 'claim:fig4c-medulla-null-smaller', 'claim:fig4e-medulla-null-lower-dimension']} seed_rows = [] | for k in SEED_OFFSETS[1:]: |     rng_k = np.random.default_rng(seed
markdown {} ## Claim fig4e-medulla-null-lower-dimension, reading G2 |  | > The movement-null sub
code {'tags': ['claim:fig4e-medulla-null-lower-dimension']} dim_rows = [] | for p, s in alm_med.items(): |     for rname in ("main", "B2"): |     
markdown {} ## Claim fig4d-decoding-asymmetry, reading G2 |  | > Prediction is asymmetric; ALM m
code {'tags': ['claim:fig4d-decoding-asymmetry']} bins = np.arange(int(round((ms.TASK_SPAN[0] - W[0]) / ms.BIN)), int(round((ms.TA
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/hasnain-2025/entry.yaml'
s=open(p).read()
s=s.replace('''  runtime_minutes: 35
''','''  runtime_minutes: 40
- path: reproduce_hasnain_2025_g2.ipynb
  title: The Figure 4 tests on the ALM and medulla sessions under the unit_quality reading of 'good'
  runtime_minutes: 45
''')
open(p,'w').write(s)
EOF
python tools/entry.py check entries/hasnain-2025 2>&1 | tail -15; date -u
```

```
0 error(s)
Sun Nov 22 05:48:11 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python $TMPDIR/mkdev.py reproduce_hasnain_2025.ipynb $TMPDIR/dev.py $TMPDIR/survey.pkl; PYTHONPATH=. ../../executed/hasnain-2025/.venv/bin/python $TMPDIR/dev.py > $TMPDIR/dev.log 2> $TMPDIR/dev.err; grep -B2 -A10 Traceback $TMPDIR/dev.err | head -20; cut -c1-250 $TMPDIR/dev.log | grep -A8 "cell 9$" ; grep -A3 "trials kept\|other delay\|predictors per" $TMPDIR/dev.log | cut -c1-300; grep -A6 "z_absmax_src" $TMPDIR/dev.log | cut -c1-200
```

```
##### cell 9
                          session  trials  kept  hits  right  go_in_trial  speed_thr  tongue_lat_ms  tongue_pre_go  lick_lat_ms  other_delay other_delay_onsets  sample_from_go_s  sample_min  sample_max  acc -2.0  acc -2.0 shuffled  acc -1.0  acc -1.0
0  sub-456774_ses-20191022T133136     570   135   111     72          570       24.5            262          0.003          399           14        -2.45,-0.95             -1.85       -1.85       -1.85      0.63               0.40      0.81          
1  sub-460436_ses-20200109T111437     517   294   255    111          517       30.0            119          0.048          321           19        -0.95,-2.45             -1.85       -1.85       -1.85      0.69               0.55      0.69          
2  sub-440956_ses-20190208T133600     480   334   312    156          480       35.0             90          0.000          200            0                                -1.85       -1.85       -1.85      0.48               0.55      0.51          
3  sub-440956_ses-20190207T120657     368   225   121    128          368       27.8            105          0.000          246            0                                -1.85       -1.85       -1.85      0.55               0.48      0.62          
trials kept per session: 135 to 334
trial labels over the selected sessions: {'outcome': {'ignore': 499, 'hit': 1143, 'miss': 293}, 'photostim_duration': {'N/A': 1517, '0.5000': 418}, 'early_lick': {'no early': 1808, 'early': 127}, 'trial_instruction': {'right': 1058, 'left': 877}}
correct and error trials left out for a sample onset other than -1.85 s (other delay): 0 to 19 per session, 33 in all
trials kept per session: 135 to 334
trial labels over the selected sessions: {'outcome': {'ignore': 499, 'hit': 1143, 'miss': 293}, 'photostim_duration': {'N/A': 1517, '0.5000': 418}, 'early_lick': {'no early': 1808, 'early': 127}, 'trial_instruction': {'right': 1058, 'left': 877}}
correct and error trials left out for a sample o
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P))
c=nb['cells'][9]; s=''.join(c['source'])
a='''print("sample cue onset relative to the go cue, kept trials: median per session %.3f to %.3f s, over all trials %.3f to %.3f s"
      % (checks.sample_from_go_s.min(), checks.sample_from_go_s.max(), checks.sample_min.min(), checks.sample_max.max()))
print("baseline window", ms.BASELINE, "s: ends before the earliest sample onset:", ms.BASELINE[1] < checks.sample_min.min())'''
assert a in s
s=s.replace(a,'''print("sample cue onset relative to the go cue in the kept trials: %.3f to %.3f s"
      % (checks.sample_min.min(), checks.sample_max.max()))
print("baseline window", ms.BASELINE, "s: ends no later than the earliest sample onset of a kept trial:",
      ms.BASELINE[1] <= checks.sample_min.min() + 1e-9)''')
c['source']=s.splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
cd  python tools/entry.py check entries/hasnain-2025 2>&1 | tail -3; python tools/entry.py --help 2>&1 | head -20
```

```
0 error(s)
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "max-minutes\|max_minutes\|timeout" tools/entry.py | head -20
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
524:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
627:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
634:        if ok and seconds > max_minutes * 60:
636:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
702:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
703:    parser.add_argument("--max-minutes", type=float, default=60,
744:                              args.timeout, args.max_minutes)
754:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/hasnain-2025 > $TMPDIR/run.log 2>&1; echo exit $?; tail -20 $TMPDIR/run.log; date -u
```

```
Sun Nov 22 05:52:59 UTC 2026
exit 0
Installed kernelspec registry-hasnain-2025 in executed/hasnain-2025/.venv/share/jupyter/kernels/registry-hasnain-2025
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (1641 s)
pass  reproduce_hasnain_2025_g2.ipynb  (2049 s)
Sun Nov 22 06:54:42 UTC 2026
```

**Agent**

Both notebooks ran (27 and 34 minutes). Reading the outputs now.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    print('=== cell',i)
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t)
        if 'Warning' in t or 'warn(' in t: continue
        print(t[:9000])
EOF
python $TMPDIR/dump.py executed/hasnain-2025/reproduce_hasnain_2025.ipynb > $TMPDIR/o1.txt; python $TMPDIR/dump.py executed/hasnain-2025/reproduce_hasnain_2025_g2.ipynb > $TMPDIR/o2.txt; wc -l $TMPDIR/o1.txt $TMPDIR/o2.txt; cut -c1-260 $TMPDIR/o1.txt | awk '/=== cell 9/,/=== cell 15/' | grep -v "^ *[0-9]* *bilateral ALM"
```

```
597 /tmp/claude-1001/o1.txt
  315 /tmp/claude-1001/o2.txt
  912 total
=== cell 9
                           session  trials  kept  hits  right  go_in_trial  speed_thr  tongue_lat_ms  tongue_pre_go  lick_lat_ms  other_delay other_delay_onsets  sample_from_go_s  sample_min  sample_max  acc -2.0  acc -2.0 shuffled  acc -1.0  acc -1.0 shuffled
0   sub-456774_ses-20191022T133136     570   135   111     72          570       24.5            262          0.003          399           14        -2.45,-0.95             -1.85       -1.85       -1.85      0.63               0.40      0.81               0.50
1   sub-460436_ses-20200109T111437     517   294   255    111          517       30.0            119          0.048          321           19        -0.95,-2.45             -1.85       -1.85       -1.85      0.69               0.55      0.69               0.60
2   sub-460436_ses-20200110T142717     500   307   280    147          500       32.3            114          0.011          451           38        -2.45,-0.95             -1.85       -1.85       -1.85      0.56               0.49      0.73               0.53
3   sub-484676_ses-20210419T130102     600   335   296    169          600       46.9             56          0.181          318           47        -0.95,-2.45             -1.85       -1.85       -1.85      0.50               0.50      0.73               0.47
4   sub-484677_ses-20210418T132006     720   420   355    266          720       32.2            126          0.020          421           56        -2.45,-0.95             -1.85       -1.85       -1.85      0.62               0.57      0.86               0.58
5   sub-440956_ses-20190208T133600     480   334   312    156          480       35.0             90          0.000          200            0                                -1.85       -1.85       -1.85      0.48               0.53      0.51               0.51
6   sub-440956_ses-20190207T120657     368   225   121    128          368       27.8       
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-240 $TMPDIR/o1.txt | awk '/=== cell 15/,/=== cell 25/' | grep -v " W2 \| D2 "
```

```
=== cell 15
sub-456774_ses-20191022T133136 done, elapsed 515 s

sub-460436_ses-20200109T111437 done, elapsed 560 s

sub-460436_ses-20200110T142717 done, elapsed 595 s

sub-484676_ses-20210419T130102 done, elapsed 623 s

sub-484677_ses-20210418T132006 done, elapsed 666 s
                           session   region reading  units  d_null  d_pot  d_null_raw  d_pot_raw  moving  fallback  z_absmax  V1 null  V1 pot  V1 both  V2 null  V2 pot  V2 both  V3 null  V3 pot  V3 both
0   sub-456774_ses-20191022T133136      ALM    main     85       9      8           9          8     0.3         0      64.7     60.2    70.0     97.7     24.4    27.1     51.5     89.8    84.4      NaN
2   sub-456774_ses-20191022T133136      ALM      B2     85       9      9           9          9     0.4         0      64.7     55.3    73.8     97.0     22.4    29.9     52.4     91.7    83.4      NaN
4   sub-456774_ses-20191022T133136      ALM    Zall     85      14     11          14         11     0.3         0      33.5     67.4    72.9     97.0     24.3    23.4     47.7     92.1    91.5      NaN
5   sub-456774_ses-20191022T133136  medulla    main    128      13      6          13          6     0.3         1     203.1     35.1    76.0     97.8     27.6    53.1     80.6     71.2    88.3      NaN
7   sub-456774_ses-20191022T133136  medulla      B2    128      16      7          16          7     0.4         1     203.1     26.4    84.0     96.7     21.3    60.3     81.6     85.1    91.5      NaN
9   sub-456774_ses-20191022T133136  medulla    Zall    128      12     16          12         16     0.3         0      29.8     55.2    65.5     98.7     27.7    35.6     63.3     89.2    83.4      NaN
10  sub-460436_ses-20200109T111437      ALM    main     81       6      5           6          5     0.5         1     115.1     49.4    78.6     97.3     18.9    28.0     47.0     74.2    85.3      NaN
12  sub-460436_ses-20200109T111437      ALM      B2     81       6      5           6          5     0.6 
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cut -c1-250 $TMPDIR/o1.txt | awk '/=== cell 25/,/=== cell 34/' | grep -v "^ *[0-9]* *ALM-ALM" | grep -v "^$"
```

```
=== cell 25
                          session  ALM units  ALM N1  ALM N2  ALM N2 per unit  medulla units  medulla N1  medulla N2  medulla N2 per unit
0  sub-456774_ses-20191022T133136         85       9    5.06             0.06            128          13        2.90                 0.02
1  sub-460436_ses-20200109T111437         81       6    3.48             0.04             65           1        1.00                 0.02
2  sub-460436_ses-20200110T142717         48       8    6.13             0.13             60           4        2.66                 0.04
3  sub-484676_ses-20210419T130102         46       5    2.87             0.06             31           6        4.29                 0.14
4  sub-484677_ses-20210418T132006         40      10    8.80             0.22             56          11        5.30                 0.09
N1: medulla mean 7.00, ALM mean 7.60, t = -0.35, p = 0.741, medulla lower in 2 of 5
N2: medulla mean 3.23, ALM mean 5.27, t = -2.26, p = 0.0868, medulla lower in 4 of 5
N2 per unit: medulla mean 0.06, ALM mean 0.10, t = -1.17, p = 0.307, medulla lower in 4 of 5
seed offset 0: N1 medulla 7.0, ALM 7.6, p = 0.741
seed offset 1000: N1 medulla 7.0, ALM 7.6, p = 0.741
seed offset 2000: N1 medulla 7.0, ALM 7.8, p = 0.68
seed offset 3000: N1 medulla 7.0, ALM 7.8, p = 0.68
seed offset 4000: N1 medulla 7.0, ALM 7.6, p = 0.741
reading main: N1 medulla 7.0, ALM 7.6, p = 0.741
reading W2: N1 medulla 6.2, ALM 6.4, p = 0.914
reading B2: N1 medulla 10.0, ALM 8.2, p = 0.393
reading D2: N1 medulla 7.0, ALM 7.6, p = 0.741
reading Zall: N1 medulla 10.2, ALM 14.4, p = 0.0424
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
grep "^without" $TMPDIR/o1.txt; cut -c1-250 $TMPDIR/o2.txt | grep -v "^$"
```

```
without ['sub-460436_ses-20200109T111437'] (claim seed plus 1): ALM units with no medulla neighbour 21.0% (within-session shuffle 0.1%), medulla units with an ALM neighbour 66.5% (within-session shuffle 99.7%); grid cells with ALM 57, of which without medulla 16; medulla cells outside ALM cells 26 of 67
=== cell 1
=== cell 3
G2: bilateral sessions 31; ALM and medulla sessions 19 from 7 mice, 1501 ALM and 1745 medulla units
ALM and medulla sessions also selected under G1: 5
                           session     G1  ALM   ALM_side  medulla  trials  kept  hits  speed_thr  tongue_lat_ms  acc_go_08  acc_shuffled
0   sub-456773_ses-20191002T143533  False   50   left ALM      167     581   334   293       25.6             98       0.84          0.46
1   sub-456773_ses-20191004T143720  False   34   left ALM      215     491   284   243       27.0             85       0.87          0.45
2   sub-456774_ses-20191021T142044  False   58   left ALM       59     440   208   167       26.4            113       0.83          0.47
3   sub-456773_ses-20191005T142316  False   40   left ALM       96     700   425   376       30.2             77       0.83          0.51
4   sub-456774_ses-20191023T142402  False   30  right ALM      168     530   208   195       23.6            148       0.95          0.59
5   sub-456774_ses-20191022T133136   True  109   left ALM      298     570   135   111       24.5            262       0.85          0.50
6   sub-460432_ses-20191218T111453  False   73   left ALM       30     520   286   192       23.3            105       0.79          0.55
7   sub-460432_ses-20191219T134919  False   56  right ALM       30     450   233   164       22.7            140       0.86          0.54
8   sub-460434_ses-20191112T114755  False  219   left ALM       39     480   161   135       26.0            183       0.76          0.49
9   sub-460434_ses-20191113T135640  False  186   left ALM       42     423   186   148       27.1            100       0.84          0.58
10  
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 560,600p tools/entry.py; grep -n "def stamp_inputs\|def entry_inputs\|README" tools/entry.py | head; awk '/untracked/,/=== cell 17/' $TMPDIR/o1.txt | head -12; date -u
```

```
import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
grep -A11 "reading  untracked" $TMPDIR/o1.txt; grep -B3 -A12 "W2 \|D2 " $TMPDIR/o1.txt | grep -E "ALM +(W2|D2) +V|medulla +(W2|D2) +V"
```

```
6       ALM      D2  V1  5     51.301   16.603    79.575  12.060 -28.274 -2.272  0.086  98.553
7       ALM      D2  V2  5     23.240    5.430    36.874  12.881 -13.635 -1.937  0.125  60.114
8       ALM      D2  V3  5     70.519   18.143    87.729   7.780 -17.209 -1.558  0.194     NaN
12      ALM      W2  V1  5     53.792   17.694    76.893  12.675 -23.102 -1.731  0.158  99.081
13      ALM      W2  V2  5     22.904    5.982    36.327  14.792 -13.422 -1.744  0.156  59.231
14      ALM      W2  V3  5     71.504   20.043    85.238   8.533 -13.734 -1.122  0.325     NaN
9   medulla      D2  V1  5     53.888   12.771    67.411  11.844 -13.523 -1.311  0.260  98.682
10  medulla      D2  V2  5     34.241    5.178    41.604  11.407  -7.362 -1.184  0.302  75.845
11  medulla      D2  V3  5     70.349    5.926    76.791  14.701  -6.441 -0.838  0.449     NaN
15  medulla      W2  V1  5     60.895   19.902    61.332  17.370  -0.437 -0.027  0.980  99.082
16  medulla      W2  V2  5     35.970    6.307    39.777  14.320  -3.806 -0.434  0.687  75.747
17  medulla      W2  V3  5     77.322    8.047    70.543  19.872   6.779  0.552  0.611     NaN
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/hasnain-2025/reproduce_hasnain_2025.ipynb'))
t=''.join(o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']) for o in nb['cells'][15]['outputs'])
i=t.find('peak memory'); print(t[i:])"
```

```
peak memory 3241 MB
                          session reading  untracked  baseline  sample  delay  response
0  sub-456774_ses-20191022T133136      B1      0.000     0.010   0.041  0.020     0.771
1  sub-456774_ses-20191022T133136      B2      0.000     0.038   0.170  0.043     0.850
2  sub-460436_ses-20200109T111437      B1      0.000     0.083   0.151  0.341     0.815
3  sub-460436_ses-20200109T111437      B2      0.000     0.201   0.335  0.547     0.938
4  sub-460436_ses-20200110T142717      B1      0.000     0.065   0.179  0.441     0.813
5  sub-460436_ses-20200110T142717      B2      0.000     0.223   0.427  0.736     0.946
6  sub-484676_ses-20210419T130102      B1      0.001     0.247   0.405  0.579     0.509
7  sub-484676_ses-20210419T130102      B2      0.001     0.440   0.707  0.780     0.832
8  sub-484677_ses-20210418T132006      B1      0.000     0.117   0.192  0.175     0.578
9  sub-484677_ses-20210418T132006      B2      0.000     0.266   0.402  0.378     0.781
```

**Agent calls Bash**

```bash
grep -E "Spearman|R2 above|below -500|largest" $TMPDIR/o1.txt
```

```
largest |z| over regions: baseline z-score 37 to 278; example.m z-score (bilateral) 24 to 124
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/hasnain-2025/reproduce_hasnain_2025.ipynb'))
for o in nb['cells'][33]['outputs']:
    t=o.get('text','');t=t if isinstance(t,str) else ''.join(t)
    for l in t.splitlines():
        if 'Spearman' in l or 'below -500' in l or 'R2 above' in l or 'ALM-ALM' in l: print(l[:230])
"
```

```
10      ALM-ALM  sub-440956_ses-20190208T133600  right ALM           278                        0.23 -53319.6   -15347.8               0.99   -1699576   -13570.0       4.203  -33440.4      8.995     -85122.7        27.739
11      ALM-ALM  sub-440956_ses-20190208T133600   left ALM           261                        0.31 -59247.5   -17699.4               1.00   -1133416   -88915.3       2.787  -91135.7      3.012     -21869.8        90.168
12      ALM-ALM  sub-440956_ses-20190207T120657  right ALM            50                        0.34   -199.4      -94.8               0.48      -3458     -252.9       5.842    -185.9      3.689       -188.8        71.688
13      ALM-ALM  sub-440956_ses-20190207T120657   left ALM           127                        0.06    -19.2      -10.4               0.03       -320      -26.6       2.219     -41.3      1.679          1.5         1.679
14      ALM-ALM  sub-440958_ses-20190217T154414  right ALM            37                        0.32    -93.3      -74.4               0.29       -787      -76.0       4.761     -88.8     10.344       -103.9         2.039
15      ALM-ALM  sub-440958_ses-20190217T154414   left ALM            45                        0.03     -3.2       -3.1               0.00        -15       -3.6       1.359      -3.1      1.456         -3.1         1.386
16      ALM-ALM  sub-440957_ses-20190211T143614  right ALM           175                        0.15     -2.1       -2.8               0.00        -69      -19.2       2.861       6.7      4.048         -2.3         8.482
17      ALM-ALM  sub-440957_ses-20190211T143614   left ALM           112                        0.30  -2117.9      -51.8               0.42     -61323    -1151.7       2.493    -331.2      6.716      -3933.7        14.535
18      ALM-ALM  sub-440957_ses-20190212T153751  right ALM           141                        0.24   -255.0     -141.2               0.59      -3185     -223.6       5.113    -198.3      6.527       -312.9         5.697
19
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a[:60]); put(i,s.replace(a,b))
rep(0,'''The methods are those of the claims file''','''A second notebook, `reproduce_hasnain_2025_g2.ipynb`, repeats the tests on the ALM and medulla
sessions under reading G2 of the unit selection (`unit_quality` good, CCF labels transferred from
the nearest unit classified good); this notebook uses G1 (`classification` good) throughout.

The methods are those of the claims file''')
put(6,'''### Selection (M1, M2)

Reading G1: units classified 'good' (`classification`), with a CCF label of MOs on a probe described
as targeting ALM, or a label of IRN, GRN or PARN. `anno_name` is filled only for units classified
good. The electrodes table gives the CCF coordinates (x, y, z) of each electrode, so the other
readings (G2, `unit_quality` good; U2, all units) are formed by giving each unit the label of the
nearest unit classified good on the same probe, within 20 um (an assumption; the cell of
map-session-selection checks it and gives the counts).
''')
rep(8,'''For each selected session: the trials kept (hit or miss, no photostimulation, no early lick), the''','''For each selected session: the trials kept (hit or miss, no photostimulation, no early lick, and a
sample cue 1.85 s before the go cue, the paper's 1.2 s delay; the trial labels and the trials left
out for another delay are printed), the''')
put(13,'''**Result: not reproduced.** With the dataset's CCF labels and units classified good (G1), the
paper's rule gives 17 bilateral ALM sessions from 9 mice (paper 20 from 10) and 5 ALM and medulla
sessions from 4 mice (paper 16, or 11 from 7). The left ALM count (1001) is within tolerance of 1055;
the right ALM count (858 against 961), the ALM count of the ALM and medulla sessions (300 against 604)
and the medulla count (340 against 724) are not. Among units classified good, the nearest other such
unit on the probe carries the same CCF label for 97.3%, so the other readings were formed by that
transfer. With `unit_quality` good (G2, within 20 um) the rule gives 31 bilateral sessions from 12
mice (2767 and 2830 units) and 19 ALM and medulla sessions from 7 mice (1501 ALM and 1745 medulla
units); within 0 um 28 and 13 sessions, within 40 um 35 and 22; with all units (U2) 44 and 28. No
reading gives the session counts together with the unit counts. G1 stays the main reading: its
bilateral unit counts are near the paper's, where G2's are 2.7 to 2.9 times them, and "classified as
'good'" names the `classification` column. With a threshold of 20 good units the G1 ALM and medulla
sessions number 14, with 25 they number 9.
''')
put(18,'''**Result: partially reproduced.** Of 340 medulla units (G1), under E1 with the Bonferroni threshold
32.4% are selective in the sample epoch, 49.1% in the delay epoch and 85.9% in the response epoch
(paper 7, 21 and 49%). Under E1 the order holds (response highest, sample lowest) for every seed and
both thresholds; under E2 the early delay sub-epoch (30.3%) falls below the sample epoch (32.4%). No
reading brings a value within tolerance: the E2 sub-epochs give 30.3 to 66.8%, and the uncorrected
threshold higher values. Over the five seeds the E1 Bonferroni values range from 30.9 to 32.9%
(sample), 47.9 to 51.5% (delay) and 85.0 to 85.9% (response). By session the sample value runs from
1.7 to 54.8%. The share of right trials changes over the session (0.13 to 0.73 by fifth in one
session), but slow drift does not explain the high values: with labels shuffled only within blocks of
30 trials they are 30.3, 47.9 and 85.9%. Under reading G2 (second notebook, 1745 units) they are
16.7, 28.3 and 63.4%, also outside tolerance, with the same order. The units differ from the paper's
(340 where the paper has 724).
''')
put(23,'''**Result (fig4c-alm-null-potent-similar): partially reproduced, resting on reading G1.** Over the
5 ALM and medulla sessions, the paired t test finds no difference between null and potent variance in
ALM under the main reading (V1 51.3 against 79.6%, p = 0.086; V2 23.2 against 36.9%, p = 0.125; V3
70.5 against 87.7%, p = 0.194), nor under W2 or D2, but no reading of M3 to M6 puts both means within
tolerance of 36.0 and 37.1%. Under B2 the test finds potent above null (V1 p = 0.040, V2 p = 0.029),
with means out of tolerance. The z-score of example.m, a variant in the claims file, puts both V2
means within tolerance (30.2 against 29.0%), and there the test finds a difference (p = 0.028). With 5
sessions the test has little power: the main-reading V1 difference is 28.3 points. Over the five
seeds the main-reading V1 p ranges from 0.079 to 0.086, and the B2 V1 p is 0.040. Under reading G2
(second notebook, 19 sessions) the main reading with V2 gives 33.9 against 42.7%, p = 0.251 (0.249 to
0.261 over the seeds), which the criterion counts as reproduced; the outcome here rests on G1.

**Result (fig4c-medulla-null-smaller): reproduced under the claim's seed, resting on readings G1, B2
and V2, and sensitive to the seed.** Under B2 (supra-threshold runs shorter than 100 ms counted as
moving) with V2, the medulla null subspace explains 28.4% and the potent subspace 51.9% (tolerances
26.4 +- 3.9 and 44.8 +- 7.12, so at most 51.92), paired t p = 0.017. Over the five seeds the null mean
is 27.9 to 28.8%, the potent mean 51.0 to 52.3% and p 0.017 to 0.024; under two of them the potent
mean (52.3%) is just outside tolerance, which makes the claim partially reproduced there. Under the
main reading B1 the difference is not significant (V1 54.4 against 67.1%, p = 0.312; V2 34.5 against
41.4%, p = 0.344), nor under W2 or D2; under the example.m z-score V2 gives p = 0.042 with the null
mean (31.5%) outside tolerance. B2 also makes the ALM difference significant, so no single reading
reproduces both Figure 4c claims. Under reading G2 (19 sessions) null is below potent under the main
reading (V2 35.7 against 51.7%, p = 0.027; V1 p = 0.020; V1 and V2 p 0.008 to 0.027 over the seeds)
and under B2 (V2 30.8 against 56.4%, p = 0.005), with the null mean outside tolerance in each, which
the criterion counts as partially reproduced.
''')
put(26,'''**Result: not reproduced, resting on reading G1.** In the 5 G1 sessions the medulla's
movement-null dimensionality is not lower than ALM's under either reading. N1 (shuffle dimension):
medulla 7.0, ALM 7.6, p = 0.741, lower in 2 of 5 sessions, and p = 0.68 to 0.741 over the five seeds;
W2, B2 and D2 give p = 0.39 to 0.91 (under B2 the medulla is higher, 10.0 against 8.2). N2
(participation ratio): medulla 3.23, ALM 5.27, p = 0.087, lower in 4 of 5; divided by the unit count,
p = 0.31. The example.m z-score, a variant, gives N1 medulla 10.2 against ALM 14.4, p = 0.042. Under
reading G2 (second notebook, 19 sessions) N1 does not differ (p = 0.98), but N2 is lower in the
medulla (3.35 against 5.93, p = 0.027, lower in 14 of 19), which the criterion counts as reproduced;
there the medulla N2 is below 1.4 in 5 sessions, each with a unit whose |z| exceeds 3000. The medulla
has fewer units than ALM in 2 of the 5 G1 sessions.
''')
rep(27,'''Main reading only (W1, B1, D1, baseline z-score); each hemisphere's subspaces from its own units.''','''Main reading (W1, B1, D1, baseline z-score) and the example.m z-score, for the decoding variants;
each hemisphere's subspaces from its own units.''')
assert src(36).startswith('**Result (fig4d-alm')
put(36,'''**Result (fig4d-alm-predicts-medulla-null): not reproduced.** With lambda = 0.01 the decoder fails on
held-out trials under every reading: mean R2 from -497.1 to -249.1% for ALM to medulla and from -6098.6
to -2191.3% for ALM to ALM (A1), against 40 and 54%, and it stays negative under the five seeds. The
negative values are not an artefact of the averaging or the denominator: the median over bins is
-308.0 to -178.8% (ALM to medulla), and the R2 over the whole span, which keeps the time-locked
variance, is -262.8 to -120.3%. Nor do they come mainly from the heavy tails of the baseline
z-score: with the example.m z-score, whose largest |z| is 24 to 124 in the bilateral sessions, ALM to
medulla falls to -1828.9 to -1512.9%. Over the 44 session and direction pairs the R2 falls with the
number of predictors per training trial (9 times the source dimensions over the training trials;
Spearman correlation -0.61) more than with the source's largest |z| (-0.24); it is above zero in 3 of
44 pairs, all with 0.24 predictors per trial or fewer. The nine lagged copies of the smoothed
projections are nearly collinear (condition number about 1e6), and lambda = 0.01 barely regularizes
them. In the variants with larger penalties R2 is at most 16.6% (ALM to medulla, lambda 100), and ALM
to ALM (6.9%) stays below ALM to medulla, the reverse of the paper.

**Result (fig4d-decoding-asymmetry): not reproduced.** Under every reading the paired t test of ALM to
medulla against medulla to ALM gives p = 0.70 to 0.99 over the 5 sessions, and medulla to ALM R2 is
-517.9 to -290.4%, against 21 +- 6.7%; over the five seeds p is 0.45 to 1.00. Under the median over
bins, the R2 over the span and the example.m z-score, p is 0.11 to 0.99. In the lambda = 100 variant
ALM to medulla exceeds medulla to ALM by 6.2 points (p = 0.091), with medulla to ALM at 10.4%. Under
reading G2 (second notebook) every R2 is below -10^5 % and p is 0.15 to 0.87.
''')
assert src(39).startswith('**Result: partially')
put(39,'''**Result: partially reproduced.** In the test-set embedding 25.7% of ALM units have no medulla unit
among their 10 nearest neighbours, against 0.1% with the region labels shuffled over all units and
0.1% with them shuffled within each session (21.3 to 27.3% over the five seeds), and 6 of the 26 grid
cells that hold ALM units hold no medulla unit. So part of the ALM movement-null patterns has no
medulla counterpart, as the paper reports, and this is not the clumping of units by session, which
the within-session shuffle keeps. The second part of the criterion holds only in part. On the grid
of the claim seed's embedding no medulla cell (0 of 20) lies outside the cells that hold ALM units,
but only 59.4% of medulla units have an ALM unit among their neighbours (99.7% with labels shuffled
within session; 58.2 to 62.6% over the seeds). The medulla of sub-460436_ses-20200109 has d_null = 1,
and its units spread along one line (spread 9.75, against 2.3 to 4.7 for the other regions); without
that session (claim seed plus 1), 21.0% of ALM units have no medulla neighbour, 16 of 57 ALM cells
hold no medulla unit, and 26 of 67 medulla cells lie outside the ALM cells. The judgment rests on
these counts and the plots, as the paper's rests on inspection.
''')
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
```

```
Sun Nov 22 06:57:38 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
s=''.join(C[36]['source'])
for a,b in [("mean R2 from -497.1 to -249.1% for ALM to medulla","mean R2 from -611.5 to -249.1% for ALM to medulla"),
            ("the median over bins is\n-308.0 to -178.8% (ALM to medulla)","the median over bins is\n-364.9 to -178.8% (ALM to medulla)"),
            ("is -262.8 to -120.3%.","is -320.8 to -120.3%."),
            ("every R2 is below -10^5 % and p is 0.15 to 0.87.","every R2 is below -10^6 % and p is 0.15 to 0.87.")]:
    assert a in s, a; s=s.replace(a,b)
C[36]['source']=s.splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
grep -c "" reproduce_hasnain_2025.ipynb
```

```
1390
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
assert ''.join(C[40]['source']).startswith('## Summary')
C[40]['source']='''## Summary

| Claim | Outcome |
|---|---|
| Eleven claims on the paper's own recordings (Figures 1 to 3, Extended Data Figures 2 and 3) | Blocked: data missing |
| map-session-selection | Not reproduced |
| fig4b-medulla-selectivity | Partially reproduced |
| fig4c-alm-null-potent-similar | Partially reproduced, resting on reading G1 (reproduced under G2) |
| fig4c-medulla-null-smaller | Reproduced under the claim's seed, resting on readings G1, B2 and V2; partially reproduced under two other seeds and under G2 |
| fig4d-alm-predicts-medulla-null | Not reproduced |
| fig4d-decoding-asymmetry | Not reproduced |
| fig4e-medulla-null-lower-dimension | Not reproduced, resting on reading G1 (reproduced under G2 with N2) |
| fig4f-medulla-null-not-spanning-alm | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

How the analysis differs from the paper's:

- Under reading G1 of 'good' the selection gives 5 ALM and medulla sessions (paper 16 or 11) and 17
  bilateral sessions (paper 20), so every Figure 4 test here runs on fewer sessions and units than the
  paper's. Reading G2 (second notebook) gives 19 ALM and medulla sessions with about 2.4 times the
  paper's units; its CCF labels are transferred from the nearest unit classified good.
- The movement threshold is Otsu's threshold on the log speed, where the paper set it by hand; the
  keypoint positions are smoothed (3 frames) first.
- Ignore, photostimulation and early-lick trials are left out, and so are trials whose delay is not
  1.2 s (446 correct and error trials over the 22 sessions).
- The dimension shuffle uses 100 shuffles on every 4th bin (the paper 1000 on all bins).
- UMAP runs in umap-learn, not MATLAB's run_umap.
- The readings of the claims file were each run with the others held at the main reading, not in
  every combination.

What was found about the dataset:

- `anno_name` (the CCF label) is filled only for units whose `classification` is good (69453 of
  272227 units), and 1852 units have no `classification`. The electrodes table holds CCF coordinates,
  from which the label of other units can be estimated.
- The trial table has no column for the delay duration. In the ALM and medulla sessions and the 2021
  bilateral sessions, 13 to 57 correct and error trials per session have a 1.8 s or 0.3 s delay,
  which shows only in the sample and delay event times.
- Some units have near-silent baselines, so the baseline z-score of the Methods gives values up to 278
  s.d. among G1 units and above 50000 among G2 units.
- The jaw and nose tracking are in pixels, at about 294 Hz, in one segment per trial; unsmoothed, their
  frame-to-frame jitter hides movement. Nearly every bin of the kept trials has tracking.
- Clocks: in every selected session the tongue becomes visible a median 56 to 262 ms after the go cue,
  and lick direction is decoded from spike counts after the go cue above the shuffled labels, so the
  spike, video and trial clocks are consistent.
- The units of the session compared are identical in versions 0.230822.0128 and 0.231012.2129.
'''.splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
grep -o '"acc 0.8": [^,]*' /dev/null; python3 -c "
import json;nb=json.load(open('../../executed/hasnain-2025/reproduce_hasnain_2025.ipynb'))
t=''.join(nb['cells'][9]['outputs'][0]['text'])
import re
print(t[:200])" | head -3
```

```
session  trials  kept  hits  right  go_in_trial  speed_thr  tongue_lat_ms  tongue_pre_go  lick_lat_ms  other_delay other_delay_onsets  sample_from_go_s  sample_min  sample_m
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; sed -i 's/paper'"'"'s units; its CCF labels are transferred/paper'"'"'s units; its CCF labels are transferred/; s/with about 2.4 times the/with about 2.5 times the/' reproduce_hasnain_2025.ipynb; grep -c "2.5 times the" reproduce_hasnain_2025.ipynb; python - <<'EOF'
import json, uuid
P='reproduce_hasnain_2025_g2.ipynb'
nb=json.load(open(P)); C=nb['cells']
def md(s): return {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":s.splitlines(True)}
heads=[''.join(c['source'])[:40] for c in C]
for i,h in enumerate(heads): print(i,h.replace('\n',' '))
# header fix
s=''.join(C[0]['source'])
a="""the second a UMAP that the main notebook shows to be dominated by
# session)""".replace('# ','')
a2="the second a UMAP that the main notebook shows to be dominated by\nsession)"
assert a2 in s, s[-900:]
s=s.replace(a2,"the second is left to the main\nnotebook to keep this one within the time limit)")
C[0]['source']=s.splitlines(True)
results = {
 5: md('''**Result (reading G2): partially reproduced.** Of 1745 medulla units in 19 sessions, under E1 with
the Bonferroni threshold 16.7% are selective in the sample epoch, 28.3% in the delay epoch and 63.4% in
the response epoch (paper 7, 21 and 49%); over the five seeds 16.6 to 17.6%, 27.7 to 28.7% and 63.4 to
63.9%. The order holds, and no value is within tolerance under E1, E2 or either threshold. By session
the sample value runs from 1.9 to 42.9%.
'''),
 9: md('''**Result (reading G2).** fig4c-alm-null-potent-similar: under the main reading with V2, ALM null
and potent variance are 33.9 and 42.7%, both within tolerance of 36.0 and 37.1%, and the paired t
test finds no difference (p = 0.251 over 19 sessions; 0.249 to 0.261 over the seeds below), which the
criterion counts as reproduced. With V1 the main-reading p is 0.050 (0.050 to 0.058 over the seeds);
under B2 potent exceeds null (V1 p = 0.002, V2 p = 0.041) with means out of tolerance.
fig4c-medulla-null-smaller: null is below potent under the main reading (V1 46.3 against 67.3%,
p = 0.020; V2 35.7 against 51.7%, p = 0.027) and under B2 (V2 30.8 against 56.4%, p = 0.005), lower in
15 or 16 of 19 sessions, with the null mean outside 26.4 +- 3.9% in each, which the criterion counts as
partially reproduced. Single units dominate some regions: the largest |z| is above 1000 in 8 of the
38 regions, and in sub-460432_ses-20191218 the ALM null subspace holds 95.7% of the variance (V2).
'''),
 13: md('''**Result (reading G2).** N1 does not differ (medulla 10.9, ALM 10.9, p = 0.98; 0.86 to 1.00 over
the seeds; under B2 p = 0.876). N2 is lower in the medulla (3.35 against 5.93, p = 0.027, lower in 14 of
19 sessions; under B2 3.72 against 6.92, p = 0.018), which the criterion counts as reproduced under N2.
In 5 sessions the medulla N2 is below 1.4, and each of these regions has a unit whose |z| exceeds 3000,
so N2 there measures one unit.
'''),
 15: md('''**Result (reading G2): not reproduced.** Every mean R2 is below -10^6 % (no session has a medulla to
ALM R2 above zero), and the paired t test of ALM to medulla against medulla to ALM gives p = 0.15 to 0.46
under the claim's seed and 0.17 to 0.87 over the other seeds.

## Summary (reading G2)

| Claim | Under G2 |
|---|---|
| fig4b-medulla-selectivity | Partially reproduced (16.7, 28.3, 63.4%) |
| fig4c-alm-null-potent-similar | Reproduced (main reading, V2: 33.9 against 42.7%, p = 0.251) |
| fig4c-medulla-null-smaller | Partially reproduced (test holds, null mean out of tolerance) |
| fig4e-medulla-null-lower-dimension | Reproduced under N2 (p = 0.027), not under N1 (p = 0.98) |
| fig4d-decoding-asymmetry | Not reproduced |

The attempt's outcomes rest on reading G1 (main notebook), whose bilateral unit counts are near the
paper's; G2 gives about 2.5 times the paper's units and transfers CCF labels from the nearest unit
classified good. A failure to reproduce here may be a failure of this attempt, not of the paper: see
the reasoning and the differences from the paper's method.
'''),
}
for i in sorted(results, reverse=True):
    C.insert(i+1, results[i])
nb['cells']=C
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
```

```
1
0 # Hasnain, Han & Economo (2025) on DANDI
1 import os os.environ.setdefault("OMP_NUM
2 ## Data check  Units tables of every fil
3 from sklearn.linear_model import Logisti
4 ## Claim fig4b-medulla-selectivity, read
5 def selectivity(rng):     out = []     f
6 ## Per-region subspaces, reading G2  Mai
7 def prepare(p, region_ids, short_runs_mo
8 ## Claims fig4c-alm-null-potent-similar 
9 ve_rows = [] for (rname, reg), d in fit_
10 Seed check: the main reading again under
11 seed_rows = [] for k in SEED_OFFSETS[1:]
12 ## Claim fig4e-medulla-null-lower-dimens
13 dim_rows = [] for p, s in alm_med.items(
14 ## Claim fig4d-decoding-asymmetry, readi
15 bins = np.arange(int(round((ms.TASK_SPAN
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('executed/hasnain-2025/reproduce_hasnain_2025_g2.ipynb'))
t=''.join(o.get('text','') if isinstance(o.get('text',''),str) else ''.join(o['text']) for o in nb['cells'][7]['outputs'])
rows=[l.split() for l in t.splitlines() if ' main ' in l]
z=[float(r[10]) for r in rows]; print(len(z), sum(v>1000 for v in z), sorted(z)[-10:])
"
```

```
38 9 [871.0, 1363.0, 3406.0, 4605.0, 5099.0, 15613.0, 33422.0, 45215.0, 50011.0, 53615.0]
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; sed -i 's/is above 1000 in 8 of the/is above 1000 in 9 of the/' reproduce_hasnain_2025_g2.ipynb; grep -c "above 1000 in 9" reproduce_hasnain_2025_g2.ipynb; cat > README.md <<'EOF'
# Hasnain, Han & Economo (2025) from dandiset 000363

Tests the findings of [Hasnain, Han and Economo (2025)](https://doi.org/10.1101/2025.10.17.682917)
that can be tested on [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the
Mesoscale Activity Map recordings (Chen et al. 2024) that the paper reuses for its Figure 4. The
paper's own cell-type-specific recordings (Figures 1 to 3) are not public.

| Claim | Outcome |
|---|---|
| The paper's selection gives 20 bilateral ALM and 16 (or 11) ALM and medulla sessions | Not reproduced |
| Medullary units are selective, most in the response epoch (7, 21, 49%) | Partially reproduced |
| In ALM, null and potent subspaces explain comparable variance | Partially reproduced, resting on one reading of 'good' |
| In the medulla, the null subspace explains less variance than the potent | Reproduced, resting on one reading and sensitive to the seed |
| ALM predicts medullary null activity nearly as well as the other ALM | Not reproduced |
| Medulla predicts ALM less well than ALM predicts the medulla | Not reproduced |
| The medullary null subspace has lower dimensionality than ALM's | Not reproduced, resting on one reading of 'good' |
| Medullary units do not span ALM's null activity patterns (UMAP) | Partially reproduced |
| Eleven claims on the paper's own recordings | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper selects sessions with at least 30 units "classified as 'good'". With the `classification`
column, whose units carry the dataset's CCF labels, this gives 5 ALM and medulla sessions, not 16 or
11, so the Figure 4 tests run on fewer sessions and units than the paper's. With the `unit_quality`
column, and CCF labels transferred from the nearest classified unit, it gives 19 sessions with about
2.5 times the paper's units; the second notebook repeats the tests there. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/hasnain-2025-01.yaml`](../../attempts/hasnain-2025-01.yaml).

- `reproduce_hasnain_2025.ipynb`: the analysis, under the `classification` reading. It takes about
  30 minutes, most of it streaming the units tables of all 174 files and fitting subspaces.
- `reproduce_hasnain_2025_g2.ipynb`: the Figure 4 tests on the ALM and medulla sessions under the
  `unit_quality` reading. About 35 minutes.
- `map_subspace.py`: loading, label transfer, firing rates, movement masks, subspace identification,
  dimensionality, variance explained, cross-region decoding and selectivity, with where each
  parameter comes from. Other notebooks on this dandiset can import it.
EOF
cd  python tools/entry.py check entries/hasnain-2025 2>&1 | tail -3; date -u
```

```
1
0 error(s)
Sun Nov 22 06:58:53 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/hasnain-2025; python - <<'EOF'
import json
P='reproduce_hasnain_2025.ipynb'
nb=json.load(open(P)); C=nb['cells']
s=''.join(C[37]['source'])
a="is from the other region, against the same count with the region labels shuffled (1000 times)."
assert a in s
s=s.replace(a,"""is from the other region, against the same count with the region labels shuffled (1000 times) over
all units and within each session (which keeps any clumping of units by session). The embedding is
also shown by session, with each region's extent, and again without the session whose medulla has a
one-dimensional null subspace.""")
C[37]['source']=s.splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
cd  date -u; python tools/entry.py all entries/hasnain-2025 > $TMPDIR/run2.log 2>&1; echo exit $?; tail -4 $TMPDIR/run2.log; date -u
```

```
Sun Nov 22 06:59:01 UTC 2026
exit 0
Installed kernelspec registry-hasnain-2025 in executed/hasnain-2025/.venv/share/jupyter/kernels/registry-hasnain-2025
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (1643 s)
pass  reproduce_hasnain_2025_g2.ipynb  (2045 s)
Sun Nov 22 08:00:40 UTC 2026
```

**Agent**

Final run passed. Checking the numbers match the previous run before writing the record.

**Agent calls Bash**

```bash
cd  python $TMPDIR/dump.py executed/hasnain-2025/reproduce_hasnain_2025.ipynb > $TMPDIR/n1.txt; python $TMPDIR/dump.py executed/hasnain-2025/reproduce_hasnain_2025_g2.ipynb > $TMPDIR/n2.txt; diff <(grep -v elapsed $TMPDIR/o1.txt | grep -v "peak memory") <(grep -v elapsed $TMPDIR/n1.txt| grep -v "peak memory") | head -40; echo ----; diff <(grep -v elapsed $TMPDIR/o2.txt| grep -v "peak memory") <(grep -v elapsed $TMPDIR/n2.txt| grep -v "peak memory") | head; python3 -c "
import json;nb=json.load(open('executed/hasnain-2025/reproduce_hasnain_2025.ipynb'))
for o in nb['cells'][33]['outputs']:
    t=o.get('text','');t=t if isinstance(t,str) else ''.join(t)
    for l in t.splitlines():
        if 'Spearman' in l or 'below -500' in l: print(l[:230])
"
```

```
7c7
< sessions per probe target: {'right ALM': 103, 'left ALM': 108, 'right Striatum': 57, 'left Striatum': 54, 'right Midbrain': 68, 'right Thalamus': 36, 'left Thalamus': 45, 'left Midbrain': 68, 'right Medulla': 24, 'left Medulla': 23, 'right ECT': 14, 'left ECT': 18, 'right BLA': 8, 'left BLA': 9}
---
> sessions per probe target: {'right ALM': 103, 'left ALM': 108, 'left Striatum': 54, 'right Striatum': 57, 'right Midbrain': 68, 'right Thalamus': 36, 'left Midbrain': 68, 'left Thalamus': 45, 'left Medulla': 23, 'right Medulla': 24, 'right ECT': 14, 'left ECT': 18, 'right BLA': 8, 'left BLA': 9}
----
67c67
< === cell 7
---
> === cell 8
141c141
< === cell 9
---
> === cell 10
159c159
< === cell 11
across sessions and directions, Spearman correlation of mean R2 with the source's largest |z|: -0.24, with the predictors per training trial: -0.61
all sessions and directions (incl. ALM to ALM), Spearman correlation of mean R2 with predictors per training trial: -0.61; R2 above 0 in 3 of 44, whose largest predictors per trial is 0.24
per-bin R2 below -500% (clipped in the plot): 991 of 6600 bins
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p questions/README.md; ls questions | head -3; cat questions/asari-2009.yaml | head -30; grep -l "verifications:" attempts/*.yaml | head -3
```

```
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
README.md
asari-2009.yaml
ashworth-2025.yaml
questions:
- claim: fig2-example-long-context
  question: The criterion says the example cell and probe are not identified and accepts any
    current-clamp cell with seven natural sound fragments and a probe tested after silence and
    two other fragments. Does the Figure 2 legend identify them? Figure 2A gives the cell's
    reliability (0.61 +/- 0.07 over its stimuli) and the probe's (0.74 +/- 0.08), and Figure 2B
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "round: 1" attempts/*.yaml | head -3; f=$(grep -l "round: 1" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -60; ls schemas 2>/dev/null; grep -rn "verifications" schemas/*attempt* 2>/dev/null | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
400:    "verifications": {
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['verifications'],indent=1)[:5000])
print(json.dumps(s['properties']['outcomes']['items'].get('properties',{}).get('proposed',{}),indent=1)[:800])
"; grep -l "^verifications:" attempts/*.yaml | head -2
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk '/^verifications:/,0' attempts/andrews-2024-01.yaml | head -30
```

```
verifications:
- date: '2026-11-10'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text under paper/. The verifier queried the
    DANDI API for the version's assets and metadata, checked Table 1 against cell 16 by hand, and
    tested light_steps, window_rates and reduce_chunk on synthetic inputs.
  results:
  - claim: table1-cohort
    agrees: true
    outcome: partially_reproduced
    reason: Cells 5 and 16 give 12 slices and 7 patients (patient read from the slice-name letter),
      5 F and 2 M, ages 20 to 52, and every patient's age and sex match Table 1. All 8 HcKCR1 slice
      names are present. No opsin is recorded in the asset metadata or the inspected objects, so "8
      HcKCR1 / 2 ChR2 / 2 none" cannot be derived from the data, which meets the criterion's partial
      clause. But the search for opsin, virus, genotype or condition fields skips every object under
      general/, where NWB stores virus, subject/genotype, experiment_description, notes,
      pharmacology, protocol, optogenetics and stimulus; if any held the opsin the claim would be
      reproduced (problem 1). Cell 16 compares Table 1 ages and sexes only by printing them next to
[... 10 more lines not kept]
```

**Agent**

Outputs are identical across the two runs. Now writing the attempt record.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/hasnain-2025-01.yaml'
r=yaml.safe_load(open(P))
O={o['claim']:o for o in r['outcomes']}
O['map-session-selection'].update(notes=(
 "Reading G1 of 'good' (`classification`), units with a CCF label of MOs on a probe described as targeting ALM, "
 "or of IRN, GRN or PARN, and sessions with at least 30 such units in each region, gives 17 bilateral ALM sessions "
 "from 9 mice (paper 20 from 10), with 858 right and 1001 left ALM units (paper 961 and 1055; the left count is "
 "within tolerance, the right is not), and 5 ALM and medulla sessions from 4 mice (paper 16 in the Results, 11 from "
 "7 mice in the Methods), with 300 ALM and 340 medulla units (paper 604 and 724). Only units classified good carry "
 "a CCF label, but the electrodes table gives each electrode's CCF coordinates, and among units classified good the "
 "nearest other such unit on the probe has the same label for 97.3% of units. With labels transferred that way "
 "(within 20 um), reading G2 (`unit_quality` good) gives 31 bilateral sessions from 12 mice (2767 and 2830 units) and "
 "19 ALM and medulla sessions from 7 mice (1501 and 1745 units); within 0 um 28 and 13 sessions, within 40 um 35 and "
 "22; reading U2 (all units) gives 44 and 28 sessions. No reading gives the session counts together with the unit "
 "counts, so the claim is not reproduced. With 20 good units (G1) as the threshold there are 31 bilateral and 14 ALM "
 "and medulla sessions, with 25 there are 26 and 9."),
 deviations=[
  "The claims file's U1 is applied with `classification` as the 'good' label (G1), the only label whose units carry a "
  "CCF annotation. G2 (`unit_quality` good) and U2 (all units) are formed by giving each unit the CCF label of the "
  "nearest unit classified good on the same probe, by electrode coordinates, within 20 um (assumed; 0 and 40 um shown).",
  "G1 is the main reading for every Figure 4 claim (assumed). Its bilateral unit counts are near the paper's, where "
  "G2's are 2.7 to 2.9 times them, and the paper's 'classified as good' names the `classification` column."])
O['map-session-selection']['assumed']=True
O['fig4b-medulla-selectivity'].update(measured=[32.4,49.1,85.9], notes=(
 "340 medulla units of the 5 G1 ALM and medulla sessions, correct trials, 54 to 157 trials per side per session. "
 "Under E1 with the Bonferroni threshold (p < 0.01) 32.4% are selective in the sample epoch, 49.1% in the delay epoch "
 "and 85.9% in the response epoch (paper 7, 21 and 49%). Under E1 the order holds (response highest, sample lowest) for "
 "every seed and both thresholds, so the claim is partially reproduced; under E2 the early delay sub-epoch (30.3%) falls "
 "below the sample epoch (32.4%). No reading puts a value within tolerance (E2 sub-epochs 30.3 to 66.8%; uncorrected "
 "p < 0.05 higher still). Over the five seeds E1 Bonferroni gives 30.9 to 32.9%, 47.9 to 51.5% and 85.0 to 85.9%. By "
 "session the sample value runs from 1.7 to 54.8%. The share of right trials changes over the session (0.13 to 0.73 by "
 "fifth in one session), but with labels shuffled only within blocks of 30 trials the values are 30.3, 47.9 and 85.9%, "
 "so slow drift does not explain them. Under reading G2 (1745 units, 19 sessions) the values are 16.7, 28.3 and 63.4% "
 "(16.6 to 17.6, 27.7 to 28.7 and 63.4 to 63.9 over the seeds), also partially reproduced."),
 deviations=[
  "Ignore, photostimulation and early-lick trials are left out, and so are trials whose sample cue does not start 1.85 s "
  "before the go cue (a 1.8 s or 0.3 s delay; 446 correct and error trials over the 22 sessions), as the epochs assume "
  "the paper's 1.2 s delay (assumed; the paper does not say how MAP's photostimulation, early-lick and other-delay "
  "trials were treated).",
  "Epoch rates are the means of the smoothed 5 ms rates (Methods, \"Identifying selective neurons\"), not z-scored.",
  "Units of reading G1 (map-session-selection); G2 is shown in the second notebook."])
O['fig4b-medulla-selectivity']['assumed']=True
O['fig4c-alm-null-potent-similar'].update(measured=[51.3,79.6], notes=(
 "5 G1 sessions, 40 to 85 ALM units each. Under the main reading (W1, B1, D1, baseline z-score) the paired t test of null "
 "against potent variance finds no difference (V1 51.3 against 79.6%, p = 0.086; V2 23.2 against 36.9%, p = 0.125; V3 "
 "70.5 against 87.7%, p = 0.194), nor under W2 or D2, but no reading of M3 to M6 puts both means within tolerance, so the "
 "absence holds and the values do not, a partial reproduction. Under B2 the test finds potent above null (V1 p = 0.040, "
 "V2 p = 0.029), with means out of tolerance, which the criterion does not count against the claim. The z-score of "
 "example.m, a variant in the claims file, puts both V2 means within tolerance (30.2 against 29.0%) and there the test "
 "finds a difference (p = 0.028); were the variant a reading, the claim would be not reproduced. With 5 sessions the test "
 "has little power; the main-reading V1 difference is 28.3 points. Over the five seeds the main-reading V1 p is 0.079 to "
 "0.086, the B2 V1 p 0.040. Under reading G2 (19 sessions) the main reading with V2 gives 33.9 against 42.7%, p = 0.251 "
 "(0.249 to 0.261 over the seeds), which the criterion counts as reproduced; the outcome rests on G1. Movement-null "
 "dimensions are 5 to 10, potent 4 to 9; 30 to 50% of bins are moving, mostly in the response epoch (51 to 77% of its "
 "bins, 1 to 25% of baseline bins)."),
 deviations=[
  "5 sessions where the paper has 16 (map-session-selection, reading G1, assumed); reading G2 shown in the second notebook.",
  "The movement threshold is Otsu's threshold on log10 speed, a standard choice for the value between the two modes that "
  "the paper set by hand; the keypoint positions are first smoothed with a Gaussian of 3 frames, as unsmoothed tracking "
  "jitter makes the speed histogram unimodal.",
  "Ignore, photostimulation, early-lick and other-delay trials are left out (assumed).",
  "The dimensions come from 100 shuffles of every 4th 5 ms bin, where the paper uses 1000 shuffles, to fit the time limit.",
  "The readings W2, B2, D2 and the example.m z-score were each run with the others at the main reading, not in every "
  "combination.",
  "The total covariance C of the variance explained is taken over the bins with tracking (no more than 0.1% of bins lack it)."])
O['fig4c-medulla-null-smaller'].update(measured=[28.4,51.9], seed_sensitive=True, notes=(
 "Reproduced under the claim's seed with readings G1, B2 (supra-threshold runs shorter than 100 ms counted as moving) "
 "and V2, as the criterion accepts any one reading of M1 to M6. There the medulla null subspace explains 28.4% and the "
 "potent 51.9% (tolerances 26.4 +- 3.9 and 44.8 +- 7.12, so at most 51.92), paired t p = 0.017 over 5 sessions. Over "
 "the five seeds the null mean is 27.9 to 28.8%, the potent 51.0 to 52.3% and p 0.017 to 0.024; under the seeds plus 2000 "
 "and plus 4000 the potent mean (52.3%) is just outside tolerance, which would make the claim partially reproduced. V1 "
 "gives p = 0.003 with the potent mean (83.5%) out of tolerance. Under the main reading B1 the difference is not "
 "significant (V1 54.4 against 67.1%, p = 0.312; V2 34.5 against 41.4%, p = 0.344), nor under W2 or D2; the example.m "
 "z-score gives V2 p = 0.042 with the null mean (31.5%) out of tolerance. So the outcome rests on one of 15 reading "
 "combinations, which the paper does not settle, and under B2 the ALM difference is also significant "
 "(fig4c-alm-null-potent-similar): no single reading reproduces both Figure 4c claims. Under reading G2 (19 sessions) "
 "null is below potent under the main reading (V2 35.7 against 51.7%, p = 0.027; V1 p = 0.020; V1 and V2 p 0.008 to "
 "0.027 over the seeds) and under B2 (V2 30.8 against 56.4%, p = 0.005), with the null mean outside tolerance in each, "
 "partially reproduced. 31 to 128 medulla units per G1 session."),
 deviations=[
  "The outcome rests on reading G1 of the selection, B2 of M4 and V2 of M6, which the paper leaves open (asked of the "
  "authors under findings).",
  "5 sessions where the paper has 16; the threshold, trial, shuffle and covariance deviations of "
  "fig4c-alm-null-potent-similar apply."])
O['fig4d-alm-predicts-medulla-null'].update(measured=[-497.1,-4271.6], notes=(
 "With lambda = 0.01, as the Methods give it, held-out R2 is far below zero under every reading (T1 or T2, R1 or R2, "
 "standardized or not), from -611.5 to -249.1% for ALM to medulla (5 sessions) and from -6098.6 to -2191.3% for ALM to "
 "ALM (A1, 17 sessions), against 40 and 54%; the values given as measured are T1, unstandardized, R1. It stays negative "
 "under the five seeds. The negative values are not due to the averaging or the denominator: the median over bins is "
 "-364.9 to -178.8% (ALM to medulla) and the R2 over the whole span, which keeps the time-locked variance, -320.8 to "
 "-120.3%. Nor do they come mainly from the heavy tails of the baseline z-score: with the example.m z-score (largest |z| "
 "24 to 124 in the bilateral sessions, against 37 to 278) ALM to medulla falls to -1828.9 to -1512.9%. Over the 44 session "
 "and direction pairs the R2 falls with the number of predictors per training trial (Spearman correlation -0.61) more "
 "than with the source's largest |z| (-0.24), and it is above zero in 3 of 44 pairs, all with 0.24 predictors per trial "
 "or fewer: with up to 9 x 13 predictors and 94 to 368 training trials, a nearly unpenalized per-bin fit overfits. As "
 "variants with larger penalties, standardized and pooled, R2 is at most 16.6% (ALM to medulla, lambda 100), with ALM to "
 "ALM at 6.9%, below ALM to medulla, the reverse of the paper."),
 deviations=[
  "Subspaces from the main reading and reading G1; the bilateral sessions are 17, not 20.",
  "Larger penalties, the R2 over the whole span, the median over bins and the example.m z-score are shown as variants; "
  "the claim's lambda and the per-bin R2 of M8 decide the outcome."])
O['fig4d-decoding-asymmetry'].update(measured=-491.4, notes=(
 "Under every reading the paired t test of ALM to medulla against medulla to ALM gives p = 0.70 to 0.99 over 5 sessions, "
 "and medulla to ALM R2 is -517.9 to -290.4% (T1, unstandardized, R1 -491.4%), against 21 +- 6.7%; over the five seeds p "
 "is 0.45 to 1.00. Under the median over bins, the R2 over the span and the example.m z-score p is 0.11 to 0.99. In the "
 "lambda = 100 variant ALM to medulla exceeds medulla to ALM by 6.2 points (p = 0.091), with medulla to ALM at 10.4%. "
 "Under reading G2 (19 sessions) every mean R2 is below -10^6 % and p is 0.15 to 0.87, not reproduced."))
O['fig4e-medulla-null-lower-dimension'].update(notes=(
 "Reading G1, 5 sessions. N1 (shuffle dimension of the stationary activity) is 7.0 in the medulla and 7.6 in ALM, "
 "p = 0.741, lower in 2 of 5 sessions; 0.68 to 0.741 over the five seeds, and p = 0.39 to 0.91 under W2, B2 and D2 (under "
 "B2 the medulla is higher, 10.0 against 8.2). N2 (participation ratio of the movement-null covariance) is 3.23 against "
 "5.27, p = 0.087, lower in 4 of 5; per unit p = 0.31. Neither reading gives p < 0.05. The example.m z-score, a variant, "
 "gives N1 10.2 against 14.4, p = 0.042. Under reading G2 (19 sessions) N1 does not differ (p = 0.98; 0.86 to 1.00 over "
 "the seeds) but N2 is lower in the medulla (3.35 against 5.93, p = 0.027, lower in 14 of 19; B2 p = 0.018), which the "
 "criterion counts as reproduced; there the medulla N2 is below 1.4 in 5 sessions, each with a unit whose |z| exceeds "
 "3000. The outcome rests on G1. The medulla has 31 to 128 units and ALM 40 to 85; the medulla has fewer units in 2 "
 "sessions."),
 deviations=[
  "5 sessions (reading G1, assumed); dimensions from 100 shuffles of every 4th bin.",
  "N2 is the claims file's stand-in for the scale-dependent measure of ref 70, which the paper does not specify."])
O['fig4f-medulla-null-not-spanning-alm'].update(notes=(
 "Test-set UMAP of 300 ALM and 340 medulla units (reading G1). 25.7% of ALM units have no medulla unit among their 10 "
 "nearest neighbours, against 0.1% with the region labels shuffled over all units and 0.1% with them shuffled within each "
 "session (21.3 to 27.3% over the five seeds), and 6 of the 26 grid cells that hold ALM units hold no medulla unit, so "
 "ALM holds patterns without a medulla counterpart, as the paper reports, and this is not clumping by session. The "
 "criterion's second part holds only in part. No medulla grid cell (0 of 20) lies outside the cells that hold ALM units, "
 "but only 59.4% of medulla units have an ALM neighbour (99.7% with labels shuffled within session; 58.2 to 62.6% over "
 "seeds). The medulla of sub-460436_ses-20200109 has d_null = 1 and its units spread along one line; without that "
 "session (claim seed plus 1) 21.0% of ALM units have no medulla neighbour, 16 of 57 ALM cells hold no medulla unit and "
 "26 of 67 medulla cells lie outside the ALM cells. The judgment rests on these counts and the plots."),
 deviations=[
  "umap-learn with the Methods' parameters stands in for MATLAB's run_umap (claims, M10); the neighbour and grid counts "
  "are this attempt's description of the embedding, the paper judges by inspection.",
  "Units pooled over the 5 G1 sessions (assumed); subspaces from the main reading."])
O['fig4f-medulla-null-not-spanning-alm']['assumed']=True
# findings
F=r['findings']
F[0]['statement']=("With the dataset's own CCF labels and `classification`, the paper's selection (at least 30 good units "
 "in each region) gives 5 ALM and medulla sessions from 4 mice, with 300 ALM and 340 medullary reticular units, where the "
 "paper reports 16 sessions (or 11 from 7 mice) with 604 and 724 units; and 17 bilateral ALM sessions from 9 mice where "
 "the paper reports 20 from 10. With `unit_quality` and CCF labels transferred by electrode coordinates from the nearest "
 "classified unit it gives 19 ALM and medulla sessions from 7 mice with 1501 and 1745 units, and 31 bilateral sessions. "
 "No reading of the files recovers the paper's selection.")
F[1]['statement']=("The units' CCF annotation (`anno_name`) is filled only for units whose `classification` is good (69453 "
 "of 272227 units); the others have an empty label and only the probe's target region, though the electrodes table holds "
 "each electrode's CCF coordinates (x, y, z). The column description does not say this.")
F[6]['statement']=("Cross-region decoding (Figure 4d). With ridge lambda = 0.01 and the source projections at t and 8 "
 "preceding bins of 20 ms-smoothed rates, the predictors are nearly collinear and held-out R2 is far below zero on these "
 "data, falling with the number of predictors per training trial. Was lambda applied to standardized predictors, was R2 "
 "computed on held-out single trials at each bin and over which variance (the across-trial variance at each bin or over "
 "the whole span), and were trials or bins pooled before the fit?")
F[8]['statement']=("MAP trials and units. Were photostimulation, early-lick and ignore trials used, and the trials with a "
 "1.8 s or 0.3 s delay? Is the 'good' label of the selection the `classification` or the `unit_quality` column, with CCF "
 "regions assigned to which units? Here Figure 4c (ALM) is reproduced and Figure 4e is reproduced under N2 with "
 "`unit_quality`, and neither with `classification`.")
F[10]['statement']=("The baseline z-score (Methods, Subspace identification) divides by the baseline s.d. across trials; "
 "for MAP units with near-silent baselines this gives values up to 278 s.d. among units classified good and above 50000 "
 "among units with `unit_quality` good. Were such units excluded, or was a floor applied?")
F.append(dict(kind='metadata_insufficient', severity='minor', statement=(
 "The trial table has no column for the delay duration. In the ALM and medulla sessions and the 2021 bilateral sessions "
 "used here, 13 to 57 correct and error trials per session (446 over 22 sessions) have a 1.8 s or 0.3 s delay in place "
 "of 1.2 s, which shows only in the sample and delay event times (`sample_start_times`, `delay_start_times`).")))
by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)"
A=lambda claim,agrees,outcome,reason,response: dict(claim=claim,agrees=agrees,outcome=outcome,reason=reason,response=response)
blocked_reason=("I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174 files "
 "in every version). Searching the archive for \"Hasnain\", \"Economo\", \"extratelencephalic\" and \"movement-null\" finds "
 "no dataset with the paper's own recordings. All 11 need phototagged L-ETNs or the paper's videos, so no part can be "
 "tested on MAP.")
res=[A(c,True,'blocked',blocked_reason,"No change.") for c in ["own-recordings-cohort","fig1i-selectivity-proportions",
 "fig2c-subspace-variance","fig2e-potent-only-units","fig2f-letn-preference-like-un","fig2gh-letn-span-subspaces",
 "ed2f-false-negatives","fig3c-network-beats-linear","fig3d-letn-un-movement-encoding","ed3-letn-fast-switch","ed3a-cd-early-un-not-letn"]]
res.append(A("map-session-selection",True,"not_reproduced",
 "Cell 12: 17 bilateral sessions from 9 mice (tolerance 20 +- 2). ALM and medulla: 5 sessions from 4 mice, against 11 "
 "(Methods) or 16 (Results). Unit counts: ALM 300 (paper 604), medulla 340 (paper 724), right ALM 858 (paper 961 +- 96.1). "
 "Only left ALM (1001) is within tolerance. Problem 1: the notebook never checked whether the electrodes table carries CCF "
 "coordinates or labels per electrode, which would let the `unit_quality == 'good'` reading be tested; the paper's "
 "\"unit classification based on common spike sorting metrics\" fits that reading at least as well, and the counts are "
 "sensitive to the threshold.",
 "The electrodes table holds CCF x, y, z per electrode but no region label. Among units classified good the nearest other "
 "such unit on the probe has the same CCF label for 97.3%, so the cell now forms G2 (`unit_quality` good) and U2 (all "
 "units) by that transfer, within 0, 20 and 40 um: G2 at 20 um gives 31 bilateral sessions (2767 and 2830 units) and 19 "
 "ALM and medulla sessions from 7 mice (1501 and 1745 units). No reading gives the counts, so the outcome is unchanged. "
 "A second notebook repeats the Figure 4 tests on the ALM and medulla sessions under G2. G1 stays the main reading, as an "
 "assumption, for its bilateral unit counts near the paper's; the outcomes that differ under G2 say so."))
res.append(A("fig4b-medulla-selectivity",True,"partially_reproduced",
 "Cell 16, Bonferroni, E1 reading: sample 34.1%, delay 52.9%, response 86.5%, against 7 / 21 / 49. The order holds "
 "(response highest, sample lowest), which the criterion counts as partial, but every value is 2 to 5 times the paper's, "
 "under every seed and alpha. Problem 5: the notebook offers no diagnosis; non-stationary trial order, which would bias "
 "the permutation test, was not looked at.",
 "Added the share of right trials by fifth of the session and the test with labels shuffled within blocks of 30 trials "
 "(30.3, 47.9 and 85.9%, against 32.4, 49.1 and 85.9% unblocked), so drift does not explain the values. Trials with a "
 "1.8 s or 0.3 s delay are now left out. New values 32.4, 49.1 and 85.9%; under G2 16.7, 28.3 and 63.4%, still outside "
 "tolerance. The text now says that under E2 the early delay falls below the sample epoch. Outcome unchanged."))
res.append(A("fig4c-alm-null-potent-similar",True,"partially_reproduced",
 "Cell 18: the absence holds under every main reading (p 0.13 to 0.26, n = 5). Means are out of tolerance (V1 54.5 / "
 "77.3; V2 null 24.0, below the 28.6 floor). Only the example.m z-score, which M3 calls a \"variant\", matches (30.7 / 29.1, "
 "p = 0.119). Whether a variant counts as a reading is ambiguous in the claims file; if it does, this becomes reproduced. "
 "The small n weakens the absence claim (problem 1).",
 "Re-run with the other-delay trials left out: main reading V1 51.3 against 79.6%, p = 0.086. The example.m variant now "
 "has both V2 means in tolerance (30.2 against 29.0%) with p = 0.028, so were it a reading the claim would be not "
 "reproduced; it is kept as a variant, as the claims file has it. Under reading G2 (19 sessions) the main reading with "
 "V2 reproduces the claim (33.9 against 42.7%, p = 0.251); the outcome stays partially reproduced, resting on G1, marked "
 "assumed, and the notes give the G2 result."))
res.append(A("fig4c-medulla-null-smaller",True,"reproduced",
 "Reproduced, under the criterion but fragile. Cell 18: B2 with V2 gives null 28.5 and potent 51.2 (both within "
 "tolerance), p = 0.0097, stable over 5 seeds. That is 1 of 15 reading combinations. The main reading gives p = 0.445, "
 "and V2 is the reading the claims file says departs from the Methods formula. Problem 4: B2, which gives the medulla "
 "result, also makes ALM null fall below potent (p = 0.024), and the example.m z-score, which matches ALM, gives a "
 "medulla null mean of 31.5, outside 26.4 +- 3.9; the medulla reproduced rests on one of 15 combinations, chosen per claim.",
 "Outcome kept, with the fragility recorded in the notes. After leaving out the other-delay trials, B2 with V2 gives 28.4 "
 "against 51.9% (p = 0.017), the potent mean just inside its 51.92 bound; under two of the five seeds it is 52.3%, outside, "
 "so the outcome is now marked seed_sensitive. The notes state that it rests on 1 of 15 combinations and that no single "
 "reading reproduces both Figure 4c claims. Under G2 the test holds under the main reading and B2 with the null mean out "
 "of tolerance (partially reproduced)."))
res.append(A("fig4d-alm-predicts-medulla-null",True,"not_reproduced",
 "Cells 27 and 28: R2 at lambda = 0.01 is strongly negative under every reading and seed (ALM to medulla -153 to -326%; "
 "ALM to ALM, A1 reading, -2035 to -7423%). With a larger lambda (variant), ALM to ALM (5.7%) falls below ALM to medulla "
 "(21.3%), the reverse of the paper. Problem 2: the extreme negative R2 values were not traced to their cause; the "
 "example.m z-score was never used for decoding, and the R2 over the whole averaged span was not run.",
 "Added, on the same splits: the R2 over the whole span, the median over bins, decoding with the example.m z-score "
 "subspaces, and per session the per-bin R2 by epoch with the across-trial variance of the targets, plotted over time. "
 "All stay far below zero (span -320.8 to -120.3%, example.m -1828.9 to -1512.9% for ALM to medulla). R2 falls with the "
 "predictors per training trial (Spearman -0.61) more than with the largest |z| (-0.24), so the cause is overfitting of a "
 "nearly unpenalized per-bin fit, not the heavy tails. Outcome unchanged."))
res.append(A("fig4d-decoding-asymmetry",True,"not_reproduced",
 "Cell 27: asymmetry p = 0.46 to 0.89. Medulla to ALM R2 ranges from -378 to -184%, against 21 +- 6.7%.",
 "Same additions as for fig4d-alm-predicts-medulla-null; under them p is 0.11 to 0.99, and under G2 0.15 to 0.87. The "
 "lambda = 100 text now matches the output (6.2 points, p = 0.091 after the re-run). Outcome unchanged."))
res.append(A("fig4e-medulla-null-lower-dimension",True,"not_reproduced",
 "Cell 23: N1 p = 0.646 (medulla lower in 2 of 5 sessions). N2 p = 0.092 (lower in 4 of 5). No reading reaches p < 0.05. "
 "With n = 5 against the paper's 16 the test is weak.",
 "Re-run: N1 p = 0.741, N2 p = 0.087. Under reading G2 (19 sessions) N2 is lower in the medulla (p = 0.027, 14 of 19), "
 "which would reproduce the claim, but there the medulla N2 is near 1 in 5 sessions dominated by one near-silent unit. "
 "The outcome stays not reproduced, resting on G1 and marked assumed; the notes give the G2 result."))
res.append(A("fig4f-medulla-null-not-spanning-alm",False,"not_reproduced",
 "Not reproduced, by inspection. Cell 33 plot: medulla points cover nearly the whole extent of the ALM points. Only 2 of "
 "31 grid cells that hold ALM units have no medulla unit, and 5 of 34 medulla cells lie outside the ALM cells. The "
 "neighbour statistic cannot be trusted (problem 3): the medulla of sub-460436_ses-20200109 has d_null = 1, which maps all "
 "65 units onto two points, and the label-shuffle null mixes units across sessions, so the neighbour shares measure "
 "clumping by session and by low rank, not by region.",
 "Outcome kept as partially reproduced, and the disagreement recorded. The embedding is now shown by session with each "
 "region's extent, and the null shuffles labels within each session: 25.7% of ALM units have no medulla neighbour against "
 "0.1% under that null (21.3 to 27.3% over seeds), so the ALM patterns without a medulla counterpart are not clumping by "
 "session. In this run 6 of 26 ALM grid cells hold no medulla unit and no medulla cell lies outside the ALM cells. Without "
 "the d_null = 1 session the first part still holds (21.0%; 16 of 57 ALM cells without medulla) but 26 of 67 medulla "
 "cells lie outside the ALM cells. The first part of the criterion holds and the second in part."))
ver=dict(date='2026-11-22',kind='agent',by=by,reviewed=(
 "The first executed notebook with the conclusion cells and the summary removed, the helper module and the claims file, "
 "with the paper's full text under paper/. The verifier queried the DANDI API for the dandiset's versions and searched "
 "the archive for the paper's own recordings, and tested ridge_r2, selectivity_p, the rate kernel, shuffle_dimension and "
 "movement_mask on synthetic inputs. Its other points: subspaces fitted on all trials including test trials (problem 7; "
 "kept, as the fit is unsupervised and within one region, and stated here), the stated deviations reasonable (problem 8), "
 "bins without tracking in the total covariance (problem 9; now excluded, no more than 0.1% of bins), the cell 31 text not "
 "matching its outputs (problem 6; every result text rewritten from the new outputs), and the trial labels, moving bins per "
 "epoch and the sample cue time, now printed. The sample cue check found trials with a 1.8 s or 0.3 s delay, now left out."),
 results=res)
r['verifications']=[ver]
yaml.safe_dump(r, open(P,'w'), sort_keys=False, width=110, allow_unicode=True)
PYEOF
python3 $TMPDIR/rec.py && python tools/entry.py check entries/hasnain-2025 2>&1 | tail -5; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep "trials per side" $TMPDIR/n1.txt | cut -c1-400; cd  python3 - <<'EOF'
p='attempts/hasnain-2025-01.yaml'
s=open(p).read()
for a,b in [("(51 to 77% of its","(51 to 82% of its"),]:
    assert a in s; s=s.replace(a,b)
import re
i=s.find("or fewer: with up to 9 x 13"); print(s[i-50:i+200])
open(p,'w').write(s)
EOF
```

```
medulla units: 340  trials per side per session: {'sub-456774_ses-20191022T133136': 54, 'sub-460436_ses-20200109T111437': 103, 'sub-460436_ses-20200110T142717': 130, 'sub-484676_ses-20210419T130102': 134, 'sub-484677_ses-20210418T132006': 136}
3 of 44 pairs, all with 0.24 predictors per trial or fewer: with up to 9 x 13 predictors and 94 to 368
    training trials, a nearly unpenalized per-bin fit overfits. As variants with larger penalties, standardized
    and pooled, R2 is at most 16.6%
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
p='attempts/hasnain-2025-01.yaml'
r=yaml.safe_load(open(p))
O={o['claim']:o for o in r['outcomes']}
o=O['fig4d-alm-predicts-medulla-null']
o['notes']=o['notes'].replace("or fewer: with up to 9 x 13 predictors and 94 to 368 training trials, a nearly unpenalized per-bin fit overfits.",
 "or fewer: with up to 1.24 predictors per training trial (T1), a nearly unpenalized per-bin fit overfits.")
assert "1.24 predictors" in o['notes']
o=O['fig4b-medulla-selectivity']
o['notes']=o['notes'].replace("54 to 157 trials per side","54 to 136 trials per side"); assert "54 to 136" in o['notes']
yaml.safe_dump(r, open(p,'w'), sort_keys=False, width=110, allow_unicode=True)
EOF
grep -n "1.24 pred\|54 to 136\|51 to 82" attempts/hasnain-2025-01.yaml | cut -c1-80; grep -n "proposed\|seed_sensitive\|assumed" attempts/hasnain-2025-01.yaml | head -20
```

```
111:  notes: 340 medulla units of the 5 G1 ALM and medulla sessions, correct tri
148:    4 to 9; 30 to 50% of bins are moving, mostly in the response epoch (51 t
207:    zero in 3 of 44 pairs, all with 0.24 predictors per trial or fewer: with
97:    the nearest unit classified good on the same probe, by electrode coordinates, within 20 um (assumed; 0 and 40
99:  - G1 is the main reading for every Figure 4 claim (assumed). Its bilateral unit counts are near the paper's, where
101:  assumed: true
104:  assumed: true
125:    epochs assume the paper's 1.2 s delay (assumed; the paper does not say how MAP's photostimulation, early-lick
131:  assumed: true
151:  - 5 sessions where the paper has 16 (map-session-selection, reading G1, assumed); reading G2 shown in the second
156:  - Ignore, photostimulation, early-lick and other-delay trials are left out (assumed).
165:  assumed: true
189:  seed_sensitive: true
192:  assumed: true
217:  assumed: true
231:  assumed: true
244:  - 5 sessions (reading G1, assumed); dimensions from 100 shuffles of every 4th bin.
248:  assumed: true
264:  - Units pooled over the 5 G1 sessions (assumed); subspaces from the main reading.
470:      reproduced, resting on G1, marked assumed, and the notes give the G2 result.'
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/hasnain-2025 2>&1 | tail -2; python tools/entry.py run entries/hasnain-2025 2>&1 | tail -3; git status --short; date -u
```

```
0 error(s)
pass  reproduce_hasnain_2025.ipynb  (1643 s, reused)
pass  reproduce_hasnain_2025_g2.ipynb  (2045 s, reused)
reused the executed copies of 2026-11-22 08:00 UTC: nothing the run reads has changed since (hash 98d1c7353396). Nothing was executed and no environment was built; --fresh runs it again.
 M attempts/hasnain-2025-01.yaml
 M entries/hasnain-2025/README.md
 M entries/hasnain-2025/entry.yaml
 M entries/hasnain-2025/map_subspace.py
 M entries/hasnain-2025/reproduce_hasnain_2025.ipynb
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
?? entries/hasnain-2025/reproduce_hasnain_2025_g2.ipynb
[... 2 more lines not kept]
```

**Agent**

## Report on round 2 of hasnain-2025-01

**Outcome changes: none.** All 19 outcomes are as in round 1.
- 11 claims stay blocked (`data_missing`).
- map-session-selection, both fig4d claims and fig4e stay not reproduced.
- fig4b and fig4c-alm stay partially reproduced.
- fig4c-medulla stays reproduced. It is now marked `seed_sensitive`, because under two of the five seeds the potent mean is 52.3%, just above its 51.92 limit.
- fig4f stays partially reproduced. The verifier would give not reproduced. I kept the outcome and recorded the disagreement under `response`: when region labels are shuffled only within each session, 0.1% of ALM units lack a medulla neighbour, against 25.7% observed. So the first part of the criterion holds and is not an effect of session clumping. The second part holds only in part.

**Added or corrected, by report point:**
- **Unit selection (B1):** the electrodes table has CCF x, y, z for each electrode but no region label. Among units classified good, the nearest other such unit carries the same label for 97.3% of them. Using that nearest-neighbour label, I formed two more readings of "good": G2 (`unit_quality`) and U2 (all units). Neither recovers the paper's counts. G2 gives 19 ALM and medulla sessions with about 2.5 times the paper's units.
  - A second notebook, `reproduce_hasnain_2025_g2.ipynb`, repeats the Figure 4 tests under G2. Under G2, fig4c-alm would be reproduced and fig4e would be reproduced with N2.
  - The outcomes still rest on G1 (`classification`), marked `assumed`. Its bilateral unit counts are near the paper's, while G2's are 2.7 to 2.9 times them. The G2 results are in the notes and in the finding that asks the authors.
- **Decoding (B2):** I added three variants: R2 over the whole span, the median over bins, and decoding with the example.m z-score. I also added per-bin R2 by epoch and the target variance at each bin. All R2 stay far below zero. R2 tracks the number of predictors per training trial (Spearman −0.61) more than the heavy tails (−0.24), so the cause is overfitting of a nearly unpenalized per-bin fit.
- **UMAP (B3):** the embedding is now also coloured by session, with the per-session null dimension and extent, the within-session shuffle null, and a variant without the session whose medulla has a null dimension of 1.
- **Selectivity (B5):** a shuffle within blocks of 30 trials and the share of right trials by fifth of the session. Drift does not explain the high values.
- **Text (B6):** every result text is rewritten from the new outputs.
- **Covariance (B9):** bins without tracking are now excluded from the total covariance. They are at most 0.1% of bins.
- **Trials:** the printed trial labels and sample-cue times showed that 446 correct and error trials had a 1.8 s or 0.3 s delay. They are now left out. I added a minor data finding (number 12): the trial table has no column for delay duration. I also printed the moving bins per epoch.
- **Record:** round 1 is recorded under `verifications`, with the verifier's reasons and my responses. Findings 1, 2, 7, 9 and 11 are updated in place, so the numbering is unchanged.
- **Run:** `python tools/entry.py all` passed: 27 minutes for the main notebook and 34 for the G2 notebook. A second full run gave identical outputs.

**Not done:**
- No `questions/hasnain-2025.yaml`. The verifier reported no misreading of the claims file. The two gaps it raised (the R2 denominator in M8, and whether the example.m variant counts as a reading) go to the paper's authors through the findings and claim notes.
- B7 (subspaces fitted on all trials, test trials included) is left as it is and stated. The fit is unsupervised and within one region.
- I did not commit or push.

## End of run

73 turns, 160 minutes, $10.14 at API prices, result: success.
