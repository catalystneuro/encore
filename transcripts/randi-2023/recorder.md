# 001075 · recorder · run 39138162524

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001075 --write; git diff; ls claims/001075 transcripts/001075; cat attempts/001075-randi-2023-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001075' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (217.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/208fc169-7b30-4ea5-8232-8df1d2c8bd35/tool-results/bclunv0la.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 6056d4d..005a559 100644
--- a/README.md
+++ b/README.md
@@ -91,6 +91,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [000947](https://dandiarchive.org/dandiset/000947) | [Schwab et al. 2020](https://doi.org/10.1371/journal.pbio.3000829) | 6 (+1) | 4 | 7 | 1 | [`000947-schwab-2020`](entries/000947-schwab-2020) |
 | [000971](https://dandiarchive.org/dandiset/000971) | [Seiler et al. 2022](https://doi.org/10.1016/j.cub.2022.01.055) | 17 | 9 | 6 | 5 | [`000971-seiler-2022`](entries/000971-seiler-2022) |
 | [001038](https://dandiarchive.org/dandiset/001038) | [Azcorra et al. 2023](https://doi.org/10.1038/s41593-023-01401-9) | 16 | 7 | 1 | 0 | [`001038-azcorra-2023`](entries/001038-azcorra-2023) |
+| [001075](https://dandiarchive.org/dandiset/001075) | [Randi et al. 2023](https://doi.org/10.1038/s41586-023-06683-4) | 4 | 4 (+1) | 0 (+1) | 7 | [`001075-randi-2023`](entries/001075-randi-2023) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001075:
10.1038-s41586-023-06683-4.yaml

transcripts/001075:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001075-randi-2023-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(it,dict): it=[dict(v,_k=k) for k,v in it.items()]
for x in it:
  if '001075' in (x.get('id','')+x.get('_k','')+str(x.get('dandiset',''))): print(json.dumps(x,indent=1)[:3000])
"
```

```
Exit code 1
schema_version: 1
id: 001075-randi-2023-01
dandiset: "001075"
dandiset_version: 0.240930.1859
paper: doi:10.1038/s41586-023-06683-4
date: 2026-10-18
entry: 001075-randi-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-7
inputs:
- what: The list of the 188 head neurons (head ganglia of aconnectome_ids_ganglia.json), used to
    define the head pairs. The paper's analysis code was also read for the response classifier and
    its parameters, the photobleaching fit, the spike removal, the decaying correction and the
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
2764:### 000718, Zaki et al. 2024
2855:### 000691, Scherrer et al. 2023
2948:### 000727, Brezovec et al. 2022
3039:### 000947, Schwab et al. 2020
3132:### 000971, Seiler et al. 2022
3233:### 001038, Azcorra et al. 2023
3326 docs/pilot-notes.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 2855
}
```

```
2855	### 000691, Scherrer et al. 2023
2856	
2857	Six claims reproduced and seven blocked on the dandiset, plus two claims on
2858	data in other archives, both partially reproduced. Round 1 gave its own
2859	outcome for each claim from the notebook with its conclusions removed and
2860	agreed with all 15 as they then stood, but suspected that the SGD solver
2861	explained why no point of the local decoding map was significant (0 of 151);
2862	the 32-footprint decoders stop at objectives of 19.8 to 68.9 where the
2863	optimum is 1.976 to 2.000, so the author fit them with liblinear, as
2864	MATLAB's default for 100 or fewer predictors is BFGS run to convergence, and
2865	`ed9c-local-decoding-map` moved from not reproduced to reproduced. Round 2
2866	agreed with all 15 and nothing was proposed, so there was no third round.
2867	The paper reports two head-mounted microscopes with axicon correction
2868	optics, one optimized for weight (1.0 g, 1.0 mm FOV) and one for field of
2869	view (1.4 g, about 4 mm), that image hundreds of neurons in juvenile
2870	songbirds and thousands in a freely behaving mouse, whose position and
2871	direction in a looped maze can be decoded from the imaged activity. The
2872	footprint count and the mouse's coverage of the maze, decoding of quadrant
2873	with direction and of octant, the local decoding map, localized activity
2874	and the spread of coactive footprints in 8 NMF components were tested on the
[... 453 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 -A2 '^| Dandiset\|^| ---\|^|---' README.md | head -20; sed -n '/Counts are of/,/^$/p' README.md
```

```
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
50:|---|---|---|---|---|---|---|
51-| [000582](https://dandiarchive.org/dandiset/000582) | [Sargolini et al. 2006](https://doi.org/10.1126/science.1125572) | 2 | 1 | 0 | 0 | [`000582-sargolini-2006`](entries/000582-sargolini-2006) |
52-| [000127](https://dandiarchive.org/dandiset/000127) | [Chowdhury et al. 2020](https://doi.org/10.7554/eLife.48198) | 4 | 2 | 0 | 4 | [`000127-chowdhury-2020`](entries/000127-chowdhury-2020) |
Counts are of claims that rest on the dandiset, including those that take
names for its own codes from elsewhere. Claims that also use data from
outside the dandiset are counted apart, in brackets. Claims on data the
paper deposited in other archives are not in this table; the dashboard
shows them on each dandiset's page.
```

**Agent calls Bash**

```bash
sed -n 60,400p attempts/001075-randi-2023-01.yaml
```

```
(expected 23,433 with tolerance 2,343), from 184 head neurons (186, tolerance 18.6), with at
    most 50 observations of a pair (59, tolerance 5.9); only the neuron count is within tolerance.
    Reading (b) gives 20,422 pairs. Reading (c), without the autoresponse requirement, gives 23,813
    pairs and 184 neurons, within tolerance, but at most 86 observations. 107 animals contribute;
    172 head neurons are stimulated with an autoresponse (the Source Data list 168). With the
    stimulated ROI from the paper's export, reading (a) gives 20,351 pairs, 183 neurons and at most
    55 observations.
  deviations:
  - The stimulated ROI is found from the target position for stimulations without a manually
    located ROI; the paper maps the nearest neuron through tracking matches that are not in the
    dandiset. The two agree for 66% of such stimulations.
  - The paper's exclusion of some stimulations (950 marked -2 in its export) and its matchless
    traces for dim neurons are not in the dandiset, so all stimulations and only the regular
    traces are used.
  - The paper's text does not say whether the 23,433 pairs include i = j; the Source Data count
    does. Three readings are shown.
- claim: fig1e-avjr-avdr
  outcome: reproduced
  notebook: reproduce_randi_2023.ipynb
  output: claim:fig1e-avjr-avdr
[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,700p attempts/001075-randi-2023-01.yaml
```

```
mismatch; the export has no labels for subject 11, the dandiset has almost none for 64, 76 and 77,
      and in 86 and 91 shared names sit on other ROIs. The finding is updated. Corrected the text the
      verifier found at odds with the outputs (B7), the depth_in_um range (-0.875 to 0.875), the imaging
      depth (2.5 to 37.5 um), the (0, 0) targets (none manual) and the share of manual targets in the
      helper's docstring (about half).
  - claim: fig2d-inhibitory-fraction
    agrees: true
    outcome: not_reproduced
    reason: Negative fraction 0.151 (a) and 0.174 (b), against 0.11 with tolerance 0.011; the decaying
      variant gives 0.0956, just outside, and the Source Data means give 0.115. Sign flips from negative or
      tiny F0 (B1) and spurious negatives from uncorrected bleaching (B2) could inflate the fraction, and
      the 950 excluded stimulations are kept (B4).
    response: Added the fraction under the same variants as sourcedata-link and with the exported
      assignment, which applies the export's exclusions (asked for in section C). None reaches the
      tolerance (13.4% to 15.8%), so neither F0 nor photobleaching explains the excess. Outcome kept.
  - claim: edfig2ij-spatial-specificity
    agrees: true
    outcome: reproduced
    reason: Fraction below 0.1 is 0.741 pooled (a) and 0.817 for 10 to 16 um (c), both within 0.675 to
      0.825, and the target median over the 4 to 10 um median is 6.2. The band values agree with the
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -E '^\s*(- )?id:|data_source|uses|outside|elsewhere|kind:' claims/001075/*.yaml | head -80; python - <<'E'
import json;d=json.load(open('targets/dandisets.json'))
def walk(o):
    if isinstance(o,dict):
        if any('001075'==str(v) for v in o.values()): print(json.dumps(o,indent=1)); return
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(d)
E
```

```
45:- id: recordings-protocol
61:- id: pairs-measured
86:- id: fig1e-avjr-avdr
93:- id: fig1f-aver-avar
97:- id: fig1g-saadl-ollr
103:- id: sourcedata-link
117:- id: osf-link
130:- id: fig2d-inhibitory-fraction
147:- id: edfig2ij-spatial-specificity
165:- id: fig2c-1310-connected
169:- id: fig2c-bilateral
173:- id: fig2efg-path-length
178:- id: fig3-anatomy-predictions
183:- id: edfig6-kernel-stereotypy
187:- id: edfig7b-unc31-fewer
191:- id: fig4-rid-wt
205:- id: fig4-rid-unc31
209:  data: elsewhere
222:- id: fig5-extrasynaptic-screen
228:- id: fig6-spontaneous
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001075/10.1038-s41586-023-06683-4.yaml"
}
```

```
1	# Claims for Randi, Sharma, Dvali & Leifer (2023) on dandiset 001075.
2	# Source: the full text in PubMed Central (PMC10632145, open access, CC BY), with its Methods,
3	# figure legends and the Source Data files of the Nature article.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list of
6	# both published versions, the metadata and contents of the files, counts of subjects,
7	# recordings, stimulations, ROIs and labels, the stimulation durations, powers and intervals,
8	# the recording lengths, the units and ranges of the traces, the per-recording fit of the
9	# target positions, and the rate at which the stimulated ROI passes the paper's response
10	# classifier at the true and at shifted stimulation times. While testing the pipeline on one
11	# recording (sub-0), the author saw three single-trial dF/F0 values of AVDR after AVJR
12	# stimulation (0.21, 0.15, -0.04). No claim's analysis over the recordings had been run. The
13	# author had read the paper's Source Data (per-pair observation counts, mean dF/F0 and q values
14	# of Extended Data Figs. 3 and 4, and the distance distributions of Extended Data Fig. 2i,j).
15	#
16	# The dandiset holds the 113 wild-type-background (WT) recordings of the paper; 110 have the
17	# segmentation file with the extracted traces. The unc-31 recordings, the spontaneous-activity
18	# recordings of Fig. 6 and the unstimulated control recordings that define the null
19	# distribution of every q value are not in it. The paper's OSF repository (doi
20	# 10.17605/OSF.IO/E2SYT) holds exported traces of the WT and unc-31 recordings and the
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001075; wc -w *-report.md; cat author-report.md
```

```
1170 author-report.md
  613 author-revise-1-report.md
  555 author-revise-2-report.md
 1489 verifier-1-report.md
 1020 verifier-2-report.md
 4847 total
I've done steps 1 to 6 for dandiset 001075 (Randi et al. 2023): the entry ran clean, `check` reports 0 errors, and the handover package is built in `executed/001075-randi-2023/handover/`. Nothing is committed. I used the paper's full text, which is open access (PMC10632145, CC BY), together with its Source Data files; all of it is saved under `paper/`. I pinned version 0.240930.1859. It is the most recent, and it is the only one with `target_pumpprobe_id`, the column that says which neuron was stimulated in a manually targeted stimulation. The notebook header shows how the two versions differ.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| recordings-protocol (113 animals, up to 40 min, stimulus every 30 s) | dandiset | partially reproduced: traces exist for only 110 of 113 animals |
| pairs-measured (23,433 pairs / 186 neurons / at most 59 observations) | dandiset | partially reproduced: 20,587 / 184 / 50 |
| fig1e AVJR→AVDR | dandiset | reproduced |
| fig1f AVER→AVAR | dandiset | reproduced, but only 7 trials |
| fig1g SAADL→OLLR | dandiset | reproduced, but only 5 trials, and the sign flips under the paper code's correction |
| edfig2ij neighbours mostly don't respond | dandiset | reproduced: 74.1% below 0.1, against 75% |
| sourcedata-link (per-pair counts and means vs the paper's Source Data) | with inputs | partially reproduced: 81.7% of pairs found, ρ = 0.77, r = 0.55 |
| fig2d 11% inhibitory | with inputs | not reproduced: 15.1% here; the paper's own per-pair means give 11.5% |
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001075; cat author-revise-1-report.md author-revise-2-report.md; sed -n 1,60p verifier-2-report.md
```

```
I've worked through every point in the verifier's round-1 report and changed three outcomes. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 721 s), and every number in the conclusions comes from that run. Nothing is committed.

**Outcome changes**
- **osf-link: reproduced → partially reproduced.** The verifier was right: the 87.4% overall agreement is inflated because all 2,812 manually located targets agree by construction. For the targets found from the target position, which is what the claim states, agreement is 66.0%, inside the partial band.
- **fig4-rid-wt: blocked → partially reproduced.** The check the verifier asked for showed the old blocking note was wrong. The dandiset labels 11 ROIs as RID, and 8 stimulations in 5 animals target one of them. Only AWB meets the criterion (mean 0.076 over 12 trials, 3 detected responses). URX is observed once and ADL never.
- **fig4-rid-unc31: blocked → reproduced, on thin evidence.** The unc-31 export on OSF does label RID: 28 stimulations in 8 of its 18 recordings. Every neuron observed in both strains has a lower mean in unc-31, so the criterion holds. But the differences are small (Mann-Whitney p = 0.31 to 0.54), the WT URX value rests on one trial, and AWB responses are still detected in 17 of 50 unc-31 trials.
- I wrote the criteria for both RID claims into the claims file before computing any RID response. Its header says which RID counts I had seen at that point.

**Added or corrected**
- **fig2d (still not reproduced):** the verifier suspected baselines (F0) at or below zero and failed photobleaching fits. They are not the cause: 3,173 rows have F0 ≤ 0 and 2,037 rows use uncorrected traces, and removing them leaves the inhibitory fraction at 15.1%. I also ran it with the export's 950 excluded stimulations removed, without the nine poorly linked recordings, without the nine recordings with negative traces, and on the export's own assignment. Every variant gives 13.4%
[... 109 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001075; grep -n -i 'stream\|did not\|could not\|fail\|error' verifier-1-report.md | head -30
```

```
20:| fig4-rid-wt | blocked: metadata_insufficient | The Methods say RID has dim tagRFP-T, no extracted trace, was targeted manually, and its downstream responses used "matchless" traces and different inclusion rules. None of that is in the files. The notebook prints no check for RID labels or RID targets, so I could not confirm this beyond the paper's description. |
37:**C. What I could not check, and the output that would settle it**
39:- Whether negative or near-zero F0, or uncorrected photobleaching, drives the fig2d excess. Needed: the fig2d fraction and the sourcedata-link Pearson recomputed without rows where F0 ≤ 0 (or without the 9 negative-valued recordings) and without photobleach-failed traces, plus a count of observations with F0 ≤ 0.
44:- I did not stream any segmentation file, so I could not test the dandiset-specific values myself.
```

**Agent**

The README row is written. Now writing the subsection.

**Agent calls Bash**

```bash
cd  && cat >> docs/pilot-notes.md <<'EOF'

### 001075, Randi et al. 2023

Four claims reproduced, four partially and seven blocked on the dandiset.
With outside data, counted apart: one partially reproduced and one not
reproduced. Two claims on data in the paper's OSF repository: one reproduced
and one blocked. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with 15 of the 19. It found that
`osf-link` passed on 87.4% agreement only because all 2,812 manually located
targets agree by construction, while targets found from the position, which
the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
claim from reproduced to partially reproduced. Round 1 also asked for a check
of RID labels, which showed the earlier blocking notes wrong: the dandiset
labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
wrote criteria before computing any RID response and moved `fig4-rid-wt` from
blocked to partially reproduced and `fig4-rid-unc31` from blocked to
reproduced. The author kept `not_runnable` for `edfig6-kernel-stereotypy` and
`fig6-spontaneous`, where round 1 would have given `other` and `data_missing`,
and round 2 accepted both, the first with a reservation as no
reimplementation of the kernel fits was tried. Round 2 agreed with all 19 and
nothing was proposed, so there was no third round. The paper builds a signal
propagation atlas of the C. elegans head by stimulating single neurons in 113
WT-background animals during whole-brain calcium imaging, and compares the
measured functional connections with the connectome, with a
connectome-constrained model and with unc-31 mutants deficient in
extrasynaptic signalling. The recording protocol, the pair counts, the three
example responses of Fig. 1, spatial specificity, the link to the paper's
Source Data and OSF export, the inhibitory fraction and the RID responses were
tested. Every claim that needs q values is blocked as `data_missing`, as they
rest on unstimulated control recordings that are public nowhere, and so is the
model comparison, whose predictions are not public. Some outcomes rest on weak
ground: `fig1f-aver-avar` rests on 7 trials (Wilcoxon p = 0.22);
`fig1g-saadl-ollr` on 5 trials (p = 0.44), and the code's decaying correction
flips its sign to +0.014; and `fig4-rid-unc31` is met barely, with URX 0.031
in unc-31 against 0.032 from a single WT trial and Mann-Whitney p of 0.31 or
higher. The author used the open access full text (PMC10632145) with its
Source Data, and took the head neurons, the response classifier and other
parameters from the paper's code.

The dandiset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
The unc-31 recordings, the spontaneous recordings of Fig. 6 and the
unstimulated control recordings are not in the dandiset, and the controls,
which every q value in the paper needs, are not on OSF either, so the paper's
central statistics cannot be recomputed. For about half of the stimulations
the files give only a target position, not the stimulated ROI; the paper's
assignment uses tracking matches that are not in the dandiset, and from the
position 66% of these stimulations get the paper's ROI. The paper's export
marks 950 stimulations as excluded, which the dandiset does not mark. Three of
the 113 subjects (20, 23, 33) have only the raw imaging file, without traces
or stimulation table. In five recordings the labels reached through
`neuropal_ids` and the NeuroPAL table differ from the export for every named
ROI: subjects 64, 76 and 77 have almost no labels (4, 0 and 15 distinct names
against 70, 102 and 87 exported), and in 86 and 91 most names are shared but
sit on other ROIs; in subject 11 the ROI count (161) differs from the export
(200). The traces have unit "n.a." with no description of their processing,
and nine recordings hold values down to -196,646; 3,173 of 433,216 observation
rows have F0 at or below zero, and 897 of 14,039 traces cannot be corrected
for photobleaching with the paper's fit, though the variants without them
change no outcome. Even so, the inhibitory fraction of `fig2d` is 15.1% from
the dandiset against the 11.5% the Source Data means give for the same pairs,
and every variant gives 13.4% to 15.8%. Other findings: `neuropal_ids` holds
"merge" in 63 recordings and "check", "I4" or "RIAR" in others, and 49 ROIs in
21 recordings carry the label "target"; `depth_in_um` runs from -0.875 to
0.875, which cannot be micrometres in a volume imaged from 2.5 to 37.5 um, and
122 stimulations have the target position (0, 0); every stimulation is stored
as 0.5 s at 1.2 mW, constants written by the conversion, so the 0.1 to 0.5 s
AFD pulses of the Methods are not represented; the red channel is described
with the indicator GCaMP6s though it images tagRFP-T, two subjects have strain
"none", every age is P1D and one label confidence is 11; and thirteen
recordings last longer than the paper's "up to 40 min" (up to 48.7 min) and
three have timestamp gaps of up to 8.4 s.

The notebook ran in 404 s in the first clean run, 721 s after round 1 and
634 s after round 2. The paper's pumpprobe package would not install, and a
cell added after round 2 shows that it builds once the numpy headers are added
by hand but cannot be imported, as mistofrutta, wormbrain and wormdatamodel do
not build; OSF returned HTTP 429 for files fetched one at a time, so the
notebook streams a single tarball checked by its md5. Round 2 found statements
the outputs did not support, among them that every variant of
`sourcedata-link` falls in the partial band, which fails for the
detected-responses-only variant, and a deviation of `edfig2ij` that missed
reading (c); these were corrected, while counts differing by one between the
verifier's copy and the re-run were kept, with the Summary stating the
difference. The author's points on the protocol: no rule for the paper's own
published results such as Source Data q values and means; claims that need
data on OSF and data public nowhere, which the rule that elsewhere is never
`data_missing` does not fit; no guidance for an identifier that is absent but
can be inferred from the dandiset; whether a list of head neurons from the
paper's code is an input; a legend percentage that does not say which
neighbours it refers to; a default 10% tolerance meaningless for a count of
113 animals; block reasons resting on checks run outside the notebook; two
published versions with the same files, all re-uploaded; a clock check by
stimulated-neuron response rate in place of decoding; and no rule for outside
services that rate-limit.
EOF
grep -c '—' docs/pilot-notes.md; tail -c 300 docs/pilot-notes.md; grep -n -i 'rather' docs/pilot-notes.md | tail -2
```

```
0
fault 10% tolerance meaningless for a count of
113 animals; block reasons resting on checks run outside the notebook; two
published versions with the same files, all re-uploaded; a clock check by
stimulated-neuron response rate in place of decoding; and no rule for outside
services that rate-limit.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes.md",
 "old_string": "connectome-constrained model and with unc-31 mutants deficient in\nextrasynaptic signalling. The",
 "new_string": "connectome-constrained model and with unc-31 mutants, screening for\nextrasynaptic-dependent propagation. The"
}
```

```
The file docs/pilot-notes.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent**

I added the 001075 row to README.md (`4 | 4 (+1) | 0 (+1) | 7`) and appended this subsection to the end of docs/pilot-notes.md. Nothing is committed.

### 001075, Randi et al. 2023

Four claims reproduced, four partially and seven blocked on the dandiset.
With outside data, counted apart: one partially reproduced and one not
reproduced. Two claims on data in the paper's OSF repository: one reproduced
and one blocked. Round 1 gave its own outcome for each claim from the notebook
with its conclusions removed and agreed with 15 of the 19. It found that
`osf-link` passed on 87.4% agreement only because all 2,812 manually located
targets agree by construction, while targets found from the position, which
the claim states, agree in 1,101 of 1,667 (66.0%), and the author changed the
claim from reproduced to partially reproduced. Round 1 also asked for a check
of RID labels, which showed the earlier blocking notes wrong: the dandiset
labels 11 ROIs RID and 8 stimulations in 5 animals target one, and the unc-31
export labels RID in 28 stimulations in 8 of its 18 recordings, so the author
wrote criteria before computing any RID response and moved `fig4-rid-wt` from
blocked to partially reproduced and `fig4-rid-unc31` from blocked to
reproduced. The author kept `not_runnable` for `edfig6-kernel-stereotypy` and
`fig6-spontaneous`, where round 1 would have given `other` and `data_missing`,
and round 2 accepted both, the first with a reservation as no
reimplementation of the kernel fits was tried. Round 2 agreed with all 19 and
nothing was proposed, so there was no third round. The paper builds a signal
propagation atlas of the C. elegans head by stimulating single neurons in 113
WT-background animals during whole-brain calcium imaging, and compares the
measured functional connections with the connectome, with a
connectome-constrained model and with unc-31 mutants, screening for
extrasynaptic-dependent propagation. The recording protocol, the pair counts, the three
example responses of Fig. 1, spatial specificity, the link to the paper's
Source Data and OSF export, the inhibitory fraction and the RID responses were
tested. Every claim that needs q values is blocked as `data_missing`, as they
rest on unstimulated control recordings that are public nowhere, and so is the
model comparison, whose predictions are not public. Some outcomes rest on weak
ground: `fig1f-aver-avar` rests on 7 trials (Wilcoxon p = 0.22);
`fig1g-saadl-ollr` on 5 trials (p = 0.44), and the code's decaying correction
flips its sign to +0.014; and `fig4-rid-unc31` is met barely, with URX 0.031
in unc-31 against 0.032 from a single WT trial and Mann-Whitney p of 0.31 or
higher. The author used the open access full text (PMC10632145) with its
Source Data, and took the head neurons, the response classifier and other
parameters from the paper's code.

The dandiset was converted by CatalystNeuro (catalystneuro/leifer_lab_to_nwb).
The unc-31 recordings, the spontaneous recordings of Fig. 6 and the
unstimulated control recordings are not in the dandiset, and the controls,
which every q value in the paper needs, are not on OSF either, so the paper's
central statistics cannot be recomputed. For about half of the stimulations
the files give only a target position, not the stimulated ROI; the paper's
assignment uses tracking matches that are not in the dandiset, and from the
position 66% of these stimulations get the paper's ROI. The paper's export
marks 950 stimulations as excluded, which the dandiset does not mark. Three of
the 113 subjects (20, 23, 33) have only the raw imaging file, without traces
or stimulation table. In five recordings the labels reached through
`neuropal_ids` and the NeuroPAL table differ from the export for every named
ROI: subjects 64, 76 and 77 have almost no labels (4, 0 and 15 distinct names
against 70, 102 and 87 exported), and in 86 and 91 most names are shared but
sit on other ROIs; in subject 11 the ROI count (161) differs from the export
(200). The traces have unit "n.a." with no description of their processing,
and nine recordings hold values down to -196,646; 3,173 of 433,216 observation
rows have F0 at or below zero, and 897 of 14,039 traces cannot be corrected
for photobleaching with the paper's fit, though the variants without them
change no outcome. Even so, the inhibitory fraction of `fig2d` is 15.1% from
the dandiset against the 11.5% the Source Data means give for the same pairs,
and every variant gives 13.4% to 15.8%. Other findings: `neuropal_ids` holds
"merge" in 63 recordings and "check", "I4" or "RIAR" in others, and 49 ROIs in
21 recordings carry the label "target"; `depth_in_um` runs from -0.875 to
0.875, which cannot be micrometres in a volume imaged from 2.5 to 37.5 um, and
122 stimulations have the target position (0, 0); every stimulation is stored
as 0.5 s at 1.2 mW, constants written by the conversion, so the 0.1 to 0.5 s
AFD pulses of the Methods are not represented; the red channel is described
with the indicator GCaMP6s though it images tagRFP-T, two subjects have strain
"none", every age is P1D and one label confidence is 11; and thirteen
recordings last longer than the paper's "up to 40 min" (up to 48.7 min) and
three have timestamp gaps of up to 8.4 s.

The notebook ran in 404 s in the first clean run, 721 s after round 1 and
634 s after round 2. The paper's pumpprobe package would not install, and a
cell added after round 2 shows that it builds once the numpy headers are added
by hand but cannot be imported, as mistofrutta, wormbrain and wormdatamodel do
not build; OSF returned HTTP 429 for files fetched one at a time, so the
notebook streams a single tarball checked by its md5. Round 2 found statements
the outputs did not support, among them that every variant of
`sourcedata-link` falls in the partial band, which fails for the
detected-responses-only variant, and a deviation of `edfig2ij` that missed
reading (c); these were corrected, while counts differing by one between the
verifier's copy and the re-run were kept, with the Summary stating the
difference. The author's points on the protocol: no rule for the paper's own
published results such as Source Data q values and means; claims that need
data on OSF and data public nowhere, which the rule that elsewhere is never
`data_missing` does not fit; no guidance for an identifier that is absent but
can be inferred from the dandiset; whether a list of head neurons from the
paper's code is an input; a legend percentage that does not say which
neighbours it refers to; a default 10% tolerance meaningless for a count of
113 animals; block reasons resting on checks run outside the notebook; two
published versions with the same files, all re-uploaded; a clock check by
stimulated-neuron response rate in place of decoding; and no rule for outside
services that rate-limit.

## End of run

15 turns, 1 minutes, result: success.
