# peterson-2021 · reconcile · run 45647351295

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; grep -n "Repeat attempts" -A 80 docs/protocol.md | head -150
```

```
Wed Nov 25 15:44:01 UTC 2026
637:## Repeat attempts
638-
639-When a dataset changes after an attempt, for example after its owners fix
640-what an attempt found, or when the protocol changes, a new attempt tests the
641-dataset again. It is made blind: it is an attempt in its own right, not a
642-check of the one before it.
643-
644-- **Blind.** The author's runs (author, author-answers and each
645-  author-revise) see no earlier attempt on the dataset: not its record, entry,
646-  questions, transcripts or notes, and not the repository's history.
647-  `tools/blind.sh` takes them out of the checkout before each run and puts
648-  them back after it, and the run may not fetch the registry's website. The
649-  author keeps the claims file, unless the earlier attempt is deprecated and
650-  a reader wrote it again, and writes a new entry under the same name, a new
651-  notebook from scratch, and the record under the next number (`-02`). The
652-  verifiers see only this attempt, as always. Each finding is recorded as the
653-  attempt found it, with nothing about earlier attempts in its statement.
654-- **Reconcile.** Once the attempt is verified, a separate run, `reconcile`
655-  (`docs/agents/reconcile.md`), compares it with the attempt before it and
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/agents/reconcile.md 2>/dev/null | head -200; ls; ls entries/peterson-2021 earlier-entry attempts | head -50
```

```
You reconcile a repeat attempt in the reproduction registry, checked out in the current directory. Read docs/protocol.md, "Repeat attempts", first. Attempt `{attempt}` on paper `{key}` (data: {dataset}; entry `entries/{entry}`, dataset version {version}) was made blind: its author did not see `{earlier}` (made on version {earlier_version}). Its record is `attempts/{earlier}.yaml`. Its entry is `entries/{earlier_entry}` as it was when that record was last changed: `c=$(git log -1 --format=%H -- attempts/{earlier}.yaml)`, then `git show $c:entries/{earlier_entry}/<file>`. Both have been through their verification rounds. Your job is to say how the two compare, in a `reconciliation` block of `attempts/{attempt}.yaml` (its schema is in `schemas/attempt.schema.json`). Do not change the outcomes, statements or notes that the blind attempt recorded, its claims file or its notebooks.

1. Run `tools/blind.sh audit {folder}`. It prints the lines of this attempt's author transcripts that point at an earlier attempt. Read each in context. Set `blind: true` if the author never saw an earlier attempt's results, else `blind: false` with what it saw under `blind_note`.
2. For each finding of `{earlier}`, in order (`finding` is its number, from 1), decide whether one of `{attempt}`'s findings reports the same problem: the same files, fields or values, not only the same kind. If so, set `status` to `still_present` or `partly_fixed`, and `now` to that finding's number in `{attempt}`. If not, check the earlier finding directly on version {version}, in a new notebook `entries/{entry}/earlier_findings.ipynb` (add it to `entry.yaml`, one short section per finding, each opening with the earlier statement, and lock, check and run the entry). Then:
   - `fixed`, when the check shows the problem is gone;
   - `still_present`, when it is still there: add it to `{attempt}`'s findings with `found: on_prompt` and a statement in the protocol's usual style, and point `now` at it;
   - `not_checked`
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
tools/blind.sh audit peterson-2021; echo ---; ls entries/peterson-2021 earlier-entry; ls attempts | grep peterson
```

```
transcripts/peterson-2021/author-revise-1.md:107:([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/peterson-2021/author-revise-2.md:54:([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/peterson-2021/author-revise-2.md:82:9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/peterson-2021/author-revise-3.md:30:([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/peterson-2021/author.md:52:9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
transcripts/peterson-2021/author.md:138:Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
transcripts/peterson-2021/author.md:151:**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.
transcripts/peterson-2021/author.md:3443: "content": "schema_version: 3\nid: peterson-2021-02\ndatasets:\n- archive: dandi\n  id: \"000055\"\n  version: 0.261123.1703\n  doi: 10.48324/dandi.000055/0.261123.1703\n  relation: primary\npaper: doi:10.1523/eneuro.0007-21.2021\ndate: 2026-11-25\nentry: peterson-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/peterson-2021-01.yaml
```

```
<persisted-output>
Output too large (50.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/bbf8e917-4284-40dd-b9ef-9ae1aef4527a/tool-results/baxki8s8i.txt

Preview (first 2KB):
schema_version: 3
id: peterson-2021-01
datasets:
- archive: dandi
  id: "000055"
  version: 0.220127.0436
  doi: 10.48324/dandi.000055/0.220127.0436
  relation: primary
paper: doi:10.1523/eneuro.0007-21.2021
date: 2026-11-07
entry: peterson-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/bbf8e917-4284-40dd-b9ef-9ae1aef4527a/tool-results/baxki8s8i.txt"
}
```

```
1	schema_version: 3
2	id: peterson-2021-01
3	datasets:
4	- archive: dandi
5	  id: "000055"
6	  version: 0.220127.0436
7	  doi: 10.48324/dandi.000055/0.220127.0436
8	  relation: primary
9	paper: doi:10.1523/eneuro.0007-21.2021
10	date: 2026-11-07
11	entry: peterson-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-13
20	  runner:
[... 849 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/peterson-2021/entry.yaml; echo ---; cat earlier-entry/entry.yaml; wc -l entries/peterson-2021/ajile.py earlier-entry/ajile.py; date -u
```

```
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
  runtime_minutes: 60
helpers:
- ajile.py
related:
- id: dandi:000055/0.261123.1703
  relation: uses_data
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "starting_time\|rate\|def \|shift\|midnight" entries/peterson-2021/ajile.py | head -80
```

```
80:def list_assets():
94:def s3_url(asset_id):
98:def open_nwb(asset_id):
103:def _txt(v):
107:def load_session_meta(asset_id):
135:        ecog_rate=float(es["starting_time"].attrs["rate"]),
136:        ecog_start=float(es["starting_time"][()]),
143:        pose_rate=float(pos["R_Wrist/starting_time"].attrs["rate"]),
144:        pose_start=float(pos["R_Wrist/starting_time"][()]),
151:def load_all_meta(assets, workers=12):
156:def fold_angle(a):
166:def event_table(metas):
177:    ev["time_of_day"] = ev.start_time / 3600.0  # hours after midnight (session_description)
194:def _get(url, tries=4):
207:def figshare_files():
212:def load_projection(subject, files):
221:def morlet_bank():
233:    for i, w in enumerate(ws):
239:def band_stats(spec):
250:def _segment_psd(seg):
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/peterson-2021/ajile.py",
 "offset": 1,
 "limit": 475
}
```

```
1	"""Loading and measures for Peterson et al. (2021) on DANDI:000055 (AJILE12).
2	
3	Everything is streamed from the archive at a pinned version; nothing is written to disk.
4	
5	Where each parameter comes from:
6	
7	- Spectral method (claims file, opening comment, from the paper's Methods and code): Morlet
8	  wavelet power at 1 to 121 Hz in 5 Hz steps with n_cycles = frequency / 4, MNE's wavelet
9	  definition (sigma_t = n_cycles / (2 pi f), support of 5 sigma_t on each side, normalised;
10	  zero_mean False, the MNE 0.19 default of the code), decimated by 50 samples (10 Hz bins at
11	  500 Hz) aligned on the event, 10*log10 power. Because n_cycles / f is the same at every
12	  frequency, every wavelet spans +-0.2 s, so power is computed only at the time bins used here
13	  (-1.5 s to +1.0 s around onset); this gives the same values as convolving the whole 10 s
14	  segment.
15	- Baseline: each event's mean over the bins -1.5 to -1 s (inclusive) is subtracted, per
16	  electrode and frequency (claims file).
17	- Band power: bins 0 to 0.5 s (inclusive), LFB 11-31 Hz bins, HFB 76-96 Hz bins (claims file).
18	  The band mean (Methods) and the band median (code: median over time, then over frequency)
19	  are both returned.
20	- Segment rejection (Methods, "ECoG-event synchronization and segmentation": "discarding
[... 455 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    tags=c.get('metadata',{}).get('tags',[])
    print(i,c['cell_type'],tags,src[:100].replace('\n',' | '))
EOF
```

```
102
0 markdown [] # Reproducing Peterson et al. (2021) from DANDI:000055 |  | Paper: Peterson, Singh, Wang, Rao and Brunto
1 code [] import os, re, time, zlib, resource | os.environ.setdefault("OMP_NUM_THREADS", "1") | import numpy as np
2 code [] # LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed) | a
3 code ['sanity'] ev_all = ajile.event_table(metas) | subjects = sorted(ev_all.subject.unique()) | print("subjects:", subj
4 code ['sanity'] # Checks of the description against the values | m0 = metas[0] | print("ECoG unit:", m0["ecog_unit"], "c
5 code ['sanity'] # Coarse behavioural labels (epochs) at the event times. The Methods exclude movements during | # slee
6 markdown [] ## Projection matrices (outside input) and claim `roi-projection-link` |  | > The rows of the paper's pr
7 code ['claim:roi-projection-link'] files, fig_meta = ajile.figshare_files() | print("Figshare item", fig_meta["id"], "version", fig_meta[
8 code ['claim:roi-projection-link'] # Largest-weight region against the nearest region centroid, with mirrored MNI positions | rng = np.ra
9 markdown [] **Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as | man
10 markdown [] ## Spectral power of every event (streamed) |  | For each file, the chunk index of the ECoG series is re
11 code [] # SPECTRAL | t = time.time() | roi_idx = [cols_all.index(r) for r in ajile.ROIS] | # Electrodes good in ev
12 code ['sanity'] ev = ev_all.copy() | ev["inside"] = np.concatenate([r["inside"] for r in spec]) | ev["allzero"] = np.con
13 code ['sanity'] # Clock check: event-locked band power at the true onsets against a pseudo-onset 3 s earlier in the | 
14 code ['sanity'] # Reach angle convention: the stored angle against the angle of the wrist's largest displacement | # f
15 markdown [] ## Event sets |  | Reading (a): every event in the reaches tables. Reading (b): the events left after th
16 code [] EVA = ev | EVB = ev[ev.keep] 
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
def show(i):
    c=nb['cells'][i]
    print(f"===== CELL {i} {c['cell_type']} {c.get('metadata',{}).get('tags',[])}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--'); print(''.join(o['data']['text/plain'])[:3000])
for i in [2,3,4,12,13]: show(i)
EOF
```

```
===== CELL 2 code []
# LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed)
assets = ajile.list_assets()
metas = ajile.load_all_meta(assets)
print(len(assets), "files,", assets["size"].sum() / 1e9, "GB in all")
===== CELL 3 code ['sanity']
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
[... 147 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'));print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; ls -la; git log --oneline -5 -- .; ls ../../earlier-entry -la
```

```
0
total 296
drwxr-xr-x   3 runner runner   4096 Nov 25 15:44 .
drwxr-xr-x 351 runner runner  12288 Nov 25 15:38 ..
drwxr-xr-x   3 runner runner   4096 Nov 25 15:44 .claude
-rw-r--r--   1 runner runner   2436 Nov 25 15:38 README.md
-rw-r--r--   1 runner runner  33527 Nov 25 15:38 ajile.py
-rw-r--r--   1 runner runner   1011 Nov 25 15:38 entry.yaml
-rw-r--r--   1 runner runner 128160 Nov 25 15:38 reproduce_peterson_2021.ipynb
-rw-r--r--   1 runner runner     75 Nov 25 15:38 requirements.in
-rw-r--r--   1 runner runner 100020 Nov 25 15:38 requirements.lock.txt
578d862 Agent run on peterson-2021: author-revise-3 (success)
total 180
drwxr-xr-x  2 runner runner   4096 Nov 25 15:38 .
drwxr-xr-x 21 runner runner   4096 Nov 25 15:44 ..
-rw-r--r--  1 runner runner   2915 Nov 25 15:21 README.md
-rw-r--r--  1 runner runner  32270 Nov 25 15:21 ajile.py
-rw-r--r--  1 runner runner   1020 Nov 25 15:21 entry.yaml
-rw-r--r--  1 runner runner 123806 Nov 25 15:21 reproduce_peterson_2021.ipynb
-rw-r--r--  1 runner runner     81 Nov 25 15:21 requirements.in
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; grep -n "earlier_findings\|executed\|outputs" docs/protocol.md | head -30
```

```
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
the entry, against the schemas, and applies the conventions that keep a result
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 470,500p docs/protocol.md; ls executed 2>/dev/null; ls executed/peterson-2021 2>/dev/null
```

````
Exit code 2
### 4. Lock, check and run

```bash
python tools/entry.py lock entries/<name>
python tools/entry.py all  entries/<name>    # check, then run from a clean environment
```

`lock` pins every package, with its hashes, for the entry's Python version, and records that version as
`python` in entry.yaml (the registry's current one for a new entry). Commit notebooks without outputs. Read the executed copy in
`executed/<name>/` and confirm the conclusions still match the numbers: counts
near a threshold can move when a random split changes.

`run` keeps a stamp of what it ran from beside the executed copies in
`executed/<name>/`. When nothing it reads has changed since (the entry's files,
which name its Python and its datasets' versions), `run` and `all` reuse those
copies, say so, and execute nothing; `--fresh` executes all the same. A run of
yours starts with the executed copies of the entry as it is, when a run of it
was kept, so a session that changes nothing in the entry need not run it
again. Any edit to the entry makes the next `run` a real one.
[... 12 more lines not kept]
````

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [10,11,46,55,56,57,59,66,67,68,75,76,77]:
    c=nb['cells'][i]
    print(f"===== CELL {i} {c['cell_type']} {c.get('metadata',{}).get('tags',[])}")
    print(''.join(c['source']))
EOF
```

```
===== CELL 10 markdown []
## Spectral power of every event (streamed)

For each file, the chunk index of the ECoG series is read from the file's B-tree, and the chunks
holding the 10 s around each event are fetched and decoded. The helper's docstring gives the source
of every parameter. Every event's segment is checked by the Methods' rule, and its power is
projected to the eight regions with the weights of the electrodes good in every file of the subject;
the weights of each file's own good electrodes are kept as a variant. An electrode whose power is not
finite in an event gets weight 0 in that event, and the region's weights are renormalised.
===== CELL 11 code []
# SPECTRAL
t = time.time()
roi_idx = [cols_all.index(r) for r in ajile.ROIS]
# Electrodes good in every file of the subject (main). Variants, projection only: each file's own
# flags ("file"); the electrodes good in at least one file, i.e. only those bad in every file removed
# ("any"); and the main set with the electrodes holding a 50 ms run of zeros in an event dropped from
# that event ("zero_run", made in the helper).
GOOD_ALL = {s: np.all([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
            for s in subjects}
GOOD_ANY = {s: np.any([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/peterson-2021-02.yaml; awk '/^verifications:/,0' attempts/peterson-2021-02.yaml | grep -n -B2 -A12 "fig5-recording-day-effects\|fig4-precentral\|round\|Round" | head -250
```

```
1:schema_version: 3
2:id: peterson-2021-02
3:datasets:
9:paper: doi:10.1523/eneuro.0007-21.2021
10:date: 2026-11-25
11:entry: peterson-2021
12:provenance:
23:inputs:
28:outcomes:
417:findings:
511:verifications:
124-      the other seeds) and (b) 36.0 against 22.2, the same disagreement, and the same with each
125-      file's flags. Outcome unchanged.
126:  - claim: fig4-precentral-subject-variability
127-    agrees: true
128-    outcome: partially_reproduced
129-    reason: Parts 2, 3 and 4 hold. Part 1 fails for S09, whose HFB value is -0.030 dB.
130-    response: With the electrodes good in every file, part 4 now fails too (S04 and S08 are tied at 3
131-      bins with four other subjects, behind S07 and S09 at 2), and part 1 fails for S09 (-0.039 dB), so
132-      two of four parts hold; with each file's flags three hold. Partially reproduced either way.
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
b=yaml.safe_load(open('attempts/peterson-2021-01.yaml'))
ea={o['claim']:o for o in b['outcomes']}
for o in a['outcomes']:
    e=ea.get(o['claim'])
    print(o['claim'], o['outcome'], '|', e['outcome'] if e else None)
print(set(ea)-{o['claim'] for o in a['outcomes']})
for o in a['outcomes']:
    if o['claim'] in ('fig4-precentral-subject-variability','fig5-recording-day-effects','table1-subject-band-power-ci','fig3-group-lfb-decrease-hfb-increase'):
        print(yaml.safe_dump(o,width=100))
EOF
```

```
subject-days reproduced | reproduced
roi-projection-link reproduced | reproduced
cohort partially_reproduced | partially_reproduced
fig2-event-counts not_reproduced | not_reproduced
fig2-features-differ-across-subjects reproduced | reproduced
fig2-reach-shape partially_reproduced | partially_reproduced
fig2-bimanual-skew reproduced | reproduced
extfig2-1c-contralateral-larger reproduced | reproduced
extfig2-2-feature-correlations partially_reproduced | partially_reproduced
fig2-days-and-waking partially_reproduced | partially_reproduced
fig3-group-lfb-decrease-hfb-increase reproduced | reproduced
fig3-sensorimotor-largest reproduced | reproduced
fig3-lfb-more-widespread blocked | blocked
fig4-precentral-subject-variability partially_reproduced | reproduced
fig5-band-power-differs-across-subjects reproduced | reproduced
table1-subject-band-power-ci partially_reproduced | partially_reproduced
fig5-recording-day-effects partially_reproduced | reproduced
extfig5-1-baseline-reduces-day-variability reproduced | reproduced
discussion-day-changes-small reproduced | reproduced
fig6b-best-models-sensorimotor reproduced | reproduced
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd earlier-entry; grep -n "shift\|offset\|starting_time\|86400\|midnight" ajile.py | head -40; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if any(k in src for k in ('shift','offset','29241','starting')):
        print(f"===== CELL {i} {c['cell_type']} {c.get('metadata',{}).get('tags',[])}")
        print(src[:3000])
EOF
```

```
51:- Time of day: the files start at midnight local time (data descriptor, Methods: "each file
52:  contained data from one entire 24-hour recording day that started and ended at midnight"),
151:    out["ecog_rate"] = float(es["starting_time"].attrs["rate"])
152:    out["ecog_start"] = float(es["starting_time"][()])
171:    out["pose_rate"] = float(pos["R_Wrist/starting_time"].attrs["rate"])
172:    out["pose_start"] = float(pos["R_Wrist/starting_time"][()])
336:    t0 = float(f["acquisition/ElectricalSeries/starting_time"][()])
411:def ecog_offset(session: dict) -> float:
412:    """Seconds from midnight to the ECoG series' first sample.
414:    The files' events (`intervals/reaches`) and pose are on a clock that starts at midnight.
416:    `starting_time` is 0, but `ReachEvents` and the session start time put its first sample at
417:    midnight plus the missing time, i.e. the series ends at midnight. The notebook checks this
423:def ecog_jobs(sessions: list, weights: dict, offset: bool = True) -> list:
427:        off = ecog_offset(s) if offset else 0.0
===== CELL 12 code ['sanity']
# Clock of the pose and of the event times: contralateral wrist displacement from its mean
# position over -1.5 to -1 s, at the events and at the events shifted by -30 s.
def median_disp(tr, base_slice=slice(0, 16)):
    base = np.nanmean(tr[:, base_slice], 1)
    return np.nanmedian(np.linalg.norm(tr - base[:, None], axis=2), 0)
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd earlier-entry; sed -n 405,440p ajile.py; date -u
```

```
pc = multipletests(p.ravel(), alpha=alpha, method="fdr_bh")[1].reshape(ave.shape)
    out = ave.copy()
    out[pc >= alpha] = 0
    return out


def ecog_offset(session: dict) -> float:
    """Seconds from midnight to the ECoG series' first sample.

    The files' events (`intervals/reaches`) and pose are on a clock that starts at midnight.
    Three files hold less than 24 h of ECoG (S01 day 7, S04 day 3, S06 day 3); their ECoG
    `starting_time` is 0, but `ReachEvents` and the session start time put its first sample at
    midnight plus the missing time, i.e. the series ends at midnight. The notebook checks this
    against the neural response.
    """
    return 24 * 3600.0 - session["ecog_shape"][0] / session["ecog_rate"]


def ecog_jobs(sessions: list, weights: dict, offset: bool = True) -> list:
    jobs = []
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/peterson-2021/requirements.in; which python; python --version; python -c "import h5py, remfile, pynwb, numpy, scipy; print('ok')"; ls ~/.cache 2>/dev/null | head
```

```
h5py
ipykernel
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, pynwb, numpy, scipy; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
cd  python -m venv $TMPDIR/venv && $TMPDIR/venv/bin/pip install -q h5py remfile requests numpy pandas scipy 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import h5py,remfile;print('ok')"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/venv/bin/python -m pip install --upgrade pip
ok
```

**Agent**

Quick check of the three short-ECoG files on the new version, which bears on earlier finding 1 and both changed outcomes.

**Agent calls Bash**

```bash
cd entries/peterson-2021; $TMPDIR/venv/bin/python - <<'EOF'
import ajile, numpy as np, h5py
a=ajile.list_assets()
for s,d in [(1,7),(4,3),(6,3),(2,3)]:
    r=a[(a.subject==s)&(a.session==d)].iloc[0]
    f,_=ajile.open_nwb(r.asset_id)
    es=f["acquisition/ElectricalSeries"]
    n=es["data"].shape[0]; rate=es["starting_time"].attrs["rate"]
    re=f["processing/behavior/ReachEvents/timestamps"][:]
    st=f["intervals/reaches/start_time"][:]
    print(r.path, "ecog h", n/rate/3600, "start", es["starting_time"][()], "sst", f["session_start_time"][()],
          "RE-start max", np.abs(re-st).max(), "first RE", re[:3], "first start", st[:3], "pose n", f["processing/behavior/Position/R_Wrist/data"].shape[0]/30/3600,
          "subject", f["general/subject/sex"][()], f["general/subject/age"][()])
    f.close()
EOF
```

```
sub-01/sub-01_ses-7_behavior+ecephys.nwb ecog h 15.477107 start 30682.414 sst b'2000-01-07T00:00:00+00:00' RE-start max 0.0010000000183936208 first RE [32313.384 32323.618 32800.67 ] first start [32313.385 32323.618 32800.671] pose n 24.0 subject b'M' b'P44Y'
sub-04/sub-04_ses-3_behavior+ecephys.nwb ecog h 15.653244 start 30048.322 sst b'2000-01-03T00:00:00+00:00' RE-start max 0.0010000000038417056 first RE [49319.452 50646.16  50689.06 ] first start [49319.452 50646.161 50689.061] pose n 24.0 subject b'F' b'P19Y'
sub-06/sub-06_ses-3_behavior+ecephys.nwb ecog h 15.877621 start 29240.566 sst b'2000-01-03T00:00:00+00:00' RE-start max 0.0010000000183936208 first RE [29754.282 29785.582 31504.308] first start [29754.283 29785.583 31504.309] pose n 24.0 subject b'M' b'P37Y'
sub-02/sub-02_ses-3_behavior+ecephys.nwb ecog h 24.0 start 0.0 sst b'2000-01-03T00:00:00+00:00' RE-start max 0.0010000000111176632 first RE [21619.368 32995.002 33009.102] first start [21619.369 32995.003 33009.103] pose n 24.0 subject b'M' b'P20Y'
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; sed -n 686,726p ajile.py; python - <<'EOF'
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [1,7]:
    print(f"== {i}");print(''.join(nb['cells'][i]['source']))
EOF
```

```
def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights, weights_var = args
    return session_spectral(asset_id, times, good, weights, weights_var)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights, weights_var). Runs files in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(_spectral_job, jobs))


def match_projection(m, positions_known):
    """Rows of a projection matrix matched to the file's electrodes, by the paper's code
    (tfr_utils.load_project_spectral_power, commit 04c6faf): it keeps the rows that are not all
    zero and drops the first of them (`np.nonzero(df.transpose().mean().values != 0)[0][1:]`),
    and applies the rest, in order, to the channels of its power files. Here they are applied,
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/chk; cat > $TMPDIR/chk/fig5check.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0, "entries/peterson-2021")
import ajile
from scipy import stats
SUBJ = [1, 4, 6]
if __name__ == "__main__":
    assets = ajile.list_assets()
    assets = assets[assets.subject.isin(SUBJ)].reset_index(drop=True)
    metas = ajile.load_all_meta(assets)
    files, _ = ajile.figshare_files()
    jobs, keys = [], []
    for s in SUBJ:
        ms = [m for m in metas if int(m["subject_id"]) == s]
        m0, _ = ajile.load_projection(s, files)
        cols = list(m0.columns)
        a, note = ajile.match_projection(m0, ms[0]["electrodes"].x.notna().values)
        roi_idx = [cols.index(r) for r in ajile.ROIS]
        good_all = np.all([m["electrodes"].good.values.astype(bool) for m in ms], axis=0)
        w_main = ajile.session_weights(a[:, roi_idx], good_all)
        for m in ms:
            w_file = ajile.session_weights(a[:, roi_idx], m["electrodes"].good.values.astype(bool))
            for mode in ("as_given", "start_corrected"):
                if mode == "start_corrected" and m["ecog_start"] == 0:
                    continue
                t = m["event_times"] - (m["ecog_start"] if mode == "start_corrected" else 0.0)
                jobs.append((m["asset_id"], t, good_all, w_main, {"file": w_file}))
                keys.append((s, int(m["session_id"]), mode, m["ecog_start"]))
    spec = ajile.run_spectral(jobs, workers=8)
    out = []
    for k, r, m in zip(keys, spec, [None]*len(keys)):
        out.append(dict(key=k, region_file=r["region_var"]["file"][:, 1], region_main=r["region"][:, 1], seg_db=r["seg_db"], hf_db=r["hf_db"],
                        inside=r["inside"], allzero=r["allzero"]))
    ev = {(int(m["subject_id"]), int(m["session_id"])): (m["event_times"], m["reaches"].start_time.values) for m in metas}
    pickle.dump(dict(out=out, ev=ev), open(sys.argv[1], "wb"))
EOF
cd $TMPDIR/chk && date -u && timeout 3000 $TMPDIR/venv/bin/python fig5check.py $TMPDIR/chk/fig5.pkl 2>&1 | tail -5; date -u
```

```
Wed Nov 25 15:46:50 UTC 2026
  w = w / w.sum(axis=0)
entries/peterson-2021/ajile.py:332: RuntimeWarning: invalid value encountered in divide
  w = w / w.sum(axis=0)
entries/peterson-2021/ajile.py:332: RuntimeWarning: invalid value encountered in divide
  w = w / w.sum(axis=0)
Wed Nov 25 15:49:31 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/chk/fig5an.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0, "entries/peterson-2021")
import ajile
from scipy import stats
d = pickle.load(open(sys.argv[1], "rb"))
recs = {r["key"][:3]: r for r in d["out"]}
paper_sig = {"lfb": {3, 5, 6, 7, 8, 11}, "hfb": {3, 4, 7, 8, 10}}
for scen in ("as_given", "start_corrected"):
    print("=====", scen)
    for s in (1, 4, 6):
        days = sorted({k[1] for k in recs if k[0] == s})
        rows = []
        for dd in days:
            r = recs.get((s, dd, scen)) or recs[(s, dd, "as_given")]
            et, st = d["ev"][(s, dd)]
            for w in ("file", "main"):
                R = r["region_" + w]
                RB = R - R[..., ajile.BASE].mean(axis=-1, keepdims=True)
                bs = ajile.band_stats(RB)
                r[w + "_lfb"], r[w + "_hfb"] = bs["lfb_mean"], bs["hfb_mean"]
            rows.append(pd.DataFrame(dict(day=dd, inside=r["inside"], allzero=r["allzero"], seg_db=r["seg_db"], hf_db=r["hf_db"],
                        mism=np.abs(et - st) > 1, file_lfb=r["file_lfb"], file_hfb=r["file_hfb"], main_lfb=r["main_lfb"], main_hfb=r["main_hfb"])))
        E = pd.concat(rows, ignore_index=True)
        ok = E.inside & E.hf_db.notna()
        thr = E[ok].hf_db.mean() + 3 * E[ok].hf_db.std()
        E["keep"] = E.inside & E.seg_db.notna() & ~E.allzero & ~(E.seg_db < 0) & ~(E.hf_db > thr) & ~E.mism
        K = E[E.keep]
        out = [f"S{s:02d} kept {len(K)} per day {K.groupby('day').size().to_dict()}"]
        for w in ("file", "main"):
            for b in ("lfb", "hfb"):
                p = stats.kruskal(*[x[f"{w}_{b}"].values for _, x in K.groupby("day")]).pvalue
                dm = K.groupby("day")[f"{w}_{b}"].mean().round(2).to_dict()
                out.append(f"  {w} {b}: p={p:.3g} paper_sig={s in paper_sig[b]} day means {dm}")
        print("\n".join(out))
EOF
$TMPDIR/venv/bin/python $TMPDIR/chk/fig5an.py $TMPDIR/chk/fig5.pkl
```

```
===== as_given
S01 kept 601 per day {3: 155, 4: 194, 5: 194, 7: 58}
  file lfb: p=0.0471 paper_sig=False day means {3: -1.31, 4: -1.56, 5: -1.45, 7: -0.42}
  file hfb: p=0.0227 paper_sig=False day means {3: -0.03, 4: 0.04, 5: 0.2, 7: -0.15}
  main lfb: p=0.0432 paper_sig=False day means {3: -1.31, 4: -1.59, 5: -1.48, 7: -0.43}
  main hfb: p=0.022 paper_sig=False day means {3: -0.03, 4: 0.04, 5: 0.2, 7: -0.15}
S04 kept 390 per day {3: 13, 4: 97, 5: 43, 6: 81, 7: 156}
  file lfb: p=0.169 paper_sig=False day means {3: 0.35, 4: -0.04, 5: -0.29, 6: -0.14, 7: -0.12}
  file hfb: p=0.00124 paper_sig=True day means {3: 0.19, 4: 0.22, 5: 0.56, 6: 0.72, 7: 0.56}
  main lfb: p=0.383 paper_sig=False day means {3: 0.37, 4: -0.06, 5: -0.25, 6: -0.12, 7: -0.1}
  main hfb: p=0.00636 paper_sig=True day means {3: 0.15, 4: 0.28, 5: 0.6, 6: 0.75, 7: 0.56}
S06 kept 832 per day {3: 81, 4: 191, 5: 193, 6: 190, 7: 177}
  file lfb: p=2.6e-07 paper_sig=True day means {3: 0.27, 4: -1.77, 5: -0.7, 6: -1.09, 7: -1.14}
  file hfb: p=6.7e-11 paper_sig=False day means {3: 0.11, 4: 1.82, 5: 1.77, 6: 1.63, 7: 1.82}
  main lfb: p=2.65e-07 paper_sig=True day means {3: 0.27, 4: -1.77, 5: -0.7, 6: -1.1, 7: -1.14}
  main hfb: p=6.85e-11 paper_sig=False day means {3: 0.11, 4: 1.82, 5: 1.77, 6: 1.63, 7: 1.83}
===== start_corrected
S01 kept 733 per day {3: 155, 4: 194, 5: 194, 7: 190}
  file lfb: p=0.777 paper_sig=False day means {3: -1.31, 4: -1.56, 5: -1.45, 7: -1.35}
  file hfb: p=0.0546 paper_sig=False day means {3: -0.03, 4: 0.04, 5: 0.2, 7: 0.06}
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/peterson-2021.yaml')) if __import__('os').path.exists('claims/peterson-2021.yaml') else None
import glob;print(glob.glob('claims/*peterson*'))
EOF
```

```
['claims/peterson-2021.yaml']
```

**Agent calls Bash**

```bash
cd  head -40 claims/peterson-2021.yaml; grep -n "id: fig4-precentral\|id: fig5-recording" -A 40 claims/peterson-2021.yaml | grep -v "^\s*$" | head -90; git log --oneline -3 -- claims/peterson-2021.yaml
```

```
# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,
# "Behavioral and Neural Variability of Naturalistic Arm Movements", on dandiset 000055.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The version of record as served by Europe PMC (PMC8225404), from
# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,
# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was
# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are
# EPS downloads and are not in the text; only their legends are. Claims that rest on them are
# taken from their legends and from the Results sentences that cite them. The per-subject
# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals
# (Extended Data Figures 2-3 and 2-4) could not be read.
#
# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit
# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.
# It holds compute_spectral_power.py and tfr_utils.py (Morlet power, baseline, bootstrap
# masking, projection to regions), the MATLAB projection of electrodes onto AAL regions
# (project_ecog_to_rois.m, EEGLAB 13.5.4b, Measure Projection Toolbox 1.661),
# fit_regression_models.py and regression_utils.py (regression), and notebooks for Figures 2,
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 503,540p claims/peterson-2021.yaml; c=$(git log -1 --format=%H -- attempts/peterson-2021-01.yaml); echo $c; git diff --stat $c HEAD -- claims/peterson-2021.yaml; git diff $c HEAD -- claims/peterson-2021.yaml | head -80
```

```
test: Kruskal-Wallis test
    p: 0.001
    p_relation: "<"
  - about: HFB, S08
    test: Kruskal-Wallis test
    p: 0.004
  - about: HFB, S10
    test: Kruskal-Wallis test
    p: 0.006
  data: with_inputs
  depends_on:
  - roi-projection-link
  criterion: Per subject and band, a one-way Kruskal-Wallis test of banded precentral power
    across the subject's recording days, uncorrected, at p < 0.05 (Figure 5 legend; the notebook
    uses pingouin's uncorrected p). Band mean as the main result, band median (code) as a
    variant. The paper's pattern is the 11 significant pairs above and the 13 other subject and
    band pairs not significant. Reproduced when all 24 pairs agree; partially reproduced when at
    least 20 agree. Each p is reported, with the per-day 95% intervals of Table 2 for
    comparison.
- id: extfig5-1-baseline-reduces-day-variability
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git log --oneline | wc -l; git rev-parse --is-shallow-repository; grep -n "pilot-1[3-8]\|^## \|^### " docs/pilot-notes.md | head -60
```

```
1
true
16:## Protocol pilot-3 (2026-10-13)
59:## Protocol pilot-4 (2026-10-14)
88:## Protocol pilot-5 (2026-10-14)
113:## Protocol pilot-6 (2026-10-14), at the end of the pilot
138:## After the pilot: the first batch (2026-10-14)
156:## Protocol pilot-7 (2026-10-15): data in other archives
218:## Protocol pilot-8 (2026-10-19): the paper's own words
281:## Protocol pilot-9 (2026-10-20): the full text or nothing
320:## Protocol pilot-10 (2026-10-20): the reader and the author
381:## Protocol pilot-12 (2026-10-27): blind repeat attempts
403:## Protocol pilot-13 (2026-10-31): a notebook may take an hour
414:## Protocol pilot-14 (2026-11-09): papers first, and every dataset a paper rests on
```

**Agent calls Bash**

```bash
cd  sed -n 403,600p docs/pilot-notes.md
```

```
## Protocol pilot-13 (2026-10-31): a notebook may take an hour

CI used to fail a notebook that took more than 30 minutes, and the limit was
shaping results more than it should. Authors cut shuffles and fits short to
stay under it (000447, 000678), split analyses across notebooks (000467),
dropped neurons (000579) or recorded claims as `too_large` (000458, 000248),
and 000673's verifier-2 run failed when its LFP notebook took 42 minutes. The
limit is now 60 minutes a notebook (`tools/entry.py --max-minutes`), with CI's
run job raised to 240 minutes to fit an entry's notebooks. The aim stays
under ten minutes, and the author's time budget is unchanged.

## Protocol pilot-14 (2026-11-09): papers first, and every dataset a paper rests on

Records were filed by dataset, so a paper whose data are split across dandisets
(Semenov 2026 on 7, Churchland 2010 on 4) was tested once per dandiset, each
time with its own claims, and a paper that reuses a dataset had nowhere to go.
Records are now filed by paper (docs/paper-first.md): one claims file for the
paper, claims naming their datasets only when there are several, and one
attempt that uses as many of the paper's datasets as can be loaded. A dataset
it could not use is listed under `missing_datasets`, and the claims that need
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "pilot-1[5-8]" docs/ protocol.lock schemas/ 2>/dev/null | head -20; cat protocol.lock | head -20
```

```
docs/pilot-notes/tingley-2018-02.md:4:under pilot-15. Eight claims reproduced, eight partially, thirteen not
docs/pilot-notes/gao-2018-02.md:22:file was updated to pilot-15 for both datasets from the version of record
docs/pilot-notes/zhai-2025-02.md:3:The second attempt, made blind to the first (zhai-2025-01) under pilot-15,
docs/pilot-notes/pelot-2020-02.md:17:pilot-18 with 43 claims, and was blind to the earlier attempt. The claims
docs/protocol.md:3:Version: `pilot-18`. Record this version in the attempt's provenance.
docs/protocol.md:586:  Attempts made before `pilot-18` did not rate their findings. A later review
schemas/attempt.schema.json:467:            "description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).",
schemas/attempt.schema.json:552:            "description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.",
schemas/attempt.schema.json:739:      "description": "For an attempt made before protocol pilot-18, whose findings carry no severity: the severity a later review gave each finding about the data, and whether the review checked it against the notebook's outputs. Added to the record afterwards; nothing else in the record changes.",
v0.1.5
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k=='reconciliation': print(path+'/'+k); print(json.dumps(v,indent=1)[:6000])
            find(v,path+'/'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,path+f'[{i}]')
find(s)
EOF
```

```
/properties/reconciliation
{
 "description": "A repeat attempt's comparison with the attempt before it, written by the reconcile step once this attempt, made blind, has been verified (docs/protocol.md, \"Repeat attempts\"). A finding of this attempt that no item of `findings` points at is new.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "earlier",
  "date",
  "blind",
  "findings"
 ],
 "properties": {
  "earlier": {
   "description": "The id of the attempt compared with.",
   "type": "string"
  },
  "date": {
   "type": "string",
   "format": "date"
  },
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/chk/full.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0, "entries/peterson-2021")
import ajile
if __name__ == "__main__":
    assets = ajile.list_assets()
    metas = ajile.load_all_meta(assets)
    files, _ = ajile.figshare_files()
    subjects = sorted({int(m["subject_id"]) for m in metas})
    jobs, keys = [], []
    for s in subjects:
        ms = [m for m in metas if int(m["subject_id"]) == s]
        m0, _ = ajile.load_projection(s, files)
        cols = list(m0.columns)
        a, note = ajile.match_projection(m0, ms[0]["electrodes"].x.notna().values)
        roi_idx = [cols.index(r) for r in ajile.ROIS]
        G = np.array([m["electrodes"].good.values.astype(bool) for m in ms])
        w_all = ajile.session_weights(a[:, roi_idx], G.all(0))
        w_any = ajile.session_weights(a[:, roi_idx], G.any(0))
        w_first = ajile.session_weights(a[:, roi_idx], G[0])
        for m in ms:
            w_file = ajile.session_weights(a[:, roi_idx], m["electrodes"].good.values.astype(bool))
            t = m["event_times"] - m["ecog_start"]
            jobs.append((m["asset_id"], t, G.all(0), w_all, {"file": w_file, "any": w_any, "first": w_first}))
            keys.append((s, int(m["session_id"]), m["ecog_start"]))
    spec = ajile.run_spectral(jobs, workers=8)
    out = []
    for k, r, m in zip(keys, spec, metas):
        d = dict(key=k, main=r["region"][:, 1].astype(np.float32), seg_db=r["seg_db"], hf_db=r["hf_db"], inside=r["inside"], allzero=r["allzero"],
                 mism=np.abs(m["event_times"] - m["reaches"].start_time.values) > 1)
        for v in ("file", "any", "first"):
            d[v] = r["region_var"][v][:, 1].astype(np.float32)
        out.append(d)
    pickle.dump(out, open(sys.argv[1], "wb"))
EOF
cd $TMPDIR/chk && date -u && timeout 5400 $TMPDIR/venv/bin/python full.py $TMPDIR/chk/full.pkl 2>&1 | grep -v "RuntimeWarning\|w = w /" | tail -5; date -u; ls -la $TMPDIR/chk
```

```
Wed Nov 25 15:50:21 UTC 2026
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
Wed Nov 25 16:00:42 UTC 2026
total 95148
drwxr-xr-x 2 runner runner     4096 Nov 25 16:00 .
drwx------ 7 runner runner     4096 Nov 25 15:50 ..
-rw-r--r-- 1 runner runner 13112418 Nov 25 15:49 fig5.pkl
-rw-r--r-- 1 runner runner     1904 Nov 25 15:49 fig5an.py
-rw-r--r-- 1 runner runner     1922 Nov 25 15:46 fig5check.py
-rw-r--r-- 1 runner runner 84293924 Nov 25 16:00 full.pkl
-rw-r--r-- 1 runner runner     1801 Nov 25 15:50 full.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/chk/fullan.py <<'EOF'
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0, "entries/peterson-2021")
import ajile
from scipy import stats
out = pickle.load(open(sys.argv[1], "rb"))
rows = []
for d in out:
    s, day, st = d["key"]
    rows.append(pd.DataFrame(dict(subject=s, day=day, inside=d["inside"], allzero=d["allzero"], seg_db=d["seg_db"], hf_db=d["hf_db"], mism=d["mism"])))
E = pd.concat(rows, ignore_index=True)
ok = E.inside & E.hf_db.notna()
thr = E[ok].groupby("subject").hf_db.agg(lambda x: x.mean() + 3 * x.std())
E["keep"] = E.inside & E.seg_db.notna() & ~E.allzero & ~(E.seg_db < 0) & ~(E.hf_db > E.subject.map(thr)) & ~E.mism
print("kept", int(E.keep.sum()), "of", len(E), "; per subject", E[E.keep].groupby("subject").size().to_dict())
subjects = sorted(E.subject.unique())
F = ajile.FREQS
paper_sig = {"lfb": {3, 5, 6, 7, 8, 11}, "hfb": {3, 4, 7, 8, 10}}
for v in ("main", "file", "any", "first"):
    R = np.concatenate([d[v] for d in out])
    RB = R - R[..., ajile.BASE].mean(axis=-1, keepdims=True)
    kb = E.keep.values
    SM = np.stack([np.nanmedian(RB[kb & (E.subject.values == s)], axis=0) for s in subjects])
    P = SM - SM[..., ajile.BASE].mean(axis=-1, keepdims=True)
    sp = P[..., ajile.WIN].mean(axis=-1)
    lf, hf = sp[:, ajile.LFB].mean(1), sp[:, ajile.HFB].mean(1)
    p1 = [f"S{s:02d}" for s, a, b in zip(subjects, lf, hf) if not (a < 0 and b > 0)]
    i116, i121 = list(F).index(116), list(F).index(121)
    p2 = all(sp[subjects.index(s), i116] > 0 and sp[subjects.index(s), i121] > 0 for s in [3, 6, 7, 8, 11])
    hi = F >= 56; p3 = {}
    for s in [9, 12]:
        x = sp[subjects.index(s)]; fmax = F[hi][np.argmax(x[hi])]; top = x[hi].max()
        p3[s] = (fmax, bool(61 <= fmax <= 76 and x[F >= 101].mean() < top / 2))
    low = F <= 46
    width = {s: int((sp[i][low] < sp[i][low].min() / 2).sum()) for i, s in enumerate(subjects)}
    fewest = sorted(width, key=lambda s: width[s])[:3]
    print(f"== {v}: fig4 part1 fails {p1} (S09 HFB {hf[subjects.index(9)]:.3f}, LFB {lf[subjects.index(9)]:.3f}); part2 {p2}; part3 {p3}; widths {width}; fewest {fewest} part4 {4 in fewest and 8 in fewest}")
    bs = ajile.band_stats(RB)
    E2 = E.copy()
    for b in ("lfb", "hfb"):
        for st in ("mean", "median"):
            E2[f"{b}_{st}"] = bs[f"{b}_{st}"]
    K = E2[E2.keep]
    for st in ("mean", "median"):
        agree, dis = 0, []
        for s, g in K.groupby("subject"):
            for b in ("lfb", "hfb"):
                p = stats.kruskal(*[x[f"{b}_{st}"].values for _, x in g.groupby("day")]).pvalue
                if (p < 0.05) == (s in paper_sig[b]): agree += 1
                else: dis.append((f"S{s:02d}", b, float(f"{p:.3g}")))
        print(f"   fig5 day effects band {st}: {agree} of 24 agree; disagree {dis}")
EOF
$TMPDIR/venv/bin/python $TMPDIR/chk/fullan.py $TMPDIR/chk/full.pkl 2>&1 | grep -v Warning
```

```
kept 7883 of 8088 ; per subject {1: 733, 2: 296, 3: 638, 4: 412, 5: 264, 6: 912, 7: 787, 8: 944, 9: 210, 10: 746, 11: 965, 12: 976}
== main: fig4 part1 fails ['S09'] (S09 HFB -0.039, LFB -0.090); part2 True; part3 {9: (np.float64(76.0), True), 12: (np.float64(66.0), True)}; widths {np.int64(1): 4, np.int64(2): 3, np.int64(3): 3, np.int64(4): 3, np.int64(5): 3, np.int64(6): 4, np.int64(7): 2, np.int64(8): 3, np.int64(9): 2, np.int64(10): 3, np.int64(11): 4, np.int64(12): 4}; fewest [np.int64(7), np.int64(9), np.int64(2)] part4 False
   fig5 day effects band mean: 21 of 24 agree; disagree [('S07', 'hfb', 0.0731), ('S08', 'lfb', 0.308), ('S10', 'hfb', 0.0535)]
   fig5 day effects band median: 21 of 24 agree; disagree [('S03', 'hfb', 0.125), ('S05', 'lfb', 0.0557), ('S07', 'hfb', 0.0748)]
== file: fig4 part1 fails ['S09'] (S09 HFB -0.030, LFB -0.250); part2 True; part3 {9: (np.float64(66.0), True), 12: (np.float64(71.0), True)}; widths {np.int64(1): 5, np.int64(2): 3, np.int64(3): 3, np.int64(4): 3, np.int64(5): 3, np.int64(6): 4, np.int64(7): 2, np.int64(8): 2, np.int64(9): 5, np.int64(10): 4, np.int64(11): 4, np.int64(12): 4}; fewest [np.int64(7), np.int64(8), np.int64(2)] part4 False
   fig5 day effects band mean: 23 of 24 agree; disagree [('S10', 'hfb', 0.0935)]
   fig5 day effects band median: 22 of 24 agree; disagree [('S02', 'lfb', 0.0439), ('S05', 'lfb', 0.0557)]
== any: fig4 part1 fails [] (S09 HFB 0.097, LFB -0.408); part2 True; part3 {9: (np.float64(66.0), True), 12: (np.float64(66.0), True)}; widths {np.int64(1): 5, np.int64(2): 5, np.int64(3): 3, np.int64(4): 3, np.int64(5): 3, np.int64(6): 4, np.int64(7): 2, np.int64(8): 2, np.int64(9): 6, np.int64(10): 4, np.int64(11): 4, np.int64(12): 4}; fewest [np.int64(7), np.int64(8), np.int64(3)] part4 False
   fig5 day effects band mean: 24 of 24 agree; disagree []
   fig5 day effects band median: 23 of 24 agree; disagree [('S05', 'lfb', 0.0555)]
== first: fig4 part1 fails [] (S09 HFB 0.097, LFB -0.408); part2 True
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; $TMPDIR/venv/bin/python - <<'EOF'
import ajile, numpy as np, pandas as pd
a=ajile.list_assets(); metas=ajile.load_all_meta(a)
ev=ajile.event_table(metas)
x=ev.bimanual_overlap
print(">1",(x>1).sum(),">=1",(x>=1).sum(),"max",x.max(), "n", len(x))
print("sst", sorted({m["session_start"] for m in metas})[:3], len({m["session_start"][10:] for m in metas}), {m["session_start"][10:] for m in metas})
print("sex/age", {(int(m["subject_id"]), m["sex"], m["age"]) for m in metas})
for s in (10,11):
    m=[m for m in metas if int(m["subject_id"])==s][0]
    el=m["electrodes"]; g=el.group_name.map(m["groups"]).fillna("")
    dep=g.str.contains("depth",case=False)
    print(s, "surface",(~dep).sum(),"depth",dep.sum(), el.assign(desc=g).groupby(["group_name","desc"]).size().to_dict())
print("ecog starts", [(int(m["subject_id"]),m["session_id"],m["ecog_start"]) for m in metas if m["ecog_start"]!=0])
EOF
```

```
>1 1708 >=1 1873 max 3.833333333 n 8088
sst ['2000-01-03T00:00:00+00:00', '2000-01-04T00:00:00+00:00', '2000-01-05T00:00:00+00:00'] 1 {'T00:00:00+00:00'}
sex/age {(1, 'M', 'P44Y'), (8, 'F', 'P33Y'), (5, 'F', 'P31Y'), (3, 'M', 'P33Y'), (2, 'M', 'P20Y'), (9, 'M', 'P20Y'), (10, 'M', 'P34Y'), (4, 'F', 'P19Y'), (7, 'M', 'P26Y'), (11, 'F', 'P34Y'), (12, 'M', 'P22Y'), (6, 'M', 'P37Y')}
10 surface 78 depth 48 {('AHD', 'anterior hippocampal depth'): 4, ('AID', 'anterior insular depth'): 14, ('GRID', 'ECoG grid'): 53, ('LAT', 'left anterior temporal'): 5, ('LMT', 'left medial temporal'): 5, ('LOF', 'left orbitofrontal'): 4, ('LPT', 'left posterior temporal'): 5, ('LTP', 'left temporal pole'): 6, ('MHD', 'medial hippocampal depth'): 4, ('MID', 'medial insular depth'): 14, ('PID', 'posterior insular depth'): 12}
11 surface 88 depth 18 {('Grid', 'ECoG grid'): 64, ('LAT', 'left anterior temporal'): 16, ('LATD', 'left anterior temporal depth'): 6, ('LMTD', 'left medial temporal depth'): 6, ('LPT', 'left posterior temporal'): 8, ('LTPD', 'left temporal pole depth'): 6}
ecog starts [(1, '7', 30682.414), (4, '3', 30048.322), (6, '3', 29240.566)]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; grep -n "1661\|overlap.*> 1\|overlap > 1\|bimanual_overlap > 1" reproduce_peterson_2021.ipynb | head; grep -n "1661\|1708" ../../transcripts/peterson-2021/*.md | head
```

```
951:    "print(\"overlap values above 1:\", int((EVB.bimanual_overlap > 1).sum()), \"of\", len(EVB), \"; in all events:\",\n",
952:    "      int((EVA.bimanual_overlap > 1).sum()), \"of\", len(EVA))"
../../transcripts/peterson-2021/author-revise-1-report.md:22:- One finding's number was wrong: 1708 of 8088 bimanual overlap values are above 1, not 1661 (that figure came from the analysed subset). The findings that describe the clock check, the segment rejection, the spread measure and the electrode flags now give the new numbers.
../../transcripts/peterson-2021/author-revise-1.md:1893:  described as a fraction of the movement, is in seconds (1661 of all 8088 events above 1); the pose
../../transcripts/peterson-2021/author-revise-1.md:1923:8088 1708 3.833333333
../../transcripts/peterson-2021/author-revise-1.md:1935:a='described as a fraction of the movement, is in seconds (1661 of all 8088 events above 1); the pose'
../../transcripts/peterson-2021/author-revise-1.md:1937:s=s.replace(a,'described as a fraction of the movement, is in seconds (1708 of all 8088 events above 1); the pose')
../../transcripts/peterson-2021/author-revise-1.md:1941:grep -c "1708" reproduce_peterson_2021.ipynb; cat ../../questions/peterson-2021.yaml 2>/dev/null | head -40; ls ../../questions | grep peter; head -60 ../../questions/README.md
../../transcripts/peterson-2021/author-revise-1.md:2121:overlap values above 1: 1622 of 7649 ; in all events: 1708 of 8088
../../transcripts/peterson-2021/author-revise-1.md:2602:    but 1708 of 8088 values are above 1 (up to 3.83); the values are consistent with seconds.
../../transcripts/peterson-2021/author-revise-1.md:3085:- One finding's number was wrong: 1708 of 8088 bimanual overlap values are above 1, not 1661 (that figure came from the analysed subset). The findings that describe the clock check, the segment rejection, the spread measure and the electrode flags now give the new numbers.
../../transcripts/peterson-2021/author.md:1045:    17089    0.1
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
for i,f in enumerate(a['findings'],1):
    print(i, f.get('kind'), f.get('severity'), f.get('about'), '|', f['statement'][:400]); print()
print([k for k in a])
EOF
```

```
1 selection_undocumented major data | The files hold 8088 movement events, 211 to 996 per subject (median 770.5), where the paper analysed 151 to 947 per subject (median 640). Nothing in the files marks the events the paper used or the false positives it removed, so the paper's event set cannot be rebuilt; dropping the events without usable ECoG still leaves 210 to 976 per subject (median 692).

2 data_missing minor None | The ECoG of three files ends hours before the day ends while the pose and the events go on to 24 h; sub-01 day 7 (15.5 h), sub-04 day 3 (15.7 h) and sub-06 day 3 (15.9 h). 237 events (132, 22 and 83) have no neural data.

3 metadata_insufficient minor None | The ECoG holds stretches of NaN samples, which the files do not describe; 125 events have NaN samples within 5 s of onset (47 of them in sub-10).

4 metadata_error minor None | The bimanual overlap is described as a fraction of the contralateral movement duration, but 1708 of 8088 values are above 1 (up to 3.83); the values are consistent with seconds.

5 metadata_error minor None | The pose series are labelled in meters, but the values are pixels; the reach magnitudes computed from the pose equal the stored pixel magnitudes (median ratio 1.007).

6 metadata_insufficient minor None | The reach angle has no stated convention. It is the angle in image coordinates (y downward), -180 to 180 degrees, matching the pose to a median of 1.6 degrees, so upward reaches are negative. The paper's code negates and folds it.

7 metadata_insufficient minor None | The `good` flags of the electrodes differ between the files of a subject (bad in at least one file 3 to 32 per subject, bad in every file 1 to 17), and nothing says how they were set or which applies to the subject's analyses. The paper reports 4.9 +- 4.9 surface electrodes removed per subject; the surface electrodes bad in at least one file number 12.6 +- 8.4 per subject, those bad in every file 

8 metadata_insufficient minor None | The electrodes 
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper | grep -i "s41597\|peterson\|eneuro\|01280" ; grep -il "AJILE12" paper/* 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls entries/*/earlier_findings.ipynb | head; f=$(ls entries/*/earlier_findings.ipynb | head -1); python -c "
import json,sys;nb=json.load(open('$f'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:600]);print('---')
print(nb['metadata'])"; grep -A6 earlier_findings $(dirname $f)/entry.yaml
```

```
entries/asari-2009/earlier_findings.ipynb
entries/fujisawa-2008/earlier_findings.ipynb
entries/gao-2018/earlier_findings.ipynb
entries/huszar-2022/earlier_findings.ipynb
entries/kim-2022/earlier_findings.ipynb
entries/markowitz-2023/earlier_findings.ipynb
entries/pakhomov-2023/earlier_findings.ipynb
entries/park-2019/earlier_findings.ipynb
entries/pelot-2020/earlier_findings.ipynb
entries/petersen-2020/earlier_findings.ipynb
markdown {} # Earlier findings of asari-2009-01, checked on CRCNS ac-1

Paper. Asari H, Zador AM (2009). Long-lasting context dependence constrains neural encoding
models in rodent auditory cortex. J Neurophysiol 102:2638-2656.
[doi:10.1152/jn.00577.2009](https://doi.org/10.1152/jn.00577.2009)

Dataset. CRCNS ac-1, [doi:10.6080/K0KW5CXR](https://doi.org/10.6080/K0KW5CXR), streamed from the
public S3 bucket `crcnsarchive` (`ac-1/`), zip files opened in place. CRCNS data sets are not
versioned, so the version is recorded as `unversioned` (docs/archives.md, CRCNS); the MD5 sums of
the zip files are in `asari
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'));print(nb['metadata'], nb['nbformat'], nb['nbformat_minor']); print(nb['cells'][1].keys(), nb['cells'][1]['metadata'])"; sed -n 1,30p README.md
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}} 4 5
dict_keys(['cell_type', 'execution_count', 'id', 'metadata', 'outputs', 'source']) {}
# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/eneuro.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.261123.1703) (AJILE12), which holds the
ECoG, pose and wrist movement events of the paper's 12 subjects over 55 days. The ECoG around each
of 8088 events is streamed from the archive, and region power uses the paper's projection matrices
from [Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days are the paper's | Reproduced |
| The Figshare projection matrices match the electrodes | Reproduced |
| Cohort: sex, age, electrodes, hemispheres | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration and magnitude small, angles peak at +-90 | Partially reproduced |
| Bimanual features skewed toward unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/make.py <<'PYEOF'
import json, uuid
cells = []
def md(s): cells.append(dict(cell_type="markdown", id=uuid.uuid4().hex[:8], metadata={}, source=s.strip("\n")))
def code(s, tags=None):
    cells.append(dict(cell_type="code", id=uuid.uuid4().hex[:8], metadata={"tags": tags} if tags else {}, execution_count=None, outputs=[], source=s.strip("\n")))

md("""
# Earlier findings of peterson-2021-01, checked on DANDI:000055 version 0.261123.1703

Paper. Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural
variability of naturalistic arm movements. eNeuro 8(3). [doi:10.1523/eneuro.0007-21.2021](https://doi.org/10.1523/eneuro.0007-21.2021)

Dataset. [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.261123.1703) (AJILE12), version
0.261123.1703, streamed with the entry's helper `ajile.py`. The earlier attempt, peterson-2021-01,
used version 0.220127.0436.

The repeat attempt peterson-2021-02 reports most of the earlier findings again. This notebook checks
the four it does not report (1, 6, 8 and 11), one section each, opening with the earlier statement.
A last section reruns the precentral power of the repeat attempt's helper with the ECoG read from its
`starting_time`, for the two outcomes on which the attempts differ.
""")
code("""
import os, time, zlib
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import pandas as pd
from scipy import stats
import ajile

pd.set_option("display.width", 200)
T0 = time.time()
assets = ajile.list_assets()
metas = ajile.load_all_meta(assets)
subjects = sorted({int(m["subject_id"]) for m in metas})
print("dandiset", ajile.DANDISET, "version", ajile.VERSION, ";", len(assets), "files,", len(subjects), "subjects,",
      sum(len(m["reaches"]) for m in metas), "events")
""", ["sanity"])

md("""
## Earlier finding 1

> In three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG holds 15.5 to 15.9 h and its
> starting_time is 0, while the reaches table and the pose run on a clock from midnight. The ECoG
> starts 29241 to 30682 s after midnight, the time missing from 24 h; ReachEvents and the session
> start time agree, and the movement response appears only with this shift (S06 day 3, precentral
> HFB +1.98 dB with it, -0.07 dB without). Read with starting_time as given, the event times point at
> the wrong ECoG or past its end.

For every file, the ECoG `starting_time`, its length, and whether it ends at 24 h; whether the
ReachEvents times equal the reaches table's start_time; and, for S06 day 3, the event-locked
precentral band power (baseline -1.5 to -1 s, 0 to 0.5 s, the helper's method and the electrodes
good in every file of the subject) with the ECoG read from its `starting_time` and from 0 s.
""")
code("""
rows = []
for m in metas:
    n = m["ecog_shape"][0] / m["ecog_rate"]
    rows.append(dict(subject=int(m["subject_id"]), day=int(m["session_id"]), ecog_start_s=m["ecog_start"], ecog_hours=round(n / 3600, 3),
                     ecog_end_s=round(m["ecog_start"] + n, 1), pose_start_s=m["pose_start"],
                     reachevents_vs_start_time_max_s=round(float(np.abs(m["event_times"] - m["reaches"].start_time.values).max()), 3)))
clock = pd.DataFrame(rows)
print(clock[clock.ecog_start_s != 0].to_string(index=False))
print("files with starting_time not 0:", int((clock.ecog_start_s != 0).sum()), "; files whose ECoG ends at 86400 s:",
      int((clock.ecog_end_s.round() == 86400).sum()), "of", len(clock))
print("files where ReachEvents and start_time differ by more than 1 s:",
      clock[clock.reachevents_vs_start_time_max_s > 1][["subject", "day", "reachevents_vs_start_time_max_s"]].values.tolist())
""")
code("""
files, _ = ajile.figshare_files()
roi_idx = None
W = {}
for s in subjects:
    pm, _ = ajile.load_projection(s, files)
    ms = [m for m in metas if int(m["subject_id"]) == s]
    a, _ = ajile.match_projection(pm, ms[0]["electrodes"].x.notna().values)
    roi_idx = [list(pm.columns).index(r) for r in ajile.ROIS]
    G = np.array([m["electrodes"].good.values.astype(bool) for m in ms])
    W[s] = dict(proj=a[:, roi_idx], G=G)

m6 = [m for m in metas if int(m["subject_id"]) == 6 and int(m["session_id"]) == 3][0]
good6 = W[6]["G"].all(0)
w6 = ajile.session_weights(W[6]["proj"], good6)
for label, t in (("ECoG read from its starting_time", m6["event_times"] - m6["ecog_start"]),
                 ("ECoG read from 0 s", m6["event_times"])):
    r = ajile.session_spectral(m6["asset_id"], t, good6, w6)
    pre = r["region"][:, 1]
    st = ajile.band_stats(pre - pre[..., ajile.BASE].mean(axis=-1, keepdims=True))
    ok = r["inside"] & np.isfinite(st["hfb_mean"])
    print(f"S06 day 3, {label}: {int(ok.sum())} of {len(t)} events with ECoG; precentral HFB median "
          f"{np.median(st['hfb_mean'][ok]):+.2f} dB, LFB {np.median(st['lfb_mean'][ok]):+.2f} dB")
""")
md("""
Result: fixed. The three files now give the ECoG `starting_time` as 30682.414 s (sub-01 day 7),
30048.322 s (sub-04 day 3) and 29240.566 s (sub-06 day 3), so their ECoG ends at 86400 s, on the clock
of the reaches table, ReachEvents and the pose; the other 52 files start at 0 s. Read from its
`starting_time`, the S06 day 3 ECoG shows the movement response; read from 0 s it does not (the
numbers are printed above).
""")

md("""
## Earlier finding 6

> session_start_time is 19:00 at UTC-5 for files that start at local midnight (midnight UTC written
> in another zone), and 03:07 to 03:31 at UTC-5 for the three files whose ECoG starts later.
""")
code("""
sst = pd.DataFrame([dict(subject=int(m["subject_id"]), day=int(m["session_id"]), session_start_time=m["session_start"]) for m in metas])
print("times of day and zones of session_start_time:", sst.session_start_time.str[10:].value_counts().to_dict())
print(sst[(sst.subject.isin([1, 4, 6]))].to_string(index=False))
""")
md("""
Result: fixed. All 55 files give session_start_time at 00:00:00+00:00 of their day, including the
three files whose ECoG starts later, which now carry that delay in the ECoG `starting_time`
(finding 1).
""")

md("""
## Earlier finding 8

> The subjects' sex and age, which the paper reports, are not in the files or the archive's metadata.
""")
code("""
subj = pd.DataFrame([dict(subject=int(m["subject_id"]), sex=m["sex"], age=m["age"]) for m in metas]).drop_duplicates()
print(subj.to_string(index=False))
print("subjects with more than one sex or age across files:", int((subj.groupby("subject").size() > 1).sum()))
ages = subj.age.str.extract(r"P(\\d+)Y")[0].astype(float)
print("male:", int((subj.sex == "M").sum()), "female:", int((subj.sex == "F").sum()),
      f"; age mean {ages.mean():.2f} SD {ages.std():.2f} (paper: 8 male, 4 female, 29.4 +- 7.9 years)")
""")
md("""
Result: fixed. Every file gives the subject's sex and age (ISO 8601 durations); 8 subjects are male
and 4 female, with a mean age of 29.42 years (SD 7.94), the paper's values.
""")

md("""
## Earlier finding 11

> The electrode group descriptions and the data descriptor's Table 2 disagree for two subjects. S11
> has groups LATD, LMTD and LTPD described as depth (18 electrodes), where the descriptor gives S11
> 106 surface and no depth electrodes; S10 has 78 electrodes in groups not described as depth and 48
> in depth groups, where the descriptor gives 86 and 40.

The groups of S10 and S11 with their descriptions and electrode counts, in each of their files. The
descriptor's counts are those the earlier statement quotes (doi 10.1038/s41597-022-01280-y, Table 2).
""")
code("""
for s in (10, 11):
    for m in [m for m in metas if int(m["subject_id"]) == s]:
        el = m["electrodes"]
        desc = el.group_name.map(m["groups"]).fillna("")
        dep = desc.str.contains("depth", case=False)
        if int(m["session_id"]) == 3:
            print(f"S{s} groups:", el.assign(description=desc).groupby(["group_name", "description"]).size().to_dict())
        print(f"S{s} day {m['session_id']}: {int((~dep).sum())} electrodes in groups not described as depth, {int(dep.sum())} in depth groups")
""")
md("""
Result: still present. In every file S10 has 78 electrodes in groups not described as depth and 48 in
groups described as depth (AHD, AID, MHD, MID, PID), and S11 has 88 and 18 (LATD, LMTD and LTPD, each
described as depth), against the descriptor's 86 and 40, and 106 and 0.
""")

md("""
## The ECoG starting_time and two outcomes of peterson-2021-02

The repeat attempt's helper places each event at sample `event time x 500` of the ECoG
(`ajile.session_spectral`, "series starts at 0 s"), which ignores the `starting_time` of the three
files of finding 1. Here every file's precentral power is computed with the same helper and the same
rules for keeping events (`reproduce_peterson_2021.ipynb`, cell 12), with the event times less the
`starting_time`, under four sets of good electrodes: good in every file of the subject (the repeat
attempt's main set), each file's own flags (the set its outcome of fig5-recording-day-effects rests
on), good in at least one file, and the first file's flags (the earlier attempt's set, as the paper's
code takes them). For each set it gives the parts of fig4-precentral-subject-variability and the
count of fig5-recording-day-effects, as the claims file's criteria define them.
""")
code("""
t = time.time()
jobs, keys = [], []
for s in subjects:
    proj, G = W[s]["proj"], W[s]["G"]
    sets = {"good in every file": G.all(0), "good in at least one file": G.any(0), "first file's flags": G[0]}
    wv0 = {k: ajile.session_weights(proj, g) for k, g in sets.items()}
    for i, m in enumerate([m for m in metas if int(m["subject_id"]) == s]):
        wv = dict(wv0)
        wv["each file's flags"] = ajile.session_weights(proj, G[i])
        jobs.append((m["asset_id"], m["event_times"] - m["ecog_start"], G.all(0), wv["good in every file"], wv))
        keys.append((s, int(m["session_id"])))
spec = ajile.run_spectral(jobs, workers=8)
print(f"spectral pass {time.time() - t:.0f} s")
""")
code("""
E = pd.concat([pd.DataFrame(dict(subject=s, day=d, inside=r["inside"], allzero=r["allzero"], seg_db=r["seg_db"], hf_db=r["hf_db"],
                                 mism=np.abs(m["event_times"] - m["reaches"].start_time.values) > 1))
               for (s, d), r, m in zip(keys, spec, [m for s in subjects for m in metas if int(m["subject_id"]) == s])], ignore_index=True)
ok = E.inside & E.hf_db.notna()
thr = E[ok].groupby("subject").hf_db.agg(lambda x: x.mean() + 3 * x.std())
E["keep"] = E.inside & E.seg_db.notna() & ~E.allzero & ~(E.seg_db < 0) & ~(E.hf_db > E.subject.map(thr)) & ~E.mism
print("events kept:", int(E.keep.sum()), "of", len(E), "; per subject:", E[E.keep].groupby("subject").size().to_dict())
print("kept in the three files of finding 1:", {f"S{s:02d} day {d}": int(E[(E.subject == s) & (E.day == d)].keep.sum()) for s, d in ((1, 7), (4, 3), (6, 3))})
F = ajile.FREQS
paper_sig = {"lfb": {3, 5, 6, 7, 8, 11}, "hfb": {3, 4, 7, 8, 10}}
kb, sv = E.keep.values, E.subject.values
for name in ("good in every file", "each file's flags", "good in at least one file", "first file's flags"):
    R = np.concatenate([r["region_var"][name][:, 1] for r in spec])
    RB = R - R[..., ajile.BASE].mean(axis=-1, keepdims=True)
    SM = np.stack([np.nanmedian(RB[kb & (sv == s)], axis=0) for s in subjects])
    P = SM - SM[..., ajile.BASE].mean(axis=-1, keepdims=True)
    sp = P[..., ajile.WIN].mean(axis=-1)
    lf, hf = sp[:, ajile.LFB].mean(1), sp[:, ajile.HFB].mean(1)
    part1 = [f"S{s:02d}" for s, a, b in zip(subjects, lf, hf) if not (a < 0 and b > 0)]
    i116, i121 = list(F).index(116), list(F).index(121)
    part2 = all(sp[subjects.index(s), i116] > 0 and sp[subjects.index(s), i121] > 0 for s in [3, 6, 7, 8, 11])
    part3 = {}
    for s in [9, 12]:
        x = sp[subjects.index(s)]; hi = F >= 56; fmax = F[hi][np.argmax(x[hi])]
        part3[f"S{s:02d}"] = (int(fmax), bool(61 <= fmax <= 76 and x[F >= 101].mean() < x[hi].max() / 2))
    width = {f"S{s:02d}": int((sp[i][F <= 46] < sp[i][F <= 46].min() / 2).sum()) for i, s in enumerate(subjects)}
    print(f"=== {name}")
    print(f"fig4 part 1, subjects without the pattern: {part1} (S09 76-100 Hz {hf[subjects.index(9)]:.3f} dB); part 2 {part2}; part 3 {part3}")
    print("fig4 part 4, bins below half the minimum:", width)
    bs = ajile.band_stats(RB)
    for st in ("mean", "median"):
        agree, dis = 0, []
        for s in subjects:
            for b in ("lfb", "hfb"):
                g = E[kb & (sv == s)].assign(v=bs[f"{b}_{st}"][kb & (sv == s)])
                p = stats.kruskal(*[x.v.values for _, x in g.groupby("day")]).pvalue
                row = (f"S{s:02d}", b, float(f"{p:.3g}"))
                if (p < 0.05) == (s in paper_sig[b]):
                    agree += 1
                else:
                    dis.append(row)
                if s in (1, 6) and st == "mean":
                    print("  ", row, "paper significant:", s in paper_sig[b])
        print(f"fig5-recording-day-effects, band {st}: {agree} of 24 pairs agree; disagreeing {dis}")
print(f"notebook run time {(time.time() - T0) / 60:.1f} min")
""")
md("""
With the ECoG read from its `starting_time`, the day effects of S01 (LFB and HFB) and S06 (HFB),
which the repeat attempt found where the paper has none, are no longer significant (the p values of
S01 and S06 are printed above). The counts of fig5-recording-day-effects and the parts of
fig4-precentral-subject-variability under each set of electrodes are printed above; the
reconciliation in `attempts/peterson-2021-02.yaml` quotes them.
""")
nb = dict(cells=cells, metadata={"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}, nbformat=4, nbformat_minor=5)
json.dump(nb, open("entries/peterson-2021/earlier_findings.ipynb", "w"), indent=1)
PYEOF
python $TMPDIR/nb/make.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd  sed -i '/^roi_idx = None$/d' entries/peterson-2021/earlier_findings.ipynb 2>/dev/null; grep -n "roi_idx = None" entries/peterson-2021/earlier_findings.ipynb; grep -n "def cmd_run\|def run\|notebooks\b\|--only\|stamp" tools/entry.py | head -30
```

```
41:   "source": "files, _ = ajile.figshare_files()\nroi_idx = None\nW = {}\nfor s in subjects:\n    pm, _ = ajile.load_projection(s, files)\n    ms = [m for m in metas if int(m[\"subject_id\"]) == s]\n    a, _ = ajile.match_projection(pm, ms[0][\"electrodes\"].x.notna().values)\n    roi_idx = [list(pm.columns).index(r) for r in ajile.ROIS]\n    G = np.array([m[\"electrodes\"].good.values.astype(bool) for m in ms])\n    W[s] = dict(proj=a[:, roi_idx], G=G)\n\nm6 = [m for m in metas if int(m[\"subject_id\"]) == 6 and int(m[\"session_id\"]) == 3][0]\ngood6 = W[6][\"G\"].all(0)\nw6 = ajile.session_weights(W[6][\"proj\"], good6)\nfor label, t in ((\"ECoG read from its starting_time\", m6[\"event_times\"] - m6[\"ecog_start\"]),\n                 (\"ECoG read from 0 s\", m6[\"event_times\"])):\n    r = ajile.session_spectral(m6[\"asset_id\"], t, good6, w6)\n    pre = r[\"region\"][:, 1]\n    st = ajile.band_stats(pre - pre[..., ajile.BASE].mean(axis=-1, keepdims=True))\n    ok = r[\"inside\"] & np.isfinite(st[\"hfb_mean\"])\n    print(f\"S06 day 3, {label}: {int(ok.sum())} of {len(t)} events with ECoG; precentral HFB median \"\n          f\"{np.median(st['hfb_mean'][ok]):+.2f} dB, LFB {np.median(st['lfb_mean'][ok]):+.2f} dB\")"
18:- notebooks are committed without outputs;
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
188:    listed = [n["path"] for n in entry.get("notebooks", [])]
235:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
424:            # attempt's notebooks and cells are checked only when it was made, not against the entry as it is now
527:    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
539:    for nb in entry["notebooks"]:
565:    """A hash of everything a run of the entry's notebooks reads from the repository: every file of t
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021; python - <<'EOF'
import json
p='earlier_findings.ipynb'; nb=json.load(open(p))
for c in nb['cells']:
    c['source']=c['source'].replace("roi_idx = None\n","")
json.dump(nb,open(p,'w'),indent=1)
EOF
python - <<'EOF'
p='entry.yaml'; s=open(p).read()
s=s.replace("""  runtime_minutes: 60
helpers:""","""  runtime_minutes: 60
- path: earlier_findings.ipynb
  title: Findings of the earlier attempt peterson-2021-01, checked on this version
  runtime_minutes: 15
helpers:""")
open(p,'w').write(s)
EOF
cat entry.yaml | sed -n 9,20p; cd ../..; python tools/entry.py lock entries/peterson-2021 2>&1 | tail -3; python tools/entry.py check entries/peterson-2021 2>&1 | tail -10
```

```
matrices from Figshare, and the single-event regression models of Figure 6.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson et al. (2021) from dandiset 000055
  runtime_minutes: 60
- path: earlier_findings.ipynb
  title: Findings of the earlier attempt peterson-2021-01, checked on this version
  runtime_minutes: 15
helpers:
- ajile.py
wrote peterson-2021/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff --stat entries/peterson-2021/requirements.lock.txt; date -u; python tools/entry.py run entries/peterson-2021 2>&1 | tail -25; date -u
```

```
Wed Nov 25 16:04:12 UTC 2026
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
pass  reproduce_peterson_2021.ipynb  (1790 s)
pass  earlier_findings.ipynb  (570 s)
Wed Nov 25 16:43:37 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/peterson-2021/; python - <<'EOF'
import json
nb=json.load(open('executed/peterson-2021/earlier_findings.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print(''.join(o['text']))
            elif 'data' in o: print(''.join(o['data'].get('text/plain','')))
        print('-----')
EOF
```

```
earlier_findings.ipynb
reproduce_peterson_2021.ipynb
result.json
dandiset 000055 version 0.261123.1703 ; 55 files, 12 subjects, 8088 events

-----
 subject  day  ecog_start_s  ecog_hours  ecog_end_s  pose_start_s  reachevents_vs_start_time_max_s
       1    7     30682.414      15.477     86400.0           0.0                            0.001
       4    3     30048.322      15.653     86400.0           0.0                            0.001
       6    3     29240.566      15.878     86400.0           0.0                            0.001
files with starting_time not 0: 3 ; files whose ECoG ends at 86400 s: 55 of 55
files where ReachEvents and start_time differ by more than 1 s: [[8.0, 4.0, 86400.0]]

-----
entries/peterson-2021/ajile.py:332: RuntimeWarning: invalid value encountered in divide
  w = w / w.sum(axis=0)

S06 day 3, ECoG read from its starting_time: 165 of 166 events with ECoG; precentral HFB median +1.95 dB, LFB -1.54 dB

S06 day 3, ECoG read from 0 s: 83 of 166 events with ECoG; precentral HFB median -0.10 dB, LFB +0.32 dB
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "pilot-1[4-8]\|pilot 1[4-8]" docs/*.md schemas/*.json | grep -v "^docs/pilot-notes/" | head -20; sed -n 575,595p docs/protocol.md
```

```
docs/pilot-notes.md:414:## Protocol pilot-14 (2026-11-09): papers first, and every dataset a paper rests on
docs/protocol.md:3:Version: `pilot-18`. Record this version in the attempt's provenance.
docs/protocol.md:586:  Attempts made before `pilot-18` did not rate their findings. A later review
schemas/attempt.schema.json:467:            "description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).",
schemas/attempt.schema.json:552:            "description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.",
schemas/attempt.schema.json:739:      "description": "For an attempt made before protocol pilot-18, whose findings carry no severity: the severity a later review gave each finding about the data, and whether the review checked it against the notebook's outputs. Added to the record afterwards; nothing else in the record changes.",
  established, say), rate what was shown, at most `major`.

  A `critical` rating is a public statement about someone's data, so the
  verifier reviews each one in round 2. The revision records what it said
  under that round's `findings`: the finding's number in the record (from 1),
  `agrees`, the `severity` the verifier would give where it differs, and its
  `reason`. Where the verifier did not agree, the revision changes the rating
  to the verifier's, or keeps it and says why under `response`. Findings keep
  their order from then on, and a new one goes at the end. The site presents
  a critical finding as one only when a verifier agreed.

  Attempts
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
f=s['properties']['findings']
print(json.dumps(f,indent=1)[:3500])
EOF
tail -5 attempts/peterson-2021-02.yaml; grep -n "^findings:" -A3 attempts/peterson-2021-02.yaml; grep -n "^verifications:" attempts/peterson-2021-02.yaml
```

```
{
 "description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).",
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "kind",
   "statement"
  ],
  "properties": {
   "kind": {
    "enum": [
     "metadata_error",
     "data_missing",
     "identifier_missing",
     "metadata_insufficient",
     "selection_undocumented",
     "methods_unavailable",
     "format_error",
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/peterson-2021-02.yaml",
 "offset": 498,
 "limit": 14
}
```

```
498	  statement: Question for the authors. The dataset's good-electrode flags differ between a subject's
499	    days. Were bad electrodes removed per day or per subject, and did the analyses use the electrodes
500	    good on every day? This attempt used the electrodes good on every day for the projection and the
501	    regression; with each day's own flags, the recording-day effects of 20 of 24 subject and band
502	    pairs agree with the paper, against 18, and removing only the electrodes bad on every day gives
503	    21. Each day's flags remove 4.2 surface electrodes per subject on average, the closest to the
504	    paper's 4.9.
505	- kind: metadata_insufficient
506	  severity: minor
507	  statement: In sub-09 and sub-10 every analysed event has, on 1 to 15 electrodes marked good in
508	    every file, a run of at least 25 exact zero samples (50 ms) within the 10 s around it; no other
509	    subject has such runs. The files do not say what the zeros mean. Leaving those electrodes out of
510	    each event changes no outcome of this attempt.
511	verifications:
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/asari-2009-02.yaml; awk '/^reconciliation:/,0' attempts/asari-2009-02.yaml | head -60
```

```
1:schema_version: 3
2:id: asari-2009-02
3:datasets:
9:paper: doi:10.1152/jn.00577.2009
10:date: '2026-11-14'
11:entry: asari-2009
12:provenance:
23:outcomes:
627:verifications:
1015:findings:
1115:reconciliation:
1204:findings_review:
reconciliation:
  earlier: asari-2009-01
  date: '2026-11-18'
  blind: false
  blind_note: In its first revision run (author-revise-1) the author listed transcripts/asari-2009/, which
    still held the transcripts of asari-2009-01, and printed the first 50 lines of that attempt's verifier-2-report.md;
    its report says these showed the earlier outcomes and the earlier Figure 7 finding, and that it read
    nothing more of them. The transcript does not keep that output. The first author run did not see them,
[... 52 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/peterson-2021-02.yaml",
 "old_string": "    each event changes no outcome of this attempt.\nverifications:",
 "new_string": "    each event changes no outcome of this attempt.\n- kind: metadata_error\n  severity: minor\n  found: on_prompt\n  statement: The electrode group descriptions and the data descriptor's Table 2 (doi\n    10.1038/s41597-022-01280-y) disagree for two subjects. sub-11 has groups LATD, LMTD and LTPD\n    described as depth (18 electrodes), where the descriptor gives 106 surface and no depth\n    electrodes; sub-10 has 78 electrodes in groups not described as depth and 48 in depth groups,\n    where the descriptor gives 86 and 40.\nverifications:"
}
```

```
The file attempts/peterson-2021-02.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  cat >> attempts/peterson-2021-02.yaml <<'EOF'
reconciliation:
  earlier: peterson-2021-01
  date: '2026-11-25'
  blind: true
  findings:
  - finding: 1
    status: fixed
    note: earlier_findings.ipynb finds the ECoG starting_time of the three files now set to 30682.414,
      30048.322 and 29240.566 s, so all 55 files end at 86400 s on the clock of the events, and S06 day
      3 gives precentral HFB +1.95 dB with the ECoG read from its starting_time against -0.10 dB from 0
      s. Finding 2 of peterson-2021-02 names the same three files, but its helper reads their ECoG from
      0 s (ajile.py, session_spectral), so the ECoG it reports as ending early starts late.
  - finding: 2
    status: still_present
    now: 1
    note: Finding 1 of peterson-2021-02 reports the same 8088 events, 211 to 996 per subject (median
      770.5), with nothing in the files marking the false positives or the events the paper used.
  - finding: 3
    status: still_present
    now: 6
    note: Finding 6 of peterson-2021-02 reports the same reach angle without a stated convention, in
      image coordinates from -180 to 180 degrees, so that upward reaches are negative.
  - finding: 4
    status: still_present
    now: 5
    note: Finding 5 of peterson-2021-02 reports the same pose series labelled in meters and holding
      pixels.
  - finding: 5
    status: still_present
    now: 4
    note: Finding 4 of peterson-2021-02 reports the same bimanual overlap described as a fraction, with
      the same 1708 of 8088 values above 1 (up to 3.83).
  - finding: 6
    status: fixed
    note: earlier_findings.ipynb finds session_start_time at 00:00:00+00:00 of its day in all 55 files,
      the three files whose ECoG starts later included; their delay is now in the ECoG starting_time.
  - finding: 7
    status: still_present
    now: 3
    note: Finding 3 of peterson-2021-02 reports the same stretches of NaN ECoG samples, which the files
      do not describe, in 125 events against the earlier 124.
  - finding: 8
    status: fixed
    note: earlier_findings.ipynb finds sex and age in every file, 8 male and 4 female subjects with a
      mean age of 29.42 years (SD 7.94), the paper's values.
  - finding: 9
    status: still_present
    now: 11
    note: Finding 11 of peterson-2021-02 reports the same seven subjects (sub-01, 02, 03, 09, 10, 11 and
      12) with electrode groups described as depth, against the paper's five.
  - finding: 10
    status: still_present
    now: 7
    note: Finding 7 of peterson-2021-02 reports the same good flags differing between a subject's files
      (bad in at least one file 3 to 32 per subject), with nothing saying which applies.
  - finding: 11
    status: still_present
    now: 18
    note: earlier_findings.ipynb finds in every file of S10 78 electrodes in groups not described as
      depth and 48 in depth groups, and in S11 88 and 18 (LATD, LMTD and LTPD), as before. The
      descriptor's counts are those of the earlier statement, as the descriptor is not in the repository.
  - finding: 12
    status: still_present
    now: 14
    note: Finding 14 of peterson-2021-02 asks the authors the same question, how segment power is pooled
      over electrodes and frequencies for the 0 dB and 3 SD rules, and over which segments the SD is
      taken.
  - finding: 13
    status: still_present
    now: 15
    note: Finding 15 of peterson-2021-02 asks the same question, which measure makes low-frequency
      decreases more spatially widespread, with region counts tied and bins per frequency favouring the
      low frequencies.
  outcomes:
  - claim: fig4-precentral-subject-variability
    earlier: reproduced
    cause: reading
    choice: When a subject's files flag different electrodes as bad, which flags apply; the earlier
      attempt took each subject's first file's flags, as the paper's code does, and this attempt the
      electrodes good in every file, with each file's own flags as the variant it cites.
    note: The outcome turns on part 1 for S09, whose precentral 76-100 Hz mean on this version with this
      attempt's code is 0.097 dB with the first file's flags, against -0.039 dB with the electrodes good
      in every file and -0.030 with each file's flags (earlier_findings.ipynb). Part 4 needs a tie-break
      under every set, as S04 has 3 bins, tied with S03 and S05 behind S07 and S08 under the first
      file's flags; the earlier attempt passed it with its interpolated width. This attempt's 2 bins for
      S04 under each file's flags come from the ECoG of S04 day 3 read from 0 s (3 bins when it is read
      from its starting_time).
    confidence: medium
  - claim: fig5-recording-day-effects
    earlier: reproduced
    cause: error
    error_in: this
    note: ajile.py, session_spectral, places each event at sample event time x 500 ("series starts at 0
      s") and ignores the ECoG starting_time of sub-01 day 7, sub-04 day 3 and sub-06 day 3 (29240.566
      to 30682.414 s), so their events were read about 8 h late, which gives the day effects of S01 LFB
      (p = 0.047), S01 HFB (0.023) and S06 HFB (6.7e-11) where the paper has none. Read from the
      starting_time with each file's flags, these give p = 0.777, 0.0546 and 0.847, and 23 of 24 pairs
      agree, S10 HFB (p = 0.0935) the one left; with the first file's flags, the earlier attempt's set,
      24 of 24 agree (earlier_findings.ipynb), so the choice of electrodes decides the rest.
    confidence: medium
  protocol: The pilot notes have a heading after pilot-13 only for pilot-14, which files records by
    paper, with one claims file per paper and datasets that could not be used listed under
    missing_datasets; the paper rests on one dandiset, so it changes nothing here. Pilot-15 to pilot-17
    have no notes. From pilot-18 (docs/protocol.md) an attempt rates each finding about the data by
    severity and the round-2 verifier reviews every critical rating; this attempt rated its findings
    (one major, none critical), and the earlier attempt's were rated afterwards under findings_review.
    No change touches a criterion or an analysis rule, and neither outcome difference comes from the
    protocol.
EOF
python tools/entry.py check entries/peterson-2021 2>&1 | tail -5; python - <<'EOF'
import yaml,re
a=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
print(len(a['findings']), a['findings'][-1]['found'])
txt=open('attempts/peterson-2021-02.yaml').read().split('\nreconciliation:')[1]
print('emdash' , '—' in txt, 'rather', 'rather' in txt.lower())
EOF
```

```
0 error(s)
18 on_prompt
emdash False rather False
```

**Agent calls Bash**

```bash
cd  git status --short; ls -la entries/peterson-2021/.claude; git check-ignore -v entries/peterson-2021/.claude executed 2>&1 | head
```

```
M attempts/peterson-2021-02.yaml
 M entries/peterson-2021/entry.yaml
 M tools/build_site.py
 M tools/site_assets/app.css
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
?? earlier-entry/
?? entries/peterson-2021/earlier_findings.ipynb
?? scripts
?? tools/publish_site.py
total 12
drwxr-xr-x 3 runner runner 4096 Nov 25 15:44 .
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc .idea .vscode scripts | head -40; ls -la entries/peterson-2021/.claude/.cc-writes
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 25 15:33 scripts
total 8
drwx------ 2 runner runner 4096 Nov 25 15:44 .
drwxr-xr-x 3 runner runner 4096 Nov 25 15:44 ..
```

**Agent**

I've written the reconciliation block in `attempts/peterson-2021-02.yaml` and added `entries/peterson-2021/earlier_findings.ipynb`. The entry check reports 0 errors, and both notebooks passed a clean run (the main one in 1790 s, the new one in 570 s). Nothing is committed.

The main result: the blind attempt has a bug in its own code. Its helper (`ajile.py`, `session_spectral`, line 357) assumes every ECoG recording starts at 0 s. In this version the dataset fixed the earlier attempt's finding 1: three files (sub-01 day 7, sub-04 day 3, sub-06 day 3) now set their ECoG `starting_time` to 29240.566–30682.414 s. As a result, peterson-2021-02 read those files' events about 8 h late.

**1. Blind:** yes (`blind: true`). The audit lines are only the generic pilot-notes link, the registry README, and the author writing its own record. None point at an earlier attempt's results.

**2. Earlier findings**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | ECoG `starting_time` 0 in three late-starting files | fixed (checked in notebook) | – |
| 2 | 8088 events, false positives not marked | still_present | 1 |
| 3 | Reach angle convention not stated | still_present | 6 |
| 4 | Pose labelled meters, holds pixels | still_present | 5 |
| 5 | Bimanual overlap: 1708 values above 1 | still_present | 4 |
| 6 | `session_start_time` at 19:00 UTC-5 | fixed (checked) | – |
| 7 | NaN ECoG stretches | still_present | 3 |
| 8 | Sex and age missing | fixed (checked) | – |
| 9 | Seven subjects with depth groups, paper says five | still_present | 11 |
| 10 | `good` flags differ between a subject's files | still_present | 7 |
| 11 | S10/S11 group descriptions disagree with the data descriptor's Table 2 | still_present (checked), added as finding 18 with `found: on_prompt`, severity minor | 18 |
| 12 | Bad-segment rule unclear (question for authors) | still_present | 14 |
| 13 | "More widespread" measure unclear (question for authors) | still_present | 15 |

For finding 11, I compared the files against the descriptor's counts as quoted in the earlier statement, because the descriptor itself is not in the repository.

**3. New findings:** 2, 8, 9, 10, 12, 13, 16, 17. Finding 2 ("ECoG ends hours early, 237 events without neural data") comes from the bug: the ECoG actually starts late. I left the blind attempt's statements as they are.

**4. Outcomes that differ**
- **fig5-recording-day-effects** (earlier reproduced, now partially_reproduced): cause `error`, `error_in: this`, confidence medium.
  - The misread files produce the day effects the attempt reports for S01 LFB (p = 0.047), S01 HFB (0.023) and S06 HFB (6.7e-11), where the paper has none.
  - Read from `starting_time`, those become 0.777, 0.0546 and 0.847. Under each file's own electrode flags (the set the attempt's outcome rests on), 23 of 24 pairs then agree; S10 HFB (p = 0.0935) is the one left.
  - With the earlier attempt's electrode set (each subject's first file's flags), 24 of 24 agree. So which bad-electrode flags are used decides what remains. I left `supports` out.
- **fig4-precentral-subject-variability** (earlier reproduced, now partially_reproduced): cause `reading`, confidence medium.
  - Part 1 for S09 turns on which bad-electrode flags apply: 0.097 dB with the first file's flags, against -0.039 / -0.030 dB with the new attempt's sets.
  - Part 4 needs a tie-break under every set. The new attempt's pass of part 4 under each file's flags relied on the misread S04 day 3 file.

**5. What did not fit**
- `docs/pilot-notes.md` has nothing for pilot-15 to pilot-17. The `protocol` note covers pilot-14 (records filed by paper, no effect here) and the pilot-18 severity ratings, which I took from `docs/protocol.md` and the schema.
- `git log` for the earlier record points at HEAD because the checkout is shallow, so I used `earlier-entry/` for the earlier entry's files.
- The same bug affects every other ECoG claim of peterson-2021-02 (for example, Table 1's S06 values). Those outcomes match the earlier attempt's, so the protocol doesn't ask me to diagnose them, but they rest on misread data for three files.
- The last section of `earlier_findings.ipynb` reruns the whole spectral pass for the two outcome diagnoses. That goes beyond one section per finding; I added it so the numbers quoted in the reconciliation come from a committed notebook.

## End of run

53 turns, 61 minutes, $3.61 at API prices, result: success.
