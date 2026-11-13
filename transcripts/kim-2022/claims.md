# kim-2022 · claims · run 42745841978

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head; wc -c paper/*
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
 "file_path": "claims/kim-2022.yaml"
}
```

```
1	# Claims for Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022) on dandiset 000489.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read. The accepted author manuscript in PubMed Central (PMC9729435, NIHMS1849847), as
6	# served by ncbi_pmc, in paper/10.1016-j.bioelechem.2022.108319.txt. It holds the main text,
7	# the Methods (sections 2.1 to 2.6), the Results, the Discussion and the legends of Figs. 1 to 7.
8	# The paper has no supplement (PMC lists none, and the text cites none). No PDF was supplied;
9	# figures were not read, so values shown only in a figure are not used. The paper links no
10	# code and no data deposit, so no repository was read.
11	#
12	# The dandiset. Its title on DANDI is "The impact of the second phase amplitude (% to the first
13	# phase) on the electroporation efficiency (measured as YP emission)" and its description
14	# names 5-pulse, 1-Hz trains of unipolar 600 ns pulses (0%) or bipolar 600+600 ns pulses with
15	# a second phase of 25, 50, 75 or 100%, delivered by two stainless-steel cylinders 1.5 mm in
16	# diameter and 3 mm apart. That is the experiment of Fig. 2 (Results 3.1). The claims on Figs.
17	# 3 to 7 and on heating cover the paper's other findings; the dandiset is not meant to hold
18	# them, and whether it does is the author's to find.
19	#
20	# Data the paper used, as it reports them.
[... 517 more lines not kept]
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
 "file_path": "paper/10.1016-j.bioelechem.2022.108319.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1016-j.bioelechem.2022.108319.txt').read()
i=s.find('Fig. 1.'); i=s.find('Figure 1') if i<0 else i
import re
m=[x.start() for x in re.finditer(r'(Fig\.|Figure) ?1[\.:]',s)]
print(m)
print(s[-16000:])
"; cat papers/datasets/kim-2022.yaml; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rl "000448" --include=*.yaml --include=*.md --include=*.json . | grep -v transcripts | head -20; git log -3 --stat cecad397ab | head -30
```

```
grep: ./.mcp.json: Permission denied
./attempts/kim-2022-01.yaml
./docs/pilot-notes/kim-2022-01.md
./papers/manifest.yaml
./papers/match/000448.yaml
./papers/datasets/kim-2022.yaml
./targets/dandisets.json
./entries/kim-2022/README.md
commit cecad397abeb11bbe890de172b685d2ed3c7fffe
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Mon Nov 9 21:50:58 2026 -0500

    Paper match for DANDI:000448: matched
    
    From attempt/000448 (docs/pipeline.md, step 1).

 papers/datasets/kim-2022.yaml                  |   3 +
 papers/match/000448.yaml                       |  27 ++++++
 transcripts/match/000448/paper-match-report.md |   7 ++
 transcripts/match/000448/paper-match.md        | 124 +++++++++++++++++++++++++
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/match/000448.yaml; cat papers/match/000489.yaml 2>/dev/null; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  s=json.dumps(x)
  if '000448' in s or '000489' in s: print(s[:2500])
"
```

```
# Whether each paper DANDI:000448 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: 000448
date: '2026-11-10'
papers:
- doi: 10.1016/j.bioelechem.2022.108319
  relation: IsPublishedIn
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: partial
  by: agent
  reason: >-
    The dataset holds the FluoVolt strobe imaging of single CHO cells under 833 kHz pulse trains,
    the data of Fig. 7 (Section 3.6). The paper's main electroporation findings rest on YO-PRO-1
    uptake measurements that the dataset does not hold, and the paper gives no data location for them.
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "^  datasets:" claims/*.yaml | head; grep -h -B2 -A3 "data: elsewhere" claims/*.yaml | head -40; grep -n "elsewhere\|not available\|data_missing" docs/protocol.md | head -30
```

```
integration resulted in a final dataset of 12,065 nuclei, with a mean UMI count of 3,435 and a
    mean of 1,683 features.
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  expected:
  - quantity: Nuclei after quality control
--
  quote: Expression of Aldh1a1 and Anxa1, the latter of which is expressed only within a subset of
    Aldh1a1-expressing neurons.
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
  depends_on:
  - snrna-nuclei-qc
--
    p: 9.4e-118
    corrected: FDR
  data: elsewhere
  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
- id: scrna-meta-integration
  statement: Integrating four published single-cell datasets gives eight clusters, one of them
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
L=d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
for x in L:
  if x.get('dandiset') in ('000448','000489'): print(json.dumps(x,indent=1))
"; grep -n "000448\|000489" papers/manifest.yaml | head
```

```
{
 "dandiset": "000448",
 "name": "Time kinetics of the membrane potential at the cathode- and anode-facing poles of a cell induced by a train of 5 pulses at 833 kHz",
 "published_version": "0.230421.1844",
 "asset_count": 18,
 "size_gb": 3.17,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Cricetulus griseus - Cricetulus aureus"
 ],
 "approaches": [],
 "papers": [
  {
   "doi": "10.1016/j.bioelechem.2022.108319",
   "title": "Action spectra and mechanisms of (in) efficiency of bipolar electric pulses at electroporation",
   "relation": "IsPublishedIn",
   "resource_type": null,
   "preprint": false
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "datasets\|dataset\b\|schema_version\|'data'" tools/claims_check.py | head -40; grep -ln "^datasets:" claims/*.yaml | head -3
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  wc -l tools/claims_check.py; grep -n "def \|KEYS\|allowed\|fields" tools/claims_check.py | head -40; grep -rn "datasets" docs/paper-first.md | head -20
```

```
112 tools/claims_check.py
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
105:def main() -> int:
8:paper becomes the unit, and each paper names the datasets it is tested on.
26:  names its datasets.
32:  carry `datasets:`, naming the ones it rests on. An attempt tests the paper against as many of those datasets as can be found and
34:- The paper's datasets are listed in `papers/datasets/<paper key>.yaml`: each with archive, id,
38:- **Missing datasets do not stop an attempt.** It runs on what is there; its record lists the
39:  rest under `missing_datasets`, and each claim that needs one is blocked with
60:datasets:
65:missing_datasets: []       # datasets the paper relies on that this attempt could not use, each with why
94:paper's claims once and tests them across all its datasets. Mirrors on two archives (Girardeau
```

**Agent calls Read**

```json
{
 "file_path": "docs/paper-first.md"
}
```

```
1	# Paper-first records
2	
3	Status: proposal, 2026-11-09. Nothing here is implemented yet.
4	
5	Encore has so far been organized by dataset: a target is a dataset, the pipeline finds its paper,
6	and records are named after the dataset (`000233-tingley-2021`). We now also want to test papers
7	that reuse a dataset (the find_reuse REUSE pairs), and a dataset can have many of those. So the
8	paper becomes the unit, and each paper names the datasets it is tested on.
9	
10	## What the records hold today
11	
12	- 253 attempts on 208 papers. 19 papers are tested on more than one dataset, as separate attempts:
13	  mirrors on two archives (Girardeau 2017 on DANDI 000061 and CRCNS hc-14; Fujisawa 2008), and one
14	  paper's data split across dandisets (Semenov 2026 on 7, Churchland 2010 on 4, Pakhomov 2023 on 4).
15	- Each such pair has its own claims, chosen for what that dataset holds: Semenov 2026 has 30 to 34
16	  claims per dandiset, with different ids.
17	- No dataset is tested against more than one paper yet. Reuse papers will change that.
18	
19	## Names
20	
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in papers/datasets/*.yaml; do n=$(grep -c "^- archive" $f); [ $n -gt 1 ] && echo "$f $n"; done | head; ls claims | grep -i "semenov\|pakhomov"; grep -ln "^  datasets:\|^    datasets:" -r claims | head
```

```
papers/datasets/churchland-2010.yaml 4
papers/datasets/fujimoto-2026.yaml 2
papers/datasets/fujisawa-2008.yaml 2
papers/datasets/gao-2025.yaml 4
papers/datasets/gillon-2023.yaml 2
papers/datasets/girardeau-2017.yaml 2
papers/datasets/grosmark-2016.yaml 2
papers/datasets/kauvar-2025.yaml 2
papers/datasets/kim-2022.yaml 2
papers/datasets/kim-2023.yaml 3
pakhomov-2023
semenov-2025
semenov-2026
```

**Agent calls Bash**

```bash
cd  for k in churchland-2010 gao-2025 kim-2023 fujimoto-2026 gillon-2023 kauvar-2025; do ls claims/$k* 2>/dev/null; done; grep -rn "datasets:" claims/*.yaml | head
```

```
000128.yaml
000138.yaml
000139.yaml
000140.yaml
000463.yaml
000637.yaml
000946.yaml
001199.yaml
000631.yaml
000632.yaml
000633.yaml
001773.yaml
001785.yaml
000037.yaml
000336.yaml
001326.yaml
001347.yaml
```

**Agent calls Bash**

```bash
cd  grep -rln "claims/" tools/*.py | head; grep -rn "\"datasets\"\|'datasets'" tools/*.py | head
```

```
tools/build_site.py
tools/claims_check.py
tools/datasets.py
tools/entry.py
tools/migrate_paper_first.py
tools/paper_records.py
tools/papers_manifest.py
tools/agent_run.py:117:    return {"dataset": sentence, "datasets": "\n".join(lines), "several": several, "reader_several": reader,
tools/build_reuse_targets.py:75:    for path in (ROOT / "papers" / "datasets").glob("*.yaml"):
tools/build_reuse_targets.py:77:        if any(d.get("relation", "primary") == "primary" for d in body.get("datasets") or []):
tools/build_reuse_targets.py:93:                "datasets": [{"archive": "dandi", "id": p["dataset"], "relation": "reuses"}]}
tools/build_reuse_targets.py:94:        path = ROOT / "papers" / "datasets" / f"{key}.yaml"
tools/build_site.py:240:                       if not c.get("datasets") or dir_of(key) in c["datasets"]]})
tools/build_site.py:267:            "datasets": [key_of(d["archive"], str(d["id"])) for d in paper_records.record_datasets(a)],
tools/build_site.py:351:            "datasets": sorted({key_of(*r["id"].split("/")[0].split(":", 1)) for r in related
tools/build_site.py:469:                "description": a["description"], "datasets": [a["key"]], "papers": [a["paper"]],
tools/build_site.py:674:    return [en for en in data["entries"] if dandiset in en["datasets"]]
```

**Agent calls Bash**

```bash
cd  sed -n 225,245p tools/build_site.py; grep -n "def dir_of\|def key_of" -A6 tools/build_site.py | head -20; grep -n "dataset" tools/paper_records.py | head -20
```

```
def collect(executed: Path | None = None) -> dict:
    queue = json.loads((ROOT / "targets" / "dandisets.json").read_text())
    pilot = {key_of("dandi", t["dandiset"]) for t in load_yaml(ROOT / "targets" / "pilot.yaml")["targets"]}
    claims, claim_files = {}, {}
    for path, keys in record_files("claims"):
        data = load_yaml(path)
        claims[path] = {c["id"]: c for c in data["claims"]}
        last = (data.get("checks") or [None])[-1]
        for key in keys:
            claim_files.setdefault(key, []).append({
            "path": str(path.relative_to(ROOT)), "paper": str(data["paper"]).removeprefix("doi:"),
            "check": None if last is None else {"ready": bool(last.get("ready")), "date": str(last.get("date"))},
            "claims": [{k: squash(c.get(k) or "") for k in ("id", "statement", "source", "quote", "criterion")}
                       for c in data["claims"]
                       if not c.get("datasets") or dir_of(key) in c["datasets"]]})
    entries = {}
    for path in sorted((ROOT / "entries").glob("*/entry.yaml")):
        data = load_yaml(path)
        entries[data["name"]] = data
    titles = {p["doi"]: p["title"] for t in queue["targets"] for p in t["papers"]}
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "\[\"dataset\"\]\|get(\"dataset\")" tools/*.py | grep -iv "attempt\|match\|t\[\|p\[" | head
```

```
tools/build_openneuro_targets.py:131:    ds, snap = data["dataset"], data["snapshot"]
tools/build_site.py:1540:        name = (f'<a href="{root}{e(r["page"])}">{e(r["dataset"])}</a>' if r["page"] else e(r["dataset"]))
tools/build_site.py:1857:        modified = a["dataset"].get("modified")
tools/build_site.py:1859:    doi = a["dataset"].get("doi")
tools/build_site.py:2096:                  + (f' (<a href="https://doi.org/{e(a["dataset"]["doi"])}">doi:{e(a["dataset"]["doi"])}</a>)'
tools/build_site.py:2097:                     if a["dataset"].get("doi") else "")
tools/build_site.py:2098:                  + (f', modified {e(a["dataset"]["modified"])}' if a["dataset"].get("modified") else ""))]
tools/entry.py:83:    found = (record.get("dataset") or {}).get("id")
tools/entry.py:89:    return [str(d["id"]) for d in record.get("datasets") or ([record["dataset"]] if record.get("dataset") else [])]
tools/entry.py:100:    return (data.get("paper"), str((data.get("dataset") or {}).get("id")) if data.get("dataset") else None)
```

**Agent calls Bash**

```bash
cd  sed -n 78,110p tools/entry.py
```

```
def dataset_id(record: dict) -> str | None:
    """The identifier of the one dataset a claims file or attempt record is about, in its archive: None for a
    paper's own claims file (claims/<paper>.yaml) and for an attempt on several datasets."""
    if record.get("datasets"):
        return str(record["datasets"][0]["id"]) if len(record["datasets"]) == 1 else None
    found = (record.get("dataset") or {}).get("id")
    return str(found) if found is not None else None


def dataset_ids(record: dict) -> list[str]:
    """The identifiers of every dataset an attempt record used."""
    return [str(d["id"]) for d in record.get("datasets") or ([record["dataset"]] if record.get("dataset") else [])]


def claims_paths() -> list[Path]:
    """Every claims file: the papers' own (claims/<paper>.yaml), and the per-dataset ones from before the cutover
    to paper-first records (claims/<paper>/<folder>.yaml)."""
    return sorted((ROOT / "claims").glob("*.yaml")) + sorted((ROOT / "claims").glob("*/*.yaml"))


[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 228,
 "limit": 65
}
```

```
228	3. Choose the version to pin. Pin the version the paper cites, as the claims
229	   file gives it. If it cites none, pin the most recent published version,
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference.
233	4. Decide what comes from outside the dataset. Data from elsewhere may be
234	   used only when the claims file says the paper relies on it, it is public,
235	   and it is pinned: a DOI, or a repository at a commit. Record each under
236	   `inputs` in the attempt. A claim whose outside input is not public is
237	   blocked with `data_missing`, and its notes say where you looked.
238	
239	   The registry judges the dataset, so claims that use outside data are
240	   kept apart:
241	   - Each claim says what its test uses: `data: dataset` (the default),
242	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243	     `with_inputs` and `elsewhere` claims are counted apart, each group on
244	     its own; the others count towards what is said about the dataset.
245	   - `with_labels` is for outside sources that only name or map codes the
246	     dataset already holds, such as stimulus names for its stimulus codes.
247	     They bring in no measurements. A link claim must confirm the names, and
[... 45 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/kim-2022.yaml",
 "content": "# Claims for Kim, Semenov, Kiester, Keppler, Ibey, Bixler & Pakhomov (2022), tested on dandisets\n# 000489 and 000448.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. It replaces the file written 2026-10-23 under\n# pilot-10 for dandiset 000489 alone; ids are kept where the finding is the same.\n#\n# Text read. The accepted author manuscript in PubMed Central (PMC9729435, NIHMS1849847), as\n# served by ncbi_pmc, in paper/10.1016-j.bioelechem.2022.108319.txt. It holds the main text, the\n# Methods (sections 2.1 to 2.6), the Results (3.1 to 3.5), the Discussion and the legends of Figs.\n# 1 to 7. It is not the version of record. The paper has no supplement (PMC marks\n# \"has-supplement no\", and the text cites none). No PDF was supplied, so figures were not read and\n# values shown only in a figure are not used. The paper links no code and no data deposit, so no\n# repository was read.\n#\n# The datasets, from their titles on DANDI.\n# - 000489, \"The impact of the second phase amplitude (% to the first phase) on the electroporation\n#   efficiency (measured as YP emission)\", bovine cells. This is the title of Fig. 2A, so it is\n#   meant to hold the experiment of Fig. 2 (Results 3.1). The claims on Fig. 2 rest on it.\n# - 000448, \"Time kinetics of the membrane potential at the cathode- and anode-facing poles of a\n#   cell induced by a train of 5 pulses at 833 kHz\", Chinese hamster. This is the title of Fig. 7,\n#   the strobe imaging of CHO cells (Methods 2.6, Results 3.5). The claims on Fig. 7 rest on it.\n# - Neither title names the experiments of Figs. 3 to 6 (pulse number, duration, the aa' line,\n#   repetition rate) or the thermometry of Fig. 1E, and the paper gives no other data location.\n#   These claims are listed under 000489, the YO-PRO-1 uptake dataset of the same preparation and\n#   measure; whether it holds them is the author's to find, and they are blocked as data_missing\n#   if it does not. They are kept because they are the paper's main findings.\n#\n# Data the paper used, as it reports them.\n# - Electroporation experiments (Figs. 2 to 6). Monolayers of bovine pulmonary artery endothelial\n#   (BPAE) cells in 35 mm glass bottom dishes, in a physiological solution with 1 uM YO-PRO-1 (YP),\n#   pre-treated with propidium iodide and labeled with MemBrite Fix 405/430. Pulses were delivered\n#   by two hollow stainless-steel needles (1.5 mm, 3 mm apart) touching the glass. After 10 min the\n#   whole dish was imaged (216 tiles, 10x 0.38 NA, DAPI cube for MemBrite and FITC cube for YP) and\n#   stitched. Fluorescence was averaged in 200 um square ROI along the bb' line (equidistant from\n#   both electrodes; strongest field at the centre, falling towards the edges) or, for Fig. 5,\n#   along the aa' line (anode to cathode; weakest field at the centre). The measure is\n#   YP = YP_ROI x MB_0 / MB_ROI - YP_0, YP_0 and MB_0 measured within the electrode footprints.\n#   Each exposure protocol was tested 3 to 8 times (one dish per exposure); graphs show mean and\n#   s.e.m. Fig. 2, 5 pulses at 1 Hz, 600 ns phases, first phase 5.75 kV, second phase 0, 25, 50,\n#   75 or 100%. Fig. 3, 5, 10 or 15 pulses (600 ns, 600+600 ns at 50%), n = 3. Fig. 4, 5 pulses at\n#   1 Hz with phases of 300, 600 and 1200 ns (5.75 kV) and 50, 100 and 500 us (425, 350 and 250 V),\n#   second phase 50%. Fig. 5 re-analyzes the Fig. 4 dishes along aa'. Fig. 6, 5 pulses of 600 ns\n#   or 600+600 ns (50%) at 1 Hz, 10 to 500 kHz and 833 kHz.\n# - Strobe imaging (Fig. 7). CHO-K1 cells loaded with FluoVolt, tungsten rod electrodes (0.5 mm,\n#   1 mm apart, 50 um above the dish bottom), 37 V giving 0.3 kV/cm, trains of 5 pulses at 833 kHz,\n#   unipolar 600 ns (18 cells) or bipolar 600+600 ns with a 50% second phase (17 cells). The laser\n#   flash delay was stepped by 25 ns over 12.5 us (500 exposures at 6 per second). Each cell was\n#   recorded in two trials (ascending and descending delays) that were averaged. Pole signals were\n#   scaled to the whole-cell signal, the mean of the 40 points before the pulse taken as 100%, and\n#   expressed as percent difference from it.\n#\n# Inputs the paper relies on (step 4). The field strength of each ROI is not measured; it comes\n# from the paper's finite element model (Sim4Life V5.2, Methods 2.3, Fig. 1B and C), computed for\n# 1 V and scaled by the applied voltage. The model output is not deposited. Its geometry is given\n# in Methods 2.3 (two stainless-steel cylinders 1.5 mm in diameter, 3 mm apart, touching the glass\n# of a 35 mm dish filled to 3.5 mm with a 1.6 S/m solution, field taken 1 um above the glass), so\n# the author can recompute it if the dataset does not hold the field per ROI. For bipolar pulses\n# the field quoted is that of the first phase (Fig. 2 and Fig. 6 legends). The 15.1 kV/cm cited\n# for Fig. 2C at 5.75 kV is a check on the result.\n#\n# Details the paper leaves open, used by several criteria below.\n# - ROI placement. The paper gives the ROI size (200 um square) and the lines, not the spacing or\n#   the number of ROI. Readings are (a) contiguous ROI tiled outward from the centre along the line\n#   on both sides, and (b) the same on one side only. A named field strength (6.7, 8.7, 15.1\n#   kV/cm) is taken at the ROI whose mean field is closest to it. If the dataset holds the paper's\n#   own ROI values, those are used and the readings are not needed.\n# - The t-test. Methods 2.5 names a two-sided Student's t-test at p < 0.05 and does not say\n#   whether it is paired. Exposures with different pulse parameters are different dishes (or\n#   cells), so those comparisons are unpaired. Comparisons between ROI of the same dishes, or\n#   pulses of the same cells, can be read (a) unpaired, the two-sample test the name denotes, or\n#   (b) paired. For a claim of absence the protocol takes the paper's test as written, so (a) is\n#   the test and (b) is shown as a variant; for other claims both are run.\n# - Fits. Grapher 16 was used for fitting (Methods 2.5). Whether fits were made to mean values or\n#   to dish values, and whether exponential fits were least squares on linear values or linear\n#   regression on log values, is not given. Readings are named where an outcome depends on them.\n# - Where readings that are method choices give different outcomes, the author adopts the one the\n#   paper best supports, as an assumption, or blocks the claim as methods_underspecified (author,\n#   step 1.6). Where readings are of what a reported number means, a match under any suffices.\nschema_version: 2\ndatasets:\n- archive: dandi\n  id: \"000489\"\n- archive: dandi\n  id: \"000448\"\npaper: doi:10.1016/j.bioelechem.2022.108319\nclaims:\n- id: fig2a-uptake-rises-with-field\n  statement: For unipolar 600 ns pulses and for bipolar 600+600 ns pulses with every second phase\n    amplitude, a train of 5 pulses at 1 Hz evoked YP uptake that increased with the local electric\n    field strength.\n  source: Results 3.1, paragraph 1; Figure 2A\n  quote: A train of 5 pulses applied at 1 Hz evoked YP uptake proportionally to the local electric\n    field strength ( Fig. 2A ), along with a strong dependence on the 2 nd phase amplitude.\n  datasets:\n  - \"000489\"\n  criterion: YP per ROI along bb' as defined in Methods 2.5, with the field of each ROI from the\n    model (opening comment). The paper reports no test for this finding. For each of the five\n    second phase amplitudes (0, 25, 50, 75, 100%), the dish values at the ROI with the strongest\n    field are compared with those at the ROI with the weakest field by the paper's two-sided\n    Student's t-test (Methods 2.5), run unpaired and paired (opening comment). Reproduced when YP\n    is higher at the strongest field with p < 0.05 for all five amplitudes; partially reproduced\n    for three or four; not reproduced otherwise. The strongest against weakest comparison is this\n    file's reading of \"proportionally\". The Spearman correlation of mean YP with field across ROI\n    is reported for each amplitude as a description.\n- id: fig2a-vertical-scales\n  statement: The vertical scale of the Fig. 2A panels goes from 1200 a.u. for unipolar pulses down\n    to only 250 a.u. for bipolar pulses with a 75% second phase.\n  source: Results 3.1, paragraph 1; Figure 2A and its legend\n  quote: note the difference in the vertical scale, which is varied from 1200 a.u. for unipolar\n    pulses to only 250 a.u. for 75% bipolar pulses\n  datasets:\n  - \"000489\"\n  criterion: The numbers are axis limits, not measured values, so they bound the data. With YP in\n    the units of the dataset's fluorescence images, reproduced when the largest mean plus s.e.m.\n    over ROI is at most 1200 a.u. for unipolar pulses and at most 250 a.u. for 75% bipolar pulses,\n    and the largest unipolar mean exceeds 250 a.u. If the images are not in the units the paper\n    measured (for example rescaled on export), only the ratio of the two largest means is reported\n    and the claim is blocked on the absolute values.\n- id: fig2b-exponential-same-slope\n  statement: YP uptake increased exponentially with the field strength, and the second phase did\n    not change the slope of the exponential fits on a semi-log scale.\n  source: Results 3.1, paragraph 1; Figure 2B and its legend\n  quote: YP uptake increased exponentially with the electric field, and the presence of the 2nd\n    phase did not change the apparent slope of exponential fits when plotted on a semi-log scale\n  datasets:\n  - \"000489\"\n  criterion: As the Fig. 2B legend says, YP is fitted with an exponential function of field,\n    YP = A exp(kE), leaving out the low-signal ROI \"at less than 6-8 kV/cm\". The legend gives a\n    range, not one cutoff; 8 kV/cm is used, as it excludes what every amplitude excludes, and 6\n    and 7 kV/cm are shown as variants. Grapher's fitting method is open; nonlinear least squares\n    on linear YP is used (a standard choice) and linear regression of log YP on field is shown as\n    a variant. Exponential growth is judged from the fits to the mean values, which the legend\n    plots; it holds when the exponential fits with a lower residual sum of squares than a straight\n    line for at least four of five amplitudes (this rule is the file's; the paper gives none). The\n    slope part is a claim of absence for which the paper reports no test; it is judged by the\n    paper's test, a two-sided Student's t-test at p < 0.05 (Methods 2.5), comparing the slope k of\n    per-dish fits for each bipolar amplitude with the unipolar slopes (unpaired, as they are\n    different dishes). Reproduced when exponential growth holds and no bipolar slope differs from\n    the unipolar slope; not reproduced when any differs. Slopes and their ratios to the unipolar\n    slope are reported, with the slopes of the fits to the means and their standard errors.\n- id: fig2c-max-inhibition-50-75\n  statement: The strongest inhibition of YP uptake, to about 20% of the uptake after unipolar\n    pulses, was reached with a second phase of 50 to 75% of the first (p < 0.01).\n  source: Results 3.1, paragraph 2; Figure 2C and its legend\n  quote: The maximum inhibition of YP uptake, down to ~20% of the unipolar pulses, was achieved with\n    the 2 nd phase set to 50-75% of the first one (p<0.01, Fig. 2C ).\n  datasets:\n  - \"000489\"\n  statistics:\n  - test: two-sided Student's t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 3 to 8 exposures per protocol\n  expected:\n  - quantity: YP after bipolar pulses with the most effective second phase, as percent of unipolar\n    value: 20\n    tolerance: 2\n    unit: \"%\"\n  criterion: As the Fig. 2C legend says, for each selected field strength the YP for each\n    amplitude is expressed as percent of the unipolar YP at that field. The paper names 6.7, 8.7\n    and 15.1 kV/cm and does not list the other selected values; the ROI with fields from 8.7 to\n    15.1 kV/cm are used, the range where the text says inhibition did not depend on field.\n    Reproduced when the lower of the 50% and 75% values is below the 25% and 100% values at every\n    such field, the percent is within tolerance, and the p < 0.01 test holds. Which \"~20%\" is meant\n    is a reading of the number, and either suffices, (a) the mean percent over the fields from 8.7\n    to 15.1 kV/cm for the better of 50 and 75%, or (b) the lowest percent at any of those fields.\n    Which comparison carries p < 0.01 is not given; readings are (i) 50% and 75% dish YP against\n    unipolar dish YP, and (ii) 50% and 75% against 25% and 100%, each by an unpaired two-sided\n    Student's t-test (different dishes) at each field; either suffices. Partially reproduced when\n    the ordering and the test hold but the percent is outside tolerance under both readings.\n- id: fig2c-inhibition-flat-above-8-7\n  statement: Between 8.7 and 15.1 kV/cm the degree of inhibition by the second phase did not depend\n    on the field strength.\n  source: Results 3.1, paragraph 2; Figure 2C\n  quote: The degree of inhibition showed no dependence on the electric field strength between 8.7\n    and 15.1 kV/cm.\n  datasets:\n  - \"000489\"\n  criterion: A claim of absence, judged on the paper's test as written, the two-sided Student's\n    t-test at p < 0.05 (Methods 2.5), unpaired (opening comment). Each bipolar dish value is\n    divided by the unipolar mean at the same ROI (Fig. 2C legend, unipolar as 100%). For each\n    bipolar amplitude, the values at 8.7 kV/cm are compared with those at 15.1 kV/cm. Reproduced\n    when no amplitude shows a difference; not reproduced when any does. The size of each\n    difference is given; the paired test and the comparisons of every pair of ROI in the range are\n    shown as variants.\n  depends_on:\n  - fig2c-max-inhibition-50-75\n- id: fig2c-weaker-at-6-7\n  statement: Inhibition was weaker at 6.7 kV/cm than at the higher field strengths, with p < 0.01\n    for the 50% bipolar pulses and p < 0.05 for the 100% bipolar pulses.\n  source: Results 3.1, paragraph 2; Figure 2C\n  quote: However, inhibition was weaker at 6.7 kV/cm (p<0.01 compared to the higher electric field\n    strengths for 50% bipolar pulses, and p<0.05 for 100% bipolar pulses).\n  datasets:\n  - \"000489\"\n  statistics:\n  - about: 50% bipolar, 6.7 kV/cm against higher field strengths\n    test: two-sided Student's t-test\n    p: 0.01\n    p_relation: \"<\"\n  - about: 100% bipolar, 6.7 kV/cm against higher field strengths\n    test: two-sided Student's t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Bipolar dish YP as percent of the unipolar mean at the same ROI, as in\n    fig2c-inhibition-flat-above-8-7. For 50% and for 100% bipolar pulses, the value at the ROI\n    closest to 6.7 kV/cm is compared with the higher fields (ROI from 8.7 to 15.1 kV/cm) by a\n    two-sided Student's t-test (Methods 2.5). \"Compared to the higher electric field strengths\" is\n    read (i) against each higher field ROI and (ii) against the dish values of all higher field\n    ROI pooled; either suffices. Pairing is a method choice (opening comment); both are run.\n    Reproduced when the percent at 6.7 kV/cm is higher than at every higher field, with p < 0.01\n    for 50% and p < 0.05 for 100%; partially reproduced when it is higher at every field but the\n    test holds for only one amplitude.\n  depends_on:\n  - fig2c-max-inhibition-50-75\n- id: fig3-uptake-linear-in-pulse-number\n  statement: Uptake rose with field strength and with pulse number for both uni- and bipolar\n    pulses, almost linearly with the number of pulses, so that plots for 5, 10 and 15 pulses look\n    alike when the y-axis is scaled to 800, 1600 and 2400 a.u.\n  source: Results 3.2, paragraph 1; Figure 3A to C and legend\n  quote: Increasing the pulse number increased YP uptake almost linearly [ 15 ]. Therefore, YP\n    uptake plots for 5, 10, and 15 pulses appeared almost identical when plotted with the y-axis\n    scaled proportionally (to 800, 1600, and 2400 a.u., respectively).\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: YP for 10 pulses over YP for 5 pulses\n    value: 2\n    tolerance: 0.2\n  - quantity: YP for 15 pulses over YP for 5 pulses\n    value: 3\n    tolerance: 0.3\n  criterion: The expected 2 and 3 are read from the proportional axis limits and \"almost\n    linearly\"; the paper prints no ratio. Mean YP per ROI along bb' for each pulse type and number,\n    leaving out the ROI below the background cutoff the text gives for Fig. 3 (\"<7-8 kV/cm\",\n    Results 3.2), read as 7 and as 8 kV/cm. The paper does not say how the ratio is taken;\n    readings are (a) the mean over ROI of the ratio of means, and (b) the ratio of the 2nd degree\n    polynomial fits the paper used (Fig. 3 legend) averaged over the included field range. These\n    are method choices, run together. Reproduced when both ratios are within tolerance for\n    unipolar and for bipolar pulses; partially reproduced when they are for one pulse type.\n- id: fig3d-cancellation-independent-of-number\n  statement: The relative efficiency of 50% bipolar pulses was the same for 5, 10 and 15 pulses and\n    did not depend on the field strength.\n  source: Results 3.2, paragraph 2; Figure 3D and its legend\n  quote: The plots for 5, 10, and 15 pulses nearly overlapped, showing that within the studied\n    limits cancellation of electroporation by adding a 50% opposite polarity phase did not depend\n    on the pulse number or the electric field strength.\n  datasets:\n  - \"000489\"\n  criterion: A claim of absence, for which the paper reports no test; it is judged on the paper's\n    test, the two-sided Student's t-test at p < 0.05 (Methods 2.5), unpaired. The measure, as the\n    Fig. 3 legend and Results 3.2 say, is bipolar over unipolar YP over fields above the\n    background cutoff (8 kV/cm, the upper end of \"<7-8 kV/cm\", so that every included ROI is above\n    background; 7 kV/cm is a variant). For the test, each bipolar dish value is divided by the\n    unipolar mean at the same ROI and pulse number. Pulse number, (i) at each included ROI the\n    three pairs of pulse numbers are compared. Field, (ii) for each pulse number the lowest and\n    highest included ROI are compared. Reproduced when no comparison differs; not reproduced when\n    any does. The ratio of the 2nd degree polynomial fits (the curves of Fig. 3D) is reported for\n    each pulse number, with its range.\n- id: fig4ac-ns-bipolar-20-25pct\n  statement: Bipolar 300+300 and 600+600 ns pulses with a 50% second phase gave 20 to 25% of the\n    uptake of the respective unipolar pulses, independent of the field strength.\n  source: Results 3.3, paragraph 1; Figure 4A to D\n  quote: Electroporation by 300+300 and 600+600 ns pulses was at 20-25% of the respective unipolar\n    pulses and did not depend on the electric field strength.\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: bipolar over unipolar YP, 300 ns phases\n    value: 22.5\n    unit: \"%\"\n  - quantity: bipolar over unipolar YP, 600 ns phases\n    value: 22.5\n    unit: \"%\"\n  criterion: The reported range 20 to 25% is widened by 10% of each bound, to 18 to 27.5%. The\n    ratio is that of the fits of bipolar and unipolar mean YP against field (Fig. 4 legend). The\n    legend says \"either exponential or polynomial\" without saying which for which curve; the\n    readings, method choices run together, are (a) exponential for all, (b) 2nd degree polynomial\n    for all, as in Fig. 3, and (c) for each curve the one with the lower residual sum of squares.\n    The Fig. 4 legend refers to Fig. 2 and the text and states no background cutoff; the Fig. 3\n    cutoff (Results 3.2, 7 to 8 kV/cm) is used, read as 7 and 8. Reproduced when, for both\n    durations, the ratio stays in 18 to 27.5% over the included range and the field independence\n    holds; partially reproduced when the mean ratio over the range is inside but the curve leaves\n    it somewhere. Field independence is a claim of absence, judged on the paper's two-sided\n    Student's t-test at p < 0.05, unpaired, of dish ratios (bipolar dish YP over the unipolar mean\n    at the same ROI) between the lowest and highest included ROI.\n- id: fig4d-1200ns-tenfold\n  statement: Bipolar 1200+1200 ns pulses cancelled more at moderate field strengths, reducing YP\n    uptake tenfold.\n  source: Results 3.3, paragraph 1; Figure 4D\n  quote: However, longer 1200+1200 ns pulses were somewhat more efficient at cancellation at\n    moderate electric field strengths, reducing the YP fluorescence 10-fold ( Fig. 4D ).\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: bipolar over unipolar YP, 1200 ns phases, at moderate field\n    value: 10\n    tolerance: 1\n    unit: \"%\"\n  criterion: Ratio of the fits of bipolar and unipolar mean YP against field, with the fit readings\n    of fig4ac-ns-bipolar-20-25pct. \"Moderate\" is not defined; it is read (a) as the lowest value\n    of the ratio curve over the included field range and (b) as the ratio at the middle of that\n    range; either suffices. Reproduced when the value is within tolerance and below the 300 and\n    600 ns ratios at the same field.\n- id: fig4eg-us-bipolar-30-50pct\n  statement: A 50% second phase also reduced uptake by 50, 100 and 500 us pulses, to 30 to 50% of\n    the unipolar effect, a weak but highly significant cancellation (p < 0.01).\n  source: Results 3.3, paragraph 2; Figure 4E to H\n  quote: Cancellation by these longer pulses was relatively weak (to 30-50% of the unipolar pulse\n    effect) but highly significant (p<0.01).\n  datasets:\n  - \"000489\"\n  statistics:\n  - test: two-sided Student's t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 3 to 8 exposures per protocol\n  expected:\n  - quantity: bipolar over unipolar YP, 50 to 500 us phases\n    value: 40\n    unit: \"%\"\n  criterion: The reported range 30 to 50% is widened by 10% of each bound, to 27 to 55%. For each\n    of the three durations, the ratio of the fits of bipolar and unipolar mean YP against field\n    (Fig. 4 legend, fit readings as in fig4ac-ns-bipolar-20-25pct). The paper gives no cutoff for\n    measurable uptake with microsecond pulses, whose field range is lower; this is open, and the\n    ROI with unipolar mean YP above zero by more than its s.e.m. are used, the ratio being shown at\n    every ROI. \"To 30-50%\" is read (i) as the ratio's mean over that range and (ii) as the ratio\n    staying in the range throughout; either suffices. Which comparison carries the single p < 0.01\n    is not given; it is read as bipolar against unipolar dish YP by an unpaired two-sided\n    Student's t-test, (a) at most included ROI or (b) on dish YP summed over the included ROI;\n    either suffices. Reproduced when, for all three durations, the ratio is in 27 to 55% and the\n    test holds; partially reproduced for one or two durations.\n- id: fig4h-us-stronger-at-low-field\n  statement: For microsecond pulses, cancellation was stronger at lower field strengths.\n  source: Results 3.3, paragraph 2; Figure 4H; Discussion, paragraph 1\n  quote: The trend for more efficient cancellation at the lower electric field strengths persisted\n    throughout the microsecond range ( Fig. 4H ).\n  datasets:\n  - \"000489\"\n  criterion: The ratio of the bipolar and unipolar fits (Fig. 4 legend, fit readings as in\n    fig4ac-ns-bipolar-20-25pct) for 50, 100 and 500 us pulses, over the ROI used in\n    fig4eg-us-bipolar-30-50pct. Reproduced when the ratio is higher at the highest than at the\n    lowest included field for all three durations; partially reproduced for one or two. The paper\n    calls this a trend and reports no test; dish ratios (bipolar dish YP over the unipolar mean)\n    at the lowest and highest included ROI are compared by an unpaired two-sided Student's t-test\n    (Methods 2.5) and reported.\n  depends_on:\n  - fig4eg-us-bipolar-30-50pct\n- id: fig5-ns-symmetric-along-aa\n  statement: Along the line from anode to cathode, YP uptake was nearly symmetrical for 300 and 600\n    ns pulses.\n  source: Results 3.3, paragraph 4; Figure 5A and B\n  quote: YP uptake data measured along the aa' line was nearly symmetrical for 300- and 600-ns\n    pulses ( Fig. 5A , B ).\n  datasets:\n  - \"000489\"\n  criterion: A claim of absence, judged on the paper's test as written, the two-sided Student's\n    t-test at p < 0.05 (Methods 2.5), unpaired (opening comment). ROI along aa' (Methods 2.3 and\n    2.5, Fig. 5 legend) in the Fig. 4 dishes; each anodic ROI is matched with the cathodic ROI at\n    the same distance from the centre. YP at the two sides is compared at each distance, for uni-\n    and bipolar 300 and 600 ns pulses. Reproduced when no distance shows a difference; not\n    reproduced when any does. The anode over cathode ratio is reported at each distance, and the\n    paired test is shown as a variant.\n- id: fig5-us-anode-stronger\n  statement: For 50 to 500 us pulses, YP uptake was significantly stronger on the anodic side\n    (p < 0.01), and for 1200 ns unipolar pulses marginally stronger there.\n  source: Results 3.3, paragraph 4; Figure 5C to F\n  quote: At 1200 ns, the effect of unipolar pulses appeared marginally stronger at the anodic side\n    ( Fig. 5C ), and still longer 50-500 μs pulses showed significantly stronger YP uptake (p<0.01)\n    at the anodic site.\n  datasets:\n  - \"000489\"\n  statistics:\n  - about: anodic against cathodic side, 50 to 500 us pulses\n    test: two-sided Student's t-test\n    p: 0.01\n    p_relation: \"<\"\n  criterion: ROI along aa', matched by distance from the centre as in fig5-ns-symmetric-along-aa.\n    Reproduced when, for each of 50, 100 and 500 us unipolar pulses, anodic YP exceeds cathodic YP\n    with p < 0.01 by the two-sided Student's t-test (pairing run both ways, opening comment) at\n    one or more distances, and the 1200 ns unipolar anodic mean exceeds the cathodic mean at most\n    distances. Partially reproduced when the microsecond part holds for one or two durations.\n    Bipolar pulses are reported as well; the text does not say whether its p < 0.01 covers them.\n- id: fig6ad-unipolar-833khz-enhanced\n  statement: Unipolar 600 ns pulse trains at 10 to 500 kHz were as efficient as at 1 Hz, while at\n    833 kHz uptake was 2 to 3 times higher across the field range.\n  source: Results 3.4, paragraph 1; Figure 6A and D\n  quote: Unipolar pulses at 10 to 500 kHz showed the same efficiency as at 1 Hz ( Fig. 6A , D ).\n    ... YP uptake after 833 kHz exposure was 2-3 fold higher than at other frequencies throughout\n    the studied range of the electric field strengths.\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: unipolar YP at 833 kHz over YP at other frequencies\n    value: 2.5\n    unit: fold\n  criterion: The reported range 2 to 3 is widened by 10% of each bound, to 1.8 to 3.3. Mean YP per\n    ROI along bb' for each repetition rate, over ROI with uptake above background (the paper gives\n    no cutoff for Fig. 6; the Fig. 3 cutoff of 7 to 8 kV/cm is used, read as 7 and 8). The fold is\n    the 833 kHz mean over the mean of each other rate at the same ROI. \"The same efficiency\" is a\n    claim of absence, judged on the paper's two-sided Student's t-test at p < 0.05, unpaired\n    (different dishes), of each rate from 10 to 500 kHz against 1 Hz at each ROI. Reproduced when\n    the fold is in 1.8 to 3.3 at every included ROI and no 10 to 500 kHz rate differs from 1 Hz;\n    partially reproduced when one of the two holds.\n- id: fig6be-bipolar-khz-less-than-1hz\n  statement: Bipolar 600+600 ns pulse trains at all kHz rates were less efficient than at 1 Hz,\n    barely above background, the difference being largest (2.5 times) at the highest field.\n  source: Results 3.4, paragraph 2; Figure 6B and E\n  quote: In contrast, the efficiency of bipolar pulses at all kHz frequencies was less than at 1 Hz,\n    and the electroporative uptake of YP was just marginally above the background level ( Fig. 6B ,\n    E ). The difference between 1 Hz and kHz-rate trains was maximum (2.5 times) at the highest\n    electric field strength.\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: bipolar YP at 1 Hz over YP at kHz rates, highest field\n    value: 2.5\n    tolerance: 0.25\n    unit: fold\n  criterion: Mean YP per ROI along bb'. \"The difference between 1 Hz and kHz-rate trains\" is read\n    (a) against the mean over all kHz rates and (b) against each kHz rate; either suffices.\n    Reproduced when the mean at every kHz rate (10 to 833 kHz) is below the 1 Hz mean at the ROI\n    with the strongest field, the largest 1 Hz over kHz ratio over ROI is at that ROI, and that\n    ratio is within tolerance.\n- id: fig6cf-833khz-thirtyfold\n  statement: At 833 kHz and 12 to 15 kV/cm, bipolar pulses had only 3 to 4% of the effect of\n    unipolar pulses, about a 30-fold reduction, the strongest cancellation in the study.\n  source: Results 3.4, paragraph 3; Figure 6C and F\n  quote: At 12-15 kV/cm, the effect of bipolar pulses at 833 kHz was only 3-4% of the effect of\n    unipolar pulses (~30-fold reduction).\n  datasets:\n  - \"000489\"\n  expected:\n  - quantity: bipolar over unipolar YP at 833 kHz, 12 to 15 kV/cm\n    value: 3.5\n    unit: \"%\"\n  criterion: The reported range 3 to 4% is widened by 10% of each bound, to 2.7 to 4.4%. The ratio\n    is that of the fits of bipolar and unipolar mean YP against field at 833 kHz (Fig. 6 legend,\n    \"either exponential or polynomial\"; fit readings as in fig4ac-ns-bipolar-20-25pct). The ratio\n    of means at each ROI is shown as a variant. Reproduced when the ratio is within 2.7 to 4.4% at\n    the fields from 12 to 15 kV/cm and lower than the ratio at every other repetition rate there.\n- id: fig6cf-cancellation-stronger-at-high-field\n  statement: For high-frequency bursts of nsEP, a stronger electric field enhanced bipolar\n    cancellation.\n  source: Discussion, paragraph 1; Figure 6C and F\n  quote: For high-frequency nsEP bursts, stronger electric field enhanced cancellation ( Fig. 6C ,\n    F ).\n  datasets:\n  - \"000489\"\n  criterion: The ratio of the fits of bipolar and unipolar mean YP against field (Fig. 6 legend,\n    fit readings as in fig4ac-ns-bipolar-20-25pct) for each kHz rate, over the ROI with unipolar\n    uptake above background (cutoff as in fig6ad-unipolar-833khz-enhanced). \"High-frequency\" is\n    not defined; it is read (a) as 833 kHz only and (b) as every kHz rate from 10 to 833 kHz;\n    either suffices. Reproduced when the ratio is lower at the highest than at the lowest included\n    field. The paper reports no test; dish ratios (bipolar dish YP over the unipolar mean at the\n    same ROI) at the lowest and highest included ROI are compared by an unpaired two-sided\n    Student's t-test (Methods 2.5) and reported.\n- id: fig7-unipolar-pole-polarization\n  statement: Unipolar 600 ns pulses depolarized the membrane quickly at the cathode-facing pole of\n    the cell and hyperpolarized it in mirror image at the anode-facing pole.\n  source: Results 3.5, paragraph 1; Figure 7\n  quote: Unipolar nsEP caused fast membrane depolarization at the cathode-facing pole of the cell,\n    and a mirroring hyperpolarization at the anode-facing pole.\n  datasets:\n  - \"000448\"\n  criterion: FluoVolt emission at each pole of the 18 cells given unipolar pulses, processed as\n    Methods 2.6 says (scaled to whole-cell emission, the two trials of each cell averaged, the mean\n    of the 40 points before the pulse as 100%, percent difference from it). Which sign of emission\n    change means depolarization is not given in the text; the cathodic pole change during the\n    first pulse fixes it, and the anodic pole must then change with the opposite sign. Reproduced\n    when, at the end of the first pulse (600 ns), the cathodic and anodic values differ from zero\n    in opposite directions by a two-sided one-sample Student's t-test across cells at p < 0.05\n    (the Methods 2.5 test and threshold applied by this file, as the paper reports no test here),\n    and the anodic change is of similar size (its magnitude within half to twice the cathodic,\n    a tolerance of the file's for \"mirroring\").\n- id: fig7-charging-time-constant\n  statement: Fitting the cathodic pole response to the first unipolar pulse gave a charging time\n    constant of 200 ns and a maximum polarization of 31% emission change (425 points, r = 0.93,\n    p < 0.0001), and the discharge after it a time constant of 520 ns from 31.5% (425 points,\n    r = 0.85, p < 0.0001).\n  source: Results 3.5, paragraph 2; Figure 7 (dotted lines, top panel) and legend\n  quote: The best fit for membrane charging with an exponential function (using the first pulse in\n    the unipolar pulse train) yielded the time constant of 200 ns and the maximum membrane\n    polarization at 31% emission change (425 datapoints, correlation coefficient 0.93,\n    p<0.0001). The best fit for the discharging portion of the curve yielded the same initial\n    polarization (31.5% emission change) but, unexpectedly, a 2.5 times larger time constant of\n    520 ns\n  datasets:\n  - \"000448\"\n  statistics:\n  - about: charging fit\n    test: exponential fit, correlation coefficient\n    statistic: r = 0.93\n    p: 0.0001\n    p_relation: \"<\"\n    n: 425 datapoints\n  - about: discharging fit\n    test: exponential fit, correlation coefficient\n    statistic: r = 0.85\n    p: 0.0001\n    p_relation: \"<\"\n    n: 425 datapoints\n  expected:\n  - quantity: charging time constant\n    value: 200\n    tolerance: 20\n    unit: ns\n  - quantity: maximum polarization, charging fit\n    value: 31\n    tolerance: 3.1\n    unit: \"% emission change\"\n  - quantity: discharging time constant\n    value: 520\n    tolerance: 52\n    unit: ns\n  - quantity: initial polarization, discharging fit\n    value: 31.5\n    tolerance: 3.15\n    unit: \"% emission change\"\n  criterion: Cathodic pole traces of the 18 unipolar cells, processed as in\n    fig7-unipolar-pole-polarization. A single exponential (Fig. 7 legend) is fitted to the first\n    pulse (0 to 600 ns, charging, A(1 - exp(-t/tau))) and to the interval from its end to the next\n    pulse (600 to 1200 ns at 833 kHz, discharge, A exp(-t/tau)). The paper does not say which\n    points were fitted. The 425 datapoints are close to 18 cells times 24 time steps of 25 ns\n    (432), so the readings are (a) per-cell points pooled, the reading the count supports, and (b)\n    the trace averaged over cells. These are method choices, run together. Reproduced when all\n    four values are within tolerance and both correlations have p < 0.0001; partially reproduced\n    when the two time constants are within tolerance and the discharge constant exceeds the\n    charging constant, but an amplitude is not.\n- id: fig7-later-pulses-same-tau-difference\n  statement: Fits to the later pulses of the unipolar train gave the same kind of difference\n    between charging and discharging time constants as the first pulse.\n  source: Results 3.5, paragraph 2\n  quote: Fitting the membrane potential for the next pulses in the train consistently produced\n    similar differences between the charging and discharging time constants (data not shown).\n  datasets:\n  - \"000448\"\n  criterion: The paper shows no data for this finding. The fits of fig7-charging-time-constant,\n    under the same readings, are repeated for pulses 2 to 5 (each pulse and the interval after it;\n    after pulse 5 the discharge is fitted over 600 ns, the same span as for the others). \"Similar\n    differences\" is read as the discharge constant exceeding the charging constant, with a ratio\n    within 10% of the paper's 2.5 (2.25 to 2.75) as one reading and within 10% of the first\n    pulse's ratio as found here as another; either suffices. Reproduced when this holds for all\n    four later pulses; partially reproduced when the discharge constant is larger for all four but\n    the ratio holds for fewer.\n  depends_on:\n  - fig7-charging-time-constant\n- id: fig7-bipolar-overshoot\n  statement: Bipolar pulses caused the same initial polarization as unipolar ones during the first\n    phase, followed by a faster discharge and an overshoot into the opposite polarity.\n  source: Results 3.5, paragraph 1; Figure 7\n  quote: Bipolar nsEP caused the same initial polarization during the first phase of the pulse,\n    followed by a faster discharge and an overshoot into the opposite polarity.\n  datasets:\n  - \"000448\"\n  criterion: Cathodic pole traces as in fig7-unipolar-pole-polarization, for the 17 bipolar and 18\n    unipolar cells. Reproduced when (i) at the end of the first phase (600 ns) the bipolar and\n    unipolar cell values do not differ by the paper's two-sided Student's t-test at p < 0.05\n    (Methods 2.5; unpaired, as they are different cells), a claim of absence judged on that test,\n    with the paper's error bar gap rule (Methods 2.5) shown as a variant; (ii) after the first\n    phase the bipolar mean trace returns to the resting level sooner than the unipolar trace; and\n    (iii) during the second phase (600 to 1200 ns) the bipolar mean goes below the resting level,\n    the cell values at its minimum differing from zero by a two-sided one-sample Student's t-test\n    at p < 0.05 (the Methods 2.5 test and threshold applied by this file, as the paper reports no\n    test here).\n- id: fig7-summation-without-buildup\n  statement: With 600 ns unipolar pulses at 833 kHz, each pulse charged the membrane to the same\n    peak, with no stepwise build-up; the pulses merged into a continuous sawtooth polarization.\n  source: Results 3.5, paragraph 3; Figure 7\n  quote: Although charging by the subsequent pulses in unipolar pulse trains started with the\n    partially charged membrane, it reached the same peak potential. A stepwise build-up of the peak\n    membrane potential ... did not occur in our experiments with 833-kHz, 600-ns unipolar pulses.\n  datasets:\n  - \"000448\"\n  criterion: Cathodic pole traces of the unipolar cells as in fig7-unipolar-pole-polarization. The\n    peak of each pulse is the value at its end. No build-up is a claim of absence, judged on the\n    paper's test as written, the two-sided Student's t-test at p < 0.05 (Methods 2.5), unpaired\n    (opening comment), comparing each of the peaks of pulses 2 to 5 with the first; the paired test\n    is shown as a variant. The continuous polarization is judged by the trace before each of\n    pulses 2 to 5 staying above the resting level, its value there differing from zero by a\n    two-sided one-sample Student's t-test across cells at p < 0.05 (the Methods 2.5 test applied\n    by this file). Reproduced when no later peak differs from the first and the trace stays above\n    rest before every later pulse; not reproduced when a later peak differs from the first.\n- id: fig1e-heating\n  statement: In the worst case tested, trains of 5 bipolar pulses (second phase 50%) at 1 Hz heated\n    the sample to no more than 30 degrees C; at 833 kHz heating exceeded 30 degrees C but never\n    reached 44 degrees C, and stayed close to 30 degrees C along the bb' line.\n  source: Methods 2.4, paragraph 2; Figure 1E\n  quote: Pulses applied at 1 Hz (the repetition rate used in all but one sets of experiments) caused\n    only modest heating, not exceeding 30 °C. At a high repetition rate of 833 kHz, heating exceeded\n    30 °C but never reached the next transition point of 44 °C and remained close to 30 °C (green\n    to blue transition) along the bb' line\n  datasets:\n  - \"000489\"\n  criterion: Measured with thermochromic liquid crystal sheets photographed with a camera (Methods\n    2.4; transitions at 25, 26, 30 and 44 degrees C). Reproduced when the photographs show no blue\n    at 1 Hz, and at 833 kHz blue somewhere, no return to black (44 degrees C), and no more than the\n    green to blue transition along bb'. Neither dataset's title names these photographs.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kim-2022.yaml paper/10.1016-j.bioelechem.2022.108319.txt; python3 -c "
import yaml;d=yaml.safe_load(open('claims/kim-2022.yaml'));c=d['claims']
print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "schema\|SCHEMA" tools/claims_check.py | head; ls schemas 2>/dev/null || find . -name "*claims*schema*" -not -path "./node_modules/*" | head
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
25:from entry import _plain, schema  # noqa: E402
82:    for err in schema("claims").iter_errors(_plain(doc)):
83:        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(s.get('required'));print(json.dumps({k:v for k,v in s['properties'].items() if k!='claims'},indent=1)[:1500]); print(json.dumps(s['properties']['claims']['items']['properties'].get('datasets')))"
```

```
['schema_version', 'paper', 'claims']
{
 "schema_version": {
  "const": 2
 },
 "dataset": {
  "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
  "type": "object",
  "additionalProperties": false,
  "required": [
   "archive",
   "id"
  ],
  "properties": {
   "archive": {
    "description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
    "type": "string",
    "pattern": "^[a-z][a-z0-9-]*$"
   },
   "id": {
[... 42 more lines not kept]
```

**Agent**

Top-level `dataset` is dropped for a paper's own file; I'll remove the top-level `datasets` block.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2022.yaml",
 "old_string": "schema_version: 2\ndatasets:\n- archive: dandi\n  id: \"000489\"\n- archive: dandi\n  id: \"000448\"\npaper:",
 "new_string": "schema_version: 2\npaper:"
}
```

```
The file claims/kim-2022.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kim-2022.yaml paper/10.1016-j.bioelechem.2022.108319.txt; grep -nP "—|\brather\b" claims/kim-2022.yaml; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent**

I've brought `claims/kim-2022.yaml` up to the current protocol (pilot-14). The quote checker passes with 0 problems, and nothing is committed.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC9729435, NIHMS1849847), not the version of record. It has the Methods 2.1 to 2.6, the Results 3.1 to 3.5, the Discussion and the legends of Figs. 1 to 7. The paper has no supplement, and none was supplied. There was no PDF, so I read no figures. The paper links no code and no data deposit, so I read no repository.

**Counts.** There are 24 claims. All 24 have quotes and criteria, 5 carry statistics (7 values), and 9 have expected values.
- **000489:** the 6 claims on Fig. 2 rest on it, since its title is the Fig. 2A legend.
- **000448:** the 5 claims on Fig. 7 rest on it, since its title is the Fig. 7 legend.
- **Figs. 3 to 6 and the Fig. 1E heating (13 claims):** neither dataset's title names these data. I listed them under 000489, the YO-PRO-1 dataset from the same cells and measure. The opening comment says the author must check whether 000489 holds them; if it does not, they are blocked as `data_missing`.

**What changed**
- The top-level `dataset: 000489` is gone, as the schema requires for a paper's own claims file, and every claim now has `datasets:`.
- I added two Fig. 7 claims: `fig7-unipolar-pole-polarization` and `fig7-later-pulses-same-tau-difference`. The second is a "data not shown" finding that 000448 can test.
- The claims of absence (fig2b slope, fig2c flat, fig3d, fig4ac field independence, fig5 symmetry, fig6 same efficiency, fig7 same initial polarization and no build-up) are now judged on a single test: the paper's unpaired two-sided Student's t-test at p < 0.05. The paired test is shown as a variant.
- Where readings are method choices and give different outcomes, the author now picks one or blocks the claim as `methods_underspecified`. Before, the file declared that outcome directly. Readings of what a reported number means still need only one match.
- fig4eg now has a stated rule for which ROI count as measurable uptake, and two readings of what the p < 0.01 covers. fig4d's statement no longer says "a tenth of unipolar".
- I removed the old `checks` block. Its last entry said `ready: true` about the previous version, so the new file needs a fresh check.

**Details the paper leaves open, and the readings named**
- **ROI spacing and count along bb' and aa':** ROIs tiled from the centre on both sides, or on one side only. A named field strength is taken from the ROI closest to it.
- **Paired or unpaired t-test for comparisons within the same dishes or cells:** both are run. For claims of absence the unpaired test decides.
- **Grapher fitting:** nonlinear least squares, or regression on log values. Fits to means, or to each dish.
- **Fig. 4 and Fig. 6 fit type** ("either exponential or polynomial"): exponential for all, polynomial for all, or the better fit per curve.
- **Background cutoffs:** Fig. 2B "6-8 kV/cm" uses 8, with 6 and 7 as variants. For Figs. 3, 4 and 6 the Fig. 3 cutoff is read as 7 or 8 kV/cm. Microsecond pulses have no cutoff, so the file uses ROIs where unipolar YP is above zero by more than its s.e.m.
- **Which "~20%" (fig2c):** the mean over 8.7 to 15.1 kV/cm, or the lowest value in that range. The p < 0.01 is read as against unipolar, or against 25% and 100%.
- **What "moderate" field means (fig4d):** the lowest value of the ratio curve, or the ratio mid-range.
- **What "high-frequency" means (fig6cf):** 833 kHz only, or every kHz rate.
- **"30-50%" and its p < 0.01 (fig4eg):** the mean over the range or the whole curve; tested at most ROIs or on summed dish values.
- **The 425 fitted points (Fig. 7):** per-cell points pooled, or the trace averaged over cells.
- **Fig. 7 sign:** which direction of emission change means depolarization is fixed from the data itself. "Mirroring" is given a tolerance of the file's own: anodic size within half to twice the cathodic.

**Missing from the paper.** These gaps affect claims:
- The paper gives no data location for Figs. 3 to 6 or the heating photographs, and neither dataset's title names them.
- The finite element field model behind each ROI's field strength is not deposited. Its geometry is in Methods 2.3, so the author can recompute it.
- The paper links no code.
- Several findings (fig2a, fig3d, fig4h, fig6cf trend, the fig7 sign tests) have no reported test. Their criteria apply the general Methods 2.5 t-test, and the file says so.

## End of run

27 turns, 4 minutes, $1.73 at API prices, result: success.
