# 000727 · recorder · run 39099562569

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000727 --write; git diff; ls transcripts/000727/ claims/000727/; cat attempts/000727-brezovec-2022-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000727' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (221.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/23c5ce17-5fba-460a-af8d-f09ea3ed570f/tool-results/b6qukvbpi.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 30fe037..9a407eb 100644
--- a/README.md
+++ b/README.md
@@ -87,6 +87,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000559](https://dandiarchive.org/dandiset/000559) | [Markowitz et al. 2023](https://doi.org/10.1038/s41586-022-05611-2) | 7 | 3 | 2 | 12 | [`000559-markowitz-2023`](entries/000559-markowitz-2023) |
 | [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
 | [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
+| [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000727/:
10.1101-2022.03.20.485047.yaml

transcripts/000727/:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^| Dandiset\|^| ---\|^|--" README.md | head; cat attempts/000727-brezovec-2022-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000727' in json.dumps(x)[:300]];print(json.dumps(e,indent=1)[:3000])"
```

```
<persisted-output>
Output too large (41.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/23c5ce17-5fba-460a-af8d-f09ea3ed570f/tool-results/blmejmfd7.txt

Preview (first 2KB):
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
schema_version: 1
id: 000727-brezovec-2022-01
dandiset: '000727'
dandiset_version: 0.240106.0043
paper: doi:10.1101/2022.03.20.485047
date: 2026-10-18
entry: 000727-brezovec-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/23c5ce17-5fba-460a-af8d-f09ea3ed570f/tool-results/blmejmfd7.txt"
}
```

```
1	49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
2	50:|---|---|---|---|---|---|---|
3	schema_version: 1
4	id: 000727-brezovec-2022-01
5	dandiset: '000727'
6	dandiset_version: 0.240106.0043
7	paper: doi:10.1101/2022.03.20.485047
8	date: 2026-10-18
9	entry: 000727-brezovec-2022
10	provenance:
11	  kind: agent
12	  accountable:
13	    name: CatalystNeuro
14	  agent:
15	    harness: Claude Code (GitHub Actions)
16	    model: claude-opus-5-5
17	    protocol: pilot-7
18	inputs:
19	- what: Procedures and parameters, no data. The behaviour variables (FicTrac dRotLabY and dRotLabZ, Savitzky-Golay
20	    25 frames order 3, clipping into forward, left and right, the 4.5 mm ball radius), the walking state,
[... 647 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "000727" targets/dandisets.json | head; grep -n -B3 -A25 '"000727"' targets/dandisets.json | head -60; grep -n "^##" docs/pilot-notes.md | tail -8; wc -l docs/pilot-notes.md
```

```
3071:   "dandiset": "000727",
3068-   ]
3069-  },
3070-  {
3071:   "dandiset": "000727",
3072-   "name": "Mapping the Neural Dynamics of Locomotion across the Drosophila Brain",
3073-   "published_version": "0.240106.0043",
3074-   "asset_count": 18,
3075-   "size_gb": 609.57,
3076-   "data_standards": [
3077-    "Neurodata Without Borders (NWB)"
3078-   ],
3079-   "species": [
3080-    "Drosophila melanogaster - Fruit fly"
3081-   ],
3082-   "approaches": [
3083-    "behavioral approach",
3084-    "microscopy approach; cell population imaging"
3085-   ],
3086-   "papers": [
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3095,3102p targets/dandisets.json; sed -n 2489,2946p docs/pilot-notes.md
```

```
<persisted-output>
Output too large (31.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/23c5ce17-5fba-460a-af8d-f09ea3ed570f/tool-results/bcmrjn0ee.txt

Preview (first 2KB):
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/clandinin-lab-to-nwb",
    "contributor Mayorquin, Heberto of CatalystNeuro",
    "contributor Trapani, Alessandra of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000773",
### 000552, Huszar et al. 2022

Five claims reproduced, four partially, three not reproduced and twenty-three
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 34 of the 35;
it gave reproduced for `cohort-birthdates`, as the sex field differs between
files of the same mouse and each mouse's majority value gives the paper's 12
males and 5 females, and the author changed that claim from not reproduced
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/23c5ce17-5fba-460a-af8d-f09ea3ed570f/tool-results/bcmrjn0ee.txt",
 "offset": 180
}
```

```
180	its 289 of 417.
181	
182	The notebook ran in 272 s in the first clean run and in 289 s after round 3.
183	The author's own choice of control maps as all time without light, made
184	before noticing that the paper's control epochs are 20 ms intervals between
185	pulses, was kept with time-matched windows as a variant, and that variant
186	decided `fig3g-spatial-information`. After round 1 the paper could not be
187	downloaded again (PMC returned 429 and 503 errors and Europe PMC a 500), the
188	round-2 verifier could not run the new field rule as numpy was not installed,
189	and untracked files in the repository root that the author did not create
190	were left alone. The author's points on the protocol: no rule for when the
191	paper's Methods cannot be obtained; reading the code the paper links to does
192	not fit a general toolbox without scripts for the paper; no guidance for data
193	a claim needs that exist for only a few sessions; the duplicate check does not
194	cover every session deposited twice as a full and a no-raw-data file; a 10%
195	tolerance narrower than sampling error for correlations; no category for a
196	named data location without a pinned identifier; and no rule for what to
197	record as measured when only a later reading of the criterion matches.
198	
199	### 000559, Markowitz et al. 2023
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000727; wc -l *-report.md; cat author-report.md
```

```
51 author-report.md
   26 author-revise-1-report.md
   19 author-revise-2-report.md
   64 verifier-1-report.md
   64 verifier-2-report.md
  224 total
I've finished steps 1 to 5 and ran the handover (step 6). The entry is `entries/000727-brezovec-2022/`. It passes `check`, and `all` ran clean twice in a fresh environment with identical numbers. Nothing is committed.

I used the full text of bioRxiv v1 (21 March 2022, CC BY-NC-ND), the only preprint version, saved under `paper/`. The later Current Biology version is paywalled and was not used. I pinned 0.240106.0043, the only published version. The paper cites no DANDI version, and the draft has the same 18 assets with metadata-only changes.

## 1. Outcomes (8 reproduced, 5 partial, 1 not reproduced, 6 blocked)

| Claim | Outcome |
|---|---|
| dataset-structure (9 flies, 30,456 volumes, 1.88 Hz, 1.6M voxels, 50 Hz tracking) | reproduced |
| fig2c-fraction-correlated (39%) | partially: 31.1% at voxel level. Sampling behaviour at volume start instead of the midpoint gives 39.2% (variant only) |
| fig2c-venn-categories (15 / 20 / 4 / 10%) | partially: 11.9 / 15.9 / 3.2 / 11.5%, ranking holds |
| fig2-symmetry | reproduced (forward map vs its mirror r = 0.82; left and right turning on opposite halves) |
| fig4bcd-pc-structure | reproduced |
| fig4fg-ridge-r2 (R² ≈ 0.3) | partially: medians 0.155, 0.196, 0.212. Interleaved folds give 0.318, 0.252, 0.271 (variant only) |
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000727; cat author-revise-1-report.md author-revise-2-report.md; cat verifier-1-report.md verifier-2-report.md | head -140
```

```
No outcome changed. The 14 tested outcomes stay at 7 reproduced, 5 partially reproduced, 1 not reproduced and 1 reproduced but disputed (fig5c), with 6 blocked. The entry was re-run twice from a clean environment, passes `check`, and both runs give identical numbers in about 12.5 minutes. The round is recorded under `verifications` in `attempts/000727-brezovec-2022-01.yaml`, and nothing is committed.

**Outcome disagreements**
- **fig5c-global-below-threshold:** I kept "reproduced" and recorded the disagreement; the verifier would give "partially reproduced". Its objection was that the p = 0.031 behind the pass ignores autocorrelation. I added the null it asked for: 200 circular shifts of each fly's behaviour, which keep the autocorrelation. Under reading (b) all nine below-threshold correlations still beat it. The weakest, r = 0.013, has p = 0.025 against a null 95th percentile of 0.010. Reading (a) still fails.
- **The four region-level claims (fig2e, fig3, fig6eg, fig7):** the verifier agrees they are blocked but would give `data_missing`. I kept `metadata_insufficient`, because the voxel data are in the dandiset and only the labels are missing. The disagreement is recorded.

**Added or corrected, by verifier point**
- **fig2c, reading (b):** fixed the denominator, so 54.9% becomes 53.5%. A null with shifted behaviour gives 0.0% under both readings. The fig2c-venn reading (b) value moved with it (VF and turning 40.4% to 39.4%).
- **Clock check:** the null is now the largest |r| over the same 101 lags, so it is comparable with the observed peak. Its 99th percentile is at most 0.103, against observed peaks of 0.412 or more.
- **fig2-symmetry:**
  - Both turn directions are on the expected side in 6 of 9 flies, not 5 as the verifier counted (fly_097's left-turn difference is small but positive).
  - No fly appears flipped: every fly's maps correlate more with the pooled maps than with their mirror images (fly_105: 0.418 against 0.240).
  - I recorded that the 0.7 th
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/000727/*.yaml; grep -n "statement:" claims/000727/*.yaml | head -30
```

```
# Claims for Brezovec, Berger, Druckmann & Clandinin (2022) on dandiset 000727.
# Source: the full text of the bioRxiv preprint, version 1 (posted 21 March 2022, CC BY-NC-ND),
# read from its Results, figure legends and STAR Methods. It is the only version on bioRxiv.
#
# What the author had seen when these criteria were written. The data check: the file list,
# metadata, shapes, rates, units and FicTrac series of all nine files; the per-voxel means and
# spreads of the processed planes; the brain masks of each fly. Before that, the correlations of
# one fly's FDA plane 50 with VF, VL and VR, summed by image half (left turns on one half, right
# turns on the other), which identified the left-right axis. Then one prototype analysis, of
# the voxel correlations behind fig2c-fraction-correlated, fig2c-venn-categories and
# fig2-symmetry, on the 12 planes used here. With behaviour sampled at the midpoint of each
# volume (fixed in the helper module before this was run) 31.1% of in-brain voxels passed
# p < 1e-4, 11.9% forward only, 15.9% forward and turning, 3.2% turning only, all three 11.5% of
# the correlated voxels; with behaviour sampled at the start of each volume 39.2%, 11.6%, 24.1%,
# 3.5% and 25.8%. The forward map correlated with its mirror image at r = 0.82, the left and
# right maps with their own mirror images at 0.45 and 0.33. The volume midpoint stays the main
# choice, as decided before; the start of the volume is a variant. No other claim's analysis
# had been run.
#
# The dandiset holds, for each of the nine flies, the raw volumes, the processed GCaMP6f volumes
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000727, Brezovec et al. 2022

Eight claims reproduced, five partially, one not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it gave
partially reproduced for `fig5c-global-below-threshold`, as the pass under
one reading rests on r = 0.013 with a p-value that treats autocorrelated
samples as independent. The author kept reproduced and added a null of 200
rolls of each fly's behaviour in time, against which the weakest correlation
has p = 0.025 (null 95th percentile 0.010), and round 2 agreed. Round 1 would
also have blocked the four region-level claims as `data_missing`, the author
kept `metadata_insufficient`, as the voxel data are deposited and only their
labels are missing, and round 2 accepted it. Round 1 also found a wrong
denominator in reading (b) of `fig2c-fraction-correlated`, which moved 54.9%
to 53.5% and no outcome. Round 2 agreed with all 20 and nothing was proposed,
so there was no third round. The preprint reports that whole-brain imaging of
nine walking flies shows activity correlated with forward and turning
velocity across much of the brain, organized by neuropil and mirror-symmetric
for forward velocity, that linear models on the principal components predict
behaviour with weights stereotyped across flies, that turning raises activity
on one side and lowers it on the other, and that peak correlation times range
from leading to lagging behaviour, with lagging voxels broader in time. The
dataset structure, the share and tuning of correlated voxels, the symmetry,
the PC structure, the ridge R2 and its relation to movement, the weights, the
unique variance of forward velocity and walking state, the below-threshold
correlations of the demixed regions, the ipsilateral and contralateral
changes, the peak time range, lag against width and the ipsilateral lead were
tested on 12 of 91 planes with 6 x 6 voxel blocks in place of supervoxels.
The four region-level claims are blocked as `metadata_insufficient`, the
tdTomato control as `data_missing` and the supervoxel number sweep as
`too_large`. Some outcomes rest on weak ground: `fig6-peak-time-range` gives
0.32 s with behaviour at the volume midpoint, but 0.58 s at the volume start
and 0.50 s with each plane's median removed, so only the lag of more than 1 s
is robust; `fig5c-global-below-threshold` holds under reading (b) only, with a
left region of 4 blocks; and in `fig2-symmetry` a left-right flip of fly_105
is not excluded. The author used the full text of bioRxiv version 1, as the
Current Biology version is paywalled, and took parameters where the Methods
are silent from the paper's code at commit 8e2b275.

The dandiset was converted by CatalystNeuro (catalystneuro/clandinin-lab-to-nwb).
The processed volumes are registered into the Functional Drosophila Atlas, a
space from a later paper of the lab, while the preprint analyses its data in
its own mean brain, and the dandiset holds no neuropil labels, atlas or
template for that space, nor the paper's mean brain and registered atlas, so
none of the region-level results (Figures 2E to I, 3, 6E to G, 7) can be
tested; nor does it say how the FDA series relates to the preprint's analysis
space. The per-plane acquisition times are not in the files, which give only
a volume rate, and sampling behaviour at the start in place of the middle of
each volume changes the correlated share of the brain from 31.1% to 39.2% and
the 99th percentile of forward-velocity lead from 0.32 to 0.58 s. The
supervoxel labels, the z-depth maps and the motion-corrected tdTomato channel
are not deposited. The processed series has grid spacing 1, 1, 1 in unit
"unknown", and nothing states which half of the volume is the fly's left.
Imaging and FicTrac both start at 0 s, as the conversion code set FicTrac
timestamps to a uniform 50 Hz from 0 because synchronisation data were
missing, which the dandiset does not say; the data are consistent with a
shared start (brain-wide activity follows walking speed by 0.4 to 0.8 s in
every fly) to within a few hundred milliseconds. Every FicTrac SpatialSeries
has unit "meters" and conversion 0.0045 (the ball radius), while most hold
angles in radians, and SpatialSeriesRotationDeltaError, described as an error
in radians, has medians of 6067 to 10,435. Other findings: the paper's code
computes the walking state with np.sqrt(a, b), which reduces it to forward
velocity alone, and the two versions mark 47.2% and 57.3% of time points as
walking; the Methods cite Figure 3F and 3G for panels in Figure 4, and Figure
3G is the Nodulus in the Results and the Ellipsoid Body in the legend; and the
preprint says the data were deposited at Dryad, where no record was found,
while the dandiset links neither Dryad nor the analysis code, which was found
as ClandininLab/brezovec_volition_2023 under a different title.

The notebook ran in 483 s in the first clean run and in 12.3 minutes in the
latest run. h5py over the network read at 2.6 MB/s, so the helper reads the
gzip chunks by HTTP range requests at about 98 MB/s, matching h5py in all
nine files; bioRxiv rate-limited the downloads and after round 1 the paper
could not be fetched again, and the GitHub API reached its limit, so the
repositories were cloned with git. Round 2 found statements the outputs
contradicted (the README run time, the time to stream the 12 planes, and a
round-1 response saying the lag of more than 1 s held in every plane from 38)
and a flip check, the overlap of each brain mask with its mirror, that cannot
detect a flip; these were corrected and the check replaced with leave-one-out
maps. Untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: a paper that names no
code repository, with the code found by search under another title; outside
resources the dandiset's processed data depend on but the paper does not
use; no rule for testing on a sample of a dataset too large to stream; where
the data check ends when prototypes are needed to find the left-right axis; a
clock check that cannot resolve the sub-volume alignment some claims need;
no definition of partially reproduced for a single expected value; what to
record as measured when no reading matches; following code that tunes on test
data; and a default 10% tolerance, kept for "approximately 0.3", which is
strict.
EOF
grep -c "—\|rather" <(sed -n '/### 000727/,$p' docs/pilot-notes.md)
```

```
0
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "`data_missing`, the author\nkept",
 "new_string": "`data_missing`; the author\nkept"
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I ran `tools/readme_row.py 000727 --write`. It added the row `| 000727 | Brezovec et al. 2022 | 8 | 5 | 1 | 6 | 000727-brezovec-2022 |` to README.md. I then added the subsection below at the end of docs/pilot-notes.md. It has no em dashes and no "rather". The attempt, claims and entry are unchanged, and nothing is committed.

### 000727, Brezovec et al. 2022

Eight claims reproduced, five partially, one not reproduced and six blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it gave
partially reproduced for `fig5c-global-below-threshold`, as the pass under
one reading rests on r = 0.013 with a p-value that treats autocorrelated
samples as independent. The author kept reproduced and added a null of 200
rolls of each fly's behaviour in time, against which the weakest correlation
has p = 0.025 (null 95th percentile 0.010), and round 2 agreed. Round 1 would
also have blocked the four region-level claims as `data_missing`; the author
kept `metadata_insufficient`, as the voxel data are deposited and only their
labels are missing, and round 2 accepted it. Round 1 also found a wrong
denominator in reading (b) of `fig2c-fraction-correlated`, which moved 54.9%
to 53.5% and no outcome. Round 2 agreed with all 20 and nothing was proposed,
so there was no third round. The preprint reports that whole-brain imaging of
nine walking flies shows activity correlated with forward and turning
velocity across much of the brain, organized by neuropil and mirror-symmetric
for forward velocity, that linear models on the principal components predict
behaviour with weights stereotyped across flies, that turning raises activity
on one side and lowers it on the other, and that peak correlation times range
from leading to lagging behaviour, with lagging voxels broader in time. The
dataset structure, the share and tuning of correlated voxels, the symmetry,
the PC structure, the ridge R2 and its relation to movement, the weights, the
unique variance of forward velocity and walking state, the below-threshold
correlations of the demixed regions, the ipsilateral and contralateral
changes, the peak time range, lag against width and the ipsilateral lead were
tested on 12 of 91 planes with 6 x 6 voxel blocks in place of supervoxels.
The four region-level claims are blocked as `metadata_insufficient`, the
tdTomato control as `data_missing` and the supervoxel number sweep as
`too_large`. Some outcomes rest on weak ground: `fig6-peak-time-range` gives
0.32 s with behaviour at the volume midpoint, but 0.58 s at the volume start
and 0.50 s with each plane's median removed, so only the lag of more than 1 s
is robust; `fig5c-global-below-threshold` holds under reading (b) only, with a
left region of 4 blocks; and in `fig2-symmetry` a left-right flip of fly_105
is not excluded. The author used the full text of bioRxiv version 1, as the
Current Biology version is paywalled, and took parameters where the Methods
are silent from the paper's code at commit 8e2b275.

The dandiset was converted by CatalystNeuro (catalystneuro/clandinin-lab-to-nwb).
The processed volumes are registered into the Functional Drosophila Atlas, a
space from a later paper of the lab, while the preprint analyses its data in
its own mean brain, and the dandiset holds no neuropil labels, atlas or
template for that space, nor the paper's mean brain and registered atlas, so
none of the region-level results (Figures 2E to I, 3, 6E to G, 7) can be
tested; nor does it say how the FDA series relates to the preprint's analysis
space. The per-plane acquisition times are not in the files, which give only
a volume rate, and sampling behaviour at the start in place of the middle of
each volume changes the correlated share of the brain from 31.1% to 39.2% and
the 99th percentile of forward-velocity lead from 0.32 to 0.58 s. The
supervoxel labels, the z-depth maps and the motion-corrected tdTomato channel
are not deposited. The processed series has grid spacing 1, 1, 1 in unit
"unknown", and nothing states which half of the volume is the fly's left.
Imaging and FicTrac both start at 0 s, as the conversion code set FicTrac
timestamps to a uniform 50 Hz from 0 because synchronisation data were
missing, which the dandiset does not say; the data are consistent with a
shared start (brain-wide activity follows walking speed by 0.4 to 0.8 s in
every fly) to within a few hundred milliseconds. Every FicTrac SpatialSeries
has unit "meters" and conversion 0.0045 (the ball radius), while most hold
angles in radians, and SpatialSeriesRotationDeltaError, described as an error
in radians, has medians of 6067 to 10,435. Other findings: the paper's code
computes the walking state with np.sqrt(a, b), which reduces it to forward
velocity alone, and the two versions mark 47.2% and 57.3% of time points as
walking; the Methods cite Figure 3F and 3G for panels in Figure 4, and Figure
3G is the Nodulus in the Results and the Ellipsoid Body in the legend; and the
preprint says the data were deposited at Dryad, where no record was found,
while the dandiset links neither Dryad nor the analysis code, which was found
as ClandininLab/brezovec_volition_2023 under a different title.

The notebook ran in 483 s in the first clean run and in 12.3 minutes in the
latest run. h5py over the network read at 2.6 MB/s, so the helper reads the
gzip chunks by HTTP range requests at about 98 MB/s, matching h5py in all
nine files; bioRxiv rate-limited the downloads and after round 1 the paper
could not be fetched again, and the GitHub API reached its limit, so the
repositories were cloned with git. Round 2 found statements the outputs
contradicted (the README run time, the time to stream the 12 planes, and a
round-1 response saying the lag of more than 1 s held in every plane from 38)
and a flip check, the overlap of each brain mask with its mirror, that cannot
detect a flip; these were corrected and the check replaced with leave-one-out
maps. Untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: a paper that names no
code repository, with the code found by search under another title; outside
resources the dandiset's processed data depend on but the paper does not
use; no rule for testing on a sample of a dataset too large to stream; where
the data check ends when prototypes are needed to find the left-right axis; a
clock check that cannot resolve the sub-volume alignment some claims need;
no definition of partially reproduced for a single expected value; what to
record as measured when no reading matches; following code that tunes on test
data; and a default 10% tolerance, kept for "approximately 0.3", which is
strict.

## End of run

12 turns, 1 minutes, result: success.
