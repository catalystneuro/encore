# brudner-2026 · claims-check · run 43152362821

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; cat claims/brudner-2026.yaml; grep -n "Reader" -A60 docs/protocol.md | sed -n '1,120p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/brudner-2026.yaml"
}
```

```
1	# Claims for Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark & Emonet, "Fly navigational
2	# responses exploit plume-specific odor motion and gradient cues", PNAS 123(29) e2608896123 (2026),
3	# doi:10.1073/pnas.2608896123, on dandiset 001871.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-12,
6	# under docs/protocol.md version pilot-14 (Reader, steps 1 to 4). Nobody had analysed the dataset's
7	# data when these criteria were written; the reader saw only the dandiset's title and description.
8	#
9	# Text read: the version of record (PDF supplied by a person, published 14 July 2026), as extracted
10	# to paper/10.1073-pnas.2608896123.txt, with the SI Appendix (pnas.2608896123.sapp.pdf, appended to
11	# the same text file): Supplementary Methods, the legends of Figures S1 to S5 and of Movies S1 and S2.
12	# The main Methods section is a short summary that refers to the SI Appendix for every detail. PDF
13	# pages were opened to read the bar heights of Figures 2, 4 and 5 and the panels of Figure S5, and
14	# the upwind-turn formula of the SI agent simulations, which the text garbles. It reads
15	# P_upwind = 1 / (1 + exp(-(-0.49 + 1.5 R sin^2 theta))).
16	#
17	# Code read. The paper links github.com/emonetlab/GradientMotionMultiplePlumes; read at commit
18	# effc7b0317f6d3b62136c2a07bcba3e80e778575 (2026-07-14). It holds
19	#   - the Fig. 5E, 5F and S5D-E analysis (src/gradient_motion_panels/summary_tables.py,
20	#     scripts/generate_published_summary_tables.py, metadata/published_panel_params.json), written
[... 607 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/brudner-2026.yaml paper/10.1073-pnas.2608896123.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "offset": 700,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "SI Appendix\|Supplementary Information\|=== page" paper/10.1073-pnas.2608896123.txt | sed -n '20,80p'
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text read; now the SI Appendix.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2608896123.txt",
 "offset": 1440,
 "limit": 530
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper and SI read. Now I'm checking the figure-derived numbers against the PDF pages.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool python3; python3 -c "import fitz; print(fitz.__doc__)"; grep -n "with_inputs\|elsewhere" docs/protocol.md | head -20
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
227:4. Decide what comes from outside the dataset. Data from elsewhere may be
236:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
237:     `with_inputs` and `elsewhere` claims are counted apart, each group on
261:   - `elsewhere` is for a claim whose data the dataset does not hold at
270:   - The notes of a `with_inputs` claim say which side a difference comes
281:     `data: elsewhere` instead (step 4).
```

**Agent calls Bash**

```bash
cd  sed -n 140,165p docs/protocol.md; sed -n 225,290p docs/protocol.md; python3 -c "import pypdf" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|poppler"
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

### 4. Data from outside the paper's own recordings
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --quiet pymupdf 2>&1 | tail -2; python3 -c "import fitz; print(fitz.__version__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__version__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install pymupdf 2>&1 | tail -3; python3 -c "import pymupdf; print(pymupdf.__version__)"
```

```
Exit code 1

[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf; print(pymupdf.__version__)
    ^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/pylib pymupdf 2>&1 | grep -v notice | tail -3; PYTHONPATH=$TMPDIR/pylib python3 -c "import pymupdf; print(pymupdf.__version__)"
```

```
Successfully installed flatbuffers-25.12.19 networkx-3.7 numpy-2.5.4 onnxruntime-1.31.1 packaging-26.3 protobuf-7.36.2 psutil-7.2.2 pymupdf-2.1 pymupdf-layout-2.1 pymupdf4llm-2.1 pyyaml-6.0.3 tabulate-0.10.0

2.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python3 -c "
import pymupdf,os
t=os.environ['TMPDIR']
d=pymupdf.open('paper/10.1073-pnas.2608896123.pdf')
for p in [3,5,6,7]:
    d[p].get_pixmap(dpi=150).save(f'{t}/main{p+1}.png')
s=pymupdf.open('paper/10.1073-pnas.2608896123.supp-pnas.2608896123.sapp.pdf')
print(len(s))
for p in range(len(s)):
    s[p].get_pixmap(dpi=130).save(f'{t}/si{p+1}.png')
"; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

Rendered the figure pages; checking the bar heights and stars against the recorded values.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main7.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si13.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si14.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python3 -c "
import pymupdf,os
t=os.environ['TMPDIR']
s=pymupdf.open('paper/10.1073-pnas.2608896123.supp-pnas.2608896123.sapp.pdf')
p=s[12]; r=p.rect
clip=pymupdf.Rect(r.width*0.4, r.height*0.08, r.width*0.92, r.height*0.37)
p.get_pixmap(dpi=300, clip=clip).save(f'{t}/s4ef.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s4ef.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si12.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si9.png"
}
```

Result: no output.

**Agent**

Found two real problems so far (the S4 GLM panel contradicts the claim's "every threshold" test, and the 10% gain criterion fails on the paper's own bars). Checking Figs. S1 and S3 next.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si11.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si8.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/si10.png"
}
```

Result: no output.

**Agent**

I have what I need. Applying corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    organization on time averages.\n  depends_on:\n  - fig1il-zscore-reliability",
 "new_string": "    organization on time averages.\n  depends_on:\n  - fig1il-zscore-reliability\n  - figs1-antisymmetry-index"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    intensity scale). Smooth plume resampled from 15 Hz to 60 Hz and to the 0.153 mm grid (SI, Plume\n    movies), frames 300 to 1799; the code keeps two timing profiles, notebook_legacy and corrected,\n    and both are run.",
 "new_string": "    intensity scale). Smooth plume resampled from 15 Hz to 60 Hz and to the 0.153 mm grid (SI, Plume\n    movies); the code keeps two timing profiles, notebook_legacy and corrected, and both are run.\n    The SI gives the 1500-frame window for the complex plume only. For the smooth plume, readings\n    (a) frames 300 to 1799 after resampling (attributed to the code), (b) the first 1500 frames."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  criterion: As the SI (Plume movies) defines it. For each plume and cue, the time-averaged map M\n    (Fig. S1 columns iii and iv, computed as in fig1il-zscore-reliability), its antisymmetric\n    component",
 "new_string": "  criterion: As the SI (Plume movies) defines it. For each plume and cue, the time-averaged map M\n    (Fig. S1 columns iii and iv, the plain temporal mean of the features of\n    fig1il-zscore-reliability, not divided by the SD; the panels are titled <dI/dy>_t and\n    <-dI/dy dI/dt>_t with colour bars in raw units), its antisymmetric component"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    interpolated to 60 Hz as the smooth one (SI). Reproduced when the index rises from 5 to 10 to\n    20 cm/s, the smooth index lies below the 10 cm/s value, and the complex index is the highest of\n    the five; the outcome is the one all readings give.",
 "new_string": "    interpolated to 60 Hz as the smooth one (SI). The centerline row of the three freestream plumes\n    is not stated; read as the row of the source, the row of maximum mean intensity at the upwind\n    edge. Reproduced when the index rises from 5 to 10 to 20 cm/s, the smooth index lies below the\n    10 cm/s value (Fig. S1v places it between the 5 and 10 cm/s points), and the complex index is\n    the highest of the five; the outcome is the one all readings give. s_gradient and s_motion are\n    reported per plume for the Results sentence that gradient antisymmetry stays roughly invariant\n    while motion antisymmetry grows with wind speed."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    eye in the paper; here by their medians over masked pixels. Reproduced when",
 "new_string": "    eye in the paper, which gives no measure of similarity; here by their medians over masked\n    pixels, and the 10% widening below is this file's reading of similar. Reproduced when"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  statement: The spatial organization of the gradient and motion cues in the complex plume stays\n    consistent when sensor spacing is increased from 3 to 12 pixels or the motion delay is lengthened,\n    changing only when sampled more coarsely than the smooth plume.",
 "new_string": "  statement: The spatial organization of the gradient and motion cues in the complex plume stays\n    consistent when sensor spacing is increased from 3 to 12 pixels or the motion delay is lengthened\n    to about 150 ms, changing only when sampled more coarsely than the smooth plume."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    spacings and delays of 1, 2, 4, 8 and 15 frames. Open, with readings named. The reference map,\n    (a) the 3-pixel, 1-frame map, (b) the map at the previous spacing. The legend gives the delays as\n    33 to 500 ms, which is 30 Hz, while the movie is 60 Hz (17 to 250 ms) and the Discussion says 17\n    to about 150 ms; delays are run in frames. No threshold for consistent is given, readings\n    r >= 0.5 and r >= 0.8. Reproduced when the correlations stay at or above the threshold up to 12\n    pixels and 8 frames; the outcome is the one all readings give, and every correlation is\n    reported.",
 "new_string": "    spacings (3, 6, 9 and 12 pixels, the four points of Fig. S1F) and delays of 1, 2, 4, 8 and 15\n    frames. The reference map is the 3-pixel map for the gradient and the 3-pixel, 1-frame map for\n    motion (Fig. S1F axis \"Pearson r vs baseline\"; the outlined baseline cell of Fig. S1G). The\n    legend and the figure label the delays 33 to 500 ms, which is 30 Hz, while the movie is 60 Hz\n    (17 to 250 ms); delays are run in frames. In Fig. S1G the motion r is near 1 for 1, 2 and 4\n    frames at every spacing and drops to about 0.65 at 8 and about 0.35 at 15 frames; Fig. S1F gives\n    a gradient r of about 0.89 at 12 pixels. The Discussion's \"about 150 ms\" matches the 133 ms\n    label of 4 frames, and the smooth plume's 15 Hz sampling is 4 frames at 60 Hz. No threshold for\n    consistent is given; read as r >= 0.8, below every robust value the figure shows. Reproduced when\n    the gradient r is at least 0.8 at every spacing, the motion r is at least 0.8 at every spacing\n    for delays of 1, 2 and 4 frames, and the motion r at 8 and 15 frames is below its 4-frame value\n    at every spacing; every correlation is reported."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    of 1 to 15 frames (SI, Logistic regression models). Reproduced when, in each plume, the mean test\n    AUC at tau = 1 exceeds that at every tau from 2 to 15; partially reproduced in one plume only.",
 "new_string": "    of 1 to 15 frames (SI, Logistic regression models). In the smooth plume Fig. S2C shows the AUC\n    almost flat (about 0.541 at tau 1 to 3, about 0.528 at 15), so a strict ordering at tau 2 is\n    within noise. Reproduced when, in each plume, no tau from 2 to 15 has a mean test AUC above that\n    at tau = 1 by more than the SD over repeats, and the AUC at tau = 15 is below that at tau = 1 by\n    more than that SD; partially reproduced in one plume only. The strict reading (tau = 1 above every\n    other tau) is reported as well."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    sigma[ReLU(f1*L + f2*R + b) - ReLU(f1*R + f2*L + b)] with 30-sample filters, cross-entropy (SI,\n    Artificial neural network model); inputs log(1 + max(I - 5, 0)) (code). The SI gives learning\n    rate 1e-4 (printed garbled), batch 500 and 500 epochs;",
 "new_string": "    sigma[ReLU(f1*L + f2*R + b) - ReLU(f1*R + f2*L + b)] with 30-sample filters, cross-entropy (SI,\n    Artificial neural network model); inputs log(1 + max(I - 5, 0)) (code). The SI gives learning\n    rate 1e-4 (garbled in the text extraction, 10^-4 on the PDF page), batch 500 and 500 epochs;"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    filters have opposite signs over the last 0.1 s with similar time courses, the complex f1 has a\n    negative lobe that follows its positive peak within the last 0.1 s (Fig. S3D), and both AUCs are",
 "new_string": "    filters have opposite signs over the last 0.1 s with similar time courses, the complex f1 has a\n    negative lobe within the last 0.1 s at a longer lag than its weight at the most recent sample,\n    which is positive (delayed, Fig. S3D shows the lobe near -0.02 s), and both AUCs are"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    shown as a variant. No threshold for strongly is given. Reproduced when, for both models, the\n    responses at positive and negative shifts lie on opposite sides of 0.5 and the response to the\n    smooth model with symmetrized filters stays within 0.01 of 0.5 at every shift.",
 "new_string": "    shown as a variant. No threshold for strongly is given. Fig. 3E shows the responses largest at\n    shifts of +1 and -1 frame (about 0.545 and 0.455 smooth, 0.565 and 0.44 complex) and back near\n    0.5 by +/-6 frames, so a test at every shift would fail on the paper's own curves. Reproduced\n    when, for both models, the responses at shifts +1 and -1 lie on opposite sides of 0.5, and the\n    smooth model with symmetrized filters stays within 0.01 of 0.5 at every shift (Fig. S3H is flat\n    at 0.50); the +1 minus -1 difference is reported for each model against the figure's values."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    when the sensitivities hold and an AUC does not.\n- id: fig4ef-agent-success",
 "new_string": "    when the sensitivities hold and an AUC does not. Whether each DNM's AUC exceeds the MNM's of\n    fig3bc-mnm-filters (modestly better) is reported.\n- id: fig4ef-agent-success"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  criterion: The gain is (matched - wind only) / wind only from fig4ef-agent-success, per plume.\n    Tolerance 5 percentage points, wider than the default, as the paper writes \"~10%\" and its own\n    Fig. 4 bars give about 11% (smooth) and 18% (complex). Reproduced when both plumes' gains are\n    within tolerance; partially reproduced when one is.",
 "new_string": "  criterion: The gain is (matched - wind only) / wind only from fig4ef-agent-success, per plume.\n    The paper gives one figure for both plumes; its own Fig. 4 bars give about 11% (smooth) and 18%\n    (complex), so a per-plume test would fail the complex plume on the paper's own numbers. The\n    tested value is the mean of the two plumes' gains (about 14% on the paper's bars). Tolerance 5\n    percentage points, wider than the default, as the paper writes \"~10%\". Reproduced when the mean\n    gain is within tolerance and both gains are positive; partially reproduced when both are positive\n    and the mean is outside tolerance. Each plume's gain is reported."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  criterion: Agents as fig4ef-agent-success, with the symmetric thresholds on P(left) varied; the\n    thresholds tested are not listed and are read from Fig. S4E and S4F. The feature GLM agents use\n    the Fig. 2 combined models. Reproduced when, at every threshold tested, for both agent types and\n    both plumes, the consistent agent's success rate exceeds the inconsistent one's; partially\n    reproduced when it holds at most thresholds.",
 "new_string": "  criterion: Agents as fig4ef-agent-success, with the symmetric thresholds on P(left) varied. The\n    thresholds are not listed in the text; Fig. S4E and S4F plot 11, at 0.05, 0.1 and 0.2 to 0.9 in\n    steps of 0.1, on an axis \"Bilateral Evidence Threshold\", with the Fig. 4 models (P(left)\n    outside 0.4 to 0.6) marked at 0.2. The threshold is therefore read as t on |2 P(left) - 1|, the\n    baseline strategy used when |2 P(left) - 1| <= t. The feature GLM agents use the Fig. 2 combined\n    models. The paper's own Fig. S4F does not bear out \"across thresholds\" for the GLM agents, as the\n    smooth-plume consistent GLM is below the inconsistent one at 0.05, 0.1 and 0.2 and the\n    complex-plume consistent GLM is at or below the inconsistent one at 0.7 to 0.9; Fig. S4E shows\n    the network agents consistent above inconsistent at every threshold in both plumes. Reproduced\n    when the consistent network agent beats the inconsistent one at every threshold in both plumes,\n    and the consistent GLM agent beats the inconsistent one at a majority of thresholds in each plume;\n    partially reproduced when the network part holds at a majority of thresholds only. The GLM\n    thresholds where the order reverses are reported against those of Fig. S4F."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    taken at the last frame at or before 50 ms before turn onset, within one frame (code); onset is\n    the turn event start.",
 "new_string": "    taken at the last frame at or before 50 ms before turn onset, within one frame (code). Onset is\n    the time turn speed crosses 20% of the peak height on the rising edge (SI, Behavioral Analysis);\n    if the dataset's turn event start is defined otherwise, onset is computed from the rotational\n    velocity by that rule. The 200 ms gray boxes of the Fig. 5D legend are read as the 200 ms time\n    constant of the cue smoothing (the panel is labelled tau = 200 ms), not a window average."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  statement: Agents using one fixed rule on time-smoothed gradient and motion cues produce turns that\n    a logistic regression weights more on the gradient in the smooth plume and more on motion in the\n    complex plume, so time integration alone can give the flies' pattern.",
 "new_string": "  statement: Agents using one fixed rule on time-smoothed gradient and motion cues produce turns for\n    which a logistic regression on the local cues weights the gradient more in the smooth than in the\n    complex plume and motion more in the complex than in the smooth plume, and, within each plume,\n    weights the gradient above motion in the smooth plume and motion above the gradient in the\n    complex plume, so time integration could account for the flies' pattern."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  source: Results, Different Directional Odor Cues Predict Fly Crosswind Turning in Different Plume\n    Types, paragraph 5; SI Figure S5F to S5H",
 "new_string": "  source: Results, Different Directional Odor Cues Predict Fly Crosswind Turning in Different Plume\n    Types, paragraph 5; SI Figure S5F to S5H, legend"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "    computed for agents, (a) the Fig. 2 features over the antenna histories, (b) the gradient and\n    motion of the fly analysis (slice slope and cross-correlation offset); the upwind window, 160 to\n    200 degrees as for the flies; the test of the weight difference is not named, read as a Wald test\n    of the difference of the two coefficients. Reproduced when the gradient weight exceeds the motion\n    weight in the smooth plume and the motion weight exceeds the gradient weight in the complex\n    plume, each difference with p < 0.005, under one reading.",
 "new_string": "    computed for agents, (a) the Fig. 2 features over the antenna histories, the main reading, as\n    the SI says \"as described above\" and the fixed weights 2.65 and 0.07 are close to the smooth\n    combined-model weights of Fig. 2D, (b) the gradient and motion of the fly analysis (slice slope\n    and cross-correlation offset); the upwind window, 160 to 200 degrees as for the flies; predictors\n    z-scored per plume as in the fly analysis; the test of the weight difference is not named, read\n    as a Wald test of the difference of the two coefficients. Fig. S5G gives about 0.22 and 0.04\n    (gradient, motion) in the smooth plume and 0.13 and 0.22 in the complex plume. Reproduced when\n    the gradient weight is larger in the smooth than in the complex plume and the motion weight larger\n    in the complex than in the smooth plume (Results, Fig. S5G), and the gradient weight exceeds the\n    motion weight in the smooth plume and the motion weight exceeds the gradient weight in the\n    complex plume, each within-plume difference with p < 0.005 (Fig. S5H), under one reading;\n    partially reproduced when only one of the two comparisons holds."
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71; the paper's training and test arrays were\n    not deposited (code, REPRODUCE_FIGURES_1_3.md)",
 "new_string": "  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71, or as rescaled by the paper if its Yale\n    Dataverse deposit (doi:10.60600/YU/590UBV) holds it; the paper's training and test arrays were\n    not deposited (code, REPRODUCE_FIGURES_1_3.md)"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/brudner-2026.yaml",
 "old_string": "  data: elsewhere\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71\n  expected:",
 "new_string": "  data: elsewhere\n  where: smooth plume from Dryad doi:10.5061/dryad.g27mq71, or as rescaled by the paper if its Yale\n    Dataverse deposit (doi:10.60600/YU/590UBV) holds it\n  expected:"
}
```

```
The file claims/brudner-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  tail -c 300 claims/brudner-2026.yaml; grep -n "^checks" claims/brudner-2026.yaml
```

```
S5G), and the gradient weight exceeds the
    motion weight in the smooth plume and the motion weight exceeds the gradient weight in the
    complex plume, each within-plume difference with p < 0.005 (Fig. S5H), under one reading;
    partially reproduced when only one of the two comparisons holds.
```

**Agent calls Bash**

```bash
cd  cat >> claims/brudner-2026.yaml <<'EOF'
checks:
- date: 2026-11-12
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1eh-snapshot-organization, added figs1-antisymmetry-index to depends_on, as the criterion takes its outcome from that claim too.
  - fig1il-zscore-reliability, the smooth-plume window of frames 300 to 1799 is not in the SI (which gives the window for the complex plume only); named it as open, with the first 1500 frames as the other reading.
  - figs1-antisymmetry-index, M is the plain temporal mean (Fig. S1 columns iii and iv are titled <dI/dy>_t and <-dI/dy dI/dt>_t, with raw-unit colour bars), not the z-score of fig1il; said so. Named the freestream centerline as open, as the paper does not give it. Added reporting of s_gradient and s_motion for the Results sentence on how each changes with wind speed.
  - figs1-temporal-statistics, marked the medians and the 10% widening as this file's reading of similar, since the paper gives no measure.
  - figs1fg-resolution-robustness, the reference map is fixed by Fig. S1F ("Pearson r vs baseline") and the outlined baseline cell of Fig. S1G, so the previous-spacing reading was dropped. The old rule asked for r of at least 0.8 up to 8 frames, but Fig. S1G shows the motion r near 0.65 at 8 frames and 0.35 at 15. Rule now asks for robustness to 4 frames (the Discussion's about 150 ms is the 133 ms label of 4 frames) and a drop at 8 and 15 frames, which is past the smooth plume's 15 Hz sampling. Statement now gives the delay range.
  - figs2c-one-frame-delay, Fig. S2C shows the smooth AUC almost flat over tau 1 to 3, so a strict ordering at tau 2 is within noise. The rule now uses the SD over repeats; the strict reading is still reported.
  - fig3bc-mnm-filters, checked the learning rate on the PDF page (10^-4, garbled only in the extraction). Reworded the delayed negative lobe of f1 as a longer lag than the positive most-recent weight, since "follows its positive peak" could be read either way.
  - fig3e-mnm-motion-response, Fig. 3E responses return to about 0.5 by +/-6 frames, so "opposite sides of 0.5 at positive and negative shifts" read over every shift would fail on the paper's own curves. The rule is now set at shifts +1 and -1, with the figure's values given.
  - fig3ij-dnm-specialization, added reporting of whether the DNM AUCs exceed the MNM AUCs, for "modestly better".
  - discussion-ten-percent-gain, the paper's own Fig. 4 bars give gains of about 11% and 18%, so the per-plume rule would fail the complex plume on the paper's numbers. It now tests the mean of the two gains (about 14% on the bars) and needs both gains positive.
  - figs4-threshold-robustness, read the thresholds off Fig. S4 (0.05, 0.1, 0.2 to 0.9; Fig. 4 models marked at 0.2, so t applies to |2P - 1|). Fig. S4F itself shows the GLM consistent agent below the inconsistent one in the smooth plume at 0.05 to 0.2, and at or below it in the complex plume at 0.7 to 0.9, against the legend's "across thresholds". Rule now asks for every threshold for networks and a majority for GLMs.
  - fig5e-cue-betas, defined turn onset as the SI does (20% of the peak turn speed on the rising edge), not as the dataset's event start. Read the 200 ms gray boxes of Fig. 5D as the smoothing time constant.
  - figs5fh-smoothing-agent, the Results sentence quoted is a cross-plume comparison (Fig. S5G), and the old criterion tested only the within-plume difference (Fig. S5H). Statement and rule now cover both, with the Fig. S5G values. Made the Fig. 2 features the main reading of the agents' cues, since the weights 2.65 and 0.07 match the Fig. 2D smooth weights. Named per-plume z-scoring as a reading.
  - fig2b-smooth-auc and fig2d-smooth-weights, added the paper's own Yale Dataverse deposit as a possible source of the rescaled smooth plume.
  - Checked against the PDF figures and found consistent with the recorded values (no change); Fig. 2B to 2E bars, Fig. 4E and 4F bars and stars, Fig. 5E bars and stars (complex gradient plotted negative, consistent with the plotted sign flip), Fig. 5F, Fig. S5C and S5D-E, Fig. S3E, S3H and S3K, the SI P_upwind formula.
  - Open, not settled from the paper. The code-derived details (frame numbers, filters, turn and position filters, published tables) could not be checked here, as the repository was not read in this check. The Discussion's fivefold spatial range does not match the 3 to 12 pixels (fourfold) of Fig. S1F. The Fig. 4 legend (112 mm) and SI (+/- 83 mm) box widths still conflict. Not given claims, as qualitative and hedged in the paper; the DNM filter shapes of Fig. 3G and 3H, and the S5F success rates of the cue-smoothing agent.
EOF
python tools/claims_check.py claims/brudner-2026.yaml paper/10.1073-pnas.2608896123.txt; grep -n -- "—\|rather" claims/brudner-2026.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/brudner-2026.yaml'));print(len(d['claims']),d['checks'][-1]['ready'])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^checks:/{f=1} f' claims/brudner-2026.yaml | grep -n ': ' | grep -v -E '^\s*[0-9]+:\s*-? ?(date|kind|model|ready|changes):' | head; git status --short claims/
```

```
M claims/brudner-2026.yaml
```

**Agent**

I've checked `claims/brudner-2026.yaml` against the paper, the SI and the rendered figure pages, and corrected it. It is ready for an attempt (`ready: true`).

**Checker result line:** `claims/brudner-2026.yaml: 22 claims, 22 quotes, 4 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **fig1eh-snapshot-organization:** the criterion takes its outcome from two other claims but listed only one, so I added `figs1-antisymmetry-index` to `depends_on`.
- **fig1il-zscore-reliability:** the SI gives the 1500-frame window for the complex plume only. The smooth-plume window is now marked open, with two readings: frames 300 to 1799, or the first 1500 frames.
- **figs1-antisymmetry-index:** the map is the plain time average, as the Fig. S1 iii and iv panel titles and raw-unit colour bars show, not the z-score. The freestream centerline row, which the paper doesn't give, is now marked open. The per-cue scores are now reported.
- **figs1-temporal-statistics:** the comparison by medians and the 10% widening are now marked as this file's reading, since the paper gives no measure of "similar".
- **figs1fg-resolution-robustness:** Fig. S1F and S1G fix the reference map (the baseline), so the other reading is gone. The old rule wanted r ≥ 0.8 up to 8 frames, which fails on the paper's own figure (motion r is about 0.65 at 8 frames). It now asks for robustness up to 4 frames (the Discussion's "about 150 ms") and a drop at 8 and 15 frames, past the smooth plume's 15 Hz sampling.
- **figs2c-one-frame-delay:** Fig. S2C is almost flat for the smooth plume at delays 1 to 3, so the rule now allows for spread over repeats. The strict reading is still reported.
- **fig3bc-mnm-filters:** the PDF confirms the 1e-4 learning rate. I reworded "delayed negative lobe" so it can only mean a longer lag.
- **fig3e-mnm-motion-response:** Fig. 3E is back near 0.5 by ±6 frames, so the rule is now set at shifts of +1 and −1 frame.
- **fig3ij-dnm-specialization:** now reports whether the dense networks beat the minimal ones ("modestly better").
- **discussion-ten-percent-gain:** the paper's own Fig. 4 bars give gains of about 11% and 18%, so the per-plume rule failed the complex plume on the paper's numbers. It now tests the mean of the two gains (about 14% on the bars) and needs both to be positive.
- **figs4-threshold-robustness:** I read the thresholds off Fig. S4 (0.05, 0.1, then 0.2 to 0.9). Fig. S4F itself goes against the legend's "across thresholds" for the GLM agents, in both plumes. The rule now asks for every threshold for the network agents and a majority for the GLM agents.
- **fig5e-cue-betas:** turn onset is now as the SI defines it (20% of peak turn speed on the rising edge). The 200 ms gray boxes in Fig. 5D are read as the smoothing time constant.
- **figs5fh-smoothing-agent:** the quoted Results sentence compares across plumes (Fig. S5G), but the rule only tested within each plume (Fig. S5H). The statement and rule now cover both. The Fig. 2 features are the main reading for the agents' cues, since the weights 2.65 and 0.07 match the Fig. 2D smooth weights.
- **fig2b-smooth-auc and fig2d-smooth-weights:** added the paper's Yale Dataverse deposit as a possible source of the smooth plume.

All other figure-derived expected values and stars match the PDF.

**Still open (recorded in `checks`)**
- I could not check any detail the file attributes to the authors' code (frame numbers, filters, turn and position filters, the published tables), because I didn't have the repository.
- The Discussion says "fivefold" spatial range, but Fig. S1F spans 3 to 12 pixels (fourfold).
- The starting-box width differs: 112 mm in the Fig. 4 legend, ±83 mm in the SI. Both readings are kept.
- Two hedged, qualitative results have no claim: the dense-network filter shapes in Fig. 3G and 3H, and the cue-smoothing agents' success rates in Fig. S5F.

Nothing was committed or pushed. To render the figures I installed PyMuPDF into the temporary directory; nothing else in the repository changed.

## End of run

52 turns, 6 minutes, $2.21 at API prices, result: success.
