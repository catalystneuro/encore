# 000971 · recorder · run 39119921935

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000971 --write; git diff; ls transcripts/000971 claims/000971; grep -n '^### ' docs/pilot-notes.md | tail -6
```

```
diff --git a/README.md b/README.md
index 3cfb70c..8414da7 100644
--- a/README.md
+++ b/README.md
@@ -89,6 +89,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
 | [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
 | [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
+| [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000971:
10.1016-j.cub.2022.01.055.yaml

transcripts/000971:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 2587,3200p docs/pilot-notes.md; grep -n '^| Dandiset' -A1 README.md
```

```
<persisted-output>
Output too large (37.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/b72sbrgpy.txt

Preview (first 2KB):
### 000568, Valero et al. 2022

Four claims reproduced, six partially, six not reproduced and six blocked, all
on the dandiset. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with all 22 as they then stood, but
found that most light pulses are not in the files and that the place-field
rule differed from buzcode's; the revision restricted control time to windows
dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
11 cells between place and non-place and changed five outcomes:
`figs11-place-cell-fraction` to partially reproduced,
`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
reproduced, and `fig3g-spatial-information` and
`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
22 and disagreed on `fig3g-spatial-information`, whose larger increase for
unmasked fields (p = 0.039) does not hold against time-matched control maps,
where the increase is negative in both groups (p = 0.3); the author proposed
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/b72sbrgpy.txt"
}
```

```
1	### 000568, Valero et al. 2022
2	
3	Four claims reproduced, six partially, six not reproduced and six blocked, all
4	on the dandiset. Round 1 gave its own outcome for each claim from the notebook
5	with its conclusions removed and agreed with all 22 as they then stood, but
6	found that most light pulses are not in the files and that the place-field
7	rule differed from buzcode's; the revision restricted control time to windows
8	dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
9	11 cells between place and non-place and changed five outcomes:
10	`figs11-place-cell-fraction` to partially reproduced,
11	`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
12	reproduced, and `fig3g-spatial-information` and
13	`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
14	22 and disagreed on `fig3g-spatial-information`, whose larger increase for
15	unmasked fields (p = 0.039) does not hold against time-matched control maps,
16	where the increase is negative in both groups (p = 0.3); the author proposed
17	partially reproduced and a third round agreed. The paper reports pulsed
18	optogenetics with uLEDs in CA1 pyramidal neurons of four CaMKIIa-Cre::Ai32
19	mice: light-induced spiking falls during sharp-wave ripples, rises in the
20	place field and at the theta trough, unmasks place fields in non-place cells,
[... 527 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^| Dandiset' -A1 README.md; grep -n '001754' docs/pilot-notes.md | head
```

```
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50-|---|---|---|---|---|---|---|
747:001754, 000130 and 001616. The first pipeline run mixed results between
774:### 001754, Knierim, McNaughton and Poe 2000
863:### 001754 again, on the fixed draft (2026-10-15)
895:The earlier attempt's transcripts are now in `transcripts/001754/attempt-01/`,
```

**Agent calls Bash**

```bash
cat attempts/000971-seiler-2022-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
x=d if isinstance(d,list) else d.get('dandisets',d)
import sys
items = x if isinstance(x,list) else list(x.values())
for e in items:
  if '000971' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
"; wc -c transcripts/000971/*report.md claims/000971/*
```

```
<persisted-output>
Output too large (56.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/b82shz4i4.txt

Preview (first 2KB):
schema_version: 1
id: 000971-seiler-2022-01
dandiset: "000971"
dandiset_version: 0.261013.1707
paper: doi:10.1016/j.cub.2022.01.055
date: 2026-10-18
entry: 000971-seiler-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/b82shz4i4.txt"
}
```

```
1	schema_version: 1
2	id: 000971-seiler-2022-01
3	dandiset: "000971"
4	dandiset_version: 0.261013.1707
5	paper: doi:10.1016/j.cub.2022.01.055
6	date: 2026-10-18
7	entry: 000971-seiler-2022
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The authors' photometry analysis code (IndividualPhotometryAnalysis.m and helpers), read for the
18	    smoothing, the control fit, dF/F, the z-score, the removal of the first second, the 2 s burst rule
19	    for unrewarded nosepokes and the PSTH alignment, which the analysis follows.
20	  source: https://github.com/jillianseiler/Seiler-et-al.-2022-MATLAB-code at commit
[... 985 more lines not kept]
```

**Agent**

The README row reads 17 reproduced, 9 partially, 6 not reproduced, 5 blocked. Next I'm reading the reports, the claims file and the target entry.

**Agent calls Bash**

```bash
cd transcripts/000971; for f in author-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done; cd ../..; grep -n '000971' -A12 targets/dandisets.json | head -30
```

```
<persisted-output>
Output too large (30.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/bt8x7erqy.txt

Preview (first 2KB):
=== author-report.md
I finished steps 1 to 5 and ran the handover. The notebook passes `check` and runs from a clean environment in 760 s, which is over the 10-minute aim but under CI's 30-minute limit. Nothing is committed.

**Paper:** I used the full text of the author manuscript in PubMed Central (PMC8930615), saved under `paper/`. The supplement PDF was blocked by a browser check, so claims on Figures S1 to S7 rest on the main text only.

**Version:** pinned 0.261013.1707, the latest published version. The paper predates the dandiset and cites no version. All three published versions and the draft hold the same 4139 files (same blobs); they differ only in dandiset-level metadata. The notebook header says this.

### 1. Outcomes (38 claims)

| Outcome | Count | Claims |
|---|---|---|
| Reproduced | 18 + 1 on Zenodo data | fig1f, fig2b, fig2c, fig2d, fig2m, fig2n, figs1i, figs2b, fig3h, fig4f, fig4h, fig5h, fig5i, fig6h, fig6i, fig7g, fig7h, fig7i; the Zenodo one is figs3ab |
| Partially reproduced | 8 | fig1e, fig2a, fig2k, fig2l, fig2o, fig3g, figs5f, fig6g |
| Not reproduced | 7 | fig1d, fig3f, fig4g, fig5f, fig5g, fig6-nphr-learning-dropout, fig7f |
| Blocked, data missing | 4 | fig3e (RI30 photometry), figs1a (fear conditioning), figs3cd (open field), fig3c (histology) |

[... 7 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2fd078cf-f680-4d49-ab63-99d784f01091/tool-results/bt8x7erqy.txt"
}
```

```
1	=== author-report.md
2	I finished steps 1 to 5 and ran the handover. The notebook passes `check` and runs from a clean environment in 760 s, which is over the 10-minute aim but under CI's 30-minute limit. Nothing is committed.
3	
4	**Paper:** I used the full text of the author manuscript in PubMed Central (PMC8930615), saved under `paper/`. The supplement PDF was blocked by a browser check, so claims on Figures S1 to S7 rest on the main text only.
5	
6	**Version:** pinned 0.261013.1707, the latest published version. The paper predates the dandiset and cites no version. All three published versions and the draft hold the same 4139 files (same blobs); they differ only in dandiset-level metadata. The notebook header says this.
7	
8	### 1. Outcomes (38 claims)
9	
10	| Outcome | Count | Claims |
11	|---|---|---|
12	| Reproduced | 18 + 1 on Zenodo data | fig1f, fig2b, fig2c, fig2d, fig2m, fig2n, figs1i, figs2b, fig3h, fig4f, fig4h, fig5h, fig5i, fig6h, fig6i, fig7g, fig7h, fig7i; the Zenodo one is figs3ab |
13	| Partially reproduced | 8 | fig1e, fig2a, fig2k, fig2l, fig2o, fig3g, figs5f, fig6g |
14	| Not reproduced | 7 | fig1d, fig3f, fig4g, fig5f, fig5g, fig6-nphr-learning-dropout, fig7f |
15	| Blocked, data missing | 4 | fig3e (RI30 photometry), figs1a (fear conditioning), figs3cd (open field), fig3c (histology) |
16	
17	The main photometry results do not hold here. The DMS score is in the paper's order across phenotypes but not significant (p = 0.100). Its correlation with shocks is r = 0.17 pooled; only early sessions alone reach significance (r = 0.375, p = 0.045). The DLS score correlates with shocks (r = 0.326, p = 0.024), where the paper finds none. That last result depends on a dropout-masking step I added (item 3 below); without it r = 0.113.
18	
19	### 2. What the dandiset holds and lacks
20	
[... 233 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 3514,3540p targets/dandisets.json; head -60 claims/000971/*.yaml; grep -n 'data:\|uses:\|with_inputs\|outside' claims/000971/*.yaml | head -20
```

```
"behavioral approach",
    "optogenetic approach"
   ],
   "papers": [
    {
     "doi": "10.1016/j.cub.2022.01.055",
     "title": "Dopamine signaling in the dorsomedial striatum promotes compulsive behavior",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/lerner-lab-to-nwb",
    "contributor Adkisson-Floro, Paul of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000981",
   "name": "Whole-brain chemosensory responses of both C. elegans sexes",
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 '^  statement:' claims/000971/*.yaml | grep -v criterion | head -150
```

```
45:  statement: Mice trained on RI60 accept more shocks in the shock probes than mice trained on RR20
46-    (main effect of schedule, F1,43 = 6.37, p < 0.05; schedule by time interaction, F1,43 = 4.54,
47-    p < 0.05), and RI60 mice accept more shocks on the late probe than on the early one (p < 0.01).
48-  source: Results, first section; Figure 1D
--
55:  statement: RI60-trained mice take longer to complete the omission probe than RR20-trained mice
56-    (unpaired t-test, p < 0.05; n = 20 and 7).
57-  source: Results, first section; Figure 1E
--
62:  statement: Among RI60 mice, shocks received on the late probe and omission completion time are not
63-    significantly correlated (r = 0.42, ns).
64-  source: Results, first section; Figure 1F
--
68:  statement: RI60 mice are split by their shock probe counts into 9 punishment resistant (PR), 9
69-    delayed punishment resistant (DPR) and 18 punishment sensitive (PS) mice, by the rule in the
70-    Methods (DPR when the count rises by more than 85%; otherwise PR when the early count exceeds 13).
71-  source: Figure 2A; STAR Methods, Behavioral Analysis
--
87:  statement: There is an interaction of phenotype and probe on shocks received (p < 0.0001), and only
88-    DPR mice receive significantly more shocks on the late probe than the early one.
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 000971, Seiler et al. 2022

Seventeen claims reproduced, nine partially, six not reproduced and five
blocked on the dandiset. With outside data, counted apart: one reproduced.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with 37 of the 38; it would block
`fig6-nphr-learning-dropout`, as the dandiset holds 13 NpHR, 13 NpHR Scrambled
and 16 EYFP mice where Figure 6F counts 16, 15 and 16, so the mice the paper
dropped are, but for one, not deposited, and the author changed the claim from
not reproduced to blocked as `data_missing`. Round 1 also asked for the
training files with no rewards to be inspected; one is a 170 s false start of
mouse 140.306, without which Tukey PS vs DPR in `fig2n-rewards-per-session`
gives p = 0.059, and the author changed that claim from reproduced to
partially reproduced. Round 2 agreed with all 38 and nothing was proposed, so
there was no third round. The paper reports that RI60-trained mice accept more
shocks in shock probes than RR20-trained mice, that RI60 mice split into
punishment resistant (PR), delayed punishment resistant (DPR) and punishment
sensitive (PS) phenotypes, that a DMS dopamine axon score from fiber
photometry differs by phenotype and correlates with shocks while the DLS score
does not, and that stimulating DMS dopamine terminals on rewarded nosepokes
makes mice more likely to be PR and inhibiting them more likely to be PS,
while DLS stimulation has no such effect. The schedule comparisons, the
phenotype rule and the training and omission behaviour of the phenotypes, sex
differences, the DMS and DLS scores against phenotype, shocks and omission
time, and the DMS excitation, DMS inhibition and DLS excitation cohorts were
tested, and the DAT protein claim on the Zenodo densitometry table the
dandiset names. The RI30 photometry peaks, the inhibition dropouts, fear
conditioning, open field and histology are blocked as `data_missing`. Some
outcomes rest on weak ground: `fig4g-dls-score-shock-no-correlation` is not
reproduced (r = 0.326, p = 0.024) only with a dropout step the author added
after seeing per-session scores, which is in neither the Methods nor the
authors' code, and without it r = 0.113, p = 0.45; the same step takes the
phenotype p of `fig3f-dms-score-phenotype` from 0.389 to 0.100;
`fig3g-dms-score-shock-correlation` is partially reproduced on one of three
readings (r = 0.375, p = 0.045, n = 29), with p = 0.13 after correction for the
three; `fig2n-rewards-per-session` gives p = 0.048, 0.059 or 0.044 under three
session-exclusion rules, and the one used, set after round 1, is the only one
above 0.05; `fig5f-dms-chr2-escalation` and `fig7f-dls-escalation-similar`
rest on the pooled fit with no mouse term that the criterion fixed, and a mixed
model with a random slope per mouse would make fig5f partially reproduced but
warns of a boundary fit, while a model with a random intercept only puts ChR2
above neither control; and the claims on Figures S1 to S7 rest on the main
text alone. The author used the author manuscript in PubMed Central
(PMC8930615), whose supplement could not be downloaded, and took the
photometry processing from the authors' MATLAB code at commit 56f1529.

The dandiset was converted by CatalystNeuro (catalystneuro/lerner-lab-to-nwb).
The Methods say photometry was recorded during RI30 and on both shock probes,
but the dandiset holds photometry only for RI60 and RR20 training (62
sessions) and one session described as a probe test. Mice are missing against
the paper: 6 RR20 mice against 9 in Figure 1D (7 in the Methods), 33 DMS
excitatory mice against 39, 42 DMS inhibitory mice against 47 and 35 DLS
excitatory mice against 36, and several mice lack a probe; the NpHR mice
missing are about the number the paper dropped for not learning, and the 'Did
Not Learn' flag marks one NpHR mouse and one EYFP mouse that reached RI60.
Optogenetic mice have no stored phenotype (the notes read 'Punishment Group
nan'), and the DMS inhibitory files do not say whether a mouse is in group 1
or group 2. The fear conditioning, open field and histology are not deposited,
and the paper says data are available on request. Several photometry
recordings hold dropouts where a raw channel falls near zero (6 sessions reach
|z| above 50 after the authors' processing, up to 1758), and in 141.308 on
2019-08-09 the DLS channels drop out through most of the recording, with
nothing marking these or saying which recordings the paper excluded. The 137
files of the group 'Opto-DLS-Excitatory-Unknown' repeat sessions deposited
under a named arm (135 share subject and start time with a named file). Other
findings: 20 RR20 training files of four mice hold port entries only; 11
mouse-days have two or three RI60 files, with nothing saying which is the
day's session (81.236 on 2019-02-06 has 6, 28 and 42 rewards); in 45 of 64
RR20 training files with rewards the reward times coincide with no nosepoke
time; in shock probes on the left nosepoke the reward series is named
right_reward_times (151 files); the stitched photometry session of 332.393 on
2020-07-28 mixes MedPC reward times with TDT nosepoke times; mouse 290.407 is
filed under two experiments; the fiber coordinates are stored without their
signs (DV 2.8 for -2.8, DLS AP 0.1 for -0.1); the authors' MATLAB comments call
Dv1A the control, while the conversion and the files take it as the DMS 465 nm
signal, and the data side with the files in 46 of 61 DMS sessions; 048.392 is
stored as PR with 13 early shocks where the Methods require more than 13, and
the Methods call 13 a median split while the median is 9; the Results give
omission times in seconds that fit minutes, and the Methods give 26 DMS
inhibitory and 7 RR20 mice where the figures count 47 and 9; and the Zenodo
densitometry table holds female samples only, labelled as lanes of one
wild-type and one heterozygous mouse, while the dandiset's blot images include
males.

The notebook ran in 760 s in the first clean run, in about 25 minutes (1407 s)
after round 1, and `tools/entry.py all` took 957 s after round 2. The Europe
PMC full text returned a 500 error and NCBI BioC rate-limited the author, and
the supplement returned a browser check, later a reCAPTCHA page, with the Cell
and Europe PMC copies returning 403. Round 2 found sentences the outputs did
not support, among them that the dropout step had little effect on fig3g and
mixed-model results reported without their convergence and singularity
warnings, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a full text whose supplement cannot be fetched; a tolerance taken
from a stated spread that is the SD across mice, which becomes very wide; no
rule for a data-quality fix found after seeing scores; absence claims for
which the paper gives no test; no outcome for a claim tested on data only
partly deposited; a probe rule refined after the data check; a 10-minute
runtime aim for a dandiset of 4139 files; and version pinning for a paper that
predates its dandiset when all versions hold the same files.
EOF
grep -n '—\|rather' docs/pilot-notes.md | tail -3; git status --short
```

```
M README.md
 M docs/pilot-notes.md
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

I ran `python tools/readme_row.py 000971 --write`. It added the row Seiler et al. 2022 | 17 | 9 | 6 | 5 to README.md. I also appended the subsection below to the end of docs/pilot-notes.md. The record lists 18 reproduced, but one of them (`figs3ab-dat-protein-not-reduced`) uses the Zenodo densitometry table, so the README counts it separately. The subsection reports it the same way. Nothing is committed.

### 000971, Seiler et al. 2022

Seventeen claims reproduced, nine partially, six not reproduced and five
blocked on the dandiset. With outside data, counted apart: one reproduced.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with 37 of the 38; it would block
`fig6-nphr-learning-dropout`, as the dandiset holds 13 NpHR, 13 NpHR Scrambled
and 16 EYFP mice where Figure 6F counts 16, 15 and 16, so the mice the paper
dropped are, but for one, not deposited, and the author changed the claim from
not reproduced to blocked as `data_missing`. Round 1 also asked for the
training files with no rewards to be inspected; one is a 170 s false start of
mouse 140.306, without which Tukey PS vs DPR in `fig2n-rewards-per-session`
gives p = 0.059, and the author changed that claim from reproduced to
partially reproduced. Round 2 agreed with all 38 and nothing was proposed, so
there was no third round. The paper reports that RI60-trained mice accept more
shocks in shock probes than RR20-trained mice, that RI60 mice split into
punishment resistant (PR), delayed punishment resistant (DPR) and punishment
sensitive (PS) phenotypes, that a DMS dopamine axon score from fiber
photometry differs by phenotype and correlates with shocks while the DLS score
does not, and that stimulating DMS dopamine terminals on rewarded nosepokes
makes mice more likely to be PR and inhibiting them more likely to be PS,
while DLS stimulation has no such effect. The schedule comparisons, the
phenotype rule and the training and omission behaviour of the phenotypes, sex
differences, the DMS and DLS scores against phenotype, shocks and omission
time, and the DMS excitation, DMS inhibition and DLS excitation cohorts were
tested, and the DAT protein claim on the Zenodo densitometry table the
dandiset names. The RI30 photometry peaks, the inhibition dropouts, fear
conditioning, open field and histology are blocked as `data_missing`. Some
outcomes rest on weak ground: `fig4g-dls-score-shock-no-correlation` is not
reproduced (r = 0.326, p = 0.024) only with a dropout step the author added
after seeing per-session scores, which is in neither the Methods nor the
authors' code, and without it r = 0.113, p = 0.45; the same step takes the
phenotype p of `fig3f-dms-score-phenotype` from 0.389 to 0.100;
`fig3g-dms-score-shock-correlation` is partially reproduced on one of three
readings (r = 0.375, p = 0.045, n = 29), with p = 0.13 after correction for the
three; `fig2n-rewards-per-session` gives p = 0.048, 0.059 or 0.044 under three
session-exclusion rules, and the one used, set after round 1, is the only one
above 0.05; `fig5f-dms-chr2-escalation` and `fig7f-dls-escalation-similar`
rest on the pooled fit with no mouse term that the criterion fixed, and a mixed
model with a random slope per mouse would make fig5f partially reproduced but
warns of a boundary fit, while a model with a random intercept only puts ChR2
above neither control; and the claims on Figures S1 to S7 rest on the main
text alone. The author used the author manuscript in PubMed Central
(PMC8930615), whose supplement could not be downloaded, and took the
photometry processing from the authors' MATLAB code at commit 56f1529.

The dandiset was converted by CatalystNeuro (catalystneuro/lerner-lab-to-nwb).
The Methods say photometry was recorded during RI30 and on both shock probes,
but the dandiset holds photometry only for RI60 and RR20 training (62
sessions) and one session described as a probe test. Mice are missing against
the paper: 6 RR20 mice against 9 in Figure 1D (7 in the Methods), 33 DMS
excitatory mice against 39, 42 DMS inhibitory mice against 47 and 35 DLS
excitatory mice against 36, and several mice lack a probe; the NpHR mice
missing are about the number the paper dropped for not learning, and the 'Did
Not Learn' flag marks one NpHR mouse and one EYFP mouse that reached RI60.
Optogenetic mice have no stored phenotype (the notes read 'Punishment Group
nan'), and the DMS inhibitory files do not say whether a mouse is in group 1
or group 2. The fear conditioning, open field and histology are not deposited,
and the paper says data are available on request. Several photometry
recordings hold dropouts where a raw channel falls near zero (6 sessions reach
|z| above 50 after the authors' processing, up to 1758), and in 141.308 on
2019-08-09 the DLS channels drop out through most of the recording, with
nothing marking these or saying which recordings the paper excluded. The 137
files of the group 'Opto-DLS-Excitatory-Unknown' repeat sessions deposited
under a named arm (135 share subject and start time with a named file). Other
findings: 20 RR20 training files of four mice hold port entries only; 11
mouse-days have two or three RI60 files, with nothing saying which is the
day's session (81.236 on 2019-02-06 has 6, 28 and 42 rewards); in 45 of 64
RR20 training files with rewards the reward times coincide with no nosepoke
time; in shock probes on the left nosepoke the reward series is named
right_reward_times (151 files); the stitched photometry session of 332.393 on
2020-07-28 mixes MedPC reward times with TDT nosepoke times; mouse 290.407 is
filed under two experiments; the fiber coordinates are stored without their
signs (DV 2.8 for -2.8, DLS AP 0.1 for -0.1); the authors' MATLAB comments call
Dv1A the control, while the conversion and the files take it as the DMS 465 nm
signal, and the data side with the files in 46 of 61 DMS sessions; 048.392 is
stored as PR with 13 early shocks where the Methods require more than 13, and
the Methods call 13 a median split while the median is 9; the Results give
omission times in seconds that fit minutes, and the Methods give 26 DMS
inhibitory and 7 RR20 mice where the figures count 47 and 9; and the Zenodo
densitometry table holds female samples only, labelled as lanes of one
wild-type and one heterozygous mouse, while the dandiset's blot images include
males.

The notebook ran in 760 s in the first clean run, in about 25 minutes (1407 s)
after round 1, and `tools/entry.py all` took 957 s after round 2. The Europe
PMC full text returned a 500 error and NCBI BioC rate-limited the author, and
the supplement returned a browser check, later a reCAPTCHA page, with the Cell
and Europe PMC copies returning 403. Round 2 found sentences the outputs did
not support, among them that the dropout step had little effect on fig3g and
mixed-model results reported without their convergence and singularity
warnings, and these were corrected. Untracked files in the repository root
that the author did not create were left alone. The author's points on the
protocol: a full text whose supplement cannot be fetched; a tolerance taken
from a stated spread that is the SD across mice, which becomes very wide; no
rule for a data-quality fix found after seeing scores; absence claims for
which the paper gives no test; no outcome for a claim tested on data only
partly deposited; a probe rule refined after the data check; a 10-minute
runtime aim for a dandiset of 4139 files; and version pinning for a paper that
predates its dandiset when all versions hold the same files.

## End of run

12 turns, 2 minutes, result: success.
