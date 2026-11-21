# fritsche-2022 · recorder · run 44885264196

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py fritsche-2022; ls transcripts/fritsche-2022/; cat attempts/fritsche-2022-01.yaml; cat claims/fritsche-2022.yaml
```

```
<persisted-output>
Output too large (101.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/318547e8-41c7-47ce-800b-bf2328dab461/tool-results/b9laqze6e.txt

Preview (first 2KB):
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
| [000021](https://dandiarchive.org/dandiset/000021) | [Fritsche et al. 2022](https://doi.org/10.1523/jneurosci.1350-21.2021) | 26 | 3 | 2 | 0 | [`fritsche-2022`](entries/fritsche-2022) |
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
[... 45 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/318547e8-41c7-47ce-800b-bf2328dab461/tool-results/b9laqze6e.txt"
}
```

```
1	docs/pilot-notes/amjad-2025-01.md
2	docs/pilot-notes/andrews-2024-01.md
3	docs/pilot-notes/armstrong-2026-01.md
4	docs/pilot-notes/asari-2009-01.md
5	docs/pilot-notes/asari-2009-02.md
6	| [000021](https://dandiarchive.org/dandiset/000021) | [Fritsche et al. 2022](https://doi.org/10.1523/jneurosci.1350-21.2021) | 26 | 3 | 2 | 0 | [`fritsche-2022`](entries/fritsche-2022) |
7	author-report.md
8	author-revise-1-report.md
9	author-revise-1.md
10	author-revise-2-report.md
11	author-revise-2.md
12	author.md
13	claims-check-report.md
14	claims-check.md
15	claims-report.md
16	claims.md
17	verifier-1-report.md
18	verifier-1.md
19	verifier-2-report.md
20	verifier-2.md
[... 872 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/318547e8-41c7-47ce-800b-bf2328dab461/tool-results/b9laqze6e.txt",
 "offset": 893,
 "limit": 130
}
```

```
893	      It bears weakly on the conclusion.
894	    response: No change. The family is the claims file's reading; the family 1 to 50 results stay in the
895	      notes.
896	  - claim: fig7b-static-cortex-decay
897	    agrees: true
898	    outcome: reproduced
899	    reason: Agrees with the stated outcome, which matches the verifier's round-1 outcome.
900	    response: No change.
901	  - claim: fig7-static-lgn-single
902	    agrees: true
903	    outcome: reproduced
904	    reason: Agrees with the stated outcome, which matches the verifier's round-1 outcome.
905	    response: No change.
906	  - claim: fig7b-static-areas-long-term
907	    agrees: true
908	    outcome: reproduced
909	    reason: Agrees with the stated outcome, which matches the verifier's round-1 outcome. Remaining from
910	      round 1 (problem 4), with the 1-to-20 family the 18-to-22 test is partly met by construction, and
911	      with 1 to 50 the largest significant n is 46 to 49. This is the claims file's reading, reported.
912	      It bears weakly on the conclusion.
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02; do echo "== $f"; cat docs/pilot-notes/$f.md; done; head -5 docs/pilot-notes/knierim-2000-02.md; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000021' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
"; ls summaries | head;
```

```
<persisted-output>
Output too large (34.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/318547e8-41c7-47ce-800b-bf2328dab461/tool-results/bfmbv1j3i.txt

Preview (first 2KB):
== amjad-2025-01
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
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/318547e8-41c7-47ce-800b-bf2328dab461/tool-results/bfmbv1j3i.txt"
}
```

```
1	== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 494 more lines not kept]
```

**Agent**

Read the record, the claims header, and the five most recent notes. Next: the dataset entry, the reports and a couple of example summaries.

**Agent calls Bash**

```bash
cd  grep -n -B3 -A20 '"000021"' targets/dandisets.json | head -50; cat summaries/asari-2009-02.md summaries/armstrong-2026-01.md; wc -w transcripts/fritsche-2022/*-report.md
```

```
The paper's central finding held in this data: A1 responses depend on the preceding sound for seconds, the context-dependent power decaying with a time constant of about 1 s as reported, while in the thalamus (MGB) the effect fades fast. Fewer probes showed significant context dependence than reported, the bound on short-window models rose more slowly, and longer STRF windows did improve predictions, under a fold averaging the paper does not describe. Amplitude and frequency changes outlasted modulation and higher-order changes, but the proportions did not match, on stimulus groupings rebuilt because the paper does not list them. The synaptic conductance findings could not be tested, as the data set holds no voltage-clamp recordings.
None of the paper's main findings could be confirmed in this data, and most could not be tested. The staged spiking modulation and its ramp could not be tested, because the spike times are not on the trial clock and the files hold no synchronisation signal. The whisker and wall findings could not be tested, because only 2 of the 19 animals are present and the files hold no whisker tracking. Where tests ran, the population baseline rate was about 7 Hz against the reported 2 Hz, and the turn success rate was 0.61 to 0.69 against 0.95. The drift diffusion fit only partly held, since its nondecision time missed 0.12 s.
  906 transcripts/fritsche-2022/author-report.md
  556 transcripts/fritsche-2022/author-revise-1-report.md
  533 transcripts/fritsche-2022/author-revise-2-report.md
  500 transcripts/fritsche-2022/claims-check-report.md
  659 transcripts/fritsche-2022/claims-report.md
 1715 transcripts/fritsche-2022/verifier-1-report.md
  870 transcripts/fritsche-2022/verifier-2-report.md
 5739 total
```

**Agent calls Bash**

```bash
cd  grep -n '000021' targets/dandisets.json | head; head -c 600 targets/dandisets.json; cd transcripts/fritsche-2022; cat author-report.md author-revise-1-report.md author-revise-2-report.md
```

```
{
 "schema_version": 1,
 "generated": "2026-11-17T15:59:44+00:00",
 "source": "https://api.dandiarchive.org/api",
 "counts": {
  "public_dandisets": 678,
  "with_a_paper": 298,
  "with_a_published_version": 256,
  "papers": 316,
  "converted_by_catalystneuro": 51
 },
 "targets": [
  {
   "dandiset": "000003",
   "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
   "published_version": "0.260218.2052",
   "asset_count": 101,
   "size_gb": 1922.23,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
for e in d['targets']:
  if e['dandiset']=='000021': print(json.dumps(e,indent=1))
E
cat transcripts/fritsche-2022/claims-report.md transcripts/fritsche-2022/claims-check-report.md; ls questions/ | grep fritsche; ls docs/pilot-notes | grep -c .
```

```
I wrote `claims/fritsche-2022.yaml`. The quote checker finds no problems (29 claims, 29 quotes, 80 statistical values), and no value contains ": ", an em dash or "rather". Nothing is committed.

**Text read.** The version of record (J Neurosci 2022, PMC8916757), all of it: Methods, Results, Discussion, the legends of Figs. 1 to 8, and Tables 1 and 2. The paper has no supplement. The text file had lost the display equations, and there is no PDF, so I read the five formulas from the MathML on the same PMC page: the adaptation ratio, the single and double exponential, the orientation selectivity index (OSI), and the cumulative product. I opened no figures.

**Code not read.** The paper's code is at doi:10.34973/kpt9-y956. Its file list is public, but every script returned HTTP 401 because it sits behind a data use agreement. No criterion rests on the code.

**Claims.** 29 claims, all with quotes (none inferred), 19 with statistics, 15 with expected values, and all 29 with a criterion. They cover:
- unit counts;
- 1-back adaptation in V1, the extrastriate areas and the thalamus, for drifting and for static gratings;
- consistency across mice (Figs. 1E, 3C, 6D);
- the Fig. 2 tuning ANOVA (main effect, interaction, adaptation at each orientation, and its absence in the thalamus);
- long-term adaptation in V1 (8-back for drifting, 20-back for static);
- the exponential fits and F tests from Tables 1 and 2, and the ~14 s half-life;
- cumulative adaptation and its linearity (Fig. 4);
- the V1 against thalamus Welch tests;
- the blank-baseline analysis (Fig. 5);
- the simulation with no spurious long-term effect (Fig. 8);
- the robustness variants.

All use `data: dataset`.
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '"dandiset": "0000[0-9]*"' targets/dandisets.json | head -20; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(d['targets'][0].keys())"
```

```
14:   "dandiset": "000003",
43:   "dandiset": "000004",
71:   "dandiset": "000005",
98:   "dandiset": "000006",
125:   "dandiset": "000007",
151:   "dandiset": "000008",
177:   "dandiset": "000009",
205:   "dandiset": "000010",
233:   "dandiset": "000011",
260:   "dandiset": "000013",
287:   "dandiset": "000015",
314:   "dandiset": "000016",
346:   "dandiset": "000017",
373:   "dandiset": "000019",
399:   "dandiset": "000023",
423:   "dandiset": "000026",
481:   "dandiset": "000034",
507:   "dandiset": "000035",
534:   "dandiset": "000036",
559:   "dandiset": "000037",
[... 1 more lines not kept]
```

**Agent**

The dataset 000021 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to report. Now the verifier reports.

**Agent calls Bash**

```bash
cd transcripts/fritsche-2022; cat verifier-1-report.md | head -80; echo ======; cat verifier-2-report.md | head -60
```

```
**A. Outcomes**

The claims file holds 31 claims, and the notebook tests all 31; none is treated as blocked. My outcomes: 26 reproduced, 3 partially reproduced, 2 not reproduced.

| Claim | Outcome | Reason |
|---|---|---|
| units-responsive-count | reproduced | Cell 14, reading ace with `good` units only: total 2422, V1 580, LGN 142, LP 91, all within tolerance, and the 8 named regions are kept. Reading ade without the `good` filter also passes. |
| fig1d-v1-1back | reproduced | Cell 19: V1 ratio 0.821, inside [0.81, 0.84]; p = 6e-58 (FDR 2.4e-57); 580 units. |
| fig1d-extrastriate-1back | reproduced | Cell 21: ratios 0.795 to 0.876, all in [0.72, 0.968]; largest FDR p 2e-24. |
| fig1d-thalamus-1back | reproduced | Cell 23: LGN 0.935 (CI [0.91, 0.96]), p 6.7e-7; LP 0.833 (CI [0.79, 0.88]), p 1.7e-10. |
| fig1e-consistent-across-mice | partially_reproduced | Cell 26: cortex 32/32 mice meet (a). Thalamus 21/23 fails (a), but the sign test passes (p 6.6e-5), so only (b) holds there. The criterion makes that partial. |
| fig2-v1-tuning-main-effect | reproduced | Cell 29: main effect p 3.1e-9 (log ratios, 45° pooled) and p < 1e-9 in all four readings; the 0° ratio is lowest (0.799 < 0.875 < 0.927). |
| fig2-v1-tuning-interaction | reproduced | Cell 31: interaction p 0.011 (log) to 6e-7 (ratio). The spread across orientations is largest in the high-OSI tertile (0.248, against 0.057 and 0.125). |
| fig2-v1-adaptation-at-all-orientations | reproduced | Cell 33, 45° pooled with BH over the 9 V1 cells or over all 72 cells: 8/8 cells below 1, and the high-OSI 90° cell has p 0.92 (ratio 0.993). |
| fig2-thalamus-no-tuning-dependence | reproduced | Cell 35: no main effect or interaction is significant under any reading (LGN p_rel 0.073 to 0.28; LP ≥ 0.66). |
| fig3a-v1-long-term | reproduced | Cell 38, main reading: significant at 1 to 8, 8-back FDR p 0.022, 9-back p 0.09. |
| fig3a-v1-double-exponential | reproduced | Cell 41: a_fast 14.21, tau_fast 0.816, a_slow 3.755, tau_sl
[... 100 more lines not kept]
```

**Agent**

I have what I need. Writing the notes and the summary.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/fritsche-2022-01.md",
 "content": "# fritsche-2022, Fritsche et al. 2022\n\nTwenty-six claims reproduced, three partially, two not reproduced and none\nblocked; two outcomes, `fig3b-thalamus-short-term` and\n`decay-thalamus-single`, rest on an assumption. The first verification round\nagreed with 30 of the 31 outcomes; it gave `fig5-repeat-suppression` not\nreproduced where the record had partial, the author changed it, and the\nsecond round agreed with all 31, so there was no third round. It pins\nversion 0.251116.2246, the only published version; the paper cites none.\nThe paper, Fritsche, Solomon and de Lange, \"Brief Stimuli Cast a Persistent\nLong-Term Trace in Visual Cortex\" (J Neurosci 42(10):1999-2010), reanalyses\nthe Allen Brain Observatory Neuropixels recordings of 32 mice and reports\nthat the response to a grating is reduced when a grating of the same\norientation came n trials before, up to 8 trials back for drifting and 20\nfor static gratings in visual cortex, decaying as a double exponential with\na half-life of about 14 s, while in LGN and LP it is limited to the last one\nor two trials. The claims were written from the version of record\n(PMC8916757), which has no supplement, with the display equations read from\nits MathML and no figure opened; the paper's code at doi:10.34973/kpt9-y956\nis behind a data use agreement and every script returned HTTP 401, so the\ndetails the Methods leave open were named with their readings, and the\nclaims check added two claims, for 31. The adopted reading was the one the\nunit counts point to, and under it the 1-back values match the paper to\nwithin 0.01 for drifting gratings and static cortex. Reproduced are the unit\ncounts (2422; V1 580, LGN 142, LP 91), the 1-back ratios in every region\n(V1 0.821, static 0.897), the Figure 2 tuning effects, V1 adaptation to\n8-back with all four Table 1 estimates inside their intervals and a\nhalf-life of 13.96 s, the cumulative adaptation, the decay fits of Tables 1\nand 2 and the static long-term adaptation. `fig3b-thalamus-short-term`\npasses in 1 of 12 readings, with RL at the threshold of 6, and only if\nsignificant adaptation counts ratios below 1 and the units labelled `noise`\nare left out; with either changed it fails. Partial are the three\nacross-mice claims of Figures 1E, 6D and 7C, which hold by sign test while a\nfew mice fail, in the thalamus mice with 2 to 4 units. Not reproduced are\n`fig5-repeat-suppression`, where orthogonal over blank is still below 1 at\n2-back (0.972) under every reading and seed and in a session bootstrap, and\n`fig8-no-spurious-long-term`, seed sensitive, whose criterion asks every\ninterval of the simulated neuron to contain 1, which noise alone breaks at\nabout the chance rate (38.0% of 200 further seeds pass); both verifiers read\nthis as the claims file's misreading, and it went to a reader in\n`questions/fritsche-2022.yaml`. The author's first run gave 26 reproduced, 4\npartially and 1 not reproduced. Round 1 asked for the invalid intervals to\nbe applied as a variant, the Figure 2 units dropped per tertile, a two-sided\ncount for Figure 3B, 200 seeds for Figure 8, the thalamic units of the mice\nthat fail and a session bootstrap for Figure 5, all added. Round 2 asked for\nthe Figure 3B readings with `noise` units kept, which then met no reading,\nand found sentences the outputs did not support (seven of 12 readings, not\neight; a p range starting at 4.5e-09; the ground truth inside the interval\nin the six named runs, not in every run; the 1-back match not holding for\nstatic thalamus, LGN 0.957 against 0.93 and LP 0.900 against 0.85), all\ncorrected. The first full notebook run failed on a missing cell boundary\nthat left a function in a markdown cell; the notebook ran in 492 s at first,\nwith peak memory about 3.2 GB, and in 367 s after round 1.\n\nThe units table holds all 74658 sorted units, with a `quality` column\nmarking 20182 as `noise` and the AllenSDK quality metric columns, none of\nthem described in the files; the paper's counts are matched when the\n`noise` units are left out, as the AllenSDK's units table does, nothing in\nthe files says they should be, and keeping them changes the thalamic\nresults (LGN gains a significant 7-back and its tau falls to 0.000). Of the\nunits that pass the quality metrics, 3723 sit on channels whose area is\n`grey` and 686 on `VIS`, labels that name no structure, and they reach the\npaper's 50 responsive units for a region; they are left out. Thirteen\nsessions list invalid intervals tagged with a probe, totalling 12 to 2931 s,\nseveral overlapping the grating epochs (375 drifting presentations in 5\nsessions, 7001 static in 10); their meaning is not described, the paper does\nnot mention them, and leaving those presentations out changes the 1-back\nratios by at most 0.014. Three sessions (715093703, 719161530, 721123822)\nhold 598 drifting gratings in place of 600, and static blank sweeps number\n189 to 197 of 6000 presentations per session, about one in 31, where the\nMethods say about one in 25. The checks passed: 32 mice, one session each,\nwith the paper's genotypes, stimuli as the Methods describe, no recording or\nunit deposited twice, and V1 tuning locked to the stimulus tables in every\nsession. Three questions are put to the paper's authors: whether Figure 3B's\nborders include ratios significantly above 1, what rate and noise model the\nFigure 8 simulated neuron used and which interval, and whether the `noise`\nunits were left out.\n\nThe author's points on the protocol: it says the outcome is the one all\nreadings give, while the claims file's criteria say reproduced under one\nreading, and the claims file was followed; nothing says whether a\nsignificant n-back counts ratios above 1, and adaptation only was assumed\nwith both shown; a filter outside the listed readings, the `noise` label,\nwas treated as an assumption with the key results run without it; it does\nnot say whether each region's bootstrap takes its own seed, and every\nregion took the claim's seed; `archives.md` does not say how to get the S3\nURL, and as the download redirect returned 403 the asset metadata's\n`contentUrl` was used; and with no partial rule in the fig5 criterion the\nprotocol's general definition was used, while the strict fig8 criterion\nfails on tiny chance exclusions.\n"
}
```

```
File created successfully at: docs/pilot-notes/fritsche-2022-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat > summaries/fritsche-2022-01.md <<'E'
The paper's main findings held up in this data. In mouse visual cortex the response to a grating was reduced when a grating of the same orientation came up to 8 trials earlier, decaying with a half-life of about 14 s, while in the thalamus adaptation was limited to the last one or two trials. Adaptation strength by tuning, its accumulation over trials and the longer trace after static gratings also reproduced. The blank-baseline analysis did not: suppression after an orthogonal grating lasted to 2-back, not only 1-back. Consistency across mice held only by sign test, and the simulation control failed a criterion that chance noise alone breaks.
E
wc -w summaries/fritsche-2022-01.md; git status --short
```

```
108 summaries/fritsche-2022-01.md
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
?? docs/pilot-notes/fritsche-2022-01.md
?? scripts
?? summaries/fritsche-2022-01.md
```

**Agent calls Bash**

```bash
cd  cat > summaries/fritsche-2022-01.md <<'E'
The paper's main findings held up in this data. In mouse visual cortex the response to a grating was reduced when a grating of the same orientation came up to 8 trials earlier, decaying with a half-life of about 14 s, while in the thalamus adaptation was limited to the last one or two trials, a result that rests on two reading choices. Adaptation by tuning, its accumulation over trials and the longer trace after static gratings also reproduced. The blank-baseline analysis did not: suppression after an orthogonal grating lasted to 2-back, not only 1-back. A few thalamic mice broke the across-mice consistency, and the simulation control failed a criterion that chance noise alone breaks.
E
wc -w summaries/fritsche-2022-01.md
```

```
115 summaries/fritsche-2022-01.md
```

**Agent calls Bash**

```bash
cd  sed -i 's/A few thalamic mice broke/A few mice broke/' summaries/fritsche-2022-01.md; wc -w summaries/fritsche-2022-01.md; grep -c '—\|rather' summaries/fritsche-2022-01.md docs/pilot-notes/fritsche-2022-01.md
```

```
114 summaries/fritsche-2022-01.md
summaries/fritsche-2022-01.md:0
docs/pilot-notes/fritsche-2022-01.md:0
```

**Agent**

I wrote both files and changed nothing else; nothing is committed. Dataset 000021 has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field, and the notes do not open with the CatalystNeuro sentence.

**`docs/pilot-notes/fritsche-2022-01.md`**

# fritsche-2022, Fritsche et al. 2022

Twenty-six claims reproduced, three partially, two not reproduced and none blocked; two outcomes, `fig3b-thalamus-short-term` and `decay-thalamus-single`, rest on an assumption. The first verification round agreed with 30 of the 31 outcomes; it gave `fig5-repeat-suppression` not reproduced where the record had partial, the author changed it, and the second round agreed with all 31, so there was no third round. It pins version 0.251116.2246, the only published version; the paper cites none. The paper, Fritsche, Solomon and de Lange, "Brief Stimuli Cast a Persistent Long-Term Trace in Visual Cortex" (J Neurosci 42(10):1999-2010), reanalyses the Allen Brain Observatory Neuropixels recordings of 32 mice and reports that the response to a grating is reduced when a grating of the same orientation came n trials before, up to 8 trials back for drifting and 20 for static gratings in visual cortex, decaying as a double exponential with a half-life of about 14 s, while in LGN and LP it is limited to the last one or two trials. The claims were written from the version of record (PMC8916757), which has no supplement, with the display equations read from its MathML and no figure opened; the paper's code at doi:10.34973/kpt9-y956 is behind a data use agreement and every script returned HTTP 401, so the details the Methods leave open were named with their readings, and the claims check added two claims, for 31. The adopted reading was the one the unit counts point to, and under it the 1-back values match the paper to within 0.01 for drifting gratings and static cortex. Reproduced are the unit counts (2422; V1 580, LGN 142, LP 91), the 1-back ratios in every region (V1 0.821, static 0.897), the Figure 2 tuning effects, V1 adaptation to 8-back with all four Table 1 estimates inside their intervals and a half-life of 13.96 s, the cumulative adaptation, the decay fits of Tables 1 and 2 and the static long-term adaptation. `fig3b-thalamus-short-term` passes in 1 of 12 readings, with RL at the threshold of 6, and only if significant adaptation counts ratios below 1 and the units labelled `noise` are left out; with either changed it fails. Partial are the three across-mice claims of Figures 1E, 6D and 7C, which hold by sign test while a few mice fail, in the thalamus mice with 2 to 4 units. Not reproduced are `fig5-repeat-suppression`, where orthogonal over blank is still below 1 at 2-back (0.972) under every reading and seed and in a session bootstrap, and `fig8-no-spurious-long-term`, seed sensitive, whose criterion asks every interval of the simulated neuron to contain 1, which noise alone breaks at about the chance rate (38.0% of 200 further seeds pass); both verifiers read this as the claims file's misreading, and it went to a reader in `questions/fritsche-2022.yaml`. The author's first run gave 26 reproduced, 4 partially and 1 not reproduced. Round 1 asked for the invalid intervals to be applied as a variant, the Figure 2 units dropped per tertile, a two-sided count for Figure 3B, 200 seeds for Figure 8, the thalamic units of the mice that fail and a session bootstrap for Figure 5, all added. Round 2 asked for the Figure 3B readings with `noise` units kept, which then met no reading, and found sentences the outputs did not support (seven of 12 readings, not eight; a p range starting at 4.5e-09; the ground truth inside the interval in the six named runs, not in every run; the 1-back match not holding for static thalamus, LGN 0.957 against 0.93 and LP 0.900 against 0.85), all corrected. The first full notebook run failed on a missing cell boundary that left a function in a markdown cell; the notebook ran in 492 s at first, with peak memory about 3.2 GB, and in 367 s after round 1.

The units table holds all 74658 sorted units, with a `quality` column marking 20182 as `noise` and the AllenSDK quality metric columns, none of them described in the files; the paper's counts are matched when the `noise` units are left out, as the AllenSDK's units table does, nothing in the files says they should be, and keeping them changes the thalamic results (LGN gains a significant 7-back and its tau falls to 0.000). Of the units that pass the quality metrics, 3723 sit on channels whose area is `grey` and 686 on `VIS`, labels that name no structure, and they reach the paper's 50 responsive units for a region; they are left out. Thirteen sessions list invalid intervals tagged with a probe, totalling 12 to 2931 s, several overlapping the grating epochs (375 drifting presentations in 5 sessions, 7001 static in 10); their meaning is not described, the paper does not mention them, and leaving those presentations out changes the 1-back ratios by at most 0.014. Three sessions (715093703, 719161530, 721123822) hold 598 drifting gratings in place of 600, and static blank sweeps number 189 to 197 of 6000 presentations per session, about one in 31, where the Methods say about one in 25. The checks passed: 32 mice, one session each, with the paper's genotypes, stimuli as the Methods describe, no recording or unit deposited twice, and V1 tuning locked to the stimulus tables in every session. Three questions are put to the paper's authors: whether Figure 3B's borders include ratios significantly above 1, what rate and noise model the Figure 8 simulated neuron used and which interval, and whether the `noise` units were left out.

The author's points on the protocol: it says the outcome is the one all readings give, while the claims file's criteria say reproduced under one reading, and the claims file was followed; nothing says whether a significant n-back counts ratios above 1, and adaptation only was assumed with both shown; a filter outside the listed readings, the `noise` label, was treated as an assumption with the key results run without it; it does not say whether each region's bootstrap takes its own seed, and every region took the claim's seed; `archives.md` does not say how to get the S3 URL, and as the download redirect returned 403 the asset metadata's `contentUrl` was used; and with no partial rule in the fig5 criterion the protocol's general definition was used, while the strict fig8 criterion fails on tiny chance exclusions.

**`summaries/fritsche-2022-01.md`** (114 words)

The paper's main findings held up in this data. In mouse visual cortex the response to a grating was reduced when a grating of the same orientation came up to 8 trials earlier, decaying with a half-life of about 14 s, while in the thalamus adaptation was limited to the last one or two trials, a result that rests on two reading choices. Adaptation by tuning, its accumulation over trials and the longer trace after static gratings also reproduced. The blank-baseline analysis did not: suppression after an orthogonal grating lasted to 2-back, not only 1-back. A few mice broke the across-mice consistency, and the simulation control failed a criterion that chance noise alone breaks.

## End of run

15 turns, 2 minutes, $0.94 at API prices, result: success.
