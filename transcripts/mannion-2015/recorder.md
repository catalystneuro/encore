# crcns-vim-3 · recorder · run 42475650680

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/crcns-vim-3/ transcripts/crcns-vim-3/; python tools/readme_row.py crcns-vim-3; cat attempts/crcns-vim-3-mannion-2015-01.yaml
```

```
docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md
docs/pilot-notes/crcns-hc-14-girardeau-2017-01.md
docs/pilot-notes/002034-thompson-2026-01.md
docs/pilot-notes/002035-weible-2022-01.md
docs/pilot-notes/002020-nakamuta-2025-01.md
claims/crcns-vim-3/:
10.7717-peerj.1038.yaml

transcripts/crcns-vim-3/:
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
[... 469 more lines not kept]
```

**Agent calls Bash**

```bash
for f in docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md docs/pilot-notes/crcns-hc-14-girardeau-2017-01.md docs/pilot-notes/002034-thompson-2026-01.md docs/pilot-notes/002035-weible-2022-01.md docs/pilot-notes/002020-nakamuta-2025-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; head -5 README.md; grep -n "| Dataset\|^| ---" README.md | head; grep -n -B2 -A12 '"vim-3"' targets/dandisets.json
```

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/96e2dc53-a610-4707-a4cc-02f7e2d41e46/tool-results/brxsjtcvl.txt

Preview (first 2KB):
=== docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md
# crcns-ssc-8, Goncalves et al. 2013

Five claims reproduced, three partially (all three on an assumption), three not
reproduced (one on an assumption) and 17 blocked, 16 for missing data and one
for insufficient metadata. The first verification round agreed with all 28
outcomes and the second with all 28; nothing was proposed after the second, so
there was no third round. CRCNS does not version data sets, so the version is
recorded as unversioned with the data set's DOI (10.6080/K0X63K3X). The paper,
Goncalves, Anstey, Golshani and Portera-Cailliau in Nature Neuroscience
(16:903-909), images layer 2/3 barrel cortex of unanesthetized wild-type (WT)
and Fmr1 -/- (KO) mice at P9-11, P14-16 and P30-40 with two-photon calcium
imaging at 3.9 Hz, and reports that pairwise correlation falls with age and
with distance, that it is higher in KO mice pooled over ages and most of all at
P14-16, that more KO neurons take part in peaks of synchrony, that firing rates
from the imaging do not differ, that in whole-cell recordings KO neurons fire
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/96e2dc53-a610-4707-a4cc-02f7e2d41e46/tool-results/brxsjtcvl.txt"
}
```

```
1	=== docs/pilot-notes/crcns-ssc-8-goncalves-2013-01.md
2	# crcns-ssc-8, Goncalves et al. 2013
3	
4	Five claims reproduced, three partially (all three on an assumption), three not
5	reproduced (one on an assumption) and 17 blocked, 16 for missing data and one
6	for insufficient metadata. The first verification round agreed with all 28
7	outcomes and the second with all 28; nothing was proposed after the second, so
8	there was no third round. CRCNS does not version data sets, so the version is
9	recorded as unversioned with the data set's DOI (10.6080/K0X63K3X). The paper,
10	Goncalves, Anstey, Golshani and Portera-Cailliau in Nature Neuroscience
11	(16:903-909), images layer 2/3 barrel cortex of unanesthetized wild-type (WT)
12	and Fmr1 -/- (KO) mice at P9-11, P14-16 and P30-40 with two-photon calcium
13	imaging at 3.9 Hz, and reports that pairwise correlation falls with age and
14	with distance, that it is higher in KO mice pooled over ages and most of all at
15	P14-16, that more KO neurons take part in peaks of synchrony, that firing rates
16	from the imaging do not differ, that in whole-cell recordings KO neurons fire
17	more in Up states, that firing rises with EEG low/high power in KO mice, and
18	that isoflurane raises correlation in WT but not KO mice; the data set holds
19	the raw TIFF movies of the unanesthetized mice, one per mouse, the estimated
20	firing rates of each neuron and the cell-to-cell distances. The claims were
[... 600 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A15 'vim-3' targets/dandisets.json | head -60; grep -n "Dataset |\|Reproduced" README.md | head -3; wc -w transcripts/crcns-vim-3/*-report.md
```

```
70 transcripts/crcns-vim-3/answer-report.md
  214 transcripts/crcns-vim-3/author-answers-report.md
  825 transcripts/crcns-vim-3/author-report.md
  515 transcripts/crcns-vim-3/author-revise-1-report.md
  399 transcripts/crcns-vim-3/author-revise-2-report.md
  328 transcripts/crcns-vim-3/claims-check-report.md
  640 transcripts/crcns-vim-3/claims-report.md
 1014 transcripts/crcns-vim-3/verifier-1-report.md
  744 transcripts/crcns-vim-3/verifier-2-report.md
 4749 total
```

**Agent calls Bash**

```bash
grep -n -i 'vim' targets/dandisets.json | head; grep -n -i 'crcns' targets/dandisets.json | head -5; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'));print(type(d), (list(d)[:3] if isinstance(d,dict) else d[0]))
E
sed -n 1,40p tools/readme_row.py
```

```
<class 'dict'> ['schema_version', 'generated', 'source']
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
[... 21 more lines not kept]
```

**Agent**

The dataset has no entry in `targets/dandisets.json` (a CRCNS set), so there is no `catalystneuro` field to report. Reading the claims file and reports next.

**Agent calls Bash**

```bash
cd transcripts/crcns-vim-3; cat author-report.md author-revise-1-report.md author-revise-2-report.md answer-report.md author-answers-report.md
```

```
I've finished steps 1 to 6 of the Author section. One claim was tested and reproduced. The other 15 are blocked because the data set does not hold the V1 to V3 definitions that every response measure in the paper uses. `python tools/entry.py all` reports 0 errors and the notebook passes in about 4 min. The handover is in `executed/crcns-vim-3-mannion-2015/handover/`. Nothing is committed.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| figs2-task-no-condition-difference | reproduced (no effect has p < 0.05 under either reading the criterion names, or under one extra variant) |
| localiser-masks-ventral-dorsal, presentation-source-interaction, interaction-not-area-dependent, lower-field-below-greater, upper-field-no-source-difference, fig4-top-five-matching-source, figs3-residual-no-condition-difference, figs3-residual-upper-larger | blocked, data_missing (no V1 to V3 definitions, surfaces or anatomy) |
| fig4-qualitative-content | blocked, data_missing (depends on fig4-top-five) |
| fig5a, fig5-no-other-pixel, fig5bc, fig5def, fig5-no-other-filter | blocked, data_missing (need the V1 to V3 responses, and the monitor calibration for the DKL colour conversion is not public) |
| no-radial-bias-in-patches | blocked, data_missing (needs the monitor calibration; also depends on fig5bc in the claims file) |

**(2) Data set, assumptions, questions**
- **Pinned file:** the data set is one 2.35 GB `crcns_vim-3.tar.gz`. I recorded the version as `unversioned`, since CRCNS does not version data sets. The notebook streams the whole file once and checks its md5 against `checksums.md5`; they match. A tar.gz has no index, so it cannot be opened in place like a zip; it is streamed member by member, nothing goes to disk, and the reader reconnects if S3 drops the connection.
- **Contents:** all 7 participants have 10 runs, 10 event sequences and 10 task files each, plus 120 stimulus screenshots. No file is duplicated, and the counts match the Methods.
- **Recorded findings:**
  - T
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import yaml;d=yaml.safe_load(open('claims/crcns-vim-3/10.7717-peerj.1038.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
for c in d['claims']: print(c['id'],'|',c.get('data'),'|',c.get('figure') or c.get('location'),'|',c.get('statement','')[:300].replace('\n',' '),'\n')
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'claims/crcns-vim-3/10.7717-peerj.1038.yaml'
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml;d=yaml.safe_load(open('claims/crcns-vim-3/10.7717-peerj.1038.yaml'))
print({k:(v if not isinstance(v,(list,dict)) else '...') for k,v in d.items()})
for c in d['claims']: print(c['id'],'|',c.get('data'),'|',c.get('inputs') and 'INPUTS','|',c.get('source') or c.get('figure') or c.get('location'),'|',str(c.get('statement',''))[:250].replace('\n',' '),'\n')
E
head -c 2500 transcripts/crcns-vim-3/claims-report.md; echo; head -c 2500 transcripts/crcns-vim-3/claims-check-report.md
```

```
{'schema_version': 2, 'dataset': '...', 'paper': 'doi:10.7717/peerj.1038', 'claims': '...', 'checks': '...'}
localiser-masks-ventral-dorsal | dataset | None | Materials & Methods, Localiser, paragraph 1; Figure 2B | The localiser masks for upper visual field presentation lie largely in ventral subregions of V1 to V3 and those for lower visual field presentation in dorsal subregions. 

presentation-source-interaction | dataset | None | Results and Discussion, paragraph 1; Figure 3 | Response amplitude shows a significant interaction between presentation location (upper, lower visual field) and source location (above, below fixation), F(1,6) = 11.19, p = 0.016. 

interaction-not-area-dependent | dataset | None | Results and Discussion, paragraph 1 | The presentation by source interaction does not depend on visual area (three-way interaction F(1.9,11.4) = 1.52, p = 0.260), which justifies combining V1, V2 and V3. 

lower-field-below-greater | dataset | None | Results and Discussion, paragraph 1 | For presentation in the lower visual field, combined over V1 to V3, patches sourced from below fixation evoke larger responses than patches from above (0.80 against 0.72 psc), a significant difference (t(6) = 5.17, p = 0.002). 

upper-field-no-source-difference | dataset | None | Results and Discussion, paragraphs 1 and 2 | For presentation in the upper visual field, patches sourced from below and above fixation evoke comparable responses (0.84 against 0.85 psc; t(6) = 0.38, p = 0.719), so the predicted preference for above-sourced patches in the upper field was not fou 

fig4-top-five-matching-source | dataset | None | Results and Discussion, paragraph 3; Figure 4 | Ranking the 60 image patch pairs by the difference between upper and lower field responses, four of the five most upper-preferred pairs are sourced from above fixation and four of the five most lower-preferred pairs from below fixation. 

fig4-qualitative-content | with_inputs | None | Results and Discussion, para
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/crcns-vim-3/10.7717-peerj.1038.yaml; tail -c +2500 transcripts/crcns-vim-3/claims-report.md; head -c 3000 transcripts/crcns-vim-3/verifier-1-report.md; echo; head -c 2000 transcripts/crcns-vim-3/verifier-2-report.md
```

```
# Claims for Mannion (2015), PeerJ 3:e1038, "Sensitivity to the visual field origin of natural image
# patches in human low-level visual cortex", doi:10.7717/peerj.1038, on CRCNS data set vim-3
# (doi:10.6080/K0JS9NC2).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, PMC4485252, from the Europe PMC full-text XML as supplied under
# paper/: Abstract, Introduction, Materials & Methods, Results and Discussion, Conclusion, the legends
# of Figures 1 to 5 and the legends of Figures S2 and S3. No PDF was supplied, so values printed only
# inside figures (the psc differences of Figure 4, the points of Figure 5) were not read. The
# supplementary files themselves (Fig. S1 stimulus set, Table S1 complete ANOVA output, the Fig. S2 and
# S3 images) are not under paper/; only their titles and legends are. Table S1 holds the main effects
# and the other interactions of the three-way ANOVA; the paper's text states the two effects the
# results rest on, so no claim needs Table S1.
#
# Code. The paper links https://bitbucket.org/djmannion/ul_sens_fmri_analysis, which no longer
# exists. The same repository is on GitHub as mannion-lab/ul_sens_fmri_analysis (also archived by
# Software Heritage from the Bitbucket origin). Read at commit
# 571e9312c251ff2166be91a57201112036e5e80d (2015-05-22). It holds the single-subject pipeline
# (preproc_template.py, loc_glm.py localiser GLM, glm_prep.py masks and ROI timecourses, glm.py
[... 72 more lines not kept]
```

**Agent**

Now writing the two files.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-vim-3-mannion-2015-01.md",
 "content": "# crcns-vim-3, Mannion et al. 2015\n\nOne claim reproduced, none partially, none not reproduced and eight blocked,\nall eight for missing data; the seven claims that also need outside data,\ncounted apart, are blocked too, six for missing data and\n`no-radial-bias-in-patches` for insufficient metadata. The first verification\nround agreed with 15 of the 16 outcomes as they stood and disagreed on the\nreason for blocking `no-radial-bias-in-patches`, and the second agreed with all\n16; nothing was proposed after the second, so there was no third round. CRCNS\ndoes not version data sets, so the version is recorded as unversioned with the\ndata set's DOI (10.6080/K0JS9NC2). The paper, Mannion in PeerJ (3:e1038),\nmeasures fMRI responses in V1, V2 and V3 of seven participants to natural image\npatches taken from above or below fixation and shown in the upper or lower\nvisual field, and reports an interaction between presentation and source\nlocation (F(1,6) = 11.19, p = 0.016) that does not depend on the area, larger\nlower-field responses to patches from below than from above (0.80 against 0.72\npsc) and no difference in the upper field, that the most upper-preferred patch\npairs are mostly from above and the most lower-preferred mostly from below\n(Figure 4), that the upper minus lower response difference rises with mean\nluminance and with the output of some luminance Gabor filters (Figure 5), that\nthe patches show no radial bias, and that task performance (Figure S2) and GLM\nresiduals (Figure S3) do not differ across conditions; the data set holds the\nraw functional runs of a 35-slice occipital slab, the event sequences, the task\nrecords and 120 stimulus screenshots. The claims were written from the version\nof record (PMC4485252) as text from the Europe PMC XML, without a PDF and\nwithout the supplementary files, and from the paper's analysis code at commit\n571e931 on GitHub, as its Bitbucket link is dead; the claims check made four\ncorrections, among them marking the \"largely confined\" rule for the localiser\nmasks as an assumption and naming the two possible filter scales (about 78.7\nand 78.2 pixels per degree), for 16 claims. Only `figs2-task-no-condition-difference`\ncould be tested, and it reproduced: in the window 0.4 to 0.9 s no effect\nreaches p < 0.05 under the code as written (smallest p 0.158) or with\nassignment by absolute run time (smallest p 0.347), nor under three variants\n(p >= 0.053), though under the code as written the window 0.6 to 0.9 s gives a\npresentation effect (p = 0.034). Every other claim needs responses in V1 to V3,\nor the monitor calibration, or both. A volume variant on all localiser voxels,\nwhich decides nothing, gives lower-field responses of 0.997 psc for patches\nfrom below and 0.870 from above (p = 0.034) and an interaction of p = 0.137.\nThe author asked no questions of a reader, so the answer and author-answers\nruns changed nothing. Round 1 agreed with every outcome but held that\n`no-radial-bias-in-patches` needs only the screenshots and a calibration and\nshould be blocked for insufficient metadata, with a luminance variant run under\na stated calibration, and raised targets dropped on event onsets, assignment to\nthe event in progress and the unprinted lines of `task.py`; in reply the\nreason was changed, the radial-bias test was run as `imstats.py` runs it under\nsRGB and Adobe RGB primaries (none of the 12 tests below p = 0.05, smallest p\n0.063), variants (d) and (e) were added and the `task.py` lines printed. The\nnotebook that round 1 reviewed still held a table of outcomes in its\nintroduction, which the verifier saw and quoted. Round 2 agreed with all 16 and\nfound sentences the outputs did not support, among them a filter match of\n1.3e-15 where 8.9e-16 is printed and labels called close to random without an\noutput to show it; in reply the text was corrected and the peak lag printed for\nevery reading, which showed a 0.7 s peak for lower/above under two readings.\nNo outcome changed in either round. The notebook ran in 158 to 243 s at first\nand 386 s after the author-answers run. In one development run S3 reset the\nconnection, so the reader now reconnects, and most of the helper module was\ndeleted by accident during editing and restored from an earlier draft.\n\nThe data set holds the raw functional runs, event sequences, task records and\nstimulus screenshots, but not the anatomical images, cortical surfaces,\nretinotopic mapping or V1, V2 and V3 definitions that every response measure of\nthe paper uses; its descriptor says so and asks users to request them on the\nCRCNS forum, and 14 of the 16 claims are blocked for this reason. The monitor's\nmeasured CIE coordinates, needed to put the screenshots in the DKL space of\nFigure 5 and the radial-bias test, are in neither the data set, the paper nor\nits code, and the patches are in colour (R, G and B differ in most pixels of\n118 of the 120 patches). The data set's README.txt says it contains fMRI\nmeasurements in areas V1, V2 and V3, but the files are whole volumes of the\noccipital slab with no area labels. The NIfTI files are named by scanner\nseries number and the sequence and task files by run, with no mapping given;\nthe paper's code takes the series in order as runs 1 to 10, which a\nleave-one-run-out fit supports for six participants and could not confirm for\np1011. For p1011 the timing of the event sequences and the run order could not\nbe confirmed without motion correction (held-out runs at mean t 0.7 and 1.1\nagainst 2.6 to 4.9 in the others, a coarse motion index of 3.6 mm by run 10\nagainst at most 1.8 mm), and its upper-field voxels lie above its lower-field\nones, the reverse of the other six. For p1004 runs 1 to 5 the target column of\nthe task lookup does not describe the task performed, which the paper's code\nredefines, and the descriptor does not say so or describe the four button keys.\nThe Figure S2 legend describes performance near each condition, while `task.py`\nlabels each target by the event starting about 32 s after it; with assignment\nby absolute time the conclusion of no difference is unchanged. No question is\nput to the paper's authors.\n\nThe author's points on the protocol: `docs/archives.md` assumes CRCNS data come\nas zips, while this one is a tar.gz with no index, so it was streamed once with\nan md5 check and reconnection; the derivation check rejects `Image.open(`,\nwhich blocks reading stimulus images that are part of the data, so they were\ndecoded with `pypng`; it is unclear whether a `depends_on` that is only\nmethodological should block a claim, and both reasons were recorded for the\nradial-bias claim; the protocol does not say whether a substitute analysis may\nbe shown for claims blocked for missing data, so the volume version went in a\nseparate section labelled as deciding nothing; and it is unclear whether the\n\"several readings\" rule or the \"absence is judged on the paper's test alone\"\nrule applies to a claim of absence with no test in the paper, which did not\nmatter here as every reading gave the same outcome.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-vim-3-mannion-2015-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/crcns-vim-3-mannion-2015-01.md",
 "content": "None of the paper's main findings could be tested in this data. These are the interaction between where a natural image patch is shown and where it was taken from, the larger lower-field responses to patches from below fixation, and the links between patch statistics such as mean luminance and the field preference. All rest on responses in V1, V2 and V3, and the dataset holds the raw functional runs without the anatomy or area definitions. The image statistics also need the monitor's colour calibration, which is not public. Of the minor claims, equal task performance across conditions held up, while the residual and radial-bias checks could not be decided.\n"
}
```

```
File created successfully at: summaries/crcns-vim-3-mannion-2015-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/crcns-vim-3-mannion-2015-01.md docs/pilot-notes/crcns-vim-3-mannion-2015-01.md; grep -n -i "—\|rather" summaries/crcns-vim-3-mannion-2015-01.md docs/pilot-notes/crcns-vim-3-mannion-2015-01.md; git status --short
```

```
110 summaries/crcns-vim-3-mannion-2015-01.md
1201 docs/pilot-notes/crcns-vim-3-mannion-2015-01.md
1311 total
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
?? docs/pilot-notes/crcns-vim-3-mannion-2015-01.md
?? scripts
?? summaries/crcns-vim-3-mannion-2015-01.md
```

**Agent**

I wrote both files and changed nothing else; nothing is committed. The summary is 110 words in five sentences. CRCNS:vim-3 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field and the second paragraph does not open with the conversion sentence. The untracked dotfiles and `scripts` in the repository root were there before this run, and I left them alone.

**docs/pilot-notes/crcns-vim-3-mannion-2015-01.md**

# crcns-vim-3, Mannion et al. 2015

One claim reproduced, none partially, none not reproduced and eight blocked, all eight for missing data; the seven claims that also need outside data, counted apart, are blocked too, six for missing data and `no-radial-bias-in-patches` for insufficient metadata. The first verification round agreed with 15 of the 16 outcomes as they stood and disagreed on the reason for blocking `no-radial-bias-in-patches`, and the second agreed with all 16; nothing was proposed after the second, so there was no third round. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K0JS9NC2). The paper, Mannion in PeerJ (3:e1038), measures fMRI responses in V1, V2 and V3 of seven participants to natural image patches taken from above or below fixation and shown in the upper or lower visual field, and reports an interaction between presentation and source location (F(1,6) = 11.19, p = 0.016) that does not depend on the area, larger lower-field responses to patches from below than from above (0.80 against 0.72 psc) and no difference in the upper field, that the most upper-preferred patch pairs are mostly from above and the most lower-preferred mostly from below (Figure 4), that the upper minus lower response difference rises with mean luminance and with the output of some luminance Gabor filters (Figure 5), that the patches show no radial bias, and that task performance (Figure S2) and GLM residuals (Figure S3) do not differ across conditions; the data set holds the raw functional runs of a 35-slice occipital slab, the event sequences, the task records and 120 stimulus screenshots. The claims were written from the version of record (PMC4485252) as text from the Europe PMC XML, without a PDF and without the supplementary files, and from the paper's analysis code at commit 571e931 on GitHub, as its Bitbucket link is dead; the claims check made four corrections, among them marking the "largely confined" rule for the localiser masks as an assumption and naming the two possible filter scales (about 78.7 and 78.2 pixels per degree), for 16 claims. Only `figs2-task-no-condition-difference` could be tested, and it reproduced: in the window 0.4 to 0.9 s no effect reaches p < 0.05 under the code as written (smallest p 0.158) or with assignment by absolute run time (smallest p 0.347), nor under three variants (p >= 0.053), though under the code as written the window 0.6 to 0.9 s gives a presentation effect (p = 0.034). Every other claim needs responses in V1 to V3, or the monitor calibration, or both. A volume variant on all localiser voxels, which decides nothing, gives lower-field responses of 0.997 psc for patches from below and 0.870 from above (p = 0.034) and an interaction of p = 0.137. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 agreed with every outcome but held that `no-radial-bias-in-patches` needs only the screenshots and a calibration and should be blocked for insufficient metadata, with a luminance variant run under a stated calibration, and raised targets dropped on event onsets, assignment to the event in progress and the unprinted lines of `task.py`; in reply the reason was changed, the radial-bias test was run as `imstats.py` runs it under sRGB and Adobe RGB primaries (none of the 12 tests below p = 0.05, smallest p 0.063), variants (d) and (e) were added and the `task.py` lines printed. The notebook that round 1 reviewed still held a table of outcomes in its introduction, which the verifier saw and quoted. Round 2 agreed with all 16 and found sentences the outputs did not support, among them a filter match of 1.3e-15 where 8.9e-16 is printed and labels called close to random without an output to show it; in reply the text was corrected and the peak lag printed for every reading, which showed a 0.7 s peak for lower/above under two readings. No outcome changed in either round. The notebook ran in 158 to 243 s at first and 386 s after the author-answers run. In one development run S3 reset the connection, so the reader now reconnects, and most of the helper module was deleted by accident during editing and restored from an earlier draft.

The data set holds the raw functional runs, event sequences, task records and stimulus screenshots, but not the anatomical images, cortical surfaces, retinotopic mapping or V1, V2 and V3 definitions that every response measure of the paper uses; its descriptor says so and asks users to request them on the CRCNS forum, and 14 of the 16 claims are blocked for this reason. The monitor's measured CIE coordinates, needed to put the screenshots in the DKL space of Figure 5 and the radial-bias test, are in neither the data set, the paper nor its code, and the patches are in colour (R, G and B differ in most pixels of 118 of the 120 patches). The data set's README.txt says it contains fMRI measurements in areas V1, V2 and V3, but the files are whole volumes of the occipital slab with no area labels. The NIfTI files are named by scanner series number and the sequence and task files by run, with no mapping given; the paper's code takes the series in order as runs 1 to 10, which a leave-one-run-out fit supports for six participants and could not confirm for p1011. For p1011 the timing of the event sequences and the run order could not be confirmed without motion correction (held-out runs at mean t 0.7 and 1.1 against 2.6 to 4.9 in the others, a coarse motion index of 3.6 mm by run 10 against at most 1.8 mm), and its upper-field voxels lie above its lower-field ones, the reverse of the other six. For p1004 runs 1 to 5 the target column of the task lookup does not describe the task performed, which the paper's code redefines, and the descriptor does not say so or describe the four button keys. The Figure S2 legend describes performance near each condition, while `task.py` labels each target by the event starting about 32 s after it; with assignment by absolute time the conclusion of no difference is unchanged. No question is put to the paper's authors.

The author's points on the protocol: `docs/archives.md` assumes CRCNS data come as zips, while this one is a tar.gz with no index, so it was streamed once with an md5 check and reconnection; the derivation check rejects `Image.open(`, which blocks reading stimulus images that are part of the data, so they were decoded with `pypng`; it is unclear whether a `depends_on` that is only methodological should block a claim, and both reasons were recorded for the radial-bias claim; the protocol does not say whether a substitute analysis may be shown for claims blocked for missing data, so the volume version went in a separate section labelled as deciding nothing; and it is unclear whether the "several readings" rule or the "absence is judged on the paper's test alone" rule applies to a claim of absence with no test in the paper, which did not matter here as every reading gave the same outcome.

**summaries/crcns-vim-3-mannion-2015-01.md**

None of the paper's main findings could be tested in this data. These are the interaction between where a natural image patch is shown and where it was taken from, the larger lower-field responses to patches from below fixation, and the links between patch statistics such as mean luminance and the field preference. All rest on responses in V1, V2 and V3, and the dataset holds the raw functional runs without the anatomy or area definitions. The image statistics also need the monitor's colour calibration, which is not public. Of the minor claims, equal task performance across conditions held up, while the residual and radial-bias checks could not be decided.

## End of run

13 turns, 1 minutes, $0.74 at API prices, result: success.
