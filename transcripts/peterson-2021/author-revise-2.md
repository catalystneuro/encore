# peterson-2021 · author-revise-2 · run 45607546111

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls entries/peterson-2021 transcripts/peterson-2021 questions; cat transcripts/peterson-2021/verifier-2-report.md
```

```
Wed Nov 25 11:55:28 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
executed
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
[... 273 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | head -c 60000; wc -c docs/protocol.md
```

```
<persisted-output>
Output too large (46.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4209c94d-d07d-4927-a451-59353e14dd0c/tool-results/bvnf634ut.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4209c94d-d07d-4927-a451-59353e14dd0c/tool-results/bvnf634ut.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 761 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep peterson; wc -l attempts/peterson-2021-02.yaml; cat entries/peterson-2021/entry.yaml entries/peterson-2021/README.md; ls -la executed/peterson-2021/
```

```
peterson-2021-02.yaml
692 attempts/peterson-2021-02.yaml
schema_version: 1
name: peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds the ECoG, pose and wrist movement events of the paper's 12 subjects over 55
  days. It checks the cohort and the events, the behavioural features of Figure 2, the movement-related
  spectral power of Figures 3 to 5 and Table 1, projected to regions with the paper's projection
  matrices from Figshare, and the single-event regression models of Figure 6.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson et al. (2021) from dandiset 000055
  runtime_minutes: 40
helpers:
- ajile.py
related:
[... 54 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/peterson-2021-02.yaml"
}
```

```
1	schema_version: 3
2	id: peterson-2021-02
3	datasets:
4	- archive: dandi
5	  id: "000055"
6	  version: 0.261123.1703
7	  doi: 10.48324/dandi.000055/0.261123.1703
8	  relation: primary
9	paper: doi:10.1523/eneuro.0007-21.2021
10	date: 2026-11-25
11	entry: peterson-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 673 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "agree\|proposed\|verif" tools/entry.py | head -80; ls schemas
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
35:`handover` builds what a verifier is given in its first round
379:        # A verification round's review of a finding points at the finding by its number in the record.
380:        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
383:                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
387:        agreed = {}
388:        for rnd in (attempt.get("verifications") or [])[1:]:
390:                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
407:            verified = agreed.get(outcome.get("claim"))
408:            if verified and outcome.get("outcome") != verified:
410:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
411:                                    "and verify it in another round")
655:    """The notebook without the author's conclusions, for a verifier's first round."""
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
sed -n 370,420p tools/entry.py; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
import pprint
def find(o,k,path=''):
    if isinstance(o,dict):
        for kk,v in o.items():
            if kk==k: print(path+'/'+kk); pprint.pprint(v, width=150)
            find(v,k,path+'/'+kk)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,k,path+f'[{i}]')
find(s,'verifications'); find(s,'proposed')
"
```

```
seen = set()
        for item in (attempt.get("findings_review") or {}).get("findings") or []:
            number, its = item["finding"], attempt.get("findings") or []
            if number > len(its) or number in seen:
                report.error(where, f"`findings_review` names finding {number} " + ("twice" if number in seen else
                                    f"and the record has {len(its)} findings"))
            elif its[number - 1].get("severity"):
                report.error(where, f"`findings_review` rates finding {number}, which the attempt rated itself")
            seen.add(number)
        # A verification round's review of a finding points at the finding by its number in the record.
        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
            for item in rnd.get("findings") or []:
                if item["finding"] > len(attempt.get("findings") or []):
                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
                                        f"has {len(attempt.get('findings') or [])} findings")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
        agreed = {}
        for rnd in (attempt.get("verifications") or [])[1:]:
            for r in rnd["results"]:
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags',''),len(src),'|',src[:150].replace('\n',' ¶ '))
EOF
wc -l ajile.py
```

```
0 markdown  3358 | # Reproducing Peterson et al. (2021) from DANDI:000055 ¶  ¶ Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of ¶ Na
1 code  540 | import os, re, time, zlib, resource ¶ os.environ.setdefault("OMP_NUM_THREADS", "1") ¶ import numpy as np ¶ import pandas as pd ¶ from scipy import stats ¶ impor
2 code  233 | # LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed) ¶ assets = ajile.list_assets() ¶ metas = ajile.load_all
3 code ['sanity'] 1015 | ev_all = ajile.event_table(metas) ¶ subjects = sorted(ev_all.subject.unique()) ¶ print("subjects:", subjects) ¶ days = ev_all.groupby("subject").day.unique(
4 code ['sanity'] 2709 | # Checks of the description against the values ¶ m0 = metas[0] ¶ print("ECoG unit:", m0["ecog_unit"], "conversion:", m0["ecog_conversion"], "rate:", m0["e
5 code ['sanity'] 452 | # Coarse behavioural labels (epochs) at the event times. The Methods exclude movements during ¶ # sleep, unrelated experiments and private times. ¶ lab = 
6 markdown  592 | ## Projection matrices (outside input) and claim `roi-projection-link` ¶  ¶ > The rows of the paper's projection matrices from electrodes to the eight reg
7 code ['claim:roi-projection-link'] 2409 | files, fig_meta = ajile.figshare_files() ¶ print("Figshare item", fig_meta["id"], "version", fig_meta["version"], fig_meta["doi"]) ¶ proj, cents, link_row
8 code ['claim:roi-projection-link'] 3126 | # Largest-weight region against the nearest region centroid, with mirrored MNI positions ¶ rng = np.random.default_rng(seed("roi-projection-link")) ¶ def 
9 markdown  772 | **Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as ¶ many rows as electrodes with a position in all 12 sub
10 markdown  627 | ## Spectral power of every event (streamed) ¶  ¶ For each file, the chunk index of the ECoG series is read from the file's B-tree, and the chunks ¶ holding 
11 code  855 | # SPEC
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [0,4,11,12,13,46,56,64,66,67,68,75,76]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        print('--OUT--'); print(''.join(t)[:5000])
EOF
```

```
<persisted-output>
Output too large (46.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4209c94d-d07d-4927-a451-59353e14dd0c/tool-results/b97igei5j.txt

Preview (first 2KB):
===== 0
# Reproducing Peterson et al. (2021) from DANDI:000055

Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of
Naturalistic Arm Movements", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.

Dataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).
This version was asked for in the prompt of this attempt, a repeat attempt that tests what the
dataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,
pose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;
nothing is downloaded.

Claims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)
and checked by a second reader. Method details the claims file does not give are taken from the
paper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit
04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4209c94d-d07d-4927-a451-59353e14dd0c/tool-results/b97igei5j.txt"
}
```

```
1	===== 0
2	# Reproducing Peterson et al. (2021) from DANDI:000055
3	
4	Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of
5	Naturalistic Arm Movements", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.
6	
7	Dataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).
8	This version was asked for in the prompt of this attempt, a repeat attempt that tests what the
9	dataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,
10	pose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;
11	nothing is downloaded.
12	
13	Claims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)
14	and checked by a second reader. Method details the claims file does not give are taken from the
15	paper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit
16	04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's
17	projection matrices from electrodes to regions, Figshare item 12114408 version 1
18	(doi:10.6084/m9.figshare.12114408.v1).
19	
20	The notebook runs for about 40 minutes: about 10 minutes to stream the ECoG around 8088 events
[... 613 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "renormalis\|bad electrode\|4.9" claims/peterson-2021.yaml | head; python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/peterson-2021.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig5-recording-day-effects','fig4-precentral-subject-variability'):
        print(yaml.dump(cl,width=150))
EOF
cat questions/peterson-2021.yaml | head -80; grep -n "Problem 2\|^\*\*2\|86400" transcripts/peterson-2021/verifier-1-report.md
```

```
37:# supramarginal, superior temporal, middle temporal, inferior temporal); bad electrodes get
38:# weight 0 and each region's weights are renormalised to sum to 1 per subject (code); region
73:# pos_r2_inds); the Methods and the Figure 1 legend remove bad electrodes from further analysis,
82:# notches, resampled to 500 Hz, common median reference per electrode group, bad electrodes by
612:    selection by LFB R2, the code's 80/20 split, and the code's inclusion of bad electrodes.
648:    code's selection by LFB R2 and its inclusion of bad electrodes are shown as variants.
673:  - Header. Added that the code fits models at bad electrodes and keeps them in the Figure 6c-d box plots; the Methods and the Figure 1 legend remove bad electrodes, so good electrodes stay the main result and the code's choice is a variant.
678:  - fig6c-angle-and-day-most-informative and fig6d-upward-reaches-enhance-pattern. Added the code's inclusion of bad electrodes as a variant.
criterion: Per subject, the unmasked median over events of precentral power (Figure 4 legend, no statistical masking), with the mean of that median over
  -1.5 to -1 s subtracted again, as plot_specs_single_region in the code does, averaged over 0 to 0.5 s (the window of the paper's banded analyses, Methods;
  Figure 4 itself shows whole spectrograms and fixes no window) to give a spectrum. The paper gives no measure, so the parts are read as follows. (1) Every
  subject has a negative mean over 8-32 Hz and a positive mean over 76-100 Hz. (2) For S03, S06, S07, S08 and S11 the 116 and 121 Hz bins are positive.
  (3) For S09 and S12 the largest value among the 56-121 Hz bins is at 61 to 76 Hz (bins within 60-80 Hz), and the mean over 101-121 Hz is below half of
  it. (4) The width of the decrease is the number of 1-46 Hz bins below half of the subject's most negative value; S04 and S08 are among the three subjects
  with the fewest. Reproduced when all four hold; partially when two or three hold. Part (1) failing 
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -n -i "table 2" paper/*.txt paper/*.md 2>/dev/null | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i "Table 2[^\n]\{0,3000\}" paper/10.1523-eneuro.0007-21.2021.txt | grep -i "day" | head -3 | cut -c1-4000; grep -o "4\.9 ± 4\.9.\{0,300\}\|.\{300\}4\.9 ± 4\.9" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
for m in re.finditer(r'Table 2', t):
    print('>>>', t[max(0,m.start()-100):m.start()+600].replace('\n',' '))
    print()
for m in re.finditer(r'4\.9', t):
    print('###', t[max(0,m.start()-400):m.start()+200].replace('\n',' '))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
i=t.find('Table 2 Statistical table')
print(t[i:i+3500])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -n 290,470p ajile.py
```

```
items = []
        for i in range(used):
            k = body[i * (key_size + 8): i * (key_size + 8) + key_size]
            size = struct.unpack("<I", k[:4])[0]
            offs = struct.unpack("<" + "Q" * rank, k[8:8 + 8 * rank])
            child = struct.unpack("<Q", body[i * (key_size + 8) + key_size: (i + 1) * (key_size + 8)])[0]
            items.append((offs, size, child))
        return level, items
    level_nodes = [root]
    with ThreadPoolExecutor(n_threads) as ex:
        while level_nodes:
            nxt = []
            for level, items in ex.map(read_node, level_nodes):
                for offs, size, child in items:
                    if level == 0:
                        out[(offs[0], offs[1])] = (child, size)
                    else:
                        nxt.append(child)
            level_nodes = nxt
    return out
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [1,21,30,34,38,78,97,98,99,100]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        print('--OUT--'); print(''.join(t)[:3000])
EOF
```

```
===== 1
import os, re, time, zlib, resource
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import ajile

KEY = "peterson-2021"
def seed(claim):
    """Seed of a claim's generator (protocol, author step 3)."""
    return zlib.crc32(f"{KEY}/{claim}".encode())
SEED_OFFSETS = [0, 1000, 2000, 3000, 4000]
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
T0 = time.time()
print("dandiset", ajile.DANDISET, "version", ajile.VERSION)
--OUT--
dandiset 000055 version 0.261123.1703
[... 400 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -n 470,698p ajile.py
```

```
"onset_speed": np.log(ev.onset_speed.values + 1) if log_speed else ev.onset_speed.values,
        "speech_ratio": ev.speech_ratio.values,
        "bimanual_ratio": ev.bimanual_ratio.values,
        "bimanual_overlap": ev.bimanual_overlap.values,
        "bimanual_class": ev.bimanual_class.values,
    }
    for k, v in cont.items():
        sd = v.std()
        cols.append((v - v.mean()) / sd if sd > 0 else v * 0)
        names.append(k)
    return np.column_stack(cols), np.array(names)


def forward_select(X, y):
    """Forward selection over single columns by OLS adjusted R2, starting from 0 and adding the
    best column while the score improves (code regression_utils._forward_selected_new, which
    selects among the columns of the design, one-hot day and time-of-day columns one by one).
    Runs on all of the subject's events, as the code does. Returns a boolean mask of columns."""
    n, p = X.shape
    chosen = np.zeros(p, bool)
[... 209 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; grep -n "region_alt\|weights_alt\|n_zero_run\|run_spectral\|run_regression" ajile.py reproduce_peterson_2021.ipynb | cut -c1-200; date -u
```

```
ajile.py:323:def session_spectral(asset_id, event_times, good, weights, weights_alt=None, n_threads=6, batch_chunks=6,
ajile.py:329:    to 1; weights_alt: a second set (the variant with the file's own flags).
ajile.py:345:    region_alt = np.full((n_ev, nr, nf, nb), np.nan, np.float32) if weights_alt is not None else None
ajile.py:348:    n_zero_run = np.zeros(n_ev, int)     # good electrodes with a run of at least 25 zero samples (50 ms)
ajile.py:403:                n_zero_run[i] = int(((cz[:, 25:] - cz[:, :-25]) == 25).any(axis=1).sum())
ajile.py:429:                if weights_alt is not None:
ajile.py:430:                    region_alt[i] = project(weights_alt, db)[0]
ajile.py:450:    return dict(region=region, region_alt=region_alt, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside,
ajile.py:451:                allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el, n_zero_run=n_zero_run, wrist=wrist, wrist_t=k / prate)
ajile.py:653:def run_regression(jobs, workers=4):
ajile.py:663:    asset_id, times, good, weights, weights_alt = args
ajile.py:664:    return session_spectral(asset_id, times, good, weights, weights_alt)
ajile.py:667:def run_spectral(jobs, workers=8):
ajile.py:668:    """jobs: list of (asset_id, event_times, good, weights, weights_alt). Runs files in parallel processes."""
reproduce_peterson_2021.ipynb:404:    "spec = ajile.run_spectral(jobs, workers=8)\n",
reproduce_peterson_2021.ipynb:427:    "ev[\"n_zero_run\"] = np.concatenate([r[\"n_zero_run\"] for r in spec])\n",
reproduce_peterson_2021.ipynb:431:    "REG_ALT = np.concatenate([r[\"region_alt\"] for r in spec])  # variant: each file's own good-electrode flags\n",
reproduce_peterson_2021.ipynb:433:    "    r[\"region\"] = r[\"region_alt\"] = None\n",
reproduce_peterson_2021.ipynb:456:    "print(\"kept events with a good electrode holding a run of at least 25 zero samples (50 ms):\", int((kk.n_zero_run > 0).sum()),\n",
reproduce_peterson_2021.ipynb:457:    "      \"; per subject:\", kk[k
[... 4 more lines not kept]
```

**Agent**

Now the helper edits.

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
p='ajile.py'; s=open(p).read()
rep=[
('''def session_spectral(asset_id, event_times, good, weights, weights_alt=None, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):''','''def session_spectral(asset_id, event_times, good, weights, weights_var=None, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):'''),
('''    to 1; weights_alt: a second set (the variant with the file's own flags).
    Returns a dict of arrays, one row per event.''','''    to 1; weights_var: a dict of further sets, each projected the same way (variants of the
    electrode choice). The variant "zero_run" is added: the main weights with, in each event, the
    electrodes holding a run of at least 25 exact zero samples (50 ms) in the segment set to 0
    and the regions renormalised (a variant asked for by the verifier; 50 ms is a standard choice).
    Returns a dict of arrays, one row per event.'''),
('''    region_alt = np.full((n_ev, nr, nf, nb), np.nan, np.float32) if weights_alt is not None else None
''','''    weights_var = dict(weights_var or {})
    region_var = {k: np.full((n_ev, nr, nf, nb), np.nan, np.float32) for k in list(weights_var) + ["zero_run"]}
    zero_run_el = np.zeros((n_ev, n_ch), bool)  # electrodes (any flag) with a run of >= 25 zero samples
'''),
('''                z = seg[good] == 0
                n_zero_el[i] = int(z.any(axis=1).sum())
                cz = np.concatenate([np.zeros((z.shape[0], 1), int), np.cumsum(z, axis=1)], axis=1)
                n_zero_run[i] = int(((cz[:, 25:] - cz[:, :-25]) == 25).any(axis=1).sum())''','''                z = seg == 0
                n_zero_el[i] = int(z[good].any(axis=1).sum())
                cz = np.concatenate([np.zeros((z.shape[0], 1), int), np.cumsum(z, axis=1)], axis=1)
                zero_run_el[i] = ((cz[:, 25:] - cz[:, :-25]) == 25).any(axis=1)
                n_zero_run[i] = int(zero_run_el[i][good].sum())'''),
('''                if weights_alt is not None:
                    region_alt[i] = project(weights_alt, db)[0]''','''                for k, wv in weights_var.items():
                    region_var[k][i] = project(wv, db)[0]
                region_var["zero_run"][i] = project(weights * ~zero_run_el[i][:, None], db)[0]'''),
('''    return dict(region=region, region_alt=region_alt, elec=elec,''','''    return dict(region=region, region_var=region_var, zero_run_el=zero_run_el, elec=elec,'''),
('''    asset_id, times, good, weights, weights_alt = args
    return session_spectral(asset_id, times, good, weights, weights_alt)''','''    asset_id, times, good, weights, weights_var = args
    return session_spectral(asset_id, times, good, weights, weights_var)'''),
('''    """jobs: list of (asset_id, event_times, good, weights, weights_alt). Runs files in parallel processes."""''',
 '''    """jobs: list of (asset_id, event_times, good, weights, weights_var). Runs files in parallel processes."""'''),
('''def run_regression(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return [r for rows in ex.map(regress_subject, jobs) for r in rows]''','''def run_regression(jobs, workers=4):
    """Runs the jobs largest first (events x models), so that the workers finish together, and
    returns the rows in the order of the jobs. Each job has its own generators, so the order
    does not change a result."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    order = sorted(range(len(jobs)), key=lambda i: -jobs[i]["Y"].shape[0] * jobs[i]["Y"].shape[1])
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        res = dict(zip(order, ex.map(regress_subject, [jobs[i] for i in order])))
    return [r for i in range(len(jobs)) for r in res[i]]'''),
]
for a,b in rep:
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "def project" -A3 ajile.py | head
```

```
312:def project(weights, db):
313-    """Region power of one event: db (n_ch, n_freq, n_bins), weights (n_ch, n_roi) with bad
314-    electrodes 0. Electrodes with any non-finite value get weight 0 and each region's weights
315-    are renormalised. Returns (region power (n_roi, n_freq, n_bins), weighted electrodes dropped)."""
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [3,7,13,50,53,59,70,73,83,86]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 3
ev_all = ajile.event_table(metas)
subjects = sorted(ev_all.subject.unique())
print("subjects:", subjects)
days = ev_all.groupby("subject").day.unique().map(sorted)
print("days per subject:", days.to_dict())
for m in metas[:1]:
    print("session_description:", m["session_description"])
# Per-file facts
rows = []
for m in metas:
    el = m["electrodes"]
    rows.append(dict(subject=int(m["subject_id"]), day=int(m["session_id"]), sex=m["sex"], age=m["age"],
                     start=m["session_start"][:10], ecog_hours=m["ecog_shape"][0] / m["ecog_rate"] / 3600,
                     n_el=m["ecog_shape"][1], n_el_table=len(el), good=int(el.good.sum()),
                     no_position=int(el.x.isna().sum()), events=len(m["reaches"]), event_wrist=m["event_wrist"],
                     pose_hours=m["pose_shape"][0] / m["pose_rate"] / 3600,
                     events_after_ecog_end=int((m["event_times"] + 5 > m["ecog_shape"][0] / m["ecog_rate"]).sum())))
files = pd.DataFrame(rows)
print(files.to_string())
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
i=t.find('Table 2 Statistical table'); j=t.find('Confidence intervals for LFB (8–32 Hz) and HFB',i)
s=t[i:j].replace('−','-')
lfb,hfb=s.split('( Fig. 5 , HFB)')
out={}
for band,txt in (('lfb',lfb),('hfb',hfb)):
    for m in re.finditer(r'S(\d\d) \((.*?)\)',txt):
        sub=int(m.group(1))
        for d in re.finditer(r'[Dd]ay (\d), (-?[\d.]+)(?: to |–)(-?[\d.]+)',m.group(2)):
            out.setdefault(band,{}).setdefault(sub,{})[int(d.group(1))]=(float(d.group(2)),float(d.group(3)))
for b in out:
    print(b, sum(len(v) for v in out[b].values()))
    print(out[b])
EOF
grep -o "Data preprocessing\|Preprocessing[^.]\{0,60\}" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
i=t.find('removal of 4.9')
print(t[i-1500:i-900])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:50]); setsrc(i,s.replace(a,b))

# cell 4: removed electrodes under three readings of the flags
rep(4,'''print("columns of the reaches table:"''','''# Electrodes removed per subject under three readings of the flags, against the paper's "removal of
# 4.9 +- 4.9 surface electrodes per subject and 1.0 +- 1.4 depth electrodes for each of the five subjects
# with depth electrodes" (Methods, "ECoG data processing"). Depth: groups described as depth (cohort).
rm = []
for s in subjects:
    ms = [m for m in metas if int(m["subject_id"]) == s]
    G = np.array([m["electrodes"].good.values for m in ms]).astype(bool)
    dep = ms[0]["electrodes"].group_name.map(ms[0]["groups"]).fillna("").str.contains("depth", case=False).values
    for name, bad in (("bad in any file", (~G).any(0)), ("bad in every file", (~G).all(0))):
        rm.append(dict(subject=s, reading=name, surface=int((bad & ~dep).sum()), depth=int((bad & dep).sum()), has_depth=bool(dep.any())))
    rm.append(dict(subject=s, reading="each file's flags (mean over files)", surface=float((~G[:, ~dep]).sum(1).mean()),
                   depth=float((~G[:, dep]).sum(1).mean()), has_depth=bool(dep.any())))
rm = pd.DataFrame(rm)
print("electrodes removed per subject (surface / depth):")
print(rm.pivot(index="subject", columns="reading", values=["surface", "depth"]).round(1).to_string())
for name, g in rm.groupby("reading", sort=False):
    d = g[g.has_depth].depth
    print(f"  {name}: surface {g.surface.mean():.1f} +- {g.surface.std():.1f} per subject (paper 4.9 +- 4.9); "
          f"depth {d.mean():.1f} +- {d.std():.1f} over the {len(d)} subjects with depth groups (paper 1.0 +- 1.4)")
print("columns of the reaches table:"''')

# cell 11: a third electrode set
rep(11,'''# Electrodes good in every file of the subject (main); each file's own flags (variant, projection only)
GOOD_ALL = {s: np.all([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
            for s in subjects}
W_MAIN = {s: ajile.session_weights(proj[s][1][:, roi_idx], GOOD_ALL[s]) for s in subjects}''','''# Electrodes good in every file of the subject (main). Variants, projection only: each file's own
# flags ("file"); the electrodes good in at least one file, i.e. only those bad in every file removed
# ("any"); and the main set with the electrodes holding a 50 ms run of zeros in an event dropped from
# that event ("zero_run", made in the helper).
GOOD_ALL = {s: np.all([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
            for s in subjects}
GOOD_ANY = {s: np.any([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
            for s in subjects}
W_MAIN = {s: ajile.session_weights(proj[s][1][:, roi_idx], GOOD_ALL[s]) for s in subjects}
W_ANY = {s: ajile.session_weights(proj[s][1][:, roi_idx], GOOD_ANY[s]) for s in subjects}''')
rep(11,'''    jobs.append((m["asset_id"], m["event_times"], GOOD_ALL[s], W_MAIN[s], w_file))''','''    jobs.append((m["asset_id"], m["event_times"], GOOD_ALL[s], W_MAIN[s], {"file": w_file, "any": W_ANY[s]}))''')

# cell 12
rep(12,'''REG_ALT = np.concatenate([r["region_alt"] for r in spec])  # variant: each file's own good-electrode flags
for r in spec:
    r["region"] = r["region_alt"] = None''','''REG_VAR = {k: np.concatenate([r["region_var"][k] for r in spec]) for k in spec[0]["region_var"]}  # variants
for r in spec:
    r["region"] = r["region_var"] = None''')
rep(12,'''print("NaN region values among kept events:", int(np.isnan(REG[ev.keep.values]).sum()), "; variant:",
      int(np.isnan(REG_ALT[ev.keep.values]).sum()))''','''print("NaN region values among kept events:", int(np.isnan(REG[ev.keep.values]).sum()), "; variants:",
      {k: int(np.isnan(v[ev.keep.values]).sum()) for k, v in REG_VAR.items()})''')

# cell 13: clock check without the zero-run electrodes for S09 and S10
rep(13,'''clock = pd.DataFrame(rows)
print(clock.round(4).to_string())''','''clock = pd.DataFrame(rows)
print(clock.round(4).to_string())
# The same for S09 and S10 with, in each event, the electrodes holding a 50 ms run of zeros left out
# and the precentral weights renormalised
for s in (9, 10):
    hf, hfs, lf, lfs = [], [], [], []
    for m, r in zip(metas, spec):
        if int(m["subject_id"]) != s:
            continue
        k = ev[(ev.asset_id == m["asset_id"])].keep.values
        w = np.nan_to_num(W_MAIN[s][:, 1])[None, :] * ~r["zero_run_el"][k]
        w = w / w.sum(axis=1, keepdims=True)
        for key, lst in (("lfb_mean", lf), ("hfb_mean", hf), ("lfb_mean_shift", lfs), ("hfb_mean_shift", hfs)):
            lst.append(np.nansum(r["elec"][key][k] * w, axis=1))
    lf, hf, lfs, hfs = map(np.concatenate, (lf, hf, lfs, hfs))
    print(f"S{s:02d} without zero-run electrodes: LFB onset {np.median(lf):.4f} vs pseudo {np.median(lfs):.4f} (p = {stats.wilcoxon(lf, lfs).pvalue:.3g}); "
          f"HFB onset {np.median(hf):.4f} vs pseudo {np.median(hfs):.4f} (p = {stats.wilcoxon(hf, hfs).pvalue:.3g})")''')

# cell 67: Table 2 intervals
rep(67,'''print("pairs agreeing, band mean:", int(t5.agree_bandmean.sum()), "of 24; band median:", int(t5.agree_bandmedian.sum()), "of 24")''','''print("pairs agreeing, band mean:", int(t5.agree_bandmean.sum()), "of 24; band median:", int(t5.agree_bandmedian.sum()), "of 24")
# Table 2: the paper's per-day 95% bootstrap intervals (5000 replicates), beside the day median of the
# band mean here and its own 5000-replicate bootstrap interval (for comparison; not part of the criterion's count)
T2 = {"lfb": {1: {3: (-2.07, -0.9), 4: (-2.77, -1.52), 5: (-1.96, -1.04), 7: (-1.8, -0.66)}, 2: {3: (-0.62, 0.6), 4: (-1.61, -0.38), 5: (-2.67, -0.32), 6: (-0.72, 0.39)},
              3: {3: (-3.12, -2.46), 4: (-2.29, -1.58), 5: (-1.55, -0.86), 6: (-1.71, -0.77)}, 4: {3: (-0.51, 0.11), 4: (-0.3, 0.24), 5: (-0.51, 0.07), 6: (-0.31, 0.07), 7: (-0.16, 0.11)},
              5: {3: (-1.22, -0.44), 4: (-1.23, -0.48), 7: (-0.56, -0.18)}, 6: {3: (-2.26, -1.42), 4: (-2.58, -1.61), 5: (-1.1, -0.4), 6: (-2.08, -0.94), 7: (-1.65, 0.18)},
              7: {3: (-1.12, -0.38), 4: (-0.73, -0.02), 5: (-0.84, -0.42), 6: (-1.24, -0.8), 7: (-0.93, 0.09)}, 8: {3: (-0.72, 0.55), 4: (-1.06, -0.18), 5: (-0.23, 0.09), 6: (-0.18, 0.11), 7: (-0.09, 0.18)},
              9: {3: (-1.42, 0.6), 4: (-0.55, 0.32), 5: (-0.65, -0.01), 6: (-0.99, 0.51), 7: (-1.14, 0.29)}, 10: {3: (-1.3, 0.0), 4: (-0.56, -0.13), 5: (-0.59, -0.09), 6: (-2.03, -0.37), 7: (-1.22, -0.27)},
              11: {3: (-3.2, -2.24), 4: (-2.18, -1.31), 5: (-1.91, -1.28), 6: (-2.18, -1.51), 7: (-3.06, -1.68)}, 12: {3: (-0.58, -0.2), 4: (-1.02, -0.21), 5: (-0.86, -0.39), 6: (-0.72, -0.32), 7: (-0.85, -0.47)}},
      "hfb": {1: {3: (-0.11, 0.34), 4: (-0.36, 0.17), 5: (0.17, 0.55), 7: (-0.06, 0.21)}, 2: {3: (-0.35, 0.66), 4: (0.08, 0.98), 5: (-0.72, 0.76), 6: (0.06, 1.02)},
              3: {3: (1.6, 2.0), 4: (1.44, 1.91), 5: (1.16, 1.64), 6: (0.41, 1.41)}, 4: {3: (-0.45, 0.12), 4: (-0.23, 0.17), 5: (0.35, 0.88), 6: (0.49, 0.93), 7: (0.32, 0.62)},
              5: {3: (-0.12, 0.5), 4: (0.03, 0.58), 7: (0.2, 0.58)}, 6: {3: (2.08, 2.71), 4: (1.76, 2.41), 5: (1.96, 2.58), 6: (1.39, 2.33), 7: (1.71, 2.83)},
              7: {3: (1.45, 1.9), 4: (1.23, 1.76), 5: (0.9, 1.26), 6: (0.82, 1.13), 7: (1.15, 1.68)}, 8: {3: (-0.11, 0.88), 4: (0.05, 0.72), 5: (0.6, 1.05), 6: (0.4, 0.71), 7: (0.13, 0.47)},
              9: {3: (-0.93, 0.32), 4: (-0.52, 1.04), 5: (-0.24, 0.21), 6: (-0.02, 0.73), 7: (-0.3, 0.4)}, 10: {3: (-0.33, 0.28), 4: (-0.14, 0.23), 5: (0.08, 0.47), 6: (-0.37, 0.55), 7: (-0.04, 0.57)},
              11: {3: (-0.24, 0.36), 4: (-0.26, 0.34), 5: (0.16, 0.52), 6: (0.04, 0.4), 7: (0.02, 0.81)}, 12: {3: (0.08, 0.34), 4: (-0.26, 0.23), 5: (-0.05, 0.26), 6: (0.01, 0.26), 7: (0.04, 0.34)}}}
rng = np.random.default_rng(seed("fig5-recording-day-effects"))
rows = []
for (s, d), g in EVB.groupby(["subject", "day"]):
    for band in ("lfb", "hfb"):
        x = g[f"pre_{band}_mean"].values
        boot = np.median(x[rng.integers(0, len(x), (5000, len(x)))], axis=1)
        lo, hi_ = T2[band][s][d]
        rows.append(dict(subject=s, day=d, band=band, n=len(x), median=np.median(x), ci=np.round(np.percentile(boot, [2.5, 97.5]), 2),
                         paper=(lo, hi_), median_inside=lo <= np.median(x) <= hi_))
t2 = pd.DataFrame(rows)
print(t2.round(3).to_string())
print("day medians inside Table 2's interval:", t2.groupby("band").median_inside.agg(["sum", "size"]).to_dict("index"))''')

# cell 75/76: three variants
setsrc(75,'''## Region results under other electrode choices (variants)

The main analysis projects every event with the electrodes good in every file of the subject (the
claims file's opening comment: bad electrodes get weight 0 and the weights are renormalised per
subject). Here the region claims are recomputed, on the same events, with (1) the flags of each
event's own file, the assumption of the first round of this attempt; (2) the electrodes good in at
least one file of the subject, that is, removing only the electrodes bad in every file, which is
also per subject, keeps the electrodes the same across days and removes the fewest electrodes
(data check); and (3) the main set with, in each event, the electrodes holding a run of at least
50 ms of exact zeros left out. The bootstrap masks use the generator of claim
fig3-group-lfb-decrease-hfb-increase plus 1, 2 and 3. For fig5-recording-day-effects every pair's p
is printed.
''')
setsrc(76,'''VARIANTS = {"file": ("each file's own flags", 1), "any": ("removing only electrodes bad in every file", 2),
            "zero_run": ("main set without zero-run electrodes", 3)}
VAR_RES = {}
for key, (label, off) in VARIANTS.items():
    RB = REG_VAR[key] - REG_VAR[key][..., ajile.BASE].mean(axis=-1, keepdims=True)
    SM = np.stack([np.nanmedian(RB[kbv & (subj_v == s)], axis=0) for s in subjects])
    GA = SM.mean(axis=0)
    GA = GA - GA[..., ajile.BASE].mean(axis=-1, keepdims=True)
    MA = mask_group(np.random.default_rng(seed("fig3-group-lfb-decrease-hfb-increase") + off), group=GA, subj_med=SM)
    print(f"=== {label} ({key})")
    tA = fig3_outcome(MA)
    print("fig3-group: named regions holding under a:", int(tA.loc[named3, "holds_a"].sum()), "; under b:", int(tA.loc[named3, "holds_b"].sum()),
          {k: {r: round(float(v), 3) for r, v in d.items()} for k, d in tA.loc[named3, ["low_a", "high_a"]].to_dict().items()})
    _, rA = largest(MA)
    print("fig3-sensorimotor:", {k: (v[0], v[1], v[2]) for k, v in rA.items()})
    _, _, aA, bA, pA = widespread(MA)
    print("fig3-lfb-more-widespread: (a)", tuple(int(x) for x in aA), "; (b)", np.round(bA, 3), "; supramarginal / superior temporal:", pA)
    partsA, p1A, wA = fig4_parts(SM, show=False)
    print("fig4: parts holding", sum(partsA), "of 4", partsA, "; subjects without the part 1 pattern:", list(p1A.index[~p1A.holds]),
          p1A[~p1A.holds].round(3).to_dict("index"), "; part 4 widths:", {f"S{int(s):02d}": int(v) for s, v in wA.items()})
    stA = ajile.band_stats(RB[:, 1])
    EA = ev.copy()
    for k, v in stA.items():
        EA["pre_" + k] = v
    EA = EA[EA.keep]
    print("fig5-band-power: H (band mean) LFB", round(stats.kruskal(*[x.pre_lfb_mean.values for _, x in EA.groupby("subject")]).statistic, 1),
          "HFB", round(stats.kruskal(*[x.pre_hfb_mean.values for _, x in EA.groupby("subject")]).statistic, 1))
    inA = {f"{st}_of_band{bst}": 0 for st in ("mean", "median") for bst in ("mean", "median")}
    agA = {"mean": 0, "median": 0}; devA, prow = [], []
    for s, g in EA.groupby("subject"):
        for bi, band in enumerate(("lfb", "hfb")):
            lo, hi_ = T1[s][bi]
            for bst in ("mean", "median"):
                x = g[f"pre_{band}_{bst}"].values
                for st, fn in (("mean", np.mean), ("median", np.median)):
                    inA[f"{st}_of_band{bst}"] += lo <= fn(x) <= hi_
                p = stats.kruskal(*[x_[f"pre_{band}_{bst}"].values for _, x_ in g.groupby("day")]).pvalue
                agA[bst] += (p < 0.05) == (s in paper_sig[band])
                prow.append(dict(subject=s, band=band, stat=bst, p=p, paper_sig=s in paper_sig[band], agree=(p < 0.05) == (s in paper_sig[band])))
            dm = g.groupby("day")[f"pre_{band}_mean"].mean()
            devA.append((dm - g[f"pre_{band}_mean"].mean()).abs().max())
    print("table1: inside, four readings", inA)
    print("fig5-recording-day-effects: pairs agreeing, band mean", agA["mean"], "of 24, band median", agA["median"], "of 24")
    pr = pd.DataFrame(prow)
    print("   pairs that disagree with the paper:", [(f"S{r.subject:02d}", r.band, r.stat, f"p={r.p:.3g}") for r in pr[~pr.agree].itertuples()])
    print("   S09 and S10, p (band mean):", {(f"S{r.subject:02d}", r.band): float(f"{r.p:.3g}") for r in pr[(pr.subject.isin([9, 10])) & (pr.stat == "mean")].itertuples()})
    print("discussion: largest day deviation", round(float(max(devA)), 3), "dB")
    VAR_RES[key] = dict(parts=partsA, inA=inA, agA=agA, pr=pr)
    del RB
''')
C[76]['outputs']=[]; C[76]['execution_count']=None
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
tail -c 300 reproduce_peterson_2021.ipynb | cat -A | tail -3; git -C  status 2>&1 | head -3
```

```
"nbformat": 4,$
 "nbformat_minor": 5$
}$
fatal: not a git repository (or any of the parent directories): .git
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][2]['source']))
EOF
grep -n "^def load_all\|^def list_assets\|^def load_meta\|^def figshare_files\|^def load_projection" ajile.py; ls ../../executed/peterson-2021/.venv/bin | head
```

```
# LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed)
assets = ajile.list_assets()
metas = ajile.load_all_meta(assets)
print(len(assets), "files,", assets["size"].sum() / 1e9, "GB in all")
79:def list_assets():
150:def load_all_meta(assets, workers=12):
193:def figshare_files():
198:def load_projection(subject, files):
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
debugpy
```

**Agent**

I've added the third electrode set, a zero-run variant and the Table 2 comparison to the notebook. Next I'm smoke-testing the helper on one small file before the full re-run.

**Agent calls Bash**

```bash
cd entries/peterson-2021; date -u; time ../../executed/peterson-2021/.venv/bin/python - <<'EOF'
import numpy as np, ajile, time, resource
assets = ajile.list_assets()
print(assets.columns.tolist()); 
a = assets[assets.path.str.contains("sub-09")].iloc[:1]
metas = ajile.load_all_meta(a)
m = metas[0]
print(m["subject_id"], m["session_id"], len(m["event_times"]))
files, _ = ajile.figshare_files()
pm, c = ajile.load_projection(9, files)
el = m["electrodes"]; a_, note = ajile.match_projection(pm, el.x.notna().values)
cols = list(pm.columns); ri=[cols.index(r) for r in ajile.ROIS]
good = el.good.values.astype(bool)
w = ajile.session_weights(a_[:, ri], good)
t=time.time()
r = ajile.session_spectral(m["asset_id"], m["event_times"][:8], good, w, {"file": w, "any": ajile.session_weights(a_[:, ri], np.ones_like(good))})
print(time.time()-t, "s")
print({k: v.shape for k, v in r["region_var"].items()}, r["zero_run_el"].sum(1), r["n_zero_run"])
print(np.nanmax(np.abs(r["region_var"]["file"] - r["region"])), np.nanmax(np.abs(r["region_var"]["zero_run"] - r["region"])))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, "GB")
EOF
```

```
Wed Nov 25 11:59:04 UTC 2026
['path', 'asset_id', 'size', 'subject', 'session']
09 3 15
28.3054256439209 s
{'file': (8, 8, 25, 26), 'any': (8, 8, 25, 26), 'zero_run': (8, 8, 25, 26)} [ 9  8  8  7  9  7 10 12] [ 9  8  8  7  9  7 10 12]
0.0 3.4886627
0.687324 GB

real	0m34.078s
user	0m9.235s
sys	0m2.045s
```

**Agent calls Bash**

```bash
cd  grep -n "stamp\|def _fingerprint\|markdown" tools/entry.py | head -30
```

```
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
37:markdown cell that begins "**Result:" and everything from the "## Summary"
579:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
582:        stamp = json.loads((output_dir / STAMP).read_text())
584:        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
586:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
588:        for r in stamp["results"]:
591:        return stamp
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
599:    if stamp:
600:        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
601:        for r in stamp["results"]:
604:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
659:        if cell.cell_type == "markdown" and text.startswith("## Summary"):
661:        if cell.cell_type == "markdown" and text.startswith("**Result:"):
```

**Agent calls Bash**

```bash
cd  sed -n 20,60p tools/entry.py; grep -n "def entry_hash" -A25 tools/entry.py
```

```
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.
A run that passes leaves a stamp beside the executed copies (.clean-run.json):
a hash of everything the run read (`hash` prints it) and of each executed
copy. `run` asked again with nothing changed since reuses those copies and says
so, without executing anything; --fresh executes all the same.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/peterson-2021 2>&1 | tail -30; date -u
```

```
Wed Nov 25 11:59:49 UTC 2026
[32m---> [39m[32m71[39m     [38;5;28;01mreturn[39;00m [30;43msession[39;49m[30;43m.[39;49m[30;43mrequest[39;49m[30;43m([39;49m[30;43mmethod[39;49m[30;43m=[39;49m[30;43mmethod[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43murl[39;49m[30;43m=[39;49m[30;43murl[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43mkwargs[39;49m[30;43m)[39;49m

[36mFile [39m[32m~/work/encore-registry/encore-registry/executed/peterson-2021/.venv/lib/python3.13/site-packages/requests/sessions.py:651[39m, in [36mSession.request[39m[34m(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)[39m
[32m    646[39m send_kwargs = {
[32m    647[39m     [33m"[39m[33mtimeout[39m[33m"[39m: timeout,
[32m    648[39m     [33m"[39m[33mallow_redirects[39m[33m"[39m: allow_redirects,
[32m    649[39m }
[32m    650[39m send_kwargs.update(settings)
[32m--> [39m[32m651[39m resp = [30;43mself[39;49m[30;43m.[39;49m[30;43msend[39;49m[30;43m([39;49m[30;43mprep[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43msend_kwargs[39;49m[30;43m)[39;49m
[32m    653[39m [38;5;28;01mreturn[39;00m resp

[36mFile [39m[32m~/work/encore-registry/encore-registry/executed/peterson-2021/.venv/lib/python3.13/site-packages/requests/sessions.py:784[39m, in [36mSession.send[39m[34m(self, request, **kwargs)[39m
[32m    781[39m start = preferred_clock()
[32m    783[39m [38;5;66;03m# Send the request[39;00m
[32m--> [39m[32m784[39m r = [30;43madapter[39;49m[30;43m.[39;49m[30;43msend[39;49m[30;43m([39;49m[30;43mrequest[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43m*[39;49m[30;43m*[39;49m[30;43mkwargs[39;49m[30;43m)[39;49m
[32m    786[39m [38;5;66;03m# Total elapsed time of the request (approximately)[39;00m
[32m    787[39m elapsed = preferred_clock() - start

[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -n 185,215p ajile.py; grep -n "^def _get\|^def _range\|retry\|Retry" ajile.py
```

```
ev["bimanual_ratio"] = ev.Bimanual_ratio.fillna(0.5)
    ev["bimanual_overlap"] = ev.Bimanual_overlap
    ev["bimanual_class"] = ev.Bimanual_class
    return ev


# ----------------------------------------------------------------------------- figshare inputs

def figshare_files():
    r = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1", timeout=60).json()
    return {f["name"]: f["download_url"] for f in r["files"]}, r


def load_projection(subject, files):
    """Projection matrix (rows = electrodes in file order, columns = AAL regions) and centroids."""
    m = pd.read_csv(io.StringIO(requests.get(files[f"aal_{subject:02d}_elecs2ROI.csv"], timeout=60).text))
    c = pd.read_csv(io.StringIO(requests.get(files[f"aal_{subject:02d}_ROIcentroids_Lside.csv"], timeout=60).text))
    return m, c


[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
p='ajile.py'; s=open(p).read()
a='''def figshare_files():
    r = requests.get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1", timeout=60).json()'''
b='''def _get(url, tries=4):
    """GET with a few retries for transient network errors; the last error is raised."""
    for k in range(tries):
        try:
            r = requests.get(url, timeout=60)
            r.raise_for_status()
            return r
        except requests.RequestException:
            if k == tries - 1:
                raise
            time.sleep(10 * (k + 1))


def figshare_files():
    r = _get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1").json()'''
assert s.count(a)==1; s=s.replace(a,b)
s=s.replace('requests.get(files[f"aal_{subject:02d}_elecs2ROI.csv"], timeout=60).text','_get(files[f"aal_{subject:02d}_elecs2ROI.csv"]).text')
s=s.replace('requests.get(files[f"aal_{subject:02d}_ROIcentroids_Lside.csv"], timeout=60).text','_get(files[f"aal_{subject:02d}_ROIcentroids_Lside.csv"]).text')
open(p,'w').write(s)
EOF
grep -n "^import\|^from" ajile.py; grep -n "_get(" ajile.py
```

```
45:import io
46:import zlib
47:from concurrent.futures import ThreadPoolExecutor
49:import h5py
50:import numpy as np
51:import pandas as pd
52:import remfile
53:import requests
193:def _get(url, tries=4):
207:    r = _get(f"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1").json()
213:    m = pd.read_csv(io.StringIO(_get(files[f"aal_{subject:02d}_elecs2ROI.csv"]).text))
214:    c = pd.read_csv(io.StringIO(_get(files[f"aal_{subject:02d}_ROIcentroids_Lside.csv"]).text))
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -i 's/^import io$/import io\nimport time/' ajile.py; grep -n "^import time" ajile.py; grep -n "time\.time\|time\.sleep" ajile.py | head; cd ../..; date -u; python tools/entry.py all entries/peterson-2021 2>&1 | tail -15; date -u
```

```
46:import time
204:            time.sleep(10 * (k + 1))
Wed Nov 25 12:03:10 UTC 2026
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
took 66 minutes; the limit is 60
0 error(s)
FAIL  reproduce_peterson_2021.ipynb  (3965 s)
Wed Nov 25 13:09:26 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls -la executed/peterson-2021/; python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [4,11,12,13,56,67,76,78,97,98,100]:
    c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t)
        if 'Warning' in t: continue
        if i==4: t=t[t.find('electrodes removed'):t.find('columns of the reaches')]
        if i==78: t=t[-1500:]
        print(t[:6000])
EOF
```

```
total 484
drwxr-xr-x 3 runner runner   4096 Nov 25 12:03 .
drwxr-xr-x 3 runner runner   4096 Nov 25 11:55 ..
drwxr-xr-x 5 runner runner   4096 Nov 25 12:03 .venv
-rw-r--r-- 1 runner runner 476600 Nov 25 13:09 reproduce_peterson_2021.ipynb
-rw-r--r-- 1 runner runner    206 Nov 25 13:09 result.json
===== 4
electrodes removed per subject (surface / depth):
                surface                                                                 depth                                                      
reading bad in any file bad in every file each file's flags (mean over files) bad in any file bad in every file each file's flags (mean over files)
subject                                                                                                                                            
1                   7.0               2.0                                 3.2             2.0               1.0                                 1.2
2                   5.0               1.0                                 2.8             2.0               0.0                                 0.5
3                  11.0               1.0                                 3.8            16.0              16.0                                16.0
4                  26.0               1.0                                 6.6             0.0               0.0                                 0.0
5                   7.0               1.0                                 3.3             0.0               0.0                                 0.0
6                  18.0               1.0                                 6.2             0.0               0.0                                 0.0
7                   3.0               1.0                                 1.4             0.0               0.0                                 0.0
8                  24.0               1.0                                 8.2             0.0               0.0                                 0.0
9               
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
c=nb['cells'][67]
t=''.join(''.join(o.get('text','')) for o in c['outputs'])
print(t[-5200:])
EOF
```

```
]   (-1.65, 0.18)           True
49         6    7  hfb  177   2.030    [1.45, 2.31]    (1.71, 2.83)           True
50         7    3  lfb   93  -0.539  [-1.03, -0.29]  (-1.12, -0.38)           True
51         7    3  hfb   93   1.550    [1.28, 1.95]     (1.45, 1.9)           True
52         7    4  lfb  110  -0.232   [-0.49, 0.04]  (-0.73, -0.02)           True
53         7    4  hfb  110   1.495     [1.21, 1.7]    (1.23, 1.76)           True
54         7    5  lfb  197  -0.375  [-0.67, -0.19]  (-0.84, -0.42)          False
55         7    5  hfb  197   1.267    [1.05, 1.44]     (0.9, 1.26)          False
56         7    6  lfb  194  -0.872  [-1.17, -0.63]   (-1.24, -0.8)           True
57         7    6  hfb  194   1.289     [1.05, 1.4]    (0.82, 1.13)          False
58         7    7  lfb  193  -0.545  [-0.83, -0.29]   (-0.93, 0.09)           True
59         7    7  hfb  193   1.367    [1.17, 1.52]    (1.15, 1.68)           True
60         8    3  lfb  193   0.023   [-0.12, 0.16]   (-0.72, 0.55)           True
61         8    3  hfb  193   0.366    [0.11, 0.62]   (-0.11, 0.88)           True
62         8    4  lfb  191  -0.160   [-0.34, 0.05]  (-1.06, -0.18)          False
63         8    4  hfb  191   0.442    [0.27, 0.59]    (0.05, 0.72)           True
64         8    5  lfb  171  -0.026   [-0.15, 0.12]   (-0.23, 0.09)           True
65         8    5  hfb  171   0.617    [0.45, 0.91]     (0.6, 1.05)           True
66         8    6  lfb  193  -0.047    [-0.2, 0.11]   (-0.18, 0.11)           True
67         8    6  hfb  193   0.257    [0.12, 0.38]     (0.4, 0.71)          False
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
p='ajile.py'; s=open(p).read()
a='''def run_regression(jobs, workers=4):
    """Runs the jobs largest first (events x models), so that the workers finish together, and
    returns the rows in the order of the jobs. Each job has its own generators, so the order
    does not change a result."""'''
b='''def run_regression(jobs, workers=4, per_job=False):
    """Runs the jobs largest first (events x models), so that the workers finish together, and
    returns the rows in the order of the jobs (a list of rows per job with per_job). Each job has
    its own generators, so the order does not change a result."""'''
assert s.count(a)==1; s=s.replace(a,b)
a='''    return [r for i in range(len(jobs)) for r in res[i]]'''
b='''    if per_job:
        return [res[i] for i in range(len(jobs))]
    return [r for i in range(len(jobs)) for r in res[i]]'''
assert s.count(a)==1; s=s.replace(a,b)
open(p,'w').write(s)

import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
s97=''.join(C[97]['source'])
a=s97[s97.find('print("main fits:"'):]
b='''print("main fits:", fig6_summary(MAIN))
# All variant fits run in one pool, largest jobs first; each job keeps its own generators, so this
# gives the same fits as running each variant on its own.
t = time.time()
top = MAIN[MAIN.r2 > 0.03][["subject", "electrode"]].drop_duplicates()
print("models refit per variant:", len(top), "electrodes, both bands")
# Seeds: the splits and shuffles of the claim's seed + 1000 ... + 4000
VJOBS = {f"seed + {off}": variant_jobs(JOBS, top, seed=REG_SEED + off) for off in SEED_OFFSETS[1:]}
# log(onset speed + 1) as the code encodes it (claims file, opening comment)
VJOBS["log"] = variant_jobs(regression_jobs(REG_SEED, log_speed=True), top)
# Bad electrodes included, as the code fits them (claims file, opening comment): the main fits plus
# the electrodes bad in at least one file of the subject
JOBS_BAD = regression_jobs(REG_SEED, include_bad=True)
extra = []
for j in JOBS_BAD:
    k = ~j["good_all"][j["electrodes"]]
    jj = dict(j); jj["Y"] = j["Y"][:, k][:, :, :2]; jj["electrodes"] = j["electrodes"][k]
    jj["targets"] = ["lfb_mean", "hfb_mean"]; jj["variant"] = True
    extra.append(jj)
VJOBS["bad"] = [j for j in extra if len(j["electrodes"])]
flat = [(key, j) for key, js in VJOBS.items() for j in js]
VR = {}
for (key, _), rows in zip(flat, ajile.run_regression([j for _, j in flat], workers=4, per_job=True)):
    VR.setdefault(key, []).extend(rows)
VR = {key: pd.DataFrame(rows).assign(band=lambda d: d.target.str[:3]) for key, rows in VR.items()}
print(f"variant fits {time.time() - t:.0f} s")
sens = {}
for off in SEED_OFFSETS[1:]:
    R = VR[f"seed + {off}"]
    sens[off] = R
    print(f"seed + {off}: largest R2 {R.r2.max():.4f};", fig6_summary(R))
'''
C[97]['source']=s97.replace(a,b).splitlines(keepends=True)
C[98]['source']='''R_log = VR["log"]
print("log(onset speed + 1): largest R2", round(R_log.r2.max(), 4), ";", fig6_summary(R_log))
print("electrodes bad in at least one file with finite power:", {j["subject"]: len(j["electrodes"]) for j in extra},
      "; dropped for non-finite power:", {j["subject"]: j["dropped_nonfinite"] for j in JOBS_BAD})
R_bad = VR["bad"]
R_all = pd.concat([MAIN[["subject", "electrode", "band", "r2", "coef", "delta"]], R_bad[["subject", "electrode", "band", "r2", "coef", "delta"]]])
print("bad electrodes: models with R2 > 0.05 among them", R_bad.groupby("band").r2.apply(lambda x: int((x > 0.05).sum())).to_dict(),
      "; largest R2", round(R_bad.r2.max(), 4))
print("all electrodes (main + bad):", fig6_summary(R_all))
'''.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print(''.join(C[97]['source'])[:1500])
EOF
grep -n "run_variant\|R_log\|R_bad\|sens\[" reproduce_peterson_2021.ipynb | cut -c1-150
```

```
# Variants of the Figure 6 models. Each refits the models with R2 > 0.03 under the main fits (all
# models that pass 0.05 come from these), with the Methods' 90/10 splits and Delta R2 where R2 > 0.05.
def fig6_summary(df):
    """Per band: models with R2 > 0.05, the two features with the largest median Delta R2
    (fig6c), the median reach angle coefficient (fig6d-upward) and the two largest median
    coefficient magnitudes (fig6d-largest, reading a)."""
    out = {}
    for band in ("lfb", "hfb"):
        M = df[(df.band == band) & (df.r2 > 0.05)]
        D = pd.DataFrame([d for d in M.delta if isinstance(d, dict)]).median().sort_values(ascending=False)
        if len(M) == 0:
            out[band] = dict(n=0)
            continue
        Cf = pd.DataFrame(list(M.coef))
        ca = Cf.abs().median().sort_values(ascending=False)
        out[band] = dict(n=len(M), top_delta=list(D.index[:2]), angle_coef=round(float(Cf.angle.median()), 3),
                         top_coef=list(ca.index[:2]))
    return out
def variant_jobs(jobs0, models, **kw):
    jobs = []
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
s=''.join(C[97]['source'])
a='''def run_variant(jobs):
    R = pd.DataFrame(ajile.run_regression(jobs, workers=4))
    R["band"] = R.target.str[:3]
    return R
'''
assert s.count(a)==1
C[97]['source']=s.replace(a,'').splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
date -u
```

```
Wed Nov 25 13:10:39 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [32,38,48,51,54,57,62,65,68,71,74]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 32
**Result: partially reproduced.** Most reaches last under 2 s (88 to 95% per subject, 91.8% pooled)
and cover under 200 pixels (59 to 100% per subject, 91.3% pooled), in all 12 subjects. The angle
part fails: the density of the folded angle has its two highest maxima within 15 degrees of -90 and
+90 with a lower density at 0 in none of the 12 subjects and not pooled. Pooled, the maxima are at
-71.5 and +75 degrees, and the density at 0 (0.00407) is above the lower maximum (0.004). The
density at +75 degrees is above that at +90 in every subject, which the kernel's smoothing at the
boundary can cause; but only 6.4% of events lie within 15 degrees of -90 (19.7% of +90), and pooled
the density at -75 degrees (0.00395) is below that at 0. Reading (a) gives the same outcome.
===== 38
**Result: reproduced.** In all 12 subjects, under both readings of the rest position, the peak of the
median contralateral displacement over 0 to 1.5 s exceeds that of the ipsilateral wrist; the ratio
is 1.06 to 42.0 (reading b, smallest for S05 and S04, which move both arms most).
===== 48
**Result: reproduced.** In precentral, postcentral and inferior parietal regions the masked group
power over 4-30 Hz is below 0 and over 50-120 Hz above 0, both over 0 to 0.5 s (for example
precentral -0.728 and 0.411 dB) and at the bin of 0 s, under all five seeds. Middle frontal shows
the same pattern; in supramarginal and the temporal regions the masked high-frequency values are at
most 0.008 dB. With each file's own good-electrode flags (variant) all three named regions hold too.
===== 51
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][0]['source'])[-900:])
print('=====');print(''.join(nb['cells'][77]['source']))
EOF
```

```
reproduced |
| discussion-day-changes-small | yes | reproduced |
| fig6b-best-models-sensorimotor | yes | reproduced |
| fig6-r2-at-most-025 | yes | reproduced |
| fig6c-angle-and-day-most-informative | yes | reproduced |
| extfig6-2-angle-most-retained | yes | partially reproduced |
| fig6d-upward-reaches-enhance-pattern | yes | reproduced |
| fig6d-angle-and-day-largest-coefficients | yes | reproduced |

Assumptions (the paper leaves these open; each is stated where it is used): how the segment
rejection pools power over electrodes and frequencies; and that the good electrodes of a subject are
those marked good in every one of its files, for the segment rejection, the region projection, the
regression and the electrode-level analyses (the claims file's opening comment renormalises the
weights per subject). The flags of each event's own file are shown as a variant for the region claims.
=====
## Regression models (Figure 6)

One model per subject, electrode and band, on the events of reading (b). Electrodes are those good
in every file of the subject (the Methods remove bad electrodes; the flags differ between files, see
the data check). Ten features as the Methods and code encode them; forward selection over single
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:50]); setsrc(i,s.replace(a,b))

rep(0,'''The notebook runs for about 40 minutes: about 10 minutes to stream the ECoG around 8088 events
(about 150 GB of compressed chunks), about 17 minutes for the 3904 regression models and about 9
minutes for the regression variants.''','''The notebook runs for about an hour: about 10 to 13 minutes to stream the ECoG around 8088 events
(about 150 GB of compressed chunks), about 35 minutes for the 3904 regression models and about 10
to 15 minutes for the regression variants. The last cell prints the time of the run.''')
rep(0,'''weights per subject). The flags of each event's own file are shown as a variant for the region claims.''','''weights per subject). For the region claims two other electrode choices are shown as variants: the
flags of each event's own file, and the electrodes good in at least one file of the subject. The
paper's count of removed electrodes favours each file's own flags (section "Region results under
other electrode choices"), and under it fig5-recording-day-effects would be partially reproduced;
that change of outcome is proposed for review.''')
rep(38,''' (reading b, smallest for S05 and S04, which move both arms most).''',''' (reading b; smallest for S05 and S04, 1.06 to 1.30, a margin the criterion does not judge).''')
rep(48,'''With each file's own good-electrode flags (variant) all three named regions hold too.''','''All three named regions hold too under each of the three electrode variants (section below): each
file's own flags, removing only the electrodes bad in every file, and leaving out the electrodes with
50 ms runs of zeros.''')
rep(51,'''The variant with each file's flags gives
the same under all three readings.''','''Each of the three electrode variants
(section below) gives the same under all three readings.''')
rep(54,'''The variant with each file's flags
gives 7 against 8 and 34.6 against 24.0, the same disagreement.''','''The electrode variants
(section below) give the same disagreement: 7 against 8 and 34.6 against 24.0 with each file's flags,
8 against 8 and 35.0 against 25.2 removing only the electrodes bad in every file, 8 against 8 and 36.6
against 22.1 without the zero-run electrodes.''')
rep(57,'''With each file's own flags
(variant) parts 2 to 4 hold and part 1 fails for S09 only.''','''The electrode variants (section
below) give: with each file's own flags parts 2 to 4 hold (S04, S07 and S08 at 2 bins) and part 1
fails for S09 only (-0.030 dB), partially reproduced; removing only the electrodes bad in every file
all four parts hold, which would be reproduced; without the zero-run electrodes two parts hold, and
S09 still has a negative mean over 76-100 Hz (-0.029 dB), so its 50 ms runs of zeros do not explain
its failure of part 1. The paper's count of removed electrodes favours each file's flags (section
below), which give the same outcome as the main analysis.''')
rep(62,'''(Kruskal-Wallis H = 740 to 1028, p below the smallest double).''','''(Kruskal-Wallis H = 740 to 1028, p below the smallest double), and under every electrode variant
(band mean H = 740 to 1089, section below).''')
rep(65,'''With each file's own flags (variant) the mean of the
band mean puts 21 of 24 inside.''','''The electrode variants (section below) give at best 21 of 24
(each file's flags, mean of the band mean), 22 of 24 (removing only the electrodes bad in every file,
mean of the band mean) and 18 of 24 (without the zero-run electrodes, median of the band median),
partially reproduced in each.''')
setsrc(68,'''**Result: not reproduced.** With band means 18 of 24 subject and band pairs agree with the paper, and
18 with band medians, below the 20 the criterion asks. The day effect is significant where the paper
finds none for S01 LFB (p = 0.043), S01 HFB (p = 0.022) and S06 HFB (p = 6.9e-11), and not
significant for S07 HFB (p = 0.073), S08 LFB (p = 0.31) and S10 HFB (p = 0.054), where the paper
finds one. The day medians of the band mean lie inside Table 2's per-day intervals for 41 of 55
subject-days in LFB and 42 of 55 in HFB.

The outcome rests on the choice of good electrodes, and the other choices give partially reproduced
(section "Region results under other electrode choices"): each file's own flags give 20 of 24 (band
mean) and 19 (band median), and removing only the electrodes bad in every file gives 21 and 20.
Leaving out the electrodes with 50 ms runs of zeros gives 18 and 18; S10 HFB keeps p = 0.054 under
it, so the zeros do not explain that pair. The paper's count of removed surface electrodes (4.9 +- 4.9
per subject) is closest to each file's flags (4.2 +- 2.1), against 12.6 +- 8.4 for the main set and
1.2 +- 0.4 removing only the electrodes bad in every file (data check). The outcome stays as verified
in round 2, and a change to partially reproduced is proposed for a third round.
''')
setsrc(74,src(74).replace('''(1.49 dB with each file's flags too)''','''(1.49 dB under each electrode variant too)'''))
assert '1.49 dB under each electrode variant' in src(74)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
assert ''.join(C[76]['source']).startswith('VARIANTS')
cell={"cell_type":"markdown","metadata":{},"source":'''**Electrode choice, and the change proposed for fig5-recording-day-effects.** The Methods ("ECoG
data processing") remove "4.9 +- 4.9 surface electrodes per subject and 1.0 +- 1.4 depth electrodes
for each of the five subjects with depth electrodes". The data check counts the surface electrodes
each choice removes: 12.6 +- 8.4 per subject for the main set (electrodes bad in any file removed),
4.2 +- 2.1 for each file's own flags (mean over a subject's files), and 1.2 +- 0.4 when only the
electrodes bad in every file are removed. Each file's flags are closest to the paper's count. No
choice matches the depth count (8.1, 4.7 and 3.1 against 1.0), mostly because S03's 16 depth
electrodes, which have no position, are bad in every file.

Under each file's flags fig5-recording-day-effects has 20 of 24 pairs agreeing (band mean), and
removing only the electrodes bad in every file gives 21; both are partially reproduced under the
criterion. Only the main set gives 18. The other region claims keep their outcomes under each file's
flags (fig3 group pattern and sensorimotor regions reproduced, the widespread readings still
disagree, fig4 three of four parts, band power differs across subjects, Table 1 21 of 24, day changes
at most 1.49 dB). Removing only the electrodes bad in every file would make fig4 reproduced (four of
four parts), but that choice removes far fewer electrodes than the paper reports. The regression
claims were not refit under each file's flags. The outcome of fig5-recording-day-effects is kept as
verified in round 2, and partially reproduced is proposed, resting on each file's own flags as the
choice best supported by the paper's count.
'''.splitlines(keepends=True)}
C.insert(77,cell)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
s=''.join(C[77]['source'])
a='''criterion. Only the main set gives 18.'''
b='''criterion. Each file's flags change the electrodes from day to day, which can add or hide day
effects; removing only the electrodes bad in every file keeps them the same, as the main set does.
Only the main set gives 18.'''
assert s.count(a)==1
C[77]['source']=s.replace(a,b).splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
for i in range(len(C)):
    if ''.join(C[i]['source']).startswith('## Summary'): print('summary at', i)
EOF
```

```
summary at 100
```

**Agent**

Now the summary cell.

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
i=100
s=''.join(C[i]['source'])
reps=[
('| fig2-reach-shape | partially reproduced (no angle density peaks within 15 degrees of +-90) |',
 '| fig2-reach-shape | partially reproduced (the angle density has no maximum within 15 degrees of -90 in any subject, and its density at 0 is above the lower maximum pooled) |'),
('| fig4-precentral-subject-variability | partially reproduced (2 of 4 parts; S09 has no HFB increase, S04 and S08 tied for the narrowest decrease) |',
 '| fig4-precentral-subject-variability | partially reproduced (2 of 4 parts; S09 has no HFB increase, and S07 and S09 have the narrowest decrease at 2 bins, with S04 and S08 among six subjects at 3) |'),
('| fig5-recording-day-effects | not reproduced (18 of 24; 20 with each file\'s own electrode flags) |',
 '| fig5-recording-day-effects | not reproduced (18 of 24; 20 with each file\'s own electrode flags and 21 removing only the electrodes bad in every file; partially reproduced is proposed) |'),
('''the electrodes good in every file of the subject are used throughout (an assumption), and each
file's own flags are shown as a variant for the region claims. That choice decides
fig5-recording-day-effects (18 of 24 pairs agree with it, 20 with each file's flags).''',
'''the electrodes good in every file of the subject are used throughout (an assumption). For the
region claims, each file's own flags, the electrodes good in at least one file, and the main set
without electrodes holding 50 ms runs of zeros are shown as variants. The choice decides
fig5-recording-day-effects (18 of 24 pairs agree with the main set, 20 with each file's flags, 21
with the electrodes good in at least one file), and the paper's count of removed surface electrodes
(4.9 +- 4.9) is closest to each file's flags (4.2 +- 2.1, against 12.6 +- 8.4 for the main set), so
a change of that outcome to partially reproduced is proposed. Removing only the electrodes bad in
every file would also make fig4-precentral-subject-variability reproduced.'''),
('''- In S09 and S10 every analysed event has, on at least one electrode marked good in every file, a
  run of at least 25 exact zero samples (50 ms) in its 10 s segment; no electrode's wavelet power
  becomes infinite in the analysis window.''',
'''- In S09 and S10 every analysed event has, on at least one electrode marked good in every file, a
  run of at least 25 exact zero samples (50 ms) in its 10 s segment; no electrode's wavelet power
  becomes infinite in the analysis window. Leaving those electrodes out of each event changes no
  outcome: S09 still has no HFB increase in the precentral region, S10's HFB day effect keeps
  p = 0.054, and S09's onset and pseudo-onset power still do not differ (p = 0.84 and 0.87).'''),
]
for a,b in reps:
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
C[i]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='reproduce_peterson_2021.ipynb'
nb=json.load(open(p)); C=nb['cells']
s=''.join(C[100]['source'])
a='(the angle density has no maximum within 15 degrees of -90 in any subject, and its density at 0 is above the lower maximum pooled)'
b='(in no subject is either of the two highest maxima of the angle density within 15 degrees of -90; pooled, the density at 0 is above the lower maximum)'
assert s.count(a)==1; C[100]['source']=s.replace(a,b).splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd  date -u; grep -n "40 minutes\|runtime_minutes" entries/peterson-2021/README.md entries/peterson-2021/entry.yaml
```

```
Wed Nov 25 13:11:57 UTC 2026
entries/peterson-2021/README.md:40:The notebook runs for about 40 minutes. The attempt record, with the reasons and the differences
entries/peterson-2021/entry.yaml:15:  runtime_minutes: 40
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -i 's/  runtime_minutes: 40/  runtime_minutes: 60/' entry.yaml; sed -i 's/^The notebook runs for about 40 minutes\. /The notebook runs for about an hour. /' README.md; sed -i 's/^| Recording-day effects per subject | Not reproduced |$/| Recording-day effects per subject | Not reproduced (partially reproduced is proposed for review) |/' README.md; grep -n "hour\|Recording-day" README.md; grep -n runtime entry.yaml; cd ../..; date -u; python tools/entry.py all entries/peterson-2021 2>&1 | tail -6; date -u
```

```
27:| Recording-day effects per subject | Not reproduced (partially reproduced is proposed for review) |
40:The notebook runs for about an hour. The attempt record, with the reasons and the differences
15:  runtime_minutes: 60
Wed Nov 25 13:12:02 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
took 64 minutes; the limit is 60
0 error(s)
FAIL  reproduce_peterson_2021.ipynb  (3821 s)
Wed Nov 25 14:15:54 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        for l in t.splitlines():
            if (' s' in l and ('pass' in l or 'regression ' in l or 'variant fits' in l)) or 'run time' in l: print(i,l[:200])
    if c['metadata'].get('execution',{}): pass
for i in [97,98,99]:
    c=nb['cells'][i]
    print(i, ''.join(''.join(o.get('text','')) for o in c['outputs'])[:3000])
EOF
```

```
Exit code 1
11 spectral pass 656 s; peak memory of a worker 1.69 GB
79 regression 2109 s, 3904 models
98 variant fits 886 s
101 notebook run time 63.5 min; peak memory of this process 2.10 GB
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
KeyError: 'outputs'
```

**Agent calls Bash**

```bash
cd  cat executed/peterson-2021/result.json; echo; grep -n "max.minutes\|max_minutes" tools/entry.py | head; grep -n "r2_80\|median" entries/peterson-2021/reproduce_peterson_2021.ipynb | grep -v "nanmedian\|np.median\|\.median()" | head -20
```

```
{
 "entry": "peterson-2021",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_peterson_2021.ipynb",
   "ok": false,
   "seconds": 3821,
   "error": "took 64 minutes; the limit is 60"
  }
 ]
}

29:that takes longer than --max-minutes fails, even if it ran without error.
525:                   max_minutes: float) -> int:
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
578:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cp executed/peterson-2021/reproduce_peterson_2021.ipynb $TMPDIR/run2_backup.ipynb; grep -n "r2_80\|_median\"\]\|lfb_median\|MED\b" entries/peterson-2021/reproduce_peterson_2021.ipynb | head; python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][81]['source'])); print(''.join(''.join(o.get('text','')) for o in nb['cells'][81]['outputs']))
EOF
```

```
1151:    "SUBJ_MED = np.stack([np.nanmedian(REG_BS[kbv & (subj_v == s)], axis=0) for s in subjects])  # (subj, roi, f, b)\n",
1152:    "GROUP = SUBJ_MED.mean(axis=0)\n",
1166:    "    subj_med = SUBJ_MED if subj_med is None else subj_med\n",
1410:    "parts4, p1, width = fig4_parts(SUBJ_MED)\n"
1457:    "print(EVB[[\"pre_lfb_mean\", \"pre_hfb_mean\", \"pre_lfb_median\", \"pre_hfb_median\", \"pre_raw_lfb_mean\", \"pre_raw_hfb_mean\"]].describe().round(3).to_string())"
1915:    "                      for k in (\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\")], axis=-1)\n",
1920:    "                         electrodes=np.flatnonzero(use)[finite], targets=[\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\"],\n",
1959:    "print(\"largest with 80/20 splits:\", MAIN.r2_80.max().round(4), \"; with band median:\", REGR[REGR.target.str.endswith(\"median\")].r2.max().round(4))\n",
1961:    "print(\"ten largest:\"); print(MAIN.nlargest(10, \"r2\")[[\"subject\", \"electrode\", \"band\", \"r2\", \"r2_80\"]].round(4).to_string())"
mx = MAIN.r2.max(); row = MAIN.loc[MAIN.r2.idxmax()]
print(f"largest split-averaged withheld R2 (90/10, band mean): {mx:.4f} (S{row.subject:02d}, electrode {row.electrode}, {row.band})")
print("largest with 80/20 splits:", MAIN.r2_80.max().round(4), "; with band median:", REGR[REGR.target.str.endswith("median")].r2.max().round(4))
print("models with R2 > 0.05:", MAIN.groupby("band").r2.apply(lambda x: int((x > 0.05).sum())).to_dict(), "of", MAIN.groupby("band").size().to_dict())
print("ten largest:"); print(MAIN.nlargest(10, "r2")[["subject", "electrode", "band", "r2", "r2_80"]].round(4).to_string())
largest split-averaged withheld R2 (90/10, band mean): 0.1770 (S07, electrode 10, hfb)
largest with 80/20 splits: 0.1839 ; with band median: 0.1578
models with R2 > 0.05: {'hfb': 14, 'lfb': 14} of {'hfb': 976, 'lfb': 976}
ten largest:
      subject  electrode band      r2   r2_80
1845        7         10  hfb  0.1770  0.1839
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
C=nb['cells']
def out(i): return ''.join(''.join(o.get('text','')) for o in C[i].get('outputs',[]))
t=out(4); print(t[t.find('  bad in any'):t.find('columns of the reaches')])
t=out(13); print(t[t.find('S09 without'):t.find('median contra')])
t=out(67); print(t[t.find('pairs agreeing'):t.find('pairs agreeing')+90], t[-90:])
print(out(77)[:200] if C[77]['cell_type']=='code' else 'md77')
print(out(76)[-3500:])
for i in [81,84,87,90,93,96,98,99]:
    print(i, out(i)[:1500])
EOF
```

```
bad in any file: surface 12.6 +- 8.4 per subject (paper 4.9 +- 4.9); depth 8.1 +- 6.5 over the 7 subjects with depth groups (paper 1.0 +- 1.4)
  bad in every file: surface 1.2 +- 0.4 per subject (paper 4.9 +- 4.9); depth 3.1 +- 6.0 over the 7 subjects with depth groups (paper 1.0 +- 1.4)
  each file's flags (mean over files): surface 4.2 +- 2.1 per subject (paper 4.9 +- 4.9); depth 4.7 +- 5.7 over the 7 subjects with depth groups (paper 1.0 +- 1.4)

S09 without zero-run electrodes: LFB onset -0.1156 vs pseudo -0.1063 (p = 0.843); HFB onset 0.0171 vs pseudo -0.1188 (p = 0.871)
S10 without zero-run electrodes: LFB onset -0.3005 vs pseudo 0.0570 (p = 1.91e-10); HFB onset 0.0945 vs pseudo -0.0035 (p = 0.00696)

pairs agreeing, band mean: 18 of 24; band median: 18 of 24
     subject  day band    n  me side Table 2's interval: {'hfb': {'sum': 42, 'size': 55}, 'lfb': {'sum': 41, 'size': 55}}

md77
fb'): 0.0721, ('S09', 'hfb'): 0.281, ('S10', 'lfb'): 0.274, ('S10', 'hfb'): 0.0935}
discussion: largest day deviation 1.487 dB
=== removing only electrodes bad in every file (any)
fig3-group: named regions holding under a: 3 ; under b: 3 {'low_a': {'precentral': -0.79, 'postcentral': -0.79, 'inferior parietal': -0.603}, 'high_a': {'precentral': 0.482, 'postcentral': 0.493, 'inferior parietal': 0.272}}
fig3-sensorimotor: {'a_all_0_0.5': (True, 3, True), 'c_all_-0.5_0.5': (True, 3, True), 'b': (True, 3, True)}
fig3-lfb-more-widespread: (a) (8, 8) ; (b) [35.    25.214] ; supramarginal / superior temporal: {'supramarginal': 30, 'superior temporal': 26}
fig4: parts holding 4 of 4 [True, True, True, True] ; subjects without the part 1 pattern: [] {} ; part 4 widths: {'S01': 5, 'S02': 5, 'S03': 3, 'S04': 2, 'S05': 3, 'S06': 4, 'S07': 2, 'S08': 2, 'S09': 6, 'S10': 4, 'S11': 4, 'S12': 4}
fig5-band-power: H (band mean) LFB 760.3 HFB 1089.2
table1: inside, four readings {'mean_of_bandmean': np.int64(22), 'mean_of_bandmedian': np.int64(20), 'median_of_bandmean': np.int64(21), 'median_of_band
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for p in ['entries/peterson-2021/reproduce_peterson_2021.ipynb','executed/peterson-2021/reproduce_peterson_2021.ipynb']:
    nb=json.load(open(p))
    miss=[i for i,c in enumerate(nb['cells']) if 'id' not in c]
    print(p, miss, nb['nbformat'], nb['nbformat_minor'])
    for i in miss:
        assert ''.join(nb['cells'][i]['source']).startswith('**Electrode choice')
        nb['cells'][i]['id']='electrode-choice-proposal'
    json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python tools/entry.py check entries/peterson-2021 2>&1 | tail -5
```

```
entries/peterson-2021/reproduce_peterson_2021.ipynb [77] 4 5
executed/peterson-2021/reproduce_peterson_2021.ipynb [] 4 5
0 error(s)
```

**Agent calls Bash**

```bash
cd  head -c 1500 transcripts/peterson-2021/verifier-2.md; echo; grep -n "date:" attempts/peterson-2021-02.yaml
```

````
# peterson-2021 · verifier-2 · run 45595469096

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 604
drwxr-xr-x 6 runner runner    4096 Nov 25 11:42 .
drwxr-xr-x 8 runner runner    4096 Nov 25 11:42 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 10:28 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 10:28 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 25 11:42 .claude
-rw-r--r-- 1 runner runner       0 Nov 25 11:42 .env
-rw-r--r-- 1 runner runner       0 Nov 25 11:42 .env.development
-rw-r--r-- 1 runner runner       0 Nov 25 11:42 .env.development.local
[... 11 more lines not kept]
````

**Agent**

Now writing the record updates.

**Agent calls Bash**

```bash
cd  date -u; python - <<'EOF'
p='attempts/peterson-2021-02.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)

# fig3-group deviations: electrode set
rep('''    weights are renormalised to sum 1 per region (code). The flags of each event's own file, the
    assumption of round 1, are shown as a variant for every region claim.''','''    weights are renormalised to sum 1 per region (code). Three variants are shown for every region
    claim, on the same events; the flags of each event's own file (the assumption of round 1), the
    electrodes good in at least one file (only those bad in every file removed), and the main set
    with the electrodes holding a 50 ms run of zeros left out of each event. The main set removes
    12.6 +- 8.4 surface electrodes per subject, each file's flags 4.2 +- 2.1 and the electrodes bad
    in every file 1.2 +- 0.4, against the paper's 4.9 +- 4.9 (Methods, ECoG data processing).''')
rep('''  notes: Over 0 to 0.5 s the masked group power over 4-30 Hz and 50-120 Hz is -0.728 and +0.411 dB in
    precentral, -0.743 and +0.426 in postcentral, and -0.556 and +0.200 in inferior parietal; at the
    bin of 0 s the signs are the same. All three hold under both readings, all five seeds, unmasked,
    and with each file's own good-electrode flags (variant).''','''  notes: Over 0 to 0.5 s the masked group power over 4-30 Hz and 50-120 Hz is -0.728 and +0.411 dB in
    precentral, -0.743 and +0.426 in postcentral, and -0.556 and +0.200 in inferior parietal; at the
    bin of 0 s the signs are the same. All three hold under both readings, all five seeds, unmasked,
    and under each of the three electrode variants.''')
rep('''0.429, 0.418 and 0.251 dB for the three, 0.177 for middle frontal, and at most 0.034 for the
    temporal regions. The variant with each file's flags gives the same under all three readings.''','''0.429, 0.418 and 0.251 dB for the three, 0.177 for middle frontal, and at most 0.034 for the
    temporal regions. Each of the three electrode variants gives the same under all three readings.''')
rep('''bins) have significant low-frequency decreases. With each file's flags (variant) the readings
    give 7 against 8 and 34.6 against 24.0, the same disagreement.''','''bins) have significant low-frequency decreases. The electrode variants give the same
    disagreement; 7 against 8 and 34.6 against 24.0 with each file's flags, 8 against 8 and 35.0
    against 25.2 with the electrodes good in at least one file, 8 against 8 and 36.6 against 22.1
    without the zero-run electrodes.''')
rep('''other 11 subjects show the pattern. With each file's own flags (variant), parts 2 to 4 hold and
    part 1 fails for S09 only, also partially reproduced.''','''other 11 subjects show the pattern. With each file's own flags (variant), parts 2 to 4 hold and
    part 1 fails for S09 only (-0.030 dB), also partially reproduced. With the electrodes good in at
    least one file all four parts hold, which would be reproduced, but that set removes 1.2 surface
    electrodes per subject against the paper's 4.9; each file's flags are closest to the paper's
    count. Without the electrodes holding 50 ms runs of zeros two parts hold and S09 stays at -0.029
    dB over 76-100 Hz, so the zeros do not explain its failure of part 1.''')
rep('''    With each file's flags, H = 747 and 1052.''','''    Under the three electrode variants, H = 740 to 760 (LFB) and 1028 to 1089 (HFB).''')
rep('''own flags (variant) the mean of the band mean puts 21 of 24 inside. The attempt's own
    5000-replicate bootstrap intervals are printed beside the paper's.''','''own flags (variant) the mean of the band mean puts 21 of 24 inside, with the electrodes good in
    at least one file 22 of 24, and without the zero-run electrodes at best 18 of 24; partially
    reproduced under each. The attempt's own 5000-replicate bootstrap intervals are printed beside
    the paper's.''')
rep('''  notes: With band means 18 of 24 subject and band pairs agree with the paper, and 18 with band
    medians, below the 20 the criterion asks for a partial reproduction. A day effect is found where
    the paper has none for S01 LFB (p = 0.043), S01 HFB (p = 0.022) and S06 HFB (p = 6.9e-11), and is
    not found for S07 HFB (p = 0.073), S08 LFB (p = 0.31) and S10 HFB (p = 0.054), where the paper
    reports one. The other eight significant pairs of the paper are significant here. The outcome
    rests on the choice of good electrodes; with each file's own flags (variant, the main analysis
    of round 1) 20 of 24 agree, which would be partially reproduced. S01 lost 132 events of day 7,
    where its ECoG ends early.''','''  notes: With band means 18 of 24 subject and band pairs agree with the paper, and 18 with band
    medians, below the 20 the criterion asks for a partial reproduction. A day effect is found where
    the paper has none for S01 LFB (p = 0.043), S01 HFB (p = 0.022) and S06 HFB (p = 6.9e-11), and is
    not found for S07 HFB (p = 0.073), S08 LFB (p = 0.31) and S10 HFB (p = 0.054), where the paper
    reports one. The other eight significant pairs of the paper are significant here. The outcome
    rests on the choice of good electrodes. With each file's own flags (variant, the main analysis
    of round 1) 20 of 24 agree with band means and 19 with band medians; with the electrodes good in
    at least one file 21 and 20; both would be partially reproduced. Without the electrodes holding
    50 ms runs of zeros 18 and 18, and S10 HFB keeps p = 0.054. The day medians of the band mean lie
    inside Table 2's per-day intervals for 41 of 55 subject-days in LFB and 42 of 55 in HFB. S01
    lost 132 events of day 7, where its ECoG ends early.''')
rep('''  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: extfig5-1-baseline-reduces-day-variability''','''  proposed:
    outcome: partially_reproduced
    reason: The main set of good electrodes (good in every file) removes 12.6 +- 8.4 surface
      electrodes per subject, against the paper's 4.9 +- 4.9 (Methods, ECoG data processing); each
      file's own flags remove 4.2 +- 2.1, closest to the paper, and give 20 of 24 agreeing pairs with
      band means, at the criterion's threshold for a partial reproduction. Removing only the
      electrodes bad in every file (1.2 +- 0.4), which keeps the electrodes the same across days,
      gives 21. Only the main set gives fewer than 20 (18). The other region claims keep their
      outcomes under each file's flags. Analysis in the notebook, section "Region results under
      other electrode choices" and the cell after it.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
  - The paper's per-day intervals (Table 2) are compared with the day medians of the band mean here,
    for comparison only; the criterion's count uses the Kruskal-Wallis tests.
- claim: extfig5-1-baseline-reduces-day-variability''')
rep('''subject and band is at most 2.2 dB (1.49 dB with each file's flags too)''','''subject and band is at most 2.2 dB (1.49 dB under each electrode variant too)''')
# findings
rep('''  statement: The `good` flags of the electrodes differ between the files of a subject (bad in at least
    one file 3 to 32 per subject, bad in every file 1 to 17), and nothing says how they were set or
    which applies to the subject's analyses. The paper reports 4.9 +- 4.9 surface electrodes removed
    per subject.''','''  statement: The `good` flags of the electrodes differ between the files of a subject (bad in at least
    one file 3 to 32 per subject, bad in every file 1 to 17), and nothing says how they were set or
    which applies to the subject's analyses. The paper reports 4.9 +- 4.9 surface electrodes removed
    per subject; the surface electrodes bad in at least one file number 12.6 +- 8.4 per subject, those
    bad in every file 1.2 +- 0.4, and those bad in a file 4.2 +- 2.1 on average over a subject's
    files.''')
rep('''    for sub-09 neither band differs, so the alignment could not be established there.''','''    for sub-09 neither band differs, so the alignment could not be established there, also with the
    electrodes holding 50 ms runs of zeros left out (p = 0.84 and 0.87).''')
rep('''    regression; with each day's own flags, the recording-day effects of 20 of 24 subject and band
    pairs agree with the paper, against 18.''','''    regression; with each day's own flags, the recording-day effects of 20 of 24 subject and band
    pairs agree with the paper, against 18, and removing only the electrodes bad on every day gives
    21. Each day's flags remove 4.2 surface electrodes per subject on average, the closest to the
    paper's 4.9.''')
rep('''    every file, a run of at least 25 exact zero samples (50 ms) within the 10 s around it; no other
    subject has such runs. The files do not say what the zeros mean.''','''    every file, a run of at least 25 exact zero samples (50 ms) within the 10 s around it; no other
    subject has such runs. The files do not say what the zeros mean. Leaving those electrodes out of
    each event changes no outcome of this attempt.''')
# round 1: problem 2
rep('''    reason: The minimum is 211 (reading a) and 210 (reading b) against 151 +- 15.1. The Methods keep
      only events lasting 0.5-4 s and the dataset's durations go down to 0.233 s, but this filter is
      not one of the criterion's readings; it would lower counts but is unlikely to bring S09 down to
      151.''','''    reason: The minimum is 211 (reading a) and 210 (reading b) against 151 +- 15.1. The Methods keep
      only events lasting 0.5-4 s and the dataset's durations go down to 0.233 s, but this filter is
      not one of the criterion's readings; it would lower counts but is unlikely to bring S09 down to
      151. Separately (problem 2, not affecting a conclusion), cell 4 prints a largest difference of
      86400 s between the ReachEvents timestamps and the reaches start_time and nobody follows it up;
      the ECoG and pose windows use the ReachEvents timestamps while time of day and duration use
      start_time, so some events were probably cut with ECoG from the wrong day, likely few.''')
open(p,'w').write(s)
EOF
```

```
Wed Nov 25 14:17:44 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat >> attempts/peterson-2021-02.yaml <<'EOF'
- date: '2026-11-25'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The full executed notebook of the first revision, with its conclusions and summary, the
    helper module, the claims file, the README and the attempt record, with the paper's full text under
    paper/. The record has no finding rated critical, so no finding was reviewed for its rating.
  results:
  - claim: subject-days
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: roi-projection-link
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome; the zero rows sit at the electrodes without positions, and shifting
      the rows lowers the fit in all 12 subjects (round-1 point 6 resolved).
    response: No change.
  - claim: cohort
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome; the grid-only variant was run (round-1 point 10 resolved).
    response: No change.
  - claim: fig2-event-counts
    agrees: true
    outcome: not_reproduced
    reason: Agrees with the outcome. The one mismatched event (S08 day 4) is now dropped from reading
      (b), and the 0.5-4 s filter was run as a variant (round-1 points 2 and 9 resolved). The record's
      round-1 reasons omitted problem 2 (the 86400 s timestamp mismatch).
    response: Added problem 2 to the round-1 reasons of this claim. Outcome unchanged.
  - claim: fig2-features-differ-across-subjects
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: fig2-reach-shape
    agrees: true
    outcome: partially_reproduced
    reason: The new density table (cell 30) supports the author. Pooled, only 6.4% of events lie within
      15 degrees of -90, below the 8.3% a uniform spread would give, so the -90 side fails for a
      reason other than the kernel's boundary effect. The Summary's "no angle density peaks within 15
      degrees of +-90" is not supported; cell 30 shows a peak at +75.0 pooled and in S01, which is
      exactly 15 degrees from +90 and counts as within under the code's test. The failure is on the
      -90 side and in the density at 0.
    response: Corrected the Summary row; in no subject is either of the two highest maxima within 15
      degrees of -90, and pooled the density at 0 is above the lower maximum. Outcome unchanged.
  - claim: fig2-bimanual-skew
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: extfig2-1c-contralateral-larger
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome. Cell 38's "S05 and S04, which move both arms most" is only loosely
      supported; cell 34 ranks S07's median bimanual ratio (0.308) above S05's (0.296).
    response: Removed the phrase; the conclusion now gives the ratios of S05 and S04 (1.06 to 1.30)
      only. Outcome unchanged.
  - claim: extfig2-2-feature-correlations
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: fig2-days-and-waking
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: fig3-group-lfb-decrease-hfb-increase
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome; the assumed segment-rejection pooling is stated and reasonable.
    response: Added two electrode variants (the electrodes good in at least one file, and the main
      set without electrodes holding 50 ms runs of zeros); the three named regions hold under each.
      Outcome unchanged.
  - claim: fig3-sensorimotor-largest
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: Same under the two added electrode variants. Outcome unchanged.
  - claim: fig3-lfb-more-widespread
    agrees: true
    outcome: blocked
    reason: Agrees with the outcome.
    response: The two added electrode variants give the same disagreement between the readings.
      Outcome unchanged.
  - claim: fig4-precentral-subject-variability
    agrees: true
    outcome: partially_reproduced
    reason: The choice of good electrodes moves fig4 from 3 to 2 parts; it stays partially reproduced
      either way. Part 4 now fails; S07 and S09 have 2 bins and six subjects, S04 and S08 among them,
      tie at 3, so only one place among the three fewest is left and counting this as a fail is
      reasonable. The Summary's "S04 and S08 tied for the narrowest decrease" is not supported. S09's
      part-1 failure may bear on its runs of zeros (round-1 problem 3, partly open).
    response: Corrected the Summary row. Ran the main set without the electrodes holding 50 ms runs of
      zeros; S09 stays at -0.029 dB over 76-100 Hz, so the zeros do not explain its failure. With the
      electrodes good in at least one file all four parts hold, but that set removes far fewer
      electrodes than the paper reports; each file's flags, closest to the paper's count, give three
      of four. Outcome unchanged.
  - claim: fig5-band-power-differs-across-subjects
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: Same under the two added electrode variants. Outcome unchanged.
  - claim: table1-subject-band-power-ci
    agrees: true
    outcome: partially_reproduced
    reason: The choice of good electrodes moves table1 from 21/24 to 18/24, exactly the partial
      threshold; it stays partially reproduced either way.
    response: With the electrodes good in at least one file the best reading puts 22 of 24 inside, and
      without the zero-run electrodes 18; partially reproduced under each. Outcome unchanged.
  - claim: fig5-recording-day-effects
    agrees: false
    reason: The outcome changed from round 1 only because the main analysis now uses the electrodes
      marked good in every file of a subject. The claims header's "renormalised to sum to 1 per
      subject" does not say which electrodes count as bad. Excluding every electrode bad in any file
      removes 3 to 32 per subject (mean about 17.3), against the paper's 4.9 +- 4.9 surface
      electrodes; removing only the electrodes bad in every file gives a mean of 3.0 (SD about 4.6),
      much closer, and is also per subject and keeps the electrode mix the same across days. That set
      was not run. The result is 18/24 under the chosen set and 20/24 under each file's flags, so the
      outcome flips on an open choice; undecided between partially and not reproduced until that set
      is run. The criterion also asks for Table 2's per-day intervals for comparison, and cell 67
      prints day means only. S10's HFB day effect (p = 0.054) may bear on its runs of zeros (round-1
      problem 3, partly open).
    response: Ran the electrodes good in at least one file (only those bad in every file removed); 21
      of 24 pairs agree with band means and 20 with band medians. Split into surface and depth, that
      set removes 1.2 +- 0.4 surface electrodes per subject, the main set 12.6 +- 8.4 and each file's
      flags 4.2 +- 2.1, against the paper's 4.9 +- 4.9, so each file's flags (20 of 24) are closest to
      the paper's count. Both choices give partially reproduced. As no outcome may change in round 2,
      not reproduced is kept and partially reproduced is proposed, with the analysis in the notebook.
      Added Table 2's per-day intervals beside the day medians (41 of 55 inside in LFB, 42 of 55 in
      HFB). Leaving out the electrodes with 50 ms runs of zeros keeps S10 HFB at p = 0.054.
  - claim: extfig5-1-baseline-reduces-day-variability
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: discussion-day-changes-small
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: The largest day deviation is 1.49 dB under each electrode variant too. Outcome unchanged.
  - claim: fig6b-best-models-sensorimotor
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome; the regression electrode set and the R2 > 0.03 refit rule for the
      variants are stated and reasonable. The leakage from forward selection is disclosed (round-1
      point 5 resolved). Cell 0 and the README say the notebook runs for about 40 minutes (17 for the
      regression, 9 for the variants), where cell 100 prints 63.5 min, the regression 2052 s and the
      variants 620 + 365 s.
    response: Corrected the run time in cell 0, the README and entry.yaml (about an hour); this run took
      63.5 minutes, 2109 s for the regression and 886 s for the variants, now run in one pool.
      Outcome unchanged.
  - claim: fig6-r2-at-most-025
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome; the seed, log(onset speed + 1) and bad-electrode variants were run
      (round-1 point 4 resolved).
    response: No change.
  - claim: fig6c-angle-and-day-most-informative
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome; Delta R2 and coefficients were refit under the variants (round-1
      point 4 resolved).
    response: No change.
  - claim: extfig6-2-angle-most-retained
    agrees: true
    outcome: partially_reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: fig6d-upward-reaches-enhance-pattern
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
  - claim: fig6d-angle-and-day-largest-coefficients
    agrees: true
    outcome: reproduced
    reason: Agrees with the outcome.
    response: No change.
EOF
python tools/entry.py check entries/peterson-2021 2>&1 | tail -5; python - <<'EOF'
import yaml,json,jsonschema
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
s=json.load(open('schemas/attempt.schema.json'))
jsonschema.validate(a,s); print('schema ok', len(a['verifications']), len(a['findings']))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml,json,jsonschema,datetime
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
def fix(o):
    if isinstance(o,dict): return {k:fix(v) for k,v in o.items()}
    if isinstance(o,list): return [fix(v) for v in o]
    if isinstance(o,datetime.date): return o.isoformat()
    return o
jsonschema.validate(fix(a),json.load(open('schemas/attempt.schema.json'))); print('schema ok')
for o in a['outcomes']:
    if o['claim']=='fig5-recording-day-effects': print(o['outcome'], o['proposed']['outcome'])
EOF
ls tools; grep -rn "attempts/" tools/*.py | grep -i "def \|check" | head -5
```

```
schema ok
not_reproduced partially_reproduced
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" attempts/peterson-2021-02.yaml entries/peterson-2021/README.md entries/peterson-2021/ajile.py; python - <<'EOF'
import json
nb=json.load(open('entries/peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if '—' in s or 'rather' in s: print(i)
EOF
python tools/entry.py check entries/peterson-2021; date -u
```

```
0 error(s)
Wed Nov 25 14:18:38 UTC 2026
```

**Agent**

I've finished the round-2 revision. No outcome changed. For fig5-recording-day-effects I kept the verified "not reproduced" and proposed "partially reproduced" for a third round.

**Re-run.** `python tools/entry.py all entries/peterson-2021` passed its checks with 0 errors, but the run is marked FAIL because it took 63.5 minutes against the 60-minute limit. Every cell ran without error. That is inside the 80 minutes the verifier's re-run and the PR checks allow, but over the target for my own run. The time goes to the 3904 regression models (2109 s, limited by the 4 CPUs). I did not cut any analysis to get under 60 minutes, and no `.clean-run.json` stamp was written. All earlier numbers came out the same. `entry.py check` passes, and the record validates against the schema.

**fig5-recording-day-effects.** I ran the electrode set the verifier asked for, which removes only the electrodes bad in every file. It gives 21 of 24 agreeing pairs with band means and 20 with band medians, so it would be partially reproduced. The main set gives 18 and each file's own flags give 20. I then counted removed electrodes, surface and depth separately, against the paper's 4.9 ± 4.9 surface electrodes per subject:

| Electrode set | Surface electrodes removed per subject | fig5 pairs agreeing (band mean) |
|---|---|---|
| Main: bad in any file removed | 12.6 ± 8.4 | 18 |
| Each file's own flags | 4.2 ± 2.1 | 20 |
| Only bad in every file removed | 1.2 ± 0.4 | 21 |

The verifier's figure of 3.0 for the last set included S03's 16 depth electrodes, which have no position. Each file's flags match the paper's count best, and both alternatives to the main set give partially reproduced. The proposal's reason and the analysis behind it are in a new notebook cell. The notebook now also compares the paper's Table 2 per-day intervals with this attempt's day medians, as the criterion asks: 41 of 55 subject-days fall inside in LFB and 42 of 55 in HFB.

**Other points from the report:**
- **Electrode variants for the region claims.** Every region claim is now shown under three variants: each file's flags, removing only the electrodes bad in every file, and the main set without electrodes holding 50 ms runs of zeros. No outcome changes. One thing to note: under "bad in every file only", fig4 would have all four parts hold and so be reproduced. That set removes far fewer electrodes than the paper reports, and each file's flags give 3 of 4, so I proposed nothing for fig4.
- **Runs of zeros in S09 and S10.** Leaving those electrodes out does not explain the open results:
  - S09 still has no HFB increase (−0.029 dB).
  - S10's HFB day effect stays at p = 0.054.
  - S09's onset and pseudo-onset power still do not differ (p = 0.84 and 0.87), so its alignment is still not established.
- **Sentences the numbers did not support.** I corrected all four:
  - the fig2-reach-shape row of the Summary;
  - the fig4 row of the Summary;
  - the "move both arms most" phrase in the fig2 contralateral-wrist conclusion (cell 38);
  - the run time in cell 0, the README and `entry.yaml`, now about an hour.
- **Round-1 record.** The verifier's problem 2 (the 86400 s timestamp mismatch) was missing from the stated reasons; I added it under fig2-event-counts.
- **Round 2 under `verifications`.** All 25 claims are recorded: 24 agree, and fig5 is recorded as not agreeing, with no outcome since the verifier left it undecided. There is no `findings` list because no finding is rated critical.
- **Findings.** I updated the text of four existing findings (good-electrode flags, the zeros, the checks that passed, and the question to the authors). Their order is unchanged and none was added.

**Code changes.** In the helper (`ajile.py`), the spectral pass now builds the extra electrode variants and records which electrodes hold runs of zeros. Regression jobs run largest first, and all variant fits run in one pool; neither change alters any number. I also added retries for the Figshare downloads, because a Figshare timeout stopped the first run attempt.

**Not done.** The regression claims were not refit with each file's flags; the verifier agreed with the regression's electrode set. No question was added to `questions/peterson-2021.yaml`, because the report names no place where the claims file misreads the paper. Nothing was committed.

## End of run

55 turns, 144 minutes, $7.37 at API prices, result: success.
