# 000691 · recorder · run 39587141529

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000691 --write; git diff; ls claims/000691 transcripts/000691; cat attempts/000691-scherrer-2023-02.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000691' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (259.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/b3sbsd02n.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 2e0b7ba5..c24545e2 100644
--- a/README.md
+++ b/README.md
@@ -89,7 +89,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
 | [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s41586-022-05611-2) | 7 | 3 | 2 | 12 | [`000559-markowitz-2023`](entries/000559-markowitz-2023) |
 | [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
-| [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | – | – | – | – | [`000691-scherrer-2023`](entries/000691-scherrer-2023) (deprecated) |
+| [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 2 | 0 | 1 | 15 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
 | [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
 | [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
 | [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; ls -la transcripts/000691 transcripts/000691/attempt-01 | head -50; ls attempts | grep 000691; cat attempts/000691-scherrer-2023-02.yaml
```

```
<persisted-output>
Output too large (50.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/bvh1hxfpm.txt

Preview (first 2KB):
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
transcripts/000691:
total 776
drwxr-xr-x  3 runner runner   4096 Oct 21 10:47 .
drwxr-xr-x 83 runner runner   4096 Oct 21 10:47 ..
-rw-r--r--  1 runner runner    608 Oct 21 10:47 answer-report.md
-rw-r--r--  1 runner runner   4509 Oct 21 10:47 answer.md
drwxr-xr-x  2 runner runner   4096 Oct 21 10:47 attempt-01
-rw-r--r--  1 runner runner   2457 Oct 21 10:47 author-answers-report.md
-rw-r--r--  1 runner runner  12276 Oct 21 10:47 author-answers.md
-rw-r--r--  1 runner runner   4959 Oct 21 10:47 author-report.md
-rw-r--r--  1 runner runner   4522 Oct 21 10:47 author-revise-1-report.md
-rw-r--r--  1 runner runner 174674 Oct 21 10:47 author-revise-1.md
-rw-r--r--  1 runner runner   3872 Oct 21 10:47 author-revise-2-report.md
-rw-r--r--  1 runner runner  62689 Oct 21 10:47 author-revise-2.md
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
git log --oneline | grep 000691 | head -20; ls attempts | grep 000691; wc -c attempts/000691-scherrer-2023-02.yaml claims/000691/*
```

```
78dd50fd Agent run on 000691: author-revise-2 (success)
58f9bbec Agent run on 000691: verifier-2 (success)
a3a71c45 Agent run on 000691: author-revise-1 (success)
ac49eee1 Agent run on 000691: verifier-1 (success)
5959de44 Agent run on 000691: author-answers (success)
8ef0758f Agent run on 000691: answer (success)
52ffc7dc Agent run on 000691: author (success)
4a714689 Merge pull request #132 from catalystneuro/attempt/000691
53d6cebe Merge pull request #125 from catalystneuro/claims/000691
9c23dfdb Claims for DANDI:000691, checked
3f400b8e Agent run on 000691: claims-check (success)
ed33545f Agent run on 000691: claims (success)
f9eab779 Merge pull request #75 from catalystneuro/attempt/000691
dac844d6 Agent run on 000691: recorder (success)
c67e5c2b Agent run on 000691: author-revise-2 (success)
7af7e8c7 Agent run on 000691: verifier-2 (success)
8de26e00 Agent run on 000691: author-revise-1 (success)
27777c40 Agent run on 000691: verifier-1 (success)
37e8927b Agent run on 000691: author (success)
000691-scherrer-2023-01.yaml
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^###' docs/pilot-notes.md | tail -12; grep -n '001754' docs/pilot-notes.md
```

```
4228:### 001878, Sun et al. 2021
4320:### 001712, Davatolhagh et al. 2025
4420:### 001888, Hristova et al. 2025
4510:### 000005, Yu et al. 2016
4752:### 001754, Knierim et al. 2000, third attempt
4857:### crcns-ret-1, Lefebvre et al. 2008
4962:### 000005, Yu et al. 2016, second attempt
5082:### 000061, Girardeau et al. 2017, second attempt
5185:### 000582, Sargolini et al. 2006, second attempt
5300:### 000009, Guo et al. 2017
5400:### 000008, Scala et al. 2021
5511:### 000010, Li et al. 2015
747:001754, 000130 and 001616. The first pipeline run mixed results between
774:### 001754, Knierim, McNaughton and Poe 2000
863:### 001754 again, on the fixed draft (2026-10-15)
895:The earlier attempt's transcripts are now in `transcripts/001754/attempt-01/`,
4637:000582, 000691, 001754) were quoted from the abstract, figure titles and
4656:outcomes: four of 001754 taken from the dandiset's description, and one of
4675:001754 (both of its attempts). With no Methods to read, their authors chose
4680:of not reproduced among these attempts rested on such a measure: 001754's
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 4962
}
```

```
File content (370.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
wc -l docs/pilot-notes.md; awk 'NR>=5185 && NR<=5240' docs/pilot-notes.md | cut -c1-400
```

```
5626 docs/pilot-notes.md
### 000582, Sargolini et al. 2006, second attempt

Five claims reproduced, one partially, three not reproduced and twelve blocked
on the dandiset. The attempt replaces the deprecated 000582-sargolini-2006-01,
whose claims were written from the abstract alone; the claims file was written
again from the full text and its Supporting Online Material (SOM), so it has 21
claims where the earlier one had 3, and the three kept ids (`layer2-grid`,
`deep-hd-conjunctive`, `speed`) now carry the paper's numbers and criteria. It
pins the same version, 0.251111.2151, the only published version, whose draft
holds the same 118 assets. The author put five questions to a reader; the
answers added readings to several criteria, among them both centres and both
radii of an autocorrelogram peak (56 grid readings where there had been 32),
and changed one outcome, `grid-phase-orientation`, from blocked to partially
reproduced. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with 18 of 21. It found
that partially reproduced is not an outcome the criterion of
grid-phase-orientation names, and the claims file blocks a claim that holds
under some readings and not others, so the claim moved back to blocked as
`methods_underspecified`. It would call `speed-slope-steeper` partially
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/000691/author-report.md; for f in author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat transcripts/000691/$f-report.md; done
```

```
<persisted-output>
Output too large (31.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/b6yy0lx50.txt

Preview (first 2KB):
I've built the new attempt, written `attempts/000691-scherrer-2023-02.yaml` and run the handover; nothing is committed. The dandiset has only one published version, 0.260827.1358, and the draft holds the same files, so the version did not change. Every difference from `-01` comes from the rewritten claims file, not from the data.

The entry now has four notebooks, all of which pass a clean run: the main one (7 min), two decoding notebooks (19 min each) and a motion notebook (22 min), each kept under the 30-minute limit. After that run I changed only markdown text, copied it into the executed copies, and checked that every code cell is identical to what ran.

## 1. Outcome per claim (earlier outcome in brackets)

| Claim | This attempt | `-01` |
|---|---|---|
| abstract-thousands-of-neurons | reproduced (2948 footprints) | reproduced |
| abstract-kiloscope-fov | reproduced (4.800 × 3.612 mm at the code's 5.94 µm per pixel) | blocked, metadata insufficient |
| fig1e-featherscope-psf | reproduced (3.92 / 6.43 µm) | new |
| fig1f-kiloscope-psf | partially reproduced (4.42 / 5.44 µm; the centre misses its bound by 0.02 µm) | new |
| ed2b-featherscope-flat-illumination | reproduced | partially reproduced |
| ed2c-kiloscope-flat-illumination | reproduced | partially reproduced |
| ed7-motion-small | not reproduced (0.037 px RMS against 0.13) | new |
| fig2-quadrant-direction-decoding | blocked, not runnable | dropped in `-01` |
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cat /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/b6yy0lx50.txt; sed -n 1,12p README.md | cut -c1-300; grep -n '^| Dandiset\|^| ---' README.md | head
```

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/bzt9azb2a.txt

Preview (first 2KB):
I've built the new attempt, written `attempts/000691-scherrer-2023-02.yaml` and run the handover; nothing is committed. The dandiset has only one published version, 0.260827.1358, and the draft holds the same files, so the version did not change. Every difference from `-01` comes from the rewritten claims file, not from the data.

The entry now has four notebooks, all of which pass a clean run: the main one (7 min), two decoding notebooks (19 min each) and a motion notebook (22 min), each kept under the 30-minute limit. After that run I changed only markdown text, copied it into the executed copies, and checked that every code cell is identical to what ran.

## 1. Outcome per claim (earlier outcome in brackets)

| Claim | This attempt | `-01` |
|---|---|---|
| abstract-thousands-of-neurons | reproduced (2948 footprints) | reproduced |
| abstract-kiloscope-fov | reproduced (4.800 × 3.612 mm at the code's 5.94 µm per pixel) | blocked, metadata insufficient |
| fig1e-featherscope-psf | reproduced (3.92 / 6.43 µm) | new |
| fig1f-kiloscope-psf | partially reproduced (4.42 / 5.44 µm; the centre misses its bound by 0.02 µm) | new |
| ed2b-featherscope-flat-illumination | reproduced | partially reproduced |
| ed2c-kiloscope-flat-illumination | reproduced | partially reproduced |
| ed7-motion-small | not reproduced (0.037 px RMS against 0.13) | new |
| fig2-quadrant-direction-decoding | blocked, not runnable | dropped in `-01` |
[... 9 more lines not kept]
```

**Agent**

I'll read the saved output in pieces.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/bzt9azb2a.txt"
}
```

```
1	I've built the new attempt, written `attempts/000691-scherrer-2023-02.yaml` and run the handover; nothing is committed. The dandiset has only one published version, 0.260827.1358, and the draft holds the same files, so the version did not change. Every difference from `-01` comes from the rewritten claims file, not from the data.
2	
3	The entry now has four notebooks, all of which pass a clean run: the main one (7 min), two decoding notebooks (19 min each) and a motion notebook (22 min), each kept under the 30-minute limit. After that run I changed only markdown text, copied it into the executed copies, and checked that every code cell is identical to what ran.
4	
5	## 1. Outcome per claim (earlier outcome in brackets)
6	
7	| Claim | This attempt | `-01` |
8	|---|---|---|
9	| abstract-thousands-of-neurons | reproduced (2948 footprints) | reproduced |
10	| abstract-kiloscope-fov | reproduced (4.800 × 3.612 mm at the code's 5.94 µm per pixel) | blocked, metadata insufficient |
11	| fig1e-featherscope-psf | reproduced (3.92 / 6.43 µm) | new |
12	| fig1f-kiloscope-psf | partially reproduced (4.42 / 5.44 µm; the centre misses its bound by 0.02 µm) | new |
13	| ed2b-featherscope-flat-illumination | reproduced | partially reproduced |
14	| ed2c-kiloscope-flat-illumination | reproduced | partially reproduced |
15	| ed7-motion-small | not reproduced (0.037 px RMS against 0.13) | new |
16	| fig2-quadrant-direction-decoding | blocked, not runnable | dropped in `-01` |
17	| ed9b-octant-decoding | blocked, not runnable | reproduced |
18	| fig2k-decoder-size, fig2l-local-decoding-map | blocked, not runnable | new |
19	| ed9c-local-decoding-map | blocked, not runnable | reproduced |
20	| ed8-coactive-distributed | blocked, methods underspecified | reproduced |
[... 275 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p tools/readme_row.py
```

```
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row
    python tools/readme_row.py DATASET --write    # add it to README.md, or replace the dataset's row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
c=yaml.safe_load(open('claims/000691/10.1038-s41592-023-01806-1.yaml'))
print({k:v for k,v in c.items() if k!='claims'})
k={x['id']:(x.get('kind'),x.get('data','dataset')) for x in c['claims']}
r=yaml.safe_load(open('attempts/000691-scherrer-2023-02.yaml'))
print({k2:v for k2,v in r.items() if k2 not in('outcomes','findings','verifications')})
for o in r['outcomes']: print(o['claim'],o['outcome'],o.get('blocked_by'),k.get(o['claim']))
print(r.keys())
E
```

```
{'schema_version': 2, 'dataset': {'archive': 'dandi', 'id': '000691'}, 'paper': 'doi:10.1038/s41592-023-01806-1', 'checks': [{'date': '2026-10-20', 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['fig1e-featherscope-psf, fig1f-kiloscope-psf. Reading (c), "the mean of the two axes\' means", is not what the code computes; its error bar plot shows the mean of each axis separately. Replaced by (c) the mean major-axis FWHM and (d) the mean minor-axis FWHM.', 'fig2-quadrant-direction-decoding. The Methods say a thousand decoders on different shuffles but not how many fits make one null decoder, and the code holds no null for this panel. The file fixed one fit as if the Methods said so. Both readings (one fit, or 200 fits as for the real matrix) are now named, with methods_underspecified when they disagree.', 'ed9b-octant-decoding. The same open detail of the null, named the same way.', 'fig2k-decoder-size. The statement said decoders of every size differ from shuffled ones, which is reading (a) of the criterion; the paper says only that accuracy depended on size, P at or below 2.7e-4 for all sizes. The statement now says that, and the criterion keeps both readings.', "fig2l-local-decoding-map. Footprint positions were called centroids; the Methods do not say, and the code (subregion_map_quaddir.m) uses the first pixel where the spatial weight equals 1. The code's choice is now used and the centroid is a variant. The number of fits per null decoder (one, or 10 as at the points) is added as an open detail, and the outcome when the readings disagree (methods_underspecified) is now stated.", "ed9c-local-decoding-map. The span threshold of 0.05 was the earlier author's choice, with no source in the paper or the code. Removed; the claim is judged on (i) and the span is reported. The null's number of fits is added as an open detail, as for fig2l.", 'ed8-coactive-distributed. Reading (ii), a percentile test against 1,000 random sets of footprints, and the 
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml,json
r=yaml.safe_load(open('attempts/000691-scherrer-2023-02.yaml'))
for f in r['findings']: print(json.dumps(f,indent=1,default=str,ensure_ascii=False)); print()
E
grep -n '"000691"' -A25 targets/dandisets.json | head -40
```

```
{
 "kind": "data_missing",
 "statement": "Still present (finding of -01). The dandiset holds one of the paper's four mice and none of the songbird recordings. The bead and dye images of the optical tests are in the paper's code repository, but the USAF target images and ADC recordings are not public. The Academic Torrents deposit lists files of the same mouse session only."
}

{
 "kind": "metadata_error",
 "statement": "Still present (finding of -01). The device description reads \"Head-mounted microscope (Kiloscope) optimized for weight (1.0 mm FOV; 1.0 g)\", and the dandiset description says the data come from the microscope optimized for weight; the data are from the large-FOV Kiloscope (4 mm window, 2948 footprints, 808 x 608 pixel frames)."
}

{
 "kind": "metadata_error",
 "statement": "Still present (finding of -01). The imaging is stored as a TwoPhotonSeries and the dandiset lists two-photon microscopy among its techniques, but the microscope is a one-photon head-mounted epifluorescence microscope."
}

{
 "kind": "metadata_error",
 "statement": "Still present (finding of -01). The behaviour video is described as about 30 fps and its AVI header says 30 frames/s, but its 15521 timestamps run at a median 12.5 frames/s over 1234 s."
}

[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
awk 'NR>=5240' docs/pilot-notes.md
```

```
attempt were checked again: four are still present, and the missing methods
are partly fixed, as the SOM was supplied for this attempt, though the
dandiset states no analysis parameter and no analysis code is public. The
dandiset is described as a sample of the paper's data without saying how it
was selected; it holds 620 cell-sessions from 15 rats against the paper's 627
cells from 17, with 71 layer II cell-sessions against 108 while layers III, V
and VI hold slightly more than table S1A (227, 118 and 198 against 223, 110
and 186). No identifier links a cell across files: of 584 cell-sessions with a
depth there are 425 distinct (rat, depth, hemisphere, name), 99 of which
appear in 2 to 7 files. The positions are rescaled without saying so: in all
118 files they span exactly 100, 150 or 200 cm on the larger axis, and the 19
circular files spanning 200 cm are most likely the paper's 180 cm circle,
about 11% too large. No file gives the recording sites' distance from the
postrhinal border (`depth` is the depth the electrodes were lowered to, and
the electrodes table has one row per file, location "MEC", with no
coordinates), and no file names its enclosure, condition or the position of
the cue card. Every file says the enclosure was 1 x 1 m, but the positions
span 150 cm in 2 files and 200 cm in 20, and every file says position is given
for two LEDs, but 47 of 118 files have one, so head direction cannot be
computed for 167 of 620 cell-sessions. The 23 twenty-minute files hold two
[... 367 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml,json
r=yaml.safe_load(open('attempts/000691-scherrer-2023-02.yaml'))
for o in r['outcomes']:
  print('##',o['claim'],o['outcome'],o.get('blocked_by'))
  for k,v in o.items():
    if k not in('claim','outcome','blocked_by'): print(' ',k,':',str(v)[:1500])
print(json.dumps(r['verifications'],default=str,indent=0)[:6000])
E
python -c "
import yaml;r=yaml.safe_load(open('attempts/000691-scherrer-2023-01.yaml'));print(r.get('deprecated'), r.get('superseded_by'))"
```

```
## abstract-thousands-of-neurons reproduced None
  notebook : reproduce_scherrer_2023.ipynb
  output : claim:abstract-thousands-of-neurons
  measured : 2948
  notes : The session holds 2948 EXTRACT footprints (masks, ids and trace columns agree), within 2948 +/- 295, recorded together in one movie of 36596 frames while the mouse ran 47.7 loop lengths and visited all four quadrants. Same outcome as -01; the criterion no longer asks for duplicate merging or a nonzero trace, and the count is the same.
  deviations : ['The count is of the EXTRACT output before curation, as the claim states; the curated 2,382 are not marked in the dandiset.']
## ed6a-curated-footprints blocked metadata_insufficient
  notes : The plane segmentation has only image_mask and ROICentroids, with no column marking the curated footprints, so the criterion's count of marked footprints cannot be made. The selection is in the paper's Academic Torrents deposit (supporting_data/2021-07-26_isgood.mat, infohash aa2a3d2f5ff0b3974871db47db57bc3dabf3c192); a 4 minute download attempt outside the notebook found no peers, as in -01. Same outcome as -01.
## ed6bcd-other-mice blocked data_missing
  notes : The dandiset holds one subject (4mm-mouse-1) and one session. The Academic Torrents file list holds only this mouse's session, and no other dandiset of the paper was found. Same as -01.
## ed5-songbirds blocked data_missing
  notes : No bird data in the dandiset, the Academic Torrents file list or the code repository. Same as -01.
## birds-singing-rate blocked data_missing
  notes : No song or bird data in the dandiset or the paper's deposits. New claim.
## fig2d-lman-sparse-bursting blocked methods_underspecified
  notes : The criterion says the paper gives no measure of sparse bursting and no count of the footprints that show it, so no method the paper fixes decides the claim. Its data are also missing (data_missing), with no bird imaging in the dandiset or the paper's deposits. New claim.
## abstract-kil
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/000691-scherrer-2023-02.yaml'))
for v in r['verifications']: print(v['reviewed']); print()
c=yaml.safe_load(open('claims/000691/10.1038-s41592-023-01806-1.yaml'))
for x in c['claims'][:3]: print(x.get('statement'))
E
```

```
Round 1. The executed notebooks of the run of 2026-10-20 with the conclusion cells and the summaries removed, the helper module and the claims file, with the paper. The verifier queried the archive and tested helper functions on synthetic inputs. Its report gave its own outcome for 22 of the 23 claims; it gave none for ed3-adc, which is not listed here. It agrees with 20 of the 22 and gives reproduced for the two decoding claims the record blocks.

Round 2. The full executed notebooks of a run made by the workflow for the verifier, with the conclusions, summaries, README and attempt record, the helper module and the claims file, with the paper. The verifier agrees with all 23 outcomes, including the two decoding claims it disputed in round 1, and found no new place where the claims file misreads the paper. It found numbers in the prose that its run did not print, which it took to be carried over from another run; the run made for this revision (2026-10-21) shows that the PSF fits, the reduced runs and the timings differ between runs on different machines. Every conclusion is now written from the run made for this revision, and the record gives the values of the run of round 2 where they differ.

The Kiloscope records thousands of neurons at once in a freely behaving mouse; in the mouse with the best expression EXTRACT gave 2,948 footprints.
In the mouse with the most footprints, manual curation leaves 2,382 putative neurons.
The Kiloscope was used in four mice, and more than a thousand neurons were recorded at once in more than one of them; EXTRACT gave 2,948, 401, 1,029 and 112 footprints.
```

**Agent calls Bash**

```bash
grep -n -i 'featherscope\b\|songbird\|finch\|lightweight' claims/000691/*.yaml | cut -c1-300 | head -20
```

```
10:# text, the sentence on the Featherscope's resolution (page 547) is split by figure labels, its
11:# second half placed before its first; the quote of fig1e-featherscope-psf is that second half, and
12:# its first half reads "The Featherscope has a resolution of approximately 4 μm at the".
27:# - Added from the full text: fig1e-featherscope-psf, fig1f-kiloscope-psf, ed1cf-field-curvature,
42:# male zebra finches (50 to 70 days post hatch), GCaMP6f in LMAN, imaged with the Featherscope
44:# beads (155 for the Featherscope, 118 for the Kiloscope), a thin layer of fluorescent dye, and
152:- id: ed5-songbirds
153:  statement: The Featherscope recorded hundreds of neurons in juvenile songbirds; curation gave
172:  statement: Birds carrying the Featherscope sang 3,861 to 23,545 syllables per day, within the
220:    (Featherscope, 1.0 mm field of view).
230:  - quantity: Featherscope weight
234:- id: fig1e-featherscope-psf
235:  statement: The Featherscope's resolution (FWHM of the bead PSF) is about 4 um at the centre of
279:  criterion: As for fig1e-featherscope-psf, with f2+sf4/wf_analysis_secondorder.m (5.35 um per
296:    Featherscope and 4.38 um with the Kiloscope, and 2.2 um with Kiloscope optics on a sensor with
303:- id: ed2b-featherscope-flat-illumination
304:  statement: For the Featherscope, the axicon correction optics give a flat signal profile
331:  criterion: As for ed2b-featherscope-flat-illumination, with sf3/widefield/analysis.m (5.94 um
529:  - fig1e-featherscope-psf, fig1f-kiloscope-psf. Reading (c), "the mean of the two axes' means", is
```

**Agent calls Bash**

```bash
sed -n 1,60p claims/000691/*.yaml; sed -n 205,235p claims/000691/*.yaml
```

```
# Claims for Scherrer, Lynch, Zhang & Fee (2023) on dandiset 000691.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record (Nature Methods 20, 546-549), from a PDF supplied by a person,
# as extracted text in paper/10.1038-s41592-023-01806-1.txt. It holds the main text, the figure
# legends, the Methods, the Extended Data legends (Extended Data Figs. 1 to 10) and the reporting
# summary. The supplementary information is two videos (Supplementary Videos 1 and 2), which no
# result rests on. The PDF was not opened; the numbers needed were in the text. In the extracted
# text, the sentence on the Featherscope's resolution (page 547) is split by figure labels, its
# second half placed before its first; the quote of fig1e-featherscope-psf is that second half, and
# its first half reads "The Featherscope has a resolution of approximately 4 μm at the".
#
# Rewritten 2026-10-20 from the full text. The earlier file was written from the abstract and the
# public figure legends, and its criteria were written after its author had seen the data check
# and a prototype decoder. This file is written from the paper and its code alone, by a reader
# who has not seen the dandiset's data. What changed, and why:
# - ed9c-local-decoding-map: the null is now the paper's (Methods, Data analysis, paragraph 5),
#   a thousand decoders trained on shuffled data from 32 randomly chosen footprints, where each
#   footprint's trace is circularly shifted by its own random offset. The earlier null shifted the
[... 71 more lines not kept]
```

**Agent**

Now I have the sources. Writing the subsection.

**Agent calls Bash**

```bash
cat > $TMPDIR/sec.txt <<'EOF'
Two claims reproduced, none partially, one not reproduced and fifteen blocked on the dandiset; of five more claims on the bead and dye images in the paper's code repository, three are reproduced, one partially and one blocked. The attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were written from the abstract and public figure legends only; the claims file was written again from the full text and the paper's code, so it has 23 claims, ten of them new or restored, and several criteria that rested on the earlier author's thresholds now use the paper's numbers. It pins the same version, 0.260827.1358, the only published version, whose draft holds the same files, so every difference from `-01` comes from the claims file. The author put no questions to a reader, and the answer run found no questions file, so nothing changed. Round 1 gave its own outcome for 22 of the 23 claims from the notebooks with their conclusion cells and summaries removed (none for `ed3-adc`) and agreed with 20 of them; it gave reproduced for `fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of one fit per shuffled decoder (n1) alone, and called `ed7-motion-small` tentative because nothing checked that the movie is raw. The author kept both decoding claims blocked as `not_runnable`, and round 2 agreed with all 23 outcomes; nothing was proposed, so there was no third round. The paper, "An optical design enabling lightweight and large field-of-view head-mounted microscopes", describes two head-mounted microscopes, the Kiloscope (about 4 mm field of view, 1.4 g) and the Featherscope (1.0 mm, 1.0 g), used in four mice and three juvenile zebra finches, and reports thousands of neurons recorded at once in a freely moving mouse, decoded from to give its position and direction. The footprint count, the field of view, the bead PSFs, field curvature, the flat illumination of both microscopes and the motion of the movie were tested, and the decoding claims were run under the (n1) null. `ed7-motion-small` is not reproduced (0.037 px RMS against 0.13), and `fig1f-kiloscope-psf` is partially reproduced because no reading puts both values within tolerance. The decoding claims hold under (n1) (median accuracy 0.437 and 0.326 against the largest of 1000 shuffled decoders at 0.227 and 0.229), but the criterion also needs (n2), 200 fits per shuffled decoder, which is 200,000 fits, measured at 33.3 hours in this run (24.6 hours in the run of round 2) against 30 minutes per notebook, so fig2 and ed9b are blocked as `not_runnable`, and `fig2k-decoder-size`, `fig2l-local-decoding-map` and `ed9c-local-decoding-map` also, as they depend on them and need hours each. The other mice, the songbirds, the weights, the USAF target images and the ADC recordings are not deposited, `ed6a-curated-footprints` is blocked as `metadata_insufficient`, and `fig2d-lman-sparse-bursting`, `ed8-coactive-distributed` and `ed10-localized-activity` as `methods_underspecified`, ed8 because all four quarters are covered in 8 of 8 events under one reading of the event times and 7 of 8 under the other. Compared with `-01`, abstract-kiloscope-fov moved from blocked to reproduced, the two flat-illumination claims from partially reproduced to reproduced, and ed8, ed9b, ed9c and ed10 from reproduced to blocked. Some outcomes rest on weak ground: in abstract-kiloscope-fov both pixel sizes come from the paper's code, the shorter reading only just within tolerance (4.323 against a lower bound of 4.32) and the test close to circular at 5.94 um per pixel; and the Kiloscope PSF fits depend on the optimizer and differ between runs on different machines (4.467 um at the centre under reading (a) in this run, 4.422 um in the run of round 2).

The dataset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro is a contributor). The files are unchanged, so the nine findings of `-01` were checked again, and all are still present. The dandiset holds one of the paper's four mice and none of the songbird recordings, and the USAF target images and ADC recordings are not public. The mouse's position, which the paper's decoding and place analyses use, is not in the dandiset (its only processing module is ophys), and the opening of the behaviour video that the paper's code skips is not marked. The 2948 footprints are the EXTRACT output before curation; the paper analyses the 2,382 it kept, and nothing marks them or says the footprints are uncurated. The device description reads "Head-mounted microscope (Kiloscope) optimized for weight (1.0 mm FOV; 1.0 g)", and the dandiset description also names the microscope optimized for weight, where the data are from the large-FOV Kiloscope (4 mm window, 2948 footprints, 808 x 608 pixel frames). The imaging is stored as a TwoPhotonSeries and two-photon microscopy is listed among the techniques, though the microscope is a one-photon head-mounted epifluorescence microscope. Nothing says whether the movie is the raw video or the motion-corrected one the paper extracted footprints from; its values are consistent with the raw video, and its rigid shifts against a template have an RMS of 0.037 pixels, about a quarter of the 0.13 pixels the paper reports. Other findings: the behaviour video is described as about 30 fps and its AVI header says 30 frames/s, but its 15521 timestamps run at a median 12.5 frames/s over 1234 s; the imaging plane gives no pixel size, its indicator and location are "unknown" and its excitation wavelength is NaN, although general/virus says GCaMP7f; ROICentroids equal the mask's peak pixel for 84% of footprints and the rounded weighted centroid for only 43%; both local decoding map scripts use 64 footprints within 50 pixels where the paper describes the 32 closest within 270 um; the Extended Data Fig. 8 legend refers to a Figure 3 and a ridgeline plot in Fig. 2d, where the paper has two figures and the ridgeline plot is Fig. 2h; the paper's tracking code unwraps position with MATLAB's unwrap, which gains an error of up to pi cm at every lap of the 147.1 cm loop and changes about 1% of the running and direction labels; and the paper's bead scripts order the images by file date, which the repository does not keep, so the Kiloscope stack's slice order is not recorded.

The notebooks, four at first, ran in 7 min, 19 min, 19 min and 22 min in the first clean run and 497 s, 1122 s, 1124 s and 1237 s after the answer run. `entry.py check`, and so `entry.py all`, failed throughout on 11 errors, all in the deprecated record, which has no outcomes for the new claims and must stay as it is, and the notebooks were run with `entry.py run`. Round 1's points led to a check that the movie is raw (histogram roughness 0.740 to 0.745, which a 0.13 px sub-pixel shift lowers to 0.052, and a known 0.13 px jitter recovered with correlation 0.996), so ed7 is no longer tentative, PSF readings with the lower-cost fit for each bead, the lines of each illumination script that load the images, ed8 counts with the quarters split at the image midlines, the real decoders' single fits compared with the (n1) null, nine (n2) null decoders per decoding claim, and three new notebooks, two of (n2) null decoders and one of reduced runs of fig2k, fig2l and ed9c that decide nothing, none changing an outcome; `fig2d-lman-sparse-bursting` changed its block reason from `data_missing` to `methods_underspecified`. In both revisions the 2-hour command limit cut the run of seven notebooks, and the last, `decoding_reduced.ipynb`, was run on its own. Round 2 found numbers in the prose that its run did not print, among them the fig1f margins, the run times and 5 of 56 significant points in the reduced ed9c run where its run printed 0; the author's run for the second revision printed the prose's numbers, so the PSF fits, the reduced runs and the timings differ between runs on different machines even with every seed fixed (7 of 56 significant ed9c points in one run and 0 in the other), the cause was not found, and the record now gives both runs' values. Untracked files in the repository root that the author did not create were left alone. The author's points on the protocol: `entry.py check` fails on the deprecated `-01` record, which must stay unchanged, so `entry.py all` cannot pass; the section on repeat attempts assumes the claims file is kept and the dataset changed, where here the claims file was rewritten and the data were not; and the claims file sets decoding methods that need 10^5 fits, which a 30-minute limit per notebook cannot decide whatever the data.
EOF
grep -n 'decoded from to' $TMPDIR/sec.txt | head -2
```

```
1:Two claims reproduced, none partially, one not reproduced and fifteen blocked on the dandiset; of five more claims on the bead and dye images in the paper's code repository, three are reproduced, one partially and one blocked. The attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were written from the abstract and public figure legends only; the claims file was written again from the full text and the paper's code, so it has 23 claims, ten of them new or restored, and several criteria that rested on the earlier author's thresholds now use the paper's numbers. It pins the same version, 0.260827.1358, the only published version, whose draft holds the same files, so every difference from `-01` comes from the claims file. The author put no questions to a reader, and the answer run found no questions file, so nothing changed. Round 1 gave its own outcome for 22 of the 23 claims from the notebooks with their conclusion cells and summaries removed (none for `ed3-adc`) and agreed with 20 of them; it gave reproduced for `fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of one fit per shuffled decoder (n1) alone, and called `ed7-motion-small` tentative because nothing checked that the movie is raw. The author kept both decoding claims blocked as `not_runnable`, and round 2 agreed with all 23 outcomes; nothing was proposed, so there was no third round. The paper, "An optical design enabling lightweight and large field-of-view head-mounted microscopes", describes two head-mounted microscopes, the Kiloscope (about 4 mm field of view, 1.4 g) and the Featherscope (1.0 mm, 1.0 g), used in four mice and three juvenile zebra finches, and reports thousands of neurons recorded at once in a freely moving mouse, decoded from to give its position and direction. The footprint count, the field of view, the bead PSFs, field curvature, the flat illumination of both microscopes and the motion of the movie were tested, and the decoding claims were 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 'id: fig2-quadrant' claims/000691/*.yaml
```

```
369:- id: fig2-quadrant-direction-decoding
370-  statement: Linear SVM decoders trained on half of the data decode the mouse's combined quadrant
371-    and movement direction on the other half at an accuracy at least three times chance, above
372-    that of decoders trained on shuffled data.
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'E'
s=open('sec.txt').read()
reps=[
("so it has 23 claims, ten of them new or restored","so it has 23 claims, nine of them new or restored"),
("reports thousands of neurons recorded at once in a freely moving mouse, decoded from to give its position and direction.","reports thousands of neurons recorded at once in a freely moving mouse, from whose activity linear decoders read the mouse's combined quadrant and movement direction at least three times above chance."),
("which is 200,000 fits, measured at 33.3 hours in this run","which is 200,000 fits, measured for the quadrant claim at 33.3 hours in this run"),
("as they depend on them and need hours each.","as they depend on them and need 4.4 to 12.8 hours each on four cores."),
("the shorter reading only just within tolerance (4.323 against a lower bound of 4.32)","the reading at 5.35 um per pixel only just within tolerance (4.323 against a lower bound of 4.32)"),
("Round 1's points led to a check that the movie is raw (histogram roughness 0.740 to 0.745, which a 0.13 px sub-pixel shift lowers to 0.052, and a known 0.13 px jitter recovered with correlation 0.996)","Round 1's points led to a check of whether the movie is raw (histogram roughness 0.740 to 0.745, which sub-pixel shifts of 0.13 px RMS lower to 0.052, and a known jitter of 0.132 px RMS recovered with correlation 0.996)"),
("; the author's run for the second revision printed the prose's numbers, so the PSF fits, the reduced runs and the timings differ between runs on different machines even with every seed fixed (7 of 56 significant ed9c points in one run and 0 in the other), the cause was not found, and the record now gives both runs' values.","; the run made for the second revision printed the prose's fig1f numbers, and the PSF fits, the reduced runs and the timings turned out to differ between runs on different machines even with every seed fixed (in the reduced ed9c run, 7 of 56 points significant in one run and 0 in the other). The cause was not found, and the record gives both runs' values."),
]
for a,b in reps:
    assert s.count(a)==1,a; s=s.replace(a,b)
import textwrap,re
assert '—' not in s and 'rather' not in s
paras=[textwrap.fill(p,78,break_long_words=False,break_on_hyphens=False) for p in s.strip().split('\n\n')]
out="\n### 000691, Scherrer et al. 2023, second attempt\n\n"+"\n\n".join(paras)+"\n"
open('final.txt','w').write(out)
E
tail -c 200 docs/pilot-notes.md | od -c | tail -3
```

```
0000260   p   a   s   t       t   h   e       1   0   -   m   i   n   u
0000300   t   e       a   i   m   .  \n
0000310
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat $TMPDIR/final.txt >> docs/pilot-notes.md && git diff --stat && tail -n 120 docs/pilot-notes.md | sed -n '/### 000691/,$p'
```

```
README.md           |   2 +-
 docs/pilot-notes.md | 122 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 123 insertions(+), 1 deletion(-)
```

**Agent calls Bash**

```bash
sed -n '/^### 000691, Scherrer/,$p' docs/pilot-notes.md
```

```
<persisted-output>
Output too large (200.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/29c62b78-95a1-400f-bc66-3ed43031a759/tool-results/bn3wp4gl9.txt

Preview (first 2KB):
### 000691, Scherrer et al. 2023

Six claims reproduced and seven blocked on the dandiset, plus two claims on
data in other archives, both partially reproduced. Round 1 gave its own
outcome for each claim from the notebook with its conclusions removed and
agreed with all 15 as they then stood, but suspected that the SGD solver
explained why no point of the local decoding map was significant (0 of 151);
the 32-footprint decoders stop at objectives of 19.8 to 68.9 where the
optimum is 1.976 to 2.000, so the author fit them with liblinear, as
MATLAB's default for 100 or fewer predictors is BFGS run to convergence, and
`ed9c-local-decoding-map` moved from not reproduced to reproduced. Round 2
agreed with all 15 and nothing was proposed, so there was no third round.
The paper reports two head-mounted microscopes with axicon correction
optics, one optimized for weight (1.0 g, 1.0 mm FOV) and one for field of
view (1.4 g, about 4 mm), that image hundreds of neurons in juvenile
songbirds and thousands in a freely behaving mouse, whose position and
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^### 000691, Scherrer et al. 2023, second attempt/,$p' docs/pilot-notes.md; grep -c '^### 000691' docs/pilot-notes.md
```

```
### 000691, Scherrer et al. 2023, second attempt

Two claims reproduced, none partially, one not reproduced and fifteen blocked
on the dandiset; of five more claims on the bead and dye images in the paper's
code repository, three are reproduced, one partially and one blocked. The
attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were
written from the abstract and public figure legends only; the claims file was
written again from the full text and the paper's code, so it has 23 claims,
nine of them new or restored, and several criteria that rested on the earlier
author's thresholds now use the paper's numbers. It pins the same version,
0.260827.1358, the only published version, whose draft holds the same files,
so every difference from `-01` comes from the claims file. The author put no
questions to a reader, and the answer run found no questions file, so nothing
changed. Round 1 gave its own outcome for 22 of the 23 claims from the
notebooks with their conclusion cells and summaries removed (none for
`ed3-adc`) and agreed with 20 of them; it gave reproduced for
`fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of
one fit per shuffled decoder (n1) alone, and called `ed7-motion-small`
tentative because nothing checked that the movie is raw. The author kept both
decoding claims blocked as `not_runnable`, and round 2 agreed with all 23
[... 102 more lines not kept]
```

**Agent**

I ran `python tools/readme_row.py 000691 --write`. It replaced the 000691 row in README.md, which had been marked deprecated, with 2 reproduced, 0 partially, 1 not reproduced and 15 blocked. I then added the subsection below to the end of docs/pilot-notes.md. Nothing is committed.

The README counts cover 18 of the 23 claims. The other five use bead and dye images from the paper's code repository, and the tool leaves claims on outside data out of the counts. The first sentence gives their outcomes separately.

The `catalystneuro` field names a contributor, not a repository, so I followed the 000582 subsection's wording for that opening sentence. The earlier first attempt already has a subsection headed "### 000691, Scherrer et al. 2023", so this one is headed "second attempt".

### 000691, Scherrer et al. 2023, second attempt

Two claims reproduced, none partially, one not reproduced and fifteen blocked
on the dandiset; of five more claims on the bead and dye images in the paper's
code repository, three are reproduced, one partially and one blocked. The
attempt replaces the deprecated 000691-scherrer-2023-01, whose claims were
written from the abstract and public figure legends only; the claims file was
written again from the full text and the paper's code, so it has 23 claims,
nine of them new or restored, and several criteria that rested on the earlier
author's thresholds now use the paper's numbers. It pins the same version,
0.260827.1358, the only published version, whose draft holds the same files,
so every difference from `-01` comes from the claims file. The author put no
questions to a reader, and the answer run found no questions file, so nothing
changed. Round 1 gave its own outcome for 22 of the 23 claims from the
notebooks with their conclusion cells and summaries removed (none for
`ed3-adc`) and agreed with 20 of them; it gave reproduced for
`fig2-quadrant-direction-decoding` and `ed9b-octant-decoding`, on the null of
one fit per shuffled decoder (n1) alone, and called `ed7-motion-small`
tentative because nothing checked that the movie is raw. The author kept both
decoding claims blocked as `not_runnable`, and round 2 agreed with all 23
outcomes; nothing was proposed, so there was no third round. The paper, "An
optical design enabling lightweight and large field-of-view head-mounted
microscopes", describes two head-mounted microscopes, the Kiloscope (about 4
mm field of view, 1.4 g) and the Featherscope (1.0 mm, 1.0 g), used in four
mice and three juvenile zebra finches, and reports thousands of neurons
recorded at once in a freely moving mouse, from whose activity linear decoders
read the mouse's combined quadrant and movement direction at least three times
above chance. The footprint count, the field of view, the bead PSFs, field
curvature, the flat illumination of both microscopes and the motion of the
movie were tested, and the decoding claims were run under the (n1) null.
`ed7-motion-small` is not reproduced (0.037 px RMS against 0.13), and
`fig1f-kiloscope-psf` is partially reproduced because no reading puts both
values within tolerance. The decoding claims hold under (n1) (median accuracy
0.437 and 0.326 against the largest of 1000 shuffled decoders at 0.227 and
0.229), but the criterion also needs (n2), 200 fits per shuffled decoder,
which is 200,000 fits, measured for the quadrant claim at 33.3 hours in this
run (24.6 hours in the run of round 2) against 30 minutes per notebook, so
fig2 and ed9b are blocked as `not_runnable`, and `fig2k-decoder-size`,
`fig2l-local-decoding-map` and `ed9c-local-decoding-map` also, as they depend
on them and need 4.4 to 12.8 hours each on four cores. The other mice, the
songbirds, the weights, the USAF target images and the ADC recordings are not
deposited, `ed6a-curated-footprints` is blocked as `metadata_insufficient`,
and `fig2d-lman-sparse-bursting`, `ed8-coactive-distributed` and
`ed10-localized-activity` as `methods_underspecified`, ed8 because all four
quarters are covered in 8 of 8 events under one reading of the event times and
7 of 8 under the other. Compared with `-01`, abstract-kiloscope-fov moved from
blocked to reproduced, the two flat-illumination claims from partially
reproduced to reproduced, and ed8, ed9b, ed9c and ed10 from reproduced to
blocked. Some outcomes rest on weak ground: in abstract-kiloscope-fov both
pixel sizes come from the paper's code, the reading at 5.35 um per pixel only
just within tolerance (4.323 against a lower bound of 4.32) and the test close
to circular at 5.94 um per pixel; and the Kiloscope PSF fits depend on the
optimizer and differ between runs on different machines (4.467 um at the
centre under reading (a) in this run, 4.422 um in the run of round 2).

The dataset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro is a
contributor). The files are unchanged, so the nine findings of `-01` were
checked again, and all are still present. The dandiset holds one of the
paper's four mice and none of the songbird recordings, and the USAF target
images and ADC recordings are not public. The mouse's position, which the
paper's decoding and place analyses use, is not in the dandiset (its only
processing module is ophys), and the opening of the behaviour video that the
paper's code skips is not marked. The 2948 footprints are the EXTRACT output
before curation; the paper analyses the 2,382 it kept, and nothing marks them
or says the footprints are uncurated. The device description reads
"Head-mounted microscope (Kiloscope) optimized for weight (1.0 mm FOV; 1.0
g)", and the dandiset description also names the microscope optimized for
weight, where the data are from the large-FOV Kiloscope (4 mm window, 2948
footprints, 808 x 608 pixel frames). The imaging is stored as a
TwoPhotonSeries and two-photon microscopy is listed among the techniques,
though the microscope is a one-photon head-mounted epifluorescence microscope.
Nothing says whether the movie is the raw video or the motion-corrected one
the paper extracted footprints from; its values are consistent with the raw
video, and its rigid shifts against a template have an RMS of 0.037 pixels,
about a quarter of the 0.13 pixels the paper reports. Other findings: the
behaviour video is described as about 30 fps and its AVI header says 30
frames/s, but its 15521 timestamps run at a median 12.5 frames/s over 1234 s;
the imaging plane gives no pixel size, its indicator and location are
"unknown" and its excitation wavelength is NaN, although general/virus says
GCaMP7f; ROICentroids equal the mask's peak pixel for 84% of footprints and
the rounded weighted centroid for only 43%; both local decoding map scripts
use 64 footprints within 50 pixels where the paper describes the 32 closest
within 270 um; the Extended Data Fig. 8 legend refers to a Figure 3 and a
ridgeline plot in Fig. 2d, where the paper has two figures and the ridgeline
plot is Fig. 2h; the paper's tracking code unwraps position with MATLAB's
unwrap, which gains an error of up to pi cm at every lap of the 147.1 cm loop
and changes about 1% of the running and direction labels; and the paper's bead
scripts order the images by file date, which the repository does not keep, so
the Kiloscope stack's slice order is not recorded.

The notebooks, four at first, ran in 7 min, 19 min, 19 min and 22 min in the
first clean run and 497 s, 1122 s, 1124 s and 1237 s after the answer run.
`entry.py check`, and so `entry.py all`, failed throughout on 11 errors, all
in the deprecated record, which has no outcomes for the new claims and must
stay as it is, and the notebooks were run with `entry.py run`. Round 1's
points led to a check of whether the movie is raw (histogram roughness 0.740
to 0.745, which sub-pixel shifts of 0.13 px RMS lower to 0.052, and a known
jitter of 0.132 px RMS recovered with correlation 0.996), so ed7 is no longer
tentative, PSF readings with the lower-cost fit for each bead, the lines of
each illumination script that load the images, ed8 counts with the quarters
split at the image midlines, the real decoders' single fits compared with the
(n1) null, nine (n2) null decoders per decoding claim, and three new
notebooks, two of (n2) null decoders and one of reduced runs of fig2k, fig2l
and ed9c that decide nothing, none changing an outcome;
`fig2d-lman-sparse-bursting` changed its block reason from `data_missing` to
`methods_underspecified`. In both revisions the 2-hour command limit cut the
run of seven notebooks, and the last, `decoding_reduced.ipynb`, was run on its
own. Round 2 found numbers in the prose that its run did not print, among them
the fig1f margins, the run times and 5 of 56 significant points in the reduced
ed9c run where its run printed 0; the run made for the second revision printed
the prose's fig1f numbers, and the PSF fits, the reduced runs and the timings
turned out to differ between runs on different machines even with every seed
fixed (in the reduced ed9c run, 7 of 56 points significant in one run and 0 in
the other). The cause was not found, and the record gives both runs' values.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: `entry.py check` fails on the
deprecated `-01` record, which must stay unchanged, so `entry.py all` cannot
pass; the section on repeat attempts assumes the claims file is kept and the
dataset changed, where here the claims file was rewritten and the data were
not; and the claims file sets decoding methods that need 10^5 fits, which a
30-minute limit per notebook cannot decide whatever the data.

## End of run

24 turns, 3 minutes, result: success.
