# hasnain-2025 · claims-check · run 44973462291

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i hasnain; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/hasnain-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i hasnain; awk '/^## Reader/,/^## Author/' docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/hasnain-2025.yaml paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/hasnain-2025.yaml paper/10.1101-2025.10.17.682917.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/hasnain-2025.yaml"
}
```

```
1	# Claims for Hasnain, Han & Economo (2025), "Mapping neural subspace dynamics onto the structure
2	# of the mouse descending motor system", bioRxiv doi:10.1101/2025.10.17.682917, tested on
3	# DANDI:000363 (Mesoscale Activity Map Dataset), which the paper reuses.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-22,
5	# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
6	#
7	# Text read. The preprint (version 1, posted 2025-10-17), full text from PMC (PMC12632980), in
8	# paper/10.1101-2025.10.17.682917.txt: Abstract, Introduction, Results, Discussion, Methods, the
9	# legends of Extended Data Figures 1 to 3, and the legends of Figures 1 to 4. The paper has no
10	# separate supplement (PMC lists none); the Extended Data legends are in the text. No PDF was
11	# supplied, so no figure was read; every claim rests on the text.
12	#
13	# Code read. github.com/economolab/subspaceID, commit d593949fef8a39fe0a6eb54a21fc05cbca7bae84,
14	# the only code the paper links ("Code for identifying movement-null and movement-potent
15	# subspaces"). It holds orthogonal_subspaces.m (the manopt optimization of the Methods'
16	# objective, each term normalized by the sum of the top-d eigenvalues of its covariance, with a
17	# regularization weight alpha that example.m sets to 0), example.m (z-scores each neuron over all
18	# bins and trials, takes the covariance of stationary and of moving bins, fixes 15 dimensions per
19	# subspace, rng(101)), and a Python port (funcs.py, example.ipynb). It holds none of the paper's
20	# other analyses (session selection, movement masks, dimensionality, variance explained,
[... 488 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.17.682917.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1101-2025.10.17.682917.txt').read(); print(t[54700:80000])"
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (0 problems). Reading the remainder of the text for figure legends before judging the claims.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1101-2025.10.17.682917.txt').read(); i=t.find('Figure 1'); import re
for m in re.finditer(r'Figure [1-4]\b', t): print(m.start(), t[m.start():m.start()+80])
print(len(t))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1101-2025.10.17.682917.txt').read(); print(t[85900:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1101-2025.10.17.682917.txt').read(); i=t.find(' 69. '); print(t[i:i+900])"
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker result: 19 claims, 0 problems. Most claims match the paper. I'm fixing a few sources, notes and statistics fields now.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/hasnain-2025.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""#    the paper's three (sample, delay, response) is open between (E1) a
#    unit selective in either sub-epoch counts for the epoch and (E2) each sub-epoch alone, every
#    one reported.""","""#    the paper's three (sample, delay, response) is open between (E1) a
#    unit selective in either sub-epoch counts for the epoch and (E2) each sub-epoch alone, every
#    one reported. The Figure 1i legend gives "p < 0.05; shuffle test" with no correction; the
#    Methods' Bonferroni threshold, which names Fig. 1i and Fig. 4b, is the main reading, and the
#    uncorrected p < 0.05 is a variant.""")
rep("""#    eigenvalues of the movement-null activity, the effective dimensionality of ref 70 that the
#    Results cite.""","""#    eigenvalues of the movement-null activity, as a stand-in for the effective dimensionality the
#    Results cite to ref 70 (Recanatesi et al. 2022, a scale-dependent measure of dimensionality);
#    the paper does not say which scale or measure it used.""")
rep("""  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2e; Discussion, paragraph 2""",
"""  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2e; Discussion, paragraph 1""")
rep("""  criterion: Not testable on DANDI:000363; the paper's own recordings and videos are not public. The
    s.d. given is the spread over neurons, so 10% of each mean is used as the tolerance.""",
"""  criterion: Not testable on DANDI:000363; the paper's own recordings and videos are not public. The
    s.d. given is the spread over neurons, so 10% of each mean is used as the tolerance. The unit count
    differs between the Results (n = 1954 neurons) and the Figure 3c legend (n = 1945 units).""")
rep("""paired t -test between slope of curves in Extended Data Fig. 3d ; movement onset
  statistics:""","""paired t -test between slope of curves in Extended Data Fig. 3d ; movement onset: 105 ± 36 ms following
    the go cue, mean ± s.d.; n = 27 sessions).'
  statistics:""")
rep("""  quote: L-ETN dynamics changed rapidly at the go cue,""","""  quote: 'L-ETN dynamics changed rapidly at the go cue,""")
rep("""  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is
    found downstream of motor cortex, paragraphs 1 and 3""","""  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is
    found downstream of motor cortex, paragraphs 1 and 4""")
rep("""    p: 7.4e-5
    n: 16 sessions""","""    p: 7.4e-5
    n: not stated for this test; the 16 ALM and medulla sessions of the Results""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-11-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - ed3-letn-fast-switch, quote extended to the end of the sentence so that it holds the movement onset value (105 +- 36 ms, n = 27 sessions) the statement and expected value use.
  - map-session-selection, source corrected from Results paragraphs 1 and 3 to 1 and 4; the 1116 neurons of the bilateral ALM sessions are in the decoding paragraph, which this file elsewhere calls paragraph 4.
  - fig2e-potent-only-units, source corrected to Discussion paragraph 1; the sentence on a subpopulation larger than expected by chance follows the Discussion's opening sentence with no break in topic.
  - fig3c-network-beats-linear, criterion notes that the Figure 3c legend gives n = 1945 units against 1954 neurons in the Results.
  - fig4e-medulla-null-lower-dimension, statistics n changed to say the paper gives no n for this test; 16 sessions was an inference from the Results.
  - Header M7, the Figure 1i legend's uncorrected p < 0.05 shuffle test added as a variant to the Methods' Bonferroni threshold.
  - Header M9, ref 70 identified (Recanatesi et al. 2022, a scale-dependent dimensionality measure); the participation ratio of reading N2 is marked as a stand-in, since the paper does not name the measure or scale.
  - Open, not settled. The ALM and medulla session count (16 in the Results and Figure 4, 11 from 7 mice in the Methods) and the bilateral ALM unit count (1116 in the Results, 2016 in the Methods) conflict in the paper; both readings stay in the criteria.
  - Open, not settled. The variance explained reading V2 (normalization by total variance) departs from the Methods' formula; it is kept because the Results describe 78% of the variance in single-trial activity and the values add up, but the formula reading V1 is the Methods' own.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/hasnain-2025.yaml paper/10.1101-2025.10.17.682917.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -c "one reported\.$" claims/hasnain-2025.yaml; grep -n "checks:" claims/hasnain-2025.yaml; git diff --stat
```

```
1
```

**Agent**

The first anchor didn't match, so nothing was written. Re-running with that anchor fixed.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/hasnain-2025.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""sub-epoch alone, every
#    one reported.""","""sub-epoch alone, every
#    one reported. The Figure 1i legend gives "p < 0.05; shuffle test" with no correction; the
#    Methods' Bonferroni threshold, which names Fig. 1i and Fig. 4b, is the main reading, and the
#    uncorrected p < 0.05 is a variant.""")
rep("""#    eigenvalues of the movement-null activity, the effective dimensionality of ref 70 that the
#    Results cite.""","""#    eigenvalues of the movement-null activity, as a stand-in for the effective dimensionality the
#    Results cite to ref 70 (Recanatesi et al. 2022, a scale-dependent measure of dimensionality);
#    the paper does not say which scale or measure it used.""")
rep("""  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2e; Discussion, paragraph 2""",
"""  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2e; Discussion, paragraph 1""")
rep("""  criterion: Not testable on DANDI:000363; the paper's own recordings and videos are not public. The
    s.d. given is the spread over neurons, so 10% of each mean is used as the tolerance.""",
"""  criterion: Not testable on DANDI:000363; the paper's own recordings and videos are not public. The
    s.d. given is the spread over neurons, so 10% of each mean is used as the tolerance. The unit count
    differs between the Results (n = 1954 neurons) and the Figure 3c legend (n = 1945 units).""")
rep("""paired t -test between slope of curves in Extended Data Fig. 3d ; movement onset
  statistics:""","""paired t -test between slope of curves in Extended Data Fig. 3d ; movement onset: 105 ± 36 ms following
    the go cue, mean ± s.d.; n = 27 sessions).'
  statistics:""")
rep("""  quote: L-ETN dynamics changed rapidly at the go cue,""","""  quote: 'L-ETN dynamics changed rapidly at the go cue,""")
rep("""  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is
    found downstream of motor cortex, paragraphs 1 and 3""","""  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is
    found downstream of motor cortex, paragraphs 1 and 4""")
rep("""    p: 7.4e-5
    n: 16 sessions""","""    p: 7.4e-5
    n: not stated for this test; the 16 ALM and medulla sessions of the Results""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-11-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - ed3-letn-fast-switch, quote extended to the end of the sentence so that it holds the movement onset value (105 +- 36 ms, n = 27 sessions) the statement and expected value use.
  - map-session-selection, source corrected from Results paragraphs 1 and 3 to 1 and 4; the 1116 neurons of the bilateral ALM sessions are in the decoding paragraph, which this file elsewhere calls paragraph 4.
  - fig2e-potent-only-units, source corrected to Discussion paragraph 1; the sentence on a subpopulation larger than expected by chance follows the Discussion's opening sentence with no break in topic.
  - fig3c-network-beats-linear, criterion notes that the Figure 3c legend gives n = 1945 units against 1954 neurons in the Results.
  - fig4e-medulla-null-lower-dimension, statistics n changed to say the paper gives no n for this test; 16 sessions was an inference from the Results.
  - Header M7, the Figure 1i legend's uncorrected p < 0.05 shuffle test added as a variant to the Methods' Bonferroni threshold.
  - Header M9, ref 70 identified (Recanatesi et al. 2022, a scale-dependent dimensionality measure); the participation ratio of reading N2 is marked as a stand-in, since the paper does not name the measure or scale.
  - Open, not settled. The ALM and medulla session count (16 in the Results and Figure 4, 11 from 7 mice in the Methods) and the bilateral ALM unit count (1116 in the Results, 2016 in the Methods) conflict in the paper; both readings stay in the criteria.
  - Open, not settled. The variance explained reading V2 (normalization by total variance) departs from the Methods' formula; it is kept because the Results describe 78% of the variance in single-trial activity and the values add up, but the formula reading V1 is the Methods' own.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/hasnain-2025.yaml paper/10.1101-2025.10.17.682917.txt; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the file; it is ready for an attempt. I made seven corrections and left two problems open. Nothing is committed or pushed.

**Checker result:** `claims/hasnain-2025.yaml: 19 claims, 19 quotes, 9 statistical values, 0 problems`. The result was the same before and after my edits.

**Changes, by claim:**
- **ed3-letn-fast-switch:** the quote stopped at "movement onset", before the 105 ± 36 ms value (n = 27 sessions) that the statement and expected value use. I extended it to the end of the sentence.
- **map-session-selection:** the source said Results paragraphs 1 and 3, but the 1116 bilateral ALM neurons are in paragraph 4, the decoding paragraph. I changed it to paragraphs 1 and 4.
- **fig2e-potent-only-units:** I moved the source from Discussion paragraph 2 to paragraph 1. The text has no paragraph breaks, so this rests on the sentence following the Discussion's opening with no change of topic.
- **fig3c-network-beats-linear:** the criterion now notes that the Results give 1954 neurons and the Figure 3c legend gives 1945 units.
- **fig4e-medulla-null-lower-dimension:** the statistics recorded n = 16 sessions, but the paper gives no n for this test. The field now says so.
- **Header M7 (selectivity):** the Figure 1i legend uses an uncorrected p < 0.05 shuffle test. I added it as a variant; the Methods' Bonferroni threshold stays the main reading.
- **Header M9 (dimensionality):** ref 70 is Recanatesi et al. 2022, a scale-dependent measure of dimensionality. Reading N2 (participation ratio) is now marked as a stand-in, because the paper does not name the measure or the scale.

Everything else holds up against the paper: statements, sources, statistics (results only, no thresholds used to count units), expected values and tolerances. The criteria's methods come from the Methods, the legends, or the subspaceID code. Every main finding has a claim, and all of them come from this paper. The claims on the paper's own recordings cannot be tested, because those data are not public.

**Still open (recorded under `checks`):**
- The paper contradicts itself on the ALM and medulla sessions: 16 in the Results and Figure 4, 11 sessions from 7 mice in the Methods. It also gives 1116 bilateral ALM units in the Results and 2016 in the Methods. Both readings stay in the criteria.
- Variance-explained reading V2 normalizes by total variance, which departs from the Methods' formula. I kept it because the Results describe "78% of the variance" and the values add up. V1 is the formula's own reading.

## End of run

14 turns, 2 minutes, $0.92 at API prices, result: success.
