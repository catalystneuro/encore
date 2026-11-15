# jacobsen-2022 · recorder · run 43677995067

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py jacobsen-2022; ls transcripts/jacobsen-2022/; cat attempts/jacobsen-2022-01.yaml claims/jacobsen-2022.yaml; ls summaries | head
```

```
<persisted-output>
Output too large (88.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6a13b4df-9c95-418a-86df-9d228ea837ac/tool-results/b4oqure0t.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
| [000230](https://dandiarchive.org/dandiset/000230) | [Jacobsen et al. 2022](https://doi.org/10.1016/j.crmeth.2022.100221) | 5 | 2 | 0 | 21 | [`jacobsen-2022`](entries/jacobsen-2022) |
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
[... 43 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6a13b4df-9c95-418a-86df-9d228ea837ac/tool-results/b4oqure0t.txt"
}
```

```
1	docs/pilot-notes/amjad-2025-01.md
2	docs/pilot-notes/andrews-2024-01.md
3	docs/pilot-notes/armstrong-2026-01.md
4	docs/pilot-notes/asari-2009-01.md
5	docs/pilot-notes/ashworth-2025-01.md
6	| [000230](https://dandiarchive.org/dandiset/000230) | [Jacobsen et al. 2022](https://doi.org/10.1016/j.crmeth.2022.100221) | 5 | 2 | 0 | 21 | [`jacobsen-2022`](entries/jacobsen-2022) |
7	answer-report.md
8	answer.md
9	author-answers-report.md
10	author-answers.md
11	author-report.md
12	author-revise-1-report.md
13	author-revise-1.md
14	author-revise-2-report.md
15	author-revise-2.md
16	author.md
17	claims-check-report.md
18	claims-check.md
19	claims-report.md
20	claims.md
[... 905 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nE "^- id:|^  source:|^  statement:" -A2 claims/jacobsen-2022.yaml | grep -vE "quote|inferred|expected" | sed -n '1,400p' | tail -n +20; python -c "
import json;d=json.load(open('targets/dandisets.json'));
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000230' in json.dumps(x)[:300]: print(json.dumps(x,indent=1))"
```

```
139:  statement: No starter cells were found in the MEC.
140:  source: Results, A virus-based method for targeting a single cell and identifying its inputs,
141-    paragraph 3
--
145:- id: fig2b-rabies-cells-increase-with-time
146:  statement: The number of rabies-positive cells in the ipsilateral dorsal hippocampus increases
147-    with the days after the rabies injection (Spearman R = 0.58, p = 0.0014, n = 27 animals).
148:  source: Figure 2B, left, and legend; Results, A virus-based method for targeting a single cell
149-    and identifying its inputs, paragraph 4
--
166:- id: fig2b-conclusive-more-than-control
167:  statement: Conclusive animals (days 26 to 30) have more rabies-positive cells in the dorsal
168-    hippocampus than the no-Cre control animals, which were all inconclusive.
169:  source: Figure 2B, right, and legend
171-    animals, which were all inconclusive (p = 0.0159, Wilcoxon rank-sum test, n = 5 conclusive and
--
182:- id: figs2a-spread-increases-with-time
183:  statement: The spread of rabies-positive cells along the longitudinal axis of the dorsal
184-    hippocampus increases with days after the rabies injection (Spearman r = 0.54, p = 0.0036,
185-    n = 27 animals).
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "000230" -B3 -A15 targets/dandisets.json | head -40; cat transcripts/jacobsen-2022/author-report.md; for f in author-revise-1-report author-revise-2-report author-answers-report answer-report claims-report claims-check-report verifier-1-report verifier-2-report; do echo "=== $f"; head -c 3000 transcripts/jacobsen-2022/$f.md; echo; done
```

```
1593-   ]
1594-  },
1595-  {
1596:   "dandiset": "000230",
1597-   "name": "Jacobsen 2022",
1598-   "published_version": "0.220506.1516",
1599-   "asset_count": 9,
1600-   "size_gb": 0.24,
1601-   "data_standards": [
1602-    "Neurodata Without Borders (NWB)"
1603-   ],
1604-   "species": [
1605-    "Mus musculus - House mouse"
1606-   ],
1607-   "approaches": [
1608-    "behavioral approach",
1609-    "electrophysiological approach"
1610-   ],
1611-   "papers": [
I finished author steps 1 to 6 for `entries/jacobsen-2022/` and the record `attempts/jacobsen-2022-01.yaml`. The entry passes `tools/entry.py all` with 0 errors, the notebook runs in 81 s in a clean environment, and the handover is in `executed/jacobsen-2022/handover/`. Nothing is committed.
[... 213 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1596,1640p targets/dandisets.json | grep -n catalyst; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -5 docs/pilot-notes/knierim-2000-02.md; ls summaries | head -3; cat summaries/$(ls summaries | head -1)
```

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/6a13b4df-9c95-418a-86df-9d228ea837ac/tool-results/b1yojkdib.txt

Preview (first 2KB):
32:   "catalystneuro": []
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/6a13b4df-9c95-418a-86df-9d228ea837ac/tool-results/b1yojkdib.txt",
 "offset": 25
}
```

```
25	and no implantation dates are given.
26	
27	The author's run succeeded, but its commit failed: the commit job switched
28	to the attempt's branch, made before `tools/archive_transcripts.sh`
29	existed, and then called that script (fixed by running it from the
30	workflow's own ref). It was committed from the run's artifact. The run had
31	also started from the files of an earlier run that the subscription's
32	session limit cut short, because the chain's reset of the branch did not
33	take. It started from a branch made before pilot-7 and followed
34	pilot-6; the first revision, which saw pilot-7, changed the record's
35	protocol to pilot-7 after checking that no claim needed the `elsewhere`
36	kind. The author's points on the protocol: the data kind of a link claim
37	whose source holds both labels and measurements; clock checks when the
38	contrast is the claim itself; a criterion written after its result was
39	seen in the data check; and linked code that holds none of the analysis.
40	=== andrews-2024-01
41	# andrews-2024, Andrews et al. 2024
42	
43	No claim reproduced on the dandiset, one partially, none not reproduced and 26
44	blocked, all for missing data, with one more blocked that also uses outside
[... 499 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat summaries/amjad-2025-01.md summaries/andrews-2024-01.md; echo; sed -n '/B7/,$p' transcripts/jacobsen-2022/author-revise-1-report.md; grep -n "^\*\*B\|^- \*\*B\|^B[0-9]" transcripts/jacobsen-2022/verifier-1-report.md | head -20; tail -20 transcripts/jacobsen-2022/verifier-2-report.md
```

```
The paragraph is below, ready to save. Most of the paper's neural findings held in this data, while its insertion and imaging claims could not be tested. Dopamine was higher after large-reward cues, but weakly (p = 0.023), and beta power was lower after large-reward cues and after left cues. A clean sorted unit was found in monkey P. Insertion yields, days of implantation and the two-channel dopamine increase could not be tested without implant records or the second channel; the redox colour plot and monkey P's reward-modulated firing could not be tested because raw FSCV timing does not fit the trials and that file has no events. Recording parameters matched, except a lowest voltage of -0.347 V.
None of the paper's main findings could be tested in this data: that light on the opsin HcKCR1 suppresses unit firing in human hippocampal slices across culture media and in closed loop, that kainic acid bursts show theta coherence and spread across the granule cell layer, and that waveform clusters over that layer are linked to an opto-response cluster. The dandiset holds raw voltage only, without the curated units these analyses rest on, the light times or labels for each recording's medium. Of the minor claims, the paper's network model, rerun from its code, reproduced the dampening of seizure-like events, and the cohort matches Table 1 except that no file records each slice's opsin.

- **B7:** the notes say the deposit is curated and that the mec-inputs test cannot fail on the early side.
- **B8:** the border-score baseline is now described in the helper; the method is unchanged.

**Not done:**
- B9 needed no change. A spike exactly at the pulse time is not counted, which the verifier called immaterial at the 48 kHz spike clock.
- I added no questions to `questions/jacobsen-2022.yaml`, because the report found no place where the claims file misreads the paper.
- The verifier could not see the rate-map images. I did not add more, since the grid and border judgements rest 
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/jacobsen-2022-01.md",
 "content": "# jacobsen-2022, Jacobsen et al. 2022\n\nFive claims reproduced, two partially, none not reproduced and 21 blocked,\nall for missing data; four outcomes rest on an assumption. The first\nverification round agreed with all 28 outcomes as they stood and the second\nwith all 28; nothing was proposed after the second, so there was no third\nround. It pins version 0.220506.1516, the version the paper cites and the\nlatest published one. The paper, Jacobsen, Nair, Obenhaus, Donato, Slettmoen,\nMoser and Moser, \"All-viral tracing of monosynaptic inputs to single\nbirthdate-defined neurons in the intact brain\" (Cell Reports Methods 2,\n100221), targets single birthdate-defined hippocampal cells with in utero Cre,\na helper virus and rabies, counts their starter and input cells by histology,\nand identifies the function of input cells in the medial entorhinal cortex\n(MEC) by optogenetic tagging with RABV-ChR2-YFP and by two-photon imaging. The\nclaims were written from the version of record, with Figures S1 to S4 read\nfrom the PDF; the paper reports no code of its own and its Methods cite\nRowland et al. (2018) for the analysis of the electrophysiology, whose\nMethods and linked archdata code (for smoothing, the 5 cm/s speed cutoff and\ntuning bins) are listed as inputs. The claims check made seven changes,\namong them removing a responsiveness rule based on spikes before the pulse,\nwhich the paper never uses, and adding `population-targeting-mec-labelling`,\nfor 28 claims. Only the optogenetic tagging claims could be tested. With the\npulse time taken as the TTL onset the paper's latencies and fidelities come\nout to two decimals (T1 C89, the responsive grid cell, at 2.75 ms and\n40.73%); with the offset T1 C89 is at 1.70 ms and not responsive. Reproduced\nare `fig5c-functional-cell-types` (2 grid, 2 head direction and 1 border cell\nunder the standard shuffle, the border cell T4 C50 at 0.656 against 0.555,\nfalling short at 0.663 under the literal shuffle), `fig5c-responsive-grid-cell`,\n`fig5c-example-cells` (all nine values, taking T1 C57 from the second laser\nepoch of day 17 and T1 C52 from the first, which goes beyond the criterion),\n`responsive-cells-at-19-days` and `mec-inputs-from-two-weeks` (day 14, a test\nthat cannot fail on the early side, as no earlier session is deposited).\nPartial are `figs3-stable-input-cell` (17 of 18 values, the day 14 session 2\nopen-field rate 0.899 Hz against 1.06 ± 0.106; all 18 match over the first\n1800 s, a reading not adopted because it was found from the expected values)\nand `figs4-nonresponsive-cells` (the head direction score of 0.81 and the\npeak rate of 9.02 Hz miss, at 0.912 and 10.62 Hz, and no tuning setting of 48\nputs both within tolerance). The 19 histology claims of Figures 2 to 4, S1 and\nS2 and the two imaging claims of Figures 6 and 7 are blocked. Round 1 found\nthat the record said earlier versions hold the same assets, that the shuffle\nand the open-field span were unstated choices, that the per-epoch choice for\nday 17 decides reproduced against partial, that tuning settings lowering the\npeak rate had not been run and that the waveform does not identify the cell of\nFigure S3; in reply the shuffle sentence was quoted and the shuffled\ndistributions shown, the first 1800 s were run for all 12 units, 48 tuning\nsettings were run and the measured head direction score became the tuning-map\nmean vector length. Round 2 found sentences the outputs did not support (a\nfirst TTL event of 0.6 to 1.9 s, now 45 ms to 1.9 s; LFP timestamps running\nbackwards 3 or 4 times, now 2 to 4), and that the first 275 pulses are not a\nrule the paper applied to every session, all corrected. The author asked a\nreader nothing, so the answer and author-answers runs changed nothing. The\nauthor's run took about 21 minutes (03:04 to 03:25 UTC); its only failure,\nrepeated in the author-answers run, was `tools/entry.py lock` writing a\n`python` field that the entry schema rejects, removed by hand. The notebook\nran in 81 s at first, 201 s after round 1 and 180 to 184 s at the end.\n\nThe dandiset holds only the optrode recordings of two mice (58313, 70375), and\nof these only the 12 curated units shown in Figures 5C, S3 and S4; the\nhistology of the single-cell tracing and the two-photon imaging are not in it,\nand the paper names no other deposit, so 21 of the paper's 28 claims cannot be\ntested. For day 14 session 2 of mouse 70375 the file holds 2722 s of open\nfield and 413 pulses, and the paper's printed values (1.06 Hz, 2.95 ms, 48.00%)\nare what the first 1800 s and the first 275 pulses give, where the whole file\ngives 0.899 Hz, 3.05 ms and 46.49%; the paper does not say part of the session\nwas left out, and the first 275 pulses are not a rule it applied to every\nsession. The open field part of each session is not an epoch. The two laser\nepochs of the day-17 session of mouse 58313 carry \"N/A\" for the power label,\nwhere the other eight files carry \"10Hz20mW\", and nothing in the file tells\nthem apart. The first laser TTL event of every PhotoStim epoch starts at the\nepoch start and lasts 45 ms to 1.9 s, where every other event lasts 1.0 to 1.1\nms. The TTL events show trains of 6 pulses at 10 Hz every 2.6 s, where the\nSTAR Methods describe pulses \"at 10 Hz continuously\". The LFP timestamps run\nbackwards 2 to 4 times within each file and end at 120 to 180 s, though each\nseries has 510,250 to 815,750 samples 4 ms apart. Units `waveform_mean` is\nlabelled volts but has a peak-to-trough of 31 to 41 for the 70375 unit and 34\nto 243 for the units of 58313. No cluster label is shared across the six\nsessions of 70375, and the unit's waveforms correlate with those of 58313 up to\n0.965, so the cell of Figure S3 is identified only by each file holding one\ncurated unit. Version 0.220426.0814 holds 18 assets, the nine sessions twice\nunder real and hashed subject ids. The positions of the day-17 session span 76\nx 75 cm, where the other eight span about 94 x 95 cm. Three questions are put\nto the paper's authors: how the head direction score and the 9.02 Hz peak rate\nare computed, which day-17 laser epoch Figure 5C uses, and whether the\nshuffle of Rowland et al. (2018) shifts within 20 s or by at least 20 s.\n\nThe author's points on the protocol and tools: `tools/entry.py lock` writes a\n`python` field the entry schema rejects; the protocol does not say how to\ntreat readings listed in the claims file's shared opening comment, and the\nrule for criteria was applied with both readings reported; it has no rule for\nan epoch choice made per unit, and every option was run with the outcome\nmarked assumed; its order of sources covers the paper's own code but not code\nlinked by a paper it cites, so the text came first and the code filled the\ngaps; and the claims file's fidelity floor gives no chance level, so the\nfidelity before each pulse and with shifted pulse times was shown instead.\n"
}
```

```
File created successfully at: docs/pilot-notes/jacobsen-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/jacobsen-2022-01.md",
 "old_string": "that the record said earlier versions",
 "new_string": "that the notebook said earlier versions"
}
```

```
The file docs/pilot-notes/jacobsen-2022-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/jacobsen-2022-01.md",
 "content": "The paper's optogenetic tagging results held up in this data, but its single-cell tracing and imaging results could not be tested. Entorhinal input cells to the hippocampus responded to light within 2 to 4 ms, including a grid cell, and grid, head direction and border cells were present. The border cell and the example cells' values rest on assumptions about the shuffle and about which unlabelled laser epoch the figure uses. How reliably single starter cells are labelled, which inputs they receive and the two-photon imaging of input cells could not be tested, because the dandiset holds only the electrophysiology of two mice. Of the minor claims, a cell followed across sessions and the non-responsive cells matched in part.\n"
}
```

```
File created successfully at: summaries/jacobsen-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/jacobsen-2022-01.md; grep -c "—\|rather" summaries/jacobsen-2022-01.md docs/pilot-notes/jacobsen-2022-01.md; git status --short
```

```
119 summaries/jacobsen-2022-01.md
summaries/jacobsen-2022-01.md:0
docs/pilot-notes/jacobsen-2022-01.md:0
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
?? docs/pilot-notes/jacobsen-2022-01.md
?? scripts
?? summaries/jacobsen-2022-01.md
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "summaries/jacobsen-2022-01.md",
 "old_string": "How reliably single starter cells are labelled, which inputs they receive and the two-photon imaging of input cells could not be tested, because the dandiset holds only the electrophysiology of two mice.",
 "new_string": "How reliably single starter cells are labelled, which inputs they receive and the two-photon imaging could not be tested, because the dandiset holds only the electrophysiology of two mice."
}
```

```
The file summaries/jacobsen-2022-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

I've written the notes and the summary in two new files and changed nothing else; nothing is committed. The summary is 115 words. The `catalystneuro` field for 000230 is empty, so the dataset paragraph does not open with the CatalystNeuro sentence.

`docs/pilot-notes/jacobsen-2022-01.md`:

# jacobsen-2022, Jacobsen et al. 2022

Five claims reproduced, two partially, none not reproduced and 21 blocked, all for missing data; four outcomes rest on an assumption. The first verification round agreed with all 28 outcomes as they stood and the second with all 28; nothing was proposed after the second, so there was no third round. It pins version 0.220506.1516, the version the paper cites and the latest published one. The paper, Jacobsen, Nair, Obenhaus, Donato, Slettmoen, Moser and Moser, "All-viral tracing of monosynaptic inputs to single birthdate-defined neurons in the intact brain" (Cell Reports Methods 2, 100221), targets single birthdate-defined hippocampal cells with in utero Cre, a helper virus and rabies, counts their starter and input cells by histology, and identifies the function of input cells in the medial entorhinal cortex (MEC) by optogenetic tagging with RABV-ChR2-YFP and by two-photon imaging. The claims were written from the version of record, with Figures S1 to S4 read from the PDF; the paper reports no code of its own and its Methods cite Rowland et al. (2018) for the analysis of the electrophysiology, whose Methods and linked archdata code (for smoothing, the 5 cm/s speed cutoff and tuning bins) are listed as inputs. The claims check made seven changes, among them removing a responsiveness rule based on spikes before the pulse, which the paper never uses, and adding `population-targeting-mec-labelling`, for 28 claims. Only the optogenetic tagging claims could be tested. With the pulse time taken as the TTL onset the paper's latencies and fidelities come out to two decimals (T1 C89, the responsive grid cell, at 2.75 ms and 40.73%); with the offset T1 C89 is at 1.70 ms and not responsive. Reproduced are `fig5c-functional-cell-types` (2 grid, 2 head direction and 1 border cell under the standard shuffle, the border cell T4 C50 at 0.656 against 0.555, falling short at 0.663 under the literal shuffle), `fig5c-responsive-grid-cell`, `fig5c-example-cells` (all nine values, taking T1 C57 from the second laser epoch of day 17 and T1 C52 from the first, which goes beyond the criterion), `responsive-cells-at-19-days` and `mec-inputs-from-two-weeks` (day 14, a test that cannot fail on the early side, as no earlier session is deposited). Partial are `figs3-stable-input-cell` (17 of 18 values, the day 14 session 2 open-field rate 0.899 Hz against 1.06 ± 0.106; all 18 match over the first 1800 s, a reading not adopted because it was found from the expected values) and `figs4-nonresponsive-cells` (the head direction score of 0.81 and the peak rate of 9.02 Hz miss, at 0.912 and 10.62 Hz, and no tuning setting of 48 puts both within tolerance). The 19 histology claims of Figures 2 to 4, S1 and S2 and the two imaging claims of Figures 6 and 7 are blocked. Round 1 found that the notebook said earlier versions hold the same assets, that the shuffle and the open-field span were unstated choices, that the per-epoch choice for day 17 decides reproduced against partial, that tuning settings lowering the peak rate had not been run and that the waveform does not identify the cell of Figure S3; in reply the shuffle sentence was quoted and the shuffled distributions shown, the first 1800 s were run for all 12 units, 48 tuning settings were run and the measured head direction score became the tuning-map mean vector length. Round 2 found sentences the outputs did not support (a first TTL event of 0.6 to 1.9 s, now 45 ms to 1.9 s; LFP timestamps running backwards 3 or 4 times, now 2 to 4), and that the first 275 pulses are not a rule the paper applied to every session, all corrected. The author asked a reader nothing, so the answer and author-answers runs changed nothing. The author's run took about 21 minutes (03:04 to 03:25 UTC); its only failure, repeated in the author-answers run, was `tools/entry.py lock` writing a `python` field that the entry schema rejects, removed by hand. The notebook ran in 81 s at first, 201 s after round 1 and 180 to 184 s at the end.

The dandiset holds only the optrode recordings of two mice (58313, 70375), and of these only the 12 curated units shown in Figures 5C, S3 and S4; the histology of the single-cell tracing and the two-photon imaging are not in it, and the paper names no other deposit, so 21 of the paper's 28 claims cannot be tested. For day 14 session 2 of mouse 70375 the file holds 2722 s of open field and 413 pulses, and the paper's printed values (1.06 Hz, 2.95 ms, 48.00%) are what the first 1800 s and the first 275 pulses give, where the whole file gives 0.899 Hz, 3.05 ms and 46.49%; the paper does not say part of the session was left out, and the first 275 pulses are not a rule it applied to every session. The open field part of each session is not an epoch. The two laser epochs of the day-17 session of mouse 58313 carry "N/A" for the power label, where the other eight files carry "10Hz20mW", and nothing in the file tells them apart. The first laser TTL event of every PhotoStim epoch starts at the epoch start and lasts 45 ms to 1.9 s, where every other event lasts 1.0 to 1.1 ms. The TTL events show trains of 6 pulses at 10 Hz every 2.6 s, where the STAR Methods describe pulses "at 10 Hz continuously". The LFP timestamps run backwards 2 to 4 times within each file and end at 120 to 180 s, though each series has 510,250 to 815,750 samples 4 ms apart. Units `waveform_mean` is labelled volts but has a peak-to-trough of 31 to 41 for the 70375 unit and 34 to 243 for the units of 58313. No cluster label is shared across the six sessions of 70375, and the unit's waveforms correlate with those of 58313 up to 0.965, so the cell of Figure S3 is identified only by each file holding one curated unit. Version 0.220426.0814 holds 18 assets, the nine sessions twice under real and hashed subject ids. The positions of the day-17 session span 76 x 75 cm, where the other eight span about 94 x 95 cm. Three questions are put to the paper's authors: how the head direction score and the 9.02 Hz peak rate are computed, which day-17 laser epoch Figure 5C uses, and whether the shuffle of Rowland et al. (2018) shifts within 20 s or by at least 20 s.

The author's points on the protocol and tools: `tools/entry.py lock` writes a `python` field the entry schema rejects; the protocol does not say how to treat readings listed in the claims file's shared opening comment, and the rule for criteria was applied with both readings reported; it has no rule for an epoch choice made per unit, and every option was run with the outcome marked assumed; its order of sources covers the paper's own code but not code linked by a paper it cites, so the text came first and the code filled the gaps; and the claims file's fidelity floor gives no chance level, so the fidelity before each pulse and with shifted pulse times was shown instead.

`summaries/jacobsen-2022-01.md`:

The paper's optogenetic tagging results held up in this data, but its single-cell tracing and imaging results could not be tested. Entorhinal input cells to the hippocampus responded to light within 2 to 4 ms, including a grid cell, and grid, head direction and border cells were present. The border cell and the example cells' values rest on assumptions about the shuffle and about which unlabelled laser epoch the figure uses. How reliably single starter cells are labelled, which inputs they receive and the two-photon imaging could not be tested, because the dandiset holds only the electrophysiology of two mice. Of the minor claims, a cell followed across sessions and the non-responsive cells matched in part.

## End of run

13 turns, 2 minutes, $0.91 at API prices, result: success.
