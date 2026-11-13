# park-2019 · verifier-2 · run 43277390203

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 336
drwxr-xr-x 6 runner runner    4096 Nov 12 18:21 .
drwxr-xr-x 8 runner runner    4096 Nov 12 18:21 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 18:21 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 18:21 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .github
-rw-r--r-- 1 runner runner       0 Nov 12 18:21 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 18:11 .mcp.json
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat park-2019-01.yaml; echo =====; diff park-2019.yaml park-2019-01.yaml | head -50
```

```
<persisted-output>
Output too large (49.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/b94cb2bb-a531-48e5-9e27-c2c1ac8de50d/tool-results/bspxd8som.txt

Preview (first 2KB):
# Park, Keeley, Savin, Ranck & Fenton (2019) from CRCNS hc-20

Tests the findings of [Park et al. (2019)](https://doi.org/10.1016/j.neuron.2018.11.019) that can be
tested on [CRCNS hc-20](https://doi.org/10.6080/K0SF2TDN), which holds the spike trains of 115
medial entorhinal head-direction cells from 13 rats in stable, rotating and stable trials of a place
avoidance task, with the tracker files of those trials. The other MEC cells, the LFP and the
training sessions are not in it.

| Claim | Outcome |
|---|---|
| 115 head-direction cells from 13 rats (Table S1) | Partially reproduced |
| Head-direction cells fire at 1.41 AP/s | Reproduced |
| Rats learned the task (Figure 1A) | Blocked: data missing |
| Speed unchanged by rotation, lower in stable2 | Reproduced (assumption) |
| LFP power unchanged | Blocked: data missing |
| Firing rates maintained | Reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ======; cat park-2019-01.yaml
```

```
<persisted-output>
Output too large (45.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/b94cb2bb-a531-48e5-9e27-c2c1ac8de50d/tool-results/bek52glrp.txt

Preview (first 2KB):
# Park, Keeley, Savin, Ranck & Fenton (2019) from CRCNS hc-20

Tests the findings of [Park et al. (2019)](https://doi.org/10.1016/j.neuron.2018.11.019) that can be
tested on [CRCNS hc-20](https://doi.org/10.6080/K0SF2TDN), which holds the spike trains of 115
medial entorhinal head-direction cells from 13 rats in stable, rotating and stable trials of a place
avoidance task, with the tracker files of those trials. The other MEC cells, the LFP and the
training sessions are not in it.

| Claim | Outcome |
|---|---|
| 115 head-direction cells from 13 rats (Table S1) | Partially reproduced |
| Head-direction cells fire at 1.41 AP/s | Reproduced |
| Rats learned the task (Figure 1A) | Blocked: data missing |
| Speed unchanged by rotation, lower in stable2 | Reproduced (assumption) |
| LFP power unchanged | Blocked: data missing |
| Firing rates maintained | Reproduced |
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p park-2019-01.yaml
```

```
schema_version: 3
id: park-2019-01
datasets:
- archive: crcns
  id: hc-20
  version: unversioned
  doi: 10.6080/K0SF2TDN
  relation: primary
paper: doi:10.1016/j.neuron.2018.11.019
date: 2026-11-12
entry: park-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,700p park-2019-01.yaml
```

```
holds them.
- kind: other
  about: data
  statement: The stable2 file of unit 1121R157 P11C2 (named cl1) holds 26954 samples, half the
    trial, with a track that differs from the other units of the session.
- kind: metadata_insufficient
  statement: The spike timestamps run ahead of the tracker samples by about 0.05% (about 25 samples,
    0.8 s, by the end of a 30 min trial) when sample times are computed from the header's sampling
    rate and first timestamp; the data descriptor does not say how spike times relate to samples.
- kind: other
  about: data
  statement: Per rat, the dataset's head-direction cells match Table S1 except R029 (40 against 41)
    and R523 (2 against 1), and the 44 sessions give 146 simultaneously recorded head-direction
    pairs, against 142 in the Results.
- kind: methods_unavailable
  statement: Questions for the authors on momentary directional information (Figures 2C, S2, S3),
    which this attempt could not settle from the paper. Which direction bins and which trial's
    probabilities define p(n|d) and p(n) in Idir; which SD the 2 SD rule uses, given that the
    exemplar's p(ΔIdir > 2 SD) = 0.56 exceeds what the SD of the ΔIdir series itself allows; what
    margin defines no frame preference; how relative proximity to the two shock zones is computed;
[... 234 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 25,200p README.md
```

```
| All MEC pair correlations maintained (Figure S4) | Blocked: data missing |
| Model-based head-direction information (Figure S5) | Blocked: data missing |
| Subclass pair correlations maintained (Figure S6) | Blocked: data missing |
| No angular velocity tuning | Not reproduced (assumption) |
| Internally referenced tuning preserved | Not reproduced |
| Arena-frame registration short-lived (Figure 4C) | Not reproduced |
| Decoding error inhomogeneous (Figure 5A, B) | Partially reproduced |
| Error minima at 110 and 350 degrees | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several files are wrong in ways the notebook shows: the rotating tracks of five sessions (one a
copy of another session's, four with frames that disagree in timing), one unit's rotating spikes
(a copy of its stable1 spikes), and the file list's stable2 column for one session. The
outcomes are decided on the files as deposited, as the paper's counts imply it used them; a clean
variant leaves these out, and four outcomes (Figures 1C directionality, 2, S2 and 4) change or lose
their margin without them. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/park-2019-01.yaml`](../../attempts/park-2019-01.yaml).
[... 6 more lines not kept]
```

**Agent**

Read the attempt record and README; now extracting the notebook's outputs to check against.

**Agent calls Bash**

```bash
cd  python3 - <<'E' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_park_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    if c['cell_type']=='markdown': print(src)
    else:
        print(src[:1500] + ('...[src trunc]' if len(src)>1500 else ''))
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>>',''.join(o['text']))
            elif 'data' in o and 'text/plain' in o['data']: print('>>>',''.join(o['data']['text/plain'])[:3000])
            elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
E
wc -l $TMPDIR/nb.txt; grep -n '######## CELL' $TMPDIR/nb.txt | wc -l; grep -n 'ERROR' $TMPDIR/nb.txt | head
```

```
1969 /tmp/claude-1001/nb.txt
69
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
3	# Reproducing Park et al. (2019) from CRCNS hc-20
4	
5	**Paper.** Park EH, Keeley S, Savin C, Ranck JB Jr, Fenton AA (2019). How the internally
6	organized direction sense is used to navigate. *Neuron* 101:285-293.
7	[doi:10.1016/j.neuron.2018.11.019](https://doi.org/10.1016/j.neuron.2018.11.019). The claims
8	file (`claims/park-2019.yaml`) was written from the version of record, with its STAR Methods
9	and Supplemental Information.
10	
11	**Dataset.** CRCNS hc-20 (Park and Fenton 2018), [doi:10.6080/K0SF2TDN](https://doi.org/10.6080/K0SF2TDN),
12	streamed from the public bucket (`hc-20/live/data.zip`, read in place with fsspec and zipfile).
13	CRCNS data sets are not versioned, so the version is recorded as `unversioned`; the files read
14	are those of `data.zip` with MD5 `b82c7b97b0ba3491f04ecc4dbcd48e83` in the data set's
15	`checksums.md5` (the next cell checks the bucket's ETag against it). This is the only published
16	version, and the one the paper cites (by DOI), so it is the one pinned. Its data descriptor is
17	version 0.6 (14 November 2018).
18	
19	The dataset holds the 115 head-direction cells (one TSD file per cell and trial: stable1, the
20	rotating trial in room and in arena coordinates, stable2) from 13 rats in 44 sessions, and the
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 700,
 "limit": 650
}
```

```
700	Preference change: absolute circular difference of the bins of maximum rate. KLD: resistor
701	average of the two Kullback-Leibler divergences between Krichevsky-Trofimov probabilities,
702	from (a) spike counts per bin, (b) rates per bin. Tests: repeated-measures ANOVA on the three
703	trial pairs with Tukey-Kramer HSD, and a one-way ANOVA of the four groups with Dunnett's test
704	against the halves (criterion). The Tukey test is the repeated-measures one, as for
705	directionality; the between-groups test is shown beside it and gives the same order here.
706	
707	######## CELL 28 [code]
708	PAIRS_T = [("S1", "S2"), ("S1", "RR"), ("S1", "RA")]
709	def pair_measures(df):
710	    out = pd.DataFrame({"key": df.key})
711	    for a_, b_ in PAIRS_T + [("H1", "H2")]:
712	        out[f"pc_{a_}{b_}"] = hc20.circ_absdiff_deg(df[f"pref_{a_}"], df[f"pref_{b_}"])
713	        out[f"kc_{a_}{b_}"] = [hc20.kld(x, y) for x, y in zip(df[f"cnt_{a_}"], df[f"cnt_{b_}"])]
714	        out[f"kr_{a_}{b_}"] = [hc20.kld(x, y) for x, y in zip(df[f"curve_{a_}"], df[f"curve_{b_}"])]
715	    return out
716	PM = pair_measures(UM)
717	PMc = PM.copy()
718	for a_, b_ in PAIRS_T:
719	    bad = ~(clean(a_) & clean(b_))
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1349,
 "limit": 650
}
```

```
1349	IDIR = {(s, nb, src): idir_ensemble(s, nb, src) for s in ENS for nb in (36, 8) for src in ("rot", "s1")}
1350	
1351	def classify(pp, pm, margin):
1352	    if margin == "f2":
1353	        return "room" if pp > 2 * pm else ("arena" if pm > 2...[src trunc]
1354	>>> counts of ensembles by reading (expected room 4, arena 2):
1355	bins  src  sd_rule  margin
1356	10    rot  sdD      f2        room 3, arena 1, none 3
1357	                    p05       room 3, arena 1, none 3
1358	           sdS1     f2        room 4, arena 0, none 3
1359	                    p05       room 3, arena 1, none 3
1360	      s1   sdD      f2        room 1, arena 0, none 6
1361	                    p05       room 0, arena 0, none 7
1362	           sdS1     f2        room 0, arena 0, none 7
1363	                    p05       room 4, arena 1, none 2
1364	45    rot  sdD      f2        room 3, arena 1, none 3
1365	                    p05       room 4, arena 2, none 1
1366	           sdS1     f2        room 3, arena 0, none 4
1367	                    p05       room 4, arena 0, none 3
1368	      s1   sdD      f2        room 3, arena 0, none 4
[... 602 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "2919|614|best constant|best lag|matches|\.dat file" $TMPDIR/nb.txt | head -30
```

```
72:print("data.zip ETag:", etag, "; matches checksums.md5:", etag == "b82c7b97b0ba3491f04ecc4dbcd48e83")
73:>>> data.zip ETag: b82c7b97b0ba3491f04ecc4dbcd48e83 ; matches checksums.md5: True
235:  .dat files of 1211R039 agree with each other, and its arena-frame TSD track matches its
236:  arena .dat file exactly.
238:  tracks of the rotating trial disagree (median 7 to 13 px at the best constant lag) and
239:  neither matches the session's .dat files exactly; the .dat files agree with each other.
337:print(f"rotating .dat files: {len(DAT)} for {DAT.session.nunique()} sessions")
349:>>> rotating .dat files: 88 for 44 sessions
1901:  the dataset holds only the stable1, rotating, stable2 recording trials (the .dat files under
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;nb=json.load(open('reproduce_park_2019.ipynb'))
for i in (6,32,47,59,61): print('#####',i);print(''.join(nb['cells'][i]['source'])[1400:])
"
```

```
##### 6
es identical for every unit:", same_rr_ra)
seen = {}
for k, v in spk.items():
    for tr in ("S1", "RR", "S2"):
        seen.setdefault(v[tr]["t"].tobytes(), []).append((k, tr))
print("identical spike trains in different files:", [v for v in seen.values() if len(v) > 1])
##### 32
).to_string(index=False))
print("speed range over sessions (reading a, cm/s):", SP["a"].min().round(1).to_dict(), SP["a"].max().round(1).to_dict())
print(f"sessions: {len(sessions)} (the paper's degrees of freedom imply about 38)")
##### 47
50 deg, +- 10")

# robustness of reading (a), seven ensembles pooled, 660 ms: the whole curve, the third-deepest
# minimum, and a null in which each ensemble's errors are circularly shifted against its head
# directions (1000 shifts of at least a tenth of the windows; seeded generator for this section)
def mae_curve(sess, nsamp=20, shift_rng=None):
    errs, bins_ = [], []
    for s in sess:
[... 103 more lines not kept]
```

**Agent**

Notebook and record checked; now confirming the claims file's criteria for the outcomes in question.

**Agent calls Bash**

```bash
cd  grep -c "^- id:" park-2019.yaml; grep -n "^- id:" park-2019.yaml; python3 - <<'E'
import yaml
c=yaml.safe_load(open('park-2019.yaml'))
cl=c.get('claims',c)
for x in cl:
    if x['id'] in ('fig5-error-inhomogeneous','fig5c-error-minima-at-cues','fig1c-speed','fig4c-arena-registration-short-lived','figs3-no-head-direction-bias'):
        print('=====',x['id']); print(yaml.dump({k:v for k,v in x.items() if k not in ('statement',)},width=110,allow_unicode=True))
E
```

```
22
62:- id: cell-counts
86:- id: hd-cell-rate
104:- id: fig1a-avoidance-learning
134:- id: fig1c-speed
153:- id: fig1c-lfp-power
167:- id: fig1c-firing-rate
183:- id: fig1c-directionality
209:- id: fig1d-preference-change
237:- id: fig1d-instability
264:- id: fig2-decoding-stable-vs-rotating
293:- id: figs2-frame-preference
323:- id: fig2c-proximity-anticorrelation
365:- id: figs3-no-head-direction-bias
389:- id: fig3-hd-pair-correlations-preserved
417:- id: figs4-all-pair-correlations-preserved
439:- id: figs5-hd-cells-high-model-information
458:- id: figs6-subclass-correlations-preserved
474:- id: no-angular-velocity-tuning
488:- id: fig4-internal-tuning-preserved
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml,collections
a=yaml.safe_load(open('park-2019-01.yaml'))
o=a['outcomes'];print(len(o),collections.Counter(x['outcome'] for x in o),[x['claim'] for x in o if x.get('assumed')])
print(len(a['verifications'][0]['results']))
"; sed -n 365,389p park-2019.yaml | head -5
```

```
22 Counter({'reproduced': 9, 'partially_reproduced': 5, 'blocked': 5, 'not_reproduced': 3}) ['fig1c-speed', 'fig1c-directionality', 'fig2-decoding-stable-vs-rotating', 'figs2-frame-preference', 'figs3-no-head-direction-bias', 'no-angular-velocity-tuning']
22
- id: figs3-no-head-direction-bias
  statement: The frame preference ΔIdir does not vary systematically with head direction; its
    polar distribution over head direction in either frame is not biased toward the shock zones
    and does not differ from uniform.
  source: Results, Degraded Directional Tuning, paragraph 4; Figure S3 legend
```

**Agent**

**Round 2 verification: Park et al. 2019 (Neuron 101:285), CRCNS hc-20, attempt park-2019-01**

**1. Outcomes and assumptions**

The claims file has 22 claims and the attempt record has 22 outcomes: 9 reproduced, 5 partially reproduced, 3 not reproduced and 5 blocked. Six outcomes are marked `assumed: true`.

I now agree with all 22 outcomes. Two of them differ from my round 1 view:

- **fig4c:** the author changed it to not_reproduced, which matches my round 1 outcome.
- **fig5:** I now agree with partially_reproduced. The criterion gives a partial outcome when "the tests hold but not every r". Cell 44 shows that every Rayleigh and Kuiper test holds under readings (b) and (c). That partial branch is weak, because none of the four r values comes near its expected value. The possible misreading of the claims file is now a question for a reader, and the head-direction reading I asked for (cell 44) also stays below tolerance.

The six assumptions:

- **fig1c-speed:** stated and reasonable. The outcome needs either the 100 cm/s filter or the between-groups Tukey test (cell 32), and the record says so.
- **fig1c-directionality:** the repeated-measures Tukey test is stated, with a reason, and the record says the between-groups test would make this claim partially reproduced. It is reasonable, but a reader could defend either test.
- **fig2:** the "majority of seven" threshold comes from the claims file, and the record says the count depends on 1023R029. Stated and reasonable.
- **figs2:** the outcome rests on one reading out of 16; the record states this and shows the margin sensitivity. Stated and reasonable.
- **no-angular-velocity-tuning:** the test comes from the claims file. Stated and reasonable.
- **figs3: stated, but the reason given is weak, and the outcome depends on it.** The record defends n = sum of weights as "the standard n for grouped data with frequencies as weights (Zar)". The weights here are mean ΔIdir values rescaled so the largest is 1, not frequencies, so their sum depends on that arbitrary scaling. The claims file's own check points to reading (a), n = number of bins: at r = 0.17 it gives p ≈ 0.35. Under (a), 1121R157 in the room frame gives p = 0.0134 (cell 56). The criterion requires "every test p ≥ 0.05" and has no partial branch, so under (a) the claim would be not reproduced. I did not raise this in round 1.

**2. Sentences the printed numbers do not support**

- **Cell 45, and the fig5 notes:** "Rayleigh p from 2.66e-10 to 0.00459". The smallest p in readings (b) and (c) is 2.17e-20 (reading b, arena frame, cell 44). The outcome is not affected.
- **Cell 62, and the fig4 notes:** "So the gap follows the passive rotation of head direction in the room frame, a property of the measure". Three outputs in cell 61 work against this:
  - Per pair, the spike gap and the samples-only gap are uncorrelated (r = -0.01).
  - The spike gap (0.214 against 0.156) is about three times the samples-only gap (0.068 against 0.048).
  - In the clean pairs the spike gap shrinks to 0.176 against 0.149, while the samples-only gap stays at 0.070 against 0.047.

  The samples explain the direction of the shift, not the size of the gap. The outcome under the criterion is unchanged.
- **Cell 65, and the fig4c notes:** "The occupancy and after-side variants give the same pattern at 20 to 60 s." Cell 64 shows otherwise:
  - In the occupancy variant the arena frame is below the room frame at 40 to 60 s, and below all three other conditions at 60 s (p vs room = 0.0028).
  - In the after-side variant the room frame is below the arena frame at 20 s (p = 0.0167).

  The test that matters (arena frame below the other three at every interval from 20 to 60 s) fails in both variants, so the outcome stands.
- **Cell 8, and the attempt record's data findings:** cell 8 says each problem is "shown by the cells above", but no printed output shows these:
  - "median 7 to 13 px at the best constant lag"
  - that the .dat files of 1211R039 agree with each other and that its arena-frame TSD track "matches its arena .dat file exactly"
  - "2919 spikes" for 1024R157 P9C1
  - "614 of its spikes lie far from the sample" for 1017R035 P11C2

  None of this bears on a conclusion.
- **Entry README:** "takes about two minutes". Cell 67 prints 2.9 min.

Everything else checks against the printed outputs: the other "**Result:" cells, the Summary, the README's outcome table and its "four outcomes … change or lose their margin" sentence, and the other notes.

The attempt record states my round-1 reasons faithfully and in my own words. It also records my round 1 error on fig5c (63.3 was the neighbouring bin, not a minimum) and corrects it. One sentence of my round-1 fig4c reason is wrong and should be amended: "Under no variant is the arena frame below the room frame at 20 to 60 s." At 60 s the occupancy variant (p = 0.0028) and the clean variant (p = 0.0368) both put the arena frame below the room frame. The outcome does not change, because the ANOVA is already significant at 10 s.

**3. Round-1 points**

Resolved:
- 1 (no clean variants): added for decoding, Idir, proximity, Figure 5 and fig4c.
- 2 (which data governs): the notebook now says outcomes are decided on the files as deposited.
- 3 (repeated-measures Tukey not marked as an assumption): now stated as one.
- 5 (figs2 margins): margin sensitivity and the clean variant are shown.
- 6 (fig2 stable2 decoding at chance): the shifted-reference gaps are printed, and the clean variant gives 3 of 6.
- 7 (fig4 arena-vs-room KLD gap): checked in cell 61, though the conclusion drawn overreaches (section 2).
- 8 to 12 (non-conclusion points): stated where they apply.
- Section C requests: all answered (Table S1 dates, fig5c curve and null, head-direction reading), except the paper's 38 speed units, which cannot be identified from the data.
- 4 (fig5 misreading): handled as well as it can be. It is sent to a reader and run as a variant.

Remaining points that bear on a conclusion:
1. **figs3:** the n of the weighted Rayleigh test decides the outcome, and the stated reason for using the sum of weights does not hold (section 1).
2. **fig2 and figs2:** both reach their counts only with 1023R029, whose rotating tracks are shown wrong. Without it, fig2 gives 3 of 6 below the arena frame and figs2 gives 4 room and 1 arena. Both are disclosed and fragile.
3. **fig1c-directionality:** the outcome depends on which Tukey test is used and on the clean variant; it is disclosed.
4. **fig4:** the outcome flips to reproduced in the clean variant, and the explanation of the arena-vs-room gap is not established (section 2).
5. **fig5:** whether the claims file reads the paper's "polar distribution of directional error" correctly is still open, and is with a reader.

## End of run

15 turns, 3 minutes, $1.43 at API prices, result: success.
