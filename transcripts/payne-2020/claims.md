# payne-2020 · claims · run 44201825356

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper/ claims/ tools/
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
3	Version: `pilot-16`. Record this version in the attempt's provenance.
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
cat claims/fouke-2025.yaml
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
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "archive: sparc" claims/*.yaml | head -3; grep -n -i -A3 "sparc" docs/archives.md | head -40; cat papers/datasets/payne-2020.yaml 2>/dev/null; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.619275.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -A15 '"206"\|"id": 206' targets/sparc.json | head -40
```

```
"id": "206",
   "name": "Recording of electrically evoked neural activity and bladder pressure responses in awake rats chronically implanted with a pelvic nerve array",
   "url": "https://sparc.science/datasets/206?type=dataset",
   "doi": "10.26275/kkmb-vun5",
   "published_version": "1",
   "latest": "1",
   "versions": 1,
   "version_dois": [
    "10.26275/kkmb-vun5"
   ],
   "published": "2021-12-14",
   "license": "Creative Commons Attribution",
   "bucket": "sparc-prod-aod-discover-publish50-use1",
   "manifest_version": "Ag7Kwl87aKqHqVTtho8dzikC2BfNyghN",
   "asset_count": 88,
   "size_gb": 0.0449,
```

**Agent**

I've read the paper: the version of record, full text with Methods, no supplement referenced, no code linked. Now checking the dataset description, then writing the claims.

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/sparc.json'))
L=d if isinstance(d,list) else d.get('targets',d.get('datasets'))
for t in L:
  if str(t.get('id'))=='206':
    print({k:v for k,v in t.items() if k not in('files',)})
"; grep -n "kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c
```

```
{'id': '206', 'name': 'Recording of electrically evoked neural activity and bladder pressure responses in awake rats chronically implanted with a pelvic nerve array', 'url': 'https://sparc.science/datasets/206?type=dataset', 'doi': '10.26275/kkmb-vun5', 'published_version': '1', 'latest': '1', 'versions': 1, 'version_dois': ['10.26275/kkmb-vun5'], 'published': '2021-12-14', 'license': 'Creative Commons Attribution', 'bucket': 'sparc-prod-aod-discover-publish50-use1', 'manifest_version': 'Ag7Kwl87aKqHqVTtho8dzikC2BfNyghN', 'asset_count': 88, 'size_gb': 0.0449, 'data_standards': ['SDS', 'HDF5', 'CSV', 'Excel', 'JSON', 'text', 'pxp', 'pzfx', 'html', 'rmd', 'Python'], 'sds': {'folders': ['code', 'derivative', 'docs', 'primary', 'protocol'], 'sheets': ['dataset_description', 'subjects'], 'folder_manifests': 5}, 'files_listed': 'all', 'readme': True, 'description': 'Electrical neuromodulation of the rat pelvic nerve (homolog of the human pelvic splanchnic nerves) by chronically implanted custom planar four-electrode arrays and assessment of bladder pressure responses by cystometry in awake rats.', 'code': [], 'protocols': ['10.17504/protocols.io.bgrmjv46'], 'contributors': [{'name': 'Sophie Payne', 'orcid': '0000-0002-3428-2275'}, {'name': 'Calvin Eiber', 'orcid': '0000-0002-8240-2649'}, {'name': 'Nicole Wiedmann', 'orcid': '0000-0001-9390-2457'}, {'name': 'Agnes Wong', 'orcid': None}, {'name': 'Philipp Senn', 'orcid': None}, {'name': 'Peregrine Osborne', 'orcid': '0000-0002-8458-4159'}, {'name': 'Janet Keast', 'orcid': '0000-0002-4341-3265'}, {'name': 'James Fallon', 'orcid': '0000-0003-2686-3886'}], 'species': [], 'approaches': [], 'keywords': ['recording techniques', 'neural decoding', 'electrophysiology'], 'papers': [{'doi': '10.3389/fnins.2020.619275', 'title': 'Recording of Electrically Evoked Neural Activity and Bladder Pressure Responses in Awake Rats Chronically Implanted With a Pelvic Nerve Array', 'relation': 'IsDescribedBy', 'resource_type': 'JournalArticle', 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "kind: agent" -B3 -A8 claims/zhai-2025.yaml | head -30; head -20 claims/zhai-2025.yaml; grep -n "kind\|open\|readings\|code_read\|'deviation\|allowed\|FIELDS" tools/claims_check.py | head -40
```

```
# Claims for Zhai, Cui, Wokosin, Sun, Tkatch, Crittenden, Graybiel & Surmeier (2025) on dandiset 001538.
# Source: the full text of the version of record in PubMed Central (PMC12674127, CC BY), read from
# its Results, figure legends and Materials and Methods.
#
# What the author had seen when these criteria were written. The data check: the file list and
# metadata of every NWB file; for every patch-clamp file the cell and condition counts, the spike
# counts per current step and each cell's rheobase, and per group the median rheobase; the
# dendritic excitability index per cell and its group medians; the Sr2+-oEPSC events found by the
# detector in lid.py and their per-cell counts and mean amplitudes; the GRAB-ACh areas per mouse;
# the AIM tables. Also the paper's per-cell tables (Zenodo doi:10.5281/zenodo.17307059), and that
# most dandiset cells match a row of them exactly. No statistical test of any claim had been run.
#
# The paper's statistics (Methods) are two-sided Mann-Whitney tests for unpaired and Wilcoxon tests
# for paired data at P < 0.05, unless stated otherwise; the criteria use these. Where the dandiset
# holds so few units that the paper's test cannot reach P < 0.05 whatever the data (the smallest
# attainable two-sided P is 0.057 for 3 against 4, 0.10 for 3 against 3, 0.25 for 3 pairs and
# 0.0625 for 5 pairs), the claim is blocked with `other`, and the numbers are shown under the link
# claim for that data. Groups are formed from the file's condition_subfolder column, not from the
# session name, because files named for a drug also hold baseline cells.
#
```

**Agent calls Bash**

```bash
grep -ln "written by an agent" claims/*.yaml | head -3; f=$(grep -ln "written by an agent" claims/*.yaml | head -1); head -40 $f; grep -n "open\b\|readings" $f | head; sed -n 1,60p tools/claims_check.py
```

```
claims/dijk-2018.yaml
claims/prince-2025.yaml
claims/vittani-2025.yaml
# Claims for van Dijk & Fenton (2018), "On How the Dentate Gyrus Contributes to Memory
# Discrimination", Neuron 98, 832-845, on CRCNS hc-17.
#
# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
# Actions"), 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the version of record (paper/10.1016-j.neuron.2018.04.018.txt, supplied by a
# person, extracted from the PDF), the main text, figure legends, STAR Methods (e1 to e5) and
# the Supplemental Information (Figures S1 and S2 with legends, Tables S1 and S2). No figure
# was read from a PDF page. The CRCNS data descriptor (hc-17.data-description.txt) was read
# only to know which experiments the dataset holds; no claim comes from it.
#
# Code read: the Data and Software Availability section links
# https://github.com/FentonLab/Mcode_DG-MemoryDiscrimination-NeuronMS. At commit
# 3542a85bb44a1739425e63eb4d16f9dc30ce7f54 (2018-04-01, the only commit) it holds a one-line
# README and a file "vanDijkFenton2018Neuron-AnalysisCode" that is a macOS alias (a pointer to
# a folder on the authors' computer), not code. No analysis code could be read, so no method
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"; sed -n 1,30p claims/prince-2025.yaml
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
[... 158 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
print(json.dumps(s['properties']['claims']['items']['properties'].get('where'),indent=0)[:600]); print(list(s['properties']['claims']['items']['properties'])); print(list(s['properties']))
d=s['\$defs']; print(json.dumps({k:{'req':v.get('required'),'props':{p:(q.get('type'),q.get('enum')) for p,q in v.get('properties',{}).items()}} for k,v in d.items()},indent=0)[:3000])"
```

```
{
"description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
"type": "string",
"minLength": 1
}
['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where', 'datasets']
['schema_version', 'dataset', 'paper', 'claims', 'checks']
{
"expected": {
"req": [
"quantity",
"value"
],
"props": {
"quantity": [
"string",
null
],
"value": [
"number",
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs']['statistic']['properties']['ci']))"
```

```
{"type": "object", "additionalProperties": false, "required": ["low", "high"], "properties": {"level": {"description": "The confidence level, e.g. 0.95.", "type": "number", "exclusiveMinimum": 0, "exclusiveMaximum": 1}, "low": {"type": "number"}, "high": {"type": "number"}, "unit": {"type": "string"}}}
```

**Agent**

The paper has full text and Methods, but it has no supplement and links no code. Its Data Availability statement says data are available on request. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/payne-2020.yaml",
 "content": "# Claims for Payne, Wiedmann, Eiber, Wong, Senn, Osborne, Keast & Fallon (2020), \"Recording of\n# Electrically Evoked Neural Activity and Bladder Pressure Responses in Awake Rats Chronically\n# Implanted With a Pelvic Nerve Array\", Front. Neurosci. 14, 619275, on SPARC:206.\n#\n# Provenance: written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub\n# Actions\"), 2026-11-17, protocol pilot-16 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read: the version of record, from Europe PMC (PMC7773906, JATS XML flattened;\n# paper/10.3389-fnins.2020.619275.txt), the main text, Materials and Methods, Table 1, figure\n# legends and Discussion. The paper has no supplement. No figure was read from a PDF page (no\n# PDF was supplied); Figure 2C, 3C and 5C/D are known here only from their legends and the\n# Results.\n#\n# Code read: none. The paper links no code; its Data Availability Statement says the raw data\n# \"will be made available by the authors\". Cystometry was analysed with customized MATLAB\n# software (R2019b) and c-Fos counts in R 3.5.2 and RStudio (Methods), neither of which is\n# linked. So no method detail below is settled by code. The SPARC dataset's title and\n# description (electrical neuromodulation of the rat pelvic nerve by chronically implanted\n# planar four-electrode arrays, and bladder pressure responses by cystometry in awake rats)\n# were read; no file of the dataset was opened.\n#\n# Data the paper used (Methods; Results).\n# - Animals. 24 male Sprague-Dawley rats, 8 to 9 weeks old. Pelvic nerve array (four platinum\n#   electrodes E1 to E4, E1 closest to the bladder; E1-E2 and E3-E4 are 0.75 mm apart centre to\n#   centre, the two pairs 2.85 mm apart centre to centre) sutured over the right pelvic nerve\n#   near the major pelvic ganglion (MPG); bladder catheter in the dome.\n# - Anaesthetised ECAPs (Figure 2A to C). 5 urethane-anaesthetised rats, end of life.\n#   Stimulation on E1-E2 (bipolar, 100 us pulse, 50 us interphase gap, 10 Hz), recording on\n#   E3-E4. Two sets of ECAPs, each the average of 50 responses, at 0 to 2 mA in 0.1 mA steps;\n#   sampled at 100 kHz, filtered 300 to 5000 Hz, gain 10^2. Three positive peaks P1, P2, P3.\n#   Threshold, the lowest current giving a response of at least 0.05 uV in both recordings.\n# - Awake ECAPs. Chronically implanted awake rats at week 0 and week 1 after implantation\n#   (Methods say three rats, Results say n = 4).\n# - Impedance. Common ground impedance (biphasic 25 us per phase, 931 uA; Z from the voltage\n#   at the end of the first phase): 38 electrodes in 10 arrays before implantation, day 1 and\n#   2 weeks; 8 electrodes in 2 arrays at 8 weeks.\n# - Colonic pressure. 3 urethane-anaesthetised rats, colonic balloon at 30 to 35 mmHg, pelvic\n#   nerve stimulation at 10 Hz, 100 us, 1 mA; 13 replicate responses in the one responder.\n# - Awake cystometry (Figure 3, Table 1). 12 rats in initial studies and 12 habituated rats\n#   (3 days, 30 min a day). Sessions of 2 h between day 7 and 18 after surgery, and in 2 rats\n#   at 8 weeks. Saline infused at 100 ul/min; bladder pressure sampled at 1 kHz (LabChart).\n#   Pelvic nerve stimulation trains of 10 s, biphasic, 100 us, 10 to 25 Hz, 0.5 to 1.5 mA, at\n#   chosen stages of the cycle (mostly at an estimated 50 to 80% fill). Unstimulated voiding\n#   parameters from the three cycles before any stimulation, in 9 rats (Table 1). Stimulated\n#   responses in 8 rats, classified as evoked voids (visible urine) or evoked non-voiding\n#   contractions (eNVC).\n# - Ganglion histology (Figure 4). L6 and S1 DRG and MPG, ipsi- and contralateral, from 2 rats\n#   at 50 days; ATF-3, CGRP and synaptophysin; archived axotomy ganglia (Payne et al., 2015) as\n#   positive control. Assessed qualitatively.\n# - Spinal c-Fos (Figure 5). 3 rats at day 10 after a session of cystometry and stimulation;\n#   segments L5 to S2, five 40 um sections per segment; c-Fos+ neurons counted per region\n#   (laminae I to VIII and X, SDCom, SPN) on each side.\n#\n# Inconsistencies in the paper, noted for the author. The awake ECAP cohort is three rats in\n# the Methods and n = 4 in the Results. The anaesthetised thresholds are called \"mean\" in the\n# Results, but the Statistics section says thresholds are given as median and IQR. The awake\n# thresholds are given as value plus or minus a spread that is not named (SD or SEM). The\n# impedance spreads are also unnamed. The c-Fos session is 60 min in the Results and a 2-h\n# testing period in the Methods.\n#\n# Details the paper leaves open, named in the criteria with the readings it allows: the\n# electrode distance used for conduction velocity; the stimulus level at which peak latencies\n# are taken; how threshold amplitude is measured; mean or median across rats; which groups\n# the awake Friedman test compares; the definitions of threshold pressure, peak pressure,\n# contraction duration and HFPO frequency (the paper cites Andersson et al., 2011 and Fraser\n# et al., 2020 for them); the window that makes a void \"immediately\" follow stimulation; the\n# family of comparisons for the c-Fos Welch tests.\nschema_version: 2\npaper: doi:10.3389/fnins.2020.619275\nclaims:\n- id: anes-ecap-recorded\n  statement: In all five urethane-anaesthetised rats, ECAPs with complex waveforms were recorded\n    on the non-stimulating electrode pair during graded stimulation and could be separated from\n    the stimulation artefact.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 1; Figure 2A and 2B\n  quote: In all cases, ECAPs with complex waveforms could be recorded from the non-stimulating\n    electrode pair during graded electrical stimulation; these ECAPS could be separated from the\n    stimulation artifact\n  criterion: >-\n    Per rat, the averaged E3-E4 response to E1-E2 stimulation at each current (Methods, ECAP and\n    Impedance Testing). Reproduced when, in each of the five rats, at least one positive peak\n    after the end of the stimulus artefact reaches the paper's threshold of 0.05 uV in both\n    recordings at some current, and is absent at 0 mA. The paper does not say where the artefact\n    ends; the readings are (a) after 1 ms from pulse onset, (b) after the first return of the\n    trace to baseline; both are shown.\n- id: anes-ecap-latencies\n  statement: In anaesthetised rats, ECAPs at supra-threshold stimulation show three positive\n    peaks centred at 1.80 ms (P1, range 1.65 to 2.90 ms), 3.48 ms (P2, 2.51 to 4.16 ms) and 3.77\n    ms (P3, 3.25 to 5.67 ms), n = 5.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 1\n  quote: >-\n    At supra-threshold stimulation levels these waveforms showed positive peaks centered at:\n    P1, 1.80 ms (range 1.65–2.90 ms, n = 5); P2, 3.48 ms (2.51–4.16 ms); and P3, 3.77 ms\n    (3.25–5.67 ms)\n  expected:\n  - quantity: P1 latency, central value over 5 rats\n    value: 1.80\n    tolerance: 0.18\n    unit: ms\n  - quantity: P2 latency, central value over 5 rats\n    value: 3.48\n    tolerance: 0.348\n    unit: ms\n  - quantity: P3 latency, central value over 5 rats\n    value: 3.77\n    tolerance: 0.377\n    unit: ms\n  criterion: >-\n    Tolerance is 10% of each value; the printed ranges are the spread across rats, not an\n    uncertainty of the central value, and each rat's latency is also expected to lie within its\n    range widened by 10% of each bound. Latency is the time of each positive peak in the averaged\n    E3-E4 response. Open, and named here. The central value is (a) the median (the Statistics\n    section presents latency as median and IQR) or (b) the mean. The time origin is (a) pulse\n    onset or (b) the end of the biphasic pulse (250 us later). The stimulus level is (a) the\n    highest current, 2 mA, (b) the lowest current at which all three peaks pass threshold, or\n    (c) the mean over all currents above P3 threshold. Reproduced when all three values are\n    within tolerance under one combination of readings; every combination is shown.\n- id: anes-conduction-velocity\n  statement: Approximate conduction velocities of the three populations in anaesthetised rats\n    are 1.60 m/s (P1, 0.98 to 1.72), 0.82 m/s (P2, 0.35 to 1.13) and 0.78 m/s (P3, 0.50 to 0.88),\n    in the range of myelinated A-fibres and unmyelinated C-fibres.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 1; Discussion,\n    paragraph 4\n  quote: >-\n    Approximate conduction velocities for these populations are 1.60 m/s (P1, 0.98–1.72 m/s),\n    0.82 m/s (P2, 0.35–1.13 m/s) and 0.78 m/s (P3, 0.50–0.88 m/s)\n  depends_on:\n  - anes-ecap-latencies\n  expected:\n  - quantity: P1 conduction velocity\n    value: 1.60\n    tolerance: 0.16\n    unit: m/s\n  - quantity: P2 conduction velocity\n    value: 0.82\n    tolerance: 0.082\n    unit: m/s\n  - quantity: P3 conduction velocity\n    value: 0.78\n    tolerance: 0.078\n    unit: m/s\n  criterion: >-\n    Velocity is conduction distance over peak latency, per rat, with latencies as in\n    anes-ecap-latencies. The paper does not state the distance. The readings, from the array\n    geometry in the Methods (Design of a Custom Planar Four-Electrode Array), are (a) 2.85 mm,\n    pair centre to pair centre, (b) 2.10 mm, E2 to E3, (c) 3.60 mm, E1 to E4. The central value\n    is the median or the mean across rats, as in anes-ecap-latencies. Reproduced when all three\n    values are within tolerance under one reading; all are shown.\n- id: anes-threshold-order\n  statement: In anaesthetised rats the stimulation threshold rises in the order of the first\n    (P1, 377 uA, 267 to 783), second (P2, 648 uA, 595 to 648) and third (P3, 930 uA, 550 to 1225)\n    responding populations, a main effect in a Friedman test (P = 0.039, n = 5).\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 1; Figure 2C\n  quote: >-\n    The mean stimulation threshold of these peaks increased in the order of the first (P1: 377\n    μA, 267–783 μA), second (P2: 648 μA, 595–648 μA) and third (P3: 930 μA, 550–1225 μA)\n    responding populations (main effect: non-parametric Friedman’s within-subject ANOVA: P =\n    0.039, n = 5)\n  statistics:\n  - test: Friedman test (non-parametric within-subject ANOVA), main effect of population\n    p: 0.039\n    n: 5 rats\n  depends_on:\n  - anes-ecap-latencies\n  expected:\n  - quantity: P1 threshold, central value over 5 rats\n    value: 377\n    tolerance: 37.7\n    unit: uA\n  - quantity: P2 threshold, central value over 5 rats\n    value: 648\n    tolerance: 64.8\n    unit: uA\n  - quantity: P3 threshold, central value over 5 rats\n    value: 930\n    tolerance: 93\n    unit: uA\n  criterion: >-\n    Threshold per rat and peak is the lowest stimulus current giving a response amplitude of at\n    least 0.05 uV in both of the two recordings (Methods, ECAP and Impedance Testing). Open, and\n    named here. The amplitude is (a) the positive peak voltage relative to the pre-stimulus\n    baseline, or (b) peak to the preceding trough. The threshold is (a) the lowest 0.1 mA step\n    passing, or (b) linearly interpolated between the last failing and first passing step (the\n    printed values are not multiples of 100 uA, which favours a reading finer than the step).\n    The central value is the median (Statistics section) or the mean (the word used in the\n    Results). Reproduced when a Friedman test over P1, P2 and P3 with rat as block gives P <\n    0.05 and the central values rise from P1 to P3; the three values are also checked against\n    tolerance under each combination of readings, and all are shown.\n- id: fig2c-p3-above-p1\n  statement: The third responding population has a significantly higher threshold than the\n    first (P = 0.034).\n  source: Figure 2C legend\n  quote: Quantification of neural thresholds shows the third responding neural population had\n    significantly higher thresholds ( P = 0.034) than the first responding\n  statistics:\n  - test: Dunn's post hoc test after Friedman test\n    p: 0.034\n    n: 5 rats\n  depends_on:\n  - anes-threshold-order\n  criterion: >-\n    Thresholds as in anes-threshold-order. Dunn's post hoc test on the Friedman rank sums, P3\n    against P1 (Statistics section names Friedman and Dunn's tests). The paper does not say\n    whether the Dunn P is adjusted for the three pairwise comparisons; readings (a) unadjusted,\n    (b) Bonferroni adjusted over three pairs. Reproduced when P < 0.05 with P3 higher under one\n    reading; both are shown.\n- id: fig2ab-one-rat-p2-below-p1\n  statement: In four of five anaesthetised rats the first responding population had a lower\n    threshold than later responding populations; in one rat the threshold of P1 was higher than\n    that of P2.\n  source: Figure 2A and 2B legends; Results, Electrically Evoked Compound Action Potentials,\n    paragraph 1\n  quote: Typically ( n = 4 of 5), the first responding neural populations had lower thresholds\n    than later responding populations. (B) In one animal, the first responding neural fiber\n    population had a higher threshold than the second\n  depends_on:\n  - anes-threshold-order\n  criterion: >-\n    Per rat, thresholds as in anes-threshold-order. Reproduced when exactly four of five rats\n    have the P1 threshold below both the P2 and P3 thresholds and one rat has the P1 threshold\n    above the P2 threshold, under one reading of threshold; counts under every reading are\n    shown.\n- id: awake-ecap-latencies\n  statement: In chronically implanted awake rats (n = 4), three populations were recruited in\n    all animals at week 0 and week 1, with mean latencies of 2.27 ms (P1, 1.93 to 2.65), 3.92 ms\n    (P2, 3.19 to 4.44) and 5.62 ms (P3, 4.57 to 6.72) and conduction velocities of 1.26, 0.73\n    and 0.51 m/s.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 2\n  quote: >-\n    Three neural populations, distinguished by their distinct latencies, were consistently\n    recruited in all animals at 0 and 1 week following implantation. The first responding fiber\n    population (P1) had a mean latency of 2.27 ms (range: 1.93–2.65 ms), second responding\n    fibers (P2) had a mean latency of 3.92 ms (range: 3.19–4.44 ms), and the third (P3) had a\n    mean latency of 5.62 ms (range: 4.57–6.72 ms). Approximate conduction velocities for these\n    populations are 1.26 m/s (P1, 1.08–1.48 m/s), 0.73 m/s (P2, 0.64–0.89 m/s) and 0.51 m/s\n    (P3, 0.42–0.62 m/s)\n  expected:\n  - quantity: P1 mean latency, awake\n    value: 2.27\n    tolerance: 0.227\n    unit: ms\n  - quantity: P2 mean latency, awake\n    value: 3.92\n    tolerance: 0.392\n    unit: ms\n  - quantity: P3 mean latency, awake\n    value: 5.62\n    tolerance: 0.562\n    unit: ms\n  - quantity: P1 conduction velocity, awake\n    value: 1.26\n    tolerance: 0.126\n    unit: m/s\n  - quantity: P2 conduction velocity, awake\n    value: 0.73\n    tolerance: 0.073\n    unit: m/s\n  - quantity: P3 conduction velocity, awake\n    value: 0.51\n    tolerance: 0.051\n    unit: m/s\n  criterion: >-\n    Same stimulation and recording as the anaesthetised ECAPs (Methods). Latency and velocity\n    readings as in anes-ecap-latencies and anes-conduction-velocity (time origin, stimulus level,\n    distance 2.85, 2.10 or 3.60 mm). The mean is over the awake rats; the paper does not say\n    whether week 0 and week 1 are pooled. Readings (a) mean over all rat and week recordings,\n    (b) mean over rats of each rat's mean over the two weeks, (c) week 0 alone. The number of\n    rats is three (Methods) or four (Results); the count found is reported. Reproduced when\n    three peaks are found in every awake rat at both weeks and all six values are within\n    tolerance under one combination of readings.\n- id: awake-threshold-increase\n  statement: In awake implanted rats, thresholds of all three populations increased from week 0\n    to week 1 (P1 391 to 643 uA, P2 677 to 1051 uA, P3 713 to 1263 uA), significantly by a\n    Friedman test (P = 0.039, n = 4).\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 2; Figure 2C\n  quote: >-\n    Neural thresholds of first (P1, week 0: 391 ± 138 μA, week 1: 643 ± 300 μA), second (P2,\n    week 0: 677 ± 149 μA, week 1: 1051 ± 275 μA) and third (P3, week 0: 713 ± 119 μA, week 1:\n    1263 ± 333 μA) responding fiber populations significantly increased at 1 week (Friedman\n    test, P = 0.039, n = 4\n  statistics:\n  - test: Friedman test\n    p: 0.039\n    n: 4 rats\n  depends_on:\n  - awake-ecap-latencies\n  expected:\n  - quantity: P1 threshold, week 0\n    value: 391\n    tolerance: 138\n    unit: uA\n  - quantity: P1 threshold, week 1\n    value: 643\n    tolerance: 300\n    unit: uA\n  - quantity: P2 threshold, week 0\n    value: 677\n    tolerance: 149\n    unit: uA\n  - quantity: P2 threshold, week 1\n    value: 1051\n    tolerance: 275\n    unit: uA\n  - quantity: P3 threshold, week 0\n    value: 713\n    tolerance: 119\n    unit: uA\n  - quantity: P3 threshold, week 1\n    value: 1263\n    tolerance: 333\n    unit: uA\n  criterion: >-\n    Tolerances are the paper's printed spread, whose kind (SD or SEM) is not named. Thresholds\n    as in anes-threshold-order (amplitude and step readings). The central value is (a) the mean\n    or (b) the median. The groups of the Friedman test are not stated; readings (a) one test\n    over six groups, three populations at two weeks, with rat as block, (b) one test per\n    population over week 0 and week 1 (a sign test in effect), (c) week as factor with\n    population and rat combined as blocks. Reproduced when every population's threshold is\n    higher at week 1 than at week 0 and the Friedman test gives P < 0.05 under one reading;\n    the six values are checked against tolerance and all readings are shown.\n- id: impedance-increase\n  statement: Mean electrode impedance rose from 4.19 kOhm before implantation to 7.25 kOhm on\n    day 1, 12.04 kOhm at 2 weeks and 13.1 kOhm at 8 weeks.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 3\n  quote: >-\n    The mean electrode impedance prior to implantation) was 4.19 ± 0.17 kΩ (range 3.16–5.03, n\n    = 38 electrodes, 10 arrays). On post-surgical day 1, this increased to 7.25 ± 0.79 kΩ\n    (range: 4.54–15.18 kΩ), and further increased after 2 weeks implantation to 12.04 ± 1.15 kΩ\n    (range: 6.24–18.3 kΩ, 38 electrodes in 10 arrays) and 8 weeks implantation to 13.1 ± 2.06\n    kΩ (8.0–20.2 kΩ, n = 8 electrodes, 2 arrays)\n  expected:\n  - quantity: mean impedance before implantation, 38 electrodes\n    value: 4.19\n    tolerance: 0.17\n    unit: kOhm\n  - quantity: mean impedance, day 1\n    value: 7.25\n    tolerance: 0.79\n    unit: kOhm\n  - quantity: mean impedance, 2 weeks, 38 electrodes\n    value: 12.04\n    tolerance: 1.15\n    unit: kOhm\n  - quantity: mean impedance, 8 weeks, 8 electrodes\n    value: 13.1\n    tolerance: 2.06\n    unit: kOhm\n  criterion: >-\n    Tolerances are the paper's printed spread, whose kind is not named. Impedance per electrode\n    is the voltage at the end of the first phase over the current (931 uA), as the Methods\n    define it. Mean over electrodes at each time point. Reproduced when all four means are\n    within tolerance; partially reproduced when they rise in this order but one or more is out\n    of tolerance. The printed ranges are also checked, widened by 10% of each bound.\n- id: electrode-failures\n  statement: No short circuits occurred during implantation, and only 2 of 40 electrodes became\n    open circuit, both within 2 weeks of implantation.\n  source: Results, Electrically Evoked Compound Action Potentials, paragraph 3\n  quote: No short circuits occurred during the implantation period, and only 2 out of 40\n    electrodes became open circuit (both within 2 weeks of implantation)\n  expected:\n  - quantity: open-circuit electrodes\n    value: 2\n    tolerance: 0\n    unit: electrodes of 40\n  criterion: >-\n    The counts are exact (tolerance 0, as they are counts of events). The paper does not state\n    the impedance that marks an open or short circuit; readings (a) a flag or note in the data,\n    (b) an impedance that the stimulator could not measure (out of range) or a value far above\n    the electrode's others. Reproduced when 2 of 40 electrodes are open within 2 weeks and none\n    is short.\n- id: colonic-pressure\n  statement: Pelvic nerve stimulation increased colonic pressure in only 1 of 3 anaesthetised\n    rats, by 2.6 mmHg (mean and SEM 2.6 and 0.1, 13 replicate responses), time-locked to\n    stimulation.\n  source: Results, Colonic Pressure Changes and Non-urological Effects of Pelvic Nerve Array\n    Stimulation, paragraph 1\n  quote: Only 1 of 3 animals responded, showing a small increase in colonic pressure of 2.6 ±\n    0.1 mm Hg (mean ± SEM, 13 within-subject replicate responses) time locked to pelvic nerve\n    stimulation\n  expected:\n  - quantity: colonic pressure increase in the responder, mean of 13 responses\n    value: 2.6\n    tolerance: 0.1\n    unit: mmHg\n  - quantity: responding rats\n    value: 1\n    tolerance: 0\n    unit: rats of 3\n  criterion: >-\n    Tolerance is the paper's SEM. The paper does not define the increase or a response.\n    Readings for the increase (a) peak colonic pressure during the 10 Hz, 1 mA train minus the\n    mean over an equal window before it, (b) mean during the train minus mean before it. A rat\n    responds when its increases exceed zero by a one-sample t-test at P < 0.05 (a choice made\n    here, as the paper gives no rule). Reproduced when one of three rats responds and its mean\n    increase is within tolerance under one reading.\n- id: no-fecal-expulsion-or-erection\n  statement: In awake rats, pelvic nerve stimulation did not cause expulsion of faecal pellets\n    (n = 10) or penile erection (n = 6), and no erection was seen in anaesthetised rats.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 1; Results, Colonic Pressure Changes, paragraph 1\n  quote: stimulation did not cause expulsion of fecal pellets ( n = 10 animals) or penile\n    erection ( n = 6)\n  criterion: >-\n    Visual observation (Results). Reproduced when the data hold observation notes for these\n    rats and none records faecal expulsion or erection with stimulation.\n- id: table1-minimum-pressure\n  statement: In 9 awake implanted rats, the minimum bladder pressure of unstimulated voiding\n    cycles was 10.3 mmHg (95% CI 7.4 to 13.2).\n  source: Table 1, row Minimum pressure\n  inferred: The number is only in Table 1; the Results sentence before it says the parameters\n    were comparable to published values.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 7.4\n      high: 13.2\n      level: 0.95\n      unit: mmHg\n    n: 9 rats\n  expected:\n  - quantity: mean minimum pressure\n    value: 10.3\n    tolerance: 2.9\n    unit: mmHg\n  criterion: &urodynamics >-\n    Tolerance is the half-width of the printed 95% CI. From the three voiding cycles before any\n    stimulation in each rat (Methods, Bladder Pressure Responses). The minimum pressure is the\n    lowest pressure after a voiding contraction; relative pressures subtract it (Methods). The\n    paper takes the other definitions from Andersson et al. (2011) and Fraser et al. (2020)\n    without stating them, so they are open, with readings. Threshold pressure is (a) the pressure\n    at the onset of the voiding contraction, where pressure begins its rapid rise, or (b) the\n    pressure at the moment of urine release. Peak (closing) pressure is the maximum pressure\n    during the contraction. Contraction duration is (a) from the onset of the rapid rise to the\n    return to minimum pressure, or (b) the time pressure stays above threshold pressure.\n    Inter-void interval is the time between successive voids. The mean over 9 rats is (a) the\n    mean of each rat's mean over three cycles, with a t-based 95% CI, or (b) the mean over all\n    cycles pooled. Reproduced when the mean lies within the printed 95% CI under one reading;\n    all readings are shown.\n- id: table1-threshold-pressure\n  statement: The relative threshold pressure of unstimulated voiding was 6.6 mmHg (95% CI 4.7\n    to 8.4), n = 9 rats.\n  source: Table 1, row Relative threshold pressure\n  inferred: The number is only in Table 1.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 4.7\n      high: 8.4\n      level: 0.95\n      unit: mmHg\n    n: 9 rats\n  expected:\n  - quantity: mean relative threshold pressure\n    value: 6.6\n    tolerance: 1.9\n    unit: mmHg\n  criterion: *urodynamics\n- id: table1-peak-pressure\n  statement: The relative peak (closing) pressure of unstimulated voiding was 51.2 mmHg (95% CI\n    39.5 to 63.0), n = 9 rats.\n  source: Table 1, row Relative peak (closing) pressure\n  inferred: The number is only in Table 1.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 39.5\n      high: 63.0\n      level: 0.95\n      unit: mmHg\n    n: 9 rats\n  expected:\n  - quantity: mean relative peak pressure\n    value: 51.2\n    tolerance: 11.8\n    unit: mmHg\n  criterion: *urodynamics\n- id: table1-contraction-duration\n  statement: The contraction duration of unstimulated voiding was 28.9 s (95% CI 17.1 to 37.5),\n    n = 9 rats.\n  source: Table 1, row Contraction duration\n  inferred: The number is only in Table 1. The printed CI is not symmetric about the mean.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 17.1\n      high: 37.5\n      level: 0.95\n      unit: s\n    n: 9 rats\n  expected:\n  - quantity: mean contraction duration\n    value: 28.9\n    tolerance: 11.8\n    unit: s\n  criterion: *urodynamics\n- id: table1-intervoid-interval\n  statement: The inter-void interval of unstimulated voiding was 7.6 min (95% CI 5.9 to 9.4), n\n    = 9 rats.\n  source: Table 1, row Inter-void interval\n  inferred: The number is only in Table 1.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 5.9\n      high: 9.4\n      level: 0.95\n      unit: min\n    n: 9 rats\n  expected:\n  - quantity: mean inter-void interval\n    value: 7.6\n    tolerance: 1.8\n    unit: min\n  criterion: *urodynamics\n- id: table1-hfpo-frequency\n  statement: High-frequency pressure oscillations during voiding contractions had a centre\n    frequency of 10.7 Hz (95% CI 8.3 to 13.0), n = 9 rats.\n  source: Table 1, row HFPO frequency; Methods, Bladder Pressure Responses, paragraph 3\n  inferred: The number is only in Table 1; the Methods say only that HFPOs were analysed to\n    estimate the centre frequency of oscillation.\n  statistics:\n  - test: mean and 95% CI\n    ci:\n      low: 8.3\n      high: 13.0\n      level: 0.95\n      unit: Hz\n    n: 9 rats\n  expected:\n  - quantity: mean HFPO centre frequency\n    value: 10.7\n    tolerance: 2.4\n    unit: Hz\n  criterion: >-\n    Tolerance is the half-width of the printed 95% CI (the larger side). Same cycles and rat\n    means as table1-minimum-pressure. The paper does not say how the centre frequency is\n    estimated. Readings (a) the frequency of the largest peak of the power spectrum of the\n    pressure during the oscillation period, between 3 and 30 Hz, (b) the number of oscillation\n    peaks per second over that period. The oscillation period is the stretch of elevated\n    pressure in the voiding contraction (Figure 3B2 legend). Reproduced when the mean lies within\n    the printed CI under one reading; both are shown.\n- id: table1-comparable-to-published\n  statement: Voiding parameters after array implantation were comparable to published values\n    in naive rats, including Wiedmann et al. (2020) for threshold pressure, peak pressure,\n    contraction duration and inter-void interval.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 2; Table 1; Figure 3C legend\n  quote: These urodynamic parameters were comparable to published values ( Zhao et al., 2010 ;\n    Andersson et al., 2011 ; Fraser et al., 2020 ; Wiedmann et al., 2020 )\n  data: with_inputs\n  depends_on:\n  - table1-threshold-pressure\n  - table1-peak-pressure\n  - table1-contraction-duration\n  - table1-intervoid-interval\n  criterion: >-\n    The paper reports no test; Table 1 sets each mean and 95% CI beside those of Wiedmann et\n    al. (2020, n = 6 rats; threshold 4.5, 1.8 to 7.3 mmHg; peak 44.6, 15.3 to 74 mmHg; duration\n    37.2, 25.1 to 49.3 s; interval 8, 5.3 to 10.6 min), so the comparison is judged as the table\n    makes it. Reproduced when, for each of the four parameters, the 95% CI computed here\n    overlaps the Wiedmann CI printed in Table 1; partially reproduced for two or three.\n- id: stim-evoked-voiding\n  statement: Stimulation delivered at a partial fill was immediately followed by voiding in\n    seven of eight rats, repeated in 3 to 6 cycles in six of these.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 2; Figure 3A, 3B and 3D\n  quote: When delivered during this partly filled state, electrical stimulation of the pelvic\n    nerve was immediately followed by post-stimulation voiding (urine release) in seven of eight\n    rats and was repeated in 3–6 cycles in six of these rats\n  expected:\n  - quantity: rats with stimulus-evoked voiding\n    value: 7\n    tolerance: 0\n    unit: rats of 8\n  - quantity: rats with evoked voiding in 3 to 6 cycles\n    value: 6\n    tolerance: 0\n    unit: rats\n  criterion: >-\n    Counts of rats are exact. A response is a void when urine is visibly excreted (Methods,\n    Bladder Pressure Responses), so the classification needs the experimenters' annotation of\n    each stimulation; when the data hold none, the claim cannot be tested from pressure alone\n    and is blocked. \"Immediately followed\" is read as a void within 30 s of stimulation, the\n    window the Discussion uses (paragraph 5); the end of the 10-s train or its onset as the\n    start of the window are both shown. The eight rats are those with stimulation after\n    habituation.\n- id: stim-void-trials\n  statement: In 27 trials across eight rats a void was observed within 30 s of stimulation.\n  source: Discussion, paragraph 5\n  quote: we consider it unlikely that in the 27 trials in eight rats where we observed a void\n    within 30 s of our stimulation this was always the case\n  depends_on:\n  - stim-evoked-voiding\n  expected:\n  - quantity: stimulation trials followed by a void within 30 s\n    value: 27\n    tolerance: 2.7\n    unit: trials\n  criterion: >-\n    Tolerance 10%. Voids as annotated in the data (see stim-evoked-voiding); window starts at\n    (a) train onset or (b) train end. Reproduced when the count is within tolerance under one\n    reading.\n- id: stim-early-void\n  statement: In two rats the stimulus-evoked void occurred very early in the normal void cycle.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 2; Figure 3A and 3B1\n  quote: in two rats stimulus evoked voiding was even more clearly demonstrated by the pelvic\n    nerve induced void occurring very early in the normal void cycle\n  depends_on:\n  - stim-evoked-voiding\n  - table1-intervoid-interval\n  criterion: >-\n    The paper gives no cut-off for \"very early\". Readings (a) an evoked void less than half the\n    rat's mean unstimulated inter-void interval after the previous void (below the 50 to 80%\n    fill the experimenters targeted), (b) less than a quarter of it. Reproduced when at least\n    two rats have such a void under one reading.\n- id: stim-nonvoiding\n  statement: Stimulation also produced non-voiding bladder pressure responses, without urine\n    release, in six of eight rats.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 3; Figure 3D\n  quote: Electrical stimulation of the pelvic nerve also produced non-voiding bladder pressure\n    responses (not accompanied by release of urine) in six of eight rats\n  expected:\n  - quantity: rats with evoked non-voiding contractions\n    value: 6\n    tolerance: 0\n    unit: rats of 8\n  criterion: >-\n    Classification as in stim-evoked-voiding, from the experimenters' annotation of urine\n    release. Where a response must be judged from pressure, the paper gives no amplitude\n    criterion; readings (a) a rise in bladder pressure after the train above the pre-train\n    baseline by more than the relative threshold pressure of that rat, (b) any annotated eNVC.\n    Reproduced when exactly six of eight rats show a non-voiding response.\n- id: stim-voiding-to-nonvoiding\n  statement: Within sessions with both responses, evoked voids were common early and became\n    less frequent as the session went on, while non-voiding pressure changes became more common.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 3\n  quote: it was common to observe stimulus evoked voiding contractions early in the experimental\n    session, but as the session progressed, voiding responses became less frequent and\n    non-voiding pressure changes become more common\n  depends_on:\n  - stim-evoked-voiding\n  - stim-nonvoiding\n  criterion: >-\n    The paper reports no measure or test. Fixed here from the sentence: in each rat with both\n    evoked voids and eNVCs, the mean stimulation time of the voids is earlier than that of the\n    eNVCs. Reproduced when this holds in more than half of those rats; the per-rat order is\n    shown.\n- id: fig3e-eight-week-responses\n  statement: In both rats implanted for 8 weeks, stimulation produced both voiding and\n    non-voiding responses, and the parameters of filling-evoked and stimulation-evoked voids\n    were similar to those of rats implanted for a shorter time.\n  source: Results, Urodynamic Effects of Pelvic Nerve Array Implantation and Stimulation in\n    Awake Rats, paragraph 4; Figure 3E\n  quote: In both cases, stimulation produced both voiding (indicated in as “eV” in Figure 3E )\n    and non-voiding responses (indicated in as “eNVC” in Figure 3E ) during cystometry ...\n    The urodynamic parameters of filling evoked voids and stimulation evoked voids where similar\n    to those in rats implanted for the shorter duration\n  depends_on:\n  - table1-minimum-pressure\n  criterion: >-\n    Classification as in stim-evoked-voiding. The paper gives no test for \"similar\"; fixed here\n    from Table 1 as the comparison it offers. Reproduced when both 8-week rats show at least one\n    evoked void and one eNVC, and their mean parameters (Table 1 definitions and readings) lie\n    within the range of the per-rat means of the short-term rats widened by 10% of each bound,\n    for at least four of the six parameters.\n- id: fig4-atf3-rare\n  statement: ATF3-positive neuronal nuclei were absent or rare in L6 and S1 DRG and in the MPG\n    ipsi- and contralateral to the array 50 days after implantation, while numerous in archived\n    axotomised positive controls.\n  source: Results, Immunohistochemical Analysis of Neural Injury Markers in Ganglia, paragraphs 1\n    and 2; Figure 4A to 4D\n  quote: ATF3-positive neuronal nuclei were absent or rare in sections taken from ganglia either\n    ipsi- or contralateral to the implant ... very few or no ATF3-positive neuronal nuclei (\n    Figure 4C ) were seen in sections from MPG ipsi- or contralateral to the array\n  criterion: >-\n    Sections were assessed qualitatively (Methods). Reproduced when the images or annotations in\n    the data show no more than a few ATF3-positive nuclei per section in implanted-animal DRG\n    and MPG, and many in the control ganglia. The paper fixes no count; \"a few\" is read as at\n    most 5 per section, a choice made here.\n- id: fig4ef-axons-intact\n  statement: CGRP-positive sensory axons traversed ipsi- and contralateral MPG, and\n    synaptophysin-positive boutons surrounded the entire population of MPG neurons on both sides\n    after 50 days of implantation.\n  source: Results, Immunohistochemical Analysis of Neural Injury Markers in Ganglia, paragraph\n    3; Figure 4E and 4F\n  quote: many axons were observed to traverse both ipsi- and contralateral MPG ( Figure 4E ) ...\n    We found that following 50 days implantation of the device, synaptic boutons innervated the\n    entire population of MPG neurons, ipsilateral and contralateral to the surgery\n  criterion: >-\n    Qualitative assessment (Methods). Reproduced when the data's images or annotations show\n    CGRP-positive axons in the MPG on both sides and synaptophysin boutons around MPG neurons on\n    both sides.\n- id: fig5-cfos-distribution\n  statement: After cystometry and stimulation, c-Fos-positive neurons in L5 to S1 were most\n    dense in the dorsal horn, the sacral dorsal commissural nucleus and the sacral preganglionic\n    nucleus of L6 and S1.\n  source: Results, Immunohistochemical Analysis of Noxious Neuronal Activity in Spinal Cord,\n    paragraph 1; Figure 5A to 5C\n  quote: In spinal segments L5-S1, neurons with c-Fos + nuclei were most densely distributed in\n    dorsal horn, the sacral dorsal commissural nucleus (SDCom) and the SPN of segments L6 and S1\n  criterion: >-\n    From the per-section counts of c-Fos+ neurons by region, segment and side (Methods). The\n    paper does not normalise by region area; readings (a) raw counts per region, (b) counts per\n    unit area where areas are given. \"Dorsal horn\" is laminae I to IV (1Sp to 4Sp). Reproduced\n    when, summed over the three rats, the dorsal horn, SDCom and SPN (L6 and S1) rank above the\n    other regions (laminae V to VIII and X) under one reading.\n- id: fig5-cfos-no-side-difference\n  statement: c-Fos-positive neuron counts did not differ between the implanted and stimulated\n    side and the contralateral side of the lumbosacral cord.\n  source: Results, Immunohistochemical Analysis of Noxious Neuronal Activity in Spinal Cord,\n    paragraph 1; Figure 5C and 5D legends\n  quote: No difference was detected in the pattern of c-Fos between the two sides of the spinal\n    cord ( Figure 5D )\n  criterion: >-\n    A claim of absence, judged on the paper's test (Statistics section). Exact Welch two-sample\n    t-tests of counts per rat, implanted side against contralateral side (n = 3 rats), with the\n    Hommel correction across the comparisons. The family is not stated; readings (a) one test\n    per region, counts summed over segments L5 to S2; (b) one test per region and segment.\n    Reproduced when no Hommel-adjusted P is below 0.05 under the reading run; both readings are\n    shown with the mean differences and CIs, and a paired t-test is shown as a variant.\n- id: fig5-no-lamina1\n  statement: No activation of lamina I neurons was detected on either the stimulated side or the\n    contralateral side.\n  source: Results, Immunohistochemical Analysis of Noxious Neuronal Activity in Spinal Cord,\n    paragraph 1; Figure 5C; Discussion, paragraph 4\n  quote: No activation of lamina I neurons was detected in either the stimulated side (array\n    implanted on the pelvic nerve) or the contralateral side\n  criterion: >-\n    From the c-Fos counts in lamina I (1Sp). The paper gives no threshold for activation.\n    Readings (a) zero c-Fos+ lamina I neurons in every section, (b) lamina I counts per section\n    no higher than the lowest of the other dorsal horn laminae (2Sp to 4Sp). Reproduced under\n    either reading; the counts are shown.\n- id: macroscopic-no-pathology\n  statement: At euthanasia no infection, irritation or inflammation was seen around the\n    connector, cable or array; a thin fibrous capsule formed around the array without spreading,\n    and the prostate, pelvic nerve and vessels were undamaged.\n  source: Results, Post-mortem Analysis of Pathology After Chronic Implantation of Pelvic Nerve\n    Array, paragraph 1\n  quote: A thin fibrous tissue encapsulation had formed around the array further stabilizing the\n    device ... Suturing of the electrode array to the soft tissue overlying the prostate had not\n    caused any macroscopic damage to the prostate, pelvic nerve or blood vessels\n  criterion: >-\n    Visual post-mortem examination. Reproduced when the data hold post-mortem notes for the\n    implanted rats and none records infection, inflammation or damage.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/payne-2020.yaml paper/10.3389-fnins.2020.619275.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" claims/payne-2020.yaml; grep -c "criterion:" claims/payne-2020.yaml; grep -c "statistics:" claims/payne-2020.yaml
```

```
31
9
```

**Agent**

I wrote `claims/payne-2020.yaml`, and the quote checker passes it: 31 claims, 25 quotes, 15 statistical values, 0 problems.

**Text read:** the version of record from Europe PMC (PMC7773906, JATS XML): main text, Methods, Table 1, figure legends and Discussion. The paper has no supplement and no PDF was supplied, so I read no figure pages. It links no code; its Data Availability says data come from the authors on request. No method detail is settled by code. I did not open any of the dataset's files.

**Claims:** 31 in all.
- **Quotes:** 25 have one. The 6 Table 1 values have an `inferred` note instead, because no sentence in the text states them.
- **Statistics:** 9 claims carry them. These are the Friedman tests (anaesthetised P = 0.039 and awake P = 0.039), Dunn's test (P = 0.034) and the six 95% CIs from Table 1.
- **Criteria:** all 31 claims have one.
- **Topics covered:**
  - ECAP latencies, conduction velocities and thresholds, anaesthetised and awake
  - electrode impedance and open circuits
  - colonic pressure
  - the Table 1 voiding values and their comparison with Wiedmann et al. (2020)
  - evoked voids (7 of 8 rats, 27 trials) and non-voiding contractions (6 of 8 rats)
  - the 8-week rats
  - ATF3, CGRP and synaptophysin staining
  - the c-Fos distribution, no difference between sides, and no lamina I activation
  - post-mortem findings

**Details the paper leaves open, with the readings named:**
- **Conduction distance:** 2.85 mm (pair centre to pair centre), 2.10 mm (E2 to E3) or 3.60 mm (E1 to E4).
- **Latency:** measured from pulse onset or pulse end, at 2 mA, at the lowest current where all three peaks pass threshold, or as the mean over currents above P3 threshold.
- **Threshold amplitude and step:** amplitude as peak to baseline or peak to trough; threshold at the 0.1 mA step or interpolated between steps. The printed values are not multiples of 100 µA.
- **Central value:** mean or median. The Results say "mean" but the Statistics section says median and IQR.
- **Awake Friedman test groups:** one test over all six groups, one test per population, or week as the factor.
- **Awake pooling:** both weeks pooled, rats averaged over weeks, or week 0 alone.
- **Dunn's P:** unadjusted or Bonferroni-adjusted.
- **Urodynamic definitions:** threshold pressure at contraction onset or at urine release; contraction duration from onset to return to baseline, or time above threshold. The 9-rat mean is taken over per-rat means or over all cycles pooled. HFPO centre frequency is the spectral peak or a count of oscillation peaks.
- **"Immediately followed by a void":** within 30 s (the window the Discussion uses), timed from train onset or train end.
- **"Very early" in the void cycle:** under half, or under a quarter, of the rat's inter-void interval.
- **c-Fos Welch tests with Hommel correction:** one test per region with segments summed, or one per region and segment. A paired test is shown as a variant.
- **Lamina I "no activation":** zero counts, or counts no higher than laminae II to IV.

**Fixed by me because the paper gives no method or test:** the rule for a colonic response, "similar" for the 8-week rats, the order from voiding to non-voiding within a session, "comparable" to published values (judged as overlapping CIs), and the cut-off for "rare" ATF3 nuclei. Each criterion says the choice was mine.

**Inconsistencies in the paper, recorded for the author:**
- The awake ECAP cohort is three rats in the Methods but n = 4 in the Results.
- The kind of ± spread (SD or SEM) is not named for the awake thresholds or the impedances.
- The c-Fos session is 60 min in the Results and 2 h in the Methods.
- The P2 threshold range (595 to 648 µA) has its central value as its upper bound.

**Missing:** nothing the claims needed. Evoked voids are classified by visible urine, and the histology and observation findings were only seen by eye. Those claims can only be tested if the dataset holds the experimenters' annotations or images; otherwise they will be blocked.

## End of run

17 turns, 4 minutes, $1.31 at API prices, result: success.
