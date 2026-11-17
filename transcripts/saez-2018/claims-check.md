# saez-2018 · claims-check · run 42934839218

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i saez; cat claims/saez-2018.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/saez-2018.yaml"
}
```

```
1	# Claims for Saez, Lin, Stolk, Chang, Parvizi, Schalk, Knight & Hsu (2018), Current Biology
2	# 28:2889-2899, on CRCNS ofc-3.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
4	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
5	# files; only its description on crcns.org (paper/ofc-3.data-description.txt) was read, for which
6	# experiments it holds.
7	#
8	# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with the
9	# PDF: main text, figure legends, STAR Methods (pages e1 to e3) and the Supplemental Information
10	# (Figures S1 to S7, Tables S1 and S2). The extraction garbles some symbols (minus signs, "~" and
11	# the exponents of "p < 10^-5" and "p < 10^-6" print as a replacement glyph; the formulas of Table
12	# S1 are garbled); they were read from context and from the PDF, and quotes are cut around them.
13	#
14	# Code read: none. The paper links no code; it says analysis was done "in MATLAB and R using
15	# custom scripts" (STAR Methods, ECoG Recording).
16	#
17	# Data the paper used. 10 adult patients (4 female) with intractable epilepsy, implanted with
18	# subdural grids or strips at UCSF (2), Stanford (2), UC Irvine (5) and Albany (1). 210 OFC
19	# electrodes recorded, 192 artifact-free and confirmed in OFC kept (per patient 5, 6, 52, 5, 61,
20	# 7, 11, 10, 19 and 16 for s01 to s10, Table S2). One session of 200 rounds per patient (plus
[... 705 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 43,140p docs/protocol.md; python tools/claims_check.py claims/saez-2018.yaml paper/10.1016-j.cub.2018.07.045.txt; wc -l paper/10.1016-j.cub.2018.07.045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 140,220p docs/protocol.md
```

```
when it does; give the size of the effect either way. The rule for
     several readings does not apply: absence is judged on the paper's test
     alone, as written, even when the test mixes in a condition that does
     not belong (show the cleaner test as a variant).
   - If a criterion turns out unable to decide (two candidates tied), break
     the tie as the paper's methods or code imply, record it as a deviation,
     and show the other result.
   - `data`: what the paper's test of the finding uses, from the paper:
     `dataset` (the default: the data the paper describes recording),
     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
     4). Whether the dataset holds those data is the author's to find.
   - `depends_on`: the claims whose result this one uses, such as the cells
     another claim selects.
   - `datasets`: only when the paper is tested on more than one dataset (its
     `papers/datasets/<paper>.yaml` lists several): the folder names of the
     ones the claim rests on. With one dataset, leave it out; every claim
     rests on it. A claim on data in none of them is `data: elsewhere`, or
     rests on a dataset listed as not available.
   - A paper that reuses its datasets (`relation: reuses` in
     `papers/datasets/<paper>.yaml`) is read like any other: its claims are
[... 61 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2018.07.045.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "STAR+METHODS\|KEY RESOURCES\|Behavioral task" paper/10.1016-j.cub.2018.07.045.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2018.07.045.txt",
 "offset": 867,
 "limit": 660
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1016-j.cub.2018.07.045.pdf')
for pg in (8,9):
  for b in d[pg].get_text('blocks'):
    t=b[4].strip().replace('\n',' ')
    print(pg, round(b[0]),round(b[1]), t[:90])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftotext; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2018.07.045.pdf",
 "pages": "9-10"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF here (no poppler), so for the two Discussion sources I'll name each paragraph by its first words instead of a number. Now the edits.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
p='claims/saez-2018.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
# 1 timeout tolerance and denominator
rep("""    value: 9.98
    tolerance: 1.0
    unit: percent
  criterion: Exact counts for electrodes and patients (the per-patient electrode counts of Table
    S2 are 5, 6, 52, 5, 61, 7, 11, 10, 19 and 16 for s01 to s10, which the author compares as
    well). The timeout percentage is the number of Timeout trials over all 2,000 trials.""",
"""    value: 9.98
    tolerance: 0.998
    unit: percent
  criterion: Exact counts for electrodes and patients (the per-patient electrode counts of Table
    S2 are 5, 6, 52, 5, 61, 7, 11, 10, 19 and 16 for s01 to s10, which the author compares as
    well). The timeout percentage is the number of timeout trials over all trials of the 10
    patients. The paper's denominator is not stated; 9.98% of 2,000 is not a whole number of
    trials, so it is read as all trials recorded (2,000 when each patient played 200 rounds).""")
# 2 risk neutral statement
rep("""  statement: Patients were approximately risk neutral, choosing the gamble on 55.9% (plus or minus
    8.5%) of trials.""",
"""  statement: Patients were approximately risk neutral, choosing the gamble only slightly more often
    than a risk-neutral baseline model, on 55.9% (plus or minus 8.5%) of trials.""")
# 4 figs2a
rep("""  criterion: The paper shows this in a figure and reports no test. As in fig1c-choice-win-probability,
    a random-intercept logistic regression of gamble choice on gamble expected value (p times x);
    reproduced when the slope is positive with p < 0.05. The proportions of gamble choices per
    expected-value level are reported.""",
"""  criterion: The paper shows this in a figure and reports no test. The test is borrowed from
    fig1c-choice-win-probability (the paper's test of choice against win probability) and the
    0.05 level is a standard choice, neither from the paper. A logistic regression of gamble
    choice on gamble expected value (p times x) with patient as random effect, readings (a)
    random intercept; (b) random intercept and slope. Reproduced when, under one reading, the
    slope is positive with p < 0.05. The proportions of gamble choices per expected-value level
    are reported.""")
# 5 controls
rep("""    and Figure 1C suggest one comparison per win-probability level. Reading fixed from the legend
    (a) per shown number""","""    and Figure 1C suggest one comparison per win-probability level. Readings the legend and the
    Results (Figures 1C and S1) allow, neither fixed by them: (a) per shown number""")
# 6 RT effect size
rep("""    Reproduced for patients when, under one reading, high-conflict RTs are longer with p < 0.001.
    The healthy-subject part needs data the paper does not say were deposited.""",
"""    Reproduced for patients when, under one reading, high-conflict RTs are longer with p < 0.001.
    The healthy-subject part needs data the paper does not say were deposited. The paper gives no
    measure or test for "comparable" effect sizes; the effect size (Cohen's d, a standard choice)
    is reported for each group and that part is not judged.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/saez-2018.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
# fig3
rep("""    shuffles (STAR Methods), and the chance %EV is the mean %EV of the electrodes so selected
    under shuffles. Reproduced when at least six of the eight counts are within tolerance, every
    regressor's count exceeds the 95th percentile of its shuffled count, the peak of the mean
    %EV of choice regressors falls after game presentation in the game epoch and that of the
    outcome regressors after outcome reveal (button press plus 550 ms); partially reproduced
    when every count exceeds chance and the peaks fall as stated but fewer counts are within
    tolerance.""",
"""    shuffles (STAR Methods), and the chance %EV is the mean %EV of the electrodes so selected
    under shuffles. The paper gives the shuffles but no level for "above chance"; the 95th
    percentile of the shuffled count is a standard choice. The per-window share of encoding
    electrodes (Figure 3 bars) is not defined; readings (a) the share of the 192 electrodes with
    p < 0.05 in that window among those encoding the regressor; (b) the share of all 192 with p <
    0.05 in that window. Reproduced when all eight counts are within tolerance, every regressor's
    count exceeds the 95th percentile of its shuffled count, the peak of the mean %EV of choice
    regressors falls after game presentation in the game epoch and that of the outcome
    regressors after outcome reveal (button press plus 550 ms), and under one reading the
    per-window share of encoding electrodes peaks in the same post-event period as the mean
    %EV; partially reproduced when all of this holds but some counts are outside tolerance.""")
# fig3 latency
rep("""    and regressor, the delay to the start of the longest significant stretch and its length.
    Reproduced""","""    and regressor, the delay to the start of the longest significant stretch and its length.
    Reading (c) is the measure of fig5-past-sustained, whose current durations (799.6 and 706.9
    ms, with SEMs near 35 ms) differ from the ones here, so (a) and (b) are better supported.
    Reproduced""")
# hfa n
rep("""    n: 16 regressors (8 current, 8 past)
  expected:
  - quantity: mean proportion of encoding electrodes, HFA""","""    n: not stated; read as 16 regressors (8 current, 8 t-1)
  expected:
  - quantity: mean proportion of encoding electrodes, HFA""")
rep("""    significantly greater than using FP (mean HFA = 20.9% versus FP =
  statistics:""","""    significantly greater than using FP (mean HFA = 20.9% versus FP = 3.3%
  statistics:""")
# figs4b
rep("""    trial-averaged voltage; (b) mean broadband power. Reproduced when, under one reading, the
    maximum of the broadband response lies within 200 ms of the button press and the peak of
    outcome %EV lies at least 400 ms after it (the outcome is revealed at 550 ms). Needs the
    broadband signal.""","""    trial-averaged voltage; (b) mean broadband power (the Results say "power modulation", the
    Figure S4B legend "ERP"). The paper gives no window for "at the time of button press"; 200
    ms is a standard choice. Reproduced when, under one reading, the maximum of the broadband
    response lies within 200 ms of the button press and the peak of outcome %EV lies about 750
    ms after outcome reveal (1,300 ms after the press), within the expected tolerance. Needs the
    broadband signal.
  expected:
  - quantity: peak of the mean %EV of outcome regressors after outcome reveal
    value: 750
    tolerance: 75
    unit: ms""")
# fig4
rep("""  criterion: The t-1 regressors, with the selection and chance of fig3-present-encoding, in both
    epochs. Reproduced when at least six of the eight counts are within tolerance, each of the
    seven past regressors other than risk has a count above the 95th percentile of its shuffled
    count, and past risk has the lowest count of the eight.""","""  criterion: The t-1 regressors, with the selection and chance of fig3-present-encoding (the 95th
    percentile a standard choice), in both epochs. Reproduced when all eight counts are within
    tolerance, each of the seven past regressors other than risk has a count above the 95th
    percentile of its shuffled count, and past risk has the lowest count of the eight; partially
    reproduced when the last two hold but some counts are outside tolerance.""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/saez-2018.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""readings (a) the share of the 192 electrodes with
    p < 0.05 in that window among those encoding the regressor; (b) the share of all 192 with p <
    0.05 in that window.""","""readings (a) among the electrodes encoding the
    regressor, the share with p < 0.05 in that window; (b) the share of all 192 electrodes with
    p < 0.05 in that window.""")
# fig6
rep("""    not define; read as the shuffled chance proportion of fig3-present-encoding. Reproduced when,
    under one reading, t-2 to t-5 are lower than both t and t-1 with p < 0.01 and the t-2 to t-5
    proportions do not exceed the 95th percentile of chance for more than one regressor in
    five.""","""    not define; read as the shuffled chance proportion of fig3-present-encoding, with its 95th
    percentile as a standard choice. Reproduced when, under one reading, t-2 to t-5 are lower
    than both t and t-1 with p < 0.01 and, at each lag t-2 to t-5, the mean proportion over the 8
    regressors does not exceed the 95th percentile of chance; the per-regressor proportions
    against chance are reported (Figure 6B).""")
# figs5d direction
rep("""    and t-2 greater than t-1, as the legend states (the direction "t-1>t" is read as t-1
    stochastically larger). The paper prints""","""    and t-2 greater than t-1, as the legend states. The direction "t-2>t-1" is read as the ECDF
    of t-2 lying above that of t-1, so that t-2 has smaller -log10 p (weaker encoding), the only
    reading under which a significant result is the boundary the legend describes (the
    one-sided "larger" tail of a two-sample KS test on ECDFs); "t-1>t" likewise. The paper prints""")
# mixed
rep("""    current and t-1 regressors together. Electrodes (a) all 192; (b) encoding electrodes only.
    Bonferroni over the 16 regressors. Reproduced""","""    current and t-1 regressors together. Electrodes (a) all 192; (b) encoding electrodes only.
    The paper does not say what the Bonferroni correction is over; read as over the regressors
    tested (16), and over windows as well under time point (a). Reproduced""")
# figs3b source
rep("""  source: Figure S3B legend; Results, OFC HFA Reflects Choice- and Outcome-Related Valuation
    Signals, paragraph 3; Discussion, paragraph 9""","""  source: Figure S3B legend; Results, OFC HFA Reflects Choice- and Outcome-Related Valuation
    Signals, paragraph 3; Discussion, paragraph beginning "Finally, although ECoG is not affected\"""")
rep("""    STAR Methods, Anatomical reconstructions; Discussion, paragraph 7""","""    STAR Methods, Anatomical reconstructions; Discussion, paragraph beginning "As electrode
    locations were based\"""")
# fig7 all areas
rep("""  criterion: Electrodes encoding any regressor of a group (choice, outcome, past choice, past
    outcome), as in Table S2's "any" rows. The paper names no test for "similar"; a chi-square
    test of encoding against area per group is used, as the test the paper uses for the overlap
    of groups (Figure S7).""","""  criterion: Electrodes encoding any regressor of a group (choice, outcome, past choice, past
    outcome). The selection behind Figure 7B to 7E is not stated; readings (a) the
    5-consecutive-window selection, as in Table S2's "any" rows; (b) the stepwise selection,
    which the Results use for the groups of Figure 7F. The paper names no test for "similar"; a
    chi-square test of encoding against area per group is borrowed from the paper's test of the
    overlap of groups (Figure S7), with 0.05 a standard choice.""")
rep("""    electrodes, against regret. Reproduced when at least one risk electrode""","""    electrodes, against regret. The paper names no test; the quadratic and linear fits at p <
    0.05 are standard choices. Reproduced when at least one risk electrode""")
open(p,'w').write(s)
EOF
grep -n 'beginning' claims/saez-2018.yaml
```

```
587:    Signals, paragraph 3; Discussion, paragraph beginning "Finally, although ECoG is not affected"
638:    STAR Methods, Anatomical reconstructions; Discussion, paragraph beginning "As electrode
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/saez-2018.yaml'
s=open(p).read()
a="""  depends_on:
  - anatomy-brodmann-counts
  - fig3-present-encoding
  - fig4-past-encoding
  criterion: Electrodes encoding any"""
assert s.count(a)==1
s=s.replace(a,"""  depends_on:
  - anatomy-brodmann-counts
  - fig3-present-encoding
  - fig4-past-encoding
  - figs6b-stepwise-similar
  criterion: Electrodes encoding any""")
s=s.rstrip('\n')+'\n'+'''checks:
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - methods-electrode-trial-counts, timeout tolerance 1.0 set to 0.998, 10% of the value, as no reason was given for another; criterion notes that 9.98% of 2,000 is not a whole number, so the denominator is read as all trials recorded.
  - behavior-risk-neutral, statement adds that patients gambled only slightly more often than a risk-neutral baseline model, as the quoted sentence says.
  - figs2a-choice-gamble-ev, criterion says the test is borrowed from fig1c and the 0.05 level is a standard choice, since the paper reports no test; random-effects readings aligned with fig1c.
  - fig1c-patients-like-controls, "Reading fixed from the legend" replaced, since the legend fixes no test; both readings are named as allowed, not fixed.
  - figs2b-rt-conflict, criterion now says how the statement's "comparable effect sizes" is handled (reported, not judged; the paper gives no measure).
  - fig3-present-encoding, "at least six of the eight counts within tolerance" was not from the paper; reproduced now needs all eight, with fewer giving partial; the 95th percentile of chance named as a standard choice; the statement's rise in the number of encoding electrodes (Figure 3 bars) was untested, now tested with two readings of the per-window share.
  - fig3-latency-duration-similar, criterion notes that reading (c) is the measure of fig5-past-sustained, whose current durations differ from the ones here, so (a) and (b) are better supported.
  - hfa-more-than-fp, n "16 regressors" is a reading, not stated by the paper, now said so; quote extended to "3.3%".
  - figs4b-power-at-buttonpress, the outcome-peak condition "at least 400 ms after the press" was not from the paper (it allows a peak before outcome reveal); replaced by the paper's ~750 ms after reveal, added as an expected value with 10% tolerance; 200-ms window named as a standard choice; power against ERP wording of Results and legend noted.
  - fig4-past-encoding, same change as fig3-present-encoding for the six-of-eight rule and the 95th percentile.
  - fig6-past-short-lived, "more than one regressor in five" was a made-up threshold; replaced by the mean over regressors at each lag against the 95th percentile of chance, named as a standard choice.
  - figs5d-sharp-boundary, direction of the one-sided KS tests reversed; reading "t-2>t-1" as t-2 stochastically larger would make a significant result mean more encoding at t-2, the opposite of the boundary the legend describes; it is now read as the ECDF of t-2 lying above that of t-1.
  - mixed-effects-robust, "Bonferroni over the 16 regressors" was stated as fixed though the paper does not say, and conflicted with the windows reading; now named as a reading.
  - figs3b-no-motor-encoding, Discussion source was paragraph 9, which does not mention movement; now the paragraph beginning "Finally, although ECoG is not affected".
  - no-anatomical-gradient, Discussion source was paragraph 7, which does not mention gradients; now the paragraph beginning "As electrode locations were based".
  - fig7-all-areas-similar, the selection behind Figure 7B to 7E is not stated; stepwise selection (used for Figure 7F) added as a reading, with depends_on figs6b-stepwise-similar; chi-square test named as borrowed and 0.05 as a standard choice.
  - fig2-example-electrodes, criterion says the quadratic and linear tests are standard choices, the paper naming none.
  - Checker flags 1e-06 (fig5-past-sustained) and 0.0001 (mixed-effects-robust) as not found; the text prints "p < 10�6" and "p < 10�4" with the minus sign garbled, so both values are the paper's.
  - Open, not settled from the text. Discussion paragraphs were cited by their first words because the PDF could not be rendered to count paragraphs across page breaks. Table S2 is internally inconsistent (s06 "any choice" is 4 while every s06 choice row is 0), and its patient counts give 7.75 and not the paper's 7.41 (claim tables2-patients-coverage names readings). The Behavioral task paragraph gives 20% win probability for a shown 2 against 80% in Table S1 and the worked example (opening comment).
'''
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/saez-2018.yaml paper/10.1016-j.cub.2018.07.045.txt; python -c "import yaml;d=yaml.safe_load(open('claims/saez-2018.yaml'));print(len(d['claims']), d['checks'][-1]['ready'])"; grep -n '—\|rather' claims/saez-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/neither fixed by them: (a) per shown number/neither fixed by them, (a) per shown number/' claims/saez-2018.yaml; grep -nP '^\s+(?!- )[^:]*\S: |^\s+- [^:]*: .*: ' claims/saez-2018.yaml | grep -vP '^\d+:\s*(- )?[a-z_]+: ' | head; python tools/claims_check.py claims/saez-2018.yaml paper/10.1016-j.cub.2018.07.045.txt; grep -n '—\|rather' claims/saez-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/saez-2018.yaml'))
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
for x in d['checks'][-1]['changes']:
  if ': ' in x: print('chk',x[:40])
print(d['checks'][-1]['ready'], len(d['checks'][-1]['changes']))
"; git diff --stat
```

```
True 19
 claims/saez-2018.yaml | 133 +++++++++++++++++++++++++++++++++++---------------
 1 file changed, 94 insertions(+), 39 deletions(-)
```

**Agent**

I checked and corrected `claims/saez-2018.yaml`, and it is now fit for an attempt. Nothing was committed.

**Checker:** `claims/saez-2018.yaml: 28 claims, 28 quotes, 13 statistical values, 2 problems`. The two problems are the 1e-06 in `fig5-past-sustained` and the 0.0001 in `mixed-effects-robust`. Both are in the paper: the text extraction garbles the minus sign in "p < 10^-6" and "p < 10^-4", so the checker can't match them. Every quote matched word for word, and the Table S2 sums (all 16 electrode counts, 167 task-active electrodes, 20.9% mean) match the table.

**Changes, by claim:**
- **figs5d-sharp-boundary:** The direction of the one-sided KS tests was backwards. As written, a significant result would have meant stronger encoding at t-2, the opposite of the boundary the legend describes. It is now read so that t-2 shows weaker encoding than t-1.
- **fig3-present-encoding, fig4-past-encoding:** The rule "at least six of eight counts within tolerance" was made up. Full reproduction now needs all eight counts, and fewer gives a partial result. The 95th-percentile chance level is now named as a standard choice. The rise in the number of encoding electrodes (`fig3-present-encoding`'s statement) was never tested; it now is, under two readings.
- **figs4b-power-at-buttonpress:** The made-up condition "outcome peak at least 400 ms after the press" would have accepted a peak before the outcome is even shown. I replaced it with the paper's figure of about 750 ms after outcome reveal, added as an expected value with 10% tolerance. The 200-ms window is named as a standard choice.
- **fig6-past-short-lived:** The made-up "more than one regressor in five" threshold is replaced by the mean over regressors at each lag, compared against chance.
- **mixed-effects-robust:** The file stated the Bonferroni correction as over 16 regressors, but the paper doesn't say. It is now listed as a reading.
- **figs3b-no-motor-encoding, no-anatomical-gradient:** The Discussion paragraph numbers were wrong: the paragraphs cited don't mention movement or gradients. Each is now cited by its first words.
- **fig7-all-areas-similar:** Added the stepwise selection as a reading, plus a dependency on `figs6b-stepwise-similar`. The chi-square test is marked as borrowed from elsewhere in the paper.
- **hfa-more-than-fp:** n is now marked as a reading (the paper doesn't state it), and the quote is extended to "3.3%".
- **methods-electrode-trial-counts:** The timeout tolerance is now 0.998 (10% of the value). The criterion notes that 9.98% of 2,000 trials isn't a whole number, so the denominator is read as all trials recorded.
- **behavior-risk-neutral:** The statement now says patients gambled "only slightly more often than a risk-neutral baseline model", as the quoted sentence does.
- **fig1c-patients-like-controls:** Removed the wrong claim that the legend fixes the test.
- **figs2a-choice-gamble-ev, fig2-example-electrodes:** Their tests are now labelled as borrowed or standard choices, since the paper names none.
- **figs2b-rt-conflict:** Says how "comparable effect sizes" is handled: reported, not judged, since the paper gives no measure.
- **fig3-latency-duration-similar:** Notes that reading (c) is the measure used in Figure 5, whose values differ from the ones here, so it is the least supported reading.

**Still open:**
- I couldn't render the PDF (no PDF tools installed), so I couldn't count Discussion paragraphs across page breaks. That is why those two sources use first words instead of numbers.
- Table S2 contradicts itself: patient s06 has 4 in "any choice" but 0 in every choice row.
- Table S2's patient counts give a mean of 7.75, not the paper's 7.41. The claim already lists readings for this.
- The Methods give a 20% win probability for a shown 2, while Table S1 and the worked example give 80%. The opening comment already handles this.

Every main finding has a claim, and none comes from outside the paper. The `checks` entry is added with `ready: true`.

## End of run

18 turns, 4 minutes, $1.29 at API prices, result: success.
