# peron-2020 · claims · run 42876919445

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; ls claims | head; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/; ls claims | head -30; wc -l paper/*
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
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2062-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2062-x.txt",
 "offset": 1162,
 "limit": 540
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the full text (version of record, with Methods, Extended Data legends and the reporting summary). Next, the data description and the linked code.

**Agent calls Bash**

```bash
cat paper/ssc-11.data-description.txt; cat papers/datasets/peron-2020.yaml 2>/dev/null; ls tools; cd $TMPDIR && git clone -q https://github.com/peronlab/ablation && git clone -q https://github.com/jwittenbach/ablation-sim; for d in ablation ablation-sim; do (cd $d; git log -1 --format='%H %ad'; git ls-files | head -80; git ls-files | wc -l); done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/ablation && wc -l *.m && cat get_settings.m get_anims.m get_data_path.m get_restricted_neurons.m get_rejects_based_on_shuffle.m
```

```
26 abl_print_fig.m
  117 ablation_figure_3d_plot.m
  190 ablation_figure_beh.m
  294 ablation_figure_correlation.m
  175 ablation_figure_distance.m
  239 ablation_figure_energy.m
  169 ablation_figure_score_change.m
  205 ablation_summ_stats.m
  361 get_ablation_data.m
   13 get_anims.m
  268 get_data_path.m
   17 get_rejects_based_on_shuffle.m
   52 get_restricted_neurons.m
   29 get_settings.m
 2155 total
function settings = get_settings
%
% This should be edited to point to the data and where intermediate files should go
%
%   settings.data_path: where data lives (top-level directory)
[... 374 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ablation && cat get_ablation_data.m ablation_figure_score_change.m ablation_summ_stats.m
```

```
<persisted-output>
Output too large (33.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/21eb8af0-65f0-43e2-ad8c-f9724eae4012/tool-results/bp62tb95y.txt

Preview (first 2KB):
function [data data_columns] = get_ablation_data (anim, abl, force_redo, suppress_output)
% 
% Returns a matrix with the requested data:
%
%   anim: string representation of animal -- EXCLUDES an
%   abl: which ablation ('touch', 'silent', 'whisking')
%   force_redo: regenerate data file (usually it just loads it and returns it)
%   suppress_output: silence text
%
% Columns in matrix specified in data_columns; data is matrix itself
%
%   abl_type: 0 = silent ; 1 = touch ; 2 = whisking
%   
    settings = get_settings;
    
    if (nargin < 3) ; force_redo = 0 ;end
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/21eb8af0-65f0-43e2-ad8c-f9724eae4012/tool-results/bp62tb95y.txt"
}
```

```
1	function [data data_columns] = get_ablation_data (anim, abl, force_redo, suppress_output)
2	% 
3	% Returns a matrix with the requested data:
4	%
5	%   anim: string representation of animal -- EXCLUDES an
6	%   abl: which ablation ('touch', 'silent', 'whisking')
7	%   force_redo: regenerate data file (usually it just loads it and returns it)
8	%   suppress_output: silence text
9	%
10	% Columns in matrix specified in data_columns; data is matrix itself
11	%
12	%   abl_type: 0 = silent ; 1 = touch ; 2 = whisking
13	%   
14	    settings = get_settings;
15	    
16	    if (nargin < 3) ; force_redo = 0 ;end
17	    if (nargin < 4) ; suppress_output = 1 ;end
18	
19	    % output directory for storing reduced data for fast access
20	    if (~exist(settings.processed_data_path,'dir'))
[... 716 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ablation && cat ablation_figure_distance.m ablation_figure_correlation.m
```

```
function ablation_figure_distance
%
% Distance-to-closest-ablated analyses
%

    t_color = [0 0.5 1];
    w_color = [0 0.8 0];

    abl_type = 'touch';
    anims = get_anims(abl_type);

    resp_type = 't'; % touch cells
    fh(1) = single_plot(resp_type, t_color, abl_type, anims, [-0.25 0.15]);
    print_fig (fh(1), ['distance_abl_' abl_type '_resp_' resp_type]);

    resp_type = 'w'; % whisking cells
    fh(2) = single_plot(resp_type, w_color, abl_type, anims, [-0.2 0.2]);
    print_fig (fh(2), ['distance_abl_' abl_type '_resp_' resp_type]);

    abl_type = 'silent'; % this is its own thing -- different
[... 450 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ablation && cat ablation_figure_beh.m; sed -n 1,239p ablation_figure_energy.m | head -120; head -40 ablation_figure_3d_plot.m
```

```
function ablation_figure_beh (force_redo)
%
% Looks at performance and kinematic parameters
%
    if (nargin < 1) ; force_redo = 0 ;end

    types = {'touch','whisking','silent'};

    for t=1:length(types)
        abl_type = types{t};
        anims = get_anims(abl_type);

        frac_corr_overall = [];
        touch_per_trial_overall = [];
        for a=1:length(anims)
            [frac_corr touch_per_trial] = plot_single_animal (anims{a}, abl_type, force_redo);
            frac_corr_overall = [frac_corr_overall ; frac_corr];
            touch_per_trial_overall = [touch_per_trial_overall ; touch_per_trial];
        end
        plot_overall(frac_corr_overall, touch_per_trial_overall, abl_type);
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ablation-sim && cat README.md; wc -l code/*.py; grep -n "def \|p_\|0\.2\|0\.4\|n_abl\|ablat" code/simulate.py | head -60; cat results/6-sweep/params.json | head -60
```

```
# ablation-sim
Simulating ablations in a balanced network of integrate-and-fire neurons

### organization
- code: code for running simulations
- templates: standard parameter configuration files
- results: notebooks, figures, and corresponding parameter settings

### notes
- due to size constraints, data used to produce results are not included in the repository 
  304 code/simulate.py
   70 code/sweep.py
  177 code/sweep_utils.py
  256 code/utils.py
  807 total
10:from utils import Bunch, xc_score, spike_score, psp_to_current, ablateNeuron
68:	Wee = psp_to_current(Jee, tauE/tauSynE)
69:	Wei = psp_to_current(Jei, tauI/tauSynE)
70:	Wie = psp_to_current(Jie, tauE/tauSynI)
71:	Wii = psp_to_current(Jii, tauI/tauSynI)
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "archive: crcns" claims/*.yaml | head -3; grep -h -A2 "^dataset:" $(grep -l "archive: crcns" claims/*.yaml | head -2); sed -n 1,60p tools/claims_check.py; grep -h "^  data: \|^  kind: " claims/*.yaml | sort | uniq -c
```

```
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
dataset:
  archive: crcns
  id: apl-1
--
dataset:
  archive: crcns
  id: ac-2
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import pprint
def walk(d,p=''):
    if isinstance(d,dict):
        if 'properties' in d: print(p, list(d['properties']), d.get('required'))
        for k,v in d.items(): walk(v,p+'/'+k)
    elif isinstance(d,list):
        for x in d: walk(x,p)
walk(s)"; grep -n "enum" -A3 schemas/claims.schema.json | head -40
```

```
['schema_version', 'dataset', 'paper', 'claims', 'checks'] ['schema_version', 'paper', 'claims']
/properties/dataset ['archive', 'id', 'doi'] ['archive', 'id']
/properties/dataset/if ['archive'] None
/properties/dataset/then ['id'] None
/properties/claims/items ['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where', 'datasets'] ['id', 'statement', 'source']
/properties/claims/items/allOf/if ['kind'] ['kind']
/properties/claims/items/allOf/if ['data'] ['data']
/properties/checks/items ['date', 'kind', 'model', 'by', 'ready', 'changes'] ['date', 'kind', 'ready']
/$defs/expected ['quantity', 'value', 'tolerance', 'unit'] ['quantity', 'value']
/$defs/statistic ['about', 'test', 'statistic', 'p', 'p_relation', 'corrected', 'ci', 'n'] None
/$defs/statistic/properties/ci ['level', 'low', 'high', 'unit'] ['low', 'high']
88:            "enum": [
89-              "finding",
90-              "link"
91-            ]
--
140:            "enum": [
141-              "dataset",
142-              "with_labels",
143-              "with_inputs",
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 120,175p schemas/claims.schema.json; grep -n "where" -B2 -A8 schemas/claims.schema.json | head -40
```

```
"type": "array",
            "minItems": 1,
            "items": {
              "$ref": "#/$defs/statistic"
            }
          },
          "criterion": {
            "description": "For a claim without a number, how it will be judged. Written before the analysis is run.",
            "type": "string"
          },
          "depends_on": {
            "description": "Ids of claims in this file whose result this one uses.",
            "type": "array",
            "items": {
              "type": "string",
              "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
            }
          },
          "data": {
            "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l -i "simulat" claims/*.yaml | head -5; grep -h -i -B3 -A12 "id: .*model" claims/*.yaml | grep -i -A3 "data:\|criterion" | head -30
```

```
claims/andrews-2024.yaml
claims/athalye-2023.yaml
claims/bouchard-2013.yaml
claims/bruno-2017.yaml
claims/buccino-2020.yaml
  criterion: >-
    The null model is build_mean_model of bayesian_cell_models.py (notebooks 20 and 27), fitted to
    the same summed counts. Each model is sampled as the Methods give it (NUTS in PyMC, 4 chains,
    1000 tuning steps, 1000 draws; target_accept 0.8 from sample_model) and compared by the
--
  data: with_labels
  depends_on:
  - session-list-link
  statement: A gradient-boosted tree model of the whisker-trial lick choice, from task, history and
--
  data: elsewhere
  where: Not deposited; generated by the paper's simulation code, gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f
    at revision f6a05661
  criterion: The paper's simulation gist at revision f6a05661, run 20 times (Methods, "Each simulation
    was repeated 20 times"), with its defaults (100 patterns, 100 repeats, 800 excitatory and 200 inhibitory
[... 15 more lines not kept]
```

**Agent**

Main text, Methods and code are read. The text garbles the P values in Fig. 2j–k and Fig. 3 and drops Extended Data Table 1, so I'll look at those PDF pages.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-s41586-020-2062-x.pdf')
for p in [3,4,14,15,18]:
    d[p-1].get_pixmap(dpi=130).save(f'p{p}.png')
" && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && for p in 3 4 14 15 18; do pdftoppm -f $p -l $p -r 110 -png paper/10.1038-s41586-020-2062-x.pdf pg$p; done; ls *.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2062-x.pdf",
 "pages": "3-4"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2062-x.pdf",
 "pages": "14-18"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install -q pymupdf 2>&1 | tail -1; cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-s41586-020-2062-x.pdf')
for p in [3,4,14,15,18]:
    d[p-1].get_pixmap(dpi=130).save(f'p{p}.png')
" && ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install pymupdf 2>&1 | tail -3; python -m pip --version; python -c "import pymupdf; print(pymupdf.__file__)"
```

```
Exit code 1

[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pymupdf; print(pymupdf.__file__)
    ^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pymupdf'
```

**Agent calls Bash**

```bash
pip install --target $TMPDIR/pylib pymupdf 2>&1 | grep -iv notice | tail -3; cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1038-s41586-020-2062-x.pdf')
for p in [3,4,14,15,18]:
    d[p-1].get_pixmap(dpi=130).save(f'p{p}.png')
" && ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf as fitz
d=fitz.open('paper/10.1038-s41586-020-2062-x.pdf')
pg=d[2]; r=pg.rect
clip=fitz.Rect(r.width*0.2, r.height*0.40, r.width*0.80, r.height*0.52)
pg.get_pixmap(dpi=300, clip=clip).save('jk.png')
pg=d[3]; r=pg.rect
pg.get_pixmap(dpi=200, clip=fitz.Rect(0,0,r.width,r.height*0.55)).save('fig3.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/jk.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/fig3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p15.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p18.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p14.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
grep -n "0.098\|0.863\|0.666\|0.065\|0.721\|0.710\|0.620\|0.039\|0.508\|0.453" paper/*.txt; sed -n 60,200p tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/ablation && sed -n 120,239p ablation_figure_energy.m
```

```
function [depth_cell success max_power_cell_watt net_energy_cell_joule] = get_single_animal_data(anim, abl_type)

    z0_um = 128;
    max_y = 600;

    data_type = 'jrc';
    nyu_anims = {'276013','276015','275801','275798','274577','274424','272761','278288','278759'};
    if (ismember(anim, nyu_anims)) ; data_type = 'nyu'; end

    [pre_path post_path abl_curation_file_path] = get_data_path(anim, abl_type);
    if (iscell(abl_curation_file_path) & length(abl_curation_file_path) > 1) ; abl_curation_file_path = abl_curation_file_path{1} ; end 
    [data dc] = get_ablation_data(anim,abl_type,0);
    cell_id_data = data(:,find(strcmp(dc,'cell_id')));
    y_data = data(:,find(strcmp(dc,'y_um')));
    z_offs = 15*(y_data/max_y); 
    depth_data = data(:,find(strcmp(dc,'z_um'))) + z0_um + z_offs;

    %% collect data -- all ablations, on a per-cell basis
    switch data_type
        case 'nyu'
[... 96 more lines not kept]
```

**Agent**

I have what I need: the paper's text, both code repositories, and the figure P values and Extended Data Table 1 from the PDF. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/peron-2020.yaml",
 "content": "# Claims for Peron, Pancholi, Voelcker, Wittenbach, Olafsdottir, Freeman & Svoboda (2020),\n# \"Recurrent interactions in local cortical circuits\", Nature 579, 256-259, on CRCNS ssc-11.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read: the version of record (paper/10.1038-s41586-020-2062-x.txt, supplied by a person,\n# extracted from the PDF), with the main text, figure legends, Methods, Extended Data Figs. 1-8\n# legends, Extended Data Table 1 and the reporting summary. The P values printed only inside\n# Figs. 2j, 2k, 3b, 3f, 3g and Extended Data Figs. 5 and 6, and the rows of Extended Data\n# Table 1, were read from the PDF pages, as the text extraction garbles or omits them. The\n# supplementary information named online is the reporting summary, which is in the text; no\n# other supplement is cited by the results.\n#\n# Code read. Analysis, github.com/peronlab/ablation at commit 74b7321 (74b732149ea5813c2394207f94a6a9e7f84d9bed,\n# 2020-02-16), MATLAB. It holds the mouse lists per ablation type (get_anims.m), the pre and\n# post data folders and ablation files per mouse (get_data_path.m), the per-neuron table of\n# touch and whisking scores, shuffle scores, event rates, positions and ablation flags\n# (get_ablation_data.m), the membership rule (get_restricted_neurons.m,\n# get_rejects_based_on_shuffle.m), Fig. 2j-l (ablation_figure_score_change.m), Fig. 2m and\n# Extended Data Figs. 3a and 5 (ablation_figure_distance.m), Fig. 3c-g\n# (ablation_figure_correlation.m), Extended Data Fig. 6 (ablation_figure_beh.m), Extended Data\n# Fig. 2 (ablation_figure_energy.m), Fig. 2h-i maps (ablation_figure_3d_plot.m) and the counts\n# quoted in the Results (ablation_summ_stats.m). Simulation, github.com/jwittenbach/ablation-sim\n# at commit a8b5583 (a8b5583ef8ac9b8ad1cfef883186e67763c925ef, 2016-02-05), Python with Brian.\n# Its parameter files (5,000 neurons, 4,000 excitatory, tauE 15 ms, ablation of 30 neurons)\n# are not those of the Methods (2,000 neurons, 1,700 excitatory, tau 30 ms, 20 ablated), so it\n# predates the published model; the model claims follow the Methods and use the repository only\n# for its structure (encoding score by cross-correlation, removal of outgoing synapses).\n#\n# Data the paper used. 16 mice (Extended Data Table 1; 15 male), two lines: j mice\n# (Emx1-IRES-cre x R26-LSL-H2B-mCherry, AAV2/1-syn-GCaMP6s) and n mice (Ai162 x\n# Slc17a7-IRES2-cre). IDs j250220, j257218, j257220, j258836, j271211, j278937, j278939,\n# j281915, n274424, n272761, n274577, n275801, n275798, n278288, n276013, n278759. Mice\n# performed a single-whisker object localization task (pole in proximal or distal positions,\n# lick right or left; sample, delay and response epochs). Two-photon volumetric imaging of L2/3\n# of the spared whisker's barrel column at 7 Hz, three 600 x 600 um planes 15 um apart per\n# subvolume, 4-6 subvolumes (12-18 planes, 180-270 um), about 50 trials per subvolume per day.\n# Pre-ablation and post-ablation data are each 2-4 sessions (typically 3), with the ablation\n# day between them. Ablation types (24 ablations in all): touch, 9 mice (code: 250220, 257220,\n# 258836, 271211, 281915, 274424, 272761, 274577, 275801); whisking, 7 mice (278937, 278939,\n# 281915, 275798, 278288, 276013, 278759); silent, 8 mice (257218, 258836, 271211, 278937,\n# 278939, 275801, 275798, 276013). Several mice had two ablations in sequence; the code takes\n# the post data of the first as the pre data of the second (get_data_path.m). Measured\n# variables, as the code reads them from the session files: per neuron, the touch encoding\n# score Rtouch (feature eventBasedDff_k16t14_<whisker>AbsMaxKappaZeroNotouchGLMScore), the\n# whisking score Rwhisking (eventBasedDff_k16t14_MeanWhiskerAmplitudeGLMScore), their shuffle\n# scores (GLMShuffleScore), the calcium event rate (eventRateHz), ROI positions, and\n# trial-averaged dF/F on correct left and right trials (dffBased_HitLTrialAvg,\n# dffBased_HitRTrialAvg); the ablation logs and the curation files flagging which targets were\n# ablated successfully; whisker angle, curvature at touch, touches and trial outcomes.\n#\n# Methods common to the experimental claims, from the Methods and the analysis code.\n# A neuron belongs to a representation when its score exceeds 0.1 and exceeds the 99th\n# percentile of the shuffle scores of the neurons in its subvolume and event-rate decile\n# (Methods, Neuronal classification; get_rejects_based_on_shuffle.m), in the pre-ablation\n# period, the post-ablation period or both (Methods; get_restricted_neurons.m). Neurons that\n# belong to both representations are left out (Methods; code). Ablated neurons (successful\n# targets in the curation file) are always left out, and so are neurons within a cylinder of\n# radius 10 um and height 60 um centred on an ablated neuron (Methods, Multiphoton ablation).\n# The code applies the cylinder as lateral distance < 10 um and signed depth difference < 30\n# um (get_ablation_data.m), which also drops every neuron shallower than the ablated one within\n# 10 um laterally; the Methods cylinder (|depth difference| < 30 um) is the main reading and\n# the code's rule a variant. For each mouse, the median of the included neurons' scores before\n# and after ablation; across mice, the grand median and the adjusted MAD (1.4826 x MAD); pre\n# against post by the Wilcoxon signed-rank test on the paired mouse medians; ablation types\n# compared by the Wilcoxon rank-sum test on the per-mouse changes (Methods, Statistical\n# analyses; ablation_figure_score_change.m). The response-similarity analysis uses an\n# encoding-score cutoff of 0.25 in place of 0.1, with the same shuffle rule (Methods; code).\n#\n# Tolerances. The +/- values the paper gives with its grand medians and means are the spread\n# across mice (adjusted MAD or s.d.), not an uncertainty of the statistic; as the attempt\n# reruns the same mice, the statistic itself should come out close, so each value takes 10% of\n# itself. Simulation values take 10% likewise, as the networks are random.\n#\n# Simulation claims (data elsewhere). The model outputs were not deposited; they are to be\n# regenerated from the Methods. Open in the Methods and not settled by the repository: the\n# input strength for Pconn 0.2 and 0.4, chosen as the one whose excitatory encoding-score\n# distribution \"most closely\" matched the in vivo data \"in terms of distribution shape and\n# fraction of neurons encoding the stimulus\". Readings: (a) the strength at which the fraction\n# of excitatory neurons with score above 0.1 equals the in vivo fraction of touch neurons\n# (0.108, Results); (b) the strength minimizing the Kolmogorov-Smirnov distance between the\n# model's excitatory score distribution and the pooled pre-ablation Rtouch of the touch\n# ablation mice. Also open, with no effect expected on the outcome, the stimulus interval\n# (20 s holds 66 presentations, so about 300 ms apart, as the repository's interval of 300\n# ms) and the random seeds.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: ssc-11\npaper: doi:10.1038/s41586-020-2062-x\nclaims:\n- id: model-amplification-increases\n  statement: In the L2/3 network model, the sensory input needed to match in vivo responses\n    declines as subnetwork connectivity rises, so amplification (network output over input,\n    normalized to Pconn 0.2) increases with subnetwork connectivity.\n  source: Results, paragraph 3; Figure 1c\n  quote: The strength of sensory input required to match in vivo responses declined with increasing\n    subnetwork connectivity. Amplification—defined as the ratio of network output to network\n    input—therefore increased with subnetwork connectivity\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model), with structure from\n    github.com/jwittenbach/ablation-sim at commit a8b5583\n  criterion: >-\n    The network of the Methods (2,000 leaky integrate-and-fire neurons; 200 input-recipient\n    excitatory, 1,500 other excitatory, 300 inhibitory; connection probabilities 0.2 among\n    excitatory and 0.6 for all with inhibitory; PSP 1 mV, and 1.6 mV within the subnetwork at\n    Pconn 0.4, linearly interpolated or extrapolated in between; beta(3,5) input peaking at 10\n    ms; Poisson background 5,000 Hz excitatory and 2,000 Hz inhibitory; dt 0.1 ms; 20 s per run).\n    The input strengths for Pconn 0.2 and 0.4 are set under each reading named in the opening\n    comment and interpolated linearly for other Pconn. Amplification is the inverse of input\n    strength normalized to Pconn 0.2 (Methods). Reproduced when amplification at Pconn 0.4 is\n    above that at 0.2 and rises across the Pconn values from 0.2 to 0.4 in steps of 0.05, under\n    the reading the author adopts.\n- id: model-equal-connectivity-ablation-increases\n  statement: In networks with equal subnetwork connectivity (Pconn 0.2), ablating the strongest\n    encoders raises the encoding scores of spared neurons, from 0.237 to 0.274, owing to reduced\n    feedback inhibition.\n  source: Results, paragraph 4; Figure 1d-f\n  quote: Encoding scores for spared neurons increased after simulated ablation of 10% of the subnetwork14,\n    owing to reduced feedback inhibition13,20 (encoding score, from 0.237 ± 0.027 to 0.274 ± 0.032\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 30 simulated networks\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  depends_on:\n  - model-amplification-increases\n  expected:\n  - quantity: grand median encoding score before ablation, Pconn 0.2\n    value: 0.237\n    tolerance: 0.024\n  - quantity: grand median encoding score after ablation, Pconn 0.2\n    value: 0.274\n    tolerance: 0.027\n  criterion: >-\n    Model as in model-amplification-increases at Pconn 0.2, 30 random networks. Encoding score\n    per neuron as the Methods define it (spikes convolved with a 20 ms s.d. Gaussian, rate and\n    stimulus downsampled to 0.5 ms, peak normalized cross-correlation within lags of 10 ms). The\n    20 excitatory neurons with the highest score are ablated by setting their outgoing synapses\n    to 0 (Methods, which fix 20; the Results say 10% of the subnetwork, also 20) and the run is\n    repeated. Neurons with score above 0.1 before or after, ablated neurons left out; per\n    network the median score before and after; grand median across networks; Wilcoxon\n    signed-rank test over networks. Reproduced when both grand medians are within tolerance and\n    the test gives an increase at p < 0.001.\n- id: model-increased-connectivity-ablation-decreases\n  statement: In networks with increased subnetwork connectivity (Pconn 0.4), ablation lowers the\n    encoding scores of spared neurons, from 0.243 to 0.143, because amplification is reduced.\n  source: Results, paragraph 5; Figure 1d-f\n  quote: Ablations reduced encoding scores for spared neurons, from 0.243 ± 0.049 to 0.143 ± 0.028\n    (connectivity = 0.4; P < 0.001, n = 30 networks), because of reduced amplification\n  statistics:\n  - test: Wilcoxon signed-rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 30 simulated networks\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  depends_on:\n  - model-amplification-increases\n  expected:\n  - quantity: grand median encoding score before ablation, Pconn 0.4\n    value: 0.243\n    tolerance: 0.024\n  - quantity: grand median encoding score after ablation, Pconn 0.4\n    value: 0.143\n    tolerance: 0.014\n  criterion: >-\n    As model-equal-connectivity-ablation-increases, at Pconn 0.4 with PSPs of 1.6 mV within the\n    subnetwork. Reproduced when both grand medians are within tolerance and the signed-rank test\n    gives a decrease at p < 0.001.\n- id: model-all-or-none-robust\n  statement: Subnetwork connectivity above 0.4 gives all-or-none responses, a transient input\n    driving the subnetwork into persistent activity, and such networks keep their all-or-none\n    response after ablation of 10% of the subnetwork.\n  source: Results, paragraphs 3 and 5; Extended Data Fig. 1 (Pconn 0.44)\n  quote: Networks in the all-or-none regime19 were robust to ablation, and maintained their all-or-none\n    response\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  criterion: >-\n    Model at Pconn 0.44 (Extended Data Fig. 1), with the input strength twice the extrapolated\n    value and a strong excitatory pulse to the inhibitory population 300 ms after each stimulus\n    onset (Methods). The pulse strength is not given; the reading used is the smallest pulse\n    that returns the subnetwork rate to its pre-stimulus level before the next stimulus.\n    All-or-none is read as a bimodal response, each stimulus either driving the subnetwork to a\n    sustained rate until the reset pulse or leaving it near baseline. Reproduced when this holds\n    before and after ablating the 20 strongest encoders, and the fraction of stimuli that\n    trigger the persistent state does not fall by more than half after ablation.\n- id: model-more-ablation-larger-decline\n  statement: In the model with Pconn 0.4, ablating more neurons (top 10, 20 or 50 encoders) gives\n    larger declines in encoding score, the change correlating with the net encoding score\n    ablated (R = -0.65).\n  source: Results, paragraph 7; Extended Data Fig. 4\n  quote: Correlation of net Rstimulus ablated and ΔRstimulus: R = −0.65, P < 0.01\n  statistics:\n  - test: Pearson correlation\n    statistic: R = -0.65\n    p: 0.01\n    p_relation: \"<\"\n    n: 30 networks per ablation size\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  depends_on:\n  - model-increased-connectivity-ablation-decreases\n  expected:\n  - quantity: Pearson R, net encoding score ablated against change in encoding score\n    value: -0.65\n    tolerance: 0.065\n  criterion: >-\n    Pconn 0.4, 30 networks for each of the top 0, 10, 20 and 50 neurons ablated (Methods list 0,\n    10, 20, 50 and 100; the legend omits sizes above 50 as unstable). Per network, the change in\n    median encoding score of spared neurons (score above 0.1 before or after) against the summed\n    pre-ablation score of the ablated neurons; Pearson correlation over all networks. Whether\n    the 0-ablation networks enter is open; both readings are run. Reproduced when R is within\n    tolerance with p < 0.01 under one reading, and the median change is more negative for each\n    larger ablation size.\n- id: model-slow-input-sensitive\n  statement: Networks with Pconn 0.4 given slower, whisking-like input (peak at 50 ms) are also\n    sensitive to ablation, encoding scores falling from 0.143 to 0.104.\n  source: Results, paragraph 9; Extended Data Fig. 8\n  quote: Change in encoding score after ablation: from 0.143 ± 0.024 to 0.104 ± 0.013, grand median\n    ± adjusted MAD. P < 0.001, Wilcoxon signed-rank test paired by network (n = 30 networks)\n  statistics:\n  - test: Wilcoxon signed-rank test, paired by network\n    p: 0.001\n    p_relation: \"<\"\n    n: 30 networks\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  expected:\n  - quantity: grand median encoding score before ablation, slow input, Pconn 0.4\n    value: 0.143\n    tolerance: 0.014\n  - quantity: grand median encoding score after ablation, slow input, Pconn 0.4\n    value: 0.104\n    tolerance: 0.010\n  criterion: >-\n    As model-increased-connectivity-ablation-decreases, with the beta(3,5) input stretched so\n    that it peaks 50 ms after onset (Methods). The input strength for slow input is not given;\n    readings are (a) the strength used for touch input at the same Pconn, and (b) a strength\n    set anew by the matching rule of the opening comment. Reproduced when, under one reading,\n    both grand medians are within tolerance and the signed-rank test gives a decrease at p <\n    0.001.\n- id: model-response-similarity\n  statement: In networks with increased subnetwork connectivity, neurons whose activity is more\n    similar to the mean activity of the ablated neurons lose the most encoding score after\n    ablation; with equal connectivity the relationship is absent.\n  source: Results, paragraph 10; Figure 3a, b\n  quote: In networks with increased subnetwork connectivity, neurons with high response similarity\n    showed the largest decline in encoding score after ablation (Fig. 3b). In networks without\n    increased subnetwork connectivity, the relationship disappeared\n  statistics:\n  - about: Pconn 0.4, slopes of change in encoding score against response similarity\n    test: sign test\n    p: 0.001\n    n: 30 networks, 3,466 neurons\n  - about: Pconn 0.2\n    test: sign test\n    p: 0.2\n    n: 30 networks, 3,779 neurons\n  data: elsewhere\n  where: Not deposited; generated by the model of the Methods (Network model)\n  depends_on:\n  - model-equal-connectivity-ablation-increases\n  - model-increased-connectivity-ablation-decreases\n  criterion: >-\n    Response similarity is the Pearson correlation of a neuron's Gaussian-convolved rate (20 ms\n    s.d.) with the mean convolved rate of the ablated neurons (Methods, Response similarity),\n    neurons with encoding score above 0.25 (Methods). Per network, a line is fitted to the\n    change in encoding score against response similarity; the Methods leave open whether to the\n    neurons or to means in 0.1-wide similarity bins, so both readings are run. Sign test of the\n    30 slopes against 0. Reproduced when at Pconn 0.4 the slopes are negative with p < 0.05 and\n    at Pconn 0.2 the sign test gives p >= 0.05.\n- id: neurons-per-mouse\n  statement: Volumetric imaging in L2/3 of the spared whisker's barrel column recorded 8,126 ±\n    2,436 (mean ± s.d.) neurons per mouse across 16 mice.\n  source: Results, paragraph 6; Extended Data Table 1\n  quote: 8,126 ± 2,436 (mean ± s.d.) neurons per mouse, n = 16 mice\n  expected:\n  - quantity: mean neurons imaged per mouse\n    value: 8126\n    tolerance: 813\n  - quantity: s.d. of neurons imaged per mouse\n    value: 2436\n    tolerance: 244\n  criterion: >-\n    The neuron count of a mouse is the number of neurons in its first pre-ablation data set,\n    before any exclusion (ablation_summ_stats.m, size of the per-neuron table, over each mouse's\n    first ablation). Mean and s.d. over the 16 mice. Reproduced when both are within tolerance;\n    the per-mouse counts are compared with the Cell count column of Extended Data Table 1.\n- id: representation-sizes\n  statement: Across 16 mice, 901 ± 539 of the imaged neurons encoded touch (fraction 0.108 ±\n    0.051) and 865 ± 364 encoded whisking (fraction 0.106 ± 0.028).\n  source: Results, paragraph 6\n  quote: Across 16 mice (Extended Data Table 1), 901 ± 539 of the imaged neurons encoded touch (fraction:\n    0.108 ± 0.051) and 865 ± 364 encoded whisking (fraction: 0.106 ± 0.028)\n  depends_on:\n  - neurons-per-mouse\n  expected:\n  - quantity: mean touch neuron count per mouse\n    value: 901\n    tolerance: 90\n  - quantity: mean touch neuron fraction\n    value: 0.108\n    tolerance: 0.011\n  - quantity: mean whisking neuron count per mouse\n    value: 865\n    tolerance: 87\n  - quantity: mean whisking neuron fraction\n    value: 0.106\n    tolerance: 0.011\n  criterion: >-\n    Counts from each mouse's first pre-ablation data set, mean and s.d. over 16 mice. The rule\n    for counting is open; the readings are (a) the code's, neurons with score above 0.1 alone,\n    without the shuffle test and without leaving out neurons in both representations or ablated\n    neurons (ablation_summ_stats.m, which notes that it does not exclude neurons of both types);\n    (b) the Methods membership rule (score above 0.1 and above the shuffle 99th percentile,\n    neurons in both representations and ablated neurons left out). Extended Data Table 1 gives\n    counts \"for the 0.1 encoding score criteria\" whose means over the 16 first rows are about\n    780 touch and 624 whisking, below the text's values, so the table may follow (b) and the\n    text (a). Reproduced when, under one reading, all four values are within tolerance.\n- id: touch-ablation-size\n  statement: Touch ablations removed 16.8 ± 12.8 strong touch neurons per mouse (about 6% of the\n    touch neurons of the barrel column, 9 mice), whose touch scores were at the 70th ± 35th\n    percentile.\n  source: Results, paragraph 7; Methods, Multiphoton ablation\n  quote: Ablating a small proportion of strong touch cells (16.8 ± 12.8 neurons, 6% of touch neurons\n    in the barrel column of the spared whisker, n = 9 mice; touch score, 70th ± 35th percentile)\n  expected:\n  - quantity: mean touch neurons ablated per mouse\n    value: 16.8\n    tolerance: 1.7\n  - quantity: s.d. of touch neurons ablated per mouse\n    value: 12.8\n    tolerance: 1.3\n  - quantity: mean ablated count as percentage of 287 touch neurons per barrel column\n    value: 6\n    tolerance: 0.6\n    unit: \"%\"\n  - quantity: mean percentile of ablated neurons' touch scores\n    value: 70\n    tolerance: 7\n  - quantity: s.d. of percentile of ablated neurons' touch scores\n    value: 35\n    tolerance: 3.5\n  criterion: >-\n    Ablated neurons are the successful targets of the curation files (get_ablation_data.m). The\n    percentage is the mean count over 287, the estimated touch neurons per barrel column\n    (Methods; ablation_summ_stats.m). The percentile of an ablated neuron is the rank of its\n    pre-ablation Rtouch among the included touch neurons' pre-ablation Rtouch of its mouse; mean\n    and s.d. over all ablated neurons pooled (ablation_summ_stats.m). Reproduced when all values\n    are within tolerance.\n- id: touch-ablation-reduces-touch\n  statement: Ablating touch neurons reduced the touch-encoding score of the spared touch neurons,\n    from 0.123 to 0.100 (grand median across 9 mice, 8,392 neurons).\n  source: Results, paragraph 7; Figure 2g, h, j\n  quote: The touch-encoding score (Rtouch) across touch neurons declined (from 0.123 ± 0.021 to 0.100\n    ± 0.037 (grand median ± adjusted MAD); n = 9 mice, 8,392 neurons, P = 0.004, Wilcoxon signed-rank\n    test for mouse medians, paired by mouse)\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.004\n    n: 9 mice, 8,392 neurons\n  depends_on:\n  - touch-ablation-size\n  expected:\n  - quantity: grand median Rtouch before touch ablation\n    value: 0.123\n    tolerance: 0.012\n  - quantity: grand median Rtouch after touch ablation\n    value: 0.100\n    tolerance: 0.010\n  - quantity: touch neurons included, all 9 mice\n    value: 8392\n    tolerance: 839\n  criterion: >-\n    The common method of the opening comment, touch neurons, touch ablation mice. Reproduced\n    when both grand medians are within tolerance and the signed-rank test on the paired mouse\n    medians gives a decline at p < 0.05. The neuron count is reported; the code's proximity rule\n    is run as a variant.\n- id: touch-ablation-touch-count\n  statement: After touch ablation the number of touch neurons fell, from 932 ± 634 to 716 ± 469\n    (mean ± s.d. over 9 mice), ablated neurons excluded.\n  source: Results, paragraph 7\n  quote: as did the touch neuron count (from 932 ± 634 to 716 ± 469 (mean ± s.d.), calculations\n    exclude ablated neurons)\n  depends_on:\n  - representation-sizes\n  expected:\n  - quantity: mean touch neuron count before touch ablation\n    value: 932\n    tolerance: 93\n  - quantity: mean touch neuron count after touch ablation\n    value: 716\n    tolerance: 72\n  criterion: >-\n    Per mouse, the touch neurons counted in the pre-ablation and in the post-ablation data\n    separately; mean over the 9 touch ablation mice. Readings for the count as in\n    representation-sizes, (a) the code's score above 0.1 alone (ablation_summ_stats.m, which\n    keeps ablated neurons although the text says they are excluded; run with them left out, as\n    the text says, and with them kept) and (b) the Methods membership rule in each period.\n    Reproduced when, under one reading, both means are within tolerance.\n- id: touch-ablation-whisking-unchanged\n  statement: Touch ablation did not change the whisking-encoding score of whisking neurons (0.116\n    to 0.115, 6,975 neurons, P = 0.820) or, materially, their count (775 ± 267 to 721 ± 241).\n  source: Results, paragraph 7; Figure 2i, k\n  quote: The whisking-encoding score (Rwhisking) did not change (from 0.116 ± 0.013 to 0.115 ± 0.024;\n    6,975 neurons, P = 0.820; neuron count: from 775 ± 267 to 721 ± 241)\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.82\n    n: 9 mice, 6,975 neurons\n  expected:\n  - quantity: grand median Rwhisking before touch ablation\n    value: 0.116\n    tolerance: 0.012\n  - quantity: grand median Rwhisking after touch ablation\n    value: 0.115\n    tolerance: 0.012\n  - quantity: whisking neurons included\n    value: 6975\n    tolerance: 698\n  - quantity: mean whisking neuron count before touch ablation\n    value: 775\n    tolerance: 78\n  - quantity: mean whisking neuron count after touch ablation\n    value: 721\n    tolerance: 72\n  criterion: >-\n    A claim of absence. The common method, whisking neurons, touch ablation mice; Wilcoxon\n    signed-rank test on paired mouse medians at the 0.05 level (the level at which the paper\n    calls its P values significant, Extended Data Fig. 6 legend). Reproduced when the test gives\n    p >= 0.05; the change is reported either way. Counts as in touch-ablation-touch-count.\n- id: ablation-size-correlation\n  statement: The decline in the touch representation grew with the touch representation ablated,\n    the change in Rtouch correlating with the net Rtouch ablated (R = -0.794 over all 24\n    ablations; R = -0.779 over the 9 touch ablations).\n  source: Results, paragraph 8; Figure 2l\n  quote: the decline in touch representation increased as more of the touch representation was ablated\n    (Pearson correlation of change in Rtouch and net Rtouch ablated, R = −0.794, P < 0.001 across\n    all 24 ablations; R = −0.779, P = 0.013 for the 9 touch cell ablations)\n  statistics:\n  - about: all 24 ablations\n    test: Pearson correlation\n    statistic: R = -0.794\n    p: 0.001\n    p_relation: \"<\"\n    n: 24 ablations\n  - about: touch ablations\n    test: Pearson correlation\n    statistic: R = -0.779\n    p: 0.013\n    n: 9 ablations\n  depends_on:\n  - touch-ablation-reduces-touch\n  - whisking-ablation-no-effect-touch\n  - silent-ablation-no-effect-touch\n  expected:\n  - quantity: Pearson R, all ablations\n    value: -0.794\n    tolerance: 0.079\n  - quantity: Pearson R, touch ablations\n    value: -0.779\n    tolerance: 0.078\n  criterion: >-\n    For each of the 24 ablations, the change in the mouse median Rtouch of touch neurons (common\n    method) against the net Rtouch ablated, the sum of the pre-ablation Rtouch of the ablated\n    neurons (Fig. 2l legend; ablation_figure_score_change.m). Pearson correlation over the 24\n    ablations and over the 9 touch ablations. Reproduced when both R are within tolerance with p\n    < 0.05 and negative.\n- id: distance-dependence-touch\n  statement: After touch ablation, touch neurons 15-35 um from the nearest ablated neuron lost\n    more Rtouch than those 115-135 um away (-0.132 against -0.056), and the effect decayed with\n    distance with a length constant of 87 um.\n  source: Results, paragraph 8; Figure 2m\n  quote: Touch neurons proximal (15–35 μm) to the ablated cells experienced a larger decline in Rtouch\n    values than those distal (115–135 μm) from the ablated cells (Fig. 2m). The effects of ablating\n    the touch neurons decayed over a distance (λ = 87 μm, exponential fit)\n  statistics:\n  - test: Wilcoxon signed-rank test for proximal versus distal medians, paired by mouse\n    p: 0.02\n    n: 9 mice\n  depends_on:\n  - touch-ablation-reduces-touch\n  expected:\n  - quantity: change in Rtouch, proximal (15-35 um)\n    value: -0.132\n    tolerance: 0.013\n  - quantity: change in Rtouch, distal (115-135 um)\n    value: -0.056\n    tolerance: 0.006\n  - quantity: exponential length constant\n    value: 87\n    tolerance: 8.7\n    unit: um\n  criterion: >-\n    Touch neurons of the touch ablation mice (common method); distance is the 3-D distance to\n    the closest ablated neuron (Fig. 2m legend; get_ablation_data.m), proximal 15-35 um and\n    distal 115-135 um. Per-mouse summary and the reported values are open: the legend says\n    \"proximal versus distal medians\" and \"grand median\"; the code takes per-mouse means for the\n    test and the median and MAD over all neurons pooled for the values\n    (ablation_figure_distance.m). Readings are (a) the code's and (b) per-mouse medians, with\n    the grand median over mice as the value. The length constant is 1/|b| of a fit a exp(b d) to\n    the cross-mouse mean of per-mouse mean changes in 25-um bins from 0 to 150 um (code).\n    Reproduced when, under one reading, proximal declines more than distal with p < 0.05, and\n    the two values and the length constant are within tolerance.\n- id: distance-dependence-whisking-absent\n  statement: Touch ablation produced no distance-dependent change in the whisking representation\n    (proximal 0.000, distal -0.023).\n  source: Results, paragraph 8; Extended Data Fig. 5\n  quote: Whisking neurons exhibited no distance-dependent changes\n  statistics:\n  - test: Wilcoxon signed-rank test comparing proximal paired to distal\n    p: 0.098\n    n: 9 mice\n  expected:\n  - quantity: change in Rwhisking, proximal (15-35 um)\n    value: 0.0\n    tolerance: 0.01\n  - quantity: change in Rwhisking, distal (115-135 um)\n    value: -0.023\n    tolerance: 0.0023\n  criterion: >-\n    A claim of absence. As distance-dependence-touch, for whisking neurons, Wilcoxon signed-rank\n    test of proximal against distal paired by mouse at the 0.05 level. Reproduced when p >=\n    0.05 under the code's reading (per-mouse means), with the per-mouse medians shown as a\n    variant. The proximal value is 0.000, so its tolerance is set at 0.01, the smallest\n    difference the paper's distance values resolve with meaning (distal -0.023). P = 0.098 is\n    read from the figure.\n- id: behaviour-unchanged\n  statement: Ablations did not change whisker movement or behaviour, so behaviour does not account\n    for the decline of the touch representation; no mouse showed a significant change in whisker\n    angle, angle at touch or curvature change at touch.\n  source: Results, paragraph 8; Extended Data Fig. 6\n  quote: The declining touch representation was not caused by changes in whisker movement or behaviour\n  statistics:\n  - about: fraction correct, touch ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.863\n    n: 9 mice\n  - about: touches per trial, touch ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.666\n    n: 9 mice\n  - about: fraction correct, silent ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.065\n    n: 8 mice\n  - about: touches per trial, silent ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.721\n    n: 8 mice\n  - about: fraction correct, whisking ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.71\n    n: 7 mice\n  - about: touches per trial, whisking ablations\n    test: Wilcoxon signed-rank test, paired by mouse\n    p: 0.62\n    n: 7 mice\n  criterion: >-\n    A claim of absence. Per mouse and ablation, fraction correct (correct over all scored trials)\n    and touches per trial (touches with bursts merged at a 50 ms intertouch interval) over all\n    pre and over all post sessions (ablation_figure_beh.m); Wilcoxon signed-rank test paired by\n    mouse, as the legend says, at the 0.05 level; the code's rank-sum test is a variant. Per\n    mouse, two-sample Kolmogorov-Smirnov tests of whisker angle, angle at touch onset and net\n    curvature change at touch, pre against post, on the samples (legend); the code's test on\n    normalized histograms is a variant. Reproduced when none of the six paired tests and no\n    mouse's KS tests give p < 0.05; partially reproduced when only the KS tests of some mice do\n    (with large samples a KS test can detect small shifts; the sizes are reported). P values\n    are read from the figure.\n- id: whisking-ablation-size\n  statement: Whisking ablations removed 12.7 ± 5.7 strong whisking neurons per mouse (about 4% of\n    the barrel column's whisking neurons, 7 mice), at the 66th ± 37th percentile of whisking\n    score.\n  source: Results, paragraph 9\n  quote: ablating a subset of strong whisking neurons (12.7 ± 5.7 neurons, approximately 4% of whisking\n    neurons in the barrel column of the spared whisker, n = 7 mice; whisking score: 66th ± 37th\n    percentile)\n  expected:\n  - quantity: mean whisking neurons ablated per mouse\n    value: 12.7\n    tolerance: 1.3\n  - quantity: s.d. of whisking neurons ablated per mouse\n    value: 5.7\n    tolerance: 0.6\n  - quantity: mean ablated count as percentage of 287\n    value: 4\n    tolerance: 0.4\n    unit: \"%\"\n  - quantity: mean percentile of ablated neurons' whisking scores\n    value: 66\n    tolerance: 6.6\n  - quantity: s.d. of percentile\n    value: 37\n    tolerance: 3.7\n  criterion: >-\n    As touch-ablation-size. For the percentile, the Methods reading ranks each ablated neuron's\n    pre-ablation Rwhisking among the included whisking neurons' Rwhisking; the code ranks it\n    among the included touch neurons' Rtouch (ablation_summ_stats.m), which is run as a variant.\n    Reproduced when the counts and percentage are within tolerance, and the percentile values\n    are under one of the two readings.\n- id: whisking-ablation-no-effect-touch\n  statement: Ablating whisking neurons had no effect on the touch representation (Rtouch 0.112 to\n    0.095, 7 mice, 5,866 neurons, P = 0.109; count 838 ± 401 to 899 ± 548).\n  source: Results, paragraph 9; Figure 2j; Extended Data Fig. 7\n  quote: produced no effect on either the touch representation (Rtouch from 0.112 ± 0.081 to 0.095\n    ± 0.069, n = 7 mice, 5,866 neurons; P = 0.109, count from 838 ± 401 to 899 ± 548)\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.109\n    n: 7 mice, 5,866 neurons\n  expected:\n  - quantity: grand median Rtouch before whisking ablation\n    value: 0.112\n    tolerance: 0.011\n  - quantity: grand median Rtouch after whisking ablation\n    value: 0.095\n    tolerance: 0.010\n  - quantity: touch neurons included\n    value: 5866\n    tolerance: 587\n  - quantity: mean touch neuron count before\n    value: 838\n    tolerance: 84\n  - quantity: mean touch neuron count after\n    value: 899\n    tolerance: 90\n  criterion: >-\n    A claim of absence. Common method, touch neurons, whisking ablation mice; signed-rank test\n    on paired mouse medians at the 0.05 level. Reproduced when p >= 0.05; the change is reported\n    either way. Counts as in touch-ablation-touch-count.\n- id: whisking-ablation-no-effect-whisking\n  statement: Ablating whisking neurons did not degrade the whisking representation (Rwhisking\n    0.108 to 0.107, 6,161 neurons, P = 0.812; count 880 ± 387 to 974 ± 558).\n  source: Results, paragraph 9; Figure 2k; Extended Data Fig. 7\n  quote: or the whisking representation (Rwhisking from 0.108 ± 0.076 to 0.107 ± 0.076, n = 6,161; P\n    = 0.812, count from 880 ± 387 to 974 ± 558)\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.812\n    n: 7 mice, 6,161 neurons\n  expected:\n  - quantity: grand median Rwhisking before whisking ablation\n    value: 0.108\n    tolerance: 0.011\n  - quantity: grand median Rwhisking after whisking ablation\n    value: 0.107\n    tolerance: 0.011\n  - quantity: whisking neurons included\n    value: 6161\n    tolerance: 616\n  - quantity: mean whisking neuron count before\n    value: 880\n    tolerance: 88\n  - quantity: mean whisking neuron count after\n    value: 974\n    tolerance: 97\n  criterion: >-\n    A claim of absence, as whisking-ablation-no-effect-touch, for whisking neurons. Reproduced\n    when p >= 0.05.\n- id: silent-ablation-size\n  statement: Silent-neuron ablations (event rate below 0.025 Hz) removed 16.3 ± 2.6 neurons per\n    mouse in 8 mice.\n  source: Results, paragraph 9; Methods, Multiphoton ablation\n  quote: ablating silent neurons (event rate below 0.025 Hz; 16.3 ± 2.6 neurons, n = 8 mice)\n  expected:\n  - quantity: mean silent neurons ablated per mouse\n    value: 16.3\n    tolerance: 1.6\n  - quantity: s.d. of silent neurons ablated per mouse\n    value: 2.6\n    tolerance: 0.3\n  criterion: >-\n    Successful targets in the curation files of the 8 silent ablation mice. Reproduced when both\n    values are within tolerance, and the ablated neurons' pre-ablation event rates are reported\n    against the 0.025 Hz targeting rule.\n- id: silent-ablation-no-effect-touch\n  statement: Ablating silent neurons did not change the touch representation (Rtouch 0.115 to\n    0.107, 8 mice, 7,110 neurons, P = 0.383; count 889 ± 713 to 926 ± 681).\n  source: Results, paragraph 9; Figure 2j; Extended Data Fig. 7\n  quote: did not change the touch representation (Rtouch from 0.115 ± 0.021 to 0.107 ± 0.023, n = 8\n    mice, 7,110 neurons; P = 0.383, count from 889 ± 713 to 926 ± 681)\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.383\n    n: 8 mice, 7,110 neurons\n  expected:\n  - quantity: grand median Rtouch before silent ablation\n    value: 0.115\n    tolerance: 0.012\n  - quantity: grand median Rtouch after silent ablation\n    value: 0.107\n    tolerance: 0.011\n  - quantity: touch neurons included\n    value: 7110\n    tolerance: 711\n  - quantity: mean touch neuron count before\n    value: 889\n    tolerance: 89\n  - quantity: mean touch neuron count after\n    value: 926\n    tolerance: 93\n  criterion: >-\n    A claim of absence. Common method, touch neurons, silent ablation mice; signed-rank test at\n    the 0.05 level. Reproduced when p >= 0.05. Counts as in touch-ablation-touch-count.\n- id: silent-ablation-no-effect-whisking\n  statement: Ablating silent neurons did not change the whisking representation (Rwhisking 0.115\n    to 0.114, 7,684 neurons, P = 0.844; count 961 ± 464 to 904 ± 384).\n  source: Results, paragraphs 9 and 10\n  quote: or the whisking representation (Rwhisking from 0.115 ± 0.014 to 0.114 ± 0.015, 7,684 neurons;\n    P = 0.844, count from\n  statistics:\n  - test: Wilcoxon signed-rank test for mouse medians, paired by mouse\n    p: 0.844\n    n: 8 mice, 7,684 neurons\n  expected:\n  - quantity: grand median Rwhisking before silent ablation\n    value: 0.115\n    tolerance: 0.012\n  - quantity: grand median Rwhisking after silent ablation\n    value: 0.114\n    tolerance: 0.011\n  - quantity: whisking neurons included\n    value: 7684\n    tolerance: 768\n  - quantity: mean whisking neuron count before\n    value: 961\n    tolerance: 96\n  - quantity: mean whisking neuron count after\n    value: 904\n    tolerance: 90\n  criterion: >-\n    A claim of absence, as silent-ablation-no-effect-touch, for whisking neurons. Reproduced\n    when p >= 0.05. The counts continue the quoted sentence on the next page (\"961 ± 464 to 904\n    ± 384\").\n- id: ablation-type-specificity\n  statement: Touch ablations changed Rtouch significantly more than whisking or silent ablations,\n    while whisking and silent ablations did not differ; for Rwhisking no pair of ablation types\n    differed.\n  source: Results, paragraph 10; Figure 2j, k\n  quote: Touch ablations produced significantly different changes in encoding scores among touch (but\n    not whisking) representations than either whisking or silent ablations, whereas whisking ablations\n    did not produce significantly different changes from silent ablations\n  statistics:\n  - about: change in Rtouch, touch against silent ablations\n    test: Wilcoxon rank-sum test\n    p: 0.002\n    n: 9 and 8 mice\n  - about: change in Rtouch, touch against whisking ablations\n    test: Wilcoxon rank-sum test\n    p: 0.042\n    n: 9 and 7 mice\n  - about: change in Rtouch, silent against whisking ablations\n    test: Wilcoxon rank-sum test\n    p: 0.152\n    n: 8 and 7 mice\n  - about: change in Rwhisking, touch against silent ablations\n    test: Wilcoxon rank-sum test\n    p: 0.743\n  - about: change in Rwhisking, touch against whisking ablations\n    test: Wilcoxon rank-sum test\n    p: 0.758\n  - about: change in Rwhisking, silent against whisking ablations\n    test: Wilcoxon rank-sum test\n    p: 1\n  depends_on:\n  - touch-ablation-reduces-touch\n  - whisking-ablation-no-effect-touch\n  - silent-ablation-no-effect-touch\n  criterion: >-\n    Per-mouse change in median score (common method), compared between ablation types by the\n    Wilcoxon rank-sum test (Fig. 2j legend; ablation_figure_score_change.m). Reproduced when for\n    Rtouch the touch-silent and touch-whisking tests give p < 0.05 and the whisking-silent test p\n    >= 0.05, and for Rwhisking all three give p >= 0.05. The pairings of the P values were read\n    from the figure.\n- id: response-similarity-example\n  statement: In an example touch ablation mouse, the change in Rtouch of touch neurons falls with\n    their response similarity to the ablated neurons, with a slope of -0.44.\n  source: Figure 3c-e\n  quote: Changes induced by ablation of touch neurons on the touch score as a function of response similarity\n    in an example mouse\n  depends_on:\n  - response-similarity-touch-ablation\n  expected:\n  - quantity: slope of change in Rtouch against response similarity, example mouse\n    value: -0.44\n    tolerance: 0.044\n  criterion: >-\n    The example mouse is 272761 (ablation_figure_correlation.m). Method as in\n    response-similarity-touch-ablation. The legend says the slope is \"for a linear fit of the\n    points\"; the code fits the 0.1-wide bin means. Both readings are run; reproduced when the\n    slope is within tolerance under one.\n- id: response-similarity-touch-ablation\n  statement: After touch ablation, the change in Rtouch depended on response similarity to the\n    ablated neurons; similar neurons declined and neurons with negative similarity increased,\n    while the whisking representation showed no such dependence.\n  source: Results, paragraph 12; Figure 3e, f\n  quote: Changes in Rtouch values after ablation depended on response similarity (Fig. 3e, f). Rtouch\n    values in neurons with high response similarity declined. Neurons with negative response similarity\n    showed increased Rtouch values ... Ablation of touch neurons had no effect on the whisking network\n  statistics:\n  - about: touch neurons, slope of change in Rtouch against response similarity\n    test: sign test\n    p: 0.039\n    n: 9 mice, 2,768 touch neurons\n  - about: whisking neurons, slope of change in Rwhisking\n    test: sign test\n    p: 0.508\n    n: 9 mice, 1,085 whisking neurons\n  depends_on:\n  - touch-ablation-reduces-touch\n  expected:\n  - quantity: touch neurons in the analysis\n    value: 2768\n    tolerance: 277\n  - quantity: whisking neurons in the analysis\n    value: 1085\n    tolerance: 109\n  criterion: >-\n    Neurons of each representation with encoding score above 0.25 by the membership rule\n    (Methods; get_restricted_neurons.m with threshold 0.25), the 9 touch ablation mice. A\n    neuron's trial-averaged dF/F is its mean dF/F over correct proximal and correct distal pole\n    trials, the two vectors concatenated (Methods), from the pre-ablation data; the ablated\n    neuron mean is their average over ablated neurons; response similarity is the Pearson\n    correlation of the two. The code reads the per-session averages dffBased_HitLTrialAvg and\n    dffBased_HitRTrialAvg, 70 frames each, but writes both into the first 70 rows, so only the\n    right-trial average enters its correlation (ablation_figure_correlation.m); that is run as a\n    variant. Per mouse, the change in score averaged in 0.1-wide similarity bins from -1 to 1,\n    bins with more than 3 neurons (code); a line fitted to the bin means (code) or to the\n    neurons (also allowed by the Methods), and a sign test of the 9 slopes against 0 (Methods).\n    Reproduced when, under one reading, the touch slopes are negative with sign-test p < 0.05,\n    the bin means are above 0 for negative similarity, and the whisking slopes give p >= 0.05.\n- id: response-similarity-whisking-ablation\n  statement: Ablation of whisking neurons had no similarity-dependent effect on either\n    representation.\n  source: Results, paragraph 12; Figure 3g\n  quote: Ablation of whisker neurons had no effect on either representation (Fig. 3g)\n  statistics:\n  - about: touch neurons\n    test: sign test\n    p: 0.453\n    n: 7 mice, 1,692 touch neurons\n  - about: whisking neurons\n    test: sign test\n    p: 1\n    n: 7 mice, 935 whisking neurons\n  expected:\n  - quantity: touch neurons in the analysis\n    value: 1692\n    tolerance: 169\n  - quantity: whisking neurons in the analysis\n    value: 935\n    tolerance: 94\n  criterion: >-\n    A claim of absence. As response-similarity-touch-ablation, for the 7 whisking ablation mice,\n    with the sign test at the 0.05 level. Reproduced when both sign tests give p >= 0.05 under\n    the reading adopted for response-similarity-touch-ablation.\n- id: ablation-no-off-target-event-rate\n  statement: Ablation of silent neurons did not change the calcium event rate of neurons adjacent\n    (10-25 um) to the ablated cells (0.014 Hz before and after).\n  source: Methods, Multiphoton ablation, paragraph 5; Extended Data Fig. 3a\n  quote: Event rates among neurons adjacent to ablated silent cells did not change (event rate before\n    ablation: 0.014 ± 0.008 Hz, grand median ± adjusted MAD; after ablation: 0.014 ± 0.007 Hz; P = 0.055\n    before versus after ablation, Wilcoxon signed-rank test, paired medians across n = 8 mice; 1,028\n    neurons across all mice)\n  statistics:\n  - test: Wilcoxon signed-rank test, paired medians across mice\n    p: 0.055\n    n: 8 mice, 1,028 neurons\n  expected:\n  - quantity: grand median event rate of adjacent neurons, before\n    value: 0.014\n    tolerance: 0.0014\n    unit: Hz\n  - quantity: grand median event rate of adjacent neurons, after\n    value: 0.014\n    tolerance: 0.0014\n    unit: Hz\n  - quantity: adjacent neurons, all mice\n    value: 1028\n    tolerance: 103\n  criterion: >-\n    A claim of absence. Neurons more than 10 and less than 25 um from the closest ablated neuron,\n    ablated and cylinder-excluded neurons left out, all neurons regardless of representation;\n    per-mouse median event rate before and after; signed-rank test at the 0.05 level\n    (ablation_figure_distance.m, event_rate_plot). Reproduced when p >= 0.05.\n- id: ablation-success-rate\n  statement: About two thirds of ablation attempts succeeded; 293 cells were ablated successfully\n    in 22 sessions in 14 mice with complete logs.\n  source: Methods, Multiphoton ablation, paragraph 3; Extended Data Fig. 2c-e\n  quote: In all cases, approximately 2/3 of ablations were successful\n  expected:\n  - quantity: fraction of targeted neurons ablated successfully\n    value: 0.667\n    tolerance: 0.067\n  - quantity: successfully ablated cells with complete logs\n    value: 293\n    tolerance: 29\n  criterion: >-\n    Per targeted neuron, success is membership in the curation file's successful list, and\n    attempts are the logged ablation attempts (ablation_figure_energy.m); the fraction is\n    successes over targeted neurons, all 24 ablations. The legend excludes j250220, j257218 and 7\n    other ablations for incomplete logs from the count of 293; the 7 are not named, so the count\n    is compared after leaving out the two named mice. Reproduced when the fraction is within\n    tolerance, and the count is reported.\n- id: glial-reaction-local\n  statement: Glial reactions after ablation were confined to the lesioned neuron, IBA1 reactions\n    having radii of 11.7 ± 1.7 um (8 of 10 IBA1-labelled sites; no GFAP reaction in 6).\n  source: Methods, Multiphoton ablation, paragraph 5; Extended Data Fig. 3b-d\n  quote: These reactions had radii of 11.7 ± 1.7 μm (mean ± s.d.; n = 8 sites)\n  expected:\n  - quantity: mean IBA1 reaction radius\n    value: 11.7\n    tolerance: 1.2\n    unit: um\n  criterion: >-\n    Histology of two mice perfused 24 h after ablation (Methods). Radii by the edge detection of\n    the Methods on the IBA1 images. Reproduced when the mean radius is within tolerance and 8 of\n    10 IBA1 and 0 of 6 GFAP sites show a reaction.\n- id: per-mouse-table\n  statement: Extended Data Table 1 lists, for each of the 24 ablations, the mouse's neuron count,\n    the ablation type, the number ablated, the touch and whisking neuron counts and the change in\n    median Rtouch and Rwhisking.\n  source: Extended Data Table 1\n  inferred: The per-mouse numbers are only in Extended Data Table 1 (read from the PDF); no sentence\n    states them.\n  depends_on:\n  - neurons-per-mouse\n  - touch-ablation-reduces-touch\n  criterion: >-\n    For each row of the table, the cell count and ablated count from the per-neuron table and\n    curation files, the touch and whisking counts (readings as in representation-sizes; the\n    table says \"for the 0.1 encoding score criteria\"), and the change in mouse median Rtouch and\n    Rwhisking by the common method. Counts match when within 10%; a change matches when within\n    0.005 of the table's value, as the table rounds to 0.001 and most changes are near 0, where a\n    10% tolerance would be below the rounding. Reproduced when at least 20 of the 24 rows match\n    in cell count, ablated count and both changes; partially reproduced for 12 to 19 rows.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peron-2020.yaml paper/10.1038-s41586-020-2062-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "[^ ]: " claims/peron-2020.yaml | grep -v "^[0-9]*:#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: "
```

```
298:    0.108 ± 0.051) and 865 ± 364 encoded whisking (fraction: 0.106 ± 0.028)
410:    6,975 neurons, P = 0.820; neuron count: from 775 ± 267 to 721 ± 241)
501:    distal 115-135 um. Per-mouse summary and the reported values are open: the legend says
580:    neurons in the barrel column of the spared whisker, n = 7 mice; whisking score: 66th ± 37th
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/peron-2020.yaml'
lines=open(p).read().split('\n')
out=[];i=0
while i<len(lines):
    l=lines[i]
    m=re.match(r'^(  )(quote|statement): (?![>|])(.*)$',l)
    if m:
        j=i+1; body=[m.group(3)]
        while j<len(lines) and lines[j].startswith('    ') : body.append(lines[j].strip()); j+=1
        text=' '.join(body)
        if ': ' in text:
            out.append(f'  {m.group(2)}: >-')
            out += ['    '+b for b in body]
            i=j; print('fixed', text[:50]); continue
    out.append(l); i+=1
open(p,'w').write('\n'.join(out))
EOF
python tools/claims_check.py claims/peron-2020.yaml paper/10.1038-s41586-020-2062-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/peron-2020.yaml
```

```
98:    subnetwork connectivity. Amplification—defined as the ratio of network output to network
99:    input—therefore increased with subnetwork connectivity
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/peron-2020.yaml",
 "old_string": "    subnetwork connectivity. Amplification—defined as the ratio of network output to network\n    input—therefore increased with subnetwork connectivity",
 "new_string": "    subnetwork connectivity. Amplification ... therefore increased with subnetwork connectivity"
}
```

```
The file claims/peron-2020.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peron-2020.yaml paper/10.1038-s41586-020-2062-x.txt | tail -1; python -c "
import yaml;d=yaml.safe_load(open('claims/peron-2020.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum(x.get('data')=='elsewhere' for x in c))"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/peron-2020.yaml`. All 30 quotes pass `tools/claims_check.py`. The checker still reports 7 problems, all "value not found": these are P values printed only inside figure images that the text extraction drops, P = 0.098 in Extended Data Fig. 5 and the six behaviour P values in Extended Data Fig. 6 (0.863, 0.666, 0.065, 0.721, 0.710, 0.620). I confirmed each one on the rendered PDF pages.

**Text read.** The version of record: main text, figure legends, Methods, Extended Data Figs. 1–8 legends, Extended Data Table 1 and the reporting summary. The only supplementary information named online is the reporting summary, so no supplement is missing. I opened the PDF pages for the P values inside Figs. 2j–k, 3b, 3f–g and Extended Data Figs. 5–6, and for the rows of Extended Data Table 1. To render them I installed PyMuPDF into the temp directory.

**Code read.**
- **Analysis code** (github.com/peronlab/ablation, commit 74b7321, MATLAB). It supplied the mouse lists for each ablation type, the folder pairing for mice with two ablations in sequence, the session-file feature names, the shuffle rule, the bins and fits, and the example mouse 272761.
- **Simulation code** (github.com/jwittenbach/ablation-sim, commit a8b5583, from 2016). Its parameters (5,000 neurons, ablating 30) are not the published model's, so the model claims follow the Methods.

**Counts.** 31 claims: 30 with quotes, and 1 marked `inferred` (the per-mouse rows of Extended Data Table 1). 19 claims carry statistics, 33 test entries in all. All 31 have criteria. 7 claims are simulation findings, marked `data: elsewhere` because the model outputs were not deposited and must be regenerated. 9 are claims of absence, each judged at the 0.05 level the paper uses. Tolerances are 10% throughout: the paper's ± values are spread across mice, not uncertainty of the statistic. The file states this reason, plus two exceptions (a value of 0.000, and table changes near zero).

**Details the paper leaves open, and the readings named for each:**
- **Neuron counts in the Results (901 touch, 865 whisking, 932→716, etc.):**
  - (a) the code's rule: score above 0.1 only, keeping ablated neurons and neurons in both representations;
  - (b) the full membership rule in the Methods.
  - Extended Data Table 1 gives means of about 780 and 624, so the table and the text appear to follow different rules.
- **Exclusion cylinder around ablated neurons:** the Methods say 10 µm radius and 60 µm height; the code uses a signed depth difference under 30 µm, which also drops every shallower neuron within 10 µm laterally. The Methods version is the main reading; the code's is a variant.
- **Fig. 2m and Extended Data Fig. 5:** the code uses per-mouse means and pools neurons for the reported values; the legend says medians across mice. Both readings are named.
- **Fig. 3:**
  - Slopes could be fitted to the 0.1-wide bin means (code) or to the individual neurons.
  - The code's trial-average loader overwrites the left-trial average with the right-trial one, so only right trials enter; this is a variant against the Methods' concatenation of both.
- **Whisking-ablation percentile:** the Methods reading ranks ablated neurons among whisking neurons; the code ranks them among touch neurons' touch scores.
- **Extended Data Fig. 6:** the legend's signed-rank test against the code's rank-sum test, and KS tests on the raw samples against the code's tests on histograms.
- **Model:**
  - The input strength is fixed only by "most closely matching" the in vivo data. Readings: (a) match the 0.108 touch fraction, (b) minimise the KS distance to the in vivo Rtouch distribution.
  - The reset pulse strength (Extended Data Fig. 1).
  - The input strength for the slow, whisking-like input.
  - Whether the networks with 0 ablations enter the Extended Data Fig. 4 correlation.
- **Extended Data Fig. 2:** 7 ablations excluded for incomplete logs are not named.

**Missing from the paper.** Nothing a claim needed is missing. Two findings rest on data the paper describes but the dataset may not hold: the histology (glial reaction radii) and the simulation outputs.

I committed nothing. Other untracked files in the working tree (such as `.bashrc`, `.idea`, `scripts`) were not created by me and I left them alone.

## End of run

41 turns, 7 minutes, $2.84 at API prices, result: success.
