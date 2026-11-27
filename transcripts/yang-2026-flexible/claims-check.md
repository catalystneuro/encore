# yang-2026-flexible · claims-check · run 45005231666

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i yang; cat claims/yang-2026-flexible.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; python tools/claims_check.py claims/yang-2026-flexible.yaml paper/10.1523-eneuro.0275-26.2026.txt; wc -l claims/yang-2026-flexible.yaml paper/10.1523-eneuro.0275-26.2026.txt
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
cd  sed -n '/^## Reader/,/^## [A-Z]/p' docs/protocol.md | head -120; grep -n "Reader" docs/protocol.md | head
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold. A
data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
documentation) is a longer description, to be read for that alone; it is not
the paper, and no claim comes from it.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk '/^## Reader/{f=1} f&&/^## Author/{exit} f' docs/protocol.md | sed -n '120,260p'
```

```
are public and blocked as `data_missing` when not; the claims the
     reused dataset can test are the ones the attempt is about.

### 4. Data from outside the paper's own recordings

Say, for each claim, what data the paper's test uses (`data`, above). When the
paper relies on outside data (a model, a reference dataset, measurements of
the same cells made by another method), or deposited part of its data in
another archive, name it and where it is, as the paper gives it. The author
pins it and decides whether it can be used (author, step 4).

### 5. Check

A second reader, in a separate run, checks the claims file against the paper:
that each statement says what the paper says, no more and no less; that each
quote is word for word (the quote checker, `tools/claims_check.py`, does this
mechanically); that each source points at the place; that the statistics are
the paper's and are results, not thresholds; that every part of every
criterion's method is taken from the paper or its code, as cited; and that the
paper's main findings each have a claim. The checker corrects what it can
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/yang-2026-flexible.yaml"
}
```

```
1	# Claims for Yang (2026), "Flexible Cellular Phenotypes Retain a Shared Type-Level Organization
2	# across Response Regimes", eNeuro 13(11) ENEURO.0275-26.2026, doi:10.1523/eneuro.0275-26.2026,
3	# on DANDI 000020 (Allen Institute Patch-seq of mouse visual cortex GABAergic neurons, Gouwens et
4	# al. 2020), which the paper reuses.
5	#
6	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
7	# Actions"), 2026-11-22, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
8	#
9	# Text read. The version of record, from paper/10.1523-eneuro.0275-26.2026.txt (PMC13737997):
10	# abstract, Significance Statement, Introduction, Materials and Methods, Results, Discussion,
11	# Table 1, Table 2 (statistical summary, rows a to y), the legends of Figures 1 to 4 and of the
12	# Extended Data (Figures 1-1 to 1-3, 2-1, 3-1 to 3-3, 4-1 to 4-4; Tables 1-1 and 2-1), and the
13	# synthesis of the reviews. The Extended Data files themselves (TIF figures, DOCX Tables 1-1,
14	# 2-1, 3-1, 4-1, 4-3) are not in the text and no PDF was supplied; only their legends were read.
15	# No claim rests on a number printed only in them: every expected value below is printed in the
16	# Results, the Methods or Table 2. The retained feature lists of Extended Data Table 1-1 are
17	# taken from the paper's code (below). The paper prints "Table 2 (rows a-y)" superscript letters
18	# after its values; they appear in the quotes as stray letters ("0.434 a").
19	#
20	# Code read. https://github.com/zy-neuro/protocol-response-geometry, commit 61a5a41 (2026-10-19),
[... 1106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1523-eneuro.0275-26.2026.txt').read(); print(t[59000:])"; ls; ls papers/datasets 2>/dev/null | grep yang; cat papers/datasets/yang-2026-flexible.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1523-eneuro.0275-26.2026.txt').read(); print(t[61000:85000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls; find / -path /proc -prune -o -type d -name "protocol-response-geometry*" -print 2>/dev/null | head; git log --oneline -3 -- claims/yang-2026-flexible.yaml
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/zy-neuro/protocol-response-geometry.git prg 2>&1 | tail -2; cd prg && git log --oneline -3 && ls scripts | head -50
```

```
61a5a41 Unify accepted analysis into a single scripts/ and results/ tree.
a892bef Add revision analysis code and tables.
dump_pc1_loadings.py
figures_eneuro_results.py
figures_eneuro_supplement.py
paths.py
q1_describe_phenotype.py
q1_knn_scale.py
q1_split_half_long_square.py
q2_anchor.py
q3_mobility_modules.py
q3_wgcna_mobility.py
q3_wgcna_modules.R
q3a_centroid_robustness.py
q3a_explain.py
q3bc_explain.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; wc -l scripts/*; cat scripts/q2_anchor.py
```

```
129 scripts/dump_pc1_loadings.py
   985 scripts/figures_eneuro_results.py
  1194 scripts/figures_eneuro_supplement.py
    22 scripts/paths.py
   427 scripts/q1_describe_phenotype.py
   175 scripts/q1_knn_scale.py
   860 scripts/q1_split_half_long_square.py
   434 scripts/q2_anchor.py
   604 scripts/q3_mobility_modules.py
   406 scripts/q3_wgcna_mobility.py
   197 scripts/q3_wgcna_modules.R
   523 scripts/q3a_centroid_robustness.py
   333 scripts/q3a_explain.py
   796 scripts/q3bc_explain.py
  7085 total
#!/usr/bin/env python3
"""Q2 ANCHOR: is cellular phenotype organization biologically anchored?

Primary: A_p = Spearman(D^mol, D^phenotype).
Control: Cre alignment and within-Cre / Cre-residual t-type tests.
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 1,333p scripts/q3a_explain.py
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
cd $TMPDIR/prg; grep -n "def \|N_\|rng\.\|choice\|permutation\|percentile\|split\|//" scripts/q3a_centroid_robustness.py | head -80
```

```
27:N_MIN = 10
28:N_EQUAL = 10  # draw this many cells per type × protocol
29:N_BOOT = 200
30:N_RELIAB = 200
31:N_SHUFFLE = 1000
53:def pc_cols(fieldnames):
58:def parse_session(row: dict) -> str:
64:        return fs.split("_ses-")[1].replace("_icephys", "")
68:def choose_k(path: Path, n_available: int) -> int:
82:def load_scores(path: Path):
99:def load_join(path: Path) -> dict[str, dict]:
104:def spearman(a: np.ndarray, b: np.ndarray) -> float:
114:def protocol_arrays(stems, X, k, join):
128:def index_by_type(labs: list[str]) -> dict[str, np.ndarray]:
135:def centroids_from_indices(x: np.ndarray, by_type: dict[str, np.ndarray], types: list[str], take: dict[str, np.ndarray]) -> np.ndarray:
149:def upper(S: np.ndarray) -> np.ndarray:
154:def sample_equal_n(by_type: dict[str, np.ndarray], types: list[str], n_draw: int, rng: np.random.Generator) -> dict[str, np.ndarray] | None:
160:        take[t] = rng.choice(idx, size=n_draw, replace=False)
164:def quantiles(vals: np.ndarray) -> dict[str, float]:
176:def main() -> None:
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 254,312p scripts/q3a_centroid_robustness.py
```

```
# --- Within-regime reliability ceiling (split-half S concordance) ---
    reliab_rows = []
    reliab = {p: [] for p in PROTOCOLS}
    for b in range(N_RELIAB):
        row = {"boot": b}
        for p in PROTOCOLS:
            take_a, take_b = {}, {}
            ok = True
            for t in types:
                idx = packed[p]["by"][t]
                if idx.size < 2 * (N_EQUAL // 2) and idx.size < 4:
                    # need at least 4 cells to split reasonably; else use bootstrap halves
                    pass
                if idx.size < 4:
                    ok = False
                    break
                perm = rng.permutation(idx)
                half = idx.size // 2
                take_a[t] = perm[:half]
                take_b[t] = perm[half : 2 * half] if 2 * half <= idx.size else perm[half:]
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 1,140p scripts/q3bc_explain.py; grep -n "def \|joint\|abs(\|MARKER\|N_SHUF\|N_PERM\|>= 2\|len(g" scripts/q3bc_explain.py
```

```
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
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-prg")

[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 161,240p scripts/q3bc_explain.py; sed -n 263,320p scripts/q3bc_explain.py; sed -n 389,500p scripts/q3bc_explain.py; sed -n 656,710p scripts/q3bc_explain.py
```

```
def pairwise_euclid(M: np.ndarray) -> np.ndarray:
    nrm = np.sum(M * M, axis=1, keepdims=True)
    d2 = nrm + nrm.T - 2.0 * (M @ M.T)
    np.maximum(d2, 0.0, out=d2)
    D = np.sqrt(d2)
    np.fill_diagonal(D, 0.0)
    return D


def pca_scores(X: np.ndarray, n_pcs: int) -> tuple[np.ndarray, np.ndarray]:
    Xc = X - X.mean(axis=0, keepdims=True)
    std = Xc.std(axis=0, keepdims=True)
    std[std == 0] = 1.0
    Z = Xc / std
    # economy SVD: cells x genes
    u, s, vt = np.linalg.svd(Z, full_matrices=False)
    k = min(n_pcs, s.size)
    scores = u[:, :k] * s[:k]
    var = (s**2) / max(1, Z.shape[0] - 1)
    var = var / var.sum()
[... 286 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 710,760p scripts/q3bc_explain.py; ls results/q3b results/q3c 2>/dev/null; head -5 results/q3b/q3b_primary_null_1000.csv 2>/dev/null
```

```
if prim["spearman_T_vs_meanS"] >= 0.25 and abs(prim["spearman_T_vs_rank_range"]) < 0.15:
        landing = "rna_tracks_phenotype_distance"
    elif abs(prim["spearman_T_vs_rank_range"]) >= 0.25:
        landing = "rna_tracks_selectivity"
    else:
        landing = "rna_weak"
    q3b = {
        "question": "Q3b",
        "n_types": len(types),
        "types": types,
        "panels": summaries,
        "landing": landing,
        "rationale": (
            f"ρ(T,meanS)={prim['spearman_T_vs_meanS']:.2f} (emp_p={prim['empirical_p_T_vs_meanS']:.3f}); "
            f"ρ(T,rank_range)={prim['spearman_T_vs_rank_range']:.2f} (emp_p={prim['empirical_p_T_vs_rank_range']:.3f}); "
            f"meanT stable={prim['mean_T_stable']:.2f} vs selective={prim['mean_T_selective']:.2f}."
        ),
        "note": "Targeted curated∪HVG analysis — not a genome-wide discovery claim.",
    }
    (OUT_B / "q3b_summary.json").write_text(json.dumps(q3b, indent=2) + "\n")
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; cut -d, -f1-3,6,8,9,11 results/q3c/q3c_module_tests.csv; cat results/q3b/q3b_panel_summary.csv | cut -c1-400
```

```
module,role,n_genes_present,p_score_vs_selectivity,p_D_vs_meanS,empirical_p_D_vs_meanS,p_D_vs_rank_range
Nav,excitability,9,0.4708692812399382,9.578143729772755e-14,0.0196078431372549,0.0866505134818546
Kv3,excitability,4,0.584660926514518,7.354879091070304e-72,0.0196078431372549,0.8407447242471796
Kv_delayed,excitability,7,0.6051280757222033,0.0005562517353115016,0.0196078431372549,0.1029808933986387
HCN,excitability,4,0.7883878037339448,5.536553130690504e-32,0.0196078431372549,0.11132634660929262
Cav,excitability,8,0.0253358408579757,0.400876022335207,0.43137254901960786,0.03504009298573707
SK_BK,excitability,7,0.3283380553350938,0.02693090651346548,0.0784313725490196,0.11567178754939819
K_leak,excitability,7,0.9685573378202396,1.3566905487423399e-22,0.0196078431372549,0.3639485766626494
GABA_A,excitability,11,0.2895831938130985,0.578554066688562,0.5098039215686274,0.8084055563403982
AMPA_NMDA,excitability,9,0.005142047238132961,0.2629754813670789,0.35294117647058826,0.09862480543547401
Pvalb_marker,marker_control,2,0.43158625227923336,2.6854201731142866e-147,0.0196078431372549,0.0014156641606169606
Sst_marker,marker_control,4,5.6505823872885457e-05,0.058715855111649375,0.09803921568627451,2.5445797456718133e-09
Vip_marker,marker_control,3,0.3302943827235236,3.9580457122563416e-36,0.0196078431372549,0.33587896885143814
panel,n_genes,n_cells,n_types,n_pairs,var_explained_top5,spearman_T_vs_meanS,p_T_vs_meanS,empirical_p_T_vs_meanS,spearman_T_vs_rank_range,p_T_vs_rank_range,empirical_p_T_vs_rank_range,mean_T_stable,mean_T_selective,mannwhitney_sel_vs_stab_p
curated,263,4250,57,1596,"[0.07533758878707886, 0.05579990893602371, 0.046258799731731415, 0.020985880866646767, 0.01703413389623165]",0.5506451296159086,7.24693143280311e-153,0.0196078431372549,0.01063224011469758,0.6711899526777642,0.7058823529411765,9.919440354766385,8.802091814481088,0.004975124378109453
primary,500,4250,57,1596,"[0.09883145987987518, 0.06319931894540787, 0.05732741206884384, 0.03572581335902
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 1,175p scripts/q1_knn_scale.py | grep -v "^\s*#" | sed -n 20,175p
```

```
N_SHUFFLE = 100
K_GRID = (15, 30, 60, 120, 240, 480, 600)
VARIANCE_FLOOR = 0.80
PROTOCOLS = ("long_pulse", "ramp", "brief_pulse")
PAIRS = (
    ("long_pulse", "ramp"),
    ("long_pulse", "brief_pulse"),
    ("ramp", "brief_pulse"),
)


def pc_cols(fieldnames: list[str]) -> list[str]:
    cols = [c for c in fieldnames if c.startswith("PC") and c[2:].isdigit()]
    return sorted(cols, key=lambda c: int(c[2:]))


def load_scores(path: Path) -> tuple[list[str], np.ndarray]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        cols = pc_cols(reader.fieldnames or [])
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; grep -n "def align_pair" -A45 scripts/q1_describe_phenotype.py | head -70; grep -n "FIXED_K\|KNN\|N_PAIR" scripts/q1_describe_phenotype.py | head
```

```
163:def align_pair(
164-    stems_a: list[str],
165-    xa: np.ndarray,
166-    stems_b: list[str],
167-    xb: np.ndarray,
168-    k_a: int,
169-    k_b: int,
170-    rng: np.random.Generator,
171-) -> dict:
172-    pos_a = {s: i for i, s in enumerate(stems_a)}
173-    pos_b = {s: i for i, s in enumerate(stems_b)}
174-    shared = [s for s in stems_b if s in pos_a]
175-    ia = np.array([pos_a[s] for s in shared], dtype=int)
176-    ib = np.array([pos_b[s] for s in shared], dtype=int)
177-
178-    da = pairwise_euclidean(xa[ia, :k_a])
179-    db = pairwise_euclidean(xb[ib, :k_b])
180-    n = da.shape[0]
181-    ii, jj = sample_pairs(n, rng)
182-    ua, ub = da[ii, jj], db[ii, jj]
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; grep -n "def compute_mobility" -A40 scripts/q3_mobility_modules.py | head -50; grep -n "2000\|N_GENES\|var\|shuffle\|permutation\|>= 3\|MIN_" scripts/q3_wgcna_mobility.py | head -30; grep -n "pickSoft\|blockwise\|power\|0.8\|minModule\|merge\|reassign\|pam\|networkType\|TOMType\|maxBlock\|seed" scripts/q3_wgcna_modules.R
```

```
289:def compute_mobility(stems_by_proto, X_by_proto, k_by_proto) -> tuple[list[str], np.ndarray, dict]:
290-    sets = [set(stems_by_proto[p]) for p in PROTOCOLS]
291-    shared = [s for s in stems_by_proto["long_pulse"] if s in sets[1] and s in sets[2]]
292-    pos = {p: {s: i for i, s in enumerate(stems_by_proto[p])} for p in PROTOCOLS}
293-    dists = {}
294-    for p in PROTOCOLS:
295-        idx = np.array([pos[p][s] for s in shared], dtype=int)
296-        xp = X_by_proto[p][idx, : k_by_proto[p]]
297-        dists[p] = pairwise_euclidean(xp)
298-    n = len(shared)
299-    rhos = np.full((n, len(PAIRS)), np.nan)
300-    for j, (a, b) in enumerate(PAIRS):
301-        da, db = dists[a], dists[b]
302-        for i in range(n):
303-            # exclude self
304-            mask = np.ones(n, dtype=bool)
305-            mask[i] = False
306-            rhos[i, j] = spearman(da[i, mask], db[i, mask])
307-    mean_rho = np.nanmean(rhos, axis=1)
308-    mobility = 1.0 - mean_rho
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 60,100p scripts/q3_wgcna_mobility.py; sed -n 165,200p scripts/q3_wgcna_mobility.py
```

```
j = join.get(rec.get("file_stem") or "", {})
            sid = (j.get("transcriptomics_sample_id") or "").strip()
            tt = tt or (j.get("t_type") or "").strip()
        if not sid or not tt:
            continue
        keep_samples.append(sid)
        stem_by_sample[sid] = rec["file_stem"]
        ttype_by_sample[sid] = tt
        mob_by_sample[sid] = float(rec["mobility"])
    keep_samples = sorted(set(keep_samples))
    print(f"Mobility cells: {n_mob}; with RNA+t-type ids: {len(keep_samples)}", flush=True)

    genes, counts, samples = q3.load_counts(q3.nemo_counts_csv(), keep_samples)
    print(f"Loaded counts {counts.shape} (genes x cells)", flush=True)
    expr_all = q3.log_cpm(counts)

    curated_wanted = q3.read_gene_list(q3.CURATED)
    gset = {g: i for i, g in enumerate(genes)}
    curated = [g for g in curated_wanted if g in gset]
    var = expr_all.var(axis=1)
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; ls results/phenotype; python3 -c "
import json;d=json.load(open('results/phenotype/phenotype_summary.json'));print(json.dumps(d,indent=0)[:3500])"
```

```
brief_pulse_pca_loadings.csv
brief_pulse_pca_scores.csv
brief_pulse_pca_variance.csv
long_pulse_pca_loadings.csv
long_pulse_pca_scores.csv
long_pulse_pca_variance.csv
phenotype_summary.json
ramp_pca_loadings.csv
ramp_pca_scores.csv
ramp_pca_variance.csv
{
"long_pulse": {
"n_cells": 4344,
"n_features": 42,
"k80": 11,
"features": [
"feat.long_squares.vrest",
"feat.long_squares.ri",
"feat.long_squares.sag",
"feat.long_squares.tau",
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; python3 -c "
import csv
r=list(csv.DictReader(open('results/phenotype/long_pulse_pca_loadings.csv')))
print(list(r[0].keys())[:5])
k=[c for c in r[0] if c not in('feature',)][0]
" ; head -3 results/phenotype/long_pulse_pca_loadings.csv | cut -c1-200
```

```
['feature', 'display', 'PC1', 'PC2', 'PC3']
feature,display,PC1,PC2,PC3,PC4,PC5,abs_PC1
feat.long_squares.threshold_i,threshold i,0.3031779082335554,-0.027024583373411442,-0.0828504838993797,0.16865391761921467,0.06242923858772911,0.3031779082335554
feat.long_squares.rheobase_i,rheobase i,0.30317790823355534,-0.02702458337341144,-0.08285048389937961,0.1686539176192145,0.062429238587728975,0.30317790823355534
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sort -t, -k8 -gr results/phenotype/long_pulse_pca_loadings.csv | cut -d, -f1,3 | head -8
```

```
feat.long_squares.threshold_i,0.3031779082335554
feat.long_squares.rheobase_sweep.stim_amp,0.30317790823355534
feat.long_squares.rheobase_i,0.30317790823355534
feat.long_squares.hero_sweep.stim_amp,0.30284291446195827
feat.long_squares.ri,-0.26293397694201426
feat.long_squares.input_resistance,-0.262933976942014
feat.long_squares.tau,-0.22023472370033131
feat.long_squares.fi_fit_slope,0.2017967226639358
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; grep -n "0.45\|0.65\|0.15, \|0.35\|cutoff\|sensitiv" scripts/figures_eneuro_supplement.py | head -30
```

```
81:        name, [(1, 1, 1), tuple(0.72 + 0.28 * x for x in c), tuple(0.35 + 0.65 * x for x in c), c]
201:    ax.bar(xs - 0.18, ns, 0.35, color=[soft_bar(c, 0.38) for c in (LONG, RAMP, BRIEF)], edgecolor=[LONG, RAMP, BRIEF], lw=0.9)
202:    ax.bar(xs + 0.18, ks, 0.35, color="white", edgecolor=[LONG, RAMP, BRIEF], lw=1.1)
283:        xs - 0.18, [float(r["spearman_D"]) for r in k80], 0.35,
287:        xs + 0.18, [float(r["spearman_D"]) for r in k5], 0.35,
500:    ax.hist(mob, bins=40, color=soft_bar(INK, 0.35), edgecolor=INK, lw=0.6)
513:    ax.barh(ys + 0.16, rho_u, 0.30, color=soft_bar(INK, 0.35), edgecolor=INK, lw=0.7, label="Unadjusted")
580:    """Q3: full S maps + tag threshold sensitivity + subclass."""
583:    gs = gridspec.GridSpec(2, 3, height_ratios=[1.35, 1.0], hspace=0.35, wspace=0.28, left=0.06, right=0.96, top=0.94, bottom=0.08)
598:    # D — threshold sensitivity
600:    ranges = [0.45, 0.50, 0.55, 0.60, 0.65]
611:    ax.set_xlabel("Selective rank-range cutoff")
617:    cvs = [0.15, 0.20, 0.25, 0.30, 0.35]
628:    ax.set_xlabel("Stable rank-CV cutoff")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; sed -n 596,632p scripts/figures_eneuro_supplement.py
```

```
cbar.set_label("Type–type D", fontsize=8)

    # D — threshold sensitivity
    ax = fig.add_subplot(gs[1, 0])
    ranges = [0.45, 0.50, 0.55, 0.60, 0.65]
    sel_frac = []
    for thr in ranges:
        tags = [retag(float(r["rank_cv"]), float(r["rank_range"]), STABLE_RANK_CV, thr) for r in pairs]
        c = Counter(tags)
        sel_frac.append(100 * c["selective"] / len(pairs))
    ax.plot(ranges, sel_frac, color=INK, marker="o", lw=1.8)
    ax.axvline(SELECTIVE_RANK_RANGE, ls="--", color=REF, lw=1.0)
    ax.set_xticks(ranges)
    ax.set_xticklabels([f"{t:.2f}" for t in ranges])
    ax.set_xlim(0.43, 0.67)
    ax.set_xlabel("Selective rank-range cutoff")
    ax.set_ylabel("% selective pairs")
    letter(ax, "D")

    # E — vary CV at fixed range
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; grep -n "null" scripts/q3a_centroid_robustness.py | sed -n 1,40p; ls results/; ls results/q3a* 2>/dev/null
```

```
294:    # --- Stronger null for observed concordance (1000 type-label shuffles) ---
295:    null_rows = []
298:        null = np.empty(N_SHUFFLE, dtype=float)
309:            null[t] = spearman(upper(S_obs[a]), upper(S_sh))
310:        p_emp = float((1.0 + np.sum(null >= rho)) / (1.0 + N_SHUFFLE))
311:        null_rows.append(
315:                "null_mean": float(np.mean(null)),
316:                "null_sd": float(np.std(null)),
321:        print(f"null {lab}: rho={rho:.4f} null_mean={null.mean():.4f} p={p_emp:.4g}", flush=True)
336:    write_csv(OUT / "concordance_null_1000.csv", null_rows)
359:        "n_shuffle_null": N_SHUFFLE,
363:        "concordance_null_1000": null_rows,
378:        "Also recompute type-label shuffle nulls with **1000** permutations.",
420:        "## Type-label shuffle null (*n* = 1000)",
422:        "| Pair | ρ | null mean | emp. *p* |",
425:    for r in null_rows:
427:            f"| {r['pair'].replace('_', '–')} | {r['observed_rho']:.3f} | {r['null_mean']:.4f} | {r['empirical_p']:.4g} |"
fig1_example_traces.csv
m0
phenotype
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/prg; cat results/q3a/q3a_subclass_concordance.csv results/q3a/q3a_S_concordance.csv results/q3a_robustness/*.csv; ls results/q2 results/q1 results/q1_reliability; cat results/q2/*.csv | head -5 | cut -c1-600
```

```
pair,n_shared_subclasses,spearman_S
long_pulse__ramp,6,0.9357142857142854
long_pulse__brief_pulse,6,0.5785714285714285
ramp__brief_pulse,6,0.6214285714285712
protocol_a,protocol_b,n_types,n_type_pairs,spearman_rho,null_mean,empirical_p_vs_shuffle
long_pulse,ramp,57,1596,0.6575095911546857,-0.00398314945739279,0.009900990099009901
long_pulse,brief_pulse,57,1596,0.45515907178530046,-0.01193743283151395,0.009900990099009901
ramp,brief_pulse,57,1596,0.6084949006447687,-0.02779442312633971,0.009900990099009901
pair,observed_rho,null_mean,null_sd,empirical_p,n_shuffle
long_ramp,0.6575095911546857,-0.00298610764027863,0.05885979052901089,0.000999000999000999,1000
long_brief,0.45515907178530046,-0.011961893103390717,0.06479513657706307,0.000999000999000999,1000
ramp_brief,0.6084949006447687,-0.01607410792553784,0.04310428939772339,0.000999000999000999,1000
pair,observed_full_n,equalN_mean,equalN_sd,equalN_q025,equalN_q500,equalN_q975,equalN_n_ok,delta_mean_minus_obs
long_ramp,0.6575095911546857,0.5536565747562218,0.0390784966875684,0.4749486385831473,0.5572337495710153,0.6242229052343015,200,-0.1038530163984639
long_brief,0.45515907178530046,0.32900869586020964,0.050567082794050734,0.23066695604851883,0.3289597075644417,0.41877618286012763,200,-0.12615037592509082
ramp_brief,0.6084949006447687,0.45549584425236717,0.04993344661700967,0.3530730935108415,0.4545379275277781,0.5388042897772518,200,-0.15299905639240158
protocol,split_half_mean,split_half_sd,split_half_q025,split_half_q500,split_half_q975,split_half_n_ok
long_pulse,0.8609195500100886,0.033026714652231455,0.7914835166651639,0.8630149138704768,0.9162039904587523,200
ramp,0.8513325177243926,0.02024754272126853,0.8112950613215061,0.8525246908687049,0.893934383651412,200
brief_pulse,0.7994826559137955,0.03128524246085445,0.7278420962750133,0.8018467390280695,0.8541480056524656,200
[... 19 more lines not kept]
```

**Agent**

Most of the claims file matches the paper and its code; I'm now fixing criteria where the agent invented thresholds and the one reading that is too narrow.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2026-flexible.yaml",
 "old_string": "    ranked by absolute loading, as the Extended Data Figure 1-2 legend says. Current features are\n    threshold_i, rheobase_i and rheobase_sweep.stim_amp; input resistance features are ri and\n    input_resistance. The paper does not say how far down the ranking \"most strongly\" reaches;\n    readings are (a) the two highest-ranked distinct quantities are a rheobase or threshold\n    current and an input resistance; (b) both kinds are among the five features with the\n    largest absolute loadings. Reproduced under either reading.",
 "new_string": "    ranked by absolute loading, as the Extended Data Figure 1-2 legend says. Current features are\n    threshold_i, rheobase_i, rheobase_sweep.stim_amp and hero_sweep.stim_amp (IPFX picks the\n    hero sweep at a fixed offset above rheobase, so its amplitude is a rheobase-tied current);\n    input resistance features are ri and input_resistance. The paper does not say how far down\n    the ranking \"most strongly\" reaches; readings are (a) the two highest-ranked kinds of\n    feature are a rheobase or threshold current and an input resistance; (b) both kinds are\n    among the five features with the largest absolute loadings. Reproduced under either reading."
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
 "old_string": "    unresidualized) as a variant. The paper prints no residual eta squared value; \"detectable\"\n    is judged as residual eta squared greater than the mean of a 100-shuffle t-type label null on\n    the residualized scores, the null the Methods name for these analyses (\"Label-shuffle null\n    distributions used 100 permutations\"). Reproduced when the three A_t are within tolerance\n    with p < 0.05 and residual eta squared exceeds its null in each regime; partially reproduced\n    when every A_t has p < 0.05 but some value is out of tolerance. The brief-pulse tolerance\n    (0.0004) is 10% of a value that is itself small.",
 "new_string": "    unresidualized) as a variant. The paper prints no residual eta squared value and no test for\n    it (Statistics, Methods; eta squared has no permutation p), so \"detectable\" is open; readings\n    are (a) the residual A_t exceeds its 100-shuffle label null (Table 2 rows g to i, the only\n    test the paper reports on residual structure); (b) residual eta squared exceeds the mean of a\n    100-shuffle t-type label null on the residualized scores (Methods, \"Label-shuffle null\n    distributions used 100 permutations\"). Residual eta squared is reported in each regime.\n    Reproduced when the three A_t are within tolerance with p < 0.05 and residual structure is\n    detectable under one reading in each regime; partially reproduced when every A_t has p <\n    0.05 but some value is out of tolerance. The brief-pulse tolerance (0.0004) is 10% of a\n    value that is itself small."
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
 "old_string": "  criterion: The cutoff grids are those of the code's figure (scripts/figures_eneuro_supplement.py,\n    Extended Data Figure 3-2D,E); selective rank-range cutoffs 0.45, 0.50, 0.55, 0.60 and 0.65,\n    and stable rank-CV cutoffs 0.15, 0.20, 0.25, 0.30 and 0.35, each varied with the other held\n    at its default. The paper does not say what \"stable\" proportions means; readings are (a)\n    across each grid, the selective fraction stays below 20% and below the stable fraction\n    (the minority status the claim rests on); (b) across each grid, the varied fraction changes\n    by no more than 10 percentage points between neighboring cutoffs. Reproduced when both\n    readings hold; partially reproduced when one does. The fractions at every cutoff are shown.",
 "new_string": "  criterion: The cutoff grids are those of the code's figure (scripts/figures_eneuro_supplement.py,\n    Extended Data Figure 3-2D,E); selective rank-range cutoffs 0.45, 0.50, 0.55, 0.60 and 0.65,\n    and stable rank-CV cutoffs 0.15, 0.20, 0.25, 0.30 and 0.35, each varied with the other held\n    at its default. The paper sets no bound on what \"stable\" proportions or \"modest\" variation\n    mean. The claim is judged on the pattern the Results describe (\"a smaller subset\" of\n    selective pairs against a shared backbone); reproduced when, at every cutoff of both grids,\n    the selective fraction is below both the stable and the intermediate fractions. The three\n    fractions at every cutoff, and their change from the default cutoff, are reported, not\n    judged."
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
 "old_string": "  criterion: Read from the paper's numbers, without a new test. Reproduced when, for each regime\n    pair, the type-map concordance (fig3a-type-map-concordance) exceeds the cell-cell distance\n    correlation (fig1b-distance-correlation) and the mean 15-NN Jaccard (fig1c-knn-jaccard) is\n    below 0.05 for each pair.",
 "new_string": "  criterion: Read from the paper's numbers, without a new test; the paper gives none and no\n    threshold. The comparison on a common scale is the Spearman correlation at the two levels.\n    Reproduced when, for each regime pair, the type-map concordance (fig3a-type-map-concordance)\n    exceeds the cell-cell distance correlation (fig1b-distance-correlation). The mean 15-NN\n    Jaccard of fig1c-knn-jaccard is reported beside them, not judged against a bound."
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
 "old_string": "    phenotype values across pairs, two-sided; readings as there). Reproduced when the\n    correlations with mean S are within tolerance with p < 0.05 and each panel's correlation\n    with mean S exceeds its correlation with rank range by more than 0.3; partially reproduced",
 "new_string": "    phenotype values across pairs, two-sided; readings as there). The asymmetry is judged with\n    the code's own rule for the primary panel (scripts/q3bc_explain.py, main, landing\n    \"rna_tracks_phenotype_distance\"; the paper states none), applied to each panel; rho with\n    mean S at least 0.25 and |rho| with rank range below 0.15. Reproduced when the\n    correlations with mean S are within tolerance with p < 0.05 and the asymmetry rule holds for\n    each panel; partially reproduced"
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
 "old_string": "    Cav; partially reproduced when every |rho| is below 0.1 but the largest is out of tolerance\n    or belongs to another module.",
 "new_string": "    Cav; partially reproduced when every |rho| is below 0.10 but the largest is out of tolerance\n    or belongs to another module. The paper gives no bound for \"negligible\" here; 0.10 is the\n    bound it uses for a retained association in the WGCNA analysis (Results, paragraph 3; Table\n    2 row y), borrowed as an assumption."
}
```

```
The file claims/yang-2026-flexible.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -rn "checks" schemas/* | head; grep -l "^checks:" claims/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
schemas/claims.schema.json:209:    "checks": {
schemas/paper-match.schema.json:27:          "by": {"type": "string", "description": "checks, agent, or the name of the person who set the verdict."},
schemas/paper-match.schema.json:43:          "checks": {
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the others as variants. Said that p < 0.001 for a printed 0 is this file's reading.
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 fo
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/yang-2026-flexible.yaml <<'EOF'
checks:
- date: 2026-11-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - pc1-long-pulse-loadings. The current features left out hero_sweep.stim_amp, which IPFX sets at a fixed offset above rheobase; it is a rheobase-tied current, and leaving it out could make reading (a) fail on a feature the paper's phrase covers. Added it and said why; reading (a) now compares kinds of feature.
  - ttype-beyond-cre. The test for "residual t-type structure remained detectable" (residual eta squared above a shuffle-null mean) was given as the paper's, but the paper reports no residual eta squared and says eta squared has no permutation p. Now open, with two readings (residual A_t above its null, Table 2 rows g to i; residual eta squared above a label-shuffle null).
  - type-level-exceeds-cell-level. Removed the bound "mean 15-NN Jaccard below 0.05"; it is not in the paper. The claim is judged on type-map concordance against cell-cell distance correlation, both Spearman; the Jaccard is reported.
  - pair-tag-threshold-sensitivity. Removed the bounds "below 20%" and "no more than 10 percentage points"; neither is in the paper or the code. Judged now on the ordering the Results describe (selective below stable and intermediate at every cutoff of the code's grids), with the fractions reported.
  - fig4-alternative-panels. Replaced the made-up margin "by more than 0.3" with the code's own asymmetry rule (scripts/q3bc_explain.py, rho with mean S at least 0.25 and |rho| with rank range below 0.15), cited as such.
  - fig4c-no-module-tracks-rank-range. The 0.10 bound for the partial outcome had no source; said it is borrowed from the paper's WGCNA threshold (Table 2 row y) as an assumption.
  - Checked, unchanged. Every quote, p-value, n and expected value against the text and Table 2; the criteria against the code at commit 61a5a41 (q1_describe_phenotype.py, q1_knn_scale.py, q2_anchor.py, q3a_explain.py, q3a_centroid_robustness.py, q3bc_explain.py, q3_mobility_modules.py, q3_wgcna_mobility.py, q3_wgcna_modules.R, figures_eneuro_supplement.py), including the ordinal-rank Spearman, the Cre cell set, the kNN enrichment as a ratio of means, the type-label null, the tag order, the subclass pair order (long-brief 0.579, ramp-brief 0.621), the module distances and the equal-N tolerances.
  - Open. The Extended Data figures and the DOCX tables (1-1, 2-1, 3-1, 4-1, 4-3) are not in the text and no PDF was supplied; only their legends were read. No expected value rests on them.
  - Open. The script that ran IPFX on all cells, and the one that made the 1,000-shuffle null of Table 2 rows m and n, are not in the code; the claims name readings for both (table1-phenotype-spaces, fig4ab-rna-tracks-shared-map).
  - Open. The hierarchical subtype alignment and the Cre alignment of Extended Data Figure 2-1A have no number in the text and no claim.
EOF
python tools/claims_check.py claims/yang-2026-flexible.yaml paper/10.1523-eneuro.0275-26.2026.txt; grep -n "—\|rather" claims/yang-2026-flexible.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
M claims/yang-2026-flexible.yaml
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
?? scripts
```

**Agent**

The claims file is ready for an attempt. I made six corrections to criteria. Every quote, p-value, n and expected value was already right.

**Checker result:** `claims/yang-2026-flexible.yaml: 29 claims, 29 quotes, 26 statistical values, 0 problems`. I ran it before and after my edits, with the same result.

I also cloned the paper's code at the commit the file cites (61a5a41) into a temporary folder and checked each criterion against it. Nearly everything the file attributes to the code is there.

**Changes, by claim**
- **pc1-long-pulse-loadings:** I added `hero_sweep.stim_amp` to the current features. Its amplitude is set at a fixed offset above rheobase, so the paper's "rheobase/threshold current" covers it; leaving it out could have made reading (a) fail on a technicality.
- **ttype-beyond-cre:** The test for "residual t-type structure remained detectable" (residual η² above a shuffle null) was presented as the paper's own. The paper prints no residual η² value and no test for it. It is now marked open, with two readings: residual A_t above its null (Table 2 rows g–i), or residual η² above a label-shuffle null.
- **type-level-exceeds-cell-level:** I removed a made-up bound (15-NN Jaccard below 0.05). The claim is now judged on type-map concordance against cell–cell distance correlation; the Jaccard values are reported but not judged.
- **pair-tag-threshold-sensitivity:** I removed two made-up bounds (20%, and 10 percentage points). The claim is now judged on the ordering the Results describe: at every cutoff in the code's grids, the selective fraction is below both the stable and the intermediate fractions.
- **fig4-alternative-panels:** I replaced an invented margin ("more than 0.3") with the code's own asymmetry rule from `q3bc_explain.py`: ρ with mean S of at least 0.25, and |ρ| with rank range below 0.15.
- **fig4c-no-module-tracks-rank-range:** The 0.10 bound used for a partial result had no source. It now says the bound is borrowed, as an assumption, from the paper's WGCNA threshold (Table 2 row y).

Every change, with its reason, is in the new `checks` entry at the end of the file. No claim ids were changed.

**Still open**
- The Extended Data figures and the DOCX tables are not in the text, and no PDF was supplied, so only their legends were read. No expected value depends on them.
- The code lacks the script that ran IPFX on all cells and the one that produced the 1,000-shuffle null for Table 2 rows m and n. The claims already name readings for both.
- The hierarchical-subtype and Cre alignments in Extended Data Figure 2-1A have no numbers in the text, so they have no claim.

The only tracked change is to `claims/yang-2026-flexible.yaml`; nothing is committed or pushed. Git also shows some untracked files at the repository root (dotfiles, `.idea`, `.vscode`, `scripts`). I left them alone; the `scripts` folder was already there before I made any changes.

## End of run

39 turns, 5 minutes, $2.05 at API prices, result: success.
