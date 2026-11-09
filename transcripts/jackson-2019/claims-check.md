# openneuro-ds002778 · claims-check · run 40593316544

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/openneuro-ds002778/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,260p docs/protocol.md
```

```
- `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/openneuro-ds002778/*.yaml; python tools/claims_check.py claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml"
}
```

```
1	# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
6	# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
7	# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
8	#
9	# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
10	# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
11	# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
12	# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
13	# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
14	# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
15	# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
16	# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
17	# effect sizes (Table 3) are not in the code.
18	#
19	# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset
20	# first published by George et al. (2013) and reanalysed by Swann et al. (2015). 15 PD patients (8
[... 585 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml paper/10.1523-eneuro.0151-19.2019.txt | tail -20; wc -c paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-eneuro.0151-19.2019.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/SwannLab/Jackson_2019 && cd Jackson_2019 && git log -1 --format='%H %ci' && ls
```

```
a7c89f50106aa4ccec76ace18bbfa45a5440545e 2020-05-19 16:15:36 -0500
Figure_1.ipynb
Figure_4.ipynb
Figures_2,3.ipynb
README.md
pac.py
shape.py
utils.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && cat shape.py pac.py utils.py
```

```
<persisted-output>
Output too large (45.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d579e979-0c7a-4638-a617-90edfda83dfe/tool-results/bqc5d1swg.txt

Preview (first 2KB):
"""
shape.py
Tools for quantifying the waveform shape of oscillations
"""

from __future__ import division
import numpy as np
import pac
#import pacpy #wasn't here before
from scipy import io
from scipy.signal import firwin2, firwin
from scipy.signal import filtfilt


"""
def filtandremove(x,rejects, f_osc, Fs=512., w=3, boundary=0):
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && grep -n "def \|firwin\|taps\|log\|boundary\|w=\|delete\|filtfilt\|sqrt\|np.mean\|np.std\|ranksums\|wilcoxon\|spearman" shape.py pac.py utils.py | head -150
```

```
shape.py:11:from scipy.signal import firwin2, firwin
shape.py:12:from scipy.signal import filtfilt
shape.py:16:def filtandremove(x,rejects, f_osc, Fs=512., w=3, boundary=0):
shape.py:19:    xn = firf(x, f_osc, Fs, w=w, rmvedge=False)
shape.py:22:    xn = np.delete(xn, rejects)
shape.py:26:def findpt(x, rejects, f_osc, Fs=512., w=3, boundary=0):
shape.py:41:    boundary : int
shape.py:55:    xn = firf(x, f_osc, Fs, w=w, rmvedge=False)
shape.py:58:    def fzerofall(data):
shape.py:64:    def fzerorise(data):
shape.py:99:    if boundary > 0:
shape.py:100:        Ps = _removeboundaryextrema(x, Ps, boundary)
shape.py:101:        Ts = _removeboundaryextrema(x, Ts, boundary)
shape.py:106:def _removeboundaryextrema(x, Es, boundaryS):
shape.py:108:    Remove extrema close to the boundary of the recording
shape.py:116:    boundaryS : int
shape.py:117:        Number of samples around the boundary to reject extrema
shape.py:122:        extremas that are not too close to boundary
shape.py:129:    # Reject extrema too close to boundary
shape.py:130:    SampLims = (boundaryS, nS - boundaryS)
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && sed -n 221,320p shape.py; sed -n 96,135p utils.py; sed -n 10,70p pac.py
```

```
def ex_sharp(x, Es, widthS, ampPC=0, Fs=512, fosc=(13, 30), method='diff'):
    """
    Calculate the sharpness of extrema

    Parameters
    ----------
    x : array-like 1d
        voltage time series
    Es : array-like 1d
        time points of oscillatory peaks or troughs
    widthS : int
        Number of samples in each direction around extrema to use for sharpness estimation
    ampPC : float (0 to 100)
        The percentile threshold of beta (or other oscillation) amplitude
        for which an extrema needs to be included in the analysis
    Fs : float
        Sampling rate
    fosc : (low, high), Hz
        The frequency range of the oscillation identified by the extrema

[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Jackson_2019 && sed -n 15,95p utils.py; python3 - <<'EOF'
import json
for nb in ['Figures_2,3.ipynb','Figure_4.ipynb','Figure_1.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for c in d['cells']:
        if c['cell_type']=='code':
            print('--- code'); print(''.join(c['source']))
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t: print('>>>', ''.join(t)[:600])
        else:
            print('--- md'); print(''.join(c['source'])[:400])
EOF
```

```
def loadmeta():
    """Load meta data for analysis of PD data.

    Returns
    -------
    Fs : float
        Sampling rate (Hz)
    t : numpy array
        time array corresponding to the eeg signals
    S : int
        Number of PD patients
    Sc : int
        Number of control subjects
    flo : 2-element tuple
        frequency limits of the beta range (Hz)
    fhi : 2-element tuple
        frequency limits for the high gamma range (Hz)
    """

    Fs = 512.  # Sampling rate (Hz)
[... 650 more lines not kept]
```

**Agent**

The checker passes and the code at the cited commit matches what the opening comment says about it. I'm making a few corrections now.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""#   (a) 3 cycles of 8 Hz, 192 taps (pacpy's default rule); (b) 231 taps as in the code for beta; (c)
#   118 samples as the Methods give for beta. Gamma 50 to 150 Hz as for beta.""",
"""#   (a) 3 cycles of 8 Hz, 192 taps (pacpy's default rule); (b) 231 taps as in the code for beta; (c)
#   118 samples as the Methods give for beta. Gamma 50 to 150 Hz as for beta. For the shape filter the
#   Methods' 231 ms (118 samples) for beta is a second reading.""")
rep("""    statistic: signed rank = 9
    p: 0.004
    n: 15 patients, on and off""","""    statistic: signed rank = 9
    p: 0.004
    corrected: none (FDR corrected p = 0.0121)
    n: 15 patients, on and off""")
rep("""    the three measures. The neighbour set is this file's reading of "sensorimotor".""",
"""    the three measures. The neighbour set and the condition on F7, F8, T7 and T8 are this file's
    reading of "sensorimotor"; the paper states neither.""")
rep("""    pwelch's default Hamming window), at C3 and C4, averaged over electrodes and participants of each
    group (off, on, controls). The paper does not define a peak.""",
"""    pwelch's default Hamming window), averaged over electrodes and participants of each group (off,
    on, controls). The paper does not say which electrodes the spectra use; the main reading is C3 and
    C4, from "as would be expected in sensorimotor EEG" (Results, paragraph 4), and the average over all
    scalp electrodes is a variant. The paper does not define a peak.""")
rep("""  criterion: As for fig2-sharpness-off-on with the band 8 to 12 Hz for zero crossings (192 taps by the
    code's 3-cycle rule), FDR over the six tests of Table 1.""",
"""  criterion: As for fig2-sharpness-off-on with the band 8 to 12 Hz for zero crossings, FDR over the six
    tests of Table 1. The alpha filter length is open; readings are 192 taps (the code's findpt rule,
    3 cycles of the low cutoff) and 118 samples (the Methods' 231 ms for beta).""")
rep("""  - quantity: patients with at least one electrode in Q4 both off and on
    value: 9
    tolerance: 1""","""  - quantity: patients with off and on in Q4 at both C3 and C4
    value: 8
    tolerance: 1
  - quantity: patients with at least one electrode in Q4 both off and on
    value: 9
    tolerance: 1""")
rep("""    all and Q4. Reproduced when, under one reading, d in Q4 patients exceeds d in all patients for all
    three measures; the Q4 values are compared to Table 3 within tolerance and reported. Partially
    reproduced when d increases for two of three.""",
"""    all and Q4. Reproduced when, under one reading, d in Q4 patients exceeds d in all patients for all
    three measures and the Q4 values are within tolerance of Table 3. Partially reproduced when d
    increases for all three with a value out of tolerance, or increases for two of three.""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-10-27
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment and table1-alpha-shape-off-on, the alpha shape filter length was given as the
    code's 3-cycle rule only, but the code holds no alpha analysis; added the Methods' 231 ms (118
    samples) as a second reading.
  - fig2-steepness-off-on, recorded the uncorrected p as uncorrected (corrected none, FDR 0.0121), as
    for the sharpness claim (Table 1).
  - fig2c-topography-sensorimotor, the condition that F7, F8, T7 and T8 are not significant is not in
    the paper; marked as this file's reading with the neighbour set.
  - fig1c-beta-alpha-peaks, the criterion fixed C3 and C4 without saying the paper does not name the
    electrodes of the spectra; named it as open, C3 and C4 the main reading (Results, paragraph 4) and
    all scalp electrodes a variant.
  - q4-patient-counts, the statement gives eight patients with both electrodes in Q4 but expected
    lacked it; added (Results, Waveform shape, paragraph 2).
  - table3-q4-effect-size, the Table 3 values were only reported and did not count towards the
    outcome; full reproduction now needs them within tolerance.
  - Checked the code claims of the opening comment against SwannLab/Jackson_2019 at a7c89f5
    (findpt, ex_sharp, rd_steep, measure_shape, measure_pac, ozkurt, the notebook outputs for Tables
    1 and 2, Figure 3 and Cohen's d); they hold.
  - Open, Table 2 prints FDR p = 1 for the three non-significant tests where Benjamini-Hochberg over
    the six gives about 0.36 (Table 1 matches BH); no outcome depends on it.
  - Open, Table 3 gives d = 0.75 for PAC in all patients and Table 1 gives 0.83 (raw PAC in the code);
    the log10 reading of the Methods likely explains 0.75 but the paper does not say so.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml paper/10.1523-eneuro.0151-19.2019.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file holds up well against the paper and is ready for an attempt. I made six small corrections and left two discrepancies open.

**Checker:** `24 claims, 23 quotes, 29 statistical values, 0 problems`, both before and after my edits.

**What holds up:**
- I checked all 24 claims against the text and Tables 1 to 3.
- I cloned the paper's code (`SwannLab/Jackson_2019` at commit `a7c89f5`) and checked the opening comment's description of it. It is accurate: the filter tap counts, the sharpness and steepness functions, how artifact marks are applied, the PAC formula, the Wilcoxon p-value method, and the Cohen's d formula. The code's printed values match the paper's Tables 1 and 2 and its Figure 3 correlations.
- The six-test multiple-comparison correction for Table 1 reproduces the printed corrected p-values.
- Every main finding has a claim.

**Changes, by claim:**
- **table1-alpha-shape-off-on** (and the opening comment): the alpha filter length was given only as the code's 3-cycle rule (192 taps), but the code holds no alpha analysis. I added the Methods' 231 ms for beta (118 samples) as a second reading.
- **fig2-steepness-off-on:** the uncorrected p is now labelled uncorrected, with its corrected value, as in the sharpness claim.
- **fig2c-topography-sensorimotor:** the paper does not say that F7, F8, T7 and T8 must be non-significant. I marked that condition, like the set of neighbouring electrodes, as this file's own reading.
- **fig1c-beta-alpha-peaks:** the paper does not say which electrodes the power spectra use. I marked this as open: C3 and C4 is the main reading ("as would be expected in sensorimotor EEG"), and all scalp electrodes is a variant.
- **q4-patient-counts:** the statement says eight patients have both electrodes in quadrant 4, but that number was missing from the expected values. I added it.
- **table3-q4-effect-size:** the Table 3 effect sizes were only to be reported and did not affect the outcome. Full reproduction now requires them to be within tolerance.

**Open:**
- Table 2 prints a corrected p of 1 for its three non-significant tests. The standard correction (Benjamini-Hochberg) over its six tests gives about 0.36. No outcome depends on this.
- For PAC in all patients, Table 3 gives an effect size of 0.75 and Table 1 gives 0.83 (0.83 is what the code computes on raw PAC). Computing it on log PAC, as the Methods say, probably explains 0.75, but the paper does not say so. The criterion already accepts either reading.

**Ready:** yes. The check entry is recorded under `checks` with `ready: true`. Nothing is committed.

## End of run

13 turns, 2 minutes, result: success.
