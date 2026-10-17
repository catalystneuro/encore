# 000239 · verifier-2 · run 39032794921

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 592
drwxr-xr-x 5 runner runner    4096 Oct 17 12:38 .
drwxr-xr-x 7 runner runner    4096 Oct 17 12:38 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 17 12:38 .claude
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.development
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.local
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.production
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.test
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .env.test.local
drwx------ 2 runner runner    4096 Oct 17 12:38 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .github
-rw-r--r-- 1 runner runner       0 Oct 17 12:38 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 12:29 .mcp.json
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000239-xu-2022-01.yaml
```

```
<persisted-output>
Output too large (44.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/19bcd63b-380a-4875-8525-cdcd20078b08/tool-results/bgjlpwfbq.txt

Preview (first 2KB):
# Xu, Dong, Chen, Delgado, Hughes, Zhang & O'Connor (2022) from dandiset 000239

Tests the findings of [Xu et al. (2022)](https://doi.org/10.1038/s41586-022-04478-7) that can be
tested on [DANDI:000239](https://dandiarchive.org/dandiset/000239/0.230607.1752), which holds the
trial tables of 33 mice in a sequence licking task, tongue tracking from video, and sorted spikes
from 93 recording sessions in S1TJ, M1TJ, ALM, S1BF and other areas.

| Claim | Outcome |
|---|---|
| 1537 single and 303 multi-units from 57 sessions | Partially reproduced |
| Figure 3 session counts (8, 9, 13, 5) | Reproduced |
| 32 plus or minus 13 units per session | Reproduced |
| 2684 trials in Figure 3a | Reproduced |
| Decoding of L, L', theta, I and tau across S1TJ, M1TJ, ALM, S1BF (five claims) | Reproduced |
| The five behavioural variables are uncorrelated | Reproduced |
| Coding axes explain about half the variance of the top five PCs | Reproduced |
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/19bcd63b-380a-4875-8525-cdcd20078b08/tool-results/bgjlpwfbq.txt"
}
```

```
1	# Xu, Dong, Chen, Delgado, Hughes, Zhang & O'Connor (2022) from dandiset 000239
2	
3	Tests the findings of [Xu et al. (2022)](https://doi.org/10.1038/s41586-022-04478-7) that can be
4	tested on [DANDI:000239](https://dandiarchive.org/dandiset/000239/0.230607.1752), which holds the
5	trial tables of 33 mice in a sequence licking task, tongue tracking from video, and sorted spikes
6	from 93 recording sessions in S1TJ, M1TJ, ALM, S1BF and other areas.
7	
8	| Claim | Outcome |
9	|---|---|
10	| 1537 single and 303 multi-units from 57 sessions | Partially reproduced |
11	| Figure 3 session counts (8, 9, 13, 5) | Reproduced |
12	| 32 plus or minus 13 units per session | Reproduced |
13	| 2684 trials in Figure 3a | Reproduced |
14	| Decoding of L, L', theta, I and tau across S1TJ, M1TJ, ALM, S1BF (five claims) | Reproduced |
15	| The five behavioural variables are uncorrelated | Reproduced |
16	| Coding axes explain about half the variance of the top five PCs | Reproduced |
17	| Coding axes are largely orthogonal | Partially reproduced |
18	| Canonical correlation of coding and PC subspaces | Reproduced |
19	| ALM and M1TJ predict backtracking, S1TJ and S1BF do not | Partially reproduced |
20	| ALM encodes zigzag sequence context | Reproduced |
[... 739 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  id:\|^    id:" 10.1038-s41586-022-04478-7.yaml | head -60; grep -c "outcome:" 000239-xu-2022-01.yaml; python3 -c "
import yaml
c=yaml.safe_load(open('10.1038-s41586-022-04478-7.yaml'));print(c.keys())
a=yaml.safe_load(open('000239-xu-2022-01.yaml'))
from collections import Counter
print(len(a['outcomes']),Counter(o['outcome'] for o in a['outcomes']))
print(len(a['verifications'][0]['results']))
"
```

```
37:- id: ephys-unit-counts
56:- id: fig3-session-counts
74:- id: fig3-units-per-session
90:- id: fig3a-trial-count
103:- id: fig3c-length
126:- id: fig3c-velocity
147:- id: fig3c-angle
170:- id: fig3c-identity
192:- id: fig3c-time
212:- id: ed5b-variables-uncorrelated
221:- id: ed5e-variance-explained
238:- id: ed5f-axes-orthogonal
247:- id: fig3e-cca
262:- id: fig3f-backtracking-svm
277:- id: fig4g-zigzag-context
289:- id: ed7f-target-position-alm
300:- id: ed7h-no-time-coding
310:- id: ed4m-active-neuron-counts
331:- id: ed4l-alm-initiation
340:- id: ed4o-rhythmicity
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_xu_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    src=''.join(c['source'])
    if c['cell_type']=='code':
        print(src[:3000] + ('\n...[src truncated]' if len(src)>3000 else ''))
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>> '+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('>>> '+''.join(d['text/plain'])[:5000])
                else: print('>>> [', list(d.keys()), ']')
            elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
    else:
        print(src)
EOF
wc -l $TMPDIR/nb.txt; grep -c "CELL" $TMPDIR/nb.txt
```

```
2750 /tmp/claude-1001/nb.txt
123
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Xu et al. (2022) from dandiset 000239
4	
5	**Paper.** Xu D, Dong M, Chen Y, Delgado AM, Hughes NC, Zhang L, O'Connor DH (2022). Cortical
6	processing of flexible and context-dependent sensorimotor sequences. *Nature* 603, 464-469.
7	[doi:10.1038/s41586-022-04478-7](https://doi.org/10.1038/s41586-022-04478-7). This attempt used the
8	full text of the accepted author manuscript in PubMed Central (PMC9109820); the version of record is
9	not open access. The R2 values of Figure 3b are printed only inside the figure and were read from
10	the figure on the publisher's page.
11	
12	**Dandiset.** [DANDI:000239](https://dandiarchive.org/dandiset/000239/0.230607.1752), version
13	0.230607.1752. The paper cites no version (its data statement says data are available on request).
14	This is the only published version, so it is pinned. The draft lists the same 754 files with the
15	same sizes; it was modified later only in its metadata, none of which the analysis uses.
16	
17	**Code.** The paper says its MATLAB code is "available at GitHub" but gives no address, and no
18	repository was found. The conversion code (catalystneuro/oconnor-lab-to-nwb at commit 8d3e9e9) was
19	read: it shows that the recorded area and kind of session come only from the name of the lab's
20	data folder, kept in the session description, and that per-trial time series were placed at the
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	ALM   sub-MX180804_ses-20181125T151623     33      30      3
701	ALM   sub-MX181002_ses-20181223T145116     16      15      1
702	ALM   sub-MX181002_ses-20181224T154648     44      42      2
703	ALM   sub-MX181101_ses-20190330T112923     48      48      0
704	ALM   sub-MX181101_ses-20190331T103702     39      29     10
705	ALM   sub-MX190103_ses-20190515T110643     43      41      2
706	M1B   sub-MX180201_ses-20180403T143829     50      44      6
707	M1B   sub-MX180203_ses-20180601T162617     27      26      1
708	M1B   sub-MX180203_ses-20180602T153218     30      30      0
709	M1B   sub-MX180203_ses-20180603T173845     10      10      0
710	M1TJ  sub-MX181101_ses-20190401T114039     43      32     11
711	M1TJ  sub-MX181101_ses-20190402T123529     39      32      7
712	M1TJ  sub-MX181301_ses-20190521T122250     50      41      9
713	M1TJ  sub-MX181301_ses-20190522T105041     30      26      4
714	M1TJ  sub-MX181301_ses-20190524T135431     24      23      1
715	M1TJ  sub-MX181302_ses-20190210T163258     32      32      0
716	M1TJ  sub-MX181302_ses-20190212T154624     13      12      1
717	M1TJ  sub-MX190103_ses-20190512T114257     49      41      8
718	M1TJ  sub-MX190103_ses-20190513T110307     48      38     10
719	S1BF  sub-MX180803_ses-20181128T130139     23      20      3
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1400,
 "limit": 700
}
```

```
1400	
1401	Units per session do not depend on the seed: SD over the 35 sessions 14.4 with seed 11, as with seed 3.
1402	
1403	
1404	######## CELL 65 [markdown]
1405	With four seeds (3, 11, 12, 13) the median VE ratio of ed5e is 0.453 to 0.455, inside 0.45 to 0.55
1406	every time but always close to the lower bound. In ed5f, L' and theta have a mean absolute cosine of
1407	0.302 to 0.320 and are the only pair at or above 0.3 under every seed, so the partial outcome does
1408	not depend on the seed. The mean R2 of the five decoded variables changes little across seeds
1409	(range printed above).
1410	
1411	######## CELL 66 [markdown]
1412	## fig3e-cca
1413	
1414	> After canonical correlation, ALM trajectories in the top three PCs correlate best with the theta, I, tau coding subspace (group 2), more than with L, L', theta (group 1) or all five variables with five PCs (group 3); in S1TJ and M1TJ the correlation is high only when the coding subspace includes L and L'.
1415	
1416	######## CELL 67 [code]
1417	cc = pd.DataFrame([{"area": o["area"], "g1": o["cca"][1], "g2": o["cca"][2], "g3": o["cca"][3]} for o in f3])
1418	print("Mean canonical correlation by group (mean over sessions):")
1419	print(cc.groupby("area")[["g1", "g2", "g3"]].mean().round(3).loc[FIG3].to_string())
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 2100,
 "limit": 700
}
```

```
2100	ff = []
2101	for m, d in lt.groupby("subject"):
2102	    first = d[d.session == d.session.min()]
2103	    std = d[d.type == "standard"]
2104	    ff.append({"subject": m, "learning_files": d.session.nunique(), "first_file": d.session.min()[:10],
2105	               "last_file": d.session.max()[:10], "first_other_session": str(other_first.get(m, ""))[:10],
2106	               "first_file_trials": len(first), "first_file_types": dict(Counter(first.type)),
2107	               "init_first100": std.init.iloc[:100].median(), "speed_first100": std.speed.iloc[:100].median(),
2108	               "standard_in_last500": int((d.iloc[-500:].type == "standard").sum())})
2109	ff = pd.DataFrame(ff).set_index("subject")
2110	print(ff.round(3).to_string())
2111	print(f"\nMice whose first file has no standard trials: {int(ff.first_file_types.map(lambda x: 'standard' not in x).sum())}; "
2112	      f"mice whose first 100 standard trials already have a median initiation time under 1 s: {int((ff.init_first100 < 1).sum())} of {len(ff)}")
2113	print("Mice with fewer than 10 standard trials among their last 500 trials (no final value):",
2114	      list(ff.index[ff.standard_in_last500 < 10]))
2115	print("\nposIndex patterns of the first learning file of each mouse (top 3):")
2116	for m, d in lt.groupby("subject"):
2117	    t = [t for t in learn if t["subject"] == m and t["session_start"] == d.session.min()][0]
2118	    print(f"  {m}: {Counter(t['trials']['posIndex']).most_common(3)}")
2119	>>>           learning_files  first_file   last_file first_other_session  first_file_trials               first_file_types  init_first100  speed_first100  standard_in_last500
[... 632 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,120p 10.1038-s41586-022-04478-7.yaml
```

```
# Claims for Xu, Dong, Chen, Delgado, Hughes, Zhang & O'Connor (2022), Nature 603, 464-469, on
# dandiset 000239.
# Source: the accepted author manuscript in PubMed Central (PMC9109820), full text, read from its
# Results, Methods and figure legends. The version of record is not open access. The R2 values of
# Figure 3b are printed only inside the figure; they were read from the figure image on the
# publisher's page (Figure 3), which was viewed but not copied.
#
# The paper's analysis code is said to be "available at GitHub" with no address; no repository was
# found (see the attempt record). The conversion code (catalystneuro/oconnor-lab-to-nwb, commit
# 8d3e9e962ac1d65aa54e5e86e309e03f6850c105) was read; it shows how times and tables were built.
#
# When these criteria were written, the author had seen the data check (the file list, the
# session descriptions, which name the recorded area or the kind of session, the trial patterns
# of every file, the trial table columns, the units table, unit counts per file, and the clock
# agreement of the video with the touch times in one session) and had run the decoding of the
# five variables of Figure 3 on one ALM session (MX170903, 2018-03-04) to time it; it gave R2 of
# 0.07 (L), 0.03 (L'), 0.54 (theta), 0.77 (I) and 0.54 (tau). No other analysis had been run.
#
# Method choices fixed here where the Methods leave them open:
# - Sessions of Figure 3 are the files whose description names ALM (13), M1TJ (9), S1TJ (8) and
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 221,520p 10.1038-s41586-022-04478-7.yaml | grep -v "^  - quantity\|^    value\|^    tolerance\|^  expected"
```

```
- id: ed5e-variance-explained
  statement: Across regions, the summed variance explained by the five coding axes reached about
    half that of the top five principal components.
  source: Results, "Hierarchical population coding"; Extended Data Fig. 5e
  depends_on:
  - fig3c-length
  - fig3c-velocity
  - fig3c-angle
  - fig3c-identity
  - fig3c-time
    quantity: median over sessions of summed VE of coding axes over summed VE of top 5 PCs
  criterion: The coding axes are the unit vectors of the elastic net weights; their VE is the
    variance of the projected normalised rates over the total variance, on -0.5 to 0.8 s around
    the middle touch of the selected standard trials. An axis with all weights zero has VE 0.
- id: ed5f-axes-orthogonal
  statement: The five coding axes were largely orthogonal to each other.
  source: Results, "Hierarchical population coding"; Extended Data Fig. 5f
  depends_on:
  - ed5e-variance-explained
  criterion: The absolute cosine of each pair of coding axes, averaged over sessions where both
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 402,422p 10.1038-s41586-022-04478-7.yaml; sed -n 360,372p 10.1038-s41586-022-04478-7.yaml; python3 -c "
import json;nb=json.load(open('reproduce_xu_2022.ipynb'));print(nb['metadata'].keys())
ts=[c.get('metadata',{}).get('execution',{}) for c in nb['cells'] if c['cell_type']=='code']
print(ts[0],ts[-1])"
```

```
- id: ed2-backtracking-counts
  statement: Backtracking analyses used 7458 standard and 2695 backtracking sequences from 47
    sessions of the 9 mice trained on backtracking.
  source: Extended Data Fig. 2c,e legends; Methods, "Behavioural training"
  expected:
  - quantity: sessions
    value: 47
    tolerance: 4.7
  - quantity: standard sequences
    value: 7458
    tolerance: 745.8
  - quantity: backtracking sequences
    value: 2695
    tolerance: 269.5
  - quantity: mice
    value: 9
    tolerance: 0
  criterion: Sessions with backtracking trials ([1 2 3 1 4 5 6] or [5 4 3 5 2 1 0]). Readings,
    (a) all such non-learning files, (b) the same without the air and earplug control sessions,
    (c) as (b) without the opto efficiency sessions. Reproduced when all four values are within
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -o paper/pmc9109820.xml "https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=GetRecord&identifier=oai:pubmedcentral.nih.gov:9109820&metadataPrefix=pmc"; ls -la paper; head -c 300 paper/pmc9109820.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import re,html
x=open('paper/pmc9109820.xml').read()
t=re.sub(r'<[^>]+>',' ',x);t=html.unescape(re.sub(r'\s+',' ',t))
open('paper/pmc9109820.txt','w').write(t)
import re
for k in ['earplug','air flow','odor','100th','only touch onsets','25683','17 mice','insignificant','trend','n = 8 mice','8 mice','consummatory licks','1500','proficien']:
  for m in re.finditer(k,t):
    print('==',k,':',t[max(0,m.start()-250):m.start()+250]);
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import re
t=open('paper/pmc9109820.txt').read()
for k in ['Extended Data Fig. 1l','Learning curves','shaping','trials of training','9 mice','Phy']:
  for m in re.finditer(k,t):
    print('==',k,':',t[max(0,m.start()-400):m.start()+500]);print()
" | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round 2 verifier report: Xu et al. 2022 on DANDI 000239 (version 0.230607.1752)**

The paper text is from PMC9109820, saved as `paper/pmc9109820.xml` and `paper/pmc9109820.txt`. Cell indices below are the code-cell positions in the re-executed notebook. They differ from round 1 because cells were added.

## 1. Outcomes

The claims file has 39 claims. The attempt record has 39 outcomes: 20 reproduced, 5 partially reproduced, 3 not reproduced and 11 blocked (9 metadata_insufficient, 1 data_missing, 1 methods_underspecified).

I agree with all 39 outcomes under the criteria in the claims file.

- **fig3-units-per-session (reproduced):** this rests on reading (b), the 57 sessions. Reading (a), the 35 sessions the record itself says the claim refers to, has an SD of 14.4 against a limit of 14.3 (cell 31). That result does not depend on the seed. The criterion allows either reading.
- **ed2-backtracking-counts (not reproduced):** this would still hold under the 47-session variant (cells 104–105). That variant has 8 mice, and 8891 standard and 3207 backtracking trials before the extra filters.

## 2. Statements the printed numbers do not support

**Conclusions and summary in the notebook**

- **Cell 26** (repeated in the record's ephys-unit-counts notes): "only a 20% contamination threshold gives a count inside the tolerance (295)". Cell 23 prints two other variants inside 272.7–333.3:
  - "contamination <= 15% only": 331 multi-units
  - "RPV <= 0.5% only": 309 multi-units
- **Cell 106:** "it shows that the paper's numbers can be reached with its own exclusions".
  - The last step, initiation under 1 s, is the Figure 3 trial selection, as cell 105 says. It is not an exclusion the Methods give for Extended Data Fig. 2.
  - The variant has 8 mice, against the paper's 9.
  - Before that step the counts are 8627 and 3104, both above tolerance.
- **Cell 102** (also in the record): "every mouse's first file already holds only standard sequences". Cell 101 shows "other" trials in the first files of MX170903 (2), MX180803 (1) and MX181002 (1). This is minor.
- **Cell 121:** it treats the Methods' remark that mice "did not have experience with earplugs prior to the earplug session" as support for the earplug session being the earlier one. The remark says nothing about session order. The claim stays blocked either way.
- **Cell 14:** "stimulus and acquisition are empty". Cell 13 prints `stimulus` as holding `presentation` and `templates`. Their contents are not shown.

**Attempt record notes and responses**

- **ed7f notes:** "With trial folds 0.159 against 0.028 to 0.034". Cell 76 gives 0.022 for S1BF, so the range is 0.022 to 0.034.
- **ed2e notes:** "The touch tolerance (0 to 25 ms) changes the mean to 1.846".
  - Cell 108 gives 1.846 at both 0 and 25 ms, so the tolerance has no effect.
  - The variant loop also skips the video-end check and the filter on sessions with backtracking. That different trial set is what moves the mean from 1.854.
- **ephys-unit-counts response:** "The criterion's 15% gives 339 under the first two". The 0.5 ms censored-period estimate gives 341 (cell 23).

**Entry README**

- "It takes about 20 to 25 minutes on four cores". The execution timestamps run from 12:31:15 to 12:37:53, about 7 minutes. No core count is printed. The verification response says "about 21 minutes".
- "93 recording sessions in S1TJ, M1TJ, ALM, S1BF and other areas". The 93 files with units include the 14 opto efficiency recordings (cell 3). They are not recording sessions in the sense of the 57.
- "Optogenetic inhibition and control experiments (nine claims)". The nine include ed1f-lick-force, which is a calibration claim.

Everything else in the conclusions, the summary, the README and the record's notes matches the printed outputs. I checked each number against its cell. The two paper facts the record relies on match the paper text:
- Air flow on first in two mice and off first in four.
- Extended Data Fig. 7b shows 8 mice.

**My round-1 reasons as stated in the record**

They are faithful paraphrases. Two omissions:
- None of the fig3c reasons includes my point that I could not verify the Figure 3b targets, which were read from the figure image. All five fig3c outcomes depend on those values.
- My point that the effect of the missing inter-lick-interval standardisation on ed4m and ed4o was not quantified appears in no reason. I had marked it as not affecting a conclusion.

## 3. Round-1 points

**Resolved**
- Seed sensitivity for ed5e, ed5f and the units SD (cell 64). ed5e stays inside its range under all four seeds, and ed5f stays partial.
- Greedy trial selection (cell 35).
- Single/multi split per session and the alternative contamination estimates (cells 23–25).
- ed2 trial-level filters (cell 105).
- ed6b distribution and the video-based bout threshold (cell 111).
- First learning file contents and early speeds for ed1l-proficiency (cell 101).
- MX181003 handled by a variant (cell 97).
- fig3f: behaviour difference and PCA fitted before cross-validation, now in the conclusion and deviations.
- ed4l: S1BF and the per-second fractions (cell 85).
- ed7f: one value per mouse (cell 76).
- Opto and control metadata, the `opto` column values and the force `conversion` attribute (cell 13).
- Label-free checks for ed1i, ed1j and ed1k (cells 118–120).
- Random folds documented as a deviation.

**Remaining that bears on a conclusion**
1. **fig3c (all five claims):** the expected means and SDs come from the Figure 3b image, and I still cannot verify them.
2. **ephys-unit-counts:** the partial outcome depends on details of the contamination estimate. Dropping either criterion puts the multi-units inside tolerance. Cell 26 and the record need correcting on this point, though the outcome under the fixed criterion stands.
3. **ed1l-proficiency-1500:** it is still unsettled whether the learning files start at the start of training. The paper says training began with the complete task, which fits standard-only first files. But 3 of 15 mice are already fast in their first 100 trials. Reading (a) also saturates within about 200 trials, so the not-reproduced outcome partly reflects how proficiency was defined.
4. **fig3-units-per-session:** the reading the record says the claim refers to fails the SD limit by 0.1. The outcome is reproduced only under the wider reading.

## End of run

16 turns, 3 minutes, result: success.
