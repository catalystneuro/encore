# crcns-stc-1 · author-revise-1 · run 42265008748

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-stc-1/verifier-1-report.md; ls entries/crcns-stc-1-gu-2011 entries/crcns-stc-1-gu-2011/*
```

```
Fri Nov  6 17:55:48 UTC 2026
**A. Outcomes**

The claims file has 35 claims. The notebook tests 16 of them and treats 19 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| training-group-link | reproduced | In cell 13 the eight per-monkey counts match the Figure S2B counts one to one. That gives 89 trained and 38 naive pairs and 146 and 64 units. Monkeys 2 and 5, the ones with behavioural thresholds, both fall in the trained group. The 89/38 split follows from matching by count, so only the neuron counts and the behaviour check are independent tests. |
| fig2b-trained-lower-noise-correlation | reproduced | Cell 15: trained 0.0241 ± 0.0174, naive 0.1190 ± 0.0316, both within tolerance. Student p = 0.0056 (paper 0.006), Welch p = 0.011. |
| figs2b-individual-animals | reproduced | Cell 17: the lowest naive animal mean (0.088) is above the highest mean among the trained animals shown (0.048). Counts are 35/26/18/8 and 22/11/5. There are no time courses because the data set holds no spike times. |
| fig1-example-pair | reproduced | Cell 19: one pair, m2c338r1, has all four values within tolerance (0.828, 0.786, 0.291, 0.142). The per-pair p values cannot be checked without trial counts. |
| fig1f-modality-correlated | partially_reproduced | Cell 21: Spearman R = 0.449, p = 1e-7, on n = 127, the smaller sample the criterion allows. R is outside 0.342–0.418. |
| fig1f-modality-means-equal | reproduced | Cell 23: paired p = 0.73, n = 127. The vestibular mean of 0.056 is outside the paper's 0.035 ± 0.014, but the paper's figure is from 179 pairs. |
| fig5-noise-signal-positive | reproduced | Cell 25, pooled rnoise: the rsignal slope is positive with p = 0.00017 (vestibular) and p = 0.0007 (visual). |
| fig5-slope-unchanged | reproduced | Cell 25/27: interaction p = 0.83 (vestibular) and 0.96 (visual). |
| fig5-intercept-lower-trained | partially_reproduced | Cell 29: the training main effect is significant (p = 0.018 vestibular, 0.0074 visual, pooled rnoise). The 95%
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "^[0-9]+:[0-9]+:#|verif|round|proposed" | head -80; wc -l docs/protocol.md
```

```
21:21:- The **verifier** checks the author's work and must not be the author.
33:33:file, `verifier-1`, `author-revise-1`, `verifier-2`, `author-revise-2`, and,
34:34:when the last of these proposes changes of outcome, `verifier-3` and `author-revise-3`. Each run's
174:174:A reader is asked only when the author or a verifier believes the claims file
177:177:verification"). A method detail the claims file lacks is not asked: the author
296:296:   the verifier can check it. A detail taken this way never changes the
336:336:a task variable in windows around the trial start does this; for continuous
615 docs/protocol.md
```

**Agent calls Bash**

```bash
sed -n 270,615p docs/protocol.md
```

```
- `data_missing`: something the claim needs is not in the dataset and
     not public anywhere else, or for an outside input, not public. When the
     paper deposited it in another public archive, the claim is
     `data: elsewhere` instead (step 4).
   - `metadata_insufficient`: the data are there but cannot be interpreted or
     linked, for lack of a description, label, identifier or mapping.
   - `methods_underspecified`: neither the paper nor its code fixes the
     procedure well enough to repeat it, and no choice has a defensible basis
     (step 6; see also chance levels, under "Record the attempt").
   - `data_unreadable` and `too_large`.
   - `not_runnable`: the paper's method cannot be run here, because its
     software cannot be installed in a locked environment or it cannot run
     within the time limit. Say what was tried. For an outside input that is
     public but slow to fetch, use this only when the notebook itself shows
     the fetch does not fit the limit; otherwise test the claim.
   - `other`: say what, for example too few units under the claim's own rule.

   A claim that depends on a blocked claim is blocked for the same reason.

6. Take from the paper what the claims file does not say. When a claim needs
[... 326 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep stc; ls questions | grep stc; ls transcripts/crcns-stc-1/; wc -l attempts/crcns-stc-1-gu-2011-01.yaml entries/crcns-stc-1-gu-2011/stc1.py; grep -n "verifications" -A40 attempts/*.yaml | head -80
```

```
crcns-stc-1-gu-2011-01.yaml
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
  400 attempts/crcns-stc-1-gu-2011-01.yaml
  255 entries/crcns-stc-1-gu-2011/stc1.py
  655 total
attempts/000003-senzai-2017-01.yaml:476:verifications:
attempts/000003-senzai-2017-01.yaml-477-- date: '2026-10-16'
attempts/000003-senzai-2017-01.yaml-478-  kind: agent
attempts/000003-senzai-2017-01.yaml-479-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/crcns-stc-1-gu-2011-01.yaml
```

```
schema_version: 2
id: crcns-stc-1-gu-2011-01
dataset:
  archive: crcns
  id: stc-1
  version: unversioned
  doi: 10.6080/K07P8WKF
paper: doi:10.1016/j.neuron.2011.06.015
date: 2026-11-06
entry: crcns-stc-1-gu-2011
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | grep stc; grep -n -B2 -A40 "id: fig4dh-lateral-more-sensitive" claims/crcns-stc-1*.yaml; grep -n -A40 "id: fig7c-narrow" claims/crcns-stc-1*.yaml; cat questions/crcns-stc-1.yaml | head -50
```

```
crcns-stc-1
grep: claims/crcns-stc-1*.yaml: No such file or directory
grep: claims/crcns-stc-1*.yaml: No such file or directory
cat: questions/crcns-stc-1.yaml: No such file or directory
```

**Agent calls Bash**

```bash
ls claims/crcns-stc-1 questions/ | head; F=$(ls claims/crcns-stc-1/*.yaml | head -1); grep -n -A40 "id: fig4dh-lateral-more-sensitive" claims/crcns-stc-1/*.yaml; grep -n -A40 "id: fig7c-narrow" claims/crcns-stc-1/*.yaml
```

```
claims/crcns-stc-1:
10.1016-j.neuron.2011.06.015.yaml

questions/:
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
466:- id: fig4dh-lateral-more-sensitive
467-  statement: Neurons preferring lateral headings are more sensitive to heading variation around
468-    straight ahead than neurons preferring fore-aft headings (p << 0.001, factorial ANOVA).
469-  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single
470-    Neurons, paragraph 3; Figures 4C, 4D, 4G and 4H
471-  quote: lateral neurons were significantly more sensitive than fore-aft neurons for heading
472-    discrimination around straight ahead (p << 0.001, Factorial ANOVA, Figures 4D and 4H)
473-  statistics:
474-  - test: factorial ANOVA, main effect of preference group
475-    p: 0.001
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; cat stc1.py; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=====',i,c['cell_type'],c['metadata'].get('tags'));print(''.join(c['source'])[:600])
"
```

```
<persisted-output>
Output too large (43.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26b8781e-adde-45c1-bfad-033eba27e882/tool-results/bddcsxbrm.txt

Preview (first 2KB):
"""Loading and measures for CRCNS stc-1, MSTd pairs, for Gu et al. (2011), Neuron 71:750-761.

Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), "Perceptual Learning Reduces
Interneuronal Correlations in Macaque Visual Cortex", doi:10.1016/j.neuron.2011.06.015.

The data set (doi:10.6080/K07P8WKF) is not versioned on CRCNS; it is read as `unversioned` from
the public bucket `crcnsarchive` under stc-1/live/, and each file is checked against the MD5 sum
in the data set's checksums.md5, so that a later change is detected. Files are streamed into
memory; nothing is written to disk.

MSTd.mat holds three structures (data descriptor, version 0.6). `experiment3.pairs` holds, per
pair and per condition (`ves`, `vis`), the signal correlation, the noise correlation and the
preferred headings of the two units, with the `file_id` of the recording (for example
`m17c26r1`, monkey 17). `experiment1.units` holds trial-averaged heading tuning curves and
`experiment2.units` the choice probability and neuronal threshold of 129 single units from
monkeys 2 and 5 (Gu et al. 2008).
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26b8781e-adde-45c1-bfad-033eba27e882/tool-results/bddcsxbrm.txt"
}
```

```
1	"""Loading and measures for CRCNS stc-1, MSTd pairs, for Gu et al. (2011), Neuron 71:750-761.
2	
3	Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), "Perceptual Learning Reduces
4	Interneuronal Correlations in Macaque Visual Cortex", doi:10.1016/j.neuron.2011.06.015.
5	
6	The data set (doi:10.6080/K07P8WKF) is not versioned on CRCNS; it is read as `unversioned` from
7	the public bucket `crcnsarchive` under stc-1/live/, and each file is checked against the MD5 sum
8	in the data set's checksums.md5, so that a later change is detected. Files are streamed into
9	memory; nothing is written to disk.
10	
11	MSTd.mat holds three structures (data descriptor, version 0.6). `experiment3.pairs` holds, per
12	pair and per condition (`ves`, `vis`), the signal correlation, the noise correlation and the
13	preferred headings of the two units, with the `file_id` of the recording (for example
14	`m17c26r1`, monkey 17). `experiment1.units` holds trial-averaged heading tuning curves and
15	`experiment2.units` the choice probability and neuronal threshold of 129 single units from
16	monkeys 2 and 5 (Gu et al. 2008).
17	
18	Where the parameters come from:
19	
20	- Training groups. The data set does not say which monkey is naive or trained. The paper gives
[... 794 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; sed -n 755,830p claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml; python - <<'E'
import json;nb=json.load(open('entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for i in (0,55,56,57,58,61,62,63):
    if i<len(nb['cells']): print('=====',i);print(''.join(nb['cells'][i]['source']))
print(len(nb['cells']))
E
```

```
- id: fig8ab-choice-probability-lateral
  statement: Neurons preferring fore-aft headings have smaller choice probabilities than
    neurons preferring lateral headings (p = 0.019, t test), and choice probability does not
    differ between neurons preferring leftward and rightward headings (p = 0.11).
  source: Results, Possible rsignal Distributions in Area MSTd, paragraphs 2 and 3; Figures 8A
    and 8B
  quote: neurons with a preference for fore-aft movement show significantly smaller choice
    probabilities (p = 0.019, t test, Figures 8A and 8B) ... there was no significant difference
    in average choice probability between neurons preferring leftward and rightward headings
    (p = 0.11, t test)
  statistics:
  - about: fore-aft against lateral
    test: t test
    p: 0.019
    n: 311 single-electrode recordings, vestibular and visual pooled
  - about: leftward against rightward
    test: t test
    p: 0.11
  criterion: Choice probabilities from the single-electrode database (n = 311, vestibular and
    visual pooled), groups by preferred heading as in Figure 4 (fore-aft within 45 degrees of 0
[... 246 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper/; grep -n -i -E "five pairs|up to (five|5)|neuronal threshold|Fisher information|equation \(?[234]|interpolat|vector sum" paper/*.md paper/*.txt 2>/dev/null | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 300,320p paper/10.1016-j.neuron.2011.06.015.txt; echo ----; sed -n 900,1000p paper/10.1016-j.neuron.2011.06.015.txt; grep -n -i -E "pairs? (per|in) (an|each|one) |maximum|simultaneously recorded" paper/10.1016-j.neuron.2011.06.015.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && time python -c "
import stc1, numpy as np
mat=stc1.load_mat()
u1=mat['experiment1'].units[0]; u2=mat['experiment2'].units[0]
print(u1._fieldnames, u1.ves._fieldnames); print(u2._fieldnames, u2.ves._fieldnames)
print(u1.ves.stim_global, u1.ves.resp_global); print({k:getattr(u2.ves,k) for k in u2.ves._fieldnames})
b=mat['experiment2'].behv; print(b[0]._fieldnames if hasattr(b,'__len__') else b._fieldnames)
for s in np.atleast_1d(b): print({k:getattr(s,k) for k in s._fieldnames})
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import stc1, numpy as np
  File "entries/crcns-stc-1-gu-2011/stc1.py", line 55, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'

real	0m0.024s
user	0m0.021s
sys	0m0.003s
```

**Agent calls Bash**

```bash
ls -d .venv* envs* executed/crcns-stc-1-gu-2011 2>/dev/null; ls ~/.cache 2>/dev/null | head; grep -n "venv\|def run\|def cmd_all\|uv " tools/entry.py | head -30
```

```
342:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
345:    venv = (output_dir / ".venv").resolve()
346:    python = venv / "bin" / "python"
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
353:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
367:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && grep -n PYTHON_VERSION ../../tools/entry.py | head -2; uv venv -q --python 3.12 $TMPDIR/dv && uv pip install -q --python $TMPDIR/dv/bin/python -r requirements.lock.txt 2>&1 | tail -3; $TMPDIR/dv/bin/python -c "
import stc1, numpy as np
mat=stc1.load_mat()
u1=mat['experiment1'].units[0]; u2=mat['experiment2'].units[0]
print(u1._fieldnames, u1.ves._fieldnames); print(u2._fieldnames, u2.ves._fieldnames)
print(u1.ves.stim_global, u1.ves.resp_global); print({k:getattr(u2.ves,k) for k in u2.ves._fieldnames})
b=mat['experiment2'].behv
for s in np.atleast_1d(b): print({k:getattr(s,k) for k in s._fieldnames})
"
```

```
59:PYTHON_VERSION = "3.13"
335:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
['file_id', 'ves', 'vis'] ['stim_global', 'resp_global']
['file_id', 'ves', 'vis', 'com'] ['stim_local', 'resp_local', 'cp', 'thresh']
[ 135.    90.    45.    22.5    0.   -22.5  -45.   -90.  -135.  -180. ] [18.15920398 16.41791045 14.05472637 14.55223881 12.93532338 13.93034826
 19.90049751 27.46268657 31.46766169 25.37313433]
{'stim_local': array([ 9.  ,  3.46,  1.33,  0.51,  0.  , -0.51, -1.33, -3.46, -9.  ]), 'resp_local': array([14.28217822, 14.48019802, 16.70792079, 15.99009901, 16.75742574,
       18.0874185 , 17.84593093, 19.75247525, 21.00941801]), 'cp': 0.581, 'thresh': 9.07}
{'subj': array([<scipy.io.matlab._mio5_params.mat_struct object at 0x736244f9a8d0>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x736244f9aa80>],
      dtype=object)}
```

**Agent calls Bash**

```bash
cd ../..; grep -n -A30 "id: fig2a-behavioral-learning" claims/crcns-stc-1/*.yaml | head -40; python - <<'E'
import json;nb=json.load(open('entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for i in (10,13,37,40,43,50):
    print('=====',i);print(''.join(nb['cells'][i]['source']))
E
```

```
325:- id: fig2a-behavioral-learning
326-  statement: Heading discrimination thresholds of the five trained monkeys were high (over 10
327-    degrees) early in training and decreased gradually to a plateau of 1 to 3 degrees.
328-  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 1;
329-    Figure 2A
330-  quote: These monkeys' heading discrimination thresholds (corresponding to 84% correct) were
331-    high ... at early stages of training, and gradually decreased to a plateau of only a few
332-    degrees
333-  expected:
334-    quantity: plateau vestibular threshold
335-    value: 2.1
336-    tolerance: 1.2
337-    unit: degrees
338-  criterion: The range 1 to 3 degrees widened by 10% of each bound gives 0.9 to 3.3 degrees.
339-    Reproduced when each animal's threshold falls from above 10 degrees early in training to a
340-    plateau inside 0.9 to 3.3 degrees, the plateau read as the asymptote of an exponential fit
341-    to threshold against session, as in the legend. Needs the training histories, which the
342-    paper takes from earlier studies.
343-- id: fig3-mean-response-unchanged
344-  statement: The time course of the population average response to the preferred heading does
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && cat > $TMPDIR/proto.py <<'E'
import numpy as np, pandas as pd, stc1
from scipy import stats
from scipy.interpolate import CubicSpline
import statsmodels.formula.api as smf, statsmodels.api as sm
def wvs(headings, resp):
    h = np.asarray(headings, float) % 360.0
    o = np.argsort(h); h = h[o]; r = np.asarray(resp, float)[o]
    gap = np.diff(np.append(h, h[0] + 360.0))
    w = (gap + np.roll(gap, 1)) / 2
    hr = np.deg2rad(h)
    return float(np.rad2deg(np.arctan2((w*r*np.sin(hr)).sum(), (w*r*np.cos(hr)).sum())))
# synthetic check
H = np.array([135,90,45,22.5,0,-22.5,-45,-90,-135,-180.])
for p in (30,60,90,120,-150):
    r = stc1.tuning([p], H)[0]
    print(p, round(wvs(H,r),1), round(stc1.pref_vector_sum(H,r),1))
def fth(headings, resp, interp):
    h = np.asarray(headings, float) % 360.0
    o = np.argsort(h); h = h[o]; r = np.asarray(resp, float)[o]
    if interp == "spline":
        cs = CubicSpline(np.append(h, h[0]+360), np.append(r, r[0]), bc_type="periodic")
        f, fp = float(cs(0.0)), float(cs(0.0, 1))
    else:
        i = np.where(h == 0)[0][0]
        f = r[i]; fp = (r[i+1] - r[i-1]) / ((h[i+1]) - (h[i-1]-360))
    fp = np.rad2deg(fp)  # per radian? keep per degree
    return f, fp
mat = stc1.load_mat()
rows=[]
for u1,u2 in zip(mat["experiment1"].units, mat["experiment2"].units):
    for c in ("ves","vis"):
        x=getattr(u1,c); print if 0 else None
        rows.append(dict(cell=u1.file_id, cond=c, vs=wvs(x.stim_global,x.resp_global), sp=stc1.pref_spline_peak(x.stim_global,x.resp_global), thr2=float(getattr(u2,c).thresh), cp=float(getattr(u2,c).cp)))
d=pd.DataFrame(rows)
print((stc1.preference_group(d.vs)==stc1.preference_group(d.sp)).mean())
for rd in ("vs","sp"):
    g=stc1.preference_group(d[rd]); print(rd, pd.Series(g).value_counts().to_dict(), stats.ttest_ind(d.cp[g=="fore-aft"], d.cp[g=="lateral"]), d.cp[g=="fore-aft"].mean(), d.cp[g=="lateral"].mean())
print((d.cp>0.5).mean())
E
$TMPDIR/dv/bin/python $TMPDIR/proto.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 1, in <module>
    import numpy as np, pandas as pd, stc1
ModuleNotFoundError: No module named 'stc1'
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/proto.py
```

```
30 27.7 16.0
60 57.5 34.7
90 88.9 59.4
120 120.0 92.6
-150 -150.2 -134.0
0.7170542635658915
vs {'lateral': 157, 'fore-aft': 101} TtestResult(statistic=np.float64(-0.25943109167061423), pvalue=np.float64(0.7955111455709477), df=np.float64(256.0)) 0.5326465346534655 0.5353121019108281
sp {'fore-aft': 130, 'lateral': 128} TtestResult(statistic=np.float64(-1.4943351009798216), pvalue=np.float64(0.13631961950312077), df=np.float64(256.0)) 0.5268638461538462 0.5417890624999999
0.7170542635658915
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && cat >> $TMPDIR/proto.py <<'E'
def thr(headings, resp, interp):
    h = np.asarray(headings, float) % 360.0
    o = np.argsort(h); h = h[o]; r = np.asarray(resp, float)[o]
    if interp == "spline":
        cs = CubicSpline(np.append(h, h[0]+360), np.append(r, r[0]), bc_type="periodic")
        f, fp = float(cs(0.0)), float(cs(0.0, 1))
    else:
        f = r[0]; fp = (r[1] - r[-1]) / (h[1] - (h[-1] - 360))
    info = fp**2 / f + 0.5 * (fp / f)**2
    return np.sqrt(2) / np.sqrt(info)
for interp in ("spline","linear"):
    d[interp]=[thr(getattr(u1,c).stim_global,getattr(u1,c).resp_global,interp) for u1 in mat["experiment1"].units for c in ("ves","vis")]
print(d[["spline","linear","thr2"]].describe())
print(stats.spearmanr(d.spline,d.thr2), stats.spearmanr(d.linear,d.thr2))
for rd in ("vs","sp"):
  d["grp"]=stc1.preference_group(d[rd])
  for interp in ("spline","linear","thr2"):
    for tr in ("raw","log"):
      y = d[interp] if tr=="raw" else np.log10(d[interp])
      dd=d.assign(y=y)
      out=[]
      for c in ("ves","vis"):
        s=dd[dd.cond==c]; m=smf.ols("y~C(grp)",s).fit(); out.append(f"{c} p={sm.stats.anova_lm(m,typ=2).loc['C(grp)','PR(>F)']:.2g} med fa {s.y[s.grp=='fore-aft'].median():.3g} lat {s.y[s.grp=='lateral'].median():.3g}")
      m=smf.ols("y~C(grp)*C(cond)",dd).fit(); out.append(f"both p={sm.stats.anova_lm(m,typ=2).loc['C(grp)','PR(>F)']:.2g}")
      print(rd,interp,tr,"; ".join(out))
E
PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/proto.py 2>&1 | tail -40
```

```
/bin/bash: line 1: cd: entries/crcns-stc-1-gu-2011: No such file or directory
30 27.7 16.0
60 57.5 34.7
90 88.9 59.4
120 120.0 92.6
-150 -150.2 -134.0
0.7170542635658915
vs {'lateral': 157, 'fore-aft': 101} TtestResult(statistic=np.float64(-0.25943109167061423), pvalue=np.float64(0.7955111455709477), df=np.float64(256.0)) 0.5326465346534655 0.5353121019108281
sp {'fore-aft': 130, 'lateral': 128} TtestResult(statistic=np.float64(-1.4943351009798216), pvalue=np.float64(0.13631961950312077), df=np.float64(256.0)) 0.5268638461538462 0.5417890624999999
0.7170542635658915
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/proto.py <<'E'
def thr(headings, resp, interp):
    h = np.asarray(headings, float) % 360.0
    o = np.argsort(h); h = h[o]; r = np.asarray(resp, float)[o]
    if interp == "spline":
        cs = CubicSpline(np.append(h, h[0]+360), np.append(r, r[0]), bc_type="periodic")
        f, fp = float(cs(0.0)), float(cs(0.0, 1))
    else:
        f = r[0]; fp = (r[1] - r[-1]) / (h[1] - (h[-1] - 360))
    info = fp**2 / f + 0.5 * (fp / f)**2
    return np.sqrt(2) / np.sqrt(info)
for interp in ("spline","linear"):
    d[interp]=[thr(getattr(u1,c).stim_global,getattr(u1,c).resp_global,interp) for u1 in mat["experiment1"].units for c in ("ves","vis")]
print(d[["spline","linear","thr2"]].describe())
print(stats.spearmanr(d.spline,d.thr2), stats.spearmanr(d.linear,d.thr2))
for rd in ("vs","sp"):
  d["grp"]=stc1.preference_group(d[rd])
  for interp in ("spline","linear","thr2"):
    for tr in ("raw","log"):
      y = d[interp] if tr=="raw" else np.log10(d[interp])
      dd=d.assign(y=y)
      out=[]
      for c in ("ves","vis"):
        s=dd[dd.cond==c]; m=smf.ols("y~C(grp)",s).fit(); out.append(f"{c} p={sm.stats.anova_lm(m,typ=2).loc['C(grp)','PR(>F)']:.2g} med fa {s.y[s.grp=='fore-aft'].median():.3g} lat {s.y[s.grp=='lateral'].median():.3g}")
      m=smf.ols("y~C(grp)*C(cond)",dd).fit(); out.append(f"both p={sm.stats.anova_lm(m,typ=2).loc['C(grp)','PR(>F)']:.2g}")
      print(rd,interp,tr,"; ".join(out))
E
PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/proto.py 2>&1 | tail -32
```

```
0.7170542635658915
            spline      linear        thr2
count   258.000000  258.000000  258.000000
mean     82.527612         inf   40.220100
std     205.469048         NaN   63.808847
min       2.654027    3.079860    1.513000
25%      16.885541   20.998286    7.503750
50%      31.102312   41.876524   17.841500
75%      70.103102   87.862113   39.827750
max    2759.963253         inf  300.000000
SignificanceResult(statistic=np.float64(0.3039860244947645), pvalue=np.float64(6.447229889182984e-07)) SignificanceResult(statistic=np.float64(0.3691393176616733), pvalue=np.float64(9.48199681345546e-10))
vs spline raw ves p=0.86 med fa 56.3 lat 32; vis p=0.006 med fa 38.7 lat 13.9; both p=0.35
vs spline log ves p=0.04 med fa 1.75 lat 1.5; vis p=3.4e-07 med fa 1.59 lat 1.14; both p=1.9e-07
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 61, in <module>
    s=dd[dd.cond==c]; m=smf.ols("y~C(grp)",s).fit(); out.append(f"{c} p={sm.stats.anova_lm(m,typ=2).loc['C(grp)','PR(>F)']:.2g} med fa {s.y[s.grp=='fore-aft'].median():.3g} lat {s.y[s.grp=='lateral'].median():.3g}")
                                                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dv/lib/python3.12/site-packages/statsmodels/stats/anova.py", line 444, in anova_lm
    return anova_single(model, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/^for rd in ("vs","sp"):/d = d.replace(np.inf, np.nan); print("inf", d.isna().sum().to_dict())\nfor rd in ("vs","sp"):/' $TMPDIR/proto.py && sed -i 's/      dd=d.assign(y=y)/      dd=d.assign(y=y).dropna(subset=["y"])/' $TMPDIR/proto.py && PYTHONPATH=. $TMPDIR/dv/bin/python $TMPDIR/proto.py 2>&1 | tail -14; date -u
```

```
SignificanceResult(statistic=np.float64(0.3039860244947645), pvalue=np.float64(6.447229889182984e-07)) SignificanceResult(statistic=np.float64(0.3691393176616733), pvalue=np.float64(9.48199681345546e-10))
inf {'cell': 0, 'cond': 0, 'vs': 0, 'sp': 0, 'thr2': 0, 'cp': 0, 'spline': 0, 'linear': 2}
vs spline raw ves p=0.86 med fa 56.3 lat 32; vis p=0.006 med fa 38.7 lat 13.9; both p=0.35
vs spline log ves p=0.04 med fa 1.75 lat 1.5; vis p=3.4e-07 med fa 1.59 lat 1.14; both p=1.9e-07
vs linear raw ves p=0.48 med fa 78.2 lat 40.3; vis p=0.26 med fa 65.6 lat 15.4; both p=0.51
vs linear log ves p=0.64 med fa 1.89 lat 1.61; vis p=0.0033 med fa 1.82 lat 1.19; both p=0.013
vs thr2 raw ves p=0.00026 med fa 39.8 lat 16.1; vis p=0.48 med fa 24.1 lat 9.98; both p=0.004
vs thr2 log ves p=7.6e-05 med fa 1.6 lat 1.21; vis p=0.0019 med fa 1.38 lat 0.999; both p=7.3e-07
sp spline raw ves p=0.5 med fa 37.3 lat 35; vis p=0.65 med fa 28.6 lat 17; both p=0.66
sp spline log ves p=0.84 med fa 1.57 lat 1.54; vis p=0.085 med fa 1.46 lat 1.23; both p=0.26
sp linear raw ves p=0.43 med fa 58.4 lat 42.3; vis p=0.43 med fa 43.6 lat 17.7; both p=0.77
sp linear log ves p=0.63 med fa 1.77 lat 1.63; vis p=0.094 med fa 1.64 lat 1.25; both p=0.38
sp thr2 raw ves p=0.00015 med fa 35.8 lat 14.9; vis p=0.94 med fa 15.6 lat 12.6; both p=0.015
sp thr2 log ves p=2.3e-05 med fa 1.55 lat 1.17; vis p=0.58 med fa 1.19 lat 1.1; both p=0.0011
Fri Nov  6 17:58:05 UTC 2026
```

**Agent calls Bash**

```bash
cd ../.. && cat > $TMPDIR/edit1.py <<'E'
p='entries/crcns-stc-1-gu-2011/stc1.py'
s=open(p).read()
old_doc='''- Preferred heading from a tuning curve (fig8ab): the vector sum, or the peak of a periodic
  cubic spline through the curve at 1 degree; the two readings of the claims file
  (fig4dh-lateral-more-sensitive).'''
new_doc='''- Preferred heading from a tuning curve (fig4dh, fig8ab): the vector sum, or the peak of a
  periodic cubic spline through the curve at 1 degree; the two readings of the claims file
  (fig4dh-lateral-more-sensitive). The experiment 1 headings are unevenly spaced (+-22.5 degrees
  added to the eight 45 degrees apart), so each response in the vector sum is weighted by the
  angle it covers (half the gaps to its two neighbours); an unweighted sum is pulled toward
  straight ahead (a choice made here, after the round-1 verification found that bias).
- Single-neuron threshold (fig4dh): equations 2 and 3 for one neuron, with variance equal to the
  mean (equation 4 for i = j), so that I = f'^2 / f + 0.5 (f' / f)^2, on the tuning curve in
  spikes/s read as the count of the middle 1 s (Experimental Procedures, Noise and Signal
  Correlations). The two interpolations are the claims file's readings. For the linear one, f'
  at 0, a sampled heading, is the slope between the two neighbouring headings (-22.5 and 22.5),
  a choice made here since a piecewise-linear curve has no derivative at a knot.'''
assert old_doc in s; s=s.replace(old_doc,new_doc)
old_vs='''def pref_vector_sum(headings, resp) -> float:
    h = np.deg2rad(np.asarray(headings, float))
    r = np.asarray(resp, float)
    return float(np.rad2deg(np.arctan2((r * np.sin(h)).sum(), (r * np.cos(h)).sum())))
'''
new_vs='''def _sorted_circle(headings, resp):
    h = np.asarray(headings, float) % 360.0
    order = np.argsort(h)
    h, r = h[order], np.asarray(resp, float)[order]
    h, idx = np.unique(h, return_index=True)
    return h, r[idx]


def pref_vector_sum(headings, resp) -> float:
    """Vector sum, each response weighted by half the gaps to its two neighbouring headings."""
    h, r = _sorted_circle(headings, resp)
    gap = np.diff(np.append(h, h[0] + 360.0))
    w = r * (gap + np.roll(gap, 1)) / 2
    hr = np.deg2rad(h)
    return float(np.rad2deg(np.arctan2((w * np.sin(hr)).sum(), (w * np.cos(hr)).sum())))
'''
assert old_vs in s; s=s.replace(old_vs,new_vs)
old_sp='''    h = np.asarray(headings, float) % 360.0
    order = np.argsort(h)
    h, r = h[order], np.asarray(resp, float)[order]
    h, idx = np.unique(h, return_index=True)
    r = r[idx]
    cs = CubicSpline'''
new_sp='''    h, r = _sorted_circle(headings, resp)
    cs = CubicSpline'''
assert old_sp in s; s=s.replace(old_sp,new_sp)
old_tls='''def tls_plane('''
new_tls='''def neuron_threshold(headings, resp, interp: str = "spline") -> float:
    """Threshold (degrees) of one neuron at straight ahead, equations 2 and 3 with variance = mean.

    interp "spline" (periodic cubic spline) or "linear" (slope between the neighbours of 0).
    Infinite when the curve is flat at 0.
    """
    h, r = _sorted_circle(headings, resp)
    if interp == "spline":
        cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type="periodic")
        f, fp = float(cs(0.0)), float(cs(0.0, 1))
    else:
        f, fp = r[0], (r[1] - r[-1]) / (h[1] - h[-1] + 360.0)
    info = fp**2 / f + 0.5 * (fp / f) ** 2
    return float(np.sqrt(2.0) / np.sqrt(info)) if info > 0 else np.inf


def tls_plane('''
assert old_tls in s; s=s.replace(old_tls,new_tls)
open(p,'w').write(s)
E
python $TMPDIR/edit1.py && grep -n "h\[0\] == 0\|r\[0\]" entries/crcns-stc-1-gu-2011/stc1.py
```

```
188:    cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type="periodic")
201:        cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type="periodic")
204:        f, fp = r[0], (r[1] - r[-1]) / (h[1] - h[-1] + 360.0)
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && python - <<'E'
p='stc1.py'; s=open(p).read()
s=s.replace('''    else:
        f, fp = r[0], (r[1] - r[-1])''','''    else:
        if h[0] != 0.0:
            raise ValueError("the linear reading needs a response at 0 degrees")
        f, fp = r[0], (r[1] - r[-1])''')
open(p,'w').write(s)
E
date -u
```

```
Fri Nov  6 17:58:43 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbedit.py <<'E'
import json
p='reproduce_gu_2011.ipynb'
nb=json.load(open(p)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,t): C[i]['source']=t.splitlines(keepends=True)
def find(prefix):
    m=[i for i,c in enumerate(C) if ''.join(c['source']).startswith(prefix)]
    assert len(m)==1,(prefix,m); return m[0]
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
def md(t): return {"cell_type":"markdown","metadata":{},"source":t.splitlines(keepends=True)}
def code(t,tag): return {"cell_type":"code","metadata":{"tags":[tag]},"source":t.splitlines(keepends=True),"outputs":[],"execution_count":None}

# cell 0
i=0
rep(i,"**Random numbers.** None of the analyses below draws random numbers.",
 "**Random numbers.** Only the bootstrap intervals of fig5-intercept-lower-trained and\nfig5-regression-coefficients draw random numbers, each from its own generator with a fixed seed.")
rep(i,"""of 129 single units of two trained monkeys from Gu et al. (2008); they are used for
fig8ab-choice-probability-lateral as a subset of the paper's database.""","""of 129 single units of two trained monkeys from Gu et al. (2008); they are used for
fig4dh-lateral-more-sensitive and fig8ab-choice-probability-lateral as a subset of the paper's
database.""")
rep(i,"| fig8ab-choice-probability-lateral | tested on 129 units of two monkeys |",
 "| fig4dh-lateral-more-sensitive | tested on 129 units of two trained monkeys, without the training factor |\n| fig8ab-choice-probability-lateral | tested on 129 units of two monkeys |")
rep(i,"| fig4-tuning-width-visual, fig4-tuning-width-vestibular, fig4-amplitude-unchanged, fig4dh-lateral-more-sensitive, fig4dh-training-no-sensitivity-change, figs4-population-sensitivity-any-reference | blocked: no naive animals in the single-unit data |",
 "| fig4-tuning-width-visual, fig4-tuning-width-vestibular, fig4-amplitude-unchanged, fig4dh-training-no-sensitivity-change, figs4-population-sensitivity-any-reference | blocked: no naive animals in the single-unit data |")

# cell 11, fig2a values
i=find("The data set gives no training group.")
rep(i,"the data set's own behavioural thresholds show performed the heading discrimination task.",
 """the data set's own behavioural thresholds show performed the heading discrimination task.
These thresholds, one per monkey and condition, are the only behavioural values in the data set.
For fig2a-behavioral-learning, which is blocked for want of the training histories, they are the
only part of the claim that can be compared: both vestibular values (monkey 2 1.2 degrees,
monkey 5 3.1 degrees, printed above) lie inside the criterion's plateau range of 0.9 to 3.3
degrees, as do the visual ones (1.2 and 3.25 degrees). Whether they are plateau values, and the
fall from above 10 degrees, cannot be checked.""")

# fig5 intercept bootstrap
i=find("for (c, m), d in lines.groupby")
s=src(i)+'''
print("\\nVariant, bootstrap 95% intervals of each group's intercept from its own fit (pooled rnoise,"
      " 2000 resamples of pairs within the group):")
rng_int = np.random.default_rng(2011)
for c in ("ves", "vis"):
    ci = {}
    for g, d in pairs.groupby("group"):
        X = np.column_stack([np.ones(len(d)), d[f"rsig_{c}"].values])
        y = d.rnoise_pooled.values
        b = [np.linalg.lstsq(X[k], y[k], rcond=None)[0][0]
             for k in (rng_int.integers(0, len(d), len(d)) for _ in range(2000))]
        ci[g] = np.percentile(b, [2.5, 97.5])
    print(f"  {c}: naive [{ci['naive'][0]:.4f}, {ci['naive'][1]:.4f}], trained [{ci['trained'][0]:.4f}, "
          f"{ci['trained'][1]:.4f}], overlap {ci['trained'][1] >= ci['naive'][0]}")
'''
setsrc(i,s)

# fig6a: rsignal readings difference
i=find("print(f\"Wrapped-Gaussian sigma")
setsrc(i,src(i)+'''
p_check = stc1.uniform_prefs(256)
d_rs = np.abs(stc1.signal_corr(p_check, stc1.RSIGNAL_HEADINGS_8) - stc1.signal_corr(p_check, stc1.RSIGNAL_HEADINGS_CONT)).max()
print(f"Largest difference in rsignal between the two readings (256 neurons): {d_rs:.1e}")
''')

# fig7a crossover
i=find("rows = []\nfor name, H in rsig_readings.items():\n    for p2 in")
setsrc(i,src(i)+'''
print("\\nWhere trained/naive crosses 1 (linear interpolation between neighbouring pairs):")
for name, d in fig7a.groupby("rsignal_grid"):
    d = d.sort_values("rsignal")
    x, y = d.rsignal.values, (d.trained / d.naive).values - 1
    k = np.where(np.sign(y[:-1]) != np.sign(y[1:]))[0]
    for j in k:
        cross = x[j] - y[j] * (x[j + 1] - x[j]) / (y[j + 1] - y[j])
        print(f"  {name}: rsignal = {cross:.4f} (between pref2 {d.pref2.values[j]:g} and {d.pref2.values[j + 1]:g} degrees)")
''')

# fig4dh new section before fig8ab
i=find("## fig8ab-choice-probability-lateral")
new=[md('''## fig4dh-lateral-more-sensitive

> Neurons preferring lateral headings are more sensitive to heading variation around straight
> ahead than neurons preferring fore-aft headings (p << 0.001, factorial ANOVA).

The paper's single-electrode database (992 visual and 556 vestibular neurons, naive and trained)
is not in the data set. The experiment 1 tuning curves of 129 units of two trained monkeys are,
so the preference-group effect can be tested within trained animals only, without the training
factor of the paper's ANOVA. Per unit and condition, the threshold at straight ahead from
equations 2 and 3 for one neuron with variance equal to the mean, on the tuning curve
interpolated by a periodic cubic spline or linearly (the claims file's readings); preferred
heading by the vector sum or the spline peak (the claims file's readings; the vector sum weights
each response by the angle it covers, as the headings are unevenly spaced, see `stc1.py`).
ANOVA on threshold, raw and log10, per condition (preference group alone) and with condition as
a second factor (preference group, condition and their interaction, Type II). A unit whose
curve is flat at 0 has an infinite threshold and is left out; the count is printed. As a
variant, not a reading of the claims file, the neuronal thresholds that experiment 2 holds for
the same cells (neurometric thresholds of Gu et al. 2008, from responses to headings near
straight ahead). First, a check of the two preference readings on synthetic tuning curves
sampled at the experiment 1 headings.'''),
code('''H1 = mat["experiment1"].units[0].ves.stim_global
print("Synthetic wrapped-Gaussian curves (fig6a tuning) at the experiment 1 headings:")
print("  true preference -> weighted vector sum, spline peak, unweighted vector sum")
for p_true in (0, 30, 60, 90, 120, 150, -45, -100):
    r = stc1.tuning([p_true], H1)[0]
    h = np.deg2rad(H1)
    unweighted = np.rad2deg(np.arctan2((r * np.sin(h)).sum(), (r * np.cos(h)).sum()))
    print(f"  {p_true:5d} -> {stc1.pref_vector_sum(H1, r):7.1f} {stc1.pref_spline_peak(H1, r):7.1f} {unweighted:7.1f}")
''','claim:fig4dh-lateral-more-sensitive'),
code('''rows = []
for u1, u2 in zip(mat["experiment1"].units, mat["experiment2"].units):
    for cond in ("ves", "vis"):
        c1 = getattr(u1, cond)
        rows.append({"cell": u1.file_id, "monkey": stc1.monkey_of(u1.file_id), "condition": cond,
                     "pref_vector_sum": stc1.pref_vector_sum(c1.stim_global, c1.resp_global),
                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global),
                     "thr_spline": stc1.neuron_threshold(c1.stim_global, c1.resp_global, "spline"),
                     "thr_linear": stc1.neuron_threshold(c1.stim_global, c1.resp_global, "linear"),
                     "variant_thr_experiment2": float(getattr(u2, cond).thresh)})
sens = pd.DataFrame(rows).replace(np.inf, np.nan)
thr_cols = ["thr_spline", "thr_linear", "variant_thr_experiment2"]
print("Values:", len(sens), "; infinite thresholds left out:", sens[thr_cols].isna().sum().to_dict())
print("Threshold ranges (degrees):")
print(sens[thr_cols].describe().loc[["count", "min", "50%", "max"]].round(2).to_string())
print("Spearman rho of the Fisher thresholds with the experiment 2 thresholds:",
      {c: round(stats.spearmanr(sens[c], sens.variant_thr_experiment2, nan_policy="omit")[0], 3) for c in thr_cols[:2]})
res = []
for pref in ("pref_vector_sum", "pref_spline_peak"):
    sens["pgroup"] = stc1.preference_group(sens[pref])
    for thr in thr_cols:
        for scale in ("raw", "log10"):
            d = sens.dropna(subset=[thr]).copy()
            d["y"] = d[thr] if scale == "raw" else np.log10(d[thr])
            row = {"preference": pref, "threshold": thr, "scale": scale}
            for cond in ("ves", "vis"):
                dc = d[d.condition == cond]
                a = sm.stats.anova_lm(smf.ols("y ~ C(pgroup)", dc).fit(), typ=2)
                row[f"{cond}_n_fa/lat"] = f"{(dc.pgroup == 'fore-aft').sum()}/{(dc.pgroup == 'lateral').sum()}"
                row[f"{cond}_median_fa"] = dc[thr][dc.pgroup == "fore-aft"].median()
                row[f"{cond}_median_lat"] = dc[thr][dc.pgroup == "lateral"].median()
                row[f"{cond}_p"] = a.loc["C(pgroup)", "PR(>F)"]
            a2 = sm.stats.anova_lm(smf.ols("y ~ C(pgroup) * C(condition)", d).fit(), typ=2)
            row["two_factor_p_group"] = a2.loc["C(pgroup)", "PR(>F)"]
            row["two_factor_p_interaction"] = a2.loc["C(pgroup):C(condition)", "PR(>F)"]
            row["lateral_lower_both"] = bool((row["ves_median_lat"] < row["ves_median_fa"]) and (row["vis_median_lat"] < row["vis_median_fa"]))
            res.append(row)
fig4dh = pd.DataFrame(res)
print(fig4dh.round(5).to_string(index=False))
crit = fig4dh[fig4dh.threshold != "variant_thr_experiment2"]
passes = crit[((crit.two_factor_p_group < 0.001) | ((crit.ves_p < 0.001) & (crit.vis_p < 0.001))) & crit.lateral_lower_both]
print("\\nReadings of the claims file with lateral lower at p < 0.001:", len(passes), "of", len(crit))
print(passes[["preference", "threshold", "scale", "ves_p", "vis_p", "two_factor_p_group"]].to_string(index=False))
print("\\nPer monkey (vector-sum preference, spline threshold, log10): median threshold fore-aft, lateral, p")
sens["pgroup"] = stc1.preference_group(sens.pref_vector_sum)
for (m, c), d in sens.groupby(["monkey", "condition"]):
    fa, la = np.log10(d.thr_spline[d.pgroup == "fore-aft"]), np.log10(d.thr_spline[d.pgroup == "lateral"])
    print(f"  monkey {m}, {c}: {10 ** fa.median():.1f} (n {len(fa)}), {10 ** la.median():.1f} (n {len(la)}), p = {stats.ttest_ind(fa, la).pvalue:.3g}")
''','claim:fig4dh-lateral-more-sensitive'),
md('**Result: PLACEHOLDER**')]
C[i:i]=new

# fig8ab markdown
i=find("## fig8ab-choice-probability-lateral")
rep(i,"""comes from its experiment 1 tuning curve of the same condition (the same cells, recorded back to
back), by the two readings of the claims file.""","""comes from its experiment 1 tuning curve of the same condition (the same cells, recorded back to
back), by the two readings of the claims file, as in fig4dh-lateral-more-sensitive (the vector sum
weights each response by the angle it covers; the round-1 version did not, which pulled
preferences toward straight ahead).""")
rep(i,"""the vector sum over the 8 evenly spaced
headings only (experiment 1 adds +-22.5 degrees, which pulls a vector sum toward straight ahead),
and""","""the vector sum over the 8 evenly spaced
headings only, and""")
rep(i,"the data set does not say in which direction its CPs are signed).",
 "the data set does not say in which direction its CPs are signed; the share of CPs above 0.5 is\nprinted as a check of the sign).")
i+=1
rep(i,'print("CP range", cps.cp.min(), "to", cps.cp.max(), "; missing", int(cps.cp.isna().sum()))',
 'print("CP range", cps.cp.min(), "to", cps.cp.max(), "; missing", int(cps.cp.isna().sum()),\n      "; share above 0.5", round(float((cps.cp > 0.5).mean()), 3), "; mean", round(cps.cp.mean(), 4))')
rep(i,'"; vector sum over all 10 and over the 8 evenly spaced headings"','"; weighted vector sum over all 10 and vector sum over the 8 evenly spaced headings"')

# fig8cd markdown
i=find("## fig8cd-noise-not-preference")
rep(i,"""closest to the legend's 328 and 55 that can be run, and the outcome is judged on it; all 127
pairs (254 points) are shown as a variant.""","""closest to the legend's 328 and 55 that can be run, and the outcome is judged on it; all 127
pairs (254 points) are shown as a variant. The 127 pairs are not one of the claims file's
readings: they are its "all 179 pairs" reading with the 52 pairs over 1 mm missing. Their 254
points are nearer 328 than the 178 points used, so a reading of the claims file's rule by point
count alone would judge on them. The outcome is judged on the trained pairs because that sample
is a complete reading of the criterion and the Results speak of trained animals (Possible
rsignal Distributions in Area MSTd, paragraph 3); the variant's result is reported with the
conclusion.""")
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
cd entries/crcns-stc-1-gu-2011 && head -c 300 reproduce_gu_2011.ipynb | head -5; python $TMPDIR/nbedit.py && git diff --stat
```

```
/bin/bash: line 193: cd: entries/crcns-stc-1-gu-2011: No such file or directory
 .../crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb    | 183 +++++++++++++++++++--
 entries/crcns-stc-1-gu-2011/stc1.py                |  56 +++++--
 2 files changed, 214 insertions(+), 25 deletions(-)
```

**Agent calls Bash**

```bash
git diff reproduce_gu_2011.ipynb | head -30; git diff reproduce_gu_2011.ipynb | tail -5
```

```
diff --git a/entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb b/entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb
index 2b749d32ea..4dfef4b49f 100644
--- a/entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb
+++ b/entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb
@@ -30,13 +30,15 @@
     "single-electrode database of Figure 4, Figure S4 and Figure 8A, no training histories and no eye\n",
     "records. Experiments 1 and 2 hold the tuning curves, choice probabilities and neuronal thresholds\n",
     "of 129 single units of two trained monkeys from Gu et al. (2008); they are used for\n",
-    "fig8ab-choice-probability-lateral as a subset of the paper's database.\n",
+    "fig4dh-lateral-more-sensitive and fig8ab-choice-probability-lateral as a subset of the paper's\n",
+    "database.\n",
     "\n",
     "**Outside inputs.** None beyond the paper itself: the training group of each monkey comes from the\n",
     "paper's per-animal pair counts (Figure S2B legend), checked by the link claim\n",
     "`training-group-link`.\n",
     "\n",
-    "**Random numbers.** None of the analyses below draws random numbers.\n",
+    "**Random numbers.** Only the bootstrap intervals of fig5-intercept-lower-trained and\n",
+    "fig5-regression-coefficients draw random numbers, each from its own generator with a fixed seed.\n",
     "\n",
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../.. && grep -i -E "minutes|took|runtime|run time" transcripts/crcns-stc-1/author-answers-report.md transcripts/crcns-stc-1/author-report.md | head -5
```

```
transcripts/crcns-stc-1/author-report.md:- **Main assumption:** I took the pooled noise correlation to be the mean of the two per-condition values. It follows from z-scoring when both conditions have equal trial counts, and it reproduces 0.023 and 0.116 to the third decimal.
transcripts/crcns-stc-1/author-report.md:**4. Runtime and failures**
transcripts/crcns-stc-1/author-report.md:The work took about 25 minutes (16:53 to 17:13 UTC). The notebook runs in 99 s. Nothing failed. Some untracked files at the repo root (`.bashrc`, `.idea`, `scripts` and others) are sandbox device mounts created before I started; I left them alone. I did not commit or push.
```

**Agent**

99 s runtime, so I'll just run the whole entry.

**Agent calls Bash**

```bash
python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -20
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-crcns-stc-1-gu-2011 in executed/crcns-stc-1-gu-2011/.venv/share/jupyter/kernels/registry-crcns-stc-1-gu-2011
0 error(s)
pass  reproduce_gu_2011.ipynb  (55 s)
```

**Agent calls Bash**

```bash
python - <<'E'
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    t=''.join(c['source'])
    if any(k in t for k in ('rng_int','d_rs','crosses 1','H1 =','sens =','cps = pd','ut = stc1')) or i in (10,):
        print('=====',i)
        for o in c['outputs']:
            print(''.join(o.get('text','')) if 'text' in o else o.get('data',{}).get('text/plain',''))
E
```

```
===== 10
Group assigned per monkey: {19: 'trained', 18: 'trained', 17: 'naive', 2: 'trained', 1: 'naive', 5: 'trained', 3: 'naive', 24: 'trained'}
Pairs per group: {'trained': 89, 'naive': 38} ; units per group: {'trained': 146, 'naive': 64}

Single-unit experiments: monkeys [2, 5] ; units in experiment1 and experiment2: 129 129
experiment1 and experiment2 list the same cells in the same order (cell id before 'r'): True
Headings of experiment1 tuning curves (deg): [ 135.    90.    45.    22.5    0.   -22.5  -45.   -90.  -135.  -180. ]
Headings of experiment2 (deg): [ 9.    3.46  1.33  0.51  0.   -0.51 -1.33 -3.46 -9.  ]
Behavioural thresholds held (experiment2.behv, vestibular, visual): {'2': (1.2, 1.2), '5': (3.1, 3.25)}

===== 37
ves, rnoise_pooled: training p (full / additive) 0.0184 / 0.0179; intercept naive 0.0946, trained 0.0148
    separate fits: naive [0.0259, 0.1633], trained [-0.0180, 0.0476], overlap True
    ANCOVA model:  naive [0.0362, 0.1529], trained [-0.0203, 0.0499], overlap True
ves, rnoise_ves: training p (full / additive) 0.1832 / 0.1818; intercept naive 0.0785, trained 0.0243
    separate fits: naive [0.0070, 0.1500], trained [-0.0133, 0.0619], overlap True
    ANCOVA model:  naive [0.0139, 0.1430], trained [-0.0145, 0.0631], overlap True
vis, rnoise_pooled: training p (full / additive) 0.0074 / 0.0071; intercept naive 0.0964, trained 0.0087
    separate fits: naive [0.0277, 0.1650], trained [-0.0257, 0.0430], overlap True
    ANCOVA model:  naive [0.0376, 0.1551], trained [-0.0279, 0.0452], overlap True
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && python - <<'E'
import json,uuid
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
i=[k for k,c in enumerate(C) if ''.join(c['source']).startswith('rows = []\nfor u1, u2 in zip(mat["experiment1"].units, mat["experiment2"].units):\n    for cond in ("ves", "vis"):\n        c1 = getattr(u1, cond)\n        rows.append({"cell": u1.file_id, "monkey": stc1.monkey_of(u1.file_id), "condition": cond,\n                     "pref_vector_sum"')]
assert len(i)==1; i=i[0]
s=''.join(C[i]['source'])
s=s.replace('''rows = []
for u1, u2''','''rows = []
even8 = np.isin(H1, np.arange(-180, 180, 45))
for u1, u2''',1)
s=s.replace('''                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global),
                     "thr_spline"''','''                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global),
                     "variant_pref_vector_sum_8": stc1.pref_vector_sum(c1.stim_global[even8], c1.resp_global[even8]),
                     "thr_spline"''')
s=s.replace('for pref in ("pref_vector_sum", "pref_spline_peak"):','for pref in ("pref_vector_sum", "pref_spline_peak", "variant_pref_vector_sum_8"):')
s=s.replace('crit = fig4dh[fig4dh.threshold != "variant_thr_experiment2"]','crit = fig4dh[(fig4dh.threshold != "variant_thr_experiment2") & ~fig4dh.preference.str.startswith("variant")]')
C[i]['source']=s.splitlines(keepends=True)
# markdown mention
j=i-2
m=''.join(C[j]['source'])
m=m.replace("straight ahead). First, a check","straight ahead), and the vector sum over the 8 evenly spaced headings alone. First, a check")
C[j]['source']=m.splitlines(keepends=True)
print(nb.get('nbformat'), nb.get('nbformat_minor'), sum('id' in c for c in C), len(C))
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
```

```
4 5 62 66
```

**Agent calls Bash**

```bash
python - <<'E'
import json
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p))
print([c.get('id') for c in nb['cells'][:3]])
n=0
for k,c in enumerate(nb['cells']):
    if 'id' not in c: c['id']=f"fig4dh-{n}"; n+=1
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat
```

```
['8834b70e', '89a3ec57', '08811b5d']
 .../crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb    | 189 +++++++++++++++++++--
 entries/crcns-stc-1-gu-2011/stc1.py                |  56 ++++--
 2 files changed, 220 insertions(+), 25 deletions(-)
```

**Agent calls Bash**

```bash
cd ../.. && python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -2 && python - <<'E'
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'sens = pd' in ''.join(c['source']):
        for o in c['outputs']: print(''.join(o.get('text','')))
E
```

```
0 error(s)
pass  reproduce_gu_2011.ipynb  (56 s)
Values: 258 ; infinite thresholds left out: {'thr_spline': 0, 'thr_linear': 2, 'variant_thr_experiment2': 0}
Threshold ranges (degrees):
       thr_spline    thr_linear  variant_thr_experiment2
count      258.00  2.560000e+02                   258.00
min          2.65  3.080000e+00                     1.51
50%         31.10  4.168000e+01                    17.84
max       2759.96  1.040646e+17                   300.00
Spearman rho of the Fisher thresholds with the experiment 2 thresholds: {'thr_spline': np.float64(0.304), 'thr_linear': np.float64(0.366)}

               preference               threshold scale ves_n_fa/lat  ves_median_fa  ves_median_lat   ves_p vis_n_fa/lat  vis_median_fa  vis_median_lat   vis_p  two_factor_p_group  two_factor_p_interaction  lateral_lower_both
          pref_vector_sum              thr_spline   raw        43/86       56.33336        31.96716 0.86280        58/71       38.67137        13.90347 0.00600             0.34865                   0.23063                True
          pref_vector_sum              thr_spline log10        43/86       56.33336        31.96716 0.04011        58/71       38.67137        13.90347 0.00000             0.00000                   0.02590                True
          pref_vector_sum              thr_linear   raw        43/86       78.23421        40.27441 0.48166        56/71       65.62424        15.39149 0.26182             0.50971                   0.18896                True
          pref_vector_sum              thr_linear log10        43/86       78.23421        40.27441 0.64416        56/71       65.62424        15.39149 0.00332             0.01271                   0.07796                True
          pref_vector_sum variant_thr_experiment2   raw        43/86       39.84300        16.05800 0.00026        58/71       24.08900         9.98100 0.47696             0.00401                   0.05358                True
          pref_vector_sum variant
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && python - <<'E'
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if s.startswith('**Result') and any(k in s for k in ('main effect of\ntraining','5.41 times','For all 88','not reproduced, resting','not reproduced, on a subset','178 points')):
        print('=====',i);print(s)
E
```

```
===== 38
**Result: partially reproduced, resting on the pooled-rnoise assumption.** The main effect of
training holds in both conditions with the pooled rnoise (vestibular p = 0.0184, visual p = 0.0074;
paper 0.02 and 0.008). The naive intercepts are higher (0.095 against 0.015, and 0.096 against
0.009). But the 95% intervals of the intercepts overlap under every reading. With separate fits,
vestibular naive is [0.026, 0.163] and trained [-0.018, 0.048]. In the ANCOVA model they are
[0.036, 0.153] and [-0.020, 0.050]. The visual intervals overlap the same way, as do those of the
additive model. With the same-condition rnoise the vestibular main effect is not significant
(p = 0.183).
===== 45
**Result: reproduced, resting on the claims file's tuning amplitude and baseline, which the paper
does not give.** At 2000 neurons the naive threshold is 5.41 times the independent one (4.5 to 5.5),
and the trained threshold is within 0.01% of the naive one, under both rsignal readings. The ratio
depends on the unstated parameters: 4.32 to 5.90 over the amplitude and baseline variants. It is
9.18 without the trace term of equation 3.
===== 51
**Result: partially reproduced, resting on the same tuning parameters.** For all 88 pairs with
positive rsignal the trained threshold is lower, and for 92 of 93 with negative rsignal it is
higher. The exception has rsignal = -0.011 (second preference -2 degrees), where trained is 0.09%
lower than naive: the sign changes just below rsignal = 0, not at it. The criterion asks for every
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/concl.py <<'E'
import json
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
def idx(pred):
    m=[i for i,c in enumerate(C) if pred(''.join(c['source']))]; assert len(m)==1,m; return m[0]
def put(i,t): C[i]['source']=t.strip('\n').splitlines(keepends=True)
def rep(i,a,b):
    s=''.join(C[i]['source']); assert a in s,(i,a); put(i,s.replace(a,b))
i=idx(lambda s:s.startswith('**Result') and 'main effect of\ntraining' in s)
rep(i,"additive model. With the same-condition","additive model, and the bootstrap intervals of each group's own fit (vestibular naive [0.040,\n0.151], trained [-0.016, 0.046]; visual [0.021, 0.172] and [-0.023, 0.040]). With the same-condition")
i=idx(lambda s:s.startswith('**Result') and '5.41 times' in s)
rep(i,"under both rsignal readings. The ratio","under both rsignal readings. The two readings give the same values because their rsignal\ndiffers by at most 5.6e-07. The ratio")
i=idx(lambda s:s.startswith('**Result') and 'For all 88' in s)
rep(i,"the sign changes just below rsignal = 0, not at it.","the sign changes just below rsignal = 0, not at it.\nTrained/naive crosses 1 at rsignal = -0.0216 (second preference between -1 and -2 degrees) under\nboth rsignal readings.")
i=idx(lambda s:s.startswith('**Result: not reproduced, resting'))
put(i,"""**Result: partially reproduced, resting on the same tuning parameters.** The proportions of
positive rsignal are 48.6%, 73.1% and 92.4% for [-180, 180], [0, 180] and [30, 150], all within
tolerance. The trained improvement over naive grows from -0.48% to 4.83% as the range narrows, and
then levels off (4.58% to 4.83%). Its largest value, 4.83%, is below 8 +- 0.8%. Under the variants
the largest improvement is 3.6% to 6.0% with other amplitudes or baselines, and 11.75% without the
trace term. The effect is present and grows as the claim says, but its size at best is smaller.""")
i=idx(lambda s:s.startswith('**Result: PLACEHOLDER'))
put(i,"""**Result: reproduced, on a subset of the paper's data (258 values from 129 units of two trained
monkeys, against 992 and 556 neurons of naive and trained animals) and without the training factor
of the paper's ANOVA.** On synthetic curves the weighted vector sum and the spline peak recover the
true preference to within 3 degrees, and the unweighted vector sum does not (30 degrees comes out
as 16). Lateral units have lower median thresholds than fore-aft ones under every reading and
variant, in both conditions. Under one of the 8 readings of the claims file the difference reaches
p < 0.001: vector-sum preference, spline threshold, log10, with condition as a factor (p = 1.9e-07).
In that reading, per condition, visual gives p = 3.4e-07 and vestibular p = 0.040, so the
per-condition reading fails in the vestibular condition. The other 7 readings give p from 0.0033 to
0.77. With the spline-peak preference no reading reaches p < 0.05. The neurometric thresholds of
experiment 2, a variant, give two-factor p = 7e-07 (log10, vector sum) and p = 0.0011 (log10, spline
peak). Per monkey, the visual difference is significant in both (p = 0.00024 and 0.00017) and the
vestibular one in neither (p = 0.082 and 0.185). The linear reading leaves out 2 values whose curve
is flat at 0.""")
i=idx(lambda s:s.startswith('**Result: not reproduced, on a subset'))
put(i,"""**Result: not reproduced, on a subset of the paper's data (258 values from 129 units of two trained
monkeys, against 311).** Fore-aft units do not have smaller choice probabilities than lateral ones.
With preferences from the spline peak, fore-aft 0.527 against lateral 0.542, p = 0.136. With the
weighted vector sum, fore-aft 0.533 against lateral 0.535, p = 0.796. Leftward and rightward units
do not differ under any reading (p = 0.25 to 0.35), as the paper reports. In the variants, the
vector sum over the 8 evenly spaced headings gives p = 0.691, and the distance of CP from 0.5 gives
p = 0.10 to 0.17. The vector sum and the spline peak put 71.7% of values in the same group. Of the
CPs, 71.7% are above 0.5 (mean 0.534), as expected if they are signed relative to each unit's
preferred direction; the data set does not say so.""")
i=idx(lambda s:s.startswith('**Result') and '178 points' in s)
rep(i,"and vestibular preferences, the difference is significant (0.022 against 0.096, p = 0.0009).",
"""and vestibular preferences, the difference is significant (0.022 against 0.096, p = 0.0009); with
visual preferences it is not (p = 0.623). That variant's 254 points are nearer the legend's 328
than the 178 used, so judged by point count alone, the claims file's rule would point to it. It is
not one of the rule's readings (it is the all-179 reading with 52 pairs missing), and the outcome
is kept on the trained pairs, which the Results name. Under the variant the claim would not hold
with vestibular preferences.""")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
python $TMPDIR/concl.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011 && python - <<'E'
import json
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
n=0
for c in C:
    s=''.join(c['source']); t=s
    t=t.replace("The other 7 readings give p from 0.0033 to\n0.77.","In the other 7 readings the two-factor\np ranges from 0.013 to 0.77, and no per-condition reading has p < 0.001 in both conditions.")
    t=t.replace("print(fig4dh.round(5).to_string(index=False))",'print(fig4dh.to_string(index=False, float_format=lambda x: f"{x:.3g}"))')
    if t!=s: c['source']=t.splitlines(keepends=True); n+=1
print(n)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
```

```
Exit code 1
/bin/bash: line 1: cd: entries/crcns-stc-1-gu-2011: No such file or directory
```

**Agent calls Bash**

```bash
pwd; python - <<'E'
import json
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
n=0
for c in C:
    s=''.join(c['source']); t=s
    t=t.replace("The other 7 readings give p from 0.0033 to\n0.77.","In the other 7 readings the two-factor\np ranges from 0.013 to 0.77, and no per-condition reading has p < 0.001 in both conditions.")
    t=t.replace("print(fig4dh.round(5).to_string(index=False))",'print(fig4dh.to_string(index=False, float_format=lambda x: f"{x:.3g}"))')
    if t!=s: c['source']=t.splitlines(keepends=True); n+=1
print(n)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
```

```
entries/crcns-stc-1-gu-2011
2
```

**Agent calls Bash**

```bash
python - <<'E'
import json
p='reproduce_gu_2011.ipynb'; nb=json.load(open(p)); C=nb['cells']
c=C[-1]; s=''.join(c['source']); assert s.startswith('## Summary')
R=[("| fig7c-narrow-preferences | not reproduced (assumed) |","| fig7c-narrow-preferences | partially reproduced (assumed) |"),
("| fig8ab-choice-probability-lateral | not reproduced (subset) |","| fig4dh-lateral-more-sensitive | reproduced (subset, trained animals only) |\n| fig8ab-choice-probability-lateral | not reproduced (subset) |"),
("| fig4 (three claims), fig4dh (two claims), figs4 | blocked, data missing (no naive single units) |","| fig4 (three claims), fig4dh-training-no-sensitivity-change, figs4 | blocked, data missing (no naive single units) |"),
("Choice probabilities come from 129 units of two monkeys, not\nthe paper's 311.","Single-unit thresholds and choice probabilities come from 129 units\nof two trained monkeys, not the paper's database of naive and trained animals (992 and 556\nneurons, 311 choice probabilities), so the preference-group test of Figure 4 runs without the\ntraining factor.")]
for a,b in R:
    assert a in s,a; s=s.replace(a,b)
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
cd ../.. && python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -2; date -u
```

```
0 error(s)
pass  reproduce_gu_2011.ipynb  (49 s)
Fri Nov  6 18:04:09 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'E'
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'sens = pd' in ''.join(c['source']):
        for o in c['outputs']: print(''.join(o.get('text',''))[1200:5000])
E
cat entries/crcns-stc-1-gu-2011/README.md | head -40
```

```
43/86           39.8            16.1 0.000264        58/71           24.1            9.98    0.477             0.00401                    0.0536                True
          pref_vector_sum variant_thr_experiment2 log10        43/86           39.8            16.1 7.58e-05        58/71           24.1            9.98  0.00193            7.28e-07                     0.592                True
         pref_spline_peak              thr_spline   raw        50/79           37.3              35    0.503        80/49           28.6              17    0.653               0.658                     0.428                True
         pref_spline_peak              thr_spline log10        50/79           37.3              35    0.835        80/49           28.6              17   0.0848               0.256                     0.155                True
         pref_spline_peak              thr_linear   raw        50/79           58.4            42.3    0.428        78/49           43.6            17.7     0.43               0.771                     0.279                True
         pref_spline_peak              thr_linear log10        50/79           58.4            42.3    0.629        78/49           43.6            17.7   0.0942               0.378                      0.12                True
         pref_spline_peak variant_thr_experiment2   raw        50/79           35.8            14.9 0.000148        80/49           15.6            12.6    0.936              0.0152                    0.0111                True
         pref_spline_peak variant_thr_experiment2 log10        50/79           35.8            14.9 2.31e-05        80/49           15.6            12.6    0.576             0.00109                    0.0151                True
variant_pref_vector_sum_8              thr_spline   raw        41/88           56.3            32.6    0.858        58/71           38.7            13.9    0.006               0.348                     0.231                True
variant_pre
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/crcns-stc-1-gu-2011/README.md'; s=open(p).read()
R=[("| At best the trained threshold is about 8% lower (Figure 7C) | Not reproduced |","| At best the trained threshold is about 8% lower (Figure 7C) | Partially reproduced |"),
("| Fore-aft units have smaller choice probabilities (Figure 8A, 8B) | Not reproduced |","| Lateral units are more sensitive around straight ahead (Figures 4D, 4H; trained animals only) | Reproduced |\n| Fore-aft units have smaller choice probabilities (Figure 8A, 8B) | Not reproduced |"),
("| Training histories, single-electrode database (Figures 2A, 4, S4) | Blocked: data missing |","| Training histories, comparisons of naive and trained single units (Figures 2A, 4, S4) | Blocked: data missing |")]
for a,b in R: assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -c "^- id:" claims/crcns-stc-1/*.yaml; grep -c "^- claim:" attempts/crcns-stc-1-gu-2011-01.yaml; cat entries/crcns-stc-1-gu-2011/entry.yaml; grep -n "verifications" -A12 docs/*.md schema* 2>/dev/null | grep -i -E "date|kind|by|reviewed|agrees|outcome|reason|response" | head -20; ls
```

```
35
35
schema_version: 1
name: crcns-stc-1-gu-2011
type: reproduction
title: Perceptual learning and noise correlations in MSTd (Gu et al. 2011)
description: Tests the findings of Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis and Angelaki
  (2011) on CRCNS stc-1, which holds the noise and signal correlations and preferred headings of the
  paper's 127 MSTd pairs under 1 mm, and single-unit tuning and choice probabilities of two trained
  monkeys. It compares noise correlations between naive and trained animals, their relation to
  signal correlation, and the paper's population simulations. Analyses that need spike times,
  distances or the single-electrode database cannot be run on it.
license: Apache-2.0
notebooks:
- path: reproduce_gu_2011.ipynb
  title: Reproducing Gu et al. (2011) from CRCNS stc-1
  runtime_minutes: 2
helpers:
- stc1.py
related:
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python -c "
import json,glob
for f in glob.glob('schemas/*attempt*'):
    s=json.load(open(f)) if f.endswith('json') else None
    if s: print(json.dumps(s['properties'].get('verifications'),indent=1)[:2500]); print(json.dumps(s.get('\$defs',s.get('definitions',{})).get('verification','') ,indent=1)[:3000])
"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'E'
p='attempts/crcns-stc-1-gu-2011-01.yaml'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
# fig5 intercept
rep("""    fits give naive 0.026 to 0.163 and trained -0.018 to 0.048; the ANCOVA model gives 0.036 to 0.153
    and -0.020 to 0.050. Visual is alike, as is the additive model. With the same-condition rnoise
    the vestibular main effect is not significant (p = 0.183).""","""    fits give naive 0.026 to 0.163 and trained -0.018 to 0.048; the ANCOVA model gives 0.036 to 0.153
    and -0.020 to 0.050. Visual is alike, as is the additive model. Bootstrap intervals of each
    group's own fit (2000 resamples of pairs within the group) also overlap, vestibular naive 0.040
    to 0.151 and trained -0.016 to 0.046, visual 0.021 to 0.172 and -0.023 to 0.040. With the
    same-condition rnoise the vestibular main effect is not significant (p = 0.183).""")
rep("""    per-group fits, the ANCOVA model with interaction (Figure 5 legend, "regression fits (ANCOVA)")
    and the additive model are all shown, and all overlap.""","""    per-group fits, the ANCOVA model with interaction (Figure 5 legend, "regression fits (ANCOVA)"),
    the additive model and a bootstrap over pairs are all shown, and all overlap.""")
# fig6a
rep("""    within 0.01% of naive, under both rsignal readings, which give the same values. The ratio is""",
"""    within 0.01% of naive, under both rsignal readings, which give the same values because their
    rsignal differs by at most 5.6e-07; the open parameters that matter are the amplitude and
    baseline. The ratio is""")
# fig7a
rep("""    with negative rsignal. The exception, at rsignal = -0.011, has trained 0.09% below naive; the
    sign changes just below rsignal = 0. The criterion asks for every pair.""","""    with negative rsignal. The exception, at rsignal = -0.011, has trained 0.09% below naive; the
    ratio of trained to naive crosses 1 at rsignal = -0.0216, between second preferences of -1 and
    -2 degrees. The criterion asks for every pair.""")
# fig7c
rep("""- claim: fig7c-narrow-preferences
  outcome: not_reproduced""","""- claim: fig7c-narrow-preferences
  outcome: partially_reproduced""")
rep("""    4.83%, is below 8 +- 0.8%. The maximum is 3.6% to 6.0% under the amplitude and baseline
    variants and 11.75% without the trace term of equation 3.""","""    4.83%, is below 8 +- 0.8%. The maximum is 3.6% to 6.0% under the amplitude and baseline
    variants and 11.75% without the trace term of equation 3. Two of the criterion's three parts
    hold (the improvement grows as the range narrows; the proportions are within tolerance) and the
    best improvement is smaller than the paper's, so the effect is present but weaker. Recorded as
    not_reproduced before the round-1 verification and changed to partially_reproduced, as the
    verifier proposed.""")
# fig8ab
rep("""  notes: On 258 values from 129 units of monkeys 2 and 5, fore-aft units do not have smaller
    choice probabilities. With spline-peak preferences, fore-aft 0.527 against lateral 0.542, p =
    0.136. With the vector sum, 0.546 against 0.511, p = 0.0006, the opposite direction. Leftward
    and rightward units do not differ under any reading (p = 0.27 to 0.56), as the paper says.
    Variants, the vector sum over the 8 evenly spaced headings gives p = 0.691, and the distance of
    CP from 0.5 gives p = 0.10 to 0.85. The vector sum and spline readings put 64% of values in the
    same group.""","""  notes: On 258 values from 129 units of monkeys 2 and 5, fore-aft units do not have smaller
    choice probabilities. With spline-peak preferences, fore-aft 0.527 against lateral 0.542, p =
    0.136. With the weighted vector sum, 0.533 against 0.535, p = 0.796. Leftward and rightward
    units do not differ under any reading (p = 0.25 to 0.35), as the paper says. Variants, the
    vector sum over the 8 evenly spaced headings gives p = 0.691, and the distance of CP from 0.5
    gives p = 0.10 to 0.17. The vector sum and spline readings put 71.7% of values in the same
    group. Of the CPs 71.7% are above 0.5 (mean 0.534), consistent with CPs signed relative to each
    unit's preferred direction. The round-1 version used an unweighted vector sum, biased toward
    straight ahead by the uneven headings, which gave p = 0.0006 in the opposite direction; it was
    replaced.""")
rep("""  - Preferred headings from the experiment 1 tuning curves of the same cells, by the two readings of
    the claims file; the data set does not say how its CPs are signed.""","""  - Preferred headings from the experiment 1 tuning curves of the same cells, by the two readings of
    the claims file; the data set does not say how its CPs are signed.
  - The experiment 1 headings are unevenly spaced (+-22.5 degrees added to the eight 45 degrees
    apart), so the vector sum weights each response by half the gaps to its two neighbours. On
    synthetic curves this recovers the preference to within 3 degrees, where the unweighted sum
    puts 30 degrees at 16. A choice made here, after the round-1 verification.""")
# fig8cd
rep("""    (254 points), vestibular preferences give a significant difference (0.022 against 0.096, p =
    0.0009), visual do not (p = 0.623).""","""    (254 points), vestibular preferences give a significant difference (0.022 against 0.096, p =
    0.0009), visual do not (p = 0.623). The variant's 254 points are nearer the legend's 328 than
    the 178 used, so by point count alone the claims file's rule would judge on it, and the claim
    would then fail with vestibular preferences. The outcome is kept on the trained pairs, a
    complete reading of the criterion and the sample the Results name ("in trained animals"); the
    127 pairs are the all-179 reading with the 52 pairs over 1 mm missing.""")
# fig2a
rep("""    animal for two of the five trained monkeys (vestibular 1.2 and 3.1 degrees, both inside 0.9 to
    3.3), not the thresholds over sessions the criterion fits.""","""    animal for two of the five trained monkeys (vestibular 1.2 and 3.1 degrees, both inside 0.9 to
    3.3; visual 1.2 and 3.25 degrees), not the thresholds over sessions the criterion fits. Whether
    these are plateau values, and the fall from above 10 degrees, cannot be checked. The notebook
    states them under the data check.""")
# fig4dh
old_start=s.index("- claim: fig4dh-lateral-more-sensitive")
old_end=s.index("- claim: fig4dh-training-no-sensitivity-change")
s=s[:old_start]+"""- claim: fig4dh-lateral-more-sensitive
  outcome: reproduced
  notebook: reproduce_gu_2011.ipynb
  output: claim:fig4dh-lateral-more-sensitive
  notes: On 258 values from 129 units of two trained monkeys, lateral units have lower median
    thresholds than fore-aft ones under every reading, in both conditions. Under one of the 8
    readings of the claims file the difference reaches p < 0.001, as the criterion requires
    ("under one reading"): vector-sum preference, spline threshold, log10, condition as a factor,
    p = 1.9e-07. Per condition that reading gives visual p = 3.4e-07 and vestibular p = 0.040, so
    the per-condition reading fails in the vestibular condition. In the other 7 readings the
    two-factor p is 0.013 to 0.77, and with spline-peak preferences no reading reaches p < 0.05.
    The neurometric thresholds of experiment 2, a variant, give two-factor p = 7.3e-07 (vector sum,
    log10) and 0.0011 (spline peak, log10). Per monkey, the visual difference is significant in both
    (p = 0.00024 and 0.00017) and the vestibular one in neither (p = 0.082 and 0.185). Tested after
    the round-1 verification found that the claim had been blocked wrongly.
  deviations:
  - A subset of the paper's data. The experiment 1 tuning curves hold 129 units of two trained
    monkeys (Gu et al. 2008), against the paper's 992 visual and 556 vestibular neurons of naive
    and trained animals, so the ANOVA has no training factor. The two-factor reading has
    preference group and condition.
  - For the linear interpolation the derivative at 0, a sampled heading, is the slope between -22.5
    and 22.5 degrees, a choice made here as a piecewise-linear curve has no derivative at a knot.
    Two values whose curve is flat at 0 have infinite thresholds and are left out of that reading.
  - The tuning curves in spikes/s are read as counts over the middle 1 s (Experimental Procedures,
    Noise and Signal Correlations); a different window scales all thresholds alike.
  - The vector sum weights each response by the angle it covers, as in fig8ab.
"""+s[old_end:]
rep("""  notes: Depends on fig4dh-lateral-more-sensitive; no naive single units in the data set.""",
"""  notes: Needs naive single units, which the data set does not hold; the trained units are tested
    under fig4dh-lateral-more-sensitive.""")
# findings
rep("""    of Figure 2A by one threshold for each of two monkeys. Nineteen of the paper's 34 claims
    cannot be tested.""","""    of Figure 2A by one threshold for each of two monkeys. Eighteen of the 35 claims cannot be
    tested.""")
rep("""    the data set the fore-aft and lateral CPs differ in opposite directions under the vector sum and
    the spline peak.""","""    the data set neither the vector sum nor the spline peak gives fore-aft CPs smaller than lateral
    ones (p = 0.80 and 0.14).""")
open(p,'w').write(s)
E
python $TMPDIR/rec.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> attempts/crcns-stc-1-gu-2011-01.yaml <<'E'
verifications:
- date: '2026-11-06'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier checked the archive listing for the
    blocked claims and tested the helper functions on synthetic inputs (tls_plane, threshold,
    sigma_for_fwhm, preference_group, pref_spline_peak, pref_vector_sum, pooled_rnoise). Report in
    transcripts/crcns-stc-1/verifier-1-report.md.
  results:
  - claim: training-group-link
    agrees: true
    outcome: reproduced
    reason: In cell 13 the eight per-monkey counts match the Figure S2B counts one to one, giving 89
      trained and 38 naive pairs and 146 and 64 units; monkeys 2 and 5, the ones with behavioural
      thresholds, both fall in the trained group. The 89/38 split follows from matching by count, so
      only the neuron counts and the behaviour check are independent tests.
    response: No change.
  - claim: fig2b-trained-lower-noise-correlation
    agrees: true
    outcome: reproduced
    reason: Trained 0.0241 +- 0.0174, naive 0.1190 +- 0.0316, both within tolerance; Student p =
      0.0056 (paper 0.006), Welch p = 0.011. It checked on synthetic data that the pooled-z-score
      Pearson equals the mean of the per-condition values with equal trial numbers and no outliers;
      whether the stored values include outlier removal or renormalization cannot be told (problem
      5, not affecting a conclusion).
    response: No change; the assumption and its limits were already stated.
  - claim: figs2b-individual-animals
    agrees: true
    outcome: reproduced
    reason: The lowest naive animal mean (0.088) is above the highest mean among the trained animals
      shown (0.048), with counts 35/26/18/8 and 22/11/5. There are no time courses because the data
      set holds no spike times.
    response: No change.
  - claim: fig1-example-pair
    agrees: true
    outcome: reproduced
    reason: One pair, m2c338r1, has all four values within tolerance (0.828, 0.786, 0.291, 0.142).
      The per-pair p values cannot be checked without trial counts.
    response: No change.
  - claim: fig1f-modality-correlated
    agrees: true
    outcome: partially_reproduced
    reason: Spearman R = 0.449, p = 1e-7, on n = 127, the smaller sample the criterion allows. R is
      outside 0.342 to 0.418.
    response: No change.
  - claim: fig1f-modality-means-equal
    agrees: true
    outcome: reproduced
    reason: Paired p = 0.73, n = 127. The vestibular mean of 0.056 is outside the paper's 0.035 +-
      0.014, but the paper's figure is from 179 pairs.
    response: No change.
  - claim: fig5-noise-signal-positive
    agrees: true
    outcome: reproduced
    reason: With pooled rnoise the rsignal slope is positive with p = 0.00017 (vestibular) and p =
      0.0007 (visual).
    response: No change.
  - claim: fig5-slope-unchanged
    agrees: true
    outcome: reproduced
    reason: Interaction p = 0.83 (vestibular) and 0.96 (visual).
    response: No change.
  - claim: fig5-intercept-lower-trained
    agrees: true
    outcome: partially_reproduced
    reason: The training main effect is significant (p = 0.018 vestibular, 0.0074 visual, pooled
      rnoise). The 95% intervals of the intercepts overlap under every construction, separate fits,
      the ANCOVA model and the additive model. It could not check what interval method the paper
      used; a bootstrap interval for the per-group intercept would help.
    response: Added bootstrap 95% intervals of each group's intercept from its own fit (2000
      resamples of pairs within the group). They overlap too (vestibular naive 0.040 to 0.151,
      trained -0.016 to 0.046). Outcome kept.
  - claim: fig5-regression-coefficients
    agrees: true
    outcome: partially_reproduced
    reason: Under readings (a) and (b) the slopes are 0.119/0.084 and 0.132/0.085 and the naive
      intercept 0.077/0.074, all within tolerance. The trained intercept is 0.003/0.002, outside
      0.005 +- 0.0005, though still below the naive one. Reading (c) misses the visual slope (0.106).
      Cell 0 said that no analysis draws random numbers, but this cell runs a seeded bootstrap
      (problem 4, not affecting a conclusion).
    response: Corrected the header of the notebook, which now names the two seeded bootstraps.
      Outcome kept.
  - claim: fig6a-population-thresholds
    agrees: true
    outcome: reproduced
    reason: At N = 2000 the naive/independent ratio is 5.41 (within 4.5 to 5.5) and trained/naive
      1.000, under the claims-file reading (A30/B10) for both rsignal readings. The result is
      sensitive to the unstated amplitude and baseline (4.32 to 5.90; A35 gives 5.57). The two
      rsignal readings differ by at most 5e-7 in rsignal, so the second adds nothing (problem 6, not
      affecting a conclusion).
    response: The notebook now prints the largest difference in rsignal between the two readings
      (5.6e-07) and the conclusion and notes say the open parameters that matter are the amplitude
      and baseline. Outcome kept.
  - claim: fig6b-slope-not-intercept
    agrees: true
    outcome: reproduced
    reason: Over a slope width of 0.2 the threshold changes by 1.97 degrees, over an intercept width
      of 0.2 by 0.11 degrees. The threshold falls from the trained to the naive intercept (7.251 to
      7.217). It is not monotone at intercept 0 to 0.02.
    response: No change.
  - claim: fig7a-pair-sign-of-effect
    agrees: true
    outcome: partially_reproduced
    reason: All 88 pairs with positive rsignal follow the rule, and 92 of 93 with negative rsignal.
      The exception is at rsignal = -0.011 (pref2 = -2 degrees), and the criterion requires every
      pair. It asked for the rsignal at which trained/naive equals 1.
    response: Added the crossing, rsignal = -0.0216 (between second preferences of -1 and -2
      degrees) under both rsignal readings. Outcome kept.
  - claim: fig7c-narrow-preferences
    agrees: false
    outcome: partially_reproduced
    reason: The proportions are 48.6, 73.1 and 92.4%, all within tolerance, and the improvement
      grows from -0.5% to about 4.8%. The best improvement of 4.83% is far outside 8 +- 0.8. It stays
      at 3.6 to 6.0% under the amplitude and baseline variants; only dropping the trace term, which
      is not equation 3, reaches 8%.
    response: Changed from not_reproduced to partially_reproduced. Two of the criterion's three parts
      hold and the effect is present but smaller, which is the protocol's partially_reproduced.
  - claim: fig8ab-choice-probability-lateral
    agrees: true
    outcome: not_reproduced
    reason: 258 CPs from two trained monkeys, a subset of the paper's 311. No preferred-heading
      reading gives fore-aft CP smaller with p < 0.05. The vector sum over all 10 headings gives the
      opposite sign (p = 0.0006), but that reading is biased; stc1.pref_vector_sum takes the sum
      over the unevenly spaced headings with no weighting for angular spacing, so true preferences
      of 30/60/90/120 degrees come out as 16/35/59/93 and many lateral units are labelled fore-aft.
      It should be dropped or replaced by a spacing-weighted vector sum (problem 1). It could not
      check how many of the 258 CPs are in the paper's 311 or the sign convention of the CPs.
    response: Replaced the vector sum by one that weights each response by half the gaps to its
      neighbours, shown on synthetic curves in the notebook to recover the preference within 3
      degrees. It gives fore-aft 0.533 against lateral 0.535, p = 0.796. Added the share of CPs
      above 0.5 (71.7%, mean 0.534) as a check of the sign. The overlap with the paper's 311 cannot
      be checked from the data set. Outcome kept.
  - claim: fig8cd-noise-not-preference
    agrees: true
    outcome: reproduced
    reason: Trained pairs, as the Results specify ("in trained animals"), p = 0.43 (visual
      preference) and 0.17 (vestibular). The claims file says to judge under the reading whose point
      count is closest to 328; the 127-pair variant (254 points) is closer than the 178 used, and with
      vestibular preference it gives p = 0.0009. It keeps reproduced because the Results restrict the
      statement to trained animals, but the notebook should state this conflict with the claims-file
      rule (problem 3).
    response: The notebook's description and conclusion, and the notes, now state the conflict and
      why the outcome is kept on the trained pairs. Outcome kept.
  - claim: fig2c-timecourse-naive-higher
    agrees: true
    outcome: blocked
    reason: It confirmed the archive listing; stc-1/live holds only MSTd.mat (65 KB, derived),
      VIP.mat, demo.m, docs, filelist.txt and checksums. There are no spike times.
    response: No change.
  - claim: figs2a-difference-decreases
    agrees: true
    outcome: blocked
    reason: No spike times.
    response: No change.
  - claim: fig3-mean-response-unchanged
    agrees: true
    outcome: blocked
    reason: No spike times.
    response: No change.
  - claim: fig3-fano-unchanged
    agrees: true
    outcome: blocked
    reason: No spike times.
    response: No change.
  - claim: figs8c-renormalization
    agrees: true
    outcome: blocked
    reason: No trial-ordered responses.
    response: No change.
  - claim: discussion-stimulus-reduces-correlation
    agrees: true
    outcome: blocked
    reason: No prestimulus responses.
    response: No change.
  - claim: figs1-distance
    agrees: true
    outcome: blocked
    reason: No distances, and no pairs over 1 mm (all 127 are under 1 mm).
    response: No change.
  - claim: methods-single-vs-multiple-electrodes
    agrees: true
    outcome: blocked
    reason: No electrode label, and the recording structure (cell 6) cannot stand in for one. Cell 6
      finds a recording with 6 pairs, against the paper's stated maximum of 5; it is noted but not
      explained (problem 8, not affecting a conclusion).
    response: No change. The six pairs are all pairs of four units; the data set holds nothing that
      could explain the difference from the paper's maximum of five, which stays a finding.
  - claim: fig2a-behavioral-learning
    agrees: true
    outcome: blocked
    reason: There are no training histories. experiment2.behv holds one threshold per monkey for
      monkeys 2 and 5 (1.2/1.2 and 3.1/3.25 degrees), both inside 0.9 to 3.3 degrees. Only the
      plateau part could be checked, for 2 of 5 animals, and the notebook does not report it
      (problem 7, not affecting a conclusion).
    response: The notebook now states these thresholds against the criterion's plateau range under
      the data check, and the notes give them. Outcome kept, as the criterion needs the fall over
      sessions.
  - claim: fig4-tuning-width-visual
    agrees: true
    outcome: blocked
    reason: The single-unit data have no naive animals. Trained medians could be computed from the
      experiment1 tuning curves for a descriptive comparison only, and the ANOVA selection cannot be
      applied to trial-averaged curves.
    response: No change.
  - claim: fig4-tuning-width-vestibular
    agrees: true
    outcome: blocked
    reason: As fig4-tuning-width-visual.
    response: No change.
  - claim: fig4-amplitude-unchanged
    agrees: true
    outcome: blocked
    reason: As fig4-tuning-width-visual.
    response: No change.
  - claim: fig4dh-lateral-more-sensitive
    agrees: false
    reason: Blocked wrongly. Its main claim is the preference-group effect, which can be tested within
      the two trained monkeys from experiment1 and experiment2, with the claims-file Fisher threshold
      on interpolated tuning curves; the notebook used exactly this subset for fig8ab. The claim
      should be partially tested, not blocked (problem 2).
    response: Tested on the 129 trained units under the claims file's readings, without the training
      factor. Lateral thresholds are lower under every reading, and one of the 8 readings reaches p <
      0.001 (p = 1.9e-07), so the outcome is reproduced on the subset, with the subset and the missing
      training factor as deviations.
  - claim: fig4dh-training-no-sensitivity-change
    agrees: true
    outcome: blocked
    reason: Needs naive single units.
    response: No change.
  - claim: figs4-population-sensitivity-any-reference
    agrees: true
    outcome: blocked
    reason: Needs naive single units.
    response: No change.
  - claim: fig7b-msdt-pairs
    agrees: true
    outcome: blocked
    reason: Pairs carry only preferences and correlations, no tuning curves.
    response: No change.
  - claim: figs5-congruency
    agrees: true
    outcome: blocked
    reason: The congruency index needs each unit's tuning curves. A proxy from the visual-vestibular
      preference difference is possible but is not the paper's measure.
    response: No change.
  - claim: figs6-task-independent
    agrees: true
    outcome: blocked
    reason: No discrimination-task correlations.
    response: No change.
  - claim: figs8ab-eye-movements
    agrees: true
    outcome: blocked
    reason: No eye records.
    response: No change.
E
python tools/entry.py check entries/crcns-stc-1-gu-2011 2>&1 | tail -5; grep -n "def \|subcommand\|choices" tools/entry.py | grep -i -E "check|record|attempt" | head
```

```
error: attempts/crcns-stc-1-gu-2011-01.yaml: not valid YAML: mapping values are not allowed in this context
  in "<unicode string>", line 350, column 26
1 error(s)
78:def dataset_id(record: dict) -> str | None:
143:def check(entry_dir: Path) -> Report:
320:def _derivation_checks(report: Report, where, code: str) -> None:
428:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
```

**Agent calls Bash**

```bash
sed -n 345,352p attempts/crcns-stc-1-gu-2011-01.yaml
```

```
notebook: reproduce_gu_2011.ipynb
  output: claim:fig4dh-lateral-more-sensitive
  notes: On 258 values from 129 units of two trained monkeys, lateral units have lower median
    thresholds than fore-aft ones under every reading, in both conditions. Under one of the 8
    readings of the claims file the difference reaches p < 0.001, as the criterion requires
    ("under one reading"): vector-sum preference, spline threshold, log10, condition as a factor,
    p = 1.9e-07. Per condition that reading gives visual p = 3.4e-07 and vestibular p = 0.040, so
    the per-condition reading fails in the vestibular condition. In the other 7 readings the
```

**Agent calls Bash**

```bash
sed -i 's/    ("under one reading"): vector-sum preference/    ("under one reading"), with vector-sum preference/' attempts/crcns-stc-1-gu-2011-01.yaml && python tools/entry.py check entries/crcns-stc-1-gu-2011 2>&1 | tail -5; python -c "
import yaml,re
d=yaml.safe_load(open('attempts/crcns-stc-1-gu-2011-01.yaml'))
def walk(x):
    if isinstance(x,dict): [walk(v) for v in x.values()]
    elif isinstance(x,list): [walk(v) for v in x]
    elif isinstance(x,str) and ('—' in x or 'rather' in x): print('BAD',x[:80])
walk(d); print(len(d['outcomes']), len(d['verifications'][0]['results']))
from collections import Counter; print(Counter(o['outcome'] for o in d['outcomes']))"; grep -n ": " attempts/crcns-stc-1-gu-2011-01.yaml | grep -v -E "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

```
0 error(s)
35 35
Counter({'blocked': 18, 'reproduced': 11, 'partially_reproduced': 5, 'not_reproduced': 1})
```

**Agent calls Bash**

```bash
grep -n -c -E "—|\brather\b" entries/crcns-stc-1-gu-2011/*; git status --short
```

```
entries/crcns-stc-1-gu-2011/README.md:0
grep: entries/crcns-stc-1-gu-2011/__pycache__: Is a directory
entries/crcns-stc-1-gu-2011/__pycache__:0
entries/crcns-stc-1-gu-2011/entry.yaml:0
entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb:0
entries/crcns-stc-1-gu-2011/requirements.in:0
entries/crcns-stc-1-gu-2011/requirements.lock.txt:0
entries/crcns-stc-1-gu-2011/stc1.py:0
 M attempts/crcns-stc-1-gu-2011-01.yaml
 M entries/crcns-stc-1-gu-2011/README.md
 M entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb
 M entries/crcns-stc-1-gu-2011/stc1.py
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
rm -rf entries/crcns-stc-1-gu-2011/__pycache__; python tools/entry.py check entries/crcns-stc-1-gu-2011 2>&1 | tail -1; date -u
```

```
0 error(s)
Fri Nov  6 18:06:01 UTC 2026
```

**Agent**

I've worked through every point in the round-1 report. Two outcomes changed, and the rest stay as they were. The entry re-ran cleanly with `python tools/entry.py all` (notebook runs in 49 s, 0 check errors), and the conclusions match the new numbers. Nothing is committed.

**Outcomes that changed**
- **fig7c-narrow-preferences: not_reproduced → partially_reproduced**, as the verifier proposed. The proportions match and the improvement grows as the range narrows, but the best improvement is 4.83%, below the paper's 8 ± 0.8%.
- **fig4dh-lateral-more-sensitive: blocked → reproduced, on a subset (problem 2).** I tested it on the 129 units from two trained monkeys, using the claims file's Fisher threshold and its readings. The paper's ANOVA has a training factor, which can't be included because there are no naive units.
  - Lateral units have lower median thresholds under every reading, in both conditions.
  - One of the 8 readings reaches p < 0.001 (p = 1.9e-07), which is what the criterion asks for.
  - The result is fragile, and the notes say so:
    - In that reading, the vestibular condition alone gives p = 0.040.
    - With spline-peak preferences, no reading reaches p < 0.05.
    - Neither monkey shows a significant vestibular difference on its own.

**Corrections and additions**
- **Problem 1:** `pref_vector_sum` now weights each response by the angle it covers. A synthetic check in the notebook shows it recovers preferences to within 3°; the old version put 30° at 16°.
  - fig8ab is still not_reproduced. The weighted vector sum gives p = 0.80, and the opposite-sign result (p = 0.0006) is gone.
  - I added the share of choice probabilities above 0.5 (71.7%) as a check on how they are signed.
- **Problem 3 (fig8cd):** the notebook and notes now state the conflict with the claims file's point-count rule. The outcome stays reproduced, judged on the trained pairs.
- **Problems 4, 6 and 7:**
  - The header's random-numbers statement is corrected.
  - The notebook prints the largest difference in signal correlation between the two simulation readings (5.6e-07).
  - The two behavioural thresholds for fig2a are stated against the 0.9–3.3° plateau range.
- **Items the verifier couldn't check:**
  - fig5-intercept: bootstrap intervals for each group's intercept, which still overlap.
  - fig7a: the point where trained/naive crosses 1, at rsignal = −0.0216.
- **Attempt record:** notes and the affected findings are updated, and round 1 is recorded under `verifications` for all 35 claims (agrees false for fig7c and fig4dh). The README table is updated.

**Not done, and why**
- **Problem 8 (six pairs in one recording):** not explained. The six pairs are all pairs of four units, and nothing in the data set accounts for the paper's maximum of five. It stays a finding.
- **Problem 5:** no change needed; the verifier said it does not affect a conclusion.
- **Questions file:** no questions added, because the verifier reported no place where the claims file misreads the paper.

## End of run

47 turns, 10 minutes, $2.89 at API prices, result: success.
