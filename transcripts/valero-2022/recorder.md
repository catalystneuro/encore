# 000568 · recorder · run 39076574068

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 000568 --write; git diff; ls claims/000568 transcripts/000568; grep -n '^### ' docs/pilot-notes.md | tail -6
```

```
diff --git a/README.md b/README.md
index 193fdb7..62d71fc 100644
--- a/README.md
+++ b/README.md
@@ -83,6 +83,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000350](https://dandiarchive.org/dandiset/000350) | [Mu et al. 2019](https://doi.org/10.1016/j.cell.2019.05.050) | 2 | 3 | 4 | 10 | [`000350-mu-2019`](entries/000350-mu-2019) |
 | [000409](https://dandiarchive.org/dandiset/000409) | [Ibl et al. 2025](https://doi.org/10.1038/s41586-025-09235-0) | 17 | 3 | 3 | 7 | [`000409-ibl-2025`](entries/000409-ibl-2025) |
 | [000552](https://dandiarchive.org/dandiset/000552) | [Huszar et al. 2022](https://doi.org/10.1038/s41593-022-01138-x) | 5 | 4 | 3 | 23 | [`000552-huszar-2022`](entries/000552-huszar-2022) |
+| [000568](https://dandiarchive.org/dandiset/000568) | [Valero et al. 2022](https://doi.org/10.1126/science.abm1891) | 4 | 6 | 6 | 6 | [`000568-valero-2022`](entries/000568-valero-2022) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/000568:
10.1126-science.abm1891.yaml

transcripts/000568:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,82p README.md; sed -n '2142,$p' docs/pilot-notes.md
```

```
<persisted-output>
Output too large (34.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1e4e31c1-3352-4307-adfb-3a3b74fdea60/tool-results/belzu8yhn.txt

Preview (first 2KB):
| [001754](https://dandiarchive.org/dandiset/001754) | [Knierim et al. 2000](https://doi.org/10.1038/72910) | 3 | 0 | 1 | 3 | [`001754-knierim-2000`](entries/001754-knierim-2000) |
| [000130](https://dandiarchive.org/dandiset/000130) | [Sohn et al. 2019](https://doi.org/10.1016/j.neuron.2019.06.012) | 9 | 4 | 7 | 3 | [`000130-sohn-2019`](entries/000130-sohn-2019) |
| [001616](https://dandiarchive.org/dandiset/001616) | [Gerken et al. 2025](https://doi.org/10.7554/elife.106758.1) | 6 | 5 | 0 | 9 | [`001616-gerken-2025`](entries/001616-gerken-2025) |
| [002014](https://dandiarchive.org/dandiset/002014) | [Choi et al. 2025](https://doi.org/10.1016/j.jneumeth.2025.110467) | 4 | 1 | 0 | 8 | [`002014-choi-2025`](entries/002014-choi-2025) |
| [001933](https://dandiarchive.org/dandiset/001933) | [Chen et al. 2026](https://doi.org/10.1038/s41467-026-75194-3) | 6 | 2 | 1 (+1) | 0 | [`001933-chen-2026`](entries/001933-chen-2026) |
| [000004](https://dandiarchive.org/dandiset/000004) | [Chandravadia et al. 2020](https://doi.org/10.1038/s41597-020-0415-9) | 10 | 8 (+2) | 4 | 1 | [`000004-chandravadia-2020`](entries/000004-chandravadia-2020) |
| [002013](https://dandiarchive.org/dandiset/002013) | [Amjad et al. 2025](https://doi.org/10.1021/acschemneuro.5c00071) | 7 (+1) | 1 | 0 | 5 | [`002013-amjad-2025`](entries/002013-amjad-2025) |
| [001636](https://dandiarchive.org/dandiset/001636) | [Pasquereau et al. 2013](https://doi.org/10.3389/fnsys.2013.00098) | 4 | 3 | 3 | 18 | [`001636-pasquereau-2013`](entries/001636-pasquereau-2013) |
| [000041](https://dandiarchive.org/dandiset/000041) | [Watson et al. 2016](https://doi.org/10.1016/j.neuron.2016.03.036) | 8 | 9 | 15 | 7 | [`000041-watson-2016`](entries/000041-watson-2016) |
| [000003](http
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A12 '^| Dandiset' README.md | head -30; sed -n '2394,$p' docs/pilot-notes.md
```

```
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50-|---|---|---|---|---|---|---|
51-| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
52-| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
53-| [000207](https://dandiarchive.org/dandiset/000207) | [Zheng et al. 2022](https://doi.org/10.1038/s41593-022-01020-w) | 5 | 1 | 0 | 14 | [`000207-zheng-2022`](entries/000207-zheng-2022) |
54-| [000147](https://dandiarchive.org/dandiset/000147) | [Guan et al. 2022](https://doi.org/10.7554/eLife.74478) | 9 (+3) | 0 | 1 | 4 (+3) | [`000147-guan-2022`](entries/000147-guan-2022) |
55-| [001097](https://dandiarchive.org/dandiset/001097) | [Liu et al. 2024](https://doi.org/10.1038/s41586-024-07916-w) | 7 | 2 | 3 | 12 | [`001097-liu-2024`](entries/001097-liu-2024) |
56-| [000625](https://dandiarchive.org/dandiset/000625) | [Geiller et al. 2020](https://doi.org/10.1016/j.neuron.2020.09.013) | 4 | 4 | 6 | 12 | [`000625-geiller-2020`](entries/000625-geiller-2020) |
57-| [000035](https://dandiarchive.org/dandiset/000035) | [Scala et al. 2021](https://doi.org/10.1038/s41586-020-2907-3) | 3 (+2) | 1 (+1) | 0 | 9 (+1) | [`000035-scala-2021`](entries/000035-scala-2021) |
58-| [001453](https://dandiarchive.org/dandiset/001453) | [Fouke et al. 2025](https://doi.org/10.1016/j.cub.2025.04.027) | 7 | 1 | 2 | 10 | [`001453-fouke-2025`](entries/001453-fouke-2025) |
59-| [000006](https://dandiarchive.org/dandiset/000006) | [Economo et al. 2018](https://doi.org/10.1038/s41586-018-0642-9) | 3 | 1 | 1 | 4 | [`000006-economo-2018`](entries/000006-economo-2018) |
60-| [001754](https://dandiarchive.org/dandiset/001754) | [Knierim et al. 2000](https://doi.org/
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/000568-valero-2022-01.yaml; cat claims/000568/*.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '000568' in json.dumps(e)[:300]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (61.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1e4e31c1-3352-4307-adfb-3a3b74fdea60/tool-results/b7wakyj0w.txt

Preview (first 2KB):
schema_version: 1
id: 000568-valero-2022-01
dandiset: "000568"
dandiset_version: 0.230705.1633
paper: doi:10.1126/science.abm1891
date: 2026-10-17
entry: 000568-valero-2022
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
outcomes:
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1e4e31c1-3352-4307-adfb-3a3b74fdea60/tool-results/b7wakyj0w.txt"
}
```

```
1	schema_version: 1
2	id: 000568-valero-2022-01
3	dandiset: "000568"
4	dandiset_version: 0.230705.1633
5	paper: doi:10.1126/science.abm1891
6	date: 2026-10-17
7	entry: 000568-valero-2022
8	provenance:
9	  kind: agent
10	  accountable:
11	    name: CatalystNeuro
12	  agent:
13	    harness: Claude Code (GitHub Actions)
14	    model: claude-opus-5-5
15	    protocol: pilot-7
16	outcomes:
17	- claim: cohort-counts
18	  outcome: partially_reproduced
19	  notebook: reproduce_valero_2022.ipynb
20	  output: claim:cohort-counts
[... 992 more lines not kept]
```

**Agent**

The README row is in place (4 reproduced, 6 partially, 6 not reproduced, 6 blocked). Next I'm reading the target entry and the reports.

**Agent calls Bash**

```bash
grep -n -B2 -A15 '"000568"' targets/dandisets.json | head -40; wc -l transcripts/000568/*-report.md
```

```
2503-  },
2504-  {
2505:   "dandiset": "000568",
2506-   "name": "Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics",
2507-   "published_version": "0.230705.1633",
2508-   "asset_count": 138,
2509-   "size_gb": 904.76,
2510-   "data_standards": [
2511-    "Neurodata Without Borders (NWB)"
2512-   ],
2513-   "species": [
2514-    "Mus musculus - House mouse"
2515-   ],
2516-   "approaches": [
2517-    "behavioral approach",
2518-    "electrophysiological approach",
2519-    "optogenetic approach"
2520-   ],
   63 transcripts/000568/author-report.md
   39 transcripts/000568/author-revise-1-report.md
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/000568/author-report.md"
}
```

```
1	I did steps 1 to 5 of the protocol and built the handover (step 6) for dandiset 000568. `entry.py check` reports 0 errors, and `entry.py all` passed: the notebook ran from a clean environment in 272 s. Nothing was committed.
2	
3	I used the full text of the NIH author manuscript in PMC (PMC9632609): the main report and its figure legends. The supplement, which holds the Materials and Methods and figures S1 to S15, could not be obtained: PMC serves it behind a captcha and the publisher's copy is not open access. I pinned version 0.230705.1633, the only published version; the paper cites no DANDI version, and the draft holds the same 138 assets.
4	
5	**(1) Outcomes per claim**
6	
7	| Claim | Outcome |
8	|---|---|
9	| cohort-counts | partially reproduced (4 mice and 48.2 cells per session match; 1351 putative pyramidal cells against 822) |
10	| fig1c-pulse-protocol | partially reproduced (20 ms pulses and 0.28 to 0.38 s per-uLED intervals match; median offset between pulses is 60 and 80 ms, not 20 to 40) |
11	| fig1e-responsive-fraction | reproduced, under reading (b) only (72.5%) |
12	| fig1i-swr-decrease | reproduced (p = 6.8e-09) |
13	| figs10-swr-gain-vs-baseline-rate | partially reproduced (rho = -0.437, stronger than -0.19) |
14	| fig2b-theta-trough-gain | not reproduced |
15	| figs11-place-cell-fraction | not reproduced (chi-squared p = 0.018, where the paper reports no difference) |
16	| fig2e-infield-gain | reproduced |
17	| figs12-gain-rate-correlations | not reproduced |
18	| fig3a-place-cells-more-excitable | reproduced |
19	| fig3c-unmasked-fields | not reproduced |
20	| fig3e-ghost-fields | partially reproduced |
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 2520,2540p targets/dandisets.json; cd transcripts/000568; cat author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md verifier-1-report.md verifier-2-report.md verifier-3-report.md
```

```
<persisted-output>
Output too large (31KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1e4e31c1-3352-4307-adfb-3a3b74fdea60/tool-results/bsf1llwdw.txt

Preview (first 2KB):
   ],
   "papers": [
    {
     "doi": "10.1126/science.abm1891",
     "title": " Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb/tree/main/buzsaki_lab_to_nwb/valero",
    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb/blob/main/buzsaki_lab_to_nwb/valero/widget_demostration.ipynb",
    "contributor Mayorquin, Heberto of CatalystNeuro"
   ]
  },
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/1e4e31c1-3352-4307-adfb-3a3b74fdea60/tool-results/bsf1llwdw.txt"
}
```

```
1	   ],
2	   "papers": [
3	    {
4	     "doi": "10.1126/science.abm1891",
5	     "title": " Probing subthreshold dynamics of hippocampal neurons by pulsed optogenetics",
6	     "relation": "IsDescribedBy",
7	     "resource_type": "JournalArticle",
8	     "preprint": false
9	    }
10	   ],
11	   "catalystneuro": [
12	    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb/tree/main/buzsaki_lab_to_nwb/valero",
13	    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb/blob/main/buzsaki_lab_to_nwb/valero/widget_demostration.ipynb",
14	    "contributor Mayorquin, Heberto of CatalystNeuro"
15	   ]
16	  },
17	  {
18	   "dandiset": "000574",
19	   "name": "Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task",
20	   "published_version": "0.250815.1108",
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && tail -c 200 docs/pilot-notes.md | od -c | tail -3 && cat >> docs/pilot-notes.md <<'EOF'

### 000568, Valero et al. 2022

Four claims reproduced, six partially, six not reproduced and six blocked, all
on the dandiset. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with all 22 as they then stood, but
found that most light pulses are not in the files and that the place-field
rule differed from buzcode's; the revision restricted control time to windows
dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
11 cells between place and non-place and changed five outcomes:
`figs11-place-cell-fraction` to partially reproduced,
`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
reproduced, and `fig3g-spatial-information` and
`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
22 and disagreed on `fig3g-spatial-information`, whose larger increase for
unmasked fields (p = 0.039) does not hold against time-matched control maps,
where the increase is negative in both groups (p = 0.3); the author proposed
partially reproduced and a third round agreed. The paper reports pulsed
optogenetics with uLEDs in CA1 pyramidal neurons of four CaMKIIa-Cre::Ai32
mice: light-induced spiking falls during sharp-wave ripples, rises in the
place field and at the theta trough, unmasks place fields in non-place cells,
and with these fields ripple cofiring tracks spatial overlap for pairs that
include non-place cells. The cohort, the pulse protocol, the responsive
fraction, ripple gain, theta phase, place-cell fractions, in-field gain,
unmasked and ghost fields, stability, spatial information and ripple cofiring
were tested, all claims that need light pulses or place fields on two sessions
of one mouse (91 putative pyramidal cells, against the paper's 822). The light
intensity and intracellular claims are blocked as `data_missing`, the
excitatory against inhibitory comparison as `metadata_insufficient`, and the
position decoding, assemblies and replay as `methods_underspecified`, since
the Materials and Methods are in a supplement that could not be obtained.
Some outcomes rest on weak ground: `fig1e-responsive-fraction` is reproduced
only under reading (b), all stimulation epochs (72.5%), as the PreStim epoch
gives 62.6%; `fig4c-swr-cofiring-place-pairs` passes at p = 0.032, in sess9
only, with the same coefficient for place and non-place pairs (0.062) as for
place cell pairs (0.060); `fig3a-place-cells-more-excitable` changed outcome
with the new place-cell calls alone; and reading (a) of
`fig3c-unmasked-fields` rests on 9 cells, 7 of which have a light field
(77.8%, 95% interval 40.0 to 97.2%, including the paper's 69.3%). The author
used the NIH author manuscript in PubMed Central (PMC9632609), took method
details from buzcode and the first author's later lab code (HippoCookBook
getuLEDResponse.m), and used pyramidal cells as units with a baseline rate
below 5 Hz.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
Light pulse times are deposited for 2 of 28 sessions (fCamk1 sess9 and
sess12), and only these have laps; twenty other sessions name uLED stimulation
in their epochs but hold no pulse series. In those two sessions the files hold
pulse series for 6 of the probe's 12 uLEDs (Site3 to Site8), two of them with
only 120 to 221 pulses, and in PreStim the deposited pulses come at 5.76 and
7.50 per s, where the stated protocol implies about 17 to 25; in sess9 the
offsets between deposited pulses fall only near multiples of 20 ms, no
putative pyramidal cell on shank Group3 responds to any deposited uLED, and
time without a deposited pulse therefore cannot be taken as dark. The
OptogeneticSeries are stated in watts but hold one value per uLED, 19 in sess9
and 62623 to 63599 in sess12, so the paper's three intensities cannot be
recovered. Units carry no cell type and the no-raw-data files no waveforms.
The dandiset holds 28 sessions and 1351 units with a baseline rate below 5 Hz,
where the paper reports 822 pyramidal neurons at 43.3 per session (about 19
sessions), without saying which sessions the paper used, and 14 sessions
include CNO or DMSO epochs that the paper does not describe. Other findings:
every session is deposited twice, as a full file and a no-raw-data file with
the same units, spike times, ripples and position, and the full file of
fCamk3 sess20 is named without its session; the full file of fCamk3 sess17
holds 378 s of raw signal and 6850 s of LFP of a 34621 s session, and the six
full files of fCamk1 sess13 to sess19 hold no raw signal; session_start_time
is 2016-03-15 in every file, while the session ids date the recordings to 2020
and 2021; the linearized position holds 0 to 110 cm with a conversion factor
of 100; six sessions name their epochs only by a time stamp; in fCamk3 sess13,
fCamk3 sess17 and fCamk5 sess10 the deposited ripple intervals mark population
bursts weakly (1.2 to 1.98 times the rate 1 s later); the units table of some
files lacks the shank column; the paper gives 20 to 40 ms offsets between
pulses and the files' description 40 to 60 ms; and the paper's 822 pyramidal
neurons with 73% and 71% place cells leave about 230 non-place cells, against
its 289 of 417.

The notebook ran in 272 s in the first clean run and in 289 s after round 3.
The author's own choice of control maps as all time without light, made
before noticing that the paper's control epochs are 20 ms intervals between
pulses, was kept with time-matched windows as a variant, and that variant
decided `fig3g-spatial-information`. After round 1 the paper could not be
downloaded again (PMC returned 429 and 503 errors and Europe PMC a 500), the
round-2 verifier could not run the new field rule as numpy was not installed,
and untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: no rule for when the
paper's Methods cannot be obtained; reading the code the paper links to does
not fit a general toolbox without scripts for the paper; no guidance for data
a claim needs that exist for only a few sessions; the duplicate check does not
cover every session deposited twice as a full and a no-raw-data file; a 10%
tolerance narrower than sampling error for correlations; no category for a
named data location without a pinned identifier; and no rule for what to
record as measured when only a later reading of the criterion matches.
EOF
git diff --stat
```

```
0000260   t   o   c   o   l       d   o   e   s       n   o   t       a
0000300   d   d   r   e   s   s   .  \n
0000310
 README.md           |  1 +
 docs/pilot-notes.md | 92 +++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 93 insertions(+)
```

**Agent**

I added the README row and appended the subsection below to the end of `docs/pilot-notes.md`. The row gives 4 reproduced, 6 partially, 6 not reproduced and 6 blocked. Nothing is committed, and the attempt, claims and entry are unchanged.

### 000568, Valero et al. 2022

Four claims reproduced, six partially, six not reproduced and six blocked, all
on the dandiset. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with all 22 as they then stood, but
found that most light pulses are not in the files and that the place-field
rule differed from buzcode's; the revision restricted control time to windows
dark under the stated protocol and ported `bz_findPlaceFields1D`, which moved
11 cells between place and non-place and changed five outcomes:
`figs11-place-cell-fraction` to partially reproduced,
`fig3a-place-cells-more-excitable` and `fig4d-light-unmasked-cofiring` to not
reproduced, and `fig3g-spatial-information` and
`fig4c-swr-cofiring-place-pairs` to reproduced. Round 2 agreed with 21 of the
22 and disagreed on `fig3g-spatial-information`, whose larger increase for
unmasked fields (p = 0.039) does not hold against time-matched control maps,
where the increase is negative in both groups (p = 0.3); the author proposed
partially reproduced and a third round agreed. The paper reports pulsed
optogenetics with uLEDs in CA1 pyramidal neurons of four CaMKIIa-Cre::Ai32
mice: light-induced spiking falls during sharp-wave ripples, rises in the
place field and at the theta trough, unmasks place fields in non-place cells,
and with these fields ripple cofiring tracks spatial overlap for pairs that
include non-place cells. The cohort, the pulse protocol, the responsive
fraction, ripple gain, theta phase, place-cell fractions, in-field gain,
unmasked and ghost fields, stability, spatial information and ripple cofiring
were tested, all claims that need light pulses or place fields on two sessions
of one mouse (91 putative pyramidal cells, against the paper's 822). The light
intensity and intracellular claims are blocked as `data_missing`, the
excitatory against inhibitory comparison as `metadata_insufficient`, and the
position decoding, assemblies and replay as `methods_underspecified`, since
the Materials and Methods are in a supplement that could not be obtained.
Some outcomes rest on weak ground: `fig1e-responsive-fraction` is reproduced
only under reading (b), all stimulation epochs (72.5%), as the PreStim epoch
gives 62.6%; `fig4c-swr-cofiring-place-pairs` passes at p = 0.032, in sess9
only, with the same coefficient for place and non-place pairs (0.062) as for
place cell pairs (0.060); `fig3a-place-cells-more-excitable` changed outcome
with the new place-cell calls alone; and reading (a) of
`fig3c-unmasked-fields` rests on 9 cells, 7 of which have a light field
(77.8%, 95% interval 40.0 to 97.2%, including the paper's 69.3%). The author
used the NIH author manuscript in PubMed Central (PMC9632609), took method
details from buzcode and the first author's later lab code (HippoCookBook
getuLEDResponse.m), and used pyramidal cells as units with a baseline rate
below 5 Hz.

The dandiset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).
Light pulse times are deposited for 2 of 28 sessions (fCamk1 sess9 and
sess12), and only these have laps; twenty other sessions name uLED stimulation
in their epochs but hold no pulse series. In those two sessions the files hold
pulse series for 6 of the probe's 12 uLEDs (Site3 to Site8), two of them with
only 120 to 221 pulses, and in PreStim the deposited pulses come at 5.76 and
7.50 per s, where the stated protocol implies about 17 to 25; in sess9 the
offsets between deposited pulses fall only near multiples of 20 ms, no
putative pyramidal cell on shank Group3 responds to any deposited uLED, and
time without a deposited pulse therefore cannot be taken as dark. The
OptogeneticSeries are stated in watts but hold one value per uLED, 19 in sess9
and 62623 to 63599 in sess12, so the paper's three intensities cannot be
recovered. Units carry no cell type and the no-raw-data files no waveforms.
The dandiset holds 28 sessions and 1351 units with a baseline rate below 5 Hz,
where the paper reports 822 pyramidal neurons at 43.3 per session (about 19
sessions), without saying which sessions the paper used, and 14 sessions
include CNO or DMSO epochs that the paper does not describe. Other findings:
every session is deposited twice, as a full file and a no-raw-data file with
the same units, spike times, ripples and position, and the full file of
fCamk3 sess20 is named without its session; the full file of fCamk3 sess17
holds 378 s of raw signal and 6850 s of LFP of a 34621 s session, and the six
full files of fCamk1 sess13 to sess19 hold no raw signal; session_start_time
is 2016-03-15 in every file, while the session ids date the recordings to 2020
and 2021; the linearized position holds 0 to 110 cm with a conversion factor
of 100; six sessions name their epochs only by a time stamp; in fCamk3 sess13,
fCamk3 sess17 and fCamk5 sess10 the deposited ripple intervals mark population
bursts weakly (1.2 to 1.98 times the rate 1 s later); the units table of some
files lacks the shank column; the paper gives 20 to 40 ms offsets between
pulses and the files' description 40 to 60 ms; and the paper's 822 pyramidal
neurons with 73% and 71% place cells leave about 230 non-place cells, against
its 289 of 417.

The notebook ran in 272 s in the first clean run and in 289 s after round 3.
The author's own choice of control maps as all time without light, made
before noticing that the paper's control epochs are 20 ms intervals between
pulses, was kept with time-matched windows as a variant, and that variant
decided `fig3g-spatial-information`. After round 1 the paper could not be
downloaded again (PMC returned 429 and 503 errors and Europe PMC a 500), the
round-2 verifier could not run the new field rule as numpy was not installed,
and untracked files in the repository root that the author did not create
were left alone. The author's points on the protocol: no rule for when the
paper's Methods cannot be obtained; reading the code the paper links to does
not fit a general toolbox without scripts for the paper; no guidance for data
a claim needs that exist for only a few sessions; the duplicate check does not
cover every session deposited twice as a full and a no-raw-data file; a 10%
tolerance narrower than sampling error for correlations; no category for a
named data location without a pinned identifier; and no rule for what to
record as measured when only a later reading of the criterion matches.

## End of run

11 turns, 1 minutes, result: success.
