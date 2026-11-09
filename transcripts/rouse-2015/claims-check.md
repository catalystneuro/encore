# 000941 · claims-check · run 39878501996

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000941/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/000941/*.yaml; python tools/claims_check.py claims/000941/10.1152-jn.00686.2015.yaml paper/10.1152-jn.00686.2015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000941/10.1152-jn.00686.2015.yaml paper/10.1152-jn.00686.2015.txt 2>&1 | tail -30; wc -l claims/000941/*.yaml paper/10.1152-jn.00686.2015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000941/10.1152-jn.00686.2015.yaml"
}
```

```
1	# Claims for Rouse & Schieber (2015), J Neurophysiol 114:3268-3282, on dandiset 000941.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
4	#
5	# Text read. The version of record (PDF supplied by a person, text extracted with PyMuPDF),
6	# complete with Methods, Results, figure legends, Table 1 and Table 2. The paper has no
7	# supplement. Some symbols are garbled in the extracted text (the "<", ">", "~", "x" glyphs
8	# and the eta in "eta squared"); quotes are cut around them with "...". The sense of each
9	# garbled comparison was taken from the sentence around it (e.g. "Qm ratios ... 0.5, indicating
10	# larger location than object effects" is Qm > 0.5).
11	#
12	# Code read. The paper links no code and gives no code or data availability statement. Nothing
13	# below rests on code; every method detail is from the Methods, the Results or the legends.
14	#
15	# Dataset. Dandiset 000941 is titled "FALCON Benchmark M1-A: primary motor cortex recordings in
16	# primate during reach-to-grasp task" and lists this paper with three others from the same
17	# laboratory (J Neurosci 2016, J Neurophysiol 2016 on EMG, Cell Reports 2018). Whether it holds
18	# the kinematic data of this paper (marker positions or joint angles, for which monkeys and
19	# sessions) is for the author to find.
20	#
[... 603 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00686.2015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00686.2015.txt",
 "offset": 1132,
 "limit": 520
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000941 && python - <<'EOF'
p='10.1152-jn.00686.2015.yaml'
s=open(p).read()
def r(a,b):
    global s
    assert s.count(a)==1,a
    s=s.replace(a,b)
r("""taken from M to C only. Qm""","""taken from M to C only. Neither placement is given by the paper; (a) and (b) are both readings,
#   and an outcome holds only when they agree. Qm""")
r("""split equally before M and after C (odd one after C), with variant (b) the maximum SSError""","""split equally before M and after C (odd one after C), and reading (b) the maximum SSError""")
r("""  statement: In the same movements, the MCP, PIP, ThumbFlex, ThumbMCP and ThumbAbAd angles extend""","""  statement: In the same movements, the ThumbFlex, four MCP, ThumbMCP, IndexPIP, MiddlePIP, RingPIP
    and ThumbAbAd angles extend""")
r("""of the ten angles the paper lists (ThumbFlex, the four MCP, ThumbMCP, the four PIP; the
    sentence also names ThumbAbAd, eleven in all).""","""of the ten angles the paper lists (ThumbFlex, the four MCP, ThumbMCP, IndexPIP, MiddlePIP,
    RingPIP and ThumbAbAd; LittlePIP is not in this list, the paper puts it with the angles that
    decrease, increase and decrease again).""")
r("""    Reproduced when both hold for at least 8 of the 11 angles; partially reproduced for 5 to 7.""","""    Reproduced when both hold for at least 8 of the 10 angles; partially reproduced for 5 to 7.""")
r("""effect (Methods); "little or no object effect" is read with the default 10% tolerance as Qm of
    at least 0.9.""","""effect (Methods); the paper gives no bound for "little or no object effect", and it is read
    (a reading, not fixed by the paper) with the default 10% tolerance as Qm of at least 0.9.""")
r("""  quote: The other shoulder angles, ShoulderAbAd and ShoulderFlex, both had clear object effects
  criterion: ANOVA significance from the common methods. Reproduced""","""  quote: The other shoulder angles, ShoulderAbAd and ShoulderFlex, both had clear object effects,
    however, in some cases beginning quite ... early in the reach-to-grasp
  criterion: ANOVA significance from the common methods. "Quite early" is not given a number and
    is read as by 30% of normalized time, the paper's early sample point (a reading). Reproduced""")
r("""  criterion: ANOVA effect sizes from the common methods; hand angles are the 15 digit angles,
    proximal angles the shoulder and elbow angles. Predominate is read as peak object eta2 above
    peak location eta2 from M to C.""","""  criterion: ANOVA effect sizes from the common methods; hand angles are the 15 digit angles. The
    paper gives no measure; predominate is read as peak object eta2 above peak location eta2 from
    M to C (a reading). The paper uses "proximal" both for shoulder and wrist (paragraph 3) and for
    shoulder and elbow as against the wrist and digits (paragraph 5), so proximal angles have two
    readings, (a) the four shoulder and elbow angles, (b) these and the three wrist angles; distal
    angles are the 15 digit angles in both.""")
r("""    the mean peak object eta2 of the four shoulder and elbow angles exceeds the mean peak location
    eta2 of the 15 digit angles, pooled over monkeys.""","""    the mean peak object eta2 of the proximal angles exceeds the mean peak location eta2 of the 15
    digit angles, pooled over monkeys, under either reading of proximal.""")
r("""    angles, and (4) the location peak lies before 90% for more than half of the 18 wrist and digit
    angles with location eta2 at C below its peak.""","""    angles, and (4) the location peak lies before 90% and location eta2 at C is below the peak, for
    more than half of the 18 wrist and digit angles. "Typically", the 90% bound for "continued to
    increase" and "peaked, and then declined" are readings, not fixed by the paper.""")
r("""    The tolerance is the default 10%, tight for two-decimal values; the values printed to two
    decimals are compared after rounding. Reproduced when all nine values are within tolerance
    under one combination of readings, as the readings change the reported number itself;
    partially reproduced when, under some combination, location is at least object minus 0.01
    in every monkey and the values miss tolerance. The values under every combination are shown.""","""    The tolerance is the default 10%, tight for two-decimal values; the values printed to two
    decimals are compared after rounding. The sum of squares type and the SSError placement are
    method details the paper leaves open, so the outcome is the one all combinations give.
    Reproduced when all nine values are within tolerance under every combination; partially
    reproduced when, under every combination, location is at least object minus 0.01 in every
    monkey and some value misses tolerance. Combinations that give different outcomes make the
    claim blocked as methods_underspecified. The values under every combination are shown.""")
r("""  criterion: As fig7-mean-eta-30, at the 90% point. Reproduced when all nine values are within
    tolerance under one combination of readings; partially reproduced when, under every
    combination, mean object eta2 exceeds mean location eta2 in all three monkeys and some value
    misses tolerance.""","""  criterion: As fig7-mean-eta-30, at the 90% point. Reproduced when all nine values are within
    tolerance under every combination of readings; partially reproduced when, under every
    combination, mean object eta2 exceeds mean location eta2 in all three monkeys and some value
    misses tolerance. Combinations that give different outcomes make the claim blocked as
    methods_underspecified.""")
r("""(2) at C the order of
    mean accuracy from 50% to C is shoulder, then wrist, then each digit group;""","""(2) the mean accuracy over
    the samples from 50% to C orders shoulder above wrist, and wrist above each digit group;""")
r("""reading. Nearly 100% is read with the default 10% tolerance as at least 90% correct. In each
    monkey; (1)""","""reading. Nearly 100% is read with the default 10% tolerance as at least 90% correct; "the first
    part of the movements" as the 30% point and "by the temporal midpoint" as the 50% point (readings,
    not fixed by the paper). In each monkey, (1)""")
r("""  quote: At any given location, however, the trajectory of the distal forearm point through space
    depended to some extent on the object to which the hand was being transported, beginning quite
    early in the reach
""","""  quote: At any given location, however, the trajectory of the distal forearm point through space
    depended to some extent on the object to which the hand was being transported, beginning quite
    early in the reach ... by the time of peripheral object contact, the distal forearm point
    typically was positioned highest for the sphere (orange), intermediate for the coaxial cylinder
    (cyan), and lowest for the button (violet) at any of the locations sampled
""")
r("""object on the same coordinates. Reproduced when""","""object on the same coordinates. "Primarily on location" is read (a reading, the paper gives no
    measure) as the comparison of accuracies above chance below. Reproduced when""")
s=s.rstrip('\n')+"\n"
s+='''- id: fig8-hand-shape-invariant-to-location
  statement: Late in the reach, location-dependent differences in hand shape are minor compared
    with object-dependent differences in distal forearm position, as the lower accuracy of
    predicting location from digit angles compared with the high accuracy of predicting object from
    shoulder angles confirms; grasp shape is comparatively invariant to location.
  source: Discussion, Effects of Location on Distal Joint Angles, paragraph 2; Figure 8; Abstract
  quote: The late location-dependent differences in hand shape (Fig. 9) overall seemed relatively
    minor compared with the objectdependent differences in distal forearm position (Fig. 10). This
    impression was confirmed by the lower prediction accuracies of location from digit joint angles
    compared with the high prediction accuracy of object from shoulder joint angles (Fig. 8)
  depends_on:
  - fig8a-lda-location
  - fig8b-lda-object
  criterion: LDA from the common methods, each prior and interval reading. The paper compares
    percent correct and does not name the time; "late" is read as the 90% point (the time of Fig. 9)
    and as C, two readings of the text. Reproduced when, in each monkey, the object accuracy given
    location from shoulder angles exceeds the location accuracy given object from each of the three
    digit groups, at the 90% point or at C; partially reproduced when this holds in two monkeys.
    Accuracy above chance for each is reported as well. Prior and interval readings that disagree
    make the claim blocked as methods_underspecified.
'''
open(p,'w').write(s)
EOF
python ../../tools/claims_check.py 10.1152-jn.00686.2015.yaml ../../paper/10.1152-jn.00686.2015.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && python -c "
import fitz;d=fitz.open('paper/10.1152-jn.00686.2015.pdf')
for b in d[4].get_text('rawdict')['blocks']:
  for l in b.get('lines',[]):
    t=''.join(c['c'] for sp in l['spans'] for c in sp['chars'])
    if 'Kruskal' in t: print([(sp['font'],''.join(c['c'] for c in sp['chars'])) for sp in l['spans']])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00686.2015.pdf",
 "pages": "5"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I couldn't render the PDF, so the "<" in the Kruskal-Wallis bound can't be confirmed from the page. I'll record that as open. Now adding the checks entry.

**Agent calls Bash**

```bash
grep -n "^checks\|^questions" 10.1152-jn.00686.2015.yaml; cat >> 10.1152-jn.00686.2015.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-hand-opening-two-phases, statement and criterion list the ten angles the Results name (ThumbFlex, four MCP, ThumbMCP, IndexPIP, MiddlePIP, RingPIP, ThumbAbAd); LittlePIP was wrongly included (eleven), the paper groups it with the decrease-increase-decrease angles; the count threshold is now 8 of 10.
  - fig7-mean-eta-30 and fig7-mean-eta-90, reproduced required a match under any one combination of sum of squares type and SSError placement; these are open method details, so the protocol requires all combinations to agree, else blocked as methods_underspecified; criteria changed to that.
  - Common methods, SSError placement, the second placement was called a variant; neither is from the paper, so both are now readings that must agree.
  - fig5-location-early-object-late, part (4) restricted its denominator to angles whose location eta2 at C is below the peak, which conditions on the outcome; now the peak before 90% and the decline at C are both required over all 18 wrist and digit angles, and the bounds are named as readings.
  - fig5-hand-object-predominates, the paper uses proximal both for shoulder and wrist and for shoulder and elbow; both readings now listed, and the predominance measure is named as a reading.
  - fig5-shoulder-object-effects, quote extended to cover the statement's early-onset part, and the 30% bound for quite early named as a reading.
  - fig5-shoulderier-location, the 0.9 bound named as a reading not fixed by the paper.
  - fig8a-lda-location, part (2) was self-contradictory (at C and from 50% to C); rewritten as the mean accuracy from 50% to C; the 30% and 50% points named as readings.
  - fig10-forearm-trajectory-object, quote extended to the Discussion sentence on vertical ordering that the statement and criterion use.
  - elbow-point-trajectory-object, the accuracy-above-chance comparison named as a reading.
  - fig8-hand-shape-invariant-to-location, added; the abstract's finding that grasp shape is comparatively invariant to location (Discussion, Effects of Location on Distal Joint Angles) had no claim.
  - Open, table2-movement-time, the checker cannot find p 0.001 as the text garbles the bound ("P �10�3"); read as P < 0.001 from context, the PDF could not be rendered here to confirm the glyph.
  - Open, many criteria rest on readings of qualitative words (bounds for early, comparable, similar, nearly 100%) that the paper does not fix; they are named as readings, and outcomes near those bounds should be read with that in mind.
  - Open, Fig. 10 and the elbow point plots do not name the monkey; judged on monkey L (as in Figs. 3 and 9 and the Discussion's "this monkey"), with the others reported.
EOF
cd ../.. && python tools/claims_check.py claims/000941/10.1152-jn.00686.2015.yaml paper/10.1152-jn.00686.2015.txt 2>&1 | tail -3; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is ready for an attempt. I edited only `claims/000941/10.1152-jn.00686.2015.yaml`.

**Checker:** `26 claims, 26 quotes, 3 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND` for p = 0.001 in table2-movement-time. The text garbles the bound as "P �10�3", and I read it as P < 0.001 from the sentence around it. The PDF could not be rendered here, so I couldn't confirm the "<" glyph. All quotes, including the two I extended, match the text word for word.

**Changes, by claim:**
- **fig2-hand-opening-two-phases:** the list of angles was wrong. It included LittlePIP and gave eleven angles; the paper lists ten and puts LittlePIP with the angles that decrease, increase and decrease again. I corrected the statement and criterion, and the threshold is now 8 of 10.
- **fig7-mean-eta-30 and fig7-mean-eta-90:** these counted as reproduced if any one combination of sum of squares type and error-term (SSError) placement matched. Both are method details the paper leaves open, so the protocol requires all combinations to agree, or else the claim is blocked as methods_underspecified. I changed both criteria to that.
- **Common methods (SSError placement):** the second placement was called a "variant". Neither placement comes from the paper, so both are now readings that must agree.
- **fig5-location-early-object-late:** part (4) only counted angles whose location effect at contact was already below its peak, so it depended on its own outcome. It now covers all 18 wrist and digit angles, and the bounds are named as readings.
- **fig5-hand-object-predominates:** the paper uses "proximal" in two ways, so the criterion now lists both: shoulder and elbow, or those plus the wrist. The measure of "predominate" is named as a reading.
- **fig5-shoulder-object-effects:** the quote now covers the "beginning quite early" part of the statement, and the 30% bound for "early" is named as a reading.
- **fig5-shoulderier-location:** the 0.9 bound is named as a reading, not a number from the paper.
- **fig8a-lda-location:** part (2) said both "at C" and "from 50% to C". It is now the mean accuracy from 50% to C. The 30% and 50% points are named as readings.
- **fig10-forearm-trajectory-object:** the quote now includes the Discussion sentence on vertical order (sphere highest, coaxial cylinder next, button lowest), which the statement and criterion use.
- **elbow-point-trajectory-object:** the comparison of accuracy above chance is named as a reading.
- **New claim, fig8-hand-shape-invariant-to-location:** the abstract's finding that grasp shape varies little with location had no claim. It comes from the Discussion and Fig. 8.

**Still open:**
- The Kruskal-Wallis bound's glyph, as above.
- Many criteria depend on how qualitative words are read ("early", "comparable", "similar", "nearly 100%"). The paper gives no numbers for them. They are all labelled as readings, so outcomes close to those bounds are weak evidence either way.
- Fig. 10 and the elbow-point plots don't name the monkey. The claims are judged on monkey L, and the other monkeys are reported.

The checks entry records each of these with `ready: true`. Nothing was committed.

## End of run

11 turns, 2 minutes, result: success.
