# 001038 · recorder · run 39127106782

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001038 --write; git diff; ls claims/001038 transcripts/001038; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
diff --git a/README.md b/README.md
index 8414da7..6056d4d 100644
--- a/README.md
+++ b/README.md
@@ -90,6 +90,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
 | [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
 | [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
+| [001038](https://dandiarchive.org/dandiset/001038) | [Azcorra et al. 2023](https://doi.org/10.1038/s41593-023-01401-9) | 16 | 7 | 1 | 0 | [`001038-azcorra-2023`](entries/001038-azcorra-2023) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001038:
10.1038-s41593-023-01401-9.yaml

transcripts/001038:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 2764,3231p docs/pilot-notes.md; sed -n 60,90p README.md
```

```
<persisted-output>
Output too large (38.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/59a637cb-c5f2-42bf-a31e-8bcb87ed4dbd/tool-results/be1b9ziz6.txt

Preview (first 2KB):
### 000718, Zaki et al. 2024

Two claims reproduced, two not reproduced and twenty-one blocked on the
dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
own outcome for each claim from the notebook with its conclusions removed and
agreed with 25 of the 26; it gave not reproduced for
`offline-bursts-above-shuffle`, as the criterion is written, and suggested
blocking it as `methods_underspecified`, which the record already did, as
round 1 had not seen the record. Round 1 agreed that
`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
the criterion, but argued that the Methods' scoring has no quiet-wake class;
applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
bursts in wake, and under that reading the overlap ensemble co-bursts less
with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
p = 0.13), so the author changed the claim to not reproduced and recorded the
departure from the criterion as a deviation. Round 2 agreed with all 26 and
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/59a637cb-c5f2-42bf-a31e-8bcb87ed4dbd/tool-results/be1b9ziz6.txt"
}
```

```
1	### 000718, Zaki et al. 2024
2	
3	Two claims reproduced, two not reproduced and twenty-one blocked on the
4	dandiset. With outside data, counted apart: one reproduced. Round 1 gave its
5	own outcome for each claim from the notebook with its conclusions removed and
6	agreed with 25 of the 26; it gave not reproduced for
7	`offline-bursts-above-shuffle`, as the criterion is written, and suggested
8	blocking it as `methods_underspecified`, which the record already did, as
9	round 1 had not seen the record. Round 1 agreed that
10	`fig5c-wake-overlap-neutral-coburst` was partially reproduced by the letter of
11	the criterion, but argued that the Methods' scoring has no quiet-wake class;
12	applied to Ca_EEG2-1's EMG it puts 94.1% of quiet-wake frames and all 87
13	bursts in wake, and under that reading the overlap ensemble co-bursts less
14	with the neutral than with the aversive ensemble (26.4 against 35.6%, McNemar
15	p = 0.13), so the author changed the claim to not reproduced and recorded the
16	departure from the criterion as a deviation. Round 2 agreed with all 26 and
17	nothing was proposed, so there was no third round. The paper reports that a
18	strong aversive experience links fear to a neutral context experienced two
19	days before, that neutral and aversive ensembles in CA1 co-reactivate in
20	offline population bursts, mostly during wake, and that this co-bursting of
[... 480 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 50,60p README.md; cat attempts/001038-azcorra-2023-01.yaml; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
    if '001038' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
E
```

```
<persisted-output>
Output too large (46.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/59a637cb-c5f2-42bf-a31e-8bcb87ed4dbd/tool-results/b7ipleo9p.txt

Preview (first 2KB):
|---|---|---|---|---|---|---|
| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
| [000207](https://dandiarchive.org/dandiset/000207) | [Zheng et al. 2022](https://doi.org/10.1038/s41593-022-01020-w) | 5 | 1 | 0 | 14 | [`000207-zheng-2022`](entries/000207-zheng-2022) |
| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
| [000625](https://dandiarchive.org/dandiset/000625) | [Geiller et al. 2020](https://doi.org/10.1016/j.neuron.2020.09.013) | 4 | 4 | 6 | 12 | [`000625-geiller-2020`](entries/000625-geiller-2020) |
| [000035](https://dandiarchive.org/dandiset/000035) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 3 (+2) | 1 (+1) | 0 | 9 (+1) | [`000035-scala-2021`](entries/000035-scala-2021) |
| [001453](https://dandiarchive.org/dandiset/001453) | [Fouke et al. 2025](https://doi.org/10.1016/j.cub.2025.04.027) | 7 | 1 | 2 | 10 | [`001453-fouke-2025`](entries/001453-fouke-2025) |
| [000006](https://dandiarchive.org/dandiset/000006) | [Economo et al. 2018](https://doi.org/10.1038/s41586-018-0642-9) | 3 | 1 | 1 | 4 | [`000006-economo-2018`](entries/000006-economo-20
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001038-azcorra-2023-01.yaml | head -c 20000
```

```
schema_version: 1
id: 001038-azcorra-2023-01
dandiset: "001038"
dandiset_version: 0.241111.1719
paper: doi:10.1038/s41593-023-01401-9
date: 2026-10-18
entry: 001038-azcorra-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
- what: snRNA-seq count matrices of the two samples (barcodes, features and matrix files of
    GSM6926026 and GSM6926027), used only by the claims with data elsewhere.
  source: GEO GSE222558, https://ftp.ncbi.nlm.nih.gov/geo/samples/GSM6926nnn/ (files dated
    2023-01-09)
[... 385 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('001038' == str(v) for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
grep -n "Reproduced\|Partially\|^| Dandiset" README.md | head
```

```
{
 "dandiset": "001038",
 "name": "Unique functional responses differentially map onto genetic subtypes of dopamine neurons",
 "published_version": "0.241111.1719",
 "asset_count": 1238,
 "size_gb": 22.75,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [],
 "papers": [
  {
   "doi": "10.1038/s41593-023-01401-9",
   "title": "Unique functional responses differentially map onto genetic subtypes of dopamine neurons",
   "relation": "IsDescribedBy",
   "resource_type": "JournalArticle",
   "preprint": false
[... 8 more lines not kept]
```

**Agent**

The README row is written (16 reproduced, 7 partially, 1 not reproduced, 0 blocked). Next I'm reading the rest of the attempt record, the claims file and the reports.

**Agent calls Bash**

```bash
tail -c +20000 attempts/001038-azcorra-2023-01.yaml; grep -n "^- id:\|data:\|source\|uses\|dandiset" claims/001038/*.yaml | head -80
```

```
Results give reward P = 2e-5 for Calb1 and 0.001 for Vglut2; the Figure 4g legend
    gives them the other way round. The Figure 2f legend gives 10 Anxa1 mice, the Methods 9.
    Extended Data Figure 9k gives striatal PCs explaining 52.4% and 25.2% of SNc variance, the
    Methods 53.2% and 24.3%.
verifications:
- date: '2026-10-18'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper (PMC10545540). The verifier queried the archive's
    asset list and tested the helper functions on synthetic inputs. Its report had no attempt record
    and gave its own outcome for each claim; all 29 outcomes agree with the record, and for the three
    blocked claims it gave other reasons.
  results:
  - claim: recording-counts-locomotion
    agrees: true
    outcome: not_reproduced
    reason: 0 of 5 within tolerance, 50/28/82/89/85 against 42/22/47/74/75; Anxa1 is 74% over. The four
      Methods criteria do not account for the difference and the excess is unevenly spread (Calb1 in
      the overlap region 17 against 5, the k-means Anxa1 set 35 against 16). The stimulus counts match
[... 490 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "paper_inconsistency" -A4 attempts/001038-azcorra-2023-01.yaml | head; grep -n "^findings\|^verifications\|^summary\|^[a-z_]*:" attempts/001038-azcorra-2023-01.yaml; sed -n 1,37p claims/001038/*.yaml
```

```
404:- kind: paper_inconsistency
405-  statement: The Results give reward P = 2e-5 for Calb1 and 0.001 for Vglut2; the Figure 4g legend
406-    gives them the other way round. The Figure 2f legend gives 10 Anxa1 mice, the Methods 9.
407-    Extended Data Figure 9k gives striatal PCs explaining 52.4% and 25.2% of SNc variance, the
408-    Methods 53.2% and 24.3%.
--
653:    the asset-summary fields and the paper_inconsistency items appear in no output; cell 13 now prints the
654-    value counts of normalized_fluorescence and the related resources and asset summary of the published
655-    and draft versions, cells 46 and 73 print the paper's conflicting P-values and percentages (checked
656-    against the paper's text, saved under paper/), and the Figure 2f legend and Methods mouse counts were
1:schema_version: 1
2:id: 001038-azcorra-2023-01
3:dandiset: "001038"
4:dandiset_version: 0.241111.1719
5:paper: doi:10.1038/s41593-023-01401-9
6:date: 2026-10-18
7:entry: 001038-azcorra-2023
8:provenance:
16:inputs:
21:outcomes:
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001038; wc -w *-report.md; cat author-report.md
```

```
969 author-report.md
  630 author-revise-1-report.md
  605 author-revise-2-report.md
 1901 verifier-1-report.md
 1053 verifier-2-report.md
 5158 total
I did steps 1 to 6 for dandiset 001038 and ran the handover. The entry passes `check` and runs in 182 s from a clean environment, and the executed numbers match the conclusions. I used the paper's full text (open access, PMC10545540), saved under `paper/`. I pinned version 0.241111.1719: it is the only published version, the paper cites none, and the draft has the same files and differs only in metadata.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| recording-counts-locomotion | not reproduced (50/28/82/89/85 vs 42/22/47/74/75) |
| recording-counts-stimuli | reproduced (all 8 counts exact) |
| fig2f-xcorr-direction | reproduced |
| fig2i-trough-lag | partially reproduced (Calb1 0.140 s; the code's timing gives 0.160 s) |
| fig2jk-pca-variance | reproduced (58.32 / 22.09%, both just inside tolerance) |
| fig2l-pc-angles | reproduced |
| fig2g-event-counts | reproduced |
| ed7f-prob-transient-after-event | reproduced |
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001038; cat author-revise-1-report.md author-revise-2-report.md; head -c 6000 verifier-2-report.md
```

```
No outcome changed in round 1. The verifier's 29 outcomes all agree with the record; the only disagreements are the reasons given for the three blocked claims. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, 107 s), and every number in the updated conclusions and notes matches the new executed notebook. Round 1 is recorded under `verifications` in `attempts/001038-azcorra-2023-01.yaml`, one result per claim, with the verifier's reasons in its own words and a response to each.

**What I corrected**
- **fig5ab-transient-scaling:** the main result now uses only the recomputed onsets that also appear in the file's stored onsets. The stored ones already exclude the 5 s after every reward, as the paper's code does, so this is a closer match to the code. The new ratios are 241, 246 and 232%, against 239, 266 and 222% before; the old onsets are kept as a variant. Vglut2 and Anxa1 are now outside tolerance, so the outcome stays partially reproduced, and the measured values, notes and deviation are updated. The ratio over recordings with both quintiles, which the verifier asked about, is the same.
- **Blocked claims:** the header and summary now name the blocked reasons by their category names (`not_runnable`, `other`).

**Output added at the verifier's request**
- **Locomotion overcount:** counts after each step split by location, by single or dual fiber, and by sessions with or without stimuli, plus recordings per mouse and two variant counts. The extra recordings are spread across every split, and no variant gives the paper's counts. The paper's preprocessing code also excludes and crops some recordings by hand, which can't be repeated, so the cause is still not found.
- **ed9k denominator:** the 160 striatal components capture 100.00% of the SNc data's total variance, so the percentages are not inflated.
- **RewardNoRest:** each rest row is its reward row shifted 0.01 s with the same duration. The 2647 onsets left equal rewards minus rest reward
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "statement:" -A3 claims/001038/*.yaml | head -120
```

```
39:  statement: The striatal recordings that pass the locomotion criteria number 42 from 12
40-    Vglut2 mice, 22 from 6 Calb1 mice, 47 from 10 Anxa1 mice, 74 from 14 DAT mice and 75 from
41-    14 Aldh1a1 mice.
42-  source: Figure 2f legend; Extended Data Figure 6c legend; Methods, Analysis of signaling
--
65:  statement: The striatal recordings in the reward analysis number 28 (Vglut2), 17 (Calb1), 51
66-    (Anxa1) and 63 (DAT), and in the air puff analysis 29, 17, 57 and 69.
67-  source: Figure 4d and 4f legends; Methods, Criteria for recording inclusion
68-  expected:
--
97:  statement: Cross-correlations between dF/F and acceleration show a trough at positive lags
98-    for Calb1 and Vglut2 axons (transients after decelerations) and a peak at positive lags
99-    for Anxa1 axons (transients after accelerations).
100-  source: Figure 2d,f; Results, Genetic subtypes show different signaling patterns during
--
111:  statement: Calb1 transients follow decelerations with a shorter lag than Vglut2 transients;
112-    the trough of the cross-correlation is at 0.42 s for Vglut2 and 0.17 s for Calb1 on
113-    average (P = 1e-6).
114-  source: Figure 2i
--
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 485,540p claims/001038/*.yaml
```

```
- id: snrna-nuclei-qc
  statement: Single-nucleus RNA-seq of dopamine neurons from five DAT-Cre, Sun1-GFP mice
    yields 12,065 nuclei after quality control, with a mean of 3,435 UMIs and 1,683 genes per
    nucleus.
  source: Methods, Analysis of snRNA-seq data; Figure 1a,b
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  expected:
  - quantity: Nuclei after quality control
    value: 12065
    tolerance: 1206.5
  - quantity: Mean UMI count per nucleus
    value: 3435
    tolerance: 343.5
  - quantity: Mean number of detected genes per nucleus
    value: 1683
    tolerance: 168.3
  criterion: Nuclei with 500 or more detected genes, as the Methods filter, from the two
    samples' count matrices. Reproduced when the three values are within tolerance, partially
    reproduced when the count is and a mean is not.
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001038, Azcorra et al. 2023

Sixteen claims reproduced, seven partially and one not reproduced on the
dandiset, none blocked. Five claims on data in other archives: two
reproduced, on the snRNA-seq count matrices in GEO (GSE222558), and three
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 29, giving other reasons only for
the three blocked claims; the author kept `not_runnable` for the two claims
that need Seurat and LIGER in R and `other` for the histology claim, which
rests on manual cell counts that are not deposited, as the images are public
on Zenodo. After round 1, `fig5ab-transient-scaling` uses the recomputed onsets
that are also stored, which carry the code's exclusion after every reward
(241, 246 and 232% against 239, 266 and 222% before), and stays partially
reproduced. Round 2 agreed with all 29 and nothing was proposed, so there was
no third round. The paper reports that genetic subtypes of dopamine neurons
signal differently: Vglut2 and Calb1 axons in striatum show transients after
decelerations and respond to rewards and air puffs, Anxa1 axons show
transients after accelerations, have almost no reward response and decrease
to air puffs, the subtypes can be clustered from these responses, and somas in
SNc track their axons. The recording counts, the cross-correlations with
acceleration and their lags, PCA and angles, triggered averages and transient
scaling, the reward and air puff responses, the k-means clustering, the soma
and axon correlations, the SNc responses, Aldh1a1 heterogeneity, the overlap
region and two snRNA-seq claims were tested; the snRNA-seq clustering and the
integration of four published datasets are blocked as `not_runnable`.
`recording-counts-locomotion` is not reproduced: the Methods' criteria select
50, 28, 82, 89 and 85 striatal recordings for Vglut2, Calb1, Anxa1, DAT and
Aldh1a1, against 42, 22, 47, 74 and 75, and no variant gives the paper's
counts. Some outcomes rest on weak ground: the 18 claims that use the
locomotion selection are tested on this larger set; `fig2jk-pca-variance` is
inside tolerance by 0.5 and 0.02 points; in `fig2l-pc-angles` the Anxa1 mean
depends on where the circle is cut (circular mean 301.3 against 233.3
degrees); `fig4g-reward-response` is partially reproduced with the Methods'
windows, while the code's windows give the paper's 7.90, 12.40 and 5.88; the
cause of the Vglut2 peak timing in `ed6f-dec-peak-timing` and of the DAT air
puff mean (2.69 against 5.3) is not found; and the deep band of
`ed1h-aldh1a1-depth` holds 5 recordings. The author used the open access full
text (PMC10545540) and took what the Methods leave open from the paper's code
at commit fad12b2.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
The files carry the signal-to-noise ratio and 405 nm cross-correlation but not
the other exclusion flags (running time, 405 nm artifacts) or which recordings
each figure uses; recomputed with the paper's code, the stimulus analyses give
the paper's counts exactly, but the locomotion criteria select more striatal
recordings than Figure 2 reports (Anxa1 82 against 47, Vglut2 50 against 42).
The Events table lists consumed rewards only, and rewards the mouse did not
lick for are only in the raw 4 kHz Reward trace, so 911 acceleration and 767
deceleration onsets recomputed from the processed data are not in the stored
WheelEvents. The `coordinates` column of the fiber table is described as (AP,
ML, DV) but holds (ML, AP, DV), and 785 of 790 SNc fibers and 1281 of 2137
fibers overall have no coordinates. The column
`cross_correlation_with_acceleration` holds the peak cross-correlation of the
405 nm control with acceleration, not of dF/F, and is missing where running
was under 100 s. The dF/F series are normalized so that the largest transient
is 1, which the files do not state, and the normalization factor in
`normalized_fluorescence` holds two values per row in 123 files. Other
findings: three subject ids ending in L are left-hemisphere recordings of mice
that also have ids without it, so the archive's 105 subjects are 102 mice, and
the age is a range (P8W/P16W) in every file; the published version's link to
the paper is malformed (fixed in the draft) and its asset summary lists only
"analytical technique" and "ProcessingModule"; the code integrates responses
over windows that differ from the Methods', and the paper's reward means equal
those of the code's windows to the decimal, as do its Vglut2, Calb1 and Anxa1
air puff means within tolerance, while its DAT air puff mean (5.3) does not
(2.46); the code reports trough and peak times 0.02 and 0.01 s later than the
Methods define, prints uncorrected p-values for Figures 2i and 7f, whose
legends state Bonferroni correction, and marks 405 nm artifacts from the last
noisy section to the end of a recording and from the start to the first; and
the paper swaps the Calb1 and Vglut2 reward P-values between the Results and
the Figure 4g legend, gives 10 Anxa1 mice in the Figure 2f legend and 9 in the
Methods, and gives different SNc variance values in Extended Data Figure 9k
and the Methods. No recording is deposited twice.

The notebook ran in 182 s in the first clean run, `tools/entry.py all` took
107 s after round 1 and 2.3 minutes after round 2. The first metadata scan
took 30 minutes, as h5py serializes calls across threads and every download
URL needed its own API request, and was sped up with a process pool, the bulk
asset listing and BLAS limited to one thread; early runs crashed on the files
with two `normalized_fluorescence` values per row; and the paper's 4.4 GB
MATLAB table on Zenodo, which carries the exclusion flags, was not practical
to parse. Round 2 found statements the outputs did not support, among them
that the Calb1 trough lag with the code's timing equals the paper's, that the
response means match to the decimal, which fails for the DAT air puff mean,
and that the overlap recordings come from the same mice, as well as findings
with no output behind them, and these were corrected. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: Methods and code that disagree where the code gives
the paper's numbers; a count claim that fails while other claims use its
selection; whether analysis parameters taken from the paper's code count as
inputs; `not_runnable` for software in R and no category for manual cell
counting; a 10% tolerance for a value near zero and for angles; a MATLAB
k-means seed that cannot be repeated; and selection counts and one session's
values seen before the criteria were written.
EOF
grep -c "—\|rather" <(tail -95 docs/pilot-notes.md)
```

```
0
```

**Agent calls Bash**

```bash
git status --short
```

```
M README.md
 M docs/pilot-notes.md
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
?? scripts
```

**Agent**

I ran `tools/readme_row.py 001038 --write`, which added the 001038 row to README.md (16, 7, 1, 0), and added the subsection below to the end of docs/pilot-notes.md. Nothing is committed; those are the only two files I changed. The untracked dotfiles and `scripts` directory in the repository root were already there and I left them alone.

### 001038, Azcorra et al. 2023

Sixteen claims reproduced, seven partially and one not reproduced on the
dandiset, none blocked. Five claims on data in other archives: two
reproduced, on the snRNA-seq count matrices in GEO (GSE222558), and three
blocked. Round 1 gave its own outcome for each claim from the notebook with
its conclusions removed and agreed with all 29, giving other reasons only for
the three blocked claims; the author kept `not_runnable` for the two claims
that need Seurat and LIGER in R and `other` for the histology claim, which
rests on manual cell counts that are not deposited, as the images are public
on Zenodo. After round 1, `fig5ab-transient-scaling` uses the recomputed onsets
that are also stored, which carry the code's exclusion after every reward
(241, 246 and 232% against 239, 266 and 222% before), and stays partially
reproduced. Round 2 agreed with all 29 and nothing was proposed, so there was
no third round. The paper reports that genetic subtypes of dopamine neurons
signal differently: Vglut2 and Calb1 axons in striatum show transients after
decelerations and respond to rewards and air puffs, Anxa1 axons show
transients after accelerations, have almost no reward response and decrease
to air puffs, the subtypes can be clustered from these responses, and somas in
SNc track their axons. The recording counts, the cross-correlations with
acceleration and their lags, PCA and angles, triggered averages and transient
scaling, the reward and air puff responses, the k-means clustering, the soma
and axon correlations, the SNc responses, Aldh1a1 heterogeneity, the overlap
region and two snRNA-seq claims were tested; the snRNA-seq clustering and the
integration of four published datasets are blocked as `not_runnable`.
`recording-counts-locomotion` is not reproduced: the Methods' criteria select
50, 28, 82, 89 and 85 striatal recordings for Vglut2, Calb1, Anxa1, DAT and
Aldh1a1, against 42, 22, 47, 74 and 75, and no variant gives the paper's
counts. Some outcomes rest on weak ground: the 18 claims that use the
locomotion selection are tested on this larger set; `fig2jk-pca-variance` is
inside tolerance by 0.5 and 0.02 points; in `fig2l-pc-angles` the Anxa1 mean
depends on where the circle is cut (circular mean 301.3 against 233.3
degrees); `fig4g-reward-response` is partially reproduced with the Methods'
windows, while the code's windows give the paper's 7.90, 12.40 and 5.88; the
cause of the Vglut2 peak timing in `ed6f-dec-peak-timing` and of the DAT air
puff mean (2.69 against 5.3) is not found; and the deep band of
`ed1h-aldh1a1-depth` holds 5 recordings. The author used the open access full
text (PMC10545540) and took what the Methods leave open from the paper's code
at commit fad12b2.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
The files carry the signal-to-noise ratio and 405 nm cross-correlation but not
the other exclusion flags (running time, 405 nm artifacts) or which recordings
each figure uses; recomputed with the paper's code, the stimulus analyses give
the paper's counts exactly, but the locomotion criteria select more striatal
recordings than Figure 2 reports (Anxa1 82 against 47, Vglut2 50 against 42).
The Events table lists consumed rewards only, and rewards the mouse did not
lick for are only in the raw 4 kHz Reward trace, so 911 acceleration and 767
deceleration onsets recomputed from the processed data are not in the stored
WheelEvents. The `coordinates` column of the fiber table is described as (AP,
ML, DV) but holds (ML, AP, DV), and 785 of 790 SNc fibers and 1281 of 2137
fibers overall have no coordinates. The column
`cross_correlation_with_acceleration` holds the peak cross-correlation of the
405 nm control with acceleration, not of dF/F, and is missing where running
was under 100 s. The dF/F series are normalized so that the largest transient
is 1, which the files do not state, and the normalization factor in
`normalized_fluorescence` holds two values per row in 123 files. Other
findings: three subject ids ending in L are left-hemisphere recordings of mice
that also have ids without it, so the archive's 105 subjects are 102 mice, and
the age is a range (P8W/P16W) in every file; the published version's link to
the paper is malformed (fixed in the draft) and its asset summary lists only
"analytical technique" and "ProcessingModule"; the code integrates responses
over windows that differ from the Methods', and the paper's reward means equal
those of the code's windows to the decimal, as do its Vglut2, Calb1 and Anxa1
air puff means within tolerance, while its DAT air puff mean (5.3) does not
(2.46); the code reports trough and peak times 0.02 and 0.01 s later than the
Methods define, prints uncorrected p-values for Figures 2i and 7f, whose
legends state Bonferroni correction, and marks 405 nm artifacts from the last
noisy section to the end of a recording and from the start to the first; and
the paper swaps the Calb1 and Vglut2 reward P-values between the Results and
the Figure 4g legend, gives 10 Anxa1 mice in the Figure 2f legend and 9 in the
Methods, and gives different SNc variance values in Extended Data Figure 9k
and the Methods. No recording is deposited twice.

The notebook ran in 182 s in the first clean run, `tools/entry.py all` took
107 s after round 1 and 2.3 minutes after round 2. The first metadata scan
took 30 minutes, as h5py serializes calls across threads and every download
URL needed its own API request, and was sped up with a process pool, the bulk
asset listing and BLAS limited to one thread; early runs crashed on the files
with two `normalized_fluorescence` values per row; and the paper's 4.4 GB
MATLAB table on Zenodo, which carries the exclusion flags, was not practical
to parse. Round 2 found statements the outputs did not support, among them
that the Calb1 trough lag with the code's timing equals the paper's, that the
response means match to the decimal, which fails for the DAT air puff mean,
and that the overlap recordings come from the same mice, as well as findings
with no output behind them, and these were corrected. Untracked files in the
repository root that the author did not create were left alone. The author's
points on the protocol: Methods and code that disagree where the code gives
the paper's numbers; a count claim that fails while other claims use its
selection; whether analysis parameters taken from the paper's code count as
inputs; `not_runnable` for software in R and no category for manual cell
counting; a 10% tolerance for a value near zero and for angles; a MATLAB
k-means seed that cannot be repeated; and selection counts and one session's
values seen before the criteria were written.

## End of run

15 turns, 2 minutes, result: success.
