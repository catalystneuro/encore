# wirth-2017 · claims-check · run 42941331678

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i wirth; cat claims/wirth-2017.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i -E "wirth|2001045"; wc -l claims/wirth-2017.yaml; grep -n "Reader" docs/protocol.md | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/wirth-2017.yaml; python tools/claims_check.py claims/wirth-2017.yaml paper/10.1371-journal.pbio.2001045.txt; wc -c paper/10.1371-journal.pbio.2001045.txt; git log --oneline -3 -- claims/wirth-2017.yaml papers/datasets/wirth-2017.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git show d2bbb755d6 --stat; git show d2bbb755d6 | head -120; git show 5388460cde --stat
```

```
commit d2bbb755d6add6a8545200e0256134eca86cc68e
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 20:38:39 2026 -0500

    Paper match for CRCNS:hc-12: matched
    
    From attempt/crcns-hc-12 (docs/pipeline.md, step 1).

 papers/datasets/wirth-2017.yaml |  3 +++
 papers/match/crcns-hc-12.yaml   | 17 +++++++++++++++++
 2 files changed, 20 insertions(+)
commit d2bbb755d6add6a8545200e0256134eca86cc68e
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 20:38:39 2026 -0500

    Paper match for CRCNS:hc-12: matched
    
    From attempt/crcns-hc-12 (docs/pipeline.md, step 1).

diff --git a/papers/datasets/wirth-2017.yaml b/papers/datasets/wirth-2017.yaml
[... 46 more lines not kept]
```

**Agent**

Checker passes (28 claims, 0 problems). Now reading the claims file in full.

**Agent calls Read**

```json
{
 "file_path": "claims/wirth-2017.yaml"
}
```

```
1	# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
2	# tested on CRCNS hc-21.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
4	# protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
7	# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
8	# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
9	# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
10	# methods and cell selection, population averages, the control for space dimensionality) and
11	# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
12	# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
13	# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
14	# reference list is absent from the stored text, so reference 60 (the learning curve method)
15	# is not named.
16	#
17	# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on
18	# CRCNS (Supporting data; S2 Appendix). These are files of the dataset and were not read. No
19	# criterion below takes a method from code.
20	#
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper/; grep -l "^datasets:\|  datasets:" claims/*.yaml | head; grep -n "datasets" tools/claims_check.py | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat paper/hc-12.data-description.txt; echo ----; cat paper/hc-21.data-description.txt | head -80; echo ----; sed -n 1,5p claims/kim-2022.yaml; grep -n -B2 -A4 "^dataset\|^datasets\|  datasets:" claims/kim-2022.yaml | head -40; grep -rn "datasets" tools/*.py | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 105,120p tools/agent_run.py; grep -n "^dataset\|^datasets" -A6 claims/kim-2022.yaml claims/pakhomov-2023.yaml claims/silkuniene-2025.yaml | head -40; grep -n "crcns" claims/*.yaml | grep -i "datasets\|- crcns\|- \"crcns\|hc-" | head
```

```
f'({d.get("why", "no reason given")}). Claims that need it are blocked with '
                     f'`blocked_by: dataset_missing` (docs/protocol.md).')
    if len(usable) == 1:
        sentence = labels[0]
        several = reader = ""
    else:
        folders = ", ".join(f'`{d["folder"]}`' for d in usable)
        reader = (f" The paper's data are in {len(usable)} datasets ({folders}): give each claim `datasets:`, the "
                  f"folder names of the ones it rests on (docs/protocol.md, \"Reader\").")
        sentence = f'{", ".join(labels[:-1])} and {labels[-1]}'
        several = (f" The paper's data are in {len(usable)} datasets: use every one of them that a claim needs, "
                   f"as each claim's `datasets` says.")
    return {"dataset": sentence, "datasets": "\n".join(lines), "several": several, "reader_several": reader,
            "archive": ", ".join(sorted({datasets.archive_name(d["key"]) for d in usable})),
            "access": " ".join(dict.fromkeys(datasets.access(d["key"]) for d in usable))}
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p claims/kim-2022.yaml | grep -v "^#"; grep -n "^[a-z_]*:" claims/kim-2022.yaml claims/pakhomov-2023.yaml; python -c "
import sys; sys.path.insert(0,'tools'); import datasets as d; print(d.folder(d.parse('crcns:hc-12')))"; grep -rn "datasets" tools/claims_check.py tools/claims_schema* 2>/dev/null | head; ls tools | head -50
```

```
claims/kim-2022.yaml:79:schema_version: 2
claims/kim-2022.yaml:80:paper: doi:10.1016/j.bioelechem.2022.108319
claims/kim-2022.yaml:81:claims:
claims/kim-2022.yaml:613:checks:
claims/pakhomov-2023.yaml:108:schema_version: 2
claims/pakhomov-2023.yaml:109:paper: doi:10.1016/j.bioelechem.2023.108437
claims/pakhomov-2023.yaml:110:claims:
claims/pakhomov-2023.yaml:643:checks:
crcns-hc-12
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "dataset" tools/claims_check.py tools/entry.py | head -30
```

```
tools/entry.py:20:- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
tools/entry.py:78:def dataset_id(record: dict) -> str | None:
tools/entry.py:79:    """The identifier of the one dataset a claims file or attempt record is about, in its archive: None for a
tools/entry.py:80:    paper's own claims file (claims/<paper>.yaml) and for an attempt on several datasets."""
tools/entry.py:81:    if record.get("datasets"):
tools/entry.py:82:        return str(record["datasets"][0]["id"]) if len(record["datasets"]) == 1 else None
tools/entry.py:83:    found = (record.get("dataset") or {}).get("id")
tools/entry.py:87:def dataset_ids(record: dict) -> list[str]:
tools/entry.py:88:    """The identifiers of every dataset an attempt record used."""
tools/entry.py:89:    return [str(d["id"]) for d in record.get("datasets") or ([record["dataset"]] if record.get("dataset") else [])]
tools/entry.py:93:    """Every claims file: the papers' own (claims/<paper>.yaml), and the per-dataset ones from before the cutover
tools/entry.py:99:    """How a claims file is looked up: its paper, and its dataset for a per-dataset file."""
tools/entry.py:100:    return (data.get("paper"), str((data.get("dataset") or {}).get("id")) if data.get("dataset") else None)
tools/entry.py:104:    """The claims an attempt was tested on: the per-dataset file of its one dataset if there is one, else the
tools/entry.py:106:    one = dataset_id(attempt)
tools/entry.py:218:            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
tools/entry.py:221:                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
tools/entry.py:234:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
tools/entry.py:238:                                         f"of dataset {dandiset}, which entry.yaml pins")
tools/entry.py:253:      
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 90,125p tools/entry.py; grep -n "\"datasets\"\|'datasets'" tools/claims_check.py tools/paper_records.py | head
```

```
def claims_paths() -> list[Path]:
    """Every claims file: the papers' own (claims/<paper>.yaml), and the per-dataset ones from before the cutover
    to paper-first records (claims/<paper>/<folder>.yaml)."""
    return sorted((ROOT / "claims").glob("*.yaml")) + sorted((ROOT / "claims").glob("*/*.yaml"))


def claims_target(data: dict) -> tuple:
    """How a claims file is looked up: its paper, and its dataset for a per-dataset file."""
    return (data.get("paper"), str((data.get("dataset") or {}).get("id")) if data.get("dataset") else None)


def lookup(index: dict, attempt: dict):
    """The claims an attempt was tested on: the per-dataset file of its one dataset if there is one, else the
    paper's own."""
    one = dataset_id(attempt)
    if one is not None and (attempt.get("paper"), one) in index:
        return index[(attempt.get("paper"), one)]
    return index.get((attempt.get("paper"), None))

@functools.cache
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in claims/*.yaml; do grep -q "^dataset:" $f && echo "HAS $f"; done | wc -l; ls claims/*.yaml | wc -l; grep -n "\"dataset\"\|datasets" schemas/claims.schema.json | head -20
```

```
218
271
16:    "dataset": {
141:              "dataset",
152:          "datasets": {
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p schemas/claims.schema.json; sed -n 148,165p schemas/claims.schema.json; grep -n "dataset:" -A3 docs/paper-first.md | head -30
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
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -o ".\{200\}K0R49NQV.\{100\}" paper/10.1371-journal.pbio.2001045.txt | head -3; grep -c "K0R49NQV" paper/10.1371-journal.pbio.2001045.txt; grep -n -i "crcns\|familiar\|Supporting data\|data availab" paper/10.1371-journal.pbio.2001045.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper's Supporting data section links the CRCNS deposit 10.6080/K0R49NQV, which is hc-12. Now I'll read the paper itself to check the claims.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)" "substr($0,1,90)}' paper/10.1371-journal.pbio.2001045.txt | head -250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '9p;21p;29,43p;53,75p' paper/10.1371-journal.pbio.2001045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '81p;85p;91p;95,97p;103p;107p;113,115p' paper/10.1371-journal.pbio.2001045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '161,217p;229p;241p;249,400p' paper/10.1371-journal.pbio.2001045.txt | grep -v "^$" | grep -v "Click here"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -o ".\{300\}average = 2.7.\{200\}" paper/10.1371-journal.pbio.2001045.txt; grep -n -o ".\{100\}Approximately 50%.\{300\}" paper/10.1371-journal.pbio.2001045.txt; python3 -c "
from scipy.stats import binom
print('3/56 .025',binom.sf(2,56,.025),'.05',binom.sf(2,56,.05))
print('12/111 .05',binom.sf(11,111,.05),'4/111 ge',binom.sf(3,111,.05),'le',binom.cdf(4,111,.05))
print('12/111 .025',binom.sf(11,111,.025))
print('14/111 .05',binom.sf(13,111,.05),'15',binom.sf(14,111,.05),'29',binom.sf(28,111,.05))
print('1/42 le',binom.cdf(1,42,.05),'12/42',binom.sf(11,42,.05))
print('20/56',binom.sf(19,56,.025),binom.sf(19,56,.05))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
from math import comb
def sf(k,n,p): return sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
def cdf(k,n,p): return 1-sf(k+1,n,p)
print('3/56 .025',sf(3,56,.025),'.05',sf(3,56,.05))
print('12/111 .05',sf(12,111,.05),'4/111 ge',sf(4,111,.05),'le',cdf(4,111,.05))
print('12/111 .025',sf(12,111,.025), '4/111 .025 ge', sf(4,111,.025))
print('14/111',sf(14,111,.05),'15',sf(15,111,.05),'29',sf(29,111,.05), '30', sf(30,111,.05))
print('1/42 le',cdf(1,42,.05),'12/42',sf(12,42,.05))
print('20/56',sf(20,56,.025),sf(20,56,.05))
"
```

```
3/56 .025 0.16463791930714108 .05 0.5354425897686959
12/111 .05 0.009726520823597195 4/111 ge 0.8111022761524332 le 0.3436583431327257
12/111 .025 2.3717310894992354e-05 4/111 .025 ge 0.3018562851619515
14/111 0.0013211645571086597 15 0.00043511163762637234 29 1.3585327608120586e-13 30 1.9402880245243634e-14
1/42 le 0.37236397364738805 12/42 6.58348320148897e-07
20/56 3.003530683831922e-18 1.2984487011157223e-12
```

**Agent calls Bash**

```bash
cd  sed -n 27p paper/10.1371-journal.pbio.2001045.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "# tested on CRCNS hc-21.",
 "new_string": "# tested on CRCNS hc-12 and hc-21."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on\n# CRCNS (Supporting data; S2 Appendix). These are files of the dataset and were not read. No\n# criterion below takes a method from code.",
 "new_string": "# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on\n# CRCNS (Supporting data; S2 Appendix); the hc-12 descriptor lists them (a scripts folder that\n# plots position, direction and state-space maps, rasters and learning curves). These are files\n# of the dataset and were not read. No criterion below takes a method from code; the author may\n# read them for the map binning left open in Method W, citing the file."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "# The archive's descriptor (paper/hc-21.data-description.txt, read for this alone) describes\n# 101 cells from the two monkeys (files \"sn\" for monkey 1, Snorre, and \"ke\" for monkey 2,\n# Kevin), each file with a familiar maze (\"famallo\") and a daily new maze (\"newallo\"), and the\n# state-space coordinates and transition tags. The paper describes only daily new layouts and\n# names no familiar maze. The figure legends give the underlying data as doi 10.6080/K0R49NQV,\n# while the descriptor asks that hc-21 be cited as doi 10.6080/K0GX48R9. Whether hc-21 holds\n# the paper's cells, and which ones, is the author's to find.",
 "new_string": "# Datasets. The paper names one deposit, \"the spike and behavior data files hosted on CRCNS\n# (http://dx.doi.org/10.6080/K0R49NQV)\" (Supporting data; the figure legends give the same doi).\n# The descriptors under paper/ (read for this alone) give that doi to hc-12: 189 cells from the\n# two monkeys (files \"sn\" and \"ke\"), one session per file of about 40 minutes, in a field\n# \"newallo\" (the daily new maze), with eye positions, camera data, state-space coordinates,\n# transition tags and learning curves. hc-21 has its own doi (10.6080/K0GX48R9, 2018): 101\n# cells, each file with a familiar maze (\"famallo\") and a daily new maze (\"newallo\"), and it\n# names a second paper (Baraduc, Duhamel and Wirth, schema cells). The paper describes only\n# daily new layouts and no familiar maze, so its findings rest on hc-12, and every claim lists\n# crcns-hc-12 alone. Whether some hc-21 \"newallo\" sessions are the paper's sessions is not\n# settled by the paper; the author may test claims on them as a variant."
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "schema_version: 2\ndataset:\n  archive: crcns\n  id: hc-21\npaper:",
 "new_string": "schema_version: 2\npaper:"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Top-level `dataset` removed and the header rewritten. Next I'll add `datasets: [crcns-hc-12]` to every claim.

**Agent calls Bash**

```bash
cd  grep -c "^  criterion:" claims/wirth-2017.yaml; python3 - <<'EOF'
p='claims/wirth-2017.yaml'
s=open(p).read()
head,rest=s.split('\nchecks:\n',1)
head=head.replace('\n  criterion:','\n  datasets:\n  - crcns-hc-12\n  criterion:')
open(p,'w').write(head+'\nchecks:\n'+rest)
EOF
grep -c "crcns-hc-12$" claims/wirth-2017.yaml
```

```
28
28
```

**Agent**

Now the claim-level edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    test's layout is not stated; readings (a) a 4 x 2 contingency test of responsive and not\n    responsive counts across the four spaces, over the 189 cells; (b) the same over the 111\n    responsive cells; the pairwise tests are the 2 x 2 tables of state space against each other\n    space, Bonferroni over three.",
 "new_string": "    test's layout is not stated; readings (a) a 4 x 2 contingency test of responsive and not\n    responsive counts across the four spaces, over the 189 cells; (b) the same over the 111\n    responsive cells; (c) a goodness-of-fit test of the four counts against equal counts (\"the\n    proportion of cells responsive to each space was significantly unequal\"). The pairwise tests\n    are, under (a) and (b), the 2 x 2 tables of state space against each other space and, under\n    (c), the goodness of fit of the two counts against equal counts, Bonferroni over three."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    it is taken as a Wilcoxon signed-rank test across cells of the paired normalized values, the\n    test the Results use for the comparisons of Fig 3D to 3F. Reproduced",
 "new_string": "    it is taken as a Wilcoxon signed-rank test across cells of the paired normalized values, the\n    test the Results use for the comparisons of Fig 3D to 3F, a deviation. Reproduced"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "  - quantity: viewpoint-dependent cells\n    value: 12\n    tolerance: 1.2",
 "new_string": "  - quantity: viewpoint-dependent cells\n    value: 12\n    tolerance: 1.2\n  - quantity: path-invariant cells\n    value: 1\n    tolerance: 1"
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wirth-2017.yaml",
 "old_string": "    reading, the counts of 42 and 12 are within tolerance, 12 passes the binomial test at\n    p < 0.001, and the Kolmogorov-Smirnov test gives p < 0.001.",
 "new_string": "    reading, the counts of 42 and 12 are within tolerance, the path-invariant count is 0 to 2\n    (a count of 1 cannot carry a 10% tolerance), 12 passes the binomial test at p < 0.001, and\n    the Kolmogorov-Smirnov test gives p < 0.001."
}
```

```
The file claims/wirth-2017.yaml has been updated successfully.
```

**Agent**

Now the check entry.

**Agent calls Bash**

```bash
cd  cat >> claims/wirth-2017.yaml <<'EOF'
- date: 2026-11-11
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Top level. Removed `dataset` (hc-21). The paper is now tested on hc-12 and hc-21 (papers/datasets/wirth-2017.yaml), and the schema says a paper's own claims file leaves `dataset` out; with it, the file was keyed to hc-21 alone and an attempt on both datasets would not find it (tools/entry.py, lookup).
  - Every claim. Added `datasets` with crcns-hc-12. The paper's Supporting data names one deposit, doi 10.6080/K0R49NQV, which the descriptors give to hc-12 (189 cells, the analysed count, new maze sessions only); hc-21 is a later deposit (doi 10.6080/K0GX48R9) with a familiar maze the paper does not describe.
  - Header. Rewrote the dataset paragraph on that basis (it had said only that the legend doi and the hc-21 doi differ), and noted that the hc-12 descriptor lists the Matlab scripts the paper mentions.
  - state-space-most-responsive. Added reading (c), a goodness-of-fit test of the four counts against equal counts, which the paper's words ("the proportion of cells responsive to each space was significantly unequal") allow as well as a contingency table; pairwise tests named for each reading.
  - path-selectivity. Added the reported count of one path-invariant cell to `expected` (the statement rests on it), with the 0 to 2 band used for small counts in direction-tuning-not-maintained, and to the criterion.
  - direction-center-vs-periphery. The Wilcoxon signed-rank test is not named by the paper; the criterion now marks it as a deviation.
  - Checked, no change. The binomial readings in the header recompute as stated (12 of 111 at 0.05 gives 0.0097, 4 of 111 gives 0.81, 3 of 56 at 0.025 gives 0.16, 1 of 42 lower tail at 0.05 gives 0.37).
  - Open. Whether any hc-21 "newallo" sessions are the paper's sessions is not settled by the paper; no claim rests on hc-21, and testing on it is a variant.
  - Open. S1 Appendix (A1 to A5) and the S2 Appendix are not under paper/, and reference 60 is not named; the open items of the previous check stand (gaze-anticipates-action, gaze-anticipates-landmarks, fields-per-cell, dimensionality-control, the learning-curve bounds, the chance rate of the landmark-identity-distance binomial tests).
  - Open. The CRCNS scripts the paper points to were not read (they are files of the dataset); they may settle the map binning of Method W.
EOF
python tools/claims_check.py claims/wirth-2017.yaml paper/10.1371-journal.pbio.2001045.txt; grep -n ": .*: " claims/wirth-2017.yaml | grep -v "^[0-9]*:#" | grep -v '"' | head; grep -n "—\|rather" claims/wirth-2017.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import sys,yaml; sys.path.insert(0,'tools'); import entry
d=yaml.safe_load(open('claims/wirth-2017.yaml'))
print(list(entry.schema('claims').iter_errors(d))[:3]); print(entry.claims_target(d)); print(d['checks'][-1]['ready'], len(d['checks']))
"; git status --short
```

```
[<ValidationError: "datetime.date(2026, 11, 10) is not of type 'string'">, <ValidationError: "datetime.date(2026, 11, 11) is not of type 'string'">]
('doi:10.1371/journal.pbio.2001045', None)
True 2
 M claims/wirth-2017.yaml
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

I've finished the check of `claims/wirth-2017.yaml` and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/wirth-2017.yaml: 28 claims, 28 quotes, 25 statistical values, 0 problems` (the same before and after my edits). The file also passes the repository's schema; the only errors in a plain `yaml.safe_load` run were the `checks` dates, which both check entries share and the checker accepts.

The file had already been checked once (2026-11-10). What is new since then is that hc-12 was added as a second dataset. That turns out to matter most: the paper's Supporting data section names a single CRCNS deposit, doi 10.6080/K0R49NQV, and the descriptors show that is hc-12. hc-12 holds 189 cells, the same number the paper analyses, all in new-maze sessions. hc-21 is a later deposit (2018, 101 cells) that adds a familiar maze the paper never describes, and it also names a second paper.

**Changes, by claim**
- **Top level:** removed the `dataset: hc-21` entry. The schema says a paper's own claims file leaves it out, and with it in place the file was looked up as an hc-21-only file, so an attempt on both datasets would not have found it.
- **Every claim:** added `datasets: [crcns-hc-12]`, for the reason above.
- **Header:** rewrote the paragraph on the datasets. Also noted that the hc-12 descriptor lists the Matlab scripts the paper mentions.
- **state-space-most-responsive:** added a third way to read the chi-squared test: a goodness-of-fit test of the four counts against equal counts, which fits the paper's wording ("significantly unequal"). The pairwise tests are now given for each reading.
- **path-selectivity:** added the paper's count of one path-invariant cell to the expected values, accepted from 0 to 2 (a count of 1 cannot carry a 10% tolerance), and to the criterion.
- **direction-center-vs-periphery:** the paper does not name its test, so the criterion now marks the Wilcoxon signed-rank test as a deviation.
- **Checked, no change:** I recomputed the binomial readings in the header and they match the paper's p-values (0.0097, 0.81, 0.16 and 0.37). Every other claim checked out against the paper, and every main finding has a claim.

**Still open**
- The paper does not say whether any hc-21 new-maze sessions are its own. No claim rests on hc-21; testing on it would be a variant.
- The S1 and S2 Appendices are not under `paper/`, and reference 60 (the learning-curve method) is not named. So these stay as open as the previous check left them:
  - the methods of gaze-anticipates-action and gaze-anticipates-landmarks
  - fields-per-cell and dimensionality-control
  - the confidence bounds of the learning curves
  - the chance rate in the binomial tests of landmark-identity-distance
- I did not read the CRCNS scripts because they are files of the dataset. They might settle the map binning that the shared method leaves open.

## End of run

34 turns, 4 minutes, $1.34 at API prices, result: success.
