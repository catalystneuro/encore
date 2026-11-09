# 000037 · verifier-2 · run 39745986906

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 1280
drwxr-xr-x 6 runner runner     4096 Oct 22 08:26 .
drwxr-xr-x 7 runner runner     4096 Oct 22 08:26 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .bashrc
drwxr-xr-x 5 runner runner     4096 Oct 22 08:26 .claude
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.development
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.development.local
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.local
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.production
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.production.local
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.test
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .env.test.local
drwx------ 2 runner runner       40 Oct 22 08:26 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .github
-rw-r--r-- 1 runner runner        0 Oct 22 08:25 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 22 08:09 .mcp.json
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat 000037-gillon-2023-01.yaml
```

```
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/82db1d18-0651-4d31-962b-ea7d93ed52de/tool-results/b6c8xgs7k.txt

Preview (first 2KB):
# Gillon, Lecoq et al. (2023) from dandiset 000037

Tests the data descriptor of [Gillon, Lecoq et al. (2023)](https://doi.org/10.1038/s41597-023-02214-y)
on [DANDI:000037](https://dandiarchive.org/dandiset/000037/0.230426.0054), the version the paper
cites. The dandiset holds two-photon imaging of L2/3 and L5 pyramidal cell somata and distal
apical dendrites in 13 mice over 50 sessions, with running, pupil and stimulus tables, each
session in three files.

| Claim | Outcome |
|---|---|
| Subjects, cohorts, sex split and session count (four claims) | Reproduced |
| Session attributes of Table 2 | Not reproduced |
| Two animals had sessions that failed QC | Blocked: metadata insufficient |
| Session schedule, imaging depths, acquisition rates | Reproduced |
| ROI noise rejection, ROI count ranges | Reproduced |
| Tracked ROI totals and tracking across sessions | Reproduced |
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls docs 2>&1 | head -2; cat 10.1038-s41597-023-02214-y.yaml
```

```
<persisted-output>
Output too large (44.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/82db1d18-0651-4d31-962b-ea7d93ed52de/tool-results/bbgo0cdne.txt

Preview (first 2KB):
ls: cannot access 'docs': No such file or directory
# Claims for Gillon, Lecoq et al. (2023, Sci Data 10, 287) on dandiset 000037.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Source: the version of record, full text as served by Europe PMC (PMC10192216), read from its
# Background, Methods, Data Records, Overview of data, Technical Validation, Usage Notes, Code
# availability, Tables 1 and 2 and the figure legends. No PDF was stored; no figure image was
# seen. The paper is a data descriptor: it states that it reports no statistical analyses, so
# no claim has statistics. Its only supplement, Supplementary Table 1 (session metadata), is
# also published as metadata.csv at https://github.com/jeromelecoq/allen_openscope_metadata
# (projects/credit_assignement, commit 0e9c7aca3d67cbab7c493ab824b7287fb9508f47); that copy was
# read. It holds the columns of Tables 1 and 2 plus local subject and session numbers, UTC
# imaging times, ages and experimental notes. The two other texts under paper/ (bioRxiv
# 10.1101/2021.01.15.426915 and J Neurosci 10.1523/jneurosci.1009-23.2023) are the analysis
# papers on the same data and are not the target here.
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/82db1d18-0651-4d31-962b-ea7d93ed52de/tool-results/b6c8xgs7k.txt"
}
```

```
1	# Gillon, Lecoq et al. (2023) from dandiset 000037
2	
3	Tests the data descriptor of [Gillon, Lecoq et al. (2023)](https://doi.org/10.1038/s41597-023-02214-y)
4	on [DANDI:000037](https://dandiarchive.org/dandiset/000037/0.230426.0054), the version the paper
5	cites. The dandiset holds two-photon imaging of L2/3 and L5 pyramidal cell somata and distal
6	apical dendrites in 13 mice over 50 sessions, with running, pupil and stimulus tables, each
7	session in three files.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Subjects, cohorts, sex split and session count (four claims) | Reproduced |
12	| Session attributes of Table 2 | Not reproduced |
13	| Two animals had sessions that failed QC | Blocked: metadata insufficient |
14	| Session schedule, imaging depths, acquisition rates | Reproduced |
15	| ROI noise rejection, ROI count ranges | Reproduced |
16	| Tracked ROI totals and tracking across sessions | Reproduced |
17	| Fig. 8 example matches and conflicts (four claims) | Reproduced |
18	| Somata less order dependent than dendrites in matching | Blocked: data missing |
19	| Gabor sequence structure | Partially reproduced |
20	| Visual flow structure, stimulus durations, inconsistent fractions and blocks | Reproduced |
[... 706 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/82db1d18-0651-4d31-962b-ea7d93ed52de/tool-results/bbgo0cdne.txt"
}
```

```
1	ls: cannot access 'docs': No such file or directory
2	# Claims for Gillon, Lecoq et al. (2023, Sci Data 10, 287) on dandiset 000037.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
4	# protocol as stated in docs/protocol.md (version pilot-10).
5	#
6	# Source: the version of record, full text as served by Europe PMC (PMC10192216), read from its
7	# Background, Methods, Data Records, Overview of data, Technical Validation, Usage Notes, Code
8	# availability, Tables 1 and 2 and the figure legends. No PDF was stored; no figure image was
9	# seen. The paper is a data descriptor: it states that it reports no statistical analyses, so
10	# no claim has statistics. Its only supplement, Supplementary Table 1 (session metadata), is
11	# also published as metadata.csv at https://github.com/jeromelecoq/allen_openscope_metadata
12	# (projects/credit_assignement, commit 0e9c7aca3d67cbab7c493ab824b7287fb9508f47); that copy was
13	# read. It holds the columns of Tables 1 and 2 plus local subject and session numbers, UTC
14	# imaging times, ages and experimental notes. The two other texts under paper/ (bioRxiv
15	# 10.1101/2021.01.15.426915 and J Neurosci 10.1523/jneurosci.1009-23.2023) are the analysis
16	# papers on the same data and are not the target here.
17	#
18	# Code read: https://github.com/colleenjg/OpenScope_CA_Analysis at commit
19	# 046e7fef5f452cdc0775fe54040b0f13aeae1e57 (2024-06-30), linked in Code availability and Usage
20	# Notes, with its dependency https://github.com/colleenjg/util (tag osca_mult, commit
[... 716 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_gillon_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    outs=''
    for o in c.get('outputs',[]):
        if 'text' in o: outs+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: outs+=''.join(o['data']['text/plain'])
        if o.get('output_type')=='error': outs+='ERROR '+o['ename']
    print(f"### CELL {i} [{c['cell_type']}] srclen={len(src)} outlen={len(outs)}")
EOF
```

```
### CELL 0 [markdown] srclen=3209 outlen=0
### CELL 1 [code] srclen=332 outlen=0
### CELL 2 [code] srclen=1498 outlen=84
### CELL 3 [markdown] srclen=88 outlen=0
### CELL 4 [code] srclen=981 outlen=365
### CELL 5 [markdown] srclen=190 outlen=0
### CELL 6 [code] srclen=3040 outlen=6802
### CELL 7 [markdown] srclen=409 outlen=0
### CELL 8 [code] srclen=2905 outlen=1223
### CELL 9 [markdown] srclen=513 outlen=0
### CELL 10 [code] srclen=1271 outlen=1756
### CELL 11 [markdown] srclen=248 outlen=0
### CELL 12 [code] srclen=1448 outlen=2667
### CELL 13 [markdown] srclen=686 outlen=0
### CELL 14 [code] srclen=896 outlen=134
### CELL 15 [markdown] srclen=130 outlen=0
### CELL 16 [markdown] srclen=510 outlen=0
### CELL 17 [code] srclen=1694 outlen=2356
### CELL 18 [markdown] srclen=477 outlen=0
### CELL 19 [markdown] srclen=176 outlen=0
[... 84 more lines not kept]
```

**Agent**

Cell numbering has changed since round 1 because the conclusion cells are back in. Next I'll dump the whole notebook and read it.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_gillon_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"### CELL {i} [{c['cell_type']}]")
    print(src)
    for o in c.get('outputs',[]):
        t=''
        if 'text' in o: t=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: t=''.join(o['data']['text/plain'])
        if o.get('output_type')=='error': t='ERROR '+o['ename']+o['evalue']
        print('--- OUT ---'); print(t)
EOF
wc -l $TMPDIR/nb.txt; echo $TMPDIR
```

```
2623 /tmp/claude-1001/nb.txt
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	### CELL 0 [markdown]
2	# Reproducing Gillon, Lecoq et al. (2023) from dandiset 000037
3	
4	Paper. Gillon CJ, Lecoq JA, Pina JE, et al. (2023). Responses of pyramidal cell somata and
5	apical dendrites in mouse visual cortex over multiple days. *Scientific Data* 10, 287.
6	[doi:10.1038/s41597-023-02214-y](https://doi.org/10.1038/s41597-023-02214-y). A data descriptor.
7	The claims file (`claims/000037/10.1038-s41597-023-02214-y.yaml`) was written from the version of
8	record as served by Europe PMC (PMC10192216), with Supplementary Table 1 read as metadata.csv of
9	the authors' metadata repository.
10	
11	Dandiset. [DANDI:000037](https://dandiarchive.org/dandiset/000037/0.230426.0054), version
12	0.230426.0054. The paper cites this version: its reference 13 carries the DOI
13	10.48324/DANDI.000037/0.230426.0054 (in the Crossref record of the article; the Europe PMC text
14	prints the reference without it). The later version 0.240209.1623 holds the same 150 NWB files
15	with the same blobs, and adds a CHANGES file and links to the papers in its metadata (shown in
16	the data check). Only the basic files (`behavior+ophys`) are opened; each is streamed into memory
17	once and nothing is written to disk.
18	
19	Outside inputs, all pinned and named in the helper `openscope_ca.py`: Supplementary Table 1
20	(metadata.csv of `jeromelecoq/allen_openscope_metadata` at commit 0e9c7ac), used for Tables 1 and
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 650
}
```

```
700	
701	Text fields mentioning ('qc', 'quality', 'pass', 'fail', 'exclu', 'reject') in any of the 50 files: none
702	Text fields per file: 23 to 23
703	
704	Every text field of 759666166 (mouse 411400, local session 1, Supplementary Table 1 QC failed):
705	  file_create_date: ['2022-09-24T22:32:36.231878-07:00', '2023-04-03T21:37:43.217912-07:00']
706	  identifier: 759666166
707	  session_description: Allen Institute OpenScope dataset
708	  session_start_time: 2018-10-01T18:02:56.523000-07:00
709	  timestamps_reference_time: 2018-10-01T18:02:56.523000-07:00
710	  /@.specloc: <HDF5 object reference>
711	  /@nwb_version: 2.5.0
712	  general/devices/2p_microscope@description: Allen Institute two-photon pipeline: CAM2P.1
713	  general/institution: Allen Institute for Brain Science
714	  general/optophysiology/ImagingPlane/description: ImagingPlane
715	  general/optophysiology/ImagingPlane/excitation_lambda: 910.0
716	  general/optophysiology/ImagingPlane/imaging_rate: 30.0
717	  general/optophysiology/ImagingPlane/indicator: GCaMP6f
718	  general/optophysiology/ImagingPlane/location: {'area': 'VISp', 'depth': '20'}
719	  general/optophysiology/ImagingPlane/optical_channel/description: 2P Optical Channel
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1349,
 "limit": 650
}
```

```
1349	    dirs = v.main_flow_direction.to_numpy()
1350	    changes = int((dirs[1:] != dirs[:-1]).sum())
1351	    contiguous = all(np.all(np.diff(v.index[v.main_flow_direction == d]) == 1) for d in set(dirs))
1352	    runs = []
1353	    for d in set(dirs):
1354	        u = v[v.main_flow_direction == d].unexpected.to_numpy()
1355	        dd = v[v.main_flow_direction == d]
1356	        edges = np.flatnonzero(np.diff(np.concatenate([[0], u, [0]])))
1357	        for a, b in zip(edges[::2], edges[1::2]):
1358	            runs.append(dd.stop_time.iloc[b - 1] - dd.start_time.iloc[a])
1359	    sq = S[sid]["squares"]
1360	    speed = {}
1361	    for k, (x, y, d) in sq.items():
1362	        dx = np.diff(x.astype(float), axis=1)
1363	        step = np.median(np.abs(dx[np.abs(dx) < 100]))           # px per stimulus frame (60 Hz), wraps excluded
1364	        speed[k] = step * 60
1365	        speed[k + "_dir"] = d
1366	        # Squares moving against the main flow at the trial's first frame (reversed squares that
1367	        # leave the screen re-enter with the main flow, so the fraction falls later in the trial).
1368	        moving = np.where(np.abs(dx[:, 0]) < 100, np.sign(dx[:, 0]), 0)
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1998,
 "limit": 630
}
```

```
1998	
1999	Per mouse, lowest and median SNR:
2000	                size    min  median
2001	group  subject                     
2002	L2/3-D 413663   1488  2.173   2.381
2003	       433414   1360  2.232   2.383
2004	L2/3-S 408021    277  2.229   3.496
2005	       411424    257  2.222   2.958
2006	       440889    658  2.180   2.760
2007	L5-D   420011    546  2.265   2.524
2008	       433448   2577  2.163   2.516
2009	       433451   2981  2.193   2.567
2010	L5-S   411771    239  2.303   3.513
2011	       418779     70  2.272   3.209
2012	       433458    283  2.226   3.005
2013	
2014	### CELL 87 [markdown]
2015	**Result: reproduced.** Under all three readings: every one of the 12 groups has a median SNR above 1
2016	(2.37 to 3.43) and a 5th percentile above 1 (2.27 to 2.41), and all 10736 ROIs exceed 1 (lowest
2017	2.16). No ROI has a negative median dF/F, so by the SNR's construction none could fall below
[... 607 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "assert|def windows|def grey_transitions|text_fields",
 "path": "openscope_ca.py",
 "output_mode": "content",
 "-C": 3
}
```

```
134-                 "start_frame_twop", "stop_frame_twop", "start_frame_stim", "stop_frame_stim"]
135-
136-
137:def text_fields(f: h5py.File, max_size: int = 64) -> dict:
138-    """Every small dataset and attribute under `general`, and the file's top-level datasets and
139-    attributes (start time, creation date, reference time, descriptions), as text."""
140-    out = {}
--
201-        "pupil_y": beh["PupilTracking/pupil_position_y/data"][:],
202-        "pupil_x_unit": beh["PupilTracking/pupil_position_x/data"].attrs.get("unit"),
203-        "trial_columns": sorted(trials.keys()),
204:        "text_fields": text_fields(f),
205-    }
206-    t = {}
207-    for c in TRIAL_COLUMNS:
--
258-    return (x - med) / (p95 - p5)
259-
260-
261:def windows(x, refs, pre_n, post_n):
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; grep -n -i "dropped\|notes\b\|seven minutes\|800 nm" nb.txt | head -20
```

```
49:The analysis streams about 25 GB and takes about seven minutes.
448:notes the laser was set to 800 nm). The second is not among the 33 analysed sessions; the first
1333:three sessions of mouse 411400 among them failed QC, and Supplementary Table 1 notes dropped
Shell cwd was reset to
```

**Agent**

# Round 2 verifier report: 000037-gillon-2023-01

## 1. Outcomes

The claims file has 35 claims, and the attempt record gives an outcome for each of the 35.

**I agree with 33 of 35 outcomes.** These are the 33 that are not fig5-consistent-vs-inconsistent or fig7c-high-correlation-fraction. The numbers behind them have not changed since round 1. In cell 63, gabor-sequence-structure is still `partially_reproduced`: 46 of 50 sessions pass, with 13 of 340000 images out of range. The record now says that a strict two-way reading would give `not_reproduced`.

**I disagree with 2 of 35, as in round 1:**
- **fig5-consistent-vs-inconsistent** (record: `blocked`; my outcome: `partially_reproduced`). Cell 80 gives scaled 2/4 under (a) and 3/4 under (b), and unscaled 2/4 under each. Both readings give partial, so the readings agree. The only reason for the block is the claims file's `depends_on`.
- **fig7c-high-correlation-fraction** (record: `blocked`; my outcome: `not_reproduced`). Cell 92 gives (a) 0.0178% (134 of 752101 pairs), (b) 0.0176%, and (c) 0.0211, 0.0276 and 0.0043% by session. None is inside 0.005–0.015%, and none depends on how "similar" is read.

The author keeps both blocks under protocol author step 1.5. I cannot read `docs/protocol.md`. If the rule is as the author states it, the blocks follow procedure. The disagreement and the outcomes each claim's own test gives are recorded in the attempt record, the notebook (cells 81 and 93) and the README.

## 2. Statements the printed outputs do not support

Nearly every number I checked matches the printed output, with one figure that does not: the run time (item 3). The exceptions are below.

1. **The start times are called "evening" (cell 30; attempt record table2-sessions notes).**
   - Cell 30: "Their start times are evening Pacific times stated with a Pacific offset (for example 2018-10-19T00:18-07:00)".
   - Attempt record: "Their start times are evening Pacific clock values stated with a Pacific offset".
   - Cells 6 and 29 print 00:18, 01:51, 03:01 and 01:06 with offsets of -07:00 or -08:00. As stated, these are early-morning Pacific times. They become evening Pacific times only if the clock is read as UTC, which is the variant the text says it does not adopt. The sentence assumes the reading it then calls not decisive.
2. **Supplementary Table 1's notes are cited but never printed (cell 63, gabor notes, finding 7).**
   - Cell 63: "Supplementary Table 1 notes dropped stimulus frames for them".
   - Cell 13 and finding 7: "Supplementary Table 1 notes the laser was set to 800 nm" and "failed QC with the laser at 800 nm".
   - No cell prints that table's notes column. Cell 8 prints an excitation of 910 nm for every file, 838633305 included. These sentences may be true, but nothing in the outputs shows them.
3. **The run time (README and cell 0).** Both say "takes about seven minutes". Cell 2 prints 664 s, which is about 11 minutes.
4. **The clock check in finding 7.** The finding says the dF/F response in two sessions "does not exceed that at shifted times". Cell 12 shows that 777496949 exceeds 94.6% of the shifted contrasts (rank 0.054) and only fails the 99th-percentile test. Cell 13 states this correctly; the finding overstates it.
5. **Running speed (cell 9, data check, not a conclusion).** The cell describes "a median near a few cm/s". Cell 8 prints a median of 0.081 cm/s across the session medians.

Everything else I checked agrees with the outputs:
- every other `**Result:` sentence: cells 18–102;
- the Summary table and its findings: cell 103;
- the README table and text;
- the other notes in the attempt record.

The record's round-1 entry gives my reasons faithfully, folding problems 3, 4, 6, 7 and 9 and the section C items into the relevant claims. Most of it is close to verbatim. Nothing material is left out or changed.

## 3. Round-1 points

| # | Point | Status |
|---|---|---|
| 1 | fig5-consistent-vs-inconsistent blocked only by dependency | **Not resolved.** The block is kept by procedure. The planes where both readings hold at once are now printed: 1 of 4, L5 dendrites (cell 80). Bears on a conclusion. |
| 2 | fig7c-high-correlation-fraction blocked only by dependency | **Not resolved**, for the same reason. Bears on a conclusion. |
| 3 | The UTC variant and the truncated start string in table2-sessions | **Resolved.** Start times are printed in full (cells 6 and 29). All time and date fields of the four files are printed, and the UTC reading is labelled a variant that does not decide the outcome. The "evening" wording (item 2.1) is new. |
| 4 | SNR > 1 holds by how SNR is built | **Resolved.** Cells 86 and 87 print 0 ROIs with a negative median. |
| 5 | Over-long Gabor images | **Resolved** as far as wording goes (cell 63). The "dropped frames" source is not shown (item 2.2). |
| 6 | QC search too narrow | **Resolved.** Cell 32 searches all 23 fields in every file; there are no matches, and all fields of 759666166 are printed. |
| 7 | Alignment of 777496949 | **Resolved.** Cell 98 prints 4.07 SEM at onset and 6.77 at offset next to the clock check. |
| 8 | Supplementary Table 1 against Tables 1 and 2, not run | Unchanged. Does not bear on a conclusion. |
| 9 | No assert on dropped transitions | **Resolved.** `openscope_ca.py:447` asserts that `dropped == 0`. |
| C | Fig. 5 thresholds | **Resolved.** Printed in cell 77. The comparison with the repository's Fig. 5 source data was not added, so the ROI selection is still checked only on synthetic inputs. |

**Still open and bearing on a conclusion:**
- **Points 1 and 2.** These are the outcomes of fig5-consistent-vs-inconsistent (`partially_reproduced` by its own test) and fig7c-high-correlation-fraction (`not_reproduced` by its own test). They stay blocked under a protocol rule I cannot check.

**Still open, not changing an outcome:**
- **Item 2.1, the "evening" wording.** It sits in table2-sessions, whose outcome is `not_reproduced` either way.

## End of run

14 turns, 2 minutes, result: success.
