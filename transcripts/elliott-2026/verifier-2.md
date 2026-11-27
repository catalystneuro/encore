# elliott-2026 · verifier-2 · run 44884697151

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 1644
drwxr-xr-x 6 runner runner    4096 Nov 21 08:56 .
drwxr-xr-x 8 runner runner    4096 Nov 21 08:56 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 21 08:56 .claude
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.development
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.local
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.production
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.test
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .env.test.local
drwx------ 2 runner runner    4096 Nov 21 08:56 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .github
-rw-r--r-- 1 runner runner       0 Nov 21 08:56 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 08:23 .mcp.json
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 elliott-2026.yaml; echo ----; head -80 elliott-2026-01.yaml
```

```
# Elliott, Andrews et al. (2026) on DANDI:001132

Tests the claims of Elliott, Andrews et al., "Microscale maps of bursting dynamics across human
hippocampal slices from patients with epilepsy" (J. Neurophysiol. 2026, doi:10.1152/jn.00217.2025)
on dandiset 001132 version 0.241130.1903, the raw recordings of Andrews et al. 2024. The curated
spike sortings the paper analysed are read from the paper's repository
(github.com/braingeneers/human_hippocampus at commit 0f83f70).

- `reproduce_elliott_2026.ipynb`: the link of the sortings to the raw files, and the claims that
  need spikes only.
- `lfp_elliott_2026.ipynb`: the claims on the raw voltage.
- `hippo.py`: loading (dandiset streaming, sortings from the repository) and the measures.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The outcomes are in `attempts/elliott-2026-01.yaml`.
# Claims for Elliott, Andrews et al. (2026), J. Neurophysiol. 135, "Microscale maps of bursting
# dynamics across human hippocampal slices from patients with epilepsy", doi:10.1152/jn.00217.2025,
# tested on dandiset 001132 (relation reuses).
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,2000p elliott-2026-01.yaml
```

```
<persisted-output>
Output too large (42KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/b8aea55d-0f6e-451c-8482-e2296274cf77/tool-results/b99e6esni.txt

Preview (first 2KB):
    bursting starts within the first second, so the separate baseline recording of the same slice
    (recorded before KA; Results, paragraph 10) is used as the pre-KA reference, and the
    recording's own mean for slices without one.
  - Peaks closer than 50 ms are merged by keeping the higher (scipy find_peaks distance); the
    synchrony window of +-50 ms around a burst is a standard choice.
- claim: methods-burst-counts
  outcome: not_reproduced
  notebook: reproduce_elliott_2026.ipynb
  output: claim:methods-burst-counts
  measured: [353, 12, 344.1, 157, 19.4, 490.8]
  notes: Under every reading S1 has 12 epochs (within tolerance of 11) over 344 s (within tolerance
    of 350) but 124 to 353 bursts against 67; S2 has 89 to 157 bursts against 47, a first epoch of
    19.4 s against 50 s, and bursts over 486 to 491 s against 350. No reading matches all S1 or all
    S2 values. In the first 254 s every reading has 9 epochs where the code lists 8 seizure
    windows, and 90 to 92% of S1 bursts fall in those windows. Measured is reading a, sigma 10.
  deviations:
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/b8aea55d-0f6e-451c-8482-e2296274cf77/tool-results/b99e6esni.txt"
}
```

```
1	    bursting starts within the first second, so the separate baseline recording of the same slice
2	    (recorded before KA; Results, paragraph 10) is used as the pre-KA reference, and the
3	    recording's own mean for slices without one.
4	  - Peaks closer than 50 ms are merged by keeping the higher (scipy find_peaks distance); the
5	    synchrony window of +-50 ms around a burst is a standard choice.
6	- claim: methods-burst-counts
7	  outcome: not_reproduced
8	  notebook: reproduce_elliott_2026.ipynb
9	  output: claim:methods-burst-counts
10	  measured: [353, 12, 344.1, 157, 19.4, 490.8]
11	  notes: Under every reading S1 has 12 epochs (within tolerance of 11) over 344 s (within tolerance
12	    of 350) but 124 to 353 bursts against 67; S2 has 89 to 157 bursts against 47, a first epoch of
13	    19.4 s against 50 s, and bursts over 486 to 491 s against 350. No reading matches all S1 or all
14	    S2 values. In the first 254 s every reading has 9 epochs where the code lists 8 seizure
15	    windows, and 90 to 92% of S1 bursts fall in those windows. Measured is reading a, sigma 10.
16	  deviations:
17	  - The S2 duration of synchronized bursting is read as the span of its first epoch; the paper
18	    does not define it.
19	- claim: methods-rate-increase-after-ka
20	  outcome: not_reproduced
[... 619 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 50,400p elliott-2026.yaml
```

```
#   S1). The repository holds no code for the Kuiper test.
# - STTC clustering (figures/figure_3/sttc.ipynb). STTC with a 20 ms window (the braingeneers
#   default); entries of 0.3 or more (the diagonal included) set to 0; Euclidean distances between
#   rows; complete linkage; optimal leaf ordering. The two groups are read from the reordered
#   matrix by eye.
# - Sub-bursts of the S1 initiation stage (figures/figure_2/burst_peak_comparison.ipynb) are set
#   by hand at 14.4, 14.57, 14.75 and 14.91 s of the S1 KA recording. No code detects bursts,
#   superbursts, stages or rolling waves.
# - The LFP filters (human_hip/raw_data/filter.py) are order-5 Butterworth, zero phase; the
#   Methods give order 5 for the LFP bands and "fourth order" for the theta plots.
#
# Data the paper used. Recordings of Andrews et al. 2024 (Nat. Neurosci., ref 8), which the
# dandiset accompanies: organotypic human hippocampal slices (300 um, 4 to 8 days in culture,
# transduced with AAV9-CAMK2A-HcKCR1-eYFP) from patients with refractory mesial temporal lobe
# epilepsy, recorded on a MaxOne HD-MEA (26,400 electrodes, about 1,000 selected, 20 kHz). Of 12
# slices of the original study, 6 with at least 50 sorted units were analysed (S1 to S6, each from
# a different patient; Extended Data Tables 1 and 4), in 8 recordings:
#   1 S1, dentate gyrus, kainic acid (KA), seizure-like, 6 min, 212 units (patient A, 52 F, ILAE type 1)
#   2 S1, baseline (no drug), 5 min, 249 units
#   3 S2, dentate gyrus, KA, seizure-like, 8.5 min, 180 units (patient B, 35 M, no HS)
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,900p elliott-2026.yaml
```

```
- quantity: rolling waves per burst
    value: 3.1
    tolerance: 1.3
  - quantity: rolling wave propagations, S1 seizure stage
    value: 200
    tolerance: 20
  - quantity: rolling wave propagations, S2 seizure stage
    value: 35
    tolerance: 3.5
  criterion: The paper counted rolling waves by watching videos and gives no detector or the list
    of bursts investigated. This claim cannot be judged on the paper's method; it is blocked as
    methods_underspecified unless a detector defined in fig1j-theta-propagation-stages (a theta
    cycle whose lag-plane direction matches the seizure direction within 45 degrees and explains
    most of the lag variance) is adopted as an assumption, in which case it is reproduced when all
    five values are within tolerance (the range 2 to 4 widened by 10% of each bound is 1.8 to
    4.4).
- id: fig2a-subbursts-track-theta
  statement: At the initiation stage of S1 the first burst splits into three sub-bursts whose
    peaks and troughs coincide with the theta oscillation, and the change in single-unit firing
    from sub-burst to sub-burst alternates between the same two spatial modes as theta; S2 shows a
[... 346 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for nb in reproduce_elliott_2026 lfp_elliott_2026; do python3 - "$nb" <<'EOF'
import json,sys
nb=sys.argv[1]
d=json.load(open(nb+'.ipynb'))
out=open('/tmp/claude/'+nb+'.txt','w') if False else open(__import__('os').environ.get('TMPDIR','/tmp')+'/'+nb+'.txt','w')
for i,c in enumerate(d['cells']):
    out.write(f"\n===== CELL {i} [{c['cell_type']}] =====\n")
    out.write(''.join(c['source'])+'\n')
    for o in c.get('outputs',[]):
        if 'text' in o: out.write('--- out ---\n'+''.join(o['text'])+'\n')
        elif 'data' in o:
            if 'text/plain' in o['data']: out.write('--- out(data) ---\n'+''.join(o['data']['text/plain'])+'\n')
            if 'image/png' in o['data']: out.write('[image]\n')
        elif o.get('output_type')=='error': out.write('--- ERROR ---\n'+o['ename']+': '+o['evalue']+'\n')
print(nb,len(d['cells']))
EOF
done; wc -l $TMPDIR/*.txt
```

```
reproduce_elliott_2026 69
lfp_elliott_2026 45
  1072 /tmp/claude-1001/lfp_elliott_2026.txt
  1418 /tmp/claude-1001/reproduce_elliott_2026.txt
  2490 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_elliott_2026.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Reproducing Elliott, Andrews et al. (2026): spike-based claims
4	
5	Paper: Elliott, Andrews et al., "Microscale maps of bursting dynamics across human hippocampal slices
6	from patients with epilepsy", J. Neurophysiol. (2026), doi:10.1152/jn.00217.2025. The claims file
7	(`claims/elliott-2026.yaml`) was written from the accepted author manuscript in PubMed Central
8	(PMC12931417) and its supplement (Extended Data).
9	
10	Dataset: DANDI:001132, version 0.241130.1903 (doi:10.48324/dandi.001132/0.241130.1903), the raw
11	HD-MEA recordings of Andrews et al. 2024. The paper cites the dandiset without a version. Two
12	versions are published, 0.241119.1801 and 0.241130.1903; both list the same 69 assets with the same
13	total size, so the most recent published version is pinned, as the protocol says for a paper that
14	cites none.
15	
16	Outside input: the curated spike sortings the paper analysed are not in the dandiset. They are read
17	into memory from the paper's repository, github.com/braingeneers/human_hippocampus at commit
18	0f83f704ee4c9b4d8d7f75eb53d94f525c85abb2 (the claims file's opening comment). Which sorting file is
19	which recording is taken from the paper's latency notebooks (`figures/figure_3/latencies/t_test_try30_try3/`),
20	which load one file per recording (see `hippo.RECORDINGS`).
[... 679 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/reproduce_elliott_2026.txt",
 "offset": 700,
 "limit": 720
}
```

```
700	   S2 c (b, sigma 10)    2.343      2.377    -0.034       0.9       False
701	   S2 c (b, sigma 20)    2.343      2.377    -0.034       0.9       False
702	units KA/baseline: 212 249 | 180 51
703	
704	
705	===== CELL 31 [markdown] =====
706	**Result: not reproduced.** The mean rate per unit is lower in the KA recordings than in the baseline recordings: S1 4.20 against 4.32 spikes/s (-0.12), S2 2.28 against 2.38 (-0.10); over the bursting periods the change is -0.03 to -0.05. Reading (a) cannot be run, as no time of KA application is recorded. The KA and baseline sortings were curated separately (212 and 249 units in S1, 180 and 51 in S2), so the comparison is between different unit sets.
707	
708	===== CELL 32 [markdown] =====
709	## methods-onset-latency (blocked)
710	
711	> Epileptiform-like activity began in S1 and S2 shortly after kainic acid was applied.
712	
713	The criterion needs the time of KA application from the dandiset's metadata or annotations. The data
714	check above shows that the files hold no epochs, intervals, annotations or stimulus series, and the
715	session descriptions are empty, so the claim is blocked as `metadata_insufficient`. For reference,
716	the first detected burst is printed (it bounds the latency only if KA was applied at or before the
717	recording start, which nothing states).
718	
719	===== CELL 33 [code] =====
[... 700 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/lfp_elliott_2026.txt",
 "limit": 560
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Reproducing Elliott, Andrews et al. (2026): claims on the raw voltage
4	
5	Paper: Elliott, Andrews et al., "Microscale maps of bursting dynamics across human hippocampal slices
6	from patients with epilepsy", J. Neurophysiol. (2026), doi:10.1152/jn.00217.2025; claims file
7	`claims/elliott-2026.yaml`, written from the accepted manuscript (PMC12931417) and its Extended Data.
8	
9	Dataset: DANDI:001132 version 0.241130.1903 (the most recent published version; the paper cites no
10	version, and the two published versions list the same 69 assets; see the header of
11	`reproduce_elliott_2026.ipynb`). Raw voltage is streamed; spike sortings come from the paper's
12	repository at commit 0f83f70 (outside input). The link between sortings and raw files is
13	established in `reproduce_elliott_2026.ipynb` (claim sorting-dandiset-link) and repeated here in
14	short: recordings 1 to 6 are found in the dandiset, recordings 7 (S5) and 8 (S6) are not.
15	
16	| Claim | Status here |
17	|---|---|
18	| table2-phase-locking-counts | tested on recordings 1 to 6; 7 and 8 have no raw recording |
19	| table2-phase-locking-seizure-vs-not | tested |
20	| fig2b-phase-cluster-kuiper | tested |
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/lfp_elliott_2026.txt",
 "offset": 560,
 "limit": 520
}
```

```
560	--- out ---
561	6 sub-9E-2 (10000, 936) range 629 to 1001 uV; 21 s
562	
563	
564	===== CELL 22 [markdown] =====
565	## ext4-electrode-lag-clusters
566	
567	> In the two epileptiform slices, k-means clustering of electrodes by their pairwise theta lags gives
568	> spatial clusters that replicate the theta propagation of each stage, while the slices without
569	> epileptiform activity (S3 to S6) show no spatial pattern.
570	
571	Lag matrix as the Methods (`hippo.lag_matrix`), k-means with 2 clusters on its rows (random state
572	from the claim's seed), spatial coherence against 1000 label shuffles (`hippo.spatial_coherence`).
573	Theta filter order 5 (code) and 4 (Methods' theta plots). The S2 initiation window of the code is
574	94 ms, shorter than one theta cycle; the longer windows above are run as variants, with the fraction
575	of lags at the +-40 ms edge (`frac_at_edge`).
576	
577	===== CELL 23 [code] =====
578	seed = zlib.crc32(b"elliott-2026/ext4-electrode-lag-clusters")
579	LAGS, LABS = {}, {}
[... 494 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def phase_lock_unit" -A40 hippo.py; grep -n "def theta\b\|def theta(" -A12 hippo.py; grep -n "def burst_synchrony" -A25 hippo.py
```

```
444:def phase_lock_unit(spk_ms, th, mode="envelope"):
445-    """Phase locking of one unit to the theta of its electrode (Methods, Phase locking neurons to
446-    theta wave activity). th: theta at 1 kHz on the same clock as spk_ms (list of window arrays,
447-    each with its start in ms). Methods reading ('envelope'): spikes kept while the Hilbert
448-    envelope exceeds the RMS of the theta series over the analysed span. Code reading ('cycle'):
449-    spikes kept within theta cycles (trough to trough) whose envelope peak exceeds the RMS of the
450-    envelope. Returns (n_spikes_kept, rayleigh_p, circular_mean)."""
451-    from astropy.stats import rayleightest, circmean
452-    import astropy.units as u
453-    allth = np.concatenate([w for _, w in th])
454-    rms_sig = np.sqrt(np.mean(allth ** 2))
455-    env_all = np.concatenate([np.abs(signal.hilbert(w)) for _, w in th])
456-    rms_env = np.sqrt(np.mean(env_all ** 2))
457-    phases = []
458-    for start, w in th:
459-        an = signal.hilbert(w)
460-        ph = np.angle(an)
461-        env = np.abs(an)
462-        idx = np.round(spk_ms - start).astype(int)
463-        idx = idx[(idx >= 0) & (idx < len(w))]
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" elliott-2026.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('elliott-2026-01.yaml'))
from collections import Counter
print(len(d['outcomes']),Counter(o['outcome'] for o in d['outcomes']))
print([ (i+1,f.get('severity')) for i,f in enumerate(d['findings'])])
print(len(d['verifications'][0]['results']))"
```

```
24
24 Counter({'not_reproduced': 8, 'partially_reproduced': 7, 'reproduced': 6, 'blocked': 3})
[(1, 'major'), (2, 'major'), (3, 'major'), (4, 'minor'), (5, 'minor'), (6, 'minor'), (7, 'none'), (8, 'major'), (9, None), (10, None), (11, None), (12, None), (13, None), (14, None)]
24
```

**Agent calls Bash**

```bash
cd  grep -n -i "unknown\|location" $TMPDIR/*.txt | head
```

```
(Bash completed with no output)
```

**Agent**

**Verifier report, round 2: Elliott, Andrews et al. 2026 on DANDI:001132**

The claims file has 24 claims. The attempt record has 24 outcomes: 6 reproduced, 7 partially reproduced, 8 not reproduced, 3 blocked. "Spike nb" means `reproduce_elliott_2026.ipynb` and "LFP nb" means `lfp_elliott_2026.ipynb`.

### 1. Outcomes

I agree with all 24 outcomes. Five need a comment.

- **s4-ka-no-epileptiform (partially reproduced, assumed): agree.**
  - Once only synchronized bursts are kept (more than half of the units rising), S3 to S6 have none under any reading. S1 has 77 to 138 and S2 has 89 to 134 (spike nb cell 35).
  - The positive control still fails for S1: its longest epoch is 8 to 10 s, and it is the same with every burst kept. So the miss comes from the 5 s gap rule, not from the synchrony filter.
  - The criterion does not define a partial outcome. "Partial" fairly describes a case where neither of its clauses applies.
  - Both assumptions are stated in the deviations and are reasonable: "synchronized" means more than half of units rising, and "sustained" means an epoch longer than 10 s.
- **ext3-onset-spectral-signature (reproduced, assumed): I now agree; in round 1 I said partial.**
  - The new variant uses the first epoch that has 5 s of recording before it, under the criterion's own burst reading (b). It gives 3 of 3 electrodes in both electrode sets (LFP nb cell 40). So the result no longer rests only on the author's 14.4 s onset.
  - The criterion names the 0.1 to 100 Hz amplitude as an allowed reading, so "reproduced" follows from it.
  - The assumption is stated and reasonable: the criterion's own onset (0.73 to 0.90 s) leaves no 5 s baseline and falls inside the wavelet's edge region.
  - The notes should keep saying that the theta-amplitude reading fails at every onset (0 of 3 everywhere; at most 1.92x).
- **table2-phase-locking-counts (not reproduced): I now agree; in round 1 I said partial.** The criterion and the claims file's opening comment make the Methods' envelope selection the main reading and the code's cycle selection a variant. Under the envelope selection S1 gives 60, outside 70 ± 7. One condition remains (section 3a).
- **fig2b-phase-cluster-kuiper (reproduced): agree only by the letter of the criterion.**
  - Under the Methods' spike selection, the only reading with p ≤ 0.01 is reading (b). That split cannot fail (p = 0, LFP nb cell 18).
  - The spatial readings under the Methods' selection give 0.037 and 0.11, which would be partial.
  - The record treats the cycle selection as a variant that does not count in table2. For consistency, this outcome then rests on a test that carries no evidence.
- **methods-rolling-wave-counts (blocked): agree.** The criterion's detector was run and finds 0 rolling waves in 63 cycles (LFP nb cell 34). Adopting it would give not reproduced. Declining to adopt it is allowed by the criterion and the reason is given.

The other 19 outcomes are supported by the outputs I cite in section 2 and need no comment: link, table1, fig1g, burst counts, rate, onset latency, fig1j, ext4b, ext4, fig2a, table2-seizure-vs-not, fig2c, the two ext9 claims, the two fig3a claims, ext10, table3 and ext12.

### 2. Sentences against the printed outputs

The "**Result:" cells I checked hold against their outputs: spike nb cells 15, 18, 24, 28, 31, 37, 43, 46, 49, 53, 58, 61 and 64, and LFP nb cells 13, 16, 19, 26, 29, 32, 35, 38 and 42. Exceptions:

- **Attempt record, ext4 notes and round-1 response.** The record says "every window of one theta cycle or longer passes under all five seeds (250 ms …; 500 ms …; 1 s …; 35.0 to 35.5 s …)". The response says "250 ms, 500 ms and 1 s … all pass under all five seeds". Cell 24 runs the five seeds only for the 250 ms and 500 ms windows. The 1 s and 35.0 to 35.5 s windows were run with one seed (cell 23). Notebook cell 26 itself does not make the five-seed claim.
- **Attempt record, finding 5.** "electrode locations are all 'unknown'" is not shown by any printed output; spike nb cell 3 prints age and sex only.
- **LFP nb cell 42.** "amplitude ratios 0.77 to 1.31" is the broadband range only. The theta ratios at those onsets reach 1.91 (cell 40). This is minor.
- **Spike nb Summary (cell 67), "What was found about the dataset".** It leaves out the possible sub-3C duplicates, which are a major finding in the record and are shown in cell 5.

The README sentences and the other notes in the record are supported by the outputs.

My round-1 reasons appear in `verifications` in my own words. Each of the 14 problems is attached to its claim, and the agree/disagree flags are right (ext3 and table2-counts disagree; all others agree).

### 3. Round-1 points

Resolved:

- Problem 1 (s4 synchrony).
- Problem 2 (ext3 onset): the criterion's onset was rerun under all four readings, and a variant with a 5 s baseline was added.
- Problem 3 (S2 initiation windows; sub-burst sources printed, LFP nb cell 8).
- Problem 4 (ext12 reason). The NEST 3.10 and NESTML trials were run outside the notebook and are not shown.
- Problem 5 (bin edges: markdown corrected, edge weights and half-bin offset in cell 57).
- Problem 7 (baselines now burst-free, cell 21).
- Problem 11 (spans and windows printed beside their source, cell 8).
- Problem 12 (ext9 second eigenvector).
- All of section C: repository inputs printed, S5 shown absent from the 3C files by the 40 s test, the requested s4, ext3 and S2-window outputs added.

Problems 6, 8, 9 and 13 are claims-file questions now put to a reader. Problems 10 and 14 are stated in the notes.

What remains that bears on a conclusion:

- **a. table2-phase-locking-counts.** The criterion keeps spikes while the envelope exceeds "the RMS of the whole series". `hippo.phase_lock_unit` uses the RMS over the analysed windows only, which for recordings 1 and 3 means the seizure windows (`hippo.py:453-454`). Notebook cell 9 says this, but the record does not list it as a deviation. S1 misses by 3 units (60 against at least 63), so the outcome could turn on it. The run needed is the envelope selection with the RMS taken over the whole recording.
- **b. fig2b.** "Reproduced" rests on circular reading (b), as set out in section 1.

### 4. Critical findings

No finding is rated `critical`. Severities in the record: findings 1, 2, 3 and 8 are major; 4, 5 and 6 are minor; 7 is none; 9 to 14 are about the paper and carry no severity.

I would re-rate one:

- **Finding 8 (sub-3C-1 to sub-3C-4 may be copies of one recording).** Spike nb cell 5 shows what it states:
  - The 6 pairs among these files have 78 to 82% identical samples and correlations of sample-to-sample changes of 0.86 to 0.90.
  - The 24 other same-length pairs of a slice have 4 to 8% identical samples and correlations of -0.013 to 0.011.

  I would rate it **critical**. If confirmed, this is one recording deposited as several files, and nothing in the files shows it. A user treating these as four recordings would count one recording four times.

  The evidence covers 1 s and 64 channels only. A comparison over the full 40 s and all channels should be run to settle it. If the files turn out to share a common artifact rather than being copies, major would fit. No analysis in this attempt uses these files.

## End of run

15 turns, 3 minutes, $1.82 at API prices, result: success.
