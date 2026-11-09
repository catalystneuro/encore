# 001199 · verifier-2 · run 41367083992

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 380
drwxr-xr-x 6 runner runner    4096 Nov  2 00:32 .
drwxr-xr-x 7 runner runner    4096 Nov  2 00:32 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  2 00:32 .claude
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.development
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.local
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.production
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.test
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .env.test.local
drwx------ 2 runner runner    4096 Nov  2 00:32 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .github
-rw-r--r-- 1 runner runner       0 Nov  2 00:32 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  2 00:24 .mcp.json
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 001199-gao-2025-01.yaml
```

```
<persisted-output>
Output too large (40.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/4a948ed8-ddc1-4248-bbeb-25af1187f305/tool-results/bny8gbfx7.txt

Preview (first 2KB):
# Gao, Ramachandran, Yu & He (2025) from dandiset 001199

Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
tested on [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250). The dandiset holds
sorted units (spike times only) and trial tables from 13 rats, recorded in S1, POm and auditory
cortex (AC) during transcranial focused ultrasound at 30 to 4,500 Hz PRF with 200 us pulses.

| Claim | Outcome |
|---|---|
| Rats with S1 and POm (16) and S1 and AC (12) recordings | Not reproduced |
| RSU and FSU counts of Fig. 4 and Fig. 5 (by upper bounds from untyped units) | Not reproduced |
| AC neurons respond to 1,500 and 3,000 Hz during sonication, and to four PRFs after it | Not reproduced |
| Target determination artefact (Fig. 2) | Blocked: data missing |
| 18 other claims on RSUs and FSUs (Fig. 4 to 6, 10A to 10C, 11C, 11D) | Blocked: data missing |
| 12 claims on the duty-cycle series (Fig. 7 to 9, 10D to 10F) | Blocked: data missing |

[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "README.md"
}
```

```
1	# Gao, Ramachandran, Yu & He (2025) from dandiset 001199
2	
3	Tests the findings of [Gao et al. (2025)](https://doi.org/10.1523/jneurosci.2218-24.2025) that can be
4	tested on [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250). The dandiset holds
5	sorted units (spike times only) and trial tables from 13 rats, recorded in S1, POm and auditory
6	cortex (AC) during transcranial focused ultrasound at 30 to 4,500 Hz PRF with 200 us pulses.
7	
8	| Claim | Outcome |
9	|---|---|
10	| Rats with S1 and POm (16) and S1 and AC (12) recordings | Not reproduced |
11	| RSU and FSU counts of Fig. 4 and Fig. 5 (by upper bounds from untyped units) | Not reproduced |
12	| AC neurons respond to 1,500 and 3,000 Hz during sonication, and to four PRFs after it | Not reproduced |
13	| Target determination artefact (Fig. 2) | Blocked: data missing |
14	| 18 other claims on RSUs and FSUs (Fig. 4 to 6, 10A to 10C, 11C, 11D) | Blocked: data missing |
15	| 12 claims on the duty-cycle series (Fig. 7 to 9, 10D to 10F) | Blocked: data missing |
16	
17	A failure to reproduce here may be a failure of this attempt, not of the paper: see the
18	reasoning and the differences from the paper's method.
19	
20	The files hold no spike waveforms and no RSU or FSU labels (a `celltype_label` column described as
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "001199-gao-2025-01.yaml"
}
```

```
1	schema_version: 2
2	id: 001199-gao-2025-01
3	dataset:
4	  archive: dandi
5	  id: "001199"
6	  version: 0.250829.1250
7	  doi: 10.48324/dandi.001199/0.250829.1250
8	paper: doi:10.1523/jneurosci.2218-24.2025
9	date: 2026-11-01
10	entry: 001199-gao-2025
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 618 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" *.yaml | head; grep -c "^- claim:" 001199-gao-2025-01.yaml; grep -n "^  - claim:\|^- claim:" 001199-gao-2025-01.yaml | wc -l; python3 -c "
import yaml;d=yaml.safe_load(open('10.1523-jneurosci.2218-24.2025.yaml'));print(d.keys());
cl=d['claims'];print(len(cl));print([c['id'] for c in cl])
a=yaml.safe_load(open('001199-gao-2025-01.yaml'));import collections;print(collections.Counter(o['outcome'] for o in a['outcomes']), len(a['outcomes']))
print(set(c['id'] for c in cl)^set(o['claim'] for o in a['outcomes']))
print(collections.Counter(o.get('blocked_by') for o in a['outcomes']))
"
```

```
35
70
dict_keys(['schema_version', 'dataset', 'paper', 'claims', 'checks'])
35
['subjects', 'fig2-target-artifact', 'fig4-unit-counts', 'fig4-timelocked-rsu-3000', 'fig4-postsonication-3000', 'fig4-30hz-responses', 'fig4-no-fsu-change', 'fig5-unit-counts', 'fig5a-sham-no-response', 'fig5b-cg1-control-no-response', 'fig6-unit-counts', 'fig6a-s1-rsu-timelocked-high-prf', 'fig6a-s1-rsu-delayed', 'fig6b-s1-fsu-prf', 'fig6c-pom-rsu-prf', 'fig6d-pom-fsu-prf', 'fig7-9-unit-counts', 'fig7a-s1-rsu-dc-3000', 'fig7b-s1-fsu-dc-3000', 'fig7c-pom-rsu-dc-3000', 'fig7d-pom-fsu-dc-3000', 'fig8a-s1-rsu-dc-30', 'fig8b-s1-fsu-dc-30', 'fig9a-s1-rsu-60dc', 'fig9b-s1-fsu-60dc', 'fig10a-dsttc-3000-during', 'fig10a-dsttc-3000-post', 'fig10b-dsttc-30', 'fig10c-sttc-constant-pd', 'fig10d-sttc-60dc', 'fig10e-sttc-30hz-dc', 'fig10f-sttc-3000-dc', 'fig11b-ac-responses', 'fig11c-ac-to-s1-30hz', 'fig11d-ac-to-s1-3000']
Counter({'blocked': 31, 'not_reproduced': 4}) 35
set()
Counter({'data_missing': 31, None: 4})
```

**Agent calls Bash**

```bash
cd  python3 - <<'E' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_gao_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"=================== CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('----- OUT')
        if 'text' in o: print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']; print(''.join(d.get('text/plain','')) if 'text/plain' in d else list(d))
        elif o.get('output_type')=='error': print(o['ename'],o['evalue'])
E
wc -l $TMPDIR/nb.txt; grep -n "=== CELL" $TMPDIR/nb.txt
```

```
1534 /tmp/claude-1001/nb.txt
1:=================== CELL 0 [markdown]
41:=================== CELL 1 [code]
93:=================== CELL 2 [code]
114:=================== CELL 3 [markdown]
118:=================== CELL 4 [code]
278:=================== CELL 5 [markdown]
289:=================== CELL 6 [code]
369:=================== CELL 7 [markdown]
378:=================== CELL 8 [code]
460:=================== CELL 9 [markdown]
476:=================== CELL 10 [code]
526:=================== CELL 11 [code]
581:=================== CELL 12 [code]
862:=================== CELL 13 [markdown]
898:=================== CELL 14 [code]
966:=================== CELL 15 [markdown]
976:=================== CELL 16 [markdown]
996:=================== CELL 17 [code]
1096:=================== CELL 18 [markdown]
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 600
}
```

```
1	=================== CELL 0 [markdown]
2	# Reproducing Gao et al. (2025) from dandiset 001199
3	
4	Paper. Gao H, Ramachandran S, Yu K, He B (2025). Transcranial Focused Ultrasound Modulates
5	Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory
6	Neurons. *J Neurosci* 45(23):e2218242025.
7	[doi:10.1523/jneurosci.2218-24.2025](https://doi.org/10.1523/jneurosci.2218-24.2025). The claims
8	file was written from the version of record in PubMed Central (PMC12139594), with its Methods and
9	all figure legends; the paper has no supplement.
10	
11	Dandiset. [DANDI:001199](https://dandiarchive.org/dandiset/001199/0.250829.1250), version
12	0.250829.1250. The paper does not cite this dandiset: its Methods name dandiset 000946 as the
13	repository of all its data, with no version. 001199 has four published versions (0.250712.1551,
14	0.250713.1101, 0.250828.1941, 0.250829.1250). The cell below shows that all four and the draft
15	hold the same 229 files (same paths and blobs) and differ only in metadata the analysis does not
16	use (the order of contributors). The most recent published version is pinned, as the protocol
17	says when the paper cites none.
18	
19	What the dandiset holds. Sorted units (spike times only) and trial tables for 13 rats, recorded
20	in August and September 2024 (4 rats) and February to July 2025 (9 rats). There are no spike
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 600,
 "limit": 500
}
```

```
600	        continue
601	    lags, z = tfus.onset_correlogram(sp, f["trial_start"])
602	    w = (lags >= 0) & (lags <= 0.4)
603	    rows.append({"cohort": r.cohort, "rat": r.rat, "rec": r.rec, "target": r.target, "prf": r.prf, "units": len(sp),
604	                 "session": r.trial_key, "peak_lag_s": lags[z.argmax()], "peak_z": z.max(), "max_z_0_400ms": z[w].max(), "z": z})
605	xc = pd.DataFrame(rows)
606	xc["kind"] = np.where(xc.target == "none", "sham", "stimulated")
607	xc["peak_in_0_400ms"] = xc.peak_lag_s.between(0, 0.4)
608	print("\nPeak of the correlogram over -60 to +60 s, per file (chance of a peak in 0-400 ms: 0.4/120 = 0.3%):")
609	print(xc.groupby(["cohort", "kind"]).agg(files=("units", "size"), peak_in_0_400ms=("peak_in_0_400ms", "sum"),
610	                                         median_peak_z=("peak_z", "median"), median_max_z_0_400ms=("max_z_0_400ms", "median")).round(2).to_string())
611	for (c, k), g in xc.groupby(["cohort", "kind"]):
612	    m = np.mean(np.stack(g.z.values), axis=0)
613	    top = np.argsort(m)[::-1][:3]
614	    h, e = np.histogram(g.peak_lag_s, np.arange(-60, 60.01, 0.5))
615	    print(f"{c} {k}: mean z over files peaks at lags {[f'{v:.2f}' for v in lags[top]]} s (z {[f'{v:.2f}' for v in m[top]]}); "
616	          f"most files with a peak in one 0.5 s bin: {h.max()} (bin from {e[h.argmax()]:.1f} s)")
617	
618	# (3) Every 2025 session (files sharing a trial table): peak lag and z per file.
619	s25 = xc[xc.cohort == "2025"].sort_values(["rat", "prf", "rec"])
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1096,
 "limit": 440
}
```

```
1096	=================== CELL 18 [markdown]
1097	**Result: not reproduced.** The dandiset holds simultaneous S1 and POm recordings from 6 rats
1098	(paper 16) and S1 and AC recordings from 6 rats (paper 12), under both readings of the targets and
1099	whether a session's areas come from units with more than 2,000 spikes or from every unit. Both
1100	counts are below the paper's, but the criterion's partial result also needs the rats to be a subset
1101	of the paper's, none extra, and the evidence printed above goes against that. Every S1 file lists a
1102	64-channel A1x64-Edge probe (or H9), where the paper recorded S1 with a 32-channel A1x32-Poly3.
1103	Two rats (BH648, BH658) are in both groups, where the paper's AC rats are "another group of rats".
1104	The ten rats of the two groups were recorded from August 2024 to July 2025, after the paper's
1105	preprint (June 2024), and none is in dandiset 000946, the repository the paper names, whose 20
1106	rats were recorded from August 2023 to April 2024; of the 13 rats here only BH594, which has no
1107	POm or AC recording, is there. With the 2025 cohort left out the counts are 2 and 0.
1108	=================== CELL 19 [markdown]
1109	## fig4-unit-counts
1110	
1111	> In the constant-PD sessions at 3,000 Hz there were 312 RSUs and 54 FSUs in S1 and 233 RSUs and
1112	> 17 FSUs in POm; at 30 Hz there were 148 RSUs and 61 FSUs in S1 and 189 RSUs and 43 FSUs in POm.
1113	
1114	Criterion: units selected and typed as in U, in the 3,000 Hz/200 us and 30 Hz/200 us sessions,
1115	counted once per session; reproduced when all eight counts are within 10%, partially when at least
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import yaml
d=yaml.safe_load(open('10.1523-jneurosci.2218-24.2025.yaml'))
for k,v in d.items():
    if k!='claims': print(k, yaml.safe_dump(v, width=150)[:6000])
for c in d['claims']:
    if c['id'] in ('subjects','fig4-unit-counts','fig5-unit-counts','fig6-unit-counts','fig7-9-unit-counts','fig11b-ac-responses'):
        print(yaml.safe_dump(c, width=150))
E
```

```
schema_version 2
...

dataset archive: dandi
id: 001199

paper doi:10.1523/jneurosci.2218-24.2025
...

checks - changes:
  - Header D, the dSTTC tests were given Bonferroni's correction through T, but the Methods name it for the spiking post hoc tests only; the correction
    is now open, C1 uncorrected and C2 Bonferroni, and fig10a-dsttc-3000-during runs both.
  - Header D, the 67 ms dSTTC window length is not given by the paper; it is now named as taken from the spiking windows.
  - fig4-no-fsu-change, source changed from paragraphs 1 and 2 to paragraphs 1 and 3 and the Fig. 4 legend, where the S1 FSU 3,000 Hz part is stated; the
    outcome rule now follows the protocol when the two direction readings differ (methods_underspecified) where it had counted any decrease as not reproduced.
  - fig5a-sham-no-response (and fig5b by reference), the one-tailed direction was fixed to an increase by the agent; the paper does not state it, so increase
    only and either direction are now both read, with the same outcome rule as fig4-no-fsu-change.
  - fig5a-sham-no-response, the n of the pooled p = 1.0 entry listed only the POm groups though it covers all four groups at 201 to 268 ms; corrected.
  - fig7b-s1-fsu-dc-3000, the criterion required 30% above 0.6%, a direction the Fig. 7B legend does not give; both directions are now read.
  - fig9a-s1-rsu-60dc, B1 was glossed as the ten pairs, which is B2 in the header; corrected to B1 the five PRFs, B2 the ten pairs.
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -80 10.1523-jneurosci.2218-24.2025.yaml; grep -n -i "CG1\|cingulate\|control group\|control condition" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -o ".\{80\}\(preprint\|biorxiv\|received\|2024\).\{80\}" paper/*.txt | head; grep -n -i "4,224\|4224\|places per unit\|seven places" *.ipynb *.yaml tfus.py | head
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round 2 verification: 001199-gao-2025-01**

I counted from the claims file and the attempt record. There are 35 claims and 35 outcomes: 4 are not_reproduced (subjects, fig4-unit-counts, fig5-unit-counts, fig11b-ac-responses) and 31 are blocked, all as data_missing. No outcome carries `assumed: true`.

### 1. Outcomes

| Claim | Agree? | Comment |
|---|---|---|
| subjects | Yes | Cell 17 gives 6 and 6 rats under every reading, and 2 and 0 without the 2025 cohort. The "none extra" evidence now prints: 138 of 138 S1 files list an A1x64-Edge probe or H9; BH648 and BH658 are in both groups; none of the 10 rats is in 000946. |
| fig4-unit-counts | Yes | Cell 20: at most 4 of 8 counts can be within 10%, and a partial result needs 6. The bound is valid because keeping all 2025 files and the S1-6 sessions can only raise it. |
| fig5-unit-counts | **No longer** (I am revising my round-1 view) | The sham half fails only the 2 POm counts (37 units, cell 23). The other failures all come from CG1 sessions at 300 and 4,500 Hz. The paper's control, and the claims-file header, is CG1 at 3,000 Hz, and the dandiset has none. Counting other-PRF CG1 sessions does not bound units in sessions that are not deposited. The deviation's "can only raise the bounds" does not hold for that reason. fig7-9-unit-counts and fig5b treat an absent condition as data_missing. Treated the same way here, at most 2 of 8 counts are ruled out and a partial result (6 of 8) stays possible. So the outcome should be blocked (data_missing), or else carry `assumed: true` with the assumption stated: that the dandiset's CG1 sessions are the paper's control. |
| fig6-unit-counts | Yes (blocked) | Cell 26: at most 2 of 4 totals can be within 10%, which leaves a partial result open. I accept data_missing over my metadata_insufficient: the paper types units from waveforms, which are absent, and the label column is recorded as a metadata_error. |
| fig7-9-unit-counts and the 11 duty-cycle claims | Yes (blocked) | Cell 6: every stimulated file is PD 200, and the 26 files with no PD are the 26 sham files. |
| fig2-target-artifact, fig5b, and the 16 other type-dependent claims | Yes (blocked, data_missing) | Cell 4: 0 of 96 files hold a 1 or 2 in `celltype_label`. |
| fig11b-ac-responses | Yes, not_reproduced | 194 units against 453 ± 45.3. 3,000 Hz is never significant and nothing is significant after sonication (cells 28–29). The fallback reading of the assumptions does not apply, because the count and pattern fail under every variant. |

**Assumptions.** fig11b rests on two assumptions that are stated only as deviations, not as `assumed: true`: that the 2025 files were recorded at 5 V, and that the 2025 trial starts are sonication onsets. Both should be flagged. Both are reasonable:
- Nothing in the files states another voltage.
- Several printed outputs support the onset assumption more than the record admits (see item 2b).

### 2. Sentences not supported by the printed outputs

a. **Attempt record, format_error finding:** "Left unsorted they gave one AC unit a normalized rate of 4,224%". No output shows this. Cell 9 and the same finding also say "(one to seven places per unit)"; cell 8 prints only unit counts per rat.

b. **Cell 13, and the fig11b notes:** "untyped S1 units do not give a positive control that could separate the two explanations". The statement that T1 is not significant in 2025 is literally true. But in cell 12, T2 gives the following for 2025 S1 units:

| PRF | Window | p |
|---|---|---|
| 30 Hz | 0–67 ms | 7e-07 |
| 30 Hz | 201–268 ms | 1.6e-12 |
| 1,500 Hz | 0–67 ms | 2.7e-12 |
| 1,500 Hz | 201–268 ms | 8.1e-10 |

The sham AC units give T2 p = 0.57 (cell 29), so the test is not biased. A consistent rise right after the trial starts is locking to those starts. The notebook dismisses these results because the means are only 107–109%. Yet fig11b counts 1,500 Hz in AC as significant at a mean of 105.1% under the same T2 test. The inconsistency affects the stated "low confidence": it weakens the claim that the AC null "may come from the trial tables".

c. **Cell 30 and fig11b notes:** "with BH654 left out the R2 tests give 0.0095 and 0.006, with every R2 mean below 100%". The R2 means of that variant are not printed; cell 29 prints only KW_p, sig and lowest for it.

d. **Cell 13:** "Other files show the paper's delayed increase, from about 125 to 200 ms." The printed PSTHs (cell 11) show rises from about 200–300 ms: BH648 S1 reaches 118% at 225 ms and BH615 300 Hz reaches 110% at 300 ms. Nothing rises at 125 ms, and the BH594 files show no clear rise.

e. **Cell 15:** "as the 64-channel probes of BH594 give many units at 10 and 15 V". Per-rat counts are printed only for the 5 V set.

f. **Cell 9:** "one 2024 baseline has 400 and two 2025 sham files 149". The output gives the counts of files with each trial number, not which files they are.

g. **README:** the fig11b row says only "Not reproduced". It does not carry the low-confidence qualifier that the Summary (cell 31) and the record give.

Everything else checks against the outputs, including the Summary, the subjects, fig4 and fig5 results (cells 18, 21, 24), the counts, bounds, p-values, correlogram figures and per-rat ranges.

**My round-1 reasons in the record:** they are stated faithfully, nearly in my words, including the metadata_insufficient remark. One small misattribution: under subjects, the record appends my problem 7, which I had marked "does not affect a conclusion".

### 3. Round-1 points

**Resolved:**
- 1: fig4 and fig5 bounds, and the fig6 bound.
- 2: the main set is now 5 V, and the 2025 voltage assumption is stated in the sections and the Summary.
- 3: the "none extra" evidence is printed.
- 5: the R2 bias is accepted as not a misreading, and the outcome does not change.
- 6: PD parsing is checked in cell 6.
- 7: the more-than-2,000-spikes rule is applied, with a variant.
- 8: the variants are shown.
- All of my section C requests: per-file label counts, 2025 voltage, subject variants, trial-time span, correlogram and positive control.
- Blocked_by: I withdraw my metadata_insufficient. data_missing is reasonable.

**Partly resolved:**
- 4: the requested outputs now exist, but the notebook reads them selectively (item 2b).

**Remaining issues that bear on a conclusion:**
1. **fig5-unit-counts:** handling the absent CG1 sessions at 3,000 Hz as bounded by CG1 at other PRFs is inconsistent with fig7-9 and fig5b. On consistent treatment the outcome should be blocked, or the substitution should be marked `assumed: true`.
2. **fig11b:** the outcome should carry `assumed: true` for the 2025 trial starts being onsets and the 2025 voltage being 5 V. The conclusion about the positive control (cell 13 and the record's notes) should state the T2 results. Those results support locking in at least the 30 and 1,500 Hz sessions. The outcome itself does not change.

## End of run

13 turns, 3 minutes, result: success.
