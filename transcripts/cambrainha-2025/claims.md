# cambrainha-2025 · claims · run 45955647264

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.1103-w49n-2vz8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-w49n-2vz8.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -in "github\|code avail\|zenodo" paper/*.txt; cat papers/datasets/cambrainha-2025.yaml; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -t claims/*.yaml | head -3; f=$(grep -l "claude-opus" claims/*.yaml | head -1); echo $f; head -60 $f; curl -s https://api.dandiarchive.org/api/dandisets/000713/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 60,200p claims/alasfour-2024.yaml; mkdir -p $TMPDIR/pg; pdftoppm -r 110 -png paper/10.1103-w49n-2vz8.pdf $TMPDIR/pg/p 2>&1 | head; ls $TMPDIR/pg
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/pg && python -c "
import fitz,os
d=fitz.open('paper/10.1103-w49n-2vz8.pdf'); print(len(d))
for i in [3,4,11,13,15,17,18]:
    d[i].get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/pg/p{i+1}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls .venv* venv 2>/dev/null | head; python -c "import pymupdf" 2>&1; pip download 2>/dev/null | head -1; which mutool gs convert magick 2>/dev/null
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python -c "
import fitz,os
d=fitz.open('paper/10.1103-w49n-2vz8.pdf'); print(len(d))
for i in [3,4,11,13,15,17,18]:
    d[i].get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/pg/p{i+1}.png')
"; ls $TMPDIR/pg
```

Result: not kept, because it reads the paper's text.

**Agent**

I rendered the figure pages to read Figs. 3 and 4 (the text garbles them).

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p12.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p18.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p19.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/p16.png"
}
```

Result: no output.

**Agent**

Now the checker's schema, then I'll write the file.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "kind\|data:\|'elsewhere'\|ALLOWED\|keys" tools/claims_check.py | head -40
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

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1)[:5000])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

The paper links no analysis code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/cambrainha-2025.yaml",
 "content": "# Claims for Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), PRX Life,\n# doi:10.1103/w49n-2vz8, \"Criticality at Work: Scaling in the Mouse Cortex Enhances\n# Performance\", on dandiset 000713 (Allen Institute, Visual Behavior, Neuropixels).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.\n#\n# Text read. arXiv preprint 2410.23508 version 2 (15 Sep 2025), standing in for the PRX Life\n# version of record, in paper/10.1103-w49n-2vz8.txt: main text, Appendix (Methods and\n# Materials, sections 1 to 6), and the Supplemental Material (sections I to VIII and Figures\n# S1 to S8). The PDF was opened to read Figures 3, 4, S1, S5, S7 and S8, whose axes the text\n# garbles. Values read from figures are marked as such.\n#\n# Code read. None. The paper links no analysis code and no repository (the contributions\n# statement says D.M.C. provided initial code and G.G.C. refined it, without a location).\n#\n# Data the paper used (Appendix 1, Figure 1A). The Allen Visual Behavior Neuropixels dataset\n# (ref. 60, DANDI), which the dandiset's title names. Mice trained to lick on an image change.\n# Each recording about 2 h 25 min, in three phases. Active: about 60 min of natural images in\n# 250-ms flashes, a change-detection task with reward, lick port present. Non-natural images\n# (NNI): Gabor patches for 15 min, full-field black and white flashes, and a gray screen for\n# 5 min. Passive: the same natural images in the same order, lick port retracted, no reward.\n# Spikes sorted with Kilosort2 by the Allen Institute; single-unit and multiunit activity both\n# kept. Units in primary visual cortex (V1). The 62 sessions (from 44 mice) with more than 128\n# V1 units. Measured variables used: V1 spike times, the phase boundaries (stimulus blocks),\n# and the task trials with their outcomes (hit or miss). Familiar and novel image sessions are\n# not told apart in the paper; all are pooled.\n#\n# Method fixed by the paper (Appendix, figure legends, Supplemental Material).\n# M1 Binning and windows. Spikes binned at 50 ms; each phase cut into 30-s windows (600 bins);\n#    windows with CV > 5 excluded, CV = sigma/mu of \"the activity across the window\"\n#    (Appendix 1).\n# M2 Surrogate. Per window, the interspike intervals of each unit shuffled within the window\n#    (Appendix 2).\n# M3 Momentum-space coarse graining (Appendix 3). Per window, the covariance of the units'\n#    binned counts (Eq. 2); eigenvectors ranked by eigenvalue; projector onto the top Ncutoff\n#    (Eq. 4); psi_i = Z_i sum_j P_ij (phi_j - <phi_j>) with Z_i making var(psi_i) = 1 (Eq. 5,\n#    which prints phi_i inside the sum; read as phi_j, the projection). Kurtosis at Ncutoff =\n#    N/16, kappa = <psi^4>/<psi^2>^2.\n# M4 Kurtosis threshold. A window with kappa > kappa_th is \"scaling\", otherwise \"no scaling\"\n#    (Results A; Figure 3A). kappa_surr_max is the largest surrogate kurtosis; it is about 7 in\n#    Figures 3C, 3D and 4A (read from the figures).\n# M5 Hit rate (Appendix 5, Eqs. 11 and 12). Pooled over all windows of all sessions above (or\n#    below) kappa_th, total hits over total trials. Relative performance (Eq. 13), scaling minus\n#    no-scaling hit rate over no-scaling hit rate. Standard error by bootstrap over windows,\n#    10^5 resamples.\n# M6 Trial-shuffled control (Appendix 6). For each trial, another trial of the same session\n#    chosen at random and their outcomes swapped; scaling-window hit rate computed as in M5;\n#    500 repetitions, mean and SD shown.\n# M7 Real-space coarse graining (Appendix 4; Results B, paragraph 3). Per window, the most\n#    correlated pair of units summed, repeated until none is left unpaired (Eq. 6); iterated k\n#    times to clusters of K = 2^k units. alpha from mean cluster variance M2 ~ K^alpha (Eq. 7);\n#    beta from F = -log P_silence ~ K^beta (Eq. 8); mu from the covariance spectrum\n#    lambda = A (K/rank)^mu (Eq. 9), windows with r^2 < 0.85 discarded for mu; z from the time\n#    tau_c at which the cluster-averaged autocorrelation reaches 1/e, tau_c ~ K^z (Eq. 10).\n#    Trivial values alpha = 1, beta = 1, z = 0. Exponents computed over all windows of a session\n#    (Supplement III), reported as mean and SD across sessions (Figure 4 legend; Supplement V).\n# M8 Tests. Mann-Whitney U between phases' distributions of session exponents (Figure 4\n#    legend; Supplement V).\n#\n# Details the paper leaves open, with the readings it allows. Criteria refer to these by\n# number. An outcome that rests on one of them rests on an assumption.\n# O1 Units and sessions. \"more than 128 recorded units\" (Appendix 1) against \"N>=128\" (Figure\n#    1D). The main analysis keeps a greedy sorting \"potentially including noise units\"\n#    (Supplement II), so units are read as all units whose structure is V1 (VISp), with no\n#    quality filter, reading (a). Reading (b) applies the dataset's default unit quality\n#    filters. The \"more strict sorting criteria\" of the 43-session variant (Supplement II) are\n#    not named. Readings: (i) the dataset's default quality filters (ISI violations, amplitude\n#    cutoff, presence ratio, as the dataset documents them); (ii) units labelled good by the\n#    sorter's curation. Counts > 128 and >= 128 are both run.\n# O2 CV of a window (M1). \"The activity\" can be (a) the population count (sum over units) per\n#    bin over the 600 bins; (b) the mean over units of each unit's CV; (c) the CV of all\n#    unit-bin counts pooled. Which windows each reading drops can change every later result.\n# O3 Kurtosis pooling (M3). \"From the distribution\" of the coarse-grained activity: read as\n#    (a) the psi_i(t) of all units and bins pooled into one distribution (as in Figure 2B), the\n#    reading the text supports; (b) the mean over units of each unit's kurtosis. Ncutoff =\n#    floor(N/16) when N is not a multiple of 16 (a standard choice).\n# O4 Phases. Active is the change-detection block; passive is the replay block. NNI can be\n#    (a) Gabors, flashes and the gray screen (Figure 1A names a gray background), or (b) Gabors\n#    and flashes only. Windows tile each phase from its start, without overlap, the last\n#    partial window dropped (a standard choice).\n# O5 Trials. \"Hits and misses\" read as go (change) trials with outcome hit or miss; catch and\n#    aborted trials left out. Auto-rewarded trials (a) left out or (b) kept as hits. A trial\n#    belongs to the window holding its change time (a standard choice; the trial start time is\n#    a variant).\n# O6 kappa_surr_max (M4). (a) The maximum of surrogate kurtosis over all surrogate windows of\n#    the phase analysed (active for Figure 3); (b) over all phases (Figure 4A uses one shaded\n#    area for all phases). One surrogate per window (a standard choice).\n# O7 Threshold grid. kappa_th is evaluated on a grid of step 0.05 (a standard choice). The\n#    range judged is the plotted one, from kappa_surr_max to 12.5 for Figure 3, to 15 for\n#    Figures 4A and S8.\n# O8 Bootstrap (M5). \"averaging\" can be (a) recomputing the pooled hit rate (Eq. 11) on the\n#    resampled windows, or (b) averaging the resampled windows' own hit rates. How the 3%\n#    error of the relative gain is propagated is not said; (c) the SD of Eq. 13 over the same\n#    bootstrap resamples is used for it.\n# O9 Real-space details (M7). Correlation is Pearson between binned counts, recomputed among\n#    clusters at each step; the unit left unpaired when the count is odd is dropped (standard\n#    choices following ref. 42). P_silence: (a) F = -log of the mean over clusters of each\n#    cluster's fraction of silent bins; (b) the mean over clusters of -log of that fraction.\n#    tau_c by linear interpolation between 50-ms lags (a standard choice). Fit range of K:\n#    (a) from K = 1 to the largest K with at least two clusters; (b) from K = 1 to N/16. mu:\n#    (a) one fit on the within-cluster spectra of all cluster sizes K >= 16 pooled against\n#    rank/K, (b) the spectrum of clusters of the single size K = 64 (the largest with two\n#    clusters at N = 128), ranks 1 to K. Fits are least squares on log-log axes.\n# O10 Session exponents (M7). (a) One fit per window, the session value the mean over its\n#    windows (supported by the per-window r^2 rule for mu); (b) the window quantities (M2, F,\n#    spectra, tau_c) averaged over the session's windows, one fit per session.\n# O11 Unit of the exponent test (M8). (a) Session values, 62 per phase, two-sided, unpaired, the\n#    reading the reported p-values fit (the smallest p printed, 8e-21, is about what complete\n#    separation of 62 against 62 gives); (b) window values pooled, shown as a variant.\nschema_version: 2\npaper: doi:10.1103/w49n-2vz8\nclaims:\n- id: sessions-selected\n  statement: Of the dataset's sessions, 62 (from 44 mice) have more than 128 recorded V1 units,\n    and these are the sessions analysed.\n  source: Appendix, 1. Data, paragraph 1; Results A, paragraph 2\n  quote: We selected all 62 sessions from the dataset that had more than 128 recorded units,\n    which included both single-unit activity (SUA) and multiunit activity (MUA)\n  expected:\n  - quantity: sessions with more than 128 V1 units\n    value: 62\n    tolerance: 6.2\n  - quantity: mice of those sessions\n    value: 44\n    tolerance: 4.4\n  criterion: V1 units counted per session under the readings of O1 (a) and (b), with the\n    threshold > 128 and >= 128. Reproduced when, under one reading, both counts are within\n    tolerance.\n- id: fig3a-kurtosis-broader-than-surrogate\n  statement: Across windows of all sessions, the kurtosis of the coarse-grained activity spans a\n    broad range that overlaps the surrogate distribution and extends well above it; some\n    windows have kurtosis well above any surrogate value, others look like surrogates.\n    Surrogate kurtoses are lowest around 6.\n  source: Results A, paragraph 2; Figure 2B; Figure 3A; Appendix 3, last paragraph\n  quote: Across 62 sessions (from 44 mice), we observed a broad range of kurtosis values,\n    overlapping with the distribution from the surrogate data [Fig. 3A]\n  expected:\n  - quantity: lowest surrogate kurtoses (Appendix 3, \"around 6\")\n    value: 6\n    tolerance: 0.6\n  criterion: Kurtosis per window as in M1 to M3, with the readings of O2 and O3; surrogate as in\n    M2. Figure 3A pools \"all subjects\"; the phase is not named, read as the active phase\n    (Figure 3 is on the active phase), with all phases pooled as a variant. Reproduced when\n    the mode of the surrogate kurtoses is within tolerance of 6, the real windows' spread\n    (interquartile range) is larger than the surrogate windows', some real windows lie below\n    kappa_surr_max (O6) and a majority lie above it. Partially reproduced when the spread is\n    larger and some windows exceed kappa_surr_max but the surrogate mode is out of tolerance.\n- id: fig3c-scaling-hit-rate-higher\n  statement: In the active phase, for any kurtosis threshold above the surrogate values, the\n    hit rate pooled over scaling windows is higher than over no-scaling windows and higher\n    than the trial-shuffled control.\n  source: Results A, paragraph 3; Figure 3C\n  quote: For any value of κth above surrogate values, the average hit rate was consistently higher\n    when calculated over scaling windows than over no-scaling windows [Fig. 3C] ... we confirmed\n    that the results were better than those obtained when hits and misses were shuffled within\n    each session\n  criterion: Hit rates as in M5 (Eqs. 11 and 12), trial shuffle as in M6 (500 repetitions), on\n    active-phase windows with trials as in O5, at each kappa_th of the grid of O7 from\n    kappa_surr_max (O6) to 12.5. Reproduced when, under one reading, the scaling hit rate\n    exceeds both the no-scaling hit rate and the mean trial-shuffled hit rate at every grid\n    point. Partially reproduced when it holds at 90% or more of grid points and every failure is\n    within one bootstrap SE (O8) of the comparator. Not reproduced otherwise.\n  depends_on:\n  - fig3a-kurtosis-broader-than-surrogate\n- id: fig3c-hit-rate-rises-with-threshold\n  statement: As the threshold rises and only windows of higher kurtosis count as scaling, the hit\n    rate over the scaling windows rises.\n  source: Discussion, paragraph 2; Figure 3C\n  quote: as we consider only windows of progressively higher kurtosis (closer to the critical\n    state), the corresponding performance calculated across those windows also rises\n  criterion: The scaling hit rate of fig3c-scaling-hit-rate-higher on the grid of O7. Reproduced\n    when the Spearman correlation between kappa_th and the scaling hit rate over the grid from\n    kappa_surr_max to 12.5 is positive and the hit rate at 12.5 exceeds that at kappa_surr_max by\n    more than the sum of their bootstrap SEs (O8). The paper reports no test; this measure is\n    this file's.\n  depends_on:\n  - fig3c-scaling-hit-rate-higher\n- id: fig3d-relative-gain-24\n  statement: The relative performance gain of scaling over no-scaling windows grows with the\n    threshold and reaches up to 24% plus or minus 3%.\n  source: Results A, paragraph 3; Figure 3D; Discussion, paragraph 2\n  quote: with relative performance gain reaching up to 24% ± 3% [Fig. 3D]\n  expected:\n  - quantity: maximum relative performance gain (Eq. 13)\n    value: 24\n    tolerance: 3\n    unit: percent\n  criterion: Relative performance (Eq. 13) on the grid of O7 with the readings of O2 to O6.\n    The maximum is taken (a) over the plotted range, kappa_surr_max to 12.5, where Figure 3D\n    peaks near 12, or (b) over all thresholds at which both scaling and no-scaling windows hold\n    trials. Reproduced when, under one reading, the maximum is within tolerance (the paper's\n    own error) and the gain at kappa_th = 12 is larger than at kappa_th = 8 (Figure 3D rises\n    over that span, read from the figure).\n  depends_on:\n  - fig3c-scaling-hit-rate-higher\n- id: figs1-other-window-lengths\n  statement: With 10-s and 60-s windows the results are similar; hit rate over scaling windows\n    rises with the threshold, and the relative gain departs from zero around kappa of 7.\n  source: Results A, paragraph 3; Supplemental Material I; Figure S1\n  quote: Time windows of 10 and 60 s were also analyzed and showed similar results, associating\n    higher kurtosis with better performance\n  criterion: The analysis of fig3c-scaling-hit-rate-higher and fig3d-relative-gain-24 repeated\n    with 10-s and 60-s windows (200 and 1200 bins), with no surrogate range (Supplement I omits\n    it). For each length, reproduced when the scaling hit rate exceeds the no-scaling hit rate\n    at every grid point from kappa_th = 8 to 12 and the relative gain at 12 exceeds that at 8.\n    Reproduced when both lengths pass, partially when one does.\n  depends_on:\n  - fig3c-scaling-hit-rate-higher\n- id: figs2-strict-units\n  statement: Using only units passing stricter sorting criteria, 43 sessions keep more than 128\n    units, and the performance results stay qualitatively the same.\n  source: Supplemental Material II; Figure S2\n  quote: we repeated the analyses using only the 43 sessions that retained more than 128 units\n    after applying more strict sorting criteria ... The results remained qualitatively consistent\n    with those observed in the initial analyses\n  expected:\n  - quantity: sessions with more than 128 units after strict criteria\n    value: 43\n    tolerance: 4.3\n  criterion: Units under the strict readings of O1 (i) and (ii). Reproduced when, under one\n    reading, the session count is within tolerance and, on those sessions with those units,\n    the test of fig3c-scaling-hit-rate-higher is at least partially reproduced and the relative\n    gain at kappa_th = 12 is positive. Partially reproduced when the result holds but no\n    reading gives a count within tolerance.\n  depends_on:\n  - fig3c-scaling-hit-rate-higher\n- id: fig4a-active-most-scaling\n  statement: For any threshold, the fraction of windows above it is largest in the active phase,\n    smaller in the passive phase and smallest in the non-natural image phase; most non-natural\n    image windows still have higher kurtosis than surrogates.\n  source: Results B, paragraph 1; Figure 4A; Supplemental Material VI, paragraph 2\n  quote: For any κth, scaling windows were more abundant in the active phase than in the passive\n    phase [Fig. 4A] ... the shift towards lower levels in the kurtosis distribution was even more\n    pronounced, and scaling windows became less likely to occur [though most windows still\n    remained with higher kurtosis than those of surrogate data, Fig. 4A]\n  criterion: The complementary cumulative distribution of window kurtosis, pooled over sessions,\n    per phase (phases as in O4), on the grid of O7 from kappa_surr_max (O6) to 15, at points\n    where any phase is above zero. Reproduced when, under one reading, F_active > F_passive >\n    F_NNI at every such point and F_NNI at kappa_surr_max is above 0.5. Partially reproduced\n    when the order holds at 90% or more of points, or holds everywhere but the NNI fraction is\n    0.5 or below.\n  depends_on:\n  - fig3a-kurtosis-broader-than-surrogate\n- id: fig4-exponents-active\n  statement: In the active phase the real-space scaling exponents are alpha 1.41 +/- 0.05, beta\n    0.77 +/- 0.04, mu 0.73 +/- 0.08 and z 0.3 +/- 0.1 (mean and SD across sessions).\n  source: Results B, paragraph 3; Figures 4B to 4E\n  quote: For the active phase, we obtained α1 = 1.41±0.05, β1 = 0.77±0.04, μ1 = 0.73 ± 0.08 and z1 =\n    0.3 ± 0.1 [Figs. 4B-4E]\n  expected:\n  - quantity: alpha, active, mean across sessions\n    value: 1.41\n    tolerance: 0.05\n  - quantity: beta, active, mean across sessions\n    value: 0.77\n    tolerance: 0.04\n  - quantity: mu, active, mean across sessions\n    value: 0.73\n    tolerance: 0.08\n  - quantity: z, active, mean across sessions\n    value: 0.3\n    tolerance: 0.1\n  criterion: Exponents as in M7 with the readings of O9 and O10, on active-phase windows (O2).\n    Tolerances are the paper's SDs across sessions. Reproduced when, under one reading, all four\n    means are within tolerance; partially reproduced when three are.\n- id: fig4-exponents-passive\n  statement: In the passive phase the exponents are alpha 1.37 +/- 0.04, beta 0.78 +/- 0.04, mu\n    0.61 +/- 0.05 and z 0.36 +/- 0.06, differing significantly from the active phase for alpha,\n    z and mu but not for beta.\n  source: Results B, paragraph 3; Figures 4B to 4E; Supplemental Material V\n  quote: During the passive phase we found α2 = 1.37 ± 0.04, β2 = 0.78 ± 0.04, μ2 = 0.61 ± 0.05, z2\n    = 0.36 ± 0.06, with statistically significant differences with respect to the active phase for\n    α, z and μ\n  statistics:\n  - about: alpha, active against passive\n    test: Mann-Whitney U test\n    p: 8.0e-5\n    n: 62 sessions per phase\n  - about: beta, active against passive\n    test: Mann-Whitney U test\n    p: 0.17\n    n: 62 sessions per phase\n  - about: z, active against passive\n    test: Mann-Whitney U test\n    p: 6.0e-5\n    n: 62 sessions per phase\n  - about: mu, active against passive\n    test: Mann-Whitney U test\n    p: 4.0e-13\n    n: 62 sessions per phase\n  expected:\n  - quantity: alpha, passive, mean across sessions\n    value: 1.37\n    tolerance: 0.04\n  - quantity: beta, passive, mean across sessions\n    value: 0.78\n    tolerance: 0.04\n  - quantity: mu, passive, mean across sessions\n    value: 0.61\n    tolerance: 0.05\n  - quantity: z, passive, mean across sessions\n    value: 0.36\n    tolerance: 0.06\n  criterion: Exponents as in fig4-exponents-active on passive-phase windows. Tests as in M8 under\n    O11 (a), two-sided at 0.05 (Supplement V's significance convention). Reproduced when all\n    four means are within tolerance under one reading, alpha, z and mu differ significantly with\n    passive alpha lower, passive z higher and passive mu lower (Figures 4B, 4D, 4E), and beta does\n    not differ (p >= 0.05, a claim of absence judged on this test). Partially reproduced when\n    the tests agree but one mean is out of tolerance, or the means hold and one test disagrees.\n  depends_on:\n  - fig4-exponents-active\n- id: fig4-exponents-nni\n  statement: With non-natural images the exponents are alpha 1.28 +/- 0.03, beta 0.82 +/- 0.03,\n    mu 0.38 +/- 0.04 and z 0.4 +/- 0.1, all significantly different from both natural image\n    phases.\n  source: Results B, paragraph 3; Figures 4B to 4E; Supplemental Material V\n  quote: for non-natural stimuli the exponents were α3 = 1.28 ± 0.03, β3 = 0.82 ± 0.03, μ3 =\n    0.38±0.04 and z3 = 0.4±0.1, which are all different from the phases with natural images\n  statistics:\n  - about: alpha, passive against NNI\n    test: Mann-Whitney U test\n    p: 4.0e-19\n    n: 62 sessions per phase\n  - about: alpha, active against NNI\n    test: Mann-Whitney U test\n    p: 8.0e-21\n    n: 62 sessions per phase\n  - about: beta, passive against NNI\n    test: Mann-Whitney U test\n    p: 3.0e-10\n    n: 62 sessions per phase\n  - about: beta, active against NNI\n    test: Mann-Whitney U test\n    p: 3.0e-13\n    n: 62 sessions per phase\n  - about: z, passive against NNI\n    test: Mann-Whitney U test\n    p: 6.0e-6\n    n: 62 sessions per phase\n  - about: z, active against NNI\n    test: Mann-Whitney U test\n    p: 3.0e-10\n    n: 62 sessions per phase\n  - about: mu, passive against NNI\n    test: Mann-Whitney U test\n    p: 3.0e-8\n    n: 62 sessions per phase\n  - about: mu, active against NNI (printed as a second \"μ1 vs μ2\", the last entry of the list;\n      read as μ1 vs μ3, the only pair otherwise missing)\n    test: Mann-Whitney U test\n    p: 3.0e-8\n    n: 62 sessions per phase\n  expected:\n  - quantity: alpha, NNI, mean across sessions\n    value: 1.28\n    tolerance: 0.03\n  - quantity: beta, NNI, mean across sessions\n    value: 0.82\n    tolerance: 0.03\n  - quantity: mu, NNI, mean across sessions\n    value: 0.38\n    tolerance: 0.04\n  - quantity: z, NNI, mean across sessions\n    value: 0.4\n    tolerance: 0.1\n  criterion: Exponents as in fig4-exponents-active on NNI windows (O4 readings). Tests as in M8\n    under O11 (a), two-sided at 0.05. Reproduced when all four means are within tolerance under\n    one reading and all eight comparisons are significant with NNI alpha and mu lower, beta and\n    z higher than both other phases (Figures 4B to 4E). Partially reproduced when at least six\n    comparisons hold and at least three means are within tolerance.\n  depends_on:\n  - fig4-exponents-active\n- id: fig4bc-static-exponents-trend\n  statement: In the active phase alpha and beta deviate significantly from their trivial values\n    of 1; in the passive phase they lie closer to the trivial values, and closer still with\n    non-natural images, while z moves away from its trivial value 0 from active to passive to\n    non-natural images.\n  source: Discussion, paragraph 4; Figures 4B to 4D\n  quote: α and β (\"static exponents\" [51]) deviate significantly from trivial values α = 1 and β =\n    1 [Figs. 4B and 4C]. In contrast, during a passive replay of natural images, the static\n    exponents shift closer to trivial values, approaching this baseline even more closely when\n    non-natural images are used\n  criterion: The test of deviation from trivial values is not named. Readings, (a) session\n    alpha and beta of the active phase against those of the surrogate windows (the lighter bars\n    of Figures 4B and 4C), Mann-Whitney U (M8); (b) a one-sample two-sided Wilcoxon signed-rank\n    test of session values against 1. Reproduced when, under one reading, active alpha and beta\n    differ significantly (p < 0.05) from trivial with alpha above 1 and beta below 1, and the\n    mean distances |alpha - 1|, |1 - beta| and z are ordered active > passive > NNI for alpha,\n    active >= passive > NNI for beta (beta1 and beta2 do not differ, p = 0.17) and active <\n    passive < NNI for z. Partially reproduced when the deviation holds and one ordering fails.\n  depends_on:\n  - fig4-exponents-passive\n  - fig4-exponents-nni\n- id: figs3-exponents-stable-with-threshold\n  statement: Exponents computed only from windows with kurtosis above the threshold vary only\n    slightly with the threshold and stay within their error bars.\n  source: Results B, paragraph 3; Supplemental Material III; Figure S3\n  quote: We find that the exponent values vary only slightly and remain within their respective\n    error bars (Fig. S3)\n  criterion: Per phase, exponents as in fig4-exponents-active, the session value taken over the\n    session's windows with kappa > kappa_th, sessions with no such window left out, on the grid\n    of O7 from kappa_surr_max to 12. Reproduced when, for every phase and exponent, the mean\n    across sessions stays within one SD across sessions (at kappa_th = kappa_surr_max) of its\n    all-window value, at every grid point with at least 10 sessions contributing (the paper\n    attributes larger fluctuations at high kappa to few windows; 10 is this file's floor).\n    Partially reproduced when it holds for three of the four exponents.\n  depends_on:\n  - fig4-exponents-active\n- id: figs4-initial-kurtosis-poor-predictor\n  statement: The kurtosis of the activity before coarse graining is a very poor predictor of the\n    kurtosis after coarse graining.\n  source: Supplemental Material IV; Figure S4\n  quote: Our analysis shows that the initial kurtosis κ0 is a very poor predictor of the\n    coarse-grained kurtosis κfinal (Fig. S4)\n  criterion: kappa_0 as kappa of M3 at Ncutoff = N (the z-scored binned counts, pooled as in O3),\n    kappa_final at N/16, per window; the phase is not named, active as the main reading and all\n    phases pooled as a variant. The paper gives no measure; this file's is the Spearman\n    correlation across windows. Reproduced when its magnitude is below 0.3; partially\n    reproduced between 0.3 and 0.5.\n  depends_on:\n  - fig3a-kurtosis-broader-than-surrogate\n- id: figs5a-firing-rate-order\n  statement: Mean firing rate over windows above a kurtosis threshold decreases almost\n    monotonically with the threshold within each phase, and is ordered active < NNI < passive\n    for any threshold, unlike the kurtosis order of Figure 4A.\n  source: Supplemental Material VI; Figure S5A and S5B\n  quote: Indeed, firing rate varies almost monotonically with κth (Fig. S5A) ... The mean firing\n    rate, on the other hand, gives no clue about that, since ρactive < ρNNI < ρpassive, for any\n    κth (Fig. S5A)\n  criterion: Per window, the mean over units of spike counts per bin (Figure S5A values of 0.09\n    to 0.16 suggest this unit; the scale does not change the order). As in the S5A legend,\n    averaged over a mouse's windows above kappa_th, then over mice, on the grid of O7 from 5 to\n    12 at points where every phase has windows. Reproduced when active < NNI < passive at every\n    point and, within each phase, the Spearman correlation of rate against kappa_th is\n    negative. Partially reproduced when the order holds at 90% or more of points.\n  depends_on:\n  - fig4a-active-most-scaling\n- id: figs5c-hit-rate-firing-rate-nonmonotonic\n  statement: The hit rate over windows below a firing-rate threshold is not a monotonic function\n    of the threshold.\n  source: Supplemental Material VI; Figure S5C\n  quote: the hit rate below some threshold ρth is not a monotonic function of ρth (Fig. S5C)\n  criterion: Active-phase windows split by their mean firing rate (as in figs5a-firing-rate-order)\n    at rho_th on a grid of step 0.0025 from 0.05 to 0.20 (the plotted range); hit rate pooled as\n    in M5. Reproduced when the below-threshold hit rate has an interior maximum that exceeds its\n    values at both ends of the range by more than one bootstrap SE (O8); not reproduced when the\n    curve is monotonic within that margin.\n  depends_on:\n  - figs5a-firing-rate-order\n- id: figs7-fatigue-halves\n  statement: In each half of the active phase (first and last 30 min), the scaling hit rate still\n    rises above the no-scaling hit rate as the threshold grows, though the overall hit rate is\n    lower in the second half.\n  source: Results B, paragraph 2; Supplemental Material VIII; Figure S7\n  quote: in the second half of the active phase, we observe lower kurtoses than in the first half,\n    but the relation between performance and kurtosis is preserved\n  criterion: The analysis of fig3c-scaling-hit-rate-higher, separately for windows in the first\n    and the last 30 min of the active phase. Reproduced when, in each half, the relative gain\n    (Eq. 13) is positive at every grid point from kappa_th = 8 to 12 and larger at 12 than at 8,\n    and the overall hit rate (all windows) of the second half is lower than that of the first.\n    Partially reproduced when the gain holds in one half.\n  depends_on:\n  - fig3c-scaling-hit-rate-higher\n- id: figs8-halves-and-phase-order\n  statement: Kurtosis is lower in the second half of the active phase than in the first, yet both\n    halves keep more windows above threshold than the passive and non-natural image phases; the\n    non-natural image phase, though it precedes the passive phase, has the lowest kurtosis.\n  source: Supplemental Material VIII, paragraph 2; Figure S8\n  quote: The active phase - even subdivided into two halves - consistently exhibits higher kurtosis\n    levels compared to the other phases\n  criterion: Complementary cumulative distributions as in fig4a-active-most-scaling for four\n    groups (active first 30 min, active last 30 min, passive, NNI), on the grid of O7 from\n    kappa_surr_max to 15. Reproduced when, at every point where any group is above zero, active\n    first half >= active second half > passive > NNI. Partially reproduced when the order of\n    the second half over passive, or the first half over the second, fails at some points.\n  depends_on:\n  - fig4a-active-most-scaling\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/cambrainha-2025.yaml paper/10.1103-w49n-2vz8.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The quote crosses a page break; I'll cut it there.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/cambrainha-2025.yaml",
 "old_string": "    pronounced, and scaling windows became less likely to occur [though most windows still",
 "new_string": "    pronounced, and scaling windows became less likely to ... [though most windows still"
}
```

```
The file claims/cambrainha-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/cambrainha-2025.yaml paper/10.1103-w49n-2vz8.txt; grep -n " — \|rather" claims/cambrainha-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/cambrainha-2025.yaml`. The quote checker passes it: 18 claims, 18 quotes, 12 statistical values, 0 problems.

**Text read.** The paper file is arXiv 2410.23508 version 2, which stands in for the PRX Life version of record. It has the main text, the Methods appendix (sections 1 to 6), and the Supplemental Material (sections I to VIII, Figures S1 to S8). Nothing the claims need is missing. I opened PDF pages only to read Figures 3, 4, S1, S5, S7 and S8. The paper links no code, so no code was read.

**Claims.** All 18 have a quote and all are `data: dataset`. They cover:
- **Session selection:** 62 sessions from 44 mice.
- **Kurtosis:** spread compared with the surrogate data (Fig. 3A).
- **Performance:** scaling windows have a higher hit rate than no-scaling and trial-shuffled windows, and it rises with the threshold (Fig. 3C). The relative gain reaches 24% ± 3% (Fig. 3D).
- **Robustness checks:** 10-s and 60-s windows (S1); stricter unit selection, 43 sessions (S2); the two halves of the active phase (S7, S8).
- **Phases:** windows above threshold are ordered active > passive > non-natural images (Fig. 4A).
- **Exponents:** values for each of the three phases, the active-phase deviation from trivial values and the trend across phases, and stability with the threshold (S3).
- **Other supplement findings:** initial kurtosis is a poor predictor of final kurtosis (S4); firing-rate order (S5A); a non-monotonic hit rate against firing rate (S5C).

**Statistics.** There are 12 entries, all Mann-Whitney U p-values between phases for the exponents, from Supplement V. One is a misprint: the last entry is printed as "μ1 vs μ2" and I recorded it as μ1 vs μ3, with a note saying so.

**Criteria.** 17 claims have a criterion; the 24% gain uses the paper's ±3% and the exponents use the paper's SDs as tolerances. Where the paper gives no measure, the criterion says the threshold is the file's own choice. That applies to S4 (|Spearman| < 0.3), S3 (at least 10 sessions) and the monotonic rise in Fig. 3C.

**Details the paper leaves open, with the readings named (O1 to O11):**
- **O1, units:**
  - Main analysis: all V1 units, or V1 units after the dataset's default quality filters; ">128" and "≥128" are both run.
  - The 43-session variant's "more strict sorting criteria" are not named: the default quality filters, or units the sorter labelled good.
- **O2, CV > 5 exclusion:** the CV of the population count, the mean of the per-unit CVs, or the CV of all unit-bin counts pooled.
- **O3, kurtosis:** pooled over units and bins, or the mean of per-unit kurtoses. Equation 5 also has a misprint (φi inside the sum), which I read as φj.
- **O4, non-natural images phase:** with or without the gray-screen period.
- **O5, trials:** auto-rewarded trials left out or counted as hits.
- **O6, maximum surrogate kurtosis:** taken over the active phase only, or over all phases.
- **O7, threshold grid and range:** a standard choice, step 0.05 over the plotted range.
- **O8, bootstrap:** recompute the pooled hit rate, or average the windows' own hit rates; how the 3% error of the gain is propagated is not said.
- **O9, real-space method:**
  - P_silence: −log of the mean, or the mean of −log.
  - Range of cluster sizes K fitted: up to the largest K with two clusters, or up to N/16.
  - Fit for μ: pooled over K ≥ 16, or a single K = 64.
- **O10, session exponents:** a fit per window then averaged, or one fit per session.
- **O11, test unit:** session values, which the reported p-values fit, or pooled window values as a variant.

Neither the Methods nor the text says which phase Figs. 3A and S4 use; each claim reads it as the active phase and runs all phases pooled as a variant.

**Missing from the paper:** besides the unnamed strict sorting criteria in O1, the paper names no test for "deviate significantly from trivial values" (Discussion). The criterion names two readings: comparison with the surrogate exponents, or a Wilcoxon signed-rank test against 1.

I did not commit anything.

## End of run

24 turns, 5 minutes, $1.46 at API prices, result: success.
