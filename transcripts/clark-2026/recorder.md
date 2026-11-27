# clark-2026 · recorder · run 45918047136

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/clark-2026/; python tools/readme_row.py clark-2026; ls summaries | head
```

```
docs/pilot-notes/allen-2026-01.md
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/amjad-2025-02.md
docs/pilot-notes/andreassen-2022-01.md
docs/pilot-notes/andrews-2024-01.md
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
| [000939](https://dandiarchive.org/dandiset/000939) | [Clark et al. 2026](https://doi.org/10.1038/s41593-026-02452-4) | 17 | 3 | 0 | 0 | [`clark-2026`](entries/clark-2026) |
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
for f in docs/pilot-notes/{allen-2026-01,amjad-2025-01,amjad-2025-02,andreassen-2022-01,andrews-2024-01,knierim-2000-02}.md; do echo "== $f"; cat $f; done; grep -n -m3 "^|" README.md | head -3; echo; cat summaries/allen-2026-01.md summaries/amjad-2025-02.md
```

```
<persisted-output>
Output too large (33.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/33a5fcc5-7aa5-4096-9a64-7a3d2b241e0d/tool-results/bc8ocltck.txt

Preview (first 2KB):
== docs/pilot-notes/allen-2026-01.md
# allen-2026, Allen et al. 2026

Fifteen claims reproduced on the dataset, one partially, one not reproduced
and four blocked, all four for missing data; the ten transcriptomic claims,
whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
counted apart, with seven reproduced, two partially and one not reproduced.
One outcome, `fig4a-pca`, rests on an assumption. The first verification round
agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
reproduced where the record had not reproduced, and
`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
where it had reproduced; the author took all three. The second round agreed
with all 31, and nothing was proposed after it, so there was no third round. It
pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
drives behavioral plasticity and visual integration under environmental
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/clark-2026-01.yaml claims/clark-2026.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if '000939' in json.dumps(x)[:300]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (125.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/33a5fcc5-7aa5-4096-9a64-7a3d2b241e0d/tool-results/bonyl830h.txt

Preview (first 2KB):
schema_version: 3
id: clark-2026-01
datasets:
- archive: dandi
  id: 000939
  version: 0.240528.1542
  doi: 10.48324/dandi.000939/0.240528.1542
  relation: reuses
paper: doi:10.1038/s41593-026-02452-4
date: 2026-11-26
entry: clark-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/33a5fcc5-7aa5-4096-9a64-7a3d2b241e0d/tool-results/bc8ocltck.txt"
}
```

```
1	== docs/pilot-notes/allen-2026-01.md
2	# allen-2026, Allen et al. 2026
3	
4	Fifteen claims reproduced on the dataset, one partially, one not reproduced
5	and four blocked, all four for missing data; the ten transcriptomic claims,
6	whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
7	counted apart, with seven reproduced, two partially and one not reproduced.
8	One outcome, `fig4a-pca`, rests on an assumption. The first verification round
9	agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
10	reproduced where the record had not reproduced, and
11	`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
12	where it had reproduced; the author took all three. The second round agreed
13	with all 31, and nothing was proposed after it, so there was no third round. It
14	pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
15	al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
16	drives behavioral plasticity and visual integration under environmental
17	acidification" (Communications Biology 9:229), rears bigfin reef squid at pH
18	8.2, with 7 days at pH 7.8 after 90 days (acute-OA) or at pH 7.8 from hatching
19	(chronic-OA), and reports a higher metabolic rate, lower ammonia excretion and
20	higher blood pH, PCO2 and [HCO3-] under chronic-OA, more time in the upper half
[... 453 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/33a5fcc5-7aa5-4096-9a64-7a3d2b241e0d/tool-results/bonyl830h.txt"
}
```

```
1	schema_version: 3
2	id: clark-2026-01
3	datasets:
4	- archive: dandi
5	  id: 000939
6	  version: 0.240528.1542
7	  doi: 10.48324/dandi.000939/0.240528.1542
8	  relation: reuses
9	paper: doi:10.1038/s41593-026-02452-4
10	date: 2026-11-26
11	entry: clark-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 743 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/33a5fcc5-7aa5-4096-9a64-7a3d2b241e0d/tool-results/bonyl830h.txt",
 "offset": 764,
 "limit": 400
}
```

```
764	    response: Outcome kept; nothing in the report bears on it beyond agreement.
765	  - claim: fig7c-dmft-integrates-behavior
766	    agrees: true
767	    outcome: reproduced
768	    reason: 'Cell 9: median error 0.0315 rad, circular r 0.998.'
769	    response: Outcome kept; nothing in the report bears on it beyond agreement.
770	  - claim: fig8-grid-scores-and-torus
771	    agrees: false
772	    reason: 'Not tested: no notebook cell, and the notebook points to an attempt record the verifier did
773	      not have. The claim needs only the paper''s code, not the archive. Problem 9: it has no outputs
774	      in any notebook, so it has no outcome.'
775	    response: 'Kept blocked (too_large): the 25,000-neuron network and the grid-score sweep do not fit
776	      the run''s time. model_sims.ipynb now states the block in its own section.'
777	  - claim: figs10-robustness-comparable
778	    agrees: false
779	    reason: 'Not tested: no notebook cell, and the notebook points to an attempt record the verifier did
780	      not have. The claim needs only the paper''s code, not the archive. Problem 9: it has no outputs
781	      in any notebook, so it has no outcome.'
782	    response: 'Tested in the new notebook model_sims.ipynb, now reproduced, resting on an assumption (a
783	      continuum is at least 31 of 34 distinct states): both networks keep 34 states at noise 0, and at
[... 380 more lines not kept]
```

**Agent**

Read the attempt record. Next, the claim kinds, the outcome-count columns and the dataset entry.

**Agent calls Bash**

```bash
grep -n -B1 -A3 "Dandiset | Paper\|^| Dandiset\|^| Data" README.md | head; python - <<'E'
import yaml
c=yaml.safe_load(open('claims/clark-2026.yaml'))
a=yaml.safe_load(open('attempts/clark-2026-01.yaml'))
o={x['claim']:x['outcome'] for x in a['outcomes']}
for x in c['claims']:
    print(x['id'],x.get('kind'),x['data'],o.get(x['id']),'|',x['source'][:80])
E
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
s=json.dumps(d)
i=s.find('"000939"'); print(s[i-200:i+1500])
E
```

```
hd-cell-selection link dataset reproduced | Methods, Statistics and reproducibility, Sample size and Data exclusions; Fig. 2
tuning-curves-match-cache link with_inputs reproduced | Methods, Data processing, Tuning-curve estimation; Data availability
fig1e-heterogeneous-peaks None dataset reproduced | Results, Failure of classical ring-attractor models, paragraph 3; Fig. 1e
fig5d-peak-numbers None dataset reproduced | Fig. 5d legend
fig1fg-mean-and-fluctuation-profiles None dataset reproduced | Results, Failure of classical ring-attractor models, paragraph 3; Fig. 1f,g
fig3ab-centers-of-mass-uniform None dataset reproduced | Results, Statistical generative process, paragraph 2; Methods, Statistics and re
fig3c-correlation-approaches-circulant None dataset reproduced | Results, Statistical generative process, paragraph 3; Fig. 3c; Supplementary Fig
fig4-generative-fit None dataset partially_reproduced | Results, Statistical generative process, paragraph 5; Fig. 4d to f; Methods, Mod
fig5ab-profiles-match None dataset reproduced | Results, Statistical generative process, paragraph 6; Fig. 5a,b
fig5c-peak-counts-match None dataset reproduced | Results, Statistical generative process, paragraph 6; Fig. 5c
fig5d-peak-heights-match None dataset reproduced | Results, Statistical generative process, paragraph 6; Fig. 5d
fig5e-flip-symmetry-match None dataset reproduced | Results, Statistical generative process, paragraph 6; Fig. 5e
fig5f-information-match None dataset reproduced | Results, Statistical generative process, paragraph 6; Fig. 5f; Methods, Tuning-c
fig2b-sorted-weights-mexican-hat None dataset reproduced | Results, Dynamics of the data-derived network model, paragraph 1; Fig. 2a,b
fig2ef-data-network-quasicontinuous None dataset reproduced | Results, Dynamics of the data-derived network model, paragraph 3; Fig. 2e,f
fig2gi-circulant-noise-collapses None dataset partially_reproduced | Results, Dynamics of the data-derived network model, paragraphs 4 and 5; Fig. 2c
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/readme_row.py; grep -n "Reproduced\|reproduced |" README.md | head -3
```

```
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 40 more lines not kept]
```

**Agent**

Counts confirmed: 17 reproduced, 3 partially on the dataset, with links and the nine simulation claims counted apart. Now the reports.

**Agent calls Bash**

```bash
cd transcripts/clark-2026; wc -w *-report.md; cat author-report.md
```

```
788 author-report.md
  678 author-revise-1-report.md
  610 author-revise-2-report.md
  567 claims-check-report.md
  571 claims-report.md
 1999 verifier-1-report.md
 1223 verifier-2-report.md
 6436 total
I've built the entry `entries/clark-2026` (four notebooks, two helpers), written `attempts/clark-2026-01.yaml` and built the handover package. `python tools/entry.py all` passed, `check` reports 0 errors, and nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| hd-cell-selection (link) | reproduced: all counts exact (31, 2,691, 1,533, 315, 117/93/90/86) |
| tuning-curves-match-cache (link, uses the Zenodo cache) | reproduced: r = 1.000000 on all 1,533 curves |
| fig1e-heterogeneous-peaks | reproduced |
| fig5d-peak-numbers | reproduced: data counts exact |
| fig1fg-mean-and-fluctuation-profiles | reproduced |
| fig3ab-centers-of-mass-uniform | reproduced: 2 sessions, 0 after correction, corrected P 0.592 to 0.968 |
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/clark-2026; for f in author-revise-1-report.md author-revise-2-report.md claims-report.md claims-check-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
I worked through every point in the round-1 report. Four outcomes changed, the entry passes its checks, and the last full run (77 min) matches the run before it line for line. Nothing is committed.

**Outcome changes**
- **figs11b (global stability of the data network): partially reproduced → reproduced, resting on an assumption.** I revised the threshold the verifier found unfair (problem 5). It now comes from the fig2ef runs redone with the same 5-ms step as the runs it judges, not from the 1-ms fig2ef run. Under it, 97% to 100% of final states are within the threshold at every spread, under all five seeds. The old 1-ms threshold is kept as a variant and still fails the 95% at three spreads.
- **Three claims that were blocked for time are now tested**, in a new notebook, `model_sims.ipynb`:
  - **figs1-s2 (spectrum does not fix the symmetry): partially reproduced, seed sensitive.** The dynamics match the legends under all five seeds. The eigenvalues of the two networks differ by 5.18% under the claim's seed, just outside the 5% asked. Over the five seeds they differ by 2.4% to 5.2%, and the paper's own seed-42 matrices differ by 3.3%.
  - **figs11-s12 (global and finite-N stability of the model): reproduced, resting on an assumption, seed sensitive.** The assumption is a threshold taken from the network's own fig2ef-style run. One of the four extra seeds gives 0.94, just under the 95%.
  - **figs10 (robustness to weight noise): reproduced, resting on an assumption.** I counted a network as keeping a continuum when at least 31 of its 34 states stay distinct. Both networks keep all 34 at noise 0; at noise 0.4 they end in 8 and 9 states.
- **fig8 stays blocked** as too large.

**Added or corrected**
- **fig4:** I added the outputs the verifier asked for. They are the paper's grid point at 500,000 samples under all five seeds (second each time), 90 points instead of 30 (same minimum), and a float32 pass over all 30 (same minimum). I also 
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/clark-2026; cat verifier-1-report.md verifier-2-report.md
```

```
**Verifier report, round 1: Clark, Abbott & Sompolinsky (2026) on DANDI:000939 (0.240528.1542)**

The claims file has 30 claims. The four notebooks test 26 of them; the other 4 appear in no notebook. No notebook treats any claim as blocked. I confirmed through the archive API that the pinned version has 31 assets, 9 of them `+ogen.nwb`, as `tuning_curves.ipynb` cell 3 shows.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| hd-cell-selection | reproduced | tuning_curves cell 10: 31 sessions, 2,691 units, 1,533 head-direction units under both readings, 0 dropped by nz_mask, 9 opto mice with 315 cells, and counts of 117/93/90/86 for the right mice. |
| tuning-curves-match-cache | reproduced | Cell 12: Pearson r = 1.000000 for 100% of 1,533 units; largest curve difference 1.4e-14. The cache's labels and session order equal the data's. |
| fig1e-heterogeneous-peaks | reproduced | Cell 16: peak counts of 1 to 6 occur; the interquartile range of the separation between the two highest peaks is 1.382 rad, above π/4. |
| fig5d-peak-numbers | reproduced | Cell 18: the data give exactly 1,533/412/55. Generative samples over five seeds give 23,908–24,267 curves with ≥2 peaks and 1,001–1,082 with ≥3, all within tolerance. |
| fig1fg-mean-and-fluctuation-profiles | reproduced | Cell 20: one maximum, at offset 0; symmetry r = 0.9998; sd/mean = 0.56, so both readings hold; median consistency r is 0.996 (mean) and 0.974 (sd). |
| fig3ab-centers-of-mass-uniform | reproduced | Cell 22: 2 sessions with uncorrected P < 0.05, 0 after BH correction, corrected P from 0.592 to 0.968. |
| fig3c-correlation-approaches-circulant | reproduced | Cell 24: the distance from circulant form falls monotonically for all 4 mice and both functions, under all 5 seeds. The leading 4 eigenvectors have ≥0.89 Fourier purity, and eigenvectors 1 and 2 are at frequency 1. |
| fig4-generative-fit | partially_reproduced | Cell 26: the 500k-sample pass chooses σ 1.4737 and β 3.1103, both within tolera
[... 138 more lines not kept]
```

**Agent**

I have all the sources. Writing the notes and the summary now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/clark-2026-01.md",
 "content": "# clark-2026, Clark et al. 2026\n\nSeventeen claims reproduced on the dandiset, three partially, none not\nreproduced and none blocked; the two link claims, on the cell counts and on the\npaper's cached tuning curves on Zenodo, both reproduced, and the eight theory\nand simulation claims run from the paper's code (`data: elsewhere`) are counted\napart, with five reproduced, one partially, one not reproduced and one blocked.\nThree outcomes, `figs11b-data-network-global-stability`,\n`figs10-robustness-comparable` and `figs11-s12-global-stability-model`, rest on\nan assumption, and three are seed sensitive. The first verification round\nagreed with all 26 outcomes it gave; the other four claims had been left\nblocked for lack of time and had no outputs, and in reply three of them\n(figs10, figs11-s12 and figs1-s2) were tested in a new notebook,\n`model_sims.ipynb`, and figs11b moved from partially reproduced to reproduced on\na threshold from the fig2ef protocol run with the same 5-ms step as the runs it\njudges. The second round agreed with all 30, and nothing was proposed after it,\nso there was no third round. It pins version 0.240528.1542, the version the\npaper cites. The paper, Clark, Abbott and Sompolinsky, \"Symmetries and\ncontinuous attractors in disordered neural circuits\" (Nature Neuroscience,\ndoi:10.1038/s41593-026-02452-4), takes the 1,533 head-direction cells recorded\nin mouse postsubiculum by Duszkiewicz et al. and reports that their tuning\ncurves are heterogeneous, with up to several peaks, yet have uniform centers of\nmass and a correlation that approaches circulant form, that a statistical\ngenerative process fitted to them matches their peak counts, peak heights, flip\nsymmetry and information, that a network built from the data has a\nquasi-continuous attractor that integrates angular velocity while a circulant\nnetwork plus noise collapses to a few states, and that a mean-field theory of\nthe large-network limit gives a Mexican-hat interaction and stable bumps, with\nan extension to grid cells. The claims were written from the version of record,\nits supplement and the paper's code at commit 245726f; the claims check\ncorrected the fig6cd statement (the eigenvalues are a ratio of Fourier\ncoefficients, not a product) and added `fig7de-dmft-timescales`, for 30 claims.\nThe cell counts are exact, the rebuilt tuning curves match the cache at r =\n1.000000, and every tuning-curve statistic and every match of Fig. 5\nreproduces. `fig4-generative-fit` is partial: the minimum is at sigma 1.4737,\nbeta 3.1103, b 1.2145 under all five seeds, and b is 0.52 from 1.73, outside\n0.173; the paper's grid point comes second. `fig2gi-circulant-noise-collapses`\nis partial because the circulant plus scrambled residuals ends in 4 states but\nthe sorted optimal matrix keeps 24 to 31 on the criterion's position measure,\nshort of 50, which that measure cannot reach even for the 100 initial states;\nread on the manifold angle, its final angles fill all 50 bins.\n`figs8-s9-lambda-and-c` holds in two of four parts: at lambda 1e-2 and c 1 the\nstates keep a radius of 4.6 against the threshold of 3.9, and the flow error at\n1e-8 is not below that at 1e-12, on the paper's cached flow errors as well.\nAmong the theory claims, `fig7de-dmft-timescales` is not reproduced, as the\nbump's convergence time runs from 2.87 to 20.5 tau and the uniform state's\ndivergence time from 0.15 to 3.83 tau, outside the claims file's reading of a\nfew tau; `figs1-s2-spectrum-does-not-fix-symmetry` is partial as the\neigenvalues of its two matrices differ by 5.18% against the 5% asked; and\n`fig8-grid-scores-and-torus` is blocked as too large, since its 25,000-neuron\nnetwork did not fit in the five hours of a revision run. The protocol's seeds\nwere used where the claims file names numpy seed 42, and the fig4 grid was run\nat 25,000 samples with its 30 best points again at 500,000, in place of 500,000\nat all 18,000 points. Round 1 also found that comparing smoothing widths with\n== gave a false 78.4%, that the figs14 doublets rest on only two real pairs,\nthat the round-1 figs11b threshold sat at the noise floor, and that the fig7\ncriterion tests only the second eigenvalue; questions on fig2gi and figs8-s9\nwent to a reader in `questions/clark-2026.yaml`. Round 2 found sentences the\noutputs did not support, on fig7de, fig7, figs8-s9, figs14, figs11b, figs10,\nfinding 3 and the run times, which were corrected, and two more questions, on\nfigs1-s2 and fig7, were added. The entry took about 52 minutes per run at\nfirst, with peak memory 1.7 GB, and a second run was needed because a float32\ndistance computation rounded distances below about 1e-3 to zero. With\n`model_sims.ipynb` the five notebooks took 1,147, 2,256, 613, 157 and 3,044 s\nin the run before the round-2 revision and 1,114, 1,709, 473, 150 and 2,356 s\nin that revision's run, which went one notebook per command because the\nsandbox ended a run left in the background, and in which the grid notebook\nfailed once on a network timeout. The flow error at lambda 1e-12 is not\nrepeated exactly between runs (2.6e-9 and 3.6e-9), as that solve is\nill-conditioned.\n\nEvery file was replaced after the cited version: in the latest published\nversion, 0.261016.2310, the 31 assets have new names with session ids and sizes\nof 12.7 to 30.2 GB, none shares a blob with 0.240528.1542, and the paper's code\nreads the cited version's file names (sub-<id>_behavior+ecephys[+ogen].nwb), so\na user of a later version has to map the files. At the cited version the 31\nfiles hold what the paper describes: one session per subject, 2,691 units of\nwhich 1,533 are labelled head-direction, all also labelled excitatory (the\npaper calls the cells excitatory and the code selects on is_head_direction\nalone, which here gives the same count), a wake_square epoch in every file,\nincluding the +ogen.nwb files, which settles the claims file's open question,\nhead direction in radians sampled every 10 ms, and nine files with a wake_opto\nepoch holding 315 head-direction cells. Spikes and head direction share a clock\n(in every session the head-direction information peaks within 0.05 s of lag 0\nand falls 4.5 times by 2 s), no recording appears twice and no spike train is\nunsorted; both findings are rated none. In the paper, the generative fit of\nFig. 4 has two near-equal minima on its grid, (sigma, b, beta) = (1.4211,\n1.7307, 2.7659) and (1.4737, 1.2145, 3.1103); with 500,000 samples in float64\nthe second has the lower error under all five seeds, and the ranking flips only\nin float32 under one seed and in the paper's own cached error grid on Zenodo,\nwhere the two are 1.1% apart, so the reported b of 1.73 is one of two choices\nthe fitting procedure can return. In the mean-field stability grid of Fig.\n7d,e, at 293 of the 800 grid points the bump Jacobian has no zero eigenvalue,\nalthough the bump there is not flat (amplitude median 0.95); at the paper's\nparameters the zero is present. The paper cites Zenodo record 21827768 for its\ncached results, where the code's README gives 21827767.\n\nThe author's points on the protocol: the claims file names numpy seed 42 where\nthe protocol requires seeds from crc32 of the claim id, and the protocol's\nseeds were used and recorded as a deviation; it has no rule for a criterion too\ncostly to run as written, such as fig4's 500,000 samples at 18,000 grid points\n(about 3 hours), which was run on a shortlist; it handles ties but not\nthresholds that cannot be met, such as fig2gi's 50 states, which was applied as\nwritten with a variant measure; the run stamp hashes every file in the entry,\nso writing conclusions after a run makes the next run a full one and writing\nresults from outputs costs two full runs; `data: elsewhere` fits pure\nsimulation claims poorly, and the paper's code at its commit was treated as the\ninput; `too_large` is named only where the computation stopped it, and it was\nused with cost estimates for claims never started; and the criteria leave\n\"collapse\" and \"merged into one state\" open, so every reading was run.\n"
}
```

```
File created successfully at: docs/pilot-notes/clark-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/clark-2026-01.md",
 "old_string": "curves are heterogeneous, with up to several peaks, yet have",
 "new_string": "curves are heterogeneous, often with more than one peak, yet have"
}
```

```
The file docs/pilot-notes/clark-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/clark-2026-01.md",
 "content": "The paper's main findings on mouse head-direction cells hold up in this data: their tuning curves are heterogeneous but statistically symmetric, a fitted statistical generative process matches their statistics, and a network built from them has a quasi-continuous attractor that integrates angular velocity. The generative fit lands on a second, near-equal minimum of the paper's grid, with a different value of one parameter. The contrast with a circulant network plus noise, which collapses to a few states, holds only in part, because the state count the test asks of the data network is out of its measure's reach. The mean-field theory reproduces, but its timescales fall outside the thresholds this record chose for \"a few\" time constants, and the grid-cell extension was too large to run.\n"
}
```

```
File created successfully at: summaries/clark-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/clark-2026-01.md docs/pilot-notes/clark-2026-01.md; grep -nci "rather\|—" summaries/clark-2026-01.md docs/pilot-notes/clark-2026-01.md; git status --short
```

```
126 summaries/clark-2026-01.md
1320 docs/pilot-notes/clark-2026-01.md
1446 total
summaries/clark-2026-01.md:0
docs/pilot-notes/clark-2026-01.md:0
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
?? docs/pilot-notes/clark-2026-01.md
?? scripts
?? summaries/clark-2026-01.md
```

**Agent**

The summary is 126 words, over the limit; trimming it.

**Agent calls Write**

```json
{
 "file_path": "summaries/clark-2026-01.md",
 "content": "The paper's main findings on mouse head-direction cells hold up in this data: their tuning curves are heterogeneous but statistically symmetric, a fitted statistical generative process matches their statistics, and a network built from them has a quasi-continuous attractor that integrates angular velocity. The generative fit lands on a second, near-equal minimum of the paper's grid, with one parameter different. The contrast with a circulant network plus noise, which collapses to a few states, holds only in part, as the state count the test asks of the data network is beyond its measure's reach. The mean-field theory reproduces, but its timescales exceed the thresholds this record chose for \"a few\" time constants. The grid-cell extension was too large to run.\n"
}
```

```
The file summaries/clark-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/clark-2026-01.md
```

```
120 summaries/clark-2026-01.md
```

**Agent calls Write**

```json
{
 "file_path": "summaries/clark-2026-01.md",
 "content": "The paper's main findings on mouse head-direction cells hold up in this data: their tuning curves are heterogeneous but statistically symmetric, a fitted statistical generative process matches their statistics, and a network built from them has a quasi-continuous attractor that integrates angular velocity. The generative fit lands on a second, near-equal minimum of the paper's grid, with one parameter different. The contrast with a circulant network plus noise, which collapses to a few states, holds only in part, as the state count asked of the data network is beyond its measure's reach. The mean-field theory reproduces, but its timescales exceed the thresholds this record chose for \"a few\" time constants. The grid-cell extension was too large to run.\n"
}
```

```
The file summaries/clark-2026-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/clark-2026-01.md; cat docs/pilot-notes/clark-2026-01.md
```

```
118 summaries/clark-2026-01.md
# clark-2026, Clark et al. 2026

Seventeen claims reproduced on the dandiset, three partially, none not
reproduced and none blocked; the two link claims, on the cell counts and on the
paper's cached tuning curves on Zenodo, both reproduced, and the eight theory
and simulation claims run from the paper's code (`data: elsewhere`) are counted
apart, with five reproduced, one partially, one not reproduced and one blocked.
Three outcomes, `figs11b-data-network-global-stability`,
`figs10-robustness-comparable` and `figs11-s12-global-stability-model`, rest on
an assumption, and three are seed sensitive. The first verification round
agreed with all 26 outcomes it gave; the other four claims had been left
blocked for lack of time and had no outputs, and in reply three of them
(figs10, figs11-s12 and figs1-s2) were tested in a new notebook,
`model_sims.ipynb`, and figs11b moved from partially reproduced to reproduced on
a threshold from the fig2ef protocol run with the same 5-ms step as the runs it
judges. The second round agreed with all 30, and nothing was proposed after it,
so there was no third round. It pins version 0.240528.1542, the version the
paper cites. The paper, Clark, Abbott and Sompolinsky, "Symmetries and
continuous attractors in disordered neural circuits" (Nature Neuroscience,
[... 91 more lines not kept]
```

**Agent**

I wrote both files and changed nothing else. `docs/pilot-notes/clark-2026-01.md` is about 1,320 words, the same length as the recent notes, and `summaries/clark-2026-01.md` is 118 words in five sentences. The counts in the notes are the ones `tools/readme_row.py clark-2026` prints: 17 reproduced, 3 partially, 0 not reproduced and 0 blocked. The `catalystneuro` field for 000939 is empty, so the dataset paragraph does not open with the CatalystNeuro sentence. Nothing is committed.

`git status` also lists untracked files I did not create (`.bashrc`, `.gitconfig`, `.idea`, `.vscode`, `scripts` and a few others). I left them alone.

# clark-2026, Clark et al. 2026

Seventeen claims reproduced on the dandiset, three partially, none not
reproduced and none blocked; the two link claims, on the cell counts and on the
paper's cached tuning curves on Zenodo, both reproduced, and the eight theory
and simulation claims run from the paper's code (`data: elsewhere`) are counted
apart, with five reproduced, one partially, one not reproduced and one blocked.
Three outcomes, `figs11b-data-network-global-stability`,
`figs10-robustness-comparable` and `figs11-s12-global-stability-model`, rest on
an assumption, and three are seed sensitive. The first verification round
agreed with all 26 outcomes it gave; the other four claims had been left
blocked for lack of time and had no outputs, and in reply three of them
(figs10, figs11-s12 and figs1-s2) were tested in a new notebook,
`model_sims.ipynb`, and figs11b moved from partially reproduced to reproduced on
a threshold from the fig2ef protocol run with the same 5-ms step as the runs it
judges. The second round agreed with all 30, and nothing was proposed after it,
so there was no third round. It pins version 0.240528.1542, the version the
paper cites. The paper, Clark, Abbott and Sompolinsky, "Symmetries and
continuous attractors in disordered neural circuits" (Nature Neuroscience,
doi:10.1038/s41593-026-02452-4), takes the 1,533 head-direction cells recorded
in mouse postsubiculum by Duszkiewicz et al. and reports that their tuning
curves are heterogeneous, often with more than one peak, yet have uniform centers of
mass and a correlation that approaches circulant form, that a statistical
generative process fitted to them matches their peak counts, peak heights, flip
symmetry and information, that a network built from the data has a
quasi-continuous attractor that integrates angular velocity while a circulant
network plus noise collapses to a few states, and that a mean-field theory of
the large-network limit gives a Mexican-hat interaction and stable bumps, with
an extension to grid cells. The claims were written from the version of record,
its supplement and the paper's code at commit 245726f; the claims check
corrected the fig6cd statement (the eigenvalues are a ratio of Fourier
coefficients, not a product) and added `fig7de-dmft-timescales`, for 30 claims.
The cell counts are exact, the rebuilt tuning curves match the cache at r =
1.000000, and every tuning-curve statistic and every match of Fig. 5
reproduces. `fig4-generative-fit` is partial: the minimum is at sigma 1.4737,
beta 3.1103, b 1.2145 under all five seeds, and b is 0.52 from 1.73, outside
0.173; the paper's grid point comes second. `fig2gi-circulant-noise-collapses`
is partial because the circulant plus scrambled residuals ends in 4 states but
the sorted optimal matrix keeps 24 to 31 on the criterion's position measure,
short of 50, which that measure cannot reach even for the 100 initial states;
read on the manifold angle, its final angles fill all 50 bins.
`figs8-s9-lambda-and-c` holds in two of four parts: at lambda 1e-2 and c 1 the
states keep a radius of 4.6 against the threshold of 3.9, and the flow error at
1e-8 is not below that at 1e-12, on the paper's cached flow errors as well.
Among the theory claims, `fig7de-dmft-timescales` is not reproduced, as the
bump's convergence time runs from 2.87 to 20.5 tau and the uniform state's
divergence time from 0.15 to 3.83 tau, outside the claims file's reading of a
few tau; `figs1-s2-spectrum-does-not-fix-symmetry` is partial as the
eigenvalues of its two matrices differ by 5.18% against the 5% asked; and
`fig8-grid-scores-and-torus` is blocked as too large, since its 25,000-neuron
network did not fit in the five hours of a revision run. The protocol's seeds
were used where the claims file names numpy seed 42, and the fig4 grid was run
at 25,000 samples with its 30 best points again at 500,000, in place of 500,000
at all 18,000 points. Round 1 also found that comparing smoothing widths with
== gave a false 78.4%, that the figs14 doublets rest on only two real pairs,
that the round-1 figs11b threshold sat at the noise floor, and that the fig7
criterion tests only the second eigenvalue; questions on fig2gi and figs8-s9
went to a reader in `questions/clark-2026.yaml`. Round 2 found sentences the
outputs did not support, on fig7de, fig7, figs8-s9, figs14, figs11b, figs10,
finding 3 and the run times, which were corrected, and two more questions, on
figs1-s2 and fig7, were added. The entry took about 52 minutes per run at
first, with peak memory 1.7 GB, and a second run was needed because a float32
distance computation rounded distances below about 1e-3 to zero. With
`model_sims.ipynb` the five notebooks took 1,147, 2,256, 613, 157 and 3,044 s
in the run before the round-2 revision and 1,114, 1,709, 473, 150 and 2,356 s
in that revision's run, which went one notebook per command because the
sandbox ended a run left in the background, and in which the grid notebook
failed once on a network timeout. The flow error at lambda 1e-12 is not
repeated exactly between runs (2.6e-9 and 3.6e-9), as that solve is
ill-conditioned.

Every file was replaced after the cited version: in the latest published
version, 0.261016.2310, the 31 assets have new names with session ids and sizes
of 12.7 to 30.2 GB, none shares a blob with 0.240528.1542, and the paper's code
reads the cited version's file names (sub-<id>_behavior+ecephys[+ogen].nwb), so
a user of a later version has to map the files. At the cited version the 31
files hold what the paper describes: one session per subject, 2,691 units of
which 1,533 are labelled head-direction, all also labelled excitatory (the
paper calls the cells excitatory and the code selects on is_head_direction
alone, which here gives the same count), a wake_square epoch in every file,
including the +ogen.nwb files, which settles the claims file's open question,
head direction in radians sampled every 10 ms, and nine files with a wake_opto
epoch holding 315 head-direction cells. Spikes and head direction share a clock
(in every session the head-direction information peaks within 0.05 s of lag 0
and falls 4.5 times by 2 s), no recording appears twice and no spike train is
unsorted; both findings are rated none. In the paper, the generative fit of
Fig. 4 has two near-equal minima on its grid, (sigma, b, beta) = (1.4211,
1.7307, 2.7659) and (1.4737, 1.2145, 3.1103); with 500,000 samples in float64
the second has the lower error under all five seeds, and the ranking flips only
in float32 under one seed and in the paper's own cached error grid on Zenodo,
where the two are 1.1% apart, so the reported b of 1.73 is one of two choices
the fitting procedure can return. In the mean-field stability grid of Fig.
7d,e, at 293 of the 800 grid points the bump Jacobian has no zero eigenvalue,
although the bump there is not flat (amplitude median 0.95); at the paper's
parameters the zero is present. The paper cites Zenodo record 21827768 for its
cached results, where the code's README gives 21827767.

The author's points on the protocol: the claims file names numpy seed 42 where
the protocol requires seeds from crc32 of the claim id, and the protocol's
seeds were used and recorded as a deviation; it has no rule for a criterion too
costly to run as written, such as fig4's 500,000 samples at 18,000 grid points
(about 3 hours), which was run on a shortlist; it handles ties but not
thresholds that cannot be met, such as fig2gi's 50 states, which was applied as
written with a variant measure; the run stamp hashes every file in the entry,
so writing conclusions after a run makes the next run a full one and writing
results from outputs costs two full runs; `data: elsewhere` fits pure
simulation claims poorly, and the paper's code at its commit was treated as the
input; `too_large` is named only where the computation stopped it, and it was
used with cost estimates for claims never started; and the criteria leave
"collapse" and "merged into one state" open, so every reading was run.

---

The paper's main findings on mouse head-direction cells hold up in this data: their tuning curves are heterogeneous but statistically symmetric, a fitted statistical generative process matches their statistics, and a network built from them has a quasi-continuous attractor that integrates angular velocity. The generative fit lands on a second, near-equal minimum of the paper's grid, with one parameter different. The contrast with a circulant network plus noise, which collapses to a few states, holds only in part, as the state count asked of the data network is beyond its measure's reach. The mean-field theory reproduces, but its timescales exceed the thresholds this record chose for "a few" time constants. The grid-cell extension was too large to run.

## End of run

20 turns, 3 minutes, $1.32 at API prices, result: success.
