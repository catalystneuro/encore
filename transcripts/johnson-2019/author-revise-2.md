# crcns-fcx-3 · author-revise-2 · run 42543118671

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-fcx-3/verifier-2-report.md; ls entries/crcns-fcx-3-johnson-2019 entries/crcns-fcx-3-johnson-2019/*
```

```
Mon Nov  9 01:04:34 UTC 2026
**Verifier report, round 2: Johnson et al. 2019 on CRCNS fcx-3**

Cell numbers are 0-based positions in the executed `.ipynb`; the layout has changed since round 1. The claims file has 17 claims and the attempt record has 17 outcomes. Outside the notebook I ran one check of my own: a synthetic test of the PSI null in `$TMPDIR`, using no dataset files. It is described under fig4c.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| table1-electrodes | partial | Yes. 187 channels and 1135 pairs (cell 17). |
| trial-counts | reproduced | Yes. Cell 20. |
| fig1b-accuracy | reproduced | Yes. Range 0.625–0.975; p = 0.283 (cell 23). |
| fig1b-rt-identity-slower | reproduced | Yes. p = 0.024, 0.005, 0.010 and 0.254 (cell 26). |
| erp-no-condition-difference (assumed) | not reproduced | Yes. The assumption is stated and reasonable. The outcome hardly depends on it: in the main configuration, 5 of the 6 neighbour × alpha-per-tail combinations give a cluster with p < 0.05 (or < 0.025 where that is the threshold). Only adjacent neighbours at 0.025 per tail give none (cell 29). |
| fig2-spatial-power | partial | Yes. 5 and 1 subjects, within one of the paper's counts. The percentages are off: 37.7 and 11.8 (cell 32). |
| fig3-temporal-power | partial | Yes. 5 and 2 subjects (4 and 2 with assignment b); no reading gets the percentages within tolerance (cell 32). |
| power-difficulty-subjects | reproduced | Yes. Holds under reading (b)(i) in every configuration. S3 breaks the converse (cell 37). |
| power-low-frequencies (assumed) | reproduced | Yes, by the letter. The assumption is stated and defensible, but weak: a "maximum" at the 2-Hz end of the range only means the density keeps rising below 2 Hz. Without counting that edge, the identity > other effect fails in every combination (cell 40). |
| fig4-maintenance-parietal-led | not reproduced | Yes. No subject is below −1.96 under either reading (cell 45). |
| fig4a-delta-theta-shift | not 
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
625 docs/protocol.md
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
411:### 4. Lock, check and run
422:### 5. Record the attempt
473:### 6. Hand over for verification
511:## Repeat attempts
553:## Local and remote datasets
576:## Verifier
580:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,200p docs/protocol.md; sed -n 411,625p docs/protocol.md
```

````
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

### 4. Lock, check and run

```bash
python tools/entry.py lock entries/<name>
[... 211 more lines not kept]
````

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat README.md; wc -l fcx3.py; python -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
  print('=====',i,c['cell_type']); print(''.join(c['source'])[:300])
"
```

```
# Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019) from CRCNS fcx-3

Tests the findings of [Johnson et al. (2019)](https://doi.org/10.3389/fnsys.2018.00065) on CRCNS
data set [fcx-3](https://doi.org/10.6080/K06971S9), which holds intracranial recordings from
prefrontal and parietal cortex of 7 patients doing a visuospatial working memory task, with the
preprocessed epochs and the paper's MATLAB scripts.

| Claim | Outcome |
|---|---|
| 192 analysed electrodes and 1129 pairs (Table 1) | Partially reproduced |
| Trials kept per subject and condition | Reproduced |
| Accuracy 0.63 to 0.98, no effect of condition | Reproduced |
| Identity RT longer than spatial and temporal | Reproduced |
| No ERP difference between conditions | Not reproduced (assumption) |
| Power, identity against spatial (Figure 2) | Partially reproduced |
| Power, identity against temporal (Figure 3) | Partially reproduced |
| Identity > effects in the subjects with lower identity accuracy | Reproduced |
| Power effects at 2-7 and 9-24 Hz | Reproduced (assumption) |
| Parietal-led maintenance (Figure 4) | Not reproduced |
| Delta-theta shift with the test cue | Not reproduced |
[... 434 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/ executed/crcns-fcx-3-johnson-2019 2>&1 | head; ls attempts | grep fcx; ls questions | grep fcx; wc -l attempts/crcns-fcx-3-johnson-2019-01.yaml; python tools/entry.py --help 2>&1 | head -30
```

```
ls: cannot access 'executed/': No such file or directory
ls: cannot access 'executed/crcns-fcx-3-johnson-2019': No such file or directory
crcns-fcx-1-watson-2016-01.yaml
crcns-fcx-3-johnson-2019-01.yaml
crcns-fcx-1.yaml
crcns-fcx-3.yaml
612 attempts/crcns-fcx-3-johnson-2019-01.yaml
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la transcripts/crcns-fcx-3/; grep -rn "min\b\|minutes" transcripts/crcns-fcx-3/*.md | grep -i "run\|took\|cell 2" | head -20
```

```
<persisted-output>
Output too large (85.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a72e76bd-db6e-44a4-902b-71ff454909b6/tool-results/b8takqz67.txt

Preview (first 2KB):
total 664
drwxr-xr-x   2 runner runner   4096 Nov  9 01:00 .
drwxr-xr-x 265 runner runner  12288 Nov  9 01:00 ..
-rw-r--r--   1 runner runner   1117 Nov  9 01:00 answer-report.md
-rw-r--r--   1 runner runner   5211 Nov  9 01:00 answer.md
-rw-r--r--   1 runner runner   2862 Nov  9 01:00 author-answers-report.md
-rw-r--r--   1 runner runner  10472 Nov  9 01:00 author-answers.md
-rw-r--r--   1 runner runner   4627 Nov  9 01:00 author-report.md
-rw-r--r--   1 runner runner   4078 Nov  9 01:00 author-revise-1-report.md
-rw-r--r--   1 runner runner 189665 Nov  9 01:00 author-revise-1.md
-rw-r--r--   1 runner runner 256679 Nov  9 01:00 author.md
-rw-r--r--   1 runner runner   3226 Nov  9 01:00 claims-check-report.md
-rw-r--r--   1 runner runner  22345 Nov  9 01:00 claims-check.md
-rw-r--r--   1 runner runner   4021 Nov  9 01:00 claims-report.md
-rw-r--r--   1 runner runner  47189 Nov  9 01:00 claims.md
-rw-r--r--   1 runner runner  10069 Nov  9 01:00 verifier-1-report.md
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/crcns-fcx-3/author-revise-1-report.md; grep -n "passed in\|run took\|seconds\|elapsed" transcripts/crcns-fcx-3/author-revise-1.md | tail -20
```

```
The round-1 revision is finished. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passed in 33.5 min), and every conclusion, the summary, the README and the attempt record now match the new outputs. Nothing is committed.

**Outcome changes.** Round 1 doesn't bind outcomes, so these are changed directly, each with its reason under `response`:
- **erp-no-condition-difference: reproduced → not reproduced** (still resting on the neighbour/alpha assumption). The ERP segments are now zero-padded before filtering, as the Methods and the claim's criterion say. Under the adopted reading, S2 identity-vs-temporal has a cluster at p = 0.041. The analysis run in round 1 (whole-epoch filtering) gives 0.031 with this run's random seed, against 0.053 before. So the flip is mostly Monte Carlo noise around 0.05, and the notes say so.
- **fig4a-delta-theta-shift: partially reproduced → not reproduced.** With a corrected null (below), no subject is above zero under either PSI reading.
- **fig4c-alpha-beta-shift: not reproduced → partially reproduced**, resting on PSI reading (b). It meets the partial bar by the letter: 6 of 7 subjects below zero, and the pair-level F is 97.9. But the subject means are only −1.35 to 0.46, and on subject means the effect reverses sign (p = 0.27). The notes say this plainly.
- **directional-pairs: reproduced → not reproduced.** With the corrected null only 1 and 74 pairs (reading b) or 78 and 104 (reading a) are directional, against the paper's 1008 and 984. Trial-shuffled data give about the same counts.
- The other 13 outcomes are unchanged. power-low-frequencies now passes under every neighbour reading, but only if the 2-Hz end of the range counts as a local maximum, so that is recorded as the assumption.

**What I added or corrected, by verifier problem.**
- **PSI null (problem 1).** The z-scores are now calibrated: the null shuffles one signal's frequencies and recomputes the same statistic, as the Methods describe
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; grep -n "^def \|^[A-Z_]* = \|cache\|CACHE" fcx3.py
```

```
65:DATASET = "crcns:fcx-3/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
66:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-3/live"
67:SUBJECTS = [f"s{i}" for i in range(1, 8)]
68:BLOCK = 2**24
70:PROC_WIN = (0.3, 1.2)
71:MAIN_WIN = (0.6, 1.5)
72:BASE_WIN = (0.65, 0.85)
73:FOI = np.arange(2, 41)
74:TOI_STEP = 0.01
75:BANDS = {"delta-theta": (2, 7), "alpha-beta": (9, 24)}
76:PAD_S = 7.5
77:N_PERM = 1000
82:def read_bytes(path):
87:def checksums():
96:def bucket_listing():
106:def script_files():
115:def summary_file():
122:def channel_table():
140:def _cellstr(h, ds):
144:def parse_grid(text):
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; sed -n 540,660p fcx3.py; sed -n 854,1018p fcx3.py
```

```
def _slope(c):
    """Sum over adjacent bins of Im(conj(c_f) c_{f+1}), over the last axis."""
    return np.imag(np.conj(c[..., :-1]) * c[..., 1:]).sum(-1)


def _unit(x):
    a = np.abs(x)
    return x / np.where(a > 0, a, 1)


def psi_z(A, B, ia, ib, rng, n_perm=N_PERM, code_null=False):
    """PSI z per pair and time point, A = PFC (positive: PFC leads), B = parietal.

    A: trials x nA x f x T, B: trials x nB x f x T complex spectra of the channels, ERP already
    removed (T = 1 for the task-induced PSI). ia, ib: channel indices of each pair into A and B.
    Returns {reading: z, pairs x T} for the readings of the claims file (header P1):

    - 'a': PSI from the trial-averaged coherency C_f = <A conj(B)> / sqrt(<|A|^2><|B|^2>), the sum
      over adjacent bins of Im(conj(C_f) C_{f+1}) (Nolte et al. 2008).
    - 'b': PSI per trial from the per-trial normalised cross-spectrum A conj(B) / |A B| (the
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims | grep fcx-3; grep -n "P1\|null" claims/crcns-fcx-3*.yaml | head -40; cat questions/crcns-fcx-3.yaml
```

```
crcns-fcx-3
grep: claims/crcns-fcx-3*.yaml: No such file or directory
# Questions from attempt crcns-fcx-3-johnson-2019-01 (author revision after verifier round 1,
# 2026-11-08) about claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported this as a place where the claims file misreads
# the paper; the claims were tested as the file has them.
dataset: crcns:fcx-3
paper: doi:10.3389/fnsys.2018.00065
questions:
- claim: fig5b-alpha-beta-no-sustained
  attempt: crcns-fcx-3-johnson-2019-01
  asked: 2026-11-08
  question: Should a sustained effect be a run of significant time points lasting more than 100 ms,
    as the Figure 5 legend says, in place of at least 100 ms, as header P2 and this claim's
    criterion have it? The Methods say "at least 100 ms" and the legend says ">100 ms", so the paper
    gives both. The same question applies to fig5a-delta-theta-epochs, which uses P2's rule.
  passage: Methods, Time-Resolved PSI, paragraph 2, "Significant differences were considered
    sustained if they persisted for at least 100 ms at the FDR-corrected threshold"; Figure 5
    legend, "Shaded epochs represent effects that were sustained for >100 ms".
  why: On a 10-ms grid a run from t to t + 100 ms is sustained under the first reading and not under
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/crcns-fcx-3; f=claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml; grep -n "id: P1" -A40 $f | head -60; grep -n "id: fig4c" -A30 $f
```

```
10.3389-fnsys.2018.00065.yaml
404:- id: fig4c-alpha-beta-shift
405-  statement: Alpha-beta directionality also shifted with the test cue, but all subjects remained
406-    net parietal-led during processing (z < -12.60 +- 7.51).
407-  source: Results, Task-Induced Effects, paragraph 2; Figure 4C and 4D
408-  quote: In the alpha-beta range, there was again a shift in directionality with presentation of
409-    the test cue (processing > maintenance, F (1,2256) = 2302.30, p = 0; Figures 4C,D ). Despite
410-    the shift, however, all subjects continued to exhibit net parietal → PFC connectivity at
411-    processing, mean ± SD... z < −12.60 ± 7.51
412-  statistics:
413-  - test: linear mixed-effects model, interval fixed, subject and pair random
414-    statistic: F(1,2256) = 2302.30
415-    p: 0
416-    n: 7 subjects, 1129 electrode pairs
417-  expected:
418-  - quantity: mean alpha-beta PSI z, processing
419-    value: -12.6
420-    tolerance: 1.26
421-  - quantity: F statistic, processing against maintenance
422-    value: 2302.30
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml; sed -n 1,140p $f | grep -n "P1" ; awk '/P1/{p=1} p&&NR<200{print NR": "$0}' $f | head -50
```

```
74:# P1. Phase slope index (Methods, Directional Connectivity, Task-Induced PSI). Correct trials; "the
74: # P1. Phase slope index (Methods, Directional Connectivity, Task-Induced PSI). Correct trials; "the
75: #   raw trial-wise mean" is subtracted from each trial (readings (a) the mean over all correct
76: #   trials, (b) the mean over the trials of the condition, (c) each segment's own temporal mean);
77: #   PFC-parietal pairs in the same hemisphere;
78: #   positive PSI means PFC leads. Spectra "using the same parameters described above, but over the
79: #   full delay interval"; readings (a) one Hanning-tapered FFT of each 900 ms segment, zero-padded
80: #   to 7500 ms, read at 1-Hz steps, (b) the 3-cycle windows of S1 averaged over time. PSI per band,
81: #   delta-theta 2 to 7 Hz and alpha-beta 9 to 24 Hz; readings (a) one PSI from the cross-spectra
82: #   over all 1-Hz bins of the band (Nolte et al. 2008), (b) PSI per frequency with a 2-Hz
83: #   bandwidth, averaged over the band. Null: the frequencies of one signal shuffled and PSI
84: #   recomputed 1000 times; PSI z-scored on the null mean and SD. Whether one permutation serves all
85: #   trials or each trial gets its own is open; readings (a) one per shuffle, (b) one per trial.
86: #   PFC leads at z > 1.96, parietal leads at z < -1.96. Whether PSI is computed once per pair from
87: #   cross-spectra averaged over trials or per trial is not stated; readings (a) cross-spectra
88: #   averaged over trials, one PSI z per pair (Nolte et al. 2008, and one value per pair and
89: #   interval fits F(1,2256)), (b) PSI z per trial, averaged over trials per pair (Figure 4A legend,
90: #   "mean +- SEM per subject across all trials").
91: # P2. Group models. Task-induced PSI z per pair and interval in a linear mixed-effects model with
92: #   interval fixed and subject and pair random (Methods, Task-Induced PSI, paragraph 3);
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "claim: \|outcome: \|assumed\|proposed" attempts/crcns-fcx-3-johnson-2019-01.yaml | head -80
```

```
23:- claim: table1-electrodes
24:  outcome: partially_reproduced
42:- claim: trial-counts
43:  outcome: reproduced
61:- claim: fig1b-accuracy
62:  outcome: reproduced
81:- claim: fig1b-rt-identity-slower
82:  outcome: reproduced
96:- claim: erp-no-condition-difference
97:  outcome: not_reproduced
98:  assumed: true
133:- claim: fig2-spatial-power
134:  outcome: partially_reproduced
165:- claim: fig3-temporal-power
166:  outcome: partially_reproduced
185:- claim: power-difficulty-subjects
186:  outcome: reproduced
199:- claim: power-low-frequencies
200:  outcome: reproduced
201:  assumed: true
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,22p attempts/crcns-fcx-3-johnson-2019-01.yaml; sed -n 217,612p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
schema_version: 2
id: crcns-fcx-3-johnson-2019-01
dataset:
  archive: crcns
  id: fcx-3
  version: unversioned
  doi: 10.6080/K06971S9
paper: doi:10.3389/fnsys.2018.00065
date: 2026-11-08
entry: crcns-fcx-3-johnson-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
[... 398 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "agree\|proposed" tools/*.py | head -40
```

```
tools/agent_run.py:6:    python tools/agent_run.py proposals ROLE DATASET      # "true" if the attempt has proposed changes
tools/agent_run.py:15:author-revise-3, the third round that settles changes proposed after the second. A repeat attempt
tools/agent_run.py:273:    """The claims of the latest attempt on a dandiset that carry a proposed change of outcome."""
tools/agent_run.py:275:    return [o["claim"] for o in (found[0]["outcomes"] if found else []) if o.get("proposed")]
tools/build_site.py:26:verification decides, and it counts only if it agrees with every outcome.
tools/build_site.py:118:    "code_mismatch": "Published code disagrees",
tools/build_site.py:141:    agreed = {r["claim"] for r in latest.get("results", []) if r.get("agrees")}
tools/build_site.py:142:    return VERIFICATION_TIER.get(latest["kind"], "runs") if claims <= agreed else "runs"
tools/build_site.py:210:        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
tools/build_site.py:247:                "disagreed": o["claim"] in disagreed,
tools/build_site.py:250:                "proposed": o.get("proposed"),
tools/build_site.py:258:                "agreed": sum(1 for r in v["results"] if r.get("agrees")),
tools/build_site.py:260:                "disagreements": [{"claim": r["claim"], "outcome": r.get("outcome"),
tools/build_site.py:262:                                  for r in v["results"] if not r.get("agrees")],
tools/build_site.py:381:                "disagreed": rng.random() < 0.08,
tools/build_site.py:400:                "agreed": n_claims, "of": n_claims, "disagreements": []}],
tools/build_site.py:657:                               "deviations": o["deviations"], "disagreed": o["disagreed"],
tools/build_site.py:658:                               "verifier": "disagreed" if o["disagreed"] else None,
tools/build_site.py:763:    tags = '<span class="tag">verifier disagreed at first</span>' if o["disagreed"] else ""
tools/build_site.py:776:    if o
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 265,305p tools/entry.py; grep -n "proposed" -A15 schemas/*attempt* 2>/dev/null | head -40; ls schemas 2>/dev/null
```

```
report.error(where, "claims take names for the dataset's codes from elsewhere (`with_labels`), so "
                                    "list the source under `inputs` and record the missing names as a finding "
                                    "(metadata_insufficient or identifier_missing)")
        if known is None:
            report.error(where, "no claims file for this dataset and paper")
            continue
        recorded = [o.get("claim") for o in attempt.get("outcomes", [])]
        for claim in sorted(known - set(recorded)):
            report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
        for claim in sorted({c for c in recorded if recorded.count(c) > 1}):
            report.error(where, f"claim {claim!r} has more than one outcome")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
        agreed = {}
        for rnd in (attempt.get("verifications") or [])[1:]:
            for r in rnd["results"]:
                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
        kinds = kinds_by_target.get((dataset_id(attempt), attempt.get("paper")), {})
        for outcome in attempt.get("outcomes", []):
            # A claim on data in another archive names where they are, so it is never blocked for missing data,
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; sed -n 379,430p fcx3.py; which python; python -c "import numpy, scipy; print(numpy.__version__)"; nproc; free -g
```

```
def hanning_ft(n):
    """MATLAB hanning(n), as FieldTrip uses: 0.5*(1-cos(2*pi*k/(n+1))), k = 1..n."""
    k = np.arange(1, n + 1)
    return 0.5 * (1 - np.cos(2 * np.pi * k / (n + 1)))


def win_index(time, win):
    return np.where((time >= win[0] - 1e-9) & (time <= win[1] + 1e-9))[0]


def toi_index(time, win, step=TOI_STEP):
    toi = np.arange(win[0], win[1] + step / 2, step)
    return np.array([int(np.argmin(np.abs(time - t))) for t in toi]), toi


def tfr_fourier(x, time, fs, foi, toi_idx):
    """Complex 3-cycle Hanning spectra (mtmconvol) at the samples toi_idx: trials x ch x f x t."""
    n_tr, n_ch, n_t = x.shape
    nfft = int(2 ** np.ceil(np.log2(n_t + int(3 / foi.min() * fs) + 1)))
    X = np.fft.fft(x.reshape(-1, n_t).astype("float64"), n=nfft, axis=1)
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python -m venv $TMPDIR/venv && $TMPDIR/venv/bin/pip install -q -r requirements.lock.txt 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import numpy; print(numpy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/venv/bin/python -m pip install --upgrade pip
2.5.4
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/syn; cat > $TMPDIR/syn/syn.py <<'EOF'
import sys, numpy as np, time
sys.path.insert(0, "entries/crcns-fcx-3-johnson-2019")
import fcx3
rng = np.random.default_rng(0)
fs = 1000; R = 33; n = 1300
t = np.arange(n)/fs - 0.2
def noise(kind, R, ch):
    w = rng.standard_normal((R, ch, n))
    if kind == "brown": return np.cumsum(w, -1)
    W = np.fft.rfft(w, axis=-1); f = np.fft.rfftfreq(n, 1/fs); f[0]=1
    return np.fft.irfft(W/np.sqrt(f), n=n, axis=-1)
for kind in ("pink", "brown"):
    x = np.concatenate([noise(kind, R, 20), noise(kind, R, 8)], 1)
    for band,(lo,hi) in fcx3.BANDS.items():
        F,_ = fcx3.fft_segment(x, t, fs, (0.0, 0.9), np.arange(lo,hi+1))
        F = F - F.mean(0, keepdims=True)
        A, B = F[:, :20, :, None], F[:, 20:, :, None]
        ia, ib = np.repeat(np.arange(20), 8), np.tile(np.arange(8), 20)
        t0=time.time()
        out = fcx3.psi_z(A, B, ia, ib, np.random.default_rng(1), n_perm=int(sys.argv[1]) if len(sys.argv)>1 else 300)
        for k,v in out.items():
            v=v[:,0]; print(kind, band, k, f"mean {v.mean():.3f} sd {v.std():.3f} pass {np.mean(abs(v)>1.96):.3f}")
        print(time.time()-t0)
EOF
$TMPDIR/venv/bin/python $TMPDIR/syn/syn.py
```

```
pink delta-theta a mean -0.042 sd 1.033 pass 0.069
pink delta-theta b mean -0.275 sd 0.825 pass 0.013
0.02366161346435547
pink alpha-beta a mean -0.010 sd 1.096 pass 0.069
pink alpha-beta b mean -0.289 sd 0.939 pass 0.044
0.0837855339050293
brown delta-theta a mean -0.231 sd 0.908 pass 0.025
brown delta-theta b mean -0.624 sd 0.739 pass 0.013
0.022940397262573242
brown alpha-beta a mean -0.221 sd 1.143 pass 0.094
brown alpha-beta b mean -0.668 sd 0.969 pass 0.100
0.030847787857055664
```

**Agent calls Bash**

```bash
cat > $TMPDIR/syn/syn2.py <<'EOF'
import sys, numpy as np
sys.path.insert(0, "entries/crcns-fcx-3-johnson-2019")
import fcx3
fs = 1000; R = 33; n = 1300
t = np.arange(n)/fs - 0.2
def noise(rng, kind, R, ch):
    w = rng.standard_normal((R, ch, n))
    if kind == "brown": return np.cumsum(w, -1)
    W = np.fft.rfft(w, axis=-1); f = np.fft.rfftfreq(n, 1/fs); f[0]=1
    return np.fft.irfft(W/np.sqrt(f), n=n, axis=-1)
for kind in ("pink", "brown"):
  for band,(lo,hi) in fcx3.BANDS.items():
    res = {}
    for rep in range(10):
        rng = np.random.default_rng(rep)
        x = np.concatenate([noise(rng, kind, R, 4), noise(rng, kind, R, 4)], 1)
        F,fr = fcx3.fft_segment(x, t, fs, (0.0, 0.9), np.arange(lo,hi+1))
        F = F - F.mean(0, keepdims=True)
        for centred in (False, True):
            G = F * np.exp(2j*np.pi*fr*0.45) if centred else F
            A, B = G[:, :4, :, None], G[:, 4:, :, None]
            ia, ib = np.repeat(np.arange(4), 4), np.tile(np.arange(4), 4)
            out = fcx3.psi_z(A, B, ia, ib, np.random.default_rng(rep+100), n_perm=300)
            for k,v in out.items():
                res.setdefault((centred,k), []).append(v[:,0])
    for (c,k),v in res.items():
        v=np.concatenate(v); print(kind, band, "centred" if c else "raw", k, f"mean {v.mean():.3f} sd {v.std():.3f} pass {np.mean(abs(v)>1.96):.3f}")
EOF
$TMPDIR/venv/bin/python $TMPDIR/syn/syn2.py
```

```
pink delta-theta raw a mean -0.167 sd 1.109 pass 0.087
pink delta-theta raw b mean -0.327 sd 0.851 pass 0.019
pink delta-theta centred a mean -0.088 sd 1.269 pass 0.138
pink delta-theta centred b mean 0.004 sd 1.126 pass 0.069
pink alpha-beta raw a mean -0.041 sd 1.054 pass 0.075
pink alpha-beta raw b mean -0.305 sd 1.039 pass 0.081
pink alpha-beta centred a mean 0.025 sd 1.100 pass 0.087
pink alpha-beta centred b mean -0.021 sd 1.211 pass 0.131
brown delta-theta raw a mean -0.163 sd 1.103 pass 0.075
brown delta-theta raw b mean -0.266 sd 0.855 pass 0.037
brown delta-theta centred a mean -0.111 sd 1.238 pass 0.138
brown delta-theta centred b mean 0.048 sd 1.062 pass 0.062
brown alpha-beta raw a mean -0.039 sd 1.052 pass 0.075
brown alpha-beta raw b mean -0.303 sd 1.039 pass 0.069
brown alpha-beta centred a mean 0.027 sd 1.097 pass 0.087
brown alpha-beta centred b mean -0.019 sd 1.206 pass 0.125
```

**Agent calls Bash**

```bash
cd  f=claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml; awk '/id: fig5a-spatiotemporal/,0' $f
```

```
- id: fig5a-spatiotemporal-bidirectional
  statement: Delta-theta PSI during the selection of spatial and of temporal information stayed
    bidirectional (net near zero) throughout the processing interval.
  source: Results, Spatiotemporal Processing Effects, paragraph 3; Figure 5A
  quote: In contrast, the selection of spatial (Figure 5A , left) and temporal (right) information
    exhibited bidirectionality throughout the processing interval (all | z | < 1.60, p > 0.11)
  statistics:
  - test: PSI z against frequency-shuffled surrogates
    statistic: all |z| < 1.60
    p: 0.11
    p_relation: ">"
  depends_on:
  - directional-pairs
  criterion: Spatial-trial and temporal-trial time-resolved delta-theta PSI z (P2). A claim of
    absence, judged on the paper's measure alone; "throughout the processing interval" means
    every 10-ms time point of 0 to 900 ms. The measure is the grand mean over subjects, the
    quantity Figure 5A plots (reading (a) of fig5a-identity-direction); readings (b) and (c) are
    shown as variants. Reproduced when |z| < 1.96 (the paper's threshold for bidirectionality,
    Methods, Time-Resolved PSI) at every time point; not reproduced when any point exceeds it. The
    largest |z| is reported and compared with the paper's 1.60.
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; sed -n 760,830p fcx3.py; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i in [0,2,5,10,11,43,44,47]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
def seed(*keys):
    """A fixed seed per claim section and subject, so that each has its own generator."""
    import zlib
    return zlib.crc32("/".join(map(str, keys)).encode())


JITTER_WINDOWS = {"data_pre": (0.6, 1.6), "data_encmain": (-0.3, 1.0), "data_proc": (-0.9, 0.7)}


def jitter_check(S, max_lag=0.4, n_shuffle=20):
    """Timing contrast between the trials with 900-ms and 1150-ms delays.

    The trial table puts the encoding epoch (data_encmain) at a fixed 1.9 s after the pretrial start
    and the processing epoch at 0.6 s + jitter + 0.8 s after the encoding start, so if the columns
    mark the events, the responses inside each window below occur at the same times in both groups:
    the start screen (data_pre, 0.6 to 1.6 s), the two stimuli (data_encmain, -0.3 to 1.0 s) and
    the test cue and its offset (data_proc, -0.9 to 0.7 s; the cue is on from -0.5 to 0.3 s). The
    measure is the 70-150 Hz amplitude (Hilbert envelope of a 4th-order Butterworth band, smoothed at
    10 Hz, each trace divided by its mean), averaged over trials per group; the shift of the
    1150-ms group that best aligns it with the 900-ms group over all channels is reported, with
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; date -u; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i in [32,33,54,56,62]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
Mon Nov  9 01:07:30 UTC 2026
===== 32
def power_effects(contrast, nb, alpha=0.05, assign="a", config="methods"):
    out = []
    for sid in fcx3.SUBJECTS:
        cl = RES[sid]["power"][config][contrast]["clusters"][nb]
        n = len(RES[sid]["labels"])
        ident, other = np.zeros(n, bool), np.zeros(n, bool)
        ts_i, ts_o = np.zeros(n), np.zeros(n)
        for c in cl["pos"]:  # positive t: identity > other
            if c["p"] < alpha:
                ident |= c["elec_mask"]
                ts_i += c["tsum_by_elec"]
        for c in cl["neg"]:
            if c["p"] < alpha:
                other |= c["elec_mask"]
                ts_o += -c["tsum_by_elec"]
        if assign == "b":
            both = ident & other
            ident = ident & ~(both & (ts_o >= ts_i))
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; sed -n 1,64p fcx3.py; sed -n 172,222p fcx3.py
```

```
"""Loading and measures for CRCNS data set fcx-3 (Johnson et al. 2019, Front. Syst. Neurosci. 12, 65,
doi:10.3389/fnsys.2018.00065).

The data set (doi:10.6080/K06971S9) holds, per subject, a tar.gz with the filtered continuous iEEG
(data_primary.mat), the channel names (elec_labels.mat), electrode positions (s<n>_MNI_grid.csv),
the preprocessed epochs (data_derived.mat, FieldTrip structures data_pre, data_encmain and
data_proc, MATLAB 7.3) and a trial table (summary_file_trial.csv). The tar files are streamed from
the public bucket and decompressed in memory, one subject at a time; nothing is written to disk.
A tar.gz cannot be read at random, so each subject's file is read once, start to end.

Where the parameters come from:

- Channels analysed, by region and hemisphere: docs/summary_channel_analysis.csv of the data set.
  The derived epochs carry more channels; only the listed ones are kept.
- Analysis windows, in the time axis of the derived epochs: processing [0.3, 1.2] s of data_proc,
  maintenance [0.6, 1.5] s of data_encmain, baseline [0.65, 0.85] s of data_pre. These are the
  latencies of the paper's deposited scripts (power_compute.m, erp_compute.m, psi_compute.m); the
  notebook checks them against the trial table and the continuous data.
- Power: Hanning-tapered windows of 3 cycles (3/f s), 2 to 40 Hz in 1-Hz steps, 10-ms steps
  (Methods, Spectral Decomposition; power_compute.m). Main reading: the 900-ms segment alone,
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/patch1.py <<'EOF'
p = "fcx3.py"
s = open(p).read()
old = '''def psi_z(A, B, ia, ib, rng, n_perm=N_PERM, code_null=False):'''
new = '''def psi_z(A, B, ia, ib, rng, n_perm=N_PERM, code_null=False, trial_null=False):'''
assert old in s; s = s.replace(old, new)
old = '''    code_null=True adds 'b_code': reading (b) z-scored against the null of psianalysis.m, the slope'''
new = '''    trial_null=True adds 'a_trial' and 'b_trial': readings (a) and (b) with P1 null reading (b), each
    trial's parietal bins permuted by its own permutation in each shuffle (task-induced PSI only).

    code_null=True adds 'b_code': reading (b) z-scored against the null of psianalysis.m, the slope'''
assert old in s; s = s.replace(old, new)
old = '''    if code_null:
        pp = (ua[:, ia]'''
new = '''    if trial_null:
        assert T == 1
        Af = A[..., 0].transpose(2, 1, 0)  # f x nA x R
        Na1 = Na[..., 0]  # nA x f
        ubt = ub[..., 0].transpose(0, 2, 1)  # R x f x nB
        rr = np.arange(R)[:, None]
        t1 = {k: np.zeros(obs[k].shape) for k in ("a", "b")}
        t2 = {k: np.zeros(obs[k].shape) for k in ("a", "b")}
        for _ in range(n_perm):
            P = rng.permuted(np.tile(np.arange(nf), (R, 1)), axis=1)
            Bp = B[..., 0].transpose(0, 2, 1)[rr, P]  # R x f x nB, bins permuted per trial
            Xp = Af @ np.conj(Bp.transpose(1, 0, 2)) / R  # f x nA x nB
            Nbp = np.sqrt((np.abs(Bp) ** 2).mean(0))  # f x nB
            C = Xp[:, ia, ib].T / (Na1[ia] * Nbp[:, ib].T)  # pairs x f
            va = _slope(C)[:, None]
            g = ubt[rr, P]
            DB = np.conj(g[:, :-1]) * g[:, 1:]  # R x (f-1) x nB
            vb = (MA @ np.conj(DB).reshape(1, R * (nf - 1), nB)).imag[:, ia, ib].T / R
            for k, v in (("a", va), ("b", vb)):
                t1[k] += v
                t2[k] += v * v
        for k in ("a", "b"):
            mean = t1[k] / n_perm
            sd = np.sqrt(np.maximum(t2[k] - n_perm * mean ** 2, 0) / (n_perm - 1))
            out[k + "_trial"] = (obs[k] - mean) / sd
    if code_null:
        pp = (ua[:, ia]'''
assert old in s; s = s.replace(old, new)
open(p, "w").write(s)
EOF
python3 $TMPDIR/patch1.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/syn/t1.py <<'EOF'
import sys, numpy as np
sys.path.insert(0, "entries/crcns-fcx-3-johnson-2019")
import fcx3
class Id:
    def permutation(self, n): return np.arange(n)
    def permuted(self, x, axis): return x
r = np.random.default_rng(0)
A = r.standard_normal((20,3,6,1)) + 1j*r.standard_normal((20,3,6,1))
B = r.standard_normal((20,2,6,1)) + 1j*r.standard_normal((20,2,6,1))
ia, ib = np.array([0,1,2,0]), np.array([0,0,1,1])
o = fcx3.psi_z(A, B, ia, ib, Id(), n_perm=3, trial_null=True)
# with identity perms null sd = 0 -> compare means directly by instrumenting: obs-mean = 0 -> nan/0
print({k: v.ravel() for k, v in o.items()})
EOF
$TMPDIR/venv/bin/python $TMPDIR/syn/t1.py 2>&1 | tail -3
```

```
entries/crcns-fcx-3-johnson-2019/fcx3.py:645: RuntimeWarning: invalid value encountered in divide
  out[k + "_trial"] = (obs[k] - mean) / sd
{'a': array([nan,  0., nan, nan]), 'b': array([nan,  0., nan,  0.]), 'a_trial': array([ inf,  inf, -inf,  inf]), 'b_trial': array([nan,  0., nan,  0.])}
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/syn/t1.py <<'EOF'
R=20
Af = A[...,0].transpose(2,1,0)
Bp = B[...,0].transpose(0,2,1)
Xp = Af @ np.conj(Bp.transpose(1,0,2))/R
Na = np.sqrt((abs(A)**2).mean(0))[...,0]; Nb = np.sqrt((abs(Bp)**2).mean(0))
C = Xp[:, ia, ib].T / (Na[ia]*Nb[:, ib].T)
C2 = np.array([[ (A[:,a,f,0]*np.conj(B[:,b,f,0])).mean()/np.sqrt((abs(A[:,a,f,0])**2).mean()*(abs(B[:,b,f,0])**2).mean()) for f in range(6)] for a,b in zip(ia,ib)])
print(np.abs(C-C2).max(), fcx3._slope(C2))
EOF
$TMPDIR/venv/bin/python $TMPDIR/syn/t1.py 2>&1 | tail -1
```

```
1.1857187100668868e-16 [ 0.06009883 -0.03619706  0.00344242  0.1048399 ]
```

**Agent calls Bash**

```bash
cd $TMPDIR/syn; sed -i 's/n_perm=300)/n_perm=300, trial_null=True)/' syn2.py; sed -i 's/for centred in (False, True)/for centred in (False,)/' syn2.py; time $TMPDIR/venv/bin/python syn2.py
```

```
pink delta-theta raw a mean -0.167 sd 1.109 pass 0.087
pink delta-theta raw b mean -0.327 sd 0.851 pass 0.019
pink delta-theta raw a_trial mean -0.175 sd 1.303 pass 0.138
pink delta-theta raw b_trial mean -0.413 sd 1.083 pass 0.081
pink alpha-beta raw a mean -0.041 sd 1.054 pass 0.075
pink alpha-beta raw b mean -0.305 sd 1.039 pass 0.081
pink alpha-beta raw a_trial mean -0.048 sd 1.094 pass 0.087
pink alpha-beta raw b_trial mean -0.336 sd 1.186 pass 0.106
brown delta-theta raw a mean -0.163 sd 1.103 pass 0.075
brown delta-theta raw b mean -0.266 sd 0.855 pass 0.037
brown delta-theta raw a_trial mean -0.161 sd 1.312 pass 0.119
brown delta-theta raw b_trial mean -0.318 sd 1.029 pass 0.062
brown alpha-beta raw a mean -0.039 sd 1.052 pass 0.075
brown alpha-beta raw b mean -0.303 sd 1.039 pass 0.069
brown alpha-beta raw a_trial mean -0.046 sd 1.092 pass 0.081
brown alpha-beta raw b_trial mean -0.335 sd 1.185 pass 0.113

real	0m4.581s
user	0m11.195s
sys	0m0.147s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/patch2.py <<'EOF'
p = "fcx3.py"
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old
    s = s.replace(old, new)
rep('''POWER_CONFIGS = ("methods", "code", "methods_900")''',
    '''POWER_CONFIGS = ("methods", "code", "methods_900", "methods_half")''')
rep('''        if config == "methods":
            R["power"]["methods_900"] = {name: _power_clusters(pz[j900], ccond[j900], nb, sid, name, "methods_900", n_perm)
                                         for name in contrasts}
''', '''        if config == "methods":
            R["power"]["methods_900"] = {name: _power_clusters(pz[j900], ccond[j900], nb, sid, name, "methods_900", n_perm)
                                         for name in contrasts}
            # control for methods_900: as many trials per condition as it has, drawn from all delays
            rng = np.random.default_rng(seed("half", sid))
            half = np.zeros(len(ccond), bool)
            for c in (1, 2, 3):
                idx = np.where(ccond == c)[0]
                half[rng.choice(idx, int((j900 & (ccond == c)).sum()), replace=False)] = True
            R["n_correct_half_jitter"] = {d: int((half & (jit[correct] == d)).sum()) for d in (900, 1150)}
            R["power"]["methods_half"] = {name: _power_clusters(pz[half], ccond[half], nb, sid, name, "methods_half", n_perm)
                                          for name in contrasts}
''')
rep('''            res[interval] = {k: v[:, 0] for k, v in psi_z(A, B, ia, ib, rng, code_null=True).items()}''',
    '''            res[interval] = {k: v[:, 0] for k, v in psi_z(A, B, ia, ib, rng, code_null=True, trial_null=True).items()}''')
rep('''                sur = {k: v[:, 0] for k, v in psi_z(A, B[order], ia, ib, rng, code_null=True).items()}
                sur["same_trial_fraction"] = float(np.mean(order == np.arange(len(order))))
''', '''                sur = {k: v[:, 0] for k, v in psi_z(A, B[order], ia, ib, rng, code_null=True, trial_null=True).items()}
                sur["same_trial_fraction"] = float(np.mean(order == np.arange(len(order))))
        # processing PSI on the trials with a 900-ms delay only (timing finding), ERP of those trials removed
        F, _ = fft_segment(proc["x"][correct][j900], proc["time"], fs, PROC_WIN, foi)
        F = F - F.mean(0, keepdims=True)
        rng = np.random.default_rng(seed("psi", sid, band, "processing_900"))
        res["processing_900"] = {k: v[:, 0] for k, v in psi_z(F[:, pfc, :, None], F[:, par, :, None], ia, ib, rng).items()}
''')
# jitter traces for plotting
rep('''        out[key] = {"lag_s": lag, "r": r, "shuffled_abs_lag_max_s": max(abs(v[0]) for v in sh),
                    "shuffled_r_max": max(v[1] for v in sh)}''',
    '''        out[key] = {"lag_s": lag, "r": r, "shuffled_abs_lag_max_s": max(abs(v[0]) for v in sh),
                    "shuffled_r_max": max(v[1] for v in sh), "time": e["time"][::10],
                    "trace_900": env[jit == 900].mean((0, 1))[::10], "trace_1150": env[jit == 1150].mean((0, 1))[::10]}''')
open(p, "w").write(s)
EOF
python3 $TMPDIR/patch2.py; grep -n "jit = info\|j900 =" fcx3.py
```

```
930:    jit = info[:, 4]
939:    j900 = jit[correct] == 900
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/dev.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0, ".")
import fcx3
sid = sys.argv[1]
CHAN = fcx3.channel_table()
chan = CHAN[CHAN.subject == sid].reset_index(drop=True)
t0 = time.time()
S = fcx3.stream_subject(sid, list(chan.label))
print("streamed", time.time() - t0, flush=True)
pickle.dump((S, chan), open(f"{sys.argv[2]}/S_{sid}.pkl", "wb"), protocol=4)
EOF
date -u; time $TMPDIR/venv/bin/python $TMPDIR/dev.py s7 $TMPDIR
```

```
Mon Nov  9 01:08:56 UTC 2026
streamed 31.27202534675598

real	0m33.167s
user	0m7.560s
sys	0m2.188s
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/dev2.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0, ".")
import fcx3
sid = sys.argv[1]; n = int(sys.argv[2])
S, chan = pickle.load(open(f"/tmp/claude-1001/S_{sid}.pkl", "rb"))
t0 = time.time(); J = fcx3.jitter_check(S); print("jitter", time.time()-t0, {k: (v["trace_900"].shape, v["time"].shape) for k, v in J.items()})
t0 = time.time(); R = fcx3.analyse_subject(S, chan, n_perm=n); print("analyse", time.time()-t0)
print(R["n_correct_half_jitter"], R["n_correct_900_by_cond"])
for band in fcx3.BANDS:
    for iv in ("maintenance", "processing", "processing_900"):
        print(band, iv, {k: round(float(v.mean()), 2) for k, v in R["psi"][band][iv].items()})
    print("sur", {k: round(float(np.mean(v)), 2) for k, v in R["psi_surrogate"][band].items()})
print({c: {k: v["clusters"]["adjacent"]["neg_minp"] for k, v in R["power"][c].items()} for c in fcx3.POWER_CONFIGS})
pickle.dump((J, R), open(f"/tmp/claude-1001/R_{sid}.pkl", "wb"))
EOF
echo $TMPDIR; time $TMPDIR/venv/bin/python $TMPDIR/dev2.py s7 100
```

```
/tmp/claude-1001
jitter 1.9255478382110596 {'data_pre': ((231,), (231,)), 'data_encmain': ((231,), (231,)), 'data_proc': ((231,), (231,))}
analyse 19.7799391746521
{900: 21, 1150: 21} {1: 16, 2: 12, 3: 14}
delta-theta maintenance {'a': -0.39, 'b': -0.26, 'a_trial': -0.41, 'b_trial': -0.54, 'b_code': 12.61}
delta-theta processing {'a': -0.23, 'b': -0.11, 'a_trial': -0.24, 'b_trial': -0.23, 'b_code': 6.75}
delta-theta processing_900 {'a': 0.08, 'b': 0.42}
sur {'a': 0.13, 'b': 0.15, 'a_trial': 0.15, 'b_trial': 0.15, 'b_code': 12.87, 'same_trial_fraction': 0.0}
alpha-beta maintenance {'a': -0.28, 'b': -0.18, 'a_trial': -0.25, 'b_trial': -0.19, 'b_code': 4.21}
alpha-beta processing {'a': 0.19, 'b': -0.18, 'a_trial': 0.2, 'b_trial': -0.22, 'b_code': 4.56}
alpha-beta processing_900 {'a': -0.15, 'b': -0.05}
sur {'a': -0.08, 'b': 0.03, 'a_trial': -0.11, 'b_trial': 0.06, 'b_code': 6.86, 'same_trial_fraction': 0.0}
{'methods': {'spatial': 0.63, 'temporal': 0.0}, 'code': {'spatial': 0.69, 'temporal': 0.0}, 'methods_900': {'spatial': 0.21, 'temporal': 0.04}, 'methods_half': {'spatial': 0.16, 'temporal': 0.0}}

real	0m23.022s
user	0m37.931s
sys	0m0.540s
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i in [30,34,42,45,46,48,49,50,51,52,58,60,61,63,64]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 30
**Result: not reproduced, resting on an assumption.** Under the main reading with neighbours
adjacent by contact number and clusters judged at 0.05 per tail, S2 has a significant cluster for
identity against temporal (p = 0.041); no other subject-contrast is below 0.05, and 2 of 14 have
p <= 0.10 (the paper reports all p > 0.10). The outcome depends on the readings: at 0.025 per tail
the adjacent reading finds no significant cluster (reproduced), while the distance reading (S5,
p = 0.014) and the reading without spatial clustering (S2, p = 0.024) find one at either
threshold. Among the variants, the 1-30 Hz band-pass gives no cluster below 0.05 with adjacent
neighbours (smallest p 0.085); the per-trial baseline gives one (S5 identity against spatial,
p = 0.030); filtering the whole epoch gives S2 p = 0.031; the 900-ms-delay trials alone give one
(S5 identity against temporal, p = 0.023). The deciding p values lie between 0.02 and 0.05, so
the outcome is close to the threshold under every reading.
===== 34
**Result: partially reproduced.** Under the main spectra, 5 subjects show spatial > identity
effects (S2 to S6) under every neighbour reading and threshold, and 1 shows identity > spatial
effects (S4; paper 2) under every reading but adjacent neighbours at 0.025 per tail, which finds none. With adjacent neighbours at 0.05 per tail the percentages
are 37.7 +- 21.1% and 11.8% (S4 alone), below the paper's 54 +- 22% and 36 +- 12%. The counts
match within one subject and 5 of 7 subjects have a significant cluster, the criterion's partial
match. The paper's counts (5 and 2) appear only with the whole-epoch windows of power_compute.m,
where S7 adds an identity > spatial effect; there the distance reading gives 52.0% (within
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
c=nb['cells'][10]; print({k:v for k,v in c.items() if k!='source'})
print(nb['cells'][55]['source'][:5]); print(nb['metadata'])
"; grep -n "nbformat" reproduce_johnson_2019.ipynb | tail -2
```

```
{'cell_type': 'code', 'execution_count': None, 'id': 'bb0a42e5', 'metadata': {'tags': ['sanity']}, 'outputs': []}
['for k in ("a", "b"):\n', '    fig, axes = plt.subplots(2, 2, figsize=(12, 6), sharex=True)\n', '    for i, band in enumerate(fcx3.BANDS):\n', '        for j, (other, name) in enumerate([(2, "spatial"), (3, "temporal")]):\n', '            ax = axes[i, j]\n']
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
1711: "nbformat": 4,
1712: "nbformat_minor": 5
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
  t=c['metadata'].get('tags')
  if t: print(i,t)
"
```

```
4 ['sanity']
6 ['sanity']
8 ['sanity']
10 ['sanity']
12 ['sanity']
14 ['sanity']
17 ['claim:table1-electrodes']
20 ['claim:trial-counts']
23 ['claim:fig1b-accuracy']
26 ['claim:fig1b-rt-identity-slower']
29 ['claim:erp-no-condition-difference']
32 ['claim:fig2-spatial-power', 'claim:fig3-temporal-power']
33 ['claim:fig2-spatial-power', 'claim:fig3-temporal-power']
37 ['claim:power-difficulty-subjects']
40 ['claim:power-low-frequencies']
43 ['claim:fig4-maintenance-parietal-led', 'claim:fig4a-delta-theta-shift', 'claim:fig4c-alpha-beta-shift', 'claim:directional-pairs']
44 ['claim:directional-pairs', 'claim:fig4-maintenance-parietal-led', 'claim:fig4a-delta-theta-shift', 'claim:fig4c-alpha-beta-shift']
45 ['claim:fig4-maintenance-parietal-led']
47 ['claim:fig4a-delta-theta-shift', 'claim:fig4c-alpha-beta-shift']
48 ['claim:fig4a-delta-theta-shift', 'claim:fig4c-alpha-beta-shift']
[... 7 more lines not kept]
```

**Agent**

Now the notebook code edits.

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/nbedit.py <<'PYEOF'
import json, uuid
p = "reproduce_johnson_2019.ipynb"
nb = json.load(open(p))
C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.splitlines(keepends=True)
def sub(i, old, new):
    s = src(i); assert s.count(old) == 1, (i, old); setsrc(i, s.replace(old, new))
def cell(kind, s, tags=None):
    c = {"cell_type": kind, "id": uuid.uuid4().hex[:8], "metadata": {"tags": tags} if tags else {}, "source": s.splitlines(keepends=True)}
    if kind == "code": c.update(execution_count=None, outputs=[])
    return c
# keep references by object, insert later
c5, c10, c11, c32, c43, c44, c45, c47, c48, c51, c62 = (C[i] for i in (5, 10, 11, 32, 43, 44, 45, 47, 48, 51, 62))
idx = lambda c: C.index(c)

sub(idx(c5), "docs' channel list names 192 analysed channels in all (Table 1); only those are kept here.",
    "docs' channel list names 187 analysed channels in all (Table 1 gives 192; see table1-electrodes); only those are kept here.")

traces = cell("code", '''# cue-locked 70-150 Hz amplitude (mean over channels and trials) per delay group, the traces behind the timing contrast above
fig, axes = plt.subplots(len(fcx3.SUBJECTS), 3, figsize=(13, 2.0 * len(fcx3.SUBJECTS)), sharex="col")
for i, sid in enumerate(fcx3.SUBJECTS):
    for j, key in enumerate(fcx3.JITTER_WINDOWS):
        v = META[sid]["jitter"][key]
        ax = axes[i, j]
        ax.plot(v["time"], v["trace_900"], color="tab:blue", lw=1, label="900-ms delay")
        ax.plot(v["time"], v["trace_1150"], color="tab:orange", lw=1, label="1150-ms delay")
        for x in {"data_pre": (), "data_encmain": (), "data_proc": (-0.5, 0.3)}[key]:
            ax.axvline(x, color="0.5", lw=0.6, ls=":")
        ax.axvspan(*fcx3.JITTER_WINDOWS[key], color="0.92", zorder=0)
        if key == "data_proc":
            ax.axvspan(*fcx3.PROC_WIN, color="tab:green", alpha=0.08, zorder=0)
        ax.set_title(f"{sid} {key}", fontsize=8)
        ax.tick_params(labelsize=7)
axes[0, 0].legend(fontsize=7)
for ax in axes[-1]:
    ax.set_xlabel("time in the derived epoch (s)", fontsize=8)
fig.suptitle("70-150 Hz amplitude / its mean; grey: window of the contrast; dotted: test cue on and off (data_proc); green: processing window", fontsize=9)
plt.tight_layout()
plt.show()
''', ["sanity"])
C.insert(idx(c11), traces)

sub(idx(c32), '''               "methods_900": "segment zero-padded, 900-ms-delay trials only"}''',
    '''               "methods_900": "segment zero-padded, 900-ms-delay trials only",
               "methods_half": "segment zero-padded, random trials of both delays, as many per condition as methods_900 (control)"}''')
s = src(idx(c32)) + '''print("\\nTrials of the control (methods_half) by delay:", {sid: RES[sid]["n_correct_half_jitter"] for sid in fcx3.SUBJECTS})
print("Subjects per effect, 0.05 per tail, assignment (a): 900-ms-delay trials against the random-trial control")
print(POWER_SUMMARY[POWER_SUMMARY.config.isin(["methods_900", "methods_half"]) & (POWER_SUMMARY["alpha per tail"] == 0.05) & (POWER_SUMMARY["assign"] == "a")][
    ["config", "contrast", "neighbours", "subjects other>id (list)", "subjects id>other (list)"]].to_string(index=False))
'''
setsrc(idx(c32), s)

sub(idx(c43), '''        "b_code": "(b) against psianalysis.m's null (variant)",''',
    '''        "a_trial": "(a), one permutation per trial (P1 null (b))", "b_trial": "(b), one permutation per trial (P1 null (b))",
        "b_code": "(b) against psianalysis.m's null (variant)",''')
sub(idx(c43), '''        for iv in ("maintenance", "processing"):
            zs = {**RES[sid]["psi"][band][iv], **RES[sid]["psi_deposited"][band][iv]}''',
    '''        for iv in ("maintenance", "processing", "processing_900"):
            zs = {**RES[sid]["psi"][band][iv], **RES[sid]["psi_deposited"][band].get(iv, {})}''')

setsrc(idx(c44), '''print("Calibration on the data: processing PSI with each PFC trial paired with another trial's parietal data")
print("(trial order shuffled within subject, so no trial-locked coupling; a calibrated z has mean near 0, SD near 1, and |z| > 1.96 in about 5% of pairs)")
rows = []
SURMEAN = {}
for band in fcx3.BANDS:
    for k in ("a", "b", "a_trial", "b_trial", "b_code"):
        z = np.concatenate([RES[sid]["psi_surrogate"][band][k] for sid in fcx3.SUBJECTS])
        by = {sid: round(float(np.mean(np.abs(RES[sid]["psi_surrogate"][band][k]) > 1.96)), 2) for sid in fcx3.SUBJECTS}
        SURMEAN[(band, k)] = pd.Series({sid: float(np.mean(RES[sid]["psi_surrogate"][band][k])) for sid in fcx3.SUBJECTS})
        rows.append({"band": band, "reading": READ[k], "pairs": len(z), "fraction |z| > 1.96": round(float(np.mean(np.abs(z) > 1.96)), 3),
                     "mean of z": round(float(z.mean()), 2), "SD of z": round(float(z.std()), 2), "|z| > 1.96 by subject": by})
print(pd.DataFrame(rows).to_string(index=False))
print("\\nSurrogate mean z per subject (over the subject's pairs):")
print(pd.DataFrame({f"{b} {k}": v for (b, k), v in SURMEAN.items() if k != "b_code"}).round(2).T.to_string())
print("Trials left in place by the shuffle:", {sid: RES[sid]["psi_surrogate"]["delta-theta"]["same_trial_fraction"] for sid in fcx3.SUBJECTS})
''')

synth = cell("code", '''# Calibration on synthetic data (no data set files): independent PFC and parietal signals, so the true PSI is 0.
# 33 trials of 1/f or 1/f^2 noise, 900-ms segments, the same FFT, ERP removal and null as above (300 shuffles here).
# 'b, segment centred' moves the FFT's time origin to the centre of the segment (a diagnostic, not a reading).
rng_s = np.random.default_rng(fcx3.seed("synthetic"))
fs_s, n_s = 1000, 1300
t_s = np.arange(n_s) / fs_s - 0.2


def noise(kind, n_tr, n_ch):
    w = rng_s.standard_normal((n_tr, n_ch, n_s))
    if kind == "1/f^2":
        return np.cumsum(w, -1)
    f = np.fft.rfftfreq(n_s, 1 / fs_s)
    f[0] = 1
    return np.fft.irfft(np.fft.rfft(w, axis=-1) / np.sqrt(f), n=n_s, axis=-1)


rows = []
for kind in ("1/f", "1/f^2"):
    for band, (lo, hi) in fcx3.BANDS.items():
        zs = {}
        for rep in range(40):
            x = np.concatenate([noise(kind, 33, 4), noise(kind, 33, 4)], 1)
            F, fr = fcx3.fft_segment(x, t_s, fs_s, (0.0, 0.9), np.arange(lo, hi + 1))
            F = F - F.mean(0, keepdims=True)
            ia_s, ib_s = np.repeat(np.arange(4), 4), np.tile(np.arange(4), 4)
            out = fcx3.psi_z(F[:, :4, :, None], F[:, 4:, :, None], ia_s, ib_s, rng_s, n_perm=300, trial_null=True)
            Fc = F * np.exp(2j * np.pi * fr * 0.45)  # origin at the segment's centre (0.45 s)
            out["b, segment centred"] = fcx3.psi_z(Fc[:, :4, :, None], Fc[:, 4:, :, None], ia_s, ib_s, rng_s, n_perm=300)["b"]
            for k, v in out.items():
                zs.setdefault(k, []).append(v[:, 0])
        for k, v in zs.items():
            v = np.concatenate(v)
            rows.append({"noise": kind, "band": band, "reading": READ.get(k, k), "mean of z": round(float(v.mean()), 2),
                         "SE of mean (by run)": round(float(np.std([np.mean(u) for u in zs[k]], ddof=1) / np.sqrt(len(zs[k]))), 2),
                         "SD of z": round(float(v.std()), 2), "fraction |z| > 1.96": round(float(np.mean(np.abs(v) > 1.96)), 3)})
print(pd.DataFrame(rows).to_string(index=False))
''', ["claim:fig4c-alpha-beta-shift", "claim:fig5a-spatiotemporal-bidirectional", "claim:fig5b-alpha-beta-no-sustained"])
C.insert(idx(c44) + 1, synth)

for c in (c45, c47):
    sub(idx(c), 'for k in ("a", "b", "b_code", "code", "code_rev"):', 'for k in ("a", "b", "a_trial", "b_trial", "b_code", "code", "code_rev"):')
s = src(idx(c48)).replace('for k in ("a", "b", "b_code", "code", "code_rev"):', 'for k in ("a", "b", "a_trial", "b_trial", "b_code", "code", "code_rev"):')
s += '''print("\\nfig4c: processing alpha-beta subject means against the same subject's trial-shuffled surrogate mean (an offset of the null shows in both)")
for k in ("a", "b", "a_trial", "b_trial"):
    v = persub.loc[("alpha-beta", "processing", k)]
    d = v - SURMEAN[("alpha-beta", k)]
    print(f"  {READ[k]}: observed {v.round(2).to_dict()}; surrogate {SURMEAN[('alpha-beta', k)].round(2).to_dict()};"
          f" subjects below their surrogate {int((d < 0).sum())}/7; observed - surrogate {d.mean():.2f} +- {d.std(ddof=1):.2f}, paired t(6) p {stats.ttest_1samp(d, 0).pvalue:.3g}")
print("\\nProcessing PSI on the 900-ms-delay trials only (subject means):")
for band in fcx3.BANDS:
    for k in ("a", "b"):
        v = persub.loc[(band, "processing_900", k)]
        print(f"  {band}, {READ[k]}: above 0 {int((v > 0).sum())}/7, below 0 {int((v < 0).sum())}/7; mean {v.mean():.2f} +- {v.std(ddof=1):.2f}; {v.round(2).to_dict()}")
'''
setsrc(idx(c48), s)
sub(idx(c51), 'for k in ("a", "b", "b_code", "code", "code_rev"):', 'for k in ("a", "b", "a_trial", "b_trial", "b_code", "code", "code_rev"):')
sub(idx(c51), 'if k in ("a", "b", "b_code"):', 'if k in ("a", "b", "a_trial", "b_trial", "b_code"):')

subj = cell("code", '''# subject-level test of the time-resolved contrasts: per subject the mean z over its selected pairs, a paired t-test
# over subjects at each time point, Benjamini-Hochberg over the 91 points (pairs that share electrodes are not counted
# as independent)
def subject_stats(config, band, k, other):
    d = TR[(config, band, k)]
    zi = pd.DataFrame(d["z"][1]).groupby(d["subject"]).mean()
    zo = pd.DataFrame(d["z"][other]).groupby(d["subject"]).mean()
    if len(zi) < 3:
        return None
    t, p = stats.ttest_rel(zi.values, zo.values, axis=0)
    sig = fcx3.fdr_bh(p)
    runs = [(int(a), int(b), sign) for sign in (1, -1) for a, b in fcx3.runs(sig & (np.sign(t) == sign), TIMES)]
    return len(zi), p, sig, sorted(runs)


for band in fcx3.BANDS:
    for config in fcx3.PSI_T_CONFIGS:
        for k in ("a", "b"):
            for other, name in [(2, "spatial"), (3, "temporal")]:
                r = subject_stats(config, band, k, other)
                if r is None:
                    print(f"{band}, {TCFG[config]}, {READ[k]}, identity vs {name}: fewer than 3 subjects, no test")
                    continue
                n, p, sig, runs = r
                print(f"{band}, {TCFG[config]}, {READ[k]}, identity vs {name}: {n} subjects; FDR-significant points {int(sig.sum())}/91"
                      f" (smallest p {p.min():.3g}); runs {runs}")
for k in ("a", "b"):
    d = TR[("methods", "alpha-beta", k)]
    print(f"alpha-beta pairs per subject, {READ[k]}:", pd.Series(d["subject"]).value_counts().sort_index().to_dict())
''', ["claim:fig5b-alpha-beta-no-sustained"])
C.insert(idx(c62) + 1, subj)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False)
open(p, "a").write("\n")
PYEOF
python3 $TMPDIR/nbedit.py && git diff --stat
```

```
entries/crcns-fcx-3-johnson-2019/fcx3.py           |  53 +++++-
 .../reproduce_johnson_2019.ipynb                   | 179 +++++++++++++++++++--
 2 files changed, 211 insertions(+), 21 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/devall.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0, ".")
import fcx3
fcx3.analyse_subject.__defaults__ = (50, True)
CHAN = fcx3.channel_table()
META, RES = {}, {}
for sid in fcx3.SUBJECTS:
    t0 = time.time()
    chan = CHAN[CHAN.subject == sid].reset_index(drop=True)
    META[sid], RES[sid] = fcx3.load_subject(sid, chan)
    print(sid, time.time() - t0, flush=True)
pickle.dump((META, RES), open("/tmp/claude-1001/devall.pkl", "wb"), protocol=4)
EOF
date -u; time $TMPDIR/venv/bin/python $TMPDIR/devall.py
```

```
Mon Nov  9 01:11:06 UTC 2026
s1 148.54830932617188
s2 201.82857847213745
s3 631.331925868988
s4 112.63442492485046
s5 271.0475935935974
s6 112.55554294586182
s7 48.96175527572632

real	25m28.841s
user	29m0.915s
sys	1m0.594s
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; date -u; python3 - <<'EOF'
import json
nb = json.load(open("reproduce_johnson_2019.ipynb"))
nb["cells"][2]["source"] = ["import pickle\n", "CHAN = fcx3.channel_table()\n", "SUMMARY = fcx3.summary_file()\n", "META, RES = pickle.load(open('/tmp/claude-1001/devall.pkl', 'rb'))\n"]
json.dump(nb, open("/tmp/claude-1001/devtest.ipynb", "w"))
EOF
$TMPDIR/venv/bin/pip install -q nbconvert ipykernel 2>&1 | tail -1; cp fcx3.py $TMPDIR/; cd $TMPDIR && time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute devtest.ipynb --output devtest_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
Mon Nov  9 01:36:42 UTC 2026
[notice] To update, run: /tmp/claude-1001/venv/bin/python -m pip install --upgrade pip
[31m    [39m[31m["contrast", "neighbours", "subjects other>id (list)", "subjects id>other (list)"]].to_string(index=False))print("\nTrials of the control (methods_half) by delay:", {sid: RES[sid]["n_correct_half_jitter"] for sid in fcx3.SUBJECTS})[39m
                                                                                                               ^
[31mSyntaxError[39m[31m:[39m invalid syntax



real	0m7.973s
user	0m6.205s
sys	0m0.550s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 - <<'EOF'
import json
p="reproduce_johnson_2019.ipynb"
nb = json.load(open(p))
for i,c in enumerate(nb["cells"]):
    s="".join(c["source"])
    for bad in ['.to_string(index=False))print(', ')print("\\n']:
        if bad in s:
            print("fix", i)
    s = s.replace('.to_string(index=False))print(', '.to_string(index=False))\nprint(')
    s = s.replace('pvalue:.3g}")print(', 'pvalue:.3g}")\nprint(')
    import re
    s2 = re.sub(r'\)print\(', ')\nprint(', s)
    if s2 != s: print("regex fix", i)
    c["source"] = s2.splitlines(keepends=True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
git diff --stat
```

```
fix 33
fix 33
fix 50
regex fix 50
 entries/crcns-fcx-3-johnson-2019/fcx3.py           |  53 +++++-
 .../reproduce_johnson_2019.ipynb                   | 181 +++++++++++++++++++--
 2 files changed, 213 insertions(+), 21 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
print(''.join(nb['cells'][50]['source'])[-1400:])"; python3 - <<'EOF'
import json
nb = json.load(open("reproduce_johnson_2019.ipynb"))
nb["cells"][2]["source"] = ["import pickle\n", "CHAN = fcx3.channel_table()\n", "SUMMARY = fcx3.summary_file()\n", "META, RES = pickle.load(open('/tmp/claude-1001/devall.pkl', 'rb'))\n"]
json.dump(nb, open("/tmp/claude-1001/devtest.ipynb", "w"))
EOF
cd $TMPDIR && time $TMPDIR/venv/bin/jupyter nbconvert --to notebook --execute devtest.ipynb --output devtest_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
.3g}")
print("fig4c-alpha-beta-shift: expected every subject below 0 in processing, mean -12.60 (tol 1.26 or more negative), F 2302.30 +- 230.2")
for k in ("a", "b", "a_trial", "b_trial", "b_code", "code", "code_rev"):
    v = persub.loc[("alpha-beta", "processing", k)]
    eff, F, p, n = LME[("alpha-beta", k)]
    print(f"  {READ[k]}: subjects below 0: {int((v < 0).sum())}/7; mean {v.mean():.2f} +- {v.std(ddof=1):.2f}; model effect {eff:+.2f}, F {F:.1f}, p {p:.3g}")
print("\nfig4c: processing alpha-beta subject means against the same subject's trial-shuffled surrogate mean (an offset of the null shows in both)")
for k in ("a", "b", "a_trial", "b_trial"):
    v = persub.loc[("alpha-beta", "processing", k)]
    d = v - SURMEAN[("alpha-beta", k)]
    print(f"  {READ[k]}: observed {v.round(2).to_dict()}; surrogate {SURMEAN[('alpha-beta', k)].round(2).to_dict()};"
          f" subjects below their surrogate {int((d < 0).sum())}/7; observed - surrogate {d.mean():.2f} +- {d.std(ddof=1):.2f}, paired t(6) p {stats.ttest_1samp(d, 0).pvalue:.3g}")
print("\nProcessing PSI on the 900-ms-delay trials only (subject means):")
for band in fcx3.BANDS:
    for k in ("a", "b"):
        v = persub.loc[(band, "processing_900", k)]
        print(f"  {band}, {READ[k]}: above 0 {int((v > 0).sum())}/7, below 0 {int((v < 0).sum())}/7; mean {v.mean():.2f} +- {v.std(ddof=1):.2f}; {v.round(2).to_dict()}")

[NbConvertApp] Converting notebook devtest.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json
nb = json.load(open("devtest_out.ipynb"))
for i in [45, 46, 50, 69]:
    c = nb["cells"][i]
    print("=====", i)
    for o in c.get("outputs", []):
        print("".join(o.get("text", ""))[:6000])
EOF
```

```
Exit code 1
===== 45
Calibration on the data: processing PSI with each PFC trial paired with another trial's parietal data
(trial order shuffled within subject, so no trial-locked coupling; a calibrated z has mean near 0, SD near 1, and |z| > 1.96 in about 5% of pairs)
       band                                      reading  pairs  fraction |z| > 1.96  mean of z  SD of z                                                                |z| > 1.96 by subject
delta-theta                 (a) trial-averaged coherency   1135                0.060      -0.05     1.01   {'s1': 0.14, 's2': 0.04, 's3': 0.06, 's4': 0.0, 's5': 0.08, 's6': 0.06, 's7': 0.1}
delta-theta                   (b) per-trial PSI averaged   1135                0.001      -0.29     0.60        {'s1': 0.0, 's2': 0.0, 's3': 0.0, 's4': 0.0, 's5': 0.0, 's6': 0.0, 's7': 0.0}
delta-theta (a), one permutation per trial (P1 null (b))   1135                0.066      -0.06     1.02 {'s1': 0.14, 's2': 0.08, 's3': 0.05, 's4': 0.13, 's5': 0.08, 's6': 0.06, 's7': 0.15}
delta-theta (b), one permutation per trial (P1 null (b))   1135                0.067      -0.51     1.00  {'s1': 0.29, 's2': 0.02, 's3': 0.06, 's4': 0.2, 's5': 0.09, 's6': 0.03, 's7': 0.05}
delta-theta   (b) against psianalysis.m's null (variant)   1135                0.900       4.35    26.01  {'s1': 0.86, 's2': 0.89, 's3': 0.91, 's4': 0.9, 's5': 0.86, 's6': 0.91, 's7': 0.95}
 alpha-beta                 (a) trial-averaged coherency   1135                0.069       0.02     1.04  {'s1': 0.05, 's2': 0.07, 's3': 0.07, 's4': 0.07, 's5': 0.07, 's6': 0.06, 's7': 0.0}
 alpha-beta                   (b) per-trial PSI averaged   1135                0.063       0.15     1.04  {'s1': 0.24, 's2': 0.05, 's3': 0.06, 's4': 0.03, 's5': 0.06, 's6': 0.12, 's7': 0.0}
 alpha-beta (a), one permutation per trial (P1 null (b))   1135                0.063       0.02     1.04 {'s1': 0.05, 's2': 0.07, 's3': 0.06, 's4': 0.03, 's5': 0.05, 's6': 0.09, 's7': 0.05}
 alpha-beta (b), one
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json
nb = json.load(open("devtest_out.ipynb"))
print(len(nb["cells"]))
for i in [12, 35, 66, 67]:
    c = nb["cells"][i]
    print("=====", i, "".join(c["source"])[:80])
    for o in c.get("outputs", []):
        print("".join(o.get("text", ""))[-3500:])
EOF
```

```
68
===== 12 The test is weak where the 70-150 Hz response is small; the column "clear" marks
===== 35 **Result: partially reproduced.** Under the main spectra, 5 subjects show spatia
===== 66 **Result: reproduced, resting on an assumption.** With PSI reading (b) adopted (
===== 67 ## Summary

A failure to reproduce here may be a failure of this attempt, not of
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json
nb = json.load(open("devtest_out.ipynb"))
for i in [11, 34, 64, 65]:
    c = nb["cells"][i]
    print("=====", i, "".join(c["source"])[:80])
    for o in c.get("outputs", []):
        print("".join(o.get("text", ""))[-3000:], list(o.get("data", {}).keys()))
EOF
```

```
===== 11 # cue-locked 70-150 Hz amplitude (mean over channels and trials) per delay group
 ['image/png', 'text/plain']
===== 34 print("Per-subject % of electrodes, 'other > identity / identity > other', main 
0/9          0/9          0/9         0/9         0/9          0/9          0/9         0/4         0/4          0/4          0/4
s2         6/0         6/0          6/0          6/0        28/0        28/0         19/0         19/0         6/0         6/0          3/0          3/0
s3        50/0        50/0         50/0         50/0        94/0        94/0         94/0         94/0        10/0        10/0          7/0          7/0
s4        24/0        24/0         24/0         24/0        24/0        24/0         24/0         24/0        18/6        18/6         12/6         12/6
s5        69/0        69/0         69/0         69/0        88/0        88/0         88/0         88/0        31/0        31/0         23/0         23/0
s6        25/0        25/0         25/0         25/0        67/0        67/0         67/0         67/0         8/0         8/0          8/0          8/0
s7       22/33        0/33        22/33         0/33       22/33        0/33        22/33         0/33       11/22        0/22        11/22         0/22

Smallest cluster p of each sign and subject, main spectra; paper: all p < 0.04 for the effects it reports
contrast subject  adjacent other>id  distance other>id  none other>id  adjacent id>other  distance id>other  none id>other
 spatial      s1               0.38               0.36           0.88               0.82               0.78           0.60
 spatial      s2               0.00               0.00           0.00               0.64               0.52           0.42
 spatial      s3               0.00               0.00           0.00               0.10               0.44           0.12
 spatial      s4               0.00               0.00           0.00               0.00               0.00           0.00
 spatial      s5     
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json, base64
nb = json.load(open("devtest_out.ipynb"))
c = nb["cells"][33]
for o in c.get("outputs", []):
    t = "".join(o.get("text", ""))
    print(t[t.find("Trials of the control"):][:3000])
o = nb["cells"][11]["outputs"][0]
open("traces.png","wb").write(base64.b64decode(o["data"]["image/png"]))
EOF
```

```
Trials of the control (methods_half) by delay: {'s1': {900: 23, 1150: 28}, 's2': {900: 23, 1150: 24}, 's3': {900: 22, 1150: 27}, 's4': {900: 29, 1150: 25}, 's5': {900: 24, 1150: 22}, 's6': {900: 22, 1150: 16}, 's7': {900: 21, 1150: 21}}
Subjects per effect, 0.05 per tail, assignment (a): 900-ms-delay trials against the random-trial control
      config contrast neighbours subjects other>id (list) subjects id>other (list)
 methods_900  spatial   adjacent                 [s2, s3]                       []
 methods_900  spatial   distance                 [s3, s5]                       []
 methods_900  spatial       none             [s2, s3, s5]                       []
 methods_900 temporal   adjacent                 [s5, s7]                     [s1]
 methods_900 temporal   distance                 [s5, s7]                     [s1]
 methods_900 temporal       none                     [s5]                     [s1]
methods_half  spatial   adjacent                 [s2, s3]                     [s7]
methods_half  spatial   distance                 [s2, s3]                     [s7]
methods_half  spatial       none                 [s2, s7]                       []
methods_half temporal   adjacent             [s3, s4, s7]                     [s1]
methods_half temporal   distance             [s3, s4, s7]                     [s1]
methods_half temporal       none             [s3, s4, s7]                       []
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/traces.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/crcns-fcx-3-johnson-2019 2>&1 | tail -15; date -u
```

```
Mon Nov  9 01:38:33 UTC 2026
Installed kernelspec registry-crcns-fcx-3-johnson-2019 in executed/crcns-fcx-3-johnson-2019/.venv/share/jupyter/kernels/registry-crcns-fcx-3-johnson-2019
0 error(s)
pass  reproduce_johnson_2019.ipynb  (2573 s)

real	43m2.223s
user	84m53.692s
sys	1m3.874s
Mon Nov  9 02:21:35 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls executed/crcns-fcx-3-johnson-2019/; python3 - <<'EOF' > $TMPDIR/out.txt
import json
nb = json.load(open("executed/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    print("=====", i)
    for o in c.get("outputs", []):
        print("".join(o.get("text", "")) or "".join(o.get("data", {}).get("text/plain", "")))
EOF
wc -l $TMPDIR/out.txt; grep -n "=====" $TMPDIR/out.txt | head -50
```

```
reproduce_johnson_2019.ipynb
result.json
1034 /tmp/claude-1001/out.txt
1:===== 1
34:===== 2
51:===== 4
87:===== 6
100:===== 8
111:===== 10
138:===== 11
140:===== 13
156:===== 15
231:===== 18
246:===== 21
270:===== 24
287:===== 27
308:===== 30
415:===== 33
546:===== 34
584:===== 38
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 34,50p $TMPDIR/out.txt; sed -n 308,330p $TMPDIR/out.txt; sed -n 400,415p $TMPDIR/out.txt; sed -n 520,546p $TMPDIR/out.txt
```

```
===== 2
s1: streamed and analysed in 240 s

s2: streamed and analysed in 361 s

s3: streamed and analysed in 807 s

s4: streamed and analysed in 196 s

s5: streamed and analysed in 385 s

s6: streamed and analysed in 439 s

s7: streamed and analysed in 95 s

all subjects in 42.0 min

===== 30
==== methods: segments padded, 30-Hz low-pass, baseline mean over trials (main)
neighbours        adjacent  distance   none
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "methods_half\|methods_900" $TMPDIR/out.txt | head -5; awk 'NR>=330 && NR<=415' $TMPDIR/out.txt | grep -A30 "==== methods_900\|==== methods_half" | cut -c1-200
```

```
377:==== methods_900: as main, 900-ms-delay trials only
409:       methods_900   adjacent         1          1          4       0.023
410:       methods_900   distance         0          0          1       0.067
411:       methods_900       none         0          0          2       0.053
468:==== methods_900: segment zero-padded, 900-ms-delay trials only
==== methods_900: as main, 900-ms-delay trials only
neighbours        adjacent  distance   none
subject contrast                           
s1      spatial      0.402     0.433  0.493
        temporal     0.315     0.354  0.306
s2      spatial      0.541     0.176  0.520
        temporal     0.070     0.067  0.053
s3      spatial      0.086     0.253  0.289
        temporal     0.080     0.419  0.280
s4      spatial      0.567     0.578  0.455
        temporal     0.198     0.207  0.109
s5      spatial      0.670     0.539  0.644
        temporal     0.023     0.122  0.059
s6      spatial      0.802     0.813  0.727
        temporal     0.332     0.357  0.214
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 468,520p $TMPDIR/out.txt | cut -c1-260
```

```
==== methods_900: segment zero-padded, 900-ms-delay trials only
contrast neighbours  alpha per tail assign  subjects other>id  subjects id>other   % other>id % id>other  counts match  % match  counts within 1
 spatial   adjacent           0.050      a                  2                  0  14.2 +- 6.9          -         False    False            False
 spatial   adjacent           0.050      b                  2                  0  14.2 +- 6.9          -         False    False            False
 spatial   adjacent           0.025      a                  2                  0   9.8 +- 0.6          -         False    False            False
 spatial   adjacent           0.025      b                  2                  0   9.8 +- 0.6          -         False    False            False
 spatial   distance           0.050      a                  3                  0 46.2 +- 13.9          -         False    False            False
 spatial   distance           0.050      b                  3                  0 46.2 +- 13.9          -         False    False            False
 spatial   distance           0.025      a                  2                  0 52.1 +- 13.4          -         False    False            False
 spatial   distance           0.025      b                  2                  0 52.1 +- 13.4          -         False    False            False
 spatial       none           0.050      a                  3                  0   4.3 +- 1.7          -         False    False            False
 spatial       none           0.050      b                  3                  0   4.3 +- 1.7          -         False    False            False
 spatial       none           0.025      a                  2                  0   3.0 +- 0.1          -         False    False            False
 spatial       none           0.025      b                  2                  0   3.0 +- 0.1          -         False    False            False
temporal   adjacent           0.050      a         
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 677,902p $TMPDIR/out.txt | cut -c1-330
```

```
===== 44
Pairs per subject: {'s1': 21, 's2': 116, 's3': 756, 's4': 30, 's5': 160, 's6': 32, 's7': 20}
Frequencies read (Hz): {'delta-theta': [2.0, 3.067, 4.0, 5.067, 6.0, 7.067], 'alpha-beta': [9.067, 10.0, 11.067, 12.0, 13.067, 14.0, 15.067, 16.0, 17.067, 18.0, 19.067, 20.0, 21.067, 22.0, 23.067, 24.0]}

Per-subject mean PSI z over pairs:
subject                                 s1     s2     s3     s4     s5     s6     s7
band        interval       reading                                                  
alpha-beta  maintenance    a         -0.42  -0.15   0.01  -0.67  -0.19   0.04  -0.28
                           a_trial   -0.47  -0.12   0.00  -0.73  -0.18   0.05  -0.25
                           b         -0.25  -0.27  -0.37  -0.25  -0.48  -0.05  -0.18
                           b_code     1.94   2.22   0.34   2.56  -1.24   4.71   4.21
                           b_trial   -0.34  -0.37  -0.53  -0.38  -0.70  -0.02  -0.19
                           code      69.64  79.37  77.48  75.01  70.70  51.98  62.18
                           code_rev -75.32 -71.47 -82.01 -75.49 -71.92 -52.74 -59.85
            processing     a         -0.31  -0.05   0.18  -0.16  -0.31  -0.49   0.19
                           a_trial   -0.33  -0.04   0.18  -0.22  -0.30  -0.45   0.20
                           b         -1.07  -0.51   0.46  -0.61  -0.72  -1.35  -0.18
                           b_code   -11.72  -1.91  16.28  -0.40  -5.00 -14.70   4.56
                           b_trial   -1.61  -0.66   0.69  -0.86  -0.98  -1.70  -0.22
                           code      92.24  70.01  67.29  74.88  68.16  57.39  69.66
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 902,1034p $TMPDIR/out.txt | cut -c1-600
```

```
===== 56
methods, delta-theta, (a) trial-averaged coherency, identity vs spatial: pairs 78 in 7 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, delta-theta, (a) trial-averaged coherency, identity vs temporal: pairs 78 in 7 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, delta-theta, (b) per-trial PSI averaged, identity vs spatial: pairs 1 in 1 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, delta-theta, (b) per-trial PSI averaged, identity vs temporal: pairs 1 in 1 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, alpha-beta, (a) trial-averaged coherency, identity vs spatial: pairs 104 in 7 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, alpha-beta, (a) trial-averaged coherency, identity vs temporal: pairs 104 in 7 subjects; FDR-significant points 0/91; runs (start ms, end ms, sign of identity - other, sustained) []
methods, alpha-beta, (b) per-trial PSI averaged, identity vs spatial: pairs 74 in 6 subjects; FDR-significant points 30/91; runs (start ms, end ms, sign of identity - other, sustained) [(40, 40, 1, False), (130, 130, 1, False), (170, 190, 1, False), (250, 250, -1, False), (280, 290, 1, False), (300, 300, -1, False), (340, 350, -1, False), (380, 400, 1, False), (410, 450, -1, False), (550, 550, -1, False), (650, 650, 1, False), (670, 670, 1, False), (690, 720, 1, False), (750, 760, -1, False), (870, 870, -1, False), (900, 900, -1, False)]
methods, alpha-beta, (b) per-trial PSI averaged, identity vs temporal: pairs 74 in 6 subjects; FDR-significant points 35/91; runs (start ms, end ms, sign of identity - other, sustained) [(40, 40, 1, False), (250, 260, -1, False), (280, 320, 1, False), (330, 360, -1, False), (380, 380, 1, False), (400, 400, 1,
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
import pprint
def find(o,k):
  if isinstance(o,dict):
    for kk,v in o.items():
      if kk==k: pprint.pprint(v, width=150); 
      find(v,k)
  elif isinstance(o,list):
    for v in o: find(v,k)
find(s,'verifications')
" | head -80
```

```
{'items': {'additionalProperties': False,
           'properties': {'by': {'type': 'string'},
                          'date': {'format': 'date', 'type': 'string'},
                          'kind': {'enum': ['agent', 'person', 'paper_author']},
                          'results': {'items': {'additionalProperties': False,
                                                'properties': {'agrees': {'type': 'boolean'},
                                                               'claim': {'type': 'string'},
                                                               'outcome': {'description': 'The outcome the verifier would give.',
                                                                           'enum': ['reproduced',
                                                                                    'partially_reproduced',
                                                                                    'not_reproduced',
                                                                                    'blocked']},
                                                               'reason': {'description': "The verifier's reason, in its own words.",
                                                                          'type': 'string'},
                                                               'response': {'description': 'What the author changed or replied, kept apart from the '
                                                                                           "verifier's reason.",
                                                                            'type': 'string'}},
                                                'required': ['claim', 'agrees'],
                                                'type': 'object'},
                                      'type': 'array'},
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 245,290p schemas/attempt.schema.json; grep -rn "proposed:" attempts/*.yaml | head -3
```

```
"minLength": 1
            }
          },
          "assumed": {
            "description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
            "type": "boolean"
          },
          "proposed": {
            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
            "type": "object",
            "additionalProperties": false,
            "required": [
              "outcome",
              "reason"
            ],
            "properties": {
              "outcome": {
                "enum": [
                  "reproduced",
                  "partially_reproduced",
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown': print(i, s[:70].replace(chr(10),' '))
"; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i in [36,39,59,61]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
0 # Reproducing Johnson et al. (2019) from CRCNS data set fcx-3  **Paper
3 ## Data check  Each check of the description against the values is sta
5 The description says the derived structures have `fsample: 1000`; S7's
7 The description says the trial table lists each trial; in S6 and S7 it
9 Each derived trace is the difference of the channel's contact and one 
12 The test is weak where the 70-150 Hz response is small; the column "cl
14 The 'distance' reading places each bipolar channel at the midpoint of 
16 The deposited scripts settle some details and not others, as printed a
17 ## table1-electrodes  > The analysed data comprise 192 bipolar virtual
19 **Result: partially reproduced.** The data set's channel list holds 18
20 ## trial-counts  > After artifact rejection subjects kept on average 9
22 **Result: reproduced.** Correct trials kept average 95.71 per subject 
23 ## fig1b-accuracy  > All subjects were proficient at the task (accurac
25 **Result: reproduced.** Under reading (b), per subject and condition, 
26 ## fig1b-rt-identity-slower  > Response times differed by condition, b
28 **Result: reproduced.** On subject-condition means (reading (a)), cond
29 ## erp-no-condition-difference  > ERPs over the processing interval di
31 **Result: not reproduced, resting on an assumption.** Under the main r
32 ## fig2-spatial-power and fig3-temporal-power  > In the identity again
35 **Result: partially reproduced.** Under the main spectra, 5 subjects s
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i in [12]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 12
The test is weak where the 70-150 Hz response is small; the column "clear" marks the windows where
the shift found exceeds every shuffled one and the alignment is better than every shuffled one.
If the processing columns of 1150-ms trials lie about 0.25 s before the events, the processing
window of those trials would hold the end of the cue. The ERP and power tests are therefore also
run on the trials with a 900-ms delay only (configuration `methods_900`), whose windows are not in
question; with about half the trials these tests have less power.
```

**Agent calls Bash**

```bash
sed -n 111,137p $TMPDIR/out.txt
```

```
===== 10
Timing contrast between 900-ms and 1150-ms delay trials (70-150 Hz amplitude; see fcx3.jitter_check).
If the columns mark the events, the best shift is near 0 in every window; a shift beyond the shuffled maximum, with r
above the shuffled maximum, means the events lie at different times relative to the column in the two groups.
subject        epoch  window (s)  shift 1150 vs 900 (s)    r  shuffled max |shift|  shuffled max r  clear
     s1     data_pre  (0.6, 1.6)                 -0.396 0.05                 0.400            0.18  False
     s1 data_encmain (-0.3, 1.0)                 -0.146 0.05                 0.400            0.13  False
     s1    data_proc (-0.9, 0.7)                  0.290 0.15                 0.400            0.18  False
     s2     data_pre  (0.6, 1.6)                  0.020 0.55                 0.123            0.62  False
     s2 data_encmain (-0.3, 1.0)                  0.296 0.28                 0.374            0.25  False
     s2    data_proc (-0.9, 0.7)                  0.229 0.61                 0.032            0.60   True
     s3     data_pre  (0.6, 1.6)                 -0.030 0.34                 0.083            0.40  False
     s3 data_encmain (-0.3, 1.0)                  0.105 0.26                 0.150            0.32  False
     s3    data_proc (-0.9, 0.7)                  0.214 0.47                 0.056            0.45   True
     s4     data_pre  (0.6, 1.6)                  0.009 0.32                 0.128            0.39  False
     s4 data_encmain (-0.3, 1.0)                  0.263 0.65                 0.119            0.55   True
     s4    data_proc (-0.9, 0.7)                  0.256 0.76                 0.083            0.73   True
     s5     data_pre  (0.6, 1.6)                 -0.300 0.11                 0.400            0.17  False
     s5 data_encmain (-0.3, 1.0)                  0.224 0.29                 0.273            0.38  False
     s5    data_proc (-0.9, 0.7)                  0.276 0.37           
[... 6 more lines not kept]
```

**Agent**

Now the markdown edits for the data and power sections.

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/md1.py <<'PYEOF'
import json
p = "reproduce_johnson_2019.ipynb"
nb = json.load(open(p)); C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.rstrip("\n").splitlines(keepends=True)
def sub(i, old, new):
    s = src(i); assert s.count(old) == 1, (i, old[:60]); setsrc(i, s.replace(old, new))
sub(0, "each is streamed once, decompressed in memory, reduced to what the claims use, and released. This\ntakes about 20 of the run's 35 minutes.",
    "each is streamed once, decompressed in memory, reduced to what the claims use, and released. The\nloading cell, which streams and analyses each subject in turn, takes about 42 of the run's 43 minutes.")
setsrc(12, '''The test is weak where the 70-150 Hz response is small; the column "clear" marks the windows where
the shift found exceeds every shuffled one and the alignment is better than every shuffled one.
The traces show the same: S4's response to the stimuli and to the test cue comes about 0.25 s later
in the 1150-ms trials, relative to the columns, in the encoding and processing epochs; in the
other subjects the 70-150 Hz response is small and the two groups' traces differ little by eye.
If the processing columns of 1150-ms trials lie about 0.25 s before the events, the processing
window of those trials would hold the end of the cue. The ERP and power tests and the task-induced
PSI are therefore also run on the trials with a 900-ms delay only (configuration `methods_900`, and
interval `processing_900` for PSI), whose windows are not in question. With about half the trials
these tests have less power, so power is also run on a random draw of trials of both delays with
as many trials per condition (`methods_half`), which separates the loss of trials from the timing.''')
sub(31, "(S5 identity against temporal, p = 0.023). The deciding p values lie between 0.02 and 0.05, so\nthe outcome is close to the threshold under every reading.",
    "(S5 identity against temporal, p = 0.023). Under the adopted reading the deciding p (0.041) is\nclose to 0.05, so a different Monte Carlo draw could move it to either side; the distance reading's\np = 0.014 is not close to the threshold.")
sub(35, "significant clusters of the main spectra have p <= 0.028. On the 900-ms-delay trials alone 2 or 3\nsubjects show spatial > identity effects and none identity > spatial.",
    "significant clusters of the main spectra have p <= 0.028. On the 900-ms-delay trials alone 2 or 3\nsubjects show spatial > identity effects and none identity > spatial. A random draw of as many\ntrials from both delays loses about as much (1 to 3 subjects spatial > identity, 0 or 1 identity >\nspatial), so the loss on the 900-ms trials comes from having fewer trials and does not show that\nthe effects depend on the 1150-ms trials' timing; with half the trials these tests cannot settle it\neither way, here or for power-difficulty-subjects, which rests on the same effects.")
sub(36, "(p = 0.044). On the 900-ms-delay trials alone 1 to 3 subjects show temporal > identity effects.",
    "(p = 0.044). On the 900-ms-delay trials alone 1 to 3 subjects show temporal > identity effects and\n1 (S1) identity > temporal; the random draw of as many trials from both delays gives 2 or 3 and 0\nor 1, as for fig2-spatial-power.")
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
PYEOF
python3 $TMPDIR/md1.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 - <<'EOF'
import json
p = "reproduce_johnson_2019.ipynb"
nb = json.load(open(p)); c = nb["cells"][12]
s = "".join(c["source"])
old = """The traces show the same: S4's response to the stimuli and to the test cue comes about 0.25 s later
in the 1150-ms trials, relative to the columns, in the encoding and processing epochs; in the
other subjects the 70-150 Hz response is small and the two groups' traces differ little by eye."""
new = """In the traces, S4's response to the stimuli and to the test cue comes about 0.25 s later in the
1150-ms trials, relative to the columns, in the encoding and processing epochs. The shifts of S2
and S3 in the processing epoch (table) are small by eye, and in the other subjects the 70-150 Hz
response is small."""
assert old in s; c["source"] = s.replace(old, new).splitlines(keepends=True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
EOF
date -u
```

```
Mon Nov  9 02:22:56 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json;nb=json.load(open('reproduce_johnson_2019.ipynb'))
print(''.join(nb['cells'][43]['source'])[-600:]); print(''.join(nb['cells'][55]['source']))"
```

```
against that null is shown as a variant (`b_code`).
The deposited code without the conjugate, whose measure equals plus or minus exp(2i x the second
channel's phase) and so depends on one channel only, is shown with either channel first for the
record of that code mismatch; it is not a reading of the paper and decides no outcome. As a check of
calibration on these data, each subject's processing PSI is also computed with the parietal trials
paired with other trials' PFC data, which removes any trial-locked coupling; a calibrated z then
exceeds 1.96 in about 5% of pairs. Positive z: PFC leads.
## Time-resolved PSI: fig5a-delta-theta-epochs, fig5a-identity-direction, fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained

> Time-resolved delta-theta PSI differed between conditions in sustained epochs at 0 to 120 ms and
> 470 to 610 ms (identity against spatial) and at 0 to 170 ms and 660 to 860 ms (identity against
> temporal) after the test cue, the spatial late epoch ending about 50 ms before the temporal one
> begins.

> In identity trials the PFC led parietal sites early in processing (z > 2.62 and z > 2.35 in the
> two contrasts' early epochs) and the parietal cortex led later (z < -3.04 and z < -3.57).

> Delta-theta PSI during the selection of spatial and of temporal information stayed bidirectional
> (net near zero) throughout the processing interval.

[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/md2.py <<'PYEOF'
import json
p = "reproduce_johnson_2019.ipynb"
nb = json.load(open(p)); C = nb["cells"]
def src(i): return "".join(C[i]["source"])
def setsrc(i, s): C[i]["source"] = s.strip("\n").splitlines(keepends=True)
def sub(i, old, new):
    s = src(i); assert s.count(old) == 1, (i, old[:60]); setsrc(i, s.replace(old, new))
assert src(43).startswith("## Task-induced PSI")
sub(43, "exceeds 1.96 in about 5% of pairs. Positive z: PFC leads.", """exceeds 1.96 in about 5% of pairs. Positive z: PFC leads.

P1 also leaves open whether each shuffle permutes the bins in the same way for all trials (null
reading (a), used above) or with its own permutation per trial (null reading (b)); both are run for
readings (a) and (b) (`a_trial`, `b_trial`).

**Which reading is adopted.** Where the readings give different outcomes, reading (a) with null
reading (a) is adopted: it is the first P1 lists, the measure of Nolte et al. (2008), and the one
whose z is calibrated. On the trial-shuffled data below, its z has mean -0.05 (delta-theta) and
0.02 (alpha-beta), SD 1.01 and 1.04, and passes |z| > 1.96 in 6.0% and 6.9% of pairs. Reading (b)
has mean -0.29 and SD 0.60 in delta-theta (0.1% of pairs pass), and its subject means on the
trial-shuffled data run from -1.25 to 0.52 in alpha-beta, where the true value is 0. On independent
synthetic signals (the cell after the calibration) its mean z is -0.21 to -0.37, where reading (a)
gives -0.07 to -0.15 with SD near 1. Moving the FFT's time origin to the centre of the segment
brings reading (b)'s mean to -0.06 to 0.12, which is consistent with the offset coming from the
phase slope that each trial's spectrum carries from the segment's position in the padded window:
the per-trial phasors of reading (b) keep it, the frequency shuffle breaks it, and the trial-averaged
cross-spectrum of reading (a) cancels it. One permutation per trial does not help reading (b)
(mean -0.51 in delta-theta, 17% of alpha-beta pairs past 1.96). The first revision adopted reading
(b), for the structure of psianalysis.m; the second verification round found it uncalibrated. Three
outcomes rested on it (fig4c-alpha-beta-shift, fig5a-spatiotemporal-bidirectional,
fig5b-alpha-beta-no-sustained); they keep the outcome that round reviewed, and the change that
reading (a) gives is proposed for a third round.""")
assert src(48).startswith("**Result: not reproduced.** Under neither")
setsrc(48, """**Result: not reproduced.** Under no PSI reading is maintenance parietal-led in any subject. Under
reading (a), adopted, subject means are -0.39 to 0.15 (delta-theta, mean -0.08 +- 0.20) and -0.67
to 0.04 (alpha-beta, -0.24 +- 0.25); under reading (b) -0.67 to 0.05 and -0.48 to -0.05; with one
permutation per trial the lowest subject mean is -1.27; none is below -1.96. The paper reports
-40.03 +- 8.73 and -30.37 +- 2.60. Against psianalysis.m's null, reading (b) puts 4 of 7 subjects
below -1.96 in delta-theta (mean -0.31 +- 10.68) and none in alpha-beta, but that null gives
|z| > 1.96 in 90% and 92% of trial-shuffled pairs, so it does not measure direction. The deposited
code without the conjugate gives every subject below -1.96 with the parietal channel first (means
-55.47 and -69.83) and above +1.96 with the PFC channel first (+58.67 and +69.48); its sign follows
the channel order.""")
assert src(51).startswith("**Result: not reproduced.** No subject has net delta-theta")
setsrc(51, """**Result: not reproduced.** No subject has net delta-theta PSI z above 0 in processing under any
reading (means -0.17 +- 0.16 under reading (a), adopted, and -0.43 +- 0.34 under (b); -0.21 and
-0.76 with one permutation per trial; paper 6.01 +- 6.42 with 6 subjects above 0). Processing
exceeds maintenance in the pair-level model under reading (b) (by 0.27, F(1,2268) = 114.2, p =
4.9e-26; paper F = 1936.10) but not under reading (a) (0.06, F = 2.2, p = 0.14), and on subject
means the difference is absent under both (paired t(6) p = 0.43 and 0.95). The criterion's partial
match needs at least 4 subjects above 0. Against psianalysis.m's null, reading (b) gives 4 subjects
above 0 (mean of those 6.36) and F = 58.5, but that null is not calibrated (trial-shuffled pairs
pass |z| > 1.96 in 90% of cases). On the 900-ms-delay trials alone 2 (a) or 1 (b) subjects are above
0 (means -0.14 and -0.30).""")
assert src(52).startswith("**Result: partially reproduced, resting on an assumption.**")
setsrc(52, """**Result: partially reproduced, resting on PSI reading (b), as verified; a change to not
reproduced is proposed.** Under reading (b), 6 of 7 subjects have processing alpha-beta PSI z below
0 (S3 is above, 0.46) and processing exceeds maintenance in the pair-level model (by 0.43,
F(1,2268) = 97.9, p = 1.2e-22; paper F = 2302.30), the criterion's partial match by the letter.
The outputs above show that this match comes from reading (b)'s null. On the trial-shuffled data,
which have no trial-locked coupling, reading (b) gives subject means of -1.17, -0.40, 0.52, -0.55,
-0.60, -1.25 and 0.03 (S1 to S7), close to the observed -1.07, -0.51, 0.46, -0.61, -0.72, -1.35 and
-0.18 (observed minus surrogate -0.08 +- 0.09, paired t(6) p = 0.061), and on synthetic independent
signals reading (b)'s mean z is -0.25 to -0.29 in alpha-beta. Under reading (a), whose z is
calibrated and which is now adopted, 5 of 7 subjects are below 0 (mean -0.14 +- 0.26; observed
minus surrogate -0.01 +- 0.23, p = 0.93) and processing is higher than maintenance by 0.11 (F = 6.7,
p = 0.0097); one permutation per trial gives the same 5 of 7. That is not reproduced, and the change
is proposed for a third verification round. Subject means are -1.35 to 0.46 under (b) and -0.49 to
0.19 under (a), against the paper's -12.60 +- 7.51; on subject means the interval difference is not
significant under either reading (paired t(6) p = 0.27 and 0.48). On the 900-ms-delay trials alone
4 (a) or 6 (b) subjects are below 0.""")
assert src(54).startswith("**Result: not reproduced.** With the Methods' null")
setsrc(54, """**Result: not reproduced.** With the Methods' null, 78 (reading (a), adopted) or 1 (reading (b))
of 1135 pairs have processing |z| > 1.96 in delta-theta, and 104 or 74 in alpha-beta, against the
paper's 1008 and 984. The trial-shuffled surrogate gives 68 and 78 under (a) and 1 and 71 under
(b), and a null at 5% would give about 57, so the counts are near what signals without trial-locked
coupling give. With one permutation per trial the counts are 98 and 93 (a) and 78 and 211 (b),
against 75 and 71, and 76 and 194, on the surrogate. Against psianalysis.m's null, reading (b) gives
1014 and 1041, within tolerance, but the trial-shuffled surrogate gives 1022 and 1044 under the same
null, so that count does not reflect directionality. The deposited code as written (no conjugate)
marks 1129 to 1135 of the 1135 pairs on the real data.""")
assert src(59).startswith("**Result: not reproduced.** No time point")
setsrc(59, """**Result: not reproduced.** No time point differs between conditions after FDR in delta-theta
under either PSI reading or either spectra reading, in the pair-level model or in the subject-level
test printed under fig5b-alpha-beta-no-sustained, so there is no sustained epoch. Under reading (a),
adopted, the selection holds 78 pairs in 7 subjects; under reading (b) it holds 1 pair (S1), on
which no test can be formed.""")
sub(61, "Under\nthe main spectra, reading (a), the grand means", "Under\nthe main spectra, reading (a) (adopted), the grand means")
assert src(63).startswith("**Result: not reproduced, resting on an assumption.**")
setsrc(63, """**Result: not reproduced, resting on PSI reading (b), as verified; a change to reproduced is
proposed.** Under reading (b) the selection of directional pairs leaves one pair (S1); its
spatial-trial delta-theta PSI z reaches |z| = 3.07 (140 ms) and its temporal-trial z 2.36 (180 ms),
with 16 and 11 of 91 time points at |z| >= 1.96 (paper, all |z| < 1.60). Its identity-trial z also
passes 1.96 at 9 points, so on one pair such excursions are common. Under reading (a), now adopted
because its z is calibrated (see the task-induced PSI section and fig4c-alpha-beta-shift), the
selection holds 78 pairs in 7 subjects and the grand means stay at or below 0.87 (spatial) and 1.01
(temporal), under 1.96 at every time point and under the paper's 1.60. That meets the criterion,
and the change to reproduced is proposed for a third round. The absence shows little: under reading
(a) the identity-trial grand mean also stays below 0.99, where the paper reports |z| above 2.35, so
this measure shows no direction in any condition. With the whole-epoch windows, reading (a) gives
0.37 and 0.56 and reading (b) 2.54 and 3.03.""")
assert src(66).startswith("**Result: reproduced, resting on an assumption.**")
setsrc(66, """**Result: reproduced, resting on PSI reading (b), as verified; a change to partially reproduced
is proposed.** Under reading (b) (74 pairs in 6 subjects), 30 (identity against spatial) and 35
(against temporal) of 91 time points differ after FDR in the pair-level model, and the longest run
of one sign lasts 40 ms, so no difference is sustained under either spectra reading (whole-epoch
windows: 36 and 37 points, longest 50 and 40 ms). Those points come from the pair-level model alone.
The 74 pairs are about as many as the trial-shuffled data select under the same reading (71), S3
supplies 44 of them, and the model treats pairs that share electrodes as independent; the paired
test on the 6 subjects' means finds no point after FDR (smallest p 0.0029 and 0.0078). Under
reading (a), now adopted (see fig4c-alpha-beta-shift; 104 pairs in 7 subjects), no point is
significant after FDR in the pair-level model (smallest p 0.0015 and 0.0027) or in the
subject-level test (0.016 and 0.024), the criterion's partial match; the change to partially
reproduced is proposed for a third round. No reading shows a sustained run.""")
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
PYEOF
python3 $TMPDIR/md2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; cat > $TMPDIR/md3.py <<'PYEOF'
import json
p = "reproduce_johnson_2019.ipynb"
nb = json.load(open(p)); C = nb["cells"]
i = 67
s = "".join(C[i]["source"]); assert s.startswith("## Summary")
reps = [
("| fig4c-alpha-beta-shift | partially reproduced (assumption: PSI reading (b)) |",
 "| fig4c-alpha-beta-shift | partially reproduced (assumption: PSI reading (b)); not reproduced proposed |"),
("| fig5a-spatiotemporal-bidirectional | not reproduced (assumption: PSI reading (b)) |",
 "| fig5a-spatiotemporal-bidirectional | not reproduced (assumption: PSI reading (b)); reproduced proposed |"),
("| fig5b-alpha-beta-no-sustained | reproduced (assumption: PSI reading (b)) |",
 "| fig5b-alpha-beta-no-sustained | reproduced (assumption: PSI reading (b)); partially reproduced proposed |"),
("""(4) PSI from trial-averaged cross-spectra (reading (a), Nolte et al. 2008) or per trial
(reading (b)): for claims where the readings give different outcomes, reading (b) is adopted,
because it is the structure of psianalysis.m and Figure 4A's legend gives values "per subject
across all trials".""",
"""(4) PSI from trial-averaged cross-spectra (reading (a), Nolte et al. 2008) or per trial
(reading (b)), each with one permutation for all trials or one per trial: reading (a) with one
permutation for all trials is now adopted where the readings differ, because its z is calibrated
on trial-shuffled and on synthetic independent data and reading (b)'s is not (its mean is offset
by up to -1.25 per subject on the trial-shuffled data). Three outcomes verified under reading (b)
are kept, and the change reading (a) gives is proposed: fig4c-alpha-beta-shift to not reproduced,
fig5a-spatiotemporal-bidirectional to reproduced (an absence the measure shows in every
condition), and fig5b-alpha-beta-no-sustained to partially reproduced."""),
("""subject-level tests are printed beside them for the task-induced PSI.""",
 """subject-level tests are printed beside them for the task-induced and the time-resolved PSI."""),
("""s that do not pass the shuffle test). The ERP and power tests on the 900-ms-delay trials alone are
shown as variants.""",
"""s that do not pass the shuffle test). The ERP and power tests and the task-induced PSI on the
900-ms-delay trials alone are shown as variants; power on those trials loses most effects, and so
does power on a random draw of as many trials from both delays, so the loss reflects the smaller
number of trials and the test cannot tell whether the timing matters."""),
]
for a, b in reps:
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
C[i]["source"] = s.splitlines(keepends=True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
PYEOF
python3 $TMPDIR/md3.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 - <<'EOF'
p = "README.md"; s = open(p).read()
reps = [
("| Alpha-beta shift, still parietal-led | Partially reproduced (assumption) |",
 "| Alpha-beta shift, still parietal-led | Partially reproduced (assumption); not reproduced proposed |"),
("| Spatial and temporal PSI bidirectional | Not reproduced (assumption) |",
 "| Spatial and temporal PSI bidirectional | Not reproduced (assumption); reproduced proposed |"),
("| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption) |",
 "| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption); partially reproduced proposed |"),
("""The phase slope index is z-scored here against the null the Methods describe (the frequencies of
one signal shuffled and PSI recomputed). With that null, few pairs are directional and none of the
paper's large PSI effects appears. The deposited code omits the conjugate of the cross-spectrum and
z-scores against a null that is not the statistic it tests, which marks about 90% of pairs as
directional even when the trials of the two regions are shuffled.""",
"""The phase slope index is z-scored here against the null the Methods describe (the frequencies of
one signal shuffled and PSI recomputed). With that null, few pairs are directional and none of the
paper's large PSI effects appears. PSI from trial-averaged cross-spectra is adopted where the
readings differ, since its z is calibrated and that of per-trial PSI is not; three outcomes verified
under the per-trial reading are kept, with the change proposed for a further verification round.
The deposited code omits the conjugate of the cross-spectrum, and on the real data marks 99.5 to
100% of pairs as directional. Its null is not the statistic it tests: even with the conjugate added,
that null marks about 90% of pairs as directional when the trials of the two regions are shuffled."""),
("""It takes about 35 minutes, about 20 of them streaming
  the 11.8 GB of tar.gz files, one subject at a time.""",
 """It takes about 43 minutes, about 42 of them streaming
  the 11.8 GB of tar.gz files and analysing each subject in turn."""),
]
for a, b in reps:
    assert s.count(a) == 1, a[:50]; s = s.replace(a, b)
open(p, "w").write(s)
EOF
grep -n "minutes\|runtime\|time" entry.yaml
```

```
10:  time.
15:  runtime_minutes: 35
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; sed -i 's/  runtime_minutes: 35/  runtime_minutes: 45/' entry.yaml; cat entry.yaml; date -u
```

```
schema_version: 1
name: crcns-fcx-3-johnson-2019
type: reproduction
title: Frontoparietal working memory iEEG (Johnson et al. 2019) from CRCNS fcx-3
description: Tests the findings of Johnson, King-Stephens, Weber, Laxer, Lin and Knight (2019) on
  CRCNS data set fcx-3, which holds intracranial recordings from prefrontal and parietal cortex of 7
  patients doing a visuospatial working memory task. It checks the channel and trial counts, the
  behaviour, ERPs and power between identity, spatial and temporal trials with per-subject cluster
  tests, and the phase slope index between prefrontal and parietal channels over the delay and in
  time.
license: Apache-2.0
notebooks:
- path: reproduce_johnson_2019.ipynb
  title: Reproducing Johnson et al. (2019) from CRCNS fcx-3
  runtime_minutes: 45
helpers:
- fcx3.py
related:
- id: crcns:fcx-3/unversioned
  relation: uses_data
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 96,216p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
- claim: erp-no-condition-difference
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:erp-no-condition-difference
  notes: Under the Methods' reading (segments zero padded, 30-Hz low-pass), neighbours adjacent by
    contact number and clusters judged at 0.05 per tail, S2 has a significant cluster for identity
    against temporal (p = 0.041); no other subject-contrast is below 0.05, and 2 of 14 have p <=
    0.10 (paper, all p > 0.10). At 0.025 per tail the adjacent reading finds none, which would be
    reproduced; the distance reading (S5, p = 0.014) and no spatial clustering (S2, p = 0.024) find
    one at either threshold. Variants with adjacent neighbours at 0.05 per tail give, with the 1-30 Hz
    band-pass of the Results, no cluster (smallest p 0.085); per-trial baseline, S5 p = 0.030; the
    whole epoch filtered (erp_compute.m), S2 p = 0.031 (0.053 in round 1 with another random seed);
    900-ms-delay trials only, S5 p = 0.023. The deciding p values lie between 0.02 and 0.05, where
    the Monte Carlo standard error of 1000 shuffles is about 0.006, so the outcome is close to the
    threshold under every reading. The neighbour rule and alpha per tail are put to the paper's
    authors (findings).
  deviations:
  - Assumption. The paper says only that clusters were formed over "neighboring electrodes", and the
    deposited scripts hold no cluster test. The readings give different outcomes, so neighbours
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec1.py <<'PYEOF'
p = "attempts/crcns-fcx-3-johnson-2019-01.yaml"
s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
# ERP
rep("""    900-ms-delay trials only, S5 p = 0.023. The deciding p values lie between 0.02 and 0.05, where
    the Monte Carlo standard error of 1000 shuffles is about 0.006, so the outcome is close to the
    threshold under every reading. The neighbour rule""",
"""    900-ms-delay trials only, S5 p = 0.023. Under the adopted reading the deciding p (0.041) is
    close to 0.05, where the Monte Carlo standard error of 1000 shuffles is about 0.006; the distance
    reading's p = 0.014 is about 6 standard errors below 0.05. The neighbour rule""")
# fig2
rep("""    Five subjects show spatial > identity effects under every reading, and S4 alone identity >
    spatial under every reading but adjacent neighbours at 0.025 per tail (none). The counts match""",
"""    Under the main spectra, five subjects show spatial > identity effects under every neighbour
    reading and threshold, and S4 alone identity > spatial under each of them but adjacent neighbours
    at 0.025 per tail (none). The counts match""")
rep("""    900-ms-delay trials alone 2 or 3 subjects show spatial > identity effects and none identity >
    spatial.
  deviations:""",
"""    900-ms-delay trials alone 2 or 3 subjects show spatial > identity effects and none identity >
    spatial. A random draw of as many trials per condition from both delays gives 1 to 3 and 0 or 1,
    so that loss comes from the smaller number of trials, and these tests cannot show whether the
    1150-ms trials' timing matters.
  deviations:""")
rep("""    clustering (p = 0.044). On the 900-ms-delay trials alone 1 to 3 subjects show temporal >
    identity effects.""",
"""    clustering (p = 0.044). On the 900-ms-delay trials alone 1 to 3 subjects show temporal >
    identity effects and 1 (S1) identity > temporal; a random draw of as many trials from both delays
    gives 2 or 3 and 0 or 1.""")
open(p, "w").write(s)
PYEOF
python3 $TMPDIR/rec1.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/psiblock.yaml <<'EOF'
- claim: fig4-maintenance-parietal-led
  outcome: not_reproduced
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig4-maintenance-parietal-led
  measured:
  - -0.08
  - -0.24
  notes: With the Methods' null, no subject's mean maintenance PSI z is below -1.96 under any
    reading. Reading (a), adopted, gives subject means -0.39 to 0.15 (delta-theta, mean -0.08 +- 0.20,
    recorded) and -0.67 to 0.04 (alpha-beta, -0.24 +- 0.25); reading (b) -0.67 to 0.05 and -0.48 to
    -0.05; with one permutation per trial the lowest subject mean is -1.27. The paper reports -40.03
    +- 8.73 and -30.37 +- 2.60. Against psianalysis.m's null, reading (b) gives 4 of 7 subjects below
    -1.96 in delta-theta and none in alpha-beta, but that null gives |z| > 1.96 in 90 to 92% of
    trial-shuffled pairs. The deposited code without the conjugate gives every subject below -1.96
    with the parietal channel first (means -55.47 and -69.83) and above +1.96 with the PFC channel
    first (+58.67 and +69.48); it is not a reading of the paper.
  deviations:
  - P1 details taken from psi_compute.m and subtracterp.m, ERP removed as the mean over all correct
    trials ("raw trial-wise mean", reading (a)); one Hanning-tapered FFT of each 900-ms segment
    padded to 7.5 s, read at the nearest bins to the integer frequencies ('mtmfft', spectra reading
    (a)); one PSI per band summed over adjacent bins.
  - The null follows the Methods (Task-Induced PSI, paragraph 2), "we randomly shuffled the
    frequencies in one signal and re-computed PSI 1,000 times". Each shuffle permutes the parietal
    spectrum's bins and recomputes the statistic that is z-scored, with the same permutation for
    every trial (null reading (a)) or one per trial (null reading (b)), both run. psianalysis.m
    z-scores the mean of per-trial PSI against the slope of the trial-mean spectrum with both factors
    shuffled, a different statistic; where the Methods and the code differ the Methods come first,
    and the code's null is a variant.
  - Assumption, for the PSI claims whose outcome depends on it (fig4c-alpha-beta-shift,
    fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained). P1 leaves open whether PSI
    comes from trial-averaged cross-spectra (a) or per trial (b). Reading (a) with null reading (a) is
    adopted, since it is the first P1 lists, the measure of Nolte et al. (2008), and the only one
    whose z is calibrated. On trial-shuffled data its z has mean -0.05 and 0.02, SD 1.01 and 1.04,
    and |z| > 1.96 in 6.0% and 6.9% of pairs; reading (b) has mean -0.29 and SD 0.60 in delta-theta
    (0.1% pass), subject means from -1.25 to 0.52 in alpha-beta, and on synthetic independent
    signals a mean of -0.21 to -0.37, which one permutation per trial does not remove. The first
    revision adopted reading (b), for the structure of psianalysis.m and the Figure 4A legend's
    values "per subject across all trials"; round 2 of the verification found it uncalibrated. Here
    both readings give the same outcome.
- claim: fig4a-delta-theta-shift
  outcome: not_reproduced
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig4a-delta-theta-shift
  measured:
  - 0
  - -0.17
  - 2.2
  notes: No subject has net processing delta-theta PSI z above 0 under any reading (means -0.17 +-
    0.16 under (a), adopted and recorded, -0.43 +- 0.34 under (b), and -0.21 and -0.76 with one
    permutation per trial; paper 6 subjects, 6.01 +- 6.42). Processing exceeds maintenance in the
    pair-level model under reading (b) (by 0.27, F(1,2268) = 114.2, p = 4.9e-26; paper F = 1936.10)
    but not under (a) (0.06, F = 2.2, p = 0.14); on subject means neither differs (paired t(6) p =
    0.95 and 0.43). The partial match needs at least 4 subjects above 0. Against psianalysis.m's
    null, reading (b) gives 4 subjects above 0 and F = 58.5, but that null is not calibrated (90% of
    trial-shuffled pairs pass |z| > 1.96). On the 900-ms-delay trials alone 2 (a) or 1 (b) subjects
    are above 0.
  deviations:
  - As fig4-maintenance-parietal-led. The mixed model is computed as the paired test over pairs,
    which equals it when each pair has both intervals (checked against statsmodels MixedLM, F 2.2
    against 2.2 under reading (a) and 116.4 against 114.2 under reading (b)). Degrees of freedom 2268
    follow from 1135 pairs; as in the paper's degrees of freedom, pairs that share electrodes are
    treated as independent, which inflates F, so a paired t-test on subject means is printed beside
    it.
- claim: fig4c-alpha-beta-shift
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig4c-alpha-beta-shift
  measured:
  - -0.57
  - 97.9
  notes: The outcome is the one round 2 reviewed, under PSI reading (b), and a change to not
    reproduced is proposed. Under reading (b), 6 of 7 subjects have processing alpha-beta PSI z below
    0 (S3 is above, 0.46) and processing exceeds maintenance in the pair-level model (by 0.43,
    F(1,2268) = 97.9, p = 1.2e-22; paper F = 2302.30), the criterion's partial match by the letter.
    Subject means lie between -1.35 and 0.46 (mean -0.57 +- 0.59, recorded; paper -12.60 +- 7.51). On
    the trial-shuffled data reading (b) gives nearly the same subject means (observed minus surrogate
    -0.08 +- 0.09, p = 0.061). Under reading (a), now adopted, 5 of 7 subjects are below 0 (mean -0.14
    +- 0.26), with processing higher by 0.11 (F = 6.7, p = 0.0097). On subject means the interval
    difference is not significant under either reading (paired t(6) p = 0.27 under (b), 0.48 under
    (a)).
  deviations:
  - As fig4a-delta-theta-shift. The outcome rests on PSI reading (b), the reading round 2 reviewed;
    reading (a) is now adopted (see fig4-maintenance-parietal-led).
  proposed:
    outcome: not_reproduced
    reason: Under PSI reading (a), now adopted because its z is calibrated, 5 of 7 subjects have
      processing alpha-beta PSI z below 0 (mean -0.14 +- 0.26), fewer than the 6 the partial match
      needs; one permutation per trial also gives 5. The 6 of 7 under reading (b) come from that
      reading's null. On the trial-shuffled data, which have no trial-locked coupling, reading (b)'s
      subject means are -1.17, -0.40, 0.52, -0.55, -0.60, -1.25 and 0.03, against the observed -1.07,
      -0.51, 0.46, -0.61, -0.72, -1.35 and -0.18 (observed minus surrogate -0.08 +- 0.09, paired t(6)
      p = 0.061), and on synthetic independent signals reading (b)'s mean z is -0.25 to -0.29 in
      alpha-beta. Under reading (a) observed minus surrogate is -0.01 +- 0.23 (p = 0.93). The
      analysis is in the notebook's task-induced PSI section (calibration, synthetic and fig4c
      outputs).
- claim: directional-pairs
  outcome: not_reproduced
  notebook: reproduce_johnson_2019.ipynb
  output: claim:directional-pairs
  measured:
  - 78
  - 104
  notes: With the Methods' null, 78 (reading (a), adopted and recorded) or 1 (reading (b)) of 1135
    pairs have processing |z| > 1.96 in delta-theta, and 104 or 74 in alpha-beta, against 1008 and
    984. The trial-shuffled surrogate gives 68 and 78 under (a) and 1 and 71 under (b), and a null at
    5% gives about 57, so the counts are near what signals without trial-locked coupling give. With
    one permutation per trial the counts are 98 and 93 (a) and 78 and 211 (b), against 75 and 71, and
    76 and 194, on the surrogate. Against psianalysis.m's null, reading (b) gives 1014 and 1041,
    within tolerance (round 1's result), but the trial-shuffled surrogate gives 1022 and 1044 under
    the same null, so that count does not reflect directionality. The deposited code as written
    marks 1129 to 1135 of the 1135 pairs.
  deviations:
  - As fig4-maintenance-parietal-led; 1135 pairs, not 1129 (table1-electrodes).
- claim: fig5a-delta-theta-epochs
  outcome: not_reproduced
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5a-delta-theta-epochs
  notes: No delta-theta time point differs between conditions after FDR under either PSI reading,
    with the segment zero padded or with the whole-epoch windows of psi_compute.m, in the pair-level
    model or in a paired test on subject means, so there is no sustained epoch. Reading (a), adopted,
    selects 78 directional pairs in 7 subjects; reading (b) selects 1 pair (S1).
  deviations:
  - Time-resolved PSI per psi_compute.m ('mtmconvol', per-condition ERP removed by subtracterp.m with
    three conditions), on the 900-ms segment zero padded (Methods, Time-Resolved PSI, "Spectral
    decomposition, PSI computation, and per-subject statistical bootstrapping analysis were
    otherwise identical"); psi_compute.m's windows over the whole epoch are a variant. The null is
    the Methods' frequency shuffle of one signal, recomputed per time point. subtracterp.m selects
    temporal trials by trialinfo column 5 (the delay), which selects none; the condition column is
    used.
  - The per-time-point mixed model is computed as the paired test over pairs (checked against
    statsmodels at three time points); FDR is Benjamini-Hochberg over the 91 points; a run is
    sustained when it spans at least 100 ms (P2), and runs over 100 ms are printed for the Figure 5
    legend's ">100 ms" (asked of a reader). A paired t-test on subject means at each time point is
    printed beside it, since the model treats pairs that share electrodes as independent.
- claim: fig5a-identity-direction
  outcome: not_reproduced
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5a-identity-direction
  measured:
  - 0.73
  - 0.6
  - 0.22
  - -0.13
  notes: In the paper's four epochs no reading meets the criterion. Under reading (a), adopted (78
    pairs), with the segment zero padded, the identity-trial grand means are 0.73, 0.60, 0.22 and
    -0.13 (recorded; paper > 2.62, > 2.35, < -3.04, < -3.57). Under reading (b) (S1's one pair) they
    are 1.31, 0.93, -1.98 and 0.13; the third passes -1.96 with the right sign (-2.20 as identity
    minus spatial) but is outside the bound (-3.04, within 10%). Every value of the other readings
    (averaging, measure, PSI and spectra) is below 1.96 in absolute value.
  deviations:
  - As fig5a-delta-theta-epochs; the paper's epochs are used.
- claim: fig5a-spatiotemporal-bidirectional
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5a-spatiotemporal-bidirectional
  notes: The outcome is the one round 2 reviewed, under PSI reading (b), and a change to reproduced
    is proposed. Under reading (b) the selection leaves one directional pair (S1); its spatial-trial
    delta-theta PSI z reaches |z| = 3.07 (140 ms) and its temporal-trial z 2.36 (180 ms), with 16 and
    11 of 91 time points at |z| >= 1.96 (paper, all |z| < 1.60). Its identity-trial z also passes 1.96
    at 9 points, so on one pair such excursions are common. Under reading (a), now adopted (78 pairs
    in 7 subjects), the grand means stay at or below 0.87 and 1.01, and the identity-trial grand mean
    also stays below 0.99, where the paper reports |z| above 2.35. With the whole-epoch windows,
    reading (b) gives 2.54 and 3.03 and reading (a) 0.37 and 0.56.
  deviations:
  - The outcome rests on PSI reading (b), the reading round 2 reviewed; reading (a) is now adopted
    (see fig4-maintenance-parietal-led). As fig5a-delta-theta-epochs otherwise.
  proposed:
    outcome: reproduced
    reason: Under PSI reading (a), now adopted because its z is calibrated (see fig4c-alpha-beta-shift
      and fig4-maintenance-parietal-led), the selection holds 78 pairs in 7 subjects, and the
      spatial-trial and temporal-trial grand means stay at or below 0.87 and 1.01, under 1.96 at every
      time point and under the paper's 1.60, which the criterion counts as reproduced. The absence
      shows little, since under this reading the identity-trial grand mean also stays below 0.99,
      where the paper reports |z| above 2.35. The reading (b) result rests on one pair whose
      identity-trial z also passes 1.96 at 9 points.
- claim: fig5b-alpha-beta-no-sustained
  outcome: reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5b-alpha-beta-no-sustained
  notes: The outcome is the one round 2 reviewed, under PSI reading (b), and a change to partially
    reproduced is proposed. Under reading (b) (74 pairs in 6 subjects), 30 (identity against
    spatial) and 35 (against temporal) of 91 time points differ after FDR in the pair-level model,
    and the longest run of one sign lasts 40 ms, so no difference is sustained (whole-epoch windows,
    36 and 37 points, longest 50 and 40 ms). The trial-shuffled data select 71 pairs under the same
    reading, S3 supplies 44 of the 74, and a paired test on the 6 subjects' means finds no point
    after FDR (smallest p 0.0029 and 0.0078). Under reading (a), now adopted (104 pairs in 7
    subjects), no point is significant after FDR in the pair-level model (smallest p 0.0015 and
    0.0027) or at subject level.
  deviations:
  - The outcome rests on PSI reading (b), the reading round 2 reviewed; reading (a) is now adopted
    (see fig4-maintenance-parietal-led). As fig5a-delta-theta-epochs otherwise.
  proposed:
    outcome: partially_reproduced
    reason: Under PSI reading (a), now adopted because its z is calibrated (see fig4c-alpha-beta-shift
      and fig4-maintenance-parietal-led), no time point differs between conditions after FDR (smallest
      p 0.0015 against spatial, 0.0027 against temporal, 104 pairs in 7 subjects), which the criterion
      counts as partially reproduced. The significant points of reading (b) come from the pair-level
      model on 74 pairs, about as many as trial-shuffled data select (71), 44 of them from S3; a
      paired test on the 6 subjects' means finds none after FDR.
EOF
python3 - <<'EOF'
p = "attempts/crcns-fcx-3-johnson-2019-01.yaml"
s = open(p).read()
a = s.index("- claim: fig4-maintenance-parietal-led")
b = s.index("findings:\n")
new = open("/tmp/claude-1001/psiblock.yaml").read()
s = s[:a] + new + s[b:]
open(p, "w").write(s)
EOF
grep -n "claim: fig4-main\|^findings" attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
221:- claim: fig4-maintenance-parietal-led
423:findings:
582:  - claim: fig4-maintenance-parietal-led
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec2.py <<'PYEOF'
p = "attempts/crcns-fcx-3-johnson-2019-01.yaml"
s = open(p).read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b)
rep("""    The ERP and power tests on the 900-ms-delay trials alone are shown as variants.""",
"""    The ERP and power tests and the task-induced PSI on the 900-ms-delay trials alone are shown as
    variants. Power on those trials loses most effects, and so does power on a random draw of as
    many trials from both delays, so these tests cannot tell whether the timing affects the results.""")
rep("""    about the same counts on trial-shuffled data. This attempt used the Methods' null and adopted the
    per-trial reading, with the conjugate, where the readings give different outcomes.""",
"""    about the same counts on trial-shuffled data. This attempt used the Methods' null and adopted the
    trial-averaged reading, whose z is calibrated on trial-shuffled data, where the readings give
    different outcomes; per-trial PSI with the Methods' null gives z offset from zero on data
    without coupling.""")
open(p, "w").write(s)
PYEOF
python3 $TMPDIR/rec2.py && echo ok; sed -n 423,440p attempts/crcns-fcx-3-johnson-2019-01.yaml | head -3
```

```
ok
findings:
- kind: metadata_error
  statement: The data set's list of analysed channels (docs/summary_channel_analysis.csv) holds 187
```

**Agent calls Bash**

```bash
cd  git log -3 --format='%h %ad %s' --date=iso
```

```
9d9442c556 2026-11-09 00:59:15 +0000 Agent run on crcns-fcx-3: verifier-2 (success)
9e50d4b6e6 2026-11-08 23:58:43 +0000 Agent run on crcns-fcx-3: author-revise-1 (success)
ee0cfbb64c 2026-11-08 22:21:47 +0000 Agent run on crcns-fcx-3: verifier-1 (success)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/crcns-fcx-3-johnson-2019-01.yaml <<'EOF'
- date: '2026-11-09'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook of the first revision (commit 9e50d4b6e6), the helper
    module, the claims file and this record, with the paper. It agreed with 16 of the 17 outcomes and
    disagreed with fig4c-alpha-beta-shift; of its round-1 points it found 7 resolved and 3 (the PSI
    null, pairs treated as independent, the timing of the 1150-ms trials) partly resolved and bearing
    on a conclusion. It quoted six passages the outputs do not support.
  results:
  - claim: table1-electrodes
    agrees: true
    outcome: partially_reproduced
    reason: 187 channels and 1135 pairs (cell 17).
    response: No change needed. The data-check text that said the docs' channel list names 192
      channels now says 187, with Table 1's 192 beside it.
  - claim: trial-counts
    agrees: true
    outcome: reproduced
    reason: Cell 20.
    response: No change needed.
  - claim: fig1b-accuracy
    agrees: true
    outcome: reproduced
    reason: Range 0.625 to 0.975; p = 0.283 (cell 23).
    response: No change needed.
  - claim: fig1b-rt-identity-slower
    agrees: true
    outcome: reproduced
    reason: p = 0.024, 0.005, 0.010 and 0.254 (cell 26).
    response: No change needed.
  - claim: erp-no-condition-difference
    agrees: true
    outcome: not_reproduced
    reason: The assumption is stated and reasonable. The outcome hardly depends on it; in the main
      configuration, 5 of the 6 neighbour and alpha-per-tail combinations give a cluster with p below
      0.05 (or 0.025 where that is the threshold). Only adjacent neighbours at 0.025 per tail give
      none (cell 29). The sentence "The deciding p values lie between 0.02 and 0.05, so the outcome is
      close to the threshold under every reading" is not supported; the distance reading gives p =
      0.014, about 6 Monte Carlo SE below 0.05, and only the adopted adjacent reading (0.041) is close
      to the threshold.
    response: Outcome kept. The notebook and the notes now say that the adopted reading's p (0.041)
      is close to 0.05 and the distance reading's 0.014 is not.
  - claim: fig2-spatial-power
    agrees: true
    outcome: partially_reproduced
    reason: 5 and 1 subjects, within one of the paper's counts. The percentages are off, 37.7 and 11.8
      (cell 32). The notes' "Five subjects show spatial > identity effects under every reading" and
      "S4 alone identity > spatial under every reading" hold for the main spectra only; the 900-ms
      variant gives 2 or 3 subjects and the whole-epoch windows add S7. The 900-ms-only variant
      removes most power effects, and that loss cannot yet be separated from the halving of trials; a
      control on a random half of all trials would separate the two.
    response: Outcome kept. The notes now limit those sentences to the main spectra. The power test
      is now also run on a random draw of trials from both delays with as many trials per condition
      as the 900-ms trials (methods_half); it loses about as many effects (1 to 3 subjects spatial >
      identity, 0 or 1 identity > spatial), so the loss on the 900-ms trials comes from fewer trials,
      and the notes and the timing finding say these tests cannot tell whether the timing matters.
      The cue-locked 70-150 Hz traces per delay group are now plotted.
  - claim: fig3-temporal-power
    agrees: true
    outcome: partially_reproduced
    reason: 5 and 2 subjects (4 and 2 with assignment b); no reading gets the percentages within
      tolerance (cell 32).
    response: Outcome kept. The random-trial control is reported here as for fig2-spatial-power (2 or
      3 and 0 or 1 subjects, against 1 to 3 and 1 on the 900-ms trials).
  - claim: power-difficulty-subjects
    agrees: true
    outcome: reproduced
    reason: Holds under reading (b)(i) in every configuration. S3 breaks the converse (cell 37).
    response: No change needed; the fig2-spatial-power conclusion says the random-trial control bears
      on this claim too.
  - claim: power-low-frequencies
    agrees: true
    outcome: reproduced
    reason: Yes, by the letter. The assumption is stated and defensible, but weak; a "maximum" at the
      2-Hz end of the range only means the density keeps rising below 2 Hz. Without counting that
      edge, the identity > other effect fails in every combination (cell 40).
    response: Outcome kept, resting on the stated assumption, with the result without the edge
      printed and given in the notes, as before.
  - claim: fig4-maintenance-parietal-led
    agrees: true
    outcome: not_reproduced
    reason: No subject is below -1.96 under either reading (cell 45).
    response: Outcome kept. Reading (a) is now the adopted PSI reading and its values are recorded;
      the readings with one permutation per trial (P1 null reading (b)) are added, and none is below
      -1.96.
  - claim: fig4a-delta-theta-shift
    agrees: true
    outcome: not_reproduced
    reason: 0 of 7 subjects above zero under both readings (cell 48).
    response: Outcome kept, with reading (a)'s values recorded; the per-trial null and the 900-ms
      trials are added (2 or fewer subjects above zero).
  - claim: fig4c-alpha-beta-shift
    agrees: false
    reason: The evidence does not support it. The partial match rests on the sign of subject means
      that are all close to zero, -1.35 to 0.46 (cell 48). Under reading (b) with the Methods' null,
      z is not centred on zero for independent signals; in a synthetic test (33 trials of independent
      1/f and brown noise) reading (b) gave mean z of -0.32 to -0.34 in both bands, with SD 0.75 to
      0.82 in delta-theta, and reading (a) a mean near 0 in delta-theta and -0.13 to -0.17 in
      alpha-beta, with SD about 1. An offset of that size alone would put most subjects below zero,
      and the data show the same pattern under (b). The record justifies reading (b) by its structure,
      not by calibration; the surrogate shows (b) is too conservative in delta-theta (SD 0.60, 0.1%
      pass rate) and in alpha-beta its per-subject rates run from 0% to 24%. If reading (a) were
      adopted, fig4c would be not reproduced, fig5b partial, and fig5a-spatiotemporal reproduced by
      the letter but uninformative. It asked for the surrogate's mean z per subject under (a) and
      (b), and possibly (b) with one permutation per trial.
    response: Outcome kept as round 2 does not allow a change, and not_reproduced proposed for a third
      round. The notebook now prints the surrogate's mean z per subject, runs both readings with one
      permutation per trial, and repeats the synthetic test. Under reading (b) the surrogate's subject
      means (-1.25 to 0.52) nearly equal the observed ones (observed minus surrogate -0.08 +- 0.09, p =
      0.061), and one permutation per trial does not calibrate it (mean -0.51 in delta-theta, 17% of
      alpha-beta pairs past 1.96). Moving the FFT's time origin to the segment's centre removes the
      offset in the synthetic test, which points to the phase slope from the segment's position in the
      padded window. Reading (a), calibrated (mean -0.05 and 0.02, SD near 1, 6.0% and 6.9% pass), is
      now adopted where the readings differ; under it 5 of 7 subjects are below zero.
  - claim: directional-pairs
    agrees: true
    outcome: not_reproduced
    reason: 1 or 78 delta-theta pairs and 74 or 104 alpha-beta pairs, all near the trial-shuffled
      surrogate (cell 51). The README's statement that the deposited code z-scores against a null
      that marks about 90% of pairs as directional on shuffled trials describes psianalysis.m's null
      with the conjugate added; the code as deposited was never run on the surrogate, and on the real
      data it marks 99.5 to 100% of pairs.
    response: Outcome kept, with reading (a)'s counts (78 and 104) recorded and the per-trial nulls
      added. The README now says the deposited code marks 99.5 to 100% of pairs on the real data, and
      that the 90% on shuffled trials is that null with the conjugate added.
  - claim: fig5a-delta-theta-epochs
    agrees: true
    outcome: not_reproduced
    reason: No FDR-significant points (cells 54 and 56).
    response: No change needed; a subject-level test is now printed beside the pair-level model and
      also finds no point.
  - claim: fig5a-identity-direction
    agrees: true
    outcome: not_reproduced
    reason: Cell 58.
    response: Outcome kept, with reading (a)'s values recorded.
  - claim: fig5a-spatiotemporal-bidirectional
    agrees: true
    outcome: not_reproduced
    reason: Yes, by the letter, but the evidence is one pair in S1 (cell 60). The assumption is
      stated, but its reasoning does not address calibration (see fig4c-alpha-beta-shift).
    response: Outcome kept as round 2 does not allow a change, and reproduced proposed for a third
      round, since reading (a), now adopted for its calibration, keeps every grand mean below 1.96
      (largest 0.87 and 1.01). The notes say the absence shows little, as the identity-trial grand mean
      also stays below 0.99.
  - claim: fig5b-alpha-beta-no-sustained
    agrees: true
    outcome: reproduced
    reason: Yes, by the letter. The significant points come only from reading (b)'s pair-level test (30
      and 35 points, smallest p 2e-18). The 74 pairs it selects are about the number the
      trial-shuffled data select (71), and S3 supplies 44 of them, all treated as independent. No
      subject-level test is shown. Under reading (a) the outcome is partial.
    response: Outcome kept as round 2 does not allow a change, and partially_reproduced proposed for
      a third round under reading (a), now adopted, which finds no FDR-significant point. A paired test
      on subject means at each time point is now printed; under reading (b) it finds no point after
      FDR either (smallest p 0.0029 and 0.0078). The README and the notebook's opening no longer say
      the run takes 35 minutes; the loading cell takes about 42 of 43.
EOF
cd  && python tools/entry.py check entries/crcns-fcx-3-johnson-2019 2>&1 | tail -10
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p = "attempts/crcns-fcx-3-johnson-2019-01.yaml"
s = open(p).read()
a = """      FDR either (smallest p 0.0029 and 0.0078). The README and the notebook's opening no longer say
      the run takes 35 minutes; the loading cell takes about 42 of 43."""
b = """      FDR either (smallest p 0.0029 and 0.0078)."""
assert s.count(a) == 1; s = s.replace(a, b)
a = """    response: No change needed. The data-check text that said the docs' channel list names 192
      channels now says 187, with Table 1's 192 beside it."""
b = """    response: No change needed. The data-check text that said the docs' channel list names 192
      channels now says 187, with Table 1's 192 beside it. The README and the notebook's opening,
      which the report also quoted, no longer say the run takes 35 minutes with 20 of them streaming;
      the loading cell takes about 42 of the run's 43 minutes."""
assert s.count(a) == 1; s = s.replace(a, b)
open(p, "w").write(s)
EOF
grep -n "pilot\|protocol:" attempts/crcns-fcx-3-johnson-2019-01.yaml | head; grep -n "^version\|pilot" docs/protocol.md | head -3
```

```
18:    protocol: pilot-13
3:Version: `pilot-13`. Record this version in the attempt's provenance.
8:[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9:([pilot notes](pilot-notes.md)); the reasons for the rules are there.
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 - <<'EOF'
p = "fcx3.py"; s = open(p).read()
a = """  recomputes the same statistic (Methods), 1000 shuffles, one shuffle for all pairs and trials;
  see `psi_z`."""
b = """  recomputes the same statistic (Methods), 1000 shuffles, one shuffle for all pairs and trials, or
  one per trial (P1 null reading (b), task-induced PSI only); see `psi_z`."""
assert s.count(a) == 1; s = s.replace(a, b); open(p, "w").write(s)
EOF
date -u
```

```
Mon Nov  9 02:26:28 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-3-johnson-2019; python3 -c "
import json,re;nb=json.load(open('reproduce_johnson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  for m in re.finditer(r'[^.]*(adopt|1042|1045|6\.22|59\.5|10\.69|35 min|192)[^.]*\.', s):
    print(i, c['cell_type'], m.group(0).strip()[:250])
"
```

```
5 markdown The derived epochs carry every channel kept after preprocessing (29 to 155 per subject), of which the
docs' channel list names 187 analysed channels in all (Table 1 gives 192; see table1-electrodes); only those are kept here.
17 markdown ## table1-electrodes

> The analysed data comprise 192 bipolar virtual electrodes in seven subjects, 4 to 54 (mean 19) in
> PFC and 2 to 16 (mean 8) in parietal cortex per subject, as listed per subject in Table 1, forming
> 1129 same-hemisphere PFC-
18 code sum())
print(f"\nanalysed channels {n_el} (paper 192); PFC per subject {t1.
18 code 1%});"
      f" channels {(n_el - 192) / 192:+.
19 markdown ** The data set's channel list holds 187 analysed channels, not
192: S4 has 5 right parietal channels where Table 1 gives 10; every other subject's counts and
hemispheres equal Table 1.
31 markdown Under the adopted reading the deciding p (0.
43 markdown **Which reading is adopted.
43 markdown ** Where the readings give different outcomes, reading (a) with null
reading (a) is adopted: it is the first P1 lists, the measure of Nolte et al.
43 markdown The first revision adopted reading
(b), for the structure of psianalysis.
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "1042\|1045\|6\.22\|59\.5\|per-trial reading\|reading (b) is adopted\|35 min" attempts/crcns-fcx-3-johnson-2019-01.yaml entries/crcns-fcx-3-johnson-2019/README.md | grep -v "^.*round 1\|reason:" | head
```

```
attempts/crcns-fcx-3-johnson-2019-01.yaml:492:    reports 1008 and 984, which only the code's null reproduces (1014 and 1042), and that null gives
attempts/crcns-fcx-3-johnson-2019-01.yaml:625:      psianalysis.m's null still gives 1014 and 1042, and 1022 and 1045 on the trial-shuffled data,
attempts/crcns-fcx-3-johnson-2019-01.yaml:681:      which the report also quoted, no longer say the run takes 35 minutes with 20 of them streaming;
entries/crcns-fcx-3-johnson-2019/README.md:35:under the per-trial reading are kept, with the change proposed for a further verification round.
```

**Agent calls Bash**

```bash
cd  sed -i '492s/(1014 and 1042)/(1014 and 1041)/' attempts/crcns-fcx-3-johnson-2019-01.yaml; sed -n 485,497p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
statement: Question for the paper's authors. Was task-induced and time-resolved PSI computed from
    cross-spectra averaged over trials (Nolte et al. 2008) or per trial and averaged, as
    psianalysis.m does, and with which channel first, given that the deposited code omits the
    conjugate? And was the null the frequency shuffle of one signal with PSI recomputed, as the
    Methods say, or the slope of the trial-mean spectrum, as psianalysis.m computes it? With the
    Methods' null, 1 (per trial) or 78 (trial-averaged) of 1135 pairs are directional in
    delta-theta, and 74 or 104 in alpha-beta, near the counts of trial-shuffled data; the paper
    reports 1008 and 984, which only the code's null reproduces (1014 and 1041), and that null gives
    about the same counts on trial-shuffled data. This attempt used the Methods' null and adopted the
    trial-averaged reading, whose z is calibrated on trial-shuffled data, where the readings give
    different outcomes; per-trial PSI with the Methods' null gives z offset from zero on data
    without coupling.
verifications:
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/crcns-fcx-3-johnson-2019 2>&1 | tail -4; date -u
```

```
Mon Nov  9 02:26:43 UTC 2026
Installed kernelspec registry-crcns-fcx-3-johnson-2019 in executed/crcns-fcx-3-johnson-2019/.venv/share/jupyter/kernels/registry-crcns-fcx-3-johnson-2019
0 error(s)
pass  reproduce_johnson_2019.ipynb  (2448 s)
Mon Nov  9 03:07:39 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/out2.txt
import json
nb = json.load(open("executed/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    print("=====", i)
    for o in c.get("outputs", []):
        print("".join(o.get("text", "")) or "".join(o.get("data", {}).get("text/plain", "")))
EOF
diff <(grep -v "streamed and analysed\|all subjects in" $TMPDIR/out.txt) <(grep -v "streamed and analysed\|all subjects in" $TMPDIR/out2.txt) | head; grep "all subjects" $TMPDIR/out2.txt; git status --short
```

```
301a302
> 
903d903
< 
904a905
> 
all subjects in 40.0 min
 M attempts/crcns-fcx-3-johnson-2019-01.yaml
 M entries/crcns-fcx-3-johnson-2019/README.md
 M entries/crcns-fcx-3-johnson-2019/entry.yaml
 M entries/crcns-fcx-3-johnson-2019/fcx3.py
 M entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
p = "entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb"
nb = json.load(open(p)); c = nb["cells"][0]; s = "".join(c["source"])
a = "The\nloading cell, which streams and analyses each subject in turn, takes about 42 of the run's 43 minutes."
b = "The\nloading cell, which streams and analyses each subject in turn, takes nearly the whole run, 40 to 42\nminutes of 41 to 43 in two runs."
assert a in s; c["source"] = s.replace(a, b).splitlines(keepends=True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
for p, a, b in [("entries/crcns-fcx-3-johnson-2019/README.md", "It takes about 43 minutes, about 42 of them streaming", "It takes 41 to 43 minutes, 40 to 42 of them streaming"),
                ("attempts/crcns-fcx-3-johnson-2019-01.yaml", "the loading cell takes about 42 of the run's 43 minutes.", "the loading cell takes 40 to 42 of the run's 41 to 43 minutes.")]:
    s = open(p).read(); assert s.count(a) == 1, a; open(p, "w").write(s.replace(a, b))
EOF
git diff entries/crcns-fcx-3-johnson-2019/README.md | head -60; python tools/entry.py check entries/crcns-fcx-3-johnson-2019 2>&1 | tail -2
```

```
diff --git a/entries/crcns-fcx-3-johnson-2019/README.md b/entries/crcns-fcx-3-johnson-2019/README.md
index 579b2e5750..a180c989ba 100644
--- a/entries/crcns-fcx-3-johnson-2019/README.md
+++ b/entries/crcns-fcx-3-johnson-2019/README.md
@@ -18,26 +18,29 @@ preprocessed epochs and the paper's MATLAB scripts.
 | Power effects at 2-7 and 9-24 Hz | Reproduced (assumption) |
 | Parietal-led maintenance (Figure 4) | Not reproduced |
 | Delta-theta shift with the test cue | Not reproduced |
-| Alpha-beta shift, still parietal-led | Partially reproduced (assumption) |
+| Alpha-beta shift, still parietal-led | Partially reproduced (assumption); not reproduced proposed |
 | 1008 and 984 directional pairs | Not reproduced |
 | Time-resolved delta-theta epochs (Figure 5A) | Not reproduced |
 | Identity PFC-led early, parietal-led late | Not reproduced |
-| Spatial and temporal PSI bidirectional | Not reproduced (assumption) |
-| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption) |
+| Spatial and temporal PSI bidirectional | Not reproduced (assumption); reproduced proposed |
+| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption); partially reproduced proposed |
 
 A failure to reproduce here may be a failure of this attempt, not of the paper: see the
 reasoning and the differences from the paper's method.
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p = "entries/crcns-fcx-3-johnson-2019/README.md"; s = open(p).read()
a = """The deposited code omits the conjugate of the cross-spectrum, and on the real data marks 99.5 to
100% of pairs as directional. Its null is not the statistic it tests: even with the conjugate added,
that null marks about 90% of pairs as directional when the trials of the two regions are shuffled. The data set lists
187 analysed channels"""
b = """The deposited code omits the conjugate of the cross-spectrum, and on the real data marks 99.5 to
100% of pairs as directional. Its null is not the statistic it tests: even with the conjugate added,
that null marks about 90% of pairs as directional when the trials of the two regions are shuffled.
The data set lists 187 analysed channels"""
assert a in s; open(p, "w").write(s.replace(a, b))
EOF
sed -n 221,700p attempts/crcns-fcx-3-johnson-2019-01.yaml | grep -nE "^\s{4,}.*[^ ]: " | grep -v "^\s*[0-9]*:\s*- \|reason: \|response: \|outcome: \|statement: \|notes: " | head
```

```
287:    agrees: true
294:    agrees: true
300:    agrees: true
307:    agrees: true
314:    agrees: true
330:    agrees: true
341:    agrees: true
349:    agrees: true
357:    agrees: true
367:    agrees: true
```

**Agent calls Bash**

```bash
cd  sed -n 221,720p attempts/crcns-fcx-3-johnson-2019-01.yaml | grep -nE "^\s{4,}[^-a-z].*: |^\s{6,}[a-z].*[a-z]: [a-zA-Z]" | grep -vE "^\s*[0-9]+:\s+(agrees|claim|outcome|reason|response|kind|by|date|reviewed|results|statement|notes|measured|deviations|proposed|blocked_by):" | head; grep -c "—\|rather" attempts/crcns-fcx-3-johnson-2019-01.yaml entries/crcns-fcx-3-johnson-2019/README.md entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb
```

```
attempts/crcns-fcx-3-johnson-2019-01.yaml:0
entries/crcns-fcx-3-johnson-2019/README.md:0
entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb:0
```

**Agent**

I've finished the round-2 revision. No verified outcome changed; three changes of outcome are proposed for a third round. `python tools/entry.py all` reported 0 errors and the notebook passed (2448 s). A second full run after the last code change gave the same outputs as the first, and `entry.py check` still reports 0 errors after the final text edits.

**Proposed changes (verified outcomes kept, as round 2 requires)**

| Claim | Current outcome | Proposed |
|---|---|---|
| fig4c-alpha-beta-shift | partially reproduced | not reproduced |
| fig5a-spatiotemporal-bidirectional | not reproduced | reproduced |
| fig5b-alpha-beta-no-sustained | reproduced | partially reproduced |

All three rested on PSI reading (b), which the verifier called weak. The new outputs confirm it is miscalibrated:
- **Offset on shuffled data.** When each PFC trial is paired with another trial's parietal data, reading (b)'s per-subject means (-1.25 to 0.52) nearly equal the observed fig4c means. Observed minus shuffled is -0.08 ± 0.09 (p = 0.061), so the "6 of 7 subjects below zero" is the null's offset, not an effect.
- **Offset on synthetic noise.** On independent synthetic signals, reading (b)'s mean z is -0.21 to -0.37.
- **Likely cause.** Moving the FFT's time origin to the segment's centre removes the offset. That points to the phase slope each trial's spectrum carries from where the segment sits in the padded window.
- **Per-trial permutation doesn't help.** Shuffling with one permutation per trial (the claims file's other null reading) leaves (b) miscalibrated (mean -0.51 in delta-theta).

Reading (a) is calibrated: on the shuffled data its mean z is -0.05 and 0.02, its SD is about 1, and 6.0% and 6.9% of pairs pass |z| > 1.96. It is also the first reading the claims file lists, so I adopted it. Under (a):
- **fig4c:** 5 of 7 subjects are below zero, under the 6 the partial match needs.
- **fig5b:** no time point is significant after FDR, which the criterion calls partial.
- **fig5a-spatiotemporal:** the grand means stay at or below 1.01, so it meets the criterion. The notes say this shows little, since the identity trials show no direction under this reading either.

**Added outputs**
- The shuffled-data check now prints the mean z, overall and per subject, under every reading.
- Both readings are also run with one permutation per trial, and the synthetic calibration test is in the notebook.
- **Random-trial control for the 900-ms analysis.** Power is re-run on a random draw of trials from both delays, with as many per condition as the 900-ms-only analysis. It loses about as many effects, so that loss comes from having fewer trials. These tests can't tell whether the 1150-ms timing matters.
- Plots of 70-150 Hz amplitude around the stimuli and test cue, per delay group.
- Task-induced PSI on the 900-ms trials alone.
- Subject-level tests for the time-resolved PSI. Under reading (b) they find no significant point either.

**Corrected text**
- The ERP note now says only the adopted reading's p (0.041) is near the threshold.
- The run time is now stated as 41 to 43 minutes, about 40 to 42 of them in the loading cell. It was 35, with "about 20" streaming.
- The README sentence on the deposited code now separates the code as deposited (99.5 to 100% of pairs on the real data) from its null with the conjugate added (about 90% on shuffled trials).
- The data-check cell now says 187 channels where it said 192.
- The fig2 notes now limit "every reading" to the main analysis.
- Recorded values for the PSI claims whose outcome doesn't depend on the reading now come from reading (a).
- A few counts against the deposited code's null moved slightly because of the new random draws (1042 to 1041, F 59.5 to 58.5), and the text matches the new numbers.

Round 2 is recorded under `verifications`: 16 claims agreed and fig4c disagreed. For fig4c I gave no verifier outcome, because the report doesn't state one.

**Not done**
- PSI with one permutation per trial is run only for the task-induced PSI, not the time-resolved PSI.
- No question was added to `questions/crcns-fcx-3.yaml`, since this report found no place where the claims file misreads the paper.
- Untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) appeared in the working tree during the session. I didn't create them on purpose and left them alone.

Nothing is committed.

## End of run

80 turns, 124 minutes, $5.27 at API prices, result: success.
