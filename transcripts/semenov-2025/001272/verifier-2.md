# 001272 · verifier-2 · run 41338176202

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 4516
drwxr-xr-x 6 runner runner     4096 Nov  1 19:08 .
drwxr-xr-x 7 runner runner     4096 Nov  1 19:08 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:42 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:42 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov  1 19:08 .claude
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.development
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.local
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.production
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.test
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .env.test.local
drwx------ 2 runner runner     4096 Nov  1 19:08 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:42 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:42 .github
-rw-r--r-- 1 runner runner        0 Nov  1 19:08 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 18:42 .idea
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat round-1-report.md; echo ======; cat README.md
```

```
## Verifier report, round 1: DANDI:001272 (Semenov et al. 2025)

**Materials mismatch, read this first.** The claims file I was given is the one for DANDI:001273. Its header says "on dandiset 001273", `dataset.id: "001273"`, and it has 17 claims. The notebooks cite a different file, `claims/001272/10.1016-j.xcrp.2025.102660.yaml`, with header items F1–F6 and O1–O6 and claim ids that are not in my file (figs1-eight-neurons, figs1-aps-as-emission-decrease, fig1-20khz-needs-twice-the-field, fig4-orientation-and-poles, and others). I had neither that file nor the attempt record. So:
- Table A1 gives outcomes for the 17 claims in the file I have. Only one of them, figs1-di8-anepps-control, is assigned to 001272.
- Table A2 gives outcomes for the notebook's own figs1 claims, judged against the criteria as the notebook quotes them. I could not check those criteria against their source.

### A1. Claims in the claims file provided

| Claim | My outcome | Reason |
|---|---|---|
| figs1-di8-anepps-control | not_reproduced | The archive holds 3 subjects and 65 files, not 8 neurons (API: `numberOfSubjects` 3). Every neuron fires, and latency falls with field (Spearman rho < 0 in 3 of 3 under 10 of 12 readings, cell 18). But no neuron's highest field ends in depolarization by the file's rule (no late APs, mean dF > 5%): late mean dF at the top fields is 1.0, 3.3 and 1.7% (cell 20). Two of the three neurons were only tested up to 234 V/cm. The file's "rise ≥ 5% within 5 ms" AP reading was not run, but failing under one reading is enough. |
| fig1-pure-sine-excites-all | not_reproduced | Under all 12 readings the median first-AP latency at threshold is 15–77 ms, below the 90–220 ms window. The median ceiling is outside 54–99 Hz in 8 of 12 readings, including all four whole-frame ones (fluovolt cell 10). |
| fig2d-modulated-thresholds-higher | not_reproduced | In every reading at least one 20/2-kHz ratio is outside 1.8–2.2; whole-frame ratios are 2.27–2.83 (fluovolt cell 12). No rea
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 001272-semenov-2025-01.yaml
```

```
<persisted-output>
Output too large (45.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/3d337319-425e-41c4-8484-7eab1b2323c6/tool-results/btuygse5r.txt

Preview (first 2KB):
schema_version: 2
id: 001272-semenov-2025-01
dataset:
  archive: dandi
  id: "001272"
  version: 0.250805.1358
  doi: 10.48324/dandi.001272/0.250805.1358
paper: doi:10.1016/j.xcrp.2025.102660
date: 2026-11-01
entry: 001272-semenov-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.xcrp.2025.102660.yaml
```

```
<persisted-output>
Output too large (33.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/3d337319-425e-41c4-8484-7eab1b2323c6/tool-results/b4j9pkmdt.txt

Preview (first 2KB):
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001272.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its
# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available; the supplement's figures were read from their legends only. Values shown only in
# figures (the traces of Figure S1, the n per group of Figure 2D) are not used.
#
# Code. The paper states "This paper does not report original code". It names the software used:
# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear
# regression, Origin 8.0 for fits, Sim4Life 5.2 for the field, and RStudio in Table S1. No
# repository was read, so no method detail below is settled by code.
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/3d337319-425e-41c4-8484-7eab1b2323c6/tool-results/b4j9pkmdt.txt"
}
```

```
1	# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
2	# on dandiset 001272.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md version pilot-10, as the reader.
5	#
6	# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its
7	# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
8	# Figures S1 to S4 and Table S1, the Key Resource Table), all in
9	# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
10	# available; the supplement's figures were read from their legends only. Values shown only in
11	# figures (the traces of Figure S1, the n per group of Figure 2D) are not used.
12	#
13	# Code. The paper states "This paper does not report original code". It names the software used:
14	# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear
15	# regression, Origin 8.0 for fits, Sim4Life 5.2 for the field, and RStudio in Table S1. No
16	# repository was read, so no method detail below is settled by code.
17	#
18	# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
19	# week on 12-mm coverslips. A single neuron with no apparent somatic contact is centred in the
20	# field, with a bipolar tungsten electrode (two 100-um rods, 120-um gap, 45 degrees, tips 50 um
[... 502 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/3d337319-425e-41c4-8484-7eab1b2323c6/tool-results/btuygse5r.txt"
}
```

```
1	schema_version: 2
2	id: 001272-semenov-2025-01
3	dataset:
4	  archive: dandi
5	  id: "001272"
6	  version: 0.250805.1358
7	  doi: 10.48324/dandi.001272/0.250805.1358
8	paper: doi:10.1016/j.xcrp.2025.102660
9	date: 2026-11-01
10	entry: 001272-semenov-2025
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
[... 622 more lines not kept]
```

**Agent**

Materials now include the matching claims file (19 claims) and an attempt record with 19 outcomes. Next I'll dump the notebooks' code and text outputs.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--- out:'); print(''.join(d['text/plain']))
            elif 'image/png' in d: print('--- [image]')
        if o.get('output_type')=='error': print('--- ERROR', o.get('ename'), o.get('evalue'))
EOF
for n in di8_controls fluovolt_elsewhere strobe_check; do python3 $TMPDIR/dump.py $n.ipynb > $TMPDIR/$n.txt; wc -l $TMPDIR/$n.txt; done; grep -n "ERROR" $TMPDIR/*.txt | head
```

```
1319 /tmp/claude-1001/di8_controls.txt
1147 /tmp/claude-1001/fluovolt_elsewhere.txt
445 /tmp/claude-1001/strobe_check.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/di8_controls.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Di-8-ANEPPS controls of Semenov et al. (2025), on DANDI:001272
4	
5	Paper: Semenov, Kim, Silkuniene & Pakhomov (2025), "Excitation and polarization of isolated neurons
6	by high-frequency sine waves for temporal interference stimulation", Cell Reports Physical Science
7	6, 102660, doi:10.1016/j.xcrp.2025.102660.
8	
9	Dataset: DANDI:001272, "The Use of Di8-ANEPPS to Evaluate Neuronal Sensitivity to Unmodulated Sine
10	Waves", version 0.250805.1358. The paper cites the dandiset without a version. Two versions are
11	published, 0.250701.1622 and 0.250805.1358; both hold the same 65 files with the same blobs (checked
12	below), so the most recent published version is pinned.
13	
14	Claims: `claims/001272/10.1016-j.xcrp.2025.102660.yaml`, written from the NIH author manuscript
15	(PMC12320893) with its STAR Methods and supplement. Its header items F1 to F6 and O1 to O6 are cited
16	below by label; the helper `sinewave.py` says where every parameter comes from.
17	
18	The FluoVolt reference group of the two `with_inputs` claims comes from the paper's other deposits,
19	DANDI:001032 (0.240527.1432), 001033 (0.240527.1432) and 001035 (0.240527.1432): their 250-ms
20	unmodulated 2-kHz sessions in NaCl solution. DANDI:001034 (0.240527.1431) is loaded only to show
[... 736 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/di8_controls.txt",
 "offset": 757,
 "limit": 570
}
```

```
757	    b/b/a                     3           3.0                        3       True
758	    b/b/b                     2           2.0                        2       True
759	whole/a/a                     2           1.0                        1      False
760	whole/a/b                     3           3.0                        3       True
761	whole/b/a                     1           0.0                        1      False
762	whole/b/b                     3           2.0                        3       True
763	reproduced under 10 of 12 readings; under height (b): 6 of 6
764	
765	height as prominence, width 1-20 ms
766	  reading    subject  fields_with_aps   rho     p sustained_firing  max_rate_hz reproduced
767	    a/a/a 2_20240806                8 -0.75 0.000             True         79.1        NaN
768	    a/a/a 3_20240806               12 -0.18 0.384             True         52.3        NaN
769	    a/a/a 4_20240806                7 -0.27 0.307             True        171.5        NaN
770	    a/a/b 2_20240806                8 -0.67 0.001             True         51.4        NaN
771	    a/a/b 3_20240806               13 -0.04 0.825             True         52.3        NaN
772	    a/a/b 4_20240806                7 -0.56 0.025             True        171.5        NaN
773	    a/b/a 2_20240806                8 -0.75 0.000             True         79.1        NaN
774	    a/b/a 3_20240806               12 -0.18 0.384             True         52.3        NaN
775	    a/b/a 4_20240806                7 -0.27 0.307             True        171.5        NaN
776	    a/b/b 2_20240806                8 -0.67 0.001             True         51.4        NaN
[... 544 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fluovolt_elsewhere.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# FluoVolt experiments of Semenov et al. (2025), on the paper's other deposits
4	
5	Paper: Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
6	doi:10.1016/j.xcrp.2025.102660. Claims: `claims/001272/10.1016-j.xcrp.2025.102660.yaml`, the claims
7	marked `data: elsewhere`.
8	
9	The paper deposited its raw images in ten dandisets without saying which figure is in which; the
10	claims file assigns them from their titles. Pinned here, each at its most recent published version
11	(the paper cites none):
12	
13	- DANDI:001032, 001033 and 001035 (0.240527.1432): 250-ms sine waves at many frequencies, unmodulated
14	  and modulated at 20 Hz ("spindle"), FluoVolt, NaCl solution. Figures 1 and 2.
15	- DANDI:001034 (0.240527.1431) duplicates 001032 file for file (`di8_controls.ipynb` shows it) and is
16	  not used.
17	- DANDI:001030 (0.240520.1924): 2-s ramped 2-kHz sine waves in sodium gluconate solution. Figure 3C.
18	- DANDI:001271 (0.250805.1352): tetrodotoxin and vehicle. Figure S2.
19	
20	| Claim | Data | Here |
[... 606 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fluovolt_elsewhere.txt",
 "offset": 627,
 "limit": 530
}
```

```
627	whole/a/a        84       10        0              19                               19               0.96             1             0           39       False
628	whole/a/b        84       10        0              19                               19               0.96             1             0           39       False
629	whole/b/a        84       10        0              19                               19               0.96             1             0           39       False
630	whole/b/b        84       10        0              19                               19               0.96             1             0           39       False
631	reproduced under 8 of 12 readings
632	
633	variant, height as prominence
634	  reading  sessions  max_aps  over_10  sessions_5plus  sessions_5plus_mostly_in_window  all_aps_in_window  sust_depol_a  sust_depol_b  sust_firing  reproduced
635	    a/a/a        84       17       27              73                               54               0.61             0             0           73       False
636	    a/a/b        84        6        0              20                               20               0.90             0             0           40        True
637	    a/b/a        84       17       27              73                               54               0.61             0             0           73       False
638	    a/b/b        84        6        0              20                               20               0.90             0             0           40        True
639	    b/a/a        84       20       44              79                               53               0.58             0             0           76       False
640	    b/a/b        84        7        0              17                               17               0.88             0             0           37        True
641	    b/b/a        84       20       44              79                               53               0.58             0       
[... 507 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/strobe_check.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Strobe imaging of membrane charging (Figure 4), on DANDI:001273
4	
5	Paper: Semenov et al. (2025), Cell Reports Physical Science 6, 102660, doi:10.1016/j.xcrp.2025.102660.
6	Dataset: DANDI:001273, "Kinetics of Membrane Charging and Its Dependence on Neuron Shape and Alignment
7	with the Electric Field", version 0.250805.1356, the most recent published version (the paper cites
8	none).
9	
10	The claims fig4-pooled-time-constants and fig4-orientation-and-poles of
11	`claims/001272/10.1016-j.xcrp.2025.102660.yaml` defer their fits and readings to the claims file for
12	DANDI:001273, whose header items are cited as 001273-F1 to F5 and 001273-O1 to O5. That header (F2)
13	says the fits are run unscaled where the debris ROI is not available, recorded as a deviation. No
14	debris ROI is deposited, so the fits here are unscaled. This notebook first shows one experiment in
15	detail, then fits every experiment of 7 or 8 replicates under every reading.
16	
17	| Claim | Here |
18	|---|---|
19	| fig4-pooled-time-constants | tested, unscaled (001273-F2) |
20	| fig4-orientation-and-poles | blocked: the cell-shape groups are not in the files (001273-O4) |
[... 426 more lines not kept]
```

**Agent**

Notebooks read. I'm checking one figure (the 2-s traces for neuron c7) before writing, since the fig3c outcome depends on whether the late detections at 2.3 V are real APs.

**Agent calls Bash**

```bash
cd  python3 -c "
import json,base64
nb=json.load(open('fluovolt_elsewhere.ipynb'))
for o in nb['cells'][27]['outputs']:
    if 'data' in o and 'image/png' in o['data']:
        open('$TMPDIR/c27.png','wb').write(base64.b64decode(o['data']['image/png']))
"; python3 -c "
from PIL import Image; im=Image.open('$TMPDIR/c27.png'); print(im.size)
w,h=im.size; im.crop((0,int(h*0.47),w,int(h*0.85))).save('$TMPDIR/c27c.png')"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image; im=Image.open('/tmp/claude-1001/c27.png'); print(im.size)
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c27.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "178\b\|1,090\|1090\|dark\|gluconate" di8_controls.txt fluovolt_elsewhere.txt strobe_check.txt | grep -v "^.*178.0" | head -20; grep -n "frame0\|dark" strobe.py | head
```

```
di8_controls.txt:1029:their titles). 001030 holds only 2-s ramped waves in sodium gluconate, so none of its sessions fit.
di8_controls.txt:1042:                           naglu=r["nagluconate"], n=r["n_frames"], v=r["volts"]) for r in recs])
di8_controls.txt:1276:(n = 2 or 3, mean 108 to 152 V/cm) and FluoVolt (n = 20 to 27, mean 140 to 178 V/cm) 1-AP thresholds
fluovolt_elsewhere.txt:17:- DANDI:001030 (0.240520.1924): 2-s ramped 2-kHz sine waves in sodium gluconate solution. Figure 3C.
fluovolt_elsewhere.txt:29:| fig3b-low-conductivity-halves-threshold | none | blocked: no deposit holds 250-ms sessions in sodium gluconate |
fluovolt_elsewhere.txt:74:                        volts=r["volts"], pp=r["peak_to_peak"], naglu=r["nagluconate"], n_frames=r["n_frames"],
fluovolt_elsewhere.txt:80:      "| amplitude stated peak-to-peak:", int(fv.pp.sum()), "of", len(fv), "| sodium gluconate:", int(fv.naglu.sum()))
fluovolt_elsewhere.txt:87:l30 = pd.DataFrame([dict(subject=r["subject"], volts=r["volts"], naglu=r["nagluconate"], n_frames=r["n_frames"],
fluovolt_elsewhere.txt:91:      f"(stated as one polarity); sodium gluconate {int(l30.naglu.sum())}; frames {dict(l30.n_frames.value_counts())} "
fluovolt_elsewhere.txt:107:frame rates: [np.float64(3086.4)] | frames per file: {1200: np.int64(414), 900: np.int64(38), 1400: np.int64(1), 1800: np.int64(1)} | amplitude stated peak-to-peak: 454 of 454 | sodium gluconate: 0
fluovolt_elsewhere.txt:113:001030: 17 sessions; neurons ['c5', 'c6', 'c7', 'c8']; volts [np.float64(1.0), np.float64(1.25), np.float64(1.45), np.float64(1.5), np.float64(1.7), np.float64(1.75), np.float64(2.0), np.float64(2.3)] (stated as one polarity); sodium gluconate 17; frames {7000: np.int64(15), 6000: np.int64(2)} at [np.float64(3134.8)] frames/s; the description puts the onset at 25 ms and the end at 2,025 ms
fluovolt_elsewhere.txt:519:    b/b/b  mod 234 (n=2) vs pure 221 (n=12), p=0.8869  mod 432 (n=2) vs pure 373 (n=8), p=0.5744     mod 518 (n=1) vs pure 442 
[... 6 more lines not kept]
```

**Agent**

## Verifier report, round 2: DANDI:001272 (Semenov et al. 2025)

The claims file is now the right one (`dataset.id: "001272"`). It has 19 claims, and the attempt record has 19 outcomes, one for each claim.

### 1. Outcomes and assumptions

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| figs1-eight-neurons | not_reproduced | Yes | 3 subjects (di8 cell 14). |
| figs1-aps-as-emission-decrease | reproduced | Yes | 12 of 12 readings (cell 17). |
| figs1-near-threshold-delayed-aps | partially_reproduced, assumed | **No** | The two assumptions are stated. Prominence is well founded (null test 0.02 against 1.43 per 100 ms, cell 11). O5 (a) has a source in the paper. But under those assumptions the criterion is met in 0 of 24 combinations under O5 (a) (cell 20): only 1 of 3 neurons qualifies, and more than half are needed. The criterion is one per-neuron test that needs "1–3 APs" and "delayed" together. It does not split into parts. So the outcome under the assumptions is not_reproduced. "Partially" only describes the halves of that test. |
| figs1-stronger-field-shorter-delay-sustained-firing | reproduced, assumed | Yes | The assumptions (prominence, height (b)) are stated and reasonable, and the outcome is the same with the value reading. One caveat: subject 3's rho is −0.03 (p 0.88). It counts as negative only because the criterion looks at the sign alone. |
| figs1-culminates-in-sustained-depolarization | not_reproduced | Yes | Subjects 2 and 4 were never stimulated above 234 V/cm, so in effect only subject 3 tests this claim. |
| figs1-noisier-than-fluovolt | not_reproduced | Yes | The SD is higher for Di-8-ANEPPS in 0 of 12 readings. |
| figs1-effects-same-as-fluovolt | partially_reproduced, assumed | Yes, with a caveat | The criterion does not cover the case "pattern fails, no threshold difference", so partial is a fair call. Unit reading (i) is stated, but its only basis is the 001271 check (p = 0.29), and reading (ii) flips the result (difference in 9 of 12 readings). With n = 2–3 and 95% intervals as wide as −156 to 124 V/cm, "no difference" carries almost no information. |
| fig1-pure-sine-excites-all | not_reproduced | Yes | 0 of 12 readings, also in all three variants (cell 11). |
| fig1-20khz-needs-twice-the-field | not_reproduced | Yes | 0 of 12 (cell 14). The nominal-volts caveat is stated. |
| fig2d-modulated-thresholds-higher | not_reproduced | Yes | 0 of 12. Under whole/a/a and whole/b/a it fails only at p = 0.0500. |
| fig2-modulated-locks-to-beats | partially_reproduced, assumed | Yes | The whole-frame assumption is stated and backed by the sham and null tests. |
| fig2c-pure-more-aps | reproduced | Yes | 12 of 12 readings, under all three variants. |
| fig3b-low-conductivity-halves-threshold | blocked (other) | Yes | In substance this is data_missing; the notes explain why it is recorded as other. |
| fig3c-sustained-firing-2s | partially_reproduced, assumed | Yes | The cell 27 figure supports the prominence assumption. At 2.3 V, c7 fires about 6 APs, then sits on a flat plateau with no visible APs, so the 9 late detections under the value reading are noise. c8 at 2.0 V also looks like a block in the figure, so partial may be conservative. Two weaknesses: no null test was run on 001030, and the two bleaching corrections subtract the same trace from c7's sessions (c7 at 1.0 V is the only AP-free session), so "either correction" is one check, not two. |
| figs2-ttx-blocks-depolarization | reproduced, assumed | Yes, by the criterion | The second part passes on 1 neuron (14_20240731). No TTX neuron has a late mean above 5% before TTX (cell 30). The record states this. |
| fig4-pooled-time-constants | not_reproduced | Yes | 0 of 8 readings, also with whole-frame scaling (cell 9). The unscaled fits follow 001273-F2. 22 experiments against 19 is recorded as a deviation. |
| fig4-orientation-and-poles | blocked (metadata_insufficient) | Yes | The files have no cell-shape groups. |
| fig6-sine-less-than-pulse | blocked (other: not attempted) | Yes | The record is accurate, but the data are in 001274. |
| threshold-depolarization-estimate | blocked | Yes | One note: its first expected value, 57.7 ± 3.6 V/cm, already fails on either stated scale (140–178, or 70–89 V/cm if halved). |

**Possible gaps in the claims file (reported, not corrected):**
- **fig2-modulated-locks-to-beats:** the statement includes "triggered no sustained firing", but the criterion tests only sustained depolarization. The O6 rule for sustained firing (3 APs with one in the last 50 ms) is met by firing locked to the beats (45–46 of 84 modulated sessions, cell 20), so it does not fit this claim.
- **figs2-ttx-blocks-depolarization:** the criterion is conditional, so the depolarization part passes trivially when no neuron is depolarized before TTX. The paper describes a depolarization that the intense sine waves caused, which means it was present before TTX.
- **figs1-effects-same-as-fluovolt:** the criterion has no outcome for "pattern fails, no threshold difference".

### 2. Sentences the printed outputs do not support

**Attempt record:**
- figs1-stronger…, deviation: "the Di-8-ANEPPS APs measured here have a median height of 4.1 to 6.6%". The printed values are 3.73–6.67% (di8 cell 31).
- figs1-near…, deviation: "Under O5 (b) … (12 of 24)". With the 1-ms bound the outputs give 13 of 24 (value) and 20 of 24 (prominence). 12 of 24 is the old 2-ms result (cell 20).
- figs1-culminates…: "(with 2 ms also with the Otsu ROI and level (b))". No per-neuron table is printed for 2 ms. Cell 27 and its output give this result for prominence, not for 2 ms.
- fig1-pure-sine…: "these readings detect peaks before the onset and after the stimulus at nearly the rate during it". For a/a/a and a/b/a the rates are 1.10 and 1.06 per 100 ms against 2.47, a little under half (fluovolt cell 7). The response under fig2-modulated-locks-to-beats repeats the phrase.
- fig2-modulated-locks…: "001032 neuron 2_1, 11 V" is not printed anywhere.
- fig3b notes: "0 of 1,090 mention gluconate" is not printed. The notebook shows 0 of 454 (fluovolt cell 4).
- Findings: "All 178 files" of 001034 are identical to 001032. Only 80 of 80 2-kHz files are shown (di8 cell 29).
- Findings: 001272 files say "without tetrodotoxin (vehicle control)", and 001271 files say TTX "caused sustained depolarization". Neither description text is printed in any output.
- The other numbers in the record notes match the outputs.

**Notebooks:**
- fluovolt cell 21: "detect peaks … at nearly the rate during it". The same objection as above applies to ROI (a).
- fluovolt cell 8: "so most of its detections are noise". This holds for ROI (b) (2.1–2.4 against 3.33–3.37 per 100 ms) but not for ROI (a) (about 43%). The same cell says "2.44 to 3.38"; the printed maximum is 3.37.
- strobe cell 14: "the first acquired frame of every file is dark". This appears only in `strobe.py`, with no printed output behind it.
- All other "**Result:**" conclusions, the three Summary sections and the README match the outputs.

**My round-1 reasons in the record:** they are stated in my own words, mostly verbatim, and each sits under the right claim. Two small points:
- For threshold-depolarization-estimate, my outcome was "not_reproduced (threshold part); rest untested". The record shortens this to not_reproduced.
- fig4-orientation-and-poles combines my three separate fig4 rows. The combination is fair.

### 3. Round-1 points

**Resolved:**
- 1, the claims-file mismatch. With this file, my round-1 objections on fig3c (the window and the 5% level) and on figs2 (the 5% level) no longer apply.
- 2, the TTX pass on sustained depolarization: the record now says it rests on 1 of 6 neurons.
- 3, noise counted as APs on a raised baseline, for Di-8-ANEPPS.
- 4, the detector null test.
- 5, the degenerate eroded ROI.
- 6, the hard-coded text.
- 7, the wording on the amplitude scale.
- 8, the strobe fits: all 22 experiments are now fitted, fits stuck at a bound are flagged and left out, and the bleach-corrected variant has been added.
- 10, the fig3c window.
- 11, the truncated files and pooled latencies.

**Remaining, and bearing on a conclusion:**
- figs1-near-threshold-delayed-aps: under its stated assumptions the outcome should be not_reproduced (section 1).
- fig3c-sustained-firing-2s: the prominence reading decides the outcome (0 of 4 neurons with the value, 1 of 4 with prominence) and has no null test on 001030. For FluoVolt the record uses prominence only for fig3c and the value reading elsewhere. That includes figs2, where prominence would fail (3–4 TTX neurons keep detections). Each choice has a stated reason, but each is the reading that favours the claim.
- figs2-ttx-blocks-depolarization: the depolarization half rests on one neuron.
- figs1-effects-same-as-fluovolt: the outcome depends on the undeposited amplitude scale and an underpowered test.
- Point 9: fig6-sine-less-than-pulse and threshold-depolarization-estimate are still not attempted, though the data are in 001274.
- fig4-pooled-time-constants: 58 of 352 charging fits are left out at a bound, and the signal is a median 1.97 times the pre-pulse SD. The failure may come from the missing debris scaling, as the record says.

## End of run

16 turns, 4 minutes, result: success.
