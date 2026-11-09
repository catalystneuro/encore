# 000463 · claims-check · run 39960044608

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000463/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/000463/*.yaml; python tools/claims_check.py claims/000463/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md | sed -n 1,80p; python tools/claims_check.py claims/000463/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt | tail -30; wc -l claims/000463/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 000463.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record as served by PubMed Central (PMC12139594), full text with
6	# Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt). The
7	# paper has no supplement. No PDF was provided, so the dSTTC equation of the Methods, which the
8	# text drops, could not be read (see open details). The paper links no analysis code; none was read.
9	#
10	# Which data. The paper says its data are at DANDI 000946 ("All experimental data has been made
11	# public in a repository at the DANDI Archive (https://dandiarchive.org/dandiset/000946)").
12	# Dandiset 000463 is titled "Electrophysiological Recordings in Anesthetized Rats in the Primary
13	# Somatosensory Cortex with Phased Ultrasound Array Stimulation"; its description cites this paper,
14	# speaks of S1 recordings with 32-channel NeuroNexus electrodes under 2% isoflurane, testing
15	# "different intensities and PRFs", stimulation every 2.5 s, 200 or 500 trials per recording, and
16	# its summary lists 4 subjects. Which of the paper's experiments it holds (S1 only, or S1 with POm,
17	# or the AC group) is the author's to find; DANDI 000946 is named here as the paper's own deposit.
18	#
19	# Data the paper used, as it reports them. Male Wistar rats (Hsd WI, Envigo), 250 to 350 g, 3 to 6
20	# months, under isoflurane (2%, 0.4 to 0.6 L/min). Main group N = 16 rats with two 32-channel
[... 787 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt",
 "offset": 326
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 807
}
```

```
807	  criterion: The 30 Hz, 0.6% DC sessions, dSTTC (M5, O6, O7, O8), 0 to 67 ms against
808	    prestimulation (M6), S1 RSU to POm FSU one-tailed greater and POm RSU to S1 FSU one-tailed
809	    less, at p < 0.05. Reproduced when both hold under every reading; partially reproduced when
810	    one holds.
811	- id: fig10c-sttc-constant-pd
812	  statement: With constant 200 us pulse duration, the change of STTC between S1 RSUs and POm RSUs
813	    during sonication does not depend on PRF, though 1500 Hz gives a higher change than 30 Hz.
814	  source: Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C
815	  quote: When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not
816	    show PRF-dependent change. A total of 1,500 Hz PRF did show a higher correlation change
817	    compared with 30 Hz PRF (Fig. 10C; p = 0.02).
818	  statistics:
819	  - about: 1500 against 30 Hz
820	    test: one-tail two-sample Wilcoxon
821	    p: 0.02
822	  criterion: Pairs of S1 RSUs and POm RSUs in the constant-PD series; STTC (Cutts and Eglen 2014)
823	    with Delta t 20 ms, change during 0 to 67 ms from prestimulation normalized by O7. The absence
824	    of PRF dependence is judged on the paper's test, Kruskal-Wallis across the five PRFs at p <
825	    0.05 (M6), holding when not significant. The 1500 against 30 Hz part holds when 1500 Hz is
826	    greater, one-tailed, p < 0.05. Reproduced when both hold under every O7 reading; partially
[... 192 more lines not kept]
```

**Agent**

Checker passes with 0 problems. Now looking at how other check entries handle a missing equation, for consistency.

**Agent calls Bash**

```bash
cd claims; grep -l "^checks:" */*.yaml | head; grep -rn -A12 "^checks:" */*.yaml | grep -i -E "pdf|equation|ready" | head -20
```

```
000005/10.1038-nn.4412.yaml
000006/10.1038-s41586-018-0642-9.yaml
000008/10.1038-s41586-020-2907-3.yaml
000009/10.1038-nature22324.yaml
000010/10.1038-nature14178.yaml
000011/10.1038-nature17643.yaml
000013/10.7554-elife.06619.yaml
000015/10.1016-j.neuron.2017.05.005.yaml
000016/10.1016-j.neuron.2019.09.045.yaml
000017/10.1038-s41586-019-1787-x.yaml
000005/10.1038-nn.4412.yaml-1096-  ready: true
000006/10.1038-s41586-018-0642-9.yaml-845-  ready: true
000008/10.1038-s41586-020-2907-3.yaml-968-  ready: true
000008/10.1038-s41586-020-2907-3.yaml-970-  - Opening comment, excluded cells. Said the 7 cells with an exclusion reason are excluded; 2 of them already failed quality control (code metadata table), so the excluded cells with a t-type are the Methods' 5 (4 contaminated, 1 outside MOp).
000009/10.1038-nature22324.yaml-1029-  ready: true
000010/10.1038-nature14178.yaml-755-  ready: true
000011/10.1038-nature17643.yaml-943-  ready: true
000013/10.7554-elife.06619.yaml-1248-  ready: true
000015/10.1016-j.neuron.2017.05.005.yaml-690-  ready: true
000016/10.1016-j.neuron.2019.09.045.yaml-872-  ready: true
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/000054/*.yaml | head -20; grep -rln "ready: false" claims | head -3
```

```
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - checker. The four "value not found" reports for edf9l-null-models-frequent (p = 6e-05) are the legend's "6.0 × 10 −5", which the checker does not match; the values are the paper's, no change.
  - cells-per-session. The criterion counted FD mice without saying the paper fixes it; Extended Data Fig. 1a,b plot R and F mice only, so the R and F reading and the R, F and FD reading are both named.
  - fig3ab-block-versus-gradual-similarity. The criterion could not tell blocks from a gradual change (S-tilde 0.25 nearer S-tilde 0 than 1, and a falling similarity, hold for both). Replaced by a step share compared between groups with test M12, marked as a reading not given by the paper.
  - edf6-nmf-confirms-remapping. Same fault ("high", "low" and "step" undefined, and gradual factors also meet the rare condition); replaced by the same step share on the NMF factors, marked as a reading.
  - edf5-umap-rare-frequent-separable. The Methods give 100 shuffles for the classifier test and the Extended Data Fig. 5c legend 1,000; both now run. Sessions 8 to N now cited to the Results (the UMAP Methods name none); S bin edges named as open with a standard choice; the reported 18,230 cells added for comparison.
  - fig7-model-reproduces-remapping. The Methods list sigma_w 0.05 N(0,1), which the criterion left out; it appears in no equation, so readings with and without weight noise are named.
  - edf1-licking-before-reward. The statement includes running, which no figure shows and the criterion did not test; the criterion now says it is not judged.
  - open. Several criteria rest on readings the paper does not give, because the paper judges the finding by eye (edf4bc-overlap-cells-at-ends-and-reward, fig3ab-block-versus-gradual-similarity, edf6-nmf-confirms-remapping, edf7-checkerboard-sessions, fig4-sf-stable-along-track, edf9-early-sessions, edf10-decision-mice-like-frequent); each is marke
[... 3 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  source: Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4\n  quote: There was no activity change among S1 FSUs (n = 61) to 30 Hz PRF and POm FSUs to both PRFs\n    (3,000 Hz, n = 17; 30 Hz, n = 43)",
 "new_string": "  source: Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraphs 1 and 3;\n    Figure 4\n  quote: There was no activity change among S1 FSUs (n = 61) to 30 Hz PRF and POm FSUs to both PRFs\n    (3,000 Hz, n = 17; 30 Hz, n = 43) ... only S1 RSUs showed time-locked responses to 3,000 Hz PRF\n    instead of 30 Hz PRF"
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  statement: POm RSUs show time-locked responses to 1500 and 3000 Hz PRF; their delayed responses\n    are induced by PRFs from 1500 Hz up and are highest at 1500 Hz (141.68 +/- 2.38%).",
 "new_string": "  statement: POm RSUs show time-locked responses to 1500 and 3000 Hz PRF; their delayed responses\n    are induced by PRFs higher than 1500 Hz and are highest at 1500 Hz (141.68 +/- 2.38%)."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    4500 Hz alone is significant against baseline. The 30 against 1500 Hz difference is tested\n    one-tailed, 1500 Hz greater (the direction the paper does not state; the other is shown).\n    Reproduced when the absence and delayed parts hold; partially reproduced when one holds.",
 "new_string": "    4500 Hz alone is significant against baseline. The 30 against 1500 Hz difference in 0 to 67\n    ms has no stated direction, so it is tested one-tailed each way (1500 Hz greater, 30 Hz\n    greater), corrected p < 0.01, and holds when either is significant; the direction found is\n    reported. Reproduced when all three parts hold; partially reproduced when two hold."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    0.6% and 90% are not, and 30% exceeds 0.6% (one-tailed), under every O1 to O4 reading.\n    Partially reproduced when two of the three named DCs are significant.",
 "new_string": "    0.6% and 90% are not, and 0.6% and 30% differ, under every O1 to O4 reading. The legend gives\n    no direction for that difference, so it is tested one-tailed each way at corrected p < 0.01\n    and holds when either is significant; the direction found is reported. Partially reproduced\n    when two of the three named DCs are significant."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    both Kruskal-Wallis tests are significant, 6, 30 and 90% are each significant against\n    baseline in 0 to 67 ms, and 90% in 201 to 268 ms (one-tailed greater, corrected p < 0.01),\n    under every O1 to O4 reading. Partially reproduced when three of the four named results hold.",
 "new_string": "    both Kruskal-Wallis tests are significant, 6, 30 and 90% are each significant against\n    baseline in 0 to 67 ms, and 90% in 201 to 268 ms (corrected p < 0.01), under every O1 to O4\n    reading. The 90% responses are tested one-tailed greater (the Discussion calls the 90% DC\n    response excitatory). The paper gives no direction for the 6% and 30% time-locked responses\n    (the 0.6% DC response at 30 Hz is inhibitory, Figure 4), so each is tested one-tailed each way\n    and holds when either is significant; the direction found is reported. Partially reproduced\n    when three of the four named results hold."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  criterion: The 60% DC series (30, 300, 1500, 3000, 4500 Hz), S1 RSUs, tests of M4. The direction\n    of the 30 Hz differences is not stated; they are tested one-tailed with the other PRF greater,\n    the reverse shown. \"Only 30 Hz\" means no pair of the other four PRFs differs.",
 "new_string": "  criterion: The 60% DC series (30, 300, 1500, 3000, 4500 Hz), S1 RSUs, tests of M4. The direction\n    of the 30 Hz differences is not stated; each is tested one-tailed each way and holds when\n    either is significant, the direction found reported. \"Only 30 Hz\" means no pair of the other\n    four PRFs differs."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    highest mean 0 to 67 ms response of S1 RSUs in the constant-PD series is 1500 or 3000 Hz, the\n    PRF with the highest mean 0 to 67 ms response of POm RSUs in that series is 1500 or 3000 Hz,\n    and the two highest STTC changes in the 60% DC series are at 1500 and 3000 Hz; partially\n    reproduced when two of the three hold.",
 "new_string": "    highest mean 0 to 67 ms response of S1 RSUs in the constant-PD series is 1500 or 3000 Hz, the\n    PRF with the highest mean response of POm RSUs in that series is 1500 or 3000 Hz, and the two\n    highest STTC changes in the 60% DC series are at 1500 and 3000 Hz; partially reproduced when\n    two of the three hold. The Discussion does not say which window \"the POm highest responses\"\n    means; the readings are 0 to 67 ms and 201 to 268 ms (where Figure 6C puts the highest\n    delayed response at 1500 Hz), and the POm part holds under either."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  criterion: Pairs of the 3000 Hz sessions of the AC group (O8), dSTTC (M5, O6, O7). The absence\n    with S1 RSUs is judged on the paper's test, each 67 ms window from 0 to 268 ms against\n    prestimulation at p < 0.05 (M6), in both directions (AC to S1 RSU and S1 RSU to AC), each\n    one-tailed by O5; it holds when none is significant. The FSU part holds when a change in\n    either direction between AC neurons and S1 FSUs is significant in 201 to 268 ms (the windows",
 "new_string": "  criterion: Pairs of the 3000 Hz sessions of the AC group (O8), dSTTC (M5, O6, O7). The absence\n    with S1 RSUs is judged on the paper's test, dSTTC from AC neurons to S1 RSUs (the direction\n    the Figure 11 legend names), each 67 ms window from 0 to 268 ms against prestimulation at p <\n    0.05 (M6), one-tailed by O5; it holds when none is significant. S1 RSU to AC is shown as a\n    variant only. The FSU part holds when dSTTC from AC neurons to S1 FSUs increases or decreases\n    significantly (the legend's \"bidirectional\") in 201 to 268 ms (the windows"
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "#     Windows are 67 ms (prestimulation -67 to 0, during 0 to 67, then 67 ms steps), as in M3.",
 "new_string": "#     The paper does not state the dSTTC windows. The one reading its text supports is 67 ms\n#     windows (prestimulation -67 to 0, during 0 to 67, then 67 ms steps), as in M3."
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000463/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    recorded from POm for PRF 30 Hz.\n  expected:",
 "new_string": "    recorded from POm for PRF 30 Hz. ... sorted 1,050 RSUs (A) and 247 FSUs (B) recorded from S1\n    ... sorted 913 RSUs (C) and 106 FSUs (D) recorded from POm\n  expected:"
}
```

```
The file claims/000463/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/000463/10.1523-jneurosci.2218-24.2025.yaml <<'EOF'
checks:
- date: 2026-10-23
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4-unit-counts. The quote held only the Figure 4 counts; the Figure 6 legend counts the statement also gives are now quoted.
  - fig4-fsu-no-change. The statement's S1 FSU part (no time-locked response to 3000 Hz) had no quote; added the sentence of paragraph 3 that states it, and the source now cites it.
  - fig6c-pom-rsu-prf. The statement said "from 1500 Hz up", one of the two readings the criterion names; it now says "higher than 1500 Hz", as the paper does.
  - fig6d-pom-fsu-prf. The 30 against 1500 Hz difference is in the statement but was not part of the outcome, and its one-tailed direction was the agent's choice; it is now tested each way (the legend gives no direction) and counts toward the outcome.
  - fig7b-s1-fsu-dc-3000. The outcome required 30% to exceed 0.6% DC, a direction the Figure 7B legend does not give; now tested each way.
  - fig8a-s1-rsu-dc-30. All responses were tested one-tailed greater, but the paper gives a direction only for 90% DC (Discussion, excitatory); the 6% and 30% time-locked responses are now tested each way.
  - fig9a-s1-rsu-prf-60dc. The direction of the 30 Hz differences was the agent's choice; the paper gives none, so each is now tested each way.
  - synthesis-prf-pathway. The criterion took the POm "highest responses" as 0 to 67 ms; the Discussion names no window, and Figure 6C gives the POm peak at 1500 Hz in 201 to 268 ms, so both windows are named as readings.
  - fig11d-ac-s1-3000hz-dsttc. The absence test also covered S1 RSU to AC, a direction the paper does not report; the paper's test is AC to S1 RSU, and the reverse is now a variant only. The FSU part now says AC to S1 FSU, increase or decrease, as the legend's "bidirectional" says.
  - O7. Said plainly that the paper does not give the dSTTC windows and that 67 ms is the reading taken from the rate windows.
  - open. O6, the dSTTC equation, is not in the text read (PMC text drops it) and no PDF was supplied; the reading named is the STTC form of Cutts and Eglen with the four directional terms the Methods define. The PDF should be read to confirm it; if it differs, the dSTTC claims (fig10a, fig10b, fig11c, fig11d) must be revised.
  - open. Dandiset 000463 is not the deposit the paper names (000946); which of the paper's experiments it holds is the author's to find.
  - open. fig7c-pom-rsu-dc-3000. The unlabelled entry (n = 7, p = 0.001) in the list of delayed POm RSU responses is read as 30% DC, the only DC left; the text does not label it.
  - open. fig11c-ac-s1fsu-30hz. The Figure 11 legend (decrease) and the Results (synchronization, as with S1 RSUs) disagree on direction; the criterion tests both and records the disagreement.
EOF
python tools/claims_check.py claims/000463/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n ": " claims/000463/*.yaml | sed -n '/^1[0-9][0-9][0-9]:/p' | grep -v "^10[0-9][0-9]:  [a-z]*:" | head; git status --short
```

```
1000:- id: fig11d-ac-s1-3000hz-dsttc
1010:  - {quantity: "pairs in the 3000 Hz sessions", value: 1714, tolerance: 171.4}
1011:  - {quantity: "pairs of AC neurons and S1 FSUs, 3000 Hz sessions", value: 1016, tolerance: 101.6}
1020:- id: methods-insitu-pressure
1028:  - {quantity: "in situ peak-to-peak pressure", value: 88, tolerance: 8.8, unit: kPa}
1029:  - {quantity: "ISPTA", value: 29.42, tolerance: 2.942, unit: mW/cm2}
1030:  - {quantity: "free-water spatial peak pressure", value: 1626.4, tolerance: 162.64, unit: kPa}
1034:- date: 2026-10-23
 M claims/000463/10.1523-jneurosci.2218-24.2025.yaml
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

The file is ready for an attempt. I made nine changes and left four points open; none of the open points blocks an attempt.

**Checker result** (same before and after my edits): `37 claims, 37 quotes, 84 statistical values, 0 problems`

**Changes, by claim**
- **fig4-unit-counts:** the quote now also includes the Figure 6 legend counts, which the statement gives but the quote left out.
- **fig4-fsu-no-change:** the part saying S1 FSUs show no time-locked response at 3000 Hz had no supporting quote. I added the paragraph 3 sentence that states it and updated the source.
- **fig6c-pom-rsu-prf:** the statement said "from 1500 Hz up", which is only one of the criterion's two readings. It now says "higher than 1500 Hz", as the paper does.
- **fig6d-pom-fsu-prf:** the 30 versus 1500 Hz difference was in the statement but did not count toward the outcome, and its direction was the agent's choice. It is now tested in both directions and counts.
- **fig7b-s1-fsu-dc-3000:** the outcome required 30% DC to exceed 0.6%, a direction the legend does not give. It is now tested in both directions.
- **fig8a-s1-rsu-dc-30:** only 90% DC has a stated direction (the Discussion calls it excitatory). The 6% and 30% time-locked responses are now tested in both directions.
- **fig9a-s1-rsu-prf-60dc:** the direction of the 30 Hz differences was the agent's choice. They are now tested in both directions.
- **synthesis-prf-pathway:** the paper names no window for "the POm highest responses", so both windows (0 to 67 ms and 201 to 268 ms) are now readings.
- **fig11d-ac-s1-3000hz-dsttc:** the absence test also covered S1 RSU to AC, which the paper does not report. It is now AC to S1 RSU only, with the reverse kept as a variant. The FSU part now reads AC to S1 FSU, increase or decrease, matching the legend's "bidirectional".
- **O7 (open-details list):** it now says plainly that the paper gives no dSTTC windows, and that 67 ms is a reading taken from the rate windows.

**Open, recorded in `checks`**
- **dSTTC equation (O6):** the equation is missing from the text and no PDF was supplied. The file uses the standard STTC form with the four directional terms the Methods define. The PDF should confirm it; if it differs, the dSTTC claims (fig10a, fig10b, fig11c, fig11d) need revising.
- **Which dandiset:** the paper names DANDI 000946 as its deposit, not 000463. Which of the paper's experiments 000463 holds is for the author to find.
- **fig7c:** one entry in the list of delayed POm RSU responses (n = 7, p = 0.001) has no DC label. The file reads it as 30%, the only DC left.
- **fig11c-ac-s1fsu-30hz:** the Figure 11 legend says the correlation decreased, the Results imply it increased. The criterion tests both directions and records the disagreement.

All of the paper's main findings have a claim, and every claim comes from this paper. The changes are only in `claims/000463/` and are not committed.

## End of run

22 turns, 3 minutes, result: success.
