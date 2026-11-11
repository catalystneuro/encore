# park-2019 · claims-check · run 42851028807

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i park; cat claims/park-2019.yaml; grep -n "Reader" -A40 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i neuron.2018; wc -l claims/park-2019.yaml; python tools/claims_check.py claims/park-2019.yaml paper/10.1016-j.neuron.2018.11.019.txt
```

**Agent calls Read**

```json
{
 "file_path": "claims/park-2019.yaml"
}
```

Result: not kept, because it reads the paper's text.

```
1	# Claims for Park, Keeley, Savin, Ranck & Fenton (2019), Neuron 101:285-293, tested on CRCNS hc-20.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
3	# protocol pilot-14 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (paper/10.1016-j.neuron.2018.11.019.txt, PyMuPDF extraction
6	# of the publisher PDF), main text, figure legends, STAR Methods and the Supplemental
7	# Information (Figures S1 to S6 and Table S1). Video S1 (the rotating arena) holds no result.
8	# The PDF could not be rendered in this run, so figures were read from their legends and the
9	# Results only. Glyphs garbled by the extraction were read as follows: "10�14" is 10^-14, "R" is
10	# "at least", "%" is "at most", "4.17 3 107" is 4.17 x 10^7, "�0.141" is -0.141. The spike width
11	# of head-direction cells is printed "169.79 ± 4.58 ms"; the unit is very likely microseconds.
12	#
13	# Code read: https://github.com/FentonLab/PyCode_MEC_HDC-NeuronMS_Park at commit 545a738 (4 Nov
14	# 2018), linked under Data and Software Availability. It holds two Python 2 scripts that read
15	# the TSD files of the dataset. HD_Max_likelihood.py is the decoder of Figures 2 and 5: windows
16	# of 20 tracker samples (at 30 Hz, 667 ms; the Methods say 660 ms), the window's head direction
17	# the circular mean of its samples (samples with direction > 360 dropped), 36 bins of 10
18	# degrees, a Poisson rate per cell and bin fitted on the training file (spikes in windows at
19	# that bin divided by the number of such windows), the summed Poisson log likelihood maximized
20	# over the bins, windows in which no cell spiked left undecoded. Training is stable1 (the
[... 630 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/10.1016-j.neuron.2018.11.019.txt; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 43,140p docs/protocol.md
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
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 140,220p docs/protocol.md
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
   - A paper that reuses its datasets (`relation: reuses` in
     `papers/datasets/<paper>.yaml`) is read like any other: its claims are
[... 61 more lines not kept]
```

**Agent**

Checker ran: 1 problem (fig1d p 1e-9 not found). Now reading the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.11.019.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== page" paper/10.1016-j.neuron.2018.11.019.txt | sed -n 10,40p; grep -n "STAR+METHODS\|KEY RESOURCES\|Supplemental Information\|Figure S" paper/10.1016-j.neuron.2018.11.019.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.11.019.txt",
 "offset": 789,
 "limit": 605
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o "p = 10.\{1,4\}" paper/10.1016-j.neuron.2018.11.019.txt | od -c | head -20; grep -n "1e-9\|e-\|10\^" tools/claims_check.py | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 55,110p tools/claims_check.py
```

```
if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
[... 34 more lines not kept]
```

**Agent**

The p = 10^-9 is in the legend ("p = 10�9", minus sign garbled), so the checker's one problem is an extraction artifact. Next I'll check the linked code for the Figure 4 window side.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/FentonLab/PyCode_MEC_HDC-NeuronMS_Park pc 2>&1 | tail -2; ls pc 2>/dev/null && cd pc && git log --oneline | head -3
```

```
HD_Max_likelihood.py
README.md
Spike_triggered_FR_curve.py
545a738 Initial commit
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/pc && cat Spike_triggered_FR_curve.py | head -200; wc -l *.py
```

```
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:27:09 2015

@author: stephenkeeley
"""

import struct as st
import numpy as np
import random as rd
import os as os
import scipy.io as sio
rd.seed()



    
    

def doheader(fh,nlines):
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pc && grep -n "20\|window\|bin" HD_Max_likelihood.py | head -40
```

```
46:num_samps = 20 #this is variable. is the resolution, in bins, of the estimator.
55:estimation_window = 200 #ms
61:total_bins = np.zeros([num_cells,36])
89:        nlinbin = f.read(2)
90:        nlin = int(nlinbin)
100:        binxys = f.read(7)
101:        while binxys != "":
106:                if len(binxys) != 7:
108:                x,y,d,s = st.unpack('=BBIB', binxys)
119:                #generate total number of spikes in the estimator window from cell i
122:                bintimes = f.read(s*4) #read the remaining info
123:                binxys = f.read(7)    
131:            bin_ang_ind = np.floor(36*ang/(2*np.pi)) #convert angle to index
134:            tuning_probs[i][bin_ang_ind][s_tot] = tuning_probs[i][bin_ang_ind][s_tot] + 1 #assemble the spikes in the correct angle indices. Do this for each numsamp chunk of time
136:            total_bins[i][bin_ang_ind] = total_bins[i][bin_ang_ind]+s_tot*1 #find the total amount of time spent at each angle, too
161:lamdas =  [i/summed_tunes for i in total_bins]
195:    nlinbin = fs[i].read(2)
197:    nlin = int(nlinbin)
208:            binxys = fs[j].read(7)
209:            if len(binxys) != 7:
[... 4 more lines not kept]
```

**Agent**

Code confirms the Figure 4 window ends at the cell 1 spike, so cell 2 spikes come before it. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    successive 30 Hz samples; (b) displacement over 1 s steps. Readings of the unit are (a)\n    recording session; (b) cell (n = 115). Repeated-measures ANOVA with Greenhouse-Geisser",
 "new_string": "    successive 30 Hz samples; (b) displacement over 1 s steps. The unit is read as the\n    recording session; the cell (n = 115) is ruled out, as it would give a denominator near\n    230 degrees of freedom. Repeated-measures ANOVA with Greenhouse-Geisser"
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    condition, then Tukey-Kramer HSD. Reproduced when the effect has p < 0.05, stable1 and\n    stable2 do not differ, and stable2 > room > arena with each of these pairs significant at\n    p < 0.01;",
 "new_string": "    condition, then Tukey-Kramer HSD. Reproduced when the effect has p < 0.05, stable1 and\n    stable2 do not differ, each stable trial > room and room > arena, each of these pairs\n    significant at p < 0.01;"
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    reading and 133 ms a variant. The paper gives no summary measure; the median absolute\n    error per ensemble and condition is used, a standard choice. Reproduced when there are\n    seven ensembles of at least five simultaneously recorded head-direction cells (no\n    tolerance, as this is a count of recordings) and in at least four of them the stable2 error\n    is below both rotating-frame errors; the ensemble with poor stable2 decoding (ensemble b) is\n    expected as an exception.",
 "new_string": "    reading and 133 ms a variant. The paper gives no summary measure (Figure 2 shows error\n    histograms); the readings are (a) the median absolute circular error per ensemble and\n    condition, (b) the mean absolute circular error. The paper names no count of ensembles for\n    \"relatively accurate\" and \"relatively inaccurate\"; a majority (at least four of seven) is\n    an assumption. Reproduced when there are seven ensembles of at least five simultaneously\n    recorded head-direction cells (no tolerance, as this is a count of recordings), the stable2\n    error is below the arena-frame error in at least four ensembles, and below the room-frame\n    error in at least four (the paper allows some ensembles with room-frame decoding similar\n    to stable2, and one ensemble, b, with poor stable2 decoding)."
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    Results and Figure 4B, (b) 30 s, the code's window. The window side, (a) cell 2 spikes\n    after the cell 1 spike, as the Methods read, (b) before it, as the code has it. The\n    normalization, (a) the Methods' division by the sum of the time offsets, (b) the code's\n    division by the occupancy of each displacement. The degrees of freedom imply about 130\n    to 137 pairs, so some pairs were dropped for a reason the paper does not give; the pairs\n    used are those with a defined curve in every trial. Reproduced when all four tests have\n    p ≥ 0.05 under the main readings (5 s, Methods side and normalization); the variants are\n    shown.",
 "new_string": "    Results and Figure 4B, (b) 30 s, the code's window. The window side is not fixed by the\n    Methods or Results (\"within a maximal interval\"); the code settles it, cell 2 spikes before\n    the cell 1 spike (Spike_triggered_FR_curve.py, window from the cell 1 spike time less\n    move_ts samples to that time), which is the main reading, with cell 2 spikes after the cell 1\n    spike as a variant. The normalization, (a) the Methods' division by the sum of the time\n    offsets, (b) the code's division by the occupancy of each displacement. The degrees of\n    freedom imply about 130 to 137 pairs, so some pairs were dropped for a reason the paper\n    does not give; the pairs used are those with a defined curve in every trial. Reproduced\n    when all four tests have p ≥ 0.05 under the main readings (5 s, the code's side, the\n    Methods' normalization); the variants are shown."
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    statistic: F(3, 564) ≤ 1.59",
 "new_string": "    statistic: F(3, 564) ≤ 1.59 (printed with the glyph for ≥, read as ≤ since p > 0.19 at\n      each interval)"
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "    statistic: F(3, 564) ≥ 23.73",
 "new_string": "    statistic: F(3, 564) ≥ 23.73 (printed with the glyph for ≤, read as ≥ since p < 10^-14 at\n      each interval)"
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/park-2019.yaml",
 "old_string": "  statement: The room-frame decoding error has strong minima at 110 and 350 degrees in the room\n    frame, the directions of the leading edges of prominent orienting cues, and not in the arena\n    frame.",
 "new_string": "  statement: The room-frame decoding error histogram has strong minima at 110 and 350 degrees in\n    the room frame, the directions of the leading edges of prominent orienting cues given the\n    clockwise rotation; the minima correspond to the cue edges in the room frame but not in the\n    arena frame."
}
```

```
The file claims/park-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat >> claims/park-2019.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1c-speed, dropped the reading with the cell (n = 115) as unit, since F(2.02, 74.68) implies about 38 units and 115 cells would give near 230 denominator degrees of freedom.
  - fig1c-directionality, the criterion now requires each stable trial above the room frame, as the legend's order stable1 = stable2 > rotating-room frame states, not stable2 alone.
  - fig2-decoding-stable-vs-rotating, the error measure is now named open with two readings (median and mean absolute circular error), the four-of-seven threshold is marked as an assumption, and the test against the room frame is separate from the arena frame, since the paper says room-frame decoding was similar to stable2 for some ensembles.
  - fig4-internal-tuning-preserved, the Methods and Results do not say that cell 2 spikes follow the cell 1 spike; the linked code (Spike_triggered_FR_curve.py, commit 545a738, read in this check) takes cell 2 spikes in the window ending at the cell 1 spike, so the code's side is now the main reading (protocol step 2, code settles what the Methods leave open) and the other side a variant.
  - fig4c-arena-registration-short-lived, the two one-way ANOVA statistics now say that the legend prints them with the opposite inequality glyphs (F ≥ 1.59 with p > 0.19, F ≤ 23.73 with p < 10^-14), read as a misprint.
  - fig5c-error-minima-at-cues, statement reworded to follow Figure 5C and 5D, the minima of the room-frame error histogram correspond to cue edges in the room frame and not the arena frame, in place of saying the minima are absent in the arena frame.
  - Not changed, fig1d-preference-change p = 1e-9 is reported by the checker as not found; the legend prints "p = 10�9" with the minus sign lost in extraction, the same glyph as the other exponents, so the value stands.
  - Open, figs2-frame-preference, the margin for no frame preference (factor of 2, or both probabilities below 0.05) is not from the paper, which says only "clear" preference; the readings stand as named assumptions.
  - Open, fig2c-proximity-anticorrelation, the paper gives two averages for Idir against proximity (-0.141 ± 0.029 and -0.132 ± 0.024) without saying how they differ; the criterion accepts either.
  - Open, fig4c-arena-registration-short-lived, "strength" of internally referenced tuning is not defined; the Rayleigh vector length is the only reading given.
  - Open, figs5 and figs6, the pfgp code was not read in this check; lattice resolution and time bin are left to it.
EOF
python tools/claims_check.py claims/park-2019.yaml paper/10.1016-j.neuron.2018.11.019.txt; grep -n " — \|rather" claims/park-2019.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/park-2019.yaml | grep -n ": " | grep -v "^\S*:- date\|  [a-z]*: " ; python -c "import yaml;d=yaml.safe_load(open('claims/park-2019.yaml'));print(len(d['checks'][0]['changes']))"; git status --short
```

```
11
 M claims/park-2019.yaml
 M tools/entry.py
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

I checked the claims file for park-2019. I made six corrections, and it is ready for an attempt (`ready: true`).

**Checker result:** `claims/park-2019.yaml: 22 claims, 22 quotes, 32 statistical values, 1 problems`. The one problem is p = 1e-9 in fig1d-preference-change. The Figure 1D legend prints it as "p = 10�9": the minus sign was lost when the text was extracted from the PDF, the same garbling as the other exponents in the file. The value is the paper's, so I left it.

**Changes, by claim:**
- **fig1c-speed:** I removed the reading that uses each cell (n = 115) as the unit. The degrees of freedom, F(2.02, 74.68), imply about 38 units; 115 cells would give a denominator near 230.
- **fig1c-directionality:** the criterion now requires both stable trials to be above the room frame, as the legend's order "stable1 = stable2 > rotating-room frame" says. Before, it required only stable2.
- **fig2-decoding-stable-vs-rotating:**
  - The paper gives no summary measure of decoding error, so it is now named as open, with two readings: median or mean absolute circular error.
  - The "at least four of seven ensembles" threshold is now marked as an assumption.
  - Stable2 is now compared with the room frame and the arena frame separately, since the paper says room-frame decoding was similar to stable2 in some ensembles.
- **fig4-internal-tuning-preserved:** the file said the Methods put the second cell's spikes after the reference spike. They don't specify a side. I read the linked code (Spike_triggered_FR_curve.py, commit 545a738), which takes the second cell's spikes before the reference spike. Under protocol step 2 (code settles what the Methods leave open), the code's side is now the main reading and the other side a variant.
- **fig4c-arena-registration-short-lived:** the legend prints the two one-way ANOVA bounds with the inequality signs reversed ("F ≥ 1.59, p > 0.19" and "F ≤ 23.73, p < 10^-14"). The file had silently swapped them; the statistic strings now say they are read as a misprint.
- **fig5c-error-minima-at-cues:** I reworded the statement to follow the Figure 5C and 5D legend. The minima match the cue edges in the room frame but not the arena frame; the old wording read as if the minima were absent in the arena frame.

**Still open (recorded in `checks`):**
- **figs2-frame-preference:** the cut-off for "no frame preference" is not in the paper, which says only "clear" preference. The file's two readings (a factor of 2, or both probabilities below 0.05) remain assumptions.
- **fig2c-proximity-anticorrelation:** the paper gives two averages for the same correlation (−0.141 ± 0.029 and −0.132 ± 0.024) without saying how they differ. The criterion accepts either.
- **fig4c-arena-registration-short-lived:** the paper does not define "strength" of the internally referenced tuning. The only reading given is the Rayleigh vector length.
- **figs5 and figs6:** I did not read the Gaussian process model code (pfgp), so the lattice resolution and time bin are still left to it.

Every main finding has a claim, and every claim comes from this paper. I did not commit anything, and I left the existing change to `tools/entry.py` alone.

## End of run

24 turns, 3 minutes, $1.12 at API prices, result: success.
