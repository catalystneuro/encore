# brudner-2026 · claims · run 43150684266

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,192p docs/protocol.md; ls -la paper/; ls claims/brudner* 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 69,130p docs/protocol.md
```

```
### 3. Write the claims file

Write `claims/<paper>.yaml`, one file for the paper, across all its datasets. Its opening comment
says which text was read (the version of record or a preprint version, and the
supplement), and describes the data the paper used: the subjects, sessions,
conditions and measured variables, as the paper reports them, so that the
author can find them in the dataset.

   - One claim per finding, at the level of a figure panel or a reported
     number when the full text is available. Cover the paper's main findings,
     including those the dataset cannot test.
   - `statement`: the finding in words. `source`: where the paper shows it,
     precise enough to find without searching: a figure panel, or a section
     and paragraph ("Results, Place fields, paragraph 3").
   - `quote`: the sentence at `source` that states the finding, copied word
     for word from the full text, cut with "..." where it runs long. It lets a
     reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; wc -l claims/fouke-2025.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,321p claims/fouke-2025.yaml; cat papers/datasets/brudner-2026.yaml; grep -n -A5 brudner papers/keys.yaml
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -30 paper/*.txt; grep -n -i "supplement\|SI Appendix\|Materials and Methods\|github\|zenodo\|^Fig" paper/*.txt | head -80; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and SI Appendix are all present. Reading the text now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "offset": 30,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "offset": 729,
 "limit": 460
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "offset": 1420,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Text, Methods and SI are complete. Now the linked code and the dandiset's description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/emonetlab/GradientMotionMultiplePlumes.git gm 2>&1 | tail -2; cd gm && git log -1 --format='%H %ad' && find . -path ./.git -prune -o -type f -print | head -100
```

```
effc7b0317f6d3b62136c2a07bcba3e80e778575 Tue Jul 14 11:26:50 2026 -0400
./environment.yml
./data/published_panel_tables/fig5f_s5_model_comparison_complex_plume.csv
./data/published_panel_tables/fig5f_s5_model_comparison_smooth_plume.csv
./data/published_panel_tables/fig5e_cue_beta_complex_plume.csv
./data/published_panel_tables/fig2_glm_summary.csv
./data/published_panel_tables/fig5e_cue_beta_smooth_plume.csv
./metadata/figures_1_3.json
./metadata/published_panel_params.json
./src/gradient_motion_panels/style.py
./src/gradient_motion_panels/summary_tables.py
./src/gradient_motion_panels/plume_fields.py
./src/gradient_motion_panels/plume_sources.py
./src/gradient_motion_panels/centerline_models.py
./src/gradient_motion_panels/figure3_models.py
./src/gradient_motion_panels/figure3_training.py
./src/gradient_motion_panels/__init__.py
./tests/test_figure3_training.py
./tests/test_published_behavior_panels.py
./tests/test_figures_1_3.py
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001871/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('draft_version',{}).get('name')); print(d.get('most_recent_published_version'))"; curl -s https://api.dandiarchive.org/api/dandisets/001871/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/gm; cat README.md REPRODUCE.md; cat metadata/published_panel_params.json; for f in data/published_panel_tables/*; do echo "== $f"; cat $f; done; cat config/published_plot_config.yml
```

````
# GradientMotionMultiplePlumes

Publication code for *Fly navigational responses to odor motion and gradient cues are tuned to plume statistics*).

The Figure 1 and 3 pipelines deliberately keep large movies and model checkpoints outside Git; their renderers consume compact, provenance-carrying NPZ summaries.

## Quick start

```bash
conda env create -f environment.yml
conda activate gradient_motion_multiple_plumes
pip install -e ".[figures123,test]"  # adds PyTorch for Figure 3 training/extraction
python scripts/render_published_figure2.py
python -m pytest -q
```

## Behavior-regression panels

The behavior source is [DANDI dandiset 001871, version 0.260630.1657](https://dandiarchive.org/dandiset/001871/0.260630.1657). Compact published tables are checked in, and `scripts/generate_published_summary_tables.py` can regenerate them from the archived behavior NWB files.

[... 236 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/gm; wc -l scripts/*.py src/gradient_motion_panels/*.py; cat scripts/generate_published_summary_tables.py
```

```
167 scripts/generate_figure1_summary.py
    98 scripts/generate_figure2_summary.py
   301 scripts/generate_figure3_summary.py
   127 scripts/generate_published_summary_tables.py
   345 scripts/plot_cue_beta_paper_panel.py
   226 scripts/plot_cue_dominance_paper_panel.py
   345 scripts/plot_total_differential_panels.py
   118 scripts/render_published_behavior_panels.py
   375 scripts/render_published_figure1.py
   295 scripts/render_published_figure2.py
   360 scripts/render_published_figure3.py
    81 scripts/render_published_figures_1_3.py
   218 scripts/train_figure3_models.py
     1 src/gradient_motion_panels/__init__.py
   211 src/gradient_motion_panels/centerline_models.py
   169 src/gradient_motion_panels/figure3_models.py
   838 src/gradient_motion_panels/figure3_training.py
   416 src/gradient_motion_panels/plume_fields.py
   128 src/gradient_motion_panels/plume_sources.py
   144 src/gradient_motion_panels/style.py
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gm; cat src/gradient_motion_panels/summary_tables.py
```

```
"""Generate published behavior-panel summary tables from archived raw behavior data."""

from __future__ import annotations

import json
import math
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.signal import butter, filtfilt


DANDI_ASSETS_API = "https://api.dandiarchive.org/api/dandisets/{dandiset_id}/versions/{version}/assets/?page_size=100"

BASE_PREDICTORS = ("odor_velocity", "spatial_gradient", "signal")
[... 552 more lines not kept]
```

**Agent**

The code fixes the Fig. 5 analysis in detail (and departs from the Methods in two places). Reading the Fig. 1 to 3 code next.

**Agent calls Bash**

```bash
cd $TMPDIR/gm; cat REPRODUCE_FIGURES_1_3.md; cat metadata/figures_1_3.json | head -150; cat scripts/generate_figure2_summary.py; cat src/gradient_motion_panels/centerline_models.py
```

````
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/afcd8a1a-cb56-4068-b479-017e1bdabc00/tool-results/bjgdj62mr.txt

Preview (first 2KB):
# Reproduce Figures 1--3

The publication renderers separate large/raw inputs from compact plotting summaries. Figure 2 is self-contained. Figures 1 and 3 first generate an NPZ summary, then render from it.

All fixed values and provenance notes live in [`metadata/figures_1_3.json`](metadata/figures_1_3.json). The source reference is preprint commit [`659d0c3`](https://github.com/ClarkLabCode/OdorMotionMLdev/commit/659d0c3c34a8ab0f05abd76b38756debd4ea9214).

## Environment

```bash
conda env create -f environment.yml
conda activate gradient_motion_multiple_plumes
pip install -e ".[figures123,test]"
```

PyTorch is needed to train Figure 3 models or extract summaries from checkpoints. Rendering existing summaries does not import PyTorch.

[... 25 more lines not kept]
````

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/afcd8a1a-cb56-4068-b479-017e1bdabc00/tool-results/bjgdj62mr.txt"
}
```

````
1	# Reproduce Figures 1--3
2	
3	The publication renderers separate large/raw inputs from compact plotting summaries. Figure 2 is self-contained. Figures 1 and 3 first generate an NPZ summary, then render from it.
4	
5	All fixed values and provenance notes live in [`metadata/figures_1_3.json`](metadata/figures_1_3.json). The source reference is preprint commit [`659d0c3`](https://github.com/ClarkLabCode/OdorMotionMLdev/commit/659d0c3c34a8ab0f05abd76b38756debd4ea9214).
6	
7	## Environment
8	
9	```bash
10	conda env create -f environment.yml
11	conda activate gradient_motion_multiple_plumes
12	pip install -e ".[figures123,test]"
13	```
14	
15	PyTorch is needed to train Figure 3 models or extract summaries from checkpoints. Rendering existing summaries does not import PyTorch.
16	
17	## Figure 1
18	
19	The implementation computes the crosswind centered difference `dI/dy`, the motion cue `-(dI/dy)(dI/dt)`, and per-pixel temporal mean/std maps. In the 1500-frame analysis window, gradient statistics use all 1500 frames and motion statistics use the 1498 frames with temporal neighbors. Whole-window maps use no spatial smoothing. Snapshot panels use Gaussian sigma 3 (plume) and 1.5 (cue maps). As in the notebook, a plume snapshot at frame `n` is paired with cue maps centered at frame `n+1` from the triplet `n:n+3`; both indices are recorded.
20	
[... 730 more lines not kept]
````

**Agent**

Now the figures whose values the text does not print (Figs. 2, 4, 5).

**Agent calls Bash**

```bash
cd  python3 -c "
import fitz
d=fitz.open('paper/10.1073-pnas.2608896123.pdf')
for p in (3,6,7):
    d[p].get_pixmap(dpi=130).save('$TMPDIR/p%d.png'%(p+1))
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm; ls .venv venv 2>/dev/null | head; for p in 4 7 8; do pdftoppm -f $p -l $p -r 110 -png paper/10.1073-pnas.2608896123.pdf $TMPDIR/p$p; done; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.pdf",
 "pages": "7-8"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -m pip list 2>/dev/null | grep -i -E "pdf|mupdf|pypdf|pdfplumber|pillow"; grep -n -i "pymupdf\|fitz" tools/*.py | head -3
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv pv >/dev/null && pv/bin/pip -q install pymupdf 2>&1 | tail -1; pv/bin/python -c "
import fitz
d=fitz.open('paper/10.1073-pnas.2608896123.pdf')
for p in (3,6,7):
    d[p].get_pixmap(dpi=120).save('$TMPDIR/p%d.png'%(p+1))
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent**

Figs. 4 and 5 read; their bar values match the code's published tables. Checking Fig. 2.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent**

Fig. 2 values match the code's table. Checking the code for the Fig. 1 and S1 measures.

**Agent calls Bash**

```bash
cd $TMPDIR/gm; grep -n -i "otsu\|antisym\|bias\|intermitt\|frequen\|zscore\|z_score\|std" src/gradient_motion_panels/plume_fields.py src/gradient_motion_panels/plume_sources.py scripts/generate_figure1_summary.py | head -40; sed -n 1,60p src/gradient_motion_panels/plume_fields.py
```

```
src/gradient_motion_panels/plume_fields.py:26:    "gradient_std",
src/gradient_motion_panels/plume_fields.py:28:    "motion_std",
src/gradient_motion_panels/plume_fields.py:40:    gradient_std: np.ndarray
src/gradient_motion_panels/plume_fields.py:42:    motion_std: np.ndarray
src/gradient_motion_panels/plume_fields.py:55:    def gradient_zscore(self) -> np.ndarray:
src/gradient_motion_panels/plume_fields.py:56:        return safe_standardized_mean(self.gradient_mean, self.gradient_std)
src/gradient_motion_panels/plume_fields.py:59:    def motion_zscore(self) -> np.ndarray:
src/gradient_motion_panels/plume_fields.py:60:        return safe_standardized_mean(self.motion_mean, self.motion_std)
src/gradient_motion_panels/plume_fields.py:171:def safe_standardized_mean(mean: np.ndarray, std: np.ndarray) -> np.ndarray:
src/gradient_motion_panels/plume_fields.py:172:    """Compute the notebook's per-pixel temporal mean/std ratio.
src/gradient_motion_panels/plume_fields.py:179:    std = np.asarray(std, dtype=np.float32)
src/gradient_motion_panels/plume_fields.py:180:    if mean.shape != std.shape:
src/gradient_motion_panels/plume_fields.py:182:    denominator = np.where(std == 0, 1.0, std)
src/gradient_motion_panels/plume_fields.py:281:    gradient_mean, gradient_std = moments_gradient.finish()
src/gradient_motion_panels/plume_fields.py:282:    motion_mean, motion_std = moments_motion.finish()
src/gradient_motion_panels/plume_fields.py:315:        gradient_std=gradient_std[sl],
src/gradient_motion_panels/plume_fields.py:317:        motion_std=motion_std[sl],
"""Figure 1 plume-gradient and motion-cue computations.

The functions in this module are a small, testable replacement for the
[... 58 more lines not kept]
```

**Agent**

The repo has no code for the S1 index. Checking how other claims files record outside data.

**Agent calls Bash**

```bash
cd  grep -l "data: elsewhere" claims/*.yaml | head -3; grep -h -A6 "data: elsewhere" claims/*.yaml | head -30; grep -h -o "^  [a-z_]*:" claims/*.yaml | sort | uniq -c | sort -rn | head -30; sed -n 1,40p tools/claims_check.py
```

```
claims/azcorra-2023.yaml
claims/berg-2020.yaml
claims/bouabid-2026.yaml
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  expected:
  - quantity: Nuclei after quality control
    value: 12065
    tolerance: 1206.5
  - quantity: Mean UMI count per nucleus
--
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  depends_on:
  - snrna-nuclei-qc
  criterion: Without clustering, from raw counts of the nuclei that pass quality control, a
    gene is detected with one or more UMI. Reproduced when (i) Anxa1 and Aldh1a1 detection
    are associated (Fisher exact test, odds ratio above 1, p < 0.05), (ii) more than half of
--
  data: elsewhere
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
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
[... 128 more lines not kept]
```

**Agent**

I have what I need from the code. Rendering two SI pages: the garbled upwind-turn formula and Fig. S5.

**Agent calls Bash**

```bash
cd $TMPDIR; pv/bin/python -W ignore -c "
import pymupdf as f
d=f.open('paper/10.1073-pnas.2608896123.supp-pnas.2608896123.sapp.pdf')
print(len(d))
d[3].get_pixmap(dpi=110, clip=f.Rect(0,300,612,792)).save('s4.png')
for i in range(len(d)):
    if 'Figure S5' in d[i].get_text() or 'Figure S4' in d[i].get_text(): print(i)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s4.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR; pv/bin/python -W ignore -c "
import pymupdf as f
d=f.open('paper/10.1073-pnas.2608896123.supp-pnas.2608896123.sapp.pdf')
d[13].get_pixmap(dpi=100).save('s14.png'); d[12].get_pixmap(dpi=90).save('s13.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s14.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent**

S5D/E log-likelihood levels differ from the code's checked-in tables, though Fig. 5F matches the tables. I'll record that. Checking the Fig. 3 probe code next.

**Agent calls Bash**

```bash
cd $TMPDIR/gm; grep -n -i "synthetic\|probe\|gradient_stim\|motion_stim\|shift\|separation\|sigmoid\|response\|log1p\|transform" scripts/generate_figure3_summary.py src/gradient_motion_panels/figure3_models.py | head -50
```

```
scripts/generate_figure3_summary.py:2:"""Extract Figure 3 filters and probe responses from compatible checkpoints."""
scripts/generate_figure3_summary.py:24:    gradient_probe,
scripts/generate_figure3_summary.py:25:    iter_motion_probes,
scripts/generate_figure3_summary.py:50:        "--minimal-smooth-probe",
scripts/generate_figure3_summary.py:53:        help="User-supplied R2 probe checkpoint.",
scripts/generate_figure3_summary.py:56:        "--minimal-complex-probe",
scripts/generate_figure3_summary.py:59:        help="User-supplied R2 probe checkpoint.",
scripts/generate_figure3_summary.py:152:        "minimal_smooth_probe": checkpoint_path(args.minimal_smooth_probe),
scripts/generate_figure3_summary.py:153:        "minimal_complex_probe": checkpoint_path(args.minimal_complex_probe),
scripts/generate_figure3_summary.py:167:    minimal_smooth_probe, _ = load_model(paths["minimal_smooth_probe"], "minimal")
scripts/generate_figure3_summary.py:168:    minimal_complex_probe, _ = load_model(paths["minimal_complex_probe"], "minimal")
scripts/generate_figure3_summary.py:172:    differences, gradient_samples = gradient_probe()
scripts/generate_figure3_summary.py:203:            minimal_smooth_probe,
scripts/generate_figure3_summary.py:209:            minimal_complex_probe,
scripts/generate_figure3_summary.py:222:    shifts: list[float] = []
scripts/generate_figure3_summary.py:229:    for shift, samples in iter_motion_probes(
scripts/generate_figure3_summary.py:232:        shifts.append(shift)
scripts/generate_figure3_summary.py:236:                    minimal_smooth_probe,
scripts/generate_figure3_summary.py:246:                    minimal_complex_probe,
scripts/generate_figure3_summary.py:267:    arrays["motion_shift_seconds"] = np.asarray(shifts, dtype=np.float32)
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gm; sed -n 60,105p src/gradient_motion_panels/figure3_models.py; sed -n 170,225p scripts/generate_figure3_summary.py
```

```
def forward_module(self, input_data: Any) -> Any:
            output = input_data.clone()
            # The final ReLU is intentional: it matches the archived model code.
            for layer in self.dense_layers:
                output = torch.relu(layer(output))
            return output

        def forward(self, input_data: Any) -> Any:
            direct = self.forward_module(input_data)
            flipped = torch.cat(
                (input_data[:, time_steps:], input_data[:, :time_steps]), dim=1
            )
            return direct - self.forward_module(flipped)

    return DenseNetwork()


def class_one_probability(logits: Any) -> np.ndarray:
    """Convert legacy two-logit output to class-one probability."""

[... 84 more lines not kept]
```

**Agent**

Checking a recent paper-first claims file for header format before writing.

**Agent calls Bash**

```bash
cd  head -40 claims/bech-2026.yaml; grep -n "where:" -A2 claims/bech-2026.yaml | head
```

```
# Claims for Bech, Dard, Lebert, Smith, Bisi, Renard, Crochet & Petersen, "Retrosplenial cortex
# enables context-dependent goal-directed sensorimotor transformation", eLife reviewed preprint
# doi:10.7554/eLife.109717, on dandiset 001847.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, under
# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data
# when these criteria were written; the reader saw only the dandiset's title and description.
#
# Text read: the eLife Reviewed Preprint, version 1 (30 December 2025, "Not revised"), full text as
# served by the publisher's HTML (paper/10.7554-elife.109717.txt): Results, figure legends,
# Discussion, Methods, "Quantification and data analysis" with its figure-specific methods, and the
# legends of the four figure supplements (Figure 1 to 4, figure supplement 1), which the text gives
# under "Supplemental information". No PDF was supplied. The figures themselves were not seen, so
# claims shown only in grid maps are tested on the sentences of the Results that describe them.
#
# Code read. The paper names a "behavior GUI repo", an "NWB converter repo" and an "NWB analysis
# repo" without addresses; the dandiset's description names the two analysis repositories, which
# name the paper and this dandiset (version 0.260610.1400) in their READMEs:
#   github.com/LSENS-BMI-EPFL/Bech_Dard_process_NWB at 212a63103528cdeafb6ebcf90a50235cd2290082
#     (2026-06-30), scripts main_analysis/figure1_analysis.py to figure4_analysis.py,
[... 20 more lines not kept]
```

**Agent**

Writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/brudner-2026.yaml",
 "content": "# Claims for Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark & Emonet, \"Fly navigational\n# responses exploit plume-specific odor motion and gradient cues\", PNAS 123(29) e2608896123 (2026),\n# doi:10.1073/pnas.2608896123, on dandiset 001871.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-12,\n# under docs/protocol.md version pilot-14 (Reader, steps 1 to 4). Nobody had analysed the dataset's\n# data when these criteria were written; the reader saw only the dandiset's title and description.\n#\n# Text read: the version of record (PDF supplied by a person, published 14 July 2026), as extracted\n# to paper/10.1073-pnas.2608896123.txt, with the SI Appendix (pnas.2608896123.sapp.pdf, appended to\n# the same text file): Supplementary Methods, the legends of Figures S1 to S5 and of Movies S1 and S2.\n# The main Methods section is a short summary that refers to the SI Appendix for every detail. PDF\n# pages were opened to read the bar heights of Figures 2, 4 and 5 and the panels of Figure S5, and\n# the upwind-turn formula of the SI agent simulations, which the text garbles. It reads\n# P_upwind = 1 / (1 + exp(-(-0.49 + 1.5 R sin^2 theta))).\n#\n# Code read. The paper links github.com/emonetlab/GradientMotionMultiplePlumes; read at commit\n# effc7b0317f6d3b62136c2a07bcba3e80e778575 (2026-07-14). It holds\n#   - the Fig. 5E, 5F and S5D-E analysis (src/gradient_motion_panels/summary_tables.py,\n#     scripts/generate_published_summary_tables.py, metadata/published_panel_params.json), written\n#     to run on the behavior NWB files of dandiset 001871 version 0.260630.1657, and the published\n#     panel tables it produced (data/published_panel_tables/fig5e_*.csv and fig5f_s5_*.csv);\n#   - the Fig. 1 cue maps (plume_fields.py, generate_figure1_summary.py), the Fig. 2 logistic models\n#     (centerline_models.py, generate_figure2_summary.py) with the plotted values hard-coded from the\n#     preprint notebook (data/published_panel_tables/fig2_glm_summary.csv), and a re-implementation of\n#     the Fig. 3 network training and probes (figure3_training.py, figure3_models.py), with\n#     REPRODUCE_FIGURES_1_3.md, which says the legacy training arrays, threshold masks and\n#     checkpoints of Figs. 2 and 3 were not deposited and names where the code and the SI disagree;\n#   - nothing for the agent simulations (Fig. 4, Fig. S4, Fig. S5F-H) or for Fig. S1.\n# Where the SI leaves a choice open and the code settles it, the criteria follow the code and say\n# so; where they disagree, the SI Methods give the main reading and the code a named variant.\n#\n# The data the paper used.\n#   Behavior (Fig. 5, Fig. S5A-E). Adult female Drosophila, Orco-GAL4 > 20XUAS-CsChrimson, all\n#   blinded by GMR-hid, starved 3 days and fed all-trans-retinal, run in cohorts of 10 to 30 flies\n#   from one vial in a 270 x 170 x 10 mm arena with 100 mm/s laminar air, filmed at 60 fps under IR.\n#   A projector delivered to-scale movies of the smooth or the complex plume (2 min trials, 1 min\n#   rest, 8 trials per cohort, projection flipped across the centerline between trials); each cohort\n#   saw one plume type only. Tracked with SLEAP; per fly trajectory, position, heading, velocity and\n#   the gradient, motion and intensity signals at the antennae; saccade-like turn events. The paper\n#   reports no count of cohorts, flies, trajectories or turns. The code selects the behavior files\n#   by path, smooth files containing \"nagel-smoke\" and complex files containing \"smoke-2a\".\n#   Plume movies (Figs. 1 to 4, Fig. S1). The complex plume is a 60 Hz smoke movie (smoke_1a_orig),\n#   frames 300 to 1799 used, 1088 x 1728 pixels of 0.153 mm, centerline at row 590; the dandiset\n#   holds that 1500-frame window. The smooth plume is from Alvarez-Salvado et al. 2018 (Connor et al.\n#   2018 measurements), Dryad doi:10.5061/dryad.g27mq71, file 10302017_10cms_bounded_2.h5, dataset\n#   /dataset2, 15 Hz, which the paper rescaled to the complex plume's time and space resolution\n#   (1088 x 1696, centerline at row 544); it is not in the dandiset. Three freestream plumes (Connor\n#   et al. 2018; 5, 10 and 20 cm/s per the dandiset's description) are in the dandiset as 1500-frame\n#   windows, with a compact asset of the Fig. S1 freestream panel inputs.\n#   The paper also deposited plume recordings, behavioral tracking data and processed datasets in\n#   the Yale Dataverse, doi:10.60600/YU/590UBV (ref. 83).\n#\n# Missing from the paper and its code, as needed by claims below. The agent simulation code\n# (Fig. 4, Fig. S4, Fig. S5F-H) and the trained networks; the training and test arrays of Figs. 2\n# and 3 and the threshold that defined the valid sampling regions; the code of Fig. S1; the numbers\n# of flies, trajectories and turns behind Fig. 5. The log-likelihood levels plotted in Fig. S5D and\n# S5E (about -0.596 and -0.685 for the full models) differ from the code's published table\n# (-0.576 and -0.676), while the cue dominance of Fig. 5F matches the table.\nschema_version: 2\npaper: doi:10.1073/pnas.2608896123\nclaims:\n- id: fig1eh-snapshot-organization\n  statement: In single snapshots, the crosswind gradient feature has opposite signs on the two sides\n    of the centerline in the smooth plume but not in the complex plume, while the motion feature is\n    organized antisymmetrically in the complex plume but not in the smooth plume.\n  source: Results, Directional Odor Features Have Plume-Specific, Antisymmetric Organization Around\n    the Centerline, paragraph 2; Figure 1E to 1H\n  quote: In the smooth plume, the gradient feature had opposite signs on opposite sides of the\n    centerline while in the complex plume, it did not exhibit this antisymmetric organization across\n    the centerline ... In summary, the gradient and motion features exhibited complementary\n    distributions, with each organized antisymmetrically around the centerline in one plume type but\n    not the other\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71 (10302017_10cms_bounded_2.h5); complex\n    plume in the dandiset\n  criterion: Shown on one snapshot per plume and judged by eye in the paper; no measure is given.\n    The features are the crosswind centered difference dI/dy and -(dI/dy)(dI/dt) with centered\n    one-frame differences (Results, paragraph 2, and the code's plume_fields.py). The code's\n    snapshot frames are 601 (smooth) and 2900 (complex), cue maps centered one frame later, with\n    Gaussian smoothing of sigma 1.5 pixels for the cue panels; complex frame 2900 lies outside the\n    deposited window (code, REPRODUCE_FIGURES_1_3.md), so the complex snapshot cannot be the\n    published one. The claim is reported as a description of frames of the analysed window, and its\n    outcome is that of fig1il-zscore-reliability and figs1-antisymmetry-index, which test the same\n    organization on time averages.\n  depends_on:\n  - fig1il-zscore-reliability\n- id: fig1il-zscore-reliability\n  statement: Averaged over time and divided by its SD at each location, the gradient feature has\n    higher z-scores in the smooth plume than in the complex plume, and the motion feature has higher\n    z-scores in the complex plume than in the smooth plume.\n  source: Results, Directional Odor Features Have Plume-Specific, Antisymmetric Organization Around\n    the Centerline, paragraph 3; Figure 1I to 1L\n  quote: However, the odor gradients have higher z-scores in the smooth plume than in the complex\n    one, while the odor motion has higher z-scores in the complex plume than in the smooth one\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71 (10302017_10cms_bounded_2.h5, /dataset2);\n    complex plume in the dandiset\n  criterion: Per pixel, the temporal mean of each feature divided by its temporal SD (Results,\n    paragraph 3; the code's safe_standardized_mean, which divides by 1 where the SD is 0). Gradient is\n    the crosswind centered difference dI/dy over all 1500 frames, motion -(dI/dy)(dI/dt) with\n    centered one-frame differences over the 1498 frames with both neighbours, no spatial smoothing\n    (code, metadata/figures_1_3.json). Complex frames 300 to 1799, the dandiset's window, used as\n    stored (the code says they are already on a 0 to 255 scale; the z-score does not depend on the\n    intensity scale). Smooth plume resampled from 15 Hz to 60 Hz and to the 0.153 mm grid (SI, Plume\n    movies), frames 300 to 1799; the code keeps two timing profiles, notebook_legacy and corrected,\n    and both are run. How the maps are compared is not stated (the paper shows them). Readings,\n    (a) mean absolute z-score over the pixels of the Otsu plume mask of the SI (Plume movies);\n    (b) mean absolute z-score over the whole analysed frame; (c) the 95th percentile of the absolute\n    z-score over the mask. Reproduced when the smooth gradient value exceeds the complex one and the\n    complex motion value exceeds the smooth one; the outcome is the one all readings give.\n- id: figs1-antisymmetry-index\n  statement: The cue antisymmetry index (log ratio of motion to gradient antisymmetric organization)\n    increases monotonically with wind speed across the freestream plumes; the smooth plume lies near\n    the low end of that range and the complex plume has the highest index.\n  source: Figure S1, column v, legend; Results, Directional Odor Features Have Plume-Specific,\n    Antisymmetric Organization Around the Centerline, paragraph 1\n  quote: Across the freestream plumes the index increases monotonically with wind speed. The smooth\n    plume index falls near the low end of this range and the complex plume index is the highest\n    measured\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; freestream and complex plumes in the\n    dandiset\n  criterion: As the SI (Plume movies) defines it. For each plume and cue, the time-averaged map M\n    (Fig. S1 columns iii and iv, computed as in fig1il-zscore-reliability), its antisymmetric\n    component A(x, y) = M(x, y) - M(x, -y) about the centerline, the score s as the mean of |A| over\n    the Otsu mask, and the index log2(s_motion / s_gradient) (the legend's log2 scale bar). The\n    Otsu mask is Otsu's method on the mean intensity map with a morphology radius of 9 pixels and a\n    bias of 55 (48 for the complex plume). Open, with readings named. What the bias does is not\n    stated, (a) subtracted from the Otsu threshold in 0 to 255 intensity units, (b) a percentage of\n    the Otsu threshold; the morphology operation is taken as a binary opening then closing with a\n    disk of radius 9 (a standard choice). Intensity rescaling to the 1st and 99th percentiles is\n    stated for the freestream plumes; the index is not invariant to intensity scale, so readings\n    (i) all five movies rescaled to 0 to 1 between their 1st and 99th percentiles, (ii) only the\n    three freestream movies so rescaled, smooth and complex as used elsewhere. Freestream movies are\n    interpolated to 60 Hz as the smooth one (SI). Reproduced when the index rises from 5 to 10 to\n    20 cm/s, the smooth index lies below the 10 cm/s value, and the complex index is the highest of\n    the five; the outcome is the one all readings give.\n- id: figs1-temporal-statistics\n  statement: The smooth plume has odor encounter frequency and intermittency like the slow\n    freestream plumes; the fast freestream plume has lower intermittency and higher frequency; the\n    complex plume has the highest encounter frequencies.\n  source: Figure S1, column ii, legend\n  quote: The distribution of frequency and intermittency values at slow freestream speeds was similar\n    to the distribution of values in the smooth plume. In the fast freestream plume, intermittency\n    was relatively lower and frequency relatively higher. In the complex plume we observed the\n    highest arrival frequencies\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; freestream and complex plumes in the\n    dandiset\n  criterion: Per pixel, intensities binarized at 40% of that pixel's maximum; frequency is the rate\n    of onsets in the binary series and intermittency the fraction of time above threshold, within\n    the Otsu mask of figs1-antisymmetry-index (SI, Plume movies). The distributions are compared by\n    eye in the paper; here by their medians over masked pixels. Reproduced when the complex plume\n    has the highest median frequency of the five, the 20 cm/s freestream plume has a higher median\n    frequency and lower median intermittency than the 5 cm/s plume, and the smooth plume's medians\n    lie within the span of the 5 and 10 cm/s plumes widened by 10% of each bound.\n- id: figs1fg-resolution-robustness\n  statement: The spatial organization of the gradient and motion cues in the complex plume stays\n    consistent when sensor spacing is increased from 3 to 12 pixels or the motion delay is lengthened,\n    changing only when sampled more coarsely than the smooth plume.\n  source: Results, Directional Odor Features Have Plume-Specific, Antisymmetric Organization Around\n    the Centerline, paragraph 3; Discussion, paragraph 2; Figure S1F and S1G\n  quote: Relatedly, the complex plume's cue organization was robust to reduced sampling resolution,\n    only changing when sampled more coarsely than the smooth plume\n  criterion: Pearson correlation between time-averaged crosswind cue maps of the complex plume\n    (Fig. S1F, G legend), gradient over sensor spacings of 3 to 12 pixels, motion over the same\n    spacings and delays of 1, 2, 4, 8 and 15 frames. Open, with readings named. The reference map,\n    (a) the 3-pixel, 1-frame map, (b) the map at the previous spacing. The legend gives the delays as\n    33 to 500 ms, which is 30 Hz, while the movie is 60 Hz (17 to 250 ms) and the Discussion says 17\n    to about 150 ms; delays are run in frames. No threshold for consistent is given, readings\n    r >= 0.5 and r >= 0.8. Reproduced when the correlations stay at or above the threshold up to 12\n    pixels and 8 frames; the outcome is the one all readings give, and every correlation is\n    reported.\n- id: fig2b-smooth-auc\n  statement: In the smooth plume, a logistic model on the odor gradient feature predicts the side of\n    the centerline better (ROC AUC about 0.85) than one on the motion feature (about 0.54), and the\n    odor sum has no predictive power (AUC 0.5).\n  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 2; Figure 2B; SI\n    Figure S2A\n  quote: Models that used odor gradient to predict the smooth plume centerline direction had higher\n    AUCs than models that used odor motion for the same task ... In both plume conditions, the\n    bilateral sum ROC AUC values were 0.5\n  data: elsewhere\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; the paper's training and test arrays were\n    not deposited (code, REPRODUCE_FIGURES_1_3.md)\n  expected:\n  - quantity: test AUC, gradient only, smooth plume\n    value: 0.846\n    tolerance: 0.008\n  - quantity: test AUC, motion only, smooth plume\n    value: 0.541\n    tolerance: 0.003\n  - quantity: test AUC, sum only, smooth plume\n    value: 0.5\n    tolerance: 0.05\n  criterion: Values are the bar heights of Fig. 2B as hard-coded in the code's fig2_glm_summary.csv,\n    with tolerances the SD over 100 repeats from that table (0 for the sum, so the default 10%).\n    Samples per SI (Plume movies, Logistic regression models) and code (centerline_models.py). 1000\n    locations drawn uniformly in regions whose averaged intensity passes a threshold, two antennae 3\n    pixels apart facing upwind, each antenna's signal filtered by a 2D Gaussian of SD 1.5 pixels,\n    30-frame (0.5 s) histories, label the side of the centerline (row 544); 2,400,000 training and\n    600,000 test samples per repeat, 100 repeats. Code, nan_to_num then log(1 + max(I - 5, 0)),\n    features 0.5 mean(R + L), mean(R - L) and the delay-1 correlation, standardized with training\n    statistics, unpenalized logistic regression; test AUC. Open, with readings named. The region\n    threshold, (a) mean intensity above 5, the code's noise floor, (b) the Otsu mask of the SI. How\n    the samples are drawn from 1000 locations and split, (a) random windows split at random,\n    (b) split by location. Reproduced when gradient AUC exceeds motion AUC, the sum AUC is within\n    tolerance, and the gradient and motion AUCs are within tolerance under one reading; partially\n    reproduced when the ordering and the sum hold but the values do not.\n- id: fig2c-complex-auc\n  statement: In the complex plume, a logistic model on the odor motion feature predicts the side of\n    the centerline better (ROC AUC about 0.62) than one on the gradient feature (about 0.54), and\n    the odor sum has no predictive power.\n  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 2; Figure 2C; SI\n    Figure S2B\n  quote: In the complex plume, the opposite was true, so that odor motion was more predictive than\n    odor gradients in determining the centerline direction ... In both plume conditions, the\n    bilateral sum ROC AUC values were 0.5\n  expected:\n  - quantity: test AUC, motion only, complex plume\n    value: 0.618\n    tolerance: 0.005\n  - quantity: test AUC, gradient only, complex plume\n    value: 0.537\n    tolerance: 0.012\n  - quantity: test AUC, sum only, complex plume\n    value: 0.5\n    tolerance: 0.05\n  criterion: As fig2b-smooth-auc, on the dandiset's complex plume window (frames 300 to 1799, the\n    frames the SI uses), centerline at row 590, values and SDs from the code's fig2_glm_summary.csv\n    (the code notes the plotted complex error bars were hard-coded and differ from the SDs of its\n    result arrays). Reproduced when motion AUC exceeds gradient AUC, the sum is within tolerance and\n    the two AUCs are within tolerance under one reading; partially reproduced when the ordering and\n    the sum hold but the values do not.\n- id: figs2c-one-frame-delay\n  statement: In both plumes, the motion feature with a one-frame delay gives higher ROC AUC than\n    motion features with longer delays.\n  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 2; SI Figure S2C\n  quote: In both plume types, odor motion features with one-frame delays had higher ROC AUC values\n    than motion features using longer delays\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; complex plume in the dandiset\n  criterion: Motion-only models of fig2b-smooth-auc and fig2c-complex-auc refitted with delays tau\n    of 1 to 15 frames (SI, Logistic regression models). Reproduced when, in each plume, the mean test\n    AUC at tau = 1 exceeds that at every tau from 2 to 15; partially reproduced in one plume only.\n- id: fig2d-smooth-weights\n  statement: Fitted on all three z-scored features together in the smooth plume, the logistic model\n    gives the gradient a much larger weight (about 2.6) than motion (about 0.06), and the sum a\n    weight of 0; the combined model reaches a test AUC of 0.847.\n  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 3; Figure 2D; SI\n    Figure S2D\n  quote: The model trained in the smooth plume learned a larger weight for the odor gradient feature\n    than for the odor motion feature ... In both plumes, the weights for the odor sum feature were 0,\n    as expected\n  data: elsewhere\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71\n  expected:\n  - quantity: gradient weight, smooth plume\n    value: 2.614\n    tolerance: 0.184\n  - quantity: motion weight, smooth plume\n    value: 0.061\n    tolerance: 0.006\n  - quantity: combined-model test AUC, smooth plume\n    value: 0.847\n    tolerance: 0.085\n  criterion: As fig2b-smooth-auc, one logistic model on the three standardized features (code,\n    centerline_models.py). Weights and SDs from the code's fig2_glm_summary.csv (Fig. 2D bars); AUC\n    from the Fig. S2D legend with the default 10%. Weights are compared in absolute value, as their\n    signs depend on the left and right convention (the code uses R - L, opposite to the formula\n    printed in the paper). Reproduced when |gradient| exceeds |motion|, |sum| is below 0.01 and the\n    values are within tolerance under one reading; partially reproduced when the ordering holds\n    only.\n- id: fig2e-complex-weights\n  statement: Fitted on all three features together in the complex plume, the logistic model gives\n    motion a larger weight (about 0.40) than the gradient (about 0.10), and the sum a weight of 0;\n    the combined model reaches a test AUC of 0.612.\n  source: Results, Plume-Specific Features Predict Centerline Direction, paragraph 3; Figure 2E; SI\n    Figure S2D\n  quote: Conversely, the model trained in the complex plume learned a larger weight for the odor\n    motion feature than for the odor gradient feature ... In both plumes, the weights for the odor\n    sum feature were 0, as expected\n  expected:\n  - quantity: motion weight, complex plume\n    value: 0.403\n    tolerance: 0.034\n  - quantity: gradient weight, complex plume\n    value: 0.098\n    tolerance: 0.041\n  - quantity: combined-model test AUC, complex plume\n    value: 0.612\n    tolerance: 0.061\n  criterion: As fig2d-smooth-weights, on the dandiset's complex plume window. Reproduced when\n    |motion| exceeds |gradient|, |sum| is below 0.01 and the values are within tolerance under one\n    reading; partially reproduced when the ordering holds only.\n- id: fig3bc-mnm-filters\n  statement: A minimal opponent network trained to find the centerline learns gradient-detector\n    filters (opposite signs on the two antennae) in the smooth plume, and in the complex plume\n    filters with a delayed negative lobe in f1 like a motion detector; test AUCs are 0.726 (smooth)\n    and 0.517 (complex).\n  source: Results, Optimized Bilateral Computation for Centerline-Finding Recovers Plume-Specific Odor\n    Features, paragraph 3; Figure 3B and 3C; SI Figure S3D and S3E\n  quote: For models trained in the smooth plume, the filters acted like a gradient detector ... The\n    opposite signs of the filters suggest that they are also sensitive to gradients, but the\n    delayed, negative lobe in\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; complex plume in the dandiset; the\n    paper's training arrays and checkpoints were not deposited\n  expected:\n  - quantity: MNM test AUC, smooth plume\n    value: 0.726\n    tolerance: 0.073\n  - quantity: MNM test AUC, complex plume\n    value: 0.517\n    tolerance: 0.052\n  criterion: Training samples as fig2b-smooth-auc but with heading under a Wiener process whose RMS\n    change over 0.5 s is pi, facing upwind at the last sample (SI, Plume movies); MNM\n    sigma[ReLU(f1*L + f2*R + b) - ReLU(f1*R + f2*L + b)] with 30-sample filters, cross-entropy (SI,\n    Artificial neural network model); inputs log(1 + max(I - 5, 0)) (code). The SI gives learning\n    rate 1e-4 (printed garbled), batch 500 and 500 epochs; the code's archived-source profile used\n    300 epochs, batch 100 and 1e-5 for the MNM; the SI values are the main reading and the code's\n    the variant. Filter shapes are judged as the paper describes them. Reproduced when the smooth\n    filters have opposite signs over the last 0.1 s with similar time courses, the complex f1 has a\n    negative lobe that follows its positive peak within the last 0.1 s (Fig. S3D), and both AUCs are\n    within tolerance; partially reproduced when the shapes hold and an AUC does not.\n- id: fig3d-mnm-gradient-response\n  statement: The minimal network trained in the smooth plume responds more strongly to synthetic\n    gradient signals than the one trained in the complex plume.\n  source: Results, Optimized Bilateral Computation for Centerline-Finding Recovers Plume-Specific Odor\n    Features, paragraph 4; Figure 3D\n  quote: The model trained in the smooth plume responded more strongly to the gradient signals than\n    the model trained in the complex plume\n  data: with_inputs\n  where: as fig3bc-mnm-filters\n  depends_on:\n  - fig3bc-mnm-filters\n  criterion: Gradient probes are constant left and right signals with difference -0.5 to 0.5 and\n    mean 0.25 (SI, Testing trained models; code gradient_probe, 11 values); response is the model's\n    output probability (code). The code used a second trained MNM (R2) for the probe panels. How\n    response strength is compared is not stated, readings (a) the slope of the response against the\n    difference by least squares, (b) the mean of |response - 0.5| over the probes. Reproduced when\n    the smooth model's value exceeds the complex model's under both readings.\n- id: fig3e-mnm-motion-response\n  statement: Minimal networks trained in either plume respond strongly to synthetic motion signals,\n    and the smooth-trained model's motion response disappears when its filters are made exactly\n    symmetric.\n  source: Results, Optimized Bilateral Computation for Centerline-Finding Recovers Plume-Specific Odor\n    Features, paragraph 4; Figure 3E; SI Figure S3H\n  quote: Interestingly, the models trained in the complex and smooth plumes both responded strongly\n    to the motion signals with various delays ... Responses to the motion signals disappear if\n    exactly symmetrical filters are used\n  data: with_inputs\n  where: as fig3bc-mnm-filters\n  depends_on:\n  - fig3bc-mnm-filters\n  criterion: Motion probes are random binary left signals and a right signal shifted by -6 to 6\n    frames (SI, Testing trained models); response is the output probability averaged over 100,000\n    samples per shift (code iter_motion_probes). Symmetrized filters are not defined; read as\n    f1 and f2 replaced by their mean over the two antennae with opposite signs kept (so that the\n    model is a pure difference detector), a reading, with the average of the time-reversed pair\n    shown as a variant. No threshold for strongly is given. Reproduced when, for both models, the\n    responses at positive and negative shifts lie on opposite sides of 0.5 and the response to the\n    smooth model with symmetrized filters stays within 0.01 of 0.5 at every shift.\n- id: fig3ij-dnm-specialization\n  statement: Dense networks are more specialized than minimal ones; the smooth-trained dense network\n    is more sensitive to gradient signals and the complex-trained one responds more strongly to\n    motion signals; dense networks perform modestly better than the minimal ones (test AUC 0.735\n    smooth, 0.543 complex).\n  source: Results, Optimized Bilateral Computation for Centerline-Finding Recovers Plume-Specific Odor\n    Features, paragraphs 5 and 6; Figure 3I and 3J; SI Figure S3K\n  quote: When tested on the gradient signals, the model trained in the smooth plume was more\n    sensitive to gradient signals compared to the model trained in the complex plume ... the DNM\n    trained in the complex plumes responded more strongly to the motion signals than the one trained\n    in the smooth plumes\n  data: with_inputs\n  where: as fig3bc-mnm-filters\n  expected:\n  - quantity: DNM test AUC, smooth plume\n    value: 0.735\n    tolerance: 0.074\n  - quantity: DNM test AUC, complex plume\n    value: 0.543\n    tolerance: 0.054\n  criterion: Dense network of two hidden layers of 20 units on the 60 concatenated inputs, opponent\n    structure (output minus output on the swapped inputs, code), trained as fig3bc-mnm-filters (SI\n    values main; the code's archived dense profile, 500 epochs, batch 500, learning rate 1e-5 smooth\n    and 1e-4 complex, a variant). Probes and the two readings of response strength as\n    fig3d-mnm-gradient-response, and for motion (a) the mean over shifts of |response - 0.5|,\n    (b) the difference between the mean responses at shifts +1 and -1. Reproduced when the smooth\n    DNM's gradient sensitivity exceeds the complex DNM's, the complex DNM's motion response exceeds\n    the smooth DNM's under both readings, and the AUCs are within tolerance; partially reproduced\n    when the sensitivities hold and an AUC does not.\n- id: fig4ef-agent-success\n  statement: Navigating agents that add a centerline-predicting dense network to a wind-only strategy\n    find the source more often than wind-only agents when the network was trained in the plume they\n    navigate, and less often when it was trained in the other plume; the wind-only agents perform\n    similarly in the two plumes.\n  source: Results, Sensitivity to Plume-Appropriate Directional Features Enhances Agent Navigation,\n    paragraphs 2 to 4; Figure 4E and 4F\n  quote: In the smooth-plume, agents using the augmented strategy with the smooth plume-trained dense\n    network significantly outperformed agents using the wind-only strategy ... However, agents using\n    the augmented strategy with plume-inappropriate computations ... performed worse than agents\n    using the wind-only strategy\n  statistics:\n  - about: every pairwise comparison of success rate within each plume\n    test: z-test of proportions\n    p: 0.001\n    p_relation: \"<\"\n    n: 10,000 trajectories per condition\n  data: with_inputs\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; complex plume in the dandiset; the\n    simulation code and trained networks are not in the paper's repository\n  depends_on:\n  - fig3ij-dnm-specialization\n  expected:\n  - quantity: success rate, smooth plume, wind only\n    value: 0.176\n    tolerance: 0.018\n  - quantity: success rate, smooth plume, smooth-trained network\n    value: 0.195\n    tolerance: 0.020\n  - quantity: success rate, smooth plume, complex-trained network\n    value: 0.153\n    tolerance: 0.015\n  - quantity: success rate, complex plume, wind only\n    value: 0.187\n    tolerance: 0.019\n  - quantity: success rate, complex plume, smooth-trained network\n    value: 0.117\n    tolerance: 0.012\n  - quantity: success rate, complex plume, complex-trained network\n    value: 0.22\n    tolerance: 0.022\n  criterion: Values read from the bar heights of Fig. 4E and 4F (no sentence states them), default\n    tolerance. Agents per SI (Agent simulations). Start uniformly in a box 200 to 250 mm downwind of\n    the source with random heading; 10 mm/s forward at each movie step; turns by a Poisson process at\n    4/3 Hz, magnitude normal with mean 30 and SD 8 degrees; antennae 306 um apart; reflecting walls\n    at x = 270, y = 160 and y = 0 mm, x = 0 terminates; success on entering a 10 mm circle at\n    (0, 85) smooth or (0, 90) complex within 90 s; passing upwind of the goal fails. Wind-only\n    agents average the two antennae, binarize at 5 AU, set R to 1 above threshold and let it decay\n    with a 0.97 s time scale below, and turn upwind with P = 1/(1 + exp(-(-0.49 + 1.5 R sin^2\n    theta))). Network agents feed 500 ms histories to the dense network and turn right when its\n    P(left) < 0.4, left when > 0.6, else as wind-only. Open, with readings named. The box width,\n    (a) 112 mm (Fig. 4 legend), (b) +/- 83 mm about the centerline (SI). Whether the 1500-frame\n    complex movie is looped over the 90 s, (a) looped, as in the fly experiments, (b) the run ends\n    with the movie. Reproduced when, in each plume, the plume-matched network beats wind only and\n    wind only beats the mismatched network by two-sided z-tests at p < 0.001 under one reading;\n    the rates are reported against the expected values, and the wind-only rates of the two plumes\n    differing by less than 0.02 is reported for the similarity.\n- id: discussion-ten-percent-gain\n  statement: Adding bilateral detection to the wind-only agent improves success by about 10% of the\n    baseline level.\n  source: Discussion, paragraph 4\n  quote: improved performance by ~10% of baseline levels\n  data: with_inputs\n  where: as fig4ef-agent-success\n  depends_on:\n  - fig4ef-agent-success\n  expected:\n  - quantity: relative gain in success rate of the plume-matched network agent over wind only\n    value: 0.10\n    tolerance: 0.05\n  criterion: The gain is (matched - wind only) / wind only from fig4ef-agent-success, per plume.\n    Tolerance 5 percentage points, wider than the default, as the paper writes \"~10%\" and its own\n    Fig. 4 bars give about 11% (smooth) and 18% (complex). Reproduced when both plumes' gains are\n    within tolerance; partially reproduced when one is.\n- id: figs4-threshold-robustness\n  statement: Across a range of thresholds on the strength of bilateral evidence, agents using\n    plume-consistent features (networks or feature-based GLMs trained in the same plume) outperform\n    agents using inconsistent ones.\n  source: SI Figure S4E and S4F, legend\n  quote: Although these thresholds affect absolute performance levels, across thresholds agents using\n    consistent features ... outperformed agents using inconsistent features\n  data: with_inputs\n  where: as fig4ef-agent-success\n  depends_on:\n  - fig4ef-agent-success\n  - fig2d-smooth-weights\n  - fig2e-complex-weights\n  criterion: Agents as fig4ef-agent-success, with the symmetric thresholds on P(left) varied; the\n    thresholds tested are not listed and are read from Fig. S4E and S4F. The feature GLM agents use\n    the Fig. 2 combined models. Reproduced when, at every threshold tested, for both agent types and\n    both plumes, the consistent agent's success rate exceeds the inconsistent one's; partially\n    reproduced when it holds at most thresholds.\n- id: fig5e-cue-betas\n  statement: For upwind-facing flies in the bulk of the plume, the gradient cue 50 ms before a turn\n    significantly predicts turn direction in the smooth plume while motion does not, and the motion\n    cue does in the complex plume while the gradient does not.\n  source: Results, Different Directional Odor Cues Predict Fly Crosswind Turning in Different Plume\n    Types, paragraph 3; Figure 5E\n  quote: In the smooth plume, the gradient cue but not the motion cue was a significant predictor ...\n    conversely, in the complex plume the motion cue was a significant predictor, but the gradient\n    cue was not\n  statistics:\n  - about: gradient coefficient, smooth plume\n    test: logistic regression with cluster-robust (trajectory-level) SE\n    p: 0.005\n    p_relation: \"<\"\n  - about: motion coefficient, complex plume\n    test: logistic regression with cluster-robust (trajectory-level) SE\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: fitted gradient coefficient, smooth plume\n    value: -0.1181\n    tolerance: 0.0331\n  - quantity: fitted motion coefficient, smooth plume\n    value: -0.0074\n    tolerance: 0.0114\n  - quantity: fitted motion coefficient, complex plume\n    value: 0.0441\n    tolerance: 0.0159\n  - quantity: fitted gradient coefficient, complex plume\n    value: 0.0185\n    tolerance: 0.0161\n  criterion: Coefficients as fitted, from the code's fig5e_cue_beta tables (the figure plots the\n    gradient coefficient times -1, metadata/published_panel_params.json); tolerance 1 cluster-robust\n    SE, the paper's error bars. Turns are the dataset's saccade-like turn events (SI, Behavioral\n    Analysis). Kept turns (SI, Behavioral Analysis, and code filter_published_turns), heading at the\n    turn 160 to 200 degrees; walking upwind, the trajectory's vx low-passed by a fourth-order\n    Butterworth filter at 0.2 Hz run forward and backward (code) pointing upwind (the code tests\n    vx < 0; the SI's positive horizontal velocity is the same in the upwind frame); turn position\n    30 <= x <= 220 mm and 67 <= y <= 97 mm (code values of the SI's 3 cm < x < 22 cm and 3 cm band\n    about the centerline). Predictors are the dataset's per-frame gradient, motion and intensity\n    signals, each smoothed by a causal exponential filter with a 200 ms time constant (SI and code),\n    taken at the last frame at or before 50 ms before turn onset, within one frame (code); onset is\n    the turn event start. One logistic regression per plume of turn direction (code maps a positive\n    direction to 1) on the three predictors and an intercept, cluster-robust SE grouped by\n    trajectory (statsmodels Logit). Open, with readings named. Heading window in the complex\n    plume, (a) 160 to 200 degrees (SI, main), (b) 150 to 210 degrees (code, which produced the\n    figure). The code also drops turns within 15 mm of the arena bounds (1st and 99th percentiles of\n    the plume's positions), which the SI does not list, (a) not applied (main), (b) applied (code).\n    Z-scoring, which the SI states and the code does not perform, (a) the signals as stored (code),\n    (b) z-scored over all frames of the plume's trajectories, (c) z-scored per trajectory; (b) only\n    rescales the coefficients. Not significant is not defined, (a) p >= 0.05, (b) p >= 0.01, the\n    lowest level the legend marks. Reproduced when the smooth gradient coefficient has p < 0.005,\n    the complex motion coefficient p < 0.01, and the smooth motion and complex gradient\n    coefficients are not significant; the outcome is the one all readings give, and the values are\n    compared with the expected ones under the code's readings.\n- id: fig5f-cue-dominance\n  statement: Cue dominance, the gradient-minus-motion log-likelihood difference relative to the total\n    bilateral contribution, is near 1 in the smooth plume (gradient dominates) and negative in the\n    complex plume (motion dominates).\n  source: Results, Different Directional Odor Cues Predict Fly Crosswind Turning in Different Plume\n    Types, paragraph 4; Figure 5F; SI Figure S5D and S5E\n  quote: This measure indicates that the gradient cue dominated in the smooth plume, while the motion\n    cue dominated in the complex plume\n  depends_on:\n  - fig5e-cue-betas\n  expected:\n  - quantity: cue dominance, smooth plume\n    value: 0.946\n    tolerance: 0.095\n  - quantity: cue dominance, complex plume\n    value: -0.662\n    tolerance: 0.066\n  criterion: Values computed from the mean log-likelihoods of the code's fig5f_s5 tables, matching\n    the bar heights of Fig. 5F (about 0.95 and -0.65); default tolerance. On the turns of\n    fig5e-cue-betas, four logistic models per plume with cluster-robust SE (SI, Behavioral Analysis;\n    code VARIANT_FORMULAS), full (gradient, motion, intensity), gradient (gradient, intensity),\n    motion (motion, intensity) and base (intensity only); dominance is (LL_gradient - LL_motion) /\n    (LL_full - LL_base), with LL the log-likelihood per turn (code). Readings as fig5e-cue-betas.\n    Reproduced when the smooth value is positive and the complex value negative, with both within\n    tolerance under one reading; partially reproduced when the signs hold only.\n- id: methods-intensity-right-bias\n  statement: Upwind-facing flies show a bias for rightward turns, toward the projector mount, that\n    grows with the overall projected light intensity.\n  source: SI, Supplementary Methods, Behavioral Analysis, paragraph 3\n  quote: Intensity was included to account for an observed bias exhibited by upwind-facing animals\n    for rightward turns, towards the projector mount location, with increased overall projected\n    light intensity\n  depends_on:\n  - fig5e-cue-betas\n  criterion: The paper gives no test or number. In the full models of fig5e-cue-betas, the\n    intensity coefficient is read in the direction of right turns (the dataset's coding of turn\n    direction decides which sign is right). Reproduced when it favours right turns with p < 0.05\n    (cluster-robust Wald test) in at least one plume and does not significantly favour left turns in\n    the other; its value and p are reported for both plumes.\n- id: figs5c-turn-angles\n  statement: The detected saccade-like turns reorient flies by about 30 degrees, with median angular\n    displacements of -34.2 and +33.8 degrees for the two turn directions.\n  source: SI Figure S5C, legend; Results, Different Directional Odor Cues Predict Fly Crosswind\n    Turning in Different Plume Types, paragraph 2\n  quote: Median values (dashed lines; -34.2°, +33.8°) are similar to turn displacements reported in\n    flies navigating plumes of smoke\n  expected:\n  - quantity: median angular displacement, negative-velocity turns\n    value: -34.2\n    tolerance: 3.42\n    unit: degrees\n  - quantity: median angular displacement, positive-velocity turns\n    value: 33.8\n    tolerance: 3.38\n    unit: degrees\n  criterion: Turns are the dataset's detected turn events, split by the sign of the rotational\n    velocity at the peak (Fig. S5C legend). Open, with readings named. Which turns, (a) all detected\n    turns of both plumes pooled, (b) only the turns kept in fig5e-cue-betas. The displacement,\n    (a) the heading change from the event's start to its end, (b) the integral of rotational\n    velocity over the event. Reproduced when both medians are within tolerance under one reading.\n- id: figs5fh-smoothing-agent\n  statement: Agents using one fixed rule on time-smoothed gradient and motion cues produce turns that\n    a logistic regression weights more on the gradient in the smooth plume and more on motion in the\n    complex plume, so time integration alone can give the flies' pattern.\n  source: Results, Different Directional Odor Cues Predict Fly Crosswind Turning in Different Plume\n    Types, paragraph 5; SI Figure S5F to S5H\n  quote: We found that gradient cues were weighted more strongly in the smooth than in the complex\n    plume; conversely, motion cues were weighted more strongly in the complex than in the smooth\n    plume\n  statistics:\n  - about: within-plume difference of gradient and motion weights, each plume\n    test: logistic regression weights compared\n    p: 0.005\n    p_relation: \"<\"\n  data: with_inputs\n  where: as fig4ef-agent-success\n  criterion: Agents as fig4ef-agent-success with P(left) the logistic of 2.65 times the smoothed\n    gradient plus 0.07 times the smoothed motion, each raw cue smoothed by a causal exponential filter\n    with a 0.85 s half-life (SI, Agent simulations); turns of upwind-facing agents regressed on the\n    local gradient and motion at decision time. Open, with readings named. How the raw cues are\n    computed for agents, (a) the Fig. 2 features over the antenna histories, (b) the gradient and\n    motion of the fly analysis (slice slope and cross-correlation offset); the upwind window, 160 to\n    200 degrees as for the flies; the test of the weight difference is not named, read as a Wald test\n    of the difference of the two coefficients. Reproduced when the gradient weight exceeds the motion\n    weight in the smooth plume and the motion weight exceeds the gradient weight in the complex\n    plume, each difference with p < 0.005, under one reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/brudner-2026.yaml paper/10.1073-pnas.2608896123.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes. Checking the style rules.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/brudner-2026.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/brudner-2026.yaml'))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']))"; git status --short claims/
```

```
22 3
?? claims/brudner-2026.yaml
```

**Agent**

I wrote `claims/brudner-2026.yaml` with 22 claims. `tools/claims_check.py` reports 22 claims, 22 quotes, 4 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PNAS 123(29), published 14 July 2026) and its SI Appendix: Supplementary Methods, the legends of Figs. S1 to S5 and of Movies S1 and S2. Nothing the claims need is missing from the text. I opened PDF pages only to read bar heights (Figs. 2, 4, 5 and S5) and the upwind-turn formula of the SI agent model, which the text garbles.

**Code read.** github.com/emonetlab/GradientMotionMultiplePlumes at commit effc7b0. It holds the Fig. 5E/F analysis, written to run on this dandiset, plus its published result tables. It also holds the Fig. 1 cue maps, the Fig. 2 models with their plotted values, and a re-implementation of the Fig. 3 training.

**Claims.**
- All 22 have quotes and criteria.
- Statistics: 4 entries in 3 claims (Fig. 4 z-tests, P < 0.001; Fig. 5E coefficients, P < 0.005 and P < 0.01; Fig. S5H, P < 0.005).
- Data:
  - 7 use the dandiset alone: Fig. 2C and 2E (the complex plume), and Figs. 5E, 5F, S5C and the intensity-bias finding (behaviour). The S1 resolution claim (Fig. S1F, G) is also on the complex plume.
  - 13 need the smooth plume from Dryad (doi:10.5061/dryad.g27mq71).
  - 2 (Fig. 2B, 2D) use the smooth plume only.

**Details left open, with the readings named.**
- **Fig. 5E/F filters.** The complex-plume heading window is 160 to 200° in the Methods and 150 to 210° in the code. The code alone drops turns within 15 mm of the arena edges. The Methods z-score the cue signals but the code fits them as stored, so the readings are as stored, z-scored over the plume, or z-scored per trajectory. "Not significant" is read as p ≥ 0.05 or p ≥ 0.01.
- **Fig. 1 and S1 comparisons.**
  - The paper does not say how the z-score maps are compared: mean |z| over the plume mask, over the whole frame, or its 95th percentile.
  - The mask's "bias" could be subtracted from the threshold or be a percentage of it.
  - The S1 index could have its intensity rescaling applied to all five movies or only the freestream ones.
  - The code has two timing versions of the smooth movie.
  - For Fig. S1F/G, the reference map and the correlation threshold are not given (r ≥ 0.5 or r ≥ 0.8), and the S1 legend's delays (33 to 500 ms) do not match a 60 Hz movie.
- **Figs. 2 and 3 models.** The threshold for valid sampling regions and how train and test samples are split are not given. Training settings differ: 1e-4, batch 500 and 500 epochs in the SI against the code's archived values. How response strength is measured, and what "symmetrized filters" means, are not defined.
- **Fig. 4 agents.** The start box is 112 mm wide in the figure legend and ±83 mm in the SI. It is not said whether the complex movie loops over the 90 s runs.
- **Fig. S5.** It is not said which turns are pooled for the turn-angle medians or how displacement is measured. For the cue-smoothing agents, the paper does not say how the cues are computed or what test compares the weights.

**Missing that claims needed.**
- No simulation code or trained networks for Fig. 4, S4 and S5F to H.
- The training arrays, masks and checkpoints for Figs. 2 and 3 were not deposited.
- There is no code for Fig. S1.
- The paper gives no counts of flies, trajectories or turns.
- Most values in Figs. 2, 4 and 5 are printed nowhere in the text. I took them from the code's tables or read them off the bars.
- The log-likelihood levels in Fig. S5D/E (about −0.596 and −0.685) disagree with the code's table (−0.576 and −0.676). Fig. 5F agrees with the table.

## End of run

38 turns, 8 minutes, $2.82 at API prices, result: success.
