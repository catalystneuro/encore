# 001528 · recorder · run 39174358498

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001528 --write; git diff; ls transcripts/001528/ claims/001528/; cat attempts/001528-hadjas-2025-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (40.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/649b1e47-6fd0-4385-b3b5-73f31c82c9d8/tool-results/b7t0vl03p.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index e419374..a63b0f4 100644
--- a/README.md
+++ b/README.md
@@ -95,6 +95,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001084](https://dandiarchive.org/dandiset/001084) | [Vu et al. 2024](https://doi.org/10.1016/j.neuron.2023.12.011) | 10 (+1) | 10 | 0 | 1 | [`001084-vu-2024`](entries/001084-vu-2024) |
 | [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
 | [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
+| [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001528/:
10.1101-2025.06.03.657460.yaml

transcripts/001528/:
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 '| Dandiset' README.md | head; cat attempts/001528-hadjas-2025-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "import json;d=json.load(open('targets/dandisets.json'));print([x for x in (d if isinstance(d,list) else d.values()) if '001528' in json.dumps(x)])"
```

```
<persisted-output>
Output too large (192.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/649b1e47-6fd0-4385-b3b5-73f31c82c9d8/tool-results/bnbmosnzf.txt

Preview (first 2KB):
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
schema_version: 1
id: 001528-hadjas-2025-01
dandiset: "001528"
dandiset_version: draft
paper: doi:10.1101/2025.06.03.657460
date: 2026-10-18
entry: 001528-hadjas-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/001528/author-report.md"
}
```

```
1	I did steps 1 to 5 of the protocol and ran the handover (step 6). The entry checks with 0 errors and the notebook runs from a clean environment in 290 s. Nothing is committed. I used the preprint's full text (bioRxiv v1, CC BY), saved under `paper/`.
2	
3	**1. Outcome per claim** (25 claims; counts taken from the attempt record)
4	
5	| Claim | Outcome |
6	|---|---|
7	| cohort-sizes | not reproduced (10 of 16 group counts match) |
8	| fig2-gaba-excited | reproduced (t = 3.86 and 9.19; paper 3.8 and 9.2) |
9	| fig2-gaba-frequency | reproduced (Friedman 21.00 and 18.15) |
10	| fig3b-da-stn-250ms-peak | partially reproduced (0.786 s in the window I fixed beforehand; a narrower window gives the paper's 0.492 ± 0.033 s) |
11	| fig3c-da-stn-duration | reproduced (12.93, p = 0.0048; paper 13.0, p = 0.005) |
12	| fig3d-da-stn-frequency-ns | reproduced (4.20, p = 0.24, as in the paper) |
13	| fig3g-da-ppn-duration | not reproduced (p ≥ 0.25 under every reading) |
14	| fig3h-da-ppn-frequency-ns | reproduced (F = 1.35, p = 0.29) |
15	| fig4cf-ts-dls-opposite | reproduced (F = 40.9 and 36.4, the paper's values) |
16	| fig4dg-ts-frequency | reproduced (6 of 6 tests) |
17	| fig4eh-dls-frequency | reproduced (6 of 6 tests) |
18	| fig4eh-dls-5hz-increase | not reproduced |
19	| fig4cf-dls-rebound | partially reproduced |
20	| figs3-terminals-opposite | reproduced |
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001528; for f in verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
for x in (it if isinstance(it,list) else it.values()):
    if '001528' in json.dumps(x): print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (192.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/649b1e47-6fd0-4385-b3b5-73f31c82c9d8/tool-results/b7y4pt3c8.txt

Preview (first 2KB):
=== verifier-1-report.md
**A. Outcomes**

The claims file has 25 claims. The notebook tests 21 and treats the 4 human-tissue claims as blocked. My tally: 12 reproduced, 5 partially reproduced, 4 not reproduced, 4 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| cohort-sizes | not_reproduced | 10 of 16 counts match (cell 21); the criterion needs 12 to reproduce. The Anxa1 counts match 4 of 4 only if the unsuffixed recordings are taken as DLS, which is a variant. Even with the Vglut2 STN count explained (B4), the total stays below 12. |
| fig2-gaba-excited | reproduced | 1 s trains: STN t 3.86, p 0.0083; PPN t 9.19, p 3.7e-5 (cell 23). These match the paper's t 3.8 and 9.2. |
| fig2-gaba-frequency | reproduced | Friedman STN 21.00, p 0.00011; PPN 18.15, p 0.00041. 40 Hz is above 5 Hz in every mouse (cell 25). |
| fig3b-da-stn-250ms-peak | partially_reproduced | With the 0 to 2.25 s window the mean latency is 0.786 ± 0.204 s, outside 0.50 ± 0.03. The peak is after offset and the net response is positive (p 0.0083). The 0 to 1.25 s variant gives 0.492 ± 0.033, which matches the paper (cell 27). |
| fig3c-da-stn-duration | reproduced | Reading (a) p 0.0011; reading (b) chi2 12.93, p 0.0048, matching the paper's F 13.0, p 0.005. In 4 s trains, 0 to 0.5 s is above 3 to 4 s (p 0.00071, 11 of 11 mice) (cell 29). |
| fig3d-da-stn-frequency-ns | reproduced | Friedman chi2 4.20, p 0.24, the paper's exact values (cell 31). |
| fig3g-da-ppn-duration | not_reproduced | Readings (a), (b) and (c) give p 0.26, 0.25 and 0.46 (cell 33). The paper's F 11.5 with p 0.009 implies 3 df, which is reading (b), and that reading gives chi2 4.07. |
| fig3h-da-ppn-frequency-ns | reproduced | Greenhouse-Geisser RM ANOVA: F 1.35, df 1.85 and 14.8, p 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001528; wc -c *-report.md; cat verifier-1-report.md | sed -n '15,200p'
```

```
6837 author-report.md
 3527 author-revise-1-report.md
 2337 author-revise-2-report.md
 9389 verifier-1-report.md
 5595 verifier-2-report.md
27685 total
| fig4cf-ts-dls-opposite | reproduced | The signs are as stated (TS 6/6 and 9/9 mice above 0, DLS 7/7 and 9/9 below 0). Interaction F 40.9 (STN) and 36.4 (PPN), p < 1e-4, equal to the paper (cell 37). |
| fig4dg-ts-frequency | reproduced | 6 of 6 tests hold, with statistics close to the paper (7.62/7.5, 13.76/13.6, 17.31/16.9, 19.8/20.0, 24.3/24.0, 23.3/23.2) (cell 39). |
| fig4eh-dls-frequency | reproduced | 6 of 6 tests hold, with 40 Hz below 5 Hz in each (cell 41). |
| fig4eh-dls-5hz-increase | not_reproduced | 1 s trains at 5 Hz: STN p 0.22, PPN p 0.13 (cell 43). The paper also cites the 4 s panels S3F and S3L. There the variant gives STN p 0.0006 but PPN p 0.07, so that reading would give partially_reproduced (B2). |
| fig4cf-dls-rebound | partially_reproduced | 1 s trains, 1 s after offset: PPN mean 4.53%, p 0.017; STN mean 0.87%, p 0.29 (cell 45). |
| figs3-terminals-opposite | reproduced | TS +8.96% (9 of 9 mice), DLS −4.41% (7 of 8), interaction p 0.00013 (cell 47). |
| fig5-vglut2-excited | reproduced | 4 of 4 tests show a significant increase. STN W 43 (p 0.0078) at 0.25 s and 1 s; PPN t 2.89 and 3.42 (cell 49). The 4 s results also match (W −5, p 0.82; t 2.56, p 0.03). |
| fig5-vglut2-frequency | reproduced | The 4 core tests hold: STN 0.25 s p 0.0036; PPN p 0.011, 0.0005, 0.001. STN 1 s and 4 s are not significant, as in the paper (cell 51). |
| fig5-anxa1-dls-inhibited | not_reproduced | 2 of 6 significant with the DLS labels, n 5 and 4 (cell 53). Every mouse decreases except one in PPN 4 s, so the failure comes from sample size (B3). The unsuffixed-as-DLS variant gives 6 of 6. |
| fig5-anxa1-dls-frequency | partially_reproduced | 5 of 6 tests hold with the DLS labels; PPN 4 s RM ANOVA p 0.24 at n 4 (cell 55). |
| fig5-anxa1-dls-rebound | partially_reproduced | STN p 0.0044 (5 of 5 mice above 0); PPN p 
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001528; cat author-revise-1-report.md; echo ====; cat verifier-2-report.md; echo ====; cat author-revise-2-report.md
```

```
No outcomes changed in round 1. The verifier agreed with 24 of 25. Where it disagreed, I kept my outcome and recorded the disagreement in the attempt record. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passed in about 5.5 minutes), and every conclusion was rewritten against the new output.

**The one disagreement: `fig5-anxa1-dls-inhibited`.** The verifier would call it not_reproduced; I kept it as blocked, data missing. Its own reasoning supports the block:
- With the 5 and 4 mice in the dandiset, the Wilcoxon tests the paper uses for three of the six conditions cannot reach p < 0.05.
- The paper's own statistics show it analysed 8 and 10 mice.

That is a block decided once the selection is made (protocol step 1.8). The notebook now prints these numbers and states that the DLS recordings of nine of the paper's mice are not in the dandiset.

**Added to the notebook, one per point in the report:**
- **1 s trains (B1):** the window before the train is the baseline window, so it is always 0. The notebook now prints this and says what follows: paired tests on 1 s trains are tests against 0, and in the two-way ANOVAs the site F equals the interaction F.
- **5 Hz increase in DLS (B2):** I confirmed in the paper that Figure S3F and S3L are the 4 s DLS panels. Each train duration is now labelled with its panel. The 4 s reading holds for 1 of 2 inputs, and the notes record that it would give partially reproduced. The outcome stays on the 1 s trains of Figure 4E and 4H, which the criterion fixed and the same sentence also cites.
- **Vglut2 STN mouse count (B4):** a new helper computes exact Wilcoxon p-values. It confirms the paper's W values fit 9 mice, not the legend's 10. I moved this from a data-missing finding to a paper-inconsistency finding. The count check stays not reproduced: 11 of 16 counts match with this explained, still below the 12 needed.
- **Vglut2 PPN frequency tests (B5):** the frequency tests now list the dropped mice. C341
[... 93 more lines not kept]
```

**Agent**

Round 2 agreed on all 25 outcomes. Next I'm reading the findings in the attempt record, the target entry, and the existing pilot notes.

**Agent calls Bash**

```bash
cd  grep -n -E '^[a-z_]+:' attempts/001528-hadjas-2025-01.yaml; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if str(x.get('dandiset',x.get('id','')))=='001528' or x.get('identifier')=='001528':
            print(json.dumps(x,indent=1)[:3000]); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
1:schema_version: 1
2:id: 001528-hadjas-2025-01
3:dandiset: "001528"
4:dandiset_version: draft
5:paper: doi:10.1101/2025.06.03.657460
6:date: 2026-10-18
7:entry: 001528-hadjas-2025
8:provenance:
16:outcomes:
273:inputs: []
274:findings:
350:verifications:
{
 "dandiset": "001528",
 "name": "Fiber photometry of SNc/SNr dopamine and GABA neuron responses to optogenetic STN and PPN stimulation in Parkinson's disease",
 "published_version": null,
 "asset_count": 290,
 "size_gb": 68.06,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001528-hadjas-2025-01.yaml",
 "offset": 274,
 "limit": 78
}
```

```
274	findings:
275	- kind: data_missing
276	  statement: For the Anxa1 mice the dandiset holds DLS terminal recordings for 5 (STN) and 4 (PPN)
277	    mice where the paper analyses 8 and 10. Nine mice (C5903, C5906, C5992, C6900, C6902, C7244,
278	    C7245, C7248, C7249) have only recordings labelled SNc, without a site suffix in the file
279	    name. Their signals resemble SNc recordings, and the paper's cell-body statistics are
280	    reproduced closely by the other nine mice's SNc recordings (p to two digits, t within 0.08),
281	    so the DLS recordings of these nine mice appear not to be deposited, and the nine SNc
282	    recordings were not used in the paper.
283	- kind: selection_undocumented
284	  statement: The dandiset includes Anxa1 SNc recordings from nine mice that the paper's cell-body
285	    analysis (n = 5 and 4) leaves out, and it does not say which recordings the paper used.
286	- kind: data_missing
287	  statement: The human RNAscope and immunofluorescence counts of Figure 1 and Figure S1 and the
288	    histology of Figure S2 are not in the dandiset, and the preprint has no data availability
289	    statement.
290	- kind: data_missing
291	  statement: DA terminals in DLS have 8 mice where Figure S3 gives 9.
292	- kind: paper_inconsistency
293	  statement: The Figure 5 legend gives 10 mice for Vglut2+ neurons with STN stimulation, while the
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  n=$(grep -n '^### ' docs/pilot-notes.md | tail -5 | head -1 | cut -d: -f1); tail -n +$n docs/pilot-notes.md
```

```
<persisted-output>
Output too large (34KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/649b1e47-6fd0-4385-b3b5-73f31c82c9d8/tool-results/b8gfloqmc.txt

Preview (first 2KB):
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
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '^### ' docs/pilot-notes.md | tail -5; n=$(grep -n '^### ' docs/pilot-notes.md | tail -2 | head -1 | cut -d: -f1); tail -n +$n docs/pilot-notes.md
```

```
3233:### 001038, Azcorra et al. 2023
3328:### 001075, Randi et al. 2023
3423:### 001084, Vu et al. 2024
3523:### 001170, Ling et al. 2023
3633:### 001172, Lohani et al. 2022
### 001170, Ling et al. 2023

Two claims reproduced, four partially, four not reproduced and three blocked
on the dandiset. With outside data, counted apart: one reproduced. Five claims
on the locust recordings in the paper's Figshare record: three reproduced and
two partially reproduced. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 18 of the 19; it would
call `figs7e-ibi-chance` not reproduced, as the Methods' k = 50 classifier on
60 one-minute bins gives 3.8% and meets the criterion by construction while
k = 20 classifies the gaps between blocks at 73 to 95%. The author kept it
blocked as `methods_underspecified` under the chance-level rule, since that
procedure's own null averages 10.8% against the paper's 25%, and round 2
accepted this. Round 2 agreed with all 19 and nothing was proposed, so there
was no third round. The paper, a bioRxiv preprint later published in iScience
under a new title, compares mouse olfactory bulb glomeruli imaged with two
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/001528/*.yaml; grep -n -E '^\s*(- )?(id|statement):' claims/001528/*.yaml | cut -c1-220; sed -n '350,380p' attempts/001528-hadjas-2025-01.yaml
```

```
# Claims for Hadjas et al. (2025), bioRxiv preprint version 1, on dandiset 001528.
# Source: the full text of the preprint (CC BY), read from its JATS XML: Results, figure legends
# and Methods. The preprint has no data or code availability statement.
#
# When these criteria were written, the author had seen the data check only: the file list,
# the metadata of every file, the number of mice per group, input and recording site, the epoch
# tables, the units and timestamps of the 100 Hz series, a recomputation of the stored dF/F, and
# for the clock check the median absolute response to 1 s trains per group (at true and shifted
# onsets, without its sign). For the Anxa1 mice the author had also seen, per kind of recording
# (DLS, SNc, and the recordings without a site suffix), the median dF/F during and after 1 s
# trains (DLS -1.31 and +0.97, SNc -0.40 and +0.07, unsuffixed -0.27 and -0.06, in %, durations
# protocol). No claim's analysis had been run.
#
# Method choices fixed here, where the Methods leave them open:
# - The dF/F is the lab's own, stored in each file. Traces are aligned to train onset and the
#   mean over the 1 s before onset is subtracted (Methods). Trials of one condition are averaged
#   per mouse (Methods); statistics are across mice.
# - The response to a train is the mean dF/F during the train (Figure 3C legend). The
#   pre-stimulus comparison window has the length of the train and ends at onset; the rebound
#   window is the 1 s after offset. Windows of these lengths are among those the lab's MATLAB
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c 300 docs/pilot-notes.md | od -c | tail -3; cat >> docs/pilot-notes.md <<'EOF'

### 001528, Hadjas et al. 2025

Twelve claims reproduced, five partially, three not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 25; it would
call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
proposed, so there was no third round. The paper, a bioRxiv preprint, reports
that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
which are resilient in Parkinson's disease, while they inhibit dopamine release
in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
GABA and pan-DA responses to train duration and frequency, the opposite TS and
DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
terminal and cell-body responses were tested on the fiber photometry
recordings. The four human tissue claims are blocked as `data_missing`.
`cohort-sizes` is not reproduced (10 of 16 counts match, 11 with the Vglut2
STN count explained, against the 12 needed), `fig3g-da-ppn-duration` is not
reproduced (p 0.26, 0.25 and 0.46 under three readings, a Friedman 4.07 where
the paper gives F 11.5), and `fig4eh-dls-5hz-increase` is not reproduced on the
1 s trains its criterion fixed, while the 4 s panels the same sentence cites
would give partially reproduced. `fig3b-da-stn-250ms-peak` is partially
reproduced: the latency is 0.786 s in the window fixed beforehand, raised by
two mice with a slow rise past it, and a narrower window gives the paper's
0.492 ± 0.033 s. The author used the full text of preprint v1 and filled gaps
the Methods leave from the conversion repository's description of the lab's
MATLAB scripts, which are not public.

The dandiset was converted by CatalystNeuro (catalystneuro/hnasko-lab-to-nwb).
It has no published version, and the attempt used the draft as modified on
2026-09-01T15:27:47Z. For the Anxa1 mice it holds DLS terminal recordings for 5
(STN) and 4 (PPN) mice where the paper analyses 8 and 10. Nine mice have only
recordings labelled SNc, without a site suffix in the file name; their signals
resemble SNc recordings, and the paper's cell-body statistics are reproduced
closely by the other nine mice's SNc recordings (p to two digits, t within
0.08), so the DLS recordings of these nine mice appear not to be deposited, and
the dandiset does not say which SNc recordings the paper used. Every Anxa1 file
lists both an SNc and a DLS fiber, so the site rests on the name of the dF/F
series alone. Three Vglut2 PPN mice have no 5 Hz trains while the paper's
Friedman statistic of 24.8 needs at least 9 mice with all four frequencies, DA
terminals in DLS have 8 mice where Figure S3 gives 9, subject C4608 has no 4 s
trains, and the human counts and histology are not in the dandiset. The dF/F
series are stated in a.u. but hold percent, and a recomputation from the
stored signals agrees with a median correlation of 0.9999 (durations) and
0.9988 (frequencies). Other findings: every session start time carries the
offset -00:01, so the true offset is lost; the frequencies protocol's
description gives 10 s between trains where the epochs and the Methods give
20 s; the modulation frequencies are described inconsistently within the
files; thirteen mice have 10 trials per condition where the Methods state 5,
and 30 mice have 16 s trains the paper does not mention; eight subject ids are
lower case; the conversion code names a 5 mW block s1s10mW, and its Python dF/F
forces the fit through the origin while its description of the MATLAB scripts
includes an intercept; and in the paper the Figure 5 legend gives 10 Vglut2
STN mice where its Wilcoxon statistics are the exact values for 9, F1,11 =
12.8 is given for both STN and PPN with different p-values, two Friedman
entries do not fit their p-values, and the Figure 5 legend and the Results
disagree on the Anxa1 STN frequency effect.

The notebook ran in 290 s in the first clean run, about 5.5 minutes after
round 1 and 425 s after round 2. Loading first took about 10 minutes because
h5py serializes threads, and the author switched to a process pool; two bugs
found while preparing, timestamps stored in place of a sampling rate and
shifted onsets falling outside the recording, were fixed before the final run.
Round 2 found statements the outputs did not support, among them that
`fig5-anxa1-dls-inhibited` could not be tested by its criterion, where
partially reproduced was reachable and not reached (2 of 6), that the
cell-body statistics match exactly, and a runtime of five minutes, and these
were corrected. Untracked files in the repository root that the author did not
create were left alone. The author's points on the protocol: no published
version, where drafts are allowed only for repeat attempts; a 10% tolerance
that does not suit test statistics whose windows the paper does not state, nor
counts of animals; a block that depends on the selection where data are
missing, which the protocol would call `other`; site labels that the paper's
counts contradict and the signals support; a data check that ran into claim
territory; no recipe for a clock check on evoked photometry; a source
hierarchy that does not fit a conversion repository describing unpublished
analysis code; test choice after a Shapiro-Wilk test; and CatalystNeuro being
both the curator of the dandiset and the accountable party for the attempt.
EOF
git diff --stat
```

```
0000420   a   m   e   d       d   a   t   a       v   o   l   u   m   e
0000440       r   u   l   e   s       o   u   t   .  \n
0000454
 README.md           |  1 +
 docs/pilot-notes.md | 81 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 82 insertions(+)
```

**Agent**

I added the README row and appended the subsection to `docs/pilot-notes.md`. Nothing is committed.

The README row reads 12 reproduced, 5 partially, 3 not reproduced, 5 blocked. The author's first report gave different totals (12, 6, 3, 4), but its own per-claim table adds up to the README counts. The subsection uses the README figures and does not mention the old totals.

### 001528, Hadjas et al. 2025

Twelve claims reproduced, five partially, three not reproduced and five
blocked on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with 24 of the 25; it would
call `fig5-anxa1-dls-inhibited` not reproduced. The author kept it blocked as
`data_missing`, since at the deposited 5 and 4 mice three of its six Wilcoxon
tests cannot reach p < 0.05 and the paper's own W of -36 and -55 fix its n at
8 and 10, and round 2 accepted this. Round 2 agreed with all 25 and nothing was
proposed, so there was no third round. The paper, a bioRxiv preprint, reports
that STN and PPN inputs excite SNr GABA neurons and Vglut2+ dopamine neurons,
which are resilient in Parkinson's disease, while they inhibit dopamine release
in DLS and the DLS terminals of the vulnerable Anxa1+ neurons, and that
TH+/ANXA1+ neurons are reduced in human PD tissue. The group sizes, the SNr
GABA and pan-DA responses to train duration and frequency, the opposite TS and
DLS responses, the DLS rebound and 5 Hz increase, and the Vglut2 and Anxa1
terminal and cell-body responses were tested on the fiber photometry
recordings. The four human tissue claims are blocked as `data_missing`.
`cohort-sizes` is not reproduced (10 of 16 counts match, 11 with the Vglut2
STN count explained, against the 12 needed), `fig3g-da-ppn-duration` is not
reproduced (p 0.26, 0.25 and 0.46 under three readings, a Friedman 4.07 where
the paper gives F 11.5), and `fig4eh-dls-5hz-increase` is not reproduced on the
1 s trains its criterion fixed, while the 4 s panels the same sentence cites
would give partially reproduced. `fig3b-da-stn-250ms-peak` is partially
reproduced: the latency is 0.786 s in the window fixed beforehand, raised by
two mice with a slow rise past it, and a narrower window gives the paper's
0.492 ± 0.033 s. The author used the full text of preprint v1 and filled gaps
the Methods leave from the conversion repository's description of the lab's
MATLAB scripts, which are not public.

The dandiset was converted by CatalystNeuro (catalystneuro/hnasko-lab-to-nwb).
It has no published version, and the attempt used the draft as modified on
2026-09-01T15:27:47Z. For the Anxa1 mice it holds DLS terminal recordings for 5
(STN) and 4 (PPN) mice where the paper analyses 8 and 10. Nine mice have only
recordings labelled SNc, without a site suffix in the file name; their signals
resemble SNc recordings, and the paper's cell-body statistics are reproduced
closely by the other nine mice's SNc recordings (p to two digits, t within
0.08), so the DLS recordings of these nine mice appear not to be deposited, and
the dandiset does not say which SNc recordings the paper used. Every Anxa1 file
lists both an SNc and a DLS fiber, so the site rests on the name of the dF/F
series alone. Three Vglut2 PPN mice have no 5 Hz trains while the paper's
Friedman statistic of 24.8 needs at least 9 mice with all four frequencies, DA
terminals in DLS have 8 mice where Figure S3 gives 9, subject C4608 has no 4 s
trains, and the human counts and histology are not in the dandiset. The dF/F
series are stated in a.u. but hold percent, and a recomputation from the
stored signals agrees with a median correlation of 0.9999 (durations) and
0.9988 (frequencies). Other findings: every session start time carries the
offset -00:01, so the true offset is lost; the frequencies protocol's
description gives 10 s between trains where the epochs and the Methods give
20 s; the modulation frequencies are described inconsistently within the
files; thirteen mice have 10 trials per condition where the Methods state 5,
and 30 mice have 16 s trains the paper does not mention; eight subject ids are
lower case; the conversion code names a 5 mW block s1s10mW, and its Python dF/F
forces the fit through the origin while its description of the MATLAB scripts
includes an intercept; and in the paper the Figure 5 legend gives 10 Vglut2
STN mice where its Wilcoxon statistics are the exact values for 9, F1,11 =
12.8 is given for both STN and PPN with different p-values, two Friedman
entries do not fit their p-values, and the Figure 5 legend and the Results
disagree on the Anxa1 STN frequency effect.

The notebook ran in 290 s in the first clean run, about 5.5 minutes after
round 1 and 425 s after round 2. Loading first took about 10 minutes because
h5py serializes threads, and the author switched to a process pool; two bugs
found while preparing, timestamps stored in place of a sampling rate and
shifted onsets falling outside the recording, were fixed before the final run.
Round 2 found statements the outputs did not support, among them that
`fig5-anxa1-dls-inhibited` could not be tested by its criterion, where
partially reproduced was reachable and not reached (2 of 6), that the
cell-body statistics match exactly, and a runtime of five minutes, and these
were corrected. Untracked files in the repository root that the author did not
create were left alone. The author's points on the protocol: no published
version, where drafts are allowed only for repeat attempts; a 10% tolerance
that does not suit test statistics whose windows the paper does not state, nor
counts of animals; a block that depends on the selection where data are
missing, which the protocol would call `other`; site labels that the paper's
counts contradict and the signals support; a data check that ran into claim
territory; no recipe for a clock check on evoked photometry; a source
hierarchy that does not fit a conversion repository describing unpublished
analysis code; test choice after a Shapiro-Wilk test; and CatalystNeuro being
both the curator of the dandiset and the accountable party for the attempt.

## End of run

13 turns, 1 minutes, result: success.
