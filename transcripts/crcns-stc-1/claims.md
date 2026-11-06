# crcns-stc-1 · claims · run 42253590640

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls claims/001453/ claims/crcns-stc-1/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/stc-1.data-description.txt | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,282p paper/stc-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "=== \|SUPPLEMENT\|Supplemental" paper/10.1016-j.neuron.2011.06.015.txt | sed -n 1,60p
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt",
 "offset": 1150,
 "limit": 260
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "supplemental exp\|Supplemental Experimental\|Figure S" paper/10.1016-j.neuron.2011.06.015.txt | head -40; python -c "import fitz;d=fitz.open('paper/10.1016-j.neuron.2011.06.015.supp.pdf');print(d.page_count)" 2>&1; ls tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftotext pdftoppm; python -c "import pypdf" 2>&1; pdftotext -f 11 -l 11 -layout paper/10.1016-j.neuron.2011.06.015.pdf - 2>&1 | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.pdf",
 "pages": "11"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls claims | head; ls claims | grep -i crcns
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

[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-hc-9; head -40 claims/crcns-hc-9/*.yaml; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
10.1523-jneurosci.5680-12.2013.yaml
# Claims for Quattrocolo & Maccaferri (2013), J Neurosci 33:5486-5498, on CRCNS data set hc-9
# (doi:10.6080/K0HQ3WTH).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Materials and Methods, Results, Discussion and the legends of Figures 1 to 13. The
# paper has no supplement. It links no analysis code, so none was read. The PDF could not be
# rendered here, and the extracted text prints the signs =, < and > (and minus, plus/minus,
# mu, Omega) as a replacement character. Each p_relation below is read from the sentence it
# sits in: a difference the text calls significant, or a change it reports, is p < 0.05; one
# it calls absent ("did not change significantly", "similar", "ineffective", "returned to
# baseline") is p > 0.05. Values printed with that character between them are read as mean
# plus/minus SE, as the Methods state ("Data are presented as mean ±SE").
#
# Data the paper used. Acute hippocampal slices (350 um) from mice of either sex, P10 to P19:
# CXCR4-EGFP mice (Cajal-Retzius cells labelled by EGFP; 56 animals) and Sst-IRES-Cre;
# ChR2(H134R)-EYFP mice (8 animals) for the optogenetic experiments. Recordings at 30-32 C,
# filtered at 3 kHz and digitized at 10-20 kHz (Multiclamp 700, Clampex 9). Experiments:
[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:])"; sed -n 40,80p claims/crcns-hc-9/*.yaml
```

```
'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
      }
     },
     {
      "if": {
       "properties": {
        "kind": {
         "const": "link"
        }
[... 219 more lines not kept]
```

**Agent**

Paper text and supplement are present (the supplement holds the eight figure legends). The paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "content": "# Claims for Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), Neuron 71:750-761,\n# \"Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual Cortex\", on CRCNS data\n# set stc-1 (doi:10.6080/K07P8WKF).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),\n# with its Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, and\n# the Supplemental Information PDF (legends of Figures S1 to S8). The article says the\n# Supplemental Information \"includes Experimental Procedures and eight figures\"; the supplement\n# as supplied, whose own contents page lists only the eight figures, holds no further\n# procedures, so the Experimental Procedures of the article are taken as the whole Methods.\n# The PDF could not be rendered here; the extracted text prints degree signs, minus signs and\n# \"approximately\" as a replacement character, and quotes avoid those places. The paper links no\n# analysis code, so none was read.\n#\n# Data the paper used. Eight male rhesus monkeys (Macaca mulatta): three \"naive\" animals trained\n# only to fixate, and five \"trained\" animals extensively trained in a vestibular and visual\n# heading discrimination task (left or right of straight ahead) before recording. Pairs of\n# single units recorded simultaneously in area MSTd while the animals fixated passively and\n# experienced headings of 0, +-22.5, +-45, +-90, +-135 and 180 degrees relative to straight\n# ahead, in the horizontal and/or vertical plane, in two interleaved conditions: vestibular\n# (motion platform, Gaussian velocity profile, 2 s, peak acceleration about 1 m/s2) and visual\n# (optic flow, 3D star cloud). Each stimulus typically repeated five times, at least three for\n# inclusion. Spike counts in the middle 1 s of the 2 s stimulus. 179 pairs from 270 neurons:\n# 57 pairs on electrodes in separate guide tubes (0.8 to 25 mm apart), 55 pairs on electrodes\n# in one guide tube, 67 pairs from single-electrode recordings sorted offline (distance set to\n# 50 um). The main analyses use the 127 pairs separated by less than 1 mm: 89 in trained and\n# 38 in naive animals; per animal 35, 26, 18, 8 and 2 pairs (trained) and 22, 11 and 5\n# (naive). 41 pairs in trained animals were also recorded during the discrimination task.\n# Measured variables per pair: noise correlation (per condition and pooled), signal\n# correlation per condition, preferred headings, interneuronal distance, and the spike times\n# behind the time courses of Figures 2C and 3. Figure 4, Figure S4 and Figures 8A and 8B use a\n# larger database of single-electrode recordings from earlier studies (Gu et al. 2006, 2007,\n# 2008a, 2010; visual n = 992, vestibular n = 556 tuned neurons; choice probabilities n = 311).\n# Figure 2A uses behavioral thresholds over training (Fetsch et al. 2009; Gu et al. 2007,\n# 2008a). Figure S8 uses eye position records. Figures 6, 7A and 7C are simulations built on\n# the regression of noise on signal correlation fitted here.\n#\n# By its title and description, CRCNS stc-1 holds derived data (MATLAB files) from MSTd and\n# VIP; its experiment 3 is described as 127 MSTd pairs with signal and noise correlations for\n# the vestibular and visual conditions and the preferred headings of each pair, and lists this\n# paper. Experiments 1 and 2 (single neurons) and the VIP pairs are described as coming from\n# other papers. Whether the dataset holds spike times, distances, training group labels,\n# pooled noise correlations or tuning curves is for the author to find.\n#\n# Method details fixed by the Experimental Procedures: spike counts in the middle 1 s of the\n# stimulus; per heading, responses z-scored (minus the mean, divided by the SD); points with\n# z-scores larger than 3 removed; z-scores pooled across headings, then across the visual and\n# vestibular conditions, and rnoise is the Pearson correlation of the pooled z-scores. Signal\n# correlation is the Pearson correlation of the two tuning curves (mean firing rate in the\n# middle 1 s per heading), per condition. Time courses in 500 ms windows stepped by 50 ms (31\n# windows). Permutation tests on the sum of squared differences between group time courses,\n# 10,000 permutations, p the proportion of permuted values above the observed one. Fano factor\n# from a type II regression of log variance on log mean with the slope fixed at 1, as\n# 10^intercept, values below 0.1 set to 0.1 (Figure S3). Population thresholds from Fisher\n# information (equations 2 to 5), with the covariance Q = r sqrt(f_i f_j) and r given by the\n# regression on the two signal correlations.\n#\n# Details the paper leaves open that bear on several claims, each with the readings named in\n# the claims that use it: (1) whether the reported rnoise values include the renormalization\n# in blocks of 20 trials described in the Methods (readings: without it, with it); (2) whether\n# the outlier rule removes z > 3 or |z| > 3, and whether a trial removed for one neuron is\n# removed for both (readings: |z| > 3 removing the trial for both neurons, z > 3 removing it\n# for both); (3) the form of the t tests (two-sample, two-sided Student or Welch).\nschema_version: 2\ndataset:\n  archive: crcns\n  id: stc-1\n  doi: 10.6080/K07P8WKF\npaper: doi:10.1016/j.neuron.2011.06.015\nclaims:\n- id: fig2b-trained-lower-noise-correlation\n  statement: Mean noise correlation among MSTd pairs (separated by less than 1 mm) is\n    significantly smaller in trained animals (0.023 +- 0.017 SEM, n = 89) than in naive animals\n    (0.116 +- 0.031, n = 38).\n  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 2;\n    Figure 2B\n  quote: The mean noise correlation in the trained group (0.023 ± 0.017 SEM, n = 89) was\n    significantly smaller than that for naive animals (0.116 ± 0.031, n = 38, p = 0.006, t test)\n  statistics:\n  - test: t test\n    p: 0.006\n    n: 89 trained and 38 naive pairs\n  expected:\n  - quantity: mean rnoise, trained animals\n    value: 0.023\n    tolerance: 0.017\n  - quantity: mean rnoise, naive animals\n    value: 0.116\n    tolerance: 0.031\n  - quantity: number of pairs, trained\n    value: 89\n    tolerance: 0\n  - quantity: number of pairs, naive\n    value: 38\n    tolerance: 0\n  criterion: rnoise per pair as in the Experimental Procedures (Noise and Signal Correlations),\n    pooled across headings and across the visual and vestibular conditions, for the 127 pairs\n    under 1 mm. Tolerances on the means are the reported SEMs. The paper names only \"t test\";\n    the readings are a two-sided two-sample Student t test and a Welch t test. Whether the\n    reported values include the renormalization in blocks of 20 trials is open; both readings\n    are run. Reproduced when, under one reading, the trained mean is below the naive mean with\n    p < 0.05 and both means are within tolerance; partially reproduced when the difference is\n    significant but a mean falls outside tolerance.\n- id: fig2c-timecourse-naive-higher\n  statement: Noise correlation is greater in naive than in trained animals throughout the time\n    course of the response, computed in 500 ms windows stepped by 50 ms (p = 0.002, permutation\n    test).\n  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 3;\n    Figure 2C\n  quote: rnoise was significantly greater in naive than trained animals throughout the time\n    course of the neural response (p = 0.002, permutation test, see Experimental Procedures)\n  statistics:\n  - test: permutation test\n    p: 0.002\n    n: 89 trained and 38 naive pairs\n  criterion: Needs spike times. rnoise per pair and window as for the main measure, in 500 ms\n    windows moved in 50 ms steps (31 windows), averaged per group; the permutation test of the\n    Experimental Procedures (sum of squared differences of the two group time courses, pairs\n    drawn at random from the pooled groups into groups of the original sizes, 10,000\n    permutations, p the proportion of permuted values above the observed one). Where the 31\n    windows sit relative to stimulus onset is not stated; the reading is windows starting at\n    stimulus onset and ending at its 2 s end (0-500 ms to 1500-2000 ms), which gives exactly\n    31. Reproduced when p < 0.05 and the naive mean is above the trained mean in every window;\n    partially reproduced when p < 0.05 and the naive mean is higher in most windows.\n- id: figs2a-difference-decreases\n  statement: The difference in rnoise between naive and trained animals is largest at the\n    beginning of the trial and decreases with time (Spearman R = -0.9, p << 0.001).\n  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 3;\n    Figure S2A\n  quote: The difference in rnoise between naive and trained animals was largest at the\n    beginning of the trial and gradually decreased with time\n  statistics:\n  - test: Spearman rank correlation\n    statistic: R = -0.9\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: Spearman R between window time and the naive minus trained rnoise difference\n    value: -0.9\n    tolerance: 0.09\n  depends_on:\n  - fig2c-timecourse-naive-higher\n  criterion: The 31 window differences (naive mean minus trained mean) of fig2c, correlated\n    with window time by Spearman rank correlation. Reproduced when R is within tolerance and p <\n    0.001; partially reproduced when R is negative with p < 0.05.\n- id: figs2b-individual-animals\n  statement: The greater noise correlation in naive animals holds for individual animals; four\n    trained animals (35, 26, 18 and 8 pairs) and three naive animals (22, 11 and 5 pairs) are\n    shown, and the difference is consistent across animals within each group.\n  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 3;\n    Figure S2B; Discussion, paragraph 1\n  quote: Importantly, these observations held true when correlations were examined for\n    individual animals\n  expected:\n  - quantity: pairs per trained animal shown (descending)\n    value: 35\n    tolerance: 0\n  - quantity: pairs per naive animal shown (descending)\n    value: 22\n    tolerance: 0\n  criterion: The paper shows per-animal time courses and gives no test, so the comparison is a\n    reading of the figure and the Discussion sentence that the difference \"was highly\n    significant and consistent across animals within each group\". Per animal, the mean rnoise\n    of its pairs (pooled measure, middle 1 s). Pair counts per animal are checked against 35,\n    26, 18, 8 (and 2, not shown) trained and 22, 11, 5 naive. Reproduced when every naive\n    animal's mean exceeds every trained animal's mean among the seven animals shown; partially\n    reproduced when every naive animal's mean exceeds the trained group mean. Time courses per\n    animal are shown when spike times are available.\n- id: fig1-example-pair\n  statement: For the example pair of Figure 1, signal correlation is 0.83 (visual) and 0.79\n    (vestibular), and noise correlation is 0.29 (visual, p = 0.04) and 0.14 (vestibular, p =\n    0.3).\n  source: Results, paragraphs 1 and 2; Figure 1B to 1E\n  quote: For this example pair of neurons, rsignal = 0.83 and 0.79 for the visual and\n    vestibular conditions, respectively ... (visual condition, rnoise = 0.29, p = 0.04, Figure\n    1D; vestibular condition, R = 0.14, p = 0.3, Figure 1E)\n  expected:\n  - quantity: rsignal, visual\n    value: 0.83\n    tolerance: 0.083\n  - quantity: rsignal, vestibular\n    value: 0.79\n    tolerance: 0.079\n  - quantity: rnoise, visual\n    value: 0.29\n    tolerance: 0.029\n  - quantity: rnoise, vestibular\n    value: 0.14\n    tolerance: 0.014\n  criterion: The paper does not identify the pair. Reproduced when one pair in the data has all\n    four values within tolerance; not reproduced when none does.\n- id: fig1f-modality-correlated\n  statement: Noise correlations computed from visual and vestibular responses are correlated\n    across pairs (R = 0.38, p << 0.001, Spearman rank correlation, 179 pairs).\n  source: Results, Noise Correlations in Area MSTd, paragraph 2; Figure 1F\n  quote: Noise correlations computed from visual and vestibular responses were significantly\n    correlated across 179 pairs of neurons (R = 0.38, p << 0.001, Spearman rank correlation)\n  statistics:\n  - test: Spearman rank correlation\n    statistic: R = 0.38\n    p: 0.001\n    p_relation: \"<\"\n    n: 179 pairs\n  expected:\n    quantity: Spearman R, visual against vestibular rnoise\n    value: 0.38\n    tolerance: 0.038\n  criterion: Per-condition rnoise (z-scores pooled across headings within one condition). The\n    paper's sample is all 179 pairs; the 127 pairs under 1 mm are the other reading, used when\n    only those are available, and the outcome then notes the smaller sample. Reproduced when R\n    is within tolerance and p < 0.001; partially reproduced when R > 0 with p < 0.05.\n- id: fig1f-modality-means-equal\n  statement: Mean noise correlation does not differ between the vestibular (0.035 +- 0.014 SEM)\n    and visual (0.039 +- 0.015) conditions (p > 0.8, paired t test).\n  source: Results, Noise Correlations in Area MSTd, paragraph 2; Figure 1F\n  quote: their means were not significantly different (vestibular, 0.035 ± 0.014 SEM, visual,\n    0.039 ± 0.015, p > 0.8, paired t test)\n  statistics:\n  - test: paired t test\n    p: 0.8\n    p_relation: \">\"\n    n: 179 pairs\n  expected:\n  - quantity: mean rnoise, vestibular\n    value: 0.035\n    tolerance: 0.014\n  - quantity: mean rnoise, visual\n    value: 0.039\n    tolerance: 0.015\n  criterion: A claim of absence, judged on the paper's test, a paired t test at p < 0.05 on the\n    per-condition rnoise of the 179 pairs (the 127 pairs under 1 mm when only those are\n    available, noted). Reproduced when the test finds no difference; the means and the\n    difference are reported either way.\n- id: figs1-distance\n  statement: Noise correlations depend on distance; mean rnoise is above zero for pairs under\n    0.05 mm (0.042 +- 0.021, p = 0.049, n = 67) and 0.05 to 1 mm (0.062 +- 0.024, p = 0.011, n =\n    60), but not for pairs over 1 mm (0 +- 0.15, p = 0.9, n = 52).\n  source: Results, Noise Correlations in Area MSTd, paragraph 3; Figure S1\n  quote: Average noise correlations were significantly greater than zero for the first two\n    groups (<0.05 mm, 0.042 ± 0.021 SEM, p = 0.049, t test; 0.05-1 mm, 0.062 ± 0.024, p =\n    0.011), but not for the group of distant pairs (>1 mm, 0 ± 0.15, p = 0.9)\n  statistics:\n  - about: pairs under 0.05 mm against zero\n    test: t test\n    p: 0.049\n    n: 67 pairs\n  - about: pairs 0.05 to 1 mm against zero\n    test: t test\n    p: 0.011\n    n: 60 pairs\n  - about: pairs over 1 mm against zero\n    test: t test\n    p: 0.9\n    n: 52 pairs\n  expected:\n  - quantity: mean rnoise, under 0.05 mm\n    value: 0.042\n    tolerance: 0.021\n  - quantity: mean rnoise, 0.05 to 1 mm\n    value: 0.062\n    tolerance: 0.024\n  - quantity: mean rnoise, over 1 mm\n    value: 0\n    tolerance: 0.15\n  criterion: Pooled rnoise, groups by estimated distance as in the Experimental Procedures\n    (single-electrode pairs set to 50 um, in the first group). One-sample t tests against zero\n    (two-sided). Reproduced when the first two means are within tolerance and above zero at p <\n    0.05 and the third is not different from zero at p < 0.05; partially reproduced when two of\n    the three groups match. Not testable if distances or the pairs over 1 mm are absent.\n- id: methods-single-vs-multiple-electrodes\n  statement: Noise correlations do not differ significantly between pairs recorded on one\n    electrode (0.042 +- 0.02) and on different electrodes (0.033 +- 0.015), p > 0.7, t test.\n  source: Experimental Procedures, Electrophysiological Recordings, paragraph 2\n  quote: noise correlations were slightly greater for pairs of neurons recorded from a single\n    electrode (0.042 ± 0.02) than for pairs recorded from different electrodes (0.033 ±\n    0.015), this difference was modest and not significant (p > 0.7, t test)\n  statistics:\n  - test: t test\n    p: 0.7\n    p_relation: \">\"\n    n: 67 single-electrode pairs and 112 multiple-electrode pairs\n  expected:\n  - quantity: mean rnoise, single electrode\n    value: 0.042\n    tolerance: 0.02\n  - quantity: mean rnoise, different electrodes\n    value: 0.033\n    tolerance: 0.015\n  criterion: A claim of absence, judged on a two-sample t test at p < 0.05 on pooled rnoise\n    over all 179 pairs (the sample is not stated; all pairs is the reading, and the pairs under\n    1 mm a variant). Reproduced when the test finds no difference; the means are reported\n    either way.\n- id: fig2a-behavioral-learning\n  statement: Heading discrimination thresholds of the five trained monkeys were high (over 10\n    degrees) early in training and decreased gradually to a plateau of 1 to 3 degrees.\n  source: Results, Comparison of Noise Correlations in Trained and Naive Animals, paragraph 1;\n    Figure 2A\n  quote: These monkeys' heading discrimination thresholds (corresponding to 84% correct) were\n    high ... at early stages of training, and gradually decreased to a plateau of only a few\n    degrees\n  expected:\n    quantity: plateau vestibular threshold\n    value: 2\n    tolerance: 1.3\n    unit: degrees\n  criterion: The range 1 to 3 degrees widened by 10% of each bound gives 0.9 to 3.3 degrees.\n    Reproduced when each animal's threshold falls from above 10 degrees early in training to a\n    plateau inside 0.9 to 3.3 degrees, the plateau read as the asymptote of an exponential fit\n    to threshold against session, as in the legend. Needs the training histories, which the\n    paper takes from earlier studies.\n- id: fig3-mean-response-unchanged\n  statement: The time course of the population average response to the preferred heading does\n    not differ between trained (n = 146 neurons) and naive (n = 64) animals (p = 0.8,\n    permutation test).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 1; Figures 3A and 3C\n  quote: the time course of the populationaverage response to the preferred heading was\n    indistinguishable between trained and naive animals (p = 0.8, permutation test\n  statistics:\n  - test: permutation test\n    p: 0.8\n    n: 146 trained and 64 naive neurons\n  criterion: A claim of absence, judged on the paper's permutation test (Experimental\n    Procedures, Permutation Test) at p < 0.05, on the mean firing rate at each cell's preferred\n    heading in the 31 windows, for the neurons of the 127 pairs. Needs spike times. Whether\n    the test was run per condition or on both together is open; the readings are a test per\n    condition (visual and vestibular, as in Figures 3A and 3C) and one test on both\n    concatenated. Reproduced when no reading's test finds a difference.\n- id: fig3-fano-unchanged\n  statement: Training has no significant effect on the time course of the Fano factor (p = 0.5,\n    permutation test).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 1; Figures 3B and 3D; Figure S3\n  quote: There was also no significant effect (p = 0.5, permutation test) of training on the\n    time course of the Fano factor\n  statistics:\n  - test: permutation test\n    p: 0.5\n  criterion: A claim of absence, judged on the paper's permutation test at p < 0.05. Fano\n    factor per window and group as 10^intercept of a type II regression of log variance on log\n    mean spike count with slope fixed at 1, values below 0.1 set to 0.1 (Experimental\n    Procedures, Fano Factor; Figure S3). Which mean and variance enter the fit (per neuron and\n    heading, or per neuron at the preferred heading) is open; per neuron and heading is the\n    reading, as in the scatter plots of Figure S3. Per condition and on both conditions, as for\n    fig3-mean-response-unchanged. Needs spike times. Reproduced when no reading's test finds a\n    difference.\n- id: fig4-tuning-width-visual\n  statement: Median visual tuning width does not differ between naive (124.5 degrees) and\n    trained (126 degrees) animals (p = 0.21, Wilcoxon rank-sum test).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 2; Figure 4A\n  quote: There was no significant difference in median tuning width for the visual condition\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.21\n    n: 992 visually tuned neurons\n  expected:\n  - quantity: median visual tuning width, naive\n    value: 124.5\n    tolerance: 12.45\n    unit: degrees\n  - quantity: median visual tuning width, trained\n    value: 126\n    tolerance: 12.6\n    unit: degrees\n  criterion: A claim of absence, judged on a Wilcoxon rank-sum test at p < 0.05 on full width\n    at half maximum, for neurons with significant tuning (one-way ANOVA p < 0.05) in the\n    single-electrode database. How width is measured from the sampled tuning curve\n    (interpolation) is not stated; linear interpolation of the tuning curve over the circle is\n    the reading. Reproduced when the test finds no difference and both medians are within\n    tolerance.\n- id: fig4-tuning-width-vestibular\n  statement: Median vestibular tuning width is slightly larger in trained (131 degrees) than in\n    naive (121 degrees) animals (p = 0.045).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 2; Figure 4E\n  quote: The difference in median tuning width was significant for the vestibular condition\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.045\n    n: 556 vestibularly tuned neurons\n  expected:\n  - quantity: median vestibular tuning width, naive\n    value: 121\n    tolerance: 12.1\n    unit: degrees\n  - quantity: median vestibular tuning width, trained\n    value: 131\n    tolerance: 13.1\n    unit: degrees\n  depends_on:\n  - fig4-tuning-width-visual\n  criterion: Measure and selection as in fig4-tuning-width-visual. Reproduced when the trained\n    median is larger with p < 0.05 and both medians are within tolerance.\n- id: fig4-amplitude-unchanged\n  statement: Training has no significant effect on tuning curve amplitude, visual (naive 35.4\n    against trained 31.8 spikes/s, p = 0.24) or vestibular (17.4 against 17.2 spikes/s, p =\n    0.36).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 2; Figures 4B and 4F\n  quote: training did not have any significant effect on the distribution of tuning curve\n    amplitudes in either the visual condition (naive, 35.4 spks/s versus trained, 31.8 spks/s,\n    p = 0.24, Wilcoxon rank-sum test) or the vestibular condition (naive, 17.4 spks/s versus\n    trained, 17.2 spks/s, p = 0.36)\n  statistics:\n  - about: visual\n    test: Wilcoxon rank-sum test\n    p: 0.24\n  - about: vestibular\n    test: Wilcoxon rank-sum test\n    p: 0.36\n  expected:\n  - quantity: median visual amplitude, naive\n    value: 35.4\n    tolerance: 3.54\n    unit: spikes/s\n  - quantity: median visual amplitude, trained\n    value: 31.8\n    tolerance: 3.18\n    unit: spikes/s\n  - quantity: median vestibular amplitude, naive\n    value: 17.4\n    tolerance: 1.74\n    unit: spikes/s\n  - quantity: median vestibular amplitude, trained\n    value: 17.2\n    tolerance: 1.72\n    unit: spikes/s\n  criterion: A claim of absence, judged on Wilcoxon rank-sum tests at p < 0.05 per condition, on\n    amplitude as peak minus trough of the mean tuning curve (Figure 4 legend), same neurons as\n    fig4-tuning-width-visual. The values are read as medians, as for tuning width; means are\n    shown as a variant. Reproduced when neither test finds a difference.\n- id: fig4dh-lateral-more-sensitive\n  statement: Neurons preferring lateral headings are more sensitive to heading variation around\n    straight ahead than neurons preferring fore-aft headings (p << 0.001, factorial ANOVA).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 3; Figures 4C, 4D, 4G and 4H\n  quote: lateral neurons were significantly more sensitive than fore-aft neurons for heading\n    discrimination around straight ahead (p << 0.001, Factorial ANOVA, Figures 4D and 4H)\n  statistics:\n  - test: factorial ANOVA, main effect of preference group\n    p: 0.001\n    p_relation: \"<\"\n    n: 992 visual and 556 vestibular neurons\n  criterion: Neuronal threshold per neuron from Fisher information on the interpolated tuning\n    curve at straight ahead (equation 2 for one neuron), with Poisson variance as in Figure S4\n    and Gu et al. 2010; how tuning curves are interpolated is not stated (readings, cubic\n    spline and linear interpolation). Fore-aft is a preference within 45 degrees of 0 or 180,\n    lateral within 45 degrees of -90 or 90. A factorial ANOVA on threshold with preference group\n    and training group, per condition; whether thresholds were log transformed is open (raw\n    and log are both run). Reproduced when lateral neurons have lower thresholds with p < 0.001\n    in both conditions under one reading.\n- id: fig4dh-training-no-sensitivity-change\n  statement: Neuronal sensitivity does not differ between naive and trained animals for either\n    fore-aft or lateral neurons (p > 0.5, factorial ANOVA), with no interaction (p > 0.3).\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 3; Figures 4D and 4H\n  quote: neuronal sensitivity was not significantly different between naive and trained animals\n    (p > 0.5, factorial ANOVA) for either group of neurons, with no significant interaction\n    effect (p > 0.3)\n  statistics:\n  - about: main effect of training\n    test: factorial ANOVA\n    p: 0.5\n    p_relation: \">\"\n  - about: interaction of training and preference group\n    test: factorial ANOVA\n    p: 0.3\n    p_relation: \">\"\n  depends_on:\n  - fig4dh-lateral-more-sensitive\n  criterion: A claim of absence, judged on the factorial ANOVA of fig4dh-lateral-more-sensitive\n    at p < 0.05 for the training effect and the interaction, per condition. Reproduced when\n    neither is significant in either condition; the group means are reported either way.\n- id: figs4-population-sensitivity-any-reference\n  statement: Population sensitivity computed from the single-electrode database does not differ\n    between naive and trained animals at any reference heading; the bootstrap 95% confidence\n    bands largely overlap.\n  source: Results, Effects of Training on Tuning Curves, Variability, and Sensitivity of Single\n    Neurons, paragraph 3; Figure S4\n  quote: Confidence intervals are largely overlapping between naïve (blue) and trained (pink)\n    animals\n  criterion: As in the Figure S4 legend, population threshold from equation 2 with independent\n    Poisson neurons, 95% bands from bootstrap resampling of 100 neurons with replacement, per\n    condition and group (visual 466 naive, 526 trained; vestibular 216 naive, 340 trained). The\n    number of bootstrap iterations and the reference headings sampled are not stated; 1,000\n    iterations and references every 22.5 degrees are standard choices. Reproduced when the\n    naive and trained bands overlap at every reference heading in both conditions; partially\n    reproduced when they overlap at most.\n- id: fig5-noise-signal-positive\n  statement: Noise correlation increases with signal correlation in both conditions (vestibular\n    p = 0.0001, visual p = 0.0004, ANCOVA).\n  source: Results, Training Effects on the Noise-Signal Correlation Structure, paragraph 1;\n    Figures 5A and 5B\n  quote: There was a significant positive correlation between rnoise and rsignal in both\n    stimulus conditions (vestibular, p = 0.0001; visual, p = 0.0004, ANCOVA)\n  statistics:\n  - about: vestibular rsignal\n    test: ANCOVA\n    p: 0.0001\n    n: 89 trained and 38 naive pairs\n  - about: visual rsignal\n    test: ANCOVA\n    p: 0.0004\n    n: 89 trained and 38 naive pairs\n  criterion: Per condition, an ANCOVA of rnoise on rsignal (continuous) and training group\n    (categorical) with their interaction, over the 127 pairs. Which rnoise enters is open; the\n    readings are the rnoise pooled across conditions (the measure the Results adopt before\n    Figure 5) and the rnoise of the same condition as rsignal. Reproduced when, under one\n    reading, the rsignal slope is positive with p < 0.05 in both conditions.\n- id: fig5-slope-unchanged\n  statement: Training does not change the slope of the relation between noise and signal\n    correlation (vestibular p = 0.9, visual p = 0.9, ANCOVA interaction).\n  source: Results, Training Effects on the Noise-Signal Correlation Structure, paragraph 2;\n    Figure 5C\n  quote: the slope of the relationship between rnoise and rsignal (Figures 5A and 5B) was not\n    significantly affected by training (vestibular, p = 0.9; visual, p = 0.9, ANCOVA interaction\n    effect)\n  statistics:\n  - about: vestibular\n    test: ANCOVA interaction effect\n    p: 0.9\n  - about: visual\n    test: ANCOVA interaction effect\n    p: 0.9\n  depends_on:\n  - fig5-noise-signal-positive\n  criterion: A claim of absence, judged on the interaction term of the ANCOVA of\n    fig5-noise-signal-positive at p < 0.05 in each condition, with the paper's pooled rnoise\n    as the measure; the same-condition rnoise is shown as a variant. Reproduced when neither\n    interaction is significant; the slopes and their 95% confidence intervals per group are\n    reported either way.\n- id: fig5-intercept-lower-trained\n  statement: Training lowers noise correlation uniformly across signal correlations, a main\n    effect of training (vestibular p = 0.02, visual p = 0.008, ANCOVA) with non-overlapping 95%\n    confidence intervals of the intercepts.\n  source: Results, Training Effects on the Noise-Signal Correlation Structure, paragraph 2;\n    Figure 5D\n  quote: training had a significant main effect on rnoise (vestibular, p = 0.02; visual; p =\n    0.008 ANCOVA), and the 95% confidence intervals around the regression intercepts were\n    non-overlapping for naive and trained animals\n  statistics:\n  - about: vestibular\n    test: ANCOVA main effect of training\n    p: 0.02\n  - about: visual\n    test: ANCOVA main effect of training\n    p: 0.008\n  depends_on:\n  - fig5-noise-signal-positive\n  criterion: The training main effect of the ANCOVA of fig5-noise-signal-positive, and the 95%\n    confidence intervals of the per-group regression intercepts. Readings for rnoise as in that\n    claim. Reproduced when, under one reading, the naive intercept is higher with p < 0.05 in\n    both conditions and the intervals do not overlap; partially reproduced when the main\n    effect holds but the intervals overlap.\n- id: fig5-regression-coefficients\n  statement: The plane fitted to noise and the two signal correlations is rnoise = 0.12\n    rsignal,vestibular + 0.091 rsignal,visual + 0.072 in naive animals, with the same slopes and\n    an intercept of 0.005 in trained animals.\n  source: Results, Computation of Covariance Matrix, paragraph 2; Experimental Procedures,\n    Population Coding, equation 5\n  inferred: Read from the equations of the Results, whose multiplication sign the extracted\n    text prints as \"3\"; no sentence states the values in words.\n  expected:\n  - quantity: slope on vestibular rsignal\n    value: 0.12\n    tolerance: 0.012\n  - quantity: slope on visual rsignal\n    value: 0.091\n    tolerance: 0.0091\n  - quantity: intercept, naive\n    value: 0.072\n    tolerance: 0.0072\n  - quantity: intercept, trained\n    value: 0.005\n    tolerance: 0.0005\n  depends_on:\n  - fig5-slope-unchanged\n  criterion: A plane fitted by type II regression (minimizing orthogonal distance, as in the\n    Experimental Procedures) of pooled rnoise on vestibular and visual rsignal. How slopes come\n    to be common to both groups is not stated; the readings are (a) one orthogonal fit to all\n    127 pairs with a separate intercept per group (rnoise centred per group before fitting the\n    slopes) and (b) the fit to all pairs for the slopes, with each group's intercept as its\n    mean of rnoise minus the slope terms. Ordinary least squares is shown as a variant. The\n    tolerance of 10% on the trained intercept of 0.005 is tighter than any estimate can be;\n    it is kept as the protocol default, and the 95% interval of the fitted intercept is\n    reported beside it. Reproduced when, under one reading, all four values are within\n    tolerance; partially reproduced when the slopes match and the naive intercept exceeds the\n    trained one.\n- id: fig6a-population-thresholds\n  statement: In simulated populations, correlated noise as measured in naive animals raises the\n    population threshold about 5-fold over independent noise at 2000 neurons, while the uniform\n    reduction in trained animals has little effect on the threshold compared with naive.\n  source: Results, Effect of Training on Population Coding Efficiency, paragraphs 1 and 2;\n    Figure 6A\n  quote: For a simulated population of 2000 neurons, the predicted heading discrimination\n    threshold was ... larger compared with the case of independent noise. Surprisingly, the\n    uniform reduction in rnoise that we observed in trained animals (Figure 5) had little effect\n    on predicted discrimination thresholds, as compared with naive animals\n  expected:\n    quantity: threshold ratio, naive structure against independent noise, 2000 neurons\n    value: 5\n    tolerance: 0.5\n  depends_on:\n  - fig5-regression-coefficients\n  criterion: Simulation from equations 2 to 5 with wrapped-Gaussian tuning (bandwidth 135\n    degrees), preferences uniform on the circle, congruent visual and vestibular tuning (so\n    the two signal correlations are equal), reference heading 0, and the paper's coefficients\n    (the coefficients fitted in fig5-regression-coefficients shown as a variant). Not stated:\n    the tuning amplitude and baseline, the counting window, the headings over which rsignal is\n    computed, and how bandwidth enters the wrapped Gaussian. The readings are amplitude 30\n    spikes/s on baseline 10 spikes/s over 1 s, rsignal over the 8 headings 45 degrees apart and\n    over a continuous circle, and bandwidth as full width at half height. The factor of about\n    5 is read from the extracted text, whose \"approximately\" sign is garbled. Reproduced\n    when, under one reading, the ratio is within tolerance and the trained threshold at 2000\n    neurons is within 10% of the naive one; partially reproduced when correlated noise raises\n    the naive threshold well above independent and trained and naive are within 10%, with the\n    ratio outside tolerance.\n- id: fig6b-slope-not-intercept\n  statement: Population thresholds (256 neurons) are very sensitive to the slope of the relation\n    between noise and signal correlation and only weakly sensitive to its intercept; a uniform\n    increase in rnoise lowers the threshold slightly.\n  source: Results, Effect of Training on Population Coding Efficiency, paragraph 2; Figure 6B\n  quote: predicted thresholds were very sensitive to changes in the slope of the relationship\n    between rnoise and rsignal. In contrast, changes in the intercept of the rnoise versus\n    rsignal relationship had weak effects on predicted thresholds\n  depends_on:\n  - fig6a-population-thresholds\n  criterion: The simulation of fig6a with 256 neurons, over a grid of slopes and intercepts\n    for which rnoise stays within -1 and 1 (the grid range is read from Figure 6B; slope 0 to\n    0.4 and intercept 0 to 0.2 are the reading). Reproduced when, under the fig6a readings, the\n    threshold changes more over the slope range than over an intercept range of the same\n    width, and threshold decreases as the intercept rises at the measured slopes.\n- id: fig7a-pair-sign-of-effect\n  statement: For a single pair of neurons, reducing noise correlation lowers the discrimination\n    threshold when signal correlation is positive and raises it when signal correlation is\n    negative.\n  source: Results, Effect of Training on Population Coding Efficiency, paragraph 3; Figure 7A;\n    Figure S7A\n  quote: reducing the noise correlation between this pair of neurons results in a lower\n    population threshold (red curve below blue curve) when the pair of neurons has positive\n    rsignal. In contrast, reducing noise correlation increases the predicted threshold for\n    negative rsignal\n  depends_on:\n  - fig6a-population-thresholds\n  criterion: Two-neuron simulation of equations 2 to 5 with the naive and trained coefficients,\n    one neuron preferring -90 degrees and the other's preference swept from -90 to 90, tuning as\n    in fig6a. Reproduced when the trained threshold is below the naive one for every pair with\n    positive rsignal and above it for every pair with negative rsignal.\n- id: fig7b-msdt-pairs\n  statement: Decoding real MSTd pairs, the ratio of thresholds with rnoise = 0.1 and rnoise = 0\n    rises above 1 for pairs with positive signal correlation and falls below 1 for negative\n    signal correlation (R = 0.49, p << 0.001, Spearman).\n  source: Results, Effect of Training on Population Coding Efficiency, paragraph 3; Figure 7B\n  quote: pairs of neurons with positive rsignal yield discrimination thresholds that increase\n    with rnoise, whereas pairs with negative rsignal have discrimination thresholds that\n    decrease with rnoise (R = 0.49, p << 0.001, Spearman rank correlation)\n  statistics:\n  - test: Spearman rank correlation\n    statistic: R = 0.49\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n    quantity: Spearman R, threshold ratio against rsignal\n    value: 0.49\n    tolerance: 0.049\n  criterion: Needs each pair's tuning curves. Per pair, threshold from equations 2 to 4 at\n    straight ahead with r = 0.1 and r = 0, from the pair's interpolated tuning curves; the ratio\n    correlated with rsignal by Spearman rank correlation. Open: which condition (readings,\n    visual and vestibular separately, and both pooled as two points per pair), which pairs\n    (the 127 under 1 mm, or all 179), and the interpolation (cubic spline, linear). Reproduced\n    when, under one reading, R is within tolerance and p < 0.001; partially reproduced when R >\n    0 with p < 0.05.\n- id: fig7c-narrow-preferences\n  statement: In a 256-neuron population, narrowing heading preferences to give more pairs with\n    positive signal correlation (49%, 75%, 94%) makes the weaker noise correlations of trained\n    animals improve coding, but at best the trained threshold is about 8% lower than the naive.\n  source: Results, Effect of Training on Population Coding Efficiency, paragraph 4; Figure 7C;\n    Figure S7B\n  quote: At best, however, the predicted population discrimination threshold for trained\n    animals is ... lower than for naive animals\n  expected:\n  - quantity: best reduction of trained threshold against naive\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  - quantity: positive rsignal, preferences in [-180, 180]\n    value: 49\n    tolerance: 4.9\n    unit: percent\n  - quantity: positive rsignal, preferences in [0, 180]\n    value: 75\n    tolerance: 7.5\n    unit: percent\n  - quantity: positive rsignal, preferences in [30, 150]\n    value: 94\n    tolerance: 9.4\n    unit: percent\n  depends_on:\n  - fig6a-population-thresholds\n  criterion: The simulation of fig6a with 256 neurons and preferences uniform in [-180, 180],\n    [0, 180] and [30, 150] degrees (Figure 7C legend), and narrower ranges around 90 as the\n    figure's axis runs. The value of 8% and the percentages are read from the extracted text.\n    Reproduced when, under one fig6a reading, the trained-over-naive improvement grows as the\n    range narrows, its maximum is within tolerance, and the three proportions are within\n    tolerance.\n- id: fig8ab-choice-probability-lateral\n  statement: Neurons preferring fore-aft headings have smaller choice probabilities than\n    neurons preferring lateral headings (p = 0.019, t test), and choice probability does not\n    differ between neurons preferring leftward and rightward headings (p = 0.11).\n  source: Results, Possible rsignal Distributions in Area MSTd, paragraphs 2 and 3; Figures 8A\n    and 8B\n  quote: neurons with a preference for fore-aft movement show significantly smaller choice\n    probabilities (p = 0.019, t test, Figures 8A and 8B) ... there was no significant difference\n    in average choice probability between neurons preferring leftward and rightward headings\n    (p = 0.11, t test)\n  statistics:\n  - about: fore-aft against lateral\n    test: t test\n    p: 0.019\n    n: 311 single-electrode recordings, vestibular and visual pooled\n  - about: leftward against rightward\n    test: t test\n    p: 0.11\n  criterion: Choice probabilities from the single-electrode database (n = 311, vestibular and\n    visual pooled), groups by preferred heading as in Figure 4 (fore-aft within 45 degrees of 0\n    or 180, lateral within 45 degrees of -90 or 90). Two-sample t tests. Reproduced when fore-aft\n    choice probabilities are smaller with p < 0.05 and the leftward and rightward means do not\n    differ at p < 0.05.\n- id: fig8cd-noise-not-preference\n  statement: Noise correlation does not depend significantly on heading preference (p = 0.2,\n    t test); lateral neurons have slightly smaller noise correlations than fore-aft neurons.\n  source: Results, Possible rsignal Distributions in Area MSTd, paragraph 3; Figures 8C and 8D\n  quote: there was no significant dependence of noise correlation on the heading preferences of\n    MSTd neurons (p = 0.2, t test)\n  statistics:\n  - test: t test\n    p: 0.2\n    n: 328 fixation and 55 discrimination-task points, each pair plotted at both neurons'\n      preferences\n  criterion: A claim of absence, judged on a t test at p < 0.05 of the noise correlation of\n    lateral against fore-aft neurons, each pair entered twice, at each neuron's preferred\n    heading (Figure 8C legend). The pairs are those of Figure 8C, recorded in trained animals\n    during fixation and discrimination; which pairs and which preference (visual or\n    vestibular) are not stated, and the readings are the trained pairs under 1 mm with visual\n    preference and with vestibular preference. Reproduced when no reading's test finds a\n    difference; the group means are reported either way.\n- id: figs5-congruency\n  statement: Noise correlation differs between naive and trained animals (p = 0.008) but is not\n    affected by the congruency of the two units (p > 0.5), with no interaction (p > 0.5),\n    two-way ANOVA; an ANCOVA finds no effect of congruency on the relation to signal\n    correlation.\n  source: Results, Training Effects on the Noise-Signal Correlation Structure, paragraph 3;\n    Figure S5\n  quote: While the average noise correlation was significantly different between 'naïve' (blue\n    bars) and 'trained' (red bars) animals (p=0.008, main effect of training, two-way ANOVA), it\n    was not significantly affected by the congruency of the two units in each pair (p>0.5, main\n    effect of congruency, two-way ANOVA)\n  statistics:\n  - about: main effect of training\n    test: two-way ANOVA\n    p: 0.008\n  - about: main effect of congruency\n    test: two-way ANOVA\n    p: 0.5\n    p_relation: \">\"\n  - about: interaction\n    test: two-way ANOVA\n    p: 0.5\n    p_relation: \">\"\n  - about: congruency in the ANCOVA with rsignal\n    test: ANCOVA\n    p: 0.6\n    p_relation: \">\"\n  criterion: Congruency index per neuron as the Pearson correlation of its visual and\n    vestibular tuning curves; pairs CC, OO or CO by the signs (Figure S5 legend). Two-way ANOVA\n    of pooled rnoise on training group and pair type, over the 127 pairs. Needs tuning curves.\n    Reproduced when the training effect has p < 0.05 and neither the congruency effect nor the\n    interaction has p < 0.05 (a claim of absence for these two, judged on this test).\n- id: figs6-task-independent\n  statement: For 41 pairs recorded in both tasks, noise correlations during fixation and\n    during heading discrimination are correlated (R = 0.47, p = 0.002) and their means do not\n    differ (p = 0.26, paired t test).\n  source: Results, Computation of Covariance Matrix, paragraph 2; Figure S6\n  quote: Noise correlations were significantly correlated across task conditions (R=0.47,\n    p=0.002, Spearman rank correlation) and the mean values were not significantly different\n    (p=0.26, paired t-test, n=41)\n  statistics:\n  - about: correlation across tasks\n    test: Spearman rank correlation\n    statistic: R = 0.47\n    p: 0.002\n    n: 41 pairs\n  - about: means\n    test: paired t-test\n    p: 0.26\n    n: 41 pairs\n  expected:\n    quantity: Spearman R, fixation against discrimination rnoise\n    value: 0.47\n    tolerance: 0.047\n  criterion: Needs rnoise from the discrimination task, computed alike (the headings of that\n    task differ; z-scoring per heading as in the Methods). The Results give p = 0.3 for the\n    same comparison. The difference of means is a claim of absence, judged on a paired t test\n    at p < 0.05. Reproduced when R is within tolerance with p < 0.05 and the paired test finds\n    no difference.\n- id: figs8c-renormalization\n  statement: Renormalizing responses in blocks of 20 trials has no significant effect on noise\n    correlations (R = 0.9 before against after), and the effect does not differ between naive\n    and trained animals (interaction p = 0.7, group p = 0.9, ANCOVA).\n  source: Experimental Procedures, Noise and Signal Correlations, paragraph 2; Figure S8C\n  quote: This additional normalization had no significant effect on rnoise (p > 0.3, paired t\n    test; R = 0.9, p < < 0.001, Spearman rank correlation, n = 127, Figure S8). More\n    importantly, the effect of renormalization on noise correlations was similar in naive and\n    trained animals (p = 0.7, interaction effect, p = 0.9, group effect, ANCOVA, Figure S8)\n  statistics:\n  - about: before against after, means\n    test: paired t test\n    p: 0.3\n    p_relation: \">\"\n    n: 127 pairs\n  - about: before against after, correlation\n    test: Spearman rank correlation\n    statistic: R = 0.9\n    p: 0.001\n    p_relation: \"<\"\n    n: 127 pairs\n  - about: interaction\n    test: ANCOVA\n    p: 0.7\n  - about: group effect\n    test: ANCOVA\n    p: 0.9\n  expected:\n    quantity: Spearman R, rnoise before against after renormalization\n    value: 0.9\n    tolerance: 0.09\n  criterion: Needs trial-ordered responses. Renormalization of the z-scores in consecutive\n    blocks of 20 trials (Zohary et al. 1994b); whether blocks run over all trials of the\n    session or within each condition is open, and both are run. The Figure S8C legend gives p\n    = 0.5 for the paired test. The ANCOVA is read as rnoise after renormalization on rnoise\n    before (covariate) and training group. The absence parts are judged on the paired t test\n    and the ANCOVA terms at p < 0.05. Reproduced when R is within tolerance and none of the\n    three tests finds an effect.\n- id: figs8ab-eye-movements\n  statement: Naive animals fixate as accurately as trained animals and make fewer microsaccades\n    (p << 0.001, t test).\n  source: Discussion, Possible Explanations for the Effect of Training on Correlated Noise,\n    paragraph 2; Figures S8A and S8B\n  quote: we found that naive animals fixate as accurately as trained animals (Figure S8A).\n    Indeed, naive monkeys as a group made significantly fewer microsaccades than trained\n    animals (Figure S8B)\n  statistics:\n  - test: t-test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Needs eye position records. Deviation from initial fixation position, averaged\n    over trials per animal in the middle 1 s; microsaccades as eye velocity peaks above 10\n    deg/s after smoothing with a 5 ms Gaussian (Figure S8 legend). The unit of the t test\n    (trials or time bins per animal) is not stated; the readings are per trial and per animal.\n    Reproduced when naive animals have fewer microsaccades with p < 0.05 under one reading and\n    the mean deviation of naive animals lies within the range of the trained animals.\n- id: discussion-stimulus-reduces-correlation\n  statement: Noise correlations decrease in the presence of the stimulus compared with\n    prestimulus baseline activity.\n  source: Discussion, Properties of Noise Correlations in MSTd, paragraph 2\n  quote: we observed that noise correlations decrease in the presence of a stimulus as compared\n    with prestimulus baseline activity\n  criterion: The paper shows no figure or test. Needs spike times. rnoise as for the main\n    measure in a prestimulus window against the middle 1 s of the stimulus; the prestimulus\n    window is not stated, and the reading is the fixation period before motion onset (100 to\n    200 ms, Experimental Procedures), with 500 ms before onset as a variant. Reproduced when\n    the mean prestimulus rnoise exceeds the stimulus rnoise by a paired t test at p < 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^[^#]*[^ ]: .*: " claims/crcns-stc-1/*.yaml; grep -n "^    [^ -].*: " claims/crcns-stc-1/*.yaml
```

```
83:    p: 0.006
84:    n: 89 trained and 38 naive pairs
87:    value: 0.023
88:    tolerance: 0.017
90:    value: 0.116
91:    tolerance: 0.031
93:    value: 89
94:    tolerance: 0
96:    value: 38
97:    tolerance: 0
116:    p: 0.002
117:    n: 89 trained and 38 naive pairs
136:    statistic: R = -0.9
137:    p: 0.001
138:    p_relation: "<"
140:    quantity: Spearman R between window time and the naive minus trained rnoise difference
141:    value: -0.9
142:    tolerance: 0.09
158:    value: 35
159:    tolerance: 0
[... 184 more lines not kept]
```

**Agent**

Fixing the two colon-space continuation lines (611, 671) and turning colons into periods there.

**Agent calls Bash**

```bash
cd claims/crcns-stc-1 && sed -i 's/shown as a variant). Not stated:/shown as a variant). Not stated are/; s/rank correlation. Open: which condition/rank correlation. Open are which condition/' 10.1016-j.neuron.2011.06.015.yaml && cd ../.. && python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml'
s=open(p).read()
rep={
"""  quote: For this example pair of neurons, rsignal = 0.83 and 0.79 for the visual and
    vestibular conditions, respectively ... (visual condition, rnoise = 0.29, p = 0.04, Figure
    1D; vestibular condition, R = 0.14, p = 0.3, Figure 1E)""":
"""  quote: For this example pair of neurons, rsignal = 0.83 and 0.79 for the visual and
    vestibular conditions, respectively ... rnoise = 0.29, p = 0.04, Figure 1D ... R = 0.14, p =
    0.3, Figure 1E""",
"""  quote: their means were not significantly different (vestibular, 0.035 ± 0.014 SEM, visual,
    0.039 ± 0.015, p > 0.8, paired t test)""":
"""  quote: their means were not significantly different (vestibular ... 0.035 ± 0.014 SEM, visual
    ... 0.039 ± 0.015, p > 0.8, paired t test)""",
"""  quote: Average noise correlations were significantly greater than zero for the first two
    groups (<0.05 mm, 0.042 ± 0.021 SEM, p = 0.049, t test; 0.05-1 mm, 0.062 ± 0.024, p =
    0.011), but not for the group of distant pairs (>1 mm, 0 ± 0.15, p = 0.9)""":
"""  quote: Average noise correlations were significantly greater than zero for the first two
    groups (<0.05 mm ... 0.042 ± 0.021 SEM, p = 0.049, t test; 0.05-1 mm ... 0.062 ± 0.024, p =
    0.011), but not for the group of distant pairs (>1 mm ... 0 ± 0.15, p = 0.9)""",
"""  quote: training did not have any significant effect on the distribution of tuning curve
    amplitudes in either the visual condition (naive, 35.4 spks/s versus trained, 31.8 spks/s,
    p = 0.24, Wilcoxon rank-sum test) or the vestibular condition (naive, 17.4 spks/s versus
    trained, 17.2 spks/s, p = 0.36)""":
"""  quote: training did not have any significant effect on the distribution of tuning curve
    amplitudes in either the visual condition (naive ... 35.4 spks/s versus trained ... 31.8
    spks/s, p = 0.24, Wilcoxon rank-sum test) or the vestibular condition (naive ... 17.4 spks/s
    versus trained ... 17.2 spks/s, p = 0.36)""",
"""    stimulus conditions (vestibular, p = 0.0001; visual, p = 0.0004, ANCOVA)""":
"""    stimulus conditions (vestibular ... p = 0.0001; visual ... p = 0.0004, ANCOVA)""",
"""    significantly affected by training (vestibular, p = 0.9; visual, p = 0.9, ANCOVA interaction
    effect)""":
"""    significantly affected by training (vestibular ... p = 0.9; visual ... p = 0.9, ANCOVA
    interaction effect)""",
"""  quote: training had a significant main effect on rnoise (vestibular, p = 0.02; visual; p =
    0.008 ANCOVA)""":
"""  quote: training had a significant main effect on rnoise (vestibular ... p = 0.02; visual; p =
    0.008 ANCOVA)""",
"""  quote: there was no significant dependence of noise correlation on the heading preferences of
    MSTd neurons (p = 0.2, t test)""":
"""  quote: there was no significant ... dependence of noise correlation on the heading
    preferences of MSTd neurons (p = 0.2, t test)""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/crcns-stc-1/*.yaml; grep -c "criterion:" claims/crcns-stc-1/*.yaml; git status --short
```

```
34
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
?? claims/crcns-stc-1/
?? scripts
```

**Agent**

I wrote the claims file at `claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml`. The quote checker reports 34 claims, 33 quotes, 39 statistical values and 0 problems. Nothing is committed.

**What I read.** The version of record (the journal PDF's text), with Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, plus the supplement (legends of Figures S1 to S8). The article says its supplement includes "Experimental Procedures and eight figures". The supplement as supplied lists only the eight figures on its contents page, so I took the article's Experimental Procedures as the whole Methods. The paper links no code, so none was read. I could not render the PDF, and the text garbles degree, minus and "approximately" signs; quotes avoid those places.

**Counts.**
- 34 claims, all of kind `finding`. 33 have quotes. One, `fig5-regression-coefficients`, is `inferred`, because the coefficients appear only in equations.
- 26 claims carry statistics, 39 values in all.
- All 34 have a criterion.

**Open details, with the readings named for each:**
- **Noise correlation measure:**
  - Whether the reported noise correlations include the renormalization in blocks of 20 trials: without it, or with it.
  - The outlier rule: |z| > 3 or z > 3, with the trial removed for both neurons.
  - The form of the t test: Student or Welch, two-sided.
- **Figure 2C:** where the 31 windows sit. The reading is from stimulus onset to the end of the stimulus.
- **Figure 3:** whether the permutation test was run per condition or on both together. For the Fano fit, which mean and variance enter; the reading is per neuron and heading.
- **Figure 5:** whether the noise correlation is pooled across conditions or taken from the same condition as the signal correlation. How the common-slope plane fit is formed (two readings). Ordinary least squares is shown as a variant.
- **Figure 4:** tuning-curve interpolation (linear or cubic spline), and raw or log thresholds in the ANOVA.
- **Simulations (Figures 6 and 7):** the paper does not give tuning amplitude, baseline, counting window, the headings used for signal correlation, or how bandwidth is defined. The readings are named as assumptions, and the Figure 6B grid range is read from the figure.
- **Figure 7B:** which condition, which pairs (127 or 179) and the interpolation.
- **Figure 8C:** which pairs, and visual or vestibular preference.
- **Smaller ones:** the sample for Figure 1F (179 pairs, or the 127 under 1 mm); the Figure S4 bootstrap count and reference grid (standard choices); renormalization blocks over the session or within each condition (Figure S8C); the unit of the eye-movement t test; the prestimulus window for the Discussion claim; and the identity of the Figure 1 example pair.
- **Per-animal consistency (Figure S2B):** the paper gives no test, so a reading is set.

**Missing from the paper:**
- Several reported p-values disagree between places: the Figure S6 test is p = 0.3 in the Results and p = 0.26 in the legend, and the renormalization test is p > 0.3 in the Methods and p = 0.5 in the Figure S8 legend. Both are recorded.
- The paper does not deposit the single-electrode database (Figure 4, S4, 8A/B), the training histories (2A) or the eye records (S8) anywhere else. The paper uses spike times, distances and tuning curves for several claims. The data descriptor lists only signal and noise correlations per condition and preferred headings for the 127 pairs, so the author will need to check whether the dataset holds more.
- The 10% tolerance on the trained intercept of 0.005 is tighter than any fit can reach. I kept it as the protocol default and asked for the fitted interval to be reported beside it.

## End of run

21 turns, 5 minutes, $1.64 at API prices, result: success.
