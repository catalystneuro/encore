# okuno-2025 · author-revise-2 · run 43788154743

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/okuno-2025/verifier-2-report.md; ls entries/okuno-2025 entries/okuno-2025/*
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '/[Ss]tep 6/,+60p' | head -120
```

```
Mon Nov 16 01:53:11 UTC 2026
## Verifier report: Okuno et al. 2025 on DANDI:000727, round 2

Counts are taken from the files. The claims file has 30 claims. The attempt record has 30 outcomes: 14 blocked, 10 reproduced, 3 partially reproduced and 3 not reproduced. Eight outcomes carry `assumed: true`: fig3d-flyem-vs-flywire, fig3e, fig3g, fig4e, fig4f, fig4i, fig5b-walking-activation and fig5b-walking-suppression.

The main finding of this round is that the notebook was re-executed but its text was not updated. Almost every FC and GLM number in the "Result:" cells, the Summary and the record's notes and `measured` fields comes from an earlier run. The numbers in this run's printed output are different. Every outcome still holds on this run's output, but the stated values do not match it.

### 1. Outcomes

I agree with all 30 outcomes as stated, with these remarks:

- **fig3d (partially reproduced), agree.** Cell 19 prints FlyEM 0.5925 and FlyWire 0.5557: FlyEM is higher, and both values are below tolerance. The record's `measured` values (0.6161, 0.5808) are not this run's.
- **fig3e (reproduced), agree, but it is fragile.** Cell 23 prints 55. Across runs the count has been 54 (round 1), 53 (record) and 55 (now), against a lower bound of 52.2. It falls out of tolerance with left and right swapped (44) and with no nuisance removal (48). The record's `measured: 53` is not this run's value.
- **fig3g (not reproduced), agree.** Cell 26 prints ACh r = −0.072 (p = 0.573) and GABA r = −0.067 (p = 0.601). The record's `measured` values (0.033, −0.17) are not this run's.
- **fig4e, fig4f (reading a) and fig4i (reproduced), agree.** In cells 30, 32 and 34 the MAIN line is True/True for all three. For fig4i, the synapse p = 1.4e‑4 is below 8.3e‑3.
- **fig5b-walking-activation (reproduced), agree under reading (a).** Cell 38 prints True for all four neuropils, both atlases and both regressors.
- **fig5b-walking-suppression (not reproduced), agree.** Cell 41: no voxel is below −
[... 122 more lines not kept]
```

```
205:(step 6).
206:
207:**Time.** An author run is stopped five hours after it starts, and whatever
208:is not recorded by then is lost. The prompt says when the run started and the
209:time by which to finish. Check the clock (`date -u`) between steps. When that
210:time comes, stop analysing and finish: record each claim not yet tested as
211:blocked, `too_large` where the computation is what stopped it, saying how far
212:it got, then write the attempt record and run the entry's checks. A record
213:with some claims blocked for time is worth more than a run that is cut off.
214:
215:### 1. Establish what can be tested
216:
217:Do this before any analysis.
218:
219:1. List the dataset's files and read its metadata from the archive. Open a
220:   file and list everything it holds, including every column of every table.
221:2. Work out which of the subjects, sessions, conditions and measured
222:   variables that the claims file describes are in the dataset. A dataset
223:   that names a paper may hold only part of its data. Check for recordings
224:   deposited more than once (identical traces, frame counts or annotations),
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "### 6\|Hand over" docs/protocol.md; awk '/### 6. Hand over/,/^### 7|^## /' docs/protocol.md
```

```
186:### 6. Answer questions
190:not say what the paper says (author, step 1.6, and "Hand over for
482:  verification round, with its `reason` (see "Hand over for verification").
502:### 6. Hand over for verification
### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

- the executed notebook with the conclusion cells and the summary removed;
- the helper module;
- the claims file.

`python tools/entry.py handover entries/<name>` builds these in
`executed/<name>/handover/` from the executed copy. The verifier also gets the
paper, under `paper/`, but checks the analysis against the claims file, and a
method detail the author took from the paper against the passage the author
cites. A place where the claims file misreads the paper is reported; the
revision adds it to `questions/<paper>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
attempt, in an `answer` run started by hand; the claim's outcome stays as
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; wc -l *; cat README.md | head -80; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']): print(i,c['cell_type'],repr(''.join(c['source'])[:150]))
"
```

```
31 README.md
   536 connectome_okuno_2025.ipynb
    27 entry.yaml
   673 flyfc.py
  1195 reproduce_okuno_2025.ipynb
    10 requirements.in
  2003 requirements.lock.txt
  4475 total
# Okuno, Woodward, Okano & Hata (2025) from dandiset 000727

Tests the findings of [Okuno et al. (2025)](https://doi.org/10.7554/elife.107990.1) on
[DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), the whole-brain two-photon
imaging of nine walking flies (Brezovec et al.) that the paper reuses. The FC computed here from the
raw imaging is compared with the paper's published FlyEM and FlyWire SC matrices (its code at
commit 4b92add and Zenodo record 15532272).

| Claim | Outcome |
|---|---|
| FlyEM gives a higher FC-SC correlation than FlyWire (0.73 against 0.68) | Partially reproduced |
| FlyEM is higher in 58 of 63 regions | Reproduced |
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/okuno-2025/ 2>&1; cat entries/okuno-2025/entry.yaml; python - <<'E'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
c=nb['cells'][55]
for o in c.get('outputs',[]): print(o.get('text',''))
E
sed -n '/^## Develop on a subset/,/^## /p' docs/protocol.md | head -30; nproc; free -g
```

```
connectome_okuno_2025.ipynb
reproduce_okuno_2025.ipynb
result.json
schema_version: 1
name: okuno-2025
type: reproduction
title: Functional and structural connectivity in Drosophila (Okuno et al. 2025)
description: Tests the findings of Okuno, Woodward, Okano and Hata (2025) on dandiset 000727, which
  holds the whole-brain two-photon imaging of nine walking flies that the paper reuses. The raw
  GCaMP series are streamed, registered to the paper's resized FDA template and reduced to the 114
  hemibrain ROIs, and the resulting FC is compared with the paper's published FlyEM and FlyWire SC
  matrices, including its permutation tests of unsegregated, segregated and reciprocal synapses. A
  group GLM of walking is run on the same data. The k-means ROI atlases of the paper's smoothing
  and ROI-count analyses are not published, so those claims are blocked.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_okuno_2025.ipynb
  title: Reproducing Okuno et al. (2025) from dandiset 000727
  runtime_minutes: 23
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; grep -n "registration\|seed\|THREAD\|cache\|CACHE\|NATIVE_SPACING" flyfc.py | head -50; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i in [1,2,7,9]: print(i,''.join(nb['cells'][i]['source']));print('----')
"
```

```
23:- registration of the mean green image to the resized FDA template with ANTs SyN:
28:  template voxel a native voxel maps to by more than the registration error.
33:  correlation after an affine registration is printed for the eight flips); no flip
87:NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)
262:# --------------------------------------------------------------------------- registration
270:def choose_flip(mean, tmpl_img, seed=1):
271:    """Correlation with the template after an affine registration, for each flip."""
276:        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)
277:        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", random_seed=seed)
282:def register(mean, tmpl_img, fl, seed=1):
283:    """SyN registration of the flipped mean image to the template.
285:    The affine start is the better of two affine registrations (mean squares and
296:    mov = ants.from_numpy(m, spacing=NATIVE_SPACING_MM)
300:        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", aff_metric=metric,
301:                              random_seed=seed, aff_iterations=(2100, 1200, 1200, 10),
306:    r = ants.registration(tmpl_img, mov, type_of_transform="SyNOnly",
307:                          initial_transform=aff[best][1], random_seed=seed)
318:        ci = ants.from_numpy(g, spacing=NATIVE_SPACING_MM)
386:    repeats: further registration seeds; for each, the ROI series are computed in the
387:    same pass through that registration (R_repeats), to show how much the
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i in [7,8,9]:
  for o in nb['cells'][i].get('outputs',[]): print(o.get('text',''))
E
sed -n 380,440p entries/okuno-2025/flyfc.py
```

```
["fly-087 read 8161 MB in 118 s | correlation with template {'affine_meansquares': 0.671, 'affine_mattes': -0.187, 'syn': 0.803, 'repeat_displacement_um_median': 22.056, 'repeat_displacement_um_p95': 51.396} | ROIs not fully in the field of view 0 min coverage 1.0\n"]
["fly-089 read 7253 MB in 121 s | correlation with template {'affine_meansquares': 0.656, 'affine_mattes': 0.713, 'syn': 0.817, 'repeat_displacement_um_median': 0.877, 'repeat_displacement_um_p95': 2.253} | ROIs not fully in the field of view 6 min coverage 0.922\n"]
["fly-094 read 7666 MB in 117 s | correlation with template {'affine_meansquares': 0.653, 'affine_mattes': 0.728, 'syn': 0.794, 'repeat_displacement_um_median': 21.7, 'repeat_displacement_um_p95': 54.741} | ROIs not fully in the field of view 0 min coverage 0.999\n"]
["fly-097 read 7408 MB in 113 s | correlation with template {'affine_meansquares': 0.582, 'affine_mattes': 0.277, 'syn': 0.707, 'repeat_displacement_um_median': 5.054, 'repeat_displacement_um_p95': 9.378} | ROIs not fully in the field of view 0 min coverage 1.0\n"]
["fly-098 read 7318 MB in 112 s | correlation with template {'affine_meansquares': 0.626, 'affine_mattes': 0.371, 'syn': 0.733, 'repeat_displacement_um_median': 5.936, 'repeat_displacement_um_p95': 10.39} | ROIs not fully in the field of view 0 min coverage 1.0\n"]
["fly-099 read 7346 MB in 108 s | correlation with template {'affine_meansquares': 0.635, 'affine_mattes': 0.344, 'syn': 0.729, 'repeat_displacement_um_median': 7.077, 'repeat_displacement_um_p95': 19.357} | ROIs not fully in the field of view 0 min coverage 1.0\n"]
["fly-100 read 7084 MB in 117 s | correlation with template {'affine_meansquares': 0.629, 'affine_mattes': 0.666, 'syn': 0.729, 'repeat_displacement_um_median': 25.372, 'repeat_displacement_um_p95': 74.776} | ROIs not fully in the field of view 30 min coverage 0.0\n"]
["fly-101 read 7285 MB in 112 s | correlation with template {'affine_meansquares': 0.642, 'affine_mattes': -0.208, 'syn': 0.729
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; sed -n 1,60p flyfc.py; sed -n 262,330p flyfc.py; grep -n "def mean_image\|def code_nifti\|def load_masks\|masks" flyfc.py | head; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
print(''.join(nb['cells'][5]['source']))"
```

```
"""Loading and measures for testing Okuno et al. (2025) on dandiset 000727.

The dandiset holds the whole-brain two-photon imaging of Brezovec et al.: one NWB
file per fly with the raw GCaMP6f (green) and tdTomato (red) volumes, a processed
green series in the FDA space, and FicTrac walking data at 50 Hz.

The paper's structural connectivity (SC) and its ROI atlases are outside the
dataset. They come from

- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add
  (CODE_COMMIT): the resized FDA template, brain mask, fibre mask, the hemibrain
  neuropil atlas (atlas/hemiroi, 114 ROIs), the ROI names (data/hemiroi.mat) and
  the FlyEM cf0.8 SC of the 114 ROIs (results/sc/hemiroi_connectlist.mat);
- the paper's Zenodo record 10.5281/zenodo.15532272 (ZENODO_URL), the version of
  2025-05-28 that the code's README cites: the FlyWire sc140 SC matrices of the
  hemibrain ROIs, the selected-synapse SC matrices, the 99 null SC matrices of each
  permutation test, per-ROI transmitter counts and post-synapse counts.

Where each parameter comes from:

[... 143 more lines not kept]
```

**Agent**

Let me test whether single-threaded ANTs makes the registration repeatable, and what it costs.

**Agent calls Bash**

```bash
cd entries/okuno-2025; cat > $TMPDIR/dt.py <<'E'
import os, sys, time
os.environ["ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS"] = sys.argv[1]
import numpy as np, ants, flyfc
tm, tz = flyfc.code_nifti("template/thresholded_FDACal.nii.gz")
tmpl = ants.from_numpy(tm, spacing=tuple(float(v) / 1000 for v in tz))
a = flyfc.list_assets()[0]
p = os.path.join(os.environ["TMPDIR"], "mean0.npy")
if os.path.exists(p): mean0 = np.load(p)
else:
    h5 = flyfc.open_nwb(a["s3"]); rd = flyfc.ChunkReader(a["s3"], h5)
    T0 = rd.shape[0]; ct = rd.chunks[0]
    mean0 = rd.mean_image({0, ct * ((T0 // ct) // 2), ct * ((T0 - 1) // ct)}); np.save(p, mean0)
cs = []
for k in range(2):
    t = time.time(); c, cc, _ = flyfc.register(mean0, tmpl, (1, 1, 1)); print("reg", round(time.time() - t), "s", cc, flush=True); cs.append(c)
ok = ~np.isnan(cs[0]).any(1) & ~np.isnan(cs[1]).any(1)
print("max abs coord diff", np.nanmax(np.abs(cs[0][ok] - cs[1][ok])))
E
time python $TMPDIR/dt.py 1
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dt.py", line 3, in <module>
    import numpy as np, ants, flyfc
ModuleNotFoundError: No module named 'numpy'

real	0m0.026s
user	0m0.024s
sys	0m0.002s
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|python" tools/entry.py | head -30; ls -a; ls .venv* envs 2>/dev/null | head
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
206:        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
208:                         f"says {entry['python']}; run `tools/entry.py lock`")
414:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
417:def python_of(entry_dir: Path) -> str:
418:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
421:    if entry.get("python"):
422:        return str(entry["python"])
431:def set_python(entry_dir: Path, version: str) -> None:
432:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
435:    line = f'python: "{version}"'
436:    if re.search(r"^python:.*$", text, re.M):
437:        text = re.sub(r"^python:.*$", line, text, count=1, flags=re.M)
447:    version = version or python_of(entry_dir)
448:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/okuno-2025/.venv/bin/python 2>&1; ls -d executed/okuno-2025/.venv 2>&1
```

```
executed/okuno-2025/.venv/bin/python
executed/okuno-2025/.venv
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; time ../../executed/okuno-2025/.venv/bin/python $TMPDIR/dt.py 1
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dt.py", line 3, in <module>
    import numpy as np, ants, flyfc
ModuleNotFoundError: No module named 'flyfc'

real	0m5.295s
user	0m2.125s
sys	0m0.252s
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; time PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/dt.py 1
```

```
reg 33 s {'affine_meansquares': 0.673174842524105, 'affine_mattes': 0.4473891399598633, 'syn': 0.8023326500052372}
reg 35 s {'affine_meansquares': 0.680589435725702, 'affine_mattes': 0.4473891399598633, 'syn': 0.8022496019055586}
max abs coord diff 8.553375244140625

real	1m22.108s
user	1m18.160s
sys	0m3.149s
```

**Agent calls Bash**

```bash
cd  f=$(executed/okuno-2025/.venv/bin/python -c "import ants.registration.interface as m;print(m.__file__)"); grep -n "random_seed\|aff_metric\|Regular\|Random\|sampling" $f | head -60
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ants.registration.interface as m;print(m.__file__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'ants.registration.interface'
```

**Agent calls Bash**

```bash
cd  d=$(executed/okuno-2025/.venv/bin/python -c "import ants,os;print(os.path.dirname(ants.__file__))"); grep -rn "random_seed\|Regular\|\"Random\|aff_random" $d/registration/*.py | head -40
```

```
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:34:    aff_random_sampling_rate=0.2,
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:105:    aff_random_sampling_rate : scalar
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:335:        aff_random_sampling_rate = 1.0
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:481:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:502:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:508:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:529:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:550:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:571:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/site-packages/ants/registration/registration.py:577:            "--metric", "%s[%s,%s,1,%s,regular,%s]" % (aff_metric, fixed_str, moving_str, aff_sampling, aff_random_sampling_rate),
executed/okuno-2025/.venv/lib/python3.13/si
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  d=$(executed/okuno-2025/.venv/bin/python -c "import ants,os;print(os.path.dirname(ants.__file__))"); sed -n 1020,1035p $d/registration/registration.py; grep -n "def registration\|kwargs" $d/registration/registration.py | head; cat $d/config.py 2>/dev/null | head -40; executed/okuno-2025/.venv/bin/python -c "import ants;print(ants.__version__)"
```

```
itertools.chain.from_iterable(
                itertools.repeat(x, 1) if isinstance(x, str) else x
                for x in args
            )
        )

    # ------------------------------------------------------------

    if ants.config._random_seed is not None:
        args.append("--random-seed")
        args.append(str(ants.config._random_seed))

    if restrict_transformation is not None:
        args.append("-g")
        args.append(restrict_transformationchar)

20:def registration(
48:    **kwargs
165:    kwargs : keyword args
1116:    **kwargs
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  d=$(executed/okuno-2025/.venv/bin/python -c "import ants,os;print(os.path.dirname(ants.__file__))"); grep -n "kwargs" -A3 $d/registration/registration.py | sed -n 1,30p; grep -rn "set_ants_deterministic\|config" $d/__init__.py
```

```
48:    **kwargs
49-):
50-    """
51-    Register a pair of images either through the full or simplified
--
165:    kwargs : keyword args
166-        extra arguments
167-
168-    Returns
--
1116:    **kwargs
1117-):
1118-    """
1119-    Correct time-series data for motion.
--
1148:        kwargs: keyword args
1149-            extra arguments - these extra arguments will control the details of registration that is performed. see ants registration for more.
1150-
1151-    Returns
--
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; sed -i 's/^import numpy as np, ants, flyfc/import numpy as np, ants, flyfc\nprint(hasattr(ants, "set_ants_deterministic"))\nfrom ants import config as _c\n_orig = flyfc.register\ndef _reg(*a, **k):\n    _c._random_seed = k.get("seed", 1); return _orig(*a, **k)\nflyfc.register = _reg/' $TMPDIR/dt.py; time PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/dt.py 1
```

```
False
reg 42 s {'affine_meansquares': 0.6721018122870789, 'affine_mattes': 0.7361381682370615, 'syn': 0.8253078014017631}
reg 42 s {'affine_meansquares': 0.6721018122870789, 'affine_mattes': 0.7361381682370615, 'syn': 0.8253078014017631}
max abs coord diff 0.0

real	1m29.574s
user	1m25.802s
sys	0m0.938s
```

**Agent calls Bash**

```bash
cd  date -u; grep -n "M1\|motion\|slice" claims/okuno-2025.yaml | head -20; grep -n "^def \|^class \|    def " entries/okuno-2025/flyfc.py
```

```
Mon Nov 16 01:57:45 UTC 2026
28:# template. It does not hold the NWB-to-NIfTI extraction or the SPM12 and ANTs registration
40:# Locomotion across the Drosophila Brain", names these data.
52:# M1 Preprocessing (Methods, Preprocessing). SPM12 motion and slice-timing correction (code
122:# O2 The SPM12 and ANTs settings of M1 are not given in the paper or the code. The author uses
123:#    SPM12 defaults (realign to the mean, slice timing to the middle slice) and ANTs SyN with
150:    matter, 6 and 24 head motion, aCompCor, tCompCor, polynomial). Readings for "optimal"; (a)
91:def list_assets():
109:def open_nwb(s3):
113:class ChunkReader:
119:    def __init__(self, s3, h5, path=GREEN, threads=16):
133:    def _get(self, ci):
148:    def slices(self, zs):
157:            def submit(z):
171:    def mean_image(self, tstarts):
189:def code_file(name):
202:def code_nifti(name):
214:def zenodo_member(name):
223:def load_mat(b):
239:def load_sc(b):
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; sed -n 86,190p flyfc.py; sed -n 440,500p flyfc.py
```

```
SUBJECT_IDS = [1, 2, 3, 4, 5, 6, 8, 9]  # code's sbjids, 1-based, flies in name order
NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)


# --------------------------------------------------------------------------- archive
def list_assets():
    """NWB assets of the pinned version, sorted by path, with their S3 URLs."""
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        for a in r["results"]:
            if a["path"].endswith(".nwb"):
                out.append(a)
        url = r["next"]
    out.sort(key=lambda a: a["path"])
    for a in out:
        meta = requests.get(f"{API}/assets/{a['asset_id']}/", timeout=60).json()
        a["s3"] = [u for u in meta["contentUrl"] if "s3" in u][0]
        a["subject"] = a["path"].split("/")[0].replace("sub-", "")
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l attempts/okuno-2025-01.yaml; grep -n "^[a-z_]*:\|^  - claim:\|^- claim" attempts/okuno-2025-01.yaml | head -80; ls questions/ | grep okuno; python - <<'E'
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for o in nb['cells'][3].get('outputs',[]): print(o.get('text','')[:1500])
E
```

```
725 attempts/okuno-2025-01.yaml
1:schema_version: 3
2:id: okuno-2025-01
3:datasets:
9:paper: doi:10.7554/elife.107990.1
10:date: '2026-11-10'
11:entry: okuno-2025
12:provenance:
23:inputs:
36:outcomes:
37:- claim: fig1-poltcomp-optimal
47:- claim: fig2b-distkm-smoothing-optimum
55:- claim: figs2-1b-sckm-smoothing
63:- claim: fig2c-smoothing-plus-poltcomp
71:- claim: figs2-1d-highpass-degrades
79:- claim: fig2d-log-decline
87:- claim: fig2d-fly-values
95:- claim: fig2d-ten-thousand-rois
103:- claim: discussion-twenty-rois
111:- claim: fig3d-confidence-threshold
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i in [3,11,13,17,19,23,26,29,43]: print(i,''.join(nb['cells'][i]['source']));print('----')
"; grep -n "GREEN =\|grid_spacing" flyfc.py
```

```
3 assets = flyfc.list_assets()
print(len(assets), "NWB files")
meta = []
for a in assets:
    h5 = flyfc.open_nwb(a["s3"])
    g = h5[flyfc.GREEN]
    st = h5["acquisition/TwoPhotonSeriesFunctionalGreen/starting_time"]
    gs = h5["general/optophysiology/ImagingPlaneGCaMP6fFunctional/grid_spacing"][()]
    spd = h5["processing/behavior/FicTrac/SpatialSeriesMovementSpeed"]
    proc = h5["processing/ophys/TwoPhotonSeriesFunctionalGreenProcessed/data"]
    row = dict(subject=a["subject"], size_gb=round(a["size"] / 1e9, 1), green=g.shape, dtype=str(g.dtype),
               rate=round(float(st.attrs["rate"]), 6), spacing_um=tuple(np.round(gs * 1e6, 3)),
               speed_n=spd["data"].shape[0], speed_rate=float(spd["starting_time"].attrs["rate"]),
               speed_desc=spd.attrs["description"], processed=proc.shape,
               sex=h5["general/subject/sex"][()].decode(),
               genotype=h5["general/subject/genotype"][()].decode())
    meta.append(row)
    h5.close()
for r in meta:
    print(r["subject"], r["size_gb"], "GB green", r["green"], r["dtype"], "rate", r["rate"], "Hz spacing", r["spacing_um"],
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; sed -n 60,86p flyfc.py; sed -n 330,380p flyfc.py; sed -n 598,673p flyfc.py
```

```
"""

import gzip
import io
import os
import tarfile
import time
import zipfile
import zlib
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import remfile
import requests
import scipy.sparse as sp
from scipy import stats

DANDISET = "000727"
VERSION = "0.240106.0043"
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
p='flyfc.py'; s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a,s.count(a)); s=s.replace(a,b)
rep("""  resized FDA template"; Ext. Data Fig. 1-1a). Defaults of antspy's "SyN" are a
  standard choice (claims file, O2).""","""  resized FDA template"; Ext. Data Fig. 1-1a). Defaults of antspy's "SyN" are a
  standard choice (claims file, O2). The native voxel size is each fly's NWB
  grid_spacing. antspy 0.6.3 silently ignores a random_seed argument to
  ants.registration; the seed is set through ants.config and ITK runs on one thread
  (ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS=1), which makes a registration repeatable
  (shown in the notebook). Another seed still gives another registration.""")
rep("""NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)
""","""NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # fly-087's NWB grid_spacing (m -> mm)
GRID_SPACING = "general/optophysiology/ImagingPlaneGCaMP6fFunctional/grid_spacing"
os.environ.setdefault("ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS", "1")  # read when ITK starts
""")
rep("""def open_nwb(s3):
    return h5py.File(remfile.File(s3), "r")
""","""def open_nwb(s3):
    return h5py.File(remfile.File(s3), "r")


def spacing_mm(h5):
    \"\"\"The fly's native voxel size in mm, from the NWB grid_spacing (in m).\"\"\"
    return tuple(float(v) * 1000 for v in h5[GRID_SPACING][()])
""")
rep("""def choose_flip(mean, tmpl_img, seed=1):
    \"\"\"Correlation with the template after an affine registration, for each flip.\"\"\"
    import ants
    out = {}""","""def _seed(seed):
    \"\"\"antspy 0.6.3 passes --random-seed to antsRegistration only from ants.config.\"\"\"
    from ants import config
    config._random_seed = seed


def choose_flip(mean, tmpl_img, seed=1, spacing=NATIVE_SPACING_MM):
    \"\"\"Correlation with the template after an affine registration, for each flip.\"\"\"
    import ants
    _seed(seed)
    out = {}""")
rep("""        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)
        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", random_seed=seed)""",
"""        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=spacing)
        r = ants.registration(tmpl_img, mov, type_of_transform="Affine")""")
rep("""def register(mean, tmpl_img, fl, seed=1):""","""def register(mean, tmpl_img, fl, seed=1, spacing=NATIVE_SPACING_MM):""")
rep("""    import ants
    m = _flip(mean, fl).astype(np.float32)
    m = np.clip(m / np.percentile(m, 99.5), 0, 1)
    mov = ants.from_numpy(m, spacing=NATIVE_SPACING_MM)""","""    import ants
    _seed(seed)
    m = _flip(mean, fl).astype(np.float32)
    m = np.clip(m / np.percentile(m, 99.5), 0, 1)
    mov = ants.from_numpy(m, spacing=spacing)""")
rep("""                              random_seed=seed, aff_iterations=(2100, 1200, 1200, 10),""","""                              aff_iterations=(2100, 1200, 1200, 10),""")
rep("""                          initial_transform=aff[best][1], random_seed=seed)""","""                          initial_transform=aff[best][1])""")
rep("""        ci = ants.from_numpy(g, spacing=NATIVE_SPACING_MM)""","""        ci = ants.from_numpy(g, spacing=spacing)""")
rep("""    mean = rd.mean_image(tstarts)
    fl = flip
    coords, cc, warped = register(mean, tmpl_img, fl)""","""    mean = rd.mean_image(tstarts)
    vox = spacing_mm(h5)
    fl = flip
    coords, cc, warped = register(mean, tmpl_img, fl, spacing=vox)""")
rep("""        c2, _, _ = register(mean, tmpl_img, fl, seed=seed)""","""        c2, _, _ = register(mean, tmpl_img, fl, seed=seed, spacing=vox)""")
rep("""            dmm = np.sqrt((((coords[ok] - c2[ok]) * np.array(NATIVE_SPACING_MM) * 1000) ** 2).sum(1))""",
"""            dmm = np.sqrt((((coords[ok] - c2[ok]) * np.array(vox) * 1000) ** 2).sum(1))""")
rep("""    nvox = X * Y
    for z, a in rd.slices(range(Z)):
        xz = a.reshape(T, nvox).astype(np.float32)
        cols = slice(z * nvox, (z + 1) * nvox)""","""    nvox = X * Y
    proj = np.zeros((T, X, Y), np.float32)  # sum over z of each volume, for the motion estimate
    for z, a in rd.slices(range(Z)):
        proj += a
        xz = a.reshape(T, nvox).astype(np.float32)
        cols = slice(z * nvox, (z + 1) * nvox)""")
rep("""    h5.close()
    return dict(subject=asset["subject"], R=R.T,""","""    h5.close()
    shift = inplane_shift(proj) * np.array(vox[:2]) * 1000
    del proj
    return dict(subject=asset["subject"], R=R.T, shift=shift, vox=vox,""")
rep("""# --------------------------------------------------------------------------- nuisance and FC""","""def inplane_shift(proj):
    \"\"\"Rigid in-plane shift (T x 2, voxels along x and y) of each volume's z-sum
    against the mean over volumes, by phase correlation with a parabolic sub-voxel
    peak. A check of whether the raw series moves (the paper corrects motion with
    SPM12, Methods, Preprocessing); it sees no motion along z.\"\"\"
    ref = np.fft.rfft2(proj.mean(0) - proj.mean())
    T, X, Y = proj.shape
    out = np.empty((T, 2))
    for t0 in range(0, T, 256):
        F = np.fft.rfft2(proj[t0:t0 + 256] - proj[t0:t0 + 256].mean((1, 2), keepdims=True))
        Rm = F * np.conj(ref)
        c = np.fft.irfft2(Rm / np.maximum(np.abs(Rm), 1e-12), s=(X, Y))
        for k in range(c.shape[0]):
            i, j = np.unravel_index(np.argmax(c[k]), (X, Y))
            sh = []
            for ax, (n, q) in enumerate([(X, i), (Y, j)]):
                lo = c[k][(q - 1) % n, j] if ax == 0 else c[k][i, (q - 1) % n]
                hi = c[k][(q + 1) % n, j] if ax == 0 else c[k][i, (q + 1) % n]
                d = lo - 2 * c[k][i, j] + hi
                frac = 0.5 * (lo - hi) / d if d != 0 else 0.0
                sh.append(((q + n // 2) % n - n // 2) + frac)
            out[t0 + k] = sh
    return out


# --------------------------------------------------------------------------- nuisance and FC""")
rep('''def roi_series(fly, nuisance):
    """ROI series (T x ROIs) for nuisance '' (none) or 'poltcomp'."""
    Y = fly["R"].T.copy()
    Y = Y - Y.mean(0)
    if nuisance == "poltcomp":
        Sd = poly_regressors(Y.shape[0])
        Xn = np.hstack([Sd, tcompcor(fly["top_ts"], Sd)])''','''def roi_series(fly, nuisance, extra=None):
    """ROI series (T x ROIs) for nuisance '' (none) or 'poltcomp'; extra: further
    nuisance columns (T x k) added to Poly-tCompCor (a variant)."""
    Y = fly["R"].T.copy()
    Y = Y - Y.mean(0)
    if nuisance == "poltcomp":
        Sd = poly_regressors(Y.shape[0])
        Xn = np.hstack([Sd, tcompcor(fly["top_ts"], Sd)] + ([] if extra is None else [extra]))''')
open(p,'w').write(s)
E
grep -n "NATIVE_SPACING_MM" flyfc.py
```

```
91:NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # fly-087's NWB grid_spacing (m -> mm)
287:def choose_flip(mean, tmpl_img, seed=1, spacing=NATIVE_SPACING_MM):
300:def register(mean, tmpl_img, fl, seed=1, spacing=NATIVE_SPACING_MM):
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
p='flyfc.py'; s=open(p).read()
s=s.replace('NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # fly-087\'s NWB grid_spacing (m -> mm)\n','')
s=s.replace('seed=1, spacing=NATIVE_SPACING_MM)','spacing, seed=1)')
open(p,'w').write(s)
E
grep -n "NATIVE_SPACING\|def choose_flip\|def register\|register(" flyfc.py
cat > $TMPDIR/ts.py <<'E'
import numpy as np, flyfc
from scipy.ndimage import shift, gaussian_filter
rng=np.random.default_rng(0)
base=gaussian_filter(rng.random((256,128)),3)*1000
true=np.column_stack([np.sin(np.arange(50)/5)*1.7, np.linspace(-0.6,0.9,50)])
proj=np.stack([shift(base,s,order=3,mode='wrap')+rng.normal(0,0.5,base.shape) for s in true]).astype(np.float32)
est=flyfc.inplane_shift(proj)
est-=est.mean(0); tt=true-true.mean(0)
print(np.abs(est-tt).max(), np.corrcoef(est[:,0],tt[:,0])[0,1])
E
PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/ts.py
```

```
286:def choose_flip(mean, tmpl_img, spacing, seed=1):
299:def register(mean, tmpl_img, fl, spacing, seed=1):
424:    coords, cc, warped = register(mean, tmpl_img, fl, spacing=vox)
431:        c2, _, _ = register(mean, tmpl_img, fl, seed=seed, spacing=vox)
2.085431091637249 0.2755035027458566
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; cat > $TMPDIR/ts2.py <<'E'
import numpy as np, flyfc
from scipy.ndimage import shift, gaussian_filter
rng=np.random.default_rng(0)
base=gaussian_filter(rng.random((256,128)),3)*1000
true=np.array([[0,0],[2,0],[0,3],[1.5,-0.5],[-2,1]])
proj=np.stack([shift(base,s,order=3,mode='wrap') for s in true]).astype(np.float32)
print(flyfc.inplane_shift(proj))
E
PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/ts2.py
```

```
[[-2.0075893   0.28770947]
 [-0.00665773  0.29657367]
 [-2.00825533  3.32185465]
 [-0.0322249  -0.61566508]
 [-4.01303484  1.28308171]]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
p='flyfc.py'; s=open(p).read()
a='''        c = np.fft.irfft2(Rm / np.maximum(np.abs(Rm), 1e-12), s=(X, Y))'''
b='''        c = np.fft.irfft2(Rm, s=(X, Y))'''
assert a in s; s=s.replace(a,b)
s=s.replace("against the mean over volumes, by phase correlation with a parabolic sub-voxel","against the mean over volumes, by cross-correlation with a parabolic sub-voxel")
open(p,'w').write(s)
E
PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/ts2.py; PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/ts.py
```

```
[[-0.28925082 -0.61151159]
 [ 1.71252084 -0.61107275]
 [-0.28983083  2.39142069]
 [ 1.16474153 -1.13950571]
 [-2.28389922  0.38488045]]
0.12775538475309706 0.9998743433761046
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; date -u; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i in [4,6,10,12,16,18,22,42]: print(i,''.join(nb['cells'][i]['source']));print('----')
"
```

```
Mon Nov 16 01:59:16 UTC 2026
4 Orientation and registration. The template and the masks come from the paper's code. The
native mean image of the first fly is shown beside the template, and the correlation with the
template after an affine registration is printed for each of the eight axis flips.
----
6 In both images the slices near z = 6 hold two small dorsal-anterior structures near the midline and
the slices near z = 42 hold the optic lobes, and the dorsoventral axis runs the same way, so no
flip is applied along y or z. Left and right cannot be told apart from the image: the affine correlations printed above are
not a reliable guide (a single affine start lands in different optima from one seed to the next).
No flip is assumed; the main FC-SC results are shown with left and right ROIs swapped, and the
orientation is checked against the paper's own per-region values (fig3e section).

Reduce each fly. Each fly's raw green series is streamed once (about 7 GB per fly) and reduced
to the 114 ROI mean series and the 1000 highest-SD voxels (`flyfc.process_fly`).
----
10 Subject order and the behaviour clock. The paper's code holds the per-volume speed and the
walking regressor it computed for its nine flies (`data/behavior.mat`). Computing them from the
dandiset's FicTrac speed, with the code's offset of 104.654892 ms, and comparing fly by fly
checks both the subject order and the alignment of the behaviour to the volumes.
----
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
import json
p='reproduce_okuno_2025.ipynb'; nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
rep(1,'os.environ.setdefault("OMP_NUM_THREADS", "4")\n','os.environ.setdefault("OMP_NUM_THREADS", "4")\nos.environ["ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS"] = "1"  # with a set seed, makes ANTs registration repeatable\n')
setsrc(2,"""## Data check

The files, their metadata, and what the analysis reads from them. ANTs registration draws random
samples. antspy 0.6.3 ignores the `random_seed` argument of `ants.registration` (it falls into
`**kwargs`), so the earlier runs of this attempt were unseeded and their registrations, and every
number resting on them, changed from run to run. The seed is now set through `ants.config` and ITK
runs on one thread; the orientation cell below registers one mean image twice with the same seed
to show that the result repeats. A registration with another seed (11) is a different local
optimum, and how far it moves the voxels and the results is shown for every fly (cell after the
reduction). No other random numbers are drawn.
""")
rep(4,"template after an affine registration is printed for each of the eight axis flips.","template after an affine registration is printed for each of the eight axis flips. The first\nfly's mean image is registered twice with seed 1 to show that a seeded registration repeats.")
rep(5,"mean0 = rd0.mean_image({0, ct * ((T0 // ct) // 2), ct * ((T0 - 1) // ct)})\nh5.close()\nflips = flyfc.choose_flip(mean0, tmpl)",
"mean0 = rd0.mean_image({0, ct * ((T0 // ct) // 2), ct * ((T0 - 1) // ct)})\nvox0 = flyfc.spacing_mm(h5)\nh5.close()\nflips = flyfc.choose_flip(mean0, tmpl, vox0)")
setsrc(5, src(5)+"""
# repeatability: the same mean image registered twice with seed 1
c_a, cc_a, _ = flyfc.register(mean0, tmpl, (1, 1, 1), vox0, seed=1)
c_b, cc_b, _ = flyfc.register(mean0, tmpl, (1, 1, 1), vox0, seed=1)
ok_ = ~np.isnan(c_a).any(1) & ~np.isnan(c_b).any(1)
print("two registrations with seed 1: largest coordinate difference", float(np.abs(c_a[ok_] - c_b[ok_]).max()),
      "native voxels | same field of view:", bool((np.isnan(c_a).any(1) == np.isnan(c_b).any(1)).all()), "| SyN correlation", round(cc_a["syn"], 4), round(cc_b["syn"], 4))
""")
rep(7,'"| ROIs not fully in the field of view",','"| voxel (um)", tuple(round(v * 1000, 3) for v in f["vox"]), "| ROIs not fully in the field of view",')
# motion cell after cell 13
md = {"cell_type":"markdown","metadata":{},"source":"""Motion. The paper corrects motion and slice timing with SPM12 before registration (Methods,
Preprocessing; claims file M1); this attempt does neither. To show whether the raw series moves,
each volume's sum over z is aligned to the mean over volumes by cross-correlation, giving a rigid
in-plane shift per volume (`flyfc.inplane_shift`; it cannot see motion along z). The shift is
compared with the voxel size and with walking, and fig3d is recomputed with the two shift series
added to the nuisance regressors (fig3d section).
""".splitlines(keepends=True)}
code = {"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":"""for i, f in enumerate(flies):
    d = f["shift"] - np.median(f["shift"], 0)
    mag = np.sqrt((d ** 2).sum(1))
    step = np.sqrt((np.diff(f["shift"], axis=0) ** 2).sum(1))
    print(f["subject"], "in-plane shift from the median (um): median", round(float(np.median(mag)), 2), "95th percentile", round(float(np.percentile(mag, 95)), 2),
          "max", round(float(mag.max()), 2), "| x SD", round(float(d[:, 0].std()), 2), "y SD", round(float(d[:, 1].std()), 2),
          "| volume-to-volume step 99th percentile", round(float(np.percentile(step, 99)), 2), "| r of shift size with the walking speed", round(float(np.corrcoef(mag, mscal[i])[0, 1]), 3))
print("voxel size in plane about 2.6 um")
""".splitlines(keepends=True)}
C[14:14]=[md,code]
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']): print(i,c['cell_type'],repr(''.join(c['source'])[:80]))
" | sed -n 12,25p; head -c 300 reproduce_okuno_2025.ipynb; git diff --stat .
```

```
11 code 'reg, mscal, th_speed, b_speed = flyfc.walking_regressors([f["speed"] for f in fl'
12 markdown 'The behaviour clock is checked against the imaging with a contrast: the brain-wi'
13 code 'shifts = np.arange(-60, 61, 2)\nids_all = np.arange(114)\nfor i, f in enumerate(fl'
14 markdown 'Motion. The paper corrects motion and slice timing with SPM12 before registratio'
15 code 'for i, f in enumerate(flies):\n    d = f["shift"] - np.median(f["shift"], 0)\n    '
16 markdown 'Duplicates. Recordings deposited twice would give identical speed traces or mean'
17 code 'sp = np.array([f["speed"] for f in flies])\ncsp = np.corrcoef(sp)\nnp.fill_diagona'
18 markdown "## FC and the paper's SC\n\nFC per fly is the Pearson correlation of the 114 ROI s"
19 code 'em_nc, em_sc, em_ids52 = flyfc.load_sc(flyfc.code_file("results/sc/hemiroi_conne'
20 markdown '### fig3d-flyem-vs-flywire\n\n> Against the same FC, FlyEM gives a higher matrix-l'
21 code 'lr = {}\nfor i, n in enumerate(names):\n    if "(L)" in n:\n        j = names.index'
22 code 'a = flyfc.log_sc(em_nc[np.ix_(ids, ids)]).ravel(); b = np.abs(F[np.ix_(ids, ids)'
23 markdown '**Result: FlyEM gives the higher FC-SC correlation, but both values are below th'
24 markdown '### fig3e-flyem-higher-most-regions\n\n> Per region, FlyEM gives the higher FC-SC '
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "594b4538",
   "metadata": {},
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
import json, uuid
p='reproduce_okuno_2025.ipynb'; nb=json.load(open(p))
C=nb['cells']
for c in C:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))
rep(21,'print("second registration (another seed), Poly-tCompCor, 8 flies: FlyEM"','''F_mot = flyfc.mean_zfc([flyfc.roi_series(flies[i], "poltcomp", extra=flies[i]["shift"]) for i in sel8])
print("with the two in-plane shift series added to Poly-tCompCor, 8 flies: FlyEM", round(flyfc.fcsc_r(em_nc, F_mot, ids), 4), "FlyWire", round(flyfc.fcsc_r(fw_nc, F_mot, ids), 4))
print("second registration (another seed), Poly-tCompCor, 8 flies: FlyEM"''')
i45=[i for i,c in enumerate(C) if 'g2 = flyfc.load_mat' in src(i)][0]
rep(i45,'''Tx = T[::-1].copy()''','''print("paper's positive clusters (t >", round(thp, 3), ", >= 168 voxels):", sorted((int(s) for s in flyfc.clusters(Tp > thp)[1] if s >= 168), reverse=True))
Tx = T[::-1].copy()
print("brain mask against its own left-right mirror image: fraction of voxels shared", round(float((brain & brain[::-1]).sum() / brain.sum()), 3))''')
rep(i45,'''    print("per-neuropil mean t, paper against this attempt (63 primary ROIs): r =", round(float(np.corrcoef([tab_p[k] for k in k_], [tab_a[k] for k in k_])[0, 1]), 3))''',
'''    print("per-neuropil mean t, paper against this attempt (63 primary ROIs): r =", round(float(np.corrcoef([tab_p[k] for k in k_], [tab_a[k] for k in k_])[0, 1]), 3))
    # orientation at the ROI level: this attempt's per-neuropil means with each left ROI given its right partner's value
    sw = {k: tab_a.get(k.replace("(L)", "(R)") if "(L)" in k else k.replace("(R)", "(L)"), tab_a[k]) for k in k_}
    print("per-neuropil mean t, paper against this attempt with left and right ROIs swapped: r =", round(float(np.corrcoef([tab_p[k] for k in k_], [sw[k] for k in k_])[0, 1]), 3))''')
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
s=''.join(nb['cells'][40]['source']); print(s[:1500])"
```

```
def neuropil_table(T, th, atlas):
    rows = []
    if atlas == "hemibrain":
        for i in ids:
            m = masks[i] & brain
            if m.sum():
                rows.append((names[i], m))
    else:
        for k in np.unique(jf[jf > 0]).astype(int):
            m = (jf == k) & brain
            if m.sum():
                rows.append((f"{jlab.get(k, k)} [{k}]", m))
    out = []
    for nm, m in rows:
        out.append((nm, float(T[m].mean()), float(T[m].max()), float(T[m].min()), float((T[m] > th).mean()), float((T[m] < -th).mean()), int(m.sum())))
    return out

targets_hb = {"LAL": ["LAL(R)", "LAL(L)"], "FB": ["FB"], "IPS": ["IPS(R)"], "GNG": ["GNG"]}
targets_jf = {"LAL": ["lateral accessory lobe"], "FB": ["fan-shaped body"], "IPS": ["inferior posterior slope"], "GNG": ["adult gnathal ganglion"]}
act = {}
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; cat > $TMPDIR/tp.py <<'E'
import os, time
os.environ["ITK_GLOBAL_DEFAULT_NUMBER_OF_THREADS"] = "1"
import numpy as np, ants, flyfc
tm, tz = flyfc.code_nifti("template/thresholded_FDACal.nii.gz")
tmpl = ants.from_numpy(tm, spacing=tuple(float(v) / 1000 for v in tz))
masks = flyfc.hemiroi_masks()
a = flyfc.list_assets()[1]
t=time.time()
f = flyfc.process_fly(a, tmpl, masks, repeats=(11,))
print(a["subject"], time.time()-t, f["vox"], f["cc"], f["t_reg"])
d=f["shift"]-np.median(f["shift"],0); print(np.percentile(np.sqrt((d**2).sum(1)),[50,95,100]))
np.save(os.path.join(os.environ["TMPDIR"],"shift1.npy"), f["shift"])
E
time PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/tp.py
```

```
fly-089 137.85671854019165 (0.0025538194451299504, 0.0026703365114121003, 0.005) {'affine_meansquares': 0.6773958949901121, 'affine_mattes': 0.43824131882136363, 'syn': 0.8026203817449825, 'repeat_displacement_um_median': 43.63536085034354, 'repeat_displacement_um_p95': 92.73013837737771} 93.5338077545166
[1.11960852 3.76832721 7.94284509]

real	2m26.830s
user	3m43.128s
sys	0m17.246s
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python -c "
import flyfc
a=flyfc.list_assets()[0]; h=flyfc.open_nwb(a['s3'])
for k in h['acquisition']: print(k, h['acquisition'][k]['data'].shape, h['acquisition'][k]['data'].chunks)
"
```

```
TwoPhotonSeriesAnatomicalGreen (100, 1024, 512, 241) (9, 1024, 512, 1)
TwoPhotonSeriesAnatomicalRed (100, 1024, 512, 241) (9, 1024, 512, 1)
TwoPhotonSeriesFunctionalGreen (3384, 256, 128, 49) (152, 256, 128, 1)
TwoPhotonSeriesFunctionalRed (3384, 256, 128, 49) (152, 256, 128, 1)
Video: fictrac-20200228_161226-raw (0, 0, 0) None
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
p='flyfc.py'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a; s=s.replace(a,b)
rep('''GREEN = "acquisition/TwoPhotonSeriesFunctionalGreen/data"\n''','''GREEN = "acquisition/TwoPhotonSeriesFunctionalGreen/data"\nRED = "acquisition/TwoPhotonSeriesFunctionalRed/data"\n''')
rep('''    h5.close()
    shift = inplane_shift(proj) * np.array(vox[:2]) * 1000
    del proj
    return dict(subject=asset["subject"], R=R.T, shift=shift, vox=vox,''','''    shift_green = inplane_shift(proj) * np.array(vox[:2]) * 1000
    # the same from the structural tdTomato channel, which carries no activity, over the middle 20 slices
    rr = ChunkReader(asset["s3"], h5, path=RED)
    proj[:] = 0
    for z, a in rr.slices(range(15, 35)):
        proj += a
    shift = inplane_shift(proj) * np.array(vox[:2]) * 1000
    del proj
    h5.close()
    return dict(subject=asset["subject"], R=R.T, shift=shift, shift_green=shift_green, vox=vox,''')
rep('''                mb_read=rd.bytes_read / 1e6)''','''                mb_read=(rd.bytes_read + rr.bytes_read) / 1e6)''')
open(p,'w').write(s)
p='reproduce_okuno_2025.ipynb'
import json; nb=json.load(open(p)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
setsrc(14,"""Motion. The paper corrects motion and slice timing with SPM12 before registration (Methods,
Preprocessing; claims file M1); this attempt does neither. To show whether the raw series moves,
each volume's sum over the middle 20 slices (z = 15 to 34) of the structural tdTomato channel is
aligned to the mean over volumes by cross-correlation, giving a rigid in-plane shift per volume
(`flyfc.inplane_shift`; it cannot see motion along z). The same from the green channel's sum over
all slices is printed beside it. The shift is compared with the voxel size and with walking, and
fig3d is recomputed with the two tdTomato shift series added to the nuisance regressors (fig3d
section).
""")
setsrc(15,"""for i, f in enumerate(flies):
    for lab_, sh in [("tdTomato", f["shift"]), ("green", f["shift_green"])]:
        d = sh - np.median(sh, 0)
        mag = np.sqrt((d ** 2).sum(1))
        step = np.sqrt((np.diff(sh, axis=0) ** 2).sum(1))
        print(f["subject"], f"{lab_:8s} in-plane shift from the median (um): median", round(float(np.median(mag)), 2), "95th percentile", round(float(np.percentile(mag, 95)), 2),
              "max", round(float(mag.max()), 2), "| x SD", round(float(d[:, 0].std()), 2), "y SD", round(float(d[:, 1].std()), 2),
              "| volume-to-volume step 99th percentile", round(float(np.percentile(step, 99)), 2), "| r of shift size with walking speed", round(float(np.corrcoef(mag, mscal[i])[0, 1]), 3))
    print(f["subject"], "r between the tdTomato and green shift series: x", round(float(np.corrcoef(f["shift"][:, 0], f["shift_green"][:, 0])[0, 1]), 3),
          "y", round(float(np.corrcoef(f["shift"][:, 1], f["shift_green"][:, 1])[0, 1]), 3))
print("voxel size in plane about 2.6 um")
""")
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
date -u
```

```
Mon Nov 16 02:02:49 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; cat > $TMPDIR/tr.py <<'E'
import os, time, numpy as np, flyfc
a = flyfc.list_assets()[1]; h5=flyfc.open_nwb(a["s3"]); t=time.time()
rr = flyfc.ChunkReader(a["s3"], h5, path=flyfc.RED)
T,X,Y,Z=rr.shape; proj=np.zeros((T,X,Y),np.float32)
for z, x in rr.slices(range(15, 35)): proj += x
sh=flyfc.inplane_shift(proj)*np.array(flyfc.spacing_mm(h5)[:2])*1000
print(time.time()-t, rr.bytes_read/1e6)
d=sh-np.median(sh,0); print(np.percentile(np.sqrt((d**2).sum(1)),[50,95,100]))
g=np.load(os.path.join(os.environ["TMPDIR"],"shift1.npy")); print(np.corrcoef(sh[:,0],g[:,0])[0,1], np.corrcoef(sh[:,1],g[:,1])[0,1])
E
PYTHONPATH=. ../../executed/okuno-2025/.venv/bin/python $TMPDIR/tr.py
```

```
20.4385769367218 3249.808932
[0.89164379 3.6977888  5.70126638]
0.9643437196469453 0.886981814430268
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/okuno-2025 2>&1 | tail -30; date -u
```

```
Mon Nov 16 02:03:24 UTC 2026
Installed kernelspec registry-okuno-2025 in executed/okuno-2025/.venv/share/jupyter/kernels/registry-okuno-2025
0 error(s)
pass  reproduce_okuno_2025.ipynb  (2156 s)
pass  connectome_okuno_2025.ipynb  (1196 s)

real	56m5.300s
user	59m0.651s
sys	6m21.804s
Mon Nov 16 02:59:29 UTC 2026
```

**Agent**

The notebooks ran (36 min and 20 min). Now let me read all the new outputs.

**Agent calls Bash**

```bash
cd  python - <<'E' > $TMPDIR/out.txt
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  print(f"===== cell {i}")
  for o in c.get('outputs',[]):
    if 'text' in o: print(''.join(o['text']))
    elif 'data' in o and 'text/plain' in o['data'] and 'image/png' not in o['data']: print(''.join(o['data']['text/plain']))
E
wc -l $TMPDIR/out.txt; sed -n 1,200p $TMPDIR/out.txt | cut -c1-600
```

```
374 /tmp/claude-1001/out.txt
===== cell 1
dandiset 000727 version 0.240106.0043
code commit 4b92add4a44f641ab6add809ff6b0e0d6110b50c zenodo record 15532272

===== cell 3
9 NWB files

fly-087 69.0 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-089 66.6 GB green (3384, 256, 128, 49) uint16 rate 1.879715 Hz spacing (np.float64(2.554), np.float64(2.67), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-094 67.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-097 66.9 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-098 67.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-099 68.2 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.549), np.float64(2.675), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-100 67.7 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.578), np.float64(2.646), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-101 67.8 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.578), np.float64(2.646), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 314, 146, 91) | F
fly-105 67.3 GB green (3384, 256, 128, 49) uint16 rate 1.879714 Hz spacing (np.float64(2.611), np.float64(2.611), np.float64(5.0)) um | speed 90000 samples at 50.0 Hz | processed (3384, 
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,374p $TMPDIR/out.txt | cut -c1-700
```

```
===== cell 28
outNTypes (114, 7)
main | DA r=-0.166 p=0.192; SER r=-0.010 p=0.935; GABA r=-0.096 p=0.456; GLUT r=0.251 p=0.0475; ACH r=-0.040 p=0.757; OCT r=-0.317 p=0.0113
no nuisance | DA r=-0.233 p=0.0657; SER r=-0.225 p=0.076; GABA r=-0.006 p=0.96; GLUT r=0.375 p=0.00244; ACH r=-0.085 p=0.509; OCT r=-0.145 p=0.258
nine flies | DA r=-0.165 p=0.197; SER r=0.013 p=0.919; GABA r=-0.082 p=0.523; GLUT r=0.258 p=0.0413; ACH r=-0.068 p=0.599; OCT r=-0.314 p=0.0122
left-right swapped | DA r=-0.016 p=0.898; SER r=0.037 p=0.771; GABA r=-0.054 p=0.672; GLUT r=0.331 p=0.00812; ACH r=-0.210 p=0.099; OCT r=-0.237 p=0.0615
paper's own per-region values (Zenodo auc file) | DA r=0.209 p=0.0996; SER r=-0.170 p=0.183; GABA r=-0.252 p=0.0465; GLUT r=-0.196 p=0.123; ACH r=0.395 p=0.00136; OCT r=-0.313 p=0.0124
MAIN: ACh r = -0.040 (p = 0.757); GABA r = -0.096 (p = 0.456)

===== cell 31
fig4e-unsegregated-higher | target sp10db3000mi1_only1 synapse total 2373104 neuron total 137694 | null rd185-20 n = 99 synapse totals mean 2309356 SD 299896 | totals test p = 0.832

fig4f-segregated-lower | target sp90db3000mi1 synapse total 28954898 neuron total 713783 | null rd1560-80 n = 99 synapse totals mean 28360686 SD 1270979 | totals test p = 0.64

fig4i-reciprocal-higher | target rc20_only1 synapse total 1630011 neuron total 184921 | null rd140-15 n = 99 synapse totals mean 1594440 SD 191034 | totals test p = 0.852

===== cell 32
paper (deposited R) neuron r=0.7332 null 0.6892+-0.0017 z=+25.7 p=6.22e-146 (null range 0.6839 to 0.6948) | synapse r=0.7096 null 0.6754+-0.0025 z=+13.7 p=6.51e-43
main                neuron r=0.6257 null 0.5874+-0.0016 z=+23.5 p=3.09e-122 (null range 0.5838 to 0.5907) | synapse r=0.5774 null 0.5603+-0.0023 z=+7.4 p=1.81e-13
no nuisance         neuron r=0.5757 null 0.5984+-0.0021 z=-11.0 p=2.93e-28 (null range 0.5939 to 0.6060) | synapse r=0.5570 null 0.5894+-0.0025 z=-12.8 p=2.53e-37
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python -c "
import json;nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i in [0,6,23,26,29,33,35,37,38,42,44,46,56]: print('=====',i);print(''.join(nb['cells'][i]['source']))
"
```

```
===== 0
# Reproducing Okuno et al. (2025) from dandiset 000727

Paper. Okuno T, Woodward A, Okano H, Hata J (2025). Functional connectivity, structural
connectivity, and inter-individual variability in *Drosophila melanogaster*. eLife reviewed
preprint 107990 version 1, [doi:10.7554/elife.107990.1](https://doi.org/10.7554/elife.107990.1).
The claims file was written from the publisher's HTML of version 1 (main text, Methods, figure
legends and the legends of the Extended Data figures); no PDF was available.

Dandiset. [DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), version
0.240106.0043, the version the paper's Methods and Data availability cite. It is also the only
published version; the draft lists the same 18 assets with the same total size.

What the dandiset holds. The whole-brain two-photon imaging of Brezovec et al. that the paper
reuses: 9 flies, one NWB file each, with the raw GCaMP6f and tdTomato volumes (256 x 128 x 49 voxels,
3384 volumes at 1.88 Hz), anatomical stacks, a green series already registered to the FDA space by
Brezovec et al. (high-pass filtered and z-scored), and FicTrac walking data at 50 Hz.

Outside inputs (the claims file says the paper relies on them; both are pinned):
- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add: the resized FDA
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 505,555p tools/entry.py; grep -n "def run_entry\|stale\|fingerprint\|hash" tools/entry.py | head -30
```

```
def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git ls-files executed | head; git status --short | head -30
```

```
M entries/okuno-2025/flyfc.py
 M entries/okuno-2025/reproduce_okuno_2025.ipynb
 M tools/agent_run.py
 M tools/backfill_summaries.py
 M tools/build_reuse_targets.py
 M tools/build_site.py
 M tools/entry.py
 M tools/journals.py
 M tools/notify.py
 M tools/paper_match.py
 M tools/papers_manifest.py
 M tools/runner/chain.sh
 M tools/runner/describe.py
 M tools/runner/run_requests.py
 M tools/site_assets/app.css
 M tools/site_assets/list.js
 M tools/site_assets/progress.js
?? .bash_profile
?? .bashrc
?? .gitconfig
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E' > $TMPDIR/con.txt
import json
nb=json.load(open('executed/okuno-2025/connectome_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']!='code': continue
  print(f"===== cell {i}")
  for o in c.get('outputs',[]):
    if 'text' in o: print(''.join(o['text']))
E
for v in 0.756 0.761 0.1332 852.3 0.363 138144 138,144 212 ; do echo "$v: $(grep -c -- "$v" $TMPDIR/con.txt)"; done
```

```
0.756: 1
0.761: 1
0.1332: 1
852.3: 2
0.363: 1
138144: 6
138,144: 0
212: 2
```

**Agent calls Bash**

```bash
cd  sed -n 1,36p attempts/okuno-2025-01.yaml; sed -n 111,220p attempts/okuno-2025-01.yaml
```

```
schema_version: 3
id: okuno-2025-01
datasets:
- archive: dandi
  id: '000727'
  version: 0.240106.0043
  doi: 10.48324/dandi.000727/0.240106.0043
  relation: reuses
paper: doi:10.7554/elife.107990.1
date: '2026-11-10'
entry: okuno-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 318,725p attempts/okuno-2025-01.yaml
```

```
- claim: fig4e-unsegregated-higher
  outcome: reproduced
  notebook: reproduce_okuno_2025.ipynb
  output: claim:fig4e-unsegregated-higher
  measured: 2373104
  assumed: true
  notes: Unsegregated SC (code target sp10db3000mi1_only1) against the 99 rd185-20 null SC matrices, Poly-tCompCor, eight
    flies. Neuron SC r = 0.636 against null 0.598 +- 0.0016 (z = +23.9, p = 3e-126); synapse SC r = 0.586 against 0.570 +-
    0.0023 (z = +6.6, p = 3e-11); both above the null at p < 0.05/6. The paper's own deposited R values for the same SC matrices
    give z = +25.7 and +13.7. The selected synapse total is 2,373,104 and the null totals do not differ from it (p = 0.832).
    Nine flies agree; with left and right swapped the synapse SC is not different from the null (p = 0.88). Without nuisance
    removal both are below the null (z = -9.0 and -10.6), so the result needs Poly-tCompCor, here applied to data without
    motion correction.
  deviations:
  - 'Registration (claims file O2). The paper gives no SPM12 or ANTs settings. No SPM12 motion or slice-timing correction
    was applied (claims file M1 requires it): a streamed in-plane realignment and slice-timing correction were written in
    the revision but did not finish within the notebook limit, so the data are uncorrected. The mean of three blocks of 152
    green volumes was registered to the resized FDA template with antspy (affine start, the better of mean squares and Mattes
    mutual information, then SyN with defaults), and the ROI means were computed through the registration''s linear interpolation
    map, which equals warping each volume and averaging (extractROItimeseries.m). The registration is not repeatable: a second
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "Round 2" attempts/*.yaml | head -3; ls schemas; grep -n "verifications" -A60 schemas/attempt*.json | grep -n '"[a-z_]*": {' | head -40
```

```
attempts/armstrong-2026-01.yaml
attempts/ashworth-2025-01.yaml
attempts/azcorra-2023-01.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
1:386:    "verifications": {
3:388-      "items": {
12:397-        "properties": {
13:398-          "date": {
17:402-          "kind": {
24:409-          "by": {
27:412-          "results": {
29:414-            "items": {
36:421-              "properties": {
37:422-                "claim": {
40:425-                "agrees": {
43:428-                "reason": {
47:432-                "response": {
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 386,470p schemas/attempt.schema.json; grep -n "Round 2" -B3 -A12 attempts/ashworth-2025-01.yaml | head -40
```

```
"verifications": {
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
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
import json
p='reproduce_okuno_2025.ipynb'; nb=json.load(open(p)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.strip('\n').splitlines(keepends=True)
assert src(6).startswith("In both images"); assert src(23).startswith("**Result: FlyEM"); assert src(26).startswith("**Result: reproduced, resting")
assert src(29).startswith("**Result: not reproduced.** With"); assert src(33).startswith("**Result: reproduced.** Under")
assert src(35).startswith("**Result: reproduced under reading (a).** The segregated"); assert src(37).startswith("**Result: reproduced.** The reciprocal")
assert src(42).startswith("**Result: reproduced under reading (a).** The second"); assert src(46).startswith("**Result: not reproduced.** No voxel")
assert src(56).startswith("## Summary"); assert src(44).startswith("The paper's own second level")
setsrc(6, """In both images the slices near z = 6 hold two small dorsal-anterior structures near the midline and
the slices near z = 42 hold the optic lobes, and the dorsoventral axis runs the same way, so no
flip is applied along y or z. Left and right cannot be told apart from the image, and the affine
correlations printed above are not a reliable guide: antspy's default affine stage favours flips
along y and z, which the images rule out. No flip is assumed; the main FC-SC results are shown with
left and right ROIs swapped, and the orientation is checked against the paper's own per-region FC-SC
values (fig3e section) and its deposited GLM map (GLM section). The two checks disagree.

Reduce each fly. Each fly's raw green series is streamed once (about 7 GB per fly) and reduced
to the 114 ROI mean series and the 1000 highest-SD voxels (`flyfc.process_fly`), and the middle 20
slices of the tdTomato series are read for the motion estimate.
""")
setsrc(23, """**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**
With the code's eight flies and Poly-tCompCor, r is 0.606 for FlyEM and 0.566 for FlyWire, below
the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM
is higher in every variant: no nuisance removal 0.636 against 0.597, nine flies 0.601 against
0.562, signed FC the same as the main values, synapse SC 0.553 against 0.524, left and right
swapped 0.518 against 0.508, the second registration (seed 11) 0.592 against 0.554, and with the two
tdTomato in-plane shift series added to the nuisance regressors 0.611 against 0.571. The paper's
own output file for the FlyWire setting gives 0.684 with the same SC, so the gap is in this
attempt's FC, not in the SC. No SPM12 motion or slice-timing correction was applied; the raw series
moves by about one voxel in plane (motion cell), and regressing the shifts out raises both values by
0.005 only, which leaves them below tolerance. It does not stand in for a realignment.
""")
setsrc(26, """**Result: reproduced, resting on the left-right orientation and close to the bound.** FlyEM is
higher in 55 of 63 regions under the main setting (tolerance 52.2 to 63.8), 54 with nine flies and
55 with the second registration (seed 11). With left and right swapped the count is 47, and without
nuisance removal it is 51, both outside the tolerance. The registration is unstable: the seed 11
registration moves native voxels by a median of 2.5 to 44 um per fly (data check), and the earlier,
unseeded runs of this attempt gave 53, 54 and 55. Every registration so far has given 53 to 56,
one to four regions above the bound, so the outcome holds across them with little margin. The
orientation used is supported by the paper's own per-region FlyWire values: they correlate with
this attempt's at r = 0.661 as registered and 0.407 with left and right swapped. The GLM comparison
points the other way, more weakly (GLM section).
""")
setsrc(29, """**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise
with the cholinergic share (r = -0.040, p = 0.76) and its relation to the GABAergic share is not
significant (r = -0.096, p = 0.46); no variant gives a significant ACh or GABA correlation. The
paper's own per-region values from its Zenodo file, run through the same transmitter table, give
the paper's numbers (ACh r = 0.395, p = 0.0014; GABA r = -0.252, p = 0.047), so the difference
comes from the FC computed here, not from the transmitter table.
""")
setsrc(33, """**Result: reproduced.** Under the main setting the unsegregated SC has a higher FC-SC correlation
than the null for neuron SC (0.626 against 0.587, z = +23.5, p = 3e-122) and synapse SC (0.577
against 0.560, z = +7.4, p = 2e-13). The paper's own deposited values give z = +25.7 and +13.7.
The selected total is 2,373,104 and the null totals do not differ from it (p = 0.832). Without
nuisance removal both are below the null (z = -11.0 and -12.8), so the result needs Poly-tCompCor.
With nine flies both are above the null; with left and right swapped the neuron SC is above it
(p = 4e-52) and the synapse SC is not (p = 0.17).
""")
setsrc(35, """**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC
correlation than the null for neuron SC (0.566 against 0.570, z = -4.8, p = 1.3e-6) and synapse SC
(0.519 against 0.534, z = -10.9, p = 2e-27); the paper's deposited values give z = -7.7 and -24.4.
Nine flies and left and right swapped agree; without nuisance removal the neuron SC is not different
from the null (p = 0.83) and the synapse SC is below it (p = 1.4e-8). Reading (b) was not run.
""")
setsrc(37, """**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for
neuron SC (0.629 against 0.590, z = +24.1) and synapse SC (0.574 against 0.564, z = +4.3, p =
1.5e-5, below 0.05/6); the paper's deposited values give z = +24.8 and +11.8. Nine flies agree.
Without nuisance removal the neuron SC is not different from the null (p = 0.94) and the synapse SC
is below it (z = -4.8, p = 1.3e-6); with left and right swapped the synapse SC is below it too
(z = -3.1, p = 0.002). The synapse part therefore rests on the nuisance removal and the orientation.
""")
setsrc(42, """**Result: reproduced under reading (a).** The second level gives one large positive cluster
(404,335 voxels with the graded regressor, 351,796 with the binary one; the paper's deposited map
has one of 416,801, printed below) with maximum t = 17.2 (paper 14.7). LAL, FB, IPS and GNG all lie
in it with peak t above half the maximum (reading a) under both atlases and both regressors.
Reading (b), a mean t in the top third of the neuropils, holds for all four under the hemibrain
atlas with both regressors (LAL(L) rank 19 graded and 21 binary, of 63, where the top third ends
at 21); under JFRC2010 it fails for LAL (ranks 28 to 32 of 75) and holds for the other three. The
per-neuropil mean t correlates with the paper's deposited map at r = 0.41.
""")
setsrc(44, src(44)+"""
The positive clusters of the paper's map are printed, and the orientation is checked twice: voxel
by voxel with this attempt's map mirrored (the brain mask nearly matches its own mirror image, so
the array mirror is close to a mirror about the midline), and per neuropil with left and right ROIs
swapped, the GLM counterpart of the per-region FC check in the fig3e section.
""")
setsrc(46, """**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold
(the lowest t is -0.70, -0.68 with the binary regressor), so there is no negative cluster, and 88
to 100% of WED and AVLP voxels are above the positive threshold. The paper's deposited
second-level map has the README's two negative clusters (406 and 260 voxels, t = -6.14 and -5.65
at the README peaks), where this attempt has t = 4.37 and 4.68; in the paper's map 58% of AVLP(R)
and 88% of WED(R) are also positive-significant. The difference lies in this attempt's
preprocessing and GLM (no motion or slice-timing correction, no Tukey taper), not in the data as
such.

Orientation. The two maps correlate voxel by voxel at r = 0.359 as registered and 0.394 with this
attempt's map mirrored, and per neuropil at 0.41 as registered and 0.463 with left and right ROIs
swapped. Both GLM comparisons favour the flip, weakly; the per-region FC-SC comparison (fig3e
section, 0.661 against 0.407) favours no flip, by more. No flip is kept, as the stronger evidence
and the one computed on the quantity the FC claims use; the conflict is recorded with the
assumption. This outcome does not depend on it: neither orientation gives a negative voxel, and the
activation outcome holds under both, since LAL is tested on both sides and FB and GNG lie on the
midline.
""")
s=src(56)
s=s.replace("| fig3e-flyem-higher-most-regions | reproduced: 53 of 63 (rests on the left-right orientation, close to the bound) |",
            "| fig3e-flyem-higher-most-regions | reproduced: 55 of 63 (rests on the left-right orientation, close to the bound) |")
a=s.index("How the analysis differs from the paper's."); b=s.index("What was found about the dataset.")
s=s[:a]+"""How the analysis differs from the paper's. No SPM12 motion or slice-timing correction was applied
(claims file M1), so every FC and GLM result here rests on uncorrected data. The motion check shows
that the raw series moves: the tdTomato in-plane shift has a median of 0.6 to 3.2 um and a 95th
percentile of 2.8 to 6.1 um per fly, against a voxel of about 2.6 um. Regressing the shifts out
changes the fig3d values by 0.005. The mean green image is registered to the template with ANTs SyN
in Python and the ROI means are computed through the registration's linear map; tCompCor is taken
from native voxels; the GLM has no Tukey-taper pre-whitening and is smoothed on the beta maps. The
FC gives a lower FC-SC correlation than the paper's own output files (0.566 against 0.684 for
FlyWire), and the walking map correlates with the paper's deposited map at r = 0.36 voxel by voxel.
A seeded registration now repeats exactly. A registration with another seed (11) lands elsewhere:
it moves native voxels by a median of 2.5 to 44 um per fly and its ROI series correlate with the
first at a median of 0.18 to 0.98 (data check), yet fig3d and fig3e keep their outcomes under it.
The left-right orientation rests on the per-region FC check, which the two GLM checks contradict
weakly.

"""+s[b:]
s=s.replace("""coverage of the hemibrain ROIs (8 ROIs partly outside the field of view in this run, AL(L)
59% inside; the coverage moves between runs with the registration), which fits the paper's reason for leaving one fly out.""",
"""coverage of the hemibrain ROIs (9 ROIs partly outside the field of view, AL(L) 55% inside; the next
lowest, fly-105, has 2 ROIs at 99%), which fits the paper's reason for leaving one fly out.""")
assert "9 ROIs partly outside" in s
setsrc(56,s)
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
grep -n "rather\|—" reproduce_okuno_2025.ipynb | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; python - <<'E'
import json
p='reproduce_okuno_2025.ipynb'; nb=json.load(open(p)); C=nb['cells']
s=''.join(C[46]['source'])
a="""activation outcome holds under both, since LAL is tested on both sides and FB and GNG lie on the
midline."""
b="""activation test covers LAL and IPS on both sides (IPS on both sides only under JFRC2010, where both
pass reading a), and FB and GNG lie on the midline."""
assert a in s; s=s.replace(a,b); C[46]['source']=s.splitlines(keepends=True)
open(p,'w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
E
cd ..; cd ..; sed -i 's/  runtime_minutes: 23/  runtime_minutes: 36/; s/  runtime_minutes: 14/  runtime_minutes: 20/' entries/okuno-2025/entry.yaml; grep runtime entries/okuno-2025/entry.yaml; date -u
```

```
runtime_minutes: 36
  runtime_minutes: 20
Mon Nov 16 03:01:32 UTC 2026
```

**Agent**

Text is updated for this run's numbers. Re-running the entry now to refresh the executed copies and confirm the seeded registration gives the same numbers.

**Agent calls Bash**

```bash
cd  cp executed/okuno-2025/reproduce_okuno_2025.ipynb $TMPDIR/run1.ipynb; python tools/entry.py all entries/okuno-2025 2>&1 | tail -5; date -u
```

```
Installed kernelspec registry-okuno-2025 in executed/okuno-2025/.venv/share/jupyter/kernels/registry-okuno-2025
0 error(s)
pass  reproduce_okuno_2025.ipynb  (2051 s)
pass  connectome_okuno_2025.ipynb  (830 s)
Mon Nov 16 03:49:53 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json, os, re
def outs(p):
    nb=json.load(open(p)); r=[]
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        t=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        t=re.sub(r"read \d+ MB in \d+ s|betas done \d+ s|elapsed \(min\) [\d.]+|runtime \(min\) [\d.]+|peak memory \(GB\) [\d.]+","",t)
        r.append(t)
    return r
a=outs(os.environ['TMPDIR']+'/run1.ipynb'); b=outs('executed/okuno-2025/reproduce_okuno_2025.ipynb')
import difflib
for i,(x,y) in enumerate(zip(a,b)):
    if x!=y:
        print("cell",i); print('\n'.join(list(difflib.unified_diff(x.splitlines(),y.splitlines(),lineterm='',n=0))[:20]))
print(len(a),len(b))
E
```

```
29 29
```

**Agent**

Outputs of the two runs are identical, so the notebook is now deterministic. Next, the attempt record.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import re, textwrap
p='attempts/okuno-2025-01.yaml'; s=open(p).read()
def block(key, text, ind=2):
    pad=' '*ind
    body=textwrap.fill(' '.join(text.split()), width=118, initial_indent=pad+'  ', subsequent_indent=pad+'  ', break_long_words=False, break_on_hyphens=False)
    return f"{pad}{key}: >-\n{body}\n"
def set_notes(claim, text):
    global s
    m=re.search(r"(?ms)^- claim: "+re.escape(claim)+r"\n.*?(?=^- claim: |^findings:)", s)
    seg=m.group(0)
    n=re.search(r"(?ms)^  notes: .*?(?=^  [a-z_]+:|\Z)", seg)
    seg2=seg[:n.start()]+block('notes',text)+seg[n.end():]
    s=s[:m.start()]+seg2+s[m.end():]
def set_measured(claim, new):
    global s
    m=re.search(r"(?ms)^- claim: "+re.escape(claim)+r"\n.*?(?=^- claim: |^findings:)", s)
    seg=m.group(0)
    n=re.search(r"(?ms)^  measured:.*?(?=^  [a-z_]+:)", seg)
    seg2=seg[:n.start()]+new+seg[n.end():]
    s=s[:m.start()]+seg2+s[m.end():]

old_reg=re.search(r"(?ms)^  - 'Registration \(claims file O2\).*?the results under it\.'\n", s).group(0)
assert s.count(old_reg)==8, s.count(old_reg)
new_reg=block('', """Registration (claims file O2). The paper gives no SPM12 or ANTs settings. No SPM12 motion or slice-timing
correction was applied (claims file M1 requires it), so the data are uncorrected. The raw series moves: a rigid in-plane
shift estimated per volume from the tdTomato channel has a median of 0.6 to 3.2 um and a 95th percentile of 2.8 to 6.1 um
per fly, against an in-plane voxel of about 2.6 um (motion cell). Regressing the two shift series out moves the fig3d
values by 0.005; that check does not stand in for a realignment and was not applied to the other claims. The mean of
three blocks of 152 green volumes was registered to the resized FDA template with antspy (affine start, the better of
mean squares and Mattes mutual information, then SyN with defaults), and the ROI means were computed through the
registration's linear interpolation map, which equals warping each volume and averaging (extractROItimeseries.m). The
registration is seeded through ants.config (antspy 0.6.3 ignores the random_seed argument that the earlier runs passed,
so they were unseeded) with ITK on one thread, and it now repeats exactly; two runs of the notebook gave identical
output. It is unstable across seeds: a registration with seed 11 moved native voxels by a median of 2.5 to 44 um per fly,
and its ROI series correlate with the first at a median of 0.18 to 0.98 (data check). The notes give the results under
it.""", ind=2).replace("  : >-\n","  - >-\n",1)
s=s.replace(old_reg,new_reg)
old_or="""  - Left-right orientation. The files do not state it, and a symmetric brain cannot fix it. No flip is assumed; with left
    and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.514 against 0.603), which supports the choice.
    The swapped result is shown for every claim.
"""
assert s.count(old_or)==8, s.count(old_or)
new_or=block('', """Left-right orientation. The files do not state it, and a symmetric brain cannot fix it. No flip is assumed.
With left and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.518 against 0.606), and the paper's
own per-region FlyWire FC-SC values correlate with this attempt's at r = 0.661 as registered and 0.407 swapped, which
supports the choice. The GLM points the other way, more weakly: this attempt's walking t map correlates with the paper's
deposited map at r = 0.359 as registered and 0.394 mirrored, and per neuropil at 0.41 as registered and 0.463 with left
and right ROIs swapped. No flip is kept, as the stronger evidence and the one computed on the quantity the FC claims use.
The swapped result is shown for every claim.""", ind=2).replace("  : >-\n","  - >-\n",1)
s=s.replace(old_or,new_or)
old_vx="""  - Native voxel size from the NWB grid_spacing (2.55 to 2.61 by 2.61 to 2.68 by 5 um); the paper's NWB-to-NIfTI script is
    not published, so the voxel size its NIfTI headers carried is not known.
"""
assert old_vx in s
s=s.replace(old_vx, block('', """Native voxel size from each fly's NWB grid_spacing (2.55 to 2.61 by 2.61 to 2.68 by 5 um); the earlier runs
used fly-087's spacing for every fly. The paper's NWB-to-NIfTI script is not published, so the voxel size its NIfTI
headers carried is not known.""").replace("  : >-\n","  - >-\n",1))

set_measured('fig3d-flyem-vs-flywire', "  measured:\n  - 0.6058\n  - 0.5664\n")
set_notes('fig3d-flyem-vs-flywire', """63 primary ROIs, no smoothing, Poly-tCompCor, code's eight flies, SC neuron layer 2. FlyEM r = 0.606 and
FlyWire r = 0.566, so FlyEM is higher but both are below the tolerances (0.657 to 0.803 and 0.612 to 0.748). FlyEM is
higher in every variant: no nuisance removal 0.636 against 0.597, nine flies 0.601 against 0.562, signed FC (O3) the
same as the main values, a second registration with seed 11 0.592 against 0.554, left and right swapped 0.518 against
0.508, and the two tdTomato in-plane shift series added to the nuisance regressors 0.611 against 0.571. Synapse SC gives
0.553 against 0.524. The paper's own output file for the FlyWire setting (Zenodo,
results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat) gives R(7) = 0.684 with the same SC, so the shortfall is in the FC
computed here, most likely its missing motion and slice-timing correction (claims file M1; the raw series moves by about
one voxel in plane) and the registration, not in the SC.""")
set_measured('fig3e-flyem-higher-most-regions', "  measured: 55\n")
set_notes('fig3e-flyem-higher-most-regions', """FlyEM has the higher per-region FC-SC correlation in 55 of 63 regions (tolerance 52.2 to 63.8), 54 with nine
flies and 55 with a second registration (seed 11). The outcome is not robust. The count is one to four regions above the
bound in every registration made so far (53, 54 and 55 in the earlier unseeded runs, 55 and 56 with their second
registrations), while the registration itself is unstable: the seed 11 registration moves native voxels by a median of
2.5 to 44 um per fly. The count also depends on the orientation and the nuisance removal: with left and right swapped it
is 47 and without nuisance removal 51, both outside the tolerance. The orientation used is supported by the paper's own
per-region FlyWire values (Zenodo auc file), which correlate with this attempt's at r = 0.661 as registered and r = 0.407
with left and right swapped; the GLM comparison points weakly the other way (see the orientation deviation).""")
set_measured('fig3g-transmitter-correlation', "  measured:\n  - -0.04\n  - -0.096\n")
set_notes('fig3g-transmitter-correlation', """With this attempt's per-region FlyWire FC-SC correlation, the acetylcholine output share gives r = -0.040 (p =
0.76) and GABA r = -0.096 (p = 0.46). No variant (no nuisance removal, nine flies, left and right swapped) gives a
significant ACh or GABA correlation. The paper's own per-region values from its Zenodo file, run through the same
transmitter table, give ACh r = 0.395 (p = 0.0014) and GABA r = -0.252 (p = 0.047), the paper's numbers, so the table is
right and the difference comes from the FC computed here (its per-region values correlate with the paper's at r =
0.661), which lacks the motion and slice-timing correction of claims file M1.""")
set_notes('fig4e-unsegregated-higher', """Unsegregated SC (code target sp10db3000mi1_only1) against the 99 rd185-20 null SC matrices, Poly-tCompCor, eight
flies. Neuron SC r = 0.626 against null 0.587 +- 0.0016 (z = +23.5, p = 3e-122); synapse SC r = 0.577 against 0.560 +-
0.0023 (z = +7.4, p = 2e-13); both above the null at p < 0.05/6. The paper's own deposited R values for the same SC
matrices give z = +25.7 and +13.7. The selected synapse total is 2,373,104 and the null totals do not differ from it (p =
0.832). Nine flies agree; with left and right swapped the synapse SC is not different from the null (p = 0.17). Without
nuisance removal both are below the null (z = -11.0 and -12.8), so the result needs Poly-tCompCor, here applied to data
without motion correction.""")
set_notes('fig4f-segregated-lower', """Reading (a), the code's target sp90db3000mi1, against the 99 rd1560-80 null SC matrices. Neuron SC r = 0.566
against null 0.570 +- 0.0008 (z = -4.8, p = 1.3e-6); synapse SC r = 0.519 against 0.534 +- 0.0014 (z = -10.9, p =
2e-27); both below the null at p < 0.05/6. The paper's deposited R values give z = -7.7 and -24.4. Nine flies and
left-right swapped agree. Without nuisance removal the neuron SC is not different from the null (p = 0.83) and the
synapse SC is below it (p = 1.4e-8). The null totals match the selected total (p = 0.64). Reading (b), both sides at 0.9
or more, needs an SC rebuilt from the synapse table and was not run.""")
set_notes('fig4i-reciprocal-higher', """Reciprocal SC (code target rc20_only1) against the 99 rd140-15 null SC matrices. Neuron SC r = 0.629 against
null 0.590 +- 0.0016 (z = +24.1, p = 8e-129); synapse SC r = 0.574 against 0.564 +- 0.0021 (z = +4.3, p = 1.5e-5, below
0.05/6). The paper's deposited R values give z = +24.8 and +11.8. Nine flies agree. Without nuisance removal the neuron
SC is not different from the null (p = 0.94) and the synapse SC is below it (z = -4.8, p = 1.3e-6); with left and right
swapped the synapse SC is below it too (z = -3.1, p = 0.002). The synapse part therefore rests on the nuisance removal
and the orientation. The null totals match the selected total (p = 0.852).""")
set_notes('fig5b-walking-activation', """Second level over the nine flies, graded regressor (O1, the code's), height p < 0.001 (t > 3.242, df 56). One
positive cluster of 404,335 voxels (351,796 with the binary regressor; the paper's deposited map, recomputed here from
s80poltcomparfly-all-Tukey8full.mat, has one of 416,801), maximum t = 17.2 (paper 14.7). LAL, FB, IPS and GNG all lie
in it with peak t at least half the maximum (reading a) under the hemibrain and JFRC2010 atlases and with both
regressors. Reading (b), a mean t in the top third of the neuropils, holds for all four under the hemibrain atlas with
both regressors (LAL(L) rank 19 graded and 21 binary of 63, where the top third ends at 21); under JFRC2010 it fails for
LAL (ranks 28 to 32 of 75) and holds for the other three. The per-neuropil mean t correlates with the paper's deposited
map at r = 0.41.""")
set_notes('fig5b-walking-suppression', """No voxel in the brain mask falls below -3.242 (the lowest t is -0.70, and -0.68 with the binary regressor), so
there is no negative cluster. WED and AVLP are mostly positive: 88 to 100% of their voxels are above the positive
threshold under both atlases and both regressors. The paper's deposited second-level map has the README's two negative
clusters (406 and 260 voxels, t = -6.14 and -5.65 at (82,78,12) and (174,80,15)); at those voxels this attempt has t =
4.37 and 4.68. In the paper's map too, 58% of AVLP(R) and 88% of WED(R) are positive-significant. The two maps correlate
voxel by voxel at r = 0.359 (0.394 with this attempt's map mirrored), so the difference lies in this attempt's processing
(no motion or slice-timing correction, no Tukey taper), which the deposited map shows the paper's processing does not
share. Neither orientation gives a negative voxel.""")

# findings
a="""    This attempt registered the mean green image with antspy SyN without motion or slice-timing correction and obtains a FlyWire
    FC-SC correlation of 0.581 on the 63 primary ROIs"""
assert a in s; s=s.replace(a,a.replace("0.581","0.566"))
a="""left and right cannot, and one claim's outcome (fig3e) changes with it."""
assert a in s; s=s.replace(a,"""left and right cannot. With left and right swapped, fig3e and the synapse parts of fig4e and fig4i would no longer be
    reproduced; the evidence on which way is right conflicts between the FC and the GLM comparisons with the paper's deposits.""")
a="""one the code leaves out, has the lowest coverage of any fly after registration (in the run of 2026-11-16, 8 hemibrain
    ROIs partly outside the field of view, AL(L) 59% inside; the coverage moves between runs with the registration), consistent
    with the paper's stated reason."""
assert a in s; s=s.replace(a,"""one the code leaves out, has the lowest coverage of any fly after registration (9 hemibrain ROIs partly outside the field
    of view, AL(L) 55% inside; the next lowest, fly-105, has 2 ROIs at 99%), consistent with the paper's stated reason.""")
a="""    The missing motion and slice-timing correction (problem 1) is now stated in the deviations, the notebook summary
      and here. A streamed realignment and slice-timing correction were written and tested on one fly (sub-voxel in-plane
      motion), but the full notebook with them ran past the 60-minute cell limit twice, so the run is on uncorrected data."""
assert a in s; s=s.replace(a,"""    The missing motion and slice-timing correction (problem 1) is now stated in the deviations, the notebook summary
      and here. A streamed realignment and slice-timing correction were written and tried on one fly (that test left no output
      in the notebooks; round 2 adds a motion check), but the full notebook with them ran past the 60-minute cell limit twice,
      so the run is on uncorrected data.""")
open(p,'w').write(s)
PYEOF
python $TMPDIR/rec.py && python -c "import yaml;d=yaml.safe_load(open('attempts/okuno-2025-01.yaml'));print(len(d['outcomes']))" && git diff --stat attempts/
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/rec.py", line 42, in <module>
    assert s.count(old_or)==8, s.count(old_or)
           ^^^^^^^^^^^^^^^^^^
AssertionError: 6
```

**Agent calls Bash**

```bash
cd  sed -i 's/assert s.count(old_or)==8, s.count(old_or)/assert s.count(old_or)==6, s.count(old_or)/' $TMPDIR/rec.py; python $TMPDIR/rec.py && python -c "import yaml;d=yaml.safe_load(open('attempts/okuno-2025-01.yaml'));print(len(d['outcomes']))" && git diff --stat attempts/
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/rec.py", line 136, in <module>
    assert a in s; s=s.replace(a,"""    The missing motion and slice-timing correction (problem 1) is now stated in the deviations, the notebook summary
           ^^^^^^
AssertionError
```

**Agent calls Bash**

```bash
cd  grep -n "The missing motion" -A3 attempts/okuno-2025-01.yaml | cat -A | cut -c1-140 | head
```

```
604:    response: The missing motion and slice-timing correction (problem 1) is now stated in the deviations, the notebook summary$
605-      and here. A streamed realignment and slice-timing correction were written and tested on one fly (sub-voxel in-plane$
606-      motion), but the full notebook with them ran past the 60-minute cell limit twice, so the run is on uncorrected data.$
607-      Added a second registration with another seed (FlyEM 0.611, FlyWire 0.570). Re-run values 0.616 and 0.581; outcome unchanged.$
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import os
p=os.environ['TMPDIR']+'/rec.py'; s=open(p).read()
i=s.index('a="""    The missing motion')
s=s[:i]+'''a="""written and tested on one fly (sub-voxel in-plane
      motion), but"""
assert a in s; s=s.replace(a,"""written and tried on one fly (that test left no output in the
      notebooks; round 2 adds a motion check), but""")
open(p,'w').write(s)
'''
open(p,'w').write(s)
E
python $TMPDIR/rec.py && python -c "import yaml;d=yaml.safe_load(open('attempts/okuno-2025-01.yaml'));print(len(d['outcomes']))" && git diff --stat attempts/
```

```
30
 attempts/okuno-2025-01.yaml | 387 +++++++++++++++++++++++++++-----------------
 1 file changed, 243 insertions(+), 144 deletions(-)
```

**Agent calls Bash**

```bash
cd  sed -n 118,200p attempts/okuno-2025-01.yaml
```

```
- claim: fig3d-flyem-vs-flywire
  outcome: partially_reproduced
  notebook: reproduce_okuno_2025.ipynb
  output: claim:fig3d-flyem-vs-flywire
  measured:
  - 0.6058
  - 0.5664
  assumed: true
  notes: >-
    63 primary ROIs, no smoothing, Poly-tCompCor, code's eight flies, SC neuron layer 2. FlyEM r = 0.606 and FlyWire r
    = 0.566, so FlyEM is higher but both are below the tolerances (0.657 to 0.803 and 0.612 to 0.748). FlyEM is higher
    in every variant: no nuisance removal 0.636 against 0.597, nine flies 0.601 against 0.562, signed FC (O3) the same
    as the main values, a second registration with seed 11 0.592 against 0.554, left and right swapped 0.518 against
    0.508, and the two tdTomato in-plane shift series added to the nuisance regressors 0.611 against 0.571. Synapse SC
    gives 0.553 against 0.524. The paper's own output file for the FlyWire setting (Zenodo,
    results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat) gives R(7) = 0.684 with the same SC, so the shortfall is in the
    FC computed here, most likely its missing motion and slice-timing correction (claims file M1; the raw series moves
    by about one voxel in plane) and the registration, not in the SC.
  deviations:
  - >-
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat questions/okuno-2025.yaml | head -40; grep -n "fig4b" -A14 attempts/okuno-2025-01.yaml | sed -n 1,16p; grep -n "figs3-2cd" -A6 attempts/okuno-2025-01.yaml | head -8
```

```
dandiset: "000727"
paper: doi:10.7554/elife.107990.1
questions:
- claim: fig4b-ppssi-distribution
  asked: 2026-11-16
  question: >-
    The expected value is "neurons with a PPSSI = 139,255" with tolerance 0. Is 139,255 the number of
    neurons the index was applied to, of which some get no value? The paper's deposited per-neuron
    table lists 139,255 neurons, of which 138,144 carry a PPSSI, and the code's README prints
    6154/138144 for the fully segregated ones. Should the expected quantity be the neurons the index
    was applied to?
  passage: >-
    "Fig. 4b shows the result of applying PPSSI to 139,255 whole-brain neurons of FlyWire. The result
    showed a histogram resembling a normal distribution." (Results, Unsegregated synapses contribute
    considerably to functional connectivity, paragraph 1)
  why: >-
    Read as neurons the index was applied to, the deposited table holds exactly 139,255 and, with the
    mean of 0.471 inside 0.4 to 0.6, the claim is reproduced. Read as neurons with a value, the count
    is 138,144, outside the tolerance of 0, and the claim is partially reproduced.
315:- claim: fig4b-ppssi-distribution
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "id: fig4b-ppssi-distribution" -A30 claims/okuno-2025.yaml | grep -n "criterion\|partial\|reproduced\|tolerance" ; grep -n "partial" docs/protocol.md | head
```

```
13:506-    tolerance: 0
14:507-  criterion: PPSSI as M7. Reproduced when the neuron count matches and the mean PPSSI is within
26:519-  criterion: Ranking by (1 - PPSSI) log10(W) (M7). Reproduced when ranks 1 to 4 in FlyWire are all
262:     their notes say how the partial link bears on them. A label that
458:  - `partially_reproduced`: the effect is present but weaker, or holds only in
497:If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
```

**Agent calls Bash**

```bash
cd  sed -n 500,512p claims/okuno-2025.yaml; sed -n 450,470p docs/protocol.md
```

```
result showed a histogram resembling a normal distribution.
  data: elsewhere
  where: FlyWire sc140 synapses (Zenodo 10676866)
  expected:
  - quantity: neurons with a PPSSI
    value: 139255
    tolerance: 0
  criterion: PPSSI as M7. Reproduced when the neuron count matches and the mean PPSSI is within
    0.4 to 0.6 (the Methods' "its mean is close to 0.5", read with a 0.1 margin, a choice made
    here).
- id: fig4a-unsegregated-ranking
  statement: The unsegregated ranking puts APL and CT1 cells in the top four places in FlyWire,
    and APL first in FlyEM.
  `why` (not in any open archive, not yet converted, unreadable). A missing
  dataset does not stop the attempt: test what the others allow, and block
  each claim that needs a missing one with `dataset_missing`. The site flags
  the attempt, so that a later one can add the dataset.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/v2.py <<'PYEOF'
import textwrap, yaml
p='attempts/okuno-2025-01.yaml'; s=open(p).read()
def f(key, text, ind):
    pad=' '*ind
    body=textwrap.fill(' '.join(text.split()), width=118, initial_indent=pad+'  ', subsequent_indent=pad+'  ', break_long_words=False, break_on_hyphens=False)
    return f"{pad}{key}: >-\n{body}\n"
STALE = "The Result cells, summary and record were rewritten from this run's output (see the round's summary)."
REG = ("The registration is now seeded through ants.config (antspy 0.6.3 ignored the random_seed argument, so the earlier "
       "runs were unseeded) with ITK on one thread; two full runs gave identical output.")
blocked = ["fig1-poltcomp-optimal","fig2b-distkm-smoothing-optimum","figs2-1b-sckm-smoothing","fig2c-smoothing-plus-poltcomp",
           "figs2-1d-highpass-degrades","fig2d-log-decline","fig2d-fly-values","fig2d-ten-thousand-rois","discussion-twenty-rois",
           "fig3d-confidence-threshold"]
R = []
for c in blocked:
    R.append((c,"blocked","The 14 blocked outcomes, agree.","No change."))
R += [
("fig3d-flyem-vs-flywire","partially_reproduced",
 "Agree. Cell 19 prints FlyEM 0.5925 and FlyWire 0.5557: FlyEM is higher, and both values are below tolerance. The record's measured values (0.6161, 0.5808) are not this run's. The fig3d response's \"tested on one fly (sub-voxel in-plane motion)\" has no output in either notebook. Motion and slice-timing correction (M1) are still missing; whether the raw series needs the correction is still not shown in any output.",
 STALE+" "+REG+" New values FlyEM 0.6058 and FlyWire 0.5664, measured updated; outcome unchanged. Added a motion check: a rigid in-plane shift per volume from the tdTomato channel (median 0.6 to 3.2 um, 95th percentile 2.8 to 6.1 um per fly, against a 2.6 um voxel), so the motion is not sub-voxel; the round-1 response's unsupported parenthesis is corrected. With the shift series added to the nuisance regressors fig3d gives 0.611 and 0.571, still below tolerance. A full SPM12-style realignment and slice-timing correction were still not applied. Each fly's own grid_spacing is now used as its voxel size."),
("fig3e-flyem-higher-most-regions","reproduced",
 "Agree, but it is fragile. Cell 23 prints 55. Across runs the count has been 54 (round 1), 53 (record) and 55 (now), against a lower bound of 52.2. It falls out of tolerance with left and right swapped (44) and with no nuisance removal (48). The record's measured: 53 is not this run's value. The registration is unstable: the second seed moves voxels by up to about 25 um (median), and fig3e sits 1 to 3 regions above its bound across runs, so its reproduced is not robust; its note should say so in terms of this instability, not \"second or third decimal\". The orientation evidence conflicts: per-region r 0.637 as registered against 0.404 swapped, voxel-wise GLM 0.373 against 0.40 flipped; fig3e depends on this choice.",
 STALE+" "+REG+" The count is 55 (54 with nine flies, 55 with the seed 11 registration, 47 swapped, 51 without nuisance removal); measured updated. The note now says the outcome is not robust, in terms of the instability across registrations (53 to 56 so far, seed 11 moving voxels by a median of 2.5 to 44 um), and cell 2's \"second or third decimal\" is gone. The GLM orientation checks are now printed (voxel-wise 0.359 against 0.394 mirrored, per neuropil 0.41 against 0.463 swapped) and recorded in the orientation deviation beside the FC check (0.661 against 0.407); no flip is kept as the stronger evidence. Outcome unchanged."),
("fig3g-transmitter-correlation","not_reproduced",
 "Agree. Cell 26 prints ACh r = -0.072 (p = 0.573) and GABA r = -0.067 (p = 0.601). The record's measured values (0.033, -0.17) are not this run's.",
 STALE+" New values ACh r = -0.040 (p = 0.76) and GABA r = -0.096 (p = 0.46); measured updated. Outcome unchanged."),
("fig3a-postsynapse-counts","partially_reproduced","Agree. Cells 46 to 53 print values consistent with the notes.","No change."),
("fig3c-regional-detection","reproduced","Agree. Cells 46 to 53 print values consistent with the notes.","No change."),
("figs3-1a-regional-count-similarity","reproduced","Agree. Cells 46 to 53 print values consistent with the notes.","No change."),
("fig3f-output-transmitters","reproduced","Agree. Cells 46 to 53 print values consistent with the notes.","No change."),
("figs3-2cd-apl-similarity","blocked","The 14 blocked outcomes, agree. figs3-2cd is now not_runnable with a stated reason.","No change."),
("fig4b-ppssi-distribution","partially_reproduced",
 "Agree with reservations. The criterion defines no partial outcome for this claim, and the claims-file misreading I raised in round 1 is still open. The claims file's quantity, neurons with a PPSSI = 139,255 with tolerance 0, may misread the paper's count of neurons the index was applied to.",
 "Kept. The protocol's partially_reproduced covers a result that holds only in part, as here: the mean holds and the count does not. The question for a reader stays open in questions/okuno-2025.yaml; the claim is unchanged."),
("fig4a-unsegregated-ranking","blocked",
 "Agree. The FlyWire halves hold (connectome notebook cells 10 and 13). blocked_by: other is honest: the FlyEM synapses are public but the DBSCAN was not run.","No change."),
("fig4c-segregated-ranking","blocked",
 "Agree. The FlyWire halves hold (connectome notebook cells 10 and 13). blocked_by: other is honest: the FlyEM synapses are public but the DBSCAN was not run.","No change."),
("figs4-1ij-segregation-index-biased","not_reproduced",
 "Agree. The FlyWire mean is 0.363, which is closer to 0.5 than to 0. The claim fails whatever the 0.25 bound and whatever the untested FlyEM half gives.","No change."),
("fig4e-unsegregated-higher","reproduced",
 "Agree. In cell 30 the MAIN line is True/True. The Result cell's values (0.636 against 0.598, z = +23.9; 0.586 against 0.570, z = +6.6; no nuisance z = -9.0 and -10.6; swapped p = 5e-45 and 0.88) are not the printed ones. fig4e's synapse result depends on the orientation choice.",
 STALE+" New values: neuron z = +23.5, synapse z = +7.4, no nuisance z = -11.0 and -12.8, swapped synapse p = 0.17. The orientation conflict is recorded in the deviation and the metadata_insufficient finding now names fig4e. Outcome unchanged."),
("fig4f-segregated-lower","reproduced",
 "Agree (reading a). In cell 32 the MAIN line is True/True. The Result cell's values (0.579 against 0.584, z = -5.6; 0.529 against 0.545, z = -11.7; p = 0.93) are not the printed ones.",
 STALE+" New values: neuron z = -4.8, synapse z = -10.9, no nuisance neuron p = 0.83. Outcome unchanged."),
("fig4i-reciprocal-higher","reproduced",
 "Agree. In cell 34 the MAIN line is True/True; the synapse p = 1.4e-4 is below 8.3e-3. \"Without nuisance removal the synapse SC is below the null (p = 0.0002)\": printed p = 0.0232, which is not significant at 0.05/6; the fig4i no-nuisance statement reverses.",
 STALE+" In the seeded run the synapse p is 1.5e-5; without nuisance removal the synapse SC is below the null (z = -4.8, p = 1.3e-6) and with left and right swapped too (z = -3.1, p = 0.002), as the notes now say from this run's output. Outcome unchanged."),
("figs4-1-flyem-permutation","blocked","The 14 blocked outcomes, agree.","No change."),
("fig4h-reciprocal-distances","reproduced",
 "Agree. The mode is the 1 to 2 um bin, and ACh plus GABA make up 0.756. The criterion says \"pairs\", but each reciprocal synapse is counted from both of its neurons. The presynaptic-only split (0.761) gives the same outcome.","No change."),
("fig5b-walking-activation","reproduced",
 "Agree under reading (a). Cell 38 prints True for all four neuropils, both atlases and both regressors. The Result cell's 396,982 voxels, maximum t = 20.9, r = 0.447 and \"Reading (b) fails for LAL (rank 23 of 63 at best)\" are not the printed values: cell 38 prints reading (b) True for LAL with the graded regressor; it fails only with the binary regressor, and for GNG with the graded regressor under JFRC2010. No cell prints the deposited positive cluster.",
 STALE+" In the seeded run: one cluster of 404,335 voxels, maximum t = 17.2, per-neuropil r = 0.41; reading (b) holds for all four under the hemibrain atlas with both regressors and fails only for LAL under JFRC2010. The deposited map's positive cluster (416,801 voxels) is now printed. Outcome unchanged."),
("fig5b-walking-suppression","not_reproduced",
 "Agree. Cell 41: no voxel is below -3.24 (minimum -1.45). The Result cell's lowest t -1.74, 87 to 100%, t = 3.32 and 4.62 and r = 0.363 (0.390) are not the printed values.",
 STALE+" In the seeded run the lowest t is -0.70, 88 to 100% of WED and AVLP voxels are positive-significant, t = 4.37 and 4.68 at the README peaks, voxel-wise r = 0.359 (0.394 mirrored). Outcome unchanged."),
("fig5-wagn","reproduced",
 "Agree (reading b). The values are PPSSI 0.1332 and 22 ascending neurons at sc50 with at least 5 synapses each. At sc140 they are 212 synapses from the ANs, 65 to WPNb and a closest distance of 852.3 nm.","No change."),
]
order=[l.split("- claim: ")[1].strip() for l in s.split("\noutcomes:\n")[1].split("\nfindings:\n")[0].splitlines() if l.startswith("- claim: ")]
d={r[0]:r for r in R}
assert set(d)==set(order), set(order)^set(d)
out = "- date: '2026-11-16'\n  kind: agent\n  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)\n"
out += f("reviewed", """Round 2. The full executed notebooks of the author-revise-1 run (reproduce_okuno_2025.ipynb and
connectome_okuno_2025.ipynb), the helper module, the claims file and this record, with the paper. Report in
transcripts/okuno-2025/verifier-2-report.md. The verifier agrees with all 30 outcomes. Its main finding was that the notebook
had been re-executed but its Result cells, summary and this record still quoted an earlier run, because the registration
changed between runs. In reply the registration was made repeatable (antspy 0.6.3 ignored the random_seed argument; the seed
is now set through ants.config with ITK on one thread), each fly's own voxel size is used, a motion check from the tdTomato
channel and the GLM orientation checks were added, the entry was re-run twice with identical output, and every number in the
notebook text and this record was rewritten from that output. No outcome changed and none is proposed to change.""", 2)
out += "  results:\n"
for c in order:
    _, oc, reason, resp = d[c]
    out += f"  - claim: {c}\n    agrees: true\n    outcome: {oc}\n" + f("reason", reason, 4) + f("response", resp, 4)
s = s.rstrip("\n") + "\n" + out
open(p,'w').write(s)
y=yaml.safe_load(open(p)); print(len(y['verifications']), len(y['verifications'][-1]['results']))
for o in y['outcomes']:
    v=[r for r in y['verifications'][-1]['results'] if r['claim']==o['claim']][0]
    assert v['outcome']==o['outcome'], (o['claim'], v['outcome'], o['outcome'])
PYEOF
python $TMPDIR/v2.py
```

```
2 30
```

**Agent calls Bash**

```bash
cd  grep -n "rather\|—" attempts/okuno-2025-01.yaml entries/okuno-2025/* questions/okuno-2025.yaml | grep -v "lock.txt" | head; python tools/entry.py check entries/okuno-2025 2>&1 | tail -15
```

```
grep: entries/okuno-2025/__pycache__: Is a directory
0 error(s)
```

**Agent calls Bash**

```bash
cd  rm -rf entries/okuno-2025/__pycache__; for v in "0\.616" "0\.581" "0\.704" "0\.447" "396,982" "3 to 35" "59%" "20\.9" "1\.74" "0\.363 (0" "second or third"; do echo "== $v"; grep -n "$v" attempts/okuno-2025-01.yaml | cut -c1-80 | head -5; python -c "
import json,re,sys;nb=json.load(open('entries/okuno-2025/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  if c['cell_type']=='markdown' and re.search(sys.argv[1],''.join(c['source'])): print('nb cell',i)" "$v"; done
```

```
== 0\.616
706:      Added a second registration with another seed (FlyEM 0.611, FlyWire 0.
914:      record's measured values (0.6161, 0.5808) are not this run's. The fig3
== 0\.581
706:      Added a second registration with another seed (FlyEM 0.611, FlyWire 0.
== 0\.704
712:    response: 'Problem 2: the orientation is now checked against the paper''
== 0\.447
809:      r = 0.447). In this re-run reading (b) fails for LAL; reading (a) hold
1080:      Result cell's 396,982 voxels, maximum t = 20.9, r = 0.447 and "Readin
== 396,982
1080:      Result cell's 396,982 voxels, maximum t = 20.9, r = 0.447 and "Readin
== 3 to 35
== 59%
== 20\.9
1080:      Result cell's 396,982 voxels, maximum t = 20.9, r = 0.447 and "Readin
== 1\.74
1093:      Agree. Cell 41: no voxel is below -3.24 (minimum -1.45). The Result c
== 0\.363 (0
1094:      and 4.62 and r = 0.363 (0.390) are not the printed values.
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py hash entries/okuno-2025; python -c "import json;print(json.load(open('executed/okuno-2025/.clean-run.json'))['hash'])"; git status --short entries attempts questions; date -u
```

```
e927029ef3b289fe5b354edc4dab6206a2b07c79733fd37c57639b0740de17a2
e927029ef3b289fe5b354edc4dab6206a2b07c79733fd37c57639b0740de17a2
 M attempts/okuno-2025-01.yaml
 M entries/okuno-2025/entry.yaml
 M entries/okuno-2025/flyfc.py
 M entries/okuno-2025/reproduce_okuno_2025.ipynb
Mon Nov 16 03:52:32 UTC 2026
```

**Agent**

All 30 outcomes are unchanged and I proposed no changes. The entry was re-run twice with `python tools/entry.py all entries/okuno-2025`. Both runs printed identical output, `entry.py check` reports 0 errors, and the executed copies match the current entry hash.

**Why the text described another run.** The installed antspy (0.6.3) silently ignores the `random_seed` argument we were passing to `ants.registration`. So the registration had never been seeded, and every number resting on it changed from run to run. It is now seeded through `ants.config` with ITK on one thread, which makes it repeatable. A notebook cell registers one image twice and shows zero difference.

**What I added or corrected:**
- **Voxel size:** each fly now uses its own NWB grid_spacing. Before, fly-087's spacing was used for all nine.
- **Motion check (verifier point 3):** I estimated a rigid in-plane shift per volume from the tdTomato channel. The motion is not sub-voxel: per fly, the median is 0.6 to 3.2 µm and the 95th percentile 2.8 to 6.1 µm, against a 2.6 µm voxel. Regressing the shifts out moves fig3d by only 0.005, so it stays below tolerance. I corrected the round-1 response that called the motion sub-voxel.
- **Orientation (point 4):** the notebook now prints a per-neuropil GLM check alongside the voxel-wise one. Both point weakly towards flipping left and right:
  - voxel by voxel, 0.359 as registered against 0.394 mirrored;
  - per neuropil, 0.41 against 0.463.
  The per-region FC check points the other way, and by more (0.661 against 0.407). I kept "no flip" and recorded the conflict in the orientation deviation. The dataset finding now names fig3e, fig4e and fig4i as the outcomes a flip would change.
- **The paper's positive GLM cluster** (416,801 voxels) is now printed.
- **Registration instability (point 2):** fig3e's note now says the outcome is not robust. Every registration so far gives 53 to 56 regions, one to four above the bound of 52.2, and a registration with another seed moves voxels by a median of 2.5 to 44 µm per fly. The "second or third decimal" wording is gone.
- **All Result cells, the Summary, and the record's notes, `measured` fields, deviations and findings** were rewritten from the new output. With the new numbers, two statements the verifier said reversed now read:
  - fig4i: without nuisance removal the synapse result is again below the null (p = 1.3e-6).
  - fig5b activation: reading (b) holds for all four regions under the hemibrain atlas and fails only for LAL under JFRC2010.
- **Runtimes** in `entry.yaml` are updated to 36 and 20 minutes.
- **Round 2 is recorded under `verifications`**, with the verifier's reasons and a response for each of the 30 claims.

**What I did not do:**
- **No full SPM12-style realignment or slice-timing correction.** The shift regression is a check, not a correction, and I applied it only to fig3d.
- **No Tukey taper in the GLM.**
- **fig4b stays partially reproduced.** The mean holds and the count does not, which matches the protocol's "holds only in part". The question for a reader in `questions/okuno-2025.yaml` stays open.
- **Nothing committed**, as instructed.

## End of run

62 turns, 120 minutes, $3.48 at API prices, result: success.
