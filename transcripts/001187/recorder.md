# 001187 · recorder · run 41306240037

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls claims/001187 transcripts/001187; python tools/readme_row.py 001187; cat attempts/001187-daume-2024-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '001187' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (50.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/bvfaah03u.txt

Preview (first 2KB):
docs/pilot-notes/001174-martel-2025-01.md
docs/pilot-notes/001051-bennett-2024-01.md
docs/pilot-notes/001047-silkuniene-2025-01.md
docs/pilot-notes/000715-yemini-2021-01.md
docs/pilot-notes/001027-pakhomov-2023-01.md
claims/001187:
10.1016-j.neuron.2024.09.013.yaml

transcripts/001187:
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
cd  cat /home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/bvfaah03u.txt | sed -n '30,400p'
```

```
id: 001187-daume-2024-01
dataset:
  archive: dandi
  id: "001187"
  version: 0.240904.2347
  doi: 10.48324/dandi.001187/0.240904.2347
paper: doi:10.1016/j.neuron.2024.09.013
date: 2026-11-01
entry: 001187-daume-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/41284150060
[... 351 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '400,700p' /home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/bvfaah03u.txt
```

```
units than Table S1 lists (P1809jh hippocampus 1 against 6, P61cs_2 hippocampus 1 against 2,
    P68cs amygdala 7 against 17, P82cs amygdala 17 against 24).
- kind: metadata_error
  statement: Every file gives Cedars-Sinai Medical Center as the institution, though 14 sessions
    have Toronto Western identifiers (TWH) and 6 Johns Hopkins identifiers (JHU), and the paper
    says the patients were recorded at three institutions.
- kind: metadata_insufficient
  statement: The new pictures of the LTM test (IDs 1001 to 1200) carry no category, and their
    stimulus images are named only by ID, so analyses of preferred-category new pictures (Fig. 4d)
    need the images to be viewed. Viewed for this attempt, the images of each of the three task
    variants form consecutive blocks of 40 IDs per category, in the order of the old pictures'
    leading digits.
- kind: metadata_insufficient
  statement: The LTM confidence column is described as 1 to 6 with no coding. The accuracy column
    agrees in every trial with 1 to 3 meaning new and 4 to 6 old, 1 and 6 being sure as the
    paper's code reads it, but the coding is not stated in the files.
- kind: metadata_error
  statement: One LTM trial of sub-24 session 2 has confidence 7, outside the documented 1 to 6.
- kind: format_error
  statement: Five units have spike times out of order in the units table (sub-13 session 1 units
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '700,2000p' /home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/bvfaah03u.txt | grep -v "No change needed\|reason: Agrees\|agrees: true\|outcome:\|^  - claim" ; grep -n "Reproduced\|Partial" README.md | head -3
```

```
fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
      fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
    reason: Cell 26 gives t(45) = -4.28. With 2,000,000 sign flips, 119 exceed the observed t, so p =
      5.95e-05 with a 95% upper bound of 7.02e-05; over 100 seeds of 10,000 permutations, 63 give p below
      0.0001. Using more permutations than the claims file's 10,000 is recorded as a deviation and is
      reasonable, as 10,000 permutations cannot tell whether p is below 0.0001.
      fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
      fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
      fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
      fig1c, fig1e, ltm-rt-confidence, fig1f and fig1g), so the table accounts for 28 of the 29 claims.
    response: The README row now says six claims.
      with a true-onset advantage have it by a single unit (cell 45), and three sessions, holding 10 units,
      are assumed to share the clock without evidence; this affects few units and does not change an outcome.
    reason: 'Agrees. The note citing an earlier O-M run (17.29 and 7.79) cannot be checked, because this
      notebook does not print it. The verifier''s round-1 reason (both effects positive at p < 0.01) is
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 001174-martel-2025-01 001051-bennett-2024-01 001047-silkuniene-2025-01 000715-yemini-2021-01 001027-pakhomov-2023-01; do echo "== $f"; cat docs/pilot-notes/$f.md; done; head -3 docs/pilot-notes/001754-knierim-2000-02.md; grep -n "^| Dandiset\|^| ---" README.md | head; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d))
items = d if isinstance(d,list) else list(d.values())[0] if len(d)==1 else d
import sys
s=json.dumps(d)
" ; grep -n '"001187"' -A15 targets/dandisets.json
```

```
<persisted-output>
Output too large (44.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/buxeouajr.txt

Preview (first 2KB):
== 001174-martel-2025-01
# 001174, Martel et al. 2025

Nine claims reproduced, none partially, one not reproduced and ten blocked on
the dataset, with two more blocked that are on data elsewhere; the link claim
`zenodo-descriptors-link` is not reproduced. The first verification round
agreed with all 23 outcomes and the second with all 23, so there was no third
round. It pins version 0.250331.2218, the version the paper cites and the only
published one; the draft has the same 45 assets with the same sizes. The paper,
Martel, Pittard, Devergnas, Risk, Nassi, Yu, Downer, Wichmann and Galvan in
iScience, images four rhesus macaques (F, Q, U and V) with a nVista3 miniscope
through a GRIN lens in SMA and a prism in M1, compares event rate, IEI CV and
amplitude of CNMFe cells between spontaneous imaging and an arm-reaching task
(Figure 1), classifies cells by their response to target and movement onset
(Figure 2 and Figure S1), measures pairwise synchrony with a Z-Jaccard index
(Figure 3) and detects sequences of activity (Figure 4). The claims were
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/00c94efb-768b-467c-b7d2-cc7931a1f2c2/tool-results/buxeouajr.txt"
}
```

```
1	== 001174-martel-2025-01
2	# 001174, Martel et al. 2025
3	
4	Nine claims reproduced, none partially, one not reproduced and ten blocked on
5	the dataset, with two more blocked that are on data elsewhere; the link claim
6	`zenodo-descriptors-link` is not reproduced. The first verification round
7	agreed with all 23 outcomes and the second with all 23, so there was no third
8	round. It pins version 0.250331.2218, the version the paper cites and the only
9	published one; the draft has the same 45 assets with the same sizes. The paper,
10	Martel, Pittard, Devergnas, Risk, Nassi, Yu, Downer, Wichmann and Galvan in
11	iScience, images four rhesus macaques (F, Q, U and V) with a nVista3 miniscope
12	through a GRIN lens in SMA and a prism in M1, compares event rate, IEI CV and
13	amplitude of CNMFe cells between spontaneous imaging and an arm-reaching task
14	(Figure 1), classifies cells by their response to target and movement onset
15	(Figure 2 and Figure S1), measures pairwise synchrony with a Z-Jaccard index
16	(Figure 3) and detects sequences of activity (Figure 4). The claims were
17	written from the version of record in Europe PMC (PMC12192352) without its
18	supplement, and from the paper's code on Zenodo, whose parameter values for
19	the sequence detection are not recorded. The dandiset gives no cross-session
20	cell identity, so each cell's first occurrence was taken from the paper's
[... 614 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 4870,4920p targets/dandisets.json; head -c 6000 claims/001187/*.yaml; grep -n "^  - id:\|^- id:\|data:" claims/001187/*.yaml | head -80
```

```
{
   "dandiset": "001187",
   "name": "Data for: Daume et al. (2024) \"Persistent activity during working memory maintenance predicts long-term memory formation in the human hippocampus\"",
   "published_version": "0.240904.2347",
   "asset_count": 46,
   "size_gb": 20.67,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Homo sapiens - Human"
   ],
   "approaches": [
    "electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.1101/2024.07.15.603630v1",
     "title": "Persistent activity during working memory maintenance predicts long-term memory formation in the human hippocampus",
     "relation": "IsSourceOf",
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001187; grep -c "data: elsewhere" ../../claims/001187/*.yaml; wc -w *-report.md; cat author-report.md
```

```
0
  337 answer-report.md
  585 author-answers-report.md
  788 author-report.md
  572 author-revise-1-report.md
  455 author-revise-2-report.md
  327 claims-check-report.md
  716 claims-report.md
 1576 verifier-1-report.md
  852 verifier-2-report.md
 6208 total
I finished steps 1 to 5 of the Author section and ran the handover (step 6) at 08:21 UTC. `python tools/entry.py all` passes: 0 errors, and the notebook runs in 6.9 min. I did not verify my own work, and nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| sessions-and-neurons | reproduced (46 sessions, 950 units; 351 and 532 after the rate filter) |
| table-s1-counts | partially reproduced (unit counts match in 42 of 46 sessions) |
| behaviour-overall-accuracy, fig1c, fig1e, ltm-rt-confidence, fig1f, fig1g | reproduced |
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001187; for f in answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat $f-report.md; done
```

```
=== answer
There was one question, on fig3a-area-interactions, and it also covered eight other GLM claims. I changed the claims file in part.

**Answer:** The Methods outlier rule does apply to the GLMs. The sentence "Before each test, we removed neurons ..." comes right after "or mixed-effects GLMs (fitglme.m in MATLAB)", so it is not limited to the t-tests as the question argued. But the Methods don't say what value to compare when a GLM has a continuous term. The claims file's O-M rule (one value per neuron and condition) was the claims file's own reading, not the paper's.

The paper's code for the Fig. 3a GLM (`NWB_computeGLM.m`, commit 6d07204, which I read) settles that: one value per neuron, its mean normalised rate over all its rows. Where the code then departs from the Methods, I kept the Methods, as protocol step 2 says. The code's cut-off is 3 SD with no centring and on the upper side only, while the Methods say "±3 SD from the mean".

**What changed in the claims file:**
- **Header rule O:** it now defines a new rule, O-G: the code's per-neuron means, with neurons removed when they fall outside mean ± 3 SD of those means. O-G is the main reading for the GLMs of Figures 2 and 3. The code's rule (O-C) is a variant, and O-M is no longer a reading for those GLMs.
- **fig3a-area-interactions and fig3b-hippocampus-predicts-ltm:** their criteria now name O-G.
- **The other seven claims** (fig2b, fig2c, fig2e, fig2f, fig3b-amygdala-no-prediction, fig3g, fig3h) pick up O-G through the header rule.
- **Unchanged:** expected values and grading rules. O-M still applies to the permutation t-tests and to the Figure 4 GLMs, which the question did not cover.

O-G is a third rule that this attempt has not computed, so the author will need to run it. It should be very close to O-C, but that is my expectation, not a result.

`questions/001187.yaml` now has the answer and `answered: 2026-11-01`. `python tools/claims_check.py` reports 0 problems. Nothing is committed or push
[... 171 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001187-daume-2024-01.md",
 "content": "# 001187, Daume et al. 2024\n\nNineteen claims reproduced, four partially, two not reproduced and four\nblocked, all on the dataset. The first verification round agreed with 25 of\nthe 29 outcomes as they stood and the second with all 29, so there was no\nthird round. It pins version 0.240904.2347, the version the paper cites and\nthe only published one. The paper, Daume, Kaminski, Salimpour, Gomez Palacio\nSchjetnan, Anderson, Valiante, Mamelak and Rutishauser, \"Persistent activity\nduring working memory maintenance predicts long-term memory formation in the\nhuman hippocampus\" in Neuron, records single units in the hippocampus and\namygdala of epilepsy patients during a Sternberg working memory (WM) task\nfollowed by a long-term memory (LTM) recognition test with confidence ratings,\nand reports that persistent activity of category neurons in the hippocampus\nduring maintenance predicts later recognition. The claims were written from\nthe accepted author manuscript in PubMed Central (PMC11624075) with its\nsupplement, and from the paper's code, SBCAT-NO-release-NWB at commit 6d07204,\nwhich covers the behaviour plots, the neuron selections and the Fig. 3a GLM\nbut not Fig. 2, Fig. 3b to 3h or Fig. 4. The session and unit counts, the\nbehaviour of Figure 1 (six claims), the category and memory-selective neuron\ncounts and most of Figures 3 and 4 reproduce; `fig3b-hippocampus-predicts-ltm`\ngives 21.25, 67.37 and -30.69, all within tolerance. `table-s1-counts` is\npartial, 42 of 46 sessions matching Table S1's unit counts.\n`fig2b-hippocampus-persistent` and `fig3a-area-interactions` are partial, the\neffects significant with the paper's signs but betas outside tolerance (Fig. 3a\n19.12, 70.57 and -32.52, where the code's own outlier rule gives 16.60, 56.61\nand -27.83, within tolerance). `fig3e-early-delay-cluster` is partial, the\nsignificant cluster lying at about 0.875 to 1.05 s and not 0 to 650 ms, so the\ndata do not support an early effect. `fig3c-hippocampus-high-confidence` is not\nreproduced (t(68) = 1.17, p = 0.26 normalized; t(70) = 1.79, p = 0.078 in\nspikes per second), with 80 neurons having both conditions before any removal\nagainst 83 in the paper, so the paper's rows likely differ.\n`fig4e-fs-strong-maintenance` is not reproduced, strong below weak in all 16\nGLM and all 8 t-test readings. `fig2c-hippocampus-correct-load`,\n`fig2e-amygdala-persistent`, `fig2f-amygdala-load-not-accuracy` and\n`fig4f-ns-no-effect` are blocked as `methods_underspecified`, the readings the\ncriterion names giving different outcomes. The author's first run gave fig1d\nas partial, fig2c, fig3h and fig4e as not reproduced, fig2b, fig2e, fig2f,\nfig3a and fig3b-hippocampus as partial, fig4f as reproduced on an assumption\nand fig4d as blocked as `metadata_insufficient`. The author asked a reader\nwhether the code's outlier rule should be the main reading for the GLMs; the\nreader answered that the Methods rule applies, on the code's per-neuron means\n(rule O-G), and the following author run reran the nine GLM claims of Figures\n2 and 3, changing six outcomes. Round 1 disagreed with fig2c, fig2e, fig2f and\nfig4f, which the claims file blocks when readings disagree, found that the\nfig1d grade depended on the permutation seed, and asked for the new LTM\npictures to be labelled by viewing them; in reply those four were blocked,\nfig1d became reproduced with 2,000,000 permutations (p = 6.0e-05), fig4d\nbecame reproduced after all 600 new images of the three task variants were\nviewed, and a question was put to a reader on the 0/1 coding of reading (b) in\nfig2c and fig2f. Round 2 agreed with every outcome and found sentences the\noutputs did not support (a smallest cluster p of 0.43, the location of the\nfig3e peaks, two sessions per variant said to hold identical images, a README\nrow counting five behaviour claims, and record notes citing earlier O-M runs),\nwhich were corrected. The author's run took 1 h 04 min (07:17 to 08:21 UTC);\nthe default statsmodels optimizer once stopped at a poorer fit, so three\noptimizers are run and the best fit kept. The notebook ran in 6.9 min at\nfirst, 648 s after the answer, 880 s after round 1 and about 18 min after\nround 2.\n\nTable S1's recorded unit counts sum to 973 (386 hippocampus, 587 amygdala),\nwhile the Methods say 950 units were isolated; the dandiset holds 950, and\nfour sessions have fewer units than Table S1 lists (P1809jh hippocampus 1\nagainst 6, P61cs_2 hippocampus 1 against 2, P68cs amygdala 7 against 17, P82cs\namygdala 17 against 24). The new pictures of the LTM test (IDs 1001 to 1200)\ncarry no category and their images are named only by ID, so Fig. 4d needed the\nimages to be viewed; in each task variant they form consecutive blocks of 40\nIDs per category, in the order of the old pictures' leading digits. The LTM\nconfidence column is described as 1 to 6 with no coding, though the accuracy\ncolumn agrees in every trial with 1 to 3 meaning new and 4 to 6 old, and one\nLTM trial of sub-24 session 2 has confidence 7. Every file gives Cedars-Sinai\nMedical Center as the institution, though 14 sessions have Toronto Western\nidentifiers and 6 Johns Hopkins identifiers. Five units have spike times out\nof order (sub-13 session 1 units 1 and 2, sub-2 session 2 units 19 and 29,\nsub-24 session 2 unit 10). Eight sessions have fewer than 400 LTM trials (161,\n187, 228, 257, 384, 390, 395, 399) and one has 139 WM trials, where the paper\ndescribes 400 and 140, and picture 1 lasts 1.57 to 2.04 s and the maintenance\nperiod 2.53 to 3.20 s, where the Methods say 2 s and 2.55 to 2.85 s. The\npaper's code for the Fig. 3a GLM (NWB_computeGLM.m) removes outlier neurons\nabove 3 SD of the neuron means, without centring and on the upper side only,\nwhere the Methods remove neurons more than 3 SD from the mean, and it keeps\nthe session whose ratings are all sure, which the Results say was excluded.\nQuestions are put to the paper's authors: which outlier rule was applied to\nthe mixed-effects GLMs and on which values, whether the Fig. 2 GLMs used one\nrow per trial or per picture and which baseline, whether Fig. 2c and 2f were\nfitted with main effects only or with the interaction and with which coding;\nand, for the Fig. 4e and 4f GLM, whose Methods sentence lost its variable\nnames, which unit was the random intercept, which LTM trials were used and\nwhether a neuron was paired with itself.\n\nThe author's points on the protocol: the claims file says to block a claim\nwhose readings disagree while step 1.6 allows adopting a reading as an\nassumption, and the protocol was followed at first; neither the protocol nor\nthe claims file says how a per-condition outlier rule applies to a GLM, and\ntwo readings were run and a reader asked; reference numbers needed only for\ncomparison, such as Table S1, have no place, and they were put in the helper\nas a labelled table; the protocol does not say whether an inference from the\nneural data, such as the picture-category blocks, may be used, and it was\nshown as a variant only; and a presigned DANDI download URL refuses HEAD\nrequests, which `docs/archives.md` does not mention.\n"
}
```

```
File created successfully at: docs/pilot-notes/001187-daume-2024-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather\|\*\*" docs/pilot-notes/001187-daume-2024-01.md; git status --short
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
?? docs/pilot-notes/001187-daume-2024-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/001187-daume-2024-01.md` and changed no other file. The other untracked files in the repo root (dotfiles, `.idea`, `.vscode`, `scripts`) were there before; the author's report mentions them. Nothing is committed. The subsection:

# 001187, Daume et al. 2024

Nineteen claims reproduced, four partially, two not reproduced and four blocked, all on the dataset. The first verification round agreed with 25 of the 29 outcomes as they stood and the second with all 29, so there was no third round. It pins version 0.240904.2347, the version the paper cites and the only published one. The paper, Daume, Kaminski, Salimpour, Gomez Palacio Schjetnan, Anderson, Valiante, Mamelak and Rutishauser, "Persistent activity during working memory maintenance predicts long-term memory formation in the human hippocampus" in Neuron, records single units in the hippocampus and amygdala of epilepsy patients during a Sternberg working memory (WM) task followed by a long-term memory (LTM) recognition test with confidence ratings, and reports that persistent activity of category neurons in the hippocampus during maintenance predicts later recognition. The claims were written from the accepted author manuscript in PubMed Central (PMC11624075) with its supplement, and from the paper's code, SBCAT-NO-release-NWB at commit 6d07204, which covers the behaviour plots, the neuron selections and the Fig. 3a GLM but not Fig. 2, Fig. 3b to 3h or Fig. 4. The session and unit counts, the behaviour of Figure 1 (six claims), the category and memory-selective neuron counts and most of Figures 3 and 4 reproduce; `fig3b-hippocampus-predicts-ltm` gives 21.25, 67.37 and -30.69, all within tolerance. `table-s1-counts` is partial, 42 of 46 sessions matching Table S1's unit counts. `fig2b-hippocampus-persistent` and `fig3a-area-interactions` are partial, the effects significant with the paper's signs but betas outside tolerance (Fig. 3a 19.12, 70.57 and -32.52, where the code's own outlier rule gives 16.60, 56.61 and -27.83, within tolerance). `fig3e-early-delay-cluster` is partial, the significant cluster lying at about 0.875 to 1.05 s and not 0 to 650 ms, so the data do not support an early effect. `fig3c-hippocampus-high-confidence` is not reproduced (t(68) = 1.17, p = 0.26 normalized; t(70) = 1.79, p = 0.078 in spikes per second), with 80 neurons having both conditions before any removal against 83 in the paper, so the paper's rows likely differ. `fig4e-fs-strong-maintenance` is not reproduced, strong below weak in all 16 GLM and all 8 t-test readings. `fig2c-hippocampus-correct-load`, `fig2e-amygdala-persistent`, `fig2f-amygdala-load-not-accuracy` and `fig4f-ns-no-effect` are blocked as `methods_underspecified`, the readings the criterion names giving different outcomes. The author's first run gave fig1d as partial, fig2c, fig3h and fig4e as not reproduced, fig2b, fig2e, fig2f, fig3a and fig3b-hippocampus as partial, fig4f as reproduced on an assumption and fig4d as blocked as `metadata_insufficient`. The author asked a reader whether the code's outlier rule should be the main reading for the GLMs; the reader answered that the Methods rule applies, on the code's per-neuron means (rule O-G), and the following author run reran the nine GLM claims of Figures 2 and 3, changing six outcomes. Round 1 disagreed with fig2c, fig2e, fig2f and fig4f, which the claims file blocks when readings disagree, found that the fig1d grade depended on the permutation seed, and asked for the new LTM pictures to be labelled by viewing them; in reply those four were blocked, fig1d became reproduced with 2,000,000 permutations (p = 6.0e-05), fig4d became reproduced after all 600 new images of the three task variants were viewed, and a question was put to a reader on the 0/1 coding of reading (b) in fig2c and fig2f. Round 2 agreed with every outcome and found sentences the outputs did not support (a smallest cluster p of 0.43, the location of the fig3e peaks, two sessions per variant said to hold identical images, a README row counting five behaviour claims, and record notes citing earlier O-M runs), which were corrected. The author's run took 1 h 04 min (07:17 to 08:21 UTC); the default statsmodels optimizer once stopped at a poorer fit, so three optimizers are run and the best fit kept. The notebook ran in 6.9 min at first, 648 s after the answer, 880 s after round 1 and about 18 min after round 2.

Table S1's recorded unit counts sum to 973 (386 hippocampus, 587 amygdala), while the Methods say 950 units were isolated; the dandiset holds 950, and four sessions have fewer units than Table S1 lists (P1809jh hippocampus 1 against 6, P61cs_2 hippocampus 1 against 2, P68cs amygdala 7 against 17, P82cs amygdala 17 against 24). The new pictures of the LTM test (IDs 1001 to 1200) carry no category and their images are named only by ID, so Fig. 4d needed the images to be viewed; in each task variant they form consecutive blocks of 40 IDs per category, in the order of the old pictures' leading digits. The LTM confidence column is described as 1 to 6 with no coding, though the accuracy column agrees in every trial with 1 to 3 meaning new and 4 to 6 old, and one LTM trial of sub-24 session 2 has confidence 7. Every file gives Cedars-Sinai Medical Center as the institution, though 14 sessions have Toronto Western identifiers and 6 Johns Hopkins identifiers. Five units have spike times out of order (sub-13 session 1 units 1 and 2, sub-2 session 2 units 19 and 29, sub-24 session 2 unit 10). Eight sessions have fewer than 400 LTM trials (161, 187, 228, 257, 384, 390, 395, 399) and one has 139 WM trials, where the paper describes 400 and 140, and picture 1 lasts 1.57 to 2.04 s and the maintenance period 2.53 to 3.20 s, where the Methods say 2 s and 2.55 to 2.85 s. The paper's code for the Fig. 3a GLM (NWB_computeGLM.m) removes outlier neurons above 3 SD of the neuron means, without centring and on the upper side only, where the Methods remove neurons more than 3 SD from the mean, and it keeps the session whose ratings are all sure, which the Results say was excluded. Questions are put to the paper's authors: which outlier rule was applied to the mixed-effects GLMs and on which values, whether the Fig. 2 GLMs used one row per trial or per picture and which baseline, whether Fig. 2c and 2f were fitted with main effects only or with the interaction and with which coding; and, for the Fig. 4e and 4f GLM, whose Methods sentence lost its variable names, which unit was the random intercept, which LTM trials were used and whether a neuron was paired with itself.

The author's points on the protocol: the claims file says to block a claim whose readings disagree while step 1.6 allows adopting a reading as an assumption, and the protocol was followed at first; neither the protocol nor the claims file says how a per-condition outlier rule applies to a GLM, and two readings were run and a reader asked; reference numbers needed only for comparison, such as Table S1, have no place, and they were put in the helper as a labelled table; the protocol does not say whether an inference from the neural data, such as the picture-category blocks, may be used, and it was shown as a variant only; and a presigned DANDI download URL refuses HEAD requests, which `docs/archives.md` does not mention.

## End of run

12 turns, 1 minutes, result: success.
