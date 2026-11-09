# crcns-hc-16 · claims-check · run 41963642990

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/crcns-hc-16/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 100,220p docs/protocol.md; cat claims/crcns-hc-16/*.yaml; python tools/claims_check.py claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml paper/10.1016-j.neuron.2017.12.043.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml paper/10.1016-j.neuron.2017.12.043.txt; echo EXIT $?; wc -l claims/crcns-hc-16/*.yaml paper/10.1016-j.neuron.2017.12.043.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2017.12.043.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml"
}
```

```
1	# Claims for Talbot, Sparks, Dvorak, Curran, Alarcon & Fenton (2018), Neuron 97:684-697, on CRCNS
2	# data set hc-16 (doi:10.6080/K01V5C44).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-05,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
5	#
6	# Text read: the version of record with its supplemental information, as supplied under paper/
7	# (PyMuPDF text of the journal PDF): Results, Discussion, figure legends, STAR Methods, and the
8	# supplement (Figures S1 to S6, Tables S1 and S2). The PDF pages could not be rendered here, so no
9	# figure was read from the image. The extracted text prints some signs as other glyphs. "Dt" is
10	# delta t, "t" before a value in the Kendall passages is tau, "jDIposj" is |delta Ipos|, "3" between
11	# factors is "x", "hp 2" is partial eta squared, and "10�17" is 10 to the power -17. Quotes keep these
12	# glyphs as printed; p-values printed as powers of ten were confirmed by reading, as the quote
13	# checker cannot find them. The second paper under paper/ (Dvorak et al. 2018, PLoS Biol) also
14	# uses the data set; no claim comes from it, nor from the data set's description.
15	#
16	# Code read (the Key Resources Table links three FentonLab repositories, for Figures 3, 4, 5 and
17	# S5). SpikeField, commit 4dfbc35 (MATLAB, getLFPphase.m and getWavelets.m): spike phases from
18	# complex Morlet wavelets (wavelet factor 8) at 100 log-spaced frequencies from 2 to 250 Hz on LFP
19	# sampled at 2 kHz, the wire of each tetrode with the least artifact, spikes in artifact periods
20	# dropped, cluster 0 dropped; no speed filter. CorrelateBPFSpikeTrainEpisodes, commit 150c2df (C):
[... 1136 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2017.12.043.txt",
 "offset": 1143,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports 6 p-values it couldn't find (all printed as powers of ten). I've read the main text and am now reading the Methods and supplement.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2017.12.043.txt",
 "offset": 1860,
 "limit": 1100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Figure S[2-6]|Table S2",
 "path": "paper/10.1016-j.neuron.2017.12.043.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2017.12.043.txt",
 "offset": 3595,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent**

All six flagged p-values are printed as powers of ten in the text, and reading confirms them (lines 289, 332, 714, 731, 736, 756). I'm now correcting the problems I found against the paper.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    above both naive groups, with naive WT and naive Fmr1-null not different. Whether the unit is\n    the slice or the mouse is not stated; the slice is used, as the Methods describe one slice\n    recording per stimulus-response curve.",
 "new_string": "    above both naive groups, with naive WT and naive Fmr1-null not different. The unit is one value\n    per mouse; the error degrees of freedom (42 with six groups) give 48 units, the 22 WT and 26\n    Fmr1-null mice of the Methods."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    training ANOVA per phase, as the legend does. Reproduced when PTP",
 "new_string": "    training ANOVA per phase, as the legend does, one value per mouse (as in\n    fig1ab-baseline-transmission, from the 42 error degrees of freedom). Reproduced when PTP"
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  statement: Waveform width, burst probability, interspike interval and overall firing rate do not\n    differ between genotypes in any cell class.",
 "new_string": "  statement: Waveform width, burst probability, interspike interval and overall firing rate do not\n    differ between genotypes."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  statement: Firing rate, in-field rate, spatial coherence, information content and proportion of\n    active pixels of place cells do not differ between WT and Fmr1-null mice.",
 "new_string": "  statement: Firing rate, in-field rate, spatial coherence, information content and proportion of\n    active pixels of place cells, and the firing rate of interneurons, do not differ between WT and\n    Fmr1-null mice."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  - quantity: Fmr1-null place cell firing rate\n    value: 1.27\n    tolerance: 0.12\n    unit: AP/s\n  criterion: Tolerances",
 "new_string": "  - quantity: Fmr1-null place cell firing rate\n    value: 1.27\n    tolerance: 0.12\n    unit: AP/s\n  - quantity: WT place cell in-field rate\n    value: 2.61\n    tolerance: 0.2\n    unit: AP/s\n  - quantity: Fmr1-null place cell in-field rate\n    value: 2.2\n    tolerance: 0.13\n    unit: AP/s\n  - quantity: WT interneuron firing rate\n    value: 16.61\n    tolerance: 2.8\n    unit: AP/s\n  - quantity: Fmr1-null interneuron firing rate\n    value: 16.02\n    tolerance: 1.42\n    unit: AP/s\n  criterion: Tolerances"
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  criterion: Similarity as in the Methods, Fisher z of the Pearson correlation of rates in\n    corresponding pixels of the two maps (pixels visited in both). The square and circular\n    enclosures are read as a box and the stationary circular arena recorded the same day; whether\n    the box is the small or the large one is open, and every same-day pair of a box and the\n    stationary arena is used.",
 "new_string": "  criterion: Similarity as in the Methods, Fisher z of the Pearson correlation of rates in\n    corresponding pixels of the two maps (pixels visited in both). The square and circular\n    enclosures are read as a box and the stationary circular arena (the \"circular cylinder\" of the\n    Results); whether the box is the small or the large one is open. The paper does not say the\n    two recordings were made the same day, and Table S2 lists box and arena sessions of a mouse on\n    different dates, so the readings are (a) same-day pairs of a box and a stationary arena session\n    and (b) any box and stationary arena sessions in which the data identify the same cell; the\n    counts 25 and 31 indicate which fits."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    with fewest artifacts (Methods; SpikeField code, wavelet factor 8), spikes at speed above 2\n    cm/s only (Results). A claim of absence on the paper's t test between genotypes; reproduced\n    when both p >= 0.05. Which recordings are used is not stated; all stationary-environment\n    sessions are used.",
 "new_string": "    with fewest artifacts (Methods; SpikeField code, wavelet factor 8), spikes at speed above 2\n    cm/s only (Results). The Methods put the wavelets on a log scale from 2 to 100 Hz and the code\n    from 2 to 250 Hz; the Methods range is used, the code's as a variant, and the wavelet nearest 8\n    and 40 Hz is taken. A claim of absence on the paper's t test between genotypes; reproduced\n    when both p >= 0.05. Which recordings are used is not stated (the t169 degrees of freedom give\n    171 place cells, more than the 162 of Table S1); the readings are all stationary-environment\n    sessions, a cell counted once from its first, and the box sessions of fig2-spatial-quality-similar."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  expected:\n  - quantity: WT place cell theta phase\n    value: 353.9\n    tolerance: 36\n    unit: degrees\n  - quantity: Fmr1-null place cell theta phase\n    value: 32.1\n    tolerance: 36\n    unit: degrees\n  - quantity: WT place cell gamma phase\n    value: 332.2\n    tolerance: 36\n    unit: degrees\n  - quantity: Fmr1-null place cell gamma phase\n    value: 238.8\n    tolerance: 36\n    unit: degrees\n  - quantity: WT interneuron gamma phase\n    value: 218.6\n    tolerance: 36\n    unit: degrees\n  - quantity: Fmr1-null interneuron gamma phase\n    value: 10.6\n    tolerance: 36\n    unit: degrees\n  criterion: Phase preference per cell is the circular mean phase at 8 or 40 Hz, with 0 at the\n    trough (Figure 3B legend). The tolerance is 36 degrees, 10% of a cycle, as 10% of a circular\n    value is meaningless near 0 and 360; the printed spreads (about 50 to 76 degrees) are given as\n    ± and are not usable as SEMs. Circular distance is used. Reproduced when the three\n    Watson-Williams tests give p < 0.05 and at least four of the six means are within tolerance.",
 "new_string": "  expected:\n  - quantity: WT place cell theta phase\n    value: 353.9\n    tolerance: 67.3\n    unit: degrees\n  - quantity: Fmr1-null place cell theta phase\n    value: 32.1\n    tolerance: 53.1\n    unit: degrees\n  - quantity: WT place cell gamma phase\n    value: 332.2\n    tolerance: 63.6\n    unit: degrees\n  - quantity: Fmr1-null place cell gamma phase\n    value: 238.8\n    tolerance: 74.5\n    unit: degrees\n  - quantity: WT interneuron gamma phase\n    value: 218.6\n    tolerance: 75.0\n    unit: degrees\n  - quantity: Fmr1-null interneuron gamma phase\n    value: 10.6\n    tolerance: 76.4\n    unit: degrees\n  criterion: Phase preference per cell is the circular mean phase at 8 or 40 Hz, with 0 at the\n    trough (Figure 3B legend), averaged across cells as a circular mean. Tolerances are the printed\n    ± values, the paper's stated spread (the Quantification section calls every ± an SEM; their\n    size suggests a circular SD, and either way they are the paper's own uncertainty). Circular\n    distance is used. Reproduced when the three Watson-Williams tests give p < 0.05 in the stated\n    directions and all six means are within tolerance; partially reproduced when the tests hold\n    and some means fall outside."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    histograms normalized by the cell's spike count (Methods). The number of phase bins is not\n    stated; 20 bins (18 degrees) is used and 36 shown as a variant.",
 "new_string": "    histograms normalized by the cell's spike count (Methods), frequencies as in\n    fig3b-place-cell-modulation-similar. The number of phase bins is not stated in the paper and\n    was not found in the code read; the readings are 20 bins (18 degrees) and 36 bins (10 degrees),\n    both run."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    several sessions counts once, from its first. Mann-Whitney",
 "new_string": "    several sessions counts once, from its first (not stated in the paper; counting it per session\n    is the other reading, and the pair counts 247 and 504 indicate which fits). Mann-Whitney"
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    degrees of freedom (27) imply recordings, not mice, as units; both units are run.",
 "new_string": "    degrees of freedom (27) imply recordings, not mice, as units; both units are run. The paper\n    prints no test for speed or linearity in the Results sentence, and linearity is not defined in\n    the Methods; that part of the statement is not judged."
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "  expected:\n    quantity: r, entries against SEM of pair covariance\n    value: 0.61\n    tolerance: 0.061",
 "new_string": "  expected:\n  - quantity: r, entries against SEM of pair covariance\n    value: 0.61\n    tolerance: 0.061"
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml",
 "old_string": "    2), 10 min blocks of the 30 min extinction sessions. Reproduced",
 "new_string": "    2), 10 min blocks of the 30 min extinction sessions. The session effect of D to F has 3 degrees\n    of freedom, so four sessions; the reading is the four shock-on sessions (Train 1-3 and\n    Retrain), as shocks per entry is undefined with the shock off. Reproduced"
}
```

```
The file claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -rn -A8 "^checks:" claims/*/*.yaml | head -30
```

```
claims/000005/10.1038-nn.4412.yaml:1092:checks:
claims/000005/10.1038-nn.4412.yaml-1093-- date: 2026-10-20
claims/000005/10.1038-nn.4412.yaml-1094-  kind: agent
claims/000005/10.1038-nn.4412.yaml-1095-  model: claude-opus-5-5
claims/000005/10.1038-nn.4412.yaml-1096-  ready: true
claims/000005/10.1038-nn.4412.yaml-1097-  changes:
claims/000005/10.1038-nn.4412.yaml-1098-  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
claims/000005/10.1038-nn.4412.yaml-1099-  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
claims/000005/10.1038-nn.4412.yaml-1100-  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
--
claims/000006/10.1038-s41586-018-0642-9.yaml:841:checks:
claims/000006/10.1038-s41586-018-0642-9.yaml-842-- date: "2026-10-20"
claims/000006/10.1038-s41586-018-0642-9.yaml-843-  kind: agent
claims/000006/10.1038-s41586-018-0642-9.yaml-844-  model: claude-opus-5-5
claims/000006/10.1038-s41586-018-0642-9.yaml-845-  ready: true
claims/000006/10.1038-s41586-018-0642-9.yaml-846-  changes:
claims/000006/10.1038-s41586-018-0642-9.yaml-847-  - Opening comment. Added two code details read in Ephys.zip Code/ (Figshare doi:10.25378/janelia.7007846 v1),
claims/000006/10.1038-s41586-018-0642-9.yaml-848-    the zero weight of a neuron with rank-sum p of 1 in DirectionVector, and the epoch means taking time > start
claims/000006/10.1038-s41586-018-0642-9.yaml-849-    and <= end, unlike the CD windows.
--
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml <<'EOF'
checks:
- date: 2026-11-05
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - "All quotes match the text. The six p-values the checker could not find (fig1ab 1e-8, fig1cd 1e-6, fig3b-phase-preference 1e-7, fig3d 1e-10 and 1e-7, overdispersion-passes 1e-6) are printed as powers of ten at lines 289, 332, 714, 731, 736 and 756 of the text and were confirmed by reading."
  - "fig1ab-baseline-transmission and fig1cd-potentiation. The criterion said the unit (slice or mouse) is not stated and chose the slice; the error degrees of freedom (42 with six groups) give 48 units, the 22 WT and 26 Fmr1-null mice of the Methods, so the unit is one value per mouse."
  - "figs3-nonspatial-properties-similar. Dropped 'in any cell class' from the statement; the paper says the characteristics are indistinguishable between genotypes and tests the genotype main effect."
  - "tables1-place-cell-properties-similar. The statistics include the interneuron firing rate and the quote names interneurons, but the statement did not; added it. Added the Table S1 in-field rates (2.61 ± 0.2, 2.2 ± 0.13) and interneuron rates (16.61 ± 2.8, 16.02 ± 1.42) to expected, which had been left out."
  - "figs4-remapping-similar. The criterion restricted pairs to a box and arena recorded the same day; the paper does not say this and Table S2 lists box and arena sessions on different dates. Named it open with two readings."
  - "fig3b-place-cell-modulation-similar. The Methods give wavelets from 2 to 100 Hz, the code 2 to 250 Hz; the protocol puts the Methods first, so their range is used and the code's is a variant. The choice of recordings, stated as all stationary sessions, is named open with readings (t169 implies 171 place cells, not the 162 of Table S1)."
  - "fig3b-phase-preference. The tolerance was an invented 36 degrees and the pass rule an invented four of six means; the protocol takes the paper's stated spread, so the tolerances are now the printed ± values and all six means must match (partial otherwise)."
  - "fig3d-stereotypy. The phase bin count is not in the paper; 20 and 36 bins are now both readings, not a choice and a variant."
  - "fig4cd-kendall-place-cells. Counting a pair once from its first session was presented as fixed; marked it as not stated, with per-session counting as the other reading."
  - "locomotion-similar. The statement's speed and linearity part has no printed test and linearity is not defined in the Methods; the criterion now says that part is not judged."
  - "fig6-covariance-sem-predicts-errors. expected was a mapping; made it a one-item list like the other claims."
  - "fig6-avoidance-behavior. The criterion did not say which sessions enter the D to F ANOVA; the 3 session degrees of freedom imply four, read as the shock-on sessions Train 1-3 and Retrain."
  - "Open. fig2-spatial-quality-similar defines place fields by two readings (mean rate or 20% of peak, at least 9 pixels) that the paper does not give; the paper reports number of fields and in-field rate without defining a field, so these remain assumptions."
  - "Open. overdispersion-cells uses minimum pass counts of 2, 10 and 30 to explain 80 and 98 cells; the paper states no minimum."
  - "Open. figs1-avoidance-equal and figs5a-power-spectra-similar are claims of absence with no printed test; the criteria borrow a test (the Figure 6D ANOVA, a t test of band power), which is the reader's choice."
  - "Open. figs6-room-frame-preference reads 'similar for the two genotypes' as a non-significant interaction, which the paper does not print; which measure was log transformed is not stated."
  - "Open. Figure S6C (map stability across sessions, one t49 = 2.69, p < 0.01 comparison) and the Figure 4B and 4C upper and lower 50% insets have no claim; the extracted text does not say which S6C comparison is significant, and none is a main finding."
EOF
python tools/claims_check.py claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml paper/10.1016-j.neuron.2017.12.043.txt; grep -n "rather\|—" claims/crcns-hc-16/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short; git diff --stat; tail -5 claims/crcns-hc-16/*.yaml | cut -c1-120
```

```
M claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml
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
 .../crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml  | 112 +++++++++++++++------
 1 file changed, 84 insertions(+), 28 deletions(-)
  - "Open. fig2-spatial-quality-similar defines place fields by two readings (mean rate or 20% of peak, at least 9 pixel
  - "Open. overdispersion-cells uses minimum pass counts of 2, 10 and 30 to explain 80 and 98 cells; the paper states no
  - "Open. figs1-avoidance-equal and figs5a-power-spectra-similar are claims of absence with no printed test; the criter
  - "Open. figs6-room-frame-preference reads 'similar for the two genotypes' as a non-significant interaction, which the
  - "Open. Figure S6C (map stability across sessions, one t49 = 2.69, p < 0.01 comparison) and the Figure 4B and 4C uppe
```

**Agent**

The claims file is ready for an attempt. I corrected 11 claims against the paper and noted what remains open in a new `checks` entry. Only `claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml` was edited; nothing is committed.

**Checker result:** `32 claims, 31 quotes, 104 statistical values, 6 problems`. All quotes match the text. The six problems are p-values printed as powers of ten (fig1ab 1e-8, fig1cd 1e-6, fig3b-phase-preference 1e-7, fig3d 1e-10 and 1e-7, overdispersion-passes 1e-6). I found each one in the text at lines 289, 332, 714, 731, 736 and 756, so they are correct.

**Changes, by claim:**
- **fig1ab-baseline-transmission, fig1cd-potentiation:** the criterion treated the unit (slice or mouse) as open and picked the slice. The 42 error degrees of freedom with six groups give 48 units, which is the 22 WT and 26 Fmr1-null mice in the Methods. The unit is now one value per mouse.
- **figs3-nonspatial-properties-similar:** removed "in any cell class" from the statement. The paper only tests the genotype effect.
- **tables1-place-cell-properties-similar:** added the interneuron firing rate to the statement, since the statistics and the quote already include it. Added the missing Table S1 in-field rates and interneuron rates to `expected`.
- **figs4-remapping-similar:** the criterion required the box and arena recordings to be on the same day. The paper never says that, and Table S2 dates them differently. Same-day pairs and pairs from any date are now both readings.
- **fig3b-place-cell-modulation-similar:** the Methods give wavelets from 2 to 100 Hz and the code 2 to 250 Hz. The Methods range is now used, with the code's range as a variant. Which recordings to use is now marked open and given readings: 169 degrees of freedom imply 171 place cells, not the 162 in Table S1.
- **fig3b-phase-preference:** the 36° tolerance and the "four of six means" rule were both made up. Tolerances are now the paper's printed ± values, and all six means must match.
- **fig3d-stereotypy:** the number of phase bins is not in the paper, so 20 and 36 bins are now equal readings.
- **fig4cd-kendall-place-cells:** "a pair counts once, from its first session" is now marked as not stated in the paper, with counting per session as the other reading.
- **locomotion-similar:** the paper prints no test for speed or path linearity and never defines linearity. The criterion now says that part of the statement is not judged.
- **fig6-covariance-sem-predicts-errors:** `expected` was written as a mapping; it is now a list like the other claims.
- **fig6-avoidance-behavior:** the session effect has 3 degrees of freedom, so four sessions. These are read as the shock-on sessions (Train 1–3 and Retrain).

**Still open (noted in `checks`):**
- **fig2:** the place-field definitions (above the mean rate, or above 20% of peak, with at least 9 pixels) are not in the paper.
- **overdispersion-cells:** the minimum pass counts (2, 10, 30) are not stated in the paper.
- **figs1 and figs5a:** these claim "no difference" but the paper prints no test, so the tests used are borrowed from elsewhere.
- **figs6:** reading "similar for the two genotypes" as a non-significant interaction is our interpretation, and the paper does not say which measure was log-transformed.
- **Not covered:** Figure S6C (one significant t49 comparison; the extracted text doesn't say which) and the upper and lower 50% insets in Figures 4B and 4C have no claims. Neither is a main finding.

The paper's main findings all have claims, and no claim comes from another source.

## End of run

26 turns, 3 minutes, $1.56 at API prices, result: success.
