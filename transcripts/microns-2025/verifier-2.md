# 000402 · verifier-2 · run 41011562653

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 632
drwxr-xr-x 6 runner runner    4096 Oct 30 06:14 .
drwxr-xr-x 7 runner runner    4096 Oct 30 06:14 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 06:14 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 06:14 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .github
-rw-r--r-- 1 runner runner       0 Oct 30 06:14 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 05:59 .mcp.json
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -c 4000 10.1038-s41586-025-08790-w.yaml; echo ----; head -c 3000 000402-microns-2025-01.yaml
```

```
# MICrONS Consortium (2025) from dandiset 000402

Tests the findings of [the MICrONS Consortium (2025)](https://doi.org/10.1038/s41586-025-08790-w)
that can be tested on [DANDI:000402](https://dandiarchive.org/dandiset/000402/0.230307.2132), which
holds the 19 two-photon scans of the MICrONS mouse: masks, fluorescence traces, stimulus tables and
video, treadmill and eye tracking. The paper describes 14 of these scans (its Extended Data Table 1).
Most of the paper's EM findings rest on CAVE tables that need an account token and are not tested.

| Claim | Outcome |
|---|---|
| 14 scans, P75 to P81 | Reproduced |
| Scan rates, fields and depths (11 / 2 / 1 scans) | Reproduced |
| 125,413 masks, 115,372 somatic | Reproduced |
| 75,909 unique neurons | Blocked: data missing |
| Half of the volume in VISp | Blocked: metadata insufficient |
| Z drift under 10 um | Blocked: data missing |
| Structural stack | Blocked: data missing |
| Stimulus composition of each scan | Reproduced |
| Stimuli conserved across scans | Partially reproduced |
| Oracle clips in the same order | Reproduced |
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,2000p 000402-microns-2025-01.yaml | tail -n +40
```

```
<persisted-output>
Output too large (44.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8072fc39-85d8-4192-8632-0c9f113193ee/tool-results/bjnihr9fs.txt

Preview (first 2KB):
  outcome: reproduced
  notebook: reproduce_microns_2025.ipynb
  output: claim:scans-14-p75-p81
  measured: 14
  notes: The 14 scans of Extended Data Table 1 are all in the dataset, recorded on 6 days (4 to 9 March
    2018), which are P75 to P80 against the birth date of 19 December 2017. The dataset holds 19 scans,
    the 19 completed scans of the Methods. Each scan's fields tile 1,200 x 1,100 um (1,200 x 1,000 um
    in scan 9-6) at depths of 80 to 570 um; the files give no common frame for the scans, so the extent
    of the whole volume is not measured.
  deviations:
  - Which 14 of the 19 files are the paper's scans was taken from Extended Data Table 1 (Methods, 2P functional
    imaging, "Of 19 completed scans over 6 days of imaging, 14 are described here (Extended Data Table
    1)"). The text the claims file was read from holds only the table's caption; its cells were read from
    the table's image in PMC11981939 (41586_2025_8790_Tab1_ESM.jpg). They are 4-7, 5-6, 5-7, 6-2, 6-4,
    6-6, 6-7, 7-3, 7-4, 7-5, 8-5, 9-3, 9-4 and 9-6.
- claim: scan-configurations
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8072fc39-85d8-4192-8632-0c9f113193ee/tool-results/bjnihr9fs.txt"
}
```

```
1	  outcome: reproduced
2	  notebook: reproduce_microns_2025.ipynb
3	  output: claim:scans-14-p75-p81
4	  measured: 14
5	  notes: The 14 scans of Extended Data Table 1 are all in the dataset, recorded on 6 days (4 to 9 March
6	    2018), which are P75 to P80 against the birth date of 19 December 2017. The dataset holds 19 scans,
7	    the 19 completed scans of the Methods. Each scan's fields tile 1,200 x 1,100 um (1,200 x 1,000 um
8	    in scan 9-6) at depths of 80 to 570 um; the files give no common frame for the scans, so the extent
9	    of the whole volume is not measured.
10	  deviations:
11	  - Which 14 of the 19 files are the paper's scans was taken from Extended Data Table 1 (Methods, 2P functional
12	    imaging, "Of 19 completed scans over 6 days of imaging, 14 are described here (Extended Data Table
13	    1)"). The text the claims file was read from holds only the table's caption; its cells were read from
14	    the table's image in PMC11981939 (41586_2025_8790_Tab1_ESM.jpg). They are 4-7, 5-6, 5-7, 6-2, 6-4,
15	    6-6, 6-7, 7-3, 7-4, 7-5, 8-5, 9-3, 9-4 and 9-6.
16	- claim: scan-configurations
17	  outcome: reproduced
18	  notebook: reproduce_microns_2025.ipynb
19	  output: claim:scan-configurations
20	  measured:
[... 691 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_microns_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n=== CELL {i} [{c['cell_type']}] ===")
    src=''.join(c['source'])
    print(src if c['cell_type']=='markdown' else src[:1500])
    for o in c.get('outputs',[]):
        if 'text' in o: t=''.join(o['text'])
        elif 'data' in o: t=''.join(o['data'].get('text/plain','<image>')) if 'text/plain' in o['data'] else '<non-text>'
        else: t=str(o.get('ename'))+str(o.get('evalue'))
        print('--OUT--'); print(t[:6000])
EOF
```

```
<persisted-output>
Output too large (100.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8072fc39-85d8-4192-8632-0c9f113193ee/tool-results/bpe4eaj28.txt

Preview (first 2KB):
=== CELL 0 [markdown] ===
# Reproducing the MICrONS Consortium (2025) from dandiset 000402

**Paper.** The MICrONS Consortium (2025). Functional connectomics spanning multiple areas of mouse
visual cortex. *Nature* 640, 435-447.
[doi:10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w). The claims file was
written from the open access version of record (PMC11981939): main text, figure legends, Methods
and the captions of the Extended Data. The claims file is
`claims/000402/10.1038-s41586-025-08790-w.yaml`.

**Dandiset.** [DANDI:000402](https://dandiarchive.org/dandiset/000402/0.230307.2132), "MICrONS Two
Photon Functional Imaging", version 0.230307.2132
([doi:10.48324/dandi.000402/0.230307.2132](https://doi.org/10.48324/dandi.000402/0.230307.2132)).
This is the version the paper cites (reference 73, "version 0.230307.2132") and the only published
version. The draft lists the same 19 assets and size; it is not used.

[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8072fc39-85d8-4192-8632-0c9f113193ee/tool-results/bpe4eaj28.txt",
 "limit": 700
}
```

```
1	
2	=== CELL 0 [markdown] ===
3	# Reproducing the MICrONS Consortium (2025) from dandiset 000402
4	
5	**Paper.** The MICrONS Consortium (2025). Functional connectomics spanning multiple areas of mouse
6	visual cortex. *Nature* 640, 435-447.
7	[doi:10.1038/s41586-025-08790-w](https://doi.org/10.1038/s41586-025-08790-w). The claims file was
8	written from the open access version of record (PMC11981939): main text, figure legends, Methods
9	and the captions of the Extended Data. The claims file is
10	`claims/000402/10.1038-s41586-025-08790-w.yaml`.
11	
12	**Dandiset.** [DANDI:000402](https://dandiarchive.org/dandiset/000402/0.230307.2132), "MICrONS Two
13	Photon Functional Imaging", version 0.230307.2132
14	([doi:10.48324/dandi.000402/0.230307.2132](https://doi.org/10.48324/dandi.000402/0.230307.2132)).
15	This is the version the paper cites (reference 73, "version 0.230307.2132") and the only published
16	version. The draft lists the same 19 assets and size; it is not used.
17	
18	**What the dandiset holds.** 19 NWB files, one per two-photon scan of mouse 17797, each with the
19	raw imaging of every field, the segmentation masks (soma or artifact) and their fluorescence
20	traces, the stimulus video and three stimulus tables (Clip, Monet2, Trippy), treadmill velocity,
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8072fc39-85d8-4192-8632-0c9f113193ee/tool-results/bpe4eaj28.txt",
 "offset": 700,
 "limit": 900
}
```

```
700	 4-7      True          76.1              1.0   20.01     0.8476                           0.14                        967.9           0.45      0.849                     True
701	 4-9     False          72.0              1.0   19.99     0.9990                           1.77                          3.9           0.67      0.981                     True
702	4-10     False          82.9              1.0   20.01     0.4861                           0.16                       3263.8           0.45      0.714                     True
703	 5-3     False          66.9              1.0   20.01     0.2784                           0.14                       4582.3           0.32      0.916                     True
704	 5-6      True          63.7              1.0   19.98     1.0000                           0.12                         -0.3           0.55      0.996                     True
705	 5-7      True          65.5              1.0   19.97     1.0000                           0.11                         -0.3           0.57      0.977                     True
706	 6-2      True          57.0              1.0   20.01     1.0000                           0.12                         -0.3           0.72      0.998                     True
707	 6-4      True          58.9              1.0   20.00     1.0000                           0.12                         -0.2           0.63      0.993                     True
708	 6-6      True         100.1              1.0   20.01     1.0000                           0.08                         -0.2           0.50      0.986                     True
709	 6-7      True          99.9              1.0   20.01     1.0000                           0.14                         -0.3           0.50      0.973                     True
710	 7-3      True         100.0              1.0   20.01     1.0000                           0.06                         -0.2           0.20      0.978                     True
711	 7-4      True  
[... 766 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open('10.1038-s41586-025-08790-w.yaml'))
print(c.keys() if isinstance(c,dict) else type(c))
cl=c['claims']
from collections import Counter
print(len(cl), Counter(x.get('data') for x in cl))
for x in cl: print(x['id'], x.get('data'), list(x.keys()))
a=yaml.safe_load(open('000402-microns-2025-01.yaml'))
o=a['outcomes']; print(len(o), Counter(x['outcome'] for x in o), Counter(x.get('blocked_by') for x in o))
ids={x['id'] for x in cl}; oid=[x['claim'] for x in o]; print(set(oid)^ids, len(set(oid)))
v=a['verifications'][0]['results']; print(len(v), {x['claim'] for x in v}^ids)
for x in o:
  for k in x:
    if 'assum' in k: print(x['claim'],k,x[k])
import re
txt=open('000402-microns-2025-01.yaml').read(); print('assumed' in txt)
EOF
```

```
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
36 Counter({'elsewhere': 17, None: 16, 'with_inputs': 3})
scans-14-p75-p81 None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
scan-configurations None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
masks-125413-somatic-115372 None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
unique-neurons-75909 None ['id', 'statement', 'source', 'quote', 'expected', 'depends_on', 'criterion']
area-split-half-visp None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
z-drift-under-10um None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
structural-stack None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
stimulus-composition None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
stimulus-conserved-across-scans None ['id', 'statement', 'source', 'quote', 'depends_on', 'criterion']
oracle-same-order None ['id', 'statement', 'source', 'quote', 'depends_on', 'criterion']
spontaneous-periods None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
monet2-directions None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
fig3f-oracle-reliability None ['id', 'statement', 'source', 'quote', 'depends_on', 'criterion']
fig3g-direction-tuning None ['id', 'statement', 'source', 'quote', 'depends_on', 'criterion']
behaviour-recorded None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
photodiode-89pct None ['id', 'statement', 'source', 'quote', 'expected', 'criterion']
manual-coreg-19181 with_inputs ['id', 'statement', 'source', 'quote', 'data', 'expected', 'criterion']
ed4-matched-higher-signal-correlation with_inputs ['id', 'statement', 'source', 'quote', 'data', 'depends_on', 'criterion']
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open('10.1038-s41586-025-08790-w.yaml'))
for x in c['claims']:
  if x['id'] in ('monet2-directions','spontaneous-periods','nuclei-144120','cell-classification','em-sections','synapse-detection','unique-neurons-75909','area-split-half-visp','structural-stack','manual-coreg-19181','ed4-matched-higher-signal-correlation','fig6k-target-responses','fig7d-l3-two-hop','scans-14-p75-p81','behaviour-recorded'):
    print('#####',x['id']); print(yaml.dump({k:v for k,v in x.items() if k not in('quote',)},width=150,allow_unicode=True))
print(yaml.dump(c['checks'],width=150)[:3000])
EOF
```

```
##### scans-14-p75-p81
criterion: Count the distinct scans (session and scan index) and the distinct days on which they were recorded. The scan count is exact, as it is a count
  of files the paper lists. The ages are judged from the recording dates against the birth date of 19 December 2017 (Methods, Timeline); P75 to P81 (main
  text) and P75 to P80 (Methods timeline) are both readings the paper allows, and the claim holds when the dates fall within P75 to P81. The 6 days are
  the days of imaging of the 19 completed scans (Methods, 2P functional imaging); the 14 kept scans may span fewer, so a count of 6 or fewer days is consistent
  with the paper.
expected:
- quantity: number of scans
  tolerance: 0
  unit: scans
  value: 14
id: scans-14-p75-p81
source: Results, 2P calcium imaging, paragraph 1; Methods, 2P functional imaging
statement: The calcium imaging data comprise 14 scans of one mouse, collected between P75 and P81, spanning a volume of about 1,200 x 1,100 x 500 um.

##### unique-neurons-75909
criterion: The method is from the Methods (2P structural stack). Each scan field is registered into the structural stack and each somatic mask gets a 3D
  centroid; the closest 2 cells from different scans are grouped, iteratively, until all pairs are at least 10 um apart or a further join produces a mask
  taller than 20 um in z. The paper does not say how the height of a group is measured. The readings are (a) the range in z of the centroids in the group;
  (b) that range plus the z extent of one field's mask. It also does not say whether distances to a group are taken from its mean centroid or from its nearest
[... 299 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "monitor (on|off)|spontaneous|unique to each scan|Trippy.*seed|seeds" paper/*.txt | head -20; grep -n -i -E "7,931|27,904|subvolume 35" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  tr '\n' ' ' < paper/*.txt | grep -o -i -E ".{250}(spontaneous activity|unique to each scan|were unique|differed between scans|7,931).{250}" | head -8
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 2: doi:10.1038/s41586-025-08790-w on DANDI:000402 (0.230307.2132)**

The claims file has 36 claims: 16 on the dataset, 3 `with_inputs` and 17 `elsewhere`. The attempt record gives an outcome for each of the 36:

- 10 reproduced and 3 partially reproduced;
- 23 blocked: 16 by `other`, 4 by `data_missing`, 2 by `too_large` and 1 by `metadata_insufficient`.

It also holds a round-1 verification result for each of the 36.

### 1. Outcomes

No outcome in the attempt record is marked `assumed: true`; the word does not occur in the file. Two outcomes rest on choices that are stated as deviations, and both are reasonable:
- The 14-scan list was read from the image of Extended Data Table 1. The exact mask totals in cell 14 support it.
- The Monet2 directions were measured from the stimulus video.

**I agree with these outcomes:**
- **Reproduced:** scans-14-p75-p81, scan-configurations, masks-125413-somatic-115372, stimulus-composition, oracle-same-order, nuclei-144120 and cell-classification.
- **Reproduced, though the criterion tests little; the record says so:** fig3f-oracle-reliability and fig3g-direction-tuning.
- **Partially reproduced:** stimulus-conserved-across-scans, spontaneous-periods and behaviour-recorded.
- **Blocked:**
  - unique-neurons-75909, z-drift-under-10um, structural-stack and photodiode-89pct, all `data_missing`;
  - area-split-half-visp, `metadata_insufficient`; I said `data_missing` in round 1, and either fits;
  - the 3 `with_inputs` claims and the 13 `other` claims among the `elsewhere` ones.

**monet2-directions, reproduced:** I now agree. Cell 33 measures the directions by optical flow:
- All 560 trials have 16 distinct directions under both measures, the largest deviation from the grid is 7.9°, and both showings of each seed give the same directions in 280 of 280 pairs. That agreement checks the method independently.
- The method was changed after the first one failed. This is disclosed, and it is justified by the bias of the phase correlation towards whole-pixel shifts.

**I do not fully agree with these two:**
- **synapse-detection, blocked `too_large`.** The record says a count of the same 20 GB file took 10 minutes in an earlier run, and that the entry's run stalled. That is a failed run, not a file too large to process. The count for subvolume 65 should be retried, or the reason recorded as `other`. The subvolume 35 count and the precision and recall would stay untested either way.
- **em-sections, blocked `too_large`.** The record's metadata bounds (7,904; 14,816; 27,903) already decide the second expected quantity, the share of sections in subvolume 35: (14,816 − 7,904) / 20,000 = 34.6%, against 35 ± 3.5. Only the exact section count needs whole sections. The patch read that put the first section at 7,931 was run outside the notebook and has no printed output.

### 2. Statements against the printed outputs

Almost every sentence in the "Result:" conclusions, the Summary, the README and the record's notes matches the outputs. The exceptions:

**Cell 35 and the monet2 notes: "for the two seeds it flagged".**
- The phase correlation flagged 4 trials by the 10° rule and 6 on the grid (cell 33). Only one trial each of seeds 7637 and 6154 is printed.
- In round 1, seed 6154 was not among the grid failures. So at least two of the 6 grid-flagged trials belong to seeds that are not printed.
- The outcome does not depend on this, since the optical flow gives 16 directions in all 560 trials.

**Cell 43 and the fig3f notes: "The score on fluorescence carries a shared, stimulus-locked signal … does not separate neural reliability from that shared signal".**
- Cell 41 shows that removing each mask's fit on its field's mean trace barely changes the scores: somatic 0.200, 0.380 and 0.665 against 0.208, 0.396 and 0.702.
- That is evidence against a field-wide shared signal driving the scores. The high artifact-mask scores (0.235, 0.402 and 0.650) stay unexplained; a local neuropil signal or real neurites could account for them.
- "Cannot separate" is fair. "Carries a shared signal" is not shown for the unit scores.

**Cell 47 and the fig3g notes: the 80 units shown respond more at their preferred direction "in 91.2% of cases (median … 2.87)".**
- The 80 units are chosen by a preference index computed over all 40 trials, which include the second-half trials used to test them (cell 46). So 91.2% and 2.87 are inflated by selection.
- The unbiased number is 0.629 over all somatic masks. The fig3f caveat about shared stimulus-locked signals also applies to it and is not discussed.

**Cell 30 and the behaviour notes: "Of the 5 files outside the paper's 14, the eye tracking also stops early in 4-10, 5-3 and 8-7".**
- By the notebook's own 1 s rule (cell 29), 4-9 (3.9 s early, starting 1.77 s late) and 8-9 (6.2 s early) also fail. So all 5 fail.
- These files are not among the 14, so no conclusion changes.

**Summary (cell 61), wording:**
- "13 other … the CAVE tables that choose their neurons need an account token" does not fit fiducial-automatch, vessel-automatch, hybrid-automatch, fiducial-transform-residual or fig7d. For those, the CAVE tables are the data themselves, or no table is named.
- The `with_inputs` row says "variants on the dataset's own EM identifiers above" for fig6k-target-responses too, but no variant was run for it.

**Statements without printed output.** Several notes rest on nothing printed in the notebook:
- the em-sections bounds and patch read;
- the earlier 10-minute synapse count;
- the BossDB stack path and the export sizes (about 20 GB each).

**README.** Each row agrees with the record. I could not check the "about 12 minutes" run time; the printed cell times add up to about 8 minutes, and some cells print none.

**My round-1 reasons in the record.** They are in my own words and faithful, with two gaps:
- **em-sections:** the record keeps my round-1 "Blocked (other)" and answers "No change of outcome", but the outcome is now `too_large`. The response should say the outcome changed.
- **Problem 7:** per-unit delay and shared time stamps. It appears in no reason. It does not affect a conclusion, and the record's deviations now state it.

### 3. Round-1 points

**Resolved:**
- 1, spontaneous-periods: the bounds are now compared and the outcome is partially reproduced.
- 2, behaviour-recorded: the series in file 4-7 are listed.
- 3, stimulus-conserved-across-scans: the repeated Trippy seed is recorded.
- 4, monet2-directions: the outcome is now settled by the optical flow.
- 6, fig3g: the count is given a reference.
- 9, ed4: the variant is run on reading (b) only and decides nothing.
- 10, cell-classification: the 82,247 sum is stated.
- 11, oracle-same-order: the check now counts trials inside a repeat.
- 12, scan-configurations: the fields-by-depth table shows exactly two per depth in all 19 files.
- 13, cell 0: the group listing is printed and the unsourced statement is removed.
- C, NWB group listing, scan 4-7 eye series and fields per depth: all now printed.

**Addressed, with a new over-reach:** 5, fig3f artifact masks. The artifact-only distribution and the field-mean regression are now computed, but the interpretation goes beyond the numbers (section 2).

**Disclosed and unchanged:** 7. It does not affect an outcome.

**Partly addressed:** 8, BossDB. The notes now list the public exports and why they do not suffice.

**Still open, bearing on a conclusion:**
1. synapse-detection: `too_large` is not supported, since the same count ran in 10 minutes before. The count for subvolume 65 should be retried, or the reason changed.
2. em-sections: the subvolume 35 share can be tested from metadata, so the claim is at least partly testable. The patch read should be put in the notebook or removed from the notes.
3. fig3g: the 91.2% figure is inflated by selection. The conclusion should rest on the 62.9%, and the shared-signal caveat should be stated.
4. fig3f: the sentence on the shared signal should match the regression result.

**Still unverifiable by me:**
- The cells of Extended Data Table 1. They are now cited but cannot be printed from the data.
- The phase-correlation results for the unprinted grid-flagged trials. They are moot for the outcome.

## End of run

12 turns, 3 minutes, result: success.
