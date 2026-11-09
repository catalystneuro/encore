# 000691 · verifier-2 · run 39554835498

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 3292
drwxr-xr-x 6 runner runner     4096 Oct 21 07:50 .
drwxr-xr-x 7 runner runner     4096 Oct 21 07:50 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .bashrc
drwxr-xr-x 5 runner runner     4096 Oct 21 07:50 .claude
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.development
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.development.local
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.local
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.production
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.production.local
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.test
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .env.test.local
drwx------ 2 runner runner       40 Oct 21 07:50 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .github
-rw-r--r-- 1 runner runner        0 Oct 21 07:50 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 06:20 .mcp.json
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo =====; cat 000691-scherrer-2023-02.yaml
```

```
<persisted-output>
Output too large (39.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/14c06081-39de-4ca2-add8-4b670fe131a9/tool-results/bjh44xl84.txt

Preview (first 2KB):
# Scherrer, Lynch, Zhang & Fee (2023) from dandiset 000691

Tests the findings of [Scherrer et al. (2023)](https://doi.org/10.1038/s41592-023-01806-1) on
[DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version 0.260827.1358,
which holds one session of one mouse imaged with the large-FOV head-mounted microscope (the
Kiloscope) while it explores a square loop maze: the raw imaging video, 2948 EXTRACT footprints
with their traces and masks, and a behaviour video. The claims file was written from the paper's
full text and its code; the optical measurements of five claims are read from the paper's code
repository, where the claims file places them.

| Claim | Outcome |
|---|---|
| Thousands of neurons imaged in a freely moving mouse | Reproduced |
| Field of view of 4.8 x 3.6 mm (with the code's pixel sizes) | Reproduced |
| Featherscope resolution about 4 um at the centre, 7 um at the edge | Reproduced |
| Kiloscope resolution about 4 um at the centre, 5 um at the edge | Partially reproduced |
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Scherrer, Lynch, Zhang & Fee (2023) from dandiset 000691
2	
3	Tests the findings of [Scherrer et al. (2023)](https://doi.org/10.1038/s41592-023-01806-1) on
4	[DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version 0.260827.1358,
5	which holds one session of one mouse imaged with the large-FOV head-mounted microscope (the
6	Kiloscope) while it explores a square loop maze: the raw imaging video, 2948 EXTRACT footprints
7	with their traces and masks, and a behaviour video. The claims file was written from the paper's
8	full text and its code; the optical measurements of five claims are read from the paper's code
9	repository, where the claims file places them.
10	
11	| Claim | Outcome |
12	|---|---|
13	| Thousands of neurons imaged in a freely moving mouse | Reproduced |
14	| Field of view of 4.8 x 3.6 mm (with the code's pixel sizes) | Reproduced |
15	| Featherscope resolution about 4 um at the centre, 7 um at the edge | Reproduced |
16	| Kiloscope resolution about 4 um at the centre, 5 um at the edge | Partially reproduced |
17	| Flat illumination with the axicon correction (Featherscope, Kiloscope) | Reproduced (both) |
18	| Motion of the field of view of 0.13 pixels RMS | Not reproduced |
19	| Quadrant and direction, and octant, decoded above shuffled data; decoder size; local decoding maps | Blocked: not runnable within the time limit |
20	| Coactive footprints spread across the field of view; footprints with localized activity; field curvature; LMAN bursting (whose data are also missing) | Blocked: methods underspecified |
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000691-scherrer-2023-02.yaml"
}
```

```
1	schema_version: 2
2	id: 000691-scherrer-2023-02
3	dataset:
4	  archive: dandi
5	  id: "000691"
6	  version: 0.260827.1358
7	  doi: 10.48324/dandi.000691/0.260827.1358
8	paper: doi:10.1038/s41592-023-01806-1
9	date: 2026-10-20
10	entry: 000691-scherrer-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	inputs:
20	- what: Bead image stacks and their region lists (f2+sf4/feather, f2+sf4/feather_roi.csv,
[... 551 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-s41592-023-01806-1.yaml"
}
```

```
1	# Claims for Scherrer, Lynch, Zhang & Fee (2023) on dandiset 000691.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
3	# protocol as stated in docs/protocol.md (version pilot-10).
4	#
5	# Text read: the version of record (Nature Methods 20, 546-549), from a PDF supplied by a person,
6	# as extracted text in paper/10.1038-s41592-023-01806-1.txt. It holds the main text, the figure
7	# legends, the Methods, the Extended Data legends (Extended Data Figs. 1 to 10) and the reporting
8	# summary. The supplementary information is two videos (Supplementary Videos 1 and 2), which no
9	# result rests on. The PDF was not opened; the numbers needed were in the text. In the extracted
10	# text, the sentence on the Featherscope's resolution (page 547) is split by figure labels, its
11	# second half placed before its first; the quote of fig1e-featherscope-psf is that second half, and
12	# its first half reads "The Featherscope has a resolution of approximately 4 μm at the".
13	#
14	# Rewritten 2026-10-20 from the full text. The earlier file was written from the abstract and the
15	# public figure legends, and its criteria were written after its author had seen the data check
16	# and a prototype decoder. This file is written from the paper and its code alone, by a reader
17	# who has not seen the dandiset's data. What changed, and why:
18	# - ed9c-local-decoding-map: the null is now the paper's (Methods, Data analysis, paragraph 5),
19	#   a thousand decoders trained on shuffled data from 32 randomly chosen footprints, where each
20	#   footprint's trace is circularly shifted by its own random offset. The earlier null shifted the
[... 551 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== [{i}] {c['cell_type']} =====")
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--out--'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--out--'); print(''.join(d['text/plain']))
            elif 'image/png' in d: print('--out-- [image]')
        if o.get('output_type')=='error': print('--ERROR--',o.get('ename'),o.get('evalue'))
EOF
for f in *.ipynb; do python3 $TMPDIR/dump.py $f > $TMPDIR/${f%.ipynb}.txt; wc -l $TMPDIR/${f%.ipynb}.txt; done
```

```
128 /tmp/claude-1001/decoding_null_n2_octant.txt
129 /tmp/claude-1001/decoding_null_n2_quadrant_direction.txt
250 /tmp/claude-1001/decoding_octant.txt
309 /tmp/claude-1001/decoding_quadrant_direction.txt
220 /tmp/claude-1001/decoding_reduced.txt
321 /tmp/claude-1001/motion_scherrer_2023.txt
1515 /tmp/claude-1001/reproduce_scherrer_2023.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_scherrer_2023.txt"
}
```

```
1	===== [0] markdown =====
2	# Reproducing Scherrer, Lynch et al. (2023) from dandiset 000691
3	
4	Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
5	and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
6	[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).
7	
8	Claims. The claims file `claims/000691/10.1038-s41592-023-01806-1.yaml` was written on
9	2026-10-20 from the full text of the version of record (main text, figure legends, Methods,
10	Extended Data legends and reporting summary) and the paper's code, GitHub
11	`FeeLab/Feescope-Paper-Code` at commit d596646, by a reader who did not see the data, and checked
12	by a second reader. It decides what is tested and how. This is the second attempt on the dandiset
13	(`000691-scherrer-2023-02`); the first (`-01`) worked from claims written from the abstract and
14	the public legends, and is deprecated.
15	
16	Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
17	0.260827.1358. Why this version: the paper cites no DANDI version (its data statement points to an
18	Academic Torrents deposit), and 0.260827.1358 is the only published version, the one the first
19	attempt used. The draft was last modified when that version was published and holds the same two
20	assets with the same blobs (printed in the data check), so the data have not changed since the
[... 739 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_scherrer_2023.txt",
 "offset": 760,
 "limit": 760
}
```

```
760	        fit = ks.fit_bead(roi, s["dp"], s["start_at_max"], s["ftol"], s["max_nfev"], x_scale)
761	        hh, hw = (r.Height - 1) / 2, (r.Width - 1) / 2
762	        rad = s["dp"] * np.hypot(s["centre"][0] - (r.BY + hh + 1), s["centre"][1] - (r.BX + hw + 1))
763	        rows.append({"r_um": rad, "slice": r.Slice, **fit})
764	    out = pd.DataFrame(rows)
765	    g = s["groups"]
766	    out["group"] = g[np.abs(out.r_um.to_numpy()[:, None] - g[None]).argmin(1)]
767	    return out
768	
769	def readings(fits, name):
770	    s = psf_setups[name]
771	    by = fits.groupby("group")
772	    table = pd.DataFrame({"n": by.size(), "median_major": by.fwhm_major.median(), "median_minor": by.fwhm_minor.median(),
773	                          "mean_major": by.fwhm_major.mean(), "mean_minor": by.fwhm_minor.mean()}).round(3)
774	    centre_g, edge_g = s["groups"][0], s["groups"][-1]
775	    rows = []
776	    for label, col in [("(a) median major", "median_major"), ("(b) median minor", "median_minor"),
777	                       ("(c) mean major", "mean_major"), ("(d) mean minor", "mean_minor")]:
778	        cv, ev = table.loc[centre_g, col], table.loc[edge_g, col]
779	        rows.append({"reading": label, "centre_um": cv, "edge_um": ev,
[... 737 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/decoding_quadrant_direction.txt"
}
```

```
1	===== [0] markdown =====
2	# Scherrer, Lynch et al. (2023), dandiset 000691: decoding quadrant and direction
3	
4	Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
5	and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
6	[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).
7	
8	Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
9	version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
10	decides what is tested and how.
11	
12	Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
13	0.260827.1358, the only published version (the paper cites none); see the main notebook,
14	`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check. This notebook holds the
15	quadrant and direction decoding claims, apart to keep each notebook within the time limit.
16	
17	Footprints. The claims use the 2,382 curated footprints, with all 2,948 as a named variant.
18	The dandiset does not mark the curated set, so all 2,948 are used.
19	
20	| Claim | Data | Status |
[... 290 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/decoding_octant.txt"
}
```

```
1	===== [0] markdown =====
2	# Scherrer, Lynch et al. (2023), dandiset 000691: decoding octant
3	
4	Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
5	and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
6	[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).
7	
8	Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
9	version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
10	decides what is tested and how.
11	
12	Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
13	0.260827.1358, the only published version (the paper cites none); see the main notebook,
14	`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check. This notebook holds the
15	octant decoding claims, apart to keep each notebook within the time limit.
16	
17	Footprints. The claims use the 2,382 curated footprints, with all 2,948 as a named variant.
18	The dandiset does not mark the curated set, so all 2,948 are used.
19	
20	| Claim | Data | Status |
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat decoding_null_n2_quadrant_direction.txt; echo; echo '#################'; cat decoding_null_n2_octant.txt
```

```
===== [0] markdown =====
# Scherrer, Lynch et al. (2023), dandiset 000691: more (n2) null decoders for fig2-quadrant-direction-decoding

Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).

Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
decides what is tested and how.

Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
0.260827.1358, the only published version (the paper cites none); see the main notebook,
`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check.

Why this notebook. The criterion of fig2-quadrant-direction-decoding judges p under two readings of a null decoder: (n1)
one fit per shuffle and (n2) the average matrix of 200 fits per shuffle. The 1,000 (n2) decoders it
asks for need 200,000 fits, about 34 hours here (measured in the decoding notebook), and are not run. The first verification asked for
more of them, to show where they lie; this notebook runs 8, as many as fit within the time limit
of a notebook, beside the one in `decoding_quadrant_direction.ipynb`. They cannot give p < 0.001 and decide no
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat decoding_reduced.txt
```

```
===== [0] markdown =====
# Scherrer, Lynch et al. (2023), dandiset 000691: reduced runs of the decoder-size and map analyses

Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).

Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
decides what is tested and how.

Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
0.260827.1358, the only published version (the paper cites none); see the main notebook,
`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check.

Why this notebook. fig2k-decoder-size, fig2l-local-decoding-map and ed9c-local-decoding-map need
64,000 to 276,000 fits each, 4 to 11 hours on four cores, and are blocked as not runnable (their
cost is measured in the decoding notebooks). The first verification asked for any output of
them. This notebook runs each with far fewer fits, subsets, grid points and null decoders, choices
made here to fit the time limit of a notebook. They are not the criteria's methods and decide no
[... 201 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/motion_scherrer_2023.txt"
}
```

```
1	===== [0] markdown =====
2	# Scherrer, Lynch et al. (2023), dandiset 000691: motion of the field of view
3	
4	Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
5	and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
6	[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).
7	
8	Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
9	version of record and the paper's code. It decides what is tested and how.
10	
11	Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
12	0.260827.1358, the only published version (the paper cites none); see the main notebook,
13	`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check. This notebook reads the
14	whole imaging movie (15 GB compressed, 36 GB as 16-bit values) by HTTP range requests, in blocks of
15	1200 frames held in memory, and registers every frame.
16	
17	| Claim | Data | Status |
18	|---|---|---|
19	| ed7-motion-small | dandiset | tested |
20	===== [1] code =====
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for s in 4.467 3.639 4.537 4.685 79.9 33.6 0.099 "5 of 56" 0.078; do echo "== $s"; grep -l -- "$s" *.ipynb; done; python3 - <<'EOF'
import json,glob
for fn in glob.glob('*.ipynb'):
    nb=json.load(open(fn))
    ec=[c.get('execution_count') for c in nb['cells'] if c['cell_type']=='code']
    print(fn, ec, nb['metadata'].get('kernelspec',{}).get('name'))
EOF
```

```
== 4.467
reproduce_scherrer_2023.ipynb
== 3.639
reproduce_scherrer_2023.ipynb
== 4.537
reproduce_scherrer_2023.ipynb
== 4.685
motion_scherrer_2023.ipynb
reproduce_scherrer_2023.ipynb
== 79.9
decoding_octant.ipynb
decoding_quadrant_direction.ipynb
decoding_reduced.ipynb
reproduce_scherrer_2023.ipynb
== 33.6
decoding_null_n2_octant.ipynb
decoding_null_n2_quadrant_direction.ipynb
decoding_octant.ipynb
decoding_quadrant_direction.ipynb
motion_scherrer_2023.ipynb
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for fn,keys in [('reproduce_scherrer_2023.ipynb',['4.467','3.639','4.537','4.685','79.9']),('decoding_quadrant_direction.ipynb',['33.6','5.0 hours']),('decoding_reduced.ipynb',['0.099','5 of 56','0.078','0.53'])]:
    nb=json.load(open(fn))
    for i,c in enumerate(nb['cells']):
        for o in c.get('outputs',[]):
            txt=''.join(o.get('text',''))+''.join(o.get('data',{}).get('text/plain',''))
            for k in keys:
                if k in txt: print(fn,i,'OUTPUT has',k)
        if c['cell_type']=='markdown':
            for k in keys:
                if k in ''.join(c['source']): print(fn,i,'markdown has',k)
EOF
```

```
reproduce_scherrer_2023.ipynb 5 OUTPUT has 79.9
reproduce_scherrer_2023.ipynb 33 markdown has 4.467
reproduce_scherrer_2023.ipynb 33 markdown has 3.639
reproduce_scherrer_2023.ipynb 33 markdown has 4.537
reproduce_scherrer_2023.ipynb 33 markdown has 4.685
reproduce_scherrer_2023.ipynb 33 markdown has 79.9
decoding_quadrant_direction.ipynb 10 markdown has 33.6
decoding_quadrant_direction.ipynb 13 markdown has 5.0 hours
decoding_reduced.ipynb 6 markdown has 0.099
decoding_reduced.ipynb 6 markdown has 0.53
decoding_reduced.ipynb 12 markdown has 5 of 56
decoding_reduced.ipynb 12 markdown has 0.078
```

**Agent**

**Verifier report, round 2: 000691-scherrer-2023-02**

The claims file has 23 claims, and the attempt record gives an outcome for all 23. I found no new place where the claims file misreads the paper.

## 1. The stated outcomes

I agree with all 23 outcomes in the attempt record. That includes the two I disputed in round 1.

- **fig2-quadrant-direction-decoding and ed9b-octant-decoding, blocked (not_runnable):** I now agree and withdraw my round-1 "reproduced". Both criteria judge p under (n1) and (n2). The (n2) null takes 24.6 h (quadrant nb cell 9) and 25.0 h (octant nb cell 8) against a 30-minute limit. Nine (n2) null decoders cannot show p < 0.001. The evidence still points strongly to (n2) agreeing with (n1): 0.089–0.145 against 0.437, and 0.109–0.149 against 0.326.
- **fig2k, fig2l, ed9c, blocked (not_runnable):** I agree. The measured costs (3.0 h, 2.7–2.9 h and 6.9–7.4 h on four cores) are all far over the limit.
- **ed7-motion-small, not_reproduced:** I agree, and it is no longer tentative (see section 3).
- **fig1f-kiloscope-psf, partially_reproduced:** I agree with the outcome. The printed outputs give no reading with both values within tolerance under any of the three sets of fits (cells 29–31), and the edge is wider than the centre. The record's reasons for it are wrong, though (section 2).
- **All the others:** I agree, for the reasons I gave in round 1.

## 2. Sentences the printed numbers do not support

Every number below is quoted from the conclusion or record and compared with the notebook's own printed output. These numbers appear only in the prose, never in an output. They look like they were carried over from a different run.

**fig1f-kiloscope-psf** (main nb cell 33; attempt record notes, and the response to round 1)

| Prose says | Notebook prints |
|---|---|
| Centre under (a) is "4.467 um, 0.067 um above the bound" | 4.422, 0.022 above (cell 29) |
| "4.422 um in the run reviewed in round 1 and is 4.467 um in this run" | 4.422 in this run as well |
| Mean major axis (c) centre "4.537 um" | 4.416 |
| Jacobian scaling: "15 of 118 beads' major FWHM move" | 14 of 118 (cell 30) |
| Jacobian (a) centre "3.639 um (within)" | 3.578, which is outside |
| Lower-cost fits: "4.467 and 5.892 um under (a), both outside" | 4.084 (within) and 5.892 (cell 31) |
| Lower-cost fits under (c): "4.685 and 7.944" | 4.222 (within) and 7.952 |
| The 27.77 µm bead's costs: "60.1 against 79.9" | 60.092 and 60.092 |
| "the centre lies within 0.07 um of its tolerance" | 0.022 |

The outcome survives, but the reason given for "partial" is false. With the lower-cost fits, it is the centre that is within tolerance and the edge that is not.

**fig1e-featherscope-psf** (cell 32 and record), trivial: "(c) … 6.883" is 6.884 in the output, and the minor-axis edge "5.203" is 5.202.

**Run times** (quadrant nb cells 10, 13, 16; octant nb cells 9, 12; record notes for the five decoding claims)

| Prose says | Notebook prints |
|---|---|
| "about 33.6 hours" | 24.6 h (quadrant nb cell 9) |
| "33.9 hours" | 25.0 h (octant nb cell 8) |
| "about 5.0 hours on four cores" | 3.0 h (cell 12) |
| "4.5 to 4.8 hours" | 2.7–2.9 h (cell 15) |
| "11.9 to 12.8 hours" | 6.9–7.4 h (octant nb cell 11) |

The same stale figures recur elsewhere:
- the "about 34 hours" in cell 0 of both null-(n2) notebooks;
- the "4 to 11 hours" in cell 0 of the reduced notebook;
- the README's notebook run times (7, 20, 25, 22 and 21 min), where the notebooks print 4.6, 12.3/12.4, 15.4, 15.2 and 12.4 min.

**Reduced runs** (decoding_reduced.ipynb; record notes)

- **fig2k, cell 6:** the prose says the median rises "from 0.099"; the output gives 0.101. It says p is "1.5e-6 to 6.7e-6 from 32 on"; the output gives 1.54e-6 to 7.96e-6. It says "2 to 8 (p 0.53 to 0.87)"; the output gives 0.356, 0.749 and 0.0935. It says "16 (p 0.017)"; the output gives 0.00213.
- **fig2l, cell 9:** the prose says "0.094 to 0.281 (0.187)" and "31 with (k + 1)/(n + 1)"; the output gives 0.097 to 0.282 (span 0.184), and 32 under both definitions of p.
- **ed9c, cell 12:** the prose says "0.078 to 0.203 (0.125), and 5 of 56 points are significant … so (i) holds". The output gives 0.090 to 0.197 (span 0.107) and **0 of 56 significant under both definitions, so (i) is False** (cell 11). The record's ed9c note repeats "5 of 56". The run decides no outcome, but the prose states the opposite of the result.

**Other sentences**

- **Main nb cell 23:** "ed6a … metadata_insufficient …; the others as data_missing". "The others" includes fig2d, which the record blocks as methods_underspecified.
- **Both null-(n2) notebooks, cell 0:** they run 8 decoders, "as many as fit within the time limit". Eight took 706 s and each notebook ran 15.2 min, so about twice as many would have fitted.
- **README, and main nb cells 0 and 17:**
  - They call the movie "the raw imaging video" as a fact, where the record says only that it is "consistent with" the raw video.
  - Cell 17 and the motion summary call the shifts "frame-to-frame". They are shifts against a template.

**My round-1 reasons in the record:** they are stated faithfully in my own words. The one exception is ed8, where "the midline split leaves 85 footprints" drops "of the footprints' extent". That distinction matters now that the image-midline split is added. The count of 22 of 23 claims, with none given for ed3-adc, is correct.

## 3. My round-1 points

**Resolved**

1. **Raw movie (point 1):** there are no comments and no motion-correction module. The histogram roughness is 0.740–0.745 in every block. A sub-pixel shift of 0.13 px lowers it to 0.052. The zeros are scattered single pixels. A known jitter is recovered (r = 0.996, RMS 0.033 → 0.136). The re-implementation remains a stated deviation.
2. **Null decoders (point 2):** the real single fits are now compared with the (n1) null on equal terms, and nine (n2) decoders are shown. The full (n2) null is correctly not_runnable.
3. **Analyses not run (point 3):** reduced runs are now given. I accept not_runnable as the reason.
4. **PSF fits (point 4):** the lower-cost fits are shown, with the per-bead table.
5. **ed8 (point 5):** the image-midline split is shown (86 footprints in the lower left; 8 of 8 and 7 of 8). The five off-event times are stated.
6. **Kiloscope image order (point 10):** this matters less than I said. The Featherscope stack, whose order is confirmed, also has only 71% of beads within 5 slices (cell 28), so the 72% figure says nothing about order.
7. **Fig2d, notebook header table (point 11):** fixed in the header, the summary and the README.
8. **Old verdicts in cells 28 and 34 (point 12):** no longer applicable.

Points 6–9 needed no change; point 9 is now in the notes.

**Remaining, bearing on a conclusion**

- **fig1f:** the conclusion and record must be rewritten from cells 29–31. The outcome holds, but the stated margins and the lower-cost result are wrong, and the lower-cost fits actually split the other way (centre within, edge outside).
- **ed9c:** the reduced-run statement must be corrected to 0 of 56 significant, with (i) failing. fig2k and fig2l need their reduced-run figures corrected too.
- **Costs:** every cost and run-time figure in the conclusions, the record, the README and the added notebooks' headers should be taken from the printed outputs. None of these changes an outcome.
- **Main nb cell 23:** fig2d is still described as data_missing, which contradicts the record.

## End of run

16 turns, 2 minutes, result: success.
