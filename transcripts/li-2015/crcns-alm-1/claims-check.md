# crcns-alm-1 · claims-check · run 42414234385

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/crcns-alm-1/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,220p docs/protocol.md
```

```
better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
     finding.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-alm-1/10.1038-nature14178.yaml paper/10.1038-nature14178.txt; cat claims/crcns-alm-1/10.1038-nature14178.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml"
}
```

```
1	# Claims for Li, Chen, Guo, Gerfen & Svoboda (2015), Nature 519, 51-56, "A motor cortex circuit for
2	# motor planning and movement", doi:10.1038/nature14178, on CRCNS data set alm-1
3	# (doi:10.6080/K0RF5RZT).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record, as text extracted from the PDF supplied under paper/ (main
8	# text, Methods, legends of Figures 1 to 5 and Extended Data Figures 1 to 7). The paper has no
9	# separate Supplementary Information. The extraction prints "=" as "5", "<" as ",", ">" as ".",
10	# "±" as "6" and a minus sign as "2"; quotes keep these glyphs as printed. PDF pages 2, 3 and 5
11	# were opened to read Fig. 1d, 2c, 2d, 3e, 3f, 3i and 5b, which the text garbles.
12	#
13	# Code. The paper links no analysis code. The data set's description says it holds MATLAB scripts;
14	# they are files of the data set and were not read. Every method below is from the paper's text.
15	#
16	# Data the paper used. 52 mice (age > P60). Behaviour, whisker-based object location
17	# discrimination, head-fixed (n = 42 mice in the Results): pole at an anterior (lick left) or
18	# posterior (lick right) position; sample epoch 1.3 s from pole movement onset to 0.1 s after pole
19	# retraction onset; delay epoch 1.3 s; auditory go cue (3.4 kHz, 0.1 s); response by licking one of
20	# two lickports; licks before the cue are "lick early" trials. Photoinhibition of ALM (Fig. 1), 5
[... 704 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.txt",
 "offset": 942
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (29 claims, 0 problems). Now I'm checking the figure-derived values (star placement in Fig. 1d and 5b, bars in Fig. 2d and 3e/i) against the PDF.

**Agent calls Bash**

```bash
cd  python -c "
import fitz,os
d=fitz.open('paper/10.1038-nature14178.pdf')
for i in [1,2,4,14]:
    p=d[i]; pix=p.get_pixmap(dpi=150); pix.save(os.environ['TMPDIR']+f'/p{i+1}.png')
print(len(d))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; python -c "import pypdfium2" 2>&1; ls .venv 2>/dev/null | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent**

Read can show PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.pdf",
 "pages": "2-3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.pdf",
 "pages": "5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.pdf",
 "pages": "15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  pip install --quiet pymupdf 2>&1 | tail -2; python -c "import fitz; print(fitz.__doc__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd  pip install pymupdf 2>&1 | tail -3; pip show pymupdf 2>&1|head -3; which python pip
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
WARNING: Package(s) not found: pymupdf
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
```

**Agent calls Bash**

```bash
cd  pip install --target "$TMPDIR/pylib" pymupdf 2>&1 | grep -v notice | tail -3; PYTHONPATH=$TMPDIR/pylib python -c "import fitz; print('ok')"
```

```
Successfully installed flatbuffers-25.12.19 networkx-3.7 numpy-2.5.4 onnxruntime-1.31.1 packaging-26.3 protobuf-7.36.2 psutil-7.2.2 pymupdf-2.1 pymupdf-layout-2.1 pymupdf4llm-2.1 pyyaml-6.0.3 tabulate-0.10.0

/tmp/claude-1001/pylib/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
ok
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf,os
d=pymupdf.open('paper/10.1038-nature14178.pdf')
print(len(d))
for i in [1,2,4,14,9]:
    d[i].get_pixmap(dpi=200).save(os.environ['TMPDIR']+f'/p{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.png"
}
```

Result: no output.

## Prompt

[Image: original 1654x2174, displayed at 1522x2000. Multiply coordinates by 1.09 to map to original image.]

**Agent**

Fig. 1d stars and Fig. 2d bars match the file (the text and Fig. 2d swap the 389/304 labels, and the file already records that). Checking Fig. 3 and Fig. 5 next.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Message**

[Image: original 1654x2174, displayed at 1522x2000. Multiply coordinates by 1.09 to map to original image.]

**Agent**

Fig. 3e matches, but Fig. 3i (IT) reads about 0.22, 0.56, 0.22, not the 0.2, 0.65, 0.15 in the file. The Fig. 3j inset reads about 0.45, not 0.5. Checking Fig. 5 and ED Fig. 6.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p15.png"
}
```

Result: no output.

**Message**

[Image: original 1654x2174, displayed at 1522x2000. Multiply coordinates by 1.09 to map to original image.]

Result: no output.

**Message**

[Image: original 1654x2174, displayed at 1522x2000. Multiply coordinates by 1.09 to map to original image.]

**Agent**

Fig. 5b stars match the file. ED Fig. 6b plots PT powers of 0.12, 0.24 and 0.8 mW only, so the 0.06 mW in the ed6b criterion is wrong. Applying corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    trials; control (unstimulated) trials only. Reproduced",
 "new_string": "    trials. Which trials enter is also open (the paper does not say whether photostimulation\n    trials are left out); readings, control (unstimulated) trials only, or all trials. Reproduced"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    open (readings, at least 1, or at least 5, of each type). Reproduced when r is negative with\n    P < 0.05 in all three epochs under one reading; partially reproduced for one or two epochs.\n    The fraction of neurons whose error selectivity has the sign opposite to their correct\n    selectivity is reported.",
 "new_string": "    open (readings, at least 1, or at least 5, of each type). The paper gives r but no test of it;\n    a two-sided test of Pearson's r at P < 0.05 is a standard choice. The \"majority\" is the\n    fraction of neurons whose error selectivity has the sign opposite to their correct\n    selectivity. Reproduced when r is negative with P < 0.05 and that fraction exceeds one half\n    in all three epochs under one reading; partially reproduced for one or two epochs."
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    no sentence prints them. Preference is from total spike counts across the three epochs, lick\n    right against lick left (Methods). A claim",
 "new_string": "    no sentence prints them. Preference for Fig. 2e is from total spike counts across the three\n    epochs, lick right against lick left (Methods); the Fig. 2c sort may instead use the\n    preferred type set from 10 trials (Methods, \"To compute selectivity (Fig 2c)\"). Readings for\n    the counts, (a) total spike counts over all correct trials, (b) the 10-trial split. A claim"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    pyramidal neurons, same window. Reproduced when the test is not significant under the\n    readings; not reproduced when it is.",
 "new_string": "    pyramidal neurons, same window; (c) all 1,408 units, same window, as ED Fig. 1 shows FS and\n    pyramidal neurons. Reproduced when the test is not significant under every reading; not\n    reproduced when it is significant under every reading."
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "  - quantity: PT mean jitter\n    value: 0.1\n    tolerance: 0.01\n    unit: ms\n  - quantity: IT mean jitter\n    value: 0.2\n    tolerance: 0.02",
 "new_string": "  - quantity: PT mean jitter\n    value: 0.1\n    tolerance: 0.05\n    unit: ms\n  - quantity: IT mean jitter\n    value: 0.2\n    tolerance: 0.05"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    10% for the jitter values; a jitter value counts as matching when it rounds to the printed\n    value.",
 "new_string": "    10% for the PT and IT jitter values; their tolerance is 0.05 ms, half the last printed\n    digit, so a value matches when it rounds to the printed value."
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "Fig. 3i about 0.2, 0.65 and\n    0.15 for IT",
 "new_string": "Fig. 3i about 0.22, 0.56 and\n    0.22 for IT"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "(Fig. 3f inset reads about 0.7, Fig. 3j\n    about 0.5).",
 "new_string": "(Fig. 3f inset reads about 0.65, Fig. 3j\n    about 0.45)."
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    n: 45 PT neurons\n  - about: IT neurons, more contra-preferring\n    test: one-tailed test, bootstrap\n    p: 0.74\n    n: 27 IT neurons",
 "new_string": "    n: PT neurons (45 tagged; whether all or only the selective ones enter is not stated)\n  - about: IT neurons, more contra-preferring\n    test: one-tailed test, bootstrap\n    p: 0.74\n    n: IT neurons (27 tagged; whether all or only the selective ones enter is not stated)"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    types at P < 0.05), layer 5 (450 to 700 um). Reproduced",
 "new_string": "    types at P < 0.05), layer 5 (450 to 700 um). Contra or ipsi preference is from the average\n    calcium signal during the trial epochs (Results, A movement command emerges in the pyramidal\n    tract neurons, paragraph 3); how the epochs are combined is open. Reproduced"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    over mice, the performance change on the contralateral-bias trial type at each average power\n    (0.06, 0.12, 0.24, 0.8 mW). Reproduced",
 "new_string": "    over mice, the performance change on the contralateral-bias trial type at each average power\n    plotted in ED Fig. 6b (0.12, 0.24, 0.8 mW; not every mouse was tested at every power, and\n    only one at 0.8 mW). Reproduced"
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-alm-1/10.1038-nature14178.yaml",
 "old_string": "    outnumber ipsilateral licks during stimulation for both lines, and vM1 stimulation produces\n    no increase in lick rate over baseline (n = 8 trained mice, n = 6 untrained mice, ED Fig. 3e,\n    f legends).",
 "new_string": "    outnumber ipsilateral licks during stimulation for both lines, the fraction of stimulation\n    trials with early (premature) licks in trained mice and with licking in untrained mice is\n    above zero at high power, and vM1 stimulation produces no increase in lick rate over\n    baseline (n = 8 trained mice, n = 6 untrained mice, ED Fig. 3e, f legends). The paper gives\n    no test for these; the comparisons are read from ED Fig. 3e, f."
}
```

```
The file claims/crcns-alm-1/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'echo {}; sed -n "/^checks:/,\$p" {} | head -15'
```

```
claims/000005/10.1038-nn.4412.yaml
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
claims/000006/10.1038-s41586
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/crcns-alm-1/10.1038-nature14178.yaml <<'EOF'
checks:
- date: 2026-11-07
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - task-performance. The criterion fixed control trials only; the paper does not say which trials the 78.4% uses. Named it open, with readings control trials only or all trials.
  - ed2-error-trials-predict-choice. The criterion required P < 0.05 for r, which the paper does not report; now marked as a standard choice. The statement's "majority" was only reported; the fraction of neurons switching sign must now exceed one half, as the ED Fig. 2c legend says.
  - fig2e-equal-contra-ipsi. The counts 427 and 485 come from the Fig. 2c sort, which the Methods may base on the 10-trial preferred type, while Fig. 2e uses total spike counts. Named both as readings.
  - ed1-no-population-contra-bias. Added reading (c), all 1,408 units, since ED Fig. 1 shows FS and pyramidal neurons and the text says "the recorded population"; said the outcome must hold under every reading, as for a claim of absence.
  - antidromic-latency-jitter. The expected tolerances for PT and IT jitter (0.01, 0.02 ms) contradicted the criterion's rounding rule; set to 0.05 ms, half the last printed digit, to match it.
  - fig3ei-both-types-preparatory-and-movement. The Fig. 3i fractions were misread (0.2, 0.65, 0.15); the PDF shows about 0.22, 0.56, 0.22.
  - fig3fj-contra-preferring-pt-not-it. The inset fractions read about 0.65 (Fig. 3f) and 0.45 (Fig. 3j), not 0.7 and 0.5. The n fields gave 45 and 27 neurons although which neurons enter the bootstrap is open; reworded.
  - fig4h-imaging-pt-contra-bias. Added how imaging preference is set (average calcium signal during the trial epochs, Results), with how epochs combine named as open.
  - ed6b-pt-dose-response. The criterion listed 0.06 mW, which ED Fig. 6b does not plot for PT neurons; the powers are 0.12, 0.24 and 0.8 mW, and not every mouse was tested at each.
  - ed3-high-power-contralateral-licking. The criterion left out two parts of the statement, licking in untrained mice and premature licks in trained mice; added them, and said the paper gives no test.
  - Open, not settled. fig2d-response-categories. The text (389 peri-movement only, 304 both) and Fig. 2d (about 0.43 both, 0.33 peri-movement only) disagree; confirmed from the PDF; the criterion keeps both readings.
  - Open, not settled. fig5-pt-activation-contralateral-bias. Results define subthreshold as < 0.25 mW, yet the Fig. 5 legend pools 0.12 to 0.8 mW and ED Fig. 3 calls 0.8 mW high power. The criterion follows the legend; a run limited to 0.12 and 0.24 mW is a variant.
  - Open, not settled. fig2c-dynamic-single-neurons. The 0.5 bound on the population response correlation is read from Fig. 2c and remains an assumption; the paper gives no threshold.
EOF
python tools/claims_check.py claims/crcns-alm-1/10.1038-nature14178.yaml paper/10.1038-nature14178.txt | head -5; grep -nP "—|rather|[^\"]: [^ ]" claims/crcns-alm-1/10.1038-nature14178.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file was mostly sound. I made ten corrections, three problems are still open, and the file is ready for an attempt.

**Checker result:** `29 claims, 29 quotes, 18 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

I checked the values read from figures against PDF pages 2, 3, 5 and 15. To see the pages I installed PyMuPDF into `$TMPDIR`, outside the repo. The stars in Fig. 1d and Fig. 5b, the bars in Fig. 2d and 2e, the 427/485 axis counts and the Fig. 3e fractions all match the file.

**Changes, by claim:**
- **task-performance:** The file used control trials only, but the paper doesn't say which trials the 78.4% comes from. I listed both readings: control trials only, or all trials.
- **ed2-error-trials-predict-choice:** The criterion required P < 0.05 for r, which the paper doesn't report; it is now labelled a standard choice. The statement's "majority" is now part of the test: more than half of neurons must switch the sign of their selectivity, as the ED Fig. 2c legend says.
- **fig2e-equal-contra-ipsi:** The counts 427 and 485 come from the Fig. 2c sort, which may use the preferred trial type taken from 10 trials. Fig. 2e uses total spike counts. Both are now listed as readings.
- **ed1-no-population-contra-bias:** I added a third reading, all 1,408 units, since ED Fig. 1 shows both cell classes. The criterion now says the result must hold under every reading.
- **antidromic-latency-jitter:** The PT and IT jitter tolerances (0.01 and 0.02 ms) contradicted the criterion's own rounding rule. Both are now 0.05 ms.
- **fig3ei:** The IT fractions in Fig. 3i were misread as 0.2, 0.65 and 0.15. The figure shows about 0.22, 0.56 and 0.22.
- **fig3fj:** The inset fractions are about 0.65 (Fig. 3f) and 0.45 (Fig. 3j), not 0.7 and 0.5. The `n` fields now say it is open which neurons enter the bootstrap.
- **fig4h:** I added how the paper sets preference in the imaging data (average calcium signal during the trial epochs). How the epochs are combined is named as open.
- **ed6b-pt-dose-response:** The criterion listed 0.06 mW, which ED Fig. 6b does not plot for PT neurons. The powers are 0.12, 0.24 and 0.8 mW, and not every mouse was tested at each.
- **ed3-high-power-contralateral-licking:** The criterion left out two parts of the statement: licking in untrained mice and premature licks in trained mice. I added both and noted that the paper gives no test for them.

**Still open (recorded in `checks`):**
- **fig2d:** The text says 389 neurons are peri-movement only and 304 have both; Fig. 2d shows the reverse. The PDF confirms the disagreement, and the criterion keeps both readings.
- **fig5:** The Results define subthreshold power as below 0.25 mW, but the Fig. 5 legend pools 0.12 to 0.8 mW, and ED Fig. 3 calls 0.8 mW high power. The criterion follows the legend.
- **fig2c-dynamic-single-neurons:** The 0.5 bound on the population response correlation is read off the figure and remains an assumption.

**Coverage:** Every main finding has a claim, and none comes from outside the paper. The data descriptor is used only to describe the dataset.

**Ready:** yes. The `checks` entry is appended with `ready: true`. Only `claims/crcns-alm-1/10.1038-nature14178.yaml` changed, and nothing is committed.

## End of run

38 turns, 3 minutes, $1.40 at API prices, result: success.
