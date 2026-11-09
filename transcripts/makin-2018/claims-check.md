# 000129 · claims-check · run 40748235938

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000129/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,200p docs/protocol.md; cat claims/000129/*.yaml; python tools/claims_check.py claims/000129/10.1088-1741-2552-aa9e95.yaml paper/10.1088-1741-2552-aa9e95.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 126,200p docs/protocol.md; echo ======; python tools/claims_check.py claims/000129/10.1088-1741-2552-aa9e95.yaml paper/10.1088-1741-2552-aa9e95.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml"
}
```

```
1	# Claims for Makin, O'Doherty, Cardoso & Sabes (2018), J. Neural Eng. 15 026010, on dandiset 000129.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (PDF supplied by a person, extracted to
6	# paper/10.1088-1741-2552-aa9e95.txt), main text with its Methods, Results, Discussion and figure
7	# legends. The paper has no supplement. Two equations are garbled in the extracted text (the
8	# ridge penalty of equation 10 and the Wiener filter order sweep); the PDF could not be rendered
9	# here, and the code settles both (below).
10	#
11	# Data the paper used (Methods, Animal experiments, Data acquisition, Tasks). Three monkeys, 49
12	# sessions of continuous reaching in the horizontal plane. Monkey I (Sabes lab, 37 sessions,
13	# right hemisphere, left arm) and monkey L (Sabes lab, 10 sessions, left hemisphere, right arm):
14	# point-to-point reaching to targets on an 8 by 8 or 8 by 17 grid (I) or a 6 by 6 grid (L),
15	# 15 mm spacing, 450 ms hold, no inter-trial interval. 96-channel Utah arrays in M1 and S1;
16	# S1 was recorded in 7 of monkey I's 37 sessions and in all 10 of monkey L's. Spikes sorted
17	# online, with an unsorted hash unit kept per channel; units below 0.5 Hz discarded, leaving
18	# 171 to 413 units per session for monkey I and 416 to 523 for L. Fingertip position from a
19	# Polhemus sensor at 250 Hz. Monkey C (Koerding lab, 2 sessions, 75 and 91 units, center-out
20	# task) came from a public dataset (Dyer et al., biorxiv 080861). The Sabes lab data are
[... 514 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-aa9e95.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-aa9e95.txt",
 "offset": 700,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-aa9e95.txt",
 "offset": 1399,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1088-1741-2552-aa9e95.txt",
 "offset": 1488,
 "limit": 70
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1088-1741-2552-aa9e95.pdf')
for i in [8,11,12,14,15]:
    d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
print('ok')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool gs convert magick 2>/dev/null; python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1 | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; ls $TMPDIR/pylib | head
```

```
_yaml
bin
fitz
flatbuffers
flatbuffers-25.12.19.dist-info
google
networkx
networkx-3.7.dist-info
numpy
numpy-2.5.4.dist-info
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1088-1741-2552-aa9e95.pdf')
for i in [8,12,14,15]:
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
print('ok')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1088-1741-2552-aa9e95.pdf')
p=d[8]; r=p.rect
clip=fitz.Rect(r.x0+r.width*0.15, r.height*0.17, r.x0+r.width*0.88, r.height*0.30)
p.get_pixmap(dpi=300, clip=clip).save('fig2snr.png')
" 2>/dev/null; echo done
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig2snr.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p13.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1088-1741-2552-aa9e95.pdf')
p=d[12]; r=p.rect
p.get_pixmap(dpi=300, clip=fitz.Rect(r.width*0.15, r.height*0.60, r.width*0.42, r.height*0.74)).save('fig7pos.png')
p.get_pixmap(dpi=250, clip=fitz.Rect(r.width*0.15, r.height*0.08, r.width*0.83, r.height*0.22)).save('fig5.png')
" 2>/dev/null; echo done
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig7pos.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p16.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1088-1741-2552-aa9e95.pdf')
p=d[14]; r=p.rect
p.get_pixmap(dpi=250, clip=fitz.Rect(0, 0, r.width, r.height*0.5)).save('fig8.png')
" 2>/dev/null; echo done
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig8.png"
}
```

Result: no output.

## Prompt

[Image: original 2067x1462, displayed at 2000x1415. Multiply coordinates by 1.03 to map to original image.]

**Agent calls Bash**

```bash
grep -n "checks\|changes\|ready\|kind\|'model'\|\"model\"" tools/claims_check.py | head -40; ls claims | head; grep -l "^checks:" -r claims | head -3
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
claims/000351/10.1126-science.abq6740.yaml
claims/001750/10.1038-s41556-026-02009-4.yaml
claims/001749/10.1038-s41586-022-04507-5.yaml
```

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/000351/10.1126-science.abq6740.yaml | head -30
```

```
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4hi-delay-change-behavior-changes, criterion now says the Weibull and constant models are
    fitted to the per-trial values, not the cumulative sums (cumsum_pavlovian.m, lickdata and
    aucdata); it was left unstated.
  - fig4hi-delay-change-dopamine-unchanged, criterion now says the fit is to per-trial values, and
    counts a mean delta AIC below 0 (constant model better) as no change found; the outcome for a
    significantly negative delta AIC was left unstated.
  - fig6b-no-backpropagation, statement says the late response does not differ from the early one,
    in place of does not exceed it; the paper's test is two-tailed (Table S1, t = -0.16).
  - fig6g-inhibition-magnitude, criterion names three readings for the expected -0.6 (AUC ratio
    with the Methods' 1 s reward window, AUC ratio with the code's 0.5 s window, ratio of mean
    levels); the 0.5 s inhibition AUC over a 1 s reward AUC is about half the equal-window ratio
    the code computes, and Supplementary Note 10 gives the value as a level relative to the reward
    response.
  - figs12f-pre-cs2-licking, statement says the session effect is a main effect; it said the
[... 10 more lines not kept]
```

**Agent**

Checker passes. Reading figures 2, 5, 7, 8 and 9 from the PDF shows several criteria that would fail on the paper's own numbers. Applying corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    does not say which decoder is the nearest competitor. Readings are (a) for each variable,\n    the decoder other than the rEFH (+KF) with the highest mean SNR; (b) the UKF for all three,\n    the decoder the Results and figure 8 call the rEFH's nearest rival.",
 "new_string": "    does not say which decoder is the nearest competitor. Readings are (a) for each variable,\n    the decoder other than the two rEFH decoders with the highest mean SNR (the static rEFH is\n    excluded; figure 2 puts it within about 0.2 dB of the rEFH (+KF) for acceleration, far from\n    1.2 dB); (b) the UKF for all three, the decoder the Results and figure 8 call the rEFH's\n    nearest rival. Figure 8's canonical dynamic bars (rEFH (+KF) minus UKF) read about 0.14,\n    1.6 and 1.2 dB, which supports reading (b)."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    twice\", read here as within 25% below to 10% above). Partially",
 "new_string": "    twice\", read here as within 25% below to 10% above; a bound fixed here, the paper gives\n    none). Partially"
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  expected:\n    quantity: position SNR of rEFH (+KF) minus static rEFH\n    value: 3\n    tolerance: 0.3\n    unit: dB\n  criterion: Session-weighted mean position SNR, averaged over x and y, at 64 ms.",
 "new_string": "  expected:\n  - quantity: position SNR of rEFH (+KF) minus static rEFH\n    value: 3\n    tolerance: 0.5\n    unit: dB\n  criterion: Session-weighted mean position SNR, averaged over x and y, at 64 ms. The tolerance\n    is 0.5 dB, not 10%, because \"some 3 dB\" is a round number given to the nearest dB, and the\n    position bars of figure 2 (SNR row) give a difference of about 2.5 dB (about 2.3 for x and\n    2.8 for y), outside a 10% window."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    (24 pairs). Reproduced when y exceeds x in all 24; partially reproduced in 18 to 23. The",
 "new_string": "    (24 pairs). Reproduced when y exceeds x in all 24; partially reproduced in 18 to 23 (a\n    grading fixed here; the paper gives none). The"
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  criterion: Session-weighted mean SNR, averaged over x and y, at 64 ms. Reproduced when every\n    other decoder exceeds linear regression for every variable, except that the static\n    decoders (static KFlatent and static rEFH) may fall below it for position, which figure 2's\n    position panel allows.",
 "new_string": "  criterion: Session-weighted mean SNR at 64 ms, for each of the six kinematic variables (x and\n    y separately, as in figure 2). Reproduced when every other decoder exceeds linear regression\n    for every variable, as every bar of figure 2 is above zero, including those of the static\n    KFlatent and static rEFH for position (the Discussion also notes the static rEFH's modest\n    superiority over linear regression for position)."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now figures 5, 7, 8, 9 criteria.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    The relative advantage is read as the rEFH (+KF) SNR minus the best other decoder's SNR.\n    Reproduced when, for velocity and acceleration, the rEFH (+KF) SNR and its advantage both\n    rise from 16 to 128 ms (the 128 ms value above the 16 ms value, and no fall of more than\n    0.2 dB between neighbouring widths).",
 "new_string": "    The paper does not define the relative advantage. Readings are (a) the rEFH (+KF) SNR minus\n    the SNR of the best decoder other than the two rEFH decoders, in dB; (b) that difference as\n    a percent of the best other decoder's SNR (the \"percent increase in SNR\" of Results, Number\n    of neurons). Reproduced when, under one reading, for velocity and acceleration, the rEFH\n    (+KF) SNR and its advantage both rise from 16 to 128 ms (the 128 ms value above the 16 ms\n    value, and no fall of more than 0.2 dB, or 2 percentage points, between neighbouring\n    widths; bounds fixed here, the paper gives none)."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  criterion: Session-weighted mean SNR, averaged over x and y, at each bin width. Reproduced when,\n    at each width, every decoder other than the rEFH decoders has SNR position > velocity >\n    acceleration, and the rEFH (+KF) advantage over the best other decoder rises from position\n    to velocity to acceleration. Partially reproduced when this holds at two or three widths.",
 "new_string": "  criterion: Session-weighted mean SNR, averaged over x and y, at each bin width. \"Overall\n    reconstruction quality\" is read as the mean SNR over the six decoders other than the two\n    rEFH decoders; figure 5 shows linear regression and the WF with higher velocity than\n    position SNR at several widths, so a per-decoder ordering would contradict the paper's own\n    figure. The relative advantage is the rEFH (+KF) SNR minus that of the best decoder other\n    than the two rEFH decoders, as a percent of the latter (the \"percent increase in SNR\" of\n    Results, Number of neurons); the difference in dB cannot be meant, since at 64 ms it is 1.60\n    dB for velocity and 1.2 dB for acceleration (Introduction) while the paper says the\n    advantage increases with derivatives. Reproduced when, at each width, the mean SNR has\n    position > velocity > acceleration and the percent advantage rises from position to\n    velocity to acceleration. Partially reproduced when this holds at two or three widths."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    difference, averaged over x and y, between the rEFH (+KF) and each other decoder. Reproduced\n    when every velocity and acceleration difference is positive with p < 0.05, and the percent\n    gain over the best rival rises with f and from velocity to acceleration at each f.\n    Partially reproduced when only the first part holds.",
 "new_string": "    difference, averaged over x and y, between the rEFH (+KF) and each other decoder. The paper\n    does not say what the percent increase is taken over; readings are (a) the best decoder\n    other than the two rEFH decoders, (b) each such decoder. Reproduced when every velocity and\n    acceleration difference is positive with p < 0.01, except against the WF for acceleration\n    at f = 1/4, where p < 0.05 suffices (the levels the paper reports), and, under one reading,\n    the percent gain rises over f = 1/4, 1/2, 1 and from velocity to acceleration at each of\n    these f. Partially reproduced when only the first part holds."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  criterion: Session-weighted mean position SNR, averaged over x and y, at f = 1/8, 1/4, 1/2, 1.\n    For each decoder, the rise from f = 1/8 to 1/4 and from 1/2 to 1. Reproduced when, for each\n    of the four, the first rise exceeds the second, and the first rise exceeds that of each of\n    the four decoders of fig7-affine-position.",
 "new_string": "  criterion: Session-weighted mean position SNR, averaged over x and y, at f = 1/8, 1/4, 1/2, 1.\n    For each decoder, the slope per unit f (rise divided by the change in f) over an initial\n    interval and over 1/2 to 1. The paper does not say which interval is initial; readings are\n    (a) 1/8 to 1/4 and (b) 1/8 to 1/2. Slopes per unit f are used because the intervals differ\n    in length (1/8 and 1/2): an absolute rise of the UKF from 1/2 to 1 is larger than from 1/8\n    to 1/4 in figure 7, which still shows it saturating. Reproduced when, under one reading,\n    for each of the four the initial slope exceeds the slope from 1/2 to 1, and exceeds the\n    initial slope of each of the four decoders of fig7-affine-position."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    in length (1/8 and 1/2): an absolute rise of the UKF from 1/2 to 1 is larger than from 1/8\n    to 1/4 in figure 7, which still shows it saturating.",
 "new_string": "    in length (1/8 and 1/2): figure 7 shows the UKF rising about 1.3 dB from 1/8 to 1/4 (its\n    1/8 value clipped at 0) and about 1.8 dB from 1/2 to 1, yet the paper counts it among the\n    decoders that saturate."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    instead applies 2 sqrt(R + 3/8) (getLatentsBMI.m), shown as a variant. Reproduced when both\n    losses are within tolerance and, under the dynamic mapping, the canonical rEFH (+KF) still\n    exceeds both variants.",
 "new_string": "    instead applies 2 sqrt(R + 3/8) (getLatentsBMI.m), shown as a variant. Reproduced when both\n    losses are within tolerance and, under the dynamic mapping, the canonical rEFH (+KF) still\n    exceeds both variants. Open: figure 8 does not match the text. Its static velocity bars\n    read about 0.65 (no visible units), 0.52 (standard normal) and 0.94 dB (canonical) above\n    the UKF, losses of about 0.3 and 0.4 dB, with the standard-normal variant losing more, not\n    less. The expected values are the text's; the notebook reports both losses against the\n    text's and the figure's values."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  criterion: Session-weighted mean position SNR, averaged over x and y, at 64 ms, for the three\n    variants. Reproduced when the static values span more than 0.5 dB and the dynamic values\n    span less than 0.2 dB (bounds fixed here; the paper gives none).",
 "new_string": "  criterion: Session-weighted mean position SNR, averaged over x and y, at 64 ms, for the three\n    variants. Bootstrap of the session-weighted mean difference between the canonical rEFH and\n    each variant, static and dynamic, at p < 0.01 (the level of that paragraph of the Results).\n    Reproduced when, under the static mapping, the canonical rEFH exceeds both variants with p\n    < 0.01, and under the dynamic mapping neither variant is below the canonical rEFH (+KF) with\n    p < 0.01 (the absence part judged on this test). Figure 8 shows the static variants about\n    0.16 and 0.18 dB below the canonical and the dynamic standard-normal variant about 0.2 dB\n    above it, so bounds on the spread of the values would not fit the paper's own figure."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    mean difference. Reproduced when (i) the tapped decoders have higher mean SNR than their\n    untapped versions for velocity at every width;",
 "new_string": "    mean difference. Reproduced when (i) each tapped decoder has higher mean velocity SNR than\n    its untapped version at 16 and 32 ms (at 64 ms figure 9 shows the tapped and untapped rEFH\n    about equal, and at 128 ms the rEFH has no taps, Results, Augmenting the decoders);"
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    variants. Bootstrap of the session-weighted mean difference between the canonical rEFH and\n    each variant, static and dynamic, at p < 0.01 (the level of that paragraph of the Results).\n    Reproduced when, under the static mapping, the canonical rEFH exceeds both variants with p\n    < 0.01, and under the dynamic mapping",
 "new_string": "    variants. The paper reports no test for this finding; the bootstrap of the session-weighted\n    mean difference between the canonical rEFH and each variant at p < 0.01 (the level of that\n    paragraph of the Results) is used for the dynamic part. Reproduced when, under the static\n    mapping, the canonical rEFH has a higher mean than both variants, and under the dynamic\n    mapping"
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "  criterion: Session-weighted mean SNR, averaged over x and y and over the three variables, at\n    64 ms. Reproduced when the better of KFlatent and KFlatent (+KF) exceeds KFobs and the UKF\n    exceeds KFobs by more. Per variable values are reported, as the Results note that KFlatent\n    (+KF) decodes position slightly worse than KFobs.",
 "new_string": "  criterion: Session-weighted mean SNR, averaged over x and y, at 64 ms. The paper does not say\n    over which variables. Readings are (a) velocity, the variable the paper treats as most\n    important; (b) the mean over velocity and acceleration; (c) the mean over all three\n    variables. Under (c) figure 2 puts both KFlatent decoders slightly below KFobs, since they\n    decode position worse (Results, Reconstruction quality, bullet 2). Reproduced when, under\n    one reading, the better of KFlatent and KFlatent (+KF) exceeds KFobs and the UKF exceeds\n    KFobs by more. Per variable values are reported."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now add the two missing findings and the checks entry.

**Agent calls Bash**

```bash
cat >> claims/000129/10.1088-1741-2552-aa9e95.yaml <<'EOF'
- id: advantage-grows-with-derivative
  statement: At 64 ms and with each amount of training data, the relative advantage of the rEFH
    (+KF) over the other decoders increases from position to velocity to acceleration.
  source: Results, The rEFH against its nearest rivals, all session and monkeys, paragraph 3;
    Results, Seconds of data used for training; Figures 2, 4 and 6
  quote: Overall, the relative advantage provided by the rEFH increases with derivatives.
  criterion: Session-weighted mean SNR, averaged over x and y, at 64 ms with 320 s of training
    (figure 2), and with 80, 160 and 320 s (figure 6, "as with bin widths, the relative advantage
    of the rEFH (+KF) increases with derivatives"). The relative advantage is the rEFH (+KF)
    SNR minus that of the best decoder other than the two rEFH decoders, as a percent of the
    latter, as in fig5-derivative-order; the difference in dB falls from velocity (1.60 dB) to
    acceleration (1.2 dB) in the Introduction, so it cannot be meant. Reproduced when the percent
    advantage rises from position to velocity to acceleration at each amount of training data.
    Partially reproduced when it holds at 320 s only.
- id: static-refh-position-worse
  statement: Under the static mapping alone the rEFH reconstructs position significantly worse
    than the UKF, while the rEFH (+KF) is not distinguishable from it.
  source: Discussion, Relative reconstruction quality of position, velocity, and acceleration,
    paragraph 1; Figure 8, first panel
  quote: Despite superior velocity and acceleration decoding, the rEFH (+KF) reconstructs position
    little better than the UKF (the differences are not significant); and under a static
    mapping, significantly worse.
  criterion: Bootstrap of the session-weighted mean position SNR difference, averaged over x and
    y, between the static rEFH and the UKF at 64 ms. The paper does not give the level of
    "significantly"; the levels it uses elsewhere are 0.01 and 0.05, and both are reported.
    Reproduced when the static rEFH is below the UKF with p < 0.05. The rEFH (+KF) part is
    fig4-position.
  depends_on:
  - fig4-position
checks:
- date: 2026-10-28
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - intro-gain-over-nearest, reading (a) now excludes the static rEFH as well; figure 2 puts it
    about 0.2 dB below the rEFH (+KF) for acceleration, so a reading that includes it cannot give
    1.2 dB. Added that figure 8's canonical dynamic bars (about 0.14, 1.6, 1.2 dB over the UKF)
    support reading (b).
  - fig2-velocity-boost, criterion now says the 1.5 to 2.2 bound for "nearly twice" is fixed here.
  - fig2-position-dynamic-gain, tolerance 0.5 dB in place of 0.3 dB, with the reason; "some 3 dB"
    is a round number and figure 2's position bars give about 2.5 dB, outside a 10% window.
    expected written as a list like the other claims.
  - fig2-sagittal-better, criterion now says the 18 to 23 partial grading is fixed here.
  - fig2-linear-worst, removed the exception letting static KFlatent and static rEFH fall below
    linear regression for position; every bar of figure 2 is above zero, and the Discussion
    states the static rEFH's superiority over linear regression for position. Comparison is now
    per axis, as figure 2 plots it.
  - fig5-advantage-with-binwidth, criterion names the readings of "relative advantage" (dB
    difference, percent) and says the bounds on falls are fixed here.
  - fig5-derivative-order, "overall reconstruction quality" is now the mean over the six
    non-rEFH decoders, and the advantage is a percent; the per-decoder ordering fails for linear
    regression and the WF in figure 5, and the dB advantage falls from velocity to acceleration
    (Introduction, 1.60 and 1.2 dB), contradicting the paper's own numbers.
  - fig7-vel-acc-neurons, criterion now uses the paper's levels (p < 0.01 except WF acceleration
    at f = 1/4, p < 0.05) in place of p < 0.05 throughout, limits the trend to f = 1/4, 1/2, 1,
    and names the readings of what the percent increase is taken over.
  - fig7-kinematic-model-saturates, criterion compares slopes per unit f with two readings of the
    initial interval, in place of absolute rises over intervals of 1/8 and 1/2, which figure 7
    contradicts for the UKF.
  - fig8-velocity-variants, criterion now notes that figure 8 disagrees with the text (static
    losses of about 0.3 and 0.4 dB, the standard-normal variant losing more).
  - fig8-position-variants, criterion replaced; the made-up spread bounds (static over 0.5 dB,
    dynamic under 0.2 dB) fail on figure 8 (static spread about 0.18 dB). Now the canonical
    static mean exceeds both variants, and no dynamic variant is below the canonical by
    bootstrap at p < 0.01.
  - fig9-taps, part (i) now asks for tapped gains at 16 and 32 ms only; figure 9 shows the tapped
    and untapped rEFH about equal at 64 ms, and the rEFH has no taps at 128 ms.
  - kflatent-modest, criterion names three readings of the variables compared; averaged over all
    three variables figure 2 puts both KFlatent decoders below KFobs.
  - Added advantage-grows-with-derivative (Results, rivals paragraph 3, and Seconds of data used
    for training), a main finding the Discussion lists and no claim covered.
  - Added static-refh-position-worse (Discussion, Relative reconstruction quality, paragraph 1),
    a finding no claim covered.
  - Open, fig8-velocity-variants, the text's 0.7 and 0.4 dB do not match figure 8; the expected
    values stay the text's and the author reports both.
  - Open, the code details cited in the header and criteria (SLMD.m one-sided bootstrap, pooling
    of x and y, getLatentsBMI.m unit filter and transforms) were not checked against the
    repository in this run.
  - Open, fig4-advantage-grows, the statistic is recorded as p < 0.01 where the paper prints
    p << 0.01; no change.
EOF
python tools/claims_check.py claims/000129/10.1088-1741-2552-aa9e95.yaml paper/10.1088-1741-2552-aa9e95.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "    in length (1/8 and 1/2): figure 7",
 "new_string": "    in length (1/8 and 1/2); figure 7"
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000129/10.1088-1741-2552-aa9e95.yaml paper/10.1088-1741-2552-aa9e95.txt; grep -n ": .*: \|—\|rather" claims/000129/10.1088-1741-2552-aa9e95.yaml | grep -v "^\s*#" | head; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000129/10.1088-1741-2552-aa9e95.yaml",
 "old_string": "exceeds both variants. Open: figure 8 does not match the text.",
 "new_string": "exceeds both variants. Open, figure 8 does not match the text."
}
```

```
The file claims/000129/10.1088-1741-2552-aa9e95.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000129/10.1088-1741-2552-aa9e95.yaml paper/10.1088-1741-2552-aa9e95.txt 2>&1 | tail -5; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for 000129 and made the corrections below. The file is ready for an attempt. Nothing is committed.

**Checker result:**
- Before my changes: `29 claims, 29 quotes, 12 statistical values, 0 problems`
- After: `31 claims, 31 quotes, 12 statistical values, 0 problems`

The earlier reader said the PDF could not be rendered. I rendered figures 2, 5, 7, 8 and 9 with PyMuPDF installed to a temp folder. Several criteria failed on the paper's own figures, and those are most of the changes.

**Changes, by claim:**
- **intro-gain-over-nearest:** reading (a) now leaves out the static rEFH as well. Figure 2 puts it only about 0.2 dB below the rEFH (+KF) for acceleration, so that reading could never give 1.2 dB. Figure 8's bars (about 0.14, 1.6 and 1.2 dB over the UKF) support reading (b), the UKF.
- **fig2-position-dynamic-gain:** tolerance raised from 0.3 to 0.5 dB, with the reason given. "Some 3 dB" is a round number, and figure 2 shows about 2.5 dB. The `expected` entry is now a list like the others.
- **fig2-linear-worst:** removed the exception that let static KFlatent and static rEFH fall below linear regression for position. Every bar in figure 2 is above zero. The comparison is now per axis, as the figure plots it.
- **fig2-velocity-boost, fig2-sagittal-better:** the bounds and gradings the earlier reader invented are now marked as fixed here, not taken from the paper.
- **fig5-derivative-order:** "overall reconstruction quality" is now the mean over the six decoders other than the two rEFH ones. Figure 5 shows linear regression and the WF decoding velocity better than position. The advantage is now measured as a percent. Measured in dB it falls from velocity to acceleration (1.60 and 1.2 dB in the Introduction), which contradicts the paper's own statement.
- **fig5-advantage-with-binwidth:** names both readings of "relative advantage" (dB difference and percent) and marks its bounds as fixed here.
- **fig7-vel-acc-neurons:** now uses the paper's levels: p < 0.01, or p < 0.05 for the WF in acceleration at f = 1/4. It limits the trend to f = 1/4, 1/2 and 1, and names what the percent gain may be taken over.
- **fig7-kinematic-model-saturates:** now compares slopes per unit f, with two readings of the initial interval. Comparing absolute rises over intervals of 1/8 and 1/2 fails for the UKF in figure 7.
- **fig8-position-variants:** the invented spread bounds failed on figure 8 (static spread is about 0.18 dB). Now the canonical static mean must beat both variants, and no dynamic variant may be below the canonical at bootstrap p < 0.01.
- **fig9-taps:** part (i) now asks for gains from taps at 16 and 32 ms only. Figure 9 shows the tapped and untapped rEFH about equal at 64 ms, and the rEFH has no taps at 128 ms.
- **kflatent-modest:** names three readings of which variables are compared. Averaged over all three, figure 2 puts KFlatent below KFobs.
- **Added two claims:**
  - **advantage-grows-with-derivative:** the relative advantage rises from position to velocity to acceleration, at 64 ms and at each amount of training data.
  - **static-refh-position-worse:** under the static mapping the rEFH decodes position significantly worse than the UKF (Discussion).

**What remains open:**
- **fig8-velocity-variants:** the text says 0.7 and 0.4 dB are lost, but figure 8 shows losses of about 0.3 and 0.4 dB, with the standard-normal variant losing more. The expected values stay the text's, and the criterion asks the author to report both.
- **Code details:** the details the claims cite from the code repository (one-sided bootstrap, pooling of x and y, the unit filter, the transforms) were not checked against it in this run.
- **fig4-advantage-grows:** the paper prints p ≪ 0.01. It is recorded as p < 0.01, unchanged.

## End of run

47 turns, 6 minutes, result: success.
