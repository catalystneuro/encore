# 001199 · claims-check · run 39816597896

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001199/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; python tools/claims_check.py claims/001199/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml"
}
```

```
1	# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23) e2218242025, on dandiset 001199.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
3	# docs/protocol.md, version pilot-10.
4	#
5	# Text read: the version of record as served by PubMed Central (paper/10.1523-jneurosci.2218-24.2025.txt,
6	# fetched by paper-text-fetcher), with Abstract, Significance Statement, Introduction, Materials and
7	# Methods, Results, all eleven figure legends and Discussion. The paper has no supplement and no PDF
8	# was supplied. The text lost the equation of the directional STTC (Methods, Directional spike time
9	# tiling coefficient); only its verbal definition survives (see D below). The Fig. 6 legend prints the
10	# postsonication window as "201–28 ms" (201–268 ms in the Results), and the Fig. 11 legend labels two
11	# panels "C" (the second is Fig. 11B in the Results).
12	#
13	# Code. The paper links no analysis code and names none; it says the analysis was done in MATLAB
14	# R2022a after spike sorting in Offline Sorter (Plexon). No repository was read.
15	#
16	# Which dataset. The paper's Methods name dandiset 000946 as the repository of all its data. Dandiset
17	# 001199 has the same title and cites this paper, but its description differs from the paper. It
18	# describes S1 recordings with 64-channel Cambridge or NeuroNexus electrodes, tFUS delivered "either at
19	# S1 or PoM", and varied pressure levels (input voltage in the session identifier), none of which the
20	# paper reports, and it does not mention the auditory cortex recordings. Dandiset 000946's description
[... 802 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "offset": 822
}
```

```
822	- id: fig9b-s1-fsu-60dc
823	  statement: At constant 60% DC, S1 FSUs respond to 1,500 Hz PRF during sonication (n = 48) and
824	    postsonication prefer 4,500 Hz (n = 18), with PRF-dependent activity in both windows.
825	  source: Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 3; Figure
826	    9B legend
827	  quote: S1 FSUs responded to 1,500 Hz PRF (n = 48, p = 3.35 ×10−6) during sonication and preferred 4,500
828	    Hz post sonication (n = 18, p = 5.84 × 10−10; Fig. 9B).
829	  statistics:
830	  - about: 1,500 Hz during, against baseline
831	    test: post hoc one-tail two-sample Wilcoxon test
832	    p: 3.35e-6
833	    corrected: Bonferroni
834	    n: 48 S1 FSUs
835	  - about: 4,500 Hz postsonication
836	    test: post hoc one-tail two-sample Wilcoxon test
837	    p: 5.84e-10
838	    corrected: Bonferroni
839	    n: 18 S1 FSUs
840	  - about: during sonication, across PRFs
841	    test: Kruskal-Wallis
[... 232 more lines not kept]
```

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
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt",
 "offset": 326,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  window. Tests as T with significance at 0.05 (Methods), pairs as samples, normalized dSTTC compared\n#   with the prestimulus value (Fig. 10 legend, \"compared with prestimulation correlation\"), one-tailed in\n#   the stated direction.",
 "new_string": "  window. The window length is not given for dSTTC; 67 ms is taken from the spiking analysis (67 ms\n#   prestimulus and sonication windows), a reading the text allows and no other is named. Tests as T\n#   with significance at 0.05 (Methods), pairs as samples, normalized dSTTC compared with the\n#   prestimulus value (Fig. 10 legend, \"compared with prestimulation correlation\"), one-tailed in the\n#   stated direction. The Methods name Bonferroni's correction for the spiking post hoc tests only; for\n#   dSTTC they say \"Post hoc one-tail two-sample Wilcoxon tests were employed\". Open, (C1) uncorrected,\n#   as the dSTTC sentence reads, or (C2) Bonferroni under B1 or B2 as for spiking; the outcome is the\n#   one they all give."
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  source: Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraphs 1 and 2; Figure 4",
 "new_string": "  source: Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraphs 1 and 3; Figure 4\n    legend"
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    are an increase only (the one-tailed direction of the paper's activations) and either direction\n    (both one-tailed tests). Reproduced when no test finds a change; not reproduced when any does. The\n    mean normalized rates are reported either way, under each reading of R, T and B.",
 "new_string": "    are an increase only (the one-tailed direction of the paper's activations) and either direction\n    (both one-tailed tests). Reproduced when no test finds a change under either reading; not\n    reproduced when a test for an increase finds one; when only a decrease is found the readings\n    differ and the claim is methods_underspecified. The S1 FSU part at 3,000 Hz is read from the\n    Fig. 4 legend, which names time-locked responses in S1 and POm RSUs only, and from paragraph 3\n    (\"only S1 RSUs showed time-locked responses to 3,000 Hz PRF\"). The mean normalized rates are\n    reported either way, under each reading of R, T and B."
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's test, T at corrected p < 0.01, one-tailed for an\n    increase (the direction of the responses this control is set against), in 0 to 67 ms and 201 to\n    268 ms, for the four groups of the sham sessions, aligned to the sham trial times the dataset gives.\n    Reproduced when none of the eight tests is significant; not reproduced when any is. The effect sizes\n    (mean normalized rates) are reported, and the test for a decrease is shown as a variant. Run under\n    each reading of R, T and B; the outcome is the one they all give.",
 "new_string": "  criterion: A claim of absence, judged on the paper's test, T at corrected p < 0.01, in 0 to 67 ms and\n    201 to 268 ms, for the four groups of the sham sessions, aligned to the sham trial times the dataset\n    gives. The direction of the one-tailed tests is not stated; the readings are an increase only (the\n    direction of the responses this control is set against) and either direction. Reproduced when none\n    of the tests is significant under either reading; not reproduced when a test for an increase is;\n    when only a decrease is significant the readings differ and the claim is methods_underspecified.\n    The effect sizes (mean normalized rates) are reported. Run under each reading of R, T and B; the\n    outcome is the one they all give."
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  criterion: As fig7a-s1-rsu-dc-3000 for S1 FSUs in 201 to 268 ms. Reproduced when exactly 6%, 30% and 60%\n    are significantly above baseline and 30% is significantly above 0.6% (one-tailed); partially",
 "new_string": "  criterion: As fig7a-s1-rsu-dc-3000 for S1 FSUs in 201 to 268 ms. The legend does not give the\n    direction of the 0.6% against 30% difference; both one-tailed directions are read, the claim holding\n    under the one the data's means give. Reproduced when exactly 6%, 30% and 60% are significantly\n    above baseline and 0.6% and 30% differ significantly; partially"
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "    rank-sum tests between PRFs under B1 (the ten pairs) and B2, corrected p < 0.01.",
 "new_string": "    rank-sum tests between PRFs under B1 (the five PRFs compared with baseline) and B2 (the ten pairs),\n    corrected p < 0.01."
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "test is significant at p < 0.05 and 1,500 and 3,000 Hz have the two highest mean changes; partially\n    reproduced when it is significant and one of them is among the two highest.",
 "new_string": "test is significant at p < 0.05 and 1,500 and 3,000 Hz have the two highest changes; partially\n    reproduced when it is significant and one of them is among the two highest. The paper does not say\n    whether the preference is read from means or medians; both are read."
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "\"Tended to\" is judged on the means;\n    reproduced",
 "new_string": "\"Tended to\" is judged on the means, and\n    on the medians as a second reading (the paper names neither);\n    reproduced"
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "Run under D1 and D2, D3 and D4,\n    R-independent;",
 "new_string": "Run under D1 and D2, D3 and D4, C1 and\n    C2, R-independent;"
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001199/10.1523-jneurosci.2218-24.2025.yaml",
 "old_string": "  - about: POm RSUs and POm FSUs, during, and all four groups at 201 to 268 ms\n    test: post hoc one-tail two-sample Wilcoxon test after Kruskal-Wallis\n    p: 1.0\n    corrected: Bonferroni\n    n: 67 POm RSUs, 67 POm FSUs",
 "new_string": "  - about: POm RSUs and POm FSUs, during, and all four groups at 201 to 268 ms\n    test: post hoc one-tail two-sample Wilcoxon test after Kruskal-Wallis\n    p: 1.0\n    corrected: Bonferroni\n    n: 31 S1 RSUs, 53 S1 FSUs, 67 POm RSUs, 67 POm FSUs"
}
```

```
The file claims/001199/10.1523-jneurosci.2218-24.2025.yaml has been updated successfully.
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cat >> claims/001199/10.1523-jneurosci.2218-24.2025.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header D, the dSTTC tests were given Bonferroni's correction through T, but the Methods name it for the spiking post hoc tests only; the correction is now open, C1 uncorrected and C2 Bonferroni, and fig10a-dsttc-3000-during runs both.
  - Header D, the 67 ms dSTTC window length is not given by the paper; it is now named as taken from the spiking windows.
  - fig4-no-fsu-change, source changed from paragraphs 1 and 2 to paragraphs 1 and 3 and the Fig. 4 legend, where the S1 FSU 3,000 Hz part is stated; the outcome rule now follows the protocol when the two direction readings differ (methods_underspecified) where it had counted any decrease as not reproduced.
  - fig5a-sham-no-response (and fig5b by reference), the one-tailed direction was fixed to an increase by the agent; the paper does not state it, so increase only and either direction are now both read, with the same outcome rule as fig4-no-fsu-change.
  - fig5a-sham-no-response, the n of the pooled p = 1.0 entry listed only the POm groups though it covers all four groups at 201 to 268 ms; corrected.
  - fig7b-s1-fsu-dc-3000, the criterion required 30% above 0.6%, a direction the Fig. 7B legend does not give; both directions are now read.
  - fig9a-s1-rsu-60dc, B1 was glossed as the ten pairs, which is B2 in the header; corrected to B1 the five PRFs, B2 the ten pairs.
  - fig10d-sttc-60dc and fig10e-sttc-30hz-dc, the ranking was on means only, an agent choice; medians are added as a second reading since the paper names neither.
  - Open, whether dandiset 001199 holds the paper's recordings (the paper names 000946) is for the author to settle from the dataset.
  - Open, the dSTTC equation is lost from the text; the Cutts and Eglen form in header D is a reading, with no other named in the text.
EOF
python tools/claims_check.py claims/001199/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I've checked and corrected the claims file for 001199, and it is ready for an attempt. Nothing is committed.

**Checker:** `claims/001199/10.1523-jneurosci.2218-24.2025.yaml: 35 claims, 35 quotes, 84 statistical values, 0 problems`. It gave the same result before and after my edits.

**Changes, by claim**
- **Header D (dSTTC):**
  - The dSTTC tests had picked up Bonferroni correction through the shared test rule. The Methods name that correction only for the spiking tests; for dSTTC they say only "Post hoc one-tail two-sample Wilcoxon tests were employed". Correction is now open: C1 uncorrected, C2 Bonferroni. `fig10a-dsttc-3000-during` runs both.
  - The paper gives no window length for dSTTC. The header now says the 67 ms windows are borrowed from the spiking analysis.
- **fig4-no-fsu-change:**
  - The source said paragraphs 1 and 2. It now says paragraphs 1 and 3 and the Fig. 4 legend, which is where the "S1 FSUs at 3,000 Hz" part comes from.
  - The outcome rule called the claim not reproduced if only a decrease appeared. Under the increase-only reading it would hold, so the two readings disagree. The rule now blocks the claim as `methods_underspecified` in that case, as the protocol requires.
- **fig5a-sham-no-response** (and fig5b, which refers to it):
  - The writer had fixed the test direction to "increase". The paper doesn't state a direction, so both "increase only" and "either direction" are now read, with the same outcome rule as above.
  - One statistics entry covers all four groups at 201 to 268 ms, but its n listed only the two POm groups. It now lists all four.
- **fig7b-s1-fsu-dc-3000:** The criterion required 30% to be above 0.6%. The legend says only that they differ, so both directions are now read.
- **fig9a-s1-rsu-60dc:** The criterion called B1 "the ten pairs", which is B2 in the header. It now reads B1 as the five PRFs and B2 as the ten pairs.
- **fig10d-sttc-60dc, fig10e-sttc-30hz-dc:** The PRF and DC rankings used means only. The paper names neither means nor medians, so medians are added as a second reading.

**Coverage:** Every main finding in Results, Figs. 2 and 4 to 11, has a claim. All 35 claims come from this paper.

**Still open** (recorded under `checks`):
- The paper says its data are in dandiset 000946, and 001199's description differs from the paper. The author must find out which 001199 sessions, if any, match the paper's conditions.
- The text lost the dSTTC equation. The Cutts and Eglen form in header D is a reading; the text names no other.

**Ready:** yes (`ready: true`).

## End of run

19 turns, 2 minutes, result: success.
