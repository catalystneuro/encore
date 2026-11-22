# du-2026 · claims-check · run 44913009317

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/ claims/ docs/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## [A-Z]/p' docs/protocol.md; cat claims/du-2026.yaml; python tools/claims_check.py claims/du-2026.yaml paper/10.64898-2026.08.04.742876.txt; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0c28cf67-f83f-411d-8d94-dbce26d0e5f7/tool-results/b9kmwugq3.txt"
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
12	are enough to know which paper and which experiments it is meant to hold. A
13	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
14	documentation) is a longer description, to be read for that alone; it is not
15	the paper, and no claim comes from it.
16	
17	### 2. Read the paper's code
18	
19	Read the code the paper links to before writing criteria. Say what it holds,
20	and record the repository and commit read. Where the Methods leave a choice
[... 1189 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.08.04.742876.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.08.04.742876.txt",
 "offset": 1303
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes (33 claims, 0 problems). I've read the whole paper. Next I'll see whether the cited code release can be reached, so I can check the code-based parts of the criteria.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q --depth 1 --branch v1.0-jne-submission https://github.com/gwkuqgfkqe/neural-decoder-context-audit.git ndca 2>&1 | tail -3; cd ndca 2>/dev/null && git log -1 --format=%H && ls
```

```
Turn off this advice by setting config variable advice.detachedHead to false

b042fbe1cda2ca5a353751c693d7c95f45de0456
ANALYSIS_PROVENANCE.md
CHECKSUMS.sha256
FROZEN_ARTIFACTS.sha256
LICENSE
README.md
REPRODUCE.md
data
outputs
pyproject.toml
requirements-original-analysis.txt
requirements.txt
scripts
src
submission_source
tests
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && ls src/neural_evidence scripts submission_source outputs; grep -n "trial_count\|start_time\|warm\|history_bins\|sample_offset_ms\|neural_lead_ms\|output_lead_ms\|def \|octant\|floor" src/neural_evidence/link.py | head -80
```

```
outputs:
confirmation_analysis
primary_analysis

scripts:
audit_reference_dois.py
build_final_archive.py
build_link_confirmation_manifest.py
build_submission_figures.py
compare_reproduced_artifacts.py
download_link_confirmation.py
download_public_data.py
run_link_confirmation.py
run_link_context_ladder.py
run_nonlinear_seed_sensitivity.py
run_primary_analyses.py
run_synthetic_calibration.py
validate_frozen_artifacts.py
validate_submission_artifacts.py

[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 28,260p src/neural_evidence/link.py; grep -n "load_link(" -A12 scripts/*.py | grep -n "lead\|offset\|history\|load_link" | head -40
```

```
return np.stack(features, axis=-1)


def load_link(
    path: str | Path,
    *,
    movement_window_ms: int = 500,
    neural_history_ms: int = 100,
    neural_lead_ms: int = 80,
    neural_signal: str = "ThresholdCrossings",
    context_mode: str = "geometry_tensor",
    output_history_ms: int = 100,
    output_lead_ms: int | None = None,
    sample_offset_ms: int | None = None,
    seed: int = 20260726,
    test_size: float = 0.30,
) -> DatasetSplit:
    """Load fixed causal trial windows from one public LINK session.

    Context contains a coarse movement-direction condition, phase harmonics,
[... 239 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && grep -n "spearman\|rankdata\|gamma\|def \|lambda_c\|block" src/neural_evidence/nested_estimators.py | head -60; grep -rn "block\|separate_pen\|nonlinear_context" --include=*.py src scripts | grep -v "^src/neural_evidence/nested" | head -30; ls outputs/primary_analysis | head -80
```

```
53:    def to_dict(self) -> dict[str, object]:
91:    replacement_penalty_distance_spearman: float
101:    def to_dict(self) -> dict[str, object]:
133:    gamma_multiplier: float
138:    def to_dict(self) -> dict[str, object]:
142:def _stratified_inner_split(
164:def _select_nuisance_alphas(
202:def _fully_nested_nuisance_predictions(
286:def _select_grouped_innovation_alpha(
331:def _component_metrics(
363:def _permutation_sources(
385:def _rankdata(values: np.ndarray) -> np.ndarray:
399:def _spearman(x: np.ndarray, y: np.ndarray) -> float:
402:    return float(np.corrcoef(_rankdata(x), _rankdata(y))[0, 1])
405:def evaluate_fully_nested_audit(
656:        replacement_penalty_distance_spearman=_spearman(
684:def _rff_ridge(
688:    gamma_multiplier: float,
694:            gamma=gamma_multiplier,
703:def _select_grouped_rff_alpha(
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 181,240p src/neural_evidence/specification_estimators.py; grep -n "^def \|rff\|random_fourier" src/neural_evidence/specification_estimators.py src/neural_evidence/robustness_estimators.py | head -40; sed -n 640,700p scripts/build_submission_figures.py
```

```
def _select_block_penalties(
    *,
    context_train: np.ndarray,
    neural_train: np.ndarray,
    target_train: np.ndarray,
    context_validation: np.ndarray,
    neural_validation: np.ndarray,
    target_validation: np.ndarray,
    penalty_grid: tuple[float, ...],
) -> tuple[float, float]:
    best_pair = (float(penalty_grid[0]), float(penalty_grid[0]))
    best_score = -np.inf
    for context_penalty in penalty_grid:
        for neural_penalty in penalty_grid:
            model = _BlockRidge(
                context_penalty=context_penalty,
                neural_penalty=neural_penalty,
            )
            model.fit(context_train, neural_train, target_train)
            score = r2_score(
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 253,300p src/neural_evidence/specification_estimators.py; sed -n 429,470p src/neural_evidence/specification_estimators.py; sed -n 574,640p src/neural_evidence/specification_estimators.py; grep -n "legacy\s*=\|legacy_nlb\s*=\|nonlinear\s*=\|read_csv" scripts/build_submission_figures.py | head -30
```

```
def _select_rff_hyperparameters(
    dataset: TrialDataset,
    *,
    train_indices: np.ndarray,
    seed: int,
    inner_validation_size: float,
    alpha_grid: tuple[float, ...],
    gamma_multipliers: tuple[float, ...],
    n_components: int,
) -> tuple[float, float, float, float]:
    inner_train_indices, validation_indices = train_test_split(
        train_indices,
        test_size=inner_validation_size,
        random_state=seed + 11,
        stratify=dataset.condition[train_indices, 0],
    )
    context_inner = _flatten_trials(dataset.context, inner_train_indices)
    context_validation = _flatten_trials(dataset.context, validation_indices)
    neural_inner = _flatten_trials(dataset.neural, inner_train_indices)
    neural_validation = _flatten_trials(dataset.neural, validation_indices)
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 620,632p scripts/build_submission_figures.py; sed -n 925,990p scripts/build_submission_figures.py; grep -rn "0.00310\|0.0031\b\|0.00404\|combined" scripts/*.py ANALYSIS_PROVENANCE.md | head -20
```

```
def figure5_estimator_sensitivity() -> None:
    legacy = pd.read_csv(
        REFERENCE_SOURCE / "tables" / "estimator_sensitivity_link.csv"
    )
    nested = _primary_link()
    nonlinear = pd.read_csv(OUTPUT / "link_nonlinear_neural_metrics.csv")
    legacy_nlb = pd.read_csv(
        REFERENCE_SOURCE / "tables" / "estimator_sensitivity_nlb.csv"
    )
    nlb = pd.read_csv(OUTPUT / "nlb_fully_nested_metrics.csv")
    nlb = nlb[nlb.estimator_seed == 20260726]
    axes[1].set_title(
        "(b) Correct pairing exceeds replacement in all 20 sessions",
        loc="left",
    )
    _legend(axes[1], loc="upper left", title="Task")

    seeds = np.asarray(sorted(nonlinear_link.rff_seed.unique()))
    seed_positions = np.arange(len(seeds))
    series = []
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 600,665p src/neural_evidence/nested_estimators.py; grep -n "def evaluate_decoders_nested" -A40 src/neural_evidence/estimators.py | grep -n "neural\|split\|alpha" | head -20; grep -n "evaluate_\|import" scripts/run_link_context_ladder.py | head
```

```
permutation_gains.append(
            _normalized_gain(behavior_test, context_prediction, prediction)
        )
    if permutation_gains:
        permutation_low, permutation_high = np.quantile(
            permutation_gains, [0.025, 0.975]
        )
        permutation_mean = float(np.mean(permutation_gains))
    else:
        permutation_low = permutation_high = permutation_mean = float("nan")

    result = FullyNestedAuditResult(
        context_r2=float(
            r2_score(
                behavior_test,
                context_prediction,
                multioutput="variance_weighted",
            )
        ),
        exact_r2=float(
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && grep -rn "neural_only\|evaluate_decoders_nested" scripts/*.py src/neural_evidence/*.py | head -20; grep -n "replacement_penalty\s*=" -B4 -A4 src/neural_evidence/nested_estimators.py | head -20
```

```
src/neural_evidence/estimators.py:442:def evaluate_decoders_nested(
567-    per_trial_exact_mse = np.mean((behavior_trials - exact_trials) ** 2, axis=(1, 2))
568-    per_trial_replacement_mse = np.mean(
569-        (behavior_trials - replacement_trials) ** 2, axis=(1, 2)
570-    )
571:    replacement_penalty = per_trial_replacement_mse - per_trial_exact_mse
572-
573-    conditions = dataset.condition[:, 0]
574-    eligible_counts = np.asarray(
575-        [
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && grep -n "r2\|neural" scripts/run_link_context_ladder.py | head -30; head -3 outputs/primary_analysis/link_fully_nested_ladder_metrics.csv | cut -c1-600; sed -n 442,520p src/neural_evidence/estimators.py
```

```
13:from neural_evidence.link import load_link
14:from neural_evidence.nested_estimators import evaluate_fully_nested_audit
15:from neural_evidence.serialization import dumps_strict, write_json
50:            neural_signal="SpikingBandPower",
51:            neural_history_ms=160,
52:            neural_lead_ms=0,
117:                    "context_r2": float(
119:                            [row["context_r2"] for row in selected if row["task"] == task]
date,task,file,context_mode,context_r2,exact_r2,exact_gain,replacement_gain,self_replacement_max_abs_error,context_mse,exact_mse,replacement_mse,context_rmse,exact_rmse,replacement_rmse,normalized_context_rmse,normalized_exact_rmse,mse_reduction_percent,component_context_rmse,component_exact_rmse,component_replacement_rmse,component_exact_gain,exact_gain_ci_low,exact_gain_ci_high,train_trials,test_trials,final_context_alpha,final_residualizer_alpha,innovation_alpha,crossfit_folds,eligible_sources_min,eligible_sources_median,source_reuse_max,source_reuse_median_nonzero,replacement_distance_mean
2021-10-15,CO,sub-Monkey-N_ses-20211015_obj-1wbkdus_ecephys.nwb,causal_history,0.6853889835850544,0.6976419555886803,0.012252972379129834,0.0011516827184236212,0.0,7.316980188095993e-05,7.03201002265977e-05,7.290195241175013e-05,0.008553934877058623,0.008385708093333425,0.008538264016282826,0.56090197544357,0.5498709427469044,3.8946417526159403,"(0.00926123280730268, 0.007782619780694697)","(0.009117493077436423, 0.007583635041066677)","(0.009228108223274316, 0.007787549257824126)","(0.011033341038719259, 0.013546753861353664)",0.006783180174528812,0.017401345199489635,262,113,0.1,1000.0,10000
2021-10-15,RD,sub-Monkey-N_ses-20211015_obj-a6r2sq_ecephys.nwb,causal_history,0.6428696179886042,0.6517927938864874,0.008923176057281677,-0.008226482712162317,0.0,0.00027975597926637103,0.00027276606203384954,0.00028620014588413704,0.016725907427292876,0.01651563083971816,0.016917450927493097,0.5976038724698505,0.590090850915077,2.498576527605
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && ls submission_source/tables; for f in submission_source/tables/*temporal* submission_source/tables/*lead*; do [ -f "$f" ] && head -3 "$f" | cut -c1-400; done; grep -n -i "temporal\|offset\|lead" ANALYSIS_PROVENANCE.md REPRODUCE.md | head -20
```

```
estimator_sensitivity_link.csv
estimator_sensitivity_nlb.csv
figure5_estimator_sensitivity_source.csv
figure6_confirmation_source.csv
figure6_nonlinear_seed_source.csv
figure7_specification_sensitivity_source.csv
figure8_practical_effects_source.csv
figure8_trajectory_source.csv
link_confirmation_metrics.csv
link_context_ladder.csv
link_date_cluster_summary.csv
link_fully_nested_ladder.csv
link_fully_nested_ladder_metrics.csv
link_fully_nested_metrics.csv
link_nonlinear_neural_metrics.csv
link_nonlinear_neural_seed_metrics.csv
link_session_results.csv
nlb_fully_nested_metrics.csv
nlb_nonlinear_neural_metrics.csv
nlb_nonlinear_neural_seed_metrics.csv
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && grep -n "def figure7" -A40 scripts/build_submission_figures.py | grep -n "read_csv\|lead\|offset\|robust\|==" | head; head -2 submission_source/tables/robustness.csv | cut -c1-700; cut -d, -f1-6 submission_source/tables/robustness.csv | sort -u -t, -k1,3 | head -30
```

```
2:534-    robustness = pd.read_csv(REFERENCE_SOURCE / "tables" / "robustness.csv")
3:535-    link = pd.read_csv(OUTPUT / "link_fully_nested_metrics.csv")
6:538-    lead = robustness[robustness.analysis == "lead"].copy()
7:539-    lead["value"] = pd.to_numeric(lead["value"])
9:541-        values = lead[lead.task == task].sort_values("value")
14:546-                    "panel": "temporal_offset",
22:554-    axes[0].set_xlabel("Neural/output temporal offset (ms)")
24:556-    axes[0].set_title("(a) Retrospective temporal-offset sensitivity", loc="left")
31:563-            values = link[(link.outer_seed == seed) & (link.signal == "SpikingBandPower") & (link.context_mode == "geometry_tensor") & (link.task == task)]
analysis,value,task,delta,matched_delta,task_difference,ci_low,ci_high,exact_sign_p
lead,0,CO,0.004103020863206035,-0.003318400811775998,0.002050966332657942,0.00012392146579957072,0.004315346463616443,0.0859375
analysis,value,task,delta,matched_delta,task_difference
capacity,Linear + history,SBP,,,0.002255080861235148
capacity,Linear + history,TCR,,,0.0023496895615844277
capacity,Linear geometry,SBP,,,0.0007136332638909163
capacity,Linear geometry,TCR,,,0.0017058719683174888
capacity,Quadratic + history,SBP,,,0.004102117098374235
capacity,Quadratic + history,TCR,,,0.003739692956697323
capacity,Quadratic geometry,SBP,,,0.003582813315675089
capacity,Quadratic geometry,TCR,,,0.0051874626847012995
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && grep -n "class EvaluationResult" -A30 src/neural_evidence/*.py | grep -i "delta\|matched\|innovation" | head; grep -rn "matched_delta\|\"lead\"" --include=*.py . | head
```

```
src/neural_evidence/estimators.py-22-    innovation_r2: float
src/neural_evidence/estimators.py-23-    innovation_context_matched_r2: float
src/neural_evidence/estimators.py-24-    neural_context_matched_r2: float
src/neural_evidence/estimators.py-25-    full_context_matched_r2: float
src/neural_evidence/estimators.py-26-    delta_neural_r2: float
src/neural_evidence/estimators.py-27-    delta_neural_r2_ci_low: float
src/neural_evidence/estimators.py-28-    delta_neural_r2_ci_high: float
src/neural_evidence/estimators.py-30-    delta_neural_r2_context_matched: float
src/neural_evidence/estimators.py-31-    delta_innovation_r2: float
src/neural_evidence/estimators.py-32-    delta_innovation_r2_ci_low: float
./scripts/build_submission_figures.py:538:    lead = robustness[robustness.analysis == "lead"].copy()
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ndca && sed -n 58,72p ANALYSIS_PROVENANCE.md
```

```
selected session could be dropped or replaced based on its result.
19. Two additional neural random-feature map seeds were fixed before execution;
    all three seed-level results are reported without performance-based
    selection.

The confirmation criteria were: (i) at least 16 of 20 geometry-by-phase gains
positive, with positive task means for both center-out and random-target;
(ii) a lower combined mean after adding lag-matched measured-output history;
and (iii) correct-trial geometry-by-phase gain greater than replacement gain in
at least 16 of 20 sessions and in both task means. All three criteria were met.
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "    does not say how the neural-only penalty is chosen; the code (estimators.py,\n    evaluate_decoders_nested, as run by run_link_context_ladder.py) selects it from the grid on\n    an inner 80/20 direction-stratified split of the outer-training trials, and that is followed.",
 "new_string": "    does not say how the neural-only penalty is chosen, and no script in the release computes\n    the neural-only R2 (run_link_context_ladder.py calls only evaluate_fully_nested_audit). The\n    release's neural-only Ridge, estimators.py evaluate_decoders_nested, selects the penalty from\n    the grid on an inner 80/20 direction-stratified split of the outer-training trials (random\n    state seed + 11), and that is followed as the code's choice."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "    small that 10% is below the variation one refit could give; reproduced when the two\n    history values are within tolerance, the two phase-only values are below 0.02, and the\n    context-only R2 rises at every rung for both tasks. The phase-only values against their 10%\n    tolerances are reported.",
 "new_string": "    small that 10% is below the variation one refit could give; reproduced when the two\n    history values are within tolerance and the two phase-only values are below 0.02. The paper\n    gives no values for the middle rungs, which are reported. The phase-only values against\n    their 10% tolerances are reported."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  statement: With phase-only context, nearest-replacement gain in RD stayed positive (0.10498),\n    so replacement does not remove the task-template correction under an under-specified\n    context.",
 "new_string": "  statement: With phase-only context, the mean nearest-replacement gain in RD stayed positive\n    (0.10498)."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  criterion: Mean over the nine RD sessions of the replacement gain under phase-only context.\n    Replacement condition is the direction octant (link.py), as in every LINK replacement.",
 "new_string": "  criterion: Mean over the nine RD sessions of the replacement gain under phase-only context.\n    The replacement condition is the direction octant (\"a different same-direction trial\",\n    Results 2.3, paragraph 4; link.py). Under phase only every trial has the same context\n    trajectory, so all source distances tie and the tie rule of Methods 4.7 (integer trial\n    index) picks the source. Reproduced when the mean is positive and within tolerance."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  criterion: As rff-rtt, on the 18 development sessions, SBP only (Figure 5 legend). \"Combined\" is\n    the mean over the 18 sessions. Reproduced when the CO and RD geometry means are positive under\n    every map and the combined geometry and history means of every map fall inside their ranges\n    widened by 10% of each bound.",
 "new_string": "  criterion: As rff-rtt, on the 18 development sessions, SBP only (Figure 5 legend; Methods 4.6).\n    What the \"combined range\" spans is not stated; readings (a) the range over the three maps of\n    the mean over all 18 sessions, (b) the range over the six task means (CO and RD under each of\n    the three maps, as Figure 6c plots them). The history mean is read as the mean over all 18\n    sessions under each map. Reproduced when the CO and RD geometry means are positive under\n    every map and, under a reading, the geometry values and the history means of every map fall\n    inside their ranges widened by 10% of each bound."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  criterion: Block penalties minimize the objective of Methods 4.5 with lambda_C and lambda_X\n    chosen separately from the grid; nonlinear context augments standardized context with\n    random Fourier features (Methods 4.6). The release has no run script for these, and the\n    Methods do not say how the penalties are selected for the block model or which of the\n    nonlinear-context settings (D = 128, 256, 512; three map seeds; g in 0.25, 1, 4) Figure 5\n    shows. Readings for the nonlinear context, (a) every setting, (b) D = 256 and seed 20260726\n    with g chosen per session from the three values by inner validation, as the frozen\n    rff_capacity_sensitivity.csv baseline rows suggest. For the block model, penalties chosen\n    jointly on the inner 80/20 split of the outer-training trials (as for the nuisances). \"Task\n    means\" are read as the four signal-by-context means of Figure 5a (SBP and TCR, geometry by\n    phase and plus history). Reproduced when all are positive for both families under a reading.",
 "new_string": "  criterion: Block penalties minimize the objective of Methods 4.5 with lambda_C and lambda_X\n    chosen separately from the grid; nonlinear context augments standardized context with\n    random Fourier features (Methods 4.6). The Methods do not say how the block penalties are\n    selected or which nonlinear-context setting (D = 128, 256, 512; three map seeds; g in 0.25,\n    1, 4) Figure 5 shows. The release has no run script for these, but it holds both estimators\n    (specification_estimators.py), and Figure 5a plots the frozen table\n    estimator_sensitivity_link.csv (build_submission_figures.py, figure5_estimator_sensitivity).\n    The code is followed. Block model (evaluate_block_ridge_audit), the pair (lambda_C,\n    lambda_X) searched over the grid squared on an inner 80/20 direction-stratified split of\n    the outer-training trials (random state seed + 11), refit on all outer-training trials.\n    Nonlinear context (evaluate_rff_context_audit), D = 256, g chosen from 0.25, 1, 4 with the\n    penalties on the same inner split, five cross-fitting folds. Readings for the nonlinear\n    context, (a) that code setting, (b) every setting of Methods 4.6. \"Task means\" is open;\n    readings (a) the CO and RD means of each signal and context, (b) the four means over all 18\n    sessions that Figure 5a plots (SBP and TCR, geometry by phase and plus history). Reproduced\n    when all are positive for both families under a reading."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  criterion: LINK SBP, geometry by phase plus measured-output history, 18 development sessions,\n    fully nested estimator, CO and RD means at offsets 0, 40, 80 and 120 ms (the offset is the\n    gap between the end of both histories and the behavior bin; link.py neural_lead_ms and\n    output_lead_ms). The release has no script for this run. Holding the window fixed is read",
 "new_string": "  criterion: LINK SBP, geometry by phase plus measured-output history, 18 development sessions,\n    CO and RD means at offsets 0, 40, 80 and 120 ms (the offset is the gap between the end of\n    both histories and the behavior bin; link.py neural_lead_ms and output_lead_ms). The release\n    has no script for this run, and the paper does not name the estimator (the Figure 7a legend,\n    unlike 7b, does not say fully nested). Figure 7a plots the frozen table robustness.csv\n    (build_submission_figures.py), whose split-seed rows do not match the fully nested values of\n    Figure 7b and whose fields are those of estimators.py evaluate_decoders_nested. Readings (i)\n    the fully nested estimator, (ii) evaluate_decoders_nested, its residual-neural\n    (innovation) gain. Holding the window fixed is read"
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "    causal_history_quadratic). The release has no script for this run; the fully nested\n    estimator is assumed, as for the other development results, and the Figure 7c intervals are\n    paired date-bootstrap intervals (as in link-task-contrast-by-context).",
 "new_string": "    causal_history_quadratic). The release has no script for this run and the paper does not\n    name the estimator. Figure 7c plots the same frozen robustness.csv as Figure 7a (see\n    temporal-offset), so the readings are (i) the fully nested estimator, (ii) estimators.py\n    evaluate_decoders_nested, its residual-neural (innovation) gain. The Figure 7c intervals are\n    paired date-bootstrap intervals (legend; as in link-task-contrast-by-context)."
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/du-2026.yaml",
 "old_string": "  criterion: Replacement and permutation as in Methods 4.7. The tolerance on the seed count is\n    the paper's own prespecified criterion, at least 9 of 10 seeds (Methods 4.8). Reproduced when",
 "new_string": "  criterion: Replacement and permutation as in Methods 4.7. The tolerance on the seed count is\n    10% of the reported count, which matches the paper's prespecified criterion for replacement,\n    at least 9 of 10 seeds (Methods 4.8); the paper sets no criterion for the permutation\n    control, and the same count is used for it. Reproduced when"
}
```

```
The file claims/du-2026.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/du-2026.yaml <<'EOF'
checks:
- date: 2026-11-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - link-neural-only-r2, corrected the code citation. No release script computes neural-only R2;
    run_link_context_ladder.py calls only evaluate_fully_nested_audit. The penalty rule is now
    cited to estimators.py evaluate_decoders_nested as the code's choice (commit b042fbe read).
  - link-context-only-r2, dropped the requirement that context-only R2 rise at every rung. The
    paper states only the two endpoints, and the middle rungs are not nested (direction by phase
    and additive geometry hold different features).
  - link-phase-only-replacement, removed the interpretation added to the statement (the paper
    says replacement is "not expected to remove every predictive regularity", Results 2.3,
    paragraph 4); cited the paper for the same-direction condition; noted that under phase only
    all source distances tie, so the Methods 4.7 tie rule picks the source; added a judging rule.
  - synthetic-pair-breaking, corrected the reason for the seed-count tolerance. The paper's 9 of
    10 criterion covers replacement only (Methods 4.8); the permutation control has none.
  - rff-link, "combined range" was read as the mean over 18 sessions alone. Added the reading of
    the range over the six CO and RD task means that Figure 6c plots.
  - estimator-family-link, the block-penalty and nonlinear-context methods were described as
    unsettled by the release. The release holds both estimators (specification_estimators.py,
    evaluate_block_ridge_audit and evaluate_rff_context_audit), and Figure 5a plots their frozen
    table; the criterion now follows that code (joint grid over both penalties and D = 256 with
    g chosen on the inner 80/20 split). Added the reading of "task means" as CO and RD means.
  - temporal-offset and context-capacity-contrast, the fully nested estimator was stated as
    fact. The paper does not name the estimator for Figure 7a or 7c, and both panels plot the
    frozen robustness.csv, whose split-seed rows differ from the fully nested Figure 7b values
    and whose fields match estimators.py evaluate_decoders_nested. Both estimators are now named
    as readings.
  - Open, temporal-offset. Whether the behavioral window is fixed at the latest warm-up (280 ms)
    or elsewhere is not stated by the paper or a release script; the file's reading stands.
  - Open, replacement-ranks-lower. The supplement with the rank and random-source values was not
    supplied, so the claim is judged by sign only.
EOF
python tools/claims_check.py claims/du-2026.yaml paper/10.64898-2026.08.04.742876.txt | tail -3; grep -n ": .*: " claims/du-2026.yaml | grep -v "^\S*\s*-\?\s*\(quote\|statement\|criterion\|source\)" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/du-2026.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(p, x[:80])
walk(d); print(d['checks'][-1]['ready'], len(d['checks'][-1]['changes']))
EOF
git status --short
```

```
True 9
 M claims/du-2026.yaml
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

## Review of `claims/du-2026.yaml`

**Checker result:** `claims/du-2026.yaml: 33 claims, 32 quotes, 12 statistical values, 0 problems`. It gave the same result before and after my edits.

I read the whole paper and checked the cited code release (tag v1.0-jne-submission, commit b042fbe, which matches the commit the file records). The statements, sources, statistics, expected values and interval-based tolerances match the paper. Every main finding has a claim, and none comes from outside the paper.

**Changes, by claim:**
- **link-neural-only-r2:** the code citation was wrong. `run_link_context_ladder.py` never computes neural-only R2, and no release script does. The penalty rule is now cited to `estimators.py` `evaluate_decoders_nested` as the code's choice.
- **link-context-only-r2:** I removed the requirement that context-only R2 rise at every rung. The paper gives only the two endpoints, and the middle rungs don't contain each other's features, so a rise at each step isn't guaranteed.
- **link-phase-only-replacement:** the statement added an interpretation the paper doesn't make, and I cut it. The criterion now cites the paper for using a same-direction source. It also notes that with phase-only context every source is equally close, so the lowest trial index picks the source (the tie rule in Methods 4.7). I added a rule for judging the claim.
- **synthetic-pair-breaking:** the reason given for the seed-count tolerance was wrong. The paper's "at least 9 of 10 seeds" rule covers replacement only, not the permutation control.
- **rff-link:** "combined range" had only one reading. I added a second: the range over the six CO and RD task means that Figure 6c plots.
- **estimator-family-link:** the file said the release left these methods open. It doesn't: the code holds both estimators (`evaluate_block_ridge_audit` and `evaluate_rff_context_audit`), and Figure 5a plots their saved results. The criterion now follows that code, and "task means" can also be read as the CO and RD means.
- **temporal-offset and context-capacity-contrast:** the file stated as fact that these used the fully nested estimator, but the paper never names the estimator. The saved table behind Figures 7a and 7c doesn't match the fully nested values and has the output fields of `evaluate_decoders_nested`. Both estimators are now listed as possible readings.

**Still open:**
- **temporal-offset:** where the fixed behavioral window sits (the file assumes 280 ms after trial start) isn't stated in the paper, and no release script settles it.
- **replacement-ranks-lower:** the supplement wasn't supplied, so this claim can only be judged on whether each mean went down.

**Ready:** yes. The `checks` entry is added with `ready: true`. Nothing was committed or pushed.

`git status` also lists untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others), and I left them alone.

## End of run

31 turns, 3 minutes, $1.74 at API prices, result: success.
