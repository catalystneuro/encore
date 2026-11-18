# xia-2021 · author-revise-2 · run 44268222891

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/xia-2021/verifier-2-report.md; ls entries/xia-2021 questions/ transcripts/xia-2021
```

```
Wed Nov 18 08:37:58 UTC 2026
**Verifier report: Xia et al. 2021, attempt xia-2021-01, round 2**

The claims file has 29 claims. The attempt record gives 4 reproduced, 5 partially reproduced, 3 not reproduced and 17 blocked: 15 for missing data, 1 for insufficient metadata and 1 as not runnable. The notebook tests 12 claims (cell 0).

### 1. Outcomes

| Claim | Agree? | Notes |
|---|---|---|
| fig2d-hplc-yield (partial, assumed) | Yes, by the letter of the criterion | Reading (b), a straight line under each peak, gives 77.5–83.1% (4 of 18 readings; cell 21). The volumes cannot be tested without a flow rate, so partial is the most the attempt can give. The assumption (the second peak ends where its descent ends) is stated and reasonable. **But** the passing reading's line runs from the valley and cuts away 46% of the main peak (area 27.25 → 14.61) and 70% of the second peak (12.71 → 3.86). Cell 20 says itself that this line "cuts through the second peak". Every reading that splits the overlap the usual way gives 65.8–69.1%, just below the 69.3% floor. The conclusion should say this. |
| fig2e-page-bands (reproduced) | Yes | Cell 24 bears it out. |
| figs5-btx-staining (reproduced) | Yes | The judgement is by eye. Nearness to GFP beats chance in 3 of 4 images (0.82 vs 0.37 in the low-magnification projection). |
| fig3d-sensor-on-soma (partial, assumed) | Yes | Coincidence beats the shifted null in 4 of 5 images. The soma localisation is at chance, and (b) is 0.09–0.35. The assumption is stated and reasonable. |
| fig4b-michaelis-menten (not reproduced, assumed) | Yes | 0 of 80 readings. The onset assumption is stated, and a single common onset still gives Km 0.545 µM. |
| fig4b-lod (not reproduced, assumed) | Yes | 0 of 160 crossings. Reading (c) is still not run, and the record says so. |
| fig5b-in-vivo-response (not reproduced, assumed) | Yes | dF/F is 17.1–40.1%, and 0 of 144 readings fit. The assumption about which recordings stand for the three mice is stated. |
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md | head -80; ls attempts 2>/dev/null | grep xia; ls; cat questions/xia-2021.yaml 2>/dev/null | head -50
```

```
713 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
443:### 4. Lock, check and run
463:### 5. Record the attempt
538:### 6. Hand over for verification
576:## Repeat attempts
641:## Local and remote datasets
664:## Verifier
668:### Round 1: without the author's conclusions
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,575p docs/protocol.md
```

```
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

### 1. Establish what can be tested

Do this before any analysis.

[... 357 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 664,713p docs/protocol.md
```

```
## Verifier

Be skeptical. Do not assume the analysis is right.

### Round 1: without the author's conclusions

1. Read the notebook, the helper module and the claims file. The paper is
   under `paper/`; the claims file decides what is tested and how, and a place
   where it misreads the paper is reported, not corrected.
2. Check the code: that every number derives from the loaded data; that
   every method choice is the one the claim's criterion gives or, for a
   detail the criterion lacks, the one the passage cited in the notebook or
   the helper gives, and none is the author's own unless stated as an
   assumption; that
   a detail the paper leaves open, where it could change the outcome, was
   run under every reading the paper allows; that each assumption is
   stated and reasonable, given the paper, the
   methods it cites, the code it links and the field's practice (an
   unreasonable one is a problem that affects a conclusion, and the author
   revises it); that selection, conditions and analysis windows follow the
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/xia-2021-01.yaml
```

```
<persisted-output>
Output too large (51.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e7c65af-4557-4648-93ea-2f9972f0fbc0/tool-results/bwm1rqqp3.txt

Preview (first 2KB):
schema_version: 3
id: xia-2021-01
datasets:
- archive: sparc
  id: '108'
  version: '1'
  doi: 10.26275/w027-cisv
  relation: primary
- archive: sparc
  id: '75'
  version: '1'
  doi: 10.26275/prjd-jhoc
  relation: primary
paper: doi:10.1073/pnas.2023807118
date: '2026-11-18'
entry: xia-2021
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7e7c65af-4557-4648-93ea-2f9972f0fbc0/tool-results/bwm1rqqp3.txt"
}
```

```
1	schema_version: 3
2	id: xia-2021-01
3	datasets:
4	- archive: sparc
5	  id: '108'
6	  version: '1'
7	  doi: 10.26275/w027-cisv
8	  relation: primary
9	- archive: sparc
10	  id: '75'
11	  version: '1'
12	  doi: 10.26275/prjd-jhoc
13	  relation: primary
14	paper: doi:10.1073/pnas.2023807118
15	date: '2026-11-18'
16	entry: xia-2021
17	provenance:
18	  kind: agent
19	  accountable:
20	    name: CatalystNeuro
[... 745 more lines not kept]
```

**Agent**

Next I'll read the claims for fig7, figs12 and fig2d, and the notebook cells the report cites.

**Agent calls Bash**

```bash
ls claims | grep xia; python - <<'EOF'
import yaml
c=yaml.safe_load(open('claims/xia-2021.yaml'))
for cl in c['claims']:
    if cl['id'] in ('fig2d-hplc-yield','fig7-peak-timing','fig7-rostral-caudal','figs12-3v-propagation'):
        print(yaml.safe_dump(cl,width=120,sort_keys=False)); print('----')
EOF
grep -rn "proposed" schemas/*attempt* | head; grep -ln "proposed:" attempts/*.yaml | head -3
```

```
xia-2021.yaml
xiao-2026.yaml
id: fig2d-hplc-yield
statement: In size-exclusion HPLC the assembled nanosensors elute first (main peak near 7.5 mL), followed by a second peak
  at 9.1 to 9.2 mL of unreacted material, and the nanosensors are about 77% of the reaction mixture by area under all peaks
  of the pHAb channel.
source: Results, Fabrication and in vitro characterization, paragraph 2 (beginning "Fully assembled ACh nanosensors were purified");
  Figure 2D
quote: "ACh nanosensors represent \u223C77% of the reaction mixture based on the integration of areas under all detectable\
  \ peaks from the pHAb channel chromatogram"
datasets:
- sparc-108
expected:
- quantity: nanosensor share of pHAb-channel peak area
  value: 77
  tolerance: 7.7
  unit: '%'
- quantity: main peak retention volume
  value: 7.5
  tolerance: 0.75
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 280,360p schemas/attempt*.json; grep -n -B3 -A8 "proposed:" attempts/gabriel-2025-01.yaml | head -40; grep -n "agrees\|outcome" schemas/attempt*.json | head -40
```

```
"type": "number"
              },
              {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "number"
                }
              }
            ]
          },
          "deviations": {
            "description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          },
          "assumed": {
[... 96 more lines not kept]
```

**Agent**

Now the notebook structure.

**Agent calls Bash**

```bash
cd entries/xia-2021 && python - <<'EOF'
import json
nb=json.load(open('reproduce_xia_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),len(src),repr(src[:110]))
EOF
wc -l xia2021.py; ls ../../executed/xia-2021/
```

```
0 markdown None 4461 '# Reproducing Xia et al. (2021) from SPARC:108 and SPARC:75\n\n**Paper.** Xia J, Yang H, Mu M, Micovic N, Poskan'
1 code None 1046 'import io\nimport re\nimport resource\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy '
2 code None 1221 "# Every file this notebook reads, with its size and SHA-256 from the pinned version's manifest (the header's\n#"
3 markdown None 178 '## Data check\n\nWhat each dataset holds, read from its manifest, its SDS sheets and the files themselves. Each '
4 code ['sanity'] 1125 'for ds in ("108", "75"):\n    m = X.manifest(ds)\n    files = m["files"]\n    print(f"SPARC:{ds} version {m[\'vers'
5 markdown None 459 'SPARC:108 has six subjects in `subjects.xlsx`, with their experiment groups (calibration curve, dose-dependent'
6 code ['sanity'] 794 'man = pd.read_excel(io.BytesIO(X.read_bytes("108", "files/primary/manifest.xlsx")))\nprint("manifest.xlsx colum'
7 markdown None 807 'The primary `manifest.xlsx` describes the files under names that differ from the deposited ones (for example\n`'
8 code ['sanity'] 2293 'V = {}\nrows = []\nMAPS = {}   # block onset/peak maps of the pHAb half of sub-2 and sub-3 (fig7 and figs12), un'
9 markdown None 1766 'Frames are 16-bit counts from a Hamamatsu C11440-22C camera (binning 4, 50 ms exposure); the files carry no\nsp'
10 code ['sanity'] 2219 'def z_from_pre(tr, n_pre=X.STIM_FRAME):\n    pre = tr[:n_pre]\n    return (tr - pre.mean()) / pre.std()\n\nrows = '
11 markdown None 1682 '**Clock.** The files do not record when the stimulation was given. The paper puts its start at 10.45 s in\nFig.'
12 code ['sanity'] 1090 'from skimage.registration import phase_cross_correlation\n\ndef aligned_r(a, b):\n    h, w = min(a.shape[0], b.sh'
13 markdown None 647 'sub-2 (3 V) and sub-3 (8 V) were recorded 14 minutes apart on the same day and their mean images match with no'
14 code ['sanity'] 1585 'CAL = X.calibration_movies()\nrows = []\nfor c in CAL:\n    a = c["fr
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open('executed/xia-2021/reproduce_xia_2021.ipynb'))
for i in map(int,sys.argv[1:]):
    c=nb['cells'][i]
    print(f'===== CELL {i} ({c["cell_type"]})'); print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print('--OUT--'); print(''.join(o['data']['text/plain']))
EOF
python $TMPDIR/show.py 20 21 22
```

```
===== CELL 20 (markdown)
## fig2d-hplc-yield

> In size-exclusion HPLC the assembled nanosensors elute first (main peak near 7.5 mL), followed by a second
> peak at 9.1 to 9.2 mL of unreacted material, and the nanosensors are about 77% of the reaction mixture by
> area under all peaks of the pHAb channel.

Criterion: the area of the first peak over the summed area of all detectable peaks of the pHAb chromatogram,
(a) limits at the minima between peaks with a flat baseline at the pre-injection level, (b) the same with a
linear baseline under each peak; share 69.3 to 84.7%, main peak 6.75 to 8.25 mL, second peak 8.19 to 10.12 mL.

Details not in the claims file. "Detectable" is taken as a prominence of at least 1% of the largest peak
(0.5% as a variant), a choice made here. The start of the first peak is where the signal rises above the
pre-injection level plus 3 SD (the first 5 min, before any peak). The end of the last peak is open, and three
ends are run: (i) where the signal returns to the pre-injection level plus 3 SD; (ii) the end of the peak's own
descent, the first point after it where the slope (101-sample running mean) falls below 1% of the steepest
slope of the chromatogram; (iii) where the signal falls below 2% of the peak's height. Ends (ii) and (iii)
leave out the low tail after about 21 min, which (i) gives to the second peak. Reading (b) is run as written
(a line under each peak, from its limits) and as a common line from the start of the first peak to the end of
the last, with a vertical drop at the valley, the usual way to split two overlapping peaks on a sloped
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py 11 47 48 49 50 51 52
```

```
<persisted-output>
Output too large (36.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7e7c65af-4557-4648-93ea-2f9972f0fbc0/tool-results/bobesuntc.txt

Preview (first 2KB):
===== CELL 11 (markdown)
**Clock.** The files do not record when the stimulation was given. The paper puts its start at 10.45 s in
Fig. 6A and Fig. 7A, frame 19 on its 0.55 s clock (`STIM_FRAME`). In sub-2, sub-3 and sub-6 after washout each
tissue trace departs from baseline (|z| > 5 against frames 0 to 18) 4 to 13 frames after frame 19, at frame 23
to 34. In sub-3 (8 V) the first change is a drop in both channels, followed by the rise in one. With the drug,
sub-6 has no frame with |z| > 5 and rises by at most 3.3%. sub-4 (10 V) first
departs at frame 55, so its stimulation did not start at 10.45 s; it is used by no tested claim. Its whole trace
(printed and plotted) holds one response: one peak of 8.7% at frame 99, with |z| > 5 from frame 78 to 210 and the
signal near or below baseline before and after. It holds no repeated stimulations, so fig5e-reversibility cannot be
tested on it, and no 3 V or 5 V recording of the same ganglion exists for fig5c-voltage-dose. That the responses start after
frame 19 is consistent with the stated onset; it does not prove it.

**Channels.** In sub-2 and sub-3 the right half rises after stimulation (by 27.1% and 48.1% over the tissue)
and the left half does not rise above its baseline; the right half is taken as pHAb and the left as AF647. The files do not label
them, so this is an assumption, and figs16-af647-stable rests on it. (While preparing, outside this notebook, the
time-lapse panels of Fig. 7A, the nanosensor signal of the 8 V recording, were compared with sub-3 and match its right
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7e7c65af-4557-4648-93ea-2f9972f0fbc0/tool-results/bobesuntc.txt"
}
```

```
1	===== CELL 11 (markdown)
2	**Clock.** The files do not record when the stimulation was given. The paper puts its start at 10.45 s in
3	Fig. 6A and Fig. 7A, frame 19 on its 0.55 s clock (`STIM_FRAME`). In sub-2, sub-3 and sub-6 after washout each
4	tissue trace departs from baseline (|z| > 5 against frames 0 to 18) 4 to 13 frames after frame 19, at frame 23
5	to 34. In sub-3 (8 V) the first change is a drop in both channels, followed by the rise in one. With the drug,
6	sub-6 has no frame with |z| > 5 and rises by at most 3.3%. sub-4 (10 V) first
7	departs at frame 55, so its stimulation did not start at 10.45 s; it is used by no tested claim. Its whole trace
8	(printed and plotted) holds one response: one peak of 8.7% at frame 99, with |z| > 5 from frame 78 to 210 and the
9	signal near or below baseline before and after. It holds no repeated stimulations, so fig5e-reversibility cannot be
10	tested on it, and no 3 V or 5 V recording of the same ganglion exists for fig5c-voltage-dose. That the responses start after
11	frame 19 is consistent with the stated onset; it does not prove it.
12	
13	**Channels.** In sub-2 and sub-3 the right half rises after stimulation (by 27.1% and 48.1% over the tissue)
14	and the left half does not rise above its baseline; the right half is taken as pHAb and the left as AF647. The files do not label
15	them, so this is an assumption, and figs16-af647-stable rests on it. (While preparing, outside this notebook, the
16	time-lapse panels of Fig. 7A, the nanosensor signal of the 8 V recording, were compared with sub-3 and match its right
17	half; this is not run here, as the entry reads no figures, and it decides nothing.)
18	
19	**Recordings deposited twice.** The next cell compares the mean images.
20	===== CELL 47 (markdown)
[... 299 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py 45 46 53 54 55 56 57 | cut -c1-260; python $TMPDIR/show.py 28 43 | grep -v "^--OUT"
```

```
===== CELL 45 (code)
s3 = V["sub-3 8V"]
rows = []
for bl in ("a", "b"):
    for roi in ("own tissue mask", "whole half", "pHAb mask on AF647"):
        if roi == "own tissue mask":
            af, ph = s3["left"]["tissue"], s3["right"]["tissue"]
        elif roi == "whole half":
            af, ph = s3["left"]["full"], s3["right"]["full"]
        else:
            af, ph = s3["left"]["by_right_mask"], s3["right"]["tissue"]
        res = {}
        for name, tr in (("AF647", af), ("pHAb", ph)):
            n = len(tr); rec = ON + int(round(120 / X.FRAME_S_FILE))
            idx = np.r_[0:ON, rec:n] if bl == "a" else np.arange(n)
            corr, _ = X.bleach_correct(tr, idx)
            d = X.dff(corr, ON, "mean")
            res[name] = d
        a, p = res["AF647"], res["pHAb"]
        noise = a[:ON].mean() + 3 * a[:ON].std()
[... 218 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py 42 | grep -n "0.010\|bin" | head -20; python $TMPDIR/show.py 27 | grep -i "per 100\|density\|first" | head -20; cd  && python -c "
import yaml
c=yaml.safe_load(open('claims/xia-2021.yaml'))
for cl in c['claims']:
    if cl['id']=='fig4b-lod': print(cl['criterion'])
"; cat questions/README.md | head -60; cat questions/yu-2017.yaml | head -40
```

```
29:                    nb_ = int(round(10 / dt)); nbins = m // nb_   # variant: means of non-overlapping 10 s bins, fewer and less dependent samples
30:                    tb = stats.ttest_rel(dw[:nbins * nb_].reshape(nbins, nb_).mean(1), do[:nbins * nb_].reshape(nbins, nb_).mean(1))
33:                                 "t_10s_bins": round(tb.statistic, 2), "p_10s_bins": tb.pvalue, "n_bins": nbins})
40:print(f"paired t over the means of 10 s bins ({R6.n_bins.min()} to {R6.n_bins.max()} bins): p {R6.p_10s_bins.min():.2g} to {R6.p_10s_bins.max():.2g}; "
41:      f"below 0.01 in {int((R6.p_10s_bins < 0.01).sum())} of {len(R6)} readings")
69:  dt bleach baseline          roi  median3  peak_with  peak_without  ratio_%  reduction_%  paired_t             p  n_frames  t_10s_bins  p_10s_bins  n_bins  ratio_ok  reduction_ok
70:0.50      a     mean       tissue    False       4.09         18.45     22.2         77.8    -12.78  7.050998e-29       241       -3.09    0.010333      12     False          True
82:0.50      b     mean       tissue    False       4.31         19.48     22.1         77.9    -28.76  1.033677e-79       241       -7.62    0.000010      12     False          True
83:0.50      b     mean       tissue     True       3.47         18.95     18.3         81.7    -32.07  9.565189e-89       241       -7.68    0.000010      12      True          True
88:0.50      b    first       tissue    False       5.47         18.90     29.0         71.0    -22.31  1.889227e-60       241       -5.92    0.000101      12     False          True
120:paired t over the means of 10 s bins (12 to 12 bins): p 2.2e-06 to 0.14; below 0.01 in 37 of 48 readings
print("background rule: reflected (median + 3 SD of the reflected lower half, the rule used since round 1) and lower_half (the first version)")
background rule: reflected (median + 3 SD of the reflected lower half, the rule used since round 1) and lower_half (the first version)
The paper does not say how the points are split into th
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; grep -rn -i "10 to 15\|44.55\|22.0 s\|rostral" paper/* | cut -c1-600 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 728,800p paper/10.1073-pnas.2023807118.txt; grep -n -i "electrode\|lingual nerve" paper/10.1073-pnas.2023807118.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/xia-2021; cat README.md; grep -n "minute" reproduce_xia_2021.ipynb | head; date -u
```

```
# Xia, Yang, Mu, Micovic, Poskanzer, Monaghan & Clark (2021) from SPARC:108 and SPARC:75

Tests the findings of [Xia et al. (2021)](https://doi.org/10.1073/pnas.2023807118), a DNA-based nanosensor
for acetylcholine imaged in the submandibular ganglion of living mice, on the two SPARC datasets that hold its
data: [SPARC:108](https://sparc.science/datasets/108) version 1 (doi:10.26275/w027-cisv), the deposit the
paper cites, and [SPARC:75](https://sparc.science/datasets/75) version 1 (doi:10.26275/prjd-jhoc), confocal
images of a ganglion stained with BTX or the nanosensor.

| Claim | Outcome |
|---|---|
| HPLC: nanosensors are 77% of the pHAb peak area (Fig. 2D) | Partially reproduced (share holds under one baseline reading; volumes not testable) |
| Native PAGE: several slower bands carrying pHAb and AF647 (Fig. 2E, S2C) | Reproduced |
| BTX staining is punctate across the ganglion (Fig. S5) | Reproduced |
| Nanosensor AF647 and pHAb puncta overlap on the somata (Fig. 3D) | Partially reproduced |
| Ex vivo Michaelis-Menten calibration, Km 49 uM (Fig. 4B) | Not reproduced |
| Lower limit of detection 228 nM (Fig. 4B) | Not reproduced |
| In vivo response of 3.7% at 3 V (Fig. 5B) | Not reproduced |
| Vesamicol cuts the response by 77% (Fig. 6) | Partially reproduced |
| The AF647 channel does not respond (Fig. S16) | Reproduced |
| Rostral-to-caudal spread at 8 V (Fig. 7A-B) | Partially reproduced (order holds, times do not; block onsets in place of AQuA) |
[... 20 more lines not kept]
```

**Agent**

Clock reads 08:39 UTC, plenty of time. Editing the notebook code cells now.

**Agent calls Bash**

```bash
cat > $TMPDIR/edit.py <<'PYEOF'
import json
P='reproduce_xia_2021.ipynb'
nb=json.load(open(P))
def get(i): return ''.join(nb['cells'][i]['source'])
def put(i,s):
    lines=s.split('\n'); nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+([lines[-1]] if lines[-1] else [])
def rep(i,old,new):
    s=get(i); assert s.count(old)==1,(i,old[:60],s.count(old)); put(i,s.replace(old,new))

# fig2d: valley height, area kept by reading (b), tail level
rep(21, '''      f"{ok['main share (%)'].min():.1f} to {ok['main share (%)'].max():.1f}%")
''', '''      f"{ok['main share (%)'].min():.1f} to {ok['main share (%)'].max():.1f}%")
pk1, _ = find_peaks(y, prominence=0.01 * (y.max() - base))
v_i = peak_limits(y, pk1[:2], base + 3 * base_sd, "i return to pre-injection + 3 SD")[1]
print(f"valley between the two peaks: {y[v_i]:.2f} at {t[v_i]:.2f} min (main peak {y.max():.2f}, pre-injection {base:.3f})")
H1 = H[H.detectable == "1.0%"]
for end in H1["end of 2nd peak"].unique():
    fa = H1[(H1["end of 2nd peak"] == end) & (H1.reading == "a flat baseline")].areas.iloc[0]
    ba = H1[(H1["end of 2nd peak"] == end) & (H1.reading == "b line under each peak")].areas.iloc[0]
    print(f"  end {end}: the line under each peak (b) keeps {100 * ba[0] / fa[0]:.0f}% of the main peak's area above the flat "
          f"baseline and {100 * ba[1] / fa[1]:.0f}% of the second peak's")
''')
rep(21, '''for ch in ("260_NM", "280_NM", "652_NM"):''', '''m = (t >= 21) & (t < 30)
print(f"  signal 21-30 min: {y[m].min():.3f} to {y[m].max():.3f}, {y[m].min() / base:.1f} to {y[m].max() / base:.1f} times the pre-injection level")
for ch in ("260_NM", "280_NM", "652_NM"):''')

# figs16: does AF647 pass its pre-stimulus mean after its minimum
rep(45, '''"AF647 rise from its minimum (%)": round(a[ON + 1 + np.argmin(a[ON + 1:]):].max() - a[ON + 1:].min(), 2),''',
 '''"AF647 rise from its minimum (%)": round(a[ON + 1 + np.argmin(a[ON + 1:]):].max() - a[ON + 1:].min(), 2),
                     "AF647 highest after its minimum (%)": round(a[ON + 1 + np.argmin(a[ON + 1:]):].max(), 2),''')
rep(45, '''print(R16.to_string(index=False))
''', '''print(R16.to_string(index=False))
print(f"after its minimum the AF647 trace passes its pre-stimulus mean (0%) in {int((R16['AF647 highest after its minimum (%)'] > 0).sum())} of {len(R16)} "
      f"readings and its pre-stimulus mean + 3 SD in {int((R16['AF647 highest after its minimum (%)'] > R16['AF647 pre-onset mean+3SD (%)']).sum())}")
''')

# fig7: orientation variants
rep(48, '''def region_table(key):
    mask = V[key]["right"]["mask"]
    out = []
    for (k_, size, k, fit), a in MAPS.items():
        if k_ != key:
            continue
        a = a[a[:, 2] >= 0]
''', '''def flipped(a, mask, rows_flip, cols_flip):
    a = a.copy()
    r_, c_ = np.flatnonzero(mask.any(1)), np.flatnonzero(mask.any(0))
    if rows_flip:
        a[:, 0] = r_.min() + r_.max() - a[:, 0]
    if cols_flip:
        a[:, 1] = c_.min() + c_.max() - a[:, 1]
    return a

ORIENT = (((False, False), "as deposited (rostral up, lateral left)"), ((True, False), "flipped top to bottom"),
          ((False, True), "flipped left to right"), ((True, True), "turned 180 degrees"))

def region_table(key, flip=(False, False)):
    mask = V[key]["right"]["mask"]
    out = []
    for (k_, size, k, fit), a in MAPS.items():
        if k_ != key:
            continue
        a = flipped(a[a[:, 2] >= 0], mask, *flip)
''')
rep(48, '''      f"largest p {T3['p(rho row)'].max():.2g}; with the column (left is lateral): {T3['rho(onset, column)'].min()} to {T3['rho(onset, column)'].max()}")
''', '''      f"largest p {T3['p(rho row)'].max():.2g}; with the column (left is lateral): {T3['rho(onset, column)'].min()} to {T3['rho(onset, column)'].max()}")
print("\\nThe files carry no orientation. The order under each way the frame could be turned (regions redrawn on the turned frame):")
for flip, name in ORIENT:
    Tf = region_table("sub-3 8V", flip)
    print(f"  {name}: rostral < caudal regions < lateral in {int(Tf['order 1<2,3<4'].sum())} of {len(Tf)} variants; "
          f"rostral region first in {int((Tf['R1 onset'] < Tf[['R2 onset', 'R3 onset', 'R4 onset']].min(axis=1)).sum())}")
''')

# fig7-peak-timing: the paper's own times under both readings
rep(51, '''a = MAPS[("sub-3 8V", 16, 3.0, "a")]; a = a[a[:, 2] >= 0]''', '''stim_s = X.STIM_FRAME * X.FRAME_S_PAPER
print(f"the paper's own times (claim fig7-rostral-caudal): reading (i) rostral {exp['R1 peak'] - stim_s:.2f} s, most caudal {exp['R3 peak'] - stim_s:.2f} s; "
      f"reading (ii) rostral {exp['R1 peak'] - exp['R1 onset']:.2f} s, most caudal {exp['R3 peak'] - exp['R3 onset']:.2f} s (9-16.5 s to pass)")
a = MAPS[("sub-3 8V", 16, 3.0, "a")]; a = a[a[:, 2] >= 0]''')

# figs12: orientation variants
rep(54, '''print(f"Spearman rho of block onset with the row: {T2['rho(onset, row)'].min()} to {T2['rho(onset, row)'].max()}, largest p {T2['p(rho row)'].max():.2g}")
''', '''print(f"Spearman rho of block onset with the row: {T2['rho(onset, row)'].min()} to {T2['rho(onset, row)'].max()}, largest p {T2['p(rho row)'].max():.2g}")
for flip, name in ORIENT:
    Tf = region_table("sub-2 3V", flip)
    print(f"  frame {name}: rostral region first in {int((Tf['R1 onset'] < Tf[['R2 onset', 'R3 onset', 'R4 onset']].min(axis=1)).sum())} of {len(Tf)} variants")
''')
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit.py && git diff --stat
```

```
entries/xia-2021/reproduce_xia_2021.ipynb | 41 +++++++++++++++++++++++++++++--
 1 file changed, 39 insertions(+), 2 deletions(-)
```

**Agent**

Formatting preserved. The whole notebook takes about 100 s, so I'll run the full entry now.

**Agent calls Bash**

```bash
cd  && time python tools/entry.py all entries/xia-2021 2>&1 | tail -20
```

```
Installed kernelspec registry-xia-2021 in executed/xia-2021/.venv/share/jupyter/kernels/registry-xia-2021
0 error(s)
pass  reproduce_xia_2021.ipynb  (122 s)

real	2m14.522s
user	1m41.624s
sys	0m9.416s
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py 21 45 48 51 54 56 | grep -v "^ \{0,8\}\(16\|32\|1\.0%\|0\.5%\|a \|b \)" | grep -A40 "^--OUT" | grep -v "^ *block px\|detectable" | head -120
```

```
--OUT--
pre-injection level 0.0425 (SD 0.0051) over the first 5 min

readings with a share within 69.3-84.7%: 4 of 18; share over the readings with positive areas 65.8 to 69.1%
valley between the two peaks: 5.19 at 17.27 min (main peak 13.62, pre-injection 0.043)
  end i return to pre-injection + 3 SD: the line under each peak (b) keeps 54% of the main peak's area above the flat baseline and -136% of the second peak's
  end ii end of descent (slope < 1% of steepest): the line under each peak (b) keeps 54% of the main peak's area above the flat baseline and 30% of the second peak's
  end iii below 2% of the peak height: the line under each peak (b) keeps 54% of the main peak's area above the flat baseline and 23% of the second peak's

retention times: main 15.16 min, second 18.05 min; second / main 1.191 (paper 9.1-9.2 / 7.5 = 1.213-1.227)
flow rate that would put the main peak at 7.5 mL: 0.495 mL/min (not given in the paper; not a test)
  signal 19-20 min: mean 1.189, min 0.567, max 2.025 (pre-injection 0.043; main peak 13.62)
  signal 20-21 min: mean 0.349, min 0.250, max 0.566 (pre-injection 0.043; main peak 13.62)
  signal 21-23 min: mean 0.199, min 0.165, max 0.250 (pre-injection 0.043; main peak 13.62)
  signal 23-25 min: mean 0.151, min 0.101, max 0.173 (pre-injection 0.043; main peak 13.62)
  signal 25-27 min: mean 0.115, min 0.093, max 0.136 (pre-injection 0.043; main peak 13.62)
  signal 27-30 min: mean 0.111, min 0.055, max 0.150 (pre-injection 0.043; main peak 13.62)
  signal 30-35 min: mean 0.081, min 0.049, max 0.125 (pre-injection 0.043; main peak 13.62)
  signal 21-30 min: 0.055 to 0.250, 1.3 to 5.9 times the pre-injection level

[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py 45 48 51 54 56 | grep -i "orient\|flipped\|turned\|as deposited\|paper's own\|i from\|ii from\|per block\|own tissue\|whole half\|pHAb mask on\|variants where\|total run\|3 V below"
```

```
for roi in ("own tissue mask", "whole half", "pHAb mask on AF647"):
        if roi == "own tissue mask":
        elif roi == "whole half":
     a    own tissue mask                3.54                          4.11                     -13.00                            15.76                                 2.77              50.07             14.1                True
     a         whole half                1.35                          1.97                     -15.16                            16.50                                 1.35              46.90             34.8                True
     a pHAb mask on AF647                1.53                          1.94                     -13.27                            14.80                                 1.53              50.07             32.7                True
     b    own tissue mask                3.70                          4.14                     -12.77                            11.68                                -1.09              54.01             14.6                True
     b         whole half                0.38                          1.92                     -15.36                            11.13                                -4.23              50.85            135.0                True
     b pHAb mask on AF647                1.18                          1.89                     -13.42                            11.63                                -1.79              54.01             45.7                True
def flipped(a, mask, rows_flip, cols_flip):
ORIENT = (((False, False), "as deposited (rostral up, lateral left)"), ((True, False), "flipped top to bottom"),
          ((False, True), "flipped left to right"), ((True, True), "turned 180 degrees"))
        a = flipped(a[a[:, 2] >= 0], mask, *flip)
print("\nThe files carry no orientation. The order under each way the frame could be turned (regions redrawn on the turned frame):")
for flip, name in ORIENT:
The files carry no orientation.
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit2.py <<'PYEOF'
import json
P='reproduce_xia_2021.ipynb'
nb=json.load(open(P))
def get(i): return ''.join(nb['cells'][i]['source'])
def put(i,s):
    lines=s.split('\n'); nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+([lines[-1]] if lines[-1] else [])
def rep(i,old,new):
    s=get(i); assert s.count(old)==1,(i,old[:60],s.count(old)); put(i,s.replace(old,new))

# cell 11: orientation is not decided by nothing
rep(11, '''half; this is not run here, as the entry reads no figures, and it decides nothing.)''',
 '''half; this is not run here, as the entry reads no figures. It does not decide the channels, which rest on which half rises.)''')

# fig2d conclusion
put(22, '''**Result: partially reproduced, resting on an assumption about where the second peak ends.** The pHAb
chromatogram has two detectable peaks, at 15.16 and 18.05 min (a third, small one at 37.27 min passes the 0.5%
rule). The share of the first peak depends on the reading. With a flat baseline (reading a) it is 65.8 to 68.2%
under every end of the second peak, below the tolerance of 69.3 to 84.7%; so is a common line under both peaks
with a drop at the valley (66.2 to 69.1%). With a line under each peak (reading b, as the criterion writes it),
the share is 77.5 to 83.1%, within tolerance, when the second peak ends where its own descent ends (end ii,
20.53 min) or where it falls below 2% of its height (end iii, 20.94 min); when it ends where the signal returns
to the pre-injection level (end i, 29.76 min), the line from the valley (5.19 high, at 17.27 min) runs above the
low tail and the second area is negative, which is no share. From 21 to 30 min the signal is 0.055 to 0.250,
1.3 to 5.9 times the pre-injection level, against a main peak of 13.62; end (i) counts that tail in the second
peak. Ends (ii) and (iii), where a peak's own descent ends, are the usual limits of a peak, so the share holds
under reading (b), 4 of 18 readings in all. That reading has a cost: as the valley is high, the line under each
peak cuts through both peaks, keeping 54% of the main peak's area above the flat baseline and 30% (end ii) or
23% (end iii) of the second peak's. Every reading that splits the overlap the usual way (a flat baseline, or a
common line with a drop at the valley) gives 65.8 to 69.1%, just below the tolerance. The share therefore holds
by the letter of the criterion's reading (b) only. The retention volumes cannot be tested: the paper gives no
flow rate, and the rate that would put the main peak at 7.5 mL (0.495 mL/min) is read from the data. The ratio
of the two retention times, 1.191, is 1.8% below the paper's 1.213 to 1.227. Partially reproduced: the share
holds under one reading of the criterion, a reading that cuts away part of each peak, and the volume part cannot
be tested.''')

# figs5
rep(28, '(11.4 to 64.4 with the first', '(17.8 to 64.4 with the first')

# fig6: p of main reading's bin test
rep(43, '''twelve 10 s bins it gives p of 2.2e-06 to 0.14, below 0.01 in 37 of 48 readings.''',
 '''twelve 10 s bins it gives p of 2.2e-06 to 0.14, below 0.01 in 37 of 48 readings; under the first reading
(0.50 s, fit a, mean baseline, tissue) it is 0.0103, not below 0.01.''')

# figs16
rep(46, '''stimulation, as the pHAb channel does at first (data check), and recovers by 11.1 to 16.5% from that minimum
without passing its pre-stimulus level.''', '''stimulation, as the pHAb channel does at first (data check), and rises by 11.1 to 16.5% from that minimum.
After the minimum it passes its pre-stimulus mean in 3 of 6 readings (by 1.35 to 2.77%, all with the bleaching
curve fit outside the response), and its pre-stimulus mean plus 3 SD in none.''')

# fig7 header
rep(47, '''frames of sub-3: they show the right half of the frame, not flipped. That comparison is not run here, as the
entry reads no figures, and it decides nothing.)''', '''frames of sub-3: they show the right half of the frame, not flipped. That comparison is not run here, as the
entry reads no figures.) The orientation decides the direction: the cell below runs the frame turned each way.
That the deposited frames are oriented as Figure 7A shows them, with rostral up, is an assumption: the files
are the camera's frames, the paper shows no sign of a flip, and the criterion reads the axis from Figure 7B.''')

# fig7 conclusion
rep(49, '''Partially reproduced, as the criterion says when the order holds but the times do not.''',
 '''The direction rests on the orientation: with the frame flipped top to bottom, or turned 180 degrees, the order
holds in 0 of 18 variants, and flipped left to right also in 0 of 18 (the rostral region still starts first in
all 18, but the lateral region no longer comes last). The frame is taken as deposited, rostral up, an assumption
(see above). Partially reproduced, as the criterion says when the order holds but the times do not, on the frame
as deposited.''')

# fig7-peak-timing conclusion
put(52, '''**Result: reproduced under reading (ii), resting on the substitute for AQuA and on the orientation; asked of
a reader.** Counted from each region's onset (reading ii), the four regions of sub-3 reach their peak in 11.8
to 18.1 s; all four are within 9 to 16.5 s in 30 of 36 variants, every variant with the bleaching curve fit
outside the response (a and c) on both clocks, and at the 0.50 s clock with the whole-trace fit. For the main
variant (16 px blocks, 3 SD, fit a, paper's clock) the times are 14.30, 14.85, 15.40 and 13.48 s, and 126 of
the 157 blocks peak 9 to 16.5 s after their own onset (median 13.8 s). Counted from stimulation onset (reading
i), no variant fits: the regions peak 18.0 to 26.4 s after it, and no block peaks within 16.5 s of it. The pass
is weak. It rests on the region onsets, which come 2.75 to 3.3 s after the paper's for the rostral region (none
of the six times of fig7-rostral-caudal matches); both the onsets and the peaks are late, and their difference
falls in the window. And reading (ii) does not fit the paper's own times: from Figure 7B and the text, the
rostral region peaks 8.80 s after its onset and the most caudal 29.15 s after its own, both outside 9 to 16.5 s,
while reading (i) gives 11.55 s for the rostral region. The claims file flags the paper's contradiction only for
the most caudal region; whether reading (ii) should stand is now asked of a reader (questions/xia-2021.yaml).
The outcome follows the claims file as written, which counts a pass under either reading: reproduced under
reading (ii).''')

# figs12 conclusion
put(55, '''**Result: partially reproduced as verified, with a proposed change to blocked (data missing); one deposited
mouse of three, resting on the substitute for AQuA and on the orientation.** In the mouse stimulated at both
voltages the 3 V response is lower than the 8 V one in all 6 readings (tissue peak 27.1 to 29.0% against 46.9
to 54.0%), and in each of the four regions (block medians 21.1 to 43.6% against 38.0 to 69.9%). At 3 V the
rostral region's onset precedes the other three in 12 of 18 variants, all those with the bleaching curve fit
outside the response (a and c); with the curve fit to the whole trace (b), which takes in part of a response
still 9 to 16% above baseline at 120 s (fig5b-in-vivo-response), it does not. Every earliest block lies in the
rostral third in 11 of 18 variants, and block onset rises with the rostro-caudal position in the fits outside
the response (rho 0.42 to 0.74). With the frame flipped top to bottom or turned 180 degrees, the rostral region
starts first in 0 of 18 variants, so the direction rests on the orientation, as for fig7-rostral-caudal. The
two mice stimulated at 3 V only are not deposited. The criterion's partial outcome needs the order in two of
three mice, which one mouse cannot give, and its full outcome needs all three. The outcome verified in round 1
was partially reproduced; the round-2 verifier found that the threshold cannot be reached, and this revision
agrees and proposes blocked, for missing data, with the results in this one mouse reported as above.''')

# summary rows and text
rep(57, '''| fig7-peak-timing | reproduced (11.8 to 18.1 s from region onset, within 9 to 16.5 s in 30 of 36 variants; block onsets in place of AQuA) |
| figs12-3v-propagation | partially reproduced (one mouse of three; rostral first and lower than at 8 V; block onsets in place of AQuA) |''',
'''| fig7-peak-timing | reproduced (11.8 to 18.1 s from region onset, within 9 to 16.5 s in 30 of 36 variants; none from stimulation onset; block onsets in place of AQuA; whether reading (ii) stands is asked of a reader) |
| figs12-3v-propagation | partially reproduced (one mouse of three; rostral first and lower than at 8 V; block onsets in place of AQuA); proposed: blocked, data missing, as one mouse cannot meet the two of three mice the criterion's partial outcome needs |''')
rep(57, '''| fig2d-hplc-yield | partially reproduced (main peak 77.5 to 83.1% of the pHAb area with a line under each peak, 65.8 to 69.1% otherwise; volumes not testable without the flow rate) |''',
'''| fig2d-hplc-yield | partially reproduced (main peak 77.5 to 83.1% of the pHAb area with a line under each peak, which cuts away 46% of the main peak and 70 to 77% of the second; 65.8 to 69.1% otherwise; volumes not testable without the flow rate) |''')
rep(57, '''caudal and lateral regions, stand in for its events. The HPLC''', '''caudal and lateral regions, stand in for its events, on the frame as deposited (rostral up), an assumption on
which the direction of propagation rests. The HPLC''')
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
cd entries/xia-2021 && python $TMPDIR/edit2.py && git diff --stat; grep -n "—\|rather" reproduce_xia_2021.ipynb | head
```

```
entries/xia-2021/reproduce_xia_2021.ipynb | 139 ++++++++++++++++++++++--------
 1 file changed, 101 insertions(+), 38 deletions(-)
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
python - <<'EOF'
p='README.md'; s=open(p).read()
for o,n in [("It takes about two to three minutes, most of it streaming the files.","It takes about two minutes (113 s in the last run), most of it streaming the files."),
 ("| Responses peak 10 to 15 s after onset (Fig. 7A) | Reproduced (from each region's onset; block onsets in place of AQuA) |",
  "| Responses peak 10 to 15 s after onset (Fig. 7A) | Reproduced (from each region's onset, not from stimulation onset; block onsets in place of AQuA; the reading is asked of a reader) |"),
 ("| Same direction and lower amplitude at 3 V (Fig. S12) | Partially reproduced (one mouse of three) |",
  "| Same direction and lower amplitude at 3 V (Fig. S12) | Partially reproduced (one mouse of three); proposed: blocked, data missing |"),
 ("| HPLC: nanosensors are 77% of the pHAb peak area (Fig. 2D) | Partially reproduced (share holds under one baseline reading; volumes not testable) |",
  "| HPLC: nanosensors are 77% of the pHAb peak area (Fig. 2D) | Partially reproduced (share holds only with a line under each peak, which cuts into both peaks; volumes not testable) |"),
 ("| Rostral-to-caudal spread at 8 V (Fig. 7A-B) | Partially reproduced (order holds, times do not; block onsets in place of AQuA) |",
  "| Rostral-to-caudal spread at 8 V (Fig. 7A-B) | Partially reproduced (order holds, times do not; block onsets in place of AQuA; the direction rests on the frame being rostral up) |")]:
    assert s.count(o)==1,o; s=s.replace(o,n)
open(p,'w').write(s)
EOF
cat ../../questions/xia-2021.yaml 2>/dev/null; ls ../../questions | grep xia
```

```
xiao-2026.yaml
```

**Agent**

Next, the reader question file.

**Agent calls Write**

```json
{
 "file_path": "questions/xia-2021.yaml",
 "content": "questions:\n- claim: fig7-peak-timing\n  asked: 2026-11-18\n  question: >-\n    The criterion reads \"10 to 15 s\" in two ways, from stimulation onset (i) or from each event's own\n    onset (ii), and counts a pass under either. It flags the paper's contradiction only for the most\n    caudal region. But the paper's own Figure 7B and text times do not fit reading (ii) for the\n    rostral-most region either. It rises at 13.20 s and peaks at 22.0 s, 8.80 s after its own onset\n    and outside 9 to 16.5 s, while from stimulation onset (10.45 s) it peaks after 11.55 s, inside the\n    window. Should reading (ii) stand, or does the paper mean reading (i) only, with the most caudal\n    region as the one exception the criterion already names?\n  passage: >-\n    The rostral-most region started to increase fluorescence at 13.20 and 2.75 s after the start of\n    10 s stimulation and peaked at t = 22.0 s, 1.65 s after the last stimulation. ... The decay of\n    fluorescence intensity of the most caudal region begins at t = 44.55 and 24.2 s after the last\n    stimulation (Fig. 7B). ... All evoked nanosensor responses in Fig. 7A climbed to the peak around\n    ~10 to 15 s, an observation consistent with Fig. 5 B-E. (Results, ACh nanosensor response reflects\n    physiological ACh propagation, paragraph 1)\n  why: >-\n    The attempt passes only under reading (ii). The four regions of sub-3, with block onsets in place\n    of AQuA, peak 11.8 to 18.1 s after their own onsets (all four within 9 to 16.5 s in 30 of 36\n    variants), and 18.0 to 26.4 s after stimulation onset (0 of 36 variants, none even with the most\n    caudal region left out). If reading (ii) is dropped, the outcome would be not reproduced, not\n    reproduced. Raised by the round-2 verifier, who would give partially reproduced at most.\n"
}
```

```
File created successfully at: questions/xia-2021.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "questions/xia-2021.yaml",
 "old_string": "the outcome would be not reproduced, not\n    reproduced. Raised",
 "new_string": "the outcome would be not reproduced. Raised"
}
```

```
The file questions/xia-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the attempt record. First, a look at how another attempt records a second round.

**Agent calls Bash**

```bash
cd  grep -n "^- date\|^  by:\|^  reviewed:\|^  kind:" attempts/gabriel-2025-01.yaml | tail -8; grep -n -A6 "^  reviewed:" attempts/gabriel-2025-01.yaml | tail -8; sed -n 425,460p schemas/attempt*.json
```

```
1286:- date: '2026-11-10'
1287:  kind: agent
1288:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
1289:  reviewed: 'Round 2: the full executed notebook of the author-revise-1 run (commit 273a9ebb), the helper module pma.py,
1594:- date: '2026-11-16'
1595:  kind: agent
1596:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
1597:  reviewed: Round 3. Only the two changes of outcome proposed after round 2 (figs2-innate-behaviors and fig3a-decoding-shock-gt-ns)
--
1597:  reviewed: Round 3. Only the two changes of outcome proposed after round 2 (figs2-innate-behaviors and fig3a-decoding-shock-gt-ns)
1598-    and the analysis behind them in the re-executed notebook (cells 56 to 58 and 71 to 74), with the claims file and
1599-    the paper. Report in transcripts/gabriel-2025/verifier-3-report.md.
1600-  results:
1601-  - claim: figs2-innate-behaviors
1602-    agrees: true
1603-    outcome: not_reproduced
              "properties": {
                "claim": {
                  "type": "string"
                },
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
git log --oneline -6; head -30 transcripts/xia-2021/verifier-2.md | cut -c1-300
```

````
d5cce6b Agent run on xia-2021: verifier-2 (success)
# xia-2021 · verifier-2 · run 44266700240

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `Tas

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 3716
drwxr-xr-x 6 runner runner     4096 Nov 18 08:30 .
drwxr-xr-x 8 runner runner     4096 Nov 18 08:30 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 18 08:24 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov 18 08:24 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov 18 08:30 .claude
-rw-r--r-- 1 runner runner        0 Nov 18 08:30 .env
-rw-r--r-- 1 runner runner        0 Nov 18 08:30 .env.development
[... 11 more lines not kept]
````

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
s=open('attempts/xia-2021-01.yaml').read()
d=yaml.safe_load(s)
for w in (110,115,116,117,118,120):
    o=yaml.safe_dump(d,sort_keys=False,width=w,allow_unicode=True)
    print(w,o==s, sum(a!=b for a,b in zip(o.splitlines(),s.splitlines())))
EOF
```

```
110 True 0
115 False 698
116 False 713
117 False 705
118 False 693
120 False 687
```

**Agent**

Round-trip at width 110 is exact, so I'll edit the record in Python.

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/xia-2021-01.yaml'
d=yaml.safe_load(open(P))
O={o['claim']:o for o in d['outcomes']}
def rep(obj,key,old,new):
    assert obj[key].count(old)==1,(key,old); obj[key]=obj[key].replace(old,new)

rep(O['fig2d-hplc-yield'],'notes','second area is negative and no share can be read. 4 of 18 readings are within tolerance.',
 'second area is negative and no share can be read. 4 of 18 readings are within tolerance. The valley between the peaks is 5.19 high (main peak 13.62), so the line under each peak cuts through both peaks; it keeps 54% of the main peak\'s area above the flat baseline and 30% (end ii) or 23% (end iii) of the second peak\'s. Every reading that splits the overlap the usual way (flat baseline, or a common line with a drop at the valley) gives 65.8 to 69.1%, just below tolerance, so the share holds by the letter of reading (b) only.')
rep(O['fig6-vesamicol'],'notes','below 0.01 in 37 of 48.','below 0.01 in 37 of 48, and 0.0103 under the first reading.')
rep(O['figs16-af647-stable'],'notes','recovers by 11.1 to 16.5% from that minimum without passing its pre-stimulus level.',
 'rises by 11.1 to 16.5% from that minimum; after it, the trace passes its pre-stimulus mean in 3 of 6 readings (by 1.35 to 2.77%, all with the bleaching curve fit outside the response) and its pre-stimulus mean + 3 SD in none.')

o=O['fig7-rostral-caudal']
rep(o,'notes','Part of the delay may come','The direction rests on the orientation of the frame, which the files do not record: with the frame flipped top to bottom, flipped left to right or turned 180 degrees, the order holds in 0 of 18 variants (flipped left to right the rostral region still starts first in all 18, but the lateral region is no longer last). Part of the delay may come')
rep(o,'notes','Partially reproduced, as the criterion says when the order holds but the times do not.','Partially reproduced, as the criterion says when the order holds but the times do not, on the frame as deposited.')
ORI=('Assumed that the deposited frames are oriented as Figure 7A shows them, rostral up and lateral to the left; the files carry no orientation, they are the camera\'s frames, the paper shows no sign of a flip, and the criterion reads the axis from Figure 7B. A comparison of the panels of Fig. 7A with sub-3, made outside the notebook as the entry reads no figures, agreed, but it is not part of the test. The direction of propagation rests on this assumption: every other orientation is run and the order fails in all.')
for c in ('fig7-rostral-caudal','fig7-peak-timing','figs12-3v-propagation'):
    O[c]['deviations'].append(ORI)

o=O['fig7-peak-timing']
rep(o,'notes','Reproduced under reading (ii), which the criterion allows.',
 'The pass is weak: it rests on region onsets that come 2.75 to 3.3 s after the paper\'s for the rostral region (none of the six times of fig7-rostral-caudal matches), and reading (ii) does not fit the paper\'s own times, by which the rostral region peaks 8.80 s and the most caudal 29.15 s after their onsets, while reading (i) gives 11.55 s for the rostral region. The claims file flags the paper\'s contradiction only for the most caudal region; whether reading (ii) should stand is asked of a reader (questions/xia-2021.yaml). Reproduced under reading (ii), which the claims file as written allows.')

o=O['figs12-3v-propagation']
rep(o,'notes','every earliest block lies\n','every earliest block lies ') if 'every earliest block lies\n' in o['notes'] else None
rep(o,'notes','Partially reproduced, as the direction and the lower amplitude hold in the one mouse that can be tested.',
 'With the frame flipped top to bottom or turned 180 degrees the rostral region starts first in 0 of 18 variants, so the direction rests on the orientation. Partially reproduced as verified in round 1; a change to blocked (data missing) is proposed, as the criterion\'s partial outcome needs the order in two of three mice, which the one deposited mouse cannot give.')
o['proposed']={'outcome':'blocked','blocked_by':'data_missing','reason':
 'The criterion grants partial reproduction when two of three mice show the order, and full reproduction when all three do and the amplitude holds. Only one of the three mice is deposited (sub-2 and sub-3, one ganglion); the two mice stimulated at 3 V only are not, so neither threshold can be reached and the claim cannot be tested as the criterion states it. In the one mouse, the amplitude part holds (3 V below 8 V in 6 of 6 readings) and the rostral region starts first in 12 of 18 variants (earliest block rostral in 11 of 18), as the notebook prints. Raised by the round-2 verifier.'}

for f in d['findings']:
    if f['kind']=='methods_unavailable':
        f['statement']=f['statement'].replace('giving 17 to 37% against 3.7%','giving 17.1 to 40.1% against 3.7%')
        assert '17.1 to 40.1%' in f['statement']
        f['statement']=f['statement'].replace('Block onsets were used in its place here.','Block onsets were used in its place here, on the frame as deposited; does rostral lie at the top of the deposited frames, as Fig. 7A shows them?')

V2={'date':'2026-11-18','kind':'agent','by':'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 'reviewed':'Round 2: the full executed notebook of the author-revise-1 run with its conclusions and summary, the helper module xia2021.py, the attempt record, the README and the claims file, with the paper. Report in transcripts/xia-2021/verifier-2-report.md.',
 'results':[]}
R=V2['results']
def add(c,agrees,outcome,reason,response): R.append({'claim':c,'agrees':agrees,'outcome':outcome,'reason':reason,'response':response})
add('fig2d-hplc-yield',True,'partially_reproduced',
 'Agrees by the letter of the criterion. Reading (b), a straight line under each peak, gives 77.5 to 83.1% (4 of 18 readings). The volumes cannot be tested without a flow rate, so partial is the most the attempt can give, and the assumption that the second peak ends where its descent ends is stated and reasonable. But the passing reading\'s line runs from the valley and cuts away 46% of the main peak (area 27.25 to 14.61) and 70% of the second (12.71 to 3.86), and every reading that splits the overlap the usual way gives 65.8 to 69.1%, just below the 69.3% floor. The conclusion should say this. In cell 22, "From 21 to 30 min the signal is 0.09 to 0.25, two to six times the pre-injection level" is not supported (the 27 to 30 min minimum is 0.055, about 1.3 times), and the 5.2-high valley is not printed.',
 'Outcome kept. The valley height (5.19) and the share of each peak\'s area that reading (b) keeps (54% of the main, 30% or 23% of the second) are now printed, and the conclusion, the notes and the summary say that the share holds by the letter of reading (b) only and that the usual splits give 65.8 to 69.1%. The 21 to 30 min range is printed and corrected to 0.055 to 0.250, 1.3 to 5.9 times the pre-injection level.')
for c in ('fig2g-conjugation-ratios','figs3-size','fig3bc-retention','figs4-stability','figs6b-unit-calibration','fig4c-control-ph','fig5b-control-minimal','figs8-control-10v','fig5c-voltage-dose','fig5c-ach-concentration','fig5d-pulse-dose','figs7b-in-vitro-reversibility','figs10-control-8v','figs13-two-photon'):
    pass
order=[o['claim'] for o in d['outcomes']]
blocked_reason='Agrees with the 17 blocked claims.'
for c in order:
    if c=='fig2d-hplc-yield': continue
    oc=O[c]['outcome']
    if oc=='blocked':
        r=blocked_reason
        if c=='fig5e-reversibility': r='Agrees with the 17 blocked claims; sub-4 is now shown to hold a single response (cell 10), so fig5e is blocked.'
        if c=='figs9-aqua-vs-roi': r='Agrees with the 17 blocked claims. Accepts not_runnable on the author\'s citation of docs/protocol.md, which the verifier cannot see.'
        add(c,True,'blocked',r,'No change.')
add_map={
 'fig2e-page-bands':(True,'reproduced','Cell 24 bears it out.','No change.'),
 'figs5-btx-staining':(True,'reproduced','The judgement is by eye. Nearness to GFP beats chance in 3 of 4 images (0.82 against 0.37 in the low-magnification projection). In cell 28, "(11.4 to 64.4 with the first rule...)" is not supported: the first-rule densities printed in cell 27 are 17.79 to 64.41.','Outcome kept. Cell 28 corrected to 17.8 to 64.4.'),
 'fig3d-sensor-on-soma':(True,'partially_reproduced','Coincidence beats the shifted null in 4 of 5 images. The soma localisation is at chance, and (b) is 0.09 to 0.35. The assumption is stated and reasonable.','No change.'),
 'fig4b-michaelis-menten':(True,'not_reproduced','0 of 80 readings. The onset assumption is stated, and a single common onset still gives Km 0.545 uM.','No change.'),
 'fig4b-lod':(True,'not_reproduced','0 of 160 crossings. Reading (c) is still not run, and the record says so; this does not change an outcome.','No change. Reading (c) needs the lines of Figure 4B(ii), and the entry reads no figures.'),
 'fig5b-in-vivo-response':(True,'not_reproduced','dF/F is 17.1 to 40.1%, and 0 of 144 readings fit. The assumption about which recordings stand for the three mice is stated. The methods_unavailable finding\'s "giving 17 to 37% against 3.7%" is stale; the current range is 17.1 to 40.1% (cell 39).','Outcome kept. The finding now gives 17.1 to 40.1%.'),
 'fig6-vesamicol':(True,'partially_reproduced','One experiment of four. The reduction is within tolerance in 44 of 48 readings, and the 17% example depends on the ROI. The main reading\'s bin test gives p = 0.0103, which is not below 0.01.','Outcome kept. The conclusion and the notes now give the main reading\'s p of 0.0103.'),
 'figs16-af647-stable':(True,'reproduced','The channel assignment is stated as an assumption. Cell 46 and the record\'s notes say AF647 "recovers by 11.1 to 16.5% from that minimum without passing its pre-stimulus level", but in 4 of 6 readings the rise from the minimum exceeds the drop (own tissue mask, fit a, 15.76 against -13.00; whole half, fit a, 16.50 against -15.16), so the trace passes its pre-stimulus mean, though not the mean + 3 SD.','Outcome kept. The highest AF647 value after its minimum is now printed: the trace passes its pre-stimulus mean in 3 of 6 readings (1.35 to 2.77%, the three with fit a; with fit b the peak of the recovery comes before the minimum ends the drop, so rise and drop do not compare directly) and the mean + 3 SD in none. The conclusion and the notes are corrected.'),
 'fig7-rostral-caudal':(True,'partially_reproduced','Agrees, with a caveat. The order holds in 18 of 18 variants, and no time is within tolerance in any of the 36; the substitute for AQuA and the orientation are both stated. However, the order would reverse if the frame were flipped. Rostral-up rests on a comparison with Fig. 7A made outside the notebook, and the notebook says that comparison "decides nothing" (cells 47, 11). In fact it decides the outcome.','Outcome kept. The notebook now runs the frame turned each way: flipped top to bottom, left to right or 180 degrees, the order holds in 0 of 18 variants. The orientation is recorded as an assumption (a deviation on fig7-rostral-caudal, fig7-peak-timing and figs12), the "decides nothing" wording is removed from cells 11 and 47, and the conclusion says the direction rests on it. The question of orientation is added to the methods_unavailable finding.'),
 'fig7-peak-timing':(False,'partially_reproduced','Would call it partially reproduced at most. It passes only under reading (ii), timed from each region\'s onset (30 of 36 variants). Those onsets come 2.75 to 3.3 s after the paper\'s for the rostral region, and the parent claim matches 0 of 6 times. Timed from the stimulus, reading (i), it fits in 0 of 36 variants and 0 of 157 blocks. Reading (ii) applied to the paper\'s own Fig. 7B times gives 8.8 s for the rostral region (22.0 - 13.20), outside 9 to 16.5 s. The claims file flags the paper\'s contradiction only for the caudal region.',
   'Outcome kept, with the disagreement recorded. The criterion as written counts a pass under either reading, and under reading (ii) all four regions fall within 9 to 16.5 s in 30 of 36 variants; the criterion\'s partial outcome (all but the most caudal) is met under the same reading, so partial would not follow from the criterion either. The verifier\'s point is that reading (ii) does not fit the paper, which is a question about the claims file: it is now asked of a reader in questions/xia-2021.yaml. The notebook now prints the paper\'s own times under both readings (rostral 11.55 s under (i), 8.80 s under (ii); most caudal 34.10 and 29.15 s), and the conclusion and the notes say the pass is weak, for the late onsets and the reading.'),
 'figs12-3v-propagation':(False,'blocked','The criterion grants partial "when two of three show the order". Only one mouse is deposited, so that threshold cannot be reached. The amplitude part holds (6 of 6 readings), and the order holds in 12 of 18 variants on the median onset and 11 of 18 on the earliest block. These results should be reported without the label "partial", or the claim should be blocked for the two missing mice. The direction of propagation also depends wholly on an orientation checked outside the notebook.',
   'Agreed. The outcome stays partially_reproduced, as verified in round 1, and a change to blocked (data_missing) is proposed for round 3, with the one-mouse results kept in the notes. The orientation variants are now run (rostral first in 0 of 18 with the frame flipped top to bottom or turned 180 degrees).'),
}
for c,(a,oc,r,resp) in add_map.items(): add(c,a,oc,r,resp)
R.sort(key=lambda x: order.index(x['claim']))
assert len(R)==29, len(R)
d['verifications'].append(V2)
open(P,'w').write(yaml.safe_dump(d,sort_keys=False,width=110,allow_unicode=True))
PYEOF
python $TMPDIR/rec.py && git diff --stat attempts/
```

```
attempts/xia-2021-01.yaml | 290 ++++++++++++++++++++++++++++++++++++++++++----
 1 file changed, 265 insertions(+), 25 deletions(-)
```

**Agent**

Two fixes needed in what I just wrote: the figs16 response has a muddled clause, and the orientation deviation overstates the left-right flip for figs12.

**Agent calls Bash**

```bash
python - <<'EOF'
P='attempts/xia-2021-01.yaml'
import yaml
d=yaml.safe_load(open(P))
old='every other orientation is run and the order fails in all.'
new='every other orientation is run; flipped top to bottom or turned 180 degrees, the rostral region starts first in no variant, and flipped left to right the lateral region is no longer last at 8 V.'
n=0
for o in d['outcomes']:
    for i,dv in enumerate(o.get('deviations',[])):
        if old in dv: o['deviations'][i]=dv.replace(old,new); n+=1
assert n==3
for r in d['verifications'][-1]['results']:
    if r['claim']=='figs16-af647-stable':
        o2='(1.35 to 2.77%, the three with fit a; with fit b the peak of the recovery comes before the minimum ends the drop, so rise and drop do not compare directly)'
        assert o2 in r['response']
        r['response']=r['response'].replace(o2,'(1.35 to 2.77%, the three with fit a); the printed rise and drop give the same count, as with fit b the rise from the minimum (11.1 to 11.7%) is smaller than the drop (12.8 to 15.4%)')
open(P,'w').write(yaml.safe_dump(d,sort_keys=False,width=110,allow_unicode=True))
EOF
grep -n "—\|rather" attempts/xia-2021-01.yaml questions/xia-2021.yaml entries/xia-2021/README.md entries/xia-2021/reproduce_xia_2021.ipynb | head; date -u
```

```
Wed Nov 18 08:44:47 UTC 2026
```

**Agent**

Re-running the entry with all edits in place.

**Agent calls Bash**

```bash
python tools/entry.py all entries/xia-2021 2>&1 | tail -8
```

```
Installed kernelspec registry-xia-2021 in executed/xia-2021/.venv/share/jupyter/kernels/registry-xia-2021
0 error(s)
pass  reproduce_xia_2021.ipynb  (118 s)
```

**Agent**

Run passes. Now I'll confirm the record and questions validate, and that the numbers the text cites match the new run.

**Agent calls Bash**

```bash
ls tools; python tools/entry.py check entries/xia-2021 2>&1 | tail -3; python $TMPDIR/show.py 21 45 48 54 56 | grep -E "keeps|21-30 min|valley|passes its pre|as deposited|flipped|turned|total run"
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
[... 53 more lines not kept]
```

**Agent**

Run time is now 109 s, so I'll drop the exact figure from the README and check that `entry.py check` covers the attempt record.

**Agent calls Bash**

```bash
sed -i 's/It takes about two minutes (113 s in the last run), most of it streaming the files./It takes about two minutes, most of it streaming the files./' entries/xia-2021/README.md; grep -n "two minutes" entries/xia-2021/README.md; grep -n "attempts/\|proposed\|questions" tools/entry.py | head
```

```
35:- `reproduce_xia_2021.ipynb`: the analysis. It takes about two minutes, most of it streaming the files.
372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
sed -n 330,380p tools/entry.py; ls tests | head -30
```

```
for d in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else [])]
        # The rule is the protocol's from pilot-15. An attempt made under an earlier version is not held to it: its
        # agents had not been told (a chain under way when the rule reached main ended in a failed check, as
        # hazon-2022 did on 2026-11-12), and the site takes such a finding by its kind.
        version = re.fullmatch(r"pilot-(\d+)", str(((attempt.get("provenance") or {}).get("agent") or {}).get("protocol") or ""))
        told = not version or int(version[1]) >= 15
        for n, f in enumerate(attempt.get("findings") or [], 1):
            if told and f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
                                                                   "paper_inconsistency") else "data")
            if told and about == "data" and len(used) > 1 and not f.get("datasets"):
                report.error(where, f"finding {n}: the attempt used {len(used)} datasets; name the ones it is about "
                                    f"(`datasets:`, from {', '.join(used)})")
            for d in f.get("datasets") or []:
                if str(d) not in used:
                    report.error(where, f"finding {n}: {d} is not a dataset of this attempt ({', '.join(used)})")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
        agreed = {}
[... 48 more lines not kept]
```

**Agent**

The check covers the record, including the round-2 rule on outcomes. Final run after the README edit:

**Agent calls Bash**

```bash
python tools/entry.py all entries/xia-2021 2>&1 | tail -3; python -m pytest -q tests/test_encore.py 2>&1 | tail -3; python -c "import yaml;yaml.safe_load(open('questions/xia-2021.yaml'))" && echo questions ok; git status --short; date -u
```

```
Installed kernelspec registry-xia-2021 in executed/xia-2021/.venv/share/jupyter/kernels/registry-xia-2021
0 error(s)
pass  reproduce_xia_2021.ipynb  (118 s)
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python: No module named pytest
questions ok
 M attempts/xia-2021-01.yaml
 M entries/xia-2021/README.md
 M entries/xia-2021/reproduce_xia_2021.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? questions/xia-2021.yaml
?? scripts
[... 1 more lines not kept]
```

**Agent**

Round 2 is answered: all outcomes are unchanged, and I've proposed one change (figs12) for round 3. The entry re-ran cleanly with `python tools/entry.py all entries/xia-2021` (0 errors, notebook passes in 118 s), and the existing results are the same as before.

**Outcomes**
- **figs12-3v-propagation:** I agree with the verifier. The outcome stays `partially_reproduced`, as verified, with a `proposed` change to `blocked` (`data_missing`). The criterion's partial outcome needs the order in two of three mice, and only one mouse is deposited. The one-mouse results stay in the notes.
- **fig7-peak-timing:** I kept "reproduced" and recorded the verifier's disagreement (it would give partial at most). I did not propose a change. The criterion counts a pass under either reading, and reading (ii) passes in 30 of 36 variants. The criterion's own partial outcome is met under the same reading, so partial would not follow from it either. The verifier's real objection is that reading (ii) does not fit the paper's own times (rostral 8.80 s), so I added it as a reader question in the new `questions/xia-2021.yaml`. If a reader drops reading (ii), this claim would be not reproduced.

**Added to the notebook**
- **fig2d:** it now prints the valley height (5.19) and how much of each peak the passing reading keeps: 54% of the main peak and 30% or 23% of the second. The conclusion now says the share passes only by the letter of reading (b), and that the usual ways of splitting the two peaks give 65.8 to 69.1%.
- **fig7 and figs12:** the frame is now run turned every way. Flipped top to bottom or turned 180 degrees, the order holds in 0 of 18 variants. The frame being rostral up is now recorded as an assumption on all three Fig. 7/S12 claims, and the "decides nothing" wording is gone.
- **fig7-peak-timing:** prints the paper's own times under both readings.
- **figs16:** prints the highest AF647 value after its minimum. It passes the pre-stimulus mean in 3 of 6 readings and the mean + 3 SD in none. The verifier counted 4 of 6, but its own rise-against-drop comparison gives 3, so the record uses 3.

**Text corrected**
- Cell 22: the signal from 21 to 30 min is now 0.055 to 0.250, 1.3 to 5.9 times the pre-injection level.
- Cell 28: the first-rule densities are now 17.8 to 64.4.
- figs16 conclusion and notes: the false "without passing its pre-stimulus level" is replaced with the 3 of 6 count.
- fig6: now gives the main reading's 10 s bin test p of 0.0103, which is not below 0.01.
- The methods_unavailable finding now gives 17.1 to 40.1%, and asks whether rostral is at the top of the deposited frames.
- README: run time and table rows.
- Summary table: rows updated.
- Round 2 is recorded under `verifications` for all 29 claims.

**Not done**
- **LLOD reading (c):** still not run, because it needs the lines of Fig. 4B(ii) and the entry reads no figures. The verifier says this changes no outcome.
- **Orientation:** still not checked in the notebook, for the same reason. It is stated as an assumption, and the notebook shows what each other orientation gives.
- **Housekeeping:** nothing committed. The untracked dotfiles and `scripts/` in the repo root are not mine and I left them alone.

## End of run

36 turns, 12 minutes, $2.39 at API prices, result: success.
