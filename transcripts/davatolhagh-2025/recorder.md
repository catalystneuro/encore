# 001712 · recorder · run 39237875714

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001712 --write; echo EXIT $?; git diff; ls claims/001712 transcripts/001712; cat attempts/001712-davatolhagh-2025-01.yaml; grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (34KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d4a0677c-36f0-4b32-a91b-50d08b0fbf9a/tool-results/bz8xdw5gw.txt

Preview (first 2KB):
EXIT 0
diff --git a/README.md b/README.md
index a84626c..844b950 100644
--- a/README.md
+++ b/README.md
@@ -101,6 +101,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001692](https://dandiarchive.org/dandiset/001692) | [Bouabid et al. 2026](https://doi.org/10.64898/2026.01.20.700614) | 18 | 8 | 3 | 0 | [`001692-bouabid-2026`](entries/001692-bouabid-2026) |
 | [001699](https://dandiarchive.org/dandiset/001699) | [Moore et al. 2025](https://doi.org/10.1101/2025.01.09.632139) | 14 | 7 | 5 | 1 | [`001699-moore-2025`](entries/001699-moore-2025) |
 | [001878](https://dandiarchive.org/dandiset/001878) | [Sun et al. 2021](https://doi.org/10.22002/d1.1991) | 4 (+1) | 2 (+1) | 0 | 0 | [`001878-sun-2021`](entries/001878-sun-2021) |
+| [001712](https://dandiarchive.org/dandiset/001712) | [Davatolhagh et al. 2025](https://doi.org/10.1101/2025.09.12.675910) | 3 | 2 | 2 | 11 | [`001712-davatolhagh-2025`](entries/001712-davatolhagh-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001712:
10.1101-2025.09.12.675910.yaml

[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001712-davatolhagh-2025-01.yaml; grep -n "^| Dandiset" -A1 README.md; grep -n "^### " docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (32.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d4a0677c-36f0-4b32-a91b-50d08b0fbf9a/tool-results/bggdwx3kk.txt

Preview (first 2KB):
schema_version: 1
id: 001712-davatolhagh-2025-01
dandiset: "001712"
dandiset_version: draft
paper: doi:10.1101/2025.09.12.675910
date: 2026-10-19
entry: 001712-davatolhagh-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
outcomes:
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '"001712"' -A25 targets/dandisets.json | head -40
```

```
5902:   "dandiset": "001712",
5903-   "name": "IBL Widefield",
5904-   "published_version": null,
5905-   "asset_count": 5,
5906-   "size_gb": 39.6,
5907-   "data_standards": [
5908-    "Neurodata Without Borders (NWB)"
5909-   ],
5910-   "species": [
5911-    "Mus musculus - House mouse"
5912-   ],
5913-   "approaches": [
5914-    "microscopy approach; cell population imaging",
5915-    "behavioral approach"
5916-   ],
5917-   "papers": [
5918-    {
5919-     "doi": "10.1101/2025.09.12.675910",
5920-     "title": "Altered Use of Prior Expectations and Modified Neural Dynamics in a Mouse Model of Autism",
5921-     "relation": "IsDescribedBy",
[... 6 more lines not kept]
```

**Agent**

The attempt file is large. Let me read it in full.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/d4a0677c-36f0-4b32-a91b-50d08b0fbf9a/tool-results/bggdwx3kk.txt"
}
```

```
1	schema_version: 1
2	id: 001712-davatolhagh-2025-01
3	dandiset: "001712"
4	dandiset_version: draft
5	paper: doi:10.1101/2025.09.12.675910
6	date: 2026-10-19
7	entry: 001712-davatolhagh-2025
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: fig1c-psychometric
18	  outcome: reproduced
19	  notebook: reproduce_davatolhagh_2025.ipynb
20	  output: claim:fig1c-psychometric
[... 539 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3803
}
```

```
File content (280.2KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
sed -n '3803,4318p' docs/pilot-notes.md | awk '{print NR+3802": "length($0)}' | sort -t: -k2 -n -r | head; sed -n '4228,4318p' docs/pilot-notes.md | cut -c1-400
```

```
3858: 102
3975: 83
4284: 80
4282: 80
3842: 80
4312: 79
4293: 79
4280: 79
4279: 79
4269: 79
### 001878, Sun et al. 2021

Four claims reproduced and two partially on the dandiset, none not reproduced
or blocked. With outside data, counted apart: one reproduced and one partially
reproduced. Fourteen claims on the CalMS21 files on CaltechDATA: five
reproduced, three partially and six blocked. Round 1 gave its own outcome for
each claim from the notebook with its conclusions removed and agreed with all
22, but would give `data_missing` as the reason for blocking
`fig7-errors-at-transitions` and `fig11-annotator-similarity`; the author kept
`methods_underspecified`, since fig7 depends on the blocked baseline of
[... 81 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3803,
 "limit": 425
}
```

```
3803	### 001538, Zhai et al. 2025
3804	
3805	Fifteen claims reproduced, three not reproduced and fifteen blocked on the
3806	dandiset, none partially. With outside data, counted apart: one reproduced,
3807	two partially reproduced and one not reproduced. Nine claims on the paper's
3808	per-cell tables on Zenodo are reproduced. Round 1 gave its own outcome for
3809	each claim from the notebook with its conclusions removed and agreed with 44
3810	of the 45; it would call `fig1i-dspn-dendritic-sch-lower` not reproduced, as
3811	its criterion defines only the reproduced case and P is 0.066, and the author
3812	changed it from partially reproduced. The author also changed the reason for
3813	the six spine blocks from `not_runnable` to `methods_underspecified`, as round
3814	1 proposed. Round 2 agreed with all 45 and nothing was proposed, so there was
3815	no third round. The paper reports, in a mouse model of levodopa-induced
3816	dyskinesia, that dSPNs are more excitable in the on-state than in the
3817	off-state and iSPNs less, at the soma and in dendrites, that evoked ACh
3818	release is elevated in the off-state, that M1 receptors and CDGI underlie the
3819	off-state rise in iSPN dendritic excitability, and that deleting CDGI or iSPN
3820	M1 receptors attenuates dyskinesia. The links to the paper's tables, the
3821	somatic and dendritic excitability of dSPNs and iSPNs with SCH 23390,
3822	sulpiride, M1R antagonism, CDGI KO and M1R deletion, and two GRAB-ACh
[... 405 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '5926,5935p' targets/dandisets.json; wc -c transcripts/001712/*-report.md claims/001712/*; cat transcripts/001712/author-report.md
```

```
"catalystneuro": [
    "conversion code at https://github.com/catalystneuro/IBL-widefield-to-nwb",
    "contributor Weigl, Szonja of CatalystNeuro",
    "contributor Trapani, Alessandra of CatalystNeuro"
   ]
  },
  {
   "dandiset": "001746",
   "name": "Electrophysiological Dataset of Patch-seq Recording in non-Human Primate Anterior Insular Cortex",
   "published_version": "0.260825.0222",
 4900 transcripts/001712/author-report.md
 3511 transcripts/001712/author-revise-1-report.md
 3159 transcripts/001712/author-revise-2-report.md
 9824 transcripts/001712/verifier-1-report.md
 6621 transcripts/001712/verifier-2-report.md
11209 claims/001712/10.1101-2025.09.12.675910.yaml
39224 total
I finished steps 1 to 6 for dandiset 001712. Five of the six testable claims came out reproduced or partially reproduced and one did not; the other twelve claims are blocked because the dandiset holds one mouse with no stated genotype. I used the paper's full text (bioRxiv v1, CC-BY-NC-ND), saved under `paper/`. The entry passes `check`, runs from a clean environment in 380 s, and the handover is built. Nothing is committed.

### 1. Outcomes
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001712; cat verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; cd ../..; head -40 claims/001712/*.yaml
```

```
**Verification report, round 1: Davatolhagh et al. 2025 (doi:10.1101/2025.09.12.675910) on DANDI 001712 (draft)**

The claims file lists 18 claims. The notebook tests 7 and marks 11 blocked for missing data. No attempt record was among my materials, so these counts come from the claims file and the notebook's code cells. bioRxiv refused every request from this host (Cloudflare error 1015, then HTTP 429), so I read only the abstract, saved as `paper/biorxiv_details_abstract.json`. For methods I relied on the claims file's account of the paper.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1c-psychometric | reproduced | Cell 16: Spearman rho is 1.000 over 9 signed contrasts. P(right) at +100% minus -100% is 0.887 (needs ≥0.5). The lapse-and-erf fit is reported (bias -6.8, sigma 17.0, lapses 0.116 and 0.0). |
| fig1d-psychometric-params-genotype | blocked (data_missing) | One mouse and no genotype anywhere (checked below). |
| fig1e-rt-contrast | not_reproduced | Cell 19: rho is -0.053 with p = 0.15, which fails the p < 0.05 requirement. The median at 0% (0.089 s) does exceed the median at 100% (0.081 s). The result depends on how anticipatory movements are handled: with RT > 0.15 s, p = 0.0006 (see B2). |
| fig1f-rt-genotype | blocked (data_missing) | Genotype comparison. |
| fig1g-learning-genotype | blocked (data_missing) | One session only, and no genotype. |
| fig2bc-prior-shift | reproduced | Cell 21: at 0% contrast P(right) is 74/89 in right blocks against 37/73 in left blocks, one-sided Fisher p = 9.2e-6. Differences at each contrast and per-block biases (+2.9 vs -16.5) are reported and point the right way. |
| fig2bd-ko-smaller-shift | blocked (data_missing) | Genotype comparison. |
| fig2ef-block-adaptation | reproduced | Cell 24: A = 0.48, B = 1.00, tau = 25.1 trials, all within the criterion. Trials 20–39 vs 0–4: 0.827 vs 0.543, Fisher p = 2.7e-6. The fit is weak: B sits at its upper bound and tau has SE 16 (B3). |
| fig2g-ko-slower-a
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -E "^\s*(- id|statement|data):" -A2 claims/001712/*.yaml | cut -c1-220 | head -120
```

```
47:- id: fig1c-psychometric
48:  statement: Mice of both genotypes show sigmoidal psychometric curves, with the proportion of
49-    rightward choices increasing as the stimulus contrast increases on the right.
50-  source: Figure 1C; Results, first section
--
55:- id: fig1d-psychometric-params-genotype
56:  statement: Psychometric bias, slope and lapse rates do not differ between WT and KO mice (bias
57-    p = 0.94, slope p = 0.95, left lapse p = 0.16, right lapse p = 0.22).
58-  source: Figure 1D; Results, first section
59:- id: fig1e-rt-contrast
60:  statement: Reaction time (time to first movement) is longer at lower contrasts in both
61-    genotypes.
62-  source: Figure 1E
--
66:- id: fig1f-rt-genotype
67:  statement: Reaction times do not differ between genotypes on correct (p = 0.234) or incorrect
68-    (p = 0.522) trials.
69-  source: Figure 1F; Results, first section
70:- id: fig1g-learning-genotype
71:  statement: WT and KO mice learn the task with similar trajectories, reaching asymptotic
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/sec.txt <<'EOF'
### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked on the dandiset. Round 1 had no attempt record and gave its own outcome for each claim from the notebook with its conclusion cells and summary removed, and agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL visual decision task with biased blocks, with widefield calcium imaging of cortex and a linear encoding model, and reports that knockout mice shift their choices less between blocks and adapt more slowly after a switch, and show elevated cortical activity, higher correlations and variance, and a larger loss of explained variance when movement predictors are shuffled. The psychometric curve, the dependence of reaction time on contrast, the prior shift and adaptation after block switches, the response to contralateral stimuli and the encoding model's full cvR2 and movement contribution were tested on the one session; the eleven claims that need mice of both genotypes are blocked as `data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15), while with reaction times above 0.15 s only the correlation is -0.226 (p = 0.00062) and 149 of 899 onsets fall at or before the stimulus. `fig3b-contralateral-visual` is not reproduced because the criterion's peak search found frame corners outside the brain; a masked variant puts the peaks on opposite sides of the midline (p = 8.1e-15 and 1.6e-17) but does not show the lateralization is visual, as paw speed, wheel velocity and motion energy differ by stimulus side in the same window. `fig4c-full-cvr2` (0.471 against 0.486 to 0.660) and `fig4cd-movement-dominates` (movement drop 0.104 against 0.297 to 0.440) are partially reproduced on a design with the body camera's video components only; with the side cameras added the full cvR2 is 0.574 and 0.525, within the range, and with folds that keep each trial's frames together 0.472 and 0.405, below it, and the paper's Results give 0.60 and 0.54 while its Figure 4C legend says the trial time regressor was subtracted, under which reading the values here are 0.123 and 0.133 (0.226 and 0.236 with all cameras). Some outcomes rest on weak ground: in `fig2ef-block-adaptation` B sits at its bound and tau is poorly determined (25.12 trials, SE 16.14, bootstrap interval 6.41 to 38.37), and in fig4cd, with folds by trial and the body camera only, task exceeds movement over components (0.012 against -0.005), which the criterion would count as not reproduced.

The dandiset was converted by CatalystNeuro (catalystneuro/IBL-widefield-to-nwb). It holds one session of one mouse (sub-FD-28), where the paper analyses 10 sessions from each of 11 wild-type and 8 Nrxn1a knockout mice, so eleven of the paper's findings, all comparisons between genotypes, cannot be tested. The mouse's genotype is not given in the NWB files, the dandiset metadata or the public IBL database (subject FD_28 has an empty genotype list, from a query made by hand during the attempt); the subject description is the paper's general description of the cross, and a comment in the conversion script lists the session under knockout sessions, next to a note that the list is a placeholder. Neither NWB file holds the cortical landmarks or the registration to the Allen atlas that the conversion code's documentation describes for the processed file, so no pixel can be assigned to a cortical area, and the SVD spatial components cover the whole 540 x 640 frame with no brain mask, with large values at the corners in stimulus-evoked maps. Both imaging planes give the indicator as GCaMP6f, where the Methods and the file's keywords give GCaMP6s; the raw file's imaging planes state an imaging rate of 15 Hz, where the timestamps give 31.2 Hz per channel (32.03 ms intervals) and the Methods 30 Hz; and the dandiset's keywords and description name "CNTNALP2", which is neither the gene of the paper and the files (Nrxn1a) nor a correct spelling of Cntnap2. The wheel series state that counter-clockwise is positive, but trials whose choice is labelled counter_clockwise turn the wheel with negative velocity (95.5% of them 0.1 to 0.3 s after movement onset), while the choice labels agree with the rewards, and the wheel movement onset is described as the first movement after the go cue, but 151 of 899 onsets precede the go cue (by up to 0.18 s). Other findings: the ROI motion energy series give the ROI position in pixels but not the body part it covers; the dandiset has no published version; the paper's analysis code is to be made public on publication, and the encoding code it links (churchlandlab/chiCa) implements the model for single-cell data in another task; and in the Figure 3 legend the correlation panel is labelled (E) twice and (D) is missing, the correlation panel's legend says the KO minus WT matrix shows reduced correlations where the Results say they are increased, and the legend of panel C describes variance difference maps, as does panel E.

The notebook ran in 380 s in the first clean run, 6.6 minutes after round 1, when a second notebook (`encoding_all_cameras.ipynb`) taking 21 minutes was added for the side cameras, and 6.4 and 20.7 minutes after round 2. bioRxiv returned rate limits for several minutes before the author got the PDF, refused both verifiers and the first revision, and answered in the second revision, whose full text confirmed the Figure 3 legend finding and gave reaction time as the time to first movement without saying how that movement is detected. PyAV could not open S3 URLs directly and the video was streamed through remfile, and the author's first imaging clock check had no power and was replaced, while the 15 Hz rate, the wheel sign and the onsets before the go cue showed up only during analysis and were added to the data check. Round 1's points led to variants for fig1e, fig2ef, fig3b and the encoding model, none changing an outcome, and the count of blocked claims in the README and a finding was corrected from twelve to eleven. Round 2 found statements the outputs did not support, among them the openalyx genotype result, a count of 17 sessions for 19 mice, where the IBL places its side-camera ROI, and "brain pixels" for a brightness and margin mask, and these were labelled, removed or corrected. Untracked files in the repository root that the author did not create were left alone. The author's points on the protocol: no published version, where the protocol allows a draft only for repeat attempts; a genotype that is unknown while the paper reports values per group, so tolerances span both group means and the schema takes a single value; outside data in a live database without a pinned version; a time-shifted label check that fails where shifted windows land in other lateralized task periods and block structure correlates labels across trials; a criterion fixed in advance that hits an artefact; linked code that does not implement the paper's analysis; and leaving out part of a model for runtime, which the protocol does not cover.
EOF
python3 - <<'EOF'
import os,textwrap
t=open(os.environ['TMPDIR']+'/sec.txt').read().strip().split('\n\n')
out=[t[0]]+[textwrap.fill(p,79,break_long_words=False,break_on_hyphens=False) for p in t[1:]]
s='\n\n'.join(out)+'\n'
p='docs/pilot-notes.md'
c=open(p).read()
if not c.endswith('\n'): c+='\n'
open(p,'w').write(c+'\n'+s)
EOF
grep -c "—" docs/pilot-notes.md; tail -5 docs/pilot-notes.md; git status --short
```

```
0
pinned version; a time-shifted label check that fails where shifted windows
land in other lateralized task periods and block structure correlates labels
across trials; a criterion fixed in advance that hits an artefact; linked code
that does not implement the paper's analysis; and leaving out part of a model
for runtime, which the protocol does not cover.
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

**Agent calls Bash**

```bash
git diff docs/pilot-notes.md | head -20; grep -n -i "rather" <(git diff docs/pilot-notes.md)
```

```
diff --git a/docs/pilot-notes.md b/docs/pilot-notes.md
index bd23da9..3cc173e 100644
--- a/docs/pilot-notes.md
+++ b/docs/pilot-notes.md
@@ -4316,3 +4316,103 @@ two block reasons; no repository or commit to record for unreachable code;
 claims that are themselves data checks; a duplicate check written for the
 dandiset and run on the outside data; and the paper's own numbers used in an
 analysis.
+
+### 001712, Davatolhagh et al. 2025
+
+Three claims reproduced, two partially, two not reproduced and eleven blocked
+on the dandiset. Round 1 had no attempt record and gave its own outcome for
+each claim from the notebook with its conclusion cells and summary removed, and
+agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
+there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
+knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
+visual decision task with biased blocks, with widefield calcium imaging of
+cortex and a linear encoding model, and reports that knockout mice shift their
+choices less between blocks and adapt more slowly after a switch, and show
```

**Agent calls Bash**

```bash
sed -n '4320,$p' docs/pilot-notes.md
```

```
### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
visual decision task with biased blocks, with widefield calcium imaging of
cortex and a linear encoding model, and reports that knockout mice shift their
choices less between blocks and adapt more slowly after a switch, and show
elevated cortical activity, higher correlations and variance, and a larger loss
of explained variance when movement predictors are shuffled. The psychometric
curve, the dependence of reaction time on contrast, the prior shift and
adaptation after block switches, the response to contralateral stimuli and the
encoding model's full cvR2 and movement contribution were tested on the one
session; the eleven claims that need mice of both genotypes are blocked as
`data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15),
while with reaction times above 0.15 s only the correlation is -0.226 (p =
0.00062) and 149 of 899 onsets fall at or before the stimulus.
[... 79 more lines not kept]
```

**Agent**

I ran `tools/readme_row.py 001712 --write`, which added this row to README.md: 3 reproduced, 2 partially, 2 not reproduced, 11 blocked. I then added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, its claims and its entry are unchanged.

### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
visual decision task with biased blocks, with widefield calcium imaging of
cortex and a linear encoding model, and reports that knockout mice shift their
choices less between blocks and adapt more slowly after a switch, and show
elevated cortical activity, higher correlations and variance, and a larger loss
of explained variance when movement predictors are shuffled. The psychometric
curve, the dependence of reaction time on contrast, the prior shift and
adaptation after block switches, the response to contralateral stimuli and the
encoding model's full cvR2 and movement contribution were tested on the one
session; the eleven claims that need mice of both genotypes are blocked as
`data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15),
while with reaction times above 0.15 s only the correlation is -0.226 (p =
0.00062) and 149 of 899 onsets fall at or before the stimulus.
`fig3b-contralateral-visual` is not reproduced because the criterion's peak
search found frame corners outside the brain; a masked variant puts the peaks
on opposite sides of the midline (p = 8.1e-15 and 1.6e-17) but does not show
the lateralization is visual, as paw speed, wheel velocity and motion energy
differ by stimulus side in the same window. `fig4c-full-cvr2` (0.471 against
0.486 to 0.660) and `fig4cd-movement-dominates` (movement drop 0.104 against
0.297 to 0.440) are partially reproduced on a design with the body camera's
video components only; with the side cameras added the full cvR2 is 0.574 and
0.525, within the range, and with folds that keep each trial's frames together
0.472 and 0.405, below it, and the paper's Results give 0.60 and 0.54 while its
Figure 4C legend says the trial time regressor was subtracted, under which
reading the values here are 0.123 and 0.133 (0.226 and 0.236 with all cameras).
Some outcomes rest on weak ground: in `fig2ef-block-adaptation` B sits at its
bound and tau is poorly determined (25.12 trials, SE 16.14, bootstrap interval
6.41 to 38.37), and in fig4cd, with folds by trial and the body camera only,
task exceeds movement over components (0.012 against -0.005), which the
criterion would count as not reproduced.

The dandiset was converted by CatalystNeuro
(catalystneuro/IBL-widefield-to-nwb). It holds one session of one mouse
(sub-FD-28), where the paper analyses 10 sessions from each of 11 wild-type and
8 Nrxn1a knockout mice, so eleven of the paper's findings, all comparisons
between genotypes, cannot be tested. The mouse's genotype is not given in the
NWB files, the dandiset metadata or the public IBL database (subject FD_28 has
an empty genotype list, from a query made by hand during the attempt); the
subject description is the paper's general description of the cross, and a
comment in the conversion script lists the session under knockout sessions,
next to a note that the list is a placeholder. Neither NWB file holds the
cortical landmarks or the registration to the Allen atlas that the conversion
code's documentation describes for the processed file, so no pixel can be
assigned to a cortical area, and the SVD spatial components cover the whole 540
x 640 frame with no brain mask, with large values at the corners in
stimulus-evoked maps. Both imaging planes give the indicator as GCaMP6f, where
the Methods and the file's keywords give GCaMP6s; the raw file's imaging planes
state an imaging rate of 15 Hz, where the timestamps give 31.2 Hz per channel
(32.03 ms intervals) and the Methods 30 Hz; and the dandiset's keywords and
description name "CNTNALP2", which is neither the gene of the paper and the
files (Nrxn1a) nor a correct spelling of Cntnap2. The wheel series state that
counter-clockwise is positive, but trials whose choice is labelled
counter_clockwise turn the wheel with negative velocity (95.5% of them 0.1 to
0.3 s after movement onset), while the choice labels agree with the rewards,
and the wheel movement onset is described as the first movement after the go
cue, but 151 of 899 onsets precede the go cue (by up to 0.18 s). Other
findings: the ROI motion energy series give the ROI position in pixels but not
the body part it covers; the dandiset has no published version; the paper's
analysis code is to be made public on publication, and the encoding code it
links (churchlandlab/chiCa) implements the model for single-cell data in
another task; and in the Figure 3 legend the correlation panel is labelled (E)
twice and (D) is missing, the correlation panel's legend says the KO minus WT
matrix shows reduced correlations where the Results say they are increased, and
the legend of panel C describes variance difference maps, as does panel E.

The notebook ran in 380 s in the first clean run, 6.6 minutes after round 1,
when a second notebook (`encoding_all_cameras.ipynb`) taking 21 minutes was
added for the side cameras, and 6.4 and 20.7 minutes after round 2. bioRxiv
returned rate limits for several minutes before the author got the PDF, refused
both verifiers and the first revision, and answered in the second revision,
whose full text confirmed the Figure 3 legend finding and gave reaction time as
the time to first movement without saying how that movement is detected. PyAV
could not open S3 URLs directly and the video was streamed through remfile, and
the author's first imaging clock check had no power and was replaced, while the
15 Hz rate, the wheel sign and the onsets before the go cue showed up only
during analysis and were added to the data check. Round 1's points led to
variants for fig1e, fig2ef, fig3b and the encoding model, none changing an
outcome, and the count of blocked claims in the README and a finding was
corrected from twelve to eleven. Round 2 found statements the outputs did not
support, among them the openalyx genotype result, a count of 17 sessions for 19
mice, where the IBL places its side-camera ROI, and "brain pixels" for a
brightness and margin mask, and these were labelled, removed or corrected.
Untracked files in the repository root that the author did not create were left
alone. The author's points on the protocol: no published version, where the
protocol allows a draft only for repeat attempts; a genotype that is unknown
while the paper reports values per group, so tolerances span both group means
and the schema takes a single value; outside data in a live database without a
pinned version; a time-shifted label check that fails where shifted windows
land in other lateralized task periods and block structure correlates labels
across trials; a criterion fixed in advance that hits an artefact; linked code
that does not implement the paper's analysis; and leaving out part of a model
for runtime, which the protocol does not cover.

## End of run

14 turns, 2 minutes, result: success.
