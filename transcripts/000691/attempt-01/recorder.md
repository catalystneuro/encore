# 000691 · recorder · run 39098250362

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000691 --write; git diff; ls claims/000691 transcripts/000691; cat attempts/000691-scherrer-2023-01.yaml
```

```
<persisted-output>
Output too large (33.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/76e4ddfd-f662-41a3-b7e0-4543201a45b7/tool-results/b7bax4m3f.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 0851140..30fe037 100644
--- a/README.md
+++ b/README.md
@@ -86,6 +86,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
 | [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s41586-022-05611-2) | 7 | 3 | 2 | 12 | [`000559-markowitz-2023`](entries/000559-markowitz-2023) |
 | [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
+| [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000691:
10.1038-s41592-023-01806-1.yaml

transcripts/000691:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
git status --short; grep -n "^| Dandiset\|^| ---\|^|---" README.md | head; sed -n 70,80p README.md; cat attempts/000691-scherrer-2023-01.yaml
```

```
<persisted-output>
Output too large (34.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/76e4ddfd-f662-41a3-b7e0-4543201a45b7/tool-results/bf50ris05.txt

Preview (first 2KB):
 M README.md
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
?? scripts
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
| [000044](https://dandiarchive.org/dandiset/000044) | [Grosmark et al. 2016](https://doi.org/10.1126/science.aad1935) | 3 | 3 | 6 | 8 | [`000044-grosmark-2016`](entries/000044-grosmark-2016) |
| [000056](https://dandiarchive.org/dandiset/000056) | [Peyrache et al. 2015](https://doi.org/10.1038/nn.3968) | 6 | 2 | 0 | 13 | [`000056-peyrache-2015`](entries/000056-peyrache-2015) |
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^### " docs/pilot-notes.md | tail -6; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
print([x for x in (d if isinstance(d,list) else d.values()) if '000691' in json.dumps(x)])"
```

```
<persisted-output>
Output too large (153.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/76e4ddfd-f662-41a3-b7e0-4543201a45b7/tool-results/b7cfohh7u.txt

Preview (first 2KB):
2310:### 000350, Mu et al. 2019
2394:### 000409, International Brain Laboratory et al. 2025
2489:### 000552, Huszar et al. 2022
2587:### 000568, Valero et al. 2022
2679:### 000559, Markowitz et al. 2023
2764:### 000718, Zaki et al. 2024
[[{'dandiset': '000003', 'name': 'Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells', 'published_version': '0.260218.2052', 'asset_count': 101, 'size_gb': 2559.25, 'data_standards': ['Neurodata Without Borders (NWB)'], 'species': ['House mouse'], 'approaches': ['electrophysiological approach', 'behavioral approach'], 'papers': [{'doi': '10.1016/j.neuron.2016.12.011', 'title': 'Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells', 'relation': 'IsDescribedBy', 'resource_type': 'JournalArticle', 'preprint': False}], 'catalystneuro': ['contributor Baker, Cody of CatalystNeuro']}, {'dandiset': '000004', 'name': 'A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task', 'published_version': '0.220126.1852', 'asset_count': 87, 'size_gb': 6.2, 'data_standards': ['Neurodata Without Borders (NWB)'], 'species': ['Human'], 'approaches': ['electrophysiological approach'], 'papers': [{'doi': '10.1038/s41597-020-0415-9', 'title': 'A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task', 'relation': 'IsDescribedBy', 'resource_type': 'JournalArticle', 'preprint': False}], 'catalystneuro': ['contributor Dichter, Benjamin of CatalystNeuro']}, {'dandiset': '000005', 'name': 'Electrophysiology data from thalamic and cortical neurons during somatosensation', 'published_version': '0.220126.1853', 'asset_count': 148, 'siz
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print([x for x in d if x['dandiset']=='000691'])"; sed -n 2394,3000p docs/pilot-notes.md
```

```
<persisted-output>
Output too large (31.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/76e4ddfd-f662-41a3-b7e0-4543201a45b7/tool-results/bbk0ze26x.txt

Preview (first 2KB):
 README.md | 1 +
 1 file changed, 1 insertion(+)
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    print([x for x in d if x['dandiset']=='000691'])
                           ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
### 000409, International Brain Laboratory et al. 2025

Seventeen claims reproduced, three partially, three not reproduced and seven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 29 of the 30;
it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
author kept partially reproduced. Round 1 also found that
`traj-stim-regions`, left as not attempted, fits the time limit, so the
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 2394
}
```

```
2394	### 000409, International Brain Laboratory et al. 2025
2395	
2396	Seventeen claims reproduced, three partially, three not reproduced and seven
2397	blocked, all on the dandiset. Round 1 gave its own outcome for each claim
2398	from the notebook with its conclusions removed and agreed with 29 of the 30;
2399	it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
2400	58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
2401	author kept partially reproduced. Round 1 also found that
2402	`traj-stim-regions`, left as not attempted, fits the time limit, so the
2403	author wrote a criterion for it and tested it. Round 2 disagreed on the same
2404	claim, since the criterion defines no partial outcome, the author proposed
2405	not reproduced, and a third round agreed. The paper reports a brain-wide map
2406	of neural activity in mice performing a visual decision task with a block
2407	prior, from 459 sessions of 139 mice in 12 labs: the dataset and its
2408	canonical set of 201 regions, task behaviour, decoding of stimulus, choice
2409	and feedback, single-cell selectivity, neural trajectories and their
2410	latencies, and a feedback oscillation tied to licking. The dataset counts,
2411	mice, probes and trials, behaviour, decoding, trajectory latencies, the
2412	number of regions with significant stimulus trajectories and the oscillation
2413	were tested, the neural claims on VISp, GRN, IRN and seven regions drawn at
[... 441 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000691-scherrer-2023-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
for k in (d if isinstance(d,dict) else []):
  v=d[k]
  if isinstance(v,list):
    for x in v:
      if isinstance(x,dict) and x.get('dandiset')=='000691': print(x)
"
```

```
<persisted-output>
Output too large (32.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/76e4ddfd-f662-41a3-b7e0-4543201a45b7/tool-results/bymwg0hck.txt

Preview (first 2KB):
schema_version: 1
id: 000691-scherrer-2023-01
dandiset: "000691"
dandiset_version: 0.260827.1358
paper: doi:10.1038/s41592-023-01806-1
date: 2026-10-17
entry: 000691-scherrer-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000691-scherrer-2023-01.yaml"
}
```

```
1	schema_version: 1
2	id: 000691-scherrer-2023-01
3	dandiset: "000691"
4	dandiset_version: 0.260827.1358
5	paper: doi:10.1038/s41592-023-01806-1
6	date: 2026-10-17
7	entry: 000691-scherrer-2023
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: Images of a thin layer of fluorescent dye taken with the Featherscope and the Kiloscope with
18	    correction optics, with diffuse light, and with the plain laser (sf3/feather and sf3/widefield),
19	    used for ed2b-featherscope-flat-illumination and ed2c-kiloscope-flat-illumination. The same
20	    repository's analysis code supplied the parameters of every analysis (tracking rule, decoder
[... 498 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 88,110p README.md; grep -n "000718\|000691" README.md
```

````
| [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
| [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |

Counts are of claims that rest on the dandiset, including those that take
names for its own codes from elsewhere. Claims that also use data from
outside the dandiset are counted apart, in brackets. Claims on data the
paper deposited in other archives are not in this table; the dashboard
shows them on each dandiset's page.

## Agent runs

Attempts by agents are made in GitHub Actions, one role at a time, on the
subscription token in the `CLAUDE_CODE_OAUTH_TOKEN` secret:

```bash
gh workflow run attempt.yml -f dandiset=000147 -f role=author
```

The roles, in order, are `author`, `verifier-1`, `author-revise-1`,
`verifier-2` and `author-revise-2`, then `verifier-3` and `author-revise-3`
[... 5 more lines not kept]
````

**Agent calls Bash**

```bash
cat claims/000691/*.yaml; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
def walk(o):
    if isinstance(o,dict):
        if o.get('dandiset')=='000691': print(o); return
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
E
```

```
# Claims for Scherrer, Lynch, Zhang & Fee (2023) on dandiset 000691.
# Source: the version of record in Nature Methods is not open access. The claims are written from
# its abstract and from the parts of its article page that are public: the figure titles, the
# Extended Data legends, and the data and code availability statements. The Extended Data figure
# numbers below are those of the version of record. The main text and the legends of Figures 1
# and 2 were not available. The bioRxiv preprint (10.1101/2021.09.03.458947, version 2) was read
# for its Methods only, to fill in procedures the code leaves open; no expected value is taken
# from it.
#
# When these criteria were written, the author had seen the data check (file list, metadata, every
# dataset of the NWB file, timestamps of both streams, the behaviour video and a first tracking of
# the mouse in it) and one prototype of the quadrant and direction decoder: three fits with
# median per-class accuracies of 0.44 to 0.58, and three fits with shifted labels at 0.04 to 0.12.
# No other claim's analysis had been run.
#
# The dandiset holds one session of one mouse imaged with the large-FOV microscope (the
# Kiloscope): the raw imaging video, 2948 EXTRACT footprints with their traces and centroids, and
# a behaviour video of the mouse in a looped corridor maze. It holds no position, no curation of
# the footprints, no pixel size, and no data from the other mice, the birds, or the optical tests.
#
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000691; for f in author-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-report.md
I completed steps 1 to 6 for dandiset 000691. `tools/entry.py all` passes; the notebook takes 18 minutes and gave identical numbers on two clean runs. The handover is in `executed/000691-scherrer-2023/handover/`. I did not verify my own work, and nothing is committed.

**Paper used:** the version of record is not open access (Unpaywall wrongly flags it as open). I used its abstract plus the parts of the article page that are public: figure titles, Extended Data legends, and the data and code statements. I read the bioRxiv preprint (v2, saved in `paper/`) for its Methods only; no expected value comes from it.

**Version pinned:** 0.260827.1358. The paper cites no DANDI version, this is the only published one, and the draft holds the same two blobs.

### 1. Outcome per claim

| Claim | Data | Outcome |
|---|---|---|
| abstract-thousands-of-neurons | dandiset | reproduced (2948 footprints, no near-duplicates) |
| fig2-quadrant-direction-decoding | dandiset | reproduced (0.415 against null 95th percentile 0.145, chance 0.125) |
| ed9b-octant-decoding | dandiset | reproduced (0.313 against 0.144) |
| ed9c-local-decoding-map | dandiset | not reproduced (0 of 151 points significant; the code's 64-footprint variant gives 4 of 77) |
| ed10-localized-activity | dandiset | reproduced (100 footprints localized against 29 expected) |
| ed8-coactive-distributed | dandiset | reproduced (8 of 8 components) |
| ed6a-curated-footprints (2382) | dandiset | blocked: metadata_insufficient |
| abstract-kiloscope-fov | dandiset | blocked: metadata_insufficient (no pixel size) |
| ed6bcd-other-mice, ed5-songbirds, abstract-weights, ed1-ed4-resolution, ed3-adc | dandiset | blocked: data_missing |
[... 201 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "(deposited elsewhere|in other archives|not in the README|data elsewhere|counted apart|outside the table)",
 "path": "docs/pilot-notes.md",
 "output_mode": "content"
}
```

```
602:nine blocked. With outside data, counted apart: two reproduced, one
658:outside data, counted apart: five reproduced, one partially and two not
943:proteomics and blots behind Figures 1 to 5 are in other archives, so those
973:## Protocol pilot-7 (2026-10-15): data in other archives
1133:on data in other archives, of which four reproduced, three partially and
2062:With outside data, counted apart: two reproduced and one partially. Round 1
2767:dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
2848:repository of per-mouse figure values counts as data deposited elsewhere; a
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 1128,
 "limit": 12
}
```

```
1128	
1129	The second attempt, made because pilot-7 changed the protocol; the dandiset
1130	(0.260825.1457), the paper's code and the paper are unchanged. Six claims
1131	reproduced, two partially and one not reproduced on the dandiset, plus the
1132	link claim using the paper's source data, not reproduced, and eight claims
1133	on data in other archives, of which four reproduced, three partially and
1134	one not reproduced; before, the dandiset's counts were the same and the
1135	eight were blocked. Round 1 disagreed on one outcome,
1136	`fig3d-rim-binds-unphosphorylated`, which the author had decided with an
1137	imputation the criterion lists as a variant, because RILPL2 is found only
1138	in the p-RAB3A pulldowns and the paired test has no pairs for it; the
1139	author changed it to partially reproduced (3 of 4), round 2 agreed with all
```

**Agent calls Bash**

```bash
cd  && tail -c 200 docs/pilot-notes.md | od -c | tail -3 && cat >> docs/pilot-notes.md <<'EOF'

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
direction in a looped maze can be decoded from the imaged activity. The
footprint count and the mouse's coverage of the maze, decoding of quadrant
with direction and of octant, the local decoding map, localized activity
and the spread of coactive footprints in 8 NMF components were tested on the
one deposited mouse, with position tracked from the behaviour video, and the
flat illumination of both microscopes on dye images in the paper's code
repository. The 2382 curated footprints and the field of view are blocked as
`metadata_insufficient`, and the other mice, the songbirds, the weights, the
resolution targets and the analog-to-digital converter as `data_missing`.
Some outcomes rest on weak ground: `ed9c-local-decoding-map` gives 1
significant point with SGD and 18 of 150 with liblinear, the solver was
changed after round 1, liblinear reached its limit of 10,000 iterations in
2268 of 3000 fits, and the smallest significant z, 2.53, is below the 3.40 a
point needs alone; in `ed8-coactive-distributed` random sets of footprints of
the same size have spread ratios of 0.951 to 1.042, so any set this large
passes the criterion's half; `ed2c-kiloscope-flat-illumination` misses the
0.8 level the author chose by 0.003 and is above it for one of four 100 um
moves of the centre; and every analysis uses all 2948 footprints in place
of the 2382 curated ones. The version of record is not open access, so the
author used its abstract, figure titles, Extended Data legends and data and
code statements, read the bioRxiv preprint (version 2) for its Methods only,
and took the parameters of every analysis from the paper's code at commit
d596646; the legend of Figure 2 and the main text's numbers were not tested.

The dandiset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro
is a contributor). It holds one of the paper's four mice and none of the
songbird recordings or optical test data, and the Academic Torrents deposit
the paper names for its imaging data holds files of the same mouse session
only, so the other mice and the birds are not public. The 2948 footprints
are the EXTRACT output before curation, and nothing in the dandiset marks
the 2382 the paper kept or says that the footprints are uncurated; the
curation is in the Academic Torrents deposit, where no peer connected in two
attempts of 2.5 and 4 minutes. The mouse's position, which the decoding and
place analyses use, is not in the dandiset and must be tracked from the
behaviour video, and the first 64 s of the video (by its nominal rate), which
the paper's code drops because the experimenter is in view, are not marked.
The device description reads "Head-mounted microscope (Kiloscope) optimized
for weight (1.0 mm FOV; 1.0 g)" and the dandiset description also names the
microscope optimized for weight, while the data are from the large-FOV
microscope (a 4 mm window, 2948 footprints and 808 x 608 pixel frames). The
imaging is stored as a TwoPhotonSeries and listed as two-photon microscopy,
though the microscope is a one-photon epifluorescence microscope. Other
findings: the behaviour video is described as about 30 fps and its AVI
header says 30 frames/s, but its 15521 timestamps run at a median 12.5
frames/s over 1234 s, and at 30 frames/s it would cover only 517 s of the
1234 s of imaging; the imaging plane gives no pixel size, and its indicator
and location are "unknown" with no excitation wavelength, although
general/virus says GCaMP7f; the Extended Data Fig. 9c legend describes
decoders on the 32 closest footprints within 270 um, where the code uses 64
within 50 pixels, which at the code's own 5.94 um per pixel is 297 um; and
the title of Extended Data Fig. 8 refers to the Kiloscope data "shown in
Figure 3", while the version of record has two figures. The masks, the movie
and the traces line up, and position decoding peaks within about a second
of zero shift, so the clocks are reported as consistent, though offsets of
1 to 2 s could not be told apart.

The notebook ran in 18 minutes in the first clean run and in 25.2 minutes
after round 2. Streaming the behaviour video with PyAV over HTTPS and
through remfile failed, so the notebook reads the 105 MB file into memory;
liblinear's coordinate order was seeded after round 1, as unseeded the
exact map's count of significant points changed between runs; and the code's
64-footprint variant of the local map stays on a 60 pixel grid where the
criterion says 40, since on 40 the notebook took 32 minutes, over the
30-minute limit. Round 2 found numbers in the text that the executed
notebook contradicted (19 significant points against 18, 2264 fits at the
limit against 2268); the copy it read came from another machine, three runs
on four cores gave the stated numbers, and the text now says the counts can
differ slightly between machines. The author's points on the protocol: a
paper that is not open access whose legends and preprint are public; outside
data on a torrent with no peers, which the blocking categories do not fit;
whether data derived from the dandiset's own video, such as position, count
as dandiset data; an image-reading check that forbids reading measurement
images that are data; hardware claims with no data anywhere; a clock check
that cannot resolve offsets of 1 to 2 s; an outcome 0.003 from a threshold
the author chose, as the legend gives no number for flat; and a prototype
decoder run before the criteria were written.
EOF
git diff --stat
```

```
0000260   n   d       i   n       a   n       i   s   s   u   e       o
0000300   f       2   0   2   5   .  \n
0000310
 README.md           |  1 +
 docs/pilot-notes.md | 93 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 94 insertions(+)
```

**Agent**

I ran `python tools/readme_row.py 000691 --write`, which added the README row (6 reproduced, 0 partially, 0 not reproduced, 7 blocked), and I added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed. The repository root has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others), and I left them alone.

The table counts only claims that rest on the dandiset. The attempt's two partially reproduced claims use dye images from the paper's code repository, so the README row leaves them out. The first paragraph gives them separately, following the wording of an earlier subsection.

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
direction in a looped maze can be decoded from the imaged activity. The
footprint count and the mouse's coverage of the maze, decoding of quadrant
with direction and of octant, the local decoding map, localized activity
and the spread of coactive footprints in 8 NMF components were tested on the
one deposited mouse, with position tracked from the behaviour video, and the
flat illumination of both microscopes on dye images in the paper's code
repository. The 2382 curated footprints and the field of view are blocked as
`metadata_insufficient`, and the other mice, the songbirds, the weights, the
resolution targets and the analog-to-digital converter as `data_missing`.
Some outcomes rest on weak ground: `ed9c-local-decoding-map` gives 1
significant point with SGD and 18 of 150 with liblinear, the solver was
changed after round 1, liblinear reached its limit of 10,000 iterations in
2268 of 3000 fits, and the smallest significant z, 2.53, is below the 3.40 a
point needs alone; in `ed8-coactive-distributed` random sets of footprints of
the same size have spread ratios of 0.951 to 1.042, so any set this large
passes the criterion's half; `ed2c-kiloscope-flat-illumination` misses the
0.8 level the author chose by 0.003 and is above it for one of four 100 um
moves of the centre; and every analysis uses all 2948 footprints in place
of the 2382 curated ones. The version of record is not open access, so the
author used its abstract, figure titles, Extended Data legends and data and
code statements, read the bioRxiv preprint (version 2) for its Methods only,
and took the parameters of every analysis from the paper's code at commit
d596646; the legend of Figure 2 and the main text's numbers were not tested.

The dandiset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro
is a contributor). It holds one of the paper's four mice and none of the
songbird recordings or optical test data, and the Academic Torrents deposit
the paper names for its imaging data holds files of the same mouse session
only, so the other mice and the birds are not public. The 2948 footprints
are the EXTRACT output before curation, and nothing in the dandiset marks
the 2382 the paper kept or says that the footprints are uncurated; the
curation is in the Academic Torrents deposit, where no peer connected in two
attempts of 2.5 and 4 minutes. The mouse's position, which the decoding and
place analyses use, is not in the dandiset and must be tracked from the
behaviour video, and the first 64 s of the video (by its nominal rate), which
the paper's code drops because the experimenter is in view, are not marked.
The device description reads "Head-mounted microscope (Kiloscope) optimized
for weight (1.0 mm FOV; 1.0 g)" and the dandiset description also names the
microscope optimized for weight, while the data are from the large-FOV
microscope (a 4 mm window, 2948 footprints and 808 x 608 pixel frames). The
imaging is stored as a TwoPhotonSeries and listed as two-photon microscopy,
though the microscope is a one-photon epifluorescence microscope. Other
findings: the behaviour video is described as about 30 fps and its AVI
header says 30 frames/s, but its 15521 timestamps run at a median 12.5
frames/s over 1234 s, and at 30 frames/s it would cover only 517 s of the
1234 s of imaging; the imaging plane gives no pixel size, and its indicator
and location are "unknown" with no excitation wavelength, although
general/virus says GCaMP7f; the Extended Data Fig. 9c legend describes
decoders on the 32 closest footprints within 270 um, where the code uses 64
within 50 pixels, which at the code's own 5.94 um per pixel is 297 um; and
the title of Extended Data Fig. 8 refers to the Kiloscope data "shown in
Figure 3", while the version of record has two figures. The masks, the movie
and the traces line up, and position decoding peaks within about a second
of zero shift, so the clocks are reported as consistent, though offsets of
1 to 2 s could not be told apart.

The notebook ran in 18 minutes in the first clean run and in 25.2 minutes
after round 2. Streaming the behaviour video with PyAV over HTTPS and
through remfile failed, so the notebook reads the 105 MB file into memory;
liblinear's coordinate order was seeded after round 1, as unseeded the
exact map's count of significant points changed between runs; and the code's
64-footprint variant of the local map stays on a 60 pixel grid where the
criterion says 40, since on 40 the notebook took 32 minutes, over the
30-minute limit. Round 2 found numbers in the text that the executed
notebook contradicted (19 significant points against 18, 2264 fits at the
limit against 2268); the copy it read came from another machine, three runs
on four cores gave the stated numbers, and the text now says the counts can
differ slightly between machines. The author's points on the protocol: a
paper that is not open access whose legends and preprint are public; outside
data on a torrent with no peers, which the blocking categories do not fit;
whether data derived from the dandiset's own video, such as position, count
as dandiset data; an image-reading check that forbids reading measurement
images that are data; hardware claims with no data anywhere; a clock check
that cannot resolve offsets of 1 to 2 s; an outcome 0.003 from a threshold
the author chose, as the legend gives no number for flat; and a prototype
decoder run before the criteria were written.

## End of run

14 turns, 2 minutes, result: success.
