# pasquereau-2013 · verifier-2 · run 45875832894

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 428
drwxr-xr-x 6 runner runner    4096 Nov 26 18:44 .
drwxr-xr-x 8 runner runner    4096 Nov 26 18:44 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 26 18:44 .claude
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.development
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.local
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.production
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.test
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .env.test.local
drwx------ 2 runner runner    4096 Nov 26 18:44 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .github
-rw-r--r-- 1 runner runner       0 Nov 26 18:44 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 18:24 .mcp.json
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; diff pasquereau-2013.yaml pasquereau-2013-03.yaml | head -50; head -c 3000 pasquereau-2013.yaml; echo; head -c 3000 pasquereau-2013-03.yaml
```

```
# Pasquereau & Turner (2013) from dandiset 001636

Tests the findings of [Pasquereau and Turner (2013)](https://doi.org/10.3389/fnsys.2013.00098) that
can be tested on [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), which holds
single-unit recordings from primary motor cortex of monkeys V (Venus) and L (Leu) before and after
MPTP. Only the monkey V files mark the torque perturbations, so every claim is tested on monkey V.

| Claim | Outcome |
|---|---|
| Cells studied in monkey V, by state and projection type | Reproduced |
| Monkey L responses to wrist perturbations | Blocked: data missing |
| Baseline rate lower after MPTP for PTNs, not CSNs | Reproduced |
| PTNs fire faster than CSNs at rest | Reproduced |
| CSN antidromic latency longer after MPTP, PTN unchanged | Partially reproduced |
| False-positive rate of the response detection near 0.01 | Blocked: methods underspecified |
| 15 claims on the selected responses (prevalence, magnitude, latency, FWHM, directionality, correlations) | Blocked: methods underspecified |
| Torque-induced displacements slower and smaller after MPTP | Not reproduced |
| Latency of torque-induced displacements unchanged | Not reproduced |
| Long-latency (m2) EMG response larger after MPTP | Reproduced |
| EMG responses last longer after MPTP | Partially reproduced |
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat pasquereau-2013-03.yaml
```

```
<persisted-output>
Output too large (39.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/61ca7a2f-da94-401f-b25f-ba578c414599/tool-results/bb3iztc0y.txt

Preview (first 2KB):
schema_version: 3
id: pasquereau-2013-03
datasets:
- archive: dandi
  id: '001636'
  version: 0.261124.1906
  doi: 10.48324/dandi.001636/0.261124.1906
  relation: primary
paper: doi:10.3389/fnsys.2013.00098
date: '2026-11-26'
entry: pasquereau-2013
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "pasquereau-2013-03.yaml",
 "offset": 60
}
```

```
60	- claim: baseline-rate
61	  outcome: reproduced
62	  notebook: reproduce_pasquereau_2013.ipynb
63	  output: claim:baseline-rate
64	  measured:
65	  - 12.66
66	  - 8.85
67	  - 18.49
68	  - 14.37
69	  - 3.48
70	  - 3.36
71	  notes: Mean baseline rates (spikes/s) M1 12.66 and 8.85, PTN 18.49 and 14.37, CSN 3.48 and 3.36, all within
72	    tolerance. PTN rate lower after MPTP (-22%, Mann-Whitney p = 0.020), CSN unchanged (p = 0.65), M1 lower
73	    (-30%, p = 0.0022, below the paper's 0.05/2). The PTN test does not reach the p < 0.001 of the statement.
74	- claim: ptn-faster-than-csn
75	  outcome: reproduced
76	  notebook: reproduce_pasquereau_2013.ipynb
77	  output: claim:ptn-faster-than-csn
78	  notes: Pre-MPTP PTNs 18.49 spikes/s (n 51, range 2.6 to 49.0) against CSNs 3.48 (n 32, range 0.0 to 20.7),
79	    Mann-Whitney p = 6.3e-12. The pooled values 16.3 and 3.6 (text) and 18.3 and 3.2 (Table 1) are reported,
[... 562 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== CELL {i} [{c['cell_type']}] id={c.get('id')} tags={c.get('metadata',{}).get('tags')}")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o['output_type']=='stream': print('--OUT--'); print(''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:3000])
                if 'image/png' in d: print('[image]')
            elif o['output_type']=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "===== CELL" $TMPDIR/nb.txt | head -100
```

```
1462 /tmp/claude-1001/nb.txt
1:===== CELL 0 [markdown] id=f94066aa tags=None
43:===== CELL 1 [code] id=e27aed50 tags=None
70:===== CELL 2 [markdown] id=c5cb977f tags=None
75:===== CELL 3 [code] id=299e322f tags=None
119:===== CELL 4 [markdown] id=208caaa6 tags=None
126:===== CELL 5 [code] id=6ef15a7d tags=None
133:===== CELL 6 [code] id=20229a73 tags=None
144:===== CELL 7 [markdown] id=6cd24ca0 tags=None
146:===== CELL 8 [code] id=d7675c79 tags=['sanity']
232:===== CELL 9 [markdown] id=c11d4d1e tags=None
237:===== CELL 10 [code] id=03f6fdae tags=['sanity']
277:===== CELL 11 [markdown] id=78f988f1 tags=None
282:===== CELL 12 [code] id=6ef456c9 tags=['sanity']
323:===== CELL 13 [markdown] id=f2127f66 tags=None
331:===== CELL 14 [code] id=79f4f9b7 tags=['sanity']
373:===== CELL 15 [markdown] id=3b4d01da tags=None
382:===== CELL 16 [markdown] id=ca025f37 tags=None
392:===== CELL 17 [code] id=56d45a38 tags=['sanity']
434:===== CELL 18 [markdown] id=scale01 tags=None
[... 66 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 700
}
```

```
1	===== CELL 0 [markdown] id=f94066aa tags=None
2	# Pasquereau & Turner (2013) on DANDI:001636
3	
4	Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
5	neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
6	[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).
7	
8	Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
9	`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the
10	prompt of this attempt; it is also the newest published version (published 2026-11-24). The
11	paper cites no version.
12	
13	Claims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central
14	(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet
15	(DataSheet1.PDF), whose table gives the results for each monkey.
16	
17	The files of monkey L mark no torque perturbation, so every claim is tested on monkey V
18	(Venus, elbow), as the claims file says.
19	
20	| Claim | Tested or blocked |
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 770
}
```

```
700	print("no-torque trials, same detection: any crossing %.3f, response 20 to 60 ms %.3f (n = %d cells)"
701	      % (nt.any_crossing.mean(), nt.responds.mean(), len(nt)))
702	print("\nreadings of the test (fraction of cell-directions with any crossing over 0 to 200 ms):")
703	print(pr.groupby("onset")[["mean_sd", "ttest", "trial_se", "trial_sd"]].mean().round(3).T)
704	for label, s in [("pre", studied[~studied.post]), ("post", studied[studied.post])]:
705	    print(f"pseudo any-crossing rate {label}-MPTP: "
706	          f"{np.r_[s.pse_fle_any_crossing, s.pse_ext_any_crossing].mean():.3f}")
707	--OUT--
708	claims file's detection, pseudo onset: any crossing over 0 to 200 ms 0.230, response with onset in 20 to 60 ms 0.051 (n = 544 cell-directions)
709	no-torque trials, same detection: any crossing 0.196, response 20 to 60 ms 0.051 (n = 255 cells)
710	
711	readings of the test (fraction of cell-directions with any crossing over 0 to 200 ms):
712	onset     pseudo  torque
713	mean_sd    0.230   0.673
714	ttest      0.465   0.868
715	trial_se   0.347   0.717
716	trial_sd   0.013   0.200
717	pseudo any-crossing rate pre-MPTP: 0.257
718	pseudo any-crossing rate post-MPTP: 0.210
719	
[... 744 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('pasquereau-2013.yaml')); a=yaml.safe_load(open('pasquereau-2013-03.yaml'))
cl=c['claims'] if isinstance(c,dict) and 'claims' in c else c
ids=[x['id'] for x in cl]; print(len(ids), ids)
oc=[o['claim'] for o in a['outcomes']]; print(len(oc), set(ids)^set(oc))
from collections import Counter; print(Counter(o['outcome'] for o in a['outcomes']))
print([ (f.get('severity'),f.get('output')) for f in a['findings']])
"; grep -n -i -B2 -A12 "kinematic-latency-unchanged\|id: kinematics-slower\|id: emg-m2\|id: false-positive\|id: emg-m1" pasquereau-2013.yaml | head -200
```

```
28 ['cell-counts', 'monkey-l-perturbations', 'baseline-rate', 'ptn-faster-than-csn', 'antidromic-latency', 'false-positive-rate', 'torque-related-fractions', 'prevalence-unchanged', 'ptn-more-responsive', 'one-direction-half', 'excitatory-majority', 'magnitude-unchanged', 'venus-response-magnitudes', 'latency-shorter', 'latency-not-training', 'fwhm-shorter-ptn', 'dsi-reduced', 'venus-dsi', 'dsi-not-baseline', 'kinematics-slower', 'kinematic-latency-unchanged', 'emg-m2-larger', 'emg-duration-longer', 'emg-onset-unchanged', 'emg-m1-weak', 'velocity-matched-magnitude', 'session-correlations', 'trial-correlations']
28 set()
Counter({'blocked': 18, 'reproduced': 4, 'partially_reproduced': 3, 'not_reproduced': 3})
[('major', 'finding-leu-no-perturbations'), ('major', 'finding-kinematics-vs-paper'), ('minor', 'finding-torque-command-levels'), ('none', 'sanity'), (None, None), (None, None)]
208-    Partially reproduced when the two tests hold and a mean does not, or the reverse. A variant
209-    adds every monkey L PTN and CSN unit, as their selection by perturbations cannot be made.
210:- id: false-positive-rate
211-  statement: The detection threshold, p < 0.01 divided by 5 independent comparisons, holds the
212-    chance of a false response over the 200 ms epoch near 0.01.
213-  source: Methods, Data analysis, paragraph 6
214-  quote: The threshold for significance was adjusted to account for multiple comparisons [p <
215-    0.01/(200-ms epoch/40-ms gamma filter half-width = 5 independent comparisons) = 0.002].
216-  expected:
217-    quantity: false-positive rate per cell and direction over 0 to 200 ms
218-    value: 0.01
219-    tolerance: 0.02
220-  depends_on:
221-  - cell-counts
222-  criterion: The same detection at a pseudo onset 600 ms before the torque, on the monkey V cells
--
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
from scipy import stats
print(stats.f.sf(709.4511,1,577), stats.f.sf(596.5,1,577))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
import math
def logp(F,df):
    t=math.sqrt(F); nu=df
    lc=math.lgamma((nu+1)/2)-math.lgamma(nu/2)-0.5*math.log(nu*math.pi)
    # integrate density from t to t+20 in log-space via simple sum
    h=1e-4; s=0; x=t; ref=None
    vals=[]
    while x<t+5:
        vals.append(lc-(nu+1)/2*math.log(1+x*x/nu)); x+=h
    m=max(vals); tot=sum(math.exp(v-m) for v in vals)*h
    return (m+math.log(tot)+math.log(2))/math.log(10)
print(logp(709.4511,577), logp(596.5,577), logp(422.5,577))
"
```

```
-101.8106887241731 -90.27901158393553 -70.13073340092329
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{200\}\(0\.1 \?Nm\|Nm\b\|10°\|10 deg\|20°\|target\b\).\{200\}" 10.3389-fnsys.2013.00098.txt | head -20
```

```
7:'s axis of rotation. Flexion and extension movements rotated the manipulandum in the horizontal plane and thereby controlled the horizontal position of an onscreen cursor. A trial began when a center target appeared and the monkey made the appropriate joint movement to align the cursor with the target. The monkey maintained this position for the duration of a start-position hold period (random duration,
7:which the animal could not predict the location of the upcoming lateral target. The target then shifted to the left or right (chosen at random), and the animal moved the cursor to capture the lateral target. The animal received a drop of juice for successful completion of the task. On two-thirds of the trials (selected at random), single flexing or extending torque impulses (0.1 Nm–50 ms duration) were 
7:to the manipulandum by a DC brushless torque motor (TQ40W, Aerotech Inc., Pittsburgh PA) at an unpredictable time beginning 1–2 s (uniform randomized distribution) after initial capture of the center target. Each square-wave torque impulse induced an angular displacement of the joint (mean = 10-deg) causing a sudden stretch of arm extensor or flexor muscles. The animals were not trained to produce a spe
7:ere implanted at arm-related sites in putamen and the peduncle (Turner and Delong, 2000 ). After implantation, stimulation through the electrodes evoked arm movements similar to those observed at the target sites during microelectrode mapping. In both animals, three such electrodes were implanted in the posterior putamen between the planes of HC anterior 8 and 14, and one electrode was implanted in the
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" pasquereau-2013-03.yaml; grep -n -A8 "id: emg-m1-weak\|id: kinematics-slower" pasquereau-2013.yaml | grep -n -i "tolerance\|criterion\|value" ; sed -n 615,632p pasquereau-2013.yaml
```

```
18:703-  criterion: Session m1 and m2 of the three triceps channels for flexion torques, pre and post
    statistic: F > 49
    p: 0.01
    p_relation: "<"
  expected:
  - quantity: change of peak velocity after MPTP
    value: -16.2
    tolerance: 1.62
    unit: percent
  - quantity: change of amplitude after MPTP
    value: -6.6
    tolerance: 0.66
    unit: percent
  criterion: Session means per direction, monkey V only (the paper's ANOVA has animal as a third
    factor). Two-way ANOVA (type II) of MPTP state and direction with their interaction. The
    change is the post mean over the pre mean, minus 1. Readings, in order, (a) both directions
    pooled, (b) flexion only (Figure 1). Reproduced when both changes are within tolerance under
    one reading and MPTP reduces both measures with ANOVA p < 0.01; partially reproduced when
    both are reduced with p < 0.05 and a change is outside tolerance; not reproduced otherwise.
```

**Agent**

**Verifier report, round 2: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

Counts come from the claims file and the attempt record. There are 28 claims and 28 outcomes: 4 reproduced, 3 partially reproduced, 3 not reproduced and 18 blocked. Cell numbers below are positions in the re-executed notebook, counted from 0.

**1. Outcomes**

I agree with all 28 stated outcomes. No outcome has `assumed: true`, so there is no assumption to check.

- **cell-counts, baseline-rate, ptn-faster-than-csn: reproduced.** Agree (cells 25, 31, 34).
- **antidromic-latency: partially reproduced.** Agree (cell 37: CSN p = 0.019, above 0.0167).
- **monkey-l-perturbations: blocked, data missing.** Agree (cells 20, 28).
- **false-positive-rate and the 15 claims that depend on it: blocked, methods underspecified.** Agree. The false-positive rate is 0.230 (cell 40). The `trial_sd` reading, shown in cells 44–58, would not reproduce torque-related-fractions either (20.0% and 18.5% of M1 cells against 75 and 68% expected, cell 44).
- **velocity-matched-magnitude: blocked.** Agree. It would also stay untestable because of the data: only 2 of 581 session-directions fall in the velocity range (cell 22).
- **trial-correlations: blocked.** Agree.
- **kinematics-slower: not reproduced.** Agree by the criterion (cell 61). The torque pulse is still about twice as large after MPTP inside the "matched" 60–250 range (cell 72: median 90.9 against 181.8 units for flexion). So the faster, larger displacements cannot be separated from stimulus size.
- **kinematic-latency-unchanged: not reproduced.** I now agree; in round 1 I had it as blocked. The causal-filter variant is a valid onset measure. It gives shorter post-MPTP latencies (F = 422.5, and 146.2 within the 60–250 range; cell 66). The deciding F = 709 still comes from a measure whose post-MPTP flexion mean (3.05 ms) falls before the command leaves rest (4 ms, cell 14). The same stimulus-size confound applies.
- **emg-m2-larger: reproduced; emg-duration-longer: partially reproduced; emg-onset-unchanged: not reproduced.** Agree by the criterion (cells 73, 75, 77), with the same confound.
- **emg-m1-weak: partially reproduced.** Agree by the criterion (cell 79). Within the 60–250 range, though, the criterion is met in both states: 94.9% with median ratio 0.10 before, 97.1% with 0.26 after (cell 72).

**2. Sentences the outputs do not support**

- **Cell 59:** "No session has a mean peak velocity in the 130 to 200 deg/s range of velocity-matched-magnitude under either reading." Cell 22 shows 2 of 581 session-directions in that range, and cell 57 shows one post-MPTP flexion response there under the claims file's detection.
- **Cell 64:** "...the increase remains (+47.0% and +40.4%), so the command's arbitrary units do not explain it." Within that range the pulses still differ about twofold (cell 72: 90.9 against 181.8), so stimulus size is not excluded.
- **Cell 67** and the kinematic-latency-unchanged notes: "The variants that avoid this still find..." / "Variants that avoid this give the same outcome". The below-threshold ("quiet") variant still puts the post-MPTP flexion onset at 3.38 ms (cell 66), before the command leaves rest at 4 ms (cell 14). It removes the onsets clipped to 0 ms, but not the spread from the forwards-backwards filter. Only the causal variant avoids that.
- **Response to my round-1 point on kinematic-latency-unchanged:** "the artifact shrinks the difference but does not create it". Cell 66 shows the opposite. The pre-minus-post difference is 4.9 and 6.6 ms with the claims file's onset and 3.3 and 4.7 ms with the causal filter, and F falls from 709 to 422. The artifact enlarges the difference.
- **README:** "the EMG results hold at matched torque commands". **Cell 84 (Summary):** "the EMG claims were repeated at matched torque commands, with the same outcomes". Both fail on two counts:
  - The commands are not matched (cell 72: about 2× apart).
  - emg-m1-weak would change from partially reproduced to reproduced in that range (cell 72: 94.9% and 97.1%).
- **Finding 3 and the README:** "about three times larger (median 181.6 against 45.7 units)". Those medians differ fourfold. The means (174.7 and 58.4) give the 3× (cell 21).
- **Cell 84:** "the counts of cells ... match the paper's monkey V table". They are within 3 cells of it, not equal (cell 25: 115 against 112).
- **Cell 84:** "The post-MPTP Leu torque command moves at task events". Only one of the 34 files was timed against task events (cell 20).
- **Cell 84:** "evoked displacements (about 3 to 4 degrees)". Cell 22 gives 2.4 to 3.8.

Everything else checks against the outputs, including every number in the outcome notes.

Two smaller points on wording:
- The kinematic-latency-unchanged notes and cell 67 give "p < 1e-100", but the notebook prints this p only as 0.0000 (cell 66). From F = 709 on 1 and 577 degrees of freedom it is about 1.5e-102, so the claim is correct but not shown.
- The torque-related-fractions notes say "Blocked ... through torque-related-fractions", which names the claim as its own gate.

**My round-1 reasons in the record.** The `verifications` entry states my reasons faithfully. They keep my round-1 cell numbers, which now point to different cells: "cell 20" is now the Leu finding, and the cell counts are in cell 25. A reader following them will land in the wrong place.

**3. Round-1 points**

Resolved:
- B1: the 15 dependent claims are now shown under the `trial_sd` reading, and the possible misreading of the t-test is passed to a reader.
- B4: the angle's scale agrees with the 20-degree targets (cell 17).
- B5: source files are listed and no trial is repeated (cell 12). The 112 against 115 count difference is still unexplained but does not bear on an outcome.
- B6: Bonferroni–Holm is noted and gives the same result.
- B7: the Leu command is printed and plotted (cell 20).

Partly resolved: B2. The causal variant settles the direction of the latency change. The quiet variant does not fix the filter's spread.

Remaining, bearing on conclusions:
- **Torque size (B3).** No analysis compares the states at equal pulse size. Even within 60–250 units the post-MPTP pulse is about 2× (cell 72). This affects kinematics-slower, kinematic-latency-unchanged and all four EMG outcomes. For emg-m1-weak, the pre-MPTP shortfall disappears within that range.
- **EMG background.** The background differs by channel and state (cell 70). For triceps longus 2 the single-trial baseline SD is 2.98 before and 19.58 after MPTP. For triceps lateralis it is larger before (16.76 against 8.02) while its m2 is far smaller. That argues against a simple gain change, but the pre-MPTP m2 values (medians 4.6–10.3 units) are still near the noise.
- **New observation.** Venus perturbations come at a near-fixed 1.696 s after the centre target appears (5–95th percentile 1.696–1.732 s, cell 8). The paper says 1–2 s at random after the target is captured, which would also add a variable reaction time. The near-fixed delay suggests `center_target_appearance_time` may be reconstructed from the onset. The analog channels and spikes do line up with the onset (cell 14), so the tested claims are not affected. The Leu timing argument in cell 20 does rely on that 1.7 s. The Leu outcome stays blocked either way, because no Leu trial marks an onset.

**4. Critical findings**

No finding in the attempt record is rated `critical`. For information: finding 3 (torque command levels) is rated `minor`. I would rate it `major`. It changes the kinematic and EMG comparisons, and it cannot be worked around, since the two states barely overlap in pulse size. It is not critical, because it is evident from the command values and from the ElbowTorque description.

## End of run

13 turns, 3 minutes, $1.32 at API prices, result: success.
