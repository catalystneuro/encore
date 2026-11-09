# crcns-stc-1 · verifier-1 · run 42263047023

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 340
drwxr-xr-x 6 runner runner    4096 Nov  6 17:43 .
drwxr-xr-x 7 runner runner    4096 Nov  6 17:43 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 17:35 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 17:35 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  6 17:43 .claude
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.development
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.local
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.production
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.test
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .env.test.local
drwx------ 2 runner runner    4096 Nov  6 17:43 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 17:35 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 17:35 .github
-rw-r--r-- 1 runner runner       0 Nov  6 17:42 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 17:35 .idea
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.neuron.2011.06.015.yaml
```

```
<persisted-output>
Output too large (54.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/525e1f05-3123-4e0e-8ca1-9ff987722cfd/tool-results/brsmgcigt.txt

Preview (first 2KB):
# Claims for Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), Neuron 71:750-761,
# "Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual Cortex", on CRCNS data
# set stc-1 (doi:10.6080/K07P8WKF).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, and
# the Supplemental Information PDF (legends of Figures S1 to S8). The article says the
# Supplemental Information "includes Experimental Procedures and eight figures"; the supplement
# as supplied, whose own contents page lists only the eight figures, holds no further
# procedures, so the Experimental Procedures of the article are taken as the whole Methods.
# The PDF could not be rendered here; the extracted text prints degree signs, minus signs and
# "approximately" as a replacement character, and quotes avoid those places. The paper links no
# analysis code, so none was read.
#
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat stc1.py
```

```
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

Where the parameters come from:

- Training groups. The data set does not say which monkey is naive or trained. The paper gives
[... 235 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/525e1f05-3123-4e0e-8ca1-9ff987722cfd/tool-results/brsmgcigt.txt"
}
```

```
1	# Claims for Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), Neuron 71:750-761,
2	# "Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual Cortex", on CRCNS data
3	# set stc-1 (doi:10.6080/K07P8WKF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
5	# protocol as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
8	# with its Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, and
9	# the Supplemental Information PDF (legends of Figures S1 to S8). The article says the
10	# Supplemental Information "includes Experimental Procedures and eight figures"; the supplement
11	# as supplied, whose own contents page lists only the eight figures, holds no further
12	# procedures, so the Experimental Procedures of the article are taken as the whole Methods.
13	# The PDF could not be rendered here; the extracted text prints degree signs, minus signs and
14	# "approximately" as a replacement character, and quotes avoid those places. The paper links no
15	# analysis code, so none was read.
16	#
17	# Data the paper used. Eight male rhesus monkeys (Macaca mulatta): three "naive" animals trained
18	# only to fixate, and five "trained" animals extensively trained in a vestibular and visual
19	# heading discrimination task (left or right of straight ahead) before recording. Pairs of
20	# single units recorded simultaneously in area MSTd while the animals fixated passively and
[... 941 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_gu_2011.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'===== CELL {i} [{c[\"cell_type\"]}]')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt; grep -c "yaml" /dev/null; python3 -c "
import yaml;d=yaml.safe_load(open('10.1016-j.neuron.2011.06.015.yaml'));print(len(d['claims']))"
```

```
1094 /tmp/claude-1001/nb.txt
0
35
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	===== CELL 0 [markdown]
2	# Reproducing Gu et al. (2011) from CRCNS stc-1
3	
4	**Paper.** Gu Y, Liu S, Fetsch CR, Yang Y, Fok S, Sunkara A, DeAngelis GC, Angelaki DE (2011).
5	Perceptual learning reduces interneuronal correlations in macaque visual cortex. *Neuron* 71:750-761.
6	[doi:10.1016/j.neuron.2011.06.015](https://doi.org/10.1016/j.neuron.2011.06.015). The claims file
7	was written from the version of record (journal PDF text, with the Experimental Procedures and the
8	legends of Figures 1 to 8) and the Supplemental Information (legends of Figures S1 to S8).
9	
10	**Data set.** CRCNS [stc-1](https://doi.org/10.6080/K07P8WKF) (doi:10.6080/K07P8WKF), data
11	descriptor version 0.6 (5 September 2018), read from the public bucket `crcnsarchive` under
12	`stc-1/live/`. CRCNS data sets are not versioned, and the paper cites no version, so the version is
13	recorded as `unversioned` (docs/archives.md, CRCNS). The bucket holds one copy of the data,
14	`stc-1/live/` (`orig/` holds only an older description document), so `live/` is the version
15	pinned. The file read, `MSTd.mat`, is checked on loading against its MD5 sum in the data set's
16	`checksums.md5`, `cd4c13b360aa05689015f1bd2b88a05a`, so a later change makes the notebook fail
17	(`VIP.mat`, read only to check for overlap, `8d7924e0a1ae86c56b78cd1e2f530e2d`).
18	
19	**What the data set holds.** Derived values only. For the paper, experiment 3 of `MSTd.mat` holds
20	the 127 MSTd pairs separated by less than 1 mm, with per condition (vestibular, visual) the signal
[... 693 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 714
}
```

```
714	sizes = [16, 64, 256, 1000, 2000]
715	rsig_readings = {"8 headings": stc1.RSIGNAL_HEADINGS_8, "1-degree grid": stc1.RSIGNAL_HEADINGS_CONT}
716	rows = []
717	for name, H in rsig_readings.items():
718	    for n in sizes:
719	        prefs = stc1.uniform_prefs(n)
720	        ind = stc1.threshold(prefs, None, H)
721	        nv = stc1.threshold(prefs, stc1.NAIVE, H)
722	        tr = stc1.threshold(prefs, stc1.TRAINED, H)
723	        rows.append({"rsignal": name, "N": n, "independent": ind, "naive": nv, "trained": tr,
724	                     "naive/independent": nv / ind, "trained/naive": tr / nv})
725	fig6a = pd.DataFrame(rows)
726	print(fig6a.round(4).to_string(index=False))
727	print("\nExpected at N = 2000: naive/independent 5 +- 0.5 (4.5 to 5.5), trained within 10% of naive")
728	--OUT--
729	Wrapped-Gaussian sigma for a 135 degree full width at half height: 58.01 degrees
730	
731	--OUT--
732	      rsignal    N  independent   naive  trained  naive/independent  trained/naive
733	   8 headings   16       8.8020 12.4558  12.6727             1.4151         1.0174
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/stc-1.data-description.txt | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=stc-1/" | tr '<' '\n<' | grep -E "^(Key|Size)>" | head -50
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "fisher|threshold.*sqrt|equation|trace|Tr\[|choice probab|fore-aft|congruen|328|pooled|z-score|vector sum|preferred heading" 10.1016-j.neuron.2011.06.015.txt | head -80
```

```
119:have been z-scored to remove the stimulus effect and allow
133:we recomputed rnoise by pooling z-scored responses across
232:the time courses of firing rates and response variability. As illustrated in Figures 3A and 3C, the time course of the populationaverage response to the preferred heading was indistinguishable
273:cell’s preferred heading in trained (red, n = 146) and naive animals (blue,
309:further, we interpolated tuning curves and used Fisher information analysis (Gu et al., 2010, see Experimental Procedures) to
314:have a steep slope around straight-ahead. For quantitative analysis, neurons were divided into two groups by heading preference: ‘‘fore-aft’’ neurons with heading preferences within 45�
319:sensitive than fore-aft neurons for heading discrimination around
349:(C and G) Neurons preferring lateral headings are more sensitive to heading variations around straight ahead than neurons preferring fore-aft motion, with little
351:(D and H) Comparison of average neuronal sensitivity between fore-aft and lateral neurons (see G). Data were culled from a large database of MSTd neurons
381:vestibular heading preferences (‘‘congruent’’ cells) or mismatched preferences (‘‘opposite’’ cells) (Gu et al., 2006, 2008a).
382:Thus, we also tested whether rnoise depends on congruency.
383:Specifically, the two units in each pair could be (1) both congruent, (2) both opposite, or (3) a mixture of congruent and
384:opposite cells. As illustrated in Figure S5, rnoise was not substantially affected by congruency. Next, we incorporate these results
399:congruent visual and vestibular heading preferences. Results
400:were similar when variable congruency was introduced into the
401:simulation, consistent with the observation that noise correlations were not strongly influenced by congruency (Figure S5).
422:inverse of Fisher information (If), an upper bound on information
518:we further examined the dependence of choice probability and
521:neurons with a preference for
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 300,330p 10.1016-j.neuron.2011.06.015.txt; echo ----; sed -n 505,610p 10.1016-j.neuron.2011.06.015.txt; echo ----; sed -n 885,990p 10.1016-j.neuron.2011.06.015.txt
```

```
perform a fine heading discrimination task did not significantly
shape the heading tuning of individual MSTd neurons.
However, it remains possible that training only shaped the
tuning of a subset of neurons that were most informative for
heading discrimination around the straight-forward reference
used in training (e.g., Raiguel et al., 2006; Schoups et al.,
2001). If so, then effects might only be seen for neurons most
sensitive to heading variations around straight forward, and
may have been missed in the above analysis. To examine this
further, we interpolated tuning curves and used Fisher information analysis (Gu et al., 2010, see Experimental Procedures) to
compute the sensitivity of each neuron for discriminating
heading around straight forward. As shown in Figures 4C and
4G, the most sensitive neurons (lowest thresholds) are generally
those that prefer lateral headings, such that their tuning curves
have a steep slope around straight-ahead. For quantitative analysis, neurons were divided into two groups by heading preference: ‘‘fore-aft’’ neurons with heading preferences within 45�
of forward (0�) or backward (±180�) motion, and ‘‘lateral’’
neurons with heading preferences within 45�of leftward (�90�)
or rightward (90�) movements. Consistent with previous findings
(Gu et al., 2008a, 2010), lateral neurons were significantly more
sensitive than fore-aft neurons for heading discrimination around
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, stc1
from scipy import stats
rng=np.random.default_rng(0)
# pooled rnoise check: 8 headings x 5 reps per condition, different r per condition
def sim(r,n):
    C=[[1,r],[r,1]]; return rng.multivariate_normal([0,0],C,size=n)
err=[]
for k in range(300):
    zs=[]; rs=[]
    for r in (0.0,0.3):
        z=[]
        for h in range(8):
            x=sim(r,5); x=(x-x.mean(0))/x.std(0,ddof=1); z.append(x)
        z=np.vstack(z); zs.append(z); rs.append(np.corrcoef(z.T)[0,1])
    allz=np.vstack(zs); err.append(np.corrcoef(allz.T)[0,1]-np.mean(rs))
print('pooled - mean of per-cond: mean %.4f max abs %.4f'%(np.mean(err),np.max(np.abs(err))))
# tls
X=rng.normal(size=(500,2)); y=X@[0.12,0.09]+0.07+rng.normal(scale=0.01,size=500)
print('tls',stc1.tls_plane(X,y))
# pref
h=np.array([135,90,45,22.5,0,-22.5,-45,-90,-135,-180.])
for p in (0,60,90,180):
  r=stc1.tuning([p],h)[0]
  print(p,'vs',round(stc1.pref_vector_sum(h,r),1),'spline',stc1.pref_spline_peak(h,r))
# fwhm
g=stc1._wrapped_gaussian(np.arange(-180,180,0.5),[0.],stc1.SIGMA)[0]; m=(g-g.min())/(g.max()-g.min())
print('fwhm',(m>=0.5).sum()*0.5)
# independent threshold analytic
pr=stc1.uniform_prefs(64); f=stc1.tuning(pr,0.)[:,0]; fp=(stc1.tuning(pr,1e-3)[:,0]-stc1.tuning(pr,-1e-3)[:,0])/2e-3
I=np.sum(fp**2/f)+0.5*np.sum((fp/f)**2); print('indep',np.sqrt(2/I),stc1.threshold(pr,None))
print('units: fp per degree -> threshold in degrees')
# rsignal 8 vs cont
R8=stc1.signal_corr(pr,stc1.RSIGNAL_HEADINGS_8); Rc=stc1.signal_corr(pr,stc1.RSIGNAL_HEADINGS_CONT); print('max diff rsig',np.abs(R8-Rc).max())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, stc1
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls node_modules; which -a python python3; ls ~/.venv* /opt 2>/dev/null; pip --version; uv --version 2>/dev/null
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
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
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy scipy pandas fsspec 2>&1 | tail -2; python -c "import numpy,scipy,pandas;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, stc1
rng=np.random.default_rng(0)
def sim(r,n):
    return rng.multivariate_normal([0,0],[[1,r],[r,1]],size=n)
err=[]
for k in range(300):
    zs=[]; rs=[]
    for r in (0.0,0.3):
        z=[]
        for h in range(8):
            x=sim(r,5); x=(x-x.mean(0))/x.std(0,ddof=1); z.append(x)
        z=np.vstack(z); zs.append(z); rs.append(np.corrcoef(z.T)[0,1])
    allz=np.vstack(zs); err.append(np.corrcoef(allz.T)[0,1]-np.mean(rs))
print('pooled - mean of per-cond: mean %.4f max abs %.4f'%(np.mean(err),np.max(np.abs(err))))
X=rng.normal(size=(500,2)); y=X@[0.12,0.09]+0.07+rng.normal(scale=0.01,size=500)
print('tls',stc1.tls_plane(X,y))
h=np.array([135,90,45,22.5,0,-22.5,-45,-90,-135,-180.])
for p in (0,30,60,90,120,180):
  r=stc1.tuning([p],h)[0]
  print(p,'vs',round(stc1.pref_vector_sum(h,r),1),'spline',stc1.pref_spline_peak(h,r))
g=stc1._wrapped_gaussian(np.arange(-180,180,0.5),[0.],stc1.SIGMA)[0]; m=(g-g.min())/(g.max()-g.min())
print('fwhm',(m>=0.5).sum()*0.5)
pr=stc1.uniform_prefs(64); f=stc1.tuning(pr,0.)[:,0]; fp=(stc1.tuning(pr,1e-3)[:,0]-stc1.tuning(pr,-1e-3)[:,0])/2e-3
I=np.sum(fp**2/f)+0.5*np.sum((fp/f)**2); print('indep',np.sqrt(2/I),stc1.threshold(pr,None))
R8=stc1.signal_corr(pr,stc1.RSIGNAL_HEADINGS_8); Rc=stc1.signal_corr(pr,stc1.RSIGNAL_HEADINGS_CONT); print('max diff rsig',np.abs(R8-Rc).max())
print(stc1.preference_group([44.9,45,135,135.1,-45,-135.1]))
# min eigenvalue naive R at intercept 0 slope .211, 256
p=stc1.uniform_prefs(256); R=0.211*stc1.signal_corr(p,stc1.RSIGNAL_HEADINGS_8); np.fill_diagonal(R,1); print('min eig',np.linalg.eigvalsh(R).min())
"
```

```
pooled - mean of per-cond: mean -0.0000 max abs 0.0000
tls (array([0.12050143, 0.08968251]), 0.07012644103440852)
0 vs 0.0 spline 0.0
30 vs 16.0 spline 30.0
60 vs 34.7 spline 59.0
90 vs 59.4 spline 90.0
120 vs 92.6 spline 121.0
180 vs -180.0 spline -180.0
fwhm 135.5
indep 4.4009994385174505 4.4009994385174505
max diff rsig 5.408656572614134e-07
['fore-aft' 'lateral' 'lateral' 'fore-aft' 'lateral' 'fore-aft']
min eig 0.7889999999999942
```

**Agent**

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
| fig5-intercept-lower-trained | partially_reproduced | Cell 29: the training main effect is significant (p = 0.018 vestibular, 0.0074 visual, pooled rnoise). The 95% intervals of the intercepts overlap under every construction: separate fits, the ANCOVA model, and the additive model. |
| fig5-regression-coefficients | partially_reproduced | Cell 31, readings (a) and (b): slopes 0.119/0.084 and 0.132/0.085, naive intercept 0.077/0.074, all within tolerance. The trained intercept is 0.003/0.002, outside 0.005 ± 0.0005, though still below the naive one. Reading (c) misses the visual slope (0.106). |
| fig6a-population-thresholds | reproduced | Cell 33: at N = 2000 the naive/independent ratio is 5.41 (within 4.5–5.5) and trained/naive is 1.000, under the claims-file reading (A30/B10) for both rsignal readings. The result is sensitive to the unstated amplitude and baseline: cell 34 gives 4.32 to 5.90. |
| fig6b-slope-not-intercept | reproduced | Cell 36: over a slope width of 0.2 the threshold changes by 1.97°, over an intercept width of 0.2 by 0.11°. The threshold falls from the trained to the naive intercept (7.251 → 7.217). It is not monotone at intercept 0 → 0.02. |
| fig7a-pair-sign-of-effect | partially_reproduced | Cell 38: all 88 pairs with positive rsignal follow the rule, and 92 of 93 with negative rsignal. The exception is at rsignal = −0.011 (pref2 = −2°), and the criterion requires every pair. |
| fig7c-narrow-preferences | partially_reproduced | Cell 40: the proportions are 48.6, 73.1 and 92.4%, all within tolerance, and the improvement grows from −0.5% to about 4.8%. The best improvement of 4.83% is far outside 8 ± 0.8. It stays at 3.6–6.0% under the amplitude and baseline variants; only dropping the trace term, which is not equation 3, reaches 8%. |
| fig8ab-choice-probability-lateral | not_reproduced | Cell 42 uses 258 CPs from two trained monkeys, a subset of the paper's 311. No preferred-heading reading gives fore-aft CP smaller with p < 0.05: spline peak 0.527 vs 0.542, p = 0.14; even-8 vector sum p = 0.69. The vector sum over all 10 headings gives the opposite sign (p = 0.0006), but that reading is biased (problem 1). Left vs right shows no difference (p = 0.27–0.56). |
| fig8cd-noise-not-preference | reproduced | Cell 44, trained pairs, as the Results specify ("in trained animals"): p = 0.43 (visual preference) and 0.17 (vestibular). Lateral rnoise is lower than fore-aft only with vestibular preferences. |
| fig2c-timecourse-naive-higher | blocked (data_missing) | I confirmed the archive listing: stc-1/live holds only MSTd.mat (65 KB, derived), VIP.mat, demo.m, docs, filelist.txt and checksums. There are no spike times. |
| figs2a-difference-decreases | blocked (data_missing) | Same: no spike times. |
| fig3-mean-response-unchanged | blocked (data_missing) | Same. |
| fig3-fano-unchanged | blocked (data_missing) | Same. |
| figs8c-renormalization | blocked (data_missing) | No trial-ordered responses. |
| discussion-stimulus-reduces-correlation | blocked (data_missing) | No prestimulus responses. |
| figs1-distance | blocked (data_missing) | No distances, and no pairs over 1 mm (all 127 are under 1 mm). |
| methods-single-vs-multiple-electrodes | blocked (data_missing) | No electrode label, and the recording structure (cell 6) cannot stand in for one. |
| fig2a-behavioral-learning | blocked (data_missing) | There are no training histories. `experiment2.behv` holds one threshold per monkey for monkeys 2 and 5 (1.2/1.2° and 3.1/3.25°), both inside 0.9–3.3°. Only the plateau part could be checked, for 2 of 5 animals, and the notebook does not report it. |
| fig4-tuning-width-visual | blocked (data_missing) | The single-unit data have no naive animals. Trained medians could be computed from the experiment1 tuning curves for a descriptive comparison only. The ANOVA selection cannot be applied to trial-averaged curves. |
| fig4-tuning-width-vestibular | blocked (data_missing) | Same. |
| fig4-amplitude-unchanged | blocked (data_missing) | Same. |
| fig4dh-lateral-more-sensitive | blocked (data_missing), wrongly | The preference-group effect could have been tested within trained animals: experiment1 tuning curves give a Fisher threshold and preference for 129 units, and experiment2 adds neuronal thresholds. The notebook used the same subset for fig8ab (problem 2). |
| fig4dh-training-no-sensitivity-change | blocked (data_missing) | Needs naive single units. |
| figs4-population-sensitivity-any-reference | blocked (data_missing) | Needs naive single units. |
| fig7b-msdt-pairs | blocked (data_missing) | Pairs carry only preferences and correlations, no tuning curves. |
| figs5-congruency | blocked (data_missing) | The congruency index needs each unit's tuning curves. A proxy from the visual–vestibular preference difference is possible but is not the paper's measure. |
| figs6-task-independent | blocked (data_missing) | No discrimination-task correlations. |
| figs8ab-eye-movements | blocked (data_missing) | No eye records. |

**B. Problems**

1. [affects a conclusion] `stc1.pref_vector_sum`, used in cell 42, takes the vector sum over the 10 unevenly spaced experiment1 headings (extra ±22.5°) with no weighting for angular spacing. On synthetic wrapped-Gaussian curves, true preferences of 30/60/90/120° come out as 16/35/59/93°, so many lateral units are labelled fore-aft (171 vs 87). This reading is the only one with a significant effect, and that effect has the opposite sign. It should be dropped or replaced by a spacing-weighted vector sum. The fig8ab outcome stays not_reproduced either way.
2. [affects a conclusion] Cell 0: fig4dh-lateral-more-sensitive is marked blocked for having "no naive animals". Its main claim is the preference-group effect, which can be tested within the two trained monkeys from experiment1 and experiment2, with the claims-file Fisher threshold on interpolated tuning curves. The notebook used exactly this subset for fig8ab. The claim should be partially tested, not blocked.
3. [affects a conclusion] fig8cd-noise-not-preference, cell 44. The claims file says to judge under the reading whose point count is closest to 328. The 127-pair variant (254 points) is closer than the 178 used, and with vestibular preference it gives p = 0.0009. I keep "reproduced" because the Results restrict the statement to trained animals, but the notebook should state this conflict with the claims-file rule.
4. [does not affect a conclusion] Cell 0 says "None of the analyses below draws random numbers"; cell 31 runs a seeded bootstrap.
5. [does not affect a conclusion] `stc1.pooled_rnoise`. I checked on synthetic data that the pooled-z-score Pearson equals the mean of the per-condition values when trial numbers are equal and there are no outliers. The match to the paper's means (0.0241/0.1190 vs 0.023/0.116) supports the assumption. Whether the stored values include outlier removal or renormalization cannot be told.
6. [does not affect a conclusion] fig6a–7c: the two rsignal readings give identical results. I confirmed that the maximum difference in rsignal is 5e-7, so the second reading adds nothing. The real open parameters are amplitude and baseline, which move fig6a across its tolerance (A35 gives 5.57) and fig7c between 3.6 and 6.0%.
7. [does not affect a conclusion] Not reported for fig2a: the plateau thresholds of the two trained monkeys in `experiment2.behv`.
8. [does not affect a conclusion] Cell 6 finds a recording with 6 pairs, against the paper's stated maximum of 5. It is noted but not explained.

Helper checks on synthetic data all passed: `tls_plane` recovers known coefficients; `threshold` with independent noise matches the analytic Fisher information; `sigma_for_fwhm` gives a width of 135.5°; `preference_group` boundaries are as documented; `pref_spline_peak` is accurate to within 1°.

**C. Not checked**

- I could not re-run the data loading. The figures are not shown in the text outputs.
- Whether `corr_noise` includes renormalization or outlier removal. Per-pair trial counts would settle this, but the data set does not hold them.
- fig5-intercept: what interval method the paper used. A bootstrap interval for the per-group intercept, added alongside the parametric ones, would help.
- fig7a: where the crossover sits. Adding the rsignal at which trained/naive equals 1 would show this.
- fig8ab: how many of the 258 CPs are in the paper's 311, and the sign convention of the CPs. A per-unit result with a spacing-weighted vector sum would have made the reading sound.
- fig4dh: the trained-only analysis of thresholds by preference group, which the notebook never ran.

## End of run

16 turns, 3 minutes, $1.35 at API prices, result: success.
