# andrews-2024 · claims-check · run 42836986405

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i andrews; cat claims/andrews-2024.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i andrews; wc -l claims/andrews-2024.yaml; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | head; ls paper | wc -l; sed -n 1,200p docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/andrews-2024.yaml paper/10.1038-s41593-024-01782-5.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/andrews-2024.yaml"
}
```

```
1	# Claims for Andrews, Geng, Voitiuk et al. (2024), Nature Neuroscience 27, 2487-2499,
2	# doi:10.1038/s41593-024-01782-5, tested on DANDI:001132.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, following docs/protocol.md (Reader). No data of the dandiset were seen; only its
6	# title and description on the archive ("HD-MEA recordings of human hippocampal brain slices
7	# obtained from epilepsy patients, including optogenetic stimulus and several
8	# hyperactivity-provoking conditions of culture medium").
9	#
10	# Text read: the NIH author manuscript in PubMed Central (PMC11881784, NIHMS2047739), full text
11	# with Methods, figure legends, Tables 1 and 2 and Extended Data legends, and its two supplement
12	# files from PMC: the Inventory of Supplemental Information (Extended Data and video legends)
13	# and Supplemental_Information.pdf (Supplemental Figs. S1 to S3, Supplemental Tables ST1 to
14	# ST6). The version of record was not read. The text cross-references its supplementary tables
15	# inconsistently (Extended Data legends point to ST4, ST5 and ST6 for the firing-rate p-values;
16	# the p-values are in ST2, ST3 and ST4; the Fig. 6 legend cites ST3 for a z-score that is in
17	# ST6; the Methods cite "Supplementary Table 2" for the ST5 odds ratios). The claims cite the
18	# tables by their content.
19	#
20	# Code read: https://github.com/braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit
[... 821 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-024-01782-5.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports one issue: a p-value it can't auto-match, which the file's own comment says was confirmed by reading. Now I'll read the rest of the paper.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1038-s41593-024-01782-5.txt').read(); print(t[53000:100000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7e87bd3e-b835-49c6-bc8b-cfb2c614a43e/tool-results/b8wj2fflc.txt"
}
```

```
1	t and calculation Power output for the optical fiber was measured with Thorlabs meter PM100D with sensor S130C. The power density (mW/mm 2 ) values of the light presented here were calculated by dividing the measured power by the cross-sectional area of the fiber, using this formula: For multimode fiber with ⊘200 µm core: Beam radius = r = ( 200 μ m 2 ) = 100 μ m = 0.100 m m Average power = P avg Surface power density = P a v g π r 2 = m W / m 2 where P avg is measured power and r is ½ the fiber core diameter. For additional information of how this data was collected, see Extended Data optogenetic power density measurement and calculation. A Python script was used to automatically control the light intensity with the Arduino and take samples with the Thorlabs PM100D, then plot the calibration curves for output power. The calibration data along with parameters of the hardware (the fiber core diameter, LED wavelength, LED driver max current limit, etc.) are saved in a separate calibration CSV file. The user must import the calibration data CSV file to start an experiment. Power density (mW/mm 2 ) is calculated each time by the Python script using the formula. The user can measure different LEDs and use the calibration files to convert between intensity (0–1 value) and mW/mm 2 values during experiments and analysis. Data Acquisition Neuronal activity was sampled simultaneously at 20kHz from multiple electrodes on the HD-MEA for both action potential and local field potential bandwidth. During the experiment, an activity scan assay using MaxLab Interface across all 26,400 electrodes was performed first, then a maximum of 1,024 available channels were manually selected to record from the most active areas spread across the MEA. Closed-loop seizure detection and optical intervention started after the assay from a custom Python script. After the experiment, raw activity data and optical stimulation timestamps were saved to an hdf5 file on local memory. The optical light 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1038-s41593-024-01782-5.txt').read()
i=t.find('Figure 1 |'); i=t.find('Fig. 1 |') if i<0 else i
import re
for m in re.finditer(r'(Figure|Fig\.) ?[1-6] ?\||Table [12] ?\||Supplemental Table ST|Supplemental Fig',t): print(m.start(), t[m.start():m.start()+60])
" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1038-s41593-024-01782-5.txt').read()
print(t[111984:126500]); print('=========='); print(t[160700:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
t=open('paper/10.1038-s41593-024-01782-5.txt').read()
i=t.find('Inventory of Supplemental Information',126000); print(i); print(t[145000:160700])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "low\|high\|range\|'p'\|\"p\"\|required\|checks\|ready\|changes" tools/claims_check.py | head -60; ls schemas 2>/dev/null; ls docs
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
38:    return re.sub(r"\s+", " ", s).strip().lower()
75:    return {f.lower() for f in out}
93:            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:6000])"; grep -rn "^checks:" -A12 claims/*.yaml | head -30
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
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1)[:5000])"
```

```
{
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
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 120 git clone -q https://github.com/braingeneers/AndrewsGengVoitiukEtAl_SourceCode code 2>&1 | tail -2; cd code 2>/dev/null && git log -1 --format='%H %ci' && ls
```

```
6865bf68cc3c8ea36a9b4f853b9248288fa1e52b 2025-11-30 22:34:52 -0800
Code_for_Figures
Optogenetic_Control
README.md
Seizure_Propagation
Simulation
Spike_Sorting_Curation
Theta_Wave_Videos
Waveform_Cluster
data
experiment_implementer
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; ls Waveform_Cluster Seizure_Propagation Optogenetic_Control Optogenetic_Control/* | head -40; grep -n "0.25\|seed\|random_state\|n_components\|bin\|0.01\|min_cluster\|epsilon" Waveform_Cluster/peristimulus.py | head -40
```

```
Optogenetic_Control/1_Test_Arduino.ipynb
Optogenetic_Control/20230404T172401-2023_04_04_example_opto_stim_log.csv
Optogenetic_Control/2_Experiment_Demo.ipynb
Optogenetic_Control/Experiment_2023_04_04_hc328_hckcr1-2.ipynb
Optogenetic_Control/Experiment_hckcr1_2023_04_02.ipynb
Optogenetic_Control/LICENSE
Optogenetic_Control/README.md
Optogenetic_Control/opto_hardware.py
Optogenetic_Control/optogenetics_enviroment.py
Optogenetic_Control/setup.sh

Optogenetic_Control:
1_Test_Arduino.ipynb
20230404T172401-2023_04_04_example_opto_stim_log.csv
2_Experiment_Demo.ipynb
3D_files
Arduino
Calibration
Experiment_2023_04_04_hc328_hckcr1-2.ipynb
Experiment_hckcr1_2023_04_02.ipynb
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 84,130p Waveform_Cluster/peristimulus.py; sed -n 150,205p Waveform_Cluster/peristimulus.py; ls Optogenetic_Control/Calibration
```

```
def normalized_psh(
    all_data, *, data_section, around_opto_end, peristim_length_bins, normalize
):
    # Gather the results into simple arrays.
    index_ranges = {}
    peristimulus = []
    total_fr = []
    for exp, data in all_data.items():
        peristimulus.append(data["peristimulus"])
        total_fr.append(data["firing_rates"])
        index_ranges[exp] = data["index_range"]
    peristimulus = np.vstack(peristimulus)
    total_fr = np.hstack(total_fr)

    # Select which part of the peristimulus to base normalization on.
    if data_section == "all":
        norm_base = peristimulus
    elif data_section not in ["opto", "control"]:
        raise ValueError(f"Unknown data section: {data_section}")
    else:
[... 95 more lines not kept]
```

**Agent**

The code repo is reachable at the cited commit. The peristimulus details in the file (100 ms bins, 0.25 Hz, seed 42, 5 dimensions, p < 0.01/n) match it. Now I'll check the propagation notebook.

**Agent calls Bash**

```bash
cd $TMPDIR/code; ls Seizure_Propagation; python - <<'E'
import json,glob,re
for f in glob.glob('Seizure_Propagation/*.ipynb'):
    nb=json.load(open(f))
    for c in nb['cells']:
        s=''.join(c['source'])
        for l in s.splitlines():
            if re.search(r'baseline|find_peaks|sigma|std|\b5\b|1\.5|15|20|hc11|Hc11',l): print(f.split('/')[-1][:30],'|',l.strip()[:150])
E
```

```
functions.py
seizure_propagation_paper_figure.ipynb
seizure_propagation_paper_figu | data_path = base_path + "data/Hc112723_hckcr1_21841_120323_base_cleaned.zip"
seizure_propagation_paper_figu | figure_name = "Hc112723_hckcr1_21841_120323_base"
seizure_propagation_paper_figu | fig, ax = plt.subplots(1, 1, figsize=(11, 5), constrained_layout=True)
seizure_propagation_paper_figu | ax2.plot(pe.bins, pe.fr, color='red', linewidth=3, alpha=0.5)
seizure_propagation_paper_figu | ax2.plot([t-0.5, t+0.5], [0.1*pfr, 0.1*pfr], '--', color='red', linewidth=3, alpha=0.5)
seizure_propagation_paper_figu | propa_duration = 1.5 # seconds
seizure_propagation_paper_figu | bin_num = 15    # 12
seizure_propagation_paper_figu | std_threshold = 3
seizure_propagation_paper_figu | propa_duration = 1.5 # seconds
seizure_propagation_paper_figu | bin_num = 15    # 12
seizure_propagation_paper_figu | std_threshold = 3
seizure_propagation_paper_figu | base_fr_tuple = namedtuple("base", ['mu', 'sigma'])
seizure_propagation_paper_figu | base_fr_lim = 5   # seconds for base firing rate calculation
seizure_propagation_paper_figu | rasterized = base_sd.raster(bin_size=propa_bin)   # use the same bin for baseline and burst
seizure_propagation_paper_figu | # get mean and std for each row of the rasterized data
seizure_propagation_paper_figu | sigma = np.std(rasterized, axis=1)
seizure_propagation_paper_figu | sd_burst[i]["base_fr"] = [base_fr_tuple(mu=mu, sigma=sigma) for mu, sigma in zip(mu, sigma)]
seizure_propagation_paper_figu | # find the max std away from the mean
[... 50 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "  statement: In physiologic media (slice 3C), 10 s of continuous 530 nm light reduces the\n    spontaneous firing of HcKCR1 slices, which recovers after light-OFF.",
 "new_string": "  statement: In physiologic media (slice 3C), 10 s of continuous 530 nm light reduces the\n    spontaneous firing of HcKCR1 slices; the rate after light-OFF is higher than during light-ON\n    (ST2)."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "  statement: In a ChR2-transduced slice (4C), 470 nm light increased unit firing, which returned\n    to baseline after light-OFF; spike amplitude did not change significantly.",
 "new_string": "  statement: In a ChR2-transduced slice (4C), 470 nm light increased unit firing; the rate after\n    light-OFF did not differ significantly from pre, and spike amplitude did not change\n    significantly between pre and light-ON."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "  statement: In 0-mg media, 2 of 4 slices (10F and 9E) showed clear spontaneous bursts of\n    activity lasting under 1 s and several minutes apart, like interictal spikes.",
 "new_string": "  statement: In 0-mg media, 2 of 4 slices showed clear spontaneous bursts of activity lasting\n    under 1 s and several minutes apart, like interictal spikes. 10F is one; the second is 9E in\n    Extended Data Fig. 9 and 11G in the Extended Data Fig. 5 legend."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    the peak for under 1 s, at least 1 minute apart. Reproduced when, under one reading, exactly\n    2 of 9E, 10F, 11G, 12G qualify and they are 10F and 9E; partially reproduced when 2 qualify\n    but not those two.",
 "new_string": "    the peak for under 1 s, at least 1 minute apart. Neither peak threshold nor the 1 minute\n    spacing is given by the paper, so the outcome rests on an assumption. The second slice is\n    open, readings 9E (Extended Data Fig. 9b) and 11G (Extended Data Fig. 5g, \"showing isolated\n    bursts of activity in trials T1 and T2\"). Reproduced when, under one reading, exactly 2 of\n    9E, 10F, 11G, 12G qualify and they are 10F with 9E or 10F with 11G; partially reproduced\n    when 2 qualify but not one of those pairs."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "  statement: During a 0-mg+KA burst in slice 10F, units exceeding 3 SD above baseline firing\n    activated in sequence from the hilar aspect of the granule cell layer to its outer aspect.",
 "new_string": "  statement: During a 0-mg+KA burst in slice 10F, the units exceeding 3 SD above baseline firing\n    suggested a progression from the hilar aspect of the granule cell layer to its outer aspect."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    histology in Fig. 1d and Fig. 4. Reproduced when each unit's first active sub-window",
 "new_string": "    histology in Fig. 1d and Fig. 4. The paper shows the progression in panels and gives no test;\n    the Spearman test below is an assumption. Reproduced when each unit's first active sub-window"
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    readings of zero-mg-isolated-bursts, a slice qualifying when it shows repeated bursts at\n    intervals under 60 s. Reproduced",
 "new_string": "    readings of zero-mg-isolated-bursts, a slice qualifying when it shows repeated bursts at\n    intervals under 60 s (the paper says only \"rhythmic\"; the 60 s bound is an assumption).\n    Reproduced"
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    Bursts from ka-rhythmic-bursts. Reproduced when, in 10F, mean K(t)",
 "new_string": "    Bursts from ka-rhythmic-bursts. The paper shows the coherence in panels and gives no test or\n    band limits other than theta; the test and the other bands below are assumptions.\n    Reproduced when, in 10F, mean K(t)"
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    binomial), p adjusted by Benjamini-Hochberg over 12 clusters (Methods). Tolerances are half\n    the width of ST5's 95% CI; the test is that the odds ratio falls inside the paper's CI. Open,",
 "new_string": "    binomial), p adjusted by Benjamini-Hochberg over 12 clusters (Methods). An odds ratio matches\n    when it falls inside ST5's 95% CI, which is asymmetric; the tolerances under expected are\n    half the CI width and stand in for it only where a symmetric bound is required, the CI\n    deciding where the two differ. Open,"
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "  - about: GCL waveform group in opto-response cluster 3\n    test: standardized residual, Bonferroni-adjusted critical value 3.23\n    statistic: z = 3.28\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n  expected:",
 "new_string": "  expected:"
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    clusters 5, 6, 8, 9, 10 merged into one GCL group; chisq.test on the contingency table;\n    standardized residuals (O - E)/sqrt(E) as the Methods write them, significant beyond 3.23\n    in magnitude. Open, HDBSCAN noise units, readings excluded and kept as a category.",
 "new_string": "    clusters 5, 6, 8, 9, 10 merged into one GCL group; chisq.test on the contingency table;\n    residuals significant beyond 3.23 in magnitude (ST6). Open, (1) the residual, readings\n    (O - E)/sqrt(E) as the Methods' formula writes it (chisq.test $residuals) and the\n    standardized residual the Methods name (chisq.test $stdres), which is larger in magnitude;\n    (2) HDBSCAN noise units, readings excluded and kept as a category."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/andrews-2024.yaml",
 "old_string": "    Reproduced when its mean pre-light rate is the highest or second highest of the 5 clusters\n    and its median relative reduction (pre - light-ON)/pre is smaller than that of every other\n    responsive cluster.",
 "new_string": "    The paper gives no measure for \"high\" and \"modest\"; the ranks below are an assumption.\n    Reproduced when its mean pre-light rate is the highest or second highest of the 5 clusters\n    and its median relative reduction (pre - light-ON)/pre is smaller than that of every other\n    responsive cluster."
}
```

```
The file claims/andrews-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now I'll add the checks entry and rerun the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/andrews-2024.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3a-spontaneous-reduction. The statement said firing "recovers after light-OFF"; the paper does not say so and ST2 gives pre against OFF as significant in 3C (adjusted p 1.26e-13). Now says the OFF rate is higher than the light-ON rate, which is what ST2 and the criterion test.
  - chr2-increase. "returned to baseline" is not in the paper; restated as the Extended Data Fig. 8 test gives it (pre against OFF not significant).
  - zero-mg-isolated-bursts. The paper names two different second slices. Extended Data Fig. 9 shows 10F and 9E; the Extended Data Fig. 5 legend shows isolated bursts in 10F and 11G. The claim fixed 10F and 9E and still cited Extended Data Fig. 5g; both pairs are now readings. Said that the peak thresholds and the 1 minute spacing are not from the paper.
  - fig4-firing-propagation. The statement said units "activated in sequence"; the paper says the plot "suggested a progression". Restated, and said that the Spearman test is an assumption since the paper gives no test. The 1.5 s, 15-window reading, 3 SD threshold and 5 s baseline were confirmed in seizure_propagation_paper_figure.ipynb at the cited commit.
  - ka-rhythmic-bursts, ka-theta-coherence, opto-cluster3-profile. Said that the 60 s burst interval, the coherence test and non-theta bands, and the rank rules for "high" and "modest" are not from the paper and are assumptions.
  - waveform-gcl-association. The symmetric tolerances (half the CI width) did not agree with the rule that the odds ratio must fall inside ST5's asymmetric CI. The criterion now says the CI decides.
  - opto-waveform-association. Removed the statistics entry with p < 0.05 for the residual; the paper reports a z of 3.28 against a Bonferroni critical value of 3.23, a threshold and not a reported p. The z stays under expected. The Methods give the formula (O - E)/sqrt(E) but call it a standardized residual, which in R's chisq.test is $stdres, a different quantity; both are now readings.
  - Open. The paper also reports that spike events in 0-mg media were not completely absent during light-ON in two slices (Fig. 3c t10, Extended Data Fig. 5d,g), and says they were too sparse to draw conclusions from. It has no claim; it is a minor observation.
  - Open. Discussion paragraph numbers in the sources could not be checked; the text has no paragraph breaks.
  - Open. The quote checker cannot match the p-value 3.634e-04 (waveform-gcl-association, cluster 10). It is printed so in ST5 and in the Fig. 5 legend.
  - Checked, unchanged. Every p-value, CI, odds ratio, unit count, Table 2 percentage and S3 value against the text and supplement, and the peristimulus.py parameters (100 ms bins, 0.25 Hz, seed 42, 5 UMAP dimensions, p < 0.01/n) in the code at commit 6865bf6.
EOF
python tools/claims_check.py claims/andrews-2024.yaml paper/10.1038-s41593-024-01782-5.txt; grep -n "—\|rather" claims/andrews-2024.yaml | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent**

I've checked the claims file against the paper and corrected it. It is ready for an attempt. Nothing is committed.

**Checker result:** `claims/andrews-2024.yaml: 29 claims, 29 quotes, 51 statistical values, 1 problems`. The one problem is the cluster 10 p-value (3.634e-04). The checker can't match that form, but ST5 and the Fig. 5 legend both print it, so it is correct.

**Changes, by claim:**
- **fig3a-spontaneous-reduction:** the statement said firing "recovers after light-OFF". The paper doesn't say that, and in ST2, pre against OFF is significant for 3C. It now says the OFF rate is higher than the light-ON rate, which is what the criterion tests.
- **chr2-increase:** "returned to baseline" isn't in the paper. It now says pre against OFF was not significant, as Extended Data Fig. 8 reports.
- **zero-mg-isolated-bursts:** the paper names two different second slices. Extended Data Fig. 9 shows 10F and 9E; the Extended Data Fig. 5 legend shows 10F and 11G. The claim fixed 9E but cited Fig. 5g, so both pairs are now readings. The criterion now says its burst thresholds and the 1-minute spacing are not from the paper.
- **fig4-firing-propagation:** "activated in sequence" became "suggested a progression", the paper's words. The criterion now says the Spearman test is an assumption. The window, the 3 SD threshold and the 5 s baseline match the propagation notebook at the cited commit.
- **ka-rhythmic-bursts, ka-theta-coherence, opto-cluster3-profile:** each criterion now says which of its tests, bounds and rank rules are assumptions and not taken from the paper.
- **waveform-gcl-association:** the symmetric tolerances conflicted with the rule that the odds ratio must fall inside ST5's asymmetric 95% CI. The criterion now says the CI decides.
- **opto-waveform-association:**
  - I removed the residual's "p < 0.05" entry. The paper reports z = 3.28 against a critical value of 3.23, which is a threshold and not a reported p-value. The z stays as an expected value.
  - The Methods' formula, (O − E)/√E, and their term "standardized residual" (R's `$stdres`) are different quantities, so both are now readings.

**Still open (recorded in the checks entry):**
- The paper also says spike events in 0-mg media did not stop completely during light-ON in two slices. That finding has no claim; I judged it minor.
- I couldn't check the paragraph numbers the sources give for the Discussion, because the text has no paragraph breaks.

All other values check out against the text, the supplement and the code at commit 6865bf6: p-values, CIs, odds ratios, unit counts, Table 2 percentages and the Supplemental Fig. S3 p-values.

## End of run

32 turns, 3 minutes, $1.78 at API prices, result: success.
