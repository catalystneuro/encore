# asari-2009 · claims-check · run 42851897893

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; cat claims/asari-2009.yaml; grep -n -A40 "Reader" docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/asari-2009.yaml"
}
```

```
1	# Claims for Asari & Zador (2009), J Neurophysiol 102:2638-2656, on CRCNS ac-1.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
3	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
4	# files; only its description on crcns.org (paper/ac-1.data-description.txt) was read.
5	#
6	# Text read: the version of record, as a text extraction of the publisher's PDF (PyMuPDF), with
7	# the PDF. The extraction garbles some symbols (Greek letters, "<", ">", "~", "=" and "+/-" print
8	# as a replacement glyph); they were read from context, and quotes are cut around them. The PDF
9	# pages could not be rendered in this run, so figure axes were not read; every value used here is
10	# printed in the text or a legend. The online supplement (Supplemental Figures S1 to S10) was not
11	# supplied and was not read. The main findings rest on the main-text Figures 2 to 9 and their
12	# legends; the supplement holds example traces (S2 to S10) and the "silence probe" analysis (S1),
13	# whose one claim (figs1-silence-probe) is quoted from the Methods only.
14	#
15	# Code read: none. The paper links no code; it says all analysis was done in MATLAB.
16	#
17	# Data the paper used. Long-Evans rats, 20 to 28 days old, anesthetized with ketamine and
18	# medetomidine; in vivo blind patch recordings sampled at 10 kHz.
19	# - A1 current clamp (whole cell): 194 cells in 139 animals, of which 123 met the analysis
20	#   criterion (at least 4 repeats of a probe tested with at least 2 conditioning stimuli). By
[... 658 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/asari-2009.yaml paper/10.1152-jn.00577.2009.txt; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 43,200p docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold. A
data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
documentation) is a longer description, to be read for that alone; it is not
the paper, and no claim comes from it.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; ls papers/datasets/ | grep -i asari; cat papers/datasets/asari-2009.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (21 claims, 0 problems). Reading the rest of the paper now to check each claim.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 800,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.txt",
 "offset": 1600,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "with_inputs\|with_labels" docs/*.md | head -20; grep -rn "checks:" claims/*.yaml | head -3
```

```
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/protocol.md:149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:245:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:276:   - The notes of a `with_inputs` claim say which side a difference comes
claims/alasfour-2024.yaml:645:checks:
claims/andrews-2024.yaml:850:checks:
claims/armstrong-2026.yaml:843:checks:
```

**Agent calls Bash**

```bash
cd  sed -n 236,250p docs/protocol.md; sed -n 645,700p claims/alasfour-2024.yaml
```

```
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
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/ac-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1152-jn.00577.2009.pdf')
for pn in [5,6,9,10,11,13,15]:
  t=d[pn].get_text()
  import re
  for k in ['calculated to be','within','1 �','�1 �','lasted','observed for','80','0.51']:
    pass
print(repr(d[5].get_text()[d[5].get_text().find('calculated to be')-5:d[5].get_text().find('calculated to be')+30]))
t=d[11].get_text(); i=t.find('more than a half'); print(repr(t[i:i+60]))
t=d[11].get_text(); i=t.find('unsatisfactory'); print(repr(t[i:i+30]))
t=d[10].get_text(); i=t.find('lasted'); print(repr(t[i:i+20]))
t=d[14].get_text(); i=t.find('observed for'); print(repr(t[i:i+20]))
t=d[0].get_text(); i=t.find('up to'); print(repr(t[i:i+30]))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftotext pdftoppm mutool; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
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

**Agent**

The text-extraction checks are done; I'm now trying to read the PDF pages directly to settle glyphs the extraction garbles (liquid junction potential sign, "~4 s" and similar).

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00577.2009.pdf",
 "pages": "6-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

PDF pages can't be rendered here (no poppler), so glyphs stay read from context. Applying the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    n: one cell, one probe in three contexts, 6 trials each\n  criterion: The significance measure of the Methods (Kruskal-Wallis across the three contexts at\n    each time point, significant where P < 0.01 holds for at least 50 consecutive 0.1-ms points).\n    The cell and probe are not identified; the author looks for a current-clamp cell with seven\n    natural sound fragments and a probe tested after silence and two other fragments over six\n    trials.",
 "new_string": "    n: one cell, one probe in three contexts (6 repeats shown for one context in Figure 2A)\n  criterion: The significance measure of the Methods (Kruskal-Wallis across the three contexts at\n    each time point, significant where P < 0.01 holds for at least 50 consecutive 0.1-ms points).\n    The cell and probe are not identified; the author looks for a current-clamp cell with seven\n    natural sound fragments and a probe tested after silence and two other fragments, with six\n    repeats in at least one context (the paper gives the repeats of the other two contexts only\n    as at least 4, the analysis rule)."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    proportion at time t is over all 305 probes or over the probes still running at t.\n    Reproduced when",
 "new_string": "    proportion at time t is over all 305 probes or over the probes still running at t. The\n    intersequence silences are not probes here (Methods, Stimulus design, paragraph 2, which\n    leaves the \"silence probe\" periods out of Figure 3). Reproduced when"
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    the natural sound current-clamp data; spontaneous activity is taken from the intersequence\n    intervals, which the paper names as the silent periods. \"Decay\" is not defined;",
 "new_string": "    the natural sound current-clamp data. The paper does not say which period gives the\n    spontaneous activity; the only silences in the design are the intersequence intervals\n    (about 6 s), which are used, whole as the main reading and without their first 1 s as a\n    variant, since the Methods (Stimulus design, paragraph 2) say context effects persist soon\n    after the onset of these intervals and fade within about 1 s. \"Decay\" is not defined;"
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "  - quantity: upper bound on model performance near probe onset (1 minus alpha1)",
 "new_string": "  - quantity: upper bound on model performance near probe onset (1 + alpha1, with alpha1 = -0.49)"
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the STRF absence test, Vjp sign, Figure 8A rules, Figure 7, Figure 9 example and silence-probe criteria.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    formed (contiguous blocks, or by stimulus). \"Did not improve significantly\" names no test;\n    the readings are a paired comparison over cells of validation performance at 4052 ms against\n    180 ms by Wilcoxon signed-rank and a one-way repeated-measures test over the nine windows,\n    each at 0.05. Reproduced when, under one reading, the mean validation performance is at most\n    0.22 at every window for STRF and LN and neither test finds an improvement; the mean training\n    performance and the LN gain are reported.",
 "new_string": "    formed (contiguous blocks, or by stimulus). The paper does not say whether the 20% refers to\n    the validation (lower) or the training (upper) estimate; both are readings. \"Did not improve\n    significantly\" is a claim of absence and the paper names no test; the test fixed here, as an\n    assumption the outcome rests on, is a paired Wilcoxon signed-rank test over the 20 cells of\n    validation performance at 4052 ms against 180 ms, one-sided for an improvement, at 0.05, for\n    STRF and for LN; a Friedman test over the nine windows is shown as a variant and does not\n    decide. Reproduced when, under one reading, the mean performance is at most 0.22 at every\n    window for STRF and LN, and the Wilcoxon test finds no improvement for either; the mean\n    training performance and the LN gain are reported."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    Conductances as in Methods (Eqs. 22 to 29; Vjp -12 mV, Eexc 0 mV, Einh -85 mV, Rs from the\n    median peak transient of the 10 test pulses, Rin from their steady-state current, baseline\n    as the 90th percentile of each trial's current).",
 "new_string": "    Conductances as in Methods (Eqs. 22 to 29; Vjp of 12 mV, Eexc 0 mV, Einh -85 mV, Rs from the\n    median peak transient of the 10 test pulses, Rin from their steady-state current, baseline\n    as the 90th percentile of each trial's current). The sign before 12 mV is garbled in the text\n    extraction; readings are -12 and +12 mV in Eq. 23, a constant offset that shifts V(t) at all\n    three holding potentials alike."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "+ 25 = 110; AM 25 + 71 = 96; FM 25 + 57 = 82; higher-order 63 natural + 74 MCN = 137). Reproduced when all five\n    counts are within tolerance and the order amplitude > frequency, AM > FM > higher-order holds\n    in the proportions; partially reproduced when the order holds and some counts are outside.",
 "new_string": "+ 25 = 110; AM 25 + 71 = 96; FM 25 + 57 = 82; higher-order 63 natural + 74 MCN = 137).\n    Reproduced when all five counts are within tolerance; partially reproduced when some counts\n    are outside but the proportions keep the paper's order amplitude > frequency and AM > FM >\n    higher-order."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    range). Reproduced when the sizes fall in the printed order (amplitude > frequency > AM > FM >\n    higher-order) and at least eight of the ten values are within tolerance; partially\n    reproduced when the order holds.",
 "new_string": "    range). Reproduced when all ten values are within tolerance; partially reproduced when the\n    sizes fall in the printed order (amplitude > frequency > AM > FM > higher-order). The fitted\n    noise floors are reported against the legend's values."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    design, reproduced when at least one has its SD of PSTHs over contexts (Eq. 42) larger in the\n    first bin than in every later bin by at least a factor of two; the fraction of the 93 probes\n    for which this holds is reported.",
 "new_string": "    design, reproduced when at least one has its SD of PSTHs over contexts (Eq. 42) larger in the\n    first bin than in every later bin by at least a factor of two; the fraction of the 93 probes\n    for which this holds is reported. The factor of two is this file's reading of \"substantially\n    different responses were observed only in the first bin\" (Figure 9B legend); the paper gives\n    no threshold."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "contexts in 0.625-2.5, 2.5-10 and 10-40 kHz and a natural sound probe. Reproduced when the\n    significance measure finds a significant period ending later than 3 s after probe onset for\n    the matched probe; not testable when no cell matches.",
 "new_string": "contexts in 0.625-2.5, 2.5-10 and 10-40 kHz and a natural sound probe. Reproduced when the\n    significance measure finds a significant period ending at least 3.6 s after probe onset (4 s\n    less 10%) for the matched probe; not testable when no cell matches."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    probe and the preceding fragment as the context, over the natural sound current-clamp cells.\n    Reproduced when at least one cell has a significant period starting within 0.5 s of the\n    silence onset, and the population proportion of significant silence probes falls to within\n    twice the noise floor by 1 s after onset. The Methods give \"within ~1 s\" for the power\n    (garbled sign read as about).",
 "new_string": "    probe and the preceding fragment as the context, over the natural sound current-clamp cells.\n    The second part concerns power, not significance: during a silence all stimulus-related\n    power (Eq. 17, population average over silence probes) is attributable to the preceding\n    stimulus, which is the main reading; the context-dependent power (Eq. 19) is a variant.\n    Reproduced when at least one cell has a significant period starting within 0.5 s of the\n    silence onset (this file's reading of \"soon after\"), and the power falls below 10% of its\n    value at silence onset by 1.1 s (1 s plus 10%). The Methods give \"within ~1 s\" for the power\n    (garbled sign read as about)."
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "    conductance; not testable when no cell matches. The population claim",
 "new_string": "    conductance; not testable when no cell matches. The time at which each context's mean\n    conductance falls to the noise level is reported against the paper's \"within about 100 ms\".\n    The population claim"
}
```

```
The file claims/asari-2009.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/asari-2009.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-example-long-context. The statistics n said 6 trials in each of three contexts; Figure 2A gives 6 repeats for one context only. Corrected n, and the matching rule now asks for six repeats in at least one context.
  - fig3a-proportion-significant. Added that the intersequence silences are not probes, as the Methods (Stimulus design, paragraph 2) leave them out of Figure 3.
  - timescale-longer-than-membrane. The criterion said the paper names the intersequence intervals as the source of spontaneous activity; it does not. Named the period as open, with the whole interval as the main reading and the interval without its first 1 s as a variant (context effects persist early in the silence, Methods, Stimulus design).
  - fig4-predictability-upper-bound. The quantity label said 1 minus alpha1 while the criterion and the legend (alpha1 = -0.49, kappa = 1) give 1 + alpha1; made the label agree.
  - fig4-strf-performance-low. A claim of absence is judged on one test, not on several readings (protocol, step 3); fixed one test (paired one-sided Wilcoxon, 4052 against 180 ms, validation, 0.05) as an assumption, with the Friedman test as a variant. Named as open whether the 20% refers to the validation or the training estimate.
  - fig5-example-conductances. The sign of the liquid junction potential is garbled in the text extraction; the criterion had fixed it at -12 mV. Named both signs as readings. Added that the decay of the conductances within about 100 ms, stated in the claim, is reported.
  - fig8a-proportion-by-property. Removed the order of the five proportions from the condition for reproduced; the paper reports counts, not an order. The order stays for partial.
  - fig8a-significance-fits. Removed the rule that eight of ten values suffice; the paper gives no such threshold, so all ten must be within tolerance. Fitted noise floors are reported.
  - fig7-example-frequency-context. The cutoff of 3 s for "about 4 s" had no reason; set to 3.6 s (4 s less 10%, the protocol's default tolerance).
  - fig9-example-first-bin. Said that the factor of two is this file's reading of "substantially different", not the paper's.
  - figs1-silence-probe. The second part tested the proportion of significant silence probes, while the Methods' 1 s statement is about response power attributable to the preceding stimulus; now tested on power (Eq. 17 over silence probes, Eq. 19 as variant), falling below 10% of its onset value by 1.1 s. Said that 0.5 s for "soon after" is this file's reading.
  - Open. The online supplement (Supplemental Figures S1 to S10) was not supplied; figs1-silence-probe is written from the Methods alone and its measure and numbers are unknown. The main findings rest on the main text and do not need it.
  - Open. The PDF could not be rendered in this run either, so garbled symbols (signs, "~" against "<" or ">", as in "lasted ~4 s", "within ~100 ms", "(~20%)" and the Vjp sign) are read from context.
  - Open. Several grading thresholds are this file's where the paper gives none (partial rules in a1-mgb-firing-rates, fig3a-significance-decay, fig8b-decay-by-property; the 1/e lag and 150 ms in timescale-longer-than-membrane; the 25% plateau and "below 0.1 s" in fig9-mgb-fast-decay; non-overlapping intervals in fig8c-relative-effects); each criterion says so or gives a reason.
  - Open. The Results remark that the STRFs showed no distinct structure longer than several hundred milliseconds (Relation to response predictability, paragraph 5) has no claim; it is a qualitative side remark, not a main finding.
EOF
python tools/claims_check.py claims/asari-2009.yaml paper/10.1152-jn.00577.2009.txt; grep -n ": " claims/asari-2009.yaml | grep -v "^\s*[0-9]*:\s*#" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/asari-2009.yaml",
 "old_string": "concerns power, not significance: during",
 "new_string": "concerns power, not significance. During"
}
```

```
The file claims/asari-2009.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/asari-2009.yaml paper/10.1152-jn.00577.2009.txt; python -c "
import yaml,re
d=yaml.safe_load(open('claims/asari-2009.yaml'))
print(len(d['claims']), d['checks'][-1]['ready'], len(d['checks'][-1]['changes']))
"; grep -nE "—|rather" claims/asari-2009.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

**Checker result:** `claims/asari-2009.yaml: 21 claims, 19 quotes, 2 statistical values, 0 problems`. It passed before my edits and passes after them.

**Changes, by claim** (each is recorded with its reason under `checks`):
- **fig2-example-long-context:** `n` said 6 trials in each of three contexts. Figure 2A gives 6 repeats for one context only, so I corrected `n` and the rule for matching the example cell.
- **fig3a-proportion-significant:** Added that the intersequence silences are not probes; the Methods leave them out of Figure 3.
- **timescale-longer-than-membrane:** The criterion said the paper names the intersequence intervals as the source of spontaneous activity. It does not, so that is now named as open. The main reading uses the whole interval; a variant drops its first 1 s.
- **fig4-predictability-upper-bound:** The quantity label said "1 minus alpha1". With alpha1 = -0.49 the value is 1 + alpha1, so I made the label agree with the criterion and the legend.
- **fig4-strf-performance-low:** The paper names no test for this claim of absence, and the protocol judges absence on one test, not on several readings. I fixed one test as an assumption: a paired one-sided Wilcoxon on validation performance, 4052 ms against 180 ms, at 0.05. The Friedman test is shown as a variant. It is now named as open whether "20%" means the validation or the training estimate.
- **fig5-example-conductances:** The sign of the 12 mV liquid junction potential is garbled in the text. The criterion had fixed it at -12 mV; both signs are now readings. The decay of the conductances within about 100 ms, which the statement claims, is now reported.
- **fig8a-proportion-by-property:** Removed the order of the proportions from the condition for "reproduced". The paper reports counts, not an order. The order still applies for "partially reproduced".
- **fig8a-significance-fits:** Removed the rule that 8 of 10 values within tolerance is enough, which the paper does not give. All 10 must now be within tolerance.
- **fig7-example-frequency-context:** The 3 s cutoff for "about 4 s" had no reason given. It is now 3.6 s (4 s less the default 10%).
- **fig9-example-first-bin:** Said that the factor of two is this file's reading of "substantially different", not the paper's.
- **figs1-silence-probe:** The Methods' "within about 1 s" refers to response power, but the criterion tested the proportion of significant probes. It now tests power: Eq. 17 over silence probes, with Eq. 19 as a variant.

**What remains open:**
- The online supplement (Figures S1 to S10) was not supplied, so figs1-silence-probe is written from the Methods only. The main findings do not depend on the supplement.
- I could not render the PDF either, because no PDF renderer is installed here. Garbled symbols ("~", "<" or ">", the sign of the junction potential) are read from context.
- Several grading thresholds are the file's own choices where the paper gives none. Each criterion says so or gives a reason.
- One side remark has no claim: the paper says the STRFs showed no distinct structure longer than several hundred milliseconds. It is not a main finding.

The paper's main findings all have claims, and nothing comes from outside this paper.

**Ready:** yes (`ready: true`). Only `claims/asari-2009.yaml` was changed; nothing is committed or pushed.

## End of run

30 turns, 4 minutes, $1.55 at API prices, result: success.
