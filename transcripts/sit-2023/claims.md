# 000483 · claims · run 39951473995

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000483 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000483 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -150; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  tail -80 claims/001453/*.yaml; cat tools/claims_check.py | head -80
```

```
against 0.06, p = 0.059).
  source: Figure 2H
  quote: ZF tended to show an elevated proportion of motion-responsive neurons compared to DC (ZF =
    0.13, DC = 0.06
  statistics:
  - test: Student's t-test
    p: 0.059
    n: 5 ZF and 5 DC fish
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
    p < 0.05).
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
    p: 0.05
    p_relation: "<"
    n: 5 ZF and 5 DC fish
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
[... 140 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-023-37704-5.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-023-37704-5.txt",
 "offset": 1068,
 "limit": 640
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "import fitz;d=fitz.open('paper/10.1038-s41467-023-37704-5.pdf');print(d.page_count)"; grep -n -i "supplement" docs/pilot-notes.md docs/pipeline.md | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 255,320p docs/pilot-notes.md; sed -n 50,120p docs/pipeline.md; ls claims | head; grep -rl "supplement" claims/*/*.yaml | head -5; grep -rh -i "supplement.*not\|no supplement\|supplement.*missing" claims/ | head -10
```

```
not findings of the paper but the registry's own checks that the dandiset
is the data behind the paper's tables, source data, code or deposits (the
link claims of step 6). They now say `kind: link` and are counted apart:
the README table and the dashboard's totals are of the paper's findings
only, and the links have a line of their own. And a finding with no quote
gave no sign of whether the paper states it at all. Every finding now has
either a quote or an `inferred` note saying why the statement is the
author's reading, such as numbers that appear only in a supplementary
table. Abstract-only papers are quoted from the abstract where it states the
finding. Every claim must come from and pertain to its paper, so five
claims that the paper's open text does not state were dropped, with their
outcomes: four of 001754 taken from the dandiset's description, and one of
000691 read from the paper's code (its method is now written out in the
claim that referred to it).

The full texts of the nine remaining papers were obtained on 2026-10-20 as
PDFs (the six abstract-only papers with their supplements where they have
one, the Cell paper of 000350, and version 1 of the two preprints), and
their claims were quoted from them; the manuscript quotes of 000067 were
also checked against the publisher's PDF. Of the 1,280 claims, 24 are
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 -A12 "37704" papers/manifest.yaml; grep -n -A8 "000483" papers/triage.yaml | head -30
```

```
717-    pdf: false
718-    supplements: 1
719-  000483:
720:  - doi: 10.1038/s41467-023-37704-5
721-    status: stored
722-    version: version of record
723-    source: PDF supplied by a person
724-    pdf: true
725-    supplements: 0
726-  000489:
727-  - doi: 10.1016/j.bioelechem.2022.108319
728-    status: stored
729-    version: as served by ncbi_pmc
730-    source: ncbi_pmc+crossref (paper-text-fetcher)
731-    pdf: false
732-    supplements: 0
18:  "000483":
19-    not_papers:
20-      10.25349/d91g8q: The Dryad dataset of processed objects, not a paper.
21-    papers:
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/ucsb-goard-lab/Neurotar-HDExperiments.git && cd Neurotar-HDExperiments && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -200 | sort
```

```
Exit code 128
fatal: could not read Username for 'https://github.com': No such device or address
```

**Agent calls Bash**

```bash
cd $TMPDIR; gh repo list ucsb-goard-lab --limit 100 2>&1 | grep -i -E "neurotar|HD|heading" ; gh api repos/ucsb-goard-lab/Neurotar-HDExperiments 2>&1 | head -5
```

```
gh: To use GitHub CLI in a GitHub Actions workflow, set the GH_TOKEN environment variable. Example:
  env:
    GH_TOKEN: ${{ github.token }}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/ucsb-goard-lab/Neurotar-HDExperiments; curl -s "https://api.github.com/orgs/ucsb-goard-lab/repos?per_page=100" | grep '"full_name"' | grep -i -E "neuro|hd|head"
```

Result: the fetched text is not kept.

**Agent**

The linked URL lacks a hyphen; the repository is `Neurotar-HD-Experiments`.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/ucsb-goard-lab/Neurotar-HD-Experiments.git && cd Neurotar-HD-Experiments && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | sort | head -300; find . -type f -not -path './.git/*' | wc -l
```

```
c6344f5f1bbeb7a986eb4fe8bd479847cbf9232a 2023-03-14 11:26:37 -0700
./.DS_Store
./.gitignore
./README.md
./_Helpers/DataStructure.m
./_Helpers/Separator.m
./_MainAnalysisClasses/.DS_Store
./_MainAnalysisClasses/_AbstractClasses/Control.m
./_MainAnalysisClasses/_AbstractClasses/ControlledRotation.m
./_MainAnalysisClasses/_AbstractClasses/Cue.m
./_MainAnalysisClasses/_AbstractClasses/DualCue.m
./_MainAnalysisClasses/_AbstractClasses/FreelyMoving.m
./_MainAnalysisClasses/_AbstractClasses/SingleCue.m
./_MainAnalysisClasses/_Experiments/AxonExperiment.m
./_MainAnalysisClasses/_Experiments/FreeRoamDualExperiment.m
./_MainAnalysisClasses/_Experiments/FreeRoamSingleExperiment.m
./_MainAnalysisClasses/_Experiments/HeadRotationExperiment.m
./_MainAnalysisClasses/_Experiments/LightDarkExperiment.m
./_MainAnalysisClasses/_Experiments/RSCSomaDualExperiment.m
./_MainAnalysisClasses/_Experiments/RSCSomaSingleExperiment.m
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neurotar-HD-Experiments && wc -l README.md _Helpers/*.m _MainAnalysisClasses/*/*.m _ReviewerCode/*.m _examples/*.m screenCells.m && cat README.md
```

```
66 README.md
  105 _Helpers/DataStructure.m
   61 _Helpers/Separator.m
   18 _MainAnalysisClasses/_AbstractClasses/Control.m
  241 _MainAnalysisClasses/_AbstractClasses/ControlledRotation.m
  987 _MainAnalysisClasses/_AbstractClasses/Cue.m
   12 _MainAnalysisClasses/_AbstractClasses/DualCue.m
   90 _MainAnalysisClasses/_AbstractClasses/FreelyMoving.m
   11 _MainAnalysisClasses/_AbstractClasses/SingleCue.m
   16 _MainAnalysisClasses/_Experiments/AxonExperiment.m
   13 _MainAnalysisClasses/_Experiments/FreeRoamDualExperiment.m
   13 _MainAnalysisClasses/_Experiments/FreeRoamSingleExperiment.m
   24 _MainAnalysisClasses/_Experiments/HeadRotationExperiment.m
  153 _MainAnalysisClasses/_Experiments/LightDarkExperiment.m
   27 _MainAnalysisClasses/_Experiments/RSCSomaDualExperiment.m
   15 _MainAnalysisClasses/_Experiments/RSCSomaSingleExperiment.m
   16 _MainAnalysisClasses/_Experiments/RemappingExperiment.m
  214 _ReviewerCode/reviewer_reclassify_attempt.m
   27 _examples/example_usage.m
   35 screenCells.m
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neurotar-HD-Experiments && cat _MainAnalysisClasses/_AbstractClasses/ControlledRotation.m _MainAnalysisClasses/_AbstractClasses/Cue.m _MainAnalysisClasses/_AbstractClasses/DualCue.m _MainAnalysisClasses/_AbstractClasses/SingleCue.m
```

```
<persisted-output>
Output too large (49.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4e805956-31c3-46f8-97bd-64872434b368/tool-results/bbgec6oay.txt

Preview (first 2KB):
classdef ControlledRotation < Control
    properties
    end
    
    methods
        function obj = ControlledRotation()
            obj = obj@Control();
        end
        function is_hd = calculateHeadDirection(obj, iterations, condition_flag)
            % To determine which cells are heading selective
            
            if nargin < 2 || isempty(iterations)
                iterations = 100; % this is set low in case you accidentally call it, actually 1000 iterations for real data
            end
            
		if nargin < 3 || isempty(condition_flag)
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neurotar-HD-Experiments && cat _MainAnalysisClasses/_Experiments/RemappingExperiment.m _MainAnalysisClasses/_Experiments/HeadRotationExperiment.m _MainAnalysisClasses/_AbstractClasses/FreelyMoving.m
```

```
classdef RemappingExperiment < ControlledRotation & SingleCue
	properties
	end

	methods
		function obj = RemappingExperiment(varargin)
			obj@SingleCue(varargin{:});
			obj@ControlledRotation();
		end

		function getRecordingParameters(obj)
			obj.n_repeats = 1;
			obj.segment_length = 950;
		end
	end
end
classdef HeadRotationExperiment < ControlledRotation & SingleCue
	properties
	end
	methods
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neurotar-HD-Experiments && cat _MainAnalysisClasses/_Experiments/RSCSomaDualExperiment.m _MainAnalysisClasses/_Experiments/RSCSomaSingleExperiment.m _MainAnalysisClasses/_Experiments/LightDarkExperiment.m _MainAnalysisClasses/_Experiments/AxonExperiment.m _MainAnalysisClasses/_AbstractClasses/Control.m
```

```
classdef RSCSomaDualExperiment < LightDarkExperiment
	properties
	end

	methods
		function obj = RSCSomaDualExperiment(varargin);
			obj@LightDarkExperiment(varargin{:});
		end

		function getRecordingParameters(obj)
			% this is to (unfortunately) account for differences in older/newer recordings with slightly different parameters
			switch obj.recording_length
				case 1950
					obj.n_repeats = 1;
					obj.segment_length = 950;
				case 7550
					obj.segment_length = 1250;
					obj.n_repeats = 3;
                case 15050
                    obj.segment_length = 1250;
[... 210 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4e805956-31c3-46f8-97bd-64872434b368/tool-results/bbgec6oay.txt"
}
```

```
1	classdef ControlledRotation < Control
2	    properties
3	    end
4	    
5	    methods
6	        function obj = ControlledRotation()
7	            obj = obj@Control();
8	        end
9	        function is_hd = calculateHeadDirection(obj, iterations, condition_flag)
10	            % To determine which cells are heading selective
11	            
12	            if nargin < 2 || isempty(iterations)
13	                iterations = 100; % this is set low in case you accidentally call it, actually 1000 iterations for real data
14	            end
15	            
16			if nargin < 3 || isempty(condition_flag)
17				condition_flag = 'all';
18	        end
19	        
20		switch condition_flag
[... 1232 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Neurotar-HD-Experiments && cat _Helpers/Separator.m _examples/example_usage.m screenCells.m; sed -n 1,214p _ReviewerCode/reviewer_reclassify_attempt.m
```

```
classdef Separator < handle
% Given the segment length and number of repeats, this class separates the data into a bunch of datastructures for easier control
	properties
		data_structure
		segment_length
		recording_length
		n_repeats
		n_trials
	end

	methods
		function obj = Separator(data_structure, segment_length, n_repeats)
			obj.data_structure = data_structure;
			obj.segment_length = segment_length;
			obj.recording_length = size(obj.data_structure.get('raw_F'), 2); % raw_F is a pretty safe field to pull for the recording length
			obj.n_repeats = n_repeats;
			obj.n_trials = floor(obj.recording_length/(obj.segment_length * obj.n_repeats));
		end

		function data = run(obj)
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000483/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d['most_recent_published_version' if d.get('most_recent_published_version') else 'draft_version'] for k in ['x']},indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000483/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200
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
    "dataset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
    "dataset": {
      "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
      "type": "object",
      "additionalProperties": false,
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p schemas/claims.schema.json
```

```
}
    },
    "checks": {
      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "ready"
        ],
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
which pdftoppm mutool magick convert gs 2>/dev/null; python -c "import pypdf" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-023-37704-5.pdf",
 "pages": "7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/ucsb-goard-lab/HeadingDecoder.git && cd HeadingDecoder && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | sort && cat README* 2>/dev/null | head -40
```

```
ca9842e9602aba6c94853f2f9d20777060756ce6 2022-07-14 09:59:28 -0700
./.gitattributes
./README.md
./_classes/HeadingDecoder.m
./_classes/HeadingDecoderPreprocessor.m
./_classes/HeadingDecoderPreprocessor2.m
./_helpers/angdiff.m
./_helpers/calculateDecoderError.m
./_helpers/calculatePercentCorrect.m
./_helpers/cleanHeadingTrace.m
./_helpers/getConfusionMatrix.m
./decoding_mwe.m
./population_shift_new_testing.m
# Heading Decoder
This code is part of the analyses for this [paper](https://www.biorxiv.org/content/10.1101/2022.03.25.485865v1), and is used for decoding heading from neural activity.
Make sure you are using Experiment objects from [here](https://github.com/kevinksit/HeadingProject), which are required for this code.

This code was written by Kevin Sit.

## Installation
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HeadingDecoder && wc -l _classes/*.m _helpers/*.m *.m && cat _classes/HeadingDecoder.m _helpers/*.m decoding_mwe.m
```

```
219 _classes/HeadingDecoder.m
  255 _classes/HeadingDecoderPreprocessor.m
  270 _classes/HeadingDecoderPreprocessor2.m
   87 _helpers/angdiff.m
   20 _helpers/calculateDecoderError.m
    2 _helpers/calculatePercentCorrect.m
    4 _helpers/cleanHeadingTrace.m
   20 _helpers/getConfusionMatrix.m
   89 decoding_mwe.m
  168 population_shift_new_testing.m
 1134 total
classdef HeadingDecoder < handle
	properties
		tuning_wts
		time_series

		memory = 5 % Samples looking back for fitting a line
		window = 0 % Samples around a single point for heading distribution

		n_segments  % number of identified segments in the data
[... 433 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/HeadingDecoder && cat _classes/HeadingDecoderPreprocessor.m; diff _classes/HeadingDecoderPreprocessor.m _classes/HeadingDecoderPreprocessor2.m | head -60
```

```
classdef HeadingDecoderPreprocessor < handle
    properties
        expt
        is_bad_recording = false;
        
        n_interp_bins
        n_cells
        window
    end
    
    methods
        function obj = HeadingDecoderPreprocessor(expt)
            if ~isa(expt, 'Cue') || ~isa(expt, 'Control')
                error('Input needs to be an Experiment object')
            end
            obj.expt = expt; % this needs to be an "Experiment" object
            obj.n_interp_bins = 180;
            obj.window = 15;
            obj.n_cells = numel(obj.expt.is_head_direction);
        end
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/kevinksit/GeneralHelperCode.git && cd GeneralHelperCode && git log -1 --format='%H %ci' && find . -iname "*leaveOneOut*" -o -iname "rowrescale*" | head; f=$(find . -iname "leaveOneOutAligner*" | head -1); cat "$f"
```

```
Exit code 1
8ccc95c704613fb7cb774d83d0737a3a20bd4502 2022-03-28 17:57:10 -0700
./rowrescale.m
cat: '': No such file or directory
```

**Agent**

Code read: `ucsb-goard-lab/Neurotar-HD-Experiments` at c6344f5 (the paper's URL lacks a hyphen), plus the lab's unlinked `HeadingDecoder` (ca9842e). Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/000483/10.1038-s41467-023-37704-5.yaml",
 "content": "# Claims for Sit & Goard (2023), Nature Communications 14:1992, on dandiset 000483.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (publisher's PDF supplied by a person, extracted to text):\n# main text, figure legends, Methods and Statistical information. The Supplementary Information\n# (Figures S1 to S7 and Table S1) was not in the paper store and was not read. The main\n# findings and their statistics are all stated in the main text; the supplement holds the\n# detail of three of them (Figure S5, Figure S6 and Table S1), and the claims that rest on it\n# say so. The figures could not be opened (no PDF renderer), so no number below is read from a\n# figure.\n#\n# Code read: the repository the paper links, given there as\n# github.com/ucsb-goard-lab/Neurotar-HDExperiments; the repository is in fact\n# github.com/ucsb-goard-lab/Neurotar-HD-Experiments, commit c6344f5 (2023-03-14). It holds\n# MATLAB classes, not figure scripts: Cue.m (tuning curves, preferred direction, flip score,\n# Gaussian fits), ControlledRotation.m (trial segmentation and the heading-selection test),\n# FreelyMoving.m (the Rayleigh-vector test), LightDarkExperiment.m and its subclasses (light and\n# dark segmentation), Separator.m, and _ReviewerCode/reviewer_reclassify_attempt.m (a GMM\n# clustering run). No code for the V-tests, the coherent-remapping offsets, the flip-score\n# F-tests, the LDA, the decoding or the statistics is in it. The lab's HeadingDecoder\n# repository (github.com/ucsb-goard-lab/HeadingDecoder, commit ca9842e, 2022-07-14), whose\n# README says it is part of this paper's analyses, is not linked by the paper; it was read and\n# is used only as a named variant (\"other software\" in the protocol's order). The helper\n# leaveOneOutAligner it and the reviewer code call is not in kevinksit/GeneralHelperCode\n# (commit 8ccc95c) and was not found.\n#\n# Data the paper used (as reported). 26 mice (12 male, 14 female), 6 to 12 weeks old at\n# surgery. Somata: Emx1-Cre x ROSA-LNL-tTA x TITL-GCaMP6s or Slc17a7-IRES2-Cre x\n# TITL2-GC6s-ICL-TTA2 mice expressing GCaMP6s. Axons: AAV GCaMP7b in ADN or in AM/PM (the\n# Results say wild-type mice, the Methods say AAV-Syn-Flex-jGCaMP7b in Emx1-Cre mice). Two-photon\n# imaging of posterior dysgranular RSC at 10 Hz, head-fixed in an air-floated chamber (Neurotar\n# Mobile HomeCage) that reports chamber position, angle (heading) and speed.\n#   - Free chamber, single cue, mouse-driven: 4 recordings over 3 mice, 2665 neurons (Fig. 1D, E).\n#   - Motor-rotated chamber, single cue (3 to 7 rpm, 90 to 120 s rotations with 5 s rests,\n#     2 to 6 repeats): 16 recordings over 5 mice, 3179 neurons (Fig. 1G, H).\n#   - Head rotation (2 rpm, chamber fixed) against chamber rotation, same field: 5 recordings\n#     over 4 mice, with ROIs matched across the two (Fig. 2).\n#   - Remapping: chamber in four quadrants of cues, all replaced in darkness between two\n#     recordings (contexts A and B): 12 recordings over 4 mice (Fig. 3).\n#   - Dual symmetric cues (A-B-A-B), light-on and light-off repeats: ADN axons 17 recordings\n#     over 4 mice, AM/PM axons 7 recordings over 3 mice (Fig. 4); RSC somata 36 recordings over\n#     6 mice (Figs. 5, 6); rotation in both directions 4 recordings over 2 mice (Fig. S5);\n#     animal-controlled against motor-controlled arena 7 recordings over 3 mice (Fig. S6);\n#     standard rotation against visual-cue-only rotation (a false floor that does not turn),\n#     number of recordings not given (Fig. 5J, K).\n# Measured variables: fluorescence of somata or axon ROIs, dF/F, inferred spikes (OASIS, AR(1),\n# on dF/F), chamber heading, position and speed, light condition.\n# The dandiset's description says it holds all the accompanying data of the paper. The paper\n# also deposited processed data on Dryad (doi:10.25349/D91G8Q) and Source Data with the\n# article; no claim needs them, but the author may use them to check the link.\n#\n# Methods shared by the claims, with their sources. \"Methods\" is the paper's Methods section;\n# \"code\" is Neurotar-HD-Experiments at c6344f5.\n#   - Activity: inferred spikes from OASIS with an AR(1) kernel on dF/F (Methods, Analysis of\n#     calcium data); dF/F = (F - F0)/F0 with F0 the mode of the neuropil-corrected fluorescence\n#     (Methods, eq. 2). If the dataset holds no inferred spikes, the deconvolution's other\n#     parameters are open; the call left commented in Cue.m is deconvolveCa(dff, 'ar1',\n#     'foopsi', 'optimize_pars'), which is the reading to use.\n#   - Tuning curve: heading in 60 bins of 6 degrees, mean activity per bin, then a 15 degree\n#     moving average (Methods; code Cue.binData, movmean over 15/6 bins); per trial, then\n#     averaged over trials (Methods).\n#   - Trials (rotation experiments): one full rotation of the chamber (Methods). Code\n#     (ControlledRotation.getTrialResponses): heading glitches (steps of 20 to 350 degrees)\n#     replaced by the previous value; breaks at wraps of heading and at rests (more than 20\n#     consecutive frames with a change under 0.5 degree); segments under 50 frames dropped, and\n#     segments whose 25th or 75th heading percentile lies more than 50 degrees from +-90 dropped.\n#   - Light and dark segments (dual-cue experiments; the code hard-codes them as there were no\n#     stimulus files): somata, 1950-frame recordings are one repeat of 950-frame segments,\n#     7550-frame recordings three repeats and 15050-frame recordings six repeats of 1250-frame\n#     segments; axons, three repeats of 1250 frames. Each repeat is a light segment then a dark\n#     segment (Separator.m; Methods, the first repeat is always light-on).\n#   - Heading selection, rotation experiments (Methods; code ControlledRotation\n#     .calculateHeadDirection): 1000 iterations; in each, the trials are split at random into two\n#     halves and the correlation of the two half-mean tuning curves is taken, for the real\n#     trials and for trials each circularly shifted by an independent random amount (same\n#     split); the two sets of 1000 correlations are compared by a two-sample KS test (p < 0.1)\n#     and Cohen's d (> 0.8, pooled SD); a Gaussian (one term for a single cue, two terms for\n#     dual cues) is fitted to the min-max rescaled trial-mean tuning curve and to the shuffled\n#     trial means, and the real r2 must exceed the 90th percentile of the shuffled r2. The code\n#     also requires the fitted amplitude a1 > 0 and fits with its bounds (single: a0 and a1 in\n#     [0, 1], b1 in pi/2 +- pi/6, c1 in [0, pi/2]; double: a0 in [0, 0.2], a1, a2 in [0, 1], b1 in\n#     pi/2 +- pi/24, b2 in 3pi/2 +- pi/24, c in [0, 2pi]; x from 0 to 2pi over the 60 bins);\n#     these are followed. For dual-cue recordings the code's default runs the test on all\n#     trials, light and dark together, and the reviewer code calls it so; that is followed.\n#   - Cross-validated alignment (Methods): for each trial, the peak bin of the mean of the other\n#     trials sets that trial's circular shift; for light/dark data the shifts come from light-on\n#     trials and are applied to light-off trials. The target position of the peak is not in the\n#     Methods; the code's Gaussian bounds (b1 near pi/2) and its shift point of bin 15 imply the\n#     peak is put at bin 15 (90 degrees on a 0 to 360 axis), which is followed.\n#   - Flip score (Methods, eq. 5; code Cue.calculateFlipScore): circular autocorrelation of the\n#     tuning curve (smoothed with MATLAB smoothdata defaults), CC at 180 degrees minus the mean\n#     of CC at 90 and 270 degrees.\n#   - V-test: circ_vtest of the Circular Statistics Toolbox against 0 degrees (Methods,\n#     Statistical information). The subscript of V in the paper (V32, V66) is read as n:\n#     with u = V sqrt(2/n), V32 = 14.1 gives p = 2.1e-4 and V66 = 25.6 gives p = 4.2e-6, near the\n#     printed 2.5e-4 and 4.9e-6.\n#   - Decoding (Methods, Decoding RSC somatic activity): trials are the full rotations before\n#     and after each rest that separates light-on from light-off (and light-off from light-on);\n#     each trial resampled to 200 bins; trials aligned across recordings into pseudopopulations;\n#     Bayesian decoding (Etter et al. 2020) of \"the raw calcium data\", trained on even and tested\n#     on odd timepoints; 1000 bootstrap iterations, each sampling with replacement 332 neurons\n#     (the smallest class) from the class decoded, or from all three classes in their rough\n#     proportions for \"all tuned cells\"; decoder error |decoded - actual| per frame; decoder\n#     accuracy per trial the fraction of frames with error under 18 degrees; mean and 2.5 and\n#     97.5 percentiles over iterations; p of a light-on against light-off comparison is one minus\n#     the fraction of iterations in which a t-test passes at alpha 0.05 (Statistical\n#     information; decoding error across recordings is compared by paired t-tests). Open, with\n#     readings: the decoder input, (a) dF/F (\"raw calcium data\", Methods) or (b) inferred spikes\n#     (HeadingDecoder); the decoder, (a) the naive Bayes decoder of Etter et al. 2020 on\n#     binarized activity, with 60 heading states of 6 degrees, or (b) HeadingDecoder's (activity\n#     times row-rescaled leave-one-trial-out tuning curves, normalized, filtered over 10 samples,\n#     maximum taken; 180 resample bins; up to 15 trials each side of the transition); the\n#     t-test, (a) paired over trials or (b) unpaired; chance, (a) 0.18 (Methods) or (b) 0.10\n#     (Figure 6A legend, which equals 36/360 and HeadingDecoder's 18/180). The Methods come first;\n#     every reading is run.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000483\"\npaper: doi:10.1038/s41467-023-37704-5\nclaims:\n- id: fig1-free-heading-fraction\n  statement: In head-fixed mice moving a free floating chamber with a single cue, 14.0% of RSC\n    neurons (373 of 2665) are heading selective, with no head movement.\n  source: Results, Neurons in the RSC represent heading in the absence of physical head\n    movements, paragraph 2; Figure 1D, E\n  quote: revealing that a proportion of neurons in RSC faithfully represent heading (14.0%,\n    373/2665 neurons\n  expected:\n  - quantity: percentage of heading-selective neurons, free chamber\n    value: 14.0\n    tolerance: 1.4\n    unit: percent\n  criterion: The 4 free-chamber recordings over 3 mice. Method from the Methods (Analysis of\n    calcium data, paragraph 2) and code FreelyMoving.m. The Rayleigh vector length of each\n    neuron's tuning curve (inferred spikes, 6 degree bins, 15 degree smoothing) is compared with\n    1000 values from the spike data circularly shifted in time by a random amount; a neuron is\n    selective when its RVL meets or exceeds the 99th percentile (Methods). The code keeps only\n    frames with chamber speed above 2 (FreelyMoving.checkIsMoving), which the Methods do not\n    mention; and its default threshold is the 95th percentile. Readings, run in turn, (a) all\n    frames, 99th percentile; (b) moving frames only, 99th percentile; (c) the code's 95th\n    percentile on moving frames, as a variant. Reproduced when (a) or (b) gives a percentage\n    within tolerance; (c) is reported.\n- id: fig1g-rotation-heading-fraction\n  statement: With the chamber rotated by a motor (single cue), 14.2% of RSC neurons (452 of\n    3179, 16 recordings over 5 mice) are heading selective by the paper's reliability and\n    Gaussian-fit test, a percentage similar to the free-chamber experiments.\n  source: Results, Neurons in the RSC represent heading in the absence of physical head\n    movements, paragraph 3; Figure 1G\n  quote: we found a similar percentage heading neurons as in the experiments without controlled\n    rotation, comprising 14.2% (452/3179 neurons) of the total number of cells recorded (n = 16\n    recordings over 5 mice\n  expected:\n  - quantity: percentage of heading-selective neurons, controlled rotation\n    value: 14.2\n    tolerance: 1.42\n    unit: percent\n  - quantity: heading-selective neurons, controlled rotation\n    value: 452\n    tolerance: 45\n  criterion: The heading-selection test of the opening comment (Methods; code\n    ControlledRotation.calculateHeadDirection) with a single-term Gaussian, on inferred spikes\n    of every neuron of the 16 single-cue controlled-rotation recordings. Reproduced when the\n    percentage is within tolerance. The test uses random splits and shuffles; the random seed\n    is a standard choice that should not change the count beyond a few cells.\n- id: selection-shuffled-control\n  statement: Run on pre-shuffled data, the heading-selection test passes no cells, so the count\n    of heading-selective cells is not due to chance.\n  source: Methods, Analysis of calcium data, paragraph 4\n  quote: When repeating these procedures using pre-shuffled data, no cells passed these\n    criteria, suggesting that the number of heading selective cells is accurate, and not due to\n    chance\n  depends_on:\n  - fig1g-rotation-heading-fraction\n  criterion: The test of fig1g-rotation-heading-fraction, run after circularly shifting each\n    trial's tuning curve by an independent random amount before the test, as in the commented\n    calculateHeadDirection_shuff of Cue.m (code). The Methods do not say on which recordings;\n    the single-cue controlled-rotation recordings are used, as the claim follows that test.\n    Reproduced when no cell passes; partially reproduced when some pass but no more than 1% of\n    cells (the combined significance of p = 0.01 the Methods give for the thresholds); not\n    reproduced above 1%.\n- id: fig1h-preferred-headings-tile\n  statement: The preferred headings of heading-selective cells tile the whole circumference of\n    the chamber, including headings with the cue outside the visual field, with a moderate\n    overrepresentation near 0 degrees, where the cue is centered in front of the mouse.\n  source: Results, Neurons in the RSC represent heading in the absence of physical head\n    movements, paragraph 3; Figure 1H\n  quote: showing that heading-responsive cells tile the entire circumference of the chamber, even\n    when the cue card is outside of the visual field of the mouse; though we note there is a\n    moderate overrepresentation of responses when the cue is centered in front of the mouse\n    near 0°\n  depends_on:\n  - fig1g-rotation-heading-fraction\n  criterion: The cells selected in fig1g-rotation-heading-fraction; the preferred heading of\n    each is the peak bin of its trial-mean tuning curve, cross-validated as in the Methods\n    (sorted by \"cross-validated angle of peak response\", Figure 1H legend). Heading 0 is the cue\n    centered in front of the mouse (Results); how the dataset's heading maps to the cue is the\n    author's to find. The paper gives no measure of tiling or of overrepresentation, so both\n    are open, with these readings, (a) every one of the 60 bins of 6 degrees holds at least one\n    preferred heading; (b) every 90 degree quadrant, including the one centered on 180 degrees,\n    holds at least 10% of the preferred headings. For the overrepresentation, the share of\n    preferred headings within 45 degrees of 0 exceeds 25% (its share under uniformity).\n    Reproduced when the overrepresentation holds and tiling holds under (a) or (b).\n- id: fig2f-head-chamber-same-preference\n  statement: Matched ROIs have on average the same preferred heading relative to the wall\n    pattern whether the head is rotated in a fixed chamber or the chamber is rotated around a\n    fixed head (V-test against 0 degrees, V = 14.1, p = 2.5e-4), though not all cells keep their\n    preference.\n  source: Results, Heading cells exhibit similar preferred directions during rotation of the\n    animal or the environment; Figure 2E, F\n  quote: matched ROIs on average have the same heading preference with respect to wall pattern\n    across conditions ... (V32 = 14.1, p = 2.5 × 10−4, V-test for nonuniformity against 0°\n  statistics:\n  - test: V-test for nonuniformity against 0 degrees\n    statistic: V32 = 14.1\n    p: 2.5e-4\n    n: 32 (the subscript of V, read as the number of matched cells), 5 recordings over 4 mice\n  expected:\n  - quantity: V statistic\n    value: 14.1\n    tolerance: 1.41\n  criterion: The 5 head-rotation recordings, each paired with its chamber-rotation recording of\n    the same field; ROIs matched across the two (a single set of ROIs after derotation,\n    manually checked, Results). Per ROI the difference in preferred heading, head rotation minus\n    chamber rotation, wrapped to +-180; circ_vtest against 0. Open, with readings, the cells,\n    (a) matched ROIs heading-selective in both conditions, (b) in either condition, (c) in the\n    chamber-rotation condition; the preferred heading, (i) the peak of the trial-mean tuning\n    curve (Figure 2F legend, \"peak heading preference\"), (ii) the code's 'fit' method\n    (Cue.calculatePreferredDirection, recommended in the code's README). Reproduced when a\n    reading gives p < 0.05 with V > 0; the V and n of each reading are reported, and the one\n    whose n is 32 is named.\n- id: fig3c-coherent-remapping\n  statement: When all the wall cues are replaced, heading cells remap coherently, each shifting\n    its preferred heading by about the same angle as the rest of the population in its\n    recording (V-test of the Delta phase offsets against 0 degrees, V = 25.6, p = 4.9e-6).\n  source: Results, Changing visual cues elicits coherent remapping in RSC neurons; Figure 3C\n  quote: changing contexts caused the population of heading cells to coherently remap, as\n    indicated by low Δ phase offsets (V66 = 25.6, p = 4.9 × 10−6\n  statistics:\n  - test: V-test for nonuniformity against 0 degrees\n    statistic: V66 = 25.6\n    p: 4.9e-6\n    n: 66 (the subscript of V, read as the number of neurons), 12 recordings over 4 mice\n  expected:\n  - quantity: V statistic\n    value: 25.6\n    tolerance: 2.56\n  criterion: The 12 remapping recordings (single-cue class in the code, RemappingExperiment).\n    Per neuron n, Delta phase offset = (pref A(n) - pref B(n)) minus the expected offset of the\n    other neurons of its recording, wrapped to +-180; circ_vtest against 0 over all neurons of\n    all recordings (Methods, Calculation of coherent remapping). Open, with readings, the\n    expected offset, (i) the median over the other neurons of their differences pref A - pref B\n    (Methods text) or (ii) the median of their pref A minus the median of their pref B (the\n    Methods equation); the cells, (a) heading-selective in both contexts, (b) in either; the\n    preferred heading, the peak of the trial-mean tuning curve or the code's 'fit' method.\n    Reproduced when a reading gives p < 0.05 with V > 0; every reading's V and n are reported.\n- id: fig4-axons-light-on-shape\n  statement: In the light-on condition with two symmetric cues, ADN axons in RSC show unimodal\n    heading tuning curves, while visual cortical (AM/PM) axons show bimodal tuning curves with\n    peaks about 180 degrees apart.\n  source: Results, The ADN and visual cortex send distinct information to RSC, paragraph 2;\n    Figure 4D, E\n  quote: In the light-on condition, ADN axons show a unimodal tuning curve, whereas visual\n    cortical axons show a bimodal tuning curve\n  criterion: The 17 ADN and 7 AM/PM axon recordings (AxonExperiment, three light/dark repeats).\n    Light-on tuning curves, cross-validated alignment on light-on trials. The paper's measure of\n    bimodality is the flip score (Methods). The axons shown are open, with readings, (a) axons\n    passing the heading-selection test with a two-term Gaussian; (b) all axons. Reproduced when,\n    under a reading, the flip score of the mean aligned light-on curve is below 0 for ADN and\n    above 0 for visual axons, and the mean flip score of single visual axons exceeds that of\n    ADN axons (two-sample KS test, p < 0.05, the paper's test for two distributions).\n- id: fig4-axons-light-off\n  statement: In the light-off condition ADN axons keep their heading tuning for several trials,\n    while visual cortical axons lose their tuning.\n  source: Results, The ADN and visual cortex send distinct information to RSC, paragraph 2;\n    Figure 4D, E legends\n  quote: In the light-off condition, ADN axons maintain their response for several trials,\n    whereas visual cortical axons lose their tuning\n  depends_on:\n  - fig4-axons-light-on-shape\n  criterion: Same recordings, axons and readings as fig4-axons-light-on-shape; light-off trials\n    aligned with the light-on shifts (Methods). The paper gives no test; the measure is the\n    paper's heading-selection test run on light-off trials only (the code's 'dark' option of\n    calculateHeadDirection), with a two-term Gaussian. Reproduced when the fraction of axons\n    selective in light-off is higher for ADN than for visual axons (two-sample comparison of\n    per-recording fractions; Fisher's exact test on the pooled counts as a variant), and the\n    mean aligned light-off curve of ADN axons peaks within 18 degrees (the decoder's accuracy\n    window) of the light-on peak bin while that of visual axons has a peak-to-trough range\n    under half of its light-on range. \"For several trials\" is not tested further.\n- id: figs5-rotation-direction\n  statement: RSC tuning persists regardless of the direction of chamber rotation (bootstrapped\n    KS test, p = 0.0094, 4 recordings over 2 mice).\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 1; Figure S5\n  quote: These responses persisted regardless of rotation direction (Figure S5, p = 0.0094,\n    bootstrapped KS-test, n = 4 recordings over 2 mice)\n  statistics:\n  - test: bootstrapped KS-test\n    p: 0.0094\n    n: 4 recordings over 2 mice\n  criterion: Figure S5, where the test is shown, was not read (supplement missing). The Methods\n    give the test (p is one minus the fraction of bootstrap iterations in which a two-sample KS\n    test passes at alpha 0.05) but not what is compared. Readings the text allows, (a) the\n    distribution of differences in preferred heading between clockwise and counterclockwise\n    rotation for heading-selective cells against the same differences with cells paired at\n    random (as the shuffles of Figures 2F and 3C); (b) the correlations of each cell's\n    clockwise and counterclockwise tuning curves against those of randomly paired cells.\n    Reproduced when a reading gives p < 0.05 with the real pairs closer than the random ones.\n    The number of bootstrap iterations is not given for this test; 1000, as for the decoding,\n    is the reading.\n- id: figs6-arena-control\n  statement: RSC tuning persists whether or not the mouse is in control of the arena\n    (bootstrapped KS test, p = 0.031, 7 recordings over 3 mice).\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 1; Figure S6\n  quote: or whether or not the animal was in control of the arena (Figure S6, 0.031,\n    bootstrapped KS-test, n = 7 recordings over 3 mice)\n  statistics:\n  - test: bootstrapped KS-test\n    p: 0.031\n    n: 7 recordings over 3 mice\n  criterion: As for figs5-rotation-direction, with animal-controlled against motor-controlled\n    rotation in place of the two directions. Figure S6 was not read (supplement missing), so\n    what is compared is open, with the readings (a) and (b) of figs5-rotation-direction.\n    Reproduced when a reading gives p < 0.05 with the real pairs closer than the random ones.\n- id: fig5-three-classes\n  statement: Clustering the Gaussian-fit coefficients of RSC somatic tuning curves in light-on\n    and light-off conditions gives an optimum of three functional classes (heading, landmark and\n    alignment cells), though the responses span a continuum.\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 1; Figure 5B; Methods, Clustering of RSC soma responses\n  quote: We found that the data were optimally clustered into three functional classes ...\n    although we note that the responses span a continuum\n  criterion: The 36 dual-cue RSC soma recordings over 6 mice; heading-selective cells only (two-\n    term Gaussian test of the opening comment), as the reviewer code clusters is_head_direction\n    cells and the Results speak of tuned cells. For each cell, the light-on and light-off\n    tuning curves are aligned (cross-validated, light-on shifts), rescaled together to [0, 1]\n    (code rowrescale on the concatenation) and each fitted with the two-term Gaussian (Methods,\n    eq. 4; code LightDarkExperiment.calculateTuningFits2); the features are a1, a2, c1, c2 of\n    both fits (8 values; Methods). Silhouette evaluation of Gaussian mixture models (Methods)\n    for k = 2, 3 and 4. Reproduced when the silhouette value at k = 3 exceeds those at k = 2\n    and k = 4 (a local maximum, Methods). The reviewer code's fit (calculateTuningFits, on\n    unaligned curves centered on their peak) is a variant and is reported.\n- id: fig5-class-proportions\n  statement: 12.1% of RSC neurons are tuned in the dual-cue experiment; of these, landmark cells\n    are the plurality (33%), followed by alignment cells (28%) and heading cells (22%).\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 3; Figure 5C to E\n  quote: Of the total number of tuned cells (12.1 ± 1.1%), landmark cells made up the plurality\n    of cells (33 ± 3.5%), followed by alignment cells (28 ± 1.9%, mean ± s.e.m.), and heading\n    (22 ± 2.3%) cells\n  depends_on:\n  - fig5-three-classes\n  expected:\n  - quantity: tuned cells, percentage of all RSC neurons\n    value: 12.1\n    tolerance: 1.1\n    unit: percent\n  - quantity: landmark cells, percentage of tuned cells\n    value: 33\n    tolerance: 3.5\n    unit: percent\n  - quantity: alignment cells, percentage of tuned cells\n    value: 28\n    tolerance: 1.9\n    unit: percent\n  - quantity: heading cells, percentage of tuned cells\n    value: 22\n    tolerance: 2.3\n    unit: percent\n  criterion: Tolerances are the paper's s.e.m. Classes from a 3-component GMM on the features of\n    fig5-three-classes (the reviewer code fits it with 20 replicates and up to 1000\n    iterations, followed). Then, per the Methods, cells whose minimum Mahalanobis distance to the\n    component centroids is \"significantly greater\" go to a null cluster; archetypal light-on and\n    light-off curves are built from each component's mean coefficients (eq. 4, with b1 and b2 at\n    the code's pi/2 and 3pi/2); each cell goes to the class whose archetypes have the smallest\n    summed cosine distance to its two curves. Classes are named by their archetypes as in the\n    Results (heading, unimodal in light and dark; landmark, bimodal in light and absent in dark;\n    alignment, bimodal in light and unimodal in dark). Open, with readings, the outlier rule,\n    (a) squared Mahalanobis distance beyond the 95th percentile of a chi-square with 8 degrees of\n    freedom, (b) no outlier step (the reviewer code); the averaging, (i) mean over recordings,\n    (ii) mean over mice, (iii) pooled cells. The F-test degrees of freedom of Figure 5F to H\n    imply 332 heading, 522 landmark and 409 alignment cells (2n - 2), and 332 is the smallest\n    class in the decoding Methods; those counts are reported for comparison. Reproduced when a\n    reading puts all four values within tolerance with landmark > alignment > heading;\n    partially reproduced when the order holds but a value falls outside.\n- id: fig5e-alignment-peaks-coregistered\n  statement: In alignment cells the single light-off peak is always at the location of one of\n    the two light-on peaks, so landmark and heading responses are coregistered.\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 2; Figure 5E\n  quote: The light-off peak in these alignment cells was always at the same location as one of\n    the two peaks in the light-on condition\n  depends_on:\n  - fig5-class-proportions\n  criterion: The alignment cells of fig5-class-proportions; aligned light-on and light-off\n    tuning curves (light-on shifts applied to both, Methods). The paper gives no test; the\n    paper's test for angles clustered at a value is the V-test (Methods), which is used. Per\n    cell, the offset of the light-off peak bin from the nearer of the two light-on peaks (the\n    peak bin and the peak bin of the other half circle), wrapped to +-180; circ_vtest against 0.\n    Reproduced when p < 0.05 with V > 0; the share of cells with an offset within 18 degrees is\n    reported.\n- id: fig5f-heading-flip-unchanged\n  statement: Heading cells show no significant difference in flip score between light-on and\n    light-off conditions.\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 3; Figure 5F\n  quote: Heading cells showed no significant difference in flip score across conditions (F1,662 =\n    0.18, p = 0.67\n  statistics:\n  - test: F-test (mixed-effects model)\n    statistic: F(1,662) = 0.18\n    p: 0.67\n    n: heading cells (332, from the degrees of freedom)\n  depends_on:\n  - fig5-class-proportions\n  criterion: A claim of absence. Flip score (Methods, eq. 5; code Cue.calculateFlipScore) of each\n    heading cell's light-on and light-off tuning curve. The paper's test is an F-test on the\n    light condition in a (generalized) linear mixed-effects model with mouse as random effect\n    (Methods, Statistical information, mixed models control for cells within the same animal;\n    the residual df 2n - 2 fit one fixed effect and an intercept), run as fitlme-style flip ~\n    light + (1|mouse). Reproduced when p >= 0.05; not reproduced when p < 0.05. The difference\n    in mean flip score is reported either way, and a model with a random intercept per cell as\n    well is shown as a variant.\n- id: fig5gh-landmark-alignment-flip-drop\n  statement: Landmark and alignment cells have significantly lower flip scores in light-off\n    than in light-on (landmark F(1,1042) = 1062.5, p = 3.1e-161; alignment F(1,816) = 209.5,\n    p = 2.0e-42).\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 3; Figure 5G, H\n  quote: both landmark (F1,1042 = 1062.5, p = 3.1 × 10−161) and alignment (F1,816 = 209.5, p =\n    2.0 × 10−42) cells have significantly lower flip scores in the light-off than the light-on\n    condition\n  statistics:\n  - about: landmark cells, light-off against light-on flip score\n    test: F-test (mixed-effects model)\n    statistic: F(1,1042) = 1062.5\n    p: 3.1e-161\n    n: landmark cells (522, from the degrees of freedom)\n  - about: alignment cells, light-off against light-on flip score\n    test: F-test (mixed-effects model)\n    statistic: F(1,816) = 209.5\n    p: 2.0e-42\n    n: alignment cells (409, from the degrees of freedom)\n  depends_on:\n  - fig5-class-proportions\n  criterion: As fig5f-heading-flip-unchanged, for landmark and for alignment cells. Reproduced\n    when both classes have p < 0.05 with the light-off flip score lower; partially reproduced\n    when one does.\n- id: fig5i-axons-in-clusters\n  statement: Projected into the soma clusters' discriminant space, ADN axons fall mostly within\n    the heading cluster and visual axons mostly within the landmark cluster, with some overlap\n    with the alignment cluster.\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 4; Figure 5I\n  quote: finding that ADN axons and visual axons are mostly restricted to the boundaries of the\n    heading and landmark clusters, respectively (Fig. 5I), although there is some overlap with\n    the alignment cluster boundary\n  depends_on:\n  - fig5-class-proportions\n  - fig4-axons-light-on-shape\n  criterion: An LDA model trained on the soma features and their GMM classes (Methods,\n    Clustering of RSC soma responses) projects the axon features (same Gaussian fits, Methods,\n    Clustering of axonal responses) onto its first two discriminants; each soma class has a 95%\n    ellipse (Methods; read as the 95% region of a bivariate normal fitted to the class's\n    points). Axons as in fig4-axons-light-on-shape, readings (a) and (b). \"Mostly\" is read as\n    more than half. Reproduced when, under a reading, more than half of ADN axons lie inside the\n    heading ellipse and more than half of visual axons inside the landmark ellipse; partially\n    reproduced when only one holds. The shares inside the alignment ellipse are reported.\n- id: fig5k-visual-cue-only\n  statement: When only the visual cues rotate (no proprioceptive or somatosensory input), the\n    visual contributions to tuning are retained, but heading-cell responses are strongly\n    degraded.\n  source: Results, A functional class of RSC neurons coregisters visual and heading signals,\n    paragraph 4; Figure 5J, K\n  quote: We found that the visual contributions to tuning were retained in visual cue only\n    rotation, but the loss of proprioceptive and somatosensory information strongly degraded\n    the heading cell responses\n  depends_on:\n  - fig5-class-proportions\n  criterion: Neurons matched between a standard-rotation and a visual-cue-only recording (Figure\n    5K legend), classed in the standard recording. The paper gives neither the number of\n    recordings nor a measure or test. Readings, (a) the fraction of cells of each class that\n    pass the heading-selection test in the visual-only recording; (b) the peak-to-trough range of\n    the class's mean aligned light-on tuning curve (light-on shifts from the standard recording)\n    in visual-only relative to standard rotation. Reproduced when, under a reading, landmark\n    cells keep a bimodal light-on curve in visual-only rotation (flip score of the class mean\n    above 0) and heading cells lose more than landmark cells (lower fraction or lower relative\n    range). Blocked if the dataset holds no visual-cue-only recordings.\n- id: fig6a-population-light-on\n  statement: Decoding heading from all tuned RSC cells within single 100 ms frames is accurate in\n    the light-on condition despite the symmetric cues (mean decoder accuracy 0.82, 95% CI 0.78\n    to 0.86).\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 1;\n    Figure 6A\n  quote: When sampling across all the classes, the heading network shows remarkable accuracy,\n    even in the presence of symmetric visual cues (mean decoder accuracy = 0.82, 95% CI = [0.78,\n    0.86]\n  statistics:\n  - test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.78\n      high: 0.86\n    n: 1000 bootstrap samples of 332 neurons\n  expected:\n  - quantity: mean decoder accuracy, all tuned cells, light-on\n    value: 0.82\n    tolerance: 0.04\n  depends_on:\n  - fig5-class-proportions\n  criterion: The decoding method of the opening comment, sampling from all three classes.\n    Tolerance is the half-width of the paper's 95% CI. Reproduced when a reading of the decoder\n    gives a mean within tolerance; every reading is reported.\n- id: fig6a-population-light-off\n  statement: In the light-off condition the decoder's accuracy from all tuned cells drops (mean\n    0.44, 95% CI 0.34 to 0.54; p = 7.6e-3 against light-on) but stays above chance.\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 1;\n    Figure 6A, bottom\n  quote: When transitioning from light-on to light-off, there is a drop in the performance of\n    the decoder, although the performance remains above chance ... (mean decoder accuracy =\n    0.44, 95% CI = [0.34, 0.54], p = 7.6 × 10−3\n  statistics:\n  - test: bootstrapped t-test\n    p: 7.6e-3\n    n: 1000 bootstrapped samples\n  - test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.34\n      high: 0.54\n  expected:\n  - quantity: mean decoder accuracy, all tuned cells, light-off\n    value: 0.44\n    tolerance: 0.1\n  depends_on:\n  - fig6a-population-light-on\n  criterion: As fig6a-population-light-on, light-off trials. Above chance means the 95% interval\n    excludes chance (Methods), under either chance reading (0.18 or 0.10). Reproduced when, under\n    a decoder reading, the mean is within tolerance, the interval excludes chance and the\n    bootstrapped t-test of light-on against light-off gives p < 0.05 with light-off lower.\n- id: fig6b-heading-cells\n  statement: Heading cells alone decode heading accurately in both light-on (0.61, 95% CI 0.56 to\n    0.66) and light-off (0.44, 95% CI 0.36 to 0.52) conditions, with no significant difference\n    between them (p = 0.11).\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 2;\n    Figure 6B, top\n  quote: We found that heading cells were able to accurately decode in both light-on (mean\n    decoder accuracy = 0.61, 95% CI = [0.56, 0.66]) and light-off conditions (mean decoder\n    accuracy = 0.44, 95% CI = [0.36, 0.52]), suggesting that they contribute to the heading\n    signal in both conditions (p = 0.11\n  statistics:\n  - test: bootstrapped t-test\n    p: 0.11\n    n: 1000 bootstrapped samples\n  - about: light-on accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.56\n      high: 0.66\n  - about: light-off accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.36\n      high: 0.52\n  expected:\n  - quantity: mean decoder accuracy, heading cells, light-on\n    value: 0.61\n    tolerance: 0.05\n  - quantity: mean decoder accuracy, heading cells, light-off\n    value: 0.44\n    tolerance: 0.08\n  depends_on:\n  - fig5-class-proportions\n  criterion: The decoding method of the opening comment on heading cells only. The values are\n    judged under each decoder reading; reproduced when a reading puts both within tolerance and\n    both intervals exclude chance. The absence of a light difference is judged on the paper's\n    bootstrapped t-test alone: not significant when p >= 0.05; the claim is not reproduced if p\n    < 0.05 under the reading that matches the values.\n- id: fig6b-landmark-cells\n  statement: Landmark cells decode heading very well in light-on (0.80, 95% CI 0.75 to 0.84) but\n    fall to chance in light-off (0.20, 95% CI 0.14 to 0.27; p = 8.0e-4).\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 2;\n    Figure 6B, middle\n  quote: landmark cells have very high decoder performance in the light-on condition (mean\n    decoder accuracy = 0.80, 95% CI = [0.75, 0.84]), with an overrepresentation of decoder\n    errors at 180°, which immediately plummets to chance levels in the light-off condition (mean\n    decoder accuracy = 0.20, 95% CI = [0.14, 0.27]; p = 8.0 × 10−4\n  statistics:\n  - test: bootstrapped t-test\n    p: 8.0e-4\n    n: 1000 bootstrapped samples\n  - about: light-on accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.75\n      high: 0.84\n  - about: light-off accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.14\n      high: 0.27\n  expected:\n  - quantity: mean decoder accuracy, landmark cells, light-on\n    value: 0.80\n    tolerance: 0.05\n  - quantity: mean decoder accuracy, landmark cells, light-off\n    value: 0.20\n    tolerance: 0.07\n  depends_on:\n  - fig5-class-proportions\n  criterion: The decoding method on landmark cells only; tolerances from the paper's intervals\n    (the larger half-width). Reproduced when, under a decoder reading, both means are within\n    tolerance, the light-on against light-off p < 0.05, and the light-off interval includes\n    chance. Under the 0.10 chance reading the paper's own light-off interval excludes chance;\n    the outcome under each chance reading is reported.\n- id: fig6b-alignment-cells\n  statement: Alignment cells decode between heading and landmark cells, better in light-on (0.71,\n    95% CI 0.66 to 0.76) and fairly accurately in light-off (0.51, 95% CI 0.43 to 0.59), with no\n    significant difference (p = 0.54).\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 2;\n    Figure 6B, bottom\n  quote: alignment cells show decoder performance that is between that of heading and landmark\n    cells, taking advantage of improved decoding from the visual cues in the light-on condition\n    (mean decoder accuracy = 0.71, 95% CI = [0.66, 0.76]), but retaining fairly accurate heading\n    in the light-off condition (mean decoder accuracy = 0.51, 95% CI = [0.43, 0.59], p = 0.54\n  statistics:\n  - test: bootstrapped t-test\n    p: 0.54\n    n: 1000 bootstrapped samples\n  - about: light-on accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.66\n      high: 0.76\n  - about: light-off accuracy\n    test: bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.43\n      high: 0.59\n  expected:\n  - quantity: mean decoder accuracy, alignment cells, light-on\n    value: 0.71\n    tolerance: 0.05\n  - quantity: mean decoder accuracy, alignment cells, light-off\n    value: 0.51\n    tolerance: 0.08\n  depends_on:\n  - fig5-class-proportions\n  criterion: The decoding method on alignment cells only. Reproduced when, under a decoder\n    reading, both means are within tolerance, the light-on mean lies between those of heading\n    and landmark cells, and the light-off interval excludes chance. The absence of a light\n    difference is judged on the bootstrapped t-test alone (p >= 0.05); the claim is not\n    reproduced if p < 0.05 under the reading that matches the values.\n- id: fig6b-180-errors\n  statement: Decoding from landmark cells in light-on gives an overrepresentation of 180 degree\n    errors from the symmetric cues, while heading cells show no preponderance of 180 degree\n    errors.\n  source: Results, Contributions of distinct classes to representation of heading, paragraphs 1\n    and 2; Figure 6B\n  quote: As expected based on their tuning curves, heading cells did not exhibit a preponderance\n    of 180° errors, suggesting they do not represent visual information directly\n  depends_on:\n  - fig6b-heading-cells\n  - fig6b-landmark-cells\n  criterion: Light-on decoder errors of the class decoders, under each decoder reading. The paper\n    gives no measure; the measure is the share of frames with an absolute error within 18 degrees\n    of 180 (the paper's accuracy window, moved to 180), against its share of 0.10 under uniform\n    errors. Reproduced when that share exceeds 0.10 for landmark cells and is no more than 0.10\n    for heading cells.\n- id: fig6-heading-below-population\n  statement: In light-on, heading cells alone decode worse than the whole tuned population, so\n    alone they may not give an optimal representation of instantaneous heading.\n  source: Results, Contributions of distinct classes to representation of heading, paragraph 2;\n    Figure 6B, right; Table S1\n  quote: Since their decoder performance is lower than the population in the light-on condition,\n    heading cells alone may be insufficient for ... providing an optimal representation of\n    instantaneous heading\n  depends_on:\n  - fig6a-population-light-on\n  - fig6b-heading-cells\n  criterion: Table S1, which holds the class comparisons (linear mixed-effects models, Figure 6\n    legend), was not read (supplement missing), so the model is open. Readings, (a) the 95%\n    bootstrap intervals of light-on accuracy for heading cells and for all tuned cells do not\n    overlap; (b) a linear mixed-effects model of per-trial light-on decoder error with class\n    (heading or total) as fixed effect and recording as random intercept gives p < 0.05 with\n    heading cells worse. Reproduced when a reading holds under a decoder reading.\n"
}
```

```
File created successfully at: claims/000483/10.1038-s41467-023-37704-5.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000483/10.1038-s41467-023-37704-5.yaml paper/10.1038-s41467-023-37704-5.txt; grep -n -i -E "—|rather" claims/000483/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000483/10.1038-s41467-023-37704-5.yaml; sed -i 's/bootstrapped t-test alone: not significant when/bootstrapped t-test alone, not significant when/' $f; grep -n -E "^[^#]*[^ ]: " $f | grep -v -E "^\s*[0-9]+:\s*-? ?[a-z_]+: " | head; python tools/claims_check.py $f paper/10.1038-s41467-023-37704-5.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000483/10.1038-s41467-023-37704-5.yaml; grep -c -i -E "—|rather" $f; python -c "
import yaml;d=yaml.safe_load(open('$f'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
0
24 24 11 24 10
```

**Agent**

I wrote `claims/000483/10.1038-s41467-023-37704-5.yaml` with 24 claims. The quote checker passes every quote. It flags one value it couldn't match: p = 8.0 × 10⁻⁴ in `fig6b-landmark-cells`. I read the text and the value is correct; the paper prints "8.0 × 10−4", a form the checker doesn't recognise.

**Text read:** the version of record (a PDF supplied by a person, extracted to text): main text, figure legends, Methods and statistics. The Supplementary Information (Figures S1–S7, Table S1) is not in the paper store. All the main findings and their statistics are stated in the main text, so I went ahead and wrote the claims. I could not open the figures because there is no PDF renderer, so no number was read from a figure.

**Code read:**
- **The paper's code** (`ucsb-goard-lab/Neurotar-HD-Experiments`, commit c6344f5): the paper's URL is missing a hyphen. The repo holds MATLAB classes for tuning curves, heading selection, light/dark segmentation, flip score, Gaussian fits and one reviewer-response clustering script. It has no code for the V-tests, the remapping offsets, the F-tests, the LDA, the decoding or the statistics.
- **The lab's `HeadingDecoder`** (commit ca9842e): the paper doesn't link it, but its README says it belongs to this paper. I used it only as a named variant.
- **`leaveOneOutAligner`:** the alignment helper the code calls was not found.

**Counts:** 24 claims, all 24 with quotes and criteria, 11 with statistics, 10 with expected values. No claim needs outside data; I named the Dryad deposit (doi:10.25349/D91G8Q) for the author.

**Details left open, with the readings named:**
- **Free-chamber selection (Fig. 1):** all frames or only frames with speed above 2 (the code); 99th percentile (Methods) or 95th (code's default, as a variant).
- **Fig. 1H tiling and the excess near 0°:** the paper gives no measure. Readings: every 6° bin has a cell, or every 90° quadrant holds at least 10% of cells; the excess is more than 25% of cells within ±45° of 0°.
- **Fig. 2F and 3C:** which cells count (selective in both conditions, in either, or in the chamber-rotation condition); preferred heading as the tuning-curve peak or the code's Gaussian-fit method. For 3C, the expected offset is either the median of differences (Methods text) or the difference of medians (Methods equation). I read the subscripts in V32 and V66 as n, which matches the printed p-values closely.
- **Fig. 4 axons:** selected axons or all axons. Bimodality is judged by the sign of the flip score; light-off tuning by the selection test run on dark trials.
- **Fig. 5 clustering:** the Mahalanobis outlier rule (chi-square, 8 degrees of freedom, 95th percentile, or no outlier step as in the reviewer code); class shares averaged over recordings, over mice, or pooled. The cluster sizes 332/522/409 come from the F-test degrees of freedom.
- **Flip-score F-tests:** a mixed model with mouse as a random intercept; per-cell random effects as a variant.
- **Fig. 5K visual-cue-only rotation:** no number of recordings, measure or test is given. Readings: fraction of cells still selective, or tuning-curve range.
- **Decoding:**
  - Input: ΔF/F (Methods, "raw calcium data") or inferred spikes (`HeadingDecoder`).
  - Decoder: the naive Bayes decoder of Etter et al. or `HeadingDecoder`'s.
  - t-test: paired or unpaired.
  - Chance level: 0.18 (Methods) or 0.10 (Figure 6 legend). Under 0.10, the paper's own light-off interval for landmark cells (0.14 to 0.27) excludes chance, which contradicts "plummets to chance levels".
- **Fig. 5E coregistration, the 180° errors and the "tiling":** the paper gives no test. I used its own tools (the V-test; the 18° accuracy window moved to 180°).

**Missing from the paper that claims needed:**
- **Figures S5 and S6:** the text gives the bootstrapped KS p-values (0.0094 and 0.031) but not what is compared, so two readings are named for each.
- **Table S1:** it holds the mixed-model comparisons between decoding classes, so the model for `fig6-heading-below-population` is open.
- **Fig. 5K:** the number of visual-cue-only recordings is not given.

## End of run

33 turns, 7 minutes, result: success.
