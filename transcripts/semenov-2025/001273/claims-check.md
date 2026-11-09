# 001273 · claims-check · run 39751064091

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001273/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; python tools/claims_check.py claims/001273/*.yaml paper/*.txt; cat claims/001273/*.yaml; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9f047347-fb9a-47d2-bd7d-31aec3585f40/tool-results/bvggto1zw.txt"
}
```

```
1	## Reader
2	
3	### 1. Get the paper
4	
5	The workflow puts the paper's full text, and its PDF where there is one, under
6	`paper/`: the main text, the Methods, and the supplement. Read the text; open
7	the PDF only to read a figure or a table the text garbles. If the full text is
8	not there, or lacks the Methods or a supplement the results rest on, stop:
9	write no claims, and end with a report that names what is missing, so that it
10	can be supplied. Never write claims from the abstract. Do not copy figures.
11	Do not look at the dataset's data: its title and description on the archive
12	are enough to know which paper and which experiments it is meant to hold.
13	
14	### 2. Read the paper's code
15	
16	Read the code the paper links to before writing criteria. Say what it holds,
17	and record the repository and commit read. Where the Methods leave a choice
18	open and the code settles it, follow the code and say so. Where they disagree,
19	follow the Methods for the main result and name the code's choice as a
20	variant. When more sources disagree (the Methods, the analysis code, the
[... 568 more lines not kept]
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
print(t[52400:80000])"
```

```
ontinued for 250 ms during and about 90 ms after the stimulation, generating 1,200 images per stimulation session. After the first session, the stimulus amplitude was increased if no APs were detected or decreased to find the threshold if multiple APs were evoked. The imaging/stimulation sessions were repeated multiple times with 20–60 s intervals between them, either at escalating voltages or by choosing voltages randomly. In experiments aimed at determining the excitation thresholds ( Figure 2D ), the sine wave amplitude was adjusted up or down in 5%–10% steps until the minimal voltages eliciting 1 and 5 APs were determined. Next, we switched to a different stimulus type (e.g., from a modulated to an unmodulated signal or from 2 to 20 kHz) and repeated the search for the 1- and 5-AP thresholds. The emission intensity over the entire cell soma (F) was quantified using either Fiji ImageJ 1.53C (National Institutes of Health, USA) or MetaMorph 7.7 (Molecular Devices, San Jose, CA). The mean value over a time interval preceding the electrical stimulation was used as a 100% reference ( F 0 ) . Emission change in each frame ( Δ F ) in the sequence was determined as Δ F = 100 % × ( F − F 0 ) ∕ F 0 . APs were readily identifiable as brief emission upticks. For experiments, we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical values: 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM, n = 22). Traces of the optical membrane potential were not filtered or modified in any way (except for long recordings in Figure 3C , which were corrected for bleaching by subtracting a trace without APs). The maximum AP firing rate was measured as the inverse of the peak-to-peak time interval between the first two APs evoked in each stimulation session. Traces of the optical membrane potential, as well as other graphs, were generated with Grapher v.16 software (Golden Software, Golden, CO). Pulsed laser fluorescence mi
[... 55 more lines not kept]
```

**Agent**

The checker passes (15 claims, 0 problems). The main text is read; next I check the supplement legends and then go through each claim.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1016-j.xcrp.2025.102660.txt').read()
i=t.find('SUPPLEMENT'); i = i if i>0 else t.find('Figure S1.')
print(i); import re
for m in re.finditer(r'Figure S[1-4]\b',t): pass
j=t.rfind('--- supplement'); print(j)
print(t[-9000:])" | grep -v '^journal=' | head -120
```

```
-1
-1
ns. JAMA Neurol.. 2018. 10.1001/jamaneurol.2018.2760

[27] Improving the Effect of Transcranial Alternating Current Stimulation (tACS): A Systematic Review. Front. Hum. Neurosci.. 2021. 10.3389/fnhum.2021.652393

[28] Feasibility of Interferential and Pulsed Transcranial Electrical Stimulation for Neuromodulation at the Human Scale. Neuromodulation. 2021. 10.1111/ner.13137

[29] A deeply superficial brain stimulation. Mov. Disord.. 2017. 10.1002/mds.27111

[30] There is no Biophysical Distinction between Temporal Interference Stimulation and Direct kHz Stimulation for Actuation of Peripheral Nerves. bioRxiv. 2024.

[31] Effects of uniform extracellular DC electric fields on excitability in rat hippocampal slices in vitro. J. Physiol.. 2004. 10.1113/jphysiol.2003.055772

[32] Cell-specific effects of temporal interference stimulation on cortical function. Commun. Biol.. 2024. 10.1038/s42003-024-06728-y

[33] Untersuchungen über die Wirkung der Mittelfrequenzströme auf den Menschen. Pflügers. Arch.. 1944. 10.1007/BF01759722

[34] Über den Mechanismus der Reizwirkung mittelfrequenter Wechselströme auf die Nervenmembran. Pflugers Arch. für Gesamte Physiol. Menschen Tiere. 1966. 10.1007/BF00363808

[... 101 more lines not kept]
```

**Agent**

Checker: 15 claims, 0 problems. Now checking cross-references and the allowed outcome vocabulary.

**Agent calls Bash**

```bash
cd  ls claims/001274/ 2>&1; grep -n "^- id:" claims/001274/*.yaml; grep -rn "partial" docs/protocol.md | head; grep -n "methods_underspecified\|metadata_insufficient" docs/*.md | head -5
```

```
10.1016-j.xcrp.2025.102660.yaml
83:- id: fig1-pure-sine-excites-all
104:- id: fig1-onset-delay
122:- id: fig1-max-rate-ceiling
138:- id: fig1-excitation-block
154:- id: fig2d-20khz-twofold-threshold
184:- id: fig2d-modulated-thresholds-higher
213:- id: threshold-2khz-unmodulated
230:- id: fig2-modulated-locks-to-beats
247:- id: fig2c-pure-more-aps
259:- id: fig3b-low-conductivity-halves-threshold
278:- id: fig3c-sustained-firing-2s
296:- id: figs1-di8-anepps-control
314:- id: figs2-ttx-blocks-depolarization
327:- id: fig4-orientation-time-constants
366:- id: fig4-no-pole-difference
383:- id: fig4-discharging-slower
404:- id: fig4-pooled-time-constants
440:- id: fig5-carrier-antiphasic
457:- id: fig5-whole-cell-depolarization
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '1,82p;154,260p;543,660p' claims/001274/*.yaml
```

```
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001274.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with
# its main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available, so Figures 1 to 6 could not be looked at; numbers shown only in figures are not used.
#
# Code. The paper states that it does not report original code. Analyses were done with Fiji or
# MetaMorph (ROI intensities), Origin 8.0 (exponential fits), Grapher 16 (linear regression) and,
# per Table S1, RStudio 2024.04.2 (the LOESS fits are read here as R's loess, see below).
#
# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one
# week on coverslips, stained with FluoVolt (Di-8-ANEPPS in Figure S1). Two kinds of recording:
# (1) Fast imaging of the optical membrane potential (64 x 64 pixels, 3,130 or 3,086.4 frames/s,
# 1,200 images per session, 50 ms before, 250 ms during and about 90 ms after the stimulus), with
# 250-ms unmodulated or 20-Hz amplitude-modulated sine waves at 2 and 20 kHz (Figures 1, 2), in
[... 281 more lines not kept]
```

**Agent**

Several problems found. Making the edits now.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/001273/10.1016-j.xcrp.2025.102660.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)

# header: 001031
rep("""# 5, 6, S3), 001030 and 001032 to 001035 the 250-ms and 2-s sine wave stimulation (Figures 1 to 3).
""","""# 5, 6, S3), 001030 and 001032 to 001035 the 250-ms and 2-s sine wave stimulation (Figures 1 to 3).
# The paper also lists 001031, which no claim here is assigned to.
""")

# fig4-polarized: per shape group
rep("""    paper gives no measure; reproduced when, in more than half of the experiments, the extreme""",
"""    paper gives no measure; reproduced when, in more than half of the experiments of each shape
    group of the Figure 4D and 4E legend (or of all 19 when the labels are missing, O4), the extreme""")

# fig4-orientation criterion
rep("""    on elongated cells imaged in both orientations, (b) unpaired, on the legend's groups. Reproduced
    when, for charging and for discharging tau, the parallel mean is within tolerance of twice the
    perpendicular mean and of twice the random mean at both poles, and parallel against random
    reaches p < 0.01 and the orientation test its stated p (0.001 paired, 0.01 unpaired) at one pole
    at least, under every reading of the header (O1 to O3, F2) and both readings of the test;
    blocked as methods_underspecified when they disagree. The ratios at each pole are reported.""",
"""    on elongated cells imaged in both orientations, (b) unpaired, on the legend's groups. Which time
    constants "the time constants" means is not given, and the text's first sentence names charging
    only; readings of the subset (i) charging tau, (ii) charging and discharging tau, each at both
    poles. Reproduced when, under one subset reading, the parallel mean is within tolerance of twice
    the perpendicular mean and of twice the random mean, and parallel against random reaches
    p < 0.01 and the orientation test its stated p (0.001 paired, 0.01 unpaired) at one pole at
    least, under every reading of the header (O1 to O3, F2) and both readings of the test; blocked
    as methods_underspecified when they disagree. The ratios at each pole are reported.""")

# fig4-pooled: drop reading (b)
rep("""  criterion: Fits as in the header; random cells with both orientations pooled (Figure 4D and 4E
    legend). What ALL averages over is open (O5); readings (a) the mean over all experiment fits,
    n = 19, (b) the mean over cells of each cell's mean over its orientations. Tolerances are the
    SEMs the paper gives. Reproduced when all four are within tolerance under one of (a) or (b),
    with every reading of the header (O1 to O3, F2) giving that outcome; blocked as
    methods_underspecified when the header's readings disagree. The SEMs are reported.""",
"""  criterion: Fits as in the header. The mean over all 19 experiment fits, as the text (n = 19) and
    the Figure 4D and 4E legend (ALL, n = 19, all cells and all orientations) give it. Tolerances
    are the SEMs the paper gives. Reproduced when all four are within tolerance, with every reading
    of the header (O1 to O3, F2) giving that outcome; blocked as methods_underspecified when the
    header's readings disagree. The SEMs are reported.""")

# fig1: onset delay judged
rep("""    unit: Hz
  criterion: AP detection is given only""","""    unit: Hz
  - quantity: first-AP latency at each neuron's lowest exciting field, median over neurons
    value: 155
    tolerance: 65
    unit: ms
  criterion: AP detection is given only""")
rep("""    its midpoint and half-width); blocked as methods_underspecified when the readings disagree. Onset delay and block
    are reported.""","""    its midpoint and half-width), and the median first-AP latency at threshold lies within 90 to
    220 ms (the reported 100 to 200 ms widened the same way); blocked as methods_underspecified
    when the readings disagree. The median over neurons is a standard choice. The block is
    reported, not judged.""")

# fig2d: add 20 vs 2 kHz test
rep("""    fig1-pure-sine-excites-all, both readings. Two-tailed unpaired t tests as the text names them.
    Reproduced when each ratio is within tolerance and the three modulated pairs are higher with
    p < 0.05 (Methods) under both readings.""","""    fig1-pure-sine-excites-all, both readings. Two-tailed unpaired t tests as the text names them.
    The paper gives one p for 20 against 2 kHz over "all thresholds"; readings (a) one test per
    stimulus and AP count, each p < 0.0001, (b) one test pooling the four. Reproduced when each
    ratio is within tolerance, 20 against 2 kHz reaches p < 0.0001 under both readings of that
    test, and the three modulated pairs are higher with p < 0.05 (Methods), under both AP readings;
    blocked as methods_underspecified when the readings disagree.""")

# fig5 criterion
rep("""  criterion: Measures and readings as in the claims file for DANDI:001274 (fig5-sine-asymmetry-c7 and
    figs3-sine-asymmetry-c8), which tests this finding on its own data. Reproduced when all four
    values are within tolerance under the readings that file names.""","""  criterion: Measures and readings as in the claims file for DANDI:001274 (fig5-sine-asymmetry-c7,
    figs3-sine-asymmetry-c8, fig5-carrier-antiphasic and fig5-whole-cell-depolarization), which
    tests this finding on its own data. Reproduced when all four values are within tolerance and
    the antiphasic oscillations and whole-cell depolarization are found, under the readings that
    file names.""")

# threshold: add 57.7 and propagate tolerance
rep("""  expected:
  - quantity: emission change at the 2-kHz AP threshold
    value: 0.68
    tolerance: 0.11
    unit: percent
  - quantity: depolarization at the 2-kHz AP threshold
    value: 6.8
    tolerance: 0.68
    unit: mV""","""  expected:
  - quantity: mean unmodulated 2-kHz 1-AP threshold
    value: 57.7
    tolerance: 3.6
    unit: V/cm
  - quantity: emission change at the 2-kHz AP threshold
    value: 0.68
    tolerance: 0.11
    unit: percent
  - quantity: depolarization at the 2-kHz AP threshold
    value: 6.8
    tolerance: 1.1
    unit: mV""")
rep("""    (the calibration of reference 47 as the paper uses it). Reproduced when both are within
    tolerance.""","""    (the calibration of reference 47 as the paper uses it). Tolerances are the SEMs the paper gives,
    the last being the 0.11% times 10 mV per 1%. Reproduced when all three are within tolerance.""")

# new claims appended after fig2d claim: insert before fig3b
new = """- id: fig2-modulated-locks-to-beats
  statement: With 20-Hz modulation, firing above threshold locked to the beats, one AP near the peak
    of each of the five beats and at most two per beat (ten in all), and modulated sine waves
    triggered no sustained firing or sustained depolarization.
  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 1; Figures 2A
    and 2B
  quote: single APs emerged near the peak of each beat, so the firing rate equaled the modulation
    rate ... the maximum number of APs evoked by five beats was limited to ten. Unlike pure sine
    waves, modulated stimuli did not trigger sustained firing or sustained depolarization
  data: elsewhere
  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)
  depends_on:
  - fig1-pure-sine-excites-all
  criterion: AP detection as in fig1-pure-sine-excites-all, both readings. Modulated sessions only.
    Reproduced when no session has more than 10 APs, in sessions with 5 APs or more most APs fall
    in the half of each 50-ms beat around its peak (12.5 to 37.5 ms into the beat), and no session
    ends without APs in its last 100 ms with mean dF there above 5% (the block test of
    fig3c-sustained-firing-2s). The paper does not quantify "near the peak"; the window, the
    majority and the block test are standard choices, and the AP phase histogram is reported.
- id: fig2c-pure-more-aps
  statement: In the same neuron at the same field strength, pure sine waves triggered more APs than
    modulated ones.
  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 2; Figure 2C
  quote: At the same field strengths, pure sine waves triggered a larger number of APs
  data: elsewhere
  where: DANDI:001032, 001033, 001034 and 001035 (assigned from their titles)
  depends_on:
  - fig1-pure-sine-excites-all
  criterion: AP detection as in fig1-pure-sine-excites-all, both readings. Pairs are a neuron's
    modulated and unmodulated sessions at the same carrier and the same field. The paper reports
    no test; reproduced when the unmodulated count is larger in more pairs than the reverse under
    both readings. A two-sided paired t test of the counts (the Methods' general test) is reported.
- id: fig3b-low-conductivity-halves-threshold
"""
rep("- id: fig3b-low-conductivity-halves-threshold\n", new)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001273/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='claims/001273/10.1016-j.xcrp.2025.102660.yaml'
s=open(p).read()
a="""in the half of each 50-ms beat around its peak (12.5 to 37.5 ms into the beat), and no session
    ends without APs in its last 100 ms with mean dF there above 5% (the block test of
    fig3c-sustained-firing-2s). The paper"""
b="""in the half of each 50-ms beat around its peak (12.5 to 37.5 ms into the beat), and no session
    has, over the last 100 ms of the stimulus, no APs with mean dF above 5% (the block test of
    fig3c-sustained-firing-2s applied to that window). The paper"""
assert s.count(a)==1; s=s.replace(a,b)
s=s.rstrip('\n')+'\n'+"""checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - header. Added that the paper also lists DANDI:001031, which no claim is assigned to (Data and code availability lists ten dandisets, the header named nine).
  - fig4-polarized-poles-face-electrodes. The majority is now required in each shape group, as the text says "In neurons of all shapes"; a majority over all 19 could be met by the random group alone.
  - fig4-orientation-time-constants. Criterion required the doubling for both charging and discharging tau; the text's first sentence names charging only, and its next finding (discharging larger than charging except in elongated parallel cells) makes a discharging ratio of 2 unlikely by the paper's own account. The subset is now named as open, with readings charging only, and charging and discharging.
  - fig4-pooled-time-constants. Removed reading (b), a mean over cells; the text and the legend both give n = 19 for ALL, so the paper's mean is over the 19 experiment fits.
  - fig1-pure-sine-excites-all. The statement's 100 to 200 ms onset delay was only reported; it is a reported range, so it is now an expected value judged by the protocol's range rule (90 to 220 ms). The median over neurons is named as a standard choice.
  - fig2d-modulated-thresholds-higher. The recorded p < 0.0001 for 20 against 2 kHz was not used by the criterion; added it, with the per-group and pooled readings of "all thresholds", and the rule for disagreeing readings.
  - fig5-sine-asymmetry. The statement includes the antiphasic oscillations and the whole-cell depolarization; the criterion now judges them through the matching claims of the DANDI:001274 file.
  - threshold-depolarization-estimate. Added the 57.7 plus or minus 3.6 V/cm threshold the estimate rests on (Results, Figure 2D) as an expected value. The 6.8 mV tolerance changed from 10% to 1.1 mV, the paper's 0.11% times its 10 mV per 1% calibration, as the protocol asks for the paper's own uncertainty.
  - fig2-modulated-locks-to-beats. New claim, data elsewhere; a main finding (Results on Figures 2A and 2B, and the Highlights) had none.
  - fig2c-pure-more-aps. New claim, data elsewhere; the Figure 2C finding had none.
  - open. Several criteria rest on measures the paper does not give and that the file names as standard choices (the centroid and 45 degrees of fig4-polarized-poles-face-electrodes, the 5% level and windows of fig3c, figs1, figs2 and fig2-modulated-locks-to-beats, the AP detection readings). They could change outcomes; the paper offers nothing to replace them.
  - open. Whether the 60 to 90 Hz ceiling is meant for the median neuron or for every neuron (the inset shows three) is not settled by the text.
  - open. fig4-no-pole-difference uses a paired t test, which the paper does not name for this comparison; the Methods only say paired or unpaired as appropriate.
  - open. fig6-sine-less-than-pulse and fig5-sine-asymmetry take their readings from the DANDI:001274 claims file, which reads the same paper; the figure-to-dandiset mapping is read from titles only.
  - open. Paragraph numbers in sources could not be confirmed, as the text has no paragraph breaks and no main-text PDF was available.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001273/*.yaml paper/*.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/001273/*.yaml; python3 -c "import yaml;d=yaml.safe_load(open('claims/001273/10.1016-j.xcrp.2025.102660.yaml'));print(len(d['claims']),d['checks'][-1]['ready'])"
```

```
17 True
```

**Agent**

I checked the file against the paper and corrected it. It is ready for an attempt.

**Checker result** (after my edits): `claims/001273/10.1016-j.xcrp.2025.102660.yaml: 17 claims, 17 quotes, 9 statistical values, 0 problems`. The original 15 claims also passed with 0 problems.

**Changes, by claim**
- **Header:** it named only nine of the ten dandisets the paper lists. I added DANDI:001031, which no claim uses.
- **fig4-polarized-poles-face-electrodes:** the paper says "In neurons of all shapes", so the majority is now required within each shape group. A majority over all 19 experiments could have been met by the random-shape group alone.
- **fig4-orientation-time-constants:** the criterion required the 2-fold ratio for both charging and discharging time constants. The text names charging first, and its own next finding (discharging is slower except in aligned elongated cells) makes a discharging ratio of 2 unlikely. The subset is now open, with two readings: charging only, and charging plus discharging.
- **fig4-pooled-time-constants:** I removed the "mean over cells" reading. Both the text and the legend give n = 19 experiments.
- **fig1-pure-sine-excites-all:** the statement's 100 to 200 ms onset delay was reported but not judged. It is now an expected value, judged at 90 to 220 ms under the protocol's rule for ranges.
- **fig2d-modulated-thresholds-higher:** the criterion ignored the recorded p < 0.0001 for 20 kHz against 2 kHz. I added it, with two readings: one test per stimulus group, or one pooled test.
- **fig5-sine-asymmetry:** the statement includes the antiphasic oscillations and the whole-cell depolarization. The criterion now judges them too.
- **threshold-depolarization-estimate:** I added the 57.7 ± 3.6 V/cm threshold the estimate rests on as an expected value. The 6.8 mV tolerance is now 1.1 mV, carried from the paper's ± 0.11%, in place of a 10% default.
- **New claims** for two main findings that had none, both on data in other dandisets: `fig2-modulated-locks-to-beats` (Figures 2A and 2B) and `fig2c-pure-more-aps` (Figure 2C).

**What remains open** (recorded in the checks entry)
- Several criteria use measures the paper does not give, labelled as standard choices: the centroid and 45-degree rule for the poles, the 5% depolarization level and time windows, and the readings for detecting action potentials. These could change outcomes, and the paper offers nothing to replace them.
- The 60 to 90 Hz firing-rate ceiling could mean the median neuron or every neuron; the text does not say.
- The paper names no test for "no difference between poles". The criterion uses a paired t test, and the Methods only say "paired or unpaired as appropriate".
- The Figure 5 and 6 claims take their method readings from the DANDI:001274 claims file, which reads the same paper.
- Which figure is in which dandiset is read from dandiset titles only.
- Paragraph numbers in the sources cannot be confirmed, because the text has no paragraph breaks.

**Ready:** yes (`ready: true`). Nothing is committed.

## End of run

12 turns, 3 minutes, result: success.
