# crcns-hc-13 · author-revise-2 · run 42500963730

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-hc-13/verifier-2-report.md; ls entries/crcns-hc-13-yu-2017
```

```
Sun Nov  8 16:44:49 UTC 2026
**Round 2 verifier report: crcns-hc-13-yu-2017-01 (Yu et al. 2017, eLife 6:e27621)**

Counts are taken from the claims file and the attempt record. There are 32 claims and 32 outcomes: 11 reproduced, 7 partially reproduced, 11 not reproduced and 3 blocked. My round-1 totals line ("12 / 8 / 9 / 3") was wrong. My own round-1 table gives 11 / 7 / 11 / 3, and the record correctly does not copy that line.

### 1. Outcomes and assumptions

I agree with 30 of the 32 outcomes. Most are unchanged since round 1. The two that need comment:

**fig4s1b-offset-matched-coactivity (reproduced): I now agree; this changes my round-1 view.**
- The criterion for this claim does not say "under one reading". Its parent criterion, fig4b, does say "under one reading of O6 and O7", and so does every other multi-reading criterion in the claims file. So passing under O7(a) with O6(a) is a fair reading.
- My edge concern is settled by cell 82. With pinned pairs left out, the 4–5 s bin still passes (111 MAP-MAP vs 23 MAP-IAP pairs, p = 0.0004).
- It remains fragile: it passes under only one of four reading combinations. Under O7(b) there are only 8–13 MAP-IAP pairs per bin.

**fig2s1cd-theta-autocorrelation (partially reproduced): I disagree.**
- The criterion takes entry and exit from O1. The claims file's O1(b) makes every immobility period an entry or exit, and under that reading all four depth comparisons hold (cell 64), so the outcome is reproduced.
- The partial outcome rests on "well visits": immobility periods of at least 0.5 s within 15 cm of a well. The claims file has no such reading. It is the same kind of departure I refused for the no-width-rule variant in fig1s4b.
- The case that fails is a near tie: 0.00089 vs 0.00093, with 13 IAPs.
- The record should keep the claims file's reading for the outcome, and give the visit result as a variant.
- The visit definition may well be closer to the paper. The paper's "periods at wells" (Figure 1, supplement 1B–C
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## Author/,/## Verifier/p' docs/protocol.md | head -300; grep -n "proposed" -A10 docs/*.md | head -80
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

[... 361 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 470,510p docs/protocol.md; ls attempts | grep crcns-hc-13; ls questions | grep hc-13; cat questions/crcns-hc-13.yaml 2>/dev/null | head -80
```

```
reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method."

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
revision adds it to `questions/<folder>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
attempt, in an `answer` run started by hand; the claim's outcome stays as
tested on the claims file, and a later attempt takes up any change.
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/crcns-hc-13-yu-2017-01.yaml; grep -n "^  - claim\|^[a-z_]*:\|^- claim\|round:" attempts/crcns-hc-13-yu-2017-01.yaml | head -120
```

```
1059 attempts/crcns-hc-13-yu-2017-01.yaml
1:schema_version: 2
2:id: crcns-hc-13-yu-2017-01
3:dataset:
8:paper: doi:10.7554/elife.27621
9:date: '2026-11-08'
10:entry: crcns-hc-13-yu-2017
11:provenance:
22:outcomes:
23:- claim: fig1-iap-map-counts
33:- claim: fig1s4b-foraging-counts
62:- claim: fig1d-well-specificity
78:- claim: fig1e-iap-lower-speed
95:- claim: fig1s4d-foraging-speed
112:- claim: fig1f-iap-smaller-coverage
137:- claim: fig1s1d-transition-interval
159:- claim: fig2c-continuous-transition
190:- claim: fig2s1cd-theta-autocorrelation
220:- claim: fig2s1ij-theta-behavior-correlation
253:- claim: fig2s2-fewer-coincident-spikes
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 159,260p attempts/crcns-hc-13-yu-2017-01.yaml; sed -n 374,460p attempts/crcns-hc-13-yu-2017-01.yaml
```

```
- claim: fig2c-continuous-transition
  outcome: reproduced
  notebook: reproduce_yu_2017.ipynb
  output: claim:fig2c-continuous-transition
  notes: With well visits, 81 MAP-IAP pairs at entry and 81 at exit with > 100 coincident events
    (paper 207 and 217 over both tasks); the lower notch of the median correlogram is above zero in 46
    of 50 bins from 0 to 0.5 s at entry and in all 50 bins from -0.5 to 0 s at exit. With every
    immobility period (94 and 93 pairs) it is above zero in all 50 bins at both. It is above zero in
    0.94 to 1.00 of the bins on the other side of zero lag too, and the median correlogram holds about
    as much mass there, so the criterion as written does not separate the paper's smooth and abrupt
    scenarios sharply. The first round printed the 'other side' from the criterion's own side; that is
    corrected.
  deviations:
  - Tested on the five foraging rats only; the six W-track rats the paper pools with them are not in hc-13,
    and their data (CRCNS hc-6) were not used.
  - 'Wells and well entries and exits follow O1 reading (b), the only one the data allow (no beam-break
    times): wells are the peaks of immobile occupancy in the outer part of each quadrant of the maze,
    pooled over an animal''s days, and entries and exits are the starts and ends of immobility periods.
    The paper does not say how to find wells without the beam break; this is an assumption. In every animal
    the four wells sit at the corners of the tracked area.'
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 817,830p attempts/crcns-hc-13-yu-2017-01.yaml; sed -n 876,960p attempts/crcns-hc-13-yu-2017-01.yaml; grep -n "proposed\|agrees" tools/entry.py | head -40
```

```
verifications:
- date: '2026-11-08'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The handover of the first run, the executed notebook with the conclusions and summary removed,
    the helper module and the claims file, with the paper under paper/. Round-1 report in transcripts/crcns-hc-13/verifier-1-report.md.
  results:
  - claim: fig1-iap-map-counts
    agrees: true
    outcome: blocked
    reason: The pooled count needs the W-track rats. hc-6 is on the archive (9 rats, about 23 GB), but
      the paper does not say which six rats or days it used, and some come from Kay et al. 2016. The foraging
      part is tested under fig1s4b and fails, so the pooled count could not be reached anyway.
    response: 'blocked_by changed from not_runnable to data_missing, as the verifier gives it, with that
  - claim: fig2c-continuous-transition
    agrees: true
    outcome: reproduced
    reason: The lower notch is above 0 in 50 of 50 bins at both entry and exit. The criterion is nearly
      trivial, and the windows probably cover most of task time (problem 3).
    response: 'Problem 3: the coverage is now printed per day; windows around every immobility period
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 260,330p tools/entry.py; grep -n "proposed" -A15 schemas/attempt*.json | head -50
```

```
continue
        known = claims_by_target.get((dataset_id(attempt), attempt.get("paper")))
        if labels_used.get((dataset_id(attempt), attempt.get("paper"))):
            kinds = {f.get("kind") for f in attempt.get("findings") or []}
            if not attempt.get("inputs") or not kinds & {"metadata_insufficient", "identifier_missing"}:
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
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-13-yu-2017; python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i,c in enumerate(nb.cells):
    print(i,c.cell_type,c.metadata.get('tags',[]),repr(c.source[:100]))
"; ls ../../executed/crcns-hc-13-yu-2017/ 2>/dev/null
```

```
Exit code 2
0 markdown [] '# Reproducing Yu et al. (2017) from CRCNS hc-13\n\nPaper. Yu JY, Kay K, Liu DF, Grossrubatscher I, Lob'
1 code [] 'import time\nimport resource\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom scipy impor'
2 code [] 'R, STREAM = Y.stream_dataset(Y.process_animal)\nprint(f"streamed {STREAM[\'bytes\'] / 1e9:.2f} GB of {Y'
3 code [] 'ANIMALS = [a for a in ["T1", "S2", "Q1", "R1", "N2"] if a in R]\nTB = {a: Y.day_tables(R[a]) for a in'
4 markdown [] '## Data check'
5 code ['sanity'] 'print("Archive members (name, bytes):")\nfor name, size in STREAM["members"]:\n    print(f"  {name:28s'
6 markdown [] 'The archive holds 30 files, six per animal, as the data descriptor lists (eeg, rawpos, spikes,\ncelli'
7 code ['sanity'] 'urows = []\nfor a in ANIMALS:\n    for u in R[a]["units"]:\n        n = sum(len(v) for v in u["spikes"]'
8 markdown [] 'Units are counted per day (O4): the files number units within each day, and nothing links a unit\nacr'
9 code ['sanity'] 'sw = []\nfor a in ANIMALS:\n    for d, dd in R[a]["days"].items():\n        for rd, v in dd["swr"].item'
10 markdown [] "The paper's threshold (the 99.99th percentile of the mirrored noise distribution) lies at 0.04 to\n0."
11 code ['sanity'] '# Wells: four clusters of immobile positions per day (O1 (b))\nwr = []\nfor a in ANIMALS:\n    for d, t'
12 markdown [] 'The data set holds only the task sessions (epochs 2, 4 and 6, type `Run`); the rest sessions the\npap'
13 code ['sanity'] '# Clocks. Spikes against position: IAP rate at its well with true spike times and with spikes shifte'
14 markdown [] 'The clocks agree: in every animal with IAPs, their rate at the well falls by about half when spikes\n'
15 markdown [] '## Cell selection'
16 markdown [] '### fig1s4b-foraging-counts\n\n> In the foraging task, 33 CA1 units are IAPs and 244 are MAPs.\n\n(Figur'
17 code ['claim:fig1s4b-foraging-counts'] 'def counts(cells):\n    df = pd.DataFrame([dict(animal=c["animal"], day=c["day"
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-13-yu-2017; python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i,c in enumerate(nb.cells[42:76]):
    print(i+42,c.cell_type,c.metadata.get('tags',[]),repr(c.source[:80]))
"; ls ../../executed/crcns-hc-13-yu-2017/
```

```
Exit code 2
42 markdown [] '### fig4d-iap-swr-lower-power\n\n> IAP-SWRs have lower 150 to 250 Hz power than MA'
43 code ['claim:fig4d-iap-swr-lower-power'] 'print("Mean z-scored 150-250 Hz power in the 100 ms after SWR onset:", {t: round'
44 markdown [] '**Result: partially reproduced.** IAP-SWRs have lower 150 to 250 Hz power than M'
45 markdown [] '### fig4s5-cells-spikes-per-swr\n\n> IAP-SWRs contain fewer active cells (mean 1.0'
46 code ['claim:fig4s5-cells-spikes-per-swr'] 'cm, ci = G["MAP"].n_map, G["IAP"].n_iap\nsm_, si_ = G["MAP"].s_map, G["IAP"].s_ia'
47 markdown [] '**Result: not reproduced.** IAP-SWRs hold fewer active cells than MAP-SWRs (1.03'
48 markdown [] '### fig4s67-matched-subsamples\n\n> IAP-SWRs remain shorter and lower in power tha'
49 code ['claim:fig4s67-matched-subsamples'] 'rng = np.random.default_rng(67)\n\n\ndef matched_subsamples(var_i, var_m, reading, '
50 markdown [] '**Result: reproduced on the foraging rats.** After matching the distribution of '
51 markdown [] '### fig4s8-interspersed\n\n> There is no strong relation in timing between IAP-SWR'
52 code ['claim:fig4s8-interspersed'] 'rng = np.random.default_rng(8)\nedges = np.arange(-2, 2.0001, 0.01)\ncen = 0.5 * ('
53 markdown [] '**Result: reproduced on the foraging rats.** Outside |lag| < 0.2 s, 18 of 360 bi'
54 markdown [] '### fig4e-iap-spike-earlier\n\n> In SWRs with both MAPs and IAPs, IAPs spike earli'
55 code ['claim:fig4e-iap-spike-earlier'] 'rng = np.random.default_rng(4)\nboth = SWRT[SWRT.type == "MAP & IAP"]\nrec = {"IAP'
56 markdown [] '**Result: reproduced on the foraging rats.** In 293 MAP & IAP-SWRs, IAP spikes c'
57 markdown [] '## Cell pairs: correlograms and SWR coactivity'
58 code [] 'def mask_spikes(sp, starts, ends):\n    o = np.argsort(starts)\n    return sp[Y.in'
59 code [] 'def pair_type(c1, c2):\n    return "-".join(sorted([c1["label"], c2["label"]], re'
60 markdown [] '### fig2c-continuous-transition\n\n> MAP and IAP spiking overlap in time as the an'
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-13-yu-2017; python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i in [60,61,62,63,64,65]:
    print('=====',i); print(nb.cells[i].source)
"
```

```
===== 60
### fig2c-continuous-transition

> MAP and IAP spiking overlap in time as the animal enters and leaves a reward well, so the MAP-relative-to-IAP cross-correlogram has a tail extending beyond 0 s lag, a smooth and not an abrupt transition.

(Figure 2C; Results, Smooth transition between CA1 movement and immobility spatial representations, paragraph 2; data: `with_inputs`)

Spikes within 1.5 s of any entry (or exit) form the trains; their cross-correlogram over +-1.5 s
lags, MAP time minus IAP time, 10 ms bins. Restricting spikes to the union of the windows, and not
pairing spikes window by window, is a standard choice. Entries and exits are those of well visits
(`visit_mask`, an assumption): the windows around all immobility periods cover 32 to 62% of task time
(median 53%), those around well visits 9 to 37% (median 25%), as printed above. Both are shown.

===== 61
fig, ax = plt.subplots(2, 2, figsize=(10, 5.5))
lagc = np.arange(-1.495, 1.5, 0.01)
for r_, (defn, sfx) in enumerate((("well visits (assumption)", "_v"), ("all immobility periods (O1 b as written)", ""))):
    for k, (name, rng_) in enumerate((("entry", (0, 0.5)), ("exit", (-0.5, 0)))):
        col = name + sfx
        sel = PR[(PR.type == "MAP-IAP") & (PR[f"n_{col}"] > 100)]
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i in [66,67,68,83,87,88,89]:
    print('=====',i); print(nb.cells[i].source)
"
```

```
===== 66
### fig2s1ij-theta-behavior-correlation

> Cross-correlation peak offsets of cell pairs on the theta time scale are significantly correlated with their peak offsets on the behavioral time scale of seconds.

(Figure 2, supplement 1I-J legend; data: `with_inputs`)

Theta-scale peak: the largest bin of the +-125 ms correlogram (10 ms bins) of spikes within the
entry (exit) windows. Behavioural peak: the peak of the +-3.3 s correlogram of spikes outside
SWRs, smoothed with a Gaussian of sigma 150 ms (legend).

===== 67
for defn, sfx in (("well visits", "_v"), ("all immobility periods", "")):
    for edge in (False, True):
        for k in ("entry", "exit"):
            for t in ("MAP-IAP", "MAP-MAP"):
                col = k + sfx
                sel = PR[(PR.type == t) & (PR[f"n_{col}"] > 100)].dropna(subset=[f"theta_{col}", "off33"])
                if edge:
                    sel = sel[~sel.edge_off33]
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i in [0,6,14,114]:
    print('=====',i); print(nb.cells[i].source)
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and 'visit' in c.source and i not in (60,62,65,68,89,114): print('VISIT in',i)
"; cat README.md
```

```
===== 0
# Reproducing Yu et al. (2017) from CRCNS hc-13

Paper. Yu JY, Kay K, Liu DF, Grossrubatscher I, Loback A, Sosa M, Chung JE, Karlsson MP,
Larkin MC, Frank LM (2017). Distinct hippocampal-cortical memory representations for experiences
associated with movement versus immobility. *eLife* 6:e27621,
[doi:10.7554/eLife.27621](https://doi.org/10.7554/eLife.27621). The claims file was written from
the version of record (PMC5576488): main text, figure legends, the legends of all figure
supplements, and the Materials and methods.

Data set. CRCNS hc-13, Yu, Liu, Grossrubatscher and Frank (2017), "Simultaneous extracellular
recordings from hippocampal area CA1 and dorsal medial prefrontal cortex from rats performing a
foraging task", [doi:10.6080/K0H41PK8](https://doi.org/10.6080/K0H41PK8). Version: `unversioned`.
CRCNS data sets have no versions, and the paper cites the data set without one, so the version
used is the one published under `hc-13/live/` in the public bucket `crcnsarchive`, the only copy of
the data (`hc-13/orig/v0_7/` holds only the documentation of version 0.7 of the descriptor). The
data are one file, `hc-13/live/data.tar.gz` (8,719,155,400 bytes), whose MD5 in the data set's
`checksums.md5` is `f45a799b63c543d82d61933c0c87efbb`; the notebook computes the MD5 of the bytes
it streams and prints whether they match, so a later change is detectable. The archive is a gzipped
tar, which can only be read from its start: it is streamed once, and each animal is reduced as its
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i in [31,33]:
    print('=====',i); print(nb.cells[i].source)
"; sed -n 137,158p ../../attempts/crcns-hc-13-yu-2017-01.yaml
```

```
===== 31
### fig1s1d-transition-interval

> The animals switch between movement and immobility every 6 to 7 s; the autocorrelation of well entry and exit times peaks at 6.4 to 6.6 s in the foraging task.

(Figure 1, supplement 1D legend; Results, Identification of CA1 place cells, paragraph 1; data: `dataset`)

Entries and exits are the starts and ends of immobility periods (O1 (b)). The criterion's "peak
away from zero lag" is taken as the maximum after the first trough at positive lag. Variants: only
periods of at least 0.5 s or 1 s, the well visits used for Figure 2 (`visit_mask`), and visits
defined as runs of frames within 15 cm of a well.

===== 33
**Result: not reproduced.** The peak of the autocorrelation of entry and exit times after its
first trough is at 14.3 s for all immobility periods, outside 5.76 to 7.26 s; with periods of at
least 0.5 s it is at 14.3 s, of at least 1 s at 16.5 s, and for the well visits used below (periods
of at least 0.5 s within 15 cm of a well) at 14.1 s. Runs of frames within 15 cm of a well give 4.1
s. No definition tried gives a peak in the paper's range.
- claim: fig1s1d-transition-interval
  outcome: not_reproduced
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit.py <<'EOF'
import nbformat
P='reproduce_yu_2017.ipynb'
nb=nbformat.read(P,4)
S=lambda i: nb.cells[i].source
def rep(i,a,b):
    assert a in nb.cells[i].source,(i,a)
    nb.cells[i].source=nb.cells[i].source.replace(a,b)

# header
rep(0,"(hc-6 holds more than 28 GB over nine rats, and\nthe paper","(hc-6 holds nine rats, and the paper")
rep(0,"""For the analyses around well entry and exit (Figure 2 and its supplements, Figure 4,
supplement 3), entries and exits are the starts and ends of well visits, immobility periods of at
least 0.5 s within 15 cm of a well (an assumption, `visit_mask`); every immobility period, O1 (b) as
the claims file writes it, is shown beside it.""","""For the analyses around well entry and exit (Figure 2 and its supplements, Figure 4,
supplement 3), entries and exits are the starts and ends of every immobility period, O1 (b) as the
claims file writes it, and the outcomes rest on that. Well visits, immobility periods of at least
0.5 s within 15 cm of a well (`visit_mask`, not a reading in the claims file), are shown as a
variant; whether the claims file's O1 (b) misreads the paper's entries is asked in
`questions/crcns-hc-13.yaml`.""")
# data check
rep(6,"Each day has three task\nsessions; some are","Days hold one to three task sessions (35\nsessions over T1's 12 days, as printed above); some are")
# clocks
rep(14,"their rate at the well falls by about half when spikes\nare shifted by 30 s","their rate at the well falls by about half or more when\nspikes are shifted by 30 s (by two thirds in S2, 7.65 to 2.51 Hz)")

# fig2c
rep(60,"""Entries and exits are those of well visits
(`visit_mask`, an assumption): the windows around all immobility periods cover 32 to 62% of task time
(median 53%), those around well visits 9 to 37% (median 25%), as printed above. Both are shown.""","""Entries and exits are the starts and ends of
every immobility period (O1 (b) as the claims file writes it); the outcome rests on these. Their
windows cover 32 to 62% of task time (median 53%). Well visits (`visit_mask`, immobility periods of at
least 0.5 s within 15 cm of a well, not a reading in the claims file), whose windows cover 9 to 37%
(median 25%), are a variant.""")
rep(61,'(("well visits (assumption)", "_v"), ("all immobility periods (O1 b as written)", ""))','(("all immobility periods (O1 b as written)", ""), ("well visits (variant)", "_v"))')
nb.cells[62].source="""**Result: reproduced on the foraging rats.** With every immobility period (O1 (b) as written), for 94
MAP-IAP pairs at entry and 93 at exit (paper, both tasks: 207 and 217), the lower notch of the median
cross-correlogram is above zero in all 50 bins from 0 to 0.5 s at entry and in all 50 bins from -0.5 to
0 s at exit. With the well-visit variant (81 and 81 pairs) it is above zero in 46 of 50 bins at entry
and all 50 at exit. The lower notch is also above zero in 0.94 to 1.00 of the bins on the other side of
zero lag, and the median correlogram holds about as much mass there (0.147 against 0.107 at entry,
0.119 against 0.130 at exit, for well visits), so the criterion, as written, does not separate the
smooth and abrupt scenarios of Figure 2A-B sharply."""
# fig2s1cd
rep(64,'for k in ("entry_v", "exit_v", "entry", "exit"):','for k in ("entry", "exit", "entry_v", "exit_v"):')
rep(64,"k.replace('_v', ' (well visits)')","k.replace('_v', ' (well visits, variant)')")
rep(64,"k + ' (all immobility periods)'","k + ' (all immobility periods, O1 b as written)'")
nb.cells[65].source="""**Result: partially reproduced on the foraging rats (the verified outcome); reproduced is proposed.**
With every immobility period (O1 (b) as the claims file writes it), the mean autocorrelation at speed
> 4 cm/s has a local maximum between 0.105 and 0.125 s for MAPs and IAPs at entry and exit, and its
depth is larger than at speed < 1 cm/s in all four cases (MAP 0.00653 against 0.00140 at entry and
0.00636 against 0.00193 at exit; IAP 0.00104 against 0.00043 and 0.00135 against 0.00053), so the
criterion holds under the claims file's reading. With the well-visit variant (68 and 73 MAPs, 13 IAPs)
three of four hold: MAPs at entry (0.00479 against 0.00244) and exit (0.00526 against 0.00255) and IAPs
at exit (0.00147 against 0.00119), not IAPs at entry (0.00089 against 0.00093), a near tie on small
IAP depths. The recorded outcome, partially reproduced, rested on the well visits; as the visits are
not a reading in the claims file, the outcome under its reading, reproduced, is proposed for a third
verification round."""
# fig2s1ij
rep(67,'(("well visits", "_v"), ("all immobility periods", ""))','(("all immobility periods (O1 b as written)", ""), ("well visits (variant)", "_v"))')
nb.cells[68].source="""**Result: not reproduced.** The theta-scale and behavioural-scale peaks are not correlated. With
every immobility period (O1 (b) as written), at entry r = 0.030 (p = 0.78) for 92 MAP-IAP pairs and
-0.052 (p = 0.41) for 248 MAP-MAP pairs, at exit -0.027 (p = 0.80) and 0.001 (p = 0.99); with the
well-visit variant r = 0.047 (p = 0.68, 79 pairs), -0.025 (p = 0.81, 99), 0.072 (p = 0.53) and 0.076
(p = 0.47). Spearman correlations are as small (p >= 0.38). Leaving out the pairs whose 3.3 s peak is
pinned at the window's edge (29 MAP-IAP and 108 MAP-MAP pairs, see the O7 histogram) gives no
significant correlation either (p >= 0.14)."""
# fig4s1b
rep(83,"""Under O6 (b) one bin misses (2 to 3 s, p = 0.074); with the +-10 s window (O7 b) only
the 3 to 4 s bin is significant, with 8 to 13 MAP-IAP pairs per bin.""","""Under O6 (b) one bin misses (2 to 3 s, p = 0.074). With the +-10 s window (O7 b), 8 to
13 MAP-IAP pairs per bin, only the 3 to 4 s bin is significant under O6 (a) (p = 0.014), and no bin
from 1 to 5 s is under O6 (b) (3 to 4 s, p = 0.066).""")
# fig4s3
rep(88,'(("well visits", "_v"), ("all immobility periods", ""))','(("all immobility periods (O1 b as written)", ""), ("well visits (variant)", "_v"))')
nb.cells[89].source="""**Result: partially reproduced.** Among pairs with overlapping spikes, MAP-IAP pairs have lower
coactivity than MAP-MAP pairs at entry and at exit: with every immobility period (O1 (b) as written)
p = 9.9e-09 and 3e-08 (O6 a), with the well-visit variant p = 2.6e-05 and 0.00028 (O6 a; 81 MAP-IAP
against 99 and 95 MAP-MAP pairs). They are not lower than the 2 IAP-IAP pairs, whose medians are
-1.60 (O6 a) and -1.75 (O6 b), against MAP-IAP medians of -0.31 to -0.06. Under O6 (b) the IAP-IAP
comparison gives p = 0.027 (all periods) and 0.03 (well visits), but in the wrong direction: MAP-IAP
pairs are higher. Two of the four comparisons hold, under each reading and each definition of entry."""
# summary
rep(114,"| fig2s1cd-theta-autocorrelation | partially reproduced (foraging rats) |","| fig2s1cd-theta-autocorrelation | partially reproduced (foraging rats; reproduced under the claims file's O1 (b) is proposed) |")
rep(114,"""For the analyses around entry and exit, entries and exits are those of well visits
(immobility periods of at least 0.5 s within 15 cm of a well, an assumption); with every immobility
period, as O1 (b) is written, the windows cover about half of task time, and those results are shown
beside.""","""For the analyses around entry and exit, entries and exits are the starts and ends of
every immobility period, as O1 (b) is written; their windows cover about half of task time. Well
visits (immobility periods of at least 0.5 s within 15 cm of a well) are shown as a variant, and
whether O1 (b) misreads the paper's entries is asked of a reader.""")
nbformat.write(nb,P)
EOF
python $TMPDIR/edit.py && git diff --stat
```

```
.../crcns-hc-13-yu-2017/reproduce_yu_2017.ipynb    | 127 +++++++++++----------
 1 file changed, 64 insertions(+), 63 deletions(-)
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
print(nb.cells[1].source[-600:]); print('---'); print(nb.cells[2].source)
"
```

```
import time
import resource
import warnings

import numpy as np
import pandas as pd
from scipy import stats
from scipy.ndimage import gaussian_filter1d as gaussian
import matplotlib.pyplot as plt

import yu2017 as Y

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
started = time.time()
---
R, STREAM = Y.stream_dataset(Y.process_animal)
print(f"streamed {STREAM['bytes'] / 1e9:.2f} GB of {Y.DATASET} ({Y.VERSION}) in {time.time() - started:.0f} s; "
[... 2 more lines not kept]
```

**Agent**

I'll add a closing code cell that prints the total run time and peak memory, so the README figure is backed by output, then start the full run.

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
P='reproduce_yu_2017.ipynb'
nb=nbformat.read(P,4)
assert nb.cells[114].source.startswith('## Summary')
nb.cells.insert(114, nbformat.v4.new_code_cell('print(f"notebook run time {time.time() - started:.0f} s; peak memory "\n      f"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")'))
nbformat.write(nb,P)
EOF
cd ../..; date -u; python tools/entry.py check entries/crcns-hc-13-yu-2017 2>&1 | tail -5
```

```
Sun Nov  8 16:46:46 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/crcns-hc-13-yu-2017 > $TMPDIR/run.log 2>&1; tail -15 $TMPDIR/run.log; date -u
```

```
real	13m13.918s
user	6m25.203s
sys	0m35.032s
Installed kernelspec registry-crcns-hc-13-yu-2017 in executed/crcns-hc-13-yu-2017/.venv/share/jupyter/kernels/registry-crcns-hc-13-yu-2017
0 error(s)
pass  reproduce_yu_2017.ipynb  (784 s)
Sun Nov  8 17:00:07 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/crcns-hc-13-yu-2017; ls; python - <<'EOF'
import nbformat,glob
nb=nbformat.read(glob.glob('*.ipynb')[0],4)
def out(i):
    s=''
    for o in nb.cells[i].get('outputs',[]):
        s+=o.get('text','') if o.output_type=='stream' else str(o.get('data',{}).get('text/plain',''))
    return s
import re
o5=out(5); print(o5[:3000])
print('=== 2'); print(out(2))
print('=== 13'); print(out(13))
for i in (61,64,67,82,88,114): print('===',i); print(out(i))
EOF
```

```
reproduce_yu_2017.ipynb
result.json
Archive members (name, bytes):
  data/S2/S2eeg.mat              2240717536
  data/S2/S2rawpos.mat              6108762
  data/S2/S2cellinfo.mat              29174
  data/S2/S2spikes.mat             44891440
  data/S2/S2task.mat                    274
  data/S2/S2tetinfo.mat                3793
  data/T1/T1task.mat                    295
  data/T1/T1rawpos.mat              7580050
  data/T1/T1cellinfo.mat              35858
  data/T1/T1eeg.mat              2845123499
  data/T1/T1tetinfo.mat                4817
  data/T1/T1spikes.mat             90588824
  data/R1/R1task.mat                    283
  data/R1/R1spikes.mat             83292304
  data/R1/R1cellinfo.mat              28332
  data/R1/R1rawpos.mat              3609057
  data/R1/R1eeg.mat              1272519942
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-hc-13-yu-2017 && python - <<'EOF'
import nbformat
P='reproduce_yu_2017.ipynb'
nb=nbformat.read(P,4)
c=nb.cells[6]
a="Days hold one to three task sessions (35\nsessions over T1's 12 days, as printed above); some are"
assert a in c.source
c.source=c.source.replace(a,"Each day has three task sessions except\none day of T1, which has two (35 sessions over its 12 days, as printed above); some are")
nb.cells[62].source="""**Result: reproduced on the foraging rats.** With every immobility period (O1 (b) as written), for 94
MAP-IAP pairs at entry and 93 at exit (paper, both tasks: 207 and 217), the lower notch of the median
cross-correlogram is above zero in all 50 bins from 0 to 0.5 s at entry and in all 50 bins from -0.5 to
0 s at exit. With the well-visit variant (81 and 81 pairs) it is above zero in 46 of 50 bins at entry
and all 50 at exit. The lower notch is also above zero in 0.94 to 1.00 of the bins on the other side of
zero lag, and the median correlogram holds about as much mass there (0.148 against 0.132 on the
criterion's side at entry, 0.138 against 0.146 at exit, with every immobility period; 0.147 against
0.107 and 0.119 against 0.130 with well visits), so the criterion, as written, does not separate the
smooth and abrupt scenarios of Figure 2A-B sharply."""
c=nb.cells[89]
c.source=c.source.replace("p = 0.027 (all periods) and 0.03 (well visits)","p = 0.027 and 0.028 (all periods) and 0.03 (well visits)")
nbformat.write(nb,P)
EOF
cd  git check-ignore executed && echo ignored
```

```
executed
ignored
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
cd entries/crcns-hc-13-yu-2017 && python - <<'EOF'
p='README.md'; s=open(p).read()
a="(about 14 minutes in all, 6.2 GB of memory at peak)"
b="(the last code cell prints the run time, 776 s in the latest run, and the peak memory, 6.2 GB)"
assert a in s; s=s.replace(a,b)
a="""so wells are inferred from immobile positions,
and well entries and exits from immobility periods at a well (well visits, an assumption)."""
b="""so wells are inferred from immobile positions,
and well entries and exits are the starts and ends of immobility periods, as the claims file's O1 (b) gives them; well visits
(immobility periods of at least 0.5 s within 15 cm of a well) are shown as a variant."""
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Grep**

```json
{
 "pattern": "visit",
 "path": "entries/crcns-hc-13-yu-2017/yu2017.py",
 "output_mode": "content"
}
```

```
491:    # positions of all its days (day-wise clusters drift onto rarely visited wells' paths).
673:    The rate in visited bins is smoothed with normalized convolution, so unvisited
675:    bins visited for less than that; the paper sets no minimum, so 0 is the main
```

**Agent calls Grep**

```json
{
 "pattern": "visit_mask|def visit",
 "path": "entries/crcns-hc-13-yu-2017/reproduce_yu_2017.ipynb",
 "output_mode": "content",
 "-A": 4
}
```

```
43:    "0.5 s within 15 cm of a well (`visit_mask`, not a reading in the claims file), are shown as a\n",
44-    "variant; whether the claims file's O1 (b) misreads the paper's entries is asked in\n",
45-    "`questions/crcns-hc-13.yaml`.\n",
46-    "\n",
47-    "| Claim | Tested | Data |\n",
--
150:    "def visit_mask(per):\n",
151-    "    \"\"\"Immobility periods taken as well visits for the entry and exit analyses (assumption, see the data check).\n",
152-    "\n",
153-    "    O1 (b) of the claims file makes every immobility period an entry and exit. Many periods are brief\n",
154-    "    dips of speed below 4 cm/s away from the wells, and their +-1.5 s windows cover about half of task\n",
--
859:    "periods of at least 0.5 s or 1 s, the well visits used for Figure 2 (`visit_mask`), and visits\n",
860-    "defined as runs of frames within 15 cm of a well.\n"
861-   ]
862-  },
863-  {
--
880:    "            keep = visit_mask(p) if visits else (p[\"end\"] - p[\"start\"]) >= min_dur\n",
881-    "            for ep in np.unique(p[\"epoch\"]):\n",
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
for i,c in enumerate(nb.cells):
    if 'def visit_mask' in c.source or 'the assumption used below' in c.source:
        j=c.source.find('def visit_mask') if 'def visit_mask' in c.source else c.source.find('the assumption used below')-300
        print(i); print(c.source[j:j+1500]); print('-----')
    if c.cell_type=='markdown' and ('assum' in c.source and 'visit' in c.source): print('MD',i, c.source[:1500])
EOF
```

```
3
def visit_mask(per):
    """Immobility periods taken as well visits for the entry and exit analyses (assumption, see the data check).

    O1 (b) of the claims file makes every immobility period an entry and exit. Many periods are brief
    dips of speed below 4 cm/s away from the wells, and their +-1.5 s windows cover about half of task
    time. The paper's entries are visits to a well ("Subjects are immobile during periods at the well",
    Figure 1, supplement 1B), so a visit is taken as an immobility period whose mean position is within
    15 cm of its well and which lasts at least 0.5 s. Radius and duration are choices; the paper gives
    neither, and all immobility periods (the claims file's reading as written) are shown beside it.
    """
    return (per["dist"] < VISIT_RADIUS) & ((per["end"] - per["start"]) >= VISIT_MIN_S)
C = CELLS["a"]  # main reading of O2 (SWR time kept in the denominator); (b) shown where it differs
print("CA1 pyramidal cell-days:", len(C))
-----
58
ict(nos=nos, win=win, map=m, xe=xe, ye=ye, peak=pk, **{k: mask_spikes(c["spikes"], *win[k]) for k in win})
print("cells prepared:", len(PREP))
# How much of task time the +-1.5 s entry and exit windows cover, per day, for all immobility periods (O1 (b) as
# written) and for well visits (visit_mask, the assumption used below)
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
P='reproduce_yu_2017.ipynb'
nb=nbformat.read(P,4)
c=nb.cells[3]
for a,b in [('"""Immobility periods taken as well visits for the entry and exit analyses (assumption, see the data check).',
             '"""Immobility periods taken as well visits, a variant of the entry and exit analyses (not a reading in the claims file).'),
            ("neither, and all immobility periods (the claims file's reading as written) are shown beside it.",
             "neither. All immobility periods, the claims file's reading as written, decide the outcomes; whether that\n    reading misreads the paper is asked in questions/crcns-hc-13.yaml.")]:
    assert a in c.source; c.source=c.source.replace(a,b)
c=nb.cells[58]; a="(visit_mask, the assumption used below)"; assert a in c.source
c.source=c.source.replace(a,"(visit_mask, the variant shown below)")
nbformat.write(nb,P)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  grep -n "O1" -A8 claims/crcns-hc-13/10.7554-elife.27621.yaml | head -40; ls paper; grep -il "periods at the well" -r paper | head
```

```
59:# - O1, "at a reward well". The paper gives neither the well positions nor a radius. Readings:
60-#   (a) between beam-break entry and exit at a well, when the data set holds those times; (b) each
61-#   immobility period (speed < 4 cm/s) assigned to the nearest of the wells, the wells located as
62-#   the centres of the clusters of immobile positions (the Methods say almost all immobility is at
63-#   wells). Well entry and exit times (Figure 2) are the beam-break times under (a) and the starts
64-#   and ends of those immobility periods under (b). For Figure 6 the Methods (PFC and CA1 spiking
65-#   activity) fix well entry as the infrared beam break, so only (a) applies there; the Methods
66-#   (Pre-training) say the beam is crossed by the animal's nose at the well.
67-# - O2, "excluding spikes during SWRs". Methods exclude the spikes; the Results say "excluding
--
113:  criterion: Cells selected as in the opening comment (Methods, Cell selection), under readings O1,
114-    O2 and O4. Reproduced when, under one reading, both counts on the pooled data are within
115-    tolerance. The paper's per-task counts (Figure 1, supplement 4B) add to 83 IAPs but to 679
116-    MAPs (244 + 435), not 659; the MAP count is therefore also judged against 679 with the same
117-    tolerance, and the claim holds when either matches.
118-- id: fig1s4b-foraging-counts
119-  statement: In the foraging task, 33 CA1 units are IAPs and 244 are MAPs.
120-  source: Figure 1, supplement 4B legend
121-  quote: Cells from the foraging task are shown on left (MAP = 244, IAP = 33)
--
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "periods at the well\|well visit\|unrewarded visit\|0 and 3 s\|beam break\|beam-break" paper/10.7554-elife.27621.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

Adding the O1(b) question for a reader.

**Agent calls Bash**

```bash
cat >> questions/crcns-hc-13.yaml <<'EOF'
- claim: fig2s1cd-theta-autocorrelation
  asked: 2026-11-08
  question: >-
    The opening comment's O1 reading (b) makes the start and end of every immobility period (speed
    below 4 cm/s) a well entry and exit. The paper's entries and exits appear to be those of visits
    to a well, the "periods at wells" of Figure 1, supplement 1B and C, which alternate with
    "periods between wells". Should reading (b) take entries and exits from visits to a well (for
    example immobility periods at a well, merged or filtered by position and duration) and not from
    every pause in movement? The same reading is used by fig1s1d, fig2c, fig2s1ij and fig4s3.
  passage: >-
    Distribution of the animal's mean speed during periods at wells (red) and periods between wells
    (black) ... Subjects are immobile during periods at the well and are moving during periods
    between wells. ... In the foraging task, the two smaller peaks at 0 and 3 s for periods at
    wells correspond to visits for which no reward was delivered (incorrect trials) as the rats
    departed the well quickly after discovering the absence of reward (Figure 1, supplement 1B and C
    legend). Autocorrelation of times of entry into and exit from wells (Figure 1, supplement 1D
    legend).
  why: >-
    Under reading (b) as written there are 326 to 1977 immobility periods a day, with a median length
    of 0.23 to 0.37 s, and their +-1.5 s windows cover 32 to 62% of task time (median 53%), so they
    do not isolate transitions at wells. Taking visits (immobility periods of at least 0.5 s whose
    mean position is within 15 cm of a well, an attempt's own choice, as the paper gives no radius or
    duration) the windows cover 9 to 37%. For fig2s1cd the outcome differs between the two, all four
    depth comparisons holding with every immobility period and three of four with visits (IAPs at
    entry 0.00089 against 0.00093). The outcomes of fig2c, fig2s1ij and fig4s3 do not change. The
    paper's peak at 0 s for periods at wells suggests that a 0.5 s minimum would leave out some real
    visits. Raised by the round-2 verifier.
EOF
python -c "import yaml;yaml.safe_load(open('questions/crcns-hc-13.yaml'))" && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
sed -n 1,22p attempts/crcns-hc-13-yu-2017-01.yaml; sed -n 960,1059p attempts/crcns-hc-13-yu-2017-01.yaml
```

```
schema_version: 2
id: crcns-hc-13-yu-2017-01
dataset:
  archive: crcns
  id: hc-13
  version: unversioned
  doi: 10.6080/K0H41PK8
paper: doi:10.7554/elife.27621
date: '2026-11-08'
entry: crcns-hc-13-yu-2017
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
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import yaml
a=yaml.safe_load(open('attempts/crcns-hc-13-yu-2017-01.yaml'))
for o in a['outcomes']: print(o['claim'],o['outcome'],o.get('blocked_by',''))
print(a['verifications'][0].keys())
"
```

```
fig1-iap-map-counts blocked data_missing
fig1s4b-foraging-counts not_reproduced 
fig1d-well-specificity reproduced 
fig1e-iap-lower-speed reproduced 
fig1s4d-foraging-speed reproduced 
fig1f-iap-smaller-coverage not_reproduced 
fig1s1d-transition-interval not_reproduced 
fig2c-continuous-transition reproduced 
fig2s1cd-theta-autocorrelation partially_reproduced 
fig2s1ij-theta-behavior-correlation not_reproduced 
fig2s2-fewer-coincident-spikes not_reproduced 
fig3c-iap-swr-activation partially_reproduced 
fig3s3-iap-same-well-coactivity blocked other
fig4a-swr-counts partially_reproduced 
fig4b-coactivity partially_reproduced 
fig4s1b-offset-matched-coactivity reproduced 
fig4s2c-spatial-proximity-control not_reproduced 
fig4s3-overlapping-pairs partially_reproduced 
fig4c-iap-swr-shorter reproduced 
fig4d-iap-swr-lower-power partially_reproduced 
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'PYEOF'
p='attempts/crcns-hc-13-yu-2017-01.yaml'
s=open(p).read()
def rep(a,b,count=1):
    global s
    n=s.count(a); assert n==count,(n,a[:80]); s=s.replace(a,b)

OLD_VIS="""  - Entries and exits are the starts and ends of well visits, immobility periods of at least 0.5 s
    whose mean position is within 15 cm of the nearest well (visit_mask in the notebook). O1 (b) as
    the claims file writes it makes every immobility period an entry and exit; those number 326 to
    1977 a day, with a median length of 0.23 to 0.37 s, and their +-1.5 s windows cover 32 to 62% of
    task time (median 53%), so they do not isolate transitions. The paper's entries are visits to a
    well (Figure 1, supplement 1B, 'Subjects are immobile during periods at the well'); the visit
    windows cover 9 to 37% (median 25%). The radius and minimum duration are assumptions, as the
    paper gives neither; the results with every immobility period are shown beside.
"""
NEW_VIS="""  - A variant takes entries and exits from well visits, immobility periods of at least 0.5 s whose
    mean position is within 15 cm of the nearest well (visit_mask in the notebook); it is not a reading
    in the claims file, and its radius and minimum duration are the attempt's own choices. Every
    immobility period, as O1 (b) is written, numbers 326 to 1977 a day, with a median length of 0.23 to
    0.37 s, and their +-1.5 s windows cover 32 to 62% of task time (median 53%); the visit windows
    cover 9 to 37% (median 25%). Whether O1 (b) misreads the paper's entries, which appear to be visits
    to a well (Figure 1, supplement 1B and C, 'periods at wells'), is asked in questions/crcns-hc-13.yaml.
"""
rep(OLD_VIS,NEW_VIS,4)

# fig2c notes
rep("""  notes: With well visits, 81 MAP-IAP pairs at entry and 81 at exit with > 100 coincident events
    (paper 207 and 217 over both tasks); the lower notch of the median correlogram is above zero in 46
    of 50 bins from 0 to 0.5 s at entry and in all 50 bins from -0.5 to 0 s at exit. With every
    immobility period (94 and 93 pairs) it is above zero in all 50 bins at both. It is above zero in
    0.94 to 1.00 of the bins on the other side of zero lag too, and the median correlogram holds about
    as much mass there, so the criterion as written does not separate the paper's smooth and abrupt
    scenarios sharply. The first round printed the 'other side' from the criterion's own side; that is
    corrected.""","""  notes: With every immobility period (O1 (b) as written), 94 MAP-IAP pairs at entry and 93 at exit
    with > 100 coincident events (paper 207 and 217 over both tasks); the lower notch of the median
    correlogram is above zero in all 50 bins from 0 to 0.5 s at entry and in all 50 bins from -0.5 to 0
    s at exit. With the well-visit variant (81 and 81 pairs) it is above zero in 46 of 50 and 50 of 50.
    It is above zero in 0.94 to 1.00 of the bins on the other side of zero lag too, and the median
    correlogram holds about as much mass there (0.148 against 0.132 at entry, 0.138 against 0.146 at
    exit, every immobility period), so the criterion as written does not separate the paper's smooth
    and abrupt scenarios sharply. The first round printed the 'other side' from the criterion's own
    side; that is corrected.""")

# fig2s1cd
rep("""  notes: 'With well visits, at > 4 cm/s the mean autocorrelation has a local maximum at 0.105 to 0.125
    s for MAPs (68 and 73 cells) and IAPs (13), at entry and exit. Its depth exceeds that at < 1 cm/s
    for MAPs at entry (0.00479 against 0.00244) and exit (0.00526 against 0.00255) and for IAPs at
    exit (0.00147 against 0.00119), not for IAPs at entry (0.00089 against 0.00093): three of four
    cases. With every immobility period all four hold (MAP 0.00653 against 0.00140 and 0.00636 against
    0.00193; IAP 0.00104 against 0.00043 and 0.00135 against 0.00053). The outcome was reproduced in
    the first round, on every immobility period; it is partially reproduced on the well visits adopted
    after the round-1 verifier found the windows covered much of task time. The failing case is near a
    tie, on small IAP depths.'""","""  notes: 'With every immobility period (O1 (b) as written), at > 4 cm/s the mean autocorrelation has
    a local maximum at 0.115 to 0.125 s for MAPs (150 and 151 cells) and IAPs (14), at entry and exit,
    and its depth exceeds that at < 1 cm/s in all four cases (MAP 0.00653 against 0.00140 and 0.00636
    against 0.00193; IAP 0.00104 against 0.00043 and 0.00135 against 0.00053). With the well-visit
    variant three of four hold, MAPs at entry (0.00479 against 0.00244) and exit (0.00526 against
    0.00255) and IAPs at exit (0.00147 against 0.00119), not IAPs at entry (0.00089 against 0.00093),
    a near tie on small IAP depths. The recorded outcome, partially reproduced, was set after round 1
    on the well visits; round 2 may not change it, so the outcome under the claims file''s reading,
    reproduced, is proposed for a third round.'""")
rep("""  assumed: true
- claim: fig2s1ij-theta-behavior-correlation""","""  assumed: true
  proposed:
    outcome: reproduced
    reason: The criterion takes entry and exit from O1, and under O1 (b) as the claims file writes it,
      every immobility period, all four depth comparisons hold (notebook, fig2s1cd cell). The partial
      outcome rested on well visits, which are not a reading in the claims file (round-2 verifier);
      they are kept as a variant, and whether O1 (b) misreads the paper is asked of a reader.
- claim: fig2s1ij-theta-behavior-correlation""")
# fig2s1ij notes
rep("""  notes: Theta-scale and behavioural-scale peak offsets are uncorrelated. With well visits, entry
    MAP-IAP r = 0.047 (p = 0.68, 79 pairs), MAP-MAP r = -0.025 (p = 0.81, 99); exit 0.072 (p = 0.53)
    and 0.076 (p = 0.47). With every immobility period, 0.030 (p = 0.78, 92), -0.052 (p = 0.41, 248),
    -0.027 (p = 0.80) and 0.001 (p = 0.99).""","""  notes: Theta-scale and behavioural-scale peak offsets are uncorrelated. With every immobility period
    (O1 (b) as written), entry MAP-IAP r = 0.030 (p = 0.78, 92 pairs), MAP-MAP r = -0.052 (p = 0.41,
    248); exit -0.027 (p = 0.80) and 0.001 (p = 0.99). With the well-visit variant, 0.047 (p = 0.68,
    79), -0.025 (p = 0.81, 99), 0.072 (p = 0.53) and 0.076 (p = 0.47).""")
# fig4s1b
rep("""under O7 (b) only 3 to 4 s is significant (8 to 13 MAP-IAP pairs per bin).""","""under O7 (b) (8 to 13 MAP-IAP pairs per bin) only 3 to 4 s is significant
    with O6 (a) (p = 0.014), and no bin from 1 to 5 s with O6 (b) (3 to 4 s, p = 0.066).""")
# fig4s3
rep("""  notes: With well visits, MAP-IAP lower than MAP-MAP at entry (p = 2.6e-05) and exit (p = 0.00028),
    O6 (a); with every immobility period p = 9.9e-09 and 3e-08. Against the 2 IAP-IAP pairs (medians
    -1.60 O6 a, -1.75 O6 b) MAP-IAP is higher, not lower (medians -0.31 to -0.06); under O6 (b) that
    comparison gives p = 0.03 (visits) and 0.027 (all periods), in the wrong direction.""","""  notes: With every immobility period (O1 (b) as written), MAP-IAP lower than MAP-MAP at entry (p =
    9.9e-09) and exit (p = 3e-08), O6 (a); with the well-visit variant p = 2.6e-05 and 0.00028. Against
    the 2 IAP-IAP pairs (medians -1.60 O6 a, -1.75 O6 b) MAP-IAP is higher, not lower (medians -0.31
    to -0.06); under O6 (b) that comparison gives p = 0.027 and 0.028 (all periods) and 0.03 (visits),
    in the wrong direction.""")
open(p,'w').write(s)
PYEOF
python $TMPDIR/rec.py && echo done
```

```
done
```

**Agent calls Bash**

```bash
grep -n -i "visit" attempts/crcns-hc-13-yu-2017-01.yaml | sed -n 1,60p | cut -c1-160
```

```
121:    bins visited for at least 0.1 s 166 against 162 (p = 0.41, square) and 20 against 23 (p = 0.67,
131:  - The occupancy map is smoothed by normalized convolution over visited bins, a standard choice.
144:    visits as used for Figure 2, 14.1 s), outside 5.76 to 7.26 s. Runs of frames within 15 cm of a
155:  - The well visits of the entry and exit analyses (immobility periods of at least 0.5 s within 15
166:    s at exit. With the well-visit variant (81 and 81 pairs) it is above zero in 46 of 50 and 50 of 50.
182:  - A variant takes entries and exits from well visits, immobility periods of at least 0.5 s whose
183:    mean position is within 15 cm of the nearest well (visit_mask in the notebook); it is not a reading
186:    0.37 s, and their +-1.5 s windows cover 32 to 62% of task time (median 53%); the visit windows
187:    cover 9 to 37% (median 25%). Whether O1 (b) misreads the paper's entries, which appear to be visits
197:    against 0.00193; IAP 0.00104 against 0.00043 and 0.00135 against 0.00053). With the well-visit
201:    on the well visits; round 2 may not change it, so the outcome under the claims file''s reading,
211:  - A variant takes entries and exits from well visits, immobility periods of at least 0.5 s whose
212:    mean position is within 15 cm of the nearest well (visit_mask in the notebook); it is not a reading
215:    0.37 s, and their +-1.5 s windows cover 32 to 62% of task time (median 53%); the visit windows
216:    cover 9 to 37% (median 25%). Whether O1 (b) misreads the paper's entries, which appear to be visits
223:      outcome rested on well visits, which are not a reading in the claims file (round-2 verifier);
231:    248); exit -0.027 (p = 0.80) and 0.001 (p = 0.99). With the well-visit variant, 0.047 (p = 0.68,
249:  - A variant takes entries and exits from well visits, immobility periods of at least 0.5 s whose
250:    mean position is within 15 cm of the nearest well (visit_mask in the notebook); it is not a reading
253:    0
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,158p attempts/crcns-hc-13-yu-2017-01.yaml; sed -n 810,830p attempts/crcns-hc-13-yu-2017-01.yaml
```

```
pooled over an animal''s days, and entries and exits are the starts and ends of immobility periods.
    The paper does not say how to find wells without the beam break; this is an assumption. In every animal
    the four wells sit at the corners of the tracked area.'
  - The criterion's 'peak away from zero lag' is taken as the maximum after the first local minimum at
    positive lag; 0.2 s bins and Gaussian sigma 0.5 s as the claims file gives.
  - The well visits of the entry and exit analyses (immobility periods of at least 0.5 s within 15
    cm of a well) are shown as a further variant; the outcome is the same under every definition
    run.
  assumed: true
    distribution of 'envelope power') lies at about 0 to 0.8 z of the envelope amplitude here, giving
    about 2 SWRs per second of immobility, and below the mean for the squared envelope. Was the envelope
    amplitude or its square used, over which times was the histogram taken, and how many awake SWRs per
    day did the foraging rats give?
- kind: methods_unavailable
  statement: Question for the paper's authors. How were IAPs and MAPs selected in R1 and N2, whose stored
    spike widths mostly exceed 0.4 ms? Without the width rule there the MAP count (250) and the PFC selection
    (113) match the paper's 244 and 112.
- kind: methods_unavailable
  statement: Question for the paper's authors. Without beam-break times, which definition of a well visit
    (radius, minimum duration) reproduces the entries and exits of Figures 1 and 2 and the 6.4 to 6.6
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
p='attempts/crcns-hc-13-yu-2017-01.yaml'
s=open(p).read()
a="  - The well visits of the entry and exit analyses (immobility periods"
assert s.count(a)==1; s=s.replace(a,"  - The well-visit variant of the entry and exit analyses (immobility periods")
rec=yaml.safe_load(s)
out={o['claim']:o['outcome'] for o in rec['outcomes']}
GEN="Agrees; the outcome is unchanged since round 1, and the numbers checked match the printed outputs."
NC="No change."
R={
 'fig1s4b-foraging-counts':("Agrees. The no-width-rule variant is left unchanged, which is correct (round-1 point 11).",NC),
 'fig2c-continuous-transition':("Agrees. Reproduced, but the test is weak: the lower notch is also above zero on the side the "
   "criterion does not test, in 94 to 100% of bins (cell 61); the conclusion says so. Well visits, not a reading in the claims "
   "file, replaced O1 (b) as the main definition, and the shared O1 (b) deviation, which says entries and exits are the starts "
   "and ends of immobility periods, contradicts the next deviation, which says they are those of well visits.",
   "Every immobility period (O1 (b) as written) is now the main definition in the notebook, the notes and the deviations, and "
   "well visits are a variant; the contradictory deviation is rewritten. The outcome is the same under both."),
 'fig2s1cd-theta-autocorrelation':("Disagrees. The criterion takes entry and exit from O1; under O1 (b), which makes every "
   "immobility period an entry or exit, all four depth comparisons hold (cell 64), so the outcome is reproduced. The partial "
   "outcome rests on well visits, which the claims file has no reading for, the same kind of departure refused for the "
   "no-width-rule variant in fig1s4b; the failing case is a near tie (0.00089 against 0.00093, 13 IAPs). The record should keep "
   "the claims file's reading for the outcome and give the visit result as a variant. The visit definition may well be closer to "
   "the paper (its 'periods at wells' are visits), in which case O1 (b) is a misreading to report to the claims file, not to fix "
   "in the attempt; the paper's 0 s peak suggests the 0.5 s minimum excludes some real visits. The record also contradicts "
   "itself on entries in the O1 (b) deviation.",
   "Outcome kept as partially_reproduced, as round 2 may not change it; reproduced, the result under O1 (b) as written, is "
   "recorded under proposed for a third round. The notebook and record now put every immobility period first and the visits "
   "as a variant, the contradictory deviation is rewritten, and the question whether O1 (b) misreads the paper's entries, "
   "with the 0 s peak, is added to questions/crcns-hc-13.yaml."),
 'fig2s1ij-theta-behavior-correlation':("Agrees. Well visits, not a reading in the claims file, replaced O1 (b) as the main "
   "definition; only fig2s1cd's outcome depends on this. The O1 (b) deviation contradicts the visit deviation.",
   "Every immobility period is now the main definition and well visits a variant; the deviation is rewritten. No change of outcome."),
 'fig3c-iap-swr-activation':("Agrees. The 3 SD check leaves the outcome as it was, so the low threshold is not what drives "
   "the failure (round-1 point 1 resolved).",NC),
 'fig4a-swr-counts':("Agrees. The 3 SD check leaves the outcome as it was, and the 12-day variant matches the printed outputs "
   "(round-1 points 1 and 7 resolved).",NC),
 'fig4s1b-offset-matched-coactivity':("Agrees, changing the round-1 view. The criterion's parent, fig4b, says 'under one "
   "reading of O6 and O7', as do the other multi-reading criteria, so passing under O7 (a) with O6 (a) is a fair reading. The "
   "edge concern is settled by cell 82: with pinned pairs left out the 4 to 5 s bin still passes (111 MAP-MAP against 23 "
   "MAP-IAP pairs, p = 0.0004). It remains fragile, passing under only one of four reading combinations, with 8 to 13 MAP-IAP "
   "pairs per bin under O7 (b). Cell 83 and the notes say that with O7 (b) only the 3 to 4 s bin is significant; that holds "
   "only under O6 (a) (p = 0.014); under O7 (b) with O6 (b) no bin from 1 to 5 s is significant (3 to 4 s, p = 0.066).",
   "Cell 83 and the notes now give the O7 (b) result under each O6 reading (p = 0.014 under O6 (a); no bin under O6 (b), 3 to 4 "
   "s p = 0.066). No change of outcome."),
 'fig4s3-overlapping-pairs':("Agrees. The medians (-0.31 to -0.06) and the wrong-direction p = 0.03 and 0.027 match the "
   "outputs. Well visits, not a reading in the claims file, replaced O1 (b) as the main definition, and the O1 (b) deviation "
   "contradicts the visit deviation.",
   "Every immobility period is now the main definition and well visits a variant; the deviation is rewritten. No change of outcome."),
 'fig5-pfc-modulated-fraction':("Agrees. The 3 SD check leaves the outcome as it was; the sensitivity run matches the outputs.",NC),
 'fig5dg-pfc-groups':("Agrees. The 3 SD check leaves the outcome as it was; the sensitivity run matches the outputs.",NC),
 'fig5s1d-shuffle-control':("Agrees. Averaging over 100 replicates per unit is reasonable, and 0.394 / 0.328 / 0.495, p = "
   "0.36 and 0.73, below 0.05 in 23 of 100 single replicates, match the outputs (round-1 point 5 resolved).",NC),
 'fig4e-iap-spike-earlier':("Agrees. The duration weighting is reasonable.",NC),
 'fig6e-coincidence-index':("Agrees. The independence of the values is now stated (round-1 point 8 resolved).",NC),
}
results=[]
for c,o in out.items():
    reason,resp=R.get(c,(GEN,NC))
    r=dict(claim=c,agrees=c!='fig2s1cd-theta-autocorrelation',outcome='reproduced' if c=='fig2s1cd-theta-autocorrelation' else o,reason=reason,response=resp)
    results.append(r)
other=("Text corrected where the report found it unsupported: the data check now says each day has three task sessions "
  "except one day of T1 with two (35 over 12 days); the header no longer gives a size for hc-6; the README gives the run time "
  "and peak memory printed by a new last code cell (776 s, 6.2 GB); the clock check says the IAP rate falls by about half or "
  "more, by two thirds in S2 (7.65 to 2.51 Hz).")
for r in results:
    if r['claim'] in ('fig1-iap-map-counts',):
        r['response']="No change. "+other
rnd=dict(date='2026-11-08',kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
  reviewed=("The full executed notebook of the revision after round 1, the helper module, the claims file and the attempt "
            "record, with the paper under paper/. Round-2 report in transcripts/crcns-hc-13/verifier-2-report.md."),
  results=results)
text=yaml.safe_dump([rnd],sort_keys=False,width=110,allow_unicode=True)
open(p,'w').write(s.rstrip('\n')+'\n'+text)
yaml.safe_load(open(p))
PYEOF
python $TMPDIR/ver.py && tail -30 attempts/crcns-hc-13-yu-2017-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git diff | grep "^+" | grep -n "—\|rather" ; date -u; python tools/entry.py all entries/crcns-hc-13-yu-2017 > $TMPDIR/run2.log 2>&1; tail -4 $TMPDIR/run2.log; date -u
```

```
Sun Nov  8 17:02:33 UTC 2026
Installed kernelspec registry-crcns-hc-13-yu-2017 in executed/crcns-hc-13-yu-2017/.venv/share/jupyter/kernels/registry-crcns-hc-13-yu-2017
0 error(s)
pass  reproduce_yu_2017.ipynb  (1054 s)
Sun Nov  8 17:20:16 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/crcns-hc-13-yu-2017; python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_yu_2017.ipynb',4)
def out(i):
    return ''.join(o.get('text','') for o in nb.cells[i].get('outputs',[]) if o.output_type=='stream')
print(out(2)); print(out(114))
import hashlib
for i in (61,64,67,82,88):
    print(i, hashlib.md5(out(i).encode()).hexdigest())
EOF
cd ../..; python tools/entry.py check entries/crcns-hc-13-yu-2017 | tail -3; git status --short
```

```
processing S2
processing T1
processing R1
processing Q1
processing N2
streamed 8.72 GB of hc-13 (unversioned) in 918 s; MD5 f45a799b63c543d82d61933c0c87efbb matches checksums.md5
peak memory 6.2 GB

notebook run time 1047 s; peak memory 6.2 GB

61 4077d375b68224a2be4c3f06340abdac
64 d37697a6a74cd763f0a1220f7f82d2c2
67 55e8b0977668a453fa6c3572a3836b1e
82 4f2313d35e53622eefd08152a93550ad
88 f602e068e9c5709d9a0b2579c51a2043
0 error(s)
 M attempts/crcns-hc-13-yu-2017-01.yaml
 M entries/crcns-hc-13-yu-2017/README.md
 M entries/crcns-hc-13-yu-2017/reproduce_yu_2017.ipynb
 M questions/crcns-hc-13.yaml
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat
nb=nbformat.read('executed/crcns-hc-13-yu-2017/reproduce_yu_2017.ipynb',4)
out=lambda i:''.join(o.get('text','') for o in nb.cells[i].get('outputs',[]) if o.output_type=='stream')
print(out(64)[:400]); print(out(82)[-300:])
EOF
sed -i 's/(the last code cell prints the run time, 776 s in the latest run, and the peak memory, 6.2 GB)/(the last code cell prints the run time, 776 and 1047 s in the two latest runs as the stream speed varied, and the peak memory, 6.2 GB)/' entries/crcns-hc-13-yu-2017/README.md
sed -i 's/new last code cell (776 s, 6.2 GB)/new last code cell (776 and 1047 s in two runs, 6.2 GB)/' attempts/crcns-hc-13-yu-2017-01.yaml
grep -n "1047" entries/crcns-hc-13-yu-2017/README.md attempts/crcns-hc-13-yu-2017-01.yaml | cut -c1-120; python tools/entry.py check entries/crcns-hc-13-yu-2017 | tail -1
```

```
MAP entry (all immobility periods, O1 b as written): move: n = 150, theta peak at 0.115 s, depth 0.00653; still: n = 54, theta peak at 0.135 s, depth 0.00140
MAP exit (all immobility periods, O1 b as written): move: n = 151, theta peak at 0.115 s, depth 0.00636; still: n = 51, theta peak at 0.135 s, depth 0.00193
MAP entry (well visits, variant): move: n = 68, theta peak at 0.105 s, depth 0.00479;
56) MI 0.16 (n = 8) p = 0.25
O7 10 s, O6 (b): 0-1 s: MM 2.52 (n = 154) MI 1.34 (n = 15) p = 0.041; 1-2 s: MM 1.53 (n = 116) MI 0.59 (n = 9) p = 0.38; 2-3 s: MM 0.96 (n = 83) MI 0.36 (n = 9) p = 0.27; 3-4 s: MM 0.75 (n = 47) MI 0.39 (n = 13) p = 0.066; 4-5 s: MM 0.82 (n = 56) MI 0.13 (n = 8) p = 0.2

entries/crcns-hc-13-yu-2017/README.md:9:  the public bucket `crcnsarchive` once (the last code cell prints the run time,
attempts/crcns-hc-13-yu-2017-01.yaml:1077:      for hc-6; the README gives the run time and peak memory printed by a new
0 error(s)
```

**Agent calls Bash**

```bash
sed -n 8,11p entries/crcns-hc-13-yu-2017/README.md; sed -n 1074,1080p attempts/crcns-hc-13-yu-2017-01.yaml
```

```
- `reproduce_yu_2017.ipynb` streams the data set's single archive, `hc-13/live/data.tar.gz`, from
  the public bucket `crcnsarchive` once (the last code cell prints the run time, 776 and 1047 s in the two latest runs as the stream speed varied, and the peak memory, 6.2 GB), checks its MD5
  against the data set's `checksums.md5`, and tests each claim of
  `claims/crcns-hc-13/10.7554-elife.27621.yaml`.
    reason: Agrees; the outcome is unchanged since round 1, and the numbers checked match the printed outputs.
    response: 'No change. Text corrected where the report found it unsupported: the data check now says each day
      has three task sessions except one day of T1 with two (35 over 12 days); the header no longer gives a size
      for hc-6; the README gives the run time and peak memory printed by a new last code cell (776 and 1047 s in two runs, 6.2 GB); the
      clock check says the IAP rate falls by about half or more, by two thirds in S2 (7.65 to 2.51 Hz).'
  - claim: fig1s4b-foraging-counts
    agrees: true
```

**Agent**

I worked through every point in the round-2 report and re-ran the entry. The second full run passed in 1047 s with 6.2 GB of memory at peak, and `tools/entry.py check` reports 0 errors. I didn't commit anything.

**Outcomes.** None changed, since round 2 doesn't allow it.
- **fig2s1cd-theta-autocorrelation** stays `partially_reproduced`. I added a `proposed` change to `reproduced` for a third verification round. The verifier was right: under the claims file's reading O1 (b), where every immobility period counts as a well entry or exit, all four depth comparisons hold (for example MAP 0.00653 against 0.00140, IAP 0.00104 against 0.00043). The partial result came only from the "well visit" definition, which the claims file doesn't have.
- **fig4s1b-offset-matched-coactivity**: the verifier now agrees with `reproduced`, and round 2 records that.

**What I corrected**
- **Entry and exit definition** (fig2c, fig2s1cd, fig2s1ij, fig4s3): every immobility period, as O1 (b) is written, is now the main definition in the notebook, the helper docstring, the README, the summary and the record. Well visits (immobility periods of at least 0.5 s within 15 cm of a well) are shown only as a variant. I also rewrote the deviation that said two contradictory things about what an entry is, in all four outcomes.
- **Question for a reader**: added to `questions/crcns-hc-13.yaml`. It asks whether O1 (b) misreads the paper, whose "periods at wells" (Figure 1, supplement 1B–C) look like visits. It includes the verifier's point that the paper's 0 s peak suggests a 0.5 s minimum would leave out some real visits. The claim itself is unchanged.
- **Statements the outputs didn't support:**
  - The fig4s1b conclusion and notes now say that under O7 (b) the 3 to 4 s bin is significant only under O6 (a) (p = 0.014), and no bin is under O6 (b) (p = 0.066 at 3 to 4 s).
  - The data check now says each day has three sessions except one day of T1 with two (35 sessions over 12 days).
  - The header no longer gives a size for hc-6 (the "28 GB" figure).
  - The clock check now says the IAP rate falls by about half or more, and by two thirds in S2 (7.65 to 2.51 Hz).
  - The README run time had no printed output behind it. I added a last code cell that prints the run time and peak memory, and the README now quotes it: 776 s and 1047 s in two runs, because streaming speed varies, and 6.2 GB.
- **fig2c**: the conclusion now gives the "other side of zero lag" figures for both definitions.
- **Record**: round 2 is entered under `verifications` for all 32 claims, with the verifier's reasons as it gave them and my responses.

**Not done**: nothing the report asked for was left out. The long R1/N2 spike widths still can't be checked, as the verifier noted, because the data hold no waveforms.

## End of run

38 turns, 36 minutes, $1.75 at API prices, result: success.
