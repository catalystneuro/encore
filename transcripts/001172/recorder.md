# 001172 · recorder · run 39171549090

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001172 --write; git diff README.md; ls claims/001172 transcripts/001172; cat attempts/001172-lohani-2022-01.yaml; grep -n "^### " docs/pilot-notes.md | tail -6
```

```
<persisted-output>
Output too large (44.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0d42658b-bb8e-4a5f-b44f-6ad2903f89da/tool-results/b6bxndefy.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 0fffd8b..e419374 100644
--- a/README.md
+++ b/README.md
@@ -94,6 +94,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001075](https://dandiarchive.org/dandiset/001075) | [Randi et al. 2023](https://doi.org/10.1038/s41586-023-06683-4) | 4 | 4 (+1) | 0 (+1) | 7 | [`001075-randi-2023`](entries/001075-randi-2023) |
 | [001084](https://dandiarchive.org/dandiset/001084) | [Vu et al. 2024](https://doi.org/10.1016/j.neuron.2023.12.011) | 10 (+1) | 10 | 0 | 1 | [`001084-vu-2024`](entries/001084-vu-2024) |
 | [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
+| [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001172:
10.1038-s41593-022-01202-6.yaml

transcripts/001172:
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^| Dandiset\|^|---\|^| ---" README.md | head; cat attempts/001172-lohani-2022-01.yaml; grep -n "^### " docs/pilot-notes.md | tail -6
```

```
<persisted-output>
Output too large (43.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0d42658b-bb8e-4a5f-b44f-6ad2903f89da/tool-results/bah5caii9.txt

Preview (first 2KB):
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
schema_version: 1
id: 001172-lohani-2022-01
dandiset: "001172"
dandiset_version: 0.260129.0829
paper: doi:10.1038/s41593-022-01202-6
date: 2026-10-18
entry: 001172-lohani-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
[... 24 more lines not kept]
```

**Agent**

The attempt file is large; I'll read it directly.

**Agent calls Read**

```json
{
 "file_path": "attempts/001172-lohani-2022-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001172-lohani-2022-01
3	dandiset: "001172"
4	dandiset_version: 0.260129.0829
5	paper: doi:10.1038/s41593-022-01202-6
6	date: 2026-10-18
7	entry: 001172-lohani-2022
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The Allen parcel masks parcells_updated121519.mat and the brain mask brainMask.mat of the
18	    paper's code, which name the pixels of the dandiset's atlas-registered ΔF/F. The procedures
19	    (frame timing, locomotion change points, face normalisation, sustained states, onsets,
20	    cross-correlation and permutation statistics) follow the same code where the Methods are silent.
[... 745 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
it=d if isinstance(d,list) else d.values()
for e in it:
  if '001172' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (172.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0d42658b-bb8e-4a5f-b44f-6ad2903f89da/tool-results/bankt9954.txt

Preview (first 2KB):
3039:### 000947, Schwab et al. 2020
3132:### 000971, Seiler et al. 2022
3233:### 001038, Azcorra et al. 2023
3328:### 001075, Randi et al. 2023
3423:### 001084, Vu et al. 2024
3523:### 001170, Ling et al. 2023
3631 docs/pilot-notes.md
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d:
  if e['dandiset']=='001172': print(json.dumps(e,indent=1))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if e['dandiset']=='001172': print(json.dumps(e,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3233
}
```

```
3233	### 001038, Azcorra et al. 2023
3234	
3235	Sixteen claims reproduced, seven partially and one not reproduced on the
3236	dandiset, none blocked. Five claims on data in other archives: two
3237	reproduced, on the snRNA-seq count matrices in GEO (GSE222558), and three
3238	blocked. Round 1 gave its own outcome for each claim from the notebook with
3239	its conclusions removed and agreed with all 29, giving other reasons only for
3240	the three blocked claims; the author kept `not_runnable` for the two claims
3241	that need Seurat and LIGER in R and `other` for the histology claim, which
3242	rests on manual cell counts that are not deposited, as the images are public
3243	on Zenodo. After round 1, `fig5ab-transient-scaling` uses the recomputed onsets
3244	that are also stored, which carry the code's exclusion after every reward
3245	(241, 246 and 232% against 239, 266 and 222% before), and stays partially
3246	reproduced. Round 2 agreed with all 29 and nothing was proposed, so there was
3247	no third round. The paper reports that genetic subtypes of dopamine neurons
3248	signal differently: Vglut2 and Calb1 axons in striatum show transients after
3249	decelerations and respond to rewards and air puffs, Anxa1 axons show
3250	transients after accelerations, have almost no reward response and decrease
3251	to air puffs, the subtypes can be clustered from these responses, and somas in
3252	SNc track their axons. The recording counts, the cross-correlations with
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d['dandisets'] if isinstance(d,dict) and 'dandisets' in d else d
print(type(d), list(d)[:3] if isinstance(d,dict) else '')
it=d.values() if isinstance(d,dict) else d
for e in it:
  if isinstance(e,dict) and e.get('dandiset')=='001172': print(json.dumps(e,indent=1))
"; wc -w transcripts/001172/*report.md
```

```
<class 'dict'> ['schema_version', 'generated', 'source']
  771 transcripts/001172/author-report.md
  605 transcripts/001172/author-revise-1-report.md
  510 transcripts/001172/author-revise-2-report.md
  224 transcripts/001172/author-revise-3-report.md
 1750 transcripts/001172/verifier-1-report.md
 1037 transcripts/001172/verifier-2-report.md
  514 transcripts/001172/verifier-3-report.md
 5411 total
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(list(d))
for k,v in d.items():
  if isinstance(v,list):
    for e in v:
      if isinstance(e,dict) and e.get('dandiset')=='001172': print(json.dumps(e,indent=1))
"; cat transcripts/001172/author-report.md transcripts/001172/author-revise-1-report.md
```

```
['schema_version', 'generated', 'source', 'counts', 'targets']
{
 "dandiset": "001172",
 "name": "Dual-color mesoscopic imaging of both ACh and calcium across the neocortex of awake mice.",
 "published_version": "0.260129.0829",
 "asset_count": 32,
 "size_gb": 700.01,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "microscopy approach; cell population imaging",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1038/s41593-022-01202-6",
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001172; cat author-revise-2-report.md author-revise-3-report.md verifier-3-report.md; head -c 5000 verifier-1-report.md; echo ----; head -c 4000 verifier-2-report.md
```

```
No outcome changed in this round. I'm proposing one change, for fig2c-face-best-predictor-calcium, which a third round needs to review. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 17.1 min), and the numbers came out the same in both runs.

**Proposed change of outcome**
- **fig2c-face-best-predictor-calcium:** the record keeps `partially_reproduced` and proposes `reproduced`. The verifier was right that the paper's speed is signed. The Methods define it as "a differential of distance", and the code's `wheel_changepoints.m` keeps the sign. My switch to |speed| after round 1 was a mistake.
  - The main regression now uses the signed WheelSpeed, and |speed| is a variant.
  - With signed speed, face PC1 is the best single variable in all 4 mice (Friedman p = 0.018). Its unique contribution is also the largest in all 4, though in grabAM05 only by 0.002 over pupil.

**Comparison with the paper's own values**
- I added a check against `Fig2RawData.mat` from the paper's code repository, with a small loader in `meso.py`. Rows are matched to mice by comparing full-model R² across the 23 left parcels.
- Rows 1, 3 and 4 match grabAM05, grabAM07 and grabAM08 closely (Spearman 0.94 to 0.98 for both signals). grabAM06 has no clear row.
- For those three mice, our mean full-model R² is close to the paper's. This is the first outside check of the ridge regression port.
- grabAM05 is the one mouse where the two speed readings differ clearly, and it matches signed speed: calcium wheel R² is 0.0246 in the paper's file, 0.0253 here with signed speed and 0.0483 with |speed|. grabAM07 and grabAM08 don't favour either reading.

**Corrected text**
- **Robustness without grabAM06:** the conclusion, summary and record now say:
  - calcium locomotion above high face stays significant (p = 0.019);
  - the calcium sustained-state gradient becomes significant (p = 0.037). With 2 mice that would meet the calcium half of the s7-ap-gradient-sustained
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/001172/*.yaml; grep -n "^  statement\|^- id\|^  - id" claims/001172/*.yaml | head -60
```

```
# Claims for Lohani, Moberly et al. (2022) on dandiset 001172.
# Source: the accepted author manuscript in PubMed Central (PMC10661869), full text, read from its
# Results, figure legends and Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only, run outside the
# notebook while preparing: the file list, the metadata and every dataset of the files, the frame
# counts of all 16 sessions, the stimulus and air-puff tables, the match of the ΔF/F brain mask to
# the paper code's brainMask.mat (rotated by 180 degrees), and, on one session (grabAM05,
# 11222019 spont), the frame offset between raw and ΔF/F movies (499 frames), the lag between
# wheel speed and the calcium signal under the files' timing (499 frames), the lag between
# FaceMap PC1 and wheel speed under the files' timestamps and under the camera pulses, and the
# identity of the parcellated series (calcium, 150 frames later than the ΔF/F). No claim's
# analysis had been run.
#
# The author also read the paper's code (github.com/cardin-higley-lab/Lohani_Moberly_et_al_2022,
# commit c337686fb3776112f1609ec1a19256d277c930fd) and the conversion code
# (github.com/catalystneuro/higley-lab-to-nwb, commit 20c40d39412e7c94219438f33cae52a765ba3d87).
#
# The dandiset holds 4 of the paper's 6 ACh3.0 and jRCaMP1b mice (grabAM05 to grabAM08; the code
# lists grabAM05 to grabAM10), with spontaneous, air-puff and visual stimulus sessions. It holds
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001172, Lohani et al. 2022

Thirteen claims reproduced, seven partially, one not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 26, but noted that
the wheel predictor of the Figure 2 regressions was signed speed while the
paper says locomotion speed. The author then made |speed| the main predictor,
under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
agreed with 25 of the 26 and disputed that reason: the Methods define speed as
a differential of distance, which keeps the sign, and the paper's
`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
signed speed, added a comparison with the paper's own per-mouse R2 values in
`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
proposed reproduced. A third round reviewed only that proposal and agreed, and
the claim is reproduced. The paper images ACh (ACh3.0) and calcium (jRCaMP1b)
together across the dorsal neocortex of awake mice, and reports that facial
movement and locomotion relate to both signals with opposite
anterior-posterior gradients, that transients and sustained states differ
across areas, and that correlations between areas and the coupling of ACh and
calcium change with behavioural state. The link to the paper's Allen parcel
masks, the regressions of Figure 2, the transients at face and locomotion
onsets, the sustained states, the correlations between areas and the
ACh-calcium coupling were tested. The ECoG, scopolamine, hemodynamic
correction, sensor validation and cholinergic axon claims are blocked as
`data_missing`. `fig5-coupling-down-frontal-with-locomotion` is not
reproduced: coupling is lower with locomotion in all 23 parcels but no parcel
decreases significantly at q = 0.01, and the largest decreases are in PTLp and
SSp-tr, not frontal cortex. Some outcomes rest on weak ground:
`allen-parcel-link` is partially reproduced under a per-session reading of its
mask criterion chosen after one movie was seen to fail it per movie (0.996
against 0.999), which would make it not reproduced; the claims of Figures 3 to
5 rest on 3 mice, and without grabAM06, which contributes 2 epochs per state,
the LSD p of `fig3c-ach-sustained-face` is 0.207 and the paired t p of
`fig3d-ach-frontal-above-visual` is 0.247; `fig3c-ach-locomotion-no-further-increase`
is an absence result where locomotion exceeds high face in all 3 mice; and
the ACh mean of `s7-face-onset-transients` is inside tolerance by 0.002. The
author used the author manuscript in PubMed Central (PMC10661869) and took the
parcel masks and the procedures the Methods leave open from the paper's code
at commit c337686.

The dandiset was converted by CatalystNeuro (catalystneuro/higley-lab-to-nwb).
It holds 4 of the 6 ACh3.0 and jRCaMP1b mice of the paper's code (grabAM05 to
grabAM08) and no ECoG, drug sessions, control mice or ChAT-GCaMP6s mice, so
five of the paper's findings cannot be tested. The ΔF/F series are given the
starting time of raw frame 0 while their frame 0 is raw frame 499, so their
times are 49.9 s early in every session. The FaceMap, pupil, eye and video
timestamps are spaced 111 ms where the camera pulses are 100 ms apart, span
about 10% longer than the session and end with two values equal to the first
camera pulse; with them face movement and wheel speed are misaligned by 23 to
60 s, and with frame i at camera pulse i, as the paper's code does, they
align. RoiResponseSeriesParcellated holds the calcium ΔF/F but its
segmentation is linked to the ACh imaging plane, its image masks are
transposed relative to the ΔF/F images, and its starting time is 64.9 s before
its first frame. The ΔF/F descriptions mention detrending only, while the blue
and green ΔF/F are also hemodynamically corrected and registered to the Allen
atlas, rotated by 180 degrees; the Allen parcels the paper analyses are not in
the files, and the parcellation that is there is a functional one with 89 to
107 ROIs per session and no area names. Other findings: in the VisualStimulus
tables the columns from `stimulus_size` on are shifted by one, and the tables
do not say where the monitor stood relative to the mouse; the air-puff session
grabAM07 11262019 has no Airpuff table, and no puff in the other tables (29
puffs) is followed by a locomotion onset within 5 s, which fits the code
keeping only puffs without running, a selection the files do not state;
WheelSpeed and pupil_area have the unit "unknown", and WheelSpeed is signed,
which its description does not say; and in the calcium ΔF/F of grabAM08
11232019 spont 263 pixels inside the brain mask, all in the right AUD parcel,
are zero in every frame.

The notebook ran in 716 s in the first clean run, 12.1 minutes after round 1,
17.1 minutes after round 2 and 1047 s after round 3. One development run
failed because the helper module was missing from the scratch directory, and a
request to delete an empty harness directory in the entry was denied. Round 2
also found statements the outputs did not support, among them that the tests
across mice lose significance without grabAM06, where calcium locomotion above
high face stays at p = 0.019 and the calcium sustained-state gradient becomes
significant (p = 0.037), a runtime of 13 minutes and a data size of 110 GB,
and these were corrected or removed. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a link criterion found ambiguous after the analysis, with no rule
for a link claim that fails on one movie when 21 claims depend on it; parcel
masks that name pixels but bring no measurements, which `with_labels` does not
exactly cover; paired tests that cannot reach p < 0.05 with 4 mice; the
paper's uncertainty given as mean ± SEM; no rule for leaving out a session
whose event table is missing or for how few mice is too few; no rule for whose
timing convention to use once the file times are shown wrong; and a 10-minute
runtime aim the streamed data volume rules out.
EOF
git status --short
```

```
M README.md
 M docs/pilot-notes.md
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
```

**Agent calls Bash**

```bash
sed -n 79,82p claims/001172/*.yaml; sed -i 's/exactly cover; paired tests that cannot reach/exactly cover; signed-rank tests that cannot reach/' docs/pilot-notes.md; grep -c "signed-rank tests that cannot" docs/pilot-notes.md; grep -n "—\|rather" <(tail -95 docs/pilot-notes.md)
```

```
statement: The coupling of behaviour to fluorescence has anterior-posterior gradients that are
    inverted between the signals, with ACh most strongly linked to behaviour in frontal areas and
    calcium in posterior areas.
  source: Results, Calcium and cholinergic signals encode behavioral state; Figure 2b
1
```

**Agent**

I ran `python tools/readme_row.py 001172 --write`. It added the row to README.md: 13 reproduced, 7 partially, 1 not reproduced, 5 blocked. I then appended the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed. The repository root has untracked files I didn't create, such as `.bashrc`, `.idea` and `scripts`, and I left them alone.

Two judgement calls:
- The last five subsections all end with a paragraph on run times and failed steps before the protocol points. I followed that shape, so the run times and the denied directory deletion are in the last paragraph.
- In the protocol sentence I left out the author's figure of about 85 GB streamed. The author later dropped a similar size (110 GB) because no output supported it.

### 001172, Lohani et al. 2022

Thirteen claims reproduced, seven partially, one not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 26, but noted that
the wheel predictor of the Figure 2 regressions was signed speed while the
paper says locomotion speed. The author then made |speed| the main predictor,
under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
agreed with 25 of the 26 and disputed that reason: the Methods define speed as
a differential of distance, which keeps the sign, and the paper's
`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
signed speed, added a comparison with the paper's own per-mouse R2 values in
`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
proposed reproduced. A third round reviewed only that proposal and agreed, and
the claim is reproduced. The paper images ACh (ACh3.0) and calcium (jRCaMP1b)
together across the dorsal neocortex of awake mice, and reports that facial
movement and locomotion relate to both signals with opposite
anterior-posterior gradients, that transients and sustained states differ
across areas, and that correlations between areas and the coupling of ACh and
calcium change with behavioural state. The link to the paper's Allen parcel
masks, the regressions of Figure 2, the transients at face and locomotion
onsets, the sustained states, the correlations between areas and the
ACh-calcium coupling were tested. The ECoG, scopolamine, hemodynamic
correction, sensor validation and cholinergic axon claims are blocked as
`data_missing`. `fig5-coupling-down-frontal-with-locomotion` is not
reproduced: coupling is lower with locomotion in all 23 parcels but no parcel
decreases significantly at q = 0.01, and the largest decreases are in PTLp and
SSp-tr, not frontal cortex. Some outcomes rest on weak ground:
`allen-parcel-link` is partially reproduced under a per-session reading of its
mask criterion chosen after one movie was seen to fail it per movie (0.996
against 0.999), which would make it not reproduced; the claims of Figures 3 to
5 rest on 3 mice, and without grabAM06, which contributes 2 epochs per state,
the LSD p of `fig3c-ach-sustained-face` is 0.207 and the paired t p of
`fig3d-ach-frontal-above-visual` is 0.247; `fig3c-ach-locomotion-no-further-increase`
is an absence result where locomotion exceeds high face in all 3 mice; and
the ACh mean of `s7-face-onset-transients` is inside tolerance by 0.002. The
author used the author manuscript in PubMed Central (PMC10661869) and took the
parcel masks and the procedures the Methods leave open from the paper's code
at commit c337686.

The dandiset was converted by CatalystNeuro (catalystneuro/higley-lab-to-nwb).
It holds 4 of the 6 ACh3.0 and jRCaMP1b mice of the paper's code (grabAM05 to
grabAM08) and no ECoG, drug sessions, control mice or ChAT-GCaMP6s mice, so
five of the paper's findings cannot be tested. The ΔF/F series are given the
starting time of raw frame 0 while their frame 0 is raw frame 499, so their
times are 49.9 s early in every session. The FaceMap, pupil, eye and video
timestamps are spaced 111 ms where the camera pulses are 100 ms apart, span
about 10% longer than the session and end with two values equal to the first
camera pulse; with them face movement and wheel speed are misaligned by 23 to
60 s, and with frame i at camera pulse i, as the paper's code does, they
align. RoiResponseSeriesParcellated holds the calcium ΔF/F but its
segmentation is linked to the ACh imaging plane, its image masks are
transposed relative to the ΔF/F images, and its starting time is 64.9 s before
its first frame. The ΔF/F descriptions mention detrending only, while the blue
and green ΔF/F are also hemodynamically corrected and registered to the Allen
atlas, rotated by 180 degrees; the Allen parcels the paper analyses are not in
the files, and the parcellation that is there is a functional one with 89 to
107 ROIs per session and no area names. Other findings: in the VisualStimulus
tables the columns from `stimulus_size` on are shifted by one, and the tables
do not say where the monitor stood relative to the mouse; the air-puff session
grabAM07 11262019 has no Airpuff table, and no puff in the other tables (29
puffs) is followed by a locomotion onset within 5 s, which fits the code
keeping only puffs without running, a selection the files do not state;
WheelSpeed and pupil_area have the unit "unknown", and WheelSpeed is signed,
which its description does not say; and in the calcium ΔF/F of grabAM08
11232019 spont 263 pixels inside the brain mask, all in the right AUD parcel,
are zero in every frame.

The notebook ran in 716 s in the first clean run, 12.1 minutes after round 1,
17.1 minutes after round 2 and 1047 s after round 3. One development run
failed because the helper module was missing from the scratch directory, and a
request to delete an empty harness directory in the entry was denied. Round 2
also found statements the outputs did not support, among them that the tests
across mice lose significance without grabAM06, where calcium locomotion above
high face stays at p = 0.019 and the calcium sustained-state gradient becomes
significant (p = 0.037), a runtime of 13 minutes and a data size of 110 GB,
and these were corrected or removed. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a link criterion found ambiguous after the analysis, with no rule
for a link claim that fails on one movie when 21 claims depend on it; parcel
masks that name pixels but bring no measurements, which `with_labels` does not
exactly cover; signed-rank tests that cannot reach p < 0.05 with 4 mice; the
paper's uncertainty given as mean ± SEM; no rule for leaving out a session
whose event table is missing or for how few mice is too few; no rule for whose
timing convention to use once the file times are shown wrong; and a 10-minute
runtime aim the streamed data volume rules out.

## End of run

13 turns, 1 minutes, result: success.
