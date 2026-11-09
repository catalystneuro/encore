# 000294 · claims-check · run 39987411426

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000294/ paper/; grep -n "Reader" -A40 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 76,200p docs/protocol.md
```

```
finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
     finding.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000294/*.yaml; python tools/claims_check.py claims/000294/10.1162-neco_a_01672.yaml paper/10.1162-neco_a_01672.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat -n claims/000294/*.yaml | head -250
```

```
1	# Claims for Buccino, Damart, Bartram, ... Hierlemann & Van Geit (2024) on dandiset 000294.
     2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
     3	# protocol pilot-10 as stated in docs/protocol.md.
     4	#
     5	# Text read: the version of record (Neural Computation 36, 1286-1331, 2024, CC BY 4.0), from the
     6	# PDF supplied to paper/ and its text extraction: main text, Methods (section 5), Tables 1 to 5
     7	# and the appendix (Figures 9 and 10). The paper has no separate supplement.
     8	#
     9	# Code read: github.com/alejoe91/multimodalfitting at commit 24e8e6168b2d5be45c551bcc08b62fde187d01c7
    10	# (2025-04-12), the repository the Data and Code Availability section names. It holds the package
    11	# (ecode protocols, feature extraction, the patch and HD-MEA sync and patch-triggered average in
    12	# mea_patch/mea_patch.py, model and evaluator construction), the optimization script
    13	# (scripts/run_optimizations.py, 20 offspring and 600 generations by default), the notebooks that
    14	# make the figures (notebooks/ground-truth and notebooks/experimental/cell1, cell2, notebook
    15	# outputs stripped), and cell_models/ with the ground-truth model (hay_ais) and the two
    16	# experimental models: morphology_corrected.swc, mechanisms, parameters, and fitting/efeatures with
    17	# the extracted feature and protocol files, the thresholded probe and the template_BPO.npy
    18	# template of each cell. No optimization results (checkpoints, runs.pkl) are in the repository.
    19	# The BluePyOpt extensions are in BluePyOpt pull request 385, release 1.13.88 (not read).
    20	# In the code, cell 1 is "cell1_211006_3148" and cell 2 is "cell1_211011_3436" (the cell1 and
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cat -n claims/000294/*.yaml | sed -n 250,600p; python tools/claims_check.py claims/000294/10.1162-neco_a_01672.yaml paper/10.1162-neco_a_01672.txt | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n "^[0-9]\.\|^[0-9]\.[0-9]" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1162-neco_a_01672.txt",
 "offset": 1,
 "limit": 820
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1162-neco_a_01672.txt",
 "offset": 820,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1162-neco_a_01672.txt",
 "offset": 1200,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1162-neco_a_01672.txt",
 "offset": 1499,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Figure 9|Figure 10|Data and Code|github|NeuroMorpho|DANDI|dandi",
 "path": "paper/10.1162-neco_a_01672.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1162-neco_a_01672.txt",
 "offset": 1590,
 "limit": 225
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls; ls $TMPDIR 2>/dev/null | head; timeout 60 git ls-remote https://github.com/alejoe91/multimodalfitting 2>&1 | head -3
```

```
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
targets
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 300 git clone -q --depth 1 https://github.com/alejoe91/multimodalfitting mmf && cd mmf && git log -1 --format=%H && ls -R notebooks | head -60 && ls cell_models cell_models/*
```

```
24e8e6168b2d5be45c551bcc08b62fde187d01c7
notebooks:
0-test-model.ipynb
2-create-runs-pkl-from-checkpoints.ipynb
README.md
experimental
ground-truth

notebooks/experimental:
0-correct_morphology.ipynb
0-export-to-nwb.ipynb
cell1
cell2

notebooks/experimental/cell1:
1-generate-experimental-features_cell1.ipynb
3-compute-all-responses_cell1.ipynb
4-optimization-performance-cell1.ipynb
5-AP-dirstirbution-cell1.ipynb
6-cm-ra-cell1.ipynb
[... 69 more lines not kept]
```

**Agent**

Checker passes (23 claims, 0 problems). The code repository is reachable at the same commit, so I'm checking the code-based statements in the file against it.

**Agent calls Bash**

```bash
cd $TMPDIR/mmf; grep -n "def process_mea_patch\|def clean_sta\|def get_peak_times\|center_ms\|np.median\|np.mean\|threshold\|-20" multimodalfitting/mea_patch/mea_patch.py | head -60
```

```
14:def get_peak_times(patch, data_channel=0, efel_threshold=-20, mode="peak"):
24:    efel_threshold: float
25:        EFEL threshold to find the peak (default -20)
44:    efel.setThreshold(efel_threshold)
301:                    thresh = 1000  # Test pulse threshold; TP peak is ~3000 mV
332:                    thresh = 1000  # Test pulse threshold; TP peak is ~3000 mV
603:                            center_ms=1.5, wf_indices=None, **wf_kwargs):
623:    center_ms: float
670:    cut_out_ms_wide = cut_out_ms + 2 * center_ms
690:            sta = np.median(waveforms_to_use, axis=0)
692:            sta = np.mean(waveforms_to_use, axis=0)
714:        samples_center = int(center_ms * recording.get_sampling_frequency() / 1000)
731:    sta = np.median(waveforms_to_use, axis=0)
736:def process_mea_patch(mea_file, patch_files, save_folder, save_recording=False,
738:                      notch_freq=None, center=True, center_electrode=None, center_ms=2, clean_sta=True,
769:    center_ms: float
777:        Std threshold to clean waveforms
870:                                                                                           center_ms=center_ms,
877:            med_amp = np.median(wf_amp)
883:            sta_clean = np.mean(wf_keep, 0)
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf; sed -n 736,760p multimodalfitting/mea_patch/mea_patch.py; sed -n 840,900p multimodalfitting/mea_patch/mea_patch.py
```

```
def process_mea_patch(mea_file, patch_files, save_folder, save_recording=False,
                      patch_ttl_channel=None, patch_ttl_delay=None, freq_min=300, freq_max=6000,
                      notch_freq=None, center=True, center_electrode=None, center_ms=2, clean_sta=True,
                      plot_wf_hist=False, std_thresh=2, overwrite_recording=False,
                      overwrite_templates=False, filestem=None,
                      n_seconds=None, **wf_kwargs):
    """
    Process a MEA file and patch file(s) to compute patch-triggered average.

    First, MEA and patch data are synchronized, the MEA data is then filtered and optionally cached, and finally the
    template is computed. The template can also be cleaned to remove waveforms with amplitudes outside a certain std
    range.

    Parameters
    ----------
    mea_file: str or Path
        Path the mea h5 file
    patch_files: str, Path, or list
        Patch files or files. If a list, the files are concatenated
    save_folder: path
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks; grep -o '"[^"]*\(conover\|mannwhitney\|posthoc\|holm\|= 50\|best_seed\|best_intra\|best_extra\|min_seed\|idxmin\|argmin\)[^"]*"' ground-truth/4-optimization-performance.ipynb ground-truth/3-compute-all-responses.ipynb | sort | uniq | head -60
```

```
ground-truth/3-compute-all-responses.ipynb:"        best_individual_idx = np.argmin(scores)\n"
ground-truth/3-compute-all-responses.ipynb:"].idxmin()]\n"
ground-truth/3-compute-all-responses.ipynb:"best_extras = df_fitness.loc[df_fitness.groupby(\"
ground-truth/3-compute-all-responses.ipynb:"best_seed\"
ground-truth/3-compute-all-responses.ipynb:"for idx, row in best_extras.iterrows():\n"
ground-truth/3-compute-all-responses.ipynb:"from scipy.stats import kruskal, mannwhitneyu, wilcoxon\n"
ground-truth/3-compute-all-responses.ipynb:"print(best_extras)\n"
ground-truth/4-optimization-performance.ipynb:"                   group_col='feature_set', p_adjust = 'holm')"
ground-truth/4-optimization-performance.ipynb:"Simulating best '{strategy}' -- seed: {opt_results_training[strategy]['best_seed']}\"
ground-truth/4-optimization-performance.ipynb:"from scipy.stats import kruskal, mannwhitneyu, wilcoxon\n"
ground-truth/4-optimization-performance.ipynb:"import scikit_posthocs as sp"
ground-truth/4-optimization-performance.ipynb:"max_feature_value = 50\n"
ground-truth/4-optimization-performance.ipynb:"sp.posthoc_conover(df_feats_extra, val_col='feat_score', \n"
ground-truth/4-optimization-performance.ipynb:"sp.posthoc_conover(df_feats_intra, val_col='feat_score', \n"
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks; python - <<'EOF'
import json,glob
for f in glob.glob('*/*.ipynb')+glob.glob('experimental/*/*.ipynb'):
    nb=json.load(open(f))
    out=open(f.replace('.ipynb','.py'),'w')
    for i,c in enumerate(nb['cells']):
        out.write(f"\n# ---- cell {i} [{c['cell_type']}]\n"+''.join(c['source'])+"\n")
EOF
grep -n "best_seed\|best_extras\|best_intra\|idxmin\|max_feature_value\|eap_dist" ground-truth/4-optimization-performance.py ground-truth/3-compute-all-responses.py | head -40
```

```
ground-truth/4-optimization-performance.py:261:max_feature_value = 50
ground-truth/4-optimization-performance.py:273:                feat_value = max_feature_value
ground-truth/4-optimization-performance.py:309:max_feature_value = 50
ground-truth/4-optimization-performance.py:319:        print(f"Simulating best '{strategy}' -- seed: {opt_results_training[strategy]['best_seed']}")
ground-truth/4-optimization-performance.py:330:        eap_dist = np.sum(np.abs(eap_release_norm.ravel() - eap_norm.ravel()))
ground-truth/4-optimization-performance.py:331:        opt_results_val[strategy]["eap_dist"] = eap_dist
ground-truth/4-optimization-performance.py:365:                    feat_value = max_feature_value
ground-truth/4-optimization-performance.py:537:sns.barplot(data=df_test, x="strategy", y="eap_dist", order=order, ax=ax)
ground-truth/3-compute-all-responses.py:264:best_extras = df_fitness.loc[df_fitness.groupby("strategy")["intra_score"].idxmin()]
ground-truth/3-compute-all-responses.py:265:print(best_extras)
ground-truth/3-compute-all-responses.py:267:for idx, row in best_extras.iterrows():
ground-truth/3-compute-all-responses.py:274:    opt_results_training[strategy]["best_seed"] = seed
ground-truth/3-compute-all-responses.py:280:    eap_dist = np.sum(np.abs(eap_release_norm.ravel() - eap_norm.ravel()))
ground-truth/3-compute-all-responses.py:281:    opt_results_training[strategy]["best_eap_dist"] = eap_dist
ground-truth/3-compute-all-responses.py:282:    print(f"EAP distance: {eap_dist}")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks; sed -n 240,420p ground-truth/4-optimization-performance.py
```

```
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)
ax.set_title("Intracellular\n(10 seeds)", fontsize=20)

fig_extra_seeds, ax = plt.subplots(figsize=(7, 10))
sns.boxplot(data=df_fitness, x="strategy", y="extra_score", order=order,
            palette=colors_dict)
ax.set_xlabel("Strategy", fontsize=15)
ax.set_ylabel("Score", fontsize=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)
ax.set_title("Extracellular\n(10 seeds)", fontsize=20)

# ---- cell 29 [code]
if save_fig:
    fig_intra_seeds.savefig(figure_folder / "fig4A-left.pdf")
    fig_extra_seeds.savefig(figure_folder / "fig4A-right.pdf")

[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks; sed -n 420,540p ground-truth/4-optimization-performance.py
```

```
for strategy in figs_intra.keys():
        figs_intra[strategy].savefig(figure_folder / f"fig4C_{strategy}.png", dpi=300)
        figs_intra[strategy].savefig(figure_folder / f"fig4C_{strategy}.pdf")
        figs_extra[strategy].savefig(figure_folder / f"fig4D_{strategy}.png", dpi=300)        
        figs_extra[strategy].savefig(figure_folder / f"fig4D_{strategy}.pdf")

# ---- cell 43 [markdown]
## Compare best-fitted models

# ---- cell 44 [code]
order_full = ["soma", "all", "sections", "single"]
order = []
for strategy in order_full:
    if strategy in opt_results_val:
        order.append(strategy)

# ---- cell 45 [markdown]
### Compare features

# ---- cell 46 [code]
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; grep -n "majority\|tolerance\|rheobase\|IV\b\|\"IV\"\|ecodes_cell_timings\|run" cell1/1-generate-experimental-features_cell1.py | head -60
```

```
52:from bluepyefe.extract import read_recordings, extract_efeatures_at_targets, compute_rheobase,\
75:from bluepyefe.extract import read_recordings, extract_efeatures_at_targets, compute_rheobase,\
87:ecodes_cell_timings = {
96:    "IV": {
131:    runs = [1, 2, 3, 4, 5]  # run1 --> different rheobase
133:    runs = [3, 4, 5, 6]
135:ecode_names = list(ecodes_cell_timings.keys())
139:for run in runs:
143:            if f"run{run}" in patch_file.name and ecode.lower() in patch_file.name:
150:                                    ecode_timings=ecodes_cell_timings, 
162:targets = get_ecode_targets(ecodes_cell_timings)
168:global_tolerance = 30
170:    target["tolerance"] = global_tolerance
188:    majority = 0.4
190:    majority = 0.2
193:compute_rheobase(
195:    protocols_rheobase=['IDthres'],
196:    rheobase_strategy="majority",
197:    rheobase_settings={"majority": majority}
201:print(f"Cell rheobase: {cells[0].rheobase} nA")
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; sed -n 85,135p cell1/1-generate-experimental-features_cell1.py; diff <(sed -n 85,130p cell1/1-generate-experimental-features_cell1.py) <(sed -n 85,130p cell2/1-generate-experimental-features_cell2.py)
```

```
# ---- cell 15 [code]
# define timings for this experiment
ecodes_cell_timings = {
    "IDthres": {
        'ton': 400,
        'toff': 670
    },
    "firepattern": {
        'ton': 500,
        'toff': 4100
    },
    "IV": {
        'ton': 400,
        'toff': 3400
    },
    "IDrest": {
        'ton': 400,
        'toff': 1750
    },
    "APWaveform": {
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf; grep -n "run\b\|runs\|rename\|response_\|stimulus_\|z-proj\|processing" notebooks/experimental/0-export-to-nwb.py | head -30; ls cell_models/cell1_211006_3148/fitting/efeatures; python -c "
import json
for c in ['cell1_211006_3148','cell1_211011_3436']:
    p=json.load(open(f'cell_models/{c}/fitting/efeatures/protocols.json')) if __import__('os').path.exists(f'cell_models/{c}/fitting/efeatures/protocols.json') else {}
    print(c, sorted(k for k in p if k.startswith('IV')))
"
```

```
75:runs = [p.name.split(".")[0] for p in mea_files]
76:print(runs)
84:runs = [run for run in runs if any([int(run[-1]) in run_ids])]
85:print(runs)
88:start_file = [mea for mea in mea_files if runs[0] in mea.name][0]
100:session_description = f"Simultaneous patch-clamp/HD-MEA recording using E-CODE protocols for cell {cell_name} for {len(runs)} experimental runs."
152:imaging_module = nwbfile.create_processing_module(
168:for i, run in enumerate(runs):
169:    print(f"\n\nAdding run: {run}\n\n")
170:    mea_file_run = [m for m in mea_files if run in m.name][0]
171:    patch_files_protocols = natsorted([p.name.split(".")[1] for p in patch_files if run in p.name])
172:    patch_files_run = []
174:        patch_files_run.append([p for p in patch_files if prot in p.name and run in p.name][0])
176:    subrec, patch, timestamps, ttl_mea_sync = mp.sync_patch_mea(mea_file_run, patch_files_run, 
182:    subrec_bin = subrec.save(folder=bin_folder / run, **job_kwargs)
183:    start_time_run = get_recording_start_time(mea_file_run)
184:    tdelta = (start_time_run - start_time).seconds
189:    sequences_in_run = []
196:            name = name.replace(run, run_map[run])
203:            name=f"stimulus_{protocol_name}_{run_name}_{current_sweep}",
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/ground-truth; grep -n -i "rheobase\|270\|threshold_current\|step_amp\|np.arange" 1-generate-ecode-protocols-and-features-hay_ais.py | head -30; grep -n -i "seg\|ais\|distal\|middle\|stim\|amp" 7-AIS-test.py | head -30
```

```
62:# define rheobase min step and step increment
63:rheobase_compute_params = {
95:from multimodalfitting.ecode import compute_rheobase_for_model, generate_ecode_protocols, run_ecode_protocols,\
99:Then we find the rheobase for the model:
102:rheobase, rheo_protocols, rheo_responses = compute_rheobase_for_model(cell, sim=sim, 
103:                                                                      **rheobase_compute_params[model_name])
106:Given the rheobase, we can compute the correct amplitudes of the ECODE stimuli. The `IDrest_300` sweep (300% rheobase) will be used to compute extracellular action potentials, as it contains the highest number of spikes.
109:ecode_protocols = generate_ecode_protocols(rheobase_current=rheobase, record_extra=True,
135:from bluepyefe.extract import read_recordings, extract_efeatures_at_targets, compute_rheobase,\
180:cells[0].rheobase = rheobase
184:print(f"Rheobase: {cells[0].rheobase}")
187:protocols = group_efeatures(cells, targets, use_global_rheobase=True)
3:# Validation - AIS response of models
54:model_name = "hay_ais" # "hay", "hay_ais", "hay_ais_hillock"
83:ais_recordings = mf.utils.get_ais_extra_recordings()
105:    extra_recordings={protocol_for_eap: ais_recordings}
113:# Test AIS dynamics
128:    params_sample = opt_df.iloc[best_idx]
129:    params_dict = {k: v for k, v in zip(param_names, params_sample.best_params)}
130:    opt_results[strategy]["best_fitness"] = params_sample.best_fitness
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; grep -n "idxmin\|idxmax\|best_seed\|nan\|isnan\|dropna\|converge" cell1/3-compute-all-responses_cell1.py cell1/4-optimization-performance-cell1.py cell2/4-optimization-performance-cell2.py | head -40
```

```
cell1/3-compute-all-responses_cell1.py:492:    if np.any(np.isnan(eap)):
cell1/3-compute-all-responses_cell1.py:500:best_total = opt_results_df_no_abd.loc[opt_results_df_no_abd.groupby("strategy")["total_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:501:best_extras = opt_results_df_no_abd.loc[opt_results_df_no_abd.groupby("strategy")["extra_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:502:best_intras = opt_results_df_no_abd.loc[opt_results_df_no_abd.groupby("strategy")["intra_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:516:    opt_results_best_no_abd[strategy]["best_seed"] = row.seed
cell1/3-compute-all-responses_cell1.py:529:best_total = opt_results_df_abd.loc[opt_results_df_abd.groupby("strategy")["total_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:530:best_extras = opt_results_df_abd.loc[opt_results_df_abd.groupby("strategy")["extra_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:531:best_intras = opt_results_df_abd.loc[opt_results_df_abd.groupby("strategy")["intra_score"].idxmin()]
cell1/3-compute-all-responses_cell1.py:546:    opt_results_best_abd[strategy]["best_seed"] = row.seed
cell1/4-optimization-performance-cell1.py:364:best_intras = opt_results_df_abd.loc[opt_results_df_abd.groupby("strategy")["intra_score"].idxmin()]
cell1/4-optimization-performance-cell1.py:378:    opt_results_best[strategy]["best_seed"] = row.seed
cell1/4-optimization-performance-cell1.py:417:        print(f"Simulating best '{strategy}' -- seed: {opt_results_best[strategy]['best_seed']}")
cell2/4-optimization-performance-cell2.py:364:best_intras = opt_results_df_abd.loc[opt_results_df_abd.groupby("strategy")["intra_score"].idxmin()]
cell2/4-optimization-performance-cell2.py:378:    opt_results_best[strategy]["best_seed"] = row.seed
cell2/4-optimization-performance-cell2.py:417:        print(f"Simulating best '{strategy}' -- seed: {opt_results_best[strategy]['best_seed']}")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; sed -n 480,520p cell1/3-compute-all-responses_cell1.py; sed -n 355,380p cell1/4-optimization-performance-cell1.py; grep -n "abd" cell1/4-optimization-performance-cell1.py | head -20
```

```
showfliers=True,  order=order) #palette=colors_dict,
ax.set_xlabel("Strategy", fontsize=15)
ax.set_ylabel("Score", fontsize=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)
ax.set_title("Extracellular\n(10 seeds)", fontsize=20)

# ---- cell 54 [code]
index_na = []
for index, row in opt_results_df.iterrows():
    eap = row.eap
    if np.any(np.isnan(eap)):
        index_na.append(index)
opt_results_df = opt_results_df.drop(index_na)
print(f"Dropped {len(index_na)} rows for no spikes")

# ---- cell 55 [code]
opt_results_df_no_abd = opt_results_df.query("abd == False")
# best responses are the solutions that minimize extra_score
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; grep -n "savefig\|fig_folder /" cell1/4-optimization-performance-cell1.py cell1/3-compute-all-responses_cell1.py cell2/4-optimization-performance-cell2.py cell2/5-AP-dirstirbution-cell2.py | head -40; grep -n "isnan\|Dropped" cell1/4-optimization-performance-cell1.py cell2/*.py | head
```

```
cell1/4-optimization-performance-cell1.py:304:    fig_exp_sample.savefig(fig_folder / f"fig6up_{cell_name}_sample_response.pdf")
cell1/4-optimization-performance-cell1.py:305:    fig_exp_sample.savefig(fig_folder / f"fig6up_{cell_name}_sample_response.png", dpi=300)  
cell1/4-optimization-performance-cell1.py:319:    fig_exp_intra.savefig(figure_folder / "exp_intra.png", dpi=300)
cell1/4-optimization-performance-cell1.py:320:    fig_exp_extra.savefig(figure_folder / "exp_extra.png", dpi=300)
cell1/4-optimization-performance-cell1.py:354:    fig_intra_seeds.savefig(fig_folder / f"fig7A1_{cell_name}_intra.pdf", 
cell1/4-optimization-performance-cell1.py:356:    fig_extra_seeds.savefig(fig_folder / f"fig7A2_{cell_name}_extra.pdf", 
cell1/4-optimization-performance-cell1.py:477:    fig_extra.savefig(fig_folder / f"fig7bottom-center_{cell_name}_responses_extra.pdf", 
cell1/4-optimization-performance-cell1.py:500:    figs_zoom[0].savefig(fig_folder / f"fig7bottom-left_{cell_name}_responses_extra.pdf", 
cell1/4-optimization-performance-cell1.py:502:    figs_zoom[1].savefig(fig_folder / f"fig7bottom-right_{cell_name}_responses_extra.pdf", 
cell1/3-compute-all-responses_cell1.py:136:    fig_iter.savefig(fig_folder / "figS2-cell1.pdf")
cell1/3-compute-all-responses_cell1.py:324:#     fig_exp_sample.savefig(fig_folder / f"{cell_name}_sample_response.pdf")
cell1/3-compute-all-responses_cell1.py:325:#     fig_exp_sample.savefig(fig_folder / f"{cell_name}_sample_response.png", dpi=300)  
cell1/3-compute-all-responses_cell1.py:339:#     fig_exp_intra.savefig(fig_folder / "exp_intra.png", dpi=300)
cell1/3-compute-all-responses_cell1.py:340:#     fig_exp_extra.savefig(fig_folder / "exp_extra.png", dpi=300)
cell2/4-optimization-performance-cell2.py:304:    fig_exp_sample.savefig(fig_folder / f"fig6up_{cell_name}_sample_response.pdf")
cell2/4-optimization-performance-cell2.py:305:    fig_exp_sample.savefig(fig_folder / f"fig6up_{cell_name}_sample_response.png", dpi=300)  
cell2/4-opti
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; sed -n 100,150p cell1/4-optimization-performance-cell1.py; sed -n 320,350p cell1/4-optimization-performance-cell1.py; sed -n 380,480p cell1/4-optimization-performance-cell1.py
```

```
df_optimization = pd.DataFrame(data)
df_model = df_optimization.query(f"model == '{model_name}'")
# set strategy column

results_name = f"opt_results_training_{model_name}"
if abd:
    results_name += "_abd"
else:
    results_name += "_noabd"
results_file = f"{results_name}.pkl"

opt_results_training = None
if (result_folder / results_file).is_file():
    with open(result_folder / results_file, 'rb') as f:
        opt_results_training = pickle.load(f)
else:
    opt_results_all = None

all_responses_file = result_folder / f"all_responses_{model_name}.pkl"

[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; grep -n "best\|positions\|with_currents\|pkl" cell2/5-AP-dirstirbution-cell2.py | head -30; grep -n "best_\|pkl" cell1/5-AP-dirstirbution-cell1.py | head; grep -n "positions\|compute_features\|best_responses\|pkl" ../ground-truth/5-AP-distribution.py | head -20
```

```
61:# change this with folder containing your pkl file
66:val_responses_filename = result_folder / f"validation_responses_{model_name}.pkl"
147:positions = [soma_location, basal_location, ais_location]
149:best_params = opt_results_validation["soma"]["params"]
151:extra_recordings = mf.utils.extra_recordings_from_positions(eva_extra.cell_model, 
152:                                                            eva_extra.sim, params=best_params,
154:                                                            positions=positions,
155:                                                            with_currents=True)
165:for i, (pos_name, pos) in enumerate(zip(position_names, positions)):
184:responses_extra = eva_extra.run_protocol(eva_extra.fitness_protocols["IDrest_250"], best_params)
223:elec_idx_basal = np.argmin([np.linalg.norm(basal_location - p) for p in probe.positions])
224:elec_idx_ais = np.argmin([np.linalg.norm(ais_location - p) for p in probe.positions])
61:# change this with folder containing your pkl file
66:val_responses_filename = result_folder / f"validation_responses_{model_name}.pkl"
146:best_params = opt_results_validation["soma"]["params"]
149:                                                            eva_extra.sim, params=best_params,
180:responses_extra = eva_extra.run_protocol(eva_extra.fitness_protocols["IDrest_250"], best_params)
67:pkl_file_name = "runs.pkl"
69:data = pickle.load(open(result_folder / pkl_file_name, 'rb'))
73:if (result_folder / f"all_responses_{model_name}.pkl").is_file():
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/experimental; sed -n 130,235p cell2/5-AP-dirstirbution-cell2.py
```

```
colors="C0", lw=1)
ax_morph.get_lines()[-1].set_label("SOMA")

ax_morph = mu.plot_mea_recording(eap_all, probe, ax=ax_morph, vscale=vscale, 
                                 colors="C1", lw=1)
ax_morph.get_lines()[-1].set_label("ALL")

ax_morph.set_xlim(-110, 110)
ax_morph.set_ylim(-80, 80)


# ---- cell 19 [code]
ais_location = [-48, 5, 0]
basal_location = [-92, 11, 0]
soma_location = [0, 0, 0]

position_names = ["soma", "basal", "ais"]
positions = [soma_location, basal_location, ais_location]

best_params = opt_results_validation["soma"]["params"]
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/ground-truth; sed -n 110,125p 5-AP-distribution.py; sed -n 205,300p 5-AP-distribution.py
```

```
**extra_kwargs
)

# ---- cell 15 [code]
mf.plot_cell(eva_extra.cell_model, eva_extra.sim, param_values=params_release, color_ais="g")

# ---- cell 16 [code]
positions = np.array([[-62, 828], [-3, 954], [-27, 546], [-27, 85], [134, -28], [-117, -189],
                     [13.4, -28.7], [11.7, -1.2]]) #[12.5, -15.6],
position_names = ["apical_distal_left", "apical_distal_right", "apical_middle", "apical_proximal", 
                  "basal_right", "basal_left", "ais_distal", "ais_proximal"] #"ais_middle", 

# ---- cell 17 [code]
extra_recordings = mf.utils.extra_recordings_from_positions(cell_release, eva_extra.sim, positions, position_names)

# ---- cell 18 [code]

# ---- cell 33 [code]
order = ["soma", "all", "sections", "single"]

[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/ground-truth; grep -n "idxmin\|best\|firepattern\|protocol_for" 5-AP-distribution.py | head; grep -n "firepattern\|protocol_for_eap_val\|std_from_mean" 4-optimization-performance.py | head
```

```
94:# protocol_for_eap = "IDrest_300"
95:protocol_for_eap = "firepattern_120"
109:    protocols_with_lfp=protocol_for_eap,
133:    protocols_with_lfp=protocol_for_eap,
135:    extra_recordings={protocol_for_eap: extra_recordings}, 
143:protocol_to_run = eva_extra.fitness_protocols[protocol_for_eap]
154:    print(f"Computing '{strategy}' -- seed: {opt_results_all[strategy]['best_seed']}")
155:    best_params = opt_results_all[strategy]["best_params"]
156:    responses = eva_extra.run_protocol(protocol_to_run, best_params)
88:protocol_for_eap_val = "firepattern_120"
142:    protocols_with_lfp=protocol_for_eap_val,
172:                                     protocol_name=protocol_for_eap_val, **extra_kwargs)
175:std_from_mean = 0.05
325:                                     protocol_name=protocol_for_eap_val, **extra_kwargs)
367:                feat_score = np.abs(release_value - feat_value) / np.abs(std_from_mean * release_value)
379:                    feat_score = abs(feat_value - release_value) / abs(std_from_mean * release_value)
388:protocols_to_plot = ["firepattern_200", "HyperDepol_-160", "HyperDepol_-40", 
412:                                     protocol_name=protocol_for_eap_val,
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mmf/notebooks/ground-truth; sed -n 140,200p 7-AIS-test.py
```

```
responses_release, eap_release = simulate_responses(cell, params_release, sim, fitness_protocols, 
                                                    protocol_name=protocol_for_eap, **extra_kwargs)
responses_cut_release = mf.utils.get_peak_cutout(responses_release, ms_before=ms_before, 
                                                 ms_after=ms_after, average=True)

for strategy in np.unique(df_model.strategy):
    print(f"Computing {strategy}")
    best_params = opt_results[strategy]["best_params"]

    responses, eap = simulate_responses(cell, best_params, sim, fitness_protocols, 
                                        protocol_name=protocol_for_eap, **extra_kwargs)
    opt_results[strategy]["responses"] = responses
    responses_cut = mf.utils.get_peak_cutout(responses, ms_before=ms_before, 
                                             ms_after=ms_after, average=True)
    opt_results[strategy]["responses_cut"] = responses_cut
    

# ---- cell 18 [code]
responses_to_plot = ['IDrest_300.soma.v', 
                     'IDrest_300.ais_mid_v.v', 
[... 41 more lines not kept]
```

**Agent**

I found several problems in the criteria, mostly where the file misstates what the code does. Applying corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "  criterion: From the NWB electrodes table and series rates. Reproduced when, for each cell, the\n    number of recorded electrodes is above 500 and at most 1024 and both rates are 20 kHz.",
 "new_string": "  criterion: From the NWB electrodes table and series rates. Methods 5.2 says APWaveform was meant\n    to be recorded \"at high sampling rates (typically 200 kHz)\", so the APWaveform patch series may\n    be at 20 or 200 kHz. Reproduced when, for each cell, the number of recorded electrodes is above\n    500 and at most 1024, the MEA rate is 20 kHz, and the patch rate is 20 kHz for every protocol\n    (APWaveform at 20 or 200 kHz)."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "  criterion: Simulate the released model with a suprathreshold step and record the membrane\n    potential at the soma, the middle and the distal AIS, as in Figure 3B. Reproduced when the\n    first spike crosses -20 mV (the code's eFEL threshold) first at the distal AIS, then the\n    middle AIS, then the soma.",
 "new_string": "  criterion: Simulate the released model with IDrest 300% (7-AIS-test.ipynb) and record the\n    membrane potential at the soma, the middle and the distal AIS, as in Figure 3B; the code plots\n    the average of the spike cutouts aligned on the somatic peaks. The paper does not say how the\n    initiation site is read. Readings (a) the time the averaged AP crosses -20 mV (the code's eFEL\n    threshold); (b) the time of the averaged AP peak. Reproduced when, under both readings, the\n    distal AIS comes first, then the middle AIS, then the soma; with readings that disagree,\n    methods_underspecified."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "    or |model| when GT is 0 (4-optimization-performance.ipynb). Two-sided Mann-Whitney, soma\n    against each other strategy, Holm-corrected over the three. Reproduced when each corrected p is\n    below 1e-5 with the other strategy's median score lower; partially reproduced when all three\n    are below 0.05 but not all below 1e-5. The code's Conover test is shown as a variant.",
 "new_string": "    or |model| when GT is 0 (4-optimization-performance.ipynb). Two-sided Mann-Whitney, soma\n    against each other strategy. The paper does not say over which pairs the Holm correction runs.\n    Readings (a) the three soma comparisons; (b) all six pairs of strategies (as the code's\n    Conover test does). Reproduced when, under both readings, each soma comparison has corrected p\n    below 1e-5 with the other strategy's median score lower; partially reproduced when all three\n    are below 0.05 but not all below 1e-5; with readings that disagree, methods_underspecified. The\n    code's Conover test (scikit_posthocs.posthoc_conover, Holm) is shown as a variant."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "  criterion: Templates from firepattern 120%, each channel normalized to its peak-to-peak; per\n    channel, the sum of absolute differences from the ground truth (the code's eap_dist, taken per\n    channel).",
 "new_string": "  criterion: Templates from firepattern 120%, each channel normalized to its peak-to-peak (Figure\n    4D legend; the code divides by np.ptp of the absolute values, shown as a variant); per\n    channel, the sum of absolute differences from the ground truth (the code's eap_dist, taken per\n    channel)."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "    (runs as in recordings-two-cells-runs; BluePyEfe with rheobase by the majority rule on IDthres,\n    majority 0.4 for cell 1 and 0.2 for cell 2, amplitude tolerance 30 in the code, 10% in the\n    Methods, both shown)",
 "new_string": "    (runs as in recordings-two-cells-runs; BluePyEfe with the rheobase from IDthres. Methods 5.4\n    give the lowest amplitude triggering a spike in the majority of recordings, and an amplitude\n    tolerance of 10%; these are the main result. The code (1-generate-experimental-features\n    notebooks) sets the majority fraction to 0.4 for cell 1 and 0.2 for cell 2 and the tolerance to\n    30; shown as a variant)"
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "  criterion: The seed with the best intracellular score per strategy and cell (Figure 7B and 8B\n    legends; the code plots the best extracellular seed, shown as a variant).",
 "new_string": "  criterion: The seed with the best intracellular score per strategy and cell (Figure 7B and 8B\n    legends, and the code that makes the figures, 4-optimization-performance-cell1 and -cell2,\n    best_intras; the 3-compute-all-responses notebooks also select the best extracellular seed for\n    their own plots, shown as a variant)."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000294/10.1162-neco_a_01672.yaml",
 "old_string": "  criterion: Best-intracellular cell 2 all model; transmembrane currents at the soma, the AIS and a\n    basal dendrite (code, extra_recordings_from_positions with_currents), aligned to the recorded\n    template.",
 "new_string": "  criterion: Best-intracellular cell 2 all model (Figure 10 legend and Results 3.3 name the all\n    model; the code, 5-AP-dirstirbution-cell2.ipynb, passes the soma model's parameters,\n    opt_results_validation[\"soma\"], shown as a variant); transmembrane currents at the soma, the AIS\n    and a basal dendrite (code, extra_recordings_from_positions with_currents, positions soma\n    [0, 0, 0], basal [-92, 11, 0], AIS [-48, 5, 0] um, IDrest 250%, averaged over spike cutouts of\n    2 ms before and 5 ms after), aligned to the recorded template; the electrode near the basal\n    dendrite and the one near the AIS are those nearest these positions (code, elec_idx_basal and\n    elec_idx_ais). How the model and recorded time axes are aligned is not given; both are cut 2 ms\n    before the peak, which is used."
}
```

```
The file claims/000294/10.1162-neco_a_01672.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/000294/10.1162-neco_a_01672.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - mea-electrodes-and-rates. Methods 5.2 say APWaveform was recorded at high sampling rates (typically 200 kHz); the criterion required 20 kHz for every patch series. It now accepts 20 or 200 kHz for APWaveform.
  - fig3b-ap-initiates-distal-ais. The protocol (IDrest 300%, averaged spike cutouts) is now taken from 7-AIS-test.ipynb. The -20 mV crossing as the initiation time was a choice not in the paper; it is now one of two readings, with the AP peak time.
  - fig4b-extra-better-than-soma. The criterion fixed the Holm family at the three soma comparisons, which the paper does not say; the code corrects over all six pairs. Both are now readings.
  - fig4d-templates-better-than-soma. Noted that the code normalizes by np.ptp of the absolute template values, unlike the legend's peak-to-peak; shown as a variant.
  - fig78a-soma-intra-all-extra. The criterion used the code's rheobase majority fractions (0.4 and 0.2) as the method; Methods 5.4 say majority of recordings and a 10% tolerance. The Methods are now the main result and the code's values (0.4, 0.2, tolerance 30) a variant.
  - fig78b-validation-spiking. The criterion said the code plots the best extracellular seed; the notebooks that make Figures 7 and 8 (4-optimization-performance-cell1 and -cell2) use the best intracellular seed, as the legends say. Corrected; the best extracellular seed of the 3-compute-all-responses notebooks stays a variant.
  - fig10-cell2-soma-underestimated. Added the code's positions, protocol (IDrest 250%) and electrode choice, and that the code passes the soma model's parameters while the paper names the all model; the all model is the main result, the soma model a variant.
  - Open. fig4d-templates-better-than-soma and fig78b-validation-spiking quantify "almost all" and "main features" with readings the paper does not give; they are named as readings and the outcome needs them to agree.
  - Open. fig10-cell2-soma-underestimated. How the model and recorded time axes are aligned is not given by the paper or the code; both cutouts start 2 ms before the peak, which is used.
  - Open. fig4b-intra-no-difference and fig4b-extra-better-than-soma. The paper names post hoc Mann-Whitney tests but no omnibus test or sidedness; two-sided is used, as the criteria say.
EOF
python tools/claims_check.py claims/000294/10.1162-neco_a_01672.yaml paper/10.1162-neco_a_01672.txt | tail -3; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file against the paper and fixed seven claims. It is ready for an attempt.

**Checker:** `23 claims, 23 quotes, 3 statistical values, 0 problems`, both before and after my edits.

All quotes, sources, statements and expected values match the paper. The three p-values (all p < 1e-5, Figure 4B) are results, not thresholds used to count units. Every main finding has a claim (Figures 3 to 8, Figure 10, Table 1, the methods facts), and none comes from outside this paper. I cloned the paper's code at the commit the file cites (24e8e61) to check what the criteria say about it. Two of those statements were wrong (fig78b, fig10).

**Changes, by claim:**
- **mea-electrodes-and-rates:** Methods 5.2 say APWaveform was recorded at "typically 200 kHz", so the patch-rate check now accepts 20 or 200 kHz for APWaveform.
- **fig3b-ap-initiates-distal-ais:** the protocol (IDrest 300%, averaged spike cutouts) now comes from the code. Timing the spike start by the −20 mV crossing was not in the paper; it is now one of two readings, with the AP peak time as the other.
- **fig4b-extra-better-than-soma:** the paper does not say which pairs the Holm correction covers. The two readings are the three soma comparisons, or all six pairs as the code does.
- **fig4d-templates-better-than-soma:** the code normalizes each channel differently from the legend's peak-to-peak (it uses the range of the absolute values). Added as a variant.
- **fig78a-soma-intra-all-extra:** the criterion used the code's rheobase settings (fractions 0.4 and 0.2, tolerance 30) as the method. The main result now follows the Methods (majority of recordings, 10% tolerance), with the code's settings as a variant.
- **fig78b-validation-spiking:** the file said the code plots the best extracellular seed. The notebooks that make Figures 7 and 8 use the best intracellular seed, as the legends say. Corrected.
- **fig10-cell2-soma-underestimated:** added the code's recording positions, protocol (IDrest 250%) and electrode choice. The code passes the soma model's parameters while the paper names the all model; the all model is the main result and the soma model a variant.

**Still open (recorded in the check entry):**
- In fig4d and fig78b, "almost all" and "main features" have no definition in the paper. The criteria use two readings each, and the outcome needs them to agree.
- For fig10, neither the paper nor the code says how the model and recorded time axes are aligned. The criterion lines both up at 2 ms before the peak.
- For fig4b, the paper names post hoc Mann-Whitney tests but gives no omnibus test and does not say one- or two-sided. Two-sided is used.

The check entry is at the end of the file with `ready: true`. Nothing was committed or pushed.

## End of run

43 turns, 4 minutes, result: success.
