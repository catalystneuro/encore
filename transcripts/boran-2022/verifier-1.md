# 000575 · verifier-1 · run 41132554087

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 308
drwxr-xr-x 6 runner runner    4096 Oct 30 21:58 .
drwxr-xr-x 7 runner runner    4096 Oct 30 21:58 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:38 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:38 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 21:58 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 21:58 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:38 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:38 .github
-rw-r--r-- 1 runner runner       0 Oct 30 21:58 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:38 .idea
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuroimage.2022.119123.yaml"
}
```

```
1	# Claims for Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022), NeuroImage 254, 119123, on
2	# dandiset 000575.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (paper/10.1016-j.neuroimage.2022.119123.txt, extracted from the
7	# publisher PDF), with its Methods, Results, figure legends and Table 1. The paper has no
8	# supplement and cites none. Figures 2c, 2d, 3b and 4d were read from the PDF for the per-region
9	# counts and accuracies that the text does not print.
10	#
11	# Code read: the paper's Data and code availability names one repository,
12	# https://gin.g-node.org/USZ_NCH/Human_MTL_units_visual_WM. GIN did not answer from this run;
13	# its listing was read from the Internet Archive snapshot of 2026-10-15 (head commit
14	# 5ccc2377802efec9522e3c3baa0e600419ee4383, data files at commit 798bf013ee). It holds the 16
15	# session files (Data_Subject_XX_Session_YY.h5, NIX format), a README and a LICENSE. The README
16	# describes a code_MATLAB folder with a data-loading example script only, and that folder is not
17	# on master. No analysis code is published, so no method detail below is settled by code. The
18	# dandiset is a variant form of this GIN repository (its related resources say so).
19	# The Methods say the recording scheme and non-task-specific analyses are "identical to Boran
20	# et al. (2019)" and that dPCA methods were adapted from Kaminski et al. (2017). Neither paper is
[... 812 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "mtl_wm.py"
}
```

```
1	"""Loading and per-neuron measures for dandiset 000575 (human MTL neurons, visual working memory).
2	
3	Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022), NeuroImage 254, 119123,
4	doi:10.1016/j.neuroimage.2022.119123.
5	
6	Each NWB file holds one session: a trial table (start and stop, set size, the correct answer), the
7	participant's answer per trial (`processing/behavior/BehavioralEvents.response`), the task epochs,
8	and a Units table of sorted units with spike times, the electrode (microwire label) of each unit,
9	and the mean and standard deviation of its waveform. Files are streamed from the archive at the
10	pinned version with remfile and h5py; nothing is written to disk. The LFP is not read.
11	
12	Where the parameters come from:
13	
14	- Periods, relative to trial start (the onset of the 900 ms fixation period): fixation 0 to 0.9 s,
15	  encoding 0.9 to 1.7 s, maintenance 1.7 to 2.6 s, test 2.6 to 4.6 s. These are the durations of
16	  the claims file's opening comment (Methods 2.2 and 2.3); the notebook checks them against the
17	  epochs table of every file.
18	- Region of a unit: the claims file (neurons-recorded) names two readings. `region_of` gives
19	  reading (b), the electrode name of the unit's microwire bundle, AH and PH hippocampus, EC
20	  entorhinal cortex, A amygdala (Table 1 legend). Reading (a), the anatomical location of the
[... 363 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_boran_2022.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'=== [{i}] {c[\"cell_type\"]} ===')
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT(data)--'); print(''.join(d['text/plain'])[:6000])
                if 'image/png' in d: print('[image]')
            elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1774 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 600
}
```

```
1	57
2	=== [0] markdown ===
3	# Reproducing Boran et al. (2022) from dandiset 000575
4	
5	**Paper.** Boran E, Hilfiker P, Stieglitz L, Sarnthein J, Klaver P (2022). Persistent neuronal firing
6	in the medial temporal lobe supports performance and workload of visual working memory in humans.
7	*NeuroImage* 254, 119123. [doi:10.1016/j.neuroimage.2022.119123](https://doi.org/10.1016/j.neuroimage.2022.119123).
8	The claims file was written from the version of record (Methods, Results, figure legends and
9	Table 1; the paper has no supplement) and is `claims/000575/10.1016-j.neuroimage.2022.119123.yaml`.
10	
11	**Dandiset.** [DANDI:000575](https://dandiarchive.org/dandiset/000575/0.231010.1811), version
12	0.231010.1811 (doi:10.48324/dandi.000575/0.231010.1811). The paper cites no version of the
13	dandiset (its data statement names the GIN repository USZ_NCH/Human_MTL_units_visual_WM, of which
14	the dandiset is a converted form). 0.231010.1811 is the only published version; the draft lists the
15	same 18 assets with the same total size. The files are streamed; nothing is downloaded.
16	
17	**What it holds.** 18 NWB files for 16 sessions of 13 participants (two pairs of files of
18	participant 12 are copies): trial tables with set size and the correct answer, the answer per
19	trial, task epochs, 809 sorted units with spike times inside the trial windows and their mean
20	waveforms, and, in 12 files, LFP (not used).
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 600,
 "limit": 600
}
```

```
600	        x = t[t.set_size == n_items]
601	        H = (~x[~x.solution_same].answer_same).mean()      # change trials answered "different"
602	        FA = (~x[x.solution_same].answer_same).mean()      # no-change trials answered "different"
603	        rows.append({"key": s["key"], "participant": int(s["subject"]), "N": n_items, "H": H, "FA": FA,
604	                     "KP": (H - FA) * n_items / (1 - FA), "KC": (H - FA) * n_items})
605	K_tab = pd.DataFrame(rows)
606	print(K_tab.pivot(index="key", columns="N", values="KP").round(2).to_string())
607	sess = K_tab.groupby(["key", "participant"]).agg(Kmax=("KP", "max"), KC_max=("KC", "max")).reset_index()
608	sess["KC_6"] = K_tab[K_tab.N == 6].set_index("key").KC.reindex(sess.key).values
609	part = sess.groupby("participant")[["Kmax", "KC_max", "KC_6"]].mean()
610	def summ(x):
611	    return f"median {np.median(x):.2f}, range {np.min(x):.2f} to {np.max(x):.2f}"
612	for name, tab in [("(a) per participant (13)", part), ("(b) per session (16)", sess)]:
613	    print(f"\n{name}: KP (Kmax) {summ(tab.Kmax)}; KC (i) max over set sizes {summ(tab.KC_max)}; KC (ii) set size 6 {summ(tab.KC_6)}")
614	print("\nFalse alarm rates, range over sessions and set sizes:", K_tab.FA.min().round(3), "to", K_tab.FA.max().round(3))
615	--OUT--
616	N         1     2     4     6
617	key                          
618	P01S1  0.96  1.81  2.41  1.64
619	P02S1  0.95  1.91  2.18  2.25
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1200,
 "limit": 600
}
```

```
1200	        sub.append(hipp_counts(paired, masks, rng, col))
1201	    print(f"{name}: hippocampal maintenance neurons, correct {n_c}, incorrect {n_i}; difference {n_c - n_i}, "
1202	          f"null (correct/incorrect labels shuffled within session, {N_REP}) median {np.median(null):.0f}, "
1203	          f"95th pct {np.percentile(null, 95):.0f}, p = {p:.4f} ({time.time() - started:.0f} s)")
1204	    print(f"   reading (b) of the claim, correct trials subsampled to the incorrect count (100 subsamples): "
1205	          f"mean {np.mean(sub):.1f}, range {min(sub)} to {max(sub)}")
1206	print("Incorrect trials per session:", [int((~c).sum()) for c in cor])
1207	--OUT--
1208	(a) paired, regions (b) electrode name: hippocampal maintenance neurons, correct 47, incorrect 13; difference 34, null (correct/incorrect labels shuffled within session, 499) median 31, 95th pct 39, p = 0.3280 (9 s)
1209	   reading (b) of the claim, correct trials subsampled to the incorrect count (100 subsamples): mean 12.6, range 5 to 25
1210	
1211	--OUT--
1212	(b) unpaired, regions (b) electrode name: hippocampal maintenance neurons, correct 42, incorrect 13; difference 29, null (correct/incorrect labels shuffled within session, 499) median 28, 95th pct 35, p = 0.4980 (24 s)
1213	   reading (b) of the claim, correct trials subsampled to the incorrect count (100 subsamples): mean 11.5, range 5 to 22
1214	
1215	--OUT--
1216	(a) paired, regions (a) tip location: hippocampal maintenance neurons, correct 57, incorrect 19; difference 38, null (correct/incorrect labels shuffled within session, 499) median 41, 95th pct 51, p = 0.7120 (10 s)
1217	   reading (b) of the claim, correct trials subsampled to the incorrect count (100 subsamples): mean 16.9, range 7 to 29
1218	
1219	--OUT--
[... 556 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000575/versions/" | python3 -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000575/versions/0.231010.1811/assets/?page_size=200" | python3 -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Grep**

```json
{
 "pattern": "192|exclud|118 ms|ms/item|SNR|signal-to-noise|anatomical|atlas|Fig. 1 d|decod",
 "path": "paper/10.1016-j.neuroimage.2022.119123.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 440,475p paper/*.txt; sed -n 520,535p paper/*.txt; grep -n "Fig. 1\b\|Figure 1\|(c) Response\|response time" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np
med=[783.8,875.4,1005.1,1134.1]; mean=[812.4,900.8,1075.8,1187.1]
for n,v in [('median',med),('mean',mean)]:
  print(n,'slope per condition step',np.polyfit([1,2,3,4],v,1)[0],'per item',np.polyfit([1,2,4,6],v,1)[0])
import mtl_wm as m
rng=np.random.default_rng(0)
# perm_ttest calibration under null
fp=[]
for paired in [True,False]:
  x=rng.poisson(2,(150,400)).astype(float); y=rng.poisson(2,(150,400)).astype(float)
  t,p=m.perm_ttest(x,y,paired,1000,rng); print('paired' if paired else 'unpaired','FPR',np.mean(p<.05),'one-sided',np.mean((p<.05)&(t>0)))
  y2=y.copy(); y2[:, :50]+=1
  t,p=m.perm_ttest(y2,x,paired,1000,rng); print('  power on shifted units',np.mean((p[:50]<.05)&(t[:50]>0)), 'FPR rest',np.mean(p[50:]<.05))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls executed/000575-boran-2022/.venv/bin/python 2>&1; which python3 uv pip 2>&1; ls ~/.local/bin 2>/dev/null
```

```
ls: cannot access 'executed/000575-boran-2022/.venv/bin/python': No such file or directory
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy pandas scipy scikit-learn joblib h5py remfile requests 2>&1 | tail -2; python -c "import numpy, sklearn; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np
med=[783.8,875.4,1005.1,1134.1]; mean=[812.4,900.8,1075.8,1187.1]
for n,v in [('median',med),('mean',mean)]:
  print(n,'slope per condition step',round(np.polyfit([1,2,3,4],v,1)[0],1),'per item',round(np.polyfit([1,2,4,6],v,1)[0],1))
import mtl_wm as m
rng=np.random.default_rng(0)
for paired in [True,False]:
  x=rng.poisson(2,(150,400)).astype(float); y=rng.poisson(2,(150,400)).astype(float)
  t,p=m.perm_ttest(x,y,paired,1000,rng); print('paired' if paired else 'unpaired','FPR',np.mean(p<.05),'one-sided',np.mean((p<.05)&(t>0)))
  y2=y.copy(); y2[:, :50]+=1
  t,p=m.perm_ttest(y2,x,paired,1000,rng); print('  power',np.mean((p[:50]<.05)&(t[:50]>0)), 'FPR rest',np.mean(p[50:]<.05))
"
```

```
median slope per condition step 118.1 per item 68.8
mean slope per condition step 129.9 per item 75.8
paired FPR 0.0325 one-sided 0.0175
  power 1.0 FPR rest 0.03142857142857143
unpaired FPR 0.06 one-sided 0.0325
  power 1.0 FPR rest 0.07714285714285714
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dec.py <<'EOF'
import numpy as np, mtl_wm as m
rng=np.random.default_rng(1)
def make(effect):
    feats,groups=[],[]
    for s in range(8):
        nlo,nhi=rng.integers(85,100),rng.integers(60,80); n=nlo+nhi; nu=rng.integers(10,60)
        lab=rng.permutation(np.r_[np.zeros(nlo),np.ones(nhi)])
        base=rng.gamma(2,1,nu)*1.0; eff=rng.normal(0,effect,nu)
        lam=np.clip(base[None,:]+lab[:,None]*eff[None,:],0.01,None)
        X=rng.poisson(lam[:,:,None]*np.ones((1,1,3)))
        feats.append(X); groups.append([np.where(lab==0)[0],np.where(lab==1)[0]])
    return feats,groups
for eff in [0,0.5]:
    f,g=make(eff)
    for rd in ['c','d']:
        r,n=m.decode(f,g,20,20,20,rd,True,seed=3,n_jobs=1)
        print('effect',eff,'reading',rd,'acc',np.median(r).round(3),'null',np.median(n).round(3))
EOF
$TMPDIR/v/bin/python $TMPDIR/dec.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dec.py", line 1, in <module>
    import numpy as np, mtl_wm as m
ModuleNotFoundError: No module named 'mtl_wm'
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/dec.py
```

```
effect 0 reading c acc 0.5 null 0.508
effect 0 reading d acc 0.5 null 0.512
effect 0.5 reading c acc 1.0 null 0.492
effect 0.5 reading d acc 1.0 null 0.485
```

**Agent**

**Verifier report, round 1: Boran et al. (2022), DANDI:000575 version 0.231010.1811**

The claims file has 17 claims and the notebook tests all 17. None is treated as blocked.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| behavior-accuracy-by-set-size | reproduced | Cell 17: pooled 97.8/97.9/84.3/72.6%, all 88.2%, all within tolerance; order holds. F(3,45) = 89.78 against the paper's 89.79, permutation p = .0002. |
| behavior-capacity | reproduced | Cell 19, reading (a)(i): KP median 3.23 (range 2.25–5.00), KC median 3.00 (range 2.11–4.50). Per session (b)(i) also passes, and its KC range 1.92–4.50 matches the paper's. |
| table1-capacity-and-neurons | reproduced | Cell 21: all 13 Kmax values and all 13 neuron counts equal Table 1 exactly. |
| behavior-rt-set-size | partially_reproduced | Cell 23: 2678 correct trials; RT rises in 16 of 16 sessions; median-RT F = 48.47 (exact), p = .0002. No slope reading in the criterion reaches 118±11.8 (68.8–76.2 ms/item). The slope of the median RTs per set-size step gives exactly 118.1 ms (problem 2). The criterion has no partial clause. |
| neurons-recorded | partially_reproduced | Cell 25: total 809, per session 50.6 ± 25.4, range 11–96, all within tolerance. Region counts fail under both readings: (a) Ent 168 against 209, (b) Hipp 361 and Amg 226. No partial clause in the criterion. |
| spike-sorting-quality | not_reproduced | Cell 27: ISI < 3 ms is 0.79 ± 1.77% (SD outside 1.54 ± 0.154), majority below 0.5% holds (62.5%). SNR 5.93 ± 2.31 against 3.81 ± 0.82. ISI reading (i) and SNR reading (b) cannot be tested: the data hold spikes only inside trials and no sorter noise level. |
| firing-rates-by-period | reproduced | Cell 29: all five medians and ten quartiles are within 10% under both trial readings (a) and (b), with trial extent (i). |
| fig2c-maintenance-neurons | partially_reproduced | Cell 31: all regions p = .002. Counts by tip location are 62/20/16 paired (Hipp out of tolerance) and 55/19/13 unpaired (Amg out). Electrode-name counts are all off. No single reading puts all three counts in tolerance. |
| fig2d-workload-modulated-maintenance-neurons | not_reproduced | Cells 33–35: under every reading, increase and decrease counts are 0–3 per region and at null level (p = .04–1). The cluster reading gives 1/1/0. The paper reports 10, 5 and 6. |
| maintenance-neurons-correct-vs-incorrect | not_reproduced | Cell 37: correct 42–57 and incorrect 13–19 (paper 30). The difference is at null level, p = .33–.71, under all four readings; subsampling gives 11.5–16.9. |
| fig3b-test-neurons | partially_reproduced | Cell 39: main reading (a) gives 86 or 79 against 46. Reading (b) paired gives 42 in total (within tolerance) but region counts 23/10/9 or 20/18/4 are off. Every region is significant. No partial clause in the criterion. |
| fig4a-dpca-separates-set-sizes | not_reproduced | Cells 42–43: kernel (a) without regularization gives 32.9% for dPCs 2–4 and 81.4% for the first 15, both within tolerance. The shuffled-label test fails: p = .27 for dPCs 2–4, .35 for set-size variance, .53 for maintenance distance. |
| fig4b-speed-lowest-in-maintenance | reproduced | Cell 47: encoding is highest; maintenance is below encoding and test, p = .001, under both subsampling readings. Fixation is lowest, which the criterion excludes from the claim. |
| fig4c-distance-largest-in-maintenance | partially_reproduced | Cell 49: maintenance exceeds encoding (p = .001), but fixation is the largest period, so only the first condition holds. See problem 4 on what this measure reflects. |
| fig4d-decode-workload-all | not_reproduced | Cells 51–52: accuracy 0.44–0.49 under every reading combination, p ≥ .53. Leave-one-out quartiles are 0.44–0.47 against the paper's 85.7–87.6%. |
| fig4d-decode-workload-regions | not_reproduced | Cell 54: Hipp, Ent and Amg give 0.45–0.53, p ≥ .30, under both region readings. |
| decode-performance-not-significant | reproduced | Cell 56: no group reaches p < .0125 (p = .27–.77). Accuracies (0.46–0.54) are within tolerance. See problem 10 on how much weight this carries. |

Chance level: the paper's decoding chance is 50% (scrambled labels), and the notebook's scrambled medians are 0.47–0.51, so they agree.

**B. Problems**

1. [affects a conclusion] Cell 8 assigns regions by reading (a), the tip contact's atlas label. 133 units sit on tips labelled "unspecific" or "FuG", and the author's own fallback puts all of them in Hipp by electrode name. Reading (a) gives 495/168/146 and the paper gives 454/209/146. The excess and the deficit are both 41 (495 − 454 = 209 − 168), so moving 41 of the fallback units to Ent would reproduce the paper's region counts exactly. No other assignment of those units was tried. This affects neurons-recorded, fig2c, fig3b and the region decoding.
2. [affects a conclusion] Claims file, behavior-rt-set-size: all three of its slope readings regress RT on the set-size value (1, 2, 4, 6). Regressing the median RTs printed in cell 23 on the condition step (1, 2, 3, 4) gives 118.1 ms, the paper's number. The mean RTs give 129.9 ms that way. This is a misreading in the claims file; I report it and have not corrected it.
3. [affects a conclusion] Cells 13–15 test the alignment of spikes with trial labels. Every analysis that depends on per-trial labels fails, while within-trial contrasts (firing rates, maintenance and test neurons) roughly hold. Workload decoding at k = 0 is consistently below chance: 0.44–0.46 in every leave-one-out run, against a null of 0.50. On synthetic data the decoder gives 0.50 with no signal and 1.0 with signal (I tested `decode` under both readings c and d), so the decoder is sound. The label-dependent not_reproduced outcomes may therefore reflect a defect in the deposited data. The notebook leaves this open: k = 3 was chosen from the same data, the best k per session ranges from −9 to 9, and the scan has no per-session null.
4. [affects a conclusion] Cells 46 and 49, fig4c: the largest distance is in fixation, before any stimulus. Cell 43 shows the maintenance distance equals the shuffled-label null (p = .53). The "maintenance > encoding" result that earns the partial outcome therefore reflects period-dependent noise, not separation by set size.
5. [does not affect a conclusion] Cell 42: dPCs 1–4 are all time components, so the claims file's test of dPCs 2–4 against shuffled set-size labels cannot detect set-size information. The notebook's added set-size variance test covers this. Cell 41 also uses 10 ms bins where the paper uses 1 ms, which is negligible after 167–200 ms smoothing.
6. [does not affect a conclusion] Repetitions are below what the criteria specify:
   - decoding uses 50–100 runs and 100–200 nulls instead of 500 and 1000 (cells 51, 54, 56);
   - fig3b(b) uses 99 repetitions × 200 permutations (cell 39);
   - the cluster reading uses 99 shuffles (cell 34);
   - fig4b(b) uses 100 runs (cell 46).
   
   In the regional k = 3 variant (cell 54), 60 nulls make the minimum possible p .016, which is above .0125, so that variant cannot reach significance. It is a variant only.
7. [does not affect a conclusion] Cell 31: the claims file promises a check of fig2c at 5000 permutations, and the notebook does not show it.
8. [does not affect a conclusion] `welch_t` uses unequal variances. statcond's unpaired t may pool variances, which changes little in a permutation test. My synthetic test of `perm_ttest` gave false-positive rates of 0.03–0.08 and full power.
9. [does not affect a conclusion] Cells 51 and 56: the paper's 145–169 training trials equal 95% of each session's correct trials (153–178 in cell 3). That points to decoding on each session's whole unbalanced correct-trial set. Neither reading (c) nor (d) does that, and the notebook does not print the training-set size it used. Accuracy is below chance under both readings, so this is unlikely to change the outcome.
10. [does not affect a conclusion] Cell 56: the claim of absence is reproduced by a pipeline that also fails to detect workload, which the paper decodes at 87.5%. With 13 folds of one trial per label, the test has little demonstrated sensitivity, so the reproduced outcome carries little weight.
11. [does not affect a conclusion] behavior-rt-set-size, neurons-recorded, fig2c and fig3b: the criteria define no partial outcome. Partial is my judgment there, based on the parts that hold.

**C. What I could not check, and the output that would settle it**

- Whether a natural group of 41 among the 133 fallback units recovers 454/209/146. A crosstab of those units by bundle, participant and the atlas labels of their contacts 2–3 (cell 8) would show it.
- Whether spikes and labels are displaced, and from which trial on. Three outputs would settle this:
  - a per-session alignment scan with a label-permutation null;
  - the scan split by sessions with 192 trials against sessions with fewer;
  - the source's trial numbering, if the files hold it.
- The pseudo-trials per fold and the training-set size in each decoding run (cells 51, 54, 56).
- The fig2c counts at 5000 permutations (cell 31).
- The marginalization of dPCs 2–4 in the shuffled fits (cell 43).
- I did not view the plotted images; I relied on the printed ranges.
- On the archive side, version 0.231010.1811 lists 18 assets, including two pairs of identical-size sub-12 files, which agrees with the notebook. I did not stream any file.

## End of run

17 turns, 5 minutes, result: success.
