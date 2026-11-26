# pasquereau-2013 · recorder · run 45896280832

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py pasquereau-2013; ls transcripts/pasquereau-2013/; cat attempts/pasquereau-2013-03.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
import sys
s=json.dumps(d)
" ; grep -n '001636' -A25 targets/dandisets.json | head -40
```

```
<persisted-output>
Output too large (71.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c01238df-5636-4ad2-bd85-c58bba3b1178/tool-results/be478niyh.txt

Preview (first 2KB):
docs/pilot-notes/allen-2026-01.md
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/amjad-2025-02.md
docs/pilot-notes/andreassen-2022-01.md
docs/pilot-notes/andrews-2024-01.md
| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`pasquereau-2013`](entries/pasquereau-2013) |
attempt-01
attempt-02
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c01238df-5636-4ad2-bd85-c58bba3b1178/tool-results/be478niyh.txt"
}
```

```
1	docs/pilot-notes/allen-2026-01.md
2	docs/pilot-notes/amjad-2025-01.md
3	docs/pilot-notes/amjad-2025-02.md
4	docs/pilot-notes/andreassen-2022-01.md
5	docs/pilot-notes/andrews-2024-01.md
6	| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`pasquereau-2013`](entries/pasquereau-2013) |
7	attempt-01
8	attempt-02
9	author-report.md
10	author-revise-1-report.md
11	author-revise-1.md
12	author-revise-2-report.md
13	author-revise-2.md
14	author-revise-3-report.md
15	author-revise-3.md
16	author.md
17	reconcile-report.md
18	reconcile.md
19	verifier-1-report.md
20	verifier-1.md
[... 794 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c01238df-5636-4ad2-bd85-c58bba3b1178/tool-results/be478niyh.txt",
 "offset": 815,
 "limit": 330
}
```

```
815	    agrees: true
816	    outcome: partially_reproduced
817	    reason: Agree (cell 37, CSN p = 0.019, above 0.0167).
818	    response: No change of outcome.
819	  - claim: false-positive-rate
820	    agrees: true
821	    outcome: blocked
822	    reason: Agree. The false-positive rate is 0.230 (cell 40). The trial_sd reading, shown in cells 44 to 58, would
823	      not reproduce torque-related-fractions either (20.0% and 18.5% of M1 cells against 75 and 68% expected, cell
824	      44).
825	    response: No change of outcome.
826	  - claim: torque-related-fractions
827	    agrees: true
828	    outcome: blocked
829	    reason: Agree, blocked with false-positive-rate (cells 40, 44). The notes said Blocked ... through torque-related-fractions,
830	      which names the claim as its own gate.
831	    response: No change of outcome. The notes now say the claim is blocked with false-positive-rate, on which the
832	      selection depends.
833	  - claim: prevalence-unchanged
834	    agrees: true
[... 298 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in allen-2026-01 amjad-2025-01 amjad-2025-02 andreassen-2022-01 andrews-2024-01 knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; sed -n 7008,7040p targets/dandisets.json; ls docs/pilot-notes | grep pasquereau; ls summaries | grep -E 'pasquereau|knierim|amjad'
```

```
<persisted-output>
Output too large (33.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c01238df-5636-4ad2-bd85-c58bba3b1178/tool-results/biduzkpts.txt

Preview (first 2KB):
=== allen-2026-01
# allen-2026, Allen et al. 2026

Fifteen claims reproduced on the dataset, one partially, one not reproduced
and four blocked, all four for missing data; the ten transcriptomic claims,
whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
counted apart, with seven reproduced, two partially and one not reproduced.
One outcome, `fig4a-pca`, rests on an assumption. The first verification round
agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
reproduced where the record had not reproduced, and
`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
where it had reproduced; the author took all three. The second round agreed
with all 31, and nothing was proposed after it, so there was no third round. It
pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
drives behavioral plasticity and visual integration under environmental
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c01238df-5636-4ad2-bd85-c58bba3b1178/tool-results/biduzkpts.txt"
}
```

```
1	=== allen-2026-01
2	# allen-2026, Allen et al. 2026
3	
4	Fifteen claims reproduced on the dataset, one partially, one not reproduced
5	and four blocked, all four for missing data; the ten transcriptomic claims,
6	whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
7	counted apart, with seven reproduced, two partially and one not reproduced.
8	One outcome, `fig4a-pca`, rests on an assumption. The first verification round
9	agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
10	reproduced where the record had not reproduced, and
11	`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
12	where it had reproduced; the author took all three. The second round agreed
13	with all 31, and nothing was proposed after it, so there was no third round. It
14	pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
15	al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
16	drives behavioral plasticity and visual integration under environmental
17	acidification" (Communications Biology 9:229), rears bigfin reef squid at pH
18	8.2, with 7 days at pH 7.8 after 90 days (acute-OA) or at pH 7.8 from hatching
19	(chronic-OA), and reports a higher metabolic rate, lower ammonia excretion and
20	higher blood pH, PCO2 and [HCO3-] under chronic-OA, more time in the upper half
[... 492 more lines not kept]
```

**Agent**

I have the attempt record and the example notes. Next I'm reading the earlier pasquereau notes, the summaries, and the run reports.

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/pasquereau-2013-02.md; echo ====; cat summaries/pasquereau-2013-02.md summaries/amjad-2025-02.md; echo ====; cd transcripts/pasquereau-2013; wc -w *report.md; cat author-report.md
```

```
# 001636, Pasquereau et al. 2013, second attempt

Four claims reproduced, three partially, three not reproduced and eighteen
blocked, all on the dandiset. The attempt was made on the draft of the
dandiset, which holds a new conversion made after pasquereau-2013-01
reported its findings; the claims file is unchanged, and every claim has the
same outcome as in `-01`. The archive listed 4 uploads in progress on the
draft while it was read, and between 23:00 and 23:10 UTC every asset was
uploaded again; the first good run of the first revision read the draft
mid-upload, with 23 pre-MPTP monkey V files missing and some monkey L files
read twice, so the author waited and ran it twice more, both giving the
numbers already recorded, and the record pins the draft as modified at
2026-10-21T23:10:32Z. The author raised no questions, and the answer run
found no questions file and changed nothing. Round 1 agreed with 27 of 28
outcomes; it gave `false-positive-rate` as not reproduced, where the author
kept it blocked as `methods_underspecified` under the rule that a computed
false-positive rate far from the paper's shows the procedures differ. Round 2
accepted that and agreed with all 28, so there was no third round. The paper,
"Primary motor cortex of the parkinsonian monkey: altered neuronal responses
to muscle stretch", reports how pyramidal tract and corticostriatal neurons
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/pasquereau-2013; for f in author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md reconcile-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
I worked through every point in the round-1 report and re-ran the entry with `python tools/entry.py all entries/pasquereau-2013`. It passes with 0 errors and the notebook runs in about 11 minutes. All conclusions match the new numbers. Nothing is committed.

**Outcomes.** None changed. The only disagreement is on kinematic-latency-unchanged: the verifier would block it because the measure moves onsets early, and I kept not_reproduced and recorded the disagreement. The new outputs show the verifier is right that the forwards-backwards filter moves onsets early: 6.7% of post-MPTP onsets land at 0 ms, against 0.1% before. But every way of measuring the onset still finds shorter latencies after MPTP:
- requiring the velocity to stay below threshold for the 20 ms before onset: F = 596.5
- a causal 25 Hz filter: F = 422.5
- both again at matched torque commands: F = 214.3 and 146.2
- the unfiltered velocity also rises earlier after MPTP.

The artifact narrows the difference but does not create it.

**Added or corrected, by point in the report:**
- **B1, response detection.** The 15 blocked claims are now also shown under the `trial_sd` reading, whose false-positive rate is 0.013. They stay blocked: that reading is not the claims file's detection. It also calls only 20.0% and 18.5% of M1 cells torque-related (75% and 68% expected) and finds only increases. Whether the claims file misreads the Methods' "2-tailed t-test" is now a question for a reader in the new file `questions/pasquereau-2013.yaml`. I did not change the claim.
- **B2, movement onset.** Added the fraction of onsets at 0 ms, the velocity at torque onset, the two onset variants above and the unfiltered velocity. The variants are documented in the `pasq.py` docstring.
- **B3, EMG and torque size.** All four EMG claims were re-run on perturbations with matched command pulses (60 to 250 units). Their outcomes are the same: m2 is larger after MPTP in every channel, KS p from 7.5e-08 t
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/pasquereau-2013.yaml; grep -nE '^\s*- id:|^\s*id:|figure|source:|where:|location' claims/pasquereau-2013.yaml | head -90
```

```
# Claims for Pasquereau & Turner (2013) on dandiset 001636.
# Source: the full text in PubMed Central (PMC3840326, open access, CC BY), read from its Methods,
# Results, Table 1 and figure legends, and its supplementary data sheet (DataSheet1.PDF), whose
# table gives the neuronal results for each monkey separately.
# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC3840326).
#
# When these criteria were written, the author had seen the data check only: the file list and
# metadata, the contents of the files, the counts of units by subject, MPTP state and projection
# type, the number of torque perturbations per direction (none in any monkey L file), the timing
# of the torque command against the trials table, the sign of the joint angle, which EMG channels
# hold data, and the cross-referenced and repeated files. These counts showed that the monkey V
# units with at least 5 perturbations per direction number 112 before and 159 after MPTP, with
# 49 and 54 PTNs and 31 and 48 CSNs, as in the supplementary table. No SDF, response detection,
# kinematic measure or EMG response had been computed.
#
# The dandiset marks no torque perturbation in any monkey L file, so every claim is tested on
# monkey V (elbow), and the expected values are the paper's monkey V values where it gives them
# (supplementary table). Where the paper gives only values pooled over both monkeys, these are
# the expected values and the difference is a deviation.
#
[... 78 more lines not kept]
```

**Agent**

Now the three verifier reports, which describe how the rounds went.

**Agent calls Bash**

```bash
cd transcripts/pasquereau-2013; for f in verifier-1-report.md verifier-2-report.md verifier-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
**Verifier report, round 1: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

The claims file has 28 claims. I re-ran the helpers `detect`, `sdf_trials` and `kinematics` on synthetic inputs and queried the archive's metadata; I did not download data or re-run the notebook.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 20: 115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual-projecting. All are within tolerance. |
| monkey-l-perturbations | blocked (data_missing) | Cell 15: all 5952 Leu trials are `not_available`. The dandiset description confirms "The Leu files contain no perturbation times". |
| baseline-rate | reproduced | Cell 24: all six means are within tolerance (PTN pre 18.49 vs 20.3±2.46). PTN p = 0.0198 (< 0.05), CSN p = 0.651 (≥ 0.05). The M1 test gives p = 0.0022, below the paper's 0.05/2. |
| ptn-faster-than-csn | reproduced | Cell 26: PTN 18.5 vs CSN 3.5 spikes/s, Mann-Whitney p = 6.3e-12. |
| antidromic-latency | partially_reproduced | Cell 28: all four means are within tolerance (CSN post 6.85 vs 6.1±0.89) and PTN p = 0.68 holds. The CSN test fails: p = 0.019, above 0.05/3 = 0.0167. The variant adding Leu units gives p = 0.0072. |
| false-positive-rate | blocked (methods_underspecified) | Cell 30: the pseudo-onset rate is 0.230, outside 0.0033–0.03. My synthetic test shows the claims file's procedure gives this rate on pure noise (B1). Only the `trial_sd` reading (0.013) falls in range. |
| torque-related-fractions | blocked (methods_underspecified) | Blocked through false-positive-rate, as the claims file's opening comment requires. For information only: under the blocked detection 2 of 6 are within tolerance (cell 32). |
| prevalence-unchanged | blocked (methods_underspecified) | Same gate. Cell 33 would give p > 0.39 for all three groups. |
| ptn-more-responsive | blocked (methods_underspecified) | Same gate. Cell 34: 70.5% vs 17.5%, χ² = 49. |
| one-direction-half | bl
[... 126 more lines not kept]
```

**Agent**

I've read all the sources. Writing the notes and the summary now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/pasquereau-2013-03.md",
 "content": "# pasquereau-2013, Pasquereau et al. 2013, third attempt\n\nFour claims reproduced, three partially, three not reproduced and eighteen\nblocked, all on the dandiset; seventeen are blocked as `methods_underspecified`\nand `monkey-l-perturbations` as `data_missing`. Round 1 agreed with 27 of 28\noutcomes; it gave `kinematic-latency-unchanged` as blocked, since the\nforwards-backwards filter moves movement onsets early (the post-MPTP flexion\nmean, 3.05 ms, falls before the command leaves rest at 4 ms), and the author\nkept not reproduced and added onset variants, of which only a causal 25 Hz\nfilter avoids the filter's spread and it also gives shorter latencies after\nMPTP (F = 422.5). Round 2 agreed with all 28 and asked that the finding on\ntorque pulse sizes be raised to major. The author then compared the states at\nthe two pulse sizes both use and proposed four changes of outcome\n(`kinematic-latency-unchanged` and `emg-onset-unchanged` to reproduced,\n`emg-duration-longer` to not reproduced, `emg-m1-weak` to reproduced), so a\nthird round reviewed those four; it agreed with none, as the criteria compare\nall sessions and the equal-pulse subsets are small (5 pre-MPTP channel-sessions\nnear 180 units, 14 post-MPTP near 90), and the outcomes stand with the\nproposals on record. It pins version 0.261124.1906, the newest published. The\nattempt was blind to `pasquereau-2013-02`, and the reconciliation found no\nclaim with a different outcome. The paper, Pasquereau and Turner, \"Primary\nmotor cortex of the parkinsonian monkey: altered neuronal responses to muscle\nstretch\", reports how pyramidal tract and corticostriatal neurons (PTNs and\nCSNs) in the primary motor cortex of two monkeys respond to torque\nperturbations before and after MPTP; only monkey V can be tested. The cell\ncounts (115 and 157 cells, 51 and 54 PTNs, 32 and 48 CSNs), the resting rates\nand the faster firing of PTNs than CSNs reproduce; `antidromic-latency` is\npartial, as the CSN p = 0.019 is above 0.05/3. The claims file's response\ndetection crosses its threshold after a pseudo onset in 0.230 of\ncell-directions, where the paper implies 0.01, which blocks\n`false-positive-rate` and the 15 claims that use the detected responses; the\nother readings of the Methods' t-test give 0.465, 0.347 and 0.013, and the last\ncalls only 0.200 of real cell-directions responsive, so whether the claims file\nmisreads the t-test was put to a reader in `questions/pasquereau-2013.yaml`.\n`trial-correlations` is blocked because the Methods define no single-trial\nlatency. After MPTP the evoked displacements are faster (+28.1%) and larger\n(+14.8%), not slower and smaller, and the movement onset latency is shorter\n(F = 709.5, p = 1.5e-102); `emg-m2-larger` reproduces, `emg-duration-longer` is\npartial (22.2 and 51.5 ms against 57 and 79 ms), `emg-onset-unchanged` is not\nreproduced (44.2 and 25.0 ms) and `emg-m1-weak` is partial (74.0% before MPTP\nagainst the 75% asked). Nothing failed; the notebook ran in 344 s at first,\nabout 11 minutes after round 1, 838 s after round 2 and 570 s after round 3,\nand 851 s in the reconcile run.\n\nThe dataset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb).\nThe monkey L (Leu) files mark no torque perturbation (major): all 5952 trials\nhave torque_perturbation_type not_available, the torque command is NaN in 114\nfiles, and in the other 34, all after MPTP, it moves at task events, so the\npaper's monkey L torque results (57 of 115 and 35 of 73 responsive cells)\ncannot be tested; the dandiset description says so. The torque command's pulse\nis larger after MPTP (major), mean 174.7 against 58.4 units and median 181.6\nagainst 45.7, where the paper describes one 0.1 Nm pulse; the units have no\nconversion to newton-metres, and the states share only pulses near 90 units\n(483 pre-MPTP and 227 post-MPTP perturbations) and near 180 units (41 and\n1540), so the kinematic and EMG comparisons over all perturbations cannot\nseparate the torque from the effect of MPTP. The evoked displacements differ\nfrom the paper's (major): 2.4 to 3.8 degrees where the paper gives a mean of\n10, peak velocities of 46 to 75 deg/s, with only 2 of 581 session-directions in\nthe 130 to 200 deg/s range of the paper's velocity-matched sessions, and\nfaster (+28%) and larger (+15%) after MPTP where the paper reports -16.2% and\n-6.6%; the angle agrees with the 20 degree targets and with ElbowVelocity. In\nthe Venus files the torque onset follows the centre target by 1.695 to 1.698 s\nin 88.4% of 5550 perturbations, where the paper gives 1 to 2 s at random\n(minor). The Leu analog series are sampled at 100 Hz where the paper gives 200\nHz, and the Venus EMG is in arbitrary units, both stated in the description\n(minor); three Venus sessions (v1401, v1402 and v1501) mark 51 perturbations\nwith no pulse in the command (minor). Checks that passed: no unit name or\nrecording repeats across files, is_post_mptp agrees with every file name, the\ncommand leaves rest 4 ms after the marked onset, and twelve files join the\ntrials of two lab source files without repeating any. In the paper, the\npre-MPTP PTN and CSN resting rates are 16.3 and 3.6 spikes/s in the Results\nand 18.3 and 3.2 in Table 1, and Table 1 marks a CSN change p < 0.01 where its\ncounts give p = 0.54. Two questions are put to the paper's authors: how the\ndetection t-test was computed, and how the single-trial response latency was\ndefined. The reconciliation found earlier findings 1 to 7 still present and\nadded three the attempt had not reported; the conversion code, in an open pull\nrequest at `-02`, is now on main (https://github.com/catalystneuro/turner-lab-to-nwb/pull/33,\nmerged on 2026-11-24 before the version was published).\n\nThe author's points on the protocol: the rule that blocks claims when the\nfalse-positive rate is far from the paper's does not say what happens to the\nclaim that is the false-positive rate, which was blocked as\n`methods_underspecified` with its dependents blocked through `depends_on`; it\ndoes not say whether claims blocked through a dependency show their numbers,\nand all were shown as not deciding; breaking down by session when there is one\nsubject does not fit 291 sessions, so results were broken down by MPTP state;\nand archives.md asks for pynwb, but 438 of the 439 files were read with h5py\nbecause building the pynwb objects for every file is too slow.\n"
}
```

```
File created successfully at: docs/pilot-notes/pasquereau-2013-03.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/pasquereau-2013-03.md",
 "content": "In monkey V, the cell counts and resting rates held up: pyramidal tract neurons fired faster than corticostriatal neurons and slowed after MPTP. The central findings on torque-evoked neuronal responses, such as shorter latencies and weaker directionality after MPTP, could not be tested, because the described detection gave a false-positive rate of 0.23 against the 0.01 the paper states. The slower, smaller torque-evoked movements after MPTP did not reproduce: movements were faster and larger, but the torque pulse was also larger after MPTP. The larger long-latency EMG response held, while other EMG and antidromic results were mixed. Monkey L could not be tested, as its files mark no perturbations.\n"
}
```

```
File created successfully at: summaries/pasquereau-2013-03.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/pasquereau-2013-03.md docs/pilot-notes/pasquereau-2013-03.md; grep -nE '—|rather|\*\*' summaries/pasquereau-2013-03.md docs/pilot-notes/pasquereau-2013-03.md; git status --short
```

```
109 summaries/pasquereau-2013-03.md
1029 docs/pilot-notes/pasquereau-2013-03.md
1138 total
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
?? docs/pilot-notes/pasquereau-2013-03.md
?? scripts
?? summaries/pasquereau-2013-03.md
```

**Agent**

# pasquereau-2013, Pasquereau et al. 2013, third attempt

Four claims reproduced, three partially, three not reproduced and eighteen blocked, all on the dandiset; seventeen are blocked as `methods_underspecified` and `monkey-l-perturbations` as `data_missing`. Round 1 agreed with 27 of 28 outcomes; it gave `kinematic-latency-unchanged` as blocked, since the forwards-backwards filter moves movement onsets early (the post-MPTP flexion mean, 3.05 ms, falls before the command leaves rest at 4 ms), and the author kept not reproduced and added onset variants, of which only a causal 25 Hz filter avoids the filter's spread and it also gives shorter latencies after MPTP (F = 422.5). Round 2 agreed with all 28 and asked that the finding on torque pulse sizes be raised to major. The author then compared the states at the two pulse sizes both use and proposed four changes of outcome (`kinematic-latency-unchanged` and `emg-onset-unchanged` to reproduced, `emg-duration-longer` to not reproduced, `emg-m1-weak` to reproduced), so a third round reviewed those four; it agreed with none, as the criteria compare all sessions and the equal-pulse subsets are small (5 pre-MPTP channel-sessions near 180 units, 14 post-MPTP near 90), and the outcomes stand with the proposals on record. It pins version 0.261124.1906, the newest published. The attempt was blind to `pasquereau-2013-02`, and the reconciliation found no claim with a different outcome. The paper, Pasquereau and Turner, "Primary motor cortex of the parkinsonian monkey: altered neuronal responses to muscle stretch", reports how pyramidal tract and corticostriatal neurons (PTNs and CSNs) in the primary motor cortex of two monkeys respond to torque perturbations before and after MPTP; only monkey V can be tested. The cell counts (115 and 157 cells, 51 and 54 PTNs, 32 and 48 CSNs), the resting rates and the faster firing of PTNs than CSNs reproduce; `antidromic-latency` is partial, as the CSN p = 0.019 is above 0.05/3. The claims file's response detection crosses its threshold after a pseudo onset in 0.230 of cell-directions, where the paper implies 0.01, which blocks `false-positive-rate` and the 15 claims that use the detected responses; the other readings of the Methods' t-test give 0.465, 0.347 and 0.013, and the last calls only 0.200 of real cell-directions responsive, so whether the claims file misreads the t-test was put to a reader in `questions/pasquereau-2013.yaml`. `trial-correlations` is blocked because the Methods define no single-trial latency. After MPTP the evoked displacements are faster (+28.1%) and larger (+14.8%), not slower and smaller, and the movement onset latency is shorter (F = 709.5, p = 1.5e-102); `emg-m2-larger` reproduces, `emg-duration-longer` is partial (22.2 and 51.5 ms against 57 and 79 ms), `emg-onset-unchanged` is not reproduced (44.2 and 25.0 ms) and `emg-m1-weak` is partial (74.0% before MPTP against the 75% asked). Nothing failed; the notebook ran in 344 s at first, about 11 minutes after round 1, 838 s after round 2 and 570 s after round 3, and 851 s in the reconcile run.

The dataset was converted by CatalystNeuro (catalystneuro/turner-lab-to-nwb). The monkey L (Leu) files mark no torque perturbation (major): all 5952 trials have torque_perturbation_type not_available, the torque command is NaN in 114 files, and in the other 34, all after MPTP, it moves at task events, so the paper's monkey L torque results (57 of 115 and 35 of 73 responsive cells) cannot be tested; the dandiset description says so. The torque command's pulse is larger after MPTP (major), mean 174.7 against 58.4 units and median 181.6 against 45.7, where the paper describes one 0.1 Nm pulse; the units have no conversion to newton-metres, and the states share only pulses near 90 units (483 pre-MPTP and 227 post-MPTP perturbations) and near 180 units (41 and 1540), so the kinematic and EMG comparisons over all perturbations cannot separate the torque from the effect of MPTP. The evoked displacements differ from the paper's (major): 2.4 to 3.8 degrees where the paper gives a mean of 10, peak velocities of 46 to 75 deg/s, with only 2 of 581 session-directions in the 130 to 200 deg/s range of the paper's velocity-matched sessions, and faster (+28%) and larger (+15%) after MPTP where the paper reports -16.2% and -6.6%; the angle agrees with the 20 degree targets and with ElbowVelocity. In the Venus files the torque onset follows the centre target by 1.695 to 1.698 s in 88.4% of 5550 perturbations, where the paper gives 1 to 2 s at random (minor). The Leu analog series are sampled at 100 Hz where the paper gives 200 Hz, and the Venus EMG is in arbitrary units, both stated in the description (minor); three Venus sessions (v1401, v1402 and v1501) mark 51 perturbations with no pulse in the command (minor). Checks that passed: no unit name or recording repeats across files, is_post_mptp agrees with every file name, the command leaves rest 4 ms after the marked onset, and twelve files join the trials of two lab source files without repeating any. In the paper, the pre-MPTP PTN and CSN resting rates are 16.3 and 3.6 spikes/s in the Results and 18.3 and 3.2 in Table 1, and Table 1 marks a CSN change p < 0.01 where its counts give p = 0.54. Two questions are put to the paper's authors: how the detection t-test was computed, and how the single-trial response latency was defined. The reconciliation found earlier findings 1 to 7 still present and added three the attempt had not reported; the conversion code, in an open pull request at `-02`, is now on main (https://github.com/catalystneuro/turner-lab-to-nwb/pull/33, merged on 2026-11-24 before the version was published).

The author's points on the protocol: the rule that blocks claims when the false-positive rate is far from the paper's does not say what happens to the claim that is the false-positive rate, which was blocked as `methods_underspecified` with its dependents blocked through `depends_on`; it does not say whether claims blocked through a dependency show their numbers, and all were shown as not deciding; breaking down by session when there is one subject does not fit 291 sessions, so results were broken down by MPTP state; and archives.md asks for pynwb, but 438 of the 439 files were read with h5py because building the pynwb objects for every file is too slow.

---

In monkey V, the cell counts and resting rates held up: pyramidal tract neurons fired faster than corticostriatal neurons and slowed after MPTP. The central findings on torque-evoked neuronal responses, such as shorter latencies and weaker directionality after MPTP, could not be tested, because the described detection gave a false-positive rate of 0.23 against the 0.01 the paper states. The slower, smaller torque-evoked movements after MPTP did not reproduce: movements were faster and larger, but the torque pulse was also larger after MPTP. The larger long-latency EMG response held, while other EMG and antidromic results were mixed. Monkey L could not be tested, as its files mark no perturbations.

## End of run

13 turns, 2 minutes, $1.03 at API prices, result: success.
