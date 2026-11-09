# 001933 · recorder · run 38838861411

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001933 --write; git diff; ls transcripts/001933/ claims/001933/; cat attempts/001933-chen-2026-02.yaml
```

```
<persisted-output>
Output too large (50.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/377488e5-0a1f-4c47-bd5c-898e61cf434d/tool-results/bk6plybiw.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 2b0abbb..44444a0 100644
--- a/README.md
+++ b/README.md
@@ -61,7 +61,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000130](https://dandiarchive.org/dandiset/000130) | [Sohn et al. 2019](https://doi.org/10.1016/j.neuron.2019.06.012) | 9 | 4 | 7 | 3 | [`000130-sohn-2019`](entries/000130-sohn-2019) |
 | [001616](https://dandiarchive.org/dandiset/001616) | [Gerken et al. 2025](https://doi.org/10.7554/elife.106758.1) | 6 | 5 | 0 | 9 | [`001616-gerken-2025`](entries/001616-gerken-2025) |
 | [002014](https://dandiarchive.org/dandiset/002014) | [Choi et al. 2025](https://doi.org/10.1016/j.jneumeth.2025.110467) | 4 | 1 | 0 | 8 | [`002014-choi-2025`](entries/002014-choi-2025) |
-| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 8 | [`001933-chen-2026`](entries/001933-chen-2026) |
+| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
 | [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
 | [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
 | [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
git diff --stat; head -20 README.md | tail -15; grep -n "^| Dandiset\|^|---" README.md | head; ls attempts | grep 001933; git log --oneline -3 -- README.md
```

```
README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://catalystneuro.github.io/reproduction-registry/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
with the methods available to it. **A "not reproduced" or "partially
reproduced" outcome is not a finding that the paper is wrong.** It can come
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
001933-chen-2026-01.yaml
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^##" docs/pilot-notes.md; wc -l docs/pilot-notes.md
```

```
6:## 000582, Sargolini et al. 2006 (2026-10-13)
11:### What happened
25:### Lessons
62:### Findings about the dandiset
73:### Cost
79:## 000127, Chowdhury, Glaser & Miller 2020 (2026-10-13)
84:### What happened
101:### Lessons
136:### Findings about the dandiset
153:### Cost
159:## 000207, Zheng et al. 2022 (2026-10-13): first attempt by an agent following the protocol
203:### Verification (resumed 2026-10-13)
225:### Lessons from the verification
254:### Cost
259:## 000147, Guan et al. 2022 (2026-10-13): second attempt by an agent following the protocol
271:### What the author reported about the protocol
308:### Findings about the dandiset
318:### Verification, in GitHub Actions
339:### Lessons from running in Actions
356:### Cost
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 863
}
```

```
863	### 001754 again, on the fixed draft (2026-10-15)
864	
865	The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
866	The conversion was redone (`mcnaughton2000-to-nwb` at commit `7346882`) and
867	the draft re-uploaded on 2026-10-14, and the attempt pins `draft`. Three
868	claims reproduced, one not reproduced and three blocked, against two, two
869	and three before; both rounds agreed with every outcome and nothing was
870	proposed, so there was no third round.
871	
872	The one change of outcome, `fd4-abnormal-selectivity` from not reproduced to
873	reproduced (one-sided p 0.024 against 0.055), comes from the data, not the
874	analysis: the draft drops every copy of each group of identical rate maps,
875	which removes three near-empty Rat2 maps the first attempt counted, and a
876	notebook cell runs the same test on the earlier maps to show it. Dropping
877	every copy instead of keeping one also removed six maps from the dandiset.
878	`flight-spatial-code` stays not reproduced (Rat1 10 of 25 significant on
879	flight day 9, Rat2 2 of 28); the rounds added tests of the shuffle null on
880	real spike trains cut off from position, which give fewer false positives
881	than the 0.05 the test assumes, and the record now calls a low fraction weak
882	evidence against a spatial code, since the test's power is unmeasured.
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001933-chen-2026-02.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
import sys
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001933' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (221.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/377488e5-0a1f-4c47-bd5c-898e61cf434d/tool-results/blz1dhh5p.txt

Preview (first 2KB):
schema_version: 1
id: 001933-chen-2026-02
dandiset: "001933"
dandiset_version: 0.260825.1457
paper: doi:10.1038/s41467-026-75194-3
date: 2026-10-15
entry: 001933-chen-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 21 more lines not kept]
```

**Agent**

Row written (6 / 2 / 1 (+1) / 0, replacing the earlier attempt's row). Now reading the attempt record.

**Agent calls Bash**

```bash
cd attempts; wc -l 001933-chen-2026-02.yaml; grep -n "^[a-z_]*:" 001933-chen-2026-02.yaml; grep -n "outcome:\|  - id:\|^- id:\|claim:" 001933-chen-2026-02.yaml | head -80
```

```
712 001933-chen-2026-02.yaml
1:schema_version: 1
2:id: 001933-chen-2026-02
3:dandiset: "001933"
4:dandiset_version: 0.260825.1457
5:paper: doi:10.1038/s41467-026-75194-3
6:date: 2026-10-15
7:entry: 001933-chen-2026
8:provenance:
16:inputs:
42:outcomes:
329:findings:
427:verifications:
43:- claim: source-data-link
44:  outcome: not_reproduced
46:  output: claim:source-data-link
72:- claim: fig6e-anxa1-evoked-reduced
73:  outcome: reproduced
75:  output: claim:fig6e-anxa1-evoked-reduced
88:- claim: fig6e-anxa1-evoked-per-mouse
[... 73 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001933-chen-2026-02.yaml",
 "offset": 16,
 "limit": 420
}
```

```
16	inputs:
17	- what: The paper's source data file (Source data.xlsx, md5 c26fe3de8f340a3db5fa29a40e5a8c10). In source-data-link, the
18	    triggered traces, evoked integrals and spontaneous transient values of Figure 6 and Supplementary Figures 7 and 8,
19	    as reference values. For the claims of Figures 1, 2, 4 and 5, the per-section, per-area and per-blot values the
20	    tests run on.
21	  source: Zenodo, doi:10.5281/zenodo.19930567
22	- what: The paper's Supplementary data (Supplementary files.zip, md5 98f11f6ea1fdd13e56807ff1f639c9a4), for the volcano
23	    table of Figure 2B and to check that the PRIDE peptide table equals Supplementary data 1; and the proteomics R code
24	    (analysis code.zip), read, not run.
25	  source: Zenodo, doi:10.5281/zenodo.19930567
26	- what: The peptide groups table of the synaptosome phosphoproteomics
27	    (020623-Loukia-mouse-synaptosome-phos-quant_phosphopeptides.xlsx, md5 1ceefa5fc576c1991f07f7d637f83fae).
28	  source: PRIDE PXD065006
29	- what: The RAB3A and p-RAB3A pulldown intensities (FilteredDataset.pg_matrix.Brain_Rab3A.csv, md5
30	    cd060787ee1d324f77d151ef0c1e54f1), the DIA-NN report (report.pg_matrix.tsv, md5 454a9e2c72ed558533d74caae09b4579),
31	    the SDRF (md5 ef4a075a02271a9417f0539348639750) and the deposited limma table
32	    (Brain_Rab3A.DifferentialAbundance_volcano.csv, md5 ee6cd6c85e025bbc28d0c0d22beb7f45).
33	  source: PRIDE PXD065125
34	- what: The 168 synaptosome images of Figure 4D and 4E (1.07 GB, streamed and measured), and the file lists of the
35	    image studies of Figures 1 and 5 (S-BIAD2070, S-BIAD2071, S-BIAD2072), matched to the source data by file name.
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001933-chen-2026-02.yaml",
 "offset": 427,
 "limit": 290
}
```

```
427	verifications:
428	- date: 2026-10-15
429	  kind: agent
430	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
431	  reviewed: The executed notebook of the first run with the conclusion cells and the summary removed, the helper
432	    modules and the claims file, with the paper. The verifier tested double_threshold, evoked_integrals, cohens_d,
433	    twoway_anova and sidak_within on synthetic inputs, checked the column labels of the Figure 1D sheet and the OME
434	    metadata of one synaptosome image. Report in transcripts/001933/verifier-1-report.md.
435	  results:
436	  - claim: source-data-link
437	    agrees: true
438	    outcome: not_reproduced
439	    reason: 'Cell 24: mice match 100%, traces 60.9% and evoked integrals 60.9%, because Calb1 S8D/S8E is 0/384 for
440	      both. Spontaneous integrals match 0% under either window, so part 4 is below 50% and the claim fails. Fig 6E
441	      matches the 0.5 mW labels (120/120) and not the 4 mW labels (0/120). It found that the Calb1 dF/F is not the
442	      trace behind Supplementary Fig. 8 (problem 1), that the scaled spontaneous values equal about 0.005 times the
443	      mean dF/F of each transient, not the trapezoid integral the criterion prescribes (problem 2), and that the 6E
444	      records are assigned power 0.5 by the loader, confirmed only indirectly (problem 9). It asked for an output that
445	      fits candidate scalings at 1e-4, and for the deposited Calb1 processing parameters or a raw-to-dF/F
446	      recomputation that matches even one S8D trace.'
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; grep -n "kind\|^  - id\|^- id\|where" claims/001933/*.yaml | head -60; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('001933'==str(v) for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
wc -w transcripts/001933/*-report.md
```

```
9:# another public archive is `data: elsewhere`, names the archive under `where`, and is tested;
10:# data_missing now means public nowhere. These eight claims now carry `data`, `where` and a
65:- id: source-data-link
82:    computed here, up to the same kind of common factor, under either the Methods' exclusion
87:- id: fig6e-anxa1-evoked-reduced
104:- id: fig6e-anxa1-evoked-per-mouse
122:- id: supp7c-anxa1-evoked-all-powers
130:- id: fig6f-anxa1-spontaneous-reduced
147:- id: fig6f-anxa1-spontaneous-per-mouse
162:- id: supp8c-calb1-spontaneous-not-reduced
178:- id: supp8e-calb1-evoked-reduced
194:- id: supp8e-calb1-few-mice-reduced
210:- id: cohens-d-anxa1-larger
228:- id: fig1d-lrrk2-enriched-vulnerable
232:  data: elsewhere
233:  where: BioImage Archive S-BIAD2070 (images); Zenodo doi:10.5281/zenodo.19930567 (per-section
245:- id: fig2b-rab3-phosphorylation
249:  data: elsewhere
250:  where: PRIDE PXD065006
265:- id: fig2eg-prab3-increased
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/001933/author-report.md transcripts/001933/author-revise-1-report.md transcripts/001933/author-revise-2-report.md
```

```
I've finished attempt `001933-chen-2026-02`. The entry runs from a clean environment in about 8 minutes, and the handover is built in `executed/001933-chen-2026/handover/`. Nothing is committed. `tools/entry.py check` still reports 8 errors, all in the earlier record `001933-chen-2026-01.yaml`, which I left as it is (point 4 below).

**What pilot-7 changed.** It adds a claim kind, `data: elsewhere`, for data the paper put in another public archive, and `data_missing` now means public nowhere. The eight Figure 1 to 5 claims were blocked as `data_missing` in -01. They now carry `data: elsewhere`, a `where:` and criteria, and are tested on Zenodo, PRIDE and BioImage Archive data, counted apart from the dandiset's claims. The ten photometry claims are unchanged. Version 0.260825.1457 is still the draft's content, so the helper constant, `entry.yaml`'s `dandi:` relation and the notebook header keep that version.

**1. Outcomes (this attempt, with -01's in brackets)**

| Claim | Outcome (-01) |
|---|---|
| source-data-link | not reproduced (not reproduced) |
| fig6e-anxa1-evoked-reduced | reproduced (reproduced) |
| fig6e-anxa1-evoked-per-mouse | reproduced (reproduced) |
| supp7c-anxa1-evoked-all-powers | reproduced (reproduced) |
| fig6f-anxa1-spontaneous-reduced | reproduced (reproduced) |
| fig6f-anxa1-spontaneous-per-mouse | partially reproduced (partially reproduced) |
| supp8c-calb1-spontaneous-not-reduced | reproduced (reproduced) |
| supp8e-calb1-evoked-reduced | reproduced (reproduced) |
| supp8e-calb1-few-mice-reduced | partially reproduced (partially reproduced) |
| cohens-d-anxa1-larger | not reproduced (not reproduced) |
| fig1d-lrrk2-enriched-vulnerable | reproduced (blocked, data_missing) |
| fig2b-rab3-phosphorylation | not reproduced (blocked, data_missing) |
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cat transcripts/001933/verifier-1-report.md transcripts/001933/verifier-2-report.md
```

```
**A. Outcomes** (18 claims, taken from the claims file; there are no author outcome cells to compare against)

| Claim | Outcome | Reason |
|---|---|---|
| source-data-link | not_reproduced | Cell 24: mice match 100%. Traces match 60.9% and evoked integrals 60.9%, because Calb1 S8D/S8E is 0/384 for both. Spontaneous integrals match 0% under either window. Part 4 is below 50%, so the claim fails. Fig 6E matches the 0.5 mW labels (120/120) and not the 4 mW labels (0/120). |
| fig6e-anxa1-evoked-reduced | reproduced | Cell 32: 64 vs 56 stimulations, GS 48.8 vs WT 128, one-tailed p = 1.16e-22 (paper 1.10e-20). The code window gives 1.1e-20 exactly. |
| fig6e-anxa1-evoked-per-mouse | reproduced | Cell 34: 7 of 8 significant under all four readings, and 3743 is the exception. |
| supp7c-anxa1-evoked-all-powers | reproduced | Cell 36: G2019S is lower at all 4 powers (p from 3.1e-15 to 1.2e-22). Code-window p-values equal the paper's at 0.1, 0.5 and 1 mW. |
| fig6f-anxa1-spontaneous-reduced | reproduced | Cell 40: counts are exactly 1064 and 798, and per-mouse counts run 57 to 285. One-tailed p = 4.85e-72 (paper 2.75e-177; the per-transient-mean variant gives 2.2e-177). |
| fig6f-anxa1-spontaneous-per-mouse | partially_reproduced | Cell 42: 5 of 8 under every reading, with 3743, 4651 and 4652 not significant. The per-transient-mean variant under Student one-tailed gives the paper's 6, with exactly 3743 and 4651 as the exceptions. |
| supp8c-calb1-spontaneous-not-reduced | reproduced | Cell 44: p = 0.0509, which is ≥ 0.05. Counts are 896 and 635, both within tolerance. The margin is very thin and the Calb1 signal is not the paper's (problems 1 and 6). |
| supp8e-calb1-evoked-reduced | reproduced | Cell 46: 56 vs 40 stimulations, G2019S lower at all 4 powers (p from 6.3e-10 to 4.4e-07). |
| supp8e-calb1-few-mice-reduced | partially_reproduced | Cell 48: at 0.5 mW the readings give 7, 6, 4 and 4. The best reading is 4, which the criterion counts as partial. Two of 7 appears on
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)

The second attempt, made because pilot-7 changed the protocol; the dandiset
(0.260825.1457), the paper's code and the paper are unchanged. Six claims
reproduced, two partially and one not reproduced on the dandiset, plus the
link claim using the paper's source data, not reproduced, and eight claims
on data in other archives, of which four reproduced, three partially and
one not reproduced; before, the dandiset's counts were the same and the
eight were blocked. Round 1 disagreed on one outcome,
`fig3d-rim-binds-unphosphorylated`, which the author had decided with an
imputation the criterion lists as a variant, because RILPL2 is found only
in the p-RAB3A pulldowns and the paired test has no pairs for it; the
author changed it to partially reproduced (3 of 4), round 2 agreed with all
18 outcomes and nothing was proposed, so there was no third round. The
paper reports that LRRK2 G2019S impairs the release sites of dopamine axons
vulnerable in Parkinson's disease. The ten photometry claims of Figure 6 and
Supplementary Figures 7 and 8 were tested on the dandiset as before, and the
eight claims of Figures 1 to 5 on Zenodo, PRIDE and BioImage Archive data,
starting from the deposited per-section and per-blot values, since the
Imaris analyses and the blot quantification cannot be rerun. Two outcomes
rest on weak ground: `supp8c-calb1-spontaneous-not-reduced` has p = 0.0509
and would be below 0.05 in 59 of 121 nearby exclusion windows, and part B
of `fig4d-fewer-active-zones` fails on a re-implementation of the FIJI
analysis that keeps a median of 183 VAMP2 particles per image against the
legend's about 1000.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
None of the earlier findings is fixed. The most consequential is still that
the Calb1 dF/F is not the trace behind Supplementary Figure 8 (0 of 384
published traces match, and recomputing dF/F from the raw signal with the
published code gives the dandiset's series, not the paper's), so the Calb1
claims are results on the dandiset's processing. The finding that Figures 1
to 5 are not in the dandiset is now that the dandiset's description and
related resources do not name the deposits that hold them. The published
spontaneous values are now known exactly: 0.005 times the trapezoid
integral divided by the number of samples in the transient, to 2.2e-15 in
every Anxa1 mouse, where the Methods give the integral. The new findings
concern the other archives. In PRIDE PXD065006 the RAB3 T86 phosphopeptide
is higher in the samples labelled MLi-2, and the paper's volcano table
holds MLi-2 minus vehicle (to within 1.6e-06 up to a constant) while the
Figure 2B legend reads a positive difference as higher with vehicle, so
either the labels or the figure's direction is swapped; with swapped labels
`fig2b-rab3-phosphorylation` would reproduce. That table gives 254
phosphopeptides at the legend's thresholds where the text gives 289; the
Figure 3 counts of 69 and 16 are those at adjusted p < 0.05; the Figure 1D
p = 0.0008 matches a paired test or a test of mouse means, not the legend's
test (4.65e-06); one WT section appears twice in the Figure 5D and 5E source
data, and counted once one comparison moves from p = 0.0344 to 0.058;
counts in the source data and legends differ (51 G2019S areas against 57 in
Figure 4E); the G2019S animals of Figures 5G, 5H and 5J are not identified
in the source data; the image studies hold images the figures do not use
without saying which were used; and three synaptosome images give 488 nm
for all channels in their OME metadata.

`tools/entry.py all` stopped at its check in every run, on 8 errors in the
earlier record `001933-chen-2026-01.yaml`, whose blocks with `data_missing`
fail the pilot-7 rule; the record was left unchanged and the notebook run
with `entry.py run`. The author's points on the protocol: the check applies
the current claims file to every attempt of an entry, with no exemption by
protocol version; one claims file serves both attempts, so updating it
changes the claims the earlier attempt points to; the rules for a repeat
attempt assume a changed dandiset and have none for an earlier finding
whose kind a new protocol makes invalid; findings are defined as about the
dandiset, and the schema has no field for the archive a finding concerns;
and the criteria for the eight new claims were written after seeing the
deposited values, though before any statistic, and for `fig2b` the
criterion did not fix the normalisation that decided the outcome.
EOF
git diff --stat
```

```
README.md           |  2 +-
 docs/pilot-notes.md | 68 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 69 insertions(+), 1 deletion(-)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "paper reports that LRRK2 G2019S impairs the release sites of dopamine axons\nvulnerable in Parkinson's disease.",
 "new_string": "paper reports that LRRK2 impairs the release sites of dopamine axons\nvulnerable in Parkinson's disease, in G2019S mice."
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I ran `python tools/readme_row.py 001933 --write`. The README already had a row for 001933 from attempt -01, and the script replaced it: the counts are now 6 / 2 / 1 (+1) / 0, where the old row had 8 blocked. I added the subsection below at the end of `docs/pilot-notes.md` and committed nothing.

Every run of `tools/entry.py all` stopped at its check, on 8 errors in the earlier record `001933-chen-2026-01.yaml`. That record was left unchanged, so the workflow's check will likely fail the same way until someone exempts old records or changes the rule.

### 001933 again, Chen et al. 2026, under pilot-7 (2026-10-15)

The second attempt, made because pilot-7 changed the protocol; the dandiset
(0.260825.1457), the paper's code and the paper are unchanged. Six claims
reproduced, two partially and one not reproduced on the dandiset, plus the
link claim using the paper's source data, not reproduced, and eight claims
on data in other archives, of which four reproduced, three partially and
one not reproduced; before, the dandiset's counts were the same and the
eight were blocked. Round 1 disagreed on one outcome,
`fig3d-rim-binds-unphosphorylated`, which the author had decided with an
imputation the criterion lists as a variant, because RILPL2 is found only
in the p-RAB3A pulldowns and the paired test has no pairs for it; the
author changed it to partially reproduced (3 of 4), round 2 agreed with all
18 outcomes and nothing was proposed, so there was no third round. The
paper reports that LRRK2 impairs the release sites of dopamine axons
vulnerable in Parkinson's disease, in G2019S mice. The ten photometry claims of Figure 6 and
Supplementary Figures 7 and 8 were tested on the dandiset as before, and the
eight claims of Figures 1 to 5 on Zenodo, PRIDE and BioImage Archive data,
starting from the deposited per-section and per-blot values, since the
Imaris analyses and the blot quantification cannot be rerun. Two outcomes
rest on weak ground: `supp8c-calb1-spontaneous-not-reduced` has p = 0.0509
and would be below 0.05 in 59 of 121 nearby exclusion windows, and part B
of `fig4d-fewer-active-zones` fails on a re-implementation of the FIJI
analysis that keeps a median of 183 VAMP2 particles per image against the
legend's about 1000.

The dandiset was converted by CatalystNeuro (catalystneuro/dombeck-lab-to-nwb).
None of the earlier findings is fixed. The most consequential is still that
the Calb1 dF/F is not the trace behind Supplementary Figure 8 (0 of 384
published traces match, and recomputing dF/F from the raw signal with the
published code gives the dandiset's series, not the paper's), so the Calb1
claims are results on the dandiset's processing. The finding that Figures 1
to 5 are not in the dandiset is now that the dandiset's description and
related resources do not name the deposits that hold them. The published
spontaneous values are now known exactly: 0.005 times the trapezoid
integral divided by the number of samples in the transient, to 2.2e-15 in
every Anxa1 mouse, where the Methods give the integral. The new findings
concern the other archives. In PRIDE PXD065006 the RAB3 T86 phosphopeptide
is higher in the samples labelled MLi-2, and the paper's volcano table
holds MLi-2 minus vehicle (to within 1.6e-06 up to a constant) while the
Figure 2B legend reads a positive difference as higher with vehicle, so
either the labels or the figure's direction is swapped; with swapped labels
`fig2b-rab3-phosphorylation` would reproduce. That table gives 254
phosphopeptides at the legend's thresholds where the text gives 289; the
Figure 3 counts of 69 and 16 are those at adjusted p < 0.05; the Figure 1D
p = 0.0008 matches a paired test or a test of mouse means, not the legend's
test (4.65e-06); one WT section appears twice in the Figure 5D and 5E source
data, and counted once one comparison moves from p = 0.0344 to 0.058;
counts in the source data and legends differ (51 G2019S areas against 57 in
Figure 4E); the G2019S animals of Figures 5G, 5H and 5J are not identified
in the source data; the image studies hold images the figures do not use
without saying which were used; and three synaptosome images give 488 nm
for all channels in their OME metadata.

`tools/entry.py all` stopped at its check in every run, on 8 errors in the
earlier record `001933-chen-2026-01.yaml`, whose blocks with `data_missing`
fail the pilot-7 rule; the record was left unchanged and the notebook run
with `entry.py run`. The author's points on the protocol: the check applies
the current claims file to every attempt of an entry, with no exemption by
protocol version; one claims file serves both attempts, so updating it
changes the claims the earlier attempt points to; the rules for a repeat
attempt assume a changed dandiset and have none for an earlier finding
whose kind a new protocol makes invalid; findings are defined as about the
dandiset, and the schema has no field for the archive a finding concerns;
and the criteria for the eight new claims were written after seeing the
deposited values, though before any statistic, and for `fig2b` the
criterion did not fix the normalisation that decided the outcome.

## End of run

14 turns, 1 minutes, result: success.
