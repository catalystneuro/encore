# starkweather-2018 · claims-check · run 42835245227

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i stark; cat claims/starkweather-2018.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/starkweather-2018.yaml; grep -n "Reader" docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 635 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/starkweather-2018.yaml"
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
[... 771 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/starkweather-2018.yaml paper/10.1016-j.neuron.2018.03.036.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.03.036.txt",
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker's 16 "value not found" flags look like the extraction printing "×" as "3" (e.g. "1.9 3 10�6"). I am confirming each by reading; continuing through the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.03.036.txt",
 "offset": 900,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.03.036.txt",
 "offset": 1700,
 "limit": 850
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat paper/vta-1.data-description.txt | head -60; python -c "
from scipy.stats import fisher_exact
print(fisher_exact([[16,0],[16,2]]), fisher_exact([[1,9],[9,7]]))
from scipy.stats import f
print(2*f.cdf(0.51,40,46), 2*f.cdf(0.59,41,41), f.sf(2.2,1,163))
"; python -c "import fitz; print(fitz.__doc__)"; which pdftoppm
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 60,104p paper/vta-1.data-description.txt; git log --oneline -3 -- claims/starkweather-2018.yaml; timeout 20 git ls-remote https://github.com/cstarkweather/Starkweather2018 2>&1 | head -3
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper's code repository is reachable at the commit the file cites (d667730), so I'll check the file's statements about the code.

**Agent calls Bash**

```bash
cd $TMPDIR && rm -rf sw && git clone -q https://github.com/cstarkweather/Starkweather2018 sw && cd sw && git log --oneline -1 && ls -R | head -50
```

```
d667730 first commit
.:
Organize_for_Plotting.m
README
README.md
SimulateOdorA_withOmission.m
SimulateOdorA_withoutOmission.m
SimulateOdorB.m
SimulateOdorC.m
TDlearning.m
allSimulations_Saline_SalB.m
blur_matrices_inputWeberFraction.m
blur_vector.m
trainOdorA_WithOUTOmission.m
trainOdorA_WithOmission.m
trainOdorB.m
trainOdorC.m
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/sw && cat allSimulations_Saline_SalB.m Organize_for_Plotting.m README.md; grep -n "1e-\|O(30,30\|awgn\|Weber\|gamma\|alpha\|=.*500\|50" SimulateOdorA_withOmission.m trainOdorA_WithOmission.m TDlearning.m | head -60
```

```
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
    
[... 435 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sw && grep -n "belief_impaired\|O(30,30" SimulateOdorA_withoutOmission.m SimulateOdorB.m SimulateOdorC.m TDlearning.m; grep -n "Weber\|nTrials\|n_trials" SimulateOdorA_withOmission.m | head
```

```
SimulateOdorA_withoutOmission.m:1:function params = SimulateOdorA_withoutOmission(simulation_index,Weber_fraction,jitter,belief_impaired,weights,learning_rate)
SimulateOdorA_withoutOmission.m:108:O(30,30,2) = 0 *(1-belief_impaired) + 0 *(belief_impaired); %omission trial
SimulateOdorA_withoutOmission.m:111:O(30,30,1) = 1 *(1-belief_impaired) + 1 *(belief_impaired);
SimulateOdorA_withoutOmission.m:123:results = TDlearning(x,O,T_blur,weights,belief_impaired,Weber_fraction,learning_rate);
SimulateOdorB.m:1:function params = SimulateOdorB(simulation_index,Weber_fraction,jitter,belief_impaired,weights,learning_rate)
SimulateOdorB.m:108:O(30,30,2) = (ITIhazard*0.1)*(1-belief_impaired) + 0.0000001*belief_impaired; %omission trial
SimulateOdorB.m:111:O(30,30,1) = (1-ITIhazard*0.1)*(1-belief_impaired) + 1*belief_impaired;
SimulateOdorB.m:125:results = TDlearning(x,O,T_blur,weights,belief_impaired,Weber_fraction,learning_rate);
SimulateOdorC.m:1:function params = SimulateOdorC(simulation_index,Weber_fraction,jitter,belief_impaired,weights,learning_rate)
SimulateOdorC.m:108:O(30,30,2) = (ITIhazard*0.1)*(1-belief_impaired) + 0.0000001*belief_impaired; %omission trial
SimulateOdorC.m:111:O(30,30,1) = (1-ITIhazard*0.1)*(1-belief_impaired) + 1*belief_impaired;
SimulateOdorC.m:124:results = TDlearning(x,O,T_blur,weights,belief_impaired,Weber_fraction,learning_rate);
1:function params = SimulateOdorA_withOmission(simulation_index,Weber_fraction,jitter,belief_impaired,weights,learning_rate)
3:nTrials = 100;
25:ISIs =  find(round(full_ISIpdf*nTrials)>0);
27:ISIdistribution = round(full_ISIpdf*nTrials*0.9);
33:temp = [trialtype zeros(1,round(nTrials*0.1))];
89:T_blur = blur_matrices_inputWeberFraction(T,Weber_fraction);
128:results = TDlearning(x,O,T_blur,weights,belief_impaired,Weber_fraction,learning_rate);
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sw && sed -n 1,60p TDlearning.m
```

```
function [results new_weights] = TDlearning(x,O,T,weights,flatten_belief,Weber_fraction,learning_rate)

% TD learning for partially observable MDP.
% Author: Dr. Samuel J. Gershman
%
% USAGE: results = TD(x,O,T)
%
% INPUTS:
%   x - stimulus timeseries (1 = nothing, 2 = stimulus, 3 = reward)
%   O - [S x S x M] observation distribution: O(i,j,m) = P(x'=m|s=i,s'=j)
%   T - [S x S] transition distribution: T(i,j) = P(s'=j|s=i)
%
% OUTPUTS:
%   results - structure with the following fields:
%               .w - weight vector at each time point (prior to updating)
%               .b - belief state at each time point (prior to updating)
%               .rpe - TD error (after updating)
%
%%
% initialization
[... 34 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "  criterion: Per session, licks from odor onset to reward (or the same span for odor D) against\n    licks in the baseline window of 1 s before odor onset (the baseline the Methods use for\n    spikes; the paper does not give the lick baseline, so this is a standard choice). One-way\n    ANOVA over sessions for each odor and task. Reproduced when all six odor A to C comparisons\n    have p < 0.05 with more licks after the odor, and neither odor D comparison does.",
 "new_string": "  criterion: Per session, anticipatory licks after the odor against baseline licks; one-way ANOVA\n    for each odor and task. The paper gives neither the windows nor the observation unit of this\n    test, so these are open. Windows, readings (a) licks from odor onset to reward against licks\n    in an equal span just before odor onset, (b) lick rates from odor onset to reward against the\n    rate in the 1 s before odor onset (the spike baseline of the Methods). For odor D, which has\n    no reward, the span is odor onset to 2.8 s (the longest ISI, as in Figure S3A), a standard\n    choice. The error df (36 for odors A to C, 41 for odor D) fit neither all sessions of a task\n    as two groups (df 74 and 78, from the 38 and 40 sessions implied by Figure S3A) nor a paired\n    design; readings are (i) all sessions of a task, (ii) sessions of each task and drug\n    separately, and the observation counts used are reported. Reproduced when all six odor A to C\n    comparisons have p < 0.05 with more licks after the odor, and neither odor D comparison does."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    form is not given, a four-parameter logistic is a standard choice). One-way ANOVA of task 1",
 "new_string": "    form is not given, a four-parameter logistic is a standard choice; the trials fitted are not\n    given, odor A trials rewarded at 2.8 s as in Figure S3A and all odor A trials up to their\n    reward are the readings). One-way ANOVA of task 1"
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "  - about: x50, task 2 SalB against saline\n    test: one-way ANOVA\n    statistic: F(1, 38) = 0.42\n    p: 0.52\n  data: dataset",
 "new_string": "  - about: x50, task 2 SalB against saline\n    test: one-way ANOVA\n    statistic: F(1, 38) = 0.42\n    p: 0.52\n  - about: lick rate in each 200 ms epoch after odor A, task 1 SalB against saline\n    test: one-way ANOVA, no correction for multiple comparisons\n    statistic: F(1, 36) < 4.0\n    p: 0.4\n    p_relation: \">\"\n  - about: lick rate in each 200 ms epoch after odor A, task 2 SalB against saline\n    test: one-way ANOVA, no correction for multiple comparisons\n    statistic: F(1, 38) < 4.0\n    p: 0.4\n    p_relation: \">\"\n  - about: slope of licks on time, task 1 SalB against saline (labelled anticipatory licks in the\n      Figure S3F legend)\n    test: one-way ANOVA\n    statistic: F(1, 36) = 0.87\n    p: 0.36\n  - about: slope of licks on time, task 2 SalB against saline (labelled anticipatory licks in the\n      Figure S3F legend)\n    test: one-way ANOVA\n    statistic: F(1, 38) = 0.04\n    p: 0.84\n  - about: sigmoid steepness, task 1 SalB against saline\n    test: one-way ANOVA\n    statistic: F(1, 36) = 0.3\n    p: 0.59\n  - about: sigmoid steepness, task 2 SalB against saline\n    test: one-way ANOVA\n    statistic: F(1, 38) = 0.05\n    p: 0.82\n  data: dataset"
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    drug have p < 0.05 and task 1 x drug p >= 0.05. Neurons without a free water response are\n    left out; with no lick data, all free water deliveries is the other reading.",
 "new_string": "    drug have p < 0.05 and task 1 x drug p >= 0.05. Neurons without a free water response are\n    left out; with no lick data, all free water deliveries is the other reading. The error df of\n    163 with three terms imply 167 neurons of the 172, the same number the df of the Figure S5C\n    ANOVAs imply (see figs5c-odorbc-normalized), which supports leaving 5 neurons out."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    are neuron and odor pairs, B and C pooled, as the degrees of freedom imply. One-way ANOVAs as",
 "new_string": "    are neuron and odor pairs, B and C pooled, as the degrees of freedom imply (the four error df\n    give 82, 85, 80 and 87 neurons per comparison, consistent with 167 of the 172 neurons having a\n    free water response, 40 to 42 of them task 1 saline). One-way ANOVAs as"
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    SalB neurons is not named; the panel's other test is a Wilcoxon test, so the two-sided\n    Wilcoxon rank-sum test is the reading, Bonferroni over all epochs and trial types. A claim\n    of absence; reproduced when no epoch is significant after correction, not reproduced when\n    any is.",
 "new_string": "    SalB neurons is not named, nor the family the Bonferroni correction spans. Readings are the\n    two-sided Wilcoxon rank-sum test (the panel's other test is a Wilcoxon test) and the one-way\n    ANOVA (the test of the Figure S5C comparisons between drugs), each with Bonferroni over all\n    epochs and trial types and over the epochs of each trial type. A claim of absence; reproduced\n    when no epoch is significant after correction, not reproduced when any is."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    negative around the expected reward time. The paper's text does not say whether task 1\n    simulations are also impaired; the code's flag applies to every task, and impairing task 2\n    only (the Methods' wording) is the other reading.",
 "new_string": "    negative around the expected reward time. The impairment acts on task 2 only, as the Methods\n    say; in the code the flag changes the observation matrix of the task 2 simulations (odor A\n    with omissions, odors B and C) and leaves task 1 as intact (SimulateOdorA_withoutOmission.m\n    sets the same values either way)."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "  statement: Impairing timing by blurring the transition matrix flattens task 1 post-reward and\n    pre-reward RPEs, leaves most task 2 simulations with positive slopes, and abolishes omission\n    responses, unlike the data.",
 "new_string": "  statement: Impairing timing by blurring the transition matrix flattens task 1 post-reward RPEs\n    and pre-reward RPEs in both tasks, leaves most task 2 simulations with positive slopes, and\n    abolishes omission responses, unlike the data."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    0.56 for all. Reproduced when, under a reading, the absolute averaged task 1 post-reward and\n    pre-reward slopes are smaller than in the intact run, more than half of task 2 simulations",
 "new_string": "    0.56 for all. Reproduced when, under a reading, the absolute averaged task 1 post-reward slope\n    and the absolute averaged pre-reward slopes of both tasks are smaller than in the intact run,\n    more than half of task 2 simulations"
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the missing claim (Figure S6C to S6E) and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/starkweather-2018.yaml",
 "old_string": "    and the positive-slope count is within tolerance. vta-1 is described as holding 8 mice, so\n    these neurons may not be in it.",
 "new_string": "    and the positive-slope count is within tolerance. vta-1 is described as holding 8 mice, so\n    these neurons may not be in it.\n- id: figs6ce-kord-task1-animal\n  statement: In the task 1 mouse recorded with an mPFC tetrode as well, SalB inhibited the\n    majority of recorded mPFC neurons, so KORD was effective in task 1 too.\n  source: Results, mPFC Inactivation Impaired Dopamine Responses, paragraph 2; Figure S6A to S6E\n    legends\n  quote: We confirmed that KORD inhibited the majority of mPFC neurons in this task 1 animal\n    (Figures S6C–S6E)\n  data: dataset\n  criterion: mPFC units of the one task 1 mouse with a tetrode in the mPFC (Figure S6A), SalB\n    sessions. A neuron is inhibited when its firing rate more than 15 min after injection is below\n    half its baseline rate, the baseline being the first 5 min after SalB injection (Figure S6C to\n    S6E legends). The paper gives no count or test. Reproduced when more than half of these\n    neurons are inhibited. These recordings are not described in vta-1."
}
```

```
The file claims/starkweather-2018.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  tail -c 300 claims/starkweather-2018.yaml; grep -n "^checks\|^schema" claims/starkweather-2018.yaml; ls claims | head; grep -l "^checks:" claims/*.yaml | head -2
```

```
the intact run,
    more than half of task 2 simulations
    have positive slopes, and the averaged odor B and C omission RPE shows no dip below the
    intact run's minimum near the expected time; the paper gives no threshold for abolished, so
    the dip depth is reported against the intact run.
56:schema_version: 2
alasfour-2024.yaml
amjad-2025.yaml
armstrong-2026.yaml
ashworth-2025.yaml
athalye-2023.yaml
azcorra-2023.yaml
bakalar-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
claims/alasfour-2024.yaml
claims/armstrong-2026.yaml
```

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/armstrong-2026.yaml | head -20
```

```
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header. Added that Table S1 assigns Fig. 2I and 2L to animal 480, Fig. 3E, F, Q, R to 489 and Fig. S12 to 589; the header listed 573 alone for Fig. 2I.
  - fig1lm-staged-modulation. The epoch 1 window (-1 to 0 s) was stated as fixed; the paper gives only t < 0. Named the readings -1 to 0 s and -0.5 to 0 s, as fig1n-epoch-rates has them.
  - fig1o-trial-end-ramp. Ramp onset was defined as the suppression minimum without saying the paper does not define it. It now takes the two onset readings of fig4b-ddm-matches-ramp.
  - figs1-running-speed. The SI (Animal preparation) gives the same 21 ± 4 cm/s for habituation day 3. Added this as reading (d), usable only if the dataset holds habituation sessions.
  - fig2a-success-rate. Lateral position relative to t = 0 was stated as fixed; the paper does not set the zero. Named it open, with the readings of fig2b-lateral-spread.
  - fig2i-ft-rt. Table S1 assigns Fig. 2I to 480 ("2IL") as well as 573 ("2EFI"); the criterion named 573 only. Added readings 573, 480 and both pooled.
  - fig2jk-glm-mixed-tuning. The criterion listed 12 variables as "13 regressors plus V_wall". The SI says 13 regressors and then "additionally" V_wall, and names 12 variables with the Results. The criterion now says so, leaves a 13th variable open and fits the 12 named plus V_wall. "Among the strongest" was defined one way only; added the largest mean log likelihood ratio as a second reading.
  - fig2l-running-vs-sitting. The criterion said the animal is not named; Table S1 names 480 ("2IL"). The claim is now judged on 480, with other animals as a variant.
  - fig3-wall-kinematics. The criterion said Table S1 gives 489 for Fig. 3P. Table S1 gives 589 ("3G-P") for Fig. 3P and 489 ("3EFQR") for Fig. 3Q. Corrected, and named both animals as readings for the FT fraction, since the Fig. 3Q legend points to 589's trials.
  - fig3ijkl-whisking-across-epochs. The samp
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/starkweather-2018.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checker. The 16 p-values it flagged are all in the text, printed by the extraction as "N 3 10" with a garbled minus sign for N × 10^-k (Results and legends of Figures 3, 4, 5 and 6); each was read and matches.
  - fig3g-anticipatory-licking. The criterion fixed the windows (and an odor D span "the same as to reward", which odor D lacks) and the observation unit as if the paper gave them. It gives neither. Named the window readings (equal-span counts, or rates against the 1 s before odor onset), set the odor D span to 0 to 2.8 s as a standard choice, and said the error df 36 and 41 fit no design over the 38 and 40 sessions of Figure S3A, with all sessions of a task and each task and drug as readings.
  - figs3-task1-licks-more-sooner. Which trials the sigmoid fits use is not given; named the 2.8 s trials of Figure S3A and all odor A trials as readings.
  - figs3-salb-spares-licking. The criterion tests the epoch lick rates, lick slope and sigmoid steepness, but statistics held only the anticipatory lick and x50 tests. Added the Figure S3B, S3C, S3F and S3I tests, noting that the S3F legend labels the slope tests as anticipatory licks.
  - figs5d-omission-unchanged-by-salb. The test is not named and the Bonferroni family is not given; the criterion chose one of each. Named the rank-sum test and the one-way ANOVA (used between drugs in Figure S5C), each with the correction over all epochs and over each trial type, as readings.
  - figs5c-odorbc-normalized and anova-slopes-task-drug. Added that the error df of the four Figure S5C ANOVAs and of the slope ANOVA all imply 167 of the 172 neurons, which supports leaving out neurons without a free water response.
  - fig7fgh-model-belief-impaired. The criterion said the code's impairment flag applies to every task and named task 2 only as another reading. In the code at d667730, SimulateOdorA_withoutOmission.m sets the same observation matrix whether impaired or not, so only task 2 simulations are impaired, as the Methods say; the second reading was removed.
  - fig7ijk-model-timing-impaired. The paper says pre-reward responses were flattened in both tasks 1 and 2 (Results, Computational Modeling, paragraph 5); the statement and criterion had task 1 only. Both now include task 2.
  - Added claim figs6ce-kord-task1-animal (Results, mPFC Inactivation Impaired Dopamine Responses, paragraph 2; Figure S6C to S6E), a control finding with no claim. Its baseline is the first 5 min after SalB, as the S6C legend says.
  - Open. fig5f-task2-significant-slopes-shift. The two-sided Fisher exact test on the printed counts (saline 1 negative, 9 positive; SalB 9 negative, 7 positive) gives p = 0.037, not the reported 0.041; the conclusion at alpha 0.05 is the same, and the counts may be rounded or the test computed otherwise. The criterion is left as it is.
  - Open. fig2-kord-suppresses-mpfc. The pie charts of Figure 2F print counts (377, 202, 124, 32, and 599 and 156 on the axes of 2H) that cannot be assigned to groups from the extracted text, and the PDF could not be rendered here; the claim rests on the "more than 60%" of the Results.
  - Open. The degrees of freedom of fig4b-odorc-below-latest-odora (F(1, 41)), fig6ab-odorc-above-odorb and fig6cd-omission-dips-intact (F(1, 40) for SalB with 47 neurons; F(1, 47) in the Results) and anova-time-task-drug-interaction (error df 1347) do not follow from the neuron counts; the criteria already name the readings and ask for the counts used.
EOF
python tools/claims_check.py claims/starkweather-2018.yaml paper/10.1016-j.neuron.2018.03.036.txt 2>&1 | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short; python tools/claims_check.py claims/starkweather-2018.yaml paper/10.1016-j.neuron.2018.03.036.txt 2>&1 | grep -v "VALUE NOT FOUND" ; rm -rf $TMPDIR/sw
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file and it is fit for an attempt: the new `checks` entry says `ready: true`. Nothing is committed.

**Checker:** `claims/starkweather-2018.yaml: 32 claims, 32 quotes, 52 statistical values, 16 problems`. All 16 problems are "value not found" flags on p-values. Each one is in the text, where the extraction prints "× 10⁻ᵏ" as "3 10" plus a garbled minus sign. I read and matched every one. All quotes pass word for word.

I also read the paper's model code (github.com/cstarkweather/Starkweather2018 at commit d667730). It confirms the settings the file gives: gamma 0.93, alpha 0.1, 500 training sessions of 50 trials, noise at SNR 12, and slopes as straight-line fits of the reward-time RPE.

**Changes, by claim:**
- **fig3g-anticipatory-licking:** the criterion presented its windows and observation unit as the paper's, and gave odor D a "span to reward" although odor D has no reward. The paper gives neither. I named the readings for the windows (equal-span counts, or rates against the 1 s before odor onset) and set the odor D span to 0–2.8 s as a standard choice. I also noted that the error df (36 and 41) fit no design over the 38 and 40 sessions per task that Figure S3A implies.
- **figs3-task1-licks-more-sooner:** the paper does not say which trials the sigmoid fits use. I named two readings: the 2.8 s trials, or all odor A trials.
- **figs3-salb-spares-licking:** added the tests the criterion relies on but the statistics left out: epoch lick rates, lick slope and sigmoid steepness (Figure S3B, C, F, I).
- **figs5d-omission-unchanged-by-salb:** the paper names neither the test nor the group the Bonferroni correction covers. I named two tests (rank-sum and one-way ANOVA) and two correction groups (all epochs, or each trial type) as readings.
- **figs5c-odorbc-normalized** and **anova-slopes-task-drug:** added that the error df of all five ANOVAs imply 167 of the 172 neurons. That supports leaving out neurons without a free water response.
- **fig7fgh-model-belief-impaired:** the file said the code impairs every task. In the code the impairment changes nothing in task 1, so only task 2 is impaired, as the Methods say. I removed the false second reading.
- **fig7ijk-model-timing-impaired:** the paper says pre-reward RPEs flatten in both tasks, but the statement and criterion had task 1 only. Both now include task 2.
- **New claim figs6ce-kord-task1-animal:** KORD inhibited most mPFC neurons in the task 1 mouse (Figure S6C to S6E). This control finding had no claim. Its baseline is the first 5 min after SalB, as the legend says.

**Still open:**
- **fig5f-task2-significant-slopes-shift:** a Fisher exact test on the printed counts gives p = 0.037, not the reported 0.041. The result is the same at 0.05, so I left the claim as it is.
- **fig2-kord-suppresses-mpfc:** the counts in Figure 2's pie charts (377, 202, 124, 32) can't be assigned to groups from the extracted text, and the PDF could not be rendered here. The claim rests on the Results' "more than 60%".
- **Degrees of freedom:** in fig4b-odorc-below-latest-odora, fig6ab-odorc-above-odorb, fig6cd-omission-dips-intact and anova-time-task-drug-interaction (error df 1347) they don't follow from the neuron counts. The criteria already name the readings and ask for the counts used.

## End of run

30 turns, 5 minutes, $2.00 at API prices, result: success.
