# yang-2026-flexible · claims · run 45004283606

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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-eneuro.0275-26.2026.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper && python3 -c "
s=open('10.1523-eneuro.0275-26.2026.txt').read()
print(s[59000:])" | fold -w 2000 | head -c 45000
```

```
<persisted-output>
Output too large (41.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7ee15d95-1c09-4dc8-8a55-856e18bbbe89/tool-results/bbm55bjx8.txt

Preview (first 2KB):
endritic and axonal architecture shape electrotonic structure and the spatial distribution of membrane conductances and could contribute both to the relatively stable organization associated with cell type and to regime-dependent electrophysiological expression through its interaction with the subcellular localization of ion channels and other membrane components. Morphology was not explicitly incorporated into the present framework, which was designed to isolate relationships between electrophysiological response regimes and transcriptomic identity. Integrating morphology, transcriptomic state, and regime-specific electrophysiology within a common relational framework will be important for determining which layers of cellular organization underlie stable versus flexible components of phenotype. Type-level organization is more stable than its cellular expression The strongest evidence for this separation emerged when the analysis moved from individual cells to relationships among transcriptomic types. Although local cell neighborhoods were substantially reorganized across response regimes, type-centroid relationships remained substantially concordant, and the broader subclass organization was more conserved still. Individual cells can move relative to one another across response regimes while population-level relationships among biological types remain recoverable: type identity provides a relational scaffold rather than a fixed cellular coordinate, and the electrophysiological expression of a type can vary with the stimulus used to interrogate the cell even while the relative organization among types remains comparatively stable. This type-level conservation was reduced when centroids were estimated from equal numbers of cells per type, particularly for
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python3 -c "
s=open('paper/10.1523-eneuro.0275-26.2026.txt').read()
i=s.find('Type-level organization is more stable than its cellular expression')
j=s.find('References',i)
print(len(s), i, j)
print(s[i:i+12000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/zy-neuro/protocol-response-geometry 2>&1 | tail -3; cd protocol-response-geometry && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
61a5a413daea3b3562fad6e40207320da5665fed Mon Oct 19 09:36:19 2026 -0400
./requirements.txt
./configs/q3_curated_excitability_genes.txt
./LICENSE
./results/phenotype/brief_pulse_pca_scores.csv
./results/phenotype/ramp_pca_loadings.csv
./results/phenotype/phenotype_summary.json
./results/phenotype/long_pulse_pca_loadings.csv
./results/phenotype/ramp_pca_scores.csv
./results/phenotype/long_pulse_pca_scores.csv
./results/phenotype/ramp_pca_variance.csv
./results/phenotype/long_pulse_pca_variance.csv
./results/phenotype/brief_pulse_pca_loadings.csv
./results/phenotype/brief_pulse_pca_variance.csv
./results/q1_reliability/split_half_jaccard_cells.csv
./results/q1_reliability/split_half_summary.json
./results/q1_reliability/split_half_summary.csv
./results/q3c/q3c_module_tests.csv
./results/q3_mobility/wgcna_soft_threshold.csv
./results/q3_mobility/mobility_scores.csv
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && cat README.md requirements.txt scripts/paths.py; wc -l scripts/* configs/*
```

````
# protocol-response-geometry

Analysis code and derived tables for:

Yang Z. Flexible cellular phenotypes retain a shared type-level organization across response regimes. *eNeuro* (in press).

## Environment

Python 3.9 (NumPy 1.23, Matplotlib 3.9) on macOS (Apple Silicon). Figure regeneration:

```
pip install -r requirements.txt
```

SciPy is used only by `scripts/q3_mobility_modules.py`. Re-extracting split-half features from NWB needs IPFX / PyNWB. Reconstructing WGCNA modules needs R and WGCNA 1.74.

## Data

Raw data are not included.

[... 68 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && cat scripts/q1_describe_phenotype.py
```

```
#!/usr/bin/env python3
"""Q1 DESCRIBE: cellular phenotype organization across regimes.

No molecular or Cre labels enter the statistics.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PHENO = ROOT / "results/phenotype"
OUT = ROOT / "results/q1"
SEED = 0
N_SHUFFLE = 100
[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && cat scripts/q2_anchor.py
```

```
#!/usr/bin/env python3
"""Q2 ANCHOR: is cellular phenotype organization biologically anchored?

Primary: A_p = Spearman(D^mol, D^phenotype).
Control: Cre alignment and within-Cre / Cre-residual t-type tests.
No S_p model comparison here (that is Q3).
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PHENO = ROOT / "results/phenotype"
[... 415 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && cat scripts/q3a_explain.py
```

```
#!/usr/bin/env python3
"""Q3a EXPLAIN: shared vs selective t-type relationships.

Canonical script (k80, same as Q1/Q2). Writes results/q3a/.
S_p = Euclidean distance of t-type centroids.
Tags use rank-normalized S across the three regimes.
Model call is not Brief-centric.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PHENO = ROOT / "results/phenotype"
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && cat scripts/q3bc_explain.py
```

```
<persisted-output>
Output too large (30.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7ee15d95-1c09-4dc8-8a55-856e18bbbe89/tool-results/bk7vjvxr6.txt

Preview (first 2KB):
#!/usr/bin/env python3
"""Q3b/c EXPLAIN: transcriptomic dimensions and pre-specified modules.

Q3b: RNA PCA → type-centroid distances T(a,b) vs Q3a S_p / pair tags.
Q3c: few pre-specified excitability / marker programs only — no genome-wide fishing.

Uses Q3a pair tags in results/q3a/.
"""

from __future__ import annotations

import csv
import json
import math
import os
from collections import Counter, defaultdict
[... 44 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7ee15d95-1c09-4dc8-8a55-856e18bbbe89/tool-results/bk7vjvxr6.txt"
}
```

```
1	#!/usr/bin/env python3
2	"""Q3b/c EXPLAIN: transcriptomic dimensions and pre-specified modules.
3	
4	Q3b: RNA PCA → type-centroid distances T(a,b) vs Q3a S_p / pair tags.
5	Q3c: few pre-specified excitability / marker programs only — no genome-wide fishing.
6	
7	Uses Q3a pair tags in results/q3a/.
8	"""
9	
10	from __future__ import annotations
11	
12	import csv
13	import json
14	import math
15	import os
16	from collections import Counter, defaultdict
17	from pathlib import Path
18	
19	os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-prg")
20	
[... 777 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && grep -n "1000\|N_SHUFFLE\|N_PERM\|N_RES\|SEED" scripts/*.py scripts/*.R | grep -v "^scripts/q3bc_explain\|^scripts/q2_anchor\|^scripts/q1_describe" | head -40; cat scripts/q1_knn_scale.py | sed -n 1,175p
```

```
scripts/figures_eneuro_supplement.py:38:CONC_1000 = REPO / "results/q3a_robustness/concordance_null_1000.csv"
scripts/figures_eneuro_supplement.py:39:Q3B_PRIMARY_1000 = REPO / "results/q3b/q3b_primary_null_1000.csv"
scripts/figures_eneuro_supplement.py:937:    # Q3a — manuscript / Statistical Table j–l use the 1000 type-label shuffles
scripts/figures_eneuro_supplement.py:944:    conc1000 = {r["pair"]: r for r in load_csv(CONC_1000)} if CONC_1000.exists() else {}
scripts/figures_eneuro_supplement.py:947:        r1k = conc1000.get(key)
scripts/figures_eneuro_supplement.py:959:                "extra": f"n_types={r['n_types']}; 1000 type-label shuffles; Statistical_Table={letter[key]}"
scripts/figures_eneuro_supplement.py:977:    # Q3b — primary panel in the manuscript uses the 1000-shuffle file (Statistical Table m–n)
scripts/figures_eneuro_supplement.py:978:    primary_1000 = {r["contrast"]: r for r in load_csv(Q3B_PRIMARY_1000)} if Q3B_PRIMARY_1000.exists() else {}
scripts/figures_eneuro_supplement.py:980:        is_primary = r["panel"] == "primary" and primary_1000
scripts/figures_eneuro_supplement.py:981:        mean_null = primary_1000["T_vs_mean_S"] if is_primary else None
scripts/figures_eneuro_supplement.py:982:        range_null = primary_1000["T_vs_rank_range"] if is_primary else None
scripts/figures_eneuro_supplement.py:992:                "extra": f"n_genes={r['n_genes']}; 1000 shuffles; Statistical_Table=m" if mean_null else f"n_genes={r['n_genes']}",
scripts/figures_eneuro_supplement.py:1004:                "extra": f"n_genes={r['n_genes']}; 1000 shuffles; Statistical_Table=n" if range_null else f"n_genes={r['n_genes']}",
scripts/figures_eneuro_supplement.py:1072:                "extra": "residual |rho|<=0.039; no module with |rho|>=0.10 and emp p<0.05; Statistical_Table=y; 1000 label shuffles",
scripts/q1_knn_scale.py:20:SEED = 0
scripts/q1_knn_scale.py:21:N_SHUFFLE = 100
scripts/q1_knn_scale.py:109:    rng = np.random.default_rng(SEED)
scripts/q1_knn_sc
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && grep -rn "null_1000" scripts/ ; head -3 results/q3a_robustness/concordance_null_1000.csv results/q3b/q3b_primary_null_1000.csv | cut -c1-300; sed -n 1,140p scripts/q3a_centroid_robustness.py
```

```
scripts/figures_eneuro_supplement.py:38:CONC_1000 = REPO / "results/q3a_robustness/concordance_null_1000.csv"
scripts/figures_eneuro_supplement.py:39:Q3B_PRIMARY_1000 = REPO / "results/q3b/q3b_primary_null_1000.csv"
scripts/q3a_centroid_robustness.py:336:    write_csv(OUT / "concordance_null_1000.csv", null_rows)
scripts/q3a_centroid_robustness.py:363:        "concordance_null_1000": null_rows,
==> results/q3a_robustness/concordance_null_1000.csv <==
pair,observed_rho,null_mean,null_sd,empirical_p,n_shuffle
long_ramp,0.6575095911546857,-0.00298610764027863,0.05885979052901089,0.000999000999000999,1000
long_brief,0.45515907178530046,-0.011961893103390717,0.06479513657706307,0.000999000999000999,1000

==> results/q3b/q3b_primary_null_1000.csv <==
contrast,rho,null_mean,emp_p_one_sided,n_shuffle
T_vs_mean_S,0.5074492871980676,0.0006582590843465648,0.000999000999000999,1000
T_vs_rank_range,0.08327999801759017,0.0008981632822366412,0.000999000999000999,1000
#!/usr/bin/env python3
"""Q3a robustness: equal-N centroid resampling + within-regime S reliability.

Addresses the aggregation critique: is cross-regime type–type S concordance
only a trivial consequence of centroid averaging / unequal n?

Writes results/q3a_robustness/ and a manuscript-facing landing note.
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && sed -n 140,340p scripts/q3a_centroid_robustness.py
```

```
M = np.asarray(mus, dtype=float)
    nrm = np.sum(M * M, axis=1, keepdims=True)
    d2 = nrm + nrm.T - 2.0 * (M @ M.T)
    np.maximum(d2, 0.0, out=d2)
    S = np.sqrt(d2)
    np.fill_diagonal(S, 0.0)
    return S


def upper(S: np.ndarray) -> np.ndarray:
    i, j = np.triu_indices(S.shape[0], k=1)
    return S[i, j]


def sample_equal_n(by_type: dict[str, np.ndarray], types: list[str], n_draw: int, rng: np.random.Generator) -> dict[str, np.ndarray] | None:
    take = {}
    for t in types:
        idx = by_type[t]
        if idx.size < n_draw:
            return None
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && sed -n 1,120p scripts/q1_split_half_long_square.py; grep -n "def \|chance\|zscore\|z-score\|mean_full\|loadings" scripts/q1_split_half_long_square.py | sed -n 1,80p
```

```
#!/usr/bin/env python3
"""within-regime split-half neighborhood reliability.

Split usable long-square sweeps into two disjoint halves, extract IPFX
long-square features on each half, project into the ORIGINAL long-pulse
phenotype space (full-cell z-score + PCA; halves do not enter the fit),
and compare 15-NN Jaccard of half-A vs half-B with cross-regime 15-NN
Jaccard for the same cells.

Writes results/q1_reliability/ only.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import sys
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && sed -n 130,330p scripts/q1_split_half_long_square.py; sed -n 419,470p scripts/q1_split_half_long_square.py; sed -n 537,640p scripts/q1_split_half_long_square.py
```

```
def repair_nwb_epochs() -> None:
    from ipfx.sweep import Sweep

    if getattr(Sweep.__init__, "_prg_epoch_repair", False):
        return
    original = Sweep.__init__

    def patched(self, t, v, i, clamp_mode, sampling_rate, sweep_number=None, epochs=None):
        if epochs:
            epochs = {k: val for k, val in epochs.items() if val is not None}
        original(self, t, v, i, clamp_mode, sampling_rate, sweep_number=sweep_number, epochs=epochs)

    patched._prg_epoch_repair = True
    Sweep.__init__ = patched


def _ok_split(a: list[int], b: list[int]) -> bool:
    return len(a) >= MIN_SWEEPS_PER_HALF and len(b) >= MIN_SWEEPS_PER_HALF


[... 338 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && python3 -c "
import json;d=json.load(open('results/phenotype/phenotype_summary.json'))
for p,v in d.items():
  print(p, {k:(v[k] if not isinstance(v[k],(list,dict)) else len(v[k])) for k in v} if isinstance(v,dict) else v)
  if isinstance(v,dict) and 'features' in v: print(v['features'])
"
```

```
long_pulse {'n_cells': 4344, 'n_features': 42, 'k80': 11, 'features': 42, 'scores': 'results/phenotype/long_pulse_pca_scores.csv'}
['feat.long_squares.vrest', 'feat.long_squares.ri', 'feat.long_squares.sag', 'feat.long_squares.tau', 'feat.long_squares.vm_for_sag', 'feat.long_squares.f_i_curve_slope', 'feat.long_squares.adaptation', 'feat.long_squares.latency', 'feat.long_squares.avg_isi', 'feat.long_squares.upstroke_downstroke_ratio', 'feat.long_squares.peak_v', 'feat.long_squares.peak_t', 'feat.long_squares.trough_v', 'feat.long_squares.trough_t', 'feat.long_squares.fast_trough_v', 'feat.long_squares.fast_trough_t', 'feat.long_squares.threshold_v', 'feat.long_squares.threshold_i', 'feat.long_squares.threshold_t', 'feat.long_squares.v_baseline', 'feat.long_squares.rheobase_i', 'feat.long_squares.rheobase_sweep.avg_rate', 'feat.long_squares.rheobase_sweep.stim_amp', 'feat.long_squares.rheobase_sweep.v_baseline', 'feat.long_squares.rheobase_sweep.sag', 'feat.long_squares.rheobase_sweep.latency', 'feat.long_squares.rheobase_sweep.index', 'feat.long_squares.rheobase_sweep.sweep_number', 'feat.long_squares.fi_fit_slope', 'feat.long_squares.hero_sweep.avg_rate', 'feat.long_squares.hero_sweep.stim_amp', 'feat.long_squares.hero_sweep.v_baseline', 'feat.long_squares.hero_sweep.sag', 'feat.long_squares.hero_sweep.adapt', 'feat.long_squares.hero_sweep.latency', 'feat.long_squares.hero_sweep.isi_cv', 'feat.long_squares.hero_sweep.mean_isi', 'feat.long_squares.hero_sweep.median_isi', 'feat.long_squares.hero_sweep.first_isi', 'feat.long_squares.hero_sweep.index', 'feat.long_squares.hero_sweep.sweep_number', 'feat.long_squares.input_resistance']
ramp {'n_cells': 4139, 'n_features': 20, 'k80': 3, 'features': 20, 'scores': 'results/phenotype/ramp_pca_scores.csv'}
['feat.ramps.upstroke_downstroke_ratio', 'feat.ramps.peak_v', 'feat.ramps.peak_t', 'feat.ramps.trough_v', 'feat.ramps.trough_t', 'feat.ramps.fast_trough_v', 'feat.ramps.fast_trough_t', 'feat.ramps.threshold_v', 'feat.ramps.
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && grep -n "def \|mobility\b" scripts/q3_mobility_modules.py | head -50; sed -n 30,120p scripts/q3_mobility_modules.py
```

```
2:"""cell-level mobility and weighted co-expression modules.
9:Writes results/q3_mobility/ only. Does not change Q3 type-level claims.
43:def read_gene_list(path: Path) -> list[str]:
52:def load_csv(path: Path) -> list[dict]:
57:def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None) -> None:
69:def pc_cols(fieldnames: list[str]) -> list[str]:
74:def load_k80(path: Path, n_available: int) -> int:
84:def load_scores(path: Path) -> tuple[list[str], np.ndarray]:
98:def pairwise_euclidean(x: np.ndarray) -> np.ndarray:
108:def spearman(a: np.ndarray, b: np.ndarray) -> float:
122:def spearman_p(rho: float, n: int) -> float:
129:def empirical_spearman_p(x: np.ndarray, y: np.ndarray, rng: np.random.Generator, n: int) -> float:
142:def residualize_by_group(x: np.ndarray, groups: np.ndarray) -> np.ndarray:
151:def nemo_counts_csv() -> Path:
159:def load_counts(path: Path, keep_samples: list[str]) -> tuple[list[str], np.ndarray, list[str]]:
188:def log_cpm(counts: np.ndarray) -> np.ndarray:
194:def scale_free_r2(connectivity: np.ndarray) -> float:
213:def pick_soft_threshold(corr_abs: np.ndarray, betas=(1, 2, 3, 4, 5, 6, 8, 10, 12)) -> tuple[int, dict]:
234:def topological_overlap(adj: np.ndarray) -> np.ndarray:
245:def cut_modules(tom: np.ndarray, min_size: int = MIN_MODULE_SIZE) -> tuple[np.ndarray, float]:
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && sed -n 129,150p scripts/q3_mobility_modules.py; sed -n 289,312p scripts/q3_mobility_modules.py; sed -n 1,60p scripts/q3_wgcna_mobility.py; grep -n "power\|minModuleSize\|mergeCut\|networkType\|RsquaredCut\|corType\|TOMType" scripts/q3_wgcna_modules.R
```

```
def empirical_spearman_p(x: np.ndarray, y: np.ndarray, rng: np.random.Generator, n: int) -> float:
    obs = spearman(x, y)
    if not np.isfinite(obs):
        return float("nan")
    count = 0
    y_work = y.copy()
    for _ in range(n):
        rng.shuffle(y_work)
        if abs(spearman(x, y_work)) >= abs(obs):
            count += 1
    return (1.0 + count) / (1.0 + n)


def residualize_by_group(x: np.ndarray, groups: np.ndarray) -> np.ndarray:
    out = np.asarray(x, dtype=float).copy()
    for g in np.unique(groups):
        m = groups == g
        mu = np.nanmean(out[m])
        out[m] = out[m] - mu
    return out
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1523-eneuro.0275-26.2026.txt').read()
i=s.find('Synthesis Reviewing Editor')
j=s.find(' References ',i)
print(i,j,len(s))
t=s[i:]
print(t[3000:18000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1523-eneuro.0275-26.2026.txt').read()
import re
t=s[83289:]
k=t.find('Zeng')
print(t[k:k+300]); print('----'); print(t[k+300:k+4000]); print('...'); print(t[-2500:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p claims/fouke-2025.yaml
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "kind\|data:" claims/yang-2026.yaml | head; head -30 claims/yang-2026.yaml
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

[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:9000])"
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
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/yang-2026-flexible.yaml 2>/dev/null; grep -n "yang-2026-flexible" -r papers/keys.yaml | head
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1523/eneuro.0275-26.2026
title: Flexible Cellular Phenotypes Retain a Shared Type-Level Organization across Response Regimes
datasets:
- archive: dandi
  id: '000020'
  relation: reuses
282:  10.1523/eneuro.0275-26.2026: yang-2026-flexible
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && grep -n "cutoff\|linspace\|arange\|thresholds\|0\.55\|0\.25" scripts/figures_eneuro_supplement.py | head -30; grep -n "def chance_jaccard" -A8 scripts/q1_split_half_long_square.py; git log --oneline | head
```

```
69:STABLE_RANK_CV = 0.25
70:SELECTIVE_RANK_RANGE = 0.55
197:    xs = np.arange(3)
212:    ylim_from_zero(ax, max(ns), pad=0.25)
278:    xs = np.arange(3)
381:        ax.barh(np.arange(len(vals)), vals, color=colors, edgecolor=PCOL[p], lw=0.6, height=0.72)
382:        ax.set_yticks(np.arange(len(vals)))
472:    xs = np.arange(len(rows_plot))
476:    ax.bar(xs, obs, 0.55, color=fills, edgecolor=cols, lw=0.9)
512:    ys = np.arange(len(names))
539:    xs = np.arange(3)
548:    ax.bar(xs + 1.5 * w, a_r, w, color=soft_bar(LAB_T_CRE, 0.55), edgecolor=LAB_T_CRE, lw=0.8, label="A_t|Cre")
553:    ylim_from_zero(ax, 0.25, pad=0)
565:    ys = np.arange(len(lp))
600:    ranges = [0.45, 0.50, 0.55, 0.60, 0.65]
611:    ax.set_xlabel("Selective rank-range cutoff")
617:    cvs = [0.15, 0.20, 0.25, 0.30, 0.35]
628:    ax.set_xlabel("Stable rank-CV cutoff")
638:    xs = np.arange(3)
640:    ax.bar(xs, [float(r["spearman_S"]) for r in sub], 0.55, color=[soft_bar(c, PAIR_FILL) for c in edges], edgecolor=edges, lw=0.9)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/protocol-response-geometry && sed -n 347,420p scripts/q3_mobility_modules.py; sed -n 60,200p scripts/q3_wgcna_mobility.py | grep -n "resid\|keep\|>= 3\|MIN\|abs" ; sed -n 30,100p scripts/q3_wgcna_modules.R
```

```
# RNA join: cells with mobility + sample id + t-type
    keep_samples = []
    stem_by_sample = {}
    ttype_by_sample = {}
    mob_by_sample = {}
    for rec, mob in zip(score_rows, mobility):
        sid = rec["transcriptomics_sample_id"]
        tt = rec["t_type"]
        if not sid or not tt:
            continue
        keep_samples.append(sid)
        stem_by_sample[sid] = rec["file_stem"]
        ttype_by_sample[sid] = tt
        mob_by_sample[sid] = float(mob)
    keep_samples = sorted(set(keep_samples))
    print(f"Mobility cells with RNA+t-type: {len(keep_samples)}", flush=True)

    genes, counts, samples = load_counts(nemo_counts_csv(), keep_samples)
    print(f"Loaded counts {counts.shape} (genes x cells)", flush=True)
    expr_all = log_cpm(counts)
[... 140 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/yang-2026-flexible.yaml",
 "content": "# Claims for Yang (2026), \"Flexible Cellular Phenotypes Retain a Shared Type-Level Organization\n# across Response Regimes\", eNeuro 13(11) ENEURO.0275-26.2026, doi:10.1523/eneuro.0275-26.2026,\n# on DANDI 000020 (Allen Institute Patch-seq of mouse visual cortex GABAergic neurons, Gouwens et\n# al. 2020), which the paper reuses.\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-22, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. The version of record, from paper/10.1523-eneuro.0275-26.2026.txt (PMC13737997):\n# abstract, Significance Statement, Introduction, Materials and Methods, Results, Discussion,\n# Table 1, Table 2 (statistical summary, rows a to y), the legends of Figures 1 to 4 and of the\n# Extended Data (Figures 1-1 to 1-3, 2-1, 3-1 to 3-3, 4-1 to 4-4; Tables 1-1 and 2-1), and the\n# synthesis of the reviews. The Extended Data files themselves (TIF figures, DOCX Tables 1-1,\n# 2-1, 3-1, 4-1, 4-3) are not in the text and no PDF was supplied; only their legends were read.\n# No claim rests on a number printed only in them: every expected value below is printed in the\n# Results, the Methods or Table 2. The retained feature lists of Extended Data Table 1-1 are\n# taken from the paper's code (below). The paper prints \"Table 2 (rows a-y)\" superscript letters\n# after its values; they appear in the quotes as stray letters (\"0.434 a\").\n#\n# Code read. https://github.com/zy-neuro/protocol-response-geometry, commit 61a5a41 (2026-10-19),\n# deposited as Extended Data 1. It holds the analysis scripts (scripts/q1_describe_phenotype.py,\n# q1_knn_scale.py, q1_split_half_long_square.py, q2_anchor.py, q3a_explain.py,\n# q3a_centroid_robustness.py, q3bc_explain.py, q3_mobility_modules.py, q3_wgcna_mobility.py,\n# q3_wgcna_modules.R, figure scripts), the curated gene list\n# (configs/q3_curated_excitability_genes.txt) and derived tables under results/: the per-regime\n# PCA scores, loadings and variance, the retained feature names\n# (results/phenotype/phenotype_summary.json), and the metadata join\n# (results/m0/m0_molecular_join.csv, keyed by NWB file stem, with t_type, subclass, cre_line and\n# transcriptomics_sample_id). It does not hold the script that ran IPFX on all cells to make the\n# cell-level feature table (results/features/ipfx_cell_features.csv is referred to but absent),\n# nor the script that wrote results/q3b/q3b_primary_null_1000.csv. Where the Methods leave a\n# choice open and the code settles it, the criteria follow the code and say so. Common to all\n# scripts: seed 0 (numpy default_rng); Euclidean distance; Spearman correlation computed as the\n# Pearson correlation of ordinal ranks from np.argsort(np.argsort(x)), so ties get distinct\n# ranks in an order the sort leaves arbitrary (this matters for the binary label distances of\n# the A_t claims; see there); population standard deviation (ddof 0) for z-scores and CVs.\n#\n# Data the paper used (Methods, Dataset and animals; Electrophysiological feature extraction;\n# Protocol-resolved cellular phenotype; Molecular labels). DANDI 000020, version 0.210913.1639,\n# 4,435 files with the suffix _icephys.nwb, one per cell, current-clamp recordings of GABAergic\n# interneurons (mostly VISp) from male and female Cre-driver mice (about P45 to P70). Three\n# stimulus families are treated as response regimes: long-pulse (long squares), ramp, and\n# brief-pulse (short squares). Cell-level features come from the Allen Institute IPFX package\n# (extract_ok = 1), with empty NWB2 epoch fields dropped so that IPFX recovers the stimulus and\n# experiment windows. Each regime has its own z-scored feature matrix and PCA, kept to k80\n# components (long-pulse 4,344 cells, 42 features, k80 = 11; ramp 4,139, 20, 3; brief-pulse\n# 4,422, 21, 5). Example cell, DANDI session 639797293 (Figure 1A). Cells are matched across\n# regimes and to labels by NWB file stem.\n#\n# Outside data (step 4). The transcriptomic labels (t-type, subclass) and the Cre line are\n# taken from the joined Allen metadata of the NeMO Patch-seq release 20200611, and the gene\n# counts from its count matrix v2 (file 20200513_Mouse_PatchSeq_Release_count.v2.csv), at\n# https://data.nemoarchive.org/other/AIBS/AIBS_patchseq/transcriptome/scell/SMARTseq/processed/analysis/20200611\n# (README of the code). The paper's join of these to the NWB files is the code's\n# results/m0/m0_molecular_join.csv. Claims that need labels or counts are data: with_inputs.\n# Whether the NWB files carry the Cre line or t-type themselves is the author's to find.\n#\n# Statistics. Every p-value in the paper is an empirical permutation p, (1 + number of null\n# values >= observed)/(1 + number of permutations); with no null value reaching the observed,\n# it is 0.0099 for 100 shuffles, 0.020 for 50 and 0.000999 for 1,000 (Results, end; Table 2).\n# These floors are recorded as printed. Tolerances are 10% of each reported value unless a claim\n# says otherwise; for integers whose 10% is below 1 (k80 of 3 and 5) this means the value must\n# match exactly.\nschema_version: 2\npaper: doi:10.1523/eneuro.0275-26.2026\nclaims:\n- id: cohort-label-join\n  statement: Of the cells, 4,430 have a row in the joined metadata table and 4,266 a non-empty\n    t-type; the cells with a t-type number 4,183 in long-pulse, 3,988 in ramp and 4,266 in\n    brief-pulse.\n  source: Methods, Dataset and animals, last sentence; Figure 2 legend\n  quote: >-\n    n = 4,430 cells with a join row; n = 4,266 with a non-empty t-type) ... Cell n with t-type:\n    long-pulse 4,183; ramp 3,988; brief-pulse 4,266\n  data: with_inputs\n  depends_on:\n  - table1-phenotype-spaces\n  expected:\n  - quantity: cells with a metadata join row\n    value: 4430\n    tolerance: 443\n  - quantity: cells with a non-empty t-type\n    value: 4266\n    tolerance: 426.6\n  - quantity: long-pulse cells with a t-type\n    value: 4183\n    tolerance: 418.3\n  - quantity: ramp cells with a t-type\n    value: 3988\n    tolerance: 398.8\n  - quantity: brief-pulse cells with a t-type\n    value: 4266\n    tolerance: 426.6\n  criterion: Cells are matched to the NeMO/Allen metadata by NWB file stem, as the code's\n    results/m0/m0_molecular_join.csv does; a cell has a t-type when its t_type field is non-empty\n    (scripts/q2_anchor.py, protocol_anchor). The per-regime counts are the cells of each regime's\n    phenotype space (claim table1-phenotype-spaces) that have a t-type. Reproduced when all five\n    counts are within tolerance.\n- id: table1-phenotype-spaces\n  statement: Built independently per regime, the phenotype spaces hold 4,344 long-pulse cells\n    with 42 features and k80 = 11 components, 4,139 ramp cells with 20 features and k80 = 3, and\n    4,422 brief-pulse cells with 21 features and k80 = 5; the same-cell overlaps are 4,054\n    (long-pulse and ramp), 4,336 (long-pulse and brief-pulse), 4,134 (ramp and brief-pulse) and\n    4,049 (all three).\n  source: Methods, Protocol-resolved cellular phenotype, paragraph 1; Table 1; Results,\n    Cellular phenotypes are partially conserved, paragraph 1\n  quote: >-\n    Resulting dataset sizes are summarized in Table 1 (long-pulse: 4,344 cells, 42 features, k\n    80 = 11; ramp: 4,139 cells, 20 features, k 80 = 3; brief-pulse: 4,422 cells, 21 features, k\n    80 = 5) ... Same-cell overlaps for cross-regime comparisons were as follows: long-pulse ∩\n    ramp, n = 4,054; long-pulse ∩ brief-pulse, n = 4,336; ramp ∩ brief-pulse, n = 4,134; and\n    triple overlap, n = 4,049\n  data: dataset\n  expected:\n  - quantity: long-pulse cells\n    value: 4344\n    tolerance: 434.4\n  - quantity: long-pulse retained features\n    value: 42\n    tolerance: 4.2\n  - quantity: long-pulse k80\n    value: 11\n    tolerance: 1.1\n  - quantity: ramp cells\n    value: 4139\n    tolerance: 413.9\n  - quantity: ramp retained features\n    value: 20\n    tolerance: 2\n  - quantity: ramp k80\n    value: 3\n    tolerance: 0.3\n  - quantity: brief-pulse cells\n    value: 4422\n    tolerance: 442.2\n  - quantity: brief-pulse retained features\n    value: 21\n    tolerance: 2.1\n  - quantity: brief-pulse k80\n    value: 5\n    tolerance: 0.5\n  - quantity: cells shared by long-pulse and ramp\n    value: 4054\n    tolerance: 405.4\n  - quantity: cells shared by long-pulse and brief-pulse\n    value: 4336\n    tolerance: 433.6\n  - quantity: cells shared by ramp and brief-pulse\n    value: 4134\n    tolerance: 413.4\n  - quantity: cells in all three regimes\n    value: 4049\n    tolerance: 404.9\n  criterion: >-\n    Method from the Methods (Electrophysiological feature extraction; Protocol-resolved cellular\n    phenotype) and the code. IPFX cell-level features per NWB file, with empty epoch fields\n    dropped before IPFX builds its sweeps (the patch in scripts/q1_split_half_long_square.py,\n    repair_nwb_epochs), and only sweeps with both an experiment and a stim epoch used; cells with\n    extract_ok = 1. Per regime, numeric features with at most 30% missing and nonzero variance;\n    missing entries imputed with the feature mean; columns z-scored (population SD); PCA by SVD;\n    k80 the smallest number of components reaching 80% cumulative variance. The retained feature\n    names are those of results/phenotype/phenotype_summary.json in the code (42 long-square, 20\n    ramp, 21 short-square features, named feat.<regime>.<IPFX key>, including the sweep index\n    and sweep number fields of the rheobase and hero sweeps, which the code kept); the author\n    first applies the paper's rule and reports whether it gives the same lists. Open, and named\n    as readings since they can move the counts. (1) The script that ran IPFX on all cells is not\n    in the code, so the IPFX version and call are not fixed; reading (a) is IPFX's\n    extract_data_set_features (or its per-regime parts, as the split-half script does for long\n    squares) with features flattened as the split-half script's _pack_long_square_features does\n    (the cell feature record plus the regime's nested feature dictionary, without the spike and\n    sweep lists); the IPFX version is the current release, with the one of the Allen pipeline\n    as a variant. (2) Which cells enter a regime and the denominator of the 30% missing rule; (a)\n    as the code's fit_full_cell_pca in scripts/q1_split_half_long_square.py, cells with\n    extract_ok = 1 and at least one non-missing value among that regime's features, with\n    missingness counted among them; (b) missingness counted over all extract_ok cells. Cells\n    are matched across regimes by NWB file stem. Reproduced when, under one reading, all values\n    are within tolerance; partially reproduced when the k80 values and feature counts match and\n    some cell count does not.\n- id: pc1-long-pulse-loadings\n  statement: Long-pulse PC1 loads most strongly on rheobase or threshold current and on input\n    resistance.\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 1; Extended Data\n    Figure 1-2D\n  quote: >-\n    Long-pulse PC1, used here only as a within-regime axis, loads most strongly on\n    rheobase/threshold current and input resistance\n  data: dataset\n  depends_on:\n  - table1-phenotype-spaces\n  criterion: Loadings of PC1 from the SVD of the z-scored long-pulse feature matrix, features\n    ranked by absolute loading, as the Extended Data Figure 1-2 legend says. Current features are\n    threshold_i, rheobase_i and rheobase_sweep.stim_amp; input resistance features are ri and\n    input_resistance. The paper does not say how far down the ranking \"most strongly\" reaches;\n    readings are (a) the two highest-ranked distinct quantities are a rheobase or threshold\n    current and an input resistance; (b) both kinds are among the five features with the\n    largest absolute loadings. Reproduced under either reading.\n- id: fig1b-distance-correlation\n  statement: Pairwise cell-cell phenotypic distances are positively correlated across all three\n    regime pairs, above shuffle and well below identity, strongest for long-pulse and ramp\n    (Spearman rho 0.434), then ramp and brief-pulse (0.384), then long-pulse and brief-pulse\n    (0.336).\n  source: Results, Cellular phenotypes are partially conserved, paragraph 2; Figure 1B; Table 2\n    rows a to c\n  quote: >-\n    Conservation was strongest between long-pulse and ramp responses (Spearman's ρ = 0.434 a , n\n    = 4,054 shared cells), followed by ramp and brief-pulse responses ( ρ = 0.384 b , n = 4,134)\n    and long-pulse and brief-pulse responses ( ρ = 0.336 c , n = 4,336; Fig. 1 B )\n  statistics:\n  - about: long-pulse against ramp\n    test: Spearman correlation of pairwise distances, empirical p against 100 index shuffles\n    statistic: rho = 0.434\n    p: 0.0099\n    n: 4,054 shared cells, up to 80,000 sampled cell pairs\n  - about: ramp against brief-pulse\n    test: Spearman correlation of pairwise distances, empirical p against 100 index shuffles\n    statistic: rho = 0.384\n    p: 0.0099\n    n: 4,134 shared cells\n  - about: long-pulse against brief-pulse\n    test: Spearman correlation of pairwise distances, empirical p against 100 index shuffles\n    statistic: rho = 0.336\n    p: 0.0099\n    n: 4,336 shared cells\n  data: dataset\n  depends_on:\n  - table1-phenotype-spaces\n  expected:\n  - quantity: Spearman rho of distances, long-pulse and ramp\n    value: 0.434\n    tolerance: 0.0434\n  - quantity: Spearman rho of distances, ramp and brief-pulse\n    value: 0.384\n    tolerance: 0.0384\n  - quantity: Spearman rho of distances, long-pulse and brief-pulse\n    value: 0.336\n    tolerance: 0.0336\n  criterion: Method from the Methods (Cross-regime phenotypic organization) and\n    scripts/q1_describe_phenotype.py (align_pair). On each pair's shared cells, Euclidean\n    distances in each regime's k80 score space; 80,000 cell pairs sampled with seed 0; Spearman\n    correlation of the two distance vectors; null by permuting the cell indices of the second\n    regime 100 times, p = (1 + nulls >= observed)/101. The Methods say \"unique\" pairs while the\n    code draws random i < j pairs, which can repeat; the Methods reading (unique pairs) is the\n    main one and the code's draw a variant (it cannot change the outcome). Reproduced when all\n    three rho are within tolerance, each has p < 0.05, and the order long-ramp > ramp-brief >\n    long-brief holds.\n- id: fig1-fixed-five-pcs-ordering\n  statement: The ordering of cross-regime distance correlations is unchanged when a fixed five\n    principal components are kept in each regime instead of k80.\n  source: Results, Cellular phenotypes are partially conserved, paragraph 2; Extended Data\n    Figure 1-2A\n  quote: >-\n    this ordering was unchanged when a fixed number of five principal components was retained\n    instead of the 80% variance threshold\n  data: dataset\n  depends_on:\n  - fig1b-distance-correlation\n  criterion: As fig1b-distance-correlation with the first five components in every regime\n    (scripts/q1_describe_phenotype.py, FIXED_K = 5; ramp then uses five components although its\n    k80 is 3). Reproduced when the order long-ramp > ramp-brief > long-brief of the three rho\n    holds.\n- id: fig1c-knn-jaccard\n  statement: Local neighborhoods are much less stable; the mean Jaccard overlap of each cell's\n    15 nearest neighbors across regimes is 0.023 (long-pulse and ramp), 0.022 (long-pulse and\n    brief-pulse) and 0.019 (ramp and brief-pulse), only modestly above index-shuffle chance of\n    about 0.002.\n  source: Results, Cellular phenotypes are partially conserved, paragraph 3; Figure 1C\n  quote: >-\n    mean 15-nearest-neighbor Jaccard overlap was 0.023, 0.022, and 0.019 for the\n    long-pulse–ramp, long-pulse–brief-pulse, and ramp–brief-pulse pairs, only modestly above\n    index-shuffle chance (≈0.002; Fig. 1 C )\n  data: dataset\n  depends_on:\n  - table1-phenotype-spaces\n  expected:\n  - quantity: mean 15-NN Jaccard, long-pulse and ramp\n    value: 0.023\n    tolerance: 0.0023\n  - quantity: mean 15-NN Jaccard, long-pulse and brief-pulse\n    value: 0.022\n    tolerance: 0.0022\n  - quantity: mean 15-NN Jaccard, ramp and brief-pulse\n    value: 0.019\n    tolerance: 0.0019\n  - quantity: chance mean Jaccard under index shuffle\n    value: 0.002\n    tolerance: 0.0002\n  criterion: Method from the Methods (Cross-regime phenotypic organization), the Figure 1C\n    legend and scripts/q1_knn_scale.py. On each pair's shared cells, each cell's 15 nearest\n    neighbors (itself excluded) by Euclidean distance in each regime's k80 space; per-cell\n    Jaccard of the two neighbor sets; the mean over cells. Chance is the mean over 100 index\n    shuffles (seed 0) of the mean Jaccard after permuting the cell order of the second regime's\n    neighbor lists. Distance ties in the neighbor search are broken as np.argpartition does, a\n    standard choice that cannot change the outcome. The paper's chance is printed as about\n    0.002; it is reproduced when each pair's chance is within 0.0002 of 0.002 or rounds to it.\n    Reproduced when the three means and the chance are within tolerance.\n- id: knn-scale-sweep\n  statement: Across neighborhood sizes k = 15 to 600, chance-adjusted overlap rises with k but\n    stays low even at k = 600 (0.134, 0.101 and 0.108 for long-pulse and ramp, long-pulse and\n    brief-pulse, ramp and brief-pulse).\n  source: Results, Cellular phenotypes are partially conserved, paragraph 3; Extended Data\n    Figure 1-2B,C; Table 2 row w\n  quote: >-\n    chance-adjusted overlap increased with neighborhood size but remained low even at k = 600\n    (0.134, 0.101, and 0.108 for the same three pairs w )\n  data: dataset\n  depends_on:\n  - fig1c-knn-jaccard\n  expected:\n  - quantity: chance-adjusted Jaccard at k = 600, long-pulse and ramp\n    value: 0.134\n    tolerance: 0.0134\n  - quantity: chance-adjusted Jaccard at k = 600, long-pulse and brief-pulse\n    value: 0.101\n    tolerance: 0.0101\n  - quantity: chance-adjusted Jaccard at k = 600, ramp and brief-pulse\n    value: 0.108\n    tolerance: 0.0108\n  criterion: As fig1c-knn-jaccard at k = 15, 30, 60, 120, 240, 480 and 600, chance-adjusted\n    overlap being the observed mean Jaccard minus the mean over 100 index shuffles (Methods,\n    Cross-regime phenotypic organization; scripts/q1_knn_scale.py). \"Increased with\n    neighborhood size\" is open between (a) a rise at every step of the k grid for each pair and\n    (b) a higher value at k = 600 than at k = 15 for each pair. Reproduced when the three k =\n    600 values are within tolerance and the rise holds under one reading.\n- id: split-half-reliability\n  statement: Within long-pulse, neighborhoods built from two disjoint halves of each cell's\n    sweeps overlap more (mean 15-NN Jaccard 0.109, chance about 0.0026, adjusted 0.107, 3,598\n    cells) than cross-regime neighborhoods in the same pool (0.025, 0.024 and 0.020), but far\n    from completely.\n  source: Results, Cellular phenotypes are partially conserved, paragraph 4; Extended Data\n    Figure 1-3; Table 2 rows u and v; Methods, Cross-regime phenotypic organization\n  quote: >-\n    On the 3,598 cells with both halves successfully extracted, mean 15-NN Jaccard overlap\n    between half-A and half-B was 0.109 (chance ≈ 0.0026; chance-adjusted 0.107 u ), compared\n    with 0.025, 0.024, and 0.020 v for the long-pulse–ramp, long-pulse–brief-pulse, and\n    ramp–brief-pulse pairs recomputed in that pool\n  data: dataset\n  depends_on:\n  - table1-phenotype-spaces\n  - fig1c-knn-jaccard\n  expected:\n  - quantity: cells with both halves extracted\n    value: 3598\n    tolerance: 359.8\n  - quantity: within-regime half-A against half-B mean 15-NN Jaccard\n    value: 0.109\n    tolerance: 0.0109\n  - quantity: within-regime chance-adjusted Jaccard\n    value: 0.107\n    tolerance: 0.0107\n  - quantity: chance Jaccard for the split halves\n    value: 0.0026\n    tolerance: 0.00026\n  - quantity: same-pool cross-regime 15-NN Jaccard, long-pulse and ramp\n    value: 0.025\n    tolerance: 0.0025\n  - quantity: same-pool cross-regime 15-NN Jaccard, long-pulse and brief-pulse\n    value: 0.024\n    tolerance: 0.0024\n  - quantity: same-pool cross-regime 15-NN Jaccard, ramp and brief-pulse\n    value: 0.020\n    tolerance: 0.002\n  - quantity: same-pool cells, long-pulse and ramp\n    value: 3276\n    tolerance: 327.6\n  - quantity: same-pool cells, long-pulse and brief-pulse\n    value: 3509\n    tolerance: 350.9\n  - quantity: same-pool cells, ramp and brief-pulse\n    value: 3351\n    tolerance: 335.1\n  - quantity: cells split odd/even by sweep number\n    value: 3112\n    tolerance: 311.2\n  - quantity: cells split by random split\n    value: 358\n    tolerance: 35.8\n  criterion: >-\n    Method from the Methods (Cross-regime phenotypic organization, paragraph 2) and\n    scripts/q1_split_half_long_square.py. Cells with at least four usable long-square sweeps\n    (current clamp, with both experiment and stim epochs after the epoch repair); candidate\n    splits tried in order odd/even sweep number, interleaved by sweep-number rank, interleaved by\n    stimulus-amplitude rank (when amplitudes are available), random (seed 0), each half needing\n    at least two sweeps; IPFX extract_cell_long_square_features on each half with the cell's\n    subthreshold minimum amplitude from select_subthreshold_min_amplitude over the coarse long\n    squares; the first candidate where both halves succeed is kept. Half features are put in the\n    retained long-pulse feature columns, missing values filled with the full-cell feature mean,\n    z-scored with the full-cell mean and SD, and projected onto the full-cell PCA loadings (k80 =\n    11). 15-NN Jaccard between the two half positions; chance as the mean over 100 index\n    shuffles; the cross-regime 15-NN Jaccard recomputed among the split-half cells present in\n    both regimes of each pair. Paper's split counts are odd/even 3,112, sweep-number interleaved\n    128, amplitude-interleaved 0 and random 358; the 128 and 0 are reported, not judged (10% of\n    them is below a few cells). IPFX version open, as in table1-phenotype-spaces. Reproduced\n    when the within-regime mean and the three same-pool cross-regime means are within\n    tolerance and the within-regime mean exceeds each cross-regime mean; partially reproduced\n    when within exceeds cross for all three pairs but some value is out of tolerance.\n- id: fig2c-eta2-ttype-over-cre\n  statement: T-type accounts for more multivariate phenotypic variance than Cre line in every\n    regime (eta squared 0.327 against 0.209 long-pulse, 0.393 against 0.267 ramp, 0.149 against\n    0.110 brief-pulse).\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 2; Figure 2C\n  quote: >-\n    T-type accounted for more multivariate phenotypic variance than Cre identity in every\n    response regime ( η 2 = 0.327 vs 0.209 long-pulse; 0.393 vs 0.267 ramp; 0.149 vs 0.110\n    brief-pulse; Fig. 2 C )\n  data: with_inputs\n  depends_on:\n  - cohort-label-join\n  expected:\n  - quantity: eta squared of t-type, long-pulse\n    value: 0.327\n    tolerance: 0.0327\n  - quantity: eta squared of Cre line, long-pulse\n    value: 0.209\n    tolerance: 0.0209\n  - quantity: eta squared of t-type, ramp\n    value: 0.393\n    tolerance: 0.0393\n  - quantity: eta squared of Cre line, ramp\n    value: 0.267\n    tolerance: 0.0267\n  - quantity: eta squared of t-type, brief-pulse\n    value: 0.149\n    tolerance: 0.0149\n  - quantity: eta squared of Cre line, brief-pulse\n    value: 0.110\n    tolerance: 0.011\n  criterion: Multivariate eta squared as the Methods (Biological anchoring) define it, between-\n    group sum of squared distances of group means from the grand mean, weighted by group size,\n    over the total sum of squares, in each regime's k80 score space. T-type on the cells with a\n    t-type. For Cre the Methods say \"the same cells that had a Cre label\"; the code\n    (scripts/q2_anchor.py, protocol_anchor) uses the cells with both a t-type and a Cre line.\n    Readings are (a) the code's set and (b) all cells with a Cre line. Reproduced when, under\n    one reading, the six values are within tolerance and t-type exceeds Cre in each regime;\n    partially reproduced when t-type exceeds Cre in every regime but some value is out of\n    tolerance.\n- id: table2-alignment-ttype\n  statement: Pairwise alignment of binary t-type mismatch with phenotypic distance is small in\n    all three regimes (A_t 0.021 long-pulse, 0.025 ramp, 0.021 brief-pulse) but exceeds\n    shuffled labels in each.\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 2; Extended Data\n    Figure 2-1A; Table 2 rows d to f\n  quote: >-\n    Pairwise transcriptomic–phenotypic alignment was small in all three regimes ( A t = 0.021 d ,\n    0.025 e , and 0.021 f for long-pulse, ramp, and brief-pulse, respectively) but consistently\n    exceeded shuffled controls\n  statistics:\n  - about: long-pulse\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.021\n    p: 0.0099\n    n: 4,183 cells\n  - about: ramp\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.025\n    p: 0.0099\n    n: 3,988 cells\n  - about: brief-pulse\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.021\n    p: 0.0099\n    n: 4,266 cells\n  data: with_inputs\n  depends_on:\n  - cohort-label-join\n  expected:\n  - quantity: A_t long-pulse\n    value: 0.021\n    tolerance: 0.0021\n  - quantity: A_t ramp\n    value: 0.025\n    tolerance: 0.0025\n  - quantity: A_t brief-pulse\n    value: 0.021\n    tolerance: 0.0021\n  criterion: Method from the Methods (Biological anchoring) and scripts/q2_anchor.py (align_D).\n    On the cells with a t-type, D_mol is 1 for a pair of different t-types and 0 otherwise;\n    80,000 cell pairs sampled (seed 0); A_t is the Spearman correlation of D_mol with the k80\n    phenotypic distance over those pairs; null by permuting cell labels 100 times, p = (1 +\n    nulls >= observed)/101. The Methods say only \"Spearman correlation\". The code ranks with\n    np.argsort(np.argsort(x)), giving the tied 0s and 1s of D_mol distinct ranks in an\n    arbitrary order, which shrinks the correlation of a binary variable well below the\n    tie-corrected (average-rank) Spearman. The code settles the choice, so its ordinal ranking\n    is the main reading; the average-rank Spearman is shown as a variant and is expected to be\n    larger. Reproduced when, under the code's ranking, the three values are within tolerance\n    and each has p < 0.05; partially reproduced when all three exceed their null at p < 0.05 and\n    some value is out of tolerance.\n- id: ttype-beyond-cre\n  statement: After removing each Cre line's mean phenotype, t-type alignment stays above the\n    shuffled-label null in all three regimes, though weaker (A_t 0.011, 0.010 and 0.004 for\n    long-pulse, ramp and brief-pulse), and residual t-type eta squared remains detectable.\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 2; Figure 2C;\n    Extended Data Figure 2-1A; Table 2 rows g to i\n  quote: >-\n    residual t-type structure remained detectable after removing Cre-associated structure in all\n    three regimes ... this alignment remained above the shuffled-label null, though weaker and,\n    for brief-pulse, very small ( A t = 0.011 g , 0.010 h , 0.004 i ; Extended Data Fig. 2-1 )\n  statistics:\n  - about: long-pulse, after Cre residualization\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.011\n    p: 0.0099\n    n: 4,183 cells\n  - about: ramp, after Cre residualization\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.010\n    p: 0.0099\n    n: 3,988 cells\n  - about: brief-pulse, after Cre residualization\n    test: Spearman A_t, empirical p against 100 label shuffles\n    statistic: A_t = 0.004\n    p: 0.0099\n    n: 4,266 cells\n  data: with_inputs\n  depends_on:\n  - table2-alignment-ttype\n  - fig2c-eta2-ttype-over-cre\n  expected:\n  - quantity: A_t after Cre residualization, long-pulse\n    value: 0.011\n    tolerance: 0.0011\n  - quantity: A_t after Cre residualization, ramp\n    value: 0.010\n    tolerance: 0.001\n  - quantity: A_t after Cre residualization, brief-pulse\n    value: 0.004\n    tolerance: 0.0004\n  criterion: Method from the Methods (Biological anchoring, residual t-type structure) and\n    scripts/q2_anchor.py. Within each Cre line, that line's mean score vector is subtracted from\n    its cells; A_t and eta squared of t-type are recomputed on the residualized scores, with the\n    same 100-shuffle null and the same ordinal-rank Spearman as table2-alignment-ttype. The code\n    does this on the cells with both a t-type and a Cre line (Table 2 prints the t-type counts as\n    n); that set is the reading used, with all t-typed cells (those without a Cre line left\n    unresidualized) as a variant. The paper prints no residual eta squared value; \"detectable\"\n    is judged as residual eta squared greater than the mean of a 100-shuffle t-type label null on\n    the residualized scores, the null the Methods name for these analyses (\"Label-shuffle null\n    distributions used 100 permutations\"). Reproduced when the three A_t are within tolerance\n    with p < 0.05 and residual eta squared exceeds its null in each regime; partially reproduced\n    when every A_t has p < 0.05 but some value is out of tolerance. The brief-pulse tolerance\n    (0.0004) is 10% of a value that is itself small.\n- id: fig2d-knn-type-enrichment\n  statement: Cells are enriched for phenotypic neighbors of their own t-type, most for\n    long-pulse (6.59-fold), then ramp (3.44-fold) and brief-pulse (2.64-fold).\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 2; Figure 2D\n  quote: >-\n    Cells were also enriched for neighbors sharing their t-type relative to chance, with\n    enrichment strongest for long-pulse (6.59-fold), followed by ramp (3.44-fold) and\n    brief-pulse (2.64-fold; Fig. 2 D )\n  data: with_inputs\n  depends_on:\n  - cohort-label-join\n  expected:\n  - quantity: same-t-type 15-NN enrichment, long-pulse\n    value: 6.59\n    tolerance: 0.659\n  - quantity: same-t-type 15-NN enrichment, ramp\n    value: 3.44\n    tolerance: 0.344\n  - quantity: same-t-type 15-NN enrichment, brief-pulse\n    value: 2.64\n    tolerance: 0.264\n  criterion: On the cells with a t-type in each regime, each cell's 15 nearest neighbors in k80\n    space; the fraction sharing its t-type; chance for cell i is (n_type(i) - 1)/(n - 1)\n    (Methods, Biological anchoring). The Methods leave open whether the enrichment is the mean of\n    per-cell ratios or a ratio of means; the code (scripts/q2_anchor.py, knn_same_label) takes\n    the mean fraction over cells divided by the mean chance over cells, and that is the main\n    reading, with the mean of per-cell ratios as a variant. Reproduced when the three values\n    are within tolerance and the order long-pulse > ramp > brief-pulse holds.\n- id: fig2ab-ttype-structure-within-cre\n  statement: T-types occupy distinct but overlapping parts of phenotype space, and finer t-type\n    structure remains within single Cre-driver populations; within Sst-IRES-Cre the six most\n    frequent t-types occupy distinct positions on long-pulse PC1.\n  source: Results, Transcriptomic type anchors cellular phenotype, paragraph 1; Figure 2A,B and\n    legend; Extended Data Figure 2-1B\n  quote: >-\n    transcriptomic identities occupied distinct but overlapping portions of phenotype space, and\n    finer t-type structure remained apparent within individual Cre-driver populations\n  data: with_inputs\n  depends_on:\n  - cohort-label-join\n  criterion: The paper gives no test for Figure 2B. Its own statistic for t-type structure\n    within a Cre line is the within-Cre analysis of scripts/q2_anchor.py, which the Figure 2\n    legend points to (\"additional within-Cre analyses are reported in Extended Data Figure 2-1\"),\n    computed for Cre lines with at least 80 cells and at least two t-types; within-Cre A_t (as\n    in table2-alignment-ttype, 100-shuffle null) and within-Cre eta squared of t-type, in\n    long-pulse k80 space. Reproduced when, for Sst-IRES-Cre in long-pulse, within-Cre A_t has p\n    < 0.05 and the within-Cre eta squared of t-type exceeds the mean of a 100-shuffle label null.\n    The medians on long-pulse PC1 of its six most frequent t-types, and a Kruskal-Wallis test\n    across them, are shown as descriptive variants, not judged, since the paper names no test.\n- id: fig3a-type-map-concordance\n  statement: Among the 57 t-types with at least 10 cells in every regime (1,596 type pairs),\n    type-type centroid distance maps are concordant across all three regime pairs, strongest for\n    long-pulse and ramp (rho 0.658), then ramp and brief-pulse (0.608), then long-pulse and\n    brief-pulse (0.455).\n  source: Results, Type-level phenotypic relationships, paragraphs 1 and 2; Figure 3A; Table 2\n    rows j to l\n  quote: >-\n    Analyses were restricted to 57 t-types represented by at least 10 cells in each response\n    regime, yielding 1,596 shared type pairs ... Concordance was strongest between long-pulse\n    and ramp responses (Spearman's ρ = 0.658 j , n = 1,596 type pairs, empirical p = 0.000999),\n    followed by ramp and brief-pulse responses ( ρ = 0.608 k , empirical p = 0.000999) and\n    long-pulse and brief-pulse responses ( ρ = 0.455 l , empirical p = 0.000999; Fig. 3 A )\n  statistics:\n  - about: long-pulse against ramp\n    test: Spearman concordance of type-type distance maps, empirical p against 1,000 type-label\n      shuffles\n    statistic: rho = 0.658\n    p: 0.000999\n    n: 1,596 type pairs\n  - about: ramp against brief-pulse\n    test: Spearman concordance of type-type distance maps, empirical p against 1,000 type-label\n      shuffles\n    statistic: rho = 0.608\n    p: 0.000999\n    n: 1,596 type pairs\n  - about: long-pulse against brief-pulse\n    test: Spearman concordance of type-type distance maps, empirical p against 1,000 type-label\n      shuffles\n    statistic: rho = 0.455\n    p: 0.000999\n    n: 1,596 type pairs\n  data: with_inputs\n  depends_on:\n  - cohort-label-join\n  expected:\n  - quantity: t-types with at least 10 cells in every regime\n    value: 57\n    tolerance: 5.7\n  - quantity: type-map concordance, long-pulse and ramp\n    value: 0.658\n    tolerance: 0.0658\n  - quantity: type-map concordance, ramp and brief-pulse\n    value: 0.608\n    tolerance: 0.0608\n  - quantity: type-map concordance, long-pulse and brief-pulse\n    value: 0.455\n    tolerance: 0.0455\n  criterion: Method from the Methods (Type-type relationships across regimes) and\n    scripts/q3a_explain.py with the 1,000-shuffle null of scripts/q3a_centroid_robustness.py.\n    In each regime, t-type centroids (mean k80 scores of the regime's t-typed cells) for the\n    t-types with at least 10 cells in all three regimes; S_p(a,b) the Euclidean distance\n    between centroids; concordance the Spearman correlation of the upper-triangle vectors of two\n    regimes. Null by permuting the t-type labels of the second regime's t-typed cells (all of\n    them, not only the 57 types) and rebuilding its centroids, 1,000 times (seed 0), p = (1 +\n    nulls >= observed)/1001. Reproduced when the type count and three rho are within tolerance,\n    each p < 0.05, and the order long-ramp > ramp-brief > long-brief holds.\n- id: shared-map-model-call\n  statement: The three type-map concordances meet the prespecified shared-map criterion (minimum\n    rho at least 0.40 and range across the three below 0.25).\n  source: Results, Type-level phenotypic relationships, paragraph 2; Methods, Type-type\n    relationships across regimes\n  quote: >-\n    All three comparisons satisfied our prespecified criterion for a shared-map model (minimum ρ\n    ≥ 0.40 and range <0.25)\n  data: with_inputs\n  depends_on:\n  - fig3a-type-map-concordance\n  criterion: The rule of the Methods and scripts/q3a_explain.py (call_model) applied to the\n    three rho of fig3a-type-map-concordance. Reproduced when the minimum is at least 0.40 and\n    the maximum minus the minimum is below 0.25.\n- id: subclass-map-concordance\n  statement: At the subclass level (six subclasses), type relationships are even more conserved\n    between long-pulse and ramp (rho 0.936) and moderately aligned for the comparisons with\n    brief-pulse (0.579 and 0.621).\n  source: Results, Type-level phenotypic relationships, paragraph 2; Extended Data Figure 3-2F\n  quote: >-\n    At the broader subclass level, phenotypic relationships were even more strongly conserved\n    between long-pulse and ramp responses ( ρ = 0.936, n = 6 subclasses) and remained moderately\n    aligned for comparisons involving brief-pulse stimulation (ρ = 0.579 and 0.621\n  data: with_inputs\n  depends_on:\n  - fig3a-type-map-concordance\n  expected:\n  - quantity: subclass map concordance, long-pulse and ramp\n    value: 0.936\n    tolerance: 0.0936\n  - quantity: subclass map concordance, first comparison with brief-pulse\n    value: 0.579\n    tolerance: 0.0579\n  - quantity: subclass map concordance, second comparison with brief-pulse\n    value: 0.621\n    tolerance: 0.0621\n  - quantity: shared subclasses\n    value: 6\n    tolerance: 0\n  criterion: As fig3a-type-map-concordance with the subclass label of the join in place of\n    t-type, keeping subclasses with at least 10 cells in a regime and, for each pair, the\n    subclasses kept in both (scripts/q3a_explain.py, subclass sensitivity). With six subclasses\n    there are 15 pairs. The tolerance on the count is 0, since the n is the definition of the\n    comparison. Which brief-pulse pair is 0.579 is open; readings are (a) long-pulse and\n    brief-pulse 0.579, ramp and brief-pulse 0.621, the code's pair order; (b) the reverse.\n    Reproduced when, under one reading, all values are within tolerance.\n- id: equal-n-centroid-robustness\n  statement: Rebuilt from 10 cells per type per regime (200 resamples), type-map concordance\n    drops for all three pairs (long-pulse and ramp mean 0.554, ramp and brief-pulse 0.455,\n    long-pulse and brief-pulse 0.329) but stays well above shuffled-label nulls.\n  source: Results, Type-level phenotypic relationships, paragraph 3; Extended Data Figure 3-3A\n  quote: >-\n    cross-regime concordance decreased relative to the full-sample estimates for all three\n    regime pairs (long-pulse–ramp: 0.658→mean 0.554, 95% interval 0.475–0.624; ramp–brief:\n    0.608→mean 0.455, 95% interval 0.353–0.539; long-pulse–brief: 0.455→mean 0.329, 95% interval\n    0.231–0.419) ... All three nonetheless remained well above shuffled-label nulls\n  statistics:\n  - about: long-pulse against ramp, equal-N mean\n    ci:\n      level: 0.95\n      low: 0.475\n      high: 0.624\n    n: 200 resamples of 10 cells per type per regime\n  - about: ramp against brief-pulse, equal-N mean\n    ci:\n      level: 0.95\n      low: 0.353\n      high: 0.539\n    n: 200 resamples\n  - about: long-pulse against brief-pulse, equal-N mean\n    ci:\n      level: 0.95\n      low: 0.231\n      high: 0.419\n    n: 200 resamples\n  data: with_inputs\n  depends_on:\n  - fig3a-type-map-concordance\n  expected:\n  - quantity: equal-N mean concordance, long-pulse and ramp\n    value: 0.554\n    tolerance: 0.07\n  - quantity: equal-N mean concordance, ramp and brief-pulse\n    value: 0.455\n    tolerance: 0.084\n  - quantity: equal-N mean concordance, long-pulse and brief-pulse\n    value: 0.329\n    tolerance: 0.09\n  criterion: Method from the Methods (Type-type relationships, last paragraph) and\n    scripts/q3a_centroid_robustness.py. For each of 200 resamples (seed 0), 10 cells drawn\n    without replacement per t-type per regime, centroids rebuilt, the three concordances\n    computed; the mean and the 2.5th and 97.5th percentiles over resamples. Tolerances are the\n    paper's stated spread, the distance from each mean to the nearer bound of its 95% interval.\n    \"Well above shuffled-label nulls\" is not given a test for the equal-N estimates; readings\n    are (a) each equal-N 2.5th percentile exceeds the largest value of the 1,000-shuffle null of\n    fig3a-type-map-concordance; (b) each equal-N mean exceeds the 97.5th percentile of that\n    null. Reproduced when the three means are within tolerance, each is below its full-sample\n    value, and the null comparison holds under one reading.\n- id: within-regime-type-map-reliability\n  statement: Within-regime split-half concordance of the type-type maps (long-pulse 0.861, ramp\n    0.851, brief-pulse 0.799) is well above the mean full-sample cross-regime concordance (about\n    0.57).\n  source: Results, Type-level phenotypic relationships, paragraph 3; Extended Data Figure 3-3B\n  quote: >-\n    Within-regime split-half S concordance was substantially higher than the mean full-sample\n    cross-regime value (long-pulse 0.861, ramp 0.851, brief-pulse 0.799; 200 resamples; Extended\n    Data Fig. 3-3 B )\n  data: with_inputs\n  depends_on:\n  - fig3a-type-map-concordance\n  expected:\n  - quantity: split-half S concordance, long-pulse\n    value: 0.861\n    tolerance: 0.0861\n  - quantity: split-half S concordance, ramp\n    value: 0.851\n    tolerance: 0.0851\n  - quantity: split-half S concordance, brief-pulse\n    value: 0.799\n    tolerance: 0.0799\n  - quantity: mean full-sample cross-regime concordance\n    value: 0.57\n    tolerance: 0.057\n  criterion: As scripts/q3a_centroid_robustness.py (within-regime reliability). In each of 200\n    resamples, each t-type's cells in the regime are randomly split into two halves of equal\n    size (floor of n/2 each), centroids built from each half, and the Spearman correlation of\n    the two upper-triangle S vectors taken; the value is the mean over resamples. The reference\n    is the mean of the three full-sample rho. Reproduced when the values are within tolerance and\n    each regime's split-half value exceeds the reference.\n- id: fig3b-pair-tags\n  statement: Of the 1,596 type pairs, 639 (40.0%) are stable, 801 (50.2%) intermediate and 156\n    (9.8%) regime-selective.\n  source: Results, Type-level phenotypic relationships, paragraph 4; Figure 3B\n  quote: >-\n    Of the 1,596 type pairs, 639 (40.0%) were classified as stable, 801 (50.2%) were classified\n    as intermediate, and 156 (9.8%) were classified as regime-selective ( Fig. 3 B )\n  data: with_inputs\n  depends_on:\n  - fig3a-type-map-concordance\n  expected:\n  - quantity: stable type pairs\n    value: 639\n    tolerance: 63.9\n  - quantity: intermediate type pairs\n    value: 801\n    tolerance: 80.1\n  - quantity: regime-selective type pairs\n    value: 156\n    tolerance: 15.6\n  criterion: Method from the Methods (Type-type relationships) and scripts/q3a_explain.py. In\n    each regime the 1,596 S values are rank-normalized (ordinal rank divided by 1,595); per pair,\n    the three normalized ranks give a CV (population SD over mean) and a range (max minus min). A\n    pair is stable when CV < 0.25, else selective when range >= 0.55, else intermediate (stable\n    is tested first, as the code does). Reproduced when the three counts are within tolerance.\n- id: pair-tag-threshold-sensitivity\n  statement: The proportions of stable, intermediate and selective pairs are stable under\n    modest variation of the classification thresholds.\n  source: Results, Type-level phenotypic relationships, paragraph 4; Extended Data Figure 3-2D,E\n  quote: >-\n    The proportions assigned to these categories were stable under modest variation of the\n    classification thresholds\n  data: with_inputs\n  depends_on:\n  - fig3b-pair-tags\n  criterion: The cutoff grids are those of the code's figure (scripts/figures_eneuro_supplement.py,\n    Extended Data Figure 3-2D,E); selective rank-range cutoffs 0.45, 0.50, 0.55, 0.60 and 0.65,\n    and stable rank-CV cutoffs 0.15, 0.20, 0.25, 0.30 and 0.35, each varied with the other held\n    at its default. The paper does not say what \"stable\" proportions means; readings are (a)\n    across each grid, the selective fraction stays below 20% and below the stable fraction\n    (the minority status the claim rests on); (b) across each grid, the varied fraction changes\n    by no more than 10 percentage points between neighboring cutoffs. Reproduced when both\n    readings hold; partially reproduced when one does. The fractions at every cutoff are shown.\n- id: type-level-exceeds-cell-level\n  statement: Type-level conservation across regimes is much greater than the preservation of\n    cell-level relationships and local neighborhoods.\n  source: Results, Type-level phenotypic relationships, paragraph 5; Discussion, Type-level\n    organization is more stable\n  quote: >-\n    Type-level conservation was substantially more apparent than preservation of local\n    cell-level neighborhoods\n  data: with_inputs\n  depends_on:\n  - fig1b-distance-correlation\n  - fig1c-knn-jaccard\n  - fig3a-type-map-concordance\n  criterion: Read from the paper's numbers, without a new test. Reproduced when, for each regime\n    pair, the type-map concordance (fig3a-type-map-concordance) exceeds the cell-cell distance\n    correlation (fig1b-distance-correlation) and the mean 15-NN Jaccard (fig1c-knn-jaccard) is\n    below 0.05 for each pair.\n- id: fig4ab-rna-tracks-shared-map\n  statement: Transcriptomic distance between t-types (500-gene primary panel, 10 PCs) tracks the\n    cross-regime mean phenotypic separation much more strongly (rho 0.507) than the\n    regime-selective rank range (rho 0.083).\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 1; Figure 4A,B; Table 2 rows m and n\n  quote: >-\n    Transcriptomic distance tracked cross-regime mean phenotypic separation much more strongly\n    (Spearman's ρ = 0.507 m , empirical p = 0.000999; Fig. 4 A ) than regime-selective rank\n    range ( ρ = 0.083 n , p = 0.000999; Fig. 4 B )\n  statistics:\n  - about: T against mean S\n    test: Spearman correlation, empirical p against 1,000 label shuffles\n    statistic: rho = 0.507\n    p: 0.000999\n    n: 1,596 type pairs\n  - about: T against rank range\n    test: Spearman correlation, empirical p against 1,000 label shuffles\n    statistic: rho = 0.083\n    p: 0.000999\n    n: 1,596 type pairs\n  data: with_inputs\n  depends_on:\n  - fig3b-pair-tags\n  expected:\n  - quantity: Spearman of T with mean S, primary panel\n    value: 0.507\n    tolerance: 0.0507\n  - quantity: Spearman of T with rank range, primary panel\n    value: 0.083\n    tolerance: 0.0083\n  criterion: >-\n    Method from the Methods (Molecular labels; Molecular recovery of shared versus\n    regime-selective structure) and scripts/q3bc_explain.py. NeMO counts for the RNA samples\n    whose t-type is one of the 57 types, joined by transcriptomic sample identifier; log-CPM as\n    the code computes it, natural log of 1 + 10^6 count / library size. Curated list\n    (configs/q3_curated_excitability_genes.txt) genes present in the matrix; highly variable\n    genes ranked by the variance of log-CPM over those samples; primary panel the curated genes\n    padded with the top-variance genes to 500. Genes z-scored across cells, PCA by SVD, first 10\n    PC scores; T(a,b) the Euclidean distance between t-type means of the scores. Mean S is the\n    mean of the three regimes' S(a,b); rank range from fig3b-pair-tags. Spearman of T with each\n    over the 1,596 pairs. The null is open. The Methods say \"label-shuffle\"; the code's\n    50-permutation p (empirical_spearman_p) shuffles the mean S or rank range values across\n    type pairs and counts |null| >= |observed|; the 1,000-shuffle file the paper reports\n    (results/q3b/q3b_primary_null_1000.csv, \"emp_p_one_sided\") has no script. Readings are (a)\n    permute the phenotype values across pairs, one-sided (null >= observed), 1,000 times; (b) the\n    same, two-sided; (c) shuffle t-type labels among the RNA cells and recompute T, 1,000 times,\n    the Methods' wording. Reproduced when both rho are within tolerance and, under one reading,\n    rho with mean S has p < 0.05. The p of the rank-range correlation is reported under every\n    reading but not judged, as the paper itself reads the asymmetry from the effect sizes. The\n    tolerance on 0.083 (0.0083) is 10% of a small value; a value within 0.03 of it is reported\n    as near.\n- id: fig4-alternative-panels\n  statement: The asymmetry holds for two alternative gene sets; the curated 263-gene panel gives\n    rho 0.551 with mean S against 0.011 with rank range, and the 500 most variable genes give\n    0.520 against 0.105.\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 1; Extended Data Figure 4-2A,B; Table 2 rows o to r\n  quote: >-\n    a curated 263-gene panel ( ρ = 0.551 o vs 0.011 q ) and an independently defined set of\n    highly variable genes ( ρ = 0.520 p vs 0.105 r ; Extended Data Fig. 4-2 A , B )\n  statistics:\n  - about: curated T against mean S\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = 0.551\n    p: 0.020\n  - about: HVG500 T against mean S\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = 0.520\n    p: 0.020\n  - about: curated T against rank range\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = 0.011\n    p: 0.706\n  - about: HVG500 T against rank range\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = 0.105\n    p: 0.020\n  data: with_inputs\n  depends_on:\n  - fig4ab-rna-tracks-shared-map\n  expected:\n  - quantity: curated genes present\n    value: 263\n    tolerance: 26.3\n  - quantity: Spearman of T with mean S, curated panel\n    value: 0.551\n    tolerance: 0.0551\n  - quantity: Spearman of T with rank range, curated panel\n    value: 0.011\n    tolerance: 0.0011\n  - quantity: Spearman of T with mean S, HVG500\n    value: 0.520\n    tolerance: 0.052\n  - quantity: Spearman of T with rank range, HVG500\n    value: 0.105\n    tolerance: 0.0105\n  criterion: As fig4ab-rna-tracks-shared-map with the curated genes alone and with the 500\n    highest-variance genes alone, 50 shuffles (scripts/q3bc_explain.py, which permutes the\n    phenotype values across pairs, two-sided; readings as there). Reproduced when the\n    correlations with mean S are within tolerance with p < 0.05 and each panel's correlation\n    with mean S exceeds its correlation with rank range by more than 0.3; partially reproduced\n    when the asymmetry holds but some value is out of tolerance. The tolerance on 0.011 is 10%\n    of a value near zero; any value with |rho| < 0.05 is reported as near.\n- id: fig4c-joint-excitability-modules\n  statement: A joint representation of the prespecified excitability modules correlates with\n    mean phenotypic separation (rho 0.314) but not with rank range (rho -0.023).\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 2; Figure 4C; Table 2 rows s and t\n  quote: >-\n    a joint excitability-module representation correlated with mean phenotypic distance ( ρ =\n    0.314 s , empirical p = 0.020) but not with rank range ( ρ = −0.023 t , p = 0.294; Fig. 4 C\n    )\n  statistics:\n  - about: joint module distance against mean S\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = 0.314\n    p: 0.020\n    n: 1,596 type pairs\n  - about: joint module distance against rank range\n    test: Spearman correlation, empirical p against 50 shuffles\n    statistic: rho = -0.023\n    p: 0.294\n    n: 1,596 type pairs\n  data: with_inputs\n  depends_on:\n  - fig4ab-rna-tracks-shared-map\n  expected:\n  - quantity: Spearman of joint module distance with mean S\n    value: 0.314\n    tolerance: 0.0314\n  - quantity: Spearman of joint module distance with rank range\n    value: -0.023\n    tolerance: 0.0023\n  criterion: >-\n    Method from scripts/q3bc_explain.py (q3c_modules), as the Methods name it (module-restricted\n    transcriptomic distances for the prespecified modules, Extended Data Figure 4-1). The module\n    gene sets are the code's MODULES (Nav, Kv3, Kv delayed rectifier, HCN, Cav, SK/BK,\n    potassium leak, GABA-A, AMPA/NMDA), restricted to genes of the curated list present in the\n    matrix, a module kept when at least two are present. Log-CPM of the curated genes z-scored\n    across cells; a cell's module score is the mean z of its genes; a type's score the mean\n    over its cells; the joint distance the Euclidean distance between types over the nine\n    excitability module scores (marker controls excluded). Spearman with mean S and rank range\n    over the 1,596 pairs; 50 shuffles as in fig4-alternative-panels. Reproduced when rho with\n    mean S is within tolerance with p < 0.05 and the rank-range correlation is not significant\n    at p < 0.05 (a claim of absence, judged on that test); partially reproduced when the\n    significance pattern holds but 0.314 is out of tolerance. The size of the rank-range\n    correlation is reported either way.\n- id: fig4c-kv3-strongest\n  statement: Kv3 expression shows the strongest association with mean phenotypic distance among\n    the channel programs tested (rho 0.410).\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 2; Figure 4C\n  quote: >-\n    Kv3 expression showed the strongest association with mean phenotypic distance among the\n    tested channel programs ( ρ = 0.410)\n  data: with_inputs\n  depends_on:\n  - fig4c-joint-excitability-modules\n  expected:\n    quantity: Spearman of Kv3 module distance with mean S\n    value: 0.410\n    tolerance: 0.041\n  criterion: Per module, the distance between two types is the absolute difference of their\n    module scores (scripts/q3bc_explain.py, q3c_modules), correlated with mean S over the 1,596\n    pairs. Which programs are \"channel programs\" is open; readings are (a) the seven channel\n    modules (Nav, Kv3, Kv delayed rectifier, HCN, Cav, SK/BK, potassium leak); (b) all nine\n    excitability modules, receptors included. Reproduced when Kv3 is within tolerance and has\n    the largest rho with mean S under one reading.\n- id: fig4c-no-module-tracks-rank-range\n  statement: No excitability program, single or joint, shows more than a negligible association\n    with rank range; the largest single-module value is |rho| = 0.053, for Cav.\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 2; Figure 4C\n  quote: >-\n    No tested excitability program, individual or joint, showed more than a negligible\n    association with rank range (largest individual-module | ρ | = 0.053, Cav)\n  data: with_inputs\n  depends_on:\n  - fig4c-joint-excitability-modules\n  expected:\n    quantity: largest absolute Spearman of a single excitability module distance with rank range\n    value: 0.053\n    tolerance: 0.0053\n  criterion: As fig4c-kv3-strongest, with rank range in place of mean S, over the nine\n    excitability modules. Reproduced when the largest |rho| is within tolerance and belongs to\n    Cav; partially reproduced when every |rho| is below 0.1 but the largest is out of tolerance\n    or belongs to another module.\n- id: pvalb-marker-control\n  statement: A Pvalb marker control corresponds more strongly with mean phenotypic distance (rho\n    0.543) than any single excitability module.\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 2; Extended Data Figure 4-2C\n  quote: >-\n    a Pvalb marker control showed an even stronger correspondence with mean phenotypic distance (\n    ρ = 0.543) than any individual excitability module\n  data: with_inputs\n  depends_on:\n  - fig4c-kv3-strongest\n  expected:\n    quantity: Spearman of Pvalb marker distance with mean S\n    value: 0.543\n    tolerance: 0.0543\n  criterion: The Pvalb marker module of scripts/q3bc_explain.py (Pvalb and Tac1, restricted to\n    genes of the curated list present in the matrix; kept only when at least two are present),\n    scored and compared as in fig4c-kv3-strongest. Reproduced when its rho with mean S is within\n    tolerance and exceeds that of each of the nine excitability modules.\n- id: mobility-distribution\n  statement: Cell-level neighborhood mobility across regimes, one minus the mean Spearman\n    correlation of a cell's distance profile across the three regime pairs, has mean 0.589 and\n    SD 0.110 over the 4,049 cells in all three regimes.\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 3; Extended Data Figure 4-4A; Table 2 row x\n  quote: >-\n    mobility = 1 − mean Spearman correlation of rank-distance profiles across the three regime\n    pairs; n = 4,049; mean mobility = 0.589, SD = 0.110 x\n  data: dataset\n  depends_on:\n  - table1-phenotype-spaces\n  expected:\n  - quantity: mean mobility\n    value: 0.589\n    tolerance: 0.011\n  - quantity: SD of mobility\n    value: 0.110\n    tolerance: 0.011\n  - quantity: cells in all three regimes\n    value: 4049\n    tolerance: 404.9\n  criterion: Method from the Methods (Transcriptomic mobility and coexpression analysis) and\n    scripts/q3_mobility_modules.py (compute_mobility). On the triple-shared cells, each cell's\n    vector of Euclidean distances to all other triple-shared cells in each regime's k80 space,\n    self excluded; Spearman correlation of the vectors for each of the three regime pairs; the\n    mean of the three; mobility one minus it. SD is the population SD. The tolerance on the mean\n    is the paper's stated spread, the SD of 0.110, divided by 10 (a tenth of the spread across\n    cells, tighter than 10% of 0.589 would be loose for a mean over 4,049 cells; 10% of 0.589,\n    0.059, is shown as a variant). Reproduced when the three values are within tolerance.\n- id: wgcna-mobility-within-type\n  statement: WGCNA coexpression modules on a 2,000-gene panel show modest associations with\n    mobility before accounting for t-type (largest |rho| 0.199) but within-type residual\n    associations are |rho| at most 0.039 for every module, so within-type transcriptomic\n    heterogeneity shows little association with mobility beyond t-type.\n  source: Results, Transcriptomic structure preferentially tracks the shared phenotypic map,\n    paragraph 3; Extended Data Figures 4-3 and 4-4B; Table 2 row y; Methods, Transcriptomic\n    mobility and coexpression analysis\n  quote: >-\n    WGCNA modules built on the prespecified 2,000-gene panel showed modest associations with\n    mobility before accounting for transcriptomic type (largest | ρ | = 0.199; Extended Data\n    Fig. 4-3 ), but after within-type centering of mobility and module eigengenes, residual\n    associations fell to | ρ | ≤ 0.039 for all modules\n  data: with_inputs\n  depends_on:\n  - mobility-distribution\n  expected:\n  - quantity: cells with mobility, RNA and t-type\n    value: 3906\n    tolerance: 390.6\n  - quantity: cells in types with at least three members\n    value: 3902\n    tolerance: 390.2\n  - quantity: soft-threshold power beta\n    value: 3\n    tolerance: 0\n  - quantity: scale-free fit R squared at the chosen beta\n    value: 0.891\n    tolerance: 0.0891\n  - quantity: WGCNA modules (grey excluded)\n    value: 10\n    tolerance: 1\n  - quantity: largest unadjusted absolute Spearman of an eigengene with mobility\n    value: 0.199\n    tolerance: 0.0199\n  - quantity: largest residual absolute Spearman of an eigengene with mobility\n    value: 0.039\n    tolerance: 0.0039\n  criterion: >-\n    Method from the Methods (Transcriptomic mobility and coexpression analysis) and\n    scripts/q3_mobility_modules.py, q3_wgcna_mobility.py and q3_wgcna_modules.R. Triple-shared\n    cells with a transcriptomic sample identifier and a t-type; log-CPM as in\n    fig4ab-rna-tracks-shared-map; panel the curated genes present, then genes in descending\n    log-CPM variance over these cells, to 2,000, zero-variance genes dropped. WGCNA 1.74,\n    goodSamplesGenes; pickSoftThreshold unsigned, powers 1 to 20, beta the lowest with\n    scale-free R squared at least 0.80; blockwiseModules unsigned network and TOM, minModuleSize\n    20, mergeCutHeight 0.25, reassignThreshold 0, pamRespectsDendro FALSE, one block, seed 0;\n    grey not a module. Spearman of each eigengene with mobility, empirical p from 1,000\n    shuffles of mobility (two-sided, as empirical_spearman_p). Residual analysis: mobility and\n    each eigengene centered on their t-type mean, restricted to types with at least three\n    members. The beta is an integer the rule selects, so its tolerance is 0. Reproduced when\n    the largest residual |rho| is at most 0.039 plus tolerance, no module has residual |rho| >=\n    0.10 with p < 0.05 (the paper's own test of absence, Table 2 row y), and the largest\n    unadjusted |rho| is within tolerance; partially reproduced when the residual test holds but\n    the module count, beta or unadjusted value differ. Module identities are not expected to\n    match one to one.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2026-flexible.yaml",
 "old_string": "  - quantity: mean mobility\n    value: 0.589\n    tolerance: 0.011",
 "new_string": "  - quantity: mean mobility\n    value: 0.589\n    tolerance: 0.0589"
}
```

```
The file claims/yang-2026-flexible.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2026-flexible.yaml",
 "old_string": "mean of the three; mobility one minus it. SD is the population SD. The tolerance on the mean\n    is the paper's stated spread, the SD of 0.110, divided by 10 (a tenth of the spread across\n    cells, tighter than 10% of 0.589 would be loose for a mean over 4,049 cells; 10% of 0.589,\n    0.059, is shown as a variant). Reproduced when the three values are within tolerance.",
 "new_string": "mean of the three; mobility one minus it. SD is the population SD. Reproduced when the three\n    values are within tolerance."
}
```

```
The file claims/yang-2026-flexible.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/yang-2026-flexible.yaml paper/10.1523-eneuro.0275-26.2026.txt; grep -n "—\|rather" claims/yang-2026-flexible.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml
for ev in yaml.parse(open('claims/yang-2026-flexible.yaml')):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and (': ' in ev.value or ' #' in ev.value):
        print(repr(ev.value[:100]))
print('done')"
```

```
done
```

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/yang-2026-flexible.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
from collections import Counter;print(Counter(x.get('data','dataset') for x in c))"
```

```
29 8 29 23
Counter({'with_inputs': 21, 'dataset': 8})
```

**Agent**

I wrote `claims/yang-2026-flexible.yaml` with 29 claims. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** I read the version of record (eNeuro, PMC13737997): main text, Methods, Results, Discussion, Tables 1 and 2 (rows a to y), and all figure and Extended Data legends. The Extended Data files themselves (TIF figures, DOCX Tables 1-1, 2-1, 3-1, 4-1, 4-3) are not in the text, and there was no PDF. No claim needed them: every expected value is printed in the main text or Table 2, and the feature lists of Table 1-1 come from the paper's code instead.

**Code read.** github.com/zy-neuro/protocol-response-geometry at commit 61a5a41: the analysis scripts, the curated gene list, and derived tables (PCA scores, retained features, and the table joining NWB files to t-type, Cre line and sample ID).

**Counts.**
- 29 claims, all 29 with quotes and none inferred.
- 8 claims carry statistics, 26 statistical values in all (permutation p floors 0.0099, 0.020 and 0.000999, plus three 95% intervals).
- All 29 have criteria and 23 have expected values.
- 8 claims use the dataset alone. 21 are `with_inputs`, because they need t-type, Cre and subclass labels or the gene counts from the NeMO Patch-seq release 20200611 (count matrix v2).

**Details the paper leaves open, and the readings named:**
- **Full-cell feature extraction.** The script that ran IPFX on all cells is not in the repo, so the IPFX version and call are open. The reading is the code's split-half feature packing with the current IPFX, with the Allen pipeline's version as a variant.
- **Which cells enter a regime, and the denominator of the 30% missing-value rule.** Either cells with any non-missing feature of that regime (as the code does), or all cells that passed extraction.
- **Cell-pair sampling.** The Methods say "unique" pairs; the code's draw can repeat pairs. The Methods reading is the main one and the code's is a variant.
- **Spearman ties in A_t.** The code ranks without averaging ties. On a binary label distance this shrinks the correlation well below an average-rank Spearman. I followed the code; average ranks are a variant.
- **Neighbor enrichment.** Ratio of means (the code, used) or mean of per-cell ratios (variant).
- **Cell set for Cre eta squared and the Cre-residualized A_t.** Cells with both labels (the code) or all cells with a Cre line.
- **Null for transcriptomic distance against phenotype.** Shuffle values across pairs one-sided, the same two-sided, or shuffle t-type labels and recompute (the Methods' wording). The 1,000-shuffle file the paper reports has no script.
- **Equal-N "well above nulls".** Either each 2.5th percentile is above the null's maximum, or each mean is above the null's 97.5th percentile.
- **"Proportions stable" under threshold changes.** The cutoff grid is fixed from the figure code. The two readings are a minority-selective test and a step size of at most 10 percentage points.
- **"Increased with k".** A rise at every step of the grid, or k = 600 above k = 15.
- **Subclass concordances 0.579 and 0.621.** Which brief-pulse pair each belongs to is open.
- **"Channel programs" for the Kv3 claim.** The seven channel modules, or all nine excitability modules.
- **Figure 2B.** The paper gives no test. I judge it with the paper's within-Cre A_t and eta squared; per-type PC1 medians are shown but not judged.
- **Residual t-type eta squared.** No value is printed; it is judged against the paper's 100-shuffle label null.

**Missing.** No claim lacked a text the paper rests on. Within the code deposit, two things are absent: the full-cell IPFX extraction script (and its feature table), and the script behind the 1,000-shuffle transcriptomic null.

## End of run

37 turns, 8 minutes, $3.05 at API prices, result: success.
