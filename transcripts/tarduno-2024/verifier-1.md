# figshare-24639285 · verifier-1 · run 40577275988

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.y*ml *.json 2>/dev/null | head -300
```

```
total 308
drwxr-xr-x 6 runner runner    4096 Oct 27 20:25 .
drwxr-xr-x 7 runner runner    4096 Oct 27 20:25 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 27 20:25 .claude
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.development
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.local
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.production
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.test
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .env.test.local
drwx------ 2 runner runner    4096 Oct 27 20:25 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .github
-rw-r--r-- 1 runner runner       0 Oct 27 20:25 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 20:21 .mcp.json
[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 300,600p 10.1038-s41597-024-03626-0.yaml; cat apollo.py
```

```
- {quantity: 12021g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}
  - {quantity: 12021g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}
  - {quantity: 12040g1 M590 20 uT, value: 8.002e-9, tolerance: 8.0e-10, unit: emu}
  - {quantity: 12040g1 max intensity, value: 0.20, tolerance: 0.020, unit: uT}
  - {quantity: 12040g2 M590 20 uT, value: 6.021e-9, tolerance: 6.0e-10, unit: emu}
  - {quantity: 12040g2 max intensity, value: 0.27, tolerance: 0.027, unit: uT}
  - {quantity: 12040g3 M590 20 uT, value: 6.292e-9, tolerance: 6.3e-10, unit: emu}
  - {quantity: 12040g3 max intensity, value: 0.26, tolerance: 0.026, unit: uT}
  - {quantity: 12053g1 M590 20 uT, value: 5.283e-9, tolerance: 5.3e-10, unit: emu}
  - {quantity: 12053g1 max intensity, value: 0.31, tolerance: 0.031, unit: uT}
  - {quantity: 12053g2 M590 20 uT, value: 7.982e-9, tolerance: 8.0e-10, unit: emu}
  - {quantity: 12053g2 max intensity, value: 0.20, tolerance: 0.020, unit: uT}
  - {quantity: 14053g1 M590 20 uT, value: 3.203e-9, tolerance: 3.2e-10, unit: emu}
  - {quantity: 14053g1 max intensity, value: 0.51, tolerance: 0.051, unit: uT}
  - {quantity: 14053g2 M590 20 uT, value: 5.294e-9, tolerance: 5.3e-10, unit: emu}
  - {quantity: 14053g2 max intensity, value: 0.31, tolerance: 0.031, unit: uT}
  - {quantity: 14053g3 M590 20 uT, value: 4.523e-9, tolerance: 4.5e-10, unit: emu}
  - {quantity: 14053g3 max intensity, value: 0.36, tolerance: 0.036, unit: uT}
  - {quantity: 71055g1 M590 20 uT, value: 3.883e-9, tolerance: 3.9e-10, unit: emu}
  - {quantity: 71055g1 max intensity, value: 0.42, tolerance: 0.042, unit: uT}
[... 469 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
        if o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1207 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown
2	# Replicate Apollo sample magnetizations (Tarduno, Cottrell & Zhou 2024) on Figshare 24639285
3	
4	Paper: J. A. Tarduno, R. D. Cottrell, T. Zhou, "Dataset of replicate Apollo sample magnetizations
5	bearing on impacts and absence of a long-lived lunar dynamo", Scientific Data (2024),
6	doi:10.1038/s41597-024-03626-0.
7	
8	Dataset: Figshare item 24639285, version 1, doi:10.6084/m9.figshare.24639285.v1. Version 1 is the
9	only published version (the API lists no other), and it is the one the paper cites (ref. 26) and the
10	claims file names, so it is pinned. The cell below prints the MD5 (`computed_md5`) of every file read.
11	The files are streamed from Figshare's download service into memory; nothing is written to disk.
12	
13	Claims: `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`, written from the version of
14	record (Europe PMC PMC11271266, full text with Methods, Technical Validation, figure legends and
15	Tables 1 and 2; the paper has no supplement and no PDF was supplied).
16	
17	| Claim | Tested here |
18	|---|---|
19	| glass-specimen-set (link) | tested |
20	| glass-success-rate | tested |
[... 628 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 649,
 "limit": 560
}
```

```
649	    ss38 250        9  16.3   3.7   9.3   2.1           True                             NaN
650	    ss45 250      120  33.0  21.4 131.7  85.5           True                             NaN
651	pTRM checks matching under some reading: 6/10
652	
653	=== [18] markdown
654	## fig1-linear-components
655	
656	> Glass subsamples ss43 and ss19, which failed the reliability criteria, show hints of linear
657	> directional components on orthogonal vector plots, from which nominal paleointensities can be
658	> calculated with the 18 uT laboratory field.
659	
660	Criterion: over the Table 2 ranges, MAD and R2 as in table2-fit-statistics, and the nominal
661	paleointensity as the absolute slope times 18 uT (Figure 1 legend). Holds when both MADs and R2
662	values match Table 2 under one reading.
663	=== [19] code
664	for how in ("mean", "first"):
665	    f = fits[how].set_index("specimen")
666	    for s in ("ss43", "ss19"):
667	        n, t0, t1 = T2[s][:3]
668	        a = A.in_range(A.arai(glass[s]["data"], how), t0, t1)
[... 540 more lines not kept]
```

**Agent**

Notebook and helper read. Now checking helper functions on synthetic inputs, the paper's passages, and the archive file list.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, apollo as A
rng=np.random.default_rng(0)
# MAD line: points along a line with known perpendicular noise
d=np.array([1,0,0.]); X=np.outer(np.linspace(1,5,5),d)+rng.normal(0,0.05,(5,3))
print("mad free", A.mad_line(X), "anch", A.mad_line(X,True))
# exact line -> 0
print("exact", A.mad_line(np.outer([1,2,3],[1,1,0])))
# plane
P=rng.normal(size=(6,3)); P[:,2]=0; print("plane exact", A.mad_plane(P))
# fisher on identical dirs, watson p on random
u=np.tile([0,0,1.],(3,1)); print(A.fisher(u))
f=A.fisher(rng.normal(size=(5,3))); print(f, A.watson_p(f['n'],f['R'],1))
# Watson p calibration: fraction of random sets with p<0.05
ps=[]
for s in range(300):
    Y=rng.normal(size=(4,3)); f=A.fisher(Y); ps.append(A.watson_p(4,f['R'],s,20000))
print("false pos rate n=4", np.mean(np.array(ps)<0.05))
print([A.step_kind(s) for s in ["0","0.0","100","100.0","250.1","250.2","590.3","590.4","10mT","2.5mT"]])
# scaled_copies false positive on random 4-sig-digit replicates
fp=0
for s in range(2000):
    v=np.array([float(f"{x:.4g}") for x in rng.normal(1e-8,1e-10,4)])
    fp+=A.scaled_copies(v)
print("scaled_copies false positives /2000:", fp)
fp=0
for s in range(2000):
    v=np.array([float(f"{x:.1f}") for x in rng.uniform(100,300,1)[0]+rng.normal(0,2,4)])
    fp+=A.scaled_copies(v)
print("dec 1-decimal false positives /2000:", fp)
# plane MAD < free line MAD for random 3 and 4 point sets
for n in (3,4):
    c=0
    for s in range(2000):
        Z=rng.normal(size=(n,3)); c+= A.mad_plane(Z)<A.mad_line(Z)
    print(n,"pts: plane<line fraction on random", c/2000)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null; which -a python3 python; for p in $(which -a python3 python 2>/dev/null); do $p -c "import numpy,pandas;print('$p ok')" 2>/dev/null; done; uv --version 2>/dev/null; pip --version
```

```
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
pipx
pipx_bin
post-generation
primer
runner-cache
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && uv pip install -q -p v/bin/python numpy pandas fsspec openpyxl 2>&1 | tail -3; v/bin/python -c "import numpy;print(numpy.__version__)"
```

```
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, apollo as A
rng=np.random.default_rng(0)
d=np.array([1,0,0.]); X=np.outer(np.linspace(1,5,5),d)+rng.normal(0,0.05,(5,3))
print("mad free", A.mad_line(X), "anch", A.mad_line(X,True))
print("exact", A.mad_line(np.outer([1,2,3],[1,1,0])))
P=rng.normal(size=(6,3)); P[:,2]=0; print("plane exact", A.mad_plane(P))
print(A.fisher(np.tile([0,0,1.],(3,1))))
ps=[]
for s in range(300):
    Y=rng.normal(size=(4,3)); f=A.fisher(Y); ps.append(A.watson_p(4,f['R'],s,20000))
print("Watson false pos rate n=4", np.mean(np.array(ps)<0.05))
ps=[]
for s in range(300):
    Y=rng.normal(size=(2,3)); f=A.fisher(Y); ps.append(A.watson_p(2,f['R'],s,20000))
print("Watson false pos rate n=2", np.mean(np.array(ps)<0.05))
print([A.step_kind(s) for s in ["0","0.0","100","100.0","250.1","250.2","590.3","590.4","10mT","2.5mT"]])
fp=0
for s in range(2000):
    v=np.array([float(f"{x:.4g}") for x in rng.normal(1e-8,1e-10,4)]); fp+=A.scaled_copies(v)
print("moment false positives /2000:", fp)
fp=0
for s in range(2000):
    v=np.round(rng.uniform(100,300)+rng.normal(0,2,4),1); fp+=A.scaled_copies(v)
print("dec 1-decimal false positives /2000:", fp)
for n in (3,4):
    c=0
    for s in range(2000):
        Z=rng.normal(size=(n,3)); c+= A.mad_plane(Z)<A.mad_line(Z)
    print(n,"pts random: plane<line fraction", c/2000)
    c=0;c2=0
    for s in range(2000):
        Z=np.outer(np.linspace(1,2,n),[1,0,0])+rng.normal(0,0.1,(n,3)); c+= A.mad_plane(Z)<A.mad_line(Z)
        c2+= A.angle(Z[0],Z[-1])>A.mad_line(Z)
    print(n,"pts noisy single line: plane<line", c/2000, " first-last angle>MAD", c2/2000)
EOF
```

```
mad free 1.4127456807892633 anch 0.7126771233590302
exact 0.0
plane exact 0.0
{'n': 3, 'R': 3.0, 'dec': 0.0, 'inc': 90.0, 'k': nan, 'a95': 0.0}
Watson false pos rate n=4 0.06666666666666667
Watson false pos rate n=2 0.06
[('nrm', 0.0), ('nrm', 0.0), ('off', 100.0), ('off', 100.0), ('on', 250.0), ('check', 250.0), ('alt', 590.0), ('on40', 590.0), ('af', 10.0), ('af', 2.5)]
moment false positives /2000: 0
dec 1-decimal false positives /2000: 0
3 pts random: plane<line fraction 0.5755
3 pts noisy single line: plane<line 0.3035  first-last angle>MAD 0.3805
4 pts random: plane<line fraction 0.5625
4 pts noisy single line: plane<line 0.214  first-last angle>MAD 0.182
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "success|AF clean|pre-treat|replicate|first measure|M590|Table 1|averag|mean" paper/*.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.figshare.com/v2/articles/24639285/versions | head -c 600; echo; curl -s https://api.figshare.com/v2/articles/24639285 | $TMPDIR/v/bin/python -c "import json,sys;m=json.load(sys.stdin);print(m['version'],m['doi']);[print(f['id'],f['name'],f['size'],f['computed_md5']) for f in m['files']];print(m['description'][:1500])"
```

Result: the fetched text is not kept.

**Agent**

**Verifier report, round 1: Tarduno, Cottrell & Zhou 2024 (FIGSHARE:24639285 v1)**

The claims file has 17 claims. The notebook tests 16 and treats `interpretation-impact-no-dynamo` as blocked. I checked the archive through the Figshare API: version 1 is the only version, and its 16 files (13 xlsx, 3 pdf) have the same IDs and MD5s as notebook cell 1.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| glass-specimen-set | reproduced | Cell 8: 22 of 22 Table 2 glass specimens and 12 of 12 Table 1 crystals are present with step, moment, Dec and Inc. 10 glass specimens have AF steps, the same set as the Table 2 marks. Four of the glass sheets are not real replicate measurements (problem 1). |
| glass-success-rate | reproduced | Cell 10: 3/(3+22) = 12.0%. Without AF: 12+1 = 13; with AF: 10+2 = 12, which matches Methods paragraph 2. |
| table2-fit-statistics | partially_reproduced | Cells 12–13: n matches for all nine. With replicates averaged, 23 of 29 values match (79%), just under the 80% bar. The misses are ss10 MAD (33.3 vs 42.9), R2 for ss9, ss10 and ss34, and pTRM checks for ss19 at 250 °C and ss30 at 450 °C. Using only the first measurement gives 38%. Holding a single pTRM reading fixed gives about 66% (19/29), so the outcome is partial either way. |
| table2-no-fit | reproduced | Cell 16: 11 of 11 are irregular under reading (a) and 9 of 11 under (b). ss36 and ss39 grow away from the origin over their last step (1.77→6.00 and 2.31→9.67 ×1e-9 emu). Reading (b) passes exactly at the threshold, and 3 of its 9 are synthetic sheets (problem 1). |
| fig1-linear-components | reproduced | Cell 19, averaged replicates, free-line MAD: ss43 MAD 10.3 vs 10.0 and R2 0.902 vs 0.90; ss19 MAD 30.1 vs 30.1 and R2 0.956 vs 0.94. Nominal paleointensities are 9.6 and 23.0 µT (8.5 and 23.7 µT with first measurements). They cannot be compared with Figure 1 because the figure was not seen. |
| fig2-changing-field | reproduced | Cell 21, averaged replicates: both specimens pass readings (a) and (b), and R2 is 0.384 and 0.378 against 0.38. Both readings are weak tests (problem 6). The "curved Arai plot" part of the statement is not tested. |
| glass-directions-not-random | partially_reproduced | Cell 23: 8 of 22 specimens reject randomness with averaged replicates and 9 of 22 with first measurements. Inside the Table 2 ranges it is 8 and 7 of 22. Every count falls in the claim's quarter-to-half band. |
| glass-af-no-change | reproduced | Cell 25: 8 of 10 show no significant change under readings (a) and (b), which is the allowed maximum of two exceptions. The exceptions are ss38 (moment ratio 0.49) and ss48, a synthetic sheet. |
| table1-max-intensity | reproduced | Cell 27: 24 of 24 values match under readings a_ii, b_i and b_ii. Table 1's M590 equals the plain magnitude of the 590.1 measurement for all 12 crystals to 4 significant figures (problem 4). Applying the formula to Table 1's own M590 column gives 4 of 12 values equal to two places, and 10 of 12 if Table 1 rounded up. |
| baseline-range | reproduced | Cell 29: the values run from 0.200 µT (12040g1) to 0.500 µT (14053g1), inside 0.18–0.22 and 0.45–0.55. |
| example-14053g1-threshold | partially_reproduced | Cell 31: for 14053g1 the TRM is 3.2e-12 A m² and the threshold 0.50 µT, so the example as written fails. For 12040g1 the numbers are 8.0e-12 A m² and 0.20 µT, so it matches only if the crystal name is a misprint. |
| fig3-nrm-consistent | reproduced | Cell 33: NRM replicates are consistent for 10 of 12 crystals under reading (a) and 8 of 12 under (b), including 12040g1 and 14053g2. Most crystals have only n = 2 NRM measurements. |
| fig3-590-inconsistent | reproduced | Cell 33: 590.0 replicates are inconsistent for 12 of 12 under reading (b) and 10 of 12 under (a), including both named crystals. |
| fig3-alteration-check-inconsistent | reproduced | Cell 33: 590.3 replicates are inconsistent for 12 of 12 under reading (b). |
| crystal-14053g1-400c-stable | reproduced | Cell 35: the three 400 °C replicates give k 78 and Watson p 0.0003; 590.0 gives k 1.0 and p 0.785. Reading (a) holds. Reading (b) fails (9.3° from the NRM mean against an α95 of 4°), but the criterion needs only one. |
| no-alteration-recording-efficiency | reproduced | Cell 37: all 12 pass reading (b), with TRM40/(2·TRM20) between 0.77 and 1.17. Reading (a) passes only 11 of 12 (first measurement) or 10 of 12 (mean). The result rests on a loose cutoff (problem 7). |
| interpretation-impact-no-dynamo | blocked (other) | The claims file marks it as an interpretation resting on ref. 1 and impact-plasma models. Nothing in the deposit can test it beyond the four claims it depends on, which are tested above. |

### B. Problems

1. **[does not affect a conclusion] Synthetic replicate rows (cell 5, `synthetic_steps`).**
   - In g2, ss8, ss39 and ss48, every step's "replicates" are one row multiplied by factors of 0.95 to 1.03. This applies to declination too: ss8 has an NRM declination of 361.7°.
   - I checked `scaled_copies` on random 4-significant-figure data: it gave 0 false positives in 2000 sets, so the detection is sound.
   - The notebook keeps these sheets in all counts. Dropping them changes no outcome: af-no-change becomes 8/9, not-random 7/18, no-fit (a) 8/8. However, ss39 is one of the two specimens the no-fit "trend out of origin" condition depends on.
   - The deposit therefore does not hold real replicate measurements for 4 of the 22 glass specimens. That should be reported alongside glass-specimen-set.
2. **[does not affect a conclusion] Combining replicates by their mean is an assumption the author chose (cells 12 and 19–21, `step_table`).**
   - The data support it: averaged replicates reproduce Table 2 almost exactly (MAD 30.10, 35.36, 24.06; R2 0.384, 0.378), while first measurements do not.
   - The fig2-changing-field and fig1 R2 results depend on this choice. With first measurements, ss41 R2 is 0.16, ss22 is 0.44 and ss43 is 0.99, all outside tolerance.
3. **[does not affect a conclusion] ss6 step 250.1 has 19 rows in two direction clusters (cell 14).**
   - The clusters sit at inclinations of about −13° and +71°. Their mean vector has no physical meaning.
   - ss6 R2 is 0.89 with averaged replicates and 0.09 with first measurements. Counting it as a miss gives 22/29 (76%), still partial.
4. **[does not affect a conclusion] Table 1's M590 is not the TRM (cell 27).**
   - M590 is the raw magnitude of the 590.1 measurement. The Methods define TRM as the field-on minus field-off vector, and Technical Validation calls this value "TRM590".
   - This is a discrepancy in the paper itself; the claims file's reading (b) covers it.
5. **[does not affect a conclusion] The stated 8e-11 emu threshold is well below the measurement noise (cell 33).**
   - All 37 of the 590.0 measurements are above it (1.2e-10 to 5.7e-10 emu) while their directions are random. The real noise floor is several times 8e-11.
   - So the Table 1 "max intensity" values understate what the data can exclude.
   - Reading (a) of no-alteration compares 590.3 minus 590.0 moment differences with 8e-11, which is below the replicate scatter. 14053g1 fails it by 4e-11.
   - This bears on the interpretation claim, not on how the arithmetic criteria are scored.
6. **[does not affect a conclusion] The fig2 readings cannot discriminate (cell 21; I checked `mad_plane` and `mad_line` on synthetic data).**
   - Random 3-point sets pass reading (b) 58% of the time.
   - A single noisy line passes (a) 38% and (b) 30% of the time.
   - The criterion is met, but it is weak evidence of a changing field.
7. **[does not affect a conclusion] The no-alteration cutoff in the claims file is very loose (cell 37). This is a claims-file wording issue, reported and not corrected.**
   - The claims file's reading (b) fails only when TRM40 exceeds 4×TRM20, although its own text says "no more than about twice".
   - Under a cutoff of TRM40/TRM20 > 2, three crystals would fail (b): 12053g1 at 2.35, 14053g3 at 2.08 and 12053g2 at 2.06. Since (a) also fails at least one crystal, no reading would pass every crystal.
   - The paper's actual claim is "≫100%", and the largest apparent efficiency here is 117%, so the substance holds.
8. **[does not affect a conclusion] Matching pTRM checks on any one of four readings is permissive (cell 13).**
   - A pTRM value counts as matched if any of four readings lands within 10%. No single reading matches more than 5 of 11.
   - The partial outcome holds under a fixed reading.
9. **[does not affect a conclusion] Helper checks.**
   - `mad_line`, `mad_plane` and `step_kind` behave correctly on synthetic inputs.
   - `watson_p` gives a false-positive rate of 6–7% at n = 2 and n = 4 (300 trials), consistent with 5%.
   - `fisher` returns NaN for k when the directions are identical. No data hit this case.
   - Units are consistent: emu converts to A m² by ×1e-3 in cell 31, and the formula uses emu throughout.

### C. What I could not check
- **Figures 1–3:** no PDF was supplied, so the nominal paleointensities and the arrow-marked step ranges could not be compared.
- **Deposit PDFs:** "SupplFig1 - other Thelliers March 2024.pdf" (27.7 MB) and "SuppFig2 - All Stereonet.pdf" are in the deposit but were not read. They would show which steps the authors fitted for ss9 and ss10 (the MAD and R2 misses) and the Fig 2 intervals.
- **Outputs that would have helped:**
  - per-step replicate tables, with the scatter of each step, for ss9, ss10 and ss6;
  - the table2-fit-statistics score with a single fixed pTRM reading and with the four synthetic sheets excluded;
  - TRM40/TRM20 printed without the factor of 2;
  - a check of whether other glass sheets have two-cluster steps like ss6 250.1;
  - an Arai-curvature measure for ss41 and ss22, to test the "curved plot" part of fig2-changing-field.

## End of run

12 turns, 3 minutes, result: success.
