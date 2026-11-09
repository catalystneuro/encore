# 000129 · recorder · run 40801324939

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/000129/ claims/000129/; python tools/readme_row.py 000129; cat attempts/000129-makin-2018-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000129' in json.dumps(e): print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (265.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7f52de93-c4d2-4a39-8bf2-4f9ca42b4d9b/tool-results/bbtpz9fbu.txt

Preview (first 2KB):
docs/pilot-notes/000138-churchland-2010-01.md
docs/pilot-notes/000139-churchland-2010-01.md
docs/pilot-notes/000233-tingley-2021-01.md
docs/pilot-notes/openneuro-ds000228-richardson-2018-01.md
docs/pilot-notes/openneuro-ds004752-dimakopoulos-2022-01.md
claims/000129/:
10.1088-1741-2552-aa9e95.yaml

transcripts/000129/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000129-makin-2018-01.yaml; for f in 000138-churchland-2010-01 000139-churchland-2010-01 000233-tingley-2021-01 openneuro-ds000228-richardson-2018-01 openneuro-ds004752-dimakopoulos-2022-01 001754-knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else len(d))"
```

```
<persisted-output>
Output too large (91.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7f52de93-c4d2-4a39-8bf2-4f9ca42b4d9b/tool-results/bj4fu06w9.txt

Preview (first 2KB):
schema_version: 2
id: 000129-makin-2018-01
dataset:
  archive: dandi
  id: "000129"
  version: 0.241017.1444
  doi: 10.48324/dandi.000129/0.241017.1444
paper: doi:10.1088/1741-2552/aa9e95
date: 2026-10-28
entry: 000129-makin-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7f52de93-c4d2-4a39-8bf2-4f9ca42b4d9b/tool-results/bj4fu06w9.txt"
}
```

```
1	schema_version: 2
2	id: 000129-makin-2018-01
3	dataset:
4	  archive: dandi
5	  id: "000129"
6	  version: 0.241017.1444
7	  doi: 10.48324/dandi.000129/0.241017.1444
8	paper: doi:10.1088/1741-2552/aa9e95
9	date: 2026-10-28
10	entry: 000129-makin-2018
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
[... 853 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7f52de93-c4d2-4a39-8bf2-4f9ca42b4d9b/tool-results/bj4fu06w9.txt",
 "offset": 874,
 "limit": 620
}
```

```
874	      sessions.
875	    response: No change.
876	  - claim: fig8-gaussian-still-beats-ukf
877	    agrees: true
878	    outcome: reproduced
879	    reason: Agrees. The assumption of standardized counts is stated, is the claims file's main reading
880	      and the Results' (first standardizing the data, separately for each neuron), and is reasonable;
881	      the code's transform reverses the outcome (velocity -0.43 dB against the UKF).
882	    response: No change.
883	  - claim: fig9-taps
884	    agrees: true
885	    outcome: blocked
886	    reason: Agrees. Every grade of its criterion needs part (ii), so it stays blocked whatever parts (i)
887	      and (iii) give, and the record now states this. No single-session values are printed for it, although
888	      the README says they are printed for all 12.
889	    response: The README row now says single-session values are printed for ten of the twelve. The tapped
890	      decoders are still not implemented, for the reason in the notes.
891	  - claim: kflatent-modest
892	    agrees: true
893	    outcome: reproduced
[... 590 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "000129" README.md | head; grep -n -B2 -A2 "^| Dandiset\|^| Dataset" README.md | head -20; python -c "
import json;d=json.load(open('targets/dandisets.json'))
for e in d['targets']:
  if '000129' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"; head -60 claims/000129/*.yaml; grep -n "data:\|^  - id:\|^- id:" claims/000129/*.yaml | head -80
```

```
{
 "dandiset": "000129",
 "name": "MC_RTT: Macaque motor cortex spiking activity during self-paced reaching (Superior arm-movement decoding from cortex)",
 "published_version": "0.241017.1444",
 "asset_count": 2,
 "size_gb": 0.05,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rhesus monkey"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1088/1741-2552/aa9e95",
   "title": "Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm",
   "relation": "IsDescribedBy",
[... 98 more lines not kept]
```

**Agent**

Gathered the attempt record and the format of recent notes. Now reading the run reports.

**Agent calls Bash**

```bash
cd transcripts/000129; ls -la --time-style=+%T; wc -w *-report.md; cat author-report.md
```

```
total 588
drwxr-xr-x   2 runner runner   4096 01:35:49 .
drwxr-xr-x 231 runner runner   4096 01:35:49 ..
-rw-r--r--   1 runner runner    948 01:35:49 answer-report.md
-rw-r--r--   1 runner runner   5155 01:35:49 answer.md
-rw-r--r--   1 runner runner   1735 01:35:49 author-answers-report.md
-rw-r--r--   1 runner runner  11971 01:35:49 author-answers.md
-rw-r--r--   1 runner runner   5111 01:35:49 author-report.md
-rw-r--r--   1 runner runner   3460 01:35:49 author-revise-1-report.md
-rw-r--r--   1 runner runner 123377 01:35:49 author-revise-1.md
-rw-r--r--   1 runner runner   3068 01:35:49 author-revise-2-report.md
-rw-r--r--   1 runner runner  41143 01:35:49 author-revise-2.md
-rw-r--r--   1 runner runner 188514 01:35:49 author.md
-rw-r--r--   1 runner runner   3798 01:35:49 claims-check-report.md
-rw-r--r--   1 runner runner  36465 01:35:49 claims-check.md
-rw-r--r--   1 runner runner   3853 01:35:49 claims-report.md
-rw-r--r--   1 runner runner  63312 01:35:49 claims.md
-rw-r--r--   1 runner runner  10949 01:35:49 verifier-1-report.md
-rw-r--r--   1 runner runner  28254 01:35:49 verifier-1.md
-rw-r--r--   1 runner runner   6917 01:35:49 verifier-2-report.md
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000129; for f in answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== answer-report.md
I made no changes because there were no questions to answer. `questions/000129.yaml` does not exist, and git history on every branch shows it was never created.

The author run (commit 9a22704cb) did not raise any questions for a reader. Neither its report (`transcripts/000129/author-report.md`) nor the attempt file (`attempts/000129-makin-2018-01.yaml`) says the claims file misreads the paper or points to a questions file. The attempt does raise several questions, but they are for the paper's authors: which kinematics were decoded, which input went into a figure 8 comparison, and whether the UKF2 code and its ridge setting can be shared. Under the protocol (Author, step 1.6) those go in the claim notes and as `methods_unavailable` findings, so they are not mine to settle.

I did not create a questions file or touch `claims/000129/`, and I did not run `tools/claims_check.py` because no quotes changed. Nothing was committed or pushed.
=== author-answers-report.md
I re-ran nothing and changed no claim, notebook or record, because there were no questions to answer.

**The questions.** `questions/000129.yaml` does not exist, and git history shows it was never created. My first author run (commit 9a22704cb) asked no reader anything. It found no place where the claims file misreads the paper. The open questions it did raise are for the paper's authors, not a reader, and are recorded as `methods_unavailable` findings in `attempts/000129-makin-2018-01.yaml`:
- which kinematics were decoded;
- which input went into the figure 8 Gaussian-versus-UKF comparison;
- whether the UKF2 code and its ridge setting can be shared.

The answer run (commit ebd0b57ec) came to the same conclusion and made no changes. `claims/000129/` was last changed by the claims-check run, before my author run.

**Effect per claim.** Every outcome stays as the first author run recorded it, and no claim's notes needed an update.

**Entry checks.**
- `python tools/entry.py lock` rewrote
[... 187 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/000129-makin-2018-01.md",
 "content": "# 000129, Makin et al. 2018\n\nTen claims reproduced, two partially, six not reproduced and twelve blocked on\nthe dataset; `fig4-task-similar`, which needs monkey C's data from elsewhere,\nis counted apart and blocked as `other`, as those data are named only by a\npreprint with no archive identifier to pin. It pins version 0.241017.1444, its\nonly published version; the draft holds the same two assets and differs only\nin its title. The paper, Makin, O'Doherty, Cardoso and Sabes in the Journal of\nNeural Engineering, decodes arm movements from motor cortex in 49 sessions of\nthree monkeys and compares a new unsupervised decoder, the rEFH, with Kalman\nfilters, an unscented Kalman filter (UKF), a Wiener filter (WF) and linear\nregression. The claims were written from the version of record, which has no\nsupplement, and from the paper's code (jgmakin/rbmish at commit 700062f). The\nper-session statements were tested on the dandiset's one session: the unit\ncount, the decoder comparisons of Figures 2 and 4, the effects of bin width,\ntraining time and number of units in Figures 5 to 7, and the variant decoders\nof Figure 8. The eleven claims that need the bootstrap or regression across\nthe paper's 49 sessions are blocked as `data_missing`, with their\nsingle-session values printed for nine of them; `fig9-taps` is among them, and\nits tapped decoders were not implemented. `units-monkey-i` is not reproduced\n(111 units above 0.5 Hz against 153.9 to 454.3), `fig2-position-dynamic-gain`\nis not reproduced (4.45 dB against 3 +- 0.5), and `fig4-best-variable` is not\nreproduced, as position is the best-decoded variable for the rEFH (+KF). The\nauthor asked a reader no questions, so the answer run and the following author\nrun changed nothing; two questions were put to a reader during the revisions,\nafter the answer step, on whether `fig2-gross-failures` should cover every\nconfiguration the paper ran and whether the claims that need the paper's\nsessions should use its Zenodo deposit. Round 1 agreed with 29 of 31 outcomes;\nthe author took its `data_missing` reason in place of `too_large` for the\nclaims needing the other sessions, kept `fig2-sagittal-better` partially\nreproduced where the verifier gave reproduced (this run gives 23 of 24 pairs,\nthe verifier's copy from an earlier run 24), and kept\n`fig4-vel-acc-every-session` reproduced, resting on its per-session part, where\nthe verifier gave partially reproduced. Its points led to the Methods' EM\nstopping threshold of 1e-4 in place of 1e-6 (every run still reached the\n100-epoch limit), two more EM seeds, Wiener filter history taken from the last\ntraining bins, training and test R2 of the static rEFH map, and a list of every\nnegative R2 outside 64 ms. Round 2 agreed with all 31, dropping its round-1\ndisagreement on `fig4-vel-acc-every-session`, so there was no third round; it\nfound statements the outputs did not support, among them \"all four runs\"\nwhere six are printed, \"no negative R2 at all\" where there is none only at 64\nms, and inconsistent ranges for the last EM gain, which were corrected. Some\noutcomes rest on weak ground: `fig7-kinematic-model-saturates` passes only\nbecause the KFlatent (+KF) filter diverges at f = 1/8 (-76.63 dB), and without\nthat value fails under both readings; `fig2-velocity-boost` has a KFobs ratio\nof 1.92 against the required 2, and 2.05 with the code's kinematics;\n`fig2-refh-static-vel-acc` has a velocity margin of 0.05 dB and `kflatent-modest`\nmargins of 0.07 to 0.10 dB; and `fig2-gross-failures` holds trivially, as no R2\nis negative at 64 ms. The author's run finished at 21:00 UTC; a background\ndevelopment run was killed with its sandbox, costing about 20 minutes, and\neverything after ran in the foreground. The two notebooks ran in 604 s and\n1301 s at first and in 662 s and 1295 s after round 1.\n\nThe dandiset holds one session of monkey I (M1 array, 649.1 s with\nkinematics), released for the Neural Latents Benchmark, where the paper used\n49 sessions of three monkeys, so the paper's tests across sessions cannot be\nrun on it. The file dates the session 2017-02-02, which is not in the paper's\nlist of monkey I sessions (ending 2017-01-31), so it is probably not one of the\npaper's sessions, though the dandiset names the paper as describing it; the\npaper's own sessions are on Zenodo (doi:10.5281/zenodo.583331). The units table\nholds sorted units only, where the paper kept an unsorted hash unit for every\nchannel and counted them among its 171 to 413 units per monkey I session;\nwithout them 111 units pass the 0.5 Hz cut. The training file has three gaps\nof 0.1 s where every behavioural series is NaN and no unit has a spike, and\nneither the file nor the dandiset says what was removed. The test file (190.3\ns, 98 units) has no kinematics, so it cannot be used to score decoding. The\nMethods decode the fingertip position low-pass filtered at 10 Hz and\nsubsampled per bin, while the paper's code decodes the cursor position with\nthe filter commented out and averages each bin, and the two readings change\nthe outcome of `fig2-velocity-boost`. The Results say the standard-normal rEFH\nvariant was trained on standardized spike counts, while the code feeds it 2\nsqrt(R + 3/8), and the two readings change the outcome of\n`fig8-gaussian-still-beats-ukf`. The UKF follows Li's UKF2 package, which the\npaper's repository calls but does not hold, so it was re-implemented from the\npaper's description and cannot be checked against the original. Three\nquestions are put to the paper's authors: which kinematics were decoded, which\ninput the standard-normal variant used for Figure 8, and whether the UKF2 code\nand its ridge setting can be published with the paper's code.\n\nThe author's points on the protocol: it gives no block reason for claims on\nthe dataset that need sessions public elsewhere, so `too_large` was used\nfirst; it does not say how to grade a criterion of which only one part can be\ntested, so the testable part was graded and the rest listed as a deviation; it\ndoes not say how to record a criterion that holds trivially; its rule that\neach claim's section has its own generator does not fit claims that share one\ncostly fit, so each fit configuration was seeded; it treats a seed as a detail\nthat cannot change an outcome, though here it can; and the repository root\nhas untracked files from the sandbox.\n"
}
```

```
File created successfully at: docs/pilot-notes/000129-makin-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000129-makin-2018-01.md",
 "old_string": "of Figure 8. The eleven claims that need the bootstrap or regression across\nthe paper's 49 sessions are blocked as `data_missing`, with their\nsingle-session values printed for nine of them; `fig9-taps` is among them, and\nits tapped decoders were not implemented.",
 "new_string": "of Figure 8. The twelve claims that need the bootstrap or regression across\nthe paper's 49 sessions are blocked as `data_missing`, with their\nsingle-session values printed for ten of them; `fig9-taps` is among them, and\nits tapped decoders were not implemented."
}
```

```
The file docs/pilot-notes/000129-makin-2018-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000129-makin-2018-01.md",
 "old_string": "Neural Engineering, decodes arm movements from motor cortex in 49 sessions of",
 "new_string": "Neural Engineering, decodes arm movements from cortex in 49 sessions of"
}
```

```
The file docs/pilot-notes/000129-makin-2018-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  git status --short; grep -n -- "—\|rather" docs/pilot-notes/000129-makin-2018-01.md; cat docs/pilot-notes/000129-makin-2018-01.md
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
?? docs/pilot-notes/000129-makin-2018-01.md
?? scripts
# 000129, Makin et al. 2018

Ten claims reproduced, two partially, six not reproduced and twelve blocked on
the dataset; `fig4-task-similar`, which needs monkey C's data from elsewhere,
is counted apart and blocked as `other`, as those data are named only by a
preprint with no archive identifier to pin. It pins version 0.241017.1444, its
only published version; the draft holds the same two assets and differs only
in its title. The paper, Makin, O'Doherty, Cardoso and Sabes in the Journal of
[... 80 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/000129-makin-2018-01.md",
 "old_string": "does not say how to record a criterion that holds trivially; its rule that\neach claim's section has its own generator does not fit claims that share one\ncostly fit, so each fit configuration was seeded; it treats a seed as a detail\nthat cannot change an outcome, though here it can; and the repository root\nhas untracked files from the sandbox.",
 "new_string": "does not cover a criterion that holds trivially, which was recorded as\nreproduced with the notes saying so; its rule that each claim's section has\nits own generator does not fit claims that share one costly fit, so each fit\nconfiguration was seeded; and it treats a seed as a detail that cannot change\nan outcome, though here one can, so seed 0 was kept and the others reported."
}
```

```
The file docs/pilot-notes/000129-makin-2018-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I wrote `docs/pilot-notes/000129-makin-2018-01.md` and changed no other file. The `catalystneuro` field for 000129 is empty, so the second paragraph does not open with the conversion sentence.

Two of the reports give counts that do not match the attempt record. The author-revise-2 and verifier-2 reports say 9 reproduced and 7 not reproduced. The record has 10 and 6, and so does `tools/readme_row.py`. The note follows the record.

```markdown
# 000129, Makin et al. 2018

Ten claims reproduced, two partially, six not reproduced and twelve blocked on
the dataset; `fig4-task-similar`, which needs monkey C's data from elsewhere,
is counted apart and blocked as `other`, as those data are named only by a
preprint with no archive identifier to pin. It pins version 0.241017.1444, its
only published version; the draft holds the same two assets and differs only
in its title. The paper, Makin, O'Doherty, Cardoso and Sabes in the Journal of
Neural Engineering, decodes arm movements from cortex in 49 sessions of
three monkeys and compares a new unsupervised decoder, the rEFH, with Kalman
filters, an unscented Kalman filter (UKF), a Wiener filter (WF) and linear
regression. The claims were written from the version of record, which has no
supplement, and from the paper's code (jgmakin/rbmish at commit 700062f). The
per-session statements were tested on the dandiset's one session: the unit
count, the decoder comparisons of Figures 2 and 4, the effects of bin width,
training time and number of units in Figures 5 to 7, and the variant decoders
of Figure 8. The twelve claims that need the bootstrap or regression across
the paper's 49 sessions are blocked as `data_missing`, with their
single-session values printed for ten of them; `fig9-taps` is among them, and
its tapped decoders were not implemented. `units-monkey-i` is not reproduced
(111 units above 0.5 Hz against 153.9 to 454.3), `fig2-position-dynamic-gain`
is not reproduced (4.45 dB against 3 +- 0.5), and `fig4-best-variable` is not
reproduced, as position is the best-decoded variable for the rEFH (+KF). The
author asked a reader no questions, so the answer run and the following author
run changed nothing; two questions were put to a reader during the revisions,
after the answer step, on whether `fig2-gross-failures` should cover every
configuration the paper ran and whether the claims that need the paper's
sessions should use its Zenodo deposit. Round 1 agreed with 29 of 31 outcomes;
the author took its `data_missing` reason in place of `too_large` for the
claims needing the other sessions, kept `fig2-sagittal-better` partially
reproduced where the verifier gave reproduced (this run gives 23 of 24 pairs,
the verifier's copy from an earlier run 24), and kept
`fig4-vel-acc-every-session` reproduced, resting on its per-session part, where
the verifier gave partially reproduced. Its points led to the Methods' EM
stopping threshold of 1e-4 in place of 1e-6 (every run still reached the
100-epoch limit), two more EM seeds, Wiener filter history taken from the last
training bins, training and test R2 of the static rEFH map, and a list of every
negative R2 outside 64 ms. Round 2 agreed with all 31, dropping its round-1
disagreement on `fig4-vel-acc-every-session`, so there was no third round; it
found statements the outputs did not support, among them "all four runs"
where six are printed, "no negative R2 at all" where there is none only at 64
ms, and inconsistent ranges for the last EM gain, which were corrected. Some
outcomes rest on weak ground: `fig7-kinematic-model-saturates` passes only
because the KFlatent (+KF) filter diverges at f = 1/8 (-76.63 dB), and without
that value fails under both readings; `fig2-velocity-boost` has a KFobs ratio
of 1.92 against the required 2, and 2.05 with the code's kinematics;
`fig2-refh-static-vel-acc` has a velocity margin of 0.05 dB and `kflatent-modest`
margins of 0.07 to 0.10 dB; and `fig2-gross-failures` holds trivially, as no R2
is negative at 64 ms. The author's run finished at 21:00 UTC; a background
development run was killed with its sandbox, costing about 20 minutes, and
everything after ran in the foreground. The two notebooks ran in 604 s and
1301 s at first and in 662 s and 1295 s after round 1.

The dandiset holds one session of monkey I (M1 array, 649.1 s with
kinematics), released for the Neural Latents Benchmark, where the paper used
49 sessions of three monkeys, so the paper's tests across sessions cannot be
run on it. The file dates the session 2017-02-02, which is not in the paper's
list of monkey I sessions (ending 2017-01-31), so it is probably not one of the
paper's sessions, though the dandiset names the paper as describing it; the
paper's own sessions are on Zenodo (doi:10.5281/zenodo.583331). The units table
holds sorted units only, where the paper kept an unsorted hash unit for every
channel and counted them among its 171 to 413 units per monkey I session;
without them 111 units pass the 0.5 Hz cut. The training file has three gaps
of 0.1 s where every behavioural series is NaN and no unit has a spike, and
neither the file nor the dandiset says what was removed. The test file (190.3
s, 98 units) has no kinematics, so it cannot be used to score decoding. The
Methods decode the fingertip position low-pass filtered at 10 Hz and
subsampled per bin, while the paper's code decodes the cursor position with
the filter commented out and averages each bin, and the two readings change
the outcome of `fig2-velocity-boost`. The Results say the standard-normal rEFH
variant was trained on standardized spike counts, while the code feeds it 2
sqrt(R + 3/8), and the two readings change the outcome of
`fig8-gaussian-still-beats-ukf`. The UKF follows Li's UKF2 package, which the
paper's repository calls but does not hold, so it was re-implemented from the
paper's description and cannot be checked against the original. Three
questions are put to the paper's authors: which kinematics were decoded, which
input the standard-normal variant used for Figure 8, and whether the UKF2 code
and its ridge setting can be published with the paper's code.

The author's points on the protocol: it gives no block reason for claims on
the dataset that need sessions public elsewhere, so `too_large` was used
first; it does not say how to grade a criterion of which only one part can be
tested, so the testable part was graded and the rest listed as a deviation; it
does not cover a criterion that holds trivially, which was recorded as
reproduced with the notes saying so; its rule that each claim's section has
its own generator does not fit claims that share one costly fit, so each fit
configuration was seeded; and it treats a seed as a detail that cannot change
an outcome, though here one can, so seed 0 was kept and the others reported.
```

## End of run

13 turns, 2 minutes, result: success.
