# 000409 · recorder · run 39060368335

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000409 --write; echo EXIT $?; git diff; ls claims/000409/ transcripts/000409/; cat attempts/000409-ibl-2025-01.yaml
```

```
<persisted-output>
Output too large (51.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/add46b61-48f3-4e43-821a-8c9450d2c16a/tool-results/bnhnxbwg8.txt

Preview (first 2KB):
EXIT 0
diff --git a/README.md b/README.md
index cf2b4f8..0708629 100644
--- a/README.md
+++ b/README.md
@@ -81,6 +81,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000232](https://dandiarchive.org/dandiset/000232) | [Chang et al. 2023](https://doi.org/10.1101/2023.08.21.554194) | 19 | 7 | 2 | 1 | [`000232-chang-2023`](entries/000232-chang-2023) |
 | [000239](https://dandiarchive.org/dandiset/000239) | [Xu et al. 2022](https://doi.org/10.1038/s41586-022-04478-7) | 20 | 5 | 3 | 11 | [`000239-xu-2022`](entries/000239-xu-2022) |
 | [000350](https://dandiarchive.org/dandiset/000350) | [Mu et al. 2019](https://doi.org/10.1016/j.cell.2019.05.050) | 2 | 3 | 4 | 10 | [`000350-mu-2019`](entries/000350-mu-2019) |
+| [000409](https://dandiarchive.org/dandiset/000409) | [Ibl et al. 2025](https://doi.org/10.1038/s41586-025-09235-0) | 17 | 3 | 3 | 7 | [`000409-ibl-2025`](entries/000409-ibl-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000409/:
10.1038-s41586-025-09235-0.yaml

[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,82p README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; cat attempts/000409-ibl-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
x=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for e in (x if isinstance(x,list) else x.values()):
  if '000409' in json.dumps(e): print(json.dumps(e,indent=1))
"
```

```
<persisted-output>
Output too large (226.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/add46b61-48f3-4e43-821a-8c9450d2c16a/tool-results/buq9clpd6.txt

Preview (first 2KB):
| [001754](https://dandiarchive.org/dandiset/001754) | [Knierim et al. 2000](https://doi.org/10.1038/72910) | 3 | 0 | 1 | 3 | [`001754-knierim-2000`](entries/001754-knierim-2000) |
| [000130](https://dandiarchive.org/dandiset/000130) | [Sohn et al. 2019](https://doi.org/10.1016/j.neuron.2019.06.012) | 9 | 4 | 7 | 3 | [`000130-sohn-2019`](entries/000130-sohn-2019) |
| [001616](https://dandiarchive.org/dandiset/001616) | [Gerken et al. 2025](https://doi.org/10.7554/elife.106758.1) | 6 | 5 | 0 | 9 | [`001616-gerken-2025`](entries/001616-gerken-2025) |
| [002014](https://dandiarchive.org/dandiset/002014) | [Choi et al. 2025](https://doi.org/10.1016/j.jneumeth.2025.110467) | 4 | 1 | 0 | 8 | [`002014-choi-2025`](entries/002014-choi-2025) |
| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
| [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
| [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
| [000041](https://dandiarchive.org/dandiset/000041) | [Watson et al. 2016](https://doi.org/10.1016/j.neuron.2016.03.036) | 8 | 9 | 15 | 7 | [`000041-watson-2016`](entries/000041-watson-2016) |
| [000003](htt
[... 2 more lines not kept]
```

**Agent**

Outputs are large; I'll read them in pieces.

**Agent calls Bash**

```bash
grep -n 'Dandiset | Paper' -A2 README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md attempts/000409-ibl-2025-01.yaml claims/000409/*.yaml transcripts/000409/*report.md
```

```
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50-|---|---|---|---|---|---|---|
51-| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
1890:### 000213, Tingley et al. 2018
1975:### 000218, Tingley et al. 2019
2059:### 000226, Severson et al. 2017
2142:### 000232, Chang et al. 2023
2226:### 000239, Xu et al. 2022
2310:### 000350, Mu et al. 2019
  2392 docs/pilot-notes.md
   906 attempts/000409-ibl-2025-01.yaml
   410 claims/000409/10.1038-s41586-025-09235-0.yaml
    72 transcripts/000409/author-report.md
    38 transcripts/000409/author-revise-1-report.md
    23 transcripts/000409/author-revise-2-report.md
    12 transcripts/000409/author-revise-3-report.md
    60 transcripts/000409/verifier-1-report.md
    68 transcripts/000409/verifier-2-report.md
    25 transcripts/000409/verifier-3-report.md
  4006 total
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'));
x=d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,(list,dict)))
for e in (x if isinstance(x,list) else x.values()):
  if isinstance(e,dict) and str(e.get('id',e.get('dandiset','')))=='000409': print(json.dumps(e,indent=1))
" | head -60; python -c "import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
sed -n 1975,2392p docs/pilot-notes.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d['targets']:
  if '000409' in json.dumps(e)[:200]: print(json.dumps(e,indent=1)[:3000])
"
```

```
### 000218, Tingley et al. 2019

Four claims reproduced, seven partially, ten not reproduced and ten blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 30 of the 31; it gave
not reproduced for `fig5d-lag`, which the author kept at partially
reproduced because the coupling part of the claim holds and the lag part
does not. Round 2 disagreed on the same claim, since the criterion defines no
partial outcome, the author proposed not reproduced, and a third round agreed.
The paper reports high-frequency oscillations (HFOs) in the lateral septum
(LS) of rats, their relation to LS firing and to CA1 ripples across sleep and
waking, LS correlations before, during and after behaviour, which features of
ripples predict LS firing, optogenetic experiments and a network model. The
dataset counts, the HFOs in each animal and their count, participation and
phase locking, HFO duration and frequency against ripples, the link between
amplitude and frequency, confinement to LS, the excess correlations and their
compression, the rise in LS rates after behaviour, HFO rates by state, the
lag and coupling with CA1 ripples, ripple-triggered firing, phase coherence,
and the prediction of LS firing from CA1 spikes, state and duration were
tested on events detected anew, as the files hold none, with `hpc` taken as
[... 428 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/000409/author-report.md transcripts/000409/verifier-1-report.md transcripts/000409/author-revise-1-report.md
```

```
I've done protocol steps 1 to 6 for dandiset 000409: the entry is `entries/000409-ibl-2025/`, the attempt record is `attempts/000409-ibl-2025-01.yaml`, and the handover package is in `executed/000409-ibl-2025/handover/`. I used the paper's full text, which is open access (CC BY 4.0); it is saved under `paper/`. I pinned 0.260309.1324, the only published version. The paper cites no DANDI version, and the draft holds the same 2,048 files. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| dataset-sessions-mice-labs (459 / 139 / 12) | reproduced |
| dataset-probes-units (699 insertions, 621,733 units) | reproduced |
| well-isolated-neurons (75,708) | reproduced |
| canonical-regions (201 regions, 62,857 neurons; every inclusion step matches) | reproduced |
| brain-areas-279 | reproduced |
| mice-sex (94 male / 45 female) | reproduced |
| mice-age-weight | partially reproduced: weight matches; age at recording is 13 to 66 weeks, the paper says up to 178 |
| probe-versions (109 / 586 / 4) | reproduced |
| trials-per-session | reproduced |
| rf-mapping | blocked, data_missing |
| behav-performance (81.4% correct) | reproduced (mean over sessions, 81.58%) |
| behav-zero-contrast (58.7%, t = 20.18) | partially reproduced (58.26%, t138 = 19.68) |
| behav-early-movements (22.8% under 80 ms) | reproduced (22.75%) |
| fig1d, fig1ef, fig1g, fig1h | reproduced (fig1g only under reading b, 9.9 trials) |
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/000409/verifier-2-report.md transcripts/000409/author-revise-2-report.md transcripts/000409/verifier-3-report.md transcripts/000409/author-revise-3-report.md
```

```
**Round 2 verification: doi:10.1038/s41586-025-09235-0 on DANDI 000409 (0.260309.1324)**

Counts come from the files. The claims file has 30 claims. The attempt record now gives 17 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked. Since round 1, traj-stim-regions has moved from blocked to not reproduced. Cell indices below refer to the re-executed notebook, which has been renumbered since round 1. I did not download the paper this round: every check here is against the notebook's printed outputs and the criteria in the claims file.

**1. Outcomes**

I agree with 29 of the 30 stated outcomes. I disagree with one:

- **behav-zero-contrast** (record: partially reproduced; mine: not reproduced). The criterion defines only the reproduced case: both values within tolerance under one reading. Every other criterion in the file with two parts defines a partial case explicitly, and this one does not. Neither reading meets it (cell 48). With the 454 canonical sessions the mean is still 58.27%, so the miss of 0.04 points beyond the tolerance stands.

Notes on outcomes I agree with:

- **traj-stim-regions** (not reproduced): I agree. The criterion was written after round 1, but the counts are far from the target whichever choice is made: 46 under reading (a), 62 under (b), 46 to 53 in the variants, against 104 ± 10.4 (cell 99).
- **fig1g-block-switch** and **behav-performance** (reproduced) each pass under only one of the readings the criterion allows:
  - fig1g-block-switch: 75.9% of bootstrap resamples fall within 4.5 to 11 (cell 60).
  - behav-performance: the reading that passes, the mean over sessions, is not the reading whose s.e.m. matches the paper's ± 0.4 (cell 45).

**2. Sentences the outputs do not support**

- **README, run time:** "It takes about 26 minutes: 2 to scan … 1 to stream the spikes of the 14 regions … 12 to stream every canonical unit". The outputs show:
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p attempts/000409-ibl-2025-01.yaml
```

```
schema_version: 1
id: 000409-ibl-2025-01
dandiset: "000409"
dandiset_version: 0.260309.1324
paper: doi:10.1038/s41586-025-09235-0
date: '2026-10-17'
entry: 000409-ibl-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
- what: The paper's per-region results table brainwidemap/meta/region_info.csv (decoding effects and significance,
    single-cell fractions, trajectory significance, canonical flag), used only as the paper's reported values
    for comparison.
  source: https://github.com/int-brain-lab/paper-brain-wide-map at commit 118fc36cb3602934466ad2c6087c2b3b441f9f1f
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,560p attempts/000409-ibl-2025-01.yaml; grep -n '^[a-z_]*:' attempts/000409-ibl-2025-01.yaml
```

```
outcome: blocked
  blocked_by: other
  notes: Not attempted. The encoding model would be fitted to each of the 62,857 neurons with its leave-one-out
    refits, which needs every session's spikes and wheel traces.
- claim: video-correlates
  outcome: blocked
  blocked_by: other
  notes: Not attempted. It needs video pose and pupil series and every session's spikes; pose is present
    in 407 of 459 sessions.
- claim: granger-interactions
  outcome: blocked
  blocked_by: other
  notes: Not attempted. It needs every simultaneously recorded region pair of every session with 1,000
    permutations each.
findings:
- kind: metadata_error
  statement: In 64 sessions, all with the protocol name _iblrig_tasks_ephysChoiceWorld without a version
    (hausserlab 48, churchlandlab_ucla 13, mainenlab 2, cortexlab 1, recorded 2022-01-31 to 2023-10-19),
    probability_left alternates between 0.2 and 0.8 on every trial after the first 90, so block_index
    and block_type change on every trial. In these sessions the stimulus falls on the stated block's likely
[... 153 more lines not kept]
```

**Agent**

The README row is written (17 / 3 / 3 / 7). Now checking the claims file and the remaining verification records.

**Agent calls Bash**

```bash
sed -n 1,40p claims/000409/*.yaml; grep -n 'reviewed:\|date:\|by:' attempts/000409-ibl-2025-01.yaml | sed -n 1,20p; grep -n -i 'consortium\|international brain' -r docs/pilot-notes.md README.md | head
```

```
# Claims for International Brain Laboratory et al. (2025), A brain-wide map of neural activity
# during complex behaviour, Nature 645, 177-191, on dandiset 000409.
# Source: the full text of the version of record (open access, CC BY 4.0), read from the Results,
# figure legends and Methods. Supplementary information and Extended Data figures were not read
# beyond their legends.
#
# When these criteria were written the author had seen the data check only: the file list, the
# metadata, and a scan of every processed file (subjects, labs, probe models, trial counts per
# session, units and their quality scores and regions, the inclusion counts of the canonical set,
# the processing modules and passive protocols). In checking the trials table the author also saw
# that 22.75% of first movement times are below 80 ms (claim behav-early-movements), and the mapping
# of choice to reward. The author had read the paper's per-region table region_info.csv in the
# paper's repository (commit 118fc36), including its single-cell fractions for the regions the
# neural claims test, and its results tables meta/Results/*.pkl. No neural analysis had been run on
# the data, beyond timing one session to plan the run.
#
# The data check found that in 64 sessions (all with the protocol name _iblrig_tasks_ephysChoiceWorld
# without a version) probability_left alternates between 0.2 and 0.8 on every trial after the first
# 90 and does not follow the stimuli. The claims that use the block (fig1g-block-switch,
# fig1h-block-bias, the single-cell tests and the trajectory permutations) leave these sessions out.
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000409, International Brain Laboratory et al. 2025

Seventeen claims reproduced, three partially, three not reproduced and seven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 29 of the 30;
it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
author kept partially reproduced. Round 1 also found that
`traj-stim-regions`, left as not attempted, fits the time limit, so the
author wrote a criterion for it and tested it. Round 2 disagreed on the same
claim, since the criterion defines no partial outcome, the author proposed
not reproduced, and a third round agreed. The paper reports a brain-wide map
of neural activity in mice performing a visual decision task with a block
prior, from 459 sessions of 139 mice in 12 labs: the dataset and its
canonical set of 201 regions, task behaviour, decoding of stimulus, choice
and feedback, single-cell selectivity, neural trajectories and their
latencies, and a feedback oscillation tied to licking. The dataset counts,
mice, probes and trials, behaviour, decoding, trajectory latencies, the
number of regions with significant stimulus trajectories and the oscillation
were tested, the neural claims on VISp, GRN, IRN and seven regions drawn at
random, with one run of nested cross-validation and 100 null sessions
against the paper's 10 and 200. Receptive-field mapping is blocked as
`data_missing`; the two single-cell claims as `methods_underspecified`,
because the null run selects 2.7e-3 and 2.5e-3 of units against the paper's
5e-5, although all 14 regional stimulus fractions are within 0.02 of the
paper's table; and wheel-speed decoding, the encoding model, the video
correlates and the Granger interactions as `other`, not attempted. The
visual latencies are not reproduced (VISam 59.2 ms is not later than VISpm
61.3 ms), nor are the 104 +/- 10.4 regions with significant stimulus
trajectories (46 here). Some outcomes rest on weak ground:
`behav-performance` passes only on the mean over sessions, 81.58%, and not
on the mean over mice, whose s.e.m. of 0.43 matches the paper's +/- 0.4;
`fig1g-block-switch` passes only under reading (b), at 9.9 trials on the
point estimate, with 75.9% of resamples within 4.5 to 11; the stimulus
against choice margin of `dec-stim-restricted` and `dec-choice-widespread`
is one region and rests on CL, whose choice p of 0.0010 sits at the
2-session floor; `traj-latency-late` rests on the criterion's 0 to 150 ms
window, as in the paper's 0 to 100 ms window IRN has no latency and GRN is
at 100.0 ms; and `dec-feedback-nearly-all` could not reach the criterion's 9
of 10 regions, as the paper's own table marks 8 of these 10 significant. The
author used the open access version of record and took the paper's
per-region results and inclusion tables from its repository at commit
118fc36 as reported values only.

The dandiset was converted by CatalystNeuro (catalystneuro/IBL-to-nwb). It
holds every session, mouse, probe and unit the paper reports and every count
of its inclusion table, and no recording is deposited twice. In 64 sessions,
all with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a
version, `probability_left` alternates between 0.2 and 0.8 on every trial
after the first 90, so `block_index` and `block_type` change on every trial,
and the stimulus falls on the stated block's likely side in 47.5% to 57% of
biased trials against 75.9% to 82.8% in the other 395 sessions; these
sessions were left out of every analysis of the block prior. No session holds
the receptive-field mapping phase or its stimulus sequence, which the paper
ran in 504 of 699 insertions, and the saturation intervals of the IBL
aggregate trials table are not in the dandiset. The quality score and the
paper's 75,708 well-isolated units follow a noise cutoff below 5, where the
Methods give below 20 uV, which would give 95,430. Other findings:
`wheel_movement_onset_time` is described as after the go cue but precedes it
in 11.97% of trials; `reward_volume_uL` is 1.5 on every one of the 242,628
rewarded trials, against the Methods' 3 uL; the units description refers to
a `label` column that does not exist and calls all probes Neuropixels 1.0,
though four insertions used NP2010; subject weight is one value per mouse in
all its sessions; the paper's code takes age and weight from the IBL
database, while the ages at recording in the files are 13.1 to 65.9 weeks
against the Methods' 13 to 178, and it swaps the mean and median labels for
weight; the 81.4 +/- 0.4% correct is given as mean +/- s.d. but the 0.4 is
an s.e.m. (s.d. 5.12); the two single-cell tests are not independent, so the
paper's stated false-positive rate of 5e-5 understates it; `region_info.csv`
marks 210 regions canonical against 201; the paper's results table gives
visual latencies of 34.0, 44.7, 46.8, 59.6 and 66.0 ms against the text's
34, 42, 42, 57 and 78; the code's trajectory permutation classes and
Benjamini-Yekutieli correction differ from the Methods, though neither
brings the count near 104 (46 to 53); and the files hold spike sorting
revision 2025-05-06 where the code loads 2024-05-06, with identical counts.
The spikes share the trials' clock in 448 of the 454 canonical sessions, and
it could not be shown in 6.

Development runs failed on files without an `epochs` group, on mixed time
zones under pandas 3 and on a decoder that was not reproducible until the
liblinear seed was fixed, all fixed before the final run. Testing
`traj-stim-regions` raised the run time from about 11 to about 25 minutes
(1513 s in the last run), close to the 30-minute limit, so the nested null
was run only for VISp stimulus. Round 2 found the README run time and some
sentences of the notebook and record unsupported by the outputs, and these
were corrected. The author's points on the protocol: nothing covers a paper
whose own analysis cannot fit the time limit; no line between
`not_runnable` and not attempted; claims the criterion did not cover, one
with no measure in the paper and one whose criterion defined only the
reproduced case; no definition of a null rate far from the paper's, which
here blocks claims whose regional values match; whether the paper's results
tables count as outside inputs; no rule for data found wrong after the
criteria were written; a clock check that sessions with few loaded units
cannot pass; and a first author that is a consortium.
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

**Agent**

I added the 000409 row to README.md and appended the subsection below to the end of docs/pilot-notes.md. Nothing is committed, and the attempt, claims and entry are unchanged.

The README row names the paper "Ibl et al. 2025", because the first author is a consortium. For the heading I used the name the claims file gives, "International Brain Laboratory". There are also untracked files in the repository root that I didn't create (`.bashrc`, `.idea`, `scripts` and others); I left them alone.

### 000409, International Brain Laboratory et al. 2025

Seventeen claims reproduced, three partially, three not reproduced and seven
blocked, all on the dandiset. Round 1 gave its own outcome for each claim
from the notebook with its conclusions removed and agreed with 29 of the 30;
it gave not reproduced for `behav-zero-contrast`, whose mean of 58.26% misses
58.7 +/- 0.4 by 0.04 points while t138 = 19.68 is within tolerance, and the
author kept partially reproduced. Round 1 also found that
`traj-stim-regions`, left as not attempted, fits the time limit, so the
author wrote a criterion for it and tested it. Round 2 disagreed on the same
claim, since the criterion defines no partial outcome, the author proposed
not reproduced, and a third round agreed. The paper reports a brain-wide map
of neural activity in mice performing a visual decision task with a block
prior, from 459 sessions of 139 mice in 12 labs: the dataset and its
canonical set of 201 regions, task behaviour, decoding of stimulus, choice
and feedback, single-cell selectivity, neural trajectories and their
latencies, and a feedback oscillation tied to licking. The dataset counts,
mice, probes and trials, behaviour, decoding, trajectory latencies, the
number of regions with significant stimulus trajectories and the oscillation
were tested, the neural claims on VISp, GRN, IRN and seven regions drawn at
random, with one run of nested cross-validation and 100 null sessions
against the paper's 10 and 200. Receptive-field mapping is blocked as
`data_missing`; the two single-cell claims as `methods_underspecified`,
because the null run selects 2.7e-3 and 2.5e-3 of units against the paper's
5e-5, although all 14 regional stimulus fractions are within 0.02 of the
paper's table; and wheel-speed decoding, the encoding model, the video
correlates and the Granger interactions as `other`, not attempted. The
visual latencies are not reproduced (VISam 59.2 ms is not later than VISpm
61.3 ms), nor are the 104 +/- 10.4 regions with significant stimulus
trajectories (46 here). Some outcomes rest on weak ground:
`behav-performance` passes only on the mean over sessions, 81.58%, and not
on the mean over mice, whose s.e.m. of 0.43 matches the paper's +/- 0.4;
`fig1g-block-switch` passes only under reading (b), at 9.9 trials on the
point estimate, with 75.9% of resamples within 4.5 to 11; the stimulus
against choice margin of `dec-stim-restricted` and `dec-choice-widespread`
is one region and rests on CL, whose choice p of 0.0010 sits at the
2-session floor; `traj-latency-late` rests on the criterion's 0 to 150 ms
window, as in the paper's 0 to 100 ms window IRN has no latency and GRN is
at 100.0 ms; and `dec-feedback-nearly-all` could not reach the criterion's 9
of 10 regions, as the paper's own table marks 8 of these 10 significant. The
author used the open access version of record and took the paper's
per-region results and inclusion tables from its repository at commit
118fc36 as reported values only.

The dandiset was converted by CatalystNeuro (catalystneuro/IBL-to-nwb). It
holds every session, mouse, probe and unit the paper reports and every count
of its inclusion table, and no recording is deposited twice. In 64 sessions,
all with the protocol name `_iblrig_tasks_ephysChoiceWorld` without a
version, `probability_left` alternates between 0.2 and 0.8 on every trial
after the first 90, so `block_index` and `block_type` change on every trial,
and the stimulus falls on the stated block's likely side in 47.5% to 57% of
biased trials against 75.9% to 82.8% in the other 395 sessions; these
sessions were left out of every analysis of the block prior. No session holds
the receptive-field mapping phase or its stimulus sequence, which the paper
ran in 504 of 699 insertions, and the saturation intervals of the IBL
aggregate trials table are not in the dandiset. The quality score and the
paper's 75,708 well-isolated units follow a noise cutoff below 5, where the
Methods give below 20 uV, which would give 95,430. Other findings:
`wheel_movement_onset_time` is described as after the go cue but precedes it
in 11.97% of trials; `reward_volume_uL` is 1.5 on every one of the 242,628
rewarded trials, against the Methods' 3 uL; the units description refers to
a `label` column that does not exist and calls all probes Neuropixels 1.0,
though four insertions used NP2010; subject weight is one value per mouse in
all its sessions; the paper's code takes age and weight from the IBL
database, while the ages at recording in the files are 13.1 to 65.9 weeks
against the Methods' 13 to 178, and it swaps the mean and median labels for
weight; the 81.4 +/- 0.4% correct is given as mean +/- s.d. but the 0.4 is
an s.e.m. (s.d. 5.12); the two single-cell tests are not independent, so the
paper's stated false-positive rate of 5e-5 understates it; `region_info.csv`
marks 210 regions canonical against 201; the paper's results table gives
visual latencies of 34.0, 44.7, 46.8, 59.6 and 66.0 ms against the text's
34, 42, 42, 57 and 78; the code's trajectory permutation classes and
Benjamini-Yekutieli correction differ from the Methods, though neither
brings the count near 104 (46 to 53); and the files hold spike sorting
revision 2025-05-06 where the code loads 2024-05-06, with identical counts.
The spikes share the trials' clock in 448 of the 454 canonical sessions, and
it could not be shown in 6.

Development runs failed on files without an `epochs` group, on mixed time
zones under pandas 3 and on a decoder that was not reproducible until the
liblinear seed was fixed, all fixed before the final run. Testing
`traj-stim-regions` raised the run time from about 11 to about 25 minutes
(1513 s in the last run), close to the 30-minute limit, so the nested null
was run only for VISp stimulus. Round 2 found the README run time and some
sentences of the notebook and record unsupported by the outputs, and these
were corrected. The author's points on the protocol: nothing covers a paper
whose own analysis cannot fit the time limit; no line between
`not_runnable` and not attempted; claims the criterion did not cover, one
with no measure in the paper and one whose criterion defined only the
reproduced case; no definition of a null rate far from the paper's, which
here blocks claims whose regional values match; whether the paper's results
tables count as outside inputs; no rule for data found wrong after the
criteria were written; a clock check that sessions with few loaded units
cannot pass; and a first author that is a consortium.

## End of run

12 turns, 1 minutes, result: success.
