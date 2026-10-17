# 000239 · recorder · run 39035334487

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000239 --write; git diff; ls claims/000239 transcripts/000239; grep -n '^### ' docs/pilot-notes.md | tail -6
```

```
diff --git a/README.md b/README.md
index 54931c4..c06c195 100644
--- a/README.md
+++ b/README.md
@@ -79,6 +79,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000218](https://dandiarchive.org/dandiset/000218) | [Tingley et al. 2019](https://doi.org/10.1016/j.neuron.2019.10.012) | 4 | 7 | 10 | 10 | [`000218-tingley-2019`](entries/000218-tingley-2019) |
 | [000226](https://dandiarchive.org/dandiset/000226) | [Severson et al. 2017](https://doi.org/10.1016/j.neuron.2017.03.045) | 12 (+2) | 2 (+1) | 0 | 11 | [`000226-severson-2017`](entries/000226-severson-2017) |
 | [000232](https://dandiarchive.org/dandiset/000232) | [Chang et al. 2023](https://doi.org/10.1101/2023.08.21.554194) | 19 | 7 | 2 | 1 | [`000232-chang-2023`](entries/000232-chang-2023) |
+| [000239](https://dandiarchive.org/dandiset/000239) | [Xu et al. 2022](https://doi.org/10.1038/s41586-022-04478-7) | 20 | 5 | 3 | 11 | [`000239-xu-2022`](entries/000239-xu-2022) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000239:
10.1038-s41586-022-04478-7.yaml

transcripts/000239:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '1743,$p' docs/pilot-notes.md; grep -n -B3 '^| Dandiset' README.md | head; grep -n -A2 '| Dandiset' README.md | head -4
```

```
<persisted-output>
Output too large (32.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/b5bpa1egd.txt

Preview (first 2KB):
### 000121, Even-Chen et al. 2019

Six claims reproduced, seven partially, six not reproduced and one blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 19 of the 20; it
disagreed on `pca-variance`, where R's PC1 is 72.8% against a lower bound of
72.9%, and the author changed that claim from partially reproduced to not
reproduced, following the criterion's letter. The author also changed
`plane-timecourse` from reproduced to partially reproduced, because R's
divergence cannot be told from baseline noise; round 2 accepted this as a
judgment beyond the criterion and agreed with all 20 outcomes, and nothing
was proposed, so there was no third round. The paper reports the structure
and variability of delay activity in the dorsal premotor cortex (PMd) of two
monkeys, J and R, reaching to targets in four configurations: a plane in the
population activity that maps target position, its time course, how trial to
trial deviations along and off the plane relate to reach kinematics, and SVM
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/b5bpa1egd.txt"
}
```

```
1	### 000121, Even-Chen et al. 2019
2	
3	Six claims reproduced, seven partially, six not reproduced and one blocked,
4	all on the dandiset. Round 1 gave its own outcome for each claim from the
5	notebook with its conclusions removed and agreed with 19 of the 20; it
6	disagreed on `pca-variance`, where R's PC1 is 72.8% against a lower bound of
7	72.9%, and the author changed that claim from partially reproduced to not
8	reproduced, following the criterion's letter. The author also changed
9	`plane-timecourse` from reproduced to partially reproduced, because R's
10	divergence cannot be told from baseline noise; round 2 accepted this as a
11	judgment beyond the criterion and agreed with all 20 outcomes, and nothing
12	was proposed, so there was no third round. The paper reports the structure
13	and variability of delay activity in the dorsal premotor cortex (PMd) of two
14	monkeys, J and R, reaching to targets in four configurations: a plane in the
15	population activity that maps target position, its time course, how trial to
16	trial deviations along and off the plane relate to reach kinematics, and SVM
17	decoding of target direction and distance. The session configurations, trial
18	counts, delays and reaction times, the task-correlated channels, the PCA and
19	plane variance, the plane's time course, the on- and off-axis deviations, the
20	speed and distance axes, the ellipse orientation and the decoding errors were
[... 470 more lines not kept]
```

**Agent**

Now the sources.

**Agent calls Bash**

```bash
cat attempts/000239-xu-2022-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000239' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (57.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/bskvh9tuk.txt

Preview (first 2KB):
schema_version: 1
id: 000239-xu-2022-01
dandiset: "000239"
dandiset_version: 0.230607.1752
paper: doi:10.1038/s41586-022-04478-7
date: 2026-10-17
entry: 000239-xu-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
outcomes:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/bskvh9tuk.txt"
}
```

```
1	schema_version: 1
2	id: 000239-xu-2022-01
3	dandiset: "000239"
4	dandiset_version: 0.230607.1752
5	paper: doi:10.1038/s41586-022-04478-7
6	date: 2026-10-17
7	entry: 000239-xu-2022
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: ephys-unit-counts
18	  outcome: partially_reproduced
19	  notebook: reproduce_xu_2022.ipynb
20	  output: claim:ephys-unit-counts
[... 898 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000239; for f in author-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done; cd ../..; grep -n -B2 -A15 '"000239"' targets/dandisets.json | head -40
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/bh7461s3w.txt

Preview (first 2KB):
=== author-report.md
I've finished steps 1 to 6 for dandiset 000239. The entry passes `check` and runs from a clean environment, and the handover package is built in `executed/000239-xu-2022/handover/`. Nothing is committed.

I used the full text of the accepted author manuscript in PubMed Central (PMC9109820), fetched through NCBI efetch; the version of record is not open access. The Figure 3b R² values are printed only inside the figure, so I read them from the figure image on Nature's page. I pinned 0.230607.1752, the only published version (the paper cites none).

**1. Outcomes** (39 claims: 20 reproduced, 5 partially reproduced, 3 not reproduced, 11 blocked)

| Claim | Outcome |
|---|---|
| fig3-session-counts, fig3-units-per-session, fig3a-trial-count | reproduced |
| fig3c-length, -velocity, -angle, -identity, -time (all 20 R² values within the paper's SDs, order as stated) | reproduced |
| ed5b-variables-uncorrelated, ed5e-variance-explained (0.454, just inside 0.45–0.55), fig3e-cca | reproduced |
| fig4g-zigzag-context, ed7f-target-position-alm, ed7h-no-time-coding | reproduced |
| ed4o-rhythmicity, ed6-alm-reward-drop | reproduced |
| ed1h-sequence-duration (0.992 s, 17 mice), ed1l-learning-curves, ed2e-missed-licks, ed7b-correct-side | reproduced |
| ephys-unit-counts (339 multi-units, paper 303) | partially reproduced |
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/a8240138-dfa1-40df-807b-75dd45d226c2/tool-results/bh7461s3w.txt"
}
```

```
1	=== author-report.md
2	I've finished steps 1 to 6 for dandiset 000239. The entry passes `check` and runs from a clean environment, and the handover package is built in `executed/000239-xu-2022/handover/`. Nothing is committed.
3	
4	I used the full text of the accepted author manuscript in PubMed Central (PMC9109820), fetched through NCBI efetch; the version of record is not open access. The Figure 3b R² values are printed only inside the figure, so I read them from the figure image on Nature's page. I pinned 0.230607.1752, the only published version (the paper cites none).
5	
6	**1. Outcomes** (39 claims: 20 reproduced, 5 partially reproduced, 3 not reproduced, 11 blocked)
7	
8	| Claim | Outcome |
9	|---|---|
10	| fig3-session-counts, fig3-units-per-session, fig3a-trial-count | reproduced |
11	| fig3c-length, -velocity, -angle, -identity, -time (all 20 R² values within the paper's SDs, order as stated) | reproduced |
12	| ed5b-variables-uncorrelated, ed5e-variance-explained (0.454, just inside 0.45–0.55), fig3e-cca | reproduced |
13	| fig4g-zigzag-context, ed7f-target-position-alm, ed7h-no-time-coding | reproduced |
14	| ed4o-rhythmicity, ed6-alm-reward-drop | reproduced |
15	| ed1h-sequence-duration (0.992 s, 17 mice), ed1l-learning-curves, ed2e-missed-licks, ed7b-correct-side | reproduced |
16	| ephys-unit-counts (339 multi-units, paper 303) | partially reproduced |
17	| ed5f-axes-orthogonal (one pair at 0.302, bound 0.3) | partially reproduced |
18	| fig3f-backtracking-svm (S1TJ and S1BF also above chance) | partially reproduced |
19	| ed4m-active-neuron-counts (S1TJ 155, paper 119) | partially reproduced |
20	| ed4l-alm-initiation (ALM vs M1TJ p = 0.14) | partially reproduced |
[... 277 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1723,1745p targets/dandisets.json; head -c 3000 claims/000239/*.yaml; grep -n 'statement:' claims/000239/*.yaml | head -50
```

```
"papers": [
    {
     "doi": "10.1038/s41586-022-04478-7",
     "title": "Cortical processing of flexible and context-dependent sensorimotor sequences",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "contributor Tauffer, Luiz of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000243",
   "name": "MRI of human ex vivo brainstem",
   "published_version": null,
   "asset_count": 5,
   "size_gb": 6.08,
   "data_standards": [
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i 'tongue-jaw\|barrel\|anterolateral\|M1TJ (' claims/000239/*.yaml entries/000239-xu-2022/README.md | head; sed -n 1,40p entries/000239-xu-2022/README.md
```

```
claims/000239/10.1038-s41586-022-04478-7.yaml:20:# - Sessions of Figure 3 are the files whose description names ALM (13), M1TJ (9), S1TJ (8) and
# Xu, Dong, Chen, Delgado, Hughes, Zhang & O'Connor (2022) from dandiset 000239

Tests the findings of [Xu et al. (2022)](https://doi.org/10.1038/s41586-022-04478-7) that can be
tested on [DANDI:000239](https://dandiarchive.org/dandiset/000239/0.230607.1752), which holds the
trial tables of 33 mice in a sequence licking task, tongue tracking from video, and sorted spikes
in 93 files: 57 recording sessions in S1TJ, M1TJ, ALM, S1BF, M1B, S1L and the zigzag task, 22
recordings in other areas, and 14 recordings of the inhibition efficiency.

| Claim | Outcome |
|---|---|
| 1537 single and 303 multi-units from 57 sessions | Partially reproduced |
| Figure 3 session counts (8, 9, 13, 5) | Reproduced |
| 32 plus or minus 13 units per session | Reproduced |
| 2684 trials in Figure 3a | Reproduced |
| Decoding of L, L', theta, I and tau across S1TJ, M1TJ, ALM, S1BF (five claims) | Reproduced |
| The five behavioural variables are uncorrelated | Reproduced |
| Coding axes explain about half the variance of the top five PCs | Reproduced |
| Coding axes are largely orthogonal | Partially reproduced |
| Canonical correlation of coding and PC subspaces | Reproduced |
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000239, Xu et al. 2022

Twenty claims reproduced, five partially, three not reproduced and eleven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim from
the notebook with its conclusions removed and agreed with all 39; round 2
agreed again and nothing was proposed, so there was no third round. The paper
reports mice licking a port that moves through seven positions in standard,
backtracking and zigzag sequences, how population activity in S1TJ, M1TJ, ALM
and S1BF encodes tongue length, velocity and angle, sequence identity and
relative sequence time, and how optogenetic inhibition of these regions
changes licking. The unit and session counts, decoding of the five variables
and the relations among their coding axes, canonical correlation, decoding of
backtracking, zigzag context and the upcoming target position, the counts of
active neurons, initiation tuning, lick rhythmicity and the drop at water
contact, and the behavioural claims on sequence duration, learning,
backtracking, missed and consummatory licks and the starting side were tested.
The five optogenetic claims, the earplug, odour masking and tongue numbing
controls and the lick force are blocked as `metadata_insufficient`, inhibition
efficiency by cell type as `data_missing`, and the NNMF clustering as
`methods_underspecified`. Some outcomes rest on weak ground:
`fig3-units-per-session` is reproduced only on all 57 recording sessions, as
the 35 Figure 3 sessions the claim refers to give an SD of 14.4 against a
limit of 14.3; `ed5e-variance-explained` is 0.454 against a lower bound of
0.45 (0.453 to 0.455 over other seeds); in `ephys-unit-counts` three variants
of the unit classification put the multi-units inside tolerance (331, 309 and
295 against 339); the expected values of the five `fig3c` claims were read
from the Figure 3b image, which the verifiers could not check; in
`ed1l-proficiency-1500` proficiency had to be defined in the criterion and the
learning files may not start at the first day of training; and for
`ed2-backtracking-counts` a variant built after seeing the results, leaving
out 8 sessions with touches of a few ms, gives the paper's 47 sessions but 8
mice against 9. The author used the accepted author manuscript in PubMed
Central (PMC9109820), fetched through NCBI efetch after Europe PMC, BioC and
the PMC page failed, and read the Figure 3b values from the figure on Nature's
page.

The dandiset was converted by CatalystNeuro
(catalystneuro/oconnor-lab-to-nwb). The opto sessions do not name the
inhibited region: the 35 sessions at 4 mW and 25 at 2 mW, five per mouse,
carry only the light times and LED drive, the `opto` column (0, 1 and 2) and
the opto1 and opto2 series have no description, and no file has optogenetics
metadata, so Figure 2 and Extended Data Fig. 3j-m cannot be tested. The
control sessions do not mark the condition, which earplug session had
earplugs, which half of each air session had the air flow on, or which
numbing session was lidocaine; without the labels the paper's test finds an
earplug effect under 4 of 32 assignments and an air flow effect under 1 of 15.
The recorded area and the kind of session are given only by the session
description, the name of the lab's data folder, which is cut short ("... se")
in the files themselves; there is no electrodes table, unit location, depth or
quality label, and the area of the zigzag and "ephys others" sessions is not
given. Spike waveforms are not included, so units cannot be classified as
putative pyramidal or FS cells, and the fibre distance of the efficiency
recordings is not given. 1446 spike times in 35 files are duplicated within a
unit, which the Methods say were removed before analysis. Other findings: the
MX181003 learning file of 2018-10-02 15:30:57 repeats all 4028 touches of the
MX181002 file with the same start time and then continues, so it is unclear
which mouse it belongs to; in the 574 learning files start_time and stop_time
count from 0 while event times are on another clock (around 10^6 s); seqId in
the learning files holds the text of an unconverted MATLAB categorical object;
force sensor and lick port series are in volts without a calibration, tongue
landmarks are in pixels without a scale, and every trial column is described
as "no description"; the 8 sessions the Methods leave out for unregistered
touch offsets are not marked; and the paper says its MATLAB code is available
at GitHub but gives no address, and no repository was found. The session
groups of Figure 3, the 57 recording sessions, the 6 zigzag sessions from 3
mice and the 15 learning mice match the paper.

Threaded streaming was slow under h5py's global lock (15 minutes for an early
scan of all files), so the notebook uses processes, and an early trial filter
that wrongly required video before the cue was fixed before any claim was
judged; the seed and search variants added after round 1 raised the run time
to about 21 minutes, over the protocol's ten-minute aim. Untracked files in
the repository root that the author did not create were left alone. The
author's points on the protocol: nothing that stops outcomes being put in the
header table, which `handover` would not strip; whether numbers printed only
in a figure may serve as expected values; the paper's SD as tolerance for an
across-session mean, which is generous; a step that assumes the paper links
its code; an absence rule that assumes the paper names a test; whether an
undefined term like proficiency should be blocked or defined and tested; a
suggested clock check that is weak when sequences alternate direction; no rule
for a duplicate recording whose owner is unknown; a variant outside the
pre-registered readings that matches the paper; and a figure's p < 0.001 that
an exact paired permutation cannot reach with 8 sessions.
EOF
git status --short; grep -c '—\|rather' <(sed -n '/### 000239/,$p' docs/pilot-notes.md)
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
0
```

**Agent**

I ran `python tools/readme_row.py 000239 --write`, which added the row 20 | 5 | 3 | 11 for Xu et al. 2022 to README.md. I also added the subsection below to the end of docs/pilot-notes.md. Nothing is committed. The repository root has untracked dotfiles and a `scripts` folder that I did not create, and I left them alone.

### 000239, Xu et al. 2022

Twenty claims reproduced, five partially, three not reproduced and eleven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim from
the notebook with its conclusions removed and agreed with all 39; round 2
agreed again and nothing was proposed, so there was no third round. The paper
reports mice licking a port that moves through seven positions in standard,
backtracking and zigzag sequences, how population activity in S1TJ, M1TJ, ALM
and S1BF encodes tongue length, velocity and angle, sequence identity and
relative sequence time, and how optogenetic inhibition of these regions
changes licking. The unit and session counts, decoding of the five variables
and the relations among their coding axes, canonical correlation, decoding of
backtracking, zigzag context and the upcoming target position, the counts of
active neurons, initiation tuning, lick rhythmicity and the drop at water
contact, and the behavioural claims on sequence duration, learning,
backtracking, missed and consummatory licks and the starting side were tested.
The five optogenetic claims, the earplug, odour masking and tongue numbing
controls and the lick force are blocked as `metadata_insufficient`, inhibition
efficiency by cell type as `data_missing`, and the NNMF clustering as
`methods_underspecified`. Some outcomes rest on weak ground:
`fig3-units-per-session` is reproduced only on all 57 recording sessions, as
the 35 Figure 3 sessions the claim refers to give an SD of 14.4 against a
limit of 14.3; `ed5e-variance-explained` is 0.454 against a lower bound of
0.45 (0.453 to 0.455 over other seeds); in `ephys-unit-counts` three variants
of the unit classification put the multi-units inside tolerance (331, 309 and
295 against 339); the expected values of the five `fig3c` claims were read
from the Figure 3b image, which the verifiers could not check; in
`ed1l-proficiency-1500` proficiency had to be defined in the criterion and the
learning files may not start at the first day of training; and for
`ed2-backtracking-counts` a variant built after seeing the results, leaving
out 8 sessions with touches of a few ms, gives the paper's 47 sessions but 8
mice against 9. The author used the accepted author manuscript in PubMed
Central (PMC9109820), fetched through NCBI efetch after Europe PMC, BioC and
the PMC page failed, and read the Figure 3b values from the figure on Nature's
page.

The dandiset was converted by CatalystNeuro
(catalystneuro/oconnor-lab-to-nwb). The opto sessions do not name the
inhibited region: the 35 sessions at 4 mW and 25 at 2 mW, five per mouse,
carry only the light times and LED drive, the `opto` column (0, 1 and 2) and
the opto1 and opto2 series have no description, and no file has optogenetics
metadata, so Figure 2 and Extended Data Fig. 3j-m cannot be tested. The
control sessions do not mark the condition, which earplug session had
earplugs, which half of each air session had the air flow on, or which
numbing session was lidocaine; without the labels the paper's test finds an
earplug effect under 4 of 32 assignments and an air flow effect under 1 of 15.
The recorded area and the kind of session are given only by the session
description, the name of the lab's data folder, which is cut short ("... se")
in the files themselves; there is no electrodes table, unit location, depth or
quality label, and the area of the zigzag and "ephys others" sessions is not
given. Spike waveforms are not included, so units cannot be classified as
putative pyramidal or FS cells, and the fibre distance of the efficiency
recordings is not given. 1446 spike times in 35 files are duplicated within a
unit, which the Methods say were removed before analysis. Other findings: the
MX181003 learning file of 2018-10-02 15:30:57 repeats all 4028 touches of the
MX181002 file with the same start time and then continues, so it is unclear
which mouse it belongs to; in the 574 learning files start_time and stop_time
count from 0 while event times are on another clock (around 10^6 s); seqId in
the learning files holds the text of an unconverted MATLAB categorical object;
force sensor and lick port series are in volts without a calibration, tongue
landmarks are in pixels without a scale, and every trial column is described
as "no description"; the 8 sessions the Methods leave out for unregistered
touch offsets are not marked; and the paper says its MATLAB code is available
at GitHub but gives no address, and no repository was found. The session
groups of Figure 3, the 57 recording sessions, the 6 zigzag sessions from 3
mice and the 15 learning mice match the paper.

Threaded streaming was slow under h5py's global lock (15 minutes for an early
scan of all files), so the notebook uses processes, and an early trial filter
that wrongly required video before the cue was fixed before any claim was
judged; the seed and search variants added after round 1 raised the run time
to about 21 minutes, over the protocol's ten-minute aim. Untracked files in
the repository root that the author did not create were left alone. The
author's points on the protocol: nothing that stops outcomes being put in the
header table, which `handover` would not strip; whether numbers printed only
in a figure may serve as expected values; the paper's SD as tolerance for an
across-session mean, which is generous; a step that assumes the paper links
its code; an absence rule that assumes the paper names a test; whether an
undefined term like proficiency should be blocked or defined and tested; a
suggested clock check that is weak when sequences alternate direction; no rule
for a duplicate recording whose owner is unknown; a variant outside the
pre-registered readings that matches the paper; and a figure's p < 0.001 that
an exact paired permutation cannot reach with 8 sessions.

## End of run

11 turns, 1 minutes, result: success.
