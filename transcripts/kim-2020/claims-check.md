# kim-2020 · claims-check · run 42675429230

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i kim; cat claims/kim-2020.yaml; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/kim-2020.yaml; python tools/claims_check.py claims/kim-2020.yaml paper/*kim*.txt 2>&1 | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kim-2020.yaml paper/10.1038-s41467-020-14835-7.txt 2>&1 | tail -30; wc -l paper/10.1038-s41467-020-14835-7.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-020-14835-7.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-020-14835-7.txt",
 "offset": 509,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passed (45 claims, 0 problems). I've read the paper; now reading the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/kim-2020.yaml",
 "limit": 400
}
```

```
1	# Claims for Kim, Atencio & Schreiner (2020), Nature Communications 11, 1102,
2	# doi:10.1038/s41467-020-14835-7, tested on CRCNS data set ac-5.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-09,
4	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
5	#
6	# Text read: the version of record (PMC7046699, open access, Europe PMC JATS XML flattened), with
7	# its Results, figure legends, Tables 1 and 2, Methods, and the Supplementary Information
8	# (41467_2020_14835_MOESM1_ESM.pdf, Supplementary Figures 1 to 3 and their legends), as supplied
9	# under paper/. The PDF was not opened; the tables read cleanly in the text.
10	#
11	# Code. The paper links no code repository; its Data availability statement points only to the
12	# CRCNS data set (doi 10.6080/K07H1GSS). The data set's description says it holds a "codes" folder
13	# with the Matlab analysis scripts and stimulus files. Those are files of the data set, so the
14	# reader did not open them, and no method below is taken from them. Several details named open
15	# below (marked D1 to D17) may be settled by that code.
16	#
17	# Data the paper used. Female C57BL/6 mice (Charles River), 4 to 11 weeks old, anesthetized with
18	# ketamine and xylazine. In vivo blind whole-cell recordings from the right primary auditory cortex
19	# (A1), about 300 to 500 um deep (about layer 4), low-pass filtered at 5 kHz and sampled at 10 kHz;
20	# no current injection, no junction potential correction; recordings with rest above -50 mV
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kim-2020.yaml",
 "offset": 400,
 "limit": 400
}
```

```
400	    give 10; Supplementary Fig. 2 legend). Pearson r between the two STRFs of a pair over all
401	    pixels; whether the STRFs are the full or the significant ones is not said, readings (a) full,
402	    (b) significant. The paper's "paired" test against 0 is read as a one-sample two-tailed t-test
403	    of the 13 values against 0. Reproduced when, under one reading, the ranges are within the
404	    widened bounds and each test gives p < 0.05. If the data set holds fewer repeats than 13 pairs,
405	    the pairs present are reported.
406	- id: supfig2-psp-more-reliable-than-spikes
407	  statement: STRF test-retest correlations for large and small PSPs were usually high and
408	    significantly exceeded those for spike STRFs.
409	  source: Results, Response reliability over extended recording durations is high; Supplementary
410	    Figure 2b
411	  quote: Correlations between the resulting STRFs for both large and small PSPs were usually high and
412	    significantly exceeded those for spike STRFs
413	  depends_on:
414	  - supfig2-strf-reliability
415	  criterion: The paper names no test for this comparison. Readings (a) a two-tailed paired t-test
416	    over the 13 pairs, the test the legend uses; (b) a Wilcoxon signed-rank test over the 13 pairs.
417	    Reproduced when, under the readings, both large-PSP and small-PSP correlations exceed spike
418	    correlations at p < 0.05.
419	- id: supfig3-intensity-invariance
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kim-2020.yaml",
 "offset": 800,
 "limit": 400
}
```

```
800	    unit: octaves
801	  - quantity: total bandwidth small PSPs, mean
802	    value: 0.50
803	    tolerance: 0.32
804	    unit: octaves
805	  depends_on:
806	  - fig2-strf-significance-groups
807	  criterion: A claim of absence, judged on Table 1's paired t-tests at p < 0.05 over the 30 neurons,
808	    total bandwidth per D8. Reproduced when no pair differs; not reproduced when any does; the means
809	    are compared with the expected values and reported.
810	- id: tab1-latency-duration
811	  statement: STRF latencies were 42.7 +- 11.1 ms (spikes), 48.7 +- 11.8 ms (large PSPs) and 45.2 +-
812	    8.2 ms (small PSPs), large PSPs significantly later than spikes and small PSPs; durations were
813	    43.0 +- 24.1, 43.6 +- 18.8 and 34.5 +- 10.3 ms, small PSPs significantly shorter than spikes and
814	    large PSPs.
815	  source: Table 1, Latency and Duration
816	  inferred: Read from Table 1; the Results do not discuss STRF latency or duration.
817	  statistics:
818	  - about: latency, spikes against large PSPs
819	    test: two-tailed paired Student's t-test
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kim-2020.yaml",
 "offset": 1200,
 "limit": 370
}
```

```
1200	  - about: spike TRF Q30 against all-event STRF Q
1201	    test: two-tailed paired Student's t-test
1202	    p: 0.0025
1203	    n: 15 neurons with NDR >= 0.3
1204	  expected:
1205	  - quantity: paired neurons with NDR >= 0.3
1206	    value: 15
1207	    tolerance: 1.5
1208	  depends_on:
1209	  - fig5a-cf-bf-correlation
1210	  - fig1fgh-trf-bandwidth-narrowing
1211	  criterion: Q30 = CF / TRF bandwidth30, STRF Q = BF / all-event STRF bandwidth; bandwidth units per
1212	    D15, bandwidths per D8 and D15. Reproduced when, under one reading, STRF Q exceeds both TRF Q30s
1213	    at p < 0.05 (paired t-test), and the count of paired neurons with NDR >= 0.3 is within tolerance.
1214	- id: fig7-current-amplitude-unimodal
1215	  statement: Peak current amplitude distributions (events above 3 x s.d. of baseline) were unimodal for
1216	    EPSCs and IPSCs.
1217	  source: Results, DMR-evoked excitatory and inhibitory synaptic currents, paragraph 1; Figure 7a, b
1218	  quote: The amplitude distributions of peak currents (>3 × s.d. above baseline) were unimodal for
1219	    excitatory postsynaptic currents (EPSCs) and inhibitory postsynaptic currents (IPSCs)
[... 350 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reader" docs/protocol.md | head; awk '/^## Reader/,/^## [^R]/' docs/protocol.md | head -150
```

```
15:  it against the paper. Readers never see the dataset's data.
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
43:## Reader
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold. A
data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
documentation) is a longer description, to be read for that alone; it is not
the paper, and no claim comes from it.

### 2. Read the paper's code
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:" claims/kim-2020.yaml | wc -l; grep -n "^- id:" claims/kim-2020.yaml | awk '{print $3}' | tr '\n' ' '; echo; tail -3 claims/kim-2020.yaml; grep -n "checks" claims/kim-2020.yaml
```

```
45
cc-cohort-counts vc-cohort-counts fig1-psp-amplitude-kinetics fig1c-resting-potential-range fig1d-ndr-distribution fig1e-ndr-vs-rest-weak fig1fgh-trf-bandwidth-narrowing fig2-psp-histogram-modality fig2-strf-significance-groups fig2-psp-amplitude-ranges supfig2-strf-reliability supfig2-psp-more-reliable-than-spikes supfig3-intensity-invariance fig3d-double-peaked-counts fig3e-harmonic-ratios fig3f-bandwidth-single-vs-double fig4c-btmf-small-psp-higher fig4d-bsmf-small-psp-higher tab1-modulation-large-psp-like-spikes fig4b-bsmf-btmf-correlation fig5a-cf-bf-correlation fig5b-bf-same-across-events fig5c-bandwidth-relationships tab1-single-band-small-psp-narrower tab1-total-bandwidth-no-difference tab1-latency-duration tab1-event-rate-no-difference tab1-fsi-spikes-higher-than-large fig6b-tab1-threshold-spikes-higher fig6c-tab1-transition-spikes-lower fig6bc-no-correlation-psp-spike-nonlinearity fig6d-spike-threshold-transition-covary fig6efg-fsi-relationships fig5df-strf-narrower-than-trf fig5e-q-strf-higher fig7-current-amplitude-unimodal fig7c-ei-bf-matched fig7d-current-double-peaks fig7e-tab2-inhibition-broader fig7f-tab2-ipsc-bsmf-lower tab2-btmf-currents-higher-than-spikes tab2-event-rate-excitation-higher tab2-nonlinearity-ei tab2-fsi-ei tab2-latency-duration-ei-no-difference 
  criterion: A claim of absence, judged on Table 2's unpaired t-tests at p < 0.05, latency and
    duration per D10. Reproduced when neither differs; not reproduced when either does; the means
    are reported against the expected values.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "    under one reading, the four means are within tolerance and the eleven comparisons that Table 2\n    marks significant give p < 0.05 in the same direction; partially reproduced when the E-I\n    differences in threshold and transition hold with p < 0.05 and at least seven of the other nine\n    do.",
 "new_string": "    under one reading, the four means are within tolerance and the twelve comparisons that Table 2\n    marks significant (all seven for threshold; for transition E-I, E-spikes, E-small PSPs, I-large\n    PSPs, I-small PSPs) give p < 0.05 in the same direction; partially reproduced when the E-I\n    differences in threshold and transition hold with p < 0.05 and at least eight of the other ten\n    do."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: Double peaks per D9 on significant STRFs (D7) of spikes, large PSPs, small PSPs and all\n    events, over the 40 neurons. Reproduced when, under one reading, the counts are within tolerance\n    and spike STRFs are double-peaked in fewer neurons than PSP STRFs.",
 "new_string": "  criterion: Double peaks per D9 on significant STRFs (D7) of spikes, large PSPs, small PSPs and all\n    events, over the 40 neurons. The 20/40 is given both as double peaks \"in either the spiking or\n    the subthreshold STRFs\" and as \"double-peaked STRFs for all events, n = 20/40\" (same paragraph),\n    and Fig. 3e takes its 20 ratios from all-event STRFs; readings for that count (a) neurons with a\n    double-peaked STRF of any event type, (b) neurons with a double-peaked all-event STRF.\n    Reproduced when, under one reading, the counts are within tolerance and spike STRFs are\n    double-peaked in fewer neurons than PSP STRFs."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: Double peaks per D9 on the significant EPSC and IPSC STRFs. Reproduced when, under one\n    reading, the three counts are within tolerance.",
 "new_string": "  criterion: Double peaks per D9 on the significant EPSC and IPSC STRFs. The Results call 11/31 a\n    share \"of the current traces\", but 31 is the number of neurons and the traces number 39 (27 +\n    12), with 9 + 5 = 14 double-peaked (Fig. 7d legend). Readings for the 11 (a) neurons with a\n    double-peaked EPSC or IPSC STRF, out of 31; (b) double-peaked traces, out of 39, where 14 is\n    expected and 11 cannot be matched. Reproduced when, under one reading, the three counts are within\n    tolerance."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: Q30 = CF / TRF bandwidth30, STRF Q = BF / all-event STRF bandwidth; bandwidth units per\n    D15, bandwidths per D8 and D15.",
 "new_string": "  criterion: STRF Q = BF / all-event STRF bandwidth (Results, \"(best frequency)/bandwidth\"). The\n    paper defines no TRF best frequency; Q30 readings (a) CF / TRF bandwidth30, the usual Q30; (b)\n    the frequency of the largest response at the threshold + 30 dB level / TRF bandwidth30.\n    Bandwidth units per D15, bandwidths per D8 and D15."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: A claim of absence, judged on Table 1's paired t-tests at p < 0.05. Event rate = events\n    of the type over the DMR duration (10 min, Methods, Stimuli).",
 "new_string": "  criterion: A claim of absence, judged on Table 1's paired t-tests at p < 0.05. The paper does not\n    define event rate; it is read as events of the type over the DMR duration (10 min, Methods,\n    Stimuli), a standard choice."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: Events above 3 x s.d. of baseline (D3) over the DMR duration. Reproduced",
 "new_string": "  criterion: Events above 3 x s.d. of baseline (D3) over the DMR duration (event rate is not defined\n    in the paper; this is a standard choice). Reproduced"
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kim-2020.yaml",
 "old_string": "  criterion: As fig4c-btmf-small-psp-higher, for bSMF. Reproduced when, under one reading of D11, the\n    means are within tolerance and both paired t-tests give p < 0.05 with small PSPs higher;\n    partially reproduced when the tests hold with values outside tolerance.",
 "new_string": "  criterion: As fig4c-btmf-small-psp-higher, for bSMF. Reproduced when, under one reading of D11, the\n    means are within tolerance and both paired t-tests give p < 0.05 with small PSPs higher;\n    partially reproduced when the tests hold with values outside tolerance. The Discussion\n    (paragraph 1, observation 2) says large and small PSP STRFs differed \"not in spectral\n    preferences\", against the Results and Table 1 (p = 0.0021); the claim follows the Results and\n    Table 1."
}
```

```
The file claims/kim-2020.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry.

**Agent calls Bash**

```bash
cd  cat >> claims/kim-2020.yaml <<'EOF'
checks:
- date: 2026-11-09
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - tab2-nonlinearity-ei, criterion. Table 2 marks twelve comparisons significant (seven for threshold, five for transition), not eleven; the count is corrected, the comparisons named, and the partial rule made eight of the other ten (it was seven of nine, one of them not existing).
  - fig3d-double-peaked-counts, criterion. The paper gives the 20/40 both as double peaks in spiking or subthreshold STRFs and as double-peaked all-event STRFs (Results, Double-peaked STRFs, paragraph 1; Fig. 3e legend); both readings are now named.
  - fig7d-current-double-peaks, criterion. The Results call 11/31 a share of current traces, but 31 is the neuron count and the 39 traces hold 9 + 5 = 14 double-peaked STRFs (Fig. 7d legend); the readings (neurons, traces) are now named.
  - fig5e-q-strf-higher, criterion. The paper defines Q as best frequency over bandwidth and gives no TRF best frequency; using CF for Q30 is a reading, now named with its alternative.
  - tab1-event-rate-no-difference and tab2-event-rate-excitation-higher, criteria. The paper does not define event rate; events over the DMR duration is now marked as a standard choice.
  - fig4d-bsmf-small-psp-higher, criterion. Noted that the Discussion (paragraph 1, observation 2) says large and small PSPs did not differ in spectral preference, against the Results and Table 1; the claim follows the Results and Table 1.
  - Open. Some grading bounds are the reader's, as the paper gives no number for its words. fig1d-ndr-distribution ("very few near 1" read as under 10% of neurons above 0.7), fig1e-ndr-vs-rest-weak (partial when r below 0.3), fig7-current-amplitude-unimodal (90% and 75% of recordings unimodal), fig5c-bandwidth-relationships (five or three of six counts). They do not change what is measured, only how a near miss is graded.
  - Open. The data set's "codes" folder (Matlab analysis scripts) was not read, as it is part of the data set; it may settle D1 to D17, in particular the STRF bandwidth (D8), double-peak rule (D9) and the nonlinearity fit form (D12).
EOF
python tools/claims_check.py claims/kim-2020.yaml paper/10.1038-s41467-020-14835-7.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/kim-2020.yaml | grep -n '^  - .*: ' ; git status --short
```

```
M claims/kim-2020.yaml
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

I checked `claims/kim-2020.yaml` against the paper. Only that file is modified, and nothing is committed.

**Checker:** `claims/kim-2020.yaml: 45 claims, 41 quotes, 97 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim**
- **tab2-nonlinearity-ei:** Table 2 marks 12 comparisons significant, not 11 (all 7 for threshold, 5 for transition). I corrected the count and named the 12. The "partially reproduced" rule was "7 of the other 9", which no longer fits; I made it "8 of the other 10".
- **fig3d-double-peaked-counts:** The paper describes the 20/40 two ways: neurons with a double peak in the spiking or subthreshold STRFs, and neurons with a double-peaked all-event STRF (the Fig. 3e ratios come from all-event STRFs). The criterion now names both readings.
- **fig7d-current-double-peaks:** The Results call 11/31 a share of "current traces". But 31 is the neuron count, and the 39 traces hold 9 + 5 = 14 double-peaked STRFs. The criterion now names two readings: neurons out of 31, or traces out of 39.
- **fig5e-q-strf-higher:** The paper defines Q as best frequency over bandwidth but gives no best frequency for TRFs. Using the characteristic frequency for TRF Q30 is therefore a reading; it is now named, with an alternative.
- **tab1-event-rate-no-difference and tab2-event-rate-excitation-higher:** The paper does not define event rate. "Events over the DMR duration" is now marked as a standard choice.
- **fig4d-bsmf-small-psp-higher:** I added a note that the Discussion (observation 2) says large and small PSPs did not differ in spectral preference. The Results and Table 1 (p = 0.0021) say they did, and the claim follows those.

The other claims match the paper. Statements, sources, p-values and tolerances are the paper's, and none of the recorded statistics is a threshold used to count units. Every main finding has a claim: TRF narrowing, STRFs narrower than TRFs, modulation differences, nonlinearities, and the excitatory/inhibitory synaptic currents (EPSCs and IPSCs). Nothing comes from outside the paper.

**Still open (recorded in `checks`)**
- **Grading bounds the paper doesn't give:** Four claims grade near misses with cut-offs the first agent chose, because the paper uses words, not numbers, there:
  - fig1d: "very few near 1" read as under 10% of neurons above 0.7.
  - fig1e: "partially reproduced" when r is below 0.3.
  - fig7: 90% and 75% of recordings unimodal.
  - fig5c: five of six counts (or three or four for partial).

  These bounds affect only how a near miss is graded, not what is measured.
- **Analysis code not read:** The dataset's Matlab "codes" folder was not read, since it is part of the dataset. It may settle the open details D1 to D17, especially STRF bandwidth (D8), the double-peak rule (D9) and the form of the nonlinearity fit (D12).

**Ready:** yes (`ready: true`).

## End of run

21 turns, 2 minutes, $1.28 at API prices, result: success.
