# ebrains-q0fg-1x8 · claims-check · run 39494824098

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/ebrains-q0fg-1x8/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l claims/ebrains-q0fg-1x8/*.yaml paper/*.txt; grep -n "4.91\|3.35\|4.67\|0.8117\|1.95" paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml"
}
```

```
1	# Claims for Nagelhus, Andersson, Gonzalo Cogno, Moser & Moser (2023), "Object-centered population
2	# coding in CA1 of the hippocampus", Neuron 111, 2091-2104, on EBRAINS dataset 10.25493/Q0FG-1X8.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, protocol
4	# as stated in docs/protocol.md (pilot-10).
5	#
6	# Text read: the version of record (open access, CC BY), from the PDF supplied by a person, as
7	# extracted to paper/10.1016-j.neuron.2023.04.008.txt: main text, figure legends, STAR Methods and
8	# the Supplemental information (Supplementary Figures 1 to 8 and Supplementary Table 1). The legend
9	# of Supplementary Figure 7 is an image in the PDF and is missing from the text; it was read from
10	# PDF page 46. The CA3 p-values of Supplementary Figure 3F were read from PDF page 35. Supplementary
11	# Table 1 is garbled in the text (exponents of some p-values are lost) and is used only where legible.
12	#
13	# Code read: the paper's code on Zenodo (doi:10.5281/zenodo.7797252, "v1.0"), a snapshot of GitHub
14	# sebasoa/Object-centered-population-coding at tag v1.0, commit 4e4f5ac. It holds MATLAB functions
15	# for the object-tuning score (objectTuningScore.m, templateMatchingScore.m,
16	# shuffledTemplateMatchingScore.m, rateMapData.m, compareThreshold.m) and for the distance decoder
17	# (distanceDecoder.m, divideTrainingTesting.m, binningSpikeMatrix.m, equalDistanceEdges.m,
18	# calculateDistanceMap.m, calculateDecodingAccuracy.m), with a rate-map function (calculateRateMap.m,
19	# from the Behavioural Neurology Toolbox). Two functions they call are not in the repository:
20	# objectScore (the template and its correlation with a rate map) and PoissonDecoder_distance (the
[... 908 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml",
 "offset": 928
}
```

```
928	    statistic: W = 102
929	    p: 6.10e-4
930	  criterion: Methods, Kullback-Leibler divergence, words and distance bins as in
931	    fig5b-words-more-informative, D(NO||O) over all words, probabilities as counts over all
932	    timepoints. Words seen in NO and never in O make the sum infinite, and the paper does not say how
933	    that was handled; the one finite reading its text allows is to sum over words seen in both
934	    trials, recorded as a deviation. Shuffled data assign trial labels to words at random (Figure 5E
935	    legend). Reproduced when the Kruskal-Wallis test and the bin 1 against bin 5 signed-rank test give
936	    p < 0.05 with bin 1 higher, and the shuffled divergences show no Kruskal-Wallis effect at 0.05.
937	- id: fig5-entropy
938	  statement: The entropy of words was higher than that of counts (1.65 against 0.84 bits).
939	  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 4
940	  quote: "the entropy was higher for words than counts (entropy of words: 1.65 bits ± 0.06; entropy of
941	    counts: 0.84 bits ± 0.02; mean ± SEM)"
942	  expected:
943	  - quantity: entropy of words
944	    value: 1.65
945	    tolerance: 0.165
946	    unit: bits
947	  - quantity: entropy of counts
[... 289 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 1180,
 "limit": 1500
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports 28 unmatched p-values. The extracted text shows "×10^" as "3 10�", so I'll confirm those values by reading. Next I'm reading the Methods.

**Agent calls Grep**

```json
{
 "pattern": "^(STAR\\+METHODS|KEY RESOURCES|QUANTIFICATION|Template matching|Bayesian decoding|Statistical tests|Supplemental|Figure S\\d|Table S1)",
 "path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 1200,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 1649,
 "limit": 460
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 2108,
 "limit": 570
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the whole paper. Now checking the Supplementary Figure 7 legend, which is only an image in the PDF.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.pdf",
 "pages": "46"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2023.04.008.pdf')
for p in (34,45):
  pg=d[p]; pix=pg.get_pixmap(dpi=110); pix.save(f'p{p+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1; which mutool qpdf pdfimages gs magick convert 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re,zlib
b=open('paper/10.1016-j.neuron.2023.04.008.pdf','rb').read()
objs=list(re.finditer(rb'(\d+) 0 obj(.*?)endobj',b,re.S))
n=0
for m in objs:
    body=m.group(2)
    if b'/Subtype /Image' in body or b'/Subtype/Image' in body:
        d=body[:400]
        w=re.search(rb'/Width (\d+)',d); h=re.search(rb'/Height (\d+)',d)
        f=re.search(rb'/Filter\s*/(\w+)',d)
        print(m.group(1),w and w.group(1),h and h.group(1),f and f.group(1),len(body))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
b=open('paper/10.1016-j.neuron.2023.04.008.pdf','rb').read()
m=re.search(rb'\n91 0 obj(.*?)stream\r?\n',b,re.S)
s=m.end(); e=b.find(b'endstream',s)
open('o91.jpg','wb').write(b[s:e])
print(m.group(1)[:300])
EOF
ls -la $TMPDIR/o91.jpg
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
b=open('paper/10.1016-j.neuron.2023.04.008.pdf','rb').read()
for m in re.finditer(rb'(?<!\d)91 0 obj',b):
    s=b.find(b'stream',m.end()); s=b.find(b'\n',s)+1
    e=b.find(b'endstream',s)
    print(m.start(), b[m.end():m.end()+200])
    open('o91.jpg','wb').write(b[s:e])
EOF
ls -la $TMPDIR/o91.jpg
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/o91.jpg"
}
```

Result: no output.

## Prompt

[Image: original 1340x2306, displayed at 1162x2000. Multiply coordinates by 1.15 to map to original image.]

**Agent**

The large image is Figure 1, not the S7 legend. The Figure 1H panel's y axis runs to 62 cells, while its legend says 35. I'll note that. Next I'm checking which findings have no claim.

**Agent calls Bash**

```bash
grep -n "^- id:" claims/ebrains-q0fg-1x8/*.yaml | wc -l; grep -n -i "wall\|S8E\|S7A\|Figure 6E\|checks:" claims/ebrains-q0fg-1x8/*.yaml
```

```
55
100:# found is reported. Statistics over sessions (Methods, Statistical tests): Kruskal-Wallis across
586:    test: Kruskal-Wallis test
597:    every reading of speed and sessions, the Kruskal-Wallis test across the 5 bins gives p < 0.05 with
599:    4 vs 5 each give p < 0.05 with the nearer bin higher. Partially reproduced when the Kruskal-Wallis
619:  - test: Kruskal-Wallis test
623:  criterion: A claim of absence, judged on the paper's test, a Kruskal-Wallis test across the 5 angular
639:    test: Kruskal-Wallis test
654:    the Kruskal-Wallis test gives p < 0.05 with correlation rising from bin 1 to bin 5 and the three
672:  - test: Kruskal-Wallis test
677:    beyond 100 cm are left out, as the Methods' bins stop there. Reproduced when the Kruskal-Wallis
687:  - test: Kruskal-Wallis test
694:    Kruskal-Wallis test across the 5 bins gives p >= 0.05, not reproduced when p < 0.05.
703:  - test: Kruskal-Wallis test
743:  - test: Kruskal-Wallis test
749:    (b) position samples. Reproduced when, under one reading, the Kruskal-Wallis test gives p < 0.05
776:    test: Kruskal-Wallis test
780:    test: Kruskal-Wallis test
784:    test: Kruskal-Wallis test
792:    Kruskal-Wallis tests give p >= 0.05 and the median accuracy over sessions is below 0.6 for each;
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "4.42\|2480\|0.8117\|0.221" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --target $TMPDIR/py pymupdf 2>&1 | tail -2
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/py python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2023.04.008.pdf')
for p in (45,48):
  d[p].get_pixmap(dpi=130).save(f'p{p+1}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p46.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p49.png"
}
```

Result: no output.

**Agent**

The S7 legend (PDF page 46) confirms the figs7cd and figs7e statistics. Table S1 on page 49 gives p = 1.50e-5 for the bin-1-excluded test. Now applying corrections.

**Agent calls Bash**

```bash
cd claims/ebrains-q0fg-1x8 && python - <<'EOF'
f='10.1016-j.neuron.2023.04.008.yaml'
s=open(f).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:60])
    s=s.replace(a,b)
# A fig1c
rep("""CON2. Reproduced when, under one reading, both fractions are within tolerance and a one-sided
    binomial test of the object-tuned count against the chance fraction gives p < 0.05.""",
"""CON2. Reproduced when, under one reading, both fractions are within tolerance and a binomial test
    of the object-tuned count against the chance fraction gives p < 0.05 (two-sided, as all the
    paper's tests are; Methods, Statistical tests).""")
# B fig1g
rep("""  criterion: A claim of absence, judged on the paper's test. For every cell recorded on more than one
    day and object-tuned on at least one, each day's object-tuning score (opening comment) against the
    number of days the rat had been exposed to the object; Pearson correlation over all cell-days.
    Reproduced when p >= 0.05; not reproduced when p < 0.05. The r and the number of cells are given
    either way. Needs cell identities across days.""",
"""  criterion: A claim of absence, judged on the paper's test, a Pearson correlation at alpha 0.05 of the
    object-tuning score (opening comment) against the number of days the rat had been exposed to the
    object, over the cells recorded on more than one day and object-tuned on at least one. The legend
    says each dot is a cell (n = 62) and does not say which day's score stands for a cell; readings
    (a) the score on the first day the cell passed as object-tuned; (b) the cell's highest score;
    (c) every cell-day, in case the dots are cell-days. Reproduced when p >= 0.05; not reproduced when
    p < 0.05. The r and the number of cells are given either way. Needs cell identities across days.""")
# C fig1h
rep("""object-tuned cells passing on more than one day is within 10% of 13 or of 11, and a one-sided
    binomial test of that count among the 35 against the fraction of other cells passing on a later
    day gives p < 0.05. Needs cell identities across days.""",
"""object-tuned cells passing on more than one day is within 10% of 13 or of 11, and a two-sided
    binomial test (Methods, Statistical tests) of that count among the 35 against the fraction of
    other cells passing on a later day gives p < 0.05. The y axis of Figure 1H runs to 62 cells while
    its legend says 35; the count found is reported. Needs cell identities across days.""")
# D figs4
rep("""field's area centred on its centroid; (b) the smallest circle centred on the centroid containing
    the field. Reproduced when, under one reading, both values are within tolerance and a one-sided
    binomial test against 1% gives p < 0.05.""",
"""field's area centred on its centroid; (b) the smallest circle centred on the centroid containing
    the field. A cell counts when any of its fields passes (Supplementary Figure 4A legend: each field
    is tested). Reproduced when, under one reading, both values are within tolerance and a two-sided
    binomial test (Methods, Statistical tests) against 1% gives p < 0.05.""")
# E figs2d
rep("""The paper does not say how traces
    were removed; the one reading its text allows is to leave the OM rate-map bins inside the trace
    ROIs of figs4-object-traces out of the template correlations.""",
"""The paper does not say how traces
    were removed; readings (a) leave the OM rate-map bins inside the trace ROIs of
    figs4-object-traces out of the template correlations; (b) set the rate in those bins to zero.""")
# F fig3b
rep("""test per session; its chance level is the label-shuffling procedure (Methods, Shuffling trial
    labels). Reproduced when, under both speed readings, every session's accuracy exceeds 0.5 and
    exceeds the 99th percentile of 50 label shuffles of that session (the 50 shuffles of
    Supplementary Figure 5E).""",
"""test per session; it gives chance as 50%, and its chance level comes from the label-shuffling
    procedure (Methods, Shuffling trial labels; 50 shuffles per session, Supplementary Figure 5E).
    Reproduced when, under both speed readings, every session's accuracy exceeds 0.5 and the mean
    accuracy of that session's 50 label shuffles.""")
rep("""    Reproduced when the accuracy exceeds 0.5 and the 99th percentile of label shuffles in every
    session; partially reproduced when in more than half.""",
"""    Reproduced when the accuracy exceeds 0.5 and the mean of the session's label shuffles in every
    session; partially reproduced when in more than half.""")
# G fig3d
rep("""to each dataset's size. The paper gives no test. Reproduced when, under one reading, mean
    accuracy is higher at the largest k than at k = 1 by more than the SD across subsets, and no step
    in k lowers the mean by more than that SD.""",
"""to each dataset's size. The paper gives no test; its stated test for correlations is Pearson's
    (Methods, Statistical tests). Reproduced when, under one reading, mean accuracy is higher at the
    largest k than at k = 1 and the Pearson correlation of accuracy with k over all subsets is
    positive with p < 0.05.""")
# H fig4c
rep("""Reproduced when every session meets one
    reading; partially reproduced when more than half do; not reproduced otherwise.""",
"""Reproduced when, under one reading,
    every session meets it; partially reproduced when more than half do; not reproduced otherwise.""")
# I figs6
rep("""Reproduced when all three
    Kruskal-Wallis tests give p >= 0.05 and the median accuracy over sessions is below 0.6 for each;
    not reproduced when any test gives p < 0.05.""",
"""Reproduced when all three
    Kruskal-Wallis tests give p >= 0.05; not reproduced when any test gives p < 0.05. The paper gives
    no number for "slightly above 50%", so the median accuracy of each decoder is reported, not judged.""")
# J tables1
rep("""  expected:
    quantity: Kruskal-Wallis H across distance bins 2 to 5
    value: 25.06
    tolerance: 2.506
  criterion: The distance decoder results of fig4b-distance-decline, bins 2 to 5 only. The table's
    p-value has lost its exponent in the text. Reproduced when""",
"""  statistics:
  - test: Kruskal-Wallis test
    statistic: H = 25.06
    p: 1.50e-5
  expected:
    quantity: Kruskal-Wallis H across distance bins 2 to 5
    value: 25.06
    tolerance: 2.506
  criterion: The distance decoder results of fig4b-distance-decline, bins 2 to 5 only. The table's
    p-value has lost its exponent in the text; it was read from PDF page 49. Reproduced when""")
# K fig6ab
rep("""    value: 0.987
    tolerance: 0.013""","""    value: 0.987
    tolerance: 0.0987""")
rep("""The tolerance on the
    within-bounds fraction stops at 1.""","""The tolerance on the
    within-bounds fraction is 10% and stops at 1.""")
# L fig6d
rep("""both Kruskal-Wallis tests across sizes give p < 0.05 and the largest mean
    difference and most negative mean slope are at 400 or 500 cells.""",
"""both Kruskal-Wallis tests across sizes give p < 0.05 and the largest mean
    difference and most negative mean slope are at 500 cells, as the Results say.""")
# M fig7
rep("""all four r are
    within 0.05 of the printed values with the same sign, and each |r| is below 0.3.""",
"""all four r are
    within 0.05 of the printed values with the same sign and p < 0.05, and each |r| is below 0.3.""")
# O comment
rep("""# Table 1 is garbled in the text (exponents of some p-values are lost) and is used only where legible.""",
"""# Table 1 is garbled in the text (exponents of some p-values are lost); its values were read from PDF
# page 49.""")
rep("""# all 9 rats; the Methods refer""","""# all 9 rats; the Figure 1H legend counts 35 cells while its y axis runs to 62; the Methods refer""")
open(f,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'grep -n -A12 "^checks:" {}'
```

```
1049:checks:
1050-- date: 2026-10-20
1051-  kind: agent
1052-  model: claude-opus-5-5
1053-  ready: true
1054-  changes:
1055-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
1056-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
1057-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
1058-  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
1059-  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
1060-  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
1061-  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
746:checks:
747-- date: "2026-10-20"
748-  kind: agent
749-  model: claude-opus-5-5
750-  ready: true
751-  changes:
752-  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml <<'EOF'
- id: figs5jk-walls-no-pivot
  statement: The arena walls did not act as a pivot as the object did; position decoding error and
    population vector correlations were comparable near (under 15 cm) and far from the walls.
  source: Results, Decoding the presence of an object from neural-population activity, paragraph 5;
    Supplementary Figure 5J and 5K
  quote: "The internal walls of the recording environment did not play a similar role as the
    free-standing object, since position decoding accuracy and population vector correlations were
    comparable near and far away from the walls (Figures S5J and S5K)"
  criterion: A claim of absence. The paper reports no test; its test for paired data is the Wilcoxon
    signed-rank test (Methods, Statistical tests), applied here over the decoding sessions, near
    against far, at alpha 0.05. Near is under 15 cm from a wall, far more than 15 cm (Supplementary
    Figure 5J legend). (J) Position decoding error in the NO trial, the Euclidean distance between the
    animal's position and the decoded position. The position decoder is not described in the Methods;
    the reading allowed is the paper's Bayesian decoder (Methods, Bayesian decoding algorithm) with
    the posterior over the 50 x 50 spatial bins of the NO trial, 1 s samples, the same training and
    testing halves, and the decoded position the bin of maximum posterior. Open, could change the
    outcome; reading (b) takes the posterior mean. (K) The population vector correlation (Methods,
    Population vector correlation) between rate maps of the first and second halves of the NO trial,
    mean over the near and over the far spatial bins. Reproduced when neither signed-rank test gives
    p < 0.05 under any reading; not reproduced when one does. Differences are given either way.
- id: figs8eh-least-tuned-smaller-datasets
  statement: In the tetrode sessions and the 135-cell Neuropixels session too, keeping only the cells
    with the lowest distance tuning weakened but did not at first remove the distance reorganization;
    the slope reached zero when 60% (tetrode) or 50% (135-cell session) of the least-tuned cells were
    kept.
  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,
    paragraph 4; Supplementary Figure 8E to 8H
  quote: "As before, the finding also held in smaller-sized tetrode and Neuropixels data (Figures
    S8E–S8H)"
  depends_on:
  - fig6ab-single-cell-distance-tuning
  - fig6ef-least-tuned-cells
  expected:
  - quantity: fraction of least-tuned cells kept at which the slope reaches zero, tetrode sessions
    value: 0.6
    tolerance: 0.2
  - quantity: fraction of least-tuned cells kept at which the slope reaches zero, 135-cell session
    value: 0.5
    tolerance: 0.2
  criterion: As fig6ef-least-tuned-cells (100, 80, 60, 40 and 20% of cells with the lowest
    single-cell distance tuning kept), on the tetrode decoding sessions pooled (Supplementary Figure
    8E, 14 sessions) and on the 135-cell session. The tolerance is one step of the kept fraction (the
    paper's grid is in steps of 20%), not 10%. Reproduced when, for both datasets, the 100% curve
    has a positive bin 1 minus bin 5 difference and a negative slope, both shrink as fewer cells are
    kept, and the largest kept fraction with a mean slope of zero or above is within tolerance.
    The Results say the 20% finding "held", while the legends say the slope reached zero at 0.6 and
    0.5; the 20% values are reported.
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. 28 values flagged as not found are all printed in the paper with "x 10^" garbled to "3 10" in the text; 25 were confirmed in the text and the three of figs7cd-number-of-words (and those of figs7e-downsampled-words) on PDF page 46, rendered for this check.
  - fig1c-object-tuned-fraction. The binomial test was one-sided; the Methods (Statistical tests) say all tests were two-sided. Made two-sided.
  - fig1h-cross-day-stability. Same change to a two-sided binomial test. Noted that the Figure 1H y axis runs to 62 cells while its legend says 35.
  - figs4-object-traces. Same change to a two-sided binomial test. Added that a cell counts when any field passes, since the Supplementary Figure 4A legend tests each field.
  - fig1g-no-experience-effect. The criterion pooled all cell-days; the legend says each of the 62 dots is a cell and does not say which day's score is used. Named this open, with three readings.
  - figs2d-traces-no-interference. The criterion said only one reading of trace removal was possible; the paper does not say how traces were removed. Added the reading that sets the trace bins to zero.
  - fig3b-decode-presence and figs5a-decode-no-from-no-prime. The 99th percentile of label shuffles was not in the paper, which gives chance as 50% from the shuffling procedure. Now judged against 0.5 and the mean of the session's shuffles.
  - fig3d-number-of-cells. The SD-based rule was not in the paper. Replaced with the paper's test for correlations (Pearson) of accuracy with the number of cells.
  - fig4c-each-session-decreasing. Made explicit that every session is judged under the same reading.
  - figs6-behaviour-decoders-flat. Removed the 0.6 bound on accuracy, which is not in the paper; the medians are reported.
  - tables1-without-bin-1. Added the Kruskal-Wallis statistic with p = 1.50e-5, read from Supplementary Table 1 on PDF page 49 (the exponent is lost in the text).
  - fig6ab-single-cell-distance-tuning. The tolerance of 0.013 on the 98.7% fraction had no reason given; set to the protocol's 10%.
  - fig6d-reorganization-grows-with-cells. The criterion allowed extremes at 400 or 500 cells; the Results say both reached them at n = 500. Set to 500.
  - fig7-single-cell-properties. The statement says the correlations were significant; added p < 0.05 to the criterion.
  - Opening comment. Supplementary Table 1 values are now read from PDF page 49; added the Figure 1H 35 against 62 inconsistency.
  - figs5jk-walls-no-pivot. New claim, a finding of the Results (walls do not act like the object) that had no claim.
  - figs8eh-least-tuned-smaller-datasets. New claim, the Supplementary Figure 8E to 8H finding that had no claim.
  - Open. figs5ghi-fields-and-rates. Its tests (a rank-sum on fields within 20 cm, per-bin signed-rank tests) are not in the paper, which shows only figures. They use the paper's test types but are the claim writer's choices. A better reading could not be fixed from the paper.
  - Open. fig1d-field-distances. The test for "the entire azimuthal range" (a field in every 45 degree sector) is not from the paper.
  - Open. fig2-fraction-changed-no-o. The signed-rank pairing of the 500 within-trial and between-trial values is not given in the paper; pairing by repetition is assumed.
  - Open. figs5jk-walls-no-pivot. The Methods do not describe the position decoder; readings are named.
  - Open. fig5b-words-more-informative. The printed U >= 439 cannot come from a rank-sum of 16 against 16 sessions (largest rank sum 392), so which samples were compared stays uncertain; both readings remain.
EOF
python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | tail -4
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/ebrains-q0fg-1x8 && sed -i 's/(Supplementary Figure 4A legend: each field/(the Supplementary Figure 4A legend tests each field)/; s/^    is tested). Reproduced when/    Reproduced when/' 10.1016-j.neuron.2023.04.008.yaml && sed -n 505,515p 10.1016-j.neuron.2023.04.008.yaml && cd ../.. && python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | tail -4
```

Result: not kept, because it reads the paper's text.

**Agent**

Adding the missing period, then checking that the only problems left are the garbled-exponent values.

**Agent calls Bash**

```bash
sed -i 's/(the Supplementary Figure 4A legend tests each field)$/(the Supplementary Figure 4A legend tests each field)./' claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml && python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | grep -v "^VALUE NOT FOUND" ; python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | grep -c "VALUE NOT FOUND"; python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | grep tables1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/^  - Checker. 28 values flagged as not found are all printed/  - Checker. The 29 values flagged as not found (28 before this check, plus the Supplementary Table 1 p-value added here) are all printed/; s/25 were confirmed in the text and the three/25 were confirmed in the text, the table value on PDF page 49, and the three/' claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml && grep -n "Checker\." claims/ebrains-q0fg-1x8/*.yaml && python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt 2>&1 | tail -1
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for EBRAINS:Q0FG-1X8 is ready for an attempt. I corrected 14 claims, added 2, and left 5 problems open; they are listed under `checks`. Nothing is committed.

**Checker:** `57 claims, 57 quotes, 69 statistical values, 29 problems`. Every quote matches the text word for word. All 29 problems are p-values the checker could not match because the text garbles "×10⁻ⁿ" into "3 10�". I confirmed each one by reading: 25 in the text, and 4 on PDF pages 46 and 49, which I rendered with a temporary PyMuPDF install. Page 46 holds the Supplementary Figure 7 legend, which is only an image; page 49 holds Supplementary Table 1.

**Changes, by claim**
- **fig1c-object-tuned-fraction, fig1h-cross-day-stability, figs4-object-traces:** the binomial tests were one-sided, but the Methods say every test was two-sided. Made them two-sided.
- **fig1h-cross-day-stability:** also noted that the Figure 1H y axis runs to 62 cells while its legend says 35.
- **figs4-object-traces:** also added that a cell counts when any of its fields passes, since the legend tests each field.
- **fig1g-no-experience-effect:** the criterion pooled every cell-day, but the legend says each of the 62 dots is a cell. Which day's score stands for a cell is now named as open, with three readings.
- **figs2d-traces-no-interference:** the claim said only one way of removing traces was possible; the paper does not say how. Added a second reading (trace bins set to zero).
- **fig3b-decode-presence, figs5a-decode-no-from-no-prime:** the "99th percentile of shuffles" threshold is not in the paper. Now judged against 0.5 and the mean of the session's shuffles.
- **fig3d-number-of-cells:** the rule based on the spread across subsets was made up. Replaced it with the paper's test for correlations (Pearson).
- **fig4c-each-session-decreasing:** made explicit that every session is judged under the same reading.
- **figs6-behaviour-decoders-flat:** removed a made-up "accuracy below 0.6" condition; the medians are now only reported.
- **tables1-without-bin-1:** added p = 1.50e-5, read from the table on PDF page 49.
- **fig6ab-single-cell-distance-tuning:** a tolerance of 0.013 had no stated reason; set it to the default 10%.
- **fig6d-reorganization-grows-with-cells:** the criterion allowed the peak at 400 or 500 cells; the Results say 500, so it is 500.
- **fig7-single-cell-properties:** the statement says the correlations were significant, so p < 0.05 is now required.
- **New claims:** `figs5jk-walls-no-pivot` (the walls do not act like the object, Supplementary Figure 5J and 5K) and `figs8eh-least-tuned-smaller-datasets` (Supplementary Figure 8E to 8H). These were findings with no claim.
- **Opening comment:** updated for the table read from page 49 and the Figure 1H inconsistency.

**Still open**
- **figs5ghi-fields-and-rates:** the paper reports no test for these panels. The tests in the criterion are of the paper's kinds but were chosen by the writer.
- **fig1d-field-distances:** the paper says fields cover "the entire azimuthal range". The criterion's "a field in every 45° sector" test is not from the paper.
- **fig2-fraction-changed-no-o:** the paper does not say how the paired values for its signed-rank test are matched; pairing by repetition is assumed.
- **figs5jk-walls-no-pivot:** the Methods do not describe the position decoder, so readings are named.
- **fig5b-words-more-informative:** the printed U ≥ 439 is impossible for 16 against 16 sessions (the largest possible rank sum is 392). Which samples were compared stays open.

**Ready:** yes. The final checks entry says `ready: true`.

## End of run

32 turns, 5 minutes, result: success.
