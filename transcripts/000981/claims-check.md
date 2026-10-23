# 000981 · claims-check · run 39868229468

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000981/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md; python tools/claims_check.py claims/000981/10.1016-j.cub.2026.08.040.yaml paper/10.1016-j.cub.2026.08.040.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/000981/10.1016-j.cub.2026.08.040.yaml
```

```
<persisted-output>
Output too large (36.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/83578f20-6f4d-4787-b929-0e9e87dc0b07/tool-results/b10x9oqhj.txt

Preview (first 2KB):
# Claims for Seyedolmohadesin et al. (2026), "Whole-brain chemosensory responses of both C. elegans
# sexes", Current Biology 36, 4803-4816, on dandiset 000981.
#
# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions),
# 2026-10-22, protocol pilot-10 as stated in docs/protocol.md. No data of the dandiset were seen;
# only its title and description on the archive ("Datasets for the Current Biology paper", 47 assets).
#
# Text read. The version of record (PDF supplied by a person, text extracted with PyMuPDF), in
# paper/10.1016-j.cub.2026.08.040.txt: main text, STAR Methods, and the supplement's Figures S1 to
# S20 with their legends. Data S1 to S4 (spreadsheets behind Figures 2 to 5) and Videos S1 and S2
# are not in the text. No figure was read from the PDF (no renderer was available).
#
# Code read. https://github.com/venkatachalamlab/whole-brain-chemosensory-responses at commit
# b0dbdbf50c579d056d7991b7612fcff30091ffbd (1 June 2025). This is tag 1.0.0, which is the Zenodo
# record the key resources table cites (10.5281/zenodo.21479592). It holds compile_all_traces.ipynb
# (traces to per-presentation responses, and the band-passed traces for correlations), the figure
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/83578f20-6f4d-4787-b929-0e9e87dc0b07/tool-results/b10x9oqhj.txt"
}
```

```
1	# Claims for Seyedolmohadesin et al. (2026), "Whole-brain chemosensory responses of both C. elegans
2	# sexes", Current Biology 36, 4803-4816, on dandiset 000981.
3	#
4	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions),
5	# 2026-10-22, protocol pilot-10 as stated in docs/protocol.md. No data of the dandiset were seen;
6	# only its title and description on the archive ("Datasets for the Current Biology paper", 47 assets).
7	#
8	# Text read. The version of record (PDF supplied by a person, text extracted with PyMuPDF), in
9	# paper/10.1016-j.cub.2026.08.040.txt: main text, STAR Methods, and the supplement's Figures S1 to
10	# S20 with their legends. Data S1 to S4 (spreadsheets behind Figures 2 to 5) and Videos S1 and S2
11	# are not in the text. No figure was read from the PDF (no renderer was available).
12	#
13	# Code read. https://github.com/venkatachalamlab/whole-brain-chemosensory-responses at commit
14	# b0dbdbf50c579d056d7991b7612fcff30091ffbd (1 June 2025). This is tag 1.0.0, which is the Zenodo
15	# record the key resources table cites (10.5281/zenodo.21479592). It holds compile_all_traces.ipynb
16	# (traces to per-presentation responses, and the band-passed traces for correlations), the figure
17	# notebooks Fig2&3_prepare_data, Fig2B-E&Fig3, Fig4_prepare_data, Fig4, Fig5 and FigS2 (the drop
18	# tests), config.py (stimulus names, onset frames, which of the 47 recordings are male) and
19	# datasets.json (47 recordings, 22 hermaphrodites and 25 males). It does not hold the files it reads:
20	# neurons/neuron_classes.json (the neuron classes and their layer), the metadata spreadsheet
[... 531 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n -i "STAR\|^Results\|^Discussion\|Figure S[0-9]*\.\|^Figure [0-9]\." paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "offset": 1024,
 "limit": 530
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python -c "
import fitz
d=fitz.open('10.1016-j.cub.2026.08.040.pdf')
for pn in [5,6,8,9]:
  for b in d[pn].get_text('blocks'):
    t=b[4].strip().replace('\n',' ')
    print(pn+1, round(b[0]),round(b[1]), t[:90])
" 2>&1 | head -120
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

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
 "file_path": "paper/10.1016-j.cub.2026.08.040.pdf",
 "pages": "6-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "# outlier rule. Two readings are run: (a) the Methods' rule alone; (b) the code's filters as well, as\n# far as the dandiset carries identification confidence and ignored ranges (the author says which).",
 "new_string": "# outlier rule. Two readings are run: (a) the Methods' rule alone; (b) the code's filters as well, as\n# far as the dandiset carries identification confidence and ignored ranges (the author says which).\n# These are readings of a method detail, so a claim's outcome is the one both give; when they give\n# different outcomes the claim is blocked as methods_underspecified, with both results shown."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "# per-animal values. Functional dimorphism is |mean herm - mean male|.",
 "new_string": "# per-animal values. Functional dimorphism is |mean herm - mean male|. Reading (b) follows the\n# Methods (\"Each pairwise correlation was then averaged across all individuals\"); the code's outlier\n# removal and pooling are not in the Methods, so (b) decides the outcome and (a) is a variant\n# (docs/protocol.md, Reader, step 2).\n#\n# READINGS. Where a criterion lists readings of what a statement or reported number means (which\n# window a legend means, what \"almost all\" is), the claim holds under any of them. Where the readings\n# are choices of method (EXCLUSION (a) and (b), the OPEN details of motor state), the outcome is the\n# one they all give, and the claim is blocked as methods_underspecified when they differ."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    removes them). Reproduced when the count is within tolerance under an exclusion reading.",
 "new_string": "    removes them). Reproduced when the count is within tolerance under both exclusion readings\n    (opening comment, EXCLUSION)."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    both exclusion readings. Reproduced when the count is within tolerance under one reading.",
 "new_string": "    both exclusion readings. Reproduced when the count is within tolerance under (a) or (b), with\n    both exclusion readings giving that outcome."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    comment, CLASSES). Reproduced when all eight counts are within tolerance under one reading;\n    partially reproduced when six or seven are.",
 "new_string": "    comment, CLASSES). Reproduced when all eight counts are within tolerance under reading (a) or\n    (b) of fig5b-dimorphic-classes; partially reproduced when six or seven are. Both exclusion\n    readings must give the outcome (opening comment, READINGS)."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  criterion: CORRELATION, both readings, over the pairs of the 110 subclasses with stimuli left out\n    (code Fig4.ipynb, no_odor_score_df); R2 of an ordinary least-squares line (scipy linregress, as\n    the code). Reproduced when R2 is within tolerance under one reading.",
 "new_string": "  criterion: CORRELATION over the pairs of the 110 subclasses with stimuli left out (code Fig4.ipynb,\n    no_odor_score_df); R2 of an ordinary least-squares line (scipy linregress, as the code).\n    Reproduced when R2 is within tolerance under CORRELATION reading (b), the Methods'; reading (a),\n    the code's, is shown as a variant."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    exceeds the interneuron and the motor value under both readings and both CORRELATION readings.",
 "new_string": "    exceeds the interneuron and the motor value under both readings, with CORRELATION reading (b);\n    CORRELATION reading (a) is a variant."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    pairs\"). \"Almost all\" is read as (a) at least 95% or (b) at least 99% of pairs. Reproduced when\n    one reading holds under a CORRELATION reading; the fraction is reported.",
 "new_string": "    pairs\"). \"Almost all\" is read as (a) at least 95% or (b) at least 99% of pairs. Reproduced when\n    one reading holds under CORRELATION reading (b); the fraction is reported, and also under\n    CORRELATION reading (a) as a variant."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    one reading holds under CORRELATION reading (b); the fraction is reported, and also under\n    CORRELATION reading (a) as a variant.",
 "new_string": "    one reading holds under CORRELATION reading (b); the fraction is reported under both CORRELATION\n    readings, (a) as a variant."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent**

Now the statistics entries and monomorphic criteria.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  statistics:\n  - about: dimorphism of AWA and AWB onset responses to osmotic stress\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window, 800 mM sorbitol. Reproduced when AWA and AWB\n    have p <= 0.05 and ASER and ASH have p > 0.05 (the absence is judged on the same test). The four\n    p-values and normalized differences are reported, under both exclusion readings.",
 "new_string": "  criterion: DIMORPHISM, representation 1, onset window, 800 mM sorbitol. Reproduced when AWA and AWB\n    have p <= 0.05, and ASER and ASH have p > 0.05 (the absence is judged on the same test) and are\n    responsive to sorbitol at onset (RESPONSIVE, in at least one sex), since Figures 3 and 5 count a\n    class as monomorphic only when it responds. The four p-values and normalized differences are\n    reported, under both exclusion readings."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    windows for BAG. Reproduced when, under one reading, AWA has p <= 0.05 and BAG with 1e-2 isoamyl\n    alcohol has p > 0.05.",
 "new_string": "    windows for BAG. Reproduced when, under one reading, AWA has p <= 0.05 and BAG with 1e-2 isoamyl\n    alcohol has p > 0.05 and is responsive to it in the same window (RESPONSIVE, in at least one\n    sex), since Figures 3 and 5 count a class as monomorphic only when it responds."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  statistics:\n  - about: dimorphism of the ASH response to high salt\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window (the text cites Figure 3A, onset). Reproduced\n    when ASH has p <= 0.05 for 450 mM NaCl and p > 0.05 for sorbitol and for CuSO4.",
 "new_string": "  criterion: DIMORPHISM, representation 1, onset window (the text cites Figure 3A, onset). Reproduced\n    when ASH has p <= 0.05 for 450 mM NaCl, and p > 0.05 for sorbitol and for CuSO4 while responsive\n    to each at onset (RESPONSIVE, in at least one sex; monomorphic as in Figures 3 and 5)."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  statistics:\n  - about: dimorphism of the ASER response to low salt\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window (Figure 3A), ASER alone. Reproduced when the\n    100 mM NaCl response has p <= 0.05 and the 450 mM NaCl response p > 0.05.",
 "new_string": "  criterion: DIMORPHISM, representation 1, onset window (Figure 3A), ASER alone. Reproduced when the\n    100 mM NaCl response has p <= 0.05, and the 450 mM NaCl response has p > 0.05 while responsive at\n    onset (RESPONSIVE, in at least one sex; monomorphic as in Figures 3 and 5)."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  statistics:\n  - test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, class I2.",
 "new_string": "  criterion: DIMORPHISM, representation 1, class I2."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent**

Now ADF/M2 direction, fig4f, fig4g, connectome readings.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    and not the other in each sex, with the cues opposite between sexes; (b) DIMORPHISM gives p <=\n    0.05 for both cues in each of ADF and M2. Reproduced",
 "new_string": "    and not the other in each sex, with the cues opposite between sexes; (b) DIMORPHISM gives p <=\n    0.05 for both cues in each of ADF and M2, in the direction of a switch (for ADF the absolute\n    mean response to OP50 larger in hermaphrodites and to ascr#3 larger in males; for M2 the larger\n    sex opposite between the two cues), since a dimorphism without direction does not test the\n    switch the statement names. Reproduced"
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    Reproduced when more than half of the 36 and of the six have no functional dimorphism under one\n    reading; their mean r per sex is reported.",
 "new_string": "    Reproduced when more than half of the 36 and of the six have no functional dimorphism under one\n    reading; their mean r per sex is reported. The text's \"functionally uncorrelated in both sexes\"\n    has no measure or test in the paper (the Figure 4F legend states only little to no functional\n    dimorphism), so that part is reported descriptively and does not decide the outcome."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "    (Methods, Selecting neuron pairs...). Not connected is read as",
 "new_string": "    (Methods, Selecting neuron pairs...). The order of these exclusions is OPEN: the Methods name\n    them after the top 36, and the Figure S4C legend says the 36 include pairs that Figure 4G drops\n    (sensory-sensory pairs). Readings are (i) the exclusions applied before taking the 36; (ii) the\n    top 36 by p < 0.01 alone, with stimulus pairs and pairs absent from the connectome then left out\n    of the counts. Both are run and must give the outcome. Not connected is read as"
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "  criterion: CONNECTOME only; the dandiset is not used. Directed synapses with both neurons among the\n    recorded head neurons (code Fig4_prepare_data); SEM over the three hermaphrodite datasets (pandas\n    sem, ddof 1), its mean and SD (ddof 1) before and after normalization.",
 "new_string": "  criterion: CONNECTOME only; the dandiset is not used. SEM per directed synapse over the three\n    hermaphrodite datasets (pandas sem, ddof 1), its mean and SD (ddof 1) before and after\n    normalization. Which synapses enter is OPEN: the Methods say \"across all synapses\", the code\n    (Fig4_prepare_data) keeps synapses with both neurons among the recorded head neurons. Readings\n    are (a) the code's set; (b) every directed neuron pair with a synapse in at least one\n    hermaphrodite dataset. Reproduced when all four values are within tolerance under one reading,\n    as these are readings of what the reported numbers were computed over."
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "old_string": "- id: fig3a-osmotic-onset-examples",
 "new_string": "- id: layers-sensory-most-dimorphic\n  statement: Dimorphic and monomorphic responses are less present in interneurons than in sensory\n    neurons, and less still in motor neurons.\n  source: Summary; Figures 3A, 3B and 5B\n  quote: This dimorphic and monomorphic activity was present to a lesser extent in downstream\n    interneurons and even less so in motoneurons\n  depends_on:\n  - fig3-each-stimulus-mixed\n  - fig5b-layer-counts\n  criterion: The paper gives no measure for this. Its class counts (Figure 5B, 92% of sensory, 92%\n    of inter and 87% of motor classes dimorphic) do not order sensory above inter, so the statement\n    is read from the per-stimulus counts of Figure 5B and the cells of Figure 3A and 3B. Over the 8\n    cues, with canonical classes and layers as in fig5b-layer-counts, per layer, readings are (a)\n    the fraction of class-cue combinations with a dimorphic response (DIMORPHISM, onset or offset);\n    (b) the fraction of class-cue combinations that are responsive (RESPONSIVE, dimorphic or\n    monomorphic); (c) as (a) over subclass-cue-window cells of Figure 3A and 3B. Reproduced when,\n    under one reading, sensory > inter > motor; each reading is reported.\n- id: fig3a-osmotic-onset-examples"
}
```

```
The file claims/000981/10.1016-j.cub.2026.08.040.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -5 claims/000981/10.1016-j.cub.2026.08.040.yaml; grep -n "^checks" claims/000981/*.yaml
```

```
criterion: Drop-test avoidance indices (Methods, Behavioral assays; code FigS2.ipynb). Per stimulus
    and strain, hermaphrodite against male, two-sample t-test (S1 legend; equal variances, as the
    code). "Robust" has no test in the paper or code and is reported descriptively. Reproduced when,
    in each strain, at least one stimulus differs between the sexes (p <= 0.05) and at least one does
    not. The paper does not say these data are in the dandiset.
```

**Agent calls Bash**

```bash
cd  cat >> claims/000981/10.1016-j.cub.2026.08.040.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3a-osmotic-onset-examples, fig3a-ash-stimulus-dependent, fig3a-aser-salt-concentration and fig2e-i2-dimorphic, statistics removed. Each recorded "p < 0.05, independent-sample t test", the Results' definition of a dimorphic neuron-stimulus pair; the paper reports no test result for these pairs, so it is a threshold used to classify, not a result.
  - Opening comment, EXCLUSION and new READINGS paragraph. The two exclusion readings are choices of method, so the outcome must be the one both give, else methods_underspecified (protocol, Reader, step 3); fig5b-responsive-classes, fig5b-dimorphic-classes and fig5b-layer-counts let a claim pass under either and now require both.
  - Opening comment, CORRELATION. The code's pooling and 3 IQR outlier removal are not in the Methods, which average each correlation across individuals; by protocol step 2 the Methods' reading (b) decides and the code's (a) is a variant. fig4c-functional-connectivity-similar (was "under one reading"), fig4-stimuli-correlate-sensory and fig4-functional-dimorphism-small changed to match.
  - fig3a-osmotic-onset-examples, fig2b-bag-high-odor-monomorphic, fig3a-ash-stimulus-dependent, fig3a-aser-salt-concentration. A monomorphic response was tested only as p > 0.05, which a class that does not respond also passes; Figures 3 and 5 count a class as monomorphic only when responsive, so the criteria now also require RESPONSIVE for that cue and window.
  - fig2-adf-m2-switch. Reading (b) accepted any dimorphism to both cues, which does not test which sex responds to which cue; it now requires the direction of the switch the statement names.
  - fig4f-synaptic-top-not-functional. The criterion did not test the quoted "functionally uncorrelated"; the paper gives no measure for it, so the criterion now says it is reported descriptively and the outcome rests on the Figure 4F legend's "little to no dimorphism".
  - fig4g-functional-top-not-synaptic. The criterion applied the stimulus, sensory-sensory and connectome exclusions before taking the top 36, but the Figure S4C legend says the 36 include pairs Figure 4G drops; both orders are now named as readings and must agree.
  - connectome-normalization-sem. The restriction to recorded head neurons came from the code alone while the Methods say "all synapses"; both sets are now named as readings of what the reported numbers cover.
  - layers-sensory-most-dimorphic added. The Summary's finding that dimorphic and monomorphic activity is less present in interneurons and least in motor neurons had no claim; the paper gives no measure, so the readings are named.
  - Open. Paragraph numbers in the sources could not be checked (no PDF renderer; the text loses paragraph breaks); they were left as written and are consistent with each other.
  - Open. Several thresholds for words the paper does not quantify are readings chosen by the first reader and kept, as named in the criteria ("nearly every" in sensory-dimorphic-and-monomorphic as at least 22 of 24, "predominantly" in male-specific-unresponsive, "many" and "mostly" in figs8-state-insensitive, "largely" in figs3e-pattern-robust).
  - Open. The paper's code was not reread in this check (the file cites the repository at commit b0dbdbf); statements attributed to the code are taken from the first reader.
EOF
python tools/claims_check.py claims/000981/10.1016-j.cub.2026.08.040.yaml paper/10.1016-j.cub.2026.08.040.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000981/10.1016-j.cub.2026.08.040.yaml; sed -i 's/exclusions is OPEN: the Methods name/exclusions is OPEN. The Methods name/; s/Which synapses enter is OPEN: the Methods say/Which synapses enter is OPEN. The Methods say/' $f; grep -n "^ \+[^#].*[a-z)]: " $f | grep -v "^\S*\s*- \?[a-z_]*: " | head; python tools/claims_check.py $f paper/10.1016-j.cub.2026.08.040.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/000981/*.yaml; git status --short
```

```
M claims/000981/10.1016-j.cub.2026.08.040.yaml
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? scripts
```

**Agent**

The claims file for DANDI:000981 is ready for an attempt: I corrected what I could show was wrong from the paper and marked the last check `ready: true`. The checker now reports **33 claims, 33 quotes, 0 statistical values, 0 problems**. Before my edits it reported 32 claims and 4 statistical values, also with 0 problems. Nothing was committed or pushed.

**Changes, by claim**
- **Statistics removed** from `fig3a-osmotic-onset-examples`, `fig3a-ash-stimulus-dependent`, `fig3a-aser-salt-concentration` and `fig2e-i2-dimorphic`. Each one recorded "p < 0.05, independent-sample t test", which is the paper's definition of a dimorphic pair. The paper reports no test result for these pairs, so it is a threshold, not a result.
- **Exclusion readings** (opening comment, plus `fig5b-responsive-classes`, `fig5b-dimorphic-classes`, `fig5b-layer-counts`): these claims could pass under either exclusion reading. The two readings are choices of method, so now both must give the same outcome, or the claim is blocked as `methods_underspecified`. I added a READINGS paragraph to the opening comment that states this rule.
- **Correlation method** (opening comment, plus `fig4c-functional-connectivity-similar`, `fig4-stimuli-correlate-sensory`, `fig4-functional-dimorphism-small`): the code's pooling and outlier removal are not in the Methods. Following protocol step 2, the Methods' per-animal averaging now decides the outcome and the code's version is shown as a variant. `fig4c` previously passed "under one reading".
- **Monomorphic means responsive** (`fig3a-osmotic-onset-examples`, `fig2b-bag-high-odor-monomorphic`, `fig3a-ash-stimulus-dependent`, `fig3a-aser-salt-concentration`): "monomorphic" was tested only as p > 0.05, which a neuron that does not respond would also pass. Figures 3 and 5 count a class as monomorphic only when it responds, so these criteria now also require a response to that cue in that window.
- **`fig2-adf-m2-switch`**: reading (b) accepted any dimorphism to both cues. It now requires the switch the statement names: which sex responds more to food and which to pheromone.
- **`fig4f-synaptic-top-not-functional`**: the criterion never tested the quoted "functionally uncorrelated", and the paper gives no measure for it. It is now reported descriptively, and the outcome rests on the Figure 4F legend ("little to no dimorphism").
- **`fig4g-functional-top-not-synaptic`**: the Methods and the Figure S4C legend leave open whether the pair exclusions come before or after taking the top 36. Both orders are now named, and they must agree.
- **`connectome-normalization-sem`**: the set of synapses came from the code alone, while the Methods say "all synapses". Both sets are now named as readings.
- **Added `layers-sensory-most-dimorphic`**: the Summary's finding that this activity is weaker in interneurons and weakest in motor neurons had no claim. The paper gives no measure, and its own class counts (92%, 92%, 87%) do not put sensory above inter, so the criterion names three readings and passes if one holds.

**What remains open** (also recorded in the checks entry)
- **Paragraph numbers in the `source` fields** are unverified. The text extract loses paragraph breaks and no PDF renderer was available. They were left as written; they are consistent with each other.
- **Thresholds for unquantified words** were chosen by the first reader and kept: "nearly every", "predominantly", "many", "mostly" and "largely". They are named in the criteria.
- **The paper's code was not reread** in this check. Statements about it are the first reader's, citing commit b0dbdbf.

## End of run

34 turns, 4 minutes, result: success.
