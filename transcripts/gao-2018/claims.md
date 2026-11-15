# gao-2018 · claims · run 43584476169

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/; wc -l claims/gao-2018.yaml claims/fouke-2025.yaml
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
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
 "file_path": "claims/gao-2018.yaml"
}
```

```
1	# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), "A
2	# cortico-cerebellar loop for motor planning", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,
3	# tested on DANDI:000007 (same title on the archive; its description reads "Extracellular recording
4	# in ALM").
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
6	# protocol as stated in docs/protocol.md (version pilot-14).
7	#
8	# Text read: the NIH author manuscript (PMC6212318, NIHMS1504009) as served by Europe PMC, stored
9	# under paper/: main text, Methods, the legends of Figs. 1 to 4 and Extended Data Figs. 1 to 10;
10	# supplement 1 (Supplementary Information, 5 pages: Extended Data Fig. 10 discussion, cerebellar
11	# circuitry discussion, Supplemental Table 1 listing mice and hemispheres) and supplement 2 (the
12	# Nature reporting summary). There is no PDF of the main paper, so values and significance marks
13	# drawn only inside the figures could not be read; claims rest on the text and legends.
14	# Code: the paper links none. Its Code availability says "Software used for data analysis is
15	# available from the corresponding author upon reasonable request"; the reporting summary says
16	# scripts "will be deposited on CRCNS.org" but gives no identifier. No code was read, so every
17	# method detail below is from the Methods, legends or supplement, or is named as open.
18	#
19	# Data the paper used, as it reports them (Methods; Supplemental Table 1):
20	#  - Task. Head-fixed mice report the location of a pole (anterior or posterior) by licking left or
[... 907 more lines not kept]
```

**Agent calls Bash**

```bash
head -30 paper/10.1038-s41586-018-0633-x.txt; wc -c paper/*; cat papers/datasets/gao-2018.yaml; git log --oneline -8 -- docs/protocol.md; git log --oneline -3 -- paper claims/gao-2018.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n "^=\|^--\|^[A-Z][A-Za-z ,-]\{3,60\}$" 10.1038-s41586-018-0633-x.txt | head -80; for f in *.pdf; do echo "== $f"; pdftotext -l 1 "$f" - 2>/dev/null | head -15; pdfinfo "$f" | grep Pages; done
```

```
Exit code 1
6:------------------------------------------------------------------------
7:A cortico-cerebellar loop for motor planning
331:Author information
338:Letter
340:A cortico-cerebellar loop for motor planning
346:SUPPLEMENTARY INFORMATION
446:Experiment 
448:Figures 
450:Fastigial lesion 
456:Dentate lesion 
499:CN recording 
500:CN recording, 
510:CN recording 
520:ALM recording 
521:ALM recording  
531:ALM recording  
543:ALM recording 
553:Unilateral ALM photo-inhibition, 
561:Bilateral ALM photo-inhibition, 
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "" 10.1038-s41586-018-0633-x.txt | awk -F: 'length($0)<120' | sed -n '1,400p' | grep -v "^[0-9]*:$" | head -150
```

```
1:DOI: 10.1038/s41586-018-0633-x
2:Version: version of record, PMC6212318 (open access)
3:Source: europepmc fullTextXML
4:Stored: 2026-11-06
5:Extracted: JATS XML flattened
6:------------------------------------------------------------------------
7:A cortico-cerebellar loop for motor planning
45:## Methods
47:## Mice
53:## Surgery
59:## Behavior
65:## CN Lesion
69:## CN ChR2 photo-activation
77:## CN photo-inhibition
87:## CN photo-inhibition and effects on movement
95:## ALM photo-inhibition
101:## ALM photo-inhibition after a fastigial perturbation
107:## Behavioral data analysis
111:## Electrophysiology
119:## Electrophysiology data analysis
[... 130 more lines not kept]
```

**Agent**

Text now present: version of record (PMC6212318) with Methods, Extended Data legends and the Supplementary Information. Reading it in full.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-018-0633-x.txt",
 "offset": 29,
 "limit": 145
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -o ".\{80\}197.\{40\}\|.\{80\}329.\{40\}\|.\{60\}256.\{40\}" 10.1038-s41586-018-0633-x.txt; for f in *.pdf; do echo "== $f"; pdftotext "$f" - 2>/dev/null | head -c 600; echo; pdftotext "$f" - | grep -c "\f"; done
```

```
Exit code 1
35:hods). Activity of many ALM neurons was rapidly altered by CN photo-inhibition (197/454, p<0.01, two-tailed t-test, Extende
35:.39 spikes/s; p=0.58, two-tailed t-test). Individual ALM neurons increased (108/197) or decreased (89/197) their responses 
49:7-cre 31 crossed to Ai32 (Rosa26-LSL-ChR2-EYFP, JAX Stock#012569) 32 mice were used for CN photo-inhibi
== 10.1038-s41586-018-0633-x.supp-41586_2018_633_MOESM1_ESM.pdf

/bin/bash: line 1: pdftotext: command not found
0
== 10.1038-s41586-018-0633-x.supp1.pdf

/bin/bash: line 1: pdftotext: command not found
0
== 10.1038-s41586-018-0633-x.supp2.pdf

/bin/bash: line 1: pdftotext: command not found
0
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-018-0633-x.txt",
 "offset": 174,
 "limit": 172
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python -c "
import importlib
for m in ['fitz','pypdf','PyPDF2','pdfminer','pdfplumber']:
    try: importlib.import_module(m); print('have',m)
    except Exception: pass
"; sed -n '440,600p' 10.1038-s41586-018-0633-x.txt
```

```
3 
 
 
Experiment 
Mice ID / hemisphere 
Figures 
CN lesion (wild-type mice) 
Fastigial lesion 
(n=4) 
AN098 (left FN), AN101 (right FN) 
AN099 (left FN), AN103 (right FN) 
Figure 1d-e 
Extended Data Figure 1a-c 
Dentate lesion 
(n=4) 
AN104 (left DN), AN100 (right DN) 
CD05 (right DN), NL13 (right DN) 
Figure 1d 
Extended Data Figure 1a 
CN ChR2 photo-activation (ChR2 virus in wild-type mice) 
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l 10.1038-s41586-018-0633-x.txt; grep -n "#####\|Fig 1\b\|Figure 1 \|n=75\|75–256\|Reporting\|CRCNS" 10.1038-s41586-018-0633-x.txt | head; strings 10.1038-s41586-018-0633-x.supp2.pdf | grep -i "title\|reporting" | head -5; strings 10.1038-s41586-018-0633-x.supp1.pdf | grep -i "title" | head
```

```
666 10.1038-s41586-018-0633-x.txt
29:Preparatory activity was present in all three cerebellar nuclei ( Extended Data Fig 3 – 4 ). In the fastigial nucleus, distinct patterns of selectivity were observed during the early versus late delay epoch, where equal numbers of neurons preferred either contralateral or ipsilateral movement during the early delay, and a population-level preference for contralateral movement developed right before movement initiation ( Extended Data Fig 4g ) 23 , consistent with the directional biases induced by fastigial lesion and optogenetic manipulations during movement initiation ( Fig 1 ). These results show wide-spread activity related to motor planning and movement initiation in the CN.
109:Performance was computed as the fraction of correct choices, excluding lick early trials and no lick trials ( Fig 1g , Extended Data Figs 1e , 2g , 10b ). Chance performance was 50%. We also separately computed the performance for “lick right” and “lick left” trials ( Fig 1 ; Extended Data Figs 1 , 2 , 6 , 10 ). Significance of the performance change in each photostimulation condition was determined using bootstrap to account for variability across mice, sessions, and trials. We tested against the null hypothesis that the performance change caused by photostimulation was due to normal behavioral variability. In each round of bootstrap, we replaced the original behavioral dataset with a re-sampled dataset in which we re-sampled with replacement from: 1) mice, 2) sessions performed by each mice, 3) the trials within each session. We then computed the performance change on the re-sampled dataset. Repeating this procedure 10,000 times produced a distribution of performance changes that reflected the behavioral variability. The p-value of the observed performance change was computed as the fraction of times the bootstrap produced an inconsistent performance change (e.g. if a performance decrease was observed during photostimulation, the p-value was the fra
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git log --format="%h %ad %s" --date=short -S"pilot-15" -- docs/protocol.md | tail -3; git log --format="%h %ad %s" --date=short -- docs/protocol.md | head -5
```

```
e2d85aa 2026-11-14 Merge pull request #765 from catalystneuro/attempt/danish-2017
e2d85aa 2026-11-14 Merge pull request #765 from catalystneuro/attempt/danish-2017
```

**Agent calls Read**

```json
{
 "file_path": "paper/alm-4.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rn "not available\|available: false\|availability" docs/paper-first.md docs/protocol.md | head -20; grep -l "available" papers/datasets/*.yaml | head; grep -rln "^  datasets:" claims/ | head
```

```
docs/paper-first.md:36:  availability statement, find_reuse). A dataset the paper relies on that is in no open archive,
docs/paper-first.md:37:  or cannot be loaded, is listed with `available: false` and why.
docs/protocol.md:157:     rests on a dataset listed as not available.
claims/kim-2022.yaml
claims/pakhomov-2023.yaml
claims/silkuniene-2025.yaml
claims/wirth-2017.yaml
```

**Agent calls Bash**

```bash
cd  sed -n 20,60p docs/paper-first.md; for f in claims/kim-2022.yaml claims/wirth-2017.yaml; do echo "== $f"; head -40 $f; grep -n -B2 -A3 "datasets:" $f | head -40; done; cat papers/datasets/kim-2022.yaml papers/datasets/wirth-2017.yaml
```

```
- **Paper key**: first author's surname and year, `tingley-2021`, lower case ASCII. Where two
  papers would share one (3 today: guan-2022, daume-2024, moaddab-2021), the later-added one takes
  the first distinctive word of its title: `daume-2024-hippocampal`. Keys are assigned once and
  kept in `papers/keys.yaml` (DOI → key), never recomputed.
- **Attempt id**: `<paper key>-NN`, numbered across the paper (`semenov-2026-01`). The attempt
  names its datasets.

## One attempt, every dataset the paper relies on

- A paper's claims are extracted once, for the paper. Most papers rely on one dataset, and then
  claims name none: they rest on it. Only when the paper lists more than one does each claim
  carry `datasets:`, naming the ones it rests on. An attempt tests the paper against as many of those datasets as can be found and
  loaded: Semenov 2026's next attempt loads all 7 dandisets.
- The paper's datasets are listed in `papers/datasets/<paper key>.yaml`: each with archive, id,
  relation (primary or reuses) and how it was found (archive metadata, the paper's data
  availability statement, find_reuse). A dataset the paper relies on that is in no open archive,
  or cannot be loaded, is listed with `available: false` and why.
- **Missing datasets do not stop an attempt.** It runs on what is there; its record lists the
  rest under `missing_datasets`, and each claim that needs one is blocked with
  `blocked_by: dataset_missing`. The attempt is flagged on the site and in "waiting on you", so
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rl "000007" --include=*.yaml . | grep -v "^./claims/gao" | head; ls papers/ | head; grep -n "elsewhere\|not available\|data_missing\|no dataset" claims/wirth-2017.yaml claims/kim-2022.yaml | head
```

```
./attempts/gao-2018-01.yaml
./papers/manifest.yaml
./papers/match/000007.yaml
./papers/datasets/gao-2018.yaml
./targets/contributors.yaml
./entries/gao-2018/entry.yaml
authors.yaml
datasets
journals.yaml
keys.yaml
manifest.yaml
match
renamed.yaml
triage.yaml
claims/wirth-2017.yaml:800:    elsewhere, minus 1, a standard choice and a deviation. Reproduced when, under one reading, the
claims/wirth-2017.yaml:801:    excess is within tolerance and every landmark's area exceeds the mean elsewhere. The
claims/wirth-2017.yaml:814:    The method is not available from the text read; the author takes the claim as
claims/wirth-2017.yaml:828:  - gaze-map-landmarks. The excess measure (peak near a landmark over mean elsewhere, minus 1) is not the paper's; it is now marked as a standard choice and a deviation.
claims/kim-2022.yaml:25:#   measure; whether it holds them is the author's to find, and they are blocked as data_missing
```

**Agent calls Bash**

```bash
cd  cat papers/match/000007.yaml | head -40
```

```
# Whether each paper DANDI:000007 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '000007'
date: '2026-11-10'
papers:
- doi: 10.1038/s41586-018-0633-x
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
```

**Agent calls Bash**

```bash
cd  for f in claims/pakhomov-2023.yaml claims/silkuniene-2025.yaml claims/wirth-2017.yaml claims/kim-2022.yaml; do echo "== $f"; python - "$f" <<'EOF'
import yaml,sys
d=yaml.safe_load(open(sys.argv[1]))
for c in d['claims']:
    if 'datasets' not in c or not c['datasets']:
        print(c['id'], c.get('data'), c.get('datasets'))
EOF
done; grep -n "datasets\|unavailable\|not in any\|in neither\|none of" claims/silkuniene-2025.yaml | head -20
```

```
== claims/pakhomov-2023.yaml
== claims/silkuniene-2025.yaml
== claims/wirth-2017.yaml
== claims/kim-2022.yaml
23:# The datasets, from their titles and descriptions on DANDI (draft metadata, read 2026-11-10).
35:#   Those claims list all four datasets; the author checks each and blocks the claim as data_missing
130:  datasets:
164:  datasets:
186:  datasets:
205:  datasets:
220:  datasets:
248:  datasets:
266:  datasets:
281:  datasets:
296:  datasets:
311:  datasets:
361:  datasets:
396:  datasets:
410:  datasets:
425:  datasets:
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "datasets\|elsewhere\|data'" tools/claims_check.py | head -30; ls tools | head -50
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
entry.py
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "datasets" tools/datasets.py tools/entry.py | grep -i "claim" | head -20; grep -rn "def .*claim" tools/*.py | head
```

```
tools/entry.py:87:    paper's own claims file (claims/<paper>.yaml) and for an attempt on several datasets."""
tools/build_site.py:237:def paper_claims() -> dict[str, list[dict]]:
tools/build_site.py:1763:def claim_item(o: dict, root: str, attempt: dict | None = None, asked: dict | None = None) -> str:
tools/build_site.py:3758:def claims_only(data: dict) -> list[str]:
tools/build_site.py:3764:def claims_list(files: list[dict], titles: dict) -> tuple[str, int]:
tools/build_site.py:3792:def page_claims(data: dict, key: str) -> str:
tools/claims_check.py:78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
tools/entry.py:99:def claims_paths() -> list[Path]:
tools/entry.py:105:def claims_target(data: dict) -> tuple:
tools/paper_records.py:150:def claims_file(key: str) -> Path:
tools/paper_records.py:154:def claims_files(key: str) -> list[Path]:
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p claims/silkuniene-2025.yaml
```

```
# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), "MHz compression of pulse
# packets facilitates remote focusing of electroporation", Bioelectrochemistry 166, 109016, tested on
# dandisets 001047, 001276, 001277 and 001284.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md. It replaces the three files written 2026-10-22
# under pilot-10, one per dataset (claims/silkuniene-2025/001047.yaml, 001276.yaml, 001277.yaml);
# ids are kept where the finding is the same, taken from the file of the dataset that holds the
# figure (Figs. 3 to 5 from 001047, Fig. 6 from 001277, Fig. 7 from 001276).
#
# Text read. The accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), as served
# by ncbi_pmc, in paper/10.1016-j.bioelechem.2025.109016.txt: abstract, Introduction, Materials and
# methods 2.1 to 2.5, Results 3.1 to 3.4, Discussion, Conclusion and the legends of Figs. 1 to 7.
# It is not the version of record. The paper has no supplement (PMC marks "has-supplement no" and
# the text cites none). No PDF was supplied, so no figure was seen; values printed only in a figure
# (the packet rates other than 1 Hz, 1 kHz, 10 kHz and 0.2 MHz, the ROI positions, the zones of Fig.
# 5C, axis values) are not used.
#
# Code. The paper links no code and no data deposit ("Data will be made available on request").
# It names the software only: MetaMorph 7.8.13 for intensities, RStudio, Excel and Grapher 16 for
# processing, fits and graphs, Sim4Life Lite 7.0.1.8169 for the field. No repository was read, so no
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^checks:" -A6 claims/kim-2022.yaml claims/silkuniene-2025.yaml claims/wirth-2017.yaml | head -40; grep -n "checks" docs/protocol.md docs/pipeline.md | head
```

```
claims/kim-2022.yaml:613:checks:
claims/kim-2022.yaml-614-- date: 2026-11-10
claims/kim-2022.yaml-615-  kind: agent
claims/kim-2022.yaml-616-  model: claude-opus-5-5
claims/kim-2022.yaml-617-  ready: true
claims/kim-2022.yaml-618-  changes:
claims/kim-2022.yaml-619-  - fig7-charging-time-constant. The quote stopped at "520 ns" and left out the discharge fit's 425 datapoints, r = 0.85 and p < 0.0001, which the statement and statistics record. Extended the quote to include them (Results 3.5, paragraph 2).
--
claims/silkuniene-2025.yaml:768:checks:
claims/silkuniene-2025.yaml-769-- date: 2026-11-10
claims/silkuniene-2025.yaml-770-  kind: agent
claims/silkuniene-2025.yaml-771-  model: claude-opus-5-5
claims/silkuniene-2025.yaml-772-  ready: true
claims/silkuniene-2025.yaml-773-  changes:
claims/silkuniene-2025.yaml-774-  - Header F6 and O3, fig4c-fwhm-falls-with-rate. F6 fixed the range of the per-experiment fits of Fig. 4C at -4 to 4 mm, citing Results 3.1 and the Fig. 3B legend; both give that range for the fits to the mean profiles of Fig. 3, and Methods 2.5 allows 4 to 6 mm. The Fig. 4C range is now open in O3, readings 4, 5 and 6 mm, with 4 mm the one Results 3.1 supports; the criterion cites O3. fig4c-log-trend takes its FWHM from that claim.
--
claims/wirth-2017.yaml:816:checks:
claims/wirth-2017.yaml-817-- date: 2026-11-10
claims/wirth-2017.yaml-818-  kind: agent
claims/wirth-2017.yaml-819-  model: claude-opus-5-5
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python - <<'EOF'
import re,zlib
data=open('10.1038-s41586-018-0633-x.supp2.pdf','rb').read()
out=[]
for m in re.finditer(rb'stream\r?\n(.*?)\r?\nendstream',data,re.S):
    try: s=zlib.decompress(m.group(1))
    except Exception: continue
    t=b''.join(re.findall(rb'\((.*?)(?<!\\)\)',s))
    if t: out.append(t.decode('latin1'))
txt=' '.join(out)
for k in ['CRCNS','deposit','code','Code']:
    for mm in re.finditer(k,txt):
        print(txt[max(0,mm.start()-200):mm.start()+200].replace('\n',' ')); print('---')
EOF
```

```
ble on the Matlab FileExchange \(https://www.mathworks.com/matlabcentral/fileexchange/20057-b-spline-grid--image-and-point-based-registration\).  Custom analysis scripts and data will be deposited on CRCNS.org.  Analysis scripts and data will also be available from the corresponding author upon reasonable request.For manuscripts utilizing custom algorithms or software that are central to the resea
---
ackage available on the Matlab FileExchange \(https://www.mathworks.com/matlabcentral/fileexchange/20057-b-spline-grid--image-and-point-based-registration\).  Custom analysis scripts and data will be deposited on CRCNS.org.  Analysis scripts and data will also be available from the corresponding author upon reasonable request.For manuscripts utilizing custom algorithms or software that are central
---
om algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors/reviewers upon request. We strongly encourage code deposition in a community repository \(e.g. GitHub\). See the Nature Research guidelines for submitting code & software for further information. c
(?(q(¢(Ôî´ï@ïÌðXðåñrñÿòóó§ô4ôÂõPõÞömöû÷øø¨ù8ùÇúWú
---
n of the appropriate level for tests and full reporting of outcomes Estimates of effect sizes \(e.g. Cohen's , Pearson's \), indicating how they were calculatedClearly defined error bars Software and code Policy information about availability of computer codeData collectionBehavioral data were acquired using commercial hardware \(Bpod, Sanworks\) and software \(https://github.com/sanworks/Bpod_Gen
---
 of outcomes Estimates of effect sizes \(e.g. Cohen's , Pearson's \), indicating how they were calculatedClearly defined error bars Software and code Policy information about availability of computer codeData collectionBehavioral data were acquired using commercial hardware \(Bpod, Sanworks\) and software \(https://github.com/sanworks/Bpod_Gen2\).   Electrophysiology data were 
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; awk 'NR>=8 && NR<=43 && length($0)>0 {n++; print n": L"NR": "substr($0,1,70)}' 10.1038-s41586-018-0633-x.txt
```

```
1: L9: Persistent and ramping neural activity in frontal cortex anticipates s
2: L11: Head-fixed mice discriminated object locations (anterior or posterior)
3: L13: During the delay epoch, preparatory activity in anterior lateral motor
4: L15: ALM projects to the cerebellum via the basal pontine nucleus 23 , 24 .
5: L17: We tested fastigial involvement during specific behavioral epochs by d
6: L19: Fastigial photo-activation did not block or perturb the frequency and 
7: L21: We tested for necessity by silencing fastigial activity. We photostimu
8: L23: Thus, fastigial activity, starting from the late sample epoch and thro
9: L25: We compared the activity in ALM and CN by recording from single-units 
10: L27: Selectivity for “lick left” and “lick right” trials emerged gradually 
11: L29: Preparatory activity was present in all three cerebellar nuclei ( Exte
12: L31: The cerebellum is thought to process information over timescales of hu
13: L33: Photo-inhibiting either side of ALM reduced CN preparatory activity ( 
14: L35: We tested whether ALM preparatory activity depends on CN activity by r
15: L37: Preparatory activity requires reciprocal excitation between ALM and th
16: L39: We probed the influence of CN on ALM thalamo-cortical loop during moto
17: L41: We disambiguated the effect of fastigial and dentate photo-activations
18: L43: Our results show that the cerebellum is critical for the coding of fut
```

**Agent calls Bash**

```bash
cd paper; grep -o "Performance in control.\{0,250\}" 10.1038-s41586-018-0633-x.txt | head -1 | od -c | grep -n "342" | head -3
```

```
5:0000100   .     342 200 234   L   i   c   k       l   e   f   t 342 200
6:0000120 235       a   n   d     342 200 234   l   i   c   k       r   i
7:0000140   g   h   t 342 200 235       t   r   i   a   l   s       a   r
```

**Agent calls Write**

```json
{
 "file_path": "claims/gao-2018.yaml",
 "content": "# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), \"A\n# cortico-cerebellar loop for motor planning\", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,\n# tested on DANDI:000007 and CRCNS:alm-4.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-14,\n# protocol pilot-15 as stated in docs/protocol.md. It updates the file written 2026-11-10 under\n# pilot-14 (and checked that day) for DANDI:000007 alone; ids are kept where the finding is the\n# same, and the changes of that check are carried over.\n#\n# Text read: the version of record (PMC6212318, open access), Europe PMC JATS XML flattened, in\n# paper/10.1038-s41586-018-0633-x.txt: main text, Methods, the legends of Extended Data Figs. 1 to\n# 10, and the Supplementary Information (41586_2018_633_MOESM1_ESM.pdf, from the publisher; also\n# paper/...supp1.pdf), whose text is appended: the Extended Data Fig. 10 discussion, the cerebellar\n# circuitry discussion and Supplemental Table 1 (mice and hemispheres per experiment). supp2.pdf is\n# the Nature reporting summary. The legends of the main Figs. 1 to 4 are not in the stored text,\n# and there is no PDF of the main paper; values, significance marks and neuron counts given only in\n# those legends or inside the figures are not used here (see the report of this run). Sources cite\n# main-text paragraphs counting the opening summary paragraph as paragraph 1.\n# Code: the paper links none. Its Code availability says \"Software used for data analysis is\n# available from the corresponding author upon reasonable request\"; the reporting summary says\n# \"Custom analysis scripts and data will be deposited on CRCNS.org\" and gives no identifier. The\n# CRCNS:alm-4 descriptor names two demo files of the dataset (Demo_get_performance,\n# Demo_get_trial_aligned_raster_PSTH); they are not the paper's analysis code and were not read.\n# So every method detail below is from the Methods, the Extended Data legends or the supplement,\n# or is named as open.\n#\n# The datasets, from their titles and descriptions on the archives.\n#  - 000007 (DANDI), titled as the paper; description \"Extracellular recording in ALM\".\n#  - crcns-alm-4 (CRCNS), \"Extracellular recordings from anterior lateral motor cortex (ALM) and\n#    cerebellar nucleus neurons of adult mice performing a tactile decision behavior\". Its\n#    descriptor lists 34 sessions (9 mice) of ALM recording during fastigial or dentate\n#    photo-activation and 20 sessions (4 mice) of ALM recording during CN photo-inhibition, with\n#    photostimulation codes for fastigial or dentate photo-activation in the sample or delay (500\n#    ms) and CN photo-inhibition in the delay (500 ms or 1.3 s). It lists no CN recordings.\n#  Both are described as the ALM recordings of Figs. 2 to 4 and Extended Data Figs. 4, 5e, 9 and\n#  10, and every claim on those lists both. Supplemental Table 1 shows that the 6 mice of the 0.5 s\n#  fastigial photo-activation behavior (Fig. 1g, h) are the 6 mice of ALM recording during fastigial\n#  photo-activation, and that the 4 mice of ALM recording during CN photo-inhibition are among the 7\n#  mice of 0.5 s CN photo-inhibition (Fig. 1k), so their recording sessions may hold part of those\n#  behavioral data (photostimulation was on 33% of trials during recordings and 25% in behavior\n#  sessions, Methods). No description names the lesion experiments, the 1.3 s photostimulation\n#  experiments, the CN recordings, the photo-inhibition characterization, the movement tests, the\n#  VGAT-ChR2-EYFP behavior or the anatomy. Those claims list both datasets, as the paper's only\n#  deposits; the author checks each and blocks the claim as data_missing when neither holds the\n#  data. They are kept because they are the paper's findings.\n#\n# Data the paper used, as it reports them (Methods; Supplemental Table 1):\n#  - Task. Head-fixed mice report the location of a pole (anterior or posterior) by licking left or\n#    right. Sample epoch 1.3 s (pole movement onset to 0.1 s after retraction onset), delay epoch\n#    1.3 s, auditory go cue (3.4 kHz, 0.1 s), then the response. Lick early trials (alarm, timeout)\n#    and no-lick trials (no lick within 1.5 s of the go cue) are excluded from performance.\n#    Reaction time is from go cue onset to the first lickport contact.\n#  - Mice. 70 in all (Supplemental Table 1). ALM recordings: 1309 single units in 10 mice over 39\n#    sessions during behavior with CN ChR2 photo-activation (Fig. 2, Fig. 4); 1194 putative\n#    pyramidal (trough-to-peak spike width > 0.45 ms), 82 fast-spiking (< 0.35 ms), 33\n#    intermediate excluded. 9 of these 10 mice received CN photo-activation during the recordings\n#    (912 putative pyramidal neurons); one mouse was excluded because the virus missed the CN. The\n#    split of the 912 between fastigial and dentate sessions is not in the text read. Supplemental\n#    Table 1 lists 6 mice for fastigial (CD06, NL15, AN105, AN107, AN108, AN109) and 3 for dentate\n#    (NL12, NL14, AN106) photo-activation during ALM recording. ALM recordings during CN\n#    photo-inhibition in L7-cre x Ai32 mice: 490 units in 4 mice (CD08, CD12, CD13, CD14) over 19\n#    sessions, 454 pyramidal. The Methods say recordings were from left ALM in 10 mice and right\n#    ALM in 2; the table lists 13 ALM-recorded mice, 2 of them in right ALM (AN107, CD14). ALM was\n#    always recorded contralateral to the manipulated CN.\n#  - CN recordings: 878 units in 18 mice over 169 sessions (10 wild-type, 8 VGAT-ChR2-EYFP with\n#    ALM photo-inhibition); 268 fastigial, 139 interposed, 157 dentate, 314 outside the CN.\n#  - Photostimuli. CN photo-activation (AAV ChR2): 5 ms pulses at 20 Hz, average 0.5, 1 or 1.5 mW,\n#    from the start of an epoch for 0.455 s (10 pulses) or 1.255 s (26 pulses), on 25% of\n#    behavioral trials and 33% during ALM recordings. CN photo-inhibition (Purkinje cell ChR2): 40\n#    Hz sinusoid, 0.5, 1.5 or 4.5 mW, 0.5 or 1.3 s with a 100 to 200 ms offset ramp; during ALM\n#    recordings it starts at delay onset and lasts 1.3 s (1.5 or 4.5 mW). ALM photo-inhibition\n#    (VGAT-ChR2): bilateral, 1.3 s from delay onset, 1.5 mW per site; unilateral, a 40 Hz\n#    sinusoid at 1.5 mW (Extended Data Figs. 6, 10).\n#  - Measured variables. Spike times of sorted units, trial events (pole, go cue, licks),\n#    instructed trial type, lick direction and outcome, photostimulation condition.\n#\n# Shared methods, cited by the criteria below.\n#  B1 Behavioral performance (Methods, Behavioral data analysis). Fraction of correct choices,\n#     excluding lick early and no lick trials; also computed separately for \"lick left\" and\n#     \"lick right\" trials, grouped by instructed direction relative to the manipulated hemisphere\n#     (Extended Data Fig. 1e legend). Significance by a hierarchical bootstrap, resampling with\n#     replacement mice, then sessions of each mouse, then trials of each session, 10,000 times; the\n#     one-tailed p-value is the fraction of resamples whose performance change has the sign\n#     opposite to the observed one. Where the paper gives no threshold for a behavioral effect,\n#     p < 0.05 is used, the lowest significance mark of its bootstrap legends (Extended Data Figs.\n#     1e, 2g), and named as a choice.\n#  E1 Units (Methods, Electrophysiology data analysis). ALM analyses use putative pyramidal\n#     neurons (spike width > 0.45 ms); CN units are not classified by spike shape.\n#  E2 Trial-type selectivity. A two-tailed t-test (p < 0.05) on spike counts of \"lick left\"\n#     against \"lick right\" trials in the sample, delay or response epoch; selective when any\n#     epoch is significant. The response epoch's window is not given (open; readings (a) 1.3 s\n#     from go cue onset, the length of the other epochs and of the response epoch photostimulus;\n#     (b) 0 to 1.5 s after the go cue, the answer window). Which trials form \"lick left\" and\n#     \"lick right\" here is not stated (open; readings (a) correct trials, as in the PSTHs of\n#     Extended Data Fig. 4b; (b) all trials with a lick, grouped by instructed direction).\n#  E3 Population selectivity (Methods; Extended Data Fig. 4f legend). Each neuron's preferred\n#     trial type is fixed from a subset of trials (10 for ALM, 20 for CN) and selectivity is the\n#     spike rate difference between preferred and non-preferred trial types on the remaining\n#     trials, averaged over neurons with mean and s.e.m. by bootstrap over neurons. The averaging\n#     window is not in the text read (a standard choice, 200 ms, used). Whether the subset is 10\n#     trials in all or per trial type, and which epoch fixes the preference, are open; the paper\n#     says the epoch choice gave qualitatively similar results. For photostimulation effects, all\n#     trials (correct and incorrect) grouped by instructed type are used, and only selective\n#     neurons tested on > 3 trials in all conditions (Extended Data Figs. 5b, 6c, 9c legends).\n#  E4 Photostimulation effect on a neuron (Methods). \"Lick left\" and \"lick right\" trials pooled;\n#     two-tailed t-test on spike counts, control against photostimulation trials, at p < 0.01\n#     (Extended Data Figs. 2d, 5b, 9a legends), in the whole delay epoch (Fig. 3, Extended Data\n#     Fig. 5) or in 400 ms bins in 50 ms steps (Fig. 4f). Whether correct trials only or all trials\n#     enter is not stated (open; readings all trials and correct trials only).\n#  E5 Latency (Extended Data Fig. 9a legend). Among significantly modulated neurons, firing rate\n#     change (photostimulation minus control) with the sign flipped for suppressed neurons, in 10\n#     ms bins in 1 ms steps; onset is the first bin where the population change differs from 0 by\n#     a two-tailed t-test at p < 0.01; neurons resampled with replacement 10,000 times and the\n#     mean onset reported. The window that decides \"significantly modulated\" for this analysis is\n#     not given (open; readings (a) the photostimulation period, (b) the whole delay epoch). The\n#     paper describes this method only for CN photo-activation (Extended Data Fig. 9a); its use\n#     for the latencies of Fig. 3 (ALM and CN photo-inhibition) is assumed, as it gives no other.\n#  E6 Coding direction (Methods, Analysis of ALM population dynamics). Sessions with > 5\n#     simultaneously recorded neurons and > 5 trials per condition (28 of 39). Spike counts in\n#     400 ms windows in 10 ms steps; cd_t is the mean \"lick right\" minus mean \"lick left\" response\n#     vector, averaged over the delay epoch to one cd, from correct control trials only. Projections\n#     cd'x use control and photostimulation trials independent of those that estimated the cd,\n#     correct and incorrect, grouped by instructed type; each session is offset by its mean\n#     projection over all trials and times (from the cd-estimating trials); s.e.m. by bootstrap\n#     over sessions. How trials are split into the cd-estimating and the independent sets is not\n#     given; a random half split of control trials is used, a standard choice.\nschema_version: 2\npaper: doi:10.1038/s41586-018-0633-x\nclaims:\n- id: fig1d-fastigial-lesion-contra-choice\n  statement: Fastigial nucleus lesions impair contralesional licking choices, measured as lower\n    performance on trials instructing contralesional licking after the lesion than before.\n  source: Main text, paragraph 4; Figure 1d\n  quote: Fastigial lesions impaired initiation of contralesional licking ( Fig 1d )\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Performance as in B1 for contralesional and ipsilesional trials, before against\n    after the lesion, in the 4 fastigial lesion mice (Supplemental Table 1). The main text gives\n    no test and the Fig. 1 legend is not in the text read, so the one-sided bootstrap of B1 at p <\n    0.05 is used (B1). Whether mice are pooled or tested one by one is open (readings (a) the\n    hierarchical bootstrap of B1 over the 4 mice; (b) per mouse, the bootstrap over that mouse's\n    sessions and trials). Reproduced when, under one reading, contralesional performance drops\n    after the lesion at p < 0.05 (in every fastigial mouse, under reading (b)). The per-mouse\n    drops are reported under both readings.\n- id: fig1e-fastigial-lesion-slow-initiation\n  statement: After fastigial lesion, the first lick to the contralesional side comes later after\n    the go cue than the first lick to the ipsilesional side, while lick rate within bouts and\n    bout duration are unchanged.\n  source: Main text, paragraph 4; Figure 1e; Extended Data Figure 1b and 1c\n  quote: slowed initiation of contralesional licking following the 'go' cue ( Fig 1e ). After\n    movement initiation licking was unaffected\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Time of the first lick after go cue onset (Methods, reaction time), per trial,\n    contralesional against ipsilesional licking, in the fastigial lesion mice after the lesion;\n    one-sided hierarchical bootstrap as in B1 at p < 0.05 (the Fig. 1e legend, not in the text\n    read, would give the paper's test). Reproduced when contralesional first licks are later. For\n    the second part, a lick bout is a sequence of licks with inter-lick intervals under 500 ms\n    (Extended Data Fig. 1c legend), in the fastigial lesion mice. The legend says lick rate and\n    bout duration are \"not affected by fastigial lesion\" with data grouped by contra- and\n    ipsilesional licking, so the comparison is open (readings (a) before against after the\n    lesion, for each direction; (b) contra- against ipsilesional bouts after the lesion). The\n    paper reports no test for this absence; the bootstrap of B1, two-sided at p < 0.05, is used\n    and named as a choice, and the second part holds when under one reading neither measure\n    differs.\n- id: fig1d-dentate-lesion-no-effect\n  statement: Dentate nucleus lesions do not change behavioral choice or movement execution.\n  source: Main text, paragraph 4; Figure 1d\n  quote: Dentate lesions (~1.5 mm away) did not change behavioral choice and movement execution\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence. Performance as in B1 for contralesional and ipsilesional trials,\n    pre against post lesion, in the 4 dentate lesion mice, tested with the one-sided bootstrap of\n    B1, pooled and per mouse as the readings of fig1d-fastigial-lesion-contra-choice, at p <\n    0.05, the threshold of the paper's other absence statements (\"p>0.05 for either trial type\").\n    Reproduced when neither trial type changes at p < 0.05; the size of each change is reported.\n    For movement execution the paper shows no dentate data in the text read (Extended Data Fig.\n    1c is fastigial mice only); lick rate within bouts and bout duration, pre against post\n    lesion, are tested as in the second part of fig1e-fastigial-lesion-slow-initiation and\n    reported, the outcome noting that this part rests on a test the paper does not show.\n- id: fig1g-fastigial-activation-early-sample-no-effect\n  statement: Fastigial photo-activation during the early sample epoch does not affect behavioral\n    choice for either trial type.\n  source: Main text, paragraph 5\n  quote: Fastigial photo-activation during the early sample epoch had no effect on behavioral\n    choice (p>0.05 for either trial type, bootstrap, Methods)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n    n: 6 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence, judged on the paper's test. Performance per trial type (B1) in\n    control against early sample photo-activation trials (0.455 s from sample onset) in the 6\n    mice of \"Fastigial 0.5s photo-activation\" (Supplemental Table 1), one-sided bootstrap of B1;\n    reproduced when p > 0.05 for both trial types.\n- id: fig1g-fastigial-activation-delay-errors\n  statement: Fastigial photo-activation during the early delay epoch lowers behavioral\n    performance, even though the photostimulus ends 800 ms before the movement.\n  source: Main text, paragraph 5; Figure 1g\n  quote: Photo-activation during the delay and response epochs both resulted in incorrect choices\n    ( Fig 1g–h ). Incorrect choices were induced even when the photostimuli ceased 800 ms before\n    the movement\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Performance with \"lick left\" and \"lick right\" trials pooled (B1), control against\n    early delay photo-activation (0.455 s from delay onset) in the 6 mice of \"Fastigial 0.5s\n    photo-activation\" (Supplemental Table 1). The Fig. 1g legend, which would give the paper's\n    mark, is not in the text read. Reproduced when performance drops with a one-sided bootstrap p\n    < 0.05 (B1).\n- id: fig1h-fastigial-activation-delay-bias\n  statement: Fastigial photo-activation during the delay epoch biases future movements toward\n    either the contralateral or the ipsilateral direction, depending on the mouse.\n  source: Main text, paragraph 5; Figure 1h; Extended Data Figure 1e\n  quote: Photo-activation during the delay epoch biased future movements to either the\n    contralateral or ipsilateral direction in individual mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Per mouse, the change in performance with delay photo-activation for contralateral\n    and ipsilateral trials (B1). Fig. 1h holds both the 0.455 s early delay experiment and the\n    1.255 s whole delay experiment (Supplemental Table 1 lists Fig. 1h under both), so the\n    photostimulus is open (readings (a) early delay, 0.455 s; (b) whole delay, 1.255 s, as in\n    Extended Data Fig. 1e). The paper shows individual mice and gives no per-mouse test; the\n    per-mouse one-sided bootstrap of B1 (trials and sessions of that mouse) at p < 0.05 is named\n    here as a choice. Reproduced when under one reading at least one mouse shows a significant\n    drop on contralateral trials larger than its ipsilateral drop and at least one a significant\n    drop on ipsilateral trials larger than its contralateral drop.\n- id: fig1h-fastigial-activation-response-contra-bias\n  statement: Fastigial photo-activation during the response epoch produces a contralateral bias,\n    opposite to the bias of fastigial lesions.\n  source: Main text, paragraph 5; Figure 1h; Extended Data Figure 1e\n  quote: Photo-activation immediately before movement onset (response epoch) produced a\n    contralateral bias ( Fig 1h ), opposite from the directional bias induced by fastigial\n    lesions\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Response epoch photo-activation (1.255 s from go cue onset) in the 6 mice of\n    \"Fastigial 1.3s photo-activation\" (Supplemental Table 1). A contralateral bias is lower\n    performance on ipsilateral trials (more contralateral licks) with contralateral performance\n    not lowered. Reproduced when the ipsilateral performance drops with a one-sided bootstrap p <\n    0.05 (B1) and the contralateral drop, if any, is smaller and not significant.\n- id: fig1i-fastigial-activation-licking-unaffected\n  statement: Fastigial photo-activation does not block or change the frequency and duration of\n    licking after a lick bout starts, and photo-activation in the delay does not evoke early\n    licks.\n  source: Main text, paragraph 6; Figure 1i; Extended Data Figure 1f\n  quote: Fastigial photo-activation did not block or perturb the frequency and duration of licking\n    movements after initiation of licking bouts ( Fig 1i ). Fastigial photo-activation during the\n    delay epoch did not evoke early licks\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence; the paper reports no test. Lick rate within bouts and bout\n    duration (bouts as in Extended Data Fig. 1c, inter-lick interval < 500 ms) in control against\n    response epoch photo-activation trials, and the early lick rate in control against delay\n    photo-activation trials, per mouse (n = 6, Extended Data Fig. 1f). The bootstrap of B1,\n    two-sided at p < 0.05, is used and named as a choice; reproduced when none of the three\n    differs. Sizes are reported.\n- id: fig1g-dentate-activation-little-effect\n  statement: Dentate photo-activation produces little effect on behavioral choice.\n  source: Main text, paragraph 6; Figure 1g; Extended Data Figure 1e\n  quote: Dentate photo-activation produced little effect on behavioral choice ( Fig 1g , p=0.06,\n    bootstrap\n  statistics:\n  - test: bootstrap\n    p: 0.06\n    n: 8 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Pooled performance (B1), control against delay dentate photo-activation, in the 8\n    dentate mice. Which photostimulus is open, as the Methods put Fig. 1g under the 0.455 s\n    sub-epoch experiments, while Supplemental Table 1 lists the 8 dentate mice only under \"Dentate\n    1.3s photo-activation\" for Fig. 1g (readings (a) early delay, 0.455 s; (b) whole delay, 1.255\n    s). A claim of absence judged on the paper's test, the one-sided bootstrap of B1 at p < 0.05;\n    reproduced when it does not find a drop. The p-value (paper 0.06) and the size of the change\n    are reported.\n- id: fig1j-photoinhibition-silences-fastigial\n  statement: Photostimulating Purkinje cells in L7-cre x Ai32 mice silences fastigial nucleus\n    neurons, while photostimulation over the inferior colliculus does not.\n  source: Methods, CN photo-inhibition, paragraph 1; Figure 1j; Extended Data Figure 2c and 2d\n  quote: Photostimulation of the cerebellar cortex silenced fastigial activity whereas\n    photostimulation of the inferior colliculus did not\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Fastigial units (n = 26, 2 mice, non-behaving), spike rate in the 500 ms before\n    against the 1.2 s during photo-inhibition, each unit tested by the two-tailed t-test at p <\n    0.01 of the Extended Data Fig. 2d legend. The paper gives no count or population test.\n    Reproduced when, under cerebellar cortex photostimulation, more than half of the fastigial\n    units decrease significantly and, under inferior colliculus photostimulation, fewer than half\n    do and the mean rate over units does not drop (two-tailed paired t-test over units at p <\n    0.01, named here as a choice). The fractions are reported.\n- id: fig1k-inhibition-early-sample-no-effect\n  statement: Fastigial photo-inhibition during the early sample epoch does not affect behavioral\n    choice.\n  source: Main text, paragraph 7; Figure 1k\n  quote: Photo-inhibition during the early sample epoch did not affect behavioral choice ( Fig 1k ,\n    p>0.05 for either trial type, bootstrap, Methods)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence, judged on the paper's test. Performance per trial type (B1),\n    control against 0.5 s early sample photo-inhibition, 7 mice; reproduced when the one-sided\n    bootstrap of B1 gives p > 0.05 for both trial types.\n- id: fig1k-inhibition-late-sample-delay-errors\n  statement: Fastigial photo-inhibition during the late sample and the delay epochs causes\n    incorrect choices, with a larger effect in the delay epoch.\n  source: Main text, paragraph 7; Figure 1k; Extended Data Figure 2g and 2h\n  quote: Photo-inhibition during the late sample and delay epochs resulted in incorrect behavioral\n    choices, with a larger effect induced in the delay epoch\n  statistics:\n  - about: sub-epoch photo-inhibition, the weaker effect marked\n    test: one-sided bootstrap\n    p: 0.04\n    n: 7 mice\n  - about: sub-epoch photo-inhibition, the stronger effect marked\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 7 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Performance (B1) in control against 0.5 s photo-inhibition in the early sample, late\n    sample, early delay and late delay sub-epochs (Extended Data Fig. 2h, 7 mice). Reproduced\n    when late sample and at least one delay sub-epoch lower performance with one-sided bootstrap\n    p < 0.05, and the larger of the delay drops exceeds the late sample drop. The legend gives\n    p = 0.04 and p = 0.0002 without naming which bar carries which; both are reported.\n- id: fig1k-inhibition-delay-bias\n  statement: Fastigial photo-inhibition during the delay epoch biases future movements to the\n    contralateral or the ipsilateral direction, depending on the mouse.\n  source: Main text, paragraph 7; Extended Data Figure 2g and 2h\n  quote: Photo-inhibition during the delay epoch biased future movements to either the\n    contralateral or ipsilateral direction in individual mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: As fig1h-fastigial-activation-delay-bias (per-mouse test named there as a choice),\n    on delay photo-inhibition trials. The photostimulus is open (readings (a) the 0.5 s early or\n    late delay photo-inhibition of the 7 mice, Extended Data Fig. 2h; (b) the 1.3 s whole delay\n    photo-inhibition of the 3 mice CD12, CD13, CD16, Extended Data Fig. 2g).\n- id: fig1k-inhibition-response-ipsi-bias\n  statement: Fastigial photo-inhibition during the response epoch produces an ipsilateral bias,\n    as fastigial lesions do and opposite to photo-activation.\n  source: Main text, paragraph 7; Figure 1k; Extended Data Figure 2g\n  quote: Photo-inhibition during movement initiation (response epoch) produced an ipsilateral\n    bias ( Fig 1k ), consistent with fastigial lesions, and opposite from the bias induced by\n    fastigial photo-activation\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Response epoch photo-inhibition (1.3 s from go cue onset) in the 3 mice of the 1.3 s\n    experiment (Supplemental Table 1). An ipsilateral bias is lower performance on contralateral\n    trials with ipsilateral performance not lowered. Reproduced when the contralateral drop has a\n    one-sided bootstrap p < 0.05 (B1) and the ipsilateral drop, if any, is smaller and not\n    significant.\n- id: fig1l-inhibition-execution-unaffected\n  statement: Fastigial photo-inhibition minimally affects movement execution, and at the\n    intensities of the task evokes no consistent movement.\n  source: Main text, paragraph 7; Figure 1l; Extended Data Figure 2e, 2f and 2i; Methods, CN\n    photo-inhibition and effects on movement\n  quote: Photo-inhibition minimally affected movement execution ( Fig 1l ). No other movements\n    were consistently evoked during photo-inhibition\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence; the paper reports no test. Lick rate within bouts in control\n    against response epoch photo-inhibition trials (3 mice), and early lick rate in control\n    against delay photo-inhibition trials (7 mice, Extended Data Fig. 2i), with the bootstrap of\n    B1, two-sided at p < 0.05, named as a choice. The video scoring and jaw tracking of Extended\n    Data Fig. 2e and 2f come from 6 other mice not in Supplemental Table 1 and are reported as not\n    tested when the datasets lack them.\n- id: ed10-vgat-fastigial-perturbation-performance\n  statement: In VGAT-ChR2-EYFP mice, fastigial photostimulation in the early delay reduces\n    performance on both trial types (contra lick 74.5% to 58.5%, ipsi lick 67.8% to 57.0%).\n  source: Methods, ALM photo-inhibition after a fastigial perturbation, paragraph 1\n  quote: fastigial perturbations during the early delay epoch reduced behavioral performance for\n    both trial types (control ... 74.5% correct, \"ipsi lick\" trials, 67.8%; photostimulation ...\n    58.5% and 57.0%; p<0.05 for both trial types, bootstrap)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 VGAT-ChR2-EYFP mice\n  expected:\n  - quantity: control performance, contra lick trials\n    value: 74.5\n    tolerance: 7.45\n    unit: \"%\"\n  - quantity: control performance, ipsi lick trials\n    value: 67.8\n    tolerance: 6.78\n    unit: \"%\"\n  - quantity: fastigial perturbation performance, contra lick trials\n    value: 58.5\n    tolerance: 5.85\n    unit: \"%\"\n  - quantity: fastigial perturbation performance, ipsi lick trials\n    value: 57.0\n    tolerance: 5.7\n    unit: \"%\"\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Performance per trial type (B1) on fastigial-only trials (40 Hz, 1.5 mW, 500 ms from\n    delay onset) against control trials. Whether the percentages are pooled over trials or\n    averaged over mice is not stated (open; readings (a) pooled over all trials, (b) mean of\n    per-mouse values). Reproduced when under one reading all four values are within tolerance\n    and both drops have one-sided bootstrap p < 0.05.\n- id: fig2-alm-selective-fraction\n  statement: Most ALM putative pyramidal neurons (980 of 1194) distinguish \"lick left\" from\n    \"lick right\" trials in their spike counts.\n  source: Main text, paragraph 9; Methods, Electrophysiology data analysis\n  quote: Most ALM pyramidal neurons distinguished \"lick left\" and \"lick right\" trials in spike\n    counts (980/1194, p<0.05, two-tailed t-test, Methods)\n  expected:\n  - quantity: ALM putative pyramidal neurons\n    value: 1194\n    tolerance: 119.4\n  - quantity: selective ALM pyramidal neurons\n    value: 980\n    tolerance: 98\n  - quantity: fraction selective\n    value: 0.82\n    tolerance: 0.082\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Units as E1, selectivity test as E2. The counts rest on the 39 sessions of 10 mice;\n    if the dataset holds fewer (the CRCNS descriptor lists 34 sessions of 9 mice), the fraction\n    is judged and the counts are reported. Reproduced when, under one of the readings of E2\n    (response window (a) or (b), trials (a) or (b)), the fraction is within tolerance; where the\n    dataset holds all units, the counts must be as well.\n- id: fig2-cn-selective-fraction\n  statement: A proportion of CN neurons similar to ALM (416 of 564) shows trial-type selectivity.\n  source: Main text, paragraph 9\n  quote: A similar proportion of CN neurons showed trial-type selectivity (416/564)\n  expected:\n  - quantity: CN neurons\n    value: 564\n    tolerance: 56.4\n  - quantity: selective CN neurons\n    value: 416\n    tolerance: 41.6\n  - quantity: fraction selective\n    value: 0.74\n    tolerance: 0.074\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: CN units are those located in the fastigial, interposed or dentate nucleus (268 +\n    139 + 157 = 564; Methods). Selectivity as E2. Reproduced when under one reading of E2 the\n    fraction is within tolerance.\n- id: fig2-preparatory-more-in-alm\n  statement: Preparatory activity (selectivity before the response epoch) is more prevalent in ALM\n    (59% of neurons) than in the CN (35%).\n  source: Main text, paragraph 9\n  quote: Preparatory activity (selectivity before the response epoch) was more prevalent in ALM\n    (ALM, 59% of neurons, CN, 35%; p<0.001, chi-square test)\n  statistics:\n  - test: chi-square test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1194 ALM and 564 CN neurons\n  expected:\n  - quantity: fraction of ALM neurons with preparatory activity\n    value: 0.59\n    tolerance: 0.059\n  - quantity: fraction of CN neurons with preparatory activity\n    value: 0.35\n    tolerance: 0.035\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A neuron has preparatory activity when the E2 test is significant in the sample or\n    the delay epoch. The denominator is open (readings (a) all neurons, 1194 and 564; (b) the\n    selective neurons, 980 and 416). Trials as the readings of E2. Reproduced when under one\n    reading both fractions are within tolerance and a chi-square test of the two proportions has\n    p < 0.001 with ALM higher. The ALM fraction alone is tested where the CN neurons are missing.\n- id: fig2-peri-movement-equal\n  statement: Peri-movement activity (selectivity in the response epoch) is equally prevalent in\n    ALM (67%) and the CN (66%).\n  source: Main text, paragraph 9\n  quote: Peri-movement activity (selectivity during response epoch) was equally prevalent in both\n    regions (ALM, 67%, CN, 66%)\n  expected:\n  - quantity: fraction of ALM neurons with peri-movement selectivity\n    value: 0.67\n    tolerance: 0.067\n  - quantity: fraction of CN neurons with peri-movement selectivity\n    value: 0.66\n    tolerance: 0.066\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A neuron has peri-movement activity when the E2 test is significant in the response\n    epoch, under the response window readings of E2. Denominator as in\n    fig2-preparatory-more-in-alm (open, same readings). Reproduced when under one reading both\n    fractions are within tolerance; a chi-square test of the two proportions is reported (the\n    paper gives none).\n- id: ed4-lick-modulated-few\n  statement: In both ALM and the CN, a similar small proportion of neurons (under 10%) modulates\n    its spike rate during individual licks.\n  source: Main text, paragraph 9; Extended Data Figure 4a to 4c\n  quote: In both regions, a similar proportion (<10%) of neurons modulated their spike rates\n    during individual licks\n  expected:\n  - quantity: upper bound on the fraction of lick-modulated neurons, ALM and each CN nucleus\n    value: 0.1\n    tolerance: 0.01\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: As Extended Data Fig. 4a, for each lick, spike counts in two adjacent 50 ms windows\n    starting 20 ms from the lick detection time; across all licks and trials, a two-tailed t-test\n    between the two windows at p < 0.01 marks a neuron as lick-modulated. Whether the test is\n    paired across licks is not stated (open; readings paired and unpaired). Reproduced when under\n    one reading the fraction in ALM and in each CN nucleus is below 0.11.\n- id: fig2cd-selectivity-emerges-gradually\n  statement: Selectivity for \"lick left\" and \"lick right\" trials emerges gradually in both the\n    ALM and the CN population averages, starting during the sample epoch and peaking in the\n    response epoch.\n  source: Main text, paragraph 10; Figure 2c and 2d\n  quote: Selectivity for \"lick left\" and \"lick right\" trials emerged gradually in both ALM and CN\n    population averages ( Fig 2c–d ), starting during the sample epoch and reaching a maximum at\n    the response epoch\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 over selective neurons. The Fig. 2 legend, which gives\n    the neurons averaged, is not in the text read, so the population is open (readings (a) all\n    selective neurons, ALM 980 and CN 416; (b) those with significant sample or delay\n    selectivity). The per-nucleus counts of Extended Data Fig. 4f (87 + 50 + 60 = 197) equal 35%\n    of 564, the CN preparatory fraction, which supports (b) for the CN. Reproduced in a region\n    when, under one reading, the bootstrap 95% interval over neurons excludes zero in at least one\n    window of the sample epoch, the mean over the delay epoch exceeds the mean over the sample\n    epoch, and the maximum of the time course lies in the response epoch.\n- id: ed4e-cn-predicts-movement\n  statement: Most CN neurons with delay selectivity predict the upcoming licking direction, not\n    object location (67%), switching their preference on error trials.\n  source: Main text, paragraph 10; Extended Data Figure 4e\n  quote: However, most CN neurons predicted the upcoming licking direction (67%, Extended Data Fig\n    4 ), similar to ALM\n  expected:\n  - quantity: fraction of CN neurons with a negative error-to-correct selectivity ratio\n    value: 0.67\n    tolerance: 0.067\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: CN neurons with significant delay selectivity (E2) tested on > 3 error trials (n = 73\n    in the paper, Extended Data Fig. 4e). For each, the ratio of delay selectivity (spike rate\n    difference by instructed trial type) on error trials to that on correct trials; a negative\n    ratio means the neuron follows the movement. Reproduced when the fraction with a negative\n    ratio is within tolerance.\n- id: ed4f-preparatory-all-nuclei\n  statement: Preparatory activity is present in all three cerebellar nuclei (fastigial,\n    interposed and dentate).\n  source: Main text, paragraph 11; Extended Data Figure 4f\n  quote: Preparatory activity was present in all three cerebellar nuclei ( Extended Data Fig 3 – 4 )\n  expected:\n  - quantity: fastigial neurons in the population selectivity\n    value: 87\n    tolerance: 8.7\n  - quantity: interposed neurons in the population selectivity\n    value: 50\n    tolerance: 5\n  - quantity: dentate neurons in the population selectivity\n    value: 60\n    tolerance: 6\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 for each nucleus (Extended Data Fig. 4f, mean and s.e.m.\n    across neurons by bootstrap). Which neurons enter is not stated; the readings are those of\n    fig2cd-selectivity-emerges-gradually ((a) all selective neurons of the nucleus, (b) those\n    with significant sample or delay selectivity). Reproduced when under one reading, in each\n    nucleus, the bootstrap 95% interval over neurons excludes zero in at least one 200 ms window\n    of the delay epoch. The counts are reported against their expected values (or as fractions\n    of 268, 139 and 157 where the dataset holds fewer neurons).\n- id: ed4g-fastigial-contra-late-delay\n  statement: In the fastigial nucleus, equal numbers of neurons prefer contralateral and\n    ipsilateral movement in the early delay, and a population preference for contralateral\n    movement develops just before movement initiation.\n  source: Main text, paragraph 11; Extended Data Figure 4g\n  quote: equal numbers of neurons preferred either contralateral or ipsilateral movement during the\n    early delay, and a population-level preference for contralateral movement developed right\n    before movement initiation\n  statistics:\n  - test: one-sided bootstrap\n    p: 0.0001\n    n: 15 mice (fastigial)\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Per neuron, the preferred direction from spike counts in the first 500 ms and in the\n    last 500 ms of the delay, among neurons selective in that window (E2 test on that window, as\n    the legend implies; open whether selectivity is from that window or from E2 over epochs, both\n    run). Reproduced when the contra-preferring fraction in the last 500 ms exceeds one half with\n    a one-sided bootstrap over mice (B1 resampling scheme) p < 0.001 and the first 500 ms\n    fraction does not differ from one half at p < 0.05.\n- id: fig3-cn-altered-by-alm-inhibition\n  statement: Bilateral ALM photo-inhibition during the delay rapidly alters the activity of many\n    CN neurons (185 of 389), with a latency of 10.7 plus or minus 4.0 ms.\n  source: Main text, paragraph 12; Figure 3a and 3b; Extended Data Figure 5a\n  quote: Activity of many CN neurons was rapidly altered by ALM photo-inhibition (185/389, p<0.01,\n    two-tailed t-test; latency, 10.7 ± 4.0 ms, mean ± s.e.m.)\n  expected:\n  - quantity: CN neurons recorded during ALM photo-inhibition\n    value: 389\n    tolerance: 38.9\n  - quantity: CN neurons significantly modulated\n    value: 185\n    tolerance: 18.5\n  - quantity: latency\n    value: 10.7\n    tolerance: 4.0\n    unit: ms\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Modulated as E4 on the whole delay epoch; latency as E5 (both readings). Reproduced\n    when under one reading of E4 and E5 the count (or the fraction 0.48 where the dataset holds\n    fewer neurons) and the latency are within tolerance.\n- id: fig3b-cn-net-disinhibition\n  statement: ALM photo-inhibition makes more CN neurons increase than decrease their activity\n    (123 against 62 of 185), a net disinhibition of the CN.\n  source: Main text, paragraph 12; Figure 3b\n  quote: Photo-inhibiting ALM caused a greater proportion of CN neurons to increase their activity,\n    resulting in net disinhibition of CN ( Fig 3b , 123/185 increase, 62/185 decrease, p<0.001,\n    binomial test)\n  statistics:\n  - test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    n: 185 modulated CN neurons\n  expected:\n  - quantity: modulated CN neurons that increase\n    value: 123\n    tolerance: 12.3\n  - quantity: modulated CN neurons that decrease\n    value: 62\n    tolerance: 6.2\n  depends_on:\n  - fig3-cn-altered-by-alm-inhibition\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Among the neurons modulated in fig3-cn-altered-by-alm-inhibition, the sign of the\n    delay epoch rate change. Reproduced when the counts are within tolerance (or the increase\n    fraction 0.66 within 10%, where the dataset holds fewer neurons) and a binomial test against\n    one half gives p < 0.001 (sidedness not given; two-sided, the stricter, is used).\n- id: fig3c-cn-selectivity-abolished\n  statement: ALM photo-inhibition abolishes CN selectivity for \"lick left\" and \"lick right\"\n    trials.\n  source: Main text, paragraph 12; Figure 3c; Extended Data Figure 5b to 5d\n  quote: CN selectivity for \"lick left\" and \"lick right\" trials was abolished by photo-inhibiting\n    ALM\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 over selective CN neurons tested on > 3 trials in all\n    conditions (n = 157, Extended Data Fig. 6c; 54 fastigial, 44 interposed and 59 dentate,\n    Extended Data Fig. 5b to 5d), control against photo-inhibition trials. The window is open\n    (readings (a) the whole delay epoch, the photo-inhibition period; (b) the last 500 ms of the\n    delay, as in Extended Data Fig. 9b). Reproduced when under one reading the control\n    selectivity is above zero (bootstrap 95% interval over neurons) and the photo-inhibition\n    selectivity is not distinguishable from zero (its interval includes zero).\n- id: ed6-cn-selectivity-both-alm-hemispheres\n  statement: Photo-inhibiting either hemisphere of ALM reduces CN preparatory activity, and\n    photo-inhibiting motor cortex posterior to ALM has less effect.\n  source: Main text, paragraph 13; Extended Data Figure 6a to 6e\n  quote: Photo-inhibiting either side of ALM reduced CN preparatory activity ( Extended Data Fig 6a–d\n    ). Photo-inhibiting motor cortex regions posterior to ALM produced less effect on CN\n    preparatory activity\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 over the n = 157 neurons of Extended Data Fig. 6c, delay\n    window readings as in fig3c-cn-selectivity-abolished, in control, contralateral and\n    ipsilateral unilateral ALM photo-inhibition trials. Reproduced when both unilateral\n    conditions lower selectivity below control (bootstrap 95% interval of the difference over\n    neurons excludes zero). The M1 comparison is shown only with example neurons in the paper\n    (Extended Data Fig. 6e); it is reported, with the same measure on neurons tested with M1\n    photo-inhibition, but does not decide the outcome.\n- id: fig3d-alm-altered-by-cn-inhibition\n  statement: CN photo-inhibition during the delay rapidly alters the activity of many ALM neurons\n    (197 of 454), with a latency of 7.1 plus or minus 3.8 ms.\n  source: Main text, paragraph 14; Figure 3d and 3e; Extended Data Figure 5e\n  quote: Activity of many ALM neurons was rapidly altered by CN photo-inhibition (197/454, p<0.01,\n    two-tailed t-test, Extended Data Fig 5e ; latency, 7.1 ± 3.8 ms)\n  expected:\n  - quantity: ALM pyramidal neurons recorded during CN photo-inhibition\n    value: 454\n    tolerance: 45.4\n  - quantity: ALM neurons significantly modulated\n    value: 197\n    tolerance: 19.7\n  - quantity: latency\n    value: 7.1\n    tolerance: 3.8\n    unit: ms\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: ALM recordings during contralateral CN photo-inhibition in the 4 L7-cre x Ai32 mice\n    (19 sessions); units as E1; photo-inhibition 1.3 s from delay onset, both powers pooled (1.5\n    or 4.5 mW, Methods, CN photo-inhibition; Extended Data Fig. 5e gives 1.5 to 4.5 mW). The CRCNS\n    descriptor also lists a 500 ms delay photo-inhibition code; the Methods describe only the 1.3\n    s photostimulus for these recordings, so 1.3 s trials are used. Modulated as E4 on the whole\n    delay epoch; latency as E5 (both readings). Reproduced when under one reading the count (or\n    the fraction 0.43 where the dataset holds fewer neurons) and the latency are within\n    tolerance.\n- id: fig3e-alm-mean-rate-unchanged\n  statement: Despite the changes in individual neurons, the average ALM spike rate is nearly\n    unchanged by CN photo-inhibition (4.15 against 4.39 spikes/s).\n  source: Main text, paragraph 14\n  quote: 'However, the average spike rate was nearly unchanged (control: 4.15 spikes/s;\n    photo-inhibition: 4.39 spikes/s; p=0.58, two-tailed t-test)'\n  statistics:\n  - test: two-tailed t-test\n    p: 0.58\n  expected:\n  - quantity: mean ALM spike rate, control\n    value: 4.15\n    tolerance: 0.415\n    unit: spikes/s\n  - quantity: mean ALM spike rate, CN photo-inhibition\n    value: 4.39\n    tolerance: 0.439\n    unit: spikes/s\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence, judged on the paper's two-tailed t-test at p < 0.05. Mean delay\n    epoch spike rate per neuron in control and photo-inhibition trials (E4 trials). Open, and run\n    under each reading, are the neurons averaged ((a) all 454 pyramidal neurons, (b) the 197\n    modulated) and whether the t-test is paired over neurons or unpaired. Reproduced when the\n    rates are within tolerance under one reading of the neurons and the t-test finds no\n    difference; the outcome is marked as resting on the reading when paired and unpaired\n    disagree. The rate change is reported.\n- id: fig3e-alm-increase-decrease\n  statement: Among ALM neurons modulated by CN photo-inhibition, 108 increase and 89 decrease\n    their responses.\n  source: Main text, paragraph 14; Figure 3e\n  quote: Individual ALM neurons increased (108/197) or decreased (89/197) their responses during CN\n    photo-inhibition\n  expected:\n  - quantity: modulated ALM neurons that increase\n    value: 108\n    tolerance: 10.8\n  - quantity: modulated ALM neurons that decrease\n    value: 89\n    tolerance: 8.9\n  depends_on:\n  - fig3d-alm-altered-by-cn-inhibition\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Sign of the delay epoch rate change among the neurons of\n    fig3d-alm-altered-by-cn-inhibition. Reproduced when both counts are within tolerance, or,\n    where the dataset holds fewer neurons, the increase fraction (0.55) is within 10%.\n- id: fig3f-alm-selectivity-abolished-by-cn-inhibition\n  statement: CN photo-inhibition abolishes ALM trial-type selectivity.\n  source: Main text, paragraph 14; Figure 3f\n  quote: ALM trial-type selectivity was abolished by CN photo-inhibition ( Fig 3f )\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 (preferred type from 10 trials) over selective ALM\n    neurons tested on > 3 trials in all conditions (the selection of the Extended Data Fig. 5b\n    and 9c legends; the Fig. 3f count is not in the text read), control against CN\n    photo-inhibition trials, all trials grouped by instructed type. Window readings as in\n    fig3c-cn-selectivity-abolished. Reproduced when under one reading the control selectivity is\n    above zero (bootstrap 95% interval over neurons) and the photo-inhibition selectivity is not\n    distinguishable from zero. The neuron count is reported.\n- id: fig4bc-fastigial-targets-alm-thalamus\n  statement: Fastigial projections overlap ALM-projecting thalamus (VM and parts of VAL) more than\n    dentate projections, which target a more dorsal and lateral region.\n  source: Main text, paragraph 15; Figure 4b and 4c; Extended Data Figure 7d to 7f\n  quote: Fastigial projections mostly overlapped with parts of the thalamus that project to ALM\n    (i.e., ventral medial nucleus, VM, and parts of anterior-lateral nucleus, VAL), whereas\n    dentate projections targeted an adjacent region that was more dorsal and lateral\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Anatomy (6 fastigial, 4 dentate and 8 ALM injections, Extended Data Fig. 7d). Area\n    fraction overlap per coronal section after CCF alignment and thresholding near the 89th\n    percentile (Methods, Anatomy, analysis). The paper reports no test; reproduced when the\n    fastigial overlap is higher than the dentate overlap in sections from the same brains.\n- id: ed8-snr-sc-converge\n  statement: ALM-projecting thalamus receives inputs from the SNr and the lateral superior\n    colliculus with overlaps comparable to the fastigial nucleus, while dentate overlap is lower.\n  source: Extended Data Figure 8b\n  quote: Fastigial, SNr, and superior colliculus labeling show comparable amount of overlaps with\n    ALM-projecting thalamus. Dentate labeling show less overlap\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Area fraction overlap as in fig4bc-fastigial-targets-alm-thalamus, per source area.\n    No test reported; reproduced when the SNr and superior colliculus overlaps lie within the\n    range of the fastigial overlaps and the dentate overlaps lie below it.\n- id: fig4-fastigial-activation-alm-latency\n  statement: Fastigial photo-activation changes ALM activity rapidly (latency 4.5 plus or minus\n    2.6 ms), consistent with a disynaptic pathway through the thalamus.\n  source: Main text, paragraph 16; Extended Data Figure 9a\n  quote: Fastigial photo-activation induced rapid changes in ALM activity (latency, 4.5 ± 2.6 ms;\n    Extended Data Fig 9a ), consistent with a disynaptic pathway through the thalamus\n  expected:\n  - quantity: latency of the ALM response to fastigial photo-activation\n    value: 4.5\n    tolerance: 2.6\n    unit: ms\n  - quantity: ALM neurons significantly modulated by fastigial photo-activation\n    value: 227\n    tolerance: 22.7\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: ALM pyramidal neurons in the fastigial photo-activation sessions (6 mice,\n    Supplemental Table 1), early delay photo-activation (0.455 s from delay onset, main text\n    paragraph 16 and Methods; powers 0.5, 1 and 1.5 mW pooled, as the Methods give no split).\n    Modulated as E4 at p < 0.01; latency as E5 (both readings). Reproduced when under one reading\n    the latency is within tolerance and the count is within tolerance where the dataset holds\n    all 6 mice; otherwise the count and its fraction of the neurons are reported, as the number\n    of neurons in these sessions is not in the text read.\n- id: fig4e-fastigial-activation-abolishes-alm-selectivity\n  statement: Fastigial photo-activation abolishes selective persistent and ramping activity in\n    most ALM neurons, while in a minority it creates new preparatory activity.\n  source: Main text, paragraph 16; Figure 4e; Extended Data Figure 9c\n  quote: Selective persistent and ramping activity was abolished in most ALM neurons ( Fig 4e , top).\n    In a minority of neurons, photo-activation created new preparatory activity\n  expected:\n  - quantity: selective ALM neurons tested on more than 3 trials in all conditions, fastigial\n      sessions\n    value: 328\n    tolerance: 32.8\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Population selectivity as E3 over the selective ALM neurons tested on > 3 trials in\n    all conditions (n = 328, Extended Data Fig. 9c), control against fastigial photo-activation\n    trials, in the delay after the photostimulus (readings (a) from photostimulus offset to the\n    go cue, (b) the last 500 ms of the delay, as in Extended Data Fig. 9b). The paper gives no\n    per-neuron test; the one used here is named as a choice. Per neuron, abolished means delay\n    selectivity significant in control (E2 test on that window) and not in photo-activation\n    trials; new means the reverse. Reproduced when under one reading the population selectivity\n    is lower in photo-activation trials (bootstrap 95% interval of the difference excludes\n    zero), more than half of the control-selective neurons lose significance, and the neurons\n    gaining it are fewer than those losing it.\n- id: fig4f-fastigial-effect-persists\n  statement: Transient fastigial photo-activation alters ALM preparatory activity long (more than\n    1 s) after the photostimulus ends.\n  source: Main text, paragraph 16; Figure 4f; Extended Data Figure 9b\n  quote: Transient photo-activation of the fastigial nucleus altered ALM preparatory activity long\n    (>1 s) after cessation of the photostimulus\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: For each ALM pyramidal neuron of the fastigial photo-activation sessions, E4 in 400\n    ms bins in 50 ms steps (Methods, for Fig. 4f) gives the fraction with a significant change (p\n    < 0.01). What the fraction is compared with is not given (open; readings (a) the 1% expected\n    by chance at p < 0.01, (b) the fraction in the bins before photostimulus onset). Reproduced\n    when under one reading the fraction in bins starting 1 s or more after photostimulus offset\n    (and ending before the go cue or within the response epoch) exceeds the comparison, by a\n    one-sided binomial test at p < 0.05 for reading (a) or a one-sided test of two proportions\n    for reading (b).\n- id: fig4g-dentate-effect-recovers\n  statement: Dentate photo-activation also changes ALM responses (latency 8.3 plus or minus 5.0\n    ms), but ALM activity recovers quickly after it.\n  source: Main text, paragraph 16; Figure 4g; Extended Data Figure 9a\n  quote: Dentate photo-activation also induced ALM response changes ( Fig 4g ; latency, 8.3 ± 5.0\n    ms). Importantly, activity quickly recovered after dentate photo-activation\n  expected:\n  - quantity: latency of the ALM response to dentate photo-activation\n    value: 8.3\n    tolerance: 5.0\n    unit: ms\n  - quantity: ALM neurons significantly modulated by dentate photo-activation\n    value: 163\n    tolerance: 16.3\n  depends_on:\n  - fig4f-fastigial-effect-persists\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: As fig4-fastigial-activation-alm-latency and fig4f-fastigial-effect-persists on the\n    ALM pyramidal neurons of the dentate sessions (3 mice, Supplemental Table 1). Reproduced when\n    under one reading the latency is within tolerance (and the count, where the dataset holds all\n    3 mice), and the fraction of significant neurons in bins starting 1 s or more after\n    photostimulus offset is not above the comparison of fig4f-fastigial-effect-persists (same\n    test, p >= 0.05) and is lower than the fastigial fraction in the same bins.\n- id: fig4i-cd-control-separation\n  statement: In control trials, ALM activity trajectories for \"lick left\" and \"lick right\"\n    diverge along the coding direction during the sample epoch and stay separated through the\n    delay epoch.\n  source: Main text, paragraph 17; Figure 4h and 4i\n  quote: In control trials, activity trajectories from \"lick left\" and \"lick right\" trials diverged\n    from each other along the cd during the sample epoch and remained separated throughout the\n    delay epoch\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Coding direction and projections as E6, over the 28 sessions. Separation is the\n    \"lick right\" minus \"lick left\" projection of control trials, averaged across sessions, with a\n    bootstrap over sessions. Reproduced when the 95% interval excludes zero at some time in the\n    sample epoch and at every 400 ms window centred within the delay epoch.\n- id: fig4i-fastigial-collapses-cd\n  statement: Fastigial photo-activation collapses ALM activity trajectories along the coding\n    direction, while dentate photo-activation minimally affects them.\n  source: Main text, paragraph 17; Figure 4i; Extended Data Figure 9c\n  quote: Fastigial photo-activation resulted in a collapse of activity trajectories ... In\n    contrast, dentate photo-activation minimally impacted activity trajectories along the cd ,\n    despite having an impact on ALM neuron responses\n  depends_on:\n  - fig4i-cd-control-separation\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Separation along the cd as in fig4i-cd-control-separation, in control, fastigial and\n    dentate photo-activation trials, in the last 400 ms of the delay (the window of Extended Data\n    Fig. 10c, Methods) and averaged from photostimulus offset to the go cue. \"Collapse\" is open\n    (readings (a) fastigial separation not distinguishable from zero; (b) fastigial separation\n    lower than control, the bootstrap interval of the difference over sessions excluding zero).\n    Reproduced when under one reading and one window the fastigial separation collapses and, in\n    the same window, the dentate separation does not differ from its control (interval of the\n    difference includes zero).\n- id: cd-captures-selectivity\n  statement: The projection along the coding direction captures 64.1% of ALM population\n    selectivity over the sample and delay epochs and 27.0% of the total variance in task-related\n    activity.\n  source: Methods, Analysis of ALM population dynamics in the activity space, paragraph 2\n  quote: The projection along the cd captured 64.1±3.4% of the population selectivity for \"lick\n    left\" and \"lick right\" trials over the sample and delay epochs (root mean square, RMS, of the\n    spike rate difference between \"lick right\" and \"lick left\" trials), and 27.0±4.2% of the total\n    variance in ALM task-related activity\n  expected:\n  - quantity: fraction of population selectivity captured by the cd\n    value: 64.1\n    tolerance: 3.4\n    unit: \"%\"\n  - quantity: fraction of task-related variance captured by the cd\n    value: 27.0\n    tolerance: 4.2\n    unit: \"%\"\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: Per session (E6), on control trials over the sample and delay epochs. Selectivity is\n    the RMS of the \"lick right\" minus \"lick left\" rate difference; variance is the RMS of the\n    baseline-subtracted activity. How the captured fraction is formed is open (readings (a) the\n    ratio of the RMS along the unit cd to the RMS over all neurons; (b) the ratio of their squares,\n    a fraction of variance); the baseline window is not given (reading the 500 ms before sample\n    onset, a standard choice). The paper does not name the spread as s.e.m. or s.d.; it is used\n    as the tolerance as stated. Reproduced when under one reading both means are within\n    tolerance.\n- id: ed10b-fastigial-activation-errors-during-recording\n  statement: In the ALM recording sessions, contralateral fastigial photo-activation lowers\n    behavioral performance, with \"lick left\" and \"lick right\" trials pooled, in the 6 mice.\n  source: Extended Data Figure 10a and 10b\n  quote: Performance in control (grey) and photostimulation trials (cyan). \"Lick left\" and \"lick\n    right\" trials are pooled. Chance is 50% (dashed line). Lines, individual mice (ALM\n    photo-inhibition, n=7; fastigial photo-activation, n=6). ***, p<0.001, one-sided test,\n    bootstrap (Methods).\n  statistics:\n  - test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 6 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: ALM recording sessions with contralateral fastigial photo-activation (Extended Data\n    Fig. 10a; the 6 mice of Supplemental Table 1), early delay photo-activation (0.455 s from\n    delay onset, main text paragraph 16), all powers pooled. Pooled performance (B1), control\n    against photo-activation trials. Reproduced when performance drops with a one-sided\n    hierarchical bootstrap (B1) p < 0.001.\n- id: ed10c-alm-inhibition-endpoints-predict\n  statement: After bilateral ALM photo-inhibition in the early delay, the distance of ALM\n    trajectories to the endpoints along the coding direction still predicts the future movement,\n    though performance is near chance.\n  source: Supplementary Information, page 1, paragraph 1; Extended Data Figure 10b and 10c\n  quote: But in a trial-by-trial analysis movement direction could still be predicted based on the\n    distance of the perturbed activity trajectories to the endpoints on the cd\n  statistics:\n  - about: performance drop with bilateral ALM photo-inhibition\n    test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 7 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: The paper does not say which mice or sessions carried bilateral ALM photo-inhibition\n    during ALM recording (n = 690 trials; ALM photo-inhibition needs VGAT-ChR2 mice, which\n    Supplemental Table 1 does not list for ALM recordings, and the CRCNS descriptor lists no ALM\n    photo-inhibition code). The supplement introduces this result with \"Previously, we found\" and\n    cites its refs. 1 and 2 (Li et al. 2016; Inagaki et al. 2017), so these trials may come from\n    those studies and not from this paper's recordings. Where the datasets hold such trials, the\n    projection cd'x in the last 400 ms of the delay (E6, cd from independent correct control\n    trials; Methods) is binned and the probability of licking right is computed per bin, pooled\n    over sessions. Reproduced when that probability rises with the projection, by a logistic\n    regression of lick direction on the projection with slope p < 0.05 (a standard test named\n    here, the paper gives none), and pooled performance drops with a one-sided bootstrap p <\n    0.001 (B1).\n- id: ed10d-fastigial-endpoints-no-prediction\n  statement: After fastigial photo-activation, the distance of ALM trajectories to the endpoints\n    along the coding direction no longer predicts future movements.\n  source: Supplementary Information, page 1, paragraph 1; Extended Data Figure 10d\n  quote: After fastigial photo-activation, the distance of the perturbed trajectories to these\n    endpoints no longer predicted future movements\n  depends_on:\n  - fig4i-cd-control-separation\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: A claim of absence; the paper shows a binned curve (n = 337 fastigial photo-activation\n    trials, Extended Data Fig. 10d) and names no test. As ed10c-alm-inhibition-endpoints-predict\n    on the fastigial photo-activation trials of the ALM recording sessions, with the logistic\n    regression named there at p < 0.05. Reproduced when the slope is not significant; the slope\n    and its interval are reported, with the slope on control trials for comparison.\n- id: ed10ef-alm-drives-licking-after-fastigial\n  statement: Unilateral ALM photo-inhibition before the go cue biases licking ipsilaterally\n    whether or not a fastigial perturbation preceded it, and bilateral ALM photo-inhibition\n    during movement initiation raises the no-lick rate even after a fastigial perturbation.\n  source: Supplementary Information, page 1, paragraph 2; Extended Data Figure 10e to 10g\n  quote: Unilateral ALM photo-inhibition before movement initiation biased upcoming movements to the\n    ipsilateral direction regardless of a preceding fastigial perturbation (Extended Data Fig\n    10e-f). Bilateral ALM photo-inhibition during movement initiation led to an increased no lick\n    rate even after a preceding fastigial perturbation\n  statistics:\n  - about: unilateral ALM photo-inhibition alone, performance on contralateral trials\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 4 mice\n  - about: unilateral ALM photo-inhibition after fastigial perturbation, weaker mark\n    test: one-sided bootstrap\n    p: 0.04\n    n: 4 mice\n  - about: unilateral ALM photo-inhibition after fastigial perturbation, stronger mark\n    test: one-sided bootstrap\n    p: 0.008\n    n: 4 mice\n  - about: no lick rate, bilateral ALM photo-inhibition, weaker mark\n    test: one-sided bootstrap\n    p: 0.002\n    n: 3 mice\n  - about: no lick rate, bilateral ALM photo-inhibition, stronger mark\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 3 mice\n  datasets:\n  - \"000007\"\n  - crcns-alm-4\n  criterion: VGAT-ChR2-EYFP behavior (Methods, ALM photo-inhibition after a fastigial\n    perturbation). Unilateral ALM photo-inhibition from 800 ms after delay onset to the go cue;\n    performance per trial type (B1) with trials grouped by licking direction relative to the\n    inhibited ALM. Reproduced when, both alone and after the fastigial perturbation,\n    performance on trials instructing contralateral licking drops with a one-sided bootstrap p <\n    0.05, and when the no-lick rate with bilateral ALM photo-inhibition (1.3 s from the go cue)\n    after the perturbation exceeds that with the perturbation alone, one-sided bootstrap p <\n    0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt; python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/gao-2018.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum(len(x.get('statistics',[])) for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
ids=[x['id'] for x in c]; assert len(ids)==len(set(ids))
EOF
grep -n "—\|rather" claims/gao-2018.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
M claims/gao-2018.yaml
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

I've updated `claims/gao-2018.yaml` to pilot-15. The quote checker passes: 46 claims, 46 quotes, 17 statistical values, 0 problems. Nothing is committed.

**Text read.** The stored text is now the version of record (PMC6212318, open access, Europe PMC XML). It holds the main text, the Methods, the legends of Extended Data Figs. 1 to 10, and the Supplementary Information, including Supplemental Table 1. The last file was written from the NIH author manuscript. `supp2.pdf` is the Nature reporting summary. The paper links no code. The reporting summary says scripts "will be deposited on CRCNS.org" but gives no identifier, so no code was read.

**Missing from the text.** The legends of main Figs. 1 to 4 are not in the stored text, and there is no PDF of the main paper. The previous file took several details from those legends, and I can't check them now:
- the significance marks of Fig. 1d, 1e, 1g and 1h;
- the Fig. 3f neuron count (n = 329) and the Fig. 2d count (197);
- the split of the 912 ALM neurons into fastigial and dentate sessions (446/466);
- the power ranges in the Fig. 3d and 4d legends.

I removed the statistics that came only from those legends (Fig. 1d, 1e, 1g delay, 1h response) and the n = 329 expected value. Where the paper gives no other threshold, the criteria now use the bootstrap at p < 0.05 (the lowest mark in the paper's bootstrap legends), named as a choice. Power ranges now cite the Methods and Extended Data Fig. 5e. If the main figure legends can be supplied, these details can go back in.

**What changed.**
- Every claim now has `datasets: ["000007", crcns-alm-4]`. The opening comment says which experiments each dataset is described as holding: ALM recordings only, with no CN recordings. Claims on the lesions, the CN recordings, the 1.3 s photostimulation, the movement tests, the VGAT behavior and the anatomy are kept; the author blocks them as data_missing if neither dataset has them. The comment also notes that the 6 mice of the 0.5 s fastigial photo-activation behavior are the 6 ALM-recording mice (Supplemental Table 1).
- New claim `ed10b-fastigial-activation-errors-during-recording`: performance drops during the ALM recording sessions (Extended Data Fig. 10b, p < 0.001, 6 mice). I moved that statistic off `ed10d`, where the test was not the finding.
- Sources now give main-text paragraph numbers counted from the opening paragraph. The old numbers were off.
- I removed the old `checks` block, because its "ready" verdict was for the previous version. The file needs a new check.

**Counts.** 46 claims, all with quotes and criteria. 12 claims have statistics (17 entries), and 17 have expected values.

**Details the paper leaves open, with the readings named:**
- **Response-epoch window for selectivity:** 1.3 s from the go cue, or 0 to 1.5 s.
- **Which trials enter selectivity:** correct trials only, or all trials with a lick grouped by instruction.
- **Which trials enter the photostimulation effect test:** all trials, or correct trials only.
- **Window that decides "modulated" for latency:** the photostimulation period, or the whole delay.
- **Lesion test:** mice pooled, or tested one by one.
- **Photostimulus for Fig. 1h, the Fig. 1g dentate bar, and delay photo-inhibition:** 0.455 or 0.5 s, against 1.3 s.
- **Lick bouts:** before against after the lesion, or contra- against ipsilesional.
- **Denominator for preparatory and peri-movement fractions:** all neurons, or selective neurons.
- **Population for the CN averages:** all selective neurons, or those selective in the sample or delay.
- **Lick-modulation t-test:** paired or unpaired.
- **Window for selectivity under photostimulation:** the whole delay, or its last 500 ms.
- **ALM mean-rate test:** all 454 neurons or the 197 modulated, and paired or unpaired.
- **ED10 VGAT percentages:** pooled over trials, or averaged over mice.
- **Comparison for the persistent fastigial effect:** the 1% chance rate, or the bins before the photostimulus.
- **"Collapse" along the coding direction:** not different from zero, or lower than control.
- **Captured fraction:** a ratio of RMS values, or of squared RMS values.

These are fixed as standard choices: the coding-direction trial split, the 200 ms averaging window, the baseline window, and the tests the paper doesn't give (per-mouse bias, the licking absence claims, the endpoint logistic regression).

**Other gaps.** The supplement presents the Extended Data Fig. 10c trials (bilateral ALM photo-inhibition) as an earlier finding citing Li et al. 2016 and Inagaki et al. 2017, so they may not be in either dataset. The paper doesn't say whether the ±3.4% and ±4.2% spreads on the coding-direction figures are s.e.m. or s.d.

## End of run

31 turns, 7 minutes, $2.78 at API prices, result: success.
