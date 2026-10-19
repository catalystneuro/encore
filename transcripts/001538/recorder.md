# 001538 · recorder · run 39185628546

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001538 --write; git diff; ls claims/001538 transcripts/001538; cat attempts/001538-zhai-2025-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (59.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7da5272c-faec-4353-b1c1-863c253995bf/tool-results/b8m7bpd8z.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index a63b0f4..eaf309e 100644
--- a/README.md
+++ b/README.md
@@ -96,6 +96,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
 | [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
 | [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
+| [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 (+1) | 0 (+2) | 3 (+1) | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001538:
10.1126-sciadv.adv8224.yaml

transcripts/001538:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; grep -n -A3 -B3 '"001538"' targets/dandisets.json; head -50 README.md | grep -n -i 'count\|(+'
```

```
M README.md
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
3233:### 001038, Azcorra et al. 2023
3328:### 001075, Randi et al. 2023
3423:### 001084, Vu et al. 2024
3523:### 001170, Ling et al. 2023
3633:### 001172, Lohani et al. 2022
3722:### 001528, Hadjas et al. 2025
3801 docs/pilot-notes.md
5474-   "catalystneuro": []
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7da5272c-faec-4353-b1c1-863c253995bf/tool-results/b8m7bpd8z.txt"
}
```

```
1	diff --git a/README.md b/README.md
2	index a63b0f4..eaf309e 100644
3	--- a/README.md
4	+++ b/README.md
5	@@ -96,6 +96,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
6	 | [001170](https://dandiarchive.org/dandiset/001170) | [Ling et al. 2023](https://doi.org/10.1101/2023.04.24.538157) | 2 (+1) | 4 | 4 | 3 | [`001170-ling-2023`](entries/001170-ling-2023) |
7	 | [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
8	 | [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
9	+| [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 (+1) | 0 (+2) | 3 (+1) | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
10	 
11	 Counts are of claims that rest on the dandiset, including those that take
12	 names for its own codes from elsewhere. Claims that also use data from
13	claims/001538:
14	10.1126-sciadv.adv8224.yaml
15	
16	transcripts/001538:
17	author-report.md
18	author-revise-1-report.md
19	author-revise-1.md
20	author-revise-2-report.md
[... 921 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7da5272c-faec-4353-b1c1-863c253995bf/tool-results/b8m7bpd8z.txt",
 "offset": 942
}
```

```
942	    outcome: reproduced
943	    reason: Agrees. The shared cells and low power are now stated. The same point on the metadata_error
944	      finding applies (7 of the 11 baseline cells in drug-named files were also recorded with the drug).
945	    response: See fig1f-dspn-sch-no-change; the finding is corrected.
946	  - claim: fig3f-ispn-dendritic-on-lower
947	    agrees: true
948	    outcome: reproduced
949	    reason: Agrees. Under the stricter basal-ratio rule (0.8 to 1.25) it would fail (P = 0.077, cell 63);
950	      the cell 64 conclusion states this. The claims file fixes the 0.5 to 2 rule, so the outcome stands
951	      under the criterion. The Summary mentions only this flip, which is incomplete.
952	    response: The conclusion, the notes and the Summary now state that the stricter rule changes this
953	      outcome and fig3f-ispn-dendritic-sul-no-change in opposite directions.
954	  - claim: fig3f-ispn-dendritic-sul-no-change
955	    agrees: true
956	    outcome: not_reproduced
957	    reason: Agrees. It turns on one cell, 20190508 cell 3, which holds only a distal site; the paper's
958	      value for it gives exactly the paper's P (0.0545, cell 66). The cell 67 sentence that the difference
959	      in outcome comes from that one cell holds for the main rule only; the stricter basal-ratio rule
960	      gives P = 0.0663, which would also meet the criterion. This is not stated in the conclusion, the
961	      Summary or the finding. Reading the gap as missing data is still inference, as no output shows the
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 3328,3801p docs/pilot-notes.md; sed -n 5476,5500p targets/dandisets.json; sed -n 88,130p README.md
```

```
<persisted-output>
Output too large (37.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7da5272c-faec-4353-b1c1-863c253995bf/tool-results/bz28is0lt.txt

Preview (first 2KB):
### 001075, Randi et al. 2023

Four claims reproduced, four partially and seven blocked on the dandiset.
With outside data, counted apart: one partially reproduced and one not
reproduced. Two claims on data in the paper's OSF repository: one reproduced
and one blocked. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with 15 of the 19. It found that
`osf-link` passed on 87.4% agreement only because all 2,812 manually located
targets agree by construction, while targets found from the position, which
the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
claim from reproduced to partially reproduced. Round 1 also asked for a check
of RID labels, which showed the earlier blocking notes wrong: the dandiset
labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
wrote criteria before computing any RID response and moved `fig4-rid-wt` from
blocked to partially reproduced and `fig4-rid-unc31` from blocked to
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7da5272c-faec-4353-b1c1-863c253995bf/tool-results/bz28is0lt.txt"
}
```

```
1	### 001075, Randi et al. 2023
2	
3	Four claims reproduced, four partially and seven blocked on the dandiset.
4	With outside data, counted apart: one partially reproduced and one not
5	reproduced. Two claims on data in the paper's OSF repository: one reproduced
6	and one blocked. Round 1 gave its own outcome for each claim from the notebook
7	with its conclusions removed and agreed with 15 of the 19. It found that
8	`osf-link` passed on 87.4% agreement only because all 2,812 manually located
9	targets agree by construction, while targets found from the position, which
10	the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
11	claim from reproduced to partially reproduced. Round 1 also asked for a check
12	of RID labels, which showed the earlier blocking notes wrong: the dandiset
13	labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
14	export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
15	wrote criteria before computing any RID response and moved `fig4-rid-wt` from
16	blocked to partially reproduced and `fig4-rid-unc31` from blocked to
17	reproduced. The author kept `not_runnable` for `edfig6-kernel-stereotypy` and
18	`fig6-spontaneous`, where round 1 would have given `other` and `data_missing`,
19	and round 2 accepted both, the first with a reservation as no
20	reimplementation of the kernel fits was tried. Round 2 agreed with all 19 and
[... 523 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 5500,5530p targets/dandisets.json; grep -n -E '^\s*(- id|id|data|uses|elsewhere|source|paper|title|first_author|year|reading|text)\b' claims/001538/*.yaml | head -120
```

```
},
    {
     "doi": "10.1126/sciadv.adv8224",
     "title": "State-dependent modulation of spiny projection neurons controls levodopa-induced dyskinesia in a mouse model of Parkinson\u2019s disease",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/surmeier-lab-to-nwb",
    "contributor Mayorquin, Heberto of CatalystNeuro"
   ]
  },
  {
   "dandiset": "001539",
   "name": "Odor-Place Spatial Association Task",
   "published_version": "0.250815.1203",
   "asset_count": 38,
   "size_gb": 95.3,
[... 119 more lines not kept]
```

**Agent**

The README row is written: 15 (+1) reproduced, 0 (+2) partially, 3 (+1) not reproduced and 15 blocked. Next I'm reading the reports.

**Agent calls Bash**

```bash
cd transcripts/001538; wc -w *-report.md; cat author-report.md
```

```
956 author-report.md
  691 author-revise-1-report.md
  535 author-revise-2-report.md
 1969 verifier-1-report.md
  970 verifier-2-report.md
 5121 total
Done. I followed steps 1 to 5 of the protocol and ran `python tools/entry.py handover entries/001538-zhai-2025`. `check` reports 0 errors and the notebook runs from a clean environment in 248 s. Nothing is committed. I used the full text of the paper, which is open access (PMC12674127, CC BY). I pinned dandiset version 0.260527.1302: the paper cites no version, this is the only published one, and the draft holds the same 468 files.

**1. Outcomes (44 claims)**

| Claim | Data | Outcome |
|---|---|---|
| link-somatic-cells | with_inputs | partially reproduced (73% of cells match exactly, the criterion asked for 80%) |
| link-dendritic-cells | with_inputs | reproduced |
| link-sr-cells | with_inputs | partially reproduced |
| link-grab-rois | with_inputs | not reproduced |
| link-aim-mice | with_labels | not reproduced |
| fig1f rheobase on < off; fig1e F-I; fig1f SCH no change; fig1i dendritic on > off | dandiset | reproduced (4) |
| fig1i SCH lowers the dendritic index | dandiset | partially reproduced (P = 0.066) |
| fig3d, fig3c, fig3d sulpiride no change, fig3f | dandiset | reproduced (4) |
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001538; cat verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md
```

```
I made my own call on all 45 claims in the claims file: 24 reproduced, 2 partially reproduced, 4 not reproduced and 15 blocked. Two of the notebook's dendritic tests come out against the paper, and in both cases the index computation may be the cause rather than the data.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| link-somatic-cells | partially_reproduced | All 12 groups have the paper's n, but only 73.2% of cells match exactly (80% needed) and 85.4% match within 3 spikes (95% needed). Cell 19. |
| link-dendritic-cells | reproduced | Cell counts equal the paper's n in 7 of 10 groups, and the median relative difference is 0.040 (Spearman 0.91). Two cells are far off (1.559 in dSPN on+SCH, 1.014 in iSPN off). Cell 21. |
| link-sr-cells | partially_reproduced | All 14 cells match a paper identifier, but only 2 of 14 are within 25% on both event count and amplitude. Cell 23. |
| link-grab-rois | not_reproduced | The dandiset holds part of the regions (3/13, 3/10, 5/11). Only 5 of 11 mice match within 0.05 on every treatment, short of half. Cell 25. |
| link-aim-mice | not_reproduced | 7 of 9 mice are in the paper, but only 15 of 35 matched session totals are equal. All five Fig. 8 mice differ; the two Fig. 10 mice agree exactly. Cell 27. |
| fig1f-dspn-rheobase-on-lower | reproduced | P = 8.9e-6; medians 140 (on) vs 220 (off). Cell 30. |
| fig1e-dspn-fi-on-higher | reproduced | P = 8.8e-5, on-state higher (88 vs 36); same with complete cells only. Cell 32. |
| fig1f-dspn-sch-no-change | reproduced | P = 1.0; the paired Wilcoxon (n = 5) also gives P = 1.0. Cell 34. |
| fig1i-dspn-dendritic-on-higher | reproduced | P = 0.0091, on-state higher; holds in all variants. Cell 36. |
| fig1i-dspn-dendritic-sch-lower | not_reproduced | P = 0.066 (paper 0.0133). The SCH median is 0.419 against the paper's 0.338; one SCH cell differs 2.6-fold from the paper and may drive this (B1). Cell 38. |
| fig3d-ispn-rheobase-on-higher | reproduced | P = 0.00083; medians 16
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,30p claims/001538/*.yaml
```

```
# Claims for Zhai, Cui, Wokosin, Sun, Tkatch, Crittenden, Graybiel & Surmeier (2025) on dandiset 001538.
# Source: the full text of the version of record in PubMed Central (PMC12674127, CC BY), read from
# its Results, figure legends and Materials and Methods.
#
# What the author had seen when these criteria were written. The data check: the file list and
# metadata of every NWB file; for every patch-clamp file the cell and condition counts, the spike
# counts per current step and each cell's rheobase, and per group the median rheobase; the
# dendritic excitability index per cell and its group medians; the Sr2+-oEPSC events found by the
# detector in lid.py and their per-cell counts and mean amplitudes; the GRAB-ACh areas per mouse;
# the AIM tables. Also the paper's per-cell tables (Zenodo doi:10.5281/zenodo.17307059), and that
# most dandiset cells match a row of them exactly. No statistical test of any claim had been run.
#
# The paper's statistics (Methods) are two-sided Mann-Whitney tests for unpaired and Wilcoxon tests
# for paired data at P < 0.05, unless stated otherwise; the criteria use these. Where the dandiset
# holds so few units that the paper's test cannot reach P < 0.05 whatever the data (the smallest
# attainable two-sided P is 0.057 for 3 against 4, 0.10 for 3 against 3, 0.25 for 3 pairs and
# 0.0625 for 5 pairs), the claim is blocked with `other`, and the numbers are shown under the link
# claim for that data. Groups are formed from the file's condition_subfolder column, not from the
# session name, because files named for a drug also hold baseline cells.
#
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 -E 'id: (fig5f-ach-off-elevated|fig7f|fig8bc|fig10b|fig6d|fig1f-dspn-rheobase|fig3d-ispn-rheobase)' claims/001538/*.yaml
```

```
92:- id: fig1f-dspn-rheobase-on-lower
93-  statement: In dSPNs the rheobase is lower in the LID on-state than in the off-state.
94-  source: Figure 1F; Results, first section (P < 0.0001, Mann-Whitney)
95-  criterion: Two-sided Mann-Whitney test of per-cell rheobase, on-state against off-state.
--
151:- id: fig3d-ispn-rheobase-on-higher
152-  statement: In iSPNs the rheobase is higher in the on-state than in the off-state.
153-  source: Figure 3D; Results, second section (P = 0.0013, Mann-Whitney)
154-  criterion: Two-sided Mann-Whitney test of per-cell rheobase. Reproduced when P < 0.05 and the
--
210:- id: fig5f-ach-off-elevated
211-  statement: Evoked ACh release (GRAB-ACh3.0) in slices from LID off-state mice is greater than in
212-    unlesioned striatum.
213-  source: Figure 5F; Results, third section (P < 0.0001)
--
241:- id: fig6d-m1r-antag-dendritic-lower
242-  statement: M1R antagonism prevents the off-state elevation of iSPN dendritic excitability.
243-  source: Figure 6D (P = 0.012)
244-  criterion: Two-sided Mann-Whitney test of the index, control against M1R antagonist. Reproduced
--
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c 300 docs/pilot-notes.md | od -c | tail -3; cat >> docs/pilot-notes.md <<'EOF'

### 001538, Zhai et al. 2025

Fifteen claims reproduced, three not reproduced and fifteen blocked on the
dandiset, none partially. With outside data, counted apart: one reproduced,
two partially reproduced and one not reproduced. Nine claims on the paper's
per-cell tables on Zenodo are reproduced. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with 44
of the 45; it would call `fig1i-dspn-dendritic-sch-lower` not reproduced, as
its criterion defines only the reproduced case and P is 0.066, and the author
changed it from partially reproduced. The author also changed the reason for
the six spine blocks from `not_runnable` to `methods_underspecified`, as round
1 proposed. Round 2 agreed with all 45 and nothing was proposed, so there was
no third round. The paper reports, in a mouse model of levodopa-induced
dyskinesia, that dSPNs are more excitable in the on-state than in the
off-state and iSPNs less, at the soma and in dendrites, that evoked ACh
release is elevated in the off-state, that M1 receptors and CDGI underlie the
off-state rise in iSPN dendritic excitability, and that deleting CDGI or iSPN
M1 receptors attenuates dyskinesia. The links to the paper's tables, the
somatic and dendritic excitability of dSPNs and iSPNs with SCH 23390,
sulpiride, M1R antagonism, CDGI KO and M1R deletion, and two GRAB-ACh
comparisons were tested on the dandiset. The four Sr2+-oEPSC claims, three
GRAB-ACh claims and the two AIM claims are blocked as `other`, as the
dandiset holds so few cells, regions or mice that the paper's test cannot
reach P < 0.05 whatever the data, and the six spine claims are blocked as
`methods_underspecified`, as counting used AutoQuant, NeuronStudio or Imaris
with manual steps. `fig1i-dspn-dendritic-sch-lower` (P = 0.0662) and
`fig3f-ispn-dendritic-sul-no-change` (P = 0.0097, paper 0.0545) are not
reproduced, and each turns on one cell the dandiset holds only in part: with
the paper's value for that cell the paper's P is recovered (0.0133 and
0.0545). Some outcomes rest on weak ground: under the stricter basal-ratio
rule (0.8 to 1.25) `fig3f-ispn-dendritic-on-lower` gives P = 0.0774 and the
sulpiride claim P = 0.0663, which would reverse both; `fig5f-ach-off-elevated`
is met at P = 0.0357, the smallest attainable for 3 against 5 mice; and the
absence claims `fig3d-ispn-sul-no-change`, `fig5f-ach-off-like-6ohda` and
`fig9d-m1r-crispr-somatic-unchanged` pass with little power. The author used
the full text of the version of record in PubMed Central (PMC12674127), the
paper's per-cell tables on Zenodo (doi:10.5281/zenodo.17307059) and its
analysis scripts on Zenodo, read for method choices and not run.

The dandiset was converted by CatalystNeuro (catalystneuro/surmeier-lab-to-nwb).
It holds no patch-clamp recordings from unlesioned control or 6-OHDA-lesioned
mice (10, 12, 11 and 9 dSPNs; 21, 11, 14 and 9 iSPNs in the paper), nor the
oxo-M line scans of Figure 7E or the open-field data of Figure 10, though the
paper's raw data on Zenodo list folders for all of them. The Sr2+-oEPSC files
hold one cell per mouse (14 of the paper's 33 cells), the GRAB-ACh files one
region per mouse (11 of 34) and the AIM tables 7 of the paper's 44 mice plus
two mice (4124, 5871) not in the paper, and the dandiset does not say that it
holds a subset or how it was chosen. Session names state a drug (D1RaSch,
D2RaSul) for files that also hold baseline on-state sweeps; 11 cells in such
files have a baseline condition, 7 of them also recorded with the drug and 4
baseline only, and the condition of each sweep is only in the
RecordingsIndexTable column condition_subfolder. Two dendritic cells lack the
sites the paper's values need: dSPN on+SCH 20190411 cell 1 has only its second
pair of sites (0.584 against the paper's 0.228) and iSPN on+sul 20190508 cell
3 only a distal site, which is an inference from the recovered P values, as
the paper does not list each cell's sites. Three dendritic site series hold
six trials, two sites under one name, and split they give the paper's values
for these cells; one series holds a single trial, one two and one four. The
genotypes of the CDGI behaviour mice contradict each other across the subject
metadata, the session names, the AIM table's genotype column and the video
files, and the AIM session totals of the five Figure 8 mice differ from the
paper's table in 20 of 25 sessions (mouse 1945 session 1, 33.5 against 27.0),
while the two Figure 10 mice agree in all sessions. The raw spine image stacks
and rotation videos are there, but no spine or rotation counts (none of the 86
spine files has a processing module or analysis entry). Other findings: the
stimulus series of every dendritic sweep is all zero, and the index table
gives no kymograph slice for 53 of 997 dendritic sweeps; the Sr2+-oEPSC
light-pulse OptogeneticSeries is all zero in 69 of 140 sweeps and the
intracellular recordings table references no stimulus; the GRAB-ACh
background images, described as taken at zero laser power, have a mean (381
to 525) above the signal (F0 179 to 355); the files cite the bioRxiv preprint
and use its figure numbers for the behaviour data; patch-clamp subjects are
named by recording date with no animal identifier, in 185 subject folders; 18
somatic cells miss one or more current steps between 20 and 300 pA and 14
repeat a step; and on the paper's own tables the oxo-M test in CDGI KO gives
P = 0.47 where the paper reports 0.910, and the rotation test of Figure 8A
0.012 where the text reports 0.0092.

The notebook ran in 248 s in the first clean run, about 10 minutes after round
1 and 640 s after round 2. No run failed; the author's first check for
kymograph slices missed references of -1, and the data check caught three
wrong sentences, all corrected before the final run. Round 2 found statements
the outputs did not support, among them mouse counts the wrong way round for
the Figure 8A rotations, 11 baseline-only cells where 4 are, a sentence that
the sulpiride outcome comes from one cell, which holds under the main
basal-ratio rule only, and a subject count and dendrite count no output
printed; these were corrected or printed. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: no rule for a dandiset with so few units that the paper's test
cannot reach P < 0.05; no grading for a criterion that defines only
"reproduced"; no rule for raw data without the derived measurement, where the
spine and rotation choices are not fully consistent; whether `elsewhere`
claims may be tested on the paper's tables in place of its raw data; link
claims that gate nothing and only check whether the dandiset holds the
paper's cells; a data check that already showed group medians; clock-check
recipes that assume trial tables or continuous sessions, not sweeps; whether a
conclusion may cite the paper's reported values; and no finding kind for a
reported P that disagrees with the paper's own deposited table.
EOF
git diff --stat
```

```
0000420   a   b   l   e       p   a   r   t   y       f   o   r       t
0000440   h   e       a   t   t   e   m   p   t   .  \n
0000454
 README.md           |  1 +
 docs/pilot-notes.md | 99 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 100 insertions(+)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "3 only a distal site, which is an inference from the recovered P values, as\nthe paper does not list each cell's sites.",
 "new_string": "3 only a distal site; reading these gaps as missing data is an inference from\nthe recovered P values, as the paper does not list each cell's sites."
}
```

```
The file docs/pilot-notes.md has been updated successfully.
```

**Agent**

I ran `python tools/readme_row.py 001538 --write`, which added the row to README.md with 15 (+1) reproduced, 0 (+2) partially, 3 (+1) not reproduced and 15 blocked. I added the subsection below at the end of `docs/pilot-notes.md`. Nothing is committed.

### 001538, Zhai et al. 2025

Fifteen claims reproduced, three not reproduced and fifteen blocked on the
dandiset, none partially. With outside data, counted apart: one reproduced,
two partially reproduced and one not reproduced. Nine claims on the paper's
per-cell tables on Zenodo are reproduced. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with 44
of the 45; it would call `fig1i-dspn-dendritic-sch-lower` not reproduced, as
its criterion defines only the reproduced case and P is 0.066, and the author
changed it from partially reproduced. The author also changed the reason for
the six spine blocks from `not_runnable` to `methods_underspecified`, as round
1 proposed. Round 2 agreed with all 45 and nothing was proposed, so there was
no third round. The paper reports, in a mouse model of levodopa-induced
dyskinesia, that dSPNs are more excitable in the on-state than in the
off-state and iSPNs less, at the soma and in dendrites, that evoked ACh
release is elevated in the off-state, that M1 receptors and CDGI underlie the
off-state rise in iSPN dendritic excitability, and that deleting CDGI or iSPN
M1 receptors attenuates dyskinesia. The links to the paper's tables, the
somatic and dendritic excitability of dSPNs and iSPNs with SCH 23390,
sulpiride, M1R antagonism, CDGI KO and M1R deletion, and two GRAB-ACh
comparisons were tested on the dandiset. The four Sr2+-oEPSC claims, three
GRAB-ACh claims and the two AIM claims are blocked as `other`, as the
dandiset holds so few cells, regions or mice that the paper's test cannot
reach P < 0.05 whatever the data, and the six spine claims are blocked as
`methods_underspecified`, as counting used AutoQuant, NeuronStudio or Imaris
with manual steps. `fig1i-dspn-dendritic-sch-lower` (P = 0.0662) and
`fig3f-ispn-dendritic-sul-no-change` (P = 0.0097, paper 0.0545) are not
reproduced, and each turns on one cell the dandiset holds only in part: with
the paper's value for that cell the paper's P is recovered (0.0133 and
0.0545). Some outcomes rest on weak ground: under the stricter basal-ratio
rule (0.8 to 1.25) `fig3f-ispn-dendritic-on-lower` gives P = 0.0774 and the
sulpiride claim P = 0.0663, which would reverse both; `fig5f-ach-off-elevated`
is met at P = 0.0357, the smallest attainable for 3 against 5 mice; and the
absence claims `fig3d-ispn-sul-no-change`, `fig5f-ach-off-like-6ohda` and
`fig9d-m1r-crispr-somatic-unchanged` pass with little power. The author used
the full text of the version of record in PubMed Central (PMC12674127), the
paper's per-cell tables on Zenodo (doi:10.5281/zenodo.17307059) and its
analysis scripts on Zenodo, read for method choices and not run.

The dandiset was converted by CatalystNeuro (catalystneuro/surmeier-lab-to-nwb).
It holds no patch-clamp recordings from unlesioned control or 6-OHDA-lesioned
mice (10, 12, 11 and 9 dSPNs; 21, 11, 14 and 9 iSPNs in the paper), nor the
oxo-M line scans of Figure 7E or the open-field data of Figure 10, though the
paper's raw data on Zenodo list folders for all of them. The Sr2+-oEPSC files
hold one cell per mouse (14 of the paper's 33 cells), the GRAB-ACh files one
region per mouse (11 of 34) and the AIM tables 7 of the paper's 44 mice plus
two mice (4124, 5871) not in the paper, and the dandiset does not say that it
holds a subset or how it was chosen. Session names state a drug (D1RaSch,
D2RaSul) for files that also hold baseline on-state sweeps; 11 cells in such
files have a baseline condition, 7 of them also recorded with the drug and 4
baseline only, and the condition of each sweep is only in the
RecordingsIndexTable column condition_subfolder. Two dendritic cells lack the
sites the paper's values need: dSPN on+SCH 20190411 cell 1 has only its second
pair of sites (0.584 against the paper's 0.228) and iSPN on+sul 20190508 cell
3 only a distal site; reading these gaps as missing data is an inference from
the recovered P values, as the paper does not list each cell's sites. Three
dendritic site series hold six trials, two sites under one name, and split
they give the paper's values for these cells; one series holds a single
trial, one two and one four. The genotypes of the CDGI behaviour mice
contradict each other across the subject metadata, the session names, the AIM
table's genotype column and the video files, and the AIM session totals of the
five Figure 8 mice differ from the paper's table in 20 of 25 sessions (mouse
1945 session 1, 33.5 against 27.0), while the two Figure 10 mice agree in all
sessions. The raw spine image stacks and rotation videos are there, but no
spine or rotation counts (none of the 86 spine files has a processing module
or analysis entry). Other findings: the stimulus series of every dendritic
sweep is all zero, and the index table gives no kymograph slice for 53 of 997
dendritic sweeps; the Sr2+-oEPSC light-pulse OptogeneticSeries is all zero in
69 of 140 sweeps and the intracellular recordings table references no
stimulus; the GRAB-ACh background images, described as taken at zero laser
power, have a mean (381 to 525) above the signal (F0 179 to 355); the files
cite the bioRxiv preprint and use its figure numbers for the behaviour data;
patch-clamp subjects are named by recording date with no animal identifier, in
185 subject folders; 18 somatic cells miss one or more current steps between
20 and 300 pA and 14 repeat a step; and on the paper's own tables the oxo-M
test in CDGI KO gives P = 0.47 where the paper reports 0.910, and the rotation
test of Figure 8A 0.012 where the text reports 0.0092.

The notebook ran in 248 s in the first clean run, about 10 minutes after round
1 and 640 s after round 2. No run failed; the author's first check for
kymograph slices missed references of -1, and the data check caught three
wrong sentences, all corrected before the final run. Round 2 found statements
the outputs did not support, among them mouse counts the wrong way round for
the Figure 8A rotations, 11 baseline-only cells where 4 are, a sentence that
the sulpiride outcome comes from one cell, which holds under the main
basal-ratio rule only, and a subject count and dendrite count no output
printed; these were corrected or printed. Untracked files in the repository
root that the author did not create were left alone. The author's points on
the protocol: no rule for a dandiset with so few units that the paper's test
cannot reach P < 0.05; no grading for a criterion that defines only
"reproduced"; no rule for raw data without the derived measurement, where the
spine and rotation choices are not fully consistent; whether `elsewhere`
claims may be tested on the paper's tables in place of its raw data; link
claims that gate nothing and only check whether the dandiset holds the
paper's cells; a data check that already showed group medians; clock-check
recipes that assume trial tables or continuous sessions, not sweeps; whether a
conclusion may cite the paper's reported values; and no finding kind for a
reported P that disagrees with the paper's own deposited table.

## End of run

14 turns, 2 minutes, result: success.
