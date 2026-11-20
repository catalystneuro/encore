# pelot-2020 · claims · run 44663650997

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
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
ls -la paper/; cat claims/pelot-2020.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.601479.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.601479.txt",
 "offset": 134
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/pelot-2020.yaml
```

```
<persisted-output>
Output too large (51.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/868cf8e6-eff7-4243-b5ae-9a6c79d5a94f/tool-results/b7xa85sr6.txt

Preview (first 2KB):
# Claims for Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell & Grill (2020), "Quantified
# Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat", Front.
# Neurosci. 14, 601479, on SPARC:60.
#
# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-18, protocol pilot-16 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the version of record, from Europe PMC (PMC7672126, JATS XML flattened;
# paper/10.3389-fnins.2020.601479.txt), the abstract, Introduction, Materials and Methods,
# Results, figure legends and Discussion. No PDF was supplied, so no figure was read; Figures
# 6, 7 and 9 are known here only from their legends and the Results. Three parts are missing
# from the text read. (1) Eqs. 1 to 4, the perineurium thickness fits, were dropped in the
# flattening; only their R2 values and fascicle counts survive, so the fit coefficients are
# not available as expected values. (2) The supplement (Supplements 1 to 6, Supplementary
# Tables 1 to 6 and Supplementary Figures 13 to 18) is not under paper/; the paper's numbers
# are all in the main text, but Supplement 4 (literature values) and Supplement 6 (age
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/pelot-2020.yaml"
}
```

```
1	# Claims for Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell & Grill (2020), "Quantified
2	# Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat", Front.
3	# Neurosci. 14, 601479, on SPARC:60.
4	#
5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-18, protocol pilot-16 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read: the version of record, from Europe PMC (PMC7672126, JATS XML flattened;
9	# paper/10.3389-fnins.2020.601479.txt), the abstract, Introduction, Materials and Methods,
10	# Results, figure legends and Discussion. No PDF was supplied, so no figure was read; Figures
11	# 6, 7 and 9 are known here only from their legends and the Results. Three parts are missing
12	# from the text read. (1) Eqs. 1 to 4, the perineurium thickness fits, were dropped in the
13	# flattening; only their R2 values and fascicle counts survive, so the fit coefficients are
14	# not available as expected values. (2) The supplement (Supplements 1 to 6, Supplementary
15	# Tables 1 to 6 and Supplementary Figures 13 to 18) is not under paper/; the paper's numbers
16	# are all in the main text, but Supplement 4 (literature values) and Supplement 6 (age
17	# trends) are what two claims rest on. (3) The reference list is empty, so the identifiers of
18	# the SPARC datasets Pelot et al. (2020a to g) are not in the text read.
19	#
20	# Code read: none. The paper links no code repository. The archive's file listing for SPARC:60
[... 913 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/pelot-2020.yaml; ls papers/datasets | head -3; grep -rl "pelot" papers/ docs/ 2>/dev/null | head; ls tools/
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.3389/fnins.2020.601479
title: Quantified Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat
datasets:
- archive: sparc
  id: '60'
  relation: primary
- archive: sparc
  id: '64'
  relation: primary
- archive: sparc
  id: '65'
  relation: primary
- archive: sparc
  id: '89'
  relation: primary
- archive: sparc
  id: '16'
  relation: primary
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/pilot-notes/pelot-2020-01.md | head -60; grep -rn "sparc-60\|sparc-64\|sparc-65\|sparc-89\|sparc-16\b\|sparc-61\|sparc-82" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v transcripts | head -30
```

```
# pelot-2020, Pelot et al. 2020

Seven claims reproduced on the dataset, plus ten that also use the human and
pig datasets; none partially on the dataset alone, plus two with those
inputs; none not reproduced, plus two; and one blocked. Twelve claims on the
human and pig data only, ten reproduced and two partially, and the link claim
`rat-sample-set`, reproduced, are counted apart. The first verification round
agreed with all 35 outcomes as they stood and the second with 34, and with
`fascicles-larger-cervical` only with qualification; the author proposed it
as partially reproduced, so a third round reviewed that one claim and agreed.
The paper compares the morphology of the vagus nerve in human, pig and rat at
the cervical and subdiaphragmatic levels: nerve and fascicle diameters,
fascicle numbers, tissue proportions and perineurium thickness. SPARC:60
(version 5) holds the rat traces of nine left cervical and nine anterior
subdiaphragmatic samples from 10 rats; the human and pig data were taken from
SPARC:65 (version 6), SPARC:64 (version 4) and SPARC:89 (version 1), which
the paper's supplement cites, and the literature values from Supplement 4,
read from Europe PMC (PMC7672126) because the supplement was not under
`paper/`. Reproduced are the rat diameters, rat nerves about ten times
smaller than human and pig nerves, the similar human and pig diameters, the
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3370,3450p papers/manifest.yaml; ls targets 2>/dev/null | head; grep -rln "Quantified morphology" --include=*.yaml --include=*.json . | grep -v transcripts | head
```

```
status: stored
    version: version of record
    source: PDF supplied by a person
    pdf: true
    supplements: 1
  sparc-16:
  - doi: 10.3389/fnins.2020.601479
    status: stored
    version: version of record
    source: Europe PMC PMC7672126 (fullTextXML)
    pdf: false
    supplements: 0
  sparc-206:
  - doi: 10.3389/fnins.2020.619275
    status: stored
    version: version of record
    source: Europe PMC PMC7773906 (fullTextXML)
    pdf: false
    supplements: 0
  sparc-212:
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json
d=json.load(open('targets/sparc.json'))
items = d if isinstance(d,list) else d.get('targets', d.get('datasets', list(d.values())))
for t in items:
    if isinstance(t,dict) and str(t.get('id')) in ['60','64','65','89','16','61','82']:
        print(json.dumps({k:t[k] for k in t if k in ('id','title','description','doi','name','version')}, ensure_ascii=False)[:1500]); print()
"
```

```
{"id": "60", "name": "Quantified morphology of the rat vagus nerve", "doi": "10.26275/lg3c-1kjf", "description": "Binary traces from segmentation of cross sections of cervical and subdiaphragmatic rat vagus nerves stained with Masson's trichrome. Quantified effective nerve diameter, effective fascicle diameter, number of fascicles, and perineurium thickness."}

{"id": "64", "name": "Quantified morphology of the pig vagus nerve", "doi": "10.26275/maq2-eii4", "description": "Binary traces from segmentation of cross sections of cervical and subdiaphragmatic pig vagus nerves stained with Masson's trichrome. Quantified effective nerve diameter, effective fascicle diameter, and number of fascicles."}

{"id": "65", "name": "Quantified morphology of the human vagus nerve with anti-claudin-1", "doi": "10.26275/qgja-q7zd", "description": "Immunohistochemistry micrographs of human vagus nerves labeled with anti-claudin-1. Binary traces from segmentation to quantify effective nerve diameter, effective fascicle diameter, number of fascicles, and perineurium thickness."}

{"id": "89", "name": "Quantified morphology of the pig vagus nerve with anti-fibronectin", "doi": "10.26275/8pc2-rhu2", "description": "Immunofluorescence micrographs of pig vagus nerves labeled with anti-fibronectin. Binary traces from segmentation to quantify effective nerve diameter, effective fascicle diameter, number of fascicles, and perineurium thickness."}

{"id": "16", "name": "Rat vagus nerve stained with Masson's trichrome", "doi": "10.26275/z3ab-7j9y", "description": "Micrographs of cross sections of cervical and abdominal rat vagus nerve stained with Masson's trichrome."}

{"id": "61", "name": "Human vagus nerve stained with Masson's trichrome", "doi": "10.26275/sydt-lkiw", "description": "Micrographs of cross sections of cervical and abdominal human vagus nerve stained with Masson's trichrome."}

{"id": "82", "name": "Pig vagus nerve stained with Masson's trichrome", "doi": "10.26275/pgr9-bk2e", "d
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/fouke-2025.yaml; grep -l "^  datasets:" claims/*.yaml | head -3
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/kim-2022.yaml | grep -n "dataset" ; grep -n -B2 -A3 "^  datasets:" claims/kim-2022.yaml | head -30; grep -n "datasets\|dataset:" tools/claims_check.py | head -20; ls questions/ | grep pelot
```

```
15:# The datasets, from their titles on DANDI.
24:#   These claims are listed under 000489, the YO-PRO-1 uptake dataset of the same preparation and
87-  quote: A train of 5 pulses applied at 1 Hz evoked YP uptake proportionally to the local electric
88-    field strength ( Fig. 2A ), along with a strong dependence on the 2 nd phase amplitude.
89:  datasets:
90-  - "000489"
91-  criterion: YP per ROI along bb' as defined in Methods 2.5, with the field of each ROI from the
92-    model (opening comment). The paper reports no test for this finding. For each of the five
--
104-  quote: note the difference in the vertical scale, which is varied from 1200 a.u. for unipolar
105-    pulses to only 250 a.u. for 75% bipolar pulses
106:  datasets:
107-  - "000489"
108-  criterion: The numbers are axis limits, not measured values, so they bound the data. With YP in
109-    the units of the dataset's fluorescence images, reproduced when the largest mean plus s.e.m.
--
118-  quote: YP uptake increased exponentially with the electric field, and the presence of the 2nd
119-    phase did not change the apparent slope of exponential fits when plotted on a semi-log scale
120:  datasets:
121-  - "000489"
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/pelot-2020.yaml; sed -n 1,80p tools/claims_check.py
```

```
questions:
- claim: no-age-trend
  question: The criterion was written without Supplement 6 and says the claim rests on an assumption
    until Supplement 6 fixes the method. Supplement 6 is one figure (Figure 19, "Nerve morphology
    metrics versus age") with no test. Reading (a) applies an uncorrected Pearson test at p < 0.05
    to each of 26 per-species, per-level metrics. Does the paper's "did not show trends with age",
    judged on plots of 26 metrics, support a test that counts a single uncorrected p < 0.05 as a
    trend, or should the criterion correct for the number of tests (or judge the plots as the paper
    does)?
  passage: 'Discussion, paragraph 5, "Our morphology metrics did not show trends with age for any
    species ( Supplement 6 )"; Supplement 6 (Data_Sheet_1.pdf, page 16), "Figure 19. Nerve morphology
    metrics versus age. Note that all human subjects over 89 years old were plotted as 99 years old."'
  why: Under reading (a) as written, 3 of the 26 Pearson tests have p < 0.05 (all in pigs, 1.3 expected
    by chance) and the claim is not reproduced. With a Holm correction over the 26 tests, or within
    each species, no test is below 0.05 (smallest corrected p 0.499 and 0.154) and the claim would
    be reproduced.
- claim: fascicle-diameter-anova
  question: The criteria of fascicle-diameter-anova, rat-fascicle-diameter and the claims that use their
    model (cervical-fascicle-diameter-species, subdiaphragmatic-fascicle-diameter-comparable,
    fascicles-larger-cervical) take the rat fascicle as the largest fascicle of each sample, as the
[... 103 more lines not kept]
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "checks" .github/workflows/papers.yml tools/agent_run.py 2>/dev/null | head -20; grep -rn "Revised\|Updated:\|Revision" claims/*.yaml | head -5
```

```
.github/workflows/papers.yml:8:# the cheap checks of tools/paper_match.py leave open. Started by hand from the Actions tab or with
.github/workflows/papers.yml:115:      started: ${{ steps.agent.outputs.started || steps.checks.outputs.started }}
.github/workflows/papers.yml:194:      - name: Run the paper match's cheap checks
.github/workflows/papers.yml:195:        id: checks
.github/workflows/papers.yml:198:          # Writes papers/match/<folder>.yaml. When the checks settle every paper there is nothing for the agent.
.github/workflows/papers.yml:199:          need=$(python tools/paper_match.py checks "$FOLDER" paper)
.github/workflows/papers.yml:205:        if: ${{ inputs.account == 'unverified' && steps.checks.outputs.need != 'done' }}
.github/workflows/papers.yml:213:        if: ${{ inputs.account == 'api' && steps.checks.outputs.need != 'done' }}
.github/workflows/papers.yml:220:        if: ${{ !inputs.papers_only && steps.checks.outputs.need != 'done' }}
.github/workflows/papers.yml:253:        if: ${{ !inputs.papers_only && steps.checks.outputs.need != 'done' }}
.github/workflows/papers.yml:288:          # On an account other than the verified one, a run its safety checks flagged (a refusal, or a switch
.github/workflows/papers.yml:301:        if: always() && (steps.agent.outputs.started == 'true' || steps.checks.outputs.started == 'true') && steps.flag.outputs.flagged != 'true'
.github/workflows/papers.yml:313:          # No transcript when the paper match's checks settled every paper and no agent ran.
tools/agent_run.py:140:    write the record and run the entry's checks (docs/protocol.md, "Author", "Time")."""
tools/agent_run.py:152:                   f"computation stopped it, with how far it got), write the record, and run the entry's checks.\n")
claims/lee-2023.yaml:26:# Revised_subclass_label, Virus, Genes_Detected, marker_sum_norm_label and nwb_id), the IPFX
claims/lee-2023.yaml:68:# above. Subclass is Revised_subclass_label (SST FRZB in PVALB). Test
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 75,100p claims/markowitz-2023.yaml; grep -n "^checks:" -A6 claims/markowitz-2023.yaml | head -12
```

```
#   the code drops it (code session numbers 3 and 4, commented "remove post-stim sessions").
# - Shuffle test (Methods, Statistics). An observed correlation against 1,000 shuffled ones; when it
#   exceeds all of them P is given as < 0.001. Holm-Bonferroni correction "where appropriate".
# - Opto-DA sessions. Code session numbers -1 and 0 are baseline, 1 and 2 stimulation, 3 and 4 post
#   (behavior_01, cell 23). Catch trials are online target detections without light.
#
# Revision of 2026-11-19. The earlier file was written after the data check had been seen and took
# some choices from the data (group and site names in the files, a 0.17-s stimulation latency,
# label ranges); these are removed and every method below is from the paper or its code. Criteria
# that misread the code (100 shuffles in Fig. 1e, the measure behind Fig. 1h, a 1,800-s count window
# in Fig. 3e) are corrected, criteria are added to the claims that had none, and claims are added
# for further panels with numbers in the text.
schema_version: 2
paper: doi:10.1038/s41586-022-05611-2
claims:
- id: ed2a-syllable-repertoire
  statement: MoSeq identifies 37 commonly used syllables, with median duration 400 ms (mean 566 ms,
    s.d. 636 ms).
  source: Results, Relating DLS dopamine to spontaneous behavior, paragraph 1; Extended Data Figure 2a
  quote: MoSeq identified 37 commonly used behavioural syllables, whose median duration was 400 ± 636
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import re
src=open('claims/pelot-2020.yaml').read()
# split header / body
i=src.index('schema_version: 2')
j=src.index('checks:\n')
open('/tmp/claude/body.yaml','w').write(src[i:j]) if False else None
import os
d=os.environ.get('TMPDIR','/tmp/claude')
os.makedirs(d,exist_ok=True)
open(d+'/body.yaml','w').write(src[i:j])
print(d, len(src[i:j]))
EOF
```

```
/tmp/claude-1001 43531
```

**Agent calls Write**

```json
{
 "file_path": "claims/pelot-2020.yaml",
 "content": "# Claims for Pelot, Goldhagen, Cariello, Musselman, Clissold, Ezzell & Grill (2020), \"Quantified\n# Morphology of the Cervical and Subdiaphragmatic Vagus Nerves of Human, Pig, and Rat\", Front.\n# Neurosci. 14, 601479, on SPARC:60, SPARC:64, SPARC:65, SPARC:89, SPARC:16, SPARC:61 and\n# SPARC:82.\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-20, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n# It revises the file of 2026-11-18 (protocol pilot-16), which was read for SPARC:60 alone.\n#\n# Text read: the version of record, from Europe PMC (PMC7672126, JATS XML flattened;\n# paper/10.3389-fnins.2020.601479.txt), the abstract, Introduction, Materials and Methods,\n# Results, figure legends and Discussion. No PDF was supplied, so no figure was read; Figures\n# 6, 7 and 9 are known here only from their legends and the Results. Three parts are missing\n# from the text read. (1) Eqs. 1 to 4, the perineurium thickness fits, were dropped in the\n# flattening; only their R2 values and fascicle counts survive, so the fit form and\n# coefficients are open. (2) The supplement (Supplements 1 to 6, Supplementary Tables 1 to 6\n# and Supplementary Figures 13 to 18) is not under paper/. The paper's own numbers are all in\n# the main text; Supplement 4 (literature values) and Supplement 6 (age trends) are what three\n# claims rest on. (3) The reference list is empty, so the dataset identifiers of Pelot et al.\n# (2020a to g) are not in the text read; the mapping below is read from the dataset titles\n# and the legends that cite each one.\n#\n# Code read: none. The paper links no code repository. The Methods name the tools:\n# NIS-Elements Ar v5.02.01 for segmentation, MATLAB R2018b (bwboundaries, polyarea, fit with\n# linear least squares) for morphometry and fits, JMP Pro 14.3.0 for the mixed model ANOVAs\n# and Tukey's HSD. Where a criterion takes a JMP default, it says so as the software's choice.\n#\n# The datasets (titles and descriptions on the SPARC Portal), with the citation each most\n# likely is.\n# - sparc-60, \"Quantified morphology of the rat vagus nerve\": binary traces of the MT cross\n#   sections of cervical and subdiaphragmatic rat VNs, with nerve and fascicle diameters,\n#   fascicle numbers and perineurium thickness. Pelot et al. (2020g), cited with the rat\n#   segmentations (Figures 5, 6 and 9 legends).\n# - sparc-16, \"Rat vagus nerve stained with Masson's trichrome\": micrographs of cervical and\n#   abdominal rat VN. Pelot et al. (2020e), cited with the rat micrographs (Figure 5 legend;\n#   Results, paragraph 7).\n# - sparc-65, \"Quantified morphology of the human vagus nerve with anti-claudin-1\": IHC\n#   micrographs and traces. Pelot et al. (2020a) (Figure 2 legend).\n# - sparc-61, \"Human vagus nerve stained with Masson's trichrome\": micrographs. By elimination,\n#   Pelot et al. (2020c), which no legend cites; Supplement 3 shows these sections.\n# - sparc-64, \"Quantified morphology of the pig vagus nerve\": traces of the MT cross sections\n#   (nerve and inner perineurium, no perineurium). Pelot et al. (2020f) (Figures 3 and 6).\n# - sparc-82, \"Pig vagus nerve stained with Masson's trichrome\": micrographs. Pelot et al.\n#   (2020d) (Figure 3 legend).\n# - sparc-89, \"Quantified morphology of the pig vagus nerve with anti-fibronectin\": IF\n#   micrographs and traces with perineurium. Pelot et al. (2020b) (Figures 4, 6 and 9).\n# Every claim lists under `datasets` those it rests on. Claims needing the literature values of\n# Supplement 4 are `with_inputs`; the Sunderland and Bradley (1952) reanalysis rests on none of\n# the datasets and is `elsewhere`.\n#\n# Data the paper used (Materials and Methods).\n# - Collected. Human: 37 cervical and 32 subdiaphragmatic samples from 30 embalmed cadavers\n#   (15M/15F, 54 to 90+ years, 63 +/- 12 kg, 168 +/- 10 cm). Pig: 21 cervical and 24\n#   subdiaphragmatic samples from 12 Yorkshire pigs (3M/9F, 10.5 to 15 weeks, 33 +/- 8 kg),\n#   fresh. Rat: 18 cervical and 9 subdiaphragmatic samples from 10 Sprague-Dawley rats (5M/5F,\n#   75 to 268 days, 381 +/- 118 g), perfused with PBS and 4% paraformaldehyde; each rat\n#   subdiaphragmatic sample is the esophagus with both trunks; R18's was unusual and R26 was\n#   collected in its place. All post-fixed 2 to 8 days in 4% paraformaldehyde, paraffin, 5 um\n#   sections, MT stain for all (Supplement 3). Subject and sample metadata are in Supplement 1\n#   and Supplementary Tables 4 to 6 (not read).\n# - Analysed. Nine left cervical and nine anterior subdiaphragmatic samples per species. Human,\n#   anti-claudin-1 IHC, 4F/5M at each level, chosen at random within sex after excluding known\n#   neuropathies. Pig, MT, all left cervical (6F/3M), all male anterior subdiaphragmatic (3M)\n#   and six of nine female ones at random (6F); also four cervical (2F/2M) and four\n#   subdiaphragmatic (2F/2M) pig samples with anti-fibronectin IF, chosen for contrast. Rat,\n#   MT, all left cervical (4F/5M) and anterior subdiaphragmatic (4F/5M) samples.\n# - Segmentation. Rat by hand: cervical, the vagus is the largest nerve in the carotid sheath;\n#   subdiaphragmatic, the largest fascicle on the anterior esophagus, plus smaller fascicles\n#   within about twice its diameter from its edge and a nerve boundary at the dense to loose\n#   connective tissue transition; all statistics use the largest fascicle only, its outer\n#   perineurium boundary as the nerve boundary. Human IHC, pig MT and pig IF by NIS-Elements\n#   General Analysis, then hand edits; pig MT gives the inner perineurium boundary only.\n# - Measures (Methods, Imaging and Image Analysis, last paragraph). Boundaries by bwboundaries;\n#   area by polyarea; effective diameter, that of the circle of equal area, for nerve and\n#   fascicles; fascicle diameter from the inner perineurium boundary; perineurium thickness,\n#   half the difference of the effective diameters of the outer and inner perineurium\n#   boundaries. Epineurium area is nerve area minus endoneurium and perineurium areas (Figure 7\n#   legend). Fascicle counts count inner perineurium traces (Figure 6 legend). Perineurium fits\n#   leave out peanut fascicles (Figure 9 legend).\n# - Statistics (Methods, Statistics and Data Analyses). SDs throughout. Mixed model ANOVAs in\n#   JMP with fixed effects species and level and a random effect of subject; for fascicle\n#   diameter, log10 of the data and a further random effect of sample; Tukey's HSD post hoc.\n#   Number of fascicles excludes rats. Perineurium fits by MATLAB fit, linear least squares.\n#\n# Inconsistencies in the paper, noted for the author. The Discussion gives the rat ratio of\n# mean subdiaphragmatic to cervical nerve diameter as 0.68, but the Results' means (0.135 and\n# 0.260 mm) give 0.52; the human (0.89 against 0.87) and pig (0.73 against 0.75) ratios agree\n# with their means. The Discussion gives the rat weight as 381 +/- 38 g (SEM), the Methods 381\n# +/- 118 g (SD); these agree for n = 10. Twelve pigs, with one cervical side missing in two,\n# would give 22 cervical samples; the Methods say 21.\n#\n# Details the paper leaves open, each named in the criteria with the readings it allows. The\n# JMP mixed model settings: REML is JMP's method for random effects and Kenward-Roger its\n# denominator degrees of freedom; whether variance components are bounded at zero is read both\n# ways (JMP's Fit Model default is unbounded). Whether Tukey contrasts with one printed p for\n# both levels are main-effect or per-level contrasts. The form of the perineurium fits (Eqs. 1\n# to 3 missing) and which rat fascicles enter them. How \"for a given fascicle diameter\",\n# \"approximately ten times\", \"clearest\", \"more consistent\", \"oblong\", \"many\" and \"similar\" are\n# measured. Which rat subdiaphragmatic tissue enters the Discussion's ratios. The test, if any,\n# behind \"did not suggest a difference\" between levels and behind the absence of age trends.\n#\n# Changes from the file of 2026-11-18. The paper is now tested on seven datasets, so claims on\n# human and pig data rest on SPARC:64, 65 and 89 (`data: dataset` with `datasets`), no longer\n# `elsewhere` or `with_inputs`; the literature comparisons stay `with_inputs` (Supplement 4)\n# and the Sunderland reanalysis `elsewhere`. Link claims are added for the human, pig MT and\n# pig IF sample sets and for the three MT micrograph collections (SPARC:16, 61, 82). Claims\n# are added for the shape and epineurium of pig and human nerves, the pig cervical fascicles\n# with cell bodies, and the lower pig IF endoneurial proportion. The JMP settings are named as\n# readings in the mixed model criteria. rat-carotid-sheath-bundles no longer contradicts\n# itself: it is tested on the cervical micrographs of SPARC:16, with the counting rule named\n# as open. The check of 2026-11-18 applied to the earlier file and is not carried over; its\n# changes are kept.\nschema_version: 2\npaper: doi:10.3389/fnins.2020.601479\nclaims:\n- id: rat-sample-set\n  kind: link\n  statement: The rat traces hold the rat samples the paper analysed, segmentations of nine left\n    cervical and nine anterior subdiaphragmatic vagus nerve samples from Sprague-Dawley rats, 4F\n    and 5M at each level, from 10 rats (5M/5F).\n  source: Materials and Methods, Sample Collections, paragraph 1, and Imaging and Image Analysis,\n    paragraph 2\n  quote: We analyzed all left cervical (4F/5M) and anterior subdiaphragmatic (4F/5M) rat VN\n    samples.\n  datasets:\n  - sparc-60\n  criterion: Reproduced when the dataset holds segmentations of nine cervical and nine\n    subdiaphragmatic rat samples whose subjects are 4F and 5M at each level, drawn from no more\n    than 10 rats, with subject metadata consistent with the Methods (Sprague-Dawley, 75 to 268\n    days, 381 +/- 118 g over the 10 rats). Partially reproduced when the sample counts match\n    but the metadata differ; not reproduced when the sample counts differ. Extra samples (the\n    right cervical and posterior samples, R18) are reported, not counted against the link.\n- id: human-sample-set\n  kind: link\n  statement: The human anti-claudin-1 data hold the human samples the paper analysed, nine left\n    cervical and nine anterior subdiaphragmatic samples, 4F and 5M at each level.\n  source: Materials and Methods, Imaging and Image Analysis, paragraph 2\n  quote: After excluding human subjects with known neuropathies ( Supplementary Table 1 ), within\n    each sex, we randomly selected left cervical (4F/5M) and anterior subdiaphragmatic (4F/5M)\n    human samples for further analysis.\n  datasets:\n  - sparc-65\n  criterion: Reproduced when the dataset holds anti-claudin-1 micrographs and segmentations\n    (nerve, outer and inner perineurium) of nine cervical and nine subdiaphragmatic human\n    samples, 4F and 5M at each level, including the samples Figure 2 names (C47-2, C54-3,\n    C55-3, C56-3, C63-1, and C57-3 of Figure 8). Partially reproduced when the counts match but\n    the sexes or named samples do not; not reproduced when the counts differ.\n- id: pig-mt-sample-set\n  kind: link\n  statement: The pig MT traces hold the pig samples the paper analysed, nine left cervical\n    (6F/3M) and nine anterior subdiaphragmatic (6F/3M) samples, segmented for nerve and inner\n    perineurium boundaries.\n  source: Materials and Methods, Imaging and Image Analysis, paragraphs 2 and 5\n  quote: We analyzed all left cervical VN samples from pigs (6F/3M), as well as all anterior\n    subdiaphragmatic samples from male pigs (3M); we randomly chose six of the nine anterior\n    subdiaphragmatic samples from female pigs (6F).\n  datasets:\n  - sparc-64\n  criterion: Reproduced when the dataset holds segmentations of nine cervical and nine\n    subdiaphragmatic pig samples, 6F and 3M at each level, from no more than 12 pigs, including\n    P11-1 and P13-1 (Figure 3 legend). Partially reproduced when the counts match but the sexes\n    do not; not reproduced when the counts differ.\n- id: pig-if-sample-set\n  kind: link\n  statement: The pig anti-fibronectin data hold four cervical (2F/2M) and four subdiaphragmatic\n    (2F/2M) pig samples segmented for nerve, outer and inner perineurium boundaries.\n  source: Materials and Methods, Imaging and Image Analysis, paragraph 2\n  quote: We also quantified the morphology for four cervical (2F/2M) and four subdiaphragmatic\n    (2F/2M) pig samples using anti-fibronectin IF\n  datasets:\n  - sparc-89\n  criterion: Reproduced when the dataset holds IF micrographs and segmentations of four\n    cervical and four subdiaphragmatic pig samples, 2F and 2M at each level, each among the 18\n    pig MT samples (Methods; P12-1 is named in Figure 8). Partially reproduced when the counts\n    match but the sexes or the overlap with the MT samples do not.\n- id: mt-micrograph-collections\n  kind: link\n  statement: The MT micrograph collections hold cross sections of the samples collected, 37\n    cervical and 32 subdiaphragmatic human samples from 30 subjects, 21 cervical and 24\n    subdiaphragmatic pig samples from 12 pigs, and 18 cervical and 9 subdiaphragmatic rat\n    samples from 10 rats.\n  source: Materials and Methods, Sample Collections, paragraph 1; Results, paragraph 1\n  quote: we collected 37 cervical and 32 subdiaphragmatic human samples ( n = 30 subjects, 15M/15F\n    ... 21 cervical and 24 subdiaphragmatic pig samples ( n = 12 pigs, 3M/9F ... and 18 cervical\n    and 9 subdiaphragmatic rat samples ( n = 10 rats, 5M/5F\n  datasets:\n  - sparc-61\n  - sparc-82\n  - sparc-16\n  criterion: Per species, the number of MT micrographs (one per sample, Methods, \"we selected\n    the best of the stained sections\") by level and the number of subjects. Reproduced when\n    every count matches; partially reproduced when the counts of one species differ (the pig\n    cervical count is 21 in the Methods but 22 by its own description of missing sides, so 21\n    and 22 both match). Each collection includes the analysed samples of its species.\n- id: nerve-diameter-anova\n  statement: Effective nerve diameter differs across species and across nerve levels, with no\n    detected interaction of species and level.\n  source: Results, paragraph 3\n  quote: The nerve diameter differed across species ( p < 0.0001; F = 577.1) and nerve levels ( p\n    = 0.0030; F = 11.01), but we did not detect an interaction of species and level ( p = 0.1085;\n    F = 2.445).\n  statistics:\n  - about: species\n    test: mixed model ANOVA\n    statistic: F = 577.1\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 cervical and 9 subdiaphragmatic samples per species (human, pig MT, rat)\n  - about: nerve level\n    test: mixed model ANOVA\n    statistic: F = 11.01\n    p: 0.003\n  - about: species by level interaction\n    test: mixed model ANOVA\n    statistic: F = 2.445\n    p: 0.1085\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - rat-nerve-diameter\n  criterion: As in the Methods (Statistics and Data Analyses), a mixed model ANOVA of effective\n    nerve diameter with fixed effects species, level and their interaction (the Results report\n    the interaction) and a random effect of subject, on the 54 samples (rat sparc-60, human\n    sparc-65, pig MT sparc-64). The JMP settings the paper does not state are taken from JMP,\n    the software it names, REML with Kenward-Roger degrees of freedom; whether the variance\n    component is bounded at zero is open and could change the interaction test, so both\n    readings are run, (a) unbounded (JMP Fit Model default), (b) bounded at zero. Reproduced\n    when species and level have p < 0.05 and the interaction has p >= 0.05 (the absence judged\n    on this test) under a reading; partially reproduced when species and level hold but the\n    interaction is significant. The F values are reported against the paper's.\n- id: human-pig-nerve-diameter-similar\n  statement: Human and pig vagus nerves have similar effective diameters, 1.9 +/- 0.5 against\n    2.2 +/- 0.2 mm cervically and 1.7 +/- 0.3 against 1.6 +/- 0.2 mm subdiaphragmatically, with\n    no significant difference by Tukey's test.\n  source: Results, paragraph 3\n  quote: The human and pig nerves had similar effective diameters (1.9 ± 0.5 vs. 2.2 ± 0.2 mm at\n    the cervical level and 1.7 ± 0.3 vs. 1.6 ± 0.2 mm at the subdiaphragmatic level; p = 0.1830,\n    Tukey's test)\n  statistics:\n  - test: Tukey's test\n    p: 0.183\n    n: 9 human and 9 pig samples per level\n  datasets:\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - nerve-diameter-anova\n  expected:\n  - quantity: human cervical effective nerve diameter, mean\n    value: 1.9\n    tolerance: 0.5\n    unit: mm\n  - quantity: pig cervical effective nerve diameter, mean\n    value: 2.2\n    tolerance: 0.2\n    unit: mm\n  - quantity: human subdiaphragmatic effective nerve diameter, mean\n    value: 1.7\n    tolerance: 0.3\n    unit: mm\n  - quantity: pig subdiaphragmatic effective nerve diameter, mean\n    value: 1.6\n    tolerance: 0.2\n    unit: mm\n  criterion: A claim of absence, judged on the paper's test, Tukey's HSD after the model of\n    nerve-diameter-anova. Human nerve diameter from the inner nerve trace where Figure 2 shows\n    two (C47-2, C54-3, C55-3, C63-1; Figure 2 legend). Reproduced when the means are within the\n    stated SDs and the human against pig comparison has p >= 0.05. The paper prints one p for\n    both levels and the model has no detected interaction, so the test is read as the species\n    main-effect contrast human against pig; human against pig at each level in the species by\n    level Tukey is shown as a variant. The effect size is reported either way.\n- id: rat-nerve-diameter\n  statement: Rat vagus nerves have effective diameters of 0.260 +/- 0.025 mm at the cervical\n    level and 0.135 +/- 0.015 mm at the subdiaphragmatic level.\n  source: Results, paragraph 3\n  quote: the rat nerves were approximately ten times smaller (0.260 ± 0.025 mm at the cervical\n    level and 0.135 ± 0.015 mm at the subdiaphragmatic level\n  datasets:\n  - sparc-60\n  expected:\n  - quantity: rat cervical effective nerve diameter, mean over 9 samples\n    value: 0.26\n    tolerance: 0.025\n    unit: mm\n  - quantity: rat cervical effective nerve diameter, SD\n    value: 0.025\n    tolerance: 0.0025\n    unit: mm\n  - quantity: rat subdiaphragmatic effective nerve diameter, mean over 9 samples\n    value: 0.135\n    tolerance: 0.015\n    unit: mm\n  - quantity: rat subdiaphragmatic effective nerve diameter, SD\n    value: 0.015\n    tolerance: 0.0015\n    unit: mm\n  criterion: Effective diameter is the diameter of the circle of the area within the traced\n    boundary (bwboundaries and polyarea, Methods). Cervical, the nerve boundary of the vagus;\n    subdiaphragmatic, the outer perineurium boundary of the largest fascicle, as the Methods fix\n    for all statistics (\"largest\" read as the largest outer perineurium area, the boundary used;\n    the inner area is shown if it picks another fascicle). Mean tolerances are the paper's SDs;\n    SD tolerances are 10%. Reproduced when both means are within tolerance; the SDs are judged\n    too (partially reproduced when only the means hold). The connective tissue boundary of the\n    three multifascicular samples is shown as a variant.\n- id: rat-ten-times-smaller\n  statement: Rat vagus nerves are about ten times smaller in diameter than human and pig nerves,\n    significantly smaller than each of the two larger species.\n  source: Results, paragraph 3; Discussion, paragraph 3\n  quote: while the rat nerves were approximately ten times smaller (0.260 ± 0.025 mm at the\n    cervical level and 0.135 ± 0.015 mm at the subdiaphragmatic level; p < 0.0001, for both\n    comparisons of rat to larger species)\n  statistics:\n  - test: Tukey's test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 samples per species and level\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - nerve-diameter-anova\n  criterion: Tukey's HSD after the model of nerve-diameter-anova. The paper's \"both comparisons\n    of rat to larger species\" are rat against human and rat against pig, one p for both\n    levels, read as the species main-effect contrasts; the same contrasts at each level are\n    shown as a variant. The paper gives no bound for \"approximately ten times\"; its own means\n    give larger-species over rat ratios of 7.3 to 12.6, and the claim reads it as a ratio\n    between 5 and 20 at each level (a choice of this file, on which that part rests).\n    Reproduced when rat against human and rat against pig both have p < 0.0001 with rat\n    smaller and the ratios fall in that range; partially reproduced when p < 0.05 but not\n    below 0.0001.\n- id: nerve-cervical-larger\n  statement: Cervical vagus nerves are larger than subdiaphragmatic nerves, a trend clearest in\n    pigs and rats.\n  source: Results, paragraph 3\n  quote: The cervical nerves were significantly larger than the subdiaphragmatic nerves;\n    qualitatively, this trend was clearest for the pig and rat nerves.\n  statistics:\n  - test: mixed model ANOVA, level effect\n    statistic: F = 11.01\n    p: 0.003\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - nerve-diameter-anova\n  criterion: Reproduced when the level effect of nerve-diameter-anova has p < 0.05 with the\n    cervical least squares mean larger, and the pig and rat level differences are clearer than\n    the human one. The paper judges \"clearest\" qualitatively and names no measure; readings\n    (a) the relative difference of means (cervical minus subdiaphragmatic over cervical) is\n    larger for pig and for rat than for human; (b) the per-species difference of means over\n    the pooled SD is larger for pig and for rat than for human. That part holds under either\n    reading and rests on an assumption. The rat part alone is reported apart.\n- id: fascicle-number-human-pig\n  statement: Pig vagus nerves have almost ten times more fascicles than human nerves (47 +/- 10\n    and 38 +/- 7 against 6.7 +/- 4.5 and 4.9 +/- 4.0 at the cervical and subdiaphragmatic\n    levels), the number differs by species and level with no detected interaction, and there\n    are more fascicles cervically.\n  source: Results, paragraph 4\n  quote: The number of fascicles differed across species ( p < 0.0001; F = 213.8) and nerve levels\n    ( p = 0.0300; F = 5.486), but we did not detect an interaction of species and level ( p =\n    0.1322; F = 2.481) ... The pig nerves had almost ten times more fascicles than the human nerves\n    (47 ± 10 at the cervical level and 38 ± 7 at the subdiaphragmatic level for pigs vs. 6.7 ±\n    4.5 and 4.9 ± 4.0 for humans), and there were more fascicles at the cervical level.\n  statistics:\n  - about: species\n    test: mixed model ANOVA\n    statistic: F = 213.8\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 human and 9 pig samples per level\n  - about: nerve level\n    test: mixed model ANOVA\n    statistic: F = 5.486\n    p: 0.03\n  - about: species by level interaction\n    test: mixed model ANOVA\n    statistic: F = 2.481\n    p: 0.1322\n  datasets:\n  - sparc-65\n  - sparc-64\n  expected:\n  - quantity: pig cervical number of fascicles, mean\n    value: 47\n    tolerance: 10\n  - quantity: pig subdiaphragmatic number of fascicles, mean\n    value: 38\n    tolerance: 7\n  - quantity: human cervical number of fascicles, mean\n    value: 6.7\n    tolerance: 4.5\n  - quantity: human subdiaphragmatic number of fascicles, mean\n    value: 4.9\n    tolerance: 4.0\n  criterion: Fascicles counted as inner perineurium traces (Figure 6 legend), human from\n    sparc-65, pig from the MT traces of sparc-64. Mixed model ANOVA as in the Methods, fixed\n    species, level and interaction, random subject, rats excluded, JMP settings and the two\n    variance readings as in nerve-diameter-anova. Reproduced when the means are within the\n    stated SDs, species and level have p < 0.05 and the interaction p >= 0.05 under a reading.\n- id: rat-subdiaphragmatic-multifascicular\n  statement: Rat vagus nerves are generally monofascicular; three of the nine rat\n    subdiaphragmatic samples (R16-1, R22-1 and R23-1) are multifascicular.\n  source: Figure 6 legend; Results, paragraph 6; Discussion, paragraph 9\n  quote: The three rat samples with asterisks are multifascicular\n  datasets:\n  - sparc-60\n  criterion: Count, per rat sample, the fascicles segmented (inner perineurium traces).\n    Reproduced when all nine cervical samples have one fascicle and exactly three\n    subdiaphragmatic samples (R16-1, R22-1, R23-1) have more than one; partially reproduced\n    when three subdiaphragmatic samples are multifascicular but not those three. The counts in\n    those samples are reported (Figure 6, row 3, was not read).\n- id: rat-multifascicular-proportions\n  statement: Counting all segmented fascicles and the surrounding tissue, the epineurium,\n    perineurium and endoneurium proportions are 58.0, 3.8 and 38.2% for R16-1, 55.1, 4.2 and\n    40.7% for R23-1, and 63.4, 3.6 and 33.0% for R22-1.\n  source: Figure 6 legend\n  quote: If the multiple fascicles and surrounding tissue were included, the proportions of\n    epineurium, perineurium, and endoneurium would be ... 58.0, 3.8, and 38.2% for R16-1; 55.1,\n    4.2, and 40.7% for R23-1; 63.4, 3.6, 33.0% for R22-1.\n  datasets:\n  - sparc-60\n  depends_on:\n  - rat-subdiaphragmatic-multifascicular\n  expected:\n  - quantity: R16-1 epineurium proportion\n    value: 58.0\n    tolerance: 5.8\n    unit: \"%\"\n  - quantity: R16-1 perineurium proportion\n    value: 3.8\n    tolerance: 0.38\n    unit: \"%\"\n  - quantity: R16-1 endoneurium proportion\n    value: 38.2\n    tolerance: 3.82\n    unit: \"%\"\n  - quantity: R23-1 epineurium proportion\n    value: 55.1\n    tolerance: 5.51\n    unit: \"%\"\n  - quantity: R23-1 perineurium proportion\n    value: 4.2\n    tolerance: 0.42\n    unit: \"%\"\n  - quantity: R23-1 endoneurium proportion\n    value: 40.7\n    tolerance: 4.07\n    unit: \"%\"\n  - quantity: R22-1 epineurium proportion\n    value: 63.4\n    tolerance: 6.34\n    unit: \"%\"\n  - quantity: R22-1 perineurium proportion\n    value: 3.6\n    tolerance: 0.36\n    unit: \"%\"\n  - quantity: R22-1 endoneurium proportion\n    value: 33.0\n    tolerance: 3.3\n    unit: \"%\"\n  criterion: Areas by polyarea within the traces (Methods); endoneurium is the area within all\n    inner perineurium traces, perineurium the area between outer and inner traces, epineurium\n    the nerve (connective tissue boundary) area minus the two (Figure 7 legend). Reproduced when\n    all nine values are within 10%; partially reproduced for six to eight.\n- id: fascicle-diameter-anova\n  statement: Effective fascicle diameter differs across species and nerve levels, with a\n    significant species by level interaction.\n  source: Results, paragraph 5\n  quote: The fascicle diameters differed across species ( p = 0.0015; F = 8.989) and nerve levels\n    ( p < 0.0001; F = 51.88), and there was an interaction of species and level ( p = 0.0121; F =\n    5.273).\n  statistics:\n  - about: species\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 8.989\n    p: 0.0015\n  - about: nerve level\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 51.88\n    p: 0.0001\n    p_relation: \"<\"\n  - about: species by level interaction\n    test: mixed model ANOVA on log10 fascicle diameter\n    statistic: F = 5.273\n    p: 0.0121\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - rat-fascicle-diameter\n  criterion: As in the Methods, log10 of every fascicle's effective diameter (inner perineurium\n    boundary, every inner trace including peanut bundles, Figure 6 legend), fixed species,\n    level and interaction, random effects of subject and of sample; rats contribute their\n    largest fascicle per sample; human sparc-65, pig MT sparc-64. JMP settings and the two\n    variance readings as in nerve-diameter-anova. Reproduced when all three effects have p <\n    0.05 under a reading; partially reproduced when two do.\n- id: rat-fascicle-diameter\n  statement: The largest rat fascicle has an effective diameter of 0.249 +/- 0.024 mm at the\n    cervical level and 0.121 +/- 0.032 mm at the subdiaphragmatic level.\n  source: Results, paragraph 5\n  quote: while rat fascicles (0.249 ± 0.024 mm) were comparable sizes to both human ( p = 0.7270)\n    and pig ( p = 0.1707) fascicles ... 0.121 ± 0.032 mm\n  datasets:\n  - sparc-60\n  expected:\n  - quantity: rat cervical effective fascicle diameter, mean over 9 samples\n    value: 0.249\n    tolerance: 0.024\n    unit: mm\n  - quantity: rat subdiaphragmatic effective fascicle diameter, mean over 9 samples\n    value: 0.121\n    tolerance: 0.032\n    unit: mm\n  criterion: The effective diameter of the inner perineurium boundary of the largest fascicle\n    in each sample (Methods; largest read as in rat-nerve-diameter). Tolerances are the paper's\n    SDs. Reproduced when both means are within tolerance. The arithmetic mean is taken, as the\n    Results report mean +/- SD; the geometric mean (the analysis is on log10) is shown as a\n    variant.\n- id: cervical-fascicle-diameter-species\n  statement: At the cervical level human fascicles (0.355 +/- 0.226 mm) are larger than pig\n    fascicles (0.155 +/- 0.058 mm), while rat fascicles are comparable to both.\n  source: Results, paragraph 5\n  quote: Comparing across species at the cervical level, the human fascicles (0.355 ± 0.226 mm)\n    were larger than the pig fascicles (0.155 ± 0.058 mm; p = 0.0002), while rat fascicles (0.249\n    ± 0.024 mm) were comparable sizes to both human ( p = 0.7270) and pig ( p = 0.1707)\n    fascicles.\n  statistics:\n  - about: human against pig, cervical\n    test: Tukey's HSD\n    p: 0.0002\n  - about: rat against human, cervical\n    test: Tukey's HSD\n    p: 0.727\n  - about: rat against pig, cervical\n    test: Tukey's HSD\n    p: 0.1707\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - fascicle-diameter-anova\n  expected:\n  - quantity: human cervical effective fascicle diameter, mean over fascicles\n    value: 0.355\n    tolerance: 0.226\n    unit: mm\n  - quantity: pig cervical effective fascicle diameter, mean over fascicles\n    value: 0.155\n    tolerance: 0.058\n    unit: mm\n  criterion: Tukey's HSD on the species by level groups of the model in fascicle-diameter-anova.\n    Reproduced when human against pig has p < 0.05 with human larger and the two rat\n    comparisons have p >= 0.05 (absence judged on this test), with the means within the stated\n    SDs. The paper does not say how the human and pig means are formed; readings (a) the mean\n    over all fascicles of the nine samples, (b) the mean of per-sample means (the blue ticks of\n    Figure 6). The means hold under either.\n- id: subdiaphragmatic-fascicle-diameter-comparable\n  statement: At the subdiaphragmatic level fascicle diameters are comparable across species\n    (human 0.163 +/- 0.146, pig 0.110 +/- 0.044, rat 0.121 +/- 0.032 mm), although human\n    fascicles trend larger than pig fascicles.\n  source: Results, paragraph 5\n  quote: At the subdiaphragmatic level, the fascicles diameters were comparable across all species\n    ... although the human fascicles trended larger than the pig fascicles.\n  statistics:\n  - about: human against pig, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.3049\n  - about: human against rat, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.896\n  - about: pig against rat, subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.9947\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - fascicle-diameter-anova\n  expected:\n  - quantity: human subdiaphragmatic effective fascicle diameter, mean over fascicles\n    value: 0.163\n    tolerance: 0.146\n    unit: mm\n  - quantity: pig subdiaphragmatic effective fascicle diameter, mean over fascicles\n    value: 0.11\n    tolerance: 0.044\n    unit: mm\n  criterion: A claim of absence, judged on the paper's test, Tukey's HSD on the species by level\n    groups of the model in fascicle-diameter-anova. Reproduced when none of the three\n    subdiaphragmatic species pairs has p < 0.05 and the means are within the stated SDs (means\n    read as in cervical-fascicle-diameter-species); not reproduced when any pair differs. The\n    trend is the human mean above the pig mean. Effect sizes are reported either way.\n- id: fascicles-larger-cervical\n  statement: All three species have larger fascicles at the cervical than at the\n    subdiaphragmatic level.\n  source: Results, paragraph 5\n  quote: All species had larger fascicles at the cervical level ( p < 0.0001 for humans; p =\n    0.0009 for pigs; p = 0.0234 for rats).\n  statistics:\n  - about: humans, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0001\n    p_relation: \"<\"\n  - about: pigs, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0009\n  - about: rats, cervical against subdiaphragmatic\n    test: Tukey's HSD\n    p: 0.0234\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - fascicle-diameter-anova\n  criterion: Tukey's HSD on the species by level groups of the model in fascicle-diameter-anova.\n    Reproduced when each species has cervical larger with p < 0.05; partially reproduced for\n    two species. The p values are reported against the paper's.\n- id: rat-diameter-like-fascicle\n  statement: The monofascicular rat nerves have diameters close to that of a single human or pig\n    fascicle.\n  source: Results, paragraph 6\n  quote: The monofascicular rat nerves were ∼10× smaller, and their diameters approximated the\n    diameter of a single human or pig fascicle.\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  depends_on:\n  - rat-nerve-diameter\n  - cervical-fascicle-diameter-species\n  - subdiaphragmatic-fascicle-diameter-comparable\n  criterion: The paper fixes no measure. Readings (a) at each level the rat mean nerve diameter\n    lies between the pig and the human mean fascicle diameters (from the paper's means, 0.260\n    between 0.155 and 0.355 mm, and 0.135 between 0.110 and 0.163 mm); (b) at each level the rat\n    mean nerve diameter lies within the range of the human and pig fascicle diameters.\n    Reproduced when either reading holds at both levels.\n- id: human-pig-tissue-proportions\n  statement: Endoneurium is a larger share of the human nerve cervically (32 +/- 7.9%) than\n    subdiaphragmatically (8.8 +/- 5.3%), while in pigs it is more even across levels (27 +/- 5.3%\n    and 20 +/- 4.0%, MT); perineurium follows the same trends (human 8.9 +/- 2.5% and 3.4 +/-\n    1.6%, pig 5.1 +/- 1.8% and 4.0 +/- 0.5%).\n  source: Results, paragraph 7\n  quote: The human endoneurium occupied a larger proportion of the nerve at the cervical level (32\n    ± 7.9%) than at the subdiaphragmatic level (8.8 ± 5.3%) whereas the endoneurial proportions\n    were more consistent across levels in pigs, slightly lower than in the human cervical VN (27\n    ± 5.3% at the cervical level and 20 ± 4.0% at the subdiaphragmatic level for the MT\n    micrographs ... These same trends between species and levels were present for the proportion\n    of perineurium (8.9 ± 2.5% and 3.4 ± 1.6% at the cervical and subdiaphragmatic levels in\n    humans; 5.1 ± 1.8% and 4.0 ± 0.5% in pigs).\n  datasets:\n  - sparc-65\n  - sparc-64\n  - sparc-89\n  expected:\n  - quantity: human cervical endoneurium proportion\n    value: 32\n    tolerance: 7.9\n    unit: \"%\"\n  - quantity: human subdiaphragmatic endoneurium proportion\n    value: 8.8\n    tolerance: 5.3\n    unit: \"%\"\n  - quantity: pig cervical endoneurium proportion, MT\n    value: 27\n    tolerance: 5.3\n    unit: \"%\"\n  - quantity: pig subdiaphragmatic endoneurium proportion, MT\n    value: 20\n    tolerance: 4.0\n    unit: \"%\"\n  - quantity: human cervical perineurium proportion\n    value: 8.9\n    tolerance: 2.5\n    unit: \"%\"\n  - quantity: human subdiaphragmatic perineurium proportion\n    value: 3.4\n    tolerance: 1.6\n    unit: \"%\"\n  - quantity: pig cervical perineurium proportion\n    value: 5.1\n    tolerance: 1.8\n    unit: \"%\"\n  - quantity: pig subdiaphragmatic perineurium proportion\n    value: 4.0\n    tolerance: 0.5\n    unit: \"%\"\n  criterion: Proportions are tissue area over nerve area (Figure 7 legend), mean over samples.\n    Human from sparc-65, pig endoneurium from the MT traces (sparc-64). The pig MT traces have\n    no perineurium (Figure 6 legend), so the pig perineurium is read as the IF value (sparc-89,\n    four samples per level). Reproduced when every value is within its stated SD.\n- id: pig-if-endoneurium-lower\n  statement: The pig endoneurial proportions from the anti-fibronectin IF micrographs are about\n    2 percentage points lower than those from MT, as the IF segmentation accounts for the\n    perineurium.\n  source: Results, paragraph 7\n  quote: means were ∼2 percentile points lower for the anti-fibronectin IF micrographs for which\n    the segmentation accounted for the perineurium\n  datasets:\n  - sparc-89\n  - sparc-64\n  expected:\n  - quantity: pig MT minus pig IF mean endoneurium proportion, each level\n    value: 2\n    tolerance: 0.2\n    unit: percentage points\n  criterion: Mean endoneurial proportion of the four IF samples per level (sparc-89) against the\n    MT mean of the nine samples per level (sparc-64), the comparison the sentence makes. The\n    tolerance is the default 10%; the paper's \"∼\" sets none. A second reading compares the IF\n    and MT values of the same four samples per level; the claim holds under either. The\n    differences are reported per level.\n- id: rat-level-ratios\n  statement: In rats the ratio of mean subdiaphragmatic to mean cervical endoneurial area is 0.32\n    and the ratio of mean nerve diameters is 0.68.\n  source: Discussion, paragraph 3\n  quote: The ratios of the mean endoneurial area of the subdiaphragmatic VN to the cervical VN were\n    0.20, 0.42, and 0.32 for human, pig, and rat, respectively ... where the ratios of the mean\n    diameter of the subdiaphragmatic VN to the cervical VN were 0.87, 0.75, and 0.68 for human,\n    pig, and rat, respectively.\n  datasets:\n  - sparc-60\n  depends_on:\n  - rat-nerve-diameter\n  expected:\n  - quantity: rat ratio of mean endoneurial area, subdiaphragmatic over cervical\n    value: 0.32\n    tolerance: 0.032\n  - quantity: rat ratio of mean effective nerve diameter, subdiaphragmatic over cervical\n    value: 0.68\n    tolerance: 0.068\n  criterion: The paper does not say which rat subdiaphragmatic tissue enters these ratios, and\n    its own Results means give a diameter ratio of 0.52 (0.135/0.260), not 0.68. Readings (a)\n    the largest fascicle only, as in all statistics (nerve boundary its outer perineurium); (b)\n    for the three multifascicular samples, all segmented fascicles for endoneurial area and the\n    connective tissue boundary for nerve diameter (Figure 6 legend). Each ratio is reproduced\n    when within 10% under either reading; the claim is reproduced when both are, partially when\n    one is. The 0.52 from the Results means is reported.\n- id: human-pig-level-ratios\n  statement: The ratio of mean subdiaphragmatic to mean cervical endoneurial area is 0.20 in\n    humans and 0.42 in pigs, and the ratio of mean nerve diameters is 0.87 and 0.75.\n  source: Discussion, paragraph 3\n  quote: The ratios of the mean endoneurial area of the subdiaphragmatic VN to the cervical VN were\n    0.20, 0.42, and 0.32 for human, pig, and rat, respectively ... where the ratios of the mean\n    diameter of the subdiaphragmatic VN to the cervical VN were 0.87, 0.75, and 0.68 for human,\n    pig, and rat, respectively.\n  datasets:\n  - sparc-65\n  - sparc-64\n  expected:\n  - quantity: human ratio of mean endoneurial area\n    value: 0.2\n    tolerance: 0.02\n  - quantity: pig ratio of mean endoneurial area\n    value: 0.42\n    tolerance: 0.042\n  - quantity: human ratio of mean effective nerve diameter\n    value: 0.87\n    tolerance: 0.087\n  - quantity: pig ratio of mean effective nerve diameter\n    value: 0.75\n    tolerance: 0.075\n  criterion: Endoneurial area is the area within all inner perineurium traces of a sample\n    (Figure 7 legend), averaged over the nine samples per level; pig from the MT traces\n    (sparc-64). Each ratio is within 10% for the claim to hold.\n- id: human-variability\n  statement: Nerve and fascicle diameters are more consistent across samples in pigs (and rats)\n    than in humans.\n  source: Results, paragraph 7; Discussion, paragraph 2\n  quote: Qualitatively, the nerve and fascicle diameters were more consistent across samples for\n    the pig nerves than for the humans nerves ( Figure 6 )\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  criterion: The paper judges this qualitatively from Figure 6 and names no measure. Readings\n    (a) the coefficient of variation across samples of effective nerve diameter and of\n    per-sample mean fascicle diameter; (b) for fascicles, the Discussion's \"ranges of fascicle\n    diameters\", the coefficient of variation across samples of each sample's fascicle diameter\n    range (human and pig only, as rat statistics use one fascicle per sample). Reproduced\n    when, at both levels, the human value exceeds the pig value and the rat value for both\n    measures under either reading; partially reproduced when human exceeds pig but not rat.\n    The SDs over means from the paper's Results (nerve diameter, human 0.26 and 0.18, pig 0.09\n    and 0.13, rat 0.10 and 0.11) are reported for comparison. The outcome rests on the reading.\n- id: pig-oblong-human-round\n  statement: Pig vagus nerves are consistently oblong in cross section, whereas human nerves are\n    more circular at the cervical level.\n  source: Results, paragraph 7; Figures 2 and 3\n  quote: pig nerves were consistently oblong in shape, whereas the human samples were more\n    circular at the cervical level ( Figures 2 , 3 , Supplement 3 )\n  datasets:\n  - sparc-65\n  - sparc-64\n  criterion: The paper judges this by eye from the micrographs and names no measure. On the\n    nerve traces (human inner trace where there are two, Figure 2 legend), readings (a) the\n    aspect ratio (major over minor axis) of the ellipse with the same second moments; (b)\n    circularity, 4 pi area over perimeter squared. Reproduced when, under either reading, every\n    pig sample at both levels is less circular than the median human cervical sample and the\n    human cervical median is more circular than the pig median at each level. These rules are\n    this file's reading and the outcome rests on them. The MT sections of all collected samples\n    (sparc-61, sparc-82) are a variant judged by eye.\n- id: human-subdiaphragmatic-fatty-tissue\n  statement: Pig nerves have consistent collagenous epineurium, whereas many human\n    subdiaphragmatic nerves have fatty extrafascicular tissue.\n  source: Results, paragraph 7 (Supplement 3)\n  quote: pig nerves had consistent collagenous epineurium, whereas many human subdiaphragmatic\n    nerves had fatty extrafascicular tissue ( Supplement 3 )\n  datasets:\n  - sparc-61\n  - sparc-82\n  criterion: Judged by eye on the MT micrographs of all collected samples, as Supplement 3 shows\n    them (not read); the paper gives no rule for fat or for \"many\". Adipose tissue is read as\n    clusters of large, empty, unstained polygonal cells in the extrafascicular tissue, MT\n    staining collagen blue. Readings of \"many\", (a) at least half, (b) at least a third, of the\n    human subdiaphragmatic micrographs. Reproduced when the human count meets a reading and no\n    more than one pig micrograph (of 45) has adipose tissue within the epineurium. These rules\n    are this file's reading and the outcome rests on them.\n- id: pig-cervical-cell-bodies\n  statement: In two pig cervical cross sections (P11-1 and P13-1) one fascicle contains cell\n    bodies.\n  source: Results, paragraph 1; Figure 3 legend\n  quote: in two of the pig cervical cross sections, one fascicle contained cell bodies, although\n    we did not sample the nerve close to the nodose ganglion\n  datasets:\n  - sparc-82\n  - sparc-64\n  criterion: Judged by eye on the MT micrographs of the nine analysed pig cervical samples\n    (Figure 3 legend names P11-1 and P13-1); the paper gives no rule for identifying cell\n    bodies, read here as large round neuronal somata with a nucleus within a fascicle.\n    Reproduced when P11-1 and P13-1 each show one such fascicle and no other analysed pig\n    cervical sample does; partially reproduced when the two named samples show them and others\n    do too.\n- id: literature-comparison-human-pig\n  statement: Human cervical fascicle numbers and endoneurial areas match prior reports while the\n    nerve areas and diameters are generally smaller; human subdiaphragmatic sizes match prior\n    reports; pig fascicle numbers match literature, with slightly smaller mean diameters.\n  source: Results, paragraph 8; Discussion, paragraph 4\n  quote: The numbers of fascicles and endoneurial cross-sectional areas of the human cervical VNs\n    were comparable to previous reports, but the nerve cross-sectional areas and effective\n    diameters were generally smaller, albeit with overlapping ranges.\n  data: with_inputs\n  datasets:\n  - sparc-65\n  - sparc-64\n  criterion: Judged as Figure 7 shows it, the paper's mean +/- SD against each literature mean,\n    the literature values from Supplement 4 (studies named in the Figure 7 legend). The\n    Discussion gives the literature human cervical diameter as 3.0 mm (left and right, three\n    studies) and 2.0 mm (Stakenborg et al., 2020); that part is reproduced when the human\n    cervical mean nerve diameter is below 3.0 mm. \"Comparable\" is read as each literature mean\n    within the paper's mean +/- SD, \"smaller\" as the paper's mean below the literature mean, and\n    \"overlapping ranges\" as the paper's sample range overlapping the literature spread; these\n    rules are this file's reading of Figure 7 and the outcome rests on them. The parts that need\n    Supplement 4, which was not supplied, are not decidable from the text read.\n- id: rat-literature-comparison\n  statement: Rat cervical nerve diameters and areas agree with published data, while the rat\n    subdiaphragmatic nerves are slightly larger than prior data.\n  source: Results, paragraph 8; Discussion, paragraph 6\n  quote: The nerve diameters and cross-sectional areas of the rat cervical VNs compared well to\n    published data, while our rat subdiaphragmatic nerves were slightly larger than prior data\n  data: with_inputs\n  datasets:\n  - sparc-60\n  depends_on:\n  - rat-nerve-diameter\n  criterion: The literature values are in Supplement 4 and Figure 7 (Fazan and Lachat, 1997;\n    Licursi de Alcântara et al., 2008, cervical; Prechtl and Powley, 1985, subdiaphragmatic),\n    none of them in the text read. With those values as inputs, reproduced when each published\n    cervical mean lies within the rat cervical mean +/- SD and the rat subdiaphragmatic mean\n    exceeds each published subdiaphragmatic mean (\"compared well\" and \"slightly larger\", the\n    Discussion's \"trended larger\", are judged by the paper as Figure 7 shows them; these rules\n    are this file's reading of that figure, and the outcome rests on them). Without the values\n    the claim cannot be decided.\n- id: perineurium-species-order\n  statement: For a given fascicle diameter, human fascicles have the thickest perineurium and\n    rat fascicles the thinnest.\n  source: Results, paragraph 10; Figure 8; Figure 9A\n  quote: For a given fascicle diameter, the human samples had the thickest perineurium while the\n    rat samples had the thinnest perineurium.\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-89\n  depends_on:\n  - human-perineurium-fit\n  - pig-perineurium-fit\n  - rat-perineurium-fit\n  criterion: Perineurium thickness is half the difference of the outer and inner effective\n    diameters; non-peanut fascicles only (Figure 9 legend); human IHC (sparc-65), pig IF\n    (sparc-89), rat MT (sparc-60). The paper does not say how \"for a given diameter\" is\n    compared. Readings (a) each species' fit (fit form as in rat-perineurium-fit) evaluated\n    across the diameters common to all three species; (b) the fits evaluated at 250 um, the\n    size of the Figure 8 examples. Reproduced when human > pig > rat under either reading (over\n    the whole common range for a).\n- id: perineurium-ratio-decreases\n  statement: The ratio of perineurium thickness to fascicle diameter decreases as fascicle\n    diameter increases, particularly in humans and pigs.\n  source: Results, paragraph 10; Figure 9B\n  quote: The ratio of perineurium thickness to fascicle diameter decreased with increased fascicle\n    diameter, particularly for the human and pig samples ( Figure 9B ).\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-89\n  criterion: The paper shows this in Figure 9B without a test. Readings (a) the ratio implied by\n    each species' fit (rat-perineurium-fit) decreases over the species' range of diameters; (b)\n    Spearman correlation of the ratio with diameter is negative. Reproduced when human and pig\n    show the decrease under either reading; the rat result, of which the paper claims less, is\n    reported and not required.\n- id: human-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 73 human non-peanut\n    fascicles has R2 = 0.75.\n  source: Results, paragraphs 10 and 11 (Eq. 1)\n  quote: We fit the data from 73 human fascicles (excluding fascicles with more than one inner\n    perineurium trace for a given outer perineurium trace, i.e., peanut fascicles) as ... with d\n    fasc in microns, yielding R 2 = 0.75.\n  datasets:\n  - sparc-65\n  expected:\n  - quantity: number of human non-peanut fascicles fitted\n    value: 73\n    tolerance: 0\n  - quantity: R2 of the human fit\n    value: 0.75\n    tolerance: 0.075\n  criterion: Both levels pooled (the Results give one fit per species). Thickness and diameter\n    as in rat-perineurium-fit, with the same fit-form readings. The count tolerance is 0, as it\n    is a count of traces. Eq. 1's coefficients are missing from the text read.\n- id: pig-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 284 pig non-peanut\n    fascicles (IF) has R2 = 0.30.\n  source: Results, paragraphs 11 and 12 (Eq. 2)\n  quote: We fit the data from 284 pig non-peanut fascicles as ... with d fasc in microns, yielding\n    R 2 = 0.30.\n  datasets:\n  - sparc-89\n  expected:\n  - quantity: number of pig non-peanut fascicles fitted\n    value: 284\n    tolerance: 0\n  - quantity: R2 of the pig fit\n    value: 0.3\n    tolerance: 0.03\n  criterion: Both levels of the eight IF samples pooled. Thickness and diameter as in\n    rat-perineurium-fit, with the same fit-form readings. Eq. 2's coefficients are missing from\n    the text read.\n- id: rat-perineurium-fit\n  statement: The fit of perineurium thickness against fascicle diameter for 22 rat fascicles has\n    R2 = 0.77.\n  source: Results, paragraphs 12 and 13 (Eq. 3)\n  quote: We fit the data from 22 rat fascicles as ... with d fasc in microns, yielding R 2 = 0.77.\n  datasets:\n  - sparc-60\n  expected:\n  - quantity: number of rat fascicles fitted\n    value: 22\n    tolerance: 0\n  - quantity: R2 of the rat fit\n    value: 0.77\n    tolerance: 0.077\n  criterion: Per rat fascicle with an inner and an outer perineurium trace, effective fascicle\n    diameter (inner boundary, um) and thickness, half the outer minus inner effective diameter\n    (Methods). Fit by linear least squares (MATLAB fit, Methods). Two details are open, as Eq. 3\n    is missing from the text read. The fascicle set, read as (a) every segmented rat fascicle,\n    including the smaller ones of the multifascicular subdiaphragmatic samples, or (b) the 18\n    largest fascicles only; 22 fascicles across 18 samples points to (a). The fit form, read as\n    (i) thickness linear in diameter with an intercept, which the paper's \"also ... with a\n    linear equation with forced zero intercept\" for Eq. 4 suggests, (ii) linear through zero,\n    or (iii) another model linear in its coefficients (a power law fitted in log space is\n    excluded, as the Methods name linear least squares on the data). Reproduced when, under\n    one combination, the count is 22 and R2 is within tolerance; partially reproduced when the\n    count matches and R2 is outside. The coefficients are reported for comparison with Eq. 3\n    once it is read from the PDF.\n- id: perineurium-thicker-larger-fascicles\n  statement: In the human and pig vagus nerves, larger fascicles have thicker perineurium.\n  source: Introduction, paragraph 3; Results, paragraph 10; Figure 9A\n  quote: our data also showed thicker perineurium for larger fascicles, as well as thicker\n    perineurium as a proportion of fascicle diameter for smaller fascicles.\n  datasets:\n  - sparc-65\n  - sparc-89\n  depends_on:\n  - human-perineurium-fit\n  - pig-perineurium-fit\n  criterion: Non-peanut fascicles (Figure 9 legend), thickness and diameter as in\n    rat-perineurium-fit, the species' fits of Eqs. 1 and 2 (fit form open, readings as in\n    rat-perineurium-fit). The paper shows this in Figure 9A without a test. Readings (a) the\n    fitted thickness increases over the species' range of diameters; (b) Spearman correlation\n    of thickness with diameter is positive. Reproduced when human and pig both show the\n    increase under either reading; the rat result is reported, not required.\n- id: perineurium-no-level-difference\n  statement: The relationship between perineurium thickness and fascicle diameter does not\n    differ between cervical and subdiaphragmatic nerves in any of the three species.\n  source: Results, paragraph 13\n  quote: The data did not suggest a difference in the relationship between perineurium thickness\n    and fascicle diameter for cervical versus subdiaphragmatic nerves for any of the three\n    species.\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-89\n  depends_on:\n  - rat-perineurium-fit\n  criterion: A claim of absence for which the paper names no test, so no test of the paper's\n    can be used. Per species, the fit of rat-perineurium-fit fitted separately to cervical and\n    to subdiaphragmatic fascicles. Readings (a) the 95% confidence bounds of each coefficient\n    (as MATLAB fit, the paper's tool, reports them) overlap between levels; (b) an F-test of a\n    level term (intercept and slope by level) in the pooled linear model at p < 0.05. Reproduced\n    when no species shows a difference under reading (a); reading (b) is shown as a variant,\n    and any species where the two disagree is recorded. Both tests are choices of this file,\n    as the paper's \"did not suggest\" names none, so the outcome rests on an assumption.\n- id: sunderland-reanalysis\n  statement: Refitting all 777 fascicles of Sunderland and Bradley (1952) gives a zero-intercept\n    slope of 2.75% of fascicle diameter for perineurium thickness, with R2 = 0.51.\n  source: Results, paragraphs 13 and 14 (Eq. 4); Discussion, paragraph 7; Figure 9C and 9D\n  quote: We re-analyzed the original ( Sunderland and Bradley, 1952 ) data, including all 777\n    fascicles ... and identified the slope of the best-fit line with zero intercept as 2.75% ( R 2\n    = 0.51)\n  data: elsewhere\n  where: Sunderland and Bradley (1952), the published human somatic nerve fascicle measurements;\n    no archive identifier\n  expected:\n  - quantity: slope of zero-intercept fit, perineurium thickness over fascicle diameter\n    value: 2.75\n    tolerance: 0.275\n    unit: \"%\"\n  - quantity: R2 of the fit\n    value: 0.51\n    tolerance: 0.051\n  - quantity: fascicles fitted\n    value: 777\n    tolerance: 0\n  criterion: Linear least squares with forced zero intercept (Results, before Eq. 4) on all 777\n    fascicles. How R2 is computed for a zero-intercept fit is open; readings (a) about the mean\n    of the data (MATLAB fit's R2), (b) uncentred. The claim holds under either.\n- id: rat-perineurium-near-3-percent\n  statement: Rat perineurium thickness is close to the published 3% of fascicle diameter,\n    slightly thicker for smaller fascicles and thinner for larger ones.\n  source: Discussion, paragraph 7; Figure 9A and 9B\n  quote: While we found that the rat perineurium thickness was similar to this published\n    relationship, albeit slightly thicker for smaller fascicle diameters and thinner for larger\n    fascicle diameters\n  datasets:\n  - sparc-60\n  depends_on:\n  - rat-perineurium-fit\n  criterion: The comparison line is thickness = 3% of fascicle diameter (Figure 9 legend,\n    Grinberg et al., 2008); \"this published relationship\" can also be read as the 2.75% slope\n    of the re-analysis, so both are run. With the rat fit of rat-perineurium-fit, reproduced\n    when the fitted thickness over thickness of the reference line is between 0.5 and 2 across\n    the rat diameter range (similar, read as within a factor of two, a choice of this file on\n    which the outcome rests), and the fit lies above the line at the smallest rat diameter and\n    below it at the largest (one crossing). Partially reproduced when the rat data are within\n    the factor but do not cross the line.\n- id: human-pig-perineurium-thicker\n  statement: Human and pig vagal perineurium is substantially thicker than the 3% of fascicle\n    diameter found for human somatic nerves, especially for smaller fascicles.\n  source: Discussion, paragraph 7; Figure 9B\n  quote: the human and pig perineurium was substantially thicker, especially for smaller fascicles\n    ( Figure 9B )\n  datasets:\n  - sparc-65\n  - sparc-89\n  criterion: For non-peanut fascicles (Figure 9 legend), the ratio of thickness to diameter\n    against the 3% line of Figure 9. The paper judges this from Figure 9B and names no\n    measure; this file reads it as follows, and the outcome rests on that reading. Reproduced\n    when, for both species, the median ratio exceeds 0.03 and the median excess over 0.03 is\n    larger for fascicles below the species' median diameter than above it.\n- id: pig-if-mt-consistent\n  statement: Pig fascicle diameters from anti-fibronectin IF (14 to 303 um, mean 123, median 123,\n    interquartile range 91 to 155 um) are consistent with those from MT (5 to 399 um, mean 135,\n    median 130, interquartile range 96 to 168 um).\n  source: Results, paragraph 12\n  quote: Note that the fascicle diameters for the pig anti-fibronectin IF ( Figures 9A,B ; 14 to\n    303 μm, mean = 123 μm, median = 123 μm, interquartile range = 91 to 155 μm) are consistent\n    with the MT data ( Figure 6 ; 5 to 399 μm, mean = 135 μm, median = 130 μm, interquartile\n    range = 96 to 168 μm).\n  datasets:\n  - sparc-89\n  - sparc-64\n  expected:\n  - quantity: pig IF fascicle diameter, mean\n    value: 123\n    tolerance: 12.3\n    unit: um\n  - quantity: pig IF fascicle diameter, median\n    value: 123\n    tolerance: 12.3\n    unit: um\n  - quantity: pig MT fascicle diameter, mean\n    value: 135\n    tolerance: 13.5\n    unit: um\n  - quantity: pig MT fascicle diameter, median\n    value: 130\n    tolerance: 13\n    unit: um\n  criterion: The IF values are over the 284 non-peanut fascicles of Figure 9A and B; the MT\n    values over all inner perineurium traces of the 18 pig MT samples (Figure 6). Reproduced\n    when the four values are within 10% and the ranges and interquartile ranges are within the\n    reported ones widened by 10% of each bound. The quartile method is open and cannot move the\n    values beyond the tolerance for samples of this size; MATLAB's prctile, the paper's tool,\n    is used.\n- id: peanut-fascicle-counts\n  statement: Human IHC micrographs have 60 cervical inner perineurium traces (27 bundles in 10\n    peanut fascicles) and 44 subdiaphragmatic (4 in 2); pig IF micrographs have 210 cervical (57\n    in 25) and 179 subdiaphragmatic (48 in 19).\n  source: Figure 9 legend\n  quote: For the human anti-claudin-1 IHC micrographs, the cervical level had 60 fascicles total\n    (inner perineurium traces) of which 27 were intrafascicular bundles in 10 peanut fascicles;\n    the subdiaphragmatic level had 44 fascicles total (inner perineurium traces) of which 4 were\n    intrafascicular bundles in 2 peanut fascicles.\n  datasets:\n  - sparc-65\n  - sparc-89\n  expected:\n  - quantity: human cervical inner perineurium traces\n    value: 60\n    tolerance: 0\n  - quantity: human subdiaphragmatic inner perineurium traces\n    value: 44\n    tolerance: 0\n  - quantity: pig IF cervical inner perineurium traces\n    value: 210\n    tolerance: 0\n  - quantity: pig IF subdiaphragmatic inner perineurium traces\n    value: 179\n    tolerance: 0\n  criterion: Counts of traces, tolerance 0. A peanut fascicle is an outer perineurium trace\n    holding more than one inner trace (Figure 2 legend). Reproduced when the four totals and\n    the peanut counts (27 in 10, 4 in 2, 57 in 25, 48 in 19) match; partially reproduced when\n    the totals match and a peanut count does not. Whether the non-peanut counts (60 - 27 + 44 -\n    4 = 73 human; 210 - 57 + 179 - 48 = 284 pig) match the fit counts is reported.\n- id: no-age-trend\n  statement: The morphology metrics show no trend with age in any species.\n  source: Discussion, paragraph 5 (Supplement 6)\n  quote: Our morphology metrics did not show trends with age for any species ( Supplement 6 )\n  datasets:\n  - sparc-60\n  - sparc-65\n  - sparc-64\n  criterion: A claim of absence whose test, if any, is in Supplement 6, which was not supplied.\n    Ages are the subject metadata (Supplement 1; human ages above 89 recorded as 90+). Until\n    Supplement 6 is read, the readings are (a) Pearson correlation of each per-sample metric\n    (nerve diameter, number of fascicles, mean fascicle diameter, tissue proportions) with\n    subject age at p < 0.05 per species and level; (b) the same with Spearman correlation.\n    Reproduced when no metric shows a trend under reading (a), (b) shown as a variant; the\n    claim rests on an assumption until Supplement 6 fixes the method and the metrics.\n- id: rat-carotid-sheath-bundles\n  statement: The rat cervical carotid sheath holds up to six fascicles, of which the largest,\n    taken as the vagus, was segmented.\n  source: Discussion, paragraph 6 (Supplementary Figure 16); Materials and Methods, Imaging and\n    Image Analysis, paragraph 3\n  quote: The rat cervical VN was identified as monofascicular in prior studies ( Fazan and Lachat,\n    1997 ; Licursi de Alcântara et al., 2008 ), but we observed up to six fascicles within the\n    carotid sheath ( Supplementary Figure 16 ).\n  datasets:\n  - sparc-16\n  - sparc-60\n  criterion: Tested on the rat cervical MT micrographs, which hold the whole carotid sheath\n    (Methods, the rat cervical VN was excised with the common carotid artery), whether or not\n    the other bundles are traced. The paper gives no rule for counting bundles and\n    Supplementary Figure 16 was not read; a bundle is read as a nerve profile bounded by its\n    own perineurium within the sheath, counted by eye, and the outcome rests on that reading.\n    Readings of the sample set, (a) the nine analysed left cervical samples, (b) all 18\n    cervical samples. Reproduced when, under a reading, the largest count is six, at least one\n    sample has more than one bundle, and in each analysed sample the bundle traced as the vagus\n    in sparc-60 is the largest. Partially reproduced when the largest count is five or seven.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/pelot-2020.yaml paper/10.3389-fnins.2020.601479.txt; echo EXIT $?; grep -n "—\|rather" claims/pelot-2020.yaml; python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/pelot-2020.yaml'))
txt=open('claims/pelot-2020.yaml').read()
# plain scalars containing ': ' : look at lines with key: value where value contains ': '
for n,l in enumerate(txt.splitlines(),1):
    if l.lstrip().startswith('#'): continue
    m=re.match(r'^\s*(- )?[a-z_]+: (.*)$',l)
    rest = m.group(2) if m else l.strip()
    if ': ' in rest and not rest.startswith(('"',"'")): print(n,l)
c=d['claims']; print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum(x.get('kind')=='link' for x in c))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short
```

```
M claims/pelot-2020.yaml
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

I updated `claims/pelot-2020.yaml` to protocol pilot-18 for all seven datasets. The quote checker passes: 43 claims, 43 quotes, 21 statistical values, 0 problems.

**Text read.** The version of record from Europe PMC (PMC7672126), flattened from JATS XML: abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was supplied, so no figure was read. The paper links no code, so none was read.

**What is missing from the paper text**
- **Eqs. 1 to 4** (the perineurium thickness fits) were lost when the text was flattened. Only the R2 values and fascicle counts survive, so the fit form and coefficients are open. The PDF would settle them.
- **The whole supplement** is absent. The paper's own numbers are all in the main text, so I wrote claims, but three claims cannot be fully decided without it:
  - Supplement 4 holds the literature values for `literature-comparison-human-pig` and `rat-literature-comparison`.
  - Supplement 6 holds the age trends for `no-age-trend`.
- **The reference list is empty.** I matched each dataset to the paper's citations (Pelot et al. 2020a to g) from the dataset titles and the legends that cite each one: 60 = g, 16 = e, 65 = a, 61 = c, 64 = f, 82 = d, 89 = b.

**Counts**
- 43 claims, all with quotes and criteria; 5 are link claims.
- 9 claims carry statistics.
- 1 claim is `elsewhere` (the Sunderland and Bradley reanalysis) and has no `datasets`, since it rests on none of the seven.
- 2 are `with_inputs` (the two literature comparisons).

**What changed**
- **Data fields:** claims on human and pig data now rest on sparc-65, 64 and 89 through `datasets`; they were `elsewhere` or `with_inputs` before. Every claim except the Sunderland one lists its datasets.
- **New link claims:** `human-sample-set`, `pig-mt-sample-set`, `pig-if-sample-set`, and `mt-micrograph-collections` (covering sparc-16, 61 and 82).
- **New finding claims:** `pig-oblong-human-round`, `human-subdiaphragmatic-fatty-tissue`, `pig-cervical-cell-bodies`, and `pig-if-endoneurium-lower`.
- **Mixed-model criteria:** they now name the JMP settings. REML with Kenward-Roger degrees of freedom is taken from JMP, the software the paper names. Whether variance components are bounded at zero is run both ways.
- **`rat-carotid-sheath-bundles`:** its criterion no longer contradicts itself. It is now tested on the rat micrographs in sparc-16, with the counting rule named as open. This touches a question still open in `questions/pelot-2020.yaml`, which I did not mark answered.
- **Smaller changes:** an R2 reading for the Sunderland fit, a quartile method, and the two ways of forming the human and pig means.
- **Old check removed:** the check of 2026-11-18 applied to the earlier file, so I did not carry it over; its changes are kept.
- **Ids:** all old ids are kept.

**Details the paper leaves open, with the readings named**
- **Variance components in the mixed models:** unbounded (JMP's default) or bounded at zero.
- **Tukey contrasts printed with one p for both levels:** main-effect contrast, with per-level contrasts as a variant.
- **Perineurium fit form:** linear with intercept, through zero, or another model linear in its coefficients.
- **Rat fascicles in the perineurium fit:** all segmented fascicles, or only the largest per sample.
- **"Largest" rat fascicle:** by outer area, with inner area shown if it picks another fascicle.
- **Human and pig fascicle means:** pooled over all fascicles, or the mean of per-sample means.
- **Rat tissue in the Discussion's ratios:** the largest fascicle, or all fascicles. The paper's 0.68 diameter ratio conflicts with its own 0.52.
- **Pig IF against MT comparison:** all MT samples, or the same four samples per level.
- **Words with no measure in the paper.** The rules I named are choices of the file, and the outcomes rest on them:
  - "approximately ten times": a ratio between 5 and 20.
  - "clearest": relative difference, or difference over pooled SD.
  - "more consistent": coefficient of variation, or ranges.
  - "oblong": aspect ratio, or circularity.
  - "many": at least half, or at least a third.
  - "similar": within a factor of two.
  - "for a given diameter": fits compared over the common range, or at 250 µm.
- **The two absence claims with no stated test:**
  - Level difference in the perineurium relationship: overlapping confidence bounds, or an F-test.
  - Age trends: Pearson, or Spearman.
- **Judged by eye:** fat, cell bodies and carotid-sheath bundles, as the paper gives no rule.
- **Sunderland R2:** centred or uncentred.

**Inconsistencies in the paper, recorded for the author:** the rat diameter ratio (0.68 against 0.52), and the pig cervical sample count (21 stated, 22 implied by the Methods' own description).

## End of run

22 turns, 6 minutes, $2.05 at API prices, result: success.
