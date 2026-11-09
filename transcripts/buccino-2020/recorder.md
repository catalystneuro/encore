# 000034 · recorder · run 39835989572

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000034 --write; git diff; ls claims/000034 transcripts/000034; cat attempts/000034-buccino-2020-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (57.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/287e9507-76e1-41d4-8bf3-212a14c21f57/tool-results/b6y8gyoev.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 66d378d0..ee6f57c7 100644
--- a/README.md
+++ b/README.md
@@ -115,6 +115,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000013](https://dandiarchive.org/dandiset/000013) | [Hires et al. 2015](https://doi.org/10.7554/elife.06619) | 22 | 1 | 8 | 14 | [`000013-hires-2015`](entries/000013-hires-2015) |
 | [000015](https://dandiarchive.org/dandiset/000015) | [Chen et al. 2017](https://doi.org/10.1016/j.neuron.2017.05.005) | 11 (+1) | 3 | 7 | 8 | [`000015-chen-2017`](entries/000015-chen-2017) |
 | [000019](https://dandiarchive.org/dandiset/000019) | [Bouchard et al. 2013](https://doi.org/10.1038/nature11911) | 1 | 1 | 4 | 16 | [`000019-bouchard-2013`](entries/000019-bouchard-2013) |
+| [000034](https://dandiarchive.org/dandiset/000034) | [Buccino et al. 2020](https://doi.org/10.7554/elife.61834) | 0 | 1 | 0 | 22 | [`000034-buccino-2020`](entries/000034-buccino-2020) |
 
 Counts are of the paper's findings that rest on the dandiset, including
 those that take names for its own codes from elsewhere. Findings that also
claims/000034:
10.7554-elife.61834.yaml

transcripts/000034:
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 '^| \[000013' README.md | head; cat attempts/000034-buccino-2020-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; ls -la transcripts/000034
```

```
<persisted-output>
Output too large (57.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/287e9507-76e1-41d4-8bf3-212a14c21f57/tool-results/b10wxd26g.txt

Preview (first 2KB):
112-| [000008](https://dandiarchive.org/dandiset/000008) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 11 (+9) | 4 | 1 | 0 (+2) | [`000008-scala-2021`](entries/000008-scala-2021) |
113-| [000010](https://dandiarchive.org/dandiset/000010) | [Li et al. 2015](https://doi.org/10.1038/nature14178) | 8 | 3 | 5 | 11 | [`000010-li-2015`](entries/000010-li-2015) |
114-| [000011](https://dandiarchive.org/dandiset/000011) | [Li et al. 2016](https://doi.org/10.1038/nature17643) | 6 | 5 | 9 | 18 | [`000011-li-2016`](entries/000011-li-2016) |
115:| [000013](https://dandiarchive.org/dandiset/000013) | [Hires et al. 2015](https://doi.org/10.7554/elife.06619) | 22 | 1 | 8 | 14 | [`000013-hires-2015`](entries/000013-hires-2015) |
schema_version: 2
id: 000034-buccino-2020-01
dataset:
  archive: dandi
  id: '000034'
  version: 0.211030.0713
  doi: 10.48324/dandi.000034/0.211030.0713
paper: doi:10.7554/elife.61834
date: '2026-10-22'
entry: 000034-buccino-2020
provenance:
  kind: agent
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/000034-buccino-2020-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000034-buccino-2020-01
3	dataset:
4	  archive: dandi
5	  id: '000034'
6	  version: 0.211030.0713
7	  doi: 10.48324/dandi.000034/0.211030.0713
8	paper: doi:10.7554/elife.61834
9	date: '2026-10-22'
10	entry: 000034-buccino-2020
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 695 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 100,112p README.md; sed -n 116,135p README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; ls -la transcripts/000034; wc -c claims/000034/*
```

```
| [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 6 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
| [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
| [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 | 0 | 2 | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
| [001550](https://dandiarchive.org/dandiset/001550) | [Pagan et al. 2025](https://doi.org/10.1038/s41586-024-08433-6) | 11 (+1) | 2 | 0 | 0 | [`001550-pagan-2025`](entries/001550-pagan-2025) |
| [001692](https://dandiarchive.org/dandiset/001692) | [Bouabid et al. 2026](https://doi.org/10.64898/2026.01.20.700614) | 18 | 8 | 3 | 0 | [`001692-bouabid-2026`](entries/001692-bouabid-2026) |
| [001699](https://dandiarchive.org/dandiset/001699) | [Moore et al. 2025](https://doi.org/10.1101/2025.01.09.632139) | 14 | 7 | 5 | 1 | [`001699-moore-2025`](entries/001699-moore-2025) |
| [001878](https://dandiarchive.org/dandiset/001878) | [Sun et al. 2021](https://doi.org/10.22002/d1.1991) | 4 | 2 (+1) | 0 | 0 | [`001878-sun-2021`](entries/001878-sun-2021) |
| [001712](https://dandiarchive.org/dandiset/001712) | [Davatolhagh et al. 2025](https://doi.org/10.1101/2025.09.12.675910) | 3 | 2 | 2 | 11 | [`001712-davatolhagh-2025`](entries/001712-davatolhagh-2025) |
| [001888](https://dandiarchive.org/dandiset/001888) | [Hristova et al. 2025](https://doi.org/10.1111/epi.18606) | 13 | 9 | 2 | 10 | [`001888-hristova-2025`](entries/001888-hristova-2025) |
| [000005](https://dandiarchive.org/dandiset/000005) | [Yu et al. 2016](https://doi.org/10.1038/nn.4412) | 5 | 9 | 6 | 13 | [`000005-yu-2016`](entries/000005-yu-2016) |
| [CRCNS:ret-1](https://crcns.org/data-sets/retina/ret-1) | [Lefebvre et al. 2008](https://doi.org/10.1242/dev.0279
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^| Dandiset\|^| Data' README.md; sed -n 5857,99999p docs/pilot-notes.md
```

```
<persisted-output>
Output too large (40.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/287e9507-76e1-41d4-8bf3-212a14c21f57/tool-results/bk308xy21.txt

Preview (first 2KB):
52:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
### 000006, Economo et al. 2018, second attempt

Seven claims reproduced, five partially, three not reproduced and eight
blocked on the dandiset, with eight more on data in other archives, of which
five reproduced, one partially and two blocked. The claims file was written
again from the full text, as the earlier one, written from the abstract only,
is deprecated; it has 31 claims, and the dandiset is unchanged at version
0.220126.1855, its only published version. The author put 15 questions to a
reader. The answers made the code's per-unit rule the unit selection when
neither reading gives the paper's counts and each unit's own trial range the
trial range, so `pt-spike-rates-similar` moved from blocked to not reproduced
and `pt-variance-explained` and `pt-single-neuron-early-selectivity` from
blocked to reproduced; they moved the dependency of
`pt-lower-heterogeneous-rates` to `pt-tagged-units`, so it moved from blocked
to reproduced; they named three readings for the reconstruction counts, so
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 6100
}
```

```
File content (426.7KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 6100,
 "limit": 400
}
```

```
6100	### 000013, Hires et al. 2015
6101	
6102	Twenty-two claims reproduced, one partially, eight not reproduced and
6103	fourteen blocked, all on the dandiset and all blocked as
6104	`methods_underspecified`. It pins version 0.220126.2143, the only published
6105	version, as the paper predates the dandiset and cites none; the draft holds
6106	the same 52 blobs. The claims check added `example-cell-phase-modulation`, so
6107	the file has 45 claims. The author put seven questions to a reader; the
6108	answers changed four outcomes. They set the start of the touch response
6109	cutoff search at the transition where the curve levels off, keeping the
6110	literal search from 1 ms only as a variant, so `table1-l4-c2` moved from
6111	blocked to reproduced and `table1-l5` from blocked to partially reproduced;
6112	they made the phase decoder use the phase-tuning cycles, so
6113	`fig4c-phase-decoding` moved from not reproduced to blocked; and they made
6114	"median higher" the median of the per-cell differences, so
6115	`whisking-rate-l5-increase` moved from partially reproduced to reproduced.
6116	Round 1 gave its own outcome for each claim from the executed notebook with
6117	its conclusions and summary removed and agreed with 36 of 45.
6118	`behavior-whisking-bouts`, `behavior-touches-reaction` and
6119	`example-cell-touch-window` moved from partially reproduced to not
[... 317 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000034; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md claims-report.md claims-check-report.md; do echo "=== $f"; cat $f; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if str(x.get('id',x.get('identifier','')))in('000034','DANDI:000034'): print(json.dumps(x,indent=1))
" || grep -n -A20 '"000034"' targets/dandisets.json
```

```
<persisted-output>
Output too large (31.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/287e9507-76e1-41d4-8bf3-212a14c21f57/tool-results/brn2zulsu.txt

Preview (first 2KB):
=== author-report.md
The entry ran clean and the verifier's handover is built in `executed/000034-buccino-2020/handover/`. Only 1 of the 24 claims could be tested, and it reproduced; the other 23 are blocked because the paper's six spike sorters cannot be run here. Nothing is committed.

**1. Outcomes** (`attempts/000034-buccino-2020-01.yaml`)

| Claim | Outcome |
|---|---|
| recordings-as-described (link) | reproduced (all 15 checks hold) |
| fig4a-curators-agree | blocked, not_runnable. It depends on the blocked fig1b-unit-counts. Computed anyway from the two curated files: 226 shared units of 351 (64.39%), exactly the paper's 226 and 351. The paper's 174 needs the Kilosort2 run. |
| fig1b, fig1c, fig1d, fig1s2, fig1s3-s4, fig2c, fig2s1a, fig2s1b, fig2d, fig2e (×3), fig3a, fig3b, fig3c, fig3s1 (×2), fig3d, fig3s2, fig4b, fig4c, fig4d (22 claims) | blocked, not_runnable |

**2. What was found about the dataset.** I pinned 0.211030.0713: the paper cites only the draft, and this is the only published version, with the same six files (same ids and sizes) as the draft.
- **Contents:** all four recordings and both curations are there, with the stated rates, channel counts, durations and 250 ground-truth units. No sorter output is deposited, including the Kilosort2 run the curators worked on.
- **Clocks:** on the first seconds read, the curated and ground-truth spike times line up with spikes in the raw traces (deepest trough at lag 0).
- **Curated files:** spike times only. They have no sampling rate, no unit labels, no link to the Kilosort2 clusters, and nothing says which file is curator 1.
- **Retina recording:** stored as raw 12-bit converter counts (centred near 2048, saturating at 4096), but the file says 1e-6 V per count 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/287e9507-76e1-41d4-8bf3-212a14c21f57/tool-results/brn2zulsu.txt"
}
```

```
1	=== author-report.md
2	The entry ran clean and the verifier's handover is built in `executed/000034-buccino-2020/handover/`. Only 1 of the 24 claims could be tested, and it reproduced; the other 23 are blocked because the paper's six spike sorters cannot be run here. Nothing is committed.
3	
4	**1. Outcomes** (`attempts/000034-buccino-2020-01.yaml`)
5	
6	| Claim | Outcome |
7	|---|---|
8	| recordings-as-described (link) | reproduced (all 15 checks hold) |
9	| fig4a-curators-agree | blocked, not_runnable. It depends on the blocked fig1b-unit-counts. Computed anyway from the two curated files: 226 shared units of 351 (64.39%), exactly the paper's 226 and 351. The paper's 174 needs the Kilosort2 run. |
10	| fig1b, fig1c, fig1d, fig1s2, fig1s3-s4, fig2c, fig2s1a, fig2s1b, fig2d, fig2e (×3), fig3a, fig3b, fig3c, fig3s1 (×2), fig3d, fig3s2, fig4b, fig4c, fig4d (22 claims) | blocked, not_runnable |
11	
12	**2. What was found about the dataset.** I pinned 0.211030.0713: the paper cites only the draft, and this is the only published version, with the same six files (same ids and sizes) as the draft.
13	- **Contents:** all four recordings and both curations are there, with the stated rates, channel counts, durations and 250 ground-truth units. No sorter output is deposited, including the Kilosort2 run the curators worked on.
14	- **Clocks:** on the first seconds read, the curated and ground-truth spike times line up with spikes in the raw traces (deepest trough at lag 0).
15	- **Curated files:** spike times only. They have no sampling rate, no unit labels, no link to the Kilosort2 clusters, and nothing says which file is curator 1.
16	- **Retina recording:** stored as raw 12-bit converter counts (centred near 2048, saturating at 4096), but the file says 1e-6 V per count with no offset. Recorded as a metadata error.
17	- **Missing descriptions:** electrode location and filtering are placeholders; nothing marks which 2 of the 248 mouse channels are inactive (the paper says 24
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 500,530p targets/dandisets.json; head -60 claims/000034/10.7554-elife.61834.yaml; grep -n 'checks:' -A15 claims/000034/10.7554-elife.61834.yaml; grep -c '^- id:' claims/000034/10.7554-elife.61834.yaml
```

```
"resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000035",
   "name": "Temperature-controlled intracellular Patch-seq recordings in mouse motor cortex",
   "published_version": "0.211014.0808",
   "asset_count": 185,
   "size_gb": 1.66,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "House mouse",
    "Mus musculus - House mouse"
   ],
   "approaches": [
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^  statement:' -A3 claims/000034/10.7554-elife.61834.yaml | head -120
```

```
92:  statement: The dandiset holds the recordings the paper analyses and the files its notebooks name, with
93-    the properties the paper and the notebooks give.
94-  source: Results, opening paragraph; Data availability; the four notebooks at ee08fb6
95-  quote: The datasets are publicly available in NWB format on the DANDI archive
--
104:  statement: 'On the real Neuropixels recording the six sorters return very different numbers of units:
105-    Tridesclous the fewest (187) and SpyKING Circus the most (628); HerdingSpikes2 210, Kilosort2 446,
106-    IronClust 233 and HDSort 317.'
107-  source: Results, Spike sorters show low agreement for the same high-density dataset, paragraph 3; Figure
--
142:  statement: Of the 2031 units detected on the real recording, all six sorters agree on only 33, and two
143-    or more sorters agree on only 263.
144-  source: Results, Spike sorters show low agreement for the same high-density dataset, paragraph 4; Figure
145-    1C
--
169:  statement: For most sorters more than half of their units match no other sorter; IronClust and Tridesclous
170-    are the exceptions.
171-  source: Results, Spike sorters show low agreement for the same high-density dataset, paragraph 4; Figure
172-    1D
--
[... 99 more lines not kept]
```

**Agent**

The README row is in. Now I'm appending the subsection to docs/pilot-notes.md.

**Agent calls Bash**

```bash
cd  tail -c 200 docs/pilot-notes.md | od -c | tail -3; cat >> docs/pilot-notes.md <<'EOF'

### 000034, Buccino et al. 2020

No claim reproduced, one partially, none not reproduced and 22 blocked, all
on the dandiset; the link claim `recordings-as-described`, which the table
does not count, reproduced with all 15 of its checks holding. It pins version
0.211030.0713, the only published version, with the same six files as the
draft, the only version the paper cites. The claims check required every
reading to agree in five claims where the draft had accepted any one, and
left the file at 24 claims. The author asked no questions, as the one tested
claim was fully specified, so the answer steps changed nothing. Round 1 gave
its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with 23 of 24; it gave `fig4a-curators-agree` as
at least partially reproduced where the author had blocked it as dependent on
the blocked `fig1b-unit-counts`, and the author changed it. Round 1 also held
that `not_runnable` is not an allowed reason and gave the blocked claims as
`other`; the author kept `not_runnable`, which the schema and protocol define
for software that cannot be installed in a locked environment, and round 2
withdrew the point. Round 2 agreed with all 24, so there was no third round.
The paper, "SpikeInterface, a unified framework for spike sorting" in eLife,
runs six spike sorters on a Neuropixels recording from mouse 412804, a
simulated MEArec recording with 250 ground-truth units, a rat cortex
recording and a mouse retina recording, and reports that the sorters agree
poorly, that Kilosort2 scores highest on the simulation, that almost all
false positive units are found by a single sorter, and that consensus units
match the two experts' curations of the Kilosort2 output. Only the recordings
and the agreement of the two curators could be tested: the curators share 226
of 351 units (64.39%), within tolerance of the paper's 226, 351 and 64.2%,
while the 174 Kilosort2 units both discarded need the paper's Kilosort2 run
and are untested. The ratio leaves its tolerance at a minimum score of 0.8
(56.79%), which does not decide the outcome, as the criterion fixes the
default of 0.5. Every other claim needs the sorters' output, and Kilosort2,
IronClust and HDSort are MATLAB programs (Kilosort2 also needs a CUDA GPU)
that cannot be installed from a lock file on a runner with no MATLAB, GPU or
MPI.

The dandiset holds no output of the six sorters, including the Kilosort2 run
the two experts curated, so every comparison of sorters can be repeated only
by running them again, three of them in MATLAB, and a new Kilosort2 run will
not give the units the curators worked on. The two curated files hold a Units
table of ids and spike times only, with no sampling rate, no unit labels, no
curator name and no link to the Kilosort2 clusters, and nothing says which
file is curator 1 (they differ only by session time, 15:55:42 and 15:55:43);
their spike times fall on whole frames at 30 kHz and match the mouse
recording's clock. The retina recording is stored as unsigned 16-bit values
centred near 2048 and reaching 4096, consistent with raw counts of a 12-bit
converter, while the file states a conversion of 1e-6 V per unit and no
offset, which would put every channel near +2 mV. The mouse recording stores
int16 values with a conversion of 1e-6 V and no gain or channel_conversion;
read that way its band-passed noise SD is about 50 uV and the median curated
trough about 455 uV, several times usual Neuropixels levels, and the values
are consistent with raw counts, though the file holds nothing to show which.
Other findings: the electrode tables give location 'unknown' and filtering
'none' for every channel; the mouse recording has 248 channels where the
paper says 246 are active, without marking which; the simulated file does not
say which ground-truth cells are excitatory or inhibitory or what noise was
added; the archive's species summary lists only house mouse though one
recording is from a rat; every raw series is stored in chunks of one channel
by 7911 to 26368 frames, so reading a whole recording chunk by chunk through
h5py would take 6.2 to 16.9 h in this run, against 1.4 to 6.5 min at the 72
MB/s of one bulk ranged read; and the paper gives 226 of 351 as 64.2%, where
it is 64.39%.

The notebook ran in 288 s in the first run, after an exploratory listing of
the metadata timed out at 20 minutes and targeted reads replaced it;
HerdingSpikes 0.3.7 failed to build and SpyKING Circus had no MPI to run
with, and spikecomparison 0.2.6 and spikeextractors 0.8.4 ran on NumPy 2 with
five removed aliases restored, a recorded deviation. Round 1's points led to
the HDF5 trees of the curated files and the mouse recording, a timed bulk
read so that reading time is no longer part of the block, the mouse electrode
columns with a finding on its conversion, and the MEArec spectrum, which shows
the traces are not band-passed at 300 Hz. Round 2 found statements the
outputs did not support, among them read times from an earlier run, a
Summary that ruled out microvolts for the mouse values, a minimum-score scan
that left out the ratio falling out of tolerance at 0.8, three claims that
need Kilosort2 alone described as needing all six sorters, and a species
summary and pip results that no cell printed; these were corrected, with the
read times taken from the final run, as they vary between runs. Untracked
empty files in the repository root that the author did not create were left
alone. The author's points on the protocol: the rule that blocks a claim
depending on a blocked claim forced fig4a to blocked though its curator
counts were computed, and there is no outcome for a claim tested only in
part; `not_runnable` and `too_large` overlap when sorting software cannot
run; the protocol says nothing about restoring names removed from libraries,
which the paper-era spikecomparison and spikeextractors need on NumPy 2; and
the 10-minute aim is hard to meet when checking the data needs slow raw
reads, so only the first chunk of each recording was read.
EOF
grep -c '—\|rather' <(sed -n '/^### 000034/,$p' docs/pilot-notes.md); git status --short
```

```
0000260   e   p   o   c   h       l   e   v   e   l   "       u   n   d
0000300   e   f   i   n   e   d   .  \n
0000310
0
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
cd  python - <<'EOF'
p='docs/pilot-notes.md'; s=open(p).read()
a="""The notebook ran in 288 s in the first run, after an exploratory listing of
the metadata timed out at 20 minutes and targeted reads replaced it;"""
b="""The notebook ran in 288 s in the first run; an exploratory listing of the
metadata had timed out at 20 minutes, and targeted reads replaced it;"""
c="""draft, the only version the paper cites."""
d="""draft, which is all the paper cites."""
assert a in s and c in s
s=s.replace(a,b).replace(c,d); open(p,'w').write(s)
EOF
sed -n '/^### 000034/,$p' docs/pilot-notes.md
```

```
### 000034, Buccino et al. 2020

No claim reproduced, one partially, none not reproduced and 22 blocked, all
on the dandiset; the link claim `recordings-as-described`, which the table
does not count, reproduced with all 15 of its checks holding. It pins version
0.211030.0713, the only published version, with the same six files as the
draft, which is all the paper cites. The claims check required every
reading to agree in five claims where the draft had accepted any one, and
left the file at 24 claims. The author asked no questions, as the one tested
claim was fully specified, so the answer steps changed nothing. Round 1 gave
its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with 23 of 24; it gave `fig4a-curators-agree` as
at least partially reproduced where the author had blocked it as dependent on
the blocked `fig1b-unit-counts`, and the author changed it. Round 1 also held
that `not_runnable` is not an allowed reason and gave the blocked claims as
`other`; the author kept `not_runnable`, which the schema and protocol define
for software that cannot be installed in a locked environment, and round 2
withdrew the point. Round 2 agreed with all 24, so there was no third round.
The paper, "SpikeInterface, a unified framework for spike sorting" in eLife,
runs six spike sorters on a Neuropixels recording from mouse 412804, a
[... 66 more lines not kept]
```

**Agent**

I added the README row for 000034 (0 reproduced, 1 partially, 0 not reproduced, 22 blocked) and put the subsection below at the end of `docs/pilot-notes.md`. The dataset's `catalystneuro` field is empty, so the findings paragraph doesn't open with the CatalystNeuro sentence. Nothing is committed.

### 000034, Buccino et al. 2020

No claim reproduced, one partially, none not reproduced and 22 blocked, all
on the dandiset; the link claim `recordings-as-described`, which the table
does not count, reproduced with all 15 of its checks holding. It pins version
0.211030.0713, the only published version, with the same six files as the
draft, which is all the paper cites. The claims check required every
reading to agree in five claims where the draft had accepted any one, and
left the file at 24 claims. The author asked no questions, as the one tested
claim was fully specified, so the answer steps changed nothing. Round 1 gave
its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with 23 of 24; it gave `fig4a-curators-agree` as
at least partially reproduced where the author had blocked it as dependent on
the blocked `fig1b-unit-counts`, and the author changed it. Round 1 also held
that `not_runnable` is not an allowed reason and gave the blocked claims as
`other`; the author kept `not_runnable`, which the schema and protocol define
for software that cannot be installed in a locked environment, and round 2
withdrew the point. Round 2 agreed with all 24, so there was no third round.
The paper, "SpikeInterface, a unified framework for spike sorting" in eLife,
runs six spike sorters on a Neuropixels recording from mouse 412804, a
simulated MEArec recording with 250 ground-truth units, a rat cortex
recording and a mouse retina recording, and reports that the sorters agree
poorly, that Kilosort2 scores highest on the simulation, that almost all
false positive units are found by a single sorter, and that consensus units
match the two experts' curations of the Kilosort2 output. Only the recordings
and the agreement of the two curators could be tested: the curators share 226
of 351 units (64.39%), within tolerance of the paper's 226, 351 and 64.2%,
while the 174 Kilosort2 units both discarded need the paper's Kilosort2 run
and are untested. The ratio leaves its tolerance at a minimum score of 0.8
(56.79%), which does not decide the outcome, as the criterion fixes the
default of 0.5. Every other claim needs the sorters' output, and Kilosort2,
IronClust and HDSort are MATLAB programs (Kilosort2 also needs a CUDA GPU)
that cannot be installed from a lock file on a runner with no MATLAB, GPU or
MPI.

The dandiset holds no output of the six sorters, including the Kilosort2 run
the two experts curated, so every comparison of sorters can be repeated only
by running them again, three of them in MATLAB, and a new Kilosort2 run will
not give the units the curators worked on. The two curated files hold a Units
table of ids and spike times only, with no sampling rate, no unit labels, no
curator name and no link to the Kilosort2 clusters, and nothing says which
file is curator 1 (they differ only by session time, 15:55:42 and 15:55:43);
their spike times fall on whole frames at 30 kHz and match the mouse
recording's clock. The retina recording is stored as unsigned 16-bit values
centred near 2048 and reaching 4096, consistent with raw counts of a 12-bit
converter, while the file states a conversion of 1e-6 V per unit and no
offset, which would put every channel near +2 mV. The mouse recording stores
int16 values with a conversion of 1e-6 V and no gain or channel_conversion;
read that way its band-passed noise SD is about 50 uV and the median curated
trough about 455 uV, several times usual Neuropixels levels, and the values
are consistent with raw counts, though the file holds nothing to show which.
Other findings: the electrode tables give location 'unknown' and filtering
'none' for every channel; the mouse recording has 248 channels where the
paper says 246 are active, without marking which; the simulated file does not
say which ground-truth cells are excitatory or inhibitory or what noise was
added; the archive's species summary lists only house mouse though one
recording is from a rat; every raw series is stored in chunks of one channel
by 7911 to 26368 frames, so reading a whole recording chunk by chunk through
h5py would take 6.2 to 16.9 h in this run, against 1.4 to 6.5 min at the 72
MB/s of one bulk ranged read; and the paper gives 226 of 351 as 64.2%, where
it is 64.39%.

The notebook ran in 288 s in the first run; an exploratory listing of the
metadata had timed out at 20 minutes, and targeted reads replaced it;
HerdingSpikes 0.3.7 failed to build and SpyKING Circus had no MPI to run
with, and spikecomparison 0.2.6 and spikeextractors 0.8.4 ran on NumPy 2 with
five removed aliases restored, a recorded deviation. Round 1's points led to
the HDF5 trees of the curated files and the mouse recording, a timed bulk
read so that reading time is no longer part of the block, the mouse electrode
columns with a finding on its conversion, and the MEArec spectrum, which shows
the traces are not band-passed at 300 Hz. Round 2 found statements the
outputs did not support, among them read times from an earlier run, a
Summary that ruled out microvolts for the mouse values, a minimum-score scan
that left out the ratio falling out of tolerance at 0.8, three claims that
need Kilosort2 alone described as needing all six sorters, and a species
summary and pip results that no cell printed; these were corrected, with the
read times taken from the final run, as they vary between runs. Untracked
empty files in the repository root that the author did not create were left
alone. The author's points on the protocol: the rule that blocks a claim
depending on a blocked claim forced fig4a to blocked though its curator
counts were computed, and there is no outcome for a claim tested only in
part; `not_runnable` and `too_large` overlap when sorting software cannot
run; the protocol says nothing about restoring names removed from libraries,
which the paper-era spikecomparison and spikeextractors need on NumPy 2; and
the 10-minute aim is hard to meet when checking the data needs slow raw
reads, so only the first chunk of each recording was read.

## End of run

14 turns, 2 minutes, result: success.
