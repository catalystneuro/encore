# costabile-2023 · claims-check · run 45719109022

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/costabile-2023.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md
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
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/costabile-2023.yaml; python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/costabile-2023.yaml"
}
```

```
1	# Claims for Costabile, Balakrishnan, Schwinn & Haesemeyer (2023), "Model discovery to link neural
2	# activity to behavioral tasks", eLife 12:e83289, tested on DANDI:000235, 000236, 000237 and 000238.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
4	# protocol as stated in docs/protocol.md (version pilot-19, Reader).
5	#
6	# Text read. The version of record (eLife, published 6 June 2023), paper/10.7554-elife.83289.txt,
7	# extracted from the publisher PDF (also under paper/): main text, the legends of Figures 1 to 7,
8	# Table 1, Methods, Data availability. The PDF was opened only to read Figure 6 (panels F and G)
9	# and Figure 7 (panel E), whose values the text does not give. eLife's figure supplements
10	# (Figure 1, 2, 3, 4, 5, 6 and 7, figure supplement 1) are online only: neither their panels nor
11	# their legends are in the PDF or the text. The Results state what each of them shows, and the
12	# claims that rest on them (region enrichments, Figure 6, figure supplement 1D, E, G to I;
13	# Figure 7, figure supplement 1A to E) are written from those Results sentences and from the
14	# code that draws them. Supplementary file 1 (Z-Brain region abbreviations) and the MDAR checklist
15	# are not under paper/; neither holds results.
16	#
17	# Code read. github.com/haesemeyer/mine_pub at commit 368d75650a1de92d9dd6c7dd1aadff24be6ba379,
18	# the revision the paper archives (Software Heritage, Haesemeyer 2023). It holds the CNN
19	# (model.py), the Taylor routines (taylorDecomp.py), the MINE interface (mine.py), the simulation
20	# scripts for Figures 1 to 4 (cnn_fit_test.py, cnn_nonlin_test.py, cnn_sta_test.py, mine_edf.py,
[... 745 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt | tail -30; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 1000,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passes (32 claims, 0 problems). Reading the rest of the paper (Discussion, Methods) now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 1700,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 2400,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I have the full paper. Next I'll try to get the cited code so I can check the code details the criteria rely on.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/haesemeyer/mine_pub.git 2>&1 | tail -2; cd mine_pub 2>/dev/null && git checkout -q 368d75650a1de92d9dd6c7dd1aadff24be6ba379 && ls
```

```
AnatomyClustering.py
LICENSE
README.md
cnn_fit_test.py
cnn_nonlin_test.py
cnn_sta_test.py
environment_utf8.yml
example_train_trajectory.py
experiment.py
mine.py
mine_edf.py
model.py
perf_nlc_nonlin.py
plotMusall.py
processMusall.py
rspinal_build_main.py
rspinal_plot_panels.py
rwave_build_main.py
rwave_create_cmtk_commands.py
rwave_data_fit.py
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; grep -n "taylor_scores\|3 \*\|n_sig\|sig_cut\|norm.ppf\|norm.cdf\|min_size\|UpSet\|upset\|min_subset\|cluster_jacobian\|SpectralClustering\|percentile\|5000\|n_boot\|0\.975\|97\.5" plotMusall.py rwave_plot_panels.py rwave_build_main.py rspinal_build_main.py rspinal_plot_panels.py utilities.py | head -80
```

```
plotMusall.py:126:    def cluster_jacobian_map(self, predictor_label: str, n_clusters: int, taylor_percentile=90.0) -> [np.ndarray,
plotMusall.py:129:        Cluster jacobians in pixel space for pixels that are in the top percentile of being related to the predictor
plotMusall.py:132:        :param taylor_percentile: The threshold which pixels have to cross for their taylor metric to be included
plotMusall.py:140:        map_valid = tay_map > np.nanpercentile(tay_map, taylor_percentile)
plotMusall.py:239:        all_taylor_raw = np.vstack([sg["output_data"]["taylor_scores"][:, :, 0] for sg in session_groups])
plotMusall.py:240:        all_taylor_se = np.vstack([sg["output_data"]["taylor_scores"][:, :, 1] for sg in session_groups])
plotMusall.py:242:        sig = (all_taylor_raw - 3 * all_taylor_se) > 0
plotMusall.py:243:        all_taylor_scores = np.zeros_like(all_taylor_raw)
plotMusall.py:244:        all_taylor_scores[sig] = all_taylor_raw[sig]
plotMusall.py:246:        print(f"{np.sum(all_taylor_scores[:, 22:] > 0)} significant interaction terms found")
plotMusall.py:247:        all_taylor_scores = all_taylor_scores[:, :22].copy()
plotMusall.py:249:        all_taylor_scores_sorted = all_taylor_scores[np.argsort(np.argmax(all_taylor_scores, 1))]
plotMusall.py:251:        taylor_df = pd.DataFrame(all_taylor_scores_sorted, columns=taylor_labels)
plotMusall.py:297:        clust_lv, jac_lv = mapper.cluster_jacobian_map("lVisStim", 2)  # 2 clusters likely splits ON and OFF
plotMusall.py:298:        clust_rv, jac_rv = mapper.cluster_jacobian_map("rVisStim", 2)
plotMusall.py:299:        clust_lg, jac_lg = mapper.cluster_jacobian_map("lGrab", 2)
plotMusall.py:300:        clust_rg, jac_rg = mapper.cluster_jacobian_map("rGrab", 2)
rwave_plot_panels.py:18:import upsetplot as ups
rwave_plot_panels.py:21:from sklearn.cluster import SpectralClustering
rwave_plot_panels.py:95:        ran_mat = np.random.rand(psize, 5000) < expectation  # roll dice with p(heads)=expectation
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 600,700p rwave_build_main.py; sed -n 70,140p rwave_plot_panels.py
```

```
all_jacobians.append(jacs)
        all_mescores.append(mescores)
        all_ann_train_corrs.append(trainc)
        all_taylor_r2.append(taylorr2)

    info_dframe = pd.DataFrame(info_dict)
    info_dframe.to_csv(path.join(folder, f"Overview_Info_{path.splitext(outfile)[0]}.csv"))

    # convert lists into appropriate arrays
    all_test_corrs = np.hstack(all_test_corrs)
    all_ann_train_corrs = np.hstack(all_ann_train_corrs)
    all_taylor_r2 = np.hstack(all_taylor_r2)
    all_lm_test_corrs = np.hstack(all_lm_test_corrs)
    all_lm_tc_sh = np.hstack(all_lm_tc_sh)
    all_test_corrs_sh = np.hstack(all_test_corrs_sh)
    all_vglut = np.hstack(all_vglut)
    all_taylor_scores_raw = np.vstack(all_taylor_scores_raw)
    all_centroids = np.vstack(all_centroids)
    # calculate the required corrected significance to get an overall .05 score then threshold
    # taylor metrics based on that
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 440,720p rwave_plot_panels.py
```

```
if "activity" in dfile:
            act_index = ix_chosen
            act_plane = df_behavior["plane"][act_index]
            act_exp = df_behavior["experiment_id"][act_index]
            print(f"Example plane is plane {act_plane} from {experiment_names[act_exp]}")
            df_activity = rbm.get_cadata(dfile)
            act_valid = np.logical_and(np.hstack(df_activity["experiment_id"]) == act_exp,
                                       np.hstack(df_activity["plane"]) == act_plane)
            act_sorting = np.argsort(all_test_corrs[np.isfinite(all_test_corrs)][act_valid])[::-1]
            fig = pl.figure()
            sns.heatmap(np.vstack(df_activity["ca_data"])[act_valid][act_sorting], vmax=8, cmap="bone", rasterized=True)
            pl.xlabel("Frame")
            pl.ylabel("Neuron")
            fig.savefig(path.join(plot_dir, f"ExampleActivity_SortedByDecreasingFit.{ext}"), dpi=600)
            fig = pl.figure()
            pl.plot(all_test_corrs[np.isfinite(all_test_corrs)][act_valid][act_sorting], 'k')
            pl.plot([0, np.sum(act_valid)], [0, 0], 'C0--')
            pl.plot([0, np.sum(act_valid)], [fit_threshold, fit_threshold], 'C3--')
            pl.xticks([0, 250, 500, 750, 1000])
            pl.yticks([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 120,175p plotMusall.py; sed -n 225,300p plotMusall.py; sed -n 40,140p rspinal_plot_panels.py
```

```
jp_map = np.empty((jpix.shape[0], jpix.shape[2], jpix.shape[1]))
        for r in range(jpix.shape[1]):
            for c in range(jpix.shape[2]):
                jp_map[:, c, r] = jpix[:, r, c]
        return jp_map

    def cluster_jacobian_map(self, predictor_label: str, n_clusters: int, taylor_percentile=90.0) -> [np.ndarray,
                                                                                                      np.ndarray]:
        """
        Cluster jacobians in pixel space for pixels that are in the top percentile of being related to the predictor
        :param predictor_label: The name of the predictor
        :param n_clusters: The number of clusters
        :param taylor_percentile: The threshold which pixels have to cross for their taylor metric to be included
        :return:
            [0]: n_valid_pixels long vector of cluster labels
            [1]: The included pixel-space jacobians (n_valid_pixels x n_timepoints)
        """
        jac_map = self.create_jacobian_map(predictor_label)
        jac_map = jac_map.reshape((jac_map.shape[0], jac_map.shape[1]*jac_map.shape[2]))
        tay_map = self.create_metric_map(predictor_label).ravel()
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; grep -n "linapx\|frame_rate\|history\|shift\|Mine(\|corr_cut\|0\.1\b" plotMusall.py processMusall.py | head -40
```

```
plotMusall.py:204:        pl.plot([min_c, max_c], [0.1, 0.1], 'C3--')
plotMusall.py:210:        print(f"{np.sum(all_test_corrs >= 0.1)} out of {all_test_corrs.size} components were successfully fit.")
plotMusall.py:211:        per_sess_fit = np.hstack([np.sum(stc > 0.1) / stc.size for stc in session_test_corrs])
plotMusall.py:220:        all_linapx_scores = np.hstack([sg["output_data"]["model_lin_approx_scores"][()] for sg in session_groups])
plotMusall.py:223:        sns.kdeplot(all_linapx_scores)
plotMusall.py:230:        print(f"Fraction of nonlinear neurons: {np.sum(all_linapx_scores<0.8)/np.sum(np.isfinite(all_linapx_scores))}")
processMusall.py:51:    Creates an n_predictors x n_timepoints matrix of unique (non-timeshifted) predictors excluding video
processMusall.py:65:    # this variable contains the full set of possibly time-shifted predictors
processMusall.py:72:    # NOTE: We need to take care of the nature of the shifts used in the fullR design matrix
processMusall.py:74:    #   prevMod, water] the first index will give us the 0-shift predictor
processMusall.py:79:    #   the 0-shift predictor
processMusall.py:142:        # Relative datashift to virtually re-center convolutional filters - we set the current time
processMusall.py:161:        # corr-cut set to 0.1 to only fully process data with at least 1% explained variance on test
processMusall.py:162:        miner = Mine(2 / 3, 150, 0.1, True, True, 30, 143)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; grep -n "corr_th\s*=\|lm_thresh\s*=\|c_thresh\s*=\|sig_thresh\s*=\|min_lin_approx\s*=\|me_thresh\s*=" rwave_build_main.py rspinal_build_main.py; grep -n "plot_region_enrichment(\|def plot_region_enrichment\|boot_complexity(\|is_lm_fit\|lm_fit" rwave_plot_panels.py | head -40; grep -n "rspinal\|0\.5" rspinal_build_main.py | head -20
```

```
rwave_build_main.py:758:    corr_th = cl_args.corrthresh
rspinal_build_main.py:289:    corr_th = cl_args.corrthresh
47:def plot_region_enrichment(c_of_interest: np.ndarray, population: np.ndarray, masks: h5py.Group,
140:def boot_complexity(all_scores: np.ndarray, subset_size: int, ci: float, n_boot: int):
307:        above_threshl_lm = np.hstack(df_raw["is_lm_fit"])
694:        fit_lm_fit = np.hstack(df_fit["is_lm_fit"])
700:            lm_abt = fit_lm_fit[this_exp]
961:        plot_region_enrichment(sensory_cluster, above_thresh[above_thresh], mask_outlines, brain_outline_top,
964:        plot_region_enrichment(motor_cluster, above_thresh[above_thresh], mask_outlines, brain_outline_top,
967:        plot_region_enrichment(interact_cluster, above_thresh[above_thresh], mask_outlines, brain_outline_top,
999:        plot_region_enrichment(start_cluster, motor_assigned, mask_outlines, brain_outline_top, brain_outline_side,
1001:        plot_region_enrichment(disp_cluster, motor_assigned, mask_outlines, brain_outline_top, brain_outline_side,
1003:        plot_region_enrichment(ang_cluster, motor_assigned, mask_outlines, brain_outline_top, brain_outline_side,
1073:            l, u = boot_complexity(complexity_sens, np.sum(jac_cluster_sens == cnum)[()], 95.0, 1000)[:2]
42:    keys = ["neuron_id", "barcode", "is_rspinal", "label_brightness"]
46:def save_rs_fit_neurons(datafile: h5py.File, neuron_ids: np.ndarray, barcodes: np.ndarray, is_rspinal: np.ndarray,
48:    if not rbm.check_arg_sizes(neuron_ids, barcodes, is_rspinal, label_brightness):
53:    grp.create_dataset("is_rspinal", data=is_rspinal)
63:    keys = ["neuron_id", "experiment_id", "plane", "is_ann_fit", "is_rspinal"]
68:                        is_rspinal: np.ndarray):
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 720,790p rwave_build_main.py; sed -n 270,300p rspinal_build_main.py; grep -n "def build_all_data\|def main\|min_lin_approx\|me_thresh\|lm_thresh\|c_thresh\|sig_thresh" rwave_build_main.py | head; sed -n 940,1010p rwave_plot_panels.py; sed -n 1040,1080p rwave_plot_panels.py
```

```
s, p, e = extract_stimuli(folder, sub_folder_list)
        save_stimuli(main_file, e, p, s)
        b, p, e = extract_behaviors(folder, sub_folder_list, behavior_names)
        save_behaviors(main_file, e, p, b)
        # obtain zbrain anatomy
        region_names = load_zbrain_region_names("ZBrain_Masks.hdf5")
        save_zbrain_region_list(main_file, region_names)
        region_memberships = build_zbrain_region_barcodes(convert_h2borientum_to_zbrainpx(all_centroids), region_names,
                                                          "ZBrain_Masks.hdf5", True)
        save_zbrain_anatomy(main_file, np.arange(region_memberships.shape[0]), region_memberships)
        if save_activity:
            c, p, e, n = get_calcium_data(folder, sub_folder_list)
            valid = np.isfinite(all_test_corrs)
            save_cadata(main_file, e[valid], p[valid], n[valid], c[valid, :])


if __name__ == "__main__":
    a_parser = argparse.ArgumentParser(prog="rwave_build_main",
                                       description="Will create main file of analysis results for all figure "
                                                   "plotting")
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.7554-elife.83289.pdf')
for p in [12,14,9]:
    d[p].get_pixmap(dpi=170).save(f'p{p+1}.png')
" && ls *.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -r 150 -f 13 -l 13 -png paper/10.7554-elife.83289.pdf p && pdftoppm -r 150 -f 15 -l 15 -png paper/10.7554-elife.83289.pdf p && pdftoppm -r 150 -f 10 -l 10 -png paper/10.7554-elife.83289.pdf p; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1; python -c "import pypdf; print('pypdf')" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pillow"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf; print('pypdf')
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
```

**Agent**

Nothing here renders PDFs, so I'll try the Read tool on the PDF pages directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.pdf",
 "pages": "13"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.pdf",
 "pages": "15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; grep -n "n_reps\|range(20)\|n_iter\|n_sims\|noise\|mix_\|np.linspace\|fractions\|n_train\|train_lengths\|sample\|edf\|n_params\|count_params" cnn_fit_test.py cnn_nonlin_test.py perf_nlc_nonlin.py cnn_sta_test.py mine_edf.py | head -70
```

```
cnn_fit_test.py:42:    # all signals are standardized to unit variance/sd - noise_fraction controls the standard deviation of the noise
cnn_fit_test.py:43:    # SNR = 1/noise_fraction
cnn_fit_test.py:44:    noise_fraction = 0.25
cnn_fit_test.py:53:    # Noise: No relationship to inputs, gaussian noise
cnn_fit_test.py:92:    # since noise will be added to calcium data
cnn_fit_test.py:147:    # add noise
cnn_fit_test.py:148:    ca_response += np.random.randn(*ca_response.shape) * noise_fraction
cnn_nonlin_test.py:39:    t_base = np.linspace(0, 10, 50)
cnn_nonlin_test.py:108:    # all signals are standardized to unit variance/sd - noise_fraction controls the standard deviation of the noise
cnn_nonlin_test.py:109:    noise_fraction = 0.25
cnn_nonlin_test.py:142:    # add noise
cnn_nonlin_test.py:143:    ca_responses += np.random.randn(ca_responses.shape[0], ca_responses.shape[1]) * noise_fraction
cnn_nonlin_test.py:381:        # add noise
cnn_nonlin_test.py:382:        ca_responses += np.random.randn(ca_responses.shape[0], ca_responses.shape[1]) * noise_fraction
cnn_nonlin_test.py:462:    score_bins = np.linspace(0, 1, 100)
cnn_nonlin_test.py:478:    ttt_score = np.linspace(0, 1, 1000)
cnn_nonlin_test.py:522:    lscore_test_bins = mquantiles(all_lscore, np.linspace(0, 1, 50))
cnn_nonlin_test.py:525:    boot_sample = utilities.bootstrap_binned_average(all_lscore, all_crv, lscore_test_bins, 5000)
cnn_nonlin_test.py:526:    average = np.nanmean(boot_sample, 0)
cnn_nonlin_test.py:527:    ci_low = np.nanpercentile(boot_sample, 2.5, 0)
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 455,520p cnn_nonlin_test.py; grep -n "length\|n_frames\|frames" cnn_sta_test.py | head -30; grep -n "n_neurons\s*=\|range(n_neurons\|n_iter\|for i in range" cnn_fit_test.py cnn_sta_test.py | head
```

```
sns.kdeplot(data=lscore_tanhpow, cut=0, label='$tanh^n$')
    sns.kdeplot(data=lscore_conved, cut=0, label='convolved')
    pl.legend()
    pl.xlabel("Linear model metric")
    pl.ylabel("Density")
    sns.despine()

    score_bins = np.linspace(0, 1, 100)
    fig = pl.figure()
    pl.hist(lscore_diffed, score_bins, density=True, label='derivative', histtype='step')
    pl.hist(lscore_rect, score_bins, density=True, label='rectified', histtype='step', linestyle='dashed')
    pl.hist(lscore_tanhpow, score_bins, density=True, label='$tanh^n$', histtype='step', linestyle='dashed')
    pl.hist(lscore_conved, score_bins, density=True, label='convolved', histtype='step')
    pl.legend()
    pl.xlabel("Linear model metric")
    pl.ylabel("Density")
    sns.despine()
    fig.savefig(path.join(plot_dir, "Linear_model_score_Distribution.pdf"))

    # ROC analysis
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; sed -n 280,372p cnn_sta_test.py; sed -n 395,415p cnn_sta_test.py; sed -n 480,512p cnn_sta_test.py
```

```
def data_len_test(frame_rate: int, sta_filter: np.ndarray, stc_filter: np.ndarray) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Compares between MINE and the Ridge Model with alpha=1000 (best fit) how filter quality and test correlation
    changes with changing data length
    :param frame_rate: Frame rate to create a time-base for RandomWave stimuli
    :param sta_filter: The linear filter
    :param stc_filter: The nonlinear filter
    :return: Data frame with fitting results
    """
    n_neurons = 50
    # Note: seconds_to_test includes train (2/3) and test period (1/3)
    # Note: The rather wonky numbers below are chosen because our training dataset generation drops
    # remainders that do not fit into the batch size of 256. So to not penalize MINE (by having less t-samples
    # than the LM model) we set the samples such that this drop will be minimzed
    base_seconds = 78+15
    seconds_to_test = [base_seconds, base_seconds*2, base_seconds*4, base_seconds*8, base_seconds*16, base_seconds*32,
                       base_seconds*64]
    result_dict = {"Model": [], "Filter": [], "Similarity": [], "Train frames": []}
    tcorr_dict = {"Model": [], "test correlation": [], "Train frames": []}
    hist_steps = sta_filter.size
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub; grep -n "lm" rwave_plot_panels.py | grep -i -n "jac\|clust" | head; grep -rn "regions_for_overview = \|regions_for_overview=" rwave_plot_panels.py | head -3
```

```
800:        regions_for_overview = ['Diencephalon - Caudal Hypothalamus',  # CHYP
Shell cwd was reset to
```

**Agent**

The code checks are done. The main problems are in the criteria: some tests don't cover every part of their statement, and a few levels or readings were made up or left out. I'm editing the file now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    SD across the 20 runs, (b) the simple model's mean r2 is below MINE's by more than 0.2 in more\n    than half of the types, and (c)",
 "new_string": "    SD across the 20 runs, (b) the simple model's mean r2 is below MINE's by more than 0.2 in more\n    than half of the seven types other than noise (the i.i.d. noise type of Figure 1C, which no\n    model can predict, is left out of (b)), and (c)"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    exceeds the OLS fit's for both filters, the best Ridge penalty's median is within 0.1 of\n    MINE's or below it, and MINE's median test correlation is at least that of every Volterra\n    fit. The 0.1 margin for \"almost comparable\" is set here.",
 "new_string": "    exceeds the OLS fit's for both filters, the best Ridge penalty's median for each filter is no\n    more than 0.1 below MINE's (or above it), and MINE's median test correlation is at least that\n    of every Volterra fit. The 0.1 margin for \"almost comparable\" is set here."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    M2, R(S1) x R(S2) and |S1| response types, every expected term's mean metric exceeds every\n    unexpected term's mean metric.",
 "new_string": "    M2, R(S1) x R(S2) and |S1| response types, every expected term's mean metric exceeds every\n    unexpected term's mean metric. The r2 of the full expansion (equation 26) is reported for\n    every response type; the paper gives no level for \"high\" (its example in Figure 4B is 0.98),\n    so it does not decide the claim."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    and the grab difference map has them in opposite anterior (motor) cortices. Which hemisphere\n    carries which sign is read from the figure, contralateral to the stimulus or limb.",
 "new_string": "    and the grab difference map has them in opposite anterior (motor) cortices. Which hemisphere\n    carries which sign is read from the figure, contralateral to the stimulus or limb. The whisk\n    map (Whisk minus the mean of the two visual maps, Figure 5G and plot_session_maps) and the\n    same maps for every session (Figure 5, figure supplement 1) are shown but do not decide the\n    claim; the paper judges the whisk map by eye against Figure 2 of Musall et al. 2019, and the\n    session maps only for \"general agreement\"."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    spectral clustering. Reproduced when the excitatory visual cluster averages have weights\n    after time 0 below 10% of their peak, and the excitatory grab cluster averages depart from\n    baseline (by more than 10% of their peak) at a lag after 0 of at most 0.2 s. The 10% levels\n    are set here; the paper reads the figure by eye.",
 "new_string": "    spectral clustering. Receptive fields are at the mouse model's 15 Hz (150 timepoints for the\n    10 s history, processMusall.py). Reproduced when, for both the left and the right visual\n    predictor, (a) the excitatory cluster average has weights after time 0 below 10% of its peak,\n    (b) its peak absolute weight exceeds that of the inhibitory cluster average, and (c) it has\n    two peaks, one near time 0 and one 1.35 to 1.65 s before it (the paper's ~1.5 s widened by\n    10%); and when, for both grab predictors, (d) the excitatory cluster average departs from\n    baseline (by more than 10% of its peak) after time 0, its last such timepoint no later than\n    0.11 s plus one 15 Hz frame (the paper's 100 ms widened by 10%, plus the sampling step), and\n    (e) its width at half its peak is smaller than that of the excitatory visual cluster average\n    (\"much sharper\"). The 10% of peak levels and the half-peak width are set here; the paper reads\n    the figure by eye."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    (b) its peak absolute weight exceeds that of the inhibitory cluster average, and (c) it has\n    two peaks, one near time 0 and one 1.35 to 1.65 s before it (the paper's ~1.5 s widened by\n    10%); and when",
 "new_string": "    (b) its peak absolute weight exceeds that of the inhibitory cluster average, and (c) both\n    cluster averages are biphasic, each with two peaks of its sign, one near time 0 and one 1.35\n    to 1.65 s before it (the paper's ~1.5 s widened by 10%); and when"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    tolerance under the Results reading, or at least 0.75 of the classified neurons are\n    behavior-driven (behavior-only or mixed) and behavior-only is the largest class.",
 "new_string": "    tolerance under the Results reading, or at least 0.75 of the classified neurons are\n    behavior-driven (behavior-only or mixed) and behavior-only is the largest class. The 0.75 level\n    for \"vast majority\" is set here, not the paper's."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    complexity 2 (read from the PDF). Reproduced when behavior has the highest mean fraction and\n    stimulus and mixed are each below the all-neuron fraction by more than their bootstrap\n    standard errors.",
 "new_string": "    complexity 2 (read from the PDF). Reproduced when behavior has the highest mean fraction,\n    stimulus and mixed are each below the all-neuron fraction by more than their bootstrap\n    standard errors, and complexity 2 is below the all-neuron fraction by more than its bootstrap\n    standard error (the \"low computational complexity\" part of the statement)."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    97.5th percentile. The population is open, (a) stimulus, behavior and mixed neurons together\n    (Methods) or (b) all fit neurons (code). Reproduced when, under one reading, at least one\n    telencephalic region (pallium, subpallium or telencephalic migrated area 4), the habenula and\n    the interpeduncular nucleus are enriched for stimulus neurons, and the olfactory epithelium\n    mask holds stimulus neurons.",
 "new_string": "    97.5th percentile, over the code's list of overview regions (regions_for_overview in\n    rwave_plot_panels.py). The population is open, (a) stimulus, behavior and mixed neurons\n    together (Methods) or (b) all fit neurons (code). Reproduced when, under one reading, at least\n    one telencephalic region (pallium, subpallium or telencephalic migrated area 4), the habenula\n    and the interpeduncular nucleus are enriched for stimulus neurons, and the olfactory\n    epithelium mask holds temperature-sensitive neurons. Which neurons those are is open, (a) pure\n    stimulus neurons (the code's Stim_Neuron_Loc_OlfEpith plot) or (b) any neuron with a\n    significant temperature metric (the Results cite panel 1I, the mixed-selectivity panel)."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    \"Medial hindbrain\" and \"forebrain\" name no Z-Brain region; they are read as any rhombomere 1\n    to 7 or medial hindbrain stripe, and any telencephalic region.",
 "new_string": "    \"Medial hindbrain\" and \"forebrain\" name no Z-Brain region. \"Medial hindbrain\" is read as any\n    rhombomere 1 to 7 or medial hindbrain stripe. \"Forebrain\" is open, (a) any telencephalic\n    region or (b) any telencephalic or diencephalic region other than the ventral thalamus, which\n    the sentence names separately."
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    rhombencephalon as in rwave_plot_panels.py. Reproduced when the four shapes are found, the\n    two slow clusters have their largest telencephalic fraction among the four, the fast heating",
 "new_string": "    rhombencephalon as in rwave_plot_panels.py. \"Enriched in the forebrain\" is read as the\n    paper's sense of enrichment (Methods, Processing of zebrafish data): each slow cluster's\n    forebrain fraction is above that of all pure stimulus neurons pooled. \"Forebrain\" is open,\n    (a) the telencephalon or (b) the telencephalon and diencephalon together. Reproduced when the\n    four shapes are found, both slow clusters are enriched in the forebrain under a reading, the\n    fast heating"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "  criterion: The paper shows this by anatomical clustering (5 um radius, connected components,",
 "new_string": "  criterion: The Results cite \"Figure 7G\", which does not exist; the legend of Figure 7F is the\n    anatomical clustering by complexity, so 7F is meant. The paper shows this by anatomical\n    clustering (5 um radius, connected components,"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now adding claims for three supplement findings that had none (Figure 2, figure supplement 1D/E; Figure 3, figure supplement 1B; Figure 3, figure supplement 1I/J).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    stimuli, two linear and two nonlinear responses each. Reproduced when the AUC is within\n    tolerance and both error rates at 0.8 are at most 0.055.",
 "new_string": "    stimuli, two linear and two nonlinear responses each. Reproduced when the AUC is within\n    tolerance and both error rates at 0.8 are at most 0.055.\n- id: fig2s1-nonlinearity-metrics-agree\n  statement: On the networks of the ROC analysis, a lower linear approximation score goes on\n    average with a higher curvature metric and a higher nonlinearity coefficient.\n  source: Results, MINE characterizes computational complexity, paragraph 4; Figure 2, figure\n    supplement 1D and 1E\n  quote: Notably, a decrease in the explained variance by the linear truncation led on average to\n    increases in both these metrics of nonlinearity\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_nonlin_test.py\n  depends_on:\n  - fig2e-linearity-roc\n  criterion: Curvature metric (Methods, equation 5) and nonlinearity coefficient (equation 6) of\n    each network of the ROC analysis, averaged in 50 quantile bins of the linear approximation\n    score with 5000 bootstrap draws and 95% intervals (cnn_nonlin_test.py). The paper gives no\n    test. Reproduced when, for both metrics, the bin average in the lowest linear-score bin is\n    above the 95% interval of the highest bin, and the Spearman correlation of bin linear score\n    with bin average is negative; the rank correlation is set here.\n"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "    simulation as in mine_edf.py. Reproduced when the estimate is below 50 and the parameter\n    count is within tolerance.",
 "new_string": "    simulation as in mine_edf.py. Reproduced when the estimate is below 50 and the parameter\n    count is within tolerance.\n- id: fig3s1-white-noise-benchmark\n  statement: With Gaussian white noise input, both MINE and a direct fit of the Volterra kernels\n    recover receptive fields nearly indistinguishable from the true ones.\n  source: Results, MINE characterizes neural receptive fields, paragraph 2; Figure 3, figure\n    supplement 1A and 1B\n  quote: As expected, both MINE and directly fitting the Volterra kernels yielded receptive fields\n    that were nearly indistinguishable from the ground truth\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_sta_test.py\n  criterion: As in cnn_sta_test.py, main with white noise (stimulus drawn from N(0, 1), Methods),\n    the same filters and nonlinearities as Figure 3A, best cosine similarity of the eigenvectors of\n    Q with the three largest eigenvalues to each true filter (equation 17). The number of\n    simulations is open, (a) 100 (Methods, \"All fits were repeated for 100 randomly generated\n    stimuli\") or (b) 10 (the code's n_neurons for white noise). Reproduced when the median\n    similarity of MINE and of the OLS fit is at least 0.9 for both filters; the 0.9 level for\n    \"nearly indistinguishable\" is set here.\n- id: fig3s1-training-length\n  statement: As training data grow, the Ridge Volterra fit with the lower penalty predicts better\n    than MINE at small training sizes but gives no usable receptive fields, both Ridge fits give\n    worse receptive fields at large training sizes, and MINE is more robust to this.\n  source: Results, MINE characterizes neural receptive fields, paragraph 4; Figure 3, figure\n    supplement 1I and 1J\n  quote: The Ridge model with the lower penalty outperforms MINE for lower numbers of training\n    samples ... both Ridge models show a deterioration of extracted receptive fields for large\n    numbers of training samples ... MINE appears more robust to this effect\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_sta_test.py\n  criterion: As data_len_test in cnn_sta_test.py, 50 replicates of slowly varying stimuli of 93 s\n    times 1, 2, 4, 8, 16, 32 and 64 (two-thirds training), a separate validation stimulus,\n    MINE against Ridge Volterra fits with penalties 100 and 1000, filter quality as the dot product\n    of the extracted and true unit-norm filters. The paper gives no levels. Reproduced when (a)\n    the penalty-100 fit's mean validation correlation exceeds MINE's at the shortest length, (b)\n    for each Ridge fit the mean similarity of at least one filter at the longest length is below\n    its maximum over lengths by more than the SEM, and (c) MINE's drop from its maximum to the\n    longest length is smaller than each Ridge fit's for that filter. \"Usable\" receptive fields is\n    not judged.\n"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -2 | xargs -I{} sh -c 'echo {}; sed -n "/^checks:/,\$p" {} | head -20'
```

```
claims/alasfour-2024.yaml
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the others as variants. Said that p < 0.001 for a printed 0 is this file's reading.
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 for the alpha sign; that paragraph gives theta and gamma only. The alpha sign is cited to Results 3.1 paragraph 6.
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2 was fixed one way; the paper does not say which val
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/costabile-2023.yaml <<'EOF'
checks:
- date: 2026-11-25
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1f-mine-fits-ground-truth. Part (b) counted the i.i.d. noise type among the types where the simple model "fails"; no model can predict noise (Figure 1C), so (b) now counts the seven other types.
  - fig3-receptive-fields-slow-stimuli. "Within 0.1 of MINE's or below it" was met by any Ridge median below MINE's, so it did not test "almost comparable"; it now requires the best Ridge median to be no more than 0.1 below MINE's for each filter.
  - fig4-taylor-metric-ranks-predictors. The statement says the full expansion predicts the change in output well, which the criterion did not cover; the full-expansion r2 is now reported and named as not deciding, since the paper gives no level.
  - fig5fh-cortex-maps. The statement names the whisk map and the all-session maps, which the criterion did not cover; both are now shown and named as not deciding, as the paper judges them by eye or against Musall et al. 2019.
  - fig5i-cortex-receptive-fields. The criterion tested neither "biphasic", "excitation stronger than inhibition" nor "much sharper", which the statement and Results paragraph 4 state, and it allowed a future lag of 0.2 s where the paper says up to 100 ms. Added tests for all three (the ~1.5 s second peak widened by 10%) and set the lag to 100 ms widened by 10% plus one frame of the model's 15 Hz rate (processMusall.py, 150 timepoints for 10 s).
  - fig6f-reticulospinal-behavior. The 0.75 level of the alternative test is not the paper's; now said so.
  - fig6g-linear-model-bias. The statement says the linear model favors low complexity (Results, paragraph 6), which the criterion did not test; added the complexity 2 fraction against the all-neuron fraction.
  - figs6-stimulus-neuron-regions. The code restricts the enrichment to regions_for_overview; now said. The olfactory epithelium finding cites panel 1I (the mixed panel) and says "temperature-sensitive", while the code plots pure stimulus neurons there; both readings are now named.
  - fig7a-behavior-feature-regions. "Forebrain" was fixed to the telencephalon; forebrain also covers the diencephalon, so both readings are now named.
  - fig7c-receptive-field-types. "Enriched in the forebrain" was judged as the largest telencephalic fraction among four chosen clusters, a comparison the paper does not make. It is now the paper's sense of enrichment (Methods, Processing of zebrafish data), above the fraction of all pure stimulus neurons, with telencephalon or telencephalon plus diencephalon as readings.
  - fig7f-complexity-anatomy. The Results cite "Figure 7G", which does not exist; the criterion now says Figure 7F (complexity clustering, per its legend) is meant.
  - Added fig2s1-nonlinearity-metrics-agree (Figure 2, figure supplement 1D and E), fig3s1-white-noise-benchmark (Figure 3, figure supplement 1B) and fig3s1-training-length (Figure 3, figure supplement 1I and J). These are findings stated in the Results that had no claim. Their methods come from cnn_nonlin_test.py and cnn_sta_test.py at the cited commit, and the levels set here are named.
  - Checked, unchanged. Every quote and source against the text. The code details the criteria cite (sigma rule for the Bonferroni level, which gives 5 SDs for about 39,700 fit neurons and matches the printed 1.26e-6; UpSet minimum of 10 and six barcode columns; greedy clustering at 0.8 with minimum 25; enrichment over all fit neurons with 5000 draws; boot_complexity with 1000 draws; motor-type exclusivity; reticulospinal mask at 0.5 and the overwritten barcode line; mouse significance at 3 SE; top 10% pixels and two spectral clusters; 10 response-landscape clusters; LM threshold sqrt(0.5)). Checked at github.com/haesemeyer/mine_pub commit 368d756, which also confirms that the code lacks the analysis of lm-recovers-fewer-clusters.
  - Open. The PDF could not be rendered in this run, so the values the writer read from figures (Figure 6F bar counts behind 0.86, Figure 6G fractions, Figure 7E clusters 1, 2 and 9 below and cluster 6 near 1.4, the Figure 6E fish counts) were not checked.
  - Open. Figure supplements are online only and not under paper/; the claims on them rest on the Results sentences and the code.
  - Open. Several criteria use levels set in this file where the paper gives none (0.2 margin in fig1f, 0.8 in fig2bcd, 0.1 in fig3, 10% of peak in fig5i, 0.2 and 0.1 in figs6-train-test-uncorrelated, ratio bands in fig7d, 0.8 in fig7c, 5% in interaction-terms-small, 0.9 in fig3s1-white-noise-benchmark); each says so.
EOF
python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt; grep -n "—\|rather" claims/costabile-2023.yaml | head; python -c "
import yaml,re
d=yaml.safe_load(open('claims/costabile-2023.yaml'))
print(len(d['claims']))"
```

Result: not kept, because it reads the paper's text.

**Agent**

My text put ": " inside plain scalars. Fixing every occurrence.

**Agent calls Bash**

```bash
cd  awk 'NR>73' claims/costabile-2023.yaml | grep -n ": " | grep -v -E "^[0-9]+:\s*-? ?[a-z_]+: " | head -30
```

```
626:    paper's sense of enrichment (Methods, Processing of zebrafish data): each slow cluster's
```

**Agent calls Bash**

```bash
cd  sed -i 's/Processing of zebrafish data): each slow cluster/Processing of zebrafish data), so each slow cluster/' claims/costabile-2023.yaml; sed -n '/^checks:/,$p' claims/costabile-2023.yaml | grep -n "[^ ]: " | grep -v -E "^\s*[0-9]+:\s*-? ?[a-z_]+: "; python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt; grep -n "—\|rather" claims/costabile-2023.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I've corrected 11 claims and added 3, and the file is ready for an attempt. Nothing was committed or pushed; only `claims/costabile-2023.yaml` changed.

**Checker:** `claims/costabile-2023.yaml: 35 claims, 35 quotes, 0 statistical values, 0 problems`. It was 32 claims before my additions.

I read the full paper and the linked code at the cited commit (`mine_pub` 368d756). The code details the criteria cite match the code: the Bonferroni rule (5 SDs for about 39,700 fit neurons, matching the printed 1.26e-6), the UpSet minimum of 10, the cluster minimum of 25, the 5000-draw enrichment over all fit neurons, and the 3 SE significance rule for the mouse data, among others. The code indeed lacks the analysis behind `lm-recovers-fewer-clusters`. All quotes and sources were correct.

**Changes, by claim**
- **fig1f-mine-fits-ground-truth:** the "simple model fails in most types" test counted the pure-noise type, which no model can predict. It now counts the other seven types.
- **fig3-receptive-fields-slow-stimuli:** "within 0.1 of MINE's or below it" was met by any Ridge result below MINE's. It now requires the best Ridge result to be no more than 0.1 below MINE's for each filter.
- **fig4-taylor-metric-ranks-predictors:** the full-expansion fit is now reported, and marked as not deciding, since the paper gives no level for it.
- **fig5fh-cortex-maps:** the whisk map and the per-session maps from the statement are now shown and marked as not deciding; the paper judges them by eye.
- **fig5i-cortex-receptive-fields:** added tests for "biphasic" (second peak at about 1.5 s, widened by 10%), "excitation stronger than inhibition" and "much sharper". The grab future lag was 0.2 s; it is now the paper's 100 ms, widened by 10%, plus one 15 Hz frame (`processMusall.py`).
- **fig6f-reticulospinal-behavior:** the 0.75 level is now marked as set in this file, not the paper's.
- **fig6g-linear-model-bias:** added the low-complexity part of the statement (the complexity 2 fraction against the all-neuron fraction).
- **figs6-stimulus-neuron-regions:** now says the code restricts enrichment to its list of overview regions. For the olfactory epithelium, two readings are named: the code's pure stimulus neurons, or any temperature-driven neuron (the Results cite the mixed-selectivity panel).
- **fig7a-behavior-feature-regions:** "forebrain" can mean telencephalon only, or telencephalon plus diencephalon; both readings are now named.
- **fig7c-receptive-field-types:** "enriched in the forebrain" was judged by a ranking among four clusters, which the paper never does. It now uses the paper's own enrichment test, against all pure stimulus neurons, with both forebrain readings.
- **fig7f-complexity-anatomy:** the Results cite a "Figure 7G" that does not exist; the criterion now says Figure 7F is meant.
- **New claims** for three Results findings that had none, with methods from `cnn_nonlin_test.py` and `cnn_sta_test.py`:
  - `fig2s1-nonlinearity-metrics-agree`
  - `fig3s1-white-noise-benchmark` (the number of simulations is open: 100 in the Methods, 10 in the code)
  - `fig3s1-training-length`

**What remains open**
- I couldn't render the PDF here, so the values the first reader took from figures are unchecked: the Figure 6F counts behind 0.86, the Figure 6G fractions, the Figure 7E cluster values and the Figure 6E fish counts.
- The figure supplements are online only and not under `paper/`. The claims on them rest on the Results sentences and the code.
- Several criteria still use levels set in this file because the paper gives none. Each criterion says so.

**Ready:** yes. The `checks` entry records all of this with `ready: true`.

## End of run

45 turns, 5 minutes, $2.73 at API prices, result: success.
