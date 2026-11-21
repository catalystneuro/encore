# fritsche-2022 · claims · run 44863493314

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
cat claims/fouke-2025.yaml | head -150; wc -l claims/fouke-2025.yaml; cat papers/datasets/fritsche-2022.yaml 2>/dev/null; head -30 paper/*.txt; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk 'length>200' *.txt | head -c 90000
```

```
<persisted-output>
Output too large (70.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bssewuv0y.txt

Preview (first 2KB):
Visual processing is strongly influenced by recent stimulus history, a phenomenon termed adaptation. Prominent theories cast adaptation as a consequence of optimized encoding of visual information by exploiting the temporal statistics of the world. However, this would require the visual system to track the history of individual briefly experienced events, within a stream of visual input, to build up statistical representations over longer timescales. Here, using an openly available dataset from the Allen Brain Observatory, we show that neurons in the early visual cortex of the mouse indeed maintain long-term traces of individual past stimuli that persist despite the presentation of several intervening stimuli, leading to long-term and stimulus-specific adaptation over dozens of seconds. Long-term adaptation was selectively expressed in cortical, but not in thalamic, neurons, which only showed short-term adaptation. Early visual cortex thus maintains concurrent stimulus-specific memory traces of past input, enabling the visual system to build up a statistical representation of the world to optimize the encoding of new information in a changing environment.
...
</persisted-output>
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1350-21.2021.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1350-21.2021.txt",
 "offset": 319
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text is complete (Methods, Results, legends, tables; no supplement is referenced). The equations are missing from the text and there is no PDF. Next I'll try the linked code repository.

**Agent calls Bash**

```bash
curl -sIL https://doi.org/10.34973/kpt9-y956 | grep -i -E "^(HTTP|location)"; curl -sL https://doi.org/10.34973/kpt9-y956 | sed 's/<[^>]*>//g' | grep -v '^\s*$' | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://webdav.data.ru.nl/dccn/DSC_3018000.01_830_v1/; curl -s -X PROPFIND -H "Depth: 1" https://webdav.data.ru.nl/dccn/DSC_3018000.01_830_v1/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent**

The code collection is listable over WebDAV. I'll list it recursively, leaving out the data files.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://webdav.data.ru.nl; list(){ curl -s -X PROPFIND -H "Depth: 1" "$B$1" | grep -oP '(?<=<a:href>)[^<]+|(?<=<a:getcontentlength>)[^<]+'; }; 
q=(/dccn/DSC_3018000.01_830_v1/); while [ ${#q[@]} -gt 0 ]; do d=${q[0]}; q=("${q[@]:1}"); prev=""; for x in $(list "$d" | tail -n +2); do if [[ $x == */ ]]; then q+=("$x"); echo "$x"; elif [[ $x =~ ^[0-9]+$ ]]; then echo "  $prev $x"; else prev=$x; fi; done; done 2>&1 | head -200
```

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bhhchf25j.txt

Preview (first 2KB):
/dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/
/dccn/DSC_3018000.01_830_v1/models/
/dccn/DSC_3018000.01_830_v1/processed_data/
/dccn/DSC_3018000.01_830_v1/static_grating_analysis_scripts/
  /dccn/DSC_3018000.01_830_v1/LICENSE.txt 1959
  /dccn/DSC_3018000.01_830_v1/MANIFEST.txt 115348
  /dccn/DSC_3018000.01_830_v1/README.txt 3088
  /dccn/DSC_3018000.01_830_v1/CODELICENSE.txt 1296
  /dccn/DSC_3018000.01_830_v1/SUMMARY.txt 1720
  /dccn/DSC_3018000.01_830_v1/download_sessions.py 1226
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/.Rhistory 14445
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/a1_dg_adaptation_timecourse.py 17914
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/a2_dg_adaptation_timecourse.R 2874
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b1_dg_adaptation_tuning.py 17268
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b2_dg_adaptation_tuning.R 10376
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b3_dg_adaptation_tuning_anova.R 3039
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v processed_data /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bhhchf25j.txt | grep -v "/models/.*\.\(mat\|csv\)" | head -80; grep -c processed_data /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bhhchf25j.txt
```

```
/dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/
/dccn/DSC_3018000.01_830_v1/models/
/dccn/DSC_3018000.01_830_v1/static_grating_analysis_scripts/
  /dccn/DSC_3018000.01_830_v1/LICENSE.txt 1959
  /dccn/DSC_3018000.01_830_v1/MANIFEST.txt 115348
  /dccn/DSC_3018000.01_830_v1/README.txt 3088
  /dccn/DSC_3018000.01_830_v1/CODELICENSE.txt 1296
  /dccn/DSC_3018000.01_830_v1/SUMMARY.txt 1720
  /dccn/DSC_3018000.01_830_v1/download_sessions.py 1226
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/.Rhistory 14445
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/a1_dg_adaptation_timecourse.py 17914
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/a2_dg_adaptation_timecourse.R 2874
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b1_dg_adaptation_tuning.py 17268
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b2_dg_adaptation_tuning.R 10376
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/b3_dg_adaptation_tuning_anova.R 3039
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/c1_dg_n_back_adaptation.py 20567
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/c2_dg_n_back_adaptation_analysis_allstimuli.R 7478
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/c3_dg_n_back_adaptation_analysis.R 6284
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/c4_dg_exponential_decay_models.m 6023
  /dccn/DSC_3018000.01_830_v1/drifting_grating_analysis_scripts/c5_dg_single_double_exp_comparison.m 2877
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && B=https://webdav.data.ru.nl/dccn/DSC_3018000.01_830_v1; for f in README.txt SUMMARY.txt download_sessions.py $(grep -oP 'DSC_3018000.01_830_v1/\K(drifting|static)_grating_analysis_scripts/[^ ]+\.(py|R|m)' /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bhhchf25j.txt); do mkdir -p $(dirname $f); curl -s -o $f "$B/$f"; done; find . -type f | xargs wc -c | tail -1; cat README.txt SUMMARY.txt download_sessions.py
```

```
Exit code 2
3088 ./README.txt
# Citation

Fritsche, M. (Matthias), Samuel G. Solomon, Lange, F.P. de (Floris) (2021).
Brief stimuli cast a persistent long-term trace in visual cortex [Data set].
https://doi.org/10.34973/kpt9-y956.

# Abstract

Visual processing is strongly influenced by the recent stimulus history – a phenomenon termed adaptation. Prominent theories cast adaptation as a consequence of optimized encoding of visual information, by exploiting the temporal statistics of the world. However, this would require the visual system to track the history of individual briefly experienced events, within a stream of visual input, to build up statistical representations over longer timescales.  Here, using an openly available dataset from the Allen Brain Observatory, we show that neurons in the early visual cortex of the mouse indeed maintain long-term traces of individual past stimuli that persist despite the presentation of several intervening stimuli, leading to long-term and stimulus-specific adaptation over dozens of seconds. Long-term adaptation was selectively expressed in cortical, but not in thalamic neurons, which only showed short-term adaptation. Early visual cortex thus maintains concurrent stimulus-specific memory traces of past input, enabling the visual system to build up a statistical representation of the world to optimize the encoding of new information in a changing environment.

# Background information

You can find more information, including relevant publications pertaining to this dataset on the collection overview page at https://doi.org/10.34973/kpt9-y956.

A complete list of files that are part of this dataset can be found in the file MANIFEST.txt, including a SHA256 hash for each file to allow verification of correct data transfer.

# Restrictions on data access and reuse 

[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && B=https://webdav.data.ru.nl/dccn/DSC_3018000.01_830_v1; files="SUMMARY.txt download_sessions.py $(grep -oP 'DSC_3018000.01_830_v1/\K(drifting|static)_grating_analysis_scripts/\S+\.(py|R|m)' /home/runner/.claude/projects/-home-runner-work-encore-encore/f9efb935-feb8-44df-ac8f-4d4eaedf7142/tool-results/bhhchf25j.txt)"; echo $files | wc -w; for f in $files; do mkdir -p "$(dirname "$f")"; curl -s -w "%{http_code} $f\n" -o "$f" "$B/$f"; done
```

```
Exit code 18
33
401 SUMMARY.txt
401 download_sessions.py
401 drifting_grating_analysis_scripts/a1_dg_adaptation_timecourse.py
401 drifting_grating_analysis_scripts/a2_dg_adaptation_timecourse.R
401 drifting_grating_analysis_scripts/b1_dg_adaptation_tuning.py
401 drifting_grating_analysis_scripts/b2_dg_adaptation_tuning.R
401 drifting_grating_analysis_scripts/b3_dg_adaptation_tuning_anova.R
401 drifting_grating_analysis_scripts/c1_dg_n_back_adaptation.py
401 drifting_grating_analysis_scripts/c2_dg_n_back_adaptation_analysis_allstimuli.R
401 drifting_grating_analysis_scripts/c3_dg_n_back_adaptation_analysis.R
401 drifting_grating_analysis_scripts/c4_dg_exponential_decay_models.m
401 drifting_grating_analysis_scripts/c5_dg_single_double_exp_comparison.m
401 drifting_grating_analysis_scripts/c6_dg_exponential_decay_cortex_thalamus.m
401 drifting_grating_analysis_scripts/c7_dg_firing_rate_adaptation_scatterplots.R
401 drifting_grating_analysis_scripts/d1_dg_artificial_neuron_simulation.py
401 drifting_grating_analysis_scripts/d2_dg_nback_simulation.R
401 drifting_grating_analysis_scripts/e1_dg_cumulative_adaptation.py
401 drifting_grating_analysis_scripts/e2_dg_cumulative_adaptation_2.R
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -A "Mozilla/5.0" -o pmc.html https://pmc.ncbi.nlm.nih.gov/articles/PMC8916757/; ls -la pmc.html; grep -o '<math[^>]*alttext="[^"]*"' pmc.html | head; grep -c '<math' pmc.html; grep -o 'disp-formula[^>]*>' pmc.html | head
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'E'
import re,html
s=open('pmc.html').read()
for m in re.finditer(r'<math.*?</math>',s,re.S):
    t=re.sub(r'<annotation.*?</annotation>','',m.group(0),flags=re.S)
    t=re.sub(r'<mfrac>',' FRAC( ',t); t=re.sub(r'</mfrac>',' ) ',t)
    t=re.sub(r'<msub>',' SUB(',t);t=re.sub(r'</msub>',')',t)
    t=re.sub(r'<msup>',' SUP(',t);t=re.sub(r'</msup>',')',t)
    t=re.sub(r'<[^>]+>',' ',t); print(re.sub(r'\s+',' ',html.unescape(t)));print('--')
E
```

```
a d a p t a t i o n r a t i o = FRAC( f SUB( r r e p e a t ) f SUB( r o r t h o g o n a l ) ) , 
--
 r ( n ) = 1 − SUB( a f a s t ) * SUP( e − ( n − 1 ) / SUB( τ f a s t ) ) + SUB( a s l o w ) * SUP( e − ( n − 1 ) / SUB( τ s l o w ) ) , 
--
 SUB( τ f a s t ) 
--
 SUB( τ s l o w ) 
--
 r ( n ) = 1 − a * SUP( e − ( n − 1 ) / τ ) . 
--
 SUB( τ f a s t ) 
--
 SUB( τ s l o w ) 
--
 O S I = FRAC( f SUB( r p r e f e r r e d ) − f SUB( r n o n − p r e f e r r e d ) f SUB( r p r e f e r r e d ) + f SUB( r n o n − p r e f e r r e d ) ) , 
--
 a SUB( r 2 − 8 ) = ∏ n = 2 8 a SUB( r n ) , 
--
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 150,321p claims/fouke-2025.yaml; sed -n 1,80p tools/claims_check.py
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "kind\|'data'\|with_labels\|elsewhere\|ALLOWED\|allowed" tools/claims_check.py | head -40; ls schemas 2>/dev/null; grep -rln "claims" schemas docs 2>/dev/null | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/claims.schema.json
schemas/attempt.schema.json
docs/queue.md
docs/archives.md
docs/pilot-notes/knierim-2000-03.md
docs/pilot-notes/thompson-2026-01.md
docs/pilot-notes/markowitz-2023-01.md
docs/pilot-notes/lee-2025-01.md
docs/pilot-notes/richardson-2018-01.md
docs/pilot-notes/hulsey-2024-01.md
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json; curl -s https://api.dandiarchive.org/api/dandisets/000021/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name'])"; curl -s https://api.dandiarchive.org/api/dandisets/000021/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -rn -i "asymmetric\|inside the reported\|within the reported.*interval" claims/*.yaml | head -8; grep -rln "Paper run\|claude-opus" claims/*.yaml | head -3; head -12 claims/wang-2025.yaml
```

```
claims/andrews-2024.yaml:726:    when it falls inside ST5's 95% CI, which is asymmetric; the tolerances under expected are
claims/andrews-2024.yaml:861:  - waveform-gcl-association. The symmetric tolerances (half the CI width) did not agree with the rule that the odds ratio must fall inside ST5's asymmetric CI. The criterion now says the CI decides.
claims/boran-2022.yaml:151:    reading, both medians are within tolerance and both ranges are inside the reported ranges
claims/chandravadia-2020.yaml:231:- id: fig5b-roc-asymmetric
claims/chandravadia-2020.yaml:232:  statement: The ROC curve is asymmetric (p < 0.05), as expected for declarative memory.
claims/chandravadia-2020.yaml:234:  quote: Also, the shape of the ROC curve was asymmetric (Fig. 5b, p < 0.05), as expected for
claims/hernandez-perez-2020.yaml:352:  quote: theta was asymmetric at dorsal sites and significantly less so at relatively ventral sites,
claims/hernandez-perez-2020.yaml:353:    whether analyzed in terms of the asymmetric durations of the rise and decay (−0.43 [−0.57 –
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
# Claims for Wang, Kurgyis, Chen, Kang, Chen, Liu, Liu, Svoboda, Li & Druckmann (2025), "Brain-wide
# analysis reveals movement encoding structured across and within brain areas", Nature Neuroscience,
# doi:10.1038/s41593-025-02114-x, on dandiset 000363 (Mesoscale Activity Map Dataset), which the
# paper reuses.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
# protocol as stated in docs/protocol.md (pilot-18).
#
# Text read. The version of record (published 18 November 2025, open access), full text from the
# publisher's page: main text, figure legends, Methods, Extended Data Figs. 1 to 10 legends. The
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 12,60p claims/wang-2025.yaml; sed -n 715,735p claims/andrews-2024.yaml
```

```
# and 2) was read from its extracted text in the same file. The Reporting Summary and the three
# Supplementary Videos were not read; no claim rests on them. Figures were not opened; every
# number used below is printed in the text or a legend.
#
# Code read. github.com/druckmann-lab/MapVideoAnalysis at commit 7d27624 (7d276243db16db5af6da68a48de7720ef77007c2),
# the repository the paper links (Zenodo doi:10.5281/zenodo.16740762). It holds the package
# VideoAnalysisUtils (ridge prediction and explained variance, functions_for_r2.py; single-neuron
# choice and movement AUCs, functions_for_auc.py; area selection, nearest-neighbour and spatial
# uniformity tests, functions.py; figure classes and their statistics, plotting_utils.py, where
# the paper's Figs. 2, 4, 3, 5 and 7 are the classes Figure2, Figure3, Figure4, Figure7 and
# Figure6), the cluster scripts under Sherlock/ (train/test splits, ridge fits at each time shift,
# AUC runs) and figure notebooks under Notebooks/ with their printed outputs. The deep networks
# (autoencoder, end-to-end) are in a separate repository, github.com/kurgyis/BehaviorVideo, which
# could not be fetched (not public at the time of reading); a light version is at
# github.com/druckmann-lab/VideoAnalysisTools (commit 5850625), read only for its file list. The
# code that decodes choice from video (Fig. 6, the Calinski-Harabasz scores, the correlation with
# performance, and the single-trial video predictions used in Fig. 7) is not in either repository:
# MapVideoAnalysis reads its output from a precomputed file (cal4cat-delay.pickle). Details of Fig. 6
# that the Methods leave open are therefore open below.
# Where the Methods are silent the criteria follow this code and say so. Where the code differs from
[... 50 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/fritsche-2022.yaml",
 "content": "# Claims for Fritsche, Solomon & de Lange (2022), \"Brief Stimuli Cast a Persistent Long-Term Trace\n# in Visual Cortex\", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021, on dandiset\n# 000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1 Stimulus Set), which the\n# paper reuses.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol as stated in docs/protocol.md (pilot-18).\n#\n# Text read. The version of record, full text from PubMed Central (PMC8916757), in\n# paper/10.1523-jneurosci.1350-21.2021.txt: abstract, Introduction, Materials and Methods, Results,\n# Discussion, the legends of Figures 1 to 8 and Tables 1 and 2. The paper has no supplement. The\n# extracted text drops the display equations; these were read from the MathML of the same PMC page\n# (pmc.ncbi.nlm.nih.gov/articles/PMC8916757). They are (1) adaptation ratio = fr_repeat /\n# fr_orthogonal; (2) the double exponential, printed as r(n) = 1 - a_fast * exp(-(n-1)/tau_fast) +\n# a_slow * exp(-(n-1)/tau_slow); (3) the single exponential r(n) = 1 - a * exp(-(n-1)/tau); (4) OSI =\n# (fr_preferred - fr_non-preferred) / (fr_preferred + fr_non-preferred); (5) the cumulative ratio of\n# Fig. 4, ar_2-8 = product over n = 2 to 8 of ar_n. Figures were not opened (there is no PDF under\n# paper/); no number below is read from a figure.\n#\n# Code. The paper links its analysis code at the Donders Repository, doi:10.34973/kpt9-y956\n# (collection DSC_3018000.01_830, version 1). Its file list can be read without a login. It holds\n# download_sessions.py, drifting_grating_analysis_scripts/ (a1 to f3, Python, R and MATLAB: time\n# course, tuning and its ANOVA, n-back adaptation, exponential decay fits and their F tests, mouse\n# scatterplots, the artificial neuron simulation, cumulative adaptation, the blank baseline),\n# static_grating_analysis_scripts/ (a1 to c2, the same steps), models/ and processed_data/. Only\n# README.txt could be fetched; every script returned HTTP 401 (restricted access under a data use\n# agreement). The code was therefore not read, and no criterion below rests on it. Details the\n# Methods leave open are named as open, with the readings the text allows.\n#\n# Data the paper describes. The Allen Brain Observatory Visual Coding Neuropixels data (Siegle et\n# al., 2021), Brain Observatory 1.1 subset: 32 mice (16 C57BL/6J wild type, 6 Sst-IRES-Cre x Ai32,\n# 5 Pvalb-IRES-Cre x Ai32, 5 Vip-IRES-Cre x Ai32, either sex), all analysed regardless of line,\n# awake and passively viewing. The paper names DANDI 000021 as holding the NWB files. Stimuli used.\n# (a) Full-field drifting gratings, 2 s on, 1 s gray between; 0.04 cycles/degree, 80% contrast, 8\n# directions (0 to 315 degrees in 45 degree steps) and 5 temporal frequencies (1, 2, 4, 8, 15 Hz),\n# 15 repeats each, 600 presentations in three blocks, in random order with 30 interleaved blank\n# (gray) trials. Orientation is direction modulo 180; repeat means the same orientation (either\n# direction), orthogonal means 90 degrees apart; temporal frequency is ignored. (b) Static gratings,\n# 0.25 s each, back to back without gray; 6 orientations (0 to 150 degrees in 30 degree steps), 5\n# spatial frequencies (0.02 to 0.32 cycles/degree), 4 phases, about 50 repeats each, 6000\n# presentations in three blocks, blank sweeps about once every 25 gratings. Units. Spike-sorted\n# units with their area; kept when ISI violations <= 0.5, amplitude cutoff <= 0.1 and presence\n# ratio >= 0.9 (the AllenSDK defaults). Visually responsive units, separately per stimulus set, have\n# a mean rate to their preferred orientation above 5 Hz and above 1 SD of the rate in gray-screen\n# presentations, over 0 to 100 ms from onset (drifting) or 0 to 250 ms (static). Regions with at\n# least 50 responsive units are kept. For drifting gratings these are V1, LM, AL, RL, PM, AM\n# (cortex) and LGN (dorsolateral geniculate), LP (thalamus), 2365 responsive units in all (V1 562,\n# LGN 140, LP 90). For static gratings V1 has 530, LGN 60, LP 16; LP is dropped from the decay\n# analysis. Measure. The firing rate in 0 to 100 ms after onset (drifting) or 0 to 250 ms\n# (static); the adaptation ratio per unit is the rate when the n-back grating had the same\n# orientation as the current one over the rate when it was orthogonal, for n = 1 to 50.\n#\n# Details the paper leaves open, named in the criteria that use them.\n# O1 Ratio per unit. (a) The mean rate over all repeat trials over the mean over all orthogonal\n#   trials, pooling current orientations; (b) the ratio per current orientation, averaged (or\n#   geometric-mean averaged) over orientations.\n# O2 Region value. The paper tests log ratios against zero, so the region's ratio is (a) the\n#   exponent of the mean over units of the log ratio; or (b) the mean over units of the ratio.\n# O3 n-back position. (a) Blank trials hold a position in the sequence (supported by the blank\n#   baseline analysis, which uses \"n-back blank trial\" at \"the same n-back position\"), and pairs\n#   whose n-back trial is a blank are left out of repeat and orthogonal; (b) blanks are removed\n#   from the sequence first. Independently, (c) pairs are formed within each of the three blocks,\n#   or (d) across the whole concatenated sequence.\n# O4 Visual responsiveness. \"Larger than 1 SD of the firing rate during the first 100 ms of gray\n#   screen presentations\" is read as (a) above the gray mean plus 1 SD, or (b) above 1 SD itself;\n#   the gray presentations are (c) the blank trials of the same stimulus set, or (d) the session's\n#   spontaneous gray-screen epoch. The preferred orientation is taken over all trials of that\n#   orientation (both directions, all temporal frequencies).\n# O5 Exponential fit. Least squares on log ratios against the log of the model, over n = 1 to 50\n#   (Methods), with bounds a_fast, a_slow <= 0.5 and tau in [-50, 50]. The data fitted are (a) the\n#   region's mean log ratio at each n, or (b) every unit's log ratio at each n. The double\n#   exponential's second term is printed with a plus sign; readings (a) both terms reduce the\n#   response, r(n) = 1 - a_fast exp(-(n-1)/tau_fast) - a_slow exp(-(n-1)/tau_slow), which Tables 1\n#   and 2 support by giving both amplitudes as \"%-response reduction\"; (b) as printed. The F test\n#   compares the nested fits with the residual sums of squares and degrees of freedom of the data\n#   fitted under (a) or (b). The bootstrap resamples units with replacement 1000 times, drops fits\n#   on a bound, and takes the 2.5 and 97.5 percentiles.\n# O6 Correction. Where \"corrected for multiple comparisons\" names no method, the paper's stated\n#   method, Benjamini-Hochberg FDR at 0.05, is used; Bonferroni is a variant.\n#\n# A value with a bootstrapped 95% CI matches when it falls inside that CI; the tolerances given\n# under expected are the larger distance from the value to a CI bound, so they never reject a value\n# the CI accepts, and the CI decides where the two differ. Unit counts and other values without an\n# interval use 10%. A reported range is widened by 10% of each bound.\nschema_version: 2\npaper: doi:10.1523/jneurosci.1350-21.2021\nclaims:\n- id: units-responsive-count\n  statement: The drifting grating analysis rests on 2365 visually responsive neurons in visual\n    cortex and thalamus of 32 mice, with 562 in V1, 140 in LGN and 90 in LP.\n  source: Results, Orientation-specific adaptation in visual cortex and thalamus, paragraph 1;\n    Materials and Methods, Unit exclusion; Figure 1D\n  quote: we analyzed responses from a total of 2365 visually responsive neurons in the visual\n    cortex and thalamus of 32 mice\n  expected:\n  - quantity: visually responsive units, drifting gratings, regions with at least 50 units\n    value: 2365\n    tolerance: 236.5\n  - quantity: V1 responsive units, drifting gratings\n    value: 562\n    tolerance: 56.2\n  - quantity: LGN responsive units, drifting gratings\n    value: 140\n    tolerance: 14\n  - quantity: LP responsive units, drifting gratings\n    value: 90\n    tolerance: 9\n  criterion: Units pass the AllenSDK quality metrics named in the Methods (ISI violations, amplitude\n    cutoff, presence ratio) and the responsiveness rule of Unit exclusion (over 5 Hz and over 1 SD\n    of gray-screen rate in 0 to 100 ms, for the preferred orientation), in all 32 mice; regions\n    with at least 50 such units are kept. The readings of O4 are each run; the claim is reproduced\n    when under one reading all four counts are within tolerance, and the set of kept regions is\n    V1, LM, AL, RL, PM, AM, LGN and LP.\n- id: fig1d-v1-1back\n  statement: In V1 the immediate repetition of orientation reduces the early (0 to 100 ms) response\n    to drifting gratings by 17%, a 1-back adaptation ratio of 0.83.\n  source: Results, Orientation-specific adaptation in visual cortex and thalamus, paragraph 1;\n    Figure 1C and 1D\n  quote: Adaptation reduced the response by 17% in V1 (1-back adaptation ratio = 0.83, p = 4e-57, 95%\n    CI [0.81, 0.84])\n  statistics:\n  - test: two-tailed t test of log-transformed adaptation ratios against zero\n    p: 4.0e-57\n    corrected: FDR (Benjamini-Hochberg)\n    ci:\n      level: 0.95\n      low: 0.81\n      high: 0.84\n    n: 562 V1 units\n  expected:\n    quantity: V1 1-back adaptation ratio, drifting gratings\n    value: 0.83\n    tolerance: 0.02\n  depends_on:\n  - units-responsive-count\n  criterion: Per unit the ratio of O1, over 0 to 100 ms; the region value as O2; the t test of\n    unit log ratios against zero (Methods, Orientation-specific adaptation to drifting gratings).\n    Reproduced when, under one reading of O1 to O3, the value lies in [0.81, 0.84] and p < 0.05.\n- id: fig1d-extrastriate-1back\n  statement: Extrastriate areas show similar 1-back adaptation to drifting gratings, with ratios\n    between 0.80 and 0.88, all significant.\n  source: Results, Orientation-specific adaptation in visual cortex and thalamus, paragraph 1;\n    Figure 1D\n  quote: had a similar impact in higher-level extrastriate visual areas (Fig. 1D; 1-back adaptation\n    ratios between 0.80 and 0.88, all p values < 2e-21, two-sided t tests, corrected for multiple\n    comparisons)\n  statistics:\n  - test: two-sided t tests\n    p: 2.0e-21\n    p_relation: \"<\"\n    corrected: multiple comparisons (FDR, Benjamini-Hochberg, per the Methods)\n    n: units of LM, AL, RL, PM and AM\n  expected:\n  - quantity: lowest extrastriate 1-back ratio\n    value: 0.80\n    tolerance: 0.08\n  - quantity: highest extrastriate 1-back ratio\n    value: 0.88\n    tolerance: 0.088\n  depends_on:\n  - units-responsive-count\n  criterion: As fig1d-v1-1back, for LM, AL, RL, PM and AM. Reproduced when, under one reading,\n    every area's ratio lies in [0.72, 0.968] (the range widened by 10% of each bound) and is\n    significantly below 1 at p < 0.05 after correction.\n- id: fig1d-thalamus-1back\n  statement: LGN and LP also show orientation-specific 1-back adaptation to drifting gratings,\n    with ratios of 0.93 and 0.83.\n  source: Results, Orientation-specific adaptation in visual cortex and thalamus, paragraph 1;\n    Figure 1D\n  quote: We also found orientation-specific adaptation in the dorsolateral geniculate nucleus (LGN)\n    of the thalamus (n = 140; 1-back adaptation ratio = 0.93, p = 8e-7, 95% CI [0.91, 0.96]), and\n    the lateral posterior (LP) nucleus of the thalamus (n = 90; 1-back adaptation ratio = 0.83, p =\n    3e-10, 95% CI [0.79, 0.88])\n  statistics:\n  - about: LGN\n    test: two-tailed t test of log ratios against zero\n    p: 8.0e-7\n    ci:\n      level: 0.95\n      low: 0.91\n      high: 0.96\n    n: 140 LGN units\n  - about: LP\n    test: two-tailed t test of log ratios against zero\n    p: 3.0e-10\n    ci:\n      level: 0.95\n      low: 0.79\n      high: 0.88\n    n: 90 LP units\n  expected:\n  - quantity: LGN 1-back adaptation ratio, drifting gratings\n    value: 0.93\n    tolerance: 0.03\n  - quantity: LP 1-back adaptation ratio, drifting gratings\n    value: 0.83\n    tolerance: 0.05\n  depends_on:\n  - units-responsive-count\n  criterion: As fig1d-v1-1back. Reproduced when, under one reading, each value lies in its CI and\n    is significantly below 1 at p < 0.05.\n- id: fig1e-consistent-across-mice\n  statement: The 1-back response reduction is consistent across mice, in thalamus and in cortex.\n  source: Figure 1E; Results, Orientation-specific adaptation in visual cortex and thalamus,\n    paragraph 1\n  quote: The orientation-specific response reductions for immediate stimulus repetition were highly\n    consistent across mice (Fig. 1E).\n  depends_on:\n  - units-responsive-count\n  criterion: Per mouse, the average 0 to 100 ms firing rate of its responsive thalamic (LGN, LP)\n    and, separately, cortical units for 1-back repeat and orthogonal trials (Figure 1E legend).\n    The paper gives no test or count for \"consistent\". Readings, each run. (a) every mouse with\n    units in the group has orthogonal above repeat; (b) a two-sided sign test across mice at p <\n    0.05 with most mice above the diagonal. Reproduced when (a) holds in both groups; partially\n    reproduced when only (b) holds in one or both.\n- id: fig2-v1-tuning-main-effect\n  statement: In V1, 1-back adaptation is strongest when adaptor and test match the neuron's\n    preferred orientation and weakens for less preferred orientations, a main effect of relative\n    orientation.\n  source: Figure 2D to 2F legend; Materials and Methods, Orientation-specific adaptation to\n    drifting gratings, paragraph 3\n  quote: In V1 (D–F, far left columns), adaptation was strongest when adaptor and test stimuli\n    corresponded to the preferred orientation of the neuron and decreased when adapting and testing\n    with less preferred orientations (significant main effect of relative orientation, p = 4e-11)\n  statistics:\n  - test: 3 x 3 mixed ANOVA, main effect of relative adaptor/test orientation\n    p: 4.0e-11\n    n: V1 responsive units in three OSI tertiles\n  depends_on:\n  - units-responsive-count\n  criterion: Per region, units are split into OSI tertiles (OSI from the 0 to 100 ms rates to the\n    preferred orientation and its orthogonal, Methods). Per unit, the 1-back ratio for test\n    orientations at 0, 45 and 90 degrees from preferred, each the test orientation preceded by\n    itself over preceded by its orthogonal (Figure 2 legend). A mixed ANOVA with relative\n    orientation within units and OSI tertile between units. Open, each run. (a) the ANOVA on log\n    ratios (the paper's scale for all tests) or (b) on ratios; the 45 degree level (c) pools\n    test orientations at +45 and -45 degrees or (d) averages their two ratios; the preferred\n    orientation is taken from the same trials (the paper names no held-out set). Reproduced when\n    the main effect has p < 0.05 with the 0 degree ratio lowest, under one reading.\n- id: fig2-v1-tuning-interaction\n  statement: The dependence of V1 adaptation on relative orientation is strongest in highly\n    orientation-selective neurons (interaction of relative orientation and OSI).\n  source: Figure 2D to 2F legend\n  quote: This relationship was particularly strong in neurons exhibiting high orientation\n    selectivity (significant interaction between relative adaptor/test orientation and orientation\n    selectivity, p = 0.005\n  statistics:\n  - test: 3 x 3 mixed ANOVA, interaction of relative orientation and OSI tertile\n    p: 0.005\n  depends_on:\n  - fig2-v1-tuning-main-effect\n  criterion: The ANOVA of fig2-v1-tuning-main-effect. Reproduced when the interaction has p < 0.05\n    and the spread of ratios across relative orientations is largest in the high OSI tertile,\n    under one reading.\n- id: fig2-v1-adaptation-at-all-orientations\n  statement: V1 neurons adapt for all adaptor orientations relative to their preference, except\n    nonpreferred (90 degree) adaptor and test in the most selective units.\n  source: Figure 2D to 2F legend; Results, Orientation-specific adaptation in visual cortex and\n    thalamus, paragraph 1\n  quote: Nevertheless, there was clear adaptation for all adaptor orientations as indicated by\n    1-back adaptation ratios consistently smaller than one (all p values < 0.004, corrected for\n    multiple comparisons), except for nonpreferred (90°) adaptor and test stimuli of highly\n    selective units (F, far left column, 90°, p = 0.88).\n  statistics:\n  - about: eight of nine V1 tertile and relative orientation cells\n    test: t tests of log ratios against zero\n    p: 0.004\n    p_relation: \"<\"\n    corrected: multiple comparisons (method not named)\n  - about: high OSI tertile, 90 degrees\n    test: t test of log ratios against zero\n    p: 0.88\n  depends_on:\n  - fig2-v1-tuning-main-effect\n  criterion: Per V1 cell of tertile and relative orientation, a two-tailed t test of unit log ratios\n    against zero, corrected over the nine cells as O6. Reproduced when, under one reading of\n    fig2-v1-tuning-main-effect, the eight cells other than high OSI at 90 degrees are below 1 at\n    corrected p < 0.05 and that cell is not; partially reproduced when seven of the eight are.\n- id: fig2-thalamus-no-tuning-dependence\n  statement: In LGN and LP, 1-back adaptation does not depend on the adaptor and test orientation\n    relative to preference, nor does that dependence interact with orientation selectivity.\n  source: Figure 2D to 2F legend, two far right columns\n  quote: In thalamic areas (D–F, two far right columns), there was no evidence for a dependence of\n    adaptation on orientation preference (no significant main effects of relative adaptor/test\n    orientation, LGN, p = 0.28; LP, p = 0.91; no significant interactions between relative\n    adaptor/test orientation and orientation selectivity, LGN, p = 0.24; LP, p = 0.92)\n  statistics:\n  - about: LGN main effect of relative orientation\n    test: 3 x 3 mixed ANOVA\n    p: 0.28\n  - about: LP main effect of relative orientation\n    test: 3 x 3 mixed ANOVA\n    p: 0.91\n  - about: LGN interaction\n    test: 3 x 3 mixed ANOVA\n    p: 0.24\n  - about: LP interaction\n    test: 3 x 3 mixed ANOVA\n    p: 0.92\n  depends_on:\n  - fig2-v1-tuning-main-effect\n  criterion: A claim of absence, judged on the paper's test, the 3 x 3 mixed ANOVA of\n    fig2-v1-tuning-main-effect run in LGN and in LP at alpha 0.05. Reproduced when neither the main\n    effect of relative orientation nor its interaction with OSI tertile is significant in either\n    area; not reproduced when any is. The F values and the ratios per cell are reported either way.\n    The paper's quote reads \"orientation:\" where this file writes \"orientation,\"; see the inferred\n    note under checks if the checker reports it.\n- id: fig3a-v1-long-term\n  statement: V1 neurons adapt significantly to drifting gratings seen up to eight presentations (22\n    s) earlier, despite intervening stimuli.\n  source: Figure 3A; Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 1\n  quote: Surprisingly, we found that neurons in V1 exhibited significant adaptation effects to\n    stimuli seen up to eight presentations (or 22 s) in the past, despite the presentation of\n    multiple intervening stimuli (Fig. 3A).\n  statistics:\n  - test: two-tailed t tests of log ratios against zero, 1- to 10-back\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 562 V1 units\n  expected:\n    quantity: largest n-back with significant V1 adaptation\n    value: 8\n    tolerance: 1\n  depends_on:\n  - fig1d-v1-1back\n  criterion: Per unit and n the ratio of O1 conditioned on the n-back orientation; t tests of log\n    ratios against zero for n = 1 to 10 with FDR at 0.05 (Methods). The tolerance is one trial, as\n    10% of 8 is under one position. Reproduced when, under one reading of O1 to O3, the 8-back\n    ratio is significantly below 1 and the largest significant n is 7 to 9; partially reproduced\n    when significance reaches at least 5-back but the 8-back is not significant.\n- id: fig3a-v1-double-exponential\n  statement: The decay of V1 adaptation over n-back trials is captured by a double exponential with\n    a fast (13.99%, 0.85 trials) and a slow (3.45%, 6.82 trials) component.\n  source: Figure 3A legend; Table 1, row V1; Results, Long-term adaptation in visual cortex but not\n    in thalamus, paragraph 3\n  quote: The decay of adaptation over n-back trials was well captured by a double-exponential decay\n    model with a fast- and slow-decaying adaptation component (black dashed line; afast = 13.99%,\n    τfast = 0.85 trials, aslow = 3.45%, τslow = 6.82 trials).\n  statistics:\n  - about: tau_slow\n    ci:\n      level: 0.95\n      low: 3.39\n      high: 13.5\n  - about: a_fast\n    ci:\n      level: 0.95\n      low: 10.73\n      high: 16.14\n  - about: tau_fast\n    ci:\n      level: 0.95\n      low: 0.59\n      high: 1.13\n  - about: a_slow\n    ci:\n      level: 0.95\n      low: 1.71\n      high: 6.64\n  expected:\n  - quantity: V1 a_fast, drifting\n    value: 13.99\n    tolerance: 3.26\n    unit: \"%\"\n  - quantity: V1 tau_fast, drifting\n    value: 0.85\n    tolerance: 0.28\n    unit: trials\n  - quantity: V1 a_slow, drifting\n    value: 3.45\n    tolerance: 3.19\n    unit: \"%\"\n  - quantity: V1 tau_slow, drifting\n    value: 6.82\n    tolerance: 6.68\n    unit: trials\n  depends_on:\n  - fig3a-v1-long-term\n  criterion: The fit of O5 to V1 1- to 50-back ratios. Each estimate matches inside its CI from\n    Table 1. Reproduced when, under one reading of O1 to O3 and O5, all four estimates are inside\n    their CIs; partially reproduced when tau_slow is inside its CI and some other estimate is not.\n- id: fig3a-v1-half-life\n  statement: The slow component of V1 adaptation to drifting gratings has a half-life of about 14 s.\n  source: Discussion, paragraph 3\n  quote: This half-life is much shorter than the ∼14 s we observed in the current study.\n  expected:\n    quantity: half-life of the slow V1 component\n    value: 14\n    tolerance: 1.4\n    unit: s\n  depends_on:\n  - fig3a-v1-double-exponential\n  criterion: The paper does not give the conversion; the reading is tau_slow (trials) x 3 s per\n    trial (2 s grating and 1 s gray, Methods, Stimuli) x ln 2, which turns 6.82 trials into 14.2 s.\n    Reproduced when that value is within tolerance.\n- id: fig4-cumulative-adaptation\n  statement: Taken together, 2- to 8-back stimuli would reduce the V1 response by 19%, more than\n    the 17% reduction from the 1-back stimulus, assuming linear accumulation.\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 1; Figure 4A\n  quote: cumulative adaptation to the remote stimulus history outweighed the immediate adaptation\n    effect (17% response reduction to 1-back stimulus vs 19% cumulative response reduction to 2- to\n    8-back stimuli; Fig. 4)\n  expected:\n  - quantity: cumulative V1 response reduction, 2- to 8-back\n    value: 19\n    tolerance: 1.9\n    unit: \"%\"\n  - quantity: V1 response reduction, 1-back\n    value: 17\n    tolerance: 1.7\n    unit: \"%\"\n  depends_on:\n  - fig3a-v1-long-term\n  criterion: The reduction is 1 minus the product of the V1 region ratios for n = 2 to 8 (Figure 4\n    legend, equation from the PMC page). Reproduced when, under one reading of O1 to O3, both\n    values are within tolerance and the cumulative reduction exceeds the 1-back reduction.\n- id: fig4b-linear-accumulation\n  statement: When two adjacent past stimuli both had the current orientation, the observed\n    adaptation roughly matches that predicted by multiplying the single n-back effects, so\n    adaptation accumulates about linearly.\n  source: Figure 4B legend\n  quote: The empirically observed adaptation effect of two successive stimuli roughly matched the\n    predicted adaptation effect, suggesting that adaptation accumulates approximately linearly in\n    the current setting.\n  depends_on:\n  - fig3a-v1-long-term\n  criterion: In V1, trials whose n-back and (n+1)-back gratings both had the current orientation,\n    against trials where both were orthogonal, give the observed ratio; the product of the two\n    single ratios gives the prediction (Figure 4 legend). The legend does not say which adjacent\n    pairs are shown, nor what the baseline for the observed pair is. Readings, each run. Pairs (a)\n    1 and 2 back only, (b) every adjacent pair from 1-2 to 7-8; baseline (c) both orthogonal, (d)\n    the n-back orthogonal and the (n+1)-back any orientation. Reproduced when, under one reading,\n    each predicted value lies inside the 95% CI of the observed one (bootstrap over units).\n- id: fig3b-thalamus-short-term\n  statement: Adaptation to drifting gratings in the thalamus is limited to the 1-back trial in LGN\n    and the 2-back trial in LP, while cortical areas stay significant for about 6 to 8 trials.\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 2; Figure 3B\n  quote: In contrast to adaptation in cortex, adaptation in the thalamus appeared to be limited to\n    the 1-back (LGN) or 2-back trial (LP; Fig. 3B).\n  statistics:\n  - test: t tests of log ratios against zero, 1- to 10-back, per area\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR per area\n  depends_on:\n  - fig1d-thalamus-1back\n  - fig1d-extrastriate-1back\n  criterion: The t tests of fig3a-v1-long-term, per area for n = 1 to 10 with FDR per area (Figure\n    3B legend). Reproduced when, under one reading of O1 to O3, LGN has no significant n beyond 1,\n    LP none beyond 2, and each cortical area is significant at some n of 6 or more; partially\n    reproduced when one isolated later n is significant in LGN or LP.\n- id: v1-vs-thalamus-welch\n  statement: Adaptation to remote stimuli is stronger in V1 than in LGN (2-, 4- and 9-back) and LP\n    (3-back), even after normalizing to each region's 1-back adaptation.\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 2\n  quote: adaptation to temporally remote stimuli was significantly stronger in V1 compared with LGN\n    (2-, 4-, and 9-back stimulus, two-sided Welch's unequal variances t test, all p values < 0.02)\n    and LP (3-back stimulus, p = 0.001, corrected for multiple comparisons)\n  statistics:\n  - about: V1 against LGN, 2-, 4- and 9-back\n    test: two-sided Welch's unequal variances t test\n    p: 0.02\n    p_relation: \"<\"\n    corrected: multiple comparisons (method not named)\n    n: 562 V1 and 140 LGN units\n  - about: V1 against LP, 3-back\n    test: two-sided Welch's unequal variances t test\n    p: 0.001\n    corrected: multiple comparisons (method not named)\n    n: 562 V1 and 90 LP units\n  depends_on:\n  - fig3a-v1-long-term\n  - fig1d-thalamus-1back\n  criterion: Per n, a two-sided Welch t test of unit values in V1 against LGN, and against LP.\n    Open, each run. The normalization is (a) each unit's n-back log ratio divided by its own 1-back\n    log ratio, or (b) each unit's n-back log ratio divided by its region's mean 1-back log ratio;\n    the unnormalized test is also run, as \"even after\" implies it holds too. The tested n are (c)\n    2 to 10, the Methods' family for tests, or (d) 2 to 50; correction as O6 within each pair of\n    regions. Reproduced when, under one reading of normalization and n range, V1 adaptation is\n    significantly stronger than LGN at 2, 4 and 9 back and than LP at 3 back; partially reproduced\n    when at least one of these four holds.\n- id: fig3c-mice-long-term\n  statement: Long-term (4- to 8-back) adaptation is consistent across mice in cortex but not in\n    thalamus.\n  source: Figure 3C; Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 2\n  quote: Mice exhibit consistent long-term adaptation in cortex (right) but not in thalamus (left).\n  depends_on:\n  - fig3a-v1-long-term\n  criterion: Per mouse, the average firing rate of its cortical and, separately, its thalamic units\n    when the 4- to 8-back orientation was repeated against orthogonal (Figure 3C legend); whether\n    the five positions are pooled as trials or averaged as ratios is open and both are run. The\n    paper gives no test. Readings for cortex as in fig1e-consistent-across-mice. For thalamus,\n    \"not consistent\" is read as neither (a) nor (b) of that claim holding. Reproduced when cortex\n    meets (a) or (b) and thalamus meets neither.\n- id: decay-cortex-double-better\n  statement: Recovery from adaptation to drifting gratings in cortical areas is better fit by a\n    double than a single exponential, in all areas but RL.\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 3\n  quote: Recovery in cortical visual areas was better explained by double-exponential decay models,\n    with a fast and a slow-decaying adaptation component compared with a single-exponential decay\n    (F tests, all p values < 0.006, except RL, p = 0.072).\n  statistics:\n  - about: V1, LM, AL, PM, AM\n    test: F test of nested single- and double-exponential models\n    p: 0.006\n    p_relation: \"<\"\n  - about: RL\n    test: F test of nested single- and double-exponential models\n    p: 0.072\n  depends_on:\n  - fig3a-v1-double-exponential\n  criterion: Per area, the two fits and the F test of O5 over n = 1 to 50. Reproduced when, under\n    one reading of O1 to O3 and O5, the F test has p < 0.05 in V1, LM, AL, PM and AM; RL's p is\n    reported, and a significant RL is noted as a deviation from the paper's value only.\n- id: table1-extrastriate-tau-slow\n  statement: Extrastriate slow time constants for drifting gratings range from 3.12 to 5.52 trials,\n    with 95% CIs overlapping, close to V1's.\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 3; Table 1\n  quote: Recovery from adaptation was slowest in V1 with an exponential time constant τslow of 6.82\n    trials (bootstrapped 95% CI [3.39, 13.50]; Fig. 3A, black dashed line), but was relatively\n    similar for extrastriate areas (τslow ranging from 3.12 to 5.52 trials, all 95% CI intervals\n    overlapping; Table 1).\n  statistics:\n  - about: AL tau_slow\n    ci: {level: 0.95, low: 3.1, high: 5.94}\n  - about: AM tau_slow\n    ci: {level: 0.95, low: 2.37, high: 6.5}\n  - about: LM tau_slow\n    ci: {level: 0.95, low: 3.42, high: 10.6}\n  - about: PM tau_slow\n    ci: {level: 0.95, low: 2.75, high: 9.28}\n  - about: RL tau_slow\n    ci: {level: 0.95, low: 2.19, high: 34.41}\n  expected:\n  - {quantity: AL tau_slow, value: 4.08, tolerance: 1.86, unit: trials}\n  - {quantity: AM tau_slow, value: 3.39, tolerance: 3.11, unit: trials}\n  - {quantity: LM tau_slow, value: 5.52, tolerance: 5.08, unit: trials}\n  - {quantity: PM tau_slow, value: 4.43, tolerance: 4.85, unit: trials}\n  - {quantity: RL tau_slow, value: 3.12, tolerance: 31.29, unit: trials}\n  depends_on:\n  - decay-cortex-double-better\n  criterion: The double-exponential fit and bootstrap of O5 per area. Reproduced when, under one\n    reading, every area's tau_slow is inside its Table 1 CI and the five bootstrapped CIs and V1's\n    all overlap one another; partially reproduced when four of the five are inside. The other\n    Table 1 parameters (a_fast, tau_fast, a_slow) are reported against their CIs.\n- id: decay-thalamus-single\n  statement: Recovery in LGN and LP is best described by a single exponential with very short time\n    constants (0.02 and 0.71 trials).\n  source: Results, Long-term adaptation in visual cortex but not in thalamus, paragraph 3; Table 1\n  quote: In contrast, the recovery of adaptation in the thalamus was most parsimoniously captured by\n    a single-exponential decay model (F tests, p = 1 for both LGN and LP), and the time constants\n    of the single-exponential decays were very short (LGN, τfast = 0.02 trials, 95% CI [0.004,\n    0.63]; LP, τfast = 0.71 trials, 95% CI [0.03, 0.93]).\n  statistics:\n  - about: LGN and LP, double against single exponential\n    test: F test\n    p: 1\n  - about: LGN tau\n    ci: {level: 0.95, low: 0.004, high: 0.63}\n  - about: LP tau\n    ci: {level: 0.95, low: 0.03, high: 0.93}\n  expected:\n  - {quantity: LGN tau, single exponential, value: 0.02, tolerance: 0.61, unit: trials}\n  - {quantity: LP tau, single exponential, value: 0.71, tolerance: 0.68, unit: trials}\n  - {quantity: LGN amplitude a, value: 6.51, tolerance: 2.47, unit: \"%\"}\n  - {quantity: LP amplitude a, value: 16.76, tolerance: 4.26, unit: \"%\"}\n  depends_on:\n  - fig1d-thalamus-1back\n  criterion: The fits and F test of O5 in LGN and LP. Reproduced when, under one reading, the F\n    test is not significant (p >= 0.05) in both and each tau and amplitude is inside its Table 1\n    CI (LGN a_fast [4.04, 8.85], LP [12.68, 21.02]); partially reproduced when the F tests hold\n    and both taus are below 1 trial.\n- id: fig5-repeat-suppression\n  statement: Against a blank baseline, both repeated and orthogonal 1-back gratings suppress\n    cortical responses, but only the suppression by repeated orientations persists, up to eight\n    trials back.\n  source: Results, Cortical long-term adaptation is because of suppression following stimulus\n    repetitions; Figure 5\n  quote: Importantly, the suppressive effect of orthogonal orientations decayed quickly and was\n    limited to the 1-back trial, whereas the suppressive effect of repeated stimuli decayed more\n    slowly and remained significant for up to eight trials back (Fig. 5).\n  depends_on:\n  - fig3a-v1-long-term\n  criterion: All cortical units pooled (Figure 5 legend). Per unit and n, the rate when the n-back\n    trial was a repeat over the rate when it was a blank, and orthogonal over blank, with repeat\n    and orthogonal trials randomly subsampled to the number of n-back blank trials (Methods,\n    Dissociating adaptation). The paper does not name the test behind \"significant\". Readings,\n    each run. (a) the bootstrapped 95% CI over units (the Figure 5 error bars) excludes 1; (b)\n    t tests of log ratios against zero over n = 1 to 10 with FDR, as in the main analysis. The\n    subsample is drawn once with a fixed seed; the result over 100 draws is shown as a variant.\n    Reproduced when, under one reading, both 1-back ratios are below 1, orthogonal over blank is\n    not below 1 for any n from 2 to 10, and repeat over blank is below 1 at 8-back and at most\n    n from 2 to 8.\n- id: fig6c-static-v1-1back\n  statement: With brief back-to-back static gratings, orientation repetition reduces the V1\n    response over 0 to 250 ms, a 1-back ratio of 0.90.\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 1;\n    Figure 6B and 6C\n  quote: In V1 the repetition of stimulus orientation led to a clear reduction of the visual\n    response to the current grating (Fig. 6B, green shaded area; n = 530; adaptation ratio = 0.90,\n    p = 2e-81, 95% CI [0.89, 0.91]).\n  statistics:\n  - test: two-tailed t test of log ratios against zero\n    p: 2.0e-81\n    ci:\n      level: 0.95\n      low: 0.89\n      high: 0.91\n    n: 530 V1 units\n  expected:\n  - quantity: V1 1-back ratio, static gratings\n    value: 0.90\n    tolerance: 0.01\n  - quantity: V1 responsive units, static gratings\n    value: 530\n    tolerance: 53\n  criterion: As fig1d-v1-1back, with rates and responsiveness over 0 to 250 ms (Methods, Unit\n    exclusion and Orientation-specific adaptation to static gratings), orientations 90 degrees\n    apart as orthogonal, all spatial frequencies and phases pooled, and O3 read with blank sweeps\n    in place of blank trials. Reproduced when, under one reading, the ratio is in [0.89, 0.91], p <\n    0.05, and the count is within tolerance.\n- id: fig6c-static-other-areas-1back\n  statement: Extrastriate areas show similar 1-back adaptation to static gratings (0.89 to 0.93),\n    and the few responsive LGN and LP neurons also adapt (0.93 and 0.85).\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 1;\n    Figure 6C\n  quote: Very similar adaptation effects were found for extrastriate areas (Fig. 6C; 1-back\n    adaptation ratios between 0.89 and 0.93, all p values < 8e-9, two-sided t tests, corrected for\n    multiple comparisons) ... both LGN and LP exhibited significant adaptation effects (LGN −\n    adaptation ratio = 0.93, p = 0.004, 95% CI [0.93, 0.98]; LP – adaptation ratio = 0.85, p = 0.01,\n    95% CI [0.85, 0.96])\n  statistics:\n  - about: extrastriate areas\n    test: two-sided t tests\n    p: 8.0e-9\n    p_relation: \"<\"\n    corrected: multiple comparisons\n  - about: LGN\n    test: two-sided t test\n    p: 0.004\n    ci: {level: 0.95, low: 0.93, high: 0.98}\n    n: 60 LGN units\n  - about: LP\n    test: two-sided t test\n    p: 0.01\n    ci: {level: 0.95, low: 0.85, high: 0.96}\n    n: 16 LP units\n  expected:\n  - {quantity: lowest extrastriate 1-back ratio, static, value: 0.89, tolerance: 0.089}\n  - {quantity: highest extrastriate 1-back ratio, static, value: 0.93, tolerance: 0.093}\n  - {quantity: LGN 1-back ratio, static, value: 0.93, tolerance: 0.05}\n  - {quantity: LP 1-back ratio, static, value: 0.85, tolerance: 0.11}\n  - {quantity: LGN responsive units, static, value: 60, tolerance: 6}\n  - {quantity: LP responsive units, static, value: 16, tolerance: 1.6}\n  depends_on:\n  - fig6c-static-v1-1back\n  criterion: As fig6c-static-v1-1back. The printed LGN and LP values sit on the lower bound of their\n    CIs, so the CIs and the point values cannot both be met exactly; a thalamic value matches when\n    it is inside its CI widened down to the printed value minus 10%. Reproduced when, under one\n    reading, every extrastriate ratio is in the widened range [0.801, 1.023] and below 1 at p <\n    0.05, LGN and LP match and are below 1 at p < 0.05, and the counts are within tolerance.\n- id: fig6d-static-consistent-across-mice\n  statement: Static grating 1-back adaptation is consistent across mice.\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 1;\n    Figure 6D\n  quote: Mice show consistently reduced firing rates after a repeated versus orthogonal orientation,\n    as indicated by data points falling above the diagonal.\n  depends_on:\n  - fig6c-static-v1-1back\n  criterion: As fig1e-consistent-across-mice, over 0 to 250 ms of static gratings.\n- id: fig7a-static-v1-long-term\n  statement: After brief static gratings V1 adaptation persists for stimuli up to 20 presentations\n    (5 s) back, with a double exponential decay whose slow time constant is 9.12 trials.\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 2;\n    Figure 7A; Table 2, row V1\n  quote: Neurons in V1 showed significant adaptation effects to stimuli presented as far as 20\n    presentations (5 s) in the past (Fig. 7A,C, showing consistent adaptation across mice). Again,\n    the decay of adaptation was well described by a double exponential decay model with a long time\n    constant τslow = 9.12 trials (95% CI [6.09, 14.82]; Fig. 7A, black dashed line).\n  statistics:\n  - about: n-back significance\n    test: t tests of log ratios against zero\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  - about: tau_slow\n    ci: {level: 0.95, low: 6.09, high: 14.82}\n  - about: a_fast\n    ci: {level: 0.95, low: 7.11, high: 9.23}\n  - about: tau_fast\n    ci: {level: 0.95, low: 0.37, high: 0.71}\n  - about: a_slow\n    ci: {level: 0.95, low: 1.33, high: 2.91}\n  expected:\n  - {quantity: largest significant n-back in V1, static, value: 20, tolerance: 2}\n  - {quantity: V1 a_fast, static, value: 8.17, tolerance: 1.06, unit: \"%\"}\n  - {quantity: V1 tau_fast, static, value: 0.54, tolerance: 0.17, unit: trials}\n  - {quantity: V1 a_slow, static, value: 2.04, tolerance: 0.87, unit: \"%\"}\n  - {quantity: V1 tau_slow, static, value: 9.12, tolerance: 5.7, unit: trials}\n  depends_on:\n  - fig6c-static-v1-1back\n  criterion: As fig3a-v1-long-term and fig3a-v1-double-exponential, on 0 to 250 ms rates of static\n    gratings, fits over n = 1 to 50 (the static analyses follow the drifting ones, Methods). The\n    range of n entered in the FDR family is not stated for static gratings (the drifting family is\n    1 to 10, which cannot show 20-back); readings (a) 1 to 20, (b) 1 to 50. Reproduced when, under\n    one reading, 20-back is significant with the largest significant n in 18 to 22 (10% of 20),\n    and the four Table 2 V1 estimates are inside their CIs; partially reproduced when the\n    significance part holds and tau_slow alone is inside its CI.\n- id: fig7b-static-cortex-decay\n  statement: Extrastriate areas show similar decay after static gratings, with slow time constants\n    from 6.54 (AM) to 21.78 trials (PM), all better fit by a double exponential.\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 2;\n    Figure 7B; Table 2\n  quote: Higher-level extrastriate cortical areas showed similar decay dynamics (Fig. 7B), with\n    decay time constants ranging from 6.54 (AM) to 21.78 trials (PM; all 95% CI intervals\n    overlapping; Table 2). Although all cortical areas were significantly better fit by a double\n    exponential decay model (F tests, all p values < 1e-5)\n  statistics:\n  - about: double against single exponential, all cortical areas\n    test: F test\n    p: 1.0e-5\n    p_relation: \"<\"\n  - about: AL tau_slow\n    ci: {level: 0.95, low: 5.24, high: 39.75}\n  - about: AM tau_slow\n    ci: {level: 0.95, low: 3.82, high: 19.11}\n  - about: LM tau_slow\n    ci: {level: 0.95, low: 5.42, high: 13.36}\n  - about: PM tau_slow\n    ci: {level: 0.95, low: 13.07, high: 37.0}\n  - about: RL tau_slow\n    ci: {level: 0.95, low: 10.99, high: 37.51}\n  expected:\n  - {quantity: AL tau_slow, static, value: 14.79, tolerance: 24.96, unit: trials}\n  - {quantity: AM tau_slow, static, value: 6.54, tolerance: 12.57, unit: trials}\n  - {quantity: LM tau_slow, static, value: 7.74, tolerance: 5.62, unit: trials}\n  - {quantity: PM tau_slow, static, value: 21.78, tolerance: 15.22, unit: trials}\n  - {quantity: RL tau_slow, static, value: 19.58, tolerance: 17.93, unit: trials}\n  depends_on:\n  - fig7a-static-v1-long-term\n  criterion: The fits, F tests and bootstrap of O5 per cortical area on static gratings. Reproduced\n    when, under one reading, every cortical area (V1 included) has F test p < 0.05, and each\n    extrastriate tau_slow is inside its Table 2 CI with all CIs overlapping; partially reproduced\n    when the F tests hold and four of five taus are inside.\n- id: fig7-static-lgn-single\n  statement: After static gratings LGN is better described by a single exponential with a shorter\n    time constant (2.93 trials), and the cortex and thalamus difference is less pronounced than for\n    drifting gratings.\n  source: Results, Long-term adaptation following exposure to brief static gratings, paragraph 2;\n    Table 2, row LGN\n  quote: neurons in LGN were more parsimoniously described (p = 0.22) by a single exponential decay\n    with a shorter time constant (τfast = 2.93 trials, 95% CI [1.36, 7.32]), replicating the\n    experiment using drifting gratings. However, in this experiment, the difference in long-term\n    adaptation of cortex and thalamus was less pronounced than in the experiment using drifting\n    gratings.\n  statistics:\n  - about: LGN, double against single exponential\n    test: F test\n    p: 0.22\n  - about: LGN tau\n    ci: {level: 0.95, low: 1.36, high: 7.32}\n  expected:\n  - {quantity: LGN tau, static, value: 2.93, tolerance: 4.39, unit: trials}\n  - {quantity: LGN amplitude a, static, value: 3.91, tolerance: 2.68, unit: \"%\"}\n  depends_on:\n  - fig6c-static-other-areas-1back\n  criterion: The fits and F test of O5 in LGN on static gratings (LP is left out, Results). The\n    comparison of \"less pronounced\" is not tested in the paper and is reported only. Reproduced\n    when, under one reading, the F test has p >= 0.05 and tau and a are inside their Table 2 CIs\n    (a in [1.80, 6.59]).\n- id: fig8-no-spurious-long-term\n  statement: A simulated neuron with only 1-back adaptation, shown the experiments' own stimulus\n    sequences, shows no spurious adaptation to stimuli further back, for drifting or static\n    gratings.\n  source: Results, Short-term adaptation does not introduce spurious long-term adaptation effects;\n    Figure 8\n  quote: We observed no spurious long-term adaptation effects for this artificial neuron when\n    presented with the drifting grating sequences (Fig. 8A), nor when presented with the static\n    grating sequences (Fig. 8B)\n  criterion: For each of the 32 sessions' drifting and static grating sequences, a neuron that\n    responds equally to all orientations and is reduced only on a 1-back repeat, by the empirical V1\n    1-back ratio (Figure 8 legend), is analysed as the data are. The paper does not state the\n    response noise; readings (a) Poisson spike counts at a fixed rate, (b) no noise. The 95% CI is\n    taken across the 32 sequences (legend). Reproduced when, under one reading, the recovered\n    1-back ratio's CI contains the ground truth and every n-back ratio for n >= 2 has a CI that\n    contains 1, for both stimulus sets; partially reproduced when no more than one n in 2 to 10\n    excludes 1 at a ratio within 0.01 of 1.\n- id: robust-threshold-preferred-window\n  statement: The results are qualitatively similar with a responsiveness threshold of 2.5 or 10 Hz,\n    when only trials at the neuron's preferred orientation are used (drifting gratings), and with a\n    0 to 100 ms window for static gratings.\n  source: Materials and Methods, Unit exclusion and Orientation-specific adaptation to drifting\n    gratings, paragraph 4; Results, Orientation-specific adaptation in visual cortex and thalamus,\n    paragraph 1; Figure 7 legend\n  quote: we repeated the analyses with a more conservative (10 Hz) and less conservative (2.5 Hz)\n    threshold but obtained qualitatively similar results ... We did not observe qualitative\n    differences between the two analysis approaches.\n  depends_on:\n  - fig3a-v1-long-term\n  - fig3b-thalamus-short-term\n  - fig7a-static-v1-long-term\n  criterion: Each variant named in the Methods is run. Thresholds 2.5 and 10 Hz in place of 5 Hz.\n    The preferred-orientation analysis uses trials whose current orientation is the unit's\n    preferred and whose n-back is preferred (repeat) or orthogonal to it (Methods). Static\n    gratings over 0 to 100 ms. \"Qualitatively similar\" is read as V1 adaptation significant beyond\n    1-back (FDR as in the main analysis), V1 best fit by a double exponential, and, for drifting\n    gratings, no LGN n beyond 2 significant. For the static 0 to 100 ms window the paper says the\n    cortex and thalamus difference is less clear, so only the V1 parts apply. Reproduced when all\n    variants meet the reading; partially reproduced when most do.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The fig2-thalamus quote carried a paraphrase where the paper prints colons. I'll cut those spots with "..." and drop the note I left in that claim's criterion.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "    orientation, LGN, p = 0.28; LP, p = 0.91; no significant interactions between relative\n    adaptor/test orientation and orientation selectivity, LGN, p = 0.24; LP, p = 0.92)",
 "new_string": "    orientation ... LGN, p = 0.28; LP, p = 0.91; no significant interactions between relative\n    adaptor/test orientation and orientation selectivity ... LGN, p = 0.24; LP, p = 0.92)"
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": "    The F values and the ratios per cell are reported either way.\n    The paper's quote reads \"orientation:\" where this file writes \"orientation,\"; see the inferred\n    note under checks if the checker reports it.",
 "new_string": "    The F values and the ratios per cell are reported either way."
}
```

```
<tool_use_error>String to replace not found in file.
String:     The F values and the ratios per cell are reported either way.
    The paper's quote reads "orientation:" where this file writes "orientation,"; see the inferred
    note under checks if the checker reports it.</tool_use_error>
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/fritsche-2022.yaml paper/10.1523-jneurosci.1350-21.2021.txt; grep -n -- "—\|rather" claims/fritsche-2022.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/fritsche-2022.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker found commas inside flow mappings. I'll fix those and look for the stray note.

**Agent calls Bash**

```bash
cd claims; sed -i -E 's/quantity: ([^,]+), (single exponential|static), value/quantity: "\1, \2", value/' fritsche-2022.yaml; grep -n "inferred\|orientation,\"" fritsche-2022.yaml; cd ..; python tools/claims_check.py claims/fritsche-2022.yaml paper/10.1523-jneurosci.1350-21.2021.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/fritsche-2022.yaml",
 "offset": 300,
 "limit": 8
}
```

```
300	  - fig2-v1-tuning-main-effect
301	  criterion: A claim of absence, judged on the paper's test, the 3 x 3 mixed ANOVA of
302	    fig2-v1-tuning-main-effect run in LGN and in LP at alpha 0.05. Reproduced when neither the main
303	    effect of relative orientation nor its interaction with OSI tertile is significant in either
304	    area; not reproduced when any is. The F values and the ratios per cell are reported either way.
305	    The paper's quote reads "orientation:" where this file writes "orientation,"; see the inferred
306	    note under checks if the checker reports it.
307	- id: fig3a-v1-long-term
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/fritsche-2022.yaml",
 "old_string": " reported either way.\n    The paper's quote reads \"orientation:\" where this file writes \"orientation,\"; see the inferred\n    note under checks if the checker reports it.",
 "new_string": " reported either way."
}
```

```
The file claims/fritsche-2022.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/fritsche-2022.yaml paper/10.1523-jneurosci.1350-21.2021.txt; grep -nP "^\s+[a-z_]+: [^\"'{\[|>].*: " claims/fritsche-2022.yaml | head; grep -nP "^    [^ -].*[^\"]: " claims/fritsche-2022.yaml | head; grep -c "—" claims/fritsche-2022.yaml; grep -ci rather claims/fritsche-2022.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('claims/fritsche-2022.yaml'))
def w(x,p=''):
  if isinstance(x,dict): [w(v,p+'/'+str(k)) for k,v in x.items()]
  elif isinstance(x,list): [w(v,p+'/'+str(i)) for i,v in enumerate(x)]
  elif isinstance(x,str) and ': ' in x: print(p,x[:80])
w(d)"
```

```
(Bash completed with no output)
```

**Agent**

I wrote `claims/fritsche-2022.yaml`. The quote checker finds no problems (29 claims, 29 quotes, 80 statistical values), and no value contains ": ", an em dash or "rather". Nothing is committed.

**Text read.** The version of record (J Neurosci 2022, PMC8916757), all of it: Methods, Results, Discussion, the legends of Figs. 1 to 8, and Tables 1 and 2. The paper has no supplement. The text file had lost the display equations, and there is no PDF, so I read the five formulas from the MathML on the same PMC page: the adaptation ratio, the single and double exponential, the orientation selectivity index (OSI), and the cumulative product. I opened no figures.

**Code not read.** The paper's code is at doi:10.34973/kpt9-y956. Its file list is public, but every script returned HTTP 401 because it sits behind a data use agreement. No criterion rests on the code.

**Claims.** 29 claims, all with quotes (none inferred), 19 with statistics, 15 with expected values, and all 29 with a criterion. They cover:
- unit counts;
- 1-back adaptation in V1, the extrastriate areas and the thalamus, for drifting and for static gratings;
- consistency across mice (Figs. 1E, 3C, 6D);
- the Fig. 2 tuning ANOVA (main effect, interaction, adaptation at each orientation, and its absence in the thalamus);
- long-term adaptation in V1 (8-back for drifting, 20-back for static);
- the exponential fits and F tests from Tables 1 and 2, and the ~14 s half-life;
- cumulative adaptation and its linearity (Fig. 4);
- the V1 against thalamus Welch tests;
- the blank-baseline analysis (Fig. 5);
- the simulation with no spurious long-term effect (Fig. 8);
- the robustness variants.

All use `data: dataset`.

**Details the paper leaves open, with the readings named:**
- **O1, ratio per unit:** pool all current orientations, or compute the ratio per orientation and average.
- **O2, region value:** the exponent of the mean log ratio, or the mean of the ratios.
- **O3, n-back position:** blanks keep a place in the sequence or are removed; pairs are formed within each block or across the whole sequence.
- **O4, visual responsiveness:** "above 1 SD" means above the gray mean plus 1 SD, or above the SD itself; the gray reference is the blank trials or the spontaneous gray-screen epoch.
- **O5, exponential fit:**
  - the data fitted are the mean log ratio at each n, or every unit's log ratio;
  - the second term of the double exponential is printed with a plus sign: read as both terms reducing the response (which Tables 1 and 2 support) or as printed.
- **O6, correction:** where the paper names no method, the Benjamini-Hochberg FDR it uses elsewhere, with Bonferroni as a variant.
- **Per-claim gaps:**
  - what "consistent across mice" means: every mouse, or a sign test;
  - for the Fig. 2 ANOVA: log ratios or ratios, and how the ±45° tests are combined;
  - the normalization in the Welch tests and which n are tested (2 to 10, or 2 to 50);
  - which adjacent pairs Fig. 4B shows and what the baseline is;
  - the test behind significance in Fig. 5 (bootstrap CI, or t tests with FDR);
  - the FDR family for static gratings (1 to 20, or 1 to 50);
  - the noise in the Fig. 8 simulation (Poisson, or none);
  - the trial-to-seconds conversion behind the half-life (3 s per trial times ln 2).

**Missing from the paper that a claim needed:**
- **Region counts:** the per-region unit counts for LM, AL, RL, PM and AM are only in a figure, so they could not be used.
- **Thalamic CIs:** for static gratings, the LGN and LP ratios sit on the lower bound of their printed CIs (0.93 [0.93, 0.98] and 0.85 [0.85, 0.96]). The criterion therefore widens each CI down to the printed value minus 10%.
- **Code:** the analysis code needs a login, so no criterion could be checked against it.

## End of run

31 turns, 74 minutes, $2.04 at API prices, result: success.
