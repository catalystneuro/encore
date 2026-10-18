# 000947 · recorder · run 39116255377

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000947 --write; git diff; ls transcripts/000947/ claims/000947/; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
diff --git a/README.md b/README.md
index 9a407eb..3cfb70c 100644
--- a/README.md
+++ b/README.md
@@ -88,6 +88,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000718](https://dandiarchive.org/dandiset/000718) | [Zaki et al. 2024](https://doi.org/10.1038/s41586-024-08168-4) | 2 (+1) | 0 | 2 | 21 | [`000718-zaki-2024`](entries/000718-zaki-2024) |
 | [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
 | [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
+| [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000947/:
10.1371-journal.pbio.3000829.yaml

transcripts/000947/:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 2587
}
```

```
2587	### 000568, Valero et al. 2022
2588	
2589	Four claims reproduced, six partially, six not reproduced and six blocked, all
2590	on the dandiset. Round 1 gave its own outcome for each claim from the notebook
2591	with its conclusions removed and agreed with all 22 as they then stood, but
2592	found that most light pulses are not in the files and that the place-field
2593	rule differed from buzcode's; the revision restricted control time to windows
2594	dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
2595	11 cells between place and non-place and changed five outcomes:
2596	`figs11-place-cell-fraction` to partially reproduced,
2597	`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
2598	reproduced, and `fig3g-spatial-information` and
2599	`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
2600	22 and disagreed on `fig3g-spatial-information`, whose larger increase for
2601	unmasked fields (p = 0.039) does not hold against time-matched control maps,
2602	where the increase is negative in both groups (p = 0.3); the author proposed
2603	partially reproduced and a third round agreed. The paper reports pulsed
2604	optogenetics with uLEDs in CA1 pyramidal neurons of four CaMKIIa-Cre::Ai32
2605	mice: light-induced spiking falls during sharp-wave ripples, rises in the
2606	place field and at the theta trough, unmasks place fields in non-place cells,
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000947-schwab-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000947' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (48.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/bc1edfa2-6ce8-4bf4-b2de-4543b3cf79f6/tool-results/bc2mztal9.txt

Preview (first 2KB):
schema_version: 1
id: 000947-schwab-2020-01
dandiset: "000947"
dandiset_version: 0.240510.2211
paper: doi:10.1371/journal.pbio.3000829
date: 2026-10-18
entry: 000947-schwab-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/bc1edfa2-6ce8-4bf4-b2de-4543b3cf79f6/tool-results/bc2mztal9.txt"
}
```

```
1	schema_version: 1
2	id: 000947-schwab-2020-01
3	dandiset: "000947"
4	dandiset_version: 0.240510.2211
5	paper: doi:10.1371/journal.pbio.3000829
6	date: 2026-10-18
7	entry: 000947-schwab-2020
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The paper's per-unit result files Gaia_Analy.mat and Isis_Analy.mat, which name each analysed
18	    unit by recording file, channel and sort letter and store its peri-movement SDF, trials and
19	    detected onsets. Used for the link claim unit-link and for variants with the paper's own unit
20	    list; no outcome on the paper's findings rests on them. The analysis code read for the method
[... 753 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,110p README.md; grep -n '000947' -A15 targets/dandisets.json | head -40; cat claims/000947/*.yaml | head -80
```

```
| [001754](https://dandiarchive.org/dandiset/001754) | [Knierim et al. 2000](https://doi.org/10.1038/72910) | 3 | 0 | 1 | 3 | [`001754-knierim-2000`](entries/001754-knierim-2000) |
| [000130](https://dandiarchive.org/dandiset/000130) | [Sohn et al. 2019](https://doi.org/10.1016/j.neuron.2019.06.012) | 9 | 4 | 7 | 3 | [`000130-sohn-2019`](entries/000130-sohn-2019) |
| [001616](https://dandiarchive.org/dandiset/001616) | [Gerken et al. 2025](https://doi.org/10.7554/elife.106758.1) | 6 | 5 | 0 | 9 | [`001616-gerken-2025`](entries/001616-gerken-2025) |
| [002014](https://dandiarchive.org/dandiset/002014) | [Choi et al. 2025](https://doi.org/10.1016/j.jneumeth.2025.110467) | 4 | 1 | 0 | 8 | [`002014-choi-2025`](entries/002014-choi-2025) |
| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
| [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
| [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
| [000041](https://dandiarchive.org/dandiset/000041) | [Watson et al. 2016](https://doi.org/10.1016/j.neuron.2016.03.036) | 8 | 9 | 15 | 7 | [`000041-watson-2016`](entries/000041-watson-2016) |
| [000003](https://dandiarchive.org/dandiset/000003) | [Senzai et al. 2017](https://doi.org/10.1016/j.neuron.2016.12.011) | 15 | 11 | 3 | 2 | [`000003-senzai-2017`](entries/000003-senzai-2017) |
| [000044](https://dandiarchive.org/dandiset/000044) | [Grosmark e
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
grep -nE '^- id:|^  data:' claims/000947/*.yaml; sed -n 3399,3460p targets/dandisets.json | grep -n -i -A3 catalyst
```

```
40:- id: unit-link
44:  data: with_inputs
52:- id: table1-unit-counts
68:- id: table1-rest-rate
84:- id: table1-ap-width
101:- id: hold-period-ramps
119:- id: mvt-responsive-fraction
135:- id: increases-most-common
157:- id: monophasic-more-in-vla
171:- id: integrated-change-positive
189:- id: fig3a-vla-leads-gpi
206:- id: fig3b-gpi-decr-lag-vla-incr
220:- id: fig3c-vla-decr-lead-gpi-incr
234:- id: gating-conflict-fraction
247:- id: directional-units
262:- id: fig4-ccf-rare
274:- id: fig4-noise-corr-rare
285:- id: fig5-vla-decrease-after-gpi-bursts
297:- id: behavior-rt-mt
306:- id: figs3-emg-onset
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000947; wc -w *-report.md; cat author-report.md
```

```
1003 author-report.md
  686 author-revise-1-report.md
  568 author-revise-2-report.md
 1753 verifier-1-report.md
 1050 verifier-2-report.md
 5060 total
I did steps 1 to 6 for dandiset 000947 and Schwab et al. 2020. The entry passes `check` and runs from a clean environment in 687 s, and the handover is built in `executed/000947-schwab-2020/handover/`. I did not verify my own work, commit, or push. I used the paper's full text: it is open access in PLOS Biology, and I saved the JATS XML and a text copy under `paper/`. I pinned 0.240510.2211 because the paper cites no DANDI version and this is the only published version.

**1. Outcomes**

Of the 18 tested claims, 6 are reproduced, 5 partially reproduced and 7 not reproduced; 3 are blocked.

| Claim | Data | Outcome |
|---|---|---|
| unit-link | with_inputs | reproduced |
| table1-unit-counts | dandiset | not reproduced |
| table1-rest-rate | dandiset | reproduced |
| table1-ap-width | dandiset | reproduced |
| hold-period-ramps | dandiset | partially reproduced |
| mvt-responsive-fraction | dandiset | reproduced |
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000947; cat author-revise-1-report.md author-revise-2-report.md verifier-2-report.md
```

```
I've addressed all 14 problems and the 9 requested outputs. The entry re-ran cleanly with `python tools/entry.py all` in 798 s, `check` reports 0 errors, and nothing is committed.

**Outcome change**
- **behavior-rt-mt** goes from partially reproduced to reproduced. The verifier pointed out (problem 7) that the reaction-time ANOVA used all 250 pre-MPTP files, including M1, SMA and VLp-only files that are not part of the paper's data. Restricted to the 165 files that hold the GPi/VLa units analysed, reaction times differ neither between animals (p = 0.89) nor between directions (p = 0.41). Movement durations keep both effects. With the paper's own files the animal effect is p = 0.053. The all-files result stays as a variant, and the change is recorded as a deviation.
- The verifier agreed with the other 20 outcomes, and they are unchanged. Counts are now 7 reproduced, 4 partially reproduced, 7 not reproduced, 3 blocked.

**What I added to the notebook**
- **Chance level of the response detection**, measured on the real data with every trial aligned to a random time:
  - 62% of GPi and 71% of VLa units come out responsive by chance, against 98.5% and 97.5% in the data.
  - The hold-period slope test finds a slope in 98 to 99% of units by chance, the same as in the data. The hold-period-ramps notes now say those fractions do not separate ramps from noise. The test is the paper's own.
  - Many VLa decreases may be false positives, which is noted under fig3c.
- **One record per presumed neuron** for every claim, merging units with the same day, channel and sort letter. This merge also joins some units the paper kept apart (47 of the 117 multi-file groups). Onset and slope tests are also shown with one value per neuron. Fig3b keeps its lag, but its GPi median leaves the tolerance, so the notes now call that match fragile.
- **CCF (fig4-ccf-rare)**: an approximate c0 ≤ 0.3 exclusion as a variant, since the paper's simulation is not in its deposit. It gives KS p = 0.003, 0.
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000947; head -c 3500 verifier-1-report.md; grep -n -i 'denied\|fail\|could not\|timed out' verifier-1-report.md | head
```

```
**A. Outcomes**

The claims file lists 21 claims. The notebook tests 18 and marks 3 blocked; no separate attempt record was in the directory. My outcomes: 6 reproduced, 5 partially reproduced, 7 not reproduced, 3 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| unit-link | reproduced | 364 of 394 records found (92.4%). SDF r > 0.9 for 94.6% of 724 unit-directions (cell 17). Trial counts are equal for only 62.6%, and 25 of the matched paper-VLa units are labelled "Thalamus". |
| table1-unit-counts | not_reproduced | 268 GPi and 279 VLa units, against 209 and 185 or 218, all outside 10% (cell 19). Counting one unit per file counts a neuron recorded across several files more than once. The channel-per-day variant gives 132 and 186. |
| table1-rest-rate | reproduced | GPi 75.65 (tolerance band 63.1–77.1) and VLa 12.78 (12.15–14.85) spikes/s; rank sum p = 1e-171 (cell 21). The two animals differ in GPi (p = 0.04), where the paper says they are consistent. |
| table1-ap-width | reproduced | 0.247 and 0.509 ms, both in tolerance; p = 2.9e-37 (cell 23). |
| hold-period-ramps | partially_reproduced | The fractions, 98.5% and 98.6%, are in tolerance. The slopes differ between areas (rank sum p = 0.0415; means −0.60 and +0.23 against the paper's −0.05 and −0.14), which fails the no-difference condition (cell 25). The fraction also sits at its own chance level (problem 2). |
| mvt-responsive-fraction | reproduced | GPi 98.5%; VLa 97.5% is outside 88.1 ± 8.8 but inside the text's 94 ± 9.4, and either reading counts (cell 27). The chance level is high (problem 1). |
| increases-most-common | partially_reproduced | Monophasic increase is the most common form in both areas, and increases exceed 50% of changes. VLa monophasic increases (50.9 against 65.3) and VLa increases as a share of changes (60.2 against 68.8) are outside tolerance (cell 29). |
| monophasic-more-in-vla | not_reproduced | VLa 76.7% is outside 88.9 ± 8.9, and the difference is not significant (chi-squared p 
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 'statement:' claims/000947/*.yaml | grep -v criterion
```

```
41:  statement: The units the paper analysed can be found in the dandiset, and the dandiset's spike
42-    times and trials reproduce the per-unit peri-movement activity the paper's code stored.
43-  source: Data Availability; Dryad doi:10.5061/dryad.0cfxpnvxm, Gaia_Analy.mat and Isis_Analy.mat
44-  data: with_inputs
--
53:  statement: 209 single units met the criteria to be included as GPi neurons (105 in NHP G, 104 in
54-    NHP I) and 185 as VLa neurons (66 and 119).
55-  source: Results, first section; Table 1
56-  expected:
--
69:  statement: The resting firing rate of GPi neurons (mean 70.1 spikes/s) is significantly higher
70-    than that of VLa neurons (13.5 spikes/s), and the rates are consistent between the two animals.
71-  source: Results, first section; Table 1
72-  expected:
--
85:  statement: Action potentials of GPi neurons are shorter than those of VLa neurons (trough to
86-    peak 0.24 against 0.50 ms; rank sum p = 1e-33).
87-  source: Results, first section; Table 1
88-  expected:
--
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000947, Schwab et al. 2020

Six claims reproduced, four partially, seven not reproduced and one blocked
on the dandiset. With outside data, counted apart: one reproduced. Two claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 21 as
they then stood, but found that the reaction-time test of `behavior-rt-mt` ran
on all 250 pre-MPTP files with trials, including files with motor cortex, SMA
or VLp units only; restricted to the 165 files with units of the dandiset
rule, reaction times differ neither between the animals (p = 0.89) nor between
directions (p = 0.41), and the author changed the claim from partially
reproduced to reproduced. Round 2 agreed with all 21 and nothing was proposed,
so there was no third round. The paper reports single units in GPi and VLa of
two macaques (NHP G and NHP I) during reaching, compares the onset and sign of
their peri-movement changes with what gating of thalamus by GPi predicts, and
tests correlations between simultaneously recorded GPi and VLa units, the VLa
rate after GPi bursts and pauses, and a model thalamocortical cell. The link
to the paper's unit list, the unit counts, rest rates, spike widths,
hold-period ramps, responsive fractions, response forms, integrated change,
onset latencies, the gating conflict fraction, directional units, spike and
noise correlations, the VLa rate after bursts and the behaviour were tested,
on units chosen by a rule built from the dandiset's location labels and the
Methods' criteria, with the paper's unit list shown as a variant only. The
VLa localization is blocked as `data_missing`, since the stimulation mapping
is not public, the EMG onset as `methods_underspecified` and the simulation
as `other`. Some outcomes rest on weak ground: four depend on the selection of
units, as with the paper's records `hold-period-ramps`,
`monophasic-more-in-vla` and `fig3a-vla-leads-gpi` would be reproduced and
`fig3b-gpi-decr-lag-vla-incr` partially reproduced; in
`fig3b-gpi-decr-lag-vla-incr` the GPi median is 0.2 ms inside its tolerance;
the hold-period fractions and the 95.4% of comparisons that conflict with
gating equal their chance levels (98.4% and 99.0% with random alignment, 95.1%
with shuffled onsets); with random alignment the detector finds a decrease in
33.7% of VLa unit-directions (44.2% in the data), which may pull the VLa
decrease onsets of `fig3c-vla-decr-lead-gpi-incr` late; and in
`fig5-vla-decrease-after-gpi-bursts` bursts last 67.1 ms against the paper's
24 ms and the per-pair test is at chance, so that outcome says little about the
paper's finding. The author used the open access full text, and took the
paper's unit list and analysis code from its Dryad deposit, read from the
Zenodo mirror (record 4000719) as the Dryad download API requires a token.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
It holds more GPi and VLa units than the paper analysed (268 GPi and 279 VLa
units under its own labels and the Methods' rate criteria, against 209 and
185) and does not say which units the paper kept; the paper's unit list is
only in its Dryad deposit. No identifier links a neuron recorded over
consecutive files: 97 of the paper's 394 units span 2 to 5 files, and the
dandiset stores them as separate units. Location labels are inconsistent: GPi
and VLa are written GPI and VLA in some files, 54 Gaia thalamic units are
labelled only "Thalamus" (25 of them are VLa units in the paper), and 33 Isis
units have an empty location and no channel id. 30 of the 394 units the paper
analysed are not among the curated units, and 21 of 254 pre-MPTP files have no
curated units; 13 of them hold sorted clusters in processing/ecephys/units
(124 in all) whose only columns are spike times, unit name and location, and 8
have no such table. The electrode coordinates put the electrodes labelled VLa
ventral of those labelled VLp, if z is ventral positive as the column
description says, where the paper places VLa dorsal of VLp, and the files do
not say how the labels were assigned. Other findings: in all 254 pre-MPTP
files the session_start_time is two days after the date in the session_id;
sort labels are letters in some files and numbers in others, and the unit
quality column is missing from some files and holds free text (for example
"B -> C") in others; error trials are flagged only in the 127 of 253 files
with trials that have an error_onset_time column, and movement ends are
missing from 87 files, all of them Gaia, so the Methods' trial exclusion can
be applied only in part; I-160616-4 has no trials table, though it has 5
curated units and raw data, and one spike train is stored twice in I-170518-2,
as two M1-S units on channels 40 and 43; the pre-MPTP files name the paper only
by its bioRxiv preprint; the EMG of S3 Fig is in the Dryad deposit and not in
the dandiset; and the paper gives 218 VLa units and 94% responsive VLa units
in the Results where Table 1 gives 185 and 88.1%, and Fig 3C onsets of -62 and
-108 ms where Table 1 gives -76 and -95.5 ms.

The notebook ran in 687 s in the first clean run, `tools/entry.py all` took
798 s after round 1, and the notebook ran in 18.9 minutes after round 2. A
first run computed the burst surprise with log10, which gave bursts far longer
than the paper's, and the natural log was then used, with log10 kept as a
variant; a first burst control that did not keep the shifted events in rest
periods was fixed before the conclusions were written. Round 2 found
statements the outputs did not support, among them that two outcomes depend
on the selection of units where four do, the README run time and two findings
with no output behind them, and these were corrected; in the revision the
author also found that I-160616-4 has curated units and raw data, which the
record had denied. A Zenodo search command was denied by the permission system
and rerun without the `rm` it included, and untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: whether the paper's unit list, a selection of units, may be used
as an outside input; a Dryad download that needs a token; no null for the
clock check of spikes with a trial table, as shifted labels and offsets both
carry the target's effect; no data category for a simulation; a criterion that
defines only the reproduced case; a method error found after a first run; a
control first run not as the criterion stated; and no rule for a reported
fraction that matches its chance level.
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
sed -i 's/curated units and raw data, which the$/curated units and raw data, which the/; s/^record had denied\. A Zenodo search command was denied by the permission system$/record had said it lacked. A Zenodo search command was denied by the permission/; s/^and rerun without the `rm` it included, and untracked files in the repository$/system and rerun without the `rm` it included, and untracked files in the repository/' docs/pilot-notes.md; sed -n '/^### 000947/,$p' docs/pilot-notes.md | grep -n -E '—|rather|denied|lacked'
```

```
83:record had said it lacked. A Zenodo search command was denied by the permission
```

**Agent calls Bash**

```bash
sed -n '/^### 000947/,$p' docs/pilot-notes.md | sed -n 80,87p
```

```
on the selection of units where four do, the README run time and two findings
with no output behind them, and these were corrected; in the revision the
author also found that I-160616-4 has curated units and raw data, which the
record had said it lacked. A Zenodo search command was denied by the permission
system and rerun without the `rm` it included, and untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: whether the paper's unit list, a selection of units, may be used
as an outside input; a Dryad download that needs a token; no null for the
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='docs/pilot-notes.md'; s=open(p).read()
s=s.replace("system and rerun without the `rm` it included, and untracked files in the repository\nroot that the author did not create were left alone.","system and rerun without the `rm` it included, and untracked files in the\nrepository root that the author did not create were left alone.")
open(p,'w').write(s)
EOF
git diff --stat
```

```
README.md           |  1 +
 docs/pilot-notes.md | 93 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 94 insertions(+)
```

**Agent**

I ran `tools/readme_row.py 000947 --write`, which added the row `6 (+1) | 4 | 7 | 1` to README.md, and appended this subsection to the end of docs/pilot-notes.md. Nothing is committed.

### 000947, Schwab et al. 2020

Six claims reproduced, four partially, seven not reproduced and one blocked
on the dandiset. With outside data, counted apart: one reproduced. Two claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 21 as
they then stood, but found that the reaction-time test of `behavior-rt-mt` ran
on all 250 pre-MPTP files with trials, including files with motor cortex, SMA
or VLp units only; restricted to the 165 files with units of the dandiset
rule, reaction times differ neither between the animals (p = 0.89) nor between
directions (p = 0.41), and the author changed the claim from partially
reproduced to reproduced. Round 2 agreed with all 21 and nothing was proposed,
so there was no third round. The paper reports single units in GPi and VLa of
two macaques (NHP G and NHP I) during reaching, compares the onset and sign of
their peri-movement changes with what gating of thalamus by GPi predicts, and
tests correlations between simultaneously recorded GPi and VLa units, the VLa
rate after GPi bursts and pauses, and a model thalamocortical cell. The link
to the paper's unit list, the unit counts, rest rates, spike widths,
hold-period ramps, responsive fractions, response forms, integrated change,
onset latencies, the gating conflict fraction, directional units, spike and
noise correlations, the VLa rate after bursts and the behaviour were tested,
on units chosen by a rule built from the dandiset's location labels and the
Methods' criteria, with the paper's unit list shown as a variant only. The
VLa localization is blocked as `data_missing`, since the stimulation mapping
is not public, the EMG onset as `methods_underspecified` and the simulation
as `other`. Some outcomes rest on weak ground: four depend on the selection of
units, as with the paper's records `hold-period-ramps`,
`monophasic-more-in-vla` and `fig3a-vla-leads-gpi` would be reproduced and
`fig3b-gpi-decr-lag-vla-incr` partially reproduced; in
`fig3b-gpi-decr-lag-vla-incr` the GPi median is 0.2 ms inside its tolerance;
the hold-period fractions and the 95.4% of comparisons that conflict with
gating equal their chance levels (98.4% and 99.0% with random alignment, 95.1%
with shuffled onsets); with random alignment the detector finds a decrease in
33.7% of VLa unit-directions (44.2% in the data), which may pull the VLa
decrease onsets of `fig3c-vla-decr-lead-gpi-incr` late; and in
`fig5-vla-decrease-after-gpi-bursts` bursts last 67.1 ms against the paper's
24 ms and the per-pair test is at chance, so that outcome says little about the
paper's finding. The author used the open access full text, and took the
paper's unit list and analysis code from its Dryad deposit, read from the
Zenodo mirror (record 4000719) as the Dryad download API requires a token.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
It holds more GPi and VLa units than the paper analysed (268 GPi and 279 VLa
units under its own labels and the Methods' rate criteria, against 209 and
185) and does not say which units the paper kept; the paper's unit list is
only in its Dryad deposit. No identifier links a neuron recorded over
consecutive files: 97 of the paper's 394 units span 2 to 5 files, and the
dandiset stores them as separate units. Location labels are inconsistent: GPi
and VLa are written GPI and VLA in some files, 54 Gaia thalamic units are
labelled only "Thalamus" (25 of them are VLa units in the paper), and 33 Isis
units have an empty location and no channel id. 30 of the 394 units the paper
analysed are not among the curated units, and 21 of 254 pre-MPTP files have no
curated units; 13 of them hold sorted clusters in processing/ecephys/units
(124 in all) whose only columns are spike times, unit name and location, and 8
have no such table. The electrode coordinates put the electrodes labelled VLa
ventral of those labelled VLp, if z is ventral positive as the column
description says, where the paper places VLa dorsal of VLp, and the files do
not say how the labels were assigned. Other findings: in all 254 pre-MPTP
files the session_start_time is two days after the date in the session_id;
sort labels are letters in some files and numbers in others, and the unit
quality column is missing from some files and holds free text (for example
"B -> C") in others; error trials are flagged only in the 127 of 253 files
with trials that have an error_onset_time column, and movement ends are
missing from 87 files, all of them Gaia, so the Methods' trial exclusion can
be applied only in part; I-160616-4 has no trials table, though it has 5
curated units and raw data, and one spike train is stored twice in I-170518-2,
as two M1-S units on channels 40 and 43; the pre-MPTP files name the paper only
by its bioRxiv preprint; the EMG of S3 Fig is in the Dryad deposit and not in
the dandiset; and the paper gives 218 VLa units and 94% responsive VLa units
in the Results where Table 1 gives 185 and 88.1%, and Fig 3C onsets of -62 and
-108 ms where Table 1 gives -76 and -95.5 ms.

The notebook ran in 687 s in the first clean run, `tools/entry.py all` took
798 s after round 1, and the notebook ran in 18.9 minutes after round 2. A
first run computed the burst surprise with log10, which gave bursts far longer
than the paper's, and the natural log was then used, with log10 kept as a
variant; a first burst control that did not keep the shifted events in rest
periods was fixed before the conclusions were written. Round 2 found
statements the outputs did not support, among them that two outcomes depend
on the selection of units where four do, the README run time and two findings
with no output behind them, and these were corrected; in the revision the
author also found that I-160616-4 has curated units and raw data, which the
record had said it lacked. A Zenodo search command was denied by the permission
system and rerun without the `rm` it included, and untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: whether the paper's unit list, a selection of units,
may be used as an outside input; a Dryad download that needs a token; no null
for the clock check of spikes with a trial table, as shifted labels and
offsets both carry the target's effect; no data category for a simulation; a
criterion that defines only the reproduced case; a method error found after a
first run; a control first run not as the criterion stated; and no rule for a
reported fraction that matches its chance level.

## End of run

15 turns, 2 minutes, result: success.
