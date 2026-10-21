# 001425 · claims · run 39661443864

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001425 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt; head -50 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.02.03.631599.txt",
 "offset": 50
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/BraiDyn-BC/bdbc-data-pipeline && cd bdbc-data-pipeline && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
ab50b1758c5d3281231b8994b694416345fd18ea Sat Jul 5 18:36:10 2025 +0900
./setup.cfg
./requirements-python3.10/requirements-video.txt
./requirements-python3.10/requirements-core.txt
./requirements-python3.10/requirements-browse.txt
./requirements-python3.10/requirements-atlas.txt
./requirements-python3.10/requirements-all.txt
./process.sh
./install.py
./docs/resource/diagram.png
./docs/resource/diagram.drawio
./docs/README.md
./cuda-environment.md
./README.md
./LICENSE
./.gitmodules
./.gitignore
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/bdbc-data-pipeline && cat .gitmodules README.md docs/README.md process.sh | head -250
```

```
[submodule "pipeline-core/bdbc-nwb-packager"]
	path = pipeline-core/bdbc-nwb-packager
	url = [removed: an e-mail address]:BraiDyn-BC/bdbc-nwb-packager.git
[submodule "pipeline-core/bdbc-session-explorer"]
	path = pipeline-core/bdbc-session-explorer
	url = [removed: an e-mail address]:BraiDyn-BC/bdbc-session-explorer.git
[submodule "atlas-registration/bdbc-atlas-registration"]
	path = atlas-registration/bdbc-atlas-registration
	url = [removed: an e-mail address]:BraiDyn-BC/bdbc-atlas-registration.git
[submodule "testing/bdbc-test-nwb-packaging"]
	path = testing/bdbc-test-nwb-packaging
	url = [removed: an e-mail address]:BraiDyn-BC/bdbc-test-nwb-packaging.git
[submodule "atlas-registration/ks-affine2d"]
	path = atlas-registration/ks-affine2d
	url = [removed: an e-mail address]:BraiDyn-BC/python-ks-affine2d.git
[submodule "atlas-registration/ks-affine-aligner"]
	path = atlas-registration/ks-affine-aligner
	url = [removed: an e-mail address]:BraiDyn-BC/python-ks-affine-aligner.git
[submodule "atlas-registration/ks-mesoscaler"]
	path = atlas-registration/ks-mesoscaler
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && for r in bdbc-nwb-packager bdbc-batch-scripts bdbc-test-nwb-packaging python-ks-pupilfitting bdbc-nwb-explorer; do git clone -q https://github.com/BraiDyn-BC/$r && (cd $r && echo "$r $(git log -1 --format='%H %cd')"); done; cd bdbc-data-pipeline && git submodule status; find $TMPDIR/bdbc-batch-scripts -type f -not -path '*/.git/*' | head -80
```

```
bdbc-nwb-packager 0170a1c9940ca4e69755c5bfb60815b90c4195a9 Fri Sep 26 08:17:02 2025 +0900
bdbc-batch-scripts 763cf803bc14093c8800dca671deb8c97940f655 Fri Feb 14 22:58:08 2025 +0900
bdbc-test-nwb-packaging 4584156440e9cd93243162fcf29c1a33d4790aa9 Tue Jan 7 13:10:36 2025 +0900
python-ks-pupilfitting dc14b3649b0f6c8c7aa42ef1dad09db1bfe8c690 Fri Sep 6 22:59:46 2024 +0900
bdbc-nwb-explorer 30e2e45be5bc44cf346ede5b8b8119906b5d7c95 Wed Aug 5 17:35:12 2026 +0900
-3144657761e9e7ad22bd55e5c4c27f19a4e5926c atlas-registration/bdbc-atlas-registration
-82b5235ec93779359fa1719f87b34a876a7d0823 atlas-registration/ks-affine-aligner
-6131c2381e711bd8276ffff05b6484bb219d0002 atlas-registration/ks-affine2d
-b81db8538aea470f2d238f783824b11a8017be53 atlas-registration/ks-mesoscaler
-426f07ca62d2846f9530404fd464a71e611fa1be pipeline-core/bdbc-nwb-packager
-58089f27d4c8ca6458ac5e8e48597ce4b7792204 pipeline-core/bdbc-session-explorer
-309c5fbdbc065cffdaf46e9160383545e5c8104f repository-browsing/bdbc-nwb-explorer
-763cf803bc14093c8800dca671deb8c97940f655 testing/bdbc-batch-scripts
-4584156440e9cd93243162fcf29c1a33d4790aa9 testing/bdbc-test-nwb-packaging
-dc14b3649b0f6c8c7aa42ef1dad09db1bfe8c690 video-tracking/ks-pupilfitting
/tmp/claude-1001/bdbc-batch-scripts/sanity-check/sanity_check_nwb.py
/tmp/claude-1001/bdbc-batch-scripts/sanity-check/sanity_check_across_sessions.ipynb
/tmp/claude-1001/bdbc-batch-scripts/sanity-check/bdbc_nwb_tools.py
/tmp/claude-1001/bdbc-batch-scripts/README.md
/tmp/claude-1001/bdbc-batch-scripts/LICENSE
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bdbc-nwb-packager && git checkout -q 426f07ca62d2846f9530404fd464a71e611fa1be && git log -1 --format='%H %cd'; cd $TMPDIR/bdbc-batch-scripts && cat README.md; wc -l sanity-check/*; python3 -c "
import json;nb=json.load(open('sanity-check/sanity_check_across_sessions.ipynb'))
for c in nb['cells']:
  print('----',c['cell_type']); print(''.join(c['source'])[:3000])
"
```

```
426f07ca62d2846f9530404fd464a71e611fa1be Wed May 28 15:07:32 2025 +0900
# bdbc-batch-scripts

a set of batch scripts for validation of the output NWB files.

## `sanity-check`

The Jupyter Notebook file (.ipynb file) should work under the existence of
the accompanying Python (.py) files in the same directory.
  246 sanity-check/bdbc_nwb_tools.py
  105 sanity-check/sanity_check_across_sessions.ipynb
  246 sanity-check/sanity_check_nwb.py
  597 total
---- markdown
"Sanity check" of the resulting NWB files through visual inspection:

- check if there are unexpectedly many NaNs or zeros in the time series
- check if there are any "outlier" sessions within an animal

### Assumptions
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bdbc-nwb-packager && find . -name '*.py' -not -path './.git/*' | xargs wc -l | sort -n | tail -40; grep -rn -i "trial\|success\|response\|pull" --include=*.py . | grep -v "^./.git" | head -80
```

```
6 ./setup.py
    35 ./bdbc_nwb_packager/types.py
    39 ./bdbc_nwb_packager/tracking/__init__.py
    39 ./bdbc_nwb_packager/trials/__init__.py
    51 ./bdbc_nwb_packager/file_metadata/rois.py
    52 ./bdbc_nwb_packager/file_metadata/devices.py
    53 ./bdbc_nwb_packager/configure/__init__.py
    64 ./bdbc_nwb_packager/file_metadata/__init__.py
    69 ./bdbc_nwb_packager/file_metadata/common.py
    77 ./bdbc_nwb_packager/__init__.py
    96 ./bdbc_nwb_packager/tracking/alignment.py
   105 ./bdbc_nwb_packager/videos.py
   110 ./bdbc_nwb_packager/daq.py
   113 ./bdbc_nwb_packager/trials/io.py
   116 ./bdbc_nwb_packager/file_metadata/recording.py
   118 ./bdbc_nwb_packager/file_metadata/highlevel.py
   129 ./bdbc_nwb_packager/configure/session.py
   140 ./bdbc_nwb_packager/tracking/validation.py
   145 ./bdbc_nwb_packager/file_metadata/session.py
   156 ./bdbc_nwb_packager/tracking/pupil.py
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/BraiDyn-BC/bdbc-session-explorer && cd bdbc-session-explorer && git checkout -q 58089f27d4c8ca6458ac5e8e48597ce4b7792204 && grep -rn -i "trial\|pull\|reaction\|success" --include=*.py --include=*.json --include=*.yaml --include=*.toml . | grep -v "^./.git" | head -60; sed -n 1,218p $TMPDIR/bdbc-nwb-packager/bdbc_nwb_packager/trials/spec.py | sed -n 140,218p
```

```
./bdbc_session_explorer/session.py:75:    trialspec: Optional[_env.TrialSpec] = None
./bdbc_session_explorer/session.py:172:    metadata: Optional[_env.TrialSpecSet] = None,
./bdbc_session_explorer/session.py:175:    metadata = _env.get_trials_metadata(metadata=metadata, sessionroot=sessroot)
./bdbc_session_explorer/session.py:186:    metadata: _env.TrialSpecSet,
./bdbc_session_explorer/session.py:210:    metadata: _env.TrialSpecSet,
./bdbc_session_explorer/session.py:237:        trialspec=metadata.get(sessiontype, None),
./bdbc_session_explorer/env.py:63:TrialSpec = dict[str, Any]
./bdbc_session_explorer/env.py:64:TrialSpecSet = dict[str, TrialSpec]
./bdbc_session_explorer/env.py:203:def get_trials_metadata(
./bdbc_session_explorer/env.py:204:    metadata: Optional[TrialSpecSet] = None,
./bdbc_session_explorer/env.py:206:) -> TrialSpecSet:
./bdbc_session_explorer/env.py:209:        trialspec_dir = sessroot / "metadata" / "trials"
./bdbc_session_explorer/env.py:210:        if not trialspec_dir.exists():
./bdbc_session_explorer/env.py:211:            raise FileNotFoundError(str(trialspec_dir))
./bdbc_session_explorer/env.py:214:        for specfile in trialspec_dir.glob('*.json'):
./bdbc_session_explorer/env.py:218:            raise KeyError(f"'task' trial type not found in: {str(trialspec_dir)}")
./bdbc_session_explorer/__init__.py:48:TrialSpec = env.TrialSpec
./bdbc_session_explorer/__init__.py:49:TrialSpecSet = env.TrialSpecSet
./bdbc_session_explorer/__init__.py:69:get_trials_metadata = env.get_trials_metadata
    @classmethod
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bdbc-nwb-explorer && git checkout -q 309c5fbdbc065cffdaf46e9160383545e5c8104f && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -40; grep -rn -i "corr\|response_rate\|success\|cluster\|ward" --include=*.py . | head -20; cd $TMPDIR/bdbc-test-nwb-packaging && find . -type f -not -path './.git/*' | head; grep -rln -i "corr\|cluster" . | grep -v .git | head
```

```
309c5fbdbc065cffdaf46e9160383545e5c8104f Sat Jul 5 18:31:36 2025 +0900
./setup.cfg
./setup.py
./pyproject.toml
./bdbc_nwb_explorer/view.py
./bdbc_nwb_explorer/process.py
./bdbc_nwb_explorer/plot.py
./bdbc_nwb_explorer/logging.py
./bdbc_nwb_explorer/io.py
./bdbc_nwb_explorer/filters.py
./bdbc_nwb_explorer/auxdata.py
./bdbc_nwb_explorer/__init__.py
./bdbc_nwb_explorer/data/face_video.csv
./bdbc_nwb_explorer/data/eye_video.csv
./bdbc_nwb_explorer/data/daq.csv
./bdbc_nwb_explorer/data/body_video.csv
./bdbc_nwb_explorer/data/AllenCCF_masks.h5
./README.md
./LICENSE
./.gitignore
[... 26 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "001425",
 "output_mode": "content",
 "glob": "!transcripts/**",
 "head_limit": 20
}
```

```
targets/dandisets.json:5934:   "dandiset": "001425",
papers/manifest.yaml:1743:  '001425':
```

**Agent calls Bash**

```bash
sed -n 5925,5990p targets/dandisets.json; sed -n 1740,1760p papers/manifest.yaml
```

```
"title": "Cerebral blood flow is modulated by astrocytic cAMP elevation independently of IP3R2-mediated Ca2+ signaling in mice",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001425",
   "name": "BraiDyn-BC: mouse cued-lever-pull task dataset",
   "published_version": "0.250705.0947",
   "asset_count": 1838,
   "size_gb": 8064.86,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml | grep -n "inferred\|data:\|elsewhere\|where\|checks\|code:\|repository" | head -30; sed -n 1,80p tools/claims_check.py
```

```
1:  data: with_labels
20:  data: with_labels
39:  data: with_labels
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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
cd $TMPDIR/bdbc-nwb-packager && grep -rn "likelihood\|0\.2\|threshold" bdbc_nwb_packager/tracking/*.py bdbc_nwb_packager/timebases.py | head -20; grep -rn "def \|major\|diameter" $TMPDIR/python-ks-pupilfitting/ks_pupilfitting/*.py 2>/dev/null | head -20; ls $TMPDIR/python-ks-pupilfitting
```

```
bdbc_nwb_packager/tracking/dlc.py:60:    downsample_pcutoff: float = 0.2,
bdbc_nwb_packager/tracking/dlc.py:138:                        threshold=downsample_pcutoff,
bdbc_nwb_packager/tracking/dlc.py:157:                    confidence=_np.array(dlctab[scorer, kpt, 'likelihood'].values),
bdbc_nwb_packager/tracking/validation.py:35:VALIDATION_THRESHOLD = 0.2  # must be higher (e.g. 0.9999)
bdbc_nwb_packager/tracking/validation.py:67:    threshold: float = VALIDATION_THRESHOLD,
bdbc_nwb_packager/tracking/validation.py:81:    # likelihood-based filtering
bdbc_nwb_packager/tracking/validation.py:82:    valid = dlcdata[scorer, keypoint, 'likelihood'].values >= threshold
LICENSE
README.md
pupilfitting
pyproject.toml
setup.cfg
setup.py
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/001425/10.1101-2025.02.03.631599.yaml",
 "content": "# Claims for Kondo, Sehara, Harukuni, Aoki et al. (2025) on dandiset 001425.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# following docs/protocol.md (pilot-10), Reader, steps 1 to 4.\n#\n# Text read: the bioRxiv preprint, version 1 (doi:10.1101/2025.02.03.631599), from its JATS XML\n# as stored in paper/10.1101-2025.02.03.631599.txt. It holds the main text, the Methods, the\n# figure legends of Figures 1 to 6 and the legends of Supplementary Figures S1 to S4. The text\n# has the legends of Tables 1 to 4 but not their contents (session counts per animal and type,\n# keypoint names, DeepLabCut training image counts, NWB contents), and there is no PDF, so no\n# figure or table could be read. The claims below rest on the sentences of the text.\n#\n# Code read: https://github.com/BraiDyn-BC/bdbc-data-pipeline at commit ab50b17 (2025-07-05),\n# with the submodule commits it pins, bdbc-nwb-packager 426f07c, bdbc-session-explorer 58089f2,\n# bdbc-nwb-explorer 309c5fb, bdbc-batch-scripts 763cf80 and python-ks-pupilfitting dc14b36. The\n# code builds the NWB files (DAQ logs, ROI signals, keypoints, pupil fits, trial tables), aligns\n# the Allen CCF atlas, fits pupil ellipses, and holds a visual sanity check of the NWB files. It\n# confirms the likelihood cut-off of 0.2 used when keypoints are down-sampled\n# (bdbc_nwb_packager/tracking/dlc.py). It holds no analysis behind Figures 3 to 6 or Figure S2b:\n# not the response and success rates, the clustering, the keypoint-encoder correlations, the\n# sensory maps or the transient detection. The MATLAB preprocessing (motion correction, the\n# trial tables) is stated as not in the repository, and the trial-table columns are defined by\n# JSON files outside it. So every analysis detail below comes from the Methods and legends, or\n# is named as open.\n#\n# Data the paper used. 25 VGluT1-Cre x Ai162 (GCaMP6s) mice, 11 male and 14 female, aged 17 to\n# 31 weeks at the end of the experiments. Each was trained for 15 daily sessions (30 min) of a\n# tone-cued lever-pull task (a pull is the lever held beyond 1 mm; it must start within 1 s of a\n# 200 ms 10 kHz tone and be held for T_pull, which starts at 1 ms, rises by 50 ms after 80%\n# success over 20 trials, at most every 20 trials, up to 400 ms, and starts each session at the\n# previous session's final value minus 100 ms). Resting-state sessions (10 min) on recording\n# days 0, 1, 7 and 15 (day 8 for one mouse), and a sensory-mapping session under anaesthesia\n# (15 min; visual LED to the left eye, vibration or air puff on the right whisker pad, white\n# noise; 8 mice had two). Of 375 task sessions, 364 have imaging. Measured variables are\n# wide-field one-photon imaging at 60 Hz alternating 470 and 405 nm excitation (30 Hz per\n# channel, 288 x 288 pixels; hemodynamics-corrected dF/F of 22 Allen CCF ROIs per hemisphere),\n# lever position (rotary encoder), licking, a load cell for body motion, tone, reward and\n# stimulus TTLs, temperature, humidity, air pressure and CO2, and 100 Hz videos of the upper\n# body, the right face and the right eye with DeepLabCut keypoints and a fitted pupil ellipse,\n# both at the video rate and down-sampled to 30 Hz. The Data Records name the 15 task sessions\n# and 4 resting-state sessions as the dataset; whether the sensory-mapping sessions are\n# deposited is not said plainly (Table 1's legend counts them). The manual annotations used to\n# validate the atlas landmarks and the DeepLabCut models are not described as deposited.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001425\"\npaper: doi:10.1101/2025.02.03.631599\nclaims:\n- id: cohort-sex-age\n  statement: The dataset comes from 25 mice of both sexes, 11 males and 14 females, aged 17 to 31\n    weeks at the end of the experiments.\n  source: Methods, Animals, paragraph 1\n  quote: The mice of both sexes (11 males and 14 females) were used for the experiments. The age\n    ranged from 17–31 weeks at the end of experiments.\n  expected:\n  - quantity: number of mice\n    value: 25\n    tolerance: 0\n  - quantity: number of male mice\n    value: 11\n    tolerance: 0\n  - quantity: number of female mice\n    value: 14\n    tolerance: 0\n  criterion: Counts of subjects are exact, so the tolerance is 0. Reproduced when the subjects\n    with any session number 25 with 11 males and 14 females, and every subject's age at its\n    last session lies within 17 to 31 weeks widened by 10% of each bound (15.3 to 34.1 weeks),\n    age taken from the subject metadata (age or date of birth) and the session dates.\n- id: task-sessions-collected\n  statement: Of the 375 task training sessions (25 mice by 15 sessions), data were collected from\n    364 (97%); the 11 others lacked complete imaging. All 15 sessions were collected for 16 of\n    the 25 mice.\n  source: Background & Summary, paragraph 3; Technical Validation, paragraph 2; Figure 3d legend\n  quote: Of the 375 task training sessions conducted, we successfully collected data from 364\n    sessions ( Fig. 3d ; Table 1 ) and completed data collection for all 15 sessions in 16 out of\n    25 animals.\n  expected:\n  - quantity: task training sessions with data\n    value: 364\n    tolerance: 0\n  - quantity: mice with all 15 task sessions\n    value: 16\n    tolerance: 0\n  criterion: Counts of deposited sessions are exact, so the tolerance is 0. A task session is one\n    whose session description or file name marks it as a task (lever-pull) session; recordings\n    deposited more than once count once. Reproduced when 364 distinct task sessions are found\n    and 16 mice have all 15. The Data Records sentence (15 task and 4 resting-state sessions per\n    mouse) also bears on the count of resting-state sessions, which is reported without a\n    criterion, as Table 1's contents are not in the text.\n- id: imaging-frame-counts\n  statement: Each task session was imaged for 30 min (108000 frames at 60 Hz, so 54000 frames per\n    excitation channel at 30 Hz), each resting-state session for 10 min and the sensory-mapping\n    session for 15 min.\n  source: Methods, Acquisition of wide-field one-photon image, paragraph 1; Data Records, Imaging\n    Raw Data\n  quote: We imaged 108000 frames (30 min) in each task session, 36000 frames in each\n    resting-state session (10 min on recording days 1, 7, 15), and 54000 frames in the sensory\n    mapping session (recording day 16).\n  expected:\n  - quantity: frames per excitation channel, task session\n    value: 54000\n    tolerance: 0\n  - quantity: frames per excitation channel, resting-state session\n    value: 18000\n    tolerance: 0\n  - quantity: frames per excitation channel, sensory-mapping session\n    value: 27000\n    tolerance: 0\n  inferred: The per-channel counts are the printed 60 Hz frame counts halved, as the Methods say\n    the two channels alternate and the TIFF files hold (recording duration in seconds x 30 Hz)\n    frames.\n  criterion: The paper's 60 Hz counts are read as the sum over the two channels, from the\n    Methods sentence that the effective rate is 30 Hz and the Data Records sentence on TIFF\n    frame counts. Reproduced when the 30 Hz ROI series (and, where they are read, the TIFF\n    stacks) of most sessions of each type have these lengths; sessions that differ are listed\n    with their lengths.\n- id: training-breaks\n  statement: Training had 3.1 +/- 0.6 breaks per mouse of 2.3 +/- 0.7 days each (mean +/- s.d.,\n    25 mice), and recording days 1 to 16 spanned 24.28 +/- 3.2 calendar days.\n  source: Methods, Behavioral task, paragraph 1\n  quote: There were occasional training breaks of typically 2–3 days without any handling ( e.g.\n    over weekends; 3.1 ± 0.6 breaks throughout training; 2.3 ± 0.7 days per break; mean ± s.d., n\n    = 25 mice). ... The entire recording period (recording day 1 to 16) spanned 24.28 ± 3.2\n    calendar days (mean ± s.d.).\n  expected:\n  - quantity: breaks per mouse, mean\n    value: 3.1\n    tolerance: 0.6\n  - quantity: days per break, mean\n    value: 2.3\n    tolerance: 0.7\n  - quantity: calendar days from recording day 1 to 16, mean\n    value: 24.28\n    tolerance: 3.2\n  criterion: Tolerances are the paper's stated s.d. Dates are the session start dates. A break is\n    a gap of two or more calendar days without a session between consecutive task sessions\n    (days 1 to 15), and its length is the number of days without a session. The span is from\n    the day 1 task session to the sensory-mapping session (day 16), counted inclusively or as\n    a difference (both shown). Open details, each run. (1) Whether \"days per break\" is the\n    mean over all breaks pooled or the mean over mice of each mouse's mean. (2) Whether a\n    missing (not deposited) task session that falls in the schedule counts as a training day;\n    the deposited dates cannot show this, so the readings are the deposited dates alone, and\n    those dates with gaps of one day not counted as breaks. If no sensory-mapping session is\n    deposited, the span is blocked and the other two values are still tested.\n- id: fig3c-response-rate-increase\n  statement: Across the population the response rate to the tone rose over training, from about\n    0.55 in task session 1 to about 0.85 in task session 15 (median over mice).\n  source: Technical Validation, paragraph 2; Figure 3c, top panel\n  quote: The response rate to the sound cue tended to increase overall (∼0.55 in task training\n    session 1 to ∼0.85 in task training session 15; median)\n  expected:\n  - quantity: median response rate, task session 1\n    value: 0.55\n    tolerance: 0.055\n  - quantity: median response rate, task session 15\n    value: 0.85\n    tolerance: 0.085\n  criterion: From the Figure 3 legend, the response rate is the number of valid pulls over the\n    number of tones, a valid pull being a pull (lever beyond 1 mm) initiated within 1 s of the\n    tone onset; per session, then the median over the mice with that session (thick black line\n    of Figure 3c). How a valid pull is identified is open, with two readings, both run. (a)\n    From the trial table's outcome labels, counting successes and failures (aborted pulls) as\n    valid and misses as not, following the Methods' trial outcomes. (b) From the lever trace,\n    a trial being valid when the lever crosses 1 mm within 1 s of tone onset. Reproduced when,\n    under one reading, both medians are within tolerance and session 15's exceeds session 1's.\n- id: fig3c-success-rate-constant\n  statement: The population success rate stayed roughly constant across the 15 task sessions.\n  source: Technical Validation, paragraph 2; Figure 3c, middle panel\n  quote: while the success rate seemed to be constant as a whole ( Fig. 3c )\n  criterion: The success rate is the number of successful (rewarded) pulls over the number of\n    tones (Figure 3 legend), per session, and the population value is the median over mice. The\n    paper gives no test and no bound for \"constant\", so the readings are (a) the session-15\n    median within 10% (relative) of the session-1 median, the protocol's default tolerance;\n    (b) no monotonic trend of the 15 session medians, Spearman correlation with session index\n    at p >= 0.05. Successes are counted from reward deliveries and, where the trial table has\n    them, from its outcome labels (both shown). The claim holds when both readings hold, fails\n    when both fail, and is blocked as methods_underspecified when they differ. The change in\n    the response rate over the same sessions is shown alongside for contrast.\n  depends_on:\n  - fig3c-response-rate-increase\n- id: fig3d-tpull-clusters\n  statement: Hierarchical clustering (Ward's method) of the session-by-session T_pull_final\n    divides the mice into two clusters, A with 7 mice and B with 18.\n  source: Technical Validation, paragraph 2; Figure 3d and 3e legends\n  quote: The hierarchical clustering revealed that mice could be divided into two clusters in\n    terms of T pull_final ( Fig. 3d ).\n  expected:\n  - quantity: mice in cluster A\n    value: 7\n    tolerance: 0\n  - quantity: mice in cluster B\n    value: 18\n    tolerance: 0\n  criterion: Cluster sizes are counts, with tolerance 0 (10% of 7 is under one mouse). T_pull_final\n    is the required pull duration at the end of each session (Methods, Tone-triggered\n    lever-pull task), read from the trial table's required-duration field at the last trial;\n    where no such field exists, the author asks. Each mouse is a vector of its T_pull_final over\n    task sessions 1 to 15, clustered by Ward's method (Figure 3d legend) on Euclidean distance\n    and cut at two clusters; cluster A is the one with the higher mean T_pull_final. Open\n    details, each run. (1) The feature, \"the chronological change in T_pull_final\", read as\n    (a) the 15 values themselves, (b) the 14 differences between consecutive sessions. (2)\n    Missing sessions (9 mice), read as (i) linear interpolation from the neighbouring sessions\n    (carrying the nearest value at the ends), (ii) the previous session's value carried\n    forward, (iii) the next session's initial T_pull plus 100 ms where that session exists,\n    following the Methods' rule. Reproduced when a reading gives clusters of 7 and 18.\n- id: fig3e-cluster-a-high-tpull\n  statement: Mice of cluster A had high success rates in the early sessions (about session 5),\n    which led to a high T_pull_final that was often maintained into the late sessions.\n  source: Technical Validation, paragraph 2; Figure 3e\n  quote: Mice belonging to one cluster (cluster A) showed high success rates in the early sessions\n    (∼5) leading to high T pull_final which were often maintained even in the late sessions.\n  depends_on:\n  - fig3d-tpull-clusters\n  - fig3c-success-rate-constant\n  criterion: Uses the clusters of fig3d-tpull-clusters (under each reading that gives 7 and 18).\n    The paper gives no test; \"high\" is read against cluster B, the contrast of Figure 3e.\n    Reproduced when (1) cluster A's median success rate exceeds cluster B's in the early\n    sessions, read as (a) sessions 1 to 5, (b) session 5 alone, and (2) cluster A's median\n    T_pull_final exceeds cluster B's in the late sessions, read as (a) sessions 11 to 15, (b)\n    session 15 alone. Per-mouse values are shown.\n- id: fig3e-cluster-b-similar-rates\n  statement: Mice of cluster B rarely reached a high T_pull_final, but in the late sessions their\n    response and success rates were similar to those of cluster A.\n  source: Technical Validation, paragraph 2; Figure 3e; Figure S1c\n  quote: Mice belonging to the other cluster (cluster B) rarely achieved a high T pull_final ,\n    while they accomplished a response rate and success rate similar to the cluster A mice in\n    the late sessions ( Fig. 3e , Fig. S1).\n  depends_on:\n  - fig3d-tpull-clusters\n  - fig3c-response-rate-increase\n  - fig3c-success-rate-constant\n  criterion: Uses the clusters of fig3d-tpull-clusters. The paper gives no test or bound. \"High\n    T_pull_final\" is read as (a) the 400 ms maximum, (b) above the median of all mice's\n    T_pull_final values; \"rarely\" holds when the fraction of cluster B's mouse-sessions above\n    that level is below cluster A's and below one half. \"Late sessions\" are read as (a)\n    sessions 11 to 15, each mouse's mean, (b) session 15. \"Similar\" is read as (a) a two-sided\n    Mann-Whitney U test of A against B with p >= 0.05, (b) group medians within 10% of cluster\n    A's median. Response and success rates as in fig3c-response-rate-increase and\n    fig3c-success-rate-constant. The claim holds when the T_pull_final part holds and, for both\n    rates, the similarity holds under both readings of \"similar\"; when these readings differ it\n    is blocked as methods_underspecified, with every result shown.\n- id: methods-no-signal-degradation\n  statement: Fluorescence signal degradation across imaging sessions was not observed.\n  source: Methods, Acquisition of wide-field one-photon image, paragraph 1\n  quote: The total power of excitation lights (blue and violet) was set at ∼10 mW and the\n    fluorescent signal degradation across imaging sessions was not observed.\n  criterion: A claim of absence for which the paper names no measure and no test. The readings\n    the text allows are (a) the raw 470 nm fluorescence (the ROI baseline F_B0, the median over\n    time, where the dataset holds raw ROI signals; otherwise the session-mean intensity of the\n    blue TIFF stack within the cortical ROI masks) against task-session index, (b) the s.d. of\n    the corrected dF/F per ROI against task-session index. For each, a per-mouse Spearman\n    correlation with session index, and a Wilcoxon signed-rank test of the 25 correlations\n    against 0 at p < 0.05. The claim holds when neither reading finds a significant decline,\n    fails when both do, and is blocked as methods_underspecified when they differ; the size of\n    the change (session 15 over session 1, median over mice) is reported either way.\n- id: fig4ab-landmark-validation\n  statement: MesoNet-inferred skull landmarks used to register the Allen CCF agreed with manual\n    annotations of three representative sessions from each of the 25 mice (75 sessions).\n  source: Technical Validation, paragraph 3; Figure 4a,b legend\n  quote: We validated the accuracy of this method by comparing the MesoNet-based skull-landmark\n    annotations with the manual annotations, based on three representative sessions from each of\n    the 25 animals ( Fig. 4a,b ).\n  criterion: The paper gives no number or bound for the agreement. The test needs the manual\n    landmark annotations, which the paper does not describe as deposited; the dataset's\n    atlas_to_data_transform alone cannot be compared with them. Reproduced only if the manual\n    annotations are found, when the warped manual landmarks fall near the CCF reference\n    landmarks as in Figure 4b; the distances (median and 95th percentile, in atlas pixels) are\n    reported.\n- id: fig4d-visual-map\n  statement: In the sensory-mapping sessions, visual stimulation of the left eye evoked the\n    strongest activity in the right occipital cortex, at VISp in the registered atlas.\n  source: Technical Validation, paragraph 3; Figure 4d\n  quote: Visual stimuli to the left eye of mice elicited prominent activity in the right occipital\n    cortex ( Dräger 1975 ; Grinvald et al. 1986 ; Schuett, Bonhoeffer, and Hübener 2002 )\n    corresponding to VISp (primary visual area) in the atlas.\n  criterion: From the Figure 4d legend, the first sensory-mapping session of each mouse; the\n    response is the trial-averaged activity over 2 s from stimulus onset, normalized to 0 to 1\n    per mouse and stimulus; the area is the region above the 80th percentile of the normalized\n    map. Open details, each run. (1) The map, read as (a) the 44 ROI dF/F series in the NWB\n    file, (b) pixel maps from the blue TIFF stack as dF/F against the session median (the\n    Methods' dF/F), without hemodynamic correction, as the Methods describe it for ROIs only.\n    (2) The baseline, read as (a) none (dF/F is already relative to the session median), (b)\n    the mean over the 2 s before stimulus onset subtracted. Stimulus onsets are the visual\n    stimulus TTL onsets. Reproduced when, under one reading, right VISp is the ROI with the\n    largest response (or, for pixel maps, the peak falls inside right VISp) in the mean over\n    mice, and in more than half of the mice. If no sensory-mapping session is deposited the\n    claim is blocked.\n- id: fig4d-tactile-map\n  statement: Vibration of the right whisker pad evoked a robust response in the left barrel cortex\n    (SSp-bfd), with marked laterality.\n  source: Technical Validation, paragraph 3; Figure 4d\n  quote: Tactile stimuli to the right whisker pad elicited a robust response in the left SSp-bfd,\n    a primary sensory cortex for processing whisker-related sensory information with marked\n    hemispheric laterality\n  criterion: As fig4d-visual-map, with the tactile stimulus TTL onsets (vibration or air puff, both\n    included). Reproduced when, under one reading, left SSp-bfd is the ROI with the largest\n    response (or holds the pixel peak) in the mean over mice and in more than half of the\n    mice, and its response exceeds that of right SSp-bfd.\n- id: fig4d-auditory-map\n  statement: White-noise stimulation evoked spreading activity that included a multimodal sensory\n    area in the parietal cortex.\n  source: Technical Validation, paragraph 3; Figure 4d\n  quote: Auditory stimuli evoked spreading activity, including a multimodal sensory area in the\n    parietal cortex\n  criterion: As fig4d-visual-map, with the auditory stimulus TTL onsets. The parietal multimodal\n    area is not named; it is read as any of the posterior parietal ROIs of the Allen CCF dorsal\n    map (VISa, VISrl, or a ROI named PTLp), in either hemisphere. \"Spreading\" is read as an\n    80th-percentile region covering more than one ROI. Reproduced when, under one reading, the\n    80th-percentile region of the mean over mice includes a parietal ROI and more than one ROI.\n- id: figs2b-no-aberrant-transients\n  statement: The mice showed no sign of the aberrant short-duration, large-amplitude calcium\n    transients reported in some transgenic lines; no cluster of transients had high prominence\n    (> 0.1 dF/F) and narrow width (< 0.5 s).\n  source: Technical Validation, paragraph 3; Figure S2b legend\n  quote: High prominence (> 0.1 in Δ F / F ) and narrow width (< 0.5 s) of the transients were not\n    detected in each animal (right).\n  criterion: From the Figure S2b legend. Each mouse's first resting-state recording (day 0); the\n    left frontal, left barrel, left retrosplenial and right visual ROIs; transients detected in\n    the corrected dF/F with their prominences and widths; per mouse and region, K-means (k = 2)\n    on (prominence, width), and the two cluster centres. Reproduced when no centre in any mouse\n    and region has prominence > 0.1 and width < 0.5 s, and not reproduced when any does. Open\n    details, each run. (1) Peak detection, which the paper does not name, read as\n    scipy.signal.find_peaks (SciPy is the library the Methods name) (a) with no threshold, (b)\n    with a minimum prominence of 0.01 dF/F; width at half prominence in seconds at 30 Hz.\n    (2) The ROIs, \"frontal\" read as MOs or MOp, \"visual\" as VISp, \"barrel\" as SSp-bfd,\n    \"retrosplenial\" as RSPd or RSPagl. (3) K-means features raw or z-scored. The number of\n    transients per mouse is reported.\n- id: fig5abc-dlc-error\n  statement: DeepLabCut keypoints differed from manual annotations only by minor errors on\n    validation frames (192 frames from 25 mice for the body and face cameras, 190 for the eye).\n  source: Technical Validation, paragraph 4; Figure 5a-c legend\n  quote: Comparison of DeepLabCut model-based keypoint annotations with manual annotations showed\n    minor errors, validating the quality of our models ( Fig. 5a-c ).\n  criterion: The paper gives no number in the text (the 95th percentiles are in the figure, which\n    could not be read). The test needs the manual annotations of the validation frames (from\n    task sessions 3, 6, 9 and 12, Figure S3 legend), which the paper does not describe as\n    deposited. Blocked unless they are found; if found, the 95th-percentile error per keypoint\n    is reported, and the claim holds when it is small against the keypoint spacing.\n- id: fig5f-lever-tip-correlation\n  statement: The lever-tip position tracked from the body video correlated highly with the\n    encoder lever position, R = 0.98 +/- 0.02 (mean +/- s.d.).\n  source: Technical Validation, paragraph 4; Figure 5e,f\n  quote: Moreover, the lever tip position estimated from the videography showed a markedly high\n    correlation (0.98 ± 0.02; mean ± s.d.) with the encoder-based lever position ( Fig. 5e,f ).\n  expected:\n    quantity: mean Pearson R, lever-tip keypoint y against encoder lever position\n    value: 0.98\n    tolerance: 0.02\n  criterion: Tolerance is the paper's stated s.d. From the Figure 5 legend, Pearson's R between\n    the keypoint's y position and the encoder-based lever position, over the frames of all\n    successful trials of a session, per task session with body video and at least one\n    successful trial (354 sessions, 25 mice). Open details, each run. (1) Sampling, read as (a)\n    keypoints at the 100 Hz video rate with the lever position averaged over each video frame\n    (each dot is a video frame in Figure 5e), (b) the down-sampled 30 Hz series. (2) Keypoints\n    with likelihood below 0.2 dropped (the Methods' cut-off, confirmed in\n    bdbc_nwb_packager/tracking/dlc.py) or kept. (3) The frames of a trial, read as (a) the trial\n    interval of the trial table, (b) tone onset to tone onset plus 1 s plus the trial's T_pull.\n    (4) The summary, read as (a) mean and s.d. over sessions (the text), (b) over the per-mouse\n    means (the Figure 5f legend). (5) The sign, as computed and as an absolute value, since the\n    image y axis points down. Reproduced when, under one reading, the mean R is within\n    tolerance.\n- id: fig5f-forepaw-correlation\n  statement: The right forepaw, which pulls the lever, correlated with the lever position (R = 0.49\n    +/- 0.23), and the left forepaw did not (R = 0.05 +/- 0.19), over 354 task sessions from 25\n    mice.\n  source: Technical Validation, paragraph 4; Figure 5d-f\n  quote: We found this is exactly the case, based on the 354 task-recording sessions of our dataset\n    that successfully included upper-body videos ( Fig. 5d-f ; right forepaw, 0.49 ± 0.23; left\n    forepaw, 0.05 ± 0.19; mean±s.d., n = 354 sessions from 25 animals\n  expected:\n  - quantity: mean Pearson R, right forepaw\n    value: 0.49\n    tolerance: 0.23\n  - quantity: mean Pearson R, left forepaw\n    value: 0.05\n    tolerance: 0.19\n  - quantity: task sessions analysed\n    value: 354\n    tolerance: 0\n  depends_on:\n  - fig5f-lever-tip-correlation\n  criterion: Tolerances are the paper's stated s.d.; the session count is exact. As\n    fig5f-lever-tip-correlation, with the right and left forepaw keypoints, under the same\n    readings. The sessions are the 355 task sessions with an upper-body video less the one with\n    no successful trial. Reproduced when, under one reading, both means are within tolerance and\n    the right forepaw's exceeds the left's.\n- id: fig6b-movement-order\n  statement: In the example session, the forepaws and the nose began moving before lever-pull\n    onset, and the jaw and pupil diameter changed after it.\n  source: Technical Validation, paragraph 5; Figure 6b\n  quote: While some body parts, such as forepaws and nose, began moving before the lever-pull\n    onset, others, including jaw and pupil diameter, moved afterward at least in this session.\n  criterion: The example session is not identified, so the readings are (a) the mean over all\n    task sessions with videos of each session's trial average, (b) the fraction of sessions in\n    which the order holds, the claim holding under (b) when it holds in more than half. Lever-\n    pull onset is the lever crossing 1 mm (Methods), for pulls in (a) successful trials, (b)\n    all valid pulls. Traces are taken from -1 s to 3 s around onset (the range of Figure 6c),\n    as the keypoint's displacement from its mean position over -1 to -0.5 s. A trace's onset\n    is the first time its trial average leaves the mean +/- 2 s.d. of that baseline window; this\n    rule is not in the paper and is a standard choice, shown also with 3 s.d. Reproduced when,\n    under one reading, both forepaws and the nose have onsets before 0 and the jaw and pupil\n    diameter after 0.\n- id: fig6b-motor-somatosensory-after-reward\n  statement: In the example session, MOs activity returned quickly to baseline after the pull,\n    while MOp and the upper-limb and nose somatosensory areas (SSp-ul, SSp-n) stayed slightly\n    above baseline after reward delivery.\n  source: Technical Validation, paragraph 5; Figure 6b\n  quote: The secondary motor cortex (MOs) quickly recovered to the baseline level. In contrast, the\n    primary motor (MOp) and somatosensory cortex (SSpul and SSpn) showed slightly higher activity\n    than the baseline level after the reward delivery.\n  criterion: The example session is not identified; readings (a) and (b) for sessions and pulls\n    as in fig6b-movement-order. Trial-averaged corrected dF/F aligned to lever-pull onset,\n    baseline the mean over -1 to 0 s. After reward is read as (a) 1 to 3 s after onset (to the\n    end of the Figure 6c range), (b) 0.5 to 2 s after reward delivery in successful trials.\n    The hemisphere is not given, read as left (contralateral to the pulling forelimb), right,\n    and their mean. Reproduced when, under one reading, MOs's post-reward mean minus baseline is\n    smaller than each of MOp's, SSp-ul's and SSp-n's, and those three are above baseline.\n- id: fig6b-sensory-areas-track-pupil\n  statement: In the example session, OB, RSPagl, AUDs and VISp had activity time courses that\n    closely matched pupil dilation.\n  source: Technical Validation, paragraph 5; Figure 6b\n  quote: Other sensory-related areas (OB, olfactory bulb; RSPagl, retrosplenial area, lateral\n    agranular part; AUDs, secondary auditory areas; VISp, primary visual area) showed activity\n    traces that shared time courses closely matching the pupil dilation.\n  criterion: Readings for sessions, pulls and hemisphere as in fig6b-motor-somatosensory-after-\n    reward, over -1 to 3 s around lever-pull onset. The paper gives no measure of the match; the\n    reading here is the contrast the paragraph draws, motor and somatosensory areas tracking the\n    lever and these areas tracking the pupil. Reproduced when, under one reading, each of the\n    four areas' trial-averaged traces has a higher Pearson correlation with the trial-averaged\n    pupil diameter than with the trial-averaged lever position, and MOp's does not.\n- id: fig6b-variability-decrease\n  statement: Cortical activity varied less across trials after lever-pull onset than before it.\n  source: Technical Validation, paragraph 5; Figure 6b\n  quote: The data also revealed a decrease in activity variability after the lever-pull onset,\n    exemplifying how stereotypic movements like lever-pull constrain cortical activity.\n  criterion: Readings for sessions and pulls as in fig6b-movement-order. Variability is the\n    across-trial s.d. of the corrected dF/F at each time point, averaged over a window, per ROI;\n    before is -1 to 0 s, after is read as (a) 0 to 1 s, (b) 0 to 3 s. The paper names no test;\n    reproduced when, under one reading, the after value is lower than the before value in more\n    than half of the 44 ROIs, with a Wilcoxon signed-rank test over ROIs at p < 0.05 reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001425/10.1101-2025.02.03.631599.yaml; python3 - <<'EOF'
f='claims/001425/10.1101-2025.02.03.631599.yaml'
s=open(f).read()
a=s.index('  inferred: The per-channel'); b=s.index('  criterion: The paper\'s 60 Hz')
s=s[:a]+s[b:]
s=s.replace("as in fig6b-motor-somatosensory-after-\n    reward,","as in\n    fig6b-motor-somatosensory-after-reward,")
open(f,'w').write(s)
EOF
grep -n "—\|rather" $f; python tools/claims_check.py $f paper/10.1101-2025.02.03.631599.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s{4,}[^-].*: " claims/001425/*.yaml | grep -v "^\S*:\s*#" | head; grep -c "criterion:" claims/001425/*.yaml
```

```
57:    value: 25
58:    tolerance: 0
60:    value: 11
61:    tolerance: 0
63:    value: 14
64:    tolerance: 0
79:    value: 364
80:    tolerance: 0
82:    value: 16
83:    tolerance: 0
22
```

**Agent**

I wrote `claims/001425/10.1101-2025.02.03.631599.yaml`. The quote checker passes it with 22 claims, 22 quotes and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, taken from its JATS XML. It has the main text, the Methods, the legends of Figures 1 to 6 and the legends of Supplementary Figures S1 to S4. There is no PDF.

**Code read:** `BraiDyn-BC/bdbc-data-pipeline` at commit ab50b17, plus the submodule commits it pins:
- bdbc-nwb-packager 426f07c
- bdbc-session-explorer 58089f2
- bdbc-nwb-explorer 309c5fb
- bdbc-batch-scripts 763cf80
- ks-pupilfitting dc14b36

The code builds the NWB files, registers the atlas, fits the pupil and runs sanity-check plots. The only detail it settles is the likelihood cut-off of 0.2 for keypoints. None of the analyses behind Figures 3 to 6 or Figure S2b are in it, so every method detail comes from the Methods and legends or is named as open.

**Counts:**
- **Claims:** 22, all quoted.
- **Statistics:** none. The paper reports no tests.
- **Expected values:** 9 claims. Session and subject counts have a tolerance of 0, and the reason is given. The correlations and break statistics use the paper's stated s.d. as the tolerance.
- **Criteria:** all 22 claims have one.

**Details the paper leaves open, and the readings named for each:**
- **Response rate:** valid pulls counted from the trial outcome labels, or from the lever trace crossing 1 mm within 1 s of the tone.
- **"Constant" success rate:** session 15 within 10% of session 1, or no Spearman trend across sessions.
- **Clustering:**
  - Feature: the 15 raw T_pull_final values, or the differences between consecutive sessions.
  - Missing sessions: linear interpolation, carrying the previous value forward, or the next session's starting T_pull plus 100 ms.
- **Cluster A and B comparisons:**
  - "Early" sessions: sessions 1–5, or session 5 alone.
  - "Late" sessions: sessions 11–15, or session 15 alone.
  - "High" T_pull_final: 400 ms, or above the median.
  - "Similar": Mann-Whitney p ≥ 0.05, or group medians within 10%.
- **Training breaks:** mean pooled over all breaks or over mice; how sessions that were not deposited are treated.
- **No signal degradation:** raw blue fluorescence or dF/F s.d. against session number.
- **Sensory maps:**
  - Data: ROI series or pixel maps from the image files.
  - Baseline: none, or the 2 s before the stimulus.
  - The "parietal multimodal area": VISa, VISrl or PTLp.
- **Figure S2b (aberrant transients):**
  - Peak detection: no threshold, or a 0.01 minimum prominence.
  - Which ROIs count as frontal, retrosplenial and visual.
  - K-means features raw or z-scored.
- **Keypoint–lever correlations:**
  - Sampling: 100 Hz or 30 Hz.
  - Likelihood filter applied or not.
  - Trial window: from the trial table, or tone to tone + 1 s + T_pull.
  - Mean taken over sessions or over mice.
  - Sign as computed, or absolute value.
- **Figure 6 example session:** the paper does not say which session it is. The readings are the grand average over sessions, or the majority of sessions. Each Figure 6 claim also has readings for which pulls, which hemisphere and which windows are used.

**Where the criterion uses my own rule:** these are labelled in the file as standard choices or as my reading of the paper's contrast.
- The movement-onset threshold (2 s.d., also shown at 3 s.d.).
- The pupil-versus-lever correlation contrast in the Figure 6 sensory-area claim.

**Missing from the paper:**
- The contents of Tables 1 to 4 are absent; only their legends are in the text. That means no per-animal session counts and no keypoint names.
- Figure values (the Figure 5a–c error percentiles, the Figure 3 curves) could not be read without a PDF.
- The manual annotations used to validate the atlas landmarks and the DeepLabCut keypoints are not described as deposited. Those two claims will likely be blocked.
- The paper does not say plainly whether the sensory-mapping sessions are in the dataset. The three sensory-map claims are blocked if they are not.

## End of run

20 turns, 4 minutes, result: success.
