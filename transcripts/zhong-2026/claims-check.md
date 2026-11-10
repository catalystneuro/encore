# zhong-2026 · claims-check · run 42749279538

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i zhong; cat claims/zhong-2026.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 103,200p docs/protocol.md; ls paper/; python tools/claims_check.py claims/zhong-2026.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0e4ef909-4c77-47f2-8f2e-79ef01b476a7/tool-results/bzlaag0gu.txt"
}
```

```
1	70357 paper/10.7554-elife.109538.txt
2	DOI: 10.7554/elife.109538
3	Version: version of record
4	Source: crossref+publisher_html (find_reuse cache)
5	Stored: 2026-11-09
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	Synaptic Theory of Chunking in Working Memory
9	
10	Working memory often appears to exceed its basic span by organizing items into compact representations called chunks. Chunking can be learned over time for familiar inputs; however, it can also arise spontaneously for novel stimuli. Such on-the-fly structuring is crucial for cognition, yet the underlying neural mechanism remains unclear. Here we introduce a synaptic theory of chunking, in which short-term synaptic plasticity enables the formation of chunk representations in working memory. We show that a specialized population of “chunking neurons” selectively controls groups of stimulus-responsive neurons, akin to gating. As a result, the network maintains and retrieves the stimuli in chunks, thereby exceeding the basic capacity. Moreover, we show that our model can dynamically construct hierarchical representations within working memory through hierarchical chunking. A consequence of this proposed mechanism is a new limit on the number of items that can be stored and subsequently retrieved from working memory, depending only on the basic working memory capacity when chunking is not invoked. Predictions from our model were confirmed by analyzing single-unit responses in epileptic patients and memory experiments with verbal material. Our work provides a novel conceptual and analytical framework for understanding how the brain organizes information in real time.
11	
12	10.1126/science.1736359
13	
14	10.1016/j.conb.2013.10.008
15	
16	10.1016/j.neuron.2018.09.023
17	
18	10.1177/0963721409359277
19	
20	10.3758/BF03193078
[... 472 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rln "simulation" claims/ | head; grep -rn "^  data:" claims/*.yaml | awk '{print $3}' | sort | uniq -c; grep -n "data\b\|elsewhere\|simulation" docs/claims-schema* docs/*.md 2>/dev/null | grep -i "simul\|derivation\|theor" | head
```

```
claims/li-2016/crcns-alm-3.yaml
claims/li-2016/000011.yaml
claims/qu-2025.yaml
claims/kaku-2025.yaml
claims/wang-2014.yaml
claims/najafi-2020.yaml
claims/silkuniene-2025/001276.yaml
claims/silkuniene-2025/001047.yaml
claims/silkuniene-2025/001277.yaml
claims/mountoufaris-2024.yaml
    182 dataset
    436 elsewhere
    233 with_inputs
    334 with_labels
```

**Agent calls Bash**

```bash
cd  grep -rn -B2 -A3 "data: elsewhere" claims/qu-2025.yaml claims/wang-2014.yaml | grep -i -A4 -B4 "simul\|model" | head -40; grep -n "elsewhere" docs/protocol.md | head
```

```
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
161:     recordings of its own, or on other data, are `data: elsewhere` when they
233:4. Decide what comes from outside the dataset. Data from elsewhere may be
242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
267:   - `elsewhere` is for a claim whose data the dataset does not hold at
287:     `data: elsewhere` instead (step 4).
```

**Agent calls Bash**

```bash
cd  sed -n 228,300p docs/protocol.md
```

```
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
[... 53 more lines not kept]
```

**Agent**

The checker passes. I found a few problems; making the edits now.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/zhong-2026.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a
    s=s.replace(a,b)
rep("""    0.45 s; chunking clusters 0.01 s long at 0.2 s intervals; background switching between 10
    and -10 Hz for 0.8 s during retrieval), with Eq. (8) extended so that level-k chunking
    clusters inhibit all lower-level clusters presented before them (Methods A).""",
"""    0.45 s; chunking clusters 0.01 s long at 0.2 s intervals; background switching between 10
    and -10 Hz for 0.8 s during retrieval), with Eq. (8) extended so that level-k chunking
    clusters inhibit all lower-level clusters presented before them (Methods A). Methods C
    writes "k = 2, 3 level chunking clusters", but the Results put chunking clusters at
    k = 1, 2 and stimulus clusters at k = 3, so the 0.01 s timing is read as that of the
    chunking clusters. Tolerances are 0, as counts.""")
rep("""    Fig. S3). "Most" is read as more than half of the 14 subjects. Reproduced when more than
    half show both a dip and a ramp under a reading; partially reproduced when they do but
    P64CS shows a ramp or TWH120 shows a dip under every reading. The count, and the subjects
    sorted by dip time as in Fig. 3(b), are reported.""",
"""    Fig. S3). "Most" is read as more than half of the 14 subjects (8 or more). Reproduced
    when, under one reading, 8 or more subjects show both a dip and a ramp, P64CS shows no
    ramp and TWH120 shows no dip; partially reproduced when 8 or more show both under a
    reading but under no reading do both named exceptions hold. Not reproduced when fewer than
    8 show both under every reading. The count, and the subjects sorted by dip time as in
    Fig. 3(b), are reported.""")
rep("""  criterion: Not testable on DANDI:000207. On the data of [42], f against log2 L per order n,
    one common slope with a separate intercept per n.""",
"""  criterion: Not testable on DANDI:000207. On the data of [42], f against log2 L per order n
    and for natural text (the black curve of Fig. 4a), one common slope with a separate
    intercept per curve.""")
rep("""  where: Miller and Selfridge 1950, Am J Psychol 63:176 (published recall table); not in any
    archive
  criterion: Not testable on DANDI:000207. On""","""  where: Miller and Selfridge 1950, Am J Psychol 63:176, doi:10.2307/1418920 (published
    recall table); not in any data archive
  criterion: Not testable on DANDI:000207. On""")
rep("""  where: Miller and Selfridge 1950, Am J Psychol 63:176 (published recall table); not in any
    archive
  depends_on:""","""  where: Miller and Selfridge 1950, Am J Psychol 63:176, doi:10.2307/1418920 (published
    recall table); not in any data archive
  depends_on:""")
rep("""  where: Maher and Skovengaard 1988, Scand J Psychol 29:194; Sharma and Sen 1977, Indian J
    Psychol (published recall tables); not in any archive""",
"""  where: Maher and Skovengaard 1988, Scand J Psychol 29:194,
    doi:10.1111/j.1467-9450.1988.tb00791.x; Sharma and Sen 1977, Indian J Psychol, no DOI or
    volume given in the paper (published recall tables); not in any data archive""")
rep("""  criterion: Not testable on DANDI:000207. The analysis of fig4a-universal-slope and
    fig4b-plateau-near-eight applied to each replication. "Within the region predicted" is
    open; (a) the plateau within 10% of 8, (b) the plateau at or below 8.""",
"""  criterion: Not testable on DANDI:000207. The analysis of fig4a-universal-slope and
    fig4b-plateau-near-eight applied to each replication. "Within the region predicted" is
    open; (a) the plateau within 10% of 8, (b) the plateau at or below 8, M* being stated as
    a limit beyond which perfect retrieval is impossible. Reproduced when in each replication
    Lc rises with n and then plateaus (the "similar trends") and, under one reading, the
    plateau of all three languages is in the region.""")
s=s.rstrip('\n')+"""
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3b-individual-subjects, criterion rewritten so the outcomes do not overlap. The old
    wording made a result with a majority and a failed exception both reproduced and partially
    reproduced; the statement includes the two exceptions of the Fig. S3 legend, so reproduced
    now needs them, and "more than half of 14" is made explicit as 8 or more.
  - fig2b-hierarchical-retrieval, criterion notes that Methods C names the 0.01 s clusters
    "k = 2, 3 level chunking clusters" while the Results put chunking clusters at k = 1, 2, and
    gives the reason for the 0 tolerances.
  - fig4a-universal-slope, criterion adds the natural-text curve, which the Fig. 4a legend
    includes ("Black color represents natural text").
  - fig4a-universal-slope, fig4b-plateau-near-eight, fig4b-three-languages, `where` now give
    the DOIs the paper's reference list holds for refs. [42] and [46].
  - fig4b-three-languages, criterion states when the claim is reproduced, including the
    "similar trends" of the Results, and why reading (b) is allowed (Eq. 1 as a limit).
  - Open, the Hindi replication (ref. [47]) has no DOI or volume in the paper, so the author
    may not be able to pin it; fig4b-three-languages may then be blocked on that part.
  - Open, fig3a-dip-after-boundary and fig3c-onset-control rest on measures the paper does not
    give (bins, smoothing, window, z-score reference, how a dip, a ramp and a peak are judged,
    how boundary and onset neurons are selected); the criteria name them as open and fix
    readings, which the outcome will rest on as assumptions.
  - Open, whether "all trials" in the Fig. 3 legend includes clips of [41] without a cut is
    not said; the text ("each consisting of two episodes separated by a cut") supports cut
    clips only, the reading the criterion takes.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/zhong-2026.yaml paper/10.7554-elife.109538.txt; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked `claims/zhong-2026.yaml` against the paper and made six fixes. The file is ready for an attempt.

**Checker result** (the same before and after my edits): `claims/zhong-2026.yaml: 12 claims, 12 quotes, 0 statistical values, 0 problems`

**Changes, by claim**
- **fig3b-individual-subjects**: I rewrote the criterion. As written, one result could count as both reproduced and partially reproduced: a majority of subjects showing the pattern, but one of the two named exceptions (P64CS without a ramp, TWH120 without a dip) failing. The statement includes those exceptions, so "reproduced" now requires them. "More than half of 14" is now stated as 8 or more.
- **fig2b-hierarchical-retrieval**: The criterion now notes that Methods C calls the 0.01 s clusters "k = 2, 3 level chunking clusters", while the Results put chunking clusters at k = 1, 2. It also gives the reason for the zero tolerances (they are counts).
- **fig4a-universal-slope**: The criterion now includes the natural-text curve, which the Fig. 4a legend includes.
- **fig4a, fig4b-plateau-near-eight, fig4b-three-languages**: The `where` fields now carry the DOIs from the paper's reference list for refs [42] and [46].
- **fig4b-three-languages**: The criterion now says when the claim counts as reproduced: every language must show the "similar trends", and the plateau must fall in the predicted region. It also explains why "at or below 8" is an allowed reading: the paper calls M* a limit beyond which perfect recall is impossible.

The other claims check out: statements match the paper, sources point at the right place, there are no statistics to record (the paper reports no tests), and every main finding has a claim (Fig. 1D, Eq. 1, Fig. 2B, Fig. S2, the subject exclusion, Fig. 3A–C, Fig. 4A–B).

**What remains open** (recorded under `checks`)
- The Hindi replication (ref. [47]) has no DOI or volume in the paper, so the author may not be able to pin it. That part of fig4b-three-languages could end up blocked.
- The Fig. 3 claims depend on details the paper doesn't give: bins, smoothing, the time window, the z-score reference, how a dip, ramp or peak is judged, and how boundary and onset neurons are selected. The criteria name these as open and fix readings, so the outcomes will rest on assumptions.
- The paper doesn't say whether "all trials" includes clips without a cut. The text supports cut clips only, which is the reading the criterion uses.

The edited file is not committed, as instructed.

## End of run

9 turns, 2 minutes, $0.68 at API prices, result: success.
