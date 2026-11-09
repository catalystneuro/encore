# 000138 · claims-check · run 40755699574

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/000138/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,200p docs/protocol.md; python tools/claims_check.py claims/000138/*.yaml paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/000138/*.yaml
```

```
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000138.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md.
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102, NIHMS240235), main text,
# Methods and figure legends, with its one supplement file (NIHMS240235-supplement-01.pdf:
# Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). This is
# the accepted manuscript, not the copyedited version of record. The main-text PDF was not
# available, so Figure 6A-D, the range of dimensionalities plotted there and the per-dataset
# values in Figures 6 and 7 could not be read. The paper links no analysis code, so no code was
# read.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J) made delayed reaches on a fronto-parallel
# screen. Speed task (monkeys A, B): 7 directions, 2 distances, 2 instructed speeds, 28 conditions.
# Maze task (monkey J): straight reaches, or reaches curving around virtual barriers, with or
# without distractor targets, 108 conditions in all. Four datasets: A (64 single units), B (74), J
# (172 single units by single electrode, in four sets of 27 conditions, about 53 neurons each,
# analysed per set and then averaged), and J-array (two 96-electrode arrays, one in caudal PMd and
# one in surface M1, 146 single- and multi-unit isolations, all 108 conditions interleaved). Mean
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/10.1016-j.neuron.2010.09.015.txt; fold -s -w 200 paper/10.1016-j.neuron.2010.09.015.txt | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/17c2b837-3ed6-4956-9e58-709ec210dfa4/tool-results/bnvv8kr3m.txt"
}
```

```
1	103707 paper/10.1016-j.neuron.2010.09.015.txt
2	DOI: 10.1016/j.neuron.2010.09.015
3	Version: as served by ncbi_pmc
4	Source: ncbi_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC2991102), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
7	------------------------------------------------------------------------
8	Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 
9	10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman 
10	MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of 
11	Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, 
12	USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under 
13	the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement 
14	activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that 
15	it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, prep
[... 302 more lines not kept]
```

**Agent**

Main text read. Now the supplement section of the text.

**Agent calls Bash**

```bash
cd  grep -n -i "supplement" paper/10.1016-j.neuron.2010.09.015.txt | head; awk 'NR>=1' paper/10.1016-j.neuron.2010.09.015.txt | grep -n "Supplemental Experimental Procedures" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)}' paper/10.1016-j.neuron.2010.09.015.txt | sort -t: -k2 -n -r | head; grep -n "Supplemental Experimental\|SUPPLEMENT\|Supplemental Text" paper/10.1016-j.neuron.2010.09.015.txt | cut -c1-150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 8,900p paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/17c2b837-3ed6-4956-9e58-709ec210dfa4/tool-results/bcavlshsk.txt",
 "offset": 90
}
```

```
90	[44] Dissociation between hand motion and population vectors from neural activity in motor cortex. Nature. 2001. 10.1038/35093102
91	
92	[45] Motor cortex neural correlates of output kinematics and kinetics during isometric-force and arm-reaching tasks. J. Neurophysiol.. 2005. 10.1152/jn.00989.2004
93	
94	[46] Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. J. Neurophysiol.. 2001. 10.1152/jn.2001.86.4.1916
95	
96	[47] Preferential representation of instructed target location versus limb trajectory in dorsal premotor area. J. Neurophysiol.. 1997. 10.1152/jn.1997.77.3.1195
97	
98	[48] Generating coherent patterns of activity from chaotic neural networks. Neuron. 2009. 10.1016/j.neuron.2009.07.018
99	
100	[49] Anticipatory activity of motor cortex neurons in relation to direction of an intended movement. J. Neurophysiol.. 1976. 10.1152/jn.1976.39.5.1062
101	
102	[50] Direct cortical control of muscle activation in voluntary arm movements: A model. Nat. Neurosci.. 2000. 10.1038/73964
103	
104	[51] Turner, R.S. (1991). Movement- and instruction-related activity in the globus pallidus of the monkey. PhD thesis, University of Washington, Seattle, Washington.
105	
106	[52] A neurophysiological study of the premotor cortex in the rhesus monkey. Brain. 1984. 10.1093/brain/107.2.385
107	
108	[53] Movement-related activity in the premotor cortex of rhesus macaques. Prog. Brain Res.. 1986. 10.1016/S0079-6123(08)63407-X
109	
[... 585 more lines not kept]
```

**Agent**

I've read the paper and supplement. Checking protocol terms the file uses (`partially`, `with_inputs`, check format).

**Agent calls Bash**

```bash
cd  grep -n -i "partial\|with_inputs\|with_labels\|checks:\|ready" docs/*.md | head -40; ls claims | head; grep -l "checks:" claims/*/*.yaml | head -3
```

```
docs/design.md:20:   hypothesis on a dandiset starts from notebooks that already load the data
docs/design.md:61:  - `partially_reproduced`: the effect is present but weaker, or holds only
docs/design.md:70:  separately as the outcome's deviations, so that "partially reproduced" always
docs/encore.md:31:The run and its report go to `./encore-<name>-<date>/`, or `--out`. `report.md` there lists every claim with its outcome (reproduced, partially reproduced, not reproduced, or blocked) and every finding about the data, and points to the notebooks the author wrote. A failure to reproduce may be the agent's, not the paper's or the data's: read the notes and the notebooks before acting on one.
docs/pilot-notes.md:37:  into a partial one.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:126:  seven reproduced, one partially, two not reproduced and ten blocked.
docs/pilot-notes.md:130:  published summary values where there is no identifier; a partial link
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pilot-notes.md:352:method until one reproduced. The second is already covered by running every
docs/pipeline.md:48:`primary` (the dataset is the paper's data), `partial` (it holds part of it),
docs/pipeline.md:62:the first `partial` one. A dataset left with no usable paper is held: the chain
docs/pipeline.md:88:When the claims check says the file is ready, the runner commits the claims
docs/pipeline.md:94:drops the claims change `main` already has. A deprecated attempt is not held
docs/protocol.md:143:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:166:the end of the file. A claims file is ready for an attempt when its
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 215,262p docs/protocol.md; grep -n -A12 "^checks:" claims/000005/10.1038-nn.4412.yaml | head -30
```

```
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
     claims are the registry's checks, not findings of the paper, so the
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn -i -B2 -A2 "simulat" claims/*/*.yaml | grep -i "data:" | sort | uniq -c | head; grep -rn "^  data:" claims/ | awk '{print $NF}' | sort | uniq -c
```

```
1 claims/000289/10.1073-pnas.2210622120.yaml-244-  data: elsewhere
      1 claims/000631/10.3390-ijms241310921.yaml-56-# All claims use the paper's own recordings (data: dataset). The paper uses no outside data; the
      1 claims/000633/10.3390-ijms241310921.yaml-182-  data: with_inputs
      1 claims/000715/10.1016-j.cell.2020.12.012.yaml-295-  data: with_inputs
      1 claims/000939/10.1038-s41593-024-01588-5.yaml-487-  data: elsewhere
      1 claims/000947/10.1371-journal.pbio.3000829.yaml-507-  data: elsewhere
      1 claims/000987/10.1016-j.cub.2024.05.048.yaml-586-  data: elsewhere
      1 claims/001047/10.1016-j.bioelechem.2025.109016.yaml:63:# (F9) Fields from the paper's simulation, not from the data: a 7.2-kV first pulse gives 3.3 kV/cm at
      1 claims/001250/10.1101-2024.12.04.626805.yaml-130-  data: with_inputs
      1 claims/001250/10.1101-2024.12.04.626805.yaml-205-  data: with_inputs
    171 dataset
    646 elsewhere
    276 with_inputs
    230 with_labels
```

**Agent**

The file is mostly sound. Making targeted fixes.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/000138/10.1016-j.neuron.2010.09.015.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
rep("""    correlation averaged over neurons. The paper fixes no number for "near zero", so it is fixed
    here, from the dataset means of Figure 4 (0.06 to 0.21). Reproduced when the mean
    correlation at movement onset is below 0.1 in absolute value and below half of its value
    250 ms before movement onset, and the curve has not fallen by more than a quarter of its
    early value before 300 ms before movement onset.""",
"""    correlation averaged over neurons. The paper gives no numbers for "began to decline" or
    "near zero", so these thresholds are fixed here, not taken from the paper. Near zero is set
    from the dataset means of Figure 4 (0.06 to 0.21). Reproduced when the mean correlation at
    movement onset is below 0.1 in absolute value and below half of its value 250 ms before
    movement onset, and the mean correlation 300 ms before movement onset is at least three
    quarters of its value 400 ms before movement onset (no marked decline before about 200 ms).""")
rep("""regressed on each neuron's AP location by least squares, with the p-value of the slope (that
    of r). Reproduced for a dataset when p is 0.05 or above""",
"""regressed on each neuron's AP location by least squares, with the p-value of the slope (that
    of r). The paper names no significance threshold; 0.05 is the conventional level and is an
    assumption. Reproduced for a dataset when p is 0.05 or above""")
rep("""    recorded (not J-array), and each task space defined for the task. Reproduced when the""",
"""    recorded (not J-array), and each task space defined for the task. The upper-limit space built
    from preparatory activity (gray line of Figure 6A-D, Supplemental Experimental Procedures) and
    the shuffled control space of Figure 7A are not competitors. Reproduced when the""")
rep("""    "considerably better than chance". Reproduced when the mean performance is above zero for
    the peri-movement and kinematic spaces at their best k and for more than half of the task
    spaces.""",
"""    "considerably better than chance". "Generally" is not quantified; the share is fixed here.
    Reproduced when the mean performance is above zero for the peri-movement and kinematic spaces
    at their best k and for more than half of the task spaces.""")
rep("""    the peri-movement space; other spaces are significantly worse than the best (p < 0.001).""",
"""    the peri-movement space; spaces marked with asterisks are significantly worse than the best
    (p < 0.001).""")
rep("""lead over the next space grows from 3 to 12, and the kinematic and EMG spaces at the 12
    limit exceed every task space.""",
"""lead over the next space grows from 3 to 12, and the kinematic and EMG spaces at the 12
    limit each exceed more than half of the task spaces (the paper says "largely outcompeted";
    the share is fixed here). Which spaces carry asterisks could not be read, since the main-text
    figure was not available.""")
rep("""    space is then built as for the peri-movement space. The draw is repeated""",
"""    space is then built as for the peri-movement space. Figure 7A averages over all datasets;
    here each dataset is judged on its own. The draw is repeated""")
rep("""  criterion: Per dataset, mean performance of the peri-movement space at its best k (Figure 7B
    legend) with the window starting at movement onset, divided by that with the window starting
    150 ms before.""",
"""  criterion: Per dataset, mean performance of the peri-movement space with the window starting
    at movement onset, divided by that with the window starting 150 ms before, each at the best k
    for that start time (Figure 7B legend).""")
rep("""    Experimental Procedures) for that subset. Open whether that upper limit is taken at k = 6 or
    at its best k; both are run. Reproduced when the normalized performances of the anterior and
    posterior subsets are each above zero and within 10% of that of the random halves;""",
"""    Experimental Procedures) for that subset. Open whether that upper limit is taken at k = 6 or
    at its best k; both are run. "Only slightly different" is not quantified; the 10% bound is
    fixed here. Reproduced when the normalized performances of the anterior and posterior subsets
    are each above zero and within 10% of that of the random halves;""")
s=s.rstrip("\n")+"""
checks:
- date: 2026-10-28
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4e-correlation-time-course. The criterion compared the curve with an undefined "early value"; it now uses the value 400 ms before movement onset as reference, and says that all its thresholds are fixed here since the paper gives none.
  - results-ap-location-no-effect. Said that the 0.05 threshold is an assumption; the paper reports r and p but names no threshold.
  - fig6-peri-movement-space-best. Excluded the upper-limit space (gray line, built from preparatory activity) and the shuffled control space from the competing spaces, since the paper treats them as a bound and a control.
  - fig6-pd-adequate-all-spaces. Said that the "more than half of the task spaces" share is fixed here; the paper says only "generally".
  - fig6e-summary-rank. The statement said all other spaces are significantly worse than the best; the Figure 6E legend says only that spaces marked with asterisks are. Corrected.
  - fig6e-summary-rank. The criterion required the kinematic and EMG spaces to beat every task space; the paper says the task spaces were "largely outcompeted". Changed to more than half, marked as fixed here.
  - fig7a-shuffled-space-poor. Noted that Figure 7A averages over all datasets while the criterion judges each dataset.
  - fig7b-window-start-onset. The Figure 7B legend uses the best dimensionality for each dataset and start time; the criterion now takes the best k separately for each window start.
  - fig7c-anterior-posterior. Said that the 10% bound for "only slightly different" is fixed here.
  - Open. The main-text PDF is not available, so the Figure 6 and 7 per-dataset values, the k range plotted, and the spaces marked in Figure 6E could not be read.
  - Open. fig8-oscillator-model is a simulation that uses no recorded data; it is marked with_inputs, which keeps it apart from the dataset's count, though no outside input is involved.
"""
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/000138/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file and it is ready for an attempt. I made nine corrections and left two points open.

**Checker result:** `claims/000138/10.1016-j.neuron.2010.09.015.yaml: 15 claims, 15 quotes, 9 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim**
- **fig4e-correlation-time-course:** The criterion compared the curve against an "early value" it never defined. The reference is now the value 400 ms before movement onset, and the criterion says all its thresholds are set here, since the paper gives no numbers for "began to decline" or "near zero".
- **results-ap-location-no-effect:** The paper reports r and p but names no significance threshold, so the criterion now says p = 0.05 is an assumption.
- **fig6-peri-movement-space-best:** The upper-limit space (the gray line in Figure 6A-D) and the shuffled space of Figure 7A are no longer counted as competing spaces. The paper treats one as a bound and the other as a control.
- **fig6-pd-adequate-all-spaces:** The paper says only "generally", so the criterion now says its "more than half of task spaces" share is set here.
- **fig6e-summary-rank:**
  - The statement said all other spaces are significantly worse than the best. The legend says only that the spaces marked with asterisks are; corrected.
  - The criterion required the kinematic and EMG spaces to beat every task space, but the paper says "largely outcompeted". It now requires more than half, marked as set here.
- **fig7a-shuffled-space-poor:** Added that Figure 7A averages over all datasets, while the criterion judges each dataset on its own.
- **fig7b-window-start-onset:** Following the Figure 7B legend, the best dimensionality is now taken separately for each window start time.
- **fig7c-anterior-posterior:** The 10% bound for "only slightly different" is now marked as set here.

I found no problems in the other claims. The paper's main findings are all covered, and every claim comes from this paper.

**Still open**
- The main-text PDF isn't available, so the per-dataset values in Figures 6 and 7, the range of dimensionalities plotted, and which spaces carry asterisks in Figure 6E couldn't be read.
- **fig8-oscillator-model** is a simulation that uses no recorded data. It is marked `with_inputs`, which keeps it out of the dataset's count, even though no outside input is involved. Other claims files mark simulations both this way and as `elsewhere`, so I left it as is.

The `checks` entry with these changes is at the end of the file. Nothing was committed or pushed.

## End of run

14 turns, 2 minutes, result: success.
