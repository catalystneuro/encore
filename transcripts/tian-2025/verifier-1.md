# 001559 · verifier-1 · run 41579632825

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 3912
drwxr-xr-x 6 runner runner     4096 Nov  3 04:51 .
drwxr-xr-x 7 runner runner     4096 Nov  3 04:51 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  3 04:40 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  3 04:40 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov  3 04:51 .claude
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.development
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.local
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.production
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.test
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .env.test.local
drwx------ 2 runner runner     4096 Nov  3 04:51 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  3 04:40 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  3 04:40 .github
-rw-r--r-- 1 runner runner        0 Nov  3 04:51 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  3 04:40 .idea
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1021-acssensors.5c01093.yaml
```

```
# Claims for Tian, Zhang, Du, Huang, Bizimana, Nishimura & Ai (2025), ACS Sensors 10(8)
# 5826-5833, on dandiset 001559.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (open access, CC-BY 4.0), as served by Europe PMC
# (PMC12351538), extracted text in paper/10.1021-acssensors.5c01093.txt: main text, Methods,
# figure legends of Figures 1 to 5 and the Discussion. No PDF was supplied, so numbers and P
# values printed only inside the figures could not be read. The Supporting Information PDF
# (se5c01093_si_001.pdf; sequence alignment, Figure S1, brightness comparisons in Figure S2,
# the HEK 293T spectrum in Figure S3, and Table S1) and Movies S1 to S3 were not in the text.
# The claims that rest on them (lysate-brightness, cell-brightness, hek-spectrum,
# table-s1-fold-gains) quote the main text and say what is missing. The findings this dandiset
# holds (Figure 4) rest on the main text, the Figure 4 legend and the Methods only.
#
# Code: the paper links no analysis code. Its data statement only names Addgene plasmids
# pcDNA3-eBRIC (#241800) and pAAV-hSyn-eBRIC (#241801). The dandiset description says it
# includes "the python scripts used for analysis and for figure generation" of Figure 4.
# Those are files of the dataset, which the reader may not open, so no code was read and
# every method below comes from the paper. If the author finds that those scripts fix a
[... 391 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat ebric.py
```

```
"""Loading and measures for the eBRIC cortical recordings of dandiset 001559.

Tian, Zhang, Du, Huang, Bizimana, Nishimura & Ai (2025), ACS Sensors 10(8) 5826-5833,
doi:10.1021/acssensors.5c01093, Figure 4.

The dandiset holds one mouse (sub-582364L) and only image series (NWB TwoPhotonSeries):

- 2025-04-07, three 40 Hz camera movies (1000 x 920 pixels, uint16), whose frames cycle
  through four exposures; laser speckle imaging (Figure 4C), as far as the data show.
- 2025-05-31, six ScanImage acquisitions of four channels each (512 x 512 pixels,
  4.228 frames/s, 1000 frames). Channel 1 is a stimulus marker (it drops from about -580 to
  about -1990 for 5 s); channels 3 and 4 carry the bioluminescence; channel 2 does not.
  These are the PMT recordings of Figure 4D, with the excitation laser blocked.
- 2025-06-09, two ScanImage stacks of four channels (1024 x 1024 pixels): a wide field of the
  window (channel 2 shows vessels, channels 3 and 4 the red expression) and a field of
  labelled cells (Figure 4B).

Files are streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:
[... 315 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_tian_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:5000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:5000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (61.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/093dcf54-c33f-420f-92d8-eb8f62b133bb/tool-results/bk7rq7fl1.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Tian et al. (2025), Figure 4, from dandiset 001559

Paper. Tian X, Zhang Y, Du H, Huang W, Bizimana LA, Nishimura N, Ai H (2025). An Enhanced Red
Bioluminescent Indicator for Responsive Detection of Physiological Calcium Dynamics in Cells and
Mice. ACS Sensors 10(8), 5826-5833.
[doi:10.1021/acssensors.5c01093](https://doi.org/10.1021/acssensors.5c01093). The claims file was
written from the version of record (open access, Europe PMC PMC12351538): main text, Methods,
legends and Discussion. The Supporting Information was not in that text; it holds nothing on
Figure 4.

Dataset. [DANDI:001559](https://dandiarchive.org/dandiset/001559/0.250902.2058), version
0.250902.2058. The paper cites no version of the dandiset (it does not name the dandiset at all;
the dandiset names the paper). This is the only published version and so the most recent one. The
draft has the same 35 assets and the same size (29.39 GB); it was last modified at publication
time, so the two do not differ in anything the analysis uses.
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/093dcf54-c33f-420f-92d8-eb8f62b133bb/tool-results/bk7rq7fl1.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Tian et al. (2025), Figure 4, from dandiset 001559
3	
4	Paper. Tian X, Zhang Y, Du H, Huang W, Bizimana LA, Nishimura N, Ai H (2025). An Enhanced Red
5	Bioluminescent Indicator for Responsive Detection of Physiological Calcium Dynamics in Cells and
6	Mice. ACS Sensors 10(8), 5826-5833.
7	[doi:10.1021/acssensors.5c01093](https://doi.org/10.1021/acssensors.5c01093). The claims file was
8	written from the version of record (open access, Europe PMC PMC12351538): main text, Methods,
9	legends and Discussion. The Supporting Information was not in that text; it holds nothing on
10	Figure 4.
11	
12	Dataset. [DANDI:001559](https://dandiarchive.org/dandiset/001559/0.250902.2058), version
13	0.250902.2058. The paper cites no version of the dandiset (it does not name the dandiset at all;
14	the dandiset names the paper). This is the only published version and so the most recent one. The
15	draft has the same 35 assets and the same size (29.39 GB); it was last modified at publication
16	time, so the two do not differ in anything the analysis uses.
17	
18	What the dandiset holds, as found below: one mouse (sub-582364L) and only image series. Its
19	description says it holds "all the raw data presented in Figure 4 of the paper, including the
20	python scripts used for analysis and for figure generation"; the raw data of Figure 4 are there
[... 729 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/093dcf54-c33f-420f-92d8-eb8f62b133bb/tool-results/bk7rq7fl1.txt",
 "offset": 750
}
```

```
750	shown as a variant on the unsmoothed signal folded on the 0.2 s pulse period. The claim depends on
751	fig4d-evoked-increase.
752	==================== 34 code
753	rows = []
754	for c in ebric.BL_CHANNELS:
755	    for s in stim_sessions:
756	        tb = trials[(s, c)]
757	        for k in "ab":
758	            for kk in (2, 3):
759	                det = tb[f"resp_{k}"] > kk * tb.baseline_sd_smoothed
760	                rows.append({"channel": c, "session": s, "assumed current": "4 mA" if s in four_ma else "2 mA",
761	                             "window": k, "k": kk, "detected": int(det.sum()), "trials": len(tb), "fraction": det.mean()})
762	single = pd.DataFrame(rows)
763	print(single.pivot_table(index=["channel", "session", "assumed current"], columns=["window", "k"], values="fraction").round(3).to_string())
764	print()
765	for c in ebric.BL_CHANNELS:
766	    s4 = single[(single.channel == c) & (single["assumed current"] == "4 mA")]
767	    pooled = s4.groupby(["window", "k"]).apply(lambda d: d.detected.sum() / d.trials.sum(), include_groups=False)
768	    print(f"channel {c}, assumed 4 mA sessions pooled, fraction detected:", pooled.round(3).to_dict(),
769	          "; min", round(float(pooled.min()), 3))
[... 175 more lines not kept]
```

## Prompt

Your response above was stopped by a safety classifier — this is not a tool or API error. The rest of it was withheld, and tool calls in it that had not finished did not run. Do not produce that content again, even reworded.

**Agent calls Grep**

```json
{
 "pattern": "whisker|25 μL|645|n = 6|moving average|region 1|speckle|three months",
 "path": "paper/10.1021-acssensors.5c01093.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001559/versions/0.250902.2058/" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('assetsSummary'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001559/versions/0.250902.2058/assets/?page_size=100" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['count']);[print(a['path'],a['size']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent**

The archive matches the notebook: 35 NWB files, one subject, and no analysis scripts. Now the paper's Figure 4 text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1021-acssensors.5c01093.txt",
 "offset": 143,
 "limit": 40
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1021-acssensors.5c01093.txt",
 "offset": 304,
 "limit": 52
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, ebric
# synthetic marker: frames at 4.228 Hz, 512 lines, pulses of exactly 5 s at known onsets
fr=4.22796; nf=1000; nl=512; lr=2173.913
ft=np.arange(nf)/fr
true_on=np.array([16.937, 40.11, 100.5])
on_frac=np.zeros(nf)
per=1/fr
for t0 in true_on:
    for i in range(nf):
        a,b=ft[i],ft[i]+per
        on_frac[i]+=max(0,min(b,t0+5)-max(a,t0))/per
x=-580+(-1990+580)*on_frac
r={"lines":np.repeat(x[:,None],nl,1),"frame_t":ft,"t":ft[:,None]+np.arange(nl)[None]/lr}
on,off,st=ebric.marker_onsets(r)
print("onset err",on-true_on,"dur",off-on)
# trial_table and peak_and_rise on synthetic response: step +10 from 2 to 6 s after onset
dt=0.0589; t=np.arange(0,240,dt); y=np.random.default_rng(0).normal(0,1,t.size)
ons=np.array([20,60,100,140,180.])
for o in ons: y[(t>=o+2)&(t<o+6)]+=10
tb=ebric.trial_table(t,y,ons); print(tb[["resp_a","resp_b"]].mean().round(2).to_dict(), "expected a=6, b=4")
g,tr=ebric.event_average(t,y,ons); print(ebric.peak_and_rise(g,tr.mean(0)), "expected rise ~1.5-2 (centered 1s smoothing), peak 2.5-5.5")
# response of 2.5 in noise sd 4 per trial ~ averaged: does rise land at onset?
y2=np.random.default_rng(1).normal(0,4,t.size)
for o in ons: y2[(t>=o+3)&(t<o+5)]+=2.5
g,tr=ebric.event_average(t,y2,ons); print("small response:",ebric.peak_and_rise(g,tr.mean(0)))
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
cd  ls /usr/bin/python3* ; which -a python python3 conda uv 2>/dev/null; pip --version 2>&1 | head -1
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent**

numpy isn't installed. I'll set up a small temporary environment with numpy, pandas and h5py, and stub out the archive imports.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && uv pip install -q -p v/bin/python numpy pandas h5py scipy 2>&1 | tail -2; v/bin/python -c "import numpy,pandas,h5py;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import sys, types
sys.modules['remfile']=types.ModuleType('remfile')
d=types.ModuleType('dandi'); da=types.ModuleType('dandi.dandiapi'); da.DandiAPIClient=object
sys.modules['dandi']=d; sys.modules['dandi.dandiapi']=da
import numpy as np, ebric
fr=4.22796; nf=1000; nl=512; lr=2173.913
ft=np.arange(nf)/fr; per=1/fr
true_on=np.array([16.937, 40.11, 100.5, 150.05])
on_frac=np.zeros(nf)
for t0 in true_on:
    for i in range(nf):
        a,b=ft[i],ft[i]+per
        on_frac[i]+=max(0,min(b,t0+5)-max(a,t0))/per
x=-580+(-1990+580)*on_frac
r={"lines":np.repeat(x[:,None],nl,1),"frame_t":ft,"t":ft[:,None]+np.arange(nl)[None]/lr}
on,off,st=ebric.marker_onsets(r)
print("onset err (s)",np.round(on-true_on,4),"dur",np.round(off-on,4))
dt=0.0589; t=np.arange(0,240,dt)
rng=np.random.default_rng(0)
y=rng.normal(0,1,t.size)
ons=np.array([20,60,100,140,180.])
for o in ons: y[(t>=o+2)&(t<o+6)]+=10
tb=ebric.trial_table(t,y,ons); print("resp means",tb[["resp_a","resp_b"]].mean().round(2).to_dict(), "expected a=6, b=4")
g,tr=ebric.event_average(t,y,ons); print(ebric.peak_and_rise(g,tr.mean(0)), "true rise 2.0 (centered smoothing -> ~1.5)")
# small response, noisy: rise time artefact?
res=[]
for seed in range(200):
    rr=np.random.default_rng(seed); y2=rr.normal(0,8,t.size)
    for o in ons: y2[(t>=o+3)&(t<o+5)]+=2.5
    g,tr=ebric.event_average(t,y2,ons); res.append(ebric.peak_and_rise(g,tr.mean(0))["rise_time_s"])
res=np.array(res); print("small noisy response, true rise 3: fraction rise<0.1 s:",(res<0.1).mean(), "median",np.median(res))
EOF
```

```
onset err (s) [0. 0. 0. 0.] dur [5. 5. 5. 5.]
resp means {'resp_a': 6.11, 'resp_b': 4.12} expected a=6, b=4
{'peak_time_s': np.float64(4.188399999999092), 'peak': np.float64(10.355768966198829), 'rise_time_s': np.float64(2.0090999999993073)} true rise 2.0 (centered smoothing -> ~1.5)
small noisy response, true rise 3: fraction rise<0.1 s: 0.03 median 3.0398499999992055
```

**Agent calls Bash**

```bash
cd $TMPDIR; id=$(curl -s "https://api.dandiarchive.org/api/dandisets/001559/versions/0.250902.2058/assets/?page_size=3" | python3 -c "import json,sys;print(json.load(sys.stdin)['results'][0]['asset_id'])"); curl -s "https://api.dandiarchive.org/api/dandisets/001559/versions/0.250902.2058/assets/$id/" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for k in ['path','variableMeasured','wasGeneratedBy','measurementTechnique','description']: print(k, json.dumps(d.get(k))[:800])"
```

Result: the fetched text is not kept.

**Agent**

# Verifier report, round 1: Tian et al. 2025 (doi:10.1021/acssensors.5c01093) on DANDI:001559 v0.250902.2058

The claims file lists 21 claims. Six are tested from the data (all Figure 4). Fifteen are blocked because their data are not in the dandiset. I took these counts from the claims file; the attempt record was not available to me.

## A. Outcomes

| Claim id | My outcome | Reason |
|---|---|---|
| fig4b-expression-healthy | reproduced | Cell 24 finds 91 to 184 bright, compact objects in the channel 4 cell stack, and the wide field shows labelled tissue around dark vessels. The notebook checks cell bodies only, not processes. "Three months after surgery" cannot be checked: the surgery date is not in the metadata, and the stacks were taken 63 days after the first recording through the window. |
| fig4c-speckle-responsive-region | blocked (metadata_insufficient) | The archive metadata confirms there are no stimulus times for the 2025-04-07 movies. However, the notebook read only the first 400 frames (10 s) of each 108 to 147 s movie, so part of the claim was never tried (problem 4). |
| fig4d-steady-baseline | partially_reproduced | Cell 29: three of four recordings have a baseline change smaller than the 4 mA mean response. Session 145053 fails narrowly: 18.34 against 17.44 on channel 4, and 17.53 against 16.61 on channel 3. Across the day, the channel 4 level rises from about 352 to 402 over all six sessions. |
| fig4d-evoked-increase | blocked (methods_underspecified) | Cell 31, channel 4: window (a) with the t-test gives 4 of 4 conditions; Wilcoxon gives 3 of 4, and window (b) gives 3 of 4 with either test. The failing condition is session 150418 (window b mean 1.0, p = 0.21 to 0.25). The criterion says readings that disagree give methods_underspecified. Channel 3 agrees. |
| fig4d-4ma-single-trials | reproduced (conditional) | Cell 34: in the assumed 4 mA sessions, 100% of trials are detected under both windows, k = 2 and k = 3, on both channels. The fraction stays above half under 5 of the 6 ways of choosing the two 4 mA sessions. The exception, at 0.278, makes the two weakest sessions the 4 mA ones, which contradicts the paper. The result depends on the unverified session-to-current assumption, and on fig4d-evoked-increase, which is blocked. The pulse-level variant (b) was not detected on channel 4 (cell 35); it does not decide the claim. |
| fig4d-electrode-timing | partially_reproduced | Cell 37: at 2 mA, 145053 has both the later peak (4.42 s against 3.60 s) and the later rise (2.54 s against 0.005 s), which formally meets the criterion (bootstrap 0.89 on channel 4, 0.98 on channel 3). But the "earlier rise" of 0.005 s comes from 150418, whose response does not pass every reading of fig4d-evoked-increase; the averaged trace is already above half its peak at onset, so this is not a rise after onset. At 4 mA the peak times tie at 3.714 s and no electrode is later on both measures. |
| fig5-bla-footshock-increase, fig5-brep-minimal, fig5-10hz-imaging, fig5-double-bric | blocked (data_missing) | The archive lists 35 NWB files from one subject, all cortical imaging; there are no BLA, footshock or camera data. For fig5-double-bric (marked with_inputs), the eBRIC value from Figure 5C is also absent. |
| fig1a-lysate-18fold, fig1b-mutations, fig1d-purified-response, fig1e-kd, lysate-brightness | blocked (data_missing) | None of the 35 assets is in vitro data. Confirmed against the archive. |
| fig2b-hela-5fold, fig2c-hek-3p5fold, fig3-neurons-7p3fold, cell-brightness, hek-spectrum, table-s1-fold-gains | blocked (data_missing) | Same: no cell-culture data in the dandiset. The description promises analysis scripts, but none are in the 35 assets. |

## B. Problems

1. **[affects a conclusion]** Cell 37 / `peak_and_rise`. The 2 mA timing result rests on a rise time of 0.005 s for 150418. That value means the averaged trace is already above half of a small peak (2.5) at onset, possibly carried over from earlier trials. Two of its trials follow the previous onset by less than 15 s (cell 32). With synthetic data the function returns the correct rise time and gives a rise below 0.1 s in only 3% of noisy runs, so the cause is in that session's data, not the code. The 4 mA comparison is a tie.
2. **[affects a conclusion]** Cell 29. The criterion compares each recording with the 4 mA response "in the same recording". Because each session holds one condition, the notebook uses a 4 mA reference from other sessions; this departure is stated and unavoidable. The first-to-last-trial measure also hides the steady rise across the day (about 50 units over six sessions, unstimulated ones included), which is larger than the 4 mA response. Whether "steady during the recording" holds depends on that.
3. **[affects a conclusion]** Cell 27. Two things are assumed and never checked: that each session is one electrode-by-current condition, and that the two strongest sessions are the 4 mA ones. The second follows the paper's wording. fig4d-4ma-single-trials and the electrode pairing in fig4d-electrode-timing depend on both. The notebook prints no per-trial amplitudes in trial order, which would show whether conditions alternate within a session.
4. **[affects a conclusion]** Cells 20 to 25, `speckle_head`. Only the first 10 s of each speckle movie was read. The time course of speckle contrast over the expression region was never looked at. Even without stimulus times, the notebook could report whether contrast shows episodic changes and how large they are, as a partial test labelled as such.
5. **[does not affect a conclusion]** `trial_table`. The baseline s.d. is taken from the 1-s centred moving average. Its last ~0.5 s therefore includes signal from after onset, which makes detection conservative. Zero padding at the recording edges (`np.convolve(mode="same")`) does not matter, since every onset is at least 13 s in.
6. **[does not affect a conclusion]** Cell 18. Channel 4 is taken as the 645/65 channel by inference from the images. Channel 3 gives the same direction of result everywhere, but within fig4d-evoked-increase its count of conditions differs under window (a) with Wilcoxon (2 of 4 against 3 of 4).
7. **[does not affect a conclusion]** Cell 24. The fig4b criterion asks for labelled cell bodies and processes, but only cell bodies are measured. Processes rest on the image as displayed.
8. **[does not affect a conclusion]** Cell 3. The stated pixel size is wrong (it implies a 14.4 µm field). The notebook notes this correctly and never uses it.
9. **[does not affect a conclusion]** I tested `marker_onsets`, `trial_table`, `event_average` and `peak_and_rise` on synthetic inputs. Onsets came out exact, durations were 5.000 s, and responses and rise times were correct.

## C. What I could not check

- **Images.** I did not view the figures in cells 17, 21, 24 or 32, so the fig4b judgement rests on the printed numbers.
- **Session 150418 around onset.** Printing the averaged trace from −2 s to +3 s, with its baseline level, would show whether its 0.005 s "rise" is carry-over from earlier trials.
- **Session-to-condition assumption.** Per-trial response values in trial order for each session would let me test one condition per session.
- **Speckle time course.** The full time course of speckle contrast over the expression region, for every movie, would let fig4c be tested in part.
- **Archive file contents.** I did not stream the NWB files, so I could only confirm the absence of stimulus or interval tables from the archive's asset metadata, not from the files themselves. A printed listing of each file's top-level groups (`stimulus`, `intervals`, `processing`) would settle it.

## End of run

17 turns, 2 minutes, $1.02 at API prices, result: success.
