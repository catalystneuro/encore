# 000678 · recorder · run 41213169377

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/000678/ claims/000678/; python tools/readme_row.py 000678; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '000678' in json.dumps(x)];print(json.dumps(e,indent=1)[:3000])"
```

```
docs/pilot-notes/000686-pakhomov-2023-01.md
docs/pilot-notes/000630-chartrand-2023-01.md
docs/pilot-notes/000637-gao-2025-01.md
docs/pilot-notes/000633-kim-2023-01.md
docs/pilot-notes/000579-tseng-2022-01.md
claims/000678/:
10.1016-j.celrep.2024.113709.yaml

transcripts/000678/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('targets/dandisets.json'));
import sys
def walk(x):
  if isinstance(x,dict):
    if x.get('dandiset')=='000678': print(json.dumps(x,indent=1))
    for v in x.values(): walk(v)
  elif isinstance(x,list):
    for v in x: walk(v)
walk(d)"; grep -n "^| Dandiset\|^|---" README.md | head; cat attempts/000678-hulsey-2024-01.yaml; for f in docs/pilot-notes/000686-pakhomov-2023-01.md docs/pilot-notes/000630-chartrand-2023-01.md docs/pilot-notes/000637-gao-2025-01.md docs/pilot-notes/000633-kim-2023-01.md docs/pilot-notes/000579-tseng-2022-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (84.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9fef6908-721d-428c-8452-fe96f129e9c0/tool-results/bppwohx3n.txt

Preview (first 2KB):
{
 "dandiset": "000678",
 "name": "Pupil and movement measurements during mouse auditory and visual discrimination",
 "published_version": "0.261020.0029",
 "asset_count": 391,
 "size_gb": 8.11,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [],
 "papers": [
  {
   "doi": "10.1101/2023.03.02.530651v2",
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Dandiset" README.md | head -3; cat attempts/000678-hulsey-2024-01.yaml
```

```
<persisted-output>
Output too large (43.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9fef6908-721d-428c-8452-fe96f129e9c0/tool-results/bkx8rg8fb.txt

Preview (first 2KB):
schema_version: 2
id: 000678-hulsey-2024-01
dataset:
  archive: dandi
  id: "000678"
  version: 0.231004.2146
  doi: 10.48324/dandi.000678/0.231004.2146
paper: doi:10.1016/j.celrep.2024.113709
date: 2026-10-31
entry: 000678-hulsey-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in docs/pilot-notes/000686-pakhomov-2023-01.md docs/pilot-notes/000630-chartrand-2023-01.md docs/pilot-notes/000637-gao-2025-01.md docs/pilot-notes/000633-kim-2023-01.md docs/pilot-notes/000579-tseng-2022-01.md docs/pilot-notes/001754-knierim-2000-02.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9fef6908-721d-428c-8452-fe96f129e9c0/tool-results/bg2z1el7n.txt

Preview (first 2KB):
=== docs/pilot-notes/000686-pakhomov-2023-01.md
# 000686, Pakhomov et al. 2023

No claims reproduced, none partially, four not reproduced and 16 blocked. The
first verification round agreed with 17 of the 20 outcomes and the second with
all 20, and a third round, held on the one change of outcome proposed after
the second, agreed with it. It pins version 0.240515.1909, the only published
version; the paper cites none. The paper, Pakhomov, Gudvangen, Mangalanathan,
Kondratiev, Redondo and Semenov in Bioelectrochemistry, focuses
electroporation of CHO-K1 cells to the centre of a quadrupole array of four
1.5-mm needles (CANCAN) by the interference of packets of 600-ns unipolar
pulses, measured by YO-PRO-1 (YP) uptake, with a Sim4Life field simulation
(Fig. 3), single cells imaged by confocal time-lapse (Fig. 4) and stitched
images of cell monolayers (Figs. 5 to 9). The claims were written from the
accepted author manuscript in PubMed Central (PMC10247516), with no supplement,
and the paper links no code. Only the four Fig. 5 claims could be tested, on
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9fef6908-721d-428c-8452-fe96f129e9c0/tool-results/bg2z1el7n.txt"
}
```

```
1	=== docs/pilot-notes/000686-pakhomov-2023-01.md
2	# 000686, Pakhomov et al. 2023
3	
4	No claims reproduced, none partially, four not reproduced and 16 blocked. The
5	first verification round agreed with 17 of the 20 outcomes and the second with
6	all 20, and a third round, held on the one change of outcome proposed after
7	the second, agreed with it. It pins version 0.240515.1909, the only published
8	version; the paper cites none. The paper, Pakhomov, Gudvangen, Mangalanathan,
9	Kondratiev, Redondo and Semenov in Bioelectrochemistry, focuses
10	electroporation of CHO-K1 cells to the centre of a quadrupole array of four
11	1.5-mm needles (CANCAN) by the interference of packets of 600-ns unipolar
12	pulses, measured by YO-PRO-1 (YP) uptake, with a Sim4Life field simulation
13	(Fig. 3), single cells imaged by confocal time-lapse (Fig. 4) and stitched
14	images of cell monolayers (Figs. 5 to 9). The claims were written from the
15	accepted author manuscript in PubMed Central (PMC10247516), with no supplement,
16	and the paper links no code. Only the four Fig. 5 claims could be tested, on
17	profiles measured anew from the 18 images, as no ROI measurements are
18	deposited; the Fig. 3 claim and the four Fig. 4 claims are blocked as
19	`data_missing`, and so are the eleven Fig. 6 to 9 claims, as their conditions
20	are not in 000686, though they appear to be in DANDI:000875, 001025, 001027
[... 564 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/9fef6908-721d-428c-8452-fe96f129e9c0/tool-results/bkx8rg8fb.txt"
}
```

```
1	schema_version: 2
2	id: 000678-hulsey-2024-01
3	dataset:
4	  archive: dandi
5	  id: "000678"
6	  version: 0.231004.2146
7	  doi: 10.48324/dandi.000678/0.231004.2146
8	paper: doi:10.1016/j.celrep.2024.113709
9	date: 2026-10-31
10	entry: 000678-hulsey-2024
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
[... 790 more lines not kept]
```

**Agent**

I have the attempt record and the five recent notes. Next I'm reading the run reports and the claims file.

**Agent calls Bash**

```bash
cd transcripts/000678; wc -w *-report.md; ls -l --time-style=full-iso *.md | awk '{print $7, $9}'; cat author-report.md
```

```
148 answer-report.md
  465 author-answers-report.md
  830 author-report.md
  628 author-revise-1-report.md
  428 author-revise-2-report.md
  589 claims-check-report.md
  755 claims-report.md
 1607 verifier-1-report.md
  977 verifier-2-report.md
 6427 total
15:05:56.176914532 answer-report.md
15:05:56.177608938 answer.md
15:05:56.177608938 author-answers-report.md
15:05:56.177608938 author-answers.md
15:05:56.177608938 author-report.md
15:05:56.177608938 author-revise-1-report.md
15:05:56.177608938 author-revise-1.md
15:05:56.177608938 author-revise-2-report.md
15:05:56.177608938 author-revise-2.md
15:05:56.179608957 author.md
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000678; for f in answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== answer-report.md
There are no questions to answer for 000678, so I changed nothing.

- **No questions file:** `questions/000678.yaml` doesn't exist on this branch, and it isn't on `origin/attempt/000678` either, which is still at the same commit (b0031446a). Git history has no record of it ever being created.
- **The author asked none:** the latest run was the author's, and `transcripts/000678/author-report.md:41` says "I asked no reader questions."
- **The one open question isn't for a reader:** the author recorded it as a `methods_unavailable` finding addressed to the paper's authors (`attempts/000678-hulsey-2024-01.yaml:370`). It asks how `Figure2.py` types a state that has no confident trials, and which 381 sessions were analysed. That doesn't say the claims file misreads the paper.

I didn't edit `claims/000678/`, create `questions/000678.yaml`, or run `tools/claims_check.py`, because no claim changed. If questions are expected, they may not have been committed yet; once the file exists, this step can run again.
=== author-answers-report.md
There were no questions, so no claim, notebook or record changed. `questions/000678.yaml` does not exist on this branch, and the claims file (`claims/000678/`) has not changed since the first author run. That run asked no reader questions. Its one open question, about how `Figure2.py` types a state with no confident trials and which 381 sessions were analysed, is for the paper's authors. It is recorded as a `methods_unavailable` finding in the attempt record. The answer run before this one also found nothing to answer and changed nothing.

I didn't edit the notebook, `hulsey.py`, the README or `attempts/000678-hulsey-2024-01.yaml`, because nothing was answered to update them for.

What I ran:
- **Lock:** `python tools/entry.py lock entries/000678-hulsey-2024` rewrote the lock file with no change.
- **Check and run:** `python tools/entry.py all entries/000678-hulsey-2024` gave 0 errors, and the notebook passed in 581 s (a
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/000678/*.yaml; grep -n "^  - id:\|^- id:\|data:\|source\|pmc\|PMC\|code" claims/000678/*.yaml | head -60
```

```
# Claims for Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024), "Decision-making dynamics
# are predicted by arousal and uninstructed movements", Cell Reports 43(1), 113709, on dandiset
# 000678.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript of the version of record in PubMed Central
# (PMC11016285, NIHMS1970871), as served by ncbi_pmc, full text with Results, Discussion, STAR
# Methods and figure legends, and its supplement (NIHMS1970871-supplement-1.pdf, the legends of
# Figures S1 to S8, read as extracted text). The bioRxiv preprint (10.1101/2023.03.02.530651 v2)
# is also under paper/ and was not used for claims. The main-text PDF is not under paper/, so the
# main figures were not seen; where a significance mark appears only in a figure, it is taken from
# the figure code below, which draws it.
#
# Code read: the analysis code the paper links, Zenodo doi:10.5281/zenodo.10306018
# (hulsey2023.zip, folders hulsey2023_analysis, a minimal uobrainflex and the fork of ssm with
# categorical emissions). The hulsey2023 scripts are also in github.com/sjara/uobrainflex at
# commit ef48985192e4af332c64f9d2e70ddcfc78659040 (folder hulsey2023/), except FigureS7.py and
# FigureS8.py, which are only in the Zenodo archive. The scripts are
[... 100 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000678-hulsey-2024-01.md",
 "content": "# 000678, Hulsey et al. 2024\n\nTwenty-one claims reproduced, six partially, one not reproduced and one\nblocked. The first verification round agreed with all 29 outcomes and the\nsecond with all 29, so there was no third round. It pins version\n0.231004.2146, the version the paper cites; the later 0.261020.0029 has the\nsame assets and differs only in archive metadata. The paper, Hulsey, Zumwalt,\nMazzucato, McCormick and Jaramillo in Cell Reports, fits a GLM-HMM to the\nchoices of each of 13 head-fixed mice on an auditory (8) or visual (5)\ndiscrimination task, types the states as optimal, disengaged and sub-optimal,\nrelates them to pupil diameter, face motion energy and locomotion speed, and\nclassifies the states from these measures with decoders. The claims were\nwritten from the accepted author manuscript in PubMed Central (PMC11016285)\nand its supplement, without the main-text PDF, and from the paper's code on\nZenodo (doi:10.5281/zenodo.10306018) and in uobrainflex at commit ef48985.\nThe model of the paper's ssm fork was reimplemented with the same priors, EM\nupdates and stopping rule. 28 claims were tested; `training-duration` is\nblocked as `data_missing`, as every session is stage 5 or 6. `cohort-inclusion`\nis partial, the 13 mice matching but 376 sessions passing the criteria against\nthe paper's 381, and every later analysis uses those 376.\n`fig5c-movement-index-best` is not reproduced: the movement index decodes the\nstates at 68.6% against 71.5% for pupil (p = 0.086), and the code's conditions\nthat favour it keep pupil information, so they do not test the claim.\n`fig2a-state-types` reproduces on an assumption, one state of BW059 with no\ntrial of posterior 0.8 or more in the sessions with the optimal state being\ntyped on all sessions, where Figure2.py would score it against every template\nas 0 and mislabel the optimal state. `fig2c-dwell-times`,\n`figs4-r2-individual-movement`, `fig3-distance-from-optimal-pupil`,\n`fig4a-lower-variability` and `fig4b-variability-at-transitions` are partial,\ntheir tests holding but some values outside tolerance or some tests failing\n(the optimal dwell is 43.8 trials against 37, and the distances from the\noptimal pupil are 8.8, 16.0 and 11.8% against 7, 12.6 and 9). The author's\nfirst run used 3 cross-validation initialisations in place of 10 and fixed\nvisual stimulus values of 1, 0.8 and 0.6 to fit the 30-minute limit and gave\n`fig2b-optimal-occupancy` and `fig3f-movement-index-inverted-u` as partial.\nThe author asked a reader no questions, so the answer run and the following\nauthor run changed nothing. Round 1 agreed with all outcomes but found that 2\nof 3 random starts of the EM ended in a worse local optimum on synthetic data,\nthat the movement-index variants keep pupil information, that the stationary\nrule counted backward running, that the template matching of other states\ncannot fail, that the dwell code adds zero-length epochs, that pupil r2 rests\non one split with an outlier (BW051), and that the visual stimulus values\ncould come from the `visual_gabor_angle` column. In reply every state model\nwas re-fit with 10 initialisations and the stimulus values of\n`get_stim_vals`, which moved fig2b (indeterminate share 13.1% +/- 1.6%) and\nfig3f (r2 0.574 against the 0.57 bound) to reproduced, and variants were added\nfor the other points; the notebook then took 1550 s, close to the limit. Round\n2 agreed with all 29, calling fig3f marginal, and found sentences the outputs\ndid not support, which were corrected; three of its mismatches (1,879 against\n1,821 stationary trials, locomotion r2 0.570 against 0.567, p = 0.051 against\n0.053) came from its run on another machine, which the author ascribes, not\nconfirmed, to speeds rounding to zero in the smoothing filter (9,869 trials\nare below 1e-9 m/s but not exactly 0), and both values are now given. The\nauthor's run took about 1 h 40 min (09:19 to 11:00 UTC); a first version of\nthe model fitting diverged and was fixed with damped Newton steps before any\nreported fit. The notebook ran in 13 to 14 minutes at first, 581 s after the\nanswer, 1550 s after round 1 and 15.7 minutes in the last run.\n\nThe dandiset holds 391 stage 5 and 6 sessions of the 13 included mice, where\nthe paper analysed 381; the paper's inclusion criteria select 376 of them\ncounted from the reward series and 375 counted from the hits (14 fail both,\n13 with fewer than 100 rewards and 1 with less than 20% at one port, and 3\nfail one count only), and nothing in the dandiset marks which sessions the\npaper used. The training sessions before stage 5, the other stage 5 and 6\nsessions of the 500 the paper names, and the 18 mice that did not meet the\ninclusion criteria are not in the dandiset, so the training duration (21 +/- 8\nsessions) cannot be tested. The running_speed series of every file is\nlabelled cm/s, but its values (session medians around 0.07, 99th percentiles\nup to 0.67) are in m/s, the unit of the paper and of its code. In 38 of the 391\nsessions the post hoc pupil diameter series is present but entirely missing\nvalues (14 of BW046's 34 sessions). The rig names in the session metadata are\nspelled several ways for what appear to be the same rigs (Box 1, Box1,\nBoox1). No recording is deposited twice, and a response against no-response\ncontrast is consistent with the measures sharing the trial clock. A question\nis put to the paper's authors: how Figure2.py handled a state with no trial of\nposterior 0.8 or more in the sessions where the optimal state occurs, and\nwhich 381 sessions were analysed.\n\nThe author's points on the protocol: the paper's method does not fit the\n30-minute notebook limit in full (10 initialisations per fold and 1000 shuffle\nruns for the decoders), and the reductions to 3 initialisations and to 3 runs\nper shuffled condition with 20 null runs were recorded as deviations, not as\n`too_large`, as blocking would have blocked almost every claim resting on the\nstate fits; the paper's ssm fork is not a locked dependency, and the protocol\nsays nothing about reimplementing a method against installing the original,\nso the reimplementation was recorded as a deviation; the protocol does not say\nwhat to do when the data trigger a latent bug in the paper's code, and the fix\nwas treated as an assumption with a question to the authors; and there is no\nrule for a session set the dataset cannot reconstruct, so the paper's criteria\nwere used with a `selection_undocumented` finding.\n"
}
```

```
File created successfully at: docs/pilot-notes/000678-hulsey-2024-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='docs/pilot-notes/000678-hulsey-2024-01.md'
s=open(p).read()
a="""first run used 3 cross-validation initialisations in place of 10 and fixed
visual stimulus values of 1, 0.8 and 0.6 to fit the 30-minute limit and gave"""
b="""first run used 3 cross-validation initialisations in place of 10, to fit the
30-minute limit, and visual stimulus values of 1, 0.8 and 0.6 for every
session, and gave"""
c="""typed on all sessions, where Figure2.py would score it against every template
as 0 and mislabel the optimal state."""
d="""typed on all sessions, where Figure2.py's nansum would score it 0 against
every template and mislabel the optimal state."""
assert a in s and c in s
s=s.replace(a,b).replace(c,d)
open(p,'w').write(s)
EOF
grep -c "—\|rather" docs/pilot-notes/000678-hulsey-2024-01.md; git status --short
```

```
0
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
?? docs/pilot-notes/000678-hulsey-2024-01.md
?? scripts
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/000678-hulsey-2024-01.md"
}
```

```
1	# 000678, Hulsey et al. 2024
2	
3	Twenty-one claims reproduced, six partially, one not reproduced and one
4	blocked. The first verification round agreed with all 29 outcomes and the
5	second with all 29, so there was no third round. It pins version
6	0.231004.2146, the version the paper cites; the later 0.261020.0029 has the
7	same assets and differs only in archive metadata. The paper, Hulsey, Zumwalt,
8	Mazzucato, McCormick and Jaramillo in Cell Reports, fits a GLM-HMM to the
9	choices of each of 13 head-fixed mice on an auditory (8) or visual (5)
10	discrimination task, types the states as optimal, disengaged and sub-optimal,
11	relates them to pupil diameter, face motion energy and locomotion speed, and
12	classifies the states from these measures with decoders. The claims were
13	written from the accepted author manuscript in PubMed Central (PMC11016285)
14	and its supplement, without the main-text PDF, and from the paper's code on
15	Zenodo (doi:10.5281/zenodo.10306018) and in uobrainflex at commit ef48985.
16	The model of the paper's ssm fork was reimplemented with the same priors, EM
17	updates and stopping rule. 28 claims were tested; `training-duration` is
18	blocked as `data_missing`, as every session is stage 5 or 6. `cohort-inclusion`
19	is partial, the 13 mice matching but 376 sessions passing the criteria against
20	the paper's 381, and every later analysis uses those 376.
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='docs/pilot-notes/000678-hulsey-2024-01.md'
s=open(p).read()
reps=[("""30-minute limit, and visual stimulus values of 1, 0.8 and 0.6 for every
session, and gave
`fig2b-optimal-occupancy`""","""30-minute limit, and visual stimulus values of 1, 0.8 and 0.6 for every
session, and gave `fig2b-optimal-occupancy`"""),
("""0.053) came from its run on another machine, which the author ascribes, not
confirmed, to speeds rounding to zero in the smoothing filter (9,869 trials
are below 1e-9 m/s but not exactly 0), and both values are now given.""",
"""0.053) did not appear in the author's runs, and the author ascribes them,
without confirming it, to a run on another machine and speeds rounding to zero
in the smoothing filter (9,869 trials are below 1e-9 m/s but not exactly 0);
both values are now given."""),
("about 1 h 40 min (09:19","about 100 minutes (09:19")]
for a,b in reps:
    assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
EOF
git status --short docs
```

```
?? docs/pilot-notes/000678-hulsey-2024-01.md
```

**Agent**

I wrote `docs/pilot-notes/000678-hulsey-2024-01.md` and changed no other file. Some untracked files I did not create also show up in `git status` (`.bashrc`, `.profile`, `.idea`, `scripts` and others), and I left them alone. The verifier's round 2 report gives the counts as 19 reproduced and 8 partial, but the record and `readme_row.py` both give 21 and 6. The note uses the record's counts.

# 000678, Hulsey et al. 2024

Twenty-one claims reproduced, six partially, one not reproduced and one
blocked. The first verification round agreed with all 29 outcomes and the
second with all 29, so there was no third round. It pins version
0.231004.2146, the version the paper cites; the later 0.261020.0029 has the
same assets and differs only in archive metadata. The paper, Hulsey, Zumwalt,
Mazzucato, McCormick and Jaramillo in Cell Reports, fits a GLM-HMM to the
choices of each of 13 head-fixed mice on an auditory (8) or visual (5)
discrimination task, types the states as optimal, disengaged and sub-optimal,
relates them to pupil diameter, face motion energy and locomotion speed, and
classifies the states from these measures with decoders. The claims were
written from the accepted author manuscript in PubMed Central (PMC11016285)
and its supplement, without the main-text PDF, and from the paper's code on
Zenodo (doi:10.5281/zenodo.10306018) and in uobrainflex at commit ef48985.
The model of the paper's ssm fork was reimplemented with the same priors, EM
updates and stopping rule. 28 claims were tested; `training-duration` is
blocked as `data_missing`, as every session is stage 5 or 6. `cohort-inclusion`
is partial, the 13 mice matching but 376 sessions passing the criteria against
the paper's 381, and every later analysis uses those 376.
`fig5c-movement-index-best` is not reproduced: the movement index decodes the
states at 68.6% against 71.5% for pupil (p = 0.086), and the code's conditions
that favour it keep pupil information, so they do not test the claim.
`fig2a-state-types` reproduces on an assumption, one state of BW059 with no
trial of posterior 0.8 or more in the sessions with the optimal state being
typed on all sessions, where Figure2.py's nansum would score it 0 against
every template and mislabel the optimal state. `fig2c-dwell-times`,
`figs4-r2-individual-movement`, `fig3-distance-from-optimal-pupil`,
`fig4a-lower-variability` and `fig4b-variability-at-transitions` are partial,
their tests holding but some values outside tolerance or some tests failing
(the optimal dwell is 43.8 trials against 37, and the distances from the
optimal pupil are 8.8, 16.0 and 11.8% against 7, 12.6 and 9). The author's
first run used 3 cross-validation initialisations in place of 10, to fit the
30-minute limit, and visual stimulus values of 1, 0.8 and 0.6 for every
session, and gave `fig2b-optimal-occupancy` and `fig3f-movement-index-inverted-u` as partial.
The author asked a reader no questions, so the answer run and the following
author run changed nothing. Round 1 agreed with all outcomes but found that 2
of 3 random starts of the EM ended in a worse local optimum on synthetic data,
that the movement-index variants keep pupil information, that the stationary
rule counted backward running, that the template matching of other states
cannot fail, that the dwell code adds zero-length epochs, that pupil r2 rests
on one split with an outlier (BW051), and that the visual stimulus values
could come from the `visual_gabor_angle` column. In reply every state model
was re-fit with 10 initialisations and the stimulus values of
`get_stim_vals`, which moved fig2b (indeterminate share 13.1% +/- 1.6%) and
fig3f (r2 0.574 against the 0.57 bound) to reproduced, and variants were added
for the other points; the notebook then took 1550 s, close to the limit. Round
2 agreed with all 29, calling fig3f marginal, and found sentences the outputs
did not support, which were corrected; three of its mismatches (1,879 against
1,821 stationary trials, locomotion r2 0.570 against 0.567, p = 0.051 against
0.053) did not appear in the author's runs, and the author ascribes them,
without confirming it, to a run on another machine and speeds rounding to zero
in the smoothing filter (9,869 trials are below 1e-9 m/s but not exactly 0);
both values are now given. The author's run took about 100 minutes (09:19 to
11:00 UTC); a first version of the model fitting diverged and was fixed with
damped Newton steps before any reported fit. The notebook ran in 13 to 14
minutes at first, 581 s after the answer, 1550 s after round 1 and 15.7
minutes in the last run.

The dandiset holds 391 stage 5 and 6 sessions of the 13 included mice, where
the paper analysed 381; the paper's inclusion criteria select 376 of them
counted from the reward series and 375 counted from the hits (14 fail both,
13 with fewer than 100 rewards and 1 with less than 20% at one port, and 3
fail one count only), and nothing in the dandiset marks which sessions the
paper used. The training sessions before stage 5, the other stage 5 and 6
sessions of the 500 the paper names, and the 18 mice that did not meet the
inclusion criteria are not in the dandiset, so the training duration (21 +/- 8
sessions) cannot be tested. The running_speed series of every file is
labelled cm/s, but its values (session medians around 0.07, 99th percentiles
up to 0.67) are in m/s, the unit of the paper and of its code. In 38 of the 391
sessions the post hoc pupil diameter series is present but entirely missing
values (14 of BW046's 34 sessions). The rig names in the session metadata are
spelled several ways for what appear to be the same rigs (Box 1, Box1,
Boox1). No recording is deposited twice, and a response against no-response
contrast is consistent with the measures sharing the trial clock. A question
is put to the paper's authors: how Figure2.py handled a state with no trial of
posterior 0.8 or more in the sessions where the optimal state occurs, and
which 381 sessions were analysed.

The author's points on the protocol: the paper's method does not fit the
30-minute notebook limit in full (10 initialisations per fold and 1000 shuffle
runs for the decoders), and the reductions to 3 initialisations and to 3 runs
per shuffled condition with 20 null runs were recorded as deviations, not as
`too_large`, as blocking would have blocked almost every claim resting on the
state fits; the paper's ssm fork is not a locked dependency, and the protocol
says nothing about reimplementing a method against installing the original,
so the reimplementation was recorded as a deviation; the protocol does not say
what to do when the data trigger a latent bug in the paper's code, and the fix
was treated as an assumption with a question to the authors; and there is no
rule for a session set the dataset cannot reconstruct, so the paper's criteria
were used with a `selection_undocumented` finding.

## End of run

14 turns, 1 minutes, result: success.
