# openneuro-ds000228 · recorder · run 40746467635

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py openneuro-ds000228; ls claims/openneuro-ds000228/ transcripts/openneuro-ds000228/; cat attempts/openneuro-ds000228-richardson-2018-01.yaml
```

```
<persisted-output>
Output too large (57.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/bcm2gvz1b.txt

Preview (first 2KB):
docs/pilot-notes/openneuro-ds004752-dimakopoulos-2022-01.md
docs/pilot-notes/001177-zhuang-2025-01.md
docs/pilot-notes/000248-shin-2025-01.md
docs/pilot-notes/000336-gillon-2023-01.md
docs/pilot-notes/000253-siegle-2021-01.md
| [OPENNEURO:ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1) | [Richardson et al. 2018](https://doi.org/10.1038/s41467-018-03399-2) | 15 (+1) | 8 (+1) | 12 (+3) | 0 (+1) | [`openneuro-ds000228-richardson-2018`](entries/openneuro-ds000228-richardson-2018) |
claims/openneuro-ds000228/:
10.1038-s41467-018-03399-2.yaml

transcripts/openneuro-ds000228/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in openneuro-ds004752-dimakopoulos-2022-01.md 001177-zhuang-2025-01.md 000248-shin-2025-01.md 000336-gillon-2023-01.md 000253-siegle-2021-01.md 001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done; cd ../..; grep -n -B3 "^| \[OPENNEURO:ds004752\|^| Dataset\|^|---" README.md | head; cat tools/readme_row.py | head -60
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/bdom4eecg.txt

Preview (first 2KB):
=== openneuro-ds004752-dimakopoulos-2022-01.md
# openneuro-ds004752, Dimakopoulos et al. 2022

Seven claims reproduced, three partially, ten not reproduced and none blocked
on the dataset alone; `table1-left-hemisphere-sources`, which needs a head
model and atlas from outside the dataset, is blocked as `not_runnable`. It pins
version 1.0.1, its latest published version. The paper, Dimakopoulos,
Mégevand, Stieglitz, Imbach and Sarnthein in eLife, records hippocampal depth
LFP and scalp EEG in 15 participants with drug-resistant focal epilepsy
performing a modified Sternberg verbal working memory task, with subdural ECoG
in Participants 1 to 4, and reports by spectral Granger causality (GC) that
theta net flow runs from auditory cortex to the hippocampus during encoding and
reverses during maintenance, in each participant and across the group. The
claims were written from the version of record in Europe PMC (PMC9374435),
without the supplement's content, and from the paper's code
(vdimakopoulos/verbal_working_memory at commit 395ae13). The behaviour, the
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/bdom4eecg.txt"
}
```

```
1	=== openneuro-ds004752-dimakopoulos-2022-01.md
2	# openneuro-ds004752, Dimakopoulos et al. 2022
3	
4	Seven claims reproduced, three partially, ten not reproduced and none blocked
5	on the dataset alone; `table1-left-hemisphere-sources`, which needs a head
6	model and atlas from outside the dataset, is blocked as `not_runnable`. It pins
7	version 1.0.1, its latest published version. The paper, Dimakopoulos,
8	Mégevand, Stieglitz, Imbach and Sarnthein in eLife, records hippocampal depth
9	LFP and scalp EEG in 15 participants with drug-resistant focal epilepsy
10	performing a modified Sternberg verbal working memory task, with subdural ECoG
11	in Participants 1 to 4, and reports by spectral Granger causality (GC) that
12	theta net flow runs from auditory cortex to the hippocampus during encoding and
13	reverses during maintenance, in each participant and across the group. The
14	claims were written from the version of record in Europe PMC (PMC9374435),
15	without the supplement's content, and from the paper's code
16	(vdimakopoulos/verbal_working_memory at commit 395ae13). The behaviour, the
17	gamma, beta and phase locking results of Participant 1, hippocampal beta, the
18	GC of the four ECoG participants, the group GC between the hippocampus and the
19	dataset's beamformer virtual sensors (Figure 4 and Table 1) and the scalp
20	Laplacian control were tested. The left-hemisphere share of the EEG sources
[... 590 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/openneuro-ds000228-richardson-2018-01.yaml; grep -rln "outside data\|with_inputs" docs/pilot-notes | head
```

```
<persisted-output>
Output too large (57.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/bsohq299m.txt

Preview (first 2KB):
schema_version: 2
id: openneuro-ds000228-richardson-2018-01
dataset:
  archive: openneuro
  id: ds000228
  version: 1.1.1
  doi: 10.18112/openneuro.ds000228.v1.1.1
paper: doi:10.1038/s41467-018-03399-2
date: 2026-10-28
entry: openneuro-ds000228-richardson-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/bsohq299m.txt"
}
```

```
1	schema_version: 2
2	id: openneuro-ds000228-richardson-2018-01
3	dataset:
4	  archive: openneuro
5	  id: ds000228
6	  version: 1.1.1
7	  doi: 10.18112/openneuro.ds000228.v1.1.1
8	paper: doi:10.1038/s41467-018-03399-2
9	date: 2026-10-28
10	entry: openneuro-ds000228-richardson-2018
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 1057 more lines not kept]
```

**Agent**

Read the attempt record and the recent notes. Now checking the claims file, the dataset's target entry, and the reports.

**Agent calls Bash**

```bash
grep -n "with_inputs\|outside data\|outside input" docs/pilot-notes/001550-pagan-2025-01.md docs/pilot-notes/000035-scala-2021-01.md | head -5; f=claims/openneuro-ds000228/*.yaml; head -40 $f; grep -n "^- id:\|  data:\|  kind:" $f; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for x in (items if isinstance(items,list) else items.values()):
  if 'ds000228' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
docs/pilot-notes/001550-pagan-2025-01.md:4:reproduced or blocked. With outside data, counted apart: two reproduced and
docs/pilot-notes/000035-scala-2021-01.md:4:nine blocked. With outside data, counted apart: two reproduced, one
docs/pilot-notes/000035-scala-2021-01.md:40:2. No category covers an outside input that is public but slow to fetch; it
docs/pilot-notes/000035-scala-2021-01.md:42:3. Whether a link claim is needed when outside data is matched by label,
# Claims for Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social
# brain from age three to twelve years", Nature Communications 9, 1027,
# doi:10.1038/s41467-018-03399-2, on OpenNeuro dataset ds000228 ("MRI data of 3-12 year old children
# and adults during viewing of a short animated film"), snapshot 1.1.1
# (doi:10.18112/openneuro.ds000228.v1.1.1).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record (Nature Communications, open access, CC BY 4.0) as supplied
# under paper/ (text extracted from the PDF), with the main text, figure legends, Methods and the
# Supplementary Information (Supplementary Figures 1 to 8, Tables 1 to 4, Note 1). The four
# supplementary tables are images in the supplement PDF and are missing from the text; they were
# read from the PDF (pages 10 to 13), and their numbers are used below. The Peer Review File was
# not supplied and is not needed.
# Code: none linked. Code availability says the analysis code "is available from the
# corresponding author upon request", so no repository was read and no open detail is settled by
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A15 'ds000228' targets/dandisets.json | head -50; sed -n 1,12p docs/pilot-notes/000035-scala-2021-01.md; wc -l transcripts/openneuro-ds000228/*-report.md
```

```
# 000035, Scala et al. 2021 (2026-10-14): first attempt under pilot-5

Outcome, on the dandiset alone: three claims reproduced, one partially and
nine blocked. With outside data, counted apart: two reproduced, one
partially and one blocked. No outcome changed through either round. See
[`attempts/000035-scala-2021-01.yaml`](../../attempts/000035-scala-2021-01.yaml)
and [`transcripts/000035/`](../../transcripts/000035).

## What the attempt showed about the dandiset

The dandiset holds only the paper's 185-cell follow-up at 34 °C. The main
data set, about 1,300 neurons with their transcriptomes, is in dandiset
    6 transcripts/openneuro-ds000228/answer-report.md
   11 transcripts/openneuro-ds000228/author-answers-report.md
   51 transcripts/openneuro-ds000228/author-report.md
   28 transcripts/openneuro-ds000228/author-revise-1-report.md
   23 transcripts/openneuro-ds000228/author-revise-2-report.md
   24 transcripts/openneuro-ds000228/claims-check-report.md
   33 transcripts/openneuro-ds000228/claims-report.md
   76 transcripts/openneuro-ds000228/verifier-1-report.md
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls targets; grep -rln "ds000228" targets; grep -n "ds004752" -A12 targets/*.json | head -30
```

```
crcns.json
dandisets.json
description_papers.yaml
dryad.json
ebrains.json
figshare.json
openneuro.json
pilot.yaml
targets/openneuro.json
targets/openneuro.json:170:   "id": "ds004752",
targets/openneuro.json-171-   "name": "Dataset of intracranial EEG, scalp EEG and beamforming sources from epilepsy patients performing a verbal working memory task",
targets/openneuro.json:172:   "url": "https://openneuro.org/datasets/ds004752/versions/1.0.1",
targets/openneuro.json:173:   "doi": "10.18112/openneuro.ds004752.v1.0.1",
targets/openneuro.json-174-   "published_version": "1.0.1",
targets/openneuro.json-175-   "git_commit": "234fd4c04dea66ab9b0fd5ddbf4ec51f56b6ad02",
targets/openneuro.json-176-   "versions": 2,
targets/openneuro.json-177-   "latest": true,
targets/openneuro.json-178-   "published": "2023-09-20",
targets/openneuro.json-179-   "license": "CC0",
targets/openneuro.json-180-   "bids_version": "1.4.0",
[... 5 more lines not kept]
```

**Agent**

The dataset's entry is in `targets/openneuro.json`, not `targets/dandisets.json`, so I'm using that one.

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/openneuro.json'))
items=d if isinstance(d,list) else next(v for v in d.values() if isinstance(v,list))
for x in items:
  if x.get('id')=='ds000228': print(json.dumps(x,indent=1))
"; cd transcripts/openneuro-ds000228; for f in author-report.md claims-report.md claims-check-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (40.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/b4xun23ts.txt

Preview (first 2KB):
{
 "id": "ds000228",
 "name": "MRI data of 3-12 year old children and adults during viewing of a short animated film",
 "url": "https://openneuro.org/datasets/ds000228/versions/1.1.1",
 "doi": "10.18112/openneuro.ds000228.v1.1.1",
 "published_version": "1.1.1",
 "git_commit": "11410ae3a012249a68093471c6c95aa6f4d2da41",
 "versions": 4,
 "latest": true,
 "published": "2023-09-27",
 "license": "CC0",
 "bids_version": "1.0.1",
 "modalities": [
  "mri"
 ],
 "subjects": 155,
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "catalystneuro\|\"papers\"\|\"version_choice\|latest_version" /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/b4xun23ts.txt | head; grep -n "^=== " /home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/b4xun23ts.txt
```

```
155: "papers": [
166: "catalystneuro": []
168:=== author-report.md
220:=== claims-report.md
254:=== claims-check-report.md
279:=== answer-report.md
286:=== author-answers-report.md
298:=== verifier-1-report.md
375:=== author-revise-1-report.md
404:=== verifier-2-report.md
470:=== author-revise-2-report.md
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4c8e81c8-4f94-4270-91ef-ce4df75b06f2/tool-results/b4xun23ts.txt",
 "offset": 150
}
```

```
150	 ],
151	 "readme": true,
152	 "species": [],
153	 "approaches": [],
154	 "keywords": [],
155	 "papers": [
156	  {
157	   "doi": "10.1038/s41467-018-03399-2",
158	   "title": "Development of the social brain from age three to twelve years",
159	   "relation": "metadata",
160	   "resource_type": "JournalArticle",
161	   "preprint": false,
162	   "pmid": "29531321",
163	   "pmcid": "PMC5847587"
164	  }
165	 ],
166	 "catalystneuro": []
167	}
168	=== author-report.md
169	The attempt is written and its checks pass. Of 42 claims, 15 are reproduced, 12 partially reproduced, 13 not reproduced and 2 blocked. `entry.py check` reports 0 errors, the notebook ran clean in 147 s (`entry.py all`: pass), its outputs match my development run line for line, and the handover is built in `executed/openneuro-ds000228-richardson-2018/handover/`. Nothing is committed.
[... 325 more lines not kept]
```

**Agent**

I have everything I need. Writing the note now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md",
 "content": "# openneuro-ds000228, Richardson et al. 2018\n\nFifteen claims reproduced, eight partially, twelve not reproduced and none\nblocked on the dataset alone. With outside data, counted apart: one\nreproduced, one partially, three not reproduced and one blocked;\n`replication-sample`, on data deposited nowhere, is left out of the counts\nand blocked as `other`. It pins snapshot 1.1.1, its latest, whose CHANGES\nfile says it only updated the citation. The paper, Richardson, Lisandrelli,\nRiobueno-Naylor and Saxe in Nature Communications, scans 122 children aged\n3.5 to 12 years and 33 adults during one viewing of Pixar's \"Partly Cloudy\"\nand reports that the theory of mind (ToM) and pain networks are distinct from\nage 3, that their within-network correlations rise and their across-network\nanti-correlation grows with age, with events found by reverse correlation,\na functional maturity measure and the children's false-belief performance.\nThe claims were written from the version of record with its supplement,\nwhose four tables are images and were read from the PDF; the analysis code\nis available only on request, so no code was read. A first claims run\nstopped because the supplement was missing. The behaviour, motion,\ninter-region correlations, reverse-correlation events, functional maturity\nand the face-network controls were tested. The independent sample of 20\nadults is not deposited, and the hand-coded events of Jacoby et al. 2016\nexist only in an unpinned Saxe lab script (movloc.zip), so `hand-coded-events`\nis blocked as `other`. The four claims on the face and scene parcels count as\noutside data in the claims file, but the parcels were taken from the dataset,\nwhich holds them. The author's first run gave 15 reproduced, 12 partially, 13\nnot reproduced and 2 blocked. The author asked a reader no questions, so the\nanswer run and the following author run changed nothing. In round 1 the\nsummary cell was not removed by the handover, and the verifier read it after\nforming most of its outcomes. Round 1 agreed with 39 of 42 outcomes, and the\nauthor took its outcomes for `irc-williams`, `rc-child-adult-timecourse` and\n`maturity-across` (each from partially reproduced to not reproduced); its\npoints led to the adult and 3-year-old mean matrices, the ROI centroids (the\nmasks are in MNI mm), the image scaling (int16, no scaling), diagnostic\npipeline variants, a stated rule for absence claims that change outcome\nbetween readings, 159-TR timecourses for reading (b) of `rc-overlap`, and a\ncheck of the replicated events the README lists. Round 2 agreed with 41 of 42,\ndisagreeing on `rc-overlap`, which it judged not reproduced as its criterion\nhas no partial clause; the author kept partially reproduced, as the claim's\ntest holds and only its expected count (0 overlapping timepoints against 1)\nmisses. It found statements the outputs did not support, among them a summary\nsaying every behavioural number is recovered exactly, a within-ToM t of -6.23\ncalled out of tolerance, and an offset stated for all groups that holds for\nadults, which were corrected. Nothing was proposed, so there was no third\nround. Some outcomes rest on weak ground: `irc-tom-behavior-age` and\n`irc-fb-across` are not reproduced under the assumed O2a and O3a readings and\nwould be reproduced under O3b; `maturity-within` is reproduced and would not\nbe under O2b with O3b; `rc-fb-no-difference` is reproduced under O7a, while\nunder O7b T05 has p = .0497; `rc-3yo-events` is partially reproduced under\nO6b and not reproduced under O6a, and uses the best-matching rc-events\nreading (O5a), an extension of the criterion; and `beh-fb-tom` holds under\nreading (a) only. The author's run took about 32 minutes (16:10 to 16:42 UTC)\nand nothing failed; the notebook ran in 147 s at first, and the entry's README\ngives 146 s and 183 s for the last runs.\n\nWith the paper's own deposited preprocessed images, artifact and CompCor\nregressors and ROI masks, and the pipeline of the Methods, the inter-region\ncorrelations differ from the paper's: in adults .604, .398 and -.051 against\n.48, .35 and -.17, while in the 3-year-olds within-ToM is higher (.326 against\n.21) and within-Pain lower (.179 against .23; non-bilateral Pain .146 against\n.17). No variant within the described method closes the gap; only a shared\nToM and Pain signal added as a regressor, outside the paper's method, moves\nthe across value past the paper's, and it takes both within-network values\nto .286 and .258. Several downstream results, the within-ToM difference\nbetween false-belief passers and failers, the age effects at event peaks and\nthe T04 effect of ToM score, do not come out as reported, so either the\ndeposited data or the described pipeline differs from what produced the\npaper's numbers. The behavioural counts match exactly from participants.tsv,\nand FB_Group is also filled for 57 children aged 6 and over (54 pass, 3 inc),\nwhich the paper does not use. participants.tsv lists 2 seven-year-olds and 21\n8-12-year-olds with 3.13 mm voxels and no slice gap, where the Methods say 3\nand 20; the voxel-size column is misspelled \"Voxel slize\", and the no-gap\nlevel is stored as an empty value where participants.json defines \"None\". 19\nparticipants have face-ROI voxels without data at some timepoint, where\nSupplementary Fig. 4 counts 17 with incomplete ventral coverage, so the\ncoverage criterion may differ. The independent sample of 20 adults that\ndefined the ToM and pain ROIs is not deposited anywhere, though the ROIs it\nproduced are in the dataset, and the README's list of replicated events\noverlaps all Supplementary Table 3 events except P08, P09 and P11. Two\nquestions are put to the paper's authors: which timepoints entered the\ninter-region correlations and whether each artifact timepoint had its own\nregressor; and over which timepoints each ROI timecourse was z-normalized\nbefore the reverse correlation, whether child event magnitudes came from the\nz-normalized timecourse, and at what alpha the reverse-correlation t-tests\nwere run. The high-pass filter implementation is also not stated.\n\nThe author's points on the protocol: `replication-sample` is public nowhere,\nbut the checker rejects `data_missing` for an `elsewhere` claim, so `other`\nwas used; no block reason fits an input that is public but cannot be pinned,\nas for the hand coding; the claims file treats the face and scene parcels as\noutside input though the dataset holds them; Rule S counts a test that misses\nthe paper's p bound as failed even when the effect is significant in the same\ndirection, which made three claims not reproduced; some criteria, as for\nirc-williams and face-rc, define only the reproduced outcome; the data-check\nrule assumes trial tables, which this movie study lacks, so timing was checked\non the ROI signal at artifact timepoints and by shifting the event labels;\nabsence claims whose outcome changes between readings fall between the rule\nthat absence is judged on the paper's test and Author step 1.6, which was\nfollowed; and the repository root has untracked dotfiles from the sandbox.\n"
}
```

```
File created successfully at: docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n "—\|rather" docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md
```

```
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
?? docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md` and changed no other file. Nothing is committed.

The task said to take the dataset's entry from `targets/dandisets.json`, but ds000228 isn't in that file. It's in `targets/openneuro.json`, so I used that entry; its `catalystneuro` field is empty. The other untracked files at the repository root (dotfiles, `.idea`, `scripts` and others) were already there before I started; the author's report mentions them too.

# openneuro-ds000228, Richardson et al. 2018

Fifteen claims reproduced, eight partially, twelve not reproduced and none
blocked on the dataset alone. With outside data, counted apart: one
reproduced, one partially, three not reproduced and one blocked;
`replication-sample`, on data deposited nowhere, is left out of the counts
and blocked as `other`. It pins snapshot 1.1.1, its latest, whose CHANGES
file says it only updated the citation. The paper, Richardson, Lisandrelli,
Riobueno-Naylor and Saxe in Nature Communications, scans 122 children aged
3.5 to 12 years and 33 adults during one viewing of Pixar's "Partly Cloudy"
and reports that the theory of mind (ToM) and pain networks are distinct from
age 3, that their within-network correlations rise and their across-network
anti-correlation grows with age, with events found by reverse correlation,
a functional maturity measure and the children's false-belief performance.
The claims were written from the version of record with its supplement,
whose four tables are images and were read from the PDF; the analysis code
is available only on request, so no code was read. A first claims run
stopped because the supplement was missing. The behaviour, motion,
inter-region correlations, reverse-correlation events, functional maturity
and the face-network controls were tested. The independent sample of 20
adults is not deposited, and the hand-coded events of Jacoby et al. 2016
exist only in an unpinned Saxe lab script (movloc.zip), so `hand-coded-events`
is blocked as `other`. The four claims on the face and scene parcels count as
outside data in the claims file, but the parcels were taken from the dataset,
which holds them. The author's first run gave 15 reproduced, 12 partially, 13
not reproduced and 2 blocked. The author asked a reader no questions, so the
answer run and the following author run changed nothing. In round 1 the
summary cell was not removed by the handover, and the verifier read it after
forming most of its outcomes. Round 1 agreed with 39 of 42 outcomes, and the
author took its outcomes for `irc-williams`, `rc-child-adult-timecourse` and
`maturity-across` (each from partially reproduced to not reproduced); its
points led to the adult and 3-year-old mean matrices, the ROI centroids (the
masks are in MNI mm), the image scaling (int16, no scaling), diagnostic
pipeline variants, a stated rule for absence claims that change outcome
between readings, 159-TR timecourses for reading (b) of `rc-overlap`, and a
check of the replicated events the README lists. Round 2 agreed with 41 of 42,
disagreeing on `rc-overlap`, which it judged not reproduced as its criterion
has no partial clause; the author kept partially reproduced, as the claim's
test holds and only its expected count (0 overlapping timepoints against 1)
misses. It found statements the outputs did not support, among them a summary
saying every behavioural number is recovered exactly, a within-ToM t of -6.23
called out of tolerance, and an offset stated for all groups that holds for
adults, which were corrected. Nothing was proposed, so there was no third
round. Some outcomes rest on weak ground: `irc-tom-behavior-age` and
`irc-fb-across` are not reproduced under the assumed O2a and O3a readings and
would be reproduced under O3b; `maturity-within` is reproduced and would not
be under O2b with O3b; `rc-fb-no-difference` is reproduced under O7a, while
under O7b T05 has p = .0497; `rc-3yo-events` is partially reproduced under
O6b and not reproduced under O6a, and uses the best-matching rc-events
reading (O5a), an extension of the criterion; and `beh-fb-tom` holds under
reading (a) only. The author's run took about 32 minutes (16:10 to 16:42 UTC)
and nothing failed; the notebook ran in 147 s at first, and the entry's README
gives 146 s and 183 s for the last runs.

With the paper's own deposited preprocessed images, artifact and CompCor
regressors and ROI masks, and the pipeline of the Methods, the inter-region
correlations differ from the paper's: in adults .604, .398 and -.051 against
.48, .35 and -.17, while in the 3-year-olds within-ToM is higher (.326 against
.21) and within-Pain lower (.179 against .23; non-bilateral Pain .146 against
.17). No variant within the described method closes the gap; only a shared
ToM and Pain signal added as a regressor, outside the paper's method, moves
the across value past the paper's, and it takes both within-network values
to .286 and .258. Several downstream results, the within-ToM difference
between false-belief passers and failers, the age effects at event peaks and
the T04 effect of ToM score, do not come out as reported, so either the
deposited data or the described pipeline differs from what produced the
paper's numbers. The behavioural counts match exactly from participants.tsv,
and FB_Group is also filled for 57 children aged 6 and over (54 pass, 3 inc),
which the paper does not use. participants.tsv lists 2 seven-year-olds and 21
8-12-year-olds with 3.13 mm voxels and no slice gap, where the Methods say 3
and 20; the voxel-size column is misspelled "Voxel slize", and the no-gap
level is stored as an empty value where participants.json defines "None". 19
participants have face-ROI voxels without data at some timepoint, where
Supplementary Fig. 4 counts 17 with incomplete ventral coverage, so the
coverage criterion may differ. The independent sample of 20 adults that
defined the ToM and pain ROIs is not deposited anywhere, though the ROIs it
produced are in the dataset, and the README's list of replicated events
overlaps all Supplementary Table 3 events except P08, P09 and P11. Two
questions are put to the paper's authors: which timepoints entered the
inter-region correlations and whether each artifact timepoint had its own
regressor; and over which timepoints each ROI timecourse was z-normalized
before the reverse correlation, whether child event magnitudes came from the
z-normalized timecourse, and at what alpha the reverse-correlation t-tests
were run. The high-pass filter implementation is also not stated.

The author's points on the protocol: `replication-sample` is public nowhere,
but the checker rejects `data_missing` for an `elsewhere` claim, so `other`
was used; no block reason fits an input that is public but cannot be pinned,
as for the hand coding; the claims file treats the face and scene parcels as
outside input though the dataset holds them; Rule S counts a test that misses
the paper's p bound as failed even when the effect is significant in the same
direction, which made three claims not reproduced; some criteria, as for
irc-williams and face-rc, define only the reproduced outcome; the data-check
rule assumes trial tables, which this movie study lacks, so timing was checked
on the ROI signal at artifact timepoints and by shifting the event labels;
absence claims whose outcome changes between readings fall between the rule
that absence is judged on the paper's test and Author step 1.6, which was
followed; and the repository root has untracked dotfiles from the sandbox.

## End of run

14 turns, 2 minutes, result: success.
