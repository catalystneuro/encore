# brudner-2026 · recorder · run 43193776343

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/brudner-2026/; python tools/readme_row.py brudner-2026; ls summaries | head; grep -n -A12 '"001871"' targets/dandisets.json
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/ashworth-2025-01.md
docs/pilot-notes/athalye-2023-01.md
docs/pilot-notes/azcorra-2023-01.md
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
claims-report.md
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 7751,7770p targets/dandisets.json; head -5 README.md | head -3; grep -n "readme\|| Dandiset" README.md | head; for f in amjad-2025-01 armstrong-2026-01 ashworth-2025-01 athalye-2023-01 azcorra-2023-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; echo "--- summary"; cat summaries/$f.md; done
```

```
<persisted-output>
Output too large (40.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3e2cdc9-d29a-495b-971e-859929858831/tool-results/bi2ihgv1z.txt

Preview (first 2KB):
    "behavioral approach"
   ],
   "papers": [
    {
     "doi": "10.1007/s00348-018-2591-3",
     "title": "Quantification of airborne odor plumes using planar laser-induced fluorescence",
     "relation": "References",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001878",
   "name": "Standardized behavioral segmentation datasets",
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/brudner-2026-01.yaml; cat claims/brudner-2026.yaml
```

```
<persisted-output>
Output too large (105.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d3e2cdc9-d29a-495b-971e-859929858831/tool-results/bw12xiqe9.txt

Preview (first 2KB):
schema_version: 3
id: brudner-2026-01
datasets:
- archive: dandi
  id: "001871"
  version: 0.260630.1657
  doi: 10.48324/dandi.001871/0.260630.1657
  relation: primary
paper: doi:10.1073/pnas.2608896123
date: 2026-11-12
entry: brudner-2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3e2cdc9-d29a-495b-971e-859929858831/tool-results/bi2ihgv1z.txt"
}
```

```
1	    "behavioral approach"
2	   ],
3	   "papers": [
4	    {
5	     "doi": "10.1007/s00348-018-2591-3",
6	     "title": "Quantification of airborne odor plumes using planar laser-induced fluorescence",
7	     "relation": "References",
8	     "resource_type": "JournalArticle",
9	     "preprint": false
10	    }
11	   ],
12	   "catalystneuro": []
13	  },
14	  {
15	   "dandiset": "001878",
16	   "name": "Standardized behavioral segmentation datasets",
17	   "published_version": null,
18	   "asset_count": 6,
19	   "size_gb": 0.23,
20	   "data_standards": [
[... 526 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3e2cdc9-d29a-495b-971e-859929858831/tool-results/bw12xiqe9.txt"
}
```

```
1	schema_version: 3
2	id: brudner-2026-01
3	datasets:
4	- archive: dandi
5	  id: "001871"
6	  version: 0.260630.1657
7	  doi: 10.48324/dandi.001871/0.260630.1657
8	  relation: primary
9	paper: doi:10.1073/pnas.2608896123
10	date: 2026-11-12
11	entry: brudner-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 753 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d3e2cdc9-d29a-495b-971e-859929858831/tool-results/bw12xiqe9.txt",
 "offset": 774,
 "limit": 240
}
```

```
774	      Summary's statement that turn events end before the turn does is not shown by any output.
775	    response: 'Added the half-height reading (plumes.half_height_run): medians -25.0 to -26.6 and +26.8
776	      to +27.7, outside tolerance. Added outputs of where the events lie: inside the half-height run (start
777	      1 frame after its rising crossing, stop 1 frame before its falling one), and 99.9% stop before the
778	      falling 20% crossing, a median of 4 frames before. Kept the verified outcome and proposed not_reproduced,
779	      the outcome under the claims file''s readings, with the 20% bounds as a variant; asked a reader
780	      whether the deposited events are the paper''s turn bounds.'
781	  - claim: figs5fh-smoothing-agent
782	    agrees: true
783	    outcome: blocked
784	    reason: Agreed, listed among the other 13 blocked claims, with no reason given.
785	    response: No change.
786	- date: '2026-11-12'
787	  kind: agent
788	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
789	  reviewed: Round 3. The proposed change of outcome of figs5c-turn-angles, the only one in the record, with
790	    the analysis behind it in the notebook (cell 24), the helper module, the claims file and the attempt
791	    record; the verifier also read the paper under paper/.
792	  results:
793	  - claim: figs5c-turn-angles
[... 220 more lines not kept]
```

**Agent**

I've read the attempt record and the first part of the claims file. Next I'm reading the remaining claim statements and the reports.

**Agent calls Bash**

```bash
cd  grep -n -A4 "^- id:" claims/brudner-2026.yaml | grep -v "^--$" | sed -n 40,200p
```

```
254-  quote: In both plume types, odor motion features with one-frame delays had higher ROC AUC values
265:- id: fig2d-smooth-weights
266-  statement: Fitted on all three z-scored features together in the smooth plume, the logistic model
267-    gives the gradient a much larger weight (about 2.6) than motion (about 0.06), and the sum a
268-    weight of 0; the combined model reaches a test AUC of 0.847.
269-  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 3; Figure 2D; SI
294:- id: fig2e-complex-weights
295-  statement: Fitted on all three features together in the complex plume, the logistic model gives
296-    motion a larger weight (about 0.40) than the gradient (about 0.10), and the sum a weight of 0;
297-    the combined model reaches a test AUC of 0.612.
298-  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 3; Figure 2E; SI
316:- id: fig3bc-mnm-filters
317-  statement: A minimal opponent network trained to find the centerline learns gradient-detector
318-    filters (opposite signs on the two antennae) in the smooth plume, and in the complex plume
319-    filters with a delayed negative lobe in f1 like a motion detector; test AUCs are 0.726 (smooth)
320-    and 0.517 (complex).
347:- id: fig3d-mnm-gradient-response
348-  statement: The minimal network trained in the smooth plume responds more strongly to synthetic
349-    gradient signals than the one trained in the complex plume.
350-  source: Results, Optimized Bilateral Computation for Centerline-Finding Recovers Plume-Specific Odor
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/brudner-2026; wc -w *-report.md; cat author-report.md
```

```
118 answer-report.md
  299 author-answers-report.md
 1009 author-report.md
  641 author-revise-1-report.md
  638 author-revise-2-report.md
  298 author-revise-3-report.md
  665 claims-check-report.md
  658 claims-report.md
 1465 verifier-1-report.md
 1621 verifier-2-report.md
  544 verifier-3-report.md
 7956 total
I've finished steps 1 to 5 of the Author section and run `entry.py handover`. `entry.py check` reports 0 errors, and `entry.py all` passed from a clean environment (735 s, peak memory 7.1 GB). Nothing is committed.

## 1. Outcomes (22 claims)

| Claim | Outcome |
|---|---|
| fig5e-cue-betas | reproduced, rests on assumptions |
| fig5f-cue-dominance | reproduced, rests on assumptions |
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/brudner-2026; for f in claims-report claims-check-report answer-report author-answers-report author-revise-1-report author-revise-2-report author-revise-3-report; do echo "=== $f"; cat $f.md; done
```

```
=== claims-report
I wrote `claims/brudner-2026.yaml` with 22 claims. `tools/claims_check.py` reports 22 claims, 22 quotes, 4 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PNAS 123(29), published 14 July 2026) and its SI Appendix: Supplementary Methods, the legends of Figs. S1 to S5 and of Movies S1 and S2. Nothing the claims need is missing from the text. I opened PDF pages only to read bar heights (Figs. 2, 4, 5 and S5) and the upwind-turn formula of the SI agent model, which the text garbles.

**Code read.** github.com/emonetlab/GradientMotionMultiplePlumes at commit effc7b0. It holds the Fig. 5E/F analysis, written to run on this dandiset, plus its published result tables. It also holds the Fig. 1 cue maps, the Fig. 2 models with their plotted values, and a re-implementation of the Fig. 3 training.

**Claims.**
- All 22 have quotes and criteria.
- Statistics: 4 entries in 3 claims (Fig. 4 z-tests, P < 0.001; Fig. 5E coefficients, P < 0.005 and P < 0.01; Fig. S5H, P < 0.005).
- Data:
  - 7 use the dandiset alone: Fig. 2C and 2E (the complex plume), and Figs. 5E, 5F, S5C and the intensity-bias finding (behaviour). The S1 resolution claim (Fig. S1F, G) is also on the complex plume.
  - 13 need the smooth plume from Dryad (doi:10.5061/dryad.g27mq71).
  - 2 (Fig. 2B, 2D) use the smooth plume only.

**Details left open, with the readings named.**
- **Fig. 5E/F filters.** The complex-plume heading window is 160 to 200° in the Methods and 150 to 210° in the code. The code alone drops turns within 15 mm of the arena edges. The Methods z-score the cue signals but the code fits them as stored, so the readings are as stored, z-scored over the plume, or z-scored per trajectory. "Not significant" is read as p ≥ 0.05 or p ≥ 0.01.
- **Fig. 1 and S1 comparisons.**
  - The paper does not say how the z-score maps are compared: mean |z| over the plume mask, over the whole frame, or its 95th percentile.
  - The mask's "bias" could be 
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/brudner-2026; head -c 2500 verifier-1-report.md; echo; echo ====; head -c 2000 verifier-2-report.md; echo ====; head -c 1500 verifier-3-report.md; ls ../../questions | grep brud; grep -n "catalystneuro" ../../targets/dandisets.json | head -2
```

```
**Verifier report, brudner-2026, round 1 (DANDI:001871 @ 0.260630.1657)**

The claims file has 22 claims. The notebook tests 6, treats 16 as blocked, and its own table covers all 22.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig5e-cue-betas | not_reproduced | The criterion counts a claim as reproduced only if every reading gives that result; here the result depends on the reading. With the SI onset (`rule20`) and smoke-2a, both plumes pass with stored or pooled z-scored signals. Per-trajectory z-scoring fails both plumes: smooth motion p = 0.0066, complex motion p = 0.098 and 0.204 (cell 11). Under the code's readings the complex coefficients have the wrong sign and are out of tolerance (motion −0.0119 against +0.0441 ± 0.0159; cell 12). |
| fig5f-cue-dominance | reproduced | One reading gives both values within tolerance with the right signs: `rule20`, smoke-2a, heading 150–210, z none or pooled gives smooth 0.935 and complex −0.715 (cell 14). smoke-1a with the event start and heading 160–200 also gives 0.879 / −0.701. The result is fragile: under the code's readings the complex value is +0.388. |
| figs5c-turn-angles | reproduced (rests on an added reading) | With the files' event bounds, both readings in the claims file give medians of about ±21°, outside tolerance. Only the notebook's own turn bounds (20% crossings on the rising and falling edges) give −35.0 / +35.9, or −33.1 / +36.6 for the kept turns (cell 16). That rule has a bug (problem 2). |
| fig2c-complex-auc | partially_reproduced | Motion AUC is above gradient AUC under every reading. Under the two samplings the claims file names, the sum AUC is 0.63–0.67, which fails the sum condition. Only the added mirror sampling gives a sum AUC of 0.500. The values miss under every reading: motion 0.602 against 0.618 ± 0.005, gradient 0.554–0.560 against 0.537 ± 0.012 (cell 25). |
| fig2e-complex-weights | partially_reproduced | \|motion\| (0.415–0.424) is larger than \|gradient\| under eve
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Blocked\|blocked" README.md | head -5; grep -n "+\|elsewhere\|with_inputs" tools/readme_row.py | head -30; grep -n "data:" claims/brudner-2026.yaml | sort | uniq -c | head; grep -n "^- id:\|^  data:" claims/brudner-2026.yaml
```

```
6:elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
7:findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
37:    return "| " + ", ".join(cells)
62:            m = sum(1 for o in mine if kinds.get(o["claim"]) == "with_inputs")
63:            cells.append(f"{n} (+{m})" if m else str(n))
65:    surname, year = re.match(r"^(.+?)-(\d{4})(?:-|$)", paper).groups()
70:            f"| [{surname.capitalize()} et al. {year}](https://doi.org/{doi}) | " + " | ".join(cells)
71:            + f" | [`{entry_dir.name}`](entries/{entry_dir.name}){note} |")
      1 123:  data: with_inputs
      1 155:  data: with_inputs
      1 197:  data: elsewhere
      1 256:  data: with_inputs
      1 274:  data: elsewhere
      1 326:  data: with_inputs
      1 354:  data: with_inputs
      1 373:  data: with_inputs
      1 399:  data: with_inputs
      1 435:  data: with_inputs
63:- id: fig1eh-snapshot-organization
74:  data: with_inputs
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,12p README.md; cat docs/pilot-notes/knierim-2000-02.md | head -3; wc -w docs/pilot-notes/{amjad-2025-01,armstrong-2026-01,ashworth-2025-01,athalye-2023-01,azcorra-2023-01}.md; cat questions/brudner-2026.yaml | head -60
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

# 001754 again, on the fixed draft (2026-10-15)

The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
  392 docs/pilot-notes/amjad-2025-01.md
 1519 docs/pilot-notes/armstrong-2026-01.md
 1767 docs/pilot-notes/ashworth-2025-01.md
 1340 docs/pilot-notes/athalye-2023-01.md
 1101 docs/pilot-notes/azcorra-2023-01.md
[... 61 more lines not kept]
```

**Agent**

I have everything I need: three verification rounds, the outcome counts, and the reasons. Writing the two files now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/brudner-2026-01.md",
 "content": "# brudner-2026, Brudner et al. 2026\n\nNo claim reproduced, three partially and three not reproduced, with one claim\nblocked on the dandiset alone and 13 more that also need outside data, plus\ntwo claims on data elsewhere (the smooth plume on Dryad), both blocked. The\nfirst verification round agreed with 20 of the 22 outcomes as they stood, the\nsecond with all 22, two of them only conditionally, and a third round, on the\none change proposed after the second, agreed with it. It pins version\n0.260630.1657, the only published version and the one the paper's code names.\nThe paper, Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark and\nEmonet, \"Fly navigational responses exploit plume-specific odor motion and\ngradient cues\" in PNAS, shows that the crosswind odor gradient is organized\nantisymmetrically about the centerline in a smooth plume and odor motion in a\ncomplex one, that logistic models and small networks trained to find the\ncenterline pick up the cue of their plume, that agents gain from adding such\nbilateral detection to a wind-only strategy, and that the crosswind turns of\nblinded flies with optogenetic odor are predicted by the gradient in the\nsmooth plume and by motion in the complex plume; the dandiset holds 131\nbehavior files (83 smooth, and two complex sets of 24, \"smoke-1a\" and\n\"smoke-2a\"), a 1500-frame window of the complex plume movie, three freestream\nwindows and a compact asset of the Fig. S1 freestream inputs. The claims were\nwritten from the version of record with its SI Appendix and from the paper's\ncode (emonetlab/GradientMotionMultiplePlumes at effc7b0), which holds the\nFig. 5E/F analysis written for this dandiset with its published tables, the\nFig. 1 and 2 cue and model code and a re-implementation of Fig. 3, and nothing\nfor the agent simulations or Fig. S1. Every claim on the smooth plume, the\nnetworks or the agents is blocked as `other`, as the smooth plume could not be\nread and no agent code exists. Not reproduced are `fig5e-cue-betas` (with the\nSI's onset and the smoke-1a files no reading passes, 0 of 24, and no file set\nor onset gives the result in every reading), `figs1fg-resolution-robustness`\n(motion r 0.729 to 0.820 at a 4-frame delay as stored, below 0.8 in every\nreading, and gradient r 0.613 at 12 pixels without smoothing) and\n`figs5c-turn-angles` (medians of -20.8 and +21.3 degrees over the files' turn\nevents against -34.2 and +33.8). Partial are `fig2c-complex-auc` (motion AUC\n0.603 above gradient 0.560, neither within tolerance, resting on an assumed\nmirror balancing of the samples), `fig2e-complex-weights` (|motion| 0.426\nabove |gradient| 0.262, against 0.098 +/- 0.041) and `fig5f-cue-dominance`\n(smooth 0.937 within tolerance, complex -0.492 outside -0.662 +/- 0.066,\nresting on the smoke-1a files and the SI onset). `methods-intensity-right-bias`\nis blocked as `metadata_insufficient`: it holds under every reading if -1 is a\nright turn and fails under every reading if +1 is. The freestream and complex\nparts of the two Fig. S1 claims hold (index -2.93, -1.53 and +0.04 at 5, 10 and\n20 cm/s and 4.40 complex), as does the complex part of `figs2c-one-frame-delay`,\nbut the claims stay blocked. The author's first run gave three reproduced (all\non assumptions: the SI onset with the smoke-2a files for Fig. 5, and a turn end\nat 20% of the peak for Fig. S5C), two partially, one not reproduced and 16\nblocked. The author asked a reader nothing, so the answer and author-answers\nruns changed nothing. Round 1 disagreed on fig5e (not reproduced, as the result\ndepends on the reading) and fig5f, doubted the smoke-2a choice, since the\ndandiset's description says smoke_1a_orig was analysed throughout the paper,\nfound that the onset rule ignored the sign of the rotation and asked for the\ndecidable Fig. S1 parts; in reply the smoke-1a files became the assumed complex\nplume, fig5e moved to not reproduced and fig5f to partially reproduced, against\nthe verifier, the onset rule was fixed (the old one reversed in 0.2% of turns),\nfits per projection flip and a comparison with the code's published tables were\nadded, and a reader was asked whether the dataset's turn start is the SI's\nonset. Round 2 agreed with all 22, with fig5f and figs5c only conditionally,\nfound sentences the outputs did not support (that the complex motion cue never\nreaches significance, that only smoke-1a matches the published tables, that the\nsets do not differ by a flip convention, 1011 trajectories where the output\nprints 1010) and asked for a test of the cue signs against the plume geometry,\nwhich could not tell the two sets apart; the author removed the assumption flag\nof fig5e, ran the half-height turn bounds (medians -25.0 to -26.6 and +26.8 to\n+27.7), proposed not reproduced for figs5c and put three more questions to a\nreader. Round 3 reviewed only that proposal and agreed. The author's run took\nabout 1 h 40 min (04:15 to 05:56 UTC); a development run peaked at 11.9 GB of\nmemory, fixed before the clean runs, which peaked at 7.1 GB, and the notebook\nran in 735 s at first, 19 minutes after round 1, 823 s after round 2 and 929 s\nat the end. Untracked dotfiles in the repository root, which the author did not\ncreate, were left alone.\n\nThe smooth plume movie, used by 15 of the paper's 22 claims, is not in the\ndandiset; the description points to Dryad (doi:10.5061/dryad.g27mq71), which\nanswers 401 to downloads without an API token, and the paper's own rescaled\nversion is in neither the dandiset nor its Yale Dataverse deposit. The\ncomplex-plume behavior files come in two sets, smoke-1a and smoke-2a (24 files\neach, on the same days and vials, each with 12 flipped and 12 unflipped\nprojections), whose session descriptions name two movies and whose signals\ndiffer (99th percentile of the intensity 171 and 252, and a motion coefficient\npositive in one set and negative in the other in both projection flips);\nnothing says what smoke_2a is, the dandiset's description says smoke_1a_orig\nwas analysed throughout the paper, and the code selects smoke-2a only, so a\nsign convention differing between the sets cannot be ruled out. The code's\npublished Fig. 5E and 5F tables are matched most closely by the smoke-1a files\nwith the dataset's turn start and 160 to 200 degrees (within 0.1 SE, all four\nlog-likelihoods within 0.001 per turn), not by the smoke-2a files with 150 to\n210 degrees that the code names, which give a motion coefficient of -0.0119\n(p 0.15) and a cue dominance of +0.388 where the tables give +0.0441 and\n-0.662. The turn events are not described: they start a median of 4 frames\n(about 67 ms) after the SI's onset and stop a median of 4 frames before the\nfalling 20% crossing, so turns over the events measure about 21 degrees\nagainst the paper's 34. The turn direction (+1 or -1) is not mapped to left or\nright, and the heading, said to be in standardized arena coordinates, is\natan2(-vy, vx), so the rightward bias towards the projector cannot be tested.\nNo file gives the movie frame shown at a trajectory frame, so the odor signals\ncannot be aligned with the deposited complex window, whose provenance names a\npreprocessing run 'bgsub_gauss3_fullslice_p001_p99' that may differ from the\nmovie the paper analysed. odor_velocity is NaN on 95 to 98% of frames, which\nits description does not explain. Four smooth-plume files hold 10 frames with\ny of 768 to 814 mm in an arena 170 mm wide, 205 of 7235 trajectories have no\nposition at all, and in 47 files some trajectories carry timestamps and others\na starting time and rate. Questions are put to the paper's authors: which\ncomplex files are the complex plume of Fig. 5 and what smoke_2a is; which turn\nonset Fig. 5E-F used; how the Fig. 2 and 3 samples were balanced; where a turn\nends for Fig. S5C; how the Fig. S1G motion cue is defined and whether the maps\nwere smoothed; whether the Fig. 5 predictors were z-scored over all frames or\nper trajectory; and whether the two complex sets share a sign convention.\n\nThe author's points on the protocol: the Dryad file was not staged although\n`docs/archives.md` says it would be, and no `blocked_by` value fits data that\nare public but cannot be fetched; `entry.py lock` writes a `python:` field the\nentry schema rejects; `entry.py check` requires `about:` on findings whose\n`about` the attempt schema forbids; it does not say how to combine readings of\nseveral independent open details, or whether a reading the author adds counts\nunder \"one reading\"; the rule for `measured` does not cover an added reading;\nthe clock check cannot be done when the files hold no stimulus frame index; it\ndoes not say whether to compute the decidable parts of a claim blocked anyway;\nand the fig5e criterion tests significance but not sign.\n"
}
```

```
File created successfully at: docs/pilot-notes/brudner-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/brudner-2026-01.md",
 "content": "None of the paper's main findings was fully confirmed in this data, and most could not be tested. The plume-specific organization of gradient and motion cues, the trained networks and the navigating agents could not be tested, because the smooth plume movie is not in the dataset. In the complex plume, motion predicted the centerline side better than the gradient, but the model values missed the paper's. Fly turns followed the gradient in the smooth plume, but the complex-plume motion effect did not hold in every reading and its dominance held only in part, as the dataset holds two undocumented complex-plume file sets. Minor claims on cue robustness and turn size (about 21 against 34 degrees) did not reproduce.\n"
}
```

```
File created successfully at: summaries/brudner-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/brudner-2026-01.md docs/pilot-notes/brudner-2026-01.md; grep -n "—\|rather\|\*\*" summaries/brudner-2026-01.md docs/pilot-notes/brudner-2026-01.md; git status --short
```

```
119 summaries/brudner-2026-01.md
1466 docs/pilot-notes/brudner-2026-01.md
1585 total
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
?? docs/pilot-notes/brudner-2026-01.md
?? scripts
?? summaries/brudner-2026-01.md
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/brudner-2026-01.md",
 "old_string": "the trained networks and",
 "new_string": "the networks and"
}
```

```
The file summaries/brudner-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote two new files, `docs/pilot-notes/brudner-2026-01.md` and `summaries/brudner-2026-01.md`, and changed nothing else. The summary is 118 words. Some untracked dotfiles and folders (`.bashrc`, `.vscode`, `scripts` and others) were already in the repository root; I left them alone, so they will go into the workflow's commit unless someone removes them. Nothing is committed.

# brudner-2026, Brudner et al. 2026

No claim reproduced, three partially and three not reproduced, with one claim blocked on the dandiset alone and 13 more that also need outside data, plus two claims on data elsewhere (the smooth plume on Dryad), both blocked. The first verification round agreed with 20 of the 22 outcomes as they stood, the second with all 22, two of them only conditionally, and a third round, on the one change proposed after the second, agreed with it. It pins version 0.260630.1657, the only published version and the one the paper's code names. The paper, Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark and Emonet, "Fly navigational responses exploit plume-specific odor motion and gradient cues" in PNAS, shows that the crosswind odor gradient is organized antisymmetrically about the centerline in a smooth plume and odor motion in a complex one, that logistic models and small networks trained to find the centerline pick up the cue of their plume, that agents gain from adding such bilateral detection to a wind-only strategy, and that the crosswind turns of blinded flies with optogenetic odor are predicted by the gradient in the smooth plume and by motion in the complex plume; the dandiset holds 131 behavior files (83 smooth, and two complex sets of 24, "smoke-1a" and "smoke-2a"), a 1500-frame window of the complex plume movie, three freestream windows and a compact asset of the Fig. S1 freestream inputs. The claims were written from the version of record with its SI Appendix and from the paper's code (emonetlab/GradientMotionMultiplePlumes at effc7b0), which holds the Fig. 5E/F analysis written for this dandiset with its published tables, the Fig. 1 and 2 cue and model code and a re-implementation of Fig. 3, and nothing for the agent simulations or Fig. S1. Every claim on the smooth plume, the networks or the agents is blocked as `other`, as the smooth plume could not be read and no agent code exists. Not reproduced are `fig5e-cue-betas` (with the SI's onset and the smoke-1a files no reading passes, 0 of 24, and no file set or onset gives the result in every reading), `figs1fg-resolution-robustness` (motion r 0.729 to 0.820 at a 4-frame delay as stored, below 0.8 in every reading, and gradient r 0.613 at 12 pixels without smoothing) and `figs5c-turn-angles` (medians of -20.8 and +21.3 degrees over the files' turn events against -34.2 and +33.8). Partial are `fig2c-complex-auc` (motion AUC 0.603 above gradient 0.560, neither within tolerance, resting on an assumed mirror balancing of the samples), `fig2e-complex-weights` (|motion| 0.426 above |gradient| 0.262, against 0.098 +/- 0.041) and `fig5f-cue-dominance` (smooth 0.937 within tolerance, complex -0.492 outside -0.662 +/- 0.066, resting on the smoke-1a files and the SI onset). `methods-intensity-right-bias` is blocked as `metadata_insufficient`: it holds under every reading if -1 is a right turn and fails under every reading if +1 is. The freestream and complex parts of the two Fig. S1 claims hold (index -2.93, -1.53 and +0.04 at 5, 10 and 20 cm/s and 4.40 complex), as does the complex part of `figs2c-one-frame-delay`, but the claims stay blocked. The author's first run gave three reproduced (all on assumptions: the SI onset with the smoke-2a files for Fig. 5, and a turn end at 20% of the peak for Fig. S5C), two partially, one not reproduced and 16 blocked. The author asked a reader nothing, so the answer and author-answers runs changed nothing. Round 1 disagreed on fig5e (not reproduced, as the result depends on the reading) and fig5f, doubted the smoke-2a choice, since the dandiset's description says smoke_1a_orig was analysed throughout the paper, found that the onset rule ignored the sign of the rotation and asked for the decidable Fig. S1 parts; in reply the smoke-1a files became the assumed complex plume, fig5e moved to not reproduced and fig5f to partially reproduced, against the verifier, the onset rule was fixed (the old one reversed in 0.2% of turns), fits per projection flip and a comparison with the code's published tables were added, and a reader was asked whether the dataset's turn start is the SI's onset. Round 2 agreed with all 22, with fig5f and figs5c only conditionally, found sentences the outputs did not support (that the complex motion cue never reaches significance, that only smoke-1a matches the published tables, that the sets do not differ by a flip convention, 1011 trajectories where the output prints 1010) and asked for a test of the cue signs against the plume geometry, which could not tell the two sets apart; the author removed the assumption flag of fig5e, ran the half-height turn bounds (medians -25.0 to -26.6 and +26.8 to +27.7), proposed not reproduced for figs5c and put three more questions to a reader. Round 3 reviewed only that proposal and agreed. The author's run took about 1 h 40 min (04:15 to 05:56 UTC); a development run peaked at 11.9 GB of memory, fixed before the clean runs, which peaked at 7.1 GB, and the notebook ran in 735 s at first, 19 minutes after round 1, 823 s after round 2 and 929 s at the end. Untracked dotfiles in the repository root, which the author did not create, were left alone.

The smooth plume movie, used by 15 of the paper's 22 claims, is not in the dandiset; the description points to Dryad (doi:10.5061/dryad.g27mq71), which answers 401 to downloads without an API token, and the paper's own rescaled version is in neither the dandiset nor its Yale Dataverse deposit. The complex-plume behavior files come in two sets, smoke-1a and smoke-2a (24 files each, on the same days and vials, each with 12 flipped and 12 unflipped projections), whose session descriptions name two movies and whose signals differ (99th percentile of the intensity 171 and 252, and a motion coefficient positive in one set and negative in the other in both projection flips); nothing says what smoke_2a is, the dandiset's description says smoke_1a_orig was analysed throughout the paper, and the code selects smoke-2a only, so a sign convention differing between the sets cannot be ruled out. The code's published Fig. 5E and 5F tables are matched most closely by the smoke-1a files with the dataset's turn start and 160 to 200 degrees (within 0.1 SE, all four log-likelihoods within 0.001 per turn), not by the smoke-2a files with 150 to 210 degrees that the code names, which give a motion coefficient of -0.0119 (p 0.15) and a cue dominance of +0.388 where the tables give +0.0441 and -0.662. The turn events are not described: they start a median of 4 frames (about 67 ms) after the SI's onset and stop a median of 4 frames before the falling 20% crossing, so turns over the events measure about 21 degrees against the paper's 34. The turn direction (+1 or -1) is not mapped to left or right, and the heading, said to be in standardized arena coordinates, is atan2(-vy, vx), so the rightward bias towards the projector cannot be tested. No file gives the movie frame shown at a trajectory frame, so the odor signals cannot be aligned with the deposited complex window, whose provenance names a preprocessing run 'bgsub_gauss3_fullslice_p001_p99' that may differ from the movie the paper analysed. odor_velocity is NaN on 95 to 98% of frames, which its description does not explain. Four smooth-plume files hold 10 frames with y of 768 to 814 mm in an arena 170 mm wide, 205 of 7235 trajectories have no position at all, and in 47 files some trajectories carry timestamps and others a starting time and rate. Questions are put to the paper's authors: which complex files are the complex plume of Fig. 5 and what smoke_2a is; which turn onset Fig. 5E-F used; how the Fig. 2 and 3 samples were balanced; where a turn ends for Fig. S5C; how the Fig. S1G motion cue is defined and whether the maps were smoothed; whether the Fig. 5 predictors were z-scored over all frames or per trajectory; and whether the two complex sets share a sign convention.

The author's points on the protocol: the Dryad file was not staged although `docs/archives.md` says it would be, and no `blocked_by` value fits data that are public but cannot be fetched; `entry.py lock` writes a `python:` field the entry schema rejects; `entry.py check` requires `about:` on findings whose `about` the attempt schema forbids; it does not say how to combine readings of several independent open details, or whether a reading the author adds counts under "one reading"; the rule for `measured` does not cover an added reading; the clock check cannot be done when the files hold no stimulus frame index; it does not say whether to compute the decidable parts of a claim blocked anyway; and the fig5e criterion tests significance but not sign.

---

None of the paper's main findings was fully confirmed in this data, and most could not be tested. The plume-specific organization of gradient and motion cues, the networks and the navigating agents could not be tested, because the smooth plume movie is not in the dataset. In the complex plume, motion predicted the centerline side better than the gradient, but the model values missed the paper's. Fly turns followed the gradient in the smooth plume, but the complex-plume motion effect did not hold in every reading and its dominance held only in part, as the dataset holds two undocumented complex-plume file sets. Minor claims on cue robustness and turn size (about 21 against 34 degrees) did not reproduce.

## End of run

17 turns, 2 minutes, $1.10 at API prices, result: success.
