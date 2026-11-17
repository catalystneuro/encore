# nishimoto-2011 · recorder · run 43614423184

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; echo; python tools/readme_row.py nishimoto-2011; ls transcripts/nishimoto-2011/; cat attempts/nishimoto-2011-01.yaml; cat claims/nishimoto-2011.yaml
```

```
<persisted-output>
Output too large (83.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/blgm21sx6.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md

| [CRCNS:mt-2](http://crcns.org/data-sets/vc/mt-2) | [Nishimoto et al. 2011](https://doi.org/10.1523/jneurosci.6801-10.2011) | 14 | 3 | 2 | 1 | [`nishimoto-2011`](entries/nishimoto-2011) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
[... 46 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/blgm21sx6.txt"
}
```

```
1	docs/pilot-notes/amjad-2025-01.md
2	docs/pilot-notes/andrews-2024-01.md
3	docs/pilot-notes/armstrong-2026-01.md
4	docs/pilot-notes/asari-2009-01.md
5	docs/pilot-notes/ashworth-2025-01.md
6	
7	| [CRCNS:mt-2](http://crcns.org/data-sets/vc/mt-2) | [Nishimoto et al. 2011](https://doi.org/10.1523/jneurosci.6801-10.2011) | 14 | 3 | 2 | 1 | [`nishimoto-2011`](entries/nishimoto-2011) |
8	answer-report.md
9	answer.md
10	author-answers-report.md
11	author-answers.md
12	author-report.md
13	author-revise-1-report.md
14	author-revise-1.md
15	author-revise-2-report.md
16	author-revise-2.md
17	author.md
18	claims-check-report.md
19	claims-check.md
20	claims-report.md
[... 873 more lines not kept]
```

**Agent calls Bash**

```bash
grep -nE "^- id:|^  source:" claims/nishimoto-2011.yaml; head -n 30 README.md | grep -n "|" | head -5
```

```
78:- id: fig3b-mean-prediction
81:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
97:- id: fig3b-explainable-variance
100:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
118:- id: fig3a-example-neuron
121:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
135:- id: fig2b-contrast-normalization-no-effect
139:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
162:- id: fig2b-compressive-improves
165:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
197:- id: fig2b-expansive-decreases
200:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
226:- id: fig2b-divisive-improves
229:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
250:- id: fig2b-compressive-divisive-best
254:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
278:- id: fig2b-no-interaction
281:  source: Results, Linear and nonlinear mechanisms that predict natural visual responses in area
295:- id: complex-cells-dominate
298:  source: Materials and Methods, The V1 filter bank, paragraph 3 (data not shown)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01; do echo "=== $f"; cat $f.md; done; cd ../..; ls summaries | head; for f in $(ls summaries | head -3); do echo "== $f"; cat summaries/$f; done
```

```
<persisted-output>
Output too large (39KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/bjegjtgwo.txt

Preview (first 2KB):
=== amjad-2025-01
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/bjegjtgwo.txt"
}
```

```
1	=== amjad-2025-01
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
[... 529 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/nishimoto-2011; wc -c *-report.md; ls -l --time-style=full-iso *-report.md; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (it if isinstance(it,list) else it.values()):
  s=json.dumps(x)
  if 'mt-2' in s: print(s)
"
```

```
957 answer-report.md
 2257 author-answers-report.md
 5966 author-report.md
 3716 author-revise-1-report.md
 4105 author-revise-2-report.md
 2745 claims-check-report.md
 4717 claims-report.md
 9922 verifier-1-report.md
 7049 verifier-2-report.md
41434 total
-rw-r--r-- 1 runner runner  957 2026-11-14 16:13:51.813637579 +0000 answer-report.md
-rw-r--r-- 1 runner runner 2257 2026-11-14 16:13:51.814637587 +0000 author-answers-report.md
-rw-r--r-- 1 runner runner 5966 2026-11-14 16:13:51.814637587 +0000 author-report.md
-rw-r--r-- 1 runner runner 3716 2026-11-14 16:13:51.814637587 +0000 author-revise-1-report.md
-rw-r--r-- 1 runner runner 4105 2026-11-14 16:13:51.814637587 +0000 author-revise-2-report.md
-rw-r--r-- 1 runner runner 2745 2026-11-14 16:13:50.689112962 +0000 claims-check-report.md
-rw-r--r-- 1 runner runner 4717 2026-11-14 16:13:50.689383028 +0000 claims-report.md
-rw-r--r-- 1 runner runner 9922 2026-11-14 16:13:51.816637601 +0000 verifier-1-report.md
-rw-r--r-- 1 runner runner 7049 2026-11-14 16:13:51.816637601 +0000 verifier-2-report.md
```

**Agent calls Bash**

```bash
grep -n -i -B3 -A12 "mt-2\|nishimoto" targets/dandisets.json | head -60; cd transcripts/nishimoto-2011; for f in author answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat $f-report.md; done
```

```
<persisted-output>
Output too large (33.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/bji021idi.txt

Preview (first 2KB):
=== author
I've finished steps 1 to 6 for nishimoto-2011. The entry is in `entries/nishimoto-2011/`, the record is `attempts/nishimoto-2011-01.yaml`, and the verifier's package is in `executed/nishimoto-2011/handover/`. `check` reports 0 errors, and `all` passed in 3203 s.

The main caveat: the paper's full model doesn't fit in the time limit, so every outcome below comes from a smaller version of it. The filter bank follows the paper's rules (about 7000 complex and 1100 simple filters), but the regression weights are pooled over space onto 763 inputs. Every tested outcome is marked `assumed: true`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| fig3b-mean-prediction | not reproduced: mean r = 0.448, needed 0.468 to 0.572; no reading reaches it |
| fig3b-explainable-variance | blocked, data_missing: the files hold only repeat-averaged responses |
| fig3a-example-neuron | reproduced: 3 neurons have r of 0.71 to 0.73 |
| fig2b-contrast-normalization-no-effect | reproduced: corrected p = 1 |
| fig2b-compressive-improves | partially reproduced: significant, but 4.6% and 8.4% against 16% and 19% |
| fig2b-expansive-decreases | partially reproduced: significant, one of the two sizes outside tolerance |
| fig2b-divisive-improves | not reproduced: corrected p = 0.056 |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6588072f-7c69-475d-a5ec-e85c8161d719/tool-results/bji021idi.txt"
}
```

```
1	=== author
2	I've finished steps 1 to 6 for nishimoto-2011. The entry is in `entries/nishimoto-2011/`, the record is `attempts/nishimoto-2011-01.yaml`, and the verifier's package is in `executed/nishimoto-2011/handover/`. `check` reports 0 errors, and `all` passed in 3203 s.
3	
4	The main caveat: the paper's full model doesn't fit in the time limit, so every outcome below comes from a smaller version of it. The filter bank follows the paper's rules (about 7000 complex and 1100 simple filters), but the regression weights are pooled over space onto 763 inputs. Every tested outcome is marked `assumed: true`.
5	
6	**1. Outcomes**
7	
8	| Claim | Outcome |
9	|---|---|
10	| fig3b-mean-prediction | not reproduced: mean r = 0.448, needed 0.468 to 0.572; no reading reaches it |
11	| fig3b-explainable-variance | blocked, data_missing: the files hold only repeat-averaged responses |
12	| fig3a-example-neuron | reproduced: 3 neurons have r of 0.71 to 0.73 |
13	| fig2b-contrast-normalization-no-effect | reproduced: corrected p = 1 |
14	| fig2b-compressive-improves | partially reproduced: significant, but 4.6% and 8.4% against 16% and 19% |
15	| fig2b-expansive-decreases | partially reproduced: significant, one of the two sizes outside tolerance |
16	| fig2b-divisive-improves | not reproduced: corrected p = 0.056 |
17	| fig2b-compressive-divisive-best | reproduced |
18	| fig2b-no-interaction | reproduced |
19	| complex-cells-dominate | reproduced |
20	| fig6a-null-on-plane | reproduced in 12 of 40 combinations of readings |
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "" targets/dandisets.json; grep -n -i "crcns" targets/dandisets.json | head; grep -n -A10 '"mt-2\|mt_2\|mt2' targets/dandisets.json | head -30
```

```
8341
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/nishimoto-2011-01.md",
 "content": "# nishimoto-2011, Nishimoto et al. 2011\n\nFourteen claims reproduced, three partially, two not reproduced and one\nblocked, for missing data; all 19 tested outcomes rest on an assumption.\nThe first verification round agreed with all 20 outcomes as they then\nstood and the second with all 20; nothing was proposed after the second,\nso there was no third round. CRCNS data sets carry no version, so the\nrecord gives `unversioned`. The paper, Nishimoto and Gallant in the\nJournal of Neuroscience (31:14551-14564), records 52 MT neurons in two\nmacaques watching motion-enhanced natural movies and fits a V1 filter\nmodel with a compressive nonlinearity and divisive normalization, then\nreports that the excitatory spectral receptive fields lie on a plane, the\nsuppressive ones off it, that most neurons form a partial ring, and that\nthe horizontal-vertical ratio of the ring correlates with simulated\npattern selectivity. The claims were written from a text extraction of\nthe version of record, with figures read from the PDF; the paper links no\ncode. The paper's model does not fit in the time limit, so every tested\nclaim uses a reduced one: the filter bank follows the paper's rules (7025\ncomplex and 1082 simple channels), but the regression weights are pooled\nover space, onto 763 regressors (2 x 2 regions) for most analyses and 1465\n(3 x 3 regions) where the paper fits a weight for each of 5956 filters.\nReproduced are the mean prediction (0.518 with the 3 x 3 pooling, within\n0.468 to 0.572; 0.448 with the 2 x 2 pooling under every reading), the\nexample neuron, the compressive and divisive model as best (0.448 against\n0.432, better in 34 of 45), the lack of effect of contrast normalization\nand of interaction, the dominance of complex cells, the excitatory\non-plane ratio (0.592, all 40 combinations of readings), the null and\nsuppressive ratios (0.395, at the upper edge, and 0.168, in 6 of 40\ncombinations), the partial ring, the pattern index, the absent correlation\nbetween prediction and pattern index, the natural-movie control (0.523 and\n0.563, p = 0.43, 14 neurons) and the recovery of simulated fields. The\npattern index reproduces only on responses rectified as firing rates, an\nassumption adopted after the raw outputs failed (medians -8.6 to -10.7),\nand the indices reach the paper's range through the clipping of the tuning\ncurves. Partial are the compressive gains (4.6% and 8.4% against 16 and\n19), the expansive losses (-15.1% and -13.5% against -36 and -24) and the\nabsent correlation between prediction and horizontal-vertical ratio (r =\n-0.281, p = 0.061). Not reproduced are the gain from divisive\nnormalization alone (2.9%, corrected p 0.056 over 11; 0.084 with the 3 x 3\npooling) and the correlation between horizontal-vertical ratio and pattern\nindex (r = 0.231, p = 0.126; none of 64 combinations positive at p <\n0.01). The explainable variance is blocked. The author's first run gave 11\nreproduced, 4 partially, 4 not reproduced and 1 blocked. The author asked\na reader nothing, so the answer and author-answers runs changed nothing.\nRound 1 found that the cost of the pooling was never measured, that the\npattern index was computed on noise-free tuning curves and divided by zero\nfor a pure component cell, and that the boosting step counts were not\nprinted; in reply a second notebook, `finer_pooling.ipynb`, refitted the\nmain model with the 3 x 3 pooling (every neuron better, mean +0.070), the\npattern index was computed on rectified and Poisson-noise responses, the\nstep counts were printed (median 156, none at the cap) with a patience of\n500 as a check (0.449), and fig3b-mean-prediction, natural-movie-control\nand fig7b-pattern-index moved to reproduced. Round 2 found six sentences\nthe outputs did not support, among them that a 4 x 4 pooling did not raise\nthe correlation further on three neurons, where the changes were -0.022,\n-0.046 and +0.025, and asked for the Figure 2B models with the 3 x 3\npooling and the share of clipped directions; in reply a third notebook,\n`finer_pooling_fig2b.ipynb`, refitted four of the 12 models, which changed\nno outcome, a cell showed a median of 25% of directions clipped (Spearman\nrho 0.568 with the change of the index), and the sentences were corrected.\nThe null reading on one neuron's movies under all four combinations was\nrun but took the main notebook to 66 minutes, over the 60-minute limit,\nand is not run. The author's `entry.py all` passed in 3203 s, with the\nnotebook at 53 min and a peak of 5.1 GB per worker; after round 1 the main\nnotebook took 59.1 min and `finer_pooling.ipynb` 26.5. In the second\nrevision `entry.py all` was not run, as the three notebooks take about 140\nminutes and a command is capped at 2 hours; each notebook was run on its\nown (main 65 min, Figure 2B 47 min), so there is no clean-run stamp, the\nfinal markdown was copied into the executed copies after the runs, and\nthe threaded fits moved some values in the third decimal.\n\nThe files hold only the response averaged over repeats, not the single\nrepeats, so the explainable variance the paper reports cannot be computed,\nand `ranges.trange` is empty in every file. The data set holds 45 of the\npaper's 52 MT neurons (34 from monkey f, 11 from monkey v), as its\ndescriptor says, and no recording appears twice. Fourteen files hold a\nfield `ranges.nrange`, the first 2000 frames of a 4000-frame\n`ranges.vrange`, which the descriptor does not describe; its frames carry\nless motion than the rest of `vrange` (median frame difference over\ncontrast 0.225 against 0.325, lower in all 14), consistent with the\npaper's natural movies, whose control used 15 neurons. The denominators of\nthe averaged validation responses imply 10 to 33 repeats per neuron, where\nthe paper reports 5 to 20, and training frames carry denominators up to 5,\nso some were shown more than once, which neither the paper nor the\ndescriptor mentions. Training frames number 17,908 to 40,000 per neuron\n(mean 26,894), where the paper gives 20,000 to 40,000 (mean 27,120), and in\nct0133 (v0395) 12,729 of 19,842 training frames have no response, leaving\n7,093. The descriptor does not say how the response bins are aligned to\nthe frames; with a temporal filter centred on each frame, a delay window\nmoved 3 or 6 frames earlier fits the held-out training data better for 14\nof 45 neurons. In the paper, \"up to 10 frames or 130 ms\" disagree at 83 Hz,\nand the Methods give 20,000 to 40,000 training frames where the Results\ngive 22,000 to 42,000, which matches the training plus validation frames\nof the files. Three questions are put to the paper's authors: the temporal\nenvelope, frequencies and filter counts of the filter bank; the boosting\nstep, stopping rule, semisaturation constant and held-out parts; and the\ngrating and plaid settings of the pattern-index simulation, whether its\nresponses were rectified or noisy, and how the constraints of the optimal\nplane were balanced.\n\nThe author's points on the protocol: a model far over the time limit can\nonly be blocked as `too_large`, and a reduced model was fitted as a\ndeviation instead; the Result lines must sit in the executed notebook but\ncan only be written after the results, which cost two full runs of about\n55 min; any edit to `entry.yaml` invalidates the record of the completed\nrun, so `runtime_minutes` was left at 45 though the run took 53; it is\nunclear which reading to judge a claim of absence on when its measure has\nseveral readings from another claim, and the first was used; the clock\ncheck does not apply without a trial table, and the prediction was\ncompared with the response shifted in time instead; and `check` requires\nthe dataset version to be named in a particular form, so\n`DATASET = \"crcns:mt-2/unversioned\"` was added to the helper.\n"
}
```

```
File created successfully at: docs/pilot-notes/nishimoto-2011-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/nishimoto-2011-01.md",
 "content": "Most of the paper's main findings held up in this data, on a reduced version of its model fitted to 45 of its 52 MT neurons. The compressive and divisive V1 filter model predicted responses as well as reported (mean correlation 0.518 against 0.52) and beat the other models. Excitatory spectral receptive fields lay on a plane, suppressive ones off it, and most formed a partial ring. The link between the horizontal-vertical ratio and simulated pattern selectivity did not reproduce, in a simulation whose settings the paper does not give. Divisive normalization alone gave no significant gain, and the explainable variance could not be tested, as the files hold only repeat-averaged responses.\n"
}
```

```
File created successfully at: summaries/nishimoto-2011-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n -i "—\|rather" docs/pilot-notes/nishimoto-2011-01.md summaries/nishimoto-2011-01.md; wc -w summaries/nishimoto-2011-01.md; git status --short
```

```
112 summaries/nishimoto-2011-01.md
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
?? docs/pilot-notes/nishimoto-2011-01.md
?? scripts
?? summaries/nishimoto-2011-01.md
```

**Agent**

I've written the notes and the summary as two new files and committed nothing. `targets/dandisets.json` has no entry for CRCNS:mt-2, so the notes don't open with a CatalystNeuro conversion sentence. The repository root also has untracked files I didn't create (`.bashrc`, `.idea`, `.mcp.json`, `scripts` and others), and I left them alone.

`docs/pilot-notes/nishimoto-2011-01.md`:

# nishimoto-2011, Nishimoto et al. 2011

Fourteen claims reproduced, three partially, two not reproduced and one blocked, for missing data; all 19 tested outcomes rest on an assumption. The first verification round agreed with all 20 outcomes as they then stood and the second with all 20; nothing was proposed after the second, so there was no third round. CRCNS data sets carry no version, so the record gives `unversioned`. The paper, Nishimoto and Gallant in the Journal of Neuroscience (31:14551-14564), records 52 MT neurons in two macaques watching motion-enhanced natural movies and fits a V1 filter model with a compressive nonlinearity and divisive normalization, then reports that the excitatory spectral receptive fields lie on a plane, the suppressive ones off it, that most neurons form a partial ring, and that the horizontal-vertical ratio of the ring correlates with simulated pattern selectivity. The claims were written from a text extraction of the version of record, with figures read from the PDF; the paper links no code. The paper's model does not fit in the time limit, so every tested claim uses a reduced one: the filter bank follows the paper's rules (7025 complex and 1082 simple channels), but the regression weights are pooled over space, onto 763 regressors (2 x 2 regions) for most analyses and 1465 (3 x 3 regions) where the paper fits a weight for each of 5956 filters. Reproduced are the mean prediction (0.518 with the 3 x 3 pooling, within 0.468 to 0.572; 0.448 with the 2 x 2 pooling under every reading), the example neuron, the compressive and divisive model as best (0.448 against 0.432, better in 34 of 45), the lack of effect of contrast normalization and of interaction, the dominance of complex cells, the excitatory on-plane ratio (0.592, all 40 combinations of readings), the null and suppressive ratios (0.395, at the upper edge, and 0.168, in 6 of 40 combinations), the partial ring, the pattern index, the absent correlation between prediction and pattern index, the natural-movie control (0.523 and 0.563, p = 0.43, 14 neurons) and the recovery of simulated fields. The pattern index reproduces only on responses rectified as firing rates, an assumption adopted after the raw outputs failed (medians -8.6 to -10.7), and the indices reach the paper's range through the clipping of the tuning curves. Partial are the compressive gains (4.6% and 8.4% against 16 and 19), the expansive losses (-15.1% and -13.5% against -36 and -24) and the absent correlation between prediction and horizontal-vertical ratio (r = -0.281, p = 0.061). Not reproduced are the gain from divisive normalization alone (2.9%, corrected p 0.056 over 11; 0.084 with the 3 x 3 pooling) and the correlation between horizontal-vertical ratio and pattern index (r = 0.231, p = 0.126; none of 64 combinations positive at p < 0.01). The explainable variance is blocked. The author's first run gave 11 reproduced, 4 partially, 4 not reproduced and 1 blocked. The author asked a reader nothing, so the answer and author-answers runs changed nothing. Round 1 found that the cost of the pooling was never measured, that the pattern index was computed on noise-free tuning curves and divided by zero for a pure component cell, and that the boosting step counts were not printed; in reply a second notebook, `finer_pooling.ipynb`, refitted the main model with the 3 x 3 pooling (every neuron better, mean +0.070), the pattern index was computed on rectified and Poisson-noise responses, the step counts were printed (median 156, none at the cap) with a patience of 500 as a check (0.449), and fig3b-mean-prediction, natural-movie-control and fig7b-pattern-index moved to reproduced. Round 2 found six sentences the outputs did not support, among them that a 4 x 4 pooling did not raise the correlation further on three neurons, where the changes were -0.022, -0.046 and +0.025, and asked for the Figure 2B models with the 3 x 3 pooling and the share of clipped directions; in reply a third notebook, `finer_pooling_fig2b.ipynb`, refitted four of the 12 models, which changed no outcome, a cell showed a median of 25% of directions clipped (Spearman rho 0.568 with the change of the index), and the sentences were corrected. The null reading on one neuron's movies under all four combinations was run but took the main notebook to 66 minutes, over the 60-minute limit, and is not run. The author's `entry.py all` passed in 3203 s, with the notebook at 53 min and a peak of 5.1 GB per worker; after round 1 the main notebook took 59.1 min and `finer_pooling.ipynb` 26.5. In the second revision `entry.py all` was not run, as the three notebooks take about 140 minutes and a command is capped at 2 hours; each notebook was run on its own (main 65 min, Figure 2B 47 min), so there is no clean-run stamp, the final markdown was copied into the executed copies after the runs, and the threaded fits moved some values in the third decimal.

The files hold only the response averaged over repeats, not the single repeats, so the explainable variance the paper reports cannot be computed, and `ranges.trange` is empty in every file. The data set holds 45 of the paper's 52 MT neurons (34 from monkey f, 11 from monkey v), as its descriptor says, and no recording appears twice. Fourteen files hold a field `ranges.nrange`, the first 2000 frames of a 4000-frame `ranges.vrange`, which the descriptor does not describe; its frames carry less motion than the rest of `vrange` (median frame difference over contrast 0.225 against 0.325, lower in all 14), consistent with the paper's natural movies, whose control used 15 neurons. The denominators of the averaged validation responses imply 10 to 33 repeats per neuron, where the paper reports 5 to 20, and training frames carry denominators up to 5, so some were shown more than once, which neither the paper nor the descriptor mentions. Training frames number 17,908 to 40,000 per neuron (mean 26,894), where the paper gives 20,000 to 40,000 (mean 27,120), and in ct0133 (v0395) 12,729 of 19,842 training frames have no response, leaving 7,093. The descriptor does not say how the response bins are aligned to the frames; with a temporal filter centred on each frame, a delay window moved 3 or 6 frames earlier fits the held-out training data better for 14 of 45 neurons. In the paper, "up to 10 frames or 130 ms" disagree at 83 Hz, and the Methods give 20,000 to 40,000 training frames where the Results give 22,000 to 42,000, which matches the training plus validation frames of the files. Three questions are put to the paper's authors: the temporal envelope, frequencies and filter counts of the filter bank; the boosting step, stopping rule, semisaturation constant and held-out parts; and the grating and plaid settings of the pattern-index simulation, whether its responses were rectified or noisy, and how the constraints of the optimal plane were balanced.

The author's points on the protocol: a model far over the time limit can only be blocked as `too_large`, and a reduced model was fitted as a deviation instead; the Result lines must sit in the executed notebook but can only be written after the results, which cost two full runs of about 55 min; any edit to `entry.yaml` invalidates the record of the completed run, so `runtime_minutes` was left at 45 though the run took 53; it is unclear which reading to judge a claim of absence on when its measure has several readings from another claim, and the first was used; the clock check does not apply without a trial table, and the prediction was compared with the response shifted in time instead; and `check` requires the dataset version to be named in a particular form, so `DATASET = "crcns:mt-2/unversioned"` was added to the helper.

`summaries/nishimoto-2011-01.md` (112 words):

Most of the paper's main findings held up in this data, on a reduced version of its model fitted to 45 of its 52 MT neurons. The compressive and divisive V1 filter model predicted responses as well as reported (mean correlation 0.518 against 0.52) and beat the other models. Excitatory spectral receptive fields lay on a plane, suppressive ones off it, and most formed a partial ring. The link between the horizontal-vertical ratio and simulated pattern selectivity did not reproduce, in a simulation whose settings the paper does not give. Divisive normalization alone gave no significant gain, and the explainable variance could not be tested, as the files hold only repeat-averaged responses.

## End of run

13 turns, 2 minutes, $0.95 at API prices, result: success.
