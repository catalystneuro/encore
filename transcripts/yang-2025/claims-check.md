# yang-2025 · claims-check · run 42718567981

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/; cat claims/yang-2025.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/yang-2025.yaml"
}
```

```
1	# Claims for Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025), IEEE Trans. Neural Syst. Rehabil.
2	# Eng. 33:4008-4016, doi:10.1109/TNSRE.2025.3614867, on dandiset 001212.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
4	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
5	# files; only its title and description on the archive were read.
6	#
7	# Text read: the version of record (open access, CC BY-NC-ND), PDF supplied by a person, as text
8	# (paper/10.1109-tnsre.2025.3614867.txt), with its one supplement, supp1-3614867.docx (Figures S1
9	# to S3 with legends and Table S1). Figures 2 to 6 were read from the PDF (pages 4 to 7) for the
10	# bars, significance marks and target boxes the text does not hold; Figure S2 from its image and
11	# the transcription stored with the text; Figure S3 from its image.
12	#
13	# Code read: none. The paper links no code and gives no code or data availability statement. It
14	# names two outside MATLAB toolboxes, the MVGC toolbox for conditional multivariate Granger
15	# causality (ref. 37, Barnett and Seth 2014) and the HFO App (ref. 50), and says statistics are in
16	# the figure legends; the software for statistics is not named.
17	#
18	# Data the paper used (Methods A to C). Male Sprague-Dawley rats, lithium-pilocarpine model of
19	# temporal lobe epilepsy; 7 rats (R1 to R7) analysed, of 44 treated. Four depth electrodes per
20	# rat, right hemisphere, DG, CA1, CA3 and ANT, each a recording strand and a bipolar stimulation
[... 460 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/yang-2025.yaml paper/10.1109-tnsre.2025.3614867.txt; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 43,140p docs/protocol.md; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "supplement|table s1|fig. s|===" paper/10.1109-tnsre.2025.3614867.txt | tail -30; sed -n 1000,1087p paper/10.1109-tnsre.2025.3614867.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes with 0 problems. Next I'm checking the details the claims took from figures against the PDF pages.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm mutool; python -c "import fitz; print(fitz.__doc__)"; pdftoppm -r 130 -f 4 -l 7 -png paper/10.1109-tnsre.2025.3614867.pdf pg && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.pdf",
 "pages": "4-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"; which gs magick convert qpdf
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

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/pm pymupdf -q 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pm python -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
for i in range(3,7):
    d[i].get_pixmap(dpi=150).save(f'$TMPDIR/p{i+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
p=d[4]; r=p.rect
p.get_pixmap(dpi=400, clip=fitz.Rect(r.width*0.5, r.height*0.07, r.width, r.height*0.27)).save('f3a1.png')
p.get_pixmap(dpi=400, clip=fitz.Rect(r.width*0.5, r.height*0.18, r.width, r.height*0.31)).save('f3a2.png')
p.get_pixmap(dpi=400, clip=fitz.Rect(r.width*0.5, r.height*0.31, r.width, r.height*0.43)).save('f3bc.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f3a1.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent**

Figure 3A bar readings, significance pairs and target boxes in the claims match the PDF. Now Figure 3B and 3C.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f3bc.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
for i in (3,5,6):
    p=d[i]; r=p.rect
    p.get_pixmap(dpi=110).save(f'full{i+1}.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/full6.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
p=d[5]; r=p.rect
p.get_pixmap(dpi=400, clip=fitz.Rect(r.width*0.55, r.height*0.07, r.width*0.95, r.height*0.23)).save('f4b.png')
p.get_pixmap(dpi=250, clip=fitz.Rect(r.width*0.17, r.height*0.07, r.width*0.55, r.height*0.24)).save('f4a.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f4b.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f4a.png"
}
```

Result: no output.

**Agent**

Figure 4 matches the claims (theta *, alpha **, gamma **; windows as stated). Now Figures 5 and 6.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/full7.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
p=d[6]; r=p.rect
p.get_pixmap(dpi=400, clip=fitz.Rect(r.width*0.25, r.height*0.52, r.width*0.5, r.height*0.75)).save('f6.png')
p.get_pixmap(dpi=300, clip=fitz.Rect(r.width*0.38, r.height*0.27, r.width*0.92, r.height*0.43)).save('f5bd.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f6.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f5bd.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3614867.pdf')
p=d[3]; r=p.rect
p.get_pixmap(dpi=300, clip=fitz.Rect(0, r.height*0.05, r.width, r.height*0.45)).save('f2.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/f2.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

## Prompt

[Image: original 2550x1320, displayed at 2000x1035. Multiply coordinates by 1.27 to map to original image.]

**Agent**

Figure 2 shows 9, 9, 7 and 9 seizures with the targets ANT, ANT, CA3, DG boxed, as the claim says. Checking the supplement figures S2 and S3.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.supp-fig-S2.png"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3614867.supp-fig-S3.png"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement figures S2 and S3 match the transcription and the claims. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "    However, over time, the structure and strength of the brain network connections change\n    significantly, reflecting long-term differences (Fig. 2B).\n  expected:\n  - {quantity: R1 seizures in baseline groups 1 to 4 (Figure 2A columns), value: 34, tolerance: 0}\n  criterion:",
 "new_string": "    However, over time, the structure and strength of the brain network connections change\n    significantly, reflecting long-term differences (Fig. 2B).\n  criterion:"
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "  - about: four sites within each rat\n    test: Kruskal-Wallis",
 "new_string": "  - about: pairwise site comparisons marked in Figure 3A for R2, R3, R4, R5 and R7 (weakest mark\n      one star); the legend names the KW test and prints no omnibus p\n    test: Kruskal-Wallis"
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "named in the legend; following Methods G for independent samples, Mann-Whitney is used, with\n    an unpaired t-test shown as a variant.",
 "new_string": "named in the legend; Methods G names the paired t-test or Mann-Whitney for two samples, and\n    as these samples are independent Mann-Whitney is used, with an unpaired t-test shown as a\n    variant."
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "the three conditions (Figure 4B legend) with Dunn's post hoc. Reproduced",
 "new_string": "the three conditions (Figure 4B legend). The post hoc test behind target against each other\n    condition is not named, and Figure 4B draws only a short mark over the target bar; readings\n    are (a) Dunn's test with Bonferroni-type adjustment; (b) Dunn's test unadjusted. Reproduced"
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "    as in fig6cd-interictal-hfo-no-difference. Reproduced when the test is not significant under\n    reading (a); not reproduced when it is.",
 "new_string": "    as in fig6cd-interictal-hfo-no-difference. The x-axis labels of Figure 6E-F name the red point\n    \"Non-target stim\" and the yellow one \"Target stim\", against the colour code of Figure 6C-D and\n    of Figures 3 to 5 (red for target) and against the text of Results E; the colour code is taken\n    (red is target), so Figure 6E shows target near -0.16 and non-target near -0.04 (read from the\n    plot, for comparison only). Reproduced when the test is not significant under reading (a); not\n    reproduced when it is."
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/yang-2025.yaml",
 "old_string": "    target near -0.25, baseline near 0.2 and non-target near 0.1 (read from the plot, for\n    comparison only).",
 "new_string": "    target near -0.25, baseline near 0.2 and non-target near 0.1 (read from the plot, for\n    comparison only), taking the red point as target by the colour code; its x-axis label reads\n    \"Non-target stim\" (see fig6e-ictal-ripples-no-difference). The text says target stimulation\n    reduced fast ripples, which fits the colour code and not the labels; the stars join the red\n    point to each of the other two."
}
```

```
The file claims/yang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cat >> claims/yang-2025.yaml <<'EOF'
checks:
- date: 2026-11-09
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-r1-target-shifts, removed the expected seizure count (34, tolerance 0); the claim does not
    rest on it and the criterion already says a different count does not decide it. The count (9,
    9, 7, 9 in Figure 2A) stays in the criterion.
  - fig3a-per-rat-site-differences, statistics about now says the p bound comes from the pairwise
    marks of Figure 3A; the paper prints no omnibus Kruskal-Wallis p per rat.
  - fig3b-same-site-target-vs-nontarget, criterion no longer says Methods G gives Mann-Whitney for
    independent samples; Methods G lists it with the paired t-test for two samples.
  - fig4b-psd-target-bands, the Dunn post hoc was stated as the paper's method; the paper names
    only KW, so the post hoc is now named as open with adjusted and unadjusted readings.
  - fig6e-ictal-ripples-no-difference and fig6f-ictal-fast-ripples-reduced, added that the x-axis
    labels of Figure 6E-F name the red point non-target and the yellow target, against the colour
    code of the other figures and the text; the colour code is taken, as the text supports it.
  - Checked against the PDF and supplement images, and found right, are the Figure 3A bar values,
    target boxes and 11 significant pairs, the Figure 3B stars, the Figure 4B stars and windows,
    the Figure 5B inset, the Figure S2 target table and Table S1.
  - Open, not settled, the bands that rise after target stimulation (Results text says alpha and
    beta, Figure 4B, Abstract and Discussion say theta and alpha); kept as two readings.
  - Open, not settled, the R7 mark in Table S1 ("0.71±0.41* **") may be one, two or three stars;
    the criterion needs only p < 0.05, so the outcome does not depend on it.
  - Open, not settled, the normalization formula, the cf_w sign, the GC settings, the unit of
    analysis and the pairing of the Figure 6 paired t-test are not given by the paper; the
    readings named in the file stand.
EOF
python tools/claims_check.py claims/yang-2025.yaml paper/10.1109-tnsre.2025.3614867.txt; grep -n -P "\x{2014}|rather" claims/yang-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for yang-2025 is fit for an attempt (`ready: true`). I made six small corrections from the paper and left three open questions recorded in the file.

**Checker:** `claims/yang-2025.yaml: 19 claims, 17 quotes, 15 statistical values, 0 problems`, both before and after my edits.

I checked every claim against the text and against the PDF figures and supplement images. The figure readings match the paper: the Figure 3A bars, target boxes and 11 significant pairs; the stars in Figures 3B, 4B and 5B; the Figure 4A windows; the Figure 2 seizure counts (9, 9, 7, 9); the Figure S2 target table; and Table S1. All five key findings listed in the Discussion have a claim, and nothing comes from outside this paper.

**Changes, by claim**
- **fig2-r1-target-shifts:** removed the expected seizure count (34, tolerance 0). The claim does not rest on it, and its own criterion says a different count does not decide it.
- **fig3a-per-rat-site-differences:** the `about` of the Kruskal-Wallis entry now says the p bound comes from the pairwise marks in Figure 3A. The paper prints no overall Kruskal-Wallis p per rat.
- **fig3b-same-site-target-vs-nontarget:** fixed how the criterion quoted Methods G. Methods G lists Mann-Whitney with the paired t-test "for two paired samples", not for independent samples.
- **fig4b-psd-target-bands:** the criterion stated Dunn's follow-up test as the paper's method, but the paper names only Kruskal-Wallis. It is now marked open, with adjusted and unadjusted readings.
- **fig6e-ictal-ripples-no-difference and fig6f-ictal-fast-ripples-reduced:** the claims missed a conflict in the figure. The axis labels of Figure 6E-F call the red point "Non-target stim" and the yellow one "Target stim". That goes against the colours used in every other figure (red is target) and against the Results text. The criteria now say this and follow the colours, which the text supports.

**Still open** (named in the file, readings kept)
- **Which bands rise after target stimulation:** the Results text says alpha and beta; Figure 4B, the Abstract and the Discussion say theta and alpha.
- **The R7 mark in Table S1** ("0.71±0.41* **") could be one, two or three stars. This does not change the outcome, since the criterion only needs p < 0.05.
- **Details the paper never gives:** the normalization formula, the sign of cf_w, the Granger causality settings, the unit of analysis, and how the "paired" t-test in Figure 6 is paired.

Only `claims/yang-2025.yaml` was changed, and nothing was committed. To view the figures I installed PyMuPDF into `$TMPDIR`, because no PDF renderer was available.

## End of run

36 turns, 3 minutes, $1.19 at API prices, result: success.
