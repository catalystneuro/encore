# 000055 · author-revise-1 · run 42345958238

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000055/verifier-1-report.md; ls entries/000055-peterson-2021 entries/000055-peterson-2021/*
```

```
Sat Nov  7 06:19:05 UTC 2026
**A. Outcomes** (all 25 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| subject-days | reproduced | All 12 subjects have exactly the Table 2 days, 55 subject-days (cell 23). |
| roi-projection-link | reproduced | Rows match electrodes for 12 of 12 subjects. The top weight is at the nearest centroid for 0.59 to 0.79 of electrodes, against about 0.2 when the order is shuffled (12 of 12). The eight regions with density > 3 are the ones the claims file names (cell 25). |
| cohort | partially_reproduced | 12 subjects, surface mean 84.8 (87.0 ± 12.9), depth mean 23.7 (23.2 ± 12.1) and 5 right hemisphere all pass. Subjects with depth electrodes is 7 against an exact 5, so that part fails. Sex and age are not in the files or the archive metadata (I checked the asset metadata), so they are not testable (cell 27). |
| fig2-event-counts | not_reproduced | Reading a gives fewest 211, most 996, median 770.5. Reading b gives 211, 979, 739. The fewest and the median are outside tolerance under both readings (cell 29). Reading b could not drop the false positives (see B3). |
| fig2-features-differ-across-subjects | reproduced | All ten Kruskal-Wallis p < 0.001 under both readings; the largest is 1e-34 (cell 31). |
| fig2-reach-shape | partially_reproduced | The duration and magnitude part holds pooled and in 12 of 12 subjects. The angle part holds in 0 of 12 subjects and not pooled: peaks are near ±70° (cell 33). See B2: the criterion's angle test is biased against this claim. |
| fig2-bimanual-skew | reproduced | The ratio, overlap and class parts hold pooled and in 12 of 12 subjects. S02, S04 and S05 are among both "five" sets, under both readings (cell 36). |
| extfig2-1c-contralateral-larger | reproduced | The contralateral peak exceeds the ipsilateral peak in 12 of 12 subjects under both readings. The smallest ratio is 1.08 (S05) (cell 38). |
| extfig2-2-feature-correlations | partially_reproduced | 5 of 6 correlations are 
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
615 docs/protocol.md
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
401:### 4. Lock, check and run
412:### 5. Record the attempt
463:### 6. Hand over for verification
501:## Repeat attempts
543:## Local and remote datasets
566:## Verifier
570:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,500p docs/protocol.md
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

[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep 000055; ls claims/ | grep 000055; ls questions | grep 000055; wc -l attempts/000055*; wc -c entries/000055-peterson-2021/*; ls executed/000055-peterson-2021/ 2>/dev/null
```

```
Exit code 2
000055-peterson-2021-01.yaml
000055
368 attempts/000055-peterson-2021-01.yaml
  2460 entries/000055-peterson-2021/README.md
 23461 entries/000055-peterson-2021/ajile.py
  1007 entries/000055-peterson-2021/entry.yaml
 84166 entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
    81 entries/000055-peterson-2021/requirements.in
  2190 entries/000055-peterson-2021/requirements.lock.txt
113365 total
```

**Agent calls Bash**

```bash
ls claims/000055 questions/ | head; cat attempts/000055-peterson-2021-01.yaml
```

```
claims/000055:
10.1523-eneuro.0007-21.2021.yaml

questions/:
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
schema_version: 2
id: 000055-peterson-2021-01
dataset:
  archive: dandi
  id: "000055"
  version: 0.220127.0436
  doi: 10.48324/dandi.000055/0.220127.0436
paper: doi:10.1523/eneuro.0007-21.2021
date: 2026-11-07
entry: 000055-peterson-2021
[... 358 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/000055; python -c "
import yaml;d=yaml.safe_load(open('10.1523-eneuro.0007-21.2021.yaml'))
print(d.keys())
for c in d['claims']:
  if c['id'].startswith(('fig6','extfig6')) or c['id'] in ('fig2-event-counts','fig3-lfb-more-widespread','fig2-reach-shape'): print(yaml.dump(c,width=120))
"; nproc; free -g
```

```
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
criterion: Which events are counted is not fixed by the text. Readings are (a) all contralateral wrist movement events the
  dataset holds for a subject; (b) those left after dropping events marked false positive and ECoG segments with power below
  0 dB or with 115-125 Hz power more than 3 SD above all segments (Methods, ECoG-event synchronization; the Figure 2 code
  reads its events from the spectral power files, which have these removed). Reproduced when all three values are within tolerance
  under one reading.
expected:
- quantity: fewest events in a subject
  tolerance: 15.1
  value: 151
- quantity: most events in a subject
  tolerance: 94.7
  value: 947
- quantity: median events per subject
  tolerance: 64
  value: 640
id: fig2-event-counts
quote: The total number of events for each subject was between 151 and 947 (median, 640 across subjects).
source: Figure 2 legend
statement: Each subject contributed between 151 and 947 movement events (median 640 across subjects).
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000055/10.1523-eneuro.0007-21.2021.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
" ; head -c 6000 claims/000055/10.1523-eneuro.0007-21.2021.yaml
```

```
{'schema_version': 2, 'dataset': {'archive': 'dandi', 'id': '000055'}, 'paper': 'doi:10.1523/eneuro.0007-21.2021', 'checks': [{'date': datetime.date(2026, 10, 23), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['Read the code at the cited commit (04c6faf) to check every criterion that cites it. The spectral, projection, masking, regression and plotting details in the header and criteria match the code, except as below.', "Header. Added that the code fits models at bad electrodes and keeps them in the Figure 6c-d box plots; the Methods and the Figure 1 legend remove bad electrodes, so good electrodes stay the main result and the code's choice is a variant.", 'fig2-reach-shape. The statement left out the paper\'s "minimal intersubject variability" for duration and magnitude. Added it, and the criterion now says it is read through the 10 of 12 subject rule already there.', 'fig2-bimanual-skew. The paper\'s "less skew for subjects 02, 04, and 05" applies to both ratio and overlap; the criterion judged it on the ratio only. It now uses both features.', "fig4-precentral-subject-variability. Added the code's second subtraction of the -1.5 to -1 s mean from each subject's median (plot_specs_single_region), and said where the 0 to 0.5 s window comes from (the Methods' banded window; Figure 4 fixes none).", 'extfig5-1-baseline-reduces-day-variability. The test for "clear variability remains" (median SD above 0) was always true. It is now judged through the day effects of fig5-recording-day-effects, which the Results give as the variability that remains; added depends_on.', "fig6c-angle-and-day-most-informative and fig6d-upward-reaches-enhance-pattern. Added the code's inclusion of bad electrodes as a variant.", 'fig6d-angle-and-day-largest-coefficients. The criterion took the median of absolute coefficients as the only measure; the paper does not say how magnitude is summarised and its box plots show signed values. Named two readings (median of absolu
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s)); print(s[:300])
"
```

```
===== 0 markdown None 3029
# Reproducing Peterson et al. (2021) from dandiset 000055

**Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural
variability of naturalistic arm movements. *eNeuro* 8(3), ENEURO.0007-21.2021.
[doi:10.1523/ENEURO.0007-21.2021](https://doi.org/10.1523/ENEURO.000
===== 1 code None 405
import os
import time
import warnings

os.environ["OMP_NUM_THREADS"] = "1"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import ajile

pd.set_option("display.width", 220)
[... 446 more lines not kept]
```

**Agent calls Bash**

```bash
cat entry.yaml; ls ../../executed/ 2>/dev/null | head; grep -n "timeout\|3600\|60 \* 60\|parallel\|cpu" ../../tools/entry.py | head -30
```

```
schema_version: 1
name: 000055-peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds 55 days of ECoG and pose from 12 people in clinical epilepsy monitoring, with
  their wrist movement events and event features. It compares the behavioural features across
  subjects and days, the group and per-subject movement-related spectral power in eight cortical
  regions, and the variation of precentral band power across subjects and recording days. The
  regression models of Figure 6 were too large to run here.
license: Apache-2.0
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson et al. (2021) from dandiset 000055
  runtime_minutes: 35
helpers:
- ajile.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 330,470p ../../tools/entry.py
```

```
# --- lock and run -------------------------------------------------------------

def lock(entry_dir: Path) -> int:
    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
                        "requirements.in", "-o", "requirements.lock.txt"], cwd=entry_dir)
    if r.returncode == 0:
        print(f"wrote {(entry_dir / 'requirements.lock.txt').relative_to(ROOT)}")
    return r.returncode


def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cat ajile.py
```

```
"""Loading and measures for AJILE12, dandiset 000055, for Peterson et al. (2021), eNeuro.

Peterson, Singh, Wang, Rao & Brunton (2021), "Behavioral and Neural Variability of Naturalistic
Arm Movements", eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.

Each NWB file holds one subject and one 24 h recording day: preprocessed ECoG at 500 Hz
(`acquisition/ElectricalSeries`, stored in microvolts with a conversion of 1e-6 to volts), the
electrode table (MNI x, y, z, group, `good`, and the paper's regression R2 per electrode), pose
of nine key points at 30 frames per second (`processing/behavior/Position`, in pixels though the
files say meters), the contralateral wrist movement events (`processing/behavior/ReachEvents`)
and their ten features (`intervals/reaches`), and coarse behaviour labels (`intervals/epochs`).
Files are streamed from the archive at the pinned version with remfile and h5py; nothing is
written to disk.

Where the parameters come from:

- The spectral method follows the claims file's opening comment (Methods, "ECoG-event
  synchronization and segmentation", and the paper's code at commit 04c6faf of
  github.com/BruntonUWBio/naturalistic_arm_movements_ecog, config.py and tfr_utils.py):
  10 s segments centred on each event; Morlet power at 1 to 121 Hz in 5 Hz steps with
[... 484 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [2,3,16,17,18,54,61,76,81,82,84]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
Sat Nov  7 06:20:56 UTC 2026
===== 2
started = time.time()
assets = ajile.list_assets()
sessions = ajile.load_sessions(assets)
# LOAD-BEH-END
print(f"{len(sessions)} files of dandiset {ajile.DANDISET_ID} version {ajile.DANDISET_VERSION}, "
      f"{assets.size_gb.sum():.0f} GB in all; metadata, events and wrist traces read in "
      f"{time.time() - started:.0f} s")
===== 3
# One table of events. Time of day from the midnight clock of the files (see the helper).
rows = []
for s in sessions:
    e = s["events"].copy()
    e["subject"], e["day"], e["k"] = s["subject"], s["day"], np.arange(len(e))
    rows.append(e)
ev = pd.concat(rows, ignore_index=True)
ev = ev.rename(columns={"Reach_magnitude_px": "magnitude", "Reach_angle_degrees": "angle_file",
                        "Onset_speed_px_per_sec": "speed", "Speech_ratio": "speech",
                        "Bimanual_ratio": "bimanual_ratio", "Bimanual_overlap": "bimanual_overlap",
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog code55 && cd code55 && git checkout -q 04c6faf2f219586fa834d10c614ef48a694cec55 && ls; grep -n "def \|Huber\|shuffle\|permut" regression_utils.py | head -60
```

```
LICENSE
README.md
compute_power_gen_figs_python
project_data_rois_matlab
upload_figshare.py
grep: regression_utils.py: No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code55/compute_power_gen_figs_python && ls; grep -n "def \|Huber\|shuffle\|permut\|r2_score\|coef_\|n_splits\|train_test" regression_utils.py fit_regression_models.py | head -80
```

```
Behavioral_features_Fig2.ipynb
Plot_banded_power_Fig5.ipynb
Projected_spectral_power_Figs3_4.ipynb
Regression_results_Fig6.ipynb
__pycache__
archived_code
compute_spectral_power.py
config.py
feat_plot_utils.py
fit_regression_models.py
regression_utils.py
tfr_utils.py
regression_utils.py:13:from sklearn.linear_model import HuberRegressor
regression_utils.py:19:def user_def_f_aves(sbj_id):
regression_utils.py:51:def load_power_metadata(s,tfr_loadpath):
regression_utils.py:88:def update_events_dataframe(df_in,log_cols=['run_1'],log_cols1=['reach_r','onset_velocity'],bimanual_thresh=None):
regression_utils.py:117:def standardize_feats(df_in):
regression_utils.py:132:def train_test_split_power_inds(n_evs,per_train):
regression_utils.py:137:    np.random.shuffle(len_arr)
regression_utils.py:143:def train_test_split_day_balance(day_lst, per_train):
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code55/compute_power_gen_figs_python && sed -n 88,200p regression_utils.py; sed -n 236,462p regression_utils.py
```

```
def update_events_dataframe(df_in,log_cols=['run_1'],log_cols1=['reach_r','onset_velocity'],bimanual_thresh=None):
    '''
    Format events dataframe for context modelling. Can take absolute value or log of specific features.
    '''
    df_out = df_in.copy()
    df_out['patient_id'] = df_in.apply(lambda row: row['vid_name'][0:8], axis=1)
    df_out['tod'] = pd.to_timedelta(df_in['time'], unit='ms').dt.total_seconds()
    df_out['I_over_C_ratio'].fillna(0.5, inplace=True) #replace NaN's with 0.5
    for col in log_cols1:
        df_out[col] = np.log(df_in[col]+1)
    for col in log_cols:
        df_out[col] = np.log(df_in[col])
    if bimanual_thresh:
        df_in2 = df_in.copy()
        tmp_oll = df_in2['other_lead_lag'].values
        tmp_oll2 = tmp_oll.copy()
        tmp_oll2[np.isnan(tmp_oll)] = 0
        tmp_oll[np.abs(tmp_oll2)>bimanual_thresh] = np.nan
        bimanual = (1-np.isnan(tmp_oll)).tolist()
        df_out['bimanual'] = bimanual
[... 319 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && ls ../../executed 2>/dev/null; which python; python -c "import sklearn, mne, h5py, remfile; print(sklearn.__version__)"; grep -v "^#" requirements.in; date -u
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import sklearn, mne, h5py, remfile; print(sklearn.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'sklearn'
h5py
matplotlib
mne
numpy
pandas
remfile
requests
scikit-learn
scipy
statsmodels
Sat Nov  7 06:21:52 UTC 2026
```

**Agent**

Building a dev environment from the lock file.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.12 dev55 2>&1 | tail -2; uv pip install -q --python dev55/bin/python -r entries/000055-peterson-2021/requirements.lock.txt 2>&1 | tail -3; dev55/bin/python -c "import sklearn,numpy;print(sklearn.__version__, numpy.__version__)"; grep -n PYTHON_VERSION tools/entry.py | head -2
```

```
1.9.1 2.5.4
59:PYTHON_VERSION = "3.13"
335:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev && cat > $TMPDIR/dev/load.py <<'EOF'
import sys, time, pickle, numpy as np, pandas as pd
sys.path.insert(0, "entries/000055-peterson-2021")
import ajile
sub = sys.argv[1]
t = time.time()
assets = ajile.list_assets()
assets = assets[assets.subject == sub]
sessions = ajile.load_sessions(assets)
print("beh", time.time() - t, flush=True)
roi = ajile.roi_files()
good = sessions[0]["electrodes"]["good"].values.copy()
for s in sessions: s["subject_good"] = good
w = {sub: ajile.roi_weights(ajile.read_roi_matrix(sub, roi), good)}
t = time.time()
ecog = ajile.load_ecog(ajile.ecog_jobs(sessions, w))
print("ecog", time.time() - t, sum(len(r["ok"]) for r in ecog), flush=True)
for r in ecog: r.pop("roi_spec")
pickle.dump({"sessions": [{k: s[k] for k in ["events", "day", "subject", "electrodes"]} for s in sessions], "ecog": ecog, "good": good, "w": w[sub]},
            open(f"{sys.argv[2]}/s{sub}.pkl", "wb"))
EOF
cd $TMPDIR/dev && timeout 1500 ../dev55/bin/python load.py 07 . ; date -u
```

```
beh 8.459530591964722
ecog 139.1355972290039 800
Sat Nov  7 06:24:39 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && grep -n "regression" README.md reproduce_peterson_2021.ipynb | head -20; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][0]['source'])); print(''.join(nb['cells'][85]['source']))"
```

```
reproduce_peterson_2021.ipynb:25:    "the paper's regression R2 per electrode. Sex and age are not in it.\n",
reproduce_peterson_2021.ipynb:1590:    "The six regression claims need, for every good electrode of every subject and both bands, forward\n",
reproduce_peterson_2021.ipynb:1610:    "X, groups = ajile.regression_design(g)\n",
reproduce_peterson_2021.ipynb:1615:    "model = ajile.regression_model(X, groups, vals[:, best], g.day.values, rng_fig6, n_splits=200)\n",
reproduce_peterson_2021.ipynb:1625:    "print(\"For reference, the regression R2 stored in the files' electrode tables (low_freq_R2, high_freq_R2): \"\n",
reproduce_peterson_2021.ipynb:1635:    "**Result: blocked (too large).** One model takes the time printed above; the 2192 models of the main analysis alone exceed the notebook limit of 60 minutes on this machine, before the variants the claims ask for. The six regression claims are blocked for this reason."
reproduce_peterson_2021.ipynb:1693:    "| six regression claims (Figure 6, Extended Data Figure 6-2) | blocked, too large |\n",
reproduce_peterson_2021.ipynb:1701:    "transform is computed by FFT and matches MNE's direct convolution. The regression claims were not run.\n",
# Reproducing Peterson et al. (2021) from dandiset 000055

**Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural
variability of naturalistic arm movements. *eNeuro* 8(3), ENEURO.0007-21.2021.
[doi:10.1523/ENEURO.0007-21.2021](https://doi.org/10.1523/ENEURO.0007-21.2021). The claims file was
written from the version of record in Europe PMC (PMC8225404): main text, Methods, legends, Tables 1
and 2 and the legends of the Extended Data figures.

**Dataset.** [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12),
version 0.220127.0436. The paper cites no DANDI version: its data statement points to the curated
epochs on Figshare, and the dandiset was published later. This is the only published version, and
the draft 
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
src = open("ajile.py").read()
i = src.index("# ---------------------------------------------------------------- regression (timing only)")
new = r'''# ---------------------------------------------------------------- regression

def regression_design(ev: pd.DataFrame, log_plus_one: bool = False) -> tuple[pd.DataFrame, dict]:
    """The ten features of one subject's events, as the claims file's opening comment sets them.

    Columns in the code's order (regression_utils.single_subj_regression): the eight continuous or
    binary features, z-scored over the subject's events with pandas' SD (code,
    standardize_feats), then the day one-hot columns and the three time-of-day one-hot columns
    (0-8, 8-16, 16-24 h), not standardised (the code joins them after standardising). Reach
    duration and magnitude are log transformed (Methods); `log_plus_one` gives the code's
    log(duration), log(magnitude + 1), log(speed + 1). Returns the design and, per feature,
    its columns.
    """
    cols, groups = {}, {}
    if log_plus_one:
        cols["duration"], cols["magnitude"] = np.log(ev["duration"]), np.log(ev["magnitude"] + 1)
        cols["speed"] = np.log(ev["speed"] + 1)
    else:
        cols["duration"], cols["magnitude"] = np.log(ev["duration"]), np.log(ev["magnitude"])
        cols["speed"] = ev["speed"].astype(float)
    for c in ["angle", "speech", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]:
        cols[c] = ev[c].astype(float)
    X = pd.DataFrame(cols, index=ev.index)
    X = (X - X.mean()) / X.std().replace(0, 1)
    for c in X.columns:
        groups[c] = [c]
    for d in sorted(ev["day"].unique()):
        X[f"day_{d}"] = (ev["day"] == d).astype(float)
    groups["day"] = [c for c in X.columns if c.startswith("day_")]
    for b in range(3):
        X[f"tod_{b}"] = (ev["tod_bin"] == b).astype(float)
    groups["time_of_day"] = [f"tod_{b}" for b in range(3)]
    return X, groups


def forward_select(X: np.ndarray, y: np.ndarray) -> list:
    """Forward selection over columns by OLS adjusted R2 with an intercept (code,
    _forward_selected_new, which adds one column at a time, a day or time-of-day one-hot column
    being a column like any other). Adjusted R2 uses the rank of the design, as statsmodels does,
    so a column that adds nothing (the last day column beside the intercept) is not taken.
    Returns the selected column indices in the order taken."""
    n = len(y)
    yc = y - y.mean()
    tss = yc @ yc
    remaining, selected, current = list(range(X.shape[1])), [], 0.0
    while remaining:
        best, cand = -np.inf, None
        for c in remaining:
            A = np.column_stack([np.ones(n), X[:, selected + [c]]])
            beta, _, rank, _ = np.linalg.lstsq(A, y, rcond=None)
            res = y - A @ beta
            adj = 1 - (n - 1) / (n - rank) * (res @ res) / tss
            if adj > best:
                best, cand = adj, c
        if best > current:
            selected.append(cand)
            remaining.remove(cand)
            current = best
        else:
            break
    return selected


def _huber_obj(Z, y, th, alpha, eps, pen):
    q = Z.shape[-1]
    s = th[:, q]
    r = y - np.einsum("bnq,bq->bn", Z, th[:, :q])
    a = np.abs(r)
    out = a > eps * s[:, None]
    per = np.where(out, 2 * eps * a - eps ** 2 * s[:, None], r * r / s[:, None])
    return Z.shape[1] * s + per.sum(1) + alpha * (pen * th[:, :q] ** 2).sum(1)


def huber_fit(Z: np.ndarray, y: np.ndarray, alpha: float = 1e-4, epsilon: float = 1.35,
              max_iter: int = 100, tol: float = 1e-10) -> tuple[np.ndarray, np.ndarray]:
    """Many Huber regressions at once: Z is B x n x q (the last column all ones, the intercept),
    y is B x n. Minimises the objective of sklearn's HuberRegressor (defaults epsilon 1.35,
    alpha 1e-4 on the coefficients, not the intercept, with the scale estimated jointly):
    n*sigma + sum(H(r/sigma))*sigma + alpha*|w|^2. sklearn minimises it by L-BFGS, one problem
    at a time; here Newton's method with a backtracking line search solves all problems
    together, which reaches the same minimum (the objective is jointly convex). The notebook
    compares the two. Returns the coefficients (B x q, intercept last) and the scale."""
    B, n, q = Z.shape
    eps = epsilon
    pen = np.ones(q)
    pen[-1] = 0
    G = np.einsum("bnq,bnr->bqr", Z, Z) + 1e-8 * np.eye(q)
    w = np.linalg.solve(G, np.einsum("bnq,bn->bq", Z, y)[..., None])[..., 0]
    r = y - np.einsum("bnq,bq->bn", Z, w)
    s = np.maximum(np.median(np.abs(r), 1) / 0.6745, 1e-6)
    th = np.column_stack([w, s])
    f = _huber_obj(Z, y, th, alpha, eps, pen)
    active = np.ones(B, bool)
    for _ in range(max_iter):
        idx = np.nonzero(active)[0]
        if not len(idx):
            break
        Za, ya, ta = Z[idx], y[idx], th[idx]
        s = ta[:, q]
        r = ya - np.einsum("bnq,bq->bn", Za, ta[:, :q])
        inl = np.abs(r) <= eps * s[:, None]
        rin = np.where(inl, r, 0.0)
        sgn = np.where(inl, 0.0, np.sign(r))
        g = np.empty((len(idx), q + 1))
        g[:, :q] = (-2 / s[:, None] * np.einsum("bnq,bn->bq", Za, rin)
                    - 2 * eps * np.einsum("bnq,bn->bq", Za, sgn) + 2 * alpha * pen * ta[:, :q])
        g[:, q] = n - (rin ** 2).sum(1) / s ** 2 - (~inl).sum(1) * eps ** 2
        H = np.empty((len(idx), q + 1, q + 1))
        H[:, :q, :q] = 2 / s[:, None, None] * np.einsum("bnq,bnr->bqr", Za * inl[..., None], Za)
        H[:, :q, :q] += 2 * alpha * np.diag(pen)
        H[:, :q, q] = H[:, q, :q] = 2 / s[:, None] ** 2 * np.einsum("bnq,bn->bq", Za, rin)
        H[:, q, q] = 2 * (rin ** 2).sum(1) / s ** 3
        H += 1e-10 * np.eye(q + 1)
        d = -np.linalg.solve(H, g[..., None])[..., 0]
        dec = -(g * d).sum(1)
        t = np.ones(len(idx))
        fa = f[idx]
        todo = np.ones(len(idx), bool)
        new = ta.copy()
        for _ls in range(40):
            cand = ta[todo] + t[todo, None] * d[todo]
            okpos = cand[:, q] > 0
            fc = np.full(todo.sum(), np.inf)
            if okpos.any():
                fc[okpos] = _huber_obj(Za[todo][okpos], ya[todo][okpos], cand[okpos], alpha, eps, pen)
            acc = fc <= fa[todo] - 1e-4 * t[todo] * dec[todo]
            ti_ = np.nonzero(todo)[0]
            new[ti_[acc]] = cand[acc]
            fa[ti_[acc]] = fc[acc]
            todo[ti_[acc]] = False
            t[todo] *= 0.5
            if not todo.any():
                break
        th[idx] = new
        f[idx] = fa
        active[idx[(dec / 2 < tol * (np.abs(fa) + 1)) | todo]] = False
    return th[:, :q], th[:, q]


def _r2(y, pred):
    """Coefficient of determination per row (sklearn r2_score on each split's test events)."""
    res = ((y - pred) ** 2).sum(-1)
    tot = ((y - y.mean(-1, keepdims=True)) ** 2).sum(-1)
    return 1 - res / tot


def day_balanced_splits(days: np.ndarray, rng: np.random.Generator, n_splits: int = 200,
                        per_train: float = 0.9) -> tuple[np.ndarray, np.ndarray]:
    """Random train/test splits with equal numbers of test events from each day (code,
    train_test_split_day_balance; 90/10 from the Methods, 80/20 in the code). Returns
    n_splits x n_train and n_splits x n_test index arrays."""
    days = np.asarray(days)
    uni = np.unique(days)
    n_test_day = int(((1 - per_train) * len(days)) // len(uni))
    trs, tes = [], []
    for _ in range(n_splits):
        tr, te = [], []
        for d in uni:
            idx = rng.permutation(np.nonzero(days == d)[0])
            tr.extend(idx[:-n_test_day])
            te.extend(idx[-n_test_day:])
        trs.append(tr)
        tes.append(te)
    return np.array(trs), np.array(tes)


def electrode_model(args) -> dict:
    """One electrode and band: forward selection on all events, then a Huber fit per split of
    the full model and, per selected feature, of a refit with that feature's columns shuffled
    among the training events (all day columns together, all time-of-day columns together, as
    the code shuffles them). Unselected columns are set to 0 (code); a feature with no selected
    column gets Delta R2 0 (code).

    Returns the split-averaged withheld R2 of the full model; per feature the Delta R2 of the
    Methods (refit scored on the unshuffled withheld events) and of the code (refit scored on
    withheld events whose columns are shuffled among them; the code shuffles the column over
    all events before splitting, here the refit is shared with the Methods' version); the
    split-averaged coefficients per feature (for day and time of day the SD of their one-hot
    coefficients, code); and the fraction of each feature's columns selected (code,
    feat_select_prob). With `full_only`, only the full model is fitted.
    """
    X, groups, y, tr, te, seed, full_only = args
    rng = np.random.default_rng(seed)
    names = list(groups)
    col_of = {g: [i for i, c in enumerate(X.columns) if c in groups[g]] for g in names}
    Xn = X.to_numpy(float)
    sel = forward_select(Xn, y)
    keep = sorted(sel)
    Z = np.column_stack([Xn[:, keep], np.ones(len(y))])
    S = tr.shape[0]
    Ztr, ytr, Zte, yte = Z[tr], y[tr], Z[te], y[te]
    sel_groups = [g for g in names if any(c in keep for c in col_of[g])]
    probs = [Ztr]
    if not full_only:
        for g in sel_groups:
            zi = [keep.index(c) for c in col_of[g] if c in keep]
            Zs = Ztr.copy()
            perm = np.argsort(rng.random(Ztr.shape[:2]), axis=1)
            Zs[:, :, zi] = np.take_along_axis(Ztr[:, :, zi], perm[..., None], axis=1)
            probs.append(Zs)
    W, _ = huber_fit(np.concatenate(probs), np.tile(ytr, (len(probs), 1)))
    pred = np.einsum("bnq,bq->bn", Zte, W[:S])
    r2_full = _r2(yte, pred)
    coef_all = np.zeros((S, Xn.shape[1]))
    coef_all[:, keep] = W[:S, :-1]
    coefs = {}
    for g in names:
        ci = col_of[g]
        coefs[g] = float(coef_all[:, ci].std(1).mean() if len(ci) > 1 else coef_all[:, ci[0]].mean())
    out = {"selected": [X.columns[c] for c in sel], "r2": float(r2_full.mean()), "coef": coefs,
           "keep_prob": {g: float(np.mean([c in keep for c in col_of[g]])) for g in names}}
    if full_only:
        return out
    dr2, dr2_code = {g: 0.0 for g in names}, {g: 0.0 for g in names}
    for k, g in enumerate(sel_groups):
        Wg = W[(k + 1) * S:(k + 2) * S]
        dr2[g] = float((r2_full - _r2(yte, np.einsum("bnq,bq->bn", Zte, Wg))).mean())
        zi = [keep.index(c) for c in col_of[g] if c in keep]
        Zts = Zte.copy()
        perm = np.argsort(rng.random(Zte.shape[:2]), axis=1)
        Zts[:, :, zi] = np.take_along_axis(Zte[:, :, zi], perm[..., None], axis=1)
        dr2_code[g] = float((r2_full - _r2(yte, np.einsum("bnq,bq->bn", Zts, Wg))).mean())
    out["delta_r2"], out["delta_r2_code"] = dr2, dr2_code
    return out


def run_models(jobs: list, workers: int = 4) -> list[dict]:
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(electrode_model, jobs, chunksize=4))
'''
open("ajile.py", "w").write(src[:i] + new)
EOF
grep -n "regression\|Huber" ajile.py | head
```

```
/bin/bash: line 1: cd: entries/000055-peterson-2021: No such file or directory
8:electrode table (MNI x, y, z, group, `good`, and the paper's regression R2 per electrode), pose
29:- Band power (Methods, "Single-event spectral power linear regression"; Figure 5 legend): 0 to
419:# ---------------------------------------------------------------- regression (timing only)
421:def regression_design(ev: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
468:def regression_model(X, groups, y, days, rng, n_splits=200, per_train=0.9):
469:    """One electrode and band: Huber regression over day-balanced splits, full R2 and Delta R2.
471:    Used here only to time one model (sklearn HuberRegressor defaults, as the code)."""
472:    from sklearn.linear_model import HuberRegressor
491:        m = HuberRegressor().fit(Xs[tr], y[tr])
501:            ms = HuberRegressor().fit(Xsh, y[tr])
```

**Agent calls Bash**

```bash
pwd
```

```
entries/000055-peterson-2021
```

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/_regression_new.py",
 "content": "# ---------------------------------------------------------------- regression\n\ndef regression_design(ev: pd.DataFrame, log_plus_one: bool = False) -> tuple[pd.DataFrame, dict]:\n    \"\"\"The ten features of one subject's events, as the claims file's opening comment sets them.\n\n    Columns in the code's order (regression_utils.single_subj_regression): the eight continuous or\n    binary features, z-scored over the subject's events with pandas' SD (code,\n    standardize_feats), then the day one-hot columns and the three time-of-day one-hot columns\n    (0-8, 8-16, 16-24 h), not standardised (the code joins them after standardising). Reach\n    duration and magnitude are log transformed (Methods); `log_plus_one` gives the code's\n    log(duration), log(magnitude + 1), log(speed + 1). Returns the design and, per feature,\n    its columns.\n    \"\"\"\n    cols, groups = {}, {}\n    if log_plus_one:\n        cols[\"duration\"], cols[\"magnitude\"] = np.log(ev[\"duration\"]), np.log(ev[\"magnitude\"] + 1)\n        cols[\"speed\"] = np.log(ev[\"speed\"] + 1)\n    else:\n        cols[\"duration\"], cols[\"magnitude\"] = np.log(ev[\"duration\"]), np.log(ev[\"magnitude\"])\n        cols[\"speed\"] = ev[\"speed\"].astype(float)\n    for c in [\"angle\", \"speech\", \"bimanual_ratio\", \"bimanual_overlap\", \"bimanual_class\"]:\n        cols[c] = ev[c].astype(float)\n    X = pd.DataFrame(cols, index=ev.index)\n    X = (X - X.mean()) / X.std().replace(0, 1)\n    for c in X.columns:\n        groups[c] = [c]\n    for d in sorted(ev[\"day\"].unique()):\n        X[f\"day_{d}\"] = (ev[\"day\"] == d).astype(float)\n    groups[\"day\"] = [c for c in X.columns if c.startswith(\"day_\")]\n    for b in range(3):\n        X[f\"tod_{b}\"] = (ev[\"tod_bin\"] == b).astype(float)\n    groups[\"time_of_day\"] = [f\"tod_{b}\" for b in range(3)]\n    return X, groups\n\n\ndef forward_select(X: np.ndarray, y: np.ndarray) -> list:\n    \"\"\"Forward selection over columns by OLS adjusted R2 with an intercept (code,\n    _forward_selected_new, which adds one column at a time, a day or time-of-day one-hot column\n    being a column like any other). Adjusted R2 uses the rank of the design, as statsmodels does,\n    so a column that adds nothing (the last day column beside the intercept) is not taken.\n    Returns the selected column indices in the order taken.\"\"\"\n    n = len(y)\n    yc = y - y.mean()\n    tss = yc @ yc\n    remaining, selected, current = list(range(X.shape[1])), [], 0.0\n    while remaining:\n        best, cand = -np.inf, None\n        for c in remaining:\n            A = np.column_stack([np.ones(n), X[:, selected + [c]]])\n            beta, _, rank, _ = np.linalg.lstsq(A, y, rcond=None)\n            res = y - A @ beta\n            adj = 1 - (n - 1) / (n - rank) * (res @ res) / tss\n            if adj > best:\n                best, cand = adj, c\n        if best > current:\n            selected.append(cand)\n            remaining.remove(cand)\n            current = best\n        else:\n            break\n    return selected\n\n\ndef _huber_obj(Z, y, th, alpha, eps, pen):\n    q = Z.shape[-1]\n    s = th[:, q]\n    r = y - np.einsum(\"bnq,bq->bn\", Z, th[:, :q])\n    a = np.abs(r)\n    out = a > eps * s[:, None]\n    per = np.where(out, 2 * eps * a - eps ** 2 * s[:, None], r * r / s[:, None])\n    return Z.shape[1] * s + per.sum(1) + alpha * (pen * th[:, :q] ** 2).sum(1)\n\n\ndef huber_fit(Z: np.ndarray, y: np.ndarray, alpha: float = 1e-4, epsilon: float = 1.35,\n              max_iter: int = 100, tol: float = 1e-10) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Many Huber regressions at once: Z is B x n x q (the last column all ones, the intercept),\n    y is B x n. Minimises the objective of sklearn's HuberRegressor (defaults epsilon 1.35,\n    alpha 1e-4 on the coefficients, not the intercept, with the scale estimated jointly):\n    n*sigma + sum(H(r/sigma))*sigma + alpha*|w|^2. sklearn minimises it by L-BFGS, one problem\n    at a time; here Newton's method with a backtracking line search solves all problems\n    together, which reaches the same minimum (the objective is jointly convex). The notebook\n    compares the two. Returns the coefficients (B x q, intercept last) and the scale.\"\"\"\n    B, n, q = Z.shape\n    eps = epsilon\n    pen = np.ones(q)\n    pen[-1] = 0\n    G = np.einsum(\"bnq,bnr->bqr\", Z, Z) + 1e-8 * np.eye(q)\n    w = np.linalg.solve(G, np.einsum(\"bnq,bn->bq\", Z, y)[..., None])[..., 0]\n    r = y - np.einsum(\"bnq,bq->bn\", Z, w)\n    s = np.maximum(np.median(np.abs(r), 1) / 0.6745, 1e-6)\n    th = np.column_stack([w, s])\n    f = _huber_obj(Z, y, th, alpha, eps, pen)\n    active = np.ones(B, bool)\n    for _ in range(max_iter):\n        idx = np.nonzero(active)[0]\n        if not len(idx):\n            break\n        Za, ya, ta = Z[idx], y[idx], th[idx]\n        s = ta[:, q]\n        r = ya - np.einsum(\"bnq,bq->bn\", Za, ta[:, :q])\n        inl = np.abs(r) <= eps * s[:, None]\n        rin = np.where(inl, r, 0.0)\n        sgn = np.where(inl, 0.0, np.sign(r))\n        g = np.empty((len(idx), q + 1))\n        g[:, :q] = (-2 / s[:, None] * np.einsum(\"bnq,bn->bq\", Za, rin)\n                    - 2 * eps * np.einsum(\"bnq,bn->bq\", Za, sgn) + 2 * alpha * pen * ta[:, :q])\n        g[:, q] = n - (rin ** 2).sum(1) / s ** 2 - (~inl).sum(1) * eps ** 2\n        H = np.empty((len(idx), q + 1, q + 1))\n        H[:, :q, :q] = 2 / s[:, None, None] * np.matmul((Za * inl[..., None]).transpose(0, 2, 1), Za)\n        H[:, :q, :q] += 2 * alpha * np.diag(pen)\n        H[:, :q, q] = 2 / s[:, None] ** 2 * np.einsum(\"bnq,bn->bq\", Za, rin)\n        H[:, q, :q] = H[:, :q, q]\n        H[:, q, q] = 2 * (rin ** 2).sum(1) / s ** 3\n        H += 1e-10 * np.eye(q + 1)\n        d = -np.linalg.solve(H, g[..., None])[..., 0]\n        dec = -(g * d).sum(1)\n        t = np.ones(len(idx))\n        fa = f[idx].copy()\n        todo = np.ones(len(idx), bool)\n        new = ta.copy()\n        for _ls in range(40):\n            ti_ = np.nonzero(todo)[0]\n            cand = ta[ti_] + t[ti_, None] * d[ti_]\n            okpos = cand[:, q] > 0\n            fc = np.full(len(ti_), np.inf)\n            if okpos.any():\n                fc[okpos] = _huber_obj(Za[ti_[okpos]], ya[ti_[okpos]], cand[okpos], alpha, eps, pen)\n            acc = fc <= fa[ti_] - 1e-4 * t[ti_] * dec[ti_]\n            new[ti_[acc]] = cand[acc]\n            fa[ti_[acc]] = fc[acc]\n            todo[ti_[acc]] = False\n            t[todo] *= 0.5\n            if not todo.any():\n                break\n        th[idx] = new\n        f[idx] = fa\n        active[idx[(dec / 2 < tol * (np.abs(fa) + 1)) | todo]] = False\n    return th[:, :q], th[:, q]\n\n\ndef _r2(y, pred):\n    \"\"\"Coefficient of determination per row (sklearn r2_score on each split's test events).\"\"\"\n    res = ((y - pred) ** 2).sum(-1)\n    tot = ((y - y.mean(-1, keepdims=True)) ** 2).sum(-1)\n    return 1 - res / tot\n\n\ndef day_balanced_splits(days: np.ndarray, rng: np.random.Generator, n_splits: int = 200,\n                        per_train: float = 0.9) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Random train/test splits with equal numbers of test events from each day (code,\n    train_test_split_day_balance; 90/10 from the Methods, 80/20 in the code). Returns\n    n_splits x n_train and n_splits x n_test index arrays.\"\"\"\n    days = np.asarray(days)\n    uni = np.unique(days)\n    n_test_day = int(((1 - per_train) * len(days)) // len(uni))\n    trs, tes = [], []\n    for _ in range(n_splits):\n        tr, te = [], []\n        for d in uni:\n            idx = rng.permutation(np.nonzero(days == d)[0])\n            tr.extend(idx[:-n_test_day])\n            te.extend(idx[-n_test_day:])\n        trs.append(tr)\n        tes.append(te)\n    return np.array(trs), np.array(tes)\n\n\ndef electrode_model(args) -> dict:\n    \"\"\"One electrode and band: forward selection on all events, then a Huber fit per split of\n    the full model and, per selected feature, of a refit with that feature's columns shuffled\n    among the training events (all day columns together, all time-of-day columns together, as\n    the code shuffles them). Unselected columns are set to 0 (code), which is the same as\n    leaving them out, as their coefficients are then 0; a feature with no selected column gets\n    Delta R2 0 (code).\n\n    Returns the split-averaged withheld R2 of the full model; per feature the Delta R2 of the\n    Methods (refit scored on the unshuffled withheld events) and of the code (refit scored on\n    withheld events whose columns are shuffled among them; the code shuffles the column over\n    all events before splitting, here the refit is shared with the Methods' version); the\n    split-averaged coefficients per feature (for day and time of day the SD of their one-hot\n    coefficients, code); and the fraction of each feature's columns selected (code,\n    feat_select_prob). With `full_only`, only the full model is fitted.\n    \"\"\"\n    X, groups, y, tr, te, seed, full_only = args\n    rng = np.random.default_rng(seed)\n    names = list(groups)\n    col_of = {g: [i for i, c in enumerate(X.columns) if c in groups[g]] for g in names}\n    Xn = X.to_numpy(float)\n    sel = forward_select(Xn, y)\n    keep = sorted(sel)\n    Z = np.column_stack([Xn[:, keep], np.ones(len(y))])\n    S = tr.shape[0]\n    Ztr, ytr, Zte, yte = Z[tr], y[tr], Z[te], y[te]\n    sel_groups = [g for g in names if any(c in keep for c in col_of[g])]\n    probs = [Ztr]\n    if not full_only:\n        for g in sel_groups:\n            zi = [keep.index(c) for c in col_of[g] if c in keep]\n            Zs = Ztr.copy()\n            perm = np.argsort(rng.random(Ztr.shape[:2]), axis=1)\n            Zs[:, :, zi] = np.take_along_axis(Ztr[:, :, zi], perm[..., None], axis=1)\n            probs.append(Zs)\n    W, _ = huber_fit(np.concatenate(probs), np.tile(ytr, (len(probs), 1)))\n    pred = np.einsum(\"bnq,bq->bn\", Zte, W[:S])\n    r2_full = _r2(yte, pred)\n    coef_all = np.zeros((S, Xn.shape[1]))\n    coef_all[:, keep] = W[:S, :-1]\n    coefs = {}\n    for g in names:\n        ci = col_of[g]\n        coefs[g] = float(coef_all[:, ci].std(1).mean() if len(ci) > 1 else coef_all[:, ci[0]].mean())\n    out = {\"selected\": [X.columns[c] for c in sel], \"r2\": float(r2_full.mean()), \"coef\": coefs,\n           \"keep_prob\": {g: float(np.mean([c in keep for c in col_of[g]])) for g in names}}\n    if full_only:\n        return out\n    dr2, dr2_code = {g: 0.0 for g in names}, {g: 0.0 for g in names}\n    for k, g in enumerate(sel_groups):\n        Wg = W[(k + 1) * S:(k + 2) * S]\n        dr2[g] = float((r2_full - _r2(yte, np.einsum(\"bnq,bq->bn\", Zte, Wg))).mean())\n        zi = [keep.index(c) for c in col_of[g] if c in keep]\n        Zts = Zte.copy()\n        perm = np.argsort(rng.random(Zte.shape[:2]), axis=1)\n        Zts[:, :, zi] = np.take_along_axis(Zte[:, :, zi], perm[..., None], axis=1)\n        dr2_code[g] = float((r2_full - _r2(yte, np.einsum(\"bnq,bq->bn\", Zts, Wg))).mean())\n    out[\"delta_r2\"], out[\"delta_r2_code\"] = dr2, dr2_code\n    return out\n\n\ndef run_models(jobs: list, workers: int = 4) -> list[dict]:\n    os.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\n    with ProcessPoolExecutor(workers) as ex:\n        return list(ex.map(electrode_model, jobs, chunksize=4))\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/_regression_new.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
src = open("ajile.py").read()
i = src.index("# ---------------------------------------------------------------- regression (timing only)")
open("ajile.py", "w").write(src[:i] + open("_regression_new.py").read())
EOF
rm _regression_new.py; tail -3 ajile.py
```

```
os.environ.setdefault("OMP_NUM_THREADS", "1")
    with ProcessPoolExecutor(workers) as ex:
        return list(ex.map(electrode_model, jobs, chunksize=4))
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/test.py <<'EOF'
import sys, time, pickle, os
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np, pandas as pd
sys.path.insert(0, "entries/000055-peterson-2021")
import importlib, ajile
d = pickle.load(open(sys.argv[1], "rb"))
rows = []
for s, r in zip(d["sessions"], d["ecog"]):
    e = s["events"].copy(); e["day"] = s["day"]
    e["ok"] = r["ok"]; e["q_all"] = r["q_all"]; e["q_hf"] = r["q_hf"]
    e["y"] = [b["lfb_mean"] if b is not None else None for b in r["el_band"]]
    e["yh"] = [b["hfb_mean"] if b is not None else None for b in r["el_band"]]
    rows.append(e)
ev = pd.concat(rows, ignore_index=True)
ev = ev.rename(columns={"Reach_magnitude_px": "magnitude", "Reach_angle_degrees": "angle_file",
                        "Onset_speed_px_per_sec": "speed", "Speech_ratio": "speech",
                        "Bimanual_ratio": "bimanual_ratio", "Bimanual_overlap": "bimanual_overlap",
                        "Bimanual_class": "bimanual_class"})
ev["angle"] = ajile.fold_angle(-ev["angle_file"])
ev["tod_bin"] = np.clip((ev.start_time / 3600 // 8).astype(int), 0, 2)
thr = ev[ev.ok].q_hf.mean() + 3 * ev[ev.ok].q_hf.std()
E = ev[ev.ok & np.isfinite(ev.q_all) & (ev.q_all >= 0) & (ev.q_hf <= thr)].reset_index(drop=True)
Y = np.stack(E.y.values); YH = np.stack(E.yh.values)
print(len(E), Y.shape, d["good"].sum())
X, groups = ajile.regression_design(E)
print(X.columns.tolist())
rng = np.random.default_rng(0)
tr, te = ajile.day_balanced_splits(E.day.values, rng, 200, 0.9)
# compare huber_fit with sklearn
from sklearn.linear_model import HuberRegressor
el = int(np.argmax(np.abs(np.corrcoef(X.angle, Y.T)[0, 1:])))
y = Y[:, el]
sel = sorted(ajile.forward_select(X.to_numpy(float), y)); print("sel", [X.columns[c] for c in sel])
Z = np.column_stack([X.to_numpy(float)[:, sel], np.ones(len(y))])
t0 = time.time(); W, s = ajile.huber_fit(Z[tr[:50]], y[tr[:50]]); print("batch 50", time.time() - t0)
diffs, r2d = [], []
t0 = time.time()
for k in range(50):
    m = HuberRegressor().fit(Z[tr[k], :-1], y[tr[k]])
    wk = np.r_[m.coef_, m.intercept_]
    diffs.append(np.abs(wk - W[k]).max())
    r2d.append(abs(m.score(Z[te[k], :-1], y[te[k]]) - ajile._r2(y[te[k]], Z[te[k]] @ W[k])))
    if k == 0: print("scale", m.scale_, s[k])
print("sklearn 50", time.time() - t0, "max coef diff", max(diffs), "max r2 diff", max(r2d))
# objective comparison
for job_y, nm in [(y, "lfb")]:
    t0 = time.time()
    out = ajile.electrode_model((X, groups, job_y, tr, te, 1, False))
    print("one model", time.time() - t0, out["r2"], out["selected"])
    print(out["delta_r2"]); print(out["delta_r2_code"]); print(out["coef"]); print(out["keep_prob"])
EOF
cd $TMPDIR/dev && ../dev55/bin/python test.py s07.pkl
```

```
784 (784, 64) 63
['duration', 'magnitude', 'speed', 'angle', 'speech', 'bimanual_ratio', 'bimanual_overlap', 'bimanual_class', 'day_3', 'day_4', 'day_5', 'day_6', 'day_7', 'tod_0', 'tod_1', 'tod_2']
sel ['duration', 'magnitude', 'speed', 'angle', 'speech', 'bimanual_ratio', 'bimanual_overlap', 'day_5']
batch 50 0.021416664123535156
scale 2.368964993288115 2.3689683432351862
sklearn 50 0.0943596363067627 max coef diff 0.0002844492343566096 max r2 diff 1.7156644369076268e-05
one model 0.6602351665496826 0.044167404500130764 ['angle', 'bimanual_ratio', 'magnitude', 'day_5', 'speech', 'duration', 'bimanual_overlap', 'speed']
{'duration': 0.001973207268125631, 'magnitude': 0.002025304215004853, 'speed': -0.0007602057942793477, 'angle': 0.02353487044142667, 'speech': 0.002037916865935653, 'bimanual_ratio': 0.0008119700574393069, 'bimanual_overlap': 0.004017678329125963, 'bimanual_class': 0.0, 'day': 0.0037042126965337197, 'time_of_day': 0.0}
{'duration': 0.0018274355908116913, 'magnitude': 0.0009761096783554341, 'speed': 0.000355833317935399, 'angle': 0.02297874846634473, 'speech': -0.00032530672861695917, 'bimanual_ratio': -0.0005515984045705896, 'bimanual_overlap': 0.0033655118124270417, 'bimanual_class': 0.0, 'day': 0.004792899741215863, 'time_of_day': 0.0}
{'duration': -0.2239484811487843, 'magnitude': -0.15915051152729096, 'speed': -0.18144708008181873, 'angle': -0.6595588921945513, 'speech': -0.12944699144395214, 'bimanual_ratio': 0.20672871998905698, 'bimanual_overlap': 0.24579630711566758, 'bimanual_class': 0.0, 'day': 0.2288495215185285, 'time_of_day': 0.0}
{'duration': 1.0, 'magnitude': 1.0, 'speed': 1.0, 'angle': 1.0, 'speech': 1.0, 'bimanual_ratio': 1.0, 'bimanual_overlap': 1.0, 'bimanual_class': 0.0, 'day': 0.2, 'time_of_day': 0.0}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/dev/test.py <<'EOF'
t0 = time.time(); [ajile.forward_select(X.to_numpy(float), Y[:, k]) for k in range(10)]; print("fs x10", time.time() - t0)
t0 = time.time(); out = ajile.electrode_model((X, groups, y, tr, te, 1, True)); print("full only", time.time() - t0)
EOF
cd $TMPDIR/dev && ../dev55/bin/python test.py s07.pkl 2>&1 | tail -2
```

```
fs x10 0.036185503005981445
full only 0.07336974143981934
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -n -i "depth\|Table 2" paper/10.1038-s41597-022-01280-y.txt | head -30; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{300\}surface.\{600\}" paper/10.1038-s41597-022-01280-y.txt | grep -i "table\|S01\|EC0" | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021; python -c "
import json;nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [5,6,29,30,38,40,62,64,65]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 5
info = pd.DataFrame([{
    "subject": s["subject"], "day": s["day"], "subject_id": s["subject_id"], "session_id": s["session_id"],
    "session_start_time": s["session_start_time"], "electrodes": len(s["electrodes"]),
    "good": int(s["electrodes"]["good"].sum()), "events": len(s["events"]), "wrist": s["reach_event_desc"],
    "ecog_hours": round(s["ecog_shape"][0] / s["ecog_rate"] / 3600, 2), "ecog_Hz": s["ecog_rate"],
    "pose_hours": round(s["pose_shape"][0] / s["pose_rate"] / 3600, 2), "pose_Hz": s["pose_rate"],
    "first_event_h": round(s["events"].start_time.min() / 3600, 2),
    "last_event_h": round(s["events"].start_time.max() / 3600, 2)} for s in sessions])
print(info.to_string(index=False))
print("\nSubjects:", info.subject.nunique(), "; files:", len(info), "; events:", int(info.events.sum()))
print("subject_id and session_id agree with the file names:",
      bool((info.subject_id == info.subject).all() and (info.session_id.astype(int) == info.day).all()))
print("Subject fields in the files:", sorted({tuple(s["subject_fields"]) for s in sessions}))
print("ECoG unit and conversion:", {(s["ecog_unit"], s["ecog_conversion"]) for s in sessions},
      "; pose unit:", {s["pose_unit"] for s in sessions})
LOC = ["x", "y", "z", "group_name", "low_freq_R2", "high_freq_R2"]
print("Electrode positions, groups and stored R2 identical across a subject's files:",
      all(sessions[i]["electrodes"][LOC].equals(sessions[j]["electrodes"][LOC])
          for i in range(len(sessions)) for j in range(len(sessions))
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && timeout 900 ../dev55/bin/python load.py 05 . ; date -u
```

```
beh 7.957792282104492
ecog 306.7961883544922 267
Sat Nov  7 06:33:26 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
s = open("ajile.py").read()
s = s.replace('''def roi_weights(df: pd.DataFrame, good: np.ndarray) -> np.ndarray:
    """Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them.
''', '''def roi_weights(df: pd.DataFrame, good: np.ndarray, normalise: bool = True) -> np.ndarray:
    """Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them.
    With `normalise=False`, the rows of the file for every electrode, as they are.
''')
s = s.replace('''        raise ValueError(f"{len(w)} projection rows for {len(good)} electrodes")
    w[~good] = 0''', '''        raise ValueError(f"{len(w)} projection rows for {len(good)} electrodes")
    if not normalise:
        return w
    w[~good] = 0''')
s = s.replace('''    X, groups, y, tr, te, seed, full_only = args
    rng = np.random.default_rng(seed)
    names = list(groups)''', '''    X, groups, y, tr, te, seed, full_only = args
    rng = np.random.default_rng(seed)
    names = list(groups)
    if not np.std(y) > 0:
        return None                     # a flat electrode: nothing to fit''')
open("ajile.py", "w").write(s)
EOF
grep -n "normalise\|flat electrode" ajile.py
```

```
45:  region's weights are renormalised to sum to 1 (`rem_bad_chans=True` in the Figure 3 to 5
207:def roi_weights(df: pd.DataFrame, good: np.ndarray, normalise: bool = True) -> np.ndarray:
209:    With `normalise=False`, the rows of the file for every electrode, as they are.
223:    if not normalise:
609:        return None                     # a flat electrode: nothing to fit
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/cells && cd $TMPDIR/cells && cat > r_setup.py <<'EOF'
# Regression inputs per subject: the kept events (reading b, as the code's power files hold),
# the design of the ten features, the electrode band power (all electrodes; the bad ones are
# used only for the code's variant), and 200 day-balanced splits for each split ratio.
rng_fig6 = np.random.default_rng(6)
E = ev[ev.keep_b]
keep = ev.keep_b.values
Y = {}
i = 0
for s, r in zip(sessions, ecog):
    for k in range(len(r["ok"])):
        if keep[i]:
            for meas in ["mean", "median"]:
                for band in ["lfb", "hfb"]:
                    Y.setdefault((s["subject"], meas, band), []).append(r["el_band"][k][f"{band}_{meas}"])
        i += 1
Y = {key: np.array(v) for key, v in Y.items()}
design, splits = {}, {}
for sub in SUBJECTS:
    g = E[E.subject == sub]
    assert len(g) == len(Y[(sub, "mean", "lfb")])
    design[sub] = ajile.regression_design(g)
    splits[sub] = {pt: ajile.day_balanced_splits(g.day.values, rng_fig6, 200, pt) for pt in (0.9, 0.8)}
REG_FEATS = list(design[SUBJECTS[0]][1])
n_el = {sub: Y[(sub, "mean", "lfb")].shape[1] for sub in SUBJECTS}
print("Features:", REG_FEATS)
print("Per subject: events, design columns, electrodes (good), test events per split at 90/10 and 80/20:")
for sub in SUBJECTS:
    print(f"  S{sub}: {len(Y[(sub, 'mean', 'lfb')])} events, {design[sub][0].shape[1]} columns, {n_el[sub]} electrodes "
          f"({int(first_good[sub].sum())} good), {splits[sub][0.9][1].shape[1]} and {splits[sub][0.8][1].shape[1]} test events")
EOF
cat > r_check.py <<'EOF'
# The batched Huber fit (helper huber_fit) against sklearn's HuberRegressor, which the code uses,
# on the first 20 splits of one electrode per subject (the electrode whose LFB power correlates
# best with reach angle), with the columns forward selection keeps.
from sklearn.linear_model import HuberRegressor
rows = []
for sub in SUBJECTS:
    X, groups = design[sub]
    Xn = X.to_numpy(float)
    y = Y[(sub, "mean", "lfb")][:, int(np.nanargmax(np.abs(np.corrcoef(X["angle"], Y[(sub, "mean", "lfb")].T)[0, 1:])))]
    cols = sorted(ajile.forward_select(Xn, y))
    Z = np.column_stack([Xn[:, cols], np.ones(len(y))])
    tr, te = splits[sub][0.9]
    W, _ = ajile.huber_fit(Z[tr[:20]], y[tr[:20]])
    for k in range(20):
        m = HuberRegressor().fit(Z[tr[k], :-1], y[tr[k]])
        rows.append({"subject": sub, "coef_diff": np.abs(np.r_[m.coef_, m.intercept_] - W[k]).max(),
                     "r2_diff": abs(m.score(Z[te[k], :-1], y[te[k]]) - ajile._r2(y[te[k]], Z[te[k]] @ W[k]))})
hc = pd.DataFrame(rows)
print(f"{len(hc)} fits: largest coefficient difference {hc.coef_diff.max():.2e}, largest withheld R2 difference "
      f"{hc.r2_diff.max():.2e} (median {hc.r2_diff.median():.1e})")
EOF
cat > r_run.py <<'EOF'
# The models. Stage 1 fits the full model for every electrode and band (forward selection and
# 200 splits); the Delta R2 refits are needed only where the full model's R2 exceeds 0.05 (the
# electrodes Figure 6c-d show), so stage 2 refits those, in both bands. The same for the code's
# 80/20 split (good electrodes), and the full model for the code's median band power.
def seed_of(sub, e, band, variant):
    return int(sub) * 100000 + e * 100 + (band == "hfb") * 10 + variant

def fit(keys, meas, per_train, full_only, variant):
    jobs = []
    for sub, e, band in keys:
        X, groups = design[sub]
        tr, te = splits[sub][per_train]
        jobs.append((X, groups, Y[(sub, meas, band)][:, e], tr, te, seed_of(sub, e, band, variant), full_only))
    rows = []
    for (sub, e, band), out in zip(keys, ajile.run_models(jobs)):
        row = {"subject": sub, "electrode": e, "band": band, "good": bool(first_good[sub][e])}
        if out is None:
            rows.append(row)
            continue
        row.update({"r2": out["r2"], "selected": out["selected"]})
        row.update({f"coef:{f}": v for f, v in out["coef"].items()})
        row.update({f"keep:{f}": v for f, v in out["keep_prob"].items()})
        if not full_only:
            row.update({f"dr2:{f}": v for f, v in out["delta_r2"].items()})
            row.update({f"dr2code:{f}": v for f, v in out["delta_r2_code"].items()})
        rows.append(row)
    return pd.DataFrame(rows)

def two_stage(meas, per_train, electrodes, variant):
    keys = [(sub, e, band) for sub in SUBJECTS for e in electrodes(sub) for band in ["lfb", "hfb"]]
    full = fit(keys, meas, per_train, True, variant)
    over = full[full.r2 > 0.05][["subject", "electrode"]].drop_duplicates()
    keys2 = [(s_, e, band) for s_, e in over.itertuples(index=False) for band in ["lfb", "hfb"]]
    refit = fit(keys2, meas, per_train, False, variant)
    out = full.merge(refit[["subject", "electrode", "band"] + [c for c in refit if c.startswith("dr2")]],
                     on=["subject", "electrode", "band"], how="left")
    assert np.allclose(full.set_index(["subject", "electrode", "band"]).loc[refit.set_index(["subject", "electrode", "band"]).index].r2,
                       refit.r2)
    return out, len(keys), len(keys2)

started = time.time()
reg, n1, n2 = two_stage("mean", 0.9, lambda sub: range(n_el[sub]), 0)
t_main = time.time() - started
reg82, m1, m2 = two_stage("mean", 0.8, lambda sub: np.nonzero(first_good[sub])[0], 1)
t_82 = time.time() - started - t_main
regmed = fit([(sub, e, band) for sub in SUBJECTS for e in np.nonzero(first_good[sub])[0] for band in ["lfb", "hfb"]],
             "median", 0.9, True, 2)
print(f"main (90/10, band mean, all electrodes): {n1} full models, {n2} with refits, {t_main / 60:.1f} min; "
      f"80/20 (good electrodes): {m1} and {m2}, {t_82 / 60:.1f} min; band median: {len(regmed)} full models; "
      f"total {(time.time() - started) / 60:.1f} min")
for name, d in [("main", reg), ("80/20", reg82), ("median", regmed)]:
    print(f"{name}: models with nothing to fit (flat power) {int(d.r2.isna().sum())}, of which good {int((d.r2.isna() & d.good).sum())}; "
          f"models with no feature selected {int((d.selected.str.len() == 0).sum())}")
G = reg[reg.good]
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && cat > c_r2.py <<'EOF'
rows = []
for name, d in [("main (90/10, band mean, good electrodes)", G), ("code's 80/20 split", reg82), ("code's band median", regmed)]:
    for band in ["lfb", "hfb"]:
        x = d[d.band == band].dropna(subset=["r2"])
        top = x.loc[x.r2.idxmax()]
        rows.append({"variant": name, "band": band.upper(), "models": len(x), "max_R2": round(top.r2, 3),
                     "at": f"S{top.subject} e{top.electrode}", "median_R2": round(x.r2.median(), 4),
                     "share_R2_over_0.05": round((x.r2 > 0.05).mean(), 3), "min_R2": round(x.r2.min(), 3)})
print(pd.DataFrame(rows).to_string(index=False))
print("\nPer subject (main): largest R2 and electrodes with R2 > 0.05, by band")
print(G.groupby(["subject", "band"]).r2.agg(["max", lambda v: int((v > 0.05).sum()), "count"])
      .rename(columns={"<lambda_0>": "over_0.05"}).unstack().round(3).to_string())
mx = G.r2.max()
print(f"\nLargest full-model withheld R2 over good electrodes, subjects and bands: {mx:.3f}; at most 0.275: {mx <= 0.275}")
print(f"With bad electrodes too: {reg.r2.max():.3f}")
# For reference only: the R2 the files store per electrode (the paper's own results), against these.
stored = pd.concat([s["electrodes"].assign(subject=s["subject"], electrode=np.arange(len(s["electrodes"])))
                    for s in sessions if s["day"] == min(x["day"] for x in sessions if x["subject"] == s["subject"])])
for band, col in [("lfb", "low_freq_R2"), ("hfb", "high_freq_R2")]:
    m = G[G.band == band].merge(stored[["subject", "electrode", col]], on=["subject", "electrode"]).dropna(subset=["r2", col])
    print(f"stored {col}: max {stored[col].max():.3f}; Spearman with the R2 here over {len(m)} good electrodes "
          f"{stats.spearmanr(m.r2, m[col])[0]:.3f}; median difference (here minus stored) {np.median(m.r2 - m[col]):+.4f}")
EOF
cat > c_6b.py <<'EOF'
FP5 = ["middle frontal", "precentral", "postcentral", "inferior parietal", "supramarginal"]
SM3 = ["precentral", "postcentral", "inferior parietal"]
TEMP = ["superior temporal", "middle temporal", "inferior temporal"]
raw_w = {sub: ajile.roi_weights(roi_mats[sub], first_good[sub], normalise=False) for sub in SUBJECTS}
def region_of(sub, e):
    w = raw_w[sub][e]
    return ajile.ROI_NAMES[int(np.argmax(w))] if w.sum() > 0 else "none"
for d in (G, reg, reg82):
    d["region"] = [region_of(s_, e) for s_, e in zip(d.subject, d.electrode)]

def project(d, col):
    """Projection-weighted mean over each subject's good electrodes, then the mean over subjects."""
    per = []
    for sub in SUBJECTS:
        v = np.zeros(n_el[sub])
        x = d[d.subject == sub]
        v[x.electrode.values] = np.nan_to_num(x[col].values.astype(float))
        with np.errstate(invalid="ignore"):
            per.append(weights[sub].T @ v)
    return pd.Series(np.nanmean(per, 0), index=ajile.ROI_NAMES), pd.Series(np.sum(np.isfinite(per), 0), index=ajile.ROI_NAMES)

holds6b = {}
for band in ["lfb", "hfb"]:
    d = G[G.band == band]
    hi = d[d.r2 > 0.05]
    proj, n_sub = project(d, "r2")
    tab = pd.DataFrame({"electrodes": d.groupby("region").size(), "R2_over_0.05": hi.groupby("region").size(),
                        "median_R2": d.groupby("region").r2.median().round(4), "projected_R2": proj.round(4),
                        "subjects_covering": n_sub}).fillna(0)
    print(f"{band.upper()}:\n{tab.to_string()}")
    share = hi.region.isin(FP5).mean()
    med_sm, med_t = d[d.region.isin(SM3)].r2.median(), d[d.region.isin(TEMP)].r2.median()
    top3 = list(proj.sort_values(ascending=False).index[:3])
    a = bool(share > 0.5 and med_sm > med_t)
    b = all(r in FP5 for r in top3)
    holds6b[band] = (a, b)
    print(f"  reading a: {len(hi)} electrodes with R2 > 0.05, share in the five frontoparietal regions {share:.3f}; "
          f"median R2 sensorimotor {med_sm:.4f} against temporal {med_t:.4f}; holds {a}")
    print(f"  reading b: three highest projected R2 {top3}; all frontoparietal: {b}")
print("Holds (reading a, reading b):", holds6b)
EOF
cat > c_6c.py <<'EOF'
FEAT_ORDER = ["angle", "day", "duration", "magnitude", "speed", "speech", "bimanual_ratio", "bimanual_overlap",
              "bimanual_class", "time_of_day"]
def ranked(d, band, prefix, select_band=None, fn=np.median):
    """Median over electrodes with R2 > 0.05 (in `select_band`, default the same band) of a per-feature column."""
    sb = select_band or band
    ok = d[(d.band == sb) & (d.r2 > 0.05)][["subject", "electrode"]]
    x = d[d.band == band].merge(ok, on=["subject", "electrode"])
    vals = pd.Series({f: fn(x[f"{prefix}{f}"].values) for f in FEAT_ORDER})
    return vals.sort_values(ascending=False), len(x)
variants6c = [("main", G, "dr2:", None), ("code's Delta R2", G, "dr2code:", None),
              ("code's selection by LFB R2", G, "dr2:", "lfb"), ("code's 80/20 split", reg82[reg82.good], "dr2:", None),
              ("with bad electrodes", reg, "dr2:", None)]
tabs, top2 = {}, {}
for name, d, prefix, sb in variants6c:
    for band in ["lfb", "hfb"]:
        v, n = ranked(d, band, prefix, sb)
        tabs[(name, band.upper(), n)] = v.round(4)
        top2[(name, band)] = list(v.index[:2])
print("Median Delta R2 over electrodes with R2 > 0.05 (variant, band, electrodes):")
print(pd.DataFrame(tabs).loc[FEAT_ORDER].to_string())
for k, v in top2.items():
    print(f"  {k[0]}, {k[1].upper()}: two largest {v}; angle and day both: {set(v) == {'angle', 'day'}}")
EOF
cat > c_e62.py <<'EOF'
keep_proj = {}
for band in ["lfb", "hfb"]:
    d = G[G.band == band]
    keep_proj[band] = pd.DataFrame({f: project(d, f"keep:{f}")[0] for f in FEAT_ORDER})
    print(f"{band.upper()}: retention probability projected onto the regions (mean over subjects)")
    print(keep_proj[band].round(3).to_string())
angle_top = {}
for band in ["lfb", "hfb"]:
    for r in SM3:
        row = keep_proj[band].loc[r]
        angle_top[(band, r)] = bool(row["angle"] > row.drop("angle").max())
print("\nAngle above every other feature:", angle_top, "->", all(angle_top.values()))
ORDER = ["duration", "magnitude", "bimanual_ratio", "bimanual_overlap"]
order_holds = {}
for lab, regs in [("a, three sensorimotor regions", SM3), ("b, all eight regions", ajile.ROI_NAMES)]:
    m = pd.concat([keep_proj[b].loc[regs] for b in ["lfb", "hfb"]]).mean().sort_values(ascending=False)
    order_holds[lab[0]] = list(m.index[1:5]) == ORDER
    print(f"reading {lab}: ranking {[(f, round(v, 3)) for f, v in m.items()]}; second to fifth {list(m.index[1:5])}; "
          f"order holds {order_holds[lab[0]]}")
print("Retention over good electrodes, not projected (mean over electrodes, both bands):",
      G[[f"keep:{f}" for f in FEAT_ORDER]].mean().round(3).to_dict())
EOF
cat > c_6d1.py <<'EOF'
rows = []
for name, d, sb in [("main", G, None), ("code's selection by LFB R2", G, "lfb"), ("with bad electrodes", reg, None),
                    ("code's 80/20 split", reg82[reg82.good], None)]:
    for band in ["lfb", "hfb"]:
        ok = d[(d.band == (sb or band)) & (d.r2 > 0.05)][["subject", "electrode"]]
        x = d[d.band == band].merge(ok, on=["subject", "electrode"])["coef:angle"]
        rows.append({"variant": name, "band": band.upper(), "electrodes": len(x), "median_angle_coef": round(x.median(), 4),
                     "share_negative": round((x < 0).mean(), 3), "q25": round(x.quantile(.25), 4), "q75": round(x.quantile(.75), 4)})
a6d = pd.DataFrame(rows)
print(a6d.to_string(index=False))
m = a6d[a6d.variant == "main"].set_index("band").median_angle_coef
print(f"main: LFB median below 0 {m['LFB'] < 0}; HFB median above 0 {m['HFB'] > 0}")
print("Median angle coefficient by subject (main, electrodes with R2 > 0.05 in the band):")
print(G[G.r2 > 0.05].groupby(["subject", "band"])["coef:angle"].median().unstack().round(3).to_string())
EOF
cat > c_6d2.py <<'EOF'
res6d = {}
for name, d, sb in [("main", G, None), ("code's selection by LFB R2", G, "lfb"), ("with bad electrodes", reg, None),
                    ("code's 80/20 split", reg82[reg82.good], None)]:
    tab = {}
    for band in ["lfb", "hfb"]:
        va, n = ranked(d, band, "coef:", sb, fn=lambda v: np.median(np.abs(v)))
        vb, _ = ranked(d, band, "coef:", sb, fn=lambda v: abs(np.median(v)))
        tab[(band.upper(), "a: median |coef|", n)] = va.round(4)
        tab[(band.upper(), "b: |median coef|", n)] = vb.round(4)
        res6d[(name, band, "a")] = list(va.index[:2])
        res6d[(name, band, "b")] = list(vb.index[:2])
    print(f"{name}:\n{pd.DataFrame(tab).loc[FEAT_ORDER].to_string()}")
for k, v in res6d.items():
    print(f"  {k[0]}, {k[1].upper()}, reading {k[2]}: two largest {v}; angle and day: {set(v) == {'angle', 'day'}}")
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/harness.py <<'EOF'
import sys, time, pickle, os
os.environ["OMP_NUM_THREADS"] = "1"
import numpy as np, pandas as pd
from scipy import stats
sys.path.insert(0, "entries/000055-peterson-2021")
import ajile
SUBJECTS = sys.argv[1].split(",")
sessions, ecog = [], []
first_good, weights, roi_mats = {}, {}, {}
roi = ajile.roi_files()
for sub in SUBJECTS:
    d = pickle.load(open(f"{os.environ['TMPDIR']}/dev/s{sub}.pkl", "rb"))
    sessions += d["sessions"]; ecog += d["ecog"]; first_good[sub] = d["good"]
    roi_mats[sub] = ajile.read_roi_matrix(sub, roi); weights[sub] = ajile.roi_weights(roi_mats[sub], d["good"])
rows = []
for s, r in zip(sessions, ecog):
    e = s["events"].copy(); e["day"] = s["day"]; e["subject"] = s["subject"]
    e["ok"] = r["ok"]; e["q_all"] = r["q_all"]; e["q_hf"] = r["q_hf"]
    rows.append(e)
ev = pd.concat(rows, ignore_index=True)
ev = ev.rename(columns={"Reach_magnitude_px": "magnitude", "Reach_angle_degrees": "angle_file",
                        "Onset_speed_px_per_sec": "speed", "Speech_ratio": "speech",
                        "Bimanual_ratio": "bimanual_ratio", "Bimanual_overlap": "bimanual_overlap",
                        "Bimanual_class": "bimanual_class"})
ev["angle"] = ajile.fold_angle(-ev["angle_file"])
ev["tod_bin"] = np.clip((ev.start_time / 3600 // 8).astype(int), 0, 2)
thr = ev[ev.ok].groupby("subject").q_hf.agg(lambda v: v.mean() + 3 * v.std())
ev["keep_b"] = ev.ok & np.isfinite(ev.q_all) & (ev.q_all >= 0) & ~(ev.q_hf > ev.subject.map(thr))
for c in sys.argv[2].split(","):
    print(f"==================== {c}", flush=True)
    t0 = time.time()
    exec(open(f"{os.environ['TMPDIR']}/cells/{c}.py").read())
    print(f"[{time.time() - t0:.1f} s]")
EOF
cd $TMPDIR/dev && ../dev55/bin/python harness.py 05,07 r_setup,r_check,r_run,c_r2,c_6b,c_6c,c_e62,c_6d1,c_6d2 2>&1 | tail -150
```

```
supramarginal      0.268  0.210     0.243      0.280  0.400   0.448           0.432             0.231           0.268        0.217
superior temporal  0.413  0.225     0.229      0.316  0.225   0.457           0.483             0.341           0.276        0.247
middle temporal    0.274  0.232     0.231      0.157  0.274   0.563           0.437             0.219           0.390        0.193
inferior temporal  0.282  0.226     0.148      0.125  0.289   0.598           0.435             0.185           0.500        0.138
HFB: retention probability projected onto the regions (mean over subjects)
                   angle    day  duration  magnitude  speed  speech  bimanual_ratio  bimanual_overlap  bimanual_class  time_of_day
middle frontal     0.384  0.180     0.277      0.437  0.349   0.401           0.201             0.300           0.170        0.221
precentral         0.448  0.257     0.293      0.406  0.429   0.372           0.224             0.311           0.222        0.228
postcentral        0.511  0.298     0.334      0.274  0.401   0.393           0.330             0.255           0.315        0.218
inferior parietal  0.407  0.280     0.160      0.253  0.491   0.407           0.288             0.228           0.459        0.202
supramarginal      0.363  0.214     0.234      0.283  0.298   0.401           0.219             0.296           0.335        0.227
superior temporal  0.627  0.244     0.099      0.206  0.343   0.419           0.195             0.352           0.322        0.203
middle temporal    0.424  0.240     0.081      0.509  0.307   0.452           0.202             0.469           0.429        0.180
inferior temporal  0.310  0.226     0.083      0.549  0.363   0.438           0.146             0.537           0.459        0.154

Angle above every other feature: {('lfb', 'precentral'): True, ('lfb', 'postcentral'): True, ('lfb', 'inferior parietal'): False, ('hfb', 'precentral'): True, ('hfb', 'postcentral'): True, ('hfb', 'inferior parietal'): Fa
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && ../dev55/bin/python harness.py 05,07 r_setup,r_check,r_run,c_r2,c_6b 2>&1 | grep -v Warning | head -80
```

```
==================== r_setup
Features: ['duration', 'magnitude', 'speed', 'angle', 'speech', 'bimanual_ratio', 'bimanual_overlap', 'bimanual_class', 'day', 'time_of_day']
Per subject: events, design columns, electrodes (good), test events per split at 90/10 and 80/20:
  S05: 263 events, 14 columns, 106 electrodes (104 good), 24 and 51 test events
  S07: 784 events, 16 columns, 64 electrodes (63 good), 75 and 155 test events
[0.0 s]
==================== r_check
40 fits: largest coefficient difference 2.41e-04, largest withheld R2 difference 8.24e-05 (median 2.2e-06)
[0.2 s]
==================== r_run
main (90/10, band mean, all electrodes): 340 full models, 8 with refits, 0.1 min; 80/20 (good electrodes): 334 and 12, 0.1 min; band median: 334 full models; total 0.3 min
main: models with nothing to fit (flat power) 0, of which good 0; models with no feature selected 5
80/20: models with nothing to fit (flat power) 0, of which good 0; models with no feature selected 5
median: models with nothing to fit (flat power) 0, of which good 0; models with no feature selected 2
[18.7 s]
==================== c_r2
                                 variant band  models  max_R2      at  median_R2  share_R2_over_0.05  min_R2
main (90/10, band mean, good electrodes)  LFB     167   0.046 S07 e26    -0.0331               0.000  -0.094
main (90/10, band mean, good electrodes)  HFB     167   0.181 S07 e10    -0.0348               0.024  -0.093
                      code's 80/20 split  LFB     167   0.050 S07 e26    -0.0142               0.000  -0.071
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && sed -i 's/top2\[(name, band)\] = list(v.index\[:2\])/top2[(name, band)] = list(v.dropna().index[:2])/' c_6c.py && sed -i 's/res6d\[(name, band, "a")\] = list(va.index\[:2\])/res6d[(name, band, "a")] = list(va.dropna().index[:2])/; s/res6d\[(name, band, "b")\] = list(vb.index\[:2\])/res6d[(name, band, "b")] = list(vb.dropna().index[:2])/' c_6d2.py && grep -n "dropna().index" c_6c.py c_6d2.py
cat > s_cols.py <<'EOF'
# Columns of the reaches table in every file: is any event marked as a false positive or verified?
rc = pd.Series({f"S{s['subject']} day {s['day']}": ", ".join(s["reach_columns"]) for s in sessions})
for cols_, files in rc.groupby(rc).groups.items():
    print(f"{len(files)} files: {cols_}")
print("Any column naming false positives, verification or removal:",
      [c for s in sessions for c in s["reach_columns"] if any(w in c.lower() for w in ["false", "verif", "remov", "valid", "fp"])])
EOF
cat > s_groups.py <<'EOF'
# Electrode groups and their descriptions in each subject's first file, beside the data
# descriptor's Table 2 (Peterson et al. 2022, Sci Data 9:184, doi:10.1038/s41597-022-01280-y,
# "Surface electrodes: # good/total", "Depth electrodes: # good/total"; totals given here).
DESC_T2 = {"01": (86, 8), "02": (70, 16), "03": (80, 16), "04": (84, 0), "05": (106, 0), "06": (80, 0),
           "07": (64, 0), "08": (92, 0), "09": (98, 28), "10": (86, 40), "11": (106, 0), "12": (92, 32)}
for sub in SUBJECTS:
    s = [x for x in sessions if x["subject"] == sub][0]
    n = s["electrodes"].group_name.value_counts()
    print(f"S{sub} ({len(s['electrodes'])} electrodes; descriptor {DESC_T2[sub][0]} surface + {DESC_T2[sub][1]} depth): "
          + "; ".join(f"{g} {int(n.get(g, 0))} '{d}'" for g, d in s["group_desc"].items()))
EOF
cat > s_kde.py <<'EOF'
# Sensitivity, not the criterion: how far a Gaussian KDE without boundary correction pulls peaks
# in from the ends of a bounded range. Synthetic folded angles whose density peaks exactly at
# +-90 (90 minus a half-normal of SD 25 degrees, either sign), and the same KDE with the data
# reflected at -90 and +90 (a standard boundary correction).
rng_kde = np.random.default_rng(2)
def kde_peaks(a, reflect=False):
    data = np.r_[a, -180 - a, 180 - a] if reflect else a
    kde = gaussian_kde(data, bw_method="scott")
    if reflect:
        kde.set_bandwidth(kde.factor * (len(data) / len(a)) ** 0.2)   # Scott's bandwidth of the original n
    dens = kde(grid)
    peaks = [i for i in range(1, len(grid) - 1) if dens[i] > dens[i - 1] and dens[i] >= dens[i + 1]]
    peaks += [i for i, j in [(0, 1), (len(grid) - 1, len(grid) - 2)] if dens[i] > dens[j]]
    return sorted(np.round(grid[sorted(peaks, key=lambda i: -dens[i])[:2]], 1))
for n in [250, 900]:
    syn = np.sign(rng_kde.random(n) - 0.5) * (90 - np.abs(rng_kde.normal(0, 25, n)))
    syn = np.clip(syn, -90, 90)
    print(f"synthetic, n = {n}: Scott KDE peaks {kde_peaks(syn)}; reflected KDE peaks {kde_peaks(syn, True)}")
rows = []
for sub, g in list(E.groupby("subject")) + [("pooled", E)]:
    pk = kde_peaks(g.angle.values, True)
    rows.append({"subject": sub, "criterion_KDE_peaks": kde_peaks(g.angle.values), "reflected_KDE_peaks": pk,
                 "reflected_within_15_of_pm90": len(pk) == 2 and pk[0] <= -75 and pk[1] >= 75})
kr = pd.DataFrame(rows)
print(kr.to_string(index=False))
print("Reflected KDE: two highest maxima within 15 degrees of -90 and +90 in",
      int(kr[kr.subject != "pooled"].reflected_within_15_of_pm90.sum()), "of 12 subjects; pooled",
      bool(kr[kr.subject == "pooled"].reflected_within_15_of_pm90.iloc[0]))
EOF
cat > s_seed.py <<'EOF'
# Seed stability of the bootstrap mask: the same masks with ten other seeds.
rows = []
for seed in range(10):
    m_ = np.stack([ajile.boot_sig_mask(np.moveaxis(subj_c[:, r], 0, -1), base_i, np.random.default_rng(100 + seed))
                   for r in range(8)])
    nl = [int((m_[r][LF34][:, t_a] < 0).sum()) for r in range(8)]
    ph = [int((m_[r][HF50][:, t_a] > 0).sum()) for r in range(8)]
    pattern = [bool(m_[r][LF34][:, t_a].mean() < 0 and m_[r][HF50][:, t_a].mean() > 0) for r in range(8)]
    rows.append({"seed": 100 + seed, **{f"LF-:{n[:12]}": v for n, v in zip(ajile.ROI_NAMES, nl)},
                 **{f"HF+:{n[:12]}": v for n, v in zip(ajile.ROI_NAMES, ph)},
                 "a_LF_regions": sum(v > 0 for v in nl), "a_HF_regions": sum(v > 0 for v in ph),
                 "b_LF_per_f": round(sum(nl) / len(LF34), 2), "b_HF_per_f": round(sum(ph) / len(HF50), 2),
                 "fig3_pattern_in_named_3": sum(pattern[REG[n]] for n in named)})
sd = pd.DataFrame(rows)
print(sd.T.to_string())
print("Reading a, low-frequency regions more than high-frequency in", int((sd.a_LF_regions > sd.a_HF_regions).sum()),
      "of 10 seeds, equal in", int((sd.a_LF_regions == sd.a_HF_regions).sum()), "; reading b, low larger in",
      int((sd.b_LF_per_f > sd.b_HF_per_f).sum()), "of 10; supramarginal and superior temporal low-frequency decreases in",
      int(((sd["LF-:supramargina"] > 0) & (sd["LF-:superior tem"] > 0)).sum()), "of 10; fig3 pattern in all 3 named regions in",
      int((sd.fig3_pattern_in_named_3 == 3).sum()), "of 10")
EOF
echo; date -u
```

```
c_6c.py:18:        top2[(name, band)] = list(v.dropna().index[:2])
c_6d2.py:10:        res6d[(name, band, "a")] = list(va.dropna().index[:2])
c_6d2.py:11:        res6d[(name, band, "b")] = list(vb.dropna().index[:2])

Sat Nov  7 06:36:11 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev && ../dev55/bin/python -c "
import sys,time; sys.path.insert(0,'entries/000055-peterson-2021')
import numpy as np, ajile
x=np.random.default_rng(0).normal(size=(25,91,12)); bi=ajile._tidx(-1.5,-1)
t=time.time(); ajile.boot_sig_mask(x,bi,np.random.default_rng(1)); print('one region',time.time()-t)
" ; cat > kdetest.py <<'EOF'
import numpy as np, pandas as pd
from scipy.stats import gaussian_kde
grid = np.linspace(-90, 90, 361)
E = pd.DataFrame({"subject": np.repeat(["01", "02"], 300), "angle": np.random.default_rng(0).uniform(-90, 90, 600)})
exec(open("../cells/s_kde.py").read())
EOF
../dev55/bin/python kdetest.py
```

```
one region 0.3784515857696533
synthetic, n = 250: Scott KDE peaks [np.float64(-72.5), np.float64(70.0)]; reflected KDE peaks [np.float64(-90.0), np.float64(89.5)]
synthetic, n = 900: Scott KDE peaks [np.float64(-73.5), np.float64(74.0)]; reflected KDE peaks [np.float64(-90.0), np.float64(90.0)]
subject criterion_KDE_peaks reflected_KDE_peaks  reflected_within_15_of_pm90
     01         [1.0, 61.0]              [90.0]                        False
     02       [-48.5, 17.5]              [18.5]                        False
 pooled        [15.0, 56.0]              [90.0]                        False
Reflected KDE: two highest maxima within 15 degrees of -90 and +90 in 0 of 12 subjects; pooled False
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && sed -i 's/    return sorted(np.round(grid\[sorted(peaks, key=lambda i: -dens\[i\])\[:2\]\], 1))/    return sorted(float(v) for v in np.round(grid[sorted(peaks, key=lambda i: -dens[i])[:2]], 1))/' s_kde.py && grep -n "return sorted" s_kde.py; cd entries/000055-peterson-2021; grep -n "SUBJECTS =" reproduce_peterson_2021.ipynb
```

```
14:    return sorted(float(v) for v in np.round(grid[sorted(peaks, key=lambda i: -dens[i])[:2]], 1))
73:    "SUBJECTS = [f\"{i:02d}\" for i in range(1, 13)]"
```

**Agent calls Bash**

```bash
cp reproduce_peterson_2021.ipynb $TMPDIR/nb_backup.ipynb && python - <<'EOF'
import json, os
C = os.environ["TMPDIR"] + "/cells/"
nb = json.load(open("reproduce_peterson_2021.ipynb"))
cells = nb["cells"]
def code(src, tag=None):
    return {"cell_type": "code", "execution_count": None, "metadata": {"tags": [tag]} if tag else {},
            "outputs": [], "source": src.rstrip("\n").splitlines(keepends=True)}
def md(src):
    return {"cell_type": "markdown", "metadata": {}, "source": src.rstrip("\n").splitlines(keepends=True)}
rd = lambda n: open(C + n + ".py").read()
src = lambda i: "".join(cells[i]["source"])
assert src(81).startswith("## Regression claims") and src(82).startswith("rng_fig6") and src(83).startswith("**Result: blocked (too large)")
assert src(61).startswith("neg_lf") and src(39).startswith("fig, axes") and src(29).startswith("rows = []") and "info = pd.DataFrame" in src(5)
# cohort: descriptor variant
cells[29]["source"] = (src(29).rstrip("\n") + '''
d2 = pd.DataFrame(DESC_T2, index=["surface", "depth"]).T
print("Variant, the data descriptor's Table 2 counts: surface mean", round(d2.surface.mean(), 1), "+-",
      round(d2.surface.std(), 1), "; subjects with depth electrodes", int((d2.depth > 0).sum()), ", their mean",
      round(d2[d2.depth > 0].depth.mean(), 1), "+-", round(d2[d2.depth > 0].depth.std(), 1))
print("Subjects whose file counts differ from the descriptor's:",
      {s: (int(r.surface), int(r.depth), DESC_T2[s]) for s, r in coh.set_index("subject").iterrows() if (r.surface, r.depth) != DESC_T2[s]})
''').splitlines(keepends=True)
reg_md = md("""## Regression claims (Figure 6 and Extended Data Figure 6-2)

The method is the claims file's opening comment: per subject, good electrode and band, forward
selection by OLS adjusted R2 over the design columns, then 200 day-balanced splits (90/10, Methods)
with a Huber fit of the full model and, for the Delta R2 of each selected feature, a refit with that
feature shuffled among the training events. The fits minimise sklearn's `HuberRegressor` objective
(the code's model), many at a time (helper `huber_fit`); the first cell compares them with sklearn.
Delta R2 refits are run where the full model's R2 exceeds 0.05 in either band, the electrodes Figure
6c-d show (legend); elsewhere only R2, coefficients and selection are used. The variants the claims
name are run beside the main analysis: the code's 80/20 split, the code's band median, the code's
Delta R2 (refit scored on shuffled test events), the code's selection of electrodes by LFB R2, and
the code's inclusion of bad electrodes. The code's log(x + 1) transforms are not run as a variant.""")
def claim_md(cid, quote):
    return md(f"## Claim `{cid}`\n\n> {quote}")
new_reg = [reg_md, code(rd("r_setup")), code(rd("r_check"), "sanity"), code(rd("r_run")),
    claim_md("fig6-r2-at-most-025", "All regression models explain at most 25% of the variance of withheld single-event power."),
    code(rd("c_r2"), "claim:fig6-r2-at-most-025"), md("**Result: TODO**"),
    claim_md("fig6b-best-models-sensorimotor", "Regression models with the highest withheld R2 are mainly at electrodes over frontoparietal\n> sensorimotor areas, for both bands."),
    code(rd("c_6b"), "claim:fig6b-best-models-sensorimotor"), md("**Result: TODO**"),
    claim_md("fig6c-angle-and-day-most-informative", "Reach angle and day of recording are the most informative features for single-event power,\n> especially for low-frequency power."),
    code(rd("c_6c"), "claim:fig6c-angle-and-day-most-informative"), md("**Result: TODO**"),
    claim_md("extfig6-2-angle-most-retained", "Reach angle is the feature most often retained by forward selection in sensorimotor regions,\n> followed by reach duration, reach magnitude, bimanual ratio and bimanual overlap."),
    code(rd("c_e62"), "claim:extfig6-2-angle-most-retained"), md("**Result: TODO**"),
    claim_md("fig6d-upward-reaches-enhance-pattern", "Upward reaches are associated with lower low-frequency power and higher high-frequency power,\n> that is, a larger version of the average movement response."),
    code(rd("c_6d1"), "claim:fig6d-upward-reaches-enhance-pattern"), md("**Result: TODO**"),
    claim_md("fig6d-angle-and-day-largest-coefficients", "Reach angle and day of recording have the largest coefficient magnitudes among the features,\n> and the SD of the recording-day coefficients is large."),
    code(rd("c_6d2"), "claim:fig6d-angle-and-day-largest-coefficients"), md("**Result: TODO**")]
out = cells[:6] + [code(rd("s_cols"), "sanity"), code(rd("s_groups"), "sanity")] + cells[6:40] \
    + [code(rd("s_kde"), "claim:fig2-reach-shape")] + cells[40:62] + [code(rd("s_seed"), "claim:fig3-lfb-more-widespread")] \
    + cells[62:81] + new_reg + cells[84:]
nb["cells"] = out
json.dump(nb, open("reproduce_peterson_2021.ipynb", "w"), indent=1, ensure_ascii=False)
open("reproduce_peterson_2021.ipynb", "a").write("\n")
print(len(out))
EOF
git diff --stat
```

```
109
 entries/000055-peterson-2021/ajile.py              | 277 +++++++---
 .../reproduce_peterson_2021.ipynb                  | 580 +++++++++++++++++++--
 tools/build_site.py                                |  15 +
 tools/runner/run_requests.py                       |   4 +-
 tools/site_assets/app.css                          |   3 +
 5 files changed, 784 insertions(+), 95 deletions(-)
```

**Agent calls Bash**

```bash
cd  && python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -20
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python -c "
import nbformat, uuid
nb = nbformat.read('reproduce_peterson_2021.ipynb', as_version=4)
for c in nb.cells:
    if 'id' not in c: c['id'] = uuid.uuid4().hex[:8]
nbformat.write(nb, 'reproduce_peterson_2021.ipynb')
" && date -u && cd ../.. && time python tools/entry.py all entries/000055-peterson-2021 2>&1 | grep -v Warning | tail -30; date -u
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Sat Nov  7 06:37:03 UTC 2026
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (1594 s)

real	26m42.926s
user	61m9.071s
sys	7m10.011s
Sat Nov  7 07:03:46 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  s=''.join(c['source'])
  if any(k in s for k in ['reach_columns','DESC_T2 =','d2 = pd.DataFrame','kde_peaks','Seed stability','LOAD-ECOG-END']):
    print('=====',i, s[:60])
    for o in c['outputs']:
      print(o.get('text','') if 'text' in o else o.get('data',{}).get('text/plain',''))
"
```

```
===== 6 # Columns of the reaches table in every file: is any event m
['55 files: start_time, stop_time, Reach_magnitude_px, Reach_angle_degrees, Onset_speed_px_per_sec, Speech_ratio, Bimanual_ratio, Bimanual_overlap, Bimanual_class\n', 'Any column naming false positives, verification or removal: []\n']
===== 7 # Electrode groups and their descriptions in each subject's 
["S01 (94 electrodes; descriptor 86 surface + 8 depth): ECG 0 'electrocardiogram'; EOG 0 'electrooculogram'; GRID 64 'ECoG grid'; LAT 6 'left anterior temporal'; LID 8 'left insular depth'; LMT 4 'left medial temporal'; LPT 6 'left posterior temporal'; LTO 6 'left temporal occipital'\n", "S02 (86 electrodes; descriptor 70 surface + 16 depth): GRID 64 'ECoG grid'; RDA 8 'right depth anterior'; RDP 8 'right depth posterior'; RST 6 'right temporal'\n", "S03 (96 electrodes; descriptor 80 surface + 16 depth): GRID 64 'ECoG grid'; LAD 8 'left anterior depth'; LAT 8 'left anterior temporal'; LMT 8 'left medial temporal'; LPD 8 'left posterior depth'\n", "S04 (84 electrodes; descriptor 84 surface + 0 depth): GRID 64 'ECoG grid'; RAT 6 'right anterior temporal'; RMT 6 'right medial temporal'; RPT 8 'right posterior temporal'\n", "S05 (106 electrodes; descriptor 106 surface + 0 depth): GRID 64 'ECoG grid'; RAT 6 'right anterior temporal'; RF 16 'right frontal'; RMT 6 'right medial temporal'; RPT 8 'right posterior temporal'; RTP 6 'right temporal pole'\n", "S06 (80 electrodes; descriptor 80 surface + 0 depth): L Grid 64 'Left ECoG grid'; LO 16 'left occipital'\n", "S07 (64 electrodes; descriptor 64 surface + 0 depth): RFGRID 64 'Right Frontal ECoG grid'\n", "S08 (92 electrodes; descriptor 92 surface + 0 depth): GRID 64 'ECoG grid'; RAT 6 'right anterior temporal'; RMT 6 'right medial temporal'; ROF 8 'right orbitofrontal'; RPT 8 'right posterior temporal'\n", "S09 (126 electrodes; descriptor 98 surface + 28 depth): Grid 64 'ECoG grid'; LAT 6 'left anterior temporal'; LF 8 'left frontal'; LID 13 'left insular d
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
st=[i for i,c in enumerate(nb['cells']) if ''.join(c['source']).startswith('## Regression claims')][0]
for i,c in enumerate(nb['cells'][st:], st):
  if c['cell_type']!='code': continue
  print('=====',i, ''.join(c['source'])[:50])
  for o in c['outputs']:
    t = o.get('text') if 'text' in o else o.get('data',{}).get('text/plain','')
    print(''.join(t) if isinstance(t,list) else t)
" | grep -v "Warning\|_methods\|return _\|ret = "
```

```
===== 86 # Regression inputs per subject: the kept events (
Features: ['duration', 'magnitude', 'speed', 'angle', 'speech', 'bimanual_ratio', 'bimanual_overlap', 'bimanual_class', 'day', 'time_of_day']
Per subject: events, design columns, electrodes (good), test events per split at 90/10 and 80/20:
  S01: 732 events, 15 columns, 94 electrodes (85 good), 72 and 144 test events
  S02: 298 events, 15 columns, 86 electrodes (85 good), 28 and 56 test events
  S03: 637 events, 15 columns, 96 electrodes (79 good), 60 and 124 test events
  S04: 412 events, 16 columns, 84 electrodes (67 good), 40 and 80 test events
  S05: 263 events, 14 columns, 106 electrodes (104 good), 24 and 51 test events
  S06: 911 events, 16 columns, 80 electrodes (70 good), 90 and 180 test events
  S07: 784 events, 16 columns, 64 electrodes (63 good), 75 and 155 test events
  S08: 947 events, 16 columns, 92 electrodes (83 good), 90 and 185 test events
  S09: 211 events, 16 columns, 126 electrodes (124 good), 20 and 40 test events
  S10: 746 events, 16 columns, 126 electrodes (121 good), 70 and 145 test events
  S11: 968 events, 16 columns, 106 electrodes (103 good), 95 and 190 test events
  S12: 979 events, 16 columns, 124 electrodes (112 good), 95 and 195 test events

===== 87 # The batched Huber fit (helper huber_fit) against
240 fits: largest coefficient difference 1.16e-03, largest withheld R2 difference 4.40e-05 (median 1.9e-06)

===== 88 # The models. Stage 1 fits the full model for ever
[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
ls questions/ | grep 55; head -40 questions/000005.yaml; grep -n "verifications" -A40 docs/*.md | grep -v protocol | head -60
```

```
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
  answer: >-
    The recording's sampling rate, not 1 ms bins. The Methods give 1 ms bins for spike PSTHs
    only ("All touch-spike PSTHs were constructed with a bin size of 1 ms"), and the paper's Vm
    latencies are not on a 1 ms grid. The FS onset has "median, 4.2 ms, n = 7 neurons" and the E
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; grep -n "verifications" -A30 schemas/*attempt* 2>/dev/null | head -80; ls schemas 2>/dev/null
```

```
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
verifications:
- date: '2026-10-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier queried the archive metadata and tested
    helper functions on synthetic inputs. Its report had no attempt record and gave its own outcome for
    each claim; all 31 agree with the record.
  results:
  - claim: unit-counts
    agrees: true
    outcome: partially_reproduced
    reason: GC 609 is inside 527 to 645, but MC 568 is outside 450 to 550.
    response: No change needed.
  - claim: first-stage-labels
    agrees: true
    outcome: partially_reproduced
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 360,420p schemas/attempt.schema.json; grep -n '"proposed"' -A25 schemas/attempt.schema.json | head -30
```

```
"results": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": [
                "claim",
                "agrees"
              ],
              "properties": {
                "claim": {
                  "type": "string"
                },
                "agrees": {
                  "type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
import json
nb = json.load(open("reproduce_peterson_2021.ipynb"))
cells = nb["cells"]
S = lambda c: "".join(c["source"])
def setsrc(c, s): c["source"] = s.rstrip("\n").splitlines(keepends=True)
def find(prefix, after=None):
    hits = [i for i, c in enumerate(cells) if S(c).startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]
R = {
"fig6-r2-at-most-025": "**Result: reproduced.** The largest split-averaged full-model withheld R2 over the 1096 good electrodes of the 12 subjects and both bands is 0.189 (HFB, S04), at most 0.275; the largest in LFB is 0.149 (S01). With the code's 80/20 split it is 0.192, with the code's band median 0.203, and with bad electrodes included 0.189. The median R2 is -0.014 in both bands, and 2.0% (LFB) and 1.3% (HFB) of good electrodes exceed 0.05. For reference only, the R2 stored in the files reach 0.149 and 0.255, and their Spearman correlation with the values here is 0.718 and 0.643.",
"fig6b-best-models-sensorimotor": "**Result: reproduced.** Under reading a, all 22 good electrodes with LFB R2 > 0.05 and 13 of 14 (0.929) with HFB R2 > 0.05 are assigned to the five frontoparietal regions, and the median R2 of precentral, postcentral and inferior parietal electrodes is above that of temporal electrodes in both bands (-0.0097 against -0.0158 in LFB, -0.0117 against -0.0147 in HFB). Under reading b, the three regions with the highest projected R2 are precentral, postcentral and inferior parietal in both bands. Few electrodes exceed 0.05, from 4 subjects in LFB and 6 in HFB.",
"fig6c-angle-and-day-most-informative": "**Result: reproduced.** Over the 22 good electrodes with LFB R2 > 0.05, reach angle (median Delta R2 0.066) and recording day (0.017) have the two largest median Delta R2; time of day follows (0.0017) and the seven other features have a median of 0. In HFB (14 electrodes) day (0.068) and angle (0.033) are the two largest. Every variant (the code's Delta R2, selection by LFB R2, the 80/20 split, bad electrodes included) gives angle and day as the two largest in both bands.",
"extfig6-2-angle-most-retained": "**Result: partially reproduced.** Reach angle has the highest projected retention probability in precentral, postcentral and inferior parietal in both bands (0.448 to 0.679, against at most 0.400 for any other feature in these regions). The order of the next four does not hold: averaged over the three sensorimotor regions and both bands, the second to fifth features are onset speed, speech ratio, reach magnitude and bimanual ratio, and over all eight regions speech ratio, onset speed, reach magnitude and bimanual ratio; reach duration is sixth and seventh. The second to tenth features lie close together (0.202 to 0.357).",
"fig6d-upward-reaches-enhance-pattern": "**Result: reproduced.** Over good electrodes with R2 > 0.05 in the band, the median reach-angle coefficient is -1.027 in LFB (22 electrodes, 95.5% negative) and 0.535 in HFB (14 electrodes, none negative). The code's selection by LFB R2 gives -1.027 and 0.202, bad electrodes included -0.815 and 0.515, and the 80/20 split -0.973 and 0.540, so the signs hold in every variant. By subject the LFB medians are -1.353 to 0 (4 subjects) and the HFB medians 0 to 0.730 (6 subjects).",
"fig6d-angle-and-day-largest-coefficients": "**Result: reproduced.** Over good electrodes with R2 > 0.05, reach angle and the SD of the recording-day coefficients have the two largest values under both readings in both bands: in LFB angle 1.027 and day 0.660 (then time of day 0.188), in HFB day 0.733 and angle 0.535 (then reach magnitude 0.231 under reading a). The code's selection by LFB R2, the inclusion of bad electrodes and the 80/20 split give the same two in both bands and readings. The day SD is the second largest value in LFB and the largest in HFB.",
}
for cid, text in R.items():
    i = find(f"## Claim `{cid}`")
    assert S(cells[i + 2]) == "**Result: TODO**"
    setsrc(cells[i + 2], text)
i = find("**Result: partially reproduced.** More than half of the reaches")
setsrc(cells[i], S(cells[i]) + " With a KDE reflected at -90 and +90 (a sensitivity output, not the criterion), the two highest maxima lie within 15 degrees of +-90 pooled and in 6 of 12 subjects, not more than half. On synthetic angles whose density peaks at +-90 the criterion's KDE puts the peaks at -73.5 to 74.0 degrees, so part of the shortfall comes from the KDE's boundary bias.")
i = find("**Result: blocked (methods underspecified).**")
setsrc(cells[i], S(cells[i]) + " With ten other bootstrap seeds, reading a gives 7 against 7 regions every time and reading b 35.0 to 35.6 against 25.5 to 25.8 bins per frequency, so the readings disagree under every seed; supramarginal and superior temporal keep their low-frequency decreases and the pattern of fig3-group-lfb-decrease-hfb-increase holds in the three named regions under every seed.")
i = find("**Result: partially reproduced.** 12 subjects")
setsrc(cells[i], S(cells[i]) + " The data descriptor's Table 2 gives S10 86 surface and 40 depth electrodes and S11 106 surface and none, where the group descriptions in the files give 78 and 48, and 88 and 18. With the descriptor's counts the surface mean is 87.0 +- 12.9 and six subjects have depth electrodes (23.3 +- 12.0), still not five.")
i = find("**Result: not reproduced.** The dataset holds 211 to 996")
setsrc(cells[i], S(cells[i]) + " The reaches table has the same nine columns in all 55 files and none marks an event as a false positive or as verified, so reading b cannot drop the false positives: the outcome rests on reading a and on reading b without that step.")
i = find("The files hold 12 subjects and 55 subject-days")
setsrc(cells[i], S(cells[i]) + "\n\nThe reaches table has the same nine columns in every file, and none marks false positives or\nverified events. The electrode groups whose description says depth are listed above beside the\ndata descriptor's Table 2; S10 and S11 are counted differently there (see claim `cohort`).")
# header
i = 0
s = S(cells[0])
old = "| fig6b-best-models-sensorimotor, fig6-r2-at-most-025, fig6c-angle-and-day-most-informative, extfig6-2-angle-most-retained, fig6d-upward-reaches-enhance-pattern, fig6d-angle-and-day-largest-coefficients | blocked, too large (timed below) |"
assert old in s
s = s.replace(old, "| fig6b-best-models-sensorimotor, fig6-r2-at-most-025, fig6c-angle-and-day-most-informative, extfig6-2-angle-most-retained, fig6d-upward-reaches-enhance-pattern, fig6d-angle-and-day-largest-coefficients | tested |")
s = s.replace("that step takes\nabout half an hour.", "that step takes\nabout 22 minutes. The regression models take a few minutes.")
setsrc(cells[0], s)
# summary
i = find("## Summary")
s = S(cells[i])
old = "| six regression claims (Figure 6, Extended Data Figure 6-2) | blocked, too large |"
assert old in s
s = s.replace(old, """| fig6-r2-at-most-025 | reproduced (largest R2 0.189) |
| fig6b-best-models-sensorimotor | reproduced |
| fig6c-angle-and-day-most-informative | reproduced |
| extfig6-2-angle-most-retained | partially reproduced (angle first; the order of the next four differs) |
| fig6d-upward-reaches-enhance-pattern | reproduced |
| fig6d-angle-and-day-largest-coefficients | reproduced |""")
old = "The regression claims were not run."
assert old in s
s = s.replace(old, "The regression models minimise the objective of sklearn's HuberRegressor by a batched Newton method, which matches sklearn's fits to 4.4e-05 in withheld R2; Delta R2 refits are run only at electrodes whose full-model R2 exceeds 0.05, the electrodes Figure 6c-d show. The code's log(x + 1) transforms of reach magnitude and onset speed are not run as a variant. In the code's Delta R2 variant the refit is shared with the main version and only the test events are shuffled.")
setsrc(cells[i], s)
json.dump(nb, open("reproduce_peterson_2021.ipynb", "w"), indent=1, ensure_ascii=False)
open("reproduce_peterson_2021.ipynb", "a").write("\n")
EOF
grep -c TODO reproduce_peterson_2021.ipynb; git diff --stat reproduce_peterson_2021.ipynb
```

```
0
 .../reproduce_peterson_2021.ipynb                  | 633 +++++++++++++++++++--
 1 file changed, 593 insertions(+), 40 deletions(-)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p = "reproduce_peterson_2021.ipynb"
s = open(p).read()
old = "the criterion's KDE puts the peaks at -73.5 to 74.0 degrees"
assert s.count(old) == 1
s = s.replace(old, "the criterion's KDE puts the peaks at -72.5 and 70.0 (n = 250) and at -73.5 and 74.0 degrees (n = 900)")
open(p, "w").write(s)
EOF
grep -n "pandas\|Time of day: the files" ajile.py | head
```

```
51:- Time of day: the files start at midnight local time (data descriptor, Methods: "each file
63:import pandas as pd
428:    binary features, z-scored over the subject's events with pandas' SD (code,
```

**Agent calls Read**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "offset": 48,
 "limit": 10
}
```

```
48	- The wrist traces of Extended Data Figure 2-1 use the code's window (config
49	  `metadata_pos_min_time = -1.5`, `baseline_vals_movement = [-1.5, -1]`) and a 1.5 s end,
50	  as the claims file says.
51	- Time of day: the files start at midnight local time (data descriptor, Methods: "each file
52	  contained data from one entire 24-hour recording day that started and ended at midnight"),
53	  so the hour of an event is its start time in the file divided by 3600.
54	"""
55	
56	from __future__ import annotations
57
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "  so the hour of an event is its start time in the file divided by 3600.\n\"\"\"",
 "new_string": "  so the hour of an event is its start time in the file divided by 3600.\n- Regression (claims file's opening comment; code regression_utils.py): forward selection over\n  design columns by OLS adjusted R2 (`_forward_selected_new`), unselected columns set to 0,\n  Huber regression with sklearn's HuberRegressor defaults over 200 day-balanced splits\n  (`train_test_split_day_balance`), Delta R2 by refitting with a feature shuffled, the SD of the\n  day and time-of-day one-hot coefficients, and the selection probability (`feat_select_prob`).\n  The Huber fits solve sklearn's objective by a batched Newton method (`huber_fit`), a standard\n  choice of solver that reaches the same minimum; the notebook compares it with sklearn. The\n  time-of-day bins are 0-8, 8-16 and 16-24 h without overlap (the code's bins share their edges,\n  which no event time hits exactly). The code tests whether a day or time-of-day feature was\n  selected by looking at one fixed column; here a feature counts as selected when any of its\n  columns is.\n\"\"\""
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully.
```

**Agent calls Bash**

```bash
cat README.md
```

```
# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds 55 days
of ECoG and pose from 12 people in clinical epilepsy monitoring, with their wrist movement events and
event features. Region power uses the paper's projection matrices from
[Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days match Table 2 (link) | Reproduced |
| The Figshare projection matrices match the dataset's electrodes (link) | Reproduced |
| Cohort and electrode counts | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration, magnitude and bimodal angle | Partially reproduced |
| Bimanual features skewed to unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations (Extended Data Figure 2-2) | Partially reproduced |
| Events by day and in waking hours | Partially reproduced |
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p = "README.md"
s = open(p).read()
s = s.replace("| Regression models (Figure 6, Extended Data Figure 6-2), six claims | Blocked: too large |",
"""| All regression R2 at most 0.25 | Reproduced |
| Best models over frontoparietal sensorimotor areas | Reproduced |
| Reach angle and day most informative (Delta R2) | Reproduced |
| Reach angle most often retained, then four features in order | Partially reproduced |
| Upward reaches enhance the movement pattern | Reproduced |
| Reach angle and day have the largest coefficients | Reproduced |""")
s = s.replace("The notebook reads about 8000 ECoG segments and takes about half an hour.",
              "The notebook reads about 8000 ECoG segments and takes about half an hour; the regression models of\nFigure 6 take a few minutes, as `ajile.huber_fit` solves many Huber fits at once.")
open(p, "w").write(s)
p = "entry.yaml"
s = open(p).read()
s = s.replace(""" regions, and the variation of precentral band power across subjects and recording days. The
  regression models of Figure 6 were too large to run here.""", """ regions, the variation of precentral band power across subjects and recording days, and the
  regression of single-event band power on the behavioural features (Figure 6).""")
s = s.replace("runtime_minutes: 35", "runtime_minutes: 30")
open(p, "w").write(s)
EOF
git diff entry.yaml | head; date -u
```

```
diff --git a/entries/000055-peterson-2021/entry.yaml b/entries/000055-peterson-2021/entry.yaml
index 56fd3ea784..0cba7a932b 100644
--- a/entries/000055-peterson-2021/entry.yaml
+++ b/entries/000055-peterson-2021/entry.yaml
@@ -6,13 +6,13 @@ description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021)
   (AJILE12), which holds 55 days of ECoG and pose from 12 people in clinical epilepsy monitoring, with
   their wrist movement events and event features. It compares the behavioural features across
   subjects and days, the group and per-subject movement-related spectral power in eight cortical
-  regions, and the variation of precentral band power across subjects and recording days. The
-  regression models of Figure 6 were too large to run here.
Sat Nov  7 07:05:28 UTC 2026
```

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
p = "attempts/000055-peterson-2021-01.yaml"
s = open(p).read()
i = s.index("- claim: fig6b-best-models-sensorimotor")
j = s.index("findings:")
new = '''- claim: fig6-r2-at-most-025
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6-r2-at-most-025
  assumed: true
  measured:
  - 0.189
  notes: The largest split-averaged full-model withheld R2 over the 1096 good electrodes of the 12
    subjects and both bands is 0.189 (HFB, S04), within 0.275; the largest in LFB is 0.149 (S01). The
    code's 80/20 split gives 0.192, the code's band median 0.203, and bad electrodes included 0.189.
    The median R2 is -0.014 in both bands, and 22 (LFB) and 14 (HFB) good electrodes exceed 0.05. For
    reference only, the R2 stored in the files reach 0.149 and 0.255; their Spearman correlation with
    the R2 here is 0.718 (LFB) and 0.643 (HFB) over 1088 good electrodes.
  deviations:
  - The Huber fits minimise the objective of sklearn's HuberRegressor (the code's model, defaults) by
    a batched Newton method with a line search, many problems at once (helper huber_fit). On 240 fits
    the coefficients differ from sklearn's by at most 1.16e-03 and the withheld R2 by at most 4.4e-05.
  - Delta R2 refits are run only at electrodes whose full-model R2 exceeds 0.05 in either band (86
    models in the main analysis, 84 with the 80/20 split), as every criterion uses Delta R2 only there.
  - In the code's Delta R2 variant the refit is shared with the Methods' version and the feature is
    shuffled among the test events before scoring; the code shuffles it over all events before
    splitting.
  - The code's log(x + 1) transforms of reach magnitude and onset speed are not run as a variant.
  - Forward selection runs over design columns (each day and time-of-day one-hot column on its own,
    as in the code), with the adjusted R2 computed from the rank of the design as statsmodels does.
    A day or time-of-day feature counts as selected when any of its columns is; the code checks one
    fixed column. Time-of-day bins are 0-8, 8-16 and 16-24 h without shared edges.
  - The events are those of reading b of fig2-event-counts (7888), which include the false positives
    the paper removed, as the files do not mark them; the assumed bad-segment rule and the bad
    electrodes of each subject's first file are as for fig3-group-lfb-decrease-hfb-increase.
- claim: fig6b-best-models-sensorimotor
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6b-best-models-sensorimotor
  assumed: true
  notes: Reading a, all 22 good electrodes with LFB R2 > 0.05 and 13 of 14 (0.929) with HFB R2 > 0.05
    are assigned to the five frontoparietal regions, and the median R2 of precentral, postcentral and
    inferior parietal electrodes exceeds that of temporal electrodes in both bands (-0.0097 against
    -0.0158 in LFB, -0.0117 against -0.0147 in HFB). Reading b, the three regions with the highest
    projected R2 are precentral, postcentral and inferior parietal in both bands. Few electrodes exceed
    0.05, from 4 subjects in LFB and 6 in HFB.
  deviations:
  - As for fig6-r2-at-most-025. For reading a an electrode is assigned to the region with its largest
    weight in the Figshare projection matrix; electrodes whose row is all zero have no region and count
    as outside the five.
- claim: fig6c-angle-and-day-most-informative
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6c-angle-and-day-most-informative
  assumed: true
  notes: Over the 22 good electrodes with LFB R2 > 0.05, reach angle (median Delta R2 0.066) and
    recording day (0.017) have the two largest median Delta R2; time of day is third (0.0017) and the
    seven other features have a median of 0. In HFB (14 electrodes) day (0.068) and angle (0.033) are
    the two largest. The code's Delta R2, the code's selection by LFB R2, the 80/20 split and the
    inclusion of bad electrodes all give angle and day as the two largest in both bands.
  deviations:
  - As for fig6-r2-at-most-025.
- claim: extfig6-2-angle-most-retained
  outcome: partially_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:extfig6-2-angle-most-retained
  assumed: true
  notes: Angle part holds. Reach angle has the highest projected retention probability in
    precentral, postcentral and inferior parietal in both bands (0.448 to 0.679, against at most 0.400
    for any other feature there). Order part does not hold under either reading. Averaged over the
    three sensorimotor regions and both bands (reading a) the second to fifth features are onset speed,
    speech ratio, reach magnitude and bimanual ratio, and over all eight regions (reading b) speech
    ratio, onset speed, reach magnitude and bimanual ratio; reach duration is sixth and seventh. The
    second to tenth features lie between 0.202 and 0.357, so the order among them rests on small
    differences.
  deviations:
  - As for fig6-r2-at-most-025. Selection is run once per electrode and band on all of the subject's
    events, as in the code, so the retention probability of a feature at one electrode is 0 or 1 (a
    fraction for day and time of day) before projection.
- claim: fig6d-upward-reaches-enhance-pattern
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6d-upward-reaches-enhance-pattern
  assumed: true
  notes: The median split-averaged reach-angle coefficient over good electrodes with R2 > 0.05 is
    -1.027 in LFB (22 electrodes, 0.955 negative) and 0.535 in HFB (14 electrodes, none negative). The
    code's selection by LFB R2 gives -1.027 and 0.202, the inclusion of bad electrodes -0.815 and 0.515,
    and the 80/20 split -0.973 and 0.540. By subject, the LFB medians are -1.353 to 0 (4 subjects) and
    the HFB medians 0 to 0.730 (6 subjects).
  deviations:
  - As for fig6-r2-at-most-025.
- claim: fig6d-angle-and-day-largest-coefficients
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6d-angle-and-day-largest-coefficients
  assumed: true
  notes: Over good electrodes with R2 > 0.05, reach angle and the SD of the day coefficients have the
    two largest values under both readings and in both bands. LFB angle 1.027 and day 0.660, then time
    of day 0.188; HFB day 0.733 and angle 0.535, then reach magnitude 0.231 (reading a). The two
    readings differ only for features whose coefficients change sign. The code's selection by LFB R2,
    the inclusion of bad electrodes and the 80/20 split give the same two features in both bands and
    readings. The day SD is the second largest value in LFB and the largest in HFB, which bears on the
    statement's "large" SD.
  deviations:
  - As for fig6-r2-at-most-025.
'''
s = s[:i] + new + s[j:]
open(p, "w").write(s)
EOF
python -c "import yaml;d=yaml.safe_load(open('attempts/000055-peterson-2021-01.yaml'));print(len(d['outcomes']))"
```

```
25
```

**Agent calls Bash**

```bash
cd $TMPDIR/code55/compute_power_gen_figs_python && grep -n "bad\|good" tfr_utils.py compute_spectral_power.py regression_utils.py | head -30
```

```
tfr_utils.py:135:def load_project_spectral_power(tfr_lp,roi_proj_loadpath,good_rois,n_subjs,atlas='aal',rem_bad_chans=False):
tfr_utils.py:146:                bad_chans = power_load.info['bads']
tfr_utils.py:157:        if rem_bad_chans:
tfr_utils.py:159:            for i,bad_ch in enumerate(bad_chans):
tfr_utils.py:160:                inds2drop.append(np.nonzero(ch_list==bad_ch)[0])
tfr_utils.py:172:            #Remove channels so have some number as good ROIs
tfr_utils.py:174:            chs_rem = power_load.info['ch_names'][len(good_rois):]
tfr_utils.py:178:            for s, roi_ind in enumerate(good_rois):
tfr_utils.py:188:            pow_dat_all_roi_tmp = np.zeros([power_load.data.shape[0],len(good_rois),power_load.data.shape[2],power_load.data.shape[3]])
tfr_utils.py:189:            for s, roi_ind in enumerate(good_rois):
tfr_utils.py:286:def plot_specs_group(power_roi_subj_ave,roi_labels,good_rois,averagePower=False,useMedian=False):
tfr_utils.py:337:        ax[i//n_cols][i%n_cols].set_title(roi_label_dict[roi_labels[good_rois[curr_ind]]],
tfr_utils.py:350:def plot_specs_single_region(power_roi_subj_ave,region_label,roi_labels,good_rois,
tfr_utils.py:355:    chosen_ROI_labels = [val for s,val in enumerate(roi_labels) if any(good_rois==s)]
tfr_utils.py:466:def plot_ecog_electrodes_mni_in_order(elec_locs,bad_chans,chan_labels='all',num_grid_chans=64,colors_in=None,node_size=50,
tfr_utils.py:478:        good_chan_inds = np.ones([elec_locs[k].shape[0],1])
tfr_utils.py:479:        good_chan_inds[bad_chans[k],0] = 0
tfr_utils.py:506:        elif chan_labels== 'allgood':
tfr_utils.py:507:            locs = pd.DataFrame(np.concatenate((elec_locs[k],good_chan_inds),axis=1),columns=['X','Y','Z','goodChanInds'])
tfr_utils.py:535:        if chan_labels=='allgood':
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code55/compute_power_gen_figs_python && sed -n 135,160p tfr_utils.py; sed -n 20,40p compute_spectral_power.py
```

```
def load_project_spectral_power(tfr_lp,roi_proj_loadpath,good_rois,n_subjs,atlas='aal',rem_bad_chans=False):
    '''
    Loads in electrode-level spectral power and projects it to ROI's. 
    '''
    first_pass = 0
    metadata_list = []
    for j in range(n_subjs):
        fname_tfr = natsort.natsorted(glob.glob(tfr_lp+'subj_'+str(j+1).zfill(2)+'*_allEpochs_tfr.h5'))
        for i,fname_curr in enumerate(fname_tfr):
            if i==0:
                power_load = mne.time_frequency.read_tfrs(fname_curr)[0]
                bad_chans = power_load.info['bads']
                ch_list = np.asarray(power_load.info['ch_names'])
            else:
                pow_temp = mne.time_frequency.read_tfrs(fname_curr)[0]
                power_load.data = np.concatenate((power_load.data,pow_temp.data),axis=0)
        metadata_list += [str(j)]*int(power_load.data.shape[0])

        #Project to ROI's
        df = pd.read_csv(roi_proj_loadpath+atlas+'_'+str(j+1).zfill(2)+'_elecs2ROI.csv')
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p = "attempts/000055-peterson-2021-01.yaml"
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)
rep("""    description says depth, where the paper says five. Sex and age are not in the files or the
    archive's metadata and are not testable.""", """    description says depth, where the paper says five. Sex and age are not in the files or the
    archive's metadata and are not testable. The data descriptor of the dataset (doi
    10.1038/s41597-022-01280-y, Table 2) counts S10 as 86 surface and 40 depth electrodes and S11 as
    106 surface and none, where the group descriptions give 78 and 48, and 88 and 18. With the
    descriptor's counts the surface mean is 87.0 +- 12.9 and six subjects have depth electrodes (23.3
    +- 12.0), so the count of five fails under both. The descriptor's table also lists sex and age (8
    male, 4 female; ages with mean 29.4), which match the paper, but it is not the dataset and is not
    used for the outcome.""")
rep("""    positive, and the paper removed 17.8% of events as false positives or occlusions, so the dataset
    likely holds events the paper dropped.""", """    positive, and the paper removed 17.8% of events as false positives or occlusions, so the dataset
    likely holds events the paper dropped. The reaches table has the same nine columns in all 55 files
    and none marks false positives or verified events, so the outcome rests on reading a in full and on
    reading b without its false-positive step. Removing about 14% of the events from reading b would
    bring the median near 640, so the shortfall may come from the missing marks.""")
rep("""    lie within 30 degrees of horizontal. Reading a gives the same.
  deviations:
  - Angle convention as in fig2-features-differ-across-subjects.""", """    lie within 30 degrees of horizontal. Reading a gives the same. The criterion's KDE has no
    boundary correction, and on synthetic angles whose density peaks at +-90 it puts the peaks at
    -72.5 and 70.0 (n = 250) and -73.5 and 74.0 degrees (n = 900), so the criterion is biased against
    the angle part. With the data reflected at +-90 (a sensitivity output, not the criterion) the peaks
    lie within 15 degrees of +-90 pooled and in 6 of 12 subjects, still not more than half, so the
    outcome is the same. Asked of a reader (questions/000055.yaml).
  deviations:
  - Angle convention as in fig2-features-differ-across-subjects.""")
rep("""    sentence (Intracortical spectral power, paragraph 2) and Figure 3 give no measure; with region
    counts the two bands tie here at 7 of 8.""", """    sentence (Intracortical spectral power, paragraph 2) and Figure 3 give no measure; with region
    counts the two bands tie here at 7 of 8. The tie does not depend on the bootstrap seed. With ten
    other seeds reading a gives 7 against 7 regions every time and reading b 35.0 to 35.6 against 25.5
    to 25.8 bins per frequency, and middle and inferior temporal keep 3 to 4 and 6 to 9 significant
    high-frequency bins.""")
rep("""  - The bad electrodes are those of each subject's first file, as the code takes them; the files'
    good flags differ between days for every subject.""", """  - The bad electrodes are those of each subject's first file, as the code takes them
    (tfr_utils.py, load_project_spectral_power, which reads info['bads'] from the first power file of
    each subject only); the files' good flags differ between days for every subject.""")
rep("""    S04, part 4 fails and the claim would be partially reproduced.""", """    S04, part 4 fails and the claim would be partially reproduced. The interpolated width is also
    close for the third place (S11 16.8 Hz against S05 16.9 Hz), but S04 (14.4 Hz) is second.""")
open(p, "w").write(s)
EOF
grep -n "middle and inferior temporal keep" attempts/000055-peterson-2021-01.yaml
```

```
225:    to 25.8 bins per frequency, and middle and inferior temporal keep 3 to 4 and 6 to 9 significant
```

**Agent calls Bash**

```bash
python - <<'EOF'
p = "attempts/000055-peterson-2021-01.yaml"
s = open(p).read()
old = """Removing about 14% of the events from reading b would
    bring the median near 640, so the shortfall may come from the missing marks."""
assert old in s
s = s.replace(old, """The reading b median less 14% (739 x 0.86 = 636)
    would lie within tolerance, so the shortfall may come from the missing marks.""")
old = """- kind: methods_unavailable
  statement: The paper's rule for bad ECoG segments"""
assert old in s
s = s.replace(old, """- kind: metadata_error
  statement: The electrode group descriptions and the data descriptor's Table 2 disagree for two
    subjects. S11 has groups LATD, LMTD and LTPD described as depth (18 electrodes), where the
    descriptor gives S11 106 surface and no depth electrodes; S10 has 78 electrodes in groups not
    described as depth and 48 in depth groups, where the descriptor gives 86 and 40.
""" + old)
open(p, "w").write(s)
EOF
tail -5 attempts/000055-peterson-2021-01.yaml
```

```
- kind: methods_unavailable
  statement: The paper does not say how it judged low-frequency decreases "more spatially widespread"
    than high-frequency increases (Results, Intracortical spectral power, paragraph 2). Question for
    the authors. Was it the number of regions with significant changes or the extent of significant
    bins? The two give different answers here.
```

**Agent calls Bash**

```bash
cat >> attempts/000055-peterson-2021-01.yaml <<'EOF'
verifications:
- date: '2026-11-07'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper and the data descriptor. The verifier tested
    helper functions on synthetic inputs (fold_angle, band and time bins, band_values, segment_power,
    boot_sig_mask) and checked the archive's asset metadata. It agreed with 19 outcomes and found the
    six regression claims blocked without good reason.
  results:
  - claim: subject-days
    agrees: true
    outcome: reproduced
    reason: All 12 subjects have exactly the Table 2 days, 55 subject-days.
    response: No change needed.
  - claim: roi-projection-link
    agrees: true
    outcome: reproduced
    reason: Rows match electrodes for 12 of 12 subjects. The top weight is at the nearest centroid for
      0.59 to 0.79 of electrodes, against about 0.2 when the order is shuffled. The eight regions with
      density > 3 are the ones the claims file names.
    response: No change needed.
  - claim: cohort
    agrees: true
    outcome: partially_reproduced
    reason: 12 subjects, surface mean 84.8, depth mean 23.7 and 5 right hemisphere pass; subjects with
      depth electrodes is 7 against an exact 5. Sex and age are not in the files or the archive metadata.
      Depth electrodes are taken as groups whose description contains "depth"; the data descriptor's
      Table 2 gives S10 86 surface + 40 depth and S11 106 + 0, and with its counts 6 subjects have depth
      electrodes, so the outcome stands (B6).
    response: Added a data check printing every group and its description beside the descriptor's Table
      2, and the cohort numbers with the descriptor's counts (87.0 +- 12.9 surface, 6 subjects with
      depth electrodes). Recorded the disagreement for S10 and S11 as a finding. Outcome kept.
  - claim: fig2-event-counts
    agrees: true
    outcome: not_reproduced
    reason: The fewest and the median are outside tolerance under both readings. Reading b could not
      drop the false positives, as the files do not mark them; the gap between 8088 events and the
      descriptor's 6931 verified events could account for the mismatch (a median of 739 at about 14%
      removal is about 635), so the claim is not_reproduced only under reading a in full (B3).
    response: Added a data check printing the reaches-table columns of every file (the same nine in all
      55, none marking false positives or verified events). The notes and conclusion now say the outcome
      rests on reading a and on reading b without its false-positive step. Outcome kept.
  - claim: fig2-features-differ-across-subjects
    agrees: true
    outcome: reproduced
    reason: All ten Kruskal-Wallis p < 0.001 under both readings.
    response: No change needed.
  - claim: fig2-reach-shape
    agrees: true
    outcome: partially_reproduced
    reason: The duration and magnitude part holds; the angle part holds in 0 of 12 subjects and not
      pooled, with peaks near +-70. A Gaussian KDE without boundary correction cannot place peaks near
      +-90 for data bounded there; on synthetic folded angles peaking at +-90, Scott's bandwidth puts the
      peaks at +-72 to +-74, so the angle part's failure does not count as evidence against the paper
      (B2, in the criterion, reported and not corrected).
    response: Added the synthetic check and the same KDE with the data reflected at +-90 as a
      sensitivity output. With reflection the peaks lie within 15 degrees of +-90 pooled and in 6 of 12
      subjects, not more than half, so the outcome is the same. The criterion is asked of a reader in
      questions/000055.yaml. Outcome kept.
  - claim: fig2-bimanual-skew
    agrees: true
    outcome: reproduced
    reason: The ratio, overlap and class parts hold pooled and in 12 of 12 subjects; S02, S04 and S05 are
      among both "five" sets under both readings.
    response: No change needed.
  - claim: extfig2-1c-contralateral-larger
    agrees: true
    outcome: reproduced
    reason: The contralateral peak exceeds the ipsilateral peak in 12 of 12 subjects under both readings;
      the smallest ratio is 1.08 (S05).
    response: No change needed.
  - claim: extfig2-2-feature-correlations
    agrees: true
    outcome: partially_reproduced
    reason: 5 of 6 correlations are within tolerance; magnitude vs duration is r = 0.233 against 0.26 +-
      0.026 under both readings.
    response: No change needed.
  - claim: fig2-days-and-waking
    agrees: true
    outcome: partially_reproduced
    reason: The busiest day holds more than half of the events for S05 and S09 but not S04 (0.379); the
      waking part holds in 12 of 12 subjects.
    response: No change needed.
  - claim: fig3-group-lfb-decrease-hfb-increase
    agrees: true
    outcome: reproduced
    reason: Masked 4-30 Hz power is below 0 and 50-120 Hz power above 0 in precentral, postcentral and
      inferior parietal under both readings. Bad electrodes are taken from each subject's first file and
      the good flags differ between files for all 12 subjects; the helper attributes this to the code,
      which the verifier could not check (B7). The summary of segment power for the bad-segment rule is
      an assumption, and the SD is per subject where the Methods say all segments; the main results
      barely move without the rule (B8). The three short files are assumed to end at midnight, which
      ReachEvents and the neural response support (B9).
    response: The deviation now cites the code that takes the first file's bad list (tfr_utils.py,
      load_project_spectral_power). The seed check added for fig3-lfb-more-widespread shows the pattern
      in the three named regions under ten other seeds. Outcome kept.
  - claim: fig3-sensorimotor-largest
    agrees: true
    outcome: reproduced
    reason: Under readings a, b and c the named three are the top three, and every temporal region is
      below them.
    response: No change needed.
  - claim: fig3-lfb-more-widespread
    agrees: true
    outcome: blocked
    reason: Reading a gives 7 regions against 7, reading b 35.2 against 25.9 bins per frequency.
      Supramarginal and superior temporal do have low-frequency decreases. The disagreement rests on a
      few marginal bins in middle and inferior temporal from one bootstrap seed; if either region lost
      them under another seed, the claim would be reproduced. Seed stability was not checked (B4).
    response: Added the masks under ten other seeds. Reading a gives 7 against 7 under every seed
      (middle and inferior temporal keep 3 to 4 and 6 to 9 significant high-frequency bins) and reading b
      35.0 to 35.6 against 25.5 to 25.8, so the readings disagree under every seed. Outcome kept.
  - claim: fig4-precentral-subject-variability
    agrees: true
    outcome: reproduced
    reason: Parts 1 to 3 hold. Part 4 holds only after a tie-break, as four subjects tie at 3 bins and
      are ranked alphabetically; the interpolated width is the author's own measure, not the criterion's.
      It also passes (S04 at 14.4 Hz is second narrowest), but S11 is 16.8 Hz against S05 at 16.9 Hz.
      Under a strict reading of the tie, part 4 is indeterminate and the claim would be partial (B5).
    response: The notes give the margin at the third place. Outcome kept, marked as assumed, with the
      strict reading recorded in the deviations.
  - claim: fig5-band-power-differs-across-subjects
    agrees: true
    outcome: reproduced
    reason: p = 1.3e-163 (LFB) and 7.1e-264 (HFB) with the band mean; the median variant agrees.
    response: No change needed.
  - claim: table1-subject-band-power-ci
    agrees: true
    outcome: partially_reproduced
    reason: The best reading puts 23 of 24 values inside the paper's intervals; S06 HFB is 1.78 against
      2.02 to 2.37, and the bootstrap interval here (1.64 to 1.92) does not overlap the paper's. Other
      readings give 21, 21 and 20.
    response: No change needed.
  - claim: fig5-recording-day-effects
    agrees: true
    outcome: reproduced
    reason: With the band mean, all 24 subject and band pairs agree with the paper; the median variant
      gives 23, missing LFB S05.
    response: No change needed.
  - claim: extfig5-1-baseline-reduces-day-variability
    agrees: true
    outcome: reproduced
    reason: The SD is lower with the baseline subtracted in 9/12 (LFB) and 12/12 (HFB) subjects, and for
      92% and 90% of good electrodes; 11 day effects remain.
    response: No change needed.
  - claim: discussion-day-changes-small
    agrees: true
    outcome: reproduced
    reason: The largest day change is 1.01 dB (limit 2.2); levels without baseline are 12.4 to 36.3 dB in
      microvolts, inside 9 to 55.
    response: No change needed.
  - claim: fig6b-best-models-sensorimotor
    agrees: false
    outcome: blocked
    reason: The notebook says "too large", but its own estimate is 3.1 h on one core and 0.8 h on 4
      cores, about four times that with the variants, the same order as the 24 min ECoG step it ran. All
      inputs are in the dataset and already computed in the notebook. None of the six regression claims
      was tested (B1).
    response: Ran the regressions. The Huber fits are solved many at once by a batched Newton method on
      sklearn's objective (within 4.4e-05 of sklearn in withheld R2), and Delta R2 refits are run where
      the full model's R2 exceeds 0.05; the main analysis and every variant take 2.2 min. Outcome changed
      from blocked to reproduced. Both readings hold in both bands.
  - claim: fig6-r2-at-most-025
    agrees: false
    outcome: blocked
    reason: Not run, for the same reason as fig6b-best-models-sensorimotor. The dataset's electrode
      tables hold the paper's own R2 (max 0.149 LFB, 0.255 HFB), which fits the claim but is the paper's
      output, not a reproduction.
    response: Ran the regressions, with the per-electrode R2 table by subject and band. Outcome changed
      from blocked to reproduced. The largest R2 is 0.189, with 0.192 (80/20) and 0.203 (band median) as
      variants. The stored R2 are shown for reference only.
  - claim: fig6c-angle-and-day-most-informative
    agrees: false
    outcome: blocked
    reason: Not run, for the same reason as fig6b-best-models-sensorimotor.
    response: Ran the regressions. Outcome changed from blocked to reproduced. Angle and day have the
      two largest median Delta R2 in LFB, and in HFB, under every variant.
  - claim: extfig6-2-angle-most-retained
    agrees: false
    outcome: blocked
    reason: Not run, for the same reason as fig6b-best-models-sensorimotor.
    response: Ran the regressions. Outcome changed from blocked to partially_reproduced. Angle is the
      most retained feature in the three sensorimotor regions in both bands, but the order of the next
      four does not hold under either reading.
  - claim: fig6d-upward-reaches-enhance-pattern
    agrees: false
    outcome: blocked
    reason: Not run, for the same reason as fig6b-best-models-sensorimotor.
    response: Ran the regressions. Outcome changed from blocked to reproduced. The median angle
      coefficient is -1.027 (LFB) and 0.535 (HFB), with the same signs in every variant.
  - claim: fig6d-angle-and-day-largest-coefficients
    agrees: false
    outcome: blocked
    reason: Not run, for the same reason as fig6b-best-models-sensorimotor.
    response: Ran the regressions. Outcome changed from blocked to reproduced. Angle and the day SD are
      the two largest under both readings in both bands and in every variant.
EOF
cat > questions/000055.yaml <<'EOF'
dandiset: "000055"
paper: doi:10.1523/eneuro.0007-21.2021
questions:
- claim: fig2-reach-shape
  asked: 2026-11-07
  question: The criterion judges the angle part on a Gaussian KDE with Scott's bandwidth evaluated on
    -90 to 90, with peaks required within 15 degrees of +-90. For angles bounded at +-90 such a KDE
    without boundary correction cannot place its peaks near +-90. Should the criterion use a
    boundary-corrected density (for example reflection at +-90), a histogram, or a wider window around
    +-90?
  passage: For reach angle, the distributions tend to be bimodal, with peaks at +-90 (Results, Behavior
    during naturalistic movements, paragraph 3; Figure 2, drawn with seaborn kdeplot in the code)
  why: On synthetic folded angles whose density peaks at +-90 the criterion's KDE puts the peaks at
    -72.5 and 70.0 (n = 250) and -73.5 and 74.0 degrees (n = 900), so the test is biased against the
    claim. In this attempt the angle part fails in 0 of 12 subjects with the criterion's KDE and holds
    in 6 of 12 (and pooled) with reflection, still not more than half, so the outcome does not change
    here, but a criterion that a true peak at +-90 can pass would be judged differently on other data.
EOF
python -c "import yaml;yaml.safe_load(open('questions/000055.yaml'));d=yaml.safe_load(open('attempts/000055-peterson-2021-01.yaml'));print(len(d['verifications'][0]['results']))"; head -12 questions/000005.yaml | head -3; date -u
```

```
25
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
Sat Nov  7 07:07:08 UTC 2026
```

**Agent calls Bash**

```bash
grep -nP "^\s+(?!- )[^:]*\S: " attempts/000055-peterson-2021-01.yaml questions/000055.yaml | grep -vP "^\S+:\d+:\s+-?\s*[a-z_]+: " | head; grep -n " — \|rather" attempts/000055-peterson-2021-01.yaml questions/000055.yaml entries/000055-peterson-2021/README.md | head; cd  && python tools/entry.py check entries/000055-peterson-2021 2>&1 | grep -v Warn | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
grep -c "—\|rather" entries/000055-peterson-2021/reproduce_peterson_2021.ipynb entries/000055-peterson-2021/ajile.py; date -u; python tools/entry.py all entries/000055-peterson-2021 2>&1 | grep -v Warn | tail -5; date -u
```

```
entries/000055-peterson-2021/reproduce_peterson_2021.ipynb:0
entries/000055-peterson-2021/ajile.py:0
Sat Nov  7 07:07:19 UTC 2026
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (1691 s)
Sat Nov  7 07:35:38 UTC 2026
```

**Agent**

Run passed (28 min). Checking that the numbers match the first run and the conclusions.

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
for c in nb['cells']:
  if c['cell_type']!='code': continue
  for o in c['outputs']:
    t=o.get('text','')
    t=''.join(t) if isinstance(t,list) else t
    for l in t.splitlines():
      if any(k in l for k in ['fits: largest','Largest full-model','Holds (reading','two largest [','order holds','Angle above','main: LFB median','Reflected KDE','Reading a, low-frequency','Variant, the data','segments of','total ']) : print(l[:230])
  if o.get('output_type')=='error': print('ERROR')
" | sort | uniq -c | head -40
```

```
Traceback (most recent call last):
  File "<string>", line 10, in <module>
    if o.get('output_type')=='error': print('ERROR')
       ^
NameError: name 'o' is not defined
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('executed/000055-peterson-2021/reproduce_peterson_2021.ipynb'))
for c in nb['cells']:
  if c['cell_type']!='code': continue
  for o in c['outputs']:
    if o.get('output_type')=='error': print('ERROR')
    t=o.get('text','')
    t=''.join(t) if isinstance(t,list) else t
    for l in t.splitlines():
      if any(k in l for k in ['fits: largest','Largest full-model','Holds (reading','order holds','Angle above','main: LFB median','Reflected KDE','Reading a, low-frequency','Variant, the data','segments of','total ','main, LFB','main, HFB']) : print(l[:230])
"
```

```
ECoG segments of 8087 events read and reduced in 23.5 min
Variant, the data descriptor's Table 2 counts: surface mean 87.0 +- 12.9 ; subjects with depth electrodes 6 , their mean 23.3 +- 12.0
Reflected KDE: two highest maxima within 15 degrees of -90 and +90 in 6 of 12 subjects; pooled True
Reading a, low-frequency regions more than high-frequency in 0 of 10 seeds, equal in 10 ; reading b, low larger in 10 of 10; supramarginal and superior temporal low-frequency decreases in 10 of 10; fig3 pattern in all 3 named regi
240 fits: largest coefficient difference 1.16e-03, largest withheld R2 difference 4.40e-05 (median 1.9e-06)
main (90/10, band mean, all electrodes): 2368 full models, 86 with refits, 0.9 min; 80/20 (good electrodes): 2192 and 84, 0.7 min; band median: 2192 full models; total 2.3 min
Largest full-model withheld R2 over good electrodes, subjects and bands: 0.189; at most 0.275: True
Holds (reading a, reading b): {'lfb': (True, True), 'hfb': (True, True)}
  main, LFB: two largest ['angle', 'day']; angle and day both: True
  main, HFB: two largest ['day', 'angle']; angle and day both: True
Angle above every other feature: {('lfb', 'precentral'): True, ('lfb', 'postcentral'): True, ('lfb', 'inferior parietal'): True, ('hfb', 'precentral'): True, ('hfb', 'postcentral'): True, ('hfb', 'inferior parietal'): True} -> Tru
reading a, three sensorimotor regions: ranking [('angle', 0.582), ('speed', 0.357), ('speech', 0.356), ('magnitude', 0.343), ('bimanual_ratio', 0.324), ('duration', 0.322), ('bimanual_class', 0.301), ('day', 0.29), ('bimanual_over
reading b, all eight regions: ranking [('angle', 0.492), ('speech', 0.351), ('speed', 0.326), ('magnitude', 0.324), ('bimanual_ratio', 0.316), ('bimanual_class', 0.309), ('duration', 0.289), ('bimanual_overlap', 0.28), ('day', 0.2
main: LFB median below 0 True; HFB median above 0 True
  main, LFB, reading a: two largest ['angle', 'day']; angle and day: True
  main, LFB, reading b: two largest ['angle', 'day']; angle an
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/the main analysis and every variant take 2.2 min\./the main analysis and every variant take about 2 min./' attempts/000055-peterson-2021-01.yaml && grep -n "about 2 min" attempts/000055-peterson-2021-01.yaml && python tools/entry.py check entries/000055-peterson-2021 2>&1 | grep -v Warn | tail -2; git status --short
```

```
619:      the full model's R2 exceeds 0.05; the main analysis and every variant take about 2 min. Outcome changed
0 error(s)
 M attempts/000055-peterson-2021-01.yaml
 M entries/000055-peterson-2021/README.md
 M entries/000055-peterson-2021/ajile.py
 M entries/000055-peterson-2021/entry.yaml
 M entries/000055-peterson-2021/reproduce_peterson_2021.ipynb
 M tools/build_site.py
 M tools/runner/run_requests.py
 M tools/site_assets/app.css
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
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bashrc .bash_profile .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc scripts .idea .vscode 2>&1 | head -30
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 06:08 scripts
```

**Agent**

I've addressed the round-1 report and re-run the entry with `python tools/entry.py all entries/000055-peterson-2021`. It passed in 28 minutes and the checks report 0 errors. Nothing is committed.

**Outcome changes**

The verifier was right that the six Figure 6 claims did not need to be blocked. I added a batched Huber solver to `ajile.py` (`huber_fit`). It minimises the same objective as the `HuberRegressor` the paper's code uses, and over 240 fits it stays within 4.4e-05 of sklearn's withheld R2. The main analysis and every variant now run in about 2 minutes.

| Claim | Was | Now |
|---|---|---|
| fig6-r2-at-most-025 | blocked | reproduced (largest R2 0.189; 0.192 with the code's 80/20 split, 0.203 with its band median) |
| fig6b-best-models-sensorimotor | blocked | reproduced (both readings, both bands) |
| fig6c-angle-and-day-most-informative | blocked | reproduced (angle and day are the top two in both bands under every variant) |
| extfig6-2-angle-most-retained | blocked | partially reproduced (angle is retained most, but the order of the next four does not hold under either reading) |
| fig6d-upward-reaches-enhance-pattern | blocked | reproduced (median angle coefficient -1.027 for low-frequency power, 0.535 for high-frequency) |
| fig6d-angle-and-day-largest-coefficients | blocked | reproduced (both readings, both bands) |

The other 19 outcomes are unchanged.

**What I added or corrected for the other points**
- **Event counts (B3):** the reaches table has the same nine columns in all 55 files and none marks false positives. The notes now say `fig2-event-counts` is "not reproduced" on all events, and on the cleaned events without the false-positive removal.
- **Reach angle KDE (B2):**
  - **Synthetic check:** on angles whose true peaks sit at ±90, the criterion's KDE puts them near ±70 to ±74.
  - **Sensitivity output:** with the data reflected at ±90, the peaks hold pooled and in 6 of 12 subjects. That is still not more than half, so the outcome stays partial.
  - **Question for a reader:** the criterion is added to `questions/000055.yaml`. The claim is unchanged.
- **Bootstrap seed (B4):** I re-ran the Figure 3 masks with ten other seeds. Reading a ties at 7 against 7 regions under every seed, so `fig3-lfb-more-widespread` stays blocked.
- **Electrode counts (B6):** a new data check prints every electrode group and its description beside the data descriptor's Table 2. With the descriptor's counts, six subjects have depth electrodes, still not five, so `cohort` stays partial. The disagreement for S10 and S11 is recorded as a new finding.
- **Bad electrodes (B7):** the record now cites the exact place in the paper's code (`tfr_utils.py`, `load_project_spectral_power`) that takes each subject's bad-electrode list from its first file.
- **Tie-break (B5):** the narrow margin at the third place is now in the notes. The outcome stays reproduced and is marked as resting on an assumption.
- **Record and docs:** round 1 is recorded under `verifications` for all 25 claims. The regression claims are marked as disagreeing, since the verifier had them blocked for a different reason. I also updated the header, summary, `README.md` and `entry.yaml`.

**Not done**
- The code's log(x + 1) transforms of reach magnitude and onset speed are not run as a variant. The opening comment of the claims file names this variant, but no regression criterion does.
- In the "code's Delta R2" variant I reused the main refit and shuffled only the test events. The paper's code shuffles across all events before splitting. Both points are recorded as deviations.
- Only 22 (low-frequency) and 14 (high-frequency) good electrodes exceed R2 0.05. That makes the Figure 6c and 6d medians rest on few electrodes, from 4 and 6 subjects. The notes say so.

## End of run

64 turns, 77 minutes, $5.13 at API prices, result: success.
