# gable-2026 · claims · run 45032248354

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; wc -l claims/fouke-2025.yaml; cat papers/datasets/gable-2026.yaml 2>/dev/null; grep -n gable papers/keys.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 180 paper/10.1523-jneurosci.0974-26.2026.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 400
}
```

```
File content (28265 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 300
}
```

```
1	DOI: 10.1523/jneurosci.0974-26.2026
2	Version: version of record
3	Source: find_reuse cache
4	Stored: 2026-11-10
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc J Neurosci J Neurosci 2110 jneurosci 8102140 J. Neurosci The Journal of Neuroscience 0270-6474 1529-2401 Society for Neuroscience PMC13612898 PMC13612898.1 13612898 13612898 
8	42637560 10.1523/JNEUROSCI.0974-26.2026 jneuro-46-e0974262026 1 Research Articles Systems/Circuits Tuft Dendrite Spikes Are Accompanied by Selective Input From Distinct Functional 
9	Networks Gable Jacob https://orcid.org/0000-0002-4336-6585 Newman Zachary L. Young Sarah Scheib Jackson Bliese Savannah Miller Nicole Kerlin Aaron Department of Neuroscience, 
10	University of Minnesota , Minneapolis, MN 55455 Author Contributions: J.G. and A.K. designed research; J.G., S.Y., J.S., S.B., and N.M. performed research; J.G., Z.L.N., and A.K. 
11	analyzed data; J.G., Z.L.N., and A.K. edited the paper; J.G. wrote the paper. This work was supported with funding from the Whitehall Foundation (Grant 2020-05-71), NINDS 
12	R01NS127902, as well as the resources and staff at the University Imaging Centers (UIC; RRID: SCR_020997) and Minnesota Supercomputing Institute (MSI) at the University of 
13	Minnesota. Research reported was additionally supported by the University of Minnesota’s MnDRIVE (Minnesota’s Discovery, Research and Innovation Economy) Initiative. The authors 
14	declare no competing financial interests. Correspondence should be addressed to Aaron Kerlin at [removed: an e-mail address] . This paper contains supplemental material available at: 
15	https://doi.org/10.1523/JNEUROSCI.0974-26.2026 24 8 2026 23 9 2026 46 38 522249 e0974262026 10 6 2026 27 7 2026 7 8 2026 23 09 2026 26 09 2026 03 10 2026 Copyright © 2026 Gable et 
16	al. 2026 https://creativecommons.org/licenses/by/4.0/ This is an open-access article distributed under the terms of the Creative Commons Attribution 4.0 International 
[... 284 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 301,
 "limit": 250
}
```

```
301	TSA aligned to tuft spike onset across coupling groups ( Fig. 3 E , F ). SC synapses exhibited a higher rate of abrupt increases in activity at tuft spike onset (window: −50 to 
302	+150 ms) than the other coupling groups (SC SD vs WC SD : MD = 1.1 Hz, p = 0.002; SC SD vs NC SD : MD = 1.0 Hz, p = 0.02). Furthermore, we observed no indication that this 
303	observation was sex specific ( Table 6 ). The differences between coupler groups were far less pronounced using Θ (Δ F / F 0 ) activity, suggesting highly coupled synapses have 
304	more trial-to-trial precise input timing with respect to tuft spike onsets ( Fig. S3 G ). Interestingly, this spike-associated increase in SC activity was still highly 
305	dendrite-specific (SC SD vs SC OD : MD = 1.5 Hz, p = 6 × 10 −4 ). This suggests that although SC synapses are relatively strongly correlated with each other (same vs different 
306	coupling range MD = 0.06 ρ , p = 7.0 × 10 −3 ; Fig. 3 D ), at the onset of the tuft spikes the activity of SC synapses is driven along a dendrite-specific dimension in the 
307	activity space, and this dimension is distinct from the dimension that best captures their population-wide coactivity. Although there was a weak tendency for synapses of the same 
308	coupling group to cluster on the same dendrite segment, it was not statistically significant (same vs across dendrite MD = −0.053 a.u., p = 0.19; Fig. S2 C ), suggesting that SC 
309	synapses were not strongly targeted to particular dendrite segments. Spike-associated activity occurs along distinct dimensions partitioned by task-selectivity and population 
310	coupling After discovering a relationship between the activity of synapses at the onset of tuft spikes and the population coupling of synapses, we sought to determine whether 
311	different coupling groups encoded distinct task-variables. Trial-averaged Θ (Δ F / F 0 ) timecourses revealed clear qualitative differences in the timing of activity between 
312	coupler groups ( F
[... 238 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 551,
 "limit": 250
}
```

```
551	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
552	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
553	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
554	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
555	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
556	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
557	https://github.com/kerlin-lab/Gable_2026
558	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
559	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
560	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
561	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
562	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
563	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
564	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
565	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
566	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
567	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
568	https://www.jneurosci.org/content/jneuro/suppl/2026/08/20/JNEUROSCI.0974-26.2026.DC1/JN-RM-0974-26-suppl.pdf
569	https://www.jneurosci.org/cont
[... 231 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 801,
 "limit": 300
}
```

```
801	
802	[96] 10.1038/ncomms11380
803	
804	[97] 10.1038/nature02116
805	
806	[98] 10.1038/nn.4323
807	
808	[99] 10.1126/science.ads4706
809	
810	[100] Wu X , Lee BH , Park P , Wong-Campos JD , Xu J , Plutkis SE , Lavis LD , Cohen AE (2026) “A Dendrite-Resolved, in Vivo Transfer Function From Spike Patterns to Dendritic 
811	Ca2+.” bioRxiv, pp 2026–01. 10.64898/2026.01.18.700189
812	
813	[101] Xiao K , Li Y , Sullivan BJ , Li G , Magee JC (2025) “Rapid Neocortical Network Modifications Via Dendritic Plateau Potential Induced Plasticity.” bioRxiv, pp 2025–11. 
814	10.1101/2025.11.19.689338
815	
816	[102] 10.1038/nature11601
817	
818	[103] Yaeger CE , Soto-Albors RM , Liu W , Beltramini A , Harnett MT (2025) “Plateau Potentials Are Instructive Signals for Behavioral Timescale Synaptic Plasticity in the 
819	Neocortex.” bioRxiv, pp 2025–11. 10.1101/2025.11.07.687250
820	
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1100,1546p $TMPDIR/p.txt | grep -v '^[-0-9. ]*$' | tr '\n' ' ' | fold -s -w 200
```

```
grep: (standard input): binary file matches
```

**Agent calls Bash**

```bash
sed -n 1100,1546p $TMPDIR/p.txt | grep -av '^[-0-9. ]*$' | tr '\n' ' ' | fold -s -w 200
```

```
iGluSnFR3   (  F/F0)TSA (Hz) Spike Dendrite, Multi-Branch Other Dendrite, Multi-Branch Pre Post Onset Mean iGluSnFR3   (  F/F0)TSA (Hz) n.s. n.s.  F/F0 > 0.3  F/F0 > 1.0 Pre Post Onset Mean iGluSnFR3   
(  F/F0)TSA (Hz) n.s. n.s. Unblanked Excluded Pre Post Onset Window   (  F/F0)TSA (Hz) ** Spike Dendrite, Multi-Branch Other Dendrite, Multi-Branch Time from GO (ms) d(|  x|+|  y|)/dt (μm/s) 
Unblanked Motion Excluded Tuft Spike Amplitude (ΔF/F0) Proportion A B C Within Across Dendrite Delta Coupling 0–5 5–10 10–15 15–20 20–30 30–50 50+ Pair Distance (m)  (dF/dt)TSA Noise Correlation (ρ) 
Within Dendrite Across Dendrite 0–5 5–10 10–15 15–20 20–30 30–50 50+ Pair Distance (μm) Θ(dF/dt) Signal Correlation (ρ) Within Dendrite Across Dendrite A B C D E F G 0-14% 42-57% 85-100% Coupling 
Rank Bin Pairwise Correlation (  ) *** n.s. n.s. n.s. *** *** *** Within Bin Across Bin Coupling Rank (All Sessions) Coupling Rank (Within Session) R2 = 0.68 Coupling Rank (All Data) Coupling Rank 
(Motion Blanked) R2 = 0.98 Coupling Rank (All Data) Coupling Rank (Early Activity Blanked) R2 = 0.89 Coupling Rank (All Data) Mean Synapse Amplitude (  F/F0) R2 = 0.03 Synapses in Population Sum 
Coupling Rank (All Data) R2 = 0.01 Time from Spike Onset (ms) iGluSnFR3   (  F/F0) (Hz) Strong Spike Other Time from Spike Onset (ms) Weak Spike Other Time from Spike Onset (ms) Non-Positive Spike 
Other A B Silicon Probe ALM Li, Nuo, et al., 2015 Nature 0-14% 42-57% 85-100% Coupling Rank Bin Pairwise Correlation (  ) *** n.s. n.s. n.s. *** *** *** Within Bin Across Bin B D C A Synapse 1 
Synapse 2 Synapse 3 Synapse n Correct Left (CL) Correct Right (CR) Time from GO (s) Projection (a.u.) GO Mode CR CL Time from GO (s) Response Direction CR CL Time from GO (s) Outcome Direction 
Correct (C) Incorrect (I) Time from GO (s)  (  F/F0) (Hz) Correct Strong (SC) Weak (WC) Nonpositive (NC) Time from GO (s) Incorrect SC WC NC Time from GO (s) Correct Right SC WC NC Time from GO (s) 
Correct Lef
[... 1 more lines not kept]
```

**Agent**

Paper text, Methods and supplement are all present. DANDI:000010 (Li et al. 2015 ALM silicon probe) is only the Fig. S4 / Table 5 reanalysis. Now reading the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/kerlin-lab/Gable_2026 && cd Gable_2026 && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
688e662767ed32b6ea60a2827c3483408edf6deb Tue Jun 9 21:50:21 2026 -0500
./LICENSE
./Figures/Figure4.ipynb
./Figures/Figure1.ipynb
./Figures/FigureS2.ipynb
./Figures/FigureS3.ipynb
./Figures/sled_glutamate_functions.py
./Figures/FigureS4.ipynb
./Figures/FigureS5.ipynb
./Figures/Figure3.ipynb
./Figures/Figure5.ipynb
./Figures/Figure2.ipynb
./Figures/FigureS1.ipynb
./README.md
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026 && cat README.md && python - <<'EOF'
import json
nb=json.load(open('Figures/FigureS4.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"--- cell {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('OUT:', ''.join(o['text'])[:1500])
        elif 'data' in o and 'text/plain' in o['data']: print('OUT:', ''.join(o['data']['text/plain'])[:800])
EOF
```

```
# Gable_2026
Data and code repository for the manuscript Gable et al., 2026 Tuft dendrite spikes are accompanied by selective input from distinct functional networks
--- cell 0 [code]
import sys
import os
import copy
import importlib
import numpy as np
import pickle
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="scipy")
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ["Arial"]
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['axes.unicode_minus'] = False
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="scipy")
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026 && python - <<'EOF'
import json
nb=json.load(open('Figures/FigureS4.ipynb'))
c=nb['cells'][4]
for o in c.get('outputs',[]):
    if 'text' in o: print(''.join(o['text']))
EOF
grep -n "^def \|^    def " Figures/sled_glutamate_functions.py | wc -l; grep -n "def calculate_ephys_population_coupling\|def corrXCoupling_ephys_v3\|def _boot\|ephys" Figures/sled_glutamate_functions.py | head -40
```

```
========================================================================
Paired (session-resampled) bootstrap of ephys synchy by coupling cluster
  function: corrXCoupling_ephys_v3
========================================================================
  Input                  : 7 cluster(s) (bins); within each session every
                           neuron pair is bucketed as same- or diff-coupling.
  Resampling (per bin)   : each group resampled INDEPENDENTLY (own session draw,
                           groups NOT paired); difference = same - diff index-wise.
                           A draw is kept only if the pooled group has >= the
                           observed number of pairs (matches the original rule).
  Iterations             : 10000 accepted draws per group per cluster
  Aggregation (bootStat) : np.nanmean
  Reported statistic     : bootStat(same) - bootStat(diff), tested against 0
  Significance label     : two-sided percentile test, Bonferroni-corrected for 7
                           comparisons (*, **, ***).
  Bootstrap p-values     : (+1)-corrected proportion past 0; two-sided = 2 x smaller tail.
  One-sided alternative  : 'greater'  (diff = same - diff)
  Multiple comparisons   : 'holm' correction across the 7 cluster(s)
                           (alpha=0.05); one- and two-sided corrected separately.
  Execution              : parallel (n_jobs=100)
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026/Figures && sed -n 9703,9800p sled_glutamate_functions.py; echo ======; sed -n 10478,10512p sled_glutamate_functions.py; echo =====; sed -n 10640,10760p sled_glutamate_functions.py
```

```
def calculate_ephys_population_coupling(data, n_slices):
    population_coupling = []

    for sess in range(len(data)):

        population_coupling_sess = []

        population_sum = np.sum(data[sess], axis=0).flatten()
        
        for neuron in tqdm(range(data[sess].shape[0]), desc=f"Calculating sess {sess} population coupling"):
            
            neuron_activity = data[sess][neuron, :, :].flatten()
            
            adjusted_pop_sum = population_sum - neuron_activity

            pop_coupling_neuron = np.corrcoef(adjusted_pop_sum, neuron_activity)[0, 1]

            population_coupling_sess.append(pop_coupling_neuron)
            
        population_coupling_sess = np.array(population_coupling_sess)
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026/Figures && grep -n "def _spont_group_boot_iter" -A 30 sled_glutamate_functions.py; grep -n -i "nwb\|dandi\|pynwb\|0\.5 *Hz\|firing_rate\|photostim\|Sim1\|Tlx" sled_glutamate_functions.py *.ipynb | head; grep -n -i "gaussian_filter1d\|def.*tsa\|trial_specific\|TSA" sled_glutamate_functions.py | head -30
```

```
<persisted-output>
Output too large (281.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e8514a03-dab3-45fd-ac2c-9120c08a6008/tool-results/bpcg3qe9i.txt

Preview (first 2KB):
9976:def _spont_group_boot_iter(synchy, n_obs, num_sess, stat_fn):
9977-    # ----- ONE accepted bootstrap iteration for a SINGLE group of a single cluster -----
9978-    # Independent of the other group: draw `num_sess` session indices WITH replacement, pool
9979-    # this group's synchy values across the drawn sessions, and reduce with `stat_fn`. Mirrors
9980-    # the acceptance rule of the original corrXCoupling_spontaneous: a draw is only kept once
9981-    # the pooled group holds at least as many pairs as the observed data (n_obs); otherwise a
9982-    # fresh draw is taken. Returns one stat for this iteration.
9983-    while True:
9984-        sess_indices = np.random.choice(num_sess, num_sess)
9985-        pool = []
9986-        for sess in sess_indices:
9987-            pool.extend(synchy[sess].tolist())
9988-        if len(pool) >= n_obs:
9989-            return stat_fn(pool) if len(pool) else np.nan
9990-
9991-
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026/Figures && grep -n -i -o ".\{0,40\}\(nwb\|dandi\|photostim\|Sim1\|Tlx\).\{0,40\}" sled_glutamate_functions.py | head; for f in *.ipynb; do python -c "
import json,sys
nb=json.load(open('$f'))
s=''.join(''.join(c['source']) for c in nb['cells'])
import re
for k in ['nwb','dandi','ephys','firing']:
    if k in s.lower(): print('$f',k)
"; done
```

```
FigureS4.ipynb ephys
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -l "relation: reuses" papers/datasets/*.yaml | head -5; grep -rn "data_missing\|blocked" claims/*.yaml | head -10; grep -n "^  [a-z_]*:" claims/*.yaml | awk -F: '{print $3}' | sort | uniq -c | sort -rn | head -30
```

```
papers/datasets/alasfour-2024.yaml
papers/datasets/burman-2023.yaml
papers/datasets/cambrainha-2025.yaml
papers/datasets/clark-2026.yaml
papers/datasets/du-2026.yaml
claims/armstrong-2026.yaml:209:    in the notes. When the unit readings disagree the claim is blocked as methods_underspecified.
claims/armstrong-2026.yaml:438:    readings; when readings disagree the claim is blocked as methods_underspecified.
claims/armstrong-2026.yaml:467:    and in sitting trials epoch 2 exceeds epoch 4, in animal 480, under either reading; when readings disagree the claim is blocked as methods_underspecified.
claims/armstrong-2026.yaml:486:    above 1 in a segment after 0.4 s; when readings disagree the claim is blocked as
claims/armstrong-2026.yaml:511:    is blocked as methods_underspecified.
claims/armstrong-2026.yaml:841:    When the measure readings give different outcomes the claim is blocked as
claims/athalye-2023.yaml:1128:    within 0.5 percentage points of those reported. Needs the PPF update or its parameters; blocked
claims/bakalar-2023.yaml:409:    of (1) to (4) give different outcomes, the claim is blocked as methods_underspecified with
claims/bech-2026.yaml:362:    context, and is otherwise blocked as methods_underspecified. Reproduced when both parts hold,
claims/bech-2026.yaml:645:    otherwise blocked as methods_underspecified.
   9911   statement
   9911   source
   9737   quote
   9533   criterion
   4452   depends_on
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/du-2026.yaml; head -60 claims/du-2026.yaml; grep -n "data: \|where:" claims/du-2026.yaml | head -20; ls tools/ | head -30; ls docs/
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.64898/2026.08.04.742876
title: A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding
datasets:
- archive: dandi
  id: '001201'
  relation: reuses
- archive: dandi
  id: 000129
  relation: reuses
# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (version pilot-18, Reader).
#
# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "data\b\|'data'\|elsewhere\|with_labels\|where\|allowed\|KEYS\|keys" tools/claims_check.py | head -50; grep -rn -B2 -A3 "where: .*\(ot public\|not deposited\|not shared\|unpublished\|not available\)" claims/*.yaml | head -30
```

```
18:import unicodedata
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
claims/berg-2020.yaml-921-    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).
claims/berg-2020.yaml-922-  data: elsewhere
claims/berg-2020.yaml:923:  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
claims/berg-2020.yaml-924-    NEFH expression from the Allen Brain Map RNA-seq data, not pinned
claims/berg-2020.yaml-925-  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
claims/berg-2020.yaml-926-checks:
--
claims/jarzebowski-2026.yaml-141-    arrives to the L5 ET 15–20 ms delayed
claims/jarzebowski-2026.yaml-142-  data: elsewhere
claims/jarzebowski-2026.yaml:143:  where: the paper's two-compartment LIF model, specified in the Methods; code not public on
claims/jarzebowski-2026.yaml-144-    2026-11-21
claims/jarzebowski-2026.yaml-145-  expected:
claims/jarzebowski-2026.yaml-146-  - quantity: delay of the gated release spike
--
claims/jarzebowski-2026.yaml-163-    resulting in no spiking.
claims/jarzebowski-2026.yaml-164-  data: elsewhere
claims/jarzebowski-2026.yaml:165:  where: the paper's two-compartment LIF model, specified in the Methods; code not public on
claims/jarzebowski-2026.yaml-166-    2026-11-21
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l tools/claims_check.py; sed -n 1,80p tools/claims_check.py; head -45 claims/jarzebowski-2026.yaml; tail -30 claims/jarzebowski-2026.yaml
```

```
112 tools/claims_check.py
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:12000])"
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000010/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d['most_recent_published_version'] if False else d.get(k) for k in ['identifier']},indent=0)); v=d.get('most_recent_published_version') or d.get('draft_version'); print(v)"; curl -s "https://api.dandiarchive.org/api/dandisets/000010/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 80,112p tools/claims_check.py
```

```
texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
    problems = 0
    for err in schema("claims").iter_errors(_plain(doc)):
        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
        problems += 1
    quotes = values = 0
    for c in doc.get("claims", []):
        if c.get("quote"):
            quotes += 1
            if not quote_found(c["quote"], texts):
                print("QUOTE NOT FOUND", c["id"])
                problems += 1
        for s in c.get("statistics", []):
            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
                if v is None:
                    continue
                values += 1
                if not any(f in t for f in printed_forms(v) for t in texts):
                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
                    problems += 1
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Gable_2026/Figures && for f in Figure2 Figure3 Figure4 Figure5 FigureS1 FigureS2 FigureS3; do python - "$f" <<'EOF'
import json,sys,re
f=sys.argv[1]
nb=json.load(open(f+'.ipynb'))
s='\n'.join(''.join(c['source']) for c in nb['cells'])
hits=set(re.findall(r"(?:n_slices|alternative|nBoot|pre_window|post_window|window\w*|thresh\w*|percentile\w*)\s*=\s*[^\n]{0,40}",s))
print(f, sorted(hits)[:15])
EOF
done
```

```
Figure2 ['threshDff = pickle.load(f)', 'thresh_frames=15', 'thresh_max=30', 'threshdff = \\', 'threshdff = sled_glutamate_functions.autocorrelation', 'thresholds_c2 = copy.deepcopy(activity_thresholds_c2)', 'thresholds_c2 = pickle.load(f)', 'window_colors = ((0.2, 0.4, 0.8), (0.85, 0.35, 0.1))', 'window_colors=window_colors, bar_width=bar_width,bar_g', "window_labels = ('Pre', 'Post')", 'window_labels=window_labels, set_labels=set_labels,', 'window_stats = \\', 'window_stats = sled_glutamate_functions.post_hoc_dspike', 'window_stats= \\', 'window_stats= sled_glutamate_functions.post_hoc_dspike']
Figure3 ["alternative='greater',", 'nBoot = 10000', 'percentile = 20', 'percentile = 80', 'percentiles = sled_glutamate_functions.percentiles_unw', 'thresh_frames=15', 'thresh_max=30', 'threshold = 0.5', 'threshold = 10', 'threshold = 2.5', 'threshold = 20', 'threshold = 80', 'threshold=across_branch_corr_threshold, same_branc', 'threshold=across_branch_distance_threshold, same_b', 'threshold=same_branch_corr_threshold,']
Figure4 ['nBoot = 10000', 'nBoot=nBoot, resample_unit=resample_unit, sess']
Figure5 ['thresh_frames=15', 'thresh_max=30', 'thresholds_c2 = copy.deepcopy(activity_thresholds_c2)', 'thresholds_c2 = pickle.load(f)', 'window_colors= ((0, 0, 0), (0.5, 0.5, 0.5))', 'window_colors=window_colors, bar_width=bar_width,bar_g', "window_labels= ('SD', 'OD')", "window_labels= ('Spike', 'Other')", 'window_labels=window_labels, set_labels=set_labels,', 'window_stats = sled_glutamate_functions.merge_window_st', 'window_stats_list = [high_go_window_stats, med_go_window_sta', 'window_stats_list = [high_out_window_stats, med_out_window_s', 'windows = [(71, 107)]', 'windows = [(pre_frames-9,pre_frames+27)]', 'windows = [(pre_frames-int(40/5.738),pre_frames+in']
FigureS1 ['percentile_threshold=85', 'thresh = 0.4', 'thresh = 0.7', 'thresh1 = np.nanpercentile(-neg,99.9)', 'thresh1 = thresholds_c2[sess][dend]', 'thresh2 = np.nanpercentile(-neg,99.9)', 'thresh2 = thresholds_c2[sess]
[... 3 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/gable-2026.yaml",
 "content": "# Claims for Gable, Newman, Young, Scheib, Bliese, Miller & Kerlin (2026), \"Tuft Dendrite Spikes\n# Are Accompanied by Selective Input From Distinct Functional Networks\", J Neurosci 46(38)\n# e0974262026, doi:10.1523/jneurosci.0974-26.2026, tested on DANDI:000010, which the paper reuses.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-22,\n# protocol pilot-18 as stated in docs/protocol.md, Reader section.\n#\n# Text read. The version of record (PMC13612898, open access, CC BY) in\n# paper/10.1523-jneurosci.0974-26.2026.txt: abstract, Significance Statement, Introduction,\n# Materials and Methods, Results with the legends of Figures 1 to 5 and Tables 1 to 8, Discussion.\n# The same file holds the supplement (JN-RM-0974-26-suppl.pdf, legends of Figures S1 to S5 and the\n# panel text); the PDF of the supplement is under paper/ and was not needed. The supplement legends\n# refer to \"Table 6\", \"Table 7\" and \"Table 8\" where the main text puts the matching statistics in\n# Tables 2, 4 and 5; the main-text numbering is used here.\n#\n# Code read. github.com/kerlin-lab/Gable_2026, commit 688e662767ed32b6ea60a2827c3483408edf6deb\n# (2026-06-09), named in Code and data availability. It holds one notebook per figure (Figures 1 to\n# 5, S1 to S5) and a function library, Figures/sled_glutamate_functions.py. The notebooks load\n# pickled, already processed data from the lab's own servers; the repository holds no data. For\n# Figure S4 it holds the coupling and statistics code (FigureS4.ipynb; functions\n# calculate_ephys_population_coupling, _ephys_cluster_synchy, corrXCoupling_ephys_v3,\n# _spont_group_boot_iter) but not the step that builds its input (ephys_secondaryAna.PKL, one\n# neurons x trials x time-bins array per session) from the DANDI files: unit and session\n# selection, trial selection, binning, smoothing and trial-specific activity are not in the code.\n# The notebook's printed outputs show 20 sessions of 18 to 25 neurons each, and same-range and\n# different-range pair counts per bin summing to 771 and 6,586 (Table 5 prints 753 and 6,586).\n# These outputs were not used to set any expected value.\n#\n# The datasets. DANDI:000010, \"A motor cortex circuit for motor planning and movement\" (Li, Chen,\n# Guo, Gerfen & Svoboda 2015; published version 0.220126.1905), extracellular recordings from\n# mouse ALM (and thalamus) and calcium imaging during a delayed response task. The paper cites it\n# as Li et al. 2015b and reanalyses its silicon-probe ALM recordings for Figure S4 and Table 5\n# only. Those are the claims this attempt can test (figs4-*). Every other finding rests on the\n# paper's own two-photon imaging, which is not in DANDI:000010 and is not deposited in any public\n# archive the paper or the code names: those claims are data elsewhere, recorded as not public.\n#\n# Data the paper used, as it reports it.\n# - Own imaging (Methods, Mice and surgeries; In vivo imaging; Results paragraph 3). 20 C57BL/6J\n#   mice (11 male, 9 female); 19 task-trained, 1 imaged during spontaneous behaviour. Retrograde\n#   AAV-Cre in VM thalamus; Cre-dependent iGluSnFR3 (glutamate) and jRGECO1a (calcium) in left\n#   ALM, labelling L5B ET neurons; two mice (12 sessions) iGluSnFR3 only. Auditory delayed\n#   directional licking task (3 or 18 kHz sample, 1.25 s delay, GO cue, 2 s response window);\n#   imaging at about 175 Hz, 140 x 35 um, apical tufts under 0.1 mm depth, a 2.5 s window per trial\n#   from delay onset to 1.25 s after GO. N = 19 mice, 64 FOV (one per session), 611 dendrite\n#   segments, 2,591 synapses; median 235 trials per session (162 to 302). Trial types CL, CR, IL,\n#   IR (correct or incorrect, left or right). Spontaneous imaging (Figure S3E): one mouse, three\n#   sessions.\n# - DANDI:000010 (Methods, Secondary analysis of electrophysiology dataset; Table 5). Delayed\n#   directional licking with a tactile sample cue; ALM units from NeuroNexus silicon probes,\n#   spike sorted. Eight Sim1_KJ18-Cre and three Tlx_PL56-Cre mice; high-quality units as labelled\n#   in the dataset; sessions with at least 18 units whose session-wide firing rate exceeds 0.5 Hz;\n#   photostimulation trials excluded. Table 5 reports 11 mice, 20 sessions, 753 same-range and\n#   6,586 different-range neuron pairs. Measured variables used: unit spike times, unit quality\n#   labels, subject genotype, trial times (sample onset, GO cue), lick direction and outcome, and\n#   photostimulation per trial.\n#\n# Method for the Figure S4 claims (E1 to E8), from the Methods paragraph \"Secondary analysis of\n# electrophysiology dataset\" (SA), the Methods on synapses that SA points to, the Statistics\n# section (ST) and the code (FigureS4.ipynb and sled_glutamate_functions.py at 688e662).\n# - E1 Mice and sessions. Sim1_KJ18-Cre (8) and Tlx_PL56-Cre (3) mice; sessions that contain at\n#   least 18 units with a session-wide firing rate above 0.5 Hz (SA).\n# - E2 Units. \"Only high-quality units, as labeled in the original dataset\" (SA).\n# - E3 Trials. Photostimulation trials excluded (SA). The code then drops every trial in which any\n#   neuron's array holds a NaN (FigureS4.ipynb cell 2).\n# - E4 Activity. Spike counts in 5 ms bins, smoothed with a Gaussian of sigma 2 bins and 20 ms\n#   (4-bin) radius (SA), over each trial from tactile sample onset to 2 s after the GO cue (SA,\n#   \"estimated session-wide from activity recorded between the tactile stimulus onset and 2 s\n#   after the GO signal\").\n# - E5 Trial-specific activity (TSA). \"TSA was calculated as described for synaptic imaging data\"\n#   (SA): for each trial type (CL, CR, IR, IL) the trial-averaged activity is subtracted from the\n#   activity on the trials of that type (Methods, Activity extraction; Figure 2G).\n# - E6 Population coupling. Per session and neuron, the Pearson correlation between the neuron's\n#   TSA, flattened over trials and bins, and the summed TSA of all other neurons of the session\n#   (Methods, Population coupling; code calculate_ephys_population_coupling, which excludes no\n#   neuron other than itself). Coupling values of all sessions pooled and cut into 7 bins at the\n#   k/7 percentiles (k = 1 to 6), a value equal to an edge going to the lower bin (code, n_slices\n#   = 7; Table 5 bins 0.00 to 14.29% ... 85.71 to 100.00%).\n# - E7 Pairs. Within each session, every pair of neurons: \"same range\" for bin k when both are in\n#   bin k, \"different range\" when one is in bin k and the other in another bin. Pair value, the\n#   Pearson correlation of the two neurons' flattened TSA (code _ephys_cluster_synchy; Methods,\n#   \"Pearson's correlation coefficient was used\"). The code applies no distance or r > 0.5\n#   exclusion to neuron pairs; the Methods state those for synapse pairs only.\n# - E8 Test. For each bin, the same-range and the different-range pairs are bootstrapped\n#   independently: draw the sessions with replacement (as many as there are), pool their pairs,\n#   keep the draw only if the pool holds at least the observed number of pairs, take the mean;\n#   10,000 kept draws per group (code _spont_group_boot_iter, corrXCoupling_ephys_v3, nBoot =\n#   10000; ST, \"10,000 valid ... resamples\"). Differences are taken draw by draw (same minus\n#   different); the mean difference is the mean of these; one-tailed p = (number of differences\n#   <= 0, plus 1) / (number of valid differences, plus 1); Holm correction across the 7 bins, alpha\n#   0.05 (ST; code alternative = 'greater', pvalue_correction = 'holm'; Table 5 title \"One-tailed\").\n#\n# Open details for the Figure S4 claims, each with the readings the text allows. The notebook runs\n# every combination; a claim's outcome is the one they all give (protocol, Reader step 3).\n# - O1 Which units enter a selected session. (a) All high-quality units of a session that has at\n#   least 18 high-quality units above 0.5 Hz; (b) only the high-quality units above 0.5 Hz.\n#   SA's sentence (\"we also included only sessions that contained at least 18 units with a\n#   session-wide firing rate >0.5 Hz\") reads most directly as a session filter, (a), but (b) is\n#   allowed.\n# - O2 \"Session-wide firing rate\". (a) The unit's spike count over the whole recording divided by\n#   its duration; (b) its mean rate within the E4 windows of the included trials.\n# - O3 Trials outside the four types CL, CR, IR, IL (early-lick or no-response trials, if the\n#   dataset marks them). (a) Excluded, since TSA is defined on those four types; (b) kept, each\n#   with its own trial-type mean subtracted.\n# - O4 Where the Gaussian smoothing is applied: within each trial's window (standard choice; it\n#   cannot change the outcome beyond edge bins).\n# - O5 If trial windows from sample onset to GO + 2 s differ in length across trials, the code's\n#   fixed-size array and its NaN trial filter (E3) imply a common length; the paper does not say\n#   how it is set. Recorded as a deviation if met; the shortest common window from sample onset\n#   is the standard choice.\n# - The bootstrap seed is not given; it is a standard choice that cannot change the outcome beyond\n#   resampling noise.\n#\n# Method for the imaging claims (M1 to M6), from the Methods. These claims are not tested here;\n# the criteria say how they would be judged if the data were obtained.\n# - M1 Synaptic measures. Theta(dF/F0): dF/F0 binarized at the 99th percentile of the absolute\n#   negative deflections; Theta(dF/dt): dF/dt smoothed by a Gaussian (sigma 2, radius 4 frames)\n#   binarized at the 92nd percentile; TSA subtracts each trial type's mean (CL, CR, IL, IR);\n#   synapses with SNR < 1.5 excluded (Methods, Activity extraction).\n# - M2 Tuft spikes, SD and OD. Spike detection as in Methods, Activity extraction; only synapses on\n#   dendrites with at least 4 spikes; SD = synapses on the spiking dendrite, OD = synapses on\n#   dendrites with session-wide calcium correlation < 0.4 to it (Methods, Characterization of\n#   synaptic activity associated with tuft spikes).\n# - M3 Windows. Pre -575 to 0 ms and post 0 to 575 ms from spike onset (Figure 2F legend); coupling\n#   group and mode windows -50 to 150 ms (Figures 3F and 5B legends).\n# - M4 Population coupling and groups. Pearson correlation of a synapse's Theta(dF/dt)TSA with the\n#   summed Theta(dF/dt)TSA of the other synapses in the FOV, excluding those within 10 um on the\n#   same branch; ranks pooled over sessions; SC top 20%, WC middle 60%, NC bottom 20% (Methods,\n#   Population coupling; Results).\n# - M5 Activity modes. Weights from Equations 2 to 4, GO mode orthogonalized to the Response\n#   Direction, Outcome Direction orthogonalized to GO mode then Response Direction (Methods,\n#   Activity modes and coding directions).\n# - M6 Statistics. Hierarchical bootstrap over sessions, 10,000 valid resamples, tails as each\n#   table's title states, add-one p-values, Holm correction within each table's stated family;\n#   for Figure 3D, pairs drawn by resampling synapses 100 times without replacement within each of\n#   1,000 session bootstraps, synapse pairs closer than 2.5 um or with r > 0.5 excluded (Methods,\n#   Statistics; Pairwise correlation and autocorrelation analyses).\nschema_version: 2\npaper: doi:10.1523/jneurosci.0974-26.2026\nclaims:\n- id: figs4-session-selection\n  statement: The reanalysis of the Li et al. (2015) ALM silicon-probe recordings includes eight\n    Sim1_KJ18-Cre and three Tlx_PL56-Cre mice, 20 sessions, and yields 753 same-coupling-range and\n    6,586 different-coupling-range neuron pairs.\n  source: Methods, Secondary analysis of electrophysiology dataset; Table 5 footnote\n  quote: Our analysis included eight Sim1_KJ18-Cre mice and three Tlx_PL56-Cre mice from this study\n  expected:\n  - quantity: mice\n    value: 11\n    tolerance: 0\n  - quantity: sessions\n    value: 20\n    tolerance: 2\n  - quantity: same coupling range neuron pairs, summed over the 7 bins\n    value: 753\n    tolerance: 75\n  - quantity: different coupling range neuron pairs, summed over the 7 bins\n    value: 6586\n    tolerance: 659\n  criterion: Selection E1 to E3, binning E4 and pairs E6 and E7, under each reading of O1, O2 and\n    O3. Mice are counted exactly, as the paper names them by genotype (8 Sim1_KJ18-Cre, 3\n    Tlx_PL56-Cre); 10% for the other counts. Reproduced when, under one reading, all four\n    values are within tolerance; partially reproduced when mice and sessions are and a pair count\n    is not. The code's printed output (771 same-range pairs) is reported beside the result. The\n    reading or readings that match are carried into the other figs4 claims; when none matches,\n    those claims are run under every reading and say so.\n- id: figs4-lowest-couplers-correlated\n  statement: In the ALM silicon-probe recordings, neurons in the lowest population-coupling bin\n    (0 to 14.29%) are more correlated with each other than with neurons of other coupling bins,\n    as the synapses with the lowest coupling are.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    2; Figure S4B; Table 5\n  quote: These enhanced correlations among the lowest couplers were also found in ... publicly\n    available silicon probe recordings of ALM activity ( Fig. S4 ; Table 5 ; Li et al., 2015a )\n  statistics:\n  - about: same against different coupling range, bin 0.00 to 14.29%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.06 (rho)\n    p: 0.0007\n    corrected: Holm, across 7 bins\n    n: 753 same-range and 6,586 different-range neuron pairs, 20 sessions, 11 mice\n  depends_on:\n  - figs4-session-selection\n  expected:\n  - quantity: same minus different coupling range mean pairwise correlation, bin 0.00 to 14.29%\n    value: 0.06\n    tolerance: 0.006\n    unit: rho\n  criterion: E1 to E8, under the readings of O1 to O3 carried from figs4-session-selection.\n    Reproduced when the bin 1 mean difference is positive with Holm-corrected one-tailed p < 0.05\n    and within tolerance; partially reproduced when it is positive and significant but outside\n    tolerance; not reproduced when the Holm-corrected p is 0.05 or more.\n- id: figs4-high-couplers-correlated\n  statement: In the ALM silicon-probe recordings, neurons in the three highest coupling bins\n    (57.14 to 100%) are more correlated with neurons of the same bin than with neurons of other\n    bins, the difference growing with coupling (0.02, 0.06 and 0.1), as for the synapses.\n  source: Figure S4B; Table 5\n  quote: Figure S4. Similar organization of population coupling in silicon probe recordings\n  statistics:\n  - about: bin 57.14 to 71.43%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.02 (rho)\n    p: 0.0007\n    corrected: Holm, across 7 bins\n  - about: bin 71.43 to 85.71%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.06 (rho)\n    p: 0.0007\n    corrected: Holm, across 7 bins\n  - about: bin 85.71 to 100.00%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.1 (rho)\n    p: 0.0007\n    corrected: Holm, across 7 bins\n  depends_on:\n  - figs4-session-selection\n  expected:\n  - quantity: same minus different mean correlation, bin 57.14 to 71.43%\n    value: 0.02\n    tolerance: 0.005\n    unit: rho\n  - quantity: same minus different mean correlation, bin 71.43 to 85.71%\n    value: 0.06\n    tolerance: 0.006\n    unit: rho\n  - quantity: same minus different mean correlation, bin 85.71 to 100.00%\n    value: 0.1\n    tolerance: 0.05\n    unit: rho\n  criterion: E1 to E8, readings as in figs4-lowest-couplers-correlated. Table 5 prints one\n    significant figure, so for 0.02 and 0.1 the tolerance is the rounding interval of the\n    printed digit (0.015 to 0.025, 0.05 to 0.15), which is wider than 10%; 0.06 keeps 10%.\n    Reproduced when all three bins have a positive mean difference with Holm-corrected one-tailed\n    p < 0.05 and within tolerance; partially reproduced when all three are significant and one or\n    more is outside tolerance, or two of three are significant and within tolerance.\n- id: figs4-middle-couplers-not-correlated\n  statement: In the ALM silicon-probe recordings, the three middle coupling bins (14.29 to\n    57.14%) show no significant excess of same-bin over different-bin correlation.\n  source: Figure S4B; Table 5\n  inferred: Table 5 and the n.s. marks of Figure S4B give it; no sentence states it for the\n    silicon-probe data.\n  statistics:\n  - about: bin 14.29 to 28.57%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.004 (rho)\n    p: 0.12\n    corrected: Holm, across 7 bins\n  - about: bin 28.57 to 42.86%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.001 (rho)\n    p: 0.61\n    corrected: Holm, across 7 bins\n  - about: bin 42.86 to 57.14%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference -0.002 (rho)\n    p: 0.76\n    corrected: Holm, across 7 bins\n  depends_on:\n  - figs4-session-selection\n  criterion: A claim of absence, judged on the paper's test, E8 (one-tailed, Holm across the 7\n    bins, alpha 0.05), under the readings carried from figs4-session-selection. Reproduced when\n    none of bins 2, 3 and 4 has a Holm-corrected one-tailed p below 0.05; not reproduced when any\n    does. The three mean differences are reported either way.\n- id: fig2f-sd-input-elevated\n  statement: Mean synaptic activity, Theta(dF/F0), on the spiking dendrite (SD) is higher than on\n    simultaneously imaged other dendrites (OD) both before (by 2.5 Hz) and after (by 5.2 Hz) tuft\n    spike onset.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 4; Figure 2E, F; Table 1\n  quote: mean synaptic activity on the spiking dendrite (SD) was significantly elevated both\n    before (MD = 2.5 Hz; p = 0.002) and after (MD = 5.2 Hz; p = 6.0 × 10 −4 ) the spike\n  statistics:\n  - about: SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 2.5 Hz\n    p: 0.002\n    corrected: Holm\n    n: 826 SD and 1,922 OD synapses\n  - about: SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 5.2 Hz\n    p: 0.0006\n    corrected: Holm\n    n: 826 SD and 1,922 OD synapses\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: SD minus OD Theta(dF/F0), pre window\n    value: 2.5\n    tolerance: 0.25\n    unit: Hz\n  - quantity: SD minus OD Theta(dF/F0), post window\n    value: 5.2\n    tolerance: 0.52\n    unit: Hz\n  criterion: Not tested on the dandiset. M1 to M3 and M6 (two-tailed, Holm within the Theta(dF/F0)\n    family of Table 1). Reproduced when both differences are positive, significant and within\n    tolerance.\n- id: fig2j-tsa-dendrite-specific\n  statement: Trial-specific activity, Theta(dF/F0)TSA, rises around tuft spikes at least five times\n    more on the spiking dendrite than on other dendrites, before (MD 1.87 Hz) and after (MD 3.75\n    Hz) spike onset.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 5; Figure 2H to J; Table 1\n  quote: were at least 5 × larger on the spiking dendrite than others, both before (MD = 1.9 Hz; p\n    = 6.0 × 10 −4 ) and after (MD = 3.8 Hz; p = 6.0 × 10 −4 ) the spike\n  statistics:\n  - about: SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.87 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 3.75 Hz\n    p: 0.0006\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: SD minus OD Theta(dF/F0)TSA, pre window\n    value: 1.87\n    tolerance: 0.187\n    unit: Hz\n  - quantity: SD minus OD Theta(dF/F0)TSA, post window\n    value: 3.75\n    tolerance: 0.375\n    unit: Hz\n  criterion: Not tested on the dandiset. M1 to M3, M6. \"At least 5 times larger\" is read either\n    as the SD mean over the OD mean in each window, or as the SD increase over the OD increase\n    from a pre-spike baseline; the paper does not say which. Reproduced when both differences are\n    significant and within tolerance and the ratio is 5 or more under one reading.\n- id: fig2i-tsa-extended-kinetics\n  statement: The spike-associated Theta(dF/F0)TSA elevation on the spiking dendrite rises (HWHM\n    176 ms) and decays (HWHM 278 ms) over hundreds of milliseconds, peaking at least 101 ms after\n    spike onset, much longer than iGluSnFR3 kinetics and the signal's autocorrelation time\n    constant.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 5; Figure 2I, K\n  quote: dynamics were well-fitted by an exponential rise (176 ± 79 ms, half-width at half-max;\n    HWHM) and decay (278 ± 79 ms, HWHM) with a peak that lagged (>101 ± 38 ms) the tuft spike\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: rise half-width at half-max\n    value: 176\n    tolerance: 79\n    unit: ms\n  - quantity: decay half-width at half-max\n    value: 278\n    tolerance: 79\n    unit: ms\n  - quantity: peak lag after spike onset\n    value: 101\n    tolerance: 38\n    unit: ms\n  criterion: Not tested on the dandiset. Composite single-exponential rise and decay with a joint\n    intercept, fitted to bootstrap group means, transition at the maximum within 0 to 400 ms\n    (Methods, Characterization of synaptic activity associated with tuft spikes); tolerance the\n    paper's stated spread. Reproduced when all three values are within tolerance and both HWHMs\n    exceed the autocorrelation decay constant of Figure 2K.\n- id: figs1-controls-unchanged\n  statement: Restricting to larger tuft spikes or excluding high-motion frames does not change the\n    spike-associated synaptic activity.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 5; Figure S1E to J; Table 2\n  quote: Restricting analysis to spikes with larger peak Δ F / F 0 ( Fig. S1 E – G ; Table 2 ) or\n    excluding frames with large lateral brain motion ( Fig. S1 H – J ; Table 2 ) did not\n    significantly change the spike-associated synaptic activity timecourses\n  statistics:\n  - about: low against high event threshold, pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.0 Hz\n    p: 0.3\n    corrected: Holm\n  - about: low against high event threshold, post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.01 Hz\n    p: 1\n    corrected: Holm\n  - about: control against motion removed, pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.2 Hz\n    p: 1\n    corrected: Holm\n  - about: control against motion removed, post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.08 Hz\n    p: 1\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. A claim of absence on the paper's test, two-tailed\n    hierarchical bootstrap, Holm within each control family (Table 2), alpha 0.05; spike threshold\n    0.3 against 1.0 dF/F0 (Figure S1E legend), motion frames above the 85th percentile blanked\n    (Methods, Brain motion exclusion analysis). Reproduced when no comparison is significant.\n- id: fig2n-abrupt-input-dendrite-specific\n  statement: Abrupt increases in input, Theta(dF/dt)TSA, are elevated on the spiking dendrite\n    over other dendrites before (MD 1.15 Hz) and after (MD 1.33 Hz) tuft spike onset, with no\n    significant difference between pre and post.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 6; Figure 2L to N; Table 1\n  quote: This increase was specific to the spiking dendrite ( Fig. 2 N ; Table 1 ), both before (MD\n    = 1.1 Hz; p = 6.0 × 10 −4 ) and after (MD = 1.3 Hz; p = 6.0 × 10 −4 ) spike onset\n  statistics:\n  - about: SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.15 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.33 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: SD pre against SD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.08 Hz\n    p: 0.75\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: SD minus OD Theta(dF/dt)TSA, pre\n    value: 1.15\n    tolerance: 0.115\n    unit: Hz\n  - quantity: SD minus OD Theta(dF/dt)TSA, post\n    value: 1.33\n    tolerance: 0.133\n    unit: Hz\n  criterion: Not tested on the dandiset. M1 to M3, M6. Reproduced when both SD minus OD differences\n    are significant and within tolerance.\n- id: fig2m-abrupt-input-fast-kinetics\n  statement: The spike-associated Theta(dF/dt)TSA rises (HWHM 68 ms) and decays (HWHM 71 ms) faster\n    than Theta(dF/F0)TSA, with a peak 32 ms from spike onset.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 6; Figure 2M\n  quote: exhibited a more rapid rise (68 ± 49 ms, HWHM) and decay (71 ± 26 ms, HWHM) than the\n    spike-associated increase in ... with a peak that was closer (32 ± 13 ms) to spike onset\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: rise HWHM\n    value: 68\n    tolerance: 49\n    unit: ms\n  - quantity: decay HWHM\n    value: 71\n    tolerance: 26\n    unit: ms\n  - quantity: peak time from spike onset\n    value: 32\n    tolerance: 13\n    unit: ms\n  criterion: Not tested on the dandiset. Fit as in fig2i-tsa-extended-kinetics; tolerance the\n    paper's stated spread. Reproduced when all three values are within tolerance.\n- id: table1-both-sexes\n  statement: The dendrite-specific elevation of Theta(dF/dt)TSA holds in male and in female mice\n    analysed separately.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 6; Table 1\n  quote: Furthermore, we confirmed that these results generalized to both male and female mice (\n    Table 1 )\n  statistics:\n  - about: male, SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.4 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: male, SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.5 Hz\n    p: 0.0008\n    corrected: Holm\n  - about: female, SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.753 Hz\n    p: 0.005\n    corrected: Holm\n  - about: female, SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.11 Hz\n    p: 0.01\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. As fig2n-abrupt-input-dendrite-specific within each sex.\n    Reproduced when SD exceeds OD significantly in both windows in both sexes.\n- id: figs1l-multibranch-specific\n  statement: For putative multi-branch tuft spikes, spike-associated synaptic activity remains\n    dendrite-specific after spike onset.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 7; Figure S1K, L; Table 2\n  quote: the synaptic activity associated with these confirmed multi-branch events was still\n    dendrite-specific ( Fig. S1 K , L ; Table 2 )\n  statistics:\n  - about: SD post against OD post\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 2.0 Hz\n    p: 0.004\n    corrected: Holm\n    n: 485 SD and 1,332 OD synapses\n  - about: SD pre against OD pre\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.9 Hz\n    p: 0.16\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: SD minus OD Theta(dF/F0)TSA, post, multi-branch spikes\n    value: 2.0\n    tolerance: 0.2\n    unit: Hz\n  criterion: Not tested on the dandiset. Multi-branch events as in Methods (another segment with\n    session correlation > 0.4 and same-trial correlation > 0.7). Reproduced when the post\n    difference is significant and within tolerance.\n- id: figs2ab-correlation-declines-with-distance\n  statement: Pairwise noise and signal correlations between synapses decline with distance.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 7; Figure S2A, B\n  quote: pairwise trial-to-trial and task-driven correlations between synapses did decline as a\n    function of distance ( Fig. S2 A , B\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. Single-exponential decay fit to bootstrap means of\n    pairwise correlation against distance (Methods, Analysis of synapse clustering by function).\n    Reproduced when the fitted decay is negative for both noise and signal correlation.\n- id: fig2c-dendrite-correlation-bimodal\n  statement: Pairwise calcium correlations between dendrite segments are bimodal with an antimode\n    near 0.4.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 3; Figure 2C\n  quote: This threshold was the approximate antimode within the bimodal distribution of\n    correlations between segments ( Fig. 2 C )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. Floored dF/F0 correlations (Methods, Pairwise correlation\n    and autocorrelation analyses), 5,078 pairs. Reproduced when the distribution has two modes\n    with the antimode between 0.3 and 0.5.\n- id: figs1c-tuft-spikes-rare\n  statement: Tuft spikes occur at rates about 100 times lower than synaptic events, about 0.01 Hz,\n    with a unimodal amplitude distribution.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 3; Discussion, paragraph 1; Figure S1C, D\n  quote: tuft spikes were detected at rates ≈100 × lower than synaptic activity ( Fig. S1 C ) with\n    a unimodal amplitude distribution ( Fig. S1 D )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: tuft spike rate\n    value: 0.01\n    tolerance: 0.001\n    unit: Hz\n  criterion: Not tested on the dandiset. Reproduced when the median synaptic event rate over the\n    median tuft spike rate is between 50 and 200 (read from \"about 100\") and the tuft spike rate\n    is within tolerance.\n- id: fig3c-coupling-distribution\n  statement: Population coupling of synapses is centred near zero with a long tail of highly\n    coupled synapses.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    1; Figure 3C\n  quote: the coupling of synapses to the L5 ET tuft input population was centered near zero, with a\n    long tail of highly coupled synapses ( Fig. 3 C )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. M4 over 2,072 synapses. Reproduced when the median\n    coupling lies within 0.05 of zero (a choice made here; the paper gives no number) and the\n    distribution is right-skewed.\n- id: figs3-coupling-rank-robust\n  statement: Coupling rank is robust to population size, session pooling, signal amplitude and\n    brain motion.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    1; Figure S3A to D\n  quote: This coupling rank estimate was robust to various potential technical artifacts, including\n    synapses per FOV, signal amplitude, and brain motion ( Fig. S3 A – D )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: r, coupling rank against population size\n    value: 0.12\n    tolerance: 0.012\n  - quantity: r, pooled against within-session rank\n    value: 0.83\n    tolerance: 0.083\n  - quantity: r, coupling rank against mean transient size\n    value: -0.18\n    tolerance: 0.018\n  - quantity: r, rank before against after motion blanking\n    value: 0.99\n    tolerance: 0.099\n  criterion: Not tested on the dandiset. Values from the Figure S3A to D legends, n = 2,591\n    synapses. Reproduced when all four are within tolerance.\n- id: figs3f-coupling-not-from-early-response\n  statement: Coupling ranks stay stable after excluding the early response epoch (0 to 0.5 s from\n    GO).\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 1; Figure\n    S3F\n  quote: coupling ranks remained stable after excluding this epoch ( Fig. S3 F )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: r, coupling rank before against after removing 0 to 0.5 s from GO\n    value: 0.94\n    tolerance: 0.094\n  criterion: Not tested on the dandiset. Reproduced when r is within tolerance.\n- id: fig3d-high-couplers-correlated\n  statement: Highly coupled synapses are more correlated with each other than with synapses of\n    other coupling bins.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    2; Figure 3D; Table 3\n  quote: highly coupled synapses were more correlated with each other than with other synapses (\n    Fig. 3 D ; Table 3 )\n  statistics:\n  - about: bin 85.71 to 100.00%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.06 (rho)\n    p: 0.007\n    corrected: Holm\n  - about: bin 71.43 to 85.71%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.02 (rho)\n    p: 0.007\n    corrected: Holm\n  - about: bin 57.14 to 71.43%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.01 (rho)\n    p: 0.007\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: same minus different mean correlation, bin 85.71 to 100.00%\n    value: 0.06\n    tolerance: 0.006\n    unit: rho\n  criterion: Not tested on the dandiset. M4, M6 (Figure 3D pair procedure), 7 rank bins. Reproduced\n    when the top three bins are significant and the top bin is within tolerance.\n- id: fig3d-lowest-couplers-correlated\n  statement: Synapses with the lowest coupling are also more correlated among themselves.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    2; Figure 3D; Table 3\n  quote: Surprisingly, synapses with the lowest coupling also exhibited a higher correlation among\n    themselves ( Fig. 3 D ; Table 3 )\n  statistics:\n  - about: bin 0.00 to 14.29%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.02 (rho)\n    p: 0.007\n    corrected: Holm\n    n: 9,561 same-range and 71,212 different-range synapse pairs\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: same minus different mean correlation, bin 0.00 to 14.29%\n    value: 0.02\n    tolerance: 0.005\n    unit: rho\n  criterion: Not tested on the dandiset. As fig3d-high-couplers-correlated; tolerance the rounding\n    interval of the one printed significant figure. Reproduced when bin 1 is significant and\n    within tolerance.\n- id: figs3e-spontaneous-lowest-couplers\n  statement: The higher correlation among the lowest couplers also appears in spontaneous synaptic\n    activity.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    2; Figure S3E; Table 4\n  quote: These enhanced correlations among the lowest couplers were also found in continuous\n    imaging of spontaneous synaptic activity ( Fig. S3 E ; Table 4 )\n  statistics:\n  - about: bin 0.00 to 14.29%\n    test: one-tailed hierarchical bootstrap mean difference test\n    statistic: mean difference 0.1 (rho)\n    p: 0.0007\n    corrected: Holm\n    n: 1,965 same-range and 22,424 different-range pairs, 3 sessions, 1 mouse\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: same minus different mean correlation, bin 0.00 to 14.29%, spontaneous\n    value: 0.1\n    tolerance: 0.05\n    unit: rho\n  criterion: Not tested on the dandiset. Coupling from dF/F0 (Methods, Population coupling).\n    Reproduced when bin 1 is significant and within tolerance (rounding interval of one\n    significant figure).\n- id: fig3f-sc-most-active-at-spike\n  statement: Strongly coupled (SC) synapses on the spiking dendrite show a higher rate of abrupt\n    increases in activity at tuft spike onset than weakly (WC) or nonpositively (NC) coupled\n    ones; NC and WC do not differ.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    4; Figure 3E, F; Table 6\n  quote: SC synapses exhibited a higher rate of abrupt increases in activity at tuft spike onset\n    (window\n  statistics:\n  - about: SC SD against WC SD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.1 Hz\n    p: 0.002\n    corrected: Holm\n  - about: SC SD against NC SD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.0 Hz\n    p: 0.02\n    corrected: Holm\n  - about: NC SD against WC SD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.08 Hz\n    p: 0.7\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: SC SD minus WC SD Theta(dF/dt)TSA, -50 to 150 ms\n    value: 1.1\n    tolerance: 0.11\n    unit: Hz\n  - quantity: SC SD minus NC SD Theta(dF/dt)TSA, -50 to 150 ms\n    value: 1.0\n    tolerance: 0.1\n    unit: Hz\n  criterion: Not tested on the dandiset. M1 to M4, M6. Reproduced when both SC differences are\n    significant and within tolerance.\n- id: fig3f-dendrite-specific-every-group\n  statement: Spike-associated abrupt input is dendrite-specific in every coupling group, SC\n    included.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    4; Figure 3F; Table 6\n  quote: Interestingly, this spike-associated increase in SC activity was still highly\n    dendrite-specific\n  statistics:\n  - about: SC SD against SC OD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 1.5 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: WC SD against WC OD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.59 Hz\n    p: 0.0006\n    corrected: Holm\n  - about: NC SD against NC OD\n    test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = 0.77 Hz\n    p: 0.0006\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: SC SD minus SC OD\n    value: 1.5\n    tolerance: 0.15\n    unit: Hz\n  criterion: Not tested on the dandiset. M1 to M4, M6. Reproduced when all three SD against OD\n    differences are significant and the SC one is within tolerance.\n- id: figs3g-dff-groups-less-distinct\n  statement: Differences between coupling groups at tuft spike onset are far less pronounced with\n    Theta(dF/F0) than with Theta(dF/dt).\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    4; Figure S3G\n  quote: The differences between coupler groups were far less pronounced using Θ (Δ F / F 0 )\n    activity\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. Reproduced when the SC SD minus WC SD difference relative\n    to the WC SD level in the -50 to 150 ms window is smaller with Theta(dF/F0)TSA than with\n    Theta(dF/dt)TSA (a measure chosen here; the paper gives no test).\n- id: figs2c-no-coupling-clustering\n  statement: Synapses of the same coupling group do not significantly cluster on the same\n    dendrite segment.\n  source: Results, Inputs SC to the population are the most active at tuft spike onset, paragraph\n    4; Figure S2C\n  quote: it was not statistically significant (same vs across dendrite MD = −0.053 a.u., p = 0.19;\n    Fig. S2 C )\n  statistics:\n  - test: two-tailed hierarchical bootstrap mean difference test\n    statistic: MD = -0.053 a.u.\n    p: 0.19\n    n: 461 synapses\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. A claim of absence on the paper's test (Methods, Analysis\n    of synapse clustering by function), alpha 0.05. Reproduced when p >= 0.05.\n- id: fig4df-group-timing\n  statement: SC synapses are mostly active right after the GO cue, NC synapses later during reward\n    collection, and WC in between.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 1; Figure\n    4D to F\n  quote: SC synapses were predominantly active immediately following the GO cue ( Fig. 4 D ),\n    whereas NC synapses were predominantly active during a later epoch when mice typically\n    collected reward ( Fig. 4 F )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. Reproduced when the median peak time of correct-trial\n    Theta(dF/F0) is ordered SC < WC < NC (a measure chosen here; the paper shows heatmaps only).\n- id: fig4h-go-mode-sc\n  statement: GO-mode encoding is greater for SC than NC synapses.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 2; Figure\n    4G, H; Table 7\n  quote: The encoding of the GO Mode was greater for SC synapses than NC synapses ( Fig. 4 G , H ;\n    MD = 0.006 a.u.; p = 0.002)\n  statistics:\n  - about: SC against NC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0060 a.u.\n    p: 0.002\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: SC minus NC GO-mode projection, 0 to 0.25 s\n    value: 0.006\n    tolerance: 0.0006\n    unit: a.u.\n  criterion: Not tested on the dandiset. M5, M6. Reproduced when significant and within tolerance.\n- id: fig4h-outcome-nc\n  statement: Outcome-direction encoding is greater for NC than SC synapses, and for WC than SC.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 2; Figure\n    4G, H; Table 7\n  quote: encoding of the Outcome Direction was greater for NC synapses than SC synapses ( Fig. 4 G\n    , H ; MD = 0.002 a.u.; p = 6 × 10 −4 )\n  statistics:\n  - about: NC against SC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0020 a.u.\n    p: 0.0006\n    corrected: Holm\n  - about: WC against SC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0010 a.u.\n    p: 0.0006\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n    quantity: NC minus SC Outcome Direction projection, 0.6 to 1.2 s\n    value: 0.002\n    tolerance: 0.0002\n    unit: a.u.\n  criterion: Not tested on the dandiset. M5, M6. Reproduced when NC exceeds SC significantly\n    within tolerance.\n- id: fig4h-response-similar\n  statement: Response Direction encoding is similar across coupling groups.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 2; Figure\n    4G, H; Table 7\n  quote: Response Direction encoding was similar across groups ( Fig. 4 G , H )\n  statistics:\n  - about: SC against WC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0000 a.u.\n    p: 1.0\n    corrected: Holm\n  - about: SC against NC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0008 a.u.\n    p: 0.8\n    corrected: Holm\n  - about: WC against NC\n    test: two-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0008 a.u.\n    p: 0.6\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. A claim of absence on the paper's test (Table 7, Holm\n    within the Response Direction family, alpha 0.05). Reproduced when no pair differs.\n- id: fig5b-spike-go-mode-sc-wc\n  statement: Around tuft spikes, GO-mode projections of SD activity are greater for SC and WC than\n    for NC synapses.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 3; Figure\n    5A, B; Table 8\n  quote: along the GO Mode for both SC SD synapses and WC SD synapses were greater than for NC SD\n    synapses\n  statistics:\n  - about: SC SD against NC SD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.005 a.u.\n    p: 0.003\n    corrected: Holm\n  - about: WC SD against NC SD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.002 a.u.\n    p: 0.007\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: SC SD minus NC SD GO-mode projection, -50 to 150 ms\n    value: 0.005\n    tolerance: 0.0005\n    unit: a.u.\n  - quantity: WC SD minus NC SD GO-mode projection, -50 to 150 ms\n    value: 0.002\n    tolerance: 0.0002\n    unit: a.u.\n  criterion: Not tested on the dandiset. Theta(dF/dt)TSA projected on M5 weights, M3 window, M6.\n    Reproduced when both are significant and within tolerance.\n- id: fig5d-spike-outcome-nc\n  statement: Around tuft spikes, Outcome Direction projections of SD activity are greater for NC\n    than for SC and WC synapses.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 3; Figure\n    5C, D; Table 8\n  quote: spike-associated projections along the Outcome Direction were greater for NC SD synapses\n    than the other two groups\n  statistics:\n  - about: NC SD against SC SD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.001 a.u.\n    p: 0.02\n    corrected: Holm\n  - about: NC SD against WC SD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.001 a.u.\n    p: 0.02\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  expected:\n  - quantity: NC SD minus SC SD Outcome projection\n    value: 0.001\n    tolerance: 0.0001\n    unit: a.u.\n  - quantity: NC SD minus WC SD Outcome projection\n    value: 0.001\n    tolerance: 0.0001\n    unit: a.u.\n  criterion: Not tested on the dandiset. As fig5b-spike-go-mode-sc-wc for the Outcome Direction.\n    Reproduced when both are significant and within tolerance.\n- id: fig5b-go-mode-dendrite-specific\n  statement: GO-mode projections around tuft spikes are dendrite-specific in all coupling groups.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 3; Figure\n    5B; Table 8\n  quote: Projections were dendrite-specific for all coupling groups along the GO Mode ( Fig. 5 B ;\n    Table 8\n  statistics:\n  - about: SC SD against SC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.004 a.u.\n    p: 0.02\n    corrected: Holm\n  - about: WC SD against WC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.002 a.u.\n    p: 0.01\n    corrected: Holm\n  - about: NC SD against NC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.0006 a.u.\n    p: 0.02\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. M3 to M6. Reproduced when all three SD against OD\n    differences are significant.\n- id: fig5d-outcome-not-dendrite-specific\n  statement: Outcome Direction projections around tuft spikes are not significantly\n    dendrite-specific for any coupling group.\n  source: Results, Spike-associated activity occurs along distinct dimensions, paragraph 3; Figure\n    5D; Table 8\n  quote: Projections along the Outcome direction were not significantly dendrite-specific for any\n    coupling group\n  statistics:\n  - about: NC SD against NC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = 0.001 a.u.\n    p: 0.05\n    corrected: Holm\n  - about: WC SD against WC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = -0.0003 a.u.\n    p: 1\n    corrected: Holm\n  - about: SC SD against SC OD\n    test: one-tailed hierarchical bootstrap difference test\n    statistic: MD = -0.0002 a.u.\n    p: 1\n    corrected: Holm\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. A claim of absence on the paper's test (Table 8, Holm\n    within the Outcome SD against OD family, alpha 0.05). Reproduced when no group has a\n    corrected p below 0.05.\n- id: fig1efg-task-selective-synapses\n  statement: Individual synapses show task selectivity like ALM neurons, including GO-driven,\n    lick-direction-selective and outcome-selective synapses.\n  source: Results, Tuft spikes are accompanied by dendrite-specific, temporally extended input\n    episodes, paragraph 3; Figure 1E to G\n  quote: including synapses consistently driven by the GO cue ( Fig. 1 E ), selective for lick\n    direction ( Fig. 1 F ), and selective for task-outcome ( Fig. 1 G )\n  data: elsewhere\n  where: Not in a public archive; Code and data availability names github.com/kerlin-lab/Gable_2026,\n    which at commit 688e662 holds code only\n  criterion: Not tested on the dandiset. Shown by example synapses only; reproduced when at least\n    one synapse of each kind is found by its trial-averaged Theta(dF/F0) (a qualitative check).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Claims file written. Running the quote checker.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/gable-2026.yaml paper/10.1523-jneurosci.0974-26.2026.txt; grep -n "—\|rather" claims/gable-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/gable-2026.yaml'))['claims']
print(len(d), sum('statistics' in c for c in d), sum('criterion' in c for c in d), sum('expected' in c for c in d), sum(c.get('data','dataset')=='dataset' for c in d))"; git status --short
```

```
34 22 34 21 4
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
?? claims/gable-2026.yaml
?? scripts
```

**Agent**

I wrote `claims/gable-2026.yaml`. It has 34 claims, and the quote checker passes with 0 problems (33 quotes, 52 statistical values found). Only 4 of the claims can be tested on DANDI:000010.

**Text read.** The version of record (PMC13612898, J Neurosci 46(38) e0974262026): Methods, Results, legends for Figures 1–5, Tables 1–8 and the Discussion. The same text file holds the supplement (legends and panel text of Figures S1–S5). Nothing the claims need is missing.

**Code read.** github.com/kerlin-lab/Gable_2026 at commit 688e662. It has one notebook per figure and a function library, but no data. For Fig. S4 it holds the coupling, pairwise-correlation and bootstrap code. It does not hold the step that builds the notebook's input from the DANDI files: unit, session and trial selection, binning, smoothing, and the trial-specific activity (each trial's activity minus the mean for its trial type).

**What the dataset can test.** DANDI:000010 (Li et al. 2015, ALM silicon probes) is only reanalysed for Fig. S4 and Table 5. These are the 4 dataset claims:
- **Session selection:** 11 mice, 20 sessions, 753 same-bin and 6,586 different-bin neuron pairs.
- **Lowest coupling bin:** neurons are more correlated within the bin than with other bins (mean difference 0.06, p = 7e-4).
- **Top three bins:** same result (0.02, 0.06, 0.1).
- **Middle three bins:** no significant difference (a claim of absence).

The other 30 claims rest on the paper's own two-photon imaging. That is not in a public archive, so they are marked `data: elsewhere` (not public). They still carry criteria taken from the Methods.

**Counts.** All 34 claims have criteria, 33 have quotes (one uses `inferred`), 22 have statistics and 21 have expected values.

**Details left open for the Fig. S4 claims, with the readings named:**
- **O1, which units count in a selected session:** (a) all high-quality units of a session that has at least 18 units above 0.5 Hz; (b) only the units above 0.5 Hz.
- **O2, "session-wide firing rate":** (a) over the whole recording; (b) within the analysis windows of the included trials.
- **O3, trials outside the four correct/incorrect × left/right types (e.g. early-lick or no-response):** (a) excluded; (b) kept, each with its own trial-type mean subtracted.
- **O4 and O5, standard choices:** smoothing within each trial, and a common window length if trial lengths differ. The bootstrap seed is not given either.
- **Tolerances:** Table 5 prints one significant figure, so for 0.02 and 0.1 I used the rounding interval of that digit instead of 10%, and say why in the criterion.

**Missing from the paper:**
- The paper's imaging data are not public. Code and data availability names the GitHub repository, which holds code only.
- The step that prepares the DANDI data for Fig. S4 is not in the code, so O1 to O3 rest on the text alone.
- The code's printed output gives 771 same-bin pairs where Table 5 prints 753. I noted it in the file and did not use it for any expected value.
- A few imaging criteria use measures I chose where the paper gives no number or test. They are marked "chosen here": the coupling median near zero, the dF/F0 group contrast, and the peak-time ordering.

I did not commit anything. The untracked dotfiles and `scripts` in the working tree were there before this run.

## End of run

32 turns, 6 minutes, $2.51 at API prices, result: success.
