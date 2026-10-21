# 001636 · verifier-2 · run 38784985252

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls -la && ls paper 2>/dev/null; cat round-1-report.md
```

```
total 656
drwxr-xr-x 5 runner runner    4096 Oct 15 18:24 .
drwxr-xr-x 7 runner runner    4096 Oct 15 18:24 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 15 18:24 .claude
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.development
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.local
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.production
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.test
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .env.test.local
drwx------ 2 runner runner    4096 Oct 15 18:24 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .github
-rw-r--r-- 1 runner runner       0 Oct 15 18:24 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 15 18:20 .mcp.json
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md; cat 001636-pasquereau-2013-01.yaml
```

```
<persisted-output>
Output too large (38.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8da8a53e-1ec7-4f54-978b-bded666955ce/tool-results/b93i9fzj1.txt

Preview (first 2KB):
# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.260518.1819), which holds
single-unit recordings from M1 of two monkeys before and after MPTP. Only monkey V can be tested:
the monkey L files mark no torque perturbation.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| Monkey V cell counts (112 and 159; PTNs 49 and 54; CSNs 31 and 48) | Reproduced |
| Lower resting rate after MPTP in PTNs, not CSNs | Reproduced |
| PTNs fire faster than CSNs at rest | Reproduced |
| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Pasquereau & Turner (2013) from dandiset 001636
2	
3	Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
4	can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.260518.1819), which holds
5	single-unit recordings from M1 of two monkeys before and after MPTP. Only monkey V can be tested:
6	the monkey L files mark no torque perturbation.
7	
8	A failure to reproduce here may be a failure of this attempt, not of the paper: see the
9	reasoning and the differences from the paper's method.
10	
11	| Claim | Outcome |
12	|---|---|
13	| Monkey V cell counts (112 and 159; PTNs 49 and 54; CSNs 31 and 48) | Reproduced |
14	| Lower resting rate after MPTP in PTNs, not CSNs | Reproduced |
15	| PTNs fire faster than CSNs at rest | Reproduced |
16	| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
17	| Long-latency (m2) triceps EMG larger after MPTP | Reproduced |
18	| EMG responses longer after MPTP | Partially reproduced |
19	| m1 EMG much smaller than m2 | Partially reproduced |
20	| Torque-induced movements slower and smaller after MPTP | Not reproduced |
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "001636-pasquereau-2013-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001636-pasquereau-2013-01
3	dandiset: "001636"
4	dandiset_version: 0.260518.1819
5	paper: doi:10.3389/fnsys.2013.00098
6	date: 2026-10-15
7	entry: 001636-pasquereau-2013
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-6
16	outcomes:
17	- claim: cell-counts
18	  outcome: reproduced
19	  notebook: reproduce_pasquereau_2013.ipynb
20	  output: claim:cell-counts
[... 599 more lines not kept]
```

**Agent calls Bash**

```bash
cat 10.3389-fnsys.2013.00098.yaml | head -150; grep -c "^- id\|^  - id" 10.3389-fnsys.2013.00098.yaml; grep -n "id:" 10.3389-fnsys.2013.00098.yaml
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
[... 159 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.3389-fnsys.2013.00098.yaml",
 "offset": 150
}
```

```
150	  - quantity: PTN antidromic latency post-MPTP
151	    value: 1.9
152	    tolerance: 0.2
153	    unit: ms
154	  - quantity: CSN antidromic latency pre-MPTP
155	    value: 5.1
156	    tolerance: 0.61
157	    unit: ms
158	  - quantity: CSN antidromic latency post-MPTP
159	    value: 6.1
160	    tolerance: 0.89
161	    unit: ms
162	  depends_on:
163	  - cell-counts
164	  criterion: Antidromic latency of monkey V PTNs and CSNs studied (the expected values pool both
165	    monkeys). Reproduced when the CSN latency is longer after MPTP (Mann-Whitney p < 0.05/3),
166	    the PTN latency does not differ (p >= 0.05), and the four means are within tolerance.
167	    Partially reproduced when the two tests hold and a mean does not, or the reverse. A variant
168	    adds every monkey L PTN and CSN unit, as their selection by perturbations cannot be made.
169	- id: false-positive-rate
[... 426 more lines not kept]
```

**Agent**

Claims file has 28 claims and the attempt record has 28 outcomes. Now extracting the notebook's cells and outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
out=[]
for i,c in enumerate(nb['cells']):
    out.append(f"\n=== CELL {i} [{c['cell_type']}] ===")
    out.append(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: out.append('--OUT--\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']:
            if 'image/png' in o['data']: out.append('--IMG--')
            else: out.append('--OUT--\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': out.append('--ERR--'+o['ename'])
open('nb.txt','w').write('\n'.join(out))
print(len(nb['cells']))
EOF
wc -l nb.txt
```

```
105
2380 nb.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 1,700p nb.txt
```

```
<persisted-output>
Output too large (46.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8da8a53e-1ec7-4f54-978b-bded666955ce/tool-results/be4lk9lxw.txt

Preview (first 2KB):
=== CELL 0 [markdown] ===
# Reproducing Pasquereau & Turner (2013) from dandiset 001636

**Paper.** Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
neuronal responses to muscle stretch. *Frontiers in Systems Neuroscience* 7:98.
[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098). This attempt used the
full text (open access, PubMed Central PMC3840326) and its supplementary data sheet, whose table
gives the neuronal results of each monkey separately.

**Dandiset.** [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.260518.1819), version
0.260518.1819. The paper (2013) cites no DANDI version. This is the only published version, and
the draft differs from it only by its modification date, so it is the version pinned here. The
dandiset holds single-unit M1 recordings from two monkeys before and after MPTP, from which three
papers were written; this one uses the torque perturbation (muscle stretch) trials.

**What can be tested.** The files of monkey V (Venus, elbow) mark the torque perturbations, with
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	
2	=== CELL 0 [markdown] ===
3	# Reproducing Pasquereau & Turner (2013) from dandiset 001636
4	
5	**Paper.** Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
6	neuronal responses to muscle stretch. *Frontiers in Systems Neuroscience* 7:98.
7	[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098). This attempt used the
8	full text (open access, PubMed Central PMC3840326) and its supplementary data sheet, whose table
9	gives the neuronal results of each monkey separately.
10	
11	**Dandiset.** [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.260518.1819), version
12	0.260518.1819. The paper (2013) cites no DANDI version. This is the only published version, and
13	the draft differs from it only by its modification date, so it is the version pinned here. The
14	dandiset holds single-unit M1 recordings from two monkeys before and after MPTP, from which three
15	papers were written; this one uses the torque perturbation (muscle stretch) trials.
16	
17	**What can be tested.** The files of monkey V (Venus, elbow) mark the torque perturbations, with
18	the joint angle, the torque command and triceps EMG. The files of monkey L (Leu, wrist) mark none,
19	so every claim is tested on monkey V alone, against the paper's monkey V values where it gives
20	them (supplementary table) and against its pooled values otherwise.
[... 818 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 838,
 "limit": 560
}
```

```
838	=== CELL 24 [markdown] ===
839	### `monkey-l-perturbations`
840	
841	> In monkey L, 57 of 115 neurons before MPTP and 35 of 73 after responded to torque perturbations
842	> of the wrist.
843	
844	Blocked: the monkey L files mark no torque perturbation (data check above), so neither the trials
845	nor their onsets can be found. The files hold 138 and 72 monkey L units, against the paper's 115
846	and 73 cells studied.
847	
848	=== CELL 25 [markdown] ===
849	### `baseline-rate`
850	
851	> Before torque onset, the firing rate of M1 neurons was lower after MPTP, because PTN rates fell
852	> (Mann-Whitney p < 0.001) while CSN rates did not change (p = 0.5). In monkey V, 12.6 and 8.9
853	> spikes/s for all cells, 20.3 and 14.8 for PTNs, 3.5 and 3.4 for CSNs.
854	
855	=== CELL 26 [code] ===
856	def mwu(a, b):
857	    return stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1397,
 "limit": 520
}
```

```
1397	main_tests = mag[mag.direction == "both"]
1398	print(f"\nMain (directions pooled): smallest p {main_tests[['ks_p', 'mwu_p']].min().min():.4f}; "
1399	      f"tests with p < 0.05: {int((main_tests[['ks_p', 'mwu_p']] < 0.05).sum().sum())} of 12")
1400	for m in measures:
1401	    print(f"{m} range: {resp[m].min():.2f} to {resp[m].max():.2f}")
1402	--OUT--
1403	group direction     measure  n_pre  n_post  mean_pre  mean_post   ks_p  mwu_p
1404	   M1      both mean_change     86     116   27.3703    20.6158 0.0004 0.0005
1405	   M1      both  max_change     86     116   43.6552    32.3955 0.0017 0.0024
1406	   M1      both         auc     86     116    4.3185     1.9977 0.0254 0.0189
1407	   M1   flexion mean_change     47      64   26.3613    20.5170 0.0060 0.0090
1408	   M1   flexion  max_change     47      64   40.5192    31.4474 0.0105 0.0243
1409	   M1   flexion         auc     47      64    4.7054     1.8180 0.1129 0.0605
1410	   M1 extension mean_change     39      52   28.5863    20.7373 0.0287 0.0178
1411	   M1 extension  max_change     39      52   47.4345    33.5623 0.0786 0.0313
1412	   M1 extension         auc     39      52    3.8523     2.2189 0.2415 0.1368
1413	  PTN      both mean_change     47      59   23.4471    15.3504 0.0007 0.0001
1414	  PTN      both  max_change     47      59   33.3657    21.9125 0.0047 0.0013
1415	  PTN      both         auc     47      59    3.3663     1.1540 0.0286 0.0932
1416	  PTN   flexion mean_change     25      33   22.2380    14.2063 0.0102 0.0012
[... 500 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1916,
 "limit": 470
}
```

```
1916	    print(f"Variant, {label}: means {sk.groupby(['direction', 'state'])[col].mean().round(2).to_dict()}; "
1917	          f"MPTP F = {a.loc['C(state)', 'F']:.1f}, p = {a.loc['C(state)', 'PR(>F)']:.2g}; "
1918	          f"middle command size only F = {a2.loc['C(state)', 'F']:.2f}, p = {a2.loc['C(state)', 'PR(>F)']:.2g}")
1919	
1920	--OUT--
1921	                          sum_sq     df          F  PR(>F)
1922	C(state)               4919.5365    1.0  1032.2752     0.0
1923	C(direction)            571.0072    1.0   119.8155     0.0
1924	C(state):C(direction)    91.0699    1.0    19.1094     0.0
1925	Residual               2778.4159  583.0        NaN     NaN
1926	
1927	--OUT--
1928	direction  state
1929	extension  post      6.01
1930	           pre      11.03
1931	flexion    post      3.20
1932	           pre       9.79
1933	Variant, middle command size only: MPTP F = 0.07, p = 0.7855; means {'post': 7.73, 'pre': 7.81}
1934	
1935	Perturbations with a latency of 0 ms: 219 of 5413
[... 446 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p paper && curl -sL "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC3840326/unicode" -o paper/PMC3840326_bioc.json; ls -la paper; python3 -c "
import json;d=json.load(open('paper/PMC3840326_bioc.json'))
d=d[0] if isinstance(d,list) else d
t=[p['text'] for doc in d['documents'] for p in doc['passages']]
open('paper/PMC3840326.txt','w').write('\n\n'.join(t)); print(len(t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat paper/PMC3840326_bioc.json; echo; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3840326/fullTextXML" -o paper/PMC3840326.xml; ls -la paper; head -c 300 paper/PMC3840326.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
rm paper/PMC3840326_bioc.json; python3 -c "
import re
x=open('paper/PMC3840326.xml').read()
t=re.sub(r'<[^>]+>',' ',x); t=re.sub(r'[ \t]+',' ',t)
open('paper/PMC3840326.txt','w').write(t)"
grep -o -i ".\{200\}excitatory.\{250\}" paper/PMC3840326.txt | head; grep -o ".\{300\}Table 1.\{300\}" paper/PMC3840326.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -o "8/9 (86%).\{400\}" paper/PMC3840326.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

# Verifier report, round 2: Pasquereau & Turner 2013 on DANDI 001636 (0.260518.1819)

**Tally.** The claims file has 28 claims, and the attempt record gives an outcome for all 28:
- 4 reproduced
- 3 partially reproduced
- 3 not reproduced
- 18 blocked: 1 for missing data and 17 as methods underspecified (`false-positive-rate`, the 15 claims that depend on which responses are detected, and `trial-correlations`)

I saved the paper's full text from Europe PMC under `paper/`.

## 1. Agreement with the stated outcomes

I agree with all 28.

**`false-positive-rate`.** In round 1 I said not reproduced. I now accept blocked (methods_underspecified).
- The claim is about the paper's procedure, and this run can only measure a reconstruction of it.
- Stationary Poisson spike trains give 0.15 with the reconstructed detection (cell 37), so the rate mostly measures the reconstruction.
- A threshold calibrated to a false-positive rate of 0.01 moves the fractions of torque-related cells further from the paper's (cell 38). So the stated rate alone does not explain the gap.
- The record cites a protocol rule for this case. I could not read that protocol. The claims file itself only states the blocking rule for the claims that use the detected responses.

**Kinematics and EMG.** I agree with these outcomes on their criteria, with one caveat that the record already states. The torque command differs between the two states, so none of them can be attributed to MPTP. `emg-m2-larger` (reproduced) is the weakest. Its only same-command comparison runs the other way on triceps longus 1 (46.7 against 1.3, p = 0.013, with 40 and 6 channel-sessions; cell 87).

## 2. Statements the outputs do not support

**Cell 98.** "against 24 to 33 per group in the paper"
- The paper's counts are 24, 33, 22 and 31, so the range is 22 to 33.

**Cell 48, and the `ptn-more-responsive` notes.** "the CSN fraction is below the expected 30.4%" and "the CSN fraction is outside tolerance"
- The PTN fraction is also outside tolerance: 68.9% against 62.1 ± 6.2, whose upper bound is 68.3 (cell 47).

**Summary (cell 103), and the `methods_unavailable` finding.** "Poisson spike trains give the same"
- Poisson gives 0.15 against 0.22 observed (cells 35 and 37), so about a third of the observed rate is not explained.
- Cell 39 says the same thing more strongly: "the excess comes from the detection procedure, not from activity in the hold period". Most of the rate comes from the procedure, not all of it.

**Cell 92, and the `emg-onset-unchanged` notes.** "Pre-MPTP responses are small …, which delays their detected onset"
- Nothing tests this, and the threshold is relative (2 SD of the baseline).
- At the middle command size the post-MPTP onset is the later one (28.8 against 45.6 ms, cell 90).

**Cell 88.** "the median m2 is 0.61 at the smallest command size, 40.8 at the middle and 194.6 at the largest"
- The three medians mix states.
- The values left out work against a simple increase with command size: post-MPTP at the middle size is 1.81, and pre-MPTP at the largest is 17.09 (n = 5) (cell 87).
- The attempt record's notes give the middle-size post-MPTP value, but not the largest-size pre-MPTP one.

**Cell 80, and the `kinematics-slower` notes.** "session means 8.5 to 145.3 deg/s … lower than the paper's 130 to 200 deg/s"
- The upper end overlaps the paper's range.
- The supported statement is that the mean is 58.7 deg/s and only one response comes from a session in the window (cells 79 and 97).

**README.** "It takes a few minutes"
- Cell 104 prints 1.5 min. This is minor.

**Checked and supported.** Every other "Result:" sentence, the rest of the Summary and README, and every outcome note and finding in the attempt record matches the printed numbers.

I also checked the paper-inconsistency finding against the paper:
- The text gives 16.3 and 3.6 spikes/s, and Table 1 gives 18.3 and 3.2.
- Table 1's CSN counts are 13/13 and 10/11 against 11/13 and 8/9, and the table marks the change "## p < 0.01 (χ² test)".

**Round-1 reasons in the record.** They state my round-1 reasons faithfully and in my own words, with my problem points folded into the claims they concern. Two small gaps:
- Two points from my problem 1 are left out: the expected ~12% of false responses among those detected, and that the Methods' literal t-test reading also fails. Neither changes an outcome.
- The `velocity-matched-magnitude` reason repeats a sentence of mine that contradicts itself ("no pre-MPTP session reaches 130 deg/s (maximum 145)"). What cell 97 shows is that no pre-MPTP response comes from a session in the window. That error is mine, not the author's.

## 3. Round-1 points

**Resolved:**
- **Monkey L.** There is now a table of torque-command excursions for every file: 1 hold-window excursion in 2048 trials (cell 7).
- **Angle scale (problem 3).** Active movements are within 2% of the derived columns (cell 11), so the small torque-induced movements are in the data. The files have no torque-sensor channel.
- **Kinematic latency measure (problem 4).** The causal and not-moving variants were added, and post-MPTP latency is still shorter (F = 781 and 743, cell 82).
- **DSI categories (problem 5).** A variant classifies by DSI value (p = 0.42, cell 70).
- **First crossing as onset (problem 6).** A variant takes the first crossing overall; 6 of 202 responses have an earlier one.
- **Pooled correlations and the zero cell (problem 7).** Within-state results are reported, and the smallest expected count is given as 2.2.
- **Short pre-MPTP EMG responses (problem 8).** 63.6% of pre-MPTP durations are 10 ms or less.
- **m1/m2 ratios (problem 9).** Ratios over channel-sessions with m2 > 0 are now given.
- **Threshold diagnostics.** Example SDFs with their thresholds, and the false-positive rate split by baseline rate and by number of trials, were added (cells 37 and 38).

**Resolved as far as the data allow, but still bearing on conclusions:**
- **Detection procedure (problem 1).** The paper's procedure cannot be recovered. Every claim that uses the detected responses stays blocked.
- **Torque command differs by state (problem 2).** The outcomes of `kinematics-slower`, `kinematic-latency-unchanged`, `emg-m2-larger`, `emg-duration-longer` and `emg-onset-unchanged` all compare different stimuli. The only same-command check has 12 post-MPTP sessions, and 1 to 6 post-MPTP EMG channel-sessions per channel. Where it can be read, it removes the effect (or reverses it, for triceps longus 1 m2). The record says the differences cannot be attributed to MPTP, which is the right reading. The outcomes rest on the criteria alone.

**Still open:** I have not inspected the plotted figures. My judgements rest on the printed outputs.

## End of run

17 turns, 2 minutes, result: success.
