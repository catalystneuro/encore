# du-2026 · claims · run 44911833697

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 40,400p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 400,800p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper is a full preprint with Methods. Main text is read up to section 2.7; next I'll read the Methods, supplement and any linked code.

**Agent calls Bash**

```bash
sed -n 800,1250p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1250,1783p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/du-2026.yaml; grep -n "du-2026" -r papers/keys.yaml | head; cat claims/fouke-2025.yaml | head -150
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.64898/2026.08.04.742876
title: A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding
datasets:
- archive: dandi
  id: '001201'
  relation: reuses
- archive: dandi
  id: 000129
  relation: reuses
326:  10.64898/2026.08.04.742876: du-2026
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^  datasets:" claims/*.yaml | head -3; f=$(grep -l "^  datasets:" claims/*.yaml | head -1); sed -n 1,60p $f; grep -n "datasets:" $f | head; sed -n 1,80p tools/claims_check.py
```

```
claims/fujisawa-2008.yaml
claims/gao-2018.yaml
claims/kim-2022.yaml
# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,
# doi:10.1038/nn.2134, tested on DANDI:000067 and CRCNS pfc-2 (doi:10.6080/K01V5BWK).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-15,
# protocol as stated in docs/protocol.md (version pilot-15, Reader). It replaces the two files
# read per dataset, claims/fujisawa-2008/000067.yaml and claims/fujisawa-2008/crcns-pfc-2.yaml;
# their ids are kept where the finding is the same (map below).
#
# Text read. The version of record (PDF supplied by a person; text by PyMuPDF in
# paper/10.1038-nn.2134.txt): main text, figure legends, Methods, and the supplement (Supplementary
# Note; legends of Supplementary Figures 1 to 16; references). PDF pages were opened only for
# figures the text garbles: Figure 2 (the counts and t-test marks of panels d and e), Figure 3
# (legend of 3b, the matrix size printed as 117 squared), Supplementary Figures 1 to 3, and the
# legend of Supplementary Figure 11 (142 squared). Where the extracted text prints "1172" and
# "1422" the PDF has 117^2 and 142^2 (a lost superscript); quotes keep the extracted text. The
# paper links no analysis code; its only link is to the KlustaKwik spike sorter, which was not
# read, as it is not analysis code of the paper.
#
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,140p claims/fujisawa-2008.yaml; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

```
#   pointwise two-sided bands, and global bands by the stepping procedure (the smallest pointwise
#   band whose global acceptance level is alpha). A segment is significant when the global band is
#   broken; its extent is where the pointwise band is broken (Figure 1c legend, Supplementary
#   Figure 4E). Alpha = 0.05 (Figure 1c legend). M is not given (Methods M, Supplementary
#   Figure 4 R): 1,000 is a standard choice, as for the jitter; it should not change the outcome.
#   The positions at which D0 is evaluated are not given; 101 points from 0 to 1 is a standard
#   choice.
# - Rates for display and widths. Figure 1c legend says rates are normalised by the time spent at
#   each position (Hz); the Methods' PSTH is spikes per unit length per trial (Supplementary
#   Figure 4A says one converts to the other by dividing by occupancy). Where a rate's shape
#   matters (widths, peaks), readings P-a occupancy-normalised, P-b the Methods' PSTH.
# - Units. All well-isolated PFC units of a session; the paper sets no rate threshold. The 1 Hz
#   "Cells" list of the CRCNS description is not the paper's and is only a variant.
# - Monosynaptic connections. Every spike of each neuron is jittered uniformly on [-5, +5] ms,
#   1,000 surrogates. Cross-correlogram over latencies [-5, +5] ms; pointwise and global bands at
#   the 99% level, the global band from the maximum and minimum of each surrogate. A connection is
#   excitatory (peak) or inhibitory (trough) when the counts break the global band anywhere in
#   [1, 4] ms. Pairs are counted in both directions. The Results add onset below 5 ms and a peak
#   of 2 ms or less. Supplementary Figure 9A jitters the spikes of one neuron only, a variant.
#   The CCG bin width is not given (open; readings B-a 1 ms, B-b 0.5 ms). How the 2 ms width is
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['properties']['claims']['items']['allOf'][2:],indent=1))"
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
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/gwkuqgfkqe/neural-decoder-context-audit.git 2>&1 | tail -3; cd neural-decoder-context-audit 2>/dev/null && git log -1 --format='%H %ci' && git tag | head && ls
```

```
56ae7a8f23085600bddf042b5a4b7819ea9efd8f 2026-11-20 17:10:37 -0500
finger-velocity-2026-11
v1.0-jne-submission
ANALYSIS_PROVENANCE.md
CHECKSUMS.sha256
FROZEN_ARTIFACTS.sha256
Finger_Velocity_Analysis.zip
LICENSE
README.md
REPRODUCE.md
data
outputs
pyproject.toml
requirements-original-analysis.txt
requirements.txt
scripts
src
submission_source
tests
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && git checkout -q v1.0-jne-submission && git log -1 --format='%H %ci' && cat README.md | head -120 && ls -R src scripts submission_source | head -100 && ls outputs data | head -60
```

```
b042fbe1cda2ca5a353751c693d7c95f45de0456 2026-08-04 17:05:37 -0400
# Neural Decoder Context Audit

This archive supports the manuscript “A Context-Conditional Audit of
Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding.” It contains the
analysis implementation, automated tests, public-data identifiers, split and
fold-scope records, derived machine-readable results, figure/table source data,
and exact reproduction instructions. It contains no raw neural recordings or
confidential data.

## Fixed JNE submission release

The repository accompanies the Journal of Neural Engineering submission. The
tagged release `v1.0-jne-submission` fixes the code, tests, manifests, derived
outputs, and figure/table source data used for the submitted manuscript. The
single release ZIP is a portable copy of the same validated package.

## Contents

- `src/neural_evidence/`: estimators, public-data loaders, and strict
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && unzip -l Finger_Velocity_Analysis.zip | grep -i -E "supp|\.pdf|\.tex|\.md" | head -30; grep -ril supplement --include=*.md --include=*.json . | head; cat data/data_manifest.json | head -80
```

```
unzip:  cannot find or open Finger_Velocity_Analysis.zip, Finger_Velocity_Analysis.zip.zip or Finger_Velocity_Analysis.zip.ZIP.
./README.md
{
  "schema_version": "1.1",
  "datasets": {
    "000129": {
      "version": "0.241017.1444",
      "license": "CC-BY-4.0"
    },
    "000139": {
      "version": "0.220113.0408",
      "license": "CC-BY-4.0"
    },
    "001201": {
      "version": "0.251023.2336",
      "license": "CC-BY-4.0"
    }
  },
  "nlb": [
    {
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A2 "where:.*\(simulat\|synthetic\|generated\|code\)" claims/*.yaml | head -30; grep -n "where:" claims/*.yaml | grep -i dandi | head -5
```

```
claims/berg-2020.yaml-921-    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).
claims/berg-2020.yaml-922-  data: elsewhere
claims/berg-2020.yaml:923:  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
claims/berg-2020.yaml-924-    NEFH expression from the Allen Brain Map RNA-seq data, not pinned
claims/berg-2020.yaml-925-  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
--
claims/burman-2023.yaml-418-    awake cortices
claims/burman-2023.yaml-419-  data: elsewhere
claims/burman-2023.yaml:420:  where: Not deposited; generated by the paper's NEURON model and Matlab analysis, github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR
claims/burman-2023.yaml-421-    at commit a404c3e
claims/burman-2023.yaml-422-  criterion: Not testable on DANDI:000458. The model's parameters are in Table 2 and the Methods; the
--
claims/burman-2023.yaml-765-    spiking was more closely aligned to the spiking of other neurons in the network
claims/burman-2023.yaml-766-  data: elsewhere
claims/burman-2023.yaml:767:  where: Not deposited; generated by the paper's simulation code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f
claims/burman-2023.yaml-768-    at revision f6a05661
claims/burman-2023.yaml-769-  criterion: The paper's simulation gist at revision f6a05661, run 20 times (Methods, "Each simulation
--
claims/burman-2023.yaml-791-    n: 16,000 pyramidal neurons from the model
claims/burman-2023.yaml-792-  data: elsewhere
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && wc -l src/neural_evidence/*.py scripts/*.py && cat ANALYSIS_PROVENANCE.md | head -150
```

```
13 src/neural_evidence/__init__.py
   751 src/neural_evidence/estimators.py
   269 src/neural_evidence/link.py
   248 src/neural_evidence/mc_maze.py
   221 src/neural_evidence/mc_rtt.py
   882 src/neural_evidence/nested_estimators.py
   238 src/neural_evidence/robustness_estimators.py
    38 src/neural_evidence/serialization.py
   986 src/neural_evidence/specification_estimators.py
   242 src/neural_evidence/synthetic.py
    25 src/neural_evidence/types.py
    86 scripts/audit_reference_dois.py
   106 scripts/build_final_archive.py
   176 scripts/build_link_confirmation_manifest.py
  1096 scripts/build_submission_figures.py
   189 scripts/compare_reproduced_artifacts.py
    94 scripts/download_link_confirmation.py
    96 scripts/download_public_data.py
   284 scripts/run_link_confirmation.py
   137 scripts/run_link_context_ladder.py
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && cat src/neural_evidence/link.py
```

```
"""Loader for paired center-out and random-target LINK NWB sessions."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split

from .types import DatasetSplit, TrialDataset


def _direction_octant(displacement: np.ndarray) -> int:
    angle = np.arctan2(displacement[1], displacement[0])
    return int(np.floor(((angle + np.pi) / (2.0 * np.pi)) * 8)) % 8


def _phase_basis(n_time: int, n_harmonics: int = 4) -> np.ndarray:
    phase = np.linspace(0.0, 1.0, n_time, endpoint=False)
    features = [np.ones_like(phase)]
[... 250 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n -E "load_link|neural_history_ms|neural_lead_ms|output_|sample_offset|SpikingBand|ThresholdCross|seed|K *=|n_folds|folds|alphas|PENALT|grid|context_mode" scripts/run_primary_analyses.py scripts/run_link_confirmation.py scripts/run_link_context_ladder.py | head -80
```

```
scripts/run_primary_analyses.py:14:from neural_evidence.link import load_link
scripts/run_primary_analyses.py:25:SIGNALS = ("SpikingBandPower", "ThresholdCrossings")
scripts/run_primary_analyses.py:74:            for seed in SEEDS:
scripts/run_primary_analyses.py:75:                split = load_link(
scripts/run_primary_analyses.py:78:                    neural_history_ms=160,
scripts/run_primary_analyses.py:79:                    neural_lead_ms=0,
scripts/run_primary_analyses.py:80:                    context_mode=context,
scripts/run_primary_analyses.py:81:                    output_history_ms=100,
scripts/run_primary_analyses.py:82:                    output_lead_ms=0,
scripts/run_primary_analyses.py:83:                    seed=seed,
scripts/run_primary_analyses.py:86:                    signal == "SpikingBandPower"
scripts/run_primary_analyses.py:88:                    and seed == SEEDS[0]
scripts/run_primary_analyses.py:92:                    seed=seed,
scripts/run_primary_analyses.py:105:                            "seed": seed,
scripts/run_primary_analyses.py:126:                        "context_mode": context,
scripts/run_primary_analyses.py:127:                        "outer_seed": seed,
scripts/run_primary_analyses.py:139:            if signal == "SpikingBandPower":
scripts/run_primary_analyses.py:140:                split = load_link(
scripts/run_primary_analyses.py:143:                    neural_history_ms=160,
scripts/run_primary_analyses.py:144:                    neural_lead_ms=0,
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 1,72p scripts/run_primary_analyses.py && sed -n 240,330p scripts/run_primary_analyses.py
```

```
"""Run frozen primary analysis fully nested audits on existing LINK and NLB data."""

from __future__ import annotations

import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import numpy as np
from pynwb import NWBHDF5IO

from neural_evidence.link import load_link
from neural_evidence.mc_maze import load_mc_maze
from neural_evidence.mc_rtt import load_mc_rtt
from neural_evidence.nested_estimators import (
    evaluate_fully_nested_audit,
    evaluate_nonlinear_neural_audit,
)
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 1,221p src/neural_evidence/mc_rtt.py
```

```
"""Loader for the public NLB MC_RTT NWB training file."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .types import DatasetSplit, TrialDataset


def _spatial_series(interface: object) -> object:
    spatial_series = getattr(interface, "spatial_series", None)
    if spatial_series is None:
        return interface
    return spatial_series[next(iter(spatial_series))]


def _downsample_mean(data: np.ndarray, samples_per_bin: int) -> np.ndarray:
    usable = data.shape[0] - (data.shape[0] % samples_per_bin)
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n -i -E "cluster|bootstrap|percentile|wilcoxon|sign|exact paired|ttest|binom" scripts/*.py src/neural_evidence/nested_estimators.py | grep -v -i "signal" | head -60
```

```
scripts/build_submission_figures.py:392:        bootstrap = []
scripts/build_submission_figures.py:394:            bootstrap.append(rng.choice(differences, len(differences), replace=True).mean())
scripts/build_submission_figures.py:395:        low, high = np.quantile(bootstrap, [0.025, 0.975])
scripts/build_submission_figures.py:985:            nonlinear_link.assign(source_dataset="LINK"),
scripts/build_submission_figures.py:986:            nonlinear_nlb.assign(source_dataset="NLB"),
scripts/build_submission_figures.py:999:def date_cluster_summary() -> pd.DataFrame:
scripts/build_submission_figures.py:1019:                    "date_cluster_ci_low": np.quantile(boot, 0.025),
scripts/build_submission_figures.py:1020:                    "date_cluster_ci_high": np.quantile(boot, 0.975),
scripts/build_submission_figures.py:1068:    date_cluster_summary().to_csv(
scripts/build_submission_figures.py:1069:        TABLES / "link_date_cluster_summary.csv",
scripts/run_link_confirmation.py:45:    parser.add_argument("--bootstrap", type=int, default=500)
scripts/run_link_confirmation.py:123:    record: dict[str, object], path: Path, bootstrap: int
scripts/run_link_confirmation.py:142:            n_bootstrap=bootstrap,
scripts/run_link_confirmation.py:254:            executor.submit(_run_session, record, path, args.bootstrap): record
scripts/run_link_context_ladder.py:31:    parser.add_argument("--bootstrap", type=int, default=500)
scripts/run_link_context_ladder.py:43:def _run(path_string: str, bootstrap: int) -> list[dict[str, object]]:
scripts/run_link_context_ladder.py:62:            n_bootstrap=bootstrap,
scripts/run_link_context_ladder.py:96:        futures = {executor.submit(_run, str(path), args.bootstrap): path for path in paths}
scripts/run_primary_analyses.py:35:    parser.add_argument("--bootstrap", type=int, default=500)
scripts/run_primary_analyses.py:66:def _run_link_session(path_string: str, bootstrap: int) -> dict[str, object]:
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 370,410p scripts/build_submission_figures.py && sed -n 995,1030p scripts/build_submission_figures.py && grep -n "def _cluster_bootstrap_delta_r2" -A40 src/neural_evidence/estimators.py | head -50
```

```
loc="upper center",
        bbox_to_anchor=(0.5, -0.16),
        borderaxespad=0.0,
        fontsize=7.0,
        columnspacing=1.2,
        handletextpad=0.6,
    )
    for axis in axes:
        _style(axis)
    figure.tight_layout(h_pad=1.5, rect=(0, 0.055, 1, 1))
    _save(figure, "figure2_synthetic_matched_seeds")


def _link_ladder() -> pd.DataFrame:
    raw = pd.read_csv(OUTPUT / "link_fully_nested_ladder_metrics.csv")
    order = ["phase_only", "condition_phase", "geometry_additive", "geometry_tensor", "causal_history"]
    rng = np.random.default_rng(20260802)
    rows = []
    for level, context in enumerate(order):
        selected = raw[raw.context_mode == context]
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n -E "^def |PENALTY|ALPHA|n_splits|n_folds|test_size|0\.2|StratifiedKFold|GroupKFold|KFold|r2_score|variance_weighted|seed" src/neural_evidence/nested_estimators.py | head -80
```

```
15:from sklearn.metrics import mean_squared_error, r2_score
16:from sklearn.model_selection import StratifiedKFold, train_test_split
32:DEFAULT_ALPHA_GRID = (
134:    rff_seed: int
142:def _stratified_inner_split(
146:    seed: int,
157:        test_size=validation_size,
158:        random_state=seed,
164:def _select_nuisance_alphas(
168:    seed: int,
175:        seed=seed,
202:def _fully_nested_nuisance_predictions(
206:    seed: int,
217:    splitter = StratifiedKFold(
218:        n_splits=effective_folds,
220:        random_state=seed,
238:            seed=seed + 100 + fold,
286:def _select_grouped_innovation_alpha(
292:    seed: int,
295:    n_splits = min(3, int(counts.min()))
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && sed -n 30,40p src/neural_evidence/nested_estimators.py && sed -n 405,682p src/neural_evidence/nested_estimators.py
```

```
DEFAULT_ALPHA_GRID = (
    0.1,
    1.0,
    10.0,
    100.0,
    1000.0,
    10000.0,
    100000.0,
)
def evaluate_fully_nested_audit(
    dataset: TrialDataset,
    *,
    seed: int = 20260726,
    test_size: float = 0.30,
    inner_validation_size: float = 0.20,
    alpha_grid: tuple[float, ...] = DEFAULT_ALPHA_GRID,
    crossfit_folds: int = 5,
    n_bootstrap: int = 1000,
    n_permutations: int = 0,
    train_indices: np.ndarray | None = None,
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -rn -i "neural_only\|neural-only" scripts src | head -15; head -3 submission_source/tables/link_fully_nested_ladder_metrics.csv | cut -c1-600
```

```
date,task,file,context_mode,context_r2,exact_r2,exact_gain,replacement_gain,self_replacement_max_abs_error,context_mse,exact_mse,replacement_mse,context_rmse,exact_rmse,replacement_rmse,normalized_context_rmse,normalized_exact_rmse,mse_reduction_percent,component_context_rmse,component_exact_rmse,component_replacement_rmse,component_exact_gain,exact_gain_ci_low,exact_gain_ci_high,train_trials,test_trials,final_context_alpha,final_residualizer_alpha,innovation_alpha,crossfit_folds,eligible_sources_min,eligible_sources_median,source_reuse_max,source_reuse_median_nonzero,replacement_distance_mean
2021-10-15,CO,sub-Monkey-N_ses-20211015_obj-1wbkdus_ecephys.nwb,causal_history,0.6853889835850544,0.6976419555886803,0.012252972379129834,0.0011516827184236212,0.0,7.316980188095993e-05,7.03201002265977e-05,7.290195241175013e-05,0.008553934877058623,0.008385708093333425,0.008538264016282826,0.56090197544357,0.5498709427469044,3.8946417526159403,"(0.00926123280730268, 0.007782619780694697)","(0.009117493077436423, 0.007583635041066677)","(0.009228108223274316, 0.007787549257824126)","(0.011033341038719259, 0.013546753861353664)",0.006783180174528812,0.017401345199489635,262,113,0.1,1000.0,10000
2021-10-15,RD,sub-Monkey-N_ses-20211015_obj-a6r2sq_ecephys.nwb,causal_history,0.6428696179886042,0.6517927938864874,0.008923176057281677,-0.008226482712162317,0.0,0.00027975597926637103,0.00027276606203384954,0.00028620014588413704,0.016725907427292876,0.01651563083971816,0.016917450927493097,0.5976038724698505,0.590090850915077,2.4985765276051537,"(0.017845870234374023, 0.0155253622859702)","(0.017728857346500645, 0.015205911391795278)","(0.018033548830906403, 0.015722321976463532)","(0.005280839785826534, 0.012611564168518214)",0.004342469144520147,0.013486470156511943,262,113,0.1,1000.0,100
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -rn -i "neural_r2\|decoder_r2\|0\.308\|neural only" scripts src outputs --include=*.py --include=*.json -l | head; grep -rn "def evaluate_decoders" -A60 src/neural_evidence/estimators.py | grep -n -i "neural\|ridge\|alpha" | head -20; ls outputs/primary_analysis outputs/confirmation_analysis
```

```
scripts/build_submission_figures.py
src/neural_evidence/estimators.py
6:242-    alpha: float = 10.0,
11:247-    """Evaluate template, neural, full, innovation, and shuffle controls."""
14:250-    trial_indices = np.arange(dataset.neural.shape[0])
34:270-    neural_train = _flatten_trials(dataset.neural, train_indices)
35:271-    neural_test = _flatten_trials(dataset.neural, test_indices)
39:275-    context_model = _ridge(alpha)
40:276-    neural_model = _ridge(alpha)
41:277-    full_model = _ridge(alpha)
44:280-    neural_model.fit(neural_train, behavior_train)
46:282-        np.concatenate([context_train, neural_train], axis=1),
52:288-    neural_prediction_test = neural_model.predict(neural_test)
54:290-        np.concatenate([context_test, neural_test], axis=1)
57:293-    neural_residualizer = _ridge(alpha)
58:294-    neural_residualizer.fit(context_train, neural_train)
59:295-    residual_neural_train = (
60:296-        neural_train - neural_residualizer.predict(context_train)
69:448-    alpha_grid: tuple[float, ...] = (
83:462-    """Evaluate Ridge decoders with model-specific nested regularization."""
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -n -i "neural_r2\|0\.308\|neural only\|neural-only" scripts/build_submission_figures.py | head; sed -n 440,540p src/neural_evidence/estimators.py; head -2 submission_source/tables/link_context_ladder.csv | cut -c1-500
```

```
205:    _box(axis, (0.37, 0.69), 0.27, 0.16, "$\\widehat Y_X$\nneural only", facecolor="white", edgecolor=BLUE)


def evaluate_decoders_nested(
    dataset: TrialDataset,
    *,
    seed: int = 20260726,
    test_size: float = 0.30,
    inner_validation_size: float = 0.20,
    alpha_grid: tuple[float, ...] = (
        0.1,
        1.0,
        10.0,
        100.0,
        1000.0,
        10000.0,
        100000.0,
    ),
    n_bootstrap: int = 1000,
    crossfit_folds: int = 5,
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit/submission_source/tables && for f in figure5_estimator_sensitivity_source.csv figure7_specification_sensitivity_source.csv replacement_pool_sensitivity.csv rff_capacity_sensitivity.csv estimator_sensitivity_link.csv; do echo "== $f"; head -40 $f | cut -c1-260; done
```

```
== figure5_estimator_sensitivity_source.csv
panel,group,method,value
LINK,SBP geometry,Nested linear,0.020093010003898557
LINK,SBP + history,Nested linear,0.008732923156297319
LINK,TCR geometry,Nested linear,0.011552790320576477
LINK,TCR + history,Nested linear,0.00419769664865367
LINK,SBP geometry,Block penalties,0.019236895230883663
LINK,SBP + history,Block penalties,0.008553876485111767
LINK,TCR geometry,Block penalties,0.011023629536015933
LINK,TCR + history,Block penalties,0.004101637725889528
LINK,SBP geometry,Nonlinear context,0.017332138297402426
LINK,SBP + history,Nonlinear context,0.006626650472441267
LINK,TCR geometry,Nonlinear context,0.009488587195638672
LINK,TCR + history,Nonlinear context,0.002739043014625648
LINK,SBP geometry,Neural RFF,0.0036085102635334504
LINK,SBP + history,Neural RFF,0.0011148283557725165
LINK,TCR geometry,Neural RFF,
LINK,TCR + history,Neural RFF,
NLB,MC_Maze,Nested linear,0.000513147293947
NLB,MC_RTT,Nested linear,0.0684600125121925
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && grep -rn "sample_offset_ms\|offsets\|quadratic" --include=*.py src scripts | grep -v "^src/neural_evidence/link.py" | head -20
```

```
src/neural_evidence/synthetic.py:179:    quadratic_geometry = np.stack(
src/neural_evidence/synthetic.py:187:    repeated_quadratic = np.repeat(
src/neural_evidence/synthetic.py:188:        quadratic_geometry[:, None, :], n_time, axis=1
src/neural_evidence/synthetic.py:190:    quadratic_phase = (
src/neural_evidence/synthetic.py:191:        repeated_quadratic[:, :, :, None]
src/neural_evidence/synthetic.py:199:            repeated_quadratic,
src/neural_evidence/synthetic.py:200:            quadratic_phase,
scripts/build_submission_figures.py:648:    offsets = np.linspace(-0.24, 0.24, len(methods))
scripts/build_submission_figures.py:649:    for offset, (method, color, marker) in zip(offsets, methods):
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/neural-decoder-context-audit && python -c "
import json;m=json.load(open('outputs/primary_analysis/link_confirmation_manifest.json'));print(list(m.keys()) if isinstance(m,dict) else type(m))
s=m.get('selected') or m.get('sessions') or m
print(json.dumps(s,indent=0)[:1500])"; python -c "
import json;m=json.load(open('data/data_manifest.json'));print(sorted(r['identifier'] for r in m['link']))"
```

```
['schema_version', 'dandiset', 'version', 'selection_frozen', 'selection_rule', 'asset_count', 'excluded_frozen_v05_count', 'eligible_counts', 'selected_ranks_zero_based', 'selected']
[
{
"asset_id": "b9868d49-f641-4b95-a8e3-6295111b958b",
"path": "sub-Monkey-N/sub-Monkey-N_ses-20200924_ecephys.nwb",
"date": "2020-09-24",
"task": "CO",
"size_bytes": 36913714,
"sha256": "aafb0f44f01f92892c81dbcc3f6b7e2491e4c4790a5de93f81295e9baff20667",
"download_url": "https://api.dandiarchive.org/api/assets/b9868d49-f641-4b95-a8e3-6295111b958b/download/",
"excluded_frozen_v05": false,
"eligible_rank_zero_based": 13,
"selection_quantile": "1/11",
"output": "link_confirmation/sub-Monkey-N_ses-20200924_ecephys.nwb"
},
{
"asset_id": "c82f2c89-1e1e-49b1-91e6-068d7c640af3",
"path": "sub-Monkey-N/sub-Monkey-N_ses-20201211_ecephys.nwb",
"date": "2020-12-11",
"task": "CO",
[... 22 more lines not kept]
```

**Agent**

I have what I need. Writing the claims file now: about 33 claims covering the synthetic calibration, the LINK development and confirmation results, MC_RTT and MC_Maze, and the sensitivities.

**Agent calls Write**

```json
{
 "file_path": "claims/du-2026.yaml",
 "content": "# Claims for Du, Lai, Hu & Ye (2026), \"A Context-Conditional Audit of Trial-Pairing-Dependent\n# Neural Gain in Motor-Cortex Decoding\", bioRxiv doi:10.64898/2026.08.04.742876, tested on\n# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol as stated in docs/protocol.md (version pilot-18, Reader).\n#\n# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering\n# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,\n# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's\n# Supplementary information (formal properties, complete ladder results, replacement\n# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)\n# is not under paper/ and is not in the code release; every claim below rests on numbers the\n# main text or its tables state. The one main-text sentence that points to supplement values\n# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).\n#\n# Code read. github.com/gwkuqgfkqe/neural-decoder-context-audit, tag v1.0-jne-submission,\n# commit b042fbe1cda2ca5a353751c693d7c95f45de0456 (Code availability names this release). It\n# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and\n# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run\n# scripts for the synthetic calibration, the primary analyses, the LINK context ladder, the\n# confirmation and the nonlinear-map seeds, the figure builder, tests, and frozen outputs and\n# figure source tables. It holds no script for the temporal-offset, quadratic-capacity,\n# block-penalty or nonlinear-context runs; only their frozen tables. Frozen outputs were not\n# used to set any expected value; every expected value is the paper's.\n#\n# The datasets. DANDI:001201 is LINK, long-term Utah-array recordings from one macaque\n# (Monkey N) doing a finger task in center-out (CO) and random-target (RD) sessions. DANDI:000129\n# is MC_RTT, the Neural Latents Benchmark self-paced random-target reaching session of monkey\n# Indy. The paper also uses MC_Maze-medium, DANDI:000139 version 0.220113.0408, which is not one\n# of this attempt's datasets: its claims are data elsewhere. The synthetic calibration uses data\n# generated by the paper's code: data elsewhere.\n#\n# Data the paper used, as it reports them (Methods 4.2 and 4.3, Table 2).\n# - LINK, Dandiset 001201 version 0.251023.2336. Development set: the nine dates that have both a\n#   CO and an RD session, 18 sessions, 6,750 usable trials, 375 per session. The code's\n#   data/data_manifest.json lists them: 2021-10-15, 2022-02-25, 2022-04-08, 2022-04-15,\n#   2022-04-29, 2022-05-13, 2022-08-10, 2022-09-21, 2022-11-02. Confirmation set: 10 CO and 10 RD\n#   sessions, outside the development set, taken by sorting assets by date and asset ID within\n#   task and picking those nearest the interior ranks j/11, j = 1 to 10 (7,500 usable trials);\n#   the selected assets are listed in the code's outputs/primary_analysis/\n#   link_confirmation_manifest.json. Features are the public 20 ms series in the NWB analysis\n#   module: 96-channel spiking-band power (SBP, \"SpikingBandPower\") and threshold-crossing rate\n#   (TCR, \"ThresholdCrossings\"), finger position and velocity. Outcome is two-dimensional\n#   finger velocity (code: index_velocity and mrs_velocity); position is index_position and\n#   mrs_position; targets are the trials table's index_target_position and mrs_target_position.\n# - MC_RTT, Dandiset 000129 version 0.241017.1444, sub-Indy_desc-train_behavior+ecephys.nwb.\n#   1,080 fixed blocks (the trials table), 130 units, finger velocity, cursor position, target\n#   position; release split 810 train and 270 validation blocks.\n# - MC_Maze-medium, Dandiset 000139, one session, 250 trials, 27 conditions, 152 units, 188/62\n#   release split.\n#\n# Shared method, from the Methods and the code (cited per item).\n# - LINK trial windows (Methods 4.3; link.py). 25 velocity bins of 20 ms (500 ms) per trial.\n#   Neural features for each velocity bin are the eight 20 ms bins (160 ms) of SBP or TCR over 96\n#   channels ending immediately before that bin, flattened to 768 predictors. In the code the\n#   trial's start bin is the neural timestamp nearest the trial start_time, and the window starts\n#   after the history warm-up (8 bins, 160 ms, for the primary analyses); a trial is dropped when\n#   its window runs past start bin plus trial_count. Initial position is the position at the\n#   start bin.\n# - LINK contexts (Methods 4.4; link.py). Phase basis 1, sin(r pi tau), cos(r pi tau), r = 1 to 4,\n#   tau the within-window phase in [0, 1). Direction is the octant of target minus initial\n#   position (code floor(((atan2(dy, dx) + pi) / 2 pi) 8) mod 8). Ladder: phase only (9 features);\n#   direction by phase plus phase (81); plus additive target, initial position and displacement\n#   (87); plus geometry by phase (141, \"geometry by phase\", the primary context); plus five past\n#   bins of two-dimensional measured finger position ending at the same bin as the neural\n#   history (151, \"measured-output history\"). Quadratic sensitivities add the 21 second-order\n#   products of the six geometry variables and their phase interactions (351 and 361 features).\n# - MC_RTT (Methods 4.3 and 4.4; mc_rtt.py). Behavior averaged from 1 kHz samples into 20 ms bins,\n#   spikes histogrammed on the same grid; five 20 ms spike-count bins over 130 units (650\n#   predictors) ending 80 ms before each behavior bin. Headline context is target plus five\n#   cursor-position history bins ending at the same 80 ms boundary plus target minus the last\n#   history cursor position. Direction octant of the block's mean target error is used for\n#   stratification and replacement matching. Blocks use all bins after the warm-up (code; 21\n#   bins per block in Table 2).\n# - Fully nested estimator (Methods 4.5; nested_estimators.py, evaluate_fully_nested_audit).\n#   Ridge with predictors standardized on each training scope, penalty grid 0.1, 1, 10, 100, 1e3,\n#   1e4, 1e5. LINK outer split 70/30 whole trials stratified by direction (code random_state\n#   20260726 for the primary results); NLB uses the release labels. Five condition-stratified\n#   nuisance folds; in each, separate context-to-behavior and context-to-neural penalties from an\n#   inner 80/20 split of the fold's training trials, refit on the fold's training trials, predict\n#   the held fold. The residual learner maps out-of-fold neural residuals to out-of-fold behavior\n#   residuals; its penalty by three-fold whole-trial validation on those residuals; refit on all.\n#   Final nuisance penalties from an inner split of all outer-training trials, nuisances refit on\n#   all of them, the outer test evaluated once.\n# - Gain (Results 2.1, Methods 4.9). Gain = (MSE_C - MSE_C+X) / Var(Y) on the flattened outer-test\n#   bins of one session, MSE averaged over both components, Var(Y) the component-averaged squared\n#   deviation from each test-component mean. R2 is variance-weighted multi-output. Percentage MSE\n#   reduction = 100 (MSE_C - MSE_C+X) / MSE_C. A task mean is the mean over its sessions; a\n#   combined LINK mean is the mean over all sessions.\n# - Replacement (Methods 4.7). For each test trial, the source is another test trial of the same\n#   condition minimizing mean squared distance between complete flattened context trajectories,\n#   standardized with outer-training centers and scales; integer trial index breaks ties; the\n#   source's neural history is residualized with its own context. Permutation diagnostic: 100\n#   within-condition permutations of test trials without fixed points; fitted model held fixed.\n# - LINK date-clustered intervals (Table 1 legend; build_submission_figures.py,\n#   date_cluster_summary). Resample the nine dates with replacement 10,000 times, take the mean\n#   gain over the sessions of the sampled dates, 2.5 and 97.5 percentiles. NLB intervals resample\n#   held-out trials within condition (estimators.py, _cluster_bootstrap_delta_r2; 500 resamples in\n#   run_primary_analyses.py).\n#\n# Details the paper and code leave open are named in the criteria of the claims they affect.\nschema_version: 2\npaper: doi:10.64898/2026.08.04.742876\nclaims:\n- id: synthetic-template-null\n  statement: In the matched-seed synthetic calibration, the template-only regime (no trial signal\n    in the neural features) gave a median context-conditional neural gain of about zero\n    (-0.0000023, range -0.0000588 to 0.0000248 over ten seeds).\n  source: Results 2.2, paragraph 2; Figure 2a\n  quote: The template-only median context-conditional neural gain was -0.0000023 (range,\n    -0.0000588 to 0.0000248; Figure 2)\n  data: elsewhere\n  where: Not deposited; generated by the paper's code, github.com/gwkuqgfkqe/neural-decoder-context-audit\n    tag v1.0-jne-submission (commit b042fbe), src/neural_evidence/synthetic.py and\n    scripts/run_synthetic_calibration.py\n  expected:\n  - quantity: template-only median gain over seeds 20260726 to 20260735\n    value: -0.0000023\n    tolerance: 0.03\n    unit: delta R2\n  criterion: The generator and regimes are those of Methods 4.8 (480 trials, 60 bins, eight\n    conditions, 48 neural features, AR(1) coefficient 0.85, template scale 1.0, neural noise SD\n    0.20; template-only regime trial-signal scale 0.20 and embedding strength 0), seeds 20260726\n    to 20260735, estimated with the fully nested estimator. The tolerance is the paper's own\n    prespecified criterion, template-null median absolute gain below 0.03 (Methods 4.8), since\n    10% of a value this close to zero has no meaning. Reproduced when the median absolute gain is\n    below 0.03; the median and range are reported.\n- id: synthetic-signal-ordering\n  statement: Weak and strong trial-signal regimes gave median gains of 0.2245 and 0.3736, and the\n    three regime medians were strictly ordered (template-only, weak, strong).\n  source: Results 2.2, paragraph 2; Figure 2a\n  quote: Weak and strong regimes yielded median gains of 0.2245 and 0.3736, respectively. The\n    medians were strictly ordered for all three regimes.\n  data: elsewhere\n  where: Not deposited; generated by the paper's code, github.com/gwkuqgfkqe/neural-decoder-context-audit\n    tag v1.0-jne-submission (commit b042fbe), src/neural_evidence/synthetic.py\n  expected:\n  - quantity: weak-regime median gain\n    value: 0.2245\n    tolerance: 0.02245\n    unit: delta R2\n  - quantity: strong-regime median gain\n    value: 0.3736\n    tolerance: 0.03736\n    unit: delta R2\n  criterion: Regimes as in Methods 4.8 (weak trial-signal scale 0.25, embedding 0.8; strong 0.35,\n    1.8), seeds 20260726 to 20260735. Reproduced when both medians are within tolerance and the\n    three medians are strictly increasing from template-only to strong.\n- id: synthetic-pair-breaking\n  statement: In the strong synthetic regime, correct-pair gain exceeded nearest source-context\n    replacement and the mean of 100 within-condition permutations for 10 of 10 seeds;\n    replacement and permutation means were -0.3486 and -0.3663.\n  source: Results 2.2, paragraph 2; Figure 2b\n  quote: In the strong regime, correct-pair gain exceeded nearest replacement and the mean of 100\n    within-condition test-trial permutations for 10/10 seeds. Nearest replacement produced a mean\n    gain of -0.3486; the permutation mean was -0.3663.\n  data: elsewhere\n  where: Not deposited; generated by the paper's code, github.com/gwkuqgfkqe/neural-decoder-context-audit\n    tag v1.0-jne-submission (commit b042fbe), src/neural_evidence/synthetic.py\n  depends_on:\n  - synthetic-signal-ordering\n  expected:\n  - quantity: seeds with correct-pair gain above replacement and above the permutation mean\n    value: 10\n    tolerance: 1\n    unit: seeds of 10\n  - quantity: strong-regime mean nearest-replacement gain\n    value: -0.3486\n    tolerance: 0.03486\n    unit: delta R2\n  - quantity: strong-regime mean of permutation-mean gains\n    value: -0.3663\n    tolerance: 0.03663\n    unit: delta R2\n  criterion: Replacement and permutation as in Methods 4.7. The tolerance on the seed count is\n    the paper's own prespecified criterion, at least 9 of 10 seeds (Methods 4.8). Reproduced when\n    at least 9 seeds have correct-pair gain above both controls and both means are within\n    tolerance.\n- id: link-development-sample\n  statement: The LINK development set is the nine dates with both a CO and an RD session, 18\n    sessions and 6,750 usable trials from one macaque, with 375 usable trials in every analyzed\n    session.\n  source: Results 2.3, paragraph 1; Methods 4.2, LINK paragraph\n  quote: We analyzed all nine LINK dates containing both center-out (CO) and random-target (RD)\n    sessions... 18 sessions and 6,750 trials from one macaque\n  datasets:\n  - \"001201\"\n  expected:\n  - quantity: dates with both a CO and an RD session in Dandiset 001201\n    value: 9\n    tolerance: 0\n    unit: dates\n  - quantity: usable trials over the 18 development sessions\n    value: 6750\n    tolerance: 675\n    unit: trials\n  criterion: The number of dates is a count of the archive's sessions, so it must match exactly.\n    A usable trial is one whose 25-bin window, starting 160 ms after the bin nearest the trial\n    start, ends before the trial's last bin (link.py; Methods 4.3). Reproduced when 9 dates are\n    found, the usable trial count is within tolerance, and each of the 18 sessions has 375 usable\n    trials (\"Every analyzed LINK session had 375 usable trials\", Methods 4.2); partially\n    reproduced when the total is within tolerance but some session differs from 375.\n- id: link-neural-only-r2\n  statement: In the LINK development sessions, neural-only Ridge decoding of finger velocity from\n    160 ms of SBP had held-out R2 of 0.308 in CO and 0.313 in RD, the same at every rung of the\n    context ladder.\n  source: Results 2.3, paragraph 3; Abstract, Main results\n  quote: Neural-only performance remained at 0.308/0.313 for CO/RD\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-development-sample\n  expected:\n  - quantity: CO mean neural-only R2 over nine sessions\n    value: 0.308\n    tolerance: 0.0308\n  - quantity: RD mean neural-only R2 over nine sessions\n    value: 0.313\n    tolerance: 0.0313\n  criterion: Neural-only Ridge from X (768 SBP predictors) to Y on the same 70/30 outer split\n    (Methods 4.5, \"Neural-only Ridge used X to predict Y on the same outer splits\"). The paper\n    does not say how the neural-only penalty is chosen; the code (estimators.py,\n    evaluate_decoders_nested, as run by run_link_context_ladder.py) selects it from the grid on\n    an inner 80/20 direction-stratified split of the outer-training trials, and that is followed.\n    Variance-weighted R2 per session, averaged over the nine sessions of each task. Reproduced\n    when both task means are within tolerance.\n- id: link-context-ladder-gain\n  statement: In LINK with SBP, mean context-conditional neural gain fell along the context ladder,\n    from 0.3012/0.3125 (CO/RD) beyond phase alone to 0.0657/0.0502 beyond direction by phase,\n    0.0443/0.0332 beyond additive geometry, 0.0193/0.0209 beyond geometry by phase, and\n    0.0077/0.0098 beyond geometry by phase plus measured-output history.\n  source: Results 2.3, paragraph 3; Figure 3b\n  quote: With phase-only context, mean SBP gain was 0.3012 in CO and 0.3125 in RD (Figure 3).\n    Direction by phase reduced it to 0.0657/0.0502; additive geometry to 0.0443/0.0332; geometry\n    by phase to 0.0193/0.0209; and measured-output history to 0.0077/0.0098.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-development-sample\n  expected:\n  - quantity: CO mean gain, phase only\n    value: 0.3012\n    tolerance: 0.03012\n    unit: delta R2\n  - quantity: RD mean gain, phase only\n    value: 0.3125\n    tolerance: 0.03125\n    unit: delta R2\n  - quantity: CO mean gain, direction by phase\n    value: 0.0657\n    tolerance: 0.00657\n    unit: delta R2\n  - quantity: RD mean gain, direction by phase\n    value: 0.0502\n    tolerance: 0.00502\n    unit: delta R2\n  - quantity: CO mean gain, additive geometry\n    value: 0.0443\n    tolerance: 0.00443\n    unit: delta R2\n  - quantity: RD mean gain, additive geometry\n    value: 0.0332\n    tolerance: 0.00332\n    unit: delta R2\n  - quantity: CO mean gain, geometry by phase\n    value: 0.0193\n    tolerance: 0.00193\n    unit: delta R2\n  - quantity: RD mean gain, geometry by phase\n    value: 0.0209\n    tolerance: 0.00209\n    unit: delta R2\n  - quantity: CO mean gain, plus measured-output history\n    value: 0.0077\n    tolerance: 0.00077\n    unit: delta R2\n  - quantity: RD mean gain, plus measured-output history\n    value: 0.0098\n    tolerance: 0.00098\n    unit: delta R2\n  criterion: Fully nested estimator with SBP, the five contexts of Methods 4.4, outer split seed\n    20260726 (run_link_context_ladder.py), mean over the nine sessions of each task. Reproduced\n    when the task means fall at every step for both tasks and at least 8 of the 10 values are\n    within tolerance; partially reproduced when they fall at every step but fewer are within\n    tolerance.\n- id: link-context-only-r2\n  statement: Context-only R2 in LINK rose along the ladder from 0.0084/0.0055 (CO/RD) with phase\n    alone to 0.6617/0.6839 with geometry by phase plus measured-output history.\n  source: Results 2.3, paragraph 3; Figure 3a\n  quote: Context-only R2 rose from 0.0084/0.0055 to 0.6617/0.6839.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-development-sample\n  expected:\n  - quantity: CO mean context-only R2, phase only\n    value: 0.0084\n    tolerance: 0.00084\n  - quantity: RD mean context-only R2, phase only\n    value: 0.0055\n    tolerance: 0.00055\n  - quantity: CO mean context-only R2, plus measured-output history\n    value: 0.6617\n    tolerance: 0.06617\n  - quantity: RD mean context-only R2, plus measured-output history\n    value: 0.6839\n    tolerance: 0.06839\n  criterion: Context-only R2 is that of the fully nested final context model on the outer test of\n    each session, averaged over the nine sessions of each task. The phase-only values are so\n    small that 10% is below the variation one refit could give; reproduced when the two\n    history values are within tolerance, the two phase-only values are below 0.02, and the\n    context-only R2 rises at every rung for both tasks. The phase-only values against their 10%\n    tolerances are reported.\n- id: link-phase-only-replacement\n  statement: With phase-only context, nearest-replacement gain in RD stayed positive (0.10498),\n    so replacement does not remove the task-template correction under an under-specified\n    context.\n  source: Results 2.3, paragraph 4\n  quote: The phase-only RD replacement gain remained positive (0.10498).\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-context-ladder-gain\n  expected:\n  - quantity: RD mean nearest-replacement gain, phase only\n    value: 0.10498\n    tolerance: 0.010498\n    unit: delta R2\n  criterion: Mean over the nine RD sessions of the replacement gain under phase-only context.\n    Replacement condition is the direction octant (link.py), as in every LINK replacement.\n- id: link-task-contrast-by-context\n  statement: The descriptive RD-minus-CO gain contrast changed with the context; it was positive\n    under phase only, negative under direction by phase and additive geometry, near zero under\n    geometry by phase, and small positive after measured-output history.\n  source: Results 2.3, paragraph 5; Figure 3c\n  quote: It was positive under phase only, negative under direction and additive geometry, near\n    zero under geometry-by-phase, and small positive after measured-output history.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-context-ladder-gain\n  criterion: Per date, RD gain minus CO gain, averaged over the nine dates, with a 95% interval\n    from 10,000 date resamples (Figure 3c legend; build_submission_figures.py, _link_ladder). The\n    paper calls these descriptive and tests nothing. Signs are judged on the mean. \"Near zero\"\n    has no threshold in the paper or code; readings (a) the 95% date-bootstrap interval contains\n    zero, (b) the absolute mean is smaller than under direction by phase and under additive\n    geometry. Reproduced when phase only is positive, direction by phase and additive geometry\n    are negative, measured-output history is positive, and geometry by phase is near zero under\n    a reading; partially reproduced when the signs hold but neither reading makes geometry by\n    phase near zero.\n- id: nested-geometry-gain\n  statement: With geometry-by-phase context, fully nested mean gain over the 18 LINK sessions was\n    0.02009 for SBP (18 of 18 sessions positive) and 0.01155 for TCR (17 of 18 positive).\n  source: Results 2.4, paragraph 1; Table 1; Figure 4a\n  quote: With geometry-by-phase context, mean gain was 0.02009 for SBP (18/18 sessions positive)\n    and 0.01155 for threshold-crossing rate (TCR; 17/18 positive). Date-clustered 95% intervals\n    were [0.01586, 0.02404] and [0.00709, 0.01594], respectively.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - link-development-sample\n  statistics:\n  - about: SBP mean gain, geometry by phase\n    test: date-clustered bootstrap interval\n    ci:\n      level: 0.95\n      low: 0.01586\n      high: 0.02404\n    n: 18 sessions on nine dates\n  - about: TCR mean gain, geometry by phase\n    test: date-clustered bootstrap interval\n    ci:\n      level: 0.95\n      low: 0.00709\n      high: 0.01594\n    n: 18 sessions on nine dates\n  expected:\n  - quantity: SBP mean gain, geometry by phase\n    value: 0.02009\n    tolerance: 0.00423\n    unit: delta R2\n  - quantity: SBP sessions with positive gain\n    value: 18\n    tolerance: 1.8\n    unit: sessions of 18\n  - quantity: TCR mean gain, geometry by phase\n    value: 0.01155\n    tolerance: 0.00446\n    unit: delta R2\n  - quantity: TCR sessions with positive gain\n    value: 17\n    tolerance: 1.7\n    unit: sessions of 18\n  criterion: Tolerances on the means are the larger distance from the mean to a bound of the\n    paper's date-clustered 95% interval. Outer split seed 20260726 (run_primary_analyses.py,\n    SEEDS[0]). Reproduced when both means and both counts are within tolerance.\n- id: nested-history-gain\n  statement: Adding lag-matched measured-output history reduced fully nested mean gain to 0.00873\n    for SBP (17 of 18 sessions positive) and 0.00420 for TCR (16 of 18 positive).\n  source: Results 2.4, paragraph 1; Table 1\n  quote: Adding lag-matched measured-output history reduced the means to 0.00873 for SBP and\n    0.00420 for TCR; 17/18 and 16/18 sessions were positive.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  statistics:\n  - about: SBP mean gain, plus measured-output history\n    test: date-clustered bootstrap interval\n    ci:\n      level: 0.95\n      low: 0.00600\n      high: 0.01096\n    n: 18 sessions on nine dates\n  - about: TCR mean gain, plus measured-output history\n    test: date-clustered bootstrap interval\n    ci:\n      level: 0.95\n      low: 0.00217\n      high: 0.00630\n    n: 18 sessions on nine dates\n  expected:\n  - quantity: SBP mean gain, plus measured-output history\n    value: 0.00873\n    tolerance: 0.00273\n    unit: delta R2\n  - quantity: SBP sessions with positive gain\n    value: 17\n    tolerance: 1.7\n    unit: sessions of 18\n  - quantity: TCR mean gain, plus measured-output history\n    value: 0.0042\n    tolerance: 0.0021\n    unit: delta R2\n  - quantity: TCR sessions with positive gain\n    value: 16\n    tolerance: 1.6\n    unit: sessions of 18\n  criterion: Tolerances on the means are the larger distance to a bound of the Table 1 interval.\n    Reproduced when all four values are within tolerance and each signal's history mean is below\n    its geometry-by-phase mean.\n- id: nested-replacement-negative\n  statement: Nearest source-context replacement made all four LINK mean gains negative, -0.00714\n    and -0.00407 for SBP (geometry by phase, plus history) and -0.00905 and -0.00537 for TCR.\n  source: Results 2.4, paragraph 2; Table 1; Figure 4b\n  quote: Nearest source-context replacement changed the four mean gains to -0.00714, -0.00407,\n    -0.00905, and -0.00537, respectively.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  - nested-history-gain\n  expected:\n  - quantity: SBP mean replacement gain, geometry by phase\n    value: -0.00714\n    tolerance: 0.000714\n    unit: delta R2\n  - quantity: SBP mean replacement gain, plus history\n    value: -0.00407\n    tolerance: 0.000407\n    unit: delta R2\n  - quantity: TCR mean replacement gain, geometry by phase\n    value: -0.00905\n    tolerance: 0.000905\n    unit: delta R2\n  - quantity: TCR mean replacement gain, plus history\n    value: -0.00537\n    tolerance: 0.000537\n    unit: delta R2\n  criterion: Replacement as in Methods 4.7, with the fitted models of the correct-pair claims.\n    Reproduced when all four means are negative and at least three are within tolerance;\n    partially reproduced when all four are negative and fewer are within tolerance.\n- id: replacement-source-diagnostics\n  statement: For primary SBP geometry, every test trial had at least five eligible same-condition\n    sources, the median over sessions of the maximum source reuse was three targets and the\n    maximum over sessions four, and self-replacement reproduced the correct-pair predictions\n    exactly.\n  source: Results 2.4, paragraph 2\n  quote: For primary SBP geometry, every target had at least five eligible same-condition sources;\n    the median session maximum source reuse was three targets and the maximum over sessions was\n    four. Self-replacement reproduced correct-pair predictions exactly to numerical precision.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-replacement-negative\n  expected:\n  - quantity: minimum over sessions of eligible same-condition sources per test trial\n    value: 5\n    tolerance: 0\n    unit: trials\n  - quantity: median over sessions of the maximum reuse of one source\n    value: 3\n    tolerance: 0\n    unit: targets\n  - quantity: maximum over sessions of the maximum reuse of one source\n    value: 4\n    tolerance: 0\n    unit: targets\n  criterion: Counts are exact integers of a deterministic matching on the outer split of seed\n    20260726, so they are judged exactly; at least five eligible sources is a lower bound\n    (reproduced when the minimum is 5 or more). Self-replacement is reproduced when the largest\n    absolute difference between self-replacement and correct-pair predictions is at floating-point\n    precision (below 1e-10). Partially reproduced when the bound and self-replacement hold but a\n    reuse count differs by one.\n- id: permutation-negative\n  statement: The mean gain of 100 within-condition whole-trial permutations was negative in every\n    LINK session, with an across-session mean of -0.0142.\n  source: Results 2.4, paragraph 2\n  quote: The mean of 100 within-condition whole-trial permutations was negative in every session\n    (across-session mean, -0.0142).\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  expected:\n  - quantity: across-session mean of session permutation-mean gains\n    value: -0.0142\n    tolerance: 0.00142\n    unit: delta R2\n  criterion: Permutations as in Methods 4.7. The sentence follows the primary SBP geometry\n    sentence, but which sessions it covers is not stated; readings (a) the 18 SBP\n    geometry-by-phase sessions, (b) the 36 sessions of SBP and TCR under geometry by phase.\n    Reproduced when, under a reading, every session's permutation mean is negative and the\n    across-session mean is within tolerance.\n- id: replacement-penalty-distance\n  statement: The replacement penalty had no consistent rank relation to the nearest-source\n    context distance across sessions.\n  source: Results 2.4, paragraph 2\n  quote: Replacement penalty had no consistent rank relation to nearest-source distance across\n    sessions\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-replacement-negative\n  criterion: Per session, the Spearman correlation over test trials between the nearest-source\n    distance and the replacement penalty (trial MSE under replacement minus trial MSE under\n    correct pairing), as computed in nested_estimators.py. The paper gives no test; \"no\n    consistent rank relation\" is read as (a) the session correlations are not all of one sign, or\n    (b) the across-session mean correlation has a 95% date-bootstrap interval (as for Table 1)\n    that contains zero. A claim of absence with no test in the paper; reproduced when both\n    readings hold, partially when one does, not reproduced when neither. Sessions are the 18 SBP\n    geometry-by-phase sessions.\n- id: replacement-ranks-lower\n  statement: Replacement with the first to fifth nearest sources and with a random same-condition\n    source all lowered the across-session mean gain.\n  source: Results 2.4, paragraph 2 (values in the supplement, not available)\n  quote: Ranks one through five and a random same-condition source, reported in the supplement,\n    all lowered the across-session mean.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-replacement-negative\n  criterion: The supplement with the values was not available, so only the direction is judged.\n    For each of the six source rules, the across-session mean gain is compared with the\n    correct-pair across-session mean. Which sessions are meant is not stated; readings (a) the 18\n    SBP geometry-by-phase sessions, (b) SBP and TCR geometry-by-phase sessions, each signal\n    separately. How the random source is drawn is not given beyond \"same-condition\"; a uniform\n    draw among the other same-condition test trials with a fixed seed is a standard choice, and\n    three draws are shown. Reproduced when, under a reading, all six means are below the\n    correct-pair mean.\n- id: practical-mse-reduction\n  statement: In LINK, SBP geometry-by-phase gain reduced context-model MSE by 4.92% on average\n    (mean context RMSE 0.01407 to 0.01372), adding measured-output history reduced the remaining\n    MSE by 2.72%, and the TCR reductions were 2.83% and 1.31%.\n  source: Results 2.4, paragraph 3; Table 1; Figure 8c\n  quote: In LINK, SBP geometry reduced MSE by 4.92% on average, from mean context RMSE 0.01407 to\n    0.01372 in the released numerical velocity units per 20 ms bin. Adding measured-output\n    history reduced the remaining MSE by 2.72%. Corresponding TCR reductions were 2.83% and\n    1.31%.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  - nested-history-gain\n  expected:\n  - quantity: SBP geometry-by-phase mean percentage MSE reduction\n    value: 4.92\n    tolerance: 0.492\n    unit: percent\n  - quantity: SBP mean context RMSE, geometry by phase\n    value: 0.01407\n    tolerance: 0.001407\n    unit: released velocity units per 20 ms bin\n  - quantity: SBP mean correct-pair RMSE, geometry by phase\n    value: 0.01372\n    tolerance: 0.001372\n    unit: released velocity units per 20 ms bin\n  - quantity: SBP plus-history mean percentage MSE reduction\n    value: 2.72\n    tolerance: 0.272\n    unit: percent\n  - quantity: TCR geometry-by-phase mean percentage MSE reduction\n    value: 2.83\n    tolerance: 0.283\n    unit: percent\n  - quantity: TCR plus-history mean percentage MSE reduction\n    value: 1.31\n    tolerance: 0.131\n    unit: percent\n  criterion: Per session 100 (MSE_C - MSE_C+X) / MSE_C (Methods 4.9), averaged over the 18\n    sessions; RMSE is the square root of each session's MSE, averaged over sessions\n    (build_submission_figures.py, date_cluster_summary). In the plus-history row, \"remaining MSE\"\n    is the MSE of the plus-history context model (Table 1, \"MSE reduction is relative to context\n    only\"). Reproduced when at least five of the six values are within tolerance.\n- id: representative-trial\n  statement: The prespecified rule for the illustrative trajectory (session with median primary\n    SBP geometry gain, then the held-out trial with median context-minus-correct trial MSE\n    improvement) selects 2022-09-21 RD, trial 123.\n  source: Figure 8a and legend; Methods 4.9, last paragraph\n  quote: Prespecified median-improvement trial... 2022-09-21 RD, trial 123\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  criterion: Rule of Methods 4.9; ties to the earlier date and the lower trial index. With 18\n    sessions there is no single median session; the paper's tie rule takes the earlier date, read\n    as the lower of the two middle sessions (the ninth in gain order), or the one of the two\n    middle sessions with the earlier date. With an odd number of test trials (113) the median\n    trial is the middle one. What \"trial 123\" indexes is not stated; readings (a) the row of the\n    session's NWB trials table, (b) the index among the session's usable trials (the code's\n    trial_id), (c) the position among the session's held-out trials. Reproduced when the rule\n    selects 2022-09-21 RD and the selected trial is 123 under a reading; partially reproduced\n    when only the session matches.\n- id: confirm-geometry-gain\n  statement: In the 20 untouched LINK confirmation sessions, SBP geometry-by-phase gain was\n    positive in all 20 and averaged 0.02158 (CO 0.02104, RD 0.02213).\n  source: Results 2.5, paragraph 2; Table 1; Figure 6a\n  quote: Under geometry-by-phase, gain was positive in 20/20 sessions and averaged 0.02158 (CO,\n    0.02104; RD, 0.02213).\n  datasets:\n  - \"001201\"\n  expected:\n  - quantity: sessions with positive gain\n    value: 20\n    tolerance: 2\n    unit: sessions of 20\n  - quantity: combined mean gain\n    value: 0.02158\n    tolerance: 0.002158\n    unit: delta R2\n  - quantity: CO mean gain\n    value: 0.02104\n    tolerance: 0.002104\n    unit: delta R2\n  - quantity: RD mean gain\n    value: 0.02213\n    tolerance: 0.002213\n    unit: delta R2\n  criterion: The sessions are those of the paper's frozen manifest\n    (outputs/primary_analysis/link_confirmation_manifest.json, from the rule of Methods 4.2);\n    the rule is also re-run on the dandiset's asset list and any difference reported. SBP, outer\n    split seed 20260726 (run_link_confirmation.py). The paper's own gate, at least 16 of 20\n    positive with positive CO and RD means (ANALYSIS_PROVENANCE.md, criterion i), is reported.\n    Reproduced when all four values are within tolerance.\n- id: confirm-history-contraction\n  statement: In the confirmation sessions, adding measured-output history reduced the combined\n    mean gain to 0.00755 (CO 0.00670, RD 0.00840), with 19 of 20 sessions positive.\n  source: Results 2.5, paragraph 2; Table 1; Figure 6a\n  quote: Measured-output history reduced the combined mean to 0.00755 (CO, 0.00670; RD, 0.00840),\n    with 19/20 sessions positive.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - confirm-geometry-gain\n  expected:\n  - quantity: combined mean gain, plus measured-output history\n    value: 0.00755\n    tolerance: 0.000755\n    unit: delta R2\n  - quantity: CO mean gain, plus measured-output history\n    value: 0.0067\n    tolerance: 0.00067\n    unit: delta R2\n  - quantity: RD mean gain, plus measured-output history\n    value: 0.0084\n    tolerance: 0.00084\n    unit: delta R2\n  - quantity: sessions with positive gain\n    value: 19\n    tolerance: 1.9\n    unit: sessions of 20\n  criterion: Reproduced when all four values are within tolerance and the combined mean is below\n    the geometry-by-phase combined mean (the paper's gate ii).\n- id: confirm-replacement\n  statement: In the confirmation sessions, nearest-replacement gain averaged -0.00771 under\n    geometry by phase, and correct-pair gain exceeded replacement gain in all 20 sessions and in\n    both task means.\n  source: Results 2.5, paragraph 2; Figure 6b\n  quote: Nearest source-context replacement averaged -0.00771 under geometry, and correct-pair\n    gain exceeded replacement in 20/20 sessions and in both task means.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - confirm-geometry-gain\n  expected:\n  - quantity: combined mean replacement gain, geometry by phase\n    value: -0.00771\n    tolerance: 0.000771\n    unit: delta R2\n  - quantity: sessions with correct-pair gain above replacement gain\n    value: 20\n    tolerance: 2\n    unit: sessions of 20\n  criterion: Reproduced when both values are within tolerance and the correct-pair mean exceeds\n    the replacement mean in CO and in RD.\n- id: confirm-table1-values\n  statement: Table 1 gives, for the confirmation sessions, a replacement gain of -0.00498 with\n    measured-output history and MSE reductions of 4.76% (geometry by phase) and 2.05% (plus\n    history).\n  source: Table 1, rows \"LINK confirm SBP\"\n  inferred: Numbers only in Table 1; no sentence of the text states them.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - confirm-history-contraction\n  expected:\n  - quantity: combined mean replacement gain, plus measured-output history\n    value: -0.00498\n    tolerance: 0.000498\n    unit: delta R2\n  - quantity: mean percentage MSE reduction, geometry by phase\n    value: 4.76\n    tolerance: 0.476\n    unit: percent\n  - quantity: mean percentage MSE reduction, plus measured-output history\n    value: 2.05\n    tolerance: 0.205\n    unit: percent\n- id: rtt-data\n  statement: The MC_RTT training file holds 1,080 fixed analysis blocks, 130 units, finger\n    velocity, cursor position and target position, with a release split of 810 train and 270\n    validation blocks.\n  source: Methods 4.2, MC_RTT paragraph; Table 2\n  quote: We used sub-Indy_desc-train_behavior+ecephys.nwb from Dandiset 000129 version\n    0.241017.1444... 1,080 fixed analysis blocks, 130 units, finger velocity, cursor position, and\n    target position. Release labels provide 810/270 train/validation blocks\n  datasets:\n  - \"000129\"\n  expected:\n  - quantity: analysis blocks\n    value: 1080\n    tolerance: 0\n    unit: blocks\n  - quantity: units\n    value: 130\n    tolerance: 0\n    unit: units\n  - quantity: train blocks\n    value: 810\n    tolerance: 0\n    unit: blocks\n  - quantity: validation blocks\n    value: 270\n    tolerance: 0\n    unit: blocks\n  criterion: Counts of the released file, judged exactly. A block is a row of the trials table\n    kept by mc_rtt.py (at least one bin after the 180 ms warm-up and within the binned record);\n    train and validation are the trials table's split labels \"train\" and \"val\".\n- id: rtt-gain\n  statement: In MC_RTT, target plus lag-matched cursor-position history gave context-only R2 of\n    0.6031, and fully nested neural gain beyond it was 0.06846 (conditional interval 0.05371 to\n    0.08478), context RMSE falling from 39.78 to 36.19 (a 17.25% MSE reduction), with component\n    gains 0.0836 and 0.0513 and replacement gain -0.02297.\n  source: Results 2.6, paragraph 3; Table 1; Figure 4c\n  quote: In MC_RTT, target plus lag-matched measured cursor-position history achieved context-only\n    R2 = 0.6031. Fully nested neural gain was 0.06846 (conditional interval, [0.05371, 0.08478]);\n    context RMSE decreased from 39.78 to 36.19, a 17.25% reduction in MSE. Component gains were\n    0.0836 and 0.0513. Replacement produced -0.02297.\n  datasets:\n  - \"000129\"\n  depends_on:\n  - rtt-data\n  statistics:\n  - about: MC_RTT fully nested gain\n    test: condition-stratified whole-trial bootstrap interval, conditional on one session and fitted model\n    ci:\n      level: 0.95\n      low: 0.05371\n      high: 0.08478\n    n: 270 validation blocks\n  expected:\n  - quantity: context-only R2\n    value: 0.6031\n    tolerance: 0.06031\n  - quantity: fully nested gain\n    value: 0.06846\n    tolerance: 0.01632\n    unit: delta R2\n  - quantity: context RMSE\n    value: 39.78\n    tolerance: 3.978\n    unit: released velocity units\n  - quantity: context-plus-neural RMSE\n    value: 36.19\n    tolerance: 3.619\n    unit: released velocity units\n  - quantity: percentage MSE reduction\n    value: 17.25\n    tolerance: 1.725\n    unit: percent\n  - quantity: gain, first velocity component\n    value: 0.0836\n    tolerance: 0.00836\n    unit: delta R2\n  - quantity: gain, second velocity component\n    value: 0.0513\n    tolerance: 0.00513\n    unit: delta R2\n  - quantity: nearest-replacement gain\n    value: -0.02297\n    tolerance: 0.002297\n    unit: delta R2\n  criterion: Fully nested estimator on the release split, five 20 ms spike bins ending 80 ms\n    before behavior, headline context of Methods 4.4 (run_primary_analyses.py, _run_nlb, estimator\n    seed 20260726). The gain tolerance is the larger distance to a bound of the paper's interval.\n    Component gains use each component's variance (Methods 4.9), components in the file's column\n    order. Reproduced when the gain is within tolerance and positive, the replacement gain is\n    negative, and at least six of the other seven values are within tolerance.\n- id: maze-gain\n  statement: In MC_Maze, a condition-by-phase template with geometry gave context-only R2 of\n    0.9053, and the fully nested neural gain beyond it was 0.00051 (conditional interval 0.00026\n    to 0.00076), a 0.54% MSE reduction (RMSE 81.76 to 81.53), with replacement gain -0.00004.\n  source: Results 2.6, paragraph 2; Table 1; Figure 4c\n  quote: a condition-by-phase template and geometry achieved context-only R2 = 0.9053. Fully\n    nested neural gain was 0.00051 (conditional 95% whole-trial interval, [0.00026, 0.00076]),\n    corresponding to a 0.54% reduction in context-model MSE and RMSE 81.76 to 81.53\n  data: elsewhere\n  where: DANDI:000139 version 0.220113.0408, sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb\n  statistics:\n  - about: MC_Maze fully nested gain\n    test: condition-stratified whole-trial bootstrap interval, conditional on one session and fitted model\n    ci:\n      level: 0.95\n      low: 0.00026\n      high: 0.00076\n    n: 62 validation trials\n  expected:\n  - quantity: context-only R2\n    value: 0.9053\n    tolerance: 0.09053\n  - quantity: fully nested gain\n    value: 0.00051\n    tolerance: 0.00025\n    unit: delta R2\n  - quantity: percentage MSE reduction\n    value: 0.54\n    tolerance: 0.054\n    unit: percent\n  - quantity: replacement gain\n    value: -0.00004\n    tolerance: 0.000004\n    unit: delta R2\n  criterion: Not on this attempt's datasets. MC_Maze-medium, 40 bins after measured movement\n    onset, five spike bins ending 80 ms before behavior, 258-feature template context (Methods 4.3\n    and 4.4; mc_maze.py).\n- id: rff-rtt\n  statement: Under three prespecified nonlinear-neural random-feature maps, MC_RTT gain stayed\n    positive (0.01491 to 0.01685).\n  source: Results 2.6, paragraph 4; Figure 6c\n  quote: whereas MC_RTT remained positive (0.01491-0.01685)\n  datasets:\n  - \"000129\"\n  depends_on:\n  - rtt-gain\n  expected:\n  - quantity: lowest MC_RTT gain over the three maps\n    value: 0.01491\n    tolerance: 0.001491\n    unit: delta R2\n  - quantity: highest MC_RTT gain over the three maps\n    value: 0.01685\n    tolerance: 0.001685\n    unit: delta R2\n  criterion: Fully nested linear nuisances, standardized residual neural histories mapped to\n    D = 512 radial-basis random Fourier features with W ~ N(0, 2 gamma), gamma = 1/p (g = 1),\n    b ~ Uniform(0, 2 pi), Ridge penalty by three-fold grouped validation on out-of-fold residual\n    trials, map seeds 20260802, 20260803, 20260804 (Methods 4.6; nested_estimators.py,\n    evaluate_nonlinear_neural_audit; run_nonlinear_seed_sensitivity.py). Methods 4.6 writes\n    gamma = g/p with p the context feature count, read with the code as applying to the neural\n    features it maps. The range holds inside 0.01491 to 0.01685 widened by 10% of each bound;\n    reproduced when all three map gains are positive and inside it.\n- id: rff-maze\n  statement: Under the three nonlinear-neural maps, MC_Maze gain stayed practically zero (0.000045\n    to 0.000139).\n  source: Results 2.6, paragraph 4; Figure 6c\n  quote: MC_Maze remained practically zero (gain range, 0.000045-0.000139)\n  data: elsewhere\n  where: DANDI:000139 version 0.220113.0408, sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb\n  expected:\n  - quantity: lowest MC_Maze gain over the three maps\n    value: 0.000045\n    tolerance: 0.0000045\n    unit: delta R2\n  - quantity: highest MC_Maze gain over the three maps\n    value: 0.000139\n    tolerance: 0.0000139\n    unit: delta R2\n  criterion: Not on this attempt's datasets. As rff-rtt.\n- id: rff-link\n  statement: In LINK SBP, nonlinear-neural geometry-by-phase means were positive for both tasks\n    under every map (combined range 0.00310 to 0.00404), and the measured-output-history mean\n    ranged from 0.00111 to 0.00142.\n  source: Results 2.6, paragraph 4; Figure 6c; Figure 5a\n  quote: In LINK SBP, nonlinear-neural geometry means were positive for both tasks under every map\n    (combined range, 0.00310-0.00404), and the measured-output-history mean ranged from 0.00111\n    to 0.00142.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  expected:\n  - quantity: lowest combined geometry-by-phase mean over the three maps\n    value: 0.0031\n    tolerance: 0.00031\n    unit: delta R2\n  - quantity: highest combined geometry-by-phase mean over the three maps\n    value: 0.00404\n    tolerance: 0.000404\n    unit: delta R2\n  - quantity: lowest plus-history mean over the three maps\n    value: 0.00111\n    tolerance: 0.000111\n    unit: delta R2\n  - quantity: highest plus-history mean over the three maps\n    value: 0.00142\n    tolerance: 0.000142\n    unit: delta R2\n  criterion: As rff-rtt, on the 18 development sessions, SBP only (Figure 5 legend). \"Combined\" is\n    the mean over the 18 sessions. Reproduced when the CO and RD geometry means are positive under\n    every map and the combined geometry and history means of every map fall inside their ranges\n    widened by 10% of each bound.\n- id: estimator-family-link\n  statement: Separately penalized context and neural blocks and nonlinear context random features\n    retained positive LINK task means, with magnitudes that differed between estimator families.\n  source: Results 2.6, paragraph 5; Figure 5a\n  quote: Separately penalized context and neural blocks and nonlinear context random features\n    retained positive LINK task means\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  - nested-history-gain\n  criterion: Block penalties minimize the objective of Methods 4.5 with lambda_C and lambda_X\n    chosen separately from the grid; nonlinear context augments standardized context with\n    random Fourier features (Methods 4.6). The release has no run script for these, and the\n    Methods do not say how the penalties are selected for the block model or which of the\n    nonlinear-context settings (D = 128, 256, 512; three map seeds; g in 0.25, 1, 4) Figure 5\n    shows. Readings for the nonlinear context, (a) every setting, (b) D = 256 and seed 20260726\n    with g chosen per session from the three values by inner validation, as the frozen\n    rff_capacity_sensitivity.csv baseline rows suggest. For the block model, penalties chosen\n    jointly on the inner 80/20 split of the outer-training trials (as for the nuisances). \"Task\n    means\" are read as the four signal-by-context means of Figure 5a (SBP and TCR, geometry by\n    phase and plus history). Reproduced when all are positive for both families under a reading.\n- id: estimator-family-nlb\n  statement: Under the separate-block and nonlinear-context estimators, MC_RTT gain remained\n    positive while MC_Maze remained near zero.\n  source: Results 2.6, paragraph 5; Figure 5b\n  quote: MC_Maze remained near zero, and MC_RTT remained positive\n  datasets:\n  - \"000129\"\n  depends_on:\n  - rtt-gain\n  - estimator-family-link\n  criterion: The MC_RTT part is tested here; the MC_Maze part needs DANDI:000139 (data\n    elsewhere) and is reported only if that file is used. Estimators as in estimator-family-link,\n    with its readings. Reproduced when the MC_RTT gain is positive under both families. For\n    MC_Maze, if run, \"near zero\" is read as an absolute gain below 0.01, the code's gate for the\n    primary MC_Maze result (run_primary_analyses.py, maze_abs_gain_below_0_01).\n- id: temporal-offset\n  statement: Shifting both the neural and the measured-output histories back by 40, 80 and 120 ms\n    with the behavioral window fixed reduced the small output-history-conditional gain and\n    changed the RD direction at intermediate offsets.\n  source: Results 2.7, paragraph 1; Figure 7a\n  quote: Holding the behavioral window fixed and shifting both neural and measured-output\n    histories to offsets 0, 40, 80, and 120 ms reduced the small output-history-conditional gain\n    and changed the RD direction at intermediate offsets (Figure 7).\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-history-gain\n  criterion: LINK SBP, geometry by phase plus measured-output history, 18 development sessions,\n    fully nested estimator, CO and RD means at offsets 0, 40, 80 and 120 ms (the offset is the\n    gap between the end of both histories and the behavior bin; link.py neural_lead_ms and\n    output_lead_ms). The release has no script for this run. Holding the window fixed is read\n    as one window start for all offsets, the earliest that the 120 ms offset allows (eight SBP\n    bins plus six offset bins, 280 ms after the trial start bin; link.py sample_offset_ms), so\n    the gain at offset 0 here differs from nested-history-gain. \"Reduced\" is read as the gain\n    at 120 ms below that at 0 ms for both tasks. \"Changed the RD direction\" is open; readings\n    (a) the RD mean gain is negative at 40 or 80 ms, (b) the RD minus CO difference at 40 or 80\n    ms has the opposite sign to that at 0 ms. Reproduced when the reduction holds and a reading\n    of the RD change holds.\n- id: split-seed-stability\n  statement: The fully nested SBP geometry-by-phase result was stable across three whole-trial\n    split and refitting seeds, with CO means 0.0193, 0.0180 and 0.0158 and RD means 0.0209,\n    0.0223 and 0.0201.\n  source: Results 2.7, paragraph 2; Figure 7b\n  quote: CO means were 0.0193, 0.0180, and 0.0158; RD means were 0.0209, 0.0223, and 0.0201.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  expected:\n  - quantity: CO mean, seed 1\n    value: 0.0193\n    tolerance: 0.00193\n    unit: delta R2\n  - quantity: CO mean, seed 2\n    value: 0.018\n    tolerance: 0.0018\n    unit: delta R2\n  - quantity: CO mean, seed 3\n    value: 0.0158\n    tolerance: 0.00158\n    unit: delta R2\n  - quantity: RD mean, seed 1\n    value: 0.0209\n    tolerance: 0.00209\n    unit: delta R2\n  - quantity: RD mean, seed 2\n    value: 0.0223\n    tolerance: 0.00223\n    unit: delta R2\n  - quantity: RD mean, seed 3\n    value: 0.0201\n    tolerance: 0.00201\n    unit: delta R2\n  criterion: Seeds 20260726, 20260727, 20260728 for the outer split and all refitting\n    (run_primary_analyses.py, SEEDS). Reproduced when all six means are positive and at least\n    five are within tolerance.\n- id: context-capacity-contrast\n  statement: Adding quadratic geometry to the context changed the descriptive RD-minus-CO gain\n    contrast, and the richest quadratic-history context gave a small positive contrast for both\n    SBP and TCR.\n  source: Results 2.7, paragraph 2; Figure 7c\n  quote: Adding quadratic geometry changed the descriptive RD-minus-CO contrast, and the richest\n    quadratic-history specification yielded a small positive contrast for both SBP and TCR.\n  datasets:\n  - \"001201\"\n  depends_on:\n  - nested-geometry-gain\n  criterion: Contexts linear geometry by phase (141 features), quadratic (351), linear plus\n    history (151), quadratic plus history (361) (Methods 4.4; link.py geometry_quadratic and\n    causal_history_quadratic). The release has no script for this run; the fully nested\n    estimator is assumed, as for the other development results, and the Figure 7c intervals are\n    paired date-bootstrap intervals (as in link-task-contrast-by-context). The paper calls these\n    exploratory. Reproduced when the quadratic-plus-history mean RD minus CO difference is\n    positive for SBP and for TCR, and, for at least one signal, the quadratic-geometry contrast\n    differs from the linear-geometry contrast in sign or in whether its 95% interval excludes\n    zero (the paper gives no measure of \"changed\"; these are the two readings).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/du-2026.yaml paper/10.64898-2026.08.04.742876.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "—|rather" claims/du-2026.yaml; grep -c "criterion:" claims/du-2026.yaml; grep -c "statistics:" claims/du-2026.yaml; git status --short
```

```
32
4
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
?? claims/du-2026.yaml
?? scripts
```

**Agent**

I wrote `claims/du-2026.yaml`. The checker reports 33 claims, 32 quotes, 12 statistical values and 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering submission). I read the main text, figure legends, Tables 1 to 3, the Methods and the data and code availability statements. No PDF was supplied.

**Supplement missing.** The Supplementary information is not under `paper/`, and it is not in the code release either. No claim needs its numbers, so I wrote the claims. One main-text sentence points to supplement values (replacement with source ranks one to five, and with a random source). That claim is judged by direction only.

**Code read.** I read `github.com/gwkuqgfkqe/neural-decoder-context-audit` at tag v1.0-jne-submission, commit b042fbe1. It settled several details the Methods leave out:
- LINK trial windows start 160 ms after the trial start bin; the outcome is index plus middle-ring-small finger velocity.
- The outer split seed is 20260726, and the split-sensitivity runs use seeds 20260726 to 20260728.
- Neural-only R2 uses an inner 80/20 penalty selection.
- The date-cluster bootstrap uses 10,000 resamples of dates.
- The confirmation sessions are listed in a frozen manifest in the release.

The release has no run scripts for the temporal-offset, quadratic-capacity, block-penalty or nonlinear-context analyses, only their frozen output tables.

**Claims**
- 32 have quotes. One, the confirmation values printed only in Table 1, is `inferred`.
- 4 have statistics: date-clustered 95% intervals for LINK, and conditional whole-trial intervals for MC_RTT and MC_Maze. The paper reports no p-values.
- 32 have criteria.
- Datasets:
  - 24 rest on 001201 (LINK).
  - 4 rest on 000129 (MC_RTT).
  - 5 are `data: elsewhere`: three synthetic-calibration claims (data generated by the paper's code) and two MC_Maze claims (DANDI:000139, which is not one of this attempt's datasets).

**Details left open, with the readings named**
- **"Near zero" for the geometry-by-phase RD-minus-CO contrast:** (a) its date-bootstrap interval contains zero; (b) its absolute value is smaller than under direction-by-phase and under additive geometry.
- **Which sessions the permutation and rank-replacement sentences cover:** (a) SBP geometry sessions only; (b) SBP and TCR.
- **"No consistent rank relation" between replacement penalty and source distance:** (a) the per-session Spearman correlations are not all of one sign; (b) the across-session mean correlation has a date-bootstrap interval that contains zero.
- **Random-source draw:** a uniform draw among same-condition test trials, a standard choice; three draws are shown.
- **Figure 8 rule:** which of the two middle sessions out of 18 counts as the median. "Trial 123" could index (a) the NWB trials table, (b) the usable trials, or (c) the held-out trials.
- **Nonlinear-context sensitivity (Figure 5):** (a) every setting; (b) the configuration in the release's frozen table.
- **Block-penalty sensitivity:** the Methods do not say how its two penalties are selected; the criterion assumes the same inner 80/20 selection as the nuisance models.
- **Temporal offsets:** the fixed window start is read as 280 ms after the trial start bin, the earliest the 120 ms offset allows. "Changed the RD direction" is read as (a) the RD gain goes negative at 40 or 80 ms, or (b) the RD-minus-CO sign flips relative to 0 ms.
- **"Changed" for the quadratic-capacity contrast:** (a) a change of sign; (b) a change in whether the interval excludes zero.
- **"Near zero" for MC_Maze:** the code's gate, an absolute gain below 0.01. This is reported only if 000139 is used.
- **Nonlinear-neural map scale:** the Methods write gamma as g/p with p the context feature count; I read it with the code, as applying to the mapped neural features.

**Missing from the paper.** Only the supplement, which no claim needed for its values. Two things are not missing but limit testing: MC_Maze is outside this attempt's datasets, and the synthetic data exist only through the paper's code.

## End of run

35 turns, 6 minutes, $2.52 at API prices, result: success.
