# 001347 · verifier-1 · run 41413796706

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 1828
drwxr-xr-x 6 runner runner    4096 Nov  2 09:01 .
drwxr-xr-x 7 runner runner    4096 Nov  2 09:01 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:32 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:32 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  2 09:01 .claude
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.development
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.local
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.production
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.test
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .env.test.local
drwx------ 2 runner runner    4096 Nov  2 09:01 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:32 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:32 .github
-rw-r--r-- 1 runner runner       0 Nov  2 09:01 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 08:32 .idea
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l *.yaml paper/*.txt; head -c 6000 10.1126-science.adt3971.yaml; grep -n "^  - id\|^- id\|  id:" 10.1126-science.adt3971.yaml | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "10.1126-science.adt3971.yaml"
}
```

```
1	# Claims for Kauvar, Richman, Liu et al. (2025), Science 388, eadt3971, on dandiset 001347.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-02,
3	# protocol pilot-13 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (Science, 29 May 2025), main text with Materials and Methods,
6	# figure legends and references, and both supplement PDFs (the MDAR checklist, and the
7	# Supplementary Materials with Supplemental Note 1, the legends of figs. S1 to S38 and Tables S1
8	# to S3), all as extracted in paper/10.1126-science.adt3971.txt. No figure image could be
9	# rendered in this run, so every claim rests on the text and on Table S3. The body of Table S1
10	# (contacts with significant changes per HCP area) is garbled in the extraction and is not used.
11	# The variance-explained labels of Fig. 5G to 5I (0.954, 0.870, 0.927) are read from the
12	# extracted figure text; their assignment to panels is named as open in that claim.
13	#
14	# Code read:
15	# - Human electrophysiology and behaviour, and mouse behaviour (ref. 101): Zenodo record
16	#   14920570, kauvar-richman-liu-2025_zenodo.zip (md5 bd1fb567121aaf0291337783df57bcfc), a git
17	#   repository with one commit, b873ca5 ("First commit."). It loads its data from dandiset 001347.
18	#   Key scripts: human_ieeg/scripts/analyze_airpuff_p50.py (Fig. 1, fig. S1),
19	#   analyze_airpuff_ieeg_behavior_across_subjects.py (Fig. 2C and 2D, figs. S8 and S14G),
20	#   analyze_airpuff_ieeg_cd.py (Fig. 6C, 6E, 6G), analyze_airpuff_ieeg_sgram_load_allpt.py (Figs.
[... 692 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1126-science.adt3971.yaml",
 "offset": 712,
 "limit": 975
}
```

```
File content (32655 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "10.1126-science.adt3971.yaml",
 "offset": 712,
 "limit": 400
}
```

```
712	- id: fig3b-cluster-test-yeo-networks
713	  statement: Permutation cluster tests find ketamine-altered spectrotemporal clusters in the
714	    limbic, ventral attention and somatomotor Yeo7 networks.
715	  source: Figure 3B; fig. S21A; Table S3, Fig. 3B; Results, Brain-wide activity screen during
716	    emergence of affect in human beings, paragraph 7
717	  quote: Permutation cluster ... testing resolved ketamine-altered spectrotemporal clusters which
718	    reached statistical significance in the limbic, ventral attention, and somatomotor Yeo7
719	    resting-state networks
720	  criterion: Per participant and network, the trial spectrogram is the mean over the network's
721	    channels (only bipolar channels with both contacts in the same region); trials are stacked
722	    across participants (Frontoparietal 178, Default 214, Dorsal Attention 153, Limbic 214,
723	    Ventral Attention 214, Somatomotor 214 trials). The infusion minus preinfusion difference of
724	    trials paired by position in the puff sequence is tested with
725	    mne.stats.permutation_cluster_1samp_test, cluster-forming threshold the two-tailed t at
726	    p = 0.01, 512 permutations, seed 1, spectrogram from 0.5 s before to 1.5 s after the puff
727	    (Methods, Permutation cluster test; Table S3; code trace_utils.permutation_cluster_test and
728	    analyze_airpuff_ieeg_sgram_load_allpt.py). The lowest cluster p of each network is
729	    Benjamini-Hochberg corrected across networks; a network is significant when it is below
730	    0.01. Reproduced when limbic, ventral attention and somatomotor are significant; the result
731	    for the other three networks is reported.
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1126-science.adt3971.yaml",
 "offset": 1112,
 "limit": 575
}
```

```
1112	  - {quantity: "pre-saline", value: 0.29, tolerance: 0.08}
1113	  - {quantity: "saline", value: 0.26, tolerance: 0.06}
1114	  - {quantity: "pre-ketamine", value: 0.37, tolerance: 0.06}
1115	  - {quantity: "ketamine", value: -0.07, tolerance: 0.06}
1116	  - {quantity: "pre-PCP", value: 0.35, tolerance: 0.10}
1117	  - {quantity: "PCP", value: -0.03, tolerance: 0.05}
1118	  criterion: M-EYE on the first puff, preinfusion against infusion trials within each session,
1119	    paired t-tests across mice with Benjamini-Hochberg over the three drugs (code fig1_drugs.py,
1120	    tpuff = 0). Reproduced when, under a reading of Open I, ketamine and PCP give corrected
1121	    p < 0.05 with lower infusion values, saline gives p >= 0.05, and the means are within
1122	    tolerance; partially reproduced when the tests hold and some means do not.
1123	- id: figs2bc-mouse-ketamine-early-present-late-abolished
1124	  data: with_labels
1125	  depends_on:
1126	  - mouse-session-labels-link
1127	  statement: With ketamine, early eye closure on the first puff decreases but remains (0.78 to
1128	    0.45), while late eye closure is abolished (0.34 to -0.02), compared with saline.
1129	  source: fig. S2B and S2C; Table S3, fig. S2 B and C
1130	  quote: Early eye closure (during 0.1 to 0.2 s after puff onset) decreases with ketamine but
1131	    remains present ... closure (during 0.3 to 0.8 s after puff onset) is abolished by ketamine
[... 554 more lines not kept]
```

**Agent**

Claims file read (about 59 claims, including 5 links). Next I'm dumping the five notebooks to text so I can read the code and outputs.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/nb; python3 - <<'EOF'
import json,os
T=os.environ['TMPDIR']
for f in sorted(os.listdir('.')):
    if not f.endswith('.ipynb'): continue
    nb=json.load(open(f))
    out=[]
    for i,c in enumerate(nb['cells']):
        out.append(f"\n===== CELL {i} [{c['cell_type']}] =====\n"+''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: out.append("--- out ---\n"+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: out.append("--- out(data) ---\n"+''.join(d['text/plain'])[:5000])
                if 'image/png' in d: out.append("[image]")
            elif o.get('output_type')=='error': out.append("--- ERROR ---\n"+o['ename']+': '+o['evalue'])
    open(f"{T}/nb/{f}.txt",'w').write('\n'.join(out))
    print(f,len(nb['cells']))
EOF
wc -l $TMPDIR/nb/*; echo $TMPDIR
```

```
01_human_behavior.ipynb 35
02_mouse_behavior.ipynb 52
03_ieeg_spectral.ipynb 20
04_ieeg_cd.ipynb 35
05_mouse_npx.ipynb 36
   816 /tmp/claude-1001/nb/01_human_behavior.ipynb.txt
  1356 /tmp/claude-1001/nb/02_mouse_behavior.ipynb.txt
   870 /tmp/claude-1001/nb/03_ieeg_spectral.ipynb.txt
  1351 /tmp/claude-1001/nb/04_ieeg_cd.ipynb.txt
  1141 /tmp/claude-1001/nb/05_mouse_npx.ipynb.txt
  5534 total
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/01_human_behavior.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Kauvar, Richman, Liu et al. (2025): human eyepuff behaviour and dissociation, from DANDI:001347
4	
5	Paper: Kauvar, Richman, Liu et al., "Conserved brain-wide emergence of emotional response from sensory
6	experience in humans and mice", Science 388, eadt3971 (2025), doi:10.1126/science.adt3971.
7	
8	Dataset: [DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702), version
9	0.250528.0702. It is the only published version (28 May 2025, the day before the paper appeared); the
10	paper cites the dandiset without a version, so the latest published version is pinned. Its content
11	(207 assets, 16.0 GB) is the same size and asset count as the current draft.
12	
13	Claims file: `claims/001347/10.1126-science.adt3971.yaml`, written from the version of record with
14	its Materials and Methods, figure legends and the Supplementary Materials (Table S3).
15	
16	This notebook tests the claims on human eye closure and dissociation (CADSS). Other notebooks of the
17	entry test the mouse behaviour (02), the iEEG spectrograms (03), the iEEG coding dimension (04) and the
18	mouse Neuropixels data of DANDI:001326 (05).
19	
20	| Claim | Tested here |
[... 797 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "human_eye.py"
}
```

```
1	"""Human eye closure and CADSS for Kauvar, Richman, Liu et al. 2025 (DANDI:001347).
2	
3	Loads the eyepuff behaviour of the non-iEEG cohort (sub-h*/..._ses-P50_behavior.nwb) and of the
4	iEEG cohort (sub-SD*/..._ses-puff_behavior.nwb), streamed through dandi_io, and computes the
5	early (reflexive) and late (affective) eye closure of the claims file's method H-EYE.
6	
7	Where each parameter comes from
8	- Early window 0.1 to 0.2 s and late window 0.3 to 0.8 s after the puff: claims file, H-EYE
9	  (Fig. 1 legend, fig. S1B and S1C legends). The iEEG files also store them (ref_w, aff_w).
10	- Non-iEEG cohort: trials 3 to 40 (0-based 2 to 39), the late/early value of a participant is
11	  the mean over trials of late divided by the mean over trials of early: claims file, H-EYE and
12	  Open A reading (a), Open B reading (a). Reading (b) of Open A keeps trials 2 to 40; reading (b)
13	  of Open B takes the mean of per-trial ratios. In the P50 code the window masks are strict
14	  (tt > 0.3 and tt < 0.8; analyze_airpuff_p50.py), which is followed here.
15	- Which P50 series is saline: the files call the two series `pre_trials_data` and
16	  `post_trials_data` and do not say which visit is saline. The paper's code reads `pre` as
17	  saline and `post` as ketamine (analyze_airpuff_p50.py builds the `treatment` column so). This
18	  label comes from the code record (an outside input, with_labels; link claim
19	  p50-condition-labels-link).
20	- iEEG cohort: the per-trial late/early ratio and the trials listed in each file's
[... 184 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "dandi_io.py"
}
```

```
1	"""Streaming access to dandiset 001347 (Kauvar, Richman, Liu et al. 2025) and 001326.
2	
3	Every notebook of this entry reads the NWB files through this module. Files are
4	streamed from the DANDI Archive with remfile and h5py; nothing is written to disk.
5	
6	Version: 001347 has one published version, 0.250528.0702 (28 May 2025), the
7	day before the paper's publication (29 May 2025). The paper cites the dandiset
8	without a version, so the latest published version is pinned (protocol, author
9	step 1.3). The mouse Neuropixels data of the paper are in dandiset 001326,
10	pinned likewise at its only published version, 0.250528.1957.
11	"""
12	import functools
13	
14	import h5py
15	import remfile
16	import requests
17	
18	DANDISET = "001347"
19	VERSION = "0.250528.0702"
20	NPX_DANDISET = "001326"
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/02_mouse_behavior.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Mouse eyepuff behaviour: Kauvar, Richman, Liu et al. (2025), dandiset 001347
4	
5	Paper. Kauvar IV, Richman EB, Liu TX, et al. (2025). Conserved brain-wide emergence of emotional
6	response from sensory experience in humans and mice. *Science* 388, eadt3971.
7	[doi:10.1126/science.adt3971](https://doi.org/10.1126/science.adt3971). The claims file was written
8	from the version of record (29 May 2025) with Materials and Methods, figure legends and both
9	supplement PDFs, including Table S3.
10	
11	Dandiset. [DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702), version
12	0.250528.0702, the only published version. The paper cites the dandiset without a version, so the
13	latest published version is pinned (see `dandi_io.py`). The mouse spiking data of the paper are in
14	dandiset 001326; this notebook reads it only to count its sessions.
15	
16	What this notebook reads. The 142 head-fixed mouse behaviour files
17	`sub-mouse/sub-mouse_ses-<experiment id>_behavior.nwb` (one eye-closure trace at 200 Hz each) and
18	the 10 Neuropixels-rig behaviour files `sub-m<mouse>-<id>/..._ses-puff_behavior.nwb`.
19	
20	Outside input. The `sub-mouse` files carry no drug, dose, mouse, sex, day or pressure. The
[... 698 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "mouse_eye.py"
}
```

```
1	"""Head-fixed mouse eyepuff behaviour of dandiset 001347 (Kauvar, Richman, Liu et al. 2025).
2	
3	Two kinds of file are read, streamed through dandi_io (nothing is written to disk):
4	
5	- sub-mouse/sub-mouse_ses-<experiment id>_behavior.nwb: one TimeSeries acquisition/eye_closure
6	  at 200 Hz, trials of 81 s (16200 frames, 6 s before the first puff) concatenated, 20 or 40
7	  trials. The files carry no drug, dose, mouse, sex, day or pressure. Those labels come from the
8	  experiment lists of the paper's scripts mouse_eyepuff/scripts/fig1_*.py in the code record
9	  (Zenodo 10.5281/zenodo.14920570, kauvar-richman-liu-2025_zenodo.zip, md5
10	  bd1fb567121aaf0291337783df57bcfc, git commit b873ca5), read at run time by `code_lists`.
11	- sub-m<mouse>-<id>/..._ses-puff_behavior.nwb: Neuropixels-rig behaviour (DeepLabCut eye
12	  closure at 100 Hz, trial onsets `events-on`, `ket_trial`, stored trial ranges and windows).
13	
14	The processing reimplements ketmouse/eye_trace_utils.py of the code record (not imported):
15	
16	- `prox_norm`: each trial minus its mean over frames 0 to 399 (the first 2 s, 6 to 4 s before
17	  the first puff); eye_trace_utils.prox_norm, used with do_prox_norm=True by every fig1 script.
18	- `scale`: get_mean_traces then subtracts the mean of the first 400 frames of `baseline_trial`
19	  of the prox-normed data, which is zero, and scales by 1/(1 - that), which is one. The Methods
20	  ("Eyepuff assay (mouse)") instead scale by 1/(1 - baseline) with the raw pre-trial baseline
[... 232 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/02_mouse_behavior.ipynb.txt",
 "offset": 718,
 "limit": 640
}
```

```
718	print("late, saline infusion trials, per mouse:", R["sal"]["post_late"].round(3), "s.e.m.", round(st.sem(R["sal"]["post_late"]), 3),
719	      "median", round(np.median(R["sal"]["post_late"]), 3))
720	print("late, saline preinfusion trials of the same sessions, mean:", round(R["sal"]["pre_late"].mean(), 3))
721	print("ketamine early above zero in every mouse:", bool((R["ket50"]["post_early"] > 0).all()))
722	for (q, v, tol), x in zip(exp, s2bc[(list(READINGS)[0], "code")]):
723	    print(f"expected {q}: {v} +/- {tol}; measured {x:.3f}; within: {within(x, v, tol)}")
724	--- out ---
725	reading a (code, 6-20 / 23-37), scale code: early saline 0.778 ketamine 0.451 (t = 6.854, p = 0.0024); late saline 0.203 ketamine -0.025 (t = 4.951, p = 0.0078)
726	reading a (code, 6-20 / 23-37), scale methods: early saline 0.722 ketamine 0.463 (t = 2.873, p = 0.0453); late saline 0.186 ketamine -0.020 (t = 5.155, p = 0.0067)
727	reading b (3-20 / 23-40), scale code: early saline 0.770 ketamine 0.430 (t = 6.065, p = 0.0037); late saline 0.208 ketamine -0.024 (t = 4.908, p = 0.0080)
728	reading b (3-20 / 23-40), scale methods: early saline 0.715 ketamine 0.441 (t = 2.993, p = 0.0402); late saline 0.191 ketamine -0.020 (t = 5.164, p = 0.0067)
729	late, saline infusion trials, per mouse: [0.191 0.17  0.089 0.19  0.374] s.e.m. 0.047 median 0.19
730	late, saline preinfusion trials of the same sessions, mean: 0.24
731	ketamine early above zero in every mouse: True
732	expected early, saline: 0.78 +/- 0.05; measured 0.778; within: True
733	expected early, ketamine: 0.45 +/- 0.06; measured 0.451; within: True
734	expected late, saline: 0.34 +/- 0.07; measured 0.203; within: False
735	expected late, ketamine: -0.02 +/- 0.02; measured -0.025; within: True
736	
737	
[... 620 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/03_ieeg_spectral.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Kauvar, Richman, Liu et al. (2025): human iEEG spectral response (Figs. 2G to 2J, 3B, 3C; figs. S12, S13, S15, S27)
4	
5	Paper: Kauvar IV, Richman EB, Liu TX et al. (2025), Conserved brain-wide emergence of emotional response
6	from sensory experience in humans and mice. Science 388, eadt3971,
7	[doi:10.1126/science.adt3971](https://doi.org/10.1126/science.adt3971). The claims file
8	(claims/001347/10.1126-science.adt3971.yaml) was written from the version of record with its
9	supplementary materials.
10	
11	Dataset: [DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702), version
12	0.250528.0702, streamed. The paper cites the dandiset without a version; this is the only published
13	version (28 May 2025), so it is pinned.
14	
15	What this notebook uses: the aggregated human products in `sub-H/` (per-channel trial means split into
16	train and test halves, per-channel, per-network and per-region per-trial spectrograms), and, to compare,
17	the paper's own deposited outputs in the same folder (NMF factors and loadings, cluster-test maps). The
18	Yeo7 network of each channel is not in the dataset; it is read from the paper's code record (Zenodo
19	14920570, `anat/pts_ch_labels.pkl`) and checked against the dataset in the link claim
20	`link-ieeg-yeo-labels`. Nothing random is drawn: NMF uses random_state 1 and the cluster tests seed 1,
[... 646 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/03_ieeg_spectral.ipynb.txt",
 "offset": 666,
 "limit": 210
}
```

```
666	Ventral Attention -0.108 -0.263  0.038 -0.209 -0.096 -0.485 -0.206
667	
668	
669	===== CELL 16 [code] =====
670	t = time.time()
671	ctrl_idx = np.where(np.isin(pts, CTRL_PTS))[0]
672	Xc = np.stack([ie.read_channel_trials(s_tr, pos_tr[chs[i]], "control")[:, :, TIND].mean(0) for i in ctrl_idx])
673	print(f"read control trial means of {len(ctrl_idx)} channels in {time.time() - t:.0f} s; NaN: {int(np.isnan(Xc).sum())}")
674	Wc = ie.transform(mp, mn, Xc.reshape(len(ctrl_idx), -1))[:, ie.CODE_ORDER]
675	Wc[EXCL[ctrl_idx]] = np.nan
676	res = pd.DataFrame({"control": np.nanmean(Wc, 0), "pre (same channels)": np.nanmean(W["pre"][ctrl_idx], 0),
677	                    "pre (all channels)": np.nanmean(W["pre"], 0), "n_ch": (~np.isnan(Wc)).sum(0)})
678	res["control lower than pre (same channels)"] = res["control"] < res["pre (same channels)"]
679	res["ratio control / pre"] = res["control"] / res["pre (same channels)"]
680	print(res.round(3).to_string())
681	print("factors with lower control loading:", int(res["control lower than pre (same channels)"].sum()), "of 6")
682	print("\nmean loading by participant, control / preinfusion (same channels):")
683	cp = pts[ctrl_idx]
684	tab = pd.DataFrame({f"f{f}": [f"{np.nanmean(Wc[cp == p, f]):.2f}/{np.nanmean(W['pre'][ctrl_idx][cp == p, f]):.2f}" for p in CTRL_PTS] for f in range(6)}, index=CTRL_PTS)
685	print(tab.to_string())
[... 186 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "ieeg_spectral.py"
}
```

```
1	"""Human iEEG spectral analyses (Figs. 2G to 2J, 3B, 3C, fig. S13) of Kauvar, Richman, Liu et al. 2025.
2	
3	All spectrograms are the dataset's own aggregated products in sub-H/ of DANDI:001347
4	(read through dandi_io): per-channel trial means split into train and test halves
5	(sub-H_ses-sgramPerChannel.nwb), per-channel per-trial spectrograms
6	(sub-H_ses-sgramPerChannelPerTrial.nwb), per-network and per-region per-trial
7	spectrograms (sub-H_ses-sgramPerYeoPerTrial.nwb, sub-H_ses-sgramPerRegionPerTrial.nwb). The
8	paper's deposited outputs (NMF factors and loadings, cluster-test maps) are read only to
9	compare with the results computed here.
10	
11	Where each parameter comes from:
12	- NMF: scikit-learn NMF, solver 'mu', random_state 1, Frobenius loss, default init and
13	  iterations, 3 components on the positive part and 3 on the negative part of the
14	  pre/postinfusion training mean (claims file, Open G and fig2g criterion; code
15	  ketman/analyze/decode_utils.get_nmf and analyze_airpuff_ieeg_sgram_load_allpt.py lines
16	  381 to 389). The paper's code ran scikit-learn 1.4.1 (requirements.txt), whose default
17	  init for this shape is 'nndsvda', as in the version used here.
18	- CODE_ORDER [0, 2, 4, 5, 1, 3]: the code's fixed numbering of the fitted factors
19	  (analyze_airpuff_ieeg_sgram_load_allpt.py line 421; claims file Open G).
20	- Time bins 0 < t < 1.4 s for the NMF (same script, lines 230 to 231); -0.5 to 1.5 s for the
[... 289 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/04_ieeg_cd.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Human iEEG coding dimension, timescale and coupling: Kauvar, Richman, Liu et al. (2025), dandiset 001347
4	
5	Paper. Kauvar IV, Richman EB, Liu TX, et al. (2025). Conserved brain-wide emergence of emotional
6	response from sensory experience in humans and mice. *Science* 388, eadt3971.
7	[doi:10.1126/science.adt3971](https://doi.org/10.1126/science.adt3971). The claims file was written
8	from the version of record (29 May 2025) with Materials and Methods, figure legends and the
9	supplement, including Table S3.
10	
11	Dandiset. [DANDI:001347](https://dandiarchive.org/dandiset/001347/0.250528.0702), version
12	0.250528.0702, the only published version. The paper cites the dandiset without a version, so the
13	latest published version is pinned (see `dandi_io.py`). The mouse Neuropixels data used for
14	figs37a are in [DANDI:001326](https://dandiarchive.org/dandiset/001326/0.250528.1957), version
15	0.250528.1957, its only published version.
16	
17	What this notebook reads. For the 7 included iEEG participants (SD168, SD172, SD181, SD185,
18	SD186, SD211, SD245), the per-session files `sub-SD*/sub-SD*_ses-puff<Session>_ecephys.nwb`
19	(LFP at 200 Hz, 20 min around the eyepuff assay, an electrode table with region labels, and 20 DC
20	channels, one of which carries the puff TTL) and the behaviour files
[... 622 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/04_ieeg_cd.ipynb.txt",
 "offset": 642,
 "limit": 712
}
```

```
642	35   low gamma  methods        False     code  4.881  3.848  4.288      2.980          0.049       1.015           0.349
643	36   low gamma     code         True     none  3.431  3.062  3.278      1.163          0.524       0.676           0.524
644	37   low gamma     code         True     code  3.195  2.887  3.178      1.256          0.271       1.211           0.271
645	38   low gamma     code        False     none  3.333  2.959  3.342      1.472          0.317       1.092           0.317
646	39   low gamma     code        False     code  3.110  2.858  3.234      1.460          0.226       1.349           0.226
647	40  high gamma  methods         True     none  2.295  1.605  2.146      2.150          0.150       1.576           0.166
648	41  high gamma  methods         True     code  2.304  1.447  2.137      1.718          0.137       1.825           0.137
649	42  high gamma  methods        False     none  2.276  1.547  1.955      2.437          0.101       1.523           0.179
650	43  high gamma  methods        False     code  2.282  1.402  1.943      1.884          0.165       1.580           0.165
651	44  high gamma     code         True     none  3.723  3.979  3.836     -0.842          0.761      -0.318           0.761
652	45  high gamma     code         True     code  3.637  3.637  3.714      0.002          0.998       0.359           0.998
653	46  high gamma     code        False     none  3.768  4.099  3.952     -0.993          0.717      -0.380           0.717
654	47  high gamma     code        False     code  3.675  3.759  3.843     -0.649          0.574       0.594           0.574
655	48   broadband  methods         True     none  2.605  2.115  2.217      1.534          0.352       0.489           0.642
656	49   broadband  methods         True     code  2.607  2.114  2.249      1.702          0.279       0.736           0.490
657	50   broadband  methods        False     none  2.928  2.214  2.551      2.273          0.104       1.915           0.104

[... 695 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p ieeg_cd.py
```

**Agent calls Bash**

```bash
cd  sed -n 200,700p ieeg_cd.py
```

```
"""Human iEEG coding dimension, timescale and phase locking (DANDI:001347).

Reimplements, without importing it, the analysis of the paper's code (Zenodo
10.5281/zenodo.14920570, commit b873ca5): human_ieeg/scripts/analyze_airpuff_ieeg_cd.py,
ketman/analyze/trace_utils.py (load_raw_traces, reference, load_patients_erp,
get_erp_cd, compute_cd_cov, compute_all_cd, get_cd_timescales, extract_timescale),
ketman/analyze/cd_utils.py (plot_cd_projection_summary, plot_cd_weights, cd_pctile)
and ketman/analyze/airpuff_utils.process_led. Function docstrings cite the function
followed. Data are streamed through dandi_io; nothing is written to disk.

Where each parameter comes from
- Participants (PARTICIPANTS): the claims file header (the 7 included participants).
- Session used as "preinfusion" (PRE_SESSION_CODE): ketman/DATASETS.py, airpuff_sessions
  (SD168 and SD172 list 'baseline' first, lines 29 and 48); load_and_organize_raw_traces and
  load_patients_erp rename 'baseline' to 'preinfusion', which for SD245 (sessions
  ['baseline', 'preinfusion', ...], line 140) overwrites the Preinfusion session with the
  Baseline one. SD245's behaviour file holds only 'baseline' events, consistent with this.
  PRE_SESSION_ALT uses the Preinfusion file for SD245 (a reading shown as a variant).
- Puff times: TTL on DC channel index 2 (named 'CCEP' in the file), threshold 10e3, closing
  of 32 samples, onsets at least 1 s apart, only the second half of the epoch, first 40
[... 180 more lines not kept]
```

```
keep = ~pairs["excluded"].values
    if wm_excluded:
        keep &= ~pairs["wm"].values
    if bad is not None:
        badset = set(bad.get(pt, []))
        keep &= ~(pairs["a"].isin(badset) | pairs["b"].isin(badset)).values
    return keep


def epochs(x, puffs, trials):
    """(channels, time, trials) epochs of 2 s before to 2 s after each puff
    (get_puff_trace_matrix), for the trial indices `trials` of the 40 detected puffs."""
    n = int(EPOCH_S * FS)
    return np.stack([x[puffs[t] - n:puffs[t] + n].T for t in trials], axis=2)


def _win(tt, w):
    return (tt > w[0]) & (tt < w[1])


[... 407 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/05_mouse_npx.ipynb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Kauvar, Richman, Liu et al. 2025: mouse Neuropixels claims (DANDI:001326)
4	
5	Paper: Kauvar, Richman, Liu et al., "Conserved brain-wide emergence of emotional response from sensation in humans and mice", Science 388, eadt3971 (2025), doi:10.1126/science.adt3971.
6	
7	Data: the mouse Neuropixels recordings are not in dandiset 001347; the paper deposited them in DANDI:001326 (ref. 104), so these claims are `data: elsewhere`. DANDI:001326 has one published version, 0.250528.1957, which is pinned; the paper cites no version. Files are streamed with remfile and h5py (`dandi_io.open_h5`); nothing is downloaded. The Neuropixels-rig behaviour files of DANDI:001347 at 0.250528.0702 are read only to link sessions.
8	
9	Text read by the claims file: the version of record with its supplement (Materials and Methods, figure legends, Table S3), as extracted in `paper/10.1126-science.adt3971.txt`. Methods details not in the claims file come from that text and from the mouse analysis code, Zenodo record 14876694 (`analysis.py`, md5 6cc7aa5059737c3bd753aad1f116019d), which is read, not imported; `mouse_npx.py` reimplements what is needed and its docstring says where every parameter comes from.
10	
11	| claim | tested here |
12	|---|---|
13	| fig6d-mouse-persistent-activity-reduced | tested |
14	| fig6f-mouse-fast-activity-unchanged | tested |
15	| fig5e-mouse-emotion-dimension-late-reduced | tested |
16	| fig6h-mouse-timescale-shorter | tested |
17	| fig6j-mouse-coupling-reduced | tested |
18	| fig5d-mouse-emotion-dimension-accumulates | tested |
19	| figs34-mouse-tone-persistence-reduced | tested |
20	| fig4hi-mouse-rise-unchanged-decay-shortened | tested |
[... 593 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/05_mouse_npx.ipynb.txt",
 "offset": 613,
 "limit": 530
}
```

```
613	3   sub-2_20230902     2  0.0686  0.0345
614	4   sub-3_20230218     3  0.2464  0.2478
615	5   sub-3_20230225     3  0.4019  0.0350
616	6   sub-4_20230907     4  0.1170  0.0672
617	7   sub-6_20230823     6  0.4729  0.0366
618	8   sub-7_20220831     7  0.4571  0.1531
619	9   sub-8_20220228     8  0.9028  0.9607
620	10  sub-9_20230908     9  0.5518  0.1154
621	failed fits: 0 ; paired t, p = [3.5067 0.0057]
622	timescale preinfusion: 0.437 ± 0.077 s (expected 0.45 ± 0.07; within: True)
623	timescale ketamine: 0.162 ± 0.079 s (expected 0.14 ± 0.06; within: True)
624	averaged within mouse: [3.142  0.0138] ; sessions with ketamine shorter: 9 of 11
625	
626	
627	===== CELL 22 [markdown] =====
628	## fig6j-mouse-coupling-reduced
629	
630	> In mice, baseline pairwise correlation among the most persistent neurons halves during ketamine (0.49 of preinfusion).
631	
632	Pearson correlations of the session z-scored rates in the 30 s before each series, among the puff-modulated cells whose persistent weight is above the 90th percentile of |w|. Readings: selection and average (Methods: |w| above the percentile and the mean of r; code: signed w above it and the median of |r|); correlations within each 30-s window averaged over series (Methods, Table S3: "Values averaged within session across trials") or over the concatenated windows (code); variance M or C; series of the code (1 to 10, 23 to 32; Table S3: 10 and 10) or of the Methods epochs (1 to 20, 22 to 32). The test is the code's: paired t-test of the normalised values (1 against ketamine/preinfusion).
[... 510 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,140p mouse_npx.py; grep -n "^def \|EPOCH_READINGS\|^[A-Z_]* = " mouse_npx.py
```

```
"""Mouse Neuropixels analyses (Figs. 4G, 4H, 4I, 5D, 5E, 5G to 5I, 6D, 6F, 6H, 6J, fig. S34) for Kauvar, Richman, Liu
et al. 2025 on DANDI:001326 (version 0.250528.1957), streamed through dandi_io.

Each function follows the paper's Methods (sections cited below) and, where the Methods leave a
detail open, the mouse analysis code, Zenodo record 14876694, analysis.py (md5
6cc7aa5059737c3bd753aad1f116019d; cited as "code" with the function name). The code is not
imported; what is needed is reimplemented here.

Parameters and where they come from
- BIN = 0.01 s, causal moving average over 5 bins (50 ms): Methods, "Neuropixels recording and
  processing" ("binned at 10 ms resolution and smoothed with a causal moving average filter over
  50 ms"); the brainwide-npix firing_rates_over_recording (rates in spikes/s) and its
  moving_avg_filter (first 4 bins left unsmoothed).
- Z-scored rates: the code works on "all_zfr" (session z-scored rates); the driver that makes it
  is not in the record. Assumption: each unit's smoothed rate is z-scored over the whole recording
  (0 to its last spike time). A projection that is itself z-scored (Figs. 6D, 6F, S34) does not
  depend on this.
- Puff window -1 s to +2 s around each puff (300 bins), the window index of a puff being the first
  bin starting at or after it (code, get_windowed_puff_psth: searchsorted(bins, t) - 100).
- Ketamine start: 30 s after the last puff of series 20 (code, get_windowed_puff_psth). In all 13
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 140,200p mouse_npx.py; echo ----; sed -n 320,450p mouse_npx.py; echo ----; sed -n 600,820p mouse_npx.py
```

```
sm[SMOOTH - 1:] = (cs[SMOOTH:] - cs[:-SMOOTH]) / SMOOTH
    return sm, c


def _windows(starts, length):
    return starts[..., None] + np.arange(length)


def selective(rates):
    """Code 'selective': rates (n_series=20, 8, 300) of one cell -> bool (p <= 0.01 in any test)."""
    r = rates
    pre = r[:, :, :100].reshape(-1, 100).mean(-1)
    ref = r[:, :, 100:120].reshape(-1, 20).mean(-1)
    aff = r[:, :, 130:180].reshape(-1, 50).mean(-1)
    lng = r[:, :, 200:300].reshape(-1, 100).mean(-1)
    eb = r[:, 0, :100].mean(-1); lb = r[:, -1, :100].mean(-1)
    er = r[:, 0, 100:200].mean(-1); lr = r[:, -1, 100:200].mean(-1)
    ps = []
    for a, b in ((pre, ref), (pre, aff), (pre, lng), (eb, lb), (er, lr)):
        p = scipy.stats.ttest_rel(a, b).pvalue
[... 364 more lines not kept]
```

**Agent**

I've read everything in the notebooks and helpers. Next I'm querying the DANDI API for the asset list, to check the blocked claims (fig1f, figs4, figs12, figs15, figs27) against the archive itself.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/assets/?page_size=1000" -o a.json; python3 -c "
import json;d=json.load(open('a.json'));print(d['count'])
import collections
for a in d['results']:
    p=a['path']
    if not p.startswith('sub-mouse/'): print(p, a['size'])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/" -o v.json; python3 -c "
import json;d=json.load(open('v.json'));print(d.get('description'));print([a.get('name') for a in d.get('assetsSummary',{}).get('variableMeasured',[])] if 0 else d.get('assetsSummary'))"
python3 - <<'EOF'
import json,subprocess
d=json.load(open('a.json'))
for a in d['results']:
    if a['path'] in ('sub-h009/sub-h009_ses-P50_behavior.nwb','sub-SD181/sub-SD181_ses-puffInfusion_ecephys.nwb'):
        m=json.loads(subprocess.check_output(['curl','-s',f"https://api.dandiarchive.org/api/dandisets/001347/versions/0.250528.0702/assets/{a['asset_id']}/"]))
        print(a['path']); print({k:m.get(k) for k in ['description','wasGeneratedBy','variableMeasured']})
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i "Fig. 4B\|Fig 4B\|normalized to max\|normalized by max\|max-normal" 10.1126-science.adt3971.txt | head -20; echo ---; grep -n -i "25 min\|25-min\|30 to 40\|30-40\|peak ketamine" 10.1126-science.adt3971.txt | head -20; echo ---; grep -n -i "5 s after\|5s after\|1 s window\|1s window" 10.1126-science.adt3971.txt | head
```

```
1014:ketamine (Fig. 4B and fig. S28A) (as had occurred in our human participants that were likewise undergoing intracranial recording). We 
7690:Fig. 4B 
---
2164:Preinfusion time windows of 25 minutes prior to the start of ketamine 
2167:sleep-related activity. The peak ketamine time window was taken to 
2168:be the final 25 minutes of the ketamine infusion, excluding periods of 
2170:targeted-controlled infusion dosage, the peak ketamine time window 
2204:coincide with peak ketamine pharmacokinetic levels (which differed 
3888:measurements conducted during 40-minute ketamine infusions. (B) Average spectrograms across regions of ketamineinduced power changes. Values are z-scored at each frequency to a 25-minute pre-ketamine baseline window. Numbers in 
3889:parentheses denote patient count. (C) Spectral power changes, averaged during 30-40 minute peak ketamine window. Each 
---
1453:during ketamine, quantifying rapid (0 to 0.25 s after onset) and late emotion-like activity (2 to 3 s after first airpuff onset) epochs. Dots indicate sessions (n = 11 sessions,  
2128:to 1.5 s after each puff onset, and then baseline subtracted, using a 
2507:the 1 s window starting 5 s after the last puff onset of each preinfusion 
7692:Traces are baseline subtracted with a 1s window before puffs. Mean and 95% confidence interval of the mean 
7951:baseline subtracted with the mean eye closure in a 1s window before each puff series. Mean and 95% 
8094:x s.e.m.). Right, average persistent population activity during 0.5 to 1.5 s after puff onset, compared between 
10904:persistent population activity during 0.5 to 1.5 s after puff onset, compared between preinfusion, infusion, and
```

**Agent calls Bash**

```bash
cd paper; sed -n 7685,7700p 10.1126-science.adt3971.txt; echo ----; sed -n 2155,2215p 10.1126-science.adt3971.txt
```

```
thresholds, see supplement. 
Fig. 3C 
Analysis: Same as previous, but with regions instead of Yeo7 networks. Regions were included if there were at 
least two subjects with representation of the region. Number of trials specified in parentheses. 
0 
Fig. 4B 
Analysis: Average eye closure behavior on the first puff of each puff series, for pre and ketamine conditions. 
Traces are baseline subtracted with a 1s window before puffs. Mean and 95% confidence interval of the mean 
value is given (1.96 * s.e.m.), with trials averaged within session and variability taken across sessions. 
Condition 
# sessions 
# trials 
# subjects 
Preinfusion 
13 
20 
----
we used sliding 5-second windows to compute phase locking value.
To understand changes in PLV during ketamine relative to preinfusion, each channel’s PLV values were z-scored to its respective preinfusion window. To compute network disruption by ketamine in specific 
subnetworks (such as between sites with high post-puff persistence), 
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;c=yaml.safe_load(open('10.1126-science.adt3971.yaml'))['claims'];print(len(c));print(sum(1 for x in c if x.get('kind')=='link'))
print([x['id'] for x in c if x.get('data')=='elsewhere'])"
```

```
61
5
['fig4hi-mouse-rise-unchanged-decay-shortened', 'fig4g-mouse-slow-clusters-altered', 'fig5d-mouse-emotion-dimension-accumulates', 'fig5e-mouse-emotion-dimension-late-reduced', 'fig5g-mouse-first-order-model', 'fig6d-mouse-persistent-activity-reduced', 'fig6f-mouse-fast-activity-unchanged', 'fig6h-mouse-timescale-shorter', 'fig6j-mouse-coupling-reduced', 'figs34-mouse-tone-persistence-reduced']
```

**Agent**

Last step: quick synthetic tests of a few helper functions.

**Agent calls Bash**

```bash
cd  timeout 600 python3 - <<'EOF' 2>&1 | tail -30
import numpy as np, sys
try:
    import human_eye as he, mouse_eye as me, ieeg_cd as ic
except Exception as e:
    print("import failed:", e); sys.exit()
# window_mean: puff at sample 400, 200 Hz
x=np.zeros((1,800)); t=(np.arange(800)-400)/200
x[0]=t
print("early window mean", he.window_mean(x,(0.1,0.2)), "expected ~0.1475; late", he.window_mean(x,(0.3,0.8)), "expected ~0.5475")
# per_mouse ratio = mean(late)/mean(early)
tr=np.random.default_rng(0).random((10,16200))+1
v=me.per_mouse(tr,0); late=tr[:,me.window(0,me.LATE)].mean(1); early=tr[:,me.window(0,me.EARLY)].mean(1)
print("ratio ok", np.isclose(v['ratio'], late.mean()/early.mean()))
# extract_timescale on AR(1) process with tau 0.1 s at 200 Hz
rng=np.random.default_rng(1); fs=200; tau=0.1; a=np.exp(-1/(fs*tau)); n=120000
e=rng.standard_normal(n); s=np.zeros(n)
for i in range(1,n): s[i]=a*s[i-1]+e[i]
print("tau est lag1", ic.extract_timescale(s,start_lag=1), "lag0", ic.extract_timescale(s,start_lag=0), "true", tau)
# cd_weights: known difference
ep=np.zeros((3,800,50)); ep[0,int(2.5*200):int(3.5*200)]+=1; ep+=np.random.default_rng(2).normal(0,1,ep.shape)*0.1
print("cd weights", ic.cd_weights(ep,(0.5,1.5)).round(3))
# survival_times: trial closed until 10 s after start
tr=np.ones((1,16200)); tr[0,:1000]=0.5; tr[0,int(200*30.3):int(200*40.3)]=2; tr[0,int(200*40.3):]=0.1
print("survival", me.survival_times(tr,30.3))
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v >/dev/null 2>&1 && ./v/bin/pip -q install numpy scipy pandas 2>&1 | tail -2; ls v/bin | head -3
```

```
Activate.ps1
activate
activate.csh
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stub; for m in h5py remfile requests; do echo "" > $TMPDIR/stub/$m.py; done; PYTHONPATH=$TMPDIR/stub:. timeout 900 $TMPDIR/v/bin/python - <<'EOF' 2>&1 | tail -30
import numpy as np
import human_eye as he, mouse_eye as me, ieeg_cd as ic
x=np.zeros((1,800)); t=(np.arange(800)-400)/200; x[0]=t
print("early", he.window_mean(x,(0.1,0.2)), "late", he.window_mean(x,(0.3,0.8)))
tr=np.random.default_rng(0).random((10,16200))+1
v=me.per_mouse(tr,0); late=tr[:,me.window(0,me.LATE)].mean(1); early=tr[:,me.window(0,me.EARLY)].mean(1)
print("ratio ok", np.isclose(v['ratio'], late.mean()/early.mean()))
rng=np.random.default_rng(1); fs=200; tau=0.1; a=np.exp(-1/(fs*tau)); n=120000
e=rng.standard_normal(n); s=np.zeros(n)
for i in range(1,n): s[i]=a*s[i-1]+e[i]
print("tau lag1", ic.extract_timescale(s,start_lag=1), "lag0", ic.extract_timescale(s,start_lag=0), "true", tau)
ep=np.random.default_rng(2).normal(0,.1,(3,800,50)); ep[0,500:700]+=1
print("cd weights", ic.cd_weights(ep,(0.5,1.5)).round(3))
tr=np.ones((1,16200)); tr[0,:1000]=0.5; tr[0,int(200*30.3):int(200*40.3)]=2; tr[0,int(200*40.3):]=0.1
print("survival (expect 10 s, event)", me.survival_times(tr,30.3))
tr2=np.ones((1,16200))*2; tr2[0,:1000]=0.5
print("survival never reopens (expect 50, 0)", me.survival_times(tr2,30.3))
# plv
ph=np.random.default_rng(3).uniform(-np.pi,np.pi,(2000,3)); ph[:,1]=ph[:,0]+0.3
print("plv", ic.edge_plv(ph,[0,1,2]).round(2))
EOF
```

```
early [0.1475] late [0.545]
ratio ok True
tau lag1 0.10549865138435721 lag0 0.10494681237726249 true 0.1
cd weights [ 0.996  0.003 -0.002]
survival (expect 10 s, event) (array([9.995]), array([1]))
survival never reopens (expect 50, 0) (array([50.]), array([0]))
plv [[1.   0.04 0.04]
 [1.   0.02 0.02]]
```

**Agent**

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| p50-condition-labels-link | holds | 01 c10: the same 4 participants, each with one saline and one ketamine session, and 40 trials per series. The saline label comes from the code alone. |
| cadss-scores-link | holds | 01 c12: all 14 dataset participants have pre, infusion and post totals. |
| mouse-session-labels-link | holds | 02 c18–19: 142 of 142 ids present, none too short; (3a), (3b) and (3c) all hold (skip puff matched in 100% of infusion trials). |
| link-ieeg-yeo-labels | holds | 03 c12: 458 of 458 found, regions agree, the dataset is never larger (120 of 126 rows equal), and the deposited 2H and 2J matrices are recovered with max difference 0.0. |
| ieeg-channel-atlas-link | holds | 04 c30: every contact and pair matched, region agreement 1.0. |
| fig1e | reproduced | 01 c14: 0.706 and 0.426, t = 3.703, p = 0.0342 under A(a)/B(a); all four readings pass. |
| figs1b | reproduced | 01 c17: p = 0.2032 (≥ 0.05); means 0.839 and 0.777 match. |
| figs1c | reproduced | 01 c19: 0.591 and 0.343, t = 3.653, p = 0.0354. |
| figs1d | reproduced | 01 c21: 0.50 and 9.75, \|t\| = 7.034, p = 0.006 (code constants, as the criterion allows). |
| fig1f | blocked (data_missing) | No verbal reports anywhere; the archive's 207 assets confirm this. |
| fig2c | reproduced | 01 c29: late 0.541, 0.306, 0.518 (ketamine lower in 7 of 7); early, pre against ketamine, p = 0.236. |
| figs8a | reproduced | 01 c24–25: 14 of 14 tests significant in the stated direction, trial counts match, 21 of 21 means within tolerance. |
| figs8b | reproduced | 01 c27: none of the 7 meets both tests. |
| fig2d | reproduced | 01 c32: 0.86, 22.43, 0.86; corrected p = 0.004 and 0.004. |
| figs14g | reproduced | 01 c34: 10 kept, rho = 0.744, p = 0.0136 under reading (a). Reading (b) fails (0.561). |
| figs12 | blocked (data_missing) | No spontaneous-blink onsets in the archive; the criterion blocks in that case. |
| figs13 | reproduced | 03 c16: control loading below preinfusion for 6 of 6 factors (30 of 30 participant–factor pairs). |
| figs15 | blocked (metadata_insufficient) | See item 11 in B: an approximate test was possible but was not attempted. |
| fig2g | reproduced | 03 c7–8: 458 channels; test EV 0.466 at six components; the largest fall in gain is at 6. The refit equals the deposited factors. |
| fig2h | partially_reproduced | 03 c13: 4 of 6 rows (Limbic f3–5 share 0.495, Frontoparietal 0.463). Readings (a) and (b) give the same order. |
| fig2i | reproduced | 03 c14: every BH p matches Table S3 (f1 2.56e-05, f2 5.51e-08, f0 0.121, f4 0.406, f5 0.341); 6 of 6 means within tolerance; post-hoc recovery holds. |
| fig2j | reproduced | 03 c15: reading (a) holds for both factors. Reading (b) fails for factor 1. |
| fig3b | reproduced | 03 c17: Limbic, Ventral Attention and Somatomotor significant at BH 0.0039; the other three not. Maps equal the deposited ones. |
| fig3c | reproduced | 03 c18: reading (a) 10 of 10 listed significant; 10 of 10 others not (STG BH p = 0.0103). |
| figs27 | blocked (metadata_insufficient) | The notebook says data_missing, but the criterion's fallback window allows a partial test (item 11 in B). |
| fig6c | reproduced | 04 c9: code Open C readings 1.363, 0.411, 0.724; t = 5.88 and 3.17; corrected p < 0.05. 15 of 32 combinations pass. |
| fig6e | reproduced | 04 c12: code readings 4.120, 4.006, 3.866, p = 0.68 and 0.65, matching the paper. Methods z-scoring with the code's bad-channel list gives post against ketamine p = 0.03 (item 12). |
| figs37c | reproduced | 04 c14: code Open C with white matter excluded: pre > ketamine in 5 of 5 bands, broadband p = 0.078, post > ketamine delta p = 0.047 and beta p = 0.019. |
| figs37b | reproduced | 04 c16: no significant test under the code readings that reproduce fig6c. Methods readings show a low-gamma decrease. |
| figs37a | reproduced | 04 c34: beta is highest in 10 of 16 readings, including the code human reading. The margin over broadband is ≤ 0.01 in several readings, so the result is fragile. |
| fig6g | reproduced | 04 c18: 0.115 and 0.092, t = 4.78, p = 0.003, within tolerance (code reading, Open E 10 min). |
| fig6i | partially_reproduced | 04 c20: the test holds in all 8 readings, but the ratio is 0.93–0.96 against 0.979 ± 0.006. Open F (a) cannot be run. |
| figs38a | not_reproduced | 04 c22–23: theta and alpha differ in every channel reading (BH p 0.0001–0.03). The edge counts (368–896) never equal 716. |
| figs38b | partially_reproduced | 04 c25: beta (z units) is significant in all readings and within tolerance in 3 of 4; alpha in 3 of 4; gamma in none. |
| figs38h | reproduced | 04 c28: with the H-CD pre-puff baseline and the code's bad-channel list: 12.38 [3.09, 21.68], p = 0.009; eye 2.57, p = 0.003; infusion p = 0.35 and 0.98. |
| figs35 | reproduced | 04 c32: persistent BH p ≥ 0.68; fast somatomotor BH p < 0.001; means 0.437 and 0.339 within tolerance. |
| fig1k | reproduced | 02 c21: 0.262 and −0.068, t = 4.737, p = 0.0091. |
| fig1l | reproduced | 02 c24: ketamine BH p = 0.002, PCP 0.041, saline 0.50; 6 of 6 means within tolerance. |
| figs2bc | partially_reproduced | 02 c26: both t values match the paper exactly (6.854, 4.951) and early ketamine stays above 0. Late saline is 0.203 against 0.34 ± 0.07 (item 9). |
| fig1m | reproduced | 02 c28: reading (b) gives 15.45 s (tolerance 15.16 ± 1.52); late closure rises from 0.244 to 0.517. See item 10. |
| figs2g | reproduced | 02 c30: t values and 6 of 6 means match exactly. |
| figs2h | reproduced | 02 c32: 10 of 10 conditions agree under both Open I readings. |
| figs5c | reproduced | 02 c34: t values match exactly. |
| fig1p | reproduced | 02 c36: BH p = 0.006 and 0.0016; K/X 0.025 and 0.024, within tolerance. |
| fig1no | reproduced | 02 c38: decay rates 3.53, 11.89, 3.04, 13.20; BH p = 0.027. Late closure on the eighth puff (−0.007, 0.000) sits at zero (item 17). |
| figs2l | reproduced | 02 c40: 0 of 12 significant. |
| figs2n | reproduced | 02 c42: all BH p ≥ 0.29. |
| figs2o | reproduced | 02 c44: rise at the skipped puff is 0.0008 and 0.0004, within s.e.m.; the level stays above 0. |
| figs4 | blocked (data_missing) | No lick data in any asset (the archive check confirms it). |
| figs6 | reproduced | 02 c48: t values match; 0.602 and 0.105 within tolerance; fast early p = 0.89. |
| fig4b | not_reproduced | 02 c50: under the method of the criterion and Table S3 (baseline-subtracted, no normalisation) the intervals overlap (0.174 ± 0.058 against 0.148 ± 0.035). It passes only with the max-normalisation (item 1). 10 of 13 sessions. |
| fig4hi | partially_reproduced | 05 c31: decay shortened (median −0.19 s, interval of the median below 0; 34 of 36 regions). Under that same interval reading, rise changes by −9 ms with an interval that excludes 0 (item 8). |
| fig4g | reproduced | 05 c28: rho = +0.47; slowest three 0.51 against fastest three 0.37. 11 clusters, against the paper's 12. |
| fig5d | reproduced | 05 c19: all 16 readings pass. |
| fig5e | not_reproduced | 05 c17: under the criterion's 5–6 s target the late test fails in all 8 readings (BH p ≥ 0.067). Only the author-inferred 3–4 s code window passes (item 2). |
| fig5g | reproduced | 05 c33/c35: neural fit 0.881 (tolerance 0.954 ± 0.095); dose fits 0.930 and 0.870, within under both assignments; alternative models lower on the ketamine half (0.896, 0.897 against 0.918). |
| fig6d | reproduced | 05 c12: 0.867, −0.002, 0.515; BH p = 0.0005 and 0.029. |
| fig6f | not_reproduced | 05 c15: post against ketamine is significant in all 8 readings (BH p 0.004–0.016) and with 13 sessions; the three means are outside tolerance. |
| fig6h | reproduced | 05 c21: 0.437 and 0.162 s, p = 0.006. |
| fig6j | partially_reproduced | 05 c23: the Methods rule fails (ratio 0.85, p = 0.30). The code variant the criterion names passes (0.559, p = 9e-5). |
| figs34 | partially_reproduced | 05 c25–26: fast not significant, persistent and timescale tests hold. Main-reading coupling ratio is 1.24 (p = 0.64), and persistent pre (1.639) and ketamine timescale (0.115) are outside tolerance. |

No claim involves a decoding chance level.

**B. Problems**

1. [affects a conclusion] 02 c50, `mouse_eye.npx_series`, fig4b. The main reading divides each condition's mean trace by its own maximum, taken from analysis.py of the mouse code record. Neither the criterion nor Table S3 ("baseline subtracted with a 1s window") includes this step. On un-normalised traces, ketamine is lower in only 6 of 10 sessions. Three of the 13 sessions have no behaviour file in 001347.
2. [affects a conclusion] 05 c17, fig5e. The 3–4 s target is inferred from the code's plotting offsets and is not in the criterion. Its means match Table S3 closely (0.608, 0.308, 0.534, 0.004), which suggests the paper used it. The claims file should have named the conflict between the Methods window and the code window as an open detail.
3. [affects a conclusion] 05 c15, fig6f. Ketamine is above postinfusion in every reading, so the absence claim fails.
4. [affects a conclusion] 04 c22, `ieeg_cd.BANDS`, figs38b and figs38a. The criterion requires the code's band-edge variant ((13, 30), (31, 70) and so on). It was not run, and gamma is tested only at 30–50 Hz.
5. [affects a conclusion] 04 c22, `top_bottom` and `edge_table`, figs38a and figs38b. Edge counts are 368, 462, 792 and 896 against the paper's 716, so the site selection differs from the paper's. The figs38a absence failure may come from this. No per-participant comparison is given.
6. [affects a conclusion] 04 c20, `plv_windows`, fig6i. The windows are non-overlapping, an author choice (the Methods say "sliding"). Open F (a) cannot be run because the files hold only 20-min epochs.
7. [affects a conclusion] 05 c23 and c26, `coupling_values`, fig6j and figs34. The Methods rule averages signed r values of about 0.01, so the ratio is unstable: it ranges from 0.56 to 1.45 across readings. figs34's passing coupling rows use the windows before puff series, not before tone series.
8. [affects a conclusion] 05 c31, fig4hi. Under the interval-of-median reading the rise interval excludes 0; under the pooled reading the decay interval includes 0. No single reading satisfies both parts of the criterion.
9. [affects a conclusion] figs2bc, claims file. The expected late saline value of 0.34 conflicts with the paper's own numbers: 0.26 × 0.78 ≈ 0.20, and t = 4.951 is reproduced exactly with 0.203. The tolerance check fails because of this inconsistency in the paper, not the analysis.
10. [does not affect a conclusion] 02 c28, fig1m, claims file. The paper's 15.16 s is reproduced exactly only with all 40 trials and the code's start frame (200 trials). The claims file's "20 preinfusion trials" reading of Table S3 is likely wrong, and the pass under reading (b) is not the paper's computation.
11. [affects a conclusion] 03, figs15 and figs27. Both are marked blocked as data_missing. The infusion files span about 10 min before and after a puff start roughly 30 min into the infusion, so roughly minutes 20 to 40. That covers the fallback 30–40 min window that the figs27 criterion names explicitly, and the CADSS inputs are available. A partial test of the 7 included participants was possible. The infusion start time is not stored, so metadata_insufficient is the accurate reason.
12. [could affect a conclusion] 04 c12 and c16, fig6e and figs37b. The absence holds only with the code's z-scoring. Methods z-scoring with the code's bad-channel list gives significant results (beta post against ketamine p = 0.034; low gamma pre against ketamine p = 0.02–0.05).
13. [does not affect a conclusion] 05 c8. Treating mouse 5 as the excluded animal is an assumption. It is well argued (it is the only choice that yields 7 tone sessions from 7 mice), and the 13-session variants are shown.
14. [does not affect a conclusion] 03 c14, fig2i. Factors 3 and 4 involve 7 participants here against 5 and 6 in Table S3, although the channel counts and p values match exactly.
15. [does not affect a conclusion] 03 c16, figs13. Control loadings use all control trials, while the preinfusion values use only the test half.
16. [does not affect a conclusion] 03 c8, fig2g. Two elbow rules give 6 and 8; neither the paper nor the criterion fixes one.
17. [does not affect a conclusion] 02 c38, fig1no. Read literally, "not above" fails: ketamine late closure on the eighth puff (−0.007) is above the first (−0.025) in 4 of 5 mice, p = 0.18. Both values are at zero, so I treated the condition as met.
18. [does not affect a conclusion] 04 c24 and c26. The author's conclusion cells for figs38a and figs38b were not removed. I formed my verdicts independently.
19. [does not affect a conclusion] Helper tests on synthetic inputs all behaved as intended: `window_mean`, `per_mouse`, `extract_timescale` (τ 0.1 → 0.105), `cd_weights`, `survival_times` and `edge_plv`.

**C. Not checked**

- Code-record details could not be checked against the source: whether analysis.py produces Fig. 4B with the max-normalisation, the 3–4 s window offset (fig5e), the null model of fig5g, the paper's 716-edge selection, `fig1_persistence` trial use, and the participant counts in Table S3 for fig2i. Printing the relevant code lines in the notebook would settle each one.
- Figures were not viewable; only their printed ranges.
- Outputs that would have let me check more:
  - figs38a/b: the code band-edge variant, and per-participant high and low edge counts.
  - fig6i: sliding-window PLV.
  - figs27 and figs15: an approximate run on the infusion files.
  - fig4b: the stored puff_aff/puff_ref values with 1.96 s.e.m. intervals across sessions.

## End of run

33 turns, 7 minutes, $4.65 at API prices, result: success.
