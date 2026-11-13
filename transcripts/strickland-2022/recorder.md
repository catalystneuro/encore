# strickland-2022 · recorder · run 43359003389

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py strickland-2022; ls transcripts/strickland-2022/; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/ashworth-2025-01.md
docs/pilot-notes/athalye-2023-01.md
docs/pilot-notes/azcorra-2023-01.md
| [CRCNS:bst-3](https://crcns.org/data-sets/bst/bst-3) | [Strickland et al. 2022](https://doi.org/10.1038/s41467-022-34021-1) | 22 | 6 | 1 | 0 | [`strickland-2022`](entries/strickland-2022) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
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
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
grep -m3 -B2 "^| \[" README.md | head -5; for f in docs/pilot-notes/{amjad-2025,armstrong-2026,ashworth-2025,athalye-2023,azcorra-2023}-01.md; do echo "== $f"; cat $f; done; for f in summaries/{amjad-2025,armstrong-2026}-01.md; do echo "== $f"; cat $f; done
```

```
<persisted-output>
Output too large (37.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/bmr3foxji.txt

Preview (first 2KB):
== docs/pilot-notes/amjad-2025-01.md
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

**Agent calls Bash**

```bash
cat attempts/strickland-2022-01.yaml claims/strickland-2022.yaml; grep -n -A12 '"bst-3\|strickland' targets/dandisets.json
```

```
<persisted-output>
Output too large (110.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/b5hyt1ani.txt

Preview (first 2KB):
schema_version: 3
id: strickland-2022-01
datasets:
- archive: crcns
  id: bst-3
  version: unversioned
  doi: 10.6080/K0Q23XGR
  relation: primary
paper: doi:10.1038/s41467-022-34021-1
date: 2026-11-13
entry: strickland-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/strickland-2022; for f in author-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md claims-check-report.md claims-report.md verifier-1-report.md verifier-2-report.md answer-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (38.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/bmrisk02f.txt

Preview (first 2KB):
=== author-report.md
I've completed author steps 1 to 6 for `strickland-2022`. `python tools/entry.py all` reports 0 errors and the notebook passes on a clean run in 99 s. The handover package is in `executed/strickland-2022/handover/`. Nothing is committed.

**1. Outcomes (30 claims, none blocked)**

| Claim | Outcome |
|---|---|
| source-data-cluster-link | reproduced (all 1812 cue and outcome rows match exactly one unit) |
| fig1c-suppression-order | reproduced (F(2,142) = 147.9) |
| figs2-each-rat-discriminates | reproduced (reading c-c, 8 of 8 rats) |
| units-sessions-subjects | reproduced |
| fig1e-regions | reproduced |
| fig2b-cue-clusters | reproduced |
| fig2c-cue-pc1-ordered | reproduced (29.73%) |
| fig2c-pc1-contribution | reproduced |
| fig2d-danger-latency | not reproduced (R2 = 0.067, p = 0.26) |
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/bmr3foxji.txt"
}
```

```
1	== docs/pilot-notes/amjad-2025-01.md
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
[... 497 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/b5hyt1ani.txt"
}
```

```
1	schema_version: 3
2	id: strickland-2022-01
3	datasets:
4	- archive: crcns
5	  id: bst-3
6	  version: unversioned
7	  doi: 10.6080/K0Q23XGR
8	  relation: primary
9	paper: doi:10.1038/s41467-022-34021-1
10	date: 2026-11-13
11	entry: strickland-2022
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 837 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/b5hyt1ani.txt",
 "offset": 858,
 "limit": 300
}
```

```
858	    outcome: partially_reproduced
859	    reason: Agrees. The Result sentences, the Summary, the README and the record's notes and findings
860	      agree with the printed outputs.
861	    response: No change.
862	  - claim: fig4c-positive-prediction-error
863	    agrees: true
864	    outcome: reproduced
865	    reason: Agrees. The Result sentences, the Summary, the README and the record's notes and findings
866	      agree with the printed outputs.
867	    response: No change.
868	  - claim: fig4b-phasic-network
869	    agrees: true
870	    outcome: partially_reproduced
871	    reason: Agrees, settled from round 1. Judged with Pearson r, as the criterion says, every profile part
872	      holds and the network part fails (within -0.329 against 0.008), which is partial. The criterion
873	      allows only r where the fig2e one allows r and r squared; with r squared the claim would be
874	      reproduced. This is a claims-file inconsistency, now referred to a reader.
875	    response: No change of outcome. The conclusion now gives k3's anticorrelation with k1 and k2 (r
876	      = -0.85, -0.74) as the reason the phasic network fails.
877	  - claim: fig4b-tonic-network
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('bst-3' in str(v) for v in x.values() if not isinstance(v,(dict,list))): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
(Bash completed with no output)
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b9206493-b1b3-4e3c-9429-44f26df5d572/tool-results/bmrisk02f.txt"
}
```

```
1	=== author-report.md
2	I've completed author steps 1 to 6 for `strickland-2022`. `python tools/entry.py all` reports 0 errors and the notebook passes on a clean run in 99 s. The handover package is in `executed/strickland-2022/handover/`. Nothing is committed.
3	
4	**1. Outcomes (30 claims, none blocked)**
5	
6	| Claim | Outcome |
7	|---|---|
8	| source-data-cluster-link | reproduced (all 1812 cue and outcome rows match exactly one unit) |
9	| fig1c-suppression-order | reproduced (F(2,142) = 147.9) |
10	| figs2-each-rat-discriminates | reproduced (reading c-c, 8 of 8 rats) |
11	| units-sessions-subjects | reproduced |
12	| fig1e-regions | reproduced |
13	| fig2b-cue-clusters | reproduced |
14	| fig2c-cue-pc1-ordered | reproduced (29.73%) |
15	| fig2c-pc1-contribution | reproduced |
16	| fig2d-danger-latency | not reproduced (R2 = 0.067, p = 0.26) |
17	| fig2e-cue-subnetwork | reproduced (with r squared) |
18	| fig2f-cue-hubs | partially reproduced, rests on an assumption |
19	| fig2g-cue-anatomy | reproduced |
20	| fig3a-cluster-signals | partially reproduced (2 of 4 shapes) |
[... 303 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "bst-3|strickland|K0Q23XGR",
 "path": "targets/dandisets.json",
 "output_mode": "content",
 "-C": 12
}
```

```
No matches found
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/strickland-2022-01.md",
 "content": "# strickland-2022, Strickland et al. 2022\n\nTwenty-two claims reproduced (two on an assumption), six partially (one on an\nassumption), one not reproduced and none blocked, plus one claim linking the\ndata set to the paper's Source Data cluster sheets, reproduced (all 1812 cue\nrows and 1812 outcome rows match exactly one unit, largest difference 5e-15).\nThe first verification round agreed with 26 of the 30 outcomes as they stood\nand the second with all 30; nothing was proposed after the second, so there\nwas no third round. The data set is CRCNS bst-3, which is not versioned. The\npaper, Strickland and McDannald, \"Brainstem networks construct threat\nprobability and prediction error from neuronal building blocks\" in Nature\nCommunications, records 1812 brainstem units from ten rats in 73 sessions of\nprobabilistic fear discrimination with danger, uncertainty and safety cues,\nclusters the units by their cue and outcome firing with k-means, and uses PCA,\nregression on threat probability, behaviour, shock and prediction error, and\nshuffle lesions to describe a cue subnetwork and phasic and tonic outcome\nnetworks; the data set holds the 1812 unit files, a cube file and the paper's\nMATLAB scripts. The claims were written from the version of record\n(PMC9582012) with its Supplementary Information and Source Data workbook,\nwithout reading the scripts in the data set; the author followed the scripts\nwhere the Methods leave a detail open, and took the paper's cluster membership\nfrom the Source Data, as the data set holds none. Every claim could be tested.\n`fig2d-danger-latency` is not reproduced: with the latency searched within the\n10-s cue, as the Supplementary Methods say, its correlation with PC1\ncontribution is weak and not significant (R2 = 0.067, p = 0.26), and no\nreading tried reproduces the Source Data latencies. Partial are\n`fig2f-cue-hubs` (on danger firing k1 does not exceed k3 or k4; it rests on r\nsquared, and with r it would not be reproduced), `fig3a-cluster-signals` (two\nof four shapes), `fig3c-subnetwork-lesion` (the behaviour weight after the\nsubnetwork lesion, 0.264, is not above the one after the supranetwork lesion,\n0.268, over ten further runs as well), `fig4b-outcome-clusters` (median\nsmallest cluster 29 against 46 +- 4.6) and `fig4b-phasic-network` and\n`fig4b-tonic-network`, whose network part fails with the Pearson r the\ncriterion names (-0.329 against 0.008 and -0.250 against 0.000) and holds\nwith r squared. `fig5e-no-anatomical-bias` is reproduced on the reading behind\nSource Data Fig. 5e (phasic as k1 to k5), which passes by construction, as its\nthreshold is the largest Source Data value of the same quantity; with the\nResults' phasic network (k1 to k3) the largest differential is 9.82 and the\nclaim would not be reproduced. `cue-outcome-membership-independent` is judged\non the paper's own membership; on the attempt's own k-means it holds in 4 of\n20 seeds. The author's first run had the fig4b network claims reproduced on r\nsquared. The reader's answer run stopped without changes because no questions\nfile existed (the record's notes said \"The question is in the findings\",\nmeaning questions for the paper's authors), and the author-answers run only\nreworded those notes. Round 1 disagreed on `fig2c-pc1-contribution` (the\nattempt's own clusters rested on one seed), the two fig4b network claims and\nfig5e; in reply the network claims were judged on r and became partial,\nfig2c-pc1-contribution was rerun on all 20 seeds (median 481 units, within\n505 +- 50.5) and kept, fig5e was kept and marked as resting on an assumption\nwith a permutation reference added, the cube's 500-ms firing was recomputed\nfrom the spike times (largest difference 9.5e-13), the cited script passages\nwere printed, and `questions/strickland-2022.yaml` was written with three\nquestions to a reader (the fig4b coefficient, the fig5e threshold and phasic\nset, and loadings for fig3c). Round 2 agreed with all 30, asked for the\ncue-outcome claim to be marked as resting on an assumption, and found four\nsentences the outputs did not support (fig3d's peak in the first cue second,\nnot the second; k6 as the only cluster inhibited to surprising shock; an\nincomplete reason for the tonic network's failure; and both of fig5b's L2\ncomponents called out of tolerance), all corrected. The author's run took\nabout 40 minutes (01:09 to 01:48 UTC) and nothing failed in the final run;\nthe notebook ran in 99 s at first, 5.9 min after round 1 and 380 s at the end.\nUntracked dotfiles and a root `scripts/` directory that were already there\nwere left alone.\n\nThe data set holds no cluster membership, and the paper's clusters cannot be\nregenerated outside MATLAB, as they come from MATLAB's kmeans after rng(1) and\nare relabelled by hand-written maps in cueAnalysis.m and outcomeAnalysis.m;\nthey can be recovered only from the paper's Source Data workbook, whose\ncluster sheets every unit matches exactly. The normalization in cubeScript.m\n(1-s, 500-ms and 250-ms bins z-scored separately over the 40 s from 10 s\nbefore cue onset, baseline rounded down) differs from the Supplementary\nMethods (250-ms bins from 20 s before to 20 s after the cue, averaged into\nlarger intervals), and only the script's reproduces the paper's values; the\nlesion scripts shuffle firing of k1 to k9, k1 to k3 and k6 to k9 before\nregression, where the Methods shuffle the betas of clusters 1 to 8, and the\nShuffle function itself is not in the data set. The Source Data danger\nlatencies of Fig. 2d do not follow the Supplementary Methods' search (k1 mean\n182 ms there, 4046 ms with the stated method), cover 1498 of 1812 units by a\nrule not stated, and none of the scripts computes the latency. Source Data\nFig. 2c inset and Fig. 4c hold the units' rows with a pre-cue baseline\nsubtracted, not the matrices whose PCA gives the reported 29.7% and 17.7%\n(PCA of those sheets gives 47.1% and 24.2%). For the cue hubs the\nSupplementary Methods correlate danger firing over 14 intervals, but the\nSource Data values are squared correlations of the full 42-value cue rows; the\nMethods call the cluster correlations \"Pearson's correlation coefficient (R2)\"\nand the scripts plot r squared, and with r the outcome networks do not\nseparate. The cube's region names are MATLAB string objects that cannot be read\noutside MATLAB, the region numbers need the list in cubeScript.m, the scripts\nrenumber 35 units from region 21 (CIC) to DpWh and merge regions 11 and 24\ninto x/scp, and the units of anatomy.x, y and z are not stated. 204 of the\n1812 unit files hold repeated spike times (9289 repeats in all), which the\ncube's counts leave out. In session js10030220, 19 unit files share one set of\nevent times, while 3 others carry cue and poke times that drift from them to\nabout 0.28 and 0.30 s over the session. Session js27101920 has 5 shock times,\nwith none on its first danger trial, where the other 72 sessions have 6.\nSupplementary Table 1 lists 75 sessions, where the Results and the data set\nhave 73. The Supplementary Methods put shock first in the outcome beta matrix,\nwhere outcomeRegression.m and Source Data put prediction error first, and\nSource Data Fig. 4f right swaps the labels of k7 and k8, as outcomeAnalysis.m\nhard-codes them. Questions are put to the paper's authors: how the latencies\nwere computed and which units were left out, whether r or r squared was\naveraged for the hubs and over which cues, and whether the network separation\nis judged on r squared.\n\nThe author's points on the protocol: data.zip is opened in place, so the MD5\nthat CRCNS asks for cannot be checked; it does not say whether an author may\nadd a reading to a link criterion, as was done with the scripts'\nnormalization; its precedence order does not cover Source Data that\ncontradict the Methods; criteria with separate rules for the paper's clusters\nand the author's own k-means do not say which decides; a claim of absence\nwith no test in the paper but two readings was judged on the reading behind\nthe Source Data; and the per-animal breakdown fits poorly when results are per\ncluster.\n"
}
```

```
File created successfully at: docs/pilot-notes/strickland-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/strickland-2022-01.md",
 "old_string": "sentences the outputs did not support (fig3d's peak in the first cue second,\nnot the second; k6",
 "new_string": "sentences the outputs did not support (fig3d's PC2 probability peak placed\nin the first cue second where it is in the second; k6"
}
```

```
The file docs/pilot-notes/strickland-2022-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/strickland-2022-01.md",
 "content": "Most of the paper's main findings held up in this data, using the paper's own cluster membership from its Source Data. Cue clusters ordered by threat probability, the cue subnetwork carrying threat probability and behaviour signals, and the phasic and tonic outcome networks signalling shock and prediction error all reproduced. The link between faster danger responses and larger contribution to the threat signal did not (R2 = 0.067), as the paper's latencies do not follow its stated method and no script computes them. The cue hubs, the subnetwork lesion and the separation of the outcome networks held only in part; the networks separate with squared correlations but not with Pearson r. Every claim could be tested.\n"
}
```

```
File created successfully at: summaries/strickland-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='summaries/strickland-2022-01.md'
s=open(p).read()
s=s.replace("and the phasic and tonic outcome networks signalling shock and prediction error all reproduced.","positive prediction error coding, and the shock and prediction error signals of the outcome networks reproduced.")
open(p,'w').write(s)
print(s, len(s.split()))
E
git status --short
```

```
Most of the paper's main findings held up in this data, using the paper's own cluster membership from its Source Data. Cue clusters ordered by threat probability, the cue subnetwork carrying threat probability and behaviour signals, positive prediction error coding, and the shock and prediction error signals of the outcome networks reproduced. The link between faster danger responses and larger contribution to the threat signal did not (R2 = 0.067), as the paper's latencies do not follow its stated method and no script computes them. The cue hubs, the subnetwork lesion and the separation of the outcome networks held only in part; the networks separate with squared correlations but not with Pearson r. Every claim could be tested.
 118
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
?? docs/pilot-notes/strickland-2022-01.md
?? scripts
?? summaries/strickland-2022-01.md
```

**Agent**

I wrote both files and changed nothing else; nothing is committed.

There is no entry for CRCNS bst-3 in `targets/dandisets.json`, so I had no `catalystneuro` field to go on. The second paragraph therefore doesn't open with the CatalystNeuro sentence. Like the amjad-2025 notes, the outcome counts leave the link claim out of the 22 reproduced and report it on its own.

`docs/pilot-notes/strickland-2022-01.md`:

# strickland-2022, Strickland et al. 2022

Twenty-two claims reproduced (two on an assumption), six partially (one on an assumption), one not reproduced and none blocked, plus one claim linking the data set to the paper's Source Data cluster sheets, reproduced (all 1812 cue rows and 1812 outcome rows match exactly one unit, largest difference 5e-15). The first verification round agreed with 26 of the 30 outcomes as they stood and the second with all 30; nothing was proposed after the second, so there was no third round. The data set is CRCNS bst-3, which is not versioned. The paper, Strickland and McDannald, "Brainstem networks construct threat probability and prediction error from neuronal building blocks" in Nature Communications, records 1812 brainstem units from ten rats in 73 sessions of probabilistic fear discrimination with danger, uncertainty and safety cues, clusters the units by their cue and outcome firing with k-means, and uses PCA, regression on threat probability, behaviour, shock and prediction error, and shuffle lesions to describe a cue subnetwork and phasic and tonic outcome networks; the data set holds the 1812 unit files, a cube file and the paper's MATLAB scripts. The claims were written from the version of record (PMC9582012) with its Supplementary Information and Source Data workbook, without reading the scripts in the data set; the author followed the scripts where the Methods leave a detail open, and took the paper's cluster membership from the Source Data, as the data set holds none. Every claim could be tested. `fig2d-danger-latency` is not reproduced: with the latency searched within the 10-s cue, as the Supplementary Methods say, its correlation with PC1 contribution is weak and not significant (R2 = 0.067, p = 0.26), and no reading tried reproduces the Source Data latencies. Partial are `fig2f-cue-hubs` (on danger firing k1 does not exceed k3 or k4; it rests on r squared, and with r it would not be reproduced), `fig3a-cluster-signals` (two of four shapes), `fig3c-subnetwork-lesion` (the behaviour weight after the subnetwork lesion, 0.264, is not above the one after the supranetwork lesion, 0.268, over ten further runs as well), `fig4b-outcome-clusters` (median smallest cluster 29 against 46 +- 4.6) and `fig4b-phasic-network` and `fig4b-tonic-network`, whose network part fails with the Pearson r the criterion names (-0.329 against 0.008 and -0.250 against 0.000) and holds with r squared. `fig5e-no-anatomical-bias` is reproduced on the reading behind Source Data Fig. 5e (phasic as k1 to k5), which passes by construction, as its threshold is the largest Source Data value of the same quantity; with the Results' phasic network (k1 to k3) the largest differential is 9.82 and the claim would not be reproduced. `cue-outcome-membership-independent` is judged on the paper's own membership; on the attempt's own k-means it holds in 4 of 20 seeds. The author's first run had the fig4b network claims reproduced on r squared. The reader's answer run stopped without changes because no questions file existed (the record's notes said "The question is in the findings", meaning questions for the paper's authors), and the author-answers run only reworded those notes. Round 1 disagreed on `fig2c-pc1-contribution` (the attempt's own clusters rested on one seed), the two fig4b network claims and fig5e; in reply the network claims were judged on r and became partial, fig2c-pc1-contribution was rerun on all 20 seeds (median 481 units, within 505 +- 50.5) and kept, fig5e was kept and marked as resting on an assumption with a permutation reference added, the cube's 500-ms firing was recomputed from the spike times (largest difference 9.5e-13), the cited script passages were printed, and `questions/strickland-2022.yaml` was written with three questions to a reader (the fig4b coefficient, the fig5e threshold and phasic set, and loadings for fig3c). Round 2 agreed with all 30, asked for the cue-outcome claim to be marked as resting on an assumption, and found four sentences the outputs did not support (fig3d's PC2 probability peak placed in the first cue second where it is in the second; k6 as the only cluster inhibited to surprising shock; an incomplete reason for the tonic network's failure; and both of fig5b's L2 components called out of tolerance), all corrected. The author's run took about 40 minutes (01:09 to 01:48 UTC) and nothing failed in the final run; the notebook ran in 99 s at first, 5.9 min after round 1 and 380 s at the end. Untracked dotfiles and a root `scripts/` directory that were already there were left alone.

The data set holds no cluster membership, and the paper's clusters cannot be regenerated outside MATLAB, as they come from MATLAB's kmeans after rng(1) and are relabelled by hand-written maps in cueAnalysis.m and outcomeAnalysis.m; they can be recovered only from the paper's Source Data workbook, whose cluster sheets every unit matches exactly. The normalization in cubeScript.m (1-s, 500-ms and 250-ms bins z-scored separately over the 40 s from 10 s before cue onset, baseline rounded down) differs from the Supplementary Methods (250-ms bins from 20 s before to 20 s after the cue, averaged into larger intervals), and only the script's reproduces the paper's values; the lesion scripts shuffle firing of k1 to k9, k1 to k3 and k6 to k9 before regression, where the Methods shuffle the betas of clusters 1 to 8, and the Shuffle function itself is not in the data set. The Source Data danger latencies of Fig. 2d do not follow the Supplementary Methods' search (k1 mean 182 ms there, 4046 ms with the stated method), cover 1498 of 1812 units by a rule not stated, and none of the scripts computes the latency. Source Data Fig. 2c inset and Fig. 4c hold the units' rows with a pre-cue baseline subtracted, not the matrices whose PCA gives the reported 29.7% and 17.7% (PCA of those sheets gives 47.1% and 24.2%). For the cue hubs the Supplementary Methods correlate danger firing over 14 intervals, but the Source Data values are squared correlations of the full 42-value cue rows; the Methods call the cluster correlations "Pearson's correlation coefficient (R2)" and the scripts plot r squared, and with r the outcome networks do not separate. The cube's region names are MATLAB string objects that cannot be read outside MATLAB, the region numbers need the list in cubeScript.m, the scripts renumber 35 units from region 21 (CIC) to DpWh and merge regions 11 and 24 into x/scp, and the units of anatomy.x, y and z are not stated. 204 of the 1812 unit files hold repeated spike times (9289 repeats in all), which the cube's counts leave out. In session js10030220, 19 unit files share one set of event times, while 3 others carry cue and poke times that drift from them to about 0.28 and 0.30 s over the session. Session js27101920 has 5 shock times, with none on its first danger trial, where the other 72 sessions have 6. Supplementary Table 1 lists 75 sessions, where the Results and the data set have 73. The Supplementary Methods put shock first in the outcome beta matrix, where outcomeRegression.m and Source Data put prediction error first, and Source Data Fig. 4f right swaps the labels of k7 and k8, as outcomeAnalysis.m hard-codes them. Questions are put to the paper's authors: how the latencies were computed and which units were left out, whether r or r squared was averaged for the hubs and over which cues, and whether the network separation is judged on r squared.

The author's points on the protocol: data.zip is opened in place, so the MD5 that CRCNS asks for cannot be checked; it does not say whether an author may add a reading to a link criterion, as was done with the scripts' normalization; its precedence order does not cover Source Data that contradict the Methods; criteria with separate rules for the paper's clusters and the author's own k-means do not say which decides; a claim of absence with no test in the paper but two readings was judged on the reading behind the Source Data; and the per-animal breakdown fits poorly when results are per cluster.

`summaries/strickland-2022-01.md` (118 words):

Most of the paper's main findings held up in this data, using the paper's own cluster membership from its Source Data. Cue clusters ordered by threat probability, the cue subnetwork carrying threat probability and behaviour signals, positive prediction error coding, and the shock and prediction error signals of the outcome networks reproduced. The link between faster danger responses and larger contribution to the threat signal did not (R2 = 0.067), as the paper's latencies do not follow its stated method and no script computes them. The cue hubs, the subnetwork lesion and the separation of the outcome networks held only in part; the networks separate with squared correlations but not with Pearson r. Every claim could be tested.

## End of run

15 turns, 2 minutes, $1.03 at API prices, result: success.
