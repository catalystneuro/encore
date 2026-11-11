# starkweather-2018 · verifier-1 · run 42949290629

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 392
drwxr-xr-x 6 runner runner    4096 Nov 11 03:05 .
drwxr-xr-x 7 runner runner    4096 Nov 11 03:05 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 02:54 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 02:54 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 11 03:05 .claude
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.development
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.local
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.production
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.test
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .env.test.local
drwx------ 2 runner runner    4096 Nov 11 03:05 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 02:54 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 02:54 .github
-rw-r--r-- 1 runner runner       0 Nov 11 03:05 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 02:54 .idea
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat starkweather-2018.yaml
```

```
<persisted-output>
Output too large (49.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/1019a752-9978-4306-a2de-f3715dea8454/tool-results/bqjddt3h0.txt

Preview (first 2KB):
# Claims for Starkweather, Gershman & Uchida (2018), Neuron 98, 616-629, tested on CRCNS vta-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (paper/10.1016-j.neuron.2018.03.036.txt, supplied by a
# person), with its STAR Methods and the Supplemental Information (legends of Figures S1 to
# S8). The PDF could not be rendered here, so numbers printed only inside figures were read
# from the extracted text; the claims that rest on them say so.
#
# Code read: https://github.com/cstarkweather/Starkweather2018 at commit d667730 (the
# "GitHub link" of Code Availability points to the account; this is its repository for the
# paper). It holds only the belief state TD model (training, simulation, plotting, MATLAB).
# No analysis code for the recordings is linked, so every method for the recorded data comes
# from the Methods and legends. The code differs from the Methods in two settings of the
# simulation script (allSimulations_Saline_SalB.m) as committed, 10 simulations where the
# legends say 50, and every simulation intact (belief_impaired_dist all zeros) where the text
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat vta.py belief_td.py
```

```
"""Loading and response measures for CRCNS vta-1 (Starkweather, Gershman & Uchida 2018).

The data set is CRCNS vta-1 (doi:10.6080/K01J97X6), which CRCNS does not version
(version "unversioned"). It is one zip, `vta-1/live/data.zip`, MD5
c5d2a9f8aaf699cbdd2bda1bace22e7e in the data set's `checksums.md5`, streamed
from the public S3 bucket `crcnsarchive` and opened in place with fsspec and
zipfile. Each member is one light-identified dopamine neuron, named
`<Saline|SalB>_Task<1|2>_<n>.mat`, holding `odor_onsets`, `reward_onsets`,
`spiketimes` (all in ms) and `trial_type` (data description, version 0.6).

Where each parameter comes from:

- Post-reward response, spikes 50 to 200 ms after reward onset; pre-reward
  response, spikes 0 to 400 ms before reward onset (Methods, Data analysis),
  with 0 to 200 ms as the other reading (Figure 4A legend); both
  baseline-subtracted, baseline 0 to 1 s before odor onset (Methods, Data
  analysis). These are fixed in the claims file's opening comment. Responses are
  rates in spikes/s, as the figures plot them (claims file).
- Omission response, spikes 0 to 1000 ms after the usual reward time (Methods,
  Data analysis); the usual time is 1.2 s for odor B and 2.8 s for odor C
[... 492 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/1019a752-9978-4306-a2de-f3715dea8454/tool-results/bqjddt3h0.txt"
}
```

```
1	# Claims for Starkweather, Gershman & Uchida (2018), Neuron 98, 616-629, tested on CRCNS vta-1.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
3	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (paper/10.1016-j.neuron.2018.03.036.txt, supplied by a
6	# person), with its STAR Methods and the Supplemental Information (legends of Figures S1 to
7	# S8). The PDF could not be rendered here, so numbers printed only inside figures were read
8	# from the extracted text; the claims that rest on them say so.
9	#
10	# Code read: https://github.com/cstarkweather/Starkweather2018 at commit d667730 (the
11	# "GitHub link" of Code Availability points to the account; this is its repository for the
12	# paper). It holds only the belief state TD model (training, simulation, plotting, MATLAB).
13	# No analysis code for the recordings is linked, so every method for the recorded data comes
14	# from the Methods and legends. The code differs from the Methods in two settings of the
15	# simulation script (allSimulations_Saline_SalB.m) as committed, 10 simulations where the
16	# legends say 50, and every simulation intact (belief_impaired_dist all zeros) where the text
17	# says 60% impaired; the Methods are followed and the code's settings are variants.
18	#
19	# Data the paper used. 12 male DAT-Cre mice. Dopamine recordings in the left VTA of 8
20	# KORD-expressing mice, 4 trained on task 1 (odors A to C rewarded in 100% of trials) and 4 on
[... 845 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_starkweather_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            else: print('--OUT--', list(d.keys()))
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1212 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Starkweather, Gershman & Uchida (2018) from CRCNS vta-1
3	
4	Paper: Starkweather CK, Gershman SJ, Uchida N (2018). The Medial Prefrontal Cortex Shapes Dopamine
5	Reward Prediction Errors under State Uncertainty. *Neuron* 98, 616-629.
6	[doi:10.1016/j.neuron.2018.03.036](https://doi.org/10.1016/j.neuron.2018.03.036)
7	
8	Dataset: CRCNS vta-1, [doi:10.6080/K01J97X6](http://dx.doi.org/10.6080/K01J97X6), streamed from the
9	public S3 bucket `crcnsarchive` (`vta-1/live/data.zip`).
10	
11	Version: CRCNS does not version its data sets, so the version is `unversioned`, the only one there
12	is (the paper cites this DOI, its Data Availability). The data are pinned by the MD5 of the file read,
13	`data.zip` c5d2a9f8aaf699cbdd2bda1bace22e7e, as given in the data set's `checksums.md5`; the cell
14	below checks the bytes read against it, so a later change of the file is detected. The data
15	description read is version 0.6 (March 28, 2018).
16	
17	Claims: `claims/starkweather-2018.yaml`, written from the version of record with its STAR Methods
18	and Supplemental Information, and checked by a second reader. The belief state model claims use the
19	paper's code, https://github.com/cstarkweather/Starkweather2018 at commit d667730, ported to Python
20	in `belief_td.py` (MATLAB cannot be run here).
[... 744 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 765
}
```

```
765	### fig5e-task1-slope-distribution-unchanged
766	
767	> In task 1 the distribution of slopes did not differ between saline and SalB.
768	
769	A claim of absence, judged on the two-sided rank-sum test at alpha 0.05.
770	==================== 41 code
771	for key, Sx in SL.items():
772	    a = Sx[(Sx.task == 1) & (Sx.drug == "Saline")].slope
773	    b = Sx[(Sx.task == 1) & (Sx.drug == "SalB")].slope
774	    r = stats.ranksums(a, b)
775	    print(key, "medians saline %.2f, SalB %.2f (difference %.2f); rank-sum z = %.2f, p = %.3g; n %d, %d"
776	          % (a.median(), b.median(), b.median() - a.median(), r.statistic, r.pvalue, len(a), len(b)))
777	--OUT--
778	('file', 'trial') medians saline -1.74, SalB -1.83 (difference -0.08); rank-sum z = 0.14, p = 0.886; n 42, 42
779	('file', 'mean') medians saline -1.58, SalB -2.07 (difference -0.49); rank-sum z = 0.05, p = 0.957; n 42, 42
780	('file', 'none') medians saline -1.58, SalB -2.07 (difference -0.49); rank-sum z = 0.05, p = 0.957; n 42, 42
781	('40min', 'trial') medians saline -1.74, SalB -1.83 (difference -0.08); rank-sum z = 0.17, p = 0.865; n 42, 42
782	('40min', 'mean') medians saline -1.58, SalB -2.07 (difference -0.49); rank-sum z = 0.08, p = 0.936; n 42, 42
783	('40min', 'none') medians saline -1.58, SalB -2.07 (difference -0.49); rank-sum z = 0.08, p = 0.936; n 42, 42
784	('file-count-once', 'trial') medians saline -1.74, SalB -2.13 (difference -0.38); rank-sum z = 0.48, p = 0.63; n 42, 39
[... 429 more lines not kept]
```

**Agent**

Notebook and claims read. Now checking the archive contents for the blocked claims and testing helpers.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?prefix=vta-1/&list-type=2" | head -c 4000; echo; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/vta-1/live/checksums.md5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/vta-1/live/filelist.txt; echo; cat paper/vta-1.data-description.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, pandas as pd, vta
sp=np.array([0.,10,20,30,40,100]);print(vta._count(sp,[10,np.nan,0],0,30))
print(vta.auroc([3,4,5],[0,1,2]), vta.auroc([0,1],[0,1]))
# synthetic isi_anova: 5 neurons, slope -2 known, no noise
rows=[]
rng=np.random.default_rng(0)
for n in range(5):
  for t in range(1,10):
    for k in range(4):
      isi=1+0.2*t
      rows.append(dict(neuron=f'n{n}',type=t,isi=isi,post_raw=10-2*isi+n+rng.normal(0,.1),base=1.0,base_mean=1.0,drug='Saline',task=1,session='S1'))
df=pd.DataFrame(rows)
r=vta.isi_anova(df,'post');print(r['F'],r['df1'],r['df2'],r['p'],r['slope'],r['n'])
print(vta.slopes(df).slope.round(3).tolist())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, pandas as pd, vta
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls /opt /usr/local/bin 2>/dev/null | head -30; which -a python python3 uv pip pip3 conda 2>/dev/null
```

```
Exit code 1
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
pipx
pipx_bin
post-generation
primer
runner-cache

/usr/local/bin:
LICENSE.txt
activate-global-python-argcomplete
aws
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q $TMPDIR/v 2>&1 | tail -2; VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy pandas scipy statsmodels fsspec 2>&1 | tail -2; $TMPDIR/v/bin/python -c "
import numpy as np, pandas as pd, vta
sp=np.array([0.,10,20,30,40,100]);print(vta._count(sp,[10,np.nan,0],0,30))
print(vta.auroc([3,4,5],[0,1,2]), vta.auroc([0,1],[0,1]))
rows=[]
rng=np.random.default_rng(0)
for n in range(5):
  for t in range(1,10):
    for k in range(4):
      isi=1+0.2*t
      rows.append(dict(neuron=f'n{n}',type=t,isi=round(isi,1),post_raw=10-2*isi+n+rng.normal(0,.1),base=1.0+rng.normal(0,.1),drug='Saline',task=1,session='S1'))
df=pd.DataFrame(rows); df['base_mean']=df.groupby('neuron').base.transform('mean')
r=vta.isi_anova(df,'post');print(r['F'],r['df1'],r['df2'],r['p'],r['slope'],r['n'])
print(vta.slopes(df).slope.round(3).tolist())
print(vta.slopes(df,'mean').slope.round(3).tolist(), vta.slopes(df,'none').slope.round(3).tolist())
"
```

```
[ 3. nan  3.]
1.0 0.5
1317.857363751073 8 32 4.749131533196102e-38 -2.0045720655423374 5
[-1.937, -2.028, -2.077, -2.012, -1.969]
[-1.943, -2.013, -2.012, -2.023, -1.962] [-1.943, -2.013, -2.012, -2.023, -1.962]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.github.com/repos/cstarkweather/Starkweather2018/git/trees/d667730bd5e118ceb29abd5458bb4a7dfa0baed8?recursive=1 | grep '"path"' | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/cstarkweather/Starkweather2018/d667730bd5e118ceb29abd5458bb4a7dfa0baed8; for f in allSimulations_Saline_SalB.m SimulateOdorC.m TDlearning.m; do echo "=== $f"; curl -s $B/$f; done
```

```
=== allSimulations_Saline_SalB.m
% Medial Prefrontal Cortex Shapes Dopamine Reward Prediction Errors Under
% State Uncertainty
% POMDP in the spirit of Daw et al. (2006), Rao (2010)
% Author: Clara Kwon Starkweather
%% Training - All Odors

clearvars

Weber = 0.05; %Amount of scalar timing uncertainty (fraction of sub-state length)
Jitter = 2; %Amount of temporal jitter in detecting odor onsets (fraction of sub-state length)

n_sessions=500; %number of training sessions
alphaDistribution=linspace(0.1,0.1,n_sessions); % learning rate used in each training session. May be tapered, kept constant, etc...
learned_weightsA90=zeros(30,1); %initializing weights
learned_weightsA100=zeros(30,1);
learned_weightsB90=zeros(30,1);
learned_weightsC90=zeros(30,1);

for iterations=1:n_sessions
[... 519 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/cstarkweather/Starkweather2018/d667730bd5e118ceb29abd5458bb4a7dfa0baed8; curl -s $B/trainOdorC.m | grep -n -i -E "function|weights|results_training|save" ; curl -s $B/Organize_for_Plotting.m | grep -n -i -E "awgn|rpe *=|load" | head
```

```
1:function [weights] = trainOdorC(training_session,Weber_fraction,jitter,learning_rate,w)
124:results_training = TDlearning(x,O,T_blur,w,flatten_belief,Weber_fraction,learning_rate);
125:save(strcat('OdorC_results_',num2str(training_session),'.mat'))
127:weights = (results_training.w(end,:))';
3:omissionRPE=zeros(1,30);
4:tonicRPE=zeros(1,30);
5:load(simulations(1).name)
7:phasicRPE=zeros(length(unique_ISIs),3,length(simulations));
11:load(simulations(simulation).name)
17:results.rpe=[zeros(6,1); results.rpe];
20:results.rpe=awgn(results.rpe,noise);
34:omissionRPE = (temp/length(omission_ISI_indices)) + omissionRPE;
71:tonicRPE = tonicRPE + temp_tonic;
81:tonicRPE = tonicRPE/length(simulations);
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent**

**A. Outcomes** (32 claims in the claims file: 20 tested, 12 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig2-kord-suppresses-mpfc | blocked (data_missing) | The archive holds only `data.zip`, docs, `filelist.txt` and `checksums.md5` (S3 listing). The files are 172 dopamine-neuron files with four variables (cells 3, 63). There are no mPFC units. |
| figs1e-kord-abolishes-late-activity | blocked (data_missing) | Same reason: no mPFC units. |
| figs6ce-kord-task1-animal | blocked (data_missing) | Same reason: no mPFC units. |
| fig3g-anticipatory-licking | blocked (data_missing) | No lick variable in any file (cell 3). The data description lists none. |
| figs3-task1-licks-more-sooner | blocked (data_missing) | No licks. |
| figs3-salb-spares-licking | blocked (data_missing) | No licks. |
| figs4-cell-types-unchanged | blocked (data_missing) | Only the 172 identified dopamine neurons are present (cell 3), not the 761 VTA neurons. |
| figs5b-task2-salb-below-free-water | blocked (data_missing) | There are no free-water events. `reward_onsets` exist only on odor A to C rewarded trials (cell 63: 0 elsewhere), and no trial type 12 exists. |
| figs5c-odorbc-normalized | blocked (data_missing) | Same reason: no free-water events. |
| anova-slopes-task-drug | blocked (data_missing) | Normalization by the free-water response is impossible (see B5). |
| anova-time-task-drug-interaction | blocked (data_missing) | The free-water response is a required term (see B5). |
| figs6-salb-without-kord | blocked (data_missing) | Files by group are 42/42/41/47 = 172, matching the four KORD groups exactly. The 26 no-KORD neurons are absent. |
| fig4a-task1-saline-post-decrease | reproduced | Cell 14: F(8,328) = 12.61, p = 8.4e-16, slope −2.21, 42 neurons. Paper: F = 12.6, p = 9.1e-16. |
| fig4b-task2-saline-post-increase | reproduced | Cell 16: F(8,320) = 3.70, p = 3.8e-4 (same as the paper), slope +1.30, 41 neurons. |
| fig4b-odorc-below-latest-odora | reproduced | Cell 18: C 12.30 vs A at 2.8 s 15.06 spikes/s, F(1,40) = 22.66, p = 2.5e-5. The single-trial reading also gives p = 1.6e-7. |
| fig4ab-saline-pre-decrease | reproduced | Cell 20: both tasks p ≤ 1e-7 with negative slopes, under both windows and both 40-min readings. 0–400 ms gives p = 3.6e-11 and 5.3e-18, matching the paper's 3.5e-11 and 5.3e-18. |
| fig4c-task1-salb-post-decrease | reproduced | Cell 22: F = 11.34, p = 3.3e-14 (paper 11, 3.3e-14), slope −2.33. The count-once variant with 39 neurons holds too (cell 23). |
| fig4d-task2-salb-flat | reproduced | Cell 25: F(8,368) = 0.70, p = 0.69 (paper 0.69, 0.70), slope −0.27, 47 neurons. |
| fig4cd-salb-pre-decrease | reproduced | Cell 27: all p ≤ 1.4e-9 with negative slopes, both windows. Task 1 0–400 ms gives p = 2.4e-19, the same as the paper. |
| fig5f-task2-slope-signs | reproduced | Cell 33: 29 positive and 12 negative (saline), 24 negative of 47 (SalB) under the trial baseline. All readings are within tolerance. |
| fig5e-task1-significant-slopes-unchanged | reproduced | Cell 35, trial baseline: 16/0 and 16/2, Fisher p = 0.487. Fisher p ≥ 0.05 under every reading. Counts fall outside tolerance under the mean and none baselines (SalB 18 negative). |
| fig5f-task2-significant-slopes-shift | reproduced | Cell 37, trial baseline: 1/9 against 8/7, p = 0.0405 (paper 0.041), negative share 0.10 rising to 0.53. This depends on the reading: mean and none baselines give p = 0.239 (see B3). |
| fig4e-task2-slope-distribution-shift | reproduced | Cell 39: z = 2.15, p = 0.032. The SalB median is lower (−0.06 against 1.42). Holds under all readings (p ≤ 0.037). |
| fig5e-task1-slope-distribution-unchanged | reproduced | Cell 41: z = 0.14, p = 0.886 (paper z = 0.14, p = 0.89). p ≥ 0.63 under all readings. |
| fig5f-task2-slope-variance-up | reproduced | Cell 43: variances 10.23 and 20.29, ratio 0.50, p = 0.029. All within tolerance. Per mouse cannot be shown (no subject IDs); the criterion asks only for a description. |
| fig5e-task1-slope-variance-unchanged | reproduced | Cell 46: ratio 0.59, variances 8.81 and 14.89, p = 0.097. p ≥ 0.053 under all readings, so the result sits near the threshold under the mean and none baselines. |
| fig6ab-odorc-above-odorb | reproduced | Cell 48: saline C−B 0.913 (within 0.95 ± 0.095), F(1,40) = 5.31, p = 0.027. SalB C−B 0.997 (within 1.0 ± 0.1). Rank-sum p = 0.81. |
| fig6cd-omission-dips-intact | reproduced | Cell 50: all four omission rates are below baseline, p ≤ 0.0013. SalB used df (1,46) against the paper's (1,40); the counts are reported. |
| figs5d-omission-unchanged-by-salb | reproduced | Cell 52: no epoch significant under either test or either Bonferroni family. Smallest uncorrected p = 0.023. |
| fig7cd-model-intact | reproduced | Cell 57: every part holds (post-reward slopes −0.114 and +0.149, 100% of task 2 slopes positive, pre-reward slopes negative, omission dips −0.18 and −0.13), in 5 of 5 extra seeds. |
| fig7fgh-model-belief-impaired | reproduced | Cell 59: task 2 slope falls from +0.149 to +0.037, negative fraction rises from 0 to 0.32, task 1 slope −0.154, omission responses stay. Holds in 5 of 5 seeds. |
| fig7ijk-model-timing-impaired | reproduced | Cell 61: passes the claims-file criterion under both readings, in 5 of 5 seeds. A residual omission dip remains (see B1). |

No claim in this paper states a chance level for a selection, so there was none to compare.

**B. Problems**

1. [does not affect a conclusion] The claims file criterion for fig7ijk is weaker than the paper's word "abolished". It only requires that the omission minimum is not below the intact run's minimum. Under the timing impairment the mean omission RPE is still −0.073 (B) and −0.032 to −0.043 (C) in cell 54. That is about 40% of the intact dip, and for B about 4 standard errors below zero given the noise of 0.25 per point averaged over 50 simulations. So the dip is reduced, not gone. The verdict follows the criterion; whether "abolished" holds is left open.
2. [does not affect a conclusion] Cells 50 and 48 use 47 SalB neurons (df 46), where the paper prints df 40. This is consistent with the paper's own inconsistency, and the counts are reported as the criterion asks.
3. [does not affect a conclusion] fig5f-task2-significant-slopes-shift reproduces only under the trial-by-trial baseline (cell 37). That reading is the Methods' wording and the notebook's stated default, and it is the only one that recovers the paper's exact counts and p (1/9, 8/7 at our 8 vs 9; p = 0.0405 against 0.041). Under the mean and none baselines it fails (p = 0.239). The criterion for this claim does not say "under a reading", so this choice should be stated with the conclusion.
4. [does not affect a conclusion] Three task 1 SalB file pairs share 65 to 99.7% of their spikes (cell 5), so they are probably the same neuron deposited twice. The notebook keeps all six files to match the paper's n and runs a count-once variant. Every task 1 conclusion holds in that variant (cells 23, 27, 29, 35, 41, 46).
5. [does not affect a conclusion] `anova-time-task-drug-interaction` and `anova-slopes-task-drug` were blocked outright. Some of each could be run as a stated deviation: the tr × task and tr × drug × task terms without the free-water covariate, and the task and task × drug terms on unnormalized slopes. That would not satisfy the criterion, so blocked stands, but the notebook should say that part could be tested.
6. [does not affect a conclusion] `vta.load` skips zip members that are not `.mat`, and the notebook never prints the zip's member list. A lick or free-water file inside `data.zip` would go unnoticed (see C).
7. [does not affect a conclusion] In `vta.neuron_table`, the 40-min reading takes the session's first spike as recording onset. That is a stand-in, but both readings give the same conclusions (cells 10, 29 to 52).

Helper checks on synthetic inputs all came out as expected:
- `_count`: half-open window, NaN start gives NaN.
- `auroc`: 1.0 and 0.5 on separable and identical inputs.
- `isi_anova`: recovers a slope of −2.00 with df (8, 32) for 5 neurons.
- `slopes`: recovers about −2 under every baseline reading, and the mean and none readings agree.

The model port matches the linked MATLAB at d667730 in every part I compared:
- the observation matrix and impairment in `SimulateOdorC.m`
- `TDlearning.m`
- training carries `w(end,:)`, the weights before the last update
- 10 trials per simulation for odors B and C, one of them an omission
- awgn in `Organize_for_Plotting.m`

**C. What I could not check**

- Whether `data.zip` holds members other than the 172 neuron `.mat` files (licks, free water, mPFC units). Printing `zipfile.ZipFile(...).namelist()` in cell 1 would have settled it. The data description and `filelist.txt` suggest it holds none.
- `belief_td.blur_matrix`, `blur_vector`, the tonic and phasic indexing in `simulate`, and the A-odor simulation scripts, line by line against the MATLAB. A cell comparing one fixed-seed trace (b, rpe) with a MATLAB or Octave run of the same observation series would have verified the port directly.
- That the 21 trials with no trial type are the paper's exclusions. A per-group count of these trials, with each one's effect on that group's ANOVA, would have shown whether leaving them out matters. Given how small they are, I expect it does not.
- How independent the neurons are. There are no subject IDs, so the claim's "seen in individual mice" for the variance result cannot be tested. Cell 44 gives per-session variances only.

## End of run

16 turns, 2 minutes, $1.32 at API prices, result: success.
