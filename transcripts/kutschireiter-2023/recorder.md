# 000289 · recorder · run 40987738988

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/000289/ claims/000289/; python tools/readme_row.py 000289; cat attempts/000289-kutschireiter-2023-01.yaml
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fef8a1da-4429-463f-8632-22b6ae7b20e5/tool-results/bj4sf83ms.txt

Preview (first 2KB):
docs/pilot-notes/000166-senzai-2019-01.md
docs/pilot-notes/000223-xue-2022-01.md
docs/pilot-notes/000249-schiavo-2020-01.md
docs/pilot-notes/000231-rodgers-2022-01.md
docs/pilot-notes/000140-churchland-2010-01.md
claims/000289/:
10.1073-pnas.2210622120.yaml

transcripts/000289/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000289-kutschireiter-2023-01.yaml; for f in docs/pilot-notes/000166-senzai-2019-01.md docs/pilot-notes/000223-xue-2022-01.md docs/pilot-notes/000249-schiavo-2020-01.md docs/pilot-notes/000231-rodgers-2022-01.md docs/pilot-notes/000140-churchland-2010-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (75.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fef8a1da-4429-463f-8632-22b6ae7b20e5/tool-results/bn0z4s3su.txt

Preview (first 2KB):
schema_version: 2
id: 000289-kutschireiter-2023-01
dataset:
  archive: dandi
  id: "000289"
  version: 0.240801.1040
  doi: 10.48324/dandi.000289/0.240801.1040
paper: doi:10.1073/pnas.2210622120
date: 2026-10-29
entry: 000289-kutschireiter-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fef8a1da-4429-463f-8632-22b6ae7b20e5/tool-results/bn0z4s3su.txt"
}
```

```
1	schema_version: 2
2	id: 000289-kutschireiter-2023-01
3	dataset:
4	  archive: dandi
5	  id: "000289"
6	  version: 0.240801.1040
7	  doi: 10.48324/dandi.000289/0.240801.1040
8	paper: doi:10.1073/pnas.2210622120
9	date: 2026-10-29
10	entry: 000289-kutschireiter-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 816 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fef8a1da-4429-463f-8632-22b6ae7b20e5/tool-results/bn0z4s3su.txt",
 "offset": 837,
 "limit": 340
}
```

```
837	in PubMed Central (PMC7677212), not the version of record; the paper's code and
838	data DOI (10.35092/yhjc.c.5037737) does not resolve, no analysis code was
839	found, and the claims check made 20 corrections before the attempt. The
840	dandiset holds only the two-photon imaging, so the 20 imaging claims and
841	`fig3-retrieval-onset-range` are blocked as `metadata_insufficient`, and
842	`fig1a-isi-distribution`, the behaviour claims and
843	`ed4d-response-tracks-isi-probability` as `data_missing`. The link claim
844	`subject-group-link` is partially reproduced: every subject has a figshare
845	item titled with its mouse id (54 of 54) and 7 of the 9 group counts match the
846	paper, but no file says which call each trial played. Ten claims use the
847	whole-cell, slice and operant recordings of the figshare collection the
848	dandiset links (doi:10.6084/m9.figshare.c.5043830.v6) and are left out of the
849	counts: `ed9b-oxytocin-enhances-spiking` is reproduced and
850	`fig1g-ipsc-depress-faster` not reproduced, each resting on an assumption;
851	`fig1i-operant-prototypes` and `ed5b-press-count-unchanged` are blocked as
852	`methods_underspecified`, as the readings disagree; `ed6h-dams-evs-epsc-similar`
853	is blocked as `metadata_insufficient`; and the five in vivo whole-cell claims
854	are blocked as `other`. The author's first run had three of those five as not
855	reproduced, `fig2h-epsc-enhanced-ev` as partially reproduced and
856	`fig2i-ipsc-weaker-nv` as blocked as `methods_underspecified`. Round 1 found
[... 315 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -80; grep -n "| Dandiset\|^| ---\|^| Dataset" README.md | head; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
    if '000289' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
E
cat claims/000289/*.yaml | head -60
```

```
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
[... 118 more lines not kept]
```

**Agent**

Gathering the remaining sources now: claim data kinds, the target entry, and the reports.

**Agent calls Bash**

```bash
cd  sed -n 60,90p claims/000289/*.yaml; grep -nE "^  - id:|^- id:|^    data:|^  data:|kind: link|depends_on" claims/000289/*.yaml; grep -n -B2 -A12 '"000289"' targets/dandisets.json | head -40
```

```
# that text nor the version of record reports experiments. So the dataset holds no data this
# paper analyses. All findings below are simulation or connectome results (data elsewhere),
# except the Discussion's prediction about bump amplitude and cue reliability, the one statement
# of the paper the dataset could bear on; the paper does not test it and gives no experimental
# method for it.
#
# How the simulation claims are tested. Each is judged on the paper's own released outputs in
# data_processed/ (the README says the figure notebooks reproduce the plots from them), loaded
# with the figure's notebook. A rerun of the scan scripts (with the keyword fix above, and fewer
# trajectories if needed) is a variant, shown and not judged. Where the paper says "similar",
# "indistinguishable" or "close" with no number, the criterion names the readings the text
# allows; the outcome is the one all readings give.
schema_version: 2
dataset:
  archive: dandi
  id: "000289"
paper: doi:10.1073/pnas.2210622120
claims:
- id: fig1-conflict-decreases-certainty
  statement: >-
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1935,1960p targets/dandisets.json; cd transcripts/000289; wc -w *-report.md; ls -la --time-style=full-iso *-report.md | awk '{print $7, $9}'
```

```
"behavioral approach"
   ],
   "papers": [
    {
     "doi": "10.1101/2021.12.17.473253v4",
     "title": "Bayesian inference in ring attractor networks",
     "relation": "IsSupplementTo",
     "resource_type": null,
     "preprint": true
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000294",
   "name": "A multi-modal fitting approach to construct single-neuron models with patch-clamp and high-density microelectrode arrays",
   "published_version": "0.260528.0854",
   "asset_count": 2,
   "size_gb": 18.17,
   "data_standards": [
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000289; for f in author-report.md answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-report.md
I've finished steps 1 to 5 and the handover (step 6), in about 1 h 20 min (22:52 to 00:10 UTC). The entry passes `python tools/entry.py all` with 0 errors and the notebook runs in about 9 minutes.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1-conflict-decreases-certainty | reproduced |
| fig2h-bump-tracks-circkf | reproduced |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced |
| fig3b-bayesian-beats-conventional | reproduced |
| fig3c-update-weights | reproduced |
| fig3d-best-network-slow-decay | partially reproduced: condition (4) fails, with two small rises (0.0008 and 0.0014) |
| fig3f-noise-drop-below-70 | reproduced (63.1% at noise SD 10) |
| fig3f-retuning-reduces-drop | reproduced: measured 34.64% (expected 35 ± 3.5) |
| noise-effects-on-mu-and-kappa | partially reproduced: bump amplitude falls under noise instead of drifting up |
| fig4b-connectome-motifs | reproduced, resting on an assumption (`assumed: true`) |
| fig4gh-drosophila-network-matches | partially reproduced: holds within 0.02, not within 0.01 |
| figs2-performance-independent-of-n | partially reproduced: one value (N 16 at 0.1/s) is 0.041 off |
| prediction-bump-amplitude-cue-reliability | blocked, `methods_underspecified` (the claim's readings disagree) |
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000289; cat verifier-1-report.md | head -60; echo ======; cat verifier-2-report.md | head -50
```

```
**A. Outcomes** (13 claims, from the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Cell 12: (a) and (b) hold in 6 of 6 cases (κ_t = 1, 2, 5; γ_z = 1 and 10/s). For example, at κ_t = 5 and γ_z = 1, the full step gives 5.039 (confirmatory) against 4.904 (no observation) against 4.768 (opposite). |
| fig2h-bump-tracks-circkf | reproduced | Cell 14: at rates 15 and 10, the network-to-circKF difference is 0.016 and 0.021 rad, against circKF error of 0.483 and 0.491. Correlation over cue periods is 0.994 and 0.993. In darkness the amplitude falls from 7.21 to 1.22 (rate 15) and from 5.89 to 1.21 (rate 10), ending closer to κ* = 1. |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Cell 16: the largest accuracy difference is 0.0010 at rates ≥ 1/s and 0.0003 at ≥ 3/s, so all four combinations pass. At 0.01 to 0.1/s the attractor is less accurate (−0.073, −0.084, −0.057) and more certain (+0.82, +0.69, +0.49). |
| fig3b-bayesian-beats-conventional | reproduced | Cell 18: the optimal κ* is 1.7. The Bayesian attractor is more accurate at all 23 rates (smallest difference 0.0115) and strictly above from 0.1 to 10/s (smallest 0.034). The not-judged part fails: the smallest differences are at 0.01, 2 and 3/s, not at 0.01 and 0.03/s. |
| fig3c-update-weights | reproduced | Cell 20: the largest difference at ≥ 1/s is 0.0010 under reading (i) and 0.0062 under (ii), within both 0.02 and 0.05. Under both readings the largest difference is at 0.01/s. |
| fig3d-best-network-slow-decay | partially_reproduced | Cell 22: conditions 1, 2, 3 and 5 hold (best network κ* = 0.7, β = 0.3; the Bayesian attractor is 0.57% below it). Condition 4 fails: the maximum over κ* rises twice for β above the best (0.7→0.8 by +0.0008, 0.9→1 by +0.0014). Overall Spearman ρ is −0.98. |
| fig3f-noise-drop-below-70 | reproduced | Cell 24: untuned performance is 63.1% at SD 10 and 38.1% at SD 20 under both normalizations, all below 70%. 
[... 86 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000289-kutschireiter-2023-01.md",
 "content": "# 000289, Kutschireiter et al. 2023\n\nNo claims reproduced, none partially, none not reproduced and one blocked on\nthe dataset; the other twelve claims use data elsewhere and are left out of the\ncounts. It pins version 0.240801.1040, the only published version, and the\ndraft is identical in assets and size. The paper, Kutschireiter, Basnak, Wilson\nand Drugowitsch in PNAS, is a theory paper: it derives a circular Kalman filter\n(circKF) for head direction (HD), shows that a ring attractor network can\nimplement it as a Bayesian ring attractor, compares it with a conventional\nattractor of fixed certainty, studies the effect of neural noise, and maps the\nnetwork onto the Drosophila central complex with the hemibrain connectome. It\nrecords no data, and its one statement the dandiset could bear on is the\nDiscussion's prediction that bump amplitude is higher with reliable HD cues.\nThe claims were written from the version of record as served by Europe PMC\n(PMC9992764) with its SI Appendix, and from the paper's code and processed\nsimulation outputs on Zenodo (doi:10.5281/zenodo.7615975, commit a9db6f9). The\ntwelve simulation and connectome claims were judged on those stored outputs and\non the public hemibrain v1.2 export: seven are reproduced, four partially and\none not. `fig3d-best-network-slow-decay` fails its condition 4 with two rises\n(0.0008 and 0.0014) that are 0.32 and 0.52 standard errors;\n`noise-effects-on-mu-and-kappa` fails because the bump amplitude falls under\nnoise (0.83, 0.65, 0.82 and 0.42 against the noise-free 1.00) where the paper\nsays it drifts up; `fig4gh-drosophila-network-matches` holds within 0.02 but\nnot within 0.01 at 0.1, 0.2 and 0.3/s; `fig4b-connectome-motifs` holds under\nthe sort by protocerebral bridge glomerulus, while the second sort the\ncriterion requires cannot be formed from hemibrain names, and rests on\nassumptions; and `figs2-performance-independent-of-n` is not reproduced, as N\n16 at 0.1/s is 0.041 below the reference, 4.3 standard errors of a difference.\nThe prediction was tested on the 15 flies of the dandiset's cue-contrast\nexperiment and is blocked as `methods_underspecified`, as the readings\ndisagree: high contrast exceeds low in 10 of 15 flies with dF/F but p 0.138,\nand in 12 of 15 with raw fluorescence and p 0.021. The author asked a reader\nno questions, so the answer run and the following author run changed nothing.\nRound 1 agreed with 11 of 13 outcomes, and the author took both of its others:\nfig4b from reproduced to partially reproduced, as the criterion requires both\nsorts, and figs2 from partially reproduced to not reproduced, as both readings\nfail. Its points led to the defining lines of the released code printed, Monte\nCarlo standard errors from the 10,000 runs per scan, the inhibition and a run\nwith it held fixed for the noise claim, 18 variants of the raw signal for the\nprediction (p below 0.05 in all nine F - F0 variants and in none of the nine\ndivided by F0) and the NaN cell of Fig. S2 printed. Round 2 agreed with all 13,\nso there was no third round; it found statements the outputs did not support,\namong them swapped dF/F and raw ratios, ROI mask sizes never printed and a\nnoise control that removes the restoring force along with the noise's effect\non the inhibition, which were corrected, the last with a control that keeps\nthe inhibition at the value a noise-free bump of the decoded amplitude gives\n(mean amplitude 1.002 to 1.045 after 5 s). Three questions were put to a\nreader during the revisions, after the answer step: whether the noise claim\nshould test only the noise's direct effect, as the SI derivation does, whether\nfig4b's second sort belongs to the claim, and whether \"mostly independent\"\nallows a single exception in figs2. The author's run took about 1 h 20 min\n(22:52 to 00:10 UTC) and nothing failed; the paper's large scans were not\nre-run. The notebook ran in about 9 minutes at first, mostly streaming 10% of\nthe raw imaging, and in 6.5 minutes in the last run.\n\nThe dandiset holds no data of this paper: its related resources name the\nbioRxiv preprint of this paper (10.1101/2021.12.17.473253 version 4) as the\npaper it supplements, but its description says the data belong to\n\"Uncertainty and learning in a biological ring attractor\" (Basnak et al., in\npreparation), so it links no paper that uses them. imaging_rate is 9.18 Hz in\nevery file, but sub-4 and sub-10 are imaged at 7.87 Hz (0.127 s frame\ninterval, 9446 frames in 1200 s) with 14 planes, against 9.18 Hz and 12 planes\nin the other 13 sessions. In sub-2 the trials table has five blocks (high,\nzero, low, zero, low) where every other fly of the cue-contrast experiment has\nsix with two of each contrast, and the last block lasts 405 s against about\n200 s in the protocol, so it may hold a low and a high block labelled as one.\nThe processing behind the stored dF/F is not described: the ROI masks are 2D,\n3 to 11 pixels each (median 7), the dF/F agrees with the raw imaging averaged\nin them only after spatial smoothing (median correlation over ROIs 0.66\nwithout, 0.93 with a 4-pixel Gaussian, sub-1), and the RoiResponseSeries unit\nis \"na\". The bump phase follows the cue position with peak coupling at lag 0\nto 5 frames, so the dF/F and the cue share a clock. The paper's released code\ndoes not run as published, as RNN_filter_Run uses z but has no z parameter and\nFigure2h.ipynb and the scan scripts pass kappa_y to functions whose parameter\nis kappa_v, and one NaN remains in figureS2.npz (N 128 at 100/s); the\nconnectome is the public v1.2 export, not v1.2.1 as in the legend, since\nneuPrint now requires a personal API token. Two questions are put to the\npaper's authors: which activity signal, comparison of cue conditions and test\nwould test the bump amplitude prediction, and which spatial position Fig. 4B\nused to sort neurons, as the hemibrain names give only the PB glomerulus for\nEPG and PEN1 neurons.\n\nThe author's points on the protocol: it assumes the dataset holds the paper's\ndata, so the twelve claims on data elsewhere were tested on the Zenodo deposit\npinned by DOI and md5; it does not cover a reading the criterion names that\ncannot be formed from the data, as fig4b's second sort; the claims file\nrequires every reading to hold where the protocol lets a number be reproduced\nunder any reading, and the claims file was followed; the prediction's\ncriterion says to block when readings differ while step 1.6 allows adopting\nthe best-supported reading; it does not say what counts as public when\nneuPrint needs a personal token; it does not set the scope of the duplicate\ncheck, which compared traces only among the 15 sessions analysed; its\nstreaming rule is written for the dataset, and the outside zip and tar were\nread whole into memory; and it does not say whether one failed condition of a\nmulti-condition criterion with the effect present is partially or not\nreproduced.\n"
}
```

```
File created successfully at: docs/pilot-notes/000289-kutschireiter-2023-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -nE "—|rather|\*\*" docs/pilot-notes/000289-kutschireiter-2023-01.md; wc -w docs/pilot-notes/000289-kutschireiter-2023-01.md
```

```
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
?? docs/pilot-notes/000289-kutschireiter-2023-01.md
?? scripts
1162 docs/pilot-notes/000289-kutschireiter-2023-01.md
```

**Agent**

I wrote `docs/pilot-notes/000289-kutschireiter-2023-01.md` and changed no other file; nothing is committed. The note is 1,162 words, about the length of the recent notes. The `catalystneuro` field for 000289 is empty, so the second paragraph does not open with the CatalystNeuro sentence.

# 000289, Kutschireiter et al. 2023

No claims reproduced, none partially, none not reproduced and one blocked on the dataset; the other twelve claims use data elsewhere and are left out of the counts. It pins version 0.240801.1040, the only published version, and the draft is identical in assets and size. The paper, Kutschireiter, Basnak, Wilson and Drugowitsch in PNAS, is a theory paper: it derives a circular Kalman filter (circKF) for head direction (HD), shows that a ring attractor network can implement it as a Bayesian ring attractor, compares it with a conventional attractor of fixed certainty, studies the effect of neural noise, and maps the network onto the Drosophila central complex with the hemibrain connectome. It records no data, and its one statement the dandiset could bear on is the Discussion's prediction that bump amplitude is higher with reliable HD cues. The claims were written from the version of record as served by Europe PMC (PMC9992764) with its SI Appendix, and from the paper's code and processed simulation outputs on Zenodo (doi:10.5281/zenodo.7615975, commit a9db6f9). The twelve simulation and connectome claims were judged on those stored outputs and on the public hemibrain v1.2 export: seven are reproduced, four partially and one not. `fig3d-best-network-slow-decay` fails its condition 4 with two rises (0.0008 and 0.0014) that are 0.32 and 0.52 standard errors; `noise-effects-on-mu-and-kappa` fails because the bump amplitude falls under noise (0.83, 0.65, 0.82 and 0.42 against the noise-free 1.00) where the paper says it drifts up; `fig4gh-drosophila-network-matches` holds within 0.02 but not within 0.01 at 0.1, 0.2 and 0.3/s; `fig4b-connectome-motifs` holds under the sort by protocerebral bridge glomerulus, while the second sort the criterion requires cannot be formed from hemibrain names, and rests on assumptions; and `figs2-performance-independent-of-n` is not reproduced, as N 16 at 0.1/s is 0.041 below the reference, 4.3 standard errors of a difference. The prediction was tested on the 15 flies of the dandiset's cue-contrast experiment and is blocked as `methods_underspecified`, as the readings disagree: high contrast exceeds low in 10 of 15 flies with dF/F but p 0.138, and in 12 of 15 with raw fluorescence and p 0.021. The author asked a reader no questions, so the answer run and the following author run changed nothing. Round 1 agreed with 11 of 13 outcomes, and the author took both of its others: fig4b from reproduced to partially reproduced, as the criterion requires both sorts, and figs2 from partially reproduced to not reproduced, as both readings fail. Its points led to the defining lines of the released code printed, Monte Carlo standard errors from the 10,000 runs per scan, the inhibition and a run with it held fixed for the noise claim, 18 variants of the raw signal for the prediction (p below 0.05 in all nine F - F0 variants and in none of the nine divided by F0) and the NaN cell of Fig. S2 printed. Round 2 agreed with all 13, so there was no third round; it found statements the outputs did not support, among them swapped dF/F and raw ratios, ROI mask sizes never printed and a noise control that removes the restoring force along with the noise's effect on the inhibition, which were corrected, the last with a control that keeps the inhibition at the value a noise-free bump of the decoded amplitude gives (mean amplitude 1.002 to 1.045 after 5 s). Three questions were put to a reader during the revisions, after the answer step: whether the noise claim should test only the noise's direct effect, as the SI derivation does, whether fig4b's second sort belongs to the claim, and whether "mostly independent" allows a single exception in figs2. The author's run took about 1 h 20 min (22:52 to 00:10 UTC) and nothing failed; the paper's large scans were not re-run. The notebook ran in about 9 minutes at first, mostly streaming 10% of the raw imaging, and in 6.5 minutes in the last run.

The dandiset holds no data of this paper: its related resources name the bioRxiv preprint of this paper (10.1101/2021.12.17.473253 version 4) as the paper it supplements, but its description says the data belong to "Uncertainty and learning in a biological ring attractor" (Basnak et al., in preparation), so it links no paper that uses them. imaging_rate is 9.18 Hz in every file, but sub-4 and sub-10 are imaged at 7.87 Hz (0.127 s frame interval, 9446 frames in 1200 s) with 14 planes, against 9.18 Hz and 12 planes in the other 13 sessions. In sub-2 the trials table has five blocks (high, zero, low, zero, low) where every other fly of the cue-contrast experiment has six with two of each contrast, and the last block lasts 405 s against about 200 s in the protocol, so it may hold a low and a high block labelled as one. The processing behind the stored dF/F is not described: the ROI masks are 2D, 3 to 11 pixels each (median 7), the dF/F agrees with the raw imaging averaged in them only after spatial smoothing (median correlation over ROIs 0.66 without, 0.93 with a 4-pixel Gaussian, sub-1), and the RoiResponseSeries unit is "na". The bump phase follows the cue position with peak coupling at lag 0 to 5 frames, so the dF/F and the cue share a clock. The paper's released code does not run as published, as RNN_filter_Run uses z but has no z parameter and Figure2h.ipynb and the scan scripts pass kappa_y to functions whose parameter is kappa_v, and one NaN remains in figureS2.npz (N 128 at 100/s); the connectome is the public v1.2 export, not v1.2.1 as in the legend, since neuPrint now requires a personal API token. Two questions are put to the paper's authors: which activity signal, comparison of cue conditions and test would test the bump amplitude prediction, and which spatial position Fig. 4B used to sort neurons, as the hemibrain names give only the PB glomerulus for EPG and PEN1 neurons.

The author's points on the protocol: it assumes the dataset holds the paper's data, so the twelve claims on data elsewhere were tested on the Zenodo deposit pinned by DOI and md5; it does not cover a reading the criterion names that cannot be formed from the data, as fig4b's second sort; the claims file requires every reading to hold where the protocol lets a number be reproduced under any reading, and the claims file was followed; the prediction's criterion says to block when readings differ while step 1.6 allows adopting the best-supported reading; it does not say what counts as public when neuPrint needs a personal token; it does not set the scope of the duplicate check, which compared traces only among the 15 sessions analysed; its streaming rule is written for the dataset, and the outside zip and tar were read whole into memory; and it does not say whether one failed condition of a multi-condition criterion with the effect present is partially or not reproduced.

## End of run

12 turns, 1 minutes, result: success.
