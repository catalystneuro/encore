# burman-2023 · verifier-2 · run 42795114588

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 452
drwxr-xr-x 6 runner runner    4096 Nov 10 10:53 .
drwxr-xr-x 7 runner runner    4096 Nov 10 10:53 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 10:53 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.development
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.production
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.test
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .env.test.local
drwx------ 2 runner runner    4096 Nov 10 10:53 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .github
-rw-r--r-- 1 runner runner       0 Nov 10 10:53 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:56 .mcp.json
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; ls -la .claude; diff burman-2023-01.yaml burman-2023.yaml | head -400
```

```
# Burman, Brodersen, Raimondo, Sen & Akerman (2023) on dandiset 000458

Tests the findings of [Burman et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.005) that can
be tested on [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the Allen
Institute Neuropixels recordings with cortical electrical stimulation, awake and under isoflurane,
that the paper reuses (Figure 4A to 4D, Figure S6), and runs the paper's network model (Figure 4E
to 4H, Figure S7). The paper's gramicidin patch-clamp recordings (Figures 1 to 3) are not in the
dandiset nor deposited anywhere.

| Claim | Outcome |
|---|---|
| The 17 sessions the paper's code reads are in the dandiset with the fields it uses | Reproduced |
| 662 neurons kept and 203 excluded, from 17 recordings in 16 mice | Partially reproduced |
| Synchrony lower awake (0.325 against 0.393) | Partially reproduced |
| Entropy higher awake (1.347 against 1.111 nats) | Partially reproduced |
| Evoked firing rate higher awake | Reproduced |
| Synchrony and entropy differences remain with firing rate regressed out | Reproduced |
| Model: hyperpolarizing E_GABA gives less activity | Reproduced |
| Model: synchrony lower with shunting E_GABA (0.784 against 0.881) | Partially reproduced |
| Model: entropy higher with shunting E_GABA (0.451 against 0.197 nats) | Partially reproduced |
[... 426 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat burman-2023-01.yaml
```

```
<persisted-output>
Output too large (45.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ad1d398a-6ccf-473e-8dbd-7758d7f11052/tool-results/b0z47eb2i.txt

Preview (first 2KB):
schema_version: 3
id: burman-2023-01
datasets:
- archive: dandi
  id: "000458"
  version: 0.230317.0039
  doi: 10.48324/dandi.000458/0.230317.0039
  relation: reuses
paper: doi:10.1016/j.neuron.2023.08.005
date: '2026-11-10'
entry: burman-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ad1d398a-6ccf-473e-8dbd-7758d7f11052/tool-results/b0z47eb2i.txt"
}
```

```
1	schema_version: 3
2	id: burman-2023-01
3	datasets:
4	- archive: dandi
5	  id: "000458"
6	  version: 0.230317.0039
7	  doi: 10.48324/dandi.000458/0.230317.0039
8	  relation: reuses
9	paper: doi:10.1016/j.neuron.2023.08.005
10	date: '2026-11-10'
11	entry: burman-2023
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 699 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" burman-2023-01.yaml burman-2023.yaml | head; python3 - <<'EOF'
import json
for f in ['reproduce_burman_2023.ipynb']:
    nb=json.load(open(f))
    for i,c in enumerate(nb['cells']):
        print(f"\n===== CELL {i} [{c['cell_type']}] =====")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain']))
            elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
```

```
<persisted-output>
Output too large (63.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ad1d398a-6ccf-473e-8dbd-7758d7f11052/tool-results/bin0cv6j1.txt

Preview (first 2KB):
===== CELL 0 [markdown] =====
# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
of the dandiset, and the one the paper's analysis code names in its docstring
(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).

**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).

[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ad1d398a-6ccf-473e-8dbd-7758d7f11052/tool-results/bin0cv6j1.txt"
}
```

```
1	
2	===== CELL 0 [markdown] =====
3	# Reproducing Burman et al. (2023) on DANDI:000458: Neuropixels claims
4	
5	**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
6	promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
7	[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)
8	
9	**Dataset.** [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version
10	0.230317.0039 (doi:10.48324/dandi.000458/0.230317.0039), the Allen Institute recordings of Claar et
11	al. (2023) that the paper reuses (Figure 4A to 4D, Figure S6). This is the only published version
12	of the dandiset, and the one the paper's analysis code names in its docstring
13	(gist a77bcf5e, revision 43a13d89), so it is pinned. The draft has the same 24 assets (checked below).
14	
15	**Text the claims were written from.** The version of record (Europe PMC, PMC11913778), with STAR
16	Methods; the supplement (Figures S1 to S7) was not available (claims file, opening comment).
17	
18	**What this notebook tests.** The claims on the dandiset. The network model claims are in
19	`network_model.ipynb`. The patch-clamp claims (Figures 1 to 3, S1 to S5) rest on recordings that
20	are not in the dandiset nor deposited anywhere ("available on request"), and are blocked.
[... 711 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ad1d398a-6ccf-473e-8dbd-7758d7f11052/tool-results/bin0cv6j1.txt",
 "offset": 732
}
```

```
732	recordings with awake mean higher: 15 of 17
733	
734	
735	===== CELL 29 [markdown] =====
736	**Result: partially reproduced.** Under A1F1 entropy is higher awake, 1.389 against 1.150 nats
737	over 656 units with a value in both conditions (65 dropped with fewer than two spikes in a
738	condition; paired t test p below 0.001, table above), in the paper's direction and at its
739	significance, but both means are outside tolerance. Awake is higher in 15 of 17 recordings. Under
740	the gist's rate (A1F2, A2F2) they are 1.347 and 1.111 nats over 597 units, the paper's values.
741	
742	===== CELL 30 [markdown] =====
743	## fig4-rate-higher-awake
744	
745	> The same electrical stimuli evoke more spiking awake than under isoflurane; the mean evoked
746	> firing rate is higher in the awake state.
747	
748	===== CELL 31 [code] =====
749	rows = []
750	for name, (area, wf, rate) in npx.READINGS.items():
751	    K = kept[name]
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for f in ['network_model.ipynb']:
    nb=json.load(open(f))
    for i,c in enumerate(nb['cells']):
        print(f"\n===== CELL {i} [{c['cell_type']}] =====")
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text'])[-6000:])
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[-3000:])
            elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
```

```
===== CELL 0 [markdown] =====
# Reproducing Burman et al. (2023): the network model (Figures 4E to 4H, S7)

**Paper.** Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ (2023). Active cortical networks
promote shunting fast synaptic inhibition in vivo. *Neuron* 111, 3531-3540.
[doi:10.1016/j.neuron.2023.08.005](https://doi.org/10.1016/j.neuron.2023.08.005)

**Data.** These claims are `data: elsewhere`: their data are generated by the paper's simulation
code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision
f6a05661c10051560aa381e334099efd8521617b, transcribed in `network.py` (its docstring lists the
differences, none of which changes the model). They use nothing from DANDI:000458 (version
0.230317.0039, read in `reproduce_burman_2023.ipynb`; the version constant is `npx.VERSION`).

**Text the claims were written from.** The version of record (PMC11913778) with STAR Methods; the
supplement (Figure S7) was not available.

| Claim | Here |
|---|---|
| fig4f-model-hyperpolarizing-less-activity | tested |
| fig4h-model-synchrony | tested |
[... 358 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np
from scipy import stats
h=[0.9437,0.9328,0.9225,0.9527,0.9404,0.9146,0.9118,0.9286,0.9244,0.9398,0.9363,0.9481,0.9319,0.9452,0.9364,0.9300,0.8930,0.9456,0.9440,0.9080]
s=[0.9820,0.9785,0.9866,0.9906,0.9919,0.9855,0.9807,0.9830,0.9826,0.9833,0.9876,0.9851,0.9828,0.9833,0.9885,0.9865,0.9819,0.9905,0.9831,0.9812]
print(stats.ttest_rel(s,h), np.mean(s), np.mean(h))
"; grep -n "shuffle\|random_state\|KFold\|Stratified" network.py | head; grep -n "p = \|p <\|p=" burman-2023.yaml | sed -n '1,200p' | grep -i -n "fig4d\|0.0001\|synchron" | head
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
35:from sklearn.model_selection import StratifiedKFold, cross_val_score
203:        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
267:    as in simulate(). Its decoding uses an unseeded shuffle, so its accuracy is not compared.
4:207:    Aw.: 50.6 ± 6.4 MΩ, n = 13 neurons, 10 mice, p < 0.0001, unpaired t test)'
15:441:    mice vs. +NBQX: 136.2 ± 11.9 MΩ, n = 10 neurons, 7 mice, p < 0.0001, unpaired t test)'
```

**Agent calls Bash**

```bash
cd  python3 -c "
import math,statistics as st
h=[0.9437,0.9328,0.9225,0.9527,0.9404,0.9146,0.9118,0.9286,0.9244,0.9398,0.9363,0.9481,0.9319,0.9452,0.9364,0.9300,0.8930,0.9456,0.9440,0.9080]
s=[0.9820,0.9785,0.9866,0.9906,0.9919,0.9855,0.9807,0.9830,0.9826,0.9833,0.9876,0.9851,0.9828,0.9833,0.9885,0.9865,0.9819,0.9905,0.9831,0.9812]
d=[a-b for a,b in zip(s,h)]; print(st.mean(d)/(st.stdev(d)/math.sqrt(20)))
"; grep -n -A30 "id: fig4d-synchrony-lower-awake" burman-2023.yaml | grep -n "p:\|test\|criterion" ; grep -n -A30 "id: figs7-model-decoding" burman-2023.yaml | head -40
```

```
16.91705244892624
7:674-    ± 0.007, p < 0.001, paired t test)'
9:676-  - test: paired t test
10:677-    p: 0.001
22:689-  criterion: Synchrony (N6) per neuron and condition over the kept neurons, mean and SEM, paired t test
25:692-    Reproduced when both means are within tolerance and the paired t test gives awake lower at p < 0.001;
26:693-    partially reproduced when the direction and test hold but a mean is outside tolerance.
842:- id: figs7-model-decoding
843-  statement: Responses of networks with shunting E_GABAAR to 100 different input patterns are decoded
844-    more accurately by a downstream classifier.
845-  source: Results, Shunting inhibition promotes local network desynchronization and response flexibility,
846-    paragraph 2; Figure S7 (not read); Methods, Characterization of stimulus-evoked spiking responses,
847-    paragraph 2
848-  quote: when we assessed a network’s ability to encode different patterned inputs, we observed that networks
849-    with shunting E GABAAR could be more accurately decoded by a downstream classifier
850-  data: elsewhere
851-  where: Not deposited; generated by the paper's simulation code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f
852-    at revision f6a05661
853-  criterion: 'The paper''s simulation gist, run 20 times as in fig4h-model-synchrony: per run and condition,
854-    spike counts of the first 50 excitatory neurons in each 25 ms epoch, a k-nearest neighbor classifier
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for id in fig4c-sample fig4-rate-higher-awake fig4h-model-synchrony fig4f-model-hyperpolarizing-less-activity; do grep -n -A40 "id: $id" burman-2023.yaml | awk '/criterion:/{f=1} f{print} /^[0-9]+-- id:/{if(f)exit}' | head -14; echo ----; done
```

```
662-  criterion: Counts of regular spiking units in the stimulated area (N2) before and after the exclusion
663-    (N7), per recording. Method N1 to N8 of the opening comment (Methods and the analysis gist), judged
664-    under the Methods reading A1F1, with A1F2, A2F1, A2F2 and the gist's waveform cut shown as variants
665-    (N7). Reproduced when the numbers kept and excluded are within tolerance and the recording and mouse
666-    counts are 17 and 16; partially reproduced when only the total (865) is within 10%. The per-recording
667-    median and range are reported under each reading.
668-- id: fig4d-synchrony-lower-awake
----
731-  criterion: Evoked firing rate (N7) per neuron and condition over the kept neurons. The paper reports
732-    no value or test in the text read (Figure S6 may hold them); the paired t test of N8, used for every
733-    per-neuron comparison of Figure 4D, is used here. Method N1 to N8 of the opening comment (Methods
734-    and the analysis gist), judged under the Methods reading A1F1, with A1F2, A2F1, A2F2 and the gist's
735-    waveform cut shown as variants (N7). Reproduced when the awake mean is higher with p < 0.05; the
736-    means under each reading are reported.
737-- id: figs6-rate-regressed
----
802-  criterion: The paper's simulation gist at revision f6a05661, run 20 times (Methods, "Each simulation
803-    was repeated 20 times"), with its defaults (100 patterns, 100 repeats, 800 excitatory and 200 inhibitory
804-    neurons, E_GABA -60 mV then -80 mV in the excitatory neurons). Per run and condition, the gist's entropy
805-    and synchrony of each excitatory neuron, from spikes 0 to 12 ms after each input in the first stimulus
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" burman-2023.yaml; grep -c "^- claim:" burman-2023-01.yaml; grep "^  outcome:" burman-2023-01.yaml | sort | uniq -c; grep -n "blocked_by" burman-2023-01.yaml | awk '{print $NF}' | sort | uniq -c
```

```
35
35
     25   outcome: blocked
      5   outcome: partially_reproduced
      5   outcome: reproduced
     24 data_missing
      1 methods_underspecified
      1 notes
```

**Agent**

**Verifier report, round 2: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims and the attempt record has 35 outcomes: 5 reproduced, 5 partially_reproduced and 25 blocked (24 data_missing, 1 methods_underspecified). Below, "main" means `reproduce_burman_2023.ipynb` and "model" means `network_model.ipynb`. Cell numbers are for the re-executed notebooks, so they differ from round 1.

### 1. Outcomes and assumptions

I agree with all 35 outcomes:
- **dataset-sessions-link:** reproduced.
- **fig4c-sample, fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake:** partially_reproduced under A1F1, with the A1F2 exact match recorded as a deviation.
- **fig4-rate-higher-awake and figs6-rate-regressed:** reproduced.
- **fig4f-model-hyperpolarizing-less-activity:** reproduced.
- **fig4h-model-synchrony and fig4h-model-entropy:** partially_reproduced.
- **figs7-model-decoding:** reproduced. This holds even with the corrected statistic in §2a.
- **figs4-intrinsic-properties:** blocked, methods_underspecified.
- **The 24 patch-clamp claims:** blocked, data_missing.

No outcome sets `assumed: true`, so there is no assumption to assess.

One small gap in the claims file. For fig4c-sample, A1F1 keeps 721, which is inside 662 ± 66.2, and excludes 144, which is outside 203 ± 20.3 (main cell 19). The criterion's partial case, "only the total (865) is within 10%", does not literally cover this: the kept count is within tolerance too. Partial is still the sensible reading.

### 2. Sentences the printed numbers do not support

**a. figs7-model-decoding: wrong t and p (bears on how the conclusion is reported, not on the outcome).**
- Model cell 20 says "D1 paired t = 16.42, p = 1.11e-12". Model cell 19 prints `D1 paired t = 16.92, p = 6.52e-13`, and the printed per-run accuracies give t = 16.92 when I recompute it.
- The figs7 notes in the attempt record give the same wrong "t = 16.42, p = 1.11e-12".
- The response to round 1 says the notes were changed to "the printed t = 16.42, p = 1.11e-12". That matches the earlier run, not this one.
- So the accuracies differ between executions. The cross-validation is seeded (`network.py:203`) and the other model numbers repeat exactly. That does not fit the deviation's implication that the seeding makes the run deterministic.
- The outcome does not change: 20 of 20 runs, p ≈ 1e-12 either way.

**b. Start-time deviation claimed where it was not run.** The deviation text on fig4c-sample, fig4-rate-higher-awake and figs6-rate-regressed says timing from start_time "is shown as a variant and keeps the direction".
- The start_time variant is run only for synchrony (main cell 24) and entropy (main cell 28).
- Cell 24 prints only n = 734 for it. No kept or excluded counts, rate test or regression are printed for start_time.

**c. Main cell 37, Summary: clocks overstated.** "their labels and clocks pass the checks above" is too strong. Main cell 8 passes 33 of 34 pairs; sub-569069 awake fails (ratio 1.07, p = 0.591). Main cell 9 and the attempt notes do state this correctly.

**d. Main cell 37, Summary: "means" covers counts.** "with means a little off under the Methods' rate" also covers fig4c-sample. That outcome is about counts, not means: 144 excluded against 203.

**e. README: run times.**
- "about 20 minutes" for the model notebook: model cell 6 prints "20 runs in 40.6 min", and cell 19 prints a total run time of 43.0 min.
- "About two minutes" for the main notebook: cell 4 took 196 s to load, and cell 35 prints 3.5 min.

**f. README: tolerance misses.** "hyperpolarizing means 0.001 to 0.002 outside tolerances" does not match model cells 11 and 14, which give misses of 0.0011 and 0.0024.

Every other sentence checks against the printed outputs: the Result conclusions in main cells 17, 21, 26, 29, 32 and 36 and model cells 11, 14 and 17, the Summary of model cell 21, the other README sentences, and the attempt notes and findings.

**My round-1 reasons in the attempt record:** they are stated faithfully and in substance in my own words. They cover B1, B2, B3, B4, B5 and the section C limits. The one omission, the per-recording minimum of 7 against 1 in fig4c-sample, is immaterial. Points B6 to B9 are not attached to any claim, which is appropriate.

### 3. Round-1 points

**Resolved:**
- **B1 (attempt side).** Main cell 13 runs the gist unmodified: 865 of 865 units match with 0 differing values, it gives 662 kept and 203 excluded, and it reproduces the paper's Figure 4D means. The deviation is recorded and a question for a reader has been added.
- **B2 (attempt side).** Model cells 10 and 13 print the run-to-run standard error (SE) and how many SEs each mean is from the paper's value, and a question for a reader has been added.
- **B3.** blocked_by is now methods_underspecified, and the reasoning is given in main cell 0 and the notes.
- **B4.** p is formatted before rounding in main cells 23, 24 and 31.
- **B5.** The clock check now covers all 17 files, and the one failing pair is named.
- **Section C, gist transcriptions.** The analysis gist (main cell 13) and the simulation gist (model cell 5: 19,093 identical spikes, and 800 of 800 neurons equal) are now checked directly.
- **Section C, learning rate.** It is now printed directly from the compiled synapse code (model cell 6: 0.1 while balancing, 0 during the test).
- **B6 to B9.** No action was needed.

**What remains that bears on a conclusion:**
- **B1, for the claims file.** Should fig4c-sample and the two fig4d claims be judged under the gist's rate? The question is pending with a reader in `questions/burman-2023.yaml`, which I could not see. Until it is answered, the three partial outcomes stand.
- **B2, for the claims file.** Should the fig4h tolerances allow for differences between seeds? This is also pending with a reader. Until it is answered, the two partial model outcomes stand.
- **New: figs7's reported statistic.** Model cell 20 and the attempt notes should give the printed t = 16.92 and p = 6.52e-13. The reason accuracy varies between executions despite the seeded cross-validation should be explained, or the deviation's wording changed. The outcome is not affected.
- **Unchanged: the supplement.** The legends of Figures S4, S6 and S7 are still unavailable. The outcomes of figs6 and figs7 do not depend on them, since every reading agrees; the block on figs4 does.

## End of run

13 turns, 2 minutes, $1.14 at API prices, result: success.
