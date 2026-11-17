# robotka-2023 · verifier-2 · run 43675070340

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 332
drwxr-xr-x 6 runner runner    4096 Nov 15 04:50 .
drwxr-xr-x 8 runner runner    4096 Nov 15 04:50 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 15 04:50 .claude
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.development
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.local
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.production
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.test
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .env.test.local
drwx------ 2 runner runner    4096 Nov 15 04:50 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .github
-rw-r--r-- 1 runner runner       0 Nov 15 04:50 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 15 04:03 .mcp.json
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat robotka-2023-01.yaml
```

```
<persisted-output>
Output too large (44.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/bae7fea2-7fbc-4279-9221-5deb67dc221c/tool-results/behjnxyh9.txt

Preview (first 2KB):
# Robotka et al. (2023) from CRCNS aa-5

Tests the findings of [Robotka et al. (2023)](https://doi.org/10.1016/j.celrep.2023.112034) that can
be tested on [CRCNS aa-5](https://doi.org/10.6080/K0TT4P5Q), which holds the spike-sorted units of
four freely behaving zebra finches presented with 110 vocalizations of the 10 call types of the
repertoire, with songs and filtered songs.

| Claim | Outcome |
|---|---|
| The dataset holds the 4 birds and the 110 stimuli of the paper | Reproduced |
| The paper's 100 good units are in the dataset (link check) | Partially reproduced (91 of 100) |
| 292 of 730 units were auditory | Reproduced |
| 46 of the auditory units were inhibited | Reproduced |
| Mean unit SNR 7.42 (Table 1) | Reproduced |
| The first five PCs explain about 90% of the response variance | Reproduced |
| Distress calls and song drive the strongest responses (Figure 3C) | Reproduced (assumption) |
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 20,200p README.md; echo ======; cat robotka-2023-01.yaml
```

```
<persisted-output>
Output too large (43.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/bae7fea2-7fbc-4279-9221-5deb67dc221c/tool-results/bp0n1l51s.txt

Preview (first 2KB):
| The top 10% of ensembles reach about 50% | Reproduced (assumption) |
| Systematic confusions (Ne-Te, LT-Be, Th-Te, Di-Ag) | Reproduced |
| Per bird and per sex decoding | Blocked: too few good units in one bird |
| PCC rises with the acoustic volume spanned (R2adj 0.1) | Reproduced (assumption) |
| Mean SI is unrelated to PCC | Reproduced |
| Mean Entropy Selectivity is negatively related to PCC | Reproduced |
| PCC falls with neural variability (R2adj 0.1) | Partially reproduced |
| Four regressors explain R2adj 0.22 | Reproduced (assumption) |
| Claims by brain area (three) | Blocked: metadata insufficient |
| Acoustic clustering claims (five) | Blocked: data missing |
| Anesthetized dataset claims (four) | Blocked: CRCNS aa-4 not analysed in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The paper's Methods and its code differ on how the decoder is cross-validated; the ensemble claims are
[... 26 more lines not kept]
```

**Agent**

I'll read the attempt record with the Read tool.

**Agent calls Read**

```json
{
 "file_path": "robotka-2023-01.yaml"
}
```

```
1	schema_version: 3
2	id: robotka-2023-01
3	datasets:
4	- archive: crcns
5	  id: aa-5
6	  version: unversioned
7	  doi: 10.6080/K0TT4P5Q
8	  relation: primary
9	paper: doi:10.1016/j.celrep.2023.112034
10	date: 2026-11-14
11	entry: robotka-2023
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 644 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" robotka-2023.yaml; grep -n "^- id:\|^  id:" robotka-2023.yaml | head -40; grep -c "^- claim:" robotka-2023-01.yaml; grep "^  outcome:" robotka-2023-01.yaml | sort | uniq -c
```

```
30
148:- id: stimulus-set-link
167:- id: paper-good-units-link
180:- id: auditory-units
201:- id: inhibited-units
218:- id: fig3c-peak-call-types
242:- id: fig4a-unit-z-vs-zt
274:- id: good-units-100
304:- id: fig4b-ensemble-20
334:- id: fig4b-top-ensembles
354:- id: fig4b-confusions
369:- id: figs4-per-bird-and-sex
399:- id: figs6-primary-vs-secondary
442:- id: fig5e-volume
469:- id: fig5f-si-unrelated
483:- id: fig5g-entropy-selectivity
499:- id: fig5h-neural-noise
521:- id: fig5-multiple-regression
544:- id: pcs-variance
558:- id: table1-snr
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "robotka-2023.yaml"
}
```

```
1	# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
2	# "Sparse ensemble neural code for a complete vocal repertoire", tested on CRCNS aa-5.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the
6	# paper and its code alone; no data of the dataset were seen.
7	#
8	# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the
9	# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and
10	# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were
11	# not opened; no claim needed a value only printed in a figure.
12	#
13	# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
14	# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It
15	# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes
16	# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb
17	# makes the per-trial table (response strength z, the PCA of trial-averaged KDE responses and the
18	# five PC weights per trial); decodingCallTypesNaiveBayes.ipynb and DataBaseMerge.ipynb run the
19	# single-unit decoder; decodingCallTypesNaiveBayesPart2.ipynb and decoders.py run the ensemble
20	# decoders; plotConfusions.ipynb makes Figure 4; GenerateMLFilters.ipynb makes the MRFs, the LDA,
[... 900 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_robotka_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt | wc -l
```

```
1544 /tmp/claude-1001/nb.txt
80
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 800
}
```

```
File content (25239 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 600
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Robotka et al. (2023) from CRCNS aa-5
4	
5	**Paper.** Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), "Sparse ensemble neural code
6	for a complete vocal repertoire", Cell Reports 42, 112034, doi:10.1016/j.celrep.2023.112034.
7	
8	**Dataset.** CRCNS aa-5, "Simultaneous extracellular recordings of avian auditory neurons in freely
9	behaving zebra finches...", doi:10.6080/K0TT4P5Q, read from the public bucket
10	`crcnsarchive/aa-5/live/`. CRCNS data sets are not versioned: the version is recorded as
11	`unversioned`, the one published version there is, and the MD5 sums of every file read (from the
12	data set's `checksums.md5`) are printed below so that a later change can be detected. The paper
13	cites this DOI and no version; the bucket holds a single copy (`live/`, data descriptor v0.6 of
14	29 Nov 2022), so that is what is pinned.
15	
16	**Claims.** `claims/robotka-2023.yaml`, written from the version of record with its STAR Methods and
17	supplement, and the paper's code (github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
18	f2d2376). Method details the claims file lacks are taken from the paper and that code, cited in the
19	helper `aa5.py` and below.
20	
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 600,
 "limit": 450
}
```

```
600	auditory units with all 110 stimuli: 187 (paper 191); of these with >= 2 trials of every stimulus: 125
601	
602	--OUT--
603	                   reading   n   PCC_Z  PCC_ZT  increase_pct       t  df   p
604	       (a) exemplar, PCC_a 187 10.6770 12.0508       12.8678  7.1738 186 0.0
605	   (b) trial, 1 rep, PCC_b 187 10.7528 12.1666       13.1485  8.9863 186 0.0
606	(b) trial, 100 reps, PCC_b 187 10.7578 12.2675       14.0343 12.3040 186 0.0
607	paper: Z 10.78 (tol 1.078), Z+T 12.3 (tol 1.23), t(190) = 10.06, p < 1e-5
608	(a) exemplar, PCC_a by bird: {'ZF4F': {'Z': 10.85, 'ZT': 13.0}, 'ZF5M': {'Z': 10.65, 'ZT': 12.31}, 'ZF6M': {'Z': 10.34, 'ZT': 11.21}, 'ZF7F': {'Z': 10.69, 'ZT': 11.22}}
609	(b) trial, 1 rep, PCC_b by bird: {'ZF4F': {'Z': 11.04, 'ZT': 13.14}, 'ZF5M': {'Z': 10.67, 'ZT': 11.66}, 'ZF6M': {'Z': 10.38, 'ZT': 11.67}, 'ZF7F': {'Z': 10.72, 'ZT': 11.85}}
610	(b) trial, 100 reps, PCC_b by bird: {'ZF4F': {'Z': 11.04, 'ZT': 13.28}, 'ZF5M': {'Z': 10.66, 'ZT': 11.9}, 'ZF6M': {'Z': 10.43, 'ZT': 11.53}, 'ZF7F': {'Z': 10.72, 'ZT': 11.91}}
611	
612	
613	######## CELL 34 [code]
614	# Variant: the Methods' unit rule, all 110 stimuli with at least 2 trials of each. Each unit is decoded alone,
615	# so these are the same decodings restricted to those units.
616	full2 = [j for j, x in enumerate(full) if (db["feat"][x][1] >= 2).all()]
617	rows = []
618	for name, (cv, nperm, m) in readings.items():
619	    z, zt = single[(name, "Z")][m][full2], single[(name, "ZT")][m][full2]
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1049,
 "limit": 500
}
```

```
1049	(b) trial, 1 rep, PCC_b the paper's 91 listed good units held by the dataset
1050	
1051	--OUT--
1052	        ns    n_ens       mean         sd  pairs_top2
1053	ZF4F  34.0  10000.0  36.962164  12.646042         3.0
1054	ZF5M  19.0   3876.0  35.918356  14.222377         4.0
1055	ZF6M  16.0     16.0  22.186964  13.797258         3.0
1056	ZF7F  22.0  10000.0  40.209232   9.556780         3.0
1057	  female 37.89, male 32.00, difference 5.89; t(2) = 0.451, p = 0.696
1058	
1059	
1060	######## CELL 54 [markdown]
1061	**Result: blocked (other: too few units under the claim's own rule).** Ensembles of 15 with the
1062	corrected SD need at least 16 good units in each bird. ZF6M has 10 good units under the code's reading
1063	(9 under the Methods', where ZF7F also has 14), so the paper's test cannot be run on this attempt's
1064	good units. In the birds with more than 15, mean PCC Z+T at 15 units is 37.9% (ZF4F), 37.4% (ZF5M) and
1065	41.0% (ZF7F) under the code's reading, and 3, 3 and 4 of the four Figure 4B error pairs are among the
1066	two largest entries of their rows. As a variant, on the paper's 91 listed good units the dataset holds
1067	(ZF4F 34, ZF5M 19, ZF6M 16, ZF7F 22), the test runs: female minus male 5.89 points, t(2) = 0.451, p =
1068	0.696 (code reading), and 4.22, t(2) = 0.295, p = 0.796 (Methods' reading), so no sex difference, with
[... 477 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B2 -A4 "KDE_BW\|RateThreshold\|bandwidth" paper/aa-5.data-description.txt | head -60; grep -n "KDE_BW\|RateThreshold\|rate threshold" aa5.py | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "def " aa5.py; sed -n "$(grep -n 'def entropy_selectivity' aa5.py | cut -d: -f1),+22p" aa5.py; sed -n "$(grep -n 'def run_clustering' aa5.py | cut -d: -f1),+45p" aa5.py
```

```
66:def list_files():
83:def checksums():
91:def _unpickle(fobj):
97:def _reduce_unit(info, dfabs, dfrel, member):
129:def read_site(key, max_units=None):
163:def read_all(keys, workers=4, max_units=None, log=print):
188:def spike_diff(spike_times):
194:def unit_table(units):
223:def voc_rows(u):
227:def trial_table(u):
242:def zct_unit(u, trials):
260:def selectivity_index(z):
266:def kde_matrix(u):
278:def kde_check(r, sigmas=(0.01, 0.02, 0.03, 0.05)):
294:def trial_pcs(u, pca):
320:def unit_features(trials, T, stims):
335:def _gnb_posterior(Xtr, ytr, Xte, nc):
352:def _rows(F, C, rng, skip=None):
371:def decode(F, C, y, nc, rng, code="ZT", cv="trial", nperm=1):
419:def pcc_code(conf, ntest):
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 633,688p aa5.py
```

```
def ensemble_responses(db, uids):
    """Stimulus x (units x 6) matrix of the trial-averaged Z and T1..T5 of an ensemble (C12)."""
    F, C = stack(db, uids)
    W = np.nanmean(F, axis=2)                       # U, S, 6
    return np.transpose(W, (1, 0, 2)).reshape(F.shape[1], -1)


def ari(a, b):
    """Adjusted Rand index of two labelings (Hubert and Arabie), equal to sklearn's
    adjusted_rand_score, written with a contingency table for speed."""
    _, ai = np.unique(a, return_inverse=True)
    _, bi = np.unique(b, return_inverse=True)
    M = np.zeros((ai.max() + 1, bi.max() + 1))
    np.add.at(M, (ai, bi), 1)
    c2 = lambda x: (x * (x - 1) / 2).sum()
    sij, sa, sb, n2 = c2(M), c2(M.sum(axis=1)), c2(M.sum(axis=0)), c2(np.array([len(a)], float))
    exp = sa * sb / n2
    den = (sa + sb) / 2 - exp
    return 1.0 if den == 0 else (sij - exp) / den

[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -B2 "assumed: true" robotka-2023-01.yaml | grep claim
```

```
- claim: fig3c-peak-call-types
- claim: fig4b-ensemble-20
- claim: fig4b-top-ensembles
- claim: fig5e-volume
- claim: fig5-multiple-regression
```

**Agent**

**Verifier report, round 2: Robotka et al. 2023 on CRCNS aa-5 (attempt robotka-2023-01)**

The claims file has 30 claims, and the attempt record has 30 outcomes: 14 reproduced, 2 partially reproduced, 1 not reproduced and 13 blocked. Five outcomes are marked `assumed: true`: fig3c-peak-call-types, fig4b-ensemble-20, fig4b-top-ensembles, fig5e-volume and fig5-multiple-regression.

### 1. Outcomes and assumptions

I agree with all 30 stated outcomes. Three of them changed since round 1:

- **good-units-100 (not_reproduced).** I now agree, and withdraw my round-1 partially_reproduced. The criterion takes the count from one run and has no partial outcome when the total is outside tolerance. That run gives 89 under the code reading and 77 under the Methods reading (cell 37), both outside 90–110. The outcome depends on the seed: 8 of the 10 other seeds land in tolerance. ZF6M has 8–14 good units in every run, never within 16 ± 1.6.
- **fig5e-volume and fig5-multiple-regression (reproduced, assumed).** Both now match my round-1 outcome.

The blocked outcomes and their `blocked_by` reasons are right:

- figs4 is blocked as other. ZF6M has 10 good units, below the 16 the test needs.
- The area claims are blocked as metadata_insufficient.
- The acoustic claims are blocked as data_missing.
- The aa-4 claims are blocked as other.

The five assumptions are stated, with the other readings shown and the reason given:

- **fig3c, the code's zCT.** Reasonable: it is what Figure 3C plots. Under the Methods' zCT, So ranks first (cell 30), so the claim would not be reproduced.
- **fig4b-ensemble-20 and fig4b-top-ensembles, the code's cross-validation.** Stated and defensible: the paper's printed values match the code's scheme and not the Methods'. The record now says plainly that this scheme credits responses specific to one exemplar: 78.2% against 9.8% on synthetic data (cell 43). Under the Methods' scheme the claims are partially reproduced (32.0 / 24.1) and not reproduced (33.96).
- **fig5e, the code's sound window and eigh axes.** Stated, and fragile. R2adj is in tolerance only for the code window with eigh axes (0.0938, cell 62). The eigh axes are the smallest eigenvalues of a non-symmetric matrix. With the Methods' window and the largest-eigenvalue axes R2adj is 0.120, and the outcome would be partially_reproduced.
- **fig5-multiple-regression, the eigh axes.** Stated. With the largest-eigenvalue axes R2adj is 0.2515 or 0.2481 (cell 74), just outside tolerance.

fig5g needs no assumption, because the Methods' ES (reading b) holds under both cross-validations. But that outcome rests on a claims-file reading I still question (point 3 below).

### 2. Conclusions, Summary, README and record notes against the outputs

Almost every number checks against the printed outputs: cells 8–78, the Summary (cell 79), the README table and the record notes. The exceptions:

- **KDE_BW finding** (record `metadata_error` finding; Summary, cell 79; pcs-variance notes). "its values range from 0.2 to 10, which can only be milliseconds." Cell 5 prints only the first five values, [0.2, 3.0, 5.0, 5.2, 5.4], so the range 0.2–10 is not printed (10.0 appears only in the descriptor's example). Nothing printed shows the values must be milliseconds. The descriptor says this convolution gives a "coarse" rate used to cut out motion-artefact epochs, for which bandwidths of 0.2–10 s are plausible. This finding is not supported.
- **README.** "the whole notebook ran in 47 minutes". Cell 74 prints a total run time of 37.7 min and cell 77 adds 3.7 min of clustering, about 41.5 min in all.
- **fig5-multiple-regression notes.** "The Methods' SI changes R2adj by less than 0.002." This holds under the code's cross-validation (at most 0.0009, cell 74). Under the Methods' cross-validation the change reaches 0.0025 (0.4841 against 0.4866).
- **fig4b-top-ensembles.** The criterion takes the best ensemble "among the Figure 4B ensembles of 20". The best is now taken from the 1,800 Figure 5 ensembles (cell 59). The notes say so, but it is not listed as a deviation. It does not change the verdict: 68.4 ≥ 55.
- **Summary, fig6c row.** It reports only the code reading's units (median 10, outside 9 ± 0.9). The Methods reading's units, the main reading under the claims file, give mean 10.16 and median 9, both within tolerance (cell 77). The record notes give both.
- **Cosmetic.** Cells 31, 39, 44, 47, 50, 54, 63, 66, 69, 72 and 75 end with a stray closing `**`.

**Round-1 reasons in the record.** They state my round-1 reasons accurately and in my words, nearly verbatim from my table, with the matching problem points attached to each claim. The `agrees: false` entries (good-units-100, fig5e, fig5-multiple-regression) and the outcome I gave for each are recorded correctly.

**Claims-file points (reported, not corrected):**

- **C11 ES reading (b).** The Methods' ES formula gives negative values here (−0.18 to −0.07), against the Figure 5G legend's range of 0 to 1. The claims file used the same range argument to rule out C2(a) for SI. ES (b) also falls as single-unit PCC rises, so a negative slope is close to built in. The author has passed this to a reader.
- **C12.** The claims file says the code cuts the tree between the smallest and largest linkage distance. The author reports that the code takes the minimum and maximum over the whole linkage matrix, including its index and count columns. I cannot check this without the code. If the author is right, the claims file misreads the code. One consequence: the helper's thresholds can never yield 1 cluster (minimum 2–3, cell 77), while the paper's range starts at 1. The claim is blocked, so no outcome changes.

### 3. Round-1 points

**Resolved:**

- **B1 (cross-validation leakage).** Stated as an assumption, shown on synthetic data, and put to the authors as a question.
- **B2 (good-unit count).** Per-bird counts are now printed for every seed and for the listed units.
- **B4 (best ensemble biased upward).** Now taken from 100-repetition decodings.
- **B5 (figs4 variant).** The variant on the paper's listed units has been run (p = 0.696 and 0.796), and the message has been corrected.
- **B6 (fig6c call-type half).** Now computed.
- **B7 (fig5 code variants).** Now marked as assumptions.
- **B8 (Methods unit rule).** The 125-unit variant is in tolerance.
- **B9 (KDE kernel).** The stored KDE matches a 30 ms kernel (107 of 114 rows above r = 0.99). The test for spikeless stimuli is fixed, and the PCA is unchanged.
- **B10 (MRF scaling).** The code's `stdz = np.std(allz)` is printed, though the print does not show which units `allz` covers.
- **B11 (cell 11).** Fixed.
- **C items.** The code lines for ES normalisation, eigh, the PCC > 30 filter and n0 = n1 = 2 are now printed. The record states that no deposit exists for the vocalization database.

**Still open, bearing on a conclusion:**

- **B3 / C11, fig5g.** The outcome holds only under the Methods' ES (b). That reading's support from the paper is doubtful, and under the code's ES (a) with the code's cross-validation the slope is +18.9, p = 0.79. A reader's answer could reverse this outcome.
- **fig5e and fig5-multiple-regression.** Both rest on the code's eigh axes, and fig5e also on the code's sound window. Without them the outcomes are partially_reproduced (0.120; 0.248–0.252).
- **good-units-100.** The outcome follows the criterion but depends on the seed: 8 of 10 other seeds fall in tolerance.

## End of run

16 turns, 3 minutes, $1.62 at API prices, result: success.
