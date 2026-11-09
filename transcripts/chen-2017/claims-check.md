# 000015 · claims-check · run 39636626896

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000015 paper/ | head; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; cat claims/000015/*.yaml; python tools/claims_check.py claims/000015/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/95aac7b7-ba6d-462e-aad9-9b7e0bde0b2d/tool-results/b18bne9mn.txt"
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
[... 714 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/95aac7b7-ba6d-462e-aad9-9b7e0bde0b2d/tool-results/b0h2a0e5r.txt",
 "offset": 60,
 "limit": 700
}
```

```
60	behavioral response. Later, widely distributed neurons represented the outcome of the trial. Cortical
61	area was more predictive of neuronal selectivity
62	than laminar location or axonal projection target.
63	Motor cortex therefore represents sensory, motor,
64	and outcome information in a spatially organized
65	manner.
66	INTRODUCTION
67	The motor cortex plays roles in planning and executing voluntary
68	movements (Shenoy et al., 2013). Activating different regions of
69	the motor cortex causes movements of specific body parts (Komiyama et al., 2010; Li et al., 2015; Matyas et al., 2010; Neafsey
70	et al., 1986; Tennant et al., 2011; Travers et al., 1997). Consistent
71	with a role in controlling movement, motor cortex neurons
72	encode variables related to movement, such as movement
73	direction and speed as well as muscle force (Scott, 2008).
74	Motor cortex activity also anticipates movement. In delayed
75	response tasks, motor cortex neurons show preparatory activity,
76	which predicts specific movements, including arm movements
77	(Crutcher and Alexander, 1990; Riehle and Requin, 1989; Tanji
78	and Evarts, 1976), eye movements (Bruce and Goldberg,
79	1985), body orienting (Erlich et al., 2011), and tongue movements
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/95aac7b7-ba6d-462e-aad9-9b7e0bde0b2d/tool-results/b0h2a0e5r.txt",
 "offset": 760,
 "limit": 700
}
```

```
760	for trial outcome were observed in both ALM and MM. Similarly,
761	mixed neurons were observed both in ALM and MM during the
762	response epoch.
763	Projection-Specific Coding
764	The diverse neuronal responses in ALM (Li et al., 2015) and
765	primary motor cortex (Turner and DeLong, 2000) correlate with
766	specific neuronal projection types. We asked whether projection
767	type and cortical layer explain differences in responses across
768	neurons. In three mice, we combined retrograde labeling of
769	pyramidal tract (PT) (n = 719) and intratelencephalic (IT) (n =
770	2,631) neurons with two-photon calcium imaging (Figure 8A).
771	We divided cortical depth into superficial (<350 mm deep;
772	including L1–3) and deep (>350 mm deep; including L5A and
773	5B) layers (Hooks et al., 2013; Li et al., 2015; Mao et al., 2011).
774	IT neurons were found in both superficial and deep layers,
775	whereas PT neurons were exclusively in deep layers (Figure 8C).
776	In ALM, the strongest lick direction selectivity was observed in
777	the deep layers (Figures 8D and S10), where PT and IT neurons
778	were intermingled. A contra bias during the delay epoch was
779	error right; red dashed line, error left. The three dotted vertical lines demarcate the sample and delay epochs. The blue and red dots on the black and white image
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/95aac7b7-ba6d-462e-aad9-9b7e0bde0b2d/tool-results/b0h2a0e5r.txt",
 "offset": 1460,
 "limit": 470
}
```

```
1460	Akerboom, J., Chen, T.W., Wardill, T.J., Tian, L., Marvin, J.S., Mutlu, S.,
1461	Caldero ́ n, N.C., Esposti, F., Borghuis, B.G., Sun, X.R., et al. (2012).
1462	Optimization of a GCaMP calcium indicator for neural activity imaging.
1463	J. Neurosci. 32, 13819–13840.
1464	Amador, N., Schlag-Rey, M., and Schlag, J. (2000). Reward-predicting and
1465	reward-detecting neuronal activity in the primate supplementary eye field.
1466	J. Neurophysiol. 84, 2166–2170.
1467	Amiez, C., Joseph, J.P., and Procyk, E. (2006). Reward encoding in the monkey anterior cingulate cortex. Cereb. Cortex 16, 1040–1055.
1468	Brecht, M. (2011). Movement, confusion, and orienting in frontal cortices.
1469	Neuron 72, 193–196.
1470	Brown, S.P., and Hestrin, S. (2009). Intracortical circuits of pyramidal neurons
1471	reflect their long-range axonal targets. Nature 457, 1133–1136.
1472	Bruce, C.J., and Goldberg, M.E. (1985). Primate frontal eye fields. I. Single neurons discharging before saccades. J. Neurophysiol. 53, 603–635.
1473	Chakrabarti, S., Zhang, M., and Alloway, K.D. (2008). MI neuronal responses to
1474	peripheral whisker stimulation: relationship to neuronal activity in si barrels and
1475	septa. J. Neurophysiol. 100, 50–63.
1476	Chen, T.-W. (2008). A Systems level analysis of neuronal network function in
1477	the olfactory bulb: coding, connectivity, and modular organization. PhD
1478	Thesis (University of Go ̈ ttingen).
1479	Chen, T.W., Wardill, T.J., Sun, Y., Pulver, S.R., Renninger, S.L., Baohan, A.,
[... 443 more lines not kept]
```

**Agent**

Checker reports 31 claims, 0 problems. Now checking paragraph boundaries and figure panel times in the PDF, since several sources and one criterion depend on them.

**Agent calls Bash**

```bash
cd paper && python -c "
import fitz
d=fitz.open('10.1016-j.neuron.2017.05.005.pdf')
for pn in [7,9,11,12]:
  p=d[pn]
  for b in p.get_text('dict')['blocks']:
    for l in b.get('lines',[]):
      t=''.join(s['text'] for s in l['spans'])
      if len(t)>25: print(pn+1, round(l['bbox'][0]), t[:70])
" | grep -v '^.. *[0-9][0-9]*$' | head -400
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd  python -c "import pypdf" 2>&1; which pdftotext; python -c "import pdfplumber" 2>&1
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
 "file_path": "paper/10.1016-j.neuron.2017.05.005.pdf",
 "pages": "8-12"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn -i "with_inputs\|with_labels\|elsewhere" docs/*.md | head -30
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:49:  Elsewhere it may mean "some panels yes, some no". The pilot should show
docs/pilot-notes.md:584:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:596:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:674:tested claims are `with_inputs`, and the dandiset is judged on two. A link
docs/pilot-notes.md:729:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:979:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:983:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pilot-notes.md:1060:protocol to pilot-7 after checking that no claim needed the `elsewhere`
docs/pilot-notes.md:2761:only for comparison makes a claim `with_inputs`; and a notebook that streams
docs/pilot-notes.md:2848:repository of per-mouse figure values counts as data deposited elsewhere; a
docs/pilot-notes.md:3413:data on OSF and data public nowhere, which the rule that elsewhere is never
docs/pilot-notes.md:3514:no blocking reason for a claim on data elsewhere that could be tested but was
docs/pilot-notes.md:3715:masks that name pixels but bring no measurements, which `with_labels` does not
docs/pilot-notes.md:3894:spine and rotation choices are not fully consistent; whether `elsewhere`
docs/pilot-notes.md:4111:dandiset; per-slice summary data classed as `data: elsewhere`; a clock check
docs/pilot-notes.md:4310:that is a partial copy of the paper's own deposit, tested as `elsewhere`; a
docs/pilot-notes.md:4606:elsewhere; and runtime advice that was not enough to keep loading short.
docs/pilot-notes.md:5419:`methods_underspecified` because their data are public elsewhere and the paper
docs/pilot-notes.md:5501:table are neither `with_labels` nor `with_inputs`; it only implies that the
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 195,255p docs/protocol.md; sed -n 975,990p docs/pilot-notes.md
```

```
why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
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
[... 56 more lines not kept]
```

**Agent**

The PDF cannot be rendered here (no poppler), so I'm working from the text. Making the edits now.

**Agent calls Bash**

```bash
cd claims/000015 && python - <<'EOF'
import re
f='10.1016-j.neuron.2017.05.005.yaml'
s=open(f).read()
reps=[
# fig6-object-location-mm: Figure 6D time
("""    (the sample epoch and the first second of the delay; "early part" is not defined, and a
    window ending 1.5 s, the time of Figure 6D, is also read).""",
"""    (the sample epoch and the first second of the delay; "early part" is not defined, and a
    window ending 2.7 s, the time of Figure 6D, the last panel the sentence cites, is also read).
    Figure 6 panels B to G are at 0.9, 1.5, 2.7, 3.9, 4.5 and 5.1 s after trial start (figure
    labels, in order); this is read from the extracted text, as the PDF could not be rendered."""),
# fig6-lick-direction-deep-alm-first: early in delay
("""    applied to the fraction; (F2) onset as convention O applied to mean |beta| (the measure used for
    the onset in Figure 8D), each with baselines O1 and O2. Reproduced when, under each reading,
    deep ALM has the earliest onset of all groups and that onset is in the delay epoch (1.2 to 4.2 s
    after trial start).""",
"""    applied to the fraction; (F2) onset as convention O applied to mean |beta| (the measure used for
    the onset in Figure 8D), each with baselines O1 and O2. Reproduced when, under each reading,
    deep ALM has the earliest onset of all groups and that onset is in the delay epoch, no later
    than 2.7 s after trial start (the time of Figure 6D, the first panel the sentence cites for
    "early in the delay epoch")."""),
# fig8d-mm-object-location (a)
("""    bootstrap SD (convention B). Reproduced when (a) every MM group has a maximum of mean |alpha| in
    the sample or early delay (trial start to 2.2 s) larger than the ALM deep IT group's; (b)""",
"""    bootstrap SD (convention B). Reproduced when (a) every MM group has a maximum of mean |alpha| in
    the sample or early delay (trial start to 2.2 s) larger than that of the ALM group of the same
    depth and projection type (the paper contrasts ALM, "little object location selectivity", with
    MM); (b)"""),
("""  source: Results, Projection-Specific Coding, paragraph 3; Figure 8D
  quote: In contrast, MM neurons""",
"""  source: Results, Projection-Specific Coding, paragraph beginning 'ALM neurons displayed prominent
    lick direction selectivity'; Figure 8D; Discussion, paragraph beginning 'Object location
    selectivity was widespread in MM'
  quote: In contrast, MM neurons"""),
# discussion sources
("  source: Discussion, paragraph 4; Figure 8D",
 "  source: Discussion, paragraph beginning 'MM shows little preparatory activity'; Figure 8D"),
("  source: Discussion, paragraph 6; Figure 8D",
 "  source: Discussion, paragraph beginning 'We also observed neurons representing trial outcome';\n    Figure 8D"),
("  source: Discussion, paragraph 5; Figure 1C",
 "  source: Discussion, paragraph beginning 'MM shows little preparatory activity'; Figure 1C"),
("  source: Results, Projection-Specific Coding, paragraph 2; Discussion, paragraph 8",
 "  source: Results, Projection-Specific Coding, sentence beginning 'However, this difference in lick\n    direction selectivity onset'; Discussion, paragraph beginning 'We analyzed neuronal selectivity'"),
("  source: Results, Projection-Specific Coding, paragraph 1; Figures 8D and S10 (not read)",
 "  source: Results, Projection-Specific Coding, sentence beginning 'In ALM, the strongest lick\n    direction selectivity'; Figures 8D and S10 (not read)"),
# fig8d-error readings
("""  criterion: Among neurons purely outcome selective at any bin from the go cue to 2.5 s after it,
    those whose gamma at their most significant bin is negative (error preferring) against
    positive. Reproduced when error-preferring neurons are more numerous, by a two-sided binomial
    test at p < 0.05 (test fixed here); the mean signed gamma per bin, which Figure 8D shows, is
    reported as well.""",
"""  criterion: The paper cites Figure 8D, which shows mean signed gamma (non-significant set to 0),
    and gives no count or test. Readings (a) among neurons purely outcome selective at any bin from
    the go cue to 2.5 s after it, those whose gamma at their most significant bin is negative (error
    preferring) against positive, error preferring more numerous by a two-sided binomial test at p <
    0.05 (test fixed here); (b) mean signed gamma over all neurons, averaged over the same window,
    below zero by more than 2 bootstrap SD (convention B; bound fixed here). Reproduced when both
    readings find error preference."""),
# fig8ef
("""    Reproduced when total variance explained by area and by depth each exceed that by projection
    type, and area is the largest of the three; partially reproduced when area and depth together
    exceed projection type but area is not the largest. Bootstrap SD as convention B.""",
"""    Reproduced when total variance explained by area is the largest of the three (the Summary,
    "Cortical area was more predictive of neuronal selectivity than laminar location or axonal
    projection target") and area and depth together exceed projection type; partially reproduced
    when area and depth together exceed projection type but area is not the largest. Depth against
    projection type alone is reported. Bootstrap SD as convention B."""),
# ephys readings
("""    intermediate units are included is open; readings all 567, and the 486 putative pyramidal
    units.""",
"""    intermediate units are included is open; readings all 567; the 558 left when the 9
    intermediate units are excluded (Methods, "Units with intermediate values ... were excluded");
    and the 486 putative pyramidal units."""),
]
for a,b in reps:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)
open(f,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
f='10.1016-j.neuron.2017.05.005.yaml'
s=open(f).read()
a="""    5 mice. The paper's measure is the image itself; this measure is fixed here."""
b="""    5 mice. The paper's measure is the image itself; this measure is fixed here. The rise after the
    response across motor and somatosensory cortex is not judged; the response-epoch map is
    reported."""
assert s.count(a)==1; s=s.replace(a,b)
a="""    and the number of mice are not in the text read; no statistic can be named."""
b="""    and the number of mice are not in the text read; no statistic can be named. The Discussion
    (paragraph beginning 'In previous experiments') attributes the inactivation to Guo et al.
    (2014b); whether Figure S9 shows those data or new ones is not in the text read."""
assert s.count(a)==1; s=s.replace(a,b)
s=s.rstrip('\n')+"""
- id: alm-pt-it-lick-fraction-below-20
  statement: Even in ALM, less than 20% of PT or IT cells displayed lick direction selectivity at any
    given time, and the onset timing was variable.
  source: Discussion, paragraph beginning 'We analyzed neuronal selectivity'; Figures 6, 8 and S10
    (not read)
  quote: even in ALM, less than 20% of PT or IT cells displayed lick direction selectivity at any
    given time (Figures 6, 8, and S10), and the onset timing was variable
  depends_on:
  - fig8c-pt-deep-only
  expected:
    quantity: largest fraction, over time bins, of ALM PT or ALM IT cells lick-direction selective
    value: 20
    tolerance: 2
    unit: percent
  criterion: Per bin, the fraction of ALM PT cells and of ALM IT cells that are lick-direction
    selective (convention M), over the extracted window. Which cells count is open, readings (a)
    purely lick-direction selective (as Figure 6); (b) beta significant, pure or mixed (as the
    coefficients of Figure 8D). The paper's number is a bound; tolerance 10% of it. Reproduced when
    the largest fraction of each group stays below 22% under one reading. The variability of onset
    is not judged.
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig6-object-location-mm, the alternative window ended at 1.5 s, called the time of Figure 6D; the
    Figure 6 labels put 6C at 1.5 s and 6D at 2.7 s, so the window now ends at 2.7 s.
  - fig6-lick-direction-deep-alm-first, the criterion did not test "early in the delay epoch"; onset
    must now be no later than 2.7 s, the time of Figure 6D, the first panel the sentence cites.
  - fig8d-mm-object-location, part (a) compared MM groups with ALM deep IT alone, a choice not in the
    paper; it now compares each MM group with the ALM group of the same depth and type, as the
    paper contrasts ALM with MM. Source now cites the paragraph by its first words and adds the
    Discussion paragraph that says MM PT cells had the strongest object location selectivity.
  - fig8d-mm-posterior-preferring, fig1c-whisking-similar, fig8d-error-outnumber-correct and
    ephys-pt-it-onset-not-detected, the Discussion paragraph numbers were wrong (the posterior
    sentence is at least the fifth paragraph, not the fourth); sources now name each paragraph by its
    first words. fig8d-alm-deep-lick-direction likewise cites its sentence, as the paragraph break is
    not certain from the text.
  - fig8d-error-outnumber-correct, the paper cites Figure 8D, which shows mean signed gamma, while the
    criterion counted neurons only; the mean signed gamma is added as a second reading.
  - fig8ef-area-explains-variance, the criterion required depth alone to exceed projection type,
    which the paper does not say; it now requires area to be the largest (the Summary and
    Highlights) and area and depth together to exceed projection type.
  - ephys-selective-counts, the Methods exclude the 9 intermediate-width units; a reading of 558 units
    is added.
  - widefield-mm-to-alm, the statement includes the rise after the response, which the criterion does
    not test; it is now said to be reported only.
  - figs9-photoinhibition-alm-mm, noted that the Discussion attributes the inactivation to Guo et al.
    (2014b).
  - alm-pt-it-lick-fraction-below-20, added; the Discussion's bound on the fraction of ALM PT and IT
    cells with lick direction selectivity is a reported number with no claim.
  - open, the PDF could not be rendered in this run (no pdftoppm), so paragraph breaks and figure
    panel times were read from the extracted text alone.
  - open, ephys-selective-counts and fig7d-ephys-area-distribution are data elsewhere at CRCNS
    10.6080/K0S180F9 on the reader's reading of the dandiset metadata; the paper lists imaging and
    electrophysiology in one deposit, so the author should check whether the dandiset holds the units.
  - open, many criteria for qualitative claims (fig8d-pt-contra-bias, fig8d-mm-posterior-preferring,
    fig6-outcome-response-uniform, fig1c-whisking-similar, figs5-single-coefficient and others) use
    thresholds and tests fixed by the reader, as each says; the paper gives none.
  - open, the Supplemental Figures S1 to S10 are not in the text, so claims on S1, S4, S5, S7 and S9
    rest on the main text alone.
"""
open(f,'w').write(s)
EOF
cd  && python tools/claims_check.py claims/000015/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -e '—' -e 'rather' claims/000015/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/000015/10.1016-j.neuron.2017.05.005.yaml'));print(len(d['claims']),d['checks'][-1]['ready'])"; git status --short
```

```
32 True
 M claims/000015/10.1016-j.neuron.2017.05.005.yaml
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

I checked `claims/000015/10.1016-j.neuron.2017.05.005.yaml` against the paper, made 10 changes and added one claim, and marked it ready. Nothing is committed.

**Checker result** (run again after my edits): `32 claims, 32 quotes, 1 statistical values, 0 problems`. Before the edits it was 31 claims with 0 problems.

**Changes, by claim** (each is also logged under `checks`):
- **fig6-object-location-mm**: the second window was said to end at "1.5 s, the time of Figure 6D". The figure labels put 6C at 1.5 s and 6D at 2.7 s, so that window now ends at 2.7 s.
- **fig6-lick-direction-deep-alm-first**: the criterion did not test "early in the delay epoch". Onset must now be no later than 2.7 s, the time of Figure 6D, the first panel the sentence cites.
- **fig8d-mm-object-location**: part (a) compared every MM group with ALM deep IT only, which is the earlier writer's choice, not the paper's. Each MM group is now compared with the ALM group of the same depth and type. I also added the Discussion paragraph saying MM PT cells had the strongest object location selectivity to the source.
- **fig8d-mm-posterior-preferring, fig1c-whisking-similar, fig8d-error-outnumber-correct, ephys-pt-it-onset-not-detected**: the Discussion paragraph numbers were wrong. These sources now name each paragraph by its first words. **fig8d-alm-deep-lick-direction** now cites its sentence, because the paragraph break isn't certain.
- **fig8d-error-outnumber-correct**: the paper cites Figure 8D, which shows mean signed γ, but the criterion only counted neurons. Mean signed γ is added as a second reading, and both readings must find more error-preferring neurons.
- **fig8ef-area-explains-variance**: the criterion required depth alone to beat projection type, which the paper doesn't say. It now requires area to be the largest of the three (as the Summary says) and area plus depth together to exceed projection type.
- **ephys-selective-counts**: the Methods exclude the 9 units of intermediate spike width, so a 558-unit reading is added.
- **widefield-mm-to-alm**: the statement includes the rise in activity after the response, which the criterion doesn't test. The criterion now says that rise is reported, not judged.
- **figs9-photoinhibition-alm-mm**: added a note that the Discussion attributes the inactivation experiments to Guo et al. (2014b).
- **New claim, alm-pt-it-lick-fraction-below-20**: the Discussion says fewer than 20% of ALM PT or IT cells were lick-direction selective at any time, and no claim covered that number.

**Still open:**
- I couldn't render the PDF here because pdftoppm isn't installed. Paragraph breaks and the Figure 6 panel times are therefore read from the extracted text only.
- The two silicon-probe claims are marked as data held at CRCNS (10.6080/K0S180F9), based on the earlier writer's reading of the dandiset metadata. The paper lists imaging and probe data as one deposit, so the author should check whether the dandiset holds the probe units.
- Many criteria for qualitative claims use thresholds or tests chosen by the earlier writer, because the paper gives none. Each says so.
- Supplementary Figures S1 to S10 aren't in the text. The claims on S1, S4, S5, S7 and S9 rest on the main text alone.

**Ready:** yes; the new check entry is marked `ready: true`.

## End of run

16 turns, 3 minutes, result: success.
