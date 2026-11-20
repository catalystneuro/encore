# van-der-molen-2025 · recorder · run 44214532013

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py van-der-molen-2025; ls transcripts/van-der-molen-2025/; grep -n -A8 '"001603"' targets/dandisets.json
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
| [001603](https://dandiarchive.org/dandiset/001603) | [Van der molen et al. 2025](https://doi.org/10.1038/s41593-025-02111-0) | 29 | 11 | 7 | 2 | [`van-der-molen-2025`](entries/van-der-molen-2025) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
claims-check-report.md
claims-check.md
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 6685,6720p targets/dandisets.json; grep -n -m3 '^| Dandiset\|^|---' README.md; for f in docs/pilot-notes/{amjad-2025-01,andrews-2024-01,armstrong-2026-01,asari-2009-01,ashworth-2025-01,knierim-2000-02}.md; do echo "=== $f"; cat $f; done; ls summaries | head; cat summaries/$(ls summaries | head -1)
```

```
<persisted-output>
Output too large (41.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/07faeee3-421d-47aa-80f4-5cf4ba574d23/tool-results/bas19d4jw.txt

Preview (first 2KB):
   "dandiset": "001603",
   "name": "Preconfigured neuronal firing sequences in human brain organoids",
   "published_version": "0.260923.0623",
   "asset_count": 111,
   "size_gb": 322.24,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Homo sapiens - Human",
    "Mus musculus - House mouse",
    "Rattus norvegicus - Norway rat"
   ],
   "approaches": [
    "electrophysiological approach"
   ],
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/van-der-molen-2025-01.yaml claims/van-der-molen-2025.yaml
```

```
<persisted-output>
Output too large (160.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/07faeee3-421d-47aa-80f4-5cf4ba574d23/tool-results/baa9t8k46.txt

Preview (first 2KB):
schema_version: 3
id: van-der-molen-2025-01
datasets:
- archive: dandi
  id: '001603'
  version: 0.260923.0623
  doi: 10.48324/dandi.001603/0.260923.0623
  relation: primary
paper: doi:10.1038/s41593-025-02111-0
date: 2026-11-17
entry: van-der-molen-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/07faeee3-421d-47aa-80f4-5cf4ba574d23/tool-results/bas19d4jw.txt"
}
```

```
1	   "dandiset": "001603",
2	   "name": "Preconfigured neuronal firing sequences in human brain organoids",
3	   "published_version": "0.260923.0623",
4	   "asset_count": 111,
5	   "size_gb": 322.24,
6	   "data_standards": [
7	    "Neurodata Without Borders (NWB)"
8	   ],
9	   "species": [
10	    "Homo sapiens - Human",
11	    "Mus musculus - House mouse",
12	    "Rattus norvegicus - Norway rat"
13	   ],
14	   "approaches": [
15	    "electrophysiological approach"
16	   ],
17	   "papers": [
18	    {
19	     "doi": "10.1038/s41593-025-02111-0",
20	     "title": "Preconfigured neuronal firing sequences in human brain organoids",
[... 601 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 '001603' README.md | head; grep -n -m2 'Reproduced\|reproduced |' README.md; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
for e in (d if isinstance(d,list) else d.get('dandisets',d.values())):
    if isinstance(e,dict) and e.get('dandiset')=='001603': print({k:v for k,v in e.items() if k not in('papers','description')})
E
cat summaries/ashworth-2025-01.md summaries/asari-2009-01.md; cat tools/readme_row.py | head -60
```

```
The paper's central findings mostly hold in this data, but the width of the slow rhythm's spectral peaks and the heart-rate spectrum do not. ON and OFF responses around paw withdrawal, their sharper timing against withdrawal than heat onset, the five-minute spectral peaks and the periodic Gaussian process fits all reproduced. Peak widths came out near 90 s against the reported 17 s, and no reading of the described method gives the paper's figure. NEUTRAL cells also showed period minima like ON and OFF cells, and heart-rate spectral peaks at multiples of five minutes were not found. A minor Gaussian-CDF comparison also failed, and the comparison of fit quality between classes depended on which NEUTRAL data were used.
The paper's central finding held in this data: A1 responses depend on the preceding sounds for seconds, while in the thalamus (MGB) the effect fades fast. Its timescale did not match, as the context-dependent power decays with a time constant of 1.74 to 1.78 s against the paper's 1.04 s; the predictability bound missed on its time constant too, and the STRF result failed because a longer window gave a small significant gain. Amplitude and frequency changes outlasted modulation and higher-order changes, but gave smaller effects than natural sounds, on property sets rebuilt because the paper does not list them. The synaptic conductance findings could not be tested, as the data set holds no voltage-clamp recordings.
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from 
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk 'NR>=6685 && NR<=6800' targets/dandisets.json | grep -n -i 'catalyst\|"dandiset"' | head
```

```
1:   "dandiset": "001603",
47:   "catalystneuro": []
50:   "dandiset": "001605",
75:   "catalystneuro": []
78:   "dandiset": "001609",
105:   "catalystneuro": []
108:   "dandiset": "001616",
```

**Agent**

Not converted by CatalystNeuro. Now reading the attempt record.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/07faeee3-421d-47aa-80f4-5cf4ba574d23/tool-results/baa9t8k46.txt",
 "limit": 700
}
```

```
1	schema_version: 3
2	id: van-der-molen-2025-01
3	datasets:
4	- archive: dandi
5	  id: '001603'
6	  version: 0.260923.0623
7	  doi: 10.48324/dandi.001603/0.260923.0623
8	  relation: primary
9	paper: doi:10.1038/s41593-025-02111-0
10	date: 2026-11-17
11	entry: van-der-molen-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 680 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/van-der-molen-2025-01.yaml'))
print([k for k in r])
for v in r['verifications']:
    res=v.get('results',[])
    print('---',v['date'],v['reviewed'][:300]); print('agree',sum(x['agrees'] for x in res),'of',len(res))
    for x in res:
        if not x['agrees']: print('  DIS',x['claim'],x['outcome'],'|',x['reason'][:300],'| RESP',x.get('response','')[:400])
    for k in v:
        if k not in('results','reviewed','date','kind','by'): print(k, str(v[k])[:1500])
c=yaml.safe_load(open('claims/van-der-molen-2025.yaml'))
print([k for k in c if k!='claims'])
for x in c['claims']: print(x['id'],x.get('data'),x.get('kind'),x.get('source','')[:60] if isinstance(x.get('source'),str) else x.get('source'))
E
```

```
Exit code 1
['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications']
--- 2026-11-17 Round 1. The first executed notebooks (reproduce_van_der_molen_2025.ipynb and hmm_van_der_molen_2025.ipynb) with the conclusion cells and the summaries removed, the helper modules sequences.py and hmm.py, and the claims file, with the paper's full text. The verifier read the archive's assets and uni
agree 44 of 50
  DIS fig1e-peaks-near-burst-peak blocked | Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree (blocked, methods_underspecified). | RESP Kept as partially reproduced, with the disagreement recorded. The criterion names the four readings and requires the claim to hold under every one; they are not alternatives between which the paper leaves a choice, so a failure under one is a partial result, not an underspecified method.
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
KeyError: 'outcome'
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/van-der-molen-2025-01.yaml'))
for v in r['verifications']:
    res=v.get('results',[])
    print('---',v['date'],v['reviewed']); print('agree',sum(x['agrees'] for x in res),'of',len(res))
    for x in res:
        if not x['agrees']: print('  DIS',x['claim'],x.get('outcome'),'|',x['reason'][:400],'| RESP',x.get('response','')[:500])
    for k in v:
        if k not in('results','reviewed','date','kind','by'): print(k, str(v[k])[:1500])
c=yaml.safe_load(open('claims/van-der-molen-2025.yaml'))
print({k:str(v)[:600] for k,v in c.items() if k!='claims'})
for x in c['claims']: print(x['id'],x.get('data'),x.get('kind'),str(x.get('source'))[:70])
E
```

```
--- 2026-11-17 Round 1. The first executed notebooks (reproduce_van_der_molen_2025.ipynb and hmm_van_der_molen_2025.ipynb) with the conclusion cells and the summaries removed, the helper modules sequences.py and hmm.py, and the claims file, with the paper's full text. The verifier read the archive's assets and units tables and tested detect_bursts, burst_segments_compressed and the HMM scoring on synthetic inputs. It had no attempt record.
agree 44 of 50
  DIS fig1e-peaks-near-burst-peak blocked | Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree (blocked, methods_underspecified). | RESP Kept as partially reproduced, with the disagreement recorded. The criterion names the four readings and requires the claim to hold under every one; they are not alternatives between which the paper leaves a choice, so a failure under one is a partial result, not an underspecified method.
  DIS supp8-backbone-stable-4h None | The notebook's reason does not hold. In the archive, HO2's 8M and 8M_4H files have 90 units each with identical x_pos/y_pos in the same order. HO3's 4H file equals its 0H file once its unit 24 is dropped. Units are therefore linked. Both recordings were already analysed in L (cell 40), so the test needed only the backbone cross-table and a cross-recording burst-to-burst correlation (problem 2). No | RESP Tested. Units are linked by walking both ordered position lists (all 90 HO2 and 116 HO3 units link; HO3's 4 h unit 24 is left out), stated as an assumption, with each recording's own result. The cross-table and a cross-recording burst-to-burst correlation (sequences.cross_burst_to_burst) give the criterion in both organoids, so the outcome changes from blocked to reproduced (assumed). The identifier_missing finding is revised.
  DIS fig3f-backbone-pairs-in-tail blocked | Cell 47: above the 75th percentile in all four organoids. At the 90th, HO3 fails (87th percentile) (blocked, methods_underspecified). | RESP 
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk '/^claims:/{exit} {print}' claims/van-der-molen-2025.yaml
```

```
# Claims for van der Molen, Spaeth, Chini et al. (2025), "Preconfigured neuronal firing sequences in
# human brain organoids", Nature Neuroscience, doi:10.1038/s41593-025-02111-0, on dandiset 001603.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# version pilot-10 as stated in docs/protocol.md.
#
# Text read. The NIH author manuscript in PubMed Central (PMC12912721.1, NIHMS2139360), as served by
# NCBI PMC on 2026-10-20: main text, Methods, figure legends and Extended Data legends (Figs. 1 to 8),
# with the publisher's Supplementary Information PDF (41593_2025_2111_MOESM1_ESM.pdf; Supplementary
# Figures 1 to 27 and Supplementary Methods). Not the typeset version of record. Figures were not
# opened; every number below is from the text.
#
# Code read. https://github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19), the
# repository named under Code Availability. It holds MATLAB scripts for the spike matrices, bursts,
# backbone units, firing rates, burst-to-burst and pairwise correlations, burst similarity and PCA
# (Main_analyses_matlab, process_data_backbone.m above all), the Python spike shuffling
# (shuffle_spike_mats.py), the HMM analysis in Python with SSM (HMM_analysis_python, with lmem.R for
# the HMM statistics), the burst clustering in Python (burst_clustering_analysis_python), the d2
# results and plotting (Criticality_analysis; the d2 code itself is downloaded from figshare article
# 25927081, Sooter et al.), plotting notebooks, and processed per-figure tables (Processed_data). The
# R scripts for the linear mixed-effects models of Figs. 2, 3, 6 and 7 are not in it.
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/van-der-molen-2025; wc -w *-report.md; cat author-report.md
```

```
118 answer-report.md
  280 author-answers-report.md
  955 author-report.md
  723 author-revise-1-report.md
  553 author-revise-2-report.md
  244 author-revise-3-report.md
  368 claims-check-report.md
  751 claims-report.md
 2369 verifier-1-report.md
 1161 verifier-2-report.md
  666 verifier-3-report.md
 8188 total
I finished steps 1 to 6 and handed the entry over for verification. Both notebooks passed in a clean environment, `tools/entry.py check` reports 0 errors, and the handover is in `executed/van-der-molen-2025/handover/`. Of the 50 claims, 29 are reproduced, 11 partially reproduced, 5 not reproduced and 5 blocked. Nothing is committed.

## 1. Outcome per claim

| Claim | Outcome |
|---|---|
| methods-burst-count | reproduced (mean 35.7, but per recording it ranges from 0 to 156 bursts) |
| fig1c-example-burst-count, ed1c-lognormal-rates, fig1d-burst-duration, fig2-backbone-fraction, fig2e-b2b-correlation, fig2g-variance-latency, ed3f-burst-cluster-variability | reproduced |
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/van-der-molen-2025; for f in claims-report.md claims-check-report.md answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== claims-report.md
I've written `claims/001603/10.1038-s41593-025-02111-0.yaml`. `tools/claims_check.py` finds no problems: 48 claims, 48 quotes, 71 statistical values. Nothing is committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC12912721.1), not the typeset version of record. It has the main text, Methods, figure legends and Extended Data legends. I also read the Supplementary Information PDF, which has Supplementary Figs. 1 to 27 and the Supplementary Methods. Nothing the claims rest on is missing: the HMM, d2, rank-order and burst-clustering methods are all in the Supplementary Methods.

**Code read.** github.com/braingeneers/Protosequences at commit e9a79c4 (2025-05-19). It holds the MATLAB scripts for bursts, backbone units, correlations, burst similarity and PCA; the Python spike shuffling; the HMM code with `lmem.R`; the burst clustering; and per-figure processed tables. The R models for Figs. 2, 3, 6 and 7 are not in it.

**Claims.**
- 48 claims, all with quotes and criteria.
- 31 have statistics.
- 12 have expected values.
- One claim (murine organoid scRNA-seq, Supp. Fig. 5) is `data: elsewhere`, at GEO GSE290330. The dandiset holds only electrophysiology, and that claim is recorded but not tested because the paper does not list its markers.
- The rest use the dataset.
- Seven are claims of absence: two in Fig. 7B and 7C, plus Fig. 7D, Fig. 7E's slices and primaries, Fig. 7F, Supp. Fig. 26 and Extended Data Fig. 2D.

**Where the Methods and the code disagree** (the Methods are followed, the code is run as a variant):
- **Minimum gap between bursts:** 700 ms in the Methods, 800 ms in the code.
- **Units kept for burst-to-burst correlation:** at least 2 spikes in at least 30% of bursts (Methods), against at least 70% (code).
- **HMM cross-validation:** an 80/20 split (Supplementary Methods), against holding out 10% of time-bin by unit entries (code).
- **Lognormal fit:** the code's density divides by (2σ)² where the standard form h
[... 162 more lines not kept]
```

**Agent**

Now the verifier reports.

**Agent calls Bash**

```bash
cd transcripts/van-der-molen-2025; cat verifier-1-report.md | head -c 9000; echo ====; cat verifier-2-report.md | head -c 5000; echo ====; cat verifier-3-report.md | head -c 2500
```

```
**Verifier report, round 1: van der Molen et al. 2025 on DANDI:001603 (0.260923.0623)**

The claims file has 50 claims. The notebook tests 47 of them and marks three as blocked: supp8, supp27 and supp5.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| methods-burst-count | reproduced | Cell 11: the mean is 35.7, inside 38 ± 4. The SE is 6.2 against the paper's 4, and the agreement is fragile: four murine organoids have 0 bursts, offset by MO1 (113) and MO7 (156). |
| fig1c-example-burst-count | reproduced | Cell 13: HO1 has 46 bursts at both 700 and 800 ms. |
| ed1c-lognormal-rates | reproduced | Cell 16, reading (a) with all units: all-unit R² is 0.949 and backbone R² is 0.487 (7 fits, because HO7 has no backbone unit). Both are within tolerance. |
| fig1d-burst-duration | reproduced | Cell 18: HO1 to HO4 medians are 472 to 892 ms. |
| fig1e-peaks-near-burst-peak | blocked: methods_underspecified | Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree. |
| fig2-backbone-fraction | reproduced | Cell 22, reading (b) (units with at least 30 spikes): mean 0.331, SD 0.150, both within tolerance. Under reading (a) the SD of 0.166 is outside tolerance. |
| fig2e-b2b-correlation | reproduced | Cell 24: p 5.9e-36 (30% rule) and 1.5e-19 (70% rule). The test used 216 units. The 507 printed is all sorted units, which is a different quantity. |
| fig2g-variance-latency | reproduced | Cell 26: positive slope, p 3.6e-4 under reading (a) and 4.5e-5 under (b). |
| ed3f-burst-cluster-variability | reproduced | Cell 28: non-rigid CV is higher under all four readings, p ≤ 5e-48. |
| ed4b-gabazine-more-bursts | reproduced | Cell 32: +7.0 bursts per minute, p 5.5e-6. There are 4 paired organoids (MO12 has no baseline sorted file). |
| ed4b-nbqx-cpp-abolish-bursts | reproduced | Cell 34: treated recordings have 0, 0, 1, 0 and 0 bursts; p 3e-53. |
| ed4c-gabazine-participation | reproduced | Cell 36: +0.138, p 9e-4 pooled; the
[... 94 more lines not kept]
```

**Agent**

I have what I need. Writing the notes file.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/van-der-molen-2025-01.md",
 "content": "# van-der-molen-2025, van der Molen et al. 2025\n\nTwenty-nine claims reproduced, eleven partially, seven not reproduced and two\nblocked, both as `methods_underspecified`; `supp5-murine-organoid-forebrain-identity`,\non single-cell data in GEO (GSE290330, `data: elsewhere`), is blocked too and\ncounted apart. Three outcomes rest on an assumption (supp8-backbone-stable-4h,\nfig7d-murine-organoids-slices-same-lag and supp27-d2-near-critical). The first\nverification round agreed with 44 of the 50 outcomes as they stood, the second\nwith 48 and the third, which reviewed only the two changes proposed after the\nsecond, with both. It pins version 0.260923.0623, the only published version;\nthe paper cites none. The paper, van der Molen, Spaeth, Chini et al.,\n\"Preconfigured neuronal firing sequences in human brain organoids\" (Nature\nNeuroscience), records spontaneous activity of sorted units on high-density\nmicroelectrode arrays in human brain organoids (HO1 to HO8), murine organoids\n(MO1 to MO14), acute mouse cortical slices (MS) and primary cortical cultures\n(Pr1 to Pr8), and reports that bursts are organised around backbone units that\nfire in every burst, with higher burst-to-burst and pairwise correlations than\nnon-rigid units, that hidden Markov models (HMMs) find structure in them, and\ncompares these features across the four models. The claims were written from\nthe NIH author manuscript (PMC12912721.1) with the Supplementary Information,\nwithout the version of record, and from the paper's code (Protosequences at\ne9a79c4), which lacks the R models of Figs. 2, 3, 6 and 7; the claims check\nadded `fig4c-similarity-variance` and `supp24d-backbone-non-poisson`, for 50\nclaims. Reproduced are, among others, the burst counts (mean 34.8 over the 31\nrecordings; HO1 has the 46 bursts of Fig. 1C), the backbone fraction, the\nburst-to-burst and pairwise correlations of backbone units in organoids and\nslices, the gabazine and NBQX with R-CPP effects on bursting, burst similarity,\nthe HMM likelihood against shuffled data and the HMM dimensionality across\nmodels. Not reproduced are `fig5c-states-converge-at-peak`,\n`fig5f-svm-states-beat-rate` (states beat rate in neither test, and rate alone\nreaches 89% to 95% in HO2, HO3 and HO4), `fig7b-normalized-b2b`,\n`fig7c-backbone-pairs-above-random`, `fig7d-murine-organoids-slices-same-lag`\nand `fig7e-pca-backbone-variance`, each failing in murine organoids, and\n`ed2d-alam-el-din-rates` (p 0.0019 where the paper has 0.40). Blocked are\n`ed4d-gabazine-rank-order` and `supp10b-rank-order-by-model`, whose two\nnormalisations give opposite results. The author's first run gave 29\nreproduced, 11 partially, 5 not reproduced and 5 blocked, with supp27 not run\nfor lack of time. The author asked a reader nothing, so the answer and\nauthor-answers runs changed nothing. Round 1 found that the burst detector\nemitted duplicate bursts where a long burst holds two peaks, that the HMM\nsurrogate was scored differently from the real data, that the mixed models used\nWald z where the paper uses lmerTest, and that supp8 and the d2 test of supp27\nwere testable after all; in reply overlapping bursts were merged (35 bursts in\n13 recordings), the models moved to Satterthwaite t, the second reading of the\nrecording length was run, units were linked across 0 h and 4 h by their ordered\npositions and the d2 code of Sooter et al. was ported, which made the record\n31 reproduced, 11 partially, 7 not reproduced and 1 blocked, with ed4d and\nsupp10b reproduced on the assumed z-score. Round 2 held that the claims file\nreads the paper correctly on the rank-order normalisation, so both should be\nblocked, asked for one rule for partial outcomes, and found sentences with no\noutput behind them (HO7 has 21 bursts, not 24; a comparison of HO1 to HO4 with\nthe paper's processed tables that was never run), which were corrected; a refit\nwithout MO3 was added, and round 3 agreed to block ed4d and supp10b. The\nauthor's run took about 3 h 35 min (12:17 to 15:52 UTC); its last\n`entry.py all` was killed after 10 minutes because editing the README changed\nthe entry hash and restarted every notebook, and the author-answers run made\nthe full clean run instead. SSM would not install in a locked environment, so\nthe HMMs were fitted with the entry's own EM at K = 10, 12, ..., 30, 41 of 341\nmodels stopping at 300 iterations, and 10 shuffles per recording (3 for some\nmeasures) were run in place of 100. The notebooks ran in 23 and 21 min at\nfirst, 1354 and 1266 s after the author-answers run, 29 and 18 min after round\n1 and 1658 and 1318 s at the end.\n\nThe burst detection parameters for the murine organoids are not given, and with\nthe stated detection (4 x RMS of the 20 ms and 100 ms smoothed population rate)\nMO2, MO4, MO5 and MO6 have no burst and MO3 has four, as their highest peaks\nreach only 3.0 to 3.7 times the RMS, while the paper's code lists backbone\nunits for all nine; the murine results of Fig. 7 rest on five of nine\nrecordings, MO3's four bursts make 160 of its 234 units backbone units, and\nwithout MO3 the murine contrast of Fig. 7B holds and the murine organoid\nagainst slice lag contrast of Fig. 7D is not significant. The rank-order\nnormalisation is z-scored in the Extended Data Fig. 4D legend and (A - B)/(A +\nB) in the Supplementary Methods; on shuffled Spearman correlations centred near\n0 the ratio runs from -86,000 to 3,200, and the two give opposite conclusions.\nThe baseline sorted recording of MO12 and every longitudinal murine organoid\nrecording are missing (every MO file has age P45D), so the murine halves of\nSupplementary Fig. 2 cannot be tested. Units carry positions but no identifier\nacross recordings of one organoid; the ordered positions are identical for HO2\nat 0 h and 4 h (90 units), for HO3 once the 4 h file's unit 24 is left out\n(116 units) and for MO10, MO11 and MO14 between baseline and gabazine, but not\nfor MO13 nor for any NBQX with R-CPP recording, and positions alone are not\nunique (61 distinct positions for 90 HO2 units). The HO2 and HO3 recordings at\n6, 7, 8 months and 8 months plus 4 h are each deposited twice under different\nsession names, and the 7-month ones a third time, with identical spike\nmatrices. The dandiset description says only spike-sorted data are included\nfor the sourced human organoids, but sixteen raw ecephys files are present for\nHO1 to HO4, and the slice files say \"Sorting/curation not specified\". The n\nreported with several tests counts all sorted units or pairs (507 units and\n34,056 pairs in HO1 to HO4, 959 units and 125,607 pairs in the slices), while\nthe stated rules restrict the tests, and the Fig. 7A legend's counts (1048,\n1179, 786, 1048) match neither all units (930, 1273, 959, 2001) nor units with\nat least 30 spikes. Pr1 to Pr4 are rat cultures, as the Methods and files say,\nwhere the paper calls all primary cultures murine. The AR fit check of the d2\nanalysis is not described, and two readings keep 0, 5, 0 and 1 or 7, 9, 3 and 8\nrecordings of HO, MO, MS and PR against the paper's 3, 7, 4 and 7. Three\nquestions are put to the paper's authors: the murine organoid burst parameters,\nthe rank-order normalisation and the level it was applied at, and the d2 fit\ncheck.\n\nThe author's points on the protocol: `entry.py lock` writes a `python:` field\nthat the entry schema rejects; editing the entry's README changes its hash and\nreruns every notebook; step 1.6 adopts the best-supported reading where the\nclaims file makes disagreeing readings `methods_underspecified`, and the claims\nfile was followed; 100 shuffles per recording do not fit the 60-minute\nnotebook limit and the protocol says nothing about running fewer; expected n\nvalues count all sorted units while the criteria restrict the units tested, so\nthe count of all units was recorded as `measured`; the time rule has no\ncategory for a claim never started, and `other` was used for supp27; and the\nrule that every stream shares the trial clock does not apply without trial\ntables.\n"
}
```

```
File created successfully at: docs/pilot-notes/van-der-molen-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent**

Now the summary.

**Agent calls Write**

```json
{
 "file_path": "summaries/van-der-molen-2025-01.md",
 "content": "The paper's central findings on human organoids held in this data: bursts are organised around backbone units that fire in every burst and are more correlated across bursts and with each other than non-rigid units, as in mouse cortical slices, and hidden Markov models fit the bursts better than shuffled data. Two HMM results did not reproduce, as states did not converge at the burst peak in most organoids and state features did not classify units better than firing rate. Several cross-model comparisons in Fig. 7 failed for murine organoids, where the paper does not give the burst detection used and four of nine show no bursts under the stated settings. Minor rank-order claims could not be tested, as the paper gives two conflicting normalisations.\n"
}
```

```
File created successfully at: summaries/van-der-molen-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/van-der-molen-2025-01.md docs/pilot-notes/van-der-molen-2025-01.md; grep -c '—' summaries/van-der-molen-2025-01.md docs/pilot-notes/van-der-molen-2025-01.md; grep -ci rather summaries/van-der-molen-2025-01.md docs/pilot-notes/van-der-molen-2025-01.md; git status --short
```

```
125 summaries/van-der-molen-2025-01.md
1306 docs/pilot-notes/van-der-molen-2025-01.md
1431 total
summaries/van-der-molen-2025-01.md:0
docs/pilot-notes/van-der-molen-2025-01.md:0
summaries/van-der-molen-2025-01.md:0
docs/pilot-notes/van-der-molen-2025-01.md:0
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
?? docs/pilot-notes/van-der-molen-2025-01.md
?? scripts
?? summaries/van-der-molen-2025-01.md
```

**Agent**

The summary is 125 words, over the 120 limit, so I'm trimming it.

**Agent calls Write**

```json
{
 "file_path": "summaries/van-der-molen-2025-01.md",
 "content": "The paper's central findings on human organoids held in this data: bursts are organised around backbone units that fire in every burst and correlate more across bursts and with each other than non-rigid units, as in mouse cortical slices. Hidden Markov models fit the bursts better than shuffled data, but states did not converge at the burst peak in most organoids, and state features did not classify units better than firing rate. Several cross-model comparisons in Fig. 7 failed for murine organoids, where the paper does not give the burst detection used and four of nine show no bursts under the stated settings. Minor rank-order claims could not be tested, as the paper gives two conflicting normalisations.\n"
}
```

```
The file summaries/van-der-molen-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/van-der-molen-2025-01.md
```

```
117 summaries/van-der-molen-2025-01.md
```

**Agent**

I wrote both files and changed nothing else. The untracked dotfiles and `scripts` in the repository root were there before I started; I didn't touch them.

**docs/pilot-notes/van-der-molen-2025-01.md**

# van-der-molen-2025, van der Molen et al. 2025

Twenty-nine claims reproduced, eleven partially, seven not reproduced and two blocked, both as `methods_underspecified`; `supp5-murine-organoid-forebrain-identity`, on single-cell data in GEO (GSE290330, `data: elsewhere`), is blocked too and counted apart. Three outcomes rest on an assumption (supp8-backbone-stable-4h, fig7d-murine-organoids-slices-same-lag and supp27-d2-near-critical). The first verification round agreed with 44 of the 50 outcomes as they stood, the second with 48 and the third, which reviewed only the two changes proposed after the second, with both. It pins version 0.260923.0623, the only published version; the paper cites none. The paper, van der Molen, Spaeth, Chini et al., "Preconfigured neuronal firing sequences in human brain organoids" (Nature Neuroscience), records spontaneous activity of sorted units on high-density microelectrode arrays in human brain organoids (HO1 to HO8), murine organoids (MO1 to MO14), acute mouse cortical slices (MS) and primary cortical cultures (Pr1 to Pr8). It reports that bursts are organised around backbone units that fire in every burst, with higher burst-to-burst and pairwise correlations than non-rigid units, that hidden Markov models (HMMs) find structure in them, and compares these features across the four models. The claims were written from the NIH author manuscript (PMC12912721.1) with the Supplementary Information, without the version of record, and from the paper's code (Protosequences at e9a79c4), which lacks the R models of Figs. 2, 3, 6 and 7; the claims check added `fig4c-similarity-variance` and `supp24d-backbone-non-poisson`, for 50 claims. Reproduced are, among others, the burst counts (mean 34.8 over the 31 recordings; HO1 has the 46 bursts of Fig. 1C), the backbone fraction, the burst-to-burst and pairwise correlations of backbone units in organoids and slices, the gabazine and NBQX with R-CPP effects on bursting, burst similarity, the HMM likelihood against shuffled data and the HMM dimensionality across models. Not reproduced are `fig5c-states-converge-at-peak`, `fig5f-svm-states-beat-rate` (states beat rate in neither test, and rate alone reaches 89% to 95% in HO2, HO3 and HO4), `fig7b-normalized-b2b`, `fig7c-backbone-pairs-above-random`, `fig7d-murine-organoids-slices-same-lag` and `fig7e-pca-backbone-variance`, each failing in murine organoids, and `ed2d-alam-el-din-rates` (p 0.0019 where the paper has 0.40). Blocked are `ed4d-gabazine-rank-order` and `supp10b-rank-order-by-model`, whose two normalisations give opposite results. The author's first run gave 29 reproduced, 11 partially, 5 not reproduced and 5 blocked, with supp27 not run for lack of time. The author asked a reader nothing, so the answer and author-answers runs changed nothing. Round 1 found that the burst detector emitted duplicate bursts where a long burst holds two peaks, that the HMM surrogate was scored differently from the real data, that the mixed models used Wald z where the paper uses lmerTest, and that supp8 and the d2 test of supp27 were testable after all. In reply overlapping bursts were merged (35 bursts in 13 recordings), the models moved to Satterthwaite t, the second reading of the recording length was run, units were linked across 0 h and 4 h by their ordered positions and the d2 code of Sooter et al. was ported. That made the record 31 reproduced, 11 partially, 7 not reproduced and 1 blocked, with ed4d and supp10b reproduced on the assumed z-score. Round 2 held that the claims file reads the paper correctly on the rank-order normalisation, so both should be blocked, asked for one rule for partial outcomes, and found sentences with no output behind them (HO7 has 21 bursts, not 24; a comparison of HO1 to HO4 with the paper's processed tables that was never run), which were corrected; a refit without MO3 was added, and round 3 agreed to block ed4d and supp10b. The author's run took about 3 h 35 min (12:17 to 15:52 UTC); its last `entry.py all` was killed after 10 minutes because editing the README changed the entry hash and restarted every notebook, and the author-answers run made the full clean run instead. SSM would not install in a locked environment, so the HMMs were fitted with the entry's own EM at K = 10, 12, ..., 30, 41 of 341 models stopping at 300 iterations, and 10 shuffles per recording (3 for some measures) were run in place of 100. The notebooks ran in 23 and 21 min at first, 1354 and 1266 s after the author-answers run, 29 and 18 min after round 1 and 1658 and 1318 s at the end.

The burst detection parameters for the murine organoids are not given. With the stated detection (4 x RMS of the 20 ms and 100 ms smoothed population rate) MO2, MO4, MO5 and MO6 have no burst and MO3 has four, as their highest peaks reach only 3.0 to 3.7 times the RMS, while the paper's code lists backbone units for all nine. The murine results of Fig. 7 rest on five of nine recordings, MO3's four bursts make 160 of its 234 units backbone units, and without MO3 the murine contrast of Fig. 7B holds and the murine organoid against slice lag contrast of Fig. 7D is not significant. The rank-order normalisation is z-scored in the Extended Data Fig. 4D legend and (A - B)/(A + B) in the Supplementary Methods; on shuffled Spearman correlations centred near 0 the ratio runs from -86,000 to 3,200, and the two give opposite conclusions. The baseline sorted recording of MO12 and every longitudinal murine organoid recording are missing (every MO file has age P45D), so the murine halves of Supplementary Fig. 2 cannot be tested. Units carry positions but no identifier across recordings of one organoid. The ordered positions are identical for HO2 at 0 h and 4 h (90 units), for HO3 once the 4 h file's unit 24 is left out (116 units) and for MO10, MO11 and MO14 between baseline and gabazine, but not for MO13 nor for any NBQX with R-CPP recording, and positions alone are not unique (61 distinct positions for 90 HO2 units). The HO2 and HO3 recordings at 6, 7, 8 months and 8 months plus 4 h are each deposited twice under different session names, and the 7-month ones a third time, with identical spike matrices. The dandiset description says only spike-sorted data are included for the sourced human organoids, but sixteen raw ecephys files are present for HO1 to HO4, and the slice files say "Sorting/curation not specified". The n reported with several tests counts all sorted units or pairs (507 units and 34,056 pairs in HO1 to HO4, 959 units and 125,607 pairs in the slices), while the stated rules restrict the tests. The Fig. 7A legend's counts (1048, 1179, 786, 1048) match neither all units (930, 1273, 959, 2001) nor units with at least 30 spikes. Pr1 to Pr4 are rat cultures, as the Methods and files say, where the paper calls all primary cultures murine. The AR fit check of the d2 analysis is not described, and two readings keep 0, 5, 0 and 1 or 7, 9, 3 and 8 recordings of HO, MO, MS and PR against the paper's 3, 7, 4 and 7. Three questions are put to the paper's authors: the murine organoid burst parameters, the rank-order normalisation and the level it was applied at, and the d2 fit check.

The author's points on the protocol: `entry.py lock` writes a `python:` field that the entry schema rejects; editing the entry's README changes its hash and reruns every notebook; step 1.6 adopts the best-supported reading where the claims file makes disagreeing readings `methods_underspecified`, and the claims file was followed; 100 shuffles per recording do not fit the 60-minute notebook limit and the protocol says nothing about running fewer; expected n values count all sorted units while the criteria restrict the units tested, so the count of all units was recorded as `measured`; the time rule has no category for a claim never started, and `other` was used for supp27; and the rule that every stream shares the trial clock does not apply without trial tables.

**summaries/van-der-molen-2025-01.md**

The paper's central findings on human organoids held in this data: bursts are organised around backbone units that fire in every burst and correlate more across bursts and with each other than non-rigid units, as in mouse cortical slices. Hidden Markov models fit the bursts better than shuffled data, but states did not converge at the burst peak in most organoids, and state features did not classify units better than firing rate. Several cross-model comparisons in Fig. 7 failed for murine organoids, where the paper does not give the burst detection used and four of nine show no bursts under the stated settings. Minor rank-order claims could not be tested, as the paper gives two conflicting normalisations.

## End of run

19 turns, 2 minutes, $1.17 at API prices, result: success.
