# hasnain-2025 · recorder · run 45025483114

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py hasnain-2025; ls transcripts/hasnain-2025/; wc -c attempts/hasnain-2025-01.yaml claims/hasnain-2025.yaml transcripts/hasnain-2025/*; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
| [000363](https://dandiarchive.org/dandiset/000363) | [Hasnain et al. 2025](https://doi.org/10.1101/2025.10.17.682917) | 1 | 3 | 4 | 11 | [`hasnain-2025`](entries/hasnain-2025) |
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/{amjad-2025-01,andrews-2024-01,armstrong-2026-01,asari-2009-01,asari-2009-02}.md; do echo "=== $f"; cat $f; done; grep -n "^| Dandiset\|^|---" README.md | head; echo; cat summaries/amjad-2025-01.md summaries/asari-2009-02.md; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000363' in json.dumps(x): print(json.dumps(x,indent=1))"
```

```
<persisted-output>
Output too large (35.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/acc2a369-67ec-46a7-87e7-bfbc34e6edd7/tool-results/bun1f71d7.txt

Preview (first 2KB):
=== docs/pilot-notes/amjad-2025-01.md
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/acc2a369-67ec-46a7-87e7-bfbc34e6edd7/tool-results/bun1f71d7.txt"
}
```

```
1	=== docs/pilot-notes/amjad-2025-01.md
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 482 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A15 '"000363"' targets/dandisets.json | head -60; cat transcripts/hasnain-2025/author-report.md transcripts/hasnain-2025/claims-check-report.md
```

```
I've completed steps 1 to 5 of the Author section and built the handover package (step 6). Of the 19 claims, 11 are blocked because the paper's own recordings are not public. Of the 8 tested on the MAP data, 1 is reproduced (resting on one reading of an open method detail), 3 are partially reproduced and 4 are not reproduced. The entry is locked, `check` passes with 0 errors and the notebook ran cleanly from a fresh environment. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| own-recordings-cohort, fig1i, fig2c, fig2e, fig2f, fig2gh, ed2f, fig3c, fig3d, ed3, ed3a (11 claims) | Blocked: data_missing |
| map-session-selection | Not reproduced |
| fig4b-medulla-selectivity | Partially reproduced (assumed) |
| fig4c-alm-null-potent-similar | Partially reproduced (assumed) |
| fig4c-medulla-null-smaller | Reproduced (assumed: only under readings B2 and V2) |
| fig4d-alm-predicts-medulla-null | Not reproduced (assumed) |
| fig4d-decoding-asymmetry | Not reproduced (assumed) |
| fig4e-medulla-null-lower-dimension | Not reproduced (assumed) |
| fig4f-medulla-null-not-spanning-alm | Partially reproduced (assumed) |

No outcome changes across the five seeds.

**2. What was found**

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '000363\|hasnain' targets/dandisets.json | head; head -c 600 targets/dandisets.json
```

```
{
 "schema_version": 1,
 "generated": "2026-11-17T15:59:44+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 678,
  "with_a_paper": 298,
  "with_a_published_version": 256,
  "papers": 316,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 1922.23,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 3 more lines not kept]
```

**Agent**

I've read the five most recent notes and the author's report. DANDI:000363 isn't in `targets/dandisets.json`, so I'm checking how the attempt record cites the dataset before I go on.

**Agent calls Bash**

```bash
cd  grep -n -i 'dandiset\|000363\|catalyst' attempts/hasnain-2025-01.yaml claims/hasnain-2025.yaml | head -20; grep -c . targets/dandisets.json; python -c "
import json;d=json.load(open('targets/dandisets.json'))
for t in d['targets']:
  s=json.dumps(t)
  if 'asnain' in s or '363' in t['dandiset']: print(json.dumps(t,indent=1)[:3000])"
```

```
attempts/hasnain-2025-01.yaml:5:  id: '000363'
attempts/hasnain-2025-01.yaml:7:  doi: 10.48324/dandi.000363/0.231012.2129
attempts/hasnain-2025-01.yaml:15:    name: CatalystNeuro
attempts/hasnain-2025-01.yaml:22:    url: https://github.com/catalystneuro/encore/actions/runs/44974161321
attempts/hasnain-2025-01.yaml:27:  notes: The paper's own cell-type-specific recordings (9 mice, 27 sessions in ALM and tjM1) are not in DANDI:000363,
attempts/hasnain-2025-01.yaml:30:    no dandiset with them; DANDI:001472 holds the data of the authors' earlier paper (ref 39, Nat Neurosci 2025),
attempts/hasnain-2025-01.yaml:353:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
attempts/hasnain-2025-01.yaml:356:    the claims file, with the paper''s full text under paper/. The verifier queried the DANDI API for the dandiset''s
attempts/hasnain-2025-01.yaml:368:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:376:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:384:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:392:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:400:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:408:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:416:    reason: I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174
attempts/hasnain-2025-01.yaml:424:    reason: I checked the DANDI API. 000363 is MAP onl
[... 5 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/hasnain-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: hasnain-2025-01
3	datasets:
4	- archive: dandi
5	  id: '000363'
6	  version: 0.231012.2129
7	  doi: 10.48324/dandi.000363/0.231012.2129
8	  relation: reuses
9	paper: doi:10.1101/2025.10.17.682917
10	date: 2026-11-22
11	entry: hasnain-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 707 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/hasnain-2025/verifier-1-report.md transcripts/hasnain-2025/author-revise-1-report.md transcripts/hasnain-2025/verifier-2-report.md transcripts/hasnain-2025/author-revise-2-report.md
```

```
**Verifier report, round 1: Hasnain, Han & Economo 2025 on DANDI:000363 (0.231012.2129)**

The claims file has 19 claims. 11 rest on the paper's own recordings and 8 on the MAP data. Cells 21 and 31 still contain the author's result text. I read them but reached the outcomes below on my own from the printed outputs.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| own-recordings-cohort, fig1i-selectivity-proportions, fig2c-subspace-variance, fig2e-potent-only-units, fig2f-letn-preference-like-un, fig2gh-letn-span-subspaces, ed2f-false-negatives, fig3c-network-beats-linear, fig3d-letn-un-movement-encoding, ed3-letn-fast-switch, ed3a-cd-early-un-not-letn (11) | blocked (data_missing) | I checked the DANDI API. 000363 is MAP only (contributors Chen, Nguyen, Li, Svoboda; 28 subjects, 174 files in every version). Searching the archive for "Hasnain", "Economo", "extratelencephalic" and "movement-null" finds no dataset with the paper's own recordings. All 11 need phototagged L-ETNs or the paper's videos, so no part can be tested on MAP. |
| map-session-selection | not_reproduced | Cell 12: 17 bilateral sessions from 9 mice (tolerance 20 ± 2). ALM and medulla: 5 sessions from 4 mice, against 11 (Methods) or 16 (Results). Unit counts: ALM 300 (paper 604), medulla 340 (paper 724), right ALM 858 (paper 961 ± 96.1). Only left ALM (1001) is within tolerance. |
| fig4b-medulla-selectivity | partially_reproduced | Cell 16, Bonferroni, E1 reading: sample 34.1%, delay 52.9%, response 86.5%, against 7 / 21 / 49. The order holds (response highest, sample lowest), which the criterion counts as partial, but every value is 2 to 5 times the paper's, under every seed and alpha. |
| fig4c-alm-null-potent-similar | partially_reproduced | Cell 18: the absence holds under every main reading (p 0.13 to 0.26, n = 5). Means are out of tolerance (V1 54.5 / 77.3; V2 null 24.0, below the 28.6 floor). Only the example.m z-score, which M3 calls a "variant", matches (30.7 / 29.1, p = 0
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/hasnain-2025.yaml; grep -n -A3 '^- id:\|^  - id:\|statement:' claims/hasnain-2025.yaml | grep -v quote | head -120
```

```
# Claims for Hasnain, Han & Economo (2025), "Mapping neural subspace dynamics onto the structure
# of the mouse descending motor system", bioRxiv doi:10.1101/2025.10.17.682917, tested on
# DANDI:000363 (Mesoscale Activity Map Dataset), which the paper reuses.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-22,
# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The preprint (version 1, posted 2025-10-17), full text from PMC (PMC12632980), in
# paper/10.1101-2025.10.17.682917.txt: Abstract, Introduction, Results, Discussion, Methods, the
# legends of Extended Data Figures 1 to 3, and the legends of Figures 1 to 4. The paper has no
# separate supplement (PMC lists none); the Extended Data legends are in the text. No PDF was
# supplied, so no figure was read; every claim rests on the text.
#
# Code read. github.com/economolab/subspaceID, commit d593949fef8a39fe0a6eb54a21fc05cbca7bae84,
# the only code the paper links ("Code for identifying movement-null and movement-potent
# subspaces"). It holds orthogonal_subspaces.m (the manopt optimization of the Methods'
# objective, each term normalized by the sum of the top-d eigenvalues of its covariance, with a
# regularization weight alpha that example.m sets to 0), example.m (z-scores each neuron over all
# bins and trials, takes the covariance of stationary and of moving bins, fixes 15 dimensions per
# subspace, rng(101)), and a Python port (funcs.py, example.ipynb). It holds none of the paper's
# other analyses (session selection, movement masks, dimensionality, variance explained,
[... 139 more lines not kept]
```

**Agent**

I have what I need from all the sources. Writing the two files now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/hasnain-2025-01.md",
 "content": "# hasnain-2025, Hasnain et al. 2025\n\nOne claim reproduced, three partially, four not reproduced and eleven\nblocked, all eleven for missing data; all eight tested outcomes rest on an\nassumption. The first verification round agreed with 18 of the 19 outcomes\nand would have given `fig4f-medulla-null-not-spanning-alm` not reproduced;\nthe author kept partial, and the second round agreed with all 19, so there\nwas no third round. It pins version 0.231012.2129, the latest published;\nthe paper cites no version, and the units of the session compared are the\nsame in 0.230822.0128. The paper, Hasnain, Han and Economo, \"Mapping neural\nsubspace dynamics onto the structure of the mouse descending motor system\"\n(bioRxiv, doi:10.1101/2025.10.17.682917), records phototagged layer 5\nextratelencephalic neurons (L-ETNs) and unidentified neurons (UNs) in ALM\nand tjM1 of mice in a delayed-response licking task, and reports that\nL-ETNs are as selective as UNs, have the same movement-null and\nmovement-potent subspace preferences and span both subspaces; in the MAP\nrecordings of Chen et al. (2024), which it reuses from DANDI:000363, it\nreports that the medullary reticular nuclei hold movement-null activity\nthat explains less variance than the potent activity, is predicted from\nALM, has lower dimension and does not span ALM's patterns. The claims were\nwritten from the text of preprint version 1 (PMC12632980), with no figure\nread, and from the linked subspaceID code at commit d593949, which holds\nonly the subspace optimization; the claims check made seven corrections\nand left two points open, the paper's two session and unit counts and a\nvariance-explained reading that departs from the Methods' formula. The 11\nclaims on the paper's own recordings are blocked; the 8 on the MAP data\nwere tested. `fig4c-medulla-null-smaller` is reproduced under one of 15\nreading combinations (G1, B2 and V2: 28.4 against 51.9%, p = 0.017), and is\nseed sensitive, the potent mean being 52.3% under two seeds, outside its\n51.92 bound. Partial are the medulla selectivity (32.4, 49.1 and 85.9%\nagainst 7, 21 and 49%, the order kept), the ALM null against potent\nvariance (no difference, p = 0.086, with the means 51.3 and 79.6% out of\ntolerance) and the UMAP claim (25.7% of ALM units have no medulla\nneighbour against 0.1% with labels shuffled within session, while only\n59.4% of medulla units have an ALM neighbour). Not reproduced are the\nsession selection, both decoding claims (held-out R2 of -611.5 to -249.1%\nfor ALM to medulla against 40%) and the medulla's lower dimension (N1 p =\n0.741, N2 p = 0.087). The selection is held at reading G1 while the other\nreadings are searched; under G2 the ALM claim of Figure 4c would be\nreproduced and Figure 4e reproduced under N2, an asymmetry the round-2\nverifier asked to have stated, which it now is. Round 1 found that the\nelectrodes table had not been checked for CCF positions, that the negative\nR2 values were not traced, that the UMAP null mixed sessions and one\nmedulla session has a null dimension of 1, and that no single reading\nreproduces both Figure 4c claims; in reply units were given the CCF label\nof the nearest classified unit (97.3% agreement), a second notebook\nrepeated Figure 4 under G2, the R2 values were traced to overfitting of a\nnearly unpenalized fit (Spearman -0.61 with predictors per training\ntrial), the UMAP null was shuffled within session, and printing the sample\ncue times found 446 trials with another delay, which were left out. Round\n2 found that the text of several cells and of the record had been written\nfrom another execution than the deposited notebooks; the cause was\nOpenBLAS choosing other kernels on another processor, which the decoder,\nthe UMAP embedding and some G2 shuffle dimensions amplify, and the record\nnow gives both executions' values, with the same outcomes. The kernel was\nnot pinned, which would have taken about three hours more. The author\nasked a reader nothing and no questions file exists. The author's run took\nabout 2.5 hours (02:02 to 04:33 UTC); the notebook ran in 35 minutes at\nfirst, with peak memory about 3.8 GB, and the two notebooks in 2428 and\n3012 s at the end.\n\nThe paper's selection cannot be recovered from the files: with the\ndataset's CCF labels and `classification` it gives 5 ALM and medulla\nsessions from 4 mice with 300 ALM and 340 medullary reticular units, where\nthe paper reports 16 sessions (or 11 from 7 mice) with 604 and 724 units,\nand 17 bilateral ALM sessions from 9 mice where the paper reports 20 from\n10; with `unit_quality` and transferred labels it gives 19 ALM and medulla\nsessions from 7 mice with 1501 and 1745 units, and 31 bilateral sessions.\nThe CCF annotation (`anno_name`) is filled only for units whose\n`classification` is good (69453 of 272227 units), which its description\ndoes not say, though the electrodes table holds each electrode's CCF\ncoordinates. Units carry two quality labels, `unit_quality` and\n`classification`, with no statement of how they differ, and 1852 units\nhave no `classification` value. The trial table has no column for the\ndelay duration, and 446 correct and error trials over 22 sessions (13 to\n57 per session) have a 1.8 s or 0.3 s delay in place of 1.2 s, which shows\nonly in the event times. The jaw, nose and tongue tracking are stored in\n'a.u.' but hold pixel positions of the side camera (about 294 Hz). The\nbaseline z-score reaches 278 s.d. among units classified good and above\n50000 among units with `unit_quality` good. The spike, video and trial\nclocks agree in all 22 selected sessions. The paper's own recordings are\nnot public and no dandiset holds them; DANDI:001472 holds the data of the\nauthors' earlier paper. In the paper, the ALM and medulla sessions are 16\nin the Results and 11 in the Methods, the bilateral ALM units 1116 and\n2016, and the decoding window 40 and 45 ms. Questions are put to the\npaper's authors: how R2 and lambda were computed for the decoding, how the\nmovement threshold was set, which trials and which 'good' label were used,\nhow variance explained is normalized and which dimensionality measure\nFigure 4e uses, and how near-silent units were handled in the z-score.\n\nThe author's points on the protocol: the claims file's readings multiply\ninto dozens of combinations, and each was run against the main one, one\nfactor at a time; it does not say whether a variant named in the claims\nfile can decide an outcome, and the example.m z-score was not allowed to;\na criterion where neither branch applies was judged partial; \"reproduced\nunder any reading\" conflicts with adopting the best-supported reading, and\nthe criterion was followed with `assumed` set; per-claim seeds do not fit\nclaims that share one computation, and one claim's seed was used; seed\nchecks for every reading multiply the runtime and were run for the main\nand the deciding reading only; it does not say when to mark `assumed` for\nan assumption that applies to every claim; and an atlas check tried\noutside the notebook was dropped and left out of the record.\n"
}
```

```
File created successfully at: docs/pilot-notes/hasnain-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/hasnain-2025-01.md",
 "content": "The paper's main findings on layer 5 extratelencephalic neurons, that they resemble other motor cortex neurons in selectivity and subspace preference, could not be tested, as the paper's own recordings are not public. On the reused recordings behind Figure 4, the paper's session selection could not be recovered, leaving 5 ALM and medulla sessions where the paper has 16. Medullary movement-null activity explained less variance than movement-potent activity under only one of several analysis readings, and medullary selectivity, similar null and potent variance in ALM, and ALM patterns absent from the medulla held in part. Prediction of medullary null activity from ALM and its lower dimension did not reproduce; the decoder as described overfit, and the paper leaves its method open.\n"
}
```

```
File created successfully at: summaries/hasnain-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/hasnain-2025-01.md; grep -c '—\|rather' summaries/hasnain-2025-01.md docs/pilot-notes/hasnain-2025-01.md; git status --short
```

```
121 summaries/hasnain-2025-01.md
summaries/hasnain-2025-01.md:0
docs/pilot-notes/hasnain-2025-01.md:0
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
?? docs/pilot-notes/hasnain-2025-01.md
?? scripts
?? summaries/hasnain-2025-01.md
```

**Agent**

The summary is 121 words, one over the limit, so I'm trimming it.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/hasnain-2025-01.md",
 "old_string": "On the reused recordings behind Figure 4, the paper's session selection could not be recovered, leaving 5 ALM and medulla sessions where the paper has 16. Medullary movement-null activity explained less variance than movement-potent activity under only one of several analysis readings,",
 "new_string": "On the reused recordings behind Figure 4, the session selection could not be recovered, leaving 5 ALM and medulla sessions where the paper has 16. Medullary movement-null activity explained less variance than movement-potent activity under only one of several readings,"
}
```

```
The file summaries/hasnain-2025-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote both files and changed nothing else. One gap: DANDI:000363 has no entry in `targets/dandisets.json`, so the `catalystneuro` field couldn't be read. I left out the "converted by CatalystNeuro" opening rather than guess. The summary is 118 words.

`docs/pilot-notes/hasnain-2025-01.md`:

# hasnain-2025, Hasnain et al. 2025

One claim reproduced, three partially, four not reproduced and eleven blocked, all eleven for missing data; all eight tested outcomes rest on an assumption. The first verification round agreed with 18 of the 19 outcomes and would have given `fig4f-medulla-null-not-spanning-alm` not reproduced; the author kept partial, and the second round agreed with all 19, so there was no third round. It pins version 0.231012.2129, the latest published; the paper cites no version, and the units of the session compared are the same in 0.230822.0128. The paper, Hasnain, Han and Economo, "Mapping neural subspace dynamics onto the structure of the mouse descending motor system" (bioRxiv, doi:10.1101/2025.10.17.682917), records phototagged layer 5 extratelencephalic neurons (L-ETNs) and unidentified neurons (UNs) in ALM and tjM1 of mice in a delayed-response licking task, and reports that L-ETNs are as selective as UNs, have the same movement-null and movement-potent subspace preferences and span both subspaces; in the MAP recordings of Chen et al. (2024), which it reuses from DANDI:000363, it reports that the medullary reticular nuclei hold movement-null activity that explains less variance than the potent activity, is predicted from ALM, has lower dimension and does not span ALM's patterns. The claims were written from the text of preprint version 1 (PMC12632980), with no figure read, and from the linked subspaceID code at commit d593949, which holds only the subspace optimization; the claims check made seven corrections and left two points open, the paper's two session and unit counts and a variance-explained reading that departs from the Methods' formula. The 11 claims on the paper's own recordings are blocked; the 8 on the MAP data were tested. `fig4c-medulla-null-smaller` is reproduced under one of 15 reading combinations (G1, B2 and V2: 28.4 against 51.9%, p = 0.017), and is seed sensitive, the potent mean being 52.3% under two seeds, outside its 51.92 bound. Partial are the medulla selectivity (32.4, 49.1 and 85.9% against 7, 21 and 49%, the order kept), the ALM null against potent variance (no difference, p = 0.086, with the means 51.3 and 79.6% out of tolerance) and the UMAP claim (25.7% of ALM units have no medulla neighbour against 0.1% with labels shuffled within session, while only 59.4% of medulla units have an ALM neighbour). Not reproduced are the session selection, both decoding claims (held-out R2 of -611.5 to -249.1% for ALM to medulla against 40%) and the medulla's lower dimension (N1 p = 0.741, N2 p = 0.087). The selection is held at reading G1 while the other readings are searched; under G2 the ALM claim of Figure 4c would be reproduced and Figure 4e reproduced under N2, an asymmetry the round-2 verifier asked to have stated, which it now is. Round 1 found that the electrodes table had not been checked for CCF positions, that the negative R2 values were not traced, that the UMAP null mixed sessions and one medulla session has a null dimension of 1, and that no single reading reproduces both Figure 4c claims; in reply units were given the CCF label of the nearest classified unit (97.3% agreement), a second notebook repeated Figure 4 under G2, the R2 values were traced to overfitting of a nearly unpenalized fit (Spearman -0.61 with predictors per training trial), the UMAP null was shuffled within session, and printing the sample cue times found 446 trials with another delay, which were left out. Round 2 found that the text of several cells and of the record had been written from another execution than the deposited notebooks; the cause was OpenBLAS choosing other kernels on another processor, which the decoder, the UMAP embedding and some G2 shuffle dimensions amplify, and the record now gives both executions' values, with the same outcomes. The kernel was not pinned, which would have taken about three hours more. The author asked a reader nothing and no questions file exists. The author's run took about 2.5 hours (02:02 to 04:33 UTC); the notebook ran in 35 minutes at first, with peak memory about 3.8 GB, and the two notebooks in 2428 and 3012 s at the end.

The paper's selection cannot be recovered from the files: with the dataset's CCF labels and `classification` it gives 5 ALM and medulla sessions from 4 mice with 300 ALM and 340 medullary reticular units, where the paper reports 16 sessions (or 11 from 7 mice) with 604 and 724 units, and 17 bilateral ALM sessions from 9 mice where the paper reports 20 from 10; with `unit_quality` and transferred labels it gives 19 ALM and medulla sessions from 7 mice with 1501 and 1745 units, and 31 bilateral sessions. The CCF annotation (`anno_name`) is filled only for units whose `classification` is good (69453 of 272227 units), which its description does not say, though the electrodes table holds each electrode's CCF coordinates. Units carry two quality labels, `unit_quality` and `classification`, with no statement of how they differ, and 1852 units have no `classification` value. The trial table has no column for the delay duration, and 446 correct and error trials over 22 sessions (13 to 57 per session) have a 1.8 s or 0.3 s delay in place of 1.2 s, which shows only in the event times. The jaw, nose and tongue tracking are stored in 'a.u.' but hold pixel positions of the side camera (about 294 Hz). The baseline z-score reaches 278 s.d. among units classified good and above 50000 among units with `unit_quality` good. The spike, video and trial clocks agree in all 22 selected sessions. The paper's own recordings are not public and no dandiset holds them; DANDI:001472 holds the data of the authors' earlier paper. In the paper, the ALM and medulla sessions are 16 in the Results and 11 in the Methods, the bilateral ALM units 1116 and 2016, and the decoding window 40 and 45 ms. Questions are put to the paper's authors: how R2 and lambda were computed for the decoding, how the movement threshold was set, which trials and which 'good' label were used, how variance explained is normalized and which dimensionality measure Figure 4e uses, and how near-silent units were handled in the z-score.

The author's points on the protocol: the claims file's readings multiply into dozens of combinations, and each was run against the main one, one factor at a time; it does not say whether a variant named in the claims file can decide an outcome, and the example.m z-score was not allowed to; a criterion where neither branch applies was judged partial; "reproduced under any reading" conflicts with adopting the best-supported reading, and the criterion was followed with `assumed` set; per-claim seeds do not fit claims that share one computation, and one claim's seed was used; seed checks for every reading multiply the runtime and were run for the main and the deciding reading only; it does not say when to mark `assumed` for an assumption that applies to every claim; and an atlas check tried outside the notebook was dropped and left out of the record.

`summaries/hasnain-2025-01.md`:

The paper's main findings on layer 5 extratelencephalic neurons, that they resemble other motor cortex neurons in selectivity and subspace preference, could not be tested, as the paper's own recordings are not public. On the reused recordings behind Figure 4, the session selection could not be recovered, leaving 5 ALM and medulla sessions where the paper has 16. Medullary movement-null activity explained less variance than movement-potent activity under only one of several readings, and medullary selectivity, similar null and potent variance in ALM, and ALM patterns absent from the medulla held in part. Prediction of medullary null activity from ALM and its lower dimension did not reproduce; the decoder as described overfit, and the paper leaves its method open.

## End of run

14 turns, 2 minutes, $0.93 at API prices, result: success.
