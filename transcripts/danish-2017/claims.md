# danish-2017 · claims · run 42949549449

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ ; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; cat paper/aa-3.data-description.txt; wc paper/*.txt; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0169568.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0169568.txt",
 "offset": 222
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text with Methods and supplementary legends is present (version of record, PMC5472270). The paper links no code. Let me check the dataset listing and a recent claims file for conventions.

**Agent calls Bash**

```bash
cat papers/datasets/danish-2017.yaml 2>/dev/null; grep -n "danish" papers/keys.yaml; head -60 claims/drieu-2018.yaml; grep -rn "kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c; ls tools | head -30
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1371/journal.pone.0169568
title: Rhythmic syllable-related activity in a songbird motor thalamic nucleus necessary for learned vocalizations
datasets:
- archive: crcns
  id: aa-3
  relation: primary
272:  10.1371/journal.pone.0169568: danish-2017
# Claims for Drieu, Todorova & Zugaro (2018), Science 362, 675-679, tested on CRCNS hc-18.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (main text, figure legends of Figs. 1 to 3), and the
# author manuscript (HAL hal-02330673v1) for its Materials and Methods, the Fig. 4 legend and
# supplementary figures S1 to S13 with their legends. The extracted text of the version of
# record lacks its page 5 (Fig. 4 and the closing paragraphs), so the Fig. 4 legend is quoted
# from the author manuscript. Where the two versions print different bounds, the version of
# record is recorded: Fig. 1C peak rate P < 10^-3 (manuscript 10^-4); Fig. 1E V-test
# P < 10^-10 (manuscript 10^-11). The Methods' Data acquisition paragraph describes
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A6 "^schema_version" claims/drieu-2018.yaml; grep -n "data:" claims/drieu-2018.yaml | sort | uniq -c | head; grep -n "kind" claims/drieu-2018.yaml | head -3
```

```
100:schema_version: 2
101-paper: doi:10.1126/science.aat2952
102-claims:
103-- id: figs1-travel-similar
104-  statement: Train velocity, number of laps and travel duration did not differ between
105-    Passive 1, Active and Passive 2 (repeated-measures ANOVA, P > 0.05 for each, 5 rats).
106-  source: Results, paragraph 5; fig. S1B to S1D and legend
1181:  kind: agent
```

**Agent calls Bash**

```bash
grep -n "with_inputs\|with_labels\|elsewhere" docs/protocol.md | head -20
```

```
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
161:     recordings of its own, or on other data, are `data: elsewhere` when they
233:4. Decide what comes from outside the dataset. Data from elsewhere may be
242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
245:   - `with_labels` is for outside sources that only name or map codes the
267:   - `elsewhere` is for a claim whose data the dataset does not hold at
276:   - The notes of a `with_inputs` claim say which side a difference comes
287:     `data: elsewhere` instead (step 4).
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 230,
 "limit": 60
}
```

```
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference.
233	4. Decide what comes from outside the dataset. Data from elsewhere may be
234	   used only when the claims file says the paper relies on it, it is public,
235	   and it is pinned: a DOI, or a repository at a commit. Record each under
236	   `inputs` in the attempt. A claim whose outside input is not public is
237	   blocked with `data_missing`, and its notes say where you looked.
238	
239	   The registry judges the dataset, so claims that use outside data are
240	   kept apart:
241	   - Each claim says what its test uses: `data: dataset` (the default),
242	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243	     `with_inputs` and `elsewhere` claims are counted apart, each group on
244	     its own; the others count towards what is said about the dataset.
245	   - `with_labels` is for outside sources that only name or map codes the
246	     dataset already holds, such as stimulus names for its stimulus codes.
247	     They bring in no measurements. A link claim must confirm the names, and
248	     the missing names are recorded as a finding (`metadata_insufficient`).
249	   - When outside data has to be matched to the dataset's cells, sessions
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "'[a-z_]*'" tools/claims_check.py | grep -o "\"[a-z_]*\"\|'[a-z_]*'" | sort -u | tr '\n' ' '
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import pprint
c=s.get('\$defs',s.get('definitions',{}))
print(list(s['properties']))
for k,v in c.items(): print(k, list(v.get('properties',{})), v.get('required'))
"
```

```
['schema_version', 'dataset', 'paper', 'claims', 'checks']
expected ['quantity', 'value', 'tolerance', 'unit'] ['quantity', 'value']
statistic ['about', 'test', 'statistic', 'p', 'p_relation', 'corrected', 'ci', 'n'] None
```

**Agent**

Writing the claims file now: 24 claims covering the lesion results (Fig 2, S1 Fig) and the Uva recordings (Figs 3 to 9, S2 to S5 Figs).

**Agent calls Write**

```json
{
 "file_path": "claims/danish-2017.yaml",
 "content": "# Claims for Danish, Aronov & Fee (2017), PLoS ONE 12(6), e0169568, tested on CRCNS aa-3.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-11, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (PMC5472270, Europe PMC full-text XML, flattened), with its\n# main text, figure legends, Materials and methods, and the legends of the supporting\n# information (S1 Video, S1 Fig to S5 Fig). The supporting figures themselves were not needed;\n# no supplementary text beyond these legends exists. No PDF was supplied.\n#\n# Code: the paper links no code (\"All data analyses were performed with custom MATLAB\n# software\"). The spectral analyses use the Chronux package (ref 77), and the GTE times the\n# automated method of Boari et al. (ref 50); neither is linked to a version. The CRCNS\n# data description says the dataset holds MATLAB conversion and plotting scripts; they are\n# part of the dataset's files and were not read here.\n#\n# Data the paper used, as it reports them. Subjects are adult male zebra finches (>90 dph).\n# (1) Lesions: bilateral electrolytic Uva lesions in 7 birds (lesions > 90% only), and control\n# lesions 250 um dorsal (2 birds) or 200 um ventral (2 birds) to Uva. Song recorded in sound\n# isolation chambers for several days before surgery and for up to a week from the first day\n# of singing after it, undirected (social isolation) and directed (a female presented).\n# Measured from audio: syllable and gap durations, goodness of fit to an exponential (Gamma),\n# maturity index M and song rhythmicity R. (2) Recordings: multiunit activity in the\n# HVC-projecting core of Uva, right hemisphere, motorized microdrive, in 5 freely singing\n# birds; sites recorded at successive depths along a penetration; Uva identified by\n# antidromic stimulation from HVC. Single units only off song (4 HVC-projecting neurons in 2\n# birds; 5 neurons dorsal or ventral to Uva). Audio and neural signal at 40 kHz. The archive's\n# description of CRCNS aa-3 says it holds multiunit recordings from 3 birds during singing,\n# with syllable segmentations, and pre- and post-lesion song as .wav files; it does not say\n# which lesion birds, or whether control lesions and directed song are included.\n#\n# Common methods, from the Materials and methods; criteria refer to them by name.\n# - Multiunit activity (MUA): the recorded signal (hardware band-pass 300 Hz to 15 kHz)\n#   rectified and smoothed with a 2 ms (SD) Gaussian (Chronic neural recordings; Rhythmicity).\n# - Sound amplitude: audio band-passed 1 to 4 kHz, squared, smoothed with a 2.5 ms (SD)\n#   Gaussian, and in dB as 10 log10 (Sound analysis). The Rhythmicity section instead says\n#   the sound waveform was rectified and smoothed with a 2 ms (SD) Gaussian. Open for the\n#   spectral and correlation claims; readings (a) the Sound analysis amplitude in dB, (b) the\n#   same without the log, (c) the rectified audio smoothed at 2 ms.\n# - Segmentation: threshold at the Fisher discriminant of two Gaussian modes fit by EM to the\n#   log-amplitude; onsets and offsets at the nearest points 2 SD from noise; sounds separated\n#   by < 7 ms merged; sounds < 7 ms dropped; bouts are syllable sequences with gaps <= 300 ms;\n#   renditions with noise or female calls removed; onsets and offsets checked by hand (Sound\n#   analysis). Where segmentations made by the authors are in the dataset they are used;\n#   otherwise this procedure is run.\n# - Time warping: piecewise linear warping of MUA between syllable onsets and offsets onto a\n#   template motif, the motif whose length is closest to the median (Time warping).\n# - Shuffled baseline: \"baseline activity during vocalization determined from random\n#   shuffling of multiunit activity\", with a 95% band \"for maxima and minima anywhere in this\n#   window\" (Fig 4 and Fig 6 legends). The shuffle is not described. Open; readings (a)\n#   aligned averages built at random times during singing (inside bouts), (b) MUA circularly\n#   shifted within each bout relative to the syllable times. In both, 1000 shuffles (the\n#   number the Rhythmicity section uses for its null), and the band is the 2.5 and 97.5\n#   percentiles of the shuffles' maxima and minima over the plotted window. The average\n#   level of activity during singing is the mean of the shuffled averages.\n# - Spectra: Chronux, \"1 tapers, 2 time half-bandwith product\" (Rhythmicity), read as tapers\n#   [TW K] = [2 1]; a standard choice, as the text pairs one taper with TW 2. Null for\n#   coherency and cross-spectrum by randomly shifting MUA relative to song amplitude for all\n#   renditions, 1000 times. The segment over which spectra are taken (motif, bout or song\n#   file) is not stated; readings (a) each bout, (b) each motif rendition, averaged.\nschema_version: 2\npaper: doi:10.1371/journal.pone.0169568\nclaims:\n- id: lesion-directed-song-abolished\n  statement: After complete bilateral Uva lesions, birds presented with a female court her but\n    do not sing; they produce only sporadic short sounds like introductory notes without their\n    rhythm.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 1; S1 Video\n  quote: However, consistent with previous reports [ 26 , 27 ], lesioned birds failed to sing and\n    only produced sporadic short sounds, acoustically similar to introductory notes but without\n    their characteristic rhythmicity\n  criterion: The paper shows this by video and gives no measure. On post-lesion directed-song\n    recordings, segmented by the Segmentation method, reproduced when no bout of the bird's\n    pre-lesion motif occurs, judged as for the maturity index (no bout of at least 700 ms whose\n    spectral correlation with pre-lesion motifs reaches the pre-lesion birds' range), in every\n    lesioned bird recorded in the directed context. Untestable unless the dataset marks which\n    recordings were directed.\n- id: lesion-undirected-rate-similar\n  statement: In social isolation, Uva-lesioned birds sing at rates similar to intact birds.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 2\n  quote: While Uva lesions completely abolished directed singing, lesioned birds in social\n    isolation sang at rates similar as intact birds in social isolation\n  criterion: The paper gives neither the measure nor a test. Open; readings for the measure\n    (a) syllables per hour of recording, (b) bouts per hour, (c) total singing time per hour,\n    each for the first day of post-lesion singing against the last pre-lesion day; for\n    \"intact birds\" the same birds before the lesion (the only intact undirected song the\n    paper describes recording). As a claim of similarity with no test given, judged by the\n    paper's test for pre and post comparisons, the Wilcoxon signed-rank test over birds at\n    p < 0.05; reproduced when it finds no difference under the readings, with the post to\n    pre ratio of each bird reported. Rates depend on how much was recorded, so the\n    recording hours per day are reported too.\n- id: fig2g-maturity-index-drop\n  statement: Uva lesions lower the maturity index, a measure of song repeatability, from 0.26\n    to 0.08 (Wilcoxon signed-rank test, p < 0.025, 7 birds).\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 2; Fig 2G\n  quote: Uva lesions cause a significant decrease in a measure of song repeatability (maturity\n    index; M pre = 0.26±0.03, M post = 0.08±0.02; p<0.025, Wilcoxon signed rank test, n = 7\n    lesioned birds, ±SD\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.025\n    p_relation: \"<\"\n    n: 7 lesioned birds\n  expected:\n  - quantity: maturity index before lesion, mean over birds\n    value: 0.26\n    tolerance: 0.03\n  - quantity: maturity index after lesion, mean over birds\n    value: 0.08\n    tolerance: 0.02\n  criterion: Tolerances are the paper's SDs over birds. Maturity index as the Methods give it\n    (Maturity index) about 100 bouts drawn at random, only bouts 700 ms to 2 s long;\n    multitaper spectrograms (2 tapers, 10 ms window, 1 ms step, bandwidth parameter 1.5);\n    for every distinct pair of bouts, the correlation of power spectra between 860 Hz and 8.6\n    kHz for each pair of 1 ms slices; the maximum of the lag correlation function; averaged\n    over the ~10,000 pairs. Open; how the lag correlation function is formed from the\n    slice-by-slice matrix, readings (a) the mean of the matrix along each diagonal, maximum\n    over lags, (b) the same over the overlap only; the bout gap, readings (a) 300 ms (Sound\n    analysis), (b) 350 ms (Song rhythmicity); the post-lesion day, readings (a) the first day\n    of singing after surgery (Fig 2B), (b) all post-lesion days pooled. Reproduced when under\n    one reading both means are within tolerance and the decrease is significant by a\n    Wilcoxon signed-rank test at p < 0.025 over birds; partially reproduced when every bird\n    decreases but the values or the test (the test cannot reach p < 0.025 with fewer than 6\n    birds) do not hold.\n- id: fig2f-closer-to-exponential\n  statement: After Uva lesions syllable-duration distributions are much closer to exponential\n    (goodness of fit Gamma 3.7 against 16 before; Wilcoxon signed-rank test, p < 0.025, 7\n    birds), but stay above the subsong criterion of Gamma < 2.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 3; Fig 2C and 2F\n  quote: Post-lesion syllable duration distributions are significantly closer to exponential (Γ\n    post = 3.7±1.2) than are pre-lesion songs (Γ pre = 16±6) (p<0.025, Wilcoxon signed rank\n    test, n = 7 lesioned birds) ( Fig 2F ), but do not meet the strictest criterion for subsong\n    (Γ < 2)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.025\n    p_relation: \"<\"\n    n: 7 lesioned birds\n  expected:\n  - quantity: goodness of fit Gamma before lesion, mean over birds\n    value: 16\n    tolerance: 6\n  - quantity: goodness of fit Gamma after lesion, mean over birds\n    value: 3.7\n    tolerance: 1.2\n  criterion: Tolerances are the paper's spreads over birds (the text gives no unit for them;\n    read as SD, as in the paragraph before). Syllables segmented by the Segmentation method,\n    one day of singing (1000 to 10,000 syllables); an exponential fit to the syllable\n    durations by maximum likelihood; Gamma from the Lilliefors statistic (Methods, Sound\n    analysis, paragraph 3). Open; the scale of Gamma, which the Methods do not define and\n    whose values (16, threshold 2) exceed any raw Kolmogorov-Smirnov distance; readings (a)\n    the Lilliefors distance D times the square root of the number of syllables, (b) D divided\n    by the Lilliefors critical value at alpha 0.05 for that number of syllables; the\n    post-lesion day, readings as for the maturity index. Reproduced when under one reading\n    both means are within tolerance, the decrease is significant by a Wilcoxon signed-rank\n    test at p < 0.025, and the post-lesion mean is above 2.\n- id: fig2c-small-syllable-peak\n  statement: In 6 of 7 Uva-lesioned birds the post-lesion syllable-duration distribution has a\n    small peak at 50 to 100 ms.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 3; Fig 2C\n  quote: Indeed, in the majority of Uva-lesioned birds (n = 6/7), a small peak is seen in the\n    syllable distribution at 50-100ms\n  expected:\n  - quantity: lesioned birds with a post-lesion peak at 50-100 ms\n    value: 6\n    tolerance: 0\n    unit: birds of 7\n  criterion: The paper gives no rule for a peak. Open; readings (a) a local maximum of the\n    post-lesion syllable-duration histogram between 50 and 100 ms that lies above the fitted\n    exponential (the null of Fig 2C), (b) the same with the histogram counts above the 95%\n    bound of the fitted exponential's bin counts (Poisson). Bins of 5 ms, a standard choice;\n    10 ms is shown as a variant. Reproduced when the peak is found in 6 of 7 birds, or, with\n    fewer lesioned birds in the dataset, in all but at most one of them.\n- id: fig2d-gaps-broader\n  statement: After Uva lesions gap durations become broadly distributed, with more long and\n    more short gaps, like subsong.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 4; Fig 2D\n  quote: Following Uva lesions, however, gap durations become more broadly distributed, with an\n    increased incidence of long and short gaps\n  criterion: The paper gives no measure or test. Gaps from the Segmentation method, within\n    bouts. Open; readings for the measure (a) the fraction of post-lesion gaps outside the\n    bird's pre-lesion 5th to 95th percentile range of gap durations, against the 10% expected\n    if unchanged, (b) the interquartile range of log gap duration, post against pre. Reproduced\n    when under one reading the change is in the claimed direction in every lesioned bird, or\n    is significant by the Wilcoxon signed-rank test the paper uses for its other pre and post\n    comparisons at p < 0.05, with, for reading (a), both the short and the long fractions\n    increased.\n- id: fig2e-rhythmicity-drop\n  statement: Uva lesions decrease song rhythmicity, R, from 3.30 to 1.7 (Wilcoxon signed-rank\n    test, p < 0.025, 7 birds).\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 5; Fig 2E\n  quote: the increase in variability in both syllable and gap durations following Uva lesions is\n    accompanied by a significant decrease in rhythmicity of song temporal structure in\n    post-lesion birds ( Fig 2E ; R pre = 3.30±1.1, R post = 1.7±0.3; p<0.025 Wilcoxon signed\n    rank test, n = 7 lesioned birds\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.025\n    p_relation: \"<\"\n    n: 7 lesioned birds\n  expected:\n  - quantity: song rhythmicity R before lesion, mean over birds\n    value: 3.3\n    tolerance: 1.1\n  - quantity: song rhythmicity R after lesion, mean over birds\n    value: 1.7\n    tolerance: 0.3\n  criterion: Tolerances are the paper's spreads over birds. Rhythmicity as in Methods, Song\n    rhythmicity; bouts with gaps of no more than 350 ms; amplitude in each bout rectified,\n    smoothed, log-scaled, mean-subtracted and detrended; spectrum by Chronux with [2 1] tapers;\n    normalized by bout length and squared, then averaged over bouts; R is the maximum above 3\n    Hz of the ratio of this spectrum to the null spectrum. Open; the smoothing, readings as\n    for Sound amplitude in the header; the null spectrum, \"generated from an exponential\n    distribution of syllable durations and a unimodal distribution of gap durations\", with\n    neither fitted distribution nor the synthetic amplitude given; readings (a) synthetic\n    bouts of alternating syllables and gaps, durations drawn from an exponential fit to the\n    bird's own syllable durations and a log-normal fit to its gap durations, amplitude the\n    bird's mean syllable and gap levels, run through the same pipeline, (b) the same with the\n    syllable and gap distributions of the bird's post-lesion song; the post-lesion day,\n    readings as for the maturity index. Reproduced when under one reading both means are\n    within tolerance and the decrease is significant by a Wilcoxon signed-rank test at p <\n    0.025.\n- id: fig2e-residual-rhythm-peak\n  statement: Unlike subsong, 6 of 7 Uva-lesioned birds keep a significant peak in the song\n    rhythm spectrum between 3 and 8 Hz.\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 5; Fig 2E legend\n  quote: However, unlike subsong birds that had no significant rhythmicity, 6 of 7 Uva-lesioned\n    birds exhibited a significant peak in the power spectrum between 3-8Hz\n  expected:\n  - quantity: lesioned birds with a significant post-lesion peak at 3-8 Hz\n    value: 6\n    tolerance: 0\n    unit: birds of 7\n  depends_on:\n  - fig2e-rhythmicity-drop\n  criterion: Spectra and null as in fig2e-rhythmicity-drop, under each of its readings. The\n    test of a peak is not given. Open; readings (a) the ratio to the null spectrum exceeds the\n    95th percentile of the same ratio computed on synthetic null bouts (the null of reading\n    (a) or (b) of that claim, 1000 draws) at some frequency between 3 and 8 Hz, (b) the band\n    of the Fig 2E legend, 4 to 8 Hz, with the same test. Reproduced when the peak is found in\n    6 of 7 birds, or, with fewer lesioned birds, in all but at most one.\n- id: figs1-control-lesions-no-effect\n  statement: Control lesions 250 um dorsal or 200 um ventral to Uva have no significant effect\n    on syllable or gap duration distributions, maturity index or song rhythm (p > 0.50, 4\n    birds).\n  source: Results, Uva is necessary for adult stereotyped song, paragraph 6; S1 Fig\n  quote: these control lesions had no effect on song structure as assessed in song spectrograms,\n    nor did they have a significant effect on syllable or gap duration distributions (p>0.50 for\n    all measurements, n = 4 birds), on maturity index (p>0.50), or song rhythm spectrum (p>0.50)\n  statistics:\n  - about: syllable and gap duration distributions\n    p: 0.5\n    p_relation: \">\"\n    n: 4 control birds\n  - about: maturity index\n    p: 0.5\n    p_relation: \">\"\n    n: 4 control birds\n  - about: song rhythm spectrum\n    p: 0.5\n    p_relation: \">\"\n    n: 4 control birds\n  criterion: A claim of absence. The test is not named; the paper's test for the same measures\n    in Uva-lesioned birds is the Wilcoxon signed-rank test, used here on Gamma (syllables and,\n    for gaps, the same fit to gap durations), M and R, each computed as in the claims above\n    under their readings. Reproduced when no test gives p < 0.05; not reproduced when one\n    does; the pre and post values of each bird are reported. With 4 birds the exact two-sided\n    test cannot fall below 0.125, so the per-bird changes are also compared with the Uva\n    lesion changes. Untestable if the dataset has no control-lesion birds.\n- id: fig3-antidromic\n  statement: Antidromic responses of Uva neurons to HVC stimulation have short latencies (1.5\n    to 5 ms), small jitter (< 100 us), and thresholds of 70 to 300 uA.\n  source: Results, Song-related activity in Uva, paragraph 1; Fig 3B and 3C\n  quote: Antidromic responses had short latencies (1.5-5ms) with a small jitter (<100μs), and\n    could be elicited by stimulation intensity of 70–300μA\n  expected:\n  - quantity: antidromic latency range\n    value: 1.5\n    tolerance: 0.15\n    unit: ms (lower bound)\n  - quantity: antidromic latency range\n    value: 5\n    tolerance: 0.5\n    unit: ms (upper bound)\n  - quantity: jitter\n    value: 100\n    tolerance: 10\n    unit: us (upper bound)\n  criterion: A reported range; holds when every latency lies within 1.35 to 5.5 ms and every\n    jitter, the SD of latency across stimulations of one unit, is below 110 us. Latency is the\n    time from stimulus to the response spike. Stimulus intensities are judged only if the\n    dataset records them (70 to 300 uA, widened to 63 to 330 uA). Collision (Fig 3B, red\n    arrow) is reported where seen. Untestable unless the dataset holds antidromic\n    stimulation recordings with stimulus times.\n- id: single-unit-spontaneous-rates\n  statement: HVC-projecting Uva neurons recorded off song fire regularly at 20 to 50 Hz (4\n    neurons, 2 birds), while units just dorsal or ventral to the core fire below 10 Hz (5\n    neurons).\n  source: Results, Song-related activity in Uva, paragraph 1\n  quote: Single-unit recordings of HVC-projecting Uva neurons during non-singing revealed regular\n    spontaneous spiking at 20-50Hz (n = 4 neurons, n = 2 birds). Single-units recorded just\n    dorsal or ventral to HVC-projecting core of Uva appeared to exhibit much lower rates of\n    spontaneous spiking (n = 5 neurons, <10Hz)\n  expected:\n  - quantity: spontaneous rate of HVC-projecting Uva neurons\n    value: 20\n    tolerance: 2\n    unit: Hz (lower bound)\n  - quantity: spontaneous rate of HVC-projecting Uva neurons\n    value: 50\n    tolerance: 5\n    unit: Hz (upper bound)\n  - quantity: spontaneous rate of units outside the core\n    value: 10\n    tolerance: 1\n    unit: Hz (upper bound)\n  criterion: Mean firing rate of each single unit outside singing. Holds when the HVC-projecting\n    units fire within 18 to 55 Hz and the units outside the core below 11 Hz. \"Regular\" is not\n    measured in the paper; the coefficient of variation of interspike intervals is reported.\n    Untestable unless the dataset holds sorted single units with their location.\n- id: fig4c-call-premotor\n  statement: Uva activity rises sharply just before distance calls, leaving baseline 30 ms and\n    peaking 15 ms before call onset.\n  source: Results, Song-related activity in Uva, paragraph 2; Fig 4C\n  quote: Uva activity increases sharply immediately prior to the onset of distance calls ( Fig 4C\n    ; latency from baseline = 30±7ms, latency from peak = 15±5ms, ±SD)\n  expected:\n  - quantity: latency from baseline before call onset\n    value: 30\n    tolerance: 7\n    unit: ms\n  - quantity: latency of peak before call onset\n    value: 15\n    tolerance: 5\n    unit: ms\n  criterion: Tolerances are the paper's SDs. MUA aligned to call onsets and averaged over\n    renditions (Fig 4C legend), with the Shuffled baseline. Latency from baseline is the time\n    before onset at which the average crosses above the 95% band and stays above it to the\n    peak; latency of peak is the time of the maximum before onset, searched in the 100 ms\n    before onset (a standard window). The unit of the SD (over birds or renditions) is not\n    stated; values are averaged over birds, and the per-bird values are reported. Reproduced\n    when both are within tolerance under one reading of the shuffle.\n- id: fig4b-introductory-note-premotor\n  statement: Uva is robustly active before each introductory note, leaving baseline 39 ms and\n    peaking 21 ms before note onset.\n  source: Results, Song-related activity in Uva, paragraph 2; Fig 4B\n  quote: One of the most prominent features of Uva activity during singing is the robust\n    activation prior to each introductory note ( Fig 4B , latency from baseline = 39±8ms, peak\n    latency = 21±9ms, ±SD)\n  expected:\n  - quantity: latency from baseline before introductory note onset\n    value: 39\n    tolerance: 8\n    unit: ms\n  - quantity: latency of peak before introductory note onset\n    value: 21\n    tolerance: 9\n    unit: ms\n  criterion: As fig4c-call-premotor, with introductory note onsets in place of call onsets.\n- id: fig4a-elevated-during-song\n  statement: During bouts of singing Uva activity is persistently elevated and modulated in a\n    way locked to song.\n  source: Results, Song-related activity in Uva, paragraph 2; Fig 4A\n  quote: During bouts of singing, Uva activity is persistently elevated and is strongly modulated\n    in a manner locked to song\n  criterion: The paper gives no test. Per recording site, mean MUA inside bouts (Segmentation\n    method bouts) against mean MUA outside singing in the same files, more than 300 ms from\n    any vocalization (the bout gap). Reproduced when the mean inside bouts is higher at every\n    site, or significantly higher over sites by a paired t-test at p < 0.05, the test the\n    paper uses for syllable-related modulation. Locking to song is tested in\n    fig5-consistent-across-renditions.\n- id: fig5-consistent-across-renditions\n  statement: Uva activity is consistent across renditions of the song motif; time-warped MUA is\n    correlated across renditions (0.64 with 5 ms smoothing) and coherent below 12 Hz (mean\n    coherence 0.68 between 1 and 12 Hz).\n  source: Results, Song-related activity in Uva, paragraph 2; Fig 5A to 5C\n  quote: the smoothed multiunit signals are highly correlated across different song renditions\n    (0.64±0.06 with 5ms smoothing) and coherent across different song renditions at frequencies\n    below 12Hz (C avg = 0.68±0.09 between 1-12Hz, ±SD)\n  expected:\n  - quantity: correlation of MUA across renditions, 5 ms smoothing\n    value: 0.64\n    tolerance: 0.06\n  - quantity: mean coherence across renditions, 1 to 12 Hz\n    value: 0.68\n    tolerance: 0.09\n  criterion: Tolerances are the paper's SDs. MUA time-warped to the template motif (Time\n    warping); for the correlation, smoothed with a 5 ms Gaussian as the quote states (read as\n    SD, as for the 2 ms kernel). Coherence by Chronux with [2 1] tapers on the 2 ms MUA,\n    averaged from 1 to 12 Hz, against the null of Fig 5C (random shifts, 1000 times). Open;\n    readings for the correlation (a) the mean Pearson correlation at zero lag over all pairs\n    of renditions, (b) the peak of the cross-correlation (Fig 5B) averaged over pairs, (c)\n    each rendition against the mean of the others; the same pairing for coherence. Values\n    averaged over birds. Reproduced when under one reading both values are within tolerance.\n- id: fig5-consistent-across-sites\n  statement: Uva activity is similar at different recording depths along a penetration;\n    correlation 0.62 with 5 ms smoothing and mean coherence 0.65 between 1 and 12 Hz, with no\n    evidence that activity varies across sites.\n  source: Results, Song-related activity in Uva, paragraph 3; Fig 5D to 5F\n  quote: We find that activity at different recording sites throughout Uva is also highly\n    correlated (0.62±0.03 with 5ms smoothing) and coherent (C avg = 0.65±0.13 between 1-12Hz,\n    ±SD)\n  expected:\n  - quantity: correlation of mean MUA across sites, 5 ms smoothing\n    value: 0.62\n    tolerance: 0.03\n  - quantity: mean coherence across sites, 1 to 12 Hz\n    value: 0.65\n    tolerance: 0.13\n  criterion: As fig5-consistent-across-renditions, with the time-warped average trace of each\n    site (Fig 5D) in place of single renditions, compared over pairs of sites of one\n    penetration. Sites are the depths listed for each bird's recordings. Open; readings (a)\n    pairs of site averages, (b) single renditions from different sites. Reproduced when under\n    one reading both values are within tolerance.\n- id: fig6-peak-before-onset\n  statement: Uva activity rises significantly before syllable onsets in every bird, peaking 20\n    ms before onset and rising above its average level during singing 32 ms before onset.\n  source: Results, Song-related activity in Uva, paragraph 4; Fig 6A, 6B and 6D; S2 and S3 Figs\n  quote: exhibiting a significant increase in activity prior to syllable onsets (p<0.01 paired\n    t-test) ... significant for each bird recorded; n = 5). Uva activity peaks 20±2ms (±SEM)\n    prior to syllable onsets, and rises significantly above the average level of activity\n    during singing 32±5ms before syllable onsets\n  statistics:\n  - test: paired t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: each of 5 birds\n  expected:\n  - quantity: time of MUA peak before syllable onset, mean over birds\n    value: 20\n    tolerance: 2\n    unit: ms\n  - quantity: time MUA rises above the singing average before onset, mean over birds\n    value: 32\n    tolerance: 5\n    unit: ms\n  criterion: Tolerances are the paper's SEMs. MUA aligned to all selected syllable onsets of a\n    bird and averaged (Fig 6B), with the Shuffled baseline; the rise time is when the average\n    leaves the 95% band upward before onset, the peak the maximum in the 100 ms before onset (a\n    standard window). The paired t-test is not described. Open; readings (a) per rendition,\n    mean MUA in the 40 ms before onset (the span of the reported rise) against the same\n    rendition's mean MUA over its bout, (b) the same window against the 40 ms window centred\n    on the preceding syllable's offset. Reproduced when the paired t-test gives p < 0.01 in\n    every bird under one reading and both times, averaged over birds, are within tolerance;\n    partially reproduced when the test holds but a time does not.\n- id: fig6-dip-before-offset\n  statement: Uva activity falls significantly before syllable offsets in every bird, reaching\n    a minimum 18 ms before offset and dropping below its average level during singing 48 ms\n    before offset.\n  source: Results, Song-related activity in Uva, paragraph 4; Fig 6C and 6E; S2 and S3 Figs\n  quote: a significant decrease prior to syllable offsets ( Fig 6B ; significant for each bird\n    recorded; n = 5) ... The decrease in Uva activity at syllable offsets reaches a minimum\n    18±1ms (±SEM) prior to the offset ( Fig 6D ) and drops significantly below average Uva\n    activity during singing 48±8ms prior to the offset\n  statistics:\n  - test: paired t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: each of 5 birds\n  expected:\n  - quantity: time of MUA minimum before syllable offset, mean over birds\n    value: 18\n    tolerance: 1\n    unit: ms\n  - quantity: time MUA drops below the singing average before offset, mean over birds\n    value: 48\n    tolerance: 8\n    unit: ms\n  criterion: As fig6-peak-before-onset, aligned to syllable offsets, with the minimum and a\n    downward crossing of the 95% band, and for the test the 50 ms before offset (the span of\n    the reported drop) against the rendition's bout mean, reading (a), or against the 40 ms\n    before the next onset, reading (b). The p < 0.01 of the paper is printed with the onset\n    increase; the offset decrease is read as tested the same way.\n- id: fig7a-correlation-with-amplitude\n  statement: Uva activity correlates with song amplitude (peak correlation 0.40) and leads it\n    by 42 ms.\n  source: Results, Song-related activity in Uva, paragraph 4; Fig 7A\n  quote: Uva activity is also strongly correlated with song amplitude (magnitude of peak\n    correlation, 0.40±0.04), with a latency of 42±6ms ( Fig 7A , ± S.D)\n  expected:\n  - quantity: magnitude of peak correlation, MUA with song amplitude\n    value: 0.4\n    tolerance: 0.04\n  - quantity: lag at peak correlation, MUA leading amplitude\n    value: 42\n    tolerance: 6\n    unit: ms\n  criterion: Tolerances are the paper's SDs. Cross-correlation of MUA with sound amplitude\n    during singing, per bird, averaged over 5 birds (Fig 7A). Open; the amplitude, readings as\n    in the header; the segments, readings (a) bouts, (b) motifs; the normalization, Pearson\n    correlation at each lag. Reproduced when under one reading the peak magnitude and its lag\n    (MUA first) are within tolerance.\n- id: spectral-features-weak\n  statement: None of six spectral song features correlates significantly with Uva activity\n    within a bird; pooled over birds only amplitude (r = 0.18) and gravity center (r = 0.17)\n    do, after Bonferroni correction.\n  source: Results, Song-related activity in Uva, paragraph 5\n  quote: None of these six spectral features is significantly correlated with Uva activity in\n    individual birds. When combined across all birds, only amplitude (r = 0.18) and gravity\n    center (r = 0.17) exhibit significant correlation after Bonferroni correction for multiple\n    comparisons (6 comparisons; p<0.008)\n  statistics:\n  - about: amplitude and gravity center, all birds combined\n    test: correlation\n    statistic: r = 0.18 and r = 0.17\n    p: 0.008\n    p_relation: \"<\"\n    corrected: Bonferroni, 6 comparisons\n  expected:\n  - quantity: correlation of MUA with amplitude, all birds\n    value: 0.18\n    tolerance: 0.018\n  - quantity: correlation of MUA with gravity center, all birds\n    value: 0.17\n    tolerance: 0.017\n  criterion: Features (pitch goodness, Wiener entropy, amplitude, amplitude modulation,\n    frequency modulation, gravity center) as defined in Sound Analysis Pro, which the Methods\n    name for recording; windows from 10 ms after syllable onset to 10 ms before offset; MUA\n    taken 42 ms earlier than the song (Results, paragraph 5). Open; the unit of correlation,\n    readings (a) per syllable rendition, the mean feature against the mean MUA, (b) per time\n    bin (1 ms) within the windows; for (a) features z-scored within syllable type before\n    pooling as a variant. Pearson r, Bonferroni over 6 features (alpha 0.05/6). Reproduced\n    when under one reading no feature passes in any single bird, and in the pooled data\n    amplitude and gravity center pass with r within tolerance and the other four do not.\n- id: fig7b-10hz-power-peaks\n  statement: Song amplitude and Uva activity both have a broad spectral peak near 10 Hz, at 8.0\n    Hz for song and 8.8 Hz for Uva.\n  source: Results, Song-related activity in Uva, paragraph 6; Fig 7B\n  quote: we found that the song amplitude profile of our adult birds exhibits a broad spectral\n    peak near this frequency ( Fig 7B ; peak of average song rhythm spectrum at 8.0Hz). Notably,\n    Uva multiunit activity also exhibits peaks at nearly the same frequency (8.8Hz)\n  expected:\n  - quantity: peak frequency of the average song amplitude spectrum\n    value: 8.0\n    tolerance: 0.8\n    unit: Hz\n  - quantity: peak frequency of the average MUA spectrum\n    value: 8.8\n    tolerance: 0.88\n    unit: Hz\n  criterion: Power spectra as in the header (Spectra), normalized and averaged over 5 birds\n    (Fig 7B). The peak is the maximum of the average normalized spectrum above 3 Hz (the bound\n    of Song rhythmicity) and below 30 Hz (a standard window for a \"near 10 Hz\" peak). Open;\n    the normalization, readings (a) by the sum of the spectrum, as for long syllables\n    (Rhythmicity, paragraph 2), (b) by bout length, as for song rhythm; the segments as in the\n    header. Reproduced when under one reading both peaks are within tolerance.\n- id: fig7d-10hz-coherence\n  statement: Uva activity and song amplitude are significantly coherent near 10 Hz (peak at\n    8.8 Hz, coherence 0.75, p < 0.01, phase -0.77 pi), with a large peak in their\n    cross-spectrum.\n  source: Results, Song-related activity in Uva, paragraph 6; Fig 7C and 7D\n  quote: Further analysis reveals a large peak in the cross spectral density between multiunit\n    activity and song amplitude, as well as a significant coherency at this frequency (F peak =\n    8.8Hz, C peak = 0.75, p<0.01, phase = -0.77π)\n  statistics:\n  - test: coherency against a null of randomly shifted MUA, corrected for multiple testing\n    p: 0.01\n    p_relation: \"<\"\n    n: 5 birds\n  expected:\n  - quantity: frequency of peak coherency\n    value: 8.8\n    tolerance: 0.88\n    unit: Hz\n  - quantity: peak coherency\n    value: 0.75\n    tolerance: 0.075\n  - quantity: phase at peak coherency\n    value: -0.77\n    tolerance: 0.077\n    unit: pi radians\n  criterion: Coherency and cross-spectrum of MUA with song amplitude by Chronux with [2 1]\n    tapers, averaged over birds; null by random shifts of MUA relative to amplitude, 1000\n    times (Rhythmicity, paragraph 1), with the 95th percentile corrected for multiple testing\n    by taking it on the maximum over frequencies (Fig 7D legend gives the correction but not\n    its form; this is a standard choice). Peak between 3 and 30 Hz. Phase sign as Chronux\n    returns it; the opposite convention is shown. Reproduced when under one reading of the\n    segments and amplitude the peak frequency, coherency and phase are within tolerance and\n    the peak exceeds the null at p < 0.01.\n- id: fig8-no-gte-relation\n  statement: Uva activity shows no significant correlation with gesture trajectory extrema\n    (GTEs), in single birds or averaged across birds, against GTE times shuffled within\n    syllables.\n  source: Results, Song-related activity in Uva, paragraph 7; Fig 8D to 8F\n  quote: No significant peaks are observed in this correlation within individual birds or\n    averaged across birds, compared to surrogate datasets in which GTE times are randomly\n    shuffled within song syllables\n  criterion: A claim of absence, judged on the paper's test. GTE times from the automated\n    method of Boari et al. (ref 50, a published model of the syrinx; no code linked, so the\n    authors' published implementation is to be used if public). Cross-correlation of MUA with\n    the GTE train, against 1000 surrogates (a standard number) where the GTE count is\n    redistributed across syllables in proportion to their length and then placed at random\n    within syllables, GTEs at syllable onsets and offsets kept in place (GTE analysis); the\n    band is the 99% interval of the surrogates (Fig 8E and 8F legend), lags within +-100 ms (a\n    standard window). Reproduced when no lag leaves the band in any bird or in the average;\n    not reproduced when one does. The largest excursion is reported.\n- id: fig9-long-syllable-gamma\n  statement: In long syllables (> 150 ms; 13 syllables, 43% of song syllables) Uva activity\n    can oscillate fast; 8 of 13 have a significant spectral peak above 10 Hz, at 17 to 51 Hz,\n    and Uva activity is coherent with song amplitude from 1 to 55 Hz.\n  source: Results, Song-related activity in Uva, paragraph 8; Fig 9A to 9D; S4 Fig\n  quote: analysis done for 13 syllables longer than 150ms, in order to provide adequate sample\n    duration; this was 43% of all song syllables). Of these 13 syllables, 8 syllables show a\n    significant peak in the spectrum of the neural activity greater than 10Hz. These peaks\n    occur at frequencies ranging from 17 to 51Hz. Notably, in individual syllables, Uva\n    activity and sound amplitude are found to be significantly coherent across a broad range\n    of frequencies (1-55Hz)\n  expected:\n  - quantity: syllable types longer than 150 ms\n    value: 13\n    tolerance: 1.3\n  - quantity: fraction of song syllable types longer than 150 ms\n    value: 0.43\n    tolerance: 0.043\n  - quantity: long syllables with a significant MUA peak above 10 Hz\n    value: 8\n    tolerance: 0.8\n    unit: of 13\n  - quantity: frequencies of those peaks\n    value: 17\n    tolerance: 1.7\n    unit: Hz (lower bound)\n  - quantity: frequencies of those peaks\n    value: 51\n    tolerance: 5.1\n    unit: Hz (upper bound)\n  criterion: Long syllables are syllable types whose duration exceeds 150 ms; spectra of MUA\n    and amplitude from onset to 50 ms before offset, normalized by their sum; null by\n    scrambling MUA then smoothing at 2 ms (Rhythmicity, paragraph 2); significance against the\n    95% band for maxima anywhere in the window (Fig 9 legend). Open; \"syllable\" as a type\n    pooled over renditions (the counts 13 and 43%), or renditions; length as the median\n    duration of the type. The counts can only be matched on the 5 birds; with fewer birds the\n    fractions are compared (8/13 = 0.62, tolerance 10%), with peaks within 15.3 to 56.1 Hz.\n    The coherence part holds when the across-bird average coherence exceeds the null band\n    over most of 1 to 55 Hz.\n- id: bout-offset-suppression\n  statement: Uva activity is transiently suppressed for about 200 ms after bout offsets.\n  source: Results, Song-related activity in Uva, paragraph 9; S5 Fig; Fig 4A legend\n  quote: We did find, however, that Uva activity was transiently suppressed following bout\n    offsets for a period of approximately 200ms\n  expected:\n  - quantity: duration of suppression after bout offset\n    value: 200\n    tolerance: 20\n    unit: ms\n  criterion: MUA aligned to bout offsets (bouts per the Segmentation method) and averaged,\n    against the baseline during non-singing from random shuffling of MUA, with its 95% band\n    for maxima and minima (S5 Fig legend); shuffle readings as in the header, with the random\n    times taken outside singing. Suppression lasts from offset until the average returns into\n    the band. Reproduced when the average falls below the band after offset and the duration\n    is within tolerance.\n- id: no-motif-bout-signal\n  statement: Uva shows little activation related to the onsets or offsets of motifs or bouts.\n  source: Results, Song-related activity in Uva, paragraph 9\n  quote: Finally, we find little evidence for activation in Uva related to the onsets or offsets\n    of longer timescale song structures, such as song motifs or bouts\n  depends_on:\n  - fig6-peak-before-onset\n  criterion: A claim of absence; the paper names no test. As for syllables (Fig 6), MUA\n    aligned to motif onsets and offsets, and to bout onsets and offsets, against the\n    Shuffled baseline. The paper's comparison is the syllable-level signal. Reproduced when\n    the peak before motif and bout onsets is no larger than the peak before other syllable\n    onsets (two-sample t-test over renditions at p < 0.05, the test level of Fig 6), and no\n    excursion above the band follows motif or bout offsets; not reproduced otherwise. The\n    suppression after bout offsets (bout-offset-suppression) is not activation and does not\n    count against the claim. Introductory notes before bouts are excluded from the bout-onset\n    alignment, as their activation is a separate finding (fig4b-introductory-note-premotor).\n"
}
```

```
File created successfully at: claims/danish-2017.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/danish-2017.yaml",
 "old_string": "(magnitude of peak\n    correlation, 0.40±0.04), with",
 "new_string": "(magnitude of peak\n    correlation ... 0.40±0.04), with"
}
```

```
The file claims/danish-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "[^ ]: " claims/danish-2017.yaml | grep -v "^[0-9]*:#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: " ; grep -n "—\|rather" claims/danish-2017.yaml; python tools/claims_check.py claims/danish-2017.yaml paper/10.1371-journal.pone.0169568.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/danish-2017.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
for x in c:
  for k,v in x.items():
    if isinstance(v,str) and ': ' in v: print(x['id'],k)
"
```

```
26 26 10 8 26 19
```

**Agent**

I wrote `claims/danish-2017.yaml`. The quote checker passes it: 26 claims, 26 quotes, 10 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (PMC5472270, Europe PMC full-text XML), with main text, figure legends and Materials and methods. The supplement is only legends (S1 Video, S1 to S5 Figs), and those are all in the text. No PDF was supplied, and none was needed. The paper links no code. It names Chronux and the GTE method of Boari et al. without versions. I did not read the dataset's own scripts, because they are part of its files.

**Claims.**
- **Coverage:** 9 claims on lesions (Fig 2, S1 Fig) and 17 on recordings (Figs 3 to 9, S2 to S5 Figs).
- **Quotes:** all 26 have one, so none needed an `inferred` note.
- **Statistics:** 8 claims carry 10 entries: the three Wilcoxon tests with p < 0.025 (n = 7), the three control comparisons with p > 0.50, the paired t-tests with p < 0.01, the Bonferroni-corrected feature correlations, and the coherency at p < 0.01.
- **Expected values:** 19 claims have them. Tolerances follow the paper's SD or SEM where it gives one, and 10% otherwise.
- **Criteria:** all 26 claims have one.

**Details the paper leaves open, and the readings named for each:**
- **Sound amplitude:** (a) Sound analysis amplitude (1 to 4 kHz, squared, 2.5 ms Gaussian) in dB; (b) the same without the log; (c) rectified audio smoothed at 2 ms, as the Rhythmicity section says.
- **Shuffled baseline:** (a) averages at random times during singing; (b) a circular shift within each bout.
- **Spectral segments:** (a) each bout; (b) each motif rendition.
- **Taper setting:** "1 tapers, 2 time half-bandwidth" is read as Chronux [2 1], named as a standard choice.
- **Maturity index:** two ways of forming the lag correlation function. Also the bout gap (300 ms or 350 ms) and the post-lesion day (first day of singing, or all days pooled).
- **Goodness of fit Γ:** its scale is undefined: (a) the Lilliefors distance D times √n; (b) D divided by the critical value at alpha 0.05.
- **Null spectrum for rhythmicity R:** (a) an exponential fit to syllable durations and a log-normal fit to gaps from the bird's own song; (b) the same fits taken from its post-lesion song.
- **Peak tests:** the rule for a significant rhythm peak (3 to 8 Hz, or the legend's 4 to 8 Hz) and for a peak at 50 to 100 ms in the syllable-duration distribution.
- **Paired t-test around syllable onsets and offsets:** the window compared with (a) the rendition's bout mean or (b) a window around the neighbouring syllable boundary.
- **Correlation pairing across renditions and sites:** zero-lag pairs, peak cross-correlation, or one against the mean of the others.
- **Spectral features:** correlated per rendition or per time bin.
- **Spectrum normalization:** by the sum or by bout length.
- **Unnamed tests:** the measure and test for "sang at rates similar", "gaps more broadly distributed", the control-lesion comparisons (read as Wilcoxon), and the motif and bout absence claim.
- **Standard choices:** histogram bins, peak-search windows, the multiple-comparison form for coherency, and the number of GTE surrogates.

**Missing from the paper.**
- No code is linked, so the GTE claim depends on Boari et al.'s implementation being public.
- The paper gives no test or measure for the directed-song claim (shown only by video) or the singing-rate claim.
- The paper reports 5 recorded birds and 7 lesioned birds. The archive's description says the dataset holds multiunit recordings from 3 birds. It does not say whether control lesions, directed-song recordings, antidromic stimulation recordings or single units are included. I noted this in the opening comment and made the count criteria allow for fewer birds.

## End of run

17 turns, 5 minutes, $1.38 at API prices, result: success.
