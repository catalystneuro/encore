# crcns-ret-1 · recorder · run 39509760116

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py crcns-ret-1 --write; git diff; ls claims/crcns-ret-1/ transcripts/crcns-ret-1/; cat attempts/crcns-ret-1-lefebvre-2008-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (47.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2c466590-9180-4c7e-91b3-0635c1847369/tool-results/bn8oyhqwi.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index 6830605e..f246b9e5 100644
--- a/README.md
+++ b/README.md
@@ -104,6 +104,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001712](https://dandiarchive.org/dandiset/001712) | [Davatolhagh et al. 2025](https://doi.org/10.1101/2025.09.12.675910) | 3 | 2 | 2 | 11 | [`001712-davatolhagh-2025`](entries/001712-davatolhagh-2025) |
 | [001888](https://dandiarchive.org/dandiset/001888) | [Hristova et al. 2025](https://doi.org/10.1111/epi.18606) | 13 | 9 | 2 | 10 | [`001888-hristova-2025`](entries/001888-hristova-2025) |
 | [000005](https://dandiarchive.org/dandiset/000005) | [Yu et al. 2016](https://doi.org/10.1038/nn.4412) | – | – | – | – | [`000005-yu-2016`](entries/000005-yu-2016) (deprecated) |
+| [CRCNS:ret-1](https://crcns.org/data-sets/retina/ret-1) | [Lefebvre et al. 2008](https://doi.org/10.1242/dev.027912) | 3 | 0 | 2 | 21 | [`crcns-ret-1-lefebvre-2008`](entries/crcns-ret-1-lefebvre-2008) |
 
 Counts are of the paper's findings that rest on the dandiset, including
 those that take names for its own codes from elsewhere. Findings that also
claims/crcns-ret-1/:
10.1242-dev.027912.yaml

transcripts/crcns-ret-1/:
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B3 '^| Dataset\|^| Dandiset' README.md | head; cat attempts/crcns-ret-1-lefebvre-2008-01.yaml; grep -n '^### ' docs/pilot-notes.md | tail -6; wc -l docs/pilot-notes.md
```

```
<persisted-output>
Output too large (46KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/2c466590-9180-4c7e-91b3-0635c1847369/tool-results/b4jdidchu.txt

Preview (first 2KB):
46-
47-## Attempts so far
48-
49:| Dandiset | Paper | Reproduced | Partially | Not reproduced | Blocked | Entry |
schema_version: 2
id: crcns-ret-1-lefebvre-2008-01
dataset:
  archive: crcns
  id: ret-1
  version: unversioned
  doi: 10.6080/K0RF5RZT
paper: doi:10.1242/dev.027912
date: 2026-10-20
entry: crcns-ret-1-lefebvre-2008
provenance:
  kind: agent
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-ret-1-lefebvre-2008-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-ret-1-lefebvre-2008-01
3	dataset:
4	  archive: crcns
5	  id: ret-1
6	  version: unversioned
7	  doi: 10.6080/K0RF5RZT
8	paper: doi:10.1242/dev.027912
9	date: 2026-10-20
10	entry: crcns-ret-1-lefebvre-2008
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	outcomes:
20	- claim: fig1-broad-expression
[... 730 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '^##' docs/pilot-notes.md | tail -8; wc -l docs/pilot-notes.md; grep -n -A12 '"ret-1"\|crcns-ret-1\|ret-1' targets/dandisets.json | head -40
```

```
4228:### 001878, Sun et al. 2021
4320:### 001712, Davatolhagh et al. 2025
4420:### 001888, Hristova et al. 2025
4510:### 000005, Yu et al. 2016
4608:## Protocol pilot-8 (2026-10-19): the paper's own words
4671:## Protocol pilot-9 (2026-10-20): the full text or nothing
4710:## Protocol pilot-10 (2026-10-20): the reader and the author
4752:### 001754, Knierim et al. 2000, third attempt
4855 docs/pilot-notes.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 4228
}
```

```
File content (316.5KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
grep -n -i 'ret' targets/dandisets.json | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0])"
```

```
2271:   "name": "Dataset for \"Coregistration of heading to visual cues in retrosplenial cortex\"",
2467:    "contributor Flynn, Garrett of CatalystNeuro",
3326:   "name": "Data for: Hippocampal Theta Phase Precession Supports Memory Formation and Retrieval of Naturalistic Experience in Humans",
3342:     "title": "Hippocampal Theta Phase Precession Supports Memory Formation and Retrieval of Naturalistic Experience in Humans",
3586:   "name": "Freely moving mouse retrosplenial cortex recordings",
3613:   "name": "Photophysics-informed two-photon voltage imaging using FRET-opsin voltage indicators",
3628:     "title": "Photophysics-informed two-photon voltage imaging using FRET-opsin voltage indicators",
5688:     "title": "Primary motor cortex of the parkinsonian monkey: altered neuronal responses to muscle stretch",
6283:     "title": "Prevalence of IMPG1 and IMPG2 Mutations Leading to Retinitis Pigmentosa or Vitelliform Macular Dystrophy in a Cohort of Patients with Inherited Retinal Dystrophies",
6493:     "title": "Contrasting walking styles map to discrete neural substrates in the mouse brainstem",
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'));t=d['targets']
print(type(t), len(t))
items = t if isinstance(t,list) else list(t.values())
for x in items:
  s=json.dumps(x)
  if 'ret-1' in s or 'crcns' in s.lower(): print(json.dumps(x,indent=1)[:3000])
" | head -80
```

```
<class 'list'> 232
```

**Agent calls Bash**

```bash
ls targets/; grep -rl 'ret-1' targets/ | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(json.dumps(d['targets'][0],indent=1)[:1500])"
```

```
crcns.json
dandisets.json
ebrains.json
pilot.yaml
targets/crcns.json
{
 "dandiset": "000003",
 "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
 "published_version": "0.260218.2052",
 "asset_count": 101,
 "size_gb": 2559.25,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "House mouse"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/crcns.json'));t=d['targets']
for x in t:
  if 'ret-1' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
{
 "id": "ret-1",
 "name": "Multi-electrode recordings from retinal ganglion cells",
 "url": "https://crcns.org/data-sets/retina/ret-1",
 "doi": "10.6080/K0RF5RZT",
 "published_version": null,
 "asset_count": 4,
 "size_gb": 0.07,
 "data_standards": [
  "MATLAB"
 ],
 "species": [
  "House mouse"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1242/dev.027912",
[... 8 more lines not kept]
```

**Agent**

The dataset's entry is in `targets/crcns.json`, not `targets/dandisets.json`, and its `catalystneuro` field is empty. Next I'll read the last five subsections of the notes.

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 4752
}
```

```
File content (316.5KB) exceeds maximum allowed size (256KB). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
cd docs; sed -n '4752,4855p' pilot-notes.md | cut -c1-3000 | head -c 60000
```

```
### 001754, Knierim et al. 2000, third attempt

One claim reproduced, two partially, two not reproduced and five blocked on
the dandiset. The attempt replaces the deprecated 001754-knierim-2000-02,
whose claims were written from the abstract and figure titles; the claims file
was written again from the full text, so most criteria are new. It pins
version 0.260728.1352, the most recent published version, as the draft, which
holds a new conversion that fixes several findings, is unpublished and changed
after the second attempt read it; the three published versions hold the same
blobs, so the files are those the first attempt read. The author put five
questions to a reader, whose answers were written into the criteria; they
changed the reason for blocking `direction-selectivity` from `data_missing` to
`methods_underspecified` and changed no number. Round 1 gave its own outcome
for each claim from the notebook with its conclusion cells and summary removed
and agreed with all 10, but found that the check admitting the deposited maps
(reading M-a) for `fig3-stability-across-sessions` kept the better match when
two units chose one map, so it did not test the criterion's condition that the
pairing be one to one. Tested as the criterion states it, the pairing fails in
session 3, where four units are each tied to two maps, so M-a is not run and
fig3 moved from blocked to not reproduced (6 of 16 and 1 of 16 cells keep
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '4320,4607p' docs/pilot-notes.md
```

```
### 001712, Davatolhagh et al. 2025

Three claims reproduced, two partially, two not reproduced and eleven blocked
on the dandiset. Round 1 had no attempt record and gave its own outcome for
each claim from the notebook with its conclusion cells and summary removed, and
agreed with all 18. Round 2 agreed with all 18 and nothing was proposed, so
there was no third round. The paper, a bioRxiv preprint, compares Nrxn1a
knockout and wild-type mice (8 against 11 mice, 10 sessions each) in the IBL
visual decision task with biased blocks, with widefield calcium imaging of
cortex and a linear encoding model, and reports that knockout mice shift their
choices less between blocks and adapt more slowly after a switch, and show
elevated cortical activity, higher correlations and variance, and a larger loss
of explained variance when movement predictors are shuffled. The psychometric
curve, the dependence of reaction time on contrast, the prior shift and
adaptation after block switches, the response to contralateral stimuli and the
encoding model's full cvR2 and movement contribution were tested on the one
session; the eleven claims that need mice of both genotypes are blocked as
`data_missing`. `fig1e-rt-contrast` is not reproduced (rho -0.053, p = 0.15),
while with reaction times above 0.15 s only the correlation is -0.226 (p =
0.00062) and 149 of 899 onsets fall at or before the stimulus.
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ret-1; wc -c *-report.md; cat author-report.md
```

```
1416 answer-report.md
 3020 author-answers-report.md
 5277 author-report.md
 4046 author-revise-1-report.md
 3716 author-revise-2-report.md
 2756 claims-check-report.md
 3536 claims-report.md
 8879 verifier-1-report.md
 7628 verifier-2-report.md
40274 total
I've done steps 1 to 6 of the Author section. `tools/entry.py all` passes (0 check errors, notebook runs in 277 s) and the verifier's handover package is built in `executed/crcns-ret-1-lefebvre-2008/handover/`. Nothing is committed. I added `entries/crcns-ret-1-lefebvre-2008/`, `attempts/crcns-ret-1-lefebvre-2008-01.yaml` and `questions/crcns-ret-1.yaml`. Some untracked dotfiles (`.bashrc`, `scripts` and others) appeared in the repo root; they are sandbox device mounts, not my files, and should not be committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| 15 histology claims (Figures 1 to 8, Supplementary Figure 1) | blocked, data_missing |
| fig9a-response-variety, fig9c-on-off-index, fig9-rod-cone, fig9b-direction-selective | blocked, data_missing (no spots, flashes, bars or gratings in the data set) |
| fig9-cell-counts | not_reproduced (200 mutant and 122 control units, against 115 and 143) |
| fig9d-rf-size-similar | not_reproduced (bands separate in 18 of 18 combinations; mutant centres smaller, 116 against 156 um) |
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ret-1; for f in author-answers verifier-1 author-revise-1 verifier-2 author-revise-2; do echo "=== $f"; cat $f-report.md; done; git log --format='%h %s' | grep ret-1
```

```
=== author-answers
There was one question, and its answer changed the text of six claims but none of their outcomes. That's because this attempt had already run all three readings the answer names. `tools/entry.py lock` and `all` pass (0 check errors, notebook runs in 251 s), and the handover is built in `executed/crcns-ret-1-lefebvre-2008/handover/`. Nothing is committed, and I did not verify my own work.

## The question and its answer

**Question (fig9d-rf-size-similar, also fig9e, fig9f, fig9g, fig9h and s3):** which flickering-bar recording of a retina gives a cell's spike-triggered average, its firing rate and its model fit? The claims file named the bar widths (8.3 or 16.6 um) but not their orientation, nor what to do when a retina has more than one such recording.

**Answer:** the paper does not say. The claims file now names three readings in the fig9d criterion:
- **A:** the first vertical-bar recording.
- **B:** all vertical-bar recordings pooled, with spikes and frames together. For the firing rate, B uses the pooled spike count and the pooled duration.
- **C:** the horizontal-bar recording where the retina has one, otherwise as A.

Each of the six claims must now be judged under all three readings.

**What it changed:** the first run had used exactly these readings, and computed the rate under B from the pooled count and duration. So the re-run gives the same numbers. The changes are to wording only:
- **Attempt record:** each of the six claims' notes says what the answer changed, and the deviation that said "the bar recording is not fixed by the claims file" is gone.
- **Notebook:** the header, the Measures section and the criterion text for s3, fig9f and fig9h now cite the readings as the claims file's, not as this attempt's own choice. The summary's line on how the analysis differs from the paper is updated to match.
- **Helper:** the docstring of `bar_recordings` in `ret1.py` says the same.

## Outcome per affected claim
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/crcns-ret-1/answer-report.md; head -60 claims/crcns-ret-1/10.1242-dev.027912.yaml; grep -n '^  - id:\|^- id:\|statement:' claims/crcns-ret-1/10.1242-dev.027912.yaml | head -60
```

```
There was one question (on `fig9d-rf-size-similar`, also covering fig9e, fig9f, fig9g, fig9h and s3), and the paper doesn't answer it.

**Question: which flickering-bar recording of a retina should be used (bar orientation, and what to do when a retina has more than one recording)?**
The Methods give only the bar widths ("we projected gratings of adjacent thin bars (8.3 or 16.6 μm width)"). The Results and the Figure 9 legends don't name an orientation or say anything about retinas with several recordings, the supplement isn't in the text, and the paper links no code.

What I changed:
- **Criteria:** the `fig9d-rf-size-similar` criterion now says the paper leaves this open and names the three readings the question proposed. A is the first vertical-bar recording, B is all vertical-bar recordings pooled, and C is the horizontal-bar recording where the retina has one, otherwise A. fig9e, fig9f, fig9g, fig9h and s3 now need their outcome to hold under all three readings. For fig9f under B, the rate is taken over the pooled spike counts and durations.
- **Unchanged:** no claim's statement or expected values, since nothing in the question shows they are wrong about the paper.
- **Questions file:** the answer quotes the passage, and the question is marked `answered: 2026-10-20`.

`python tools/claims_check.py` reports 26 claims, 26 quotes, 0 problems, and both YAML files load. Nothing is committed.
# Claims for Lefebvre, Zhang, Meister, Wang & Sanes (2008), Development 135:4141-4151, on CRCNS
# data set ret-1 (doi:10.6080/K0RF5RZT).
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2644426), as supplied under paper/,
# with its Methods, Results, Discussion and the legends of Figures 1 to 9; the version of
# record's abstract is appended to it. No PDF was supplied. The supplement (Supplementary
# Figures 1 to 3,
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/crcns-ret-1/10.1242-dev.027912.yaml'))
for c in d['claims']: print(c['id'],':',c['statement'].replace(chr(10),' '))
"
```

```
fig1-broad-expression : Pcdh-gamma proteins (Pcdh-gamma-GFP in fusg mice) are present in all five retinal layers and in all six retinal cell types (photoreceptors, horizontal, bipolar, amacrine, RGCs and Mueller glia).
fig2-postnatal-localization : Pcdh-gamma is present in the IPL, neuroblast layer and RGC axons at P0, appears in the developing OPL by P7, and reaches the adult pattern by P14.
fig3-synaptic-localization : Pcdh-gammas are present in pre- and postsynaptic compartments of rod and cone synapses in the OPL, though little is in horizontal cell varicosities, and at many but not only synaptic sites in the IPL.
s1-chx10-recombination : Chx10-Cre recombination is extensive (above 90%) in the INL and ONL, while about half of the cells in the GCL are not recombined.
fig4h-inl-ipl-thinner : At P18, retinas lacking Pcdh-gammas in Chx10-Cre mutants are properly laminated but about 25% thinner than controls, from a selective reduction of about 40% in INL and IPL thickness.
fig4-alleles-equivalent : The INL and IPL are thinned to the same extent in Chx10-Cre;Pcdh-gamma fcon3/fcon3 and fdel/fdel retinas, so fcon3 is functionally a null.
fig4i-cell-type-loss : In peripheral Pax6alpha-Cre;Pcdh-gamma fcon3/fcon3 retina at P18, bipolar, amacrine and retinal ganglion cells are reduced by 45 to 65%, Mueller glia by about 20%, while horizontal cells and photoreceptors differ little from controls.
fig5-postnatal-onset : Mutant and control retinas do not differ perinatally (E17.5 to P3); INL and IPL are thinner in mutants by P7, about 40% thinner by P14, and change little over the following months.
fig5-increased-apoptosis : Apoptosis (cleaved caspase-3) follows the normal time course but is significantly higher in mutant than control retinas during the first postnatal weeks.
fig6f-amacrine-loss-central : In central retina of Pax6alpha-Cre;Pcdh-gamma fcon3/fcon3 mice, where only the Pax6alpha amacrines lack Pcdh-gammas, these amacrines are 58% fewer than in controls, a loss eq
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c 300 docs/pilot-notes.md | od -c | tail -3; git diff --stat
```

```
0000420   s   e   c   t   i   o   n   '   s       u   s   e       o   f
0000440       t   h   e       d   r   a   f   t   .  \n
0000454
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

**Agent calls Bash**

```bash
cd  cat >> docs/pilot-notes.md <<'EOF'

### crcns-ret-1, Lefebvre et al. 2008

Three claims reproduced, two not reproduced and twenty-one blocked on the
data set, none partially reproduced. The data set is on CRCNS and has no
versions, so it is recorded as unversioned; the notebook checks the zip's MD5
against `checksums.md5` and lists each member's CRC-32. The author put one
question to a reader, which flickering-bar recording of a retina to use; the
paper does not say, so the claims file now names three readings (A, the first
vertical-bar recording; B, all vertical-bar recordings pooled; C, the
horizontal-bar recording where the retina has one, otherwise A), which the
first run had already used, and the answer changed the text of six claims and
no outcome. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with all 26, and asked for
the frame and onset search of 20080702_R4 to be run in the notebook. The search
showed that the stated frame lengths of two vertical-bar recordings are wrong,
and with the corrected frame the DKW bands overlap under reading B with the svd
separation, so `fig9d-rf-size-similar` separates in 17 of 18 combinations and
moved from not reproduced to blocked as `methods_underspecified`. Round 2
agreed with all 26, including the change, and nothing was proposed, so there
was no third round. The paper, "Gamma-Protocadherins regulate neuronal
survival but are dispensable for circuit formation in retina" in Development,
removes the Pcdh-gamma cluster from mouse retina with Chx10-Cre or
Pax6alpha-Cre, and reports from histology that the mutant retina is properly
laminated but its INL and IPL are thinned, with increased apoptosis, that
deleting Bax rescues the neurons that die, and that their processes reach the
appropriate IPL sublaminae, and from multielectrode recordings of retinal
ganglion cells that mutant cells have a similar variety of responses, similar
receptive field sizes and an unaltered threshold, with a slower time course, a
lower firing rate and a reduced gain. The 15 histology claims and the four on
flashing spots, flashes, moving bars and gratings are blocked as
`data_missing`; the cell counts and the six claims on the white-noise responses
were tested. `fig9-cell-counts` is not reproduced (200 mutant and 122 control
units against 115 and 143), and `fig9g-threshold-unaltered` is not reproduced
(36 of 36 combinations separate, with mutant thresholds higher).
`fig9e-slower-time-course` (36 of 36, mutant medians longer by 16.7 to 33.3
ms) and `fig9f-lower-firing-rate` (9 of 9, reading A median 3.82 against 9.02
Hz) are reproduced, and `fig9h-gain-reduced` is blocked as
`methods_underspecified` because the printed and continuous forms of the
nonlinearity disagree. `s3-receptive-field-surrounds` is reproduced under its
criterion, but null STAs meet the rule in 194 to 198 of 200 mutant and 119 to
121 of 122 control units, so the result is no evidence for or against
surrounds. Some outcomes rest on weak ground: fig9d rests on one borderline
combination and on the frame correction, and with the frames as deposited all
18 separate; among units with an STA peak above twice the null's (103 mutant,
107 control), fig9f and fig9g would be blocked, as no DKW band separates, so
their outcomes hold only on all units, as the claims file's header reads the
groups; and in fig9-cell-counts a threshold of STA strength between 1.5 and 2
could put the mutant count inside its tolerance, so the outcome rests on the
control count, which no reading can bring inside.

The data set holds only the white-noise recordings behind Figure 9D to 9H. The
histology of Figures 1 to 8 and Supplementary Figure 1, and the flashing-spot,
flash, moving-bar and grating recordings of Figure 9A to 9C, are not in it, and
the paper names no other deposit, so 19 of the 26 claims cannot be tested. It
holds 200 mutant and 122 control units (and 3 from a Bax -/- mutant), where the
paper's Figure 9 has 115 mutant and 143 control cells, and it does not say how
its units relate to the paper's, which were kept, or why the counts differ. 95
of the 122 control units are labelled "WT (chx10 het)", while the paper's
Figure 9 legend gives the controls as Pax6-Cre;Pcdh-gamma +/f-del or
Pcdh-gamma f-del/f-del without Cre. In the 8 recordings of 20080628_R4,
20080628_R6, 20080702_R1 and 20080702_R4, 82 of 86 spike trains are not in time
order: each runs to 1440 s and then holds a second segment between 720 and 780
s, though the stimulus runs to 1500 s, which is consistent with the last minute
stored with a 720 s offset in place of 1440 s. The frame lengths stated for the
vertical-bar recordings of 20080702_R1 and 20080702_R4 (16.6691 and 16.6653 ms)
are not those of the stimulus; rebuilt with the stated frame, the bars of
20080702_R4 give no STA above the null in any of its 12 units (median ratio
0.96), and with 16.6718 ms, the frame of every other bar recording, the median
ratio is 2.57 and 10 of the 12 units have peaks above twice the null's. 16
pairs of units share 70 to 100% of their spikes within 0.5 ms in every
recording of their retina (12 pairs in mutant retinas, 4 in a control retina),
most likely single neurons sorted twice, and the data set does not mark them.
The files do not give the age of the mice, the Pcdh-gamma allele (the paper's
Results say fcon3 and its Figure 9 legend f-del), the region recorded in the
Pax6-Cre retinas, whose periphery alone the paper used, or the cell type of the
units. Other findings: 97 of 200 mutant and 15 of 122 control units have an STA
peak less than twice the null's, and much of the fig9d difference comes from
them; all 5 retinas recorded with 8.3 um bars are mutant, and every control
retina was recorded with 16.6 um bars; and one checkerboard recording
(20080628_R5) has 1 or 2 spikes near 2 s out of order in 15 units.

The notebook ran in 277 s in the first clean run, 251 s after the answer,
about 8 minutes after round 1 and 500 s after round 2. Two string-escaping
errors in the author's notebook generator were fixed along the way. Round 1's
points led to a label-shuffle calibration of the bands (the binomial band
separates in 35% of shuffles, the bootstrap band in 37% and DKW in 0 of 1600),
counts of LN fits at the grid edge, a synthetic check of the LN fit, a table of
units per retina and example STAs; with the corrected frame the mutant count
above an STA ratio of 1.5 went from 126 to 138. Round 2 found statements the
outputs did not support, among them the README stating the misplaced last
minute as fact, a summary sentence saying the results hold with the 16.6 um
bars alone, which is false for fig9d, and grid-edge counts described as fits
at the top of the grid where both ends were counted, and these were corrected;
the author then added every claim's combinations under all three readings for
the frames as deposited, units with clear STAs and the 16.6 um bars alone.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: "units with a flicker
response" in fig9-cell-counts is undefined; the protocol says how to count
recordings deposited twice but not units sorted twice; the criteria do not say
what to do when bands separate in both directions; a criterion can be met by
noise, with no rule for when its own null meets it; the clock check assumes
trial tables, which continuous white noise does not have; the schema has no
kind for disagreement between the paper and the data set's labels; and
`archives.md` asks for MD5s of the files read, where only the zip has one.
EOF
git diff --stat
```

```
README.md           |   1 +
 docs/pilot-notes.md | 105 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 106 insertions(+)
```

**Agent calls Bash**

```bash
cd  git diff docs/pilot-notes.md | grep -n -i 'rather\|—\|\*\*' ; echo done
```

```
done
```

**Agent**

I added the README row with `tools/readme_row.py` (3 reproduced, 0 partially, 2 not reproduced, 21 blocked) and added the subsection to the end of `docs/pilot-notes.md`. Nothing is committed.

The dataset has no entry in `targets/dandisets.json`. I used its entry in `targets/crcns.json` instead. Its `catalystneuro` field is empty, so the findings paragraph doesn't open with the CatalystNeuro sentence.

### crcns-ret-1, Lefebvre et al. 2008

Three claims reproduced, two not reproduced and twenty-one blocked on the
data set, none partially reproduced. The data set is on CRCNS and has no
versions, so it is recorded as unversioned; the notebook checks the zip's MD5
against `checksums.md5` and lists each member's CRC-32. The author put one
question to a reader, which flickering-bar recording of a retina to use; the
paper does not say, so the claims file now names three readings (A, the first
vertical-bar recording; B, all vertical-bar recordings pooled; C, the
horizontal-bar recording where the retina has one, otherwise A), which the
first run had already used, and the answer changed the text of six claims and
no outcome. Round 1 gave its own outcome for each claim from the notebook with
its conclusion cells and summary removed and agreed with all 26, and asked for
the frame and onset search of 20080702_R4 to be run in the notebook. The search
showed that the stated frame lengths of two vertical-bar recordings are wrong,
and with the corrected frame the DKW bands overlap under reading B with the svd
separation, so `fig9d-rf-size-similar` separates in 17 of 18 combinations and
moved from not reproduced to blocked as `methods_underspecified`. Round 2
agreed with all 26, including the change, and nothing was proposed, so there
was no third round. The paper, "Gamma-Protocadherins regulate neuronal
survival but are dispensable for circuit formation in retina" in Development,
removes the Pcdh-gamma cluster from mouse retina with Chx10-Cre or
Pax6alpha-Cre, and reports from histology that the mutant retina is properly
laminated but its INL and IPL are thinned, with increased apoptosis, that
deleting Bax rescues the neurons that die, and that their processes reach the
appropriate IPL sublaminae, and from multielectrode recordings of retinal
ganglion cells that mutant cells have a similar variety of responses, similar
receptive field sizes and an unaltered threshold, with a slower time course, a
lower firing rate and a reduced gain. The 15 histology claims and the four on
flashing spots, flashes, moving bars and gratings are blocked as
`data_missing`; the cell counts and the six claims on the white-noise responses
were tested. `fig9-cell-counts` is not reproduced (200 mutant and 122 control
units against 115 and 143), and `fig9g-threshold-unaltered` is not reproduced
(36 of 36 combinations separate, with mutant thresholds higher).
`fig9e-slower-time-course` (36 of 36, mutant medians longer by 16.7 to 33.3
ms) and `fig9f-lower-firing-rate` (9 of 9, reading A median 3.82 against 9.02
Hz) are reproduced, and `fig9h-gain-reduced` is blocked as
`methods_underspecified` because the printed and continuous forms of the
nonlinearity disagree. `s3-receptive-field-surrounds` is reproduced under its
criterion, but null STAs meet the rule in 194 to 198 of 200 mutant and 119 to
121 of 122 control units, so the result is no evidence for or against
surrounds. Some outcomes rest on weak ground: fig9d rests on one borderline
combination and on the frame correction, and with the frames as deposited all
18 separate; among units with an STA peak above twice the null's (103 mutant,
107 control), fig9f and fig9g would be blocked, as no DKW band separates, so
their outcomes hold only on all units, as the claims file's header reads the
groups; and in fig9-cell-counts a threshold of STA strength between 1.5 and 2
could put the mutant count inside its tolerance, so the outcome rests on the
control count, which no reading can bring inside.

The data set holds only the white-noise recordings behind Figure 9D to 9H. The
histology of Figures 1 to 8 and Supplementary Figure 1, and the flashing-spot,
flash, moving-bar and grating recordings of Figure 9A to 9C, are not in it, and
the paper names no other deposit, so 19 of the 26 claims cannot be tested. It
holds 200 mutant and 122 control units (and 3 from a Bax -/- mutant), where the
paper's Figure 9 has 115 mutant and 143 control cells, and it does not say how
its units relate to the paper's, which were kept, or why the counts differ. 95
of the 122 control units are labelled "WT (chx10 het)", while the paper's
Figure 9 legend gives the controls as Pax6-Cre;Pcdh-gamma +/f-del or
Pcdh-gamma f-del/f-del without Cre. In the 8 recordings of 20080628_R4,
20080628_R6, 20080702_R1 and 20080702_R4, 82 of 86 spike trains are not in time
order: each runs to 1440 s and then holds a second segment between 720 and 780
s, though the stimulus runs to 1500 s, which is consistent with the last minute
stored with a 720 s offset in place of 1440 s. The frame lengths stated for the
vertical-bar recordings of 20080702_R1 and 20080702_R4 (16.6691 and 16.6653 ms)
are not those of the stimulus; rebuilt with the stated frame, the bars of
20080702_R4 give no STA above the null in any of its 12 units (median ratio
0.96), and with 16.6718 ms, the frame of every other bar recording, the median
ratio is 2.57 and 10 of the 12 units have peaks above twice the null's. 16
pairs of units share 70 to 100% of their spikes within 0.5 ms in every
recording of their retina (12 pairs in mutant retinas, 4 in a control retina),
most likely single neurons sorted twice, and the data set does not mark them.
The files do not give the age of the mice, the Pcdh-gamma allele (the paper's
Results say fcon3 and its Figure 9 legend f-del), the region recorded in the
Pax6-Cre retinas, whose periphery alone the paper used, or the cell type of the
units. Other findings: 97 of 200 mutant and 15 of 122 control units have an STA
peak less than twice the null's, and much of the fig9d difference comes from
them; all 5 retinas recorded with 8.3 um bars are mutant, and every control
retina was recorded with 16.6 um bars; and one checkerboard recording
(20080628_R5) has 1 or 2 spikes near 2 s out of order in 15 units.

The notebook ran in 277 s in the first clean run, 251 s after the answer,
about 8 minutes after round 1 and 500 s after round 2. Two string-escaping
errors in the author's notebook generator were fixed along the way. Round 1's
points led to a label-shuffle calibration of the bands (the binomial band
separates in 35% of shuffles, the bootstrap band in 37% and DKW in 0 of 1600),
counts of LN fits at the grid edge, a synthetic check of the LN fit, a table of
units per retina and example STAs; with the corrected frame the mutant count
above an STA ratio of 1.5 went from 126 to 138. Round 2 found statements the
outputs did not support, among them the README stating the misplaced last
minute as fact, a summary sentence saying the results hold with the 16.6 um
bars alone, which is false for fig9d, and grid-edge counts described as fits
at the top of the grid where both ends were counted, and these were corrected;
the author then added every claim's combinations under all three readings for
the frames as deposited, units with clear STAs and the 16.6 um bars alone.
Untracked files in the repository root that the author did not create were
left alone. The author's points on the protocol: "units with a flicker
response" in fig9-cell-counts is undefined; the protocol says how to count
recordings deposited twice but not units sorted twice; the criteria do not say
what to do when bands separate in both directions; a criterion can be met by
noise, with no rule for when its own null meets it; the clock check assumes
trial tables, which continuous white noise does not have; the schema has no
kind for disagreement between the paper and the data set's labels; and
`archives.md` asks for MD5s of the files read, where only the zip has one.

## End of run

20 turns, 2 minutes, result: success.
