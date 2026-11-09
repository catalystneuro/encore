# crcns-pfc-1 · claims · run 42223923091

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-pfc-1/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -40 paper/10.1016-j.neuron.2014.04.031.txt; cat tools/claims_check.py | head -60; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.04.031.txt",
 "offset": 40,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.04.031.txt",
 "offset": 740,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.04.031.txt",
 "offset": 1640,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2014.04.031.txt",
 "offset": 2440,
 "limit": 730
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/pfc-1.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/cxrodgers/Rodgers2014 && cd Rodgers2014 && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | sort
```

```
390b6089c429877dfea9c56de153bbea0380c20f Sat Jul 9 20:17:44 2016 -0400
./.gitignore
./2-1-behavres/main00.py
./2-1-behavres/main02.py
./2-1-behavres/main03.py
./2-1-behavres/main04.py
./2-1-behavres/main05.py
./2-1-behavres/perf.py
./3-1-hold/main0.py
./3-1-hold/main1.py
./3-1-hold/main2.py
./3-1-hold/main3.py
./3-1-hold/main6.py
./3-2-errhold/main1.py
./3-2-errhold/main2.py
./3-2-errhold/main3.py
./3-3-vs_spont/main2.py
./3-3-vs_spont/main3.py
./3-4-RT_vs_hold/main.py
./3-4-RT_vs_hold/main3.py
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat README.md metadata/figures_generated_by_each_script.csv && wc -l */*.py | sort -n | tail -70 && head -5 metadata/unit_db.csv && head -3 metadata/sessions_df.csv
```

```
Rodgers2014
===========

This repository contains all of the code necessary to recapitulate the analyses presented in Rodgers and DeWeese (2014), Neuron.


Format
------
This repository consists of:

* Numbered subdirectories. Each one contains a series of scripts of the form main1.py, main2.py, ..., relating to a specific type of analysis. (For instance, subdirectory 2-1-behavres contains all the scripts for analyzing the behavioral results.)
* A subdirectory called 'modules'. This contains copies of my other github repositories that you need to run the code. I copied the modules to make it easier to install, and also because I removed some (but not all) of the code from the modules that is not related to the analyses presented here.

The 'modules' directory needs to be on your PYTHONPATH so that the scripts can import the modules it contains. For instance, you should be able to 'import ns5_process' and get the module in modules/ns5_process.

The scripts should be run in order: from lowest to highest numbered subdirectory, and within each subdirectory from lowest to highest numbered script. This is because some scripts depend on the output of previous scripts.


Data
----
[... 186 more lines not kept]
```

**Agent**

Full text and supplement are present, and the paper's code (github.com/cxrodgers/Rodgers2014, commit 390b608) is cloned. Next I'm reading the key analysis scripts.

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 3-1-hold/main0.py 3-1-hold/main1.py 3-1-hold/main3.py
```

```
# Dump spike counts from hold period


import numpy as np, os.path
import pandas, itertools
import kkpandas, kkpandas.kkrs
from ns5_process import myutils, LBPB
import my, my.dataload

# Hooks to data
gets = my.dataload.getstarted()
unit_db = gets['unit_db']

# How long the hold should be, and how long to count over
ratname2hold_time = {'CR12B': 50, 'CR17B': 50, 'YT6A': 50,
    'CR24A': 250, 'CR20B': 250, 'CR21A': 250}

# Which units to analyze
units_to_analyze = unit_db[unit_db.include].index

[... 411 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 2-1-behavres/main00.py 2-1-behavres/main02.py 2-1-behavres/perf.py; grep -n "def is_auditory" -A30 modules/kkpandas/kkrs.py
```

```
# Collate all behavioral data from included sessions

import numpy as np
from my.dataload import session2rs, session2kk_server
import kkpandas
from ns5_process import LBPB, myutils
import my
from perf import perfcount, perfratio


def session2ratname(session):
    return session.split('_')[0]

gets = my.dataload.getstarted()
session_db = gets['session_db']
session_db['ratname'] = map(session2ratname, session_db.index)

# Return variable
trials_info_dd = dict([(ratname, {}) for ratname in session_db.ratname.unique()])

[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014/modules && grep -n "random hits by block" -B3 -A25 my/dataload.py | head -80; grep -n "def r_utest" -A40 my/stats.py; grep -n "def r_adj_pval" -A20 my/stats.py; grep -n "def getstarted" -A40 my/dataload.py | grep -n -i "include\|unit_db\|session"
```

```
90-        #~ labels = ['-'.join(t) for t in label_kwargs]
91-        trial_picker_kwargs = {'labels': labels, 'label_kwargs': label_kwargs,
92-            'nonrandom' : 0}
93:    elif trial_picker_kwargs == 'random hits by block':
94-        trial_picker_kwargs = {
95-            'labels': ['LB', 'PB'],
96-            'label_kwargs': [{'block': 2} , {'block': 4}],
97-            'nonrandom' : 0,
98-            'outcome' : 'hit'
99-            }
100-
101-    # How to fold the window around each trial
102-    if folding_kwargs is None:
103-        folding_kwargs = {'dstart': -.25, 'dstop': .3}    
104-
105-
106-    # Load data
107-    gets = getstarted()
108-    
109-    
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && python3 -c "
import csv,collections
r=list(csv.DictReader(open('metadata/unit_db.csv')))
inc=[x for x in r if x['include']=='True']
print(len(r),len(inc),collections.Counter(x['region'] for x in inc))
print(collections.Counter((x['region'],x['audresp']) for x in inc))
print(collections.Counter((x['ratname'],x['region']) for x in inc))
s=list(csv.DictReader(open('metadata/sessions_df.csv')));print(len(s),sum(x['include']=='True' for x in s))
"; grep -n "def load_trials_info" -A30 modules/kkpandas/io.py | head -45
```

```
401 220 Counter({'PFC': 121, 'A1': 99})
Counter({('PFC', 'nothing'): 60, ('A1', 'nothing'): 31, ('PFC', 'weak'): 30, ('PFC', 'too brief'): 26, ('A1', 'weak'): 24, ('A1', 'good'): 19, ('A1', 'too brief'): 11, ('A1', 'sustained'): 6, ('A1', 'lasts to end'): 5, ('A1', 'lasts too long'): 3, ('PFC', 'lasts to end'): 2, ('PFC', 'lasts too long'): 2, ('PFC', 'good'): 1})
Counter({('CR24A', 'PFC'): 65, ('CR12B', 'A1'): 60, ('CR20B', 'PFC'): 40, ('CR17B', 'A1'): 18, ('CR20B', 'A1'): 12, ('YT6A', 'PFC'): 9, ('CR21A', 'PFC'): 7, ('CR21A', 'A1'): 5, ('CR24A', 'A1'): 4})
55 55
32:def load_trials_info(basename, join_on_trial_timings=True, drop_munged=True,
33-    join_on_trial_numbers=False):
34-    """Load the trials info matrix. 
35-    
36-    Loads a matrix of info about each trial (outcome, stimulus, etc) from
37-    the specified directory. The index is the behavioral trial number.
38-    
39-    join_on_trial_timings : if True, then also load the information from
40-        the same directory about the timing of certain events in each trial.
41-        This will drop any trials that didn't actually occur (because they
42-        were before or after the neural data collection) 
43-    drop_munged : drop trials that are marked as munged in trial_timings
44-        No effect if join_on_trials_info is False
45-    join_on_trial_numbers : this is really just for compatibility reasons
46-        No effect if join_on_trial_timings is True and trial_timings exists
47-        But if trial_timings does not exist, this will still allow you to
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 3-2-errhold/main1.py 3-2-errhold/main2.py 3-3-vs_spont/main2.py 3-3-vs_spont/main3.py
```

```
# Dump counts in hold period, now including error trials

import numpy as np, os.path
import pandas, itertools
import kkpandas, kkpandas.kkrs
from ns5_process import myutils, LBPB
import my, my.dataload

# Hooks to data
gets = my.dataload.getstarted()
unit_db = gets['unit_db']

# How long the hold should be, and how long to count over
ratname2hold_time = {'CR12B': 50, 'CR17B': 50, 'YT6A': 50,
    'CR24A': 250, 'CR20B': 250, 'CR21A': 250}

# Which units to analyze
units_to_analyze = unit_db[unit_db.include].index

# Iterate over units
[... 385 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 5-1-timecourse/main1.py 5-1-timecourse/main2b.py; sed -n 1,253p 5-1-timecourse/shared.py | grep -v "^\s*$" | head -150
```

```
# Dump foldeds locked to:
#   cpoke_start
#   stim_onset
#   cpoke_stop
#   choice_made
# Also gets distributions locked to lots of events in the trials
# Slices trials based on a variety of criteria, eg after_nogo


import my, my.dataload
import numpy as np, pandas, kkpandas
from ns5_process import LBPB, bcontrol
import glob, os.path


# Load cached prev_rew_stop if it exists
if os.path.exists('cached'):
    cached = my.misc.pickle_load('cached')
else:
    cached = {}
[... 514 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 5-2-timecourse_exemplars/main0_dumpcounts.py 5-2-timecourse_exemplars/main1.py 5-2-timecourse_exemplars/main2.py 5-2-timecourse_exemplars/main3.py; grep -n "stat__\|median\|iqr\|percentile" -B2 -A8 5-2-timecourse_exemplars/main4.py | head -80
```

```
# Estimate time course of effect in both blocks, with exemplars
# Unlike the other timecourse directory, here we only analyze by block,
# and not by go/nogo etc
# So begin by redumping the dfoldeds

import numpy as np, os.path
import pandas, itertools
from kkpandas import kkrs
import kkpandas
from ns5_process import myutils, LBPB
import my, my.dataload


# Which ulabels showed significant effect of hold
boot_results = pandas.load('../3-1-hold/hold_results')
sig_boot_results = boot_results[boot_results.p_adj < .05]

my.misc.no_warn_rs()

# All data
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,110p 5-2-timecourse_exemplars/main4.py
```

```
# Plots


import numpy as np, os.path
import pandas, itertools
from kkpandas import kkrs
import kkpandas
from ns5_process import myutils, LBPB
import my, my.dataload, my.plot, scipy.stats
import matplotlib.pyplot as plt
from matplotlib import mlab

plots_to_make = [
    'text summary of intervals',
    'exemplars traces',
    ]


# Hold results
hold_results = pandas.load('../3-1-hold/hold_results')
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 6-2-evokmisc/main0.py 6-2-evokmisc/main1.py 6-3-evokgain/main0.py
```

```
# Dump evoked counts from all audresp units, so that we can 
# then calculate some simple statistics on audresp latencies and strengths
from ns5_process import myutils, LBPB
import kkpandas, kkpandas.kkrs
import pandas, os.path
import numpy as np
import my, my.dataload, my.plot

# Include only units that passed feature check and were audresp
unit_db = my.dataload.getstarted()['unit_db']
audresp_units = unit_db.ix[unit_db.include &
    unit_db.audresp.isin(['good', 'weak', 'sustained'])]

# Iterate over units and regrab spikes from all stimuli, all trials
trial_picker_kwargs = 'all'
folding_kwargs = {'dstart': -.050, 'dtstop': .050}
rec_l = []
for ulabel in audresp_units.index:
    #~ myutils.printnow(ulabel)
    # Get folded and concatenate all trials
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,140p 6-3-evokgain/main2.py; grep -n "audresp" -r --include=*.py . | grep -v "^./modules" | head -30
```

```
# Plot results of main0
# correlation between hold and stim-equalized change
# Also print out the summary stats on stim-equalized subhold
# These are used to point out the CR12B thing
# Maybe some example units too


from ns5_process import myutils, LBPB
import kkpandas
import pandas, os.path
import numpy as np
import my, my.dataload, my.plot, scipy.stats
import matplotlib.pyplot as plt




# Load stim-equalized with hold
suffix = 'whold'
A1_stim_equalized_res_whold = pandas.load('A1_stim_equalized_res' + '_' + suffix)
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -n "with_labels\|with_inputs" docs/protocol.md | head -20
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 215,275p docs/protocol.md; grep -n "defs" -A60 schemas/claims.schema.json | sed -n 1,90p | grep -n '"' | head -60; grep -n "crcns" docs/archives.md | head
```

```
file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
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
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 244,330p schemas/claims.schema.json; sed -n 30,60p docs/archives.md; ls claims | grep -i crcns; ls claims/crcns-hc-7 2>/dev/null;
```

```
"$defs": {
    "expected": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "quantity",
        "value"
      ],
      "properties": {
        "quantity": {
          "type": "string"
        },
        "value": {
          "type": "number"
        },
        "tolerance": {
          "type": "number",
          "minimum": 0
        },
        "unit": {
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/crcns-hc-7/*.yaml; ls claims/crcns-*/
```

```
# Claims for Kohus, Kali, Rovira-Esteban, Schlingloff, Papp, Freund, Hajos & Gulyas (2016), J Physiol,
# "Properties and dynamics of inhibitory synaptic communication within the CA3 microcircuits of
# pyramidal cells and interneurons expressing parvalbumin or cholecystokinin", doi:10.1113/jp272231,
# on CRCNS data set hc-7 (doi:10.6080/K0MK69T5).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (J Physiol 2016, pp 1 to 30), as supplied under paper/ (text
# extracted from the PDF with PyMuPDF): Key points, Methods, Results, Discussion, the legends of
# Figures 1 to 13 and Tables 1 to 4. The paper has no supplement. The PDF could not be opened as
# images in this run (no renderer installed), so values printed only inside figures (the medians of
# Fig. 4B, 5C, 5Db, 6B and C, 7, 10, 11B and 12) were not read; claims on those figures rest on the
# Results and the legends. The extracted Table 4 holds every column: for the three PV+ types U0,
# tau_r (1080, 1620, 1700 ms), tau_e (23.7, 13.5, 13.6 ms), a_e, k_e and Imax; for CCK+BC to PC U0
# 0.15 (0.11, 0.18), tau_r 71 ms, tau_f 10.9 (7.2, 53.5) ms and Imax 499 (252, 708) pA. Table 4 gives
# the best model of each type; the Figure 11 legend gives the type parameters of a fit that includes
# use-dependent replenishment for all four types, and differs from Table 4 for CCK+BC to PC (tau_r
# 12.9 s against 71 ms) and for PV+BC to PV+BC tau_e (2.37 against 23.7 ms).
#
# Code. The paper links no code. Its Methods name in-house and third-party programs (Stimulog, EVAN,
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,140p claims/crcns-hc-7/*.yaml; grep -n "^dataset" -A4 claims/crcns-hc-7/*.yaml
```

```
#   detection on the raw sweeps, a uIPSC being a peak in the response window larger than three
#   standard deviations of the pre-AP baseline (a standard choice, not the paper's).
# M3. Which APs are "single" (Results, The type of interneuron determines the properties of uIPSCs
#   onto PCs, paragraph 1; Fig. 4Ca; Fig. 8A legend). Readings: (a) the single AP that precedes the
#   RIP train by 1000 ms (Methods, paragraph on protocols); (b) the ten APs of the 1 Hz train (the
#   Fig. 8A legend shows uIPSCs "triggered by 10 single action potentials"); (c) both pooled.
# M4. Amplitude in trains. The paper does not fix the window or baseline. Readings: (a) the per-sweep
#   amplitudes of the data set's tables, averaged over sweeps; (b) the peak of the sweep-averaged
#   trace in the interval from the AP to the next AP (or 10 ms after the last AP), measured from the
#   current just before that AP. Relative amplitude is the mean amplitude at each AP divided by the
#   mean amplitude of the first IPSC of the same train (Methods, paragraph 6), per pair; the group
#   value is the median over pairs (Fig. 6C and 9B legends; Statistical analysis).
# M5. Sweeps. The Methods say each pattern was repeated 10 (trains) or 10 or 20 times (RIP, EPI); the
#   Results say 20 bursts were averaged. All sweeps of a protocol are used. The Fig. 5A legend speaks
#   of a "steady-state average"; whether any first sweeps were left out is not said, so a variant
#   leaving out the first three sweeps is shown where a criterion depends on sweep averages.
# M6. Tests (Methods, Statistical analysis): Kruskal-Wallis across groups, post hoc Mann-Whitney U
#   with Bonferroni correction; the number of comparisons is not given, so the factor is the number of
#   pairwise comparisons among the groups of that panel (3 for three groups); Pearson chi-squared for
#   connection probabilities. A threshold of p < 0.05 unless the claim states another. The
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && cat 6-1-evoked/main0.py; sed -n 1,113p 6-1-evoked/main1.py; sed -n 1,102p 6-1-evoked/main2.py
```

```
# Evoked analysis
# Dump spike counts from random hits in onset window
# Include both A1 and PFC cells


from ns5_process import myutils, LBPB
import kkpandas
import pandas, os.path
import numpy as np
import my, my.dataload

my.misc.no_warn_rs()

# Unit db
gets = my.dataload.getstarted()
unit_db = gets['unit_db']

# Hold results
hold_results = pandas.load('../3-1-hold/hold_results')

[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,160p 6-1-evoked/main4.py; grep -n "def logreg_score2" -A80 6-1-evoked/decoders.py | head -120
```

```
# The final figs
# Decodability of target in both blocks and regions


import pandas, numpy as np, my, my.dataload, kkpandas, kkpandas.kkrs
from ns5_process import LBPB, myutils
import scipy.stats
import matplotlib.pyplot as plt, my.plot

# Load data
gets = my.dataload.getstarted()
unit_db = gets['unit_db']
hold_results = pandas.load('../3-1-hold/hold_results')
hold_results['diffHz'] = (hold_results['mPB'] - hold_results['mLB']) / \
    hold_results['dt']


my.plot.font_embed()
my.plot.publication_defaults()

[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,400p 7-1-zap/main1.py | grep -v "^\s*#~" | head -300
```

```
# Summary figures


import zap
import numpy as np
import matplotlib.pyplot as plt
import my, pandas
import scipy.stats

my.plot.font_embed()
my.plot.publication_defaults()

# Load the behavioral data
TI_d = my.misc.pickle_load('../data/miscellaneous/zap/TI_d')

# Compute stats
sstats = zap.compute_summary_stats(TI_d)
sstats2 = sstats.copy()
sstats2.columns = sstats2.columns.swaplevel(0, 1)

[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && grep -n "def compute_summary_stats" -A80 7-1-zap/zap.py | head -110
```

```
129:def compute_summary_stats(TI_d):
130-    """Compute summary stats on each session in TI_d"""
131-    sstats_l = []
132-    session_names = []
133-
134-    # These are the results that are stored from each computation
135-    keepcols = ['pmw', 'pfish',
136-        'zap_l', 'zap_m', 'zap_h',
137-        'ctl_l', 'ctl_m', 'ctl_h']    
138-
139-    for session_name, TI in TI_d.items():
140-        session_names.append(session_name)
141-        #rec = session_db.ix[session_name]
142-
143-        # Run all computes
144-        za = ZapAnalyzer(TI)
145-        res = {}
146-
147-        res.update(za.compute_by_block())
148-        res.update(za.compute_by_block_and_gonogo())
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,128p 7-1-zap/zap.py
```

```
"""Objects and functions for analyzing effect of zap on behavior"""


from ns5_process import bcontrol
import numpy as np, pandas
import my, my.stats, my.plot, glob, os.path
import matplotlib.pyplot as plt
import datetime, time
import scipy.stats

def compare(zdata, cdata):
    """Return mean, binom CIs, U-test, and Fisher's test on two unpaired arrays.
    
    This the inner function called by each control/disruption comparison.
    They differ mainly in how they choose zdata and cdata.
    zdata and cdata should be 1 for hit and 0 for non-hit
    
    Fisher's Exact Test (pfish) is the preferred p-value to use here.
    """
    subres = {}
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,126p 2-1-behavres/main05.py | grep -v "^\s*$" | head -90; grep -rn "698\|intertrial\|ITI\|n_trials" --include=*.py . | grep -v modules | head
```

```
# Catch trial analysis
import numpy as np
import os.path
import glob, pandas
import my, my.plot, my.dataload
import matplotlib.pyplot as plt
import scipy.stats
dir = '../data/miscellaneous/catch_trial_task'
my.plot.publication_defaults()
my.plot.font_embed()
# for ratnames
gets = my.dataload.getstarted()
def my_binom_test(x0, n0, x1, n1):
    return scipy.stats.fisher_exact([[x0, n0-x0], [x1, n1-x1]])[1]
catch_task_filenames = {
    'CR21A': 'CR21A_trials_info',
    'CR20B': 'CR20B_trials_info',
    }
ratname2TI = {}
for ratname, fn in catch_task_filenames.items():
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 1,71p 3-5-vidtrack/main1.py | grep -v "^\s*$" | head -60; grep -n "equaliz\|def \|binom\|utest\|MAD\|mad\|shuffle\|10000" 3-5-vidtrack/main4.py 3-5-vidtrack/main5.py | head -50
```

```
# Head angle histograms
import vidtrack
import my, my.dataload, kkpandas, os, pandas, numpy as np
import scipy.stats, my.stats
import matplotlib.pyplot as plt
import my.plot
my.plot.publication_defaults()
my.plot.font_embed()
plots_to_make = [
    'angl by session',
    ]
session_names = [
    'CR24A_121022_001_behaving',
    'CR20B_120602_001_behaving',
    'CR17B_110803_001_behaving']
test_res = pandas.load('test_res')
full_data = pandas.load('full_data')
# full_data is indexed by ulabel but we only need one per session
idxs = [[s for s in full_data.index.levels[0] if s.startswith(session_name)][0]
    for session_name in session_names]
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 28,75p 3-5-vidtrack/main4.py; sed -n 1,64p 3-5-vidtrack/main3.py | grep -v "^\s*$"; grep -n "def \|angl\|arctan" 3-5-vidtrack/main0.py | head -30
```

```
# hold results
hold_results = pandas.load('../3-1-hold/hold_results')

# angles and counts
full_data = pandas.load('full_data')

# subsampled indexes
session2subindex = my.misc.pickle_load('session2subindex')

# Iterate over ulabels and compare original and subsampled hold effect    
#res = {}
rec_l = []
for ulabel in full_data.index.levels[0]:
    # Get subsampled indexes
    session = kkpandas.kkrs.ulabel2session_name(ulabel)
    block2subindex = session2subindex[session]

    # Get this ulabel
    fdu = full_data.ix[ulabel]

[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && grep -n "anova\|fev\|FEV\|median" 3-5-vidtrack/main0.py 3-5-vidtrack/main2.py 3-5-vidtrack/main7.py 3-5-vidtrack/main8.py | head -40; sed -n 1,60p 3-5-vidtrack/main0.py | grep -v "^\s*$" | head -50
```

```
3-5-vidtrack/main0.py:69:    aov_res = my.stats.anova(full_df, 'np.sqrt(counts) ~ block * angl', typ=2)
3-5-vidtrack/main7.py:52:    # Fit a bunch of fake anovas
3-5-vidtrack/main7.py:61:        fake_aovres = my.stats.anova(fdu, 'faked_sqrt_counts ~ angl + block',
3-5-vidtrack/main7.py:69:    # Fit the real anova
3-5-vidtrack/main7.py:70:    real_aovres = my.stats.anova(fdu, 'sqrt_counts ~ angl + block', typ=2)
3-5-vidtrack/main8.py:86:        for line in box_shit['medians']:
3-5-vidtrack/main8.py:110:sdump = ['FEV of head angle in real and simulated data']
3-5-vidtrack/main8.py:113:    sdump.append("%s n=%d: median ess_angl: %0.3f, median fake_mean_ess_angl: %0.3f" % (
3-5-vidtrack/main8.py:114:        region, len(subdf), subdf['real_ess_angl'].median(),
3-5-vidtrack/main8.py:115:        subdf['fake_mean_ess_angl'].median()))
3-5-vidtrack/main8.py:117:with file('stat__FEV_of_head_angle_in_real_and_sim_data', 'w') as fi:
# First vidtrack script
# Put head angle and spike count data together, run ANOVAs, and dump
import vidtrack
import my, my.dataload, kkpandas, os, pandas, numpy as np
import scipy.stats, my.stats
# Video data location
root_dir = '../data/miscellaneous/vidtrack'
session_names = [
    'CR24A_121022_001_behaving',
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && grep -n "MIN_\|linregress\|pearson\|spearman\|kruskal\|wilcoxon\|ttest\|r_adj\|corr" 6-1-evoked/main6.py 6-1-evoked/main5.py 3-4-RT_vs_hold/main.py 3-4-RT_vs_hold/main3.py 5-1-timecourse/main2.py 8-1-model/main1.py 8-1-model/main2.py | head -50
```

```
6-1-evoked/main6.py:2:# does not correlate with hold effect.
6-1-evoked/main6.py:40:MIN_TRIAL_COUNT = 25
6-1-evoked/main6.py:42:    rows='ulabel', cols='block', values='n_trials').min(1) >= MIN_TRIAL_COUNT
6-1-evoked/main6.py:86:            scipy.stats.stats.linregress(x.flatten(), y.flatten())
6-1-evoked/main5.py:109:            F, p = scipy.stats.kruskal(*diff.values.T)
6-1-evoked/main5.py:111:            # Plot results of kruskal
6-1-evoked/main5.py:123:                # Save the p-values so that we can correct them
6-1-evoked/main5.py:124:                p_l = [scipy.stats.wilcoxon(diff[sname].values)[1]
6-1-evoked/main5.py:126:                p_l = my.stats.r_adj_pval(p_l)
6-1-evoked/main5.py:128:                # iterate over corrected so we can plot *s
3-4-RT_vs_hold/main.py:2:# Extract RT and MT for each trial, separated by block and correct/incorrect
3-4-RT_vs_hold/main.py:94:            ma, ya, ra, pa, sea = scipy.stats.linregress(v2, v1a)
3-4-RT_vs_hold/main.py:95:            mb, yb, rb, pb, seb = scipy.stats.linregress(v2, v1b)
3-4-RT_vs_hold/main3.py:58:        res[newkey] = my.stats.r_adj_pval(vals)
3-4-RT_vs_hold/main3.py:59:        print "%r: %d/%d signif corr" % (newkey,
3-4-RT_vs_hold/main3.py:69:    sdump = ['correlating motion time and hold period effect across neurons']
3-4-RT_vs_hold/main3.py:84:            # Get r and pvals for correlation
3-4-RT_vs_hold/main3.py:89:            t, p = scipy.stats.ttest_1samp(rvals, 0.)
3-4-RT_vs_hold/main3.py:113:    sdump = ['correlating reaction time and hold period effect across neurons']
3-4-RT_vs_hold/main3.py:128:            # Get r and pvals for correlation
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 60,100p 6-1-evoked/main6.py; sed -n 60,100p 3-4-RT_vs_hold/main.py; sed -n 40,100p 3-4-RT_vs_hold/main3.py; sed -n 1,60p 8-1-model/main1.py | grep -v "^\s*$"
```

```
# Join hold effect (quantified as log-ratio) and region
tunings = piv.join(hold_results[['mPB', 'mLB', 'region']])
tunings['lograt'] = np.log10(tunings['mPB'] / tunings['mLB'])

# Rename the tuning metrics
tune_metrics = ['lc_tuneQ', 'pc_tuneQ']
tunings = tunings.rename_axis({'lc': 'lc_tuneQ', 'pc': 'pc_tuneQ'})

# Drop any units that weren't tested in both blocks (for instance, because
# failed the trial count criterion in one block but not the other)
# with the current filtering, this shouldn't happen anyway
tunings = tunings.dropna()

for region in ['A1', 'PFC']:
    subtunings = my.pick_rows(tunings, region=region)
    
    # Correlate with hold effect
    f, axa = plt.subplots(1, 2, figsize=(7,3))
    f.subplots_adjust(left=.125, right=.95, wspace=.475)
    for ax, tune_metric in zip(axa.flatten(), tune_metrics):
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && grep -n "ratname2num" -A12 modules/my/dataload.py | head -30; grep -n "def difference_CI_bootstrap_wrapper" -A50 modules/my/bootstrap.py | grep -n "p\b\|'p'\|pval\|min_bucket" | head
```

```
171:    res['ratname2num'] = pandas.Series(
172-        ['Rat 1', 'Rat 2', 'Rat 3', 'Rat 4', 'Rat 5', 'Rat 6'],
173-        ['CR12B', 'CR17B', 'YT6A', 'CR20B', 'CR21A', 'CR24A'])
174-    
175-    # Metadata: location of kk_servers
176-    res['kksfiles'] = dict([
177-        (ratname, os.path.join(root_dir, 'metadata', ratname + '_behaving.kks'))
178:        for ratname in res['ratname2num'].index])
179-    res['kk_servers'] = dict([
180-        (ratname, kkpandas.kkio.KK_Server.from_saved(kksfile))
181-        for ratname, kksfile in res['kksfiles'].items()])
182-    
183-    # Fix the relative paths in the kk_servers
184-    for ratname, kks in res['kk_servers'].items():
185-        for session_name in kks.session_d:
186-            kks.session_d[session_name] = os.path.join(
187-                root_dir, 'data', ratname, session_name, 'klusters0')
188-
189-    # Data directory
190-    res['data_dirs'] = dict([(ratname, os.path.join(root_dir, 'data', ratname))
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 14,130p 6-1-evoked/main5.py | grep -v "^\s*$\|^\s*#~"
```

```
unit_db = my.dataload.getstarted()['unit_db']
# Analyze only included units with audresps
units_to_analyze = my.pick_rows(unit_db, audresp=['good', 'weak', 'sustained'],
    include=True)
# Load evoked responses from previous analysis
evoked_resps = pandas.load('evoked_resps')
# Load hold results
hold_results = pandas.load('../3-1-hold/hold_results')
# Mean the evoked responses
mer = evoked_resps[LBPB.mixed_stimnames].applymap(np.mean)
# Convert to hertz
mer = mer.divide(evoked_resps['evok_dt'], axis=0)
# Join the hold for subtraction
hr = hold_results[['mLB', 'mPB']].divide(hold_results['dt'], axis=0)
mer['hold_LB_hz'] = hr['mLB'].ix[mer.index]
mer['hold_PB_hz'] = hr['mPB'].ix[mer.index]
# Square-root to normalize variance
mer = np.sqrt(mer)
# Split by block
snames = LBPB.mixed_stimnames_noblock
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && sed -n 120,135p 3-4-RT_vs_hold/main3.py; sed -n 1,58p 3-4-RT_vs_hold/main.py | grep -n "RT\|MT\|include_l\|units_to"
```

```
f, axa = plt.subplots(1, 2, figsize=(7, 3))
        f.subplots_adjust(left=.125, right=.95, wspace=.475)
        f.suptitle((region, 'RT'))
        
        # One col per block
        for nb, block in enumerate(['LB', 'PB']):
            ax = axa[block == 'PB']
            
            # Get r and pvals for correlation
            rvals = res['all hits']['rRT'][region][block]
            pvals = res['all hits']['pRT_adj'][region][block]
            
            # Test pop
            t, p = scipy.stats.ttest_1samp(rvals, 0.)
            
            sdump.append(
1:# Correlate RTs with neural activity
2:# Extract RT and MT for each trial, separated by block and correct/incorrect
16:units_to_analyze = unit_db[unit_db.include]
23:include_l = [
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Rodgers2014 && grep -n "bins\|Smooth\|smooth\|ttest\|meth" 5-1-timecourse/main2.py | head -20
```

```
20:bins = kkpandas.define_bin_edges2(t_start=-3., t_stop=3, binwidth=.05)
21:bincenters = 0.5 * (bins[:-1] + bins[1:])
22:distr_bins = kkpandas.define_bin_edges2(t_start=-3., t_stop=3, binwidth=.1)
23:meth = np.histogram
35:        bins=bins, meth=meth)
83:        plot_distrs(ax, ax_distrs, bottom_edge, locking_event, distr_bins)
151:        plot_distrs(ax, ax_distrs, bottom_edge, locking_event, distr_bins, maxheight=1)
211:        plot_distrs(ax, ax_distrs, bottom_edge, locking_event, distr_bins, maxheight=.75)
Shell cwd was reset to
```

**Agent**

I've read the code for every figure. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml",
 "content": "# Claims for Rodgers & DeWeese (2014), Neuron 82, 1157-1170, \"Neural correlates of task switching in\n# prefrontal cortex and primary auditory cortex in a novel stimulus selection task for rodents\",\n# doi:10.1016/j.neuron.2014.04.031, on CRCNS data set pfc-1 (doi:10.6080/K0W66HPJ).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader), version pilot-13.\n#\n# Text read: the version of record with its Supplemental Information, as supplied under paper/ (text\n# extracted from the PDF with PyMuPDF): Summary, Introduction, Results, Discussion, Experimental\n# Procedures, the legends of Figures 1 to 8, the legends of Figures S1 to S7 and the Supplemental\n# Experimental Procedures. The PDF pages were not opened; every number used here is printed in the\n# text or a legend. The data descriptor (paper/pfc-1.data-description.txt) was read only to know what\n# the data set holds.\n#\n# Code read: github.com/cxrodgers/Rodgers2014 at commit 390b6089c429877dfea9c56de153bbea0380c20f\n# (2016-07-09), linked from the Experimental Procedures. It holds one folder of Python 2 scripts per\n# figure (2-1-behavres, 3-1-hold, 3-2-errhold, 3-3-vs_spont, 3-4-RT_vs_hold, 3-5-vidtrack,\n# 5-1-timecourse, 5-2-timecourse_exemplars, 6-1-evoked, 6-2-evokmisc, 6-3-evokgain, 7-1-zap, 8-1-model),\n# the helper modules (my, kkpandas, ns5_process, vidtrack) and a metadata folder:\n# metadata/unit_db.csv (one row per sorted cluster, with an include flag, the region, the auditory\n# response class audresp and the response window audresp_t1 to audresp_t2), metadata/sessions_df.csv\n# (55 sessions) and metadata/figures_generated_by_each_script.csv (which script makes which panel).\n# The code's README says the data set's spike files hold good units and bad clusters alike, and that\n# only units listed in unit_db.csv with include True were analyzed. The scripts that set the include\n# flag (sort quality, waveform and firing-rate drift checks) and the audresp class and window are not\n# in the repository; the table holds their results. Claims on single units therefore take the unit\n# set, and where needed the audresp class and window, from that table (data with_labels); where the\n# Supplement describes how to recompute them, a recomputation is named as a second reading.\n#\n# Data the paper used. Male Long-Evans rats trained on an auditory stimulus selection task in a\n# three-port box. Each trial, after a center-poke hold (0 to 100 ms in Rats 1 to 3, 250 to 350 ms in\n# Rats 4 to 6), a 250 ms stimulus pair is played: a broadband noise burst from the LEFT or RIGHT\n# speaker plus a LOW (6 kHz) or HIGH (16 kHz) warble from both. Localization blocks (go left for LEFT,\n# nogo for RIGHT) alternate with pitch discrimination blocks (go right for LOW, nogo for HIGH); each\n# block is 80 trials, the first 20 cue trials without distractor. Recordings: tetrodes in A1 and/or\n# prelimbic mPFC of six rats; the code names them Rat 1 CR12B, Rat 2 CR17B, Rat 3 YT6A, Rat 4 CR20B,\n# Rat 5 CR21A, Rat 6 CR24A; 121 mPFC and 99 A1 single units (unit_db.csv include True; CR12B and CR17B\n# A1 only). Measured variables: spike times; per trial the stimulus, block, outcome (hit, error,\n# wrong_port), cpoke_start, stim_onset, cpoke_stop, choice_made, nonrandom and is_munged flags. Other\n# experiments: electrical disruption of mPFC in three further rats (Z1, Z2, Z3; the code names them\n# CR25A, CR28A, CR28B; 6, 8 and 8 sessions; 10 Hz pulse trains on 20% of trials); a catch-trial task in\n# two rats (CR20B, CR21A; novel distractor on 15% of trials); video scoring of ear positions in three\n# sessions (CR24A_121022, CR20B_120602, CR17B_110803); and the results of the network simulation of\n# Figure 8. By its description the CRCNS data set holds the spike times and trial files of every\n# session, and, under miscellaneous/, the catch-trial, disruption (zap), video (vidtrack) and model\n# simulation data.\n#\n# Shared method details, used by the criteria below.\n# M1. Units. The 220 units with include True in metadata/unit_db.csv; region from its region column\n#   (which matches the data descriptor's rule on unit numbers). Paper: Supplemental Experimental\n#   Procedures, Analysis of waveform variation and firing rate drift; Power analysis (at least 20\n#   hold-period spikes).\n# M2. Trials. Correct (hit) trials of the non-cue blocks (block 2 localization, block 4 pitch\n#   discrimination), nonrandom 0, munged trials dropped, as the code's trial picker \"random hits by\n#   block\" does (modules/my/dataload.py; kkpandas.io.load_trials_info drops munged trials). Trials with\n#   a hold under 50 ms are dropped (Supplemental Experimental Procedures, Trial timings).\n# M3. Hold-period count and rule encoding (Figure 3C legend; Supplemental Experimental Procedures,\n#   Trial timings; 3-1-hold/main0.py, main1.py). Spikes counted in the window ending at stimulus\n#   onset, 50 ms long for Rats 1 to 3 and 250 ms for Rats 4 to 6; rate is count over window. A unit\n#   encodes the selection rule when an unpaired two-sided Mann-Whitney U-test of its counts in the\n#   two blocks gives a Benjamini-Hochberg adjusted p below 0.05. The code runs R's wilcox.test with\n#   exact=FALSE and adjusts the p-values of all 220 units of both regions together; the paper does\n#   not say whether the adjustment is per region. Readings, (a) pooled over both regions, as the\n#   code; (b) per region. The preferred block is the one with the higher mean count.\n# M4. Auditory-responsive units (Supplemental Experimental Procedures, Calculation of evoked\n#   responses; Figure S5A legend). Readings, (a) audresp in good, weak or sustained in unit_db.csv,\n#   with the window audresp_t1 to audresp_t2, as every evoked script of the code uses; (b) recomputed\n#   as the Supplement says (spike trains smoothed with a 1 ms Gaussian, every 0.5 ms bin after onset\n#   compared by unpaired Mann-Whitney test with all 0.5 ms bins of the 50 ms before onset, the first\n#   contiguous run of significant bins is the window, windows under 1 ms discarded). For (b) the\n#   paper leaves open the trials used (Figure S5A says all stimuli and trials), the per-bin threshold\n#   and any correction (p < 0.05 uncorrected is used here as the standard choice), and how the four\n#   of 108 atypical units were judged; (b) is a variant, (a) the main reading.\n# M5. Tests. \"Paired Mann-Whitney\" in the paper is R's wilcox.test with paired=TRUE in the code\n#   (my.stats.r_utest), that is the Wilcoxon signed-rank test. Binomial tests are two-sided\n#   (scipy.stats.binom_test). Tolerances are 10% of the reported value unless a claim says otherwise.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: pfc-1\n  doi: 10.6080/K0W66HPJ\npaper: doi:10.1016/j.neuron.2014.04.031\nclaims:\n- id: fig2a-above-chance\n  statement: Trained rats perform significantly above 50% correct in both localization and pitch\n    discrimination blocks in the recording sessions, with a median of 698 trials per session; the\n    best rats reach about 85% in both blocks. Sessions not above 50% in either block (4 of 55) were\n    discarded.\n  source: Results, A Novel Behavioral Task for Rodents, paragraph 2; Figure 2A; Supplemental\n    Experimental Procedures, Chance performance on the task\n  quote: Trained rats performed many trials per session (median, 698). We verified that the rats\n    were performing significantly above 50% in both blocks ... Our best rats' typical performance\n    during recording sessions was approximately 85% in both blocks ... although some sessions failed\n    the first criterion and were discarded (p > 0.05 for 4/55 sessions)\n  expected:\n  - quantity: median trials per session\n    value: 698\n    tolerance: 69.8\n  - quantity: best rat's typical performance in each block\n    value: 85\n    tolerance: 8.5\n    unit: percent\n  criterion: Performance per session and block as 2-1-behavres/perf.py computes it, hits over hits\n    plus errors plus wrong-port trials, non-cue blocks 2 and 4, nonrandom 0; sessions as in\n    2-1-behavres/main00.py (sessions_df.csv include True, less the catch-trial session\n    CR20B_120613_001_behaving). Each session and block is tested against 0.5 with a binomial test\n    (Supplement). Reproduced when at most 4 of the sessions fail in either block, the median trial\n    count is within tolerance and, for at least one rat, the median over its sessions is within\n    tolerance of 85% in both blocks. Open, and named as readings. The trials counted per session,\n    (a) all trials performed (outcome not future_trial), (b) after dropping munged and nonrandom\n    trials. Which 55 sessions the paper's count refers to, (a) the 55 of sessions_df.csv, all marked\n    include, so the four failing sessions may be among them; (b) a set before the cut, so that none\n    of the data set's sessions should fail. Under (b) the claim is reproduced only when no analysed\n    session fails.\n- id: figs1a-go-better-than-nogo\n  statement: Performance is typically better on go trials than on nogo trials.\n  source: Results, A Novel Behavioral Task for Rodents, paragraph 2; Figure S1A\n  quote: Performance was typically better on go trials than on nogo trials\n  criterion: As 2-1-behavres/main02.py, per rat the mean over sessions of the performance on go and\n    on nogo trials in each block (perf.py, nonrandom 0). Reproduced when go exceeds nogo in at least\n    7 of the 12 rat and block pairs (a majority, reading \"typically\"); the pairs are reported.\n  depends_on:\n  - fig2a-above-chance\n- id: iti-median\n  statement: The median intertrial interval is 4.0 s (interquartile range 2.7 to 5.3 s).\n  source: Results, Within-Trial Timescale of the Encoding of the Selection Rule, paragraph 1\n  quote: Across the data set, the median intertrial interval was 4.0 s (interquartile range, 2.7-5.3\n    s)\n  expected:\n  - quantity: median intertrial interval\n    value: 4.0\n    tolerance: 0.4\n    unit: s\n  - quantity: first quartile\n    value: 2.7\n    tolerance: 0.27\n    unit: s\n  - quantity: third quartile\n    value: 5.3\n    tolerance: 0.53\n    unit: s\n  criterion: Neither the paper nor the code defines the interval. Readings, (a) time between\n    consecutive stimulus onsets; (b) time between consecutive center-poke starts; each over all\n    trials of the sessions with included units, pooled. Reproduced when under one reading the\n    median and both quartiles are within tolerance.\n- id: fig3c-pfc-rule-encoding\n  statement: In the hold period of correct trials, 63% (76 of 121) of mPFC neurons individually\n    encode the selection rule; 36 prefer localization and 40 pitch discrimination, and neither\n    preference is significantly more common.\n  source: Results, Anticipatory Neuronal Activity in mPFC and A1 Encodes the Selection Rule,\n    paragraph 3; Figure 3C\n  quote: population of mPFC neurons, 63% (76/121) of the neurons individually and significantly\n    encoded the selection rule during the hold period (Figure 3C). Of these, 36 neurons preferred\n    (i.e., fired ... more during) localization and 40 preferred pitch discrimination; neither\n    preference was significantly more common (binomial test, p > 0.05)\n  statistics:\n  - about: localization-preferring against pitch-discrimination-preferring counts\n    test: binomial test\n    p: 0.05\n    p_relation: \">\"\n    n: 76 rule-encoding mPFC neurons\n  expected:\n  - quantity: mPFC neurons encoding the rule\n    value: 76\n    tolerance: 7.6\n  - quantity: mPFC neurons preferring localization\n    value: 36\n    tolerance: 3.6\n  - quantity: mPFC neurons preferring pitch discrimination\n    value: 40\n    tolerance: 4\n  criterion: Units M1, trials M2, test M3 under both readings of the adjustment. Reproduced when\n    under one reading the three counts are within tolerance and a two-sided binomial test of the two\n    preference counts gives p > 0.05.\n  data: with_labels\n- id: fig4c-a1-rule-encoding\n  statement: In the hold period of correct trials, 36% (36 of 99) of A1 neurons encode the selection\n    rule; 13 prefer localization and 23 pitch discrimination, and neither preference is significantly\n    more common.\n  source: Results, Anticipatory Neuronal Activity in mPFC and A1 Encodes the Selection Rule,\n    paragraph 4; Figure 4C\n  quote: Across our recorded population, 36% (36/99) of A1 neurons encoded selection rule. As with\n    mPFC, neither population was significantly larger (13 preferring localization, 23 preferring pitch\n    discrimination; binomial test, p > 0.05)\n  statistics:\n  - about: localization-preferring against pitch-discrimination-preferring counts\n    test: binomial test\n    p: 0.05\n    p_relation: \">\"\n    n: 36 rule-encoding A1 neurons\n  expected:\n  - quantity: A1 neurons encoding the rule\n    value: 36\n    tolerance: 3.6\n  - quantity: A1 neurons preferring localization\n    value: 13\n    tolerance: 1.3\n  - quantity: A1 neurons preferring pitch discrimination\n    value: 23\n    tolerance: 2.3\n  criterion: As fig3c-pfc-rule-encoding, for the A1 units.\n  data: with_labels\n- id: a1-rule-encoding-not-audresp-dependent\n  statement: In A1, rule encoding is not significantly more common among stimulus-responsive\n    neurons (14 of 49) than among nonresponsive ones (22 of 50).\n  source: Results, Anticipatory Neuronal Activity in mPFC and A1 Encodes the Selection Rule,\n    paragraph 4\n  quote: Rule encoding was not significantly more widespread in either stimulus-responsive (14/49) or\n    nonresponsive (22/50) neurons (p > 0.05, Fisher's exact test)\n  statistics:\n  - test: Fisher's exact test\n    p: 0.05\n    p_relation: \">\"\n    n: 49 responsive and 50 nonresponsive A1 neurons\n  expected:\n  - quantity: rule-encoding among responsive A1 neurons\n    value: 14\n    tolerance: 1.4\n  - quantity: rule-encoding among nonresponsive A1 neurons\n    value: 22\n    tolerance: 2.2\n  criterion: A claim of absence. Responsiveness by M4, rule encoding by M3; a two-sided Fisher's exact\n    test on the 2 x 2 table, as 3-1-hold/main3.py. Reproduced when p > 0.05; the counts and the\n    odds ratio are reported.\n  data: with_labels\n  depends_on:\n  - fig4c-a1-rule-encoding\n- id: rule-encoding-effect-size\n  statement: Among rule-encoding neurons, the median increase in hold-period firing rate in the\n    preferred block is 74.7% in mPFC and 99.7% in A1.\n  source: Results, Anticipatory Neuronal Activity in mPFC and A1 Encodes the Selection Rule,\n    paragraph 5\n  quote: among rule-encoding neurons, the median increase in firing rate during the preferred block\n    was 74.7% in mPFC and 99.7% in A1\n  expected:\n  - quantity: median increase, mPFC\n    value: 74.7\n    tolerance: 7.47\n    unit: percent\n  - quantity: median increase, A1\n    value: 99.7\n    tolerance: 9.97\n    unit: percent\n  criterion: As 3-1-hold/main3.py, per rule-encoding unit the larger of the two ratios of mean\n    hold-period rates (preferred over non-preferred), minus 1; the median over units of each\n    region.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: fig3ab-pfc-example-units\n  statement: Two simultaneously recorded mPFC units encode the rule with opposite preferences; one\n    fires 12.1 Hz in localization against 7.2 Hz in pitch discrimination (483 and 295 trials), the\n    other 5.4 Hz in pitch discrimination against 2.7 Hz in localization, both p < 0.001.\n  source: Figure 3A and 3B legends\n  quote: During the hold period (gray), the firing rate is significantly (p < 0.001, unpaired\n    Mann-Whitney U-test) higher on localization (mean 12.1 Hz, n = 483) than on pitch discrimination\n    (mean 7.2 Hz, n = 295) trials ... The hold period firing rate is significantly (p < 0.001) higher\n    on pitch discrimination (mean 5.4 Hz) than on localization (mean 2.7 Hz) trials\n  statistics:\n  - test: unpaired Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 483 localization and 295 pitch discrimination trials\n  expected:\n  - quantity: unit A localization rate\n    value: 12.1\n    tolerance: 1.21\n    unit: Hz\n  - quantity: unit A pitch discrimination rate\n    value: 7.2\n    tolerance: 0.72\n    unit: Hz\n  - quantity: unit B pitch discrimination rate\n    value: 5.4\n    tolerance: 0.54\n    unit: Hz\n  - quantity: unit B localization rate\n    value: 2.7\n    tolerance: 0.27\n    unit: Hz\n  - quantity: localization trials\n    value: 483\n    tolerance: 48.3\n  - quantity: pitch discrimination trials\n    value: 295\n    tolerance: 29.5\n  criterion: The units are named in metadata/figures_generated_by_each_script.csv, 3A\n    CR24A_121021_001_behaving-257 and 3B CR24A_121021_001_behaving-259. Hold rates and test as M2\n    and M3 (250 ms window); reproduced when the rates and trial counts are within tolerance and each\n    unadjusted test gives p < 0.001.\n  data: with_labels\n- id: fig4ab-a1-example-units\n  statement: Two simultaneously recorded A1 units encode the rule; one fires 8.0 Hz in localization\n    against 4.8 Hz in pitch discrimination, the other 10.1 Hz in pitch discrimination against 2.0 Hz\n    in localization, both p < 0.001.\n  source: Figure 4A and 4B legends\n  quote: An example A1 neuron that responds significantly more (p < 0.001) during localization (8.0\n    Hz, n = 312 trials) than during pitch discrimination (4.8 Hz, n = 253) ... Simultaneously recorded\n    A1 neuron that significantly (p < 0.001) prefers pitch discrimination (10.1 Hz, n = 312 trials)\n    over localization (2.0 Hz, n = 253)\n  statistics:\n  - test: unpaired Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: unit A localization rate\n    value: 8.0\n    tolerance: 0.8\n    unit: Hz\n  - quantity: unit A pitch discrimination rate\n    value: 4.8\n    tolerance: 0.48\n    unit: Hz\n  - quantity: unit B pitch discrimination rate\n    value: 10.1\n    tolerance: 1.01\n    unit: Hz\n  - quantity: unit B localization rate\n    value: 2.0\n    tolerance: 0.2\n    unit: Hz\n  criterion: Units as named in metadata/figures_generated_by_each_script.csv, 4A\n    CR20B_120602_001_behaving-612 and 4B CR20B_120602_001_behaving-712; method as\n    fig3ab-pfc-example-units. The two legends give the same session's trial counts with the blocks\n    swapped (312 localization and 253 pitch discrimination in 4A, the reverse in 4B), so the counts\n    are compared as a pair, 312 and 253 within 10% each, in either assignment, and the assignment\n    found is reported.\n  data: with_labels\n- id: fig3d-pfc-interference\n  statement: In mPFC rule-encoding neurons, rule encoding is weakened on interference trials; the\n    hold-period response on interference trials is higher than on correct trials in the\n    non-preferred block and lower in the preferred block (57 neurons).\n  source: Results, Error Trial Analysis, paragraph 2; Figure 3D legend\n  quote: in mPFC, the encoding of selection rule was significantly weakened on interference trials,\n    as compared with correct trials ... The population response on interference trials is\n    significantly increased during the nonpreferred block and decreased during the preferred block (n\n    = 57 neurons, paired Mann-Whitney test)\n  statistics:\n  - test: paired Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    n: 57 neurons\n  expected:\n  - quantity: mPFC neurons in the analysis\n    value: 57\n    tolerance: 5.7\n  criterion: As 3-2-errhold/main1.py and main2.py. Hold counts as M3 on all trials of blocks 2 and 4\n    with nonrandom 0, by stimulus and outcome. Categories per block, hits; interference trials,\n    wrong-port responses to stimuli whose distractor cues a go (localization le_lo_lc and ri_lo_lc,\n    pitch discrimination le_hi_pc and le_lo_pc); go-on-nogo errors (localization ri_hi_lc and\n    ri_lo_lc, pitch discrimination le_hi_pc and ri_hi_pc). Rule-encoding units (M3) with at least 3\n    trials in each of the six categories; rates in Hz relabelled by preferred block and normalized\n    by subtracting the hit rate in the non-preferred block. Wilcoxon signed-rank tests (M5) across\n    neurons, hit against interference in the non-preferred block and in the preferred block.\n    Reproduced when both are significant at p < 0.05 with interference higher in the non-preferred\n    and lower in the preferred block; partially reproduced when one holds.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n- id: fig4d-a1-interference\n  statement: In A1 rule-encoding neurons the rule encoding is reversed on interference trials; the\n    hold-period response on interference trials is greater in the non-preferred block than in the\n    preferred block (16 neurons).\n  source: Results, Error Trial Analysis, paragraph 2; Figure 4D legend\n  quote: The population response on interference trials (orange bars) is significantly greater\n    during the nonpreferred block than during the preferred block (p < 0.01, n = 16 neurons, paired\n    Mann-Whitney U-test)\n  statistics:\n  - test: paired Mann-Whitney U-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 16 neurons\n  expected:\n  - quantity: A1 neurons in the analysis\n    value: 16\n    tolerance: 1.6\n  criterion: As fig3d-pfc-interference, for A1 units; the test is interference in the preferred\n    block against interference in the non-preferred block (3-2-errhold/main2.py). Reproduced when the\n    non-preferred interference response is higher with p < 0.01.\n  data: with_labels\n  depends_on:\n  - fig4c-a1-rule-encoding\n- id: figs2f-s3f-bidirectional-vs-spont\n  statement: Across rule-encoding neurons in both regions, the hold-period rate is significantly\n    above the spontaneous rate in the preferred block and significantly below it in the\n    non-preferred block.\n  source: Results, Within-Trial Timescale of the Encoding of the Selection Rule, paragraph 4; Figures\n    S2F and S3F\n  quote: across the population of rule-encoding neurons, the firing rate was significantly higher\n    than spontaneous during the preferred block and significantly lower than spontaneous during the\n    nonpreferred block\n  statistics:\n  - test: paired Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As 3-3-vs_spont/main2.py and main3.py. Spontaneous rate of each unit, the spike count\n    over the time between its session's first and last stimulus onset that lies more than 2 s from\n    every stimulus onset (all trials, munged included, time in 0.1 s steps); hold rates as M3.\n    Wilcoxon signed-rank tests (M5) of hold rate against spontaneous rate, in each region for the\n    localization-preferring and the pitch-discrimination-preferring units separately, each block.\n    Reproduced when, in all four region and preference groups, the preferred-block rate is above and\n    the non-preferred-block rate below the spontaneous rate at p < 0.05; partially reproduced when\n    this holds in some groups. The paper's text pools preferences, so the pooled test per region\n    (preferred and non-preferred relabelled) is shown as a variant.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: fig5ab-single-unit-onset\n  statement: The median rule-encoding unit first shows a significant block preference 0.55 s before\n    the stimulus in A1 and 0.625 s before it in mPFC, so most develop it before the trial is\n    initiated.\n  source: Results, Within-Trial Timescale of the Encoding of the Selection Rule, paragraphs 1 and 2;\n    Figures 5A and 5B\n  quote: In A1, the median rule-encoding unit first developed a significant block preference 0.55 s\n    prestimulus; in PFC, the median was 0.625 s prestimulus. Thus, the majority of rule-encoding\n    neurons developed this property well before the rat initiated a trial by center-poking\n  expected:\n  - quantity: median onset, A1\n    value: 0.55\n    tolerance: 0.05\n    unit: s before stimulus onset\n  - quantity: median onset, mPFC\n    value: 0.625\n    tolerance: 0.05\n    unit: s before stimulus onset\n  criterion: Per rule-encoding unit, M2 trials, spike trains smoothed with a 50 ms Gaussian and\n    sampled in 50 ms bins (Results; Figure 5A legend; 5-2-timecourse_exemplars/main1.py), an\n    unpaired Mann-Whitney test between blocks in each bin, p-values adjusted by Benjamini-Hochberg\n    over all bins and units together (main2.py, main3.py); the interval is the contiguous run of\n    significant bins, with the preferred direction, that contains the bin just before stimulus\n    onset, and its first bin is the onset; median over units per region (main4.py). The tolerance is\n    one 50 ms bin, the resolution of the measure. The window differs, the Results say up to 3 s\n    before and after onset, the code uses 5 s; the Results' 3 s is the main reading and 5 s a\n    variant. Reproduced when both medians are within tolerance and both exceed 0.35 s, the longest\n    hold.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: fig5c-population-onset\n  statement: The population activity of rule-encoding neurons in their preferred block ramps up\n    before the stimulus and is significantly elevated earlier in mPFC (from 2.7 s before stimulus\n    onset) than in A1 (from 0.88 s).\n  source: Results, Within-Trial Timescale of the Encoding of the Selection Rule, paragraph 3; Figure\n    5C legend\n  quote: The PFC population increases its response earlier (first significantly activated 2.7 s\n    before stimulus onset) than the A1 population (first significantly activated 0.88 s before\n    stimulus onset)\n  statistics:\n  - test: one-sample t test\n    p: 0.05\n    p_relation: \"<\"\n    n: 76 mPFC and 36 A1 neurons\n  expected:\n  - quantity: first significant time, mPFC\n    value: 2.7\n    tolerance: 0.27\n    unit: s before stimulus onset\n  - quantity: first significant time, A1\n    value: 0.88\n    tolerance: 0.088\n    unit: s before stimulus onset\n  criterion: As 5-1-timecourse/main1.py and main2b.py and the Supplement (Timecourse analysis). Hits\n    on the eight non-cue stimulus pairs, nonrandom 0, locked to stimulus onset; 50 ms bins from -2.9\n    to 2.9 s, 50 ms Gaussian smoothing; each unit's rates z-scored over all bins and stimulus pairs,\n    averaged within go and nogo pairs of each block and then over go and nogo; the preferred block\n    of each rule-encoding unit. Per bin a one-sample t-test against 0 over units, Benjamini-Hochberg\n    over bins; the first significant bin with positive mean is the onset (bin centre). Reproduced\n    when both times are within tolerance and the mPFC time is earlier; partially reproduced when\n    only the order holds.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: fig5d-go-nogo\n  statement: In the preferred block, after the rat leaves the center port, the population rate of\n    rule-encoding neurons stays above baseline for several seconds on nogo trials and falls below\n    baseline on go trials, in both mPFC and A1.\n  source: Results, Encoding of Behavioral Choice, paragraph 1; Figure 5D legend\n  quote: On nogo trials (gray), the firing rate remained elevated above baseline for at least several\n    seconds ... On go trials, the firing rate was suppressed below baseline as the rat moved to the\n    choice port and consumed a reward\n  criterion: As 5-1-timecourse/main1.py and main2.py, locked to center-port exit (cpoke_stop), 50 ms\n    bins from -3 to 3 s, counts without smoothing, z-scored per unit as in fig5c-population-onset\n    (baseline is 0); the preferred block; go and nogo pairs kept apart. The paper reports no test\n    or window for this panel. Readings, (a) the mean over units of the mean z-scored rate from 0 to\n    3 s after exit, tested against 0 with a one-sample t-test over units (the test of Figure 5C);\n    (b) per-bin one-sample t-tests with Benjamini-Hochberg over bins, as for Figure 5C, the claim\n    holding when nogo is significantly above 0 and go significantly below 0 over most bins of 0.5\n    to 3 s. Reproduced when under one reading nogo is above and go below baseline at p < 0.05 in\n    both regions; partially reproduced when this holds in one region.\n  data: with_labels\n  depends_on:\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: audresp-prevalence\n  statement: Auditory-responsive neurons are significantly rarer in mPFC (31 of 121) than in A1 (49\n    of 99).\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    1\n  quote: \"Auditory-responsive neurons in mPFC were significantly rarer (mPFC, 31/121; A1, 49/99; p <\n    0.001, Fisher's exact test) than in A1\"\n  statistics:\n  - test: Fisher's exact test\n    p: 0.001\n    p_relation: \"<\"\n    n: 121 mPFC and 99 A1 neurons\n  expected:\n  - quantity: auditory-responsive mPFC neurons\n    value: 31\n    tolerance: 3.1\n  - quantity: auditory-responsive A1 neurons\n    value: 49\n    tolerance: 4.9\n  criterion: Responsiveness by M4 (both readings), two-sided Fisher's exact test as\n    6-2-evokmisc/main1.py. Reproduced when under one reading both counts are within tolerance and\n    p < 0.001.\n  data: with_labels\n- id: figs5cd-evoked-strength\n  statement: Onset responses are stronger in auditory-responsive A1 neurons than in mPFC neurons,\n    0.12 against 0.02 extra spikes per trial (median) and 209% against 171% of baseline.\n  source: Figure S5C and S5D legends\n  quote: \"The responses are significantly stronger in A1 neurons (median: 0.12 spikes) than in PFC\n    neurons (median: 0.02 spikes), p < 0.001, unpaired Mann-Whitney U-test ... Again the responses\n    are stronger in A1 neurons (median: 209% of baseline) than in PFC neurons (median: 171% of\n    baseline), p < 0.001, unpaired Mann-Whitney U-test\"\n  statistics:\n  - about: extra spikes\n    test: unpaired Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 49 A1 and 31 mPFC neurons\n  - about: percent of baseline\n    test: unpaired Mann-Whitney U-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 49 A1 and 31 mPFC neurons\n  expected:\n  - quantity: median extra spikes, A1\n    value: 0.12\n    tolerance: 0.012\n  - quantity: median extra spikes, mPFC\n    value: 0.02\n    tolerance: 0.002\n  - quantity: median response, A1\n    value: 209\n    tolerance: 20.9\n    unit: percent of baseline\n  - quantity: median response, mPFC\n    value: 171\n    tolerance: 17.1\n    unit: percent of baseline\n  criterion: As 6-2-evokmisc/main0.py and main1.py. All trials and stimuli of each responsive unit\n    (M4); baseline rate from the 50 ms before onset, evoked rate in the response window; extra\n    spikes are (evoked rate minus baseline rate) times the window length, percent is evoked over\n    baseline rate. Reproduced when the four medians are within tolerance and both tests give\n    p < 0.001.\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: figs5e-latency\n  statement: The median response latency of auditory-responsive mPFC neurons is slightly but\n    significantly longer than in A1, 19.75 against 16.75 ms.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    1; Figure S5E legend\n  quote: Their median response latency was also significantly longer, though only slightly (19.75 ms\n    versus 16.75 ms in A1; Figure S5E) ... though only slightly. p < 0.05, unpaired Mann-Whitney\n    U-test\n  statistics:\n  - test: unpaired Mann-Whitney U-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 49 A1 and 31 mPFC neurons\n  expected:\n  - quantity: median latency, mPFC\n    value: 19.75\n    tolerance: 1.975\n    unit: ms\n  - quantity: median latency, A1\n    value: 16.75\n    tolerance: 1.675\n    unit: ms\n  criterion: Latency is the centre of the response window (Figure S5E legend; 6-2-evokmisc/main1.py\n    takes the mean of audresp_t1 and audresp_t2). Reproduced when both medians are within tolerance,\n    the mPFC median is the longer and the two-sided test gives p < 0.05.\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: fig6cd-baseline-evoked-correlation\n  statement: Across auditory-responsive neurons, the change in hold-period rate between blocks\n    correlates with the change in evoked rate, in A1 (43 neurons, trend slope close to 1) and in\n    mPFC (17 neurons), p < 0.001 in each.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    2; Figure 6C and 6D legends\n  quote: For A1 neurons (n = 43), increased anticipatory firing during one block significantly\n    correlated (p < 0.001) with increased evoked responses during the same block ... The slope of\n    the trend line is close to 1 ... but for auditory-responsive mPFC neurons (n = 17). Again, the\n    change in anticipatory activity across neurons correlated closely with the change in evoked\n    response (p < 0.001)\n  statistics:\n  - about: A1\n    test: linear regression\n    p: 0.001\n    p_relation: \"<\"\n    n: 43 neurons\n  - about: mPFC\n    test: linear regression\n    p: 0.001\n    p_relation: \"<\"\n    n: 17 neurons\n  expected:\n  - quantity: A1 neurons\n    value: 43\n    tolerance: 4.3\n  - quantity: mPFC neurons\n    value: 17\n    tolerance: 1.7\n  criterion: As 6-1-evoked/main0.py and 6-3-evokgain/main0.py, main2.py. Evoked counts in the response\n    window (M4) on hits of the eight non-cue stimulus pairs, nonrandom 0. Units are dropped when a\n    one-sample t-test of all their evoked rates against their hold rate (block-weighted) gives\n    p > 0.05. Evoked change is the stimulus-equalized difference, pitch discrimination minus\n    localization, of mean evoked rates (mean within each stimulus pair, then over pairs); baseline\n    change is the hold-rate difference of M3. Linear regression of evoked change on baseline change\n    (scipy linregress). Reproduced when both regressions are positive with p < 0.001 and the unit\n    counts are within tolerance. \"Close to 1\" is given no value; the A1 slope is reported with its\n    95% confidence interval, and taken to hold when that interval contains 1, a choice made here.\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: evoked-beyond-baseline-rare\n  statement: After subtracting each block's baseline, only 6 of 43 A1 neurons (14%) change their\n    evoked response significantly between blocks, 4 of the 6 from one rat (Rat 1), with higher\n    rates in pitch discrimination.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    2; Supplemental Experimental Procedures, Changes in magnitude of evoked response not explained by\n    changes in baseline\n  quote: we found very little evidence of any block-specific change in evoked firing rate ... We found\n    that a small population (6/43, or 14%) of A1 neurons increased their evoked response\n    significantly ... these neurons were predominantly (4/6) observed in a single animal (Rat 1)\n  expected:\n  - quantity: A1 neurons with a significant baseline-subtracted change\n    value: 6\n    tolerance: 0.6\n  - quantity: of these, from Rat 1 (CR12B)\n    value: 4\n    tolerance: 0.4\n  criterion: As 6-3-evokgain/main0.py with the block's hold rate subtracted from each trial's evoked\n    rate; trials drawn with replacement equally from each stimulus pair in each block (10000\n    draws, at least 5 trials per stimulus), two-sided bootstrap p of a zero difference, floored at\n    1/10000, Benjamini-Hochberg within region. Reproduced when the count is 5 to 7 of the A1 units\n    and at least half of them come from CR12B; partially reproduced when the count is within 3 to 9.\n    The tolerance of one neuron on 6 and 4 follows the 10% rule rounded to whole neurons.\n  data: with_labels\n  depends_on:\n  - fig6cd-baseline-evoked-correlation\n- id: fig6e-decoding\n  statement: Sound identity is decoded more accurately from A1 ensembles (21 ensembles, 49 neurons)\n    than from mPFC ensembles (17 ensembles, 31 neurons), but for neither sound nor region is\n    decoding better in one block than the other.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    3; Figure 6E legend\n  quote: It could be decoded significantly more accurately (p < 0.001 for the main effect of brain\n    region) using A1 responses (n = 21 ensembles of 49 neurons total) than using mPFC responses (n =\n    17 ensembles of 31 neurons total). However, for both sounds and both brain regions, the decoding\n    was not significantly more accurate during either pitch discrimination (red) or localization\n    (blue) trials (p > 0.05 for each pair of bars using a paired t test)\n  statistics:\n  - about: main effect of brain region\n    test: three-way ANOVA on brain region, target sound and block\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 A1 and 17 mPFC ensembles\n  - about: localization against pitch discrimination, each region and sound\n    test: paired t test\n    p: 0.05\n    p_relation: \">\"\n  expected:\n  - quantity: A1 ensembles\n    value: 21\n    tolerance: 2.1\n  - quantity: mPFC ensembles\n    value: 17\n    tolerance: 1.7\n  criterion: As 6-1-evoked/main1.py, main2.py, main4.py and the Supplement (Decoder analysis). An\n    ensemble is the responsive units (M4) of one region in one session. Per ensemble, block and sound\n    (noise burst side, warble pitch), a logistic regression (scikit-learn, class weights balanced)\n    on the trial-by-trial evoked counts of hits of the four stimulus pairs, scored in sample as the\n    fraction correct averaged over the two classes. A type II three-way ANOVA of the scores on\n    region, sound and block; paired t-tests between blocks per region and sound, adjusted by\n    Benjamini-Hochberg as the code does (the paper does not say). Reproduced when the region effect\n    has p < 0.001 with A1 higher and all four block comparisons give p > 0.05; the region claim and\n    the block claim (an absence, judged on the paired t-tests) are reported apart. Leave-one-out\n    scores are shown as a variant (Supplement).\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: figs5fg-tuning-vs-rule\n  statement: There is no correlation between a neuron's change in anticipatory activity and its\n    tuning for the noise burst or the warble, in A1 or mPFC.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    4; Figure S5F and S5G legends\n  quote: we did not observe any correlation between each neuron's change in anticipatory activity and\n    its tuning for the stimuli\n  criterion: A claim of absence. As 6-1-evoked/main2.py and main6.py and the Figure S5F legend.\n    Tuning is the single-unit decoding score (as fig6e-decoding) of the cue sound on cue-trial hits,\n    the noise burst from localization cue trials and the warble from pitch discrimination cue\n    trials; units with at least 25 cue trials in each block and at least 10 evoked spikes on them;\n    anticipatory change is log10 of the pitch discrimination over localization hold rate. Linear\n    regression of the change on each tuning, per region. Reproduced when all four regressions give\n    p > 0.05; the r values are reported.\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: figs5hi-stimulus-pairs\n  statement: No stimulus pair shows a greater change in evoked response between blocks than the\n    others, with or without baseline subtraction, and in absolute value.\n  source: Results, Changes in Baseline Activity Correlate with Changes in Evoked Activity, paragraph\n    4; Figure S5H and S5I legends\n  quote: A one-way Kruskal-Wallis test revealed no significant difference between the stimulus pairs\n    ... We found no significant difference from zero for any individual stimulus pair\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \">\"\n  - about: each stimulus pair against zero\n    test: Wilcoxon signed-rank test\n    p: 0.05\n    p_relation: \">\"\n    corrected: false discovery rate\n  criterion: A claim of absence, as 6-1-evoked/main5.py. Per responsive unit (M4) and stimulus pair,\n    the square root of the mean evoked rate on hits in pitch discrimination minus that in\n    localization; baseline-subtracted as the square root of the evoked rate minus the square root of\n    the block's hold rate. Kruskal-Wallis across the four pairs per region, raw and\n    baseline-subtracted, and on absolute values; Wilcoxon signed-rank against zero per pair with\n    Benjamini-Hochberg over the four pairs. Reproduced when no test gives p < 0.05; the p-values are\n    reported.\n  data: with_labels\n  depends_on:\n  - audresp-prevalence\n- id: figs2gh-s3gh-rt-mt\n  statement: Anticipatory firing rate does not correlate with reaction time or movement time; few\n    neurons correlate individually and the mean correlation does not differ from zero.\n  source: Discussion, The Potential Roles of Motor Planning and Posture, paragraph 3; Figures S2G,\n    S2H, S3G, S3H legends\n  quote: we did not observe any correlation between the anticipatory firing rate and the reaction or\n    movement time\n  statistics:\n  - about: mean of the correlation coefficients against zero\n    test: one-sample t-test\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence, as 3-4-RT_vs_hold/main.py and main3.py. Per unit and block, the\n    correlation (linear regression) between the square root of the hold count and reaction time\n    (center-port exit minus stimulus onset) on all hits, and movement time on go hits. The code takes\n    movement time as choice-port entry minus stimulus onset; the legend's \"time necessary for the\n    rat to move to the choice port\" can also be read as choice-port entry minus center-port exit,\n    shown as a variant. Reproduced when the one-sample t-test of the r values against zero gives\n    p > 0.05 in each region, block and measure; the count of individually significant units\n    (Benjamini-Hochberg) is reported.\n  data: with_labels\n- id: figs2i-head-angle\n  statement: The rat's head angle during the center poke differs between blocks by about 30\n    degrees, 26.9, 36.6 and 24.1 degrees in the three scored sessions.\n  source: Results, Potential Role of Posture, paragraph 1; Figure S2I legend; Supplemental\n    Experimental Procedures, Video analysis of preparatory head positioning\n  quote: differs by approximately 30 degrees between blocks ... The mean difference between blocks\n    was 26.9, 36.6, and 24.1 degrees in each of the three analyzed sessions\n  expected:\n  - quantity: head angle difference, session 1\n    value: 26.9\n    tolerance: 2.69\n    unit: degrees\n  - quantity: head angle difference, session 2\n    value: 36.6\n    tolerance: 3.66\n    unit: degrees\n  - quantity: head angle difference, session 3\n    value: 24.1\n    tolerance: 2.41\n    unit: degrees\n  criterion: From the ear positions in miscellaneous/vidtrack, head angle as vidtrack.vts_db2head_pos_df\n    computes it (in degrees), on the trials of the hold analysis (M2), as 3-5-vidtrack/main0.py and\n    main1.py. The paper does not say which value belongs to which session, so the three differences\n    of block means are compared to the three reported values as a set (sorted). Reproduced when all\n    three are within tolerance.\n- id: figs2kl-s3kl-fev\n  statement: For most rule-encoding neurons, block explains far more of the hold-period variance than\n    head angle; the median fraction explained by block is 94.1% in mPFC and 83.0% in A1 (head angle\n    5.9% and 17.0%), and only 3 of 16 mPFC and 1 A1 neuron are mostly explained by head angle.\n  source: Figures S2K, S2L, S3K, S3L legends; Supplemental Experimental Procedures, Video analysis,\n    Results\n  quote: \"Only three out of 16 bars are more than 50% black ... most of the variance (median: 94.1%)\n    is explained by block; the small amount that remains is explained by head angle (median: 5.9%)\n    ... Only one bar is more than 50% black ... most of the variance (median: 83.0%) is explained by\n    block; the small amount that remains is explained by head angle (median: 17.0%)\"\n  expected:\n  - quantity: median FEV of block, mPFC\n    value: 94.1\n    tolerance: 9.41\n    unit: percent\n  - quantity: median FEV of block, A1\n    value: 83.0\n    tolerance: 8.3\n    unit: percent\n  - quantity: median FEV of head angle, mPFC\n    value: 5.9\n    tolerance: 0.59\n    unit: percent\n  - quantity: median FEV of head angle, A1\n    value: 17.0\n    tolerance: 1.7\n    unit: percent\n  - quantity: mPFC neurons mostly explained by head angle\n    value: 3\n    tolerance: 0.3\n  criterion: Rule-encoding units of the three video sessions (16 mPFC, 8 A1); per unit a type II\n    ANOVA of the square root of hold counts on head angle plus block (3-5-vidtrack/main7.py); FEV of\n    a factor is its sum of squares over the sum for both. One A1 unit whose overall F-test gives\n    p > 0.05 is left out (Supplement, technical note). Reproduced when the medians are within\n    tolerance and the counts of units with head-angle FEV above 50% are 3 (mPFC) and 1 (A1).\n    Tolerances on the FEV medians are 10% of each value, so block and head angle are tested apart.\n  data: with_labels\n  depends_on:\n  - figs2i-head-angle\n  - fig3c-pfc-rule-encoding\n  - fig4c-a1-rule-encoding\n- id: posture-equalized-sign\n  statement: On posture-equalized trials the rule encoding persists; its population spread (0.471 in\n    mPFC, 0.318 in A1) exceeds that of shuffles (p < 0.005), and only 1 of 16 mPFC and 0 of 8 A1\n    cells switch preferred block (binomial p = 0.0005 and 0.008).\n  source: Results, Potential Role of Posture, paragraph 2; Figures S2M, S2O, S3M, S3O; Supplemental\n    Experimental Procedures, Posture equalization by trial selection\n  quote: The PRE was 0.471 in PFC and 0.318 in A1 on the posture-equalized trials; the fraction of\n    shuffles that yielded a greater PRE was <0.005 in both brain regions ... In fact we observed that\n    only 1/16 PFC cells and 0/8 A1 cells switch their preferred block after posture equalization.\n    The p-value (two-tailed binomial test) of this result is 0.008 for A1 and 0.0005 in PFC\n  statistics:\n  - about: PRE against shuffled block labels\n    test: shuffle test\n    p: 0.005\n    p_relation: \"<\"\n  - about: switches of preferred block, mPFC\n    test: two-tailed binomial test\n    p: 0.0005\n    n: 16 cells\n  - about: switches of preferred block, A1\n    test: two-tailed binomial test\n    p: 0.008\n    n: 8 cells\n  expected:\n  - quantity: PRE, mPFC\n    value: 0.471\n    tolerance: 0.0471\n  - quantity: PRE, A1\n    value: 0.318\n    tolerance: 0.0318\n  - quantity: mPFC cells switching\n    value: 1\n    tolerance: 0\n  - quantity: A1 cells switching\n    value: 0\n    tolerance: 0\n  criterion: As 3-5-vidtrack/main3.py to main5.py. Posture-equalized trials per session, the\n    localization trials with the highest head angles and the pitch discrimination trials with the\n    lowest, the largest equal number for which the localization mean stays above the pitch\n    discrimination mean, less one. Rule encoding is log10 of the pitch discrimination over\n    localization mean count; PRE is the scaled median absolute deviation (statsmodels stand_mad)\n    over units; 10000 shuffles of block labels on the posture-equalized trials. Reproduced when the\n    PREs are within tolerance with shuffle p < 0.005 and the switch counts match. Switch counts are\n    whole cells and taken exactly.\n  data: with_labels\n  depends_on:\n  - figs2kl-s3kl-fev\n- id: posture-equalized-magnitude\n  statement: The mean magnitude of rule encoding is not significantly altered on posture-equalized\n    trials, in mPFC or A1.\n  source: Figures S2N and S3N legends; Supplemental Experimental Procedures, Posture equalization by\n    trial selection\n  quote: we found that the mean magnitude of rule-encoding was not significantly altered by postural\n    equalization\n  statistics:\n  - test: paired Mann-Whitney U-test\n    p: 0.05\n    p_relation: \">\"\n    n: 16 mPFC and 8 A1 cells\n  criterion: A claim of absence. Absolute rule encoding (as posture-equalized-sign) on\n    posture-equalized and on the other trials, compared per region with the Wilcoxon signed-rank\n    test (M5). Reproduced when p > 0.05 in each region; the change is reported.\n  data: with_labels\n  depends_on:\n  - posture-equalized-sign\n- id: fig7-disruption-by-block\n  statement: Electrical disruption of mPFC impairs performance; across sessions the impairment is\n    significant in pitch discrimination for all three rats and in localization for two of three.\n  source: Results, Disruption of mPFC Significantly Impairs Task Performance, paragraph 2; Figure 7A\n  quote: This impairment was significant across sessions (p < 0.05, binomial test on the number of\n    impaired sessions) during pitch discrimination for all (three of three) rats and during\n    localization for most (two of three) rats\n  statistics:\n  - test: binomial test on the number of impaired sessions\n    p: 0.05\n    p_relation: \"<\"\n    n: Z1 6, Z2 8 and Z3 8 sessions\n  expected:\n  - quantity: sessions, Z1\n    value: 6\n    tolerance: 0\n  - quantity: sessions, Z2\n    value: 8\n    tolerance: 0\n  - quantity: sessions, Z3\n    value: 8\n    tolerance: 0\n  criterion: As 7-1-zap/zap.py and main1.py on miscellaneous/zap/TI_d. Per session, performance\n    (fraction of hits) on disruption and control trials of block 2 and of block 4, munged trials\n    dropped (the code does not drop nonrandom trials; dropping them is a variant). Per rat, a\n    two-sided binomial test of the number of sessions with control above disruption performance.\n    Reproduced when pitch discrimination is significant for all three rats and localization for two;\n    partially reproduced when at least four of the six rat and block tests are. Session counts are\n    whole sessions and taken exactly.\n- id: fig7c-disruption-nogo\n  statement: Disruption impairs nogo trials in particular; every rat is significantly impaired on\n    nogo trials in one block or the other, and Z2 also on localization go trials.\n  source: Results, Disruption of mPFC Significantly Impairs Task Performance, paragraph 2; Figure 7C\n    legend\n  quote: All rats were significantly impaired on nogo trials during one block or the other. One rat\n    (Z2) also showed a significant impairment on localization go trials\n  statistics:\n  - test: binomial test on number of impaired sessions\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As fig7-disruption-by-block, split by go and nogo in each block (zap.py\n    compute_by_block_and_gonogo). Reproduced when each rat has a significant nogo impairment in at\n    least one block and, among go trial types, only Z2 localization go is significant.\n  depends_on:\n  - fig7-disruption-by-block\n- id: figs1bc-catch\n  statement: Rats perform as well when the distractor is replaced by a novel neutral sound as on\n    standard trials, so they select the target and do not memorize the four stimulus pairs.\n  source: Figure S1B and S1C legends\n  quote: The rats perform just as well on catch trials as on standard trials (Fisher's Exact Test on\n    the trial outcomes, p > 0.05 in all cases)\n  statistics:\n  - test: Fisher's Exact Test\n    p: 0.05\n    p_relation: \">\"\n    n: 2 rats, 4 trial types each\n  criterion: A claim of absence, as 2-1-behavres/main05.py on miscellaneous/catch_trial_task. For each\n    rat and each catch stimulus, hits and trials on it against the two standard stimuli with the same\n    target pooled; two-sided Fisher's exact test. Reproduced when all eight tests give p > 0.05; the\n    performances are reported.\n- id: fig8-model\n  statement: In the network model with 320 neurons, a task signal alone lets the network perform\n    above 80% correct with a sensory signal-to-noise ratio as low as 0.0625, and 100% at an SNR of\n    0.25 for virtually any positive task signal.\n  source: Results, A Simulated Network Model, paragraph 3; Figure 8B legend\n  quote: With 320 neurons, the network performs above 80% correct even with a signal-to-noise ratio\n    (SNR) as low as 0.0625 ... At the highest SNR of 0.25 (darkest trace), the model produces 100%\n    correct responses for virtually any positive task switch signal\n  expected:\n  - quantity: SNR at which the 320-neuron network exceeds 80% correct\n    value: 0.0625\n    tolerance: 0\n  criterion: From the deposited simulation results (miscellaneous/model, simulation_resdf and\n    simulation_params.pickle), as 8-1-model/main1.py; performance is score1b or score2b over\n    NT_TEST for the task whose population receives the signal. SNR is the sensory gain over the\n    noise level; the Supplement calls the noise its strength and Figure S7 its variance, so both\n    gain/noise and gain/sqrt(noise) are named, the one that yields the printed SNR grid (powers of\n    2 from 2^-6 to 2^-2) taken. Reproduced when for N = 320 and SNR 0.0625 some positive task signal\n    gives above 80% correct in both tasks, and at SNR 0.25 performance is at least 99% over most\n    positive task signals. The SNR is a grid value and taken exactly.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml paper/10.1016-j.neuron.2014.04.031.txt; grep -nP "^\s+(statement|criterion|source|quote|inferred|quantity|n|about|test): [^\"].*: " claims/crcns-pfc-1/*.yaml | head; grep -n "—\|rather" claims/crcns-pfc-1/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml && python3 - "$f" <<'EOF'
import sys,re
p=sys.argv[1]
s=open(p).read()
s=s.replace("prestimulus. Thus, the majority of rule-encoding neurons developed this property","prestimulus. Thus, the majority of ... neurons developed this property")
s=s.replace("""prestimulus; in PFC, the median was 0.625 s prestimulus. Thus, the majority of rule-encoding
    neurons developed""","""prestimulus; in PFC, the median was 0.625 s prestimulus. Thus, the majority of ...
    neurons developed""")
open(p,'w').write(s)
import yaml
d=yaml.safe_load(s)
for c in d['claims']:
    for k,v in c.items():
        if isinstance(v,str) and ': ' in v: print(c['id'],k)
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2014.04.031.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
32 32 21 27 32 23
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
?? claims/crcns-pfc-1/
?? scripts
```

**Agent**

I wrote `claims/crcns-pfc-1/10.1016-j.neuron.2014.04.031.yaml`, and the quote checker passes on it with 0 problems. Nothing is committed.

**Text read:** the version of record (Neuron 82, 1157–1170) with its Supplemental Information: Figures S1 to S7 legends and the Supplemental Experimental Procedures. Nothing the claims needed was missing, so I never opened the PDF. I read the data descriptor only to see what the data set holds.

**Code read:** github.com/cxrodgers/Rodgers2014 at commit 390b608. It has one folder of scripts per figure, the helper modules, and `metadata/unit_db.csv`. That table holds each unit's include flag, region, auditory-response class and response window. The scripts that set those columns are not in the repository. So every single-unit claim takes its units from that table and is marked `data: with_labels`. Recomputing the auditory-response classification as the Supplement describes is named as a variant.

**Counts:**
- 32 claims, and all 32 have quotes (none needed `inferred`).
- 21 claims carry 27 statistics entries.
- All 32 have a criterion; 23 have expected values.
- 8 are claims of absence, each judged on the paper's own test.
- Areas covered: behaviour, rule encoding, error trials, time course, evoked responses, decoding, posture, mPFC disruption, catch trials and the model.

**Details the paper leaves open, with the readings named:**
- **Benjamini-Hochberg adjustment for rule encoding:** (a) pooled over both regions, as the code does; (b) per region.
- **Auditory-responsive units:** (a) the code table's classes and windows; (b) recomputed per the Supplement. For (b) the trials used, the per-bin threshold, any correction and how atypical units were judged are open.
- **Which 55 sessions the "4 of 55 failed" refers to:** (a) the code table's 55, all marked include; (b) a set before that cut. Also open is which trials count toward the median of 698 per session.
- **Intertrial interval:** between stimulus onsets, or between center-poke starts.
- **Single-unit onset window:** the Results say ±3 s and the code uses ±5 s. I took the Results as the main reading and the code as a variant.
- **Figure 5D (go/nogo after leaving the center port):** the paper gives no test or window. Readings are a 0–3 s mean, or per-bin t-tests as in Figure 5C.
- **"Slope close to 1" (Figure 6C):** no value is given. I judged it by whether the slope's 95% confidence interval contains 1, and the file marks this as my own choice.
- **Movement time:** choice-port entry minus stimulus onset (the code), or minus center-port exit (the legend).
- **Model signal-to-noise ratio:** gain over noise, or over the square root of noise. The Supplement and Figure S7 disagree on whether the noise figure is a strength or a variance.
- **Head-angle differences:** which of 26.9, 36.6 and 24.1° belongs to which session is not said, so they are compared as a set.
- **Disruption analysis:** the code keeps the trials flagged as non-random; dropping them is a variant.
- **Smaller points:** Figure 4A and 4B give the same session's trial counts with the blocks swapped, so the counts are compared as a pair. The paired t-tests in Figure 6E are adjusted only in the code.

**Missing from the paper:** nothing a claim needed. The only gaps are the unit-selection and response-classification steps, whose results exist only as the code's table.

## End of run

46 turns, 8 minutes, $4.27 at API prices, result: success.
