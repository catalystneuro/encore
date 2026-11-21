# fritsche-2022 · claims-check · run 44869856133

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/ | grep -i fritsche; python tools/claims_check.py claims/fritsche-2022.yaml paper/fritsche-2022.txt; cat claims/fritsche-2022.yaml; grep -n -A40 -i "reader" docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls paper/; ls paper/* | grep -i -E "fritsche|1350"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/fritsche-2022.yaml paper/10.1523-jneurosci.1350-21.2021.txt; wc -l claims/fritsche-2022.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/fritsche-2022.yaml"
}
```

```
1	# Claims for Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace
2	# in Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021, on dandiset
3	# 000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1 Stimulus Set), which the
4	# paper reuses.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
6	# protocol as stated in docs/protocol.md (pilot-18).
7	#
8	# Text read. The version of record, full text from PubMed Central (PMC8916757), in
9	# paper/10.1523-jneurosci.1350-21.2021.txt: abstract, Introduction, Materials and Methods, Results,
10	# Discussion, the legends of Figures 1 to 8 and Tables 1 and 2. The paper has no supplement. The
11	# extracted text drops the display equations; these were read from the MathML of the same PMC page
12	# (pmc.ncbi.nlm.nih.gov/articles/PMC8916757). They are (1) adaptation ratio = fr_repeat /
13	# fr_orthogonal; (2) the double exponential, printed as r(n) = 1 - a_fast * exp(-(n-1)/tau_fast) +
14	# a_slow * exp(-(n-1)/tau_slow); (3) the single exponential r(n) = 1 - a * exp(-(n-1)/tau); (4) OSI =
15	# (fr_preferred - fr_non-preferred) / (fr_preferred + fr_non-preferred); (5) the cumulative ratio of
16	# Fig. 4, ar_2-8 = product over n = 2 to 8 of ar_n. Figures were not opened (there is no PDF under
17	# paper/); no number below is read from a figure.
18	#
19	# Code. The paper links its analysis code at the Donders Repository, doi:10.34973/kpt9-y956
20	# (collection DSC_3018000.01_830, version 1). Its file list can be read without a login. It holds
[... 788 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1350-21.2021.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1350-21.2021.txt",
 "offset": 319
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passed (29 claims, 0 problems). Now I'm checking each claim against the paper text and the protocol's rules.

**Agent calls Bash**

```bash
grep -n -i -E "reader|step 5|checks|ready|tolerance|threshold|open" docs/protocol.md | head -80
```

```
13:- The **reader** reads the paper and writes the claims file: every finding,
14:  and how each is to be tested, taken from the paper. A second reader checks
15:  it against the paper. Readers never see the dataset's data.
19:  lacks it takes from the paper, citing the passage, and it asks a reader
21:- The **verifier** checks the author's work and must not be the author.
25:comes from the paper. Where the paper leaves a method open, the choice made is
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
32:`author`, `author-answers` when a reader answered a question on the claims
43:## Reader
48:`paper/`: the main text, the Methods, and the supplement. Read the text; open
63:open and the code settles it, follow the code and say so. Where they disagree,
71:Write `claims/<paper>.yaml`, one file for the paper, across all its datasets. Its opening comment
85:     reader check the statement against the paper without opening it. For a
100:     numbers the attempt must match, with tolerances, stay in `expected`.
101:     Record only tests whose result is the finding. A significance threshold
106:   - `expected`: each reported number the claim rests on, with a tolerance.
110:     widened by 10% of each bound. Give the reason for any other tolerance.
122:     bins, thresholds, what a measure is compared with) is taken from the
125:     treating a detail as open.
138:     criterion names the test and threshold the paper used. The claim is
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 43,
 "limit": 150
}
```

```
43	## Reader
44	
45	### 1. Get the paper
46	
47	The workflow puts the paper's full text, and its PDF where there is one, under
48	`paper/`: the main text, the Methods, and the supplement. Read the text; open
49	the PDF only to read a figure or a table the text garbles. If the full text is
50	not there, or lacks the Methods or a supplement the results rest on, stop:
51	write no claims, and end with a report that names what is missing, so that it
52	can be supplied. Never write claims from the abstract. Do not copy figures.
53	Do not look at the dataset's data: its title and description on the archive
54	are enough to know which paper and which experiments it is meant to hold. A
55	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
56	documentation) is a longer description, to be read for that alone; it is not
57	the paper, and no claim comes from it.
58	
59	### 2. Read the paper's code
60	
61	Read the code the paper links to before writing criteria. Say what it holds,
62	and record the repository and commit read. Where the Methods leave a choice
[... 130 more lines not kept]
```

**Agent**

Every quote, p-value and interval matches the text. Tolerances all equal the larger distance from the value to a CI bound. I found a few gaps and overreaches and am fixing them now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "#   spontaneous gray-screen epoch. The preferred orientation is taken over all trials of that\n#   orientation (both directions, all temporal frequencies).",
 "new_string": "#   spontaneous gray-screen epoch. The preferred orientation, \"eliciting the highest firing rate\",\n#   is (e) the orientation whose trials, pooled over both directions and all temporal\n#   frequencies, give the highest mean rate, or (f) the orientation of the single direction and\n#   temporal frequency condition with the highest mean rate; the Methods do not say which."
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "  statement: The slow component of V1 adaptation to drifting gratings has a half-life of about 14 s.",
 "new_string": "  statement: Adaptation in this study has a half-life of about 14 s; the paper does not say of which\n    component or area, and it is read here as the slow V1 component for drifting gratings."
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "  statement: Extrastriate slow time constants for drifting gratings range from 3.12 to 5.52 trials,\n    with 95% CIs overlapping, close to V1's.",
 "new_string": "  statement: Recovery from adaptation to drifting gratings is slowest in V1 (tau_slow 6.82 trials),\n    and relatively similar in extrastriate areas, whose slow time constants range from 3.12 to 5.52\n    trials with all 95% CIs overlapping."
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "    all overlap one another; partially reproduced when four of the five are inside. The other\n    Table 1 parameters",
 "new_string": "    all overlap one another; partially reproduced when four of the five are inside. Whether V1's\n    tau_slow is the largest of the six is reported (the paper's \"slowest in V1\" rests on point\n    estimates whose CIs overlap, and gives no test). The other Table 1 parameters"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "  criterion: Per V1 cell of tertile and relative orientation, a two-tailed t test of unit log ratios\n    against zero, corrected over the nine cells as O6. Reproduced",
 "new_string": "  criterion: Per V1 cell of tertile and relative orientation, a two-tailed t test of unit log ratios\n    against zero, corrected as O6. The legend does not name the family corrected over; readings,\n    each run, (a) the nine V1 cells, (b) all cells of all areas in Figure 2D to 2F. Reproduced"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "    1-back ratio (Figure 8 legend), is analysed as the data are. The paper does not state the\n    response noise; readings (a) Poisson spike counts at a fixed rate, (b) no noise. The 95% CI is\n    taken across the 32 sequences (legend). Reproduced when, under one reading, the recovered\n    1-back ratio's CI contains the ground truth and every n-back ratio for n >= 2 has a CI that\n    contains 1, for both stimulus sets;",
 "new_string": "    1-back ratio (Figure 8 legend; for each stimulus set, that set's V1 1-back ratio), is analysed\n    as the data are. The paper does not state the response noise; readings (a) Poisson spike\n    counts at a fixed rate, (b) no noise. Nor does it state the range of n shown; readings (c) 2 to\n    10, the tested family, (d) 2 to 50, the fitted range. The 95% CI is taken across the 32\n    sequences (legend). Reproduced when, under one reading, the recovered 1-back ratio's CI\n    contains the ground truth and every n-back ratio in the range read has a CI that contains 1,\n    for both stimulus sets;"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Next I'm adding claims for the two Figure 7 findings that had none (7B per-area significance, 7C consistency across mice), then the check entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "- id: fig8-no-spurious-long-term",
 "new_string": "- id: fig7b-static-areas-long-term\n  statement: After static gratings, cortical areas show significant adaptation to orientations\n    presented up to 20 trials back, whereas in the thalamus long-term adaptation is less evident.\n  source: Figure 7B legend\n  quote: In cortical areas (squares) there is significant adaptation to stimulus orientations\n    presented up to 20 trials back (symbols with black border, p < 0.05, FDR corrected per area),\n    whereas in thalamic areas (circles) long-term adaptation is less evident.\n  statistics:\n  - test: t tests of log ratios against zero, per area\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR per area\n  expected:\n    quantity: largest significant n-back in cortical areas, static\n    value: 20\n    tolerance: 2\n  depends_on:\n  - fig7a-static-v1-long-term\n  - fig6c-static-other-areas-1back\n  criterion: The t tests of fig3b-thalamus-short-term, per area, on 0 to 250 ms rates of static\n    gratings, with the FDR family read as in fig7a-static-v1-long-term ((a) 1 to 20, (b) 1 to 50).\n    The legend leaves open whether \"up to 20 trials back\" holds in (c) some cortical area or (d)\n    every cortical area; the largest significant n is to lie in 18 to 22 (10% of 20). \"Less\n    evident\" has no test in the paper; it is read as the largest significant n in LGN and in LP\n    being smaller than in every cortical area. Reproduced when, under one reading, the cortical\n    and thalamic parts both hold; the largest significant n per area is reported.\n- id: fig7c-static-long-term-across-mice\n  statement: Long-term adaptation to static gratings (5- to 20-back) is consistent across mice.\n  source: Figure 7C; Results, Long-term adaptation following exposure to brief static gratings,\n    paragraph 2\n  quote: Neurons in V1 showed significant adaptation effects to stimuli presented as far as 20\n    presentations (5 s) in the past (Fig. 7A,C, showing consistent adaptation across mice).\n  depends_on:\n  - fig7a-static-v1-long-term\n  criterion: Per mouse, the average 0 to 100 ms... no, 0 to 250 ms firing rate of its units when\n    the 5- to 20-back orientation was repeated against orthogonal (Figure 7C legend), whether the\n    positions are pooled as trials or averaged as ratios being open, both run. The panel shows\n    thalamus and cortex; the text does not say which group is consistent; readings (a) the\n    cortical units, (b) the V1 units (the subject of the sentence). Consistency is read as in\n    fig1e-consistent-across-mice. Reproduced when it holds under one reading; the thalamic panel\n    is reported only.\n- id: fig8-no-spurious-long-term"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Fixing a stray phrase I left in that criterion:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "  criterion: Per mouse, the average 0 to 100 ms... no, 0 to 250 ms firing rate of its units when",
 "new_string": "  criterion: Per mouse, the average 0 to 250 ms firing rate of its units when"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/fritsche-2022.yaml <<'EOF'
checks:
- date: 2026-11-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header O4, named the preferred orientation as open (pooled over directions and temporal frequencies, or the best single condition), since the Methods say only "eliciting the highest firing rate" and the file had fixed one reading without saying so.
  - fig3a-v1-half-life, statement now says the paper does not name the component or area of the ~14 s half-life and that slow V1 is a reading; the old statement said more than the Discussion does.
  - table1-extrastriate-tau-slow, statement now gives the paper's "slowest in V1" and "relatively similar" in place of "close to V1's", and the criterion reports whether V1's tau_slow is the largest.
  - fig2-v1-adaptation-at-all-orientations, the family for the multiple-comparison correction is named as open (nine V1 cells, or all cells of Figure 2D to 2F); the legend does not give it.
  - fig8-no-spurious-long-term, the range of n is named as open (2 to 10 or 2 to 50) and the simulated 1-back ratio is that of each stimulus set's V1; the old criterion used "every n >= 2" without a bound.
  - Added fig7b-static-areas-long-term, the Figure 7B finding that cortical areas adapt up to 20 trials back after static gratings and the thalamus less so, which had no claim.
  - Added fig7c-static-long-term-across-mice, the Figure 7C finding of consistent long-term static adaptation across mice, which had no claim (Figures 1E, 3C and 6D each have one).
  - Open, not settled here. The display equations (the double exponential's sign, the cumulative ratio) were read by the writer from the PMC MathML and are absent from paper/; they could not be checked against the text under paper/. The criteria name both sign readings, so no outcome rests on it.
  - Open, not settled here. The analysis code (doi:10.34973/kpt9-y956) is reported as restricted; it was not read, so the readings named under O1 to O6 stay open.
  - Open, not settled here. The LGN and LP static ratios (0.93, 0.85) sit on the lower bounds of their printed CIs; the widened-CI rule of fig6c-static-other-areas-1back is the writer's and is kept with its stated reason.
EOF
python tools/claims_check.py claims/fritsche-2022.yaml paper/10.1523-jneurosci.1350-21.2021.txt; grep -n ': .*: ' claims/fritsche-2022.yaml | grep -v '^\s*#' | grep -v '{' | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -E "rather|—" claims/fritsche-2022.yaml; git status --short
```

```
M claims/fritsche-2022.yaml
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

The checker passed and the file is ready for an attempt. The only change on disk is to `claims/fritsche-2022.yaml`; nothing is committed.

**Checker result:** `claims/fritsche-2022.yaml: 31 claims, 31 quotes, 81 statistical values, 0 problems`. Before my changes it was 29 claims, 29 quotes, 80 values, 0 problems. I ran it against `paper/10.1523-jneurosci.1350-21.2021.txt`; there is no `paper/fritsche-2022.txt`.

**What held up:** I checked every expected value and tolerance against the text, Table 1 and Table 2. Each tolerance is the larger distance from the value to a CI bound, or 10% where the paper gives no interval. Ranges are widened by 10% of each bound. No statistic is a threshold used to count units, and no claim comes from outside this paper.

**Changes, by claim:**
- **Header, open detail O4:** how the preferred orientation is chosen is now named as open, with two readings: the best orientation pooled over directions and temporal frequencies, or the orientation of the single best condition. The Methods say only "eliciting the highest firing rate", and the file had silently picked the first.
- **fig3a-v1-half-life:** the statement no longer says the ~14 s half-life belongs to the slow V1 component. The Discussion doesn't say which component or area it is; that is now marked as a reading.
- **table1-extrastriate-tau-slow:** the statement now uses the paper's words, "slowest in V1" and "relatively similar", in place of "close to V1's". The criterion also reports whether V1 has the largest slow time constant.
- **fig2-v1-adaptation-at-all-orientations:** which tests the multiple-comparison correction covers is now open, with two readings: the nine V1 cells, or every cell in Figure 2D to 2F.
- **fig8-no-spurious-long-term:** the range of n-back positions is now open (2 to 10, or 2 to 50); the old criterion had no upper bound. The simulated neuron's 1-back ratio is now that stimulus set's own V1 ratio.
- **New, fig7b-static-areas-long-term:** after static gratings, cortical areas adapt up to 20 trials back and the thalamus less so (Fig. 7B). This finding had no claim.
- **New, fig7c-static-long-term-across-mice:** long-term static adaptation is consistent across mice (Fig. 7C). This was missing, while the matching Figures 1E, 3C and 6D each have a claim.

**Still open (recorded under `checks`):**
- The model equations, including the sign of the double exponential's second term, are not in the text under `paper/`. The writer read them from the PubMed Central page, so I couldn't check them. The criteria run both sign readings, so no outcome depends on this.
- The paper's analysis code is reported as access-restricted and was never read. The open details O1 to O6 therefore stay open.
- In the static-grating results, the LGN and LP ratios (0.93, 0.85) sit exactly on the lower edges of their printed confidence intervals. The writer's rule for this, which widens each interval down to the value minus 10%, is not from the paper. I kept it with its stated reason.

`git status` also lists untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others). I left them alone.

## End of run

19 turns, 3 minutes, $1.20 at API prices, result: success.
