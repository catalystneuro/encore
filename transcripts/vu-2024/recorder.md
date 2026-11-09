# 001084 · recorder · run 39143698288

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001084 --write; git diff; ls claims/001084 transcripts/001084; cat attempts/001084-vu-2024-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (51.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/622ef0c1-3ed1-4f0f-8f0b-21e7501bb341/tool-results/bpxr1lu86.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 005a559..740fadd 100644
--- a/README.md
+++ b/README.md
@@ -92,6 +92,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
 | [001038](https://dandiarchive.org/dandiset/001038) | [Azcorra et al. 2023](https://doi.org/10.1038/s41593-023-01401-9) | 16 | 7 | 1 | 0 | [`001038-azcorra-2023`](entries/001038-azcorra-2023) |
 | [001075](https://dandiarchive.org/dandiset/001075) | [Randi et al. 2023](https://doi.org/10.1038/s41586-023-06683-4) | 4 | 4 (+1) | 0 (+1) | 7 | [`001075-randi-2023`](entries/001075-randi-2023) |
+| [001084](https://dandiarchive.org/dandiset/001084) | [Vu et al. 2024](https://doi.org/10.1016/j.neuron.2023.12.011) | 10 (+1) | 10 | 0 | 1 | [`001084-vu-2024`](entries/001084-vu-2024) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001084:
10.1016-j.neuron.2023.12.011.yaml

transcripts/001084:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001084-vu-2024-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001084' in json.dumps(x)];print(json.dumps(e,indent=1))"; head -c 3000 README.md | tail -c 1500
```

```
<persisted-output>
Output too large (230KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/622ef0c1-3ed1-4f0f-8f0b-21e7501bb341/tool-results/brdihnqef.txt

Preview (first 2KB):
schema_version: 1
id: 001084-vu-2024-01
dandiset: "001084"
dandiset_version: 0.241023.2011
paper: doi:10.1016/j.neuron.2023.12.011
date: 2026-10-18
entry: 001084-vu-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
[... 28 more lines not kept]
```

**Agent**

The yaml is big. Let me read it with Read.

**Agent calls Read**

```json
{
 "file_path": "attempts/001084-vu-2024-01.yaml"
}
```

```
1	schema_version: 1
2	id: 001084-vu-2024-01
3	dandiset: "001084"
4	dandiset_version: 0.241023.2011
5	paper: doi:10.1016/j.neuron.2023.12.011
6	date: 2026-10-18
7	entry: 001084-vu-2024
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	inputs:
17	- what: The paper's per-fiber results of the salient-stimulus GLM (glm_spline_results.mat, folder
18	    Fig04/general_functions of Fig04.zip), used only by fig4-link-published-results to check that the
19	    dandiset holds the data behind them, and to identify DL18's 12 kHz tones for a variant.
20	  source: Zenodo doi:10.5281/zenodo.10272874 (record 10272874)
[... 769 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 '^| \[000971' README.md | head; grep -n '(+' README.md | head -3; sed -n '/^Counts are of claims/,/^$/p' README.md; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else (d.get('dandisets') or list(d.values()))
for x in it:
  if '001084' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
89-| [000691](https://dandiarchive.org/dandiset/000691) | [Scherrer et al. 2023](https://doi.org/10.1038/s41592-023-01806-1) | 6 | 0 | 0 | 7 | [`000691-scherrer-2023`](entries/000691-scherrer-2023) |
90-| [000727](https://dandiarchive.org/dandiset/000727) | [Brezovec et al. 2022](https://doi.org/10.1101/2022.03.20.485047) | 8 | 5 | 1 | 6 | [`000727-brezovec-2022`](entries/000727-brezovec-2022) |
91-| [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
92:| [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
54:| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
57:| [000035](https://dandiarchive.org/dandiset/000035) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 3 (+2) | 1 (+1) | 0 | 9 (+1) | [`000035-scala-2021`](entries/000035-scala-2021) |
64:| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
Counts are of claims that rest on the dandiset, including those that take
names for its own codes from elsewhere. Claims that also use data from
outside the dandiset are counted apart, in brackets. Claims on data the
paper deposited in other archives are not in this table; the dashboard
shows them on each dandiset's page.

2855:### 000691, Scherrer et al. 2023
2948:### 000727, Brezovec et al. 2022
3039:### 000947, Schwab et al. 2020
3132:### 000971, Seiler et al. 2022
3233:### 001038, Azcorra et al. 2023
3328:### 001075, Randi et al. 2023
3421 docs/pilot-notes.md
```

**Agent calls Bash**

```bash
sed -n 40,52p README.md; grep -n -A12 '"001084"' targets/dandisets.json | head -40
```

```
- [`claims/`](claims): for each target attempted, the findings of the paper
  that were tested.
- [`attempts/`](attempts): one record per attempt, with an outcome for each
  claim, whether or not it worked.
- [`entries/`](entries): the notebooks.
- [`schemas/`](schemas): draft schemas for the files above.

## Attempts so far

| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
|---|---|---|---|---|---|---|
| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
4013:   "dandiset": "001084",
4014-   "name": "Targeted micro-fiber arrays for measuring and manipulating localized multi-scale neural dynamics over large, deep brain volumes during behavior",
4015-   "published_version": "0.241023.2011",
4016-   "asset_count": 180,
4017-   "size_gb": 826.75,
4018-   "data_standards": [
4019-    "Neurodata Without Borders (NWB)"
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 2948
}
```

```
2948	### 000727, Brezovec et al. 2022
2949	
2950	Eight claims reproduced, five partially, one not reproduced and six blocked,
2951	all on the dandiset. Round 1 gave its own outcome for each claim from the
2952	notebook with its conclusions removed and agreed with 19 of the 20; it gave
2953	partially reproduced for `fig5c-global-below-threshold`, as the pass under
2954	one reading rests on r = 0.013 with a p-value that treats autocorrelated
2955	samples as independent. The author kept reproduced and added a null of 200
2956	rolls of each fly's behaviour in time, against which the weakest correlation
2957	has p = 0.025 (null 95th percentile 0.010), and round 2 agreed. Round 1 would
2958	also have blocked the four region-level claims as `data_missing`; the author
2959	kept `metadata_insufficient`, as the voxel data are deposited and only their
2960	labels are missing, and round 2 accepted it. Round 1 also found a wrong
2961	denominator in reading (b) of `fig2c-fraction-correlated`, which moved 54.9%
2962	to 53.5% and no outcome. Round 2 agreed with all 20 and nothing was proposed,
2963	so there was no third round. The preprint reports that whole-brain imaging of
2964	nine walking flies shows activity correlated with forward and turning
2965	velocity across much of the brain, organized by neuropil and mirror-symmetric
2966	for forward velocity, that linear models on the principal components predict
2967	behaviour with weights stereotyped across flies, that turning raises activity
[... 455 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 4013,4060p targets/dandisets.json; grep -n -E '^\s*(- )?id:|data:|^  [a-z_]+:' claims/001084/*.yaml | head -80
```

```
"dandiset": "001084",
   "name": "Targeted micro-fiber arrays for measuring and manipulating localized multi-scale neural dynamics over large, deep brain volumes during behavior",
   "published_version": "0.241023.2011",
   "asset_count": 180,
   "size_gb": 826.75,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
   "approaches": [
    "microscopy approach; cell population imaging"
   ],
   "papers": [
    {
     "doi": "10.1016/j.neuron.2023.12.011",
     "title": "Targeted micro-fiber arrays for measuring and manipulating localized multi-scale neural dynamics over large, deep brain volumes during behavior",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,37p claims/001084/*.yaml; grep -n 'data: elsewhere' -B6 claims/001084/*.yaml | grep -E 'id:|data:'; wc -w transcripts/001084/*-report.md
```

```
# Claims for Vu, Brown, Wen et al. (2024), Neuron, on dandiset 001084.
# Source: the NIH author manuscript in PubMed Central (PMC10957316), full text (Results, figure
# legends, STAR Methods). The supplementary PDF could not be retrieved, so the supplementary
# figure legends were not read; claims on supplementary figures rest on the Results text, the
# Methods and the paper's code.
#
# Code read before writing the criteria: the analysis code the paper deposited on Zenodo
# (doi:10.5281/zenodo.10272874, folders Fig01, Fig04, Fig05, Fig06, Fig07, SuppFig02, SuppFig04,
# SuppFig05, SuppFig06, SuppFig07) and the conversion code github.com/catalystneuro/howe-lab-to-nwb
# at commit 3c53055.
#
# When these criteria were written the author had seen the data check only: the file list,
# subjects, sessions, frame rates, event counts, fiber tables (positions, `included` flags,
# locations), the frame alignment of events, and which fiber carries the laser artefact in each
# optogenetic session. As a check of the loading code, the GLM of one mouse (DL21) had been fit
# once and its per-fiber point estimates compared with the paper's published per-fiber results
# (raw triggered averages identical; spline estimates correlated at 0.998 or more); no
# significance test, latency, gradient or count of any claim had been computed.
#
# Method choices fixed here, from the Methods and, where they are silent, the paper's code:
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001084; cat author-report.md author-revise-1-report.md author-revise-2-report.md; echo =====; sed -n 1,60p verifier-1-report.md; echo ====; sed -n 1,30p verifier-2-report.md
```

```
I finished steps 1 to 6 for dandiset 001084. The entry was locked and passes `check`; the clean run passed in 827 s; the handover was built in `executed/001084-vu-2024/handover/`. Nothing is committed.

I used the full text of the NIH author manuscript in PubMed Central (PMC10957316), saved under `paper/`. The supplement PDF was blocked by a captcha, so I did not read the supplementary figure legends. I pinned version 0.241023.2011, the only published version; the paper cites no DANDI version.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-isosbestic-control | reproduced |
| figs2d-correlation-distance | reproduced |
| figs2ef-no-bundle-crosstalk | reproduced |
| fig1d-chronic-reward-stability | partially (only weeks 5 to 8 can be tested) |
| fig4-link-published-results (with Zenodo inputs) | reproduced |
| fig4e-light-increases-widespread | reproduced |
| fig4e-light-anterior-posterior-gradient | partially |
| fig4f-tone-tail-increase-anterior-decrease | reproduced |
| fig4f-decreases-lateral-ventral | partially |
| figs4ac-patterns-consistent-across-mice | partially |
| figs4eh-patterns-not-movement | partially |
| figs5-isosbestic-no-pattern | partially |
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; grep -n -A3 'statement:' claims/001084/*.yaml | grep -v -E 'source:|criterion:' | cut -c1-200; sed -n 30,80p transcripts/001084/verifier-2-report.md
```

```
39:  statement: In a D1-cre mouse expressing GCaMP7f in D1 spiny projection neurons, fluorescence
40-    under 470 nm excitation shows Ca2+ transients across fibers that are absent under 405 nm
41-    (isosbestic) excitation.
--
49:  statement: Pairwise correlations of D1 SPN Ca2+ signals are generally low but variable, and drop
50-    off significantly with the distance between fiber tips.
--
59:  statement: After accounting for distance in the brain, signal correlations do not depend on the
60-    distance between fibers on the bundle surface, so nearby fibers in the bundle do not cross-talk.
--
69:  statement: Dopamine release to unpredicted water reward is reliable and of comparable amplitude
70-    over at least 12 weeks after implantation (median over 44 fibers, normalized to week 5).
--
84:  statement: The dandiset's DF/F traces, fibers and stimulus times are those behind the paper's
85-    salient-stimulus analysis, so that its per-fiber responses can be linked to the paper's.
87-  data: with_inputs
--
99:  statement: The light evokes transient increases in dopamine release across many striatal
100-    locations.
--
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001084, Vu et al. 2024

Ten claims reproduced, ten partially and one blocked on the dandiset, none
not reproduced. With outside data, counted apart: one reproduced. Four claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 26,
giving `data_missing` as the reason for the five blocked claims; the author
kept `other` (not attempted) for the four whose data are on Zenodo, and changed
`figs3-targeting-errors` to `data_missing` after a new data check showed that
no file's fiber table holds a planned target and the paper's code reads the
targets from calibration files in none of the Zenodo archives. After round 1
the author also added variants that rank AP and the response within each mouse
and permute within mice, under which the light amplitude gradient (r = 0.152,
p = 0.013) and the light and tone latency gradients (r = -0.223, p = 0.0014;
r = 0.214, p = 0.003) remain, and a refit of DL18 with its 14 tones of 12 kHz
identified from the paper's published results. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper records D1 SPN
calcium and dopamine release through micro-fiber arrays across the mouse
striatum, and reports that light and tone evoke dopamine release with distinct
spatial patterns and latency gradients, and that stimulating dopamine axons
through one fiber evokes release at other sites that falls with distance. The
isosbestic control, the pairwise correlations and bundle cross-talk, the
chronic reward responses, the link to the paper's published GLM results on
Zenodo, the light and tone patterns and their consistency across mice and
against movement, the 415 nm control, the latencies and their gradients, and
the optogenetic counts, spread with distance and tdTomato and photoswitching
controls were tested. The histology, the freely moving recordings and the two
D1-cre jaw claims are blocked as `other`, as their data are on Zenodo and were
not tested in this attempt. Some outcomes rest on weak ground:
`fig5ab-response-latencies` is partially reproduced only because the Methods
count latency from the onset frame, while the code's count, one frame later,
gives the paper's means within 2 ms; `figs4eh-patterns-not-movement` fails
under the code's raw DF/F because of the level before onset in the
deceleration trials, and a baseline-subtracted variant holds the tone pattern
in both splits; `fig1d-chronic-reward-stability` can be tested only to week 8;
and in `fig4e-light-increases-widespread` the paper gives p < 1e-6 for its
significance test where the chance rate per fiber is 0.024, which the author
did not block on, since the raw averages are identical to the paper's and
significance agrees with its published calls for 93.6 to 94.5% of pairs. The
author used the NIH author manuscript in PubMed Central (PMC10957316), whose
supplement was blocked by a captcha, so the supplementary figure legends were
not read, and took method choices where the Methods are silent from the
paper's code on Zenodo (doi:10.5281/zenodo.10272874).

The dandiset was converted by CatalystNeuro (catalystneuro/howe-lab-to-nwb).
The 280 fibers of the 7 salient-stimulus mice are the paper's, and their raw
triggered averages equal the paper's published values (largest difference
0.0). The optogenetic sessions (Opto2, Opto4, Opto9, UG21) hold no stimulation
times and no record of which fiber was stimulated, and the trigger line the
paper's code uses is not in the files; both can be recovered only from the
laser artefact in the DF/F, which is unambiguous in Opto2 and UG21 but spreads
over many fibers in the tdTomato mice. The event table gives tones without
their frequency, so DL18's 44 tones cannot be reduced to the 14 at 12 kHz the
paper analysed, and the tone start times are the trigger times, 11 frames
before the sound according to the paper's code, which the dandiset does not
say. DL15's sessions from 2021-09-10 (44 to 70 rewards) were run in a ViRMEn
task whose variables are not in the files, so unpredicted rewards cannot be
separated and Figure 1D can be tested only to week 8. The FiberPhotometryTable
column `included` is described as "whether this fiber has been successfully
implanted", but it marks fibers within the striatum, and in Opto2 two fibers
labelled Caudoputamen are not included; with them the counts match the paper's
24 locations. UG21's indicator is given as tdTomato, while its 3 sessions, 22
included fibers and stimulated fibers 12, 18 and 24 match the paper's rDAm3.0
mouse without opsin. In DL31 and DL32 the fiber photometry series store a
regular rate, but the frame timestamps of the behaviour drift from it by up to
0.43 and 0.54 s over the session. The data of Figures 2, 3, 7, S1 and S5A-D
are not in the dandiset and are on Zenodo, and Opto9 has 12 sessions, so one
of the paper's 26 tdTomato stimulations is missing; the planned fiber targets
behind Figure S3 are neither in the dandiset nor on Zenodo. Other findings: the
paper gives p < 1e-6 for its test of a significant response, the value for
independent frames, while with the same test three given consecutive frames
are all outside the band at a rate of 0.0037; the paper's latency code divides
the 1-based index of the half-maximum frame by the frame rate, so its
latencies are one frame (33 ms) longer than the Methods' definition; its
cross-correlation of DF/F with locomotion does not shift negative lags; the
Figure 1C legend describes 23 example fibers of a 93-fiber array, while the
code plots 33 fibers of mouse 842, whose recording has 82 fibers; and the
archive's summary gives the approach as "cell population imaging" and lists
only NWB container types as variables measured.

The notebook ran in 827 s in the first clean run, in about 10 minutes in two
runs after round 1 and in 12.2 minutes after round 2. Zenodo returned "429 Too
Many Requests" during preparation, handled with retrying range requests, and
early runs failed on a column named `tail` that clashed with a pandas method,
windows running past the end of the recording and event placement in the
18 Hz sessions. Round 2 found sentences the outputs did not support, among
them that none of the 405 nm traces has frames above the threshold (11 of 61
have none), an exact match of the data to the paper's analysis claimed for
mice beyond the 7 where it was shown, and the README run time, and these were
corrected; a slip in the verifier's own round-1 reason for fig1d was left as
given and corrected in the round-2 entry. The author's points on the protocol:
no blocking reason for a claim on data elsewhere that could be tested but was
not attempted; a reported number that matches code disagreeing with the
Methods, where the rule for several readings and the rule for Methods against
code point different ways; no guidance for criteria on supplementary figures
whose legends are unavailable; whether the stated spread in the tolerance rule
includes an SD across fibers; facts seen only while preparing that matter but
may not supply numbers; a duplicate check that needs data from every file; and
a 10-minute runtime aim that the Methods' 10,000 null refits exceed.
EOF
git status --short
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

I ran `python tools/readme_row.py 001084 --write`, which added the 001084 row to README.md. It gives 10 (+1) reproduced, 10 partially, 0 not reproduced and 1 blocked. I then added the subsection below to the end of docs/pilot-notes.md. I haven't committed anything. The repository root has some untracked files I didn't create (.bashrc, .idea, scripts and others), and I left them alone.

### 001084, Vu et al. 2024

Ten claims reproduced, ten partially and one blocked on the dandiset, none
not reproduced. With outside data, counted apart: one reproduced. Four claims
on data in other archives are blocked. Round 1 gave its own outcome for each
claim from the notebook with its conclusions removed and agreed with all 26,
giving `data_missing` as the reason for the five blocked claims; the author
kept `other` (not attempted) for the four whose data are on Zenodo, and changed
`figs3-targeting-errors` to `data_missing` after a new data check showed that
no file's fiber table holds a planned target and the paper's code reads the
targets from calibration files in none of the Zenodo archives. After round 1
the author also added variants that rank AP and the response within each mouse
and permute within mice, under which the light amplitude gradient (r = 0.152,
p = 0.013) and the light and tone latency gradients (r = -0.223, p = 0.0014;
r = 0.214, p = 0.003) remain, and a refit of DL18 with its 14 tones of 12 kHz
identified from the paper's published results. Round 2 agreed with all 26 and
nothing was proposed, so there was no third round. The paper records D1 SPN
calcium and dopamine release through micro-fiber arrays across the mouse
striatum, and reports that light and tone evoke dopamine release with distinct
spatial patterns and latency gradients, and that stimulating dopamine axons
through one fiber evokes release at other sites that falls with distance. The
isosbestic control, the pairwise correlations and bundle cross-talk, the
chronic reward responses, the link to the paper's published GLM results on
Zenodo, the light and tone patterns and their consistency across mice and
against movement, the 415 nm control, the latencies and their gradients, and
the optogenetic counts, spread with distance and tdTomato and photoswitching
controls were tested. The histology, the freely moving recordings and the two
D1-cre jaw claims are blocked as `other`, as their data are on Zenodo and were
not tested in this attempt. Some outcomes rest on weak ground:
`fig5ab-response-latencies` is partially reproduced only because the Methods
count latency from the onset frame, while the code's count, one frame later,
gives the paper's means within 2 ms; `figs4eh-patterns-not-movement` fails
under the code's raw DF/F because of the level before onset in the
deceleration trials, and a baseline-subtracted variant holds the tone pattern
in both splits; `fig1d-chronic-reward-stability` can be tested only to week 8;
and in `fig4e-light-increases-widespread` the paper gives p < 1e-6 for its
significance test where the chance rate per fiber is 0.024, which the author
did not block on, since the raw averages are identical to the paper's and
significance agrees with its published calls for 93.6 to 94.5% of pairs. The
author used the NIH author manuscript in PubMed Central (PMC10957316), whose
supplement was blocked by a captcha, so the supplementary figure legends were
not read, and took method choices where the Methods are silent from the
paper's code on Zenodo (doi:10.5281/zenodo.10272874).

The dandiset was converted by CatalystNeuro (catalystneuro/howe-lab-to-nwb).
The 280 fibers of the 7 salient-stimulus mice are the paper's, and their raw
triggered averages equal the paper's published values (largest difference
0.0). The optogenetic sessions (Opto2, Opto4, Opto9, UG21) hold no stimulation
times and no record of which fiber was stimulated, and the trigger line the
paper's code uses is not in the files; both can be recovered only from the
laser artefact in the DF/F, which is unambiguous in Opto2 and UG21 but spreads
over many fibers in the tdTomato mice. The event table gives tones without
their frequency, so DL18's 44 tones cannot be reduced to the 14 at 12 kHz the
paper analysed, and the tone start times are the trigger times, 11 frames
before the sound according to the paper's code, which the dandiset does not
say. DL15's sessions from 2021-09-10 (44 to 70 rewards) were run in a ViRMEn
task whose variables are not in the files, so unpredicted rewards cannot be
separated and Figure 1D can be tested only to week 8. The FiberPhotometryTable
column `included` is described as "whether this fiber has been successfully
implanted", but it marks fibers within the striatum, and in Opto2 two fibers
labelled Caudoputamen are not included; with them the counts match the paper's
24 locations. UG21's indicator is given as tdTomato, while its 3 sessions, 22
included fibers and stimulated fibers 12, 18 and 24 match the paper's rDAm3.0
mouse without opsin. In DL31 and DL32 the fiber photometry series store a
regular rate, but the frame timestamps of the behaviour drift from it by up to
0.43 and 0.54 s over the session. The data of Figures 2, 3, 7, S1 and S5A-D
are not in the dandiset and are on Zenodo, and Opto9 has 12 sessions, so one
of the paper's 26 tdTomato stimulations is missing; the planned fiber targets
behind Figure S3 are neither in the dandiset nor on Zenodo. Other findings: the
paper gives p < 1e-6 for its test of a significant response, the value for
independent frames, while with the same test three given consecutive frames
are all outside the band at a rate of 0.0037; the paper's latency code divides
the 1-based index of the half-maximum frame by the frame rate, so its
latencies are one frame (33 ms) longer than the Methods' definition; its
cross-correlation of DF/F with locomotion does not shift negative lags; the
Figure 1C legend describes 23 example fibers of a 93-fiber array, while the
code plots 33 fibers of mouse 842, whose recording has 82 fibers; and the
archive's summary gives the approach as "cell population imaging" and lists
only NWB container types as variables measured.

The notebook ran in 827 s in the first clean run, in about 10 minutes in two
runs after round 1 and in 12.2 minutes after round 2. Zenodo returned "429 Too
Many Requests" during preparation, handled with retrying range requests, and
early runs failed on a column named `tail` that clashed with a pandas method,
windows running past the end of the recording and event placement in the
18 Hz sessions. Round 2 found sentences the outputs did not support, among
them that none of the 405 nm traces has frames above the threshold (11 of 61
have none), an exact match of the data to the paper's analysis claimed for
mice beyond the 7 where it was shown, and the README run time, and these were
corrected; a slip in the verifier's own round-1 reason for fig1d was left as
given and corrected in the round-2 entry. The author's points on the protocol:
no blocking reason for a claim on data elsewhere that could be tested but was
not attempted; a reported number that matches code disagreeing with the
Methods, where the rule for several readings and the rule for Methods against
code point different ways; no guidance for criteria on supplementary figures
whose legends are unavailable; whether the stated spread in the tolerance rule
includes an SD across fibers; facts seen only while preparing that matter but
may not supply numbers; a duplicate check that needs data from every file; and
a 10-minute runtime aim that the Methods' 10,000 null refits exceed.

## End of run

12 turns, 2 minutes, result: success.
