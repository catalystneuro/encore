# sadeghi-2019 · author-revise-1 · run 43549100374

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md | head -c 60000 | wc -c; ls entries/sadeghi-2019 transcripts/sadeghi-2019 questions | head -50
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/sadeghi-2019/verifier-1-report.md"
}
```

```
1	I've verified all 28 claims in the claims file. 21 were tested, 2 neural claims are blocked for missing data, and 7 model-classifier claims are blocked as "too large". That last blocking isn't supported: the notebook's own estimate is 56–115 min, so the 7 claims were never run.
2	
3	**A. Outcomes**
4	
5	| Claim | My outcome | Reason |
6	|---|---|---|
7	| fig1k-example-temporal-widths | reproduced (depends on one reading) | Cell 10: the `code_half` window with the channel-mean curve gives 10/11 within tolerance, and crowd and water are narrower than fire. The two window readings the claims file names give at most 8/11, which would be partially reproduced. `code_half` comes from NeuralExample.m, which I could not see. Its 60.9 ms snake period fits S1 Text, which puts the first-half rattle at about 16.5 Hz. |
8	| fig1-snr-noise-stronger | partially_reproduced | Cell 12: no reading gets both means and ≥3 of 4 bounds. Several readings have both means within the SD tolerance and SNR mostly below 0 dB (e.g. whole (a)(d)(e): −11.8 / −8.1 dB, 100% / 85% negative). |
9	| fig1-s5-model-predicts-neural | blocked (data_missing) | The data set has no tone-pip responses, so no best frequencies. Agreed (see B6). |
10	| fig2-noise-restricted | reproduced | Cell 14: noise width at 50% is narrower for 5/5 sounds in both domains, under every window. The SD across sounds is lower for noise (spectral 0.33 vs 0.68; temporal 3.63 vs 48.67). |
11	| fig3a-example-tonotopy-removal | partially_reproduced | Cell 18: no reading has both values in tolerance (without tonotopy: 45.1, 31.3, 60.0, 30.0 against 35 ± 3.5). The drop is ≥20 points under every reading (20.0 to 40.0). |
12	| fig3a-example-classifier-order | partially_reproduced | Cell 20: the order st ≥ spec ≥ temp holds under 1a2b a(a), 1b2a and 1b2b a(a). The noiseless rule fails under every reading; noiseless temporal is 15–20 points below single-trial, not similar. |
13	| fig3b-population-above-chance | reproduced | Cell 22: under ev
[... 43 more lines not kept]
```

```
Sat Nov 14 03:03:48 UTC 2026
40441
entries/sadeghi-2019:
README.md
entry.yaml
model.py
reproduce_sadeghi_2019_model.ipynb
reproduce_sadeghi_2019_neural.ipynb
requirements.in
requirements.lock.txt
sadeghi.py

questions:
README.md
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/71db02ca-3d13-4a7f-b5bf-1b3c1460bbaa/tool-results/bm2o7xcsi.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/71db02ca-3d13-4a7f-b5bf-1b3c1460bbaa/tool-results/bm2o7xcsi.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 657 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep sadeghi; wc -l attempts/sadeghi-2019-01.yaml entries/sadeghi-2019/*; cat entries/sadeghi-2019/entry.yaml; git status --short; git diff --stat; ls executed/sadeghi-2019 2>/dev/null
```

```
sadeghi-2019-01.yaml
   370 attempts/sadeghi-2019-01.yaml
    40 entries/sadeghi-2019/README.md
    27 entries/sadeghi-2019/entry.yaml
   188 entries/sadeghi-2019/model.py
   520 entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb
  1213 entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb
     8 entries/sadeghi-2019/requirements.in
  1636 entries/sadeghi-2019/requirements.lock.txt
   674 entries/sadeghi-2019/sadeghi.py
  4676 total
schema_version: 1
name: sadeghi-2019
type: reproduction
title: A neural ensemble correlation code for sound category identification (Sadeghi et al. 2019)
description: Tests the findings of Sadeghi, Zhai, Stevenson and Escabi (2019) on CRCNS bst-2, which
  holds the analog multiunit activity of 35 inferior colliculus recordings in unanesthetized rabbits
  (13 sites listening to five natural sounds, 11 to their 1/f spectrum-equalized variants, 11 to six
  exemplars of three categories) and the 195 sounds of the paper's auditory model. It recomputes the
  stimulus-driven and noise correlations with a port of the paper's code, the single-trial
[... 41 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/sadeghi-2019-01.yaml"
}
```

```
1	schema_version: 3
2	id: sadeghi-2019-01
3	datasets:
4	- archive: crcns
5	  id: bst-2
6	  version: unversioned
7	  doi: 10.6080/K03X84V3
8	  relation: primary
9	paper: doi:10.1371/journal.pbio.3000449
10	date: '2026-11-13'
11	entry: sadeghi-2019
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 351 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/sadeghi-2019/model.py"
}
```

```
1	"""Cochlear model and short-term correlations for Sadeghi et al. (2019), from the Methods
2	("Auditory model", "Nonstationary spectro-temporal correlation statistics", "Stationarity and
3	ensemble diversity indices") and the paper's MATLAB code in the data set
4	(Code/AuditoryModelCorr: cochleogram.m, cochleogramdyncorr.m, xcorrst.m, xcorrstsym.m,
5	fdesignkdt.m, finddtdfw.m, gammatonefilter.m, lowpass.m, fdesignh.m, h.m).
6	
7	Where each parameter comes from:
8	- 58 gammatone filters of order 3, phase 0, centre frequencies from 100 Hz to 16 kHz in 1/8
9	  octave steps (Methods; centres placed as cochleogram.m does, Xc = (0.5 .. L-0.5)/L log2(fN/f1)).
10	- Bandwidths b = 25 + 75 (1 + 1.4 f^2)^0.69, f in kHz (Methods). The code's ModelExample.m uses
11	  criticalbandwidth.m, 94 + 71 f^1.5, which differs; the Methods are followed (protocol, reader
12	  step 2) and the difference is recorded as a finding.
13	- Passband gain 1 (Methods; gammatonefilter.m divides by the peak of |FFT|).
14	- Envelope: magnitude of the analytic signal, low-pass at 500 Hz with 125 Hz transition and 60 dB
15	  attenuation (Methods), designed as lowpass.m/fdesignh.m/h.m do, negative values set to 0
16	  (cochleogram.m), then resampled to 1 kHz (Methods; the code's ModelExample.m keeps 3675 Hz).
17	- The sound is normalised to unit SD first (cochleogramdyncorr.m).
18	- Short-term correlation: Kaiser window, beta from 40 dB attenuation (fdesignkdt.m gives 3.395,
19	  the Methods say 3.4), length chosen so that two SDs of the window (finddtdfw.m) equal tau_W;
20	  normalised as a correlation coefficient with time- and delay-dependent means and variances
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  id:" claims/sadeghi-2019.yaml | head -40; python - <<'EOF'
import json
nb=json.load(open('entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb'))
for i,c in enumerate(nb['cells']):
    print('---',i,c['cell_type'],c['metadata'].get('tags'))
    print(''.join(c['source'])[:3000])
EOF
```

```
110:- id: fig1k-example-temporal-widths
182:- id: fig1-snr-noise-stronger
228:- id: fig1-s5-model-predicts-neural
269:- id: fig2-noise-restricted
290:- id: fig3a-example-tonotopy-removal
311:- id: fig3a-example-classifier-order
326:- id: fig3b-population-above-chance
345:- id: figs6-per-sound-above-chance
367:- id: figs9-mixing-coefficient
388:- id: figs10-amua-tmua
424:- id: fig4-example-original-vs-equalized
446:- id: fig4e-population-original-vs-equalized
474:- id: fig4f-example-equalized-classification
513:- id: fig4h-population-equalized-classification
553:- id: fig8b-example-pca-variance
580:- id: fig8e-example-categorization
601:- id: fig8f-population-categorization
636:- id: fig5-speech-water-widths
663:- id: fig6-category-half-widths
699:- id: fig6c-category-diversity
[... 324 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,110p claims/sadeghi-2019.yaml
```

```
# Claims for Sadeghi, Zhai, Stevenson & Escabi (2019), "A neural ensemble correlation code for
# sound category identification", PLoS Biol 17(10):e3000449, on CRCNS data set bst-2.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
# protocol as stated in docs/protocol.md (Reader). The writer did not look at the data set's data or
# files; only its description (paper/bst-2.data-description.txt) was read, to know what it holds.
#
# Text read: the version of record (PMC6788721, Europe PMC full-text XML, flattened), with its
# Results, Discussion, Materials and methods, all figure legends (Figs 1 to 10, S1 to S10 Figs),
# and the supplement files S1 Text (s001, proofs on signal and noise correlations, and notes on
# S2 to S4 and S6 Figs), S1 Table (s026, the 195 model sounds) and S2 Table (s027, the 18 sounds
# of paradigm 3). No PDF was supplied. The extraction dropped every displayed equation (the
# shuffled and unshuffled correlograms, their normalization, the noise correlation, the MAP
# rule, the spectro-temporal model average, the 1/f filter, the SI and CDI formulas); the prose
# around each was read and the criteria below name where an equation would have settled a
# detail. The movies and sound files listed as supporting information were not read; no claim
# rests on them.
#
# Code: the paper links only the CRCNS deposit (doi:10.6080/K03X84V3), which holds MATLAB code
# (Code/MUACorrAnalysis, with rastermuashuffledxcovwinfastN.m; Code/AuditoryModelCorr, with
# Cochleogram.m and cochleogramdyncorr.m; Code/Examples, with NeuralExample.m for Fig 1 and
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 760,1000p claims/sadeghi-2019.yaml
```

```
- id: fig9a-optimal-resolution
  statement: In the 13-category model task, the spectral and temporal correlation classifiers
    perform best at a window resolution of 141 ms and the spectro-temporal classifier at 100 ms,
    and all perform above chance (7.69%) at every resolution.
  source: Results, Decoding sound-correlation statistics to categorize sounds, paragraph 2; Figure
    9A
  quote: The optimal window resolution for both the temporal and spectral classifiers is 141 ms,
    while the optimal resolution for the joint spectro-temporal classifier is slightly faster (100
    ms). Classification performance is above chance for all temporal resolutions tested ( Fig 9A ;
    chance performance = 7.69%; p < 0.01, t test, Bonferroni correction)
  statistics:
  - test: t test against chance
    p: 0.01
    p_relation: <
    corrected: Bonferroni
  expected:
  - quantity: optimal tau_W, spectral and temporal
    value: 141
    tolerance: 14.1
    unit: ms
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -n -i "Dimensionality reduction\|Bayesian classifier\|Cross validation\|Spectrum-based classifier\|Optimal temporal resolution" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 330,360p paper/10.1371-journal.pbio.3000449.txt; grep -n "Fig 10\|vocalization" paper/10.1371-journal.pbio.3000449.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,140p entries/sadeghi-2019/sadeghi.py
```

```
"""Loading and measures for Sadeghi, Zhai, Stevenson & Escabi (2019) on CRCNS bst-2.

The data set is one gzip-compressed tar file (bst-2/live/data.tar.gz, 5.3 GB) in the public
S3 bucket crcnsarchive. A gzip stream cannot be read at random, so `stream_members` reads it
once from the start over HTTP and hands each wanted member to the caller in memory; nothing
is written to disk. The neural files are MATLAB 7.3 (HDF5) files, read with h5py from memory.

Where each parameter comes from:

- Correlations (`window_corr`) port the paper's own MATLAB code in the data set,
  Code/MUACorrAnalysis/rastermuashuffledxcorrwinfast.m and rastermuashuffledxcovwinfast.m
  (Materials and methods, "Neural ensemble stimulus-driven correlation" and "Neural ensemble
  noise correlation", whose equations the text lost): square window of Nw samples centred at
  T0, PSTH-based shuffled correlogram with the within-trial terms removed, noise correlogram
  as unshuffled minus shuffled, all normalised by the unshuffled (signal plus noise) variances
  (R12_sh, R12_ush, R12_noise of the code). Maximum delay 100 ms (Noiseless neural classifier,
  paragraph 6, and NeuralExample.m).
- Single-trial correlations (`single_trial_features`) are the same code applied to one trial
  with the within-trial terms kept (the "unshuffled correlations for individual trials" of
  "Single-trial neural classifier").
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        print('---',i,out[:2500])
EOF
```

```
--- 1 
--- 3 read 195 files in 3 s

--- 4 categories: 13 ['Automobile_Engines', 'Bell', 'Bird_Chorus', 'Cat_Meowing', 'Dog_Barking', 'Fire', 'Flowing_Water', 'Human_Speech', 'Single_Bird_Songs', 'Speech_Babble', 'Thunder_Rain', 'Wave', 'Wind']
Automobile_Engines   sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 13.3-52.0
Bell                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 31.8-52.1
Bird_Chorus          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 23.0-51.4
Cat_Meowing          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 9.4-48.0
Dog_Barking          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 24.4-42.0
Fire                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 26.1-50.0
Flowing_Water        sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 32.4-34.7
Human_Speech         sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 28.9-37.0
Single_Bird_Songs    sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 29.7-45.2
Speech_Babble        sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 26.4-38.5
Thunder_Rain         sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 12.3-67.8
Wave                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 22.0-48.8
Wind                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 13.6-72.1
WAV header of one file: format tag 1 bits 16 (1 = integer PCM; the data description says double precision, normalised to SD 0.001)
SD as a fraction of full scale, all model sounds: 0.00029 to 0.0022

[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "spectro-temporal classifier\|joint spectro\|spectro-temporal correlation classifier\|time-averaged classifier\|time averaged" paper/10.1371-journal.pbio.3000449.txt | cut -c1-600; sed -n 139,140p paper/10.1371-journal.pbio.3000449.txt; sed -n 300,330p paper/10.1371-journal.pbio.3000449.txt | cut -c1-1500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; grep -n "def cmd_run\|def run\|--fresh\|--only\|notebook" tools/entry.py | head -40; nproc; free -g
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 345,424p claims/sadeghi-2019.yaml; python - <<'EOF'
import json
nb=json.load(open('entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print('---',i,c['cell_type'],c['metadata'].get('tags'), len(s))
    print(s[:300])
EOF
```

```
- id: figs6-per-sound-above-chance
  statement: Single-trial accuracy at 1 s exceeds chance for every sound and classifier except the
    snake sound with the temporal classifiers (p = 0.15 with tonotopy, 0.92 without).
  source: S6 Fig legend
  quote: The classification accuracy of the single-trial classifier at 1 s duration exceeded chance
    ( p < 0.05, t test) for all conditions except for the snake sound
  statistics:
  - about: all other sounds and classifiers against chance
    test: t test
    p: 0.05
    p_relation: <
  - about: snake, temporal classifier
    test: t test
    p: 0.15
  - about: snake, temporal classifier without tonotopy
    test: t test
    p: 0.92
  criterion: Per sound, the fraction of single-trial decisions for that sound that are correct, at
    1 s, per site; t test across the 13 sites against 20% at p < 0.05. Readings (1) and (2) of
    the opening comment. Reproduced when, under one reading, at least 17 of the 18 non-snake-temporal
[... 399 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; mkdir -p $TMPDIR/dev; time python - <<'EOF'
import fsspec, tarfile, os, pickle
D=os.environ['TMPDIR']+'/dev'
URL="https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
f=fsspec.open(URL,block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
names=[]; snd={}; code={}
for m in tf:
    names.append((m.name,m.size,m.isfile()))
    if m.isfile() and "/ModelSounds/" in m.name and m.name.endswith(".wav"):
        snd[m.name]=tf.extractfile(m).read()
    elif m.isfile() and m.name.endswith(".m"):
        code[m.name]=tf.extractfile(m).read()
pickle.dump(names,open(D+'/names.pkl','wb')); pickle.dump(snd,open(D+'/snd.pkl','wb')); pickle.dump(code,open(D+'/code.pkl','wb'))
print(len(names), len(snd), len(code))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'fsspec'

real	0m0.025s
user	0m0.017s
sys	0m0.008s
```

**Agent calls Bash**

```bash
cd  ls -a executed/ | head; ls -d .venv* envs* 2>/dev/null; grep -n "venv\|env_dir" tools/entry.py | head
```

```
.
..
sadeghi-2019
519:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
555:    venv = (output_dir / ".venv").resolve()
556:    python = venv / "bin" / "python"
560:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
563:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
577:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent calls Bash**

```bash
cd  ls -a executed/sadeghi-2019/; sed -n 553,566p tools/entry.py
```

```
.
..
.clean-run.json
.venv
reproduce_sadeghi_2019_model.ipynb
reproduce_sadeghi_2019_neural.ipynb
result.json
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; cp -r executed/sadeghi-2019/.venv $TMPDIR/venv 2>/dev/null; time $PY - <<'EOF'
import fsspec, tarfile, os, pickle
D=os.environ['TMPDIR']+'/dev'
URL="https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
f=fsspec.open(URL,block_size=2**24).open()
tf=tarfile.open(fileobj=f,mode="r|gz")
names=[]; snd={}; code={}
for m in tf:
    names.append((m.name,m.size,m.isfile()))
    if m.isfile() and "/ModelSounds/" in m.name and m.name.endswith(".wav"):
        snd[m.name]=tf.extractfile(m).read()
    elif m.isfile() and (m.name.endswith(".m") or m.name.lower().endswith(".txt")):
        code[m.name]=tf.extractfile(m).read()
pickle.dump(names,open(D+'/names.pkl','wb')); pickle.dump(snd,open(D+'/snd.pkl','wb')); pickle.dump(code,open(D+'/code.pkl','wb'))
print(len(names), len(snd), len(code))
EOF
```

```
311 195 19

real	4m45.864s
user	0m31.599s
sys	0m13.258s
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import pickle
names=pickle.load(open('names.pkl','rb'))
for n,s,f in names:
    if '/ModelSounds/' in n and n.endswith('.wav'): continue
    print(n,s)
EOF
```

```
data 0
data/Docs 0
data/Docs/FigureData.docx 118935
data/Docs/crcns_data_description.docx 26647
data/Sounds 0
data/Sounds/Paradigm3 0
data/Sounds/Paradigm3/S3_Sound_Fire5.wav 529280
data/Sounds/Paradigm3/S3_Sound_Water1.wav 529280
data/Sounds/Paradigm3/S3_Sound_Speech1.wav 529280
data/Sounds/Paradigm3/S3_Sound_Speech3.wav 529280
data/Sounds/Paradigm3/S3_Sound_Fire3.wav 529280
data/Sounds/Paradigm3/S3_Sound_Speech4.wav 529280
data/Sounds/Paradigm3/S3_Sound_Water2.wav 529280
data/Sounds/Paradigm3/S3_Sound_Speech5.wav 529280
data/Sounds/Paradigm3/S3_Sound_Water4.wav 529280
data/Sounds/Paradigm3/S3_Sound_Speech6.wav 529280
data/Sounds/Paradigm3/S3_Sound_Fire1.wav 529280
data/Sounds/Paradigm3/S3_Sound_Water5.wav 529280
data/Sounds/Paradigm3/S3_Sound_Water3.wav 529280
data/Sounds/Paradigm3/S3_Sound_Fire4.wav 529280
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python -c "
import pickle; c=pickle.load(open('code.pkl','rb')); print(c['data/Code/Examples/NeuralExample.m'].decode('latin1'))"
```

```
%%
% This routine takes data from an example recording location and generates
% the signal and noise correlograms (both for temporal and spectral) from the
% multi-channel and multi-trial MUA responses as described in Sadeghi et al
% PLOS Bio 2019
%
% The example used is the sam as Fig. 1. The routine generates Panels
% B-M of that figure
%
% (C) X. Zhai & M.A. Escabi (2019)
%

%Load data for paradigm 1 site 04
load('../../NeuralData/Paradigm1/P1_Site04.mat', 'Data')

%Some parameters
RASNFire=Data.Sound(1);                 %Fire sound response
RASNWater=Data.Sound(4);                %Water sound response
NChan=length(RASNFire.Channel);         %16 channel
Fsd=RASNFire.Channel(1).Fs;             %Raster sampling rate
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY -c "
import numpy as np, model as M
for tw in 25*2**(np.arange(10)/2):
    K,b=M.kaiser_for(tw/1000); print(round(tw,1), len(K))
"; date -u
```

```
25.0 69
35.4 97
50.0 135
70.7 191
100.0 269
141.4 381
200.0 537
282.8 759
400.0 1073
565.7 1517
Sat Nov 14 03:11:51 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sadeghi-2019/model.py",
 "old_string": "def short_term_iter(S, tau_w_ms, maxlag, step=None, pairs=\"all\"):\n    K, _ = kaiser_for(tau_w_ms / 1000)\n    W = np.sqrt(K)\n    N = (len(W) - 1) // 2\n    maxlag = min(maxlag, N)\n    nw = 2 * N + 1\n    step = step or max(1, int(round(tau_w_ms / 4)))\n    C, T = S.shape\n    lags = np.arange(-maxlag, maxlag + 1)\n    # sliding sums over every window start s: sum_j W[j] S[c, s + j] and sum_j K[j] S[c, s + j]^2\n    SW = signal.fftconvolve(S, W[None, ::-1], mode=\"valid\", axes=1) / nw\n    SK2 = signal.fftconvolve(S ** 2, K[None, ::-1], mode=\"valid\", axes=1) / nw\n    L = nw + 2 * maxlag\n    nfft = 1 << int(np.ceil(np.log2(L + nw)))\n    for k in range(2 * N, T - 2 * N, step):",
 "new_string": "def short_term_iter(S, tau_w_ms, maxlag, step=None, pairs=\"all\", centres=None):\n    \"\"\"centres: the window centres (samples) to use; by default every step from 2N to T - 2N.\"\"\"\n    K, _ = kaiser_for(tau_w_ms / 1000)\n    W = np.sqrt(K)\n    N = (len(W) - 1) // 2\n    maxlag = min(maxlag, N)\n    nw = 2 * N + 1\n    step = step or max(1, int(round(tau_w_ms / 4)))\n    C, T = S.shape\n    lags = np.arange(-maxlag, maxlag + 1)\n    # sliding sums over every window start s: sum_j W[j] S[c, s + j] and sum_j K[j] S[c, s + j]^2\n    SW = signal.fftconvolve(S, W[None, ::-1], mode=\"valid\", axes=1) / nw\n    SK2 = signal.fftconvolve(S ** 2, K[None, ::-1], mode=\"valid\", axes=1) / nw\n    L = nw + 2 * maxlag\n    nfft = 1 << int(np.ceil(np.log2(L + nw)))\n    for k in (range(2 * N, T - 2 * N, step) if centres is None else centres):"
}
```

```
The file entries/sadeghi-2019/model.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; cat requirements.in; grep -i "joblib\|threadpoolctl\|scikit" requirements.lock.txt | head
```

```
aiohttp
fsspec
h5py
matplotlib
numpy
requests
scikit-learn
scipy
    # via joblib
joblib==1.6.0 \
    # via scikit-learn
    # via scikit-learn
    #   scikit-learn
scikit-learn==1.9.1 \
    #   scikit-learn
threadpoolctl==3.8.0 \
    # via scikit-learn
```

**Agent**

Now the classifier code, appended to `model.py`.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; cat >> model.py <<'EOF'


# ---------------------------------------------------------------- model classifier (Figs 9, 10)
#
# Methods, "Dimensionality reduction and distribution model", "Bayesian classifier", "Cross
# validation", "Optimal temporal resolution and integration time", "Spectrum-based classifier";
# claims file, opening comment (readings 6 and 7). Choices the paper does not make, each stated
# in the notebook as an assumption or a standard choice:
# - training observations are the short-term features at every tau_W / 4 (the step used above),
#   at most TRAIN_CAP per category by a seeded random subsample (standard choice, for speed);
# - the spectro-temporal feature vector is the spectral and temporal features of one time point
#   side by side (assumption: the Methods give it its own PCs and N_c, so it is one vector);
# - temporal observations are (time point, channel) pairs, and a window's temporal log-likelihood
#   is summed over its 58 channels (Methods: "both time points and different frequency channels
#   are treated as observations"; "features at each time sample are conditionally independent");
# - the spectrum feature is the Kaiser-weighted mean envelope of each channel in the window;
# - PCA is fitted once on the training observations of all 195 sounds (assumption; refitting it
#   in every fold is run as a variant).

TRAIN_CAP = 20000
RES_MS = 25 * 2 ** (np.arange(10) / 2)  # 25 to 566 ms in half octave steps (Methods)
REPORTED = {"spec": (26, 8), "temp": (8, 5), "st": (87, 13)}  # (PCs, N_c), Methods


def features(S, tau_w_ms):
    """Short-term features of one cochleogram at resolution tau_w_ms, on a grid of window
    centres every tau_W / 4 where the window and every lag fit in the sound.
    Returns dict spec (n, 1653), temp (n, 58, maxlag), spectrum (n, 58), centres (ms), K."""
    K, _ = kaiser_for(tau_w_ms / 1000)
    N = (len(K) - 1) // 2
    maxlag = min(int(tau_w_ms // 2), N)
    step = max(1, int(round(tau_w_ms / 4)))
    C, T = S.shape
    centres = np.arange(N + maxlag, T - N - maxlag - 1, step)
    iu = np.triu_indices(C, 1)
    spec = np.array([z[iu] for z in short_term_iter(S, tau_w_ms, 0, pairs="zero", centres=centres)], np.float32)
    temp = np.array([a[:, maxlag + 1:] for a in short_term_iter(S, tau_w_ms, maxlag, pairs="auto", centres=centres)],
                    np.float32)
    SK = signal.fftconvolve(S, K[None, ::-1], mode="valid", axes=1) / K.sum()
    spectrum = SK[:, centres - N].T.astype(np.float32)
    return {"spec": spec, "temp": temp, "spectrum": spectrum, "centres": centres, "klen": len(K), "step": step}


def test_index(F, spacing_ms):
    """Grid indices of consecutive non-overlapping test windows from the start of the sound, at
    least spacing_ms apart (reading 6a: tau_W; 6b: the full Kaiser window length)."""
    stride = int(np.ceil(spacing_ms / F["step"] - 1e-9))
    return np.arange(0, len(F["centres"]), stride)


def n_steps(nmax):
    """N = 1 to the largest number of windows in half octave steps (Cross validation)."""
    ns = sorted({int(round(2 ** (j / 2))) for j in range(40) if round(2 ** (j / 2)) <= nmax})
    return ns if ns[-1] == nmax else ns + [nmax]
EOF
date -u
```

```
Sat Nov 14 03:12:36 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; time OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 $PY - <<'EOF'
import pickle, os, numpy as np, model as M
from joblib import Parallel, delayed
D=os.environ['TMPDIR']+'/dev'
snd=pickle.load(open(D+'/snd.pkl','rb'))
keys=sorted(snd)
def f(k):
    fs,x=M.read_wav(snd[k]); return M.cochleogram(x,fs).astype(np.float32)
out=Parallel(n_jobs=4)(delayed(f)(k) for k in keys)
coch={(k.split('/')[-2], int(k.split('_')[-1][:-4])): v for k,v in zip(keys,out)}
pickle.dump(coch, open(D+'/coch.pkl','wb'))
print(len(coch), out[0].shape)
EOF
```

```
195 (58, 10000)

real	5m54.839s
user	16m28.540s
sys	6m39.875s
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; cat >> model.py <<'EOF'


def obs_of(F, kind, idx=None):
    """Observations of one sound for a classifier: (n, m, d), m = 58 channels for temporal, else 1.
    idx selects grid points (all by default)."""
    sl = slice(None) if idx is None else idx
    if kind == "spec":
        return F["spec"][sl][:, None]
    if kind == "spectrum":
        return F["spectrum"][sl][:, None]
    if kind == "temp":
        return F["temp"][sl]
    t = F["temp"][sl]
    return np.concatenate([F["spec"][sl], t.reshape(len(t), -1)], 1)[:, None]


def fit_pca(Fs, kind, rng, nfit=15000, kmax=150):
    """PCA of the pooled observations of the sounds Fs (list of feature dicts), fitted on at most
    nfit rows drawn at random (standard choice). Returns mean, components (k, d), and the
    cumulative fraction of the total variance (trace) the components explain."""
    from sklearn.decomposition import PCA
    rows = []
    per = max(1, nfit // len(Fs))
    for F in Fs:
        X = obs_of(F, kind)
        X = X.reshape(-1, X.shape[-1])
        rows.append(X[rng.choice(len(X), min(per, len(X)), replace=False)])
    X = np.concatenate(rows).astype(np.float64)
    k = min(kmax, X.shape[1], X.shape[0] - 1)
    p = PCA(k, svd_solver="randomized" if X.shape[1] > 500 else "full", random_state=0).fit(X)
    total = X.var(0, ddof=1).sum()
    return p.mean_, p.components_.astype(np.float32), np.cumsum(p.explained_variance_) / total


def project(F, kind, mean, comps):
    X = obs_of(F, kind)
    n, m, d = X.shape
    return ((X.reshape(-1, d) - mean.astype(np.float32)) @ comps.T).reshape(n, m, -1)


def fit_gmm(X, nc, seed=0):
    from sklearn.mixture import GaussianMixture
    return GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed).fit(X)


def train_rows(Zs, npc, rng, cap=TRAIN_CAP):
    X = np.concatenate([z[:, :, :npc].reshape(-1, npc) for z in Zs])
    return X if len(X) <= cap else X[rng.choice(len(X), cap, replace=False)]


def window_ll(gm, Zw, npc):
    """Log-likelihood of each test window (n, m, d): summed over its m observations."""
    n, m, _ = Zw.shape
    return gm.score_samples(Zw[:, :, :npc].reshape(-1, npc).astype(np.float64)).reshape(n, m).sum(1)


def loso(Z, labels, npc, nc, tests, seed, n_jobs=4):
    """Leave one sound out (Cross validation). Z: per-sound observations (n, m, d); labels: class
    of each sound; tests: per-sound dict {name: window arrays (n_w, m, d)} to score. A fold
    changes only the held-out sound's class model, so each class is fitted once on all its
    sounds and refitted once per held-out sound. Returns {name: (sounds, n_w, classes) LL} and
    the fitted models."""
    from joblib import Parallel, delayed
    labels = np.asarray(labels)
    classes = np.unique(labels)
    rs = np.random.SeedSequence(seed)
    seeds = rs.generate_state(len(Z) + len(classes))

    def job(c, leave):
        idx = [i for i in np.flatnonzero(labels == c) if i != leave]
        rng = np.random.default_rng(seeds[leave if leave >= 0 else len(Z) + int(np.flatnonzero(classes == c)[0])])
        return fit_gmm(train_rows([Z[i] for i in idx], npc, rng), nc)

    full = Parallel(n_jobs=n_jobs)(delayed(job)(c, -1) for c in classes)
    refit = Parallel(n_jobs=n_jobs)(delayed(job)(labels[j], j) for j in range(len(Z)))
    out = {}
    for name in tests[0]:
        LL = []
        for j in range(len(Z)):
            Zw = tests[j][name]
            col = [window_ll(refit[j] if c == labels[j] else full[k], Zw, npc) for k, c in enumerate(classes)]
            LL.append(np.array(col).T)
        out[name] = LL
    return out, full, refit


def accuracy_curve(LL, labels, classes, ns):
    """Fraction correct (per sound 0/1) after summing the log-likelihoods of the first N windows."""
    labels = np.asarray(labels)
    res = np.zeros((len(LL), len(ns)))
    for j, L in enumerate(LL):
        cs = np.cumsum(L, 0)
        for i, n in enumerate(ns):
            res[j, i] = classes[int(np.argmax(cs[min(n, len(cs)) - 1]))] == labels[j]
    return res
EOF
date -u
```

```
Sat Nov 14 03:19:18 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; cat > $TMPDIR/dev/t1.py <<'EOF'
import pickle, os, time, sys, resource, numpy as np, model as M
from threadpoolctl import threadpool_limits
threadpool_limits(1)
D=os.environ['TMPDIR']+'/dev'
coch=pickle.load(open(D+'/coch.pkl','rb'))
keys=sorted(coch); cats=sorted({k[0] for k in keys}); labels=[cats.index(k[0]) for k in keys]
tw=float(sys.argv[1]); kinds=sys.argv[2].split(',')
t0=time.time()
Fs=[M.features(coch[k].astype(np.float64), tw) for k in keys]
print('features', round(time.time()-t0), 's', len(Fs[0]['centres']), 'grid points', Fs[0]['temp'].shape, flush=True)
rng=np.random.default_rng(1)
for kind in kinds:
    t1=time.time()
    mean, comps, cum = M.fit_pca(Fs, kind, rng)
    Z=[M.project(F, kind, mean, comps) for F in Fs]
    npc90=int(np.searchsorted(cum, 0.9)+1)
    print(kind, 'pca', round(time.time()-t1), 's; PCs for 90%:', npc90, 'cum at k:', round(float(cum[-1]),3), flush=True)
    npc, nc = M.REPORTED.get(kind, (npc90, 8))
    ia = M.test_index(Fs[0], tw); ib = M.test_index(Fs[0], Fs[0]['klen'])
    tests=[{'a': z[ia], 'b': z[ib]} for z in Z]
    t1=time.time()
    LL, full, refit = M.loso(Z, labels, npc, nc, tests, 5)
    print(kind, 'loso', round(time.time()-t1), 's', flush=True)
    for nm, idx in (('a', ia), ('b', ib)):
        ns=M.n_steps(len(idx)); acc=M.accuracy_curve(LL[nm], labels, np.arange(13), ns)
        print(kind, nm, 'N', ns, 'acc', np.round(100*acc.mean(0),1))
print('peak GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
time $PY $TMPDIR/dev/t1.py 141.42 spec,temp
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/t1.py", line 1, in <module>
    import pickle, os, time, sys, resource, numpy as np, model as M
ModuleNotFoundError: No module named 'model'

real	0m0.107s
user	0m0.332s
sys	0m0.014s
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; time PYTHONPATH=. $PY $TMPDIR/dev/t1.py 141.42 spec,temp
```

```
features 80 s 271 grid points (271, 58, 70)
spec pca 4 s; PCs for 90%: 26 cum at k: 0.987
spec loso 10 s
spec a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 55] acc [53.3 59.5 65.6 66.7 72.8 75.9 77.9 79.  81.5 81.  82.1 81.5]
spec b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 25] acc [53.3 64.6 71.8 76.4 74.9 77.4 77.9 81.5 82.6 81.5]
temp pca 1 s; PCs for 90%: 8 cum at k: 1.0
temp loso 16 s
temp a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 55] acc [46.2 51.3 56.9 59.5 67.7 71.3 73.3 78.5 77.4 76.4 76.4 77.9]
temp b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 25] acc [46.2 55.4 63.6 64.6 70.8 76.4 76.9 76.9 77.4 78.5]
peak GB 2.934148

real	1m52.198s
user	2m40.564s
sys	0m10.462s
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; sed -i 's/^Fs=\[M.features(coch\[k\].astype(np.float64), tw) for k in keys\]/from joblib import Parallel, delayed\nFs=Parallel(n_jobs=4)(delayed(M.features)(coch[k].astype(np.float64), tw) for k in keys)/' $TMPDIR/dev/t1.py; time PYTHONPATH=. $PY $TMPDIR/dev/t1.py 100 st,spectrum
```

```
features 46 s 386 grid points (386, 58, 50)
st pca 9 s; PCs for 90%: 90 cum at k: 0.934
st loso 30 s
st a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 97] acc [58.5 64.1 64.1 66.7 71.3 73.3 78.5 81.  80.5 81.5 82.6 82.6 82.6 82.1]
st b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 36] acc [58.5 65.6 69.2 72.3 79.  80.  82.1 82.1 83.1 80.5 81. ]
spectrum pca 0 s; PCs for 90%: 6 cum at k: 1.0
spectrum loso 6 s
spectrum a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 97] acc [44.1 53.8 53.3 57.9 67.2 68.2 70.3 71.8 71.8 74.4 76.9 74.9 75.9 76.9]
spectrum b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 36] acc [44.1 55.9 66.2 67.2 71.8 69.7 73.8 75.9 73.8 76.4 76.4]
peak GB 3.463788

real	1m33.338s
user	4m51.594s
sys	0m25.436s
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; time PYTHONPATH=. $PY $TMPDIR/dev/t1.py 25 spec,temp,st,spectrum; date -u
```

```
features 55 s 1652 grid points (1652, 58, 12)
spec pca 5 s; PCs for 90%: 81 cum at k: 0.954
executed/sadeghi-2019/.venv/lib/python3.13/site-packages/joblib/externals/loky/process_executor.py:787: UserWarning: A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak.
  warnings.warn(
joblib.externals.loky.process_executor._RemoteTraceback: 
"""
Traceback (most recent call last):
  File "executed/sadeghi-2019/.venv/lib/python3.13/site-packages/joblib/externals/loky/process_executor.py", line 490, in _process_worker
    r = call_item()
  File "executed/sadeghi-2019/.venv/lib/python3.13/site-packages/joblib/externals/loky/process_executor.py", line 291, in __call__
    return self.fn(*self.args, **self.kwargs)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "executed/sadeghi-2019/.venv/lib/python3.13/site-packages/joblib/parallel.py", line 607, in __call__
    return [func(*args, **kwargs) for func, args, kwargs in self.items]
            ~~~~^^^^^^^^^^^^^^^^^
  File "entries/sadeghi-2019/model.py", line 315, in job
    return fit_gmm(train_rows([Z[i] for i in idx], npc, rng), nc)
  File "entries/sadeghi-2019/model.py", line 286, in fit_gmm
    return GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed).fit(X)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
s=open('model.py').read()
s=s.replace('''def fit_gmm(X, nc, seed=0):
    from sklearn.mixture import GaussianMixture
    return GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed).fit(X)''','''def fit_gmm(X, nc, seed=0):
    """Diagonal GMM (Methods). scikit-learn's default variance floor (reg_covar 1e-6); a fit that
    fails on a collapsed component is refitted with 1e-4 (standard choice) and flagged."""
    from sklearn.mixture import GaussianMixture
    X = np.asarray(X, np.float64)
    try:
        gm = GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed).fit(X)
        gm.refitted_ = False
    except ValueError:
        gm = GaussianMixture(nc, covariance_type="diag", max_iter=200, random_state=seed, reg_covar=1e-4).fit(X)
        gm.refitted_ = True
    return gm''')
open('model.py','w').write(s)
EOF
time PYTHONPATH=. $PY $TMPDIR/dev/t1.py 25 spec,temp,st,spectrum; date -u
```

```
features 55 s 1652 grid points (1652, 58, 12)
spec pca 5 s; PCs for 90%: 81 cum at k: 0.954
executed/sadeghi-2019/.venv/lib/python3.13/site-packages/joblib/externals/loky/process_executor.py:787: UserWarning: A worker stopped while some jobs were given to the executor. This can be caused by a too short worker timeout or by a memory leak.
  warnings.warn(
spec loso 106 s
spec a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 181, 256, 331] acc [34.4 34.9 41.5 45.1 49.7 52.3 54.9 56.9 60.5 63.1 71.8 72.8 73.8 73.3
 74.4 72.3 73.3]
spec b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 138] acc [34.4 42.6 43.1 47.7 51.3 51.8 57.9 64.6 70.8 74.4 76.4 76.4 75.9 72.8
 73.3]
temp pca 1 s; PCs for 90%: 5 cum at k: 1.0
temp loso 33 s
temp a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 181, 256, 331] acc [27.7 26.7 29.2 32.3 38.5 37.9 41.5 43.1 47.2 50.3 55.4 60.  60.  62.6
 63.6 65.1 64.6]
temp b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 138] acc [27.7 29.7 34.9 34.4 39.5 45.1 44.6 50.8 53.3 57.9 62.6 61.5 61.  64.6
 63.1]
st pca 7 s; PCs for 90%: 135 cum at k: 0.91
st loso 126 s
st a N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 181, 256, 331] acc [45.6 53.8 53.3 57.4 57.9 58.5 64.1 65.6 69.2 72.3 73.8 73.3 76.4 76.9
 76.9 77.9 76.9]
st b N [1, 2, 3, 4, 6, 8, 11, 16, 23, 32, 45, 64, 91, 128, 138] acc [45.6 52.3 55.4 57.4 65.6 64.1 67.7 74.9 74.4 74.9 75.4 75.4 77.4 76.9
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; sed -i 's/^TRAIN_CAP = 20000/TRAIN_CAP = 10000/' model.py; grep -n "TRAIN_CAP =" model.py; grep -n "def ttest_chance\|def within" -A8 sadeghi.py | head -30
```

```
209:TRAIN_CAP = 10000
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/build_clf.py <<'PYEOF'
import nbformat as nbf, sys
nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s))
def code(s, tag=None):
    c = nbf.v4.new_code_cell(s)
    if tag: c.metadata["tags"] = [tag]
    C.append(c)

md("""# Sadeghi et al. (2019): auditory model classifier claims (CRCNS bst-2)

Paper: Sadeghi M, Zhai X, Stevenson IH, Escabi MA (2019). A neural ensemble correlation code for
sound category identification. PLoS Biol 17(10):e3000449, doi:10.1371/journal.pbio.3000449. The
claims file (claims/sadeghi-2019.yaml) was written from the version of record (PMC6788721) with
its supplement.

Dataset: CRCNS bst-2 (doi:10.6080/K03X84V3), bst-2/live/data.tar.gz in the public bucket
crcnsarchive, `crcns:bst-2/unversioned` (CRCNS does not version data sets; the paper cites the DOI
only, and this is the bucket's only copy). The model sounds are
data/Sounds/ModelSounds/<category>/Sound_<n>.wav. The deposit's code (data/Code) has no classifier
code, so the classifier follows the Methods.

This notebook tests the model classification claims; the model correlation claims are in
reproduce_sadeghi_2019_model.ipynb and the neural claims in reproduce_sadeghi_2019_neural.ipynb.

| Claim | Tested here |
|---|---|
| fig9a-optimal-resolution | tested |
| fig9b-similar-maximum | tested |
| fig9b-accumulation-rate | tested |
| fig9c-time-averaged-worse | tested |
| fig9e-category-specific | tested |
| fig9-spectrum-classifier-lower | tested |
| fig10-vocalization-background | tested |

Method (Methods, "Dimensionality reduction and distribution model", "Bayesian classifier",
"Cross validation", "Optimal temporal resolution and integration time", "Spectrum-based
classifier"; model.py says where each parameter comes from): the cochleogram and short-term
correlations of reproduce_sadeghi_2019_model.ipynb at the ten resolutions tau_W = 25 to 566 ms;
spectral features c_kl(t, 0) without the diagonal, temporal features c_kk(t, tau) for tau from 1
ms to tau_W / 2 with time points and channels as observations, spectro-temporal features both side
by side, the spectrum feature the windowed mean envelope of each channel; PCA; one diagonal GMM
per category; leave one sound out; N consecutive non-overlapping windows from the start of the
test sound, N in half octave steps; log-likelihoods summed; equal priors. Readings of the claims
file: (6) the window spacing, (a) tau_W, (b) the full Kaiser window length; (7) PCs and N_c, (a)
refitted at each tau_W (PCs explaining 90% of the variance; N_c is the reported count, and the
cross-validated choice of N_c is run at each classifier's optimum), (b) the reported counts (26,
8 and 87 PCs; 8, 5 and 13 components) at every tau_W. Chance is 1/13 = 7.69%.""")

code("""import time, resource
import numpy as np
from scipy import stats, optimize
from joblib import Parallel, delayed
from threadpoolctl import threadpool_limits
import matplotlib.pyplot as plt
import sadeghi as S
import model as M

threadpool_limits(1)  # many small fits run in parallel processes
T_START = time.time()
SEED = {"pca": 11, "loso": 21, "avg": 31, "two": 41, "nc": 51, "fold_pca": 61}  # standard choices
CHANCE = 100 / 13""")

md("""## Loading

The 195 model sounds are read from the tar stream (the first members after the paradigm sounds;
the stream is closed once they are read) and each is passed through the cochlear model.""")

code("""raw = {}
for name, b in S.stream_members(lambda n: "/Sounds/ModelSounds/" in n and n.endswith(".wav")):
    raw[name] = b
    if len(raw) == 195:
        break
KEYS = sorted((n.split("/")[-2], int(n.split("_")[-1][:-4])) for n in raw)
CATS = sorted({k[0] for k in KEYS})
LAB = np.array([CATS.index(k[0]) for k in KEYS])
by_key = {(n.split("/")[-2], int(n.split("_")[-1][:-4])): b for n, b in raw.items()}

def coch(b):
    fs, x = M.read_wav(b)
    return M.cochleogram(x, fs).astype(np.float32), fs, len(x)

out = Parallel(n_jobs=4)(delayed(coch)(by_key[k]) for k in KEYS)
COCH = [o[0] for o in out]
del raw, by_key
print(f"read and filtered {len(COCH)} sounds in {(time.time() - T_START) / 60:.1f} min")""")

code("""print("categories:", len(CATS), "; sounds per category:", np.bincount(LAB).tolist())
print("sampling rates:", sorted({o[1] for o in out}), "; samples per sound:", sorted({o[2] for o in out}))
print("cochleogram shape (channels, ms):", sorted({c.shape for c in COCH}))
print("envelope range over all sounds:", round(float(min(c.min() for c in COCH)), 3), "to", round(float(max(c.max() for c in COCH)), 3),
      "(the sound is normalised to unit SD before filtering)")
F0 = M.features(COCH[0].astype(np.float64), 100)
print("features at tau_W = 100 ms:", {k: v.shape for k, v in F0.items() if hasattr(v, 'shape')}, "; Kaiser length", F0["klen"], "ms")
print("spectral feature range", round(float(F0['spec'].min()), 3), "to", round(float(F0['spec'].max()), 3),
      "; temporal", round(float(F0['temp'].min()), 3), "to", round(float(F0['temp'].max()), 3), "(correlations, within -1 to 1)")
print("resolutions tau_W (ms):", np.round(M.RES_MS, 1))
print("Kaiser window length (ms) at each:", [M.kaiser_for(t / 1000)[0].size for t in M.RES_MS])
del out, F0""", "sanity")

md("""## Classifiers at every resolution

For each tau_W: features of the 195 sounds; PCA of each feature set fitted on the training
observations of all sounds (an assumption: PCA is unsupervised and the held-out sound is 1 of 195;
a variant below refits it in every fold); leave-one-sound-out GMM classifiers under reading (7b)
and, where the PC count for 90% of the variance differs from the reported one, (7a); test windows
under readings (6a) and (6b). The spectrum classifier has no reported counts; it uses the PCs
explaining 90% and 8 components (the spectral count) under both readings.""")

code("""KINDS = ["spec", "temp", "st", "spectrum"]
LL, NPC90, CUM, NWIN, SPACING, REFITTED = {}, {}, {}, {}, {}, {}
t0 = time.time()
for tw in M.RES_MS:
    Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
    ia, ib = M.test_index(Fs[0], tw), M.test_index(Fs[0], Fs[0]["klen"])
    NWIN[tw] = {"a": len(ia), "b": len(ib)}
    SPACING[tw] = {"a": Fs[0]["step"] * int(np.ceil(tw / Fs[0]["step"] - 1e-9)) / 1000,
                   "b": Fs[0]["step"] * int(np.ceil(Fs[0]["klen"] / Fs[0]["step"] - 1e-9)) / 1000}
    for kind in KINDS:
        mean, comps, cum = M.fit_pca(Fs, kind, np.random.default_rng(SEED["pca"]))
        Z = [M.project(F, kind, mean, comps) for F in Fs]
        n90 = int(min(np.searchsorted(cum, 0.9) + 1, len(cum)))
        NPC90[(kind, tw)], CUM[(kind, tw)] = n90, cum
        tests = [{"a": z[ia], "b": z[ib]} for z in Z]
        rep = M.REPORTED.get(kind, (n90, 8))
        runs = {"7b": rep}
        if n90 != rep[0]:
            runs["7a"] = (n90, rep[1])
        for r7, (npc, nc) in runs.items():
            ll, full, refit = M.loso(Z, LAB, npc, nc, tests, SEED["loso"])
            REFITTED[(kind, r7, tw)] = sum(g.refitted_ for g in full + refit)
            for sp in "ab":
                LL[(kind, r7, sp, tw)] = ll[sp]
        if "7a" not in runs:
            for sp in "ab":
                LL[(kind, "7a", sp, tw)] = LL[(kind, "7b", sp, tw)]
        del Z, tests
    del Fs
    print(f"tau_W {tw:6.1f} ms: windows (6a) {NWIN[tw]['a']}, (6b) {NWIN[tw]['b']}; PCs for 90%: "
          + ", ".join(f"{k} {NPC90[(k, tw)]}" for k in KINDS) + f" | {(time.time() - t0) / 60:.1f} min,"
          f" peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB", flush=True)
print("GMM fits refitted with the larger variance floor:", sum(REFITTED.values()), "of", len(REFITTED) * 208)""")

code("""READ = [(r7, sp) for r7 in ("7b", "7a") for sp in "ab"]
ACC = {}  # (kind, r7, sp, tw) -> (195 sounds, durations) 0/1
NS = {}
for (kind, r7, sp, tw), ll in LL.items():
    ns = M.n_steps(NWIN[tw][sp])
    NS[(sp, tw)] = ns
    ACC[(kind, r7, sp, tw)] = M.accuracy_curve(ll, LAB, np.arange(13), ns)
def at10(kind, r7, sp, tw):
    return 100 * ACC[(kind, r7, sp, tw)][:, -1].mean()
print("accuracy (%) at the full sound duration (the largest N), by resolution:")
for r7, sp in READ:
    print(f"reading ({r7})({sp}):")
    for kind in KINDS:
        print(f"   {kind:9s}", " ".join(f"{at10(kind, r7, sp, tw):5.1f}" for tw in M.RES_MS))
print("   tau_W    ", " ".join(f"{tw:5.0f}" for tw in M.RES_MS))
print("full duration (s) of the largest N: (6a)", [round(NS[('a', tw)][-1] * SPACING[tw]['a'], 2) for tw in M.RES_MS])
print("                                    (6b)", [round(NS[('b', tw)][-1] * SPACING[tw]['b'], 2) for tw in M.RES_MS])""")

md("""## fig9a-optimal-resolution

> In the 13-category model task, the spectral and temporal correlation classifiers perform best
> at a window resolution of 141 ms and the spectro-temporal classifier at 100 ms, and all perform
> above chance (7.69%) at every resolution.

Optimum: the resolution with the highest accuracy at the full duration (ties go to the first).
t test of the 195 per-sound outcomes against 7.69%, Bonferroni over the 10 resolutions; the 13
category accuracies are a variant.""")

code("""OPT = {}
for r7, sp in READ:
    for kind in KINDS:
        accs = [at10(kind, r7, sp, tw) for tw in M.RES_MS]
        OPT[(kind, r7, sp)] = M.RES_MS[int(np.argmax(accs))]
    worst = []
    for kind in ("spec", "temp", "st"):
        for tw in M.RES_MS:
            x = 100 * ACC[(kind, r7, sp, tw)][:, -1]
            p = stats.ttest_1samp(x, CHANCE, alternative="greater").pvalue * 10
            cat = np.array([x[LAB == c].mean() for c in range(13)])
            pc = stats.ttest_1samp(cat, CHANCE, alternative="greater").pvalue * 10
            worst.append((min(p, 1), min(pc, 1), x.mean(), kind, tw))
    pmax = max(worst)[0]; pcmax = max(w[1] for w in worst); lo = min(worst, key=lambda w: w[2])
    o = {k: OPT[(k, r7, sp)] for k in KINDS}
    ok = (abs(o["spec"] - 141.4) < 1 and abs(o["temp"] - 141.4) < 1 and abs(o["st"] - 100) < 1)
    step = lambda a, b: abs(np.log2(a / b)) <= 0.5 + 1e-9
    near = step(o["spec"], 141.4) and step(o["temp"], 141.4) and step(o["st"], 100)
    print(f"({r7})({sp}): optimum spectral {o['spec']:.1f}, temporal {o['temp']:.1f}, spectro-temporal {o['st']:.1f}, spectrum {o['spectrum']:.1f} ms"
          f" | on the reported grid points: {ok} | within one grid step: {near}")
    print(f"      lowest correlation-classifier accuracy {lo[2]:.1f}% ({lo[3]} at {lo[4]:.0f} ms); largest Bonferroni p over sounds {pmax:.1e},"
          f" over category means {pcmax:.1e}; every resolution above chance at p < 0.01: {pmax < 0.01}")
fig, ax = plt.subplots(1, 2, figsize=(9, 3))
for a, (r7, sp) in zip(ax, (("7b", "a"), ("7b", "b"))):
    for kind in KINDS:
        a.plot(M.RES_MS, [at10(kind, r7, sp, tw) for tw in M.RES_MS], "o-", label=kind)
    a.axhline(CHANCE, color="k", lw=0.5); a.set_xscale("log"); a.set_xlabel("tau_W (ms)"); a.set_title(f"({r7})({sp}), full duration")
ax[0].set_ylabel("% correct"); ax[0].legend(fontsize=7); plt.tight_layout(); plt.show()
print("plotted range:", round(min(at10(k, '7b', s, tw) for k in KINDS for s in 'ab' for tw in M.RES_MS), 1), "to",
      round(max(at10(k, '7b', s, tw) for k in KINDS for s in 'ab' for tw in M.RES_MS), 1), "%")""", "claim:fig9a-optimal-resolution")

md("""## fig9b-similar-maximum

> At about 10 s the three correlation classifiers reach similar performance (spectro-temporal 84%,
> spectral 83%, temporal 81%), with no significant pairwise differences.

Each classifier at its own optimum (fig9a), full duration; two-sample t tests of the 195
per-sound outcomes for each pair, with the 13 category accuracies as a variant.""")

code("""EXP9B = {"st": (84, 8.4), "spec": (83, 8.3), "temp": (81, 8.1)}
for r7, sp in READ:
    x = {k: 100 * ACC[(k, r7, sp, OPT[(k, r7, sp)])][:, -1] for k in EXP9B}
    hits = sum(abs(x[k].mean() - e) <= t for k, (e, t) in EXP9B.items())
    line = []
    pmin = 1
    for a, b in (("spec", "temp"), ("spec", "st"), ("temp", "st")):
        p = stats.ttest_ind(x[a], x[b]).pvalue
        ca = [x[a][LAB == c].mean() for c in range(13)]; cb = [x[b][LAB == c].mean() for c in range(13)]
        pc = stats.ttest_ind(ca, cb).pvalue
        pmin = min(pmin, p)
        line.append(f"{a}-{b} {x[a].mean() - x[b].mean():+.1f} points, p {p:.2f} (categories p {pc:.2f})")
    print(f"({r7})({sp}): spectro-temporal {x['st'].mean():.1f}, spectral {x['spec'].mean():.1f}, temporal {x['temp'].mean():.1f}%"
          f" | in tolerance {hits}/3 | " + "; ".join(line) + f" | no pair differs at 0.05: {pmin >= 0.05}")""", "claim:fig9b-similar-maximum")

md("""## fig9b-accumulation-rate

> The spectral classifier reaches 90% of its maximum faster than the temporal one (1.7 against
> 3.0 s), and the spectro-temporal classifier fastest (1.2 s).

Rise time to 90% of the accuracy at the full duration, on the curves of fig9b: (a) linear
interpolation between the sampled durations, (b) the first sampled duration reaching it, (c) an
exponential fit P(t) = P_inf - (P_inf - P_0) exp(-t / tau). Duration is N times the window spacing.""")

code("""EXPR = {"spec": (1.7, 0.17), "temp": (3.0, 0.3), "st": (1.2, 0.12)}
def rise(t, y):
    thr = 0.9 * y[-1]
    i = int(np.argmax(y >= thr))
    lin = t[0] if i == 0 else t[i - 1] + (t[i] - t[i - 1]) * (thr - y[i - 1]) / (y[i] - y[i - 1])
    try:
        f = lambda tt, pinf, p0, tau: pinf - (pinf - p0) * np.exp(-tt / tau)
        (pinf, p0, tau), _ = optimize.curve_fit(f, t, y, p0=(y[-1], y[0], 1.0), maxfev=20000)
        tt = np.linspace(0, t[-1], 100001)
        yy = f(tt, pinf, p0, tau)
        ex = float(tt[np.argmax(yy >= 0.9 * f(t[-1], pinf, p0, tau))])
    except RuntimeError:
        ex = np.nan
    return lin, t[i], ex
CURVES = {}
for r7, sp in READ:
    res = {}
    for k in EXPR:
        tw = OPT[(k, r7, sp)]
        t = np.array(NS[(sp, tw)]) * SPACING[tw][sp]
        y = 100 * ACC[(k, r7, sp, tw)].mean(0)
        CURVES[(k, r7, sp)] = (t, y)
        res[k] = rise(t, y)
    for j, lab in enumerate(("(a) interpolated", "(b) first sampled", "(c) exponential fit")):
        v = {k: res[k][j] for k in EXPR}
        hits = sum(abs(v[k] - e) <= tol for k, (e, tol) in EXPR.items())
        order = v["st"] < v["spec"] < v["temp"]
        print(f"({r7})({sp}) {lab}: spectro-temporal {v['st']:.2f}, spectral {v['spec']:.2f}, temporal {v['temp']:.2f} s"
              f" | in tolerance {hits}/3 | order st < spectral < temporal: {order}")
for k in EXPR:
    t, y = CURVES[(k, "7b", "a")]
    print(f"curve (7b)(a) {k} at {OPT[(k, '7b', 'a')]:.0f} ms: " + ", ".join(f"{a:.2f} s {b:.1f}%" for a, b in zip(t, y)))
fig, ax = plt.subplots(figsize=(4.5, 3))
for k in list(EXPR) + ["spectrum"]:
    tw = OPT[(k, "7b", "a")]
    ax.plot(np.array(NS[("a", tw)]) * SPACING[tw]["a"], 100 * ACC[(k, "7b", "a", tw)].mean(0), "o-", ms=3, label=k)
ax.set_xscale("log"); ax.set_xlabel("duration (s)"); ax.set_ylabel("% correct"); ax.legend(fontsize=7); ax.set_title("(7b)(a), each at its optimum")
plt.tight_layout(); plt.show()""", "claim:fig9b-accumulation-rate")

md("""## fig9c-time-averaged-worse

> Ignoring nonstationary structure by averaging the spectro-temporal statistics over time reduces
> category identification performance by about 25%.

At the spectro-temporal optimum, full duration. Reading (a): one time-averaged spectro-temporal
vector per training sound, PCA of the 195 time averages (PCs for 90%, at most 13, as a category
has 14 or 15 training vectors), one diagonal Gaussian per category (N_c = 1, as 14 vectors cannot
fit more), leave one sound out; the test vector is the average over the first N windows.
Reading (b): the short-term category models of the main classifier, and the test feature is the
running average of the short-term correlation over the first N windows, scored as one
observation. Reduction (c) in points, (d) relative to the short-term accuracy.""")

code("""def time_avg_classifier(r7, sp):
    tw = OPT[("st", r7, sp)]
    Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
    idx = M.test_index(Fs[0], tw if sp == "a" else Fs[0]["klen"])
    ns = NS[(sp, tw)]
    npc, nc = M.REPORTED["st"] if r7 == "7b" else (NPC90[("st", tw)], M.REPORTED["st"][1])
    mean, comps, _ = M.fit_pca(Fs, "st", np.random.default_rng(SEED["pca"]))
    Z = [M.project(F, "st", mean, comps) for F in Fs]
    # (b): running averages of the test windows, scored under the short-term models
    tests = [{"run": np.array([z[idx][:n].mean(0) for n in ns])} for z in Z]
    llb, _, _ = M.loso(Z, LAB, npc, nc, tests, SEED["loso"])
    acc_b = np.array([[int(np.argmax(L[i])) == LAB[j] for i in range(len(ns))] for j, L in enumerate(llb["run"])])
    # (a): one time-averaged vector per sound
    X = np.array([M.obs_of(F, "st")[:, 0].mean(0) for F in Fs], np.float64)
    Xw = [np.array([M.obs_of(F, "st", idx)[:n, 0].mean(0) for n in ns]) for F in Fs]
    acc_a = np.zeros((195, len(ns)))
    for j in range(195):
        tr = np.arange(195) != j
        mu = X[tr].mean(0)
        U, s, Vt = np.linalg.svd(X[tr] - mu, full_matrices=False)
        k = min(int(np.searchsorted(np.cumsum(s ** 2) / (s ** 2).sum(), 0.9) + 1), 13)
        P = (X[tr] - mu) @ Vt[:k].T
        Pw = (Xw[j] - mu) @ Vt[:k].T
        ll = np.zeros((len(ns), 13))
        for c in range(13):
            pc = P[LAB[tr] == c]
            m, v = pc.mean(0), pc.var(0) + 1e-6 * P.var(0).max()
            ll[:, c] = -0.5 * (((Pw - m) ** 2) / v + np.log(2 * np.pi * v)).sum(1)
        acc_a[j] = ll.argmax(1) == LAB[j]
    del Fs, Z
    return tw, ns, acc_a, acc_b, k
AVG = {}
for r7, sp in READ:
    if r7 == "7a" and NPC90[("st", OPT[("st", r7, sp)])] == M.REPORTED["st"][0] and OPT[("st", r7, sp)] == OPT[("st", "7b", sp)]:
        AVG[(r7, sp)] = AVG[("7b", sp)]
        continue
    AVG[(r7, sp)] = time_avg_classifier(r7, sp)
for (r7, sp), (tw, ns, acc_a, acc_b, k) in AVG.items():
    st = at10("st", r7, sp, tw)
    for lab, acc in (("(a) time-averaged models", acc_a), ("(b) running average", acc_b)):
        v = 100 * acc[:, -1].mean()
        d_pts, d_rel = st - v, 100 * (st - v) / st
        print(f"({r7})({sp}) {lab} at {tw:.0f} ms: {v:.1f}% against short-term {st:.1f}% | reduction (c) {d_pts:.1f} points"
              f" (in 25 +/- 2.5: {abs(d_pts - 25) <= 2.5}), (d) {d_rel:.1f}% (in tolerance: {abs(d_rel - 25) <= 2.5}) | at least 10 points lower: {d_pts >= 10}")
    print(f"      (a) curve: " + ", ".join(f"N={n} {100 * m:.1f}%" for n, m in zip(ns, acc_a.mean(0))) + f"; PCs of the time averages (last fold) {k}")""", "claim:fig9c-time-averaged-worse")

md("""## fig9e-category-specific

> Some categories are identified much better by one feature set; waves by spectral correlations
> (100% against 33%) and wind by temporal ones (47% against 80%).

Per-category accuracy over its 15 sounds, each classifier at its optimum, full duration.""")

code("""EXP9E = [("Wave", "spec", 100, 10), ("Wave", "temp", 33, 6.7), ("Wind", "spec", 47, 6.7), ("Wind", "temp", 80, 8)]
for r7, sp in READ:
    pc = {k: [100 * ACC[(k, r7, sp, OPT[(k, r7, sp)])][LAB == c, -1].mean() for c in range(13)] for k in ("spec", "temp", "st")}
    v = [pc[k][CATS.index(c)] for c, k, _, _ in EXP9E]
    hits = sum(abs(x - e) <= t + 1e-9 for x, (_, _, e, t) in zip(v, EXP9E))
    part = (v[0] - v[1] >= 13.3 - 1e-9) and (v[3] - v[2] >= 13.3 - 1e-9)
    print(f"({r7})({sp}): waves spectral {v[0]:.1f}, temporal {v[1]:.1f}; wind spectral {v[2]:.1f}, temporal {v[3]:.1f}%"
          f" | in tolerance {hits}/4 | waves better spectral and wind better temporal by two sounds or more: {part}")
    print("      per category spectral/temporal/st: " + ", ".join(f"{c} {pc['spec'][i]:.0f}/{pc['temp'][i]:.0f}/{pc['st'][i]:.0f}" for i, c in enumerate(CATS)))""", "claim:fig9e-category-specific")

md("""## fig9-spectrum-classifier-lower

> The spectrum-based classifier does not depend on temporal resolution and performs below all
> three correlation classifiers.

Range of the spectrum classifier's full-duration accuracy over the ten resolutions (under 10
points for "does not depend"), and at every duration of each correlation classifier's curve (at
its optimum) the spectrum classifier at its own optimum, taken at the longest of its durations
not exceeding that duration.""")

code("""for r7, sp in READ:
    v = [at10("spectrum", r7, sp, tw) for tw in M.RES_MS]
    tws = OPT[("spectrum", r7, sp)]
    ts = np.array(NS[(sp, tws)]) * SPACING[tws][sp]
    ys = 100 * ACC[("spectrum", r7, sp, tws)].mean(0)
    below, below10 = {}, {}
    for k in ("spec", "temp", "st"):
        tw = OPT[(k, r7, sp)]
        t = np.array(NS[(sp, tw)]) * SPACING[tw][sp]
        y = 100 * ACC[(k, r7, sp, tw)].mean(0)
        yspec = np.array([ys[max(0, np.searchsorted(ts, x + 1e-9) - 1)] for x in t])
        below[k] = (int((yspec < y).sum()), len(t), float((y - yspec).min()))
        below10[k] = ys[-1] < y[-1]
    allb = all(b[0] == b[1] for b in below.values())
    print(f"({r7})({sp}): spectrum classifier at full duration {min(v):.1f} to {max(v):.1f}% over resolutions (range {max(v) - min(v):.1f} points,"
          f" under 10: {max(v) - min(v) < 10}); optimum {tws:.0f} ms, {ys[-1]:.1f}%")
    print("      durations where it is below: " + ", ".join(f"{k} {b[0]}/{b[1]} (smallest margin {b[2]:+.1f})" for k, b in below.items())
          + f" | below at every duration: {allb} | below all three at full duration: {all(below10.values())}")""", "claim:fig9-spectrum-classifier-lower")

md("""## fig10-vocalization-background

> In a vocalization against background task, the spectro-temporal classifier approaches 90% for
> background and nearly 100% for vocalizations; vocalization accuracy improves with duration while
> background accuracy stays constant, and vocalizations are classified better with spectral than
> temporal correlations.

Vocalizations: single bird songs, cat meowing, dog barking, human speech (60 sounds); background:
the other nine categories (135). Readings (a) one GMM per class fitted on its pooled sounds (same
PCs and N_c as the 13-category classifier, leave one sound out), (b) the 13-category decision
mapped to its class. Each classifier at its 13-category optimum. Spectral against temporal on the
vocalizations: paired t test over the 60 sounds at each duration, Bonferroni over durations (the
two-sample test is shown too). The temporal minus spectro-temporal difference is read (c) at the
full duration and (d) as the mean over durations.""")

code("""VOC = [CATS.index(c) for c in ("Single_Bird_Songs", "Cat_Meowing", "Dog_Barking", "Human_Speech")]
CLS = np.isin(LAB, VOC).astype(int)  # 1 vocalization, 0 background
def two_class(r7, sp):
    res = {}
    for k in ("spec", "temp", "st"):
        tw = OPT[(k, r7, sp)]
        ns = NS[(sp, tw)]
        accb = np.array([[CLS[j] == int(np.isin(np.argmax(np.cumsum(L, 0)[n - 1]), VOC)) for n in ns] for j, L in enumerate(LL[(k, r7, sp, tw)])])
        Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
        idx = M.test_index(Fs[0], tw if sp == "a" else Fs[0]["klen"])
        npc, nc = M.REPORTED[k] if r7 == "7b" else (NPC90[(k, tw)], M.REPORTED[k][1])
        mean, comps, _ = M.fit_pca(Fs, k, np.random.default_rng(SEED["pca"]))
        Z = [M.project(F, k, mean, comps) for F in Fs]
        del Fs
        ll, _, _ = M.loso(Z, CLS, npc, nc, [{"w": z[idx]} for z in Z], SEED["two"])
        acca = M.accuracy_curve(ll["w"], CLS, np.arange(2), ns)
        res[k] = {"a": acca, "b": accb, "t": np.array(ns) * SPACING[tw][sp]}
        del Z
    return res
TWO = {}
for r7, sp in (("7b", "a"), ("7b", "b")):
    TWO[(r7, sp)] = two_class(r7, sp)
for (r7, sp), res in TWO.items():
    for rd in ("a", "b"):
        st = res["st"][rd]
        voc, bg = 100 * st[CLS == 1].mean(0), 100 * st[CLS == 0].mean(0)
        ok_v = abs(voc[-1] - 100) <= 10 and abs(bg[-1] - 90) <= 9
        rises = voc[-1] > voc[0]
        flat = bg.max() - bg.min() < 10
        n = st.shape[1]
        sv, tv = res["spec"][rd][CLS == 1], res["temp"][rd][CLS == 1]
        m = min(sv.shape[1], tv.shape[1])
        pp = [stats.ttest_rel(sv[:, i], tv[:, i]).pvalue * m if (sv[:, i] != tv[:, i]).any() else 1.0 for i in range(m)]
        p2 = [stats.ttest_ind(sv[:, i], tv[:, i]).pvalue * m for i in range(m)]
        better = [sv[:, i].mean() > tv[:, i].mean() for i in range(m)]
        sig = [better[i] and pp[i] < 0.01 for i in range(m)]
        tm = 100 * res["temp"][rd][CLS == 1].mean(0)
        k_ = min(len(tm), len(voc))
        diff_c, diff_d = tm[-1] - voc[-1], float(np.mean(tm[:k_] - voc[:k_]))
        print(f"({r7})({sp}) reading ({rd}): spectro-temporal at full duration background {bg[-1]:.1f}%, vocalizations {voc[-1]:.1f}% (both in tolerance: {ok_v})"
              f" | vocalizations rise from {voc[0]:.1f}%: {rises} | background range {bg.min():.1f} to {bg.max():.1f} (under 10 points: {flat})")
        print(f"      vocalizations, spectral {100 * sv[:, -1].mean():.1f} against temporal {100 * tv[:, -1].mean():.1f}% at full duration; spectral higher and"
              f" Bonferroni paired p < 0.01 at {sum(sig)} of {m} durations (smallest p {min(pp):.1e}; two-sample smallest {min(p2):.1e})"
              f" | temporal minus spectro-temporal (c) {diff_c:+.1f}, (d) {diff_d:+.1f} points (in -20 +/- 2: {abs(diff_c + 20) <= 2}, {abs(diff_d + 20) <= 2})")
        for k in ("spec", "temp", "st"):
            print(f"      {k:5s} vocalizations " + " ".join(f"{100 * x:.0f}" for x in res[k][rd][CLS == 1].mean(0))
                  + " | background " + " ".join(f"{100 * x:.0f}" for x in res[k][rd][CLS == 0].mean(0)))""", "claim:fig10-vocalization-background")

md("""## Variants: N_c by cross-validated likelihood, and PCA refitted in every fold

Reading (7a) also chooses N_c by cross-validated likelihood (Methods, N_c = 1 to 20). At each
classifier's (7b)(a) optimum: for each N_c, 3-fold cross-validation over the sounds of each
category (5 sounds held out each time), mean held-out log-likelihood per observation summed over
the 13 categories. Then the spectral classifier at its optimum with the PCA refitted within
every fold, to show what fitting it on all sounds does.""")

code("""t1 = time.time()
NC_GRID = list(range(1, 21))
for k in ("spec", "temp", "st"):
    tw = OPT[(k, "7b", "a")]
    Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
    mean, comps, _ = M.fit_pca(Fs, k, np.random.default_rng(SEED["pca"]))
    Z = [M.project(F, k, mean, comps) for F in Fs]
    npc = M.REPORTED[k][0]
    del Fs
    rng = np.random.default_rng(SEED["nc"])
    def cv_ll(nc):
        tot = 0.0
        for c in range(13):
            idx = np.flatnonzero(LAB == c)
            for f in range(3):
                te = idx[f::3]; tr = np.setdiff1d(idx, te)
                gm = M.fit_gmm(M.train_rows([Z[i] for i in tr], npc, np.random.default_rng(c * 10 + f), cap=5000), nc)
                X = np.concatenate([Z[i][:, :, :npc].reshape(-1, npc) for i in te])
                X = X[np.random.default_rng(c * 10 + f + 1).choice(len(X), min(len(X), 5000), replace=False)]
                tot += gm.score(X.astype(np.float64)) / 39
        return tot
    cv = Parallel(n_jobs=4)(delayed(cv_ll)(nc) for nc in NC_GRID)
    best = NC_GRID[int(np.argmax(cv))]
    print(f"{k} at {tw:.0f} ms, {npc} PCs: cross-validated N_c {best} (reported {M.REPORTED[k][1]}); held-out log-likelihood per observation "
          + ", ".join(f"{nc}: {v:.2f}" for nc, v in zip(NC_GRID, cv) if nc in (1, 2, 3, 5, 8, 13, 20)), flush=True)
    if k == "spec":
        # PCA refitted without the held-out sound, all 13 category models refitted in every fold
        Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
        idx = M.test_index(Fs[0], tw)
        def fold(j):
            tr = [F for i, F in enumerate(Fs) if i != j]
            mu, co, _ = M.fit_pca(tr, "spec", np.random.default_rng(SEED["fold_pca"] + j))
            Zt = [M.project(F, "spec", mu, co) for F in Fs]
            ll = np.array([M.window_ll(M.fit_gmm(M.train_rows([Zt[i] for i in np.flatnonzero(LAB == c) if i != j], npc,
                                                                np.random.default_rng(j * 13 + c)), M.REPORTED["spec"][1]),
                                       Zt[j][idx], npc) for c in range(13)]).T
            return np.cumsum(ll, 0)[-1].argmax() == LAB[j]
        hit = Parallel(n_jobs=4)(delayed(fold)(j) for j in range(195))
        print(f"spectral at {tw:.0f} ms, (7b)(a), PCA refitted in every fold: {100 * np.mean(hit):.1f}% at full duration, against {at10('spec', '7b', 'a', tw):.1f}% with one PCA")
        del Fs
    del Z
print(f"variants took {(time.time() - t1) / 60:.1f} min")""")

md("""## Summary

(filled in after the run)""")

code("""print(f"total run time {(time.time() - T_START) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")""")
nb.cells = C
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, sys.argv[1])
PYEOF
cd entries/sadeghi-2019; executed/sadeghi-2019/.venv/bin/python $TMPDIR/dev/build_clf.py reproduce_sadeghi_2019_classifier.ipynb && echo ok; date -u
```

```
ok
Sat Nov 14 03:33:21 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import json, os
D=os.environ['TMPDIR']+'/dev'
nb=json.load(open('reproduce_sadeghi_2019_classifier.ipynb'))
c=nb['cells'][3]
c['source']="""import pickle
_c = pickle.load(open('%s/coch.pkl','rb'))
KEYS = sorted(_c); CATS = sorted({k[0] for k in KEYS}); LAB = np.array([CATS.index(k[0]) for k in KEYS])
COCH = [_c[k] for k in KEYS]; out = [(None, 44100, 441000)] * 195
M.RES_MS = M.RES_MS[[3, 4, 5]]
""" % D
json.dump(nb, open(D+'/clf_dev.ipynb','w'))
print(json.load(open('reproduce_sadeghi_2019_model.ipynb'))['metadata'])
EOF
cd $TMPDIR/dev; cp entries/sadeghi-2019/*.py .; time $PY -m jupyter nbconvert --to notebook --execute clf_dev.ipynb --output clf_dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5; date -u
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
[32m-> [39m[32m7035[39m     return ttest_1samp(a - b, popmean=0., axis=axis, alternative=alternative,
[32m   7036[39m                        _no_deco=[38;5;28;01mTrue[39;00m)

[31mTypeError[39m: numpy boolean subtract, the `-` operator, is not supported, use the bitwise_xor, the `^` operator, or the logical_xor function instead.


real	22m14.366s
user	65m27.251s
sys	5m16.407s
Sat Nov 14 03:55:45 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import json
nb=json.load(open('clf_dev_out.ipynb')) if __import__('os').path.exists('clf_dev_out.ipynb') else None
print(nb is None)
EOF
ls $TMPDIR/dev
```

```
True
__pycache__
build_clf.py
clf_dev.ipynb
coch.pkl
code.pkl
model.py
names.pkl
sadeghi.py
snd.pkl
t1.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
s=open('model.py').read()
old_start=s.index('def train_rows(')
old_end=s.index('def window_ll(')
s=s[:old_start]+'''def train_rows(Zs, npc, rng, cap=TRAIN_CAP):
    """Training observations of the sounds Zs, at most cap, drawn at random in equal numbers from
    each sound (standard choice, for speed)."""
    per = int(np.ceil(cap / len(Zs)))
    out = []
    for z in Zs:
        X = z[:, :, :npc].reshape(-1, npc)
        out.append(X if len(X) <= per else X[rng.choice(len(X), per, replace=False)])
    return np.concatenate(out)


'''+s[old_end:]
a=s.index('def loso(')
b=s.index('def accuracy_curve(')
s=s[:a]+'''def loso(Z, labels, npc, nc, tests, seed, n_jobs=4):
    """Leave one sound out (Cross validation). Z: per-sound observations (n, m, d); labels: class
    of each sound; tests: per-sound dict {name: window arrays (n_w, m, d)} to score. A fold
    changes only the held-out sound's class model, so each class is fitted once on all its
    sounds and refitted once per held-out sound. Returns {name: per-sound (n_w, classes) LL}
    and the fitted models (full per class, refit per sound)."""
    from joblib import Parallel, delayed
    labels = np.asarray(labels)
    classes = np.unique(labels)
    seeds = np.random.SeedSequence(seed).generate_state(len(Z) + len(classes))

    def rows(c, leave, s):
        idx = [i for i in np.flatnonzero(labels == c) if i != leave]
        return train_rows([Z[i] for i in idx], npc, np.random.default_rng(s))

    jobs = [(c, -1, seeds[len(Z) + k]) for k, c in enumerate(classes)] + [(labels[j], j, seeds[j]) for j in range(len(Z))]
    fits = Parallel(n_jobs=n_jobs)(delayed(fit_gmm)(rows(c, j, s), nc) for c, j, s in jobs)
    full, refit = fits[:len(classes)], fits[len(classes):]
    out = {}
    for name in tests[0]:
        LL = []
        for j in range(len(Z)):
            Zw = tests[j][name]
            LL.append(np.array([window_ll(refit[j] if c == labels[j] else full[k], Zw, npc) for k, c in enumerate(classes)]).T)
        out[name] = LL
    return out, full, refit


'''+s[b:]
open('model.py','w').write(s)
EOF
grep -n "def " model.py | tail -12
```

```
214:def features(S, tau_w_ms):
233:def test_index(F, spacing_ms):
240:def n_steps(nmax):
246:def obs_of(F, kind, idx=None):
260:def fit_pca(Fs, kind, rng, nfit=15000, kmax=150):
278:def project(F, kind, mean, comps):
284:def fit_gmm(X, nc, seed=0):
298:def train_rows(Zs, npc, rng, cap=TRAIN_CAP):
309:def window_ll(gm, Zw, npc):
315:def loso(Z, labels, npc, nc, tests, seed, n_jobs=4):
326:    def rows(c, leave, s):
343:def accuracy_curve(LL, labels, classes, ns):
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
s=open('build_clf.py').read()
# main loop: keep projected scores
s=s.replace('''KINDS = ["spec", "temp", "st", "spectrum"]
LL, NPC90, CUM, NWIN, SPACING, REFITTED = {}, {}, {}, {}, {}, {}''','''KINDS = ["spec", "temp", "st", "spectrum"]
LL, NPC90, CUM, NWIN, SPACING, REFITTED, ZS, TIDX = {}, {}, {}, {}, {}, {}, {}, {}''')
s=s.replace('''    NWIN[tw] = {"a": len(ia), "b": len(ib)}''','''    NWIN[tw] = {"a": len(ia), "b": len(ib)}
    TIDX[tw] = {"a": ia, "b": ib}''')
s=s.replace('''        if "7a" not in runs:
            for sp in "ab":
                LL[(kind, "7a", sp, tw)] = LL[(kind, "7b", sp, tw)]
        del Z, tests''','''        if "7a" not in runs:
            for sp in "ab":
                LL[(kind, "7a", sp, tw)] = LL[(kind, "7b", sp, tw)]
        kk = max(v[0] for v in runs.values())
        ZS[(kind, tw)] = [np.ascontiguousarray(z[:, :, :kk]) for z in Z]  # kept for fig9c and fig10
        del Z, tests''')
# time-avg classifier rewrite
a=s.index('code("""def time_avg_classifier')
b=s.index('"claim:fig9c-time-averaged-worse")')
s=s[:a]+'''code("""def time_avg_classifier(r7, sp):
    tw = OPT[("st", r7, sp)]
    idx = TIDX[tw][sp]
    ns = NS[(sp, tw)]
    npc, nc = M.REPORTED["st"] if r7 == "7b" else (NPC90[("st", tw)], M.REPORTED["st"][1])
    Z = ZS[("st", tw)]
    # (b): running averages of the test windows, scored under the short-term models
    tests = [{"run": np.array([z[idx][:n].mean(0) for n in ns])} for z in Z]
    llb, _, _ = M.loso(Z, LAB, npc, nc, tests, SEED["loso"])
    acc_b = np.array([[int(np.argmax(L[i])) == LAB[j] for i in range(len(ns))] for j, L in enumerate(llb["run"])], float)
    # (a): one time-averaged vector per sound (the mean of its short-term PC scores, which is the
    # projection of its time-averaged correlation), one diagonal Gaussian per category
    X = np.array([z[:, 0, :npc].mean(0) for z in Z], np.float64)
    Xw = [np.array([z[idx][:n, 0, :npc].mean(0) for n in ns], np.float64) for z in Z]
    acc_a = np.zeros((195, len(ns)))
    for j in range(195):
        tr = np.arange(195) != j
        ll = np.zeros((len(ns), 13))
        for c in range(13):
            pc = X[tr & (LAB == c)]
            m, v = pc.mean(0), pc.var(0) + 1e-6 * X[tr].var(0).max()
            ll[:, c] = -0.5 * (((Xw[j] - m) ** 2) / v + np.log(2 * np.pi * v)).sum(1)
        acc_a[j] = ll.argmax(1) == LAB[j]
    return tw, ns, acc_a, acc_b, npc
AVG = {}
for r7, sp in READ:
    AVG[(r7, sp)] = time_avg_classifier(r7, sp)
for (r7, sp), (tw, ns, acc_a, acc_b, k) in AVG.items():
    st = at10("st", r7, sp, tw)
    for lab, acc in (("(a) time-averaged models", acc_a), ("(b) running average", acc_b)):
        v = 100 * acc[:, -1].mean()
        d_pts, d_rel = st - v, 100 * (st - v) / st
        print(f"({r7})({sp}) {lab} at {tw:.0f} ms, {k} PCs: {v:.1f}% against short-term {st:.1f}% | reduction (c) {d_pts:.1f} points"
              f" (in 25 +/- 2.5: {abs(d_pts - 25) <= 2.5}), (d) {d_rel:.1f}% (in tolerance: {abs(d_rel - 25) <= 2.5}) | at least 10 points lower: {d_pts >= 10}")
    print(f"      curves (a): " + ", ".join(f"N={n} {100 * m:.1f}" for n, m in zip(ns, acc_a.mean(0)))
          + " | (b): " + ", ".join(f"N={n} {100 * m:.1f}" for n, m in zip(ns, acc_b.mean(0))))""", '''+s[b:]
s=s.replace('''Reading (a): one time-averaged spectro-temporal
vector per training sound, PCA of the 195 time averages (PCs for 90%, at most 13, as a category
has 14 or 15 training vectors), one diagonal Gaussian per category (N_c = 1, as 14 vectors cannot
fit more), leave one sound out; the test vector is the average over the first N windows.''','''Reading (a): one time-averaged spectro-temporal
vector per training sound (the mean of its short-term PC scores, the same PCs as the short-term
classifier; PCA is linear, so this is the projection of the time-averaged correlation), one
diagonal Gaussian per category (N_c = 1, as a category has only 14 or 15 such vectors), leave one
sound out; the test vector is the average over the first N windows.''')
# fig10 rewrite of feature part
s=s.replace('''        accb = np.array([[CLS[j] == int(np.isin(np.argmax(np.cumsum(L, 0)[n - 1]), VOC)) for n in ns] for j, L in enumerate(LL[(k, r7, sp, tw)])])
        Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
        idx = M.test_index(Fs[0], tw if sp == "a" else Fs[0]["klen"])
        npc, nc = M.REPORTED[k] if r7 == "7b" else (NPC90[(k, tw)], M.REPORTED[k][1])
        mean, comps, _ = M.fit_pca(Fs, k, np.random.default_rng(SEED["pca"]))
        Z = [M.project(F, k, mean, comps) for F in Fs]
        del Fs
        ll, _, _ = M.loso(Z, CLS, npc, nc, [{"w": z[idx]} for z in Z], SEED["two"])
        acca = M.accuracy_curve(ll["w"], CLS, np.arange(2), ns)
        res[k] = {"a": acca, "b": accb, "t": np.array(ns) * SPACING[tw][sp]}
        del Z''','''        accb = np.array([[CLS[j] == int(np.isin(np.argmax(np.cumsum(L, 0)[n - 1]), VOC)) for n in ns] for j, L in enumerate(LL[(k, r7, sp, tw)])], float)
        idx = TIDX[tw][sp]
        npc, nc = M.REPORTED[k] if r7 == "7b" else (NPC90[(k, tw)], M.REPORTED[k][1])
        Z = ZS[(k, tw)]
        ll, _, _ = M.loso(Z, CLS, npc, nc, [{"w": z[idx]} for z in Z], SEED["two"])
        acca = M.accuracy_curve(ll["w"], CLS, np.arange(2), ns)
        res[k] = {"a": acca, "b": accb, "t": np.array(ns) * SPACING[tw][sp]}''')
# variants rewrite
a=s.index('code("""t1 = time.time()\nNC_GRID')
b=s.index('md("""## Summary')
s=s[:a]+'''code("""t1 = time.time()
NC_GRID = [1, 2, 3, 5, 8, 13, 20]
for k in ("spec", "temp", "st"):
    tw = OPT[(k, "7b", "a")]
    Z = ZS[(k, tw)]
    npc = M.REPORTED[k][0]
    def cv_ll(nc):
        tot = 0.0
        for c in range(13):
            idx = np.flatnonzero(LAB == c)
            for f in range(3):
                te = idx[f::3]; tr = np.setdiff1d(idx, te)
                gm = M.fit_gmm(M.train_rows([Z[i] for i in tr], npc, np.random.default_rng(SEED["nc"] + c * 10 + f), cap=5000), nc)
                X = M.train_rows([Z[i] for i in te], npc, np.random.default_rng(SEED["nc"] + c * 10 + f + 1), cap=5000)
                tot += gm.score(X.astype(np.float64)) / 39
        return tot
    cv = Parallel(n_jobs=4)(delayed(cv_ll)(nc) for nc in NC_GRID)
    best = NC_GRID[int(np.argmax(cv))]
    print(f"{k} at {tw:.0f} ms, {npc} PCs: cross-validated N_c {best} (reported {M.REPORTED[k][1]}); mean held-out log-likelihood per observation: "
          + ", ".join(f"{nc}: {v:.2f}" for nc, v in zip(NC_GRID, cv)), flush=True)
# PCA refitted without the held-out sound, all 13 category models refitted, for two sounds per category
tw = OPT[("spec", "7b", "a")]
Fs = Parallel(n_jobs=4)(delayed(M.features)(c.astype(np.float64), tw) for c in COCH)
idx = TIDX[tw]["a"]
npc, nc = M.REPORTED["spec"]
def fold(j):
    tr = [F for i, F in enumerate(Fs) if i != j]
    mu, co, _ = M.fit_pca(tr, "spec", np.random.default_rng(SEED["fold_pca"] + j))
    Zt = [M.project(F, "spec", mu, co) for F in Fs]
    ll = np.array([M.window_ll(M.fit_gmm(M.train_rows([Zt[i] for i in np.flatnonzero(LAB == c) if i != j], npc,
                                                        np.random.default_rng(j * 13 + c)), nc), Zt[j][idx], npc) for c in range(13)]).T
    return bool(np.cumsum(ll, 0)[-1].argmax() == LAB[j])
FOLDS = [int(i) for c in range(13) for i in np.flatnonzero(LAB == c)[:2]]
hit = Parallel(n_jobs=4)(delayed(fold)(j) for j in FOLDS)
one = ACC[("spec", "7b", "a", tw)][FOLDS, -1]
print(f"spectral at {tw:.0f} ms, (7b)(a), the first two sounds of each category ({len(FOLDS)} folds): PCA refitted in each fold {100 * np.mean(hit):.1f}%,"
      f" one PCA on all sounds {100 * one.mean():.1f}%; the two agree on {int((np.array(hit) == one.astype(bool)).sum())} of {len(FOLDS)} sounds")
del Fs
print(f"variants took {(time.time() - t1) / 60:.1f} min")""")

'''+s[b:]
s=s.replace('''## Variants: N_c by cross-validated likelihood, and PCA refitted in every fold

Reading (7a) also chooses N_c by cross-validated likelihood (Methods, N_c = 1 to 20). At each
classifier's (7b)(a) optimum: for each N_c, 3-fold cross-validation over the sounds of each
category (5 sounds held out each time), mean held-out log-likelihood per observation summed over
the 13 categories. Then the spectral classifier at its optimum with the PCA refitted within
every fold, to show what fitting it on all sounds does.''','''## Variants: N_c by cross-validated likelihood, and PCA refitted in every fold

Reading (7a) also chooses N_c by cross-validated likelihood (Methods, N_c = 1 to 20). At each
classifier's (7b)(a) optimum, for N_c of 1, 2, 3, 5, 8, 13 and 20 (a subset of the Methods' 1 to
20, for time): 3-fold cross-validation over the sounds of each category (5 sounds held out each
time), the mean held-out log-likelihood per observation averaged over the 13 categories and
folds. Then the spectral classifier at its optimum with the PCA refitted without the held-out
sound, for the first two sounds of each category, to show what fitting it once on all sounds
does.''')
open('build_clf.py','w').write(s)
EOF
grep -n "time_avg_classifier\|ZS\[" build_clf.py | head
```

```
139:        ZS[(kind, tw)] = [np.ascontiguousarray(z[:, :, :kk]) for z in Z]  # kept for fig9c and fig10
291:code("""def time_avg_classifier(r7, sp):
296:    Z = ZS[("st", tw)]
317:    AVG[(r7, sp)] = time_avg_classifier(r7, sp)
399:        Z = ZS[(k, tw)]
447:    Z = ZS[(k, tw)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
s=open('build_clf.py').read()
s=s.replace('''for r7, sp in READ:
    AVG[(r7, sp)] = time_avg_classifier(r7, sp)''','''for r7, sp in READ:
    tw = OPT[("st", r7, sp)]
    if r7 == "7a" and OPT[("st", "7b", sp)] == tw and NPC90[("st", tw)] == M.REPORTED["st"][0]:
        AVG[(r7, sp)] = AVG[("7b", sp)]  # the same classifier
    else:
        AVG[(r7, sp)] = time_avg_classifier(r7, sp)''')
open('build_clf.py','w').write(s)
EOF
cd entries/sadeghi-2019; $PY $TMPDIR/dev/build_clf.py reproduce_sadeghi_2019_classifier.ipynb; cp model.py sadeghi.py $TMPDIR/dev/; $PY - <<'EOF'
import json, os
D=os.environ['TMPDIR']+'/dev'
nb=json.load(open('reproduce_sadeghi_2019_classifier.ipynb'))
nb['cells'][3]['source']="""import pickle
_c = pickle.load(open('%s/coch.pkl','rb'))
KEYS = sorted(_c); CATS = sorted({k[0] for k in KEYS}); LAB = np.array([CATS.index(k[0]) for k in KEYS])
COCH = [_c[k] for k in KEYS]; out = [(None, 44100, 441000)] * 195
M.RES_MS = M.RES_MS[[0, 5]]
""" % D
for c in nb['cells']:
    if c['cell_type']=='code': c['source']="_tc=time.time()\n"+c['source']+"\nprint('CELL', round(time.time()-_tc), 's')" if 'import time' not in c['source'] else c['source']
json.dump(nb, open(D+'/clf_dev.ipynb','w'))
EOF
cd $TMPDIR/dev; time $PY -m jupyter nbconvert --to notebook --execute --allow-errors clf_dev.ipynb --output clf_dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -2; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
TypeError: can only concatenate str (not "list") to str
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 144670 bytes to clf_dev_out.ipynb

real	28m26.763s
user	96m51.201s
sys	1m52.877s
Sat Nov 14 04:25:40 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import json
nb=json.load(open('clf_dev_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        out=''.join(''.join(o.get('text','')) if 'text' in o else (o.get('ename','')+str(o.get('evalue',''))) for o in c.get('outputs',[]))
        print('---',i,out[:3000])
EOF
```

```
--- 1 
--- 3 
--- 4 categories: 13 ; sounds per category: [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
sampling rates: [44100] ; samples per sound: [441000]
cochleogram shape (channels, ms): [(58, 10000)]
envelope range over all sounds: 0.0 to 26.193 (the sound is normalised to unit SD before filtering)
features at tau_W = 100 ms: {'spec': (386, 1653), 'temp': (386, 58, 50), 'spectrum': (386, 58), 'centres': (386,)} ; Kaiser length 269 ms
spectral feature range -0.268 to 0.997 ; temporal -0.541 to 0.98 (correlations, within -1 to 1)
resolutions tau_W (ms): [ 70.7 100.  141.4]
Kaiser window length (ms) at each: [191, 269, 381]

--- 6 tau_W   70.7 ms: windows (6a) 136, (6b) 50; PCs for 90%: spec 42, temp 8, st 103, spectrum 7 | 2.5 min, peak memory 3.5 GB
tau_W  100.0 ms: windows (6a) 97, (6b) 36; PCs for 90%: spec 34, temp 8, st 90, spectrum 6 | 4.6 min, peak memory 3.6 GB
tau_W  141.4 ms: windows (6a) 55, (6b) 25; PCs for 90%: spec 26, temp 8, st 73, spectrum 6 | 6.2 min, peak memory 3.9 GB
GMM fits refitted with the larger variance floor: 0 of 3536

--- 7 accuracy (%) at the full sound duration (the largest N), by resolution:
reading (7b)(a):
   spec       79.0  79.0  80.5
   temp       75.4  75.9  80.0
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY $TMPDIR/dev/build_clf.py reproduce_sadeghi_2019_classifier.ipynb; cp model.py sadeghi.py $TMPDIR/dev/; $PY - <<'EOF'
import json, os
D=os.environ['TMPDIR']+'/dev'
nb=json.load(open('reproduce_sadeghi_2019_classifier.ipynb'))
nb['cells'][3]['source']="""import pickle
_c = pickle.load(open('%s/coch.pkl','rb'))
KEYS = sorted(_c); CATS = sorted({k[0] for k in KEYS}); LAB = np.array([CATS.index(k[0]) for k in KEYS])
COCH = [_c[k] for k in KEYS]; out = [(None, 44100, 441000)] * 195
M.RES_MS = M.RES_MS[[5]]
""" % D
for c in nb['cells']:
    if c['cell_type']=='code':
        src=''.join(c['source']) if isinstance(c['source'],list) else c['source']
        if 'import time' not in src: c['source']="_tc=time.time()\n"+src+"\nprint('CELL', round(time.time()-_tc), 's')"
json.dump(nb, open(D+'/clf_dev.ipynb','w'))
EOF
cd $TMPDIR/dev; time $PY -m jupyter nbconvert --to notebook --execute --allow-errors clf_dev.ipynb --output clf_dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -1; $PY - <<'EOF'
import json
nb=json.load(open('clf_dev_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        out=''.join(''.join(o.get('text','')) if 'text' in o else (o.get('ename','')+str(o.get('evalue',''))) for o in c.get('outputs',[]))
        print('---',i,out[-1500:])
EOF
date -u
```

```
[NbConvertApp] Writing 131926 bytes to clf_dev_out.ipynb

real	6m7.779s
user	21m13.395s
sys	0m27.879s
--- 1 
--- 3 CELL 0 s

--- 4 categories: 13 ; sounds per category: [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
sampling rates: [44100] ; samples per sound: [441000]
cochleogram shape (channels, ms): [(58, 10000)]
envelope range over all sounds: 0.0 to 26.193 (the sound is normalised to unit SD before filtering)
features at tau_W = 100 ms: {'spec': (386, 1653), 'temp': (386, 58, 50), 'spectrum': (386, 58), 'centres': (386,)} ; Kaiser length 269 ms
spectral feature range -0.268 to 0.997 ; temporal -0.541 to 0.98 (correlations, within -1 to 1)
resolutions tau_W (ms): [141.4]
Kaiser window length (ms) at each: [381]
CELL 1 s

--- 6 tau_W  141.4 ms: windows (6a) 55, (6b) 25; PCs for 90%: spec 26, temp 8, st 73, spectrum 6 | 1.7 min, peak memory 3.8 GB
GMM fits refitted with the larger variance floor: 0 of 1040
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; grep -n "WINDOW_READINGS\|def correlation_readings\|def describe\|def site_correlations" -A14 sadeghi.py | head -90; grep -n "S10 Fig\|split-half\|split half" ../../paper/10.1371-journal.pbio.3000449.txt | cut -c1-1500 | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; sed -n 213,225p sadeghi.py; grep -n "S10 Fig" ../../paper/10.1371-journal.pbio.3000449.txt | head -3; grep -n "measured between the first and second half" ../../paper/10.1371-journal.pbio.3000449.txt | head -2 | cut -c1-200; sed -n 553,600p sadeghi.py; grep -n "first half\|second half" ../../paper/10.1371-journal.pbio.3000449.txt | cut -c1-100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; sed -n 497p ../../paper/10.1371-journal.pbio.3000449.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import json
nb=json.load(open('reproduce_sadeghi_2019_neural.ipynb'))
for i in (1,3,5,6,10,30,58):
    print('---',i); print(''.join(nb['cells'][i]['source']))
EOF
PYTHONPATH=. $PY -c "
import numpy as np, time, sadeghi as S
r=np.random.default_rng(0).random((16,20,6104)).astype(np.float32)
t=time.time(); T0,Tw=S.whole_window(3052); S.site_correlations(r[:,:,:3052],T0,Tw); print(time.time()-t)
t=time.time(); T0,Tw=S.whole_window(6104); S.site_correlations(r[:,::2],T0,Tw); print(time.time()-t)
"
```

```
--- 1
import time, resource
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import sadeghi as S

T_START = time.time()
P1_EXAMPLE, P2_EXAMPLE, P3_EXAMPLE = "P1_Site04", "P2_Site11", "P3_Site04"  # data set's FigureData list (finding aid)
SEED = {"P1": 101, "P2": 202, "P3": 303, "P3pca": 304}  # standard choices; one generator per site, from these
--- 3
desc, R1, R2, R3 = {}, {}, {}, {}
for name, raw in S.stream_members(lambda n: "/NeuralData/Paradigm" in n and n.endswith(".mat")):
    d = S.read_site(name, raw)
    del raw
    site = d["name"]
    desc[site] = S.describe(d)
    i = int(site[-2:])
    if site.startswith("P1"):
        R1[site] = S.process_p1(d, np.random.default_rng(SEED["P1"] * 100 + i), noiseless=(site == P1_EXAMPLE))
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import json
nb=json.load(open('reproduce_sadeghi_2019_neural.ipynb'))
for i in (8,35,38):
    print('---',i); print(''.join(nb['cells'][i]['source']))
nb=json.load(open('../../executed/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'))
for i in (24,30,35,58):
    print('--- out',i); print(''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])[:2500])
EOF
```

```
--- 8
def width_at(curve, tau, frac):
    """Full width (ms) of the contiguous region around the peak where curve >= frac * peak,
    with linear interpolation of the crossings."""
    i0 = int(np.argmax(curve))
    thr = frac * curve[i0]
    def cross(step):
        i = i0
        while 0 <= i + step < len(curve) and curve[i + step] >= thr:
            i += step
        if not (0 <= i + step < len(curve)):
            return tau[i]
        a, b = curve[i], curve[i + step]
        return tau[i] + (tau[i + step] - tau[i]) * (a - thr) / (a - b)
    return cross(1) - cross(-1)


def side_peak(curve, tau, min_lag=10.0):
    """Lag (ms) of the largest local maximum at positive lags beyond min_lag."""
    m = tau > min_lag
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
s=open('sadeghi.py').read()
s=s.replace('''    out = {"name": name.split("/")[-1][:-4],
           "param": {k: _chars(P[k]) for k in P.keys()}, "ras": {}, "fs": set(), "ntrials_ch": {}}
    snd = D["Sound"]
    sub = [k for k in snd.keys()][0]  # 'Channel', 'Condition' or 'Exemplar\'''','''XX''') if False else s
old='''    out = {"name": name.split("/")[-1][:-4],
           "param": {k: _chars(P[k]) for k in P.keys()}, "ras": {}, "fs": set(), "ntrials_ch": {}}
    snd = D["Sound"]'''
assert old in s
s=s.replace(old,'''    out = {"name": name.split("/")[-1][:-4],
           "param": {k: _chars(P[k]) for k in P.keys()}, "ras": {}, "fs": set(), "ntrials_ch": {},
           "fields": {"Data": sorted(D.keys()), "Data.Param": sorted(P.keys()), "Data.Sound": sorted(D["Sound"].keys())}}
    snd = D["Sound"]''')
old='''def whole_window(nsamples'''
s=s.replace(old,'''def split_half(ras):
    """Split-half reliability of the stimulus-driven (shuffled) correlations of one raster
    (channels, trials, samples), for the aMUA part of S10 Fig F ("comparing neural correlations
    across halves of the data"). Halves are read two ways: (time) the first and second 1.5 s, as
    NeuralExample.m splits the raster (sA, sB), each with its whole-window correlation; (trial)
    odd and even trials, each over the whole response. Returns {half: (r spectral with the
    diagonal, r spectral off the diagonal, r temporal)}, Pearson r between the two halves."""
    NS = ras.shape[-1]
    NS2 = NS // 2
    T0h, Twh = whole_window(NS2)
    T0, Tw = whole_window(NS)
    pairs = {"time": (site_correlations(ras[:, :, :NS2], T0h, Twh), site_correlations(ras[:, :, NS2:2 * NS2], T0h, Twh)),
             "trial": (site_correlations(ras[:, 0::2], T0, Tw), site_correlations(ras[:, 1::2], T0, Tw))}
    off = ~np.eye(ras.shape[0], dtype=bool)
    out = {}
    for k, (a, b) in pairs.items():
        out[k] = (float(np.corrcoef(a["spec"]["sh"].ravel(), b["spec"]["sh"].ravel())[0, 1]),
                  float(np.corrcoef(a["spec"]["sh"][off], b["spec"]["sh"][off])[0, 1]),
                  float(np.corrcoef(a["temp"]["sh"].ravel(), b["temp"]["sh"].ravel())[0, 1]))
    return out


def whole_window(nsamples''',1)
s=s.replace('''    out = {"param": d["param"], "fs": sorted(d["fs"]), "cond": {}}''','''    out = {"param": d["param"], "fs": sorted(d["fs"]), "cond": {}, "fields": d["fields"]}''')
open('sadeghi.py','w').write(s)
EOF
grep -n "def zero_lag_all" sadeghi.py; PYTHONPATH=. $PY -c "
import numpy as np, sadeghi as S
r=np.random.default_rng(0).random((16,20,6104)).astype(np.float32)
r+= np.sin(np.arange(6104)/30)[None,None,:]*np.linspace(0.2,1,16)[:,None,None]
print(S.split_half(r))"
```

```
166:def zero_lag_all(X):
{'time': (0.9998914130941651, 0.9998882974809692, 0.9999897277417502), 'trial': (0.9999199366728589, 0.9999215600134317, 0.9999891125009551)}
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import json
p='reproduce_sadeghi_2019_neural.ipynb'
nb=json.load(open(p))
src=lambda i: ''.join(nb['cells'][i]['source'])
def put(i, s): nb['cells'][i]['source']=s
# loading
s=src(3)
s=s.replace('''desc, R1, R2, R3 = {}, {}, {}, {}
for name, raw in S.stream_members(lambda n: "/NeuralData/Paradigm" in n and n.endswith(".mat")):
    d = S.read_site(name, raw)''','''desc, R1, R2, R3, SH, NAMES, CODE = {}, {}, {}, {}, {}, [], {}
def want(n):
    NAMES.append(n)  # every file member of the tar, for the data check
    return ("/NeuralData/Paradigm" in n and n.endswith(".mat")) or n.endswith("/Code/Examples/NeuralExample.m")
for name, raw in S.stream_members(want):
    if name.endswith(".m"):
        CODE[name.split("/")[-1]] = raw.decode("latin-1")
        continue
    d = S.read_site(name, raw)''')
s=s.replace('''    desc[site] = S.describe(d)
''','''    desc[site] = S.describe(d)
    SH[site] = {key: S.split_half(r) for key, r in d["ras"].items()}  # figs10-amua-tmua, aMUA part
''')
put(3,s)
# sanity
s=src(5)
s=s.replace('''print("files:", len(P1_SITES)''','''tops = {}
for n in NAMES:
    parts = n.split("/")
    tops.setdefault("/".join(parts[:3]) if parts[1] in ("NeuralData", "Sounds", "Code") else "/".join(parts[:2]), []).append(n)
print("tar members (files):", len(NAMES), "|", ", ".join(f"{k} {len(v)}" for k, v in sorted(tops.items())))
print("files other than .mat and .wav:", sorted(n for n in NAMES if not n.endswith((".mat", ".wav"))))
print("fields of every neural file:", sorted({repr(desc[s_]["fields"]) for s_ in desc}))
print("Param fields:", sorted({tuple(sorted(desc[s_]["param"])) for s_ in desc}))
print("files:", len(P1_SITES)''')
put(5,s)
# fig1k: print the code lines
s=src(10)
s=('''code = CODE["NeuralExample.m"].splitlines()
print("NeuralExample.m, the lines that set the window of Fig 1 (line numbers of the file):")
for i, line in enumerate(code, 1):
    if any(k in line for k in ("NS2=", "sA=", "sB=", "RASNMod=", "T0Mod=", "TwMod=", "MaxTau=", "MaxLag=", "rastermuashuffledxcovwinfastN(RASNMod")):
        print(f"   {i:3d}: {line.strip()}")
'''+s)
put(10,s)
# figs6: flag snake below chance
s=src(30)
s=s.replace('''        snake_ns = all(v[1] >= 0.05 or v[0] <= 20 for v in snake.values())
        print(f"{READ_TXT[r]}, a ({st[-1]}): {n_ok}/18 other conditions above chance (two-sided p < 0.05);"
              f" snake temporal not above chance: {snake_ns}")''','''        snake_ns = all(v[1] >= 0.05 or v[0] <= 20 for v in snake.values())
        below = [f"{c} {v[0]:.0f}% p={v[1]:.2g}" for c, v in snake.items() if v[0] < 20 and v[1] < 0.05]
        print(f"{READ_TXT[r]}, a ({st[-1]}): {n_ok}/18 other conditions above chance (two-sided p < 0.05);"
              f" snake temporal not above chance: {snake_ns}; snake significantly below chance (the paper has p = 0.15 and 0.92): {below or 'none'}")''')
put(30,s)
# fig4: add temporal r without lag 0 and per channel
s=src(35)
s+='''
print("temporal r variants, whole window, over the five sounds (verifier round 1 asked whether lag 0 drives it):")
for lab, sel in (("lags other than 0", np.abs(TAU) > 1e-9), ("|lag| > 5 ms", np.abs(TAU) > 5), ("|lag| > 20 ms", np.abs(TAU) > 20)):
    v = [np.corrcoef(R2[P2_EXAMPLE]["corr_orig"][k]["whole"]["temp"]["sh"][:, sel].ravel(),
                     R2[P2_EXAMPLE]["corr_eq"][k]["whole"]["temp"]["sh"][:, sel].ravel())[0, 1] for k in range(5)]
    print(f"   {lab}: r {np.mean(v):.3f} +/- {se(np.array(v)):.3f} (per sound {np.round(v, 2)})")
v = [np.median([np.corrcoef(R2[P2_EXAMPLE]["corr_orig"][k]["whole"]["temp"]["sh"][c], R2[P2_EXAMPLE]["corr_eq"][k]["whole"]["temp"]["sh"][c])[0, 1]
                for c in range(16)]) for k in range(5)]
print(f"   per channel (median over the 16 channels): r {np.mean(v):.3f} +/- {se(np.array(v)):.3f} (per sound {np.round(v, 2)})"
      f" | within 0.72 +/- 0.07: {within(np.mean(v), 0.72, 0.07)}")'''
put(35,s)
# figs9: eq_3a and eq_3b, and per-site values
s=src(58)
s=s.replace('''for r in READ:
    for asel in ("a", "b"):
        a1 = np.array([R1[s]["single"]["alpha"][(r, asel)] for s in P1_SITES])
        a2 = np.array([R2[s]["eq_3a"]["alpha"][(r, asel)] for s in P2_SITES])
        pooled = np.concatenate([a1, a2])
        line = (f"{r} a on ({asel}) data: P1 median''','''for r in READ:
  for m2 in ("eq_3a", "eq_3b"):
    for asel in ("a", "b"):
        a1 = np.array([R1[s]["single"]["alpha"][(r, asel)] for s in P1_SITES])
        a2 = np.array([R2[s][m2]["alpha"][(r, asel)] for s in P2_SITES])
        pooled = np.concatenate([a1, a2])
        line = (f"{r} P2 ({m2[-2:]}) a on ({asel}) data: P1 median''')
s+='''
print("per-site a, (1b)(2a), a on the validation data (P1 | P2 (3a) | P2 (3b) | P3 (a)):")
print("   ", [R1[s]["single"]["alpha"][("1b2a", "b")] for s in P1_SITES], "|", [R2[s]["eq_3a"]["alpha"][("1b2a", "b")] for s in P2_SITES], "|",
      [R2[s]["eq_3b"]["alpha"][("1b2a", "b")] for s in P2_SITES], "|", [R3[s]["a"]["alpha"][("1b2a", "b")] for s in P3_SITES])'''
put(58,s)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; python - <<'EOF'
import json
nb=json.load(open('entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'))
for i,c in enumerate(nb['cells']):
    if 'figs9-mixing' in str(c['metadata'].get('tags')): print(''.join(c['source'])[:600])
EOF
```

```
entries/sadeghi-2019/model.py                      | 167 ++++++++-
 .../reproduce_sadeghi_2019_neural.ipynb            | 166 +--------
 entries/sadeghi-2019/sadeghi.py                    |  27 +-
 tools/build_site.py                                | 386 ++++++++++++++++++---
 tools/entry.py                                     |   6 +
 tools/site_assets/app.css                          |  89 ++++-
 tools/site_assets/list.js                          |  11 +-
 7 files changed, 617 insertions(+), 235 deletions(-)
for r in READ:
  for m2 in ("eq_3a", "eq_3b"):
    for asel in ("a", "b"):
        a1 = np.array([R1[s]["single"]["alpha"][(r, asel)] for s in P1_SITES])
        a2 = np.array([R2[s][m2]["alpha"][(r, asel)] for s in P2_SITES])
        pooled = np.concatenate([a1, a2])
        line = (f"{r} P2 ({m2[-2:]}) a on ({asel}) data: P1 median {np.median(a1):.2f}, P2 median {np.median(a2):.2f},"
                f" pooled 24 sites median {np.median(pooled):.2f} (quartiles {np.percentile(pooled, 25):.2f}, {np.percentile(pooled, 75):.2f})")
        for rd in ("a", "b"):
            a3 = np.array([R3[s][rd]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY -c "
import nbformat as n
for p in ['reproduce_sadeghi_2019_neural.ipynb','reproduce_sadeghi_2019_classifier.ipynb']:
    nb=n.read(p,as_version=4); n.validate(nb); n.write(nb,p)
"; git diff --stat .; git diff reproduce_sadeghi_2019_neural.ipynb | head -30
```

```
entries/sadeghi-2019/model.py                      | 167 ++++++++++++++++++++-
 .../reproduce_sadeghi_2019_neural.ipynb            |  50 +++++-
 entries/sadeghi-2019/sadeghi.py                    |  27 +++-
 3 files changed, 232 insertions(+), 12 deletions(-)
diff --git a/entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb b/entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb
index bb35400..09e802a 100644
--- a/entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb
+++ b/entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb
@@ -89,12 +89,19 @@
    "metadata": {},
    "outputs": [],
    "source": [
-    "desc, R1, R2, R3 = {}, {}, {}, {}\n",
-    "for name, raw in S.stream_members(lambda n: \"/NeuralData/Paradigm\" in n and n.endswith(\".mat\")):\n",
+    "desc, R1, R2, R3, SH, NAMES, CODE = {}, {}, {}, {}, {}, [], {}\n",
+    "def want(n):\n",
+    "    NAMES.append(n)  # every file member of the tar, for the data check\n",
+    "    return (\"/NeuralData/Paradigm\" in n and n.endswith(\".mat\")) or n.endswith(\"/Code/Examples/NeuralExample.m\")\n",
+    "for name, raw in S.stream_members(want):\n",
+    "    if name.endswith(\".m\"):\n",
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; time PYTHONPATH=. $PY - <<'EOF'
import numpy as np, sadeghi as S, time
desc, SH, NAMES, CODE = {}, {}, [], {}
def want(n):
    NAMES.append(n)
    return ("/NeuralData/Paradigm" in n and n.endswith(".mat")) or n.endswith("/Code/Examples/NeuralExample.m")
for name, raw in S.stream_members(want):
    if name.endswith(".m"):
        CODE[name.split("/")[-1]] = raw.decode("latin-1"); continue
    d = S.read_site(name, raw); site=d["name"]
    desc[site] = S.describe(d)
    t=time.time(); SH[site] = {key: S.split_half(r) for key, r in d["ras"].items()}; print('split', time.time()-t)
    break
tops = {}
for n in NAMES:
    parts = n.split("/")
    tops.setdefault("/".join(parts[:3]) if parts[1] in ("NeuralData", "Sounds", "Code") else "/".join(parts[:2]), []).append(n)
print("tar members (files):", len(NAMES), "|", ", ".join(f"{k} {len(v)}" for k, v in sorted(tops.items())))
print("fields of every neural file:", sorted({repr(desc[s_]["fields"]) for s_ in desc}))
print("Param fields:", sorted({tuple(sorted(desc[s_]["param"])) for s_ in desc}))
print(list(SH[site].items())[:3])
code = CODE["NeuralExample.m"].splitlines()
for i, line in enumerate(code, 1):
    if any(k in line for k in ("NS2=", "sA=", "sB=", "RASNMod=", "T0Mod=", "TwMod=", "MaxTau=", "MaxLag=", "rastermuashuffledxcovwinfastN(RASNMod")):
        print(f"   {i:3d}: {line.strip()}")
EOF
```

```
split 11.075096130371094
tar members (files): 247 | data/Code/AuditoryModelCorr 14, data/Code/Examples 4, data/Code/MUACorrAnalysis 3, data/Docs 2, data/NeuralData/Paradigm3 1, data/Sounds/ModelSounds 195, data/Sounds/Paradigm1 5, data/Sounds/Paradigm2 5, data/Sounds/Paradigm3 18
fields of every neural file: ["{'Data': ['Param', 'Sound'], 'Data.Param': ['AnimalNo', 'BlockNo', 'RecordDate'], 'Data.Sound': ['Exemplar']}"]
Param fields: [('AnimalNo', 'BlockNo', 'RecordDate')]
[((0, 0), {'time': (0.9767499364999195, 0.9749895884215664, 0.8752192636211854), 'trial': (0.969180717509102, 0.9707083683392503, 0.9848297339166661)}), ((0, 1), {'time': (0.9758961767112406, 0.972348519541287, 0.8548221989464364), 'trial': (0.9942970471159599, 0.9950520100554539, 0.9854948957952937)}), ((0, 2), {'time': (0.9576822787783766, 0.9492709648154759, 0.8809713178588499), 'trial': (0.9949292594189564, 0.9948491260280135, 0.9947038748226525)})]
    73: NS2=floor(NS/2);
    74: sA=1:NS2;           %First half (1.5 s) of the data
    75: sB=NS2+1:NS;        %Second half (1.5 s) of the data
    80: RASNMod=RASNA;
    83: MaxTau=100;                                     %Maxium lag in ms for correlation
    84: MaxLag=ceil(MaxTau*Fsd/1000);                   %Maximum lag in samples for correlation
    86: T0Mod=floor(NSMod/Fsd*1000/2);                  %Center time of the raster in ms
    87: TwMod=floor((NSMod-MaxLag*2-2)/Fsd*1000);       %Width of the window in ms
    90: [CovWinDataN]=rastermuashuffledxcovwinfastN(RASNMod,Fsd,T0Mod,TwMod,MaxTau,'y','y','n');    %THIS IS THE MAIN ROUTINE USED TO GENERATE THE CORRELOGRAMS
   110: ModData(k,l).Win(1,1).Param.MaxTau=MaxTau;

real	0m33.125s
user	0m16.673s
sys	0m1.924s
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import nbformat as n
p='reproduce_sadeghi_2019_neural.ipynb'
nb=n.read(p,as_version=4)
i=[k for k,c in enumerate(nb.cells) if c.cell_type=='markdown' and c.source.startswith('## Summary')][0]
md=n.v4.new_markdown_cell('''## figs10-amua-tmua (aMUA part)

> Correlations from thresholded MUA resemble those from aMUA (median r 0.81 spectral, 0.35
> temporal) but are weaker and noisier; split-half reliability is higher for aMUA (0.98 and 0.83)
> than for tMUA (0.77 and 0.27).

The tMUA needs the raw voltage traces, which the data set does not hold (the data check lists
every member of the tar and every field of the neural files), so four of the six values cannot
be computed and the claim stays blocked. The two aMUA split-half values can: Pearson r between
the stimulus-driven correlations of two halves of the data (S10 Fig F legend), per raster.
Halves are read as (time) the first and second 1.5 s, as NeuralExample.m splits the raster, or
(trial) odd and even trials; sites and sounds as the claims file's readings (a) paradigm 1, (b)
all paradigms. The spectral r is shown with and without the zero-lag diagonal.''')
code=n.v4.new_code_cell('''for half in ("time", "trial"):
    for rd, sites in (("a", P1_SITES), ("b", P1_SITES + P2_SITES + P3_SITES)):
        V = np.array([SH[s][key][half] for s in sites for key in SH[s]])
        print(f"halves ({half}), reading ({rd}), {len(V)} site and sound rasters: median r spectral {np.median(V[:, 0]):.3f}"
              f" (off the diagonal {np.median(V[:, 1]):.3f}), temporal {np.median(V[:, 2]):.3f}"
              f" | range spectral {V[:, 0].min():.2f} to {V[:, 0].max():.2f}, temporal {V[:, 2].min():.2f} to {V[:, 2].max():.2f}"
              f" | within 0.98 +/- 0.098: {within(np.median(V[:, 0]), 0.98, 0.098)}, 0.83 +/- 0.083: {within(np.median(V[:, 2]), 0.83, 0.083)}")
for p_, sites in (("P1", P1_SITES), ("P2", P2_SITES), ("P3", P3_SITES)):
    V = np.array([SH[s][key]["time"] for s in sites for key in SH[s]])
    print(f"   {p_}, time halves: median spectral {np.median(V[:, 0]):.3f}, temporal {np.median(V[:, 2]):.3f}")''')
code.metadata['tags']=['claim:figs10-amua-tmua']
md2=n.v4.new_markdown_cell('**Result: (filled in after the run)**')
nb.cells[i:i]=[md,code,md2]
n.write(nb,p)
EOF
date -u
```

```
Sat Nov 14 04:34:54 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python -c "
import pickle; c=pickle.load(open('code.pkl','rb')); print(c['data/Code/AuditoryModelCorr/criticalbandwidth.m'].decode('latin1'))"
```

```
%
%function [CB]=criticalbandwidth(fc)
%
%   FILE NAME       : CRITICAL BANDWIDTH
%   DESCRIPTION     : Critical Bandwidth for auditory fitlers
%                     
%	fc              : Filter characteristic frequency (Hz)
%
%RETURNED VARIABLES
%
%	CB               : Critical Bandwidth (Hz)
%
% (C) Monty A. Escabi, December 2007
%
function [CB]=criticalbandwitdh(fc)

CB=94+71.*(fc/1000).^(3/2);

%Alternate form which gives nearly identical result: CB = 25 + 75 * [1 + 1.4 *(fc/1000).^2].^0.69 - Zwicker & Terhardt 1980
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
s=open('model.py').read()
s=s.replace('''def cochleogram(x, fs=FS_SOUND):
    """(58 channels, samples at 1 kHz) envelopes."""
    x = x / x.std()
    fc = centre_frequencies()
    bw = bandwidth_methods(fc)''','''def bandwidth_code(fc):
    """criticalbandwidth.m of the deposit's code: 94 + 71 f^1.5, f in kHz (a variant)."""
    return 94 + 71 * (fc / 1000) ** 1.5


def cochleogram(x, fs=FS_SOUND, bandwidth=bandwidth_methods):
    """(58 channels, samples at 1 kHz) envelopes."""
    x = x / x.std()
    fc = centre_frequencies()
    bw = bandwidth(fc)''')
open('model.py','w').write(s)
import nbformat as n
p='reproduce_sadeghi_2019_model.ipynb'
nb=n.read(p,as_version=4)
i=[k for k,c in enumerate(nb.cells) if 'claim:fig7i-stationarity' in str(c.metadata.get('tags'))][0]
md=n.v4.new_markdown_cell('''Variant: the bandwidths of the deposit's criticalbandwidth.m (94 + 71 f^1.5, used by
ModelExample.m) in place of the Methods' formula, for the eight categories the SI values rest on
(reading (c): flowing water, waves, thunder and rain, wind; the four vocalizations), with the
same short-term correlation at tau_W = 100 ms.''')
code=n.v4.new_code_cell('''t1 = time.time()
SIc = {"a": {}, "b": {}}
for c in ENV_C + VOC:
    for i in range(1, 16):
        fs, x, _ = sounds[(c, i)]
        Sg = M.cochleogram(x, fs, bandwidth=M.bandwidth_code)
        n, s2, acc = 0, 0.0, None
        for v in M.short_term_iter(Sg, 100, 49, pairs="all"):
            v = v.astype(np.float64)
            acc = v.copy() if acc is None else acc + v
            s2 += (v ** 2).sum()
            n += 1
        m2 = float(((acc / n) ** 2).sum())
        SIc["a"][(c, i)] = 1 - (s2 / n - m2) / m2
        SIc["b"][(c, i)] = 1 - (s2 / n - m2) / (s2 / n)
for r in ("a", "b"):
    catm = {c: np.mean([SIc[r][(c, i)] for i in range(1, 16)]) for c in ENV_C + VOC}
    ev, vv = [catm[c] for c in ENV_C], [catm[c] for c in VOC]
    se = lambda x: np.std(x, ddof=1) / np.sqrt(len(x))
    print(f"code bandwidths, ({r})(c)(e): environmental {np.mean(ev):.3f} +/- {se(ev):.3f}, vocalizations {np.mean(vv):.3f} +/- {se(vv):.3f}"
          f" | both in tol {abs(np.mean(ev) - 0.49) <= 0.04 and abs(np.mean(vv) - 0.28) <= 0.04} | category means "
          + ", ".join(f"{c} {v:.3f}" for c, v in sorted(catm.items(), key=lambda kv: kv[1])))
print(f"variant took {(time.time() - t1) / 60:.1f} min")''')
code.metadata['tags']=['claim:fig7i-stationarity']
nb.cells[i+1:i+1]=[md,code]
n.write(nb,p)
EOF
grep -n "ENV_C\b\|^VOC" -m3 reproduce_sadeghi_2019_model.ipynb | head
```

```
374:    "ENV_C = [\"Flowing_Water\", \"Wave\", \"Thunder_Rain\", \"Wind\"]\n",
375:    "GROUPS = {\"c\": (ENV_C, VOC), \"d\": (ENV_C + [\"Bird_Chorus\", \"Speech_Babble\"], VOC)}\n",
418:    "for c in ENV_C + VOC:\n",
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import nbformat as n
p='reproduce_sadeghi_2019_model.ipynb'
nb=n.read(p,as_version=4)
h=nb.cells[0].source
old_rows=[l for l in h.splitlines() if l.startswith('| fig9') or l.startswith('| fig10')]
for l in old_rows:
    cid=l.split('|')[1].strip()
    h=h.replace(l, f'| {cid} | in reproduce_sadeghi_2019_classifier.ipynb |')
h=h.replace("This notebook tests the auditory model claims; the neural claims are in\nreproduce_sadeghi_2019_neural.ipynb.",
 "This notebook tests the auditory model correlation claims; the model classifier claims are in\nreproduce_sadeghi_2019_classifier.ipynb and the neural claims in reproduce_sadeghi_2019_neural.ipynb.")
nb.cells[0].source=h
# drop the cost-estimate cells (markdown, code, result)
k=[i for i,c in enumerate(nb.cells) if c.source.startswith('## Model classification claims: cost estimate')][0]
del nb.cells[k:k+3]
s=[c for c in nb.cells if c.source.startswith('## Summary')][0]
s.source=s.source.replace('| fig9a, fig9b (two), fig9c, fig9e, fig9 spectrum, fig10 | blocked, too large for this run |','| fig9a, fig9b (two), fig9c, fig9e, fig9 spectrum, fig10 | tested in reproduce_sadeghi_2019_classifier.ipynb |')
n.write(nb,p)
print(nb.cells[0].source[-900:])
EOF
grep -n "cost\|too large" reproduce_sadeghi_2019_model.ipynb | head; PYTHONPATH=. $PY -c "
import pickle,os,model as M, numpy as np
snd=pickle.load(open(os.environ['TMPDIR']+'/dev/snd.pkl','rb'))
k=[k for k in snd if 'Wind' in k][0]; fs,x=M.read_wav(snd[k]); a=M.cochleogram(x,fs,bandwidth=M.bandwidth_code); b=M.cochleogram(x,fs); print(a.shape, np.abs(a-b).max())
print(M.bandwidth_code(np.array([1000.,4000])), M.bandwidth_methods(np.array([1000.,4000])))"
```

```
|
| fig9a-optimal-resolution | in reproduce_sadeghi_2019_classifier.ipynb |
| fig9b-similar-maximum | in reproduce_sadeghi_2019_classifier.ipynb |
| fig9b-accumulation-rate | in reproduce_sadeghi_2019_classifier.ipynb |
| fig9c-time-averaged-worse | in reproduce_sadeghi_2019_classifier.ipynb |
| fig9e-category-specific | in reproduce_sadeghi_2019_classifier.ipynb |
| fig9-spectrum-classifier-lower | in reproduce_sadeghi_2019_classifier.ipynb |
| fig10-vocalization-background | in reproduce_sadeghi_2019_classifier.ipynb |

Method: the cochlear model and short-term correlations follow the Methods ("Auditory model",
"Nonstationary spectro-temporal correlation statistics", "Stationarity and ensemble diversity
indices") and port the paper's code in the data set (Code/AuditoryModelCorr); model.py says
where each parameter comes from. White noise is generated, as the data set does not hold it.
(58, 10000) 0.10244887334844965
[165. 662.] [162.21671569 685.41998197]
```

**Agent calls Bash**

```bash
cd  sed -n 566,610p tools/entry.py
```

```
return 1

    results, failed = [], False
    for notebook in entry["notebooks"]:
        name = notebook["path"]
        started = time.time()
        r = subprocess.run(
            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
             "--output-dir", str(output_dir.resolve()), "--output", name, name],
            cwd=entry_dir, capture_output=True, text=True,
            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
        seconds = round(time.time() - started)
        ok = r.returncode == 0
        error = None if ok else r.stderr[-3000:]
        if ok and seconds > max_minutes * 60:
            ok = False
            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
        failed |= not ok
        results.append({"notebook": name, "ok": ok, "seconds": seconds, "error": error})
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; python - <<'EOF'
s=open('entry.yaml').read()
s=s.replace('''notebooks:
- path: reproduce_sadeghi_2019_neural.ipynb''','''notebooks:
- path: reproduce_sadeghi_2019_classifier.ipynb
  title: Auditory model classifier of the 195 model sounds (Figs 9 and 10)
  runtime_minutes: 40
- path: reproduce_sadeghi_2019_neural.ipynb''')
s=s.replace('runtime_minutes: 35','runtime_minutes: 40').replace('runtime_minutes: 16','runtime_minutes: 24')
s=s.replace("the model's correlation widths, stationarity and diversity.","the model's correlation widths, stationarity and diversity, and the model's leave-one-sound-out\n  category classifier.")
open('entry.yaml','w').write(s)
EOF
cat entry.yaml; cd ../..; python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -15; date -u
```

```
schema_version: 1
name: sadeghi-2019
type: reproduction
title: A neural ensemble correlation code for sound category identification (Sadeghi et al. 2019)
description: Tests the findings of Sadeghi, Zhai, Stevenson and Escabi (2019) on CRCNS bst-2, which
  holds the analog multiunit activity of 35 inferior colliculus recordings in unanesthetized rabbits
  (13 sites listening to five natural sounds, 11 to their 1/f spectrum-equalized variants, 11 to six
  exemplars of three categories) and the 195 sounds of the paper's auditory model. It recomputes the
  stimulus-driven and noise correlations with a port of the paper's code, the single-trial
  correlation classifiers, and the model's correlation widths, stationarity and diversity, and the model's leave-one-sound-out
  category classifier.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_sadeghi_2019_classifier.ipynb
  title: Auditory model classifier of the 195 model sounds (Figs 9 and 10)
  runtime_minutes: 40
- path: reproduce_sadeghi_2019_neural.ipynb
  title: Neural ensemble correlations and classifiers, paradigms 1 to 3
  runtime_minutes: 40
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
s=open('build_clf.py').read()
old_a=s.index('def coch(b):')
old_b=s.index('print(f"read and filtered')
s=s[:old_a]+'''WAV = [M.read_wav(by_key[k]) for k in KEYS]
COCH = [M.cochleogram(x, fs).astype(np.float32) for fs, x in WAV]
del raw, by_key
'''+s[old_b:]
s=s.replace('''print("sampling rates:", sorted({o[1] for o in out}), "; samples per sound:", sorted({o[2] for o in out}))''','''print("sampling rates:", sorted({w[0] for w in WAV}), "; samples per sound:", sorted({len(w[1]) for w in WAV}))''')
s=s.replace('del out, F0', 'del WAV, F0')
open('build_clf.py','w').write(s)
EOF
grep -n "WAV\|del raw" $TMPDIR/dev/build_clf.py | head; cd entries/sadeghi-2019; executed/sadeghi-2019/.venv/bin/python $TMPDIR/dev/build_clf.py reproduce_sadeghi_2019_classifier.ipynb; executed/sadeghi-2019/.venv/bin/python -c "
import nbformat as n; nb=n.read('reproduce_sadeghi_2019_classifier.ipynb',as_version=4); print(nb.cells[3].source)"
```

```
79:WAV = [M.read_wav(by_key[k]) for k in KEYS]
80:COCH = [M.cochleogram(x, fs).astype(np.float32) for fs, x in WAV]
81:del raw, by_key
85:print("sampling rates:", sorted({w[0] for w in WAV}), "; samples per sound:", sorted({len(w[1]) for w in WAV}))
95:del WAV, F0""", "sanity")
raw = {}
for name, b in S.stream_members(lambda n: "/Sounds/ModelSounds/" in n and n.endswith(".wav")):
    raw[name] = b
    if len(raw) == 195:
        break
KEYS = sorted((n.split("/")[-2], int(n.split("_")[-1][:-4])) for n in raw)
CATS = sorted({k[0] for k in KEYS})
LAB = np.array([CATS.index(k[0]) for k in KEYS])
by_key = {(n.split("/")[-2], int(n.split("_")[-1][:-4])): b for n, b in raw.items()}

WAV = [M.read_wav(by_key[k]) for k in KEYS]
COCH = [M.cochleogram(x, fs).astype(np.float32) for fs, x in WAV]
del raw, by_key
print(f"read and filtered {len(COCH)} sounds in {(time.time() - T_START) / 60:.1f} min")
```

**Agent**

Entry check passes. Starting the full run: the classifier notebook first, then neural, then model. Expected about 100 minutes.

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/sadeghi-2019 2>&1 | tail -30; date -u
```

```
Exit code 143
Command timed out after 2h 0m 0s
Sat Nov 14 04:36:24 UTC 2026
```

**Agent calls Bash**

```bash
date -u; ls -la executed/sadeghi-2019/; cat executed/sadeghi-2019/result.json
```

```
Sat Nov 14 06:36:31 UTC 2026
total 636
drwxr-xr-x 3 runner runner   4096 Nov 14 05:15 .
drwxr-xr-x 3 runner runner   4096 Nov 14 03:03 ..
drwxr-xr-x 5 runner runner   4096 Nov 14 04:36 .venv
-rw-r--r-- 1 runner runner 166461 Nov 14 05:15 reproduce_sadeghi_2019_classifier.ipynb
-rw-r--r-- 1 runner runner  98070 Nov 14 02:44 reproduce_sadeghi_2019_model.ipynb
-rw-r--r-- 1 runner runner 364673 Nov 14 06:14 reproduce_sadeghi_2019_neural.ipynb
-rw-r--r-- 1 runner runner    293 Nov 14 02:44 result.json
{
 "entry": "sadeghi-2019",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_sadeghi_2019_neural.ipynb",
   "ok": true,
   "seconds": 1678,
   "error": null
  },
  {
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git checkout entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb; executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import json
nb=json.load(open('executed/sadeghi-2019/reproduce_sadeghi_2019_classifier.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        out=''.join(''.join(o.get('text','')) if 'text' in o else (o.get('ename','')+str(o.get('evalue',''))) for o in c.get('outputs',[]) )
        print('---',i,c['metadata'].get('tags'),out[:4000])
EOF
```

```
Updated 1 path from the index
--- 1 None 
--- 3 None read and filtered 195 sounds in 9.7 min

--- 4 ['sanity'] categories: 13 ; sounds per category: [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
sampling rates: [44100] ; samples per sound: [441000]
cochleogram shape (channels, ms): [(58, 10000)]
envelope range over all sounds: 0.0 to 26.193 (the sound is normalised to unit SD before filtering)
features at tau_W = 100 ms: {'spec': (386, 1653), 'temp': (386, 58, 50), 'spectrum': (386, 58), 'centres': (386,)} ; Kaiser length 269 ms
spectral feature range -0.268 to 0.997 ; temporal -0.541 to 0.98 (correlations, within -1 to 1)
resolutions tau_W (ms): [ 25.   35.4  50.   70.7 100.  141.4 200.  282.8 400.  565.7]
Kaiser window length (ms) at each: [69, 97, 135, 191, 269, 381, 537, 759, 1073, 1517]

--- 6 None tau_W   25.0 ms: windows (6a) 331, (6b) 138; PCs for 90%: spec 80, temp 5, st 135, spectrum 8 | 4.1 min, peak memory 5.7 GB
tau_W   35.4 ms: windows (6a) 275, (6b) 100; PCs for 90%: spec 66, temp 6, st 126, spectrum 7 | 7.7 min, peak memory 6.3 GB
tau_W   50.0 ms: windows (6a) 164, (6b) 69; PCs for 90%: spec 53, temp 7, st 117, spectrum 7 | 11.1 min, peak memory 6.9 GB
tau_W   70.7 ms: windows (6a) 136, (6b) 50; PCs for 90%: spec 42, temp 8, st 103, spectrum 7 | 13.5 min, peak memory 7.0 GB
tau_W  100.0 ms: windows (6a) 97, (6b) 36; PCs for 90%: spec 34, temp 8, st 90, spectrum 6 | 15.6 min, peak memory 7.2 GB
tau_W  141.4 ms: windows (6a) 55, (6b) 25; PCs for 90%: spec 26, temp 8, st 73, spectrum 6 | 17.2 min, peak memory 7.5 GB
tau_W  200.0 ms: windows (6a) 47, (6b) 17; PCs for 90%: spec 21, temp 8, st 60, spectrum 6 | 19.0 min, peak memory 8.0 GB
[... 124 more lines not kept]
```

**Agent**

Classifier results are in. Now the new neural outputs:

**Agent calls Bash**

```bash
cd  executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import json
nb=json.load(open('executed/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'))
errs=[o for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]) if o.get('output_type')=='error']
print('errors', len(errs))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        t=c['metadata'].get('tags')
        out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
        if t in (['sanity'],) : print('---',i,out[:900])
        if t and any(x in t[0] for x in ('fig1k','figs10','fig4-example','figs9')): print('---',i,t,out[:3500] if 'figs9' not in t[0] else out[-1800:])
        if t and 'figs6' in t[0]: print('---',i,out[:700])
    if c['cell_type']=='code' and 'total run time' in ''.join(c['source']): print(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])))
EOF
```

```
errors 0
--- 5 tar members (files): 281 | data/Code/AuditoryModelCorr 14, data/Code/Examples 4, data/Code/MUACorrAnalysis 3, data/Docs 2, data/NeuralData/Paradigm1 13, data/NeuralData/Paradigm2 11, data/NeuralData/Paradigm3 11, data/Sounds/ModelSounds 195, data/Sounds/Paradigm1 5, data/Sounds/Paradigm2 5, data/Sounds/Paradigm3 18
files other than .mat and .wav: ['data/Code/AuditoryModelCorr/bandpass.m', 'data/Code/AuditoryModelCorr/cochleogram.m', 'data/Code/AuditoryModelCorr/cochleogramdyncorr.m', 'data/Code/AuditoryModelCorr/convfft.m', 'data/Code/AuditoryModelCorr/criticalbandwidth.m', 'data/Code/AuditoryModelCorr/erb.m', 'data/Code/AuditoryModelCorr/fdesignh.m', 'data/Code/AuditoryModelCorr/fdesignkdt.m', 'data/Code/AuditoryModelCorr/finddtdfw.m', 'data/Code/AuditoryModelCorr/gammatonefilter.m', 'data/Code/AuditoryModelCorr/h.m', 'data/Code/AuditoryModelCorr/lowpass.m', 'data/Code/AuditoryModelCorr
--- 10 ['claim:fig1k-example-temporal-widths'] NeuralExample.m, the lines that set the window of Fig 1 (line numbers of the file):
    73: NS2=floor(NS/2);
    74: sA=1:NS2;           %First half (1.5 s) of the data
    75: sB=NS2+1:NS;        %Second half (1.5 s) of the data
    80: RASNMod=RASNA;
    83: MaxTau=100;                                     %Maxium lag in ms for correlation
    84: MaxLag=ceil(MaxTau*Fsd/1000);                   %Maximum lag in samples for correlation
    86: T0Mod=floor(NSMod/Fsd*1000/2);                  %Center time of the raster in ms
    87: TwMod=floor((NSMod-MaxLag*2-2)/Fsd*1000);       %Width of the window in ms
    90: [CovWinDataN]=rastermuashuffledxcovwinfastN(RASNMod,Fsd,T0Mod,TwMod,MaxTau,'y','y','n');    %THIS IS THE MAIN ROUTINE USED TO GENERATE THE CORRELOGRAMS
   110: ModData(k,l).Win(1,1).Param.MaxTau=MaxTau;
window whole     curve mean  : crowd 50% 2.8, water 50% 3.3, fire 50% 4.4, crowd 10% 5.7, water 10% 7.9, fire 10% 10.9, bird 50% 5.4, bird 10% 138.8, snake 50% 6.9, snake 10% 18.8
    snake side peak, channels 9-16 
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  grep -n "verifications" -A30 attempts/*.yaml | grep -v "^--$" | head -50; cat entries/sadeghi-2019/README.md | head -40
```

```
Sat Nov 14 06:37:29 UTC 2026
attempts/amjad-2025-01.yaml:287:verifications:
attempts/amjad-2025-01.yaml-288-- date: '2026-10-15'
attempts/amjad-2025-01.yaml-289-  kind: agent
attempts/amjad-2025-01.yaml-290-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
attempts/amjad-2025-01.yaml-291-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
attempts/amjad-2025-01.yaml-292-    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
attempts/amjad-2025-01.yaml-293-    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
attempts/amjad-2025-01.yaml-294-    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
attempts/amjad-2025-01.yaml-295-    reward_blocks). It had no attempt record and took the claims from the claims file.
attempts/amjad-2025-01.yaml-296-  results:
attempts/amjad-2025-01.yaml-297-  - claim: insertion-yield
attempts/amjad-2025-01.yaml-298-    agrees: true
attempts/amjad-2025-01.yaml-299-    outcome: blocked
attempts/amjad-2025-01.yaml-300-    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
attempts/amjad-2025-01.yaml-301-      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
attempts/amjad-2025-01.yaml-302-      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
attempts/amjad-2025-01.yaml-303-      not in the archive.
attempts/amjad-2025-01.yaml-304-    response: No change.
attempts/amjad-2025-01.yaml-305-  - claim: chronic-duration
[... 71 more lines not kept]
```

**Agent**

Writing the attempt record first, since it matters most.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/sadeghi-2019-01.yaml'
s=open(p).read()
a=s.index('- claim: fig9a-optimal-resolution')
b=s.index('findings:')
new='''- claim: fig9a-optimal-resolution
  outcome: reproduced
  assumed: true
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9a-optimal-resolution
  measured: [141.4, 100.0]
  notes: Under readings (6b) (windows spaced by the full Kaiser length) and (7b) (the reported PC and
    component counts), the spectral and temporal classifiers are best at 141 ms (82.1 and 80.5% at the
    full duration) and the spectro-temporal one at 100 ms (81.5%). Under (6a)(7b) the optima are 283,
    141 and 141 ms, and under the (7a) readings the spectro-temporal optimum is 283 ms, so the outcome
    rests on (6b)(7b). Every correlation classifier is above 7.69% at every resolution under every
    reading (lowest 58.5%, temporal at 25 ms; largest Bonferroni p over the 195 per-sound outcomes
    1.3e-31, over the 13 category means 7.9e-05). The accuracy curves over resolution are flat (spectral
    72 to 82%), so the optimum moves between neighbouring grid points with the reading.
  deviations:
  - The classifier is the Methods' pipeline, with choices the paper does not make, stated in
    model.py and the notebook; the spectro-temporal feature vector is the spectral and temporal
    features of a time point side by side; PCA is fitted once on all 195 sounds (refitted per fold
    for 26 folds as a variant, 80.8% against 76.9%); training observations are subsampled to 10000 per
    category, equally from each sound; the spectrum classifier, whose counts the paper does not give,
    uses the PCs for 90% and 8 components.
  - Reading (7a) uses the PCs explaining 90% at each resolution with the reported N_c; the
    cross-validated choice of N_c (over 1, 2, 3, 5, 8, 13 and 20 components, a subset of the Methods'
    1 to 20, for time) was run at each (6a)(7b) optimum only, giving 3 (reported 8) for spectral, 20
    (reported 5) for temporal and 13 (reported 13) for spectro-temporal.
- claim: fig9b-similar-maximum
  outcome: reproduced
  assumed: true
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9b-similar-maximum
  measured: [81.5, 82.1, 80.5]
  notes: Each classifier at its own optimum and the full duration, under (6b)(7b) the spectro-temporal
    classifier is 81.5%, spectral 82.1% and temporal 80.5%, all within tolerance, and no pair differs
    (two-sample t tests over the 195 per-sound outcomes, p 0.70, 0.90 and 0.80; over the 13 category
    accuracies p 0.84 to 0.95). Under (6a)(7b) the values are 83.1, 82.1 and 80.0% (p 0.43 to 0.79).
    Under (6a)(7a) the spectro-temporal classifier reaches 87.7% and differs from the temporal one
    (p = 0.04 over sounds, 0.27 over categories), so the absence holds under the (7b) readings, the
    reported counts, and under (7a) with (6b) (p 0.18 to 0.70).
  deviations:
  - As in fig9a-optimal-resolution.
- claim: fig9b-accumulation-rate
  outcome: partially_reproduced
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9b-accumulation-rate
  measured: [1.92, 2.67, 1.23]
  notes: No reading puts all three rise times within tolerance; the order spectro-temporal < spectral <
    temporal holds under the (7b) readings and (6a)(7a) for every way of measuring it. Under (6b)(7b)
    with linear interpolation, spectral 1.92 s (1.7 +/- 0.17), temporal 2.67 s (3.0 +/- 0.3) and
    spectro-temporal 1.23 s (1.2 +/- 0.12); with the first sampled duration 2.31, 3.08 and 1.65 s; with
    an exponential fit 1.45, 1.90 and 1.10 s. Under (6a)(7b) the times are shorter (0.6 to 1.9 s).
    Under (6b)(7a) the spectro-temporal classifier (at 283 ms) is no faster than the spectral one.
  deviations:
  - As in fig9a-optimal-resolution.
- claim: fig9c-time-averaged-worse
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9c-time-averaged-worse
  measured: 5.1
  notes: At the spectro-temporal optimum and the full duration, reading (a) (time-averaged category
    models, one diagonal Gaussian per category) is 5.1 to 5.6 points below the short-term classifier
    under every reading ((6b)(7b) 76.4 against 81.5%; 6.0 to 6.8% relative), not 25. Reading (b) (the
    running average of the test sound scored under the short-term models) is 15.4 to 36.9 points lower
    ((6b)(7b) 44.6 against 81.5%, 36.9 points, 45.3% relative). No reading gives 25 +/- 2.5; the
    time-averaged classifier is at least 10 points lower under reading (b) only, which meets the
    partial rule. The outcome rests on reading (b), whose test feature differs from the training
    features of the models.
  deviations:
  - As in fig9a-optimal-resolution. Reading (a) uses N_c = 1, as a category has only 14 or 15
    time-averaged vectors, and the vectors are the time averages of the short-term PC scores.
- claim: fig9e-category-specific
  outcome: partially_reproduced
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9e-category-specific
  measured: [100.0, 33.3, 33.3, 80.0]
  notes: Under (6a)(7b), waves are 100% with the spectral and 33.3% with the temporal classifier and
    wind 33.3% and 80.0%; three of four values are within tolerance (wind spectral 33.3 against 47 +/-
    6.7). Under the (6b) readings waves temporal and wind spectral are both 40.0% (two of four). Under
    every reading waves are better identified by spectral and wind by temporal correlations by at least
    six sounds of 15, which meets the partial rule.
  deviations:
  - As in fig9a-optimal-resolution.
- claim: fig9-spectrum-classifier-lower
  outcome: not_reproduced
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig9-spectrum-classifier-lower
  notes: The spectrum classifier (windowed mean envelope of each channel) varies by 9.7 to 10.3 points
    over the ten resolutions (70.3 to 80.5% at the full duration) and is best at the shortest windows,
    25 or 50 ms, where it reaches 80.0 to 80.5%. It is not below every correlation classifier at the full
    duration under any reading (for example (6a)(7b) 80.0% against temporal 80.0% and spectral 82.1%) and
    is above the temporal classifier at most durations (below at 2 to 4 of 10 to 12). Neither the full
    nor the partial rule is met.
  deviations:
  - As in fig9a-optimal-resolution. The spectrum classifier's PC and component counts are not given;
    the PCs for 90% (5 to 8) and 8 components are used.
- claim: fig10-vocalization-background
  outcome: reproduced
  assumed: true
  notebook: reproduce_sadeghi_2019_classifier.ipynb
  output: claim:fig10-vocalization-background
  measured: [93.3, 96.7, -20.5]
  notes: Under (6b)(7b) and reading (a) (one GMM per class), the spectro-temporal classifier is 93.3% for
    background and 96.7% for vocalizations at the full duration, vocalization accuracy rises from 81.7%,
    background stays within 87.4 to 94.1%, and the temporal classifier is 20.5 points below the
    spectro-temporal one on vocalizations averaged over durations (reading d; 23.3 at the full duration,
    reading c). Spectral beats temporal on the vocalizations at every duration (90.0 against 73.3% at the
    full duration) but at Bonferroni-corrected p < 0.01 (paired t test over the 60 vocalizations) at 1 of
    10 durations only, so that part holds weakly. Under (6a)(7b) reading (a) the values are 94.8 and
    98.3%, the difference -25.0 (c) and -24.3 (d) points. Under reading (b) (13-category decisions
    mapped to the class) the temporal classifier reaches 98.3% on vocalizations and the difference is
    -1.7 to -11.8 points. In the (6a)(7b) rows the spectral and temporal curves are at different
    optima (283 and 141 ms), and the per-duration tests pair them by index, not by duration; the
    (6b)(7b) rows are at the same optimum (141 ms).
  deviations:
  - As in fig9a-optimal-resolution. The class models use the 13-category classifier's PC and
    component counts.
'''
s=s[:a]+new+s[b:]
# figs10 notes
old=s[s.index('- claim: figs10-amua-tmua'):s.index('- claim: fig4-example-original-vs-equalized')]
s=s.replace(old,'''- claim: figs10-amua-tmua
  outcome: blocked
  blocked_by: data_missing
  notebook: reproduce_sadeghi_2019_neural.ipynb
  output: claim:figs10-amua-tmua
  notes: Thresholded MUA needs the raw voltage traces (events 2 SDs above the noise floor). The
    data set holds only the aMUA envelopes downsampled to 2034.5 Hz; the notebook lists every member
    of the tar (281 files, code, documents, sounds and the 35 neural files) and every field of the
    neural files (Data.Param with AnimalNo, BlockNo and RecordDate, and Data.Sound), and none holds
    voltage traces or spike times, so four of the six values cannot be computed. The two aMUA
    split-half values can and match. With the time halves of NeuralExample.m (first and second 1.5 s)
    the median r between halves of the stimulus-driven correlations is 0.980 spectral and 0.830
    temporal over the 65 paradigm 1 rasters (reading a; 0.980 and 0.842 over all 373 rasters, reading
    b), against 0.98 and 0.83; with odd and even trials as halves they are 0.996 and 0.986.
''')
open(p,'w').write(s)
EOF
date -u
```

```
Sat Nov 14 06:38:04 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/sadeghi-2019-01.yaml'
s=open(p).read()
def add_note(claim, text):
    global s
    i=s.index(f'- claim: {claim}\n')
    j=s.index('  notes:', i)
    k=s.find('\n  deviations:', j); k2=s.find('\n- claim:', j)
    end=min(x for x in (k,k2) if x>0)
    s=s[:end]+' '+text+s[end:]
add_note('fig1k-example-temporal-widths', 'The notebook now prints the lines of NeuralExample.m that set this window\n    (73 to 75, NS2 = floor(NS/2), sA = 1:NS2; 80, RASNMod = RASNA; 86 and 87, T0 at the centre and\n    TwMod = floor((NSMod - 2 MaxLag - 2)/Fsd 1000)).')
add_note('figs6-per-sound-above-chance', 'Under (1a)(2a) the snake temporal classifier without tonotopy is\n    significantly below chance (12%, p = 0.012), where the paper gives p = 0.92; the criterion asks only\n    that it is not above chance, so the outcome stands, and the notebook flags the difference.')
add_note('figs9-mixing-coefficient', 'With paradigm 2 a taken from the whole-response classifier (reading 3b)\n    no combination passes (pooled medians 0.35 to 0.60, paradigm 3 0.00 to 0.90). The passing reading\n    sits at the edge of the tolerance and the per-site values spread from 0.0 to 1.0 (printed), so the\n    outcome is fragile.')
add_note('fig4-example-original-vs-equalized', 'Lag 0 does not drive the high temporal r; without lag 0 it is\n    0.888, without lags within 5 ms 0.693 +/- 0.110 (inside 0.72 +/- 0.07) and without lags within 20 ms\n    0.661; per channel the median r is 0.952. Only the first of these is the claims file\'s measure.')
s=s.replace("outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig1k-example-temporal-widths","outcome: reproduced\n  assumed: true\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig1k-example-temporal-widths",1)
s=s.replace("outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:figs9-mixing-coefficient","outcome: reproduced\n  assumed: true\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:figs9-mixing-coefficient",1)
s=s.rstrip('\n')+'\n'
s+='''verifications:
- date: '2026-11-14'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
  reviewed: Round 1. The executed neural and model notebooks of the first run with the conclusion cells and
    the summary removed, the helpers sadeghi.py and model.py, and the claims file, with the paper. The
    verifier checked the archive's file list and data description and tested site_correlations, width_at,
    the decision helpers and the train and validation windows on synthetic inputs. It found no place
    where the claims file misreads the paper, so no question was added for a reader. Report in
    transcripts/sadeghi-2019/verifier-1-report.md. In reply the model classifier was built and run (a third
    notebook), the aMUA split-half values were computed, and the outputs asked for were added. The
    criticalbandwidth.m variant of fig7i (point 8) was added to the model notebook but could not be run in
    the time left and was removed again, so the model notebook's executed copy is that of the first run.
  results:
  - claim: fig1k-example-temporal-widths
    agrees: true
    outcome: reproduced
    reason: The code_half window with the channel-mean curve gives 10/11 within tolerance, and crowd and water
      are narrower than fire. The claims file's two window readings give at most 8/11, which would be
      partially reproduced. code_half comes from NeuralExample.m, which the verifier could not see (point 3).
    response: The notebook now prints the lines of NeuralExample.m that set the window (first half of the
      raster, T0 at its centre, TwMod = NSMod - 2 MaxLag - 2 samples), streamed from the deposit. The outcome
      is marked as resting on that reading.
  - claim: fig1-snr-noise-stronger
    agrees: true
    outcome: partially_reproduced
    reason: No reading gets both means and at least 3 of 4 bounds; several readings have both means within
      the SD tolerance and SNR mostly below 0 dB.
    response: No change.
  - claim: fig1-s5-model-predicts-neural
    agrees: true
    outcome: blocked
    reason: The data set has no tone-pip responses, so no best frequencies; a version with an assumed
      channel-to-frequency mapping would need an assumption the paper does not make.
    response: The data check now lists every tar member and every field of the neural files (Data.Param holds
      only AnimalNo, BlockNo and RecordDate), which confirms the block.
  - claim: fig2-noise-restricted
    agrees: true
    outcome: reproduced
    reason: Noise width at 50% is narrower for 5/5 sounds in both domains under every window, and the SD
      across sounds is lower for noise.
    response: No change.
  - claim: fig3a-example-tonotopy-removal
    agrees: true
    outcome: partially_reproduced
    reason: No reading has both values in tolerance; the drop is at least 20 points under every reading.
    response: No change.
  - claim: fig3a-example-classifier-order
    agrees: true
    outcome: partially_reproduced
    reason: The order holds under some readings; the noiseless rule fails under every reading, noiseless
      temporal being 15 to 20 points below single-trial. With a chosen on model data the noiseless
      spectro-temporal classifier uses in-sample log-likelihoods, a sign of a degenerate choice (point 7).
    response: No change; point 7 is noted, and the noiseless rule fails on the temporal classifier under every
      choice of a.
  - claim: fig3b-population-above-chance
    agrees: true
    outcome: reproduced
    reason: Under every reading all four classifiers are above 20%, 1 s beats 62.5 ms, and the tonotopy drop
      is 25 to 32 points.
    response: No change.
  - claim: figs6-per-sound-above-chance
    agrees: true
    outcome: reproduced
    reason: 18/18 other conditions are above chance and snake temporal is not; snake without tonotopy is
      significantly below chance (p = 0.012) where the paper has p = 0.92, which the notebook does not flag
      (point 5).
    response: The notebook now flags snake conditions significantly below chance, and the notes say so.
  - claim: figs9-mixing-coefficient
    agrees: true
    outcome: reproduced
    reason: Reproduced but fragile; only 1 of 16 reading combinations passes, at the tolerance edge, and
      paradigm 2's a was taken only from reading (3)(a) (point 4).
    response: Reading (3)(b) for paradigm 2 is now run (no combination passes with it) and the per-site values
      are printed; the outcome is kept, marked as resting on an assumption, and the notes say it is fragile.
  - claim: figs10-amua-tmua
    agrees: true
    outcome: blocked
    reason: tMUA needs raw voltages, which are absent; the two aMUA split-half values (0.98, 0.83) could have
      been tested (point 2).
    response: The aMUA split-half values are now computed (0.980 and 0.830 with time halves over the paradigm 1
      rasters, within tolerance); the claim stays blocked as four of its six values need tMUA.
  - claim: fig4-example-original-vs-equalized
    agrees: true
    outcome: not_reproduced
    reason: Spectral 0.93 is in tolerance; temporal 0.88 to 0.90 against 0.72 is outside both the tolerance
      and 10% under every reading. Whether lag 0 drives the 0.90 could not be checked.
    response: Temporal r without lag 0, without lags within 5 and 20 ms, and per channel are now printed; lag 0
      does not drive it (0.888 without it). No change of outcome.
  - claim: fig4e-population-original-vs-equalized
    agrees: true
    outcome: not_reproduced
    reason: 0/4 values in tolerance under every reading; same-sound beats across-sound, but the temporal values
      are more than 10% off, so the partial rule fails.
    response: No change.
  - claim: fig4f-example-equalized-classification
    agrees: true
    outcome: partially_reproduced
    reason: The one reading with 4/4 in tolerance has the 1/f spectrum classifier at 31%, not below 30%; the
      pattern holds under other readings. The within-site z test of reading (b) treats overlapping windows
      as independent (point 6).
    response: No change; the outcome does not use that test, as the notes say.
  - claim: fig4h-population-equalized-classification
    agrees: true
    outcome: partially_reproduced
    reason: At most 3/5 values in tolerance; the t tests pass and the spectrum classifier is lowest on 1/f
      under every reading.
    response: No change.
  - claim: fig8b-example-pca-variance
    agrees: true
    outcome: reproduced
    reason: Reading b_st1000 gives 96.3% and 85.3 to 85.5%; nearest-centroid accuracy 88.6% and 85.6%.
    response: No change.
  - claim: fig8e-example-categorization
    agrees: true
    outcome: reproduced
    reason: Under every reading all three correlation classifiers are at least 90% at 1 s, rise from 62.5 ms,
      and the spectrum classifier is 91 to 94%.
    response: No change.
  - claim: fig8f-population-categorization
    agrees: true
    outcome: reproduced
    reason: 4/4 in tolerance, p < 1e-11 against 33.3%, and every classifier rises with duration, under every
      reading.
    response: No change.
  - claim: fig5-speech-water-widths
    agrees: true
    outcome: reproduced
    reason: Readings (ii)(a)(iii)(a) give speech 64.5 ms and water 4.0 ms; spectral breadth 0.464 against
      0.259.
    response: No change.
  - claim: fig6-category-half-widths
    agrees: true
    outcome: reproduced
    reason: 4/5 in tolerance (cat 160.9 against 117.3 is out) and every vocalization is wider than water and
      wind; single bird songs' spectral breadth is below wind's, which the criterion does not test.
    response: No change.
  - claim: fig6c-category-diversity
    agrees: true
    outcome: reproduced
    reason: Reading (c), norms not squared, gives 5/6 in tolerance; speech is lowest of the 13 categories and
      white noise lowest overall.
    response: No change.
  - claim: fig7i-stationarity
    agrees: true
    outcome: not_reproduced
    reason: Environmental 0.65 to 0.79 against 0.49 and vocalizations 0.36 to 0.62 against 0.28 under every
      reading; the criterion has no partial clause. Whether the code's bandwidth formula would close the gap
      is untested (point 8).
    response: The criticalbandwidth.m variant was written but not run, for lack of time in this round; no
      change.
  - claim: fig9a-optimal-resolution
    agrees: false
    outcome: blocked
    reason: The too_large blocking is not supported; the notebook's own estimate is 56 to 115 min, no time
      limit is cited, and the estimate overcounts, since in leave-one-sound-out only the held-out sound's
      category model changes per fold. The claims are testable and were not run (point 1).
    response: The classifier was built, with one fit per category plus one refit per held-out sound, and run in
      reproduce_sadeghi_2019_classifier.ipynb (38 min). The outcome changed from blocked to reproduced under
      readings (6b)(7b).
  - claim: fig9b-similar-maximum
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; reproduced under the (7b) readings.
  - claim: fig9b-accumulation-rate
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; partially reproduced (the order holds, the values do not).
  - claim: fig9c-time-averaged-worse
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; partially reproduced (the running-average reading is 15 to 37 points lower, not 25).
  - claim: fig9e-category-specific
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; partially reproduced (3 of 4 values; waves better spectral, wind better temporal).
  - claim: fig9-spectrum-classifier-lower
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; not reproduced (the spectrum classifier matches the temporal one at the full duration).
  - claim: fig10-vocalization-background
    agrees: false
    outcome: blocked
    reason: As for fig9a-optimal-resolution, testable and not run.
    response: Tested; reproduced under (6b)(7b), reading (a).
'''
open(p,'w').write(s)
EOF
python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -8; date -u
```

```
0 error(s)
Sat Nov 14 06:38:52 UTC 2026
```

**Agent**

Record written and the check passes. Now the conclusion cells in the notebooks (markdown only, so the executed outputs still match the code).

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import nbformat as n
p='reproduce_sadeghi_2019_classifier.ipynb'
nb=n.read(p,as_version=4)
R={
'claim:fig9a-optimal-resolution':"**Result: under readings (6b)(7b) the spectral and temporal classifiers are best at 141 ms and the spectro-temporal classifier at 100 ms, as reported; under the other readings the optima move to neighbouring or further grid points (spectral 283 ms under (6a)(7b), spectro-temporal 283 ms under (7a)), as the accuracy curves over resolution are flat. Every correlation classifier is above 7.69% at every resolution under every reading (lowest 58.5%, largest Bonferroni p 1.3e-31 over sounds).**",
'claim:fig9b-similar-maximum':"**Result: at their optima and the full duration the three classifiers are within tolerance under every reading ((6b)(7b) spectro-temporal 81.5, spectral 82.1, temporal 80.5%) and no pair differs under the (7b) readings (p 0.43 to 0.90); under (6a)(7a) the spectro-temporal classifier reaches 87.7% and differs from the temporal one (p = 0.04 over sounds).**",
'claim:fig9b-accumulation-rate':"**Result: no reading puts the three rise times within tolerance; under (6b)(7b) with interpolation the spectral classifier needs 1.92 s, the temporal 2.67 s and the spectro-temporal 1.23 s. The order spectro-temporal < spectral < temporal holds under the (7b) readings and (6a)(7a) for every measure, not under (6b)(7a).**",
'claim:fig9c-time-averaged-worse':"**Result: time-averaged category models (reading a) are only 5.1 to 5.6 points below the short-term classifier; scoring the running average of the test sound under the short-term models (reading b) is 15.4 to 36.9 points lower. No reading gives 25 +/- 2.5; the reduction is at least 10 points under reading (b) only.**",
'claim:fig9e-category-specific':"**Result: waves are identified by spectral correlations (100%) far better than by temporal ones (33.3 to 40%), and wind by temporal (80%) better than by spectral ones (33.3 to 40%), under every reading; three of four values are within tolerance at best, wind spectral (33.3%) being below 47 +/- 6.7%.**",
'claim:fig9-spectrum-classifier-lower':"**Result: the spectrum classifier varies by 9.7 to 10.3 points over resolution, is best at 25 or 50 ms (80.0 to 80.5%), and is not below all three correlation classifiers at the full duration under any reading; it is above the temporal classifier at most durations.**",
'claim:fig10-vocalization-background':"**Result: under (6b)(7b) with one model per class, the spectro-temporal classifier is 93.3% on background and 96.7% on vocalizations at the full duration, vocalizations rise from 81.7% while background stays within 87.4 to 94.1%, and the temporal classifier is 20.5 points below the spectro-temporal one on vocalizations averaged over durations; spectral beats temporal on vocalizations at every duration but at Bonferroni p < 0.01 at 1 of 10 durations only. In the (6a)(7b) rows the spectral and temporal curves come from different optima and the per-duration tests pair them by index.**",
}
cells=[]
for c in nb.cells:
    cells.append(c)
    t=(c.metadata.get('tags') or [''])[0]
    if t in R: cells.append(n.v4.new_markdown_cell(R[t]))
nb.cells=cells
s=[c for c in nb.cells if c.source.startswith('## Summary')][0]
s.source='''## Summary

| Claim | Outcome |
|---|---|
| fig9a-optimal-resolution | reproduced under (6b)(7b) (141, 141 and 100 ms) |
| fig9b-similar-maximum | reproduced under the (7b) readings |
| fig9b-accumulation-rate | partially reproduced (order holds, times do not) |
| fig9c-time-averaged-worse | partially reproduced (15 to 37 points lower under reading b, not 25) |
| fig9e-category-specific | partially reproduced (3 of 4 values) |
| fig9-spectrum-classifier-lower | not reproduced |
| fig10-vocalization-background | reproduced under (6b)(7b), reading (a) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's: the deposit has no classifier code, so the classifier
follows the Methods, with these choices of its own: the spectro-temporal feature vector is the
spectral and temporal features side by side; PCA is fitted once on all sounds (refitting it per
fold changed 1 of 26 tested decisions); training observations are subsampled to 10000 per
category; the spectrum classifier uses the PCs for 90% and 8 components; the time-averaged
classifier of Fig 9C is not described and two readings are run; the cross-validated choice of
N_c was run at the optima only, on a subset of 1 to 20. PCs explaining 90% at 141 ms are 26
(spectral) and 8 (temporal), the paper's counts, and the cross-validated N_c of the spectral and
spectro-temporal classifiers (at 141 ms, 13 for spectro-temporal) match the reported ones where
tested. What was found about the dataset: the 195 model sounds are all there and suffice for the
classifier.'''
n.write(nb,p)
EOF
date -u
```

```
Sat Nov 14 06:39:13 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import nbformat as n
p='reproduce_sadeghi_2019_classifier.ipynb'
nb=n.read(p,as_version=4)
s=[c for c in nb.cells if c.source.startswith('## Summary')][0]
s.source=s.source.replace('''the paper's counts, and the cross-validated N_c of the spectral and
spectro-temporal classifiers (at 141 ms, 13 for spectro-temporal) match the reported ones where
tested.''','''the paper's counts; the cross-validated N_c of the spectro-temporal
classifier (13 at 141 ms) matches the reported one, those of the spectral (3 at 283 ms) and
temporal (20 at 141 ms) classifiers do not.''')
n.write(nb,p)
# neural: figs10 result + summary row + figs6/figs9/fig4 sentences
p='reproduce_sadeghi_2019_neural.ipynb'
nb=n.read(p,as_version=4)
for c in nb.cells:
    if c.cell_type=='markdown' and c.source=='**Result: (filled in after the run)**':
        c.source="**Result: the aMUA split-half reliability matches the paper: with the time halves of NeuralExample.m the median r between halves is 0.980 for spectral and 0.830 for temporal correlations over the 65 paradigm 1 rasters (0.980 and 0.842 over all 373), against 0.98 and 0.83; with odd and even trials as halves it is higher (0.996 and 0.986). The tMUA values cannot be computed from the data set, so the claim stays blocked.**"
s=[c for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('## Summary')][0]
print(s.source[:2500])
n.write(nb,p)
EOF
```

```
## Summary

| Claim | Outcome |
|---|---|
| fig1k-example-temporal-widths | reproduced (code's window; 6 to 8 of 11 under the claims file's windows) |
| fig1-snr-noise-stronger | partially reproduced (means hold, range bounds do not) |
| fig1-s5-model-predicts-neural | blocked, data missing |
| fig2-noise-restricted | reproduced |
| fig3a-example-tonotopy-removal | partially reproduced |
| fig3a-example-classifier-order | partially reproduced |
| fig3b-population-above-chance | reproduced |
| figs6-per-sound-above-chance | reproduced |
| figs9-mixing-coefficient | reproduced under one reading of many |
| figs10-amua-tmua | blocked, data missing |
| fig4-example-original-vs-equalized | not reproduced |
| fig4e-population-original-vs-equalized | not reproduced |
| fig4f-example-equalized-classification | partially reproduced |
| fig4h-population-equalized-classification | partially reproduced |
| fig8b-example-pca-variance | reproduced |
| fig8e-example-categorization | reproduced |
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; PY=executed/sadeghi-2019/.venv/bin/python; $PY - <<'EOF'
import nbformat as n
p='reproduce_sadeghi_2019_neural.ipynb'
nb=n.read(p,as_version=4)
s=[c for c in nb.cells if c.cell_type=='markdown' and c.source.startswith('## Summary')][0]
s.source=s.source.replace('| figs9-mixing-coefficient | reproduced under one reading of many |','| figs9-mixing-coefficient | reproduced under one reading of many, at the tolerance edge (fragile) |')
s.source=s.source.replace('| figs10-amua-tmua | blocked, data missing |','| figs10-amua-tmua | blocked, data missing (tMUA); the two aMUA split-half values match |')
# figs6 / figs9 / fig4 result sentences
for c in nb.cells:
    if c.cell_type!='markdown' or not c.source.startswith('**Result:'): continue
    if 'snake' in c.source and 'non-snake' in c.source or ('18 of the 18' in c.source):
        c.source=c.source.rstrip('*').rstrip()+' Under (1a)(2a) the snake temporal classifier without tonotopy is significantly below chance (12%, p = 0.012), where the paper gives p = 0.92.**'
    elif c.source.startswith('**Result: the medians of a depend strongly'):
        c.source=c.source.rstrip('*').rstrip()+' With paradigm 2 a from the whole-response classifier (3b) no combination passes, and the per-site values spread from 0.0 to 1.0.**'
    elif c.source.startswith('**Result: at the example site the spectral correlations of original'):
        c.source=c.source.rstrip('*').rstrip()+' Lag 0 does not drive the temporal value (0.888 without it); without lags within 5 ms it is 0.693.**'
n.write(nb,p)
for c in nb.cells:
    if c.cell_type=='markdown' and c.source.startswith('**Result:') and ('0.012' in c.source or '3b' in c.source or '0.888' in c.source): print(c.source[-250:],'\n')
# model notebook: markdown only
p='reproduce_sadeghi_2019_model.ipynb'
nb=n.read(p,as_version=4)
h=nb.cells[0]
for l in [l for l in h.source.splitlines() if l.startswith('| fig9') or l.startswith('| fig10')]:
    cid=l.split('|')[1].strip()
    h.source=h.source.replace(l, f'| {cid} | in reproduce_sadeghi_2019_classifier.ipynb |')
for c in nb.cells:
    if c.cell_type=='markdown' and c.source.startswith('**Result: the leave-one-sound-out classifier needs'):
        c.source="**Result: this cost estimate is from the first round. In round 2 the classifier was built with one fit per category plus one refit per held-out sound (only the held-out sound's category model changes in a fold), and runs in reproduce_sadeghi_2019_classifier.ipynb, where the seven classification claims are tested.**"
    if c.cell_type=='markdown' and c.source.startswith('## Summary'):
        c.source=c.source.replace('| fig9a, fig9b (two), fig9c, fig9e, fig9 spectrum, fig10 | blocked, too large for this run |','| fig9a, fig9b (two), fig9c, fig9e, fig9 spectrum, fig10 | tested in reproduce_sadeghi_2019_classifier.ipynb |')
n.write(nb,p)
EOF
cd  git diff --stat entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb; date -u
```

```
ions do not. Under the (1b) readings 16 to 18 of 18 exceed chance but a snake temporal condition does too. Under (1a)(2a) the snake temporal classifier without tonotopy is significantly below chance (12%, p = 0.012), where the paper gives p = 0.92.** 

 correlations agree more closely than reported (r = 0.898 +/- 0.022 against 0.72 +/- 0.07), outside the tolerance and outside 10% under every reading. Lag 0 does not drive the temporal value (0.888 without it); without lags within 5 ms it is 0.693.** 

 are 0.80 to 0.90; with a chosen on the validation data and the (1a) readings, the paradigm 3 medians are 0.00 to 0.40. With paradigm 2 a from the whole-response classifier (3b) no combination passes, and the per-site values spread from 0.0 to 1.0.** 

 .../sadeghi-2019/reproduce_sadeghi_2019_model.ipynb  | 20 ++++++++++----------
 1 file changed, 10 insertions(+), 10 deletions(-)
Sat Nov 14 06:39:37 UTC 2026
```

**Agent calls Bash**

```bash
cd  executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import json
nb=json.load(open('executed/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code' and 'figs9' in str(c['metadata'].get('tags')):
        out=''.join(''.join(o.get('text','')) for o in c['outputs'])
        for l in out.splitlines():
            if '(3b)' in l: print(l[:400])
EOF
```

```
1a2a P2 (3b) a on (a) data: P1 median 0.50, P2 median 0.40, pooled 24 sites median 0.50 (quartiles 0.20, 0.60) | P3 (a) median 0.90 (25th pct 0.85); pooled rule False, per-paradigm rule False | P3 (b) median 0.80 (25th pct 0.80); pooled rule False, per-paradigm rule False
1a2a P2 (3b) a on (b) data: P1 median 0.70, P2 median 0.70, pooled 24 sites median 0.70 (quartiles 0.40, 0.80) | P3 (a) median 0.40 (25th pct 0.40); pooled rule True, per-paradigm rule True | P3 (b) median 0.30 (25th pct 0.15); pooled rule False, per-paradigm rule False
1a2b P2 (3b) a on (a) data: P1 median 0.60, P2 median 0.50, pooled 24 sites median 0.60 (quartiles 0.47, 0.70) | P3 (a) median 0.90 (25th pct 0.85); pooled rule False, per-paradigm rule False | P3 (b) median 0.90 (25th pct 0.80); pooled rule False, per-paradigm rule False
1a2b P2 (3b) a on (b) data: P1 median 0.50, P2 median 0.10, pooled 24 sites median 0.35 (quartiles 0.18, 0.60) | P3 (a) median 0.20 (25th pct 0.00); pooled rule False, per-paradigm rule False | P3 (b) median 0.00 (25th pct 0.00); pooled rule False, per-paradigm rule False
1b2a P2 (3b) a on (a) data: P1 median 0.50, P2 median 0.40, pooled 24 sites median 0.40 (quartiles 0.30, 0.53) | P3 (a) median 0.80 (25th pct 0.70); pooled rule False, per-paradigm rule False | P3 (b) median 0.80 (25th pct 0.80); pooled rule False, per-paradigm rule False
1b2a P2 (3b) a on (b) data: P1 median 0.80, P2 median 0.40, pooled 24 sites median 0.65 (quartiles 0.30, 0.80) | P3 (a) median 0.50 (25th pct 0.25); pooled rule True, per-paradigm rule False | P3 (b) median 0.30 (25th pct 0.20); pooled rule False, per-paradigm rule False
1b2b P2 (3b) a on (a) data: P1 median 0.60, P2 median 0.50, pooled 24 sites median 0.60 (quartiles 0.47, 0.70) | P3 (a) median 0.90 (25th pct 0.85); pooled rule False, per-paradigm rule False | P3 (b) median 0.90 (25th pct 0.80); pooled rule False, per-paradigm rule False
1b2b P2 (3b) a on (b) data: P1 median 0.50, P2 median 0.10, pooled 24 sites median 0.35 (qua
[... 1 more lines not kept]
```

**Agent**

I misstated the figs9 result: under reading 3b two combinations pass, one of them under the per-paradigm rule too. Correcting the note and the notebook sentence.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/sadeghi-2019-01.yaml'
s=open(p).read()
old='''With paradigm 2 a taken from the whole-response classifier (reading 3b)
    no combination passes (pooled medians 0.35 to 0.60, paradigm 3 0.00 to 0.90). The passing reading
    sits at the edge of the tolerance and the per-site values spread from 0.0 to 1.0 (printed), so the
    outcome is fragile.'''
assert old in s
s=s.replace(old,'''With paradigm 2 a taken from the whole-response classifier (reading 3b)
    two more combinations pass, (1a)(2a) with a on the validation data (pooled median 0.70, paradigm 2
    0.70, paradigm 3 0.40, which also meets the per-paradigm rule) and (1b)(2a) on the validation data
    (pooled 0.65, paradigm 3 0.50); the other 14 combinations with 3b do not. The passing medians sit at
    the edge of the tolerance and the per-site values spread from 0.0 to 1.0 (printed), so the outcome
    depends on how a is chosen.''')
s=s.replace('''    response: Reading (3)(b) for paradigm 2 is now run (no combination passes with it) and the per-site values
      are printed; the outcome is kept, marked as resting on an assumption, and the notes say it is fragile.''','''    response: Reading (3)(b) for paradigm 2 is now run (2 of its 16 combinations pass, one also per paradigm)
      and the per-site values are printed; the outcome is kept, marked as resting on an assumption (a chosen
      on the validation data), and the notes say it depends on that choice.''')
open(p,'w').write(s)
EOF
executed/sadeghi-2019/.venv/bin/python - <<'EOF'
import nbformat as n
p='entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb'
nb=n.read(p,as_version=4)
for c in nb.cells:
    if c.cell_type=='markdown' and 'With paradigm 2 a from the whole-response classifier (3b) no combination passes' in c.source:
        c.source=c.source.replace('With paradigm 2 a from the whole-response classifier (3b) no combination passes, and the per-site values spread from 0.0 to 1.0.','With paradigm 2 a from the whole-response classifier (3b), two combinations pass with a chosen on the validation data ((1a)(2a): pooled 0.70, paradigm 3 0.40, also per paradigm; (1b)(2a): pooled 0.65, paradigm 3 0.50), and the per-site values spread from 0.0 to 1.0.')
n.write(nb,p)
EOF
date -u
```

```
Sat Nov 14 06:39:53 UTC 2026
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019; python - <<'EOF'
s=open('README.md').read()
s=s.replace('| aMUA against thresholded MUA (S10 Fig) | Blocked: data missing |','| aMUA against thresholded MUA (S10 Fig) | Blocked: data missing (the aMUA split-half values match) |')
s=s.replace('| Model classifiers (Figs 9 and 10, seven claims) | Blocked: too large for the run |','''| Model, optimal resolution 141 and 100 ms (Fig 9A) | Reproduced (one reading) |
| Model, similar maximum performance (Fig 9B) | Reproduced |
| Model, accumulation rate (Fig 9B) | Partially reproduced |
| Model, time-averaged classifier worse (Fig 9C) | Partially reproduced |
| Model, waves spectral and wind temporal (Fig 9E) | Partially reproduced |
| Model, spectrum classifier lower (Fig 9) | Not reproduced |
| Model, vocalization against background (Fig 10) | Reproduced (one reading) |''')
s=s.replace('The neural notebook takes about 35 to 55 minutes, the model notebook about 15 to 25, depending on the machine.','The neural notebook takes about 35 to 60 minutes, the model notebook about 15 to 25 and the model classifier notebook about 40, depending on the machine.')
open('README.md','w').write(s)
EOF
sed -n 30,60p README.md; cd ../..; python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -5; date -u
```

```
| Model, category diversity index (Fig 6C) | Reproduced |
| Model, stationarity index (Fig 7I) | Not reproduced |
| Model, optimal resolution 141 and 100 ms (Fig 9A) | Reproduced (one reading) |
| Model, similar maximum performance (Fig 9B) | Reproduced |
| Model, accumulation rate (Fig 9B) | Partially reproduced |
| Model, time-averaged classifier worse (Fig 9C) | Partially reproduced |
| Model, waves spectral and wind temporal (Fig 9E) | Partially reproduced |
| Model, spectrum classifier lower (Fig 9) | Not reproduced |
| Model, vocalization against background (Fig 10) | Reproduced (one reading) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set is one 5.3 GB tar.gz file; the notebooks stream it once and parse each member in
memory. The neural notebook takes about 35 to 60 minutes, the model notebook about 15 to 25 and the model classifier notebook about 40, depending on the machine. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/sadeghi-2019-01.yaml`](../../attempts/sadeghi-2019-01.yaml).
0 error(s)
Sat Nov 14 06:40:17 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
for i,l in enumerate(open('attempts/sadeghi-2019-01.yaml'),1):
    body=re.sub(r'^\s*-?\s*[a-z_]+: ','',l.rstrip('\n'),count=1)
    if ': ' in body and not body.strip().startswith(('-', "'")): print(i,l.rstrip()[:150])
    if '—' in l or 'rather' in l: print('STYLE',i,l[:120])
EOF
python -c "import yaml;yaml.safe_load(open('attempts/sadeghi-2019-01.yaml'))" && echo yaml-ok
```

```
yaml-ok
```

**Agent**

Adding one finding for the paper's authors about the classifier choices the Methods leave open, then a final check.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/sadeghi-2019-01.yaml'
s=open(p).read()
i=s.index('verifications:')
add='''- kind: methods_unavailable
  statement: For the authors. The deposit holds no code for the model classifier of Figs 9 and 10, and
    the Methods leave open how the spectro-temporal feature vector is formed (taken here as the spectral
    and temporal features side by side), how the test windows are spaced (tau_W or the full Kaiser
    window), whether the PC and component counts were refitted at each resolution, and how the
    time-averaged classifier of Fig 9C was built. The optimal resolutions and the Fig 9C reduction change
    with these choices (spectro-temporal optimum 100 to 283 ms; reduction 5 to 37 points). Which were
    used?
'''
s=s[:i]+add+s[i:]
open(p,'w').write(s)
EOF
python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -3; git status --short | grep -v "^??"; date -u
```

```
0 error(s)
 M attempts/sadeghi-2019-01.yaml
 M entries/sadeghi-2019/README.md
 M entries/sadeghi-2019/entry.yaml
 M entries/sadeghi-2019/model.py
 M entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb
 M entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb
 M entries/sadeghi-2019/sadeghi.py
 M tools/build_site.py
 M tools/entry.py
 M tools/site_assets/app.css
 M tools/site_assets/list.js
Sat Nov 14 06:40:36 UTC 2026
```

**Agent**

## Round-1 revision of sadeghi-2019-01

**The run.** I ran `python tools/entry.py all`, but it hit the tool's 2-hour limit before it finished. The classifier notebook (38 min) and the neural notebook (59 min) both completed, and both executed copies have no errors. The model notebook was cut off mid-run. With too little time left to re-run it, I restored its code to the committed version, so its executed copy from the first run still matches the code. I changed only its markdown.

Two consequences:
- **No stamp.** I wrote the conclusion cells after the run, so there is no clean-run stamp, and the next `run` will execute all three notebooks.
- **Classifier notebook timing.** It is about 40 minutes.

`tools/entry.py check` passes.

**What changed in the outcomes.** The verifier was right that the seven model-classifier claims were testable (B1). I built the classifier as a third notebook, `reproduce_sadeghi_2019_classifier.ipynb`. Only the held-out sound's category is refitted in each fold, as the verifier suggested. The seven claims are now tested:

| Claim | Outcome | Key numbers |
|---|---|---|
| fig9a, optimal resolution | reproduced, rests on readings (6b)(7b) | optima 141, 141 and 100 ms; other readings move them |
| fig9b, similar maximum | reproduced under the (7b) readings | 81.5, 82.1 and 80.5%; under (6a)(7a) one pair differs, p = 0.04 |
| fig9b, accumulation rate | partially reproduced | the order holds, the rise times do not |
| fig9c, time-averaged worse | partially reproduced | 15 to 37 points lower under reading (b), 5 under (a), never 25 |
| fig9e, category-specific | partially reproduced | 3 of 4 values; waves better spectral, wind better temporal |
| fig9, spectrum classifier lower | not reproduced | it matches the temporal classifier at the full duration |
| fig10, vocalization vs background | reproduced, rests on (6b)(7b), reading (a) | 93.3, 96.7 and −20.5; the spectral advantage is significant at only 1 of 10 durations |

At 141 ms, the PCs that explain 90% of the variance are 26 spectral and 8 temporal, the paper's counts.

None of the 21 neural and model-correlation outcomes changed. fig1k and figs9 are now marked as resting on an assumption.

**What I added or corrected in reply to the report.**
- **B2:** the aMUA split-half values for figs10 are now computed: 0.980 and 0.830, against the paper's 0.98 and 0.83. The claim stays blocked, because four of its six values need thresholded MUA, which needs raw voltages the data set lacks.
- **B3:** the fig1k cell now prints the window lines of NeuralExample.m, read from the deposit.
- **C:** the data check now lists every tar member and every field of the neural files. Only AnimalNo, BlockNo and RecordDate exist, which confirms both data_missing blocks.
- **B4:** figs9 now runs paradigm 2 reading (3b) and prints every site's a. Two more combinations pass, so I kept the outcome and noted that it depends on how a is chosen.
- **B5:** the notebook now flags the snake condition without tonotopy as significantly below chance (p = 0.012, against the paper's 0.92).
- **fig4 (C):** temporal r is now printed without lag 0 (0.888), without lags within 5 ms (0.693), and per channel. Lag 0 does not drive the high value. The outcome is unchanged.
- **Record:** the round is recorded under `verifications`, the README and summaries are updated, and I added a methods_unavailable finding about the classifier choices the Methods leave open. No question for a reader was needed: the verifier found no misreading of the claims file.

**What I did not do.**
- **B8:** I wrote the bandwidth variant for fig7i (the code's formula, 94 + 71 f^1.5) but removed it again, because there was no time left to re-run the model notebook. The verifier marked this point as not affecting a conclusion.
- **N_c search:** the cross-validated choice of N_c ran only at each classifier's optimum, over a subset of the 1 to 20 grid (1, 2, 3, 5, 8, 13, 20).
- **fig10 index pairing:** in the (6a)(7b) rows of fig10, the per-duration spectral-against-temporal tests pair two different optima by index, not by duration. The notes say so, and the outcome rests on the (6b)(7b) rows, where both classifiers are at the same optimum.

## End of run

75 turns, 217 minutes, $8.43 at API prices, result: success.
