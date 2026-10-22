# 001636 · recorder · run 38838234746

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001636 --write; echo EXIT $?; git diff; ls claims/001636 transcripts/001636; cat attempts/001636-pasquereau-2013-01.yaml
```

```
<persisted-output>
Output too large (46.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d27277f8-29b6-4b6d-b305-53185bfd1d12/tool-results/b1a6p7sxj.txt

Preview (first 2KB):
EXIT 0
diff --git a/README.md b/README.md
index 13a27bb..2b0abbb 100644
--- a/README.md
+++ b/README.md
@@ -64,6 +64,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 8 | [`001933-chen-2026`](entries/001933-chen-2026) |
 | [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
 | [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
+| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001636:
10.3389-fnsys.2013.00098.yaml

[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,62p README.md; cat attempts/001636-pasquereau-2013-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6
```

```
<persisted-output>
Output too large (48.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d27277f8-29b6-4b6d-b305-53185bfd1d12/tool-results/b38kkhxka.txt

Preview (first 2KB):
- [`claims/`](claims): for each target attempted, the findings of the paper
  that were tested.
- [`attempts/`](attempts): one record per attempt, with an outcome for each
  claim, whether or not it worked.
- [`entries/`](entries): the notebooks.
- [`schemas/`](schemas): draft schemas for the files above.

## Attempts so far

| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
|---|---|---|---|---|---|---|
| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
| [000207](https://dandiarchive.org/dandiset/000207) | [Zheng et al. 2022](https://doi.org/10.1038/s41593-022-01020-w) | 5 | 1 | 0 | 14 | [`000207-zheng-2022`](entries/000207-zheng-2022) |
| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
it=d.values() if isinstance(d,dict) else d
[print(json.dumps(x,indent=1)) for x in it if '001636' in json.dumps(x)]"
```

```
<persisted-output>
Output too large (172.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d27277f8-29b6-4b6d-b305-53185bfd1d12/tool-results/bnftrvvxs.txt

Preview (first 2KB):
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
[... 63 more lines not kept]
```

**Agent**

Outputs are large; I'll read the pieces directly.

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
[print(json.dumps(x,indent=1)) for x in d if x['dandiset']=='001636']"; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md attempts/001636-pasquereau-2013-01.yaml claims/001636/*.yaml transcripts/001636/*report.md transcripts/001636/author-interrupted.md
```

```
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    [print(json.dumps(x,indent=1)) for x in d if x['dandiset']=='001636']
                                                 ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
826:### 001616, Gerken et al. 2025
863:### 001754 again, on the fixed draft (2026-10-15)
904:### 002014, Choi et al. 2025
937:### 001933, Chen et al. 2026
991:### 000004, Chandravadia et al. 2020
1028:### 002013, Amjad et al. 2025
  1064 docs/pilot-notes.md
   823 attempts/001636-pasquereau-2013-01.yaml
   594 claims/001636/10.3389-fnsys.2013.00098.yaml
    54 transcripts/001636/author-report.md
    33 transcripts/001636/author-revise-1-report.md
    20 transcripts/001636/author-revise-2-report.md
    60 transcripts/001636/verifier-1-report.md
    78 transcripts/001636/verifier-2-report.md
  1301 transcripts/001636/author-interrupted.md
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
for k,v in (d.items() if isinstance(d,dict) else []):
  if isinstance(v,list):
    for x in v:
      if isinstance(x,dict) and x.get('dandiset')=='001636': print(json.dumps(x,indent=1))
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
{
 "dandiset": "001636",
 "name": "Pyramidal tract and corticostriatal neuron recordings in MPTP-treated macaque performing visuomotor tasks",
 "published_version": "0.260518.1819",
 "asset_count": 447,
 "size_gb": 6.42,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Macaca mulatta - Rhesus monkey"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.3389/fnsys.2013.00098",
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 826
}
```

```
826	### 001616, Gerken et al. 2025
827	
828	Six claims reproduced, five partially and nine blocked, all on the dandiset
829	alone. Totals match the paper (29 patients, 2,286 units), but the counts by
830	region do not, with no mapping between them. The paper's test of which
831	neurons respond is not calibrated on these data (it flags about as many
832	units at random times as at real onsets), and the dataset's own ZETA test,
833	which is calibrated, flags far fewer than the paper reports (79 against
834	1,025 for camera cuts), so the claims built on responsive units are
835	blocked as `methods_underspecified`. The decoding claims with the paper's
836	logistic regression reproduce; those about its LSTM were blocked or tested
837	with the logistic regression as a stand-in. Findings: spike times are
838	stored in milliseconds, which NWB does not allow; the face labels lack the
839	"excluded" state the Methods use; an earlier version held 28 recordings
840	twice; and the dataset's training code selects no hippocampal units,
841	because no unit is labelled `H`.
842	
843	The author's first revision took 3 hours 24 minutes, mostly running the
844	ZETA test on every unit, and moved two blocked claims to partially
845	reproduced, as the protocol allows after round 1. `check` then held those
[... 220 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001636; for f in author-report.md author-revise-1-report.md verifier-1-report.md author-revise-2-report.md verifier-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (29.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d27277f8-29b6-4b6d-b305-53185bfd1d12/tool-results/bkjs4x3kf.txt

Preview (first 2KB):
=== author-report.md
I've done protocol steps 1 to 6 for dandiset 001636, and `entry.py all` and `handover` pass. The verifier package is in `executed/001636-pasquereau-2013/handover/`. The main result: 4 claims reproduced, 3 partially, 3 not reproduced and 18 blocked, 17 of them because my response detection has a far higher false-positive rate than the paper's threshold implies.

**Inputs.** The paper is open access, so I used the full text and its supplementary data sheet (PMC3840326, saved under `paper/`). The supplementary table gives monkey V values separately, which I used as expected values. I pinned 0.260518.1819 because it is the only published version and the paper cites none.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cell-counts | reproduced |
| baseline-rate | reproduced |
| ptn-faster-than-csn | reproduced |
| emg-m2-larger | reproduced |
| antidromic-latency | partially reproduced (CSN test p = 0.018, threshold 0.0167) |
| emg-duration-longer | partially reproduced |
| emg-m1-weak | partially reproduced |
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d27277f8-29b6-4b6d-b305-53185bfd1d12/tool-results/bkjs4x3kf.txt"
}
```

```
1	=== author-report.md
2	I've done protocol steps 1 to 6 for dandiset 001636, and `entry.py all` and `handover` pass. The verifier package is in `executed/001636-pasquereau-2013/handover/`. The main result: 4 claims reproduced, 3 partially, 3 not reproduced and 18 blocked, 17 of them because my response detection has a far higher false-positive rate than the paper's threshold implies.
3	
4	**Inputs.** The paper is open access, so I used the full text and its supplementary data sheet (PMC3840326, saved under `paper/`). The supplementary table gives monkey V values separately, which I used as expected values. I pinned 0.260518.1819 because it is the only published version and the paper cites none.
5	
6	## 1. Outcomes
7	
8	| Claim | Outcome |
9	|---|---|
10	| cell-counts | reproduced |
11	| baseline-rate | reproduced |
12	| ptn-faster-than-csn | reproduced |
13	| emg-m2-larger | reproduced |
14	| antidromic-latency | partially reproduced (CSN test p = 0.018, threshold 0.0167) |
15	| emg-duration-longer | partially reproduced |
16	| emg-m1-weak | partially reproduced |
17	| kinematics-slower | not reproduced (post-MPTP movements are faster and larger) |
18	| kinematic-latency-unchanged | not reproduced |
19	| emg-onset-unchanged | not reproduced |
20	| monkey-l-perturbations | blocked: data missing |
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^[a-z_]*:' attempts/001636-pasquereau-2013-01.yaml; python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/001636-pasquereau-2013-01.yaml'))
for k in a:
  if k not in('outcomes','verifications'): print(k, yaml.safe_dump(a[k],width=200,allow_unicode=True))
for o in a['outcomes']: print(o['claim'],o['outcome'],o.get('reason',''))
E
```

```
1:schema_version: 1
2:id: 001636-pasquereau-2013-01
3:dandiset: "001636"
4:dandiset_version: 0.260518.1819
5:paper: doi:10.3389/fnsys.2013.00098
6:date: 2026-10-15
7:entry: 001636-pasquereau-2013
8:provenance:
16:outcomes:
329:findings:
387:verifications:
schema_version 1
...

id 001636-pasquereau-2013-01
...

dandiset '001636'

dandiset_version 0.260518.1819
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
head -40 claims/001636/10.3389-fnsys.2013.00098.yaml; tail -5 README.md | head -0
```

```
# Claims for Pasquereau & Turner (2013) on dandiset 001636.
# Source: the full text in PubMed Central (PMC3840326, open access, CC BY), read from its Methods,
# Results, Table 1 and figure legends, and its supplementary data sheet (DataSheet1.PDF), whose
# table gives the neuronal results for each monkey separately.
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata, the contents of the files, the counts of units by subject, MPTP state and projection
# type, the number of torque perturbations per direction (none in any monkey L file), the timing
# of the torque command against the trials table, the sign of the joint angle, which EMG channels
# hold data, and the cross-referenced and repeated files. These counts showed that the monkey V
# units with at least 5 perturbations per direction number 112 before and 159 after MPTP, with
# 49 and 54 PTNs and 31 and 48 CSNs, as in the supplementary table. No SDF, response detection,
# kinematic measure or EMG response had been computed.
#
# The dandiset marks no torque perturbation in any monkey L file, so every claim is tested on
# monkey V (elbow), and the expected values are the paper's monkey V values where it gives them
# (supplementary table). Where the paper gives only values pooled over both monkeys, these are
# the expected values and the difference is a deviation.
#
# Method choices fixed here where the Methods leave them open (also in the helper's docstring):
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001636, Pasquereau et al. 2013

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. Round 1 called `false-positive-rate` not
reproduced where the author had it blocked; the author kept it blocked under
the protocol's rule for a computed false-positive rate far from the paper's,
and round 2 accepted that and agreed with all 28 outcomes, so there was no
third round. The paper reports how pyramidal tract and corticostriatal
neurons in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP. Only monkey V can be tested. The cell
counts, resting rates, antidromic latencies, kinematics and EMG were tested;
17 claims are blocked as `methods_underspecified`, because the response
detection as described gives a false-positive rate of 0.22 against the 0.01
its threshold implies, which blocks that claim and the 15 that use the
detected responses, and because the paper does not define the single-trial
latencies of `trial-correlations`.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
No monkey L file marks a torque perturbation, the monkey L torque command is
NaN in every pre-MPTP file, and 15 of 51 post-MPTP monkey L files have no
analog data, so the monkey L half of the paper (115 and 73 cells) cannot be
tested. The torque command's 50 ms pulse has three sizes (about 46, 91 and
183 units above rest), the smallest in most pre-MPTP sessions (108 of 157)
and the largest in most post-MPTP sessions (129 of 141), where the paper
describes one 0.1 Nm impulse; the kinematic and EMG outcomes therefore
compare different stimuli and cannot be attributed to MPTP, and post-MPTP
movements are faster and larger, the opposite of the paper. The analog
streams are not on the clock of the trials and spikes and fall behind by up
to 365 ms within a session; moving each trial's segment to its start puts
the command step 4 to 7 ms after every labelled onset. Other findings: the
angle's reference frame says positive is extension where the data show
flexion; four monkey V files repeat a block of another file's trials, and in
two of them the same unit is stored twice with different projection types;
`unit_also_in_session_id` uses the wrong prefixes, 35 of its 43 references
name files not in the dandiset, and the others point to a different unit;
the dandiset description gives systemic MPTP, elbow movements for both
monkeys and 1993 for Leu, where the files and paper say intracarotid MPTP,
the wrist for monkey L and August 1992; monkey L analog is sampled at 100 Hz
against the paper's 200 Hz, and the EMG is stored in uncalibrated A/D units;
the torque onset comes 1.70 to 1.73 s after `center_target_appearance_time`
in 90% of monkey V perturbations, where the Methods put it 1 to 2 s after
center capture at random; and no analysis code is published. The paper
itself gives different pre-MPTP PTN and CSN resting rates in the text (16.3
and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and marks a CSN change p <
0.01 that its own counts give as p = 0.54.

An earlier author run, cut short by the session limit, had left a draft
helper and its transcript on the branch; the author read the end of that
transcript, replaced the helper, and flagged it as possible contamination of
the protocol-alone test. The author's other points on the protocol: the
paper states a per-comparison threshold, not a false-positive rate, and the
block that follows from treating it as one spreads to latency results that
match the paper; no rule for how to compute a false-positive rate; "the
stated spread" for a mean and SD over cells; supplementary material and a
dandiset that holds one of two subjects; counting each recording once
against matching counts that include duplicated units; a stimulus that
differs between conditions, which fits no finding kind; absence claims with
many tests; and no field in the attempt schema for the code repository and
commit read.
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

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and marks a CSN change p <\n0.01 that its own counts give as p = 0.54.",
 "new_string": "and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and Table 1 marks the CSN\nchange in the fraction of excitatory responses p < 0.01, where its own\ncounts give p = 0.54."
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
git diff --stat; tail -5 docs/pilot-notes.md
```

```
README.md           |  1 +
 docs/pilot-notes.md | 61 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 62 insertions(+)
dandiset that holds one of two subjects; counting each recording once
against matching counts that include duplicated units; a stimulus that
differs between conditions, which fits no finding kind; absence claims with
many tests; and no field in the attempt schema for the code repository and
commit read.
```

**Agent**

I ran `tools/readme_row.py 001636 --write`, which added the 001636 row to README.md (4 reproduced, 3 partially, 3 not reproduced, 18 blocked). I then added this subsection at the end of docs/pilot-notes.md. Nothing is committed.

### 001636, Pasquereau et al. 2013

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. Round 1 called `false-positive-rate` not
reproduced where the author had it blocked; the author kept it blocked under
the protocol's rule for a computed false-positive rate far from the paper's,
and round 2 accepted that and agreed with all 28 outcomes, so there was no
third round. The paper reports how pyramidal tract and corticostriatal
neurons in the primary motor cortex of two monkeys respond to torque
perturbations before and after MPTP. Only monkey V can be tested. The cell
counts, resting rates, antidromic latencies, kinematics and EMG were tested;
17 claims are blocked as `methods_underspecified`, because the response
detection as described gives a false-positive rate of 0.22 against the 0.01
its threshold implies, which blocks that claim and the 15 that use the
detected responses, and because the paper does not define the single-trial
latencies of `trial-correlations`.

The dandiset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).
No monkey L file marks a torque perturbation, the monkey L torque command is
NaN in every pre-MPTP file, and 15 of 51 post-MPTP monkey L files have no
analog data, so the monkey L half of the paper (115 and 73 cells) cannot be
tested. The torque command's 50 ms pulse has three sizes (about 46, 91 and
183 units above rest), the smallest in most pre-MPTP sessions (108 of 157)
and the largest in most post-MPTP sessions (129 of 141), where the paper
describes one 0.1 Nm impulse; the kinematic and EMG outcomes therefore
compare different stimuli and cannot be attributed to MPTP, and post-MPTP
movements are faster and larger, the opposite of the paper. The analog
streams are not on the clock of the trials and spikes and fall behind by up
to 365 ms within a session; moving each trial's segment to its start puts
the command step 4 to 7 ms after every labelled onset. Other findings: the
angle's reference frame says positive is extension where the data show
flexion; four monkey V files repeat a block of another file's trials, and in
two of them the same unit is stored twice with different projection types;
`unit_also_in_session_id` uses the wrong prefixes, 35 of its 43 references
name files not in the dandiset, and the others point to a different unit;
the dandiset description gives systemic MPTP, elbow movements for both
monkeys and 1993 for Leu, where the files and paper say intracarotid MPTP,
the wrist for monkey L and August 1992; monkey L analog is sampled at 100 Hz
against the paper's 200 Hz, and the EMG is stored in uncalibrated A/D units;
the torque onset comes 1.70 to 1.73 s after `center_target_appearance_time`
in 90% of monkey V perturbations, where the Methods put it 1 to 2 s after
center capture at random; and no analysis code is published. The paper
itself gives different pre-MPTP PTN and CSN resting rates in the text (16.3
and 3.6 spikes/s) and Table 1 (18.3 and 3.2), and Table 1 marks the CSN
change in the fraction of excitatory responses p < 0.01, where its own
counts give p = 0.54.

An earlier author run, cut short by the session limit, had left a draft
helper and its transcript on the branch; the author read the end of that
transcript, replaced the helper, and flagged it as possible contamination of
the protocol-alone test. The author's other points on the protocol: the
paper states a per-comparison threshold, not a false-positive rate, and the
block that follows from treating it as one spreads to latency results that
match the paper; no rule for how to compute a false-positive rate; "the
stated spread" for a mean and SD over cells; supplementary material and a
dandiset that holds one of two subjects; counting each recording once
against matching counts that include duplicated units; a stimulus that
differs between conditions, which fits no finding kind; absence claims with
many tests; and no field in the attempt schema for the code repository and
commit read.

## End of run

14 turns, 1 minutes, result: success.
