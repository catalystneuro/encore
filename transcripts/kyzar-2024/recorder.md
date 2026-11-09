# 000469 · recorder · run 41081417449

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/000469 transcripts/000469; python tools/readme_row.py 000469; cat attempts/000469-kyzar-2024-01.yaml
```

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bph5osgdh.txt

Preview (first 2KB):
docs/pilot-notes/000458-claar-2023-01.md
docs/pilot-notes/000462-krishnan-2022-01.md
docs/pilot-notes/000447-tang-2023-01.md
docs/pilot-notes/000402-microns-2025-01.md
docs/pilot-notes/000404-athalye-2023-01.md
claims/000469:
10.1038-s41597-024-02943-8.yaml

transcripts/000469:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bph5osgdh.txt; sed -n '35,400p' $f
```

```
doi: 10.48324/dandi.000469/0.240123.1806
paper: doi:10.1038/s41597-024-02943-8
date: 2026-10-30
entry: 000469-kyzar-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41057427767
outcomes:
- claim: subjects-sessions
  outcome: reproduced
  notebook: reproduce_kyzar_2024.ipynb
  output: claim:subjects-sessions
[... 346 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bph5osgdh.txt; sed -n '400,700p' $f | grep -nE "^- date|reviewed:|Round|agrees: false|third|failed" ; cd docs/pilot-notes; for x in 000458-claar-2023-01 000462-krishnan-2022-01 000447-tang-2023-01 000402-microns-2025-01 000404-athalye-2023-01; do echo "=== $x"; cat $x.md; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000469' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (38.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bc9c0g7dw.txt

Preview (first 2KB):
98:- date: '2026-10-30'
101:  reviewed: Round 2. The full executed notebook with conclusions and summary, the helper module, the claims
=== 000458-claar-2023-01
# 000458, Claar et al. 2023

12 claims reproduced, 13 partially, seven not reproduced and five blocked. It
pins version 0.230317.0039, which the paper cites and which is the only
published version; the dandiset names the bioRxiv preprint. The paper, Claar,
Rembado, Kuyat, Russo, Marks, Olsen and Koch in eLife, records a 30-electrode
skull EEG and up to three Neuropixels probes in head-fixed mice while single
biphasic pulses at three currents stimulate MOs or SSp in layer 2/3
(superficial) or layer 5/6 (deep), awake (quiet or running), under isoflurane
and in recovery, and shows that deep stimulation evokes a late ERP component
that follows thalamic rebound bursts and that PCIst is lower under anesthesia.
The claims were written from the version of record in Europe PMC with its
figure supplement legends; the paper links only the PCIst code
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bc9c0g7dw.txt"
}
```

```
1	98:- date: '2026-10-30'
2	101:  reviewed: Round 2. The full executed notebook with conclusions and summary, the helper module, the claims
3	=== 000458-claar-2023-01
4	# 000458, Claar et al. 2023
5	
6	12 claims reproduced, 13 partially, seven not reproduced and five blocked. It
7	pins version 0.230317.0039, which the paper cites and which is the only
8	published version; the dandiset names the bioRxiv preprint. The paper, Claar,
9	Rembado, Kuyat, Russo, Marks, Olsen and Koch in eLife, records a 30-electrode
10	skull EEG and up to three Neuropixels probes in head-fixed mice while single
11	biphasic pulses at three currents stimulate MOs or SSp in layer 2/3
12	(superficial) or layer 5/6 (deep), awake (quiet or running), under isoflurane
13	and in recovery, and shows that deep stimulation evokes a late ERP component
14	that follows thalamic rebound bursts and that PCIst is lower under anesthesia.
15	The claims were written from the version of record in Europe PMC with its
16	figure supplement legends; the paper links only the PCIst code
17	(renzocom/PCIst at commit e495a0a), whose threshold search was replaced by an
18	exact count and checked against the original on all 30 sites with a largest
19	difference of 0. No analysis says which current it uses, so the highest and the
20	medium current were both run, and the medium current gives the example ERP of
[... 520 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A15 '"000469"' targets/dandisets.json | head -40; f=/home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bph5osgdh.txt; sed -n '400,560p' $f | grep -vE "^\s+(response: No change needed\.)$"
```

```
2382-   "catalystneuro": []
2383-  },
2384-  {
2385:   "dandiset": "000469",
2386-   "name": "Dataset of human-single neuron activity during a Sternberg working memory task.",
2387-   "published_version": "0.240123.1806",
2388-   "asset_count": 41,
2389-   "size_gb": 9.79,
2390-   "data_standards": [
2391-    "Neurodata Without Borders (NWB)"
2392-   ],
2393-   "species": [
2394-    "Homo sapiens - Human"
2395-   ],
2396-   "approaches": [
2397-    "electrophysiological approach"
2398-   ],
2399-   "papers": [
2400-    {
      negligible effect (problem 8).
[... 146 more lines not kept]
```

**Agent**

I have the attempt record and the five most recent notes. Next I'll read the dataset's target entry and the run reports.

**Agent calls Bash**

```bash
sed -n 2399,2425p targets/dandisets.json; f=/home/runner/.claude/projects/-home-runner-work-encore-encore/817b8ecb-c3b4-437d-b756-6172b8434f76/tool-results/bph5osgdh.txt; sed -n '560,700p' $f | grep -E "response|reason" | head -30; cd transcripts/000469; wc -w *-report.md; cat author-report.md
```

```
"papers": [
    {
     "doi": "10.1038/s41597-024-02943-8",
     "title": "Dataset of human-single neuron activity during a Sternberg working memory task",
     "relation": "IsSupplementTo",
     "resource_type": null,
     "preprint": false
    },
    {
     "doi": "10.1038/nn.4509",
     "title": "Persistently active neurons in human medial frontal and medial temporal lobe support working memory",
     "relation": "IsDerivedFrom",
     "resource_type": null,
     "preprint": false
    },
    {
     "doi": "10.1016/j.neuron.2020.01.032",
     "title": "Combined Phase-Rate Coding by Persistently Active Neurons as a Mechanism for Maintaining Multiple Items in Working Memory in Humans",
     "relation": "IsDerivedFrom",
     "resource_type": null,
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000469; cat claims-report.md claims-check-report.md answer-report.md author-answers-report.md author-revise-1-report.md author-revise-2-report.md; head -40 ../../claims/000469/*.yaml
```

```
I wrote `claims/000469/10.1038-s41597-024-02943-8.yaml`. It has 20 claims, all 20 with word-for-word quotes, and the quote checker reports 0 problems. Nothing is committed.

**Text read:** the version of record from Europe PMC (PMC10796636), full text with Methods, Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has no supplement. Its Methods say they are shortened from refs 15 and 20 (Kaminski 2017 and 2020). Those two papers are also under `paper/`, but I did not use them, since the protocol takes methods only from this paper and its code.

**Code read:** `rutishauserlab/workingmem-release-NWB` at commit f8594e0. Its code is the same as tag v1.0.0 (4a98f46); only the README and citation file differ. A rewrite for another dataset was added and reverted the same day, and I ignored it. The Methods name permutation tests; the code runs ordinary parametric tests (ANOVA, paired one-sided t-tests) and keeps permutation versions only in comments. Following the protocol, the Methods give the main criteria and the code's tests are variants. The code also has three bugs:
- **Trial masks:** the masks for preferred and non-preferred trials pick every trial and no trial. As written, the code cannot produce the paper's persistent-activity numbers, and its extra maintenance test for concept cells cannot run.
- **Wrong window:** its "preferred vs non-preferred" rates come from the first encoding window, not the maintenance period the paper names.
- **Encoding 3:** the probe test counts the Encoding 2 window a second time in place of Encoding 3.

**Statistics and criteria:**
- **Statistics:** two claims record a statistic. These are the load effect on reaction time (F(2,40) = 7.92, p = 0.0013) and the persistent-activity test (p = 1.38e-21).
- **Expected numbers:** 19 claims have them, all with a 10% tolerance. The exception is the subject and session counts, which have zero tolerance.
- **Criteria:** all 20 claims have one.

**Details the
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000469; head -c 3500 verifier-1-report.md; echo; echo ====; head -c 2500 verifier-2-report.md
```

```
**Verifier report, round 1: Kyzar et al. 2024 (doi:10.1038/s41597-024-02943-8), DANDI:000469 v0.240123.1806**

The claims file has 20 claims and the notebook tests all 20. My outcomes: 18 reproduced, 1 not_reproduced, 1 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| subjects-sessions | reproduced | Cell 10: 21 subjects, 41 sessions, 21 Sternberg, 20 screening; only subject 19 (P47HMH) has no screening session. My own API query of the pinned version agrees: 41 assets, 21 subjects, 20 ses-1 and 21 ses-2. Ages are 17 to 70, matching Table 1. |
| sternberg-unit-yield | reproduced | Cell 12: 902 units (Hipp 190, Amg 259, dACC 171, pre-SMA 250, vmPFC 32). Every count is exact. |
| screening-unit-yield | reproduced | Cell 14: 907 units, MTL 421. 421 is within 10% of both 449 and 421, so it matches the 421 reading exactly. |
| behavior-accuracy | reproduced | Cell 17: mean over sessions 88.73%. |
| behavior-rt-load | reproduced | Cell 19, correct trials: F(2,40) = 7.92, p = 0.0013, and the mean of session medians rises 1.055 → 1.130 → 1.198 s. I checked `rm_anova_load` against statsmodels AnovaRM on synthetic data and it gives the same F. |
| behavior-accuracy-load | reproduced | Cell 21: accuracy falls monotonically, 91.22 → 88.62 → 86.35%. |
| isi-violations | reproduced | Cell 25: on all units, the mean (0.428) is in tolerance but the s.d. (0.625) is not. With the code's filter (units below 4%, n = 901) the values are 0.416 and 0.498, both in tolerance. The criterion accepts either reading. |
| firing-rate | reproduced | Cell 27: mean 2.546 Hz, min 0.108 Hz, max 33.824 Hz. |
| projection-distance | reproduced | Cell 29: 13.774 ± 7.325 (734 non-zero values). |
| waveform-snr | reproduced | Cell 31: `peak_snr` gives 6.625 ± 3.632. `mean_snr` (1.65 ± 0.95) does not match, but one reading is enough. |
| cv2 | reproduced | Cell 33: 0.938 ± 0.138. |
| isolation-distance | reproduced | Cell 35: median 31.138 over the 676 non-NaN units. |
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "| Dataset" README.md | head -3
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000469-kyzar-2024-01.md",
 "content": "# 000469, Kyzar et al. 2024\n\n18 claims reproduced, none partially, one not reproduced and one blocked, and\nboth verification rounds agreed with all 20 outcomes. It pins version\n0.240123.1806, the latest; the paper cites no version, and all four published\nversions and the draft hold the same 41 assets. The paper, Kyzar, Kaminski,\nBrzezicka, Reed, Chung, Mamelak and Rutishauser in Scientific Data, is a data\ndescriptor of single neurons recorded with hybrid macro-micro depth electrodes\nin 21 patients with drug-resistant epilepsy during an image screening task and\na Sternberg working memory task, and reports the unit yield, behaviour, spike\nsorting quality and the fractions of concept, maintenance and probe cells. The\nclaims were written from the version of record in Europe PMC (PMC10796636) and\nfrom the paper's code (rutishauserlab/workingmem-release-NWB at commit\nf8594e0), whose MATLAB scripts run parametric tests (anovan, paired t-tests)\nwhere the Methods name permutation tests, and keep the permutation versions in\ncomments; the Methods gave the main criteria, with the 2000 permutations of the\ncode's comment, and the code's tests were run as variants. All 20 claims were\ntested and no outcome rests on an assumption. The subject, session and unit\ncounts, the behaviour and the quality metrics match, `isi-violations` only with\nthe code's filter of units below 4% (0.416 and 0.498% against 0.428 and 0.625%\nover all 902 units). `screening-concept-mfc` passes near the tolerance bound:\n27 (5.56%) on the main seed, 29 (5.97%), outside, on one of three other seeds,\nand 26 (5.35%) when the 142 MFC units with a p-value between 0.02 and 0.10 are\nre-tested with 20000 permutations. `persistent-activity` is not reproduced: in\nthe maintenance window concept cells fire more on preferred trials (every\npaired one-sided p below 1e-6), but the preferred means are 2.57 to 3.13 Hz\nagainst the paper's 4.76. `probe-cells-mfc` is blocked as\n`methods_underspecified`, as sign flipping gives 118 (26.05%) and 111 (24.50%),\nwithin tolerance, and label shuffling 109 (24.06%) and 104 (22.96%), outside\nit, against 122, which the code's paired one-sided t-tests give. The author\nasked a reader no questions, so the answer run and the following author run\nchanged nothing. Round 1 found eight problems, none affecting a conclusion;\nthey led to a variant counting ties as exceedances (permutationTest.m counts\nwith a strict inequality, which with discrete spike counts makes the tests\nslightly anti-conservative), under which the maintenance counts stay within\ntolerance (140, 139, 142 and 141) and the probe readings still disagree, to\nthree more seeds for `sternberg-concept-mtl` (95 to 97 two-sided, 99 to 100\none-sided) and to a check of short fixation periods that found a third odd\ntrial. Round 2, whose verifier could not run code as numpy was not installed,\nfound statements the outputs did not support, among them the summary's \"every\nnumber in the paper's quality and behaviour sections is recovered\" and column\ndescriptions no cell printed, which were narrowed or given new outputs, so\nthere was no third round. The author's run took about 45 minutes; two notebook\nruns failed during development, on a dict with float keys passed as `**kwargs`\nand on p-values printed as 0 by rounding, and were fixed. The notebook ran in\n322 s at first and in 223 s in the last run.\n\nThe paper's persistent activity values (4.76 plus or minus 4.71 against 2.67\nplus or minus 3.66 Hz \"during the maintenance period\") are reproduced exactly\nby the rates 200 to 1000 ms after Encoding 1 onset of the code's 119\nparametric concept cells in all areas (4.764 plus or minus 4.709 against 2.673\nplus or minus 3.656 Hz), split by whether the Encoding 1 image is the preferred\none, while in the maintenance window the same cells fire at 3.05 against 2.70\nHz; the released code computes these Encoding 1 rates, and its preferred and\nnon-preferred trial masks, as written, select every trial and no trial. The\ncode's parametric tests reproduce every published cell count exactly (138, 26,\n94, 144, 122), though the Methods name permutation tests. The text gives 449\nMTL units for the screening task, which is the Sternberg MTL count (190 + 259);\nthe screening files hold 421 (159 hippocampus, 262 amygdala), which agrees with\nthe paper's own percentages (138 is 32.78% of 421). The reported ISI violation\nspread (0.41 plus or minus 0.50%) needs the code's exclusion of one unit at\n11.74%, and the reaction time ANOVA uses correct trials only, as the code does;\nneither filter is stated in the paper. Four units have spike times out of\norder, each with one backward step (0.3 to 12.4 ms), in the screening files of\nsubjects 11 and 5 and the Sternberg file of subject 2. `waveforms_mean_proj_dist`\nis described as the isolation distance, `loadsEnc3_PicIDs` as \"Picture ID for\nEnc1 loads\", and every column of the electrodes table but `id` as \"my\ndescription\". Subjects 13 and 14 have the native IDs P39CS and P39CS_2, the\nsame age (26), sex, recording year and diagnosis, with different units and\nelectrodes, and nothing says whether they are one patient, so the 21 patients\nmay be 20. Three Sternberg trials have implausible timestamps: one of subject 9\nhas no maintenance period, another of subject 9 has fixation and Encoding 1\nonsets 0.03 ms apart, and one of subject 21 has a 14.07 s fixation; leaving\nthem out does not change the persistent activity result. Ages in the files run\nfrom 17 to 70, as in Table 1, while the text gives 17 to 71. One question is\nput to the paper's authors: whether the published counts were computed with the\nparametric tests and, if permutation tests were used, how many permutations,\nwhether the probe and maintenance comparisons were paired by trial, and which\nencoding periods form the probe cells' encoding rate.\n\nThe author's points on the protocol: step 1.6 lets the author adopt the\nbest-supported reading while the probe-cells criterion says to block when the\nreadings disagree, and the criterion was followed; persistent-activity's effect\nholds in direction but is much weaker, which the protocol would call partially\nreproduced, while its criterion says not reproduced otherwise, and the\ncriterion was followed; the protocol does not say what to do when a permutation\ncount sits at a tolerance bound, and the 20000-permutation re-test was recorded\nas a deviation; the clock check peaks away from the true onsets in 18 of the 41\nfiles, mostly those with few units, which the notebook lists as not\nestablished; and the example attempt the prompt points to (001453) records\nprotocol `pilot-5`, older than `pilot-12`.\n"
}
```

```
File created successfully at: docs/pilot-notes/000469-kyzar-2024-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -nE "—|rather|\*\*" docs/pilot-notes/000469-kyzar-2024-01.md; git status --short
```

```
44:runs failed during development, on a dict with float keys passed as `**kwargs`
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
?? docs/pilot-notes/000469-kyzar-2024-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/000469-kyzar-2024-01.md`. It is the only file I changed and nothing is committed. The root-level untracked files that `git status` lists (`.bashrc`, `.idea`, `scripts` and others) were already there before this run, and I left them alone.

# 000469, Kyzar et al. 2024

18 claims reproduced, none partially, one not reproduced and one blocked, and both verification rounds agreed with all 20 outcomes. It pins version 0.240123.1806, the latest; the paper cites no version, and all four published versions and the draft hold the same 41 assets. The paper, Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak and Rutishauser in Scientific Data, is a data descriptor of single neurons recorded with hybrid macro-micro depth electrodes in 21 patients with drug-resistant epilepsy during an image screening task and a Sternberg working memory task, and reports the unit yield, behaviour, spike sorting quality and the fractions of concept, maintenance and probe cells. The claims were written from the version of record in Europe PMC (PMC10796636) and from the paper's code (rutishauserlab/workingmem-release-NWB at commit f8594e0), whose MATLAB scripts run parametric tests (anovan, paired t-tests) where the Methods name permutation tests, and keep the permutation versions in comments; the Methods gave the main criteria, with the 2000 permutations of the code's comment, and the code's tests were run as variants. All 20 claims were tested and no outcome rests on an assumption. The subject, session and unit counts, the behaviour and the quality metrics match, `isi-violations` only with the code's filter of units below 4% (0.416 and 0.498% against 0.428 and 0.625% over all 902 units). `screening-concept-mfc` passes near the tolerance bound: 27 (5.56%) on the main seed, 29 (5.97%), outside, on one of three other seeds, and 26 (5.35%) when the 142 MFC units with a p-value between 0.02 and 0.10 are re-tested with 20000 permutations. `persistent-activity` is not reproduced: in the maintenance window concept cells fire more on preferred trials (every paired one-sided p below 1e-6), but the preferred means are 2.57 to 3.13 Hz against the paper's 4.76. `probe-cells-mfc` is blocked as `methods_underspecified`, as sign flipping gives 118 (26.05%) and 111 (24.50%), within tolerance, and label shuffling 109 (24.06%) and 104 (22.96%), outside it, against 122, which the code's paired one-sided t-tests give. The author asked a reader no questions, so the answer run and the following author run changed nothing. Round 1 found eight problems, none affecting a conclusion; they led to a variant counting ties as exceedances (permutationTest.m counts with a strict inequality, which with discrete spike counts makes the tests slightly anti-conservative), under which the maintenance counts stay within tolerance (140, 139, 142 and 141) and the probe readings still disagree, to three more seeds for `sternberg-concept-mtl` (95 to 97 two-sided, 99 to 100 one-sided) and to a check of short fixation periods that found a third odd trial. Round 2, whose verifier could not run code as numpy was not installed, found statements the outputs did not support, among them the summary's "every number in the paper's quality and behaviour sections is recovered" and column descriptions no cell printed, which were narrowed or given new outputs, so there was no third round. The author's run took about 45 minutes; two notebook runs failed during development, on a dict with float keys passed as `**kwargs` and on p-values printed as 0 by rounding, and were fixed. The notebook ran in 322 s at first and in 223 s in the last run.

The paper's persistent activity values (4.76 plus or minus 4.71 against 2.67 plus or minus 3.66 Hz "during the maintenance period") are reproduced exactly by the rates 200 to 1000 ms after Encoding 1 onset of the code's 119 parametric concept cells in all areas (4.764 plus or minus 4.709 against 2.673 plus or minus 3.656 Hz), split by whether the Encoding 1 image is the preferred one, while in the maintenance window the same cells fire at 3.05 against 2.70 Hz; the released code computes these Encoding 1 rates, and its preferred and non-preferred trial masks, as written, select every trial and no trial. The code's parametric tests reproduce every published cell count exactly (138, 26, 94, 144, 122), though the Methods name permutation tests. The text gives 449 MTL units for the screening task, which is the Sternberg MTL count (190 + 259); the screening files hold 421 (159 hippocampus, 262 amygdala), which agrees with the paper's own percentages (138 is 32.78% of 421). The reported ISI violation spread (0.41 plus or minus 0.50%) needs the code's exclusion of one unit at 11.74%, and the reaction time ANOVA uses correct trials only, as the code does; neither filter is stated in the paper. Four units have spike times out of order, each with one backward step (0.3 to 12.4 ms), in the screening files of subjects 11 and 5 and the Sternberg file of subject 2. `waveforms_mean_proj_dist` is described as the isolation distance, `loadsEnc3_PicIDs` as "Picture ID for Enc1 loads", and every column of the electrodes table but `id` as "my description". Subjects 13 and 14 have the native IDs P39CS and P39CS_2, the same age (26), sex, recording year and diagnosis, with different units and electrodes, and nothing says whether they are one patient, so the 21 patients may be 20. Three Sternberg trials have implausible timestamps: one of subject 9 has no maintenance period, another of subject 9 has fixation and Encoding 1 onsets 0.03 ms apart, and one of subject 21 has a 14.07 s fixation; leaving them out does not change the persistent activity result. Ages in the files run from 17 to 70, as in Table 1, while the text gives 17 to 71. One question is put to the paper's authors: whether the published counts were computed with the parametric tests and, if permutation tests were used, how many permutations, whether the probe and maintenance comparisons were paired by trial, and which encoding periods form the probe cells' encoding rate.

The author's points on the protocol: step 1.6 lets the author adopt the best-supported reading while the probe-cells criterion says to block when the readings disagree, and the criterion was followed; persistent-activity's effect holds in direction but is much weaker, which the protocol would call partially reproduced, while its criterion says not reproduced otherwise, and the criterion was followed; the protocol does not say what to do when a permutation count sits at a tolerance bound, and the 20000-permutation re-test was recorded as a deviation; the clock check peaks away from the true onsets in 18 of the 41 files, mostly those with few units, which the notebook lists as not established; and the example attempt the prompt points to (001453) records protocol `pilot-5`, older than `pilot-12`.

## End of run

12 turns, 1 minutes, result: success.
