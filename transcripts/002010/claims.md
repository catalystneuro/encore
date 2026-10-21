# 002010 · claims · run 39545069211

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/002010/ claims/001453/ paper/ 2>&1; git log --stat -3 | head -40; grep -n "^#" docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,170p docs/protocol.md; cat transcripts/002010/claims-report.md transcripts/002010/claims-check-report.md
```

```
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim, and it asks a reader for any method detail the file lacks.
- The **verifier** checks the author's work and must not be the author.

[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; head -30 *.txt; wc -l *.txt; grep -n "Z-scores of the change" -A3 *.txt; pdfinfo *.supp1.pdf | grep Pages; pdfinfo *.supp2.pdf | grep Pages; pdftotext -layout *.supp1.pdf - | head -60; pdftotext -layout *.supp2.pdf - | head -60
```

```
DOI: 10.1101/2023.04.19.537568
Version: preprint, version 1
Source: bioRxiv JATS XML (api.biorxiv.org)
Stored: 2026-10-20
Extracted: JATS XML flattened; with 2 supplement PDF(s), extracted with PyMuPDF (dehyphenated, NFKC)
------------------------------------------------------------------------
Contrasting walking styles map to discrete neural substrates in the mouse brainstem

## Abstract

Walking is a slow gait which is particularly adaptable to meet internal or external needs and is prone to maladaptive alterations that lead to gait disorders. Alterations can affect speed, but also style (the way one walks). While slowed speed may signify the presence of a problem, style represents the hallmark essential for clinical classification of gait disorders. However, it has been challenging to objectively capture key stylistic features while uncovering neural substrates driving these features. Here we revealed brainstem hotspots that drive strikingly different walking styles by employing an unbiased mapping assay that combines quantitative walking signatures with focal, cell type specific activation. We found that activation of inhibitory neurons that mapped to the ventromedial caudal pons induced slow motion-like style. Activation of excitatory neurons that mapped to the ventromedial upper medulla induced shuffle-like style. Contrasting shifts in walking signatures distinguished these styles. Activation of inhibitory and excitatory neurons outside these territories or of serotonergic neurons modulated walking speed, but without walking signature shifts. Consistent with their contrasting modulatory actions, hotspots for slow-motion and shuffle-like gaits preferentially innervated different substrates. These findings lay the basis for new avenues to study mechanisms underlying (mal)adaptive walking styles and gait disorders.

## Graphical abstract

## Introduction

Walking is a slow gait which is particularly adaptable and is prone to maladaptive alterations that lead to 
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^## \|^=====\|^# \|Supplement" 10.1101-2023.04.19.537568.txt | head -150
```

```
<persisted-output>
Output too large (32.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/b805f225-bdcc-488e-a776-51b0acce0727/tool-results/b0gat5b9p.txt

Preview (first 2KB):
9:## Abstract
13:## Graphical abstract
15:## Introduction
27:## Which neural substrates modulate walking style?
33:## Results
35:## Chemogenetic mRF modulation elicited different walking styles
41:## Chemogenetic activation of VGaT, VGluT2 or SerT mRF neurons elicited contrasting walking styles.
51:## Slomo walking is defined by upward shifts in select gait signatures
57:## Slomo walking style was characterized by walking signature shifts and changes in EMG metrics that dictate the swing phase
63:## Activation of the anterior tibial muscle is prolonged during slomo walking
67:## Do slomo mice have deficits in other (loco)motor tasks?
71:## Shifts in gait signatures that define Shuffle style contrast those of Slomo walking
77:## : Shuffle style was characterized by gait signature shifts and EMG changes that are distinct from slomo style
81:## Anterior tibial and gastrocnemius muscles co-activate during shuffle walking
85:## Serotonergic activation modulates walking speed without shifts in walking signatures
91:## mRF SerT hM3Dq activation modulated gait speed without style changes
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^## " 10.1101-2023.04.19.537568.txt | sed -n 20,200p | cut -c1-120
```

```
123:## Hotspots for slomo and shuffle walking target distinct neuronal substrates
129:## Slomo and shuffle hotspots preferentially targeted different substrates in the lumbar cord.
137:## May sensory gating contribute to prolongation of swing time in slomo walking?
143:## S lomo walking style was associated with modulation of low but not high threshold sensory stimuli.
147:## Slomo style involves gait phase specific mechanisms
153:## Two seconds of optogenetic stimulation of the slomo site reproduced chemogenetic changes in gait style, whereas t
157:## Discussion
161:## The unique design served to elicit, quantify and map walking styles
165:## Discrete mRF sites serve distinct walking styles
171:## Walking style modules represent components of more complex mobility repertoires
181:## Ideas and speculation
183:## Are different walking styles driven by unique downstream neural substrates?
187:## Slomo walking
191:## Shuffle walking
197:## Faster walking
201:## How may these insights translate to human walking?
205:## Materials and Methods
207:## Ethics statement
211:## Viral vectors and tracers
215:## DREADD activation experiments
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 321,342p 10.1101-2023.04.19.537568.txt | cut -c1-1500; grep -n "SUPPLEMENT\|supp1\|supp2\|^--- \|^=== " 10.1101-2023.04.19.537568.txt | head; sed -n 346,420p 10.1101-2023.04.19.537568.txt | cut -c1-300
```

```
## Data availability statement

The data that support the findings of this study are presented in the Figures, Supplementary Figures, and an extensive set of Tables. Additional source data can be made available through the corresponding author upon reasonable request.

## Code availability statement

Custom MATLAB code was used to extract gait data from video files and Spike2 code was used to deliver optogenetic pulses based upon EMG feedback. Code has been made available: https://sourceforge.net/projects/gait-analysis-gui/ https://sourceforge.net/projects/gait-emg-step-trigger/

## Supporting information

## Acknowledgements

The authors would like to thank Dr Brad Lowell (BIDMC) for AAV-DIO-synaptophysin-mCherry and Dr Susan Dymecki (Harvard Medical School) for SerT-cre breeders. This work was supported by R01 NS079623 (VV), R25 NS070682 (AK), the JG Foundation (VV) and donations from grateful patients (VV).

## Adherence to scientific standards

Reporting of study details is in accordance with ARRIVE guidelines for animal research.

## Competing interests

[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^##### " 10.1101-2023.04.19.537568.txt; grep -n "Table S\?[0-9]*\b" 10.1101-2023.04.19.537568.txt | awk -F: '$1>1400' | head -50 | cut -c1-200
```

```
411:##### Supplement: supplementary figures (media-1.pdf)
1867:##### Supplement: supplementary tables S1 to S18 (media-2.pdf)
1858:bars represent SD. Ordinary One Way ANOVA or Kruskall Wallis followed by multiple comparison test (see Supplementary Table 15S).
1870:Table 1
2181:Table 2
2262:Table 3
2692:Supplementary Table 4
3177:Supplementary Table 5
3217:Supplementary Table 6
3384:Supplementary Table 7
3673:Supplementary Table 8
4104:Supplementary Table 9
4269:Supplementary Table 10
4680:Supplementary Table 11
4965:Supplementary Table 12
5395:Supplementary Table 13
5908:Supplementary Table 14
6072:Supplementary Table 15
6273:Supplementary Table 16
6355:Supplementary Table 17
[... 1 more lines not kept]
```

**Agent**

Supplement tables S1–S18 and the supplementary figures are now in the text. The Z-score equation is still missing from the Methods; I'll treat it as an open detail. Reading the main text now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2023.04.19.537568.txt",
 "offset": 33,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2023.04.19.537568.txt",
 "offset": 205,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls; ls tools docs; grep -rn "002010" --include=*.yaml --include=*.md . | grep -v transcripts | head; sed -n 1,80p tools/claims_check.py
```

```
LICENSE
README.md
attempts
bunfig.toml
claims
docs
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
questions
schemas
scripts
targets
tests
tools
transcripts
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1920,1960p papers/manifest.yaml; ls targets | head; grep -rl "002010" targets | head; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
pdf: false
    supplements: 0
  001968:
  - doi: 10.1038/s41593-026-02260-w
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  '002010':
  - doi: 10.1101/2023.04.19.537568
    status: stored
    version: preprint, version 1
    source: bioRxiv JATS XML (api.biorxiv.org)
    pdf: false
    supplements: 0
  '002013':
  - doi: 10.1021/acschemneuro.5c00071
    status: stored
    version: as served by europe_pmc
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"; python -c "
import json;d=json.load(open('targets/dandisets.json'))
x=[e for e in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '002010' in json.dumps(e)]
print(json.dumps(x,indent=1)[:3000])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 198 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/dandisets.json'))
L=d[0] if isinstance(d,list) and isinstance(d[0],list) else d
for e in L:
  if e.get('dandiset')=='002010': print(json.dumps(e,indent=1))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    if e.get('dandiset')=='002010': print(json.dumps(e,indent=1))
       ^^^^^
AttributeError: 'str' object has no attribute 'get'
```

**Agent calls Bash**

```bash
cd  grep -n '"002010"' -A30 targets/dandisets.json | head -40
```

```
6482:   "dandiset": "002010",
6483-   "name": "VanderHorst Contrasting Walking Styles",
6484-   "published_version": null,
6485-   "asset_count": 1,
6486-   "size_gb": 0.15,
6487-   "data_standards": [],
6488-   "species": [],
6489-   "approaches": [],
6490-   "papers": [
6491-    {
6492-     "doi": "10.1101/2023.04.19.537568",
6493-     "title": "Contrasting walking styles map to discrete neural substrates in the mouse brainstem",
6494-     "relation": "IsDescribedBy",
6495-     "resource_type": "JournalArticle",
6496-     "preprint": true
6497-    }
6498-   ],
6499-   "catalystneuro": []
6500-  },
6501-  {
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 161,204p 10.1101-2023.04.19.537568.txt
```

```
## The unique design served to elicit, quantify and map walking styles

The conceptual and technical design of this study stood out from prior work. We enhanced translational potential by focusing on walking gait, which is shared among bi- and quadripeds, rather than speed capacity ( 20 ) or transitions between gait patterns that are unique to quadrupeds ( 22 ). Secondly, while treadmill can be used to control speed ( 23 ) this would have impeded self-selection of speed, crucial for this study. Furthermore, we did not optimize our assay to halt mice ( 18 ), as that would have defied the purpose of our study. Additionally, canonical activation of the hM3Dq receptor magnifies physiological responses and differs from direct depolarization by optogenetic activation ( 44 , 45 ) that was used in many prior mouse studies ( 18 , 20 , 23 ). Next, we combined the high specificity of discrete hM3Dq modulation sites in eliciting walking styles with a sensitive walking signature toolkit into an unbiased assay to map out a functional sub-organization, a common feature of supraspinal systems ( 46 , 47 ), but beyond prior locomotor studies that employed other methodologies ( 18 , 20 , 23 ). Finally, hindlimbs provide the propulsive component of walking in both bi- and quadruped models and therefore we focused on mRF sites with connections to the lumbar cord, whether with or without connections to other CNS sites, while avoiding sites exclusively serving forelimb goal directed movements ( 48 ) and lateral sites serving respiration and autonomic functions ( 25 , 49 ).

## Discrete mRF sites serve distinct walking styles

The degree of functional-anatomical organization within the mRF remains controversial. We revealed a more precise functional-anatomical organization within the mRF than reported in studies using larger transfection sites, other functional tools, and anatomy-based site selection ( 18 , 20 , 48 , 49 ). Both slomo and shuffle hotspots reside within the ventral mRF, but 
[... 36 more lines not kept]
```

**Agent**

Now the supplementary figure legends in full.

**Agent calls Bash**

```bash
cd paper; sed -n 382,410p 10.1101-2023.04.19.537568.txt
```

```
Figure 3-Figure supplement 2: Quantification of changes in anterior tibial EMG in experimental hM3Dq transfected VGaT mice. Supplementary to Fig. 3. a: Graphs showing anterior tibial (TA) burst and interburst duration, amplitude and area under the curve (AUC) during steady walking in saline and CNO conditions for each of the Z score based subgroups of VGaT hM3Dq mice. Bars represent average, error bars SD. Two tailed paired t-test between conditions. EMG amplitude and AUC were normalized to the amplitude and AUC during swimming, with recruitment being near maximum, in the saline condition. Data is not controlled for speed. Table S4 for statistical details including interburst, swimming, gastrocnemius and WT control data. b: Rectified averaged EMG during ground walking and swimming of a representative VGaT hM3Dq slomo mouse (Z SwT >3) showing activity of biceps femoris (BF) and triceps muscles (Tr; a forelimb muscle), in addition to TA activity (as in Fig. 3 ) during saline and CNO conditions. c: Correlation between Z SwT and TA Z BurstDuration in VGaT hM3Dq mice instrumented with EMG (Pearson correlation coefficient; Table S5). Z scores indicate the change between baseline and CNO activation conditions. Changes in TA burst duration are strongly correlated with changes in swing time in VGaT mice. d: Correlation between Z SwT and Z BurstAmplitude in VGaT hM3Dq mice (Pearson correlation coefficient; Table S5). Changes in TA burst amplitude are not correlated with changes in swing time.

Figure 3-Figure supplement 3: Absence of gait asymmetries following activation of unilaterally transfected VGaT hM3Dq neurons in the slow motion hotspot. Supplementary to Fig. 3; text results. Assessment of spatial (stride length) and temporal (swing time) asymmetries following unilateral transfection of VGaT-hM3Dq neurons involving the slow-motion hotspot (N=6). i: Stride length or swing time ipsi- or contralateral to the transfected site did not vary between saline and CNO conditions.
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 376,380p 10.1101-2023.04.19.537568.txt; grep -n -i "z-score\|z score\|mean\b\|σ\|μ" 10.1101-2023.04.19.537568.txt | awk -F: '$1>410' | head -40
```

```
Representative example of the effect of mRF VGaT-ChR2 activation from the Slomo hotspot on gait. The same mouse is shown at baseline (top walkway) and during optogenetic stimulation (bottom walkway). Videos from the walkway and beam are played at 25% and 100% of real-time speed, respectively. The transfection site was bilateral and centered in the ventral mRF at and rostral to the rostral pole of the facial nucleus, with a midline fiber positioned immediately dorsal to the transfection site.

Figure 2-Figure supplement 1: Dose and time response data. Supplementary to results (paragraph 1), and methods. a: Effects of doses of 0.15, 0.3 and 0.6mg/kg CNO (i.p.) on average stride velocity and average swing time (n=14 VGaT-ires-cre mice with Z SwT >2; n=20 VGluT2-ires-cre mice with Z SwT <-2; one way ANOVA, followed by Dunnett’s multiple comparisons test with single pooled variance). b: Effect of a single dose of 0.3mg/kg CNO on swing time and stride velocity at different time points (n=5 VGaT-ires-cre mice with Z SwT >2; Friedman test, followed by Dunn’s multiple comparisons test). Table S1 for statistical details. Bars indicate SD.

734:saline and CNO conditions for each of the Z score based subgroups of VGaThM3Dq mice. Bars represent average, error bars SD. Two tailed 
740:(Pearson correlation coefficient; Table S5). Z scores indicate the change between baseline and CNO activation conditions. Changes in TA 
1074:saline and CNO conditions for each of the Z score based subgroups of VGluT2hM3Dq mice. Bars represent average, error bars SD. Two 
1078:ZBurstDuration in VGluT2hM3Dq mice instrumented with EMG (Pearson correlation coefficient; Table S5). Z scores indicate the change between 
1384:saline and CNO conditions for each of the Z score based subgroups of SerThM3Dq mice. Bars represent average, error bars SD. Two tailed 
1418:100μm
1446:3% levels of opacity, respectively. This process was repeated at rostrocaudal intervals of 320μm. i: bar= 1 mm; ii: bar = 200 μm; iii
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1867,2262p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g' | cut -c1-6000
```

```
##### Supplement: supplementary tables S1 to S18 (media-2.pdf)||
=== page 1 ===|Table 1|CNO Dose and Time response titration|with Supplementary Figure 1|VGaT Dose Response|Time tested 1-2 hrs post CNO injection|One-way ANOVA|a 0.05|Group Z > 2 (slomo)|N|Mean (s)|SD (s)|F (DFn, DFd)|P value|Dunnett's multiple comparisons test|Mean Diff.|95.00% CI of diff.|P Value, a 0.05|saline|14|0.103|0.009|F (3, 43) = 27.14|P<0.0001|Saline vs. 0.15 mg/kg|-0.07015|-0.09294 to -0.04736|0.0001|0.15 mg/kg CNO|6|0.173|0.025|Saline vs. 0.3 mg/kg|-0.05342|-0.07107 to -0.03577|0.0001|0.30 mg/kg CNO|14|0.157|0.022|Saline vs. 0.6 mg/kg|-0.04278|-0.06077 to -0.02479|0.0001|0.60 mg/kg CNO|13|0.146|0.021|VGaT Dose Response|Time tested 1-2 hrs post CNO|One-way ANOVA|a 0.05|Group Z > 2 (slomo)|N|Mean (cm/s)|SD (cm/s)|F (DFn, DFd)|P value|Dunnett's multiple comparisons test|Mean Diff.|95.00% CI of diff.|P Value, a 0.05|saline|14|11.29|4.31|F (3, 43) = 6.283|0.001|Saline vs. 0.15 mg/kg|5.963|1.915 to 10.01|0.002|0.15 mg/kg CNO|6|5.33|1.87|Saline vs. 0.3 mg/kg|4.133|0.9976 to 7.269|0.007|0.30 mg/kg CNO|14|7.16|3.19|Saline vs. 0.6 mg/kg|4.358|1.163 to 7.554|0.005|0.60 mg/kg CNO|13|6.94|3.00|VGluT2 Dose Response|Time tested 1-2 hrs post CNO|One-way ANOVA|a 0.05|Group Z< -2 (shuffle)|N|Mean (s)|SD (s)|F (DFn, DFd)|P value|Dunnett's multiple comparisons test|Mean Diff.|95.00% CI of diff.|P Value, a 0.05|saline|20|0.098|0.017|F (3, 59) = 10.96|P<0.0001|Saline vs. 0.15 mg/kg|0.02248|0.00867 to 0.0363|0.0007|0.15 mg/kg CNO|9|0.076|0.011|Saline vs. 0.3 mg/kg|0.02355|0.01267 to 0.03444|0.0001|0.30 mg/kg CNO|20|0.075|0.015|Saline vs. 0.6 mg/kg|0.01908|0.007086 to 0.03107|0.0009|0.60 mg/kg CNO|14|0.079|0.008|VGluT2 Dose Response|Time tested 1-2 hrs post CNO|One-way ANOVA|a 0.05|Group Z < -2 (shuffle)|N|Mean (cm/s)|SD (cm/s)|F (DFn, DFd)|P value|Dunnett's multiple comparisons test|Mean Diff.|95.00% CI of diff.|P Value, a 0.05|saline|20|10.95|1.97|F (3, 59) = 11.19|P<0.0001|Saline vs. 0.15 mg/kg|3.681|1.61 to 5
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2262,2692p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g'
```

```
Table 3|Gait metrics with saline versus CNO in VGaT sub-cohorts|with Figure 3 and |Supplementary Figure 2|Footfall metrics|Group Z Swing Time >3 (slomo)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|Figure 3|N= 9|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|9.91|5.70|5.67|3.71|t=3.33 df=8|0.01|Stride length (mm)|44.7 (2, 479)|<0.0001|Stride length (mm)|40.93|11.88|40.25|12.49|t=0.09 df=8|0.93|n Strides:|Swing time (s)|160.1 (2, 479)|<0.0001|Swing time (s)|0.10|0.02|0.16|0.05|t=11.88 df=8|<0.0001|saline: n = 320|Stance time (s)|2.83 (4, 519)|0.02|Stance time (s)|0.43|0.33|0.83|0.69|t=5.12 df=8|0.0009|CNO: n = 313|Cadence (Hz)|24.27 (2, 548)|<0.0001|Cadence (Hz)|2.35|0.97|1.38|0.78|t=6.89 df=8|0.0001|Swing speed (cm/s)|42.4 (2, 522)|<0.0001|Swing speed (cm/s)|41.69|10.82|26.63|8.35|t=8.07 df=8|<0.0001|Group 3>Z Swing Time>2 (intermediate slomo)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|N=5|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|13.59|3.66|9.98|2.88|t=5.99 df=4|0.004|Stride length (mm)|38.84 (2, 260)|<0.0001|Stride length (mm)|46.84|6.05|49.02|5.17|t=2.489 df=4|0.07|n Strides:|Swing time (s)|41.56 (2, 260)|<0.0001|Swing time (s)|0.11|0.01|0.15|0.02|t=9.679 df=4|0.0006|saline: n = 186|Stance time (s)|5.171 (4, 252)|0.0005|Stance time (s)|0.32|0.09|0.43|0.12|t=2.659 df=4|0.06|CNO: n = 170|Cadence (Hz)|21.21 (2, 225)|<0.0001|Cadence (Hz)|2.84|0.41|1.99|0.36|t=7.336 df=4|0.002|Swing speed (cm/s)|31.18 (2, 322)|<0.0001|Swing speed (cm/s)|42.68|5.72|34.30|5.52|t=6.651 df=4|0.003|Group Z Swing Time <2 (non-slomo)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|Supplementary Figure 2|N= 21|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|11.63|3.84|9.45|3.73|t=2.49 df=20|0.02|Stride length (mm)|2.62 (2, 1012)|0.07|Stride length (mm)|43.76|5.75|42.43|6.84|t=0.85 df=20|0.41|n Strides:|Swing time (s)|3.91 (2, 1012)|0.02|Swing time (s)|0.11|0.02|0.12|0.02|t=1.94 df=20|0.07|saline: n = 671|Stance time (s)|1.47 (4, 1133)|0.21|Stance time (s)|0.41|0.14|0.55|0.25
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 2692,3673p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g'
```

```
Supplementary Table 4|A: Anterior Tibial EMG in VGaT sub-cohorts|with Supplementary  Figure 3|Saline|CNO|Paired, two-tailed t test|(alpha=0.05)|with Supplementary  Figure 3|Walk|Sub-cohort (Z Swing Time)|N|Average|SD|Average|SD|t, df|p|Duration|burst (sec)|Z>2 (slomo)|6|0.07|0.022|0.16|0.04|t=6.475 df=5|0.001|Z<2 (non-slomo)|10|0.07|0.014|0.09|0.05|t=2.076 df=9|0.07|WT|4|0.09|0.037|0.10|0.03|t=1.376 df=3|0.26|interburst (sec)|Z>2 (slomo)|6|0.37|0.157|1.82|1.14|t=3.445 df=5|0.02|Z<2 (non-slomo)|10|0.38|0.126|0.74|0.38|t=3.316 df=9|0.01|WT|4|0.45|0.231|0.49|0.13|t=0.4227 df=3|0.70|Peak amplitude|burst|Z>2 (slomo)|6|0.43|0.19|0.39|0.20|t=1.678 df=5|0.15|(Normalized)|Z<2 (non-slomo)|10|0.35|0.14|0.30|0.08|t=0.7027 df=9|0.50|WT|4|0.34|0.03|0.34|0.02|t=0.04207 df=3|0.97|interburst|Z>2 (slomo)|6|0.54|0.26|0.29|0.11|t=3.04 df=5|0.03|Z<2 (non-slomo)|10|0.46|0.19|0.37|0.18|t=2.721 df=9|0.02|WT|4|0.51|0.19|0.39|0.12|t=3.05 df=3|0.06|Integral|burst|Z>2 (slomo)|6|0.46|0.17|0.66|0.28|t=3.303 df=5|0.02|(Normalized)|Z<2 (non-slomo)|10|0.39|0.13|0.40|0.11|t=0.1362 df=9|0.89|WT|4|0.47|0.18|0.50|0.14|t=1.003 df=3|0.39|interburst|Z>2 (slomo)|6|1.27|0.85|3.41|2.89|t=2.38 df=5|0.06|Z<2 (non-slomo)|10|1.39|0.77|2.04|1.07|t=2.549 df=9|0.03|WT|4|1.50|1.09|1.60|0.93|t=0.3774 df=3|0.73|Saline|CNO|Paired, two-tailed t test|(alpha=0.05)|Swim|Sub-cohort (Z Swing Time)|N|Average|SD|Average|SD|t, df|p|Duration|burst (sec)|Z>2 (slomo)|6|0.06|0.012|0.07|0.0|t=1.95 df=5|0.11|Z<2 (non-slomo)|10|0.06|0.014|0.06|0.0|t=0.4518 df=9|0.66|WT|4|0.07|0.021|0.05|0.0|t=1.034 df=3|0.38|interburst (sec)|Z>2 (slomo)|6|0.11|0.017|0.14|0.0|t=2.313 df=5|0.07|Z<2 (non-slomo)|10|0.11|0.029|0.12|0.0|t=1.591 df=9|0.15|WT|4|0.11|0.024|0.11|0.0|t=0.06607 df=3|0.95|Saline|CNO|Wilcoxon two-tailed paired ranks test|Sub-cohort (Z Swing Time)|N|Median|Lower 95% CI|Upper 95% CI|Median|Lower 95% CI|Upper 95% CI|W|p|Frequency|(Hz)|Z>2 (slomo)|6|6.0|5.4|6.9|5.2|4.0|6.2|-21|0.03|Z<2 (non-slomo)|10|5.9|5.7|6.5|5.7|5.3|6.2|-33|0.11|WT
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 3673,4965p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g'
```

```
Supplementary Table 8|Gait metrics with saline versus CNO in VGluT2 subcohorts|with Figure 4|Footfall metrics|and Supplementary Figure 4|Group Z Swing Time<-3 (shuffle)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|with Figure 4|N = 15|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|10.42|2.03|7.05|2.60|t=3.777 df=14|0.002|Stride length (mm)|84.18 (2, 906)|<0.0001|Stride length (mm)|40.74|5.47|28.22|7.09|t=6.325 df=14|<0.0001|n Strides:|Swing time (s)|63.13 (2, 906)|<0.0001|Swing time (s)|0.11|0.02|0.07|0.02|t=11.87 df=14|<0.0001|saline n = 491|Stance time (s)|20.28 (4, 841)|<0.0001|Stance time (s)|0.36|0.06|0.43|0.12|t=1.978 df=14|0.07|CNO n = 631|Cadence (Hz)|49.5 (2, 886)|<0.0001|Cadence (Hz)|2.49|0.26|2.42|0.42|t=0.4978 df=14|0.63|Swing speed (cm/s)|176.9 (2, 1015)|<0.0001|Swing speed (cm/s)|40.19|6.62|38.57|7.56|t=0.812 df=14|0.43|Group -2>Z Swing Time >-3 (intermediate shuffle)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|N= 16|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|10.73|2.14|7.29|1.55|t=6.11 df=15|<0.0001|Stride length (mm)|26.67 (2, 1120)|<0.0001|Stride length (mm)|40.50|5.91|30.61|2.77|t=8.79 df=15|<0.0001|n Strides:|Swing time (s)|5.26 (2, 1120)|0.005|Swing time (s)|0.10|0.02|0.08|0.01|t=7.98 df=15|<0.0001|saline: n = 656|Stance time (s)|9.43 (4, 1148)|<0.0001|Stance time (s)|0.35|0.07|0.45|0.16|t=2.69 df=15|0.02|CNO: n = 675|Cadence (Hz)|11.16 (2, 1070)|<0.0001|Cadence (Hz)|2.61|0.37|2.34|0.48|t=2.10 df=15|0.05|Swing speed (cm/s)|80.38 (2, 1196)|<0.0001|Swing speed (cm/s)|42.57|4.63|38.21|5.15|t=6.28 df=15|<0.0001|with Supplementary Figure 4 Group Z Swing Time >-2 (non-shuffle)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|N = 14|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|12.32|3.82|8.90|3.06|t=3.612 df=13|0.003|Stride length (mm)|8.57 (2, 1009)|0.0002|Stride length (mm)|41.78|6.22|33.04|7.50|t=5.823 df=13|<0.0001|n Strides:|Swing time (s)|2.23 (2, 1009)|0.11|Swing time (s)|0.10|0.10|0.09|0.01|t=8.376 df=13|<0.0001|saline n = 575|
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 4965,6072p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g'
```

```
Supplementary Table 12|Gait metrics in the SerT cohort|with Figure 5|Footfall metrics|and Supplementary Figure 6|high Z Stride Velocity (faster)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|Figure 5|N= 6|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|11.37|2.24|15.61|1.84|t=8.82 df=5|0.0003|Stride length (mm)|0.00154 (2, 302)|1.00|Stride length (mm)|41.26|4.35|49.18|4.42|t=9.81 df=5|0.0002|n Strides:|Swing time (s)|2.206 (2, 302)|0.11|Swing time (s)|0.12|0.02|0.12|0.01|t=0.098 df=5|0.9255|saline: n = 236|Stance time (s)|0.7058 (4, 298)|0.59|Stance time (s)|0.31|0.05|0.23|0.04|t=6.17 df=5|0.0016|CNO: n = 223|Cadence (Hz)|0.001025 (2, 226)|1.00|Cadence (Hz)|2.72|0.35|3.10|0.17|t=3.03 df=5|0.03|Swing speed (mm)|5.577 (2, 427)|0.004|Swing speed (cm/s)|36.63|6.78|42.15|3.84|t=4.43 df=5|0.01|intermediate Z Stride Velocity|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|N= 6|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|11.97|2.14|12.71|2.31|t=1.5 df=5|0.19|Stride length (mm)|1.02 (2, 371)|0.36|Stride length (mm)|42.29|5.83|42.93|6.66|t=0.36 df=5|0.73|n Strides:|Swing time (s)|1.01 (2, 321)|0.36|Swing time (s)|0.12|0.02|0.12|0.02|t=0.31 df=5|0.77|saline: n = 229|Stance time (s)|1.73 (4, 367)|0.14|Stance time (s)|0.27|0.05|0.24|0.03|t=2.65 df=5|0.05|CNO: n = 251|Cadence (Hz)|1.61 (2, 271)|0.20|Cadence (Hz)|2.83|0.34|3.02|0.23|t=2.37 df=5|0.06|Swing speed (mm)|3.50 (2, 461)|0.03|Swing speed (cm/s)|36.48|4.43|36.16|3.92|t=0.34 df=5|0.75|Supplementary Figure 6 low Z Stride Velocity (slower)|F (DFn, DFd)|p|Average|SD|Average|SD|t(df)|p|N= 6|Stride velocity (cm/s)| -| -|Stride velocity (cm/s)|12.79|4.27|8.63|1.67|t=2.93 df=5|0.03|Stride length (mm)|2.94 (2, 369)|0.05|Stride length (mm)|43.46|5.61|36.32|4.01|t=3.95 df=5|0.01|n Strides:|Swing time (s)|1.972 (2, 369)|0.14|Swing time (s)|0.11|0.02|0.10|0.02|t=2.33 df=5|0.07|saline: n = 229|Stance time (s)|2.264 (4, 370)|0.06|Stance time (s)|0.29|0.11|0.39|0.04|t=2.89 df=5|0.03|CNO: n = 241|Cadence (Hz)|2.55 (2, 319)|0.08|Cad
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 6072,6930p 10.1101-2023.04.19.537568.txt | paste -sd'|' | sed 's/=== page/\n=== page/g'
```

```
Supplementary Table 15|Quantification of synaptophysin labeled boutons onto spinal profiles|With Supplementary Figure 15|Fig. 15 c Boutons in apposition to ChAT-IR motoneuron soma, dendrite or C bouton, per genotype|Ordinary One Way Anova|Sidak's multiple comparisons test|Mean Diff.|95.00% CI of diff.|Summary|Adjusted P Value|F (DFn, DFd)|P value|VGluT2 Soma vs. VGat Soma|-0.5|-26.80 to 25.80|ns|>0.9999|F (5, 30) = 14.69|<0.0001|VGluT2 Dendrite vs. VGaT Dendrite|0|-26.30 to 26.30|ns|>0.9999|VGluT2 C-bouton vs. VGaT C-bouton|28.5|2.195 to 54.80|*|0.03|VGluT2 Soma vs. VGluT2 Dendrite|-46.5|-72.80 to -20.20|****|<0.0001|VGluT2 Soma vs. VGluT2 C-bouton|-22.17|-48.47 to 4.138|ns|0.15|VGluT2 Dendrite vs. VGluT2 C-bouton|24.33|-1.971 to 50.64|ns|0.09|VGat Soma vs. VGaT Dendrite|-46|-72.30 to -19.70|***|0.0001|VGat Soma vs. VGaT C-bouton|6.833|-19.47 to 33.14|ns|0.995|VGaT Dendrite vs. VGaT C-bouton|52.83|26.53 to 79.14|****|<0.0001|Fig. 15 d Boutons in lamina IX (standardized volume)|Ordinary One Way Anova|Tukey's multiple comparisons test|Mean Diff.|95.00% CI of diff.|Summary|Adjusted P Value|F (DFn, DFd)|P value|VGluT2 rostral vs. VGluT2 intermediate|25.33|-10.26 to 60.93|ns|0.23|F (3, 23) = 10.70|0.0001|VGluT2 rostral vs. VGaT rostral|50|16.44 to 83.56|**|0.002|VGluT2 rostral vs. VGaT intermediate|6.333|-27.23 to 39.90|ns|0.95|VGluT intermediate vs. VGaT rostral|24.67|-1.867 to 51.20|ns|0.07|VGluT intermediate vs. VGaT intermediate|-19|-45.53 to 7.533|ns|0.22|VGaT rostral vs. VGaT intermediate|-43.67|-67.40 to -19.93|***|0.0002|Fig. 15 f Boutons in area X (standardized volume) |Kruskal-Wallis test|P value|Dunn's multiple comparisons test|Mean rank diff.|Summary|Adjusted P Value|KW 9.482|0.0009|VGluT2 rostral vs. VGluT2 intermediate|-1.667|ns|>0.9999|VGluT2 rostral vs. VGaT rostral|6.5|ns|0.16|VGluT2 rostral vs. VGaT intermediate|3.833|ns|>0.9999|VGluT intermediate vs. VGaT rostral|8.167|*|0.03|VGluT intermediate vs. VGaT intermediate|5.5|ns|0.37|VGaT rostral vs. VGaT in
[... 3 more lines not kept]
```

**Agent**

I've read the main text, Methods, legends and Tables S1–S18. Next, the linked code on SourceForge.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 60 "https://sourceforge.net/projects/gait-analysis-gui/files/" -o ga.html; echo $?; ls -la ga.html; grep -o 'href="[^"]*files/[^"]*"' ga.html | sort -u | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for p in "gait-analysis-gui/files/hsGUI/" "gait-analysis-gui/files/HTML%20version/" "gait-emg-step-trigger/files/"; do echo "== $p"; curl -sL -m 60 "https://sourceforge.net/projects/$p" | grep -oE 'title="[^"]+"[^>]*class="folder|<th scope="row"[^>]*headers="files_name_h"><a href="[^"]+"|"name": ?"[^"]+"|files_date_h[^<]*<abbr title="[^"]+"' | head -30; done; curl -sL -m 60 https://sourceforge.net/projects/gait-analysis-gui/ | grep -iE "last update|code|git|svn|commit" | head -10
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code; for u in "gait-analysis-gui/files/hsGUI/README.txt" "gait-analysis-gui/files/hsGUI/hsGUI.zip" "gait-emg-step-trigger/files/README.txt" "gait-emg-step-trigger/files/TAgateTimer.pls"; do f=$(echo $u | tr '/' '_'); curl -sL -m 120 "https://downloads.sourceforge.net/project/${u/files\//}" -o "$f"; file "$f"; done; ls -la; sha256sum *
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code; cat gait-analysis-gui_files_hsGUI_README.txt; echo; cat gait-emg-step-trigger_files_README.txt; python -c "
import zipfile;z=zipfile.ZipFile('gait-analysis-gui_files_hsGUI_hsGUI.zip');[print(i.filename,i.file_size) for i in z.infolist()];z.extractall('hs')"
```

```
hsGUI Package:

Software Platform: 
Matlab 2014a with image processing package

Software Authorship: 
This code was developed by BA Ellison and A Worley under supervision of V VanderHorst and compiled by A Kirby (4/2023).

Role in Research: 
This code was employed to extract gait metrics which were then used to validate analytical approaches to quantify changes in gait style through gait signatures. These analytical approaches can be found in:
1. Broom L, Ellison BA, Worley A, Wagenaar L, Sorberg E, Ashton C, et al. A translational approach to capture gait signatures of neurological disorders in mice and humans. Sci Rep. 2017;7(1):3225.
2. Broom L, Worley A, Gao F, Hernandez LD, Ashton CE, Shih LC, et al. Translational methods to detect asymmetries in temporal and spatial walking metrics in parkinsonian mouse models and human subjects with Parkinson’s disease. Sci Rep. 2019;9(2437).

Raw Data: 
This custom software package was written to display movies taken of mice walking on a plexiglass runway with a mirror at a 45 degree angle underneath. The video is captured with the animal walking horizontally on the plexiglass surface so that both the lateral view and the view from underneath the animal are captured simultaneously. The videos are captured at 120 frames per second and stored in .AVI format.

Software Description:
The program hs initiates a graphical interface to score bouts of gait that are pre-identified in the video. After starting the program, the user selects a video and then is prompted to enter time ranges that contain bouts of gait to be scored. The video load and initial frame displays for the purpose of spatial calibration. The user then manually indicates the long axis of the walkway, and locates points on the apparatus that are a fixed 5 cm distance apart. Once this preparation is complete, scoring begins. First, a subset of video frames corresponding to the first time range identified by the program is then loaded. The interface allows navigating 
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; cat getgait.m write2gp.m; cat arrangeGP.m | head -200
```

```
function [T]=getgait(group, condition, front, pool)
%GETGAIT generates a structure array containing the gait parameters STANCE
%DURATION, SWING DURATION, STRIDE LENGTH, CYCLE SPEED, STEP LENGTH, SPATIAL
%ALTERNATION, TEMPORAL ALTERNATION,
%
%GETGAIT(group,condition,side,pool) GROUP is a scalar or vector of numbers
%corresponding to the ID of an animal whose gait has been scored AND OUTPUT
%VIA THE MAT2CSV FUNCTION. Condition is a string matching the format used
%by mat2csv output function (e.g. 'saline1', 'CNO1001', etc.)
%
%Note: The expected file name follows the format:
%'output_csv\<AnimalID>\<AnimalID>-<Condition>.csv'.
%Any deviation in file name or location will cause data to be skipped.
%% establish indices
%These correspond to the 16 (pooled) or 19 (sided) pieces of information & their locations in the
%standard csv spreadsheet layout. Note the index lists will need to be
%updated if the format changes or if additional pieces of information are
%to be added.
startcol=[3 3 8 8 5 5 5 5 5 5 5 5 12 12 7 7 9 6 13]; %column to start reading from on each of the 19 rows
if front %list of rows from which to read (different for back vs front)
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; grep -n -i "speed\|swing\|stance\|strlen\|stride\|cadence\|talt\|phase" newpawsAnalyze.m mat2csv.m | head -80
```

```
newpawsAnalyze.m:155:    sp(end+1)=struct('StrLenBL',[],...
newpawsAnalyze.m:156:        'StrLenBR',[],...
newpawsAnalyze.m:157:        'StrLenFL',[],...
newpawsAnalyze.m:158:        'StrLenFR',[],...
newpawsAnalyze.m:191:        BL(z)=struct('v',zeros(1,size(sp(z).StrLenBL,2)),...
newpawsAnalyze.m:192:            'StrLen',sp(z).StrLenBL(1,:),...
newpawsAnalyze.m:193:            'dst',zeros(1,size(sp(z).StrLenBL,2)),...
newpawsAnalyze.m:194:            'dsw',zeros(1,size(sp(z).StrLenBL,2)),...
newpawsAnalyze.m:195:            'dcycle',zeros(1,size(sp(z).StrLenBL,2)),...
newpawsAnalyze.m:196:            'frSt',zeros(1,size(sp(z).StrLenBL,2))...
newpawsAnalyze.m:199:        BR(z)=struct('v',zeros(1,size(sp(z).StrLenBR,2)),...
newpawsAnalyze.m:200:            'StrLen',sp(z).StrLenBR(1,:),...
newpawsAnalyze.m:201:            'dst',zeros(1,size(sp(z).StrLenBR,2)),...
newpawsAnalyze.m:202:            'dsw',zeros(1,size(sp(z).StrLenBR,2)),...
newpawsAnalyze.m:203:            'dcycle',zeros(1,size(sp(z).StrLenBR,2)),...
newpawsAnalyze.m:204:            'frSt',zeros(1,size(sp(z).StrLenBR,2))...
newpawsAnalyze.m:207:        FL(z)=struct('v',zeros(1,size(sp(z).StrLenFL,2)),...
newpawsAnalyze.m:208:            'StrLen',sp(z).StrLenFL(1,:),...
newpawsAnalyze.m:209:            'dst',zeros(1,size(sp(z).StrLenFL,2)),...
newpawsAnalyze.m:210:            'dsw',zeros(1,size(sp(z).StrLenFL,2)),...
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; grep -n "function.*calcSpeed" -A40 newpawsAnalyze.m mat2csv.m | head -60; grep -n "120\|fps\|frame" newpawsAnalyze.m mat2csv.m | head
```

```
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; grep -rn "calcSpeed" . | head; grep -rln "function" . ; sed -n 1,60p mat2csv.m
```

```
./newpawsAnalyze.m:226:        [BL(a).v, BL(a).dst, BL(a).dsw, BL(a).dcycle, BL(a).frSt,err]=calcSpeed(sp(a).StrLenBL(1,:),paws(a).LeftBSwing,paws(a).LeftB,a,animalNum);
./newpawsAnalyze.m:228:        [BR(a).v, BR(a).dst, BR(a).dsw, BR(a).dcycle, BR(a).frSt,err]=calcSpeed(sp(a).StrLenBR(1,:),paws(a).RightBSwing,paws(a).RightB,a,animalNum);
./newpawsAnalyze.m:230:        [FL(a).v, FL(a).dst, FL(a).dsw, FL(a).dcycle, FL(a).frSt,err]=calcSpeed(sp(a).StrLenFL(1,:),paws(a).LeftFSwing,paws(a).LeftF,a,animalNum);
./newpawsAnalyze.m:232:        [FR(a).v, FR(a).dst, FR(a).dsw, FR(a).dcycle, FR(a).frSt,err]=calcSpeed(sp(a).StrLenFR(1,:),paws(a).RightFSwing,paws(a).RightF,a,animalNum);
./getgait.m
./arrangeGP.m
./newpawsAnalyze.m
./GUI/scripts/videoCalibrate.m
./GUI/scripts/hsFrameList2.m
./GUI/scripts/hsGUI.m
./GUI/scripts/uicomponent.m
./mat2csv.m
./write2gp.m
./dateLookup2.m
function mat2csv(animal,conditionarray,varargin)
global conditions filename cueingType ID
for i = 1:length(animal)
    animalNum = animal(i);
    ID = num2str(animal(i));
    disp(ID);
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; sed -n 130,260p mat2csv.m
```

```
end
                writefunc(cl,sp,timing,coup,FILE);
            end
        end
    end
    fclose all;
end
end
%% print
%%%Print to CSV
function writefunc(cl,sp,timing,coup,fid)
global conditions filename cueingType ID
fprintf(fid,'%s \n',cueingType);
if    size(sp(end).StrLenBL,2) < 3 ||...
        size(sp(end).StrLenBR,2) < 3 ||...
        size(sp(end).StrLenFL,2) < 3 ||...
        size(sp(end).StrLenFR,2) < 3 ||...
        any(cellfun(@isempty,struct2cell(coup)))
    fprintf(2,['********NOT ENOUGH Steps. SKIPPED:  ',...
        ID,' ',conditions,' ',cueingType...
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; grep -n "coup\|Talt\|phase" newpawsAnalyze.m | head -20; sed -n 236,300p newpawsAnalyze.m; head -40 $TMPDIR/code/gait-emg-step-trigger_files_TAgateTimer.pls
```

```
1:function [cl,sp,timing,coup]=newpawsAnalyze(npaws,cue)
5:coup = [];
252:    coup=struct('BlBr',zeros(1,size(BL(1).frSt,2)-1),...
268:    coup.BlBr=calcTimeCoupling(BL,BR);
271:    coup.BrBl=calcTimeCoupling(BR,BL);
274:    coup.FlFr=calcTimeCoupling(FL,FR);
277:    coup.FrFl=calcTimeCoupling(FR,FL);
280:    coup.BlFl=calcTimeCoupling(BL,FL);
283:    coup.FlBl=calcTimeCoupling(FL,BL);
286:    coup.BrFr=calcTimeCoupling(BR,FR);
289:    coup.FrBr=calcTimeCoupling(FR,BR);
292:    coup.BlFr=calcTimeCoupling(BL,FR);
295:    coup.FrBl=calcTimeCoupling(FR,BL);
298:    coup.BrFl=calcTimeCoupling(BR,FL);
301:    coup.FlBr=calcTimeCoupling(FL,BR);
    
    trialDurations(a)=(max([paws(a).LeftB(:,3)' paws(a).LeftF(:,3)' paws(a).RightB(:,3)' paws(a).RightF(:,3)' ]) - ...
        min([paws(a).LeftB(:,3)' paws(a).LeftF(:,3)' paws(a).RightB(:,3)' paws(a).RightF(:,3)' ]))/119.88 ;
    
    %these vectors now contain the speeds, stride lengths, swing, stance and
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/hs/hsGUI/hsGUI_programfiles; grep -rn "^ *function" --include=*.m . | grep -v uicomponent | cut -c1-150
```

```
./getgait.m:1:function [T]=getgait(group, condition, front, pool)
./arrangeGP.m:1:function [Array,mArray,measures,stepcts,ec] = arrangeGP(animals,conditions,front)
./newpawsAnalyze.m:1:function [cl,sp,timing,coup]=newpawsAnalyze(npaws,cue)
./GUI/scripts/videoCalibrate.m:1:function [c mEdge]=videoCalibrate
./GUI/scripts/videoCalibrate.m:135:function wbmf                               % window motion callback function to draw the rubber line
./GUI/scripts/videoCalibrate.m:148:function deleteobj(no_use1,no_use2)         % this uicontrol callback does Not Use inputs
./GUI/scripts/videoCalibrate.m:157:function storecoord(result)
./GUI/scripts/hsFrameList2.m:1:function varargout = hsFrameList2(varargin)
./GUI/scripts/hsFrameList2.m:48:function hsFrameList2_OpeningFcn(hObject, eventdata, handles, varargin)
./GUI/scripts/hsFrameList2.m:71:function varargout = hsFrameList2_OutputFcn(hObject, eventdata, handles) 
./GUI/scripts/hsFrameList2.m:84:function pushDone_Callback(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:169:function edit1_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:185:function edit2_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:200:function edit3_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:214:function edit4_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:229:function edit5_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:245:function edit6_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:261:function edit7_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:277:function edit8_CreateFcn(hObject, eventdata, handles)
./GUI/scripts/hsFrameList2.m:288:function edit9_CreateFcn(hObject, eventdata, handles)
[... 86 more lines not kept]
```

**Agent**

I have everything I need: the text, Tables S1–S18, and the code (MATLAB stride scoring and metric export, plus a Spike2 trigger script, with no statistics in either). Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/code; sed -n 60,140p hs/hsGUI/hsGUI_programfiles/mat2csv.m | grep -n "newpawsAnalyze\|cue\|Cued" | head; grep -n "119.88\|/119\|120" hs/hsGUI/hsGUI_programfiles/*.m | head
```

```
19:        %             [cl,sp,timing,coup] = newpawsAnalyze(pawsC);
21:        %             cueingType = 'All Trials';
24:        %                     ID,' ',conditions,' ',cueingType...
36:                        [cl,sp,timing,coup]=newpawsAnalyze(pawsC);
37:                        cueingType = 'All Trials';
40:                                ID,' ',conditions,' ',cueingType...
45:                        [cl,sp,timing,coup] = newpawsAnalyze(pawsC,1);
46:                        cueingType = 'NO Cueing';
49:                                ID,' ',conditions,' ',cueingType...
54:                        [cl,sp,timing,coup] = newpawsAnalyze(pawsC,2);
hs/hsGUI/hsGUI_programfiles/newpawsAnalyze.m:238:        min([paws(a).LeftB(:,3)' paws(a).LeftF(:,3)' paws(a).RightB(:,3)' paws(a).RightF(:,3)' ]))/119.88 ;
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/002010/10.1101-2023.04.19.537568.yaml",
 "content": "# Claims for VanderHorst and colleagues, \"Contrasting walking styles map to discrete neural\n# substrates in the mouse brainstem\" (bioRxiv doi:10.1101/2023.04.19.537568), on dandiset 002010.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 (docs/protocol.md, Reader).\n#\n# Text read: the bioRxiv preprint, version 1, from its JATS XML (main text, Methods, figure\n# legends, figure supplement legends), with the two supplement PDFs extracted to text: the\n# supplementary figures (media-1.pdf) and Supplementary Tables S1 to S18 (media-2.pdf). All in\n# paper/10.1101-2023.04.19.537568.txt. No PDF of the main text. The Methods equation for the\n# gait Z-scores (Methods, Behavioral and electrophysiological data analyses, a) is missing from\n# the text: the sentence \"Z-scores of the change in gait metrics were then calculated as\n# follows:\" runs on with no formula. Its readings are named in claim zscore-subgroups.\n# The legend of Figure 7-Figure supplement 3 is complete in the supplementary figures PDF.\n#\n# Code read: the two SourceForge projects the Code availability statement links, files dated\n# 2023-04-14 (SourceForge has no commit for them; sha256 of the archives read below).\n#   gait-analysis-gui, hsGUI/hsGUI.zip (sha256 a2d61d8d995232e2af04e63d137cc95de07b28daeb16a674610b20b494d5834c)\n#     MATLAB GUI (hs.m, hsGUI.m) to mark footfalls (stance onset, swing onset, paw position) in\n#     120 fps walkway videos; mat2csv.m and newpawsAnalyze.m turn the marks into per-stride\n#     speed, stride length, stance, swing and cycle duration and interlimb temporal coupling\n#     (the frame rate used is 119.88 fps); trials with fewer than 3 strides in any limb are\n#     skipped; write2gp.m and arrangeGP.m export per-stride values and per-mouse means for\n#     GraphPad, with columns for stance, 1 - log10(stance), swing, stride length, stride\n#     frequency (speed / stride length) and swing speed (stride length / swing). The helper\n#     functions calcSpeed and calcTimeCoupling are called but not in the archive.\n#   gait-emg-step-trigger, TAgateTimer.pls (sha256 b8694e738a92ba7ea6fd44d36e88437625ac192189ce4a61d7efc33309d693b8)\n#     Spike2 sequencer script that detects TA EMG bursts by threshold and delivers 1 or 2\n#     optogenetic pulses (default 20 ms apart).\n# Neither holds the statistics, the Z-scores, the regression models or the EMG analysis, which\n# the Methods say were done in GraphPad Prism 7, custom MATLAB scripts and Spike2 8.03b.\n#\n# Data the paper used, as it reports them:\n#   Chemogenetic cohorts (AAV8-DIO-hM3Dq-mCherry into the medial pontomedullary reticular\n#   formation, mRF; median 35 nl, uni- or bilateral): 35 male VGaT-ires-cre and 10 WT littermates;\n#   46 VGluT2-ires-cre and 7 WT littermates; 18 SerT-cre and 15 WT littermates. Each mouse is its\n#   own control: at least 2 saline and 2 CNO (0.3 mg/kg i.p.) sessions, tested 45 min to 2.5 h\n#   after injection, on non-consecutive days, in the order rotarod, gait, beam, ladder.\n#   Gait: 120 fps video of the middle 40 cm of a 120 x 8 cm walkway with a mirror below; at least\n#   4 valid trials per session (at least 4 consecutive strides per limb); per stride: stride\n#   velocity, swing and stance time, stride length, cadence, swing speed, interlimb coupling;\n#   about 35 to 42 hindlimb strides per mouse per session. Postural heights of iliac crest and\n#   tail base at start and end of swing from marked video frames.\n#   Motor tests: rotarod latency to fall (3 trials per session), beam and horizontal ladder\n#   slips and misses (2 trials per session).\n#   EMG (subset): TA and gastrocnemius (G), some gluteal, quadriceps, biceps femoris, triceps;\n#   10 kHz; walking and swimming; 20 cycles per mouse per condition; analysed groups n=6 VGaT\n#   Z>2, 10 VGaT Z<2, 7 VGluT2 Z<-2, 6 VGluT2 Z>-2, 5 SerT Z>0, 3 SerT Z<0, 4 VGaT WT, 7 SerT WT.\n#   Sensory screen (VGaT subset and WT): von Frey 0.4 to 2 g, 10 applications each; pinprick\n#   time; hotplate 55 C latency.\n#   Optogenetics: 10 VGaT-ires-cre mice with ChR2 and a midline fiber; 4 with 2 to 5 s trains\n#   (20 Hz, 5 ms) during walkway gait; 6 with TA and G EMG and EMG-triggered single or double\n#   5 ms pulses.\n#   Histology and tracing: transfection site reconstructions at 320 um intervals; CTb retrograde\n#   tracing (8 WT mice for reticulospinal maps; 6 VGaT, 6 VGluT2, 6 SerT after behaviour);\n#   synaptophysin-mCherry anterograde tracing (6 VGaT, 6 VGluT2); confocal bouton counts in 6\n#   lumbar regions of 10 VGaT hM3Dq mice (3 sections each).\n#\n# Method choices fixed here from the paper, used by many claims:\n#   Subgroups are defined by Z-scores of each mouse's change from saline to CNO (claim\n#   zscore-subgroups, which names the readings of the missing formula). VGaT and VGluT2 groups\n#   use hindlimb swing time (Z SwT), SerT groups stride velocity (Z StrV). Thresholds as the\n#   paper and its tables give them: VGaT Z>3 slomo, 3>Z>2 intermediate, Z<2 non-slomo, and Z>2\n#   against Z<2 for EMG, bouton and sensory analyses; VGluT2 Z<-3 shuffle, -3<Z<-2 intermediate,\n#   Z>-2 non-shuffle, and Z<-2 against Z>-2 for EMG; SerT high, intermediate and low thirds of\n#   ranked Z StrV (6 mice each in Tables S12 and S14) for gait and motor tests, Z>0 against Z<0\n#   for EMG (Methods, d).\n#   Walking signatures (Methods, b): per subgroup, hindlimb strides of all its mice pooled per\n#   condition, strides with velocity 3 to 16 cm/s, each metric against stride velocity (stride\n#   length also against swing speed), fitted with the metric's model, and saline against CNO by\n#   the extra sum of squares F test at alpha 0.001. The paper names no model, citing its\n#   reference 36; Tables S3, S8 and S12 give numerator degrees of freedom of 2 for stride\n#   length, swing time, cadence and swing speed and 4 for stance time, so the models have 2 and 4\n#   parameters. Readings for the 2-parameter models are (a) a straight line, (b) a power law\n#   (straight line in log-log), (c) a straight line against log10 velocity; for the 4-parameter\n#   stance model, (a) a third-order polynomial, (b) a four-parameter logistic, each fitted to\n#   stance as such or to 1 - log10(stance), the transform the paper's write2gp/arrangeGP export\n#   provides. A signature claim is decided only when all readings give the same outcome.\n#   Per-mouse averages (bar graphs, paired two-tailed t-tests at alpha 0.05) use all strides,\n#   not restricted to the walking range (\"Bar graphs of averaged data that was not corrected for\n#   speed\", Figure 3 legend).\n#   Tolerances: 10% of the reported value. The tables also give SDs, but they are the spread\n#   between mice, not an uncertainty of the mean, and the means here are of the same mice.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"002010\"\npaper: doi:10.1101/2023.04.19.537568\nclaims:\n- id: zscore-subgroups\n  statement: Z-scores of each mouse's change in hindlimb swing time between saline and CNO,\n    relative to WT littermates, separate slomo (extreme positive Z SwT, VGaT cohort) and shuffle\n    (extreme negative Z SwT, VGluT2 cohort) mice from mice whose walking is normal; the\n    resulting subgroups hold 9 (Z>3), 5 (3>Z>2) and 21 (Z<2) VGaT mice and 15 (Z<-3), 16\n    (-3<Z<-2) and 14 (Z>-2) VGluT2 mice.\n  source: Results, Chemogenetic mRF modulation elicited different walking styles, paragraph 3;\n    Figure 2c and 2d; group sizes in Tables S3 and S8\n  quote: we employed Z-scores for hindlimb swing time (time a limb is off the ground; Z SwT ) and\n    stride velocity (Z StrV ) that for each mouse reflected the change between its baseline and\n    CNO conditions relative to variation in WT littermates. Scatterplots of these scores ( Fig. 2c\n    ) revealed that slomo and shuffle styles were distinct from normal walking based upon extreme\n    values of Z SwT , positive for slomo style and negative for shuffle style\n  expected:\n  - quantity: VGaT-ires-cre mice with Z SwT > 3 (slomo)\n    value: 9\n    tolerance: 0.9\n  - quantity: VGaT-ires-cre mice with 3 > Z SwT > 2 (intermediate)\n    value: 5\n    tolerance: 0.5\n  - quantity: VGaT-ires-cre mice with Z SwT < 2 (non-slomo)\n    value: 21\n    tolerance: 2.1\n  - quantity: VGluT2-ires-cre mice with Z SwT < -3 (shuffle)\n    value: 15\n    tolerance: 1.5\n  - quantity: VGluT2-ires-cre mice with -3 < Z SwT < -2 (intermediate)\n    value: 16\n    tolerance: 1.6\n  - quantity: VGluT2-ires-cre mice with Z SwT > -2 (non-shuffle)\n    value: 14\n    tolerance: 1.4\n  criterion: The Methods (Behavioral and electrophysiological data analyses, a) say the Z-score\n    is based on each animal's difference between baseline and CNO, that differences between\n    conditions in the corresponding WT group defined the population averages, and the Results\n    say relative to variation in WT littermates; the formula itself is missing from the text.\n    Per mouse, the hindlimb swing time (or, for SerT, stride velocity) is averaged over all\n    strides of each condition (both hindlimbs pooled, as the paper's getgait.m does with pool\n    set). Readings of the Z-score, all with WT littermates of the same cohort as reference\n    (VGaT 10, VGluT2 7, SerT 15) and the sample SD (a standard choice), are (a) Z = (d - mean\n    of WT d) / SD of WT d, with d = CNO mean minus saline mean; (b) the same with d as the\n    relative change (CNO - saline) / saline. A second open detail is whether the condition\n    mean pools all strides of the 2 or more sessions or averages session means; both are run.\n    Reproduced when, under one reading, the VGaT Z SwT values have a positive tail and the\n    VGluT2 values a negative tail beyond the range of their WT littermates and the six group\n    counts are within tolerance. The 46 VGluT2 mice of Table S2 against 45 in Table S8 are\n    reported; the Methods exclude one mouse whose transfection site lay far outside the area of\n    interest. The subgroups formed under the matching reading are those used by the claims that\n    depend on this one; when several readings match, each is carried forward.\n- id: fig2b-slower-vgat-vglut2\n  statement: CNO decreased average stride velocity in the VGaT-ires-cre cohort (11.5 to 8.5 cm/s)\n    and in the VGluT2-ires-cre cohort (11.1 to 7.7 cm/s).\n  source: Figure 2b; Results, Chemogenetic mRF modulation elicited different walking styles,\n    paragraph 2; Table S2\n  quote: We found that mRF activation decreased speed in both VGaT and VGluT2 cohorts ( Fig. 2b ;\n    Table S2)\n  statistics:\n  - about: VGaT-ires-cre, saline against CNO\n    test: paired, 2 tailed t-test\n    statistic: t=4.965 df=34\n    p: 0.0001\n    p_relation: \"<\"\n    n: 35 VGaT-ires-cre mice\n  - about: VGluT2-ires-cre, saline against CNO\n    test: paired, 2 tailed t-test\n    statistic: t=6.657 df=45\n    p: 0.0001\n    p_relation: \"<\"\n    n: 46 VGluT2-ires-cre mice\n  expected:\n  - quantity: VGaT-ires-cre mean stride velocity, saline\n    value: 11.5\n    tolerance: 1.15\n    unit: cm/s\n  - quantity: VGaT-ires-cre mean stride velocity, CNO\n    value: 8.5\n    tolerance: 0.85\n    unit: cm/s\n  - quantity: VGluT2-ires-cre mean stride velocity, saline\n    value: 11.1\n    tolerance: 1.11\n    unit: cm/s\n  - quantity: VGluT2-ires-cre mean stride velocity, CNO\n    value: 7.7\n    tolerance: 0.77\n    unit: cm/s\n  criterion: Per mouse, the mean hindlimb stride velocity over all strides of each condition;\n    paired two-tailed t-test across mice (Figure 2b legend, Table S2). Reproduced when both\n    cohorts give p < 0.05 with CNO lower and the four means are within tolerance.\n- id: fig2b-controls-no-velocity-change\n  statement: CNO did not change average stride velocity in the WT littermates of the VGaT and\n    VGluT2 cohorts.\n  source: Figure 2b legend; Table S2\n  quote: Average stride velocity decreased following hM3Dq activation in experimental VGaT and\n    VGluT2 cohorts, but not their controls (2-tailed paired t-test; Table S2\n  statistics:\n  - about: VGaT WT littermates\n    test: paired, 2 tailed t-test\n    statistic: t=0.6937 df=9\n    p: 0.51\n    n: 10 WT mice\n  - about: VGluT2 WT littermates\n    test: paired, 2 tailed t-test\n    statistic: t=1.518 df=6\n    p: 0.18\n    n: 7 WT mice\n  criterion: A claim of absence, judged on the paper's test, the paired two-tailed t-test on\n    per-mouse mean stride velocity at alpha 0.05 (Figure 2b legend). Reproduced when neither WT\n    group gives p < 0.05; the mean change is reported either way.\n- id: fig2b-sert-no-velocity-change\n  statement: At the group level CNO did not change average stride velocity in SerT-cre mice\n    (12.0 against 12.3 cm/s) or their WT littermates.\n  source: Results, Chemogenetic mRF modulation elicited different walking styles, paragraph 3;\n    Table S2\n  quote: In contrast, activation of SerT neurons did not reveal an unusual style and did not\n    change group-wise average stride velocity\n  statistics:\n  - about: SerT-cre mice\n    test: paired, 2 tailed t-test\n    statistic: t=0.2782 df=17\n    p: 0.78\n    n: 18 SerT-cre mice\n  - about: SerT WT littermates\n    test: paired, 2 tailed t-test\n    statistic: t=0.005928 df=14\n    p: 1.0\n    n: 15 WT mice\n  criterion: A claim of absence, judged on the paper's test, the paired two-tailed t-test on\n    per-mouse mean stride velocity at alpha 0.05 (Table S2). Reproduced when neither group gives\n    p < 0.05; the means are reported either way.\n- id: fig2c-sert-subset-faster\n  statement: In a subset of SerT-cre mice CNO increased stride velocity; in the third with the\n    highest Z StrV, mean stride velocity rose from 11.37 to 15.61 cm/s.\n  source: Results, Chemogenetic mRF modulation elicited different walking styles, paragraph 3;\n    Figure 2c; Table S12 (high Z stride velocity group)\n  quote: However, in a subset of mice stride velocity (Z StrV ) increased\n  statistics:\n  - test: paired, 2 tailed t-test\n    statistic: t=8.82 df=5\n    p: 0.0003\n    n: 6 SerT-cre mice with the highest Z StrV\n  expected:\n  - quantity: high Z StrV group mean stride velocity, saline\n    value: 11.37\n    tolerance: 1.14\n    unit: cm/s\n  - quantity: high Z StrV group mean stride velocity, CNO\n    value: 15.61\n    tolerance: 1.56\n    unit: cm/s\n  depends_on:\n  - zscore-subgroups\n  criterion: The 18 SerT-cre mice ranked by Z StrV and split into thirds of 6 (Table S12); paired\n    two-tailed t-test on per-mouse mean stride velocity in the top third. Reproduced when p <\n    0.05 with CNO faster and both means are within tolerance.\n- id: wt-gait-unperturbed\n  statement: In WT littermates of all three cohorts CNO changed neither stride velocity nor the\n    walking signatures.\n  source: Results, Chemogenetic mRF modulation elicited different walking styles, paragraph 3;\n    Results, Slomo walking is defined by upward shifts in select gait signatures, paragraph 2;\n    Tables S3, S8 and S12 (WT control)\n  quote: In WT controls, CNO did not perturb gait metrics\n  statistics:\n  - about: VGaT WT, swing time signature (smallest signature p among VGaT WT metrics is cadence, 0.04)\n    test: sum of squares F test\n    statistic: F (2, 547) = 3.00\n    p: 0.05\n    n: 10 WT mice, 363 saline and 346 CNO strides\n  - about: VGluT2 WT, stance time signature (smallest signature p among VGluT2 WT metrics)\n    test: sum of squares F test\n    statistic: F (4, 248) = 2.56\n    p: 0.04\n    n: 6 WT mice, 160 saline and 160 CNO strides\n  - about: SerT WT, swing speed signature (smallest signature p among SerT WT metrics)\n    test: sum of squares F test\n    statistic: F (2, 1114) = 3.5\n    p: 0.03\n    n: 15 WT mice, 567 saline and 604 CNO strides\n  criterion: A claim of absence, judged on the paper's tests. For each WT group, every walking\n    signature (stride length, swing time, stance time, cadence against stride velocity, and\n    stride length against swing speed) by the extra sum of squares F test at alpha 0.001, and\n    per-mouse mean stride velocity by the paired two-tailed t-test at alpha 0.05 (Methods, b;\n    Tables S3, S8, S12). Reproduced when no signature test gives p < 0.001 and no velocity test\n    gives p < 0.05 in any WT group, under every model reading; the F statistics are reported\n    either way. The VGluT2 WT stride length t-test (p 0.03 in Table S8) and the SerT WT Watson\n    test (p 0.02 in Table S12) are shown as they stand.\n  depends_on:\n  - zscore-subgroups\n- id: fig3b-slomo-swing-time-shift\n  statement: In the VGaT Z SwT > 3 (slomo) group CNO shifted the swing time signature upward,\n    swing time increasing beyond what the slower speed explains.\n  source: Figure 3b; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: As expected, swing time increased with an upward signature shift between baseline and CNO\n  statistics:\n  - test: sum of squares F test\n    statistic: F (2, 479) = 160.1\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice, 320 saline and 313 CNO hindlimb strides\n  depends_on:\n  - zscore-subgroups\n  criterion: Walking signature test as fixed in the opening comment, swing time against stride\n    velocity in the slomo group. Reproduced when p < 0.001 and the CNO curve lies above the\n    saline curve over the shared velocity range, under every model reading.\n- id: fig3b-slomo-stance-no-shift\n  statement: In the slomo group stance time increased with CNO, but in proportion to the\n    decreased stride velocity, without a signature shift.\n  source: Figure 3b; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: In contrast, while stance time increased, it did so in proportion to decreased stride\n    velocity (no shift)\n  statistics:\n  - test: sum of squares F test\n    statistic: F (4, 519) = 2.83\n    p: 0.02\n    n: 9 mice, 320 saline and 313 CNO hindlimb strides\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the extra sum of squares F test of\n    stance time against stride velocity at alpha 0.001 (Methods, b; Figure 3 legend). Reproduced\n    when p >= 0.001 under the stance model readings named in the opening comment; not\n    reproduced when p < 0.001 under any reading used for the main result (each reading's F is\n    shown). The per-mouse stance increase (0.43 to 0.83 s, t-test p 0.0009, Table S3) is\n    reported.\n- id: fig3b-slomo-stride-length-shift\n  statement: In the slomo group stride length was longer than expected for the slower speed (a\n    signature shift).\n  source: Figure 3b; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: Stride length was significantly longer than expected for speed (shift)\n  statistics:\n  - test: sum of squares F test\n    statistic: F (2, 479) = 44.7\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice, 320 saline and 313 CNO hindlimb strides\n  depends_on:\n  - zscore-subgroups\n  criterion: Walking signature test, stride length against stride velocity. Reproduced when p <\n    0.001 and the CNO curve lies above the saline curve over the shared velocity range, under\n    every model reading.\n- id: fig3c-slomo-cadence-shift\n  statement: In the slomo group stride frequency (cadence) decreased out of proportion to the\n    slowed speed.\n  source: Figure 3c; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: Stride frequency, derived from swing and stance time, decreased out of proportion to\n    slowed speed, driven by increased swing time\n  statistics:\n  - test: sum of squares F test\n    statistic: F (2, 548) = 24.27\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice, 320 saline and 313 CNO hindlimb strides\n  depends_on:\n  - zscore-subgroups\n  criterion: Walking signature test, cadence (1 / (stance + swing), Methods, b) against stride\n    velocity. Reproduced when p < 0.001 and the CNO curve lies below the saline curve over the\n    shared velocity range, under every model reading.\n- id: fig3c-slomo-coupling-unchanged\n  statement: In the slomo group left-right temporal coupling of the hindlimbs did not change with\n    CNO.\n  source: Figure 3c ii; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3 (temporal coupling)\n  quote: Temporal coupling of the hindlimbs did not change, as shown by polar plots ( Fig. 3c ii ),\n    in line with preserved footfall patterns\n  statistics:\n  - test: Watson-Williams test\n    p: 0.62\n    n: 9 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the Watson-Williams test of back\n    left against back right phase, saline against CNO, for strides of 3 to 16 cm/s, at alpha\n    0.05 (Methods, b; Figure 3 legend). The phase computation (calcTimeCoupling) is not in the\n    code archive; the reading used is the standard one, the lag of the right hindlimb's stance\n    onset after the left's divided by the left's cycle duration, as an angle. Reproduced when p\n    >= 0.05. The mean resultant lengths (0.59 saline, 0.79 CNO) are reported.\n- id: fig3d-slomo-swing-speed-shift\n  statement: In the slomo group swing speed decreased for a given stride length.\n  source: Figure 3d; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: In the Z SwT >3 ( slomo ) group ( Fig. 3d ), but not the non-slomo group (Figure\n    3-Figure supplement 1), swing speed decreased for a given stride length\n  statistics:\n  - about: slomo group, stride length against swing speed\n    test: sum of squares F test\n    statistic: F (2, 522) = 42.4\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice\n  - about: non-slomo group, stride length against swing speed\n    test: sum of squares F test\n    statistic: F (2, 1229) = 0.34\n    p: 0.71\n    n: 21 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Walking signature test of stride length against swing speed (stride length /\n    swing time), in the 3 to 16 cm/s stride velocity range. Reproduced when the slomo group\n    gives p < 0.001 with lower swing speed for a given stride length under CNO, and the\n    non-slomo group gives p >= 0.001, under every model reading.\n- id: fig3-slomo-averages\n  statement: Per-mouse averages in the slomo group change consistently across mice with CNO;\n    stride velocity falls from 9.91 to 5.67 cm/s, swing time rises from 0.10 to 0.16 s, cadence\n    falls from 2.35 to 1.38 Hz and swing speed from 41.69 to 26.63 cm/s, while average stride\n    length does not change.\n  source: Figure 3b-d inserts; Results, Slomo walking is defined by upward shifts in select gait\n    signatures, paragraph 2; Table S3\n  quote: Averaged gait metrics of each mouse, which represent data irrespective of changing speed,\n    showed that changes were homogeneous within subgroup\n  statistics:\n  - about: stride velocity\n    test: paired, 2 tailed t-test\n    statistic: t=3.33 df=8\n    p: 0.01\n    n: 9 mice\n  - about: swing time\n    test: paired, 2 tailed t-test\n    statistic: t=11.88 df=8\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice\n  - about: cadence\n    test: paired, 2 tailed t-test\n    statistic: t=6.89 df=8\n    p: 0.0001\n    n: 9 mice\n  - about: swing speed\n    test: paired, 2 tailed t-test\n    statistic: t=8.07 df=8\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice\n  - about: stride length\n    test: paired, 2 tailed t-test\n    statistic: t=0.09 df=8\n    p: 0.93\n    n: 9 mice\n  expected:\n  - quantity: mean stride velocity, saline\n    value: 9.91\n    tolerance: 0.99\n    unit: cm/s\n  - quantity: mean stride velocity, CNO\n    value: 5.67\n    tolerance: 0.57\n    unit: cm/s\n  - quantity: mean swing time, saline\n    value: 0.10\n    tolerance: 0.01\n    unit: s\n  - quantity: mean swing time, CNO\n    value: 0.16\n    tolerance: 0.016\n    unit: s\n  - quantity: mean cadence, saline\n    value: 2.35\n    tolerance: 0.235\n    unit: Hz\n  - quantity: mean cadence, CNO\n    value: 1.38\n    tolerance: 0.138\n    unit: Hz\n  - quantity: mean swing speed, saline\n    value: 41.69\n    tolerance: 4.17\n    unit: cm/s\n  - quantity: mean swing speed, CNO\n    value: 26.63\n    tolerance: 2.66\n    unit: cm/s\n  depends_on:\n  - zscore-subgroups\n  criterion: Per-mouse means over all strides of each condition, paired two-tailed t-tests at\n    alpha 0.05 (Figure 3 legend). Reproduced when velocity, swing time, cadence and swing speed\n    each give p < 0.05 in the stated direction, stride length gives p >= 0.05, and the means are\n    within tolerance. Cadence is taken per stride as 1 / (stance + swing) (Methods, b) and as\n    stride velocity / stride length (the column the paper's arrangeGP.m exports); both are\n    shown.\n- id: tables3-intermediate-slomo-reproduced\n  statement: The slomo signature shifts were reproduced in the milder VGaT subgroup with 2 < Z\n    SwT < 3.\n  source: Results, Slomo walking is defined by upward shifts in select gait signatures,\n    paragraph 2; Table S3 (intermediate slomo group)\n  quote: We reproduced these results in the mild subgroup (2<Z SwT <3; Table S3)\n  statistics:\n  - about: swing time signature\n    test: sum of squares F test\n    statistic: F (2, 260) = 41.56\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5 mice, 186 saline and 170 CNO strides\n  - about: stride length signature\n    test: sum of squares F test\n    statistic: F (2, 260) = 38.84\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5 mice\n  - about: cadence signature\n    test: sum of squares F test\n    statistic: F (2, 225) = 21.21\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5 mice\n  - about: swing speed signature\n    test: sum of squares F test\n    statistic: F (2, 322) = 31.18\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: The walking signature tests of the slomo claims, run in the 3 > Z SwT > 2 group.\n    Reproduced when swing time, stride length and swing speed (against stride length) shift in\n    the slomo direction and cadence shifts down, each at p < 0.001, under every model reading.\n    Table S3 also gives a stance time shift in this group (F (4, 252) = 5.171, p 0.0005), which\n    differs from the slomo group; the stance result is reported but not part of the criterion,\n    as the text names no stance result for this group.\n- id: figs3-1-nonslomo-no-shift\n  statement: In the VGaT Z SwT < 2 (non-slomo) group stride velocity decreased with CNO, but gait\n    metrics followed normal speed-dependent rules without signature shifts.\n  source: Figure 3-Figure supplement 1; Results, Slomo walking is defined by upward shifts in\n    select gait signatures, paragraph 2; Table S3 (non-slomo group)\n  quote: In contrast, in the Z SwT <2 ( non-slomo ) group, stride velocity decreased, but gait\n    metrics followed normal speed-dependent rules without signature shifts\n  statistics:\n  - about: stride velocity, per-mouse means\n    test: paired, 2 tailed t-test\n    statistic: t=2.49 df=20\n    p: 0.02\n    n: 21 mice\n  - about: swing time signature (smallest signature p in this group)\n    test: sum of squares F test\n    statistic: F (2, 1012) = 3.91\n    p: 0.02\n    n: 21 mice, 671 saline and 731 CNO strides\n  depends_on:\n  - zscore-subgroups\n  criterion: Velocity by the paired two-tailed t-test at alpha 0.05; the absence of shifts is\n    judged on the paper's test, the extra sum of squares F test at alpha 0.001 for stride\n    length, swing time, stance time, cadence and swing speed. Reproduced when velocity\n    decreases with p < 0.05 and no signature test gives p < 0.001 under any model reading; the\n    F statistics are reported either way.\n- id: fig3d-posture-not-slomo-specific\n  statement: At the start of the swing phase the tail base, and less so the iliac crest, were\n    carried higher with CNO in both the slomo and the non-slomo VGaT groups, so these postural\n    changes are not specific to slomo gait.\n  source: Figure 3d; Figure 3-Figure supplement 1; Results, Slomo walking is defined by upward\n    shifts in select gait signatures, paragraph 2; Table S3 (postural metrics)\n  quote: At the start of the swing phase the base of the tail and less so iliac crest were carried\n    higher following VGaT hM3Dq activation than at baseline in both slomo and Z SwT <2 (\n    non-slomo ) sub-cohorts\n  statistics:\n  - about: tail base height at start of swing, slomo\n    test: paired, 2 tailed t-test\n    statistic: t=8.571 df=8\n    p: 0.0001\n    p_relation: \"<\"\n    n: 9 mice\n  - about: iliac crest height at start of swing, slomo\n    test: paired, 2 tailed t-test\n    statistic: t=3.113 df=8\n    p: 0.01\n    n: 9 mice\n  - about: tail base height at start of swing, non-slomo\n    test: paired, 2 tailed t-test\n    statistic: t=2.63 df=20\n    p: 0.02\n    n: 21 mice\n  - about: iliac crest height at start of swing, non-slomo\n    test: paired, 2 tailed t-test\n    statistic: t=1.284 df=20\n    p: 0.21\n    n: 21 mice\n  expected:\n  - quantity: slomo tail base height at start of swing, saline\n    value: 12.6\n    tolerance: 1.26\n    unit: mm\n  - quantity: slomo tail base height at start of swing, CNO\n    value: 16.5\n    tolerance: 1.65\n    unit: mm\n  - quantity: non-slomo tail base height at start of swing, saline\n    value: 14.0\n    tolerance: 1.4\n    unit: mm\n  - quantity: non-slomo tail base height at start of swing, CNO\n    value: 16.2\n    tolerance: 1.62\n    unit: mm\n  depends_on:\n  - zscore-subgroups\n  criterion: Heights of tail base and iliac crest above the floor at the start of swing, from\n    marked video frames (Methods, Kinematic data), per mouse averaged per condition; paired\n    two-tailed t-tests at alpha 0.05 (Table S3). Reproduced when tail base height rises with p <\n    0.05 in both groups and the four tail base means are within tolerance. The Methods do not\n    say how many swing phases per mouse were marked; all available marked swings are used.\n- id: figs3-2-ta-burst-prolonged\n  statement: With CNO, TA burst duration during steady walking was prolonged in the VGaT Z SwT >\n    2 (slomo) group (0.07 to 0.16 s) but not in the Z SwT < 2 or WT groups.\n  source: Figure 3e; Figure 3-Figure supplement 2a; Results, Activation of the anterior tibial\n    muscle is prolonged during slomo walking; Table S4\n  quote: Group analyses confirmed prolonged TA burst duration in the Z SwT >2 ( slomo ) group, but\n    not Z<2 and WT groups, with CNO compared to baseline\n  statistics:\n  - about: Z SwT > 2\n    test: Paired, two-tailed t test\n    statistic: t=6.475 df=5\n    p: 0.001\n    n: 6 mice\n  - about: Z SwT < 2\n    test: Paired, two-tailed t test\n    statistic: t=2.076 df=9\n    p: 0.07\n    n: 10 mice\n  - about: WT\n    test: Paired, two-tailed t test\n    statistic: t=1.376 df=3\n    p: 0.26\n    n: 4 mice\n  expected:\n  - quantity: Z SwT > 2 TA burst duration, saline\n    value: 0.07\n    tolerance: 0.007\n    unit: s\n  - quantity: Z SwT > 2 TA burst duration, CNO\n    value: 0.16\n    tolerance: 0.016\n    unit: s\n  depends_on:\n  - zscore-subgroups\n  criterion: EMG processed as in the Methods (d), band pass 67 to 1500 Hz (7th order Butterworth\n    IIR), DC removal with a 0.3 s window, rectification, RMS smoothing over 10 ms; burst and\n    interburst durations from the rectified signal; 20 walking cycles per mouse per condition;\n    per-mouse means; paired two-tailed t-test at alpha 0.05. Burst onset and offset detection\n    is not specified in the Methods; readings are (a) threshold crossings of the smoothed\n    envelope at a fixed fraction of the burst peak, (b) bursts as marked in the data if the\n    dataset provides them. Reproduced when the Z > 2 group gives p < 0.05 with longer bursts\n    and means within tolerance, and the Z < 2 and WT groups give p >= 0.05.\n- id: figs3-2-burst-duration-correlates-zswt\n  statement: In EMG-instrumented VGaT mice, the Z-score of TA burst duration correlated with Z\n    SwT from gait analysis (r 0.63).\n  source: Figure 3-Figure supplement 2c; Results, Activation of the anterior tibial muscle is\n    prolonged during slomo walking; Table S5\n  quote: showed that Z-scores for TA burst duration correlated with Z SwT from gait analyses\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.63\n    p: 0.005\n    ci:\n      level: 0.95\n      low: 0.1911\n      high: 0.8567\n    n: 16 VGaT mice\n  expected:\n  - quantity: Pearson r, Z SwT against Z TA burst duration\n    value: 0.63\n    tolerance: 0.063\n  depends_on:\n  - zscore-subgroups\n  - figs3-2-ta-burst-prolonged\n  criterion: Z-score of TA burst duration computed for each VGaT mouse as for Z SwT (same\n    readings, with the VGaT WT EMG mice as reference); Pearson correlation with Z SwT over the\n    16 VGaT mice with EMG. Reproduced when r is within tolerance and p < 0.05.\n- id: tables5-burst-amplitude-no-correlation\n  statement: Z-scores for TA burst amplitude did not correlate with Z SwT, in VGaT mice (r 0.24)\n    or VGluT2 mice (r -0.34).\n  source: Figure 3-Figure supplement 2d; Figure 4-Figure supplement 2c; Results, Activation of\n    the anterior tibial muscle is prolonged during slomo walking; Table S5\n  quote: As expected, Z-scores for TA amplitude did not correlate with Z SwT (Figure 3-Figure\n    supplement 2, Table S5)\n  statistics:\n  - about: VGaT\n    test: Pearson correlation\n    statistic: r = 0.24\n    p: 0.37\n    ci:\n      level: 0.95\n      low: -0.2914\n      high: 0.6568\n    n: 16 VGaT mice\n  - about: VGluT2\n    test: Pearson correlation\n    statistic: r = -0.34\n    p: 0.25\n    ci:\n      level: 0.95\n      low: -0.7523\n      high: 0.2555\n    n: 13 VGluT2 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the Pearson correlation at alpha\n    0.05 (Table S5). Reproduced when neither cohort gives p < 0.05; r is reported either way.\n- id: figs3-2-ta-amplitude\n  statement: In VGaT mice CNO did not change average TA peak burst amplitude in any Z SwT\n    subgroup, while TA interburst amplitude decreased in both the high (slomo) and low Z SwT\n    groups but not in WT, so there was no co-activation of TA and G.\n  source: Figure 3-Figure supplement 2a; Results, Activation of the anterior tibial muscle is\n    prolonged during slomo walking; Table S4\n  quote: average TA peak burst amplitude was variable but did not change in any Z SwT -defined\n    subgroup whereas TA interburst amplitude decreased in both high ( slomo ) and low Z SwT\n    groups but not WT\n  statistics:\n  - about: peak burst amplitude, Z>2\n    test: Paired, two-tailed t test\n    statistic: t=1.678 df=5\n    p: 0.15\n    n: 6 mice\n  - about: peak burst amplitude, Z<2\n    test: Paired, two-tailed t test\n    statistic: t=0.7027 df=9\n    p: 0.5\n    n: 10 mice\n  - about: peak burst amplitude, WT\n    test: Paired, two-tailed t test\n    statistic: t=0.04207 df=3\n    p: 0.97\n    n: 4 mice\n  - about: interburst amplitude, Z>2\n    test: Paired, two-tailed t test\n    statistic: t=3.04 df=5\n    p: 0.03\n    n: 6 mice\n  - about: interburst amplitude, Z<2\n    test: Paired, two-tailed t test\n    statistic: t=2.721 df=9\n    p: 0.02\n    n: 10 mice\n  - about: interburst amplitude, WT\n    test: Paired, two-tailed t test\n    statistic: t=3.05 df=3\n    p: 0.06\n    n: 4 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: EMG processing as in figs3-2-ta-burst-prolonged; amplitudes from the smoothed\n    signal normalized to the mean peak of 20 baseline swimming bursts (Methods, d); per-mouse\n    means; paired two-tailed t-tests at alpha 0.05. The absence of a peak amplitude change is\n    judged on that test. Reproduced when no group gives p < 0.05 for peak burst amplitude, and\n    interburst amplitude decreases with p < 0.05 in the Z > 2 and Z < 2 groups and gives p >=\n    0.05 in WT.\n- id: tables4-vgat-swimming\n  statement: During swimming, TA cycle frequency decreased slightly with CNO in the VGaT Z SwT >\n    2 group (median 6.0 to 5.2 Hz), but TA burst and interburst durations did not change\n    significantly in any Z SwT subgroup.\n  source: Results, Do slomo mice have deficits in other (loco)motor tasks?; Table S4 (swim)\n  quote: During swimming, TA cycle frequency decreased slightly in the Z SwT >2 ( slomo ) group\n    with CNO compared to baseline (Table S4), but TA burst or interburst duration alone did not\n    change significantly between conditions in any Z SwT subgroup\n  statistics:\n  - about: cycle frequency, Z>2\n    test: Wilcoxon two-tailed paired ranks test\n    statistic: W = -21\n    p: 0.03\n    n: 6 mice\n  - about: burst duration, Z>2\n    test: Paired, two-tailed t test\n    statistic: t=1.95 df=5\n    p: 0.11\n    n: 6 mice\n  - about: interburst duration, Z>2\n    test: Paired, two-tailed t test\n    statistic: t=2.313 df=5\n    p: 0.07\n    n: 6 mice\n  expected:\n  - quantity: Z>2 median TA swimming cycle frequency, saline\n    value: 6.0\n    tolerance: 0.6\n    unit: Hz\n  - quantity: Z>2 median TA swimming cycle frequency, CNO\n    value: 5.2\n    tolerance: 0.52\n    unit: Hz\n  depends_on:\n  - zscore-subgroups\n  criterion: Swimming EMG, 20 cycles per mouse per condition, processed as for walking; cycle\n    frequency as 1 / (burst + interburst duration) per cycle, averaged per mouse. Frequency by\n    the Wilcoxon matched-pairs test, durations by paired two-tailed t-tests, at alpha 0.05, as\n    Table S4 gives them. Reproduced when the Z > 2 frequency decreases with p < 0.05, and no\n    subgroup (Z > 2, Z < 2, WT) gives p < 0.05 for burst or interburst duration.\n- id: tables6-vgat-rotarod\n  statement: With CNO, latency to drop off the rotarod was shortened both in VGaT mice with high\n    Z SwT and in those with Z SwT < 2, so it was not specific to slomo mice.\n  source: Results, Do slomo mice have deficits in other (loco)motor tasks?; Table S6\n  quote: With CNO, latency to drop off a rotarod was shortened in both Z SwT >2 and Z SwT <2\n    groups compared to saline, i.e. not specific for slomo mice\n  statistics:\n  - about: Z>3 (slomo)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -45\n    p: 0.004\n    n: 9 mice\n  - about: 3>Z>2 (intermediate)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -10\n    p: 0.13\n    n: 5 mice\n  - about: Z<2 (non-slomo)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -151\n    p: 0.007\n    n: 21 mice\n  - about: WT control\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 19\n    p: 0.38\n    n: 10 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Per mouse, the mean latency to fall over 3 trials per session, averaged over\n    sessions per condition (Methods, Rotarod); Wilcoxon matched-pairs signed rank test,\n    two-tailed, at alpha 0.05 (Methods, e). The text says Z SwT > 2 while Table S6 splits it\n    into Z > 3 and 3 > Z > 2; readings are (a) the Z > 3 group, as in Table S6; (b) all mice\n    with Z SwT > 2 pooled. Reproduced when, under one reading, the high-Z group and the Z < 2\n    group both give p < 0.05 with shorter latency under CNO. The WT result is reported.\n- id: tables6-vgat-beam-ladder-unchanged\n  statement: VGaT hM3Dq activation did not affect slips and misses on the beam or the horizontal\n    ladder in the slomo or Z SwT < 2 groups.\n  source: Results, Do slomo mice have deficits in other (loco)motor tasks?; Table S6\n  quote: Activation did not affect errors on beam or ladder in Z SwT >2 ( slomo ) or Z SwT <2\n    groups\n  statistics:\n  - about: beam, Z>3\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -8\n    p: 0.58\n    n: 9 mice\n  - about: beam, Z<2\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -32\n    p: 0.53\n    n: 21 mice\n  - about: ladder, Z>3\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 4\n    p: 0.81\n    n: 9 mice\n  - about: ladder, Z<2\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -30\n    p: 0.32\n    n: 21 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the two-tailed Wilcoxon matched\n    pairs signed rank test at alpha 0.05 on per-mouse hind paw slips and misses (mean of 2\n    trials per session; Methods, f), in the Z > 3, 3 > Z > 2 and Z < 2 groups as in Table S6.\n    Reproduced when no group gives p < 0.05 on either test; the paper's text pools Z > 2, so\n    the pooled Z > 2 test is shown as a variant.\n- id: fig4b-shuffle-signature-shifts\n  statement: In the VGluT2 Z SwT < -3 (shuffle) group CNO shortened swing time, stance time and\n    stride length out of proportion to the slowed speed (downward signature shifts), and stride\n    frequency was higher than expected for stride velocity.\n  source: Figure 4b; Results, Shifts in gait signatures that define Shuffle style contrast those\n    of Slomo walking; Table S8\n  quote: VGluT2 hM3Dq activation in the Z SwT <-3 ( shuffle ) group caused shortening of swing\n    time, stance time and stride length out of proportion to slowed speed as demonstrated by\n    downward shifts of their respective walking signatures ( Fig. 4b ). Due shortening of both\n    swing and stance times, stride frequency (cadence) was higher than expected for stride\n    velocity\n  statistics:\n  - about: swing time\n    test: sum of squares F test\n    statistic: F (2, 906) = 63.13\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice, 491 saline and 631 CNO strides\n  - about: stance time\n    test: sum of squares F test\n    statistic: F (4, 841) = 20.28\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: stride length\n    test: sum of squares F test\n    statistic: F (2, 906) = 84.18\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: cadence\n    test: sum of squares F test\n    statistic: F (2, 886) = 49.5\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Walking signature tests in the shuffle group. Reproduced when swing time, stance\n    time and stride length each give p < 0.001 with the CNO curve below the saline curve over\n    the shared velocity range, and cadence gives p < 0.001 with the CNO curve above, under every\n    model reading.\n- id: fig4c-shuffle-coupling-variable\n  statement: In the shuffle group hindlimb left-right coupling became more variable with CNO.\n  source: Figure 4c; Results, Shifts in gait signatures that define Shuffle style contrast those\n    of Slomo walking; Table S8 (temporal coupling)\n  quote: Polar plots revealed that hindlimb coupling was more variable following VGluT2 hM3Dq\n    activation than at baseline in the Z SwT <-3 ( shuffle ) group\n  statistics:\n  - test: Watson-Williams test\n    p: 0.00002\n    n: 15 mice\n  expected:\n  - quantity: mean resultant length r, saline\n    value: 0.74\n    tolerance: 0.074\n  - quantity: mean resultant length r, CNO\n    value: 0.60\n    tolerance: 0.06\n  depends_on:\n  - zscore-subgroups\n  criterion: Back left against back right phase as in fig3c-slomo-coupling-unchanged, strides of\n    3 to 16 cm/s; Watson-Williams test of saline against CNO at alpha 0.05 (Methods, b). More\n    variable is read as a lower mean resultant length r, the value Table S8 reports. Reproduced\n    when the Watson-Williams test gives p < 0.05 and r is lower under CNO, with both r within\n    tolerance.\n- id: fig4d-shuffle-swing-speed-preserved\n  statement: In the shuffle group stride length shortened during the swing phase while swing\n    speed was preserved, in contrast to slomo mice in which swing speed decreased.\n  source: Figure 4d; Results, Shifts in gait signatures that define Shuffle style contrast those\n    of Slomo walking; Table S8\n  quote: During the swing phase, stride length shortened with preserved swing speed ( Fig. 4d ),\n    in contrast to slomo mice with stable stride length but decreased swing speed\n  statistics:\n  - about: per-mouse mean swing speed\n    test: paired, 2 tailed t-test\n    statistic: t=0.812 df=14\n    p: 0.43\n    n: 15 mice\n  - about: per-mouse mean stride length\n    test: paired, 2 tailed t-test\n    statistic: t=6.325 df=14\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: stride length against swing speed signature\n    test: sum of squares F test\n    statistic: F (2, 1015) = 176.9\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Per-mouse mean swing speed and stride length by paired two-tailed t-tests at alpha\n    0.05, and the stride length against swing speed signature by the extra sum of squares F\n    test at alpha 0.001 (Table S8). Preserved swing speed is judged on the paper's t-test, as an\n    absence. Reproduced when swing speed gives p >= 0.05, stride length decreases with p < 0.05,\n    and the signature shifts with shorter strides for a given swing speed at p < 0.001.\n- id: fig4-shuffle-posture-lowered\n  statement: Shuffle gait was accompanied by a lowered tail base and iliac crest during the swing\n    phase.\n  source: Figure 4d; Results, Shifts in gait signatures that define Shuffle style contrast those\n    of Slomo walking; Table S8 (postural metrics)\n  quote: Postural changes including lowered tail base and iliac crest accompanied shuffle gait in Z\n    SwT <-3 sub-group\n  statistics:\n  - about: iliac crest height, start of swing\n    test: paired, 2 tailed t-test\n    statistic: t=4.131 df=14\n    p: 0.001\n    n: 15 mice\n  - about: tail base height, start of swing\n    test: paired, 2 tailed t-test\n    statistic: t=5.514 df=14\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: iliac crest height, end of swing\n    test: paired, 2 tailed t-test\n    statistic: t=5.823 df=14\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: tail base height, end of swing\n    test: paired, 2 tailed t-test\n    statistic: t=7.008 df=14\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  expected:\n  - quantity: tail base height at start of swing, saline\n    value: 15.0\n    tolerance: 1.5\n    unit: mm\n  - quantity: tail base height at start of swing, CNO\n    value: 10.2\n    tolerance: 1.02\n    unit: mm\n  - quantity: iliac crest height at start of swing, saline\n    value: 26.9\n    tolerance: 2.69\n    unit: mm\n  - quantity: iliac crest height at start of swing, CNO\n    value: 24.4\n    tolerance: 2.44\n    unit: mm\n  depends_on:\n  - zscore-subgroups\n  criterion: Heights as in fig3d-posture-not-slomo-specific; paired two-tailed t-tests at alpha\n    0.05. Reproduced when tail base and iliac crest heights fall with p < 0.05 at the start and\n    end of swing and the start-of-swing means are within tolerance.\n- id: figs4-1-nonshuffle\n  statement: In the VGluT2 Z SwT > -2 (non-shuffle) group walking speed decreased with CNO, without\n    shifts of the swing and stance time signatures, with subtle changes in the stride length\n    signature and in hindlimb coupling.\n  source: Figure 4-Figure supplement 1; Results, Shifts in gait signatures that define Shuffle\n    style contrast those of Slomo walking; Table S8 (non-shuffle group)\n  quote: In the Z SwT >-2 ( non-shuffle ) group (Figure 4-Figure supplement 1; Table S8), walking\n    speed decreased, but without changes in swing and stance time signatures or posture, and with\n    subtle changes in stride length signature and hindlimb coupling\n  statistics:\n  - about: stride velocity, per-mouse means\n    test: paired, 2 tailed t-test\n    statistic: t=3.612 df=13\n    p: 0.003\n    n: 14 mice\n  - about: swing time signature\n    test: sum of squares F test\n    statistic: F (2, 1009) = 2.23\n    p: 0.11\n    n: 14 mice, 575 saline and 806 CNO strides\n  - about: stance time signature\n    test: sum of squares F test\n    statistic: F (4, 1126) = 3.14\n    p: 0.01\n    n: 14 mice\n  - about: stride length signature\n    test: sum of squares F test\n    statistic: F (2, 1009) = 8.57\n    p: 0.0002\n    n: 14 mice\n  - about: hindlimb coupling\n    test: Watson-Williams test\n    p: 0.03\n    n: 14 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Velocity by the paired two-tailed t-test at alpha 0.05; swing and stance signatures\n    judged as absences on the paper's F test at alpha 0.001; stride length signature by the F\n    test at alpha 0.001; coupling by the Watson-Williams test at alpha 0.05. Reproduced when\n    velocity decreases with p < 0.05, swing and stance give p >= 0.001, stride length gives p <\n    0.001 and coupling p < 0.05, under every model reading. Posture is reported; Table S8 gives\n    tail base at end of swing at p 0.047, which the text counts as no change.\n- id: tables9-vglut2-motor-unchanged\n  statement: In none of the Z SwT-defined VGluT2 groups or their WT controls did CNO change\n    performance on rotarod, beam or ladder.\n  source: Results, Shifts in gait signatures that define Shuffle style contrast those of Slomo\n    walking; Table S9\n  quote: In none of the Z SwT -defined experimental or control groups (Table S9) CNO activation\n    changed performance on rotarod, beam, or ladder\n  statistics:\n  - about: rotarod, Z<-3 (smallest p of the shuffle group tests is the ladder, 0.19)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 25\n    p: 0.23\n    n: 10 mice\n  - about: rotarod, WT control (smallest p of all Table S9 tests)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 15\n    p: 0.16\n    n: 6 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, two-tailed Wilcoxon matched-pairs\n    signed rank tests at alpha 0.05 on per-mouse rotarod latency and beam and ladder slips and\n    misses, in the Z < -3, -3 < Z < -2, Z > -2 and WT groups. Table S9 holds 10, 10 and 13\n    experimental mice (fewer than the gait groups). Reproduced when none of the 12 tests gives\n    p < 0.05.\n- id: fig4e-shuffle-coactivation\n  statement: In shuffle mice (VGluT2 Z SwT < -2) TA and G co-activated during the stance phase,\n    because TA interburst activity increased with CNO.\n  source: Figure 4e; Results, Anterior tibial and gastrocnemius muscles co-activate during\n    shuffle walking; Table S10\n  quote: EMG of TA and G muscles in shuffle mice (VGluT2 hM3Dq Z SwT <-2) revealed co-activation of\n    TA and G muscles during the stance phase due to increased TA interburst activity\n  statistics:\n  - about: TA interburst peak amplitude\n    test: Paired, two-tailed t test\n    statistic: t=3.043 df=6\n    p: 0.02\n    n: 7 mice\n  - about: TA interburst integral\n    test: Paired, two-tailed t test\n    statistic: t=2.877 df=6\n    p: 0.03\n    n: 7 mice\n  expected:\n  - quantity: TA interburst peak amplitude (normalized), saline\n    value: 0.44\n    tolerance: 0.044\n  - quantity: TA interburst peak amplitude (normalized), CNO\n    value: 0.62\n    tolerance: 0.062\n  depends_on:\n  - zscore-subgroups\n  criterion: EMG processing as in figs3-2-ta-burst-prolonged; per-mouse means of TA interburst\n    peak amplitude and integral during walking, normalized to baseline swimming; paired\n    two-tailed t-tests at alpha 0.05 (Table S10). Reproduced when both increase with p < 0.05\n    and the amplitude means are within tolerance. Table S10 also gives increases in the Z > -2\n    group (p 0.05 and 0.02); they are reported.\n- id: figs4-2-shuffle-burst-shorter\n  statement: TA burst duration during steady walking decreased with CNO in shuffle mice (0.08 to\n    0.05 s), and less so in the non-shuffle group.\n  source: Figure 4e iii; Figure 4-Figure supplement 2a; Results, Anterior tibial and\n    gastrocnemius muscles co-activate during shuffle walking; Table S10\n  quote: TA EMG envelopes during steady walking demonstrated decreased TA burst duration with a\n    more rapid ramp down with CNO compared to saline\n  statistics:\n  - about: Z<-2 (shuffle)\n    test: Paired, two-tailed t test\n    statistic: t=4.324 df=6\n    p: 0.005\n    n: 7 mice\n  - about: Z>-2 (non-shuffle)\n    test: Paired, two-tailed t test\n    statistic: t=3.367 df=5\n    p: 0.02\n    n: 6 mice\n  expected:\n  - quantity: shuffle TA burst duration, saline\n    value: 0.08\n    tolerance: 0.008\n    unit: s\n  - quantity: shuffle TA burst duration, CNO\n    value: 0.05\n    tolerance: 0.005\n    unit: s\n  depends_on:\n  - zscore-subgroups\n  criterion: Burst duration as in figs3-2-ta-burst-prolonged; paired two-tailed t-tests at\n    alpha 0.05. Reproduced when the shuffle group decreases with p < 0.05 and its means are\n    within tolerance. \"Less pronounced\" in the non-shuffle group is read on the paper's own\n    numbers (t 3.367 against 4.324, p 0.02 against 0.005), so the non-shuffle t statistic and\n    mean change are reported next to the shuffle ones; the claim does not rest on them.\n- id: tables10-ta-peak-amplitude-up-both\n  statement: Peak TA burst amplitude increased significantly with CNO in both the shuffle (Z SwT\n    < -2) and non-shuffle (Z SwT > -2) VGluT2 groups, so it is not specific to shuffle mice.\n  source: Results, Anterior tibial and gastrocnemius muscles co-activate during shuffle walking;\n    Table S10\n  quote: However, peak TA burst amplitude increased significantly with CNO compared to saline in\n    both Z SwT <-2 ( shuffle ) and Z SwT >-2 ( non-shuffle ) groups (Table S10)\n  statistics:\n  - about: Z<-2\n    test: Paired, two-tailed t test\n    statistic: t=3.307 df=6\n    p: 0.02\n    n: 7 mice\n  - about: Z>-2\n    test: Paired, two-tailed t test\n    statistic: t=3.044 df=5\n    p: 0.03\n    n: 6 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Peak burst amplitude from the smoothed signal normalized to baseline swimming\n    (Methods, d); per-mouse means; paired two-tailed t-tests at alpha 0.05. Reproduced when both\n    groups increase with p < 0.05.\n- id: tables10-shuffle-swimming-unchanged\n  statement: During swimming, neither TA burst and interburst duration nor cycle frequency\n    changed between baseline and CNO in the shuffle group.\n  source: Results, Anterior tibial and gastrocnemius muscles co-activate during shuffle walking;\n    Table S10 (swim)\n  quote: During swimming, neither TA burst and interburst duration nor cycle frequency changed\n    between baseline and CNO in the Z SwT <-2 ( shuffle ) group\n  statistics:\n  - about: burst duration\n    test: Paired, two-tailed t test\n    statistic: t=0.2822 df=6\n    p: 0.79\n    n: 7 mice\n  - about: interburst duration\n    test: Paired, two-tailed t test\n    statistic: t=0.8298 df=6\n    p: 0.44\n    n: 7 mice\n  - about: cycle frequency\n    test: Wilcoxon two-tailed paired ranks test\n    statistic: W = 14\n    p: 0.3\n    n: 7 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's tests at alpha 0.05 (paired t-tests for\n    durations, Wilcoxon for frequency, as Table S10 gives them), swimming cycles processed as in\n    tables4-vgat-swimming. Reproduced when none of the three gives p < 0.05.\n- id: tables10-g-emg-unchanged\n  statement: There were no significant changes in gastrocnemius EMG parameters at the group level\n    in VGluT2 mice, though G data were underpowered.\n  source: Results, Anterior tibial and gastrocnemius muscles co-activate during shuffle walking;\n    Table S10 (gastrocnemius)\n  quote: There were no significant changes in G EMG parameters at the group level, though G data\n    was underpowered due to quality constraints (Table S10)\n  statistics:\n  - about: smallest p of the G tests, interburst amplitude in Z<-2 (also burst amplitude and integral in Z>-2)\n    test: Wilcoxon two-tailed paired ranks test\n    statistic: W = 15\n    p: 0.06\n    n: 5 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the two-tailed Wilcoxon paired\n    ranks test at alpha 0.05 on per-mouse G burst and interburst duration, peak amplitude and\n    integral, walking and swimming, in the Z < -2 and Z > -2 groups (Table S10). Reproduced when\n    none gives p < 0.05.\n- id: fig5-sert-no-signature-shift\n  statement: In the SerT high Z StrV (fast) and low Z StrV (slow) groups CNO changed spatial and\n    temporal gait metrics that dictate speed in opposite directions, but in proportion to speed,\n    without curve shifts.\n  source: Figure 5; Figure 5-Figure supplement 1; Results, Serotonergic activation modulates\n    walking speed without shifts in walking signatures; Table S12\n  quote: In high Z StrV ( fast ) ( Fig. 5 ) and low Z StrV ( slow ) groups (Figure 5-Figure\n    supplement 1), CNO activation changed spatial and temporal gait metrics that dictate speed in\n    opposite directions, but in proportion to speed, i.e. without curve shifts\n  statistics:\n  - about: fast group, swing time signature (smallest p among stride length, swing, stance, cadence)\n    test: sum of squares F test\n    statistic: F (2, 302) = 2.206\n    p: 0.11\n    n: 6 mice, 236 saline and 223 CNO strides\n  - about: slow group, stride length signature (smallest p among stride length, swing, stance, cadence)\n    test: sum of squares F test\n    statistic: F (2, 369) = 2.94\n    p: 0.05\n    n: 6 mice, 229 saline and 241 CNO strides\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, the extra sum of squares F test at\n    alpha 0.001 for stride length, swing time, stance time and cadence against stride velocity\n    (the metrics that dictate speed) in the top and bottom thirds of SerT mice by Z StrV.\n    Reproduced when none of the eight tests gives p < 0.001 under any model reading. The\n    stride length against swing speed tests are reported as they are; Table S12 gives p 0.0001\n    for it in the slow group.\n- id: fig5-sert-opposite-directions\n  statement: CNO changed per-mouse averages in opposite directions in the SerT fast and slow\n    groups; in the fast group stride velocity rose from 11.37 to 15.61 cm/s with longer strides\n    and shorter stance, in the slow group it fell from 12.79 to 8.63 cm/s with shorter strides\n    and longer stance.\n  source: Figure 5; Figure 5-Figure supplement 1; Table S12\n  inferred: Directions and numbers from Table S12 (per-mouse averages); the text says only that\n    the metrics changed in opposite directions.\n  statistics:\n  - about: fast, stride length\n    test: paired, 2 tailed t-test\n    statistic: t=9.81 df=5\n    p: 0.0002\n    n: 6 mice\n  - about: fast, stance time\n    test: paired, 2 tailed t-test\n    statistic: t=6.17 df=5\n    p: 0.0016\n    n: 6 mice\n  - about: slow, stride velocity\n    test: paired, 2 tailed t-test\n    statistic: t=2.93 df=5\n    p: 0.03\n    n: 6 mice\n  - about: slow, stride length\n    test: paired, 2 tailed t-test\n    statistic: t=3.95 df=5\n    p: 0.01\n    n: 6 mice\n  - about: slow, stance time\n    test: paired, 2 tailed t-test\n    statistic: t=2.89 df=5\n    p: 0.03\n    n: 6 mice\n  expected:\n  - quantity: fast mean stride length, saline\n    value: 41.26\n    tolerance: 4.13\n    unit: mm\n  - quantity: fast mean stride length, CNO\n    value: 49.18\n    tolerance: 4.92\n    unit: mm\n  - quantity: slow mean stride velocity, saline\n    value: 12.79\n    tolerance: 1.28\n    unit: cm/s\n  - quantity: slow mean stride velocity, CNO\n    value: 8.63\n    tolerance: 0.86\n    unit: cm/s\n  depends_on:\n  - zscore-subgroups\n  - fig2c-sert-subset-faster\n  criterion: Per-mouse means, paired two-tailed t-tests at alpha 0.05 (Table S12). Reproduced\n    when, in the fast group, stride length rises and stance falls, and in the slow group,\n    velocity and stride length fall and stance rises, each with p < 0.05, and the means are\n    within tolerance.\n- id: tables12-sert-coupling-posture-unchanged\n  statement: Left-right temporal hindlimb coupling and the posture of iliac crest and tail base\n    did not change with CNO in any Z StrV subgroup of SerT mice.\n  source: Results, Serotonergic activation modulates walking speed without shifts in walking\n    signatures; Table S12\n  quote: Left-right temporal hindlimb coupling and posture of iliac crest and tail base did not\n    change following CNO activation in any Z StrV subgroup (Table S12)\n  statistics:\n  - about: coupling, high Z\n    test: Watson-Williams test\n    p: 0.3\n    n: 6 mice\n  - about: coupling, intermediate Z\n    test: Watson-Williams test\n    p: 0.65\n    n: 6 mice\n  - about: coupling, low Z\n    test: Watson-Williams test\n    p: 0.43\n    n: 6 mice\n  - about: tail base height at end of swing, high Z (smallest posture p)\n    test: paired, 2 tailed t-test\n    statistic: t=2.464 df=5\n    p: 0.06\n    n: 6 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's tests at alpha 0.05, the Watson-Williams\n    test for coupling (strides of 3 to 16 cm/s) and paired two-tailed t-tests for the four\n    postural heights, in each SerT third (posture is tabled for the high and low thirds).\n    Reproduced when no test gives p < 0.05.\n- id: tables13-sert-emg-trend\n  statement: In the SerT high Z StrV (fast) group TA peak burst amplitude and area under the curve\n    during steady walking showed a trend to increase with CNO, without changes in TA timing;\n    neither timing nor amplitude changed in the low Z StrV group.\n  source: Figure 5e; Figure 5-Figure supplement 2; Results, Serotonergic activation modulates\n    walking speed without shifts in walking signatures; Table S13\n  quote: EMG of TA and G muscles revealed a trend for increased peak amplitude and area under the\n    curve of TA bursts during steady walking in the high Z StrV ( fast ) group ... but without the\n    changes in timing or co-activation seen in slomo or shuffle subgroups. Neither timing nor\n    amplitude changed in the low Z StrV (slow) group\n  statistics:\n  - about: peak burst amplitude, Z>0\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 15\n    p: 0.06\n    n: 5 mice\n  - about: burst integral, Z>0\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 15\n    p: 0.06\n    n: 5 mice\n  - about: burst duration, Z>0\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = 9\n    p: 0.31\n    n: 5 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: SerT EMG groups as the Methods (d) give them, Z StrV > 0 (n 5) and Z StrV < 0 (n\n    3); per-mouse means; two-tailed Wilcoxon matched-pairs signed rank tests (Methods, d). The\n    paper calls p 0.06 a trend; with 5 pairs this is the smallest two-tailed p the test can give,\n    reached only when all 5 mice change in the same direction (W = 15, Table S13). Reproduced\n    when peak amplitude and integral increase in all 5 fast mice (W = 15), burst and interburst\n    duration and interburst amplitude give p >= 0.05 in the fast group, and no test gives p <\n    0.05 in the slow group.\n- id: tables13-sert-swimming\n  statement: During swimming, TA EMG metrics did not change with CNO in the high or low Z StrV\n    SerT groups, except for a trend towards increased cycle frequency in the fast group.\n  source: Results, Serotonergic activation modulates walking speed without shifts in walking\n    signatures; Table S13 (swim)\n  quote: During swimming, TA EMG metrics did not change in high or low Z StrV groups with CNO\n    versus baseline, except for a trend towards increased cycle frequency in the high Z StrV (\n    fast ) group (Table S13)\n  statistics:\n  - about: cycle frequency, Z>0\n    test: Wilcoxon two-tailed paired ranks test\n    statistic: W = 15\n    p: 0.06\n    n: 5 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Swimming cycles as in tables4-vgat-swimming; two-tailed Wilcoxon tests (Table S13).\n    Reproduced when no swimming TA test gives p < 0.05 in either group and the fast group's\n    cycle frequency increases in all 5 mice (W = 15, the paper's trend).\n- id: tables14-sert-motor-g-unchanged\n  statement: CNO induced no changes in G EMG metrics or in rotarod, beam and ladder performance\n    in any Z StrV-defined SerT group or control group.\n  source: Results, Serotonergic activation modulates walking speed without shifts in walking\n    signatures; Tables S13 and S14\n  quote: CNO induced no changes in G EMG metrics or in performance on rotarod, beam, and ladder in\n    any of the Z StrV -defined experimental or control groups (Table S14)\n  statistics:\n  - about: rotarod, WT control (smallest p of Table S14)\n    test: Wilcoxon matched-pairs signed rank test, two-tailed\n    statistic: W = -66\n    p: 0.06\n    n: 15 mice\n  depends_on:\n  - zscore-subgroups\n  criterion: A claim of absence, judged on the paper's test, two-tailed Wilcoxon matched-pairs\n    signed rank tests at alpha 0.05; motor tests in the high, intermediate and low thirds and WT\n    (Table S14), G EMG in the Z > 0 and Z < 0 groups (Table S13). Reproduced when none gives p <\n    0.05.\n- id: fig6-slomo-sites-bilateral\n  statement: All VGaT Z SwT > 3 (slomo) transfection sites were bilateral; unilateral sites, even\n    when centered on the slomo hotspot, gave Z SwT < 2.\n  source: Results, Walking styles map to different mRF subregions, paragraph 2; Figure 6a; Table\n    S7 (note)\n  quote: In the VGaT cohort, Z SwT >3 ( slomo ) sites localized to the ventromedial caudal pons and\n    were all bilateral. Bilateral Z SwT <2 ( non-slomo ) sites were located dorsally, or ventrally\n    at more caudal levels. Unilateral sites, even when purposefully centered at the slomo\n    hotspot, yielded Z SwT <2\n  expected:\n  - quantity: unilateral VGaT cases targeted at the slomo hotspot, all with Z SwT < 2\n    value: 6\n    tolerance: 0.6\n  depends_on:\n  - zscore-subgroups\n  criterion: Per mouse, transfection laterality (unilateral or bilateral) from the histology\n    reconstructions, or from injection records if the data hold no reconstructions. Reproduced\n    when every Z > 3 mouse is bilateral and every unilateral mouse has Z SwT < 2 (Table S7\n    lists 6 unilateral and 15 bilateral Z < 2 mice).\n- id: fig6-shuffle-unilateral-sufficient\n  statement: In contrast to slomo gait, unilateral VGluT2 sites were sufficient to induce shuffle\n    style.\n  source: Results, Walking styles map to different mRF subregions, paragraph 3; Figure 6a;\n    Figure 4-Figure supplement 3\n  quote: In contrast to slomo gait, unilateral sites were sufficient to induce shuffle style\n  depends_on:\n  - zscore-subgroups\n  criterion: Laterality per mouse as in fig6-slomo-sites-bilateral. Reproduced when at least one\n    unilateral VGluT2 mouse has Z SwT < -3. Figure 4-Figure supplement 3 and Table S11 analyse\n    15 unilateral shuffle mice; that count is reported.\n- id: figs3-3-vgat-unilateral-no-asymmetry\n  statement: In VGaT mice with unilateral transfection involving the slomo hotspot, CNO did not\n    change stride length or swing time of either hindlimb, and ipsi- and contralateral hindlimbs\n    were similar in both conditions.\n  source: Figure 3-Figure supplement 3; Results, Walking styles map to different mRF subregions,\n    paragraph 2; Table S7\n  quote: Post-hoc analyses in unilateral cases did not reveal asymmetries in temporal (swing time)\n    or spatial (stride length) metrics\n  statistics:\n  - about: contralateral swing time, saline against CNO (smallest p of these tests)\n    test: sum of squares F test\n    statistic: F (2, 139) = 2.541\n    p: 0.08\n    n: 6 mice\n  - about: ipsi- against contralateral swing time, saline\n    test: sum of squares F test\n    statistic: F (2, 138) = 2.283\n    p: 0.11\n    n: 6 mice\n  depends_on:\n  - zscore-subgroups\n  - fig6-slomo-sites-bilateral\n  criterion: A claim of absence, judged on the paper's test, the extra sum of squares F test at\n    alpha 0.001 on stride length and swing time signatures (Table S7), for the 6 unilateral mice;\n    ipsilateral and contralateral hindlimbs, each saline against CNO, and ipsi against contra\n    within saline and within CNO. Reproduced when none of the 8 tests gives p < 0.001 under any\n    model reading.\n- id: figs4-3-shuffle-unilateral-asymmetry\n  statement: Unilateral VGluT2 shuffle sites shifted swing time and stride length signatures of\n    both hindlimbs; with CNO the swing time shift was larger contralateral to the transfection,\n    while stride length changed symmetrically.\n  source: Figure 4-Figure supplement 3; Results, Walking styles map to different mRF subregions,\n    paragraph 3; Table S11\n  quote: revealed that activation of uni lateral VGluT2 hM3Dq Z SwT <-3 ( shuffle ) sites shifted\n    key temporal (swing time) and spatial (stride length) gait signatures in a bilateral manner.\n    Shifts in swing time signatures were larger contra -than ipsilateral to the transfection site\n  statistics:\n  - about: ipsilateral swing time, saline against CNO\n    test: sum of squares F test\n    statistic: F (2, 448) = 16.9\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: contralateral swing time, saline against CNO\n    test: sum of squares F test\n    statistic: F (2, 453) = 20.91\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: ipsi- against contralateral swing time, CNO\n    test: sum of squares F test\n    statistic: F (2, 514) = 10.21\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 mice\n  - about: ipsi- against contralateral stride length, CNO\n    test: sum of squares F test\n    statistic: F (2, 514) = 0.9296\n    p: 0.4\n    n: 15 mice\n  - about: ipsi- against contralateral swing time, saline\n    test: sum of squares F test\n    statistic: F (2, 387) = 0.3077\n    p: 0.74\n    n: 15 mice\n  depends_on:\n  - zscore-subgroups\n  - fig6-shuffle-unilateral-sufficient\n  criterion: Unilateral VGluT2 shuffle mice (Z SwT < -3); strides labelled ipsi- or\n    contralateral to the transfection; extra sum of squares F tests at alpha 0.001 (Table S11).\n    Reproduced when swing time and stride length signatures shift for both hindlimbs, ipsi\n    against contra differs for swing time under CNO with the contralateral swing time shorter\n    for a given velocity, and ipsi against contra gives p >= 0.001 for stride length under CNO\n    and for swing time under saline, under every model reading.\n- id: fig6a-hotspot-locations\n  statement: Slomo, shuffle and fast styles map to distinct mRF sites; slomo sites to the\n    ventromedial caudal pons, shuffle sites ventrally but caudal to the slomo hotspot with\n    non-shuffle sites dorsal or lateral, and SerT fast and slow sites to the caudal and rostral\n    poles of the midline medullary raphe.\n  source: Figure 6a and 6b; Results, Walking styles map to different mRF subregions, paragraphs 2\n    to 5\n  quote: In the VGluT2 hM3Dq cohort, Z SwT <-3 ( shuffle ) sites also localized ventrally, but\n    caudal to the VGaT hM3Dq slomo hotspot. Z SwT >-2 ( non-shuffle ) sites localized more dorsally\n    or laterally ... In the SerT cohort, transfection sites of high ( fast ) and low ( slow ) Z StrV\n    groups localized to caudal and rostral poles of the midline medullary raphe, respectively\n  depends_on:\n  - zscore-subgroups\n  criterion: Transfection sites reconstructed at 320 um intervals with core and periphery, merged\n    by Z-score group (Methods, Reconstructions of injection sites; Figure 6-Figure supplement\n    1). The paper compares the maps by eye; the measure fixed from its Methods is the group\n    composite, and the comparison is the rostrocaudal (relative to obex) and dorsoventral\n    position of each composite's peak. Reproduced when the slomo peak is rostral to the shuffle\n    peak, both ventral to their negative groups' peaks, and the SerT fast peak caudal to the\n    slow peak. If the dataset holds only stereotaxic targets per mouse, those are used, with the\n    paper's hotspot coordinates (slomo AP 0, shuffle AP -0.2, raphe obscurus AP -0.45 relative\n    to obex) as the reference.\n- id: figs6-2-interburst-amplitude-map\n  statement: In the VGaT cohort, decreased Z InterburstAmplitude mapped to the ventral mRF in a\n    region extending caudally far beyond the slomo hotspot and involving both bilateral and\n    unilateral sites.\n  source: Figure 6-Figure supplement 2; Results, Walking styles map to different mRF subregions,\n    paragraph 2\n  quote: Indeed, while decreased Z InterburstAmplitude mapped to the ventral mRF, this region\n    extended caudally far beyond the slomo hotspot and involved both bilateral and unilateral sites\n  depends_on:\n  - zscore-subgroups\n  - fig6a-hotspot-locations\n  criterion: VGaT mice with Z InterburstAmplitude < -1.3 (the threshold of Figure 6-Figure\n    supplement 2), Z computed as for Z SwT; their sites compiled as in fig6a-hotspot-locations.\n    Reproduced when that group includes unilateral and bilateral mice and its composite extends\n    caudal to the slomo composite.\n- id: fig6c-rsn-clusters\n  statement: Inhibitory and excitatory reticulospinal neurons, retrogradely labelled from the\n    cervical and lumbar cord, cluster in the centers of the slomo and shuffle hotspots\n    respectively, but many reticulospinal neurons lie beyond the hotspots.\n  source: Figure 6c; Results, Sites that drive contrasting walking styles differ in connectivity,\n    paragraph 2\n  quote: Inhibitory and excitatory reticulospinal neurons (RSN) form clusters in the centers of\n    slomo and shuffle hotspots, respectively, but these clusters represent only a small portion of\n    the reticulospinal system\n  criterion: CTb-labelled reticulospinal neurons with VGaT or VGluT2 mRNA by ISH, in the two\n    reconstructed WT cases (Methods, Mapping of RSNs). The paper reports the maps without a\n    count or test; the comparison is the location of the densest VGaT+ and VGluT2+ CTb+ clusters\n    against the hotspot coordinates of the Methods. Reproduced when those clusters fall at the\n    slomo and shuffle hotspots and CTb+ neurons also lie outside them.\n- id: fig6d-lumbar-projections\n  statement: VGaT projections from the slomo hotspot densely innervate the lumbar dorsal horn and\n    intermediate zone and less so the ventral horn; VGluT2 projections from the shuffle hotspot\n    most densely target the intermediate zone, especially area X; SerT fast sites innervate\n    ventral, intermediate and dorsal horn and slow sites the dorsal horn only.\n  source: Figure 6d; Results, Sites that drive contrasting walking styles differ in connectivity,\n    paragraph 3\n  quote: VGaT hM3Dq-mCherry projections from the Z SwT >3 ( slomo ) hotspot densely innervated\n    dorsal horn and intermediate zone and less so ventral horn. VGluT2 hM3Dq-mCherry projections\n    from the Z SwT <-3 ( shuffle ) hotspot most densely targeted the intermediate zone of the\n    lumbar cord, especially area X, and also less so ventral horn ... SerT hM3Dq-mCherry sites in\n    the high ( fast ) Z StrV group innervated the spinal ventral, intermediate and dorsal horn and\n    the low ( slow ) Z StrV group the dorsal horn only\n  depends_on:\n  - zscore-subgroups\n  criterion: Following the Methods (Spinal projections, Global distribution) for representative\n    cases with small sites; 3 upper and 3 mid lumbar sections, color thresholding of labelled\n    axons and terminals to binary images, superimposed, 5-pixel mean filter. The paper reads the\n    maps by eye and names no threshold; the measure here is the labelled area fraction in the\n    dorsal horn, intermediate zone (with area X) and ventral horn of the composite. Reproduced\n    when the regional ranking of each case matches the statement. If the dataset holds no\n    spinal images, not testable.\n- id: figs6-3-hotspots-sparse-ascending\n  statement: Slomo and shuffle hotspots in mice with a prominent style phenotype did not project\n    heavily to mid- and forebrain, in contrast to sites involving more dorsal mRF regions.\n  source: Figure 6-Figure supplement 3; Results, Sites that drive contrasting walking styles\n    differ in connectivity, paragraph 3\n  quote: Slomo or shuffle hotspots in mice with a prominent style phenotype did not project heavily\n    to mid- and forebrain sites in sharp contrast to sites that involved more dorsal mRF regions\n  criterion: Representative cases as in Figure 6-Figure supplement 3, mCherry (DAB) labelling in\n    forebrain and midbrain sections. The paper gives no measure; the measure used is the\n    labelled area fraction from the same thresholding as fig6d-lumbar-projections. Reproduced\n    when the hotspot cases have lower mid- and forebrain fractions than the dorsal-site cases.\n- id: fig7-ctb-confirms-connections\n  statement: Retrograde CTb injected into the dorsal horn (VGaT), intermediate zone (VGluT2) or\n    ventral half (SerT) of the lumbar cord labelled hM3Dq-mCherry neurons in the respective\n    hotspots, confirming ipsilateral connections; ISH and IHC confirmed cell type specificity of\n    transfected neurons and boutons.\n  source: Figure 7a-b; Figure 7-Figure supplement 1; Results, Hotspots for slomo and shuffle\n    walking target distinct neuronal substrates, paragraph 1\n  quote: Retrograde CTb labeling of hM3Dq-mCherry transfected neurons in the hotspots confirmed\n    ipsilateral connections to the respective spinal sub-regions. We further verified cell type\n    specificity in the transfected hotspots and in transfected spinal boutons using ISH and IHC\n  criterion: Images of the hotspot transfection sites after spinal CTb injections (6 VGaT, 6\n    VGluT2, 6 SerT mice; Methods, Mapping experiments). The paper reports no count; reproduced\n    when CTb and mCherry double-labelled neurons are present in each hotspot ipsilateral to the\n    spinal injection.\n- id: fig7-syp-targets\n  statement: Synaptophysin-labelled VGaT boutons from the slomo region densely innervate lamina\n    III, apposing large-fibre primary afferents and VGaT reporter neurons; VGluT2 boutons from the\n    shuffle region densely innervate area X, apposing cholinergic interneurons and commissural\n    VGluT2 interneurons.\n  source: Figure 7c-e; Results, Hotspots for slomo and shuffle walking target distinct neuronal\n    substrates, paragraph 2\n  quote: SYP + projections to lumbar segments confirmed dense innervation of lamina III from the\n    VGaT + slomo brainstem region and of area X from sites involving the VGluT2 + shuffle site.\n    VGaT SYP + boutons in lamina III derived from the slomo hotspot apposed CTb-labeled large fiber\n    primary (muscle) afferents and with L10-GFP + VGaT reporter neurons ( Fig. 7 ). VGluT2 SYP+\n    boutons in area X derived from the shuffle hotspot apposed cholinergic interneurons or L10-GFP\n    + VGluT2 reporter neurons that represented commissural interneurons\n  criterion: Confocal images of SYP-mCherry boutons with CTb, ChAT or L10-GFP labelling (Methods,\n    Spinal projections, Identification of neuronal sub-specialization). The paper reports\n    appositions without a count for these targets; reproduced when the images show these\n    appositions in the named laminae.\n- id: tables15-lamina-ix-gradient\n  statement: Ventral mRF VGaT sites caudal to the slomo center and VGluT2 sites rostral to the\n    shuffle center innervate lamina IX more heavily than the levels of the slomo and shuffle\n    centers.\n  source: Figure 7-Figure supplement 3d; Results, Hotspots for slomo and shuffle walking target\n    distinct neuronal substrates, paragraph 2; Table S15 (Fig. 15 d)\n  quote: Quantification of bouton-like profiles in lamina IX derived from different levels in the\n    ventral mRF using confocal imaging confirmed that more caudal VGaT and more rostral VGluT2\n    sites more heavily innervated lamina IX than levels representing the centers of slomo and\n    shuffle sites\n  statistics:\n  - about: one-way ANOVA over the four groups\n    test: Ordinary One Way Anova\n    statistic: F (3, 23) = 10.70\n    p: 0.0001\n    n: 4-9 sections per mouse, representative mice per genotype per level\n  - about: VGaT rostral against VGaT intermediate\n    test: Tukey's multiple comparisons test\n    p: 0.0002\n  - about: VGluT2 rostral against VGluT2 intermediate\n    test: Tukey's multiple comparisons test\n    p: 0.23\n  criterion: SYP+ bouton-like profiles in lamina IX per standardized volume (compressed 8 um x\n    142.7 um x 142.7 um stacks, 4 to 9 sections per mouse), one-way ANOVA with Tukey's test\n    (Table S15). Table S15 labels the groups VGaT and VGluT2 \"rostral\" and \"intermediate\"\n    without saying which is a hotspot center; the readings are (a) VGaT rostral and VGluT2\n    intermediate are the slomo and shuffle centers, so the comparisons are VGaT intermediate\n    against VGaT rostral and VGluT2 rostral against VGluT2 intermediate; (b) the hotspot\n    centers are the levels with the fewest lamina IX boutons in each genotype. Reproduced when\n    the ANOVA gives p < 0.05 and both comparisons show more boutons off center with p < 0.05;\n    partially reproduced when only one does. The paper's own table gives p 0.23 for the VGluT2\n    comparison under reading (a).\n- id: tables15-c-boutons\n  statement: The shuffle hotspot innervated lamina IX sparsely, apposing large cholinergic C\n    boutons more than motoneurons, and the differential innervation of motoneurons and\n    cholinergic boutons by VGaT and VGluT2 sites was confirmed at the group level.\n  source: Figure 7-Figure supplement 3c; Results, Hotspots for slomo and shuffle walking target\n    distinct neuronal substrates, paragraph 3; Table S15 (Fig. 15 c)\n  quote: This differential innervation of motoneurons and cholinergic boutons was confirmed with\n    quantification at the group level\n  statistics:\n  - about: one-way ANOVA over genotype by target\n    test: Ordinary One Way Anova\n    statistic: F (5, 30) = 14.69\n    p: 0.0001\n    p_relation: \"<\"\n  - about: VGluT2 C-bouton against VGaT C-bouton appositions\n    test: Sidak's multiple comparisons test\n    p: 0.03\n    n: 2 slices per mouse from 3 VGaT-ires-cre and 3 VGluT2-ires-cre mice\n  criterion: SYP+ profiles apposed to ChAT-IR motoneuron somata, dendrites or C-boutons in lamina\n    IX, per 0.8 um confocal slice, 2 slices per mouse (Figure 7-Figure supplement 3c); one-way\n    ANOVA with Sidak's test (Table S15). Reproduced when the ANOVA gives p < 0.05 and VGluT2\n    sites have more C-bouton appositions than VGaT sites with p < 0.05.\n- id: fig7-bouton-size\n  statement: The few lamina IX boutons from the slomo hotspot apposed motoneuron dendrites and had\n    a mean diameter of 2.48 um, while ventral VGaT sites lateral or caudal to the hotspot densely\n    innervated motoneuron somata with smaller boutons (1.40 um).\n  source: Results, Hotspots for slomo and shuffle walking target distinct neuronal substrates,\n    paragraph 3\n  quote: The few boutons in lamina IX derived from the slomo hotspot apposed motoneuronal dendrites\n    and had an average diameter of 2.48µm+/-0.42µm. In contrast, ventral VGaT mRF sites lateral or\n    caudal to the slomo hotspot densely innervated motoneuron somata with smaller bouton size\n    (1.40µm +/-0.32µm)\n  expected:\n  - quantity: mean bouton diameter, slomo hotspot, lamina IX\n    value: 2.48\n    tolerance: 0.42\n    unit: um\n  - quantity: mean bouton diameter, VGaT sites lateral or caudal to the hotspot, lamina IX\n    value: 1.40\n    tolerance: 0.32\n    unit: um\n  criterion: Bouton diameter measured on confocal slices (Methods, Spinal projections,\n    Identification of neuronal sub-specialization). Tolerances are the SDs the paper gives with\n    the means. Reproduced when both means are within tolerance and the hotspot boutons are\n    larger.\n- id: fig8b-lamina-iii-boutons\n  statement: VGaT hM3Dq-mCherry bouton counts per standardized volume were higher in slomo (high Z\n    SwT) than in non-slomo mice only in lamina III of the lumbar cord.\n  source: Figure 8b; Results, May sensory gating contribute to prolongation of swing time in\n    slomo walking?; Table S16\n  quote: Bouton counts per standardized volume were higher in slomo than non-slomo mice only in\n    lamina III\n  statistics:\n  - about: Z-score group main effect\n    test: 2 way ANOVA\n    statistic: F (1, 48) = 6.227\n    p: 0.02\n    n: 5 high and 5 low Z SwT mice, 6 regions\n  - about: lamina III, high against low Z SwT\n    test: Sidak's multiple comparisons test\n    p: 0.016\n    n: 5 high and 5 low Z SwT mice\n  depends_on:\n  - zscore-subgroups\n  criterion: Bouton-like profiles counted in 6 regions (lamina I-II, III-IV, lateral V, VIII, IX,\n    area X) from 3 lumbar sections per mouse, z-stacks of 10 slices of 0.8 um compressed by\n    standard deviation (Methods, Spinal projections, Density measurements); two-way ANOVA (Z\n    group by region) with Sidak's test at alpha 0.05. Groups are the 5 high (Z SwT 2.6 to 5.7)\n    and 5 low (0.2 to 1.9) mice of Table S16. Reproduced when lamina III is higher in the high\n    group with Sidak p < 0.05 and no other region gives p < 0.05.\n- id: fig8c-lamina-iii-correlation\n  statement: Z SwT correlated positively with mCherry bouton density in lamina III (r 0.65) but\n    not in other regions; the correlation trend was negative for lamina IX.\n  source: Figure 8c-d; Results, May sensory gating contribute to prolongation of swing time in\n    slomo walking?; Table S16\n  quote: In addition, Z SwT correlated significantly and positively with bouton density in this\n    region, but not in other regions. The correlation trend was negative for lamina IX\n  statistics:\n  - about: lamina III\n    test: Pearson correlation\n    statistic: r = 0.65\n    p: 0.04\n    ci:\n      level: 0.95\n      low: 0.02904\n      high: 0.9071\n    n: 10 mice\n  - about: lamina IX\n    test: Pearson correlation\n    statistic: r = -0.33\n    p: 0.35\n    ci:\n      level: 0.95\n      low: -0.7942\n      high: 0.3789\n    n: 10 mice\n  expected:\n  - quantity: Pearson r, Z SwT against lamina III bouton count\n    value: 0.65\n    tolerance: 0.065\n  depends_on:\n  - zscore-subgroups\n  - fig8b-lamina-iii-boutons\n  criterion: Per-mouse bouton counts as in fig8b-lamina-iii-boutons; Pearson correlation with Z\n    SwT over the 10 mice (Methods). Reproduced when lamina III gives p < 0.05 with r within\n    tolerance, no other region gives p < 0.05, and lamina IX has r < 0.\n- id: fig8f-von-frey\n  statement: In VGaT slomo mice (Z SwT > 2) CNO reduced the response rate to the 1 g and 2 g von\n    Frey filaments compared to saline; WT controls were unaffected.\n  source: Figure 8f; Results, May sensory gating contribute to prolongation of swing time in\n    slomo walking?; Table S17\n  quote: VGaT hM3Dq activation in Z SwT >2 mice reduced the response rate to von Frey filaments\n    that produce mild pressures of 1 and 2g\n  statistics:\n  - about: treatment effect, Z SwT > 2\n    test: 2 way RM ANOVA\n    statistic: F (1, 8) = 8.490\n    p: 0.02\n    n: 9 mice with Z SwT > 2\n  - about: filament by treatment interaction, Z SwT > 2\n    test: 2 way RM ANOVA\n    statistic: F (3, 24) = 4.344\n    p: 0.01\n    n: 9 mice\n  - about: 1 g filament, saline against CNO\n    test: Sidak's multiple comparisons test\n    ci:\n      level: 0.95"
}
```

Result: not kept, because it reads the paper's text.

## Prompt

Your response above was stopped by a safety classifier — this is not a tool or API error. The rest of it was withheld, and tool calls in it that had not finished did not run. Do not produce that content again, even reworded.

**Agent**

I didn't write a claims file. The response that was writing `claims/002010/10.1101-2023.04.19.537568.yaml` was stopped by a safety classifier before the file was saved. I was told not to produce that content again, so nothing is under `claims/002010/` and the quote checker was never run.

**What I read before it stopped:**
- **Text:** `paper/10.1101-2023.04.19.537568.txt`, the bioRxiv preprint, version 1, from the JATS XML. It has the main text, Methods, figure legends and figure supplement legends. It now also includes both supplement PDFs: the supplementary figures (media-1) and Supplementary Tables S1 to S18 (media-2). Those tables were missing in the earlier run, and they hold the statistics for nearly every finding. There is still no PDF of the main text.
- **Code:** the two SourceForge projects the paper links, with files dated 2023-04-14. SourceForge shows no commit for them, so I recorded checksums instead.
  - `gait-analysis-gui` is MATLAB. It scores footfalls on the video and turns them into stride metrics, using 119.88 fps and skipping trials with fewer than 3 strides in any limb. It exports these for GraphPad. Two functions it calls, `calcSpeed` and `calcTimeCoupling`, are not in the archive.
  - `gait-emg-step-trigger` is a Spike2 script that fires optogenetic pulses when it detects a TA EMG burst.
  - Neither project contains the statistics, the Z-scores or the curve fits.

**Still missing from the paper:**
- **The Z-score equation.** In the Methods, section (a), the sentence ends "calculated as follows:" and no formula follows. Every subgroup in the paper is defined by Z SwT or Z StrV. I had planned to name two readings: Z = (the mouse's change − the WT mean change) / the WT SD, with the change taken either as CNO minus saline or as a relative change. Whether to pool strides across sessions or average session means is also open.
- **The regression models behind the walking-signature F-tests.** The paper only cites its reference 36. The degrees of freedom in Tables S3, S8 and S12 imply a 2-parameter model for most metrics and a 4-parameter model for stance time. I had planned to name linear, power and semilog readings for the first, and polynomial or logistic readings for the second.

**Counts:** 0 claims, so none with quotes, statistics or criteria.

To get the file written, someone needs to start a new claims run, which could reuse the reading above. Alternatively, a person can write the file.

## End of run

39 turns, 11 minutes, result: success.
