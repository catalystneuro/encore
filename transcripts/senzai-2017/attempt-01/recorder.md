# 000003 · recorder · run 38861157458

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000003 --write; git diff; ls transcripts/000003/ claims/000003/; cat attempts/000003-senzai-2017-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000003' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (239.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b6937443-35a7-49c4-9014-12dfa9abaad5/tool-results/bhe3648xm.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index f82f4d6..e5cb9e9 100644
--- a/README.md
+++ b/README.md
@@ -66,6 +66,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
 | [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
 | [000041](https://dandiarchive.org/dandiset/000041) | [Watson et al. 2016](https://doi.org/10.1016/j.neuron.2016.03.036) | 8 | 9 | 15 | 7 | [`000041-watson-2016`](entries/000041-watson-2016) |
+| [000003](https://dandiarchive.org/dandiset/000003) | [Senzai et al. 2017](https://doi.org/10.1016/j.neuron.2016.12.011) | 15 | 11 | 3 | 2 | [`000003-senzai-2017`](entries/000003-senzai-2017) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000003/:
10.1016-j.neuron.2016.12.011.yaml

transcripts/000003/:
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 "^| Dandiset\|^|---\|^| ---" README.md | head; python -c "import json;d=json.load(open('targets/dandisets.json'));print(type(d)); s=json.dumps(d); i=s.find('\"000003\"'); print(s[i-200:i+800])"; grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
<class 'dict'>
https://api.dandiarchive.org/api", "counts": {"public_dandisets": 657, "with_a_paper": 232, "with_a_published_version": 201, "papers": 246, "converted_by_catalystneuro": 50}, "targets": [{"dandiset": "000003", "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "published_version": "0.260218.2052", "asset_count": 101, "size_gb": 2559.25, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["House mouse"], "approaches": ["electrophysiological approach", "behavioral approach"], "papers": [{"doi": "10.1016/j.neuron.2016.12.011", "title": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells", "relation": "IsDescribedBy", "resource_type": "JournalArticle", "preprint": false}], "catalystneuro": ["contributor Baker, Cody of CatalystNeuro"]}, {"dandiset": "000004", "name": "A NWB-based dataset and processing pipeline of human single-neuron activity during a declarative memory task",
937:### 001933, Chen et al. 2026
991:### 000004, Chandravadia et al. 2020
1028:### 002013, Amjad et al. 2025
1066:### 001636, Pasquereau et al. 2013
1127:### 001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)
1195:### 000041, Watson et al. 2016
1264 docs/pilot-notes.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 991
}
```

```
991	### 000004, Chandravadia et al. 2020
992	
993	Ten claims reproduced, eight partially, four not reproduced and one blocked
994	on the dandiset, plus two claims using the earlier release (Faraut et al.
995	2018), both partially reproduced; both rounds agreed with every outcome.
996	The paper is a data descriptor, so most claims are about what the files
997	hold (counts, tables, codes, dates); the rest are the Figure 5 analyses of
998	visually and memory selective cells, which reproduce for the visually
999	selective cells and the ROC measures.
1000	
1001	The dandiset was converted with CatalystNeuro's involvement (Ben Dichter
1002	is a contributor). The most consequential finding is that the
1003	`new_old_labels_recog` column is described, in every file and in the
1004	paper, as 0 for old and 1 for new, while the data use 1 for old; the
1005	paper's own code reads it correctly, but a user who follows the
1006	description inverts every recognition analysis. Others: two pairs of
1007	sessions hold identical spike trains for all their units, so 55 of 1864
1008	units are repeats; eight sessions have fewer encoding trials than the 100
1009	the paper describes; the spike times of 13 units are out of order and two
1010	units hold every spike twice; electrode impedance is empty and some MNI
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000003; wc -c *-report.md; cat author-report.md
```

```
6827 author-report.md
 4385 author-revise-1-report.md
 3526 author-revise-2-report.md
10769 verifier-1-report.md
 5558 verifier-2-report.md
31065 total
I've finished steps 1 to 6 for dandiset 000003. The entry locks, passes `check`, and the notebook runs from a clean environment in 8.1 minutes (twice, with identical outputs). The handover package is built in `executed/000003-senzai-2017/handover/`. Nothing is committed.

**Paper:** I used the full text, from the accepted author manuscript in PubMed Central (PMC5293146), saved under `paper/`. The supplementary figures were not available.

**Version:** pinned to 0.260218.2052. The paper cites no DANDI version. All four published versions hold the same 101 files (same paths, sizes and checksums) and differ only in metadata, so I took the most recent. The notebook header says this and prints the comparison.

### 1. Outcomes (31 claims: 15 reproduced, 11 partially, 3 not reproduced, 2 blocked)

| Claim | Outcome |
|---|---|
| unit-counts (586 GC, 500 MC; here 609 and 568) | partially reproduced |
| first-stage-labels | partially reproduced |
| interneuron-rates | partially reproduced |
| gc-narrower-waveform | reproduced |
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000003; cat verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md
```

```
**A. Outcomes** (31 claims in the claims file. No attempt record was among my materials, so the counts come from the claims file alone.)

| Claim | Outcome | Reason |
|---|---|---|
| unit-counts | partially_reproduced | GC 609 is inside 527–645, but MC 568 is outside 450–550 (cell 25). |
| first-stage-labels | partially_reproduced | Two of three groups pass under both thresholds: GC+MC 0.982, wI 0.917/0.933. nI below 0.425 ms is 0.825, under the 0.90 bar (cell 27). |
| interneuron-rates | partially_reproduced | Kruskal-Wallis P ≤ 5e-15 under both readings. Under (b), nI 8.75 Hz is inside its tolerance but wI 3.08 Hz is outside 1.90–2.32; under (a) both are outside (cell 29). |
| gc-narrower-waveform | reproduced | GC 0.710 vs MC 0.740 ms, P = 2.3e-14 (cell 31). This rests on truncated latencies; see B1. |
| optotag-drd2 | partially_reproduced | MC suppressed 0.642 (pre-pulse baseline) vs the paper's 0.271; GC 0.030. MC exceeds four times GC (cell 33). |
| mc-more-active | reproduced | MC > GC in wake (P = 1.8e-114) and NREM (P = 2e-29) (cell 35). |
| gc-nrem-highest | partially_reproduced | NREM exceeds wake and REM (adjusted P ≤ 9e-31), but wake (0.077) and REM (0.198) differ (adjusted P = 1.4e-25) (cell 37). |
| ca3-wake-highest | not_reproduced | The wake median (0.441, or 0.433 with quiet wake) is below NREM (0.459), and NREM vs wake is not significant (adjusted P = 0.77/0.59). The ordering fails (cell 39). |
| nrem-wake-ratio | reproduced | GC median ratio 4.63 vs MC 1.11, P = 3.9e-141. The MC NREM-vs-wake Wilcoxon gives P = 1.4e-6, so the "equivalent" part for MC is not supported (cell 41). |
| theta-modulation | reproduced | MRL GC 0.422 > MC 0.339 (P = 1.5e-20). Phase under reading (a): GC 30.8° vs MC 12.0°, P = 1e-17 (cell 43). See B8. |
| gamma-modulation | reproduced | MRL GC 0.319 > MC 0.212 (P = 4.8e-43). GC phase earlier (−20.2° vs 1.7°), P = 1.2e-23 under (a) (cell 45). |
| gamma-rate-correlation | partially_reproduced | Under (a), GC r = −0.177 is in
[... 151 more lines not kept]
```

**Agent**

README row written (15, 11, 3, 2). Now reading the attempt record's findings for exact numbers.

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/000003-senzai-2017-01.yaml'))
print([k for k in d])
for f in d.get('findings',[]): print(yaml.dump(f,width=200)); print('---')
for v in d.get('verifications',[]): print({k:v[k] for k in v if k not in('outcomes','claims')})
E
grep -rn "to-nwb\|github.com" attempts/000003-senzai-2017-01.yaml | head; grep -n "to-nwb" transcripts/000003/author.md | head -5
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b6937443-35a7-49c4-9014-12dfa9abaad5/tool-results/b6qbrj8ke.txt

Preview (first 2KB):
['schema_version', 'id', 'dandiset', 'dandiset_version', 'paper', 'date', 'entry', 'provenance', 'outcomes', 'findings', 'verifications']
kind: format_error
statement: In 24 files the end index of the first unit in the units table is short by a multiple of 65,536 spikes (k = 1 to 7). The missing spikes open the second unit's spike train, which then restarts
  at the beginning of the recording, so the second unit's times are not sorted. The first moved spike follows the first unit's last stored spike by 2 ms to 0.5 s. This looks like an integer overflow at
  conversion; the waveforms follow the same boundaries.

---
kind: metadata_error
statement: The genotypes in the files (6 SST-Cre, 5 Drd2-Cre::Ai35, 4 POMC-Cre::Arch, 1 POMC-Cre::Ai35) do not match the paper's 16 mice (7 SST-Cre, 5 DRD2-Cre::Ai35, 3 POMC-Cre::Ai35 and 1 wild type).

---
kind: metadata_insufficient
statement: 83 of 101 files do not say which shank each unit was recorded on (`shank_id` is a cluster number, and there is no `electrode_group`), and no file gives site coordinates (x, y, z are NaN). The
  paper's depth measures can be computed for 17 files only, and distances between cells not at all.

---
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
d=yaml.safe_load(open('attempts/000003-senzai-2017-01.yaml'))
for f in d['findings']: print(f['kind'],'|',f['statement']); print()
for v in d['verifications']: print({k:(str(v[k])[:300]) for k in v})
E
grep -n "to-nwb" attempts/000003-senzai-2017-01.yaml claims/000003/*.yaml transcripts/000003/*-report.md | head
```

```
format_error | In 24 files the end index of the first unit in the units table is short by a multiple of 65,536 spikes (k = 1 to 7). The missing spikes open the second unit's spike train, which then restarts at the beginning of the recording, so the second unit's times are not sorted. The first moved spike follows the first unit's last stored spike by 2 ms to 0.5 s. This looks like an integer overflow at conversion; the waveforms follow the same boundaries.

metadata_error | The genotypes in the files (6 SST-Cre, 5 Drd2-Cre::Ai35, 4 POMC-Cre::Arch, 1 POMC-Cre::Ai35) do not match the paper's 16 mice (7 SST-Cre, 5 DRD2-Cre::Ai35, 3 POMC-Cre::Ai35 and 1 wild type).

metadata_insufficient | 83 of 101 files do not say which shank each unit was recorded on (`shank_id` is a cluster number, and there is no `electrode_group`), and no file gives site coordinates (x, y, z are NaN). The paper's depth measures can be computed for 17 files only, and distances between cells not at all.

metadata_insufficient | The T-maze position series (`twhl_linearized`, `twhl_norm`) are not described. The values show column 0 of `twhl_linearized` runs along the central arm (0 to 2) and column 1 is an angle along the circular side arms, negative for the left arm, which fits the maze in the Methods but is not stated.

metadata_insufficient | The states table holds `awake`, `quiet`, `nrem`, `rem` and `transit` without a description; the paper names wake, NREM and REM, and whether `quiet` counts as wake is not stated.

metadata_insufficient | The interneuron labels (narrow-waveform, wide-waveform) do not say whether the unit is in the dentate gyrus or CA3, which the paper separates; only the excitatory label was split by region (granule cell or CA3 pyramidal cell).

data_missing | The monosynaptic connections the authors detected and curated (`MonoSynConvClick.mat`) were not converted (the conversion code comments them out), so the pair-based results (Figures 3, 4 and 7) cannot be checked on the aut
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -on "[A-Za-z0-9_./-]*to-nwb[A-Za-z0-9_./-]*\|github.com/[A-Za-z0-9_./-]*" transcripts/000003/*.md claims/000003/*.yaml | sort -u -t: -k3 | head -20; python -c "
import yaml;d=yaml.safe_load(open('claims/000003/10.1016-j.neuron.2016.12.011.yaml'));print([k for k in d]); print(str(d)[:1500])"
```

```
transcripts/000003/author.md:589://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb
transcripts/000003/author.md:638://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits
transcripts/000003/author.md:3900://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits/e4652c1
transcripts/000003/author.md:600://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/commits/master
transcripts/000003/author.md:589://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/git/trees/HEAD
transcripts/000003/author.md:652://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/git/trees/c5ddf39
transcripts/000003/author.md:660://api.github.com/repos/catalystneuro/buzsaki-lab-to-nwb/git/trees/e4652c1
transcripts/000003/author.md:2830://github.com/catalystneuro/buzsaki-lab-to-nwb
transcripts/000003/author.md:600://raw.githubusercontent.com/catalystneuro/buzsaki-lab-to-nwb/
transcripts/000003/author.md:670://raw.githubusercontent.com/catalystneuro/buzsaki-lab-to-nwb/e4652c1/buzsaki_lab_to_nwb/original_code/convert_yuta.py
transcripts/000003/author.md:589:github.com/search/code
['schema_version', 'dandiset', 'paper', 'claims']
{'schema_version': 1, 'dandiset': '000003', 'paper': 'doi:10.1016/j.neuron.2016.12.011', 'claims': [{'id': 'unit-counts', 'statement': 'The second-stage classification divided dentate excitatory neurons into 586 putative granule cells (GC) and 500 putative mossy cells (MC).', 'source': 'Results, Identification of granule cells and mossy cells; Figure 1F', 'expected': [{'quantity': 'GC units', 'value': 586, 'tolerance': 58.6}, {'quantity': 'MC units', 'value': 500, 'tolerance': 50}], 'criterion': "Counted from the units' cell_type labels over all files, once per recording day. Reproduced when both counts are within tolerance; partially reproduced when one is."}, {'id': 'first-stage-labels', 'statement': 'Narrow-waveform interneurons have a trough-to-peak latency below 0.425 ms, and among wide-waveform units the excitatory cells have a burst in
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> docs/pilot-notes.md <<'E'

### 000003, Senzai et al. 2017

Fifteen claims reproduced, eleven partially, three not reproduced and two
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
without seeing the record and agreed with all 31; round 2 agreed again and
nothing was proposed, so there was no third round. The paper reports the
physiological properties and behavioral correlates of granule cells and
mossy cells in the mouse dentate gyrus. The unit counts and classification,
firing rates across wake, NREM and REM, theta and gamma modulation,
recruitment by dentate spikes, monosynaptic granule to mossy cell pairs,
place fields and remapping in the T-maze and open field, and depth (on the
17 files that give each unit's shank) were tested. `gc-mc-distance` and
`gc-backpropagation` are blocked as `metadata_insufficient`, because no file
gives site coordinates; the second revision found the stored channel order
consistent with depth, which makes them testable on the 17 files, but left
that to a new attempt. Some outcomes rest on weak ground: the phase part of
`theta-modulation` holds on one cut of the cycle only, and the spike-count
corrected comparison gives P = 0.00056 against the paper's P < 0.0001; the
permutation test for `pv-remap` gives P = 0.32; the overlap of 0.31 in
`inheritance-tmaze` is at chance (median 0.38); `gc-narrower-waveform` on all
files is mostly driven by truncated waveforms, and on the wide-band signal of
the 17 files gives P = 0.017 unfiltered and P = 0.4 after a 300 Hz
high-pass; and the pair-based claims rest on automatic detections, 65 pairs
against the paper's 32.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). In 24 files the end index of the first unit is short by a
multiple of 65,536 spikes (k = 1 to 7), and the missing spikes open the
second unit's train, which looks like an integer overflow at conversion; the
loader moves them back and reports each repair. In the 17 files with the
wide-band signal, the electrodes table's map of columns to shanks and sites
disagrees with the data: a unit's largest spike lies on the shank the units
table gives for 45% of units and on the table's own site for 9%, and the DS2
amplitude along the table's site numbers crosses zero more than once on 43
of 64 shanks; the units' `electrode_group` and stored waveform channels fit
one fixed map in all 4 mice, so the error is in the table. The authors'
curated monosynaptic connections (`MonoSynConvClick.mat`) were not
converted, so Figures 3, 4 and 7 cannot be checked on their pairs. Other
findings: the genotypes in the files (6 SST-Cre, 5 Drd2-Cre::Ai35, 4
POMC-Cre::Arch, 1 POMC-Cre::Ai35) do not match the paper's (7 SST-Cre, 5
DRD2-Cre::Ai35, 3 POMC-Cre::Ai35 and 1 wild type); 83 of 101 files do not say
which shank each unit was on and no file gives site coordinates, and the
units table has two layouts; the stored waveforms are about 5 times larger
than the same spikes in the wide-band signal, consistent with ADC counts read
as microvolts, and their 1.6 ms window cuts off the peak of 43% of GC, 67%
of MC and 78% of CA3 waveforms; the dandiset holds 568 mossy cells and 609
granule cells against the paper's 500 and 586, and 237 units labelled
`missing`; the T-maze position series and the states `quiet` and `transit`
are not described; the interneuron labels do not say whether a unit is in
the dentate gyrus or CA3; one light-pulse series holds 24,286 duplicate
times among 89,086; seven dates hold two files of one mouse that are
separate recordings, without saying what they are; and the paper gives a
burst index threshold of 1.2 in the Methods and 1.8 in the Figure 1A legend.

The electrodes-table finding came in the first revision, after the verifier
asked whether waveform channels map to the shank's electrodes; the criteria
of `mc-deeper` and `gc-mc-classification` were then changed to take each
unit's site from the wide-band signal, with what had been seen recorded in
the claims file, and both stayed reproduced. Untracked dotfiles and a
`scripts/` directory that the author did not create appeared in the
repository during the run and were left alone. The author's points on the
protocol: preliminary results printed while building the helper before the
criteria were written; no rule on deposited labels against re-running the
paper's classification; where to record conversion code read when no
analysis code is linked; whether to repair a detectable format error; the
10% rule giving zero tolerance for a reported zero; dependents of partially
reproduced claims, which the `depends_on` rule does not cover; metadata
found after the criteria were written; multiple readings that make ambiguous
claims pass easily; clock checks for continuous sessions without trial
tables; counting the same unit across days; and claims citing supplementary
figures that were not available.
E
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

**Agent**

I ran `python tools/readme_row.py 000003 --write`, which added the row 15 / 11 / 3 / 2 to README.md, and I added the subsection below at the end of docs/pilot-notes.md. Nothing is committed.

Two things to check before the workflow commits:

- **Conversion repository:** the `catalystneuro` field for 000003 names a person ("contributor Baker, Cody of CatalystNeuro"), not a repository. None of the sources I was allowed to use names one either. So the opening sentence of the second paragraph gives the contributor, as the 000004 subsection does. The full author transcript (`transcripts/000003/author.md`) does read `catalystneuro/buzsaki-lab-to-nwb`, if you want the repository there instead.
- **Untracked files:** dotfiles (`.bashrc`, `.gitconfig`, `.mcp.json` and others), `.idea`, `.vscode` and a `scripts/` directory are untracked in the repo root. The author's report says it did not create them. Make sure they don't go into the commit.

### 000003, Senzai et al. 2017

Fifteen claims reproduced, eleven partially, three not reproduced and two
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
without seeing the record and agreed with all 31; round 2 agreed again and
nothing was proposed, so there was no third round. The paper reports the
physiological properties and behavioral correlates of granule cells and
mossy cells in the mouse dentate gyrus. The unit counts and classification,
firing rates across wake, NREM and REM, theta and gamma modulation,
recruitment by dentate spikes, monosynaptic granule to mossy cell pairs,
place fields and remapping in the T-maze and open field, and depth (on the
17 files that give each unit's shank) were tested. `gc-mc-distance` and
`gc-backpropagation` are blocked as `metadata_insufficient`, because no file
gives site coordinates; the second revision found the stored channel order
consistent with depth, which makes them testable on the 17 files, but left
that to a new attempt. Some outcomes rest on weak ground: the phase part of
`theta-modulation` holds on one cut of the cycle only, and the spike-count
corrected comparison gives P = 0.00056 against the paper's P < 0.0001; the
permutation test for `pv-remap` gives P = 0.32; the overlap of 0.31 in
`inheritance-tmaze` is at chance (median 0.38); `gc-narrower-waveform` on all
files is mostly driven by truncated waveforms, and on the wide-band signal of
the 17 files gives P = 0.017 unfiltered and P = 0.4 after a 300 Hz
high-pass; and the pair-based claims rest on automatic detections, 65 pairs
against the paper's 32.

The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
a contributor). In 24 files the end index of the first unit is short by a
multiple of 65,536 spikes (k = 1 to 7), and the missing spikes open the
second unit's train, which looks like an integer overflow at conversion; the
loader moves them back and reports each repair. In the 17 files with the
wide-band signal, the electrodes table's map of columns to shanks and sites
disagrees with the data: a unit's largest spike lies on the shank the units
table gives for 45% of units and on the table's own site for 9%, and the DS2
amplitude along the table's site numbers crosses zero more than once on 43
of 64 shanks; the units' `electrode_group` and stored waveform channels fit
one fixed map in all 4 mice, so the error is in the table. The authors'
curated monosynaptic connections (`MonoSynConvClick.mat`) were not
converted, so Figures 3, 4 and 7 cannot be checked on their pairs. Other
findings: the genotypes in the files (6 SST-Cre, 5 Drd2-Cre::Ai35, 4
POMC-Cre::Arch, 1 POMC-Cre::Ai35) do not match the paper's (7 SST-Cre, 5
DRD2-Cre::Ai35, 3 POMC-Cre::Ai35 and 1 wild type); 83 of 101 files do not say
which shank each unit was on and no file gives site coordinates, and the
units table has two layouts; the stored waveforms are about 5 times larger
than the same spikes in the wide-band signal, consistent with ADC counts read
as microvolts, and their 1.6 ms window cuts off the peak of 43% of GC, 67%
of MC and 78% of CA3 waveforms; the dandiset holds 568 mossy cells and 609
granule cells against the paper's 500 and 586, and 237 units labelled
`missing`; the T-maze position series and the states `quiet` and `transit`
are not described; the interneuron labels do not say whether a unit is in
the dentate gyrus or CA3; one light-pulse series holds 24,286 duplicate
times among 89,086; seven dates hold two files of one mouse that are
separate recordings, without saying what they are; and the paper gives a
burst index threshold of 1.2 in the Methods and 1.8 in the Figure 1A legend.

The electrodes-table finding came in the first revision, after the verifier
asked whether waveform channels map to the shank's electrodes; the criteria
of `mc-deeper` and `gc-mc-classification` were then changed to take each
unit's site from the wide-band signal, with what had been seen recorded in
the claims file, and both stayed reproduced. Untracked dotfiles and a
`scripts/` directory that the author did not create appeared in the
repository during the run and were left alone. The author's points on the
protocol: preliminary results printed while building the helper before the
criteria were written; no rule on deposited labels against re-running the
paper's classification; where to record conversion code read when no
analysis code is linked; whether to repair a detectable format error; the
10% rule giving zero tolerance for a reported zero; dependents of partially
reproduced claims, which the `depends_on` rule does not cover; metadata
found after the criteria were written; multiple readings that make ambiguous
claims pass easily; clock checks for continuous sessions without trial
tables; counting the same unit across days; and claims citing supplementary
figures that were not available.

## End of run

10 turns, 1 minutes, result: success.
