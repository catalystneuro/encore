# crcns-stc-1 · author-revise-2 · run 42269729626

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-stc-1/verifier-2-report.md; ls entries/crcns-stc-1-gu-2011 entries/crcns-stc-1-gu-2011/*
```

```
Fri Nov  6 18:24:11 UTC 2026
**Verifier report, round 2: Gu et al. (2011) on CRCNS stc-1**

**1. Outcomes**

The claims file has 35 claims and the attempt record has 35 outcomes: 17 tested and 18 blocked.

I agree with all 35 outcomes. Three need comment:

- **fig7c-narrow-preferences, now partially_reproduced.** I agree. This is the change I asked for in round 1.
- **fig4dh-lateral-more-sensitive, now reproduced (it was blocked).** I agree that it meets the criterion as written: lateral thresholds are lower with p < 0.001 under at least one reading. The result is fragile, though, and the record does not say so in full:
  - Only 1 of the 8 claims-file readings passes (cell 57: weighted vector sum, spline, log10, two-factor ANOVA, p = 1.9e-07).
  - In that reading the preference × condition interaction is significant (p = 0.026). Neither the conclusion (cell 58) nor the notes report this.
  - The two-factor ANOVA counts each of the 129 units twice, once per condition.
  - With spline-peak preferences, no reading reaches p < 0.05.
  - See section 3 for a deviation the record leaves out.
- **fig8ab-choice-probability-lateral, not_reproduced.** I agree. It holds under every preference reading, including the corrected vector sum (p = 0.80). It also holds under the distance-from-0.5 variant (p = 0.10 to 0.17), so it does not depend on how the CPs are signed.

There are 11 outcomes marked `assumed: true`. Each assumption is stated and reasonable:

[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; ls attempts 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*crcns-stc-1-gu-2011-01*" -print
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
401:### 4. Lock, check and run
412:### 5. Record the attempt
463:### 6. Hand over for verification
501:## Repeat attempts
543:## Local and remote datasets
566:## Verifier
570:### Round 1: without the author's conclusions
595:### Round 2: with the author's conclusions
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,200p docs/protocol.md; sed -n 400,620p docs/protocol.md
```

````
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


### 4. Lock, check and run

```bash
[... 212 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-stc-1-gu-2011-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-stc-1-gu-2011-01
3	dataset:
4	  archive: crcns
5	  id: stc-1
6	  version: unversioned
7	  doi: 10.6080/K07P8WKF
8	paper: doi:10.1016/j.neuron.2011.06.015
9	date: 2026-11-06
10	entry: crcns-stc-1-gu-2011
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 681 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; cat README.md; cat entry.yaml; wc -l stc1.py; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print('=====',i,c['cell_type'],len(s)); print(s[:300])
"; ls ../../questions/crcns-stc-1.yaml && cat ../../questions/crcns-stc-1.yaml
```

```
Exit code 2
# Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011) from CRCNS stc-1

Tests the findings of [Gu et al. (2011)](https://doi.org/10.1016/j.neuron.2011.06.015) that can be
tested on [CRCNS stc-1](https://doi.org/10.6080/K07P8WKF). The data set holds derived values: the
noise and signal correlations and preferred headings of the paper's 127 MSTd pairs under 1 mm, and
the tuning curves and choice probabilities of 129 single units of two trained monkeys. It holds no
spike times, distances, training-group labels or naive single units.

| Claim | Outcome |
|---|---|
| The monkeys can be assigned to the naive and trained groups by their pair counts | Reproduced |
| Noise correlation is lower in trained than in naive animals (Figure 2B) | Reproduced |
| The difference holds in each animal (means; Figure S2B) | Reproduced |
| The example pair of Figure 1 | Reproduced |
| Visual and vestibular noise correlations are correlated (Figure 1F) | Partially reproduced |
| Visual and vestibular means do not differ (Figure 1F) | Reproduced |
| Noise correlation rises with signal correlation (Figure 5) | Reproduced |
| Training does not change the slope (Figure 5C) | Reproduced |
| Training lowers the intercept, with non-overlapping intervals (Figure 5D) | Partially reproduced |
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions | head -30; ls questions | grep -i stc; ls executed/ 2>/dev/null | head; ls executed/crcns-stc-1-gu-2011 2>/dev/null
```

```
Exit code 2
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
000036.yaml
000037.yaml
000045.yaml
000061.yaml
000115.yaml
000128.yaml
000129.yaml
000139.yaml
000166.yaml
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 201,330p docs/protocol.md | grep -n -A25 "1.6\|6\. " | head -80; cat questions/000010.yaml | head -50; ls claims | grep stc
```

```
89:6. Take from the paper what the claims file does not say. When a claim needs
90-   a method detail the claims file does not give (which trials, which subset,
91-   a window, a threshold, what a measure is compared with), take it from the
92-   paper: the main text, the Methods, the legends, the supplement or the code
93-   it links. Search all of them, and where they disagree, follow the order of
94-   reader, step 2. Record each detail taken as a deviation that quotes or
95-   cites the passage, and cite it too in the notebook or the helper, so that
96-   the verifier can check it. A detail taken this way never changes the
97-   claim's statement, expected values or criterion.
98-   - When the paper allows more than one reading of a detail that could
99-     change the outcome, run every reading, as for the readings a criterion
100-     names (reader, step 3). The outcome is the one they all give.
101-   - When the readings give different outcomes, or the paper does not settle
102-     the detail, you may adopt the choice best supported by the paper, the
103-     methods it cites, the code it links and the field's standard practice.
104-     Record it as an assumption: a deviation that says what was assumed and
105-     why, and `assumed: true` on the outcome. The notebook still shows the
106-     result under every plausible reading, so that the outcome's dependence
107-     on the choice can be seen. The outcome stands, marked as resting on the
108-     assumption.
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-stc-1; grep -n -B2 -A40 "id: fig4dh-lateral-more-sensitive" claims/crcns-stc-1/*.yaml | head -70; grep -n -A40 "id: fig8ab" claims/crcns-stc-1/*.yaml | head -50
```

```
10.1016-j.neuron.2011.06.015.yaml
464-    fig4-tuning-width-visual. The values are read as medians, as for tuning width; means are
465-    shown as a variant. Reproduced when neither test finds a difference.
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
476-    p_relation: "<"
477-    n: 992 visual and 556 vestibular neurons
478-  criterion: Neuronal threshold per neuron from Fisher information on the interpolated tuning
479-    curve at straight ahead (equations 2 and 3 for one neuron), with variance equal to the mean
480-    as equation 4 gives for i = j; how tuning curves are interpolated is not stated (readings,
481-    cubic spline and linear interpolation). Fore-aft is a preference within 45 degrees of 0 or
482-    180, lateral within 45 degrees of -90 or 90 (Results). How the preferred heading is
[... 65 more lines not kept]
```

**Agent**

Now the fig4dh cells in full.

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i in [0,1,3,4,5,6,7,55,57,58,65]:
  c=nb['cells'][i]; print('=====',i,c['cell_type']); print(''.join(c['source']))
"; ls ../../executed/ 2>/dev/null
```

```
Exit code 2
===== 0 markdown
# Reproducing Gu et al. (2011) from CRCNS stc-1

**Paper.** Gu Y, Liu S, Fetsch CR, Yang Y, Fok S, Sunkara A, DeAngelis GC, Angelaki DE (2011).
Perceptual learning reduces interneuronal correlations in macaque visual cortex. *Neuron* 71:750-761.
[doi:10.1016/j.neuron.2011.06.015](https://doi.org/10.1016/j.neuron.2011.06.015). The claims file
was written from the version of record (journal PDF text, with the Experimental Procedures and the
legends of Figures 1 to 8) and the Supplemental Information (legends of Figures S1 to S8).

**Data set.** CRCNS [stc-1](https://doi.org/10.6080/K07P8WKF) (doi:10.6080/K07P8WKF), data
descriptor version 0.6 (5 September 2018), read from the public bucket `crcnsarchive` under
`stc-1/live/`. CRCNS data sets are not versioned, and the paper cites no version, so the version is
recorded as `unversioned` (docs/archives.md, CRCNS). The bucket holds one copy of the data,
`stc-1/live/` (`orig/` holds only an older description document), so `live/` is the version
pinned. The file read, `MSTd.mat`, is checked on loading against its MD5 sum in the data set's
`checksums.md5`, `cd4c13b360aa05689015f1bd2b88a05a`, so a later change makes the notebook fail
(`VIP.mat`, read only to check for overlap, `8d7924e0a1ae86c56b78cd1e2f530e2d`).

**What the data set holds.** Derived values only. For the paper, experiment 3 of `MSTd.mat` holds
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i in [3,4,5,6,7,8,9,10,11,12,57]:
  c=nb['cells'][i]; print('=====',i,c['cell_type']); print(''.join(c['source']))
"
```

```
===== 3 code
published = stc1.checksums()
print("checksums.md5 now lists:", published)
print("MSTd.mat and VIP.mat match the sums pinned in stc1.py:",
      all(published[k] == v for k, v in stc1.MD5.items()))
print("Variables in MSTd.mat:", [k for k in mat if not k.startswith("__")], mat["__header__"].decode())
for e in ("experiment1", "experiment2", "experiment3"):
    x = mat[e]
    print(f"{e}: name {x.name!r}, fields {x._fieldnames}")
q = mat["experiment3"].pairs[0]
print("experiment3.pairs fields:", q._fieldnames, "; per condition:", q.ves._fieldnames)
u1, u2 = mat["experiment1"].units[0], mat["experiment2"].units[0]
print("experiment1.units fields:", u1._fieldnames, u1.ves._fieldnames)
print("experiment2.units fields:", u2._fieldnames, u2.ves._fieldnames, "; com:", u2.com._fieldnames)
print("experiment2.behv.subj:", [(s.monk_id, s.ves.thresh._fieldnames) for s in mat["experiment2"].behv.subj])
===== 4 code
pairs = stc1.pairs_table(mat)
print("Pairs in experiment3:", len(pairs), "(data descriptor: 127 MSTd pairs; paper: 127 pairs under 1 mm)")
print("Missing values:", int(pairs.isna().sum().sum()))
cols = ["rsig_ves", "rsig_vis", "rnoise_ves", "rnoise_vis", "pref1_ves", "pref2_ves", "pref1_vis", "pref2_vis"]
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; grep -n "def \|CACHE\|cache" stc1.py | head -50; time python -c "
import stc1
mat=stc1.load_mat('MSTd.mat')
u=mat['experiment1'].units[0]; print(u._fieldnames, u.ves._fieldnames)
for f in u.ves._fieldnames: print(f, getattr(u.ves,f))
u=mat['experiment2'].units[0]; print(u._fieldnames, u.ves._fieldnames)
for f in u.ves._fieldnames: print(f, getattr(u.ves,f))
"
```

```
Exit code 1
82:def read_bytes(name: str) -> bytes:
92:def checksums() -> dict[str, str]:
98:def load_mat(name: str = "MSTd.mat"):
102:def monkey_of(file_id: str) -> int:
106:def pairs_table(mat) -> pd.DataFrame:
120:def assign_groups(counts: pd.Series) -> dict[int, str]:
130:def pooled_rnoise(df: pd.DataFrame) -> pd.Series:
135:def neurons_per_recording(df: pd.DataFrame) -> pd.Series:
147:def unit_table(df: pd.DataFrame) -> pd.DataFrame:
158:def wrap180(a):
162:def preference_group(pref):
169:def _sorted_circle(headings, resp):
177:def pref_vector_sum(headings, resp) -> float:
186:def pref_spline_peak(headings, resp) -> float:
193:def neuron_threshold(headings, resp, interp: str = "spline") -> float:
211:def tls_plane(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float]:
232:def _wrapped_gaussian(theta, pref, sigma):
238:def sigma_for_fwhm(fwhm: float) -> float:
240:    def half(s):
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* envs 2>/dev/null | head; grep -n "venv\|env" tools/entry.py | head -30
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -15
```

```
Installed kernelspec registry-crcns-stc-1-gu-2011 in executed/crcns-stc-1-gu-2011/.venv/share/jupyter/kernels/registry-crcns-stc-1-gu-2011
0 error(s)
pass  reproduce_gu_2011.ipynb  (57 s)

real	1m4.610s
user	2m43.010s
sys	0m4.499s
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; P=../../executed/crcns-stc-1-gu-2011/.venv/bin/python; $P -c "
import stc1
mat=stc1.load_mat('MSTd.mat')
u=mat['experiment1'].units[0]; print(u._fieldnames, u.ves._fieldnames)
for f in u.ves._fieldnames: print(f, getattr(u.ves,f))
u=mat['experiment2'].units[0]; print(u._fieldnames, u.ves._fieldnames)
for f in u.ves._fieldnames: print(f, getattr(u.ves,f))
print(u.com._fieldnames)
"; sed -n 160,215p stc1.py
```

```
['file_id', 'ves', 'vis'] ['stim_global', 'resp_global']
stim_global [ 135.    90.    45.    22.5    0.   -22.5  -45.   -90.  -135.  -180. ]
resp_global [18.15920398 16.41791045 14.05472637 14.55223881 12.93532338 13.93034826
 19.90049751 27.46268657 31.46766169 25.37313433]
['file_id', 'ves', 'vis', 'com'] ['stim_local', 'resp_local', 'cp', 'thresh']
stim_local [ 9.    3.46  1.33  0.51  0.   -0.51 -1.33 -3.46 -9.  ]
resp_local [14.28217822 14.48019802 16.70792079 15.99009901 16.75742574 18.0874185
 17.84593093 19.75247525 21.00941801]
cp 0.581
thresh 9.07
['stim_local', 'resp_local', 'cp', 'thresh']


def preference_group(pref):
    """'fore-aft' within 45 degrees of 0 or 180, else 'lateral'."""
    d = np.abs(wrap180(pref))
    fore_aft = (d < 45) | (d > 135)
    return np.where(fore_aft, "fore-aft", "lateral")


[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rn -i "repetition\|ANOVA\|repeated" paper/ | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 825,845p paper/*2011.06.015.txt; sed -n 160,172p paper/*2011.06.015.txt; sed -n 345,355p paper/*2011.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "fano" paper/*2011.06.015.txt | head; grep -n -i "middle 1\|1 s\b" paper/*2011.06.015.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; P=../../executed/crcns-stc-1-gu-2011/.venv/bin/python; cat > $TMPDIR/proto.py <<'EOF'
import numpy as np, pandas as pd, statsmodels.api as sm, statsmodels.formula.api as smf
from scipy import stats
import stc1
mat=stc1.load_mat('MSTd.mat')
H1 = mat["experiment1"].units[0].ves.stim_global
rows=[]
for u1 in mat["experiment1"].units:
    for cond in ("ves","vis"):
        c1=getattr(u1,cond); r=np.asarray(c1.resp_global,float)
        k=len(r)
        def pval(n,fano):
            F = n*((r-r.mean())**2).sum()/(k-1)/(fano*r.mean())
            return stats.f.sf(F,k-1,k*(n-1))
        rows.append({"cell":u1.file_id,"condition":cond,
          "pref_vector_sum":stc1.pref_vector_sum(c1.stim_global,r),
          "pref_spline_peak":stc1.pref_spline_peak(c1.stim_global,r),
          "thr_spline":stc1.neuron_threshold(c1.stim_global,r,"spline"),
          "thr_linear":stc1.neuron_threshold(c1.stim_global,r,"linear"),
          "p5_1":pval(5,1),"p3_2":pval(3,2)})
s=pd.DataFrame(rows).replace(np.inf,np.nan)
print((s.p5_1<0.05).sum(),(s.p3_2<0.05).sum(), len(s))
print(s.groupby('condition')[['p5_1','p3_2']].apply(lambda d:(d<0.05).sum()))
for sel in ("all","p5_1","p3_2"):
  for pref in ("pref_vector_sum","pref_spline_peak"):
    for thr in ("thr_spline","thr_linear"):
      for scale in ("raw","log10"):
        d=s.dropna(subset=[thr]).copy()
        if sel!="all": d=d[d[sel]<0.05]
        d["pgroup"]=stc1.preference_group(d[pref])
        d["y"]=d[thr] if scale=="raw" else np.log10(d[thr])
        a2=sm.stats.anova_lm(smf.ols("y ~ C(pgroup) * C(condition)",d).fit(),typ=2)
        pv=[sm.stats.anova_lm(smf.ols("y ~ C(pgroup)",d[d.condition==c]).fit(),typ=2).loc["C(pgroup)","PR(>F)"] for c in ("ves","vis")]
        mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
        pm=mm.pvalues["C(pgroup)[T.lateral]"]
        print(sel,pref[5:],thr,scale,len(d),f"{a2.loc['C(pgroup)','PR(>F)']:.2g} int {a2.loc['C(pgroup):C(condition)','PR(>F)']:.2g} ves {pv[0]:.2g} vis {pv[1]:.2g} mixed {pm:.2g} coef {mm.params['C(pgroup)[T.lateral]']:.3g}")
EOF
$P $TMPDIR/proto.py 2>&1 | grep -v Warning
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 3, in <module>
    import stc1
ModuleNotFoundError: No module named 'stc1'
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; PYTHONPATH=. ../../executed/crcns-stc-1-gu-2011/.venv/bin/python $TMPDIR/proto.py 2>&1 | grep -v -i Warning
```

```
mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
  mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
  mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
  mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
  mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
  mm=smf.mixedlm("y ~ C(pgroup) + C(condition)",d,groups=d["cell"]).fit()
252 169 258
           p5_1  p3_2
condition            
ves         124    67
vis         128   102
all vector_sum thr_spline raw 258 0.35 int 0.23 ves 0.86 vis 0.006 mixed 0.46 coef -19.8
all vector_sum thr_spline log10 258 1.9e-07 int 0.026 ves 0.04 vis 3.4e-07 mixed 2.7e-07 coef -0.311
all vector_sum thr_linear raw 256 0.51 int 0.19 ves 0.48 vis 0.26 mixed 0.51 coef -6.39e+14
all vector_sum thr_linear log10 256 0.013 int 0.078 ves 0.64 vis 0.0033 mixed 0.013 coef -0.46
all spline_peak thr_spline raw 258 0.66 int 0.43 ves 0.5 vis 0.65 mixed 0.72 coef 9.59
all spline_peak thr_spline log10 258 0.26 int 0.16 ves 0.84 vis 0.085 mixed 0.49 coef -0.0449
all spline_peak thr_linear raw 256 0.77 int 0.28 ves 0.43 vis 0.43 mixed 0.77 coef -2.81e+14
all spline_peak thr_linear log10 256 0.38 int 0.12 ves 0.63 vis 0.094 mixed 0.38 coef -0.163
p5_1 vector_sum thr_spline raw 252 0.37 int 0.22 ves 0.84 vis 0.0062 mixed 0.49 coef -18.9
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; PYTHONPATH=. ../../executed/crcns-stc-1-gu-2011/.venv/bin/python -W always $TMPDIR/proto.py 2>&1 | grep -i Warning | sort | uniq -c
```

```
6 /tmp/claude-1001/proto.py:33: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; PYTHONPATH=. ../../executed/crcns-stc-1-gu-2011/.venv/bin/python -c "
import stc1
mat=stc1.load_mat('MSTd.mat'); p=stc1.pairs_table(mat)
print(p.file_id.head().tolist())
s=p[p.file_id.str.endswith('s')]; print(len(s), s.monkey.value_counts().to_dict(), s.file_id.unique().tolist())
cells={u.file_id.split('r')[0] for u in mat['experiment1'].units}
print(list(cells)[:5])
sh=p[p.file_id.str.split('r').str[0].isin(cells)]; print(len(sh), sh.file_id.nunique(), sh.file_id.unique().tolist())
"; grep -rn "end in\|'s'\|share a cell" ../../executed/crcns-stc-1-gu-2011/*.ipynb | head
```

```
['m17c26r1', 'm17c28r1', 'm17c29r1', 'm17c30r1', 'm17c31r3']
10 {17: 10} ['m17c36r1s', 'm17c40r1s', 'm17c41r1s', 'm17c42r1s', 'm17c44r1s', 'm17c48r1s']
['m2c443', 'm5c87', 'm5c46', 'm2c195', 'm5c8']
7 7 ['m2c170r1', 'm2c183r1', 'm2c193r1', 'm2c370r1', 'm2c417r1', 'm5c109r1', 'm5c167r1']
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
print(''.join(nb['cells'][55]['source']))
print(nb['cells'][57].keys(), nb['nbformat'], nb['nbformat_minor'])
print(nb['cells'][57].get('id'))
"
```

```
## fig4dh-lateral-more-sensitive

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
straight ahead), and the vector sum over the 8 evenly spaced headings alone. First, a check of the two preference readings on synthetic tuning curves
sampled at the experiment 1 headings.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
for i in [6,7,55,56,57,58,63,64,65]: print(i, nb['cells'][i]['id'], nb['cells'][i]['metadata'])
"
```

```
6 67966e03 {'tags': ['sanity']}
7 f5ad2791 {}
55 fig4dh-0 {}
56 fig4dh-1 {'tags': ['claim:fig4dh-lateral-more-sensitive']}
57 fig4dh-2 {'tags': ['claim:fig4dh-lateral-more-sensitive']}
58 fig4dh-3 {}
63 91cd6d1b {'tags': ['claim:fig8cd-noise-not-preference']}
64 4a2eb047 {}
65 975b4b25 {}
```

**Agent**

Now the helper change (window parameter) and the notebook edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-stc-1-gu-2011/stc1.py",
 "old_string": "def neuron_threshold(headings, resp, interp: str = \"spline\") -> float:\n    \"\"\"Threshold (degrees) of one neuron at straight ahead, equations 2 and 3 with variance = mean.\n\n    interp \"spline\" (periodic cubic spline) or \"linear\" (slope between the neighbours of 0).\n    Infinite when the curve is flat at 0.\n    \"\"\"",
 "new_string": "def neuron_threshold(headings, resp, interp: str = \"spline\", window: float = 1.0) -> float:\n    \"\"\"Threshold (degrees) of one neuron at straight ahead, equations 2 and 3 with variance = mean.\n\n    interp \"spline\" (periodic cubic spline) or \"linear\" (slope between the neighbours of 0).\n    resp in spikes/s, counted over `window` seconds. Infinite when the curve is flat at 0.\n    \"\"\"\n    resp = np.asarray(resp, float) * window"
}
```

```
The file entries/crcns-stc-1-gu-2011/stc1.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; cat > $TMPDIR/edit1.py <<'EOF'
import json
nb = json.load(open("reproduce_gu_2011.ipynb"))
cells = nb["cells"]
def src(i): return "".join(cells[i]["source"])
def setsrc(i, s): cells[i]["source"] = s.splitlines(keepends=True)
def code(cid, s, tags):
    return {"cell_type": "code", "execution_count": None, "id": cid, "metadata": {"tags": tags} if tags else {},
            "outputs": [], "source": s.splitlines(keepends=True)}
def md(cid, s):
    return {"cell_type": "markdown", "id": cid, "metadata": {}, "source": s.splitlines(keepends=True)}

# cell 6: print the 's' file_ids and the cell ids shared with experiment 1
s = src(6)
s += '''
s_ids = pairs[pairs.file_id.str.endswith("s")]
print("\\nPairs whose file_id ends in 's':", len(s_ids), "; monkeys", s_ids.monkey.value_counts().to_dict(),
      "; recordings", s_ids.file_id.unique().tolist())
cells1 = {u.file_id.split("r")[0] for u in mat["experiment1"].units}
shared = pairs[pairs.file_id.str.split("r").str[0].isin(cells1)]
print("Pairs whose recording shares a cell id (before 'r') with an experiment 1 unit:", len(shared),
      "in", shared.file_id.nunique(), "recordings", shared.file_id.unique().tolist())
'''
setsrc(6, s)
s = src(7).rstrip("\n")
s += ''' Ten pairs of monkey 17, in six recordings, have
`file_id`s ending in "s", which the data descriptor does not explain. Seven pairs, each in its
own recording, share a cell id with an experiment 1 unit; the data set does not say which pair
unit, if any, that unit is.
'''
setsrc(7, s)

# fig4dh description: say the significance selection is not applied in the main readings
s = src(55).rstrip("\n")
s += '''

The Figure 4 legend includes "only neurons with significant heading tuning (p < 0.05, ANOVA)".
The data set holds trial-averaged curves only, so that selection cannot be applied, and the
readings above include every unit. After the main table, two checks of how much the outcome
depends on this and on each unit entering twice: a proxy of the selection, a one-way ANOVA
computed from the mean curve with variance equal to the mean (equation 4) and the Experimental
Procedures' "typically repeated five times (minimum of three repetitions for inclusion)"
(Experimental Protocol and Task), over the middle 1 s; and a mixed model with a random intercept
per unit in place of the two-factor ANOVA, which counts each unit once per condition.
'''
setsrc(55, s)

new = code("fig4dh-4", '''# Selection proxy: one-way ANOVA F from the mean curve, with n repetitions and variance = Fano x mean
# (counts over 1 s). n = 5, Fano 1 is the paper's typical protocol with equation 4's variance; n = 3,
# Fano 2 a stricter selection (the paper's minimum repetitions and a variance twice the mean).
def tuning_p(resp, n, fano):
    r = np.asarray(resp, float)
    k = len(r)
    F = n * ((r - r.mean()) ** 2).sum() / (k - 1) / (fano * r.mean())
    return stats.f.sf(F, k - 1, k * (n - 1))

units1 = {u.file_id: u for u in mat["experiment1"].units}
for n, fano in ((5, 1), (3, 2)):
    sens[f"tuned_n{n}_fano{fano}"] = [tuning_p(getattr(units1[c], cond).resp_global, n, fano) < 0.05
                                      for c, cond in zip(sens.cell, sens.condition)]
print("Values kept by the selection proxy (of 258):",
      {c: int(sens[c].sum()) for c in ("tuned_n5_fano1", "tuned_n3_fano2")},
      "; per condition:", sens.groupby("condition")[["tuned_n5_fano1", "tuned_n3_fano2"]].sum().to_dict())
res = []
for sel in ("all", "tuned_n5_fano1", "tuned_n3_fano2"):
    for pref in ("pref_vector_sum", "pref_spline_peak"):
        for thr in ("thr_spline", "thr_linear"):
            for scale in ("raw", "log10"):
                d = sens.dropna(subset=[thr]).copy()
                if sel != "all":
                    d = d[d[sel]]
                d["pgroup"] = stc1.preference_group(d[pref])
                d["y"] = d[thr] if scale == "raw" else np.log10(d[thr])
                a2 = sm.stats.anova_lm(smf.ols("y ~ C(pgroup) * C(condition)", d).fit(), typ=2)
                pc = {c: sm.stats.anova_lm(smf.ols("y ~ C(pgroup)", d[d.condition == c]).fit(), typ=2).loc["C(pgroup)", "PR(>F)"]
                      for c in ("ves", "vis")}
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    mm = smf.mixedlm("y ~ C(pgroup) + C(condition)", d, groups=d["cell"]).fit()
                res.append({"selection": sel, "preference": pref, "threshold": thr, "scale": scale, "n": len(d),
                            "two_factor_p_group": a2.loc["C(pgroup)", "PR(>F)"],
                            "two_factor_p_interaction": a2.loc["C(pgroup):C(condition)", "PR(>F)"],
                            "ves_p": pc["ves"], "vis_p": pc["vis"],
                            "mixed_p_group": mm.pvalues["C(pgroup)[T.lateral]"],
                            "mixed_lateral_minus_fa": mm.params["C(pgroup)[T.lateral]"],
                            "mixed_unit_var": float(mm.cov_re.iloc[0, 0])})
checks = pd.DataFrame(res)
print(checks.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("\\nReadings with the two-factor or the mixed-model p < 0.001 (lateral lower):")
print(checks[((checks.two_factor_p_group < 0.001) | (checks.mixed_p_group < 0.001)) & (checks.mixed_lateral_minus_fa < 0)]
      [["selection", "preference", "threshold", "scale", "n", "two_factor_p_group", "two_factor_p_interaction", "mixed_p_group"]]
      .to_string(index=False, float_format=lambda x: f"{x:.3g}"))

# Counting window: equation 3's first term scales with the window, its trace term does not.
sens["pgroup"] = stc1.preference_group(sens.pref_vector_sum)
print("\\nCounting window, vector-sum preference, spline threshold, log10, two-factor p of preference group:")
for w in (0.5, 1.0, 2.0):
    d = sens.copy()
    d["y"] = np.log10([stc1.neuron_threshold(getattr(units1[c], cond).stim_global, getattr(units1[c], cond).resp_global,
                                             "spline", window=w) for c, cond in zip(d.cell, d.condition)])
    a2 = sm.stats.anova_lm(smf.ols("y ~ C(pgroup) * C(condition)", d).fit(), typ=2)
    print(f"  {w} s: median threshold fore-aft {10 ** d.y[d.pgroup == 'fore-aft'].median():.2f}, lateral "
          f"{10 ** d.y[d.pgroup == 'lateral'].median():.2f} deg, p = {a2.loc['C(pgroup)', 'PR(>F)']:.3g}")
''', ["claim:fig4dh-lateral-more-sensitive"])
cells.insert(58, new)

# elapsed time, before the summary (index shifts by one)
i_sum = next(i for i, c in enumerate(cells) if "".join(c["source"]).startswith("## Summary"))
cells.insert(i_sum, code("runtime", 'print(f"Notebook run time from the first cell: {time.time() - started:.0f} s")\n', []))
json.dump(nb, open("reproduce_gu_2011.ipynb", "w"), indent=1, ensure_ascii=False)
open("reproduce_gu_2011.ipynb", "a").write("\n")
EOF
python $TMPDIR/edit1.py; git diff --stat
```

```
.../crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb    | 104 ++++++++++++++++++++-
 entries/crcns-stc-1-gu-2011/stc1.py                |   5 +-
 2 files changed, 104 insertions(+), 5 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb | tail -5; python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -4; date -u
```

```
+   ]
+  },
   {
    "cell_type": "markdown",
    "id": "975b4b25",
Installed kernelspec registry-crcns-stc-1-gu-2011 in executed/crcns-stc-1-gu-2011/.venv/share/jupyter/kernels/registry-crcns-stc-1-gu-2011
0 error(s)
pass  reproduce_gu_2011.ipynb  (58 s)
Fri Nov  6 18:29:02 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for c in nb['cells']:
  if c['id'] in ('67966e03','fig4dh-2','fig4dh-4','runtime'):
    print('=====',c['id'])
    for o in c['outputs']: print(''.join(o.get('text','')) or o)
"
```

```
===== 67966e03
Recordings by (pairs, units): {(1, 2): 85, (3, 3): 12, (6, 4): 1}
Every recording with k units has k(k-1)/2 pairs: True
Distinct units over the 127 pairs: 210
Largest number of pairs in one recording: 6 ['m19c21r1'] ; paper: 'maximum of 5 pairs in an experiment' (Experimental Procedures)

Pairs with identical correlations (deposited twice): 0
VIP pairs: 139 ; recordings shared with MSTd: 0 ; noise-correlation pairs shared: 0

Pairs whose file_id ends in 's': 10 ; monkeys {17: 10} ; recordings ['m17c36r1s', 'm17c40r1s', 'm17c41r1s', 'm17c42r1s', 'm17c44r1s', 'm17c48r1s']
Pairs whose recording shares a cell id (before 'r') with an experiment 1 unit: 7 in 7 recordings ['m2c170r1', 'm2c183r1', 'm2c193r1', 'm2c370r1', 'm2c417r1', 'm5c109r1', 'm5c167r1']

===== fig4dh-2
Values: 258 ; infinite thresholds left out: {'thr_spline': 0, 'thr_linear': 2, 'variant_thr_experiment2': 0}
Threshold ranges (degrees):
       thr_spline    thr_linear  variant_thr_experiment2
count      258.00  2.560000e+02                   258.00
min          2.65  3.080000e+00                     1.51
50%         31.10  4.168000e+01                    17.84
max       2759.96  1.040646e+17                   300.00
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; cat > $TMPDIR/edit2.py <<'EOF'
import json
nb = json.load(open("reproduce_gu_2011.ipynb"))
cells = {c["id"]: c for c in nb["cells"]}
def get(cid): return "".join(cells[cid]["source"])
def put(cid, s): cells[cid]["source"] = s.splitlines(keepends=True)

s = get("fig4dh-3")
old = """vestibular one in neither (p = 0.082 and 0.185). The linear reading leaves out 2 values whose curve
is flat at 0."""
assert old in s
s = s.replace(old, """vestibular one in neither (p = 0.082 and 0.185). The linear reading leaves out 2 values whose curve
is flat at 0.

The outcome rests on that one reading, and three things about it bear on how firmly. In it the
preference by condition interaction is significant (p = 0.026): the difference is larger in the
visual condition. The two-factor ANOVA counts each unit twice, once per condition; a mixed model
with a random intercept per unit gives p = 2.7e-07 for the preference group in the same reading,
and does not change which readings pass. The paper includes only units with significant tuning,
which cannot be applied to trial-averaged curves; with the proxy selection (n = 5 repetitions,
variance equal to the mean) 252 of 258 values are kept and the reading gives p = 1.2e-07, and with
the stricter proxy (n = 3, variance twice the mean) 169 are kept and it gives p = 9.6e-08. Under
both selections the other readings still do not reach p < 0.001 (smallest 0.012), and with
spline-peak preferences the smallest is 0.051. A counting window of 0.5 s or 2 s in place of
1 s does not scale the thresholds exactly alike, as the trace term of equation 3 does not
scale with the window, but the p value stays at 1.9e-07.""")
put("fig4dh-3", s)

s = get("975b4b25")
old = """not the pooled one, so the pooled value is taken as their mean. Under that reading the
main result matches the paper to the third decimal."""
assert old in s
s = s.replace(old, """not the pooled one, so the pooled value is taken as their mean. Under that reading the
group means of the main result (0.0241 and 0.1190) lie within the SEMs of the paper's 0.023 and
0.116, and the t test gives p = 0.0056 against the paper's 0.006. Seven of the 17 tested outcomes
rest on this assumption.""")
old = """The simulations use a tuning amplitude and baseline that the paper does not give, and the
threshold ratios depend on them."""
assert old in s
s = s.replace(old, """The simulations use a tuning amplitude and baseline that the paper does not give, and the
threshold ratios depend on them; four outcomes rest on this assumption.""")
old = """so the preference-group test of Figure 4 runs without the
training factor."""
assert old in s
s = s.replace(old, """so the preference-group test of Figure 4 runs without the
training factor and without the paper's selection of significantly tuned units, which needs trial
responses. Its outcome rests on one of the claims file's 8 readings.""")
old = """The data descriptor lists seven monkeys for the MSTd pairs. The files name eight,
including monkey 24 with two pairs."""
assert old in s
s = s.replace(old, """The data descriptor lists seven monkeys for the MSTd pairs. The files name eight,
including monkey 24 with two pairs. Ten pairs of monkey 17, in six recordings, have `file_id`s
ending in "s", which the descriptor does not explain.""")
put("975b4b25", s)
json.dump(nb, open("reproduce_gu_2011.ipynb", "w"), indent=1, ensure_ascii=False)
open("reproduce_gu_2011.ipynb", "a").write("\n")
EOF
python $TMPDIR/edit2.py && git diff --stat
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/edit2.py", line 31, in <module>
    assert old in s
           ^^^^^^^^
AssertionError
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python -c "
import json;nb=json.load(open('reproduce_gu_2011.ipynb'))
c=[c for c in nb['cells'] if c['id']=='975b4b25'][0]; print(c['source'][-25:])"
```

```
['| fig7b-msdt-pairs, figs5-congruency | blocked, data missing (no tuning curves of the pair units) |\n', '| figs6-task-independent | blocked, data missing |\n', '| figs8ab-eye-movements | blocked, data missing |\n', '\n', 'A failure to reproduce here may be a failure of this attempt, not of the paper: see the\n', "reasoning and the differences from the paper's method.\n", '\n', "How the analysis differs from the paper's. The data set holds per-condition noise correlations,\n", 'not the pooled one, so the pooled value is taken as the mean of the two. Under that reading the\n', "main result matches the paper to the third decimal. Training groups come from the paper's\n", 'per-animal pair counts. Only the 127 pairs under 1 mm are available, where Figure 1F uses 179.\n', 'The simulations use a tuning amplitude and baseline that the paper does not give, and the\n', 'threshold ratios depend on them. Single-unit thresholds and choice probabilities come from 129 units\n', "of two trained monkeys, not the paper's database of naive and trained animals (992 and 556\n", 'neurons, 311 choice probabilities), so the preference-group test of Figure 4 runs without the\n', 'training factor.\n', '\n', 'What was found about the data set. It holds derived values only: no spike times, trial\n', 'responses, distances, electrode labels or training-group labels, and none of the 52 pairs over\n', '1 mm. The data descriptor lists seven monkeys for the MSTd pairs. The files name eight,\n', 'including monkey 24 with two pairs. One recording (m19c21r1) has six pairs from four units,\n', 'where the paper states a maximum of five pairs per experiment. How the preferred headings\n', 'were computed is not described. The pairs are internally consistent (units per recording,\n', "rsignal against the preference difference) and match the paper's group counts of pairs and\n", 'units.']
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python - <<'EOF'
import re,os
p=os.path.expandvars("$TMPDIR/edit2.py"); s=open(p).read()
s=s.replace('''not the pooled one, so the pooled value is taken as their mean. Under that reading the
main result matches the paper to the third decimal."""''','''not the pooled one, so the pooled value is taken as the mean of the two. Under that reading the
main result matches the paper to the third decimal."""''')
s=s.replace('''not the pooled one, so the pooled value is taken as their mean. Under that reading the
group means''','''not the pooled one, so the pooled value is taken as the mean of the two. Under that reading the
group means''')
s=s.replace('''including monkey 24 with two pairs."""
assert''','''including monkey 24 with two pairs. One recording"""
assert''')
s=s.replace('''ending in "s", which the descriptor does not explain.""")''','''ending in "s", which the descriptor does not explain. One recording""")''')
open(p,"w").write(s)
EOF
python $TMPDIR/edit2.py && git diff --stat
```

```
.../crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb    | 131 +++++++++++++++++++--
 entries/crcns-stc-1-gu-2011/stc1.py                |   5 +-
 2 files changed, 126 insertions(+), 10 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python - <<'EOF'
import json
nb=json.load(open("reproduce_gu_2011.ipynb"))
c=[c for c in nb["cells"] if c["id"]=="fig4dh-3"][0]
s="".join(c["source"])
old="spline-peak preferences the smallest is 0.051."
assert old in s
s=s.replace(old,"spline-peak preferences the smallest two-factor p is 0.051.")
c["source"]=s.splitlines(keepends=True)
json.dump(nb, open("reproduce_gu_2011.ipynb", "w"), indent=1, ensure_ascii=False)
open("reproduce_gu_2011.ipynb", "a").write("\n")
EOF
grep -n "spline-peak preferences the smallest" reproduce_gu_2011.ipynb
```

```
1425:    "spline-peak preferences the smallest two-factor p is 0.051. A counting window of 0.5 s or 2 s in place of\n",
```

**Agent calls Bash**

```bash
cd entries/crcns-stc-1-gu-2011; python - <<'EOF'
s=open("README.md").read()
old="""Most outcomes rest on one assumption: the data set holds per-condition noise correlations, and the
paper's pooled value is taken as their mean. Under it the main result matches the paper to the third
decimal. The simulations use a tuning amplitude and baseline that the paper does not give. The
attempt record"""
new="""Seven of the 17 tested outcomes rest on one assumption: the data set holds per-condition noise
correlations, and the paper's pooled value is taken as their mean. Under it the group means of the
main result (0.0241 and 0.1190) lie within the SEMs of the paper's 0.023 and 0.116. Four outcomes
rest on another: the simulations use a tuning amplitude and baseline that the paper does not give.
The Figure 4 test of lateral against fore-aft sensitivity passes under one of the claims file's 8
readings and runs without the paper's selection of significantly tuned units. The attempt record"""
assert old in s; s=s.replace(old,new)
old="It takes about two minutes."
assert old in s; s=s.replace(old,"It runs in about one minute.")
open("README.md","w").write(s)
e=open("entry.yaml").read(); assert "runtime_minutes: 2" in e
open("entry.yaml","w").write(e.replace("runtime_minutes: 2","runtime_minutes: 1"))
EOF
cd ../..; python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -3
```

```
Installed kernelspec registry-crcns-stc-1-gu-2011 in executed/crcns-stc-1-gu-2011/.venv/share/jupyter/kernels/registry-crcns-stc-1-gu-2011
0 error(s)
pass  reproduce_gu_2011.ipynb  (58 s)
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code':
    t=''.join(''.join(o.get('text','')) for o in c['outputs'])
    for k in ['0.0241','run time','1.17e-07','9.57e-08','2.68e-07','1.91e-07']:
      if k in t: print(c['id'],k)
"
```

```
72864bcc 0.0241
3eb9208b 0.0241
fd1c8763 1.17e-07
fig4dh-2 1.91e-07
fig4dh-4 1.17e-07
fig4dh-4 9.57e-08
fig4dh-4 2.68e-07
fig4dh-4 1.91e-07
runtime run time
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n "question" tools/entry.py | head; python -c "
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
print([o.get('text') for c in nb['cells'] if c['id']=='runtime' for o in c['outputs']])"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
[['Notebook run time from the first cell: 51 s\n']]
```

**Agent calls Bash**

```bash
cd  cat schemas/questions.schema.json | head -60; grep -n "## Verifications\|verifications" -A3 schemas/attempt.schema.json | head -60
```

```
cat: schemas/questions.schema.json: No such file or directory
334:    "verifications": {
335-      "type": "array",
336-      "items": {
337-        "type": "object",
```

**Agent calls Bash**

```bash
cd  sed -n 334,420p schemas/attempt.schema.json; grep -n "proposed" -A20 schemas/attempt.schema.json | head -30
```

```
"verifications": {
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
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "questions" tools/*.py | head -15; ls questions | grep -v "^0" | head
```

```
tools/build_site.py:322:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
tools/build_site.py:325:    checks, questions, items = {}, {}, {}
tools/build_site.py:330:    for path in sorted((ROOT / "questions").glob("*.yaml")):
tools/build_site.py:332:        q = q.get("questions", []) if isinstance(q, dict) else q
tools/build_site.py:333:        questions[key_of_dir(path.stem)] = sum(1 for x in q if not x.get("answered"))
tools/build_site.py:335:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
tools/build_site.py:516:                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]
tools/build_site.py:557:    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
tools/build_site.py:571:        open_q = inputs["questions"].get(d, 0)
tools/build_site.py:590:            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
tools/build_site.py:1227:CHART_STEPS = [(k, label) for k, label in PIPELINE_STEPS if k != "questions"]
tools/build_site.py:1391:  check, the attempt, the questions it raised, and verification. {len(waiting):,} targets are waiting on a person,
tools/build_site.py:1686:    questions = (data.get("pipeline") or {}).get("question_items", {}).get(dandiset, [])
tools/build_site.py:1688:    for i, q in enumerate(questions, 1):
tools/build_site.py:1876:    for i, q in enumerate(questions, 1):
README.md
crcns-ac-2.yaml
crcns-hc-16.yaml
crcns-ofc-4.yaml
crcns-ret-1.yaml
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -30 questions/crcns-hc-16.yaml; sed -n 1,40p questions/README.md
```

```
questions:
- claim: overdispersion-passes
  asked: 2026-11-05
  question: >-
    The claims file reads the pass rule literally, a 5 s interval is a pass when exp, the
    expected spike count in the interval, is at least the cell's average rate in AP/s. Is the
    threshold meant as the count expected at the average rate over the interval (exp at least
    the average rate x 5 s), so that a pass is an interval in which the expected firing is at
    least the cell's average? The same rule selects the joint passes of
    fig4b-covariance-30-passes and fig4b-covariance-40-passes, and the passes of
    overdispersion-cells.
  passage: >-
    Only 5 s intervals when the mouse sampled a cell's firing field well were studied. These
    were identified by exp >= average rate for the cell (Fenton et al., 2010). To study
    discharge covariations between pairs of cells, we selected 5 s epochs when the mouse crossed
    the firing fields of both cells as epochs when expected spatial firing (exp) of each cell
    was above the individual cell's average rate. (STAR Methods, Overdispersion; the extracted
    text prints the sign as "R")
  why: >-
    The literal rule compares a count with a rate. Here it passes a median 76% of a cell's 5 s
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A6 "deviated away" paper/*2011.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('executed/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
for c in nb['cells']:
  if 'claim:fig8ab-choice-probability-lateral' in c['metadata'].get('tags',[]):
    for o in c['outputs']: print(''.join(o.get('text','')))
"
```

```
Values: 258 from 129 units; per monkey and condition: {(2, 'ves'): 72, (2, 'vis'): 72, (5, 'ves'): 57, (5, 'vis'): 57}
CP range 0.256 to 0.793 ; missing 0 ; share above 0.5 0.717 ; mean 0.5343
Agreement of the readings' groups: vector sum and spline peak 0.717 ; weighted vector sum over all 10 and vector sum over the 8 evenly spaced headings 0.977
                                    0                 1                  2
preference            pref_vector_sum  pref_spline_peak  pref_vector_sum_8
n_fore_aft                        101               130                 99
cp_fore_aft                    0.5326            0.5269             0.5317
n_lateral                         157               128                159
cp_lateral                     0.5353            0.5418             0.5358
p_fa_vs_lat                    0.7955            0.1363             0.6911
p_fa_vs_lat_welch              0.7881            0.1365             0.6799
cp_left_all                    0.5401            0.5389             0.5398
cp_right_all                   0.5285            0.5295             0.5288
n_left_all                        128               132                129
n_right_all                       130               126                129
p_left_right_all               0.2503            0.3492             0.2735
cp_left_lateral                 0.543            0.5506             0.5423
cp_right_lateral               0.5283            0.5342             0.5296
p_left_right_lateral           0.2835            0.2657             0.3504
variant_dev_fore_aft            0.063            0.0632             0.0624
[... 8 more lines not kept]
```

**Agent**

Writing the questions file.

**Agent calls Write**

```json
{
 "file_path": "questions/crcns-stc-1.yaml",
 "content": "# Questions from attempt crcns-stc-1-gu-2011-01 (author, 2026-11-06) about the claims file\n# claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml. Each was raised by the round-2 verifier\n# and is asked under docs/protocol.md, \"Hand over for verification\"; the claims are tested as\n# written.\nquestions:\n- claim: fig4dh-lateral-more-sensitive\n  asked: 2026-11-06\n  question: >-\n    The criterion does not include the selection that the Figure 4 legend applies to the\n    neurons of Figures 4D and 4H, significant heading tuning at p < 0.05 by ANOVA. Should the\n    criterion restrict the test to neurons with significant tuning?\n  passage: >-\n    Figure 4 legend, (D and H), \"Data were culled from a large database of MSTd neurons recorded\n    with a single electrode. Only neurons with significant heading tuning (p < 0.05, ANOVA) were\n    included (visual: n = 992; vestibular: n = 556).\"\n  why: >-\n    Without the selection, poorly tuned units enter the test with very large thresholds and\n    arbitrary preferred headings. The data set holds only trial-averaged curves, so the\n    selection can be approximated at best. With a proxy (one-way ANOVA from the mean curve,\n    five repetitions, variance equal to the mean) 252 of 258 values are kept, and with a\n    stricter one (three repetitions, variance twice the mean) 169; the one reading that passes\n    (vector-sum preference, spline threshold, log10, two factors) gives p = 1.2e-07 and 9.6e-08,\n    and no other reading passes, so the outcome here does not change. Raised by the round-2\n    verifier.\n- claim: fig8ab-choice-probability-lateral\n  asked: 2026-11-06\n  question: >-\n    The criterion compares the raw choice probabilities of fore-aft and lateral neurons. The\n    Figure 8A legend describes lateral neurons' choice probabilities as \"more deviated away from\n    the chance level of 0.5\". Is the comparison meant on the raw values, or on their distance\n    from 0.5?\n  passage: >-\n    Figure 8 legend, (A), \"Choice probability tends to be more deviated away from the chance\n    level of 0.5 for neurons with lateral heading preferences.\" Results, Possible rsignal\n    Distributions in Area MSTd, \"neurons with a preference for fore-aft movement show\n    significantly smaller choice probabilities (p = 0.019, t test, Figures 8A and 8B)\".\n  why: >-\n    The two readings differ when choice probabilities below 0.5 are common. On the 258 values of\n    the data set, the distance from 0.5 is larger for lateral units under every preference\n    reading (0.072 to 0.074 against 0.062 to 0.063) but not significantly (p = 0.10 to 0.17),\n    as the raw values are not (p = 0.14 to 0.80), so the outcome here does not change. Raised by\n    the round-2 verifier.\n"
}
```

```
File created successfully at: questions/crcns-stc-1.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/crcns-stc-1-gu-2011-01.yaml"; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old[:60]
    s=s.replace(old,new)
rep("""  notes: No pair carries an electrode label. Ten file_ids of monkey 17 end in "s", which the data
    descriptor does not explain;""","""  notes: No pair carries an electrode label. Ten pairs of monkey 17, in six recordings, have file_ids
    ending in "s", which the data descriptor does not explain (printed under the data check);""")
rep("""  statement: No pair carries an electrode or distance label, and ten file_ids of monkey 17 end in
    "s" without explanation,""","""  statement: No pair carries an electrode or distance label, and ten pairs of monkey 17, in six
    recordings (m17c36r1s, m17c40r1s, m17c41r1s, m17c42r1s, m17c44r1s, m17c48r1s), have file_ids
    ending in "s" without explanation,""")
rep("""headings. Seven pair recordings share a cell id with experiment 1 units, but the data set does
    not say which pair unit, if any, those curves belong to.""","""headings. Seven pairs, each in its own recording, share a cell id with experiment 1 units
    (printed under the data check), but the data set does not say which pair unit, if any, those
    curves belong to.""")
rep("""values in the data set approximates, matching 0.023 and 0.116 to the third decimal), and do the""",
"""values in the data set approximates, giving 0.0241 and 0.1190, within the SEMs of the paper's
    0.023 and 0.116), and do the""")
rep("""    (p = 0.00024 and 0.00017) and the vestibular one in neither (p = 0.082 and 0.185). Tested after
    the round-1 verification found that the claim had been blocked wrongly.""",
"""    (p = 0.00024 and 0.00017) and the vestibular one in neither (p = 0.082 and 0.185). The outcome
    rests on the one passing reading. In it the preference by condition interaction is significant
    (p = 0.026), the difference being larger in the visual condition. The two-factor ANOVA counts
    each unit twice; a mixed model with a random intercept per unit gives p = 2.7e-07 in that
    reading and no other reading below 0.001. With a proxy of the paper's tuning selection, 252 of
    258 values are kept and the reading gives p = 1.2e-07 (mixed model 1.8e-07); with a stricter
    proxy, 169 are kept and it gives p = 9.6e-08. Under both, no other reading reaches p < 0.001
    (smallest 0.012), and the smallest two-factor p with spline-peak preferences is 0.051. Tested
    after the round-1 verification found that the claim had been blocked wrongly.""")
rep("""  - The tuning curves in spikes/s are read as counts over the middle 1 s (Experimental Procedures,
    Noise and Signal Correlations); a different window scales all thresholds alike.""",
"""  - The tuning curves in spikes/s are read as counts over the middle 1 s (Experimental Procedures,
    Noise and Signal Correlations). The first term of equation 3 scales with the window and the
    trace term does not, so another window does not scale all thresholds alike; with 0.5 s or 2 s
    the passing reading gives p = 1.9e-07, as with 1 s.
  - The Figure 4 legend includes only neurons with significant heading tuning (p < 0.05, ANOVA).
    That selection needs trial responses, which the data set does not hold, so the readings
    include every unit. As a check, a proxy selection computes the one-way ANOVA from each mean
    curve with variance equal to the mean (equation 4) and five repetitions ("typically repeated
    five times", Experimental Protocol and Task), and a stricter one with three repetitions and
    variance twice the mean; the outcome is the same under both.
  - The two-factor reading counts each unit once per condition, as the paper's pooled neuron
    counts suggest; a mixed model with a random intercept per unit is shown and agrees.""")
open(p,"w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/crcns-stc-1-gu-2011-01.yaml"; s=open(p).read()
old="""  - The two-factor reading counts each unit once per condition, as the paper's pooled neuron
    counts suggest; a mixed model"""
assert old in s
s=s.replace(old,"""  - The two-factor reading counts each unit once per condition; a mixed model""")
open(p,"w").write(s)
EOF
date -u
```

```
Fri Nov  6 18:31:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/v2.py <<'EOF'
import yaml, textwrap
p="attempts/crcns-stc-1-gu-2011-01.yaml"
rec=yaml.safe_load(open(p))
outc={o["claim"]:o["outcome"] for o in rec["outcomes"]}
order=[r["claim"] for r in rec["verifications"][0]["results"]]
pooled="The pooled-rnoise assumption (mean of the two per-condition values) is stated and reasonable."
tuning="The tuning amplitude 30 and baseline 10 spikes/s over 1 s assumption is stated and reasonable."
reasons={
 "fig2b-trained-lower-noise-correlation":(pooled+" It quoted the statement that the main result matches the paper to the third decimal (Summary, README, methods_unavailable finding) as not supported, as cell 16 prints 0.0241 and 0.1190 against 0.023 and 0.116, within the paper's SEMs but not equal to the third decimal; it overstates the support for the assumption. It also quoted the README's \"Most outcomes rest on one assumption\", as only 7 of the 17 tested outcomes rest on it and another 4 rest on the tuning amplitude and baseline.",
   "The Summary, the README and the methods_unavailable finding now say that the means lie within the paper's SEMs, giving the values, and the Summary and README say that 7 of the 17 tested outcomes rest on this assumption and 4 on the tuning parameters. Outcome kept."),
 "figs2b-individual-animals":(pooled,"No change."),
 "fig5-noise-signal-positive":(pooled,"No change."),
 "fig5-slope-unchanged":(pooled,"No change."),
 "fig5-intercept-lower-trained":(pooled+" Resolved from round 1, bootstrap intercept intervals added (cell 37); they overlap.","No change."),
 "fig5-regression-coefficients":(pooled+" Problem 4 (cell 0 header) is fixed.","No change."),
 "fig8cd-noise-not-preference":(pooled+" Problem 3 resolved, the conflict with the claims-file point-count rule is stated in cells 62 and 64 and in the notes, and the claims-file readings support the argument made there.","No change."),
 "fig6a-population-thresholds":(tuning+" fig6a is sensitive to this choice, in cell 44 baseline 2 gives 4.32 and baseline 20 gives 5.90, both outside 4.5 to 5.5, and the record states this. Problem 6 resolved, cell 43 prints the rsignal difference (5.6e-07).","No change."),
 "fig6b-slope-not-intercept":(tuning,"No change."),
 "fig7a-pair-sign-of-effect":(tuning+" Resolved from round 1, the crossover is reported, rsignal = -0.0216 (cell 50).","No change."),
 "fig7c-narrow-preferences":(tuning+" It agrees with partially_reproduced, the change it asked for in round 1.","No change."),
 "fig8ab-choice-probability-lateral":("It holds under every preference reading, including the corrected vector sum (p = 0.80), and under the distance-from-0.5 variant (p = 0.10 to 0.17), so it does not depend on how the CPs are signed. Problem 1 resolved, the vector sum is weighted for the uneven heading spacing, checked on synthetic curves in cell 56. The criterion tests raw CP, where the Figure 8A legend describes CP \"more deviated away from the chance level of 0.5\"; the notebook runs this as a variant and the outcome is unchanged. Whether the 258 CPs are among the paper's 311 cannot be resolved from the data set. The rule \"reproduced under one reading\" is permissive when there are 8 or more readings, a design point, not a misreading.",
   "Added the reading of the Figure 8A legend to questions/crcns-stc-1.yaml as a question for a reader; the claim is unchanged. The one-reading rule is the claims file's and is not changed. Outcome kept."),
 "methods-single-vs-multiple-electrodes":("Problem 8 resolved, recorded as a finding. The statement \"Ten file_ids of monkey 17 end in 's'\" in the notes and a metadata_insufficient finding is printed by no cell.",
   "The data check now prints the pairs whose file_id ends in \"s\" (10 pairs of monkey 17 in six recordings, listed), and the notes and finding now say ten pairs in six recordings. Outcome kept."),
 "fig2a-behavioral-learning":("Problem 7 resolved, fixed in cell 11.","No change."),
 "fig7b-msdt-pairs":("The statement in the notes that seven pair recordings share a cell id with experiment 1 units is printed by no cell.",
   "The data check now prints them (7 pairs in 7 recordings, listed), and the notes point to it. Outcome kept."),
 "fig4dh-lateral-more-sensitive":("It meets the criterion as written, lateral thresholds lower with p < 0.001 under at least one reading, but the result is fragile and the record does not say so in full. Only 1 of the 8 claims-file readings passes (cell 57, weighted vector sum, spline, log10, two-factor ANOVA, p = 1.9e-07). In that reading the preference by condition interaction is significant (p = 0.026), which neither the conclusion nor the notes report. The two-factor ANOVA counts each of the 129 units twice. With spline-peak preferences no reading reaches p < 0.05. The analysis applies no tuning-significance selection, which the Figure 4 legend uses (\"Only neurons with significant heading tuning (p < 0.05, ANOVA) were included\"), and the record does not list this as a deviation; without it poorly tuned units with huge thresholds and arbitrary preferences enter the test, which may explain why the two preference readings agree on only 71.7% of group labels and why no spline-peak reading passes. The selection cannot be applied exactly to trial-averaged curves; it should be listed as a deviation, with the interaction and the double counting. The deviation \"a different window scales all thresholds alike\" is not exact, as the trace term 0.5(f'/f)^2 does not scale with the counting window; the effect is small and does not change the outcome. Problem 2 resolved, the claim is now tested.",
   "Added a check after the main table. A proxy of the tuning selection (one-way ANOVA from each mean curve with variance equal to the mean and five repetitions, the Experimental Procedures' typical count) keeps 252 of 258 values, and a stricter one (three repetitions, variance twice the mean) keeps 169; the passing reading gives p = 1.2e-07 and 9.6e-08, and no other reading reaches p < 0.001. A mixed model with a random intercept per unit gives p = 2.7e-07 in the passing reading and agrees on which readings pass. The conclusion and notes now report the interaction (p = 0.026) and that the outcome rests on one reading. The selection, the double counting and the corrected window statement are deviations, and the notebook now shows the passing reading with 0.5 s and 2 s windows (p = 1.9e-07 in each). The missing selection is added to questions/crcns-stc-1.yaml as a question for a reader; the claim is unchanged. Outcome kept, no change proposed, as every check gives the same outcome."),
}
results=[]
for c in order:
    r,resp=reasons.get(c,("Agrees with the outcome; no comment.","No change."))
    if c=="training-group-link": r="Agrees with the outcome; no comment."
    results.append({"claim":c,"agrees":True,"outcome":outc[c],"reason":r,"response":resp})
# README runtime statement: attach to no claim; recorded in reviewed text
v={"date":"2026-11-06","kind":"agent","by":"Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
   "reviewed":"Round 2. The full executed notebook with the conclusions and the summary, the attempt record, the README, the helper module and the claims file, with the paper. Report in transcripts/crcns-stc-1/verifier-2-report.md. Points not tied to one claim, the README's \"It takes about two minutes\" (no output gives a run time) is answered by a cell before the summary that prints the run time (51 s), and the README now says about one minute.",
   "results":results}
out=yaml.safe_dump([v],sort_keys=False,width=100,allow_unicode=True)
out=textwrap.indent(out,"")
open(p,"a").write(out)
EOF
python $TMPDIR/v2.py; tail -30 attempts/crcns-stc-1-gu-2011-01.yaml
```

```
outcome: blocked
    reason: Agrees with the outcome; no comment.
    response: No change.
  - claim: figs4-population-sensitivity-any-reference
    agrees: true
    outcome: blocked
    reason: Agrees with the outcome; no comment.
    response: No change.
  - claim: fig7b-msdt-pairs
    agrees: true
    outcome: blocked
    reason: The statement in the notes that seven pair recordings share a cell id with experiment 1 units
      is printed by no cell.
    response: The data check now prints them (7 pairs in 7 recordings, listed), and the notes point to
      it. Outcome kept.
  - claim: figs5-congruency
    agrees: true
    outcome: blocked
    reason: Agrees with the outcome; no comment.
    response: No change.
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/reason: Agrees with the outcome; no comment\./reason: Agrees with the outcome (it agrees with all 35), with no comment on this claim./' attempts/crcns-stc-1-gu-2011-01.yaml; grep -n -- "—\|rather" attempts/crcns-stc-1-gu-2011-01.yaml questions/crcns-stc-1.yaml entries/crcns-stc-1-gu-2011/README.md; grep -c "reproduce_gu" entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb; grep -n "—\| rather" entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb | head; python tools/entry.py check entries/crcns-stc-1-gu-2011 2>&1 | tail -5; python tools/entry.py --help 2>&1 | head -20
```

```
0
0 error(s)
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls tools; python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -2; git status --short
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
paper_match.py
papers_manifest.py
progress.py
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;nb=json.load(open('entries/crcns-stc-1-gu-2011/reproduce_gu_2011.ipynb'))
print(sum(len(c.get('outputs',[])) for c in nb['cells']))"; python -c "import yaml;yaml.safe_load(open('questions/crcns-stc-1.yaml'));print('ok')"
```

```
0
ok
```

**Agent**

No outcome changed and none is proposed. The round-2 verifier agreed with all 35 outcomes, and the new checks it prompted give the same results. The entry passes `python tools/entry.py all` (0 errors, notebook runs in about 53 s). Nothing is committed.

**fig4dh-lateral-more-sensitive (still reproduced).** I added three checks after the main table:
- **Tuning selection.** The paper includes only significantly tuned neurons, which needs trial data the data set does not have. As a stand-in, I ran a one-way ANOVA from each mean curve, assuming spike-count variance equal to the mean and five repetitions per heading. That keeps 252 of 258 values, and the passing reading gives p = 1.2e-07. A stricter version (three repetitions, variance twice the mean) keeps 169 values and gives p = 9.6e-08.
- **Units counted twice.** A mixed model with one random intercept per unit gives p = 2.7e-07 in the passing reading, and no other reading passes.
- **Counting window.** With 0.5 s or 2 s windows the passing reading still gives p = 1.9e-07.

The other readings still do not reach p < 0.001 under either selection. The conclusion, notes and deviations now say:
- the outcome rests on one of the 8 readings;
- the preference by condition interaction is significant (p = 0.026);
- the tuning selection is not applied, and each unit enters twice.

I also corrected the claim that "a different window scales all thresholds alike"; one term of the threshold formula does not scale with the window. To support this, `stc1.neuron_threshold` gained a `window` argument, which defaults to 1 s, so earlier results are unchanged.

**Text corrected:**
- "Matches the paper to the third decimal" is gone from the Summary, the README and the finding. They now say the group means 0.0241 and 0.1190 lie within the SEMs of the paper's 0.023 and 0.116.
- The README now says 7 of the 17 tested outcomes rest on the pooled noise-correlation assumption and 4 on the tuning amplitude and baseline, instead of "most outcomes".

**Outputs added:**
- The data check now prints the file_ids ending in "s". The record said "ten file_ids"; it is ten pairs in six recordings, so the notes and the finding now say that.
- The data check also prints the 7 pairs whose recordings share a cell id with experiment 1 units.
- A new cell prints the notebook run time. The README now says about one minute, and `entry.yaml` lists 1 minute.

**Questions file:** I created `questions/crcns-stc-1.yaml` with two questions for a reader, without changing the claims:
- whether the fig4dh criterion should apply the Figure 4 legend's selection of significantly tuned neurons;
- whether fig8ab should compare raw choice probabilities or their distance from 0.5, as the Figure 8A legend describes.

**Record:** Round 2 is under `verifications`, with `agrees: true` for all 35 claims, the verifier's reasons and my responses.

**Not done:** The verifier's point that "reproduced under one reading" is a lenient rule when there are 8 or more readings is about how the claims file was designed, not a misreading of the paper. I recorded it in the fig8ab response and left the rule alone. The paper's exact tuning selection cannot be applied without trial responses, and whether the data set's 258 choice probabilities are among the paper's 311 cannot be checked from it.

## End of run

48 turns, 10 minutes, $2.04 at API prices, result: success.
