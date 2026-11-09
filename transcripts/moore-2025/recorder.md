# 001699 · recorder · run 39214867545

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001699 --write; git diff; ls transcripts/001699/ claims/001699/; cat attempts/001699-moore-2025-01.yaml
```

```
<persisted-output>
Output too large (54.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/bv1e4mlr9.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 330e004..91ca402 100644
--- a/README.md
+++ b/README.md
@@ -99,6 +99,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 (+1) | 0 (+2) | 3 (+1) | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
 | [001550](https://dandiarchive.org/dandiset/001550) | [Pagan et al. 2025](https://doi.org/10.1038/s41586-024-08433-6) | 11 (+2) | 2 | 0 (+1) | 0 | [`001550-pagan-2025`](entries/001550-pagan-2025) |
 | [001692](https://dandiarchive.org/dandiset/001692) | [Bouabid et al. 2026](https://doi.org/10.64898/2026.01.20.700614) | 18 | 8 | 3 | 0 | [`001692-bouabid-2026`](entries/001692-bouabid-2026) |
+| [001699](https://dandiarchive.org/dandiset/001699) | [Moore et al. 2025](https://doi.org/10.1101/2025.01.09.632139) | 14 | 7 | 5 | 1 | [`001699-moore-2025`](entries/001699-moore-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001699/:
10.1101-2025.01.09.632139.yaml

transcripts/001699/:
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; sed -n '90,110p' README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
README.md | 1 +
 1 file changed, 1 insertion(+)
| [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
| [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
| [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
| [001038](https://dandiarchive.org/dandiset/001038) | [Azcorra et al. 2023](https://doi.org/10.1038/s41593-023-01401-9) | 16 | 7 | 1 | 0 | [`001038-azcorra-2023`](entries/001038-azcorra-2023) |
| [001075](https://dandiarchive.org/dandiset/001075) | [Randi et al. 2023](https://doi.org/10.1038/s41586-023-06683-4) | 4 | 4 (+1) | 0 (+1) | 7 | [`001075-randi-2023`](entries/001075-randi-2023) |
| [001084](https://dandiarchive.org/dandiset/001084) | [Vu et al. 2024](https://doi.org/10.1016/j.neuron.2023.12.011) | 10 (+1) | 10 | 0 | 1 | [`001084-vu-2024`](entries/001084-vu-2024) |
| [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
| [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
| [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
| [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 (+1) | 0 (+2) | 3 (+1) | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
| [001550](https
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^| Dandiset' README.md; sed -n '3633,4114p' docs/pilot-notes.md
```

```
<persisted-output>
Output too large (33.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/b67v0vik3.txt

Preview (first 2KB):
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
### 001172, Lohani et al. 2022

Thirteen claims reproduced, seven partially, one not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 26, but noted that
the wheel predictor of the Figure 2 regressions was signed speed while the
paper says locomotion speed. The author then made |speed| the main predictor,
under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
agreed with 25 of the 26 and disputed that reason: the Methods define speed as
a differential of distance, which keeps the sign, and the paper's
`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
signed speed, added a comparison with the paper's own per-mouse R2 values in
`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/b67v0vik3.txt"
}
```

```
1	49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
2	### 001172, Lohani et al. 2022
3	
4	Thirteen claims reproduced, seven partially, one not reproduced and five
5	blocked on the dandiset. Round 1 gave its own outcome for each claim from the
6	notebook with its conclusions removed and agreed with all 26, but noted that
7	the wheel predictor of the Figure 2 regressions was signed speed while the
8	paper says locomotion speed. The author then made |speed| the main predictor,
9	under which wheel speed beats face PC1 in grabAM06 (0.147 against 0.142), and
10	lowered `fig2c-face-best-predictor-calcium` to partially reproduced. Round 2
11	agreed with 25 of the 26 and disputed that reason: the Methods define speed as
12	a differential of distance, which keeps the sign, and the paper's
13	`wheel_changepoints.m` uses a signed `db1SpeedMpS`. The author returned to
14	signed speed, added a comparison with the paper's own per-mouse R2 values in
15	`Fig2RawData.mat`, where the row matched to grabAM05 gives a calcium wheel R2
16	of 0.0246 against 0.0253 here with signed speed and 0.0483 with |speed|, and
17	proposed reproduced. A third round reviewed only that proposal and agreed, and
18	the claim is reproduced. The paper images ACh (ACh3.0) and calcium (jRCaMP1b)
19	together across the dorsal neocortex of awake mice, and reports that facial
20	movement and locomotion relate to both signals with opposite
[... 464 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001699-moore-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '001699' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (53KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/bky49ssvj.txt

Preview (first 2KB):
schema_version: 1
id: 001699-moore-2025-01
dandiset: 001699
dandiset_version: 0.260917.2322
paper: doi:10.1101/2025.01.09.632139
date: 2026-10-19
entry: 001699-moore-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
outcomes:
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/bky49ssvj.txt"
}
```

```
1	schema_version: 1
2	id: 001699-moore-2025-01
3	dandiset: 001699
4	dandiset_version: 0.260917.2322
5	paper: doi:10.1101/2025.01.09.632139
6	date: 2026-10-19
7	entry: 001699-moore-2025
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: unit-counts
18	  outcome: partially_reproduced
19	  notebook: reproduce_moore_2025.ipynb
20	  output: claim:unit-counts
[... 860 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any(str(v)=='001699' for v in x.values()): print(json.dumps(x,indent=1))
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
head -80 claims/001699/10.1101-2025.01.09.632139.yaml; wc -l claims/001699/*.yaml transcripts/001699/*report.md
```

```
{
 "dandiset": "001699",
 "name": "Altered developmental profile of the head-direction signal in a rat model of fragile X syndrome",
 "published_version": "0.260917.2322",
 "asset_count": 98,
 "size_gb": 825.12,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rattus norvegicus - Norway rat"
 ],
 "approaches": [
  "behavioral approach",
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1101/2025.01.09.632139",
   "title": "Age-dependent alterations in the head-direction signal in a rat model of Fragile X Syndrome",
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "converted by CatalystNeuro" docs/pilot-notes.md | grep -v "to-nwb)" ; grep -n "contributor" docs/pilot-notes.md | head; cat transcripts/001699/*report.md
```

```
<persisted-output>
Output too large (34.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/84ca3e3e-2ea7-4dff-bb16-c3841ede0781/tool-results/bsh3dxt8u.txt

Preview (first 2KB):
1038:The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
1291:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1364:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1421:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1490:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1559:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
1849:The dandiset was converted by CatalystNeuro (Benjamin Dichter of
1930:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
2014:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
2094:The dandiset was converted by CatalystNeuro (Benjamin Dichter and Luiz
2181:The dandiset was converted by CatalystNeuro (Luiz Tauffer and Benjamin
2262:The dandiset was converted by CatalystNeuro
2343:The dandiset was converted by CatalystNeuro (Cody Baker of CatalystNeuro is
2533:The dandiset was converted by CatalystNeuro (Garrett Flynn and Cody Baker of
2895:The dandiset was converted by CatalystNeuro (Szonja Weigl of CatalystNeuro
3367:The dandiset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001699; for f in author-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-report.md
I'm done with steps 1 to 6 and the entry passes `check` and `run`. Of the 27 claims, 14 are reproduced, 10 partially reproduced, 2 not reproduced and 1 blocked. I used the paper's full text: the bioRxiv preprint is open access (CC BY-NC). The claims come from version 1, whose title you named and which the dandiset links. I also read the revised version 2 (January 2026), used its Methods only where version 1 says nothing, and put its numbers in the notes. Nothing is committed.

## 1. Outcomes per claim

| Claim | Outcome |
|---|---|
| unit-counts | partially reproduced (3 of 4 groups exact) |
| units-per-recording | partially reproduced |
| figs1c-juvenile-behaviour-similar | reproduced (speed while active p = 0.0504) |
| figs2c-adult-behaviour-similar | reproduced |
| figs1-juvenile-cell-metrics-similar | reproduced |
| figs2-adult-cell-metrics-similar | reproduced |
| fig1ef-juvenile-sharper-tuning | partially reproduced (HD information p = 0.033; half-width no) |
| fig1g-juvenile-halves-correlation | partially reproduced (r 0.76 and 0.84 against the paper's 0.90 and 0.95) |
| fig1h-juvenile-smaller-offset | reproduced (p = 0.0125) |
| fig1j-juvenile-less-drift | not reproduced (p = 0.079, same direction) |
| figs1j-juvenile-epochs-correlation | partially reproduced |
| figs1k-juvenile-epoch-drift-similar | reproduced |
| fig2c-juvenile-isomap-wake-correlation | reproduced |
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001699; for f in verifier-1-report.md verifier-2-report.md verifier-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
I checked all 27 claims in the claims file and assigned outcomes myself from the notebook outputs, since the attempt record was not in my materials. My tally is 14 reproduced, 7 partially reproduced, 5 not reproduced and 1 blocked. The main caveat is the relabelling of rat H3026 (problem 1): with the archive's own genotype labels, three of the four juvenile positive results stop being significant.

**What I checked**
- **LME test:** `hdfx.lme_lrt` matches statsmodels on synthetic data to four decimals, for both the coefficient and the likelihood-ratio p (maximum-likelihood fits).
- **Other helpers on synthetic inputs:** `hd_info`, `half_width`, `vector_length`, `offset_deg`, `trough_to_peak` and `contamination` behave as expected, in the right units.
- **Train/test split:** the decoder builds tuning curves from the first half of session 1 and decodes only the second half, so there is no leakage.
- **Chance levels:** none of the claims states one.
- **Paper:** version 1 is saved as `paper/v1.xml` and `paper/v1.txt`.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| unit-counts | partially_reproduced | Cell 26, reading (a): juvenile WT 406/7, juvenile KO 372/5 and adult WT 543/6 match exactly; adult KO is 440/5 against 507/6, so 3 of 4 groups match. The archive's labels match 0 of 4. |
| units-per-recording | partially_reproduced | Cell 28: juvenile 8 to 83 matches under (a) all units. Adult is 55 to 114 under (a) and 30 to 81 under (b), so the adult pair never holds under one reading. |
| figs1c-juvenile-behaviour-similar | reproduced | Cell 30: p = 0.37, 0.085 and 0.0504, none significant. Fragile: the speed t is 2.22 against the paper's 1.53, and the first-day variant gives p = 0.031. |
| figs2c-adult-behaviour-similar | reproduced | Cell 30: p = 0.98, 0.35 and 0.67 (t(9); only 5 adult KO rats). |
| figs1-juvenile-cell-metrics-similar | reproduced | Cell 32: LME p = 0.71, 0.72, 0.62 and 0.11. |
| figs2-adult-cell-metrics-simila
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 "statement:" claims/001699/*.yaml | grep -v "^--" | head -120
```

```
46:  statement: 406 units were recorded from 7 juvenile WT rats and 372 from 5 juvenile Fmr1-/y rats;
47-    543 units from 6 adult WT rats and 507 from 6 adult Fmr1-/y rats.
48-  source: Results, paragraphs 2 and 5
49-  expected:
80:  statement: Juvenile recordings held 8 to 83 putative excitatory units each, adult recordings 30
81-    to 114.
82-  source: Results, paragraphs 2 and 5
83-  expected:
101:  statement: Juvenile Fmr1-/y and WT rats do not differ in the time spent inactive, the time spent
102-    in the centre of the arena, or the speed while active.
103-  source: Figure S1c (t-tests on animal averages, t(10) = 1.53, 1.07 and 1.53, P > 0.05)
104-  criterion: Claim of absence, judged by two-sided Student's t-tests on animal averages at 0.05.
110:  statement: Adult Fmr1-/y and WT rats do not differ in the time spent inactive, the time spent in
111-    the centre of the arena, or the speed while active.
112-  source: Figure S2c (t-tests on animal averages, t(10) = 1.21, 0.29 and 0.51, P > 0.05)
113-  criterion: As for figs1c-juvenile-behaviour-similar, on the adult rats.
115:  statement: In juveniles, cluster contamination, mean and peak firing rates, and the resultant
116-    vector length of PoSub cells do not differ between genotypes.
117-  source: Figure S1f-i (LME, no genotype effect, P > 0.05)
118-  criterion: Claim of absence, by the LME test at 0.05 on the cells of session 1. Mean rate is
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn -i "postsubic\|head-direction cells\|HD cells" claims/001699/ attempts/001699-moore-2025-01.yaml transcripts/001699/*report.md | head
```

```
attempts/001699-moore-2025-01.yaml:398:    H4823). No image annotates the probe tract or the postsubiculum, and the electrodes table gives a
```

**Agent calls Bash**

```bash
cd  tail -c 200 docs/pilot-notes.md | od -c | tail -3
```

```
0000260   R   x   i   v       b   l   o   c   k   e   d       d   o   w
0000300   n   l   o   a   d   s   .  \n
0000310
```

**Agent calls Bash**

```bash
cd  cat >> docs/pilot-notes.md <<'EOF'

### 001699, Moore et al. 2025

Fourteen claims reproduced, seven partially, five not reproduced and one
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 27; it would
call `fig1g-juvenile-halves-correlation`, `fig3g-adult-halves-correlation` and
`figs2j-adult-epochs-correlation` not reproduced, as neither of their two
values is within tolerance. The author applied that rule to all correlation
claims and changed fig3g and figs2j, but after fixes to spike counting and a
cut of every session to its first 20 min, the paper's session length, fig1g
gave a WT r of 0.815 against a bound of 0.81 and stayed partially reproduced.
In the same revision Isomap was fitted on every bin, as the criterion says, and
`fig2d-juvenile-isomap-wake-sharper` went from reproduced to not reproduced (p
= 0.056) and `fig2h-juvenile-isomap-rem-sharper` from not reproduced to
reproduced (p = 0.045). Round 2 agreed with all 27 but noted that the 20 min
cut departs from the claims file's session definition, which keeps blocks
whole and cuts only those over 30 min to 1300 s; under that definition fig1g
gives r = 0.761 and 0.839, neither within tolerance, the author proposed not
reproduced, and a third round reviewed only that proposal and agreed. The
paper, a bioRxiv preprint, records head-direction cells in the postsubiculum
(PoSub) of juvenile and adult Fmr1-/y and WT rats, and reports that juvenile
Fmr1-/y cells have higher HD information and drift less relative to the room,
also when tuned to the Isomap angle of waking and REM sleep activity, while in
adults tuning does not differ and Fmr1-/y tuning curves drift more within and
between sessions. The unit counts, behaviour, cell metrics, HD tuning, its
stability between halves and between sessions, the drift of tuning curves and
of a Bayesian decoder, and the Isomap tuning in waking and REM sleep were
tested. `figs1d-probe-in-posub` is blocked as `other`: all 36 files hold
histology images, but none marks the probe tract or PoSub, and judging them
needs an anatomist. Besides fig1g, `fig3g-adult-halves-correlation` (r = 0.804
and 0.748 against 0.94) and `figs2j-adult-epochs-correlation` (0.787 and 0.562
against 0.90 and 0.76) are not reproduced, `fig1j-juvenile-less-drift` gives
the paper's direction at t(10) = -1.91, p = 0.085, and fig2d gives p = 0.056.
Some outcomes rest on weak ground: the main grouping counts H3026, labelled WT,
as a juvenile Fmr1-/y rat and H3029, whose date of birth makes it an adult, as
a juvenile WT rat, chosen because it matches the paper's unit counts, and with
H3026 left out the HD information of `fig1ef-juvenile-sharper-tuning`, fig1h
and fig2h give p = 0.072, 0.068 and 0.095; fig2h is at the threshold, with p
= 0.16 on the first day alone; `fig1h-juvenile-smaller-offset` gives p = 0.060
for cells with half-width below 120 degrees; cells re-recorded on later days
are counted on each day, as the files give no probe depth per day; and the
active speed of `figs1c-juvenile-behaviour-similar` differs on the first day
alone (p = 0.034). The author used the full text of version 1 of the preprint,
which the dandiset links, and version 2's Methods only where version 1 leaves
a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in rounds 2 and after, so the version-2 numbers in the notes were
not checked by a verifier.

The dandiset was converted by CatalystNeuro (Paul Adkisson-Floro of
CatalystNeuro is a contributor). The paper's unit counts (406 units in 7
juvenile WT rats, 372 in 5 juvenile Fmr1-/y rats, 543 in 6 adult WT rats) and
its range of 8 to 83 units per juvenile recording are matched exactly only if
H3026 and H3029 are regrouped as above; with the archive's labels the juvenile
groups have 5 WT and 4 Fmr1-/y rats, and the juvenile effects weaken (HD
information p = 0.23, offsets p = 0.17). The file of H4825 holds the recording
of H4824 (identical waveforms, unit and spike counts, and spike times up to
1248 s), with its spike and tracking times shifted piece by piece onto H4825's
epoch table and clipped at its end, where 131373 spikes share the last spike
time and 12970 tracking frames repeat a timestamp; H4825's own recording is not
in the dandiset, so the adult Fmr1-/y group has 5 rats and 440 units where the
paper has 6 and 507. The dates of birth of H3023 (2022-08-13) and H3026
(2022-09-13) are after their recordings in 2021, so the archive's asset
metadata give them negative ages (P-366D to P-344D), H3029 shares H4830's date
of birth, and no NWB file sets the subject's age. The units table holds only
spike times, mean waveforms, electrode group and sampling rate, with no cell
type, contamination or depth, so the paper's exclusion of cells recorded in
the part of PoSub already recorded on the previous day cannot be repeated. The
epochs and processing/tasks tables do not mark the exploration sessions
reliably: in H3001 200202 task epoch 1 is called wake but lasts 94 min without
tracking, in H3026 211003 epoch 1 spans 112 min of waking and sleep, in H3023
210813-1 epoch 2 runs from the end of the first session into the second, and
H4823 has a single epoch and no sleep task; every file's session description
mentions a cue rotation, and most files hold a third tracked session
(`wake_cue_rot`) that version 1 of the paper does not describe. Spikes and
tracking share a clock in 32 of 35 recordings, and in the other three the cells
are too weakly tuned to show it. Other findings: in H3015 210417 and H4823
221108 position is stated in centimetres but spans about 300 and 700 units, so
it is in pixels, and head direction runs from -pi to pi where the other files
use 0 to 2 pi; one unit of H3023 210812 has spike times out of order, and 22 of
the 24 juvenile files have one to three tracking frames whose timestamp does
not increase; the dandiset's `about` field lists "Fmr1 protein, rat" as an
anatomy term with the MeSH identifier of Fragile X Syndrome (D005600); the
paper's analysis code is not public, and the repository the dandiset links,
woodcode (commit 61ee178), is the lab's general library; and in the paper the
Methods exclude units with contamination scores "below 0.5", which would remove
1727 of 1761 units, the ranges of units per recording mix counts of all units
(8 to 83, maximum 114) with a count of putative excitatory units (minimum 30),
and version 2 gives the adult counts as 372 and 406 units in 6 rats each, the
juvenile numbers repeated.

The notebook ran in 154 to 162 s in the first clean run, 282 s after round 1,
about 13 minutes after round 2, which repeated every claim's main test under
both session definitions, and 789 s after round 3. The statsmodels mixed-model
fits failed to converge on several measures, one giving p = 1.0, and the author
replaced them with an exact profile-likelihood fit of the same model, which
matched statsmodels to 8 digits on a synthetic case. Round 1 also found that
frame counting on speed-filtered frames lost spikes (2.6% on synthetic data)
and that the decoder error was interpolated before unwrapping, and both were
fixed. Round 2 found statements the outputs did not support, among them
archive-label p values kept from round 1, a cause for the 279 decoded bins of
H3001 200201 that no output showed, and the 20 min cut presented as following
the paper, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: two preprint versions under one DOI; no rule for correlation values
outside tolerance; no rule for which grouping is the main one when the
archive's labels contradict the paper's own counts; counting each recording
once where a count claim matches only if the duplicate is counted; linked code
that is the lab's general library and not the paper's analysis; no rule for
claims of absence that rest on several tests; no blocking reason for images
that need expert judgement; and a contamination threshold in the Methods that
would remove almost every unit.
EOF
grep -c "—\|rather" <(sed -n '4115,$p' docs/pilot-notes.md); git status --short
```

```
0
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

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes.md'; s=open(p).read()
a="""Fmr1-/y cells have higher HD information and drift less relative to the room,
also when tuned to the Isomap angle of waking and REM sleep activity, while in"""
b="""Fmr1-/y cells have higher HD information, also against the Isomap angle of
waking and REM sleep activity, and drift less relative to the room, while in"""
c="""a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in rounds 2 and after, so the version-2 numbers in the notes were
not checked by a verifier."""
d="""a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in round 2 and its revision, so the version-2 numbers in the notes
were not checked by a verifier."""
assert s.count(a)==1 and s.count(c)==1
s=s.replace(a,b).replace(c,d); open(p,'w').write(s)
E
git diff --stat
```

```
README.md           |   1 +
 docs/pilot-notes.md | 112 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 113 insertions(+)
```

**Agent**

I added the 001699 row to README.md with `tools/readme_row.py`; it reads 14 reproduced, 7 partially, 5 not reproduced and 1 blocked. I also appended the subsection below to the end of docs/pilot-notes.md. Nothing is committed. The attempt, claims and entry are unchanged, and I left the untracked files in the repository root alone.

The `catalystneuro` field for this dandiset names a contributor (Paul Adkisson-Floro), not a repository. So I opened the second paragraph the way earlier subsections do for that case: "(… of CatalystNeuro is a contributor)".

### 001699, Moore et al. 2025

Fourteen claims reproduced, seven partially, five not reproduced and one
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 27; it would
call `fig1g-juvenile-halves-correlation`, `fig3g-adult-halves-correlation` and
`figs2j-adult-epochs-correlation` not reproduced, as neither of their two
values is within tolerance. The author applied that rule to all correlation
claims and changed fig3g and figs2j, but after fixes to spike counting and a
cut of every session to its first 20 min, the paper's session length, fig1g
gave a WT r of 0.815 against a bound of 0.81 and stayed partially reproduced.
In the same revision Isomap was fitted on every bin, as the criterion says, and
`fig2d-juvenile-isomap-wake-sharper` went from reproduced to not reproduced (p
= 0.056) and `fig2h-juvenile-isomap-rem-sharper` from not reproduced to
reproduced (p = 0.045). Round 2 agreed with all 27 but noted that the 20 min
cut departs from the claims file's session definition, which keeps blocks
whole and cuts only those over 30 min to 1300 s; under that definition fig1g
gives r = 0.761 and 0.839, neither within tolerance, the author proposed not
reproduced, and a third round reviewed only that proposal and agreed. The
paper, a bioRxiv preprint, records head-direction cells in the postsubiculum
(PoSub) of juvenile and adult Fmr1-/y and WT rats, and reports that juvenile
Fmr1-/y cells have higher HD information, also against the Isomap angle of
waking and REM sleep activity, and drift less relative to the room, while in
adults tuning does not differ and Fmr1-/y tuning curves drift more within and
between sessions. The unit counts, behaviour, cell metrics, HD tuning, its
stability between halves and between sessions, the drift of tuning curves and
of a Bayesian decoder, and the Isomap tuning in waking and REM sleep were
tested. `figs1d-probe-in-posub` is blocked as `other`: all 36 files hold
histology images, but none marks the probe tract or PoSub, and judging them
needs an anatomist. Besides fig1g, `fig3g-adult-halves-correlation` (r = 0.804
and 0.748 against 0.94) and `figs2j-adult-epochs-correlation` (0.787 and 0.562
against 0.90 and 0.76) are not reproduced, `fig1j-juvenile-less-drift` gives
the paper's direction at t(10) = -1.91, p = 0.085, and fig2d gives p = 0.056.
Some outcomes rest on weak ground: the main grouping counts H3026, labelled WT,
as a juvenile Fmr1-/y rat and H3029, whose date of birth makes it an adult, as
a juvenile WT rat, chosen because it matches the paper's unit counts, and with
H3026 left out the HD information of `fig1ef-juvenile-sharper-tuning`, fig1h
and fig2h give p = 0.072, 0.068 and 0.095; fig2h is at the threshold, with p
= 0.16 on the first day alone; `fig1h-juvenile-smaller-offset` gives p = 0.060
for cells with half-width below 120 degrees; cells re-recorded on later days
are counted on each day, as the files give no probe depth per day; and the
active speed of `figs1c-juvenile-behaviour-similar` differs on the first day
alone (p = 0.034). The author used the full text of version 1 of the preprint,
which the dandiset links, and version 2's Methods only where version 1 leaves
a procedure out (the decoder and the speed smoothing); bioRxiv refused
downloads in round 2 and its revision, so the version-2 numbers in the notes
were not checked by a verifier.

The dandiset was converted by CatalystNeuro (Paul Adkisson-Floro of
CatalystNeuro is a contributor). The paper's unit counts (406 units in 7
juvenile WT rats, 372 in 5 juvenile Fmr1-/y rats, 543 in 6 adult WT rats) and
its range of 8 to 83 units per juvenile recording are matched exactly only if
H3026 and H3029 are regrouped as above; with the archive's labels the juvenile
groups have 5 WT and 4 Fmr1-/y rats, and the juvenile effects weaken (HD
information p = 0.23, offsets p = 0.17). The file of H4825 holds the recording
of H4824 (identical waveforms, unit and spike counts, and spike times up to
1248 s), with its spike and tracking times shifted piece by piece onto H4825's
epoch table and clipped at its end, where 131373 spikes share the last spike
time and 12970 tracking frames repeat a timestamp; H4825's own recording is not
in the dandiset, so the adult Fmr1-/y group has 5 rats and 440 units where the
paper has 6 and 507. The dates of birth of H3023 (2022-08-13) and H3026
(2022-09-13) are after their recordings in 2021, so the archive's asset
metadata give them negative ages (P-366D to P-344D), H3029 shares H4830's date
of birth, and no NWB file sets the subject's age. The units table holds only
spike times, mean waveforms, electrode group and sampling rate, with no cell
type, contamination or depth, so the paper's exclusion of cells recorded in
the part of PoSub already recorded on the previous day cannot be repeated. The
epochs and processing/tasks tables do not mark the exploration sessions
reliably: in H3001 200202 task epoch 1 is called wake but lasts 94 min without
tracking, in H3026 211003 epoch 1 spans 112 min of waking and sleep, in H3023
210813-1 epoch 2 runs from the end of the first session into the second, and
H4823 has a single epoch and no sleep task; every file's session description
mentions a cue rotation, and most files hold a third tracked session
(`wake_cue_rot`) that version 1 of the paper does not describe. Spikes and
tracking share a clock in 32 of 35 recordings, and in the other three the cells
are too weakly tuned to show it. Other findings: in H3015 210417 and H4823
221108 position is stated in centimetres but spans about 300 and 700 units, so
it is in pixels, and head direction runs from -pi to pi where the other files
use 0 to 2 pi; one unit of H3023 210812 has spike times out of order, and 22 of
the 24 juvenile files have one to three tracking frames whose timestamp does
not increase; the dandiset's `about` field lists "Fmr1 protein, rat" as an
anatomy term with the MeSH identifier of Fragile X Syndrome (D005600); the
paper's analysis code is not public, and the repository the dandiset links,
woodcode (commit 61ee178), is the lab's general library; and in the paper the
Methods exclude units with contamination scores "below 0.5", which would remove
1727 of 1761 units, the ranges of units per recording mix counts of all units
(8 to 83, maximum 114) with a count of putative excitatory units (minimum 30),
and version 2 gives the adult counts as 372 and 406 units in 6 rats each, the
juvenile numbers repeated.

The notebook ran in 154 to 162 s in the first clean run, 282 s after round 1,
about 13 minutes after round 2, which repeated every claim's main test under
both session definitions, and 789 s after round 3. The statsmodels mixed-model
fits failed to converge on several measures, one giving p = 1.0, and the author
replaced them with an exact profile-likelihood fit of the same model, which
matched statsmodels to 8 digits on a synthetic case. Round 1 also found that
frame counting on speed-filtered frames lost spikes (2.6% on synthetic data)
and that the decoder error was interpolated before unwrapping, and both were
fixed. Round 2 found statements the outputs did not support, among them
archive-label p values kept from round 1, a cause for the 279 decoded bins of
H3001 200201 that no output showed, and the 20 min cut presented as following
the paper, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: two preprint versions under one DOI; no rule for correlation values
outside tolerance; no rule for which grouping is the main one when the
archive's labels contradict the paper's own counts; counting each recording
once where a count claim matches only if the duplicate is counted; linked code
that is the lab's general library and not the paper's analysis; no rule for
claims of absence that rest on several tests; no blocking reason for images
that need expert judgement; and a contamination threshold in the Methods that
would remove almost every unit.

## End of run

16 turns, 2 minutes, result: success.
