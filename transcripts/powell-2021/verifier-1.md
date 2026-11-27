# powell-2021 · verifier-1 · run 45650305438

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper; ls docs 2>/dev/null
```

```
Exit code 2
total 400
drwxr-xr-x 6 runner runner    4096 Nov 25 16:06 .
drwxr-xr-x 8 runner runner    4096 Nov 25 16:06 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 15:58 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 15:58 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 25 16:06 .claude
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.development
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.local
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.production
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.test
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .env.test.local
drwx------ 2 runner runner    4096 Nov 25 16:06 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 15:58 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 15:58 .github
-rw-r--r-- 1 runner runner       0 Nov 25 16:06 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 15:58 .idea
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "powell-2021.yaml"
}
```

```
1	# Claims for Powell, Haddad, Gorur-Shandilya & Marder (2021), eLife 10, e60454,
2	# doi:10.7554/elife.60454, tested on ZENODO:3924718.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-25, following docs/protocol.md (Reader, protocol version pilot-18). No data of the
6	# dataset were seen; only its title and description on the archive (the paper's title and
7	# abstract: evoked gastric mill and pyloric rhythms of Cancer borealis recorded from 7 to 23 C).
8	#
9	# Text read: the version of record as served by Europe PMC (PMC7889077, open access JATS,
10	# flattened to paper/10.7554-elife.60454.txt), with Results, Discussion, Materials and methods,
11	# the figure legends of Figures 1 to 6 and the legends of the four figure supplements (Figure 2,
12	# figure supplement 1; Figure 3, figure supplement 1; Figure 4, figure supplements 1 and 2).
13	# The paper has no other supplementary text. The legend of Figure 5f is garbled in the text
14	# ("Ratios of LG to PD cycle period were n across temperature"); the Results sentence that
15	# reports the same test is quoted instead.
16	#
17	# Code read: https://github.com/marderlab/gastric at commit
18	# fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2 (2020-11-17), the commit the paper cites as archived
19	# at Software Heritage, and the later head 7a82b1f9a2239f46d73ae86d2cc70de8226d89be
20	# (2021-09-09), which differs in fig_phase_relationships.m (a prep-by-prep Rayleigh test on the
[... 512 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "stg.py"
}
```

```
1	"""Loading and measures for the evoked gastric mill data of Zenodo record 3924718.
2	
3	Powell, Haddad, Gorur-Shandilya & Marder (2021), eLife 10, e60454, doi:10.7554/elife.60454.
4	
5	The record holds `evoked_data.mat` (MATLAB 7.3, HDF5), the spike annotations of the ten evoked
6	preparations, and zip files of raw ABF recordings. `evoked_data.mat` is a 10 x 1 struct `data`
7	with, per preparation, the spike times of PD, LG and DG (seconds), the saline temperature and a
8	mask sampled at 1 kHz, and two MATLAB `categorical` arrays: `experiment_idx` (the preparation's
9	name) and `filename` (per 1 kHz sample, the ABF file it comes from). The categoricals are stored
10	as MCOS objects; `load` decodes them from the file's `#subsystem#/MCOS` cell, where each object's
11	category names are followed by its codes. The file is streamed into memory from the archive and
12	its MD5 checked; nothing is written to disk.
13	
14	Where the parameters come from:
15	
16	- Burst detection is crabsort.computePeriods (https://github.com/sg-s/crabsort, +crabsort/
17	  computePeriods.m at commit 79bf337631b16b3de141d4d4ba065170caeda578, the last change before
18	  the paper's code commit), called by the paper's figure scripts with ISI thresholds of 0.18 s
19	  (PD) and 1 s (LG, DG) and minimum counts of 2 (PD) and 5 (LG, DG) (claims file header; the
20	  1 s threshold and the counts are the Methods, "Detection of bursts and measurement of burst
[... 384 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_powell_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1614 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Powell et al. (2021) from Zenodo record 3924718
3	
4	**Paper.** Powell D, Haddad SA, Gorur-Shandilya S, Marder E (2021). Coupling between fast and slow
5	oscillator circuits in *Cancer borealis* is temperature-compensated. *eLife* 10:e60454.
6	[doi:10.7554/elife.60454](https://doi.org/10.7554/elife.60454). The claims file
7	(`claims/powell-2021.yaml`) was written from the version of record (Europe PMC, PMC7889077) with its
8	figure supplements, and from the paper's code, https://github.com/marderlab/gastric at commit
9	fa07d36a7e57fc7787a9a8e2fed72300b1a8e6e2.
10	
11	**Dataset.** [ZENODO:3924718](https://zenodo.org/records/3924718), DOI 10.5281/zenodo.3924718,
12	record 3924718. The paper's data statement cites https://zenodo.org/record/3924718, this record,
13	and the deposit has no other version (concept 3924717 has the one version 3924718), so it is pinned.
14	Files read: `evoked_data.mat` whole (72,856,015 bytes, MD5 7b4062371133a07e373900cde8c42b15, checked
15	on loading), the zip directories of the eleven zip files (their central directories only, not
16	their contents), and the first 200 kB of the first ABF file of 941_003.zip and 941_006.zip and of
17	901_046_0006.abf in 901_046.zip, for their headers. Those partial reads have no MD5 to check.
18	
19	**What the record holds.** `evoked_data.mat` holds the sorted PD, LG and DG spike times, the saline
20	temperature and a stimulation mask (1 kHz) of the ten evoked preparations of the paper's second set
[... 748 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 769,
 "limit": 850
}
```

```
769	--OUT--
770	--- LG bursts: code, 7 ISIs; 64 stretches from 10 preparations
771	 T  stretches  preps  seconds_with_data  mean_period_0_60s  mean_period_540_600s  slope_s_per_s      r
772	 7         10      9                601            15.3992               19.6416         0.0060 0.6511
773	 9          2      2                601             8.7769               10.3877         0.0008 0.1692
774	11         17     10                601            11.1177               15.0117         0.0059 0.8031
775	13          2      2                601             6.8318                8.1445        -0.0006 0.1221
776	15         11     10                601             7.5635               11.4662         0.0059 0.8178
777	17          2      2                450             7.6063                   NaN         0.0031 0.3398
778	19         11     10                601             6.6657               10.1239         0.0058 0.6714
779	21          8      8                601             6.9069               15.7133         0.0171 0.8668
780	23          1      1                160             4.0949                   NaN         0.0267 0.7733
781	positive slope at 8 of 9 temperatures
782	--- LG bursts: Methods, 5 spikes; 64 stretches from 10 preparations
783	 T  stretches  preps  seconds_with_data  mean_period_0_60s  mean_period_540_600s  slope_s_per_s      r
784	 7         10      9                601            15.3992               19.4066         0.0058 0.6290
785	 9          2      2                601             8.7769               10.3877         0.0008 0.1692
786	11         17     10                601            11.0951               15.8418         0.0070 0.8441
787	13          2      2                601             6.8318                8.1445        -0.0006 0.1221
788	15         11     10                601             7.5635               11.7020         0.0064 0.8721
[... 827 more lines not kept]
```

**Agent**

Notebook, helper and claims read. Now checking the paper text on a few points (fig3 count, Q10 method, Figure 6c) and testing helper functions.

**Agent calls Bash**

```bash
cd  grep -n -i -E "9 of 10|Q 10|Q10|spike probability|spontaneous and evoked|four preparations|evoked gastric rhythms across|until no" paper/*.txt | cut -c1-700
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -o -E ".{300}7 to 21.{300}" paper/*.txt; sed -n 213,220p paper/*.txt | cut -c1-1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -o -E ".{200}(nine of|9 of|of 10 prep|of ten).{200}" paper/*.txt; grep -c "" paper/*.txt; sed -n 60,70p paper/*.txt | cut -c1-2500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, stg
from scipy import stats
# bursts: 3 bursts of 5,6,4 spikes separated by 2 s gaps
s=[]; t=0
for n in (5,6,4):
    s+= list(t+np.arange(n)*0.1); t+=3
s=np.array(s)
print(stg.bursts(s,1.0,5,"spikes"))
print(stg.bursts(s,1.0,5,"isis"))
# rayleigh vs formula & uniform
rng=np.random.default_rng(0)
ph=np.r_[rng.vonmises(0,2,40)/(2*np.pi)%1]
p,z=stg.rayleigh(ph); r=np.abs(np.mean(np.exp(2j*np.pi*ph))); print(p,z,40*r**2)
try:
    from astropy.stats import rayleightest; print(rayleightest(ph*2*np.pi))
except Exception as e: print("no astropy")
# KS asymptotic vs scipy
a=rng.random(300); b=rng.random(100)**1.3
print(stg.ks_2samp_asymp(a,b), stats.ks_2samp(a,b,method='asymp'))
# measure_phase
prep={"temperature":np.full(100000,11.0)}
pdst=np.arange(0,90,1.0); b={"PD":{"starts":pdst,"periods":np.append(np.diff(pdst),np.nan)}}
print(stg.measure_phase(prep,b,np.array([5.5,10.25,20.75,30.5,40.1])))
# integer coupling: PD period 1, LG starts every 10.3 s
lg=np.arange(0.2,80,10.3); bb={"PD":{"starts":pdst},"LG":{"starts":lg,"periods":np.append(np.diff(lg),np.nan)}}
ic=stg.integer_coupling(prep,bb,"LG"); print(ic["ratio"], ic["rem"])
# integerness on uniform vs integer
print(stg.integerness(rng.random(40),rng), stg.integerness(np.full(40,0.02)+rng.random(40)*0.05,rng))
# q10_methods: f doubles per 10 C
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
cd  ls ~/.local/bin 2>/dev/null; which uv pip pip3 python3; python3 -m pip --version 2>&1 | head -1
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
pip 26.3 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy scipy h5py fsspec astropy 2>&1 | tail -2; python -c "import numpy, scipy; print(numpy.__version__)"
```

```
2.5.5
Shell cwd was reset to
```

**Agent**

Environment ready; running synthetic tests of the helper functions.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, stg
from scipy import stats
s=[]; t=0
for n in (5,6,4):
    s+= list(t+np.arange(n)*0.1); t+=3
s=np.array(s)
print("spikes", stg.bursts(s,1.0,5,"spikes"))
print("isis", stg.bursts(s,1.0,5,"isis"))
rng=np.random.default_rng(0)
ph=rng.vonmises(0,0.5,40)/(2*np.pi)%1
p,z=stg.rayleigh(ph); r=np.abs(np.mean(np.exp(2j*np.pi*ph))); print("rayleigh",p,z,40*r**2)
from astropy.stats import rayleightest; print("astropy",rayleightest(ph*2*np.pi))
a=rng.random(300); b=rng.random(100)**1.3
print(stg.ks_2samp_asymp(a,b), stats.ks_2samp(a,b,method='asymp'))
prep={"temperature":np.full(100000,11.0)}
pdst=np.arange(0,90,1.0); b={"PD":{"starts":pdst,"periods":np.append(np.diff(pdst),np.nan)}}
print(stg.measure_phase(prep,b,np.array([5.5,10.25,20.75,30.5,40.1])))
lg=np.arange(0.2,80,10.3); bb={"PD":{"starts":pdst},"LG":{"starts":lg,"periods":np.append(np.diff(lg),np.nan)}}
ic=stg.integer_coupling(prep,bb,"LG"); print(ic["ratio"].round(3), ic["rem"].round(3))
print(stg.integerness(rng.random(40),rng), stg.integerness(0.02+rng.random(40)*0.05,rng))
# q10: temperature ramps, f = 2^((T-11)/10)
T=np.repeat(np.arange(7,22,2.0),200*1000)  # 200 s per step
prep={"temperature":T}
st=[];tt=0.0
while tt< len(T)/1e3-5:
    Tc=T[int(tt*1e3)]; per=1/(2**((Tc-11)/10)); st.append(tt); tt+=per
st=np.array(st); bq={"PD":{"starts":st,"periods":np.append(np.diff(st),np.nan)}}
print("q10", stg.q10_methods(prep,bq,"PD",5)[0], stg.q10_code(prep,bq,"PD",5))
EOF
```

```
spikes {'starts': array([3.]), 'ends': array([3.5]), 'periods': array([nan]), 'n': array([6])}
isis {'starts': array([3.]), 'ends': array([3.5]), 'periods': array([nan]), 'n': array([6])}
rayleigh 0.2710465643112816 1.3111314697625733 1.3111314697625733
astropy 0.2710660247597072
(0.1833333333333334, 0.01106231407688173) KstestResult(statistic=np.float64(0.18333333333333335), pvalue=np.float64(0.0111650106053633), statistic_location=np.float64(0.5568705605309892), statistic_sign=np.int8(-1))
(array([ nan, 0.25, 0.75, 0.5 ,  nan]), array([nan, 11., 11., 11., nan]))
[10.3 10.3 10.3 10.3 10.3 10.3 10.3  nan] [0.3 0.3 0.3 0.3 0.3 0.3 0.3 nan]
0.05274173408456621 0.019446322472777153
q10 2.0000000000000204 1.9989247311828175
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, stg
s=[]; t=0
for n in (3,5,6,5,3):
    s+= list(t+np.arange(n)*0.1); t+=3
s=np.array(s)
for c in ("spikes","isis"): print(c, stg.bursts(s,1.0,5,c))
EOF
```

```
spikes {'starts': array([3., 6., 9.]), 'ends': array([3.4, 6.5, 9.4]), 'periods': array([ 3.,  3., nan]), 'n': array([5, 6, 5])}
isis {'starts': array([6.]), 'ends': array([6.5]), 'periods': array([nan]), 'n': array([6])}
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 60 https://zenodo.org/api/records/3924718 | $TMPDIR/v/bin/python -c "
import json,sys; r=json.load(sys.stdin); m=r['metadata']
print(m['title']); print(m.get('description','')[:400]); print([ (f['key'],f['size']) for f in r['files']]); print(r.get('versions'), m.get('related_identifiers'))"
for z in 941_006 941_003 901_086; do echo "== $z"; curl -s -m 120 "https://zenodo.org/records/3924718/preview/$z.zip?include_deleted=0" | grep -o -E '[A-Za-z0-9_./ -]+\.(mat|txt|csv|crab|m)' | sort -u | head -40; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -m 120 "https://zenodo.org/records/3924718/preview/941_006.zip" -o p6.html; $TMPDIR/v/bin/python - <<'EOF'
import re,html
t=open('/tmp/claude-1001/p6.html').read()
items=re.findall(r'<span[^>]*>\s*([^<]+?)\s*</span>',t)
items=[html.unescape(i) for i in items if not i.endswith('.abf')]
print(len(t)); print([i for i in items if '.' in i or '/' in i][:60])
print(re.findall(r'\.abf',t).__len__())
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o -E '>[^<>]{2,80}<' p6.html | grep -v '\.abf' | sed -n 1,200p | tr '\n' ' ' | cut -c1-3000
```

```
>Preview< > 941_006.zip< >941_006 < > .DS_Store< >12.3 kB< > 5aab4127ba9d95057ca00665573808b4.snr< >51.4 kB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >38.4 MB< >37.8 MB< >network < >dgn < > 58b13283442bba1cb7884aace585d7f1.mat< >295.6 kB< >lgn < > 58b13283442bba1cb7884aace585d7f1.mat< >302.7 kB< >lvn < > 5424b5a192928c4b89c3a183b253cb75.mat< >295.5 kB< >mvn < >ogn < >pdn < > 58b13283442bba1cb7884aace585d7f1.mat< >295.8 kB< >temperature < >__MACOSX < >941_006 < > ._.DS_Store< >120 Bytes<
Shell cwd was reset to
```

**Agent**

**A. Outcomes**

The claims file has 22 claims. The notebook tests 17 and treats 5 as blocked. My tally: 10 reproduced, 4 partially reproduced, 3 not reproduced, 5 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| fig2-spontaneous-11-to-30 | blocked (data_missing) | The spontaneous set (Haddad & Marder 2018) is not in the record. Its 12 files are evoked_data.mat, the evoked-prep zips, and 941_003/941_006 (June 2019). |
| fig2a-less-regular-at-high-temperature | blocked (data_missing) | Same as above. 830_116_2 is not in the record. |
| fig3-evoked-7-to-21-in-9-of-10 | reproduced (on the criterion's literal wording) | Cell 16 reports 8 of 10, failing 901_062 and 901_086. But the code also requires bins 7 and 21 to be present, which the criterion does not ask. 901_062 never reaches 21 C (0 s, T_max 19.3) and has bursts in every bin it was held at, so the literal reading gives 9 of 10. If 21 C must be reached, it is 8 of 10, which would fail the tolerance of 0. 10 evoked preparations: exact. |
| fig3s1-spontaneous-and-evoked-similar | blocked (data_missing), partly testable | 941_006.zip holds only raw ABF files and crabsort classifier files (network/dgn, lgn, lvn, pdn), with no spike times. The other three preparations (901_062, 901_080, 901_086) are in evoked_data.mat and could have been tested. |
| fig4b-periods-decrease-all-preps | reproduced | Cell 19: 10 of 10 under both readings and both burst rules. |
| fig4c-q10-about-2 | not_reproduced | Cell 22, main (Methods) Q10: 1–3 of 10 have both Q10s in range, under both ranges and both the all-bins and held-steps variants. Only the code's per-burst variant with range (b) gives 8 of 10. |
| fig4c-q10-pd-lg-not-different | reproduced | Cell 24: p = 0.190 (all bins) and 0.479 (steps), both ≥ 0.05. The code rule with the code Q10 gives t = 1.272, p = 0.235, exactly the paper's values. |
| fig4s1-slowdown-after-stimulation | reproduced | Cell 26: positive slope at 8 of 9 temperatures under both burst rules. |
| fig4s2-gastric-without-pyloric-pacemaker | blocked (data_missing) | The 2020 PD-hyperpolarization set (999_017) is not in the record. |
| fig4s2-rhythm-counts | blocked (data_missing) | Same as above. |
| fig5a-example-ratios | reproduced (fragile) | Cell 28, reading (a): 10.96 at 7 C and 10.87 at 23 C, both within 10% of the labels and within 0.2 of an integer. At 7 C the "closest" cycle is a near-tie (T_LG 9.244 vs 9.245, ratios 10.96 vs 10.02), and the one chosen reads as ~11 where the paper says ~10. Reading (b) fails at 23 C (median 14.0). |
| fig5d-lg-pd-integer-coupled | reproduced | Cell 30, Methods rule, code shuffle: every bin from 7 to 21 C has p < 0.0056 and D ≥ 0.223 > 0.216. This is stable across 5 seeds. The paper's p < 1e-5 is missed at 17, 19 and 21 C (p up to 4.9e-4). |
| fig5d-dg-pd-not-coupled | reproduced | Cell 33, code shuffle: no bin with p < 0.0056 (smallest p 0.082) across 5 seeds. In the permutation variant, 11 and 15 C are significant. |
| fig5e-lg-area-exceeds-dg | partially_reproduced | Cell 35: LG > DG in 8/8 bins, which holds. The DG ± SEM interval overlaps the shuffled interval in only 1/8 bins (1–4 across seeds), never "most". |
| fig5f-ratio-independent-of-temperature | reproduced | Cell 37: Methods rule p = 0.311 (n = 3850). Code rule p = 0.880 with n = 3799, exactly the paper's values. |
| fig5f-ratio-range | not_reproduced | Cell 39: the 2.5th percentile is 7.03–7.04 under both readings, above 5.5. The upper end (26.0) passes. |
| fig6b-lg-phase-locked | partially_reproduced | Cell 41, sample (a): all 41 combinations have p < 0.05 (max 0.008). Four fail p < 4.4e-4, and z min is 4.74 < 6.75. Variant (b) with the code rule gives z 7.49–45.44, max p 4.5e-4, which matches the paper's numbers. |
| fig6b-lg-start-counts | partially_reproduced | Cell 43, Methods rule: LG 3908 (in tolerance) and fraction 0.339 (in tolerance), but DG 3573 exceeds 3228 + 322.8. With the code rule all three pass, and pooling temperatures with ≥ 100 gives exactly LG 3816. |
| fig6b-lg-phase-constant | partially_reproduced | Cell 45: no trend (p = 0.651 / 0.289; code rule rho = −0.310, p = 0.456, exactly the paper). But bin means of 0.416–0.494 (all starts) and 0.337–0.504 (first 40) put 4–6 bins outside 0.45–0.55. |
| fig6c-lg-spiking-drops-near-pd-end | not_reproduced | Cell 47: the value at 23 C is < 1, but the Spearman rho with temperature is positive (+0.15 / +0.17; +0.64 without 23 C) under both readings. The dip near PD end gets shallower from 7 to 21 C. |
| fig6e-dg-not-phase-locked | reproduced | Cell 49: p ≥ 0.05 in 16 of 35 combinations. Median DG z is 3.4 against LG 22.6. The DG ranges (p down to 1.4e-8, z up to 16) exceed the paper's ranges, which the claims file already notes are inconsistent with each other. |
| fig6f-dg-spiking-no-drop | reproduced | Cell 51: holds at 8 of 8 temperatures (DG 0.89–1.09). |

**B. Problems**

1. [affects a conclusion] Cell 16, `evoked_7_21`: the code requires `{7, 21} ⊆` held bins with a rhythm. The criterion only asks for a rhythm in "every bin the preparation was held at". This added requirement is not stated as an assumption, and the notebook's headline 8 of 10 depends on it. The literal criterion gives 9 of 10 (901_062 is never at 21 C). Both counts should be reported. The Methods' "in some preparations, 19°C was the warmest" fits two preparations topping out at 19 C.
2. [affects a conclusion] fig3s1 is marked blocked as a whole, but three of its four preparations (901_062, 901_080, 901_086) have LG spike times in evoked_data.mat. Their spontaneous (before first stimulation, 11 C) and evoked LG periods, means ± SD, could be tested. The count of evoked preparations with pre-stimulation LG bursting at 11 C could also be tested. Only 941_006 has no spike times; its zip has only raw ABF files and classifier .mat files, as I checked in the Zenodo preview.
3. [affects a conclusion; a claims-file issue, reported not corrected] The paper's own statistics match the code variants exactly, not the Methods readings the claims file makes main:
   - t = 1.272, p = 0.235: code rule with per-burst Q10.
   - n = 3799, p = 0.88: code rule.
   - LG 3816: code rule, pooled over temperatures with ≥ 100 starts.
   - rho = −0.310, p = 0.456: code rule, all starts.
   - z 7.49–45.44: code rule, first 50.

   This is strong evidence the figures were produced with crabsort's ISI-count rule (≥ 6 spikes) and the code's sampling. fig4c-q10-about-2 is not reproduced only under the Methods Q10; the code variant gives 8 of 10. Under the code variants, fig6b-lg-start-counts would be reproduced, and so would fig6b-lg-phase-locked: the code-rule first-50 numbers match the paper's figures, though one p is 4.5e-4 against the 4.4e-4 cutoff.
4. [affects a conclusion; a claims-file issue] In fig5d-lg-pd-integer-coupled, the "reproduced" clause (p < 0.05/9, D > 0.216) contradicts the "partial" clause ("some D or p miss the reported bounds", where the reported bound is p < 1e-5). No reading meets both p < 1e-5 and D > 0.216 in every bin: the draw shuffle misses p at 17–21 C, and the permutation misses D at 21 C. I applied the explicit reproduced clause.
5. [does not affect a conclusion] `stg.q10_methods` uses the bin centre for T, not the measured temperature. For the 9 and 13 C pass-through bins the exponent is 5, which produces LG Q10s of 98 and 181 from 1–2 bursts. The held-steps reading mitigates this, and the outcome is the same either way.
6. [does not affect a conclusion] Cell 26 and `phase_tables`/`spike_pdf_table` keep only odd rounded temperatures, so stretches or events at even rounded temperatures are silently dropped. How many are dropped is not printed.
7. [does not affect a conclusion] Cell 43: the fraction under reading (a) is taken over combinations with at least one start (0.339). Over all 90 combinations it would be 0.544. The author chose this without stating it as an assumption, though both are shown.
8. [does not affect a conclusion] Cell 35: preparation-bins with a single preparation get SEM 0, so overlap there is a point test. This makes "overlaps" harder to meet at 13 and 17 C.
9. I tested the helpers on synthetic inputs and they behave correctly: `bursts` (5- vs 6-spike rule), `rayleigh` (matches astropy p, z = nR²), `ks_2samp_asymp` (matches scipy asymp), `measure_phase`, `integer_coupling`, `integerness`, `q10_methods`/`q10_code` (Q10 = 2.000 on a synthetic Q10 = 2 rhythm). The data checks (cells 7–13: clock alignment, duplicate recordings, preparation identity) are sound.

**C. Not checked**

- I did not read crabsort `computePeriods` or the gastric repo, so the ISI-count burst rule rests on the helper's description. The exact matches in problem 3 support it.
- I could not check whether 901_062's run stopped at 19 C because no rhythm could be evoked at 21 C. A printout of 901_062's stimulation blocks and temperatures at the end of the recording would help.
- For fig3s1, the notebook would need per-preparation LG burst counts and periods before the first stimulation at 11 C, for all ten preparations.
- For fig5e, which shuffle `plotIntegerCoupling.m` uses for the area (one pooled permutation vs independent draws) cannot be confirmed without the code. A run with independent draws would show whether the overlap result depends on it.
- The number of stretches and events dropped by the odd-temperature filter (problem 6) is not printed.
- I did not view the notebook's figures (cells 20 and 37), only their printed ranges.

## End of run

18 turns, 5 minutes, $1.61 at API prices, result: success.
