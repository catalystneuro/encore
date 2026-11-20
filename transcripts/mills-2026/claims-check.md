# mills-2026 · claims-check · run 44705643799

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ claims/ docs/; grep -n "Reader" -A60 docs/protocol.md | head -150; cat claims/mills-2026.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i mills; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/mills-2026.yaml
```

```
<persisted-output>
Output too large (56.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f6a95b7b-465b-4dec-b436-a42b7f5cc105/tool-results/bgbf8rlds.txt

Preview (first 2KB):
# Claims for Mills, Lee, Howe, Li et al. (2026), "Amygdalostriatal transition zone neurons encode
# sustained cue responses to guide defensive behaviors", Neuron, doi:10.1016/j.neuron.2026.08.012,
# tested on DANDI:001203.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-20, protocol pilot-18 as stated in docs/protocol.md.
#
# Text read. paper/10.1016-j.neuron.2026.08.012.txt, from Europe PMC (PMC13592531, NIHMS2206276):
# the author-accepted manuscript under CC BY, which its header says is the publisher's accepted
# version, with the Summary, Results with figure legends 1 to 6, Discussion, Resource
# availability, STAR Methods and Key resources table. The supplement read is MMC1 (the legends of
# Figures S1 to S17, as text extracted from its PDF). MMC2 (Data S1, 46 pages) is image only: per
# mouse histology of electrode, probe, fiber and virus placements, with the mice left out for
# poor targeting or CeA expression. Its first pages were looked at to identify it; no claim rests
# on it, but an author can use it to match exclusions. Figures themselves were not looked at.
#
# Code read. https://github.com/Tyelab/Mills-et-al-2026 at commit
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
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
[... 754 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/mills-2026.yaml"
}
```

```
1	# Claims for Mills, Lee, Howe, Li et al. (2026), "Amygdalostriatal transition zone neurons encode
2	# sustained cue responses to guide defensive behaviors", Neuron, doi:10.1016/j.neuron.2026.08.012,
3	# tested on DANDI:001203.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-20, protocol pilot-18 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.1016-j.neuron.2026.08.012.txt, from Europe PMC (PMC13592531, NIHMS2206276):
8	# the author-accepted manuscript under CC BY, which its header says is the publisher's accepted
9	# version, with the Summary, Results with figure legends 1 to 6, Discussion, Resource
10	# availability, STAR Methods and Key resources table. The supplement read is MMC1 (the legends of
11	# Figures S1 to S17, as text extracted from its PDF). MMC2 (Data S1, 46 pages) is image only: per
12	# mouse histology of electrode, probe, fiber and virus placements, with the mice left out for
13	# poor targeting or CeA expression. Its first pages were looked at to identify it; no claim rests
14	# on it, but an author can use it to match exclusions. Figures themselves were not looked at.
15	#
16	# Code read. https://github.com/Tyelab/Mills-et-al-2026 at commit
17	# 1fee26d1a5bb8179c44b02b24632d3d872e0b801 (2026-09-08), linked in Data and code availability. It
18	# holds five Python analyses of the electrophysiology, all reading one MATLAB file (discAll.mat,
19	# not in the repository): the CS decoding of Figure 3H (named "fig4H" in the code), freezing and
20	# darting decoding, the GLM of Figures 3I to 3M (named "fig4G"), the average trajectories of
[... 1117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; python tools/claims_check.py claims/mills-2026.yaml paper/10.1016-j.neuron.2026.08.012.txt 2>&1 | tail -20; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2026.08.012.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (46 claims, 0 problems). Reading the rest of the paper now (Methods and supplement legends).

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1016-j.neuron.2026.08.012.txt').read()
import os
d=os.environ['TMPDIR']
for i in range(0,len(t),45000):
    open(f'{d}/p{i//45000}.txt','w').write(t[i:i+45000].replace('. ','.\n'))
print(len(t))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p1.txt"
}
```

```
1	ues, rather than simply motor output.
2	Analysis of subsecond behavior during electrophysiology recordings revealed that ASt neuron firing was not aligned with individual bouts of either freezing or darting, and logistic regression decoding and GLM analyses further showed that ASt activity predominantly represented the conditioned cue rather than specific behaviors.
3	Inhibition of Drd2 + ASt neurons also reduced both freezing and darting to the cue, rather than driving a unidirectional change in motor output.
4	Together, these findings suggest the ASt does not encode individual defensive movements directly but rather represents the threat cue itself to direct behavioral responses.
5	The ASt in models of amygdala and striatum function Importantly, our findings complement rather than contradict the large body of existing work examining amygdala circuits mediating learned associations.
6	Many studies have shown outputs from the CeA to the periaqueductal gray (PAG) are essential for expression of conditioned fear, 3 , 5 , 6 and ASt neurons likely act in concert with these canonical circuits to drive defensive behavior.
7	However, in some cases the ASt and amygdala may have distinct roles.
8	The BLA and CeA are essential for contextual fear conditioning, 70 , 71 but our calcium imaging and inhibition experiments both showed that ASt neurons did not appear to play a role in conditioned responses to contexts.
9	Interestingly, the hippocampus, a key structure for spatial and contextual learning, 72 , 73 projects to the BLA but not the ASt.
10	74 The ASt may therefore be specialized for responses to acute sensory cues, while amygdala circuits play a central role in responses to context.
11	How does the ASt fit in the hierarchy of established circuit models for directing behavior? With respect to the amygdala, two major models are possible.
12	First, the ASt may be “downstream” of the amygdala complex.
13	The ASt receives robust input from the LA, 38 , 39 and so it is poss
[... 265 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.txt"
}
```

```
1	ell below −2 (inhibited).
2	Proportions of neurons excited or inhibited were compared across regions or groups using chi-square tests, with each family of comparisons corrected by the Holm-Bonferroni method.
3	The number of animals and the number of neurons recorded is specified in the figures, the figure legends, and the text.
4	Statistical analysis of behavior Behavioral analysis of open field test, elevated plus maze, and real-time place preference task Behavioral performance was recorded by digital cameras positioned above the test arena.
5	Ethovision XT software (Noldus, Wageningen, Netherlands) was used to track mouse location.
6	For the open field test, overall locomotion and time in the edge and center regions were quantified per epoch, and for the elevated plus maze, time in the open and closed arms was quantified per epoch; these were analyzed by two-way ANOVA (group × laser epoch).
7	For real-time place preference, the percentage of time spent on the ON and OFF sides was quantified across three time bins and analyzed separately for each genotype by two-way repeated-measures ANOVA (side × time bin, with time bin as the repeated measure).
8	All analyses were followed by Bonferroni post hoc tests.
9	Behavioral analysis of two-tone discrimination task To automatically detect animal defensive behaviors, SLEAP 62 was used to estimate animal poses in behavioral videos.
10	A training data set of over 15,000 frames was labeled using a 14-point skeleton to represent the mouse (nose, left ear tip, left ear base, right ear base, right ear tip, skull base, shoulders, haunch, tail base, tail segment, left arm, right arm, right leg, and left leg).
11	This data set was used to train a bottom-up model; in this model, first the animal is detected using a centroid model, then the location of each labeled body part is identified using a centered instance model.
12	For quantification of freezing, our defined criteria was when the total displacement of ALL mouse body points 
[... 662 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001; grep -n -m3 "Figure S1\b\|Supplementary\|MMC1\|S5\." p3.txt p4.txt p5.txt | head; wc -c p*.txt
```

```
p3.txt:337:Associated Data Supplementary Materials MMC1 MMC2 Data Availability Statement snRNA-seq data have been deposited at GEO: GSE211437 .
p4.txt:796:##### Supplement: NIHMS2206276-supplement-MMC1.pdf
p4.txt:840:Figure S1.
p4.txt:940:Figure S5.
 45221 p0.txt
 45293 p1.txt
 45334 p2.txt
 45091 p3.txt
 45164 p4.txt
 12628 p5.txt
238731 total
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.txt",
 "offset": 796
}
```

```
796	##### Supplement: NIHMS2206276-supplement-MMC1.pdf
797	
798	=== page 1 ===
799	Neuron, Volume 115 
800	Supplemental information 
801	Amygdalostriatal transition zone neurons 
802	encode sustained cue responses 
803	to guide defensive behaviors 
804	Fergil Mills, Christopher R.
805	Lee, James R.
806	Howe, Hao Li, Maria N.
807	Keisler, Shan 
808	Shao, Felix H.
809	Taschbach, Mackenzie E.
810	Lemieux, Faith Aloboudi, Jesse White, May G.
811	
812	Chan, Matilde Borio, Laurel R.
813	Keyes, Hannah S.
814	Chen, Fabiha Bushra, Gates P.
815	
[... 389 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.txt"
}
```

```
1	A, Drd2a-Cre ChR2: effect of side F(1,10) = 
2	1.951, p = 0.1927; eYFP: effect of side F(1,30) = 0.3750, p = 0.5449.
3	Drd2a-Cre ChR2: n = 6 mice, eYFP: n = 16 mice).
4	 
5	(G-H) Optogenetic stimulation of Drd1a+ or Drd2+ ASt neurons had no effect on time spent in open arms of an elevated 
6	plus maze.
7	(Two-way ANOVA, Drd1a-Cre, group x laser interaction F(1,20) = 0.4057, p = 0.5314.
8	Drd1a-Cre ChR2: n = 5 
9	mice, eYFP: n = 7 mice; Two-way ANOVA, Drd2a-Cre, group x laser interaction F(1,40) = 0.9907, p = 0.3256.
10	Drd2a-Cre 
11	ChR2: n = 6 mice, eYFP: n = 16 mice).
12	Data presented as mean ±SEM.
13	
14	
15	=== page 15 ===
16	14 
17	Figure S13.
18	Targeting of ASt neurons and behavioral validation for in vivo calcium imaging.
19	
20	(A-B) Histologically verified GRIN lens implant locations and AAV1-Syn-FLEX-GCaMP7f viral injection sites in recording 
[... 265 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.txt",
 "offset": 330
}
```

```
330	10.48550/arXiv.1802.03426.
331	125.
332	Tweedie S, Braschi B, Gray K, Jones TEM, Seal RL, Yates B, and Bruford EA (2021).
333	Genenames.org : the HGNC and VGNC resources in 2021.
334	Nucleic Acids Res.
335	49, D939–D946.
336	10.1093/nar/gkaa980.
337	Associated Data Supplementary Materials MMC1 MMC2 Data Availability Statement snRNA-seq data have been deposited at GEO: GSE211437 .
338	Raw and processed data are made freely available at https://dandiarchive.org/dandiset/001203 .
339	Code freely available from our laboratory GitHub at https://github.com/Tyelab/Mills-et-al-2026 .
340	
341	[HYPERLINKS]
342	https://creativecommons.org/licenses/by/4.0/
343	10.1016/j.neuron.2026.08.012
344	https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE211437
345	https://dandiarchive.org/dandiset/001203
346	https://github.com/Tyelab/Mills-et-al-2026
347	https://miniscopeparts.com/
348	http://billkarsh.github.io/SpikeGLX/
349	http://miniscope.org/
[... 499 more lines not kept]
```

**Agent**

Read the full paper and supplement legends. Now checking registry conventions (link claims by readers, `checks` format) and whether the code repo is reachable.

**Agent calls Bash**

```bash
cd  grep -l "kind: link" claims/*.yaml | head; echo ---; grep -n -A12 "^checks:" claims/*.yaml | head -40; echo ---; timeout 30 git ls-remote https://github.com/Tyelab/Mills-et-al-2026 2>&1 | head -3
```

```
claims/amjad-2025.yaml
claims/bech-2026.yaml
claims/bennett-2024.yaml
claims/berg-2020.yaml
claims/brinke-2017.yaml
claims/buccino-2020.yaml
claims/burman-2023.yaml
claims/calvigioni-2023.yaml
claims/carcea-2021.yaml
claims/chandravadia-2020.yaml
---
claims/alasfour-2024.yaml:645:checks:
claims/alasfour-2024.yaml-646-- date: 2026-11-10
claims/alasfour-2024.yaml-647-  kind: agent
claims/alasfour-2024.yaml-648-  model: claude-opus-5-5
claims/alasfour-2024.yaml-649-  ready: true
claims/alasfour-2024.yaml-650-  changes:
claims/alasfour-2024.yaml-651-  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
claims/alasfour-2024.yaml-652-  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
claims/alasfour-2024.yaml-653-  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -B2 -A6 "kind: link" claims/bennett-2024.yaml | head -20; cd $TMPDIR && git clone -q https://github.com/Tyelab/Mills-et-al-2026 code && cd code && git checkout -q 1fee26d1a5bb8179c44b02b24632d3d872e0b801 && find . -name "*.py" | head -40
```

```
claims:
- id: link-code-tables
  kind: link
  statement: The 87 sessions the paper's code lists as passing ephys QC are sessions of the dandiset,
    and for them the code's units table agrees with the dandiset's units (unit ids, counts per session,
    quality metrics and receptive-field p values).
  source: STAR Methods, Key resources table and Data and code availability; DynamicGating_ephys_metrics.ipynb
    and metadata_tables/units_table.csv at commit 3c09a0dc
  quote: Analysis code used in this paper is available here
./tests/test_repository.py
./scripts/__init__.py
./scripts/trajectories/__init__.py
./scripts/trajectories/trajectories_2s_rev_2025_10ms.py
./scripts/trajectories/trajectory_comparison_plots_v3.py
./scripts/trajectories/trajectories_rev_2025.py
./scripts/trajectories/average_trajectory_utils.py
./scripts/build_notebooks.py
./scripts/fig4H/decode_tone_2025.py
./scripts/notebook_utils/fig4h_all_decoding_workflow.py
./scripts/notebook_utils/__init__.py
[... 13 more lines not kept]
```

**Agent**

Code repo is reachable at the cited commit; spot-checking the code claims the criteria rely on.

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -n "50\b\|firing_rate\|mean_rate\|< *50" scripts/utils/discall.py | head -20; echo ---TRAJ; grep -n "0\.9\|explained\|PCA\|group\|unpaired\|paired" scripts/trajectories/trajectories_rev_2025.py | head -40
```

```
145:    maximum_firing_rate_hz: float = 50.0,
172:    firing_rates_hz = spike_counts / durations
173:    high_hz_filter = firing_rates_hz < maximum_firing_rate_hz
189:        f"ASt paired units after <{maximum_firing_rate_hz:g} Hz filter: "
196:        "firingRateHz": firing_rates_hz,
---TRAJ
14:from sklearn.decomposition import PCA
122:        Filtered spikes, behavior, events, and group data
127:    group = db["group"]
135:        m["unitLogis"]["paired"] & 
163:    group_filtered = np.array(list(compress(group, animal_filter)))
165:    return spikes_roi, beh_roi, events_filtered, group_filtered
444:        PCA components and transformed data
448:    # Concatenate data for PCA
454:    print(f"Using {data_for_pca.shape[0]} timepoints × {data_for_pca.shape[1]} animals for PCA")
456:    # Fit PCA
457:    pca = PCA()
461:    n_dim = np.where(np.cumsum(pca.explained_variance_ratio_) >= 0.90)[0][0] + 1
462:    print(f"Using {n_dim} PCA components to explain 90% of variance")
484:        PCA-transformed neural data
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; f=scripts/fig4G/glm_variance_partitioning_paired_vs_unpaired_parallel.py; grep -n "fisher\|alternative\|>= *\|abs(\|perm_p\|p_cs\|mannwhitney" $f | head -40
```

```
23:from scipy.stats import mannwhitneyu
24:from scipy.stats import fisher_exact
169:            trial_spikes = neuron_spikes[(neuron_spikes >= trial_start) & (neuron_spikes < trial_end)]
171:            spike_bins = spike_bins[(spike_bins >= 0) & (spike_bins < n_time_bins)]
200:            frame_mask = (f2s >= bin_start_s) & (f2s < bin_end_s)
228:    if llnull >= 0:
356:    p_value = np.mean(np.abs(null_coefs[valid]) >= np.abs(real_cs_coef))
411:    p_value = np.mean(null_joint >= real_joint)
756:        'median_abs_cs_coef': animals['cs_coef'].apply(lambda x: np.median(np.abs(x))),
780:def safe_mannwhitneyu(x, y, alternative='two-sided'):
786:    return mannwhitneyu(x, y, alternative=alternative)
790:u, p = safe_mannwhitneyu(paired_animal['pct_cs_responsive'].values,
792:                         alternative='greater')
799:u2, p2 = safe_mannwhitneyu(paired_animal['median_abs_cs_coef'].values,
801:                           alternative='greater')
808:u3, p3 = safe_mannwhitneyu(paired_animal['median_delta_mfi_cs'].values,
810:                           alternative='greater')
817:u4, p4 = safe_mannwhitneyu(paired_animal['median_cv_delta_dev_cs'].values,
819:                           alternative='greater')
832:odds_ratio, fisher_p = fisher_exact(contingency, alternative='greater')
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -n "min_units\|min_trials\|>= *10\|> *10\|30\|wilcoxon\|n_iter\|100" scripts/notebook_utils/pairwise_trajectory_workflow.py scripts/trajectories/trajectory_comparison_plots_v3.py | head -30; echo ---DEC; grep -n "> *10\|29\|n_shuffle\|20\|wilcoxon\|mannwhitney\|liblinear\|StratifiedKFold" scripts/notebook_utils/fig4h_decoding_workflow.py scripts/fig4H/decode_tone_2025.py | head -30
```

```
scripts/notebook_utils/pairwise_trajectory_workflow.py:46:CACHE_SIGNATURE = {'roi': 'ASt', 'groups': ['paired', 'unpaired'], 'minimum_neurons': 10, 'minimum_trials': 30, 'bin_size_s': 0.1, 'trial_window_s': [-20, 40], 'pca_components': 3, 'pca_trials_per_condition': 30, 'smoothing_sigma': 5, 'random_seed': 42}
scripts/notebook_utils/pairwise_trajectory_workflow.py:468:MIN_TRIALS = 30  # Minimum number of trials per condition
scripts/notebook_utils/pairwise_trajectory_workflow.py:469:BIN_SIZE = 0.1  # 100ms bins
scripts/notebook_utils/pairwise_trajectory_workflow.py:478:N_TRIALS_FOR_PCA = 30  # Number of trials for fitting PCA
scripts/notebook_utils/pairwise_trajectory_workflow.py:717:        c=color1, marker='^', s=100, edgecolors='black', linewidths=1.5,
scripts/notebook_utils/pairwise_trajectory_workflow.py:722:        c=color2, marker='^', s=100, edgecolors='black', linewidths=1.5,
scripts/notebook_utils/pairwise_trajectory_workflow.py:729:        c=color1, marker='s', s=100, edgecolors='black', linewidths=1.5,
scripts/notebook_utils/pairwise_trajectory_workflow.py:734:        c=color2, marker='s', s=100, edgecolors='black', linewidths=1.5,
scripts/notebook_utils/pairwise_trajectory_workflow.py:785:    plt.savefig(output_file_png, dpi=300, bbox_inches='tight')
scripts/notebook_utils/pairwise_trajectory_workflow.py:975:    print(f"Bin size: {BIN_SIZE * 1000:.0f} ms")
scripts/notebook_utils/pairwise_trajectory_workflow.py:1156:            print(f"    PCs to explain ≥{VARIANCE_THRESHOLD*100:.0f}% variance: {n_components_explained}")
scripts/trajectories/trajectory_comparison_plots_v3.py:51:MIN_TRIALS = 30  # Minimum number of trials per condition
scripts/trajectories/trajectory_comparison_plots_v3.py:52:BIN_SIZE = 0.1  # 100ms bins
scripts/trajectories/trajectory_comparison_plots_v3.py:61:N_TRIALS_FOR_PCA = 30  # Number of trials for fitting PCA
scripts/trajectories/trajectory_comparison_plots_v3.py:292:        c=color1, marker='^', s=100, edgecolors='black', linewi
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 538,550p scripts/notebook_utils/fig4h_decoding_workflow.py; grep -n "TRAINING_WINDOW\|training_start\|training_end" scripts/notebook_utils/fig4h_decoding_workflow.py | head; grep -n "pairwise\|wilcoxon\|cosine" scripts/notebook_utils/pairwise_trajectory_workflow.py | grep -i "wilcoxon\|n_iter\|iteration" | head
```

```
TIME_VECTOR = np.arange(0, TOTAL_DURATION_S, TIME_BIN_SIZE_S)
TIMEPOINTS_PER_TRIAL = int((ANALYSIS_WINDOW_BEFORE_ONSET_S + ANALYSIS_WINDOW_AFTER_ONSET_S) * SAMPLING_RATE_HZ)
BASELINE_END_INDEX = int(ANALYSIS_WINDOW_BEFORE_ONSET_S * SAMPLING_RATE_HZ)  # Index corresponding to event onset (0s)

# Update the training window to remain from -20 to +18 seconds
TRAINING_WINDOW_BEFORE_ONSET_S = 20  # Time before event onset for training (seconds)
TRAINING_WINDOW_AFTER_ONSET_S = 18   # Time after event onset for training (seconds)

# Update the derived constants for training accordingly
TRAINING_TIMEPOINTS = int((TRAINING_WINDOW_BEFORE_ONSET_S + TRAINING_WINDOW_AFTER_ONSET_S) * SAMPLING_RATE_HZ)
TRAINING_WINDOW_INDICES = slice(BASELINE_END_INDEX - int(TRAINING_WINDOW_BEFORE_ONSET_S * SAMPLING_RATE_HZ), 
                                BASELINE_END_INDEX + int(TRAINING_WINDOW_AFTER_ONSET_S * SAMPLING_RATE_HZ))

543:TRAINING_WINDOW_BEFORE_ONSET_S = 20  # Time before event onset for training (seconds)
544:TRAINING_WINDOW_AFTER_ONSET_S = 18   # Time after event onset for training (seconds)
547:TRAINING_TIMEPOINTS = int((TRAINING_WINDOW_BEFORE_ONSET_S + TRAINING_WINDOW_AFTER_ONSET_S) * SAMPLING_RATE_HZ)
548:TRAINING_WINDOW_INDICES = slice(BASELINE_END_INDEX - int(TRAINING_WINDOW_BEFORE_ONSET_S * SAMPLING_RATE_HZ), 
549:                                BASELINE_END_INDEX + int(TRAINING_WINDOW_AFTER_ONSET_S * SAMPLING_RATE_HZ))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; grep -n "TRAINING_WINDOW_INDICES\|X_train\b\|X_train =" scripts/notebook_utils/fig4h_decoding_workflow.py | head
```

```
548:TRAINING_WINDOW_INDICES = slice(BASELINE_END_INDEX - int(TRAINING_WINDOW_BEFORE_ONSET_S * SAMPLING_RATE_HZ),
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "  criterion: Proportions as in the Figure 1J legend, nuclei of the Drd1a+ or Drd2+ cluster, with\n    those expressing the other receptor counted as dual expressing. The denominator is open;\n    readings, (a) all nuclei in the two MSN clusters, (b) those clusters without the dual\n    expressing nuclei. Reproduced when under one reading both values are within tolerance and\n    the chi-squared tests of ASt against TS and against DS (Holm-corrected) give p < 0.001.",
 "new_string": "  criterion: Proportions as in the Figure 1J legend, nuclei of the Drd1a+ or Drd2+ cluster, with\n    those expressing the other receptor counted as dual expressing. The denominator is all nuclei\n    in the two MSN clusters, dual expressing included, since 71% and 26% sum to 97% and the\n    legend counts dual expressing nuclei as a third class. Reproduced when both values are within\n    tolerance and the chi-squared tests of ASt against TS and against DS (Holm-corrected) give\n    p < 0.001."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "  - quantity: ASt cells labeled Drd1a\n    value: 27\n    tolerance: 2.7\n    unit: percent\n- id: figs4-cdh6-slit2-gradient",
 "new_string": "  - quantity: ASt cells labeled Drd1a\n    value: 27\n    tolerance: 2.7\n    unit: percent\n  criterion: Cells labeled when over the puncta threshold of 6 for a probe, dual labeled when over\n    it for both (STAR Methods, Object identification; Comparison of Drd1a/Drd2 composition).\n    Denominator the cells labeled for Drd1a, Drd2 or both (Figure 1L legend). Pooling is open;\n    readings, (a) cells pooled over mice, (b) the mean of per-mouse proportions. Per mouse and\n    region the log-ratio log(Drd1a-only / Drd2-only), two-tailed paired t-tests, Holm over the\n    three region pairs (STAR Methods). Reproduced when under one reading both values are within\n    tolerance and the ASt against TS and ASt against DS tests give p < 0.05.\n- id: figs4-cdh6-slit2-gradient"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F(7, 16) = 22.65\n    p: 3.6e-7\n    n: 3 mice\n- id: figs5-ephys-mice-discriminate",
 "new_string": "    statistic: F(7, 16) = 22.65\n    p: 3.6e-7\n    n: 3 mice\n  criterion: Per mouse and region, the share of DAPI cells labeled for each gene at 3 or more\n    puncta (STAR Methods, Object identification). Eight regions (df 7, 16); the text names ASt,\n    CeA, LA, DS and TS(v), TS(m), TS(d) (Figure S4A), and the eighth is not named. One-way ANOVA\n    over regions with Tukey's test (Figure S4 legend). Reproduced when for each gene the ANOVA\n    gives p < 0.05, Tukey puts ASt above TS(d) and above CeA at p < 0.05, ASt against LA is not\n    significant, and the region means fall in the order ASt > TS(v) > TS(m) > TS(d) > DS. The\n    ordering of means is this file's reading of \"decreasing in a dorsoventral gradient\"; the paper\n    reports no test of it.\n- id: figs5-ephys-mice-discriminate"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    The tree is cut into seven clusters. A cluster is sustained when its mean CS-shock z over\n    0.1 to 19 s is above 1 and its mean over the last 5 s of the cue is above half its mean\n    over the first 5 s. Reproduced",
 "new_string": "    The number of clusters is not stated: the Results name clusters 1 to 7, so the tree is cut\n    into seven, and eight is run as a variant in case the figure holds more. A cluster is\n    sustained when its mean CS-shock z over 0.1 to 19 s is above 1 and its mean over the last\n    5 s of the cue is above half its mean over the first 5 s; both thresholds are choices made\n    here, as the paper defines \"sustained\" only by eye. Reproduced"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F (2, 547) = 15.57\n    p: 0.0001\n    p_relation: \"<\"\n  - about: CS-reward sustained, region\n    test: one-way ANOVA with region as factor\n    statistic: F (2, 547) = 16.38\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: As fig2o-ast-greater-cs-shock-responses, for CS-reward. Reproduced when both ANOVAs\n    give p < 0.0001 and the mean ASt phasic z to CS-reward is above 0 by a one-sample t-test at\n    p < 0.05. The paper",
 "new_string": "    statistic: F (2, 547) = 15.57\n    p: 0.0001\n    p_relation: \"<\"\n    n: 193 ASt, 212 TS and 145 CeA neurons\n  - about: CS-reward sustained, region\n    test: one-way ANOVA with region as factor\n    statistic: F (2, 547) = 16.38\n    p: 0.0001\n    p_relation: \"<\"\n    n: 193 ASt, 212 TS and 145 CeA neurons\n  criterion: As fig2o-ast-greater-cs-shock-responses, for CS-reward. Reproduced when both ANOVAs\n    give p < 0.0001 and the mean ASt phasic z to CS-reward is above 0 by a one-sample t-test at\n    p < 0.05. The paper gives no test for \"robust phasic responses\"; the one-sample t-test is a\n    choice made here. The paper"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "  criterion: As the code does (scripts/trajectories/trajectories_rev_2025.py at the commit read),\n    following the STAR Methods (Neural trajectory analysis). Paired ASt units, 100 ms bins, -20 to\n    40 s around each CS onset; per animal, each neuron z-scored over all its trials and bins,\n    averaged per CS type, all animals' neurons stacked; PCA on the concatenated averages, keeping\n    the components that explain 90% of variance; Euclidean distance between the CS-shock and\n    CS-reward projections per bin. The paper gives no test. Reproduced when the mean distance over\n    0 to 18 s exceeds the largest distance in the -20 to 0 s baseline. The Methods say the PCA\n    includes paired and unpaired animals; the code's version for Figure 2Q is shown, and a PCA\n    over both groups is a variant.",
 "new_string": "  criterion: From the STAR Methods (Neural trajectory analysis), with details they leave open from\n    the code (scripts/trajectories/trajectories_rev_2025.py at the commit read). ASt units, 100 ms\n    bins, -20 to 40 s around each CS onset; per animal, each neuron z-scored over all its trials\n    and bins, averaged per CS type, all animals' neurons stacked; one PCA on the concatenated\n    averages of paired and unpaired animals, as the Methods say; Euclidean distance between the\n    paired CS-shock and CS-reward projections per bin in the complete principal component space,\n    as the Methods say. The code fits the PCA on paired animals only and keeps the components\n    that explain 90% of variance; that is run as a variant. The paper gives no test. Reproduced\n    when the mean distance over 0 to 18 s exceeds the largest distance in the -20 to 0 s\n    baseline; this threshold is a choice made here."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    cosine similarity per bin; averaged over 0 to 18 s. Animals as in the code (ASt, at least 10\n    units, at least 30 trials per CS; 8 paired and 3 unpaired animals in its printout).",
 "new_string": "    cosine similarity per bin; averaged over 0 to 18 s. Animals as in the code that plots the\n    example pairs (pairwise_trajectory_workflow.py; ASt, at least 10 units, at least 30 trials\n    per CS; 8 paired and 3 unpaired animals in its printout); the code holds no statistics for\n    Figure S8E-F, so this selection is the nearest the code gives, not the selection of the test."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    shock-reward lower at p < 0.01 and the unpaired group does not show it at p < 0.05. Vectors",
 "new_string": "    shock-reward lower at p < 0.01 and the unpaired group does not show it at p < 0.05. With 3\n    unpaired animals a per-animal signed-rank test cannot reach p < 0.05, so under readings (a)\n    and (b) the unpaired part cannot fail; the unpaired effect size is reported. Vectors"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "  - quantity: mice in the high group\n    value: 8\n    tolerance: 0\n  - quantity: mice in the low group\n    value: 7\n    tolerance: 0",
 "new_string": "  - quantity: mice in the high group\n    value: 8\n    tolerance: 0.8\n  - quantity: mice in the low group\n    value: 7\n    tolerance: 0.7"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F (1,32) = 10.48\n    p: 0.0028\n    n: 8 ChR2 and 10 eYFP mice",
 "new_string": "    statistic: F (1,32) = 10.48\n    p: 0.0028\n    n: 8 ChR2 and 10 eYFP mice\n  criterion: Freezing per mouse in laser ON and OFF epochs of the open field (3 to 6 and 9 to 12\n    min ON; STAR Methods, Open field test), two-way ANOVA group by laser epoch with Bonferroni\n    post hoc tests (STAR Methods, Statistical analysis of behavior). How freezing was scored in\n    the open field (Ethovision settings) is not given. Reproduced when the interaction gives\n    p < 0.05 and the post hoc test has ChR2 freezing higher in ON than OFF epochs at p < 0.05."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F(1,18) = 0.2911\n    p: 0.5961\n    n: 10 eYFP mice",
 "new_string": "    statistic: F(1,18) = 0.2911\n    p: 0.5961\n    n: 10 eYFP mice\n  criterion: Percentage of time on the ON and OFF sides in three time bins of the 30 min session,\n    two-way repeated measures ANOVA (side by time bin) for each group (STAR Methods, Statistical\n    analysis of behavior). Reproduced when the ChR2 effect of side gives p < 0.05 with less time\n    on the ON side and the eYFP effect of side does not give p < 0.05."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    p = 0.0039 for paired, p = 0.5 for unpaired), shown as a variant. Reproduced when the paired\n    mice's accuracies exceed chance by the Mann-Whitney U test at p < 0.01 and the unpaired\n    mice's do not at p < 0.05.",
 "new_string": "    p = 0.0039 for paired, p = 0.5 for unpaired), shown as a variant. Reproduced when the paired\n    mice's accuracies exceed chance by the Mann-Whitney U test at p < 0.01 and the unpaired\n    mice's do not at p < 0.05. With 3 unpaired mice a two-sided Mann-Whitney U test of their\n    accuracies against their chance values cannot reach p < 0.05, so the unpaired part cannot\n    fail; the unpaired accuracy above chance is reported."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    dropped; CS p-value from 1,000 trial-level shuffles of CS labels, Benjamini-Hochberg at 0.05\n    within group.",
 "new_string": "    dropped; CS p-value from 1,000 trial-level shuffles of CS labels, Benjamini-Hochberg at 0.05\n    within group. The Methods call the CS p-value two-sided but write it as the share of\n    permutations with the permuted coefficient at or above the observed one, which is one-sided;\n    the code takes the share with |permuted| at or above |observed| (line 356), which settles it\n    as two-sided. The one-sided formula is run as a variant."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F (1,10) = 9.117\n    p: 0.0129\n    n: 6 ChR2 Drd2-Cre mice",
 "new_string": "    statistic: F (1,10) = 9.117\n    p: 0.0129\n    n: 6 ChR2 Drd2-Cre mice\n  criterion: As fig3b-ast-activation-freezing for the open field (ON epochs 8 to 12 and 20 to 24 min\n    in the Drd1a-Cre and Drd2-Cre cohorts; STAR Methods, Open field test) and as\n    fig3c-ast-activation-avoidance for real-time place preference, in Drd2-Cre mice. Reproduced\n    when the open field interaction gives p < 0.05 with ChR2 freezing higher in ON epochs, and the\n    ChR2 effect of side gives p < 0.05 with less time on the ON side."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: t 19 = 2.235\n    p: 0.038\n    n: 8 NpHR and 13 eYFP mice",
 "new_string": "    statistic: t 19 = 2.235\n    p: 0.038\n    n: 8 NpHR and 13 eYFP mice\n  criterion: Per mouse, total defensive behavior (freezing plus darting) during CS-shock on laser ON\n    trials against laser OFF trials (STAR Methods, Two-tone discrimination tasks; Figure 6C), and\n    NpHR against eYFP mice by Student's t test. The per-mouse measure is open; readings, (a) the\n    percent change from OFF to ON, as Figure S16 reports for freezing and darting, (b) the\n    difference ON minus OFF. Reproduced when under one reading the test gives p < 0.05 with the\n    larger reduction in NpHR mice. The NpHR mean percent change is reported against the\n    Discussion's \"nearly 50%\", which is not judged."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: t19 = 2.097\n    p: 0.0496\n    n: 8 NpHR and 13 eYFP mice",
 "new_string": "    statistic: t19 = 2.097\n    p: 0.0496\n    n: 8 NpHR and 13 eYFP mice\n  expected:\n  - quantity: NpHR change in freezing, laser ON against OFF\n    value: -40.4\n    tolerance: 6.4\n    unit: percent\n  - quantity: eYFP change in freezing, laser ON against OFF\n    value: -16.3\n    tolerance: 7.9\n    unit: percent\n  - quantity: NpHR change in darting, laser ON against OFF\n    value: -48.9\n    tolerance: 3.5\n    unit: percent\n  - quantity: eYFP change in darting, laser ON against OFF\n    value: 3.7\n    tolerance: 19.4\n    unit: percent\n  criterion: Per mouse, percent change in freezing and in darting (STAR Methods, Behavioral analysis\n    of two-tone discrimination task) during CS-shock from laser OFF to laser ON trials (Figure\n    S16H and S16J); Student's t-tests of NpHR against eYFP mice. Tolerances are the SEMs the\n    legends give. Reproduced when both tests give p < 0.05 with the larger reduction in NpHR mice\n    and the four group means are within tolerance."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: t 19 = 0.809\n    p: 0.428\n  criterion",
 "new_string": "    statistic: t 19 = 0.809\n    p: 0.428\n    n: 8 NpHR and 13 eYFP mice\n  criterion"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: F (1,32) = 0.011\n    p: 0.9167\n  - about: real-time place preference, NpHR effect of side\n    test: two-way RM ANOVA\n    statistic: F(1,8) = 0.6896\n    p: 0.4304\n  - about: elevated plus maze\n    test: two-way ANOVA, group x laser interaction\n    statistic: F (1,32) = 0.011\n    p: 0.9177\n  - about: contextual fear, day 2\n    test: Student's t test\n    statistic: t 16 = 0.395\n    p: 0.6984",
 "new_string": "    statistic: F (1,32) = 0.011\n    p: 0.9167\n    n: 5 NpHR and 13 eYFP mice\n  - about: real-time place preference, NpHR effect of side\n    test: two-way RM ANOVA\n    statistic: F(1,8) = 0.6896\n    p: 0.4304\n    n: 5 NpHR mice\n  - about: elevated plus maze\n    test: two-way ANOVA, group x laser interaction\n    statistic: F (1,32) = 0.011\n    p: 0.9177\n    n: 5 NpHR and 13 eYFP mice\n  - about: contextual fear, day 2\n    test: Student's t test\n    statistic: t 16 = 0.395\n    p: 0.6984\n    n: 5 NpHR and 13 eYFP mice"
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mills-2026.yaml",
 "old_string": "    statistic: t13 = 0.137\n    p: 0.893\n  - about: port entry during CS-reward\n    test: Student's t-test\n    statistic: t13 = 0.493\n    p: 0.63\n  criterion: A claim of absence, on the paper's two Student's t-tests at p < 0.05.",
 "new_string": "    statistic: t13 = 0.137\n    p: 0.893\n    n: 6 NpHR and 9 eYFP Drd1a-Cre mice\n  - about: port entry during CS-reward\n    test: Student's t-test\n    statistic: t13 = 0.493\n    p: 0.63\n    n: 6 NpHR and 9 eYFP Drd1a-Cre mice\n  criterion: A claim of absence, on the paper's two Student's t-tests at p < 0.05.\n- id: figs2-ast-many-degs\n  statement: ASt neurons in both the Drd1a+ and Drd2+ clusters have large numbers of differentially\n    expressed genes compared with neurons from the other regions, hundreds in the Discussion's\n    words.\n  source: Results, The ASt has a distinct transcriptomic identity from the TS or CeA, paragraph 3;\n    Figures S2B and S3; Discussion, ASt neurons have distinct genetic identities, paragraph 1\n  quote: ASt neurons within both the Drd1a + and Drd2 + clusters had large numbers of differentially\n    expressed genes (DEGs) compared with neurons from other regions\n  data: elsewhere\n  where: GEO GSE211437\n  depends_on:\n  - fig1b-ast-distinct-subclusters\n  criterion: Within the Drd1a+ and Drd2+ clusters, pseudobulk by batch with Libra run_de and edgeR's\n    likelihood ratio test, genes kept at 1.5-fold and Benjamini-Hochberg p < 0.01 (STAR Methods,\n    Differential expression). The comparison is open; readings, (a) ASt batches against all other\n    regions' batches (region-specific genes), (b) ASt against each of CeA, TS and DS (pairwise, as\n    Figure S2B shows), counting the union. Reproduced when under one reading each cluster has at\n    least 200 DEGs, up and down together. The 200 is this file's reading of \"hundreds\"\n    (Discussion); Figure S2B gives the counts only in a figure.\n- id: figs12gh-activation-no-epm-effect\n  statement: Activating Drd1a+ or Drd2+ ASt neurons does not change time spent in the open arms of an\n    elevated plus maze.\n  source: Figure S12G-H; Results, ASt neuron activity is sufficient to drive freezing and avoidance\n    behavior, paragraph 4\n  quote: Activation of Drd1a + and Drd2 + ASt neurons did not have a significant effect on time spent\n    in open arms of an elevated plus maze\n  statistics:\n  - about: Drd1a-Cre\n    test: two-way ANOVA, group x laser interaction\n    statistic: F(1,20) = 0.4057\n    p: 0.5314\n    n: 5 ChR2 and 7 eYFP mice\n  - about: Drd2-Cre\n    test: two-way ANOVA, group x laser interaction\n    statistic: F(1,40) = 0.9907\n    p: 0.3256\n    n: 6 ChR2 and 16 eYFP mice\n  criterion: A claim of absence, on the paper's two two-way ANOVAs (group by laser epoch, time in\n    open arms per epoch; STAR Methods) at p < 0.05."
}
```

```
The file claims/mills-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now adding the `checks` entry and re-running the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/mills-2026.yaml <<'EOF'
checks:
- date: 2026-11-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1j-ast-drd2-enriched. Dropped the denominator reading without dual expressing nuclei; 71% and 26% sum to 97% and the Figure 1J legend counts dual expressing nuclei as a third class, so only the reading with them fits the paper.
  - fig1l-rnascope-drd2-enriched. Added a criterion; the statement claims the ASt balance differs from TS and DS, which the expected values alone do not settle. Puncta threshold and log-ratio paired t-tests from the STAR Methods; pooling of cells named as open.
  - figs4-cdh6-slit2-gradient. Added a criterion; the claim had none and no expected values. ANOVA and Tukey from the Figure S4 legend, puncta threshold from the STAR Methods; said that the eighth region is not named and that the ordering of means is this file's reading of the gradient.
  - fig2e-ast-sustained-clusters. The cut into seven clusters and the sustained thresholds (z above 1, last 5 s above half the first 5 s) were stated as fixed; the paper gives neither. Said they are choices, and added eight clusters as a variant.
  - fig2o-region-differs-cs-reward. Said that the one-sample t-test of ASt phasic z against 0 is a choice made here; the paper gives no test for "robust phasic responses". Added n to the statistics.
  - fig2q-trajectories-diverge. The criterion took the code's PCA (paired only, 90% of variance) as main and the Methods' as a variant. The STAR Methods say one PCA over paired and unpaired animals and distance in the complete PC space; per protocol step 2 the Methods are now main and the code a variant (confirmed at trajectories_rev_2025.py line 461 at the commit read). Said that the baseline threshold is a choice.
  - figs8-single-trial-divergence. Said that the animal selection comes from the code that plots example pairs, as the code has no statistics for Figure S8E-F, and that with 3 unpaired animals the per-animal signed-rank test cannot reach p < 0.05.
  - fig3h-cs-decoded-paired-only. Said that with 3 unpaired mice the Mann-Whitney U test cannot reach p < 0.05, so the unpaired part cannot fail.
  - fig3j-cs-encoding-glm. The Methods call the CS permutation p-value two-sided but write a one-sided formula; the code (line 356) uses absolute values. Named this, with the code's two-sided test as main and the formula as a variant.
  - figs10-high-defensive-mice-greater-responses. Tolerance 0 on mouse counts had no reason; set to 10% (0.8, 0.7), which still requires the exact counts.
  - fig3b-ast-activation-freezing, fig3c-ast-activation-avoidance, fig4eg-drd2-activation-freezing-avoidance, fig6e-drd2-inhibition-reduces-defense. Added criteria; none had one and none is settled by expected values. Tests and epochs from the legends and STAR Methods; the per-mouse measure of fig6e named as open, and the open field freezing scoring named as not given.
  - figs16-drd2-inhibition-freezing-darting. Added the four group mean changes the statement quotes as expected values, with the legend SEMs as tolerances, and a criterion.
  - fig6f-drd2-inhibition-no-reward-effect, fig6g-j-drd2-inhibition-no-other-effects, figs17-drd1-inhibition-no-effect. Added n from the legends.
  - figs2-ast-many-degs. New claim; the Results finding of large numbers of DEGs in ASt Drd1a+ and Drd2+ neurons had none. The 200 threshold for "hundreds" is named as this file's reading.
  - figs12gh-activation-no-epm-effect. New claim; the Results state that activating Drd1a+ or Drd2+ ASt neurons did not change open arm time, and no claim covered it.
  - Open. fig2-recorded-neurons is a link claim written by the reader, which protocol step 1.4 assigns to the author; it is kept because other claims depend on it and it only checks the paper's own counts.
  - Open. Figures S15L-Q (imaging activity not aligned with freezing bouts) and S11B-C (VGAT activation leaves center time and open arm time unchanged) have no claim; both are secondary and give no Results statistic for the first.
EOF
python tools/claims_check.py claims/mills-2026.yaml paper/10.1016-j.neuron.2026.08.012.txt 2>&1 | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/The number of clusters is not stated: the Results name clusters 1 to 7, so/The number of clusters is not stated; the Results name clusters 1 to 7, so/' claims/mills-2026.yaml; grep -n ": [a-z]" claims/mills-2026.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: " | head; python tools/claims_check.py claims/mills-2026.yaml paper/10.1016-j.neuron.2026.08.012.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "—\|rather" claims/mills-2026.yaml; git diff --stat; git status --short
```

```
claims/mills-2026.yaml | 191 ++++++++++++++++++++++++++++++++++++++++++-------
 1 file changed, 167 insertions(+), 24 deletions(-)
 M claims/mills-2026.yaml
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

I checked `claims/mills-2026.yaml` against the paper and edited only that file. Nothing is committed.

**Checker result** (re-run after my edits): `claims/mills-2026.yaml: 48 claims, 47 quotes, 83 statistical values, 0 problems`. Before the edits it gave 46 claims, 45 quotes and 0 problems.

I also checked the criteria that cite the paper's code against the repository at the cited commit (1fee26d). The 50 Hz unit filter, the trajectory PCA, the decoder settings and the selection for the trial-pair analysis match what the file says.

**Changes, by claim**
- **fig1j-ast-drd2-enriched:** removed the reading that leaves out the nuclei expressing both receptors. 71% and 26% add up to 97%, and the legend counts the dual-expressing nuclei as a third class, so only the reading that includes them fits.
- **fig1l-rnascope-drd2-enriched, figs4-cdh6-slit2-gradient:** added criteria, since neither claim was settled by its expected values. Puncta thresholds, the tests on per-animal log-ratios, and ANOVA with Tukey come from the Methods and legends. The file now says which details are open (how cells are pooled, the eighth region nobody names) and which are this file's reading (the order of means that stands for the gradient).
- **fig2e-ast-sustained-clusters:** cutting the tree into seven clusters and the "sustained" thresholds were written as if fixed. The paper gives neither, so they are now marked as choices, with eight clusters as a variant.
- **fig2o-region-differs-cs-reward:** marked the one-sample t-test as a choice made here, since the paper gives no test for it, and added n.
- **fig2q-trajectories-diverge:** the code's PCA (paired animals only, 90% of variance) was the main test. The Methods say one PCA over paired and unpaired animals, with distance measured in the complete component space. The protocol says the Methods come first, so they are now the main test and the code is a variant. The baseline threshold is marked as a choice.
- **figs8-single-trial-divergence, fig3h-cs-decoded-paired-only:** added a note that with 3 unpaired animals the test cannot reach p < 0.05. That part of each claim can never fail. The figs8 note also says the animal selection comes from code that only plots example pairs.
- **fig3j-cs-encoding-glm:** the Methods call the CS permutation p-value two-sided but write a one-sided formula. The code uses absolute values, so it is two-sided, and the file now takes that as the main test with the formula as a variant.
- **figs10-high-defensive-mice-greater-responses:** the tolerance on mouse counts was 0 with no reason given. It is now 10% (0.8 and 0.7), which still requires the exact counts.
- **fig3b, fig3c, fig4eg, fig6e:** added criteria from the legends and Methods. The open-field freezing scoring is not given in the paper, and the per-mouse measure for fig6e is open; both are named.
- **figs16-drd2-inhibition-freezing-darting:** added the four group means as expected values, with the legend's SEMs as tolerances, and a criterion.
- **fig6f, fig6g-j, figs17:** added n from the legends.
- **New claims:** figs2-ast-many-degs (the many differentially expressed genes in ASt neurons, using the GEO data) and figs12gh-activation-no-epm-effect (activating Drd1a+ or Drd2+ neurons does not change open-arm time).

**Still open**
- fig2-recorded-neurons is a link claim written by the reader, and the protocol gives link claims to the author. I kept it because other claims depend on it and it only checks the paper's own counts.
- Figures S15L-Q and S11B-C have no claim. Both are secondary.
- figs2-ast-many-degs reads "hundreds" as at least 200. That threshold is this file's reading, not the paper's.

**Ready:** yes. The last entry under `checks` records `ready: true`.

## End of run

45 turns, 5 minutes, $2.79 at API prices, result: success.
