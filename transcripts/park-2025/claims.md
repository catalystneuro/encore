# 001266 · claims · run 39784956223

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 paper claims/001266 2>&1
```

```
Exit code 2
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
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -200; wc -l paper/*.txt; head -30 paper/10.1038-s41467-025-55819-9.txt; head -15 paper/10.1101-2023.06.02.543490.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,140p claims/001453/*.yaml; grep -n "^  [a-z_]*:" claims/001453/*.yaml | awk -F: '{print $3}' | sort | uniq -c
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
f=claims/001453/*.yaml; grep -oE "^ *[a-z_]+:" $f | sort | uniq -c; tail -40 $f; cat tools/claims_check.py | head -80
```

```
1     corrected:
      9     n:
     14     p:
     12     p_relation:
      2     test:
      4     tolerance:
      4     unit:
      4     value:
      1   archive:
      9   criterion:
      8   data:
      7   depends_on:
      2   expected:
      1   id:
      1   kind:
     19   quote:
     20   source:
     20   statement:
     13   statistics:
      1 claims:
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"
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
[... 82 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -c 3000 paper/10.1101-2023.06.02.543490.txt; echo; echo ----; head -c 1500 paper/10.1038-s41467-025-55819-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/10.1038-s41467-025-55819-9.txt; grep -n "^=\+\|SUPPLEMENT\|supp[0-9]" paper/10.1038-s41467-025-55819-9.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-025-55819-9.txt",
 "limit": 572
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk 'NR<=572{print NR": "length($0)}' paper/10.1038-s41467-025-55819-9.txt | sort -t: -k2 -n -r | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7p paper/10.1038-s41467-025-55819-9.txt | fold -s -w 200 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; sed -n '8,30p' paper/10.1038-s41467-025-55819-9.txt | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 200
}
```

```
1	2873 ncomms Nature Communications Nat Commun Nature Publishing Group PMC11794848 11794848 11794848 39905023 10.1038/s41467-025-55819-9 Dendritic excitations govern back-propagation via a spike-rate 
2	accelerometer Park Pojeong 1 5 # Wong-Campos J David 1 # Itkis Daniel G 1 Lee Byung Hun 1 Qi Yitong 1 Davis Hunter C 1 Antin Benjamin 2 Pasarkar Amol 2 Grimm Jonathan B 3 Plutkis Sarah E 3 Holland 
3	Katie L 3 Paninski Liam 2 Lavis Luke D 3 Cohen Adam E 1 4 ✉ 1 Department of Chemistry and Chemical Biology, Harvard University, Cambridge, MA USA 2 Departments of Statistics and Neuroscience, 
4	Columbia University, New York, NY USA 3 Janelia Research Campus, Howard Hughes Medical Institute, Ashburn, VA USA 4 Department of Physics, Harvard University, Cambridge, MA USA 5 Present Address: 
5	Department of Brain Sciences, DGIST, Daegu, Republic of Korea ✉ Corresponding author. # Contributed equally. 4 2 2025 16 1333 1333 5 2 2025 © The Author(s) 2025 Open Access This article is licensed 
6	under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as 
7	long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
8	permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative 
9	Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory 
10	regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/ 
11	
[... 189 more lines not kept]
```

**Agent**

The version of record text with its supplement is present. Reading the rest of the main text and Methods.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 200,
 "limit": 200
}
```

```
200	in 87 ms. For ‘EFS after bAPs’, the amplification decayed exponentially with a time constant of 35 ms. These findings are consistent with prior results showing that when presynaptic inputs are paired 
201	with postsynaptic bursts, hippocampal LTP can occur for either relative timing of pre- and post-synaptic activity 31 , 52 . We then tested how the number of optogenetically evoked bAPs affected the 
202	nonlinear amplification. Triggering a single bAP by a 10 ms optogenetic stimulus targeted to the soma did not evoke a nonlinear dendritic response, regardless of timing relative to the EFS ( n = 5 
203	cells from 4 animals; Fig. 5c, d ). We conclude that at least one bAP-evoked sodium dSpike was necessary to create a plateau potential. In our model, Na V -mediated dSpikes are a necessary trigger 
204	for plateau potentials. This model makes a counterintuitive prediction: if there is a sustained train of somatic spikes, and a distal synaptic input arrives after the dSpike window has closed 
205	( > 180 ms after spike-train onset), then this synaptic input will not be able to trigger a plateau potential despite coincidence with somatic spikes. We tested this prediction by stimulating the 
206	soma with gradual (3 s) optogenetic stimulus ramps, and delivering EFS at the beginning (0.5 s after ramp start) and end (2.5 s after ramp start) of the ramps (Fig. 5e ). The early EFS reliably 
207	evoked plateau potentials (AUC 5.6 ± 3.6, mean ± s.d.), whereas the late EFS, which occurred when the average spike rate was 24 ± 4 Hz (mean ± s.d.), did not (AUC 1.6 ± 1.0, mean ± s.d., n = 7 cells 
208	from 5 animals, p = 0.01, paired t-test, Fig. 5f ). These experiments illustrate the important contribution of the dendritic spike-rate accelerometer to formation of plateau potentials: coincidence 
209	of distal synaptic inputs with somatic spikes alone was not sufficient to induce a plateau potential; rather, distal synaptic inputs had to coincide with onset of rapid somatic spi
[... 190 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 400,
 "limit": 172
}
```

```
400	optogenetic stimulation, so our model did not contain VGCC or NMDAR conductances. Table 1 shows values of the model parameters. Table 1 Ion channel densities in a model CA1 pyramidal cell. Channel 
401	models were adapted from Ref. 49 Dendritic properties Channel Name Proximal (mS/cm 2 ) Distal (mS/cm 2 ) d 1/2 (μm) z (μm) Na V ( ḡ NaV ) 50 47 300 100 A-type K V ( ḡ KA ) –200 * 300 0 150 Delayed 
402	rectifier K V ( ḡ KDR ) 40 40 N/A N/A Na V slow inactivation ( s max ) 0% 60% 300 100 Axonal properties Channel properties Parameters Location Na V ( ḡ NaV ) 30 S/cm 2 Nodes of Ranvier Na V ( ḡ NaV ) 
403	15 S/cm 2 Axon initial segment Na V ( ḡ NaV ) 50 mS/cm 2 Axon (other segments) A-type K V ( ḡ KA ) 9.6 mS/cm 2 Nodal and internodal compartments A-type K V ( ḡ KA ) 48 mS/cm 2 Axon (AIS and hillock) 
404	Membrane capacitance ( C m ) 0.04 μF/cm 2 Internodal compartments, myelinated Constitutive properties Membrane capacitance ( C m ) 1.5 μF/cm 2 All compartments except axon Specific membrane 
405	resistance ( R m ) 80,000 Ω·cm 2 Uniform, leak conductance Specific axial resistance of the cytoplasm ( ρ ) 200 Ω·cm Uniform * Since the conductance is only evaluated for d > 0 in Eq. 1 , g KA > 0 
406	everywhere. Parameters d 1/2 and z are defined in Eq. 1 . For voltage-gated channels, the maximum channel conductance densities were modeled as sigmoidal functions of the contour distance, d , from 
407	the soma. These sigmoid distributions take the general form shown in Eq. 1 , with asymptotic densities g Prox and g Distal , a half-way distance d 1/2 (where the density is ( g Prox + g Distal )/2) 
408	and a steepness parameter z . 1 g d = g P r o x + g D i s t a l − g P r o x ⋅ 1 + exp d − d 1 / 2 z − 1 The g parameters were selected to agree with literature values 22 , while the other parameters 
409	were adjusted to match our data. Fig. S19a–c show channel densities of Na V and A-type K V across the neuron morphology after tuning to match our data. For temperature-dependen
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "^=== \|^\[\|^---\|^#" 10.1038-s41467-025-55819-9.txt | grep -v "=== page" | head -40
```

```
6:------------------------------------------------------------------------
9:[HYPERLINKS]
363:[1] Golding, N. L. & Spruston, N. Dendritic sodium spikes are variable triggers of axonal action potentials in hippocampal CA1 pyramidal neurons. Neuron 21, 1189–1200 (1998). 10.1016/S0896-6273(00)80635-2
365:[2] Magee, J. C. & Johnston, D. Characterization of single voltage‐gated Na+ and Ca2+ channels in apical dendrites of rat CA1 pyramidal neurons. J. Physiol. 487, 67–90 (1995). 10.1113/jphysiol.1995.sp020862
367:[3] Larkum, M. E., Zhu, J. J. & Sakmann, B. A new cellular mechanism for coupling inputs arriving at different cortical layers. Nature 398, 338–341 (1999). 10.1038/18686
369:[4] Golding, N. L., Jung, H., Mickus, T. & Spruston, N. Dendritic calcium spike initiation and repolarization are controlled by distinct potassium channel subtypes in CA1 pyramidal neurons. J. Neurosci. 19, 8789–8798 (1999). 10.1523/JNEUROSCI.19-20-08789.1999
371:[5] Johnston, D., Magee, J. C., Colbert, C. M. & Cristie, B. R. Active properties of neuronal dendrites. Annu. Rev. Neurosci. 19, 165–186 (1996). 10.1146/annurev.ne.19.030196.001121
373:[6] Hausser, M., Spruston, N. & Stuart, G. J. Diversity and dynamics of dendritic signaling. Science 290, 739–744 (2000). 10.1126/science.290.5492.739
375:[7] Spruston, N. Pyramidal neurons: dendritic structure and synaptic integration. Nat. Rev. Neurosci. 9, 206–221 (2008). 10.1038/nrn2286
377:[8] Major, G., Larkum, M. E. & Schiller, J. Active properties of neocortical pyramidal neuron dendrites. Annu. Rev. Neurosci. 36, 1–24 (2013). 10.1146/annurev-neuro-062111-150343
379:[9] Takahashi, H. & Magee, J. C. Pathway interactions and synaptic plasticity in the dendritic tuft regions of CA1 pyramidal neurons. Neuron 62, 102–111 (2009). 10.1016/j.neuron.2009.03.007
381:[10] Brandalise, F., Carta, S., Helmchen, F., Lisman, J. & Gerber, U. Dendritic NMDA spikes are necessary for timing-dependent associative LTP in CA3 pyramidal cells. Nat. Commun. 7, 13480 
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '565,580p' paper/10.1038-s41467-025-55819-9.txt | cut -c1-300; grep -n "SUPPLEMENT\|supp[1-4]\|^\[Supp" paper/10.1038-s41467-025-55819-9.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^##### Supplement" paper/10.1038-s41467-025-55819-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-025-55819-9.txt",
 "offset": 571,
 "limit": 540
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1110,1130p;1975,2019p' paper/10.1038-s41467-025-55819-9.txt | cut -c1-400
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement are all present. The peer review file comes next, checked for method details.

**Agent calls Bash**

```bash
sed -n '1130,1975p' paper/10.1038-s41467-025-55819-9.txt | grep -n -i "threshold\|dspike prob\|defin\|criteri\|bimodal\|code\|DANDI\|github" | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1130,1975p' paper/10.1038-s41467-025-55819-9.txt | grep -n -i -B2 -A4 "high-pass\|FWHM\|full width\|300 \?µm\|300 \?μm\|AUC\|area under" | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001266/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001266/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'));print(m.get('version'))"
```

Result: the fetched text is not kept.

**Agent**

The dataset description says a Source Data file on the journal site maps the DANDI files to figure panels. Next, the paper's supplementary simulation code.

**Agent calls Bash**

```bash
cd $TMPDIR; for n in 7 8 10; do for ext in zip m xlsx rar; do u="https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-025-55819-9/MediaObjects/41467_2025_55819_MOESM${n}_ESM.$ext"; c=$(curl -s -o /dev/null -w "%{http_code}" "$u"); echo "$n $ext $c"; done; done
```

```
7 zip 200
7 m 403
7 xlsx 403
7 rar 403
8 zip 200
8 m 403
8 xlsx 403
8 rar 403
10 zip 403
10 m 403
10 xlsx 200
10 rar 403
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; b="https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-025-55819-9/MediaObjects/41467_2025_55819_MOESM"; curl -s -o s7.zip ${b}7_ESM.zip; curl -s -o s8.zip ${b}8_ESM.zip; curl -s -o sd.xlsx ${b}10_ESM.xlsx; sha256sum s7.zip s8.zip sd.xlsx; unzip -l s7.zip; unzip -l s8.zip
```

```
9eab52ac20d889991fc7ba5f24130d0d80f7d53c3ea69057c5af0f4007049249  s7.zip
a5a1b5930931d6b93dc6ee08e32a17e2e410fc6f9af78d6a0d5b6f3fc310c6b6  s8.zip
142a0621e8581da59891f5a9e0b9f86983b5c2f080d6fba617eb02130044774d  sd.xlsx
Archive:  s7.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2024-03-18 08:24   Supplementary NEURON models/Conductance-based model/
      113  2023-06-12 21:02   Supplementary NEURON models/Conductance-based model/delete_neuron.py
   376942  2024-03-03 20:10   Supplementary NEURON models/Conductance-based model/FullCA1Model.py
     6841  2024-03-03 19:55   Supplementary NEURON models/Conductance-based model/main.py
        0  2024-03-18 08:24   Supplementary NEURON models/Conductance-based model/Model Robustness/
        0  2024-03-18 08:24   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/
     1532  2023-01-06 05:32   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/ampa_forti.mod
      813  2023-05-19 22:56   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/cacum.mod
     2522  2023-05-18 11:49   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/cad.mod
     1817  2023-09-29 23:47   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/cagk.mod
     2789  2023-09-29 23:45   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/cal.mod
     2057  2023-09-29 23:46   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/calH.mod
     1981  2023-09-29 23:43   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/car.mod
     1453  2023-01-06 05:32   Supplementary NEURON models/Conductance-based model/Model Robustness/ChannelsUnused/car_mag.mod
[... 98 more lines not kept]
```

**Agent**

The supplementary code is simulation only (NEURON and Izhikevich models), with no analysis code. Next, the Source Data workbook's layout.

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "
import openpyxl
wb=openpyxl.load_workbook('sd.xlsx',read_only=True,data_only=True)
for ws in wb.worksheets:
    rows=list(ws.iter_rows(values_only=True))
    print('==',ws.title,len(rows))
    for r in rows[:6]: print([c for c in r if c is not None][:12])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import openpyxl
ModuleNotFoundError: No module named 'openpyxl'
```

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p sdx; cd sdx; unzip -o -q ../sd.xlsx; ls xl/worksheets; python - <<'E'
import re
wb=open('xl/workbook.xml').read()
print(re.findall(r'<sheet [^>]*name="([^"]+)"',wb))
ss=open('xl/sharedStrings.xml').read()
strs=[re.sub(r'<[^>]+>','',m) for m in re.findall(r'<si>(.*?)</si>',ss,re.S)]
print(len(strs))
for s in strs[:150]: print(repr(s[:160]))
E
```

```
_rels
sheet1.xml
sheet10.xml
sheet11.xml
sheet12.xml
sheet2.xml
sheet3.xml
sheet4.xml
sheet5.xml
sheet6.xml
sheet7.xml
sheet8.xml
sheet9.xml
['Raw data in Dandi_Archive', 'Figure 5', 'Figure 6', 'Supplementary Fig 1', 'Supplementary Fig 2', 'Supplementary Fig 3', 'Supplementary Fig 12', 'Supplementary Fig 16', 'Supplementary Fig 17', 'Supplementary Fig 18', 'Supplementary Fig 24', 'Supplementary Fig 25']
306
'Control'
'Figure 5b'
'Figure 5h'
'Figure 6b'
'Opto'
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sdx; python - <<'E'
import re
ss=open('xl/sharedStrings.xml').read()
strs=[re.sub(r'<[^>]+>','',m) for m in re.findall(r'<si>(.*?)</si>',ss,re.S)]
for s in strs[150:]:
    if not s.startswith("'sub-"): print(repr(s[:160]))
E
```

```
'000820PP070_P17_V2_11_freq_opto_2khz'
'Patch clamp_1kHz (Fig. S2d)'
'/Volumes/Data-1/230902_PP070_P19_intrinsic_properties'
'150706PP070_P19_V2_14_freq_opto'
'/Volumes/Data-1/230903_PP070_P20_488_dmd_test'
'205240PP070_P20_Cel3_freq_opto'
'232204PP070_P17_V2_10_opto_ramp_step'
'/Volumes/Data-1/230918_PP070_P16_488_dmd_test'
'215254PP070_P16_Cell1_opto_freq_ctx'
'004720PP070_P17_V2_12_freq_opto'
'212457PP070_P20_Cell4_freq_opto'
'Patch clamp_2kHz (Fig. S2d)'
'150945PP070_P19_V2_14_freq_opto_2kHz_594_inc'
'205908PP070_P20_Cel3_freq_opto_2khz'
'233122PP070_P17_V2_10_opto_ramp_step_2kHz'
'215422PP070_P16_Cell1_opto_freq_ctx_2kHz'
'004921PP070_P17_V2_12_freq_opto_2kHz_594_inc'
'212620PP070_P20_Cell4_freq_opto_2kHz'
'eYFP_calibration(Fig. S3b)'
'/Volumes/Data-1/230905_PP070_P10_488_dmd_test'
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; unzip -o -q s7.zip; unzip -o -q s8.zip; cat "Supplementary Izhikevich model/Two_compartment_Izhikevich.m"; sed -n 1,80p "Supplementary NEURON models/Conductance-based model/main.py"
```

```
% Two-compartment Izhikevich model of dendritic excitability in CA1
% pyramidal neurons
%
% Daniel Itkis, [removed: an e-mail address]
% Adam Cohen, [removed: an e-mail address]
% June 5, 2023

clear all;
close all;

%%
% Define parameters for the Izhikevich neuron model
a = 0.0025;
b = 0.01;
c = -55;
d = 1;

vmax = 0;
rho = 1;
cSoma = -65;
[... 161 more lines not kept]
```

**Agent**

I have what I need: no analysis code exists (only simulation code), and the Source Data index is the outside label source. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -o "Source data for Fig. 5[^.]*\.\|n = 8 neurons from 5 animals[^)]*)" main.txt | head; python - <<'E'
import re
t=open('paper/10.1038-s41467-025-55819-9.txt').read()
for k in ['3.6 ×10','255 ±','313 ±','141 ±','~80%','AUC 5.6','42 ± 7%','dendritic CheRiff currents','93% of the variance','s.e.m.) and for more']:
    i=t.find(k); print(repr(t[i-60:i+120]))
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001266/10.1038-s41467-025-55819-9.yaml",
 "content": "# Claims for Park, Wong-Campos et al. (2025), \"Dendritic excitations govern back-propagation via a\n# spike-rate accelerometer\", Nat Commun 16, 1333, on dandiset 001266.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, protocol\n# version pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record (PMC11794848, Europe PMC full text) with its Supplementary\n# Information (Figs. S1 to S25, MOESM1), the Peer Review File (MOESM2), the Description of Additional\n# Supplementary Files (MOESM3) and the Reporting Summary (MOESM9, no text extracted). The file\n# paper/10.1101-2023.06.02.543490.txt is an earlier bioRxiv preprint with a different title and was\n# not used.\n#\n# Code read: the paper links no analysis code (\"All analysis was performed in MATLAB\"; the analysis\n# scripts are not published). It links simulation code only, as Supplementary Software, read from\n# the journal's static content (no repository or commit exists):\n#   Supplementary Software 1, 41467_2025_55819_MOESM7_ESM.zip (sha256 9eab52ac...7049249): the\n#     NEURON conductance-based CA1 model (main.py, run_simulation.py, parameters_list.py, mod files,\n#     MATLAB plotting of Figs. S19 and S20 phase diagrams).\n#   Supplementary Software 2, 41467_2025_55819_MOESM8_ESM.zip (sha256 a5a1b593...0c6b6): the\n#     two-compartment Izhikevich model, Two_compartment_Izhikevich.m. It differs from the Methods\n#     and Fig. S21 in two details: somatic reset -65 (Fig. S21a gives vrs = -55) and initial\n#     dendritic u = -18 (Methods give -13). The Methods' values are the main reading; the code's are\n#     a variant.\n# Neither holds any method for the analysis of the recordings.\n#\n# Outside material the dataset needs: the Source Data file, 41467_2025_55819_MOESM10_ESM.xlsx\n# (https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-025-55819-9/MediaObjects/\n# 41467_2025_55819_MOESM10_ESM.xlsx, sha256 142a0621e8581da59891f5a9e0b9f86983b5c2f080d6fba617eb02130044774d).\n# The dandiset's description names it as \"an index mapping files on DANDI to paper figure panels\".\n# Its sheet \"Raw data in Dandi_Archive\" maps each DANDI file name (sub-...) to a figure panel; its\n# other sheets give per-cell values for Figs. 5b, 5f, 5h, 6b, S1c, S2d, S3f, S12c, S16d, S16g, S17d,\n# S18e, S18h, S24 and S25f, g. The index lists example recordings for Figs. 1c-f, 2, 3, 4a, 4c-d,\n# 5a, 5c, 5e, 5g, 6a, S2, S3b, S4a, S4e, S5a, S13a, S14a-c, S15, S16-S18, S22 and S25. Only the\n# index sheet was read here, for its panel names; no recording was opened.\n#\n# The data the paper reports: acute coronal hippocampal slices (300 µm) from CD1 mice of either sex,\n# 2 to 4 postnatal weeks, after in utero electroporation of Optopatch-V (LR-Voltron2 with\n# LR-CheRiff-eYFP), dye JFX608. CA1 pyramidal neurons were imaged at 34 °C on a custom 1-photon\n# microscope with micromirror-patterned 594 nm voltage imaging, at 1 kHz unless stated (2 kHz in\n# Fig. S2), and patterned 488 nm optogenetic stimulation; with 2-photon or HiLo structural images;\n# in some cells whole-cell patch clamp at the soma (100 kHz). The experiments and their samples:\n# branch, soma and soma plus dendrite stimulation (20 ms, 5 Hz, 54 trials; 17 neurons, 15 animals;\n# Figs. 2, 3, S8 to S12); dendrite stimulation distance series (35 dendrites, 13 cells, 11 animals,\n# Fig. 3i); ramps (188 ramps, 56 cells, 44 animals, Fig. S13); steps (43 stimulated branches, 16\n# cells, 13 animals, Fig. 4b); wide-field stimulation (9 cells, 9 animals, Fig. 4c-e); patch current\n# pulses 3 to 100 Hz (29 recordings, 14 cells, 11 animals, Fig. S14); drugs on dSpikes (BaCl2 9\n# cells, 4-AP 4 cells, TTX 4 cells, Ni2+ 5 and 6 cells; Figs. S16 to S18); plateau experiments with\n# electric field stimulation (EFS) of the temporoammonic path with picrotoxin and 1 mM Mg2+ (28\n# cells, 12 animals, Fig. 5b; timing 8 and 5 cells, Fig. 5d; ramps and steps 7 or 8 cells, 5 animals,\n# Fig. 5e-h; drugs D-AP5 6, TTX 4, Ni2+ 4, vehicle 11 cells, Fig. 6); temperature 34 against 24 °C\n# (6 cells, 4 animals, Fig. S25); validation (Figs. S1 to S5). The measured variables are the\n# camera movies (Voltron2 fluorescence, which falls with depolarization), the stimulus timing and\n# patterns, eYFP images, structural images, and patch clamp current and voltage. The dandiset's\n# description gives the patch clamp channel scalings.\n#\n# Shared method, from the Methods unless marked; criteria refer to it.\n#   Fluorescence is taken from regions of the raw movie (not the PCA-denoised or 3D-reconstructed\n#   maps, Results paragraph 3), either by the maximum-likelihood pixel weighting of ref. 33 or by\n#   the unweighted mean of a user-drawn region (\"These two approaches gave similar results\"), and\n#   photobleaching is corrected by dividing by a regression fit to the mean fluorescence.\n#   Depolarization is -dF (Voltron2 fluorescence falls with voltage).\n#   Every somatic spike is a bAP. Spikes are found by high-pass filtering and a threshold with a\n#   maximum; the threshold was set by hand. dSpikes are found the same way in a distal region,\n#   typically > 300 µm from the soma, as large narrow events, typically < 5 ms full width at half\n#   maximum. Distances are measured in the image plane, ignoring z.\n#   Open, none of the paper, its legends, its supplement or its code fixes them:\n#   (1) The high-pass filter. Readings run: (a) subtraction of a 20 ms moving median; (b) a\n#       zero-phase Butterworth high-pass at 20 Hz. Both are standard choices that keep events\n#       shorter than 5 ms.\n#   (2) The dSpike threshold. The paper's reading, shown in Figs. 2b and S10c, is a threshold\n#       between the two modes of the distal amplitude histogram; it is placed at the histogram's\n#       trough for each recording, and the FWHM < 5 ms rule is applied.\n#   (3) Which distal event belongs to which bAP. Standard choice that cannot change a count by more\n#       than chance overlaps: the distal peak within 5 ms after the somatic peak.\n#   (4) The somatic spike threshold. Standard choice: 5 times the robust s.d. of the filtered\n#       trace; the paper reports zero false positives and negatives at the soma (Fig. S2), so this\n#       cannot change the outcome.\n#   Area under the curve (AUC) is the time integral of -dF in a distal dendrite > 200 µm from the\n#   soma (Methods; Figs. 5c, 6a, S24). The integration window is open. Readings: (a) from stimulus\n#   onset until the cumulative area stops rising (the cumulative curve of Fig. S22a); (b) from\n#   stimulus onset to the end of the stimulus epoch before the next stimulus.\n#   Statistics: two-tailed paired or unpaired Student's t-tests, or one-way ANOVA with Bonferroni's\n#   post hoc test (Methods, Statistics).\n#\n# Data: claims on one example recording use the dataset with the Source Data index as labels\n# (with_labels, depending on source-data-index). Claims on pooled recordings use the dataset; the\n# paper gives no list of the pooled recordings, and finding them is the author's. Simulation claims\n# use the paper's Supplementary Software (with_inputs).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001266\"\npaper: doi:10.1038/s41467-025-55819-9\nclaims:\n- id: source-data-index\n  kind: link\n  statement: The dandiset's files are the recordings the paper's Source Data index assigns to\n    figure panels, so that example panels can be found by file name.\n  source: Data availability; Source Data file, sheet \"Raw data in Dandi_Archive\"; dandiset description\n  quote: The voltage imaging data generated in this study are on the DANDI archive under accession\n    code 001266\n  data: with_labels\n  criterion: Files are matched by the name in the index's column \"File name on DandiArchive\"\n    against the dandiset's subject and session names. Reproduced when every file the index names\n    is found; partially reproduced when at least half are; not reproduced otherwise. Where the\n    index's file name and the legend's label differ (Fig. 2 \"D1 stim\" is listed as file ..._D3;\n    Fig. 3 lists files D1, D2, D4, soma and D4+soma for the legend's D2, soma and Soma + D2), the\n    file for each panel is the one whose trial and event counts match the legend (54 trials each;\n    Fig. 2, 8 dSpikes; Fig. 3 D2, 49 -dSpikes and 35 +dSpikes; soma, 161 and 6; Soma + D2, 116 and\n    54; Fig. S8a, 80 and 12; Fig. S8c-d D4, 85 and 11). The readings for the legend's D2 are (a)\n    file D2 and (b) file D4 (the combined file is named D4+soma); both are reported.\n- id: fig2a-dspike-dichotomy\n  statement: In the Fig. 2 neuron, stimulation of proximal oblique dendrites evoked two somatic\n    spikes per trial; in most trials the distal dendrites showed only an attenuated copy, and in 8\n    of 54 trials a single rapid dSpike, always on the second somatic spike.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 1; Figure 2a, 2c\n  quote: Each stimulus evoked two spikes at the soma ... in some cases (8 of 54 trials), the dendrites\n    produced a single rapid spike ... the dendritic excitations always emerged from the second\n    somatic spike, never the first\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: trials with a dSpike, of 54\n    value: 8\n    tolerance: 0.8\n  criterion: In the Fig. 2 recording (index entry \"branch_stim (Fig.2)\"), bAPs and dSpikes are\n    counted per trial as in the shared method, distal region > 300 µm (legend). Reproduced when\n    the count is within tolerance under both filter readings and no dSpike follows the first\n    somatic spike of a trial.\n- id: fig2b-bimodal-distal-amplitudes\n  statement: Spike amplitudes have a unimodal distribution at the soma and a bimodal one in the\n    distal dendrite.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 1; Figure 2b\n  quote: A histogram of event amplitudes in the soma and dendrites showed a unimodal distribution at\n    the soma and a clearly bimodal distribution in the distal dendrites\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The paper names no test of modality. For the Fig. 2 recording, the amplitude (-dF/F at\n    the bAP's peak) of every bAP at the soma and in the distal region (> 300 µm). Readings, from\n    the figure (a histogram with a threshold between two groups) and two standard tests, (a)\n    Hartigan's dip test, p < 0.05 for the distal amplitudes and p >= 0.05 for the soma; (b) a\n    two-component Gaussian mixture preferred over one component by BIC in the distal amplitudes\n    and not at the soma. Reproduced when both readings agree that the distal distribution is\n    bimodal and the somatic one is not; when they differ, methods_underspecified.\n- id: fig2e-f-dspike-maps\n  statement: bAPs without a dSpike are confined to the soma and proximal dendrites, while bAPs with\n    a dSpike are amplified in the distal dendrites.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 2; Figure 2e, 2f\n  quote: In the -dSpike trials the bAP was primarily confined to the soma and proximal apical and\n    basal dendrites ... In the +dSpike trials, the depolarization was amplified in the distal\n    dendrites\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: For the Fig. 2 recording, spike-triggered averages of -dF normalized by dF_ref (the\n    fluorescence change during the passive return to baseline, Methods; Fig. 1d legend, mean from\n    10 to 20 ms after the spike) along the apical trunk in 10-pixel segments (Methods,\n    Kymographs). Reproduced when the -dSpike average at > 300 µm is below half its value at the\n    soma and the +dSpike average at > 300 µm is at least its value at the soma. The paper gives\n    no number; half and equal are the readings of \"confined\" and \"amplified\" used here, and the\n    ratios are reported.\n- id: fig2h-length-constant\n  statement: The peak amplitude of bAPs without a dSpike decays exponentially along the apical trunk\n    with a length constant of 255 ± 10 µm (mean ± s.e.m., 93 spikes).\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 2; Figure 2h\n  quote: Plots of the peak spike amplitude along the apical trunk showed exponential decay of the\n    -dSpike events (length constant 255 ± 10 μm, mean ± s.e.m., n = 93 spikes)\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: length constant of -dSpike bAP amplitude along the apical trunk\n    value: 255\n    tolerance: 10\n    unit: µm\n  criterion: Tolerance is the paper's s.e.m. The amplitude (-dF/F_ref) of each -dSpike bAP in\n    10-pixel segments along the trunk is fitted with an exponential in distance from the soma, one\n    fit per spike, and the length constants are averaged. Open, as the paper does not say, (1)\n    which 93 spikes; readings (a) the -dSpike bAPs of the Fig. 2 recording, (b) the -dSpike bAPs of\n    all Fig. 2 and Fig. 3 recordings of that neuron; (2) the fit; readings (a) A exp(-x/lambda),\n    (b) A exp(-x/lambda) + c. Reproduced when the mean is within tolerance under one reading of\n    (1) for both readings of (2), and each reading is shown.\n- id: fig3-subthreshold-no-dendritic-initiation\n  statement: Subthreshold depolarization follows the stimulus location and decays smoothly outside\n    it; dSpikes never initiated in the dendrites.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 3; Figure 3d-f, S10, S11\n  quote: We only observed diffusive-like propagation of the subthreshold voltages, never dSpikes that\n    initiated in the dendrites.\n  data: dataset\n  criterion: In the branch, soma and soma plus dendrite recordings, every dSpike is checked for a\n    somatic spike whose peak precedes the distal peak (shared method, item 3). Reproduced when no\n    dSpike lacks a preceding somatic spike.\n- id: fig3-two-motifs-location-independent\n  statement: Neurons produced only two kinds of excitation, perisomatic bAPs and distal dSpikes,\n    and neither spatial profile depended on which dendrite was stimulated.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 4; Figures S9 to S11\n  quote: the neurons produced precisely two kinds of excitations ... neither spatial profile depended\n    on the location of the driving stimulus\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The paper names no measure. For the neuron of Figs. 2, 3 and S8 (index entries\n    branch_stim), the -dSpike and the +dSpike spike-triggered amplitude profiles along the trunk\n    (-dF/F_ref, 10-pixel segments) for each stimulus location. Reproduced when, for each class,\n    every pair of locations' profiles has Pearson r >= 0.9 and the +dSpike profiles all exceed the\n    -dSpike profiles beyond 300 µm. The threshold 0.9 is a reading of \"precisely two kinds\", not\n    the paper's; the correlations are reported.\n- id: fig3h-dspike-peak-distance\n  statement: The amplitude of dSpikes relative to the first bAP peaks in the distal trunk, 313 ±\n    41 µm from the soma (mean ± s.d., 22 stimulated regions, 17 neurons).\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 4; Figure 3g, 3h\n  quote: was maximum in the distal dendritic trunk (313 ± 41 µm from the soma, mean ± s.d., n = 22\n    stimulated regions (soma or proximal branch), 17 neurons, 15 animals\n  data: dataset\n  expected:\n  - quantity: distance of peak dF_max/dF_1 from the soma\n    value: 313\n    tolerance: 41\n    unit: µm\n  criterion: Tolerance is the paper's s.d. For each recording with soma or proximal (< 200 µm)\n    stimulation, dF_1 is the amplitude of the first bAP after stimulus onset and dF_max the\n    amplitude of a later dSpike (Fig. 3h legend) in each trunk segment; the distance of the\n    segment with the largest ratio is taken, and the mean over stimulated regions is compared.\n    Open, the paper does not say whether ratios are of trial averages or averaged over trials;\n    readings (a) ratio of the averages, (b) average of single-trial ratios. Reproduced when the mean\n    is within tolerance under both.\n- id: fig3g-later-bap-ratio\n  statement: Later bAPs that carry a dSpike have a larger amplitude ratio to the first bAP than\n    later bAPs without one.\n  source: Figure 3g\n  quote: g Amplitude ratio of later bAPs to the first bAP (∆F max /∆F 1 ). Data sorted by the\n    presence ( + dSpike) vs. absence (-dSpike) of dSpike.\n  data: dataset\n  criterion: Per stimulated region (soma or proximal < 200 µm, 22 regions), the mean ratio at the\n    distal region for later bAPs with and without dSpikes. The paper reports no test; the\n    Methods' paired two-tailed t-test across regions is applied. Reproduced when the +dSpike ratio\n    is higher with p < 0.05.\n- id: figs12-bap-velocity\n  statement: bAPs propagate along the apical trunk at 141 ± 30 µm/ms (mean ± s.d., 17 neurons).\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 4; Figure S12\n  quote: Mean propagation velocity of bAPs along the apical trunk was 141 ± 30 µm/ms (mean ± s.d., n\n    = 17 neurons, 15 animals\n  data: dataset\n  expected:\n  - quantity: mean bAP propagation velocity along the apical trunk\n    value: 141\n    tolerance: 30\n    unit: µm/ms\n  criterion: Tolerance is the paper's s.d. Per neuron, with soma stimulation (Fig. S12a), the time\n    of each spike's peak along the trunk; sub-frame timing by SNAPT (Methods, time at 50% of the\n    local maximum from a quadratic spline fit to the spike-triggered average). Open, how velocity\n    is taken from the delays; readings (a) the slope of a line fitted to distance against delay,\n    (b) the mean of segment-wise distance over delay. Reproduced when the mean over neurons is\n    within tolerance under both readings. The Source Data (sheet Supplementary Fig 12) gives the\n    17 per-neuron values for comparison.\n- id: fig3e-soma-third-bap\n  statement: In the Fig. 3 neuron, soma stimulation never evoked dSpikes on the first two bAPs and\n    evoked one on the third bAP in 6 of 54 trials.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 5; Figure 3e\n  quote: Stimulation of the soma alone never evoked dSpikes on the first two bAPs, and occasionally\n    evoked a dSpike on the third bAP (6 of 54 trials)\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: trials with a dSpike on the third bAP, of 54\n    value: 6\n    tolerance: 0.6\n  criterion: The soma recording of the Fig. 3 neuron (index entry \"branch_stim (Fig.3)\", file\n    ..._soma). Reproduced when no first or second bAP carries a dSpike and the count is within\n    tolerance.\n- id: fig3d-distal-first-bap\n  statement: In the Fig. 3 neuron, stimulation of distal dendrite D2 evoked a dSpike on the first\n    bAP in 35 of 54 trials (65%).\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 5; Figure 3d\n  quote: Stimulation of distal dendrite D2 alone evoked dSpikes on the first bAP, with 65% probability\n    (35 of 54 trials\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: trials with a dSpike on the first bAP, of 54\n    value: 35\n    tolerance: 3.5\n  criterion: The recording for the legend's D2 is identified as in source-data-index (readings,\n    file D2 or file D4). Reproduced when the count is within tolerance under the reading whose\n    total counts match the legend; when neither matches, both are shown and the claim is\n    methods_underspecified.\n- id: fig3f-soma-plus-distal\n  statement: In the Fig. 3 neuron, simultaneous soma and D2 stimulation gave two quick bAPs without\n    dSpikes and then a third bAP that evoked a dSpike in all 54 trials.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 5; Figure 3f\n  quote: Simultaneous stimulation at soma and D2 produced two quick bAPs which failed to evoke\n    dSpikes, and then the third bAP (12 – 17 ms after stimulus onset) triggered a dSpike with 100%\n    probability (54 of 54 trials\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: trials with a dSpike on the third bAP, of 54\n    value: 54\n    tolerance: 5.4\n  criterion: The combined recording (file ..._D4+soma). Reproduced when the count is within\n    tolerance and at most 10% of first and second bAPs carry a dSpike.\n- id: fig3i-distance-dependence\n  statement: The probability that the first bAP evokes a dSpike rises sigmoidally with the distance\n    of the stimulus from the soma, reaching a plateau of about 80% beyond 300 µm, and is near zero\n    for stimuli within 200 µm.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 5; Figure 3i\n  quote: Proximal stimuli ( < 200 μm from the soma) almost never evoked dSpikes on the first bAP ...\n    the probability of evoking a dSpike with the first bAP followed a sigmoidal distance\n    dependence, with a plateau of ~80% success rate for stimuli > 300 µm from the soma\n  data: dataset\n  expected:\n  - quantity: plateau of first-bAP dSpike probability for stimuli beyond 300 µm\n    value: 80\n    tolerance: 8\n    unit: \"%\"\n  criterion: For each of the 35 dendrite stimulations, the fraction of trials whose first bAP\n    carries a dSpike, against the distance of the stimulus from the soma (Fig. 3i legend). Open,\n    the paper does not say how the distance of a stimulus region is taken or what the plateau\n    is; readings for distance, (a) the centroid of the stimulus polygon's eYFP fluorescence, (b)\n    the point of the polygon nearest the soma; readings for the plateau, (a) the upper asymptote\n    of a logistic fit, (b) the mean probability of stimuli beyond 300 µm. Reproduced when every\n    reading gives a plateau within tolerance and the mean probability for stimuli within 200 µm\n    is below 10%.\n- id: fig3-predepolarization-rule\n  statement: dSpikes arise if and only if the distal dendrites have been depolarized for at least\n    15 ms before the bAP arrives.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 6\n  quote: dSpikes arose if and only if the distal dendrites had been depolarized for at least 15 ms\n    prior to arrival of a bAP.\n  data: dataset\n  criterion: The paper states the rule from its examples and gives no test. For every bAP in the\n    branch, soma and soma plus dendrite recordings, the time the distal region (> 300 µm) has been\n    depolarized before the bAP, from the first frame after stimulus onset at which the\n    stimulus-triggered average distal -dF exceeds 2 s.d. of its pre-stimulus baseline (a standard\n    onset choice). Reproduced when at least 90% of dSpikes follow >= 15 ms of distal\n    depolarization and at least 90% of bAPs that follow < 15 ms fail; the full table is reported.\n- id: figs13-ramp-first-spike\n  statement: Under a gradual optogenetic ramp to the soma or proximal dendrites, the first somatic\n    spike almost always evokes a dSpike (92%).\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 7; Figure S13\n  quote: For this stimulus waveform, the first somatic spike almost always evoked a dSpike (92%, 188\n    ramps, 56 cells, 44 animals\n  data: dataset\n  expected:\n  - quantity: fraction of first bAPs of a ramp that evoke a dSpike\n    value: 92\n    tolerance: 9.2\n    unit: \"%\"\n  criterion: The ramp recordings (3 s linear ramps, soma or proximal < 150 µm). The text says 188\n    ramps and the Fig. S13d legend \"92% out of 225 bAPs\". Readings, (a) the fraction of ramps whose\n    first bAP carries a dSpike, (b) the fraction of all first bAPs counted over recordings\n    including repeats. Reproduced when one reading is within tolerance; both are shown.\n- id: fig4a-step-example\n  statement: In the Fig. 4a neuron, a step stimulus to a proximal apical dendrite evoked a bAP\n    without a dSpike, then two bAPs with dSpikes, then a series of bAPs without dSpikes.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 1; Figure 4a\n  quote: a step stimulus to a proximal apical dendrite evoked a bAP without a dSpike, then two bAPs\n    with dSpikes, then a series of bAPs without dSpikes\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The recording of index entry \"branch_adaptation (Fig.4a)\". Reproduced when the\n    sequence of failures and dSpikes in at least one trial is failure, dSpike, dSpike, then only\n    failures, and the most common sequence over trials is reported.\n- id: fig4b-dspike-window\n  statement: Under step stimulation dSpikes fail for the first 18 ± 7 ms, succeed until 83 ± 47 ms\n    after onset, and then fail (mean ± s.d., 43 stimulated branches, 16 cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 1; Figure 4b\n  quote: dSpikes failed for the first 18 ± 7 ms (mean ± s.d.), then there was a period where dSpikes\n    succeeded which lasted until 83 ± 47 ms after stimulus onset, followed by subsequent dSpike\n    failures\n  data: dataset\n  expected:\n  - quantity: time of window opening (end of initial failures) after stimulus onset\n    value: 18\n    tolerance: 7\n    unit: ms\n  - quantity: time of window closing (last dSpike) after stimulus onset\n    value: 83\n    tolerance: 47\n    unit: ms\n  criterion: Tolerances are the paper's s.d. The step recordings (> 200 ms, soma or proximal\n    dendrites). Open, the paper does not say how the two times are taken per branch; readings,\n    (a) per stimulated branch, the time of the first and of the last dSpike in each trial,\n    averaged over trials, then mean over branches; (b) per branch, the first and last time at\n    which the trial-pooled dSpike fraction per 10 ms bin is above zero. Reproduced when both\n    means are within tolerance under both readings.\n- id: fig4b-few-late-dspikes\n  statement: Sustained somatic spiking produced very few dSpikes later than 100 ms after stimulus\n    onset, whatever the stimulus strength or location.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 1; Figure 4b\n  quote: Sustained spiking at the soma led to very few dSpikes later than 100 ms after stimulus onset,\n    regardless of stimulus strength or location.\n  data: dataset\n  criterion: In the step recordings, the percent of bAPs carrying a dSpike before and after 100 ms\n    from onset (Fig. 4b bottom). Reproduced when the later percent is below one fifth of the\n    earlier and below 10% (a reading of \"very few\"); both percents are reported.\n- id: fig4ce-period-doubling\n  statement: Wide-field optogenetic stimulation evoked a period-doubling bifurcation, bAPs\n    alternately succeeding and failing to evoke dSpikes, with all bAPs after about 180 ms failing\n    (9 cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 3; Figure 4c-e\n  quote: this stimulus reliably evoked a period-doubling bifurcation ... ( n = 9 cells from 9 animals,\n    Fig. 4c, d ). The dSpike window persisted to ~180 ms after stimulus onset, but, despite the\n    stronger stimulus, all bAPs after ~180 ms failed to evoke dSpikes\n  data: dataset\n  expected:\n  - quantity: end of the dSpike window under wide-field stimulation\n    value: 180\n    tolerance: 18\n    unit: ms\n  criterion: In the wide-field recordings, bAP frequency from inter-peak intervals and amplitude\n    normalized to the mean of the final 5 bAPs of the epoch (Methods, Period doubling; Fig. 4e).\n    Alternation holds in a cell when successive normalized amplitudes alternate above and below 1\n    for at least 4 consecutive bAPs (the alternating motif of Fig. 4e right). Reproduced when at\n    least 7 of 9 cells alternate and the time of the last dSpike, averaged over cells, is within\n    tolerance.\n- id: fig4d-example-alternation\n  statement: In the Fig. 4c-d neuron, the first 12 bAPs under wide-field stimulation showed two bAP\n    failures followed by alternating dSpikes and failures.\n  source: Figure 4d\n  quote: Amplitude maps of the first 12 bAPs showing two bAP failures, followed by alternating dSpikes\n    and bAP failures.\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The recording of index entry \"branch_bifurcation (Fig.4c,d)\". Reproduced when the\n    first 12 bAPs read failure, failure, then alternate dSpike and failure, in at least one trial.\n- id: figs15-stochastic\n  statement: Even stronger wide-field stimuli evoked an epoch of seemingly random interplay of bAPs\n    and dSpikes, varying from trial to trial while somatic spiking stayed regular, followed by\n    sustained dSpike failures.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 3; Figure S15\n  quote: Even stronger stimuli evoked an epoch of seemingly random interplay of bAPs and dSpikes\n    (Fig. S15 ), followed by sustained dSpike failures.\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The recording of index entry \"period_doubling (Fig. S15)\". Reproduced when the\n    sequence of dSpikes and failures differs between at least two trials while somatic spike\n    times stay within 2 ms of each other across trials for the same bAP index, and later bAPs\n    fail.\n- id: figs14-low-rate-attenuation\n  statement: With somatic current pulses at 3 Hz, distal bAP amplitudes attenuate progressively,\n    without dSpikes.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 2; Figure S14d\n  quote: At low frequencies (e.g., 3 Hz), membrane depolarization did not accumulate sufficiently to\n    trigger dSpikes; instead, we observed a progressive attenuation of bAP amplitudes in the\n    distal dendrites\n  data: dataset\n  criterion: In the patch clamp pulse recordings (2 nA, 2 ms), the distal (> 300 µm) -dF/F of each\n    spike relative to the last spike at 3 Hz (Fig. S14d, 29 recordings). Reproduced when the first\n    spike's ratio exceeds 1 in a paired two-tailed t-test (p < 0.05) across recordings and no\n    dSpike is found at 3 Hz.\n- id: figs14-high-rate-window\n  statement: With somatic current pulses at 80 Hz or more, bAPs first fail, then a series of\n    dSpikes arises, then failures again.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 2; Figure S14e, f\n  quote: At frequencies ≥ 80 Hz, however, we observed a characteristic motif of bAP failure, then a\n    series of dSpikes, and then failures again\n  data: dataset\n  criterion: Maximum distal amplitude per frequency normalized to each dataset's minimum (Fig.\n    S14e), and the sequence of successes at 80 Hz (Fig. S14f). Reproduced when dSpikes occur at\n    80 Hz and above and not below, and the 80 Hz sequence in most recordings starts with at least\n    one failure and ends with failures.\n- id: figs16-ba-increases-dspikes\n  statement: BaCl2 (150 µM) increased the dSpike probability under soma stimulation from 11 ± 2%\n    to 64 ± 10% (mean ± s.e.m., 9 cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S16e-g\n  quote: 'BaCl 2 : 11 ± 2% before to 64 ± 10% after, mean ± s.e.m., n = 9 cells from 6 animals, p <\n    0.001, paired t-test'\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 9 cells from 6 animals\n  - about: same test, as the Fig. S16 legend gives it\n    test: two-sided paired Student's t-test\n    p: 0.00068\n    n: 9 cells from 6 animals\n  data: dataset\n  expected:\n  - quantity: dSpike probability, baseline\n    value: 11\n    tolerance: 2\n    unit: \"%\"\n  - quantity: dSpike probability, BaCl2\n    value: 64\n    tolerance: 10\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e.m. dSpike probability is the percent of bAPs carrying\n    a dSpike (Source Data column \"dSpike (%)\"), per cell, for 20 or 30 ms soma stimuli at 5 Hz\n    (59 repeats). Reproduced when both means are within tolerance and a two-sided paired t-test\n    gives p < 0.001 for an increase. The Source Data sheet gives per-cell values.\n- id: figs16-4ap-increases-dspikes\n  statement: 4-AP (5 mM) increased the dSpike probability from 19 ± 4% to 92 ± 4% (mean ± s.e.m., 4\n    cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S16b-d\n  quote: '4-AP: 19 ± 4% before to 92 ± 4% after, mean ± s.e.m., n = 4 cells from 3 animals, p < 0.001,\n    paired t-test'\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 cells from 3 animals\n  - about: same test, as the Fig. S16d legend gives it\n    test: two-sided paired Student's t-test\n    p: 0.001\n    n: 4 cells from 3 animals\n  data: dataset\n  expected:\n  - quantity: dSpike probability, baseline\n    value: 19\n    tolerance: 4\n    unit: \"%\"\n  - quantity: dSpike probability, 4-AP\n    value: 92\n    tolerance: 4\n    unit: \"%\"\n  criterion: As figs16-ba-increases-dspikes. The text gives p < 0.001 and the legend p = 0.001;\n    reproduced when both means are within tolerance and a two-sided paired t-test gives p <= 0.001\n    for an increase. Note that the example recording of the index (\"after_4AP (Fig.S16c)\") is\n    named TTX20nM+4AP5mM.\n- id: figs17-ttx-decreases-dspikes\n  statement: Low TTX (20 nM) did not affect somatic spiking but decreased the dSpike probability\n    from 44 ± 15% to 11 ± 8% (mean ± s.e.m., 4 cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S17a-d\n  quote: This low TTX dose did not affect spiking at the soma, but the mean dSpike probability was\n    significantly decreased (control: 44 ± 15%, TTX: 11 ± 8%, mean ± s.e.m., n = 4 cells from 3\n    animals, p = 0.008, paired t-test\n  statistics:\n  - test: paired t-test\n    p: 0.008\n    n: 4 cells from 3 animals\n  data: dataset\n  expected:\n  - quantity: dSpike probability, control\n    value: 44\n    tolerance: 15\n    unit: \"%\"\n  - quantity: dSpike probability, TTX 20 nM\n    value: 11\n    tolerance: 8\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e.m. dSpike probability as figs16-ba-increases-dspikes,\n    for stimuli over about 100 µm across the soma and proximal dendrites (20 ms, 5 Hz, 59 to 118\n    repeats). Reproduced when both means are within tolerance and a two-sided paired t-test gives\n    p < 0.05 for a decrease; the number of somatic spikes per stimulus before and after is\n    reported.\n- id: figs17e-ttx-high-dose\n  statement: At 100 nM, TTX eliminated distal dSpikes while somatic spiking continued.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S17e\n  quote: In some experiments, a higher concentration of TTX (100 nM) eliminated all dSpikes at distal\n    dendrites, while preserving somatic spiking\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The example of index entries \"after_TTX (100nM; Fig.S17e)\" and its baseline. Reproduced\n    when the 100 nM recording has somatic spikes and no distal dSpike, while the baseline has\n    dSpikes.\n- id: figs18e-ni-no-effect-on-dspikes\n  statement: The CaV blocker Ni2+ (100 to 500 µM) did not affect dSpikes.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S18a-e\n  quote: The dSpikes were not affected by addition of the Ca V blocker Ni 2+ (100-500 µM; Fig. S18a–e\n    ), suggesting that they are not mediated by VGCCs.\n  data: dataset\n  criterion: A claim of absence. The legend names no test; the Methods' test for paired treatment\n    data is the two-sided paired t-test at 0.05 (n = 5 cells from 4 animals), on dSpike\n    probability as figs16-ba-increases-dspikes. Which Ni2+ concentration Fig. S18e pools is not\n    said (the example has 100 and 500 µM); the test is run on the highest concentration each cell\n    received, and on 100 µM and 500 µM separately as variants. Reproduced when the main test\n    gives p >= 0.05; the mean change is reported either way.\n- id: figs18-ni-blocks-calcium-spikes\n  statement: Under strong drive, dSpikes occasionally triggered broad (> 20 ms) dendritic spikes;\n    Ni2+ (500 µM) eliminated them while preserving dendritic Na+ spikes, and reduced their\n    frequency significantly (6 cells).\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S18f-h\n  quote: Addition of Ni 2+ (500 μM) eliminated these broad spikes, confirming their dependence on VGCC\n    activation.\n  statistics:\n  - test: two-sided paired Student's t-test\n    p: 0.017\n    n: 6 cells from 6 animals\n  data: dataset\n  criterion: Putative Ca2+ spikes are distal depolarizations lasting > 20 ms (Fig. S18f legend),\n    counted per ramp (3 s), mean of three trials per cell, pooled from the wide-field and the\n    Ba2+ ramp experiments (Fig. S18h legend). Open, how duration is measured; readings (a) full\n    width at half maximum, (b) time above the dSpike threshold. Reproduced when under both\n    readings the count falls with Ni2+ with p < 0.05 in a two-sided paired t-test and dSpikes\n    remain under Ni2+.\n- id: figs18g-ba-increases-calcium-spikes\n  statement: Adding Ba2+ (150 µM) increased the incidence of putative dendritic Ca2+ spikes under\n    soma-targeted ramp stimulation.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 4; Figure S18g\n  quote: Addition of K V blocker Ba 2+ (150 µM) to otherwise untreated neurons increased the\n    prevalence of putative Ca 2+ spikes\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: The example of index entries \"baseline (Fig.S18g)\", \"after_Ba2+ (Fig.S18g)\" and\n    \"after_Ba2+_NiCl (Fig.S18g)\", with Ca2+ spikes as in figs18-ni-blocks-calcium-spikes.\n    Reproduced when the count is higher after Ba2+ than at baseline and lower again after Ni2+.\n- id: fig4f-g-model-accelerometer\n  statement: In the multi-compartment CA1 model, step stimulation at the soma gives a dSpike motif\n    of failure, success, success, failures, and wide-field stimulation gives alternating successes\n    and failures followed by repeated failures.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 5; Figure 4f, 4g\n  quote: a simulated step-wise optogenetic stimulation at the soma led to a dSpike motif of failure,\n    success, success, failures ... Simulated wide-field optogenetic stimulation with the same model\n    parameters evoked a period-doubling bifurcation with alternating dSpike successes and failures,\n    followed by repeated failures\n  data: with_inputs\n  criterion: Supplementary Software 1 run as provided with the Table 1 parameters; a bAP succeeds\n    when the compartment 500 µm from the soma peaks above -40 mV (Methods, Parameter fitting).\n    Reproduced when the soma run gives the motif and the wide-field run alternates and then fails.\n- id: figs20-model-robustness\n  statement: In the model, the accelerometer motif of bAP failure, dSpikes, then failure persists\n    over a wide range of dendritic NaV density, NaV slow inactivation, A-type KV density and\n    stimulus strength.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 6; Figure S20c-e\n  quote: the spike-rate accelerometer motif of bAP failure, dSpikes, and then failure persisted over a\n    wide range of parameters\n  data: with_inputs\n  criterion: The parameter sweeps of Supplementary Software 1 (Model Robustness, parameters_list.py)\n    with the -40 mV at 500 µm rule. Reproduced when the motif occupies a contiguous region in each\n    of the three phase diagrams that includes the Table 1 parameters.\n- id: figs20ab-model-patch-vs-opto\n  statement: In the model, a 2 nA dendritic current injection evokes dendrite-localized sodium\n    spikes, while optogenetic stimulation of the same dendrite evokes a somatic spike first that\n    then back-propagates, explaining the absence of dendrite-initiated dSpikes in the experiments.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 3; Figure S20a, b\n  quote: the absence of dendrite-initiated dSpikes in our experiments was likely due to the more\n    gradual, weaker, and spatially distributed nature of optogenetic vs. patch clamp stimuli\n  data: with_inputs\n  criterion: The \"Oblique Patch Clamp and Optogenetic Stimulus\" runs of Supplementary Software 1.\n    Reproduced when the current injection peaks first in the stimulated dendrite and the\n    optogenetic stimulus peaks first at the soma.\n- id: figs21-izhikevich\n  statement: A two-compartment Izhikevich model reproduces the opening and closing of the dSpike\n    window under soma stimulation and period-doubling under combined soma and dendrite stimulation.\n  source: Results, Dendritic spike-rate accelerometer, period-doubling, and stochastic back-propagation, paragraph 6; Figure S21\n  quote: which also captured the opening and closing of the dSpike window (i.e. spike-rate\n    accelerometer) and the period-doubling under simultaneous distal and proximal stimulation\n  data: with_inputs\n  criterion: Two_compartment_Izhikevich.m with the Methods' parameters (gs = 0.16, gD = 0 for soma\n    only; gs = 0.3, gD = 0.05 combined; vrs = -55 and initial u_D = -13), and as a variant with the\n    script's own (-65, -18). Reproduced when the soma run gives dendritic failure, spikes, then\n    failure, and the combined run alternates, under the Methods' parameters.\n- id: fig5a-plateau-collision\n  statement: Combining soma optogenetic stimulation with EFS of distal synaptic inputs evoked a\n    long-lasting (about 120 ms) dendritic plateau potential and a burst of somatic spikes, unlike\n    either stimulus alone.\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 2; Figure 5a\n  quote: Remarkably, combining optogenetic and electrical stimuli evoked a long-lasting ( ~ 120 ms)\n    plateau potential in the dendrites and a burst of spikes on top of a strong subthreshold\n    depolarization at the soma\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: plateau duration\n    value: 120\n    tolerance: 12\n    unit: ms\n  criterion: The recording of index entry \"Plateau_induction (Fig.5a)\". Duration is the time the\n    distal (> 200 µm) -dF stays above half its peak (a standard measure; the paper names none).\n    Reproduced when the combined stimulus gives a duration within tolerance, more somatic spikes\n    than the optogenetic stimulus alone, and neither single stimulus gives a distal event lasting\n    over 60 ms.\n- id: fig5b-supralinear-auc\n  statement: The distal AUC for combined stimulation was on average 3.1 ± 0.7-fold the sum of the\n    AUCs for optical and EFS stimuli alone (mean ± s.e.m.), and more than twice that sum in 15 of 28\n    cells.\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 3; Figure 5b\n  quote: The average AUC combined was 3.1 ± 0.7-fold greater than AUC optical + AUC electrical (mean ±\n    s.e.m.) and for more than half of the cells studied (15 of 28 cells from 12 animals)\n  data: dataset\n  expected:\n  - quantity: mean AUC combined over AUC optical plus AUC electrical\n    value: 3.1\n    tolerance: 0.7\n  - quantity: cells with ratio above 2, of 28\n    value: 15\n    tolerance: 1.5\n  criterion: Tolerance of the mean is the paper's s.e.m. AUC as in the shared method (both window\n    readings), at a distal dendrite > 200 µm, with 30 ms soma stimulation and one 0.1 ms EFS pulse.\n    Reproduced when both values are within tolerance under one window reading; both are shown. The\n    Source Data sheet Figure 5 gives per-cell values.\n- id: fig5d-timing-window\n  statement: Nonlinear amplification was greatest when optical and electrical stimuli overlapped;\n    for EFS before bAPs it fell sigmoidally, by half in 87 ms, and for EFS after bAPs exponentially\n    with a 35 ms time constant.\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 3; Figure 5c, 5d\n  quote: 'For ‘EFS before bAPs’, the amplification followed a sigmoidal profile, decaying by half in\n    87 ms. For ‘EFS after bAPs’, the amplification decayed exponentially with a time constant of 35\n    ms.'\n  data: dataset\n  expected:\n  - quantity: half-decay of amplification, EFS before bAPs\n    value: 87\n    tolerance: 8.7\n    unit: ms\n  - quantity: exponential time constant, EFS after bAPs\n    value: 35\n    tolerance: 3.5\n    unit: ms\n  criterion: Per cell (8 cells, 30 ms stimulus), combined AUC against dTime, scaled to [0, 1]\n    (Methods; Fig. 5d legend). Fits to the pooled points, an exponential from -245 to 0 ms and a\n    sigmoid from 0 to +245 ms (legend). The legend's fit ranges place EFS after bAPs at negative\n    dTime; the file names (interval_-100ms and so on) are read the same way. Open, the fits'\n    forms; readings (a) exp(dTime/tau) and 1/(1 + exp((dTime - t_half)/k)), both without offset,\n    (b) the same fitted to the per-time means. Reproduced when both values are within tolerance\n    under one reading.\n- id: fig5d-single-bap-no-plateau\n  statement: A single bAP (10 ms soma stimulus) did not evoke a nonlinear dendritic response at any\n    timing relative to EFS (5 cells).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 4; Figure 5c, 5d\n  quote: Triggering a single bAP by a 10 ms optogenetic stimulus targeted to the soma did not evoke a\n    nonlinear dendritic response, regardless of timing relative to the EFS\n  data: dataset\n  criterion: Per cell and dTime, combined AUC over AUC optical plus AUC electrical, as\n    fig5b-supralinear-auc. The paper's threshold for a nonlinear response is \"> 200% nonlinearity\"\n    (Results, paragraph 3). Reproduced when no cell's ratio exceeds 2 at any dTime.\n- id: fig5ef-late-efs-no-plateau\n  statement: During a 3 s optogenetic ramp, EFS early (0.5 s) evoked plateau potentials but EFS late\n    (2.5 s, somatic rate 24 ± 4 Hz) did not (AUC 5.6 ± 3.6 against 1.6 ± 1.0, mean ± s.d.).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 5; Figure 5e, 5f\n  quote: The early EFS reliably evoked plateau potentials (AUC 5.6 ± 3.6, mean ± s.d.), whereas the\n    late EFS, which occurred when the average spike rate was 24 ± 4 Hz (mean ± s.d.), did not (AUC\n    1.6 ± 1.0, mean ± s.d., n = 7 cells from 5 animals, p = 0.01, paired t-test\n  statistics:\n  - test: paired t-test\n    p: 0.01\n    n: 7 cells from 5 animals (the Fig. 5f legend gives 8 neurons from 5 animals)\n  data: dataset\n  expected:\n  - quantity: AUC, early EFS\n    value: 5.6\n    tolerance: 3.6\n  - quantity: AUC, late EFS\n    value: 1.6\n    tolerance: 1.0\n  - quantity: somatic spike rate at late EFS\n    value: 24\n    tolerance: 4\n    unit: Hz\n  criterion: Tolerances are the paper's s.d. The AUC unit is not given (the Source Data label is\n    \"Area (a.u.)\"); the Source Data sheet Figure 5 gives per-cell values, and the AUCs here are\n    compared with them in the same units after the same integration. Open, the sample, 7 cells\n    (text) or 8 (legend); both are run. Reproduced when under one sample and window reading the\n    means are within tolerance and a two-sided paired t-test gives p < 0.05 for early above late.\n- id: fig5gh-weak-step-equal\n  statement: Under a weak 3 s optogenetic step, EFS at 0.5 s and at 2.5 s were equally effective\n    at inducing plateau potentials (AUC 4.5 ± 2.0 and 4.0 ± 2.0, mean ± s.d., p = 0.19).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 5; Figure 5g, 5h\n  quote: In this case EFS at 0.5 s and at 2.5 s were equally effective at inducing plateau potentials\n    (0.5 s: AUC 4.5 ± 2.0, mean ± s.d., 2.5 s: AUC 4.0 ± 2.0, mean ± s.d., p = 0.19, n = 7 cells from\n    5 animals, paired t-test\n  statistics:\n  - test: paired t-test\n    p: 0.19\n    n: 7 cells from 5 animals (the Fig. 5h legend gives 8 neurons from 5 animals)\n  data: dataset\n  expected:\n  - quantity: AUC, EFS at 0.5 s\n    value: 4.5\n    tolerance: 2.0\n  - quantity: AUC, EFS at 2.5 s\n    value: 4.0\n    tolerance: 2.0\n  criterion: A claim of absence, judged on the paper's two-sided paired t-test at 0.05, on the 7\n    cells of the text, with the legend's 8 as a variant. Reproduced when p >= 0.05; the mean\n    difference is reported either way.\n- id: fig6-dap5-reduces-plateau\n  statement: Blocking NMDARs with D-AP5 (50 µM) reduced the plateau area to 42 ± 7% of baseline,\n    against 107 ± 5% for vehicle (mean ± s.e.m.).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 6; Figure 6a, 6b\n  quote: Block of NMDARs by D-AP5 (50 µM) reduced the plateau area to 42 ± 7% of baseline ( n = 6\n    cells from 5 animals, mean ± s.e.m.) compared to vehicle control (107 ± 5% of baseline, n = 11\n    cells from 8 animals; p < 0.001, one-way ANOVA with Bonferroni’s post hoc test\n  statistics:\n  - test: one-way ANOVA with Bonferroni's post hoc test\n    p: 3.6e-7\n    corrected: Bonferroni\n    n: 6 D-AP5 cells from 5 animals and 11 vehicle cells from 8 animals\n  data: dataset\n  expected:\n  - quantity: plateau AUC, D-AP5, percent of baseline\n    value: 42\n    tolerance: 7\n    unit: \"%\"\n  - quantity: plateau AUC, vehicle, percent of baseline\n    value: 107\n    tolerance: 5\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e.m. Per cell, combined-stimulus (30 ms soma, 0.1 ms EFS)\n    AUC after treatment over AUC before (Methods, % baseline), at > 200 µm. A one-way ANOVA over\n    vehicle, D-AP5, TTX and Ni2+ with Bonferroni post hoc tests against vehicle. Reproduced when\n    the means are within tolerance and the D-AP5 comparison has p < 0.001.\n- id: fig6-ni-reduces-plateau\n  statement: Blocking VGCCs with Ni2+ (100 µM) largely eliminated the plateau potential (18 ± 5%\n    of baseline, mean ± s.e.m.).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 6; Figure 6a, 6b\n  quote: Block of voltage-gated Ca 2+ channels (VGCCs) by Ni 2+ (100 µM) largely eliminated the\n    plateau potential (AUC 18 ± 5% of baseline, n = 4 cells from 4 animals, mean ± s.e.m.\n  statistics:\n  - test: one-way ANOVA with Bonferroni's post hoc test\n    p: 1.8e-8\n    corrected: Bonferroni\n    n: 4 Ni2+ cells from 4 animals and 11 vehicle cells from 8 animals\n  data: dataset\n  expected:\n  - quantity: plateau AUC, Ni2+, percent of baseline\n    value: 18\n    tolerance: 5\n    unit: \"%\"\n  criterion: As fig6-dap5-reduces-plateau; reproduced when the mean is within tolerance and the\n    Ni2+ comparison has p < 0.001.\n- id: fig6-ttx-reduces-plateau\n  statement: Blocking dendritic NaV channels with TTX (20 nM) also eliminated plateau potentials (26\n    ± 8% of baseline, mean ± s.e.m.).\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 8; Figure 6a, 6b\n  quote: Block of dendritic Na V channels by TTX (20 nM) also eliminated plateau potentials (AUC 26 ±\n    8% of baseline, n = 4 cells from 3 animals, mean ± s.e.m.\n  statistics:\n  - test: one-way ANOVA with Bonferroni's post hoc test\n    p: 8.8e-8\n    corrected: Bonferroni\n    n: 4 TTX cells from 3 animals and 11 vehicle cells from 8 animals\n  data: dataset\n  expected:\n  - quantity: plateau AUC, TTX, percent of baseline\n    value: 26\n    tolerance: 8\n    unit: \"%\"\n  criterion: As fig6-dap5-reduces-plateau; reproduced when the mean is within tolerance and the TTX\n    comparison has p < 0.001.\n- id: figs24-drugs-selective\n  statement: The drugs' effects on the plateau were much larger than their effects on the AUC for\n    EFS or optogenetic stimulation alone.\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 8; Figure S24\n  quote: The drug effects on the plateau were much larger than their effects on the AUC for EFS or\n    optogenetic stimulation alone\n  statistics:\n  - about: D-AP5 against baseline\n    test: two-sided paired Student's t-test\n    p: 0.0005\n    n: 6 cells from 5 animals\n  - about: TTX against baseline\n    test: two-sided paired Student's t-test\n    p: 0.0022\n    n: 4 cells from 3 animals\n  - about: Ni2+ against baseline\n    test: two-sided paired Student's t-test\n    p: 0.00037\n    n: 4 cells from 4 animals\n  data: dataset\n  criterion: The Fig. S24 legend does not say which response its p-values compare; the readings are\n    (a) the combined response, (b) each response. Per cell and drug, AUC after over AUC before for\n    optical alone, EFS alone and combined. Reproduced when for every drug the mean fall of the\n    combined AUC exceeds the mean fall of each single-stimulus AUC, and the combined comparison\n    has p < 0.05 in a two-sided paired t-test.\n- id: figs23-dendrite-drives-soma\n  statement: Subtracting the somatic signal from the dendritic signal reveals a slowly rising and\n    falling dendritic depolarization lasting up to about 300 ms after the optogenetic stimulus,\n    which drives the high-frequency somatic firing.\n  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 9; Figure S23\n  quote: This procedure revealed the slowly rising and falling dendritic depolarization (presumably\n    dominated by VGCC and NMDAR currents) which persisted for up to ~300 ms after the end of the\n    optogenetic stimulus to the soma\n  data: dataset\n  expected:\n  - quantity: longest persistence of dendrite minus soma depolarization after stimulus end\n    value: 300\n    tolerance: 30\n    unit: ms\n  criterion: In the combined-stimulus recordings (Fig. S23, 9 neurons), -dF/F at the dendritic\n    region with the largest plateau minus that at the soma. Persistence is the time after the 30\n    ms stimulus ends until the difference returns within 2 s.d. of its pre-stimulus baseline\n    (a standard choice). Reproduced when the longest persistence over cells is within tolerance\n    and the difference is positive in most cells.\n- id: figs25-temperature\n  statement: Cooling from 34 to 24 °C increased the dSpike probability (first bAP 0% against 29 ±\n    16%; any bAP 16 ± 3% against 50 ± 12%, mean ± s.e.m., 6 cells).\n  source: Methods, Slice preparation, paragraph 2; Figure S25f, g\n  quote: We observed a significant increase in dSpike probability at 24 °C (0% vs. 29 ± 16% by the\n    first bAP, p = 0.09; 16 ± 3% vs. 50 ± 12% by any bAP, p = 0.02; mean ± s.e.m., n = 6 cells from\n    4 animals, paired t-test)\n  statistics:\n  - about: first bAP, 34 against 24 °C\n    test: paired t-test\n    p: 0.09\n    n: 6 cells from 4 animals\n  - about: any bAP, 34 against 24 °C\n    test: paired t-test\n    p: 0.02\n    n: 6 cells from 4 animals\n  - about: any bAP, as the Fig. S25g legend gives it\n    test: two-sided paired Student's t-test\n    p: 0.03\n    n: 6 cells from 4 animals\n  data: dataset\n  expected:\n  - quantity: dSpike probability by the first bAP, 34 °C\n    value: 0\n    tolerance: 0\n    unit: \"%\"\n  - quantity: dSpike probability by the first bAP, 24 °C\n    value: 29\n    tolerance: 16\n    unit: \"%\"\n  - quantity: dSpike probability by any bAP, 34 °C\n    value: 16\n    tolerance: 3\n    unit: \"%\"\n  - quantity: dSpike probability by any bAP, 24 °C\n    value: 50\n    tolerance: 12\n    unit: \"%\"\n  criterion: Tolerances are the paper's s.e.m.; a reported 0% needs a count of 0. Soma stimulation\n    30 ms at 5 Hz. \"By the first bAP\" is the percent of trials whose first bAP carries a dSpike.\n    \"By any bAP\" is open; readings (a) the percent of all bAPs carrying a dSpike, (b) the percent\n    of trials with a dSpike on any bAP. Reproduced when, under one reading, all four values are\n    within tolerance and the any-bAP increase has p < 0.05 in a two-sided paired t-test.\n- id: figs1-no-perturbation\n  statement: Optopatch-V expression did not change resting potential, rheobase, capacitance, input\n    resistance or spike rates relative to neighboring non-expressing neurons.\n  source: Results, paragraph 2; Figure S1\n  quote: No significant difference was found between the groups (p > 0.05, two-sided paired\n    Student’s t-test).\n  statistics:\n  - test: two-sided paired Student's t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 16 cells from 6 animals for each group\n  data: dataset\n  criterion: A claim of absence, judged on the paper's two-sided paired t-test at 0.05 for each\n    property (16 pairs of an expressing and a neighboring non-expressing cell). Rheobase is the\n    smallest 500 ms step that evokes a spike (Methods). Reproduced when no property gives p <\n    0.05; the differences are reported.\n- id: figs2-imaging-fidelity\n  statement: Optical recording at 1 kHz detected every spike up to 90 Hz with no false positives or\n    negatives (7 cells, 2212 spikes), with a single-trial noise-equivalent voltage of 1.2 ± 0.5 mV\n    (2.5 ± 0.8 mV at 2 kHz) and sensitivity of about 12% dF/F per 100 mV.\n  source: Results, paragraph 2; Figure S2\n  quote: The single-trial optical noise-equivalent voltage was 1.2 ± 0.5 mV at 1 kHz and 2.5 ± 0.8 mV\n    at 2 kHz (mean ± s.d., n = 7 neurons, 4 animals) ... with zero false-positives or false-negatives\n    up to the maximum observed spike rate of 90 Hz (n = 7 cells, 2212 spikes)\n  data: with_labels\n  depends_on:\n  - source-data-index\n  expected:\n  - quantity: noise-equivalent voltage at 1 kHz\n    value: 1.2\n    tolerance: 0.5\n    unit: mV\n  - quantity: noise-equivalent voltage at 2 kHz\n    value: 2.5\n    tolerance: 0.8\n    unit: mV\n  - quantity: fluorescence sensitivity\n    value: 12\n    tolerance: 1.2\n    unit: \"% dF/F per 100 mV\"\n  - quantity: false positive and false negative optical spikes\n    value: 0\n    tolerance: 0\n  criterion: The paired patch and imaging recordings listed in the index for Fig. S2 (7 cells). The\n    paper does not define the noise-equivalent voltage; reading, the s.d. of the bleach-corrected\n    subthreshold fluorescence divided by the dF/F per mV from the -70 to +20 mV step (Fig. S2d).\n    Optical spikes are matched to patch spikes within one frame. Reproduced when all values are\n    within tolerance (tolerances are the paper's s.d. or 10%).\n- id: figs2d-frame-rate-same-sensitivity\n  statement: Fluorescence changes for a step from -70 to +20 mV were the same at 1 kHz and 2 kHz.\n  source: Figure S2d\n  quote: Fluorescence changes upon a voltage step from -70 to +20 mV were the same for 1 kHz vs. 2 kHz\n    camera frame rates (p > 0.05, two-sided paired Student’s t-test)\n  statistics:\n  - test: two-sided paired Student's t-test\n    p: 0.05\n    p_relation: \">\"\n    n: 7 cells from 4 animals\n  data: with_labels\n  depends_on:\n  - source-data-index\n  criterion: A claim of absence, judged on the paper's two-sided paired t-test at 0.05, on dF/F at\n    +20 mV per cell at the two frame rates. Reproduced when p >= 0.05.\n- id: figs3-eyfp-dosimetry\n  statement: Dosimetry by eYFP fluorescence had 7.8-fold lower variance than dosimetry by blue laser\n    power (0.084 against 0.66).\n  source: Figure S3f\n  quote: Dosimetry via eYFP fluorescence had 7.8-fold lower variance than did dosimetry via raw blue\n    laser power (0.084 vs. 0.66, n = 18 cells and 6 animals; p = 9.9 x 10-5, F-test)\n  statistics:\n  - test: F-test\n    p: 9.9e-5\n    n: 18 cells and 6 animals\n  data: dataset\n  expected:\n  - quantity: variance of normalized slope, eYFP dosimetry\n    value: 0.084\n    tolerance: 0.0084\n  - quantity: variance of normalized slope, laser power dosimetry\n    value: 0.66\n    tolerance: 0.066\n  criterion: Per cell, slopes of charge against blue intensity and against cumulative eYFP in the\n    linear regime (I < 1 mW/mm2), each normalized to its group mean (legend). Reproduced when both\n    variances are within tolerance and an F-test of equal variances gives p < 0.05.\n- id: figs4-stimulus-localization\n  statement: Patterned optogenetic stimuli are localized; photocurrent fell to half when stimuli were\n    offset by 11 ± 4 µm from the soma, and dendritic responses fell to half at 11 ± 5 µm and to 20%\n    at 34 ± 14 µm.\n  source: Results, paragraph 2; Figure S4d, S4h\n  quote: The induced photocurrent fell to half maximum when stimuli were offset by 11 ± 4 μm and to\n    20% of maximum at 23 ± 7 μm ... Evoked responses, |∆F|, fell to half maximum for stimuli at 11 ±\n    5 μm offset and to 20% of maximum at 34 ± 14 μm offset\n  data: dataset\n  expected:\n  - quantity: soma photocurrent half-maximum offset\n    value: 11\n    tolerance: 4\n    unit: µm\n  - quantity: soma photocurrent 20% offset\n    value: 23\n    tolerance: 7\n    unit: µm\n  - quantity: dendritic response half-maximum offset\n    value: 11\n    tolerance: 5\n    unit: µm\n  - quantity: dendritic response 20% offset\n    value: 34\n    tolerance: 14\n    unit: µm\n  criterion: Tolerances are the paper's s.d. Per cell or branch, responses normalized to 0 µm offset\n    and the offsets of half and 20% found by linear interpolation (a standard choice). Reproduced\n    when all four means are within tolerance.\n- id: figs5-focal-selectivity\n  statement: Voltage signals fall to half at 4 µm transverse offset from an in-focus branch and\n    plateau at 11% (IQR 7 to 24%) beyond 20 µm.\n  source: Results, paragraph 2; Figure S5b\n  quote: The |∆F| signal fell to half maximum at transverse offsets of 4 μm (n = 49 branches, 21 cells,\n    median). At offsets > 20 μm, the fluorescence signal plateaued at 11% (median, IQR: 7 - 24%) of\n    maximum\n  data: dataset\n  expected:\n  - quantity: median half-maximum offset\n    value: 4\n    tolerance: 0.4\n    unit: µm\n  - quantity: median plateau beyond 20 µm\n    value: 11\n    tolerance: 1.1\n    unit: \"%\"\n  criterion: Rectangular ROIs shifted in 5 µm steps up to 25 µm from the branch centre; -dF during\n    bAPs normalized to 0 µm (legend). Half offset by linear interpolation, plateau as the mean of\n    the 20 and 25 µm points (standard choices). Reproduced when both medians are within tolerance.\n    The 5 µm step makes the half offset coarse; the tolerance of 0.4 µm is the protocol's 10%.\n- id: fig1-denoising-variance\n  statement: The PCA-denoised voltage maps accounted for more than 93% of the variance of the raw\n    data, and the first five principal components held more than 96% of the pixel waveform variance.\n  source: Results, paragraph 3; Methods, PCA-based filtering; Figure S7b\n  quote: voltage maps which accounted for > 93% of the variance in the raw data\n  data: dataset\n  expected:\n  - quantity: variance of raw data explained by the first five components\n    value: 96\n    tolerance: 9.6\n    unit: \"%\"\n  criterion: For the stimulus-triggered average movie of Fig. S7a (distal stimulus, 11 trials, the\n    Fig. 3a recording), PCA of the pixel waveforms. The paper gives > 93% and > 96%; reproduced\n    when the first five components explain at least 93% of the variance.\n- id: fig3-cheriff-current\n  statement: From cumulative eYFP fluorescence, dendrite-targeted optogenetic stimulation drives\n    dendritic CheRiff currents of about 130 pA.\n  source: Results, Distal dendritic depolarization favors dendritic spikes, paragraph 3\n  quote: Based on the cumulative eYFP fluorescence evoked by our dendrite-targeted optogenetic\n    stimulation, we estimate dendritic CheRiff currents of ~130 pA\n  data: dataset\n  expected:\n  - quantity: estimated dendritic CheRiff current\n    value: 130\n    tolerance: 13\n    unit: pA\n  criterion: The paper gives no method beyond the eYFP to charge calibration of Fig. S3e. Reading,\n    charge per eYFP unit from the soma calibrations (Fig. S3e) applied to the cumulative eYFP of\n    dendrite-targeted stimuli, divided by the stimulus duration. If the calibration recordings or\n    the eYFP images are not in the dataset, the claim cannot be tested; the paper's own method is\n    otherwise too sparse, and a result outside tolerance is methods_underspecified, not\n    not_reproduced.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001266/10.1038-s41467-025-55819-9.yaml paper/10.1038-s41467-025-55819-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s+[^ -][^:]*: .*" claims/001266/10.1038-s41467-025-55819-9.yaml | grep -vE "^\S+:\s+(- )?[a-z_]+: " | head; grep -nE "^  (  )?[a-z_]+: .*: " claims/001266/10.1038-s41467-025-55819-9.yaml | grep -v "'"
```

```
534:    significantly decreased (control: 44 ± 15%, TTX: 11 ± 8%, mean ± s.e.m., n = 4 cells from 3
762:    (0.5 s: AUC 4.5 ± 2.0, mean ± s.d., 2.5 s: AUC 4.0 ± 2.0, mean ± s.d., p = 0.19, n = 7 cells from
1048:    median). At offsets > 20 μm, the fluorescence signal plateaued at 11% (median, IQR: 7 - 24%) of
```

**Agent calls Bash**

```bash
cd claims/001266; python - <<'E'
import re
p='10.1038-s41467-025-55819-9.yaml'
s=open(p).read()
lines=s.split('\n')
out=[];i=0
while i<len(lines):
    l=lines[i]
    m=re.match(r'^(  quote: )(.*)$',l)
    if m:
        block=[l]; j=i+1
        while j<len(lines) and lines[j].startswith('    ') : block.append(lines[j]); j+=1
        text=' '.join([m.group(2)]+[b.strip() for b in block[1:]])
        if ': ' in text and not m.group(2).startswith("'"):
            first=m.group(1)+"'"+m.group(2)
            block=[first]+block[1:]
            block[-1]=block[-1]+"'"
        out+=block; i=j; continue
    out.append(l); i+=1
open(p,'w').write('\n'.join(out))
E
cd ../..; python tools/claims_check.py claims/001266/10.1038-s41467-025-55819-9.yaml paper/10.1038-s41467-025-55819-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/001266/10.1038-s41467-025-55819-9.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001266/10.1038-s41467-025-55819-9.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
from collections import Counter;print(Counter(x.get('data','dataset') for x in c))"
```

```
55 55 14 20 55 30
Counter({'dataset': 34, 'with_labels': 17, 'with_inputs': 4})
```

**Agent**

I wrote `claims/001266/10.1038-s41467-025-55819-9.yaml` with 55 claims. The checker passes every quote but exits with one problem: it cannot find the p-value 5.0 × 10⁻⁴ in figs24-drugs-selective. The Fig. S24 legend prints it as "p = 5.0 x 10-4", a form the checker doesn't recognise. I confirmed it by reading and left both the quote and the checker as they are. Nothing is committed.

**Text read.** The version of record (PMC11794848, Europe PMC full text) with its Methods. Also read: the Supplementary Information (Figs. S1 to S25), the Peer Review File and the Description of Additional Supplementary Files. The Reporting Summary had no extracted text. The other file under `paper/` is an earlier bioRxiv preprint with a different title, so I did not use it.

**Code.** The paper links no analysis code; the analysis was done in MATLAB and not published. Its only code is two simulation packages from the journal site (no repository or commit exists), and I recorded their sha256 hashes:
- **Supplementary Software 1:** the NEURON CA1 model.
- **Supplementary Software 2:** the two-compartment Izhikevich model. Its script differs from the Methods in two values (somatic reset −65 against −55, initial dendritic u −18 against −13). The Methods' values are the main reading and the script's are a variant.

**Outside material.** The dandiset's description points to the paper's Source Data file, which maps DANDI file names to figure panels and gives per-cell values. I pinned it by URL and sha256 and read only its index sheet. The dandiset appears to hold mainly example recordings for each panel. Whether it holds the pooled recordings is for the author to find.

**Claims.** 55 in total: one link claim (the Source Data index) and 54 findings.
- **Quotes:** all 55 have one, so none needed `inferred`.
- **Statistics:** 14 claims carry 20 statistical entries.
- **Expected values:** 30 claims have them. Tolerances are the paper's s.e.m. or s.d. where it gives one, otherwise 10%.
- **Criteria:** every claim has one.
- **Data:** 34 use the dataset, 17 use it with the Source Data index as labels, and 4 are model claims that use the paper's simulation code.

**Details the paper leaves open, and the readings named:**
- **High-pass filter for spike detection:** a 20 ms moving median, or a zero-phase Butterworth at 20 Hz.
- **dSpike threshold:** at the trough of the bimodal distal amplitude histogram, as Figs. 2b and S10c show. Pairing distal events with bAPs (within 5 ms) and the somatic threshold are standard choices.
- **AUC integration window:** until the cumulative area stops rising, or to the end of the stimulus epoch.
- **Which files are which panels:** the legend's labels and the file names differ (Fig. 2 "D1" is file D3; Fig. 3 "D2" could be file D2 or D4). Files are matched to panels by the legend's trial and event counts, and both readings for D2 are run.
- **Length constant (255 µm):** which 93 spikes, and whether the exponential fit has an offset.
- **Peak distance (313 µm):** ratio of averages, or average of single-trial ratios.
- **bAP velocity:** a line fitted to distance against delay, or the mean of segment velocities.
- **Fig. 3i:** stimulus distance as the eYFP centroid or the nearest point of the stimulus polygon; plateau as the logistic asymptote or the mean beyond 300 µm.
- **Ramp 92%:** text says 188 ramps, the Fig. S13 legend says 225 bAPs; both readings run.
- **Fig. 4b window times:** per-trial first and last dSpike, or binned pooled fractions.
- **Fig. 5d:** the fit forms, with the sign of the time offset read from the legend's fit ranges.
- **Fig. 5f and 5h:** the text gives 7 cells and the legends 8; both are run.
- **Fig. S18e:** which Ni²⁺ concentration it pools.
- **Fig. S24:** which response its p-values compare.
- **Fig. S25:** "dSpike probability by any bAP" as a fraction of bAPs or of trials.
- **Undefined measures:** the noise-equivalent voltage and the ~130 pA CheRiff current estimate have no stated method.
- **No test given:** for claims such as bimodality, "two motifs" and the 15 ms rule, the criteria name a test and say that it is not the paper's.

**Places where the paper disagrees with itself (recorded as found):**
- 4-AP: the text gives p < 0.001 and the legend p = 0.001.
- Temperature, any bAP: the text gives p = 0.02 and the legend p = 0.03.
- Fig. 5f and 5h: n = 7 in the text and n = 8 in the legends.

**Missing from the paper:** nothing that would stop the claims file. The gaps that matter are the missing analysis code and the unspecified filter, threshold and integration window. These are named as open in the criteria, with the readings listed above.

## End of run

36 turns, 8 minutes, result: success.
