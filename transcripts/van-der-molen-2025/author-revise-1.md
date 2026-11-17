# van-der-molen-2025 · author-revise-1 · run 44140543710

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/van-der-molen-2025/verifier-1-report.md; ls entries/van-der-molen-2025 entries/van-der-molen-2025/*
```

```
Tue Nov 17 17:54:40 UTC 2026
**Verifier report, round 1: van der Molen et al. 2025 on DANDI:001603 (0.260923.0623)**

The claims file has 50 claims. The notebook tests 47 of them and marks three as blocked: supp8, supp27 and supp5.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| methods-burst-count | reproduced | Cell 11: the mean is 35.7, inside 38 ± 4. The SE is 6.2 against the paper's 4, and the agreement is fragile: four murine organoids have 0 bursts, offset by MO1 (113) and MO7 (156). |
| fig1c-example-burst-count | reproduced | Cell 13: HO1 has 46 bursts at both 700 and 800 ms. |
| ed1c-lognormal-rates | reproduced | Cell 16, reading (a) with all units: all-unit R² is 0.949 and backbone R² is 0.487 (7 fits, because HO7 has no backbone unit). Both are within tolerance. |
| fig1d-burst-duration | reproduced | Cell 18: HO1 to HO4 medians are 472 to 892 ms. |
| fig1e-peaks-near-burst-peak | blocked: methods_underspecified | Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree. |
| fig2-backbone-fraction | reproduced | Cell 22, reading (b) (units with at least 30 spikes): mean 0.331, SD 0.150, both within tolerance. Under reading (a) the SD of 0.166 is outside tolerance. |
| fig2e-b2b-correlation | reproduced | Cell 24: p 5.9e-36 (30% rule) and 1.5e-19 (70% rule). The test used 216 units. The 507 printed is all sorted units, which is a different quantity. |
| fig2g-variance-latency | reproduced | Cell 26: positive slope, p 3.6e-4 under reading (a) and 4.5e-5 under (b). |
| ed3f-burst-cluster-variability | reproduced | Cell 28: non-rigid CV is higher under all four readings, p ≤ 5e-48. |
| ed4b-gabazine-more-bursts | reproduced | Cell 32: +7.0 bursts per minute, p 5.5e-6. There are 4 paired organoids (MO12 has no baseline sorted file). |
| ed4b-nbqx-cpp-abolish-bursts | reproduced | Cell 34: treated recordings have 0, 0, 1, 0 and 0 bursts; p 3e-53. |
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
647 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
159:### 4. Data from outside the paper's own recordings
167:### 5. Check
180:### 6. Answer questions
193:## Author
209:### 1. Establish what can be tested
339:### 2. Check the data against its description
354:### 3. Write the entry
422:### 4. Lock, check and run
433:### 5. Record the attempt
495:### 6. Hand over for verification
533:## Repeat attempts
575:## Local and remote datasets
598:## Verifier
602:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 193,575p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 364 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep molen; ls executed/van-der-molen-2025/ 2>/dev/null; cat entries/van-der-molen-2025/entry.yaml; wc -l entries/van-der-molen-2025/*.py; ls questions | grep molen; git log --oneline | head -5; ls transcripts/van-der-molen-2025/
```

```
van-der-molen-2025-01.yaml
hmm_van_der_molen_2025.ipynb
reproduce_van_der_molen_2025.ipynb
result.json
schema_version: 1
name: van-der-molen-2025
type: reproduction
title: Preconfigured firing sequences in brain organoids (van der Molen et al. 2025)
description: Tests the findings of van der Molen, Spaeth, Chini et al. (2025) on dandiset 001603,
  which holds the sorted spike trains of 8 human organoids, 9 murine organoids, 6 neonatal mouse
  slices and 8 primary cultures, murine organoids treated with gabazine and with NBQX and R-CPP, and
  longitudinal human organoid recordings. It detects population bursts and backbone units, and
  compares burst-to-burst and pairwise correlations, burst similarity, PCA and hidden Markov models
  between unit groups and model types.
license: Apache-2.0
notebooks:
- path: reproduce_van_der_molen_2025.ipynb
  title: Bursts, backbone units, correlations and model comparisons (Figs. 1 to 4, 6 and 7)
  runtime_minutes: 23
- path: hmm_van_der_molen_2025.ipynb
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/van-der-molen-2025-01.yaml | head -400; wc -l attempts/van-der-molen-2025-01.yaml
```

```
schema_version: 3
id: van-der-molen-2025-01
datasets:
- archive: dandi
  id: "001603"
  version: 0.260923.0623
  doi: 10.48324/dandi.001603/0.260923.0623
  relation: primary
paper: doi:10.1038/s41593-025-02111-0
date: 2026-11-17
entry: van-der-molen-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,478p attempts/van-der-molen-2025-01.yaml; ls questions/ | head; cat docs/*.md | grep -n "verifications" | head -20
```

```
- claim: supp26-state-traversal
  outcome: reproduced
  notebook: hmm_van_der_molen_2025.ipynb
  output: claim:supp26-state-traversal
  notes: Primary cultures traverse more states per second than human organoids (20.2, p 3e-6) and
    slices (11.7, p 0.0095); human and murine organoids do not differ (4.4, p 0.37). Primary cultures
    also exceed murine organoids (p 3e-7), where the paper reports P 0.064.
- claim: supp27-d2-near-critical
  outcome: blocked
  blocked_by: other
  notes: Not run in this attempt. The run's time went to the other 49 claims; the d2 code of Sooter et
    al. (figshare article 25927081, version 1, which the paper's r_download.sh fetches) was not fetched
    or run, and the AR fit check that selects the preparations is not specified beyond "within one
    order of magnitude". The spike data it needs are in the dandiset.
- claim: ed2d-alam-el-din-rates
  outcome: not_reproduced
  notebook: reproduce_van_der_molen_2025.ipynb
  output: claim:ed2d-alam-el-din-rates
  notes: Backbone units fire faster in HO1 to HO4 (0.72 log10 units, p 1e-77) and also in HO5 to HO8
    (0.12, p 0.0018), where the paper finds P 0.40.
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -60; ls schemas 2>/dev/null; grep -rn "verifications" tools/*.py | head
```

```
attempts/amjad-2025-01.yaml
attempts/armstrong-2026-01.yaml
attempts/ashworth-2025-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
      not in the archive.
[... 57 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/van-der-molen-2025/sequences.py"
}
```

**Agent calls Read**

```json
{
 "file_path": "entries/van-der-molen-2025/hmm.py"
}
```

```
1	"""Poisson hidden Markov models for van der Molen et al. (2025), in place of the SSM package.
2	
3	The paper fits HMMs with Poisson observations using SSM (Supplementary Methods, "Hidden Markov
4	model analysis"), on spike counts in 30 ms bins, with 10 to 30 hidden states, by EM (the code's
5	tolerance 1e-3, at most 5000 iterations; claims file). SSM is not on PyPI in a form that installs in
6	a locked environment, so this module implements the same model: a stationary transition matrix, an
7	initial state distribution, and one Poisson rate per unit and state, fitted by Baum-Welch EM. The
8	initialisation (k-means on the binned counts, transitions with 0.9 on the diagonal) is a standard
9	choice; the iteration limit (300) is lower than the code's, a deviation stated in the notebook.
10	"""
11	import numba
12	import numpy as np
13	from scipy.special import gammaln
14	
15	BIN_MS = 30  # Supplementary Methods
16	TOL = 1e-3  # claims file (the code's tolerance)
17	MAX_ITER = 300
18	
19	
20	def bin_counts(M, bin_ms=BIN_MS):
[... 115 more lines not kept]
```

```
1	"""Loading and measures for van der Molen, Spaeth, Chini et al. (2025) on DANDI:001603.
2	
3	Every recording is read from the dandiset's sorted files at the pinned version, by streaming
4	(remfile and h5py), from the 1 ms spike matrix ``processing/curated_binning/t_spk_mat`` that each
5	sorted file holds. That matrix is the input of the paper's own code (the claims file, opening
6	comment: "Spike matrix at 1 ms resolution"). It marks a bin as 1 when it holds at least one spike.
7	
8	Where each parameter comes from is said beside it:
9	- "claims" means the claims file's opening comment or the claim's criterion, which cite the paper's
10	  Methods or its code (github.com/braingeneers/Protosequences at e9a79c4);
11	- "paper" means a passage of the paper taken by the author (protocol, author step 1.6), cited;
12	- "standard choice" means a detail that cannot change an outcome beyond noise.
13	"""
14	import json
15	import urllib.request
16	
17	import h5py
18	import numba
19	import numpy as np
20	import remfile
[... 736 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python - <<'EOF'
import json
for nb in ["reproduce_van_der_molen_2025.ipynb","hmm_van_der_molen_2025.ipynb"]:
    d=json.load(open(nb))
    out=open(f"/tmp/claude/{nb}.txt" if False else f"{__import__('os').environ['TMPDIR']}/{nb}.txt","w")
    for i,c in enumerate(d["cells"]):
        out.write(f"\n##### CELL {i} [{c['cell_type']}] tags={c.get('metadata',{}).get('tags')}\n")
        out.write("".join(c["source"])+"\n")
    print(nb,len(d["cells"]))
EOF
wc -l $TMPDIR/*.txt
```

```
reproduce_van_der_molen_2025.ipynb 132
hmm_van_der_molen_2025.ipynb 28
  417 /tmp/claude-1001/hmm_van_der_molen_2025.ipynb.txt
 1392 /tmp/claude-1001/reproduce_van_der_molen_2025.ipynb.txt
 1809 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_van_der_molen_2025.ipynb.txt",
 "limit": 420
}
```

```
1	
2	##### CELL 0 [markdown] tags=None
3	# Reproducing van der Molen, Spaeth, Chini et al. (2025) from dandiset 001603
4	
5	**Paper.** van der Molen T, Spaeth A, Chini M, et al. (2025). Preconfigured neuronal firing
6	sequences in human brain organoids. *Nature Neuroscience*.
7	[doi:10.1038/s41593-025-02111-0](https://doi.org/10.1038/s41593-025-02111-0). The claims file was
8	written from the NIH author manuscript in PubMed Central (PMC12912721.1) with the publisher's
9	Supplementary Information; this attempt read the same text.
10	
11	**Dandiset.** [DANDI:001603](https://dandiarchive.org/dandiset/001603/0.260923.0623), version
12	0.260923.0623. The paper cites no version of the dandiset. This is the only published version and
13	the most recent one; the draft has the same 111 assets and size, so the published version is
14	pinned.
15	
16	**What is used.** The sorted files only: each holds a 1 ms binary spike matrix
17	(`processing/curated_binning/t_spk_mat`, the input of the paper's code), and most also a units
18	table. Recordings are cut to the code's lengths (180 s for HO1 to HO4, slices and primary
19	cultures; 600 s for HO5 to HO8 and murine organoids). The raw `_ecephys` files are not read.
20	
[... 400 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_van_der_molen_2025.ipynb.txt",
 "offset": 420,
 "limit": 500
}
```

```
420	    return np.array(out)
421	
422	
423	def kneedle(ks, sse):
424	    """Knee of a decreasing convex curve: the point farthest below the chord (Satopaa et al.)."""
425	    x = (np.array(ks) - ks[0]) / (ks[-1] - ks[0])
426	    y = (np.array(sse) - min(sse)) / (max(sse) - min(sse))
427	    return ks[int(np.argmax((1 - x) - y))]
428	
429	
430	rows, kinfo = [], []
431	for k in HO8:
432	    r = R[k]
433	    seg = r["segments"]
434	    V = burst_corr_vectors(seg)
435	    ks = list(range(2, min(10, len(V) - 1) + 1))
436	    sse, sil, labels = [], [], {}
437	    for kk in ks:
438	        best = None
439	        for seed in range(10):
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_van_der_molen_2025.ipynb.txt",
 "offset": 919,
 "limit": 480
}
```

```
919	##### CELL 80 [markdown] tags=None
920	## fig4f-pca-variance
921	
922	> In the example organoid, the first two principal components of backbone unit rates explain 73%
923	> of their variance against 25% for non-rigid units, and across organoids backbone units need
924	> fewer components than all units while non-rigid units need more.
925	
926	##### CELL 81 [code] tags=['claim:fig4f-pca-variance']
927	rows = []
928	for k in HO8:
929	    p = R[k]["pca"]
930	    rows.append(dict(rec=k, **{f"{s}_2pc": (100 * p[s][:2].sum() if p[s] is not None else np.nan) for s in ["all", "bb", "nr"]}))
931	f4f = pd.DataFrame(rows)
932	f4f["bb_gt_all"] = f4f.bb_2pc > f4f.all_2pc
933	f4f["nr_lt_all"] = f4f.nr_2pc < f4f.all_2pc
934	print(f4f.round(1).to_string(index=False))
935	print("Expected for the example organoid: backbone 73 +- 7.3, non-rigid 25 +- 2.5 percent")
936	match = f4f[(f4f.bb_2pc.between(65.7, 80.3)) & (f4f.nr_2pc.between(22.5, 27.5))]
937	print("Organoids matching both:", match.rec.tolist())
938	
[... 455 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hmm_van_der_molen_2025.ipynb.txt"
}
```

```
1	
2	##### CELL 0 [markdown] tags=None
3	# Hidden Markov models: van der Molen et al. (2025) on dandiset 001603
4	
5	The HMM claims of the paper (Figs. 5 and 7F, Supplementary Figs. 18, 24D and 26), on
6	[DANDI:001603](https://dandiarchive.org/dandiset/001603/0.260923.0623) version 0.260923.0623,
7	the only published version (see the header of `reproduce_van_der_molen_2025.ipynb` for the
8	choice of version and the data check).
9	
10	**Model.** Poisson-observation HMMs on spike counts in 30 ms bins (Supplementary Methods), fitted
11	by EM in `hmm.py`, which implements the model of the SSM package the paper used (SSM does not
12	install from PyPI in a locked environment). The recording lengths are the code's (180 s or 600 s),
13	burst peaks and backbone units are as in the main notebook (`sequences.py`).
14	
15	**Deviations for runtime.** The paper fits every K from 10 to 30 (21 models per recording); this
16	notebook fits K = 10, 12, ..., 30 (11 models per recording), with at most 300 EM iterations where
17	the code allows 5000. The cross-validation of Supplementary Fig. 18 uses K = 10, 20 and 30.
18	
19	| Claim | Tested here |
20	|---|---|
[... 398 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/ | grep molen; python - <<'EOF'
import yaml
c=yaml.safe_load(open("claims/van-der-molen-2025.yaml"))
print(c.keys() if isinstance(c,dict) else type(c))
cl=c["claims"]
for x in cl:
    if x["id"] in ("fig1e-peaks-near-burst-peak","fig3f-backbone-pairs-in-tail","supp8-backbone-stable-4h","supp27-d2-near-critical","fig5f-svm-states-beat-rate","fig7d-murine-organoids-slices-same-lag","supp5-murine-organoid-forebrain-identity","ed4d-gabazine-rank-order","supp10b-rank-order-by-model","supp18-hmm-likelihood-real-above-shuffled"):
        print(yaml.safe_dump(x,width=110,sort_keys=False))
EOF
```

```
van-der-molen-2025.yaml
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
id: fig1e-peaks-near-burst-peak
statement: Most units reach their peak firing rate close to the peak of the population burst.
source: Results, Temporal dynamics of neuronal firing sequences, paragraph 1; Figure 1E
quote: A majority of units firing rates peaked in close proximity to the population burst maxima ( Fig. 1E )
criterion: "Peak time per unit and burst, the time of its maximum rate between burst start and end relative to the\
  \ burst peak, in bursts where it fires at least two spikes (Methods). HO1 to HO4. \"Close proximity\" is not fixed\
  \ by the paper. Readings for the quantity, (i) each unit's median peak time, (ii) all unit-burst peak times pooled;\
  \ for the bound, (a) within 50 ms and (b) within 100 ms of the burst peak (the Results speak of lags near 10 ms\
  \ and sequences of about 10\xB2 ms). Reproduced when more than half of the values fall within the bound in each\
  \ organoid, under every reading."

id: ed4d-gabazine-rank-order
statement: Gabazine makes the order of backbone sequences more consistent across bursts.
source: Extended Data Fig. 4D
quote: "There is a significant increase in backbone sequence order similarity after treatment with gabazine ( P\
  \ < 10 \u221220 , two-sided linear mixed-effect model)"
statistics:
- test: two-sided linear mixed-effect model
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 6000 claims/van-der-molen-2025.yaml; grep -n -i "2000 ms\|min_dist\|minimum distance\|minimal distance" paper/* | head -20; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 20,80p claims/van-der-molen-2025.yaml; ls paper/; grep -rn -i "2000 ms\|2,000 ms" paper/ | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | head; grep -n -i "recording length\|40 bursts\|about 40\|KEEP_DURATION" claims/van-der-molen-2025.yaml | cut -c1-400 | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 40,70p claims/van-der-molen-2025.yaml | cut -c1-300; grep -n -i -o ".\{300\}2000.\{200\}" paper/10.1038-s41593-025-02111-0.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; date -u; ls ~/.cache 2>/dev/null | head; python -c "import sys; print(sys.version)"; pip list 2>/dev/null | grep -i -E "numba|scipy|statsmodels|remfile|h5py|pandas"
```

```
Tue Nov 17 17:56:22 UTC 2026
3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_\|uv " tools/entry.py | head -40; ls -a; ls executed/van-der-molen-2025
```

```
521:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
557:    venv = (output_dir / ".venv").resolve()
558:    python = venv / "bin" / "python"
562:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
565:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
579:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 540,600p tools/entry.py; cat entries/van-der-molen-2025/requirements.in
```

```
return stamp
    except (OSError, ValueError, KeyError, TypeError):
        return None


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv --quiet --clear $TMPDIR/venv --python 3.13 && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/van-der-molen-2025/requirements.lock.txt && $TMPDIR/venv/bin/python -c "import numba, scipy; print('ok')"; nproc; free -g
```

```
ok
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          14
Swap:              0           0           0
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/survey.py <<'EOF'
import sys, time, pickle
sys.path.insert(0, "entries/van-der-molen-2025")
import numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
import sequences as sq
t0=time.time()
assets = sq.list_assets()
sa = [a for a in assets if "_ecephys" not in a["path"]]
with ThreadPoolExecutor(8) as ex:
    infos = list(ex.map(sq.sorted_file_info, sa))
files = sq.recording_table(assets, infos)
first = files.sort_values("path").groupby("recording").first()
first.to_pickle(f"{sys.argv[1]}/first.pkl")
def go(name):
    M = sq.load_matrix(first.loc[name].asset_id, sq.keep_seconds(name))
    np.save(f"{sys.argv[1]}/{name}.npy", np.packbits(M, axis=1)); 
    out = dict(rec=name, U=M.shape[0], T=M.shape[1])
    for md in (700, 800, 2000):
        b = sq.detect_bursts(M, sq.model_type(name), md)
        key = set(zip(b["start"], b["end"]))
        out[f"n{md}"] = len(b["peak"]); out[f"uniq{md}"] = len(key)
    out["rms"]=b["rms"]
    c=b["coarse"]; out["thr"]=4*b["rms"]; out["max_coarse"]=c.max(); 
    return out
with ThreadPoolExecutor(4) as ex:
    rows=list(ex.map(go, sq.MAIN))
print(pd.DataFrame(rows).round(2).to_string()); print(time.time()-t0)
EOF
mkdir -p $TMPDIR/data; cd $TMPDIR/dev && $TMPDIR/venv/bin/python survey.py $TMPDIR/data
```

```
rec    U       T  n700  uniq700  n800  uniq800  n2000  uniq2000   rms    thr  max_coarse
0    HO1  131  180000    46       46    46       46     46        46  0.41   1.64        2.46
1    HO2  173  180000    31       31    31       31     31        31  0.24   0.94        1.88
2    HO3   80  180000    42       42    42       42     42        42  0.19   0.75        1.31
3    HO4  123  180000    28       28    28       28     28        28  0.21   0.84        1.31
4    HO5  308  600000    20       20    20       20     11        11  0.29   1.15        2.45
5    HO6   50  600000    33       32    33       32     22        22  0.08   0.32        0.95
6    HO7   30  599940    24       24    23       23     14        14  0.05   0.20        0.89
7    HO8   35  599970    23       23    21       21     13        13  0.05   0.19        0.50
8    MO1  103  600000   113      113   113      113    102       102  1.22   4.89        5.62
9    MO2  199  600000     0        0     0        0      0         0  2.28   9.11        6.79
10   MO3  234  600000     4        4     4        4      4         4  1.08   4.32        4.49
11   MO4  194  600000     0        0     0        0      0         0  1.57   6.28        5.86
12   MO5   86  600000     0        0     0        0      0         0  1.28   5.12        4.75
13   MO6  170  600000     0        0     0        0      0         0  1.13   4.51        4.12
14   MO7   82  600000   156      156   156      156    154       154  0.98   3.91        5.10
15   MO8   48  600000    65       65    65       65     65        65  0.34   1.34        1.84
16   MO9  157  600000    22       22    22       22     20        20  1.02   4.08        5.44
17  M1S1  139  180000    24       24    24       24     22        22  0.31   1.23        3.54
18  M1S2  411  180000    23       23    21       21     16        16  0.91   3.64        6.35
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/overlap.py <<'EOF'
import sys
sys.path.insert(0, "entries/van-der-molen-2025")
import numpy as np, sequences as sq
D="/tmp/claude-1001/data"
for name in sq.MAIN:
    p=np.load(f"{D}/{name}.npy"); M=np.unpackbits(p,axis=1).astype(bool)
    T=int({"HO":0}.get("",0)) 
    b=sq.detect_bursts(M, sq.model_type(name))
    s,e=b["start"],b["end"]; o=np.argsort(s); s,e=s[o],e[o]
    ov=int((s[1:]<=e[:-1]).sum())
    if ov: print(name, len(s), "overlapping consecutive:", ov)
EOF
$TMPDIR/venv/bin/python $TMPDIR/dev/overlap.py
```

```
HO5 20 overlapping consecutive: 3
HO6 33 overlapping consecutive: 9
HO7 24 overlapping consecutive: 3
HO8 23 overlapping consecutive: 4
MO9 22 overlapping consecutive: 2
M1S2 23 overlapping consecutive: 4
M2S1 11 overlapping consecutive: 1
M3S1 12 overlapping consecutive: 1
M3S2 7 overlapping consecutive: 1
Pr7 42 overlapping consecutive: 2
```

**Agent calls Bash**

```bash
curl -s -m 20 https://api.figshare.com/v2/articles/25927081/versions/1 | head -c 1500; echo; grep -n -i -A3 "d2 calculation\|d 2 calculation" paper/*.txt | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  sed -n 975,1010p paper/*.txt; curl -s -m 20 https://api.figshare.com/v2/articles/25927081/versions/1 | python -c "
import json,sys; d=json.load(sys.stdin)
for f in d['files']: print(f['name'], f['size'], f['download_url'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in 46655761:getDbetas.m 46655764:getFixedPointDistance.m 46655734:myYuleWalker.m 46655773:test.m; do id=${f%%:*}; n=${f#*:}; curl -sL -m 30 https://ndownloader.figshare.com/files/$id -o $n; echo "=== $n"; cat $n; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in 46655788:myAutocorr.m 46655749:getFR.m; do id=${f%%:*}; n=${f#*:}; curl -sL -m 30 https://ndownloader.figshare.com/files/$id -o $n; echo "=== $n"; cat $n; done; sed -n 1010,1025p paper/*.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in 46655743:getAvalanches.m 46655770:getARstats.m 46655731:simAR.m 46655737:simARwindowed.m 46655794:myPSD.m; do id=${f%%:*}; n=${f#*:}; curl -sL -m 30 https://ndownloader.figshare.com/files/$id -o $n; echo "=== $n"; cat $n; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov 17 17:59:54 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "old_string": "    \"\"\"Population bursts (claims, opening comment; Methods \"Population rate calculations\").\n\n    Returns a dict with arrays start, end and peak (frames) and the coarse population rate.\"\"\"\n    p = BURST_PARAMS[\"PR\"] if mtype == \"PR\" else BURST_PARAMS[\"default\"]\n    pop = M.sum(0).astype(float)\n    coarse = gauss(movmean(pop, p[\"square_ms\"]), p[\"gauss_ms\"])\n    fine = gauss(movmean(pop, 5), 5)\n    rms = np.sqrt(np.mean(coarse ** 2))\n    pk, _ = signal.find_peaks(coarse, height=p[\"rms_mult\"] * rms, distance=min_dist_ms)\n    T = len(coarse)\n    starts, ends, peaks = [], [], []\n    for k in pk:\n        thr = p[\"edge_frac\"] * coarse[k]\n        below = np.nonzero(coarse[:k] < thr)[0]\n        s = below[-1] if len(below) else 0\n        above = np.nonzero(coarse[k:] < thr)[0]\n        e = k + above[0] if len(above) else T - 1\n        pt = s + int(np.argmax(fine[s:e + 1]))\n        starts.append(s)\n        ends.append(e)\n        peaks.append(pt)\n    starts, ends, peaks = (np.array(x, dtype=int) for x in (starts, ends, peaks))\n    keep = (peaks >= EDGE_DROP_START_MS) & (peaks <= T - EDGE_DROP_END_MS)\n    return dict(start=starts[keep], end=ends[keep], peak=peaks[keep], coarse=coarse,\n                rms=rms, n_raw=len(pk))",
 "new_string": "    \"\"\"Population bursts (claims, opening comment; Methods \"Population rate calculations\").\n\n    A peak in the tail of a long burst, where the rate never falls below the edge fraction between\n    the two peaks, gives a second burst that overlaps the first. The Methods avoid this by raising\n    the minimum peak distance \"up to 2000 ms\" for \"recordings with long duration bursts ... to\n    prevent peaks in the tail of the burst from being detected as separate burst instances\", without\n    saying for which recordings. Here every recording keeps 700 ms, and of bursts that overlap only\n    the one with the highest peak of the coarse rate is kept (an assumption that applies the stated\n    purpose to every recording; 2000 ms for all is a variant in the notebook).\n\n    Returns a dict with arrays start, end and peak (frames), the coarse population rate, its RMS, the\n    number of peaks found and the number of overlapping bursts dropped.\"\"\"\n    p = BURST_PARAMS[\"PR\"] if mtype == \"PR\" else BURST_PARAMS[\"default\"]\n    pop = M.sum(0).astype(float)\n    coarse = gauss(movmean(pop, p[\"square_ms\"]), p[\"gauss_ms\"])\n    fine = gauss(movmean(pop, 5), 5)\n    rms = np.sqrt(np.mean(coarse ** 2))\n    pk, _ = signal.find_peaks(coarse, height=p[\"rms_mult\"] * rms, distance=min_dist_ms)\n    T = len(coarse)\n    starts, ends, peaks = [], [], []\n    for k in pk:\n        thr = p[\"edge_frac\"] * coarse[k]\n        below = np.nonzero(coarse[:k] < thr)[0]\n        s = below[-1] if len(below) else 0\n        above = np.nonzero(coarse[k:] < thr)[0]\n        e = k + above[0] if len(above) else T - 1\n        pt = s + int(np.argmax(fine[s:e + 1]))\n        starts.append(s)\n        ends.append(e)\n        peaks.append(pt)\n    starts, ends, peaks = (np.array(x, dtype=int) for x in (starts, ends, peaks))\n    keep = np.zeros(len(pk), bool)\n    for i in np.argsort(-coarse[pk], kind=\"stable\"):\n        if not (keep & (starts <= ends[i]) & (ends >= starts[i])).any():\n            keep[i] = True\n    n_overlap = int((~keep).sum())\n    keep &= (peaks >= EDGE_DROP_START_MS) & (peaks <= T - EDGE_DROP_END_MS)\n    return dict(start=starts[keep], end=ends[keep], peak=peaks[keep], coarse=coarse,\n                rms=rms, n_raw=len(pk), n_overlap=n_overlap)"
}
```

```
The file entries/van-der-molen-2025/sequences.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "old_string": "def burst_to_burst(M, bursts, min_frac=0.3, min_spikes=MIN_SPIKES, R=None):\n    \"\"\"Burst-to-burst correlation per unit (claims, fig2e-b2b-correlation; Methods).\n\n    Burst-only rates; per pair of bursts in which the unit has at least two spikes in the -250 to\n    500 ms window, the maximum xcorr coefficient within 10 ms; the mean over those pairs. Units kept\n    with at least two spikes in at least min_frac of the bursts and at least min_spikes spikes.\n    Returns an array with NaN for units not kept.\"\"\"\n    U, T = M.shape\n    if R is None:\n        R = isi_rates(M, bursts)\n    peaks = bursts[\"peak\"]\n    win = peaks[:, None] + np.arange(-WIN_PRE, WIN_POST + 1)[None, :]\n    win = np.clip(win, 0, T - 1)\n    cnt_win = M[:, win].sum(2)  # units by bursts\n    active = cnt_win >= 2\n    keep = (active.mean(1) >= min_frac) & (M.sum(1) >= min_spikes)",
 "new_string": "def burst_to_burst(M, bursts, min_frac=0.3, min_spikes=MIN_SPIKES, R=None, n_spk=None):\n    \"\"\"Burst-to-burst correlation per unit (claims, fig2e-b2b-correlation; Methods).\n\n    Burst-only rates; per pair of bursts in which the unit has at least two spikes in the -250 to\n    500 ms window, the maximum xcorr coefficient within 10 ms; the mean over those pairs. Units kept\n    with at least two spikes in at least min_frac of the bursts and at least min_spikes spikes in the\n    whole recording (n_spk; M's own counts when not given). Returns an array with NaN for units not\n    kept.\"\"\"\n    U, T = M.shape\n    if R is None:\n        R = isi_rates(M, bursts)\n    if n_spk is None:\n        n_spk = M.sum(1)\n    peaks = bursts[\"peak\"]\n    win = peaks[:, None] + np.arange(-WIN_PRE, WIN_POST + 1)[None, :]\n    win = np.clip(win, 0, T - 1)\n    cnt_win = M[:, win].sum(2)  # units by bursts\n    active = cnt_win >= 2\n    keep = (active.mean(1) >= min_frac) & (n_spk >= min_spikes)"
}
```

```
The file entries/van-der-molen-2025/sequences.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "old_string": "def xcorr_coeff_max(X, maxlag):\n    \"\"\"For a units-by-bursts-by-frames array, MATLAB xcorr(x, y, maxlag, 'coeff') between every pair\n    of bursts of each unit; returns the maximum over lags, units by bursts by bursts.\"\"\"\n    U, B, T = X.shape\n    X = X.astype(np.float64)\n    norm = np.sqrt((X ** 2).sum(2))\n    best = np.full((U, B, B), -np.inf)\n    for lag in range(-maxlag, maxlag + 1):\n        if lag >= 0:\n            a, b = X[:, :, lag:], X[:, :, :T - lag]\n        else:\n            a, b = X[:, :, :T + lag], X[:, :, -lag:]\n        c = np.einsum(\"ubt,uct->ubc\", a, b)\n        best = np.maximum(best, c)\n    den = norm[:, :, None] * norm[:, None, :]\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return best / den",
 "new_string": "def xcorr_coeff_max(X, maxlag, Y=None):\n    \"\"\"For a units-by-bursts-by-frames array, MATLAB xcorr(x, y, maxlag, 'coeff') between every pair\n    of bursts of each unit; returns the maximum over lags, units by bursts by bursts. With Y (the\n    same units' bursts in a second recording), between every burst of X and every burst of Y.\"\"\"\n    X = X.astype(np.float64)\n    Y = X if Y is None else Y.astype(np.float64)\n    U, B, T = X.shape\n    nx = np.sqrt((X ** 2).sum(2))\n    ny = np.sqrt((Y ** 2).sum(2))\n    best = np.full((U, B, Y.shape[1]), -np.inf)\n    for lag in range(-maxlag, maxlag + 1):\n        if lag >= 0:\n            a, b = X[:, :, lag:], Y[:, :, :T - lag]\n        else:\n            a, b = X[:, :, :T + lag], Y[:, :, -lag:]\n        c = np.einsum(\"ubt,uct->ubc\", a, b)\n        best = np.maximum(best, c)\n    den = nx[:, :, None] * ny[:, None, :]\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        return best / den\n\n\ndef cross_burst_to_burst(M1, b1, M2, b2, min_frac=0.3, min_spikes=MIN_SPIKES):\n    \"\"\"Burst-to-burst correlation of each unit between two recordings whose units are the same\n    (Supplementary Fig. 8E: bursts paired across the 0 h and 4 h recordings): burst-only rates, the\n    maximum xcorr coefficient within 10 ms for every burst of the first recording against every\n    burst of the second in which the unit has at least two spikes in the -250 to 500 ms window; the\n    mean over those pairs. Units kept when they pass the rules of burst_to_burst in both recordings.\n    Returns an array with NaN for units not kept.\"\"\"\n    parts = []\n    for M, b in ((M1, b1), (M2, b2)):\n        T = M.shape[1]\n        win = np.clip(b[\"peak\"][:, None] + np.arange(-WIN_PRE, WIN_POST + 1)[None, :], 0, T - 1)\n        active = M[:, win].sum(2) >= 2\n        keep = (active.mean(1) >= min_frac) & (M.sum(1) >= min_spikes)\n        parts.append((isi_rates(M, b)[:, win], active, keep))\n    (X1, a1, k1), (X2, a2, k2) = parts\n    out = np.full(M1.shape[0], np.nan)\n    idx = np.nonzero(k1 & k2)[0]\n    if len(idx) == 0:\n        return out\n    C = xcorr_coeff_max(X1[idx], B2B_MAXLAG, X2[idx])\n    for j, u in enumerate(idx):\n        v = C[j][a1[u][:, None] & a2[u][None, :]]\n        v = v[np.isfinite(v)]\n        out[u] = v.mean() if len(v) else np.nan\n    return out"
}
```

```
The file entries/van-der-molen-2025/sequences.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "old_string": "    max(end, peak + 500) + margin, joined by gap frames of silence. Burst-only rates are zero\n    outside the burst windows (apart from the 50 ms Gaussian's tail, under margin), so their\n    cross-correlations up to 350 ms lag and their sums are the same on the cut recording (exact).\n    Returns the cut matrix and the bursts in its frames.\"\"\"",
 "new_string": "    max(end, peak + 500) + margin, joined by gap frames of silence. Burst-only rates are zero\n    outside the burst windows (apart from the 50 ms Gaussian's tail, under margin), so their sums\n    are the same on the cut recording. Every gap between neighbourhoods becomes gap frames long: a\n    longer gap is shortened, which leaves the cross-correlations up to 350 ms lag unchanged, and a\n    shorter one is lengthened, which drops the lag terms between rates at the end of one burst and\n    the start of the next (not exact; such gaps are below 351 ms of near-zero burst-only rate).\n    Returns the cut matrix and the bursts in its frames.\"\"\""
}
```

```
The file entries/van-der-molen-2025/sequences.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "old_string": "def compress_zeros(R, keep_gap=PAIR_MAXLAG + 1):\n    \"\"\"Shorten every run of frames where all rates are zero to keep_gap frames. Lags up to\n    keep_gap - 1 of a zero-padded cross-correlation are unchanged by this (exact).\"\"\"\n    nz = (R != 0).any(0)\n    keep = nz.copy()\n    run = 0\n    for i in range(len(nz)):\n        if nz[i]:\n            run = 0\n        else:\n            run += 1\n            if run <= keep_gap:\n                keep[i] = True\n    return R[:, keep]\n\n\ndef",
 "new_string": "def"
}
```

```
The file entries/van-der-molen-2025/sequences.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -rn "compress_zeros" entries/van-der-molen-2025/ | grep -v "\.ipynb_checkpoints"
```

```
grep: entries/van-der-molen-2025/__pycache__/sequences.cpython-313.pyc: binary file matches
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; grep -n "class RandomInterceptFit" -A 200 sequences.py | head -5
```

```
712:class RandomInterceptFit:
713-    """Result of lmm: fixed effects, their covariance, Wald z and two-sided p."""
714-
715-    def __init__(self, names, beta, cov, lam, sigma2, n_groups, n_obs):
716-        import pandas as pd
```

**Agent**

Now I'll rewrite the statistics section with Satterthwaite degrees of freedom.

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python - <<'EOF'
src = open("sequences.py").read()
i = src.index("class RandomInterceptFit:")
new = '''class RandomInterceptFit:
    """Result of lmm: fixed effects, their covariance, t statistics with Satterthwaite degrees of
    freedom and two-sided p, as lmerTest reports them."""

    def __init__(self, names, beta, cov, lam, sigma2, n_groups, n_obs, dV, A):
        import pandas as pd
        self.fe_params = pd.Series(beta, index=names)
        self.params = self.fe_params
        self._cov = pd.DataFrame(cov, index=names, columns=names)
        self._dV, self._A = dV, A
        se = np.sqrt(np.diag(cov))
        self.bse = pd.Series(se, index=names)
        self.tvalues = self.fe_params / self.bse
        self.df = pd.Series([self.satterthwaite(np.eye(len(names))[j]) for j in range(len(names))],
                            index=names)
        self.pvalues = pd.Series(2 * stats.t.sf(np.abs(self.tvalues.values), self.df.values), index=names)
        self.group_var = lam * sigma2
        self.resid_var = sigma2
        self.n_groups, self.nobs = n_groups, n_obs

    def cov_params(self):
        return self._cov

    def satterthwaite(self, w):
        """Satterthwaite degrees of freedom of the contrast w (lmerTest's contest1D): 2 (w'Vw)^2 over
        g'Ag, g the gradient of w'Vw in the variance parameters and A their asymptotic covariance."""
        v = float(w @ self._cov.values @ w)
        g = np.array([float(w @ d @ w) for d in self._dV])
        den = float(g @ self._A @ g)
        return 2 * v ** 2 / den if den > 0 else np.inf


def lmm(df, formula, group):
    """Linear mixed-effects model with a random intercept per group, fitted by REML, the model of
    lme4's lmer(y ~ x + (1 | group)) that the paper uses (Methods, "Statistical analyses for model
    comparisons"). The variance ratio is found by maximising the profile REML likelihood over one
    parameter. Fixed effects and contrasts are tested with t tests on Satterthwaite degrees of
    freedom, as lmerTest does: the gradient of the fixed-effect covariance and the Hessian of the
    REML deviance in the log variance parameters are taken by central differences."""
    import patsy
    from scipy.optimize import minimize_scalar
    df = df.replace([np.inf, -np.inf], np.nan).reset_index(drop=True)
    y, X = patsy.dmatrices(formula, df, return_type="dataframe")
    names = list(X.columns)
    g = df.loc[y.index, group].values
    yv, Xv = y.values[:, 0], X.values
    _, gi = np.unique(g, return_inverse=True)
    G = gi.max() + 1
    n_g = np.bincount(gi, minlength=G).astype(float)
    N, p = Xv.shape
    ym = np.bincount(gi, yv, G) / n_g
    Xm = np.vstack([np.bincount(gi, Xv[:, j], G) for j in range(p)]).T / n_g[:, None]

    def transform(lam):
        theta = 1 - np.sqrt(1 / (1 + n_g * lam))
        return yv - theta[gi] * ym[gi], Xv - theta[gi][:, None] * Xm[gi]

    def fit(lam):
        ys, Xs = transform(lam)
        XtX = Xs.T @ Xs
        beta = np.linalg.lstsq(Xs, ys, rcond=None)[0]
        rss = float(((ys - Xs @ beta) ** 2).sum())
        s2 = rss / (N - p)
        sign, logdet = np.linalg.slogdet(XtX)
        ll = -0.5 * ((N - p) * np.log(s2) + np.log(1 + n_g * lam).sum() + logdet)
        return ll, beta, s2, XtX, rss, logdet

    res = minimize_scalar(lambda t: -fit(np.exp(t))[0], bounds=(-15, 8), method="bounded")
    lam = np.exp(res.x)
    if fit(0.0)[0] > fit(lam)[0]:
        lam = 0.0
    ll, beta, s2, XtX, _, _ = fit(lam)
    cov = s2 * np.linalg.pinv(XtX)

    # variance parameters phi = log(group variance), log(residual variance); the group variance
    # is left out when it is estimated at zero (lmerTest drops a parameter on the boundary)
    def unpack(phi):
        s2_ = np.exp(phi[-1])
        return (np.exp(phi[0]) / s2_ if len(phi) == 2 else 0.0), s2_

    def deviance(phi):
        lam_, s2_ = unpack(phi)
        _, _, _, XtX_, rss_, logdet_ = fit(lam_)
        return ((N - p) * np.log(s2_) + np.log(1 + n_g * lam_).sum() + logdet_ + rss_ / s2_)

    def vcov(phi):
        lam_, s2_ = unpack(phi)
        return s2_ * np.linalg.pinv(fit(lam_)[3])

    phi0 = np.log([lam * s2, s2]) if lam > 0 else np.log([s2])
    k, h = len(phi0), 1e-3
    E = np.eye(k) * h
    H = np.zeros((k, k))
    d0 = deviance(phi0)
    for i in range(k):
        for j in range(k):
            H[i, j] = (deviance(phi0 + E[i] + E[j]) - deviance(phi0 + E[i] - E[j])
                       - deviance(phi0 - E[i] + E[j]) + deviance(phi0 - E[i] - E[j])) / (4 * h * h)
    A = 2 * np.linalg.pinv(H)
    dV = [(vcov(phi0 + E[i]) - vcov(phi0 - E[i])) / (2 * h) for i in range(k)]
    return RandomInterceptFit(names, beta, cov, lam, s2, G, N, dV, A)


def contrast(fit, weights):
    """Estimate, t, Satterthwaite degrees of freedom and two-sided p of a linear combination of
    fixed effects (dict name -> weight)."""
    names = fit.fe_params.index
    w = np.array([weights.get(n, 0.0) for n in names])
    est = float(w @ fit.fe_params.values)
    cov = fit.cov_params().loc[names, names].values
    se = float(np.sqrt(w @ cov @ w))
    t = est / se if se > 0 else np.nan
    dfree = fit.satterthwaite(w)
    return dict(estimate=est, se=se, z=t, t=t, df=dfree, p=2 * stats.t.sf(abs(t), dfree))


def cell_means_contrast(fit, a, b):
    """Contrast between two cells of a model fitted with the cell-means formula "0 + C(cell)":
    a minus b, by their names in the fit."""
    return contrast(fit, {f"C(cell)[{a}]": 1.0, f"C(cell)[{b}]": -1.0})
'''
open("sequences.py","w").write(src[:i] + new)
EOF
grep -n "d0 = deviance" sequences.py
```

```
805:    d0 = deviance(phi0)
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; sed -i '/    d0 = deviance(phi0)/d' sequences.py; cat > $TMPDIR/dev/test_lmm.py <<'EOF'
import sys; sys.path.insert(0,".")
import numpy as np, pandas as pd, sequences as sq, time
rng=np.random.default_rng(1)
# balanced: 10 groups, 5 per group; between-group factor x (5 vs 5) -> df = 8 exactly; within factor w -> df = 39
rows=[]
for g in range(10):
    b=rng.normal()
    for i in range(5):
        rows.append(dict(g=g,x=int(g<5),w=i%2,y=b+0.3*(g<5)+0.2*(i%2)+rng.normal()))
d=pd.DataFrame(rows)
f=sq.lmm(d,"y ~ x + w","g")
print(f.df.round(2).to_dict(), f.pvalues.round(4).to_dict())
from scipy import stats
# compare with t-test on group means for x
gm=d.groupby("g").agg(y=("y","mean"),x=("x","first"))
print("t-test group means", stats.ttest_ind(gm.y[gm.x==1], gm.y[gm.x==0]))
# large
N=100000; d=pd.DataFrame(dict(g=rng.integers(0,30,N), x=rng.integers(0,3,N))); d["y"]=rng.normal(size=N)+0.01*d.x
t=time.time(); f=sq.lmm(d,"y ~ 0 + C(x)","g"); print(time.time()-t, sq.contrast(f,{"C(x)[1]":1,"C(x)[0]":-1}))
EOF
$TMPDIR/venv/bin/python $TMPDIR/dev/test_lmm.py
```

```
{'Intercept': 8.33, 'x': 8.0, 'w': 39.0} {'Intercept': 0.5983, 'x': 0.3198, 'w': 0.049}
t-test group means TtestResult(statistic=np.float64(-1.0606090935127732), pvalue=np.float64(0.3198352087656802), df=np.float64(8.0))
0.35950636863708496 {'estimate': 0.018528318741909827, 'se': 0.007743340706217574, 'z': 2.392806857514661, 't': 2.392806857514661, 'df': 99996.999992694, 'p': np.float64(0.01672187351735175)}
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; grep -n "def analyse" sequences.py
```

```
599:def analyse(name, M, seed, n_shuf=0, n_shuf_pair=0, similarity=False, min_dist_ms=MIN_PEAK_DIST_MS,
```

**Agent calls Read**

```json
{
 "file_path": "entries/van-der-molen-2025/sequences.py",
 "offset": 599,
 "limit": 95
}
```

```
599	def analyse(name, M, seed, n_shuf=0, n_shuf_pair=0, similarity=False, min_dist_ms=MIN_PEAK_DIST_MS,
600	            light=False):
601	    """Every measure of one recording that does not need an HMM. M is units by 1 ms frames.
602	    light=True keeps only bursts, backbone units, peak times and rank-order correlations (with
603	    their shuffles), for the drug recordings."""
604	    rng_seeds = np.random.default_rng(seed).integers(0, 2 ** 31 - 1, size=max(n_shuf, 1))
605	    mt = model_type(name)
606	    U, T = M.shape
607	    n_spk = M.sum(1)
608	    res = dict(name=name, mtype=mt, U=U, T=T, n_spk=n_spk, rate=n_spk / (T / 1000.0))
609	    b = detect_bursts(M, mt, min_dist_ms)
610	    res["bursts"] = {k: b[k] for k in ("start", "end", "peak")}
611	    res["n_bursts"] = len(b["peak"])
612	    res["n_bursts_800"] = len(detect_bursts(M, mt, 800)["peak"])
613	    res["cv2"] = np.array([cv2(np.nonzero(m)[0]) for m in M])
614	    if res["n_bursts"] < 2:
615	        return res
616	    counts = spikes_in_bursts(M, b)
617	    res["counts"] = counts
618	    res["frac2"] = (counts >= 2).mean(1)
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python - <<'EOF'
s=open("sequences.py").read()
rep = [
('''def analyse(name, M, seed, n_shuf=0, n_shuf_pair=0, similarity=False, min_dist_ms=MIN_PEAK_DIST_MS,
            light=False):
    """Every measure of one recording that does not need an HMM. M is units by 1 ms frames.
    light=True keeps only bursts, backbone units, peak times and rank-order correlations (with
    their shuffles), for the drug recordings."""''',
'''def analyse(name, M, seed, n_shuf=0, n_shuf_pair=0, similarity=False, min_dist_ms=MIN_PEAK_DIST_MS,
            light=False, cut_rates=False):
    """Every measure of one recording that does not need an HMM. M is units by 1 ms frames.
    light=True keeps only bursts, backbone units, peak times and rank-order correlations (with
    their shuffles), for the drug recordings. cut_rates=True takes the peak times from the rates of
    the cut recording (as for the shuffles), which saves memory on long recordings; the inverse ISI
    held across a cut can then differ at a burst's edge."""'''),
('''    res["n_bursts_800"] = len(detect_bursts(M, mt, 800)["peak"])
''',
'''    res["n_bursts_800"] = len(detect_bursts(M, mt, 800)["peak"])
    res["n_bursts_2000"] = len(detect_bursts(M, mt, 2000)["peak"])
    res["n_overlap"] = b["n_overlap"]
    res["rms"], res["thr"] = b["rms"], BURST_PARAMS["PR" if mt == "PR" else "default"]["rms_mult"] * b["rms"]
    pk_all, _ = signal.find_peaks(b["coarse"], distance=min_dist_ms)
    res["coarse_top"] = np.sort(b["coarse"][pk_all])[::-1][:5]
    res["coarse_median"] = float(np.median(b["coarse"]))
'''),
('''    # full rates: peak times, unit sequence, burst similarity
    R = isi_rates(M)
    res["P"] = peak_times(R, b, counts)
''',
'''    Mc, bc = burst_segments_compressed(M, b)
    # full rates: peak times, unit sequence, burst similarity
    R = isi_rates(Mc) if cut_rates else isi_rates(M)
    res["P"] = peak_times(R, bc if cut_rates else b, counts)
'''),
('''    del R
    Mc, bc = burst_segments_compressed(M, b)
    if light:''', '''    del R
    if light:'''),
('''        sh = dict(rank=[])
        for k in range(n_shuf if res["rank"] is not None else 0):
            Ms, _ = okun_shuffle(M, int(rng_seeds[k]))''',
'''        sh = dict(rank=[], done=[], requested=5 * int(n_spk.sum()))
        for k in range(n_shuf if res["rank"] is not None else 0):
            Ms, done = okun_shuffle(M, int(rng_seeds[k]))
            sh["done"].append(done)'''),
('''    res["b2b30"] = burst_to_burst(Mc, bc, 0.3, R=Rb)
    res["b2b70"] = burst_to_burst(Mc, bc, 0.7, R=Rb)''',
'''    res["b2b30"] = burst_to_burst(Mc, bc, 0.3, R=Rb, n_spk=n_spk)
    res["b2b70"] = burst_to_burst(Mc, bc, 0.7, R=Rb, n_spk=n_spk)'''),
('''    res["pca"] = {k: (pca_cumvar(Rb, v, T) if len(v) >= 3 else None) for k, v in sel.items()}
''',
'''    res["pca"] = {k: (pca_cumvar(Rb, v, T) if len(v) >= 3 else None) for k, v in sel.items()}
    if similarity:
        # the code's burst-only rates: spikes outside bursts removed, the inverse ISI then held
        # across the gaps between bursts as well (compute_rate_isi on the burst-only spikes)
        Rcode = isi_rates(M & burst_mask(b, T)[None, :])
        res["pca_code"] = {k: (pca_cumvar(Rcode, v, T) if len(v) >= 3 else None) for k, v in sel.items()}
        del Rcode
'''),
('''    sh = dict(b2b30=[], cv2=[], pca=[], rank=[], pw_corr=[], pw_lag=[], sim_all=[])
    for k in range(n_shuf):
        Ms, _ = okun_shuffle(M, int(rng_seeds[k]))''',
'''    sh = dict(b2b30=[], cv2=[], pca=[], rank=[], pw_corr=[], pw_lag=[], sim_all=[], done=[],
              requested=5 * int(n_spk.sum()))
    for k in range(n_shuf):
        Ms, done = okun_shuffle(M, int(rng_seeds[k]))
        sh["done"].append(done)'''),
('''        sh["b2b30"].append(burst_to_burst(Msc, bc, 0.3, R=Rbs))''',
'''        sh["b2b30"].append(burst_to_burst(Msc, bc, 0.3, R=Rbs, n_spk=n_spk))'''),
]
for a,b in rep:
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
open("sequences.py","w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python - <<'EOF'
s=open("sequences.py").read()
a='''    p = BURST_PARAMS["PR"] if mtype == "PR" else BURST_PARAMS["default"]
    pop = M.sum(0).astype(float)
    coarse ='''
b='''    return bursts_from_pop(M.sum(0), mtype, min_dist_ms)


def bursts_from_pop(pop, mtype, min_dist_ms=MIN_PEAK_DIST_MS):
    """detect_bursts on the population count per frame (pop)."""
    p = BURST_PARAMS["PR"] if mtype == "PR" else BURST_PARAMS["default"]
    pop = np.asarray(pop, float)
    coarse ='''
assert s.count(a)==1; s=s.replace(a,b)
a='''def spikes_in_bursts(M, bursts):'''
b='''def length_for_bursts(pop, mtype, lo=38, step_s=5):
    """Recording-length reading (b) of the claims file (opening comment): the shortest initial
    segment, in steps of step_s seconds, in which detect_bursts finds at least lo bursts (38 to 40);
    the whole recording when it holds fewer. Returns the length in frames."""
    T = len(pop)
    for n in range(60_000, T + step_s * 1000, step_s * 1000):
        n = min(n, T)
        if len(bursts_from_pop(pop[:n], mtype)["peak"]) >= lo:
            return n
    return T


def spikes_in_bursts(M, bursts):'''
assert s.count(a)==1; s=s.replace(a,b)
open("sequences.py","w").write(s)
EOF
grep -n "def detect_bursts" -A 16 sequences.py | tail -5
```

```
165-    number of peaks found and the number of overlapping bursts dropped."""
166-    return bursts_from_pop(M.sum(0), mtype, min_dist_ms)
167-
168-
169-def bursts_from_pop(pop, mtype, min_dist_ms=MIN_PEAK_DIST_MS):
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat >> sequences.py <<'EOF'


# ---------------------------------------------------------------- d2 (Supplementary Fig. 27)
# Ported from the d2 code of Sooter et al. that the paper's r_download.sh fetches (figshare article
# 25927081, version 1: myYuleWalker.m, myAutocorr.m, getFixedPointDistance.m, getAvalanches.m), on
# one window per recording.

D2_BIN_MS = 30  # Supplementary Methods, "d2 calculation": 30 ms bins
D2_ORDER = 20  # order-20 AR model


def load_pop(asset_id, keep_s=None, chunk=200_000):
    """Population spike count per 1 ms frame, read in chunks of frames (the whole recording when
    keep_s is None)."""
    with open_nwb(asset_id) as f:
        d = f["processing/curated_binning/t_spk_mat/data"]
        n = d.shape[0] if keep_s is None else min(d.shape[0], int(keep_s * 1000))
        return np.concatenate([d[a:min(a + chunk, n), :].astype(bool).sum(1) for a in range(0, n, chunk)])


def ar_yule_walker(x, order=D2_ORDER):
    """myYuleWalker.m: the z-scored series' autocorrelation at lags 1 to order (sums over n - j
    products), the Toeplitz system solved for the AR coefficients; returns them and the noise
    variance 1 - acf . varphi."""
    z = (x - x.mean()) / x.std(ddof=1)
    n = len(z)
    acf = np.array([np.sum(z[:n - j] * z[j:]) / (n - j) for j in range(1, order + 1)])
    col = np.r_[1.0, acf[:-1]]
    R = col[np.abs(np.subtract.outer(np.arange(order), np.arange(order)))]
    varphi = np.linalg.solve(R, acf)
    return varphi, 1 - acf @ varphi


def d2_distance(varphi):
    """getFixedPointDistance.m with beta = 2: the Euclidean distance of the AR coefficients from the
    hyperplane through the history kernels x_k (k = 1 to order, x_k(t) = C(k, t)(-1)^(t+1) for
    t <= k)."""
    from scipy.special import comb
    order = len(varphi)
    x = np.zeros((order, order))
    for k in range(1, order + 1):
        for t in range(1, k + 1):
            x[t - 1, k - 1] = comb(k, t, exact=True) * (-1) ** (t + 1)
    X = x[:, 1:] - x[:, [0]]
    v = np.linalg.lstsq(X, varphi - x[:, 0], rcond=None)[0]
    return float(np.linalg.norm(varphi - (x[:, 0] + X @ v)))


def bin_pop(M_or_pop, bin_ms=D2_BIN_MS):
    p = np.asarray(M_or_pop)
    if p.ndim == 2:
        p = p.sum(0)
    n = len(p) // bin_ms
    return p[:n * bin_ms].reshape(n, bin_ms).sum(1).astype(float)


def shuffle_each_unit(M, rng):
    """The d2 control (Supplementary Methods): each unit's spikes moved to random frames of the
    recording independently, keeping its spike count."""
    U, T = M.shape
    out = np.zeros_like(M)
    for u in range(U):
        out[u, rng.choice(T, int(M[u].sum()), replace=False)] = True
    return out


def simulate_ar(varphi, var_noise, n, rng, burn=1000):
    """simAR.m (MATLAB arima simulate, zero constant): an AR series of n steps after a burn-in."""
    p = len(varphi)
    e = rng.normal(0, np.sqrt(max(var_noise, 1e-12)), n + burn + p)
    x = np.zeros(n + burn + p)
    for t in range(p, len(x)):
        x[t] = varphi @ x[t - p:t][::-1] + e[t]
    return x[-n:]


def avalanches(x, quant=0.1):
    """getAvalanches.m with above_thresh = 1: runs above the quant quantile; size, the summed excess
    over the threshold; duration, the run length in bins. quant 0.1 is test.m's value."""
    thr = np.quantile(x, quant)
    below = np.nonzero(x <= thr)[0]
    sizes, durs = [], []
    for a, b in zip(below[:-1], below[1:]):
        if b - a > 1:
            sizes.append(np.sum(x[a + 1:b] - thr))
            durs.append(b - a - 1)
    return np.array(sizes), np.array(durs)


def max_log_ratio(a, b, bins):
    """Largest |log10| ratio of two probability densities on shared bins, over bins where both
    have mass."""
    ha, _ = np.histogram(a, bins=bins, density=True)
    hb, _ = np.histogram(b, bins=bins, density=True)
    ok = (ha > 0) & (hb > 0)
    return float(np.max(np.abs(np.log10(ha[ok] / hb[ok])))) if ok.any() else np.nan


def ar_fit_check(x, varphi, var_noise, rng, nperseg=1000):
    """The AR fit check (Supplementary Methods): the AR model simulated over the same number of
    bins, then the avalanche size and duration distributions and the power spectrum compared with
    the data's. The paper's rule is a deviation of more than one order of magnitude; it is read
    here as the largest |log10| ratio of the densities over logarithmic bins where both have mass,
    and of the Welch spectra (1000-bin, 30 s, segments; the code's 200 s window is longer than the
    180 s recordings) over frequencies. Returns the three largest deviations."""
    z = (x - x.mean()) / x.std(ddof=1)
    sim = simulate_ar(varphi, var_noise, len(z), rng)
    s, d = avalanches(z)
    s_ar, d_ar = avalanches(sim)
    keep = s_ar >= s.min() if len(s) else np.ones(len(s_ar), bool)  # getARstats.m
    s_ar, d_ar = s_ar[keep], d_ar[keep]
    out = dict(n_aval=len(s), n_aval_ar=len(s_ar))
    if len(s) < 5 or len(s_ar) < 5:
        return dict(out, size=np.nan, duration=np.nan, spectrum=np.nan)
    lo, hi = min(s.min(), s_ar.min()), max(s.max(), s_ar.max())
    out["size"] = max_log_ratio(s, s_ar, np.logspace(np.log10(lo), np.log10(hi), 15))
    out["duration"] = max_log_ratio(d, d_ar, np.unique(np.round(np.logspace(0, np.log10(max(d.max(), d_ar.max()) + 1), 15))))
    f, p1 = signal.welch(z, nperseg=min(nperseg, len(z)))
    _, p2 = signal.welch(sim, nperseg=min(nperseg, len(z)))
    ok = (f > 0) & (p1 > 0) & (p2 > 0)
    out["spectrum"] = float(np.max(np.abs(np.log10(p1[ok] / p2[ok]))))
    return out
EOF
$TMPDIR/venv/bin/python -c "
import sys; sys.path.insert(0,'.')
import numpy as np, sequences as sq
# check: an AR model on the hyperplane has d2 ~ 0: x_1 = [1,0,...] (k=1) is a random walk
v=np.zeros(20); v[0]=1; print(sq.d2_distance(v))
rng=np.random.default_rng(0); x=rng.normal(size=6000); vp,vn=sq.ar_yule_walker(x); print(sq.d2_distance(vp), vn)
"
```

```
0.0
0.21546108022912247 0.9957999951575089
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/d2.py <<'EOF'
import sys; sys.path.insert(0,"entries/van-der-molen-2025")
import numpy as np, pandas as pd, sequences as sq
from scipy import stats
D="/tmp/claude-1001/data"; rows=[]
for i,name in enumerate(sq.MAIN):
    M=np.unpackbits(np.load(f"{D}/{name}.npy"),axis=1).astype(bool)
    rng=np.random.default_rng(500+i)
    x=sq.bin_pop(M); vp,vn=sq.ar_yule_walker(x); d=sq.d2_distance(vp)
    chk=sq.ar_fit_check(x,vp,vn,rng)
    xs=sq.bin_pop(sq.shuffle_each_unit(M,rng)); ds=sq.d2_distance(sq.ar_yule_walker(xs)[0])
    rows.append(dict(rec=name,type=sq.model_type(name),d2=d,d2_shuf=ds,**chk))
df=pd.DataFrame(rows); df["passes"]=(df[["size","duration","spectrum"]]<=1).all(1)
print(df.round(3).to_string())
print(stats.ttest_ind(df.d2_shuf,df.d2,equal_var=False))
print(df.groupby("type").passes.sum())
EOF
time $TMPDIR/venv/bin/python $TMPDIR/dev/d2.py
```

```
/tmp/claude-1001/dev/d2.py:12: Pandas4Warning: Starting with pandas version 4.0 all arguments of all will be keyword-only.
  df=pd.DataFrame(rows); df["passes"]=(df[["size","duration","spectrum"]]<=1).all(1)
     rec type     d2  d2_shuf  n_aval  n_aval_ar   size  duration  spectrum  passes
0    HO1   HO  0.052    0.223     719        277  0.854     1.244     1.258   False
1    HO2   HO  0.036    0.236     491        260  1.555     0.530     1.181   False
2    HO3   HO  0.040    0.223     112        197  0.797     0.709     1.265   False
3    HO4   HO  0.021    0.224     142        132  1.044     0.981     1.578   False
4    HO5   HO  0.015    0.220    2084        638  1.265     1.856     0.734   False
5    HO6   HO  0.018    0.229    3927        636  1.870     2.253     0.737   False
6    HO7   HO  0.033    0.226    3720        824  2.007     2.267     0.469   False
7    HO8   HO  0.041    0.227    4358        989  1.834     1.996     0.646   False
8    MO1   MO  0.045    0.221    3005        742  1.852     1.453     0.423   False
9    MO2   MO  0.054    0.237    1825        934  1.136     0.652     0.327   False
10   MO3   MO  0.029    0.227    1944        886  1.137     0.943     0.328   False
11   MO4   MO  0.079    0.234    1641       1259  0.588     0.394     0.363    True
12   MO5   MO  0.070    0.226    1946       1279  0.769     0.851     0.454    True
13   MO6   MO  0.089    0.229    1768       1551  1.062     0.511     0.411   False
14   MO7   MO  0.037    0.222     662        735  1.195     1.172     0.689   False
15   MO8   MO  0.032    0.229    3382        802  1.764     2.324     0.860   False
16   MO9   MO  0.029    0.222    1900        857  1.009     1.249     0.358   False
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python - <<'EOF'
s=open("sequences.py").read()
rep=[('''def max_log_ratio(a, b, bins):
    """Largest |log10| ratio of two probability densities on shared bins, over bins where both
    have mass."""
    ha, _ = np.histogram(a, bins=bins, density=True)
    hb, _ = np.histogram(b, bins=bins, density=True)
    ok = (ha > 0) & (hb > 0)
    return float(np.max(np.abs(np.log10(ha[ok] / hb[ok])))) if ok.any() else np.nan
''','''def log_ratios(a, b, bins):
    """|log10| ratios of two probability densities on shared bins, over bins where both have mass."""
    ha, _ = np.histogram(a, bins=bins, density=True)
    hb, _ = np.histogram(b, bins=bins, density=True)
    ok = (ha > 0) & (hb > 0)
    return np.abs(np.log10(ha[ok] / hb[ok]))
'''),
('''    180 s recordings) over frequencies. Returns the three largest deviations."""''',
'''    180 s recordings) over frequencies (reading i), or as the median of those ratios (reading ii).
    Returns both for each of the three comparisons."""'''),
('''        return dict(out, size=np.nan, duration=np.nan, spectrum=np.nan)
    lo, hi = min(s.min(), s_ar.min()), max(s.max(), s_ar.max())
    out["size"] = max_log_ratio(s, s_ar, np.logspace(np.log10(lo), np.log10(hi), 15))
    out["duration"] = max_log_ratio(d, d_ar, np.unique(np.round(np.logspace(0, np.log10(max(d.max(), d_ar.max()) + 1), 15))))
    f, p1 = signal.welch(z, nperseg=min(nperseg, len(z)))
    _, p2 = signal.welch(sim, nperseg=min(nperseg, len(z)))
    ok = (f > 0) & (p1 > 0) & (p2 > 0)
    out["spectrum"] = float(np.max(np.abs(np.log10(p1[ok] / p2[ok]))))
    return out''','''        return out
    lo, hi = min(s.min(), s_ar.min()), max(s.max(), s_ar.max())
    f, p1 = signal.welch(z, nperseg=min(nperseg, len(z)))
    _, p2 = signal.welch(sim, nperseg=min(nperseg, len(z)))
    ok = (f > 0) & (p1 > 0) & (p2 > 0)
    lr = {"size": log_ratios(s, s_ar, np.logspace(np.log10(lo), np.log10(hi), 15)),
          "duration": log_ratios(d, d_ar, np.unique(np.round(np.logspace(0, np.log10(max(d.max(), d_ar.max()) + 1), 15)))),
          "spectrum": np.abs(np.log10(p1[ok] / p2[ok]))}
    for k, v in lr.items():
        out[f"{k}_max"] = float(v.max()) if len(v) else np.nan
        out[f"{k}_median"] = float(np.median(v)) if len(v) else np.nan
    return out''')]
for a,b in rep:
    assert s.count(a)==1, a[:50]; s=s.replace(a,b)
open("sequences.py","w").write(s)
EOF
sed -i 's/df\["passes"\]=(df\[\["size","duration","spectrum"\]\]<=1).all(1)/df["p_max"]=(df[["size_max","duration_max","spectrum_max"]]<=1).all(axis=1); df["p_med"]=(df[["size_median","duration_median","spectrum_median"]]<=1).all(axis=1)/; s/df.groupby("type").passes.sum()/df.groupby("type")[["p_max","p_med"]].sum()/' $TMPDIR/dev/d2.py; $TMPDIR/venv/bin/python $TMPDIR/dev/d2.py | tail -8
```

```
30   Pr8   PR  0.053    0.218     619        250     1.253        0.317         0.871            0.200         0.694            0.116  False   True
TtestResult(statistic=np.float64(41.185538238813756), pvalue=np.float64(1.9213277837284846e-37), df=np.float64(45.123881888676856))
      p_max  p_med
type              
HO        0      7
MO        2      9
MS        0      2
PR        0      8
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,".")
import pandas as pd, numpy as np, sequences as sq
first=pd.read_pickle("/tmp/claude-1001/data/first.pkl")
print([r for r in first.index if r.startswith(("HO2","HO3"))])
row=first.loc["HO3_8M"]
with sq.open_nwb(row.asset_id) as f:
    print(list(f["units"].keys()))
EOF
```

```
['HO2', 'HO2_6M', 'HO2_7M', 'HO2_8M', 'HO2_8M_4H', 'HO3', 'HO3_6M', 'HO3_7M', 'HO3_8M', 'HO3_8M_4H']
['id', 'spike_times', 'spike_times_index', 'x_pos', 'y_pos']
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,".")
import pandas as pd, numpy as np, sequences as sq
first=pd.read_pickle("/tmp/claude-1001/data/first.pkl")
def pos(r):
    with sq.open_nwb(first.loc[r].asset_id) as f:
        return np.c_[f["units/x_pos"][:], f["units/y_pos"][:]], f["processing/curated_binning/t_spk_mat/data"].shape
for o in ["HO2","HO3"]:
    a,sa=pos(f"{o}_8M"); b,sb=pos(f"{o}_8M_4H"); print(o, a.shape, b.shape, sa, sb)
    if len(a)==len(b): print(" identical", (a==b).all())
    else:
        for drop in range(len(b)):
            bb=np.delete(b,drop,0)
            if (bb==a).all(): print(" equal after dropping 4H unit", drop, b[drop])
        # does dropped unit position duplicate another?
EOF
```

```
HO2 (90, 2) (90, 2) (180000, 90) (180000, 90)
 identical True
HO3 (116, 2) (117, 2) (180000, 116) (180149, 117)
 equal after dropping 4H unit 24 [2047.5  542.5]
```

**Agent calls Bash**

```bash
date -u; cd entries/van-der-molen-2025; cat >> sequences.py <<'EOF'


def unit_positions(asset_id):
    """Unit positions (x_pos, y_pos) from the units table: units by 2."""
    with open_nwb(asset_id) as f:
        return np.c_[f["units/x_pos"][:], f["units/y_pos"][:]]
EOF
```

```
Tue Nov 17 18:03:48 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/dev/len40.py <<'EOF'
import sys, time; sys.path.insert(0,".")
import pandas as pd, numpy as np, sequences as sq
from concurrent.futures import ThreadPoolExecutor
first=pd.read_pickle("/tmp/claude-1001/data/first.pkl")
t0=time.time()
def go(n):
    pop=sq.load_pop(first.loc[n].asset_id)
    L=sq.length_for_bursts(pop, sq.model_type(n))
    return dict(rec=n, total_s=len(pop)/1000, len40_s=L/1000, bursts=len(sq.bursts_from_pop(pop[:L], sq.model_type(n))["peak"]), code_s=sq.keep_seconds(n))
with ThreadPoolExecutor(4) as ex: rows=list(ex.map(go, sq.MAIN))
print(pd.DataFrame(rows).to_string()); print(time.time()-t0)
EOF
$TMPDIR/venv/bin/python $TMPDIR/dev/len40.py
```

```
rec   total_s   len40_s  bursts  code_s
0    HO1   180.000   150.000      38     180
1    HO2   180.000   180.000      31     180
2    HO3   180.000   165.000      38     180
3    HO4   180.000   180.000      28     180
4    HO5   600.018   600.018      17     600
5    HO6   600.012   600.012      24     600
6    HO7   599.940   599.940      21     600
7    HO8   599.970   599.970      19     600
8    MO1   606.428   145.000      39     600
9    MO2   606.130   606.130       0     600
10   MO3   602.338   602.338       4     600
11   MO4   604.498   604.498       0     600
12   MO5   662.859   662.859       0     600
13   MO6   623.818   623.818       0     600
14   MO7   764.213   160.000      38     600
15   MO8   600.736   300.000      38     600
16   MO9   630.956   630.956      21     600
17  M1S1   378.034   255.000      38     180
18  M1S2  2044.067   430.000      39     180
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import json
d=json.load(open("reproduce_van_der_molen_2025.ipynb"))
for i in [7,8,30,50,53,55,81,89,91,96,101,121]:
    c=d["cells"][i]; print(i, c.get("metadata"), c.get("id"), c.get("outputs"), c.get("execution_count"))
print(d["metadata"]); print(d["nbformat"], d["nbformat_minor"])
EOF
```

```
7 {} e84feb4e [] None
8 {'tags': ['sanity']} 91b110bc [] None
30 {'tags': ['claim:fig2e-b2b-correlation']} 7b347424 [] None
50 {'tags': ['claim:ed4d-gabazine-rank-order']} 3663ac79 [] None
53 {'tags': ['claim:supp2a-backbone-fraction-declines']} a6fe62b8 [] None
55 {'tags': ['claim:supp2c-b2b-increases-with-age']} d9d7471f [] None
81 {'tags': ['claim:fig4f-pca-variance']} a838926a [] None
89 {} 93e78e4d [] None
91 {'tags': ['claim:fig7a-backbone-higher-rate']} 0bc8b96d [] None
96 {'tags': ['claim:fig7b-normalized-b2b']} 1282ac46 [] None
101 {} 9ac59895 [] None
121 {'tags': ['claim:supp10b-rank-order-by-model']} 2a331673 [] None
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
4 5
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/edit; cat > $TMPDIR/edit/nb.py <<'EOF'
import json, uuid
class NB:
    def __init__(s, path): s.path=path; s.d=json.load(open(path))
    @property
    def cells(s): return s.d["cells"]
    def find(s, sub, kind=None):
        hits=[i for i,c in enumerate(s.cells) if sub in "".join(c["source"]) and (kind is None or c["cell_type"]==kind)]
        assert len(hits)==1, (sub, hits); return hits[0]
    def src(s, i): return "".join(s.cells[i]["source"])
    def set(s, i, text): s.cells[i]["source"]=text.strip("\n").splitlines(keepends=True)
    def replace(s, i, a, b):
        t=s.src(i); assert t.count(a)==1, (i, a[:60]); s.set(i, t.replace(a,b))
    def new(s, kind, text, tags=None):
        c={"cell_type":kind,"id":uuid.uuid4().hex[:8],"metadata":({"tags":tags} if tags else {}),"source":text.strip("\n").splitlines(keepends=True)}
        if kind=="code": c.update(outputs=[], execution_count=None)
        return c
    def insert_after(s, i, *cells):
        for k,c in enumerate(cells): s.cells.insert(i+1+k, c)
    def save(s): json.dump(s.d, open(s.path,"w"), indent=1, ensure_ascii=False); open(s.path,"a").write("\n")
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; head -c 300 reproduce_van_der_molen_2025.ipynb; echo; tail -c 100 reproduce_van_der_molen_2025.ipynb | od -c | tail -3
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "632db554",
   "metadata": {},
   "source": [
    "# Reproducing van der Molen, Spaeth, Chini et al. (2025) from dandiset 001603\n",
    "\n",
    "**Paper.** van der Molen T, Spaeth A, Chini M, et al. (2025). Preconfigured neuronal firing\n",
 
0000120   b   f   o   r   m   a   t   _   m   i   n   o   r   "   :    
0000140   5  \n   }  \n
0000144
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/edit/main_code.py <<'PYEOF'
import sys; sys.path.insert(0, "/tmp/claude-1001/edit")
from nb import NB
nb = NB("reproduce_van_der_molen_2025.ipynb")

# run(): d2 for the main recordings
i = nb.find("def run(args):")
nb.replace(i, '''    r = sq.analyse(name, m, seed, n_shuf=n_shuf, n_shuf_pair=n_pair, similarity=sim, light=light)
    r["secs"] = time.time() - t0
    return rec, r''', '''    r = sq.analyse(name, m, seed, n_shuf=n_shuf, n_shuf_pair=n_pair, similarity=sim, light=light)
    if rec == name:
        # d2 (supp27-d2-near-critical): intact, one per-unit shuffle, and the AR fit check
        rng = np.random.default_rng(seed + 500)
        x = sq.bin_pop(m)
        vp, vn = sq.ar_yule_walker(x)
        xs = sq.bin_pop(sq.shuffle_each_unit(m, rng))
        r["d2"] = dict(d2=sq.d2_distance(vp), d2_shuffled=sq.d2_distance(sq.ar_yule_walker(xs)[0]),
                       **sq.ar_fit_check(x, vp, vn, rng))
    r["secs"] = time.time() - t0
    return rec, r''')

# summary table: burst diagnostics
i = nb.find('summ = pd.DataFrame([dict(recording=k, type=r["mtype"]')
nb.set(i, '''summ = pd.DataFrame([dict(recording=k, type=r["mtype"], units=r["U"], seconds=r["T"] / 1000,
                          units_ge30_spikes=int((r["n_spk"] >= 30).sum()),
                          mean_rate_hz=round(r["rate"].mean(), 3), max_rate_hz=round(r["rate"].max(), 2),
                          bursts=r["n_bursts"], overlapping_dropped=r["n_overlap"],
                          backbone=int(r["bb"].sum()) if "bb" in r else np.nan,
                          shuffles=len(r.get("shuf", {}).get("done", [])))
                     for k, r in res.items()])
print(summ.to_string(index=False))
print("\\nRecordings per model type (main set):", pd.Series([R[k]["mtype"] for k in RECS]).value_counts().to_dict())
print("Paper: 8 human organoids, 9 murine organoids, 6 slices, 8 primary cultures.")
print("Burst parameters:", sq.BURST_PARAMS, "minimum peak distance", sq.MIN_PEAK_DIST_MS, "ms")
print("Overlapping bursts dropped (a peak in the tail of a longer burst):", int(summ.overlapping_dropped.sum()),
      "in", int((summ.overlapping_dropped > 0).sum()), "recordings")''')
nb.insert_after(i, nb.new("code", '''# Burst threshold against the coarse population rate (the rate burst peaks are found on)
diag = pd.DataFrame([dict(recording=k, bursts=R[k]["n_bursts"], rms=R[k]["rms"], threshold=R[k]["thr"],
                          median_rate=R[k]["coarse_median"], highest_peak=R[k]["coarse_top"][0],
                          highest_peak_over_rms=R[k]["coarse_top"][0] / R[k]["rms"],
                          top5_peaks=np.round(R[k]["coarse_top"], 2).tolist()) for k in RECS])
print(diag.round(3).to_string(index=False))
print("\\nPopulation rate in spikes per 1 ms frame summed over units (20 ms moving mean, 100 ms Gaussian; 50 ms for Pr).")

# Okun swaps made against those requested (5 per spike); a swap is refused when the two units or
# frames are equal or the target bins already hold a spike, and the loop stops after 4 x (requested
# + spikes) draws
sw = pd.DataFrame([dict(recording=k, shuffles=len(r["shuf"]["done"]), requested=r["shuf"]["requested"],
                        done_min=min(r["shuf"]["done"]), done_frac_min=min(r["shuf"]["done"]) / r["shuf"]["requested"])
                   for k, r in res.items() if r.get("shuf", {}).get("done")])
print(sw.round(3).to_string(index=False))
print("\\nShuffles with fewer swaps than requested:", int((sw.done_frac_min < 1).sum()), "recordings; lowest fraction",
      round(sw.done_frac_min.min(), 3))''', tags=["sanity"]))

# methods-burst-count: 2000 ms
i = nb.find('nb800 = pd.Series({k: R[k]["n_bursts_800"] for k in RECS})')
nb.set(i, '''nb = pd.Series({k: R[k]["n_bursts"] for k in RECS})
nb800 = pd.Series({k: R[k]["n_bursts_800"] for k in RECS})
nb2000 = pd.Series({k: R[k]["n_bursts_2000"] for k in RECS})
print(pd.DataFrame({"bursts_700ms": nb, "bursts_800ms": nb800, "bursts_2000ms": nb2000,
                    "overlapping_dropped": pd.Series({k: R[k]["n_overlap"] for k in RECS}),
                    "seconds": [R[k]["T"] / 1000 for k in RECS]}).T.to_string())
for lab, s in [("700 ms, overlapping bursts dropped (main)", nb), ("800 ms", nb800), ("2000 ms for every recording", nb2000)]:
    print(f"{lab}: mean {s.mean():.1f}, SE {s.std(ddof=1) / np.sqrt(len(s)):.1f}, SD {s.std(ddof=1):.1f}, range {s.min()} to {s.max()}")
ok = nb > 0
print(f"Leaving out the recordings with no burst: mean {nb[ok].mean():.1f}, SE {nb[ok].std(ddof=1) / np.sqrt(ok.sum()):.1f}")
print("Expected 38 +- 4")''')

# unit_table with src
i = nb.find("def unit_table(keys, bbkey=\"bb\"):")
nb.replace(i, '''def unit_table(keys, bbkey="bb"):
    rows = []
    for k in keys:
        r = R[k]''', '''def unit_table(keys, bbkey="bb", src=None):
    src = R if src is None else src
    rows = []
    for k in keys:
        r = src[k]''')

# ed4d: degeneracy of the ratio
i = nb.find("rk = rank_table(D, [k for k in D if not k.endswith(\"NBQXCPP\")])")
nb.replace(i, '''    print(f"{v}: {len(d)} burst pairs; gabazine minus baseline {f.params['gab']:.3f}, p {f.pvalues['gab']:.2g}")''',
'''    print(f"{v}: {len(d)} burst pairs; gabazine minus baseline {f.params['gab']:.3f}, p {f.pvalues['gab']:.2g}")
print("\\nThe ratio (A - B)/(A + B) on signed correlations:")
print(f"   shuffle mean B: median {rk.shuf.median():.3f}, 5th to 95th percentile {rk.shuf.quantile(0.05):.3f} to {rk.shuf.quantile(0.95):.3f}")
print(f"   burst pairs with |A + B| < 0.1: {np.mean(np.abs(rk.raw + rk.shuf) < 0.1):.3f}; with A + B < 0 (sign reversed): {np.mean(rk.raw + rk.shuf < 0):.3f}")
print(f"   ratio 1st to 99th percentile {rk.norm.quantile(0.01):.1f} to {rk.norm.quantile(0.99):.1f}; min {rk.norm.min():.3g}, max {rk.norm.max():.3g}")
print("Raw correlation, gabazine minus baseline (no normalisation):",
      f"{(f_raw := sq.lmm(rk, 'raw ~ gab', 'organoid')).params['gab']:.3f}, p {f_raw.pvalues['gab']:.2g}")''')

# supp8 after supp2c
i = nb.find("Backbone above non-rigid at every age:")
s8 = nb.new("markdown", '''## supp8-backbone-stable-4h

> Units classed as backbone in one recording are mostly classed as backbone again 4 h later, units
> classed as non-rigid are mostly classed as non-rigid again, and backbone units keep more
> consistent firing patterns across the two recordings than non-rigid units.

The dandiset gives no unit identifier across recordings. The units are linked here by position: a
0 h unit is matched to the 4 h unit at the identical (x, y) position when exactly one 4 h unit is
there. Identical positions for every unit, in the same order, are what joint sorting of the two
recordings gives and what two separate sortings would not; this is an assumption, and the results
of each recording on its own are shown as well.''')
s8c = nb.new("code", '''x8 = []
for o in ["HO2", "HO3"]:
    k0, k4 = f"{o}_8M", f"{o}_8M_4H"
    p0, p4 = sq.unit_positions(first.loc[k0].asset_id), sq.unit_positions(first.loc[k4].asset_id)
    where4 = {}
    for j, p in enumerate(map(tuple, p4)):
        where4.setdefault(p, []).append(j)
    link = np.array([where4.get(tuple(p), [-1, -1])[0] if len(where4.get(tuple(p), [])) == 1 else -1 for p in p0])
    same_order = bool((link[link >= 0] == np.sort(link[link >= 0])).all())
    unlinked4 = sorted(set(range(len(p4))) - set(link[link >= 0]))
    print(f"{o}: {len(p0)} units at 0 h, {len(p4)} at 4 h; linked {int((link >= 0).sum())}, in the same order: {same_order}; "
          f"4 h units without a 0 h unit: {unlinked4}")
    r0, r4 = L[k0], L[k4]
    ok = link >= 0
    bb0, bb4 = r0["bb"][ok], r4["bb"][link[ok]]
    print(f"   bursts {r0['n_bursts']} (0 h) and {r4['n_bursts']} (4 h); backbone units {int(r0['bb'].sum())} and {int(r4['bb'].sum())}")
    print(pd.crosstab(pd.Series(np.where(bb0, "backbone", "non-rigid"), name="0 h"),
                      pd.Series(np.where(bb4, "backbone", "non-rigid"), name="4 h")).to_string())
    stay_bb = bb4[bb0].mean() if bb0.any() else np.nan
    stay_nr = (~bb4[~bb0]).mean()
    M0 = sq.load_matrix(first.loc[k0].asset_id, sq.keep_seconds(o))
    M4 = sq.load_matrix(first.loc[k4].asset_id, sq.keep_seconds(o))[link[ok]]
    M0 = M0[ok]
    for rule in [0.3, 0.7]:
        c = sq.cross_burst_to_burst(M0, r0["bursts"], M4, r4["bursts"], rule)
        f = np.isfinite(c)
        d = pd.DataFrame(dict(y=c[f], bb=bb0[f].astype(int)))
        t = stats.ttest_ind(d.y[d.bb == 1], d.y[d.bb == 0], equal_var=False)
        x8.append(dict(organoid=o, rule=rule, backbone_stay=stay_bb, nonrigid_stay=stay_nr, units=int(f.sum()),
                       backbone_units=int(d.bb.sum()), cross_b2b_backbone=d.y[d.bb == 1].mean(),
                       cross_b2b_nonrigid=d.y[d.bb == 0].mean(), welch_p=t.pvalue))
    # each recording on its own
    for k, r in [(k0, r0), (k4, r4)]:
        y = r["b2b30"]
        print(f"   {k} alone, burst-to-burst (30% rule): backbone {np.nanmean(y[r['bb']]):.3f}, non-rigid {np.nanmean(y[~r['bb']]):.3f}")
x8 = pd.DataFrame(x8)
print(x8.round(4).to_string(index=False))
print("\\nCriterion: backbone_stay > 0.5, nonrigid_stay > 0.5 and cross_b2b_backbone > cross_b2b_nonrigid in both organoids:",
      bool(((x8.backbone_stay > 0.5) & (x8.nonrigid_stay > 0.5) & (x8.cross_b2b_backbone > x8.cross_b2b_nonrigid)).all()))''', tags=["claim:supp8-backbone-stable-4h"])
nb.insert_after(i + 1, s8, s8c)  # after supp2c conclusion markdown

# fig4f: code's rates
i = nb.find("match = f4f[(f4f.bb_2pc.between(65.7, 80.3))")
nb.replace(i, '''print("Organoids matching both:", match.rec.tolist())''', '''print("Organoids matching both:", match.rec.tolist())
rows = []
for k in HO8:
    p = R[k]["pca_code"]
    rows.append(dict(rec=k, **{f"{s}_2pc": (100 * p[s][:2].sum() if p[s] is not None else np.nan) for s in ["all", "bb", "nr"]}))
f4c_code = pd.DataFrame(rows)
print("\\nVariant, the code's burst-only rates (inverse ISI held across the gaps between bursts):")
print(f4c_code.round(1).to_string(index=False))
print("Organoids matching both:", f4c_code[(f4c_code.bb_2pc.between(65.7, 80.3)) & (f4c_code.nr_2pc.between(22.5, 27.5))].rec.tolist())''')

nb.save()
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/edit/main_code.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/edit/main_code2.py <<'PYEOF'
import sys; sys.path.insert(0, "/tmp/claude-1001/edit")
from nb import NB
nb = NB("reproduce_van_der_molen_2025.ipynb")

i = nb.find("Raw correlation, gabazine minus baseline (no normalisation):")
nb.replace(i, '''print("Raw correlation, gabazine minus baseline (no normalisation):",
      f"{(f_raw := sq.lmm(rk, 'raw ~ gab', 'organoid')).params['gab']:.3f}, p {f_raw.pvalues['gab']:.2g}")''',
'''f_raw = sq.lmm(rk, "raw ~ gab", "organoid")
print(f"Raw correlation, gabazine minus baseline (no normalisation): {f_raw.params['gab']:.3f}, p {f_raw.pvalues['gab']:.2g}")''')

# after supp10b conclusion: reading (b) of the recording length, then supp27
i = nb.find("## The two sets of human organoids (ed2d, ed2e, ed2f)", "markdown")
md_b = nb.new("markdown", '''## Recording length, reading (b): the shortest initial segment with 38 to 40 bursts

The claims file names two readings of the recording length: (a) the code's lengths, used above,
and (b) the shortest initial segment of each recording that holds 38 to 40 bursts (searched in 5 s
steps; the whole recording when it holds fewer). Under (b) every recording is analysed again
where its length differs from (a) by more than a second, with 5 shuffles (2 for the pairwise
correlations) and the peak times taken from the rates of the cut recording, to fit the runtime and
memory. The table below gives every judged contrast of Figs. 6 and 7 and Supplementary Figs. 10B
and 24C under both readings.''')
code_b = nb.new("code", '''def find_length(k):
    pop = sq.load_pop(first.loc[k].asset_id)
    return k, len(pop), sq.length_for_bursts(pop, sq.model_type(k))


with ThreadPoolExecutor(4) as ex:
    lengths = pd.DataFrame([dict(rec=k, total_s=n / 1000, a_code_s=R[k]["T"] / 1000, b_40_bursts_s=m / 1000)
                            for k, n, m in ex.map(find_length, RECS)]).set_index("rec")
redo = lengths.index[(lengths.b_40_bursts_s - lengths.a_code_s).abs() > 1]


def run_b(args):
    k, n, seed = args
    m = sq.load_matrix(first.loc[k].asset_id, n / 1000)
    return k, sq.analyse(k, m, seed, n_shuf=5, n_shuf_pair=2, cut_rates=True)


t0 = time.time()
R40 = dict(R)
with ProcessPoolExecutor(2) as ex:
    for k, r in ex.map(run_b, [(k, int(lengths.loc[k, "b_40_bursts_s"] * 1000), 4000 + i) for i, k in enumerate(redo)]):
        R40[k] = r
lengths["bursts_a"] = [R[k]["n_bursts"] for k in lengths.index]
lengths["bursts_b"] = [R40[k]["n_bursts"] for k in lengths.index]
lengths["backbone_a"] = [int(R[k]["bb"].sum()) if "bb" in R[k] else np.nan for k in lengths.index]
lengths["backbone_b"] = [int(R40[k]["bb"].sum()) if "bb" in R40[k] else np.nan for k in lengths.index]
lengths["reanalysed"] = lengths.index.isin(redo)
print(lengths.to_string())
print(f"{len(redo)} recordings analysed again in {time.time() - t0:.0f} s")''')
code_t = nb.new("code", '''def judged_contrasts(src):
    """Every judged contrast of Figs. 6 and 7 and Supplementary Figs. 10B and 24C on one set of
    analysed recordings: (claim, contrast) -> (estimate, p), the same models as the cells above."""
    keys = [k for k in RECS if src[k]["n_bursts"] >= 2]
    out = {}

    def put(claim, label, c):
        out[(claim, label)] = (c["estimate"], c["p"])

    def bbkey(k, sk):
        return sk if src[k]["mtype"] == "MS" else "bb"

    for sk in ["bb", "bb_70"]:
        tag = "slices 90%" if sk == "bb" else "slices 70%"
        ua = pd.concat([unit_table([k], bbkey(k, sk), src) for k in keys], ignore_index=True)
        d = ua[(ua.mtype == "MS") & np.isfinite(ua.b2b30)]
        f = sq.lmm(d.rename(columns={"b2b30": "y"}), "y ~ bb", "rec")
        put("fig6f-slice-b2b-correlation", f"MS backbone - non-rigid, {tag}", sq.contrast(f, {"bb": 1.0}))
        d = ua[ua.n_spk >= sq.MIN_SPIKES].assign(lr=lambda x: np.log10(x.rate))
        f, con = within_type(d, "lr")
        for t, c in con.items():
            put("fig7a-backbone-higher-rate", f"{t} backbone - non-rigid, {tag}", c)
        for g in ["bb", "nr"]:
            for t in ["HO", "MO", "MS"]:
                put("fig7a-primary-higher-rate", f"PR - {t} {g}, {tag}", sq.cell_means_contrast(f, f"PR_{g}", f"{t}_{g}"))
        d = ua[(ua.n_spk >= sq.MIN_SPIKES) & np.isfinite(ua.cv2)]
        f, con = within_type(d, "cv2")
        for t, c in con.items():
            put("supp24c-nonrigid-more-variable", f"{t} non-rigid - backbone (raw CV2), {tag}", dict(estimate=-c["estimate"], p=c["p"]))
        d = ua[np.isfinite(ua.b2b30) & np.isfinite(ua.b2b_shuf)].copy()
        d["nb"] = sq.normalize(d.b2b30, d.b2b_shuf)
        f, con = within_type(d, "nb")
        for t in ["HO", "MO", "MS"]:
            put("fig7b-normalized-b2b", f"{t} backbone - non-rigid, {tag}", con[t])
            put("fig7b-normalized-b2b", f"{t} backbone - PR backbone, {tag}", sq.cell_means_contrast(f, f"{t}_bb", "PR_bb"))
        put("fig7b-primary-no-b2b-difference", f"PR backbone - non-rigid, {tag}", con["PR"])
        pp = pd.concat([pair_table([k], bbkey(k, sk), src) for k in keys], ignore_index=True)
        pp = pp[np.isfinite(pp.y)]
        ms = pp[pp.mtype == "MS"]
        f = sq.lmm(ms.rename(columns={"y": "yy"}), "yy ~ 0 + C(type)", "rec")
        for other in ["mix", "nr"]:
            put("fig6g-slice-pairwise-correlation", f"MS bb - {other} pairs, {tag}",
                sq.contrast(f, {"C(type)[bb]": 1.0, f"C(type)[{other}]": -1.0}))
        pn = pp[np.isfinite(pp.shuf)].assign(norm=lambda x: sq.normalize(x.y, x.shuf))
        dm = pn[pn.type.isin(["bb", "nr"])].groupby(["rec", "mtype", "type"]).norm.median().reset_index()
        dm = dm.assign(cell=dm.mtype + "_" + dm.type)
        f = sq.lmm(dm.rename(columns={"norm": "yy"}), "yy ~ 0 + C(cell)", "rec")
        names = set(f.fe_params.index)
        for t in ["HO", "MO", "MS", "PR"]:
            if f"C(cell)[{t}_bb]" in names and f"C(cell)[{t}_nr]" in names:
                claim = "fig7c-normalized-pairwise" if t in ("HO", "MO") else "fig7c-slices-primaries-no-pair-difference"
                put(claim, f"{t} bb - nr pairs (recording medians), {tag}", sq.cell_means_contrast(f, f"{t}_bb", f"{t}_nr"))
        for t in ["HO", "MO", "MS", "PR"]:
            d = pn[(pn.mtype == t) & (pn.type == "bb")]
            if d.rec.nunique() >= 2:
                f = sq.lmm(d, "norm ~ 1", "rec")
                est, p2 = f.params["Intercept"], f.pvalues["Intercept"]
                put("fig7c-backbone-pairs-above-random", f"{t} bb pairs above 0 (one-sided), {tag}",
                    dict(estimate=est, p=p2 / 2 if est > 0 else 1 - p2 / 2))
        if sk == "bb":
            lag = pn[(pn.type == "bb") & (pn.lag > 0)].assign(ll=lambda x: np.log10(x.lag))
            f = sq.lmm(lag, "ll ~ 0 + C(mtype)", "rec")
            for a, b in [("HO", "PR"), ("MO", "PR"), ("HO", "MO"), ("HO", "MS")]:
                put("fig7d-lag-times", f"{a} - {b} log10 lag", sq.contrast(f, {f"C(mtype)[{a}]": 1.0, f"C(mtype)[{b}]": -1.0}))
            for a, b in [("MO", "MS"), ("MS", "PR")]:
                put("fig7d-murine-organoids-slices-same-lag", f"{a} - {b} log10 lag",
                    sq.contrast(f, {f"C(mtype)[{a}]": 1.0, f"C(mtype)[{b}]": -1.0}))
    rows = []
    for k in keys:
        p = src[k]["pca"]
        if any(p[s] is None for s in ["all", "bb", "nr"]) or not src[k]["shuf"]["pca"]:
            continue
        A = sq.pca_ratio(p["all"], p["bb"], p["nr"])
        Bs = [sq.pca_ratio(x["all"], x["bb"], x["nr"]) for x in src[k]["shuf"]["pca"]
              if all(x[s] is not None for s in ["all", "bb", "nr"])]
        B = np.mean(Bs, 0)
        rows += [dict(rec=k, mtype=src[k]["mtype"], sel=s, norm=sq.normalize(A[j], B[j])) for j, s in enumerate(["all", "bb", "nr"])]
    pc_ = pd.DataFrame(rows)
    for reading, other in [("a", "nr"), ("b", "all")]:
        d = pc_[pc_.sel.isin(["bb", other])].assign(cell=lambda x: x.mtype + "_" + x.sel)
        f = sq.lmm(d.rename(columns={"norm": "yy"}), "yy ~ 0 + C(cell)", "rec")
        for t in ["HO", "MO", "MS", "PR"]:
            put("fig7e-pca-backbone-variance", f"{t} backbone - {other} ({reading})", sq.cell_means_contrast(f, f"{t}_bb", f"{t}_{other}"))
    rk_ = rank_table(src, keys)
    rk_["mtype"] = rk_.rec.map(lambda k: src[k]["mtype"])
    for v in ["z", "norm"]:
        d = rk_[np.isfinite(rk_[v])]
        f = sq.lmm(d, f"{v} ~ 0 + C(mtype)", "rec")
        names = list(f.fe_params.index)
        Wm = np.array([[1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1]], float)
        cov = f.cov_params().loc[names, names].values
        est = Wm @ f.fe_params.values
        F = float(est @ np.linalg.solve(Wm @ cov @ Wm.T, est)) / 3
        dfs = [f.satterthwaite(w) for w in Wm]
        put("supp10b-rank-order-by-model", f"main effect, {v} (F on 3 and {min(dfs):.1f} df)",
            dict(estimate=F, p=stats.f.sf(F, 3, min(dfs))))
        put("supp10b-rank-order-by-model", f"HO - PR, {v}", sq.contrast(f, {"C(mtype)[HO]": 1.0, "C(mtype)[PR]": -1.0}))
    return out


ja, jb = judged_contrasts(R), judged_contrasts(R40)
jt = pd.DataFrame({"a_estimate": {k: v[0] for k, v in ja.items()}, "a_p": {k: v[1] for k, v in ja.items()},
                   "b_estimate": {k: v[0] for k, v in jb.items()}, "b_p": {k: v[1] for k, v in jb.items()}})
jt.index.names = ["claim", "contrast"]
pd.set_option("display.max_colwidth", 80)
print(jt.to_string(float_format=lambda v: f"{v:.3g}"))''', tags=["claim:fig7-reading-b"])
nb.insert_after(i - 1, md_b, code_b, code_t)

i = nb.find("## The two sets of human organoids (ed2d, ed2e, ed2f)", "markdown")
md27 = nb.new("markdown", '''## supp27-d2-near-critical

> A subset of every preparation type shows near-critical temporal dynamics (d2 between 0 and 0.1),
> and shuffling spike times raises d2 well above that.

d2 as the Supplementary Methods ("d2 calculation") and the code of Sooter et al. that the paper's
`r_download.sh` fetches (figshare article 25927081, version 1), ported to `sequences.py`:
population counts in 30 ms bins, z-scored, an order-20 AR model by Yule-Walker, and the distance
of its coefficients from the beta = 2 hyperplane. The control moves each unit's spikes to random
frames independently (one shuffle per recording). Recordings at the code's lengths. The AR fit
check is read two ways (see `ar_fit_check`): every log-binned density and spectrum ratio within
one order of magnitude (i), or their median (ii).''')
code27 = nb.new("code", '''d2 = pd.DataFrame([dict(rec=k, type=R[k]["mtype"], **R[k]["d2"]) for k in RECS])
d2["pass_i"] = (d2[["size_max", "duration_max", "spectrum_max"]] <= 1).all(axis=1)
d2["pass_ii"] = (d2[["size_median", "duration_median", "spectrum_median"]] <= 1).all(axis=1)
print(d2.round(3).to_string(index=False))
w = stats.ttest_ind(d2.d2_shuffled, d2.d2, equal_var=False)
print(f"\\nIntact d2: mean {d2.d2.mean():.3f}, range {d2.d2.min():.3f} to {d2.d2.max():.3f}; shuffled: mean {d2.d2_shuffled.mean():.3f}, "
      f"range {d2.d2_shuffled.min():.3f} to {d2.d2_shuffled.max():.3f}")
print(f"Welch t-test, shuffled against intact over the {len(d2)} recordings: t {w.statistic:.1f}, p {w.pvalue:.2g}")
print("Intact recordings with d2 at most 0.1:", int((d2.d2 <= 0.1).sum()), "of", len(d2))
cnt = d2.groupby("type")[["pass_i", "pass_ii"]].sum().astype(int)
cnt["paper"] = pd.Series({"HO": 3, "MO": 7, "MS": 4, "PR": 7})
print("\\nRecordings passing the AR fit check, by type:")
print(cnt.to_string())
print("Kept intact recordings with d2 at most 0.1: reading (i)", bool((d2.d2[d2.pass_i] <= 0.1).all()),
      "; reading (ii)", bool((d2.d2[d2.pass_ii] <= 0.1).all()))''', tags=["claim:supp27-d2-near-critical"])
nb.insert_after(i - 1, md27, code27)
nb.save()
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/edit/main_code2.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
cd  grep -n "claim:" tools/entry.py | head -20
```

```
465:            if tag.startswith("claim:"):
```

**Agent calls Bash**

```bash
cd  sed -n 440,500p tools/entry.py
```

```
elif re.search(r"^license:.*$", text, re.M):
        text = re.sub(r"^(license:.*)$", rf"\1\n{line}", text, count=1, flags=re.M)
    else:
        text = text.rstrip("\n") + f"\n{line}\n"
    path.write_text(text)


def lock(entry_dir: Path, version: str | None = None) -> int:
    """Pin every package, with its hashes, for the entry's Python version, which entry.yaml then records."""
    version = version or python_of(entry_dir)
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        set_python(entry_dir, version)
        print(f"wrote {entry_dir.name}/requirements.lock.txt (Python {version}, with hashes)")
    return r.returncode


def tagged_outputs(notebook: Path) -> dict[str, str]:
    """The text each claim-tagged cell of an executed notebook printed, by tag."""
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find("ja, jb = judged_contrasts(R), judged_contrasts(R40)")
nb.cells[i]["metadata"]={}
nb.save()
EOF
grep -rn "claim:" tools/*.py | grep -v "^.*#" | grep -i "tag" | head
```

```
tools/entry.py:465:            if tag.startswith("claim:"):
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("hmm_van_der_molen_2025.ipynb")
i=nb.find("def cv_recording(args):")
nb.replace(i, '''            full = hmm.loglik(m, X)
            tr = hmm.loglik(m, X, train)
            sur = hmm.loglik(m, S, ~train)
            rows.append(dict(rec=name, K=K, fold=fold, held_out=frac, validation=(full - tr) / n_held, surrogate=sur / n_held))''',
'''            # both scored the same way, log p(held-out entries | the rest) = log p(all) - log p(rest)
            real = hmm.loglik(m, X) - hmm.loglik(m, X, train)
            sur = hmm.loglik(m, S) - hmm.loglik(m, S, train)
            # the round-1 scoring of the surrogate, the marginal likelihood of its held-out entries alone
            sur_marginal = hmm.loglik(m, S, ~train)
            rows.append(dict(rec=name, K=K, fold=fold, held_out=frac, validation=real / n_held, surrogate=sur / n_held,
                             surrogate_marginal=sur_marginal / n_held))''')
i=nb.find('cv["real_above"] = cv.validation > cv.surrogate')
nb.set(i, '''cv["real_above"] = cv.validation > cv.surrogate
cv["margin"] = cv.validation - cv.surrogate
print(cv.groupby(["held_out", "rec"]).agg(folds=("fold", "size"), real_above=("real_above", "sum"),
                                          validation=("validation", "mean"), surrogate=("surrogate", "mean"),
                                          margin_min=("margin", "min"), margin_max=("margin", "max")).round(4).to_string())
for frac in [0.2, 0.1]:
    c = cv[cv.held_out == frac]
    print(f"held out {frac:.0%}: real above surrogate in {int(c.real_above.sum())} of {len(c)} fold, K and organoid combinations; "
          f"smallest margin {c.margin.min():.4f} nats per entry")
print("\\nMargin per fold (nats per entry), 20% held out:")
print(cv[cv.held_out == 0.2].pivot_table(index=["rec", "K"], columns="fold", values="margin").round(4).to_string())
c = cv[cv.held_out == 0.2]
print(f"\\nRound-1 scoring (surrogate as a marginal likelihood): smallest margin {(c.validation - c.surrogate_marginal).min():.4f}; "
      f"marginal minus conditional surrogate score, mean {(c.surrogate_marginal - c.surrogate).mean():.4f}")''')
i=nb.find("def loo_accuracy(F, y, seed):")
nb.replace(i, '''print(svm.groupby("rec")[["state_acc", "rate_acc"]].mean().round(3).to_string())''',
'''chance = pd.Series({k: max(H[k]["bb"].mean(), 1 - H[k]["bb"].mean()) for k in svm.rec.unique()}, name="majority_class")
print(svm.groupby("rec")[["state_acc", "rate_acc"]].mean().join(chance).round(3).to_string())
print(f"Chance (majority class) per organoid, mean {100 * chance.mean():.1f}%; the paper states no chance level")''')
nb.save()
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/dev/smoke.py <<'EOF'
import sys, time, resource; sys.path.insert(0,".")
import numpy as np, sequences as sq
D="/tmp/claude-1001/data"
for name, sim in [("HO7", True), ("M3S2", False)]:
    M=np.unpackbits(np.load(f"{D}/{name}.npy"),axis=1).astype(bool)
    t=time.time(); r=sq.analyse(name, M, 1, n_shuf=2, n_shuf_pair=1, similarity=sim)
    print(name, r["n_bursts"], r["n_overlap"], r["n_bursts_2000"], int(r["bb"].sum()), r["shuf"]["done"], r["shuf"]["requested"], round(time.time()-t,1))
    if sim: print({k:(None if v is None else v[:2].sum()) for k,v in r["pca_code"].items()})
    r2=sq.analyse(name, M, 1, n_shuf=1, n_shuf_pair=1, cut_rates=True); print("cut", r2["n_bursts"], int(r2["bb"].sum()))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, "GB")
EOF
$TMPDIR/venv/bin/python $TMPDIR/dev/smoke.py
```

```
HO7 21 3 14 0 [71970, 71970] 71970 2.5
{'all': np.float64(0.4470791557208315), 'bb': None, 'nr': np.float64(0.4470791557208315)}
cut 21 0
M3S2 6 1 4 5 [14450, 14450] 14450 0.1
cut 6 5
0.670524 GB
```

**Agent calls Bash**

```bash
cd  grep -n "^HARNESS" -A3 tools/entry.py;
```

```
64:HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
65-STAMP = ".clean-run.json"                 # beside the executed copies: what they were made from (entry_hash)
66-RUN_VERSION = 1                           # raise when `run` changes in a way that changes what a run produces
67-REUSE_DAYS = 30                           # executed copies older than this are made again
```

**Agent calls Bash**

```bash
uv pip install --quiet --python $TMPDIR/venv/bin/python ipykernel nbconvert && $TMPDIR/venv/bin/python -m ipykernel install --prefix $TMPDIR/venv --name devkernel >/dev/null && echo ok; date -u
```

```
ok
Tue Nov 17 18:09:13 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; mkdir -p $TMPDIR/out; export JUPYTER_PATH=$TMPDIR/venv/share/jupyter; 
( $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=7200 --ExecutePreprocessor.kernel_name=devkernel --output-dir $TMPDIR/out reproduce_van_der_molen_2025.ipynb > $TMPDIR/out/main.log 2>&1; echo "main exit $? $(date -u)" >> $TMPDIR/out/status ) &
( $TMPDIR/venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=7200 --ExecutePreprocessor.kernel_name=devkernel --output-dir $TMPDIR/out hmm_van_der_molen_2025.ipynb > $TMPDIR/out/hmm.log 2>&1; echo "hmm exit $? $(date -u)" >> $TMPDIR/out/status ) &
wait; cat $TMPDIR/out/status; tail -5 $TMPDIR/out/*.log
```

```
Exit code 1
hmm exit 0 Tue Nov 17 18:33:06 UTC 2026
main exit 0 Tue Nov 17 18:47:06 UTC 2026
error: unexpected argument '-5' found

  tip: to pass '-5' as a value, use '-- -5'

Usage: tail [OPTION]... [FILE]...

For more information, try '--help'.
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/dump.py <<'EOF'
import json, sys
d=json.load(open(sys.argv[1])); out=open(sys.argv[2],"w")
for i,c in enumerate(d["cells"]):
    if c["cell_type"]!="code": 
        out.write(f"\n##### MD {i}: {''.join(c['source'])[:80]!r}\n"); continue
    out.write(f"\n##### CELL {i} tags={c['metadata'].get('tags')}\n")
    for o in c.get("outputs",[]):
        t=o.get("text") or (o.get("data") or {}).get("text/plain") or o.get("evalue") or ""
        out.write("".join(t) if isinstance(t,list) else t)
EOF
cd $TMPDIR/out; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py reproduce_van_der_molen_2025.ipynb main.txt; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py hmm_van_der_molen_2025.ipynb hmm.txt; wc -l main.txt hmm.txt
```

```
1218 main.txt
   245 hmm.txt
  1463 total
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out/main.txt",
 "offset": 150,
 "limit": 330
}
```

```
150	          Pr8    238  900.986         270484      270590.0          900.98600                  True             106.0
151	
152	Every matrix count is at most the units-table count (several spikes in one 1 ms bin count once): True
153	
154	##### MD 6: "The spike matrices are 1 ms bins (the file's description says so); where a units"
155	
156	##### CELL 7 tags=None
157	analysed 53 recordings in 1827 s
158	
159	##### CELL 8 tags=['sanity']
160	    recording type  units  seconds  units_ge30_spikes  mean_rate_hz  max_rate_hz  bursts  overlapping_dropped  backbone  shuffles
161	          HO1   HO    131   180.00                 94         1.347         8.06      46                    0      27.0        10
162	          HO2   HO    173   180.00                 79         0.506         8.08      31                    0      26.0        10
163	          HO3   HO     80   180.00                 52         0.705         3.39      42                    0      23.0        10
164	          HO4   HO    123   180.00                 51         0.568         9.08      28                    0      15.0        10
165	          HO5   HO    308   600.00                308         0.460         2.94      17                    3     134.0        10
166	          HO6   HO     50   600.00                 50         0.692         3.28      24                    9      23.0        10
167	          HO7   HO     30   599.94                 30         0.800         2.64      21                    3       0.0        10
168	          HO8   HO     35   599.97                 35         0.810         4.50      19                    4      14.0        10
169	          MO1   MO    103   600.00                103         6.266        21.32     113                    0      56.0        10
[... 310 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,149p $TMPDIR/out/main.txt | grep -n "##### CELL [5-7]\|Every matrix"
```

```
96:##### CELL 5 tags=['sanity']
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out/main.txt",
 "offset": 480,
 "limit": 300
}
```

```
480	 MO11_NBQXCPP     MO11  NBQXCPP     18    600.0       0             0.0
481	MO12_GABAZINE     MO12 GABAZINE     22    600.0     160            16.0
482	 MO12_NBQXCPP     MO12  NBQXCPP     22    600.0       1             0.1
483	    MO13_BASE     MO13     BASE     21    600.0     107            10.7
484	MO13_GABAZINE     MO13 GABAZINE     21    600.0     134            13.4
485	 MO13_NBQXCPP     MO13  NBQXCPP     21    600.0       0             0.0
486	    MO14_BASE     MO14     BASE     57    600.0     114            11.4
487	MO14_GABAZINE     MO14 GABAZINE     57    600.0     220            22.0
488	 MO14_NBQXCPP     MO14  NBQXCPP     57    600.0       0             0.0
489	
490	MO12 has no baseline sorted file. Unit counts are equal across the conditions of each organoid.
491	
492	##### MD 41: '## ed4b-gabazine-more-bursts\n\n> In murine organoids, blocking GABA-A receptors w'
493	
494	##### CELL 42 tags=['claim:ed4b-gabazine-more-bursts']
495	cond      BASE  GABAZINE
496	organoid                
497	MO10       8.1      16.3
498	MO11      10.4      18.4
499	MO12       NaN      16.0
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find("x8 = []")
nb.replace(i, '''    where4 = {}
    for j, p in enumerate(map(tuple, p4)):
        where4.setdefault(p, []).append(j)
    link = np.array([where4.get(tuple(p), [-1, -1])[0] if len(where4.get(tuple(p), [])) == 1 else -1 for p in p0])
    same_order = bool((link[link >= 0] == np.sort(link[link >= 0])).all())
    unlinked4 = sorted(set(range(len(p4))) - set(link[link >= 0]))
    print(f"{o}: {len(p0)} units at 0 h, {len(p4)} at 4 h; linked {int((link >= 0).sum())}, in the same order: {same_order}; "
          f"4 h units without a 0 h unit: {unlinked4}")''', '''    # walk both lists in order: a 0 h unit is linked to the next 4 h unit at the identical position,
    # skipping 4 h units that have no 0 h counterpart
    link, j = np.full(len(p0), -1), 0
    for u in range(len(p0)):
        while j < len(p4) and not (p4[j] == p0[u]).all():
            j += 1
        if j < len(p4):
            link[u], j = j, j + 1
    unlinked4 = sorted(set(range(len(p4))) - set(link[link >= 0]))
    n_pos = len({tuple(p) for p in p0})
    print(f"{o}: {len(p0)} units at 0 h ({n_pos} distinct positions), {len(p4)} at 4 h; 0 h units linked in order: "
          f"{int((link >= 0).sum())}; 4 h units left out: {unlinked4}")''')
nb.save()
EOF
grep -n "x8 = \[\]" -A3 reproduce_van_der_molen_2025.ipynb | head -3
```

```
1121:    "x8 = []\n",
1122-    "for o in [\"HO2\", \"HO3\"]:\n",
1123-    "    k0, k4 = f\"{o}_8M\", f\"{o}_8M_4H\"\n",
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/dev/s8.py <<'EOF'
import sys; sys.path.insert(0,".")
import numpy as np, pandas as pd, sequences as sq, json
from scipy import stats
first=pd.read_pickle("/tmp/claude-1001/data/first.pkl")
L={}
for o in ["HO2","HO3"]:
    for c in ["8M","8M_4H"]:
        k=f"{o}_{c}"; L[k]=sq.analyse(o, sq.load_matrix(first.loc[k].asset_id, 180), 3000)
nbj=json.load(open("reproduce_van_der_molen_2025.ipynb"))
src=[ "".join(c["source"]) for c in nbj["cells"] if "x8 = []" in "".join(c["source"])][0]
exec(src)
EOF
$TMPDIR/venv/bin/python $TMPDIR/dev/s8.py
```

```
HO2: 90 units at 0 h (61 distinct positions), 90 at 4 h; 0 h units linked in order: 90; 4 h units left out: []
   bursts 39 (0 h) and 33 (4 h); backbone units 10 and 14
4 h        backbone  non-rigid
0 h                           
backbone          8          2
non-rigid         6         74
   HO2_8M alone, burst-to-burst (30% rule): backbone 0.794, non-rigid 0.672
   HO2_8M_4H alone, burst-to-burst (30% rule): backbone 0.772, non-rigid 0.588
HO3: 116 units at 0 h (84 distinct positions), 117 at 4 h; 0 h units linked in order: 116; 4 h units left out: [24]
   bursts 38 (0 h) and 28 (4 h); backbone units 13 and 19
4 h        backbone  non-rigid
0 h                           
backbone         13          0
non-rigid         6         97
   HO3_8M alone, burst-to-burst (30% rule): backbone 0.852, non-rigid 0.654
   HO3_8M_4H alone, burst-to-burst (30% rule): backbone 0.864, non-rigid 0.657
organoid  rule  backbone_stay  nonrigid_stay  units  backbone_units  cross_b2b_backbone  cross_b2b_nonrigid  welch_p
     HO2   0.3            0.8         0.9250     27              10              0.7481              0.6271   0.0389
     HO2   0.7            0.8         0.9250     17               9              0.7378              0.6991   0.6152
     HO3   0.3            1.0         0.9417     35              13              0.8205              0.6067   0.0000
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out/main.txt",
 "offset": 780,
 "limit": 440
}
```

```
780	Expected for the example organoid: backbone 73 +- 7.3, non-rigid 25 +- 2.5 percent
781	Organoids matching both: []
782	
783	Variant, the code's burst-only rates (inverse ISI held across the gaps between bursts):
784	rec  all_2pc  bb_2pc  nr_2pc
785	HO1     26.0    75.1    15.3
786	HO2     18.1    65.1    10.8
787	HO3     29.5    75.7    14.7
788	HO4     16.3    70.7    11.3
789	HO5     36.3    56.8    26.0
790	HO6     41.3    58.7    32.8
791	HO7     44.7     NaN    44.7
792	HO8     35.5    54.6    32.0
793	Organoids matching both: []
794	
795	##### MD 85: '**Result: partially reproduced.** In HO1 the first two PCs explain 75.4% of the '
796	
797	##### MD 86: '## Neonatal slices (fig6f, fig6g)'
798	
799	##### CELL 87 tags=['claim:fig6f-slice-b2b-correlation']
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/venv/bin/python - <<'EOF'
import yaml
c=yaml.safe_load(open("claims/van-der-molen-2025.yaml"))
for x in c["claims"]:
    if x["id"] in ("methods-burst-count","fig4e-similarity-rises-at-backbone-onset","fig7c-backbone-pairs-above-random","fig7b-normalized-b2b","fig7e-pca-backbone-variance","ed2f-backbone-pairs-above-zero","fig4f-pca-variance"):
        print(x["id"], "::", x["criterion"], "\n")
EOF
grep -n -i "Supplementary Fig. 10\|Supplementary Figure 10" paper/*.txt | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
c=yaml.safe_load(open("claims/van-der-molen-2025.yaml"))
for x in c["claims"]:
    if x["id"] in ("methods-burst-count","fig4e-similarity-rises-at-backbone-onset","fig7c-backbone-pairs-above-random","fig7b-normalized-b2b","fig7e-pca-backbone-variance","ed2f-backbone-pairs-above-zero","fig4f-pca-variance","ed5-shuffle-reduces-b2b"):
        print(x["id"], "::", x["criterion"], "\n")
EOF
sed -n 352,362p paper/*.txt; grep -n -i "z-scor" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 7000 /home/runner/.claude/projects/-home-runner-work-encore-encore/a8a7588f-9d6c-46d7-a5b0-2c9606906d3d/tool-results/b59958qsh.txt | tail -c 5000
```

```
_m in the code's single_unit table). Model as in fig7a-backbone-higher-rate on the normalized value (not log-transformed). Reproduced when backbone exceeds non-rigid with p < 0.05 in human organoids, murine organoids and slices, and backbone units of each of these three exceed those of primary cultures with p < 0.05; partially reproduced when only the within-type contrasts hold. The Results and the legend print different p-values for the same panel; both are recorded. Supplementary Fig. 9B describes the normalization as subtracting the shuffle mean (A - B); that is shown as a variant, as for fig7e-pca-backbone-variance. 

fig7c-backbone-pairs-above-random :: Normalized backbone-backbone pair correlations, (A - B)/(A + B), tested above 0 per model type with a linear mixed-effects model and a random intercept per recording, one-sided as in Extended Data Fig. 2F (the Results do not name the sidedness; two-sided is a variant). Reproduced when the value is above 0 with p < 0.05 in organoids and in slices and not significant in primary cultures (the absence judged on the same test at alpha 0.05). 

fig7e-pca-backbone-variance :: PCA as in fig4f-pca-variance. Per recording and unit set, the variance of the first three PCs divided by that of the first X PCs, X the smallest number of PCs among all, backbone and non-rigid units; normalized as (A - B)/(A + B) to 100 shuffles (Methods; m_value in the code's pca table; Supplementary Fig. 15 says the shuffle mean was subtracted, a variant). Model, value on unit type, model type and their interaction with a random intercept per recording. The legend plots all units, backbone and non-rigid and says only "Differences were significant", and the Methods compare "the three selections", so which contrast is meant is open; readings (a) backbone against non-rigid (unit types backbone and non-rigid), (b) backbone against all units (all three selections in the model). Reproduced when backbone exceeds the comparison group with p < 0.05 in hu
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/out/hmm.txt | cut -c1-200 | grep -v "^HO[1-8] *[0-9]* *[0-9] *[0-9.-]* *[0-9.-]* *[0-9.-]* *[0-9.-]* *[0-9.-]*$" | head -150
```

```
##### MD 0: '# Hidden Markov models: van der Molen et al. (2025) on dandiset 001603\n\nThe HMM '

##### CELL 1 tags=None

##### CELL 2 tags=None
fitted 341 HMMs in 830 s

##### CELL 3 tags=['sanity']
 rec type  units  bins  bin_ms  max_count  bursts  backbone
 HO1   HO    131  6000      30          5      46      27.0
 HO2   HO    173  6000      30          4      31      26.0
 HO3   HO     80  6000      30          4      42      23.0
 HO4   HO    123  6000      30          7      28      15.0
 HO5   HO    308 20000      30          4      17     134.0
 HO6   HO     50 20000      30          3      24      23.0
 HO7   HO     30 19998      30          5      21       0.0
 HO8   HO     35 19999      30          5      19      14.0
 MO1   MO    103 20000      30         13     113      56.0
 MO2   MO    199 20000      30         14       0       NaN
 MO3   MO    234 20000      30         12       4     160.0
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/CELL 13 tags/,/CELL 15 tags/p' $TMPDIR/out/hmm.txt | head -14; sed -n '/CELL 15 tags/,/Chance/p' $TMPDIR/out/hmm.txt; sed -n '/CELL 18 tags/,$p' $TMPDIR/out/hmm.txt | tail -45
```

```
##### CELL 13 tags=['claim:fig5d-backbone-more-states']
    n_above        mean_cons       
bb        0      1         0      1
rec                                
HO1   1.129  8.020     0.089  0.387
HO2   0.693  6.605     0.069  0.334
HO3   1.112  8.704     0.086  0.426
HO4   0.643  9.394     0.070  0.464
HO5   0.090  1.433     0.029  0.102
HO6   0.421  1.016     0.063  0.089
HO8   0.208  1.071     0.042  0.081
n_above: backbone minus non-rigid 3.738, p 0 (9900 unit-model rows, 7 organoids; K as a fixed factor)
mean_cons: backbone minus non-rigid 0.172, p 0 (9900 unit-model rows, 7 organoids; K as a fixed factor)
HO7 has no backbone unit and is left out.
##### CELL 15 tags=['claim:fig5f-svm-states-beat-rate']
     state_acc  rate_acc  majority_class
rec                                     
HO1      0.975     0.916           0.794
HO2      0.950     0.948           0.850
HO3      0.883     0.888           0.712
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('claims/van-der-molen-2025.yaml'))
for x in c['claims']:
    if x['id'] in ('supp26-state-traversal','fig7f-hmm-dimensionality','fig5d-backbone-more-states'):
        print(x['id'], '::', x.get('statement'), '::', x['criterion'], x.get('statistics'), '\n')
"
```

```
fig5d-backbone-more-states :: Backbone units are active across a larger pool of HMM states than non-rigid units. :: Consistency of a unit in a state, the fraction of the state's realizations (bins where it is most probable) in which the unit fires at least once (Supplementary Methods). The size of the "pool" is not defined; readings (a) the number of states with consistency above 0.5, (b) the mean consistency over states. HO1 to HO8, K from 10 to 30. No test is reported; a linear mixed-effects model on unit type with random intercepts for organoid and K. Reproduced when backbone is higher with p < 0.05 under both readings. None 

fig7f-hmm-dimensionality :: HMM state spaces are higher-dimensional in human and murine organoids than in primary cultures. :: HMMs as in supp18-hmm-likelihood-real-above-shuffled for all 31 recordings, K from 10 to 30. Per model, PCA of the K by units matrix of Poisson rates (exp of the fitted log lambdas, Supplements.py); dimensionality, the smallest number of components whose cumulative explained variance exceeds theta = 0.75 (counted up to 10). Test as in lmem.R, a Poisson GLMM (glmer, log link) of dimensionality on model type with a random intercept per recording, emmeans pairwise contrasts (Tukey adjustment, the emmeans default). Reproduced when primary cultures are lower than human and murine organoids with p < 0.05. The human organoid against slice contrast is reported; the legend's "but not compared with slices" next to P = 0.036 is not judged. [{'about': 'primary cultures against human organoids, Results', 'test': 'linear mixed-effects model with Poisson observations', 'p': 0.0001, 'p_relation': '<'}, {'about': 'primary cultures against murine organoids, Results', 'test': 'linear mixed-effects model with Poisson observations', 'p': 0.003}, {'about': 'human organoids against slices, Results', 'test': 'linear mixed-effects model with Poisson observations', 'p': 0.04}, {'about': 'human organoids against primary cultures, Figure 7F le
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
date -u
```

```
Tue Nov 17 18:49:23 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find("def judged_contrasts(src):")
nb.replace(i,'''        put("supp10b-rank-order-by-model", f"main effect, {v} (F on 3 and {min(dfs):.1f} df)",
            dict(estimate=F, p=stats.f.sf(F, 3, min(dfs))))''','''        # F on 3 and the smallest Satterthwaite df of the three contrasts (a conservative choice)
        put("supp10b-rank-order-by-model", f"main effect, {v} (F)", dict(estimate=F, p=stats.f.sf(F, 3, min(dfs))))''')
i=nb.find('f = sq.lmm(d, "y ~ bb", "rec")\n    print(f"{rule}')
nb.replace(i,"LMM effect {f.params['bb']:.3f}, z {f.tvalues['bb']:.1f}","LMM effect {f.params['bb']:.3f}, t {f.tvalues['bb']:.1f}")
i=nb.find('print(f"{v}: {len(d)} burst pairs in {d.rec.nunique()} recordings; main effect chi2(3)')
print(nb.src(i))
nb.save()
EOF
```

```
rk_all = rank_table(R, ALL)
rk_all["mtype"] = rk_all.rec.map(lambda k: R[k]["mtype"])
print(rk_all.groupby("mtype")[["raw", "norm", "z"]].median().round(3).to_string())
for v in ["norm", "z"]:
    d = rk_all[np.isfinite(rk_all[v])]
    f = sq.lmm(d, f"{v} ~ 0 + C(mtype)", "rec")
    names = list(f.fe_params.index)
    Wm = np.array([[1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1]], float)
    cov = f.cov_params().loc[names, names].values
    est = Wm @ f.fe_params.values
    chi2 = float(est @ np.linalg.solve(Wm @ cov @ Wm.T, est))
    c = sq.contrast(f, {"C(mtype)[HO]": 1.0, "C(mtype)[PR]": -1.0})
    print(f"{v}: {len(d)} burst pairs in {d.rec.nunique()} recordings; main effect chi2(3) {chi2:.1f}, p {stats.chi2.sf(chi2, 3):.2g}; "
          f"HO minus PR {c['estimate']:.3f}, p {c['p']:.2g}")
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find('print(f"{v}: {len(d)} burst pairs in {d.rec.nunique()} recordings; main effect chi2(3)')
nb.replace(i,'''    chi2 = float(est @ np.linalg.solve(Wm @ cov @ Wm.T, est))
    c = sq.contrast(f, {"C(mtype)[HO]": 1.0, "C(mtype)[PR]": -1.0})
    print(f"{v}: {len(d)} burst pairs in {d.rec.nunique()} recordings; main effect chi2(3) {chi2:.1f}, p {stats.chi2.sf(chi2, 3):.2g}; "
          f"HO minus PR {c['estimate']:.3f}, p {c['p']:.2g}")''','''    chi2 = float(est @ np.linalg.solve(Wm @ cov @ Wm.T, est))
    df_min = min(f.satterthwaite(w) for w in Wm)
    c = sq.contrast(f, {"C(mtype)[HO]": 1.0, "C(mtype)[PR]": -1.0})
    print(f"{v}: {len(d)} burst pairs in {d.rec.nunique()} recordings; main effect F {chi2 / 3:.2f} on 3 and {df_min:.1f} df "
          f"(the smallest Satterthwaite df of the three contrasts), p {stats.f.sf(chi2 / 3, 3, df_min):.2g} (Wald chi2(3) p {stats.chi2.sf(chi2, 3):.2g}); "
          f"HO minus PR {c['estimate']:.3f}, t {c['t']:.2f} on {c['df']:.1f} df, p {c['p']:.2g}")''')
nb.save()
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find("def judged_contrasts(src):")
nb.replace(i,'''        d = pc_[pc_.sel.isin(["bb", other])].assign(cell=lambda x: x.mtype + "_" + x.sel)''','''        d = (pc_[pc_.sel.isin(["bb", "nr"])] if reading == "a" else pc_).assign(cell=lambda x: x.mtype + "_" + x.sel)''')
nb.save()
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
for i,c in enumerate(nb.cells):
    if c["cell_type"]=="markdown" and ("**Result" in nb.src(i) or i in (0,)):
        print(i, nb.src(i)[:70].replace("\n"," "))
EOF
```

```
0 # Reproducing van der Molen, Spaeth, Chini et al. (2025) from dandiset
13 **Result: reproduced, numerically.** The mean is 35.7 bursts over the 
16 **Result: reproduced.** HO1 has 46 bursts in its first 180 s under bot
20 **Result: reproduced, under reading (a) with all units.** The mean R² 
23 **Result: reproduced.** The median burst durations of HO1 to HO4 are 5
26 **Result: partially reproduced.** In 15 of the 16 combinations of orga
29 **Result: reproduced, under reading (b).** With units of at least 30 s
32 **Result: reproduced.** Backbone units have higher burst-to-burst corr
35 **Result: reproduced.** The variance of backbone peak times rises with
38 **Result: reproduced.** Non-rigid units vary more between burst cluste
43 **Result: reproduced.** Gabazine raises the burst rate in each of the 
46 **Result: reproduced.** Every NBQX with R-CPP recording has no burst o
49 **Result: reproduced.** With units pooled per condition, the fraction 
52 **Result: blocked (methods underspecified).** The raw rank-order corre
55 **Result: partially reproduced.** In the human organoids HO2 and HO3 t
57 **Result: partially reproduced.** In HO2 and HO3 the burst-to-burst co
62 **Result: reproduced.** For backbone units of HO1 to HO8 the real burs
65 **Result: reproduced.** Backbone pairs (0.70) exceed mixed (0.36) and 
68 **Result: partially reproduced.** The backbone-pair mean lies above th
73 **Result: reproduced.** In the example organoid HO1 the standard devia
[... 21 more lines not kept]
```

**Agent**

Now writing all conclusion cells with the new numbers.

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/edit/md.py <<'PYEOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
def res(start, text):
    i=[k for k,c in enumerate(nb.cells) if c["cell_type"]=="markdown" and nb.src(k).startswith(start)]
    assert len(i)==1, (start, i); nb.set(i[0], text)

i=0
nb.replace(0, '''**Shuffles.** The paper normalises to 100 Okun-swap shuffles per recording. This notebook uses 10
per recording, and 3 for the pairwise cross-correlations and the shuffled burst similarity, to fit
the runtime limit (a deviation; the shuffle mean is the reference, and its noise is small next to
the effects tested).''', '''**Shuffles.** The paper normalises to 100 Okun-swap shuffles per recording. This notebook uses 10
per recording, and 3 for the pairwise cross-correlations and the shuffled burst similarity, to fit
the runtime limit (a deviation; the shuffle mean is the reference, and its noise is small next to
the effects tested). Every shuffle made all the swaps requested (data check).

**Bursts.** Peaks at 700 ms minimum distance (Methods); where a peak in the tail of a long burst
gives a second, overlapping burst, only the burst with the higher peak is kept, which is what the
Methods' increase of the distance "up to 2000 ms" for long-burst recordings is for (an assumption
on which recordings it applies to; 2000 ms for every recording is shown as a variant).

**Statistics.** Mixed models are fitted by REML with a random intercept, and fixed effects and
contrasts are tested with t on Satterthwaite degrees of freedom, as lmerTest does
(`sequences.lmm`).''')
nb.replace(0, "| supp8-backbone-stable-4h | blocked: units are not identified across the 0 h and 4 h recordings |",
              "| supp8-backbone-stable-4h | tested, with units linked by their identical positions (an assumption) |")
nb.replace(0, "| fig7a to fig7e (ten claims), supp24c-nonrigid-more-variable, supp10b-rank-order-by-model | tested |",
              "| fig7a to fig7e (ten claims), supp24c-nonrigid-more-variable, supp10b-rank-order-by-model | tested, under both readings of the recording length |")
nb.replace(0, "| supp27-d2-near-critical | blocked (see the attempt record) |",
              "| supp27-d2-near-critical | tested, with the d2 code of Sooter et al. ported |")

res("The dandiset holds 8 human organoids", '''The dandiset holds 8 human organoids, 9 murine organoids, 6 slices and 8 primary cultures, as the
paper says. 35 overlapping bursts in 13 recordings (HO5 to HO8, MO9, the slices, Pr7) are peaks in
the tail of a longer burst and are dropped (cell above). Following the stated burst detection
(population rate above 4 times its RMS), four murine organoids (MO2, MO4, MO5, MO6) have no burst
and MO3 has four. The table of thresholds shows why: their highest peaks reach only 3.0 to 3.7
times the RMS of the rate, against 4.2 to 18 times in every other recording, because their rate
between bursts is high (median coarse rate 0.47 to 1.07 against at most 0.6 elsewhere), so the
RMS is close to the peaks. The paper's code processed every murine organoid, so it must have used
other burst parameters for them, which the paper does not give. Claims that rest on murine
organoid bursts use the recordings that have bursts, and say so. Every shuffle made all the Okun
swaps requested (5 per spike).''')
res("**Result: reproduced, numerically.**", '''**Result: reproduced, numerically.** The mean is 34.8 bursts over the 31 recordings (within 38 ±
4), with an SE of 6.3 and a range from 0 to 156: four murine organoids have no burst and two have
more than 100, so the mean matches while the recordings do not each hold about 40 bursts. The
agreement rests on MO1 and MO7 offsetting the four recordings without bursts. With 800 ms the mean
is 34.7; with 2000 ms for every recording it is 29.5 (outside), but the Methods raise the distance
only for recordings with long bursts.''')
res("**Result: reproduced.** The median burst durations of HO1 to HO4", '''**Result: reproduced.** The median burst durations of HO1 to HO4 are 511, 628, 472 and 892 ms,
all within 100 to 1000 ms. Over all recordings with bursts the medians run from 104 ms (Pr4) to
2681 ms (MO3); HO6, MO3 and MO9 have medians above 1000 ms.''')
res("**Result: partially reproduced.** In 15 of the 16", '''**Result: partially reproduced.** In 15 of the 16 combinations of organoid, quantity and bound,
more than half of the values lie within the bound (0.53 to 0.89); the exception is HO4 with
pooled unit-burst peak times within 50 ms (0.481). The criterion requires every reading, so the
claim holds in part.''')
res("**Result: reproduced.** Backbone units have higher burst-to-burst corr", '''**Result: reproduced.** Backbone units have higher burst-to-burst correlations than non-rigid
units (0.796 against 0.574, p = 3e-27, 216 units under the Methods' 30% rule; 0.796 against
0.629, p = 9e-16, 150 units under the code's 70% rule), in each organoid. The paper's n of 507
is the number of all sorted units in HO1 to HO4 (507 here as well); the units that pass the
rules are fewer, and burst-to-burst correlations exist only for units active in bursts, so a test
over all 507 cannot be run.''')
res("**Result: reproduced.** The variance of backbone peak times", '''**Result: reproduced.** The variance of backbone peak times rises with relative position under
both readings (rank, p = 6e-4; rescaled median time, p = 1e-4; on log variance p = 3e-6 and
1e-6), with positive rank correlations in each organoid (0.11 to 0.68).''')
res("**Result: reproduced.** Non-rigid units vary more between burst clusters", '''**Result: reproduced.** Non-rigid units vary more between burst clusters than backbone units
under both elbow readings and both organoid sets (mean CV 0.64 to 1.31 against 0.07 to 0.30, p
from 6e-40 to 2e-84). The elbow picked by the kneedle rule (3 to 7 clusters) and by the largest
silhouette (2 or 3) differ, and the outcome is the same.''')
res("**Result: reproduced.** Gabazine raises the burst rate", '''**Result: reproduced.** Gabazine raises the burst rate in each of the four organoids with a
baseline recording (by 2.7 to 10.6 bursts per minute; 7.1 per minute in the mixed model, p =
0.011; paired t-test over the four, p = 0.021).''')
res("**Result: reproduced.** Every NBQX with R-CPP", '''**Result: reproduced.** Every NBQX with R-CPP recording has no burst or one (MO12), against 81 to
114 bursts at baseline, and the fall is significant (10.1 per minute, p = 9e-7).''')
res("**Result: reproduced.** With units pooled per condition", '''**Result: reproduced.** With units pooled per condition, the fraction of bursts in which a unit
fires at least twice rises with gabazine by 0.139 (p = 9e-4), in each of the four organoids with
a baseline. Treating units as matched in the three organoids whose unit positions are identical
across conditions (which the dataset does not state) gives 0.152, p = 7e-8; MO12 has no baseline
file and MO13's unit positions differ between conditions, so both are left out of that variant.''')
res("**Result: blocked (methods underspecified).** The raw rank-order", '''**Result: reproduced, on the assumption that the z-score normalisation is the one used.** The
raw rank-order correlation of backbone sequences rises with gabazine in every organoid (medians
0.07 to 0.35 at baseline, 0.55 to 0.91 with gabazine; 0.381, p printed as 0), and normalised by
z-score to the shuffles gabazine is higher by 2.0 (p printed as 0). Normalised as (A - B)/(A + B)
it is not (-1.15, p = 0.6). That ratio is not usable on these values: the shuffled Spearman
correlations are signed and centred on 0 (median 0.009, 5th to 95th percentile -0.12 to 0.13), so
A + B changes sign for 8.8% of burst pairs and is below 0.1 in magnitude for 5.8%, and the ratio
runs from -86,000 to 3,200. The legend's z-score is adopted; which normalisation the authors used
is asked of them (a methods_unavailable finding).''')
res("**Result: partially reproduced.** In HO2 and HO3 the burst-to-burst", '''**Result: partially reproduced.** In HO2 and HO3 the burst-to-burst correlation rises with age
(means 0.61, 0.69 and 0.72 at 6, 7 and 8 months; age effect F = 18.7, p = 2e-8 with unit type as
the second factor, F = 13.3, p = 3e-6 with organoid), and backbone units are above non-rigid
units at every age. The murine part cannot be tested.''')
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/edit/md.py && echo ok
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/edit/md.py", line 56, in <module>
    res("**Result: reproduced.** Backbone units have higher burst-to-burst corr", '''**Result: reproduced.** Backbone units have higher burst-to-burst correlations than non-rigid
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    units (0.796 against 0.574, p = 3e-27, 216 units under the Methods' 30% rule; 0.796 against
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<2 lines>...
    rules are fewer, and burst-to-burst correlations exist only for units active in bursts, so a test
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    over all 507 cannot be run.''')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/edit/md.py", line 6, in res
    assert len(i)==1, (start, i); nb.set(i[0], text)
           ^^^^^^^^^
AssertionError: ('**Result: reproduced.** Backbone units have higher burst-to-burst corr', [32, 88])
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; sed -i 's/res("\*\*Result: reproduced.\*\* Backbone units have higher burst-to-burst corr", /res("**Result: reproduced.** Backbone units have higher burst-to-burst correlations than", /' $TMPDIR/edit/md.py; $TMPDIR/venv/bin/python $TMPDIR/edit/md.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; echo "nb.save()" >> $TMPDIR/edit/md.py; $TMPDIR/venv/bin/python $TMPDIR/edit/md.py && grep -c "Satterthwaite degrees" reproduce_van_der_molen_2025.ipynb
```

```
1
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat > $TMPDIR/edit/md2.py <<'PYEOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
def res(start, text):
    i=[k for k,c in enumerate(nb.cells) if c["cell_type"]=="markdown" and nb.src(k).startswith(start)]
    assert len(i)==1, (start, i); nb.set(i[0], text)
def after_code(sub, text):
    i=nb.find(sub, "code"); assert nb.cells[i+1]["cell_type"]=="code" or True
    nb.insert_after(i, nb.new("markdown", text))

res("## supp8-backbone-stable-4h", '''## supp8-backbone-stable-4h

> Units classed as backbone in one recording are mostly classed as backbone again 4 h later, units
> classed as non-rigid are mostly classed as non-rigid again, and backbone units keep more
> consistent firing patterns across the two recordings than non-rigid units.

The dandiset gives no unit identifier across recordings. The units are linked here by position:
walking both units tables in order, each 0 h unit is linked to the next 4 h unit at the identical
(x, y) position. Positions alone are not unique (several units share an electrode), but the whole
ordered list of positions is identical at 0 h and 4 h (HO3's 4 h file has one extra unit), which
is what joint sorting of the two recordings gives and what two separate sortings would not. This is
an assumption, and each recording's own result is shown as well. The cross-recording
burst-to-burst correlation pairs every 0 h burst with every 4 h burst (`cross_burst_to_burst`).''')
after_code("x8 = []", '''**Result: reproduced, on the assumption that units are linked by their identical ordered
positions.** All 90 HO2 units and all 116 HO3 units at 0 h are linked (HO3's 4 h unit 24 has no
0 h counterpart). Of the 0 h backbone units, 8 of 10 (HO2) and 13 of 13 (HO3) are backbone at 4 h;
of the non-rigid units, 74 of 80 and 97 of 103 stay non-rigid. Across the two recordings, backbone
units have higher burst-to-burst correlations than non-rigid units in both organoids (HO2 0.748
against 0.627, Welch p = 0.039; HO3 0.821 against 0.607, p = 4e-5, 30% rule); with the code's 70%
rule both means are still higher (HO2 0.738 against 0.699, p = 0.62; HO3 p = 0.001). Within each
recording on its own, backbone units are above non-rigid units as well.''')
res("**Result: reproduced.** For backbone units of HO1 to HO8 the real burs", '''**Result: reproduced.** For backbone units of HO1 to HO8 the real burst-to-burst correlation
(0.605) exceeds the mean over shuffles (0.492): by 0.112 with a random intercept per organoid (p =
1e-26) or per unit (p = 2e-28), and the normalised value is above 0 (0.082, one-sided p = 0.014).
HO8 goes the other way (-0.034); HO7 has no backbone unit. The claims file asks for random
intercepts for unit and organoid together; they are fitted one at a time here.''')
res("**Result: reproduced.** In HO1, backbone similarity is significantly", '''**Result: reproduced.** In HO1, backbone similarity is significantly higher than non-rigid and
than shuffled similarity at every one of the 226 frames of the backbone window (Bonferroni). The
same holds at every frame in HO2 to HO6; in HO8 at 67% and 45% of frames.''')
res("**Result: partially reproduced.** In the seven organoids that have bac", '''**Result: partially reproduced.** In the seven organoids that have backbone units, the mean
similarity over the backbone period exceeds its value at the period's first frame (in HO8 barely,
0.334 against 0.323). HO7 has no backbone unit, so no backbone period, and the claim holds in 7 of
8 organoids.''')
res("**Result: partially reproduced.** In HO1 the first two PCs explain 75.", '''**Result: partially reproduced.** In HO1 the first two PCs explain 75.4% of the backbone units'
variance (within 73 ± 7.3) but 17.4% for non-rigid units (outside 25 ± 2.5); no organoid matches
both values. With the code's burst-only rates, which hold the inverse ISI across the gaps between
bursts, HO1 gives 75.1% and 15.3%, so the zeroing between bursts does not explain the difference.
In each of the seven organoids with backbone units, backbone units have a higher and non-rigid
units a lower two-PC variance than all units; HO7 has no backbone unit.''')
res("**Result: reproduced.** Backbone units have higher burst-to-burst correlations under both", '''**Result: reproduced.** Backbone units have higher burst-to-burst correlations under both
thresholds and both random-effect structures (effects 0.122 to 0.159, p from 1e-17 to 2e-37), and
under the second reading of the recording length (p below 1e-33, table under "Recording length,
reading (b)"). The paper's n of 959 is the number of all sorted units in the six slices (959
here); 685 pass the unit rules.''')
res("**Result: reproduced.** Backbone pairs exceed mixed and non-rigid pair", '''**Result: reproduced.** Backbone pairs exceed mixed and non-rigid pairs under every reading,
both recording lengths included (contrasts 0.16 to 0.26, p printed as 0). The paper's 125,607
pairs is the number of pairs among all sorted units of the slices (125,607 here); 89,669 pairs
among units with at least 30 spikes enter the test.''')
res("**Result: reproduced.** Backbone units fire faster than non-rigid unit", '''**Result: reproduced.** Backbone units fire faster than non-rigid units in every model type
(log10 rate differences 0.35 to 0.81, p below 1e-30), at both slice thresholds and both recording
lengths. The unit counts differ from the legend's: 699, 624, 813 and 1744 units with at least 30
spikes (HO, MO, MS, PR) against 1048, 1179, 786 and 1048; the four murine organoids without bursts
are left out. The dandiset holds 930 sorted human organoid units in the main recordings, fewer than
the legend's 1048.''')
res("**Result: partially reproduced.** Five of the six contrasts favour pri", '''**Result: partially reproduced.** Five of the six contrasts favour primary cultures with p <
0.05; primary backbone units do not fire faster than murine organoid backbone units (difference
0.04 log10 units, p = 0.66 and 0.67; 0.13, p = 0.20 under the second recording length).''')
res("**Result: partially reproduced.** After normalisation, backbone units are more", '''**Result: not reproduced.** With the ratio normalisation, backbone units have higher
burst-to-burst correlations than non-rigid units in human organoids (0.083, p = 2e-10) and slices
(p below 1e-15), but not in murine organoids (0.026, p = 0.11; -0.003, p = 0.84 under the second
recording length). Backbone units of human organoids and slices exceed primary-culture backbone
units at the 90% slice threshold (p = 0.043 and 0.043), murine organoid ones do not (p = 0.59), and
the slice contrast is not significant at 70% (p = 0.11). The criterion's partial outcome needs the
three within-type contrasts, and the murine one fails. With the difference normalisation (a
variant), murine organoids are above (0.044, p = 0.007).''')
res("**Result: reproduced.** In primary cultures normalised burst-to-burst", '''**Result: reproduced.** In primary cultures normalised burst-to-burst correlations do not differ
between backbone and non-rigid units (-0.002, p = 0.81; difference normalisation p = 0.74; p =
0.98 under the second recording length).''')
res("**Result: reproduced.** On per-recording medians of the ratio-normalis", '''**Result: reproduced.** On per-recording medians of the ratio-normalised correlations,
backbone pairs exceed non-rigid pairs in human organoids (0.163, p = 0.001) and murine organoids
(0.236, p = 2e-4, five recordings with bursts), at both slice thresholds and both recording
lengths; the difference normalisation and the pair-level variant agree.''')
res("**Result: reproduced.** On the same model, backbone and non-rigid pair", '''**Result: reproduced.** On the same model, backbone and non-rigid pairs do not differ in slices
(0.053, p = 0.29; 0.068, p = 0.20 at 70%) or primary cultures (0.031, p = 0.47), nor under the
second recording length (p = 0.24 to 0.51). The pair-level variant finds both significant (p below
1e-25).''')
res("**Result: not reproduced.** Normalised backbone pair correlations are", '''**Result: not reproduced.** Normalised backbone pair correlations are above 0 in human
organoids (0.164, one-sided p = 6e-4) but not in murine organoids (0.008, p = 0.36), and not in
slices (0.076, p = 0.065 at 90%; 0.070, p = 0.091 at 70%; under the second recording length p =
0.10 and 0.038). In primary cultures they are above 0 (0.043, p = 0.017), where the paper finds no
effect.''')
res("**Result: partially reproduced.** Backbone lags are longer in human or", '''**Result: partially reproduced.** Backbone lags are longer in human organoids (0.86 log10 units,
p = 7e-7) and murine organoids (0.70, p = 4e-5) than in primary cultures, and human organoids
differ from slices (p = 0.002), but not from murine organoids (0.15, p = 0.29). Setting zero lags
to 1 ms, and the second recording length, give the same pattern. The code's lag table
(Processed_data/Figure7/lag_data.xlsx) has no zero lag, so reading (a), dropping them, is the
code's.''')
res("**Result: not reproduced.** Under reading (a), the code's, murine orga", '''**Result: not reproduced, on the assumption that zero lags are dropped as in the code.** Under
reading (a), the code's, murine organoid lags are longer than slice lags (0.31 log10 units, p =
0.045); with zero lags set to 1 ms, p = 0.07; under the second recording length (zero lags
dropped), p = 0.013. The second contrast, slices against primary cultures, differs under every
reading (p = 0.008, 0.006 and 0.029), where the paper reports P = 0.53.''')
res("**Result: not reproduced.** The normalised three-PC variance of backbo", '''**Result: not reproduced.** The normalised three-PC variance of backbone units exceeds that of
non-rigid units in human organoids (0.188, p = 1e-6) but not in murine organoids (-0.040, p =
0.25); against all units, human organoids again (p = 1e-6) and murine organoids not (p = 0.24),
and the same under the second recording length. Human organoid backbone units exceed those of
slices (p = 0.014) and primary cultures (p = 8e-4); murine organoid ones do not.''')
res("**Result: reproduced.** Non-rigid units have higher CV2 than backbone", '''**Result: reproduced.** Non-rigid units have higher CV2 than backbone units in all four model
types, raw (p from 1e-6 to 7e-39) and z-scored to the shuffles (p from 0.018 to 3e-53), at both
slice thresholds and both recording lengths.''')
res("**Result: blocked (methods underspecified).** With z-scored rank-order", '''**Result: reproduced, on the assumptions that the z-score normalisation and the code's
recording lengths are the ones used.** With z-scored rank-order correlations the model type
matters (F test p = 0.031) and human organoids exceed primary cultures (1.53, p = 0.031), both
weaker than the paper's P = 0.004 and 0.0004. With the ratio normalisation neither holds (p = 0.66
and 0.49), but that ratio is not usable on signed correlations centred on 0 (ed4d). Under the
second recording length the z-scored contrasts are not significant (p = 0.064 and 0.099), with 5
shuffles per recording.''')
res("**Result: not reproduced.** Backbone units fire faster in the Sharf re", '''**Result: not reproduced.** Backbone units fire faster in the Sharf recordings (0.72 log10
units, p = 2e-50), and also in the Alam El Din recordings (0.12, p = 0.0019), where the paper
finds no difference (P = 0.40).''')
res("**Result: reproduced.** Normalised burst-to-burst correlations are hig", '''**Result: reproduced.** Normalised burst-to-burst correlations are higher for backbone units in
both sets (Sharf 0.040, p = 0.005; Alam El Din 0.119, p = 1e-8).''')
res("**Result: partially reproduced.** Backbone pairs are above 0 in both s", '''**Result: partially reproduced.** Backbone pairs are above 0 in both sets (Sharf 0.148, p =
0.010; Alam El Din 0.185, p = 0.041), and non-rigid pairs are not; mixed pairs are also above 0
in the Sharf recordings (0.087, p = 0.048), where the paper finds P = 0.145.''')
nb.save()
PYEOF
$TMPDIR/venv/bin/python $TMPDIR/edit/md2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
def fix(a,b):
    i=[k for k,c in enumerate(nb.cells) if a in nb.src(k)]; assert len(i)==1,(a,i); nb.replace(i[0],a,b)
fix("(effects 0.122 to 0.159, p from 1e-17 to 2e-37)", "(effects 0.122 to 0.159, p from 5e-17 to 2e-37)")
fix("(log10 rate differences 0.35 to 0.81, p below 1e-30), at both slice thresholds and both recording\nlengths.", "(log10 rate differences 0.34 to 0.81, p below 1e-28), at both slice thresholds and both recording\nlengths.")
fix("raw (p from 1e-6 to 7e-39)", "raw (p from 1e-6 to 5e-39)")
fix("print(x8.round(4).to_string(index=False))", "print(x8.to_string(index=False, float_format=lambda v: f\"{v:.3g}\"))")
nb.save()
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'PYEOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("reproduce_van_der_molen_2025.ipynb")
i=nb.find("ja, jb = judged_contrasts(R), judged_contrasts(R40)", "code")
nb.insert_after(i, nb.new("markdown", '''Under reading (b) the lengths run from 80 s (Pr5) to 1270 s (M3S2), and 25 recordings are
analysed again; backbone sets change most in the slices (M2S1 149 to 123 units, M1S1 31 to 22) and
MO7 (40 to 49). The judged contrasts keep their direction and significance under (b), with these
exceptions: the z-scored model-type effect of supp10b is no longer significant (main effect p =
0.064, human organoids against primary cultures p = 0.099); slice backbone pairs become
significantly above 0 at the 70% threshold (fig7c-backbone-pairs-above-random, p = 0.038); and
slice backbone units no longer exceed primary-culture ones at 90% (fig7b-normalized-b2b, p =
0.056). Only the first bears on an outcome, as recorded under supp10b.'''))
i=nb.find("d2 = pd.DataFrame([dict(rec=k, type=R[k][\"mtype\"], **R[k][\"d2\"]) for k in RECS])", "code")
nb.insert_after(i, nb.new("markdown", '''**Result: partially reproduced, on the assumption of how the AR fit check is read.** Shuffling
raises d2 in every recording: intact d2 has mean 0.044 (0.014 to 0.099), shuffled 0.221 (0.199 to
0.251), Welch t = 38.3, p = 5e-38. All 31 intact recordings have d2 at most 0.1, so the kept
recordings do under either reading of the fit check. The numbers kept differ from the paper's (3,
7, 4 and 7 for HO, MO, MS and PR): 0, 5, 0 and 1 when every density and spectrum ratio must be
within one order of magnitude, 7, 9, 3 and 8 when their median must be. The paper does not say
how the comparison was made, so the counts are open (a question for the authors).'''))
i=[k for k,c in enumerate(nb.cells) if nb.src(k).startswith("## Summary")][0]
nb.set(i, '''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| methods-burst-count | reproduced (mean only; recordings range from 0 to 156 bursts) |
| fig1c-example-burst-count | reproduced (HO1, 46 bursts) |
| ed1c-lognormal-rates | reproduced (reading a, all units) |
| fig1d-burst-duration | reproduced |
| fig1e-peaks-near-burst-peak | partially reproduced (15 of 16 readings) |
| fig2-backbone-fraction | reproduced (units with at least 30 spikes) |
| fig2e-b2b-correlation | reproduced |
| fig2g-variance-latency | reproduced |
| ed3f-burst-cluster-variability | reproduced |
| ed4b-gabazine-more-bursts | reproduced |
| ed4b-nbqx-cpp-abolish-bursts | reproduced |
| ed4c-gabazine-participation | reproduced |
| ed4d-gabazine-rank-order | reproduced (assumed: z-score normalisation) |
| supp2a-backbone-fraction-declines | partially reproduced (human only) |
| supp2c-b2b-increases-with-age | partially reproduced (human only) |
| supp8-backbone-stable-4h | reproduced (assumed: units linked by position) |
| ed5-shuffle-reduces-b2b | reproduced |
| fig3e-pairwise-correlation | reproduced |
| fig3f-backbone-pairs-in-tail | partially reproduced |
| fig4c-similarity-variance | reproduced |
| fig4d-burst-similarity | reproduced |
| fig4e-similarity-rises-at-backbone-onset | partially reproduced (HO7 has no backbone) |
| supp13-top-correlated-units-similarity | reproduced |
| fig4f-pca-variance | partially reproduced |
| fig6f-slice-b2b-correlation | reproduced |
| fig6g-slice-pairwise-correlation | reproduced |
| fig7a-backbone-higher-rate | reproduced |
| fig7a-primary-higher-rate | partially reproduced |
| fig7b-normalized-b2b | not reproduced (murine organoids) |
| fig7b-primary-no-b2b-difference | reproduced |
| fig7c-normalized-pairwise | reproduced |
| fig7c-slices-primaries-no-pair-difference | reproduced |
| fig7c-backbone-pairs-above-random | not reproduced |
| fig7d-lag-times | partially reproduced |
| fig7d-murine-organoids-slices-same-lag | not reproduced (assumed: zero lags dropped, as the code) |
| fig7e-pca-backbone-variance | not reproduced |
| supp24c-nonrigid-more-variable | reproduced |
| supp10b-rank-order-by-model | reproduced (assumed: z-score normalisation, code's lengths) |
| supp27-d2-near-critical | partially reproduced (assumed: reading of the AR fit check) |
| ed2d-alam-el-din-rates | not reproduced |
| ed2e-alam-el-din-b2b | reproduced |
| ed2f-backbone-pairs-above-zero | partially reproduced |
| HMM claims (supp18, fig5c, fig5d, fig5f, fig7f, supp24d, supp26) | in `hmm_van_der_molen_2025.ipynb` |
| supp5-murine-organoid-forebrain-identity | blocked (data elsewhere; markers not listed) |

**How the analysis differs from the paper's.** 10 shuffles per recording (3 for pairwise
correlations and shuffled similarity; 5 and 2 under the second recording length) where the paper
uses 100; burst-only rates that do not hold the inverse ISI across the gap between bursts (the
code's rates are shown for fig4f); overlapping bursts merged at 700 ms where the paper raises the
peak distance for some recordings; mixed models fitted here by REML with Satterthwaite t tests in
place of the paper's R; MATLAB smoothing replaced by its scipy counterparts (Gaussian with
standard deviation one fifth of the window); the shuffles cover the analysed segment (the code
shuffles the first 180 s); d2 from a Python port of the code of Sooter et al., with one shuffle per
recording and an AR fit check whose rule the paper does not give.

**What was found about the dataset.** Every recording the paper analyses is in the dandiset as a
sorted file with a 1 ms spike matrix; the backbone units and burst counts of HO1 to HO4 equal the
numbers in the paper's processed tables (27, 26, 23 and 15 backbone units; 46, 31, 42 and 28
bursts). The HO2 and HO3 longitudinal recordings are deposited two or three times. The baseline
sorted file of MO12 and all murine organoid longitudinal recordings are missing. Units carry
positions but no identifier linking them across recordings of one organoid; the 0 h and 4 h
recordings of HO2 and HO3 have identical ordered positions. Pr1 to Pr4 are labelled rat, the paper
calls them murine. With the stated burst detection, four murine organoids have no burst (their
highest peaks reach 3.0 to 3.7 times the RMS), so the paper's murine organoid parameters are not
given.''')
nb.save()
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'PYEOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
nb=NB("hmm_van_der_molen_2025.ipynb")
def res(start, text):
    i=[k for k,c in enumerate(nb.cells) if c["cell_type"]=="markdown" and nb.src(k).startswith(start)]
    assert len(i)==1, (start, i); nb.set(i[0], text)
res("**Result: reproduced.** The held-out log likelihood", '''**Result: reproduced.** Scored the same way on both, as the log likelihood of the held-out
entries given the rest, the real data beat the randomized surrogate in all 120 combinations of
fold, K and organoid with 20% held out (smallest margin 0.015 nats per entry, HO4 at K = 30) and in
all 40 with the code's 10% (smallest 0.021). The round-1 scoring gave the surrogate the marginal
likelihood of its held-out entries, which is lower by 0.008 nats per entry on average; with it the
smallest margin was 0.009.''')
res("**Result: not reproduced.** The state entropy", '''**Result: not reproduced.** The state entropy across bursts, averaged over K, has its minimum
below both window ends in seven organoids, but within 90 ms of the peak only in HO8, and within
the backbone window in three (HO1, HO6, HO8); in HO2, HO3 and HO4 the minimum lies 120 to 510 ms
before the peak, where the entropy is already near 0 at the window's start in HO3 (0.015) and HO4
(0.18). The criterion asks for at least 6 of 8 under both readings.''')
res("**Result: partially reproduced.** The state-feature accuracy", '''**Result: not reproduced.** The state-feature accuracy, 86.5% ± 11.6% over all models, is
within 83.9 ± 12.0%, but the rate-only accuracy, 73.9% ± 23.2% over seven organoids, is outside
63.2 ± 10.4%, and states beat rate significantly in neither test: paired over organoids p =
0.086; per organoid in four of seven (HO2, HO3 and HO4, where rate alone reaches 89% to 95%, are
not). The majority class is 54% to 88% of units (mean 70.6%); the rate-only accuracy is below it in
HO5 and HO8. HO7 has no backbone unit to classify.''')
res("**Result: reproduced.** HMM dimensionality", '''**Result: reproduced.** HMM dimensionality at theta = 0.75 is lower in primary cultures (mean
1.73) than in human (2.85, p = 4e-6) and murine organoids (2.59, p = 0.005). Human organoids and
slices do not differ here (p = 0.60), where the paper reports P = 0.04 (not judged).''')
res("**Result: reproduced.** In every model type the median", '''**Result: reproduced.** In every model type the median fraction of non-Poisson states is 0 or
0.001 for non-rigid units and higher for backbone units (0.013 to 0.262); backbone minus
non-rigid 0.21 in the mixed model, p printed as 0.''')
res("**Result: reproduced.** Primary cultures traverse", '''**Result: partially reproduced.** Primary cultures traverse more states per second in the
backbone window than human organoids (by 19.8, p = 9e-5), and human and murine organoids do not
differ (4.5, p = 0.35), but primary cultures are above slices by 8.8 with p = 0.056, not below
0.05. Primary cultures also exceed murine organoids (p = 2.5e-5), where the paper reports P =
0.064. The p-values are not Tukey-adjusted; an adjustment would only raise them.''')
i=[k for k,c in enumerate(nb.cells) if nb.src(k).startswith("## Summary")][0]
nb.set(i, '''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| supp18-hmm-likelihood-real-above-shuffled | reproduced |
| fig5c-states-converge-at-peak | not reproduced |
| fig5d-backbone-more-states | reproduced |
| fig5f-svm-states-beat-rate | not reproduced |
| fig7f-hmm-dimensionality | reproduced |
| supp24d-backbone-non-poisson | reproduced |
| supp26-state-traversal | partially reproduced |

**Differences from the paper's method.** HMMs fitted with this entry's EM in place of SSM, with
K = 10, 12, ..., 30 in place of every K from 10 to 30 and at most 300 iterations in place of 5000
(41 of 341 models stopped there); cross-validation folds refitted from scratch with K = 10, 20 and
30; the Poisson GLMM of Fig. 7F replaced by a Poisson GEE with exchangeable correlation within
recording; for fig5d, K enters as a fixed factor in place of a random intercept; mixed models
tested with Satterthwaite t (`sequences.lmm`) without the Tukey adjustment of emmeans.''')
i=nb.find("| supp18-hmm-likelihood-real-above-shuffled | tested |","markdown")
nb.save()
PYEOF
grep -o "fitted [0-9]* HMMs" $TMPDIR/out/hmm.txt; sed -n '/CELL 18 tags/,/Test:/p' $TMPDIR/out/hmm.txt | tail -8
```

```
fitted 341 HMMs
Pr7     NaN   NaN   NaN  2.36
Pr8     NaN   NaN   NaN  1.64
{'HO': 2.85, 'MO': 2.59, 'MS': 3.03, 'PR': 1.73}
PR minus HO (log scale): -0.502, p 3.5e-06
PR minus MO (log scale): -0.404, p 0.0046
HO minus MS (log scale): -0.061, p 0.6
MO minus MS (log scale): -0.159, p 0.29
Test: Poisson GEE with an exchangeable correlation within recording (the paper: glmer with a random intercept).
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; cat README.md
```

```
# van der Molen, Spaeth, Chini et al. (2025) from dandiset 001603

Tests the findings of [van der Molen et al. (2025)](https://doi.org/10.1038/s41593-025-02111-0)
on [DANDI:001603](https://dandiarchive.org/dandiset/001603/0.260923.0623), which holds the sorted
spike trains of 8 human organoids, 9 murine organoids, 6 neonatal mouse cortical slices and 8
primary cultures, murine organoids recorded with gabazine and with NBQX and R-CPP, and longitudinal
recordings of two human organoids.

Of the 50 claims, 29 are reproduced, 11 partially reproduced, 5 not reproduced and 5 blocked. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/van-der-molen-2025-01.yaml`](../../attempts/van-der-molen-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Burst detection as the Methods state it reproduces the paper's burst counts and backbone units for
HO1 to HO4 exactly, but finds no burst in four of the nine murine organoids, so claims on murine
organoids rest on the five that have bursts. The baseline sorted file of MO12 and the longitudinal
murine organoid recordings are not in the dandiset.

[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; python3 - <<'EOF'
s=open("README.md").read()
s=s.replace("Of the 50 claims, 29 are reproduced, 11 partially reproduced, 5 not reproduced and 5 blocked.","Of the 50 claims, 31 are reproduced, 11 partially reproduced, 7 not reproduced and 1 blocked.")
s=s.replace("""organoids rest on the five that have bursts. The baseline sorted file of MO12 and the longitudinal
murine organoid recordings are not in the dandiset.""","""organoids rest on the five that have bursts. The baseline sorted file of MO12 and the longitudinal
murine organoid recordings are not in the dandiset. Units have no identifier across recordings;
the 0 h and 4 h recordings of HO2 and HO3 are linked here by their identical ordered unit
positions.""")
s=s.replace("""correlations, burst similarity, PCA and the comparisons across model types (about 23 minutes,
  most of it the shuffles).""","""correlations, burst similarity, PCA, d2 and the comparisons across model types, under both
  readings of the recording length (about 35 minutes, most of it the shuffles).""")
s=s.replace("the hidden Markov model claims (about 22 minutes).","the hidden Markov model claims (about 20 minutes).")
open("README.md","w").write(s)
EOF
grep -n "31 are\|about" README.md
```

```
9:Of the 50 claims, 31 are reproduced, 11 partially reproduced, 7 not reproduced and 1 blocked. The
25:  readings of the recording length (about 35 minutes, most of it the shuffles).
26:- `hmm_van_der_molen_2025.ipynb`: the hidden Markov model claims (about 20 minutes).
```

**Agent calls Bash**

```bash
cd  sed -i 's/  runtime_minutes: 23/  runtime_minutes: 35/; s/  runtime_minutes: 22/  runtime_minutes: 20/' entries/van-der-molen-2025/entry.yaml; sed -i 's/compares burst-to-burst and pairwise correlations, burst similarity, PCA and hidden Markov models/compares burst-to-burst and pairwise correlations, burst similarity, PCA, d2 and hidden Markov models/' entries/van-der-molen-2025/entry.yaml; grep -n "runtime\|d2" entries/van-der-molen-2025/entry.yaml; python3 tools/entry.py check entries/van-der-molen-2025 2>&1 | tail -20
```

```
9:  compares burst-to-burst and pairwise correlations, burst similarity, PCA, d2 and hidden Markov models
15:  runtime_minutes: 35
18:  runtime_minutes: 20
0 error(s)
```

**Agent calls Bash**

```bash
cd  date -u; python3 tools/entry.py all entries/van-der-molen-2025 2>&1 | tail -20; date -u
```

```
Tue Nov 17 18:52:53 UTC 2026
Installed kernelspec registry-van-der-molen-2025 in executed/van-der-molen-2025/.venv/share/jupyter/kernels/registry-van-der-molen-2025
0 error(s)
pass  reproduce_van_der_molen_2025.ipynb  (1670 s)
pass  hmm_van_der_molen_2025.ipynb  (1085 s)
Tue Nov 17 19:38:54 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/van-der-molen-2025; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py reproduce_van_der_molen_2025.ipynb $TMPDIR/out/main_final.txt; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py hmm_van_der_molen_2025.ipynb $TMPDIR/out/hmm_final.txt; diff <(grep -v "^##### \|ran in\|analysed .* in\|analysed again in" $TMPDIR/out/hmm.txt) <(grep -v "^##### \|ran in\|analysed again in" $TMPDIR/out/hmm_final.txt) | head; diff <(grep -v "^##### \|ran in\|analysed .* in\|analysed again in" $TMPDIR/out/main.txt) <(grep -v "^##### \|ran in\|analysed .* in\|analysed again in" $TMPDIR/out/main_final.txt) | head -150
```

```
4c4
< fitted 341 HMMs in 830 s
---
> fitted 341 HMMs in 672 s
400c400
< b2b30: 216 units (91 backbone); mean backbone 0.796, non-rigid 0.574; LMM effect 0.210, z 12.5, p 2.8e-27
---
> b2b30: 216 units (91 backbone); mean backbone 0.796, non-rigid 0.574; LMM effect 0.210, t 12.5, p 2.8e-27
402c402
< b2b70: 150 units (91 backbone); mean backbone 0.796, non-rigid 0.629; LMM effect 0.170, z 9.0, p 8.9e-16
---
> b2b70: 150 units (91 backbone); mean backbone 0.796, non-rigid 0.629; LMM effect 0.170, t 9.0, p 8.9e-16
573c573
< HO2: 90 units at 0 h, 90 at 4 h; linked 46, in the same order: True; 4 h units without a 0 h unit: [1, 2, 4, 6, 9, 10, 11, 12, 13, 17, 18, 19, 20, 21, 22, 31, 32, 33, 38, 39, 41, 42, 50, 51, 52, 54, 56, 57, 58, 59, 60, 62, 63, 65, 69, 73, 74, 75, 76, 78, 84, 85, 88, 89]
---
> HO2: 90 units at 0 h (61 distinct positions), 90 at 4 h; 0 h units linked in order: 90; 4 h units left out: []
577,578c577,578
< backbone          4          1
< non-rigid         3         38
---
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/van-der-molen-2025; $TMPDIR/venv/bin/python - <<'EOF'
import sys; sys.path.insert(0,"/tmp/claude-1001/edit")
from nb import NB
for path, fixes in [("reproduce_van_der_molen_2025.ipynb", [("HO3 0.821 against 0.607, p = 4e-5, 30% rule", "HO3 0.820 against 0.607, p = 4e-8, 30% rule"), ("matters (F test p = 0.031)", "matters (F test p = 0.032)")]),
                    ("hmm_van_der_molen_2025.ipynb", [("than in human (2.85, p = 4e-6)", "than in human (2.85, p = 3.5e-6)")])]:
    nb=NB(path)
    for a,b in fixes:
        i=[k for k,c in enumerate(nb.cells) if a in nb.src(k)]; assert len(i)==1,(a,i); nb.replace(i[0],a,b)
    nb.save()
EOF
date -u
```

```
Tue Nov 17 19:39:16 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['verifications'],indent=0)[:2500]); print(json.dumps(p.get('inputs'),indent=0)[:1200])
"; grep -n "^inputs:" -A8 attempts/*.yaml | head -20
```

```
{
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"date",
"kind",
"by",
"results"
],
"properties": {
"date": {
"type": "string",
"format": "date"
},
"kind": {
"enum": [
"agent",
"person",
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(list(o['properties'].keys())); print(o.get('required'))
print(json.dumps(s['properties']['findings']['items']['properties'],indent=0)[:800])"
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
['claim', 'outcome']
{
"kind": {
"enum": [
"metadata_error",
"data_missing",
"identifier_missing",
"metadata_insufficient",
"selection_undocumented",
"methods_unavailable",
"format_error",
"code_mismatch",
"paper_inconsistency",
"other"
]
},
"statement": {
"type": "string",
"minLength": 1
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "verification" tools/entry.py | head -30
```

```
350:        for rnd in (attempt.get("verifications") or [])[1:]:
372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
cd  sed -n 1,30p attempts/van-der-molen-2025-01.yaml | head -30; grep -n "^[a-z_]*:" attempts/van-der-molen-2025-01.yaml
```

```
schema_version: 3
id: van-der-molen-2025-01
datasets:
- archive: dandi
  id: "001603"
  version: 0.260923.0623
  doi: 10.48324/dandi.001603/0.260923.0623
  relation: primary
paper: doi:10.1038/s41593-025-02111-0
date: 2026-11-17
entry: van-der-molen-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec; cat > $TMPDIR/rec/upd1.py <<'PYEOF'
U = {}
NB = "reproduce_van_der_molen_2025.ipynb"
HM = "hmm_van_der_molen_2025.ipynb"
U["methods-burst-count"] = dict(measured=34.8, notes=
"Mean 34.8 bursts over the 31 recordings under the code's lengths (SE 6.3, range 0 to 156), within 38 plus or minus 4. The mean matches but the recordings do not each hold about 40 bursts; four murine organoids (MO2, MO4, MO5, MO6) have none under the stated detection and MO1 and MO7 have 113 and 156, which offset them. With 800 ms minimum distance the mean is 34.7; with 2000 ms for every recording it is 29.5, outside, but the Methods raise the distance only for recordings with long bursts. 35 overlapping bursts in 13 recordings are dropped (none in HO1 to HO4).",
add_dev=["Of overlapping bursts (a peak in the tail of a longer burst), only the one with the higher peak is kept, at 700 ms in every recording. The Methods raise min_dist \"up to 2000 ms\" for \"recordings with long duration bursts ... to prevent peaks in the tail of the burst from being detected as separate burst instances\" without naming the recordings; this applies the stated purpose to all (35 bursts in 13 recordings). 2000 ms for every recording is shown as a variant."])
U["fig1d-burst-duration"] = dict(notes="Median burst durations of HO1 to HO4 are 511, 628, 472 and 891.5 ms, all between 100 and 1000 ms. Over the 27 recordings with bursts the medians run from 104 ms (Pr4) to 2681 ms (MO3); HO6, MO3 and MO9 are above 1000 ms.")
U["fig1e-peaks-near-burst-peak"] = dict(notes="More than half of the values fall within the bound in 15 of 16 combinations of organoid, quantity and bound (fractions 0.53 to 0.89). The exception is HO4, pooled unit-burst peak times within 50 ms (0.481). The criterion names the readings and requires every one, so the claim holds in part; the readings are not alternatives to choose between.")
U["fig2e-b2b-correlation"] = dict(notes="Backbone 0.796 against non-rigid 0.574 (effect 0.210, p 3e-27, 216 units) under the Methods' 30% rule, and 0.796 against 0.629 (p 9e-16, 150 units) under the code's 70% rule; higher in each organoid. The measured value is the number of sorted units in HO1 to HO4, which equals the paper's n of 507; the units that pass the unit rules and enter the test are 216 or 150. Burst-to-burst correlations exist only for units active in bursts, so a test over all 507 units cannot be run.",
replace_dev={"Mixed models fitted by REML": "Mixed models fitted by REML with a random intercept, tested with t on Satterthwaite degrees of freedom (sequences.lmm, checked against an exact balanced case), in place of the paper's R; the 30-spike rule counts spikes over the whole analysed recording."})
U["fig2g-variance-latency"] = dict(notes="Over 91 backbone units the peak-time variance rises with relative position, p 6e-4 for the rank reading and 1e-4 for the rescaled median time (log variance, p 3e-6 and 1e-6); the rank correlation is positive in each organoid (0.11 to 0.68).")
U["ed3f-burst-cluster-variability"] = dict(notes="Non-rigid units vary more between burst clusters than backbone units under both elbow readings and both organoid sets (mean CV 0.64 to 1.31 against 0.07 to 0.30; p 6e-40 to 2e-84). The kneedle rule picks 3 to 7 clusters, the silhouette 2 or 3.")
U["ed4b-gabazine-more-bursts"] = dict(notes="Burst rate rises with gabazine in each of the four organoids with a baseline (by 2.7 to 10.6 bursts per minute); mixed model 7.1 per minute, p 0.011 (5 organoids, 9 recordings); paired t-test over the four, p 0.021.")
U["ed4b-nbqx-cpp-abolish-bursts"] = dict(notes="The five NBQX with R-CPP recordings have 0, 0, 1 (MO12), 0 and 0 bursts against 81 to 114 at baseline; burst rate falls by 10.1 per minute, p 9e-7.")
U["ed4c-gabazine-participation"] = dict(notes="Units pooled per condition (the dataset does not identify units across recordings), the fraction of bursts with at least two spikes rises by 0.139 with gabazine, p 9e-4, in each of the four organoids with a baseline. Treating units as matched in MO10, MO11 and MO14, whose unit positions are identical across conditions, gives 0.152, p 7e-8; MO12 has no baseline file and MO13's positions differ between conditions, so both are left out of that variant.")
U["ed4d-gabazine-rank-order"] = dict(outcome="reproduced", assumed=True, drop=["blocked_by"], notes="Raw rank-order correlations of backbone sequences rise with gabazine in every organoid (medians 0.07 to 0.35 at baseline, 0.55 to 0.91 with gabazine; 0.381, p printed as 0), and z-scored to the shuffles gabazine is higher by 2.0 (p printed as 0). As (A - B)/(A + B) per burst pair it is not (-1.15, p 0.6). That ratio is not usable on these values. The shuffled Spearman correlations are signed and centred on 0 (median 0.009, 5th to 95th percentile -0.12 to 0.13), so A + B changes sign for 8.8% of burst pairs and is below 0.1 in magnitude for 5.8%, and the ratio runs from -86,000 to 3,200. The legend's z-score is adopted (assumed). Which normalisation was used, and at which level, is asked of the authors (methods_unavailable finding).",
add_dev=["Assumption. The rank-order correlations are normalised by z-score to the shuffles, as the Extended Data Fig. 4D legend says, and not as (A - B)/(A + B), the Supplementary Methods' general normalisation, which is unstable on signed correlations whose shuffle mean is near 0. Both are shown."])
U["supp2c-b2b-increases-with-age"] = dict(notes="In HO2 and HO3 the burst-to-burst correlation rises with age (0.61, 0.69, 0.72 at 6, 7 and 8 months; age effect F 18.7, p 2e-8 with unit type as the second factor, F 13.3, p 3e-6 with organoid), and backbone units are above non-rigid units at every age. The murine part cannot be tested (no longitudinal murine organoid recordings).")
U["supp8-backbone-stable-4h"] = dict(outcome="reproduced", assumed=True, drop=["blocked_by"], notebook=NB, output="claim:supp8-backbone-stable-4h",
notes="Units linked by position, walking both units tables in order. All 90 HO2 units and all 116 HO3 units at 0 h are linked; the two ordered lists of positions are identical, apart from one extra 4 h unit in HO3 (unit 24). Of the 0 h backbone units, 8 of 10 (HO2) and 13 of 13 (HO3) are backbone at 4 h; of the non-rigid units, 74 of 80 and 97 of 103 stay non-rigid. Across recordings, backbone units have higher burst-to-burst correlations than non-rigid units in both organoids (HO2 0.748 against 0.627, Welch p 0.039; HO3 0.820 against 0.607, p 4e-8, 30% rule); with the 70% rule the means are still higher (HO2 0.738 against 0.699, p 0.62; HO3 p 0.001). Within each recording alone backbone units are above non-rigid units too.",
add_dev=["Assumption. The dandiset has no unit identifier across the 0 h and 4 h recordings. Units are linked by their identical (x, y) positions in the same order, which joint sorting gives and two separate sortings would not; positions alone are not unique (61 distinct positions for 90 HO2 units). Results of each recording alone are also shown.",
"Cross-recording burst-to-burst correlation, every 0 h burst against every 4 h burst in which the unit fires at least twice in the -250 to 500 ms window (Methods' burst-to-burst correlation, bursts paired across recordings as Supplementary Fig. 8E), units passing the unit rules in both recordings."])
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec/upd2.py <<'PYEOF'
U["ed5-shuffle-reduces-b2b"] = dict(notes="Backbone units of HO1 to HO8 (259 with both values), real 0.605 against shuffled mean 0.492; (a) 0.112 with a random intercept per organoid, p 1e-26, per unit p 2e-28; (b) normalised mean 0.082, one-sided p 0.014. HO8 goes the other way (-0.034).",
replace_dev={"10 shuffles per recording": "10 shuffles per recording, where the paper uses 100. Reading (a) fits the unit and organoid intercepts one at a time, where the criterion names both together."})
U["fig3e-pairwise-correlation"] = dict(notes="Backbone pairs 0.70 against mixed 0.36 and non-rigid 0.23, both contrasts p printed as 0, in each organoid. The measured value is the number of pairs among all sorted units of HO1 to HO4, which equals the paper's n; 9,648 pairs among units with at least 30 spikes enter the test.")
U["fig3f-backbone-pairs-in-tail"] = dict(notes="The backbone-pair mean lies above the 75th percentile of all pairs in every organoid (87th to 95th percentile) and above the 90th in three of four (HO3 at the 87th). The criterion requires both readings, so the claim holds in part. Skew 0.26 to 1.08; R squared of a normal fit to the log correlations 0.28 to 0.80.")
U["fig4d-burst-similarity"] = dict(notes="In HO1 backbone similarity exceeds non-rigid and shuffled similarity significantly at all 226 frames of the backbone window (Bonferroni). The same in HO2 to HO6; HO8 67% and 45% of frames.")
U["fig4e-similarity-rises-at-backbone-onset"] = dict(notes="In the seven organoids with backbone units the mean similarity over the backbone period exceeds its value at the first frame (HO8 barely, 0.334 against 0.323). HO7 has no backbone unit under the 100% rule, so no backbone period; 7 of 8.")
U["fig4f-pca-variance"] = dict(notes="In HO1 the first two PCs explain 75.4% for backbone units (within 73 plus or minus 7.3) and 17.4% for non-rigid units (outside 25 plus or minus 2.5); no organoid matches both. With the code's burst-only rates, which hold the inverse ISI across the gaps between bursts, HO1 gives 75.1% and 15.3%, again no organoid matches both. In each of the seven organoids with backbone units, backbone is above and non-rigid below all units; HO7 has no backbone unit.")
U["supp18-hmm-likelihood-real-above-shuffled"] = dict(notes="Held-out log likelihood per entry, scored on both as log p(held-out | rest), is higher on real data than on the surrogate in all 120 fold, K and organoid combinations with 20% held out (smallest margin 0.015 nats per entry, HO4 at K 30; every fold's margin printed) and in all 40 with 10% held out (smallest 0.021). The round-1 scoring gave the surrogate the marginal likelihood of its held-out entries, 0.008 nats per entry lower on average; with it the smallest margin was 0.009.")
U["fig5c-states-converge-at-peak"] = dict(notes="The state entropy across bursts (averaged over K) has its minimum below both window ends in seven organoids, within 90 ms of the peak in one (HO8), and within the backbone window in three (HO1, HO6, HO8); in HO2, HO3 and HO4 it lies 120 to 510 ms before the peak, where in HO3 and HO4 the entropy is already near 0 at the window's start (0.015 and 0.18). The criterion needs 6 of 8 under both readings.",
replace_dev={"K = 10, 12, ..., 30": "K = 10, 12, ..., 30 (11 models per recording) in place of every K from 10 to 30, at most 300 EM iterations (41 of 341 models stopped there), with the entry's EM in place of SSM."})
U["fig5f-svm-states-beat-rate"] = dict(outcome="not_reproduced", measured=[86.5, 73.9], notes="State-feature accuracy 86.5% plus or minus 11.6 over all models is within 83.9 plus or minus 12.0; rate accuracy 73.9% plus or minus 23.2 over seven organoids is outside 63.2 plus or minus 10.4. States beat rate in neither test, (a) paired over organoids p 0.086, (b) per organoid significant in four of seven; in HO2, HO3 and HO4 rate alone reaches 89% to 95%. The majority class is 54% to 88% of units (mean 70.6%); rate-only accuracy is below it in HO5 and HO8. The paper states no chance level. HO7 has no backbone unit to classify. The criterion defines no partial outcome, and its central comparison fails.")
U["fig6f-slice-b2b-correlation"] = dict(notes="Backbone units have higher correlations at both thresholds and with a random intercept per slice or per animal (effects 0.122 to 0.159, p 5e-17 to 2e-37; 685 units in the test), and under the second reading of the recording length (p below 1e-33). The measured value is the number of sorted units in the six slices, which equals the paper's n.")
U["fig6g-slice-pairwise-correlation"] = dict(notes="Backbone pairs exceed mixed and non-rigid pairs under every reading, both recording lengths included (contrasts 0.16 to 0.26, p printed as 0; 89,669 pairs among units with at least 30 spikes). The measured value is the number of pairs among all sorted units of the slices, which equals the paper's n.")
U["fig7a-backbone-higher-rate"] = dict(notes="Backbone units fire faster in every model type (log10 differences 0.34 to 0.81, p below 1e-28) at both slice thresholds and both recording lengths. Unit counts with at least 30 spikes (699, 624, 813, 1744) are outside the legend's (1048, 1179, 786, 1048); all sorted units are 930, 1273, 959 and 2001, so the dandiset holds fewer human organoid units than the legend counts. The four murine organoids without bursts are left out, so murine organoids are 5 of 9 recordings.")
U["fig7a-primary-higher-rate"] = dict(notes="Five of six contrasts favour primary cultures with p below 0.05; primary backbone units do not fire faster than murine organoid backbone units (0.04 log10 units, p 0.66 and 0.67; 0.13, p 0.20 under the second recording length).")
U["fig7b-normalized-b2b"] = dict(outcome="not_reproduced", notes="With the ratio normalisation, backbone above non-rigid in human organoids (0.083, p 2e-10) and slices (p below 1e-15 at both thresholds), not in murine organoids (0.026, p 0.11; -0.003, p 0.84 under the second recording length). Human organoid and slice backbone units exceed primary backbone units at the 90% slice threshold (p 0.043 and 0.043), murine organoid ones do not (p 0.59), and slices not at 70% (p 0.11). The criterion's partial outcome needs the three within-type contrasts; the murine one fails. With the difference normalisation (variant) murine organoids are above (0.044, p 0.007). In round 1 the murine contrast was p 7e-5; it changed with the merged overlapping bursts (MO9), the whole-recording 30-spike rule and the Satterthwaite tests.")
U["fig7b-primary-no-b2b-difference"] = dict(notes="Primary backbone minus non-rigid -0.002, p 0.81 (difference normalisation -0.003, p 0.74; p 0.98 under the second recording length).")
U["fig7c-normalized-pairwise"] = dict(notes="On per-recording medians, backbone pairs exceed non-rigid pairs in human organoids (0.163, p 0.001) and murine organoids (0.236, p 2e-4, five recordings with bursts) at both slice thresholds and both recording lengths; the difference normalisation and pair-level variants agree.")
U["fig7c-slices-primaries-no-pair-difference"] = dict(notes="Slices 0.053, p 0.29 (0.068, p 0.20 at 70%); primary cultures 0.031, p 0.47; under the second recording length p 0.24 to 0.51. The pair-level variant finds both significant.")
U["fig7c-backbone-pairs-above-random"] = dict(notes="Normalised backbone pairs are above 0 in human organoids (0.164, one-sided p 6e-4) but not in murine organoids (0.008, p 0.36); slices 0.076, p 0.065 at 90% and 0.070, p 0.091 at 70% (under the second recording length p 0.10 and 0.038); primary cultures are above 0 (0.043, p 0.017) where the paper finds no effect.")
U["fig7d-lag-times"] = dict(notes="Lags are longer in human (0.86 log10 units, p 7e-7) and murine organoids (0.70, p 4e-5) than in primary cultures and human organoids differ from slices (p 0.002), but not from murine organoids (p 0.29); the same under both zero-lag readings and both recording lengths.")
U["fig7d-murine-organoids-slices-same-lag"] = dict(assumed=True, notes="Under reading (a), the code's (dropping zero lags), murine organoid lags exceed slice lags (0.31 log10 units, p 0.045); with zero lags set to 1 ms, p 0.07; under the second recording length with zero lags dropped, p 0.013. Slices against primary cultures differ under every reading (p 0.008, 0.006 and 0.029) where the paper has 0.53. The readings of zero lags disagree on the first contrast; the code's is adopted, and the second contrast fails under all.",
add_dev=["Assumption. Zero lags are dropped (reading a), because the code's lag table (Processed_data/Figure7/lag_data.xlsx at e9a79c4) holds no zero lag; setting them to 1 ms is shown."])
U["fig7e-pca-backbone-variance"] = dict(notes="Backbone above non-rigid in human organoids (0.188, p 1e-6) but not murine organoids (-0.040, p 0.25); against all units, human organoids again (p 1e-6), murine not (p 0.24), primary cultures p 0.053; the same pattern under the second recording length. Human organoid backbone units exceed slice (p 0.014) and primary (p 8e-4) ones; murine organoid ones do not.")
U["fig7f-hmm-dimensionality"] = dict(notes="Mean dimensionality at theta 0.75 is 1.73 in primary cultures against 2.85 in human (p 3.5e-6) and 2.59 in murine organoids (p 0.005). Human organoids and slices do not differ (p 0.60).")
U["supp24c-nonrigid-more-variable"] = dict(notes="Non-rigid CV2 exceeds backbone CV2 in every model type, raw (p 1e-6 to 5e-39) and z-scored to the shuffles (p 0.018 to 3e-53), at both slice thresholds and both recording lengths.")
U["supp24d-backbone-non-poisson"] = dict(notes="Median fraction of non-Poisson states is 0 or 0.001 for non-rigid units and 0.013 to 0.262 for backbone units in every model type; backbone minus non-rigid 0.21 in the mixed model.")
U["supp10b-rank-order-by-model"] = dict(outcome="reproduced", assumed=True, drop=["blocked_by"], notes="With z-scored rank-order correlations the model type matters (F 3.57 on 3 and 20.9 df, p 0.032) and human organoids exceed primary cultures (1.53, t 2.31 on 20.9 df, p 0.031), both weaker than the paper's P 0.004 and 0.0004. With the ratio normalisation neither (p 0.66 and 0.49), but the ratio is not usable on signed correlations centred on 0 (ed4d-gabazine-rank-order). Under the second recording length (5 shuffles) the z-scored contrasts are not significant (p 0.064 and 0.099), so the outcome also rests on the code's lengths. The question to the authors is the one of ed4d.",
add_dev=["Assumption. z-score normalisation, as for ed4d-gabazine-rank-order.", "Assumption. The code's recording lengths (KEEP_DURATION), used for every claim; under the second reading of the length the result is not significant.", "Main effect as an F test on 3 and the smallest Satterthwaite df of the three contrasts with primary cultures."])
U["supp26-state-traversal"] = dict(outcome="partially_reproduced", notes="Primary cultures traverse more states per second than human organoids (19.8, p 9e-5), and human and murine organoids do not differ (4.5, p 0.35), but primary cultures exceed slices by 8.8 with p 0.056, not below 0.05. Primary cultures also exceed murine organoids (p 2.5e-5), where the paper reports P 0.064. p-values are not Tukey-adjusted; an adjustment would only raise them. In round 1 the slice contrast was p 0.0095 with Wald z; it is above 0.05 with Satterthwaite t, as lmerTest would give.")
U["ed2d-alam-el-din-rates"] = dict(notes="Backbone units fire faster in HO1 to HO4 (0.72 log10 units, p 2e-50) and also in HO5 to HO8 (0.12, p 0.0019), where the paper finds P 0.40.")
U["ed2e-alam-el-din-b2b"] = dict(notes="Normalised burst-to-burst correlations are higher for backbone units in HO1 to HO4 (0.040, p 0.005) and HO5 to HO8 (0.119, p 1e-8).")
U["ed2f-backbone-pairs-above-zero"] = dict(notes="Backbone pairs are above 0 in both sets (0.148, p 0.010 and 0.185, p 0.041) and non-rigid pairs are not; mixed pairs are also above 0 in HO1 to HO4 (0.087, p 0.048), where the paper finds P 0.145.")
U["supp27-d2-near-critical"] = dict(outcome="partially_reproduced", assumed=True, drop=["blocked_by"], notebook=NB, output="claim:supp27-d2-near-critical", measured=[0, 5, 0, 1],
notes="Shuffling raises d2 in every recording; intact mean 0.044 (0.014 to 0.099), shuffled 0.221 (0.199 to 0.251), Welch t 38.3, p 5e-38. All 31 intact recordings have d2 at most 0.1, so the kept recordings do under any selection. The numbers passing the AR fit check differ from the paper's 3, 7, 4 and 7 (HO, MO, MS, PR): 0, 5, 0 and 1 when every log-binned density and spectrum ratio must be within one order of magnitude (measured), 7, 9, 3 and 8 when their median must be. The criterion's partial outcome applies (test holds, counts differ). How the fit check compared the distributions is asked of the authors.",
add_dev=["d2 from a Python port of the code of Sooter et al. (figshare article 25927081, version 1; myYuleWalker.m, myAutocorr.m, getFixedPointDistance.m, getAvalanches.m), one window per recording at the code's lengths, one per-unit shuffle per recording.",
"Assumption. The AR fit check is read as the largest (i) or the median (ii) absolute log10 ratio between the data's and a simulated AR series' avalanche size and duration densities (15 logarithmic bins, avalanche threshold at the 10% quantile as test.m) and Welch spectra (30 s segments; the code's 200 s window is longer than the 180 s recordings), at most 1. The paper says only that preparations were excluded when the distributions deviated by more than one order of magnitude."])
U["supp5-murine-organoid-forebrain-identity"] = dict()
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  grep -n "Wald\|10 shuffles per recording\|K = 10, 12" attempts/van-der-molen-2025-01.yaml
```

```
94:  - Mixed models fitted by REML with a random intercept, tested with Wald z, where the paper uses
178:  - 10 shuffles per recording, where the paper uses 100.
254:  - K = 10, 12, ..., 30 (11 models per recording) in place of every K from 10 to 30, at most 300 EM
379:    intercept; K = 10, 12, ..., 30.
```

**Agent**

Now the verification round and the apply script.

**Agent calls Bash**

```bash
cat > $TMPDIR/rec/ver.py <<'PYEOF'
# (claim, agrees, verifier outcome or None, reason (verifier's words), response)
V = [
("methods-burst-count", True, "reproduced", "Cell 11: the mean is 35.7, inside 38 ± 4. The SE is 6.2 against the paper's 4, and the agreement is fragile: four murine organoids have 0 bursts, offset by MO1 (113) and MO7 (156). Duplicate bursts from detect_bursts could change it (problem 1).",
 "Overlapping bursts (a peak in the tail of a longer burst) are now merged, keeping the higher peak; 35 bursts in 13 recordings were dropped, none in HO1 to HO4 or the murine organoids without bursts. The data check prints the counts with 700, 800 and 2000 ms and the overlaps dropped. Mean 34.8 (SE 6.3), still within tolerance; 29.5 with 2000 ms for every recording. The notes say the agreement rests on MO1 and MO7. Outcome unchanged."),
("fig1c-example-burst-count", True, "reproduced", "Cell 13: HO1 has 46 bursts at both 700 and 800 ms.", "No change; HO1 has no overlapping burst."),
("ed1c-lognormal-rates", True, "reproduced", "Cell 16, reading (a) with all units: all-unit R² is 0.949 and backbone R² is 0.487 (7 fits, because HO7 has no backbone unit). Both are within tolerance.", "No change."),
("fig1d-burst-duration", True, "reproduced", "Cell 18: HO1 to HO4 medians are 472 to 892 ms.", "No change; the medians of HO5 to HO8 changed with the merged bursts and the notes say so."),
("fig1e-peaks-near-burst-peak", False, "blocked", "Cell 20: 15 of 16 reading combinations pass. HO4 pooled at 50 ms gives 0.481, so the readings disagree (blocked, methods_underspecified).",
 "Kept as partially reproduced, with the disagreement recorded. The criterion names the four readings and requires the claim to hold under every one; they are not alternatives between which the paper leaves a choice, so a failure under one is a partial result, not an underspecified method."),
("fig2-backbone-fraction", True, "reproduced", "Cell 22, reading (b) (units with at least 30 spikes): mean 0.331, SD 0.150, both within tolerance. Under reading (a) the SD of 0.166 is outside tolerance.", "No change."),
("fig2e-b2b-correlation", True, "reproduced", "Cell 24: p 5.9e-36 (30% rule) and 1.5e-19 (70% rule). The test used 216 units. The 507 printed is all sorted units, which is a different quantity (problem 10: the exact match suggests the paper's tests included all units; that reading was not run). The 30-spike rule counts only spikes inside the cut burst neighbourhoods (problem 8).",
 "The 30-spike rule now counts spikes over the whole recording, and the tests use Satterthwaite t (p 3e-27 and 9e-16). Burst-to-burst correlations exist only for units active in bursts, so a test over all 507 units cannot be run; the notes say so. Outcome unchanged."),
("fig2g-variance-latency", True, "reproduced", "Cell 26: positive slope, p 3.6e-4 under reading (a) and 4.5e-5 under (b).", "Numbers updated (Satterthwaite t, p 6e-4 and 1e-4). Outcome unchanged."),
("ed3f-burst-cluster-variability", True, "reproduced", "Cell 28: non-rigid CV is higher under all four readings, p ≤ 5e-48.", "Numbers updated after the merged bursts (p 6e-40 to 2e-84). Outcome unchanged."),
("ed4b-gabazine-more-bursts", True, "reproduced", "Cell 32: +7.0 bursts per minute, p 5.5e-6. There are 4 paired organoids (MO12 has no baseline sorted file).", "With Satterthwaite t the mixed-model p is 0.011 (5 organoids); the paired t-test gives 0.021. Outcome unchanged."),
("ed4b-nbqx-cpp-abolish-bursts", True, "reproduced", "Cell 34: treated recordings have 0, 0, 1, 0 and 0 bursts; p 3e-53.", "p is 9e-7 with Satterthwaite t. Outcome unchanged."),
("ed4c-gabazine-participation", True, "reproduced", "Cell 36: +0.138, p 9e-4 pooled; the matched variant gives p 1e-8. The matched variant leaves out MO13 without saying why.", "The conclusion and notes now say why MO12 (no baseline) and MO13 (unit positions differ between conditions) are left out of the matched variant. Outcome unchanged."),
("ed4d-gabazine-rank-order", True, "blocked", "Cell 38: the z-score reading gives gabazine higher, p ≈ 0. The (A−B)/(A+B) reading gives −1.14, p 0.6. That reading is degenerate here (problem 6: normalize is applied to signed Spearman correlations; because B ≈ 0, the ratio is about 1 for most pairs and explodes when A ≈ −B; the notebook does not flag it).",
 "The notebook now prints the degeneracy: the shuffle means are centred on 0 (5th to 95th percentile -0.12 to 0.13), A + B changes sign for 8.8% of burst pairs, and the ratio runs from -86,000 to 3,200. As the verifier finds the ratio reading gives no information, the legend's z-score is adopted as an assumption, and the outcome changes from blocked to reproduced (assumed); the question to the authors stays."),
("supp2a-backbone-fraction-declines", True, "partially_reproduced", "Cell 40: holds for the human organoids under both readings. The archive holds no murine longitudinal recordings (every MO subject is P45D), so the murine half is missing data.", "No change."),
("supp2c-b2b-increases-with-age", True, "partially_reproduced", "Cell 41, human organoids: age effect p 3.4e-8 (with unit type) and 4.8e-6 (with organoid); the paper gives 4.14e-6. Means rise with age, and backbone exceeds non-rigid at every age. The murine half is missing data.", "Numbers updated (p 2e-8 and 3e-6). Outcome unchanged."),
("supp8-backbone-stable-4h", False, None, "The notebook's reason does not hold. In the archive, HO2's 8M and 8M_4H files have 90 units each with identical x_pos/y_pos in the same order. HO3's 4H file equals its 0H file once its unit 24 is dropped. Units are therefore linked. Both recordings were already analysed in L (cell 40), so the test needed only the backbone cross-table and a cross-recording burst-to-burst correlation (problem 2). No outcome.",
 "Tested. Units are linked by walking both ordered position lists (all 90 HO2 and 116 HO3 units link; HO3's 4 h unit 24 is left out), stated as an assumption, with each recording's own result. The cross-table and a cross-recording burst-to-burst correlation (sequences.cross_burst_to_burst) give the criterion in both organoids, so the outcome changes from blocked to reproduced (assumed). The identifier_missing finding is revised."),
("ed5-shuffle-reduces-b2b", True, "reproduced", "Cell 43: (a) p 8.6e-26; (b) one-sided p 0.0072. This uses 10 shuffles, not 100. ed5 fits separate unit and organoid intercepts where the claim asks for both together.",
 "Numbers updated ((a) p 1e-26, (b) one-sided p 0.014). The deviation now states that the two intercepts are fitted one at a time. Outcome unchanged."),
("fig3e-pairwise-correlation", True, "reproduced", "Cell 45: bb−mix and bb−nr p ≈ 0.", "No change."),
("fig3f-backbone-pairs-in-tail", False, "blocked", "Cell 47: above the 75th percentile in all four organoids. At the 90th, HO3 fails (87th percentile) (blocked, methods_underspecified).",
 "Kept as partially reproduced, with the disagreement recorded. The criterion requires both readings to hold, so a failure under one is a partial result, not an underspecified method."),
("fig4c-similarity-variance", True, "reproduced", "Cell 51: in HO1, inside < outside under both readings, and in all of HO1 to HO8.", "No change."),
("fig4d-burst-similarity", True, "reproduced", "Cell 53: HO1 is significant at 100% of frames against both comparisons. HO8 is not (67% and 21%), but HO8 is only reported.", "HO8 is now 67% and 45%. Outcome unchanged."),
("fig4e-similarity-rises-at-backbone-onset", True, "partially_reproduced", "Cell 55: holds in 7 of 8. HO7 has no backbone period. HO8 is marginal (0.329 against 0.326).", "HO8 is now 0.334 against 0.323; HO7 still has no backbone unit. Outcome unchanged."),
("supp13-top-correlated-units-similarity", True, "reproduced", "Cell 57: top 20% higher and bottom 20% lower at 100% of frames.", "No change."),
("fig4f-pca-variance", True, "partially_reproduced", "Cell 59: HO1 backbone is 75.4% (inside tolerance) but non-rigid is 17.4%, outside 25 ± 2.5. No organoid matches both. The across-organoid ordering holds in all 7 testable organoids; HO7 cannot be tested. The non-rigid 17.4% may come from the notebook's zeroing between bursts.",
 "Added the PCA on the code's burst-only rates, which hold the inverse ISI across the gaps: HO1 gives 75.1% and 15.3%, and no organoid matches both, so the zeroing does not explain the difference. Outcome unchanged."),
("supp18-hmm-likelihood-real-above-shuffled", True, "reproduced", "HMM notebook cell 6: real data beat the surrogate in 120/120 and 40/40 combinations. The real and surrogate data are scored differently, in a way that favours real (problem 3: the surrogate is scored as the marginal likelihood of the held-out entries alone; on synthetic data this alone favours the conditional score by about 0.005 nats per entry; the smallest margin observed is 0.009; the surrogate should be scored as loglik(S) − loglik(S, train)). Not secure.",
 "The surrogate is now scored as loglik(S) - loglik(S, train), as the real data. Real beats surrogate in 120 of 120 and 40 of 40 combinations, smallest margin 0.015 nats per entry; every fold's margin is printed, and so is the old scoring (0.008 lower on average). Outcome unchanged."),
("fig5c-states-converge-at-peak", True, "not_reproduced", "HMM notebook cell 8: 1 of 8 organoids meets reading (a) and 4 of 8 meet (b); 6 are needed. A custom EM fit in place of SSM could bear on fig5c, which hinges on the very low entropy far from bursts in HO3 and HO4.",
 "Now 1 and 3 of 8 (HO5 moved with the merged bursts). The notes say the low entropy at the window's start in HO3 and HO4 drives the result. SSM could not be installed in a locked environment, so the EM stays a deviation. Outcome unchanged."),
("fig5d-backbone-more-states", True, "reproduced", "HMM notebook cell 11: both readings p ≈ 0. K is a fixed effect, where the claim asks for a random intercept.", "No change; the deviation was already recorded."),
("fig5f-svm-states-beat-rate", False, "not_reproduced", "HMM notebook cell 12: rate accuracy 73.9% is just outside 63.2 ± 10.4. The paired test gives p 0.081, and the per-organoid test is significant in only 4 of 7. No chance level is reported; for HO5 and HO8 the rate-only accuracies (0.497 and 0.429) are below the majority-class rate (0.565 and 0.60).",
 "Changed from partially reproduced to not reproduced: the criterion defines no partial outcome, and both its comparison of states with rate and the rate mean fail. The majority-class rate per organoid is now printed (mean 70.6%)."),
("fig6f-slice-b2b-correlation", True, "reproduced", "Cell 61: p ≤ 2.4e-9 under all four readings. The expected n is units in the test (problem 10).", "Also run under the second recording length (p below 1e-33). Outcome unchanged."),
("fig6g-slice-pairwise-correlation", True, "reproduced", "Cell 62: all contrasts p ≈ 0.", "Also run under the second recording length. Outcome unchanged."),
("fig7a-backbone-higher-rate", True, "reproduced", "Cell 66: all four model types p ≤ 2e-31. The murine organoid set is 5 of 9 recordings. Human organoids give 699 tested units and 930 sorted in the whole dandiset, below the paper's 1048 (problem 13).", "Also run under the second recording length (p below 1e-28). The notes say the dandiset holds fewer human organoid units than the legend counts. Outcome unchanged."),
("fig7a-primary-higher-rate", True, "partially_reproduced", "Cell 67: 5 of 6 contrasts hold; PR−MO backbone gives p 0.66.", "No change; also 0.20 under the second recording length."),
("fig7b-normalized-b2b", True, "partially_reproduced", "Cell 69: the within-type contrasts hold in HO, MO and MS. Backbone units of these types are not above primary-culture backbone units (p 0.11, 0.41, 0.22).",
 "Changed to not reproduced. After the merged bursts, the whole-recording 30-spike rule and the Satterthwaite tests, the murine organoid within-type contrast is p 0.11 (0.84 under the second recording length), so the criterion's partial outcome, which needs all three within-type contrasts, no longer holds."),
("fig7b-primary-no-b2b-difference", True, "reproduced", "Cell 70: p 0.76.", "Now p 0.81. Outcome unchanged."),
("fig7c-normalized-pairwise", True, "reproduced", "Cell 73: HO p 1.7e-4, MO p 6.6e-6.", "With Satterthwaite t, p 0.001 and 2e-4; the same under the second recording length. Outcome unchanged."),
("fig7c-slices-primaries-no-pair-difference", True, "reproduced", "Cell 74: MS p 0.24/0.27 and PR p 0.46/0.49. fig7c MS (one-sided p 0.043) is a borderline result that would likely move with Satterthwaite t (problem 7).", "Now MS p 0.29 and 0.20, PR p 0.47; 0.24 to 0.51 under the second recording length. Outcome unchanged."),
("fig7c-backbone-pairs-above-random", True, "not_reproduced", "Cell 75: MO is not above 0 (p 0.35), and primary cultures are above 0 (p 0.004).", "With Satterthwaite t, MO p 0.36, slices p 0.065, primary cultures p 0.017. Outcome unchanged."),
("fig7d-lag-times", True, "partially_reproduced", "Cells 77–78: HO−PR and MO−PR are larger with p < 1e-6 under both readings. HO−MO is not significant (p 0.28/0.21).", "No change; the same under the second recording length."),
("fig7d-murine-organoids-slices-same-lag", False, "blocked", "Cell 79: MO−MS gives p 0.035 (drop zeros) and 0.059 (zero set to 1 ms). With Satterthwaite-type df it would probably be non-significant under both (problem 7). The secondary contrast, slices against primaries, fails under both readings (p 0.0037/0.0027 against the paper's 0.53). Blocked, methods_underspecified.",
 "Satterthwaite t gives MO-MS p 0.045 (zero lags dropped) and 0.07 (set to 1 ms), and 0.013 under the second recording length; slices against primary cultures p 0.008, 0.006 and 0.029. Kept as not reproduced, now marked assumed: the code's lag table holds no zero lag, so dropping them is the best-supported reading, and the second contrast fails under every reading. The disagreement is recorded."),
("fig7e-pca-backbone-variance", True, "not_reproduced", "Cell 81: the MO contrast fails under both readings (−0.04, p 0.23; +0.03, p 0.23). fig7e reading (b) PR (p 0.046) is borderline (problem 7).", "With Satterthwaite t, MO p 0.25 and 0.24, PR (b) p 0.053; the same under the second recording length. Outcome unchanged."),
("fig7f-hmm-dimensionality", True, "reproduced", "HMM notebook cell 14: PR < HO (p 3e-6) and PR < MO (p 0.0033). This is a GEE, not the paper's GLMM.", "No change."),
("supp24c-nonrigid-more-variable", True, "reproduced", "Cell 83: all four types significant for both raw and z-scored CV2.", "Also under the second recording length. Outcome unchanged."),
("supp24d-backbone-non-poisson", True, "reproduced", "HMM notebook cell 16: backbone median > non-rigid in every type, and non-rigid medians are ≤ 0.001.", "No change."),
("supp10b-rank-order-by-model", True, "blocked", "Cell 85: the ratio reading gives main effect p 0.65 and HO−PR p 0.45; the z reading gives p 0.015 and 0.033. The z-reading HO−PR p would likely pass 0.05 with t-tests (problem 7), which would make this not_reproduced.",
 "With Satterthwaite t the z reading gives main effect F p 0.032 and HO-PR p 0.031 (t 2.31 on 20.9 df), still below 0.05. With the ratio reading set aside as degenerate (ed4d), the z-score is adopted and the outcome changes from blocked to reproduced (assumed). Under the second recording length the z contrasts are p 0.064 and 0.099, so the outcome also rests on the code's lengths; the notes say so."),
("supp26-state-traversal", True, "reproduced", "HMM notebook cell 18: PR > HO (p 3e-6), PR > MS (p 0.0095), HO vs MO p 0.37.",
 "With Satterthwaite t, the test the verifier asked for borderline contrasts, PR > MS is p 0.056, so the outcome changes from reproduced to partially reproduced (PR > HO p 9e-5 and HO against MO p 0.35 still hold)."),
("supp27-d2-near-critical", False, "blocked", "The notebook gives no reason; the attempt record is not available to me. The spike matrices for all 31 recordings are in the archive, so the intact-against-shuffled Welch test of d2 was testable. Only the AR fit-check counts are underspecified (blocked, methods_underspecified, counts only).",
 "Tested. The d2 code of Sooter et al. (figshare 25927081 v1) is ported to sequences.py; Welch p 5e-38 with every intact d2 at most 0.1. The AR fit check is read two ways (largest or median log ratio within one order of magnitude); the counts (0, 5, 0, 1 and 7, 9, 3, 8) differ from the paper's 3, 7, 4, 7, so the criterion's partial outcome applies, assumed. Outcome changed from blocked to partially reproduced."),
("ed2d-alam-el-din-rates", True, "not_reproduced", "Cell 87: the Alam El Din fit is significant (p 0.0018); the paper has 0.40.", "No change (p 0.0019)."),
("ed2e-alam-el-din-b2b", True, "reproduced", "Cell 88: p 0.0051 and 1.1e-5.", "Numbers updated (p 0.005 and 1e-8). Outcome unchanged."),
("ed2f-backbone-pairs-above-zero", True, "partially_reproduced", "Cell 89: backbone pairs are above 0 in both sets, but Sharf mixed pairs are also above 0 (p 0.0085).", "With Satterthwaite t, Sharf mixed pairs p 0.048 and Alam El Din backbone pairs p 0.041. Outcome unchanged."),
("supp5-murine-organoid-forebrain-identity", True, "blocked", "The data are on GEO, not in the dandiset, which holds electrophysiology only (blocked, data_missing).",
 "Kept as blocked with methods_underspecified. The data are public in GEO (GSE290330), and the protocol blocks a data: elsewhere claim for the reason that applies, never data_missing; the markers that define the identity are not listed in the text."),
]
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec/apply.py <<'PYEOF'
import yaml, sys
sys.path.insert(0, "/tmp/claude-1001/rec")
U = {}
exec(open("/tmp/claude-1001/rec/upd1.py").read())
exec(open("/tmp/claude-1001/rec/upd2.py").read())
exec(open("/tmp/claude-1001/rec/ver.py").read())
P = "attempts/van-der-molen-2025-01.yaml"
a = yaml.safe_load(open(P))
order = ["claim", "outcome", "blocked_by", "assumed", "notebook", "output", "measured", "notes", "deviations", "proposed"]
seen = set()
for o in a["outcomes"]:
    c = o["claim"]; seen.add(c)
    u = U.get(c, {})
    for k in u.get("drop", []):
        o.pop(k, None)
    for k in ("outcome", "notes", "measured", "assumed", "notebook", "output"):
        if k in u:
            o[k] = u[k]
    devs = o.get("deviations", [])
    for prefix, new in u.get("replace_dev", {}).items():
        hits = [i for i, d in enumerate(devs) if d.startswith(prefix)]
        assert len(hits) == 1, (c, prefix); devs[hits[0]] = new
    devs += u.get("add_dev", [])
    if devs:
        o["deviations"] = devs
    o2 = {k: o[k] for k in order if k in o}
    assert set(o2) == set(o), (c, set(o) - set(o2))
    o.clear(); o.update(o2)
assert seen >= set(U), set(U) - seen
# the supp27 notes from round 1 no longer apply: rewritten above; supp5 unchanged
fx = a["findings"]
fx[0]["statement"] = ("Burst detection parameters for the murine organoids are not given. With the stated detection (4 x RMS of "
    "the 20 ms and 100 ms smoothed population rate) MO2, MO4, MO5 and MO6 have no burst and MO3 has four: their highest "
    "peaks reach only 3.0 to 3.7 times the RMS, because their rate between bursts is high (median smoothed population rate "
    "0.47 to 1.07 spikes per ms), yet the paper's code lists backbone units for all nine. Question for the authors, which "
    "threshold, peak distance and recording length were used for each murine organoid, and for which recordings the "
    "minimum peak distance was raised towards 2000 ms (35 overlapping bursts in 13 recordings here, a peak in the tail of a "
    "longer burst, are merged in its place).")
fx[3]["statement"] = ("Units have positions but no identifier linking them across recordings of one organoid (0 h and 4 h, "
    "Supplementary Fig. 8; drug conditions, Extended Data Fig. 4). The ordered unit positions are identical for HO2 at 0 h "
    "and 4 h (90 units), for HO3 once the 4 h file's unit 24 is left out (116 units), and for MO10, MO11 and MO14 across "
    "conditions, which is consistent with joint sorting, but not for MO12 or MO13. Positions alone are not unique (61 "
    "distinct positions for 90 HO2 units).")
fx.append(dict(kind="methods_unavailable", statement=("Question for the authors on the AR fit check of the d2 analysis "
    "(Supplementary Methods, d2 calculation; Supplementary Fig. 27). Preparations were excluded when the AR model's "
    "avalanche size and duration distributions or power spectrum deviated from the data's by more than one order of "
    "magnitude, but the comparison is not given (which bins, the largest or a typical deviation, the spectral window; the "
    "code's 200 s Welch window is longer than the 180 s recordings). Two readings here keep 0, 5, 0 and 1 or 7, 9, 3 and 8 "
    "recordings of HO, MO, MS and PR, against the paper's 3, 7, 4 and 7.")))
a["inputs"] = [dict(what=("The d2 code of Sooter et al. that the paper's r_download.sh fetches (myYuleWalker.m, myAutocorr.m, "
    "getFixedPointDistance.m, getAvalanches.m, getARstats.m, simAR.m), read and ported to sequences.py for "
    "supp27-d2-near-critical; no data from it are used."), source="https://figshare.com/articles/software/d_beta_code_repository/25927081/1")]
a["verifications"] = [dict(date="2026-11-17", kind="agent",
    by="Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
    reviewed=("Round 1. The first executed notebooks (reproduce_van_der_molen_2025.ipynb and hmm_van_der_molen_2025.ipynb) "
              "with the conclusion cells and the summaries removed, the helper modules sequences.py and hmm.py, and the "
              "claims file, with the paper's full text. The verifier read the archive's assets and units tables and tested "
              "detect_bursts, burst_segments_compressed and the HMM scoring on synthetic inputs. It had no attempt record."),
    results=[dict(claim=c, agrees=ag, **({"outcome": oc} if oc else {}), reason=r, response=resp) for c, ag, oc, r, resp in V])]
assert {r["claim"] for r in a["verifications"][0]["results"]} == {o["claim"] for o in a["outcomes"]}
keys = list(a.keys())
top = ["schema_version", "id", "datasets", "paper", "date", "entry", "provenance", "inputs", "outcomes", "findings", "verifications"]
a = {k: a[k] for k in top + [k for k in keys if k not in top] if k in a}
class D(yaml.SafeDumper):
    def ignore_aliases(self, data): return True
yaml.dump(a, open(P, "w"), Dumper=D, sort_keys=False, width=100, allow_unicode=True)
print("written")
PYEOF
cd  cp attempts/van-der-molen-2025-01.yaml $TMPDIR/rec/backup.yaml; python3 $TMPDIR/rec/apply.py && head -40 attempts/van-der-molen-2025-01.yaml
```

```
written
schema_version: 3
id: van-der-molen-2025-01
datasets:
- archive: dandi
  id: '001603'
  version: 0.260923.0623
  doi: 10.48324/dandi.001603/0.260923.0623
  relation: primary
paper: doi:10.1038/s41593-025-02111-0
date: 2026-11-17
entry: van-der-molen-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 tools/entry.py check entries/van-der-molen-2025 2>&1 | tail; ls tools | grep -i valid; grep -n "def main\|add_parser\|subparsers" tools/entry.py | head -20
```

```
0 error(s)
644:def main() -> int:
```

**Agent calls Bash**

```bash
cd  sed -n 644,700p tools/entry.py | grep -n "\"" | head -20; ls tests | head; python3 -c "
import json,yaml,jsonschema
s=json.load(open('schemas/attempt.schema.json')); a=yaml.safe_load(open('attempts/van-der-molen-2025-01.yaml'))
import datetime
def fix(x):
    if isinstance(x,dict): return {k:fix(v) for k,v in x.items()}
    if isinstance(x,list): return [fix(v) for v in x]
    if isinstance(x,(datetime.date,)): return x.isoformat()
    return x
jsonschema.validate(fix(a),s); print('schema ok')"
```

```
4:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python", "hash"])
5:    parser.add_argument("entry", type=Path, nargs="+",
6:                        help="the entry directory, e.g. entries/000582-sargolini-2006; `check` takes several")
7:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
8:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
9:    parser.add_argument("--max-minutes", type=float, default=60,
10:                        help="a notebook that takes longer than this fails")
11:    parser.add_argument("--fresh", action="store_true",
12:                        help="run: execute even when the executed copies were made from the entry as it is now")
13:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
14:                                         "upgrade-python: the version to move to")
15:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
16:                                                    "(default: executed/<entry>)")
19:    if args.command == "check" and len(args.entry) > 1:
24:            if not (entry_dir / "entry.yaml").is_file():
25:                parser.error(f"{entry} has no entry.yaml")
27:            print(f"{entry_dir.name}: {len(report.errors)} error(s)")
29:                print(f"  error: {line}")
31:        print(f"{failed} of {len(args.entry)} entries with errors")
34:        parser.error(f"{args.command} takes one entry")
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rln "attempt.schema" tools/ encore_science/ scripts/ 2>/dev/null | head; date -u
```

```
tools/build_site.py
Tue Nov 17 19:42:25 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -n "def validate\|def check_attempt\|def load_attempts" tools/build_site.py | head; grep -n "argparse\|add_argument" tools/build_site.py | head
```

```
36:import argparse
4070:    parser = argparse.ArgumentParser(description=__doc__,
4071:                                     formatter_class=argparse.RawDescriptionHelpFormatter)
4072:    parser.add_argument("--output", type=Path, default=ROOT / "site")
4073:    parser.add_argument("--demo", type=int, metavar="N",
4075:    parser.add_argument("--issues", type=Path, metavar="JSON",
4077:    parser.add_argument("--queue", type=Path, metavar="JSON",
4079:    parser.add_argument("--responses", type=Path, metavar="JSON",
4081:    parser.add_argument("--noindex", action="store_true",
4083:    parser.add_argument("--notebooks-from", metavar="URL",
```

**Agent calls Bash**

```bash
cd  timeout 600 python3 tools/build_site.py --output $TMPDIR/site 2>&1 | grep -i -E "molen|error|invalid|warn" | head -10; echo exit $?
```

```
exit 0
```

**Agent calls Bash**

```bash
cd  date -u; python3 tools/entry.py all entries/van-der-molen-2025 2>&1 | tail -5; date -u
```

```
Tue Nov 17 19:42:38 UTC 2026
Installed kernelspec registry-van-der-molen-2025 in executed/van-der-molen-2025/.venv/share/jupyter/kernels/registry-van-der-molen-2025
0 error(s)
pass  reproduce_van_der_molen_2025.ipynb  (1753 s)
pass  hmm_van_der_molen_2025.ipynb  (1057 s)
Tue Nov 17 20:29:35 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/van-der-molen-2025; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py reproduce_van_der_molen_2025.ipynb $TMPDIR/out/main_final2.txt; $TMPDIR/venv/bin/python $TMPDIR/dev/dump.py hmm_van_der_molen_2025.ipynb $TMPDIR/out/hmm_final2.txt; diff <(grep -v "ran in\|analysed .* in\|fitted .* in" $TMPDIR/out/main_final.txt) <(grep -v "ran in\|analysed .* in\|fitted .* in" $TMPDIR/out/main_final2.txt) | grep -v "^[<>] ##### MD\|^---\|^[0-9,c]*$" | head; diff <(grep -v "ran in\|fitted .* in" $TMPDIR/out/hmm_final.txt) <(grep -v "ran in\|fitted .* in" $TMPDIR/out/hmm_final2.txt) | grep -v "^[<>] ##### MD\|^---\|^[0-9,c]*$" | head; ls -la; git -C  status --short | head -20
```

```
total 300
drwxr-xr-x 4 runner runner   4096 Nov 17 20:29 .
drwxr-xr-x 3 runner runner   4096 Nov 17 17:54 ..
drwxr-xr-x 3 runner runner   4096 Nov 17 19:39 .claude
-rw-r--r-- 1 runner runner    502 Nov 17 20:29 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 17 19:42 .venv
-rw-r--r-- 1 runner runner  43275 Nov 17 20:29 hmm_van_der_molen_2025.ipynb
-rw-r--r-- 1 runner runner 235664 Nov 17 20:11 reproduce_van_der_molen_2025.ipynb
-rw-r--r-- 1 runner runner    293 Nov 17 20:29 result.json
 M attempts/van-der-molen-2025-01.yaml
 M entries/van-der-molen-2025/README.md
 M entries/van-der-molen-2025/entry.yaml
 M entries/van-der-molen-2025/hmm_van_der_molen_2025.ipynb
 M entries/van-der-molen-2025/reproduce_van_der_molen_2025.ipynb
 M entries/van-der-molen-2025/sequences.py
 M tools/agent_run.py
 M tools/backfill_summaries.py
 M tools/build_site.py
 M tools/entry.py
 M tools/get_papers.sh
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 tools/entry.py check entries/van-der-molen-2025 | tail -2; git diff --stat -- attempts entries | tail -3; date -u
```

```
0 error(s)
 .../reproduce_van_der_molen_2025.ipynb             | 679 +++++++++++++---
 entries/van-der-molen-2025/sequences.py            | 358 +++++++--
 6 files changed, 1582 insertions(+), 420 deletions(-)
Tue Nov 17 20:29:49 UTC 2026
```

**Agent**

I've addressed the round-1 report and re-run the entry with `tools/entry.py all`. Both notebooks pass (29 and 18 minutes), the two clean runs printed the same numbers, the entry check shows 0 errors, and the record matches the attempt schema. The round is recorded under `verifications` with each claim's agreement, the verifier's outcome and reason, and my response. Nothing is committed.

**Outcome changes** (now 31 reproduced, 11 partially reproduced, 7 not reproduced, 1 blocked; before, 29, 11, 5 and 5):
- **ed4d** (blocked → reproduced, resting on an assumption): the (A−B)/(A+B) normalisation can't be used on signed shuffle correlations centred on 0. The sum A+B changes sign for 8.8% of burst pairs and the ratio runs from −86,000 to 3,200. I adopted the legend's z-score.
- **supp10b** (blocked → reproduced, assumed): with the z-score and Satterthwaite t, the main effect is p 0.032 and human organoids against primary cultures p 0.031. Under the second reading of the recording length both are no longer significant (p 0.064 and 0.099), so it also rests on the code's recording lengths.
- **supp8** (blocked → reproduced, assumed): units are linked by their identical positions taken in order. Every 0 h unit links (HO3's extra 4 h unit is left out), and the criterion holds in both organoids.
- **supp27** (blocked → partially reproduced, assumed): I ported the d2 code from the figshare article the paper uses. Shuffling raises d2, Welch p 5e-38, and every intact d2 is at most 0.1. How many recordings pass the AR fit check depends on how "one order of magnitude" is read: 0/5/0/1 or 7/9/3/8, against the paper's 3/7/4/7.
- **fig5f** (partially → not reproduced): the criterion defines no partial outcome, and the comparison of state features with firing rate fails.
- **fig7b-normalized-b2b** (partially → not reproduced): the murine within-type contrast is now p 0.11, so the criterion's partial outcome no longer holds.
- **supp26** (reproduced → partially reproduced): with Satterthwaite t, primary cultures against slices is p 0.056.

**Fixes and added outputs:**
- **Duplicate bursts:** overlapping bursts are merged, keeping the higher peak. This dropped 35 bursts in 13 recordings, none in HO1 to HO4. Burst counts at 2000 ms are shown as a variant.
- **Mixed models:** they now use Satterthwaite t, as lmerTest does. I checked this against an exact balanced case (df 8, same p as a t-test).
- **Recording length:** the second reading (the shortest segment holding about 40 bursts) is now run for Figs. 6 and 7 and Supplementary Figs. 10B and 24C.
- **HMM scoring:** the surrogate is scored the same way as the real data. Real still beats surrogate in all 120 and all 40 combinations, smallest margin 0.015, with every fold printed.
- **Other outputs the verifier asked for:**
  - Burst thresholds for the murine organoids without bursts: their highest peaks reach only 3.0 to 3.7 times the RMS.
  - Okun swaps done against requested: all complete.
  - PCA on the code's own burst-only rates: HO1 non-rigid is 15.3%, still outside the expected range.
  - The majority-class chance level for fig5f.
  - Why MO13 is left out of the ed4c variant.
  - Corrected helper docstrings.
- **Record:** findings revised and one new methods question for the authors on the d2 fit check; the figshare d2 code is listed under `inputs`.

**Disagreements kept, with reasons in the record:**
- **fig1e and fig3f** stay partially reproduced, not blocked: the criterion requires every reading, so a failure under one is a partial result.
- **fig7d-murine-organoids-slices-same-lag** stays not reproduced (now assumed): the code's lag table has no zero lags, so dropping them is the best-supported reading, and the slices-against-primary-cultures contrast fails under every reading.
- **supp5** stays blocked as `methods_underspecified`, not `data_missing`: the data are public in GEO, and the protocol does not allow `data_missing` for such claims.

**Not done:**
- I added no reader questions to `questions/`, because the report names no place where the claims file misreads the paper. Its note that the paper's n counts all units is recorded in the notes; a test over all units can't be run because burst-to-burst correlations exist only for units active in bursts.
- These stay as recorded deviations: SSM (replaced by the entry's own EM), 100 shuffles (10 used), every K from 10 to 30 (11 values used), and K as a random intercept in fig5d.

## End of run

113 turns, 155 minutes, $9.31 at API prices, result: success.
