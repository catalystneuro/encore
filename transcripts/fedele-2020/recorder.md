# 000576 · recorder · run 41142814831

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 000576; ls claims/000576 transcripts/000576; cat attempts/000576-fedele-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000576' in json.dumps(x)[:300]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (51.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8385f3ee-802c-4c4b-8c1a-fd03a6175036/tool-results/b9979zzb1.txt

Preview (first 2KB):
docs/pilot-notes/000467-hart-2023-01.md
docs/pilot-notes/000541-yemini-2021-01.md
docs/pilot-notes/000489-kim-2022-01.md
docs/pilot-notes/000469-kyzar-2024-01.md
docs/pilot-notes/000458-claar-2023-01.md
| [000576](https://dandiarchive.org/dandiset/000576) | [Fedele et al. 2020](https://doi.org/10.1016/j.neuroimage.2020.116705) | 0 | 3 (+1) | 12 | 3 (+6) | [`000576-fedele-2020`](entries/000576-fedele-2020) |
claims/000576:
10.1016-j.neuroimage.2020.116705.yaml

transcripts/000576:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000576-fedele-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
def walk(o):
  if isinstance(o,dict):
    if str(o.get('id',''))=='000576' or o.get('dandiset')=='000576': print(json.dumps(o,indent=1)); return
    for v in o.values(): walk(v)
  elif isinstance(o,list):
    for v in o: walk(v)
walk(d)"
```

```
<persisted-output>
Output too large (51.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8385f3ee-802c-4c4b-8c1a-fd03a6175036/tool-results/b1kthfc17.txt

Preview (first 2KB):
schema_version: 2
id: 000576-fedele-2020-01
dataset:
  archive: dandi
  id: '000576'
  version: 0.231010.1811
  doi: 10.48324/dandi.000576/0.231010.1811
paper: doi:10.1016/j.neuroimage.2020.116705
date: 2026-10-30
entry: 000576-fedele-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 000467-hart-2023-01 000541-yemini-2021-01 000489-kim-2022-01 000469-kyzar-2024-01 000458-claar-2023-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; echo ===; cat docs/pilot-notes/001754-knierim-2000-02.md | head -5
```

```
<persisted-output>
Output too large (35.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8385f3ee-802c-4c4b-8c1a-fd03a6175036/tool-results/bgrn845px.txt

Preview (first 2KB):
=== 000467-hart-2023-01
# 000467, Hart et al. 2023

Three claims reproduced, three partially, 11 not reproduced and eight blocked
on the dandiset; the seven claims on data in other archives, counted apart,
are blocked too. The verification rounds agreed on every outcome but one:
the verifier holds `figs4a-bilateral-symmetry` to be not reproduced, and the
disagreement is recorded. It pins version 0.261004.1655, the only published
version; the paper cites none. The paper, Hart, Frank, Lopes et al. in Cell,
expresses GCaMP6s in the olfactory sensory neurons of the clonal raider ant
Ooceraea biroi, images the antennal lobe (AL) with two photons while the ants
smell general odorants and four alarm pheromones, and shows that the
pheromones are encoded sparsely and stereotypically, implicating a core
glomerulus for alarm behaviour. The claims were written from the accepted
author manuscript in PubMed Central (PMC10334690) and from the lab's
repository Hart_Kronauer2023 at commit 72d041a, which holds a TIFF converter
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8385f3ee-802c-4c4b-8c1a-fd03a6175036/tool-results/bgrn845px.txt"
}
```

```
1	=== 000467-hart-2023-01
2	# 000467, Hart et al. 2023
3	
4	Three claims reproduced, three partially, 11 not reproduced and eight blocked
5	on the dandiset; the seven claims on data in other archives, counted apart,
6	are blocked too. The verification rounds agreed on every outcome but one:
7	the verifier holds `figs4a-bilateral-symmetry` to be not reproduced, and the
8	disagreement is recorded. It pins version 0.261004.1655, the only published
9	version; the paper cites none. The paper, Hart, Frank, Lopes et al. in Cell,
10	expresses GCaMP6s in the olfactory sensory neurons of the clonal raider ant
11	Ooceraea biroi, images the antennal lobe (AL) with two photons while the ants
12	smell general odorants and four alarm pheromones, and shows that the
13	pheromones are encoded sparsely and stereotypically, implicating a core
14	glomerulus for alarm behaviour. The claims were written from the accepted
15	author manuscript in PubMed Central (PMC10334690) and from the lab's
16	repository Hart_Kronauer2023 at commit 72d041a, which holds a TIFF converter
17	and the ImageJ macro for the peak maps; the repository the Key Resources Table
18	links returns 404. The 17 imaging claims were tested; the behaviour,
19	transgenesis and pupa image claims are blocked as `data_missing`, the four
20	Brain Image Library claims as `other`, as the retrieve API answered "no entry
[... 495 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 "000576\|^| Dataset\|^|---" README.md | head -20; sed -n 1,80p tools/readme_row.py
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
[... 58 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8385f3ee-802c-4c4b-8c1a-fd03a6175036/tool-results/b1kthfc17.txt"
}
```

```
1	schema_version: 2
2	id: 000576-fedele-2020-01
3	dataset:
4	  archive: dandi
5	  id: '000576'
6	  version: 0.231010.1811
7	  doi: 10.48324/dandi.000576/0.231010.1811
8	paper: doi:10.1016/j.neuroimage.2020.116705
9	date: 2026-10-30
10	entry: 000576-fedele-2020
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
[... 815 more lines not kept]
```

**Agent**

Read the attempt record and the five recent notes; now the reports and claims file.

**Agent calls Bash**

```bash
cd transcripts/000576; wc -c *-report.md; cat author-report.md
```

```
907 answer-report.md
 1657 author-answers-report.md
 6202 author-report.md
 4477 author-revise-1-report.md
 2775 author-revise-2-report.md
 3116 claims-check-report.md
 4182 claims-report.md
10257 verifier-1-report.md
 7362 verifier-2-report.md
40935 total
I've written and run the entry for DANDI:000576 (Fedele, Tzovara et al. 2020) and built the handover package. All 25 claims have an outcome: 4 reproduced, 3 partially reproduced, 10 not reproduced and 8 blocked. The notebook runs in about 2.7 min from a clean environment; `check` and `all` pass and `handover` built the package. I did not verify my own work, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1b-delta-decrease | blocked, methods_underspecified (holds in 10 of 16 readings; the criterion blocks when they disagree) |
| fig1c-hgp-increase-first-2s | not reproduced (no high gamma cluster under any of the 32 readings) |
| other-bands-no-effect | not reproduced (assumed) |
| table2-mi-values | not reproduced |
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000576; for f in answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== answer-report.md
No questions to answer, and I changed nothing.

- **`questions/000576.yaml` does not exist.** No branch in the git history has ever had it.
- **The author asked readers nothing.** Their report (`transcripts/000576/author-report.md`) says "Questions to a reader: none."
- **The attempt does contain three questions, but they are for the paper's authors.** They are recorded as `methods_unavailable` findings in `attempts/000576-fedele-2020-01.yaml` and are not claims-file questions for a reader. They ask:
  - how the power envelopes were z-scored within each trial;
  - over which window the modulation index was computed;
  - on what time base, and over which span, a condition was measured.

None of them says the claims file misreads the paper, so there is nothing to amend in `claims/000576/` and no `answered` dates to set.

If questions were filed somewhere else, tell me where and I'll answer them.
=== author-answers-report.md
No reader answered anything, so no claim changed and none needed re-running. The entry still passes its checks and runs cleanly, and the handover package is built.

**Questions.** There were none. `questions/000576.yaml` does not exist, and the reader's report (`transcripts/000576/answer-report.md`) says it had nothing to answer and changed nothing. My earlier author run asked readers nothing. Its three open questions were about the paper's methods and are for the paper's authors: they are recorded as `methods_unavailable` findings in the attempt record. They ask:
- how the power envelopes were z-scored;
- over which window each modulation index was computed;
- on what time base and span the Fig. 3B firing versus high gamma correlations were computed.
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/000576/*.yaml; head -40 $f; grep -n "^  - id:\|^- id:\|data:\|kind:" $f | head -80
```

```
# Claims for Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, on dandiset 000576.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF),
# main text, figure legends, Tables 1 and 2 and Methods. Table 2 was read from the extracted
# text, in which minus signs print as a replacement glyph; its signs agree with the counts the
# Results give (12 of 14 negative DELTA MI, HGP MI positive in 7 of 7 nSOZ and negative in 6 of
# 7 SOZ amygdalae). The PDF pages could not be rendered here. The supplement (Appendix A, online)
# was not supplied; the text cites it only for Fig. S2 (waveforms and inter-spike intervals of
# the neurons of each patient), which carries no finding. The Results also cite "Methods 7.8"
# for the other spectral bands; no such section exists in the text, and section 4.8 lists the
# bands without results.
# The data descriptor of the same data (Fedele et al. 2021, Sci Data, doi:10.1038/s41597-020-00790-x,
# in paper/) was read for the layout of the deposited data only; no claim is taken from it.
#
# Code: the paper links no analysis code. The data descriptor says scripts for reading the NIX
# files and for its own Figs 2 and 3 come with the G-Node and OpenNeuro deposits; these are not
# the paper's analysis and were not read. Every method below is from the paper's Methods (4.7
# to 4.11), Results and figure legends.
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,106p claims/000576/*.yaml
```

```
# claims that use BOLD are marked with_inputs. The muHGP claims need the continuous microwire
# signals; the data descriptor says only spike times and mean waveforms of the microwire data
# were shared.
#
# Inconsistencies in the paper, recorded here and in the claims that they touch: the abstract
# says 5 participants had microwires, Results 2.3 says 9 amygdalae, and the MUA column of
# Table 1 lists 8 amygdalae of 6 patients (1 L and R, 2 L and R, 3 L, 4 L, 5 R, 8 L), three of
# them SOZ, while Discussion 3.4 says there were no microwire recordings from SOZ amygdalae.
# Methods 4.4 gives eight AVERSIVE and nine NEUTRAL blocks; the data descriptor, quoting
# Schacher et al., gives eight of each. The Table 2 legend says BOLD correlated positively
# with HGP in 5 of 5 amygdalae; the Results and the table's own values give 3 of 5 nSOZ.
#
# Method of the iEEG power analysis, from Methods 4.8 and 4.11, used by several claims:
# bipolar amygdala channel; IIR Butterworth filter of order 2 per band, delta 1-4 Hz, theta
# 4-8, alpha 8-15, beta 15-30, gamma 30-60, high gamma above 60 Hz; amplitude of the Hilbert
# analytic signal; smoothed with a 1 s window; baseline corrected with the 1 s before the
# start of each sequence; z-scored within each trial; time-point by time-point linear mixed
# model Power ~ condition + (1|Patients) on all single trials; cluster-based permutation over
# time with 500 permutations of the AVERSIVE and NEUTRAL labels across participants,
# significance at p < 0.05. Modulation index MI = AVERSIVE minus NEUTRAL time-averaged power
[... 47 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000576-fedele-2020-01.md",
 "content": "# 000576, Fedele et al. 2020\n\nNo claim reproduced, three partially, 12 not reproduced and three blocked on\nthe dandiset; with outside data, counted apart, one partially reproduced and\nsix blocked. The first verification round agreed with 20 of 25 outcomes and\nthe second with all 25, so there was no third round. It pins version\n0.231010.1811, the only published version; the paper predates the dandiset\nand cites none. The paper, Fedele, Tzovara et al. in NeuroImage, records\nmacroelectrode iEEG and microwire units in the 14 amygdalae of nine patients\nwith drug-resistant mesial temporal lobe epilepsy while they watch blocks of\ndynamic fearful faces (AVERSIVE) and landscapes (NEUTRAL), and relates a\nsustained delta power decrease and an onset increase in high gamma power\n(HGP) to neuronal firing and to the BOLD signal of a pre-operative fMRI, with\nthe HGP modulation index (MI) separating amygdalae outside the seizure onset\nzone (nSOZ) from those within it (SOZ). The claims were written from the\nversion of record, a PDF supplied by a person; the paper links no analysis\ncode, and the data descriptor (Fedele et al. 2021) was read for the layout of\nthe data only. The iEEG and spike claims were tested; the six claims that\nneed the BOLD time courses and the muHGP claim are blocked as `data_missing`,\nand `fig3d-firing-correlations-modalities` was tested on its HGP part only.\n`fig1b-delta-decrease` is blocked as `methods_underspecified`, as it holds in\n6 of the 12 mixed-model readings: z-scoring over the whole 26 s trial finds\nno delta cluster, while z-scoring against the 2 s baseline finds AVERSIVE\nbelow NEUTRAL over 14.3 s of the 24 s block in the nSOZ amygdalae and 15.6 s\nin all 14. No reading finds the HGP increase in the first 2 s (smallest\ncluster p 0.056); the three HGP clusters that begin there are variants, and\nall use a baseline other than the 1 s clip. The group test finds no HGP\ncluster, so the MI claims rest on fixed windows of 0 to 2 s for HGP and 0 to\n24 s for delta, taken from the Results' text, an assumption; under them no\nreading gives all 28 Table 2 values within tolerance (at best 4 of 28), the\ndelta and HGP MIs correlate at r = -0.30 (p = 0.30) where the printed values\ngive -0.74, and `fig1f-hgp-more-specific-than-delta` is blocked as the\nreadings disagree. `table2-delta-reduced-12-of-14` is partially reproduced,\nas the claims file's readings give 11, 11 and 12 and only the fixed-window\ntrial reading gives 10. Among the neuron claims, `neuron-count` is partially\nreproduced (42 units, within 4.1 of 41, but in 8 amygdalae, not 9), the mean\nfiring rate variability is 0.033 plus or minus 0.690 Hz with 27 of 42 units\npositive (p = 0.50), the SSI correlation is 0.26 (p = 0.11) and 0.40 against\n0.78, the FRV coefficient of `fig4b-regression-firing-hgp` has p 0.07 to\n0.65, and `fig3b-firing-hgp-no-condition-difference` is partially reproduced,\nholding in 4 of 6 readings. The author's first run gave four reproduced,\nthree partially, ten not reproduced and eight blocked. The author asked a\nreader no questions, so the answer run and the following author run changed\nnothing. Round 1 agreed with 20 of 25 outcomes; it found that outcomes were\njudged on readings the author had chosen (baseline z-scoring, the 1 s fig3b\nreading and an added trialsd z-scoring), that the per-trial baseline SD rests\non about 2 independent values, that the per-amygdala window set MIs to 0\nwhere it found no cluster, that SSI did not check microwire identity, and\nthat the fig3b smoothing mixed neighbouring blocks. Judging on the claims\nfile's three z-scorings, leaving such MIs undefined and smoothing each block\non its own moved `nsoz-delta-hgp-mi-inverse` from reproduced to not\nreproduced, table2-delta-reduced-12-of-14 and fig3b from reproduced to\npartially, fig1f from reproduced to blocked and fig4b from partially to not\nreproduced; two questions to a reader, on the binomial interval and on the\nprinted Table 2 values of Fig. 1E, were put during the revision after the\nanswer step. Round 2 agreed with all 25; it asked that the outcomes resting\non the fixed windows be marked assumed, which all but fig1f now are, as the\nrecord's schema allows the mark only on outcomes that are not blocked, asked\nwhy fig3b is partial and not blocked, which the notes now say, and found\nsentences the outputs did not support, among them four channel locations not\nnaming the amygdala where there are five and two HGP clusters in the first\n2 s left out, which were corrected. The author's run took about 37 minutes\n(21:07 to 21:44 UTC), with two small coding errors fixed during development.\nThe notebook ran in about 2.7 min at first and in 4.8 min in the last run.\n\nThe BOLD time courses of the clinical fMRI, on which six claims rest, are not\npublic: the dandiset holds none, the OpenNeuro version (ds003374, 1.1.1)\nholds only iEEG, and the paper names no deposit. The continuous microwire\nsignals behind muHGP are not deposited either, only spike times and mean\nwaveforms, and each unit is assigned only to the bipolar macro channel of its\namygdala, with no microwire, so the spatial synchronisation index cannot be\ncomputed as defined; a spike train test flags 4 of 116 testable pairs as\nlikely sharing a wire. The units are in 8 amygdalae of 5 patients (1 L and R,\n2 L and R, 3 L, 4 L, 7 L and R), while the paper's Results give 9 amygdalae\nand its Table 1 lists multi-unit activity for patients 5 and 8 and none for\n7; three of the 8 (1 R, 2 R, 7 R, with 17 units) are SOZ amygdalae, though\nDiscussion 3.4 says there were no microwire recordings from SOZ amygdalae,\nand their mean rate is 4.65 plus or minus 3.91 Hz against the data\ndescriptor's 1.66 plus or minus 2.65 Hz. Every unit's obs_intervals cover all\n17 epochs, but the 16 units of subject 7 have no spike after 286 s and four\nunits of subject 2 none in epoch 1, at rates of 1 to 16 Hz elsewhere. Each\nsession is deposited twice, as `_ecephys.nwb` and `_ecephys+image.nwb`, with\nidentical iEEG, spikes and trials, so the 18 NWB files hold 9 recordings. The\niEEG is stated in volts, but its values (standard deviation 15 to 101, up to\n1546) are microvolts. The trial table gives trial 1 as 0 to 26 s, including\nits 2 s baseline clip, and trials 2 to 17 as their 24 s blocks only, and the\niEEG timestamps run without a gap from 0 to 442 s though the 17 epochs are\nnot contiguous (median step 12 to 36 at the boundaries against 1.4 to 1.9\nwithin epochs). The ages of subjects 2 and 8 (39 and 24) differ from those in\nthe paper and the data descriptor (48 and 27), and subject 2's file holds the\nsame subject metadata as subject 7's. The right channel of subjects 1, 5 and\n9 is located in the \"Right Hippocampus, rostral hippocampus\" and both\nchannels of subject 6 are \"unknown\", though their labels, the paper and the\ndata descriptor place them in the amygdala. Run on the paper's printed Table\n2 values, the Fig. 1E tests find the DELTA MI also different between nSOZ\nand SOZ amygdalae (rank-sum p = 0.035, t-test p = 0.013), the chi-square\ntest of Fig. 1F gives p = 0.0098 (0.053 with Yates' correction), not about\n0.2, and no single binomial interval method gives all three printed\nintervals. Three questions are put to the paper's authors: how the power\nenvelopes were z-scored within each trial, as a z-score over the whole trial\nremoves the sustained delta decrease and a z-score against the baseline keeps\nit, over which window each amygdala's MI was computed, and on what time base\nand over which span the Fig. 3B correlations of firing with HGP were\ncomputed.\n\nThe author's points on the protocol: several criteria ask for a result under\nevery reading while the per-amygdala cluster reading leaves most values at 0\nin these data, and outcomes were judged on the readings the data can carry;\nfor a claim of absence with several open details, judging on the paper's\ntest alone leaves those details open, and one reading was adopted as an\nassumption; `measured` cannot mark an expected value that cannot be tested,\nso the first expected value alone was given; neighbouring claims settle the\nsame open detail differently, as fig1b's criterion forces a block when\nreadings disagree while the others allow an assumption; and the rule against\nbold conflicts with the bold headers of the example notebook.\n"
}
```

```
File created successfully at: docs/pilot-notes/000576-fedele-2020-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n -i "—\|rather\|\*\*" docs/pilot-notes/000576-fedele-2020-01.md; git status --short
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
?? docs/pilot-notes/000576-fedele-2020-01.md
?? scripts
```

**Agent**

I wrote the notes to `docs/pilot-notes/000576-fedele-2020-01.md` and changed no other file. The file contains no em dashes, no "rather" and no bold. The other untracked files in the checkout (`.bashrc`, `scripts/` and so on) are sandbox leftovers that were already there before this run, as the author's reports also say; I left them alone. Here is the section:

# 000576, Fedele et al. 2020

No claim reproduced, three partially, 12 not reproduced and three blocked on the dandiset; with outside data, counted apart, one partially reproduced and six blocked. The first verification round agreed with 20 of 25 outcomes and the second with all 25, so there was no third round. It pins version 0.231010.1811, the only published version; the paper predates the dandiset and cites none. The paper, Fedele, Tzovara et al. in NeuroImage, records macroelectrode iEEG and microwire units in the 14 amygdalae of nine patients with drug-resistant mesial temporal lobe epilepsy while they watch blocks of dynamic fearful faces (AVERSIVE) and landscapes (NEUTRAL), and relates a sustained delta power decrease and an onset increase in high gamma power (HGP) to neuronal firing and to the BOLD signal of a pre-operative fMRI, with the HGP modulation index (MI) separating amygdalae outside the seizure onset zone (nSOZ) from those within it (SOZ). The claims were written from the version of record, a PDF supplied by a person; the paper links no analysis code, and the data descriptor (Fedele et al. 2021) was read for the layout of the data only. The iEEG and spike claims were tested; the six claims that need the BOLD time courses and the muHGP claim are blocked as `data_missing`, and `fig3d-firing-correlations-modalities` was tested on its HGP part only. `fig1b-delta-decrease` is blocked as `methods_underspecified`, as it holds in 6 of the 12 mixed-model readings: z-scoring over the whole 26 s trial finds no delta cluster, while z-scoring against the 2 s baseline finds AVERSIVE below NEUTRAL over 14.3 s of the 24 s block in the nSOZ amygdalae and 15.6 s in all 14. No reading finds the HGP increase in the first 2 s (smallest cluster p 0.056); the three HGP clusters that begin there are variants, and all use a baseline other than the 1 s clip. The group test finds no HGP cluster, so the MI claims rest on fixed windows of 0 to 2 s for HGP and 0 to 24 s for delta, taken from the Results' text, an assumption; under them no reading gives all 28 Table 2 values within tolerance (at best 4 of 28), the delta and HGP MIs correlate at r = -0.30 (p = 0.30) where the printed values give -0.74, and `fig1f-hgp-more-specific-than-delta` is blocked as the readings disagree. `table2-delta-reduced-12-of-14` is partially reproduced, as the claims file's readings give 11, 11 and 12 and only the fixed-window trial reading gives 10. Among the neuron claims, `neuron-count` is partially reproduced (42 units, within 4.1 of 41, but in 8 amygdalae, not 9), the mean firing rate variability is 0.033 plus or minus 0.690 Hz with 27 of 42 units positive (p = 0.50), the SSI correlation is 0.26 (p = 0.11) and 0.40 against 0.78, the FRV coefficient of `fig4b-regression-firing-hgp` has p 0.07 to 0.65, and `fig3b-firing-hgp-no-condition-difference` is partially reproduced, holding in 4 of 6 readings. The author's first run gave four reproduced, three partially, ten not reproduced and eight blocked. The author asked a reader no questions, so the answer run and the following author run changed nothing. Round 1 agreed with 20 of 25 outcomes; it found that outcomes were judged on readings the author had chosen (baseline z-scoring, the 1 s fig3b reading and an added trialsd z-scoring), that the per-trial baseline SD rests on about 2 independent values, that the per-amygdala window set MIs to 0 where it found no cluster, that SSI did not check microwire identity, and that the fig3b smoothing mixed neighbouring blocks. Judging on the claims file's three z-scorings, leaving such MIs undefined and smoothing each block on its own moved `nsoz-delta-hgp-mi-inverse` from reproduced to not reproduced, table2-delta-reduced-12-of-14 and fig3b from reproduced to partially, fig1f from reproduced to blocked and fig4b from partially to not reproduced; two questions to a reader, on the binomial interval and on the printed Table 2 values of Fig. 1E, were put during the revision after the answer step. Round 2 agreed with all 25; it asked that the outcomes resting on the fixed windows be marked assumed, which all but fig1f now are, as the record's schema allows the mark only on outcomes that are not blocked, asked why fig3b is partial and not blocked, which the notes now say, and found sentences the outputs did not support, among them four channel locations not naming the amygdala where there are five and two HGP clusters in the first 2 s left out, which were corrected. The author's run took about 37 minutes (21:07 to 21:44 UTC), with two small coding errors fixed during development. The notebook ran in about 2.7 min at first and in 4.8 min in the last run.

The BOLD time courses of the clinical fMRI, on which six claims rest, are not public: the dandiset holds none, the OpenNeuro version (ds003374, 1.1.1) holds only iEEG, and the paper names no deposit. The continuous microwire signals behind muHGP are not deposited either, only spike times and mean waveforms, and each unit is assigned only to the bipolar macro channel of its amygdala, with no microwire, so the spatial synchronisation index cannot be computed as defined; a spike train test flags 4 of 116 testable pairs as likely sharing a wire. The units are in 8 amygdalae of 5 patients (1 L and R, 2 L and R, 3 L, 4 L, 7 L and R), while the paper's Results give 9 amygdalae and its Table 1 lists multi-unit activity for patients 5 and 8 and none for 7; three of the 8 (1 R, 2 R, 7 R, with 17 units) are SOZ amygdalae, though Discussion 3.4 says there were no microwire recordings from SOZ amygdalae, and their mean rate is 4.65 plus or minus 3.91 Hz against the data descriptor's 1.66 plus or minus 2.65 Hz. Every unit's obs_intervals cover all 17 epochs, but the 16 units of subject 7 have no spike after 286 s and four units of subject 2 none in epoch 1, at rates of 1 to 16 Hz elsewhere. Each session is deposited twice, as `_ecephys.nwb` and `_ecephys+image.nwb`, with identical iEEG, spikes and trials, so the 18 NWB files hold 9 recordings. The iEEG is stated in volts, but its values (standard deviation 15 to 101, up to 1546) are microvolts. The trial table gives trial 1 as 0 to 26 s, including its 2 s baseline clip, and trials 2 to 17 as their 24 s blocks only, and the iEEG timestamps run without a gap from 0 to 442 s though the 17 epochs are not contiguous (median step 12 to 36 at the boundaries against 1.4 to 1.9 within epochs). The ages of subjects 2 and 8 (39 and 24) differ from those in the paper and the data descriptor (48 and 27), and subject 2's file holds the same subject metadata as subject 7's. The right channel of subjects 1, 5 and 9 is located in the "Right Hippocampus, rostral hippocampus" and both channels of subject 6 are "unknown", though their labels, the paper and the data descriptor place them in the amygdala. Run on the paper's printed Table 2 values, the Fig. 1E tests find the DELTA MI also different between nSOZ and SOZ amygdalae (rank-sum p = 0.035, t-test p = 0.013), the chi-square test of Fig. 1F gives p = 0.0098 (0.053 with Yates' correction), not about 0.2, and no single binomial interval method gives all three printed intervals. Three questions are put to the paper's authors: how the power envelopes were z-scored within each trial, as a z-score over the whole trial removes the sustained delta decrease and a z-score against the baseline keeps it, over which window each amygdala's MI was computed, and on what time base and over which span the Fig. 3B correlations of firing with HGP were computed.

The author's points on the protocol: several criteria ask for a result under every reading while the per-amygdala cluster reading leaves most values at 0 in these data, and outcomes were judged on the readings the data can carry; for a claim of absence with several open details, judging on the paper's test alone leaves those details open, and one reading was adopted as an assumption; `measured` cannot mark an expected value that cannot be tested, so the first expected value alone was given; neighbouring claims settle the same open detail differently, as fig1b's criterion forces a block when readings disagree while the others allow an assumption; and the rule against bold conflicts with the bold headers of the example notebook.

## End of run

13 turns, 2 minutes, result: success.
