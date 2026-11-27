# yang-2026 · author-revise-2 · run 44917108358

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 60000; ls entries/yang-2026 transcripts/yang-2026 questions paper
```

```
<persisted-output>
Output too large (49.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/10c8d8e0-181c-49d3-be1e-ba0e4b0babf8/tool-results/b98s75j19.txt

Preview (first 2KB):
Sat Nov 21 15:09:38 UTC 2026
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,230p docs/protocol.md; sed -n 385,800p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/yang-2026/verifier-2-report.md; ls transcripts/yang-2026 entries/yang-2026 attempts | grep -i yang; ls entries/yang-2026
```

```
**Verifier report, round 2: Yang (2026) on DANDI:000363**

The claims file has 25 claims. The attempt record has 25 outcomes: 16 reproduced and 9 partially reproduced, with none not reproduced or blocked. My round-1 opening sentence said "15 reproduced and 10 partially reproduced". That was my own miscount: my round-1 table gives 16 and 9, and the record's `verifications` copy that table correctly. Cell numbers below are those of the re-executed notebook. They differ from round 1; for example, the session counts are now in cell 13 and the decoding in cell 70.

### 1. Outcomes and assumptions

I agree with all 25 outcomes. The new runs change none of them:
- **Laser trials kept (M1 reading a):** cell 18 gives 5/5 joint fractions under the licks reading, 4/5 under the outcome reading, 10/10 axis fractions and both cosines within tolerance.
- **Decoding laser trials alone (M8 reading a):** cells 70 and 73 give 0–4 of 10 values within tolerance, and the Go-aligned criterion fails in every part.
- **Seed 17:** cells 27, 30, 41, 47, 50, 56, 59, 62, 65, 70 and 73 give the same outcome as the claim's seed everywhere except fig3c-late-residuals.
- **The fig1b rule under all eight readings:** cell 88 never selects the paper's session.

Two outcomes are marked `assumed: true`. Both assumptions are stated, as a deviation, in the notes and in the Result cell, and both are reasonable:
- **fig2d-choice-share-flat:** the partial clause is read with the criterion's own SEM rule. That rule is the only definition of "rise" the criterion gives. Cell 76 prints both counts: 4 regions not rising under the SEM rule, 3 counting any increase.
- **fig3-1c-alm-early-residual:** the early window is scored in two 50 ms bins. This rests on the Methods passages quoted in cell 58 and matches the paper's 12.6 ± 2.0 almost exactly. Cell 59 prints both readings (12.59 binned, 18.36 as one window).

fig3c-late-residuals is correctly kept at the claim's seed and flagged `seed_sensitive: true`.

### 2. S
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/yang-2026/ 2>/dev/null; cat entries/yang-2026/README.md; wc -l attempts/yang-2026-01.yaml; cat questions/yang-2026.yaml
```

```
reproduce_yang_2026.ipynb
result.json
# Yang (2026) from dandiset 000363

Tests the findings of [Yang (2026)](https://doi.org/10.21203/rs.3.rs-11447300/v1), a reanalysis of
the late-delay bilateral ALM photoinhibition sessions of the Mesoscale Activity Map dataset,
[DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129) (Chen et al. 2024), at the
version the paper cites, 0.231012.2129.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the outcome of each claim, the reasons and the differences from the
paper's method, is [`attempts/yang-2026-01.yaml`](../../attempts/yang-2026-01.yaml).

- `reproduce_yang_2026.ipynb`: the analysis. It surveys the 174 session files, streams the spike
  times, trial events, licks and video keypoints of the 112 late-delay sessions, and tests the 25
  claims. It takes about 40 minutes, about 25 of them streaming.
- `mam.py`: loading of the sessions, trial sets, z-scored window rates, choice and action axes,
  control splits, decoding, matching and distances. Other notebooks on this dandiset can import it.
[... 35 more lines not kept]
```

**Agent**

The round-2 report asks only for text corrections; no outcome is disputed. I'll locate each sentence in the notebook, README and record.

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n "20210129T132207\|rank it\|highest of the other\|40 minutes\|0.657\|thalamus 250\|outside 0.036\|0.036" reproduce_yang_2026.ipynb README.md ../../attempts/yang-2026-01.yaml | cut -c1-400; grep -n "0.423\|three of four" ../../attempts/yang-2026-01.yaml | cut -c1-300
```

```
reproduce_yang_2026.ipynb:8:    "# Reproducing Yang (2026) from dandiset 000363\n",
reproduce_yang_2026.ipynb:17:    "Dandiset. [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the Mesoscale\n",
reproduce_yang_2026.ipynb:28:    "licks and video keypoints. Nothing is downloaded to disk. The run takes about 40 minutes: about 25 for\n",
reproduce_yang_2026.ipynb:752:    "median is within tolerance (147 to 157 over the readings) and so is the highest of the other\n",
reproduce_yang_2026.ipynb:1173:    "> striatum, 0.142 in thalamus, 0.063 in midbrain and 0.036 in medulla."
reproduce_yang_2026.ipynb:1187:    "EXP_RAT = {\"ALM\": (0.111, 0.009), \"striatum\": (0.093, 0.031), \"thalamus\": (0.142, 0.034), \"midbrain\": (0.063, 0.007), \"medulla\": (0.036, 0.010)}\n",
reproduce_yang_2026.ipynb:1767:    "            ok250 = all(0.657 <= v <= 0.847 for v in v250.values())\n",
reproduce_yang_2026.ipynb:1780:    "centred 250 ms after Go the region means are 0.72 to 0.78, inside 0.657 to 0.847; every delay bin\n",
reproduce_yang_2026.ipynb:1783:    "(M8 reading a, 26 entries) gives noisy curves (delay bins 0.41 to 0.69, the thalamus 250 ms bin\n",
reproduce_yang_2026.ipynb:1796:    "> regions and rises only in medulla, from 0.036 to 0.058, with pre-lick means of 0.025 (ALM), 0.019\n",
reproduce_yang_2026.ipynb:1838:    "    med_ok = abs(t.loc[\"medulla\", \"early\"] - 0.036) <= 0.0036\n",
reproduce_yang_2026.ipynb:1840:    "    print(f\"  early means in 0.0315-0.0506: {early_ok}; pre-lick within: {pre_ok}; medulla early within 0.036: {med_ok}; \"\n",
reproduce_yang_2026.ipynb:1953:    "        out = {r: [round(float(v), 3) for v in curves[r][dl] if not 0.036 <= v <= 0.088] for r in mam.REGIONS}\n",
reproduce_yang_2026.ipynb:1954:    "        print(f\"  delay bins, {dname}: {dv.min():.3f} to {dv.max():.3f}; all in 0.036-0.088: {bool(((dv >= 0.036) & (dv <= 0.088)).all())}; outside: {out}\")"
reproduce_yang_2026.ipynb:1964:    "0.079, thalamus 0.050), but th
[... 20 more lines not kept]
```

**Agent**

Now the executed outputs the verifier cites (cells 27, 33, 73, 82, 88, 94).

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
for i in [27,33,73,82,88,94]:
    c=nb['cells'][i]
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    print('=====',i); print(out[-3500:])
E
```

```
===== 27
region-entry sides with fewer than twice as many controls as laser trials: 0
seed+ ratio small sides    ALM  striatum  thalamus  midbrain  medulla  lowest other  highest other  min mouse ratio  every mouse > 1
    0     a    disjoint 147.05      2.73      5.16      8.18     2.82          2.73           8.18             1.22             True
    0     a independent 146.78      2.75      5.09      7.56     2.73          2.73           7.56             1.16             True
    0     b    disjoint 152.68      2.80      5.31      8.77     2.94          2.80           8.77             1.33             True
    0     b independent 156.48      2.84      5.23      8.33     2.84          2.84           8.33             1.26             True
ratio a, disjoint: ALM within True, lowest within False, highest within True
ratio a, independent: ALM within True, lowest within False, highest within False
ratio b, disjoint: ALM within True, lowest within False, highest within True
ratio b, independent: ALM within True, lowest within False, highest within True

over the five seeds, reading a, disjoint: ALM [147.0, 148.9, 161.8, 151.3, 146.3] ; lowest other [2.73, 2.76, 2.73, 2.66, 2.71] ; highest other [8.18, 8.01, 7.9, 8.23, 8.09]
lowest other over the five seeds and all readings: 2.57 to 2.86

seed 17 (paper):
seed+ ratio small sides    ALM  striatum  thalamus  midbrain  medulla  lowest other  highest other  min mouse ratio  every mouse > 1
paper     a    disjoint 145.11      2.70      4.98      7.69     2.79          2.70           7.69             1.17             True
paper     a independent 147.87      2.72      5.12      8.02     2.77          2.72           8.02             1.14             True
paper     b    disjoint 152.32      2.78      5.20      8.38     2.88          2.78           8.38             1.26             True
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 125,140p attempts/yang-2026-01.yaml; sed -n 168,178p attempts/yang-2026-01.yaml; sed -n 192,206p attempts/yang-2026-01.yaml; sed -n 248,260p attempts/yang-2026-01.yaml; sed -n 334,345p attempts/yang-2026-01.yaml
```

```
output: claim:fig1e-laser-vs-control-split
  measured:
  - 147.05
  - 2.73
  - 8.18
  notes: Median across mice of the mouse mean ratio of laser to control-split energy (reading a, disjoint
    groups) ALM 147.0, striatum 2.73, thalamus 5.16, midbrain 8.18, medulla 2.82. Every mouse ratio exceeds
    1 (smallest 1.16 to 1.33 over readings). ALM is within tolerance under all four readings (146.8 to
    156.5) and the highest other region under three of four (7.56 to 8.77), but the lowest other region
    is 2.73 to 2.84, outside 3.3 +- 0.33, under every reading. No region-entry side had fewer than twice
    as many controls as laser trials, so the two small-side readings differ only in the draws. Over the
    five seeds (reading a, disjoint) ALM 146.3 to 161.8, lowest other 2.66 to 2.76, highest other 7.90
    to 8.23; over all seeds and readings the lowest other is 2.57 to 2.86, so the outcome holds under
    every seed. Under the paper's seed 17, ALM 145.1 to 158.2, lowest other 2.70 to 2.82, highest other
    7.69 to 8.74 and every mouse above 1 (smallest 1.14), the same outcome.
  deviations:
  notebook: reproduce_yang_2026.ipynb
  output: claim:fig1-1c-fraction-vs-neurons
  measured: -0.366
  notes: Spearman correlation of the session joint fraction with the number of units, pooled over regions,
[... 47 more lines not kept]
```

**Agent**

Every number except the session names checks out. Now I'll look at the notebook passages to edit.

**Agent calls Bash**

```bash
cd entries/yang-2026; sed -n 26,30p reproduce_yang_2026.ipynb; sed -n 748,756p reproduce_yang_2026.ipynb; sed -n 1778,1788p reproduce_yang_2026.ipynb; sed -n 1960,1968p reproduce_yang_2026.ipynb; sed -n 2124,2134p reproduce_yang_2026.ipynb
```

```
"What is used. The 174 session files are surveyed for photoinhibition; the 112 late-delay\n",
    "bilateral sessions are then streamed for the spike times of the \"good\" units, the trial events,\n",
    "licks and video keypoints. Nothing is downloaded to disk. The run takes about 40 minutes: about 25 for\n",
    "streaming, and most of the rest for decoding under six seeds.\n",
    "\n",
   "id": "9c070ae4",
   "metadata": {},
   "source": [
    "**Result: partially reproduced.** Every mouse in every region has a ratio above 1, the ALM\n",
    "median is within tolerance (147 to 157 over the readings) and so is the highest of the other\n",
    "regions (midbrain, 7.6 to 8.8), but the lowest of the other regions (striatum or medulla) is 2.7 to\n",
    "2.8 under the claim's seed and 2.6 to 2.9 over all readings and seeds, below the 2.97 the tolerance\n",
    "allows. Seed 17 gives the same: ALM 145 to 158, lowest other 2.70 to 2.82, highest other 7.7 to\n",
    "8.7, every mouse above 1."
   "source": [
    "**Result: reproduced.** Decoding laser and control trials together (M8 reading b), in the bin\n",
    "centred 250 ms after Go the region means are 0.72 to 0.78, inside 0.657 to 0.847; every delay bin\n",
    "lies between 0.54 and 0.59, inside 0.495 to 0.638; and the 250 ms bin exceeds every delay bin in\n",
    "every region, under both bin readings, all five seeds and seed 17. Decoding laser trials alone\n",
    "(M8 reading a, 26 entries) gives noisy curves (delay bins 0.41 to 0.69, the thalamus 250 ms bin\n",
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/yang-2026/reproduce_yang_2026.ipynb",
 "offset": 26,
 "limit": 4
}
```

```
File content (48207 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "entries/yang-2026/README.md"
}
```

```
1	# Yang (2026) from dandiset 000363
2	
3	Tests the findings of [Yang (2026)](https://doi.org/10.21203/rs.3.rs-11447300/v1), a reanalysis of
4	the late-delay bilateral ALM photoinhibition sessions of the Mesoscale Activity Map dataset,
5	[DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129) (Chen et al. 2024), at the
6	version the paper cites, 0.231012.2129.
7	
8	A failure to reproduce here may be a failure of this attempt, not of the paper: see the
9	reasoning and the differences from the paper's method.
10	
11	The attempt record, with the outcome of each claim, the reasons and the differences from the
12	paper's method, is [`attempts/yang-2026-01.yaml`](../../attempts/yang-2026-01.yaml).
13	
14	- `reproduce_yang_2026.ipynb`: the analysis. It surveys the 174 session files, streams the spike
15	  times, trial events, licks and video keypoints of the 112 late-delay sessions, and tests the 25
16	  claims. It takes about 40 minutes, about 25 of them streaming.
17	- `mam.py`: loading of the sessions, trial sets, z-scored window rates, choice and action axes,
18	  control splits, decoding, matching and distances. Other notebooks on this dandiset can import it.
19
```

**Agent calls Read**

```json
{
 "file_path": "attempts/yang-2026-01.yaml",
 "offset": 560,
 "limit": 217
}
```

```
560	    handled changes any analysis that regresses out tongue position.
561	- kind: other
562	  about: data
563	  severity: minor
564	  statement: In two of the 112 late-delay sessions the side-camera video does not span the trials to within
565	    5 s, so some trials of those sessions have no keypoints.
566	- kind: methods_unavailable
567	  statement: Question for the author. Was the matched distance in the early window (12.6 in ALM, Figure
568	    3-1C) computed in two 50 ms bins with the per-bin distances averaged, as for the pre-lick window,
569	    or over the single 20 to 120 ms window? The two give 12.59 and 18.36 here; the attempt assumes the
570	    binned reading (Methods, Matched distance and Time courses).
571	- kind: methods_unavailable
572	  statement: Question for the author. Several details are not in the Methods and the code is private;
573	    the attempt chose, where the data allowed, the reading that matches the paper's counts. (1) Laser
574	    trials with an early lick were dropped (the counts of Table 1 match only then). (2) Each laser trial
575	    took the control trial with the closest reaction time within the caliper (a random match gives a median
576	    difference of 43 ms, not 1.3 ms). (3) A video keypoint was taken as detected at likelihood 0.9 and
577	    trials without a detection took the control mean; dropping them from the fit gives other fractions
578	    and cosines. (4) Lick direction was decoded from laser and control trials together; with laser trials
579	    alone only 26 of 278 region entries have the 40 trials and 15 per direction the Methods require. Please
[... 197 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/yang-2026/reproduce_yang_2026.ipynb",
 "offset": 26,
 "limit": 4
}
```

```
File content (48207 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent**

I'll edit the notebook sources with a script, asserting each old string appears exactly once.

**Agent calls Bash**

```bash
cd entries/yang-2026; python - <<'E'
p='reproduce_yang_2026.ipynb'
s=open(p).read()
reps=[
("The run takes about 40 minutes: about 25 for\\n\",\n    \"streaming, and most of the rest for decoding under six seeds.",
 "The run takes about an hour (62 minutes in the last run): about\\n\",\n    \"25 for streaming, and most of the rest for decoding under six seeds."),
("median is within tolerance (147 to 157 over the readings) and so is the highest of the other\\n\",\n    \"regions (midbrain, 7.6 to 8.8), but",
 "median is within tolerance (147 to 157 over the readings), the highest of the other regions\\n\",\n    \"(midbrain, 7.6 to 8.8) is within it under three of the four readings (7.56 under reading a with\\n\",\n    \"independent groups is below 7.83), but"),
("(M8 reading a, 26 entries) gives noisy curves (delay bins 0.41 to 0.69, the thalamus 250 ms bin\\n\",\n    \"0.63) that fail",
 "(M8 reading a, 26 entries) gives noisy curves (delay bins 0.41 to 0.69, the 250 ms bin 0.63 in\\n\",\n    \"thalamus and 0.635 in ALM, both below 0.657) that fail"),
("in the first bin and thalamus 0.034 to 0.035 in several bins.",
 "in the first bin, thalamus 0.034 to 0.035 in several bins, and ALM 0.035 in one bin with 50 ms\\n\",\n    \"steps."),
("readings that drop trials without keypoints select ses-20210129T132207 and rank it 38th (its joint\\n\",\n    \"fraction is 0.001 there).",
 "readings that drop trials without keypoints select ses-20201230T112558 (three readings) or\\n\",\n    \"ses-20200925T153348 (one) and rank the paper's session 38th (its joint fraction is 0.001 there)."),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
import json; json.load(open(p))
E
sed -i 's/claims. It takes about 40 minutes, about 25 of them streaming./claims. It takes about an hour (62 minutes in the last run), about 25 minutes of it streaming./' README.md; grep -n hour README.md
```

```
16:  claims. It takes about an hour (62 minutes in the last run), about 25 minutes of it streaming.
```

**Agent**

Now the record. Let me fix the fig1b, fig1-1c, fig2a and fig2b notes.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/yang-2026-01.yaml'
s=open(p).read()
reps=[
("""    against 0.0019 to 0.0033), and the four that drop trials without keypoints select ses-20210129T132207
    and rank it 38th of 43 (its joint fraction is 0.0008 to 0.0009 there).'""",
"""    against 0.0019 to 0.0033), and the four that drop trials without keypoints select ses-20201230T112558
    (three readings) or ses-20200925T153348 (one) and rank ses-20200922T135318 38th of 43 (its joint fraction
    is 0.0008 to 0.0009 there).'"""),
("rho -0.366 to -0.423 over the eight readings.","rho -0.366 to -0.428 over the eight readings."),
("gives a 250 ms bin of 0.628 to 0.780 (thalamus below 0.657)","gives a 250 ms bin of 0.628 to 0.780 (thalamus 0.628 and ALM 0.635 below 0.657)"),
("""    first bin) and thalamus (0.034 to 0.035).""","""    first bin), thalamus (0.034 to 0.035) and, with 50 ms steps, ALM (0.035)."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
grep -n "selects ses-20210419T161140 and rank it" attempts/yang-2026-01.yaml
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/yang-2026-01.yaml'
s=open(p).read()
reps=[
("""    missing keypoints select ses-20210419T161140 and rank it second or third""","""    missing keypoints select ses-20210419T161140 and rank ses-20200922T135318 second or third"""),
("""      No reading selects ses-20200922T135318: the fill readings select ses-20210419T161140 and rank it
      second or third, the drop readings select ses-20210129T132207 and rank it 38th. Outcome unchanged.'""",
"""      No reading selects ses-20200922T135318: the fill readings select ses-20210419T161140 and rank it
      second or third, the drop readings select ses-20201230T112558 or ses-20200925T153348 and rank it
      38th. Outcome unchanged. (Corrected after round 2, which found that this response named the wrong
      session selected by the drop readings.)'"""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
sed -n 1,60p attempts/yang-2026-01.yaml; grep -n "^[a-z_]*:" attempts/yang-2026-01.yaml
```

```
schema_version: 3
id: yang-2026-01
datasets:
- archive: dandi
  id: '000363'
  version: 0.231012.2129
  doi: 10.48324/dandi.000363/0.231012.2129
  relation: reuses
paper: doi:10.21203/rs.3.rs-11447300/v1
date: '2026-11-21'
entry: yang-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/select ses-20210419T161140 and rank it\n      second or third/X/' attempts/yang-2026-01.yaml; grep -l "^  findings:" attempts/*.yaml | head; grep -n "findings" tools/entry.py | head -30; ls schema* tools
```

```
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
attempts/asari-2009-02.yaml
attempts/ashworth-2025-01.yaml
attempts/athalye-2023-01.yaml
attempts/azcorra-2023-01.yaml
attempts/bakalar-2023-01.yaml
attempts/bech-2026-01.yaml
attempts/bellvila-2026-01.yaml
281:        # A repeat attempt's reconciliation points into the earlier record's findings and its own by number.
288:                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
289:                numbers = [f.get("finding") for f in rec.get("findings") or []]
291:                    report.error(where, f"reconciliation: give each of the {n_then} findings of "
293:                for f in rec.get("findings") or []:
306:            kinds = {f.get("kind") for f in attempt.get("findings") or []}
352:        for n, f in enumerate(attempt.get("findings") or [], 1):
368:        # A later review of an earlier attempt's findings (`findings_review`) rates those about the data, each once,
369:        # by its number in the record; an attempt that rates its own findings (pilot-18 on) has no such review.
371:        for item in (attempt.get("findings_review") or {}).get("findings") or []:
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));
v=s['properties']['verifications'];print(json.dumps(v,indent=1)[:4000])"
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 89 more lines not kept]
```

**Agent**

Text edits to the entry are done. Starting the full re-run now (last one took 62 minutes).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/yang-2026 2>&1 | tail -30; date -u
```

```
Sat Nov 21 15:11:18 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
0 error(s)
pass  reproduce_yang_2026.ipynb  (2178 s)
Sat Nov 21 15:47:49 UTC 2026
```

**Agent**

The run passed in 36 minutes, much faster than last time (62). Checking the printed totals and that the numbers I cited are unchanged.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
old=None
for i,c in enumerate(nb['cells']):
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if 'total run time' in out or 'paper\'s session rank' in out or 'pooled rho' in out: print(i, out[-1800:])
E
```

```
33 pooled over regions: Spearman rho = -0.366, p = 3e-10, n = 278 region entries
  ALM       rho = -0.580, p = 1.1e-09, n = 93
  striatum  rho = -0.283, p = 0.051, n = 48
  thalamus  rho = -0.213, p = 0.25, n = 31
  midbrain  rho = -0.371, p = 0.0015, n = 71
  medulla   rho = -0.413, p = 0.014, n = 35
reading own,fill,licks       pooled rho = -0.366
reading own,fill,outcome     pooled rho = -0.374
reading own,drop,licks       pooled rho = -0.404
reading own,drop,outcome     pooled rho = -0.423
reading go,fill,licks        pooled rho = -0.366
reading go,fill,outcome      pooled rho = -0.372
reading go,drop,licks        pooled rho = -0.401
reading go,drop,outcome      pooled rho = -0.421

88 in 130 +- 13: True; fraction within 0.053 +- 0.0053: True

the rule under every reading of M3, M4 and M5 (candidates: ALM entries with matched pairs, at least the median unit count of the reading):
         reading  ALM mouse mean  candidates            selected  selected distance  paper's session rank  paper's session distance  paper's session units  paper's session joint
  own,fill,licks         0.05492          44 ses-20210419T161140            0.00200                     2                   0.00210                    130                0.05282
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git ls-files executed/yang-2026 | head; git log --oneline -3 -- executed/yang-2026
```

```
(Bash completed with no output)
```

**Agent**

The old executed copy isn't tracked, but I printed cells 27, 33, 73, 82 and 88 from it earlier. Comparing those against the new run:

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
for i in [27,73,82]:
    c=nb['cells'][i]
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    print('=====',i); print(out[-2500:])
E
```

```
===== 27
region-entry sides with fewer than twice as many controls as laser trials: 0
seed+ ratio small sides    ALM  striatum  thalamus  midbrain  medulla  lowest other  highest other  min mouse ratio  every mouse > 1
    0     a    disjoint 147.05      2.73      5.16      8.18     2.82          2.73           8.18             1.22             True
    0     a independent 146.78      2.75      5.09      7.56     2.73          2.73           7.56             1.16             True
    0     b    disjoint 152.68      2.80      5.31      8.77     2.94          2.80           8.77             1.33             True
    0     b independent 156.48      2.84      5.23      8.33     2.84          2.84           8.33             1.26             True
ratio a, disjoint: ALM within True, lowest within False, highest within True
ratio a, independent: ALM within True, lowest within False, highest within False
ratio b, disjoint: ALM within True, lowest within False, highest within True
ratio b, independent: ALM within True, lowest within False, highest within True

over the five seeds, reading a, disjoint: ALM [147.0, 148.9, 161.8, 151.3, 146.3] ; lowest other [2.73, 2.76, 2.73, 2.66, 2.71] ; highest other [8.18, 8.01, 7.9, 8.23, 8.09]
lowest other over the five seeds and all readings: 2.57 to 2.86

seed 17 (paper):
seed+ ratio small sides    ALM  striatum  thalamus  midbrain  medulla  lowest other  highest other  min mouse ratio  every mouse > 1
paper     a    disjoint 145.11      2.70      4.98      7.69     2.79          2.70           7.69             1.17             True
paper     a independent 147.87      2.72      5.12      8.02     2.77          2.72           8.02             1.14             True
paper     b    disjoint 152.32      2.78      5.20      8.38     2.88          2.78           8.38             1.26             True
[... 30 more lines not kept]
```

**Agent**

Primary-reading results are identical between runs; only the "drop trials without keypoints" readings move. Looking at how those are computed.

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n "drop" mam.py | head -60
```

```
20:  kept is open; `LASER_EARLY` names the readings ("keep", "drop").
31:  and SD of control trials in that window; units with control SD below 1e-6 dropped. The early
44:  without a detection take the control mean ("fill", reading a) or are dropped from the fit
45:  ("drop", reading b).
330:def trial_sets(S: dict, laser_early: str = "drop", lick: str = "licks") -> dict:
335:    if laser_early == "drop":
611:def residual(Zbins: list[np.ndarray], pairs, missing: str = "drop", combine: str = "mean"):
615:    per-bin distances, 'concat' takes the distance of the concatenated bins. missing 'drop'
616:    drops a pair without a second control from both distances; 'keep' keeps it for the
```

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n "fill\|kp_ok\|keypoint\|detected" mam.py | head -60
```

```
8:photostimulation onsets with a control code), the photostimulation sites, video keypoints, and
41:  keypoint's likelihood is at least `LIKELIHOOD_MIN` (0.9), an assumption: the files give a
44:  without a detection take the control mean ("fill", reading a) or are dropped from the fit
214:    For the clock check, also the fraction of frames with the tongue detected in the 50 ms
238:        info[kp] = {"frames": len(ts), "detected": float(ok.mean()),
408:def video_design(S: dict, control_lick: np.ndarray, reading: str = "fill", threshold: float | None = None):
410:    selects the keypoint likelihood cut (default LIKELIHOOD_MIN)."""
412:    if reading == "fill":
424:def axes(S: dict, region: str, ts: dict, early: str = "early_own", video: str = "fill",
```

**Agent calls Bash**

```bash
cd entries/yang-2026; sed -n 340,520p mam.py
```

```
rt[tt["lick_dir"] == 0] = np.nan
    sides = [sd for sd in (-1, 1)
             if (laser & (tt["instr"] == sd)).sum() >= MIN_TRIALS_SIDE
             and (control & (tt["instr"] == sd)).sum() >= MIN_TRIALS_SIDE]
    return {"laser": laser, "control": control, "sides": sides, "lick_dir": lick_dir,
            "rt": rt, "instr": tt["instr"]}


def zscore_window(X: np.ndarray, control: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Z-score (trials, units) by control trials; return z and the mask of units kept."""
    mu = np.nanmean(X[control], axis=0)
    sd = np.nanstd(X[control], axis=0)
    keep = sd >= SD_MIN
    with np.errstate(invalid="ignore", divide="ignore"):
        Z = (X - mu) / np.where(keep, sd, 1.0)
    return Z, keep


def window_rates(S: dict, units: np.ndarray, name) -> np.ndarray:
    """Rates (trials, units) in a named window: 'choice', 'action', 'early_go', 'early_own',
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,re
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    src=''.join(c['source'])
    if re.search(r'video|keypoint',out,re.I) and i<25: print('=====',i,src[:600]); print(out[:2500])
E
```

```
===== 8 rows = []
for s in S:
    tt = s["trials"]
    reg = pd.Series(s["region"]).value_counts()
    alm = np.where(s["region"] == "ALM")[0]
    bil = np.isin(tt["code"], tt["bilateral_codes"])
    ctrl = (~tt["stim"]) & (~tt["early"])

    def effect(col):
        # mean over ALM units of |laser mean - control mean| / control SD
        if len(alm) == 0:
            return np.nan, np.nan
        X = s["rates"][:, alm, col]
        sd = X[ctrl].std(0)
        ok = sd > 0
        return float(np.mean(np.abs(X[bil].mean(0) - X[ctrl].mean(0))[ok] / sd[ok])), float(np.mean((X[bil].mean(0) < X[ctrl].mean
good units of the five regions, per session:
         ALM  striatum  thalamus  midbrain  medulla
count  112.0     112.0     112.0     112.0    112.0
mean   116.4      56.7      70.0      60.8     42.9
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n '"video"\|video_by_threshold\|KEYPOINTS\|def load' mam.py | head; grep -n "VIDEO_FEAT\|KEYPOINT" mam.py | head
```

```
79:KEYPOINTS = ["Jaw", "Nose", "Tongue"]
219:    for k, kp in enumerate(KEYPOINTS):
251:def load_session(s: dict) -> dict:
313:                "video": video[LIKELIHOOD_MIN], "video_by_threshold": video, "video_info": vinfo, "unsorted_units": unsorted,
321:def load_all(surveys: list[dict], workers: int = 3) -> list[dict]:
411:    V = (S["video"] if threshold is None else S["video_by_threshold"][threshold])[control_lick]
79:KEYPOINTS = ["Jaw", "Nose", "Tongue"]
219:    for k, kp in enumerate(KEYPOINTS):
```

**Agent calls Bash**

```bash
cd entries/yang-2026; sed -n 200,330p mam.py
```

```
def survey_all(asset_list: list[dict], workers: int = 8) -> list[dict]:
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(survey, asset_list))


def is_late_delay(s: dict) -> bool:
    return np.isfinite(s["median_onset"]) and abs(s["median_onset"] - LATE_ONSET) <= ONSET_TOL


def _video(f: h5py.File, go: np.ndarray, licks: np.ndarray) -> tuple[np.ndarray, dict]:
    """Per trial mean x, y of jaw, nose, tongue over the choice window (-0.6 to 0 s from Go).

    For the clock check, also the fraction of frames with the tongue detected in the 50 ms
    after each lick, and with the lick times shifted by -0.5 s."""
    B = f["acquisition/BehavioralTimeSeries"]
    out = {thr: np.full((len(go), 6), np.nan) for thr in LIKELIHOOD_VARIANTS}
    info = {}
    for k, kp in enumerate(KEYPOINTS):
        name = f"Camera0_side_{kp}Tracking"
        if name not in B:
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
for i in range(1,8):
    c=nb['cells'][i]
    if c['cell_type']=='code': print('=====',i,''.join(c['source'])[:1500])
E
```

```
===== 1 import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_k] = "1"
import json
import resource
import time
import urllib.request
import warnings

import numpy as np
import pandas as pd
from joblib import Parallel, delayed
from scipy import stats

import mam

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 300)
[... 52 more lines not kept]
```

**Agent**

Threads are pinned to 1, so a change between runs points to different CPU kernels on different runners acting on an ill-conditioned fit. Testing on the five sessions named under the drop readings:

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n "def assets\|def survey\b\|def survey(" mam.py; date -u; cat > $TMPDIR/t.py <<'E'
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_k]="1"
import sys, time, pickle; sys.path.insert(0,'.')
import numpy as np, mam
want=["ses-20200922T135318","ses-20210129T132207","ses-20201230T112558","ses-20200925T153348","ses-20210419T161140"]
A=[a for a in mam.assets() if any(w in str(a) for w in want)]
print(len(A))
t=time.time(); SV=mam.survey_all(A, workers=5); S=mam.load_all(SV, workers=5); print('load',time.time()-t)
pickle.dump(S,open(os.environ['TMPDIR']+'/S.pkl','wb'))
E
executed/yang-2026/.venv/bin/python $TMPDIR/t.py; date -u
```

```
105:def assets() -> list[dict]:
184:def survey(asset: dict) -> dict:
Sat Nov 21 15:48:49 UTC 2026
5
load 54.69492149353027
Sat Nov 21 15:50:02 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/yang-2026/reproduce_yang_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if 'def ' in src and c['cell_type']=='code' and i<20: print('=====',i,src[:3000])
E
```

```
===== 8 rows = []
for s in S:
    tt = s["trials"]
    reg = pd.Series(s["region"]).value_counts()
    alm = np.where(s["region"] == "ALM")[0]
    bil = np.isin(tt["code"], tt["bilateral_codes"])
    ctrl = (~tt["stim"]) & (~tt["early"])

    def effect(col):
        # mean over ALM units of |laser mean - control mean| / control SD
        if len(alm) == 0:
            return np.nan, np.nan
        X = s["rates"][:, alm, col]
        sd = X[ctrl].std(0)
        ok = sd > 0
        return float(np.mean(np.abs(X[bil].mean(0) - X[ctrl].mean(0))[ok] / sd[ok])), float(np.mean((X[bil].mean(0) < X[ctrl].mean(0))[ok]))
    eff_e, down_e = effect(mam.COL_EARLY_OWN)
    eff_b, _ = effect(0)
    rows.append({"mouse": s["mouse"], "session": s["session"], **{r: int(reg.get(r, 0)) for r in mam.REGIONS},
                 "probe_labels": "; ".join(sorted(set(s["probe"]))),
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026; cat > $TMPDIR/t2.py <<'E'
import os
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_k]="1"
import sys, pickle; sys.path.insert(0,'.')
import numpy as np, mam
S=pickle.load(open(os.environ['TMPDIR']+'/S.pkl','rb'))
for s in S:
  for l in ("licks","outcome"):
    ts=mam.trial_sets(s,"drop",l)
    cl=ts["control"]&(ts["lick_dir"]!=0)
    for r in mam.REGIONS:
        for v in ("fill","drop"):
            ax=mam.axes(s,r,ts,early="early_own",video=v)
            if ax is None: continue
            D,rows=mam.video_design(s,cl,v)
            f=mam.fractions(ax["d"],ax)
            dirs=ts["lick_dir"][cl][rows]
            print(s["session"],l,r,v,"ctrl",cl.sum(),"rows",rows.sum(),"cols",D.shape[1],"rank",np.linalg.matrix_rank(D),"dirs+",(dirs==1).sum(),"dirs-",(dirs==-1).sum(),"units",ax["n_units"],"joint %.5f"%f["joint"])
E
executed/yang-2026/.venv/bin/python $TMPDIR/t2.py
```

```
ses-20200922T135318 licks ALM fill ctrl 294 rows 294 cols 7 rank 7 dirs+ 138 dirs- 156 units 130 joint 0.05282
ses-20200922T135318 licks ALM drop ctrl 294 rows 22 cols 7 rank 7 dirs+ 3 dirs- 19 units 130 joint 0.00078
ses-20200922T135318 licks medulla fill ctrl 294 rows 294 cols 7 rank 7 dirs+ 138 dirs- 156 units 247 joint 0.03277
ses-20200922T135318 licks medulla drop ctrl 294 rows 22 cols 7 rank 7 dirs+ 3 dirs- 19 units 247 joint 0.03345
ses-20200922T135318 outcome ALM fill ctrl 293 rows 293 cols 7 rank 7 dirs+ 138 dirs- 155 units 130 joint 0.05215
ses-20200922T135318 outcome ALM drop ctrl 293 rows 22 cols 7 rank 7 dirs+ 3 dirs- 19 units 130 joint 0.00080
ses-20200922T135318 outcome medulla fill ctrl 293 rows 293 cols 7 rank 7 dirs+ 138 dirs- 155 units 247 joint 0.03238
ses-20200922T135318 outcome medulla drop ctrl 293 rows 22 cols 7 rank 7 dirs+ 3 dirs- 19 units 247 joint 0.03323
ses-20200925T153348 licks ALM fill ctrl 235 rows 235 cols 7 rank 7 dirs+ 111 dirs- 124 units 220 joint 0.03377
ses-20200925T153348 licks ALM drop ctrl 235 rows 16 cols 7 rank 7 dirs+ 6 dirs- 10 units 220 joint 0.03823
ses-20200925T153348 licks midbrain fill ctrl 235 rows 235 cols 7 rank 7 dirs+ 111 dirs- 124 units 102 joint 0.00339
ses-20200925T153348 licks midbrain drop ctrl 235 rows 16 cols 7 rank 7 dirs+ 6 dirs- 10 units 102 joint 0.01891
ses-20200925T153348 outcome ALM fill ctrl 233 rows 233 cols 7 rank 7 dirs+ 111 dirs- 122 units 220 joint 0.03419
ses-20200925T153348 outcome ALM drop ctrl 233 rows 15 cols 7 rank 7 dirs+ 6 dirs- 9 units 220 joint 0.04353
ses-20200925T153348 outcome midbrain fill ctrl 233 rows 233 cols 7 rank 7 dirs+ 111 dirs- 122 units 102 joint 0.00375
ses-20200925T153348 outcome midbrain drop ctrl 233 rows 15 cols 7 rank 7 dirs+ 6 dirs- 9 units 102 joint 0.01059
ses-20201230T112558 licks ALM fill ctrl 259 rows 259 cols 7 rank 7 dirs+ 117 dirs- 142 units 185 joint 0.06079
ses-20201230T112558 licks ALM drop ctrl 259 rows 10 cols 7 rank 7 dirs+ 7 dirs- 3 units 185 joi
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B2 -A12 "keypoint" claims/yang-2026.yaml | head -80
```

```
27-#
28-# Data the paper used (Methods, Dataset; Units and regions; Table 1). DANDI 000363, version
29:# 0.231012.2129; spike times, trial events, optogenetic locations and video keypoints from the
30-# derived session files. Mice performing a memory-guided directional licking task (instructed
31-# left or right, lick after a Go cue), with Neuropixels recordings from ALM, striatum,
32-# thalamus, midbrain and medulla. 168 sessions contained photoinhibition; the analysed sessions
33-# are those with bilateral ALM photoinhibition during the last 0.5 s of the delay, ending at Go.
34-# 19 mice and 93 sessions gave an ALM estimate; Table 1 gives the counts per region (ALM 19 /
35-# 93, striatum 13 / 48, thalamus 10 / 31, midbrain 16 / 71, medulla 8 / 35; after matching 19 /
36-# 87, 12 / 42, 10 / 29, 15 / 64, 8 / 32). Measured variables per trial: instructed side,
37-# photostimulation code and its location list, laser onset, Go cue time, lick times and
38-# directions, early-lick flag, outcome; per unit: spike times, classification label, electrode
39:# location; per video frame: jaw, nose and tongue keypoints.
40-#
41-# Shared methods, cited once here and named in the criteria by label. Each says where it comes
42-# from; details the paper does not fix are marked open, with the readings its text allows.
43-# Every reading is run; a claim is reproduced when its result matches under any combination of
44-# readings, and the readings that match are reported.
45-# M1 Sessions (Methods, Dataset). Sessions that contain photoinhibition trials. Bilateral
46-#   trials are those whose photostimulation control code has an optogenetic location list with
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/yang-2026; grep -n 'video=\|video_design\|"drop"' reproduce_yang_2026.ipynb mam.py | cut -c1-250
```

```
reproduce_yang_2026.ipynb:358:    "            ax = mam.axes(s, r, ts, early=f\"early_{e}\", video=v)\n",
reproduce_yang_2026.ipynb:529:    "            ax = mam.axes(s, r, ts, early=f\"early_{e}\", video=v)\n",
mam.py:20:  kept is open; `LASER_EARLY` names the readings ("keep", "drop").
mam.py:45:  ("drop", reading b).
mam.py:330:def trial_sets(S: dict, laser_early: str = "drop", lick: str = "licks") -> dict:
mam.py:335:    if laser_early == "drop":
mam.py:408:def video_design(S: dict, control_lick: np.ndarray, reading: str = "fill", threshold: float | None = None):
mam.py:446:        D, rows = video_design(S, cl, video, threshold)
mam.py:611:def residual(Zbins: list[np.ndarray], pairs, missing: str = "drop", combine: str = "mean"):
```

**Agent calls Bash**

```bash
cd entries/yang-2026; sed -n 36,50p mam.py; sed -n 350,375p reproduce_yang_2026.ipynb; sed -n 515,545p reproduce_yang_2026.ipynb
```

```
- Go-aligned grid (claims M10; Methods, Time courses): 50 ms bins from -600 to +600 ms; 100 ms
  bins as the mean of two adjacent 50 ms rates, stepped by 50 ms (the non-overlapping reading is
  the subset starting at -600 ms).
- Video regression (claims M5; Methods, Rates and coding axes): mean x and y of jaw, nose and
  tongue over the choice window with an intercept. A frame counts as a detection when the
  keypoint's likelihood is at least `LIKELIHOOD_MIN` (0.9), an assumption: the files give a
  likelihood per frame and no detection flag, and 0.9 is the usual DeepLabCut cut (0.5 and 0.99
  are computed as well, `LIKELIHOOD_VARIANTS`, to show how much it matters). Trials
  without a detection take the control mean ("fill", reading a) or are dropped from the fit
  ("drop", reading b).
"""

from __future__ import annotations

import json
    "        for s in S:\n",
    "            TS[(le, l, s[\"session\"])] = mam.trial_sets(s, le, l)\n",
    "AX = {}\n",
    "frac_rows = []\n",
    "for (e, v, l) in READINGS:\n",
[... 52 more lines not kept]
```

**Agent**

Applying the fix in `mam.axes` and adding a printout of the entries left out to cell 11:

**Agent calls Bash**

```bash
cd entries/yang-2026; python - <<'E'
p='mam.py'; s=open(p).read()
a='''  without a detection take the control mean ("fill", reading a) or are dropped from the fit
  ("drop", reading b).
"""'''
b='''  without a detection take the control mean ("fill", reading a) or are dropped from the fit
  ("drop", reading b). Under reading b a region entry whose kept control trials are no more
  than the design's columns is left out: the regression is then exact, and the residual choice
  axis is round-off that differs between machines (a standard choice; the claims file and the
  paper set no minimum).
"""'''
assert s.count(a)==1; s=s.replace(a,b)
a='''        D, rows = video_design(S, cl, video, threshold)
'''
b='''        D, rows = video_design(S, cl, video, threshold)
        if D.shape[0] <= D.shape[1]:
            return None
'''
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
p='reproduce_yang_2026.ipynb'; s=open(p).read()
a='''    "FR = pd.DataFrame(frac_rows)\\n",
'''
b='''    "FR = pd.DataFrame(frac_rows)\\n",
    "# Reading b of the video regression leaves out an entry whose kept control trials are no more than the regressors.\\n",
    "for (e, v, l) in READINGS:\\n",
    "    if v != \\"drop\\":\\n",
    "        continue\\n",
    "    k = lambda rd: set(map(tuple, FR[FR.reading == rd][[\\"region\\", \\"session\\"]].values))\\n",
    "    lost = sorted(k(f\\"{e},fill,{l}\\") - k(f\\"{e},drop,{l}\\"))\\n",
    "    print(f\\"reading {e},drop,{l}: {len(k(f'{e},drop,{l}'))} region entries; left out (too few control trials with keypoints): {len(lost)}\\", lost)\\n",
'''
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
import json; json.load(open(p))
E
executed/yang-2026/.venv/bin/python $TMPDIR/t2.py | grep -c drop
```

```
22
```

**Agent**

Fix works on the subset: the 2-trial entries of ses-20210129T132207 are now left out, nothing else changes. Re-running the full entry:

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/yang-2026 2>&1 | tail -5; date -u
```

```
Sat Nov 21 15:51:01 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
0 error(s)
pass  reproduce_yang_2026.ipynb  (2102 s)
Sat Nov 21 16:26:14 UTC 2026
```

**Agent**

Run passed (35 min). Since drop-reading entries changed, every number quoted "over the readings" may have moved. I'll dump all outputs and check each claim's conclusions.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,os
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
with open(os.environ['TMPDIR']+'/out.txt','w') as f:
  for i,c in enumerate(nb['cells']):
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    tags=c['metadata'].get('tags',[])
    if c['cell_type']=='markdown': f.write(f'##### {i} MD\n'+''.join(c['source'])+'\n')
    else: f.write(f'##### {i} CODE {tags}\n'+out+'\n')
E
wc -l $TMPDIR/out.txt; grep -n "left out (too few" $TMPDIR/out.txt | cut -c1-600
```

```
1229 /tmp/claude-1001/out.txt
175:reading own,drop,licks: 230 region entries; left out (too few control trials with keypoints): 48 [('ALM', 'ses-20191022T133136'), ('ALM', 'ses-20191023T142402'), ('ALM', 'ses-20191122T144855'), ('ALM', 'ses-20191217T123303'), ('ALM', 'ses-20200921T162104'), ('ALM', 'ses-20210111T122809'), ('ALM', 'ses-20210125T124258'), ('ALM', 'ses-20210129T132207'), ('ALM', 'ses-20210130T135022'), ('ALM', 'ses-20210318T122039'), ('ALM', 'ses-20210320T130513'), ('ALM', 'ses-20210321T131204'), ('ALM', 'ses-20210323T121231'), ('ALM', 'ses-20210324T143423'), ('ALM', 'ses-20210324T182545'), ('ALM', 'ses-20210
176:reading own,drop,outcome: 230 region entries; left out (too few control trials with keypoints): 48 [('ALM', 'ses-20191022T133136'), ('ALM', 'ses-20191023T142402'), ('ALM', 'ses-20191122T144855'), ('ALM', 'ses-20191217T123303'), ('ALM', 'ses-20200921T162104'), ('ALM', 'ses-20210111T122809'), ('ALM', 'ses-20210125T124258'), ('ALM', 'ses-20210129T132207'), ('ALM', 'ses-20210130T135022'), ('ALM', 'ses-20210318T122039'), ('ALM', 'ses-20210320T130513'), ('ALM', 'ses-20210321T131204'), ('ALM', 'ses-20210323T121231'), ('ALM', 'ses-20210324T143423'), ('ALM', 'ses-20210324T182545'), ('ALM', 'ses-202
177:reading go,drop,licks: 230 region entries; left out (too few control trials with keypoints): 48 [('ALM', 'ses-20191022T133136'), ('ALM', 'ses-20191023T142402'), ('ALM', 'ses-20191122T144855'), ('ALM', 'ses-20191217T123303'), ('ALM', 'ses-20200921T162104'), ('ALM', 'ses-20210111T122809'), ('ALM', 'ses-20210125T124258'), ('ALM', 'ses-20210129T132207'), ('ALM', 'ses-20210130T135022'), ('ALM', 'ses-20210318T122039'), ('ALM', 'ses-20210320T130513'), ('ALM', 'ses-20210321T131204'), ('ALM', 'ses-20210323T121231'), ('ALM', 'ses-20210324T143423'), ('ALM', 'ses-20210324T182545'), ('ALM', 'ses-202104
178:reading go,drop,outcome: 230 region entries; left out (too few control trials with keypoints): 48 [('ALM', 'ses-20191022T133136'), ('ALM', 'ses-20191023T142402'), 
[... 1 more lines not kept]
```

**Agent**

48 of 278 region entries had 7 or fewer usable control trials under reading (b), so a sixth of that reading's entries had been noise. Reading the full new output against the record:

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt",
 "offset": 150,
 "limit": 330
}
```

```
150	onsets lie within a millisecond of the session median, so the two placements of the early window
151	(claims M4) give the same trials and nearly the same spikes. The tongue is rarely detected in the
152	choice window (no detection in 82% of trials), which bears on the video regression's handling of
153	missing keypoints (claims M5). In two sessions the video does not cover the span of the trials to
154	within 5 s; trials without keypoints take the control mean.
155	##### 10 MD
156	## Shared measures
157	
158	The early-window measures for every region entry, under each combination of the open readings
159	that bear on them: early-window placement (M4: `own`, laser trials on their own onset; `go`, all
160	trials at the median onset), missing video keypoints (M5: `fill` with the control mean; `drop`
161	the trial from the fit), and lick direction (M3: `licks`, first lick after Go; `outcome`, from
162	instruction and outcome). Laser trials with an early lick are dropped (M1 reading b), the reading
163	under which the session counts match (claim session-counts). The first combination listed,
164	`own, fill, licks`, is the one reported first. Under `drop` a control trial that lacks a
165	detection of any keypoint leaves the choice-axis fit itself, not only the regression; as the tongue
166	is undetected in the choice window on 82% of trials, the choice axis then rests on about a fifth
167	of the control trials, which is why the `drop` readings give other fractions and cosines.
168	
169	Seeds. Every random step is run under the claim's seed, the four more seeds of the protocol
[... 310 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt",
 "offset": 479,
 "limit": 300
}
```

```
479	the corrected fractions remain low, but no reading gives both printed values: correction b puts
480	medulla near 0.003 (-0.003 to 0.002) with thalamus at 0.075 to 0.077, below the 0.089 the
481	tolerance allows; correction a puts thalamus near 0.11 with medulla below zero; the single mouse
482	extremes are far from both values. No reading matches both values under any of the five seeds. Seed 17 gives the same (no reading matches both, every region mean below 0.15 under
483	all six).
484	
485	##### 32 MD
486	## fig1-1c-fraction-vs-neurons
487	
488	> Joint fractions decrease with the number of neurons in a session.
489	##### 33 CODE ['claim:fig1-1c-fraction-vs-neurons']
490	pooled over regions: Spearman rho = -0.366, p = 3e-10, n = 278 region entries
491	  ALM       rho = -0.580, p = 1.1e-09, n = 93
492	  striatum  rho = -0.283, p = 0.051, n = 48
493	  thalamus  rho = -0.213, p = 0.25, n = 31
494	  midbrain  rho = -0.371, p = 0.0015, n = 71
495	  medulla   rho = -0.413, p = 0.014, n = 35
496	reading own,fill,licks       pooled rho = -0.366
497	reading own,fill,outcome     pooled rho = -0.374
498	reading own,drop,licks       pooled rho = -0.391
[... 280 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt",
 "offset": 779,
 "limit": 460
}
```

```
779	seed +0: regions inside 5 of 5; outside: none
780	seed +1000: regions inside 4 of 5; outside: {'thalamus': [1.93, 1.55, 1.02, 0.77]}
781	seed +2000: regions inside 5 of 5; outside: none
782	seed +3000: regions inside 4 of 5; outside: {'thalamus': [1.91, 1.63, 1.03, 0.76]}
783	seed +4000: regions inside 4 of 5; outside: {'thalamus': [1.99, 1.64, 1.08, 0.79]}
784	seed 17 (paper): regions inside 4 of 5; outside: {'thalamus': [1.95, 1.59, 1.02, 0.81]}
785	
786	##### 66 MD
787	**Result: reproduced.** Under the claim's seed every region lies inside its widened range in the
788	four bins centred 225 to 375 ms after Go (ALM 0.79 to 1.33, thalamus 0.82 to 1.95, striatum 0.29 to
789	0.80, midbrain and medulla at most 0.47). Under seeds +1000, +3000 and +4000 and under seed 17 the
790	thalamus value in the bin centred 375 ms (0.76 to 0.81) falls just below the widened lower bound of
791	0.81, so four of five regions hold and the outcome there would be partially reproduced; under +2000
792	all five hold. The outcome is seed-sensitive.
793	
794	##### 67 MD
795	## Decoding (shared by table1-decoding-early-vs-prelick and fig2a-decoding-rises-after-go)
796	
797	Lick direction is decoded under both readings of M8. Reading (b), laser and control trials
798	together, is reported first, as nearly every region entry passes the Methods' rule of 40 trials
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "drop\|eight readings\|other readings" attempts/yang-2026-01.yaml | sed -n 1,80p | cut -c1-260
```

```
42:    39 bilateral sessions start near -1.2 s. With laser trials that had an early lick dropped (M1 reading
45:    49, 10 / 31, 16 / 72 and 8 / 35. The dropped reading is used first in every other claim.
62:    0.10. All four readings that fill missing keypoints give 5 of 5; the four that drop trials without
93:    under the four readings that fill missing keypoints, 7 of 10 under those that drop such trials. With
112:    sessions of 278 have a negative cosine). The readings that drop trials without a keypoint give 0.20
174:    rho -0.366 to -0.428 over the eight readings.
201:    the first reading) the rule never selects ses-20200922T135318: the three other readings that fill
203:    against 0.0019 to 0.0033), and the four that drop trials without keypoints select ses-20201230T112558
373:  notes: Closest match within the caliper, 2,667 pairs in 98 sessions (14 sessions dropped with fewer
395:  notes: Closest match, pairs without a second control dropped, per-bin distances averaged, pre-lick residual
575:    trials with an early lick were dropped (the counts of Table 1 match only then). (2) Each laser trial
578:    trials without a detection took the control mean; dropping them from the fit gives other fractions
598:    reason: 'Cell 13: 168 photoinhibition sessions. With early-lick laser trials dropped, every region
600:    response: 'No change. Point 6 of the report (only the early-lick-dropped reading of M1 carried past
610:      says that the drop reading removes about 82% of control trials from the choice-axis fit itself (point
656:    response: 'The rule is now run under all eight readings of M3 to M5, with the candidate distances.
658:      second or third, the drop readings select ses-20201230T112558 or ses-20200925T153348 and rank it
660:      session selected by the drop readings.)'
729:    reason: 'Cell 36, closest/drop/mean: 1.552 / 1.358 / 2.912 / 0.762 / 0.528, 5/5 within tolerance,
```

**Agent calls Bash**

```bash
cd  sed -n 58,70p attempts/yang-2026-01.yaml; sed -n 88,118p attempts/yang-2026-01.yaml; sed -n 196,206p attempts/yang-2026-01.yaml; grep -n "deviations" -A8 attempts/yang-2026-01.yaml | grep -i -n "keypoint" | head
```

```
- 0.0587
  - 0.0521
  notes: Joint fractions, mean across mice (first reading, own onset, keypoints filled, licks), ALM 0.0549,
    striatum 0.0601, thalamus 0.0844, midbrain 0.0587, medulla 0.0521; all within tolerance and below
    0.10. All four readings that fill missing keypoints give 5 of 5; the four that drop trials without
    a keypoint from the video fit give 1 or 2 of 5, since the tongue is undetected in the choice window
    on 82% of trials. Thalamus is highest; the lowest is medulla, not ALM (the criterion does not require
    the order). The likelihood cut (0.5, 0.9, 0.99) changes the fractions by at most 0.0017. With laser
    trials that had an early lick kept (M1 reading a; 19 / 94, 13 / 49, 10 / 31, 16 / 72, 8 / 35 entries)
    the fractions are 0.054 to 0.087, 5 of 5 within tolerance under the licks reading and 4 of 5 under
    the outcome reading, all below 0.10.
  deviations:
  - A video keypoint counts as detected when its likelihood is at least 0.9; the files give a likelihood
  - 0.0268
  - 0.0316
  - 0.025
  notes: First reading, choice fractions ALM 0.0344, striatum 0.0424, thalamus 0.0615, midbrain 0.0288,
    medulla 0.0308; action fractions 0.0220, 0.0194, 0.0268, 0.0316, 0.0250. 10 of 10 within tolerance
    under the four readings that fill missing keypoints, 7 of 10 under those that drop such trials. With
    laser trials that had an early lick kept (M1 reading a), 10 of 10 within tolerance under the four
[... 43 more lines not kept]
```

**Agent**

The axes-cosine note also quotes stale drop values (0.20 and 0.33); the new run gives thalamus 0.237 and ALM 0.383. Editing the notebook text now:

**Agent calls Bash**

```bash
cd entries/yang-2026; python - <<'E'
p='reproduce_yang_2026.ipynb'; s=open(p).read()
reps=[
("The run takes about an hour (62 minutes in the last run): about\\n\",\n    \"25 for streaming,",
 "The run takes 35 to 60 minutes, depending on the runner: about\\n\",\n    \"25 for streaming,"),
("of the control trials, which is why the `drop` readings give other fractions and cosines.",
 "of the control trials, which is why the `drop` readings give other fractions and cosines. A\\n\",\n    \"region entry with no more such trials than the regression's seven columns is left out of the\\n\",\n    \"`drop` readings (48 of 278 entries, printed below): the fit is then exact, and the residual\\n\",\n    \"choice axis is round-off that differs from one machine to another."),
("trials give 7 of 10.", "trials give 6 of 10."),
("The readings that drop trials\\n\",\n    \"without keypoints give lower cosines, outside tolerance.",
 "The readings that drop trials\\n\",\n    \"without keypoints give lower cosines (thalamus 0.24, ALM 0.38), outside tolerance."),
("readings that drop trials without keypoints select ses-20201230T112558 (three readings) or\\n\",\n    \"ses-20200925T153348 (one) and rank the paper's session 38th (its joint fraction is 0.001 there).",
 "readings that drop trials without keypoints select ses-20201230T112558 and rank the paper's\\n\",\n    \"session 34th of 39 (its joint fraction is 0.001 there)."),
]
for a,b in reps:
    assert s.count(a)==1,a[:70]
    s=s.replace(a,b)
open(p,'w').write(s)
import json; json.load(open(p))
E
sed -i 's/It takes about an hour (62 minutes in the last run), about 25 minutes of it streaming./It takes 35 to 60 minutes depending on the runner, about 25 of them streaming./' README.md; grep -n minutes README.md
```

```
16:  claims. It takes 35 to 60 minutes depending on the runner, about 25 of them streaming.
```

**Agent calls Bash**

```bash
cd entries/yang-2026; python - <<'E'
p='reproduce_yang_2026.ipynb'; s=open(p).read()
a="without keypoints give lower cosines (thalamus 0.24, ALM 0.38), outside tolerance."
b="without keypoints give lower cosines (thalamus 0.24, ALM 0.38), outside tolerance; the absolute\\n\",\n    \"cosine puts their thalamus (0.25) within it but not their ALM (0.39)."
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
import json; json.load(open(p))
E
cd  date -u; python tools/entry.py all entries/yang-2026 2>&1 | tail -3; date -u
```

```
Sat Nov 21 16:27:07 UTC 2026
Installed kernelspec registry-yang-2026 in executed/yang-2026/.venv/share/jupyter/kernels/registry-yang-2026
0 error(s)
pass  reproduce_yang_2026.ipynb  (2143 s)
Sat Nov 21 17:03:01 UTC 2026
```

**Agent**

Run passed again. Confirming the outputs match the previous run (determinism) before editing the record:

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,os
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
new=[]
for i,c in enumerate(nb['cells']):
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
    if c['cell_type']=='markdown': new.append(f'##### {i} MD\n'+''.join(c['source'])+'\n')
    else: new.append(f'##### {i} CODE {c["metadata"].get("tags",[])}\n'+out+'\n')
old=open(os.environ['TMPDIR']+'/out.txt').read()
import difflib,re
strip=lambda t:[l for l in t.splitlines() if not re.search(r' in \d+ s$|run time|peak memory',l)]
d=list(difflib.unified_diff(strip(old),strip(''.join(new)),lineterm='',n=0))
print('\n'.join(d)[:5000])
E
```

```
--- 
+++ 
@@ -22 +22 @@
-licks and video keypoints. Nothing is downloaded to disk. The run takes about an hour (62 minutes in the last run): about
+licks and video keypoints. Nothing is downloaded to disk. The run takes 35 to 60 minutes, depending on the runner: about
@@ -165 +165,4 @@
-of the control trials, which is why the `drop` readings give other fractions and cosines.
+of the control trials, which is why the `drop` readings give other fractions and cosines. A
+region entry with no more such trials than the regression's seven columns is left out of the
+`drop` readings (48 of 278 entries, printed below): the fit is then exact, and the residual
+choice axis is round-off that differs from one machine to another.
@@ -343 +346 @@
-trials give 7 of 10. With laser trials that had an early lick kept (M1
+trials give 6 of 10. With laser trials that had an early lick kept (M1
@@ -397 +400,2 @@
-without keypoints give lower cosines, outside tolerance. With laser trials that had an early lick kept (M1 reading a)
+without keypoints give lower cosines (thalamus 0.24, ALM 0.38), outside tolerance; the absolute
+cosine puts their thalamus (0.25) within it but not their ALM (0.39). With laser trials that had an early lick kept (M1 reading a)
@@ -1125,2 +1129,2 @@
-readings that drop trials without keypoints select ses-20201230T112558 (three readings) or
[... 3 more lines not kept]
```

**Agent**

The outputs are identical to the previous run, apart from the edited text. Now the record notes:

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/yang-2026/reproduce_yang_2026.ipynb'))
print(''.join(nb['cells'][94]['outputs'][0]['text']))
p='attempts/yang-2026-01.yaml'; s=open(p).read()
reps=[
("""    under the four readings that fill missing keypoints, 7 of 10 under those that drop such trials.""",
 """    under the four readings that fill missing keypoints, 6 of 10 under those that drop such trials."""),
("""The readings that drop trials without a keypoint give 0.20
    and 0.33, outside tolerance.""",
 """The readings that drop trials without a keypoint give 0.237
    and 0.383, outside tolerance; their absolute cosine puts thalamus (0.252) within it but not ALM (0.395)."""),
("rho -0.366 to -0.428 over the eight readings.","rho -0.366 to -0.432 over the eight readings."),
("""    against 0.0019 to 0.0033), and the four that drop trials without keypoints select ses-20201230T112558
    (three readings) or ses-20200925T153348 (one) and rank ses-20200922T135318 38th of 43 (its joint fraction
    is 0.0008 to 0.0009 there).'""",
 """    against 0.0019 to 0.0033), and the four that drop trials without keypoints select ses-20201230T112558
    and rank ses-20200922T135318 34th of 39 (its joint fraction is 0.0008 to 0.0009 there).'"""),
("""      second or third, the drop readings select ses-20201230T112558 or ses-20200925T153348 and rank it
      38th. Outcome unchanged. (Corrected after round 2, which found that this response named the wrong
      session selected by the drop readings.)'""",
 """      second or third, the drop readings select another session and rank it far down. Outcome unchanged.
      (Corrected after round 2, which found that this response named the wrong session; the sessions
      and ranks of the current run are in the notes.)'"""),
("""    0.10. All four readings that fill missing keypoints give 5 of 5; the four that drop trials without
    a keypoint from the video fit give 1 or 2 of 5, since the tongue is undetected in the choice window
    on 82% of trials.""",
 """    0.10. All four readings that fill missing keypoints give 5 of 5; the four that drop trials without
    a keypoint from the video fit give 1 or 2 of 5, since the tongue is undetected in the choice window
    on 82% of trials. Under those four, 48 of 278 region entries are left out, as they keep no more
    control trials than the regression's seven columns."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:70]
    s=s.replace(a,b)
open(p,'w').write(s)
E
sed -n 66,76p attempts/yang-2026-01.yaml
```

```
total run time 35.6 min; peak memory 9.4 GB

    the order). The likelihood cut (0.5, 0.9, 0.99) changes the fractions by at most 0.0017. With laser
    trials that had an early lick kept (M1 reading a; 19 / 94, 13 / 49, 10 / 31, 16 / 72, 8 / 35 entries)
    the fractions are 0.054 to 0.087, 5 of 5 within tolerance under the licks reading and 4 of 5 under
    the outcome reading, all below 0.10.
  deviations:
  - A video keypoint counts as detected when its likelihood is at least 0.9; the files give a likelihood
    per frame and no detection flag, and the paper gives no rule. Cuts of 0.5 and 0.99 change no early
    fraction or cosine by more than 0.002 (standard choice, shown in the notebook).
  - Regions are the probe targets the files give for each unit's electrode (claims M2, reading a). Reading
    b (Allen CCF parents of the per-unit annotation) was not run, as it needs the Allen ontology, an outside
    input the claims file does not name; the probe labels give exactly the paper's Table 1 counts.
```

**Agent**

Adding the deviation for the new exclusion, then the round-2 verification block:

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/yang-2026-01.yaml'; s=open(p).read()
a="""    the outcome reading, all below 0.10.
  deviations:
"""
b="""    the outcome reading, all below 0.10.
  deviations:
  - Under reading b of the video regression (claims M5, trials lacking a keypoint dropped from the fit)
    a region entry whose kept control trials are no more than the regression's seven columns is left
    out, as the fit is then exact and its residual choice axis is round-off that differs between machines
    (48 of 278 entries). The claims file and the paper set no minimum (standard choice). Added after verifier
    round 2; it changes only the drop readings, on which no outcome rests.
"""
assert s.count(a)==1; s=s.replace(a,b)
s=s.rstrip('\n')+'\n'+'''- date: '2026-11-21'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full re-executed notebook after the round-1 revision, with its conclusions and
    summary, the helper module mam.py, the claims file, the attempt record and the paper's full text.
    The verifier agreed with all 25 outcomes and found both assumptions (fig2d-choice-share-flat, fig3-1c-alm-early-residual)
    stated and reasonable. No finding is rated critical, and the verifier said none should be; it found
    finding 1 (severity none) supported by the data check and the minor ratings of findings 2 to 5 right.
    Cell numbers in the reasons are those of the round-2 copy. After this round the author found that
    the readings that drop trials without keypoints (claims M5 reading b) gave different numbers on two
    runners, as 48 region entries kept no more control trials than the regression has columns; those
    entries are now left out of that reading (a deviation under table1-early-joint-fraction), and the
    notes that cite it were updated. No outcome rests on that reading.
  results:
  - claim: session-counts
    agrees: true
    outcome: reproduced
    reason: I agree; the new runs change none of the outcomes. Laser trials kept (M1 reading a) are now
      reported.
    response: No change.
  - claim: table1-early-joint-fraction
    agrees: true
    outcome: reproduced
    reason: 'Laser trials kept (M1 reading a): cell 18 gives 5/5 joint fractions under the licks reading
      and 4/5 under the outcome reading.'
    response: No change from the report. The drop readings now leave out the 48 region entries whose
      video fit was exact (see reviewed); they give 1 or 2 of 5 as before. Outcome unchanged.
  - claim: table1-early-axis-fractions
    agrees: true
    outcome: reproduced
    reason: 'Laser trials kept (M1 reading a): cell 18 gives 10/10 axis fractions.'
    response: With the 48 exact-fit entries left out of the drop readings, those readings give 6 of 10,
      not 7; the notes and the Result cell say so. Outcome unchanged.
  - claim: axes-cosine
    agrees: true
    outcome: reproduced
    reason: 'Laser trials kept (M1 reading a): cell 18 gives both cosines within tolerance.'
    response: The drop-reading cosines in the notes (0.20 and 0.33) were stale; they are now 0.237 and
      0.383, given in the notes and the Result cell. Outcome unchanged.
  - claim: fig1e-laser-vs-control-split
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 28 says "so is the highest of the other regions (midbrain, 7.6 to 8.8)", meaning within
      tolerance under every reading. Cell 27 prints "ratio a, independent: ... highest within False" (7.56,
      against a lower bound of 7.83). The seed-17 run''s a/disjoint value, 7.69, is also outside. The attempt
      record''s "under three of four" is correct. The outcome is not affected.'
    response: Cell 28 now says the highest other region is within tolerance under three of the four readings,
      with 7.56 below 7.83 under reading a with independent groups. Outcome unchanged.
  - claim: fig1-1b-corrected-joint-fraction
    agrees: true
    outcome: partially_reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig1-1c-fraction-vs-neurons
    agrees: true
    outcome: reproduced
    reason: The attempt record says "pooled rho -0.366 to -0.423 over the eight readings". Cell 33 prints
      -0.366 to -0.428.
    response: Corrected. With the exact-fit entries left out of the drop readings, the range is now -0.366
      to -0.432 (cell 33), as the notes say. Outcome unchanged.
  - claim: fig1-1d-without-video-regression
    agrees: true
    outcome: reproduced
    reason: I agree; the new runs change none of the outcomes.
    response: No change.
  - claim: fig1b-example-session
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 89 says "the readings that drop trials without keypoints select ses-20210129T132207 and
      rank it 38th". The same claim appears in the attempt record''s fig1b notes and in the response to
      my round-1 reason. Cell 88 shows the drop readings select ses-20201230T112558 under three readings
      and ses-20200925T153348 under one. ses-20210129T132207 appears in no output. The rank of 38 and the
      joint fraction of 0.0008-0.0009 belong to the paper''s session, so "rank it" has the wrong referent.
      Cell 88 never selects the paper''s session under any of the eight readings. The outcome is not affected.'
    response: 'The wrong name came from an earlier run: the drop readings depended on round-off in sessions
      whose video fit was exact (ses-20210129T132207 keeps 2 control trials with every keypoint against
      7 regression columns), so they selected another session on each runner. Those entries are now left
      out of the drop readings, and two runs give the same selection: all four drop readings select ses-20201230T112558
      and rank ses-20200922T135318 34th of 39. Cell 89, the notes and the round-1 response now name the
      session selected and say that the rank is the paper''s session''s. The rule still never selects ses-20200922T135318.
      Outcome unchanged.'
  - claim: table1-decoding-early-vs-prelick
    agrees: true
    outcome: partially_reproduced
    reason: 'Decoding laser trials alone (M8 reading a): cell 70 gives 0-4 of 10 values within tolerance.'
    response: No change.
  - claim: fig2a-decoding-rises-after-go
    agrees: true
    outcome: reproduced
    reason: 'Decoding laser trials alone (M8 reading a): cell 73 shows the Go-aligned criterion fails in
      every part. The attempt record''s "(thalamus below 0.657)" and cell 74''s "the thalamus 250 ms bin
      0.63" omit that ALM, at 0.635 (cell 73), is also below 0.657.'
    response: The notes and cell 74 now name both thalamus (0.628) and ALM (0.635) as below 0.657. Outcome
      unchanged.
  - claim: matched-reaction-time
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig2d-choice-share-flat
    agrees: true
    outcome: partially_reproduced
    reason: 'The assumption is stated and reasonable: the partial clause is read with the criterion''s own
      SEM rule, the only definition of "rise" the criterion gives; cell 76 prints both counts (4 regions
      not rising under the SEM rule, 3 counting any increase). Remaining: partial only under the SEM-rule
      reading; counting any increase as a rise gives not reproduced. This ambiguity is in the claims file,
      and it has been asked of a reader.'
    response: No change; the question stands in questions/yang-2026.yaml.
  - claim: fig2e-action-share-rises
    agrees: true
    outcome: partially_reproduced
    reason: I agree; the new runs change none of the outcomes.
    response: No change.
  - claim: fig2b-go-aligned-joint-fraction
    agrees: true
    outcome: partially_reproduced
    reason: Cell 83 and the attempt record list medulla and thalamus as outside 0.036-0.088 in the delay
      bins. Cell 82 also lists ALM at 0.035 in the overlapping bins.
    response: Cell 83 and the notes now also name ALM (0.035, 50 ms steps). Outcome unchanged.
  - claim: fig2-1-energy-outside-subspace
    agrees: true
    outcome: partially_reproduced
    reason: I agree; the new runs change none of the outcomes.
    response: No change.
  - claim: fig3a-matched-pairs
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: table1-prelick-residual
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig3e-residual-ratio
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig3-1ab-distances-scale
    agrees: true
    outcome: reproduced
    reason: I agree; the new runs change none of the outcomes.
    response: No change.
  - claim: fig3-1d-matching-keeps-distance
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig3-1c-alm-early-residual
    agrees: true
    outcome: reproduced
    reason: 'The assumption is stated and reasonable: the early window is scored in two 50 ms bins, which
      rests on the Methods passages quoted in cell 58 and matches the paper''s 12.6 +- 2.0 almost exactly;
      cell 59 prints both readings (12.59 binned, 18.36 as one window). Remaining: reproduced only under
      the two-bin reading. The single 100 ms window the claims file''s criterion implies gives 18.36 and
      would be partial. The claims file does not name this binning as open; this is a gap in the claims
      file, now asked of a reader.'
    response: No change; the question stands in questions/yang-2026.yaml.
  - claim: fig3c-residual-time-course
    agrees: true
    outcome: reproduced
    reason: I agree; seed 17 gives the same outcome as the claim's seed.
    response: No change.
  - claim: fig3c-late-residuals
    agrees: true
    outcome: reproduced
    reason: Correctly kept at the claim's seed and flagged seed_sensitive. Reproduced at the claim's seed
      and at +2000; it is partial at +1000, +3000, +4000 and at the paper's seed 17, where thalamus is 0.76-0.81
      against a bound of 0.81. The outcome is protocol-correct and flagged, but it is fragile.
    response: No change; the notes and the Result cell give the value under each seed.
  - claim: fig3b-example-plane
    agrees: true
    outcome: partially_reproduced
    reason: I agree; the new runs change none of the outcomes.
    response: No change.
'''
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
E
python tools/entry.py check entries/yang-2026 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Check passes. Adding the run-time point to `reviewed`, then checking my text for em dashes and "rather":

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/yang-2026-01.yaml'; s=open(p).read()
a="""    notes that cite it were updated. No outcome rests on that reading.
  results:"""
b="""    notes that cite it were updated. No outcome rests on that reading. The README and the notebook header
    gave a run time of about 40 minutes, against 62.1 printed in the round-2 copy; the last three runs
    took 35 to 36 minutes, and both now say 35 to 60 minutes, depending on the runner.
  results:"""
assert s.count(a)==1; s=s.replace(a,b); open(p,'w').write(s)
E
git diff | grep "^+" | grep -n -i "—\|rather" ; python tools/entry.py check entries/yang-2026 2>&1 | tail -2; git status --short; date -u
```

```
0 error(s)
 M attempts/yang-2026-01.yaml
 M entries/yang-2026/README.md
 M entries/yang-2026/mam.py
 M entries/yang-2026/reproduce_yang_2026.ipynb
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
Sat Nov 21 17:04:20 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/yang-2026/reproduce_yang_2026.ipynb'));print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; git diff --stat
```

```
0
 attempts/yang-2026-01.yaml                  | 208 ++++++++++++++++++++++++++--
 entries/yang-2026/README.md                 |   2 +-
 entries/yang-2026/mam.py                    |   7 +-
 entries/yang-2026/reproduce_yang_2026.ipynb |  37 +++--
 4 files changed, 229 insertions(+), 25 deletions(-)
```

**Agent**

No outcome changed in this round: all 25 stay as verified, 16 reproduced and 9 partially reproduced. The verifier agreed with every one and nothing is proposed. The entry's checks pass, and the full re-run passed three times; the last two runs gave the same outputs.

**One problem I found myself.** While re-running, I saw that the "drop trials without keypoints" reading (claims M5, reading b) gave different numbers on different runners.
- **Cause:** the tongue is undetected on 82% of trials, so 48 of the 278 region entries kept 7 or fewer control trials for a 7-column video regression. ses-20210129T132207, for example, kept 2. The fit was then exact, and the resulting choice axis was round-off noise.
- **Fix:** in `mam.axes`, under that reading, an entry with no more kept trials than regression columns is now left out. The notebook prints which entries, and this is recorded as a deviation under table1-early-joint-fraction.
- **Effect:** no outcome rests on that reading, so none changes. Several numbers quoted for it did change, and I updated them in the notebook and the record:
  - table1-early-axis-fractions: the drop readings give 6 of 10 within tolerance, not 7.
  - axes-cosine: the drop-reading cosines quoted in the notes (0.20 and 0.33) were stale. They are now 0.237 and 0.383.
  - fig1-1c: pooled ρ is −0.366 to −0.432 over the eight readings.
  - fig1b: the drop readings now select ses-20201230T112558 and rank the paper's session 34th of 39.

**Corrections the verifier asked for:**
- **fig1b, wrong session named:** cell 89, the notes and my round-1 response now name the session the drop readings select, and make clear that the rank belongs to the paper's session. The mismatch the verifier saw came from the runner-dependent bug above.
- **fig1e:** the highest other region is now said to be within tolerance under three of the four readings. Under reading a with independent groups it is 7.56, below 7.83.
- **fig2a:** ALM at 0.635 is now named as below 0.657, alongside thalamus.
- **fig2b:** ALM at 0.035 (50 ms steps) is now named as outside 0.036 to 0.088.
- **Run time:** the README and notebook header said about 40 minutes. They now say 35 to 60 minutes depending on the runner: the round-2 copy took 62.1 minutes and my runs about 35.

**Recorded:** round 2 is under `verifications`, with the verifier's reasons in its own words and my responses. No finding is rated critical, and the verifier agreed none should be, so the round has no `findings` items. Its review of findings 1 to 5 is summarised under `reviewed`.

**Not done:**
- **Reader questions:** none were added. The verifier reported no new place where the claims file misreads the paper, and the two open questions (fig3-1c binning, fig2d SEM rule) already stand in `questions/yang-2026.yaml`.
- **fig3c-late-residuals:** it stays reproduced at the claim's seed and flagged `seed_sensitive`. The verifier noted it is fragile but did not dispute it.
- **Next round:** the drop-reading fix was made after the verifier's review, so it has not been verified. A reviewer should check it.

Nothing is committed.

## End of run

51 turns, 115 minutes, $2.44 at API prices, result: success.
