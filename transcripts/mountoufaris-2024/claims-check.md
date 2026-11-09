# 001131 · claims-check · run 39835872250

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001131/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; cat claims/001131/*.yaml; python tools/claims_check.py claims/001131/10.1016-j.cell.2024.08.015.yaml paper/10.1016-j.cell.2024.08.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; python tools/claims_check.py claims/001131/10.1016-j.cell.2024.08.015.yaml paper/10.1016-j.cell.2024.08.015.txt; wc -l claims/001131/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001131/10.1016-j.cell.2024.08.015.yaml"
}
```

```
1	# Claims for Mountoufaris, Nair, Yang, Kim, Vinograd, Kim, Linderman & Anderson (2024), Cell 187,
2	# 5998-6015, on dandiset 001131.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md version pilot-10.
5	#
6	# Source: the accepted author manuscript in PubMed Central (PMC11490375, NIHMS2020595), full text
7	# as served by PMC: Results, Discussion, STAR Methods, main and supplementary figure legends. The
8	# supplement (NIHMS2020595-supplement-1.pdf) holds the images of Figures S1 to S7 only; their
9	# legends are in the main text. The version of record was not read. The main figures are not in
10	# the files read, so the star level of each main-figure panel could not be read; where the text
11	# says "significantly" and the panel's stars are not readable, the statistics record p < 0.05,
12	# the paper's lowest level ("* P < 0.05", STAR Methods, Statistical analysis). Stars read from the
13	# supplement images are recorded as read.
14	#
15	# Code read. The paper links https://github.com/DJALab/VMHvl_MPOA_dynamics (commit ed83c41,
16	# 2023-11-28) and https://github.com/lindermanlab/ssm (commit eb6c8aa, 2025-05-09). The DJALab
17	# repository holds one notebook that draws flow fields and dynamic velocity landscapes for two
18	# synthetic 2-dimensional linear systems (from Nair et al. 2023, Fig 3); it holds no code for this
19	# paper's data. Its README points to ssm's notebooks/4-Recurrent-SLDS.ipynb for fitting, which
20	# fits an rSLDS with ssm.SLDS(transitions="recurrent_only", dynamics="diagonal_gaussian",
[... 891 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2024.08.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
t=open('paper/10.1016-j.cell.2024.08.015.txt').read()
print(t[48900:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/c2cb7eb9-9f67-4567-9443-2e2c757d8700/tool-results/bie7u85cs.txt"
}
```

```
1	131 ™ ) were transfected with EFS-Cas9-Blast plasmid (addgene # 52962) and selected for four days with blasticidin antibiotic. Individual gRNAs were cloned in ph7SK-gRNA (addgene # 53189) or phH1-gRNA (addgene # 53186) or pmU6-gRNA (addgene # 53187) or phU6-gRNA (addgene # 53188) plasmids, 0.5–1 ug transfected in Neuro2a-Cas9 cells and after three days genomic DNA was isolated. We used T7 endonuclease assay for testing the efficiency of each gRNAs to generate edits, similar to what has been described in https://www.neb.com/protocols/2014/08/11/determining-genome-targeting-efficiency-using-t7-endonuclease-i . In addition, Sanger traces were generated with target-specific PCR and analyzed with the Tracking of INDELs by Decomposition (TIDE) web tool http://tide.nki.nl (data not shown) . Screening for aggressor male and resident intruder assay All experimental male mice (“residents”) were individually housed for two weeks and received sexual experience (for at least one week). Previously it has been reported that ~20–25% of inbreeding C57BL/6N male animals fail to display territorial aggression against conspecific male intruders during the RI assay 93 . We pre-screened males for baseline aggression using resident-intruder testing sessions to identify and exclude no aggressors from our analysis. Animals that attacked two constitutively presented intruders were termed aggressors and added to the pool of animals for CRISRP/Cas9-based gene editing surgeries. On the experimental day, the preselected male residents were transported in their home cage to a novel behavioral testing room (under infrared light), where they acclimated for 5–10 min. An unfamiliar group housed BALB/c mouse (“intruder”) was then placed in the resident’s home cage, and residents were allowed to interact with it for period of time. Acute brain slices preparation Briefly, male adult mice were anesthetized with isoflurane and transcardially perfused with cold NMDG-ACSF (adjusted to pH 7.3–7.4) containi
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import re
t=open('paper/10.1016-j.cell.2024.08.015.txt').read()
for m in re.finditer(r'Figure [1-7]\.? ', t): print(m.start(), t[m.start():m.start()+80].replace('\n',' '))
" | awk '\$1>100000'; python -c "
t=open('paper/10.1016-j.cell.2024.08.015.txt').read(); print(len(t))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
t=open('paper/10.1016-j.cell.2024.08.015.txt').read()
i=t.find('Figure 1.',100000); print(i)
import re
j=[m.start() for m in re.finditer('Figure [1-7][.] ', t) if m.start()>100000]; print(j)
print(t[min(j) if j else 120000:])" > $TMPDIR/tail.txt; head -c 300 $TMPDIR/tail.txt; wc -c $TMPDIR/tail.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
t=open('paper/10.1016-j.cell.2024.08.015.txt').read()
print(t[109893:121000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import fitz;d=fitz.open('paper/10.1016-j.cell.2024.08.015.supp.pdf');print(len(d))
for i,p in enumerate(d): print(i+1, p.get_text()[:150].replace('\n',' | '))
"; grep -n "p_relation" -A3 tools/claims_check.py | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "p_relation\|RELATION" tools/claims_check.py | head; ls schema* docs/ 2>/dev/null; which pdftoppm pdfinfo; pdfinfo paper/*.pdf | grep Pages
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "p_relation" -A4 schemas/claims.schema.json; grep -n '"checks"' -A30 schemas/claims.schema.json | head -50; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
297:          "description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.",
298-          "type": "number",
299-          "minimum": 0,
300-          "maximum": 1
301-        },
302:        "p_relation": {
303-          "description": "How p was reported: exactly (the default) or as a bound.",
304-          "enum": [
305-            "=",
306-            "<",
202:    "checks": {
203-      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
204-      "type": "array",
205-      "items": {
206-        "type": "object",
207-        "additionalProperties": false,
208-        "required": [
209-          "date",
210-          "kind",
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 302,315p schemas/claims.schema.json; sed -n 232,250p schemas/claims.schema.json; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2024.08.015.supp.pdf",
 "pages": "4-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001131 && python - <<'EOF'
import re
p='10.1016-j.cell.2024.08.015.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""  statistics:
  - test: Mann-Whitney test (nested Mann-Whitney in S2)
    p: 0.05
    p_relation: "<"
    n: 11 mice per group
""","""  statistics:
  - about: attack measures of Figure 2G
    test: Mann-Whitney test
    p: 0.01
    p_relation: "<"
    n: 11 mice per group
  - about: attack measures of Figure S2B-C
    test: nested Mann-Whitney test
    p: 0.05
    p_relation: "<"
    n: 11 mice per group
""")
rep("""  - about: mean activity (Figure 4E)
    test: nested Mann-Whitney test
    p: 0.05
    p_relation: "<"
  - about: cumulative distributions (Figure 4F, S4D)
    test: Kolmogorov-Smirnov test (nested in S4D)
    p: 0.05
    p_relation: "<"
""","""  - about: mean activity (Figure 4E)
    test: nested Mann-Whitney test
    p: 0.01
    p_relation: "<"
  - about: cumulative distributions (Figure 4F, S4D)
    test: Kolmogorov-Smirnov test (nested in S4D)
    p: 0.01
    p_relation: "<"
""")
rep("""  - about: z-scored activity
    test: nested Kolmogorov-Smirnov test
    p: 0.05
    p_relation: "<"
""","""  - about: z-scored activity
    test: nested Kolmogorov-Smirnov test
    p: 0.01
    p_relation: "<"
""")
rep("""  - about: cumulative distributions (Figure 5A, S5B)
    test: nested Kolmogorov-Smirnov test
    p: 0.05
    p_relation: "<"
  - about: mean single-unit activity (Figure 5C)
    test: nested Mann-Whitney test
    p: 0.05
    p_relation: "<"
""","""  - about: cumulative distributions (Figure 5A)
    test: nested Kolmogorov-Smirnov test
    p: 0.01
    p_relation: "<"
  - about: cumulative distributions, z-scored (Figure S5B)
    test: nested Kolmogorov-Smirnov test
    p: 0.05
    p_relation: "<"
  - about: mean single-unit activity (Figure 5C)
    test: nested Mann-Whitney test
    p: 0.01
    p_relation: "<"
""")
rep("""  - test: Mann-Whitney test
    p: 0.05
    p_relation: "<"
    about: decoder accuracy against shuffled decoders (Figure 4D)
""","""  - test: Mann-Whitney test
    p: 0.01
    p_relation: "<"
    about: decoder accuracy against shuffled decoders (Figure 4D)
""")
# fig2-spares criterion windows
rep("""per mouse (n=11 each) on male-directed sniff time, female-directed sniff time and the mounting
    measures of S2D. Reproduced""","""per mouse (n=11 each) on male-directed sniff time over the first 15 min of the male-male assay,
    and female-directed sniff time and the mounting measures of S2D over 10 min of male-female
    interaction (STAR Methods, Behavior annotations); for the inter-mount interval, mice with at
    most 1 mount bout are left out (same section). The percentage of animals mounting (S2Di) is a
    group proportion and is reported without a per-mouse test. Reproduced""")
# figs7b test
rep("""  statistics:
  - test: nested Mann-Whitney test and Kolmogorov-Smirnov test
    p: 0.05
    p_relation: "<"
    n: 5 control and 7 experimental mice
  expected:
    quantity: relative reduction of mean ACHW, all units, female interaction""","""  statistics:
  - test: not named for panel B (the S7 legend names only a Kruskal-Wallis test with Dunn's
      correction over time points 0-1000 s, which belongs to the slice panels)
    p: 0.05
    p_relation: "<"
    n: 5 control and 7 experimental mice
  expected:
    quantity: relative reduction of mean ACHW, all units, female interaction""")
rep("""(S7B legend). The S7B image shows one and two stars; the legend does not say which test each
    belongs to, and p < 0.05 is recorded. Reproduced when, under a reading, the reduction is within
    tolerance.""","""(S7B legend). The S7 legend names no test for panel B; the tests of the matching male panel
    (Figure 7C, nested Mann-Whitney on the mean, Kolmogorov-Smirnov on the distribution) are run
    and reported, and do not decide the outcome. The S7B image is read as showing one and two
    stars, and p < 0.05 is recorded. Reproduced when, under a reading, the reduction is within
    tolerance.""")
# fig6a post hoc
rep("""within tolerance and the Kruskal-Wallis test across the five dimensions' tau values (mice as
    samples), followed by the comparison of dimension 1 with dimension 2, gives p < 0.05. With 4
    mice a pairwise test may be unable to reach p < 0.05; the attainable minimum p is reported.""","""within tolerance and the Kruskal-Wallis test across the five dimensions' tau values (mice as
    samples) gives p < 0.05 with dimension 1 the largest. The Figure 6 legend names no pairwise
    test after the Kruskal-Wallis test; readings (a) the Kruskal-Wallis test alone, (b) Dunn's
    multiple comparison of dimension 1 with dimension 2, the correction the paper pairs with
    Kruskal-Wallis in the S1F and S7 legends. With 4 mice a pairwise test may be unable to reach
    p < 0.05; the attainable minimum p is reported.""")
# figs7cd inconsistency
rep("""Readings (a) 2 latent dimensions, (b) 5 latent dimensions with
    the two largest tau reported; the number of states read as 1 and 3. Reproduced when, under one
    reading, all three values are within tolerance.""","""Readings (a) 2 latent dimensions, (b) 5 latent dimensions with
    the two largest tau reported; the number of states read as 1 and 3. The paper's numbers are
    not consistent with each other (90 s over 15 s is 6, not 8-9), so the fold ratio is not an
    expected value; the ratio found is reported. Reproduced when, under one reading, all three
    values are within tolerance.""")
# fig5e assignment
rep("""Fractions as pooled or
    per-mouse means, and "reduction" or "increase" as relative change.""","""Fractions as pooled or
    per-mouse means, and "reduction" or "increase" as relative change. For the sniff female
    against sniff male fractions, the values are assigned as the word "increased" requires
    (control 28.8%, experimental 41.1%); elsewhere in this section the paper lists the
    experimental value first, which would give the opposite assignment and contradict the text,
    so that reading is reported and does not decide.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='10.1016-j.cell.2024.08.015.yaml'
s=open(p).read()
a="""# the paper's lowest level ("* P < 0.05", STAR Methods, Statistical analysis). Stars read from the
# supplement images are recorded as read.
"""
assert s.count(a)==1
s=s.replace(a,"""# the paper's lowest level ("* P < 0.05", STAR Methods, Statistical analysis), unless the
# legend's key of stars starts at "**p<=0.01" (Figures 2, 4, 5, S3, S4, S6), in which case any
# significant panel of that figure is at p <= 0.01 and p < 0.01 is recorded. Stars read from the
# supplement images are recorded as read.
""")
s=s.rstrip('\n')+"""
- id: fig3d-cre-editing-spares-mounting
  statement: Bilateral Cre-dependent co-editing in VMHvl Esr1 neurons does not change mounting of
    female intruders.
  source: Results, Altered VMHvl Esr1 neural activity during social interactions, paragraph 2;
    Figure 3D, S3D
  quote: consistent with the lack of an effect on mounting behavior
  statistics:
  - test: Mann-Whitney test
    p: 0.05
    p_relation: ">"
    n: 15 control and 13 experimental mice
  criterion: A claim of absence, judged on the paper's test, the Mann-Whitney test between groups
    per mouse (Figure 3 legend) on the measures of Figure 3D and S3D (mean mount bout duration,
    latency to the first mount, interval between mount bouts) over 10 min of male-female
    interaction (STAR Methods, Behavior annotations); for the interval, mice with at most 1 mount
    bout are left out (same section). Reproduced when none gives p < 0.05; the effect sizes are
    reported either way.
- id: figs7l-blockers-slight-effect
  statement: In slices, synaptic transmission blockers (CNQX and MK-801) only slightly increase the
    decay rate of the peptide-evoked calcium response, during its later phases.
  source: Results, OXT and AVP evoke persistent responses in VMHvl Esr1 neurons ex vivo,
    paragraph 1; Figure S7L
  quote: the inclusion of synaptic transmission blockers (20 μ M CNQX and 10 μ M MK-801) only
    slightly increased the decay rate during later phases of the peptide response
  statistics:
  - test: Kruskal-Wallis test over time points 0-1000 s
    corrected: Dunn's multiple comparison
    p: 0.05
    p_relation: "<"
    n: 45 cells
  criterion: From the S7L legend, the mean response of 45 cells to 100 nM AVP with 20 uM CNQX and
    10 uM MK-801, compared over time points 0-1000 s by Kruskal-Wallis with Dunn's correction. The
    comparison condition is not given (readings, the response to AVP without blockers, or to OXT
    plus AVP without blockers), nor which time points are "later phases". Reproduced when the
    blocker response decays faster than the comparison only after its peak, with significant time
    points (p < 0.05) only in the later part of the response.
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - PLACEHOLDER
"""
open(p,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001131/10.1016-j.cell.2024.08.015.yaml paper/10.1016-j.cell.2024.08.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/001131/10.1016-j.cell.2024.08.015.yaml'
s=open(p).read()
a="""  statistics:
  - test: Kruskal-Wallis test over time points 0-1000 s
    corrected: Dunn's multiple comparison
    p: 0.05
    p_relation: "<"
    n: 45 cells
  criterion: From the S7L legend, the mean response of 45 cells to 100 nM AVP with 20 uM CNQX and
    10 uM MK-801, compared over time points 0-1000 s by Kruskal-Wallis with Dunn's correction. The
    comparison condition is not given (readings, the response to AVP without blockers, or to OXT
    plus AVP without blockers), nor which time points are "later phases". Reproduced when the
    blocker response decays faster than the comparison only after its peak, with significant time
    points (p < 0.05) only in the later part of the response.
"""
b="""  criterion: From the S7L legend, the mean response of 45 cells to 100 nM AVP with 20 uM CNQX and
    10 uM MK-801. The S7 legend names a Kruskal-Wallis test with Dunn's correction over time points
    0-1000 s, and the text does not say the effect is significant, so no p-value is recorded; the
    test is run and reported. The comparison condition is not given (readings, the response to AVP
    without blockers, or to OXT plus AVP without blockers), nor which time points are "later
    phases". Reproduced when, under a reading, the blocker response decays faster than the
    comparison after its peak and not before it.
"""
assert s.count(a)==1; s=s.replace(a,b)
changes='''  - "Header: added the rule used below, that a figure whose legend key of stars starts at **p<=0.01 has every significant panel at p <= 0.01."
  - "fig2g-bilateral-editing-reduces-aggression: split the statistics; Figure 2G is a Mann-Whitney test and the Figure 2 legend key lists only **p<=0.01, so p < 0.01; S2B-C is a nested Mann-Whitney test with * as the lowest level, p < 0.05 kept."
  - "fig2-bilateral-editing-spares-sniff-and-mating: criterion now gives the scored windows (15 min male, 10 min female) and the exclusion of mice with at most 1 bout for intervals (STAR Methods, Behavior annotations), and says the percentage of mice mounting is a group proportion with no per-mouse test."
  - "fig4ef-male-activity-slightly-lower: p raised from 0.05 to 0.01 for both entries; the Figure 4 and S4 legend keys start at **p<=0.01."
  - "fig4ef-female-activity-unchanged: z-scored KS entry p 0.05 to 0.01 (S4 key starts at **)."
  - "fig4d-sex-decoding-intact: p 0.05 to 0.01 (Figure 4 key starts at **)."
  - "fig5ac-behavior-activity-male-lower: Figure 5A and 5C entries p 0.05 to 0.01 (Figure 5 key starts at **); S5B split into its own entry at p < 0.05 (S5 key starts at *)."
  - "fig5e-cp-tuning-shift: criterion notes that the 28.8% and 41.1% are assigned as the word increased requires, though the paper lists the experimental value first elsewhere in the section; the other assignment is reported."
  - "fig6a-control-tau1-greater: the criterion's unnamed pairwise comparison after Kruskal-Wallis is now two readings, Kruskal-Wallis alone or Dunn's comparison of dimension 1 with 2 (the correction paired with Kruskal-Wallis in the S1F and S7 legends)."
  - "figs7b-achw-female-slight: the test was recorded as nested Mann-Whitney and KS, which the S7 legend does not name; recorded as not named, and the criterion runs the Figure 7C tests as report only."
  - "figs7cd-slice-rslds: criterion notes the paper's numbers disagree (90 s over 15 s is 6, not 8-9 fold), so the ratio is reported and not an expected value."
  - "Added fig3d-cre-editing-spares-mounting: a finding of the Results (Figure 3D, S3D) with no claim."
  - "Added figs7l-blockers-slight-effect: a finding of the Results (Figure S7L) with no claim; no p-value recorded since the text does not call it significant."
  - "Not settled: the S7B stars and the S4A, S6E star levels were read from supplement images by the first reader; this check could not render the PDF and did not verify them."
  - "Not settled: fig4c-pls-sex-separation judges a qualitative separation with thresholds the paper does not give (sign of mean PLS1, ROC area beyond 0.75 or 0.25); they are named readings, not the paper's."
  - "Not settled: fig6g-flow-field-line-vs-point judges the flow-field shape by the line attractor score in a majority of mice, a proxy the paper does not state; it largely repeats fig6f-line-attractor-score."
  - "Not settled: fig6-rslds-fit-quality variance explained as emissions R2, the seeds 0 to 3, the forward-simulation horizons and folds, and fig4d C values are readings chosen for details the paper leaves open."
'''
s=s.replace("  - PLACEHOLDER\n",changes)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001131/10.1016-j.cell.2024.08.015.yaml paper/10.1016-j.cell.2024.08.015.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for DANDI:001131 and I've marked it ready. It now has 36 claims, up from 34. Nothing is committed.

**Checker:** `claims/001131/10.1016-j.cell.2024.08.015.yaml: 36 claims, 36 quotes, 32 statistical values, 0 problems`

**Changes, by claim**
- **Header:** The file recorded p < 0.05 for most significant results. When a figure legend's star key starts at `**p≤0.01` (Figures 2, 4, 5, S3, S4, S6), every significant panel in that figure is at p ≤ 0.01. The header now says so, and p < 0.01 is recorded for those figures.
- **fig2g-bilateral-editing-reduces-aggression:** Statistics split in two. Figure 2G is a Mann-Whitney test at p < 0.01. S2B-C is a nested Mann-Whitney test at p < 0.05.
- **fig2-bilateral-editing-spares-sniff-and-mating:** The criterion now gives the scored windows from the Methods (15 min with males, 10 min with females) and the rule that mice with at most 1 bout are left out of the interval measures. It also says the percentage of mice mounting is a group proportion with no per-mouse test.
- **fig4ef-male-activity-slightly-lower**, the z-scored entry of **fig4ef-female-activity-unchanged**, and **fig4d-sex-decoding-intact:** p raised from 0.05 to 0.01 (star keys of Figures 4 and S4).
- **fig5ac-behavior-activity-male-lower:** Figure 5A and 5C set to p < 0.01. S5B is now a separate entry at p < 0.05.
- **fig5e-cp-tuning-shift:** The 28.8% and 41.1% values are assigned so that the fraction increases, as the text says. Elsewhere in that section the paper lists the experimental value first, which would give the opposite. That other reading is reported but does not decide.
- **fig6a-control-tau1-greater:** The Figure 6 legend names no test after Kruskal-Wallis. The criterion now has two readings: Kruskal-Wallis alone, or Dunn's comparison of dimension 1 with dimension 2. Dunn's is the follow-up test the paper uses with Kruskal-Wallis in the S1F and S7 legends.
- **figs7b-achw-female-slight:** The file named nested Mann-Whitney and Kolmogorov-Smirnov tests, but the S7 legend does not name them. The test is now recorded as not named. The Figure 7C tests are run for reporting only.
- **figs7cd-slice-rslds:** The paper's numbers disagree: 90 s over 15 s is 6-fold, not 8–9-fold. The ratio is reported and is no longer an expected value.
- **Added fig3d-cre-editing-spares-mounting** (Figure 3D, S3D) and **figs7l-blockers-slight-effect** (Figure S7L). Both are findings in the Results that had no claim. The S7L claim records no p-value, because the text does not call the effect significant.

**Still open (listed under `checks`)**
- The S7B, S4A and S6E star levels were read from the supplement images by the first reader. I could not open those images (pdftoppm, the PDF-to-image tool, is not installed), so they are unverified.
- **fig4c-pls-sex-separation:** The thresholds for "clear separation" are not from the paper: the sign of the mean PLS1 score, and a ROC area above 0.75 or below 0.25.
- **fig6g-flow-field-line-vs-point:** The flow-field shape is judged by the line attractor score in a majority of mice. The paper does not state this proxy, and the claim largely repeats fig6f.
- **rSLDS and decoder claims:** Several values fill details the paper leaves open, and the file names each as a reading. These are variance explained as the R² of the reconstruction, seeds 0 to 3, the forward-simulation horizon and folds, and the decoder's C values.

**Ready:** yes (`ready: true`). Every open detail is named as such, with the readings the paper allows.

## End of run

19 turns, 4 minutes, result: success.
