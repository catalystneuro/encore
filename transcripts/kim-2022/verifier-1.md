# kim-2022 · verifier-1 · run 42764078681

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 2680
drwxr-xr-x 6 runner runner     4096 Nov 10 06:02 .
drwxr-xr-x 7 runner runner     4096 Nov 10 06:02 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 10 05:43 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 10 05:43 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov 10 06:02 .claude
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.development
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.local
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.production
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.test
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .env.test.local
drwx------ 2 runner runner     4096 Nov 10 06:02 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 10 05:43 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 10 05:43 .github
-rw-r--r-- 1 runner runner        0 Nov 10 06:02 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 10 05:43 .idea
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kim-2022.yaml"
}
```

```
1	# Claims for Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022), tested on dandisets
2	# 000489 and 000448.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md. It replaces the file written 2026-10-23 under
5	# pilot-10 for dandiset 000489 alone; ids are kept where the finding is the same.
6	#
7	# Text read. The accepted author manuscript in PubMed Central (PMC9729435, NIHMS1849847), as
8	# served by ncbi_pmc, in paper/10.1016-j.bioelechem.2022.108319.txt. It holds the main text, the
9	# Methods (sections 2.1 to 2.6), the Results (3.1 to 3.5), the Discussion and the legends of Figs.
10	# 1 to 7. It is not the version of record. The paper has no supplement (PMC marks
11	# "has-supplement no", and the text cites none). No PDF was supplied, so figures were not read and
12	# values shown only in a figure are not used. The paper links no code and no data deposit, so no
13	# repository was read.
14	#
15	# The datasets, from their titles on DANDI.
16	# - 000489, "The impact of the second phase amplitude (% to the first phase) on the electroporation
17	#   efficiency (measured as YP emission)", bovine cells. This is the title of Fig. 2A, so it is
18	#   meant to hold the experiment of Fig. 2 (Results 3.1). The claims on Fig. 2 rest on it.
19	# - 000448, "Time kinetics of the membrane potential at the cathode- and anode-facing poles of a
20	#   cell induced by a train of 5 pulses at 833 kHz", Chinese hamster. This is the title of Fig. 7,
[... 606 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kim2022.py"
}
```

```
1	"""Loading and measures for Kim et al. (2022), Bioelectrochemistry 149:108319.
2	
3	Two dandisets, streamed from the DANDI archive at pinned versions:
4	
5	- 000489: stitched two-channel images of BPAE monolayers after 5 pulses of
6	  600 ns (unipolar) or 600+600 ns (bipolar, second phase 25 to 100%) at 1 Hz
7	  (the experiment of Fig. 2). Channel index 0 is MemBrite (350/460 nm),
8	  index 1 is YO-PRO-1 (480/535 nm); this is checked in the notebook.
9	- 000448: strobe image stacks (500 frames, 25 ns apart) of FluoVolt-loaded CHO
10	  cells given trains of 5 pulses at 833 kHz (Fig. 7).
11	
12	Where each parameter comes from is said where it is defined.
13	"""
14	
15	from __future__ import annotations
16	
17	import h5py
18	import numpy as np
19	import remfile
20	import requests
[... 447 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kim_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]}')
    print(''.join(c['source']))
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d and 'image/png' not in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
                elif 'image/png' in d: print('--IMG--')
            elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1170 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown
2	# Reproducing Kim et al. (2022) from dandisets 000489 and 000448
3	
4	**Paper.** Kim V, Semenov I, Kiester AS, Keppler MA, Ibey BL, Bixler JN, Pakhomov AG (2022).
5	Action spectra and mechanisms of (in)efficiency of bipolar electric pulses at electroporation.
6	*Bioelectrochemistry* 149:108319. [doi:10.1016/j.bioelechem.2022.108319](https://doi.org/10.1016/j.bioelechem.2022.108319).
7	The claims file (`claims/kim-2022.yaml`) was written from the accepted author manuscript in
8	PubMed Central (PMC9729435); the paper has no supplement and links no code.
9	
10	**Dandisets.**
11	[DANDI:000489](https://dandiarchive.org/dandiset/000489/0.230518.1811) version 0.230518.1811 and
12	[DANDI:000448](https://dandiarchive.org/dandiset/000448/0.230421.1844) version 0.230421.1844.
13	The paper cites no version of either. Each dandiset has one published version, the one pinned;
14	the drafts list the same number of assets and bytes (18 files, 18594422294 and 3173065152 bytes)
15	and were last modified before the publication of these versions, so the published versions are
16	the most recent and match the claims file's description as well as the drafts do.
17	
18	**What the dandisets hold.** 000489 holds 17 stitched dish images of the Fig. 2 experiment
19	(BPAE cells, 5 pulses of 600 ns or 600+600 ns at 1 Hz, second phase 0, 25, 50, 75 or 100%) and one
20	sample image labelled Fig1F. 000448 holds strobe image stacks of 9 CHO cells (5 unipolar, 4
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 620
}
```

```
620	    groups = defaultdict(list)
621	    for d in dishes:
622	        groups[d["digest"][ch]].append(d["subject_id"])
623	    print(f"channel {ch}: images shared by more than one file:", [v for v in groups.values() if len(v) > 1])
624	--OUT--
625	Fig. 2 dishes per second phase amplitude (%): {0: 3, 25: 3, 50: 5, 75: 3, 100: 3}
626	other files: ['Fig1F']
627	Fig1F           ch0 median    232 max   65435 | ch1 median    232 max   65435 | digests ['729663067506', '729663067506']
628	Fig2_0_03       ch0 median    193 max   58703 | ch1 median    284 max   50356 | digests ['e27c37030680', '951013f1cb48'] | footprints 4.55 mm apart, radii [0.43, 0.72] mm | centre/far ch0 1.24 ch1 1.28
629	Fig2_0_06       ch0 median    191 max   65435 | ch1 median    263 max   65435 | digests ['d9dfad1bba31', '90c8c025a7e6'] | footprints 4.57 mm apart, radii [0.77, 0.75] mm | centre/far ch0 1.05 ch1 3.41
630	Fig2_0_07       ch0 median    193 max   65435 | ch1 median    286 max   64995 | digests ['8332b8ad3ef2', 'b13bf326c14a'] | footprints 4.44 mm apart, radii [0.69, 0.74] mm | centre/far ch0 1.13 ch1 3.40
631	Fig2_100_03     ch0 median    237 max   65435 | ch1 median    250 max   58006 | digests ['0c4da72912d5', '89b1134af0bb'] | footprints 4.51 mm apart, radii [0.76, 0.74] mm | centre/far ch0 1.20 ch1 3.41
632	Fig2_100_07     ch0 median    221 max   65436 | ch1 median    250 max   65435 | digests ['cc7a47ce1f79', '3b617d0bb622'] | footprints 4.49 mm apart, radii [0.78, 0.73] mm | centre/far ch0 1.45 ch1 5.92
633	Fig2_100_08     ch0 median    241 max   65436 | ch1 median    219 max   23985 | digests ['8ee7515e0aa6', 'ef774f0589e8'] | footprints 4.50 mm apart, radii [0.79, 0.72] mm | centre/far ch0 1.32 ch1 6.54
634	Fig2_25_04      ch0 median    247 max   65435 | ch1 median    284 max   50356 | digests ['c55963453c20', '951013f1cb48'] | footprints 4.55 mm apart, radii [0.43, 0.72] mm | centre/far ch0 1.13 ch1 1.28
635	Fig2_25_10      ch0 median    236 max   65436 | ch1 median    327 max  
[... 536 more lines not kept]
```

**Agent**

Notebook and helper read. Next I'll check the archive listings for the blocked claims and look at the footprint-detection figure.

**Agent calls Bash**

```bash
cd $TMPDIR; for d in "000489/versions/0.230518.1811" "000448/versions/0.230421.1844"; do curl -s "https://api.dandiarchive.org/api/dandisets/$d/assets/?page_size=200" | python3 -c "
import json,sys; j=json.load(sys.stdin); print(j['count']); [print(a['path'],a['size']) for a in j['results']]"; done
for d in 000548 000549 000550; do curl -s "https://api.dandiarchive.org/api/dandisets/$d/" | python3 -c "
import json,sys; j=json.load(sys.stdin); v=j.get('most_recent_published_version') or j.get('draft_version'); print('$d', v['name'], v['version'], v['asset_count'])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import json,base64,os
nb=json.load(open('reproduce_kim_2022.ipynb'))
for i in (7,11,28,32):
    for o in nb['cells'][i]['outputs']:
        if 'data' in o and 'image/png' in o['data']:
            open(os.environ['TMPDIR']+f'/c{i}.png','wb').write(base64.b64decode(o['data']['image/png']))
"; grep -n -i -E "100%|ROI|bb'|200-|Fig. 2C|6-8|unipolar pulses" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  tr '\n' ' ' < paper/*.txt | grep -o -i -E ".{300}(ROI|100% bipolar|Fig. 2C|nonlinear|Student).{300}" | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  tr '\n' ' ' < paper/*.txt | grep -o -E "Instead, the statistical significance.{400}"; tr '\n' ' ' < paper/*.txt | grep -o -E "Fig. 2\. .{1500}" | head -c 2500; echo; tr '\n' ' ' < paper/*.txt | grep -o -E "Fig. 7\. .{1200}" | head -c 1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c28.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c11.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c32.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, kim2022 as k
print('centre field', k.field_kv_cm(0,0))
# potential check: numerically integrate E along x from electrode surface to surface
x=np.linspace(-1.5,1.5,30001); E=k.field_kv_cm(x,0)  # kV/cm
print('integral V (kV)', np.trapz(E,x)/10)
img=np.full((200,200),5.0); print('square_mean const', k.square_mean(img,np.array([100,100]),np.array([0,1.]),np.array([1.,0]),20))
r=np.random.default_rng(0).normal(size=300); print('align_lag', k.align_lag(r, np.roll(r,-7)))
t=np.arange(24)*25.; v=30*(1-np.exp(-t/200)); print('charge_fit', k.charge_fit(t,v)[0]); print('discharge', k.discharge_fit(t,30*np.exp(-t/520))[0])
print(k.shift(np.arange(5.),2), k.shift(np.arange(5.),-2))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, kim2022 as k
ModuleNotFoundError: No module named 'numpy'
```

**Agent**

Numpy isn't installed here; trying a local install so I can test the helpers on synthetic inputs.

**Agent calls Bash**

```bash
cd  pip install --quiet --target $TMPDIR/py numpy scipy h5py remfile requests 2>&1 | tail -2; PYTHONPATH=$TMPDIR/py python3 -c "
import numpy as np, kim2022 as k
print('centre field', k.field_kv_cm(0,0))
x=np.linspace(-1.5,1.5,30001); E=k.field_kv_cm(x,0)
print('integral V (kV)', np.trapezoid(E,x)/10)
img=np.full((200,200),5.0); print('square_mean const', k.square_mean(img,np.array([100,100]),np.array([0,1.]),np.array([1.,0]),20))
r=np.random.default_rng(0).normal(size=300); print('align_lag', k.align_lag(r, np.roll(r,-7)))
t=np.arange(24)*25.; v=30*(1-np.exp(-t/200)); print('charge_fit', k.charge_fit(t,v)[0]); print('discharge', k.discharge_fit(t,30*np.exp(-t/520))[0])
t2=t+12.5; print('charge fit with t0 offset half frame', k.charge_fit(t, 30*(1-np.exp(-t2/200)))[0])
print(k.shift(np.arange(5.),2), k.shift(np.arange(5.),-2))
"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
centre field 15.376998099719149
integral V (kV) 5.750000006834222
square_mean const 5.0
align_lag 7
charge_fit [ 30. 200.]
discharge [ 30. 520.]
charge fit with t0 offset half frame [ 29.23656642 175.58048021]
[nan nan  0.  1.  2.] [ 2.  3.  4. nan nan]
```

**Agent calls Bash**

```bash
cd  grep -c -E "rois_fp0" reproduce_kim_2022.ipynb; grep -o -E "fp0[13]" $TMPDIR/nb.txt | sort | uniq -c
```

```
0
```

**Agent**

**A. Outcomes**

The claims file has 25 claims. I checked the blocked ones against the archive API: 000489 holds 18 files (Fig1F plus 17 Fig2 dishes), and 000448 holds 18 strobe files covering 9 cells.

| Claim | Outcome | Reason |
|---|---|---|
| fig2a-uptake-rises-with-field | reproduced | Cell 34: under the unpaired test, YP is higher at the strongest-field ROI with p<0.05 for 5/5 amplitudes (p 0.0001 to 0.044), and Spearman ρ ≥ 0.96 for every amplitude. The paired test passes only 3/5, failing for 0% and 25% where n=2 (df=1). The paper's test as written is two-sample. |
| fig2a-vertical-scales | not_reproduced | Cell 36: for 75% the largest mean is 263 a.u. and the largest mean+sem is 339 a.u., both over 250. The unit-free ratio of largest means (unipolar/75%) is 2.47, against 4.8 for the paper's axis limits. This rests on the raw counts being the paper's units, which can't be proven. |
| fig2b-exponential-same-slope | not_reproduced | Cell 38, primary reading (8 kV/cm cutoff, NLS): the exponential beats a straight line for only 3/5 amplitudes, below the required 4, while 0/4 bipolar slopes differ from unipolar. The outcome flips with the reading. At 6 or 7 kV/cm with NLS it is reproduced. With log-linear fits at 6 or 7 kV/cm, 4/4 slopes differ. |
| fig2c-max-inhibition-50-75 | partially_reproduced | Cell 40: the ordering holds at 10/10 fields, and reading (ii) gives p<0.01 at 7/10 fields. The percent is 49.3% (reading a) or 35.1% (reading b), far outside 20±2. If "the test holds" has to hold at every field, the outcome is not_reproduced. |
| fig2c-inhibition-flat-above-8-7 | reproduced (letter of the criterion, main ROI reading only) | Cell 42: under reading (a), 0/4 amplitudes differ. The differences are large, though: +33 points for 50% (p=0.07) and +51 points for 75% (p=0.15). Under the one-sided readings (b+ and b−), 1/4 amplitudes differ. |
| fig2c-weaker-at-6-7 | partially_reproduced | Cell 44: 100% passes on a valid test (per-ROI unpaired, max p=0.0215). 50% reaches p<0.01 only through the pooled unpaired test (p=1.5e-9), which treats 50 ROI values from 5 dishes as independent. Its valid tests give per-ROI max p of 0.08 to 0.10 and a pooled paired p of 0.07. |
| fig3-uptake-linear-in-pulse-number | blocked (data_missing) | Not in 000489 or 000448 (archive listing checked). DANDI:000548, "Effect of the number of pulses…", likely holds it but is outside this attempt. |
| fig3d-cancellation-independent-of-number | blocked (data_missing) | Same as fig3-uptake-linear-in-pulse-number. |
| fig4ac-ns-bipolar-20-25pct | blocked (data_missing) | Not in the two named datasets. DANDI:000549, "Effect of the pulse duration…", is a candidate. |
| fig4d-1200ns-tenfold | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig4eg-us-bipolar-30-50pct | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig4h-us-stronger-at-low-field | blocked (data_missing) | Same as fig4ac-ns-bipolar-20-25pct. |
| fig5-ns-symmetric-along-aa | blocked (data_missing) | Fig. 5 re-analyzes the Fig. 4 dishes, which are not in 000489. The aa' line can't be measured on the Fig. 2 dishes in its place, because the claim is about other pulse durations. |
| fig5-us-anode-stronger | blocked (data_missing) | Same as fig5-ns-symmetric-along-aa. |
| fig6ad-unipolar-833khz-enhanced | blocked (data_missing) | Not in the two named datasets. DANDI:000550, "Pulse repetition rate", is a candidate. |
| fig6be-bipolar-khz-less-than-1hz | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig6cf-833khz-thirtyfold | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig6cf-cancellation-stronger-at-high-field | blocked (data_missing) | Same as fig6ad-unipolar-833khz-enhanced. |
| fig1e-heating | blocked (data_missing) | Neither dataset holds thermometry photographs. Fig1F is a staining image. |
| fig7-unipolar-pole-polarization | reproduced | Cell 13: at 600 ns the cathodic pole is +22.1% (p=0.0012) and the anodic pole −20.7% (p=0.0026), ratio 0.94. This holds under all 4 pole-mask variants. n=5 cells against the paper's 18. |
| fig7-charging-time-constant | not_reproduced | Cell 15: the charging τ of 191 ns is inside tolerance. Everything else is outside: amplitude 23.2% (vs 31±3.1), discharge τ 613 ns (vs 520±52), discharge amplitude 22.7%, and pooled r 0.84 (vs 0.93). Partial credit needs both τ inside tolerance, so it fails. |
| fig7-later-pulses-same-tau-difference | partially_reproduced | Cell 17: discharge τ exceeds charging τ for 4/4 later pulses. No ratio falls in 2.25 to 2.75. Within 10% of the pulse-1 ratio (3.21): 2/4 pulses with the free-start form, 0/4 with the criterion's A(1−exp) form. |
| fig7-bipolar-overshoot | reproduced | Cell 19: (i) bipolar and unipolar don't differ at 600 ns (21.5 vs 22.1%, p=0.86); (ii) the bipolar trace returns sooner (50% decay at 150 vs 475 ns); (iii) the bipolar minimum is −8.1% (p=0.0012). n=4 bipolar cells against the paper's 17. |
| fig7-bipolar-alternation | reproduced | Cell 21: 5/5 pulses have a significant positive end of phase 1 and a significant negative minimum in phase 2. |
| fig7-summation-without-buildup | reproduced (letter of the criterion) | Cell 23: under the unpaired test, later peaks don't differ from the first (p 0.61 to 0.75), and the pre-pulse values stay above zero (p ≤ 0.017). The paired variant does show a build-up: pulses 2 to 4 are 1.7 to 2.2 points higher with p 0.014 to 0.04, at n=5. |

No chance levels apply. The paper states none, and the analysis makes no selection against one.

**B. Problems**

1. [affects a conclusion] Cell 44, fig2c-weaker-at-6-7. The "pooled" reading runs `ttest_ind` on every dish×ROI value from 10 ROI, about 50 values from 5 dishes, as if they were independent. That is pseudo-replication, and it is the only route by which 50% reaches p<0.01. The cell also ORs together the paired and unpaired variants. The opening comment of the claims file says pairing is a method choice to adopt or block, not to OR. Part of this sits in the claims file, which permits pooling dish values: that is a statistical flaw rather than a misreading of the paper.
2. [affects a conclusion] Cells 31, 42 and 44: the low-field percents are not meaningful. The unipolar denominator at low field rests on n=2 dishes near background (19 a.u. at 2.4 mm, 7 a.u. at 3.0 mm). The bipolar groups sit at 30 to 50 a.u. at the same ROI. That gives 198% and 283% "of unipolar" at 6.7 kV/cm, meaning bipolar uptake exceeds unipolar, which is not the paper's "weaker inhibition". A per-group background offset is likely: the 0% and 25% dishes were imaged on 2021-07-29, the 75% and 100% dishes on 2021-08-24. `process_dish` computes footprint-radius variants (`rois_fp01`, `rois_fp03`), and the helper says they are "varied in the notebook", but no cell uses them.
3. [affects a conclusion] Cell 38, fig2b-exponential-same-slope. The outcome changes with the cutoff and the fit method, both open method choices, and the notebook neither adopts one with a reason nor blocks the claim as the claims file requires. The per-dish slope t-test has almost no power because unipolar has n=2 (slopes 0.205 and 0.41). The slopes of the fits to the means for 50% and 75% are 0.72× unipolar (k 0.189±0.016 and 0.191±0.014 against 0.263±0.027).
4. [affects a conclusion] Cell 42, fig2c-inhibition-flat-above-8-7. The ROI-placement reading changes the outcome: 0/4 under (a), 1/4 under (b+) and (b−). The notebook does not decide between them. In the every-pair variant, 19/180 pairs differ (10.6%), about twice the 5% expected by chance. "No difference" here comes from n=3 to 5 dishes, not from small effects.
5. [affects a conclusion] Cell 40, fig2c-max-inhibition-50-75. The notebook prints counts of fields passing (3/10 under reading i, 7/10 under reading ii) but never applies the criterion's "test holds". Whether that must hold at every field decides between partially_reproduced and not_reproduced.
6. [affects a conclusion] Cells 26 and 31: one YP image is deposited under two dishes, Fig2_0_03 (unipolar) and Fig2_25_04 (25%). Leaving both out is sensible, but it leaves the unipolar reference that every Fig. 2C percent divides by at n=2, below the paper's n=3 to 8. Separately, the 100% bipolar means exceed unipolar at most fields (93 to 139%). That conflicts with the paper's description of 100% as inhibitory. It is not a code error, but it bears on every percent claim and the notebook doesn't mention it.
7. [affects a conclusion] Cell 36, fig2a-vertical-scales. The verdict depends on the image counts being the paper's units, which the notebook assumes and says it cannot verify. The ratio check (2.47 against 4.8) points the same way, but axis limits only bound the data.
8. [does not affect a conclusion] Cell 15, `fit_pulse`. The charging window is frames 0 to 23 (0 to 575 ns), where the criterion says 0 to 600 ns. Onset is defined as the first frame above threshold, so t=0 is late by up to a frame. On synthetic data, a half-frame offset biases τ by −12%. The ±1-frame variant moves charging τ from 149 to 250 ns, so "in tolerance" isn't robust. The verdict doesn't change because discharge τ and the amplitudes fail anyway.
9. [does not affect a conclusion] Cell 17: the free-start charging form is the author's addition, not in the criterion. Both forms give partially_reproduced. The pulse-5 ratio of 2.887 sits just under the 10% bound of 2.889.
10. [does not affect a conclusion] Cells 19 and 21: the time of the minimum is chosen on the mean trace and then tested on the same cells. The effects are large (p ≤ 0.0013).
11. [does not affect the letter of the outcome] Cell 23: as the claims file prescribes, pulses within the same cells are compared with an unpaired test. With n=5, the claim of absence is weak, and the paired variant contradicts it.
12. [does not affect a conclusion] Cell 10: cathode = upper pole is inferred from FluoVolt's sign (it brightens on depolarization), not from metadata. That is reasonable and consistent across all 9 cells.
13. [does not affect a conclusion] Fig. 7 has n=5 unipolar and n=4 bipolar cells against the paper's 18 and 17, so 120 pooled points against 425. The deposit is a subset, and the notebook states this.
14. [does not affect a conclusion] Cell 0: the Fig. 3 to 6 claims are blocked because the claims file assigns them to 000489. The API shows that 000548, 000549 and 000550 exist with titles matching Figs. 3, 4 and 6. This is a scoping issue in the claims file, not a notebook error.
15. Checked and found correct:
    - `field_kv_cm`: 15.38 kV/cm at the centre, and integrating it between the electrodes gives exactly 5.75 kV.
    - `square_mean`, `align_lag`, `shift`, `charge_fit` and `discharge_fit` behave correctly on synthetic inputs.
    - The 0.65 µm pixel size is confirmed by the measured 4.51 mm electrode centre spacing.
    - The footprint overlays in cell 28 sit on the electrode footprints.
    - The 15.1/15.38 field scaling doesn't change which ROI is nearest to each named field.
    - There is no train/test split, so leakage doesn't apply.

**C. What I could not check, and what output would have let me**

- Per-dish ROI values and per-dish YP0/MB0. Printing them would show the background offset between imaging dates.
- The `rois_fp01` and `rois_fp03` results. Rerunning cells 40, 42 and 44 on them would test whether the low-field percents depend on the footprint disc.
- Fig. 2B under each cutoff and fit method. A table with a stated adopted reading and a semi-log plot of the fits would settle problem 3.
- Fig. 7 fit residuals and the overlay of the fits on the traces.
- The masks figure in cell 7. I did not look at it.
- Whether 000548, 000549 and 000550 hold the Fig. 3 to 6 data. Only their titles and asset counts were checked.

## End of run

17 turns, 4 minutes, $1.51 at API prices, result: success.
