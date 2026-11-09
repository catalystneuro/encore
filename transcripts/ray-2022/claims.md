# crcns-nac-1 · claims · run 42157068421

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/crcns-nac-1 2>&1; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ paper/ claims/crcns-nac-1 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 185
}
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
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

**Agent calls Bash**

```bash
ls claims/; ls claims/crcns-* 2>/dev/null | head; cat docs/archives.md | sed -n '1,200p' | grep -n -i -A5 crcns | head -60; wc -l paper/*.txt; head -30 paper/10.1523-jneurosci.1107-21.2021.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1107-21.2021.txt",
 "offset": 30,
 "limit": 760
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1107-21.2021.txt",
 "offset": 790,
 "limit": 740
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/nac-1.data-description.txt; head -60 claims/crcns-bf-1/*.yaml; cat tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,120p paper/nac-1.data-description.txt | cut -c1-300
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,380p paper/nac-1.data-description.txt | grep -v "^\s*$" | cut -c1-200 | sed -n '60,260p'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -sL -m 30 http://mcdannaldlab.org/resources | sed 's/<[^>]*>/ /g' | grep -v "^\s*$" | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 https://www.mcdannaldlab.org/ | grep -o 'href="[^"]*"' | sort -u | head -40; curl -sL -m 30 -o /dev/null -w "%{http_code}\n" https://www.mcdannaldlab.org/resources
```

Result: the fetched text is not kept.

**Agent**

The paper's linked code page (mcdannaldlab.org/resources) returns 404, so there is no code to read. Now checking the CRCNS file format and the checker.

**Agent calls Bash**

```bash
sed -n 1,45p claims/crcns-bf-1/*.yaml; grep -n "argv\|def \|data:\|kind" tools/claims_check.py | head -40
```

```
# Claims for Nair, Klaassen, Arato, Vyssotski, Harvey & Rainer (2018), PNAS 115:1352-1357, on
# CRCNS data set bf-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader, version pilot-13).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Results, figure legends and short Materials and Methods, and the supplement
# (pnas.201712431si.pdf: SI results on low-frequency power, unimodality, excursions and
# locomotion, SI Materials and Methods, and the legends of Figs. S1 to S7). The Methods that
# fix the analyses are in the SI Materials and Methods. The paper links no analysis code, so none
# was read; it names the toolboxes used (Wave_clus, CircStat, Chronux, BSMART, MVGC, SPSS). No PDF
# renderer was available, so figures were read from their legends and the Results only. The
# extracted text prints one p-value as "P < 0.0" (ACC gamma, Results, Gamma Oscillations in BF
# Cortical Projection Targets); it is recorded as printed.
#
# Data the paper used. Adult male Long Evans rats, 80 to 120 days old. 16 rats implanted with
# tungsten microelectrodes in the BF (AP -0.8, ML 2.8, DV -8.2 mm from bregma), 14 of them also in
# the VC and 8 in the ACC; 22 BF hemispheres in the group analyses; 4 more rats with bipolar BF
# electrodes. LFPs were recorded with a head-mounted Neurologger 2A (four LFP channels at 1.6 kHz,
# and a 3D accelerometer for movement), and in tethered recordings (TDT RZ5) LFP at 1.6 kHz with
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,110p tools/claims_check.py; grep -n "^dataset\|^  archive\|^  id\|^paper\|^schema" claims/crcns-bf-1/*.yaml
```

```
SAME = {"−": "-", "–": "-", "—": "-", "‐": "-", "‑": "-", "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", " ": " ", " ": " "}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in SAME.items():
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def flattenings(raw: str) -> list[str]:
    """The text with inline tags removed, with every tag as a space, and both without spaces."""
    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]


def quote_found(quote: str, texts: list[str]) -> bool:
    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 55,62p claims/crcns-bf-1/*.yaml; ls schemas* docs/*schema* 2>/dev/null; grep -rn "def schema" tools/*.py | head;
```

```
#   BF signal per rat and session, so tests run over rats (n = 6), with the two sessions of a
#   condition (a) averaged per rat, or (b) kept as separate pairs (session 1 with session 1).
schema_version: 2
dataset:
  archive: crcns
  id: bf-1
  doi: 10.6080/K0MK6B2Q
paper: doi:10.1073/pnas.1712431115
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
tools/entry.py:83:def schema(name: str) -> Draft202012Validator:
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
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
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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

**Agent**

Full text and Methods are present; the Extended Data figures (1-1, 1-2, 2-1) are not, and the lab's code page returns 404. Let me see how earlier files set tolerances from asymmetric CIs.

**Agent calls Bash**

```bash
grep -rn -B2 -A8 "ci:" claims/crcns-*/ claims/0016*/ 2>/dev/null | grep -n "tolerance\|ci:\|low\|high\|value\|criterion" | head -40; grep -rln "bootstrap" claims/ | head
```

```
3:claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml:580:    ci:
5:claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml-582-      low: -0.8432
6:claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml-583-      high: -0.0169
15:claims/001687/10.1016-j.neuron.2026.05.027.yaml:1397:    ci:
17:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1399-      low: 2.09
18:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1400-      high: 7.45
25:claims/001687/10.1016-j.neuron.2026.05.027.yaml:1407:    ci:
27:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1409-      low: -0.04
28:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1410-      high: 5.02
34:claims/001687/10.1016-j.neuron.2026.05.027.yaml:1416:    ci:
36:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1418-      low: 0.95
37:claims/001687/10.1016-j.neuron.2026.05.027.yaml-1419-      high: 3.85
claims/000011/10.1038-nature17643.yaml
claims/001084/10.1016-j.neuron.2023.12.011.yaml
claims/001687/10.1016-j.neuron.2026.05.027.yaml
claims/000015/10.1016-j.neuron.2017.05.005.yaml
claims/000688/10.1016-j.neuron.2018.09.030.yaml
claims/000252/10.1101-2022.12.07.22283227.yaml
claims/000552/10.1038-s41593-022-01138-x.yaml
claims/crcns-ret-1/10.1242-dev.027912.yaml
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 560,620p claims/crcns-ofc-4/10.1016-j.neuron.2016.08.019.yaml
```

```
p: 0.03
  - about: correlation of decoding with error rate, hippocampus and DLPFC
    test: Pearson correlation
    p: 0.14
    p_relation: ">"
  - about: similarity and error rate, hippocampus, DLPFC, FFA/PPA
    p: 0.17
    p_relation: ">"
  criterion: Needs the hippocampus, DLPFC and PPA/FFA ROIs (AAL labels, Methods), which the data
    set's description does not list.
- id: fig4a-decoding-error-correlation
  statement: Across participants, mean classification accuracy of the three hidden components in
    OFC correlates negatively with error rate.
  source: Results, paragraph 11; Figure 4A; Figure S4
  quote: participants’ average error rates were significantlycorrelated with themean
    classificationaccuracyofallthree hidden state components
  statistics:
  - test: Pearson correlation
    statistic: r = -0.58, t25 = -3.6
    p: 0.002
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1523-jneurosci.1107-21.2021.pdf')
for i in (5,6):
  d[i].get_pixmap(dpi=110).save(f'p{i+1}.png')
print(len(d))
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
which pdftoppm mutool gs magick convert 2>/dev/null; python -c "import pypdfium2" 2>&1 | tail -1
```

```
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1107-21.2021.pdf",
 "pages": "6"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

No PDF renderer is available, so figures are read from legends and Results only. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml",
 "content": "# Claims for Ray, Moaddab & McDannald (2022), J Neurosci 42:817-833, on CRCNS data set nac-1.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-06,\n# protocol as stated in docs/protocol.md (Reader, version pilot-13).\n#\n# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF):\n# Introduction, Materials and Methods, Results, figure legends and Discussion. The Extended Data\n# (Figures 1-1, 1-2 and 2-1: per-rat suppression ratios, session by session suppression ratios,\n# and the alternative clustering heat plots) are not under paper/ and were not read. No claim\n# below rests on them alone; the Results state the numbers the claims use. No PDF renderer was\n# available, so figures were read from their legends and the Results only; the value of the\n# narrow/wide waveform boundary (dashed line, Figure 3C) could not be read. The extracted text\n# prints minus signs and the \"x 10^\" of p-values as a replacement character; values below are\n# recorded as the paper prints them (for example \"p = 6.00 x 10^-5\" as 6.0e-5).\n#\n# Code: the paper links no analysis code for the neural analyses. It says the Med Associates\n# programs and the MATLAB programs for behavioral analyses are at http://mcdannaldlab.org/resources;\n# that page returned 404 on 2026-11-06 (and https://www.mcdannaldlab.org/resources as well), so no\n# code was read. The data set's own sample scripts are part of the data set and were not read.\n#\n# Data the paper used. Seven adult female Long-Evans rats, food restricted to 85% of free-feeding\n# weight, nose poking on a VI-60 schedule for food pellets throughout. Pavlovian fear\n# discrimination: three 10-s auditory cues, each with a footshock probability (0.5 mA, 0.5 s, 2 s\n# after cue offset): danger p = 1.00, uncertainty p = 0.25, safety p = 0.00. Sessions of 16 trials\n# (4 danger, 2 uncertainty shock, 6 uncertainty omission, 4 safety), mean ITI 3.5 min, each trial\n# a 20-s baseline then the 10-s cue. Eight sessions before surgery (Figure 1C), then single-unit\n# recording from 16-wire drivable bundles in the nucleus accumbens core (Plexon OmniPlex, units\n# sorted offline in Offline Sorter). 368 NAcc units from 95 recording sessions; 193 cue-responsive\n# units from 82 sessions; the three main populations (172 units) from 79 sessions. Measured\n# variables: spike times, nose pokes, pellet feeder advances (rewards), cue and shock times, mean\n# waveforms. The fear measure is the suppression ratio of nose poking.\n#\n# The CRCNS data set, by its title and data description, holds the NAcc recordings of this paper:\n# 368 single units from 95 behavior sessions of 7 female rats, one MATLAB file per unit, with\n# nose poke, suppression ratio, firing and waveform data organized by the 16 trials of a session.\n# Whether it holds the eight pre-surgery sessions (Figure 1C), pellet and nose poke times in the\n# ITI (Figures 9 and 10), and the paper's own population labels is for the author to find.\n#\n# Method details from the Methods, used by every claim below unless it says otherwise:\n# - Suppression ratio per trial: (baseline poke rate - cue poke rate) / (baseline poke rate + cue\n#   poke rate), baseline the 20 s before cue onset, cue the 10-s cue, using that trial's baseline.\n# - Cue-responsive screen: per unit, mean firing (Hz) in the 10 s before cue onset against the\n#   first 1 s and against the last 5 s of each cue, paired two-tailed t-test, p < 0.05, no\n#   correction; a unit is cue responsive if any cue in either window differs.\n# - Normalized firing: per unit and trial type, firing in 250-ms bins from 20 s before cue onset to\n#   20 s after cue offset (200 bins), averaged over the trials of the type; the mean of the 10 s\n#   before cue onset of that trial type subtracted from each bin; then z-scored across all trial\n#   types of the unit together (mean 0, SD 1 over all bins).\n# - Cue firing ANOVA: cue (danger, uncertainty, safety) by interval (48 bins of 250 ms, 2 s before\n#   cue onset to cue offset), within units; uncertainty shock and omission trials collapsed.\n#   Onset is the first 1 s of the cue, late cue the last 5 s.\n# - 95% bootstrap CIs: MATLAB bootci, studentized, 1000 resamples of the mean over units (or\n#   rats); a difference is found when the CI excludes zero, and absent when it contains zero.\n#\n# Details the paper leaves open that apply to many claims, with the readings it allows:\n# - Trial types in the z-score: (a) four (danger, uncertainty shock, uncertainty omission,\n#   safety), as the session design has; (b) three, with uncertainty collapsed.\n# - Collapsing uncertainty: (a) the mean over all eight uncertainty trials; (b) the mean of the\n#   shock and omission trial-type traces.\n# - Population labels: the paper's labels come from its k-means clustering (fig2-five-clusters).\n#   (a) If the data set holds the paper's population labels, the population claims use them;\n#   (b) the populations of the reproduced clustering are run as a variant, or as the only\n#   reading when no labels are held.\n# - Per-trial normalized firing (tuning curve, fear output regression): the Methods give the\n#   normalization only for trial-type means. (a) Each trial's firing minus that trial's 10-s\n#   pre-cue mean, divided by the unit's SD from the normalization above; (b) the same, with the\n#   trial-type baseline subtracted; (c) each trial's binned firing z-scored over all trials and\n#   bins of the unit.\n# - Suppression ratio when a trial has no pokes in baseline or cue (0/0): (a) the trial is left\n#   out; (b) the ratio is set to 0.\n# - The data set's units are rows of one structure; session-level behavior is repeated for every\n#   unit of a session. Behavior claims count each session once.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: nac-1\n  doi: 10.6080/K0M906VB\npaper: doi:10.1523/jneurosci.1107-21.2021\nclaims:\n- id: units-recorded\n  statement: 368 NAcc single units were recorded from seven rats over 95 fear discrimination\n    sessions.\n  source: Results, NAcc neurons show heterogeneous cue firing is preceded by Results, paragraph 3\n    (after Figure 2 legend)\n  quote: A total of 368 NAcc single units were recorded from seven rats over 95 fear discrimination\n    sessions\n  expected:\n  - quantity: NAcc single units\n    value: 368\n    tolerance: 0\n  - quantity: recording sessions\n    value: 95\n    tolerance: 0\n  - quantity: rats\n    value: 7\n    tolerance: 0\n  criterion: Counts of units, distinct sessions (rat and date) and rats in the data set. These are\n    counts of what was deposited, so the tolerance is zero.\n- id: cue-responsive-193\n  statement: The cue-responsive screen identified 193 units (about 53% of all units) from 82\n    sessions, with at least seven cue-responsive units in each rat.\n  source: Results, paragraph 3 (the paragraph beginning \"A total of 368 NAcc single units\")\n  quote: This screen identified 193 cue-responsive single units (;53% of all units recorded) from\n    82 sessions, with at least seven cue-responsive single units identified in each rat\n  depends_on:\n  - units-recorded\n  expected:\n  - quantity: cue-responsive units\n    value: 193\n    tolerance: 19.3\n  - quantity: sessions with a cue-responsive unit\n    value: 82\n    tolerance: 8.2\n  - quantity: minimum cue-responsive units per rat\n    value: 7\n    tolerance: 0.7\n  criterion: The screen of the Methods (Identifying cue-responsive neurons), as in the opening\n    comment. The t-test pairs, for each trial, the 10-s baseline mean with the cue-window mean\n    (paired, as the Methods say). Which trials form the uncertainty cue is open; (a) all eight\n    uncertainty trials, as the cue analyses collapse them; (b) shock and omission trials tested\n    as separate cues. Reproduced when, under one reading, all three counts are within\n    tolerance.\n- id: fig1c-acquisition\n  statement: Over the eight pre-surgery sessions rats acquired discrimination, with high\n    suppression to danger, intermediate to uncertainty and low to safety; ANOVA found a main\n    effect of cue and a cue by session interaction.\n  source: Results, paragraph 1; Figure 1C\n  quote: Rats acquired discrimination over the first eight sessions, showing high suppression in\n    response to danger, intermediate suppression in response to uncertainty, and low suppression in\n    response to safety (Fig. 1C)\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, cue by session\n    statistic: F(2,12) = 24.49\n    p: 6.0e-5\n    n: 7 rats\n  - about: cue by session interaction\n    test: ANOVA, cue by session\n    statistic: F(14,84) = 4.57\n    p: 5.0e-6\n    n: 7 rats\n  criterion: Per rat and pre-surgery session, the mean suppression ratio of each cue over its\n    trials (uncertainty trials pooled); repeated-measures ANOVA with cue (3) and session (1 to 8)\n    as within-rat factors, as the Methods (Calculating suppression ratios) say. Reproduced when\n    the cue main effect and the cue by session interaction both have p < 0.05 and, in session 8,\n    the mean over rats is ordered danger > uncertainty > safety. Needs the eight pre-surgery\n    sessions, which the data set's description (95 recording sessions) may not hold.\n- id: fig1g-discrimination\n  statement: During the recording sessions all rats discriminated the cues, with suppression\n    ratios highest to danger, intermediate to uncertainty and lowest to safety; every cue pair\n    differed.\n  source: Results, paragraph 4 (beginning \"Rats showed complete discrimination\"); Figure 1G\n  quote: Suppression ratios were high in response to danger, intermediate in response to\n    uncertainty, and low in response to safety. ANOVA for mean individual suppression ratio\n    revealed a main effect of cue\n  statistics:\n  - about: main effect of cue\n    test: ANOVA\n    statistic: F(2,12) = 57.41\n    p: 7.18e-7\n    n: 7 rats\n  - about: danger minus uncertainty suppression ratio\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.16\n      high: 0.29\n    n: 7 rats\n  - about: uncertainty minus safety suppression ratio\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.35\n      high: 1.03\n    n: 7 rats\n  - about: danger minus safety suppression ratio\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.5\n      high: 1.25\n    n: 7 rats\n  expected:\n  - quantity: mean differential suppression ratio, danger minus uncertainty\n    value: 0.21\n    tolerance: 0.05\n  - quantity: mean differential suppression ratio, uncertainty minus safety\n    value: 0.47\n    tolerance: 0.12\n  - quantity: mean differential suppression ratio, danger minus safety\n    value: 0.69\n    tolerance: 0.19\n  criterion: Per rat, the mean suppression ratio of each cue over the trials of the chosen\n    sessions; repeated-measures ANOVA on cue (n = 7 rats); studentized bootstrap 95% CIs (1000\n    resamples) of the per-rat differences, as in the Methods. Tolerances are the distance from\n    each mean to the nearer bound of the paper's CI. Which sessions is open; (a) the 82 sessions\n    with a cue-responsive unit, as the Results say; (b) all 95 recording sessions; (c) the 79\n    sessions of the three main populations. Reproduced when, under one reading, the cue effect\n    has p < 0.05, every CI excludes zero and the three means are within tolerance; partially\n    reproduced when the ANOVA and all three CIs hold but a mean is out of tolerance.\n- id: fig1h-poke-rate-unrelated\n  statement: Baseline nose poke rate was unrelated to suppression to any cue and to overall\n    discrimination (danger minus safety suppression ratio).\n  source: Results, paragraph 5 (beginning \"To reveal possible relationships\"); Figure 1H\n  quote: There was no relationship between baseline nose poke rate and suppression in response to\n    any cue or to overall discrimination\n  statistics:\n  - test: Pearson correlation\n    p: 0.06\n    p_relation: \">\"\n    n: 7 rats\n  depends_on:\n  - fig1g-discrimination\n  criterion: A claim of absence, judged on the paper's test. Per rat, the mean baseline poke rate\n    (20 s before cue onset) and the mean suppression ratios of fig1g-discrimination (same session\n    readings); Pearson correlation of baseline rate with danger, uncertainty and safety\n    suppression and with danger minus safety (n = 7). Reproduced when no correlation has p <\n    0.05; not reproduced when any does. The R values are reported either way (paper, all |R| <\n    0.73).\n- id: fig1h-discrimination-safety\n  statement: Overall discrimination was largely the product of low safety suppression; it\n    correlated negatively with the safety suppression ratio across rats.\n  source: Results, paragraph 5; Figure 1H\n  quote: Discrimination was largely the product of reduced safety suppression ratios. In support,\n    there was a significant negative relationship between overall discrimination and safety\n    suppression ratio\n  statistics:\n  - test: Pearson correlation\n    statistic: R = -0.98\n    p: 1.41e-4\n    n: 7 rats\n  depends_on:\n  - fig1g-discrimination\n  expected:\n    quantity: Pearson R, danger minus safety suppression against safety suppression\n    value: -0.98\n    tolerance: 0.098\n  criterion: As fig1h-poke-rate-unrelated, the Pearson correlation across the seven rats of\n    danger minus safety suppression ratio with safety suppression ratio. Reproduced when R is\n    negative with p < 0.05 and within tolerance.\n- id: fig2-five-clusters\n  statement: K-means clustering of the 193 cue-responsive units on six firing epochs (onset and\n    late cue firing to each cue) gave five functional populations; Threat Excited (5), Threat\n    Inhibited (26), Danger Excited (55), Bidirectional Valence (91) and Non-Selective (16).\n  source: Results, NAcc neurons show heterogeneous cue firing, paragraphs 1 and 2; Figure 2 legend\n  quote: We applied k-means clustering to the matrix and found that five clusters grouped similar\n    functional types\n  depends_on:\n  - cue-responsive-193\n  expected:\n  - quantity: Threat Excited units\n    value: 5\n    tolerance: 0.5\n  - quantity: Threat Inhibited units\n    value: 26\n    tolerance: 2.6\n  - quantity: Danger Excited units\n    value: 55\n    tolerance: 5.5\n  - quantity: Bidirectional Valence units\n    value: 91\n    tolerance: 9.1\n  - quantity: Non-Selective units\n    value: 16\n    tolerance: 1.6\n  criterion: The 193 x 6 matrix of the Methods (K-means clustering), MATLAB kmeans with its\n    defaults (squared Euclidean distance, k-means++ starts), k = 5 as the paper reports choosing\n    it. The matrix entries are open; (a) mean normalized firing, as the Results say; (b) mean\n    firing in Hz, as the Methods say. The start is random and the paper gives no seed or number\n    of replicates; (i) the solution with the lowest summed distance over 100 starts; (ii) the\n    most frequent partition over 100 starts. Clusters are named from their centroids by the\n    Results' descriptions (Results, NAcc neurons show heterogeneous cue firing, paragraph 2):\n    Threat Excited and Threat Inhibited change equally to danger and uncertainty, less to\n    safety (up and down); Danger Excited increase most to danger; Bidirectional Valence\n    decrease most to danger; Non-Selective increase without differing between cues. Reproduced\n    when, under one reading, all five counts are within tolerance; partially reproduced when\n    the five named patterns appear but a count is out of tolerance. The cluster number rule\n    (fewest clusters with smallest mean distance, k from 1 to 7) is shown as a variant, with\n    the mean distance at each k.\n- id: populations-by-rat\n  statement: Threat Excited units came from two of seven rats (four from one rat), Threat\n    Inhibited from four rats, Danger Excited from six and Bidirectional Valence from all seven;\n    the three main populations (172 units) came from 79 sessions.\n  source: Results, NAcc neurons show heterogeneous cue firing, paragraph 2\n  quote: Threat Excited neurons (n = 5) were observed in only two of seven subjects, with four\n    single units coming from one subject\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: rats with Threat Excited units\n    value: 2\n    tolerance: 0\n  - quantity: rats with Threat Inhibited units\n    value: 4\n    tolerance: 0\n  - quantity: rats with Danger Excited units\n    value: 6\n    tolerance: 0\n  - quantity: rats with Bidirectional Valence units\n    value: 7\n    tolerance: 0\n  - quantity: sessions of the three main populations\n    value: 79\n    tolerance: 7.9\n  criterion: Counts of distinct rats and sessions among the units of each population, under the\n    population readings of the opening comment. Rat counts are small integers, so they must\n    match exactly. Reproduced when all counts match.\n- id: most-units-threat\n  statement: Most cue-responsive NAcc units showed their greatest firing change to the\n    shock-associated cues, danger and uncertainty.\n  source: Discussion, paragraph 1; Results, NAcc neurons show heterogeneous cue firing,\n    paragraph 2\n  quote: \"most NAcc neurons showed the greatest firing changes in response to the shockassociated\n    cues: danger and uncertainty\"\n  depends_on:\n  - fig2-five-clusters\n  criterion: The paper rests this on its cluster counts; the four populations with differential\n    cue firing (Threat Excited, Threat Inhibited, Danger Excited, Bidirectional Valence) are 177\n    of 193 units, and Non-Selective units do not differ between cues. Reproduced when these\n    four populations hold more than half of the cue-responsive units.\n- id: fig3ab-rate-cv-unimodal\n  statement: Across the 172 units of the three main populations, baseline firing rate and\n    coefficient of variance had unimodal distributions.\n  source: Results, NAcc neurons show heterogeneous cue firing, paragraph 3; Figure 3A and 3B\n  quote: we observed unimodal distributions for baseline firing rate\n  statistics:\n  - about: baseline firing rate\n    test: Hartigan's Dip Statistic\n    statistic: dip = 0.013\n    p: 1.0\n    n: 172 units\n  - about: coefficient of variance\n    test: Hartigan's Dip Statistic\n    statistic: dip = 0.016\n    p: 0.99\n    n: 172 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: A claim of absence, judged on the paper's test. Baseline rate is the mean firing in\n    the 10 s before cue onset (Methods, Firing and waveform characteristics); which trials are\n    averaged is not said, and all 16 trials are used. The coefficient of variance is the SD\n    over the mean of the interspike intervals; the spikes it uses are not said, and the paper's\n    text allows (a) the 10-s baseline periods, as the Results say these measures were taken\n    while rats poked for food, and (b) the whole session. Hartigan's dip test with a p-value by\n    bootstrap from the uniform distribution (the paper does not name its implementation).\n    Reproduced when neither distribution has p < 0.05; not reproduced when either does.\n- id: fig3c-waveform-bimodal\n  statement: Waveform peak-valley duration was bimodal across the 172 units; Threat Inhibited\n    units were mostly wide (bimodal only at an uncorrected p), Danger Excited units unimodal and\n    mostly narrow, and Bidirectional Valence units bimodal with about half narrow and half wide.\n  source: Results, NAcc neurons show heterogeneous cue firing, paragraphs 3 and 4; Figure 3C\n  quote: we observed a bimodal distribution for waveform peak- valley duration across all 172\n    neurons\n  statistics:\n  - about: all 172 units\n    test: Hartigan's Dip Statistic\n    p: 0\n    n: 172 units\n  - about: Threat Inhibited\n    test: Hartigan's Dip Statistic\n    statistic: dip = 0.096\n    p: 0.035\n    n: 26 units\n  - about: Danger Excited\n    test: Hartigan's Dip Statistic\n    statistic: dip = 0.06\n    p: 0.18\n    n: 55 units\n  - about: Bidirectional Valence\n    test: Hartigan's Dip Statistic\n    statistic: dip = 0.11\n    p: 0\n    n: 91 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: dip, Threat Inhibited\n    value: 0.096\n    tolerance: 0.0096\n  - quantity: dip, Danger Excited\n    value: 0.06\n    tolerance: 0.006\n  - quantity: dip, Bidirectional Valence\n    value: 0.11\n    tolerance: 0.011\n  criterion: Peak-valley duration is the time from the valley of the mean waveform to the\n    following peak (Methods, Firing and waveform characteristics); dip test as in\n    fig3ab-rate-cv-unimodal. The narrow/wide boundary is the dashed line of Figure 3C, whose\n    value could not be read here; it is taken as the lowest point of the 172-unit histogram\n    between its two modes, and the split is shown. Reproduced when the 172-unit and\n    Bidirectional Valence distributions have p < 0.05, Danger Excited has p >= 0.05 with most\n    units narrow, Threat Inhibited has most units wide, and Bidirectional Valence has between\n    40% and 60% narrow; partially reproduced when the dip tests hold but a split does not.\n    The dip values are reported against their tolerances.\n- id: fig4ab-thi-threat-firing\n  statement: Threat Inhibited units decreased firing more to danger and uncertainty than to\n    safety, both at cue onset and during late cue.\n  source: Results, NAcc populations show distinct danger and uncertainty firing patterns,\n    paragraph 1; Figure 4A and 4B\n  quote: Threat Inhibited neurons showed greater firing decreases in response to threat cues\n    (danger and uncertainty) compared with safety at onset\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, cue by interval\n    statistic: F(2,50) = 37.84\n    p: 9.83e-11\n    n: 26 units\n  - about: cue by interval interaction\n    test: ANOVA, cue by interval\n    statistic: F(94,2350) = 4.95\n    p: 7.61e-45\n    n: 26 units\n  - about: danger and uncertainty minus safety, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.63\n      high: -0.32\n    n: 26 units\n  - about: danger and uncertainty minus safety, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.6\n      high: -0.2\n    n: 26 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: mean differential normalized firing, threat minus safety, onset\n    value: -0.47\n    tolerance: 0.15\n  - quantity: mean differential normalized firing, threat minus safety, late cue\n    value: -0.44\n    tolerance: 0.16\n  criterion: Normalized firing and the cue by interval ANOVA as in the opening comment. Per unit,\n    the mean of danger and uncertainty minus safety in each window; studentized bootstrap 95%\n    CI over units. \"Danger and uncertainty\" is open; (a) the mean of the danger and uncertainty\n    window values; (b) danger and uncertainty trials pooled before averaging. Tolerances are\n    the distance to the nearer CI bound. Reproduced when the cue effect and the interaction\n    have p < 0.05, both CIs exclude zero and both means are within tolerance; partially\n    reproduced when the CIs exclude zero with a mean out of tolerance.\n- id: fig4b-thi-danger-equals-uncertainty\n  statement: Threat Inhibited firing decreases to danger and uncertainty did not differ, at onset\n    or during late cue.\n  source: Results, NAcc populations show distinct danger and uncertainty firing patterns,\n    paragraph 1; Figure 4B\n  quote: Firing decreases in response to danger and uncertainty did not differ at onset\n  statistics:\n  - about: danger minus uncertainty, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.11\n      high: 0.12\n    n: 26 units\n  - about: danger minus uncertainty, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.14\n      high: 0.12\n    n: 26 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: A claim of absence, judged on the paper's test, the studentized bootstrap 95% CI of\n    per-unit danger minus uncertainty normalized firing, at onset and late cue. Reproduced when\n    both CIs contain zero; not reproduced when either excludes it. The means are reported\n    (paper, -0.01 and -0.02).\n- id: fig4cd-de-danger-firing\n  statement: Danger Excited units fired most to danger and discriminated all three cues at\n    onset, and during late cue their firing was selective for danger over uncertainty and\n    safety.\n  source: Results, NAcc populations show distinct danger and uncertainty firing patterns,\n    paragraph 2; Figure 4C and 4D\n  quote: Firing was maximal in response to danger and fully discriminated the three cues at onset\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, cue by interval\n    statistic: F(2,106) = 13.05\n    p: 9.0e-6\n    n: 55 units\n  - about: cue by interval interaction\n    test: ANOVA, cue by interval\n    statistic: F(94,4982) = 2.23\n    p: 1.87e-10\n    n: 55 units\n  - about: danger minus uncertainty, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.11\n      high: 0.33\n    n: 55 units\n  - about: uncertainty minus safety, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.07\n      high: 0.33\n    n: 55 units\n  - about: danger minus mean of uncertainty and safety, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.07\n      high: 0.27\n    n: 55 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: danger minus uncertainty, onset\n    value: 0.22\n    tolerance: 0.11\n  - quantity: uncertainty minus safety, onset\n    value: 0.21\n    tolerance: 0.12\n  - quantity: danger minus mean of uncertainty and safety, late cue\n    value: 0.17\n    tolerance: 0.1\n  criterion: As fig4ab-thi-threat-firing. Reproduced when the cue effect and interaction have p\n    < 0.05, the three CIs exclude zero and the three means are within tolerance; partially\n    reproduced when the CIs exclude zero with a mean out of tolerance.\n- id: fig4ef-bv-danger-decrease\n  statement: Bidirectional Valence units, the most abundant population (about 47% of\n    cue-responsive units), decreased firing to danger more than to uncertainty and safety, at\n    onset and during late cue.\n  source: Results, NAcc populations show distinct danger and uncertainty firing patterns,\n    paragraph 3; Figure 4E and 4F\n  quote: Bidirectional Valence neurons showed danger firing decreases that exceeded uncertainty and\n    safety decreases at onset\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, cue by interval\n    statistic: F(2,178) = 8.90\n    p: 2.07e-4\n    n: 91 units\n  - about: cue by interval interaction\n    test: ANOVA, cue by interval\n    statistic: F(94,8366) = 1.45\n    p: 0.003\n    n: 91 units\n  - about: danger minus mean of uncertainty and safety, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.22\n      high: -0.03\n    n: 91 units\n  - about: danger minus mean of uncertainty and safety, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.16\n      high: -0.02\n    n: 91 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: danger minus mean of uncertainty and safety, onset\n    value: -0.13\n    tolerance: 0.09\n  - quantity: danger minus mean of uncertainty and safety, late cue\n    value: -0.09\n    tolerance: 0.07\n  - quantity: Bidirectional Valence share of cue-responsive units\n    value: 47\n    tolerance: 4.7\n    unit: percent\n  criterion: As fig4ab-thi-threat-firing. Reproduced when the cue effect and interaction have p\n    < 0.05, both CIs exclude zero and the means and share are within tolerance; partially\n    reproduced when the CIs exclude zero with a value out of tolerance.\n- id: fig4f-bv-safety-variability\n  statement: Bidirectional Valence units varied more in their safety onset firing than in their\n    danger or uncertainty onset firing.\n  source: Results, NAcc populations show distinct danger and uncertainty firing patterns,\n    paragraph 4; Figure 4F\n  quote: There was greater variability in onset safety firing compared with either danger\n    (Pitman-Morgan test, p=0.0087) or uncertainty onset firing\n  statistics:\n  - about: safety against danger onset firing variance\n    test: Pitman-Morgan test\n    p: 0.0087\n    n: 91 units\n  - about: safety against uncertainty onset firing variance\n    test: Pitman-Morgan test\n    p: 0.0046\n    n: 91 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: Per unit, normalized onset firing (first 1 s) to each cue; Pitman-Morgan test of\n    equal variances of paired values (safety against danger, safety against uncertainty), as the\n    Methods name it. Reproduced when both tests have p < 0.05 with the safety variance larger.\n- id: fig5ab-the-onset\n  statement: Threat Excited units increased firing more to danger and uncertainty than to safety\n    at onset, but not during late cue.\n  source: Results, Threat Excited and Non-Selective population, paragraph 1; Figure 5A and 5B\n  quote: Threat Excited neurons (Fig. 5A) showed greater firing increases to threat cues (danger\n    and uncertainty) compared with safety at onset\n  statistics:\n  - about: main effect of interval\n    test: ANOVA, cue by interval\n    statistic: F(47,188) = 19.75\n    p: 1.99e-51\n    n: 5 units\n  - about: cue by interval interaction\n    test: ANOVA, cue by interval\n    statistic: F(94,376) = 1.46\n    p: 0.008\n    n: 5 units\n  - about: threat minus safety, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.3\n      high: 12.58\n    n: 5 units\n  - about: threat minus safety, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -1.08\n      high: 1.11\n    n: 5 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n    quantity: threat minus safety, onset\n    value: 0.9\n    tolerance: 0.6\n  criterion: As fig4ab-thi-threat-firing, for the five Threat Excited units. Reproduced when the\n    interaction has p < 0.05, the onset CI excludes zero with the mean within tolerance, and the\n    late cue CI contains zero (the paper's test for the absence at late cue).\n- id: fig5cd-ns-nonselective\n  statement: Non-Selective units showed no main effect of cue and no cue by interval\n    interaction, and their threat and safety firing did not differ at onset or late cue.\n  source: Results, Threat Excited and Non-Selective population, paragraph 1; Figure 5C and 5D\n  quote: ANOVA for Non-Selective neurons (Fig. 5C) found neither a main effect of cue\n  statistics:\n  - about: main effect of cue\n    test: ANOVA, cue by interval\n    statistic: F(2,30) = 3.04\n    p: 0.063\n    n: 16 units\n  - about: cue by interval interaction\n    test: ANOVA, cue by interval\n    statistic: F(94,1410) = 1.19\n    p: 0.11\n    n: 16 units\n  - about: threat minus safety, onset\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.22\n      high: 0.36\n    n: 16 units\n  - about: threat minus safety, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.09\n      high: 0.46\n    n: 16 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: A claim of absence, judged on the paper's tests; the ANOVA of fig4ab-thi-threat-firing\n    at p < 0.05 and the two bootstrap CIs. Reproduced when neither ANOVA term has p < 0.05 and\n    both CIs contain zero; not reproduced when any finds the effect. Sizes are reported.\n- id: fig6-similarity-anova\n  statement: Temporal firing similarity between cue pairs depended on population and comparison,\n    with a population by comparison interaction.\n  source: Results, Threat Inhibited neurons show greatest temporal firing similarity, paragraph 2;\n    Figure 6\n  quote: revealed significant main effects of population\n  statistics:\n  - about: main effect of population\n    test: ANOVA, population by comparison\n    statistic: F(2,169) = 3.34\n    p: 0.038\n    n: 172 units\n  - about: main effect of comparison\n    test: ANOVA, population by comparison\n    statistic: F(2,338) = 26.26\n    p: 2.51e-11\n    n: 172 units\n  - about: population by comparison interaction\n    test: ANOVA, population by comparison\n    statistic: F(4,338) = 3.86\n    p: 0.004\n    n: 172 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: Per unit, mean normalized firing to each cue in 12 bins of 1 s (2 s before cue onset\n    to cue offset); Pearson R between the 12-bin traces of each cue pair (danger/uncertainty,\n    uncertainty/safety, danger/safety), as in the Methods (Firing similarity analyses). Mixed\n    ANOVA on R, population between units and comparison within. Whether the 1-s bins are\n    averages of the 250-ms normalized bins or recomputed is open; (a) the mean of four 250-ms\n    normalized bins; (b) 1-s bins normalized in the same way. Reproduced when all three terms\n    have p < 0.05; partially reproduced when the interaction holds and a main effect does not.\n- id: fig6d-thi-similarity\n  statement: In Threat Inhibited units, danger/uncertainty firing similarity exceeded\n    uncertainty/safety and danger/safety similarity.\n  source: Results, Threat Inhibited neurons show greatest temporal firing similarity, paragraph\n    2; Figure 6D\n  quote: Paired t tests (Bonferroni corrected for nine tests; 0.05/9= 0.0056) revealed Threat\n    Inhibited R values for danger/uncertainty to exceed those for uncertainty/ safety\n  statistics:\n  - about: danger/uncertainty against uncertainty/safety\n    test: paired t test\n    statistic: t(25) = 3.31\n    p: 0.003\n    corrected: Bonferroni, nine tests (alpha 0.0056)\n    n: 26 units\n  - about: danger/uncertainty against danger/safety\n    test: paired t test\n    statistic: t(25) = 4.11\n    p: 3.74e-4\n    corrected: Bonferroni, nine tests (alpha 0.0056)\n    n: 26 units\n  depends_on:\n  - fig6-similarity-anova\n  criterion: R values of fig6-similarity-anova; paired t tests at the Bonferroni level 0.05/9.\n    Reproduced when both are significant with danger/uncertainty higher.\n- id: fig6e-de-similarity\n  statement: In Danger Excited units, danger/uncertainty firing similarity exceeded\n    uncertainty/safety and danger/safety similarity.\n  source: Results, Threat Inhibited neurons show greatest temporal firing similarity, paragraph\n    2; Figure 6E\n  quote: Danger Excited R values for danger/uncertainty exceed those for uncertainty/safety\n  statistics:\n  - about: danger/uncertainty against uncertainty/safety\n    test: paired t test\n    statistic: t(54) = 3.24\n    p: 0.002\n    corrected: Bonferroni, nine tests (alpha 0.0056)\n    n: 55 units\n  - about: danger/uncertainty against danger/safety\n    test: paired t test\n    statistic: t(54) = 4.21\n    p: 9.6e-5\n    corrected: Bonferroni, nine tests (alpha 0.0056)\n    n: 55 units\n  depends_on:\n  - fig6-similarity-anova\n  criterion: As fig6d-thi-similarity, for Danger Excited units.\n- id: fig6f-bv-no-similarity-difference\n  statement: In Bidirectional Valence units, firing similarity did not differ between any cue\n    pairs.\n  source: Results, Threat Inhibited neurons show greatest temporal firing similarity, paragraph\n    2; Figure 6F\n  quote: no differences were observed for any cue pair in Bidirectional Valence neurons\n  statistics:\n  - test: paired t test\n    p: 0.0056\n    p_relation: \">\"\n    corrected: Bonferroni, nine tests (alpha 0.0056)\n    n: 91 units\n  depends_on:\n  - fig6-similarity-anova\n  criterion: A claim of absence, judged on the paper's test; the three paired t tests between\n    comparisons at the Bonferroni level 0.05/9. Reproduced when none is significant; not\n    reproduced when any is. The t values are reported (paper, all t < 2.1).\n- id: fig6-thi-greatest-similarity\n  statement: Danger/uncertainty firing similarity in Threat Inhibited units exceeded that of\n    Danger Excited and Bidirectional Valence units, and was the greatest of all populations and\n    cue pairs.\n  source: Results, Threat Inhibited neurons show greatest temporal firing similarity, paragraphs\n    1 and 2; Figure 6D to 6F legend\n  quote: danger/uncertainty firing similarity by Threat Inhibited neurons exceeded that for Danger\n    Excited (Fig. 6E) and Bidirectional Valence neurons (Fig. 6F)\n  statistics:\n  - test: unpaired t test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig6-similarity-anova\n  criterion: Danger/uncertainty R values of Threat Inhibited units against those of Danger\n    Excited and of Bidirectional Valence units, unpaired t tests. The level is open; (a) p <\n    0.05, as the Figure 6 legend marks; (b) p < 0.0056, the Bonferroni level the Methods give\n    for within- and between-cluster comparisons. Reproduced when, under one reading, both tests\n    are significant with Threat Inhibited higher and the Threat Inhibited danger/uncertainty\n    mean R is the highest of the nine population and pair means.\n- id: fig7-tuning-curves\n  statement: The extreme of the Threat Inhibited tuning curve was at an uncertainty assignment\n    of 0.75, and those of Danger Excited and Bidirectional Valence units at 0.50, so each\n    population signaled an exaggerated threat above the uncertainty cue's 0.25 shock\n    probability.\n  source: Results, NAcc neurons do not signal fear output, paragraph 1; Figure 7\n  quote: The extreme of the Threat Inhibited tuning curve occurred at an uncertainty assignment of\n    0.75, while the extremes of the tuning curves for Danger Excited and Bidirectional Valence\n    neurons occurred at an uncertainty assignment of 0.50\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: uncertainty assignment at the tuning curve extreme, Threat Inhibited\n    value: 0.75\n    tolerance: 0\n  - quantity: uncertainty assignment at the tuning curve extreme, Danger Excited\n    value: 0.5\n    tolerance: 0\n  - quantity: uncertainty assignment at the tuning curve extreme, Bidirectional Valence\n    value: 0.5\n    tolerance: 0\n  criterion: Per unit, the 16 trials of its session, a cue regressor of 1 for danger, 0 for\n    safety and u for the eight uncertainty trials, u in 0, 0.25, 0.5, 0.75, 1; linear regression\n    with a constant (Methods, Tuning curve). The firing regressed is open; (a) one regression on\n    each trial's mean normalized firing over the 10-s cue, as the Methods say; (b) a regression\n    for each 1-s cue bin, with the ten betas averaged, as the Results say (\"averaging beta\n    coefficients across the 10 s cue\"). Per-trial normalization as in the opening comment. The\n    population curve is the mean beta at each u; the extreme is the most negative mean for the\n    inhibited populations (Threat Inhibited, Bidirectional Valence) and the most positive for\n    Danger Excited. The assignment is a choice among five levels, so it must match exactly.\n    Reproduced when, under one reading, all three match; partially reproduced when two do.\n- id: fig8ab-thi-exaggerated-threat\n  statement: Threat Inhibited firing signaled exaggerated threat and not fear output; exaggerated\n    threat betas were below zero at early and late cue, and exceeded fear output betas in\n    magnitude at early but not late cue.\n  source: Results, NAcc neurons do not signal fear output, paragraph 3; Figure 8A and 8B\n  quote: Beta coefficients for exaggerated threat, but not for the fear output, were shifted below\n    zero during early cue\n  statistics:\n  - about: regressor by interval interaction\n    test: ANOVA, regressor by interval\n    statistic: F(11,264) = 2.32\n    p: 0.01\n    n: 26 units (the degrees of freedom imply 25)\n  - about: exaggerated threat beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -1.42\n      high: -0.56\n  - about: exaggerated threat beta, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.86\n      high: -0.05\n  - about: exaggerated threat minus fear output beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -1.58\n      high: -0.32\n  - about: exaggerated threat minus fear output beta, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -1.06\n      high: 0.43\n  depends_on:\n  - fig7-tuning-curves\n  expected:\n  - quantity: exaggerated threat beta, early cue\n    value: -0.97\n    tolerance: 0.41\n  - quantity: exaggerated threat beta, late cue\n    value: -0.47\n    tolerance: 0.39\n  - quantity: exaggerated threat minus fear output beta, early cue\n    value: -0.92\n    tolerance: 0.6\n  criterion: Per unit and 1-s bin (2 s before cue onset to cue offset, 12 bins), per-trial\n    normalized firing over the 16 trials of its session regressed on the trial's suppression\n    ratio (fear output) and the population's cue pattern (1 danger, 0 safety, uncertainty at\n    the population's tuning curve extreme of fig7-tuning-curves, 0.75 by the paper), with a\n    constant (Methods, Single-unit linear regression). Whether the two regressors share one\n    model is open; (a) one model with both, as the Methods give one output per regressor; (b)\n    a separate model for each. Early cue is the first 5 s and late cue the last 5 s (Figure 8\n    legend); per unit the mean beta over those bins; studentized bootstrap CIs over units.\n    Repeated-measures ANOVA on beta, regressor by bin. The degrees of freedom imply one unit\n    fewer than 26; units with a regression that cannot be fit (no variation in suppression\n    ratio) are left out, as a reading. Reproduced when the interaction has p < 0.05, the two\n    exaggerated threat CIs and the early difference CI exclude zero with means within\n    tolerance, the fear output CIs contain zero and the late difference CI contains zero;\n    partially reproduced when the exaggerated threat CIs exclude zero and the fear output CIs\n    contain zero but another part fails.\n- id: fig8cd-de-exaggerated-threat\n  statement: Danger Excited firing signaled exaggerated threat and not fear output; exaggerated\n    threat betas exceeded zero at early and late cue, and exceeded fear output betas at early but\n    not late cue.\n  source: Results, NAcc neurons do not signal fear output, paragraphs 3 and 4; Figure 8C and 8D\n  quote: Beta coefficients exceeding zero were observed for exaggerated threat during early cue\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA, regressor by interval\n    statistic: F(1,53) = 6.64\n    p: 0.01\n    n: 55 units (the degrees of freedom imply 54)\n  - about: exaggerated threat beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.22\n      high: 0.61\n  - about: exaggerated threat beta, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.06\n      high: 0.51\n  - about: exaggerated threat minus fear output beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.1\n      high: 0.69\n  - about: exaggerated threat minus fear output beta, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.05\n      high: 0.58\n  depends_on:\n  - fig7-tuning-curves\n  expected:\n  - quantity: exaggerated threat beta, early cue\n    value: 0.43\n    tolerance: 0.18\n  - quantity: exaggerated threat beta, late cue\n    value: 0.3\n    tolerance: 0.21\n  - quantity: exaggerated threat minus fear output beta, early cue\n    value: 0.39\n    tolerance: 0.29\n  criterion: As fig8ab-thi-exaggerated-threat, with the uncertainty value at 0.50, and the main\n    effect of regressor in place of the interaction.\n- id: fig8ef-bv-exaggerated-threat\n  statement: Bidirectional Valence firing signaled exaggerated threat and not fear output; early\n    exaggerated threat betas were below zero while fear output betas were not, and the two\n    differed at early but not late cue.\n  source: Results, NAcc neurons do not signal fear output, paragraph 4; Figure 8E and 8F\n  quote: Early beta coefficients were shifted below zero for exaggerated threat\n  statistics:\n  - about: main effect of regressor\n    test: ANOVA, regressor by interval\n    statistic: F(1,85) = 6.22\n    p: 0.015\n    n: 91 units (the degrees of freedom imply 86)\n  - about: regressor by interval interaction\n    test: ANOVA, regressor by interval\n    statistic: F(11,935) = 2.56\n    p: 0.003\n    n: 91 units (the degrees of freedom imply 86)\n  - about: exaggerated threat beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.45\n      high: -0.16\n  - about: fear output beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.05\n      high: 0.2\n  - about: exaggerated threat minus fear output beta, early cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.62\n      high: -0.12\n  - about: exaggerated threat minus fear output beta, late cue\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.4\n      high: 0.08\n  depends_on:\n  - fig7-tuning-curves\n  expected:\n  - quantity: exaggerated threat beta, early cue\n    value: -0.31\n    tolerance: 0.14\n  - quantity: exaggerated threat minus fear output beta, early cue\n    value: -0.39\n    tolerance: 0.23\n  criterion: As fig8ab-thi-exaggerated-threat, with the uncertainty value at 0.50. Reproduced\n    when the regressor effect and the interaction have p < 0.05, the early exaggerated threat and\n    early difference CIs exclude zero with means within tolerance, and the early fear output\n    and late difference CIs contain zero.\n- id: fig9a-reward-firing\n  statement: Around pellet feeder advance in the ITI, Bidirectional Valence units selectively\n    increased firing after reward, while Threat Inhibited and Danger Excited units did not\n    change firing.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 2; Figure 9A\n  quote: The interaction was the result of Bidirectional Valence neurons selectively increasing\n    firing following pellet feeder advance\n  statistics:\n  - about: main effect of interval, three populations\n    test: ANOVA, population by interval\n    statistic: F(15,2430) = 3.83\n    p: 8.49e-7\n    n: three main populations (the degrees of freedom imply 165 units)\n  - about: population by interval interaction\n    test: ANOVA, population by interval\n    statistic: F(30,2430) = 1.72\n    p: 0.009\n    n: three main populations (the degrees of freedom imply 165 units)\n  - about: main effect of interval, Bidirectional Valence\n    test: repeated-measures ANOVA\n    statistic: F(15,1290) = 8.78\n    p: 1.24e-19\n    n: Bidirectional Valence units (the degrees of freedom imply 87)\n  - about: main effect of interval, Threat Inhibited and Danger Excited, each\n    test: repeated-measures ANOVA\n    statistic: F < 1.1\n    p: 0.4\n    p_relation: \">\"\n  depends_on:\n  - fig2-five-clusters\n  criterion: Pellet feeder advances during the ITI, with no cue or shock; per unit, firing in 16\n    bins of 250 ms from 2 s before to 2 s after each advance, averaged over events, minus the\n    mean of the 1 s before advance (Methods, z-score normalization). Open details; which\n    rewards count as ITI: (a) advances whose 4-s window falls outside the 20 s before cue onset\n    to 20 s after cue offset; (b) advances whose window does not overlap a cue or a shock. The\n    normalization of the reward trace: (i) divided by the unit's SD from the cue normalization;\n    (ii) z-scored over the 16 reward bins. The degrees of freedom imply that some units (7 of\n    172, 4 of the Bidirectional Valence units) were left out; units with no qualifying reward\n    are left out, as a reading. Mixed ANOVA, population between and bin within; then a\n    repeated-measures ANOVA per population. Reproduced when, under one reading, the\n    interaction and the Bidirectional Valence interval effect have p < 0.05 and neither Threat\n    Inhibited nor Danger Excited has an interval effect at p < 0.05.\n- id: fig9bcd-reward-pre-post\n  statement: Bidirectional Valence firing around zero before reward rose after reward, with post\n    exceeding pre; Threat Inhibited and Danger Excited pre and post reward firing differed\n    neither from zero nor from each other.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 2; Figure 9B to 9D\n  quote: In Threat Inhibited and Danger Excited neurons, pre-reward and post-reward firing differed\n    neither from zero nor from each other (all 95% CIs contained zero\n  statistics:\n  - about: Bidirectional Valence pre-reward firing\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: -0.07\n      high: 0.13\n  - about: Bidirectional Valence post-reward firing\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.28\n      high: 0.62\n  - about: Bidirectional Valence post minus pre\n    test: 95% bootstrap confidence interval\n    ci:\n      level: 0.95\n      low: 0.21\n      high: 0.58\n  depends_on:\n  - fig9a-reward-firing\n  expected:\n  - quantity: Bidirectional Valence post-reward firing\n    value: 0.47\n    tolerance: 0.15\n  - quantity: Bidirectional Valence post minus pre\n    value: 0.42\n    tolerance: 0.16\n  criterion: The normalized reward traces of fig9a-reward-firing (same readings); pre is the\n    250-ms bin before advance and post the first 250-ms bin after (Methods, Population and\n    single-unit firing analyses); studentized bootstrap 95% CIs over units. Reproduced when the\n    Bidirectional Valence pre CI contains zero, the post and difference CIs exclude zero with\n    means within tolerance, and all six Threat Inhibited and Danger Excited CIs (pre, post,\n    difference) contain zero; partially reproduced when the Bidirectional Valence part holds\n    and a Threat Inhibited or Danger Excited CI excludes zero.\n- id: fig9efg-reward-cue-correlations\n  statement: Bidirectional Valence reward onset firing correlated positively with safety onset\n    firing and negatively with danger firing, and the two correlations differed; in Threat\n    Inhibited units only the danger correlation was significant and the two did not differ, and\n    in Danger Excited units neither was significant though they differed.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraphs 3 and 4; Figure 9E to 9G\n  quote: Bidirectional Valence neurons (Fig. 9G) showed a significant, positive relationship\n    between reward onset firing and safety onset firing\n  statistics:\n  - about: Threat Inhibited, reward onset against safety onset\n    test: Pearson correlation\n    statistic: R2 = 0.07\n    p: 0.18\n  - about: Threat Inhibited, reward onset against danger\n    test: Pearson correlation\n    statistic: R2 = 0.15\n    p: 0.05\n  - about: Threat Inhibited, difference of the two correlations\n    test: Fisher r-to-z\n    statistic: Z = -0.50\n    p: 0.62\n  - about: Danger Excited, reward onset against safety onset\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.07\n  - about: Danger Excited, reward onset against danger\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.07\n  - about: Danger Excited, difference of the two correlations\n    test: Fisher r-to-z\n    statistic: Z = -2.10\n    p: 0.035\n  - about: Bidirectional Valence, reward onset against safety onset\n    test: Pearson correlation\n    statistic: R2 = 0.08\n    p: 0.006\n  - about: Bidirectional Valence, reward onset against danger\n    test: Pearson correlation\n    statistic: R2 = 0.12\n    p: 8.43e-4\n  - about: Bidirectional Valence, difference of the two correlations\n    test: Fisher r-to-z\n    statistic: Z = -3.96\n    p: 7.7e-5\n  depends_on:\n  - fig9a-reward-firing\n  expected:\n  - quantity: R2, Bidirectional Valence, reward onset against safety onset\n    value: 0.08\n    tolerance: 0.008\n  - quantity: R2, Bidirectional Valence, reward onset against danger\n    value: 0.12\n    tolerance: 0.012\n  criterion: Per unit, reward onset firing (first 250-ms bin after advance, fig9a-reward-firing\n    readings), safety onset firing (first 1 s) and danger firing (10-s cue), normalized; Pearson\n    correlation within each population (Methods, Population and single-unit firing analyses).\n    The comparison of the two correlations is open; (a) Fisher r-to-z for independent\n    correlations; (b) a test for dependent correlations sharing a variable (Steiger). Reproduced\n    when, for Bidirectional Valence, the safety correlation is positive and the danger\n    correlation negative, each with p < 0.05, and the comparison has p < 0.05, and Threat\n    Inhibited shows no difference between the correlations at p < 0.05; the R2 values are\n    reported against their tolerances, and the Threat Inhibited and Danger Excited\n    correlations are reported.\n- id: fig9hij-danger-safety-correlations\n  statement: Danger firing correlated negatively with safety onset firing in Danger Excited and\n    Bidirectional Valence units but not in Threat Inhibited units.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 4; Figure 9H to 9J\n  quote: Danger Excited neurons (R2 = 0.25, p = 1.17\n  statistics:\n  - about: Threat Inhibited\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.24\n    n: 26 units\n  - about: Danger Excited\n    test: Pearson correlation\n    statistic: R2 = 0.25\n    p: 1.17e-4\n    n: 55 units\n  - about: Bidirectional Valence\n    test: Pearson correlation\n    statistic: R2 = 0.06\n    p: 0.015\n    n: 91 units\n  depends_on:\n  - fig2-five-clusters\n  expected:\n  - quantity: R2, Danger Excited\n    value: 0.25\n    tolerance: 0.025\n  - quantity: R2, Bidirectional Valence\n    value: 0.06\n    tolerance: 0.006\n  criterion: Per unit, normalized danger firing over the 10-s cue and safety onset firing (first\n    1 s); Pearson correlation within each population. Reproduced when Danger Excited and\n    Bidirectional Valence correlations are negative with p < 0.05 and the Threat Inhibited\n    correlation has p >= 0.05 (the paper's test for its absence); the R2 values are reported\n    against their tolerances.\n- id: fig10a-poke-cessation-anova\n  statement: The three populations showed minimal firing changes around nose poke cessation in\n    the ITI; there was no main effect of interval, and a population by interval interaction\n    driven by modest Bidirectional Valence increases.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 5; Figure 10A\n  quote: NAcc populations showed minimal firing changes around periods of natural nose poke\n    cessation occurring during the intertrial intervals\n  statistics:\n  - about: main effect of interval\n    test: ANOVA, population by interval\n    statistic: F(15,2535) = 1.58\n    p: 0.071\n    n: 172 units\n  - about: population by interval interaction\n    test: ANOVA, population by interval\n    statistic: F(30,2535) = 2.18\n    p: 2.35e-4\n    n: 172 units\n  depends_on:\n  - fig2-five-clusters\n  criterion: Cessation events are a poke followed by at least 2 s without a poke, in the ITI\n    (Methods); 16 bins of 250 ms from 2 s before to 2 s after the poke, minus the mean of the 1\n    s before, normalized with the readings of fig9a-reward-firing (ITI definition and\n    normalization). Mixed ANOVA, population between and bin within. Reproduced when the\n    interval effect has p >= 0.05 (the paper's test for its absence) and the interaction has p\n    < 0.05.\n- id: fig10bcd-poke-cessation-pre-post\n  statement: Pre and post nose poke cessation firing differed neither from zero nor from each\n    other in Threat Inhibited and Danger Excited units; in Bidirectional Valence units both\n    exceeded zero but did not differ.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 5; Figure 10B to 10D\n  quote: Pre- and post-nose poke cessation firing both exceeded zero, but did not differ from each\n    other for Bidirectional Valence neurons\n  depends_on:\n  - fig10a-poke-cessation-anova\n  criterion: Pre is the 250-ms bin before cessation and post the first 250-ms bin after;\n    studentized bootstrap 95% CIs over units for pre, post and post minus pre. Reproduced when\n    the six Threat Inhibited and Danger Excited CIs contain zero, and the Bidirectional Valence\n    pre and post CIs exclude zero above it with the difference CI containing zero.\n- id: fig10efg-poke-cessation-cue-unrelated\n  statement: Nose poke cessation firing was unrelated to safety onset and danger cue firing in\n    all three populations, so NAcc cue firing reflects cue information and not the suppression\n    of nose poking.\n  source: Results, Reward-related firing confirms NAcc threat and Bidirectional Valence\n    populations, paragraph 5; Figure 10E to 10G\n  quote: zero relationships were observed between nose poke cessation (first 250ms following nose\n    poke cessation) and cue firing\n  statistics:\n  - test: Pearson correlation\n    statistic: all R2 < 0.02\n    p: 0.45\n    p_relation: \">\"\n  depends_on:\n  - fig10a-poke-cessation-anova\n  criterion: A claim of absence, judged on the paper's test. Per unit, firing in the first 250 ms\n    after cessation against safety onset (first 1 s) and danger (10-s cue) firing; Pearson\n    correlation within each population, six tests. Reproduced when none has p < 0.05; not\n    reproduced when any does. The R2 values are reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml paper/10.1523-jneurosci.1107-21.2021.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Fixing colon-space in plain scalars; let me find all of them.

**Agent calls Bash**

```bash
cd claims/crcns-nac-1 && grep -n ': .*: \|[^ ]: [a-zA-Z(]' 10.1523-jneurosci.1107-21.2021.yaml | grep -v '^\S*#' | grep -v '^[0-9]*:\s*\(- \)\?[a-z_]*: [^:]*$' | head
```

```
77:paper: doi:10.1523/jneurosci.1107-21.2021
1015:    rewards count as ITI: (a) advances whose 4-s window falls outside the 20 s before cue onset
1017:    normalization of the reward trace: (i) divided by the unit's SD from the cue normalization;
```

**Agent calls Bash**

```bash
cd  && F=claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml && sed -n 269,273p $F && sed -n 1013,1018p $F
```

```
of replicates; (i) the solution with the lowest summed distance over 100 starts; (ii) the
    most frequent partition over 100 starts. Clusters are named from their centroids by the
    Results' descriptions (Results, NAcc neurons show heterogeneous cue firing, paragraph 2):
    Threat Excited and Threat Inhibited change equally to danger and uncertainty, less to
    safety (up and down); Danger Excited increase most to danger; Bidirectional Valence
    bins of 250 ms from 2 s before to 2 s after each advance, averaged over events, minus the
    mean of the 1 s before advance (Methods, z-score normalization). Open details; which
    rewards count as ITI: (a) advances whose 4-s window falls outside the 20 s before cue onset
    to 20 s after cue offset; (b) advances whose window does not overlap a cue or a shock. The
    normalization of the reward trace: (i) divided by the unit's SD from the cue normalization;
    (ii) z-scored over the 16 reward bins. The degrees of freedom imply that some units (7 of
```

**Agent calls Bash**

```bash
F=claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml && python - "$F" <<'EOF'
import sys,re
p=sys.argv[1]; s=open(p).read()
s=s.replace("cue firing, paragraph 2):\n    Threat Excited","cue firing, paragraph 2).\n    Threat Excited")
s=s.replace("Open details; which\n    rewards count as ITI: (a)","Open details. Which\n    rewards count as ITI; (a)")
s=s.replace("The\n    normalization of the reward trace: (i)","The\n    normalization of the reward trace; (i)")
open(p,'w').write(s)
EOF
grep -n "[^ ]: " $F | grep -v "^[0-9]*:#" | grep -vE '^[0-9]+:\s*(- )?[a-z_]+: ' | head; python tools/claims_check.py $F paper/10.1523-jneurosci.1107-21.2021.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
F=claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml && python - "$F" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
old="quote: There was no relationship between baseline nose poke rate and suppression in response to\n    any cue or to overall discrimination"
assert old in s
s=s.replace(old,"quote: There was no relationship ... between baseline nose poke rate and suppression in response\n    to any cue or to overall discrimination")
open(p,'w').write(s)
EOF
python tools/claims_check.py $F paper/10.1523-jneurosci.1107-21.2021.txt | grep -v "VALUE NOT FOUND"; grep -n "—\|rather" $F
```

Result: not kept, because it reads the paper's text.

**Agent**

Quotes all pass and the schema validates. One source string is clumsy; tidying it.

**Agent calls Bash**

```bash
F=claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml && python - "$F" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
old="""  source: Results, NAcc neurons show heterogeneous cue firing is preceded by Results, paragraph 3
    (after Figure 2 legend)"""
assert old in s
s=s.replace(old,"""  source: Results, opening section before NAcc neurons show heterogeneous cue firing, paragraph 3
    (beginning "A total of 368 NAcc single units")""")
s=s.replace("source: Results, paragraph 3 (the paragraph beginning \"A total of 368 NAcc single units\")","source: Results, opening section, paragraph 3 (beginning \"A total of 368 NAcc single units\")")
open(p,'w').write(s)
EOF
python tools/claims_check.py $F paper/10.1523-jneurosci.1107-21.2021.txt | tail -1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file at `claims/crcns-nac-1/10.1523-jneurosci.1107-21.2021.yaml`: 34 claims, all with quotes. All 34 quotes pass `tools/claims_check.py` and the file matches the schema. The checker still reports 44 problems, all of the "VALUE NOT FOUND (confirm by reading)" kind. In the extracted text, minus signs and the "× 10^" in p-values come out as a replacement character, so the checker can't match those values. I checked each one against the text by reading. Nothing was committed.

**Text read**
- The version of record (the journal PDF's text under `paper/`): Methods, Results, figure legends and Discussion.
- Not read: Extended Data Figures 1-1, 1-2 and 2-1 (per-rat suppression ratios, session-by-session suppression ratios, alternative clusterings) are not under `paper/`. No claim rests on them alone, because the Results state the numbers used.
- No PDF renderer was available, so I read figures only through their legends and the Results.
- Code: the paper links only http://mcdannaldlab.org/resources, and that page returns 404, so no code was read. I read the data descriptor only for what the data set holds.

**Statistics and criteria**
- 117 statistical values: F and t tests, Pearson correlations, Fisher r-to-z, Hartigan's dip, Pitman–Morgan, and 46 bootstrap confidence intervals. All recorded as printed.
- Every claim has a criterion. Where the paper gives a CI, the tolerance is the distance from the mean to the nearer bound; otherwise it is 10%. Counts of deposited units, sessions and rats must match exactly.
- Absence claims are judged on the paper's own test: a CI containing zero, p ≥ 0.05, or the Bonferroni level 0.05/9.

**Details the paper leaves open, with the readings named**
- **z-scoring:** over four trial types, or three with uncertainty collapsed. How uncertainty is collapsed: mean over all eight trials, or mean of the shock and omission traces.
- **Per-trial normalized firing** (Figures 7 and 8): three readings, mainly which baseline is subtracted, plus z-scoring each trial over the unit's bins.
- **Suppression ratio when a trial has no pokes (0/0):** leave the trial out, or set it to 0.
- **Sessions for Figure 1G:** the 82 sessions with a cue-responsive unit, all 95, or the 79 sessions of the main populations.
- **Cue-responsive screen:** uncertainty tested as one cue, or shock and omission trials tested separately.
- **k-means:** clustering on normalized firing (Results) or firing in Hz (Methods). No seed or replicate count is given, so either the best of 100 starts or the most frequent partition. k = 5 is fixed, with the paper's rule for choosing it run as a variant.
- **Population labels:** the paper's own labels if the data set holds them, otherwise the reproduced clusters.
- **Tuning curve:** one regression on the 10-s cue mean (Methods), or per-1-s-bin betas averaged (Results).
- **Fear output regression:** one model with both regressors, or a separate model for each.
- **Reward and nose-poke windows:** which ITI events qualify (two readings) and how the trace is normalized (two readings).
- **Comparing two correlations:** Fisher r-to-z for independent correlations, or Steiger's test.
- **Figure 6 between-population test:** p < 0.05 (legend) or 0.0056 (Methods).
- **Coefficient of variance:** spikes from the baseline periods, or the whole session. The dip-test implementation isn't named.
- **Narrow/wide waveform boundary:** taken as the lowest point between the two modes of the 172-unit histogram, because the figure's dashed line couldn't be read.

**Missing from the paper**
- Some degrees of freedom imply fewer units than the stated n, with no reason given: Figure 8 (25, 54 and 86 units against 26, 55 and 91) and the Figure 9 reward ANOVA (165 of 172; 87 of 91 Bidirectional Valence). This is recorded as a reading.
- The Figure 1C acquisition claim needs the eight pre-surgery sessions. The data set's description lists only the 95 recording sessions, so they may not be there.

## End of run

30 turns, 6 minutes, $2.52 at API prices, result: success.
