# 001274 · claims-check · run 39730976828

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001274/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001274/*.yaml paper/*.txt; cat claims/001274/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; echo ======; python tools/claims_check.py claims/001274/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001274/10.1016-j.xcrp.2025.102660.yaml"
}
```

```
1	# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
2	# on dandiset 001274.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md version pilot-10, as the reader.
5	#
6	# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with
7	# its main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
8	# Figures S1 to S4 and Table S1, the Key Resource Table), all in
9	# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
10	# available, so Figures 1 to 6 could not be looked at; numbers shown only in figures are not used.
11	#
12	# Code. The paper states that it does not report original code. Analyses were done with Fiji or
13	# MetaMorph (ROI intensities), Origin 8.0 (exponential fits), Grapher 16 (linear regression) and,
14	# per Table S1, RStudio 2024.04.2 (the LOESS fits are read here as R's loess, see below).
15	#
16	# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
17	# week on coverslips, stained with FluoVolt (Di-8-ANEPPS in Figure S1). Two kinds of recording:
18	# (1) Fast imaging of the optical membrane potential (64 x 64 pixels, 3,130 or 3,086.4 frames/s,
19	# 1,200 images per session, 50 ms before, 250 ms during and about 90 ms after the stimulus), with
20	# 250-ms unmodulated or 20-Hz amplitude-modulated sine waves at 2 and 20 kHz (Figures 1, 2), in
[... 590 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.xcrp.2025.102660.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1016-j.xcrp.2025.102660.txt').read()
print(t[52400:85000])"
```

```
<persisted-output>
Output too large (32KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0575ce91-aa50-488e-859d-7ba42bc29478/tool-results/bb2fx91rv.txt

Preview (first 2KB):
ontinued for 250 ms during and about 90 ms after the stimulation, generating 1,200 images per stimulation session. After the first session, the stimulus amplitude was increased if no APs were detected or decreased to find the threshold if multiple APs were evoked. The imaging/stimulation sessions were repeated multiple times with 20–60 s intervals between them, either at escalating voltages or by choosing voltages randomly. In experiments aimed at determining the excitation thresholds ( Figure 2D ), the sine wave amplitude was adjusted up or down in 5%–10% steps until the minimal voltages eliciting 1 and 5 APs were determined. Next, we switched to a different stimulus type (e.g., from a modulated to an unmodulated signal or from 2 to 20 kHz) and repeated the search for the 1- and 5-AP thresholds. The emission intensity over the entire cell soma (F) was quantified using either Fiji ImageJ 1.53C (National Institutes of Health, USA) or MetaMorph 7.7 (Molecular Devices, San Jose, CA). The mean value over a time interval preceding the electrical stimulation was used as a 100% reference ( F 0 ) . Emission change in each frame ( Δ F ) in the sequence was determined as Δ F = 100 % × ( F − F 0 ) ∕ F 0 . APs were readily identifiable as brief emission upticks. For experiments, we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical values: 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM, n = 22). Traces of the optical membrane potential were not filtered or modified in any way (except for long recordings in Figure 3C , which were corrected for bleaching by subtracting a trace without APs). The maximum AP firing rate was measured as the inverse of the peak-to-peak 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0575ce91-aa50-488e-859d-7ba42bc29478/tool-results/bb2fx91rv.txt"
}
```

```
1	ontinued for 250 ms during and about 90 ms after the stimulation, generating 1,200 images per stimulation session. After the first session, the stimulus amplitude was increased if no APs were detected or decreased to find the threshold if multiple APs were evoked. The imaging/stimulation sessions were repeated multiple times with 20–60 s intervals between them, either at escalating voltages or by choosing voltages randomly. In experiments aimed at determining the excitation thresholds ( Figure 2D ), the sine wave amplitude was adjusted up or down in 5%–10% steps until the minimal voltages eliciting 1 and 5 APs were determined. Next, we switched to a different stimulus type (e.g., from a modulated to an unmodulated signal or from 2 to 20 kHz) and repeated the search for the 1- and 5-AP thresholds. The emission intensity over the entire cell soma (F) was quantified using either Fiji ImageJ 1.53C (National Institutes of Health, USA) or MetaMorph 7.7 (Molecular Devices, San Jose, CA). The mean value over a time interval preceding the electrical stimulation was used as a 100% reference ( F 0 ) . Emission change in each frame ( Δ F ) in the sequence was determined as Δ F = 100 % × ( F − F 0 ) ∕ F 0 . APs were readily identifiable as brief emission upticks. For experiments, we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical values: 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM, n = 22). Traces of the optical membrane potential were not filtered or modified in any way (except for long recordings in Figure 3C , which were corrected for bleaching by subtracting a trace without APs). The maximum AP firing rate was measured as the inverse of the peak-to-peak time interval between the first two APs evoked in each stimulation session. Traces of the optical membrane potential, as well as other graphs, were generated with Grapher v.16 software (Golden Software, Golden, CO). Pulsed laser fluorescence 
[... 108 more lines not kept]
```

**Agent**

Now the supplement text.

**Agent calls Bash**

```bash
cd paper; grep -n -i "supplement\|Figure S\|LOESS\|RStudio\|Table S1" 10.1016-j.xcrp.2025.102660.txt | cut -c1-300 | tail -40
```

```
5:Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
7:319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12320893 NIHMS2098259 40762005 10.1016/j.xcrp.2025.102660 Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation Semenov Iurii 1 Kim Vitalii 1 2 Silkuniene Gi
53:12, 1763. 10.1038/s41598-022-04868-x. Associated Data Supplementary Materials 1
370:##### Supplement: NIHMS2098259-supplement-1.pdf
374:Supplemental information 
384:Figure S1, related to Figure 1. Excitation and inhibition of firing in a neuron loaded with Di-8-ANEPPS 
396:Figure S2, related to Figure 1. Tetrodotoxin (TTX) abolishes both firing and sustained depolarization 
409:Figure S3, related to Figure 5. Confirmation of the increased asymmetry of membrane charging by 
470:Figure S4, related to Star Methods.  Electric field simulation for the two electrode configurations (A-C 
496:Table S1: Key Resource Table 
558:RStudio
```

**Agent calls Bash**

```bash
cd paper; sed -n 370,600p 10.1016-j.xcrp.2025.102660.txt
```

```
##### Supplement: NIHMS2098259-supplement-1.pdf

=== page 1 ===
Cell Reports Physical Science, Volume 6 
Supplemental information 
Excitation and polarization of isolated neurons 
by high-frequency sine waves 
for temporal interference stimulation 
Iurii Semenov, Vitalii Kim, Giedre Silkuniene, and Andrei G. Pakhomov 

=== page 2 ===
 
 
 
Figure S1, related to Figure 1. Excitation and inhibition of firing in a neuron loaded with Di-8-ANEPPS 
potentiometric dye. The cell was stimulated by 250-ms-long, 2-kHz sine waves at different field strengths 
(V/cm). Depolarization reduces the emission of Di-8-ANEPPS, so the optical membrane potential traces 
have been inverted to display depolarizions upward. See Figure 1 for more details. 

=== page 3 ===
[... 182 more lines not kept]
```

**Agent**

Checker passes. I've read the full text and supplement. Now applying corrections.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/001274/10.1016-j.xcrp.2025.102660.yaml'
s=open(p).read()
R=[
# header
("""# 140 V/cm pulses applied from two orthogonal directions with a three-electrode array, 160 images
# at 50-ns steps, eight replicates, 19 neurons (3 elongated parallel, 6 elongated perpendicular,
# 10 random).""",
"""# 140 V/cm pulses applied from two orthogonal directions with a three-electrode array, 160 images
# at 50-ns steps, eight replicates, 19 experiments (3 elongated parallel, 6 elongated
# perpendicular, 10 random with both orientations pooled; the paper counts experiments, not cells,
# and does not say how many cells they come from)."""),
("""# fit of the whole-cell response (Figure 5H and 6C legends). Magnitudes are compared, as the
# figures plot the hyperpolarized and depolarized ROIs as bars of one sign.""",
"""# fit of the whole-cell response (Figure 5H and 6C legends). Magnitudes are compared, as the text
# reports the sensitivities of both the hyper- and the depolarized ROIs as positive numbers (15% to
# 47% for pulses, 1.5% to 28.4% for sine waves)."""),
# fig1-pure-sine
("""  statement: Unmodulated 250-ms sine waves at 2 kHz and at 20 kHz excited every neuron tested,
    with sustained firing and no on-off response.""",
"""  statement: Unmodulated 250-ms sine waves at 2 kHz and at 20 kHz excited every neuron tested,
    never as an on-off response."""),
("""    5 ms, which also counts APs riding on a depolarization. Reproduced when, under each reading,
    at least 90% of neurons tested with each frequency are excited.""",
"""    5 ms, which also counts APs riding on a depolarization. Reproduced when, under each reading,
    at least 90% of neurons tested with each frequency are excited; blocked as
    methods_underspecified when the readings disagree."""),
# fig1-onset-delay
("""    (Spearman correlation below zero in more than half of the neurons with at least three
    sessions with APs).""",
"""    (Spearman correlation below zero in more than half of the neurons with at least three
    sessions with APs). The paper gives no test for either part; the median, the Spearman sign and
    the majority are standard choices."""),
# fig2d twofold
("""    mean 2-kHz threshold, and a two-tailed unpaired t test of the two (Methods, Quantification
    and statistical analysis). Reproduced when each ratio is within tolerance and each p < 0.0001.
    The field per session is taken from the dataset's metadata (the description of 001030 states
    1 V = 36 V/cm for this electrode; the paper shows the conversion only in Figure S4C).""",
"""    mean 2-kHz threshold, and a two-tailed unpaired t test of the two (Methods, Quantification
    and statistical analysis). The paper gives one p for "all thresholds", so which comparison it
    is open; readings (a) one test per group, each p < 0.0001, (b) one test pooling the four
    groups, 20 kHz against 2 kHz. Reproduced when each ratio is within tolerance and the test
    gives p < 0.0001 under both readings of the test; blocked as methods_underspecified when the
    readings disagree. The field per session is taken from the dataset's metadata; the paper gives
    the conversion from volts to V/cm only as the simulated profile of Figure S4C, with no number
    in the text, so a session without a recorded field is open."""),
# threshold-2khz
("""  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,
    paragraph 4; Figure 2D
  quote: the AP threshold""",
"""  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,
    paragraph 6; Figure 2D
  quote: the AP threshold"""),
("""  criterion: The mean over neurons of the 1-AP threshold as in fig2d-20khz-twofold-threshold,
    under both AP readings; reproduced when one is within tolerance (the SEM the paper gives).""",
"""  criterion: The mean over neurons of the 1-AP threshold as in fig2d-20khz-twofold-threshold,
    under both AP readings; reproduced when both are within tolerance (the SEM the paper gives),
    blocked as methods_underspecified when the readings disagree."""),
# figs1
("""    Reproduced when, under one reading, every neuron is excited, latency falls with field in more
    than half, and the highest field meets the block test in more than half.""",
"""    Reproduced when, under every reading, every neuron is excited, latency falls with field in
    more than half, and the highest field meets the block test in more than half; blocked as
    methods_underspecified when the readings disagree."""),
# fig4-orientation
("""    Figure 4D and 4E legend (parallel n = 3, perpendicular n = 6, random n = 10). The legend's n
    differ, so the paired test is read as on the elongated cells with both orientations; the
    readings for what is compared are (a) the charging tau, (b) the discharging tau, at each pole.
    Reproduced when, under each, the parallel mean is within tolerance of twice the perpendicular
    mean and both tests reach their stated p in at least one pole.""",
"""    Figure 4D and 4E legend (parallel n = 3, perpendicular n = 6, random n = 10). The text names a
    paired t test (p < 0.001) for parallel against perpendicular, while the legend marks p < 0.01
    between the orthogonal orientations with an unpaired two-tailed t test, and the group n
    differ; readings for that test are (a) paired, on the elongated cells imaged in both
    orientations, (b) unpaired, on the legend's groups. The time constants compared are the
    charging tau and the discharging tau, at each pole. Reproduced when, for both, the parallel
    mean is within tolerance of twice the perpendicular mean and of twice the random mean, and the
    parallel against random test reaches p < 0.01 and the orientation test its stated p (0.001
    paired, 0.01 unpaired) in at least one pole, under both readings; blocked as
    methods_underspecified when the readings disagree."""),
("""  expected:
    quantity: ratio of parallel to perpendicular time constants
    value: 2
    tolerance: 0.2""",
"""  expected:
  - quantity: ratio of parallel to perpendicular time constants
    value: 2
    tolerance: 0.2
  - quantity: ratio of parallel to random time constants
    value: 2
    tolerance: 0.2"""),
# fig4-no-pole
("""    the same cell, so the test is a two-sided paired t test over all 19 cells of |dFmax|, charging""",
"""    the same cell, so the test is a two-sided paired t test over all 19 experiments of |dFmax|, charging"""),
# fig4-discharging
("""    against charging tau over cells and poles. The pooling is not given; readings (a) all 19 cells,""",
"""    against charging tau over cells and poles. The pooling is not given; readings (a) all 19 experiments,"""),
# fig4-pooled
("""  statement: Pooled over all 19 cells, the charging and discharging time constants were 0.7 and
    0.91 us at the cathodic pole and 0.65 and 0.8 us at the anodic pole, so membranes charge fully
    within 3 us.""",
"""  statement: Pooled over all 19 experiments, the charging and discharging time constants were 0.7
    and 0.91 us at the cathodic pole and 0.65 and 0.8 us at the anodic pole, so membranes exceed
    95% of full charge within 3 us."""),
("""    orientation is open; readings (a) the mean over the 19 cells of each cell's mean over its
    orientations, (b) the mean over all cell and orientation fits. Reproduced when, under one""",
"""    orientation is open (the paper's n = 19 counts experiments); readings (a) the mean over all
    cell and orientation fits, (b) the mean over cells of each cell's mean over its orientations.
    Reproduced when, under one"""),
# fig5-carrier
("""    (O3, reading a) has opposite signs in the two ROIs. The whole-cell depolarization is tested
    in fig5-whole-cell-depolarization.""",
"""    (O3, reading a) has opposite signs in the two ROIs. The paper gives no test; the spectral
    peak, the Pearson correlation and the sign of the regression are standard choices, with the
    Methods' p < 0.05. The whole-cell depolarization is tested in fig5-whole-cell-depolarization."""),
# fig5-whole-cell
("""  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,
    paragraph 2; Figures 5C and 5D
  quote: These high-frequency""",
"""  source: Figure 5C and 5D legend; Figures 5C and 5D
  quote: These high-frequency"""),
# fig5fg
("""    14 have the sign of the Figure 5F ROIs' median, and the largest |sensitivity| among the
    Figure 5G ROIs is below the largest among the Figure 5F ROIs.""",
"""    14 have the sign of the Figure 5F ROIs' median, and the largest |sensitivity| among the
    Figure 5G ROIs is below the largest among the Figure 5F ROIs. Which of the 16 ROIs belong to
    Figure 5F and which to 5G is shown only in the figure (the text says only that they lie on
    opposite sides of the cell, with 10 to 14 in 5G); without that split from the dataset the
    claim is blocked as metadata_insufficient."""),
# fig6b
("""    without debris scaling. Reproduced when, under one of the two, the mean over the 18 ROIs is
    within tolerance (the SEM the paper gives) and every ROI lies within 13.5% to 51.7% (15% to 47%
    widened by 10% of each bound).""",
"""    without debris scaling. Reproduced when, under both, the mean over the 18 ROIs is within
    tolerance (the SEM the paper gives) and every ROI lies within 13.5% to 51.7% (15% to 47%
    widened by 10% of each bound); blocked as methods_underspecified when the two disagree."""),
]
for a,b in R:
    assert s.count(a)==1, a[:80]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  f=claims/001274/10.1016-j.xcrp.2025.102660.yaml; sed -i 's/opposite sides of the cell, with 10 to 14 in 5G); without/opposite sides of the cell, with 12 to 14 in 5G); without/' $f; grep -n "^checks" $f; cat >> $f <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - header, Figure 4 data. "19 neurons" changed to 19 experiments; the paper counts experiments (Results, paragraph on Figures 4D and 4E; legend ALL n = 19), and parallel n = 3 with perpendicular n = 6 cannot be the same cells.
  - header, magnitudes. The reason given (bars of one sign in figures the reader says it could not see) replaced by the text's basis, positive sensitivities reported for both ROIs.
  - fig1-pure-sine-excites-all. Statement no longer says every neuron fired in a sustained way; the paper says sustained firing only at higher fields. Criterion adds the protocol's rule for AP detection readings that disagree.
  - fig1-onset-delay. Criterion now says the median, Spearman sign and majority are standard choices; the paper gives no test.
  - fig2d-20khz-twofold-threshold. The paper gives one p for all thresholds; criterion names the per-group and pooled readings. Removed the 1 V = 36 V/cm conversion taken from the description of DANDI:001030, which is not from the paper; the conversion is named as open.
  - threshold-2khz-unmodulated. Source corrected to paragraph 6 (the quote is in the paragraph starting "Using FluoVolt's sine wave sensitivity"). AP detection is a method detail, so both readings must agree (was one).
  - figs1-di8-anepps-control. Same change, every reading must agree (was one), as the detection level is a method detail.
  - fig4-orientation-time-constants. The legend's unpaired p < 0.01 between orientations conflicts with the text's paired p < 0.001; criterion names both readings. Added the expected parallel to random ratio, as the statement and quote claim doubling against random cells too.
  - fig4-no-pole-difference, fig4-discharging-slower. "19 cells" changed to 19 experiments, as above.
  - fig4-pooled-time-constants. "19 cells" changed to 19 experiments; "charge fully" changed to the paper's "exceed 95% of full charge" within 3 us; readings reordered with the per-fit mean first, as n = 19 counts experiments.
  - fig5-carrier-antiphasic. Criterion now says the spectral peak, correlation and regression sign are standard choices; the paper gives no test.
  - fig5-whole-cell-depolarization. Source corrected to the Figure 5C and 5D legend, where the quote is.
  - fig5fg-no-migration. Criterion now says the split of the 16 ROIs between Figures 5F and 5G is only in the figure, and blocks the claim without it.
  - fig6b-pulse-sensitivity. Criterion required one of the two scalings; the header and Methods say both are run, so both must agree.
  - open. The LOESS span and degree (O2), the form of the sine wave regression (O3), the ROIs (O1) and the identity of cells C7 and C8 (O4) are not in the paper and stay open as the header names them.
  - open. The figure-to-dandiset mapping is read from dandiset titles only; the paper gives none. Whether the 2-us pulse recordings of the cells of Figures 5 and 6 are in 001274 or 001273 is unknown.
  - open. Paragraph numbers in the Kinetics section could not be confirmed, as the text has no paragraph breaks and no main-text PDF was available.
EOF
python tools/claims_check.py $f paper/10.1016-j.xcrp.2025.102660.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for DANDI:001274 against the full text and the supplement, made 14 corrections, and the file is ready for an attempt.

**Checker result** (the same before and after my edits): `26 claims, 26 quotes, 8 statistical values, 0 problems`

**Changes, by claim:**
- **Header:**
  - The paper's Figure 4 n = 19 counts experiments, not neurons, so "19 neurons" is now "19 experiments". The groups (3 parallel, 6 perpendicular) cannot be the same cells.
  - The header compared magnitudes because "the figures plot bars of one sign", but it also says the figures could not be seen. I replaced that reason with the text's: both ROIs' sensitivities are reported as positive numbers.
- **fig1-pure-sine-excites-all:** the statement said every neuron fired in a sustained way. The paper says that only for stronger fields, so I removed it. The criterion now applies the protocol's rule when the AP detection readings disagree.
- **fig1-onset-delay, fig5-carrier-antiphasic:** the tests in these criteria were invented without saying so. They are now labelled as standard choices, since the paper gives no test.
- **fig2d-20khz-twofold-threshold:**
  - The paper gives a single p for "all thresholds". The criterion now names two readings: one test per group, or one pooled test.
  - I removed a 1 V = 36 V/cm conversion taken from the DANDI:001030 description, which is not from the paper. The conversion is now marked as open.
- **threshold-2khz-unmodulated:** the source is now paragraph 6 (it said paragraph 4). Both AP detection readings must now agree (it accepted either one).
- **figs1-di8-anepps-control, fig6b-pulse-sensitivity:** these accepted "one reading" or "one of the two scalings". Both are method details, so all readings must now agree. That also matches the header's own rule on scaling.
- **fig4-orientation-time-constants:**
  - The text names a paired t test (p < 0.001), while the Figure 4 legend marks an unpaired test (p < 0.01). The criterion now names both readings.
  - I added the parallel-to-random ratio as an expected value, since the statement claims doubling against random cells too.
- **fig4-no-pole-difference, fig4-discharging-slower, fig4-pooled-time-constants:** "19 cells" is now "19 experiments". In fig4-pooled, "charge fully" is now the paper's wording, "exceed 95% of full charge" within 3 µs.
- **fig5-whole-cell-depolarization:** the source is now the Figure 5C and 5D legend, where the quote actually is.
- **fig5fg-no-migration:** which of the 16 ROIs belong to Figure 5F and which to 5G is shown only in the figure. Without that split from the dataset, the claim is now blocked as `metadata_insufficient`.

**Still open** (recorded in the checks entry):
- These details are not in the paper and stay open as the header names them:
  - the ROIs (O1)
  - the LOESS span and degree (O2)
  - how the field enters the sine-wave regression (O3)
  - which recordings are cells C7 and C8 (O4)
- Which figure is in which dandiset is read only from the dandisets' titles; the paper gives no mapping. It is unknown whether the 2-µs pulse recordings of the Figure 5 and 6 cells are in 001274 or 001273.
- I could not confirm the paragraph numbers in the Kinetics section: the text has no paragraph breaks and there is no main-text PDF.

**Ready:** yes. The checks entry is appended with `ready: true`. Nothing is committed.

## End of run

12 turns, 2 minutes, result: success.
