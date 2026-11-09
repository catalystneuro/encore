# crcns-bf-1 · recorder · run 42163491667

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/crcns-bf-1/ transcripts/crcns-bf-1/; python tools/readme_row.py crcns-bf-1; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if 'bf-1' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
docs/pilot-notes/001863-welch-2025-01.md
docs/pilot-notes/001708-ashworth-2025-01.md
docs/pilot-notes/001710-plitt-2023-01.md
docs/pilot-notes/001250-laquitaine-2024-01.md
docs/pilot-notes/001847-bech-2026-01.md
claims/crcns-bf-1/:
10.1073-pnas.1712431115.yaml

transcripts/crcns-bf-1/:
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
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A12 'bf-1' targets/dandisets.json | head -40; head -5 README.md; grep -n 'readme_row\|Reproduced\|Partially' README.md | head; for f in docs/pilot-notes/001863-welch-2025-01.md docs/pilot-notes/001708-ashworth-2025-01.md docs/pilot-notes/001710-plitt-2023-01.md docs/pilot-notes/001250-laquitaine-2024-01.md docs/pilot-notes/001847-bech-2026-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "== $f"; cat $f; done
```

```
<persisted-output>
Output too large (58KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2462a374-1280-4bdb-85de-ec08ba5b1f32/tool-results/b4teyyt0l.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
== docs/pilot-notes/001863-welch-2025-01.md
# 001863, Welch et al. 2025

Twenty-two claims reproduced (one on an assumption), two partially (one on an
assumption), two not reproduced and nine blocked, all nine for missing data;
the link claim the author added, `htr-event-link`, is reproduced and not
counted. The first verification round agreed with 33 of the 36 outcomes as
they stood and the second with all 36; nothing was proposed after the second,
so there was no third round. It pins version 0.260806.2109, the published
version. The paper, Welch, Gonzales-Hess, Tarvin, Connor and Smear, "The
impact of a psychedelic drug on olfactory search behavior by mice", a bioRxiv
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2462a374-1280-4bdb-85de-ec08ba5b1f32/tool-results/b4teyyt0l.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	== docs/pilot-notes/001863-welch-2025-01.md
7	# 001863, Welch et al. 2025
8	
9	Twenty-two claims reproduced (one on an assumption), two partially (one on an
10	assumption), two not reproduced and nine blocked, all nine for missing data;
11	the link claim the author added, `htr-event-link`, is reproduced and not
12	counted. The first verification round agreed with 33 of the 36 outcomes as
13	they stood and the second with all 36; nothing was proposed after the second,
14	so there was no third round. It pins version 0.260806.2109, the published
15	version. The paper, Welch, Gonzales-Hess, Tarvin, Connor and Smear, "The
16	impact of a psychedelic drug on olfactory search behavior by mice", a bioRxiv
17	preprint, gives 22 C57Bl6/J mice (12 female, 10 male) one DOI session (3
18	mg/kg IP) and one saline session, crossed over at least a week apart, in a
19	two-alternative olfactory search task with 10% odor omission trials, and
20	compares accuracy, trial counts and durations, reward-port durations, speed
[... 792 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^| Dataset\|^|---\|^| ---' README.md | head -3; grep -n 'bf-1' -A15 targets/dandisets.json | head -30; wc -l attempts/crcns-bf-1-nair-2018-01.yaml claims/crcns-bf-1/*.yaml transcripts/crcns-bf-1/*-report.md; ls docs/pilot-notes | grep -i crcns
```

```
752 attempts/crcns-bf-1-nair-2018-01.yaml
   712 claims/crcns-bf-1/10.1073-pnas.1712431115.yaml
     8 transcripts/crcns-bf-1/answer-report.md
    16 transcripts/crcns-bf-1/author-answers-report.md
    56 transcripts/crcns-bf-1/author-report.md
    28 transcripts/crcns-bf-1/author-revise-1-report.md
    22 transcripts/crcns-bf-1/author-revise-2-report.md
    20 transcripts/crcns-bf-1/claims-check-report.md
    37 transcripts/crcns-bf-1/claims-report.md
    45 transcripts/crcns-bf-1/verifier-1-report.md
    64 transcripts/crcns-bf-1/verifier-2-report.md
  1760 total
crcns-ac-2-deweese-2004-01.md
crcns-hc-16-talbot-2018-01.md
crcns-hc-9-quattrocolo-2013-01.md
crcns-ia-1-eyherabide-2008-01.md
crcns-ofc-4-schuck-2016-01.md
crcns-pfc-6-peyrache-2009-01.md
crcns-ret-1-lefebvre-2008-01.md
```

**Agent calls Bash**

```bash
grep -n -i 'bf' targets/dandisets.json | head; grep -n -i 'crcns' targets/dandisets.json | head -5; head -c 800 targets/dandisets.json; ls targets; grep -n 'Reproduced\|Partial' README.md | head -5; cat docs/pilot-notes/crcns-hc-16-talbot-2018-01.md | head -30
```

```
{
 "schema_version": 1,
 "generated": "2026-11-05T14:39:45+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 672,
  "with_a_paper": 295,
  "with_a_published_version": 254,
  "papers": 312,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 2448.74,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n 'crcns-hc-16' README.md | head -2; grep -n -m3 '^| Data' README.md; cd transcripts/crcns-bf-1; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "== $f"; cat $f; done
```

```
<persisted-output>
Output too large (30KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2462a374-1280-4bdb-85de-ec08ba5b1f32/tool-results/b17q55itv.txt

Preview (first 2KB):
== author-report.md
The entry for CRCNS bf-1 is written, locked and run, and the attempt record and verifier handover are in place. Of the 28 claims, 10 were tested and 18 are blocked; `entry.py check` and `all` pass with 0 errors, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig3a-bf-gamma-reduction | partially reproduced: gamma falls 48% in the arena (paper 35 ± 3), paired t p = 0.012 over 6 rats; every reading gives 46.8–48.1% |
| fig3a-each-hemisphere-significant | reproduced: all 12 arena recordings p < 1e-7 |
| fig3b-arena-gamma-unrelated-to-movement | reproduced: one-way p = 1.0 |
| fig3b-home-cage-gamma-increases-with-movement | not reproduced: the claims file's test gives p = 0.82. Gamma does rise in all 6 rats; a repeated-measures ANOVA gives p = 2e-5 |
| fig3b-matched-movement | not reproduced: one-way p = 0.070; a paired test of the same values gives p = 0.007 |
| fig3c-home-cage-above-both-sessions | not reproduced: arena session 2 is 15.9% *below* session 1 (paper +5.62%), p = 0.020. Rests on an assumption (below) |
| fig3d-gamma-rises-with-time-in-arena | partially reproduced: r = 0.86 in 1-min bins (paper 0.72); 0.13 and 0.045 under the other readings |
| figs2-bf-low-frequency-bands | reproduced under all 12 readings |
| figs3-unimodal-states | reproduced: smallest dip-test p = 0.102 |
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2462a374-1280-4bdb-85de-ec08ba5b1f32/tool-results/b17q55itv.txt"
}
```

```
1	== author-report.md
2	The entry for CRCNS bf-1 is written, locked and run, and the attempt record and verifier handover are in place. Of the 28 claims, 10 were tested and 18 are blocked; `entry.py check` and `all` pass with 0 errors, and nothing was committed.
3	
4	## 1. Outcomes
5	
6	| Claim | Outcome |
7	|---|---|
8	| fig3a-bf-gamma-reduction | partially reproduced: gamma falls 48% in the arena (paper 35 ± 3), paired t p = 0.012 over 6 rats; every reading gives 46.8–48.1% |
9	| fig3a-each-hemisphere-significant | reproduced: all 12 arena recordings p < 1e-7 |
10	| fig3b-arena-gamma-unrelated-to-movement | reproduced: one-way p = 1.0 |
11	| fig3b-home-cage-gamma-increases-with-movement | not reproduced: the claims file's test gives p = 0.82. Gamma does rise in all 6 rats; a repeated-measures ANOVA gives p = 2e-5 |
12	| fig3b-matched-movement | not reproduced: one-way p = 0.070; a paired test of the same values gives p = 0.007 |
13	| fig3c-home-cage-above-both-sessions | not reproduced: arena session 2 is 15.9% *below* session 1 (paper +5.62%), p = 0.020. Rests on an assumption (below) |
14	| fig3d-gamma-rises-with-time-in-arena | partially reproduced: r = 0.86 in 1-min bins (paper 0.72); 0.13 and 0.045 under the other readings |
15	| figs2-bf-low-frequency-bands | reproduced under all 12 readings |
16	| figs3-unimodal-states | reproduced: smallest dip-test p = 0.102 |
17	| figs5-arena-excursions | partially reproduced: the gamma and theta tests hold, but there are 10–14 excursions per 20 min averaging 5 s, against the paper's 8 lasting 8–44 s |
18	| bipolar-gamma-reduction, fig3c-consistent-over-days | blocked, metadata_insufficient |
19	| fig3d-rapid-switch-to-home-cage, plus 15 behaviour, object, unit, ACC and VC claims | blocked, data_missing |
20	
[... 227 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-bf-1-nair-2018-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-bf-1-nair-2018-01
3	dataset:
4	  archive: crcns
5	  id: bf-1
6	  version: unversioned
7	  doi: 10.6080/K0MK6B2Q
8	paper: doi:10.1073/pnas.1712431115
9	date: '2026-11-06'
10	entry: crcns-bf-1-nair-2018
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 733 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-bf-1/10.1073-pnas.1712431115.yaml",
 "limit": 90
}
```

```
1	# Claims for Nair, Klaassen, Arato, Vyssotski, Harvey & Rainer (2018), PNAS 115:1352-1357, on
2	# CRCNS data set bf-1.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
4	# protocol as stated in docs/protocol.md (Reader, version pilot-13).
5	#
6	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
7	# with its Results, figure legends and short Materials and Methods, and the supplement
8	# (pnas.201712431si.pdf: SI results on low-frequency power, unimodality, excursions and
9	# locomotion, SI Materials and Methods, and the legends of Figs. S1 to S7). The Methods that
10	# fix the analyses are in the SI Materials and Methods. The paper links no analysis code, so none
11	# was read; it names the toolboxes used (Wave_clus, CircStat, Chronux, BSMART, MVGC, SPSS). No PDF
12	# renderer was available, so figures were read from their legends and the Results only. The
13	# extracted text prints one p-value as "P < 0.0" (ACC gamma, Results, Gamma Oscillations in BF
14	# Cortical Projection Targets); it is recorded as printed.
15	#
16	# Data the paper used. Adult male Long Evans rats, 80 to 120 days old. 16 rats implanted with
17	# tungsten microelectrodes in the BF (AP -0.8, ML 2.8, DV -8.2 mm from bregma), 14 of them also in
18	# the VC and 8 in the ACC; 22 BF hemispheres in the group analyses; 4 more rats with bipolar BF
19	# electrodes. LFPs were recorded with a head-mounted Neurologger 2A (four LFP channels at 1.6 kHz,
20	# and a 3D accelerometer for movement), and in tethered recordings (TDT RZ5) LFP at 1.6 kHz with
[... 70 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "title|Gamma Band|gamma oscillations",
 "path": "claims/crcns-bf-1/10.1073-pnas.1712431115.yaml",
 "-i": true,
 "output_mode": "content",
 "head_limit": 10
}
```

```
13:# extracted text prints one p-value as "P < 0.0" (ACC gamma, Results, Gamma Oscillations in BF
28:# The CRCNS data set, by its title and data description, holds BF LFP from six rats at 400 Hz,
415:    80 Hz) gamma oscillations.
418:    significant phase locking to broadband (30–80 Hz) gamma oscillations
473:  source: Results, Gamma Oscillations in BF Cortical Projection Targets, paragraph 1; Figure 6A
485:  source: Results, Gamma Oscillations in BF Cortical Projection Targets, paragraph 1; Figure 6A
509:  source: Results, Gamma Oscillations in BF Cortical Projection Targets, paragraph 1; Figure 6B
533:  source: Results, Gamma Oscillations in BF Cortical Projection Targets, paragraph 2; Figure 6C
565:  source: Results, Gamma Oscillations in BF Cortical Projection Targets, paragraph 2; Figure 6D
599:    significant difference is in the high gamma band (above 60 Hz)
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-bf-1-nair-2018-01.md",
 "content": "# crcns-bf-1, Nair et al. 2018\n\nFour claims reproduced, four partially (one on an assumption), two not\nreproduced and eighteen blocked, sixteen for missing data and two for\ninsufficient metadata. The first verification round agreed with 27 of the\n28 outcomes as they stood and the second with all 28; nothing was proposed\nafter the second, so there was no third round. CRCNS does not version data\nsets, so the version is recorded as unversioned with the data set's DOI\n(10.6080/K0MK6B2Q) and the archive's MD5 from `checksums.md5`, which the\nnotebook checks while streaming it. The paper, Nair, Klaassen, Arato,\nVyssotski, Harvey and Rainer in PNAS, records basal forebrain (BF) LFP in rats\nin the home cage and while they explore a novel arena, finds BF gamma power\n(30 to 80 Hz) lower in the arena, rising with movement in the home cage but\nnot in the arena, and relates BF activity to single units and to the\nanterior cingulate (ACC) and visual cortex (VC); the data set holds the BF\nLFP of six rats at 400 Hz in 2-s segments, with a movement value per segment\nand two home-cage and two arena sessions per rat. The claims were written\nfrom the PyMuPDF text of the version of record and its supplement, without\nrendering any figure; the paper links no code. The gamma, movement quartile,\nlow-frequency band, unimodality and excursion claims could be tested; the\nbehaviour, object, single-unit, ACC and VC claims, the bipolar recordings,\nthe consistency over days and the switch back to the home cage could not.\nReproduced are `fig3a-each-hemisphere-significant` (all 12 arena recordings\nbelow the home cage, largest p = 2.7e-30 with 2-s epochs),\n`fig3b-arena-gamma-unrelated-to-movement` (one-way p = 1.0),\n`figs2-bf-low-frequency-bands` (under all 12 readings) and\n`figs3-unimodal-states` (smallest dip-test p = 0.102). Partial are\n`fig3a-bf-gamma-reduction` (p = 0.012 over 6 rats, but a reduction of 46.8%\nto 48.1% against 35 +/- 3%), `fig3c-home-cage-above-both-sessions` (the home\ncage above both arena sessions by Bonferroni-corrected paired t, p = 0.038\nand 0.035, not by Tukey's HSD, p = 0.30 and 0.19, the session-order part not\njudged), `fig3d-gamma-rises-with-time-in-arena` (r = 0.859 in 1-min bins\nagainst 0.72; 30-s bins give 0.744 and 0.747, within tolerance) and\n`figs5-arena-excursions` (the gamma and theta tests hold, but 10.7 to 14.5\nexcursions per 20 min of 5.1 to 5.6 s on average against 8 of 16 +/- 8 s).\nNot reproduced are `fig3b-home-cage-gamma-increases-with-movement` (one-way\nANOVA on per-rat quartile means p = 0.82, though gamma rises in 6 of 6 rats\nand a repeated-measures ANOVA gives p = 2.0e-05) and `fig3b-matched-movement`\n(p = 0.070, a paired t test of the same values p = 0.0071); both rest on the\nclaims file's test, which puts the between-rat spread into the error term.\nThe author's first run had 4 reproduced, 3 partially, 3 not reproduced and 18\nblocked, with fig3c not reproduced on the assumption that sessions 1 and 2\nare a day's first and second arena trials. The author asked no questions of a\nreader, so the answer and author-answers runs changed nothing. Round 1\ndisagreed on fig3c (partially reproduced, the session-order part blocked as\nmetadata insufficient, as the descriptor calls the sessions \"two separate\nexamples\") and found that the criterion's one-way ANOVA cannot detect a\nwithin-rat effect with six rats, that time in the arena assumed each file\nstarts at arena entry, that Tukey's test ignores the pairing within rat, that\nthe boxcar zero-padded file ends and that dip tests were run on raw power\nonly; in reply fig3c was changed, fig3d was marked assumed for its 1-min bins\nwith a window anchored at the file end and a sweep of bin widths, the boxcar\nwas fixed, log10 dip tests were added (one per-session p = 0.035) and whether\nthe per-rat one-way ANOVA is the paper's test went to a reader in\n`questions/crcns-bf-1.yaml`, a file written after the answer run, so the\nquestion is unanswered. Round 2 agreed with all 28 outcomes and found text the\noutputs did not support, among them a summary that read as 17 data_missing\nclaims for 16, a run time in the README with no printed support and 20-s\nbins with the end anchor (r = 0.662) left out as within tolerance; in reply\nthe text was corrected. The author briefly opened another attempt's\n`entry.yaml` (crcns-hc-9) to check an id format, against the instruction not\nto read other attempts. The notebook ran in about 14 s at first and 19 s, 19 s\nand 20 s after the later runs; a string-formatting error during development\nwas the only failure.\n\nThe data set holds only the BF LFP of six rats in home cage and arena: the\nACC and VC recordings, single units, object sessions, video and behaviour\nscoring of the paper are not in it, and the paper names no other deposit, so\n16 of the 28 claims need data that are not in it. Rat_3_Type_HCage_Session_2.mat\nis not a separate recording: 287 of its 291 segments are segments of\nRat_3_Type_HCage_Session_1.mat with the same LFP and movement values, 100 s\nlater on that file's clock, and it was counted once. The sessions carry no\nday and no time of recording, and each file has its own clock starting at 0,\nso the paper's day factor, the order of home-cage and arena sessions and the\ntransfer between them cannot be reconstructed; the descriptor does not say\nwhether sessions 1 and 2 are a day's two arena trials, which matters, as\nsession 2 has 15.9% lower gamma than session 1 where the paper reports 5.62%\nhigher in the second trial. Which electrodes were bipolar is not stated.\nArtifact segments were removed without a stated rule, 2.6% to 23.5% of each\nfile's span against the 1-4% the SI reports, and the SI's rule applied to the\ndelivered segments removes a further 16.8%. The LFP has no stated unit, and\nthe movement value is dimensionless, with a scale in rats 4 and 5 about a\nquarter of that in the other rats, which is not explained. In 13 of 24 files\nthe movement value correlates best with the 100-200 Hz LFP power of the next\nsegment, so the movement stream may lead the LFP by up to one 2-s segment,\nand rat 2's home-cage session 1 has a line at 50 Hz, 26 times its neighbours,\ninside the gamma band. The descriptor names the home-cage condition 'Hcage'\nwhere the files use 'HCage', and describes basal_forebrain_lfp.tar.gz as a\nfile of .mat files without saying it is a gzipped tar. Questions are put to\nthe paper's authors: what the observations of the Fig. 3B one-way ANOVAs were\nand whether gamma was normalized per animal; how the 35% reduction was\ncomputed; what power scale, histogram bins and minimum length define the\nexcursions; and what was correlated with time in Fig. 3D, at what bin width\nand from which anchor.\n\nThe author's points on the protocol: the guidance on CRCNS data assumes zip\nfiles while bf-1 is a `.tar.gz`, so it was streamed with fsspec and\n`tarfile` and its MD5 checked during the stream; the clock check names no\nmethod for data without a trial table, so 100-200 Hz LFP power was compared\nwith the movement values at shifts of -5 to +5 segments; there is no rule for\na criterion that names no partial outcome when the effect holds and its size\ndoes not, as for fig3d, so partially reproduced was used from the general\ndefinition; several criteria fix a one-way ANOVA on per-rat means that large\nbetween-rat differences make insensitive, and the criterion was followed with\nthe repeated-measures and paired variants shown; and a duplicated recording\nbreaks session pairing, so the affected pair was dropped (11 pairs) and the\n12-pair version shown as a variant.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-bf-1-nair-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && git status --short && grep -c -- '—\|rather' docs/pilot-notes/crcns-bf-1-nair-2018-01.md
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
?? docs/pilot-notes/crcns-bf-1-nair-2018-01.md
?? scripts
0
```

**Agent**

I wrote `docs/pilot-notes/crcns-bf-1-nair-2018-01.md` and changed no other file. The untracked dotfiles, `.idea` and `scripts` in the repository root were already there, and I left them alone. Two things to know:

- `targets/dandisets.json` has no entry for CRCNS:bf-1, so there was no `catalystneuro` field to check. The note does not open with the CatalystNeuro sentence.
- The sources don't give the paper's title, so the note names only the authors and the journal.

# crcns-bf-1, Nair et al. 2018

Four claims reproduced, four partially (one on an assumption), two not
reproduced and eighteen blocked, sixteen for missing data and two for
insufficient metadata. The first verification round agreed with 27 of the
28 outcomes as they stood and the second with all 28; nothing was proposed
after the second, so there was no third round. CRCNS does not version data
sets, so the version is recorded as unversioned with the data set's DOI
(10.6080/K0MK6B2Q) and the archive's MD5 from `checksums.md5`, which the
notebook checks while streaming it. The paper, Nair, Klaassen, Arato,
Vyssotski, Harvey and Rainer in PNAS, records basal forebrain (BF) LFP in rats
in the home cage and while they explore a novel arena, finds BF gamma power
(30 to 80 Hz) lower in the arena, rising with movement in the home cage but
not in the arena, and relates BF activity to single units and to the
anterior cingulate (ACC) and visual cortex (VC); the data set holds the BF
LFP of six rats at 400 Hz in 2-s segments, with a movement value per segment
and two home-cage and two arena sessions per rat. The claims were written
from the PyMuPDF text of the version of record and its supplement, without
rendering any figure; the paper links no code. The gamma, movement quartile,
low-frequency band, unimodality and excursion claims could be tested; the
behaviour, object, single-unit, ACC and VC claims, the bipolar recordings,
the consistency over days and the switch back to the home cage could not.
Reproduced are `fig3a-each-hemisphere-significant` (all 12 arena recordings
below the home cage, largest p = 2.7e-30 with 2-s epochs),
`fig3b-arena-gamma-unrelated-to-movement` (one-way p = 1.0),
`figs2-bf-low-frequency-bands` (under all 12 readings) and
`figs3-unimodal-states` (smallest dip-test p = 0.102). Partial are
`fig3a-bf-gamma-reduction` (p = 0.012 over 6 rats, but a reduction of 46.8%
to 48.1% against 35 +/- 3%), `fig3c-home-cage-above-both-sessions` (the home
cage above both arena sessions by Bonferroni-corrected paired t, p = 0.038
and 0.035, not by Tukey's HSD, p = 0.30 and 0.19, the session-order part not
judged), `fig3d-gamma-rises-with-time-in-arena` (r = 0.859 in 1-min bins
against 0.72; 30-s bins give 0.744 and 0.747, within tolerance) and
`figs5-arena-excursions` (the gamma and theta tests hold, but 10.7 to 14.5
excursions per 20 min of 5.1 to 5.6 s on average against 8 of 16 +/- 8 s).
Not reproduced are `fig3b-home-cage-gamma-increases-with-movement` (one-way
ANOVA on per-rat quartile means p = 0.82, though gamma rises in 6 of 6 rats
and a repeated-measures ANOVA gives p = 2.0e-05) and `fig3b-matched-movement`
(p = 0.070, a paired t test of the same values p = 0.0071); both rest on the
claims file's test, which puts the between-rat spread into the error term.
The author's first run had 4 reproduced, 3 partially, 3 not reproduced and 18
blocked, with fig3c not reproduced on the assumption that sessions 1 and 2
are a day's first and second arena trials. The author asked no questions of a
reader, so the answer and author-answers runs changed nothing. Round 1
disagreed on fig3c (partially reproduced, the session-order part blocked as
metadata insufficient, as the descriptor calls the sessions "two separate
examples") and found that the criterion's one-way ANOVA cannot detect a
within-rat effect with six rats, that time in the arena assumed each file
starts at arena entry, that Tukey's test ignores the pairing within rat, that
the boxcar zero-padded file ends and that dip tests were run on raw power
only; in reply fig3c was changed, fig3d was marked assumed for its 1-min bins
with a window anchored at the file end and a sweep of bin widths, the boxcar
was fixed, log10 dip tests were added (one per-session p = 0.035) and whether
the per-rat one-way ANOVA is the paper's test went to a reader in
`questions/crcns-bf-1.yaml`, a file written after the answer run, so the
question is unanswered. Round 2 agreed with all 28 outcomes and found text the
outputs did not support, among them a summary that read as 17 data_missing
claims for 16, a run time in the README with no printed support and 20-s
bins with the end anchor (r = 0.662) left out as within tolerance; in reply
the text was corrected. The author briefly opened another attempt's
`entry.yaml` (crcns-hc-9) to check an id format, against the instruction not
to read other attempts. The notebook ran in about 14 s at first and 19 s, 19 s
and 20 s after the later runs; a string-formatting error during development
was the only failure.

The data set holds only the BF LFP of six rats in home cage and arena: the
ACC and VC recordings, single units, object sessions, video and behaviour
scoring of the paper are not in it, and the paper names no other deposit, so
16 of the 28 claims need data that are not in it. Rat_3_Type_HCage_Session_2.mat
is not a separate recording: 287 of its 291 segments are segments of
Rat_3_Type_HCage_Session_1.mat with the same LFP and movement values, 100 s
later on that file's clock, and it was counted once. The sessions carry no
day and no time of recording, and each file has its own clock starting at 0,
so the paper's day factor, the order of home-cage and arena sessions and the
transfer between them cannot be reconstructed; the descriptor does not say
whether sessions 1 and 2 are a day's two arena trials, which matters, as
session 2 has 15.9% lower gamma than session 1 where the paper reports 5.62%
higher in the second trial. Which electrodes were bipolar is not stated.
Artifact segments were removed without a stated rule, 2.6% to 23.5% of each
file's span against the 1-4% the SI reports, and the SI's rule applied to the
delivered segments removes a further 16.8%. The LFP has no stated unit, and
the movement value is dimensionless, with a scale in rats 4 and 5 about a
quarter of that in the other rats, which is not explained. In 13 of 24 files
the movement value correlates best with the 100-200 Hz LFP power of the next
segment, so the movement stream may lead the LFP by up to one 2-s segment,
and rat 2's home-cage session 1 has a line at 50 Hz, 26 times its neighbours,
inside the gamma band. The descriptor names the home-cage condition 'Hcage'
where the files use 'HCage', and describes basal_forebrain_lfp.tar.gz as a
file of .mat files without saying it is a gzipped tar. Questions are put to
the paper's authors: what the observations of the Fig. 3B one-way ANOVAs were
and whether gamma was normalized per animal; how the 35% reduction was
computed; what power scale, histogram bins and minimum length define the
excursions; and what was correlated with time in Fig. 3D, at what bin width
and from which anchor.

The author's points on the protocol: the guidance on CRCNS data assumes zip
files while bf-1 is a `.tar.gz`, so it was streamed with fsspec and
`tarfile` and its MD5 checked during the stream; the clock check names no
method for data without a trial table, so 100-200 Hz LFP power was compared
with the movement values at shifts of -5 to +5 segments; there is no rule for
a criterion that names no partial outcome when the effect holds and its size
does not, as for fig3d, so partially reproduced was used from the general
definition; several criteria fix a one-way ANOVA on per-rat means that large
between-rat differences make insensitive, and the criterion was followed with
the repeated-measures and paired variants shown; and a duplicated recording
breaks session pairing, so the affected pair was dropped (11 pairs) and the
12-pair version shown as a variant.

## End of run

13 turns, 1 minutes, $0.94 at API prices, result: success.
