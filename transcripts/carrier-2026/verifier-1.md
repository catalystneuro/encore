# carrier-2026 · verifier-1 · run 45676852004

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls -la; ls paper; ls docs 2>/dev/null
```

```
Exit code 2
total 404
drwxr-xr-x 6 runner runner    4096 Nov 25 18:44 .
drwxr-xr-x 8 runner runner    4096 Nov 25 18:44 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 18:33 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 18:33 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 25 18:44 .claude
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.development
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.local
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.production
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.test
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .env.test.local
drwx------ 2 runner runner    4096 Nov 25 18:44 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 18:33 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 18:33 .github
-rw-r--r-- 1 runner runner       0 Nov 25 18:44 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 18:33 .idea
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "carrier-2026.yaml"
}
```

```
1	# Claims for Carrier, Romano, Scaria, Palmer, O'Leary, Marder & Powell (2026), "The combined
2	# effects of temperature and salinity on the stomatogastric nervous system of two species of
3	# decapod crustacea", J Neurophysiol 135: 797-814, doi:10.1152/jn.00294.2025, tested on
4	# Zenodo:17624449 (Part I, folder zenodo-17624449) and Zenodo:17794764 (Part II, folder
5	# zenodo-17794764).
6	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
7	# protocol as stated in docs/protocol.md (version pilot-19, Reader).
8	#
9	# Text read. The version of record (J Neurophysiol PDF, CC-BY 4.0), full text in
10	# paper/10.1152-jn.00294.2025.txt: main text, Methods, figure legends 1 to 9, Table 1, Data
11	# availability. The paper has no supplement and cites none. The PDF could not be rendered in this
12	# run, so the bar heights of Figures 1E, 4E and 9 (percentages) were not read; only the numbers
13	# the text states are used.
14	#
15	# Code read. None. The paper links no code repository; Data availability says "All data and
16	# custom analysis scripts" are in the two Zenodo records. The archives' file lists show no
17	# separate script files, so any scripts sit inside the data archives, which a reader does not
18	# open. Burst detection, frequency and phase were computed with "custom Spike2 (CED) or MATLAB
19	# (MathWorks) scripts" (Methods, Data Analysis and Statistics); regressions and two-sample tests
20	# in GraphPad Prism; mixed-effects models of frequency in R (lme4, lmerTest); in vivo spectrograms
[... 1098 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "stns.py"
}
```

```
1	"""Loading and measures for Carrier et al. (2026) on Zenodo records 17624449 and 17794764.
2	
3	Carrier, Romano, Scaria, Palmer, O'Leary, Marder & Powell (2026), "The combined effects of
4	temperature and salinity on the stomatogastric nervous system of two species of decapod
5	crustacea", J Neurophysiol 135: 797-814, doi:10.1152/jn.00294.2025.
6	
7	Record 17624449 (Part I, folder zenodo-17624449) holds the raw Spike2 recordings of the lobster
8	(H. americanus) temperature ramps (`Lobster STNS.zip`), half of the crab (C. borealis) raw data
9	(`Raw Crab Data 1.zip`), and the authors' analysis tables: `Crab Metadata.xlsx` (per crab
10	preparation: PD burst frequency at each step of each ramp, the salinity series, the crash
11	temperature of each neuron, phases), `Lobster Pyloric Frequencies.xlsx` (per lobster
12	preparation: PD burst frequency at each step of each ramp, with the crash step), three GraphPad
13	Prism 10 files (`.prism`, zip archives of JSON and CSV) and four MATLAB files. Record 17794764
14	(Part II, folder zenodo-17794764) holds the other half of the crab raw data and the in vivo PPG
15	recordings (Axon `.abf` files in zips inside zips).
16	
17	Every file is read from the archive into memory with fsspec (block_size 2**20), at the pinned
18	record, and a file read whole is checked against the MD5 the record lists. Nothing is written
19	to disk.
20	
[... 446 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_carrier_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n===== CELL {i} [{c['cell_type']}] =====")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- out:'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -c "===== CELL" $TMPDIR/nb.txt
```

```
1648 /tmp/claude-1001/nb.txt
67
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Reproducing Carrier et al. (2026) from Zenodo records 17624449 and 17794764
4	
5	**Paper.** Carrier MA, Romano DM, Scaria A, Palmer H, O'Leary T, Marder E, Powell D (2026). The
6	combined effects of temperature and salinity on the stomatogastric nervous system of two
7	species of decapod crustacea. *J Neurophysiol* 135: 797-814.
8	[doi:10.1152/jn.00294.2025](https://doi.org/10.1152/jn.00294.2025). The claims file
9	(`claims/carrier-2026.yaml`) was written from the version of record (full text, Methods, figure
10	legends, Table 1); the paper has no supplement.
11	
12	**Datasets.** Two Zenodo records the authors deposited for the paper, both read at the only
13	version each has (Zenodo pins a version by its record id; the paper cites these record DOIs,
14	and the target list gives no other version):
15	
16	- [ZENODO:17624449](https://zenodo.org/records/17624449) (Part I, folder `zenodo-17624449`),
17	  record 17624449, DOI 10.5281/zenodo.17624449, published 2025-11-16.
18	- [ZENODO:17794764](https://zenodo.org/records/17794764) (Part II, folder `zenodo-17794764`),
19	  record 17794764, DOI 10.5281/zenodo.17794764, published 2025-12-02.
20	
[... 686 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 706,
 "limit": 500
}
```

```
706	===== CELL 23 [markdown] =====
707	The crab 1.25x crash temperatures of the Prism file follow the unit table row for row except
708	963_106, where the table's neurons crashed at 21.2 C (LP) and 26 C (PD), so the rhythm crashed at
709	26 C, and the Prism file has 36 C. The paper's two crab 1.25x means (26.2 C in Fig. 2E, 27.28 C in
710	Fig. 7F) are the two versions of this value.
711	
712	===== CELL 24 [code] =====
713	exts = pd.Series([k.rsplit(".", 1)[-1].lower() for k in list(files1) + list(files2)]).value_counts()
714	print("File types in the two records:", exts.to_dict())
715	inner = pd.Series([n.rsplit(".", 1)[-1].lower() for k in nested for n, _ in nested[k]]).value_counts()
716	print("File types inside the raw-crab and in vivo zips (first level):", inner.to_dict())
717	print("File types inside Lobster STNS.zip:", lob_members.ext.value_counts().to_dict())
718	code = lob_members[lob_members.ext.isin(["m", "py", "r", "ipynb", "s2s"])]
719	print("Script files in Lobster STNS.zip:", len(code))
720	print("Lobster preparations in Sheet4 without a folder in Lobster STNS.zip:",
721	      sorted(set(lob_f.prep) - set(lob_members.prep.dropna())))
722	--- out:
723	File types in the two records: {'zip': 7, 'mat': 4, 'csv': 3, 'prism': 3, 'xlsx': 2}
724	File types inside the raw-crab and in vivo zips (first level): {'zip': 80}
725	File types inside Lobster STNS.zip: {'txt': 1404, 's2rx': 296, 'smr': 289, 'xlsx': 14, 'smrx': 2}
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1205,
 "limit": 450
}
```

```
1205	
1206	
1207	===== CELL 45 [code] =====
1208	def at10(df, sal=1.0, exclude=()):
1209	    d = df[(df.salinity == sal) & (df.temp == 10) & ~df.prep.isin(exclude)]
1210	    return d.groupby("prep").freq.first()
1211	
1212	crab10 = at10(crab_f)
1213	lob10 = at10(lob_f, exclude=lob_r[lob_r.not_used].prep.tolist())
1214	w = stats.ttest_ind(crab10, lob10, equal_var=False)
1215	print(f"R-a: crab n = {len(crab10)}, {crab10.mean():.3f} +/- {crab10.std():.3f} Hz; lobster n = {len(lob10)}, "
1216	      f"{lob10.mean():.3f} +/- {lob10.std():.3f} Hz; Welch t = {w.statistic:.2f}, P = {w.pvalue:.2g}")
1217	crab_base = crab_s[crab_s.salinity == 1.0].groupby("prep").freq.first().dropna()
1218	w2 = stats.ttest_ind(crab_base, lob10, equal_var=False)
1219	print(f"R-b: crab salinity-series baseline n = {len(crab_base)}, {crab_base.mean():.3f} Hz (first 1x value per preparation); "
1220	      f"no lobster salinity series is deposited, so the lobster side stays the 10 C ramp step: Welch P = {w2.pvalue:.2g}")
1221	--- out:
1222	R-a: crab n = 19, 1.206 +/- 0.144 Hz; lobster n = 15, 0.563 +/- 0.119 Hz; Welch t = 14.29, P = 2e-15
1223	R-b: crab salinity-series baseline n = 12, 1.162 Hz (first 1x value per preparation); no lobster salinity series is deposited, so the lobster side stays the 10 C ramp step: Welch P = 9.3e-10
1224	
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for r in 17624449 17794764; do curl -s https://zenodo.org/api/records/$r | python3 -c "import json,sys,re;d=json.load(sys.stdin);m=d['metadata'];print(d['id'],m.get('version'),m['title']);print(re.sub('<[^>]+>',' ',m.get('description',''))[:3000]);print([f['key'] for f in d['files']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, stns
rng=np.random.default_rng(0)
T=np.repeat(np.arange(10,26,2),10).astype(float)
F=10**(0.025*T-0.2)*(1+0.05*rng.standard_normal(len(T)))
for rd in ("Q-a","Q-b"):
    r=stns.semilog_fit(T,F,rd); print(rd, round(r['q10'],3), 'true', round(10**0.25,3))
F2=10**(0.025*T+0.1)*(1+0.05*rng.standard_normal(len(T)))
print(stns.shared_slope_test({'a':(T,F),'b':(T,F2)})['p'])
F3=10**(0.035*T+0.1)*(1+0.05*rng.standard_normal(len(T)))
print(stns.shared_slope_test({'a':(T,F),'b':(T,F3)})['p'])
print(stns.zero_slope_test(T,np.full(len(T),1.0)+0.05*rng.standard_normal(len(T)))['p'])
# band rule on white noise and on noise with no rhythm
fs=50; y=rng.standard_normal(fs*1800).astype(np.float32)
f,t,S=stns.ppg_spectrogram(y,fs); print('white noise pass frac', stns.band_present(f,S).mean())
# pink/brown-ish noise (low-frequency dominated)
yb=np.cumsum(rng.standard_normal(fs*1800)).astype(np.float32)
f,t,S=stns.ppg_spectrogram(yb,fs); print('brown noise pass frac', stns.band_present(f,S).mean())
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
ls /usr/bin/python3* ; which -a python python3 uv pip 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/usr/bin/pip
/bin/pip
/opt:
actionarchivecache
az
containerd
google
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q $TMPDIR/v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy scipy pandas requests fsspec 2>&1 | tail -2; $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, stns
rng=np.random.default_rng(0)
T=np.repeat(np.arange(10,26,2),10).astype(float)
F=10**(0.025*T-0.2)*(1+0.05*rng.standard_normal(len(T)))
for rd in ("Q-a","Q-b"):
    r=stns.semilog_fit(T,F,rd); print(rd, round(r['q10'],3), 'true', round(10**0.25,3))
F2=10**(0.025*T+0.1)*(1+0.05*rng.standard_normal(len(T)))
print('same slope p', stns.shared_slope_test({'a':(T,F),'b':(T,F2)})['p'])
F3=10**(0.035*T+0.1)*(1+0.05*rng.standard_normal(len(T)))
print('diff slope p', stns.shared_slope_test({'a':(T,F),'b':(T,F3)})['p'])
print('flat zero-slope p', stns.zero_slope_test(T,np.full(len(T),1.0)+0.05*rng.standard_normal(len(T)))['p'])
fs=50; y=rng.standard_normal(fs*1800).astype(np.float32)
f,t,S=stns.ppg_spectrogram(y,fs); print('white noise pass frac', stns.band_present(f,S).mean())
yb=np.cumsum(rng.standard_normal(fs*1800)).astype(np.float32)
f,t,S=stns.ppg_spectrogram(yb,fs); print('brown noise pass frac', stns.band_present(f,S).mean())
EOF
```

```
Q-a 1.802 true 1.778
Q-b 1.805 true 1.778
same slope p 0.17283402619015945
diff slope p 4.8940891173048096e-06
flat zero-slope p 0.23547171020397645
white noise pass frac 0.9637883008356546
brown noise pass frac 1.0
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "9 of 20|all three neurons|n = 10 \(0.75|Figure 5C|Fig. 5C|30 min|first 30|2.5 h|15 h" 10.1152-jn.00294.2025.txt | head -40
```

```
151:30 min. Dissections were performed as previously described
216:physiological saline for 30 min to obtain a baseline (control) recording.
598:In C. borealis, in 1�saline, we observed that in 9 of 20
599:preparations all three neurons crashed at the same temperature, and in 14 of 20 preparations, the PY neurons
788:Figure 5C shows plots of the pyloric rhythm frequency as a
797:temperatures greater than 24�C (Fig. 5C, left plot) and the
799:saline (Fig. 5C, right plot). Therefore, for the nonlinear (semilog) regression Q10 fits, we only fit the data within these more
883:single Jonah crab, of the first 30 min of each 1-h application
907:and decreased saline concentrations for 2.5 h (n 1⁄4 6; data not
908:shown) and 15 h (n 1⁄4 5). Although all animals generally
935:tolerated 1-h and 2.5-h changes in their environmental salinity, after 15 h some mortalities were observed. Figure 9 shows
1030:increased saline concentrations 1.25�, 1.5�, and 1.75�. All recordings are from the first 30 min of a 1-h saline perturbation. Preparations maintained
```

**Agent calls Bash**

```bash
cd paper; sed -n 590,610p 10.1152-jn.00294.2025.txt; echo ----; sed -n 770,800p 10.1152-jn.00294.2025.txt; echo ----; sed -n 875,890p 10.1152-jn.00294.2025.txt; sed -n 1020,1040p 10.1152-jn.00294.2025.txt
```

```
COMBINED EFFECTS OF TWO PERTURBATIONS ON A SMALL CIRCUIT
J Neurophysiol �doi:10.1152/jn.00294.2025
803
Downloaded from journals.physiology.org/journal/${contentReq.journalCode} (136.144.042.092) on November 25, 2026.

=== page 8 ===
In this study, we define crash temperature as the temperature at which at least two of the three pyloric motor
neurons fail to remain rhythmically active (see, METHODS).
In C. borealis, in 1�saline, we observed that in 9 of 20
preparations all three neurons crashed at the same temperature, and in 14 of 20 preparations, the PY neurons
crashed. The LP neuron always crashed. We did not
observe a difference in neuron crash temperature in 1�
saline [Fig. 2I, REML mixed-effects model: F(0.57,7.67) 1⁄4
1.14, P 1⁄4 0.27, n 1⁄4 20 (LP), 14 (PY), 15 (PD)]. In 0.75�saline,
the PD neurons only crashed in 4 of 11 preparations,
whereas the LP and PY neurons crashed in all experiments.
In 1.25�saline, in 5 of 9 preparations the PY neurons
crashed and 6 of those 9 experiments included a loss of
PD. LP crashed in all experiments. Like the neuron crash
temperatures in 1�saline, we did not observe any difference in neuron crash temperature in either 0.75�saline
[... 71 more lines not kept]
```

**Agent**

**Verification report, round 1: Carrier et al. 2026 (doi:10.1152/jn.00294.2025)**

The claims file has 29 claims. The notebook tests 21 and treats 8 as blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-cb-075-frequency-unchanged | reproduced | Cell 27: n = 10, 1x 1.175 Hz and 0.75x 1.183 Hz (tolerance ±0.07 around 1.18), paired t P = 0.816. The table has only one 1x value, so the two baseline readings cannot be told apart. |
| fig1d-cb-125-frequency-unchanged | reproduced | Cell 29: n = 10, 1.176 and 1.169 Hz (1.2 ± 0.04), P = 0.748. |
| fig1e-cb-salinity-crash-fractions | blocked (data_missing), partly testable | 0.5x and 1.75x are not in the table. Cell 29 does show three of the five counts: 0.75x 10/10 with values, 1.25x 10/10, and 1.5x 9/10 (888_141 missing), which matches "all but one" if a missing value means a crash. The notebook does not report these. |
| fig2b-cb-crash-temp-075-unchanged | reproduced | Cell 31: n = 11, 29.35 and 30.62 °C, Wilcoxon P = 0.401. Levene's test centred on the mean gives P = 0.0497 with the 0.75x SD lower (4.49 vs 2.47 °C). Centred on the median it gives P = 0.102, so the variance part holds only under the mean-centred reading. |
| fig2e-cb-crash-temp-125-lower | reproduced | Cell 32: 31.27 vs 26.17 °C, paired t P = 0.003 (paper 0.008), lower in 9 of 9. The variant using the Prism value (36 °C for 963_106) gives P = 0.0145 and 8 of 9. |
| fig2f-cb-125-frequency-rises | reproduced | Cells 38–39: 1.25x Q10 = 1.705 (above 1) and shared-slope P = 0.769. The step means are lower in 1.25x at every step, which is consistent with the paper's other sentence ("a decrease"). |
| fig2g-cb-q10-075-unchanged | reproduced | Cell 37, reading Q-a: Q10 1.723 and 1.712, F(1,171) = 0.006, P = 0.936. The degrees of freedom match the paper exactly. |
| fig2h-cb-q10-125-unchanged | reproduced | Cell 38, readings W-a and Q-a: 1.673 and 1.705, F(1,148) = 0.087, P = 0.769, with 152 points. This matches the paper exactly. |
| fig2f-cb-mixed-model | partially_reproduced | Cell 41: no reading gives the full pattern. Two of three terms hold under 6 of 8 readings. Under S-b (n = 11) salinity is significant (P = 0.015); under S-a with frequency the interaction is not (P = 0.28). The tests are Wald tests, not lmerTest's, but the problem 3 argument shows this cannot move the outcome. |
| fig2i-cb-neuron-crash-counts | reproduced | Cell 33: 9 of the 10 counts match exactly. For "all three crashed at the same temperature", the cell 33 table has exactly 9 of 20 ramps where all three neurons crashed, each within ≤1 °C (less than one 2 °C step). The notebook's own two readings give 4 and 9, but its "9" counts a different set of ramps (problem 2). |
| fig2i-cb-neuron-crash-temps-similar | reproduced | Cell 34: P = 0.32, 0.069 and 0.20 (Wald χ²) and 0.34, 0.11 and 0.25 (F scale), all above 0.05. A Geisser-Greenhouse correction would only raise them. |
| fig3b-ha-frequency-q10 | reproduced | Cell 44, readings Q-a and P-a: Q10 1.434 [1.24, 1.66], F(1,8) = 35.72, P = 0.00033. This matches the paper exactly. |
| species-frequency-at-10c | reproduced | Cell 45, reading R-a: n = 19 and 15, 1.206 and 0.563 Hz (tolerance ±0.03), Welch P = 2e-15. |
| fig3c-ha-phase-constant | reproduced | Cell 46: only PY on is below 0.05 (P = 0.024 for Q-a). All five Q10s are within tolerance (0.915, 0.910, 1.010, 1.160, 0.979). |
| fig4b-ha-075-frequency-unchanged | blocked (data_missing) | No lobster salinity-series file appears among the Lobster STNS.zip names (cell 18), and no table holds the series. This is plausible but rests on file names only (section C). |
| fig4d-ha-125-frequency-unchanged | blocked (data_missing) | Same as fig4b. |
| fig4e-ha-salinity-crash-fractions | blocked (data_missing) | Same as fig4b. |
| fig5b-ha-lp-crashes-before-py | blocked (data_missing / too_large) | Per-neuron lobster crash temperatures are not tabulated. LP and PY burst files exist for 6 of 19 preparations (cell 65), so only a subset below the paper's n could be tested. The `1x saline` sheet and the `.mat` files were never shown (section C). |
| fig5c-ha-mixed-model | partially_reproduced | Cell 48: temperature and the interaction are significant under every reading, salinity under none (P = 0.07 to 0.79). The model used 14/19/14 ramps where the paper used n = 10/14/8 (problem 4), so this is provisional. |
| fig5d-ha-q10-salinity-unchanged | not_reproduced | Cell 49, Q-a: the 0.75x set gives F(1,210) = 4.04, P = 0.046 (paper F(1,209) = 3.50, P = 0.063). The 1.25x set gives P = 0.098 under Q-a and 0.034 under Q-b. All four Q10s are within tolerance, but the criterion counts a P just below 0.05 as not reproduced. The miss is marginal and rests on one data point per set (problem 5). |
| fig6a-ha-py-crash-temp-salinity | blocked (data_missing) | Depends on fig5b. |
| fig6b-ha-lp-crash-temp-salinity | blocked (data_missing) | Depends on fig5b. |
| fig7a-species-q10-075 | reproduced | Cell 51, Q-a: 1.716 and 1.404, F(1,250) = 12.18, P = 0.0006. This matches the paper exactly. |
| fig7b-species-q10-1x-similar | reproduced | Cell 52, Q-a: 1.604 and 1.436, F(1,353) = 3.042, P = 0.082. This matches the paper exactly. Under Q-b, P = 0.0025. |
| fig7c-species-q10-125 | reproduced | Cell 53, readings T-c and Q-a: 1.609 and 1.253, F(1,175) = 9.371, P = 0.0026. This matches the paper exactly. |
| fig7e-species-crash-temp-1x | not_reproduced | Cell 54: both means match (30.21 and 27.62 °C), but crab n = 20, not 21, and Welch P = 0.0603. The deposited Prism result gives the same P = 0.0603 with n = 20. |
| fig7df-species-crash-temp-075-125-similar | reproduced | Cell 55: Mann-Whitney P = 1.000 at 0.75x and Welch P = 0.145 at 1.25x (paper 0.08), both above 0.05. All four means are within tolerance. Crab 1.25x has n = 9 against the paper's 10. |
| fig8-invivo-rhythm-maintained | partially_reproduced | Cell 63: all 58 exposures pass readings B-a and B-b. However, the rule also passes shuffled traces in 90–99% of windows (problem 6), so it cannot detect a crash. Each "1-h" exposure holds only 32 min (cell 62), so the full-hour part of the claim cannot be tested. A noise-calibrated variant holds in 51 of 58. |
| fig9-15h-mortality | blocked (data_missing) | The deposit has one 32-min "15Hours" recording (cell 58) and no survival records. The Zenodo descriptions, which I queried, mention none. |

### B. Problems

1. **[affects a conclusion] fig8, cell 63 and `band_present`.** The "peak above 3× median" rule cannot fail. The notebook's own shuffled traces pass it in 0.90–0.99 of windows. On synthetic data I got 0.96 for white noise and 1.00 for brown noise. The criterion also requires every spectrogram to be shown, and cell 64 shows 2 of 58. Two crab exposures (animal 18 at 0.25x and 0.5x) have a median peak at 2.3–2.4 Hz, and nobody checked whether that is the pyloric band.
2. **[does not affect a conclusion] fig2i counts, cell 33 `same_ii`.** Reading (ii) is the author's own and is not in the paper or the claims file. It counts ramps where one neuron never crashed (953_092, 888_090, 888_112, 888_150, 888_155). Its total of 9 is a coincidence. The paper's wording ("all three neurons crashed") fits "all three crashed, within one step", which also gives 9 of 20 from the same table.
3. **[does not affect a conclusion] `mixed_model` (cells 41, 48) and `neuron_mixed` (cell 34).** These use statsmodels Wald tests, not lmerTest's Satterthwaite F tests or Prism's Geisser-Greenhouse correction. Wald tests are anti-conservative, and none of the decisive P values would cross 0.05 in the direction that changes an outcome. Random-effect structures whose fit failed get AIC = inf and are dropped silently. The Bayes-factor step was skipped. In cell 41, salinity as a factor (S-c) has 2 df while the paper prints 1.
4. **[affects a conclusion] fig5c, cell 48.** The paper's n = 10 (0.75x), 14 (1x) and 8 (1.25x) almost exactly matches the ramps with a "Crash" mark in Sheet4: 10, 13 and 8 (cell 7). The notebook fitted all 14/19/14 ramps and never ran the subset the paper's n points to. Whether salinity becomes significant under that subset is untested.
5. **[affects a conclusion] fig5d, cell 49.** The deposit gives 214 and 176 points where the paper has 213 and 175: one extra point in each set. The extra point was not identified. Since P sits on 0.05 (0.046 against the paper's 0.063), the outcome depends on it. Removing the 111122 duplicate gives P = 0.052, but the paper's degrees of freedom show it kept that copy.
6. **[affects a conclusion] fig8, cells 59 and 62.** Seven pairs of identical recordings are filed under different animals or salinities, so there are 51 distinct recordings among the 58 one-hour exposures. Every exposure holds only the first 32 min, so reading B-a ("in at least half the windows of the hour") cannot be applied as written.
7. **[does not affect a conclusion] Cell 15.** It says `Lobster_Q10s_1x&075x.mat` carries 120722's values under 111122. No cell reads any `.mat` file, so this statement has no output behind it.
8. **[does not affect a conclusion] fig1e, cell 66.** The blocked reason ignores the three counts that can be read from the salinity table (0.75x, 1.25x, 1.5x). The notebook could have reported them as a partial test.
9. **[does not affect a conclusion] fig1d, cell 29.** The rows "888_136 (1)" and "888_136 (2)" (cell 21) enter as two preparations. The paper's n = 10 implies it did the same, but there are only 9 distinct animals.
10. **[does not affect a conclusion] `abf_signal`.** It is annotated as returning a 2-tuple but returns 3 values. Files are decimated separately and joined across gaps of up to 1130 s (crab 16 at 1.5x), so some windows straddle a gap.

Checks that passed:
- On synthetic data, `semilog_fit`, `zero_slope_test` and `shared_slope_test` behave correctly: the Q10 is recovered, and P is small only when the slopes truly differ.
- They reproduce the deposited Prism outputs exactly in 7 comparisons.
- `rhythm_crash` reproduces the Prism crab crash temperatures exactly at 1x and 0.75x.

### C. What I could not check, and the output that would have let me

- **Lobster per-neuron crash data (fig5b, 6a, 6b).** I could not see whether it is in the lobster `1x saline` sheet (43×34, mostly unshown), the four `.mat` files, or the crab `Phase (Salinity)` sheet. A printout of those sheets' headers and a key listing of each `.mat` file would settle it.
- **Lobster salinity series (fig4b, 4d, 4e).** I could not confirm they are absent. The names of the 14 xlsx and 1404 txt files in Lobster STNS.zip, and the member list of at least one inner Raw Crab zip, would have done so.
- **fig8 crash judgement.** All 58 spectrograms (the criterion asks for them), plus the per-window peak frequency, would show whether the 2.3 Hz peaks in crab 18 are the pyloric rhythm.
- **fig5c.** A mixed-model run restricted to the Sheet4 ramps with a Crash mark (10/13/8).
- **fig5d.** A diff of the 1x-control points against the Prism or `.mat` fit data, to find the one extra point per set.
- **fig2i "same temperature".** A step-binned count (crash temperature rounded to the 2 °C ramp step), to confirm my 9 of 20 reading in code and not by eye.

## End of run

14 turns, 4 minutes, $1.61 at API prices, result: success.
