# 001754 · verifier-1 · run 39492165452

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 280
drwxr-xr-x 6 runner runner    4096 Oct 20 20:30 .
drwxr-xr-x 7 runner runner    4096 Oct 20 20:30 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 20 20:27 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 20 20:27 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 20 20:30 .claude
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.development
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.local
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.production
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.test
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .env.test.local
drwx------ 2 runner runner      40 Oct 20 20:30 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 20 20:27 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 20 20:27 .github
-rw-r--r-- 1 runner runner       0 Oct 20 20:30 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 20 20:27 .idea
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-72910.yaml"
}
```

```
1	# Claims for Knierim, McNaughton & Poe (2000) on dandiset 001754.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, as
3	# the reader of docs/protocol.md (version pilot-10, Reader, steps 1 to 4). The reader has not
4	# seen the dandiset's data; it read only its title and description on the archive.
5	#
6	# Text read. The version of record (Nature Neuroscience 3(3), 211-212), from a PDF supplied by a
7	# person, as extracted to paper/10.1038-72910.txt. It is a two-page brief communication. It has
8	# no separate Methods section and no supplement; its methods are stated in the main text and the
9	# figure legends, and the spatial information measure is cited to Skaggs et al. 1996 (its ref.
10	# 13). The paper links no code. Its acknowledgements credit analysis software written by
11	# W. Skaggs and M. Wilson, which is not published with the paper and was not read. The
12	# dandiset's conversion code (catalystneuro/mcnaughton2000-to-nwb) is not the paper's code and
13	# fixes no method here. The paper has no section headings, so sources name a body paragraph by
14	# its opening words; the unheaded first paragraph is called the standfirst.
15	#
16	# Data the paper used, as it reports them. Three rats (rats 1, 2 and 3) implanted with a
17	# multi-electrode recording array (refs. 11, 12), recorded during the Neurolab Space Shuttle
18	# mission (STS-90, April 1998). In flight the rats ran a three-dimensional track, the Escher
19	# staircase (three 90 degree yaw turns interleaved with three 90 degree pitch turns), for medial
20	# forebrain bundle stimulation as reward, mostly clockwise with short counterclockwise runs.
[... 328 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "neurolab.py"
}
```

```
1	"""Loading and spatial measures for the Neurolab (STS-90) place cell data of dandiset 001754.
2	
3	Knierim, McNaughton & Poe (2000), Nature Neuroscience 3(3):211-212, doi:10.1038/72910.
4	
5	Each NWB file of the pinned version holds one rat on one day (preflight, flight day 4 or flight
6	day 9): sorted units (spike times in seconds, tetrode and Xclust cluster id), task epochs (BL
7	baseline, ES Escher staircase, MC Magic Carpet), and a table of 64 x 64 rate and occupancy maps
8	from the original analysis (one row per .RMA file, with its task type, tetrode, 8.3 short file
9	name and a `cell_number` read from that name). The flight files also hold the video position in
10	pixels (0 to 255), but only at the spike times of the file's units. Files are streamed from the
11	archive at the pinned version; nothing is written to disk.
12	
13	Where the parameters come from.
14	
15	- `ACTIVE_HZ = 0.05`: active cells have a mean firing rate above 0.05 Hz on the track (the
16	  paper's main text, as the claims file's criteria give it).
17	- `ALPHA = 0.05`, two-sided: the level of the Mann-Whitney tests, which the paper does not print;
18	  the claims file reads it as two-sided p < 0.05.
19	- Spatial information is Skaggs' information per spike, I = sum_i p_i (r_i / r) log2(r_i / r)
20	  (the claims file, after the paper's ref. 13), over every visited bin, off-track positions kept
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_knierim_2000.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--out--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--out--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (137.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/5ca1b978-f532-4673-8260-ae3adea39507/tool-results/bjquzg6dw.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Knierim, McNaughton & Poe (2000) from dandiset 001754

Paper. Knierim JJ, McNaughton BL, Poe GR (2000). Three-dimensional spatial selectivity of
hippocampal neurons during space flight. *Nature Neuroscience* 3(3):211-212.
[doi:10.1038/72910](https://doi.org/10.1038/72910). The claims file,
`claims/001754/10.1038-72910.yaml`, was written from the full text of the version of record, a
two-page brief communication with no separate Methods section and no supplement; its methods are
in the main text and the figure legends. The paper links no code.

Dandiset. [DANDI:001754](https://dandiarchive.org/dandiset/001754/0.260728.1352), version
0.260728.1352 (doi:10.48324/dandi.001754/0.260728.1352). Why this version: the paper cites no
version of the dandiset, so the most recent published version is pinned, and 0.260728.1352 is it.
The two earlier published versions (0.260227.0029 and 0.260227.0031) hold the same files with the
same blobs (data check), so none of them matches the claims file better. The draft holds a new
conversion that addresses the findings of the first attempt, but it is not published, and it has
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/5ca1b978-f532-4673-8260-ae3adea39507/tool-results/bjquzg6dw.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Knierim, McNaughton & Poe (2000) from dandiset 001754
3	
4	Paper. Knierim JJ, McNaughton BL, Poe GR (2000). Three-dimensional spatial selectivity of
5	hippocampal neurons during space flight. *Nature Neuroscience* 3(3):211-212.
6	[doi:10.1038/72910](https://doi.org/10.1038/72910). The claims file,
7	`claims/001754/10.1038-72910.yaml`, was written from the full text of the version of record, a
8	two-page brief communication with no separate Methods section and no supplement; its methods are
9	in the main text and the figure legends. The paper links no code.
10	
11	Dandiset. [DANDI:001754](https://dandiarchive.org/dandiset/001754/0.260728.1352), version
12	0.260728.1352 (doi:10.48324/dandi.001754/0.260728.1352). Why this version: the paper cites no
13	version of the dandiset, so the most recent published version is pinned, and 0.260728.1352 is it.
14	The two earlier published versions (0.260227.0029 and 0.260227.0031) hold the same files with the
15	same blobs (data check), so none of them matches the claims file better. The draft holds a new
16	conversion that addresses the findings of the first attempt, but it is not published, and it has
17	changed since `001754-knierim-2000-02` read it (the data check prints when it was last
18	modified), so it is not used. This is the version that `001754-knierim-2000-01` read;
19	`001754-knierim-2000-02` read the draft.
20	
[... 712 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/5ca1b978-f532-4673-8260-ae3adea39507/tool-results/bjquzg6dw.txt",
 "offset": 733,
 "limit": 700
}
```

```
733	  timestamps_reference_time  ()  object  
734	  units/  group  Units
735	  units/cluster_id  (47,)  int64  Cluster ID from Xclust sorting
736	  units/electrodes  (188,)  int64  the electrodes that each spike unit came from
737	  units/electrodes_index  (47,)  uint8  Index for VectorData 'electrodes'
738	  units/id  (47,)  int64  
739	  units/spike_times  (58717,)  float64  the spike times for each unit in seconds
740	  units/spike_times_index  (47,)  uint16  Index for VectorData 'spike_times'
741	  units/tetrode  (47,)  object  Tetrode name (e.g. TT0)
742	
743	Neurodata types of groups, and the number of files holding each: {'Device': 8, 'DynamicTable': 8, 'ElectrodeGroup': 8, 'ElectrodesTable': 8, 'Position': 5, 'ProcessingModule': 8, 'SpatialSeries': 5, 'Subject': 8, 'TimeIntervals': 8, 'Units': 8}
744	
745	==================== 4 markdown
746	The three published versions hold the same eight files with the same blobs; every file of the draft
747	is a different blob, and the draft's description has been rewritten (the sentences printed above:
748	it no longer places the preflight recordings on a flat rectangular track, and it says the EEG is
749	not included). Those changes are in the draft only; the pinned version keeps the description
750	printed above. The listing shows every group and dataset of every file. The neurodata types are
751	only those printed under it: there is no ElectricalSeries or LFP, so no file holds EEG or any
752	continuous voltage. The units table has `tetrode`, `cluster_id`, `spike_times` and `electrodes`;
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/5ca1b978-f532-4673-8260-ae3adea39507/tool-results/bjquzg6dw.txt",
 "offset": 1433,
 "limit": 700
}
```

```
1433	print("\nReading M-b, active units per flight epoch: spikes, spikes dropped at the lost position or with no sample, spikes in unvisited bins:")
1434	print(pd.DataFrame([{"rat": k[0], "day": k[1], "epoch": k[2], "active": int(d.active.sum()), "spikes": int(d[d.active].spikes.sum()),
1435	                     "dropped_lost_or_no_sample": int(d[d.active].spikes_lost_position.sum()), "in_unvisited_bins": int(d[d.active].spikes_unvisited_bin.sum()),
1436	                     "info_range": f"{d[d.active]['info'].min():.3f}-{d[d.active]['info'].max():.3f}"} for k, d in mb.items()]).to_string(index=False))
1437	print("The preflight files hold no position, so M-b cannot be computed for any preflight cell.")
1438	
1439	def ma_values(rat, day, epoch):
1440	    return active_ma[(active_ma.rat == rat) & (active_ma.day == day) & (active_ma.epoch == epoch)]["info"].values
1441	
1442	def mb_values(rat, day, epoch):
1443	    d = mb[(rat, day, epoch)]
1444	    return d[d.active]["info"].dropna().values
1445	
1446	def readings(rat, day, epoch):
1447	    """Every reading of a flight-against-preflight comparison: M-a on both sides with each preflight
1448	    epoch (each is a candidate under S-a and, as the one preflight day is the closest before launch,
1449	    under S-b), and as variants M-b flight values against M-a preflight values."""
1450	    rows = []
1451	    for pre in ["ES1", "MC1"]:
1452	        rows.append({"reading": f"M-a, preflight {pre} (S-a, S-b)"} | nl.compare(ma_values(rat, day, epoch), ma_values(rat, "preflight", pre)))
[... 648 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -w paper/10.1038-72910.txt; cat paper/10.1038-72910.txt | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -A8 "Fig. 2\.\|Fig. 3\.\|seven\|fourth" paper/10.1038-72910.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://api.dandiarchive.org/api/dandisets/001754/versions/0.260728.1352; curl -s "$B/" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for k in ['variableMeasured','measurementTechnique','assetsSummary','description']:
    print(k, json.dumps(d.get(k))[:1500])
"; curl -s "$B/assets/?page_size=100" | python3 -c "
import json,sys;d=json.load(sys.stdin)
print(d['count'])
for a in d['results']: print(a['path'],a['size'],a['asset_id'])
" > assets.txt; cat assets.txt
```

```
variableMeasured null
measurementTechnique null
assetsSummary {"species": [{"name": "Rattus norvegicus - Norway rat", "schemaKey": "SpeciesType", "identifier": "http://purl.obolibrary.org/obo/NCBITaxon_10116"}], "approach": [{"name": "electrophysiological approach", "schemaKey": "ApproachType"}, {"name": "behavioral approach", "schemaKey": "ApproachType"}], "schemaKey": "AssetsSummary", "dataStandard": [{"name": "Neurodata Without Borders (NWB)", "schemaKey": "StandardsType", "identifier": "RRID:SCR_015242"}], "numberOfBytes": 32448840, "numberOfFiles": 8, "numberOfSubjects": 3, "variableMeasured": ["Units", "ProcessingModule", "ElectrodeGroup", "SpatialSeries", "Position"], "measurementTechnique": [{"name": "analytical technique", "schemaKey": "MeasurementTechniqueType"}, {"name": "surgical technique", "schemaKey": "MeasurementTechniqueType"}, {"name": "spike sorting technique", "schemaKey": "MeasurementTechniqueType"}, {"name": "behavioral technique", "schemaKey": "MeasurementTechniqueType"}]}
description "This dataset contains extracellular recordings from hippocampal place cells in three freely moving rats during the Neurolab Space Shuttle mission (STS-90) in April 1998. The experiment investigated whether the hippocampus can maintain stable spatial representations during three-dimensional navigation in microgravity. Rats were implanted with multi-electrode recording arrays and trained to traverse a three-dimensional track called the \"Escher staircase,\" in which three 90-degree yaw turns were interleaved with three 90-degree pitch turns, creating a closed loop after only 270 degrees of total yaw rotation. This design placed the spatial information from external landmarks in conflict with the expected input from the head-direction system, which normally requires 360 degrees of yaw to signal a return to the starting direction. The dataset includes both preflight recordings on a flat rectangular track and in-flight recordings on the Escher staircase track from fl
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
B=https://api.dandiarchive.org/api/dandisets/001754/versions/0.260728.1352; for id in a670099d-c635-46b0-a02d-c51a89f9ad91 b8dbee0b-e84e-45f9-998d-39bee1803fc9; do curl -s "$B/assets/$id/" | python3 -c "
import json,sys;d=json.load(sys.stdin)
print(d.get('path'), [v.get('value') for v in d.get('variableMeasured',[])], d.get('wasGeneratedBy',[{}])[0].get('description','')[:300])"; done
```

```
sub-Rat3/sub-Rat3_ses-19980420T152800_behavior+ecephys.nwb ['Units', 'ElectrodeGroup', 'SpatialSeries', 'ProcessingModule', 'Position'] Flight Day 4 recording — Rat 3. Separate recording session; partial data recovered due to technical issues.
sub-Rat1/sub-Rat1_ses-19980425T124500_behavior+ecephys.nwb ['Units', 'ElectrodeGroup', 'SpatialSeries', 'ProcessingModule', 'Position'] Flight Day 9 recording — Rat 1. Escher Staircase and Magic Carpet tasks with baseline sessions.
```

**Agent**

The archive confirms no EEG in any file. Next I'm testing the fig3 M-a pairing check on synthetic input. I suspect it cannot detect a map that two units both match best.

**Agent calls Bash**

```bash
python3 -c "
# Replicates cell 37's owner/pairing_ok logic. Units u1,u2 both best-match map 'm1' in S2; u3 best-matches 'm2'.
best_s2={'u1':('m1',0.9),'u2':('m1',0.8),'u3':('m2',0.7)}
best_s3={'u1':'n1','u2':'n2','u3':'n3'}
owner={}
for u,(i,r) in best_s2.items():
    if i not in owner or r>owner[i][1]: owner[i]=(u,r)
cells_a=['m1','m2']
units=[owner[i][0] for i in cells_a if i in owner]
maps3=[best_s3[u] for u in units]
print('owner',owner,'pairing_ok',len(units)==len(cells_a) and len(set(units))==len(units) and len(set(maps3))==len(maps3))
"
```

```
owner {'m1': ('u1', 0.9), 'm2': ('u3', 0.7)} pairing_ok True
```

**Agent**

## Verifier report, round 1: Knierim, McNaughton & Poe (2000), dandiset 001754 @ 0.260728.1352

The claims file has 10 claims. The notebook judges six against the data and blocks four.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| si-comparable-to-preflight | partially_reproduced | Cell 25: under M-a, neither preflight epoch shows a difference (p 0.88 and 0.66). Flight mean is 1.377 against 1.13 ± 0.09; preflight is 1.320 and 1.284 against 1.12 ± 0.08, so no reading puts both means within tolerance. M-b cannot be run on both sides (no preflight position), so as the criterion says it is not judged. |
| si-rat1-fd9-vs-preflight | blocked (methods_underspecified) | Cell 27: the readings disagree. Against preflight ES1 p = 0.50; against preflight MC1 p = 0.0055, with flight higher. Under S-a both preflight epochs are candidates, so the criterion blocks the claim. |
| si-rat3-fd4-vs-preflight | reproduced | Cell 29: no difference under either reading (p 0.28 and 0.77). With the ES1 preflight reading both means are within tolerance (1.231 against 1.12 ± 0.27; 1.518 against 1.48 ± 0.11). Cell counts are well off (11 flight against 7; 38 against 24), but the criterion's rule does not use counts. |
| flight-spatial-code | blocked (methods_underspecified) | Cell 32: the dependencies are partial, blocked and reproduced. If rat 1 were reproduced or partial the outcome would be partial; if not reproduced, not_reproduced. The others do not decide it, so the criterion blocks it. |
| fd4-abnormal-selectivity | partially_reproduced | Cell 34: Rat 2's FD4 information is significantly lower than preflight under both readings (p 0.0006 and 0.0015). Rat 1's is lower under neither (p 0.077 and 0.36). The rule gives "holds for one rat". This rests entirely on Rat 2's FD4 maps; see B2. |
| fig3-stability-across-sessions | blocked (methods_underspecified), possibly not_reproduced | Cell 36: under M-b, (a) 6 of 16 and (b) 1 of 16 cells keep their field. Cell 37: under M-a, (a) 6 of 11 (more than half) and (b) 5 of 11. The readings disagree only because M-a was admitted. The check that admits M-a does not test the criterion's condition (B1). If the condition fails, M-a is not run and the outcome is not_reproduced. |
| direction-selectivity | blocked (methods_underspecified) | Cell 39: position exists only at spike times (gaps up to 12.7 s), there is one occupancy map per epoch with no direction, and no file gives the track layout. The criterion blocks the claim when these are missing. In substance this is missing data, but the criterion fixes the label. |
| theta-normal | blocked (data_missing) | No ElectricalSeries or LFP in any file (cell 3). I confirmed this on the archive: every asset's `variableMeasured` is Units, ElectrodeGroup, SpatialSeries, ProcessingModule and Position, and the dandiset totals 32 MB in 8 files. No part can be tested. |
| ripples-normal | blocked (data_missing) | Same as theta-normal: there is no pouch or baseline EEG in the archive. No part can be tested. |
| three-orthogonal-surfaces | blocked (methods_underspecified) | Part (i) depends on two blocked claims, and the possible outcomes are not_reproduced or partially_reproduced, so the claim is undecided. Part (ii) cannot be tested at all: the position is one 2-D pixel frame with no track outline. If fig3 turns out not_reproduced (B1), this claim becomes not_reproduced. |

### B. Problems

1. **[affects a conclusion]** Cell 37, `owner` / `pairing_ok`: the check does not test the criterion's condition. The criterion admits M-a only when each map is tied to one unit and no unit to two maps.
   - The code pairs each unit with its best-matching map, and when two units pick the same map it silently keeps the higher match. That conflict is exactly what the condition is meant to catch.
   - The check is also never applied to the session 3 maps across all units.
   - I replicated the logic on a synthetic case where two units share a best map: `pairing_ok` comes out True.
   - The risk is real here: 47 units compete for 19 ES1 maps, and TT8 has at least 5 units for 3 to 4 maps.
   - Which way this goes decides whether fig3 is blocked or not_reproduced, and so the outcome of three-orthogonal-surfaces too.
2. **[affects a conclusion]** Cells 19–20 and 34: the notebook's own time-shift check finds no sign that the position trace in Rat 2's FD4 ES window is Rat 2's (0 of 17 units; 1 of 17 for Rat 1). The deposited maps came from the same shared tracker. So the low FD4 information for Rat 2, the only support for fd4-abnormal-selectivity, may come from tracking rather than firing. The notebook notes this caveat but still judges the claim.
3. **[affects a conclusion, unverified]** `ma_table`: M-a counts every deposited map as a cell, including maps with `cell_number` −1, which the table describes as "not a per-cell map" (14 to 33 per file outside Rat3 FD4). Their file names are printed only for Rat3 FD4 ES. If some are combined or multi-unit maps, they shift the counts and means in every spatial information comparison. Counts are off throughout (Rat3 preflight 38 against 24; Rat3 FD4 11 against 7), which is consistent with selection differing from the paper's.
4. **[does not affect a conclusion]** `mb_maps`: spikes that fall in bins with zero deposited occupancy (33 to 1,188 per epoch) are silently dropped. M-b is only a variant for the spatial information claims, and fig3 under M-b fails by a wide margin either way.
5. **[does not affect a conclusion]** Cell 36: M-b maps are unsmoothed at 4 px with very few spikes per bin, so reading (b), "peak in field", nearly always fails (1 of 16). This follows from the criterion's definition, not from a choice by the author.
6. **[does not affect a conclusion]** Rat 2's preflight units share no tetrode with its flight units (cell 7). The file may be assigned to the wrong rat; it cannot be checked from the data, and the notebook says so.
7. **[does not affect a conclusion]** Things I checked and found correct:
   - `skaggs_info` and `peak_in_field` pass their synthetic tests (cell 15).
   - `compare` is a two-sided Mann-Whitney test at 0.05, as the claims file reads it.
   - The 1/11 chance level of the shift test is correct for 10 shifts.
   - The paper states no chance level, so there is nothing to compare.
   - No training/test leakage applies.
8. **Claims file:** I found no misreading of the paper. The fig3 statement ("fourth cell lost its field", "a few other cells gained a field") matches the Fig. 3 legend. Fixing rat 2's preflight cells to the rectangular track is an inference from Fig. 2b, but the criterion runs both preflight epochs anyway.

### C. What I could not check, and the output that would settle it

- **Fig3 pairing (B1):** for every ES1 and ES2 map of Rat3 FD4, the best-matching unit and its correlation, plus every unit's best ES1 and ES2 map. Flag any map that is best for more than one unit and any unit that is best for more than one map.
- **M-a selection (B3):** `source_file` and `cell_number` of every map counted as active, per file. That would show whether maps with `cell_number` −1 are per-cell maps.
- **Rat 2 FD4 position (B2):** the time-shift contrast with Rat 2's units on the Rat 1 file's trace versus the Rat 2 file's trace in the same ES window, at the timestamps where they differ.
- **Cell counts:** for Rat3 FD4 ES1, which of the 11 active maps are place cells in the paper's sense. That would show whether some selection reproduces the paper's 7 cells.
- **Smoothing:** the kernel of the deposited maps is unknown and cannot be recovered from the files. I did not re-run any computation; every number above is taken from the notebook's outputs.

## End of run

13 turns, 3 minutes, result: success.
