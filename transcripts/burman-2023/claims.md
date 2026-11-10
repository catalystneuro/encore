# burman-2023 · claims · run 42756855333

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i burman; ls claims | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i burman; ls paper | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 198
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; wc -c paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d35adccd-ae5e-4b4f-a5fd-2a7e5740e973/tool-results/bmqfbhocf.txt",
 "limit": 260
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
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
tail -60 /home/runner/.claude/projects/-home-runner-work-encore-encore/d35adccd-ae5e-4b4f-a5fd-2a7e5740e973/tool-results/bmqfbhocf.txt; grep -n "data: elsewhere\|data_missing\|kind:" claims/fouke-2025.yaml | head; cat papers/datasets/burman-2023.yaml 2>/dev/null; grep -n burman papers/keys.yaml; head -50 paper/10.1016-j.neuron.2023.08.005.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Protocol and example read. The paper text is 73,046 lines long, so I'm checking its structure next.

**Agent calls Bash**

```bash
cd paper; f=10.1016-j.neuron.2023.08.005.txt; wc -c $f; grep -c "^$" $f; sed -n 1,40p $f | cut -c1-200
```

```
73046 10.1016-j.neuron.2023.08.005.txt
62
DOI: 10.1016/j.neuron.2023.08.005
Version: version of record
Source: europe_pmc+crossref (find_reuse cache)
Stored: 2026-11-09
Extracted: as fetched
------------------------------------------------------------------------
pmc Neuron Neuron Neuron 0896-6273 1097-4199 Cell Press 11913778 S0896-6273(23)00586-X 10.1016/j.neuron.2023.08.005 Report Active cortical networks promote shunting fast synaptic inhibition in vivo Bu

[HYPERLINKS]
https://briansimulator.org/
https://scicrunch.org/resolver/SCR_002998
https://imagej.net/
https://scicrunch.org/resolver/SCR_003070
https://scicrunch.org/resolver/SCR_001622
http://www.neuron.yale.edu
https://scicrunch.org/resolver/SCR_005393
http://www.numpy.org
https://scicrunch.org/resolver/SCR_008633
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1016-j.neuron.2023.08.005.txt; awk '{print NR": "length($0)}' $f | sort -t: -k2 -n -r | head; sed -n 7p $f | fold -w 2000 | head -c 6000
```

```
7: 69635
124: 85
32: 74
6: 72
3: 46
30: 44
26: 41
24: 41
22: 41
19: 41
pmc Neuron Neuron Neuron 0896-6273 1097-4199 Cell Press 11913778 S0896-6273(23)00586-X 10.1016/j.neuron.2023.08.005 Report Active cortical networks promote shunting fast synaptic inhibition in vivo Burman Richard J. 1 2 4 Brodersen Paul J.N. 1 4 Raimondo Joseph V. 3 Sen Arjune 2 Akerman Colin J. [removed: an e-mail address] 1 5 ∗ 1 Department of Pharmacology, University of Oxford, Oxford, OX1 3QT, UK 2 Oxford Epilepsy Research Group, Nuffield Department of Clinical Neurosciences, University of Oxford, Oxford, OX3 9DU, UK 3 Division of Cell Biology, Department of Human Biology, Neuroscience Institute and Institute of Infectious Diseases and Molecular Medicine, University of Cape Town, Cape Town, 7935, South Africa ∗ Corresponding author [removed: an e-mail address] 4 These authors contributed equally 5 Lead contact 15 11 2023 15 11 2023 111 22 3531 3540.e6 1 3 2023 3 7 2023 4 8 2023 © 2023 The Author(s) 2023 https://creativecommons.org/licenses/by/4.0/ This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Summary Fast synaptic inhibition determines neuronal response properties in the mammalian brain and is mediated by chloride-permeable ionotropic GABA-A receptors (GABA A Rs). Despite their fundamental role, it is still not known how GABA A Rs signal in the intact brain. Here, we use in vivo gramicidin recordings to investigate synaptic GABA A R signaling in mouse cortical pyramidal neurons under conditions that preserve native transmembrane chloride gradients. In anesthetized cortex, synaptic GABA A Rs exert classic hyperpolarizing effects. In contrast, GABA A R-mediated synaptic signaling in awake cortex is found to be predominantly shunting. This is due to more depolarized GABA A R equilibrium potentials (E GABAAR ), which are shown to result from the high levels of synaptic activity that characterize awake cortical networks. Synaptic E GABAAR obs
[... 2 more lines not kept]
```

**Agent**

The text is a single 70,000-character line. I'll fold it into a temp file to read it.

**Agent calls Bash**

```bash
cd paper; sed -n 7p 10.1016-j.neuron.2023.08.005.txt | fold -s -w 180 > $TMPDIR/b.txt; wc -l $TMPDIR/b.txt; grep -n -o "STAR★Methods\|STAR Methods\|Supplemental\|Figure S[0-9]\|Quantification and statistical analysis\|Figure [0-9]\. \|Method details\|References\|Acknowledg" $TMPDIR/b.txt | sort -u -t: -k2 | head -60; ls
```

```
397 /tmp/claude-1001/b.txt
388:Acknowledg
259:Figure S3
188:Method details
315:References
173:STAR★Methods
386:Supplemental
10.1016-j.neuron.2023.08.005.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/b.txt",
 "offset": 14,
 "limit": 160
}
```

```
14	gramicidin recordings reveal the driving force for synaptic GABA A Rs • Synaptic E GABAAR favors shunting inhibition in the awake cortex • The high levels of cortical activity 
15	raise E GABAAR to promote shunting inhibition • Shunting inhibition promotes local network desynchronization and response flexibility In this study, Burman et al. demonstrate that 
16	the way in which fast synaptic inhibition operates in the intact mammalian cortex is linked to the level of activity within the network. The authors further show that this dynamic 
17	inhibition has profound implications for how the cortex responds to incoming stimuli. Keywords synaptic inhibition GABA-A receptor signaling cortex equilibrium potential ionic 
18	driving force network activity population coupling stimulus discrimination Published: September 3, 2023 Introduction Synaptic inhibition is tightly coupled to synaptic excitation 
19	and plays a key role in cortical computations, 1 including modulating sensory response properties 2 , 3 and oscillatory activities. 4 Fast synaptic inhibition in cortex is 
20	mediated by ionotropic GABA-A receptors (GABA A Rs), which are mainly permeable to chloride (Cl − ). 5 , 6 , 7 The inhibitory effects that GABA A Rs have upon a neuron therefore 
21	depend upon the local transmembrane Cl − gradient, which reflects a dynamic equilibrium between Cl − extrusion and intrusion processes. 8 , 9 , 10 When the GABA A R equilibrium 
22	potential (E GABAAR ) is more negative than the membrane potential (V m ), GABA A R activation will lead to membrane hyperpolarization. If E GABAAR is close to V m , GABA A R 
23	activation would have minimal effects upon V m , and the inhibitory effects would be primarily mediated by local effects on the membrane resistance (R m )—a phenomenon known as 
24	“shunting inhibition.” 11 , 12 These different forms of signaling determine how inhibition is temporally integrated with incoming excitatory synaptic inputs. 13 , 14 Thus, 
25	appreciatin
[... 148 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/b.txt",
 "offset": 173,
 "limit": 145
}
```

```
173	These findings support the general idea that dynamic changes in GABA A R-mediated synaptic inhibition can be used to optimize cortical function. STAR★Methods Key resources table 
174	REAGENT or RESOURCE SOURCE IDENTIFIER Antibodies Streptavidin-Cy3 ThermoFisher 438315 Chemicals, peptides, and recombinant proteins Biocytin Merck 576-19-2 NBQX 
175	(2,3-dihydroxy-6-nitro-7-sulfamoylbenzo (F) quinoxaline) Torcis 1044 Urethane Merck U2500 VU0463271 Torcis 4719 Deposited data Neuropixels dataset Claar et al. 29 , 30 DANDI 
176	Archive: 000458 Experimental models: Organisms/strains Gad2-IRES-Cre mice Jackson Labs RRID:IMSR_JAX:010802 Ai32(RCL-ChR2(H134R)/EYFP) Jackson Labs RRID:IMSR_JAX:012569 Software 
177	and algorithms Brian Simulator https://briansimulator.org/ RRID: SCR_002998 ImageJ https://imagej.net/ RRID: SCR_003070 MATLAB MathWorks RRID: SCR_001622 NEURON 
178	http://www.neuron.yale.edu RRID: SCR_005393 NumPy http://www.numpy.org RRID: SCR_008633 pCLAMP 11 Software Molecular Devices RRID: SCR_011323 pyABF 2.3.7 Harden (2022) 47 
179	https://github.com/swharden/pyABF Python 3.10.9 https://www.python.org/ RRID: SCR_008394 Scipy http://www.scipy.org/ RRID: SCR_008058 ZEISS Imaging Suite http://www.zeiss.com 
180	RRID: SCR_013672 Other Custom code (Python) This paper https://gist.github.com/paulbrodersen Custom code (Matlab) This paper https://github.com/richardjburman Digidata 1550B Data 
181	Acquisition System Molecular Devices Digidata 1550B1 HumBug noise eliminator (50Hz) Digitimer SKU: D.HUMBUG LSM 880 microscope Zeiss - MultiClamp 700B Microelectrode Amplifier 
182	Molecular Devices N/A Optopatcher A-M Systems 663849 Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will 
183	be fulfilled by the lead contact, Colin Akerman ( [removed: an e-mail address] ). Materials availability No new materials were generated in this study. Experimental model and 
184	subject details All mice were bred
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 380,397p $TMPDIR/b.txt; grep -n -o ".\{200\}Figure S[4-7].\{300\}" $TMPDIR/b.txt | head
```

```
Vogels T.P. Sprekeler H. Zenke F. Clopath C. Gerstner W. Inhibitory plasticity balances excitation and inhibition in sensory pathways and memory networks Science 334 2011 1569 
1573 10.1126/science.1211095 22075724 58 Hines M.L. Carnevale N.T. The NEURON simulation environment Neural Comput. 9 1997 1179 1209 10.1162/neco.1997.9.6.1179 9248061 59 Ascoli 
G.A. Donohue D.E. Halavi M. NeuroMorpho.Org: a central resource for neuronal morphologies J. Neurosci. 27 2007 9247 9251 10.1523/JNEUROSCI.2055-07.2007 17728438 60 Madisen L. 
Garner A.R. Shimaoka D. Chuong A.S. Klapoetke N.C. Li L. van der Bourg A. Niino Y. Egolf L. Monetti C. Transgenic mice for intersectional targeting of neural sensors and effectors 
with high specificity and performance Neuron 85 2015 942 958 10.1016/j.neuron.2015.02.022 25741722 61 Virtanen P. Gommers R. Oliphant T.E. Haberland M. Reddy T. Cournapeau D. 
Burovski E. Peterson P. Weckesser W. Bright J. SciPy 1.0: fundamental algorithms for scientific computing in Python Nat. Methods 17 2020 261 272 10.1038/s41592-019-0686-2 32015543 
Supplemental information Document S1. Figures S1–S7 Document S2. Article plus supplemental information Data and code availability Custom code used in analysis of data is publicly 
available as of the date of publication (links provided in the key resources table ). Any additional materials required to reanalyze data are available on request to the lead 
contact. Acknowledgments We would like to thank members of the Akerman lab for advice and comments. We thank Mateo Velez-Fort, Christopher Pugh, and Troy Margrie (Sainsbury 
Wellcome Centre) for their help in setting up the in vivo patch-clamp recordings. We thank Leslie Claar at the Allen Institute for making data publicly available, providing 
assistance with interpreting the data, and commenting on the results of our analyses. We thank Lex Kravitz, Luigi Petrucco, and Ethan Tyler for sharing their mouse illustrations 
on the Sci-Draw opensource platform and Ed Mann
[... 6 more lines not kept]
```

**Agent**

The supplement (Document S1, Figures S1 to S7) is not in the text. Before deciding whether to stop, I'm checking how earlier claims files in the repo handled a missing supplement.

**Agent calls Bash**

```bash
cd  grep -il "supplement" claims/*.yaml | head -40; grep -h -i "supplement.*\(not\|missing\|absent\)" claims/*.yaml | head -20; grep -n -i "supplement" docs/pilot-notes.md | head -20
```

```
claims/alasfour-2024.yaml
claims/armstrong-2026.yaml
claims/ashworth-2025.yaml
claims/athalye-2023.yaml
claims/bakalar-2023.yaml
claims/bech-2026.yaml
claims/bellvila-2026.yaml
claims/bennett-2024.yaml
claims/berg-2020.yaml
claims/boran-2019.yaml
claims/boran-2022.yaml
claims/bouchard-2013.yaml
claims/bruno-2017.yaml
claims/buccino-2020.yaml
claims/buccino-2024.yaml
claims/calvigioni-2023.yaml
claims/chantranupong-2023.yaml
claims/chartrand-2023.yaml
claims/chaunsali-2025.yaml
claims/chen-2017.yaml
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/burman-2023.yaml; grep -rn "000458" papers/datasets/*.yaml | head; head -40 claims/claar-2023.yaml
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.neuron.2023.08.005
title: Active cortical networks promote shunting fast synaptic inhibition in vivo
datasets:
- archive: dandi
  id: 000458
  relation: reuses
papers/datasets/burman-2023.yaml:7:  id: 000458
papers/datasets/claar-2023.yaml:6:  id: 000458
# Claims for Claar, Rembado, Kuyat, Russo, Marks, Olsen & Koch (2023) on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
# pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read: the version of record (eLife 12, RP84630, 2023), full text as served by Europe PMC
# (paper/10.7554-elife.84630.txt), with Results, Discussion, Methods, all figure legends including
# the figure supplement legends, the eLife assessment, the public reviews and the authors' response.
# eLife has no separate supplementary text; the figure supplements are figures whose legends are in
# the text. No PDF was supplied and none was needed. The bioRxiv preprint (10.1101/2022.07.22.501195,
# the paper the dandiset names) is also under paper/ and was not used; the version of record replaces it.
[... 30 more lines not kept]
```

**Agent**

Now the paper's linked code: Python gists by paulbrodersen and a Matlab repo by richardjburman.

**Agent calls Bash**

```bash
curl -s "https://api.github.com/users/paulbrodersen/gists?per_page=100" | python3 -c "import json,sys; [print(g['id'], g['updated_at'], g['description'], list(g['files'])) for g in json.load(sys.stdin)]" | head -80; echo ---; curl -s "https://api.github.com/users/richardjburman/repos?per_page=100" | python3 -c "import json,sys; [print(r['name'], r['pushed_at'], r['description']) for r in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for g in a77bcf5e06ae27fa96923cb313a02ccf 2ce61e4e57c7659b727d30e3e1e0128f; do curl -s https://api.github.com/gists/$g | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['id'], [h['version'] for h in d['history']]); f=list(d['files'].values())[0]; open(f['filename'],'w').write(f['content']); print(f['filename'], f['truncated'])"; done; wc -l *.py; git clone -q https://github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR.git mrepo && cd mrepo && git log --oneline | head -3 && find . -type f -not -path './.git/*' | head -40
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; cat burman_et_al_2023_neuropixel_data_analysis.py; curl -s https://api.github.com/gists/a77bcf5e06ae27fa96923cb313a02ccf | python3 -c "import json,sys; d=json.load(sys.stdin); [print(h['version'],h['committed_at']) for h in d['history']]"; cd mrepo; git rev-parse HEAD; cat README.md
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -n "data:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c; grep -B12 "data: elsewhere" claims/*.yaml | grep -i -m5 "simulat\|model"; grep -n "kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c; ls tools; sed -n 1,60p tools/claims_check.py | head -80
```

```
1 (Takatoh
      1 The
      1 across
      1 and
    182 dataset
      4 dataset).
      1 decoder
      1 default).
    440 elsewhere
      2 files.
      1 on
      1 server
      1 tested;
      2 the
    261 with_inputs
    334 with_labels
      1 wrap,
claims/buccino-2024.yaml-    alejoe91/multimodalfitting at commit 24e8e61, cell_models/<cell>/morphology_corrected.swc
claims/buccino-2024.yaml-  statement: The ground-truth model's rheobase, estimated with a 270 ms step, is 150 pA.
claims/buccino-2024.yaml-    (estimated using a 270 ms step). For our groundtruth model, the rheobase current was 150 pA
[... 99 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));t=json.dumps(s,indent=1);print(t[6000:12000])"; grep -l "relation: reuses" papers/datasets/*.yaml | head -5
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p claims/alasfour-2024.yaml; grep -n "data:\|where:" claims/alasfour-2024.yaml | sort | uniq -c | sort -rn | head; grep -n -i "not public\|not deposited\|no public" claims/alasfour-2024.yaml claims/kussovska-2025.yaml claims/okuno-2025.yaml | head
```

```
# Claims for Alasfour & Gilja (2024), Front. Hum. Neurosci. 18:1388267, "Consistent
# spectro-spatial features of human ECoG successfully decode naturalistic behavioral states",
# on dandiset 000055 (AJILE12).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. The version of record from PubMed Central (PMC11169785), in
# paper/10.3389-fnhum.2024.1388267.txt: abstract, Introduction, Methods, Results, figure legends
# (Figures 1 to 7), Table 1, Discussion and Data availability statement. The paper has no
# supplement (PMC lists none, and the text cites none). No PDF was supplied, so the figures
# could not be read; every claim rests on the text and the legends. Values shown only in the
# figures (per-feature accuracies, confidence intervals, the finite chance level, the
# per-participant matrices and curves) are not known here.
#
# Code read. None. The paper links no analysis code and names no software or toolbox.
#
# Data the paper used. Five of the twelve AJILE12 participants (Peterson et al., 2022), 2 male
# and 3 female, numbered 1, 2, 4, 5 and 8 in Table 1, chosen as those with at least 1 h of the
# behaviours of interest, in epilepsy monitoring with ECoG placed for clinical needs.
# Post-surgical days 3 to 7 only. ECoG at 1 kHz, preprocessed as in AJILE12 (median removed,
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -B3 -A3 "on request\|not deposited\|not public" claims/*.yaml | grep -i "data:\|where:\|criterion\|on request" | head -20; grep -n -A2 "simulat" claims/claar-2023.yaml | head
```

```
claims/berg-2020.yaml-922-  data: elsewhere
claims/berg-2020.yaml:923:  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
claims/berg-2020.yaml-925-  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
claims/dembrow-2024.yaml-13-# analysis code supplies it where it printed one, and the criterion says so; the code's
claims/dembrow-2024.yaml-406-  criterion: >-
claims/dembrow-2024.yaml-975-  criterion: >-
claims/duszkiewicz-2024.yaml-787-  - Open, the Fig. 5e legend gives n = (83, 52) for PoSub-FS cells where the Methods leave 46; the criterion's reading of 46 cannot be confirmed from the text.
claims/funamizu-2016.yaml:11:# are "available from corresponding author upon request"; it links no code, so none was read.
claims/hickman-2026.yaml:24:# (available on request); the evoked-potential and saturation claims (Figures 1L, 2, 3, S1, S2) rest
claims/ishii-2025.yaml-56-  data: with_inputs
claims/ishii-2025.yaml-57-  criterion: Densities computed here as in fig2c-brain-wide-increase (ClearMap registration to the
claims/kalogriopoulos-2024.yaml:16:# study are available upon request." No repository was read. Its Data availability says no
claims/kalogriopoulos-2024.yaml-513-  - ed12cd-expression-baseline, criterion. The baseline value (mean of pre-DCZ sweeps) was a choice made by the writer; the paper does not define it, so it is now named as open with readings B1 and B2. The sweep and cell exclusions, which depend on the A1, A2 and Rin window readings of fig4i-rmp, are now named.
claims/kalogriopoulos-2024.yaml-514-  - ed12g-expression-rmp, criterion. The legend's "not specifically linked" can mean no correlation in either group or no correlation specific to DCZ plus mCherry; both readings are now named, since the table in Extended Data Fig. 12h cannot be read from the text. The sweep exclusions and their readings are now named.
claims/kalogriopoulos-2024.yaml:516:  - Open, slice claims. The ch
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 915,930p claims/berg-2020.yaml; sed -n 30,45p claims/kennedy-2020.yaml; grep -n -A6 "^- id:" claims/kennedy-2020.yaml | grep -m6 "data:\|where:"; sed -n 20,30p claims/hickman-2026.yaml; grep -n "data:\|where:" claims/hickman-2026.yaml | head -5
```

```
neurons are not, and NEFH, the gene coding the SMI-32 epitope, is higher in deep FREM3 and
    CARM1P1 than in COL22A1 and the superficial types.
  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph
    7; Figure 6e and 6f
  quote: The large FREM3 and CARM1P1 neurons were SMI-32ir, while COL22A1 neurons were not SMI-32ir.
    Furthermore, the gene coding SMI-32, NEFH, also shows increased expression in deep FREM3 and
    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).
  data: elsewhere
  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
    NEFH expression from the Allen Brain Map RNA-seq data, not pinned
  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
# sweeps of 17 to 20 kHz at 85 dB) and a 2 kHz tone. Traces come from CNMF-E after manual screening;
# 187.3 cells were imaged per day and cells were registered across the three days (roughly half).
# Responses are in units of the standard deviation of a 30 s pre-stimulus baseline (Methods, Units of
# neuronal activation). The fiber photometry (Fig 1, ED 1 and 3), the open field and home cage
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 1,450p burman_et_al_2023_neuronal_network_simulation.py | grep -v "^\s*$" | head -400
```

```
#!/usr/bin/env python
# -*- coding: utf-8 -*
"""Simulate a LIF neuronal network with variable EGABA and structured inputs.
Copyright (C) 2023 by Paul Brodersen.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version. This program is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details. You
should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/.
"""
import time
import pathlib
import brian2 as b2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
[... 369 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -h -i "tolerance.*SEM\|SEM.*tolerance\|± .*as.*tolerance\|stated spread" claims/*.yaml | head -12
```

```
Tolerances are the paper's stated spread for the rates, one 5 ms bin for the epoch 2 peak time
    shown. The SEM is the regression's standard error. The tolerance is the paper's SEM. The
    the tolerance is the paper's SEM. The ratio uses the first-ramp slope under the same reading.
    cells of each class (Table S1). The tolerance is the paper's stated spread (protocol
    stated spread over cells. Reproduced when all six means are within tolerance; partially
    median, and the three means are within the stated spread.
    within the stated spread; the class medians, whose order may differ given the spread, are
    the tolerance, and the SD and SEM over mice are both reported. Reproduced when the four means
    trials of the amplitude. Tolerances are the paper's stated spread. Open, with readings run
    readings; tolerance the stated spread.
    count); the others are the stated spread, or 10% for the totals. A neuron counts as
    median over neurons. 10% tolerance, as the stated spreads (2.11 and 4.92 Hz) are wider than
```

**Agent**

Most of the method is settled now. Last code check: a quick look at what the Matlab/NEURON repo holds, so I can describe it accurately.

**Agent calls Bash**

```bash
cd $TMPDIR/mrepo; sed 's/\\[a-z0-9]*//g' "NEURON Modelling/NEURON_Modelling_ReadMe.rtf" | tr -s ' \n' | head -c 1500; echo; head -30 "NEURON Modelling/Matlab_code/NEURON_Egaba_Analysis.m"; grep -n "0.9\|Rs\|90" "NEURON Modelling/Matlab_code/dependencies/Sz_ramp_calc.m" | head
```

```
{
{ Helvetica;}
{;;}
{*;;}
 //ReadMe
This code was written by Joseph Raimondo but heavily based on previous code written by Blake Richards
2/2/2023
Instructions:
Install NEURON
Ensure that a '91data'92 directory exists in the folder within you wish to run the simulation.
Paramaters are set in the '91setParameters.hoc'92 file.
To run the simulation type: 'nrngui mosinit.hoc' at the command.
Data will be output to the '91data'92 folder.
The file suffix number reflects the simulation number - ie each number reflects a particular set Egaba.
'91-t'92 is time
'91-v'92 is the command voltage
'91-i'92 is the recorded current
'91-vmem'92 is the recorded voltage at the soma
These output traces can then be analysed in Matlab using the '91NEURON_Egaba_Analysis.m'92 script
}
[... 32 more lines not kept]
```

**Agent**

Code read and the method is settled. I'm writing the claims file now, generated from Python so YAML quoting is handled safely.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen; echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/gen/make.py",
 "content": "import yaml\n\nHEADER = \"\"\"\\\n# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,\n# \"Active cortical networks promote shunting fast synaptic inhibition in vivo\", on dandiset 000458.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),\n# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of\n# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.\n# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF\n# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is\n# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7\n# rest on the main-text sentences that cite them, and their tests are not known here.\n#\n# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision\n# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads\n# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,\n# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and\n# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.\n# (2) gist.github.com/paulbrodersen/2ce61e4e790e2a351d52d921f848e122, revision\n# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the\n# Brian 2 network of Figure 4E to 4H and Figure S7, one run per call. (3)\n# github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR, commit\n# a404c3ec9e8ba6865500ec5e1138835df4398c08: the NEURON model of an L2/3 pyramidal neuron and the\n# Matlab analysis of its simulated ramps (Figure S4; 90% series resistance correction). No code for\n# the patch-clamp analysis is linked (the Methods say it was custom Python).\n#\n# Data the paper used, as it reports them.\n# Patch clamp (Figures 1 to 3, S1 to S5). Gad2-IRES-Cre x Ai32 (ChR2(H134R)-YFP in Gad2 neurons)\n# mice of both sexes, 6 to 8 weeks old. Gramicidin perforated patch recordings of L2/3 pyramidal\n# neurons in V1, under urethane anesthesia or awake and head-fixed, with local VU0463271 (KCC2\n# block, anesthetized) or NBQX (awake). 473 nm light through the pipette (Optopatcher) evokes\n# GABA-A receptor responses; 20 kHz sampling. Measured: series and membrane resistance,\n# spontaneous Vm in current clamp (5 min), light-evoked current-clamp responses (15 sweeps, 10 ms\n# pulse), and voltage-clamp ramp (-130 to -30 mV, 150 ms, baseline and light ramps) and step\n# protocols, from which RMP, E_GABAAR, DF_GABAAR and the GABA conductance are taken. None of\n# these recordings is in DANDI:000458, and the paper deposits them nowhere (\"Any additional\n# materials required to reanalyze data are available on request to the lead contact\"). Their\n# claims are kept, as data the paper recorded; they cannot be tested on this dandiset.\n# Neuropixels (Figures 4A to 4D, S6). The paper reanalyzes the Allen Institute dataset of Claar et\n# al. (2023), DANDI:000458 (key resources table; claims/claar-2023.yaml describes it): head-fixed\n# mice with up to three Neuropixels probes and a bipolar stimulating electrode in layer 2/3 or 5/6\n# of SSp or MOs, single electrical pulses delivered awake and under isoflurane. The paper uses 17\n# recordings in 16 mice (sub-569073 has two sessions); units are regular spiking units of the\n# stimulated area, 662 after exclusion. Measured variables used: unit spike times, waveform\n# duration and location; trial times, stimulus type, behavioral epoch, validity and stimulation\n# target region.\n# Network models (Figures 4E to 4H, S7) are generated by the paper's simulation code (data\n# elsewhere, where names the code).\n#\n# Method for the claims on DANDI:000458, fixed from the Methods (\"Pre-processing of Neuropixels\n# dataset\", \"Characterization of stimulus-evoked spiking responses\", \"Statistical analyses\") and\n# the analysis gist (1). Cited in the criteria as N1 to N8.\n# N1 Sessions. The 17 sessions listed in the gist (see dataset-sessions-link).\n# N2 Units. Regular spiking units, waveform duration of 0.4 ms or more (Methods; the gist uses\n#    strictly more than 0.4, which is shown as a variant). Area, open between two readings:\n#    (A1) the Methods, units whose location annotation is \"SSp-ll\" or \"SSp-tr\", or \"MOs\",\n#    whichever area was electrically stimulated in the session; (A2) the gist, units whose\n#    location's first three characters are among the session's estim_target_region values of\n#    its electrical trials.\n# N3 Trials. Electrical stimulus trials with is_valid true, behavioral_epoch \"awake\" for awake\n#    and \"isoflurane\" for anesthetized; all stimulus intensities and stimulation sites of a\n#    session pooled; times taken from each trial's stop_time (gist; the Methods say only\n#    \"following an electrical stimulus\").\n# N4 Window. Spikes from 2 to 12 ms after the stimulus (Methods and gist), in 1 ms bins (10\n#    bins). The Methods' \"12 ms following stimulus onset\" for the histograms is read as this\n#    window, as the gist computes it.\n# N5 Entropy. Per unit and condition, the histogram of its spikes over all trials, normalized\n#    to sum to 1, entropy by scipy.stats.entropy (natural log, nats); undefined for fewer than\n#    two spikes (gist).\n# N6 Synchrony. Per trial, the histogram of the spikes of all the session's selected units (the\n#    unit itself included), divided by its total spike count; for each spike of a unit, the\n#    value of that histogram at the spike's bin; the unit's synchrony is the mean over all its\n#    spikes in all trials (Methods and gist).\n# N7 Evoked firing rate and exclusion. Units with an evoked rate below 0.1 Hz or above 200 Hz in\n#    either condition are excluded (Methods). The rate is open between two readings: (F1) the\n#    Methods, the unit's spike count in the window divided by the number of trials times 10 ms;\n#    (F2) the gist's get_firing_rate, which sums the spikes' times in ms after the stimulus\n#    (np.sum of spike_times) where a count would be expected, and divides by (the highest index\n#    of a trial with any population spike, plus one) times 10 ms. The Methods come first; F2 is\n#    the code that produced the paper's numbers. The gist does not apply the exclusion; it is\n#    taken to act on the rate column it writes. Every claim on the dandiset is run under the four\n#    readings A1F1, A1F2, A2F1 and A2F2.\n# N8 Statistics. Values are mean +- SEM over neurons and awake against anesthetized is a paired\n#    t test (scipy.stats.ttest_rel) over the neurons (Figure 4D legend; Methods). A unit with an\n#    undefined value in either condition is left out of that measure's test, a standard choice.\n#\n# Tolerances. The paper's SEM where it gives one; otherwise 10% of the reported value.\nschema_version: 2\n\"\"\"\n\nNOT_HERE = (\"Not testable on DANDI:000458, which holds only the Allen Institute Neuropixels \"\n            \"recordings; the paper's patch-clamp recordings are not deposited (available on \"\n            \"request).\")\nANOVA = (\"a one-way ANOVA over the anesthetized, awake and awake plus NBQX groups with \"\n         \"Bonferroni-corrected post hoc comparison (Methods, Statistical analyses: \\\"For data \"\n         \"used in both Figures 2 and 3\\\")\")\nSIM_WHERE = (\"Not deposited; generated by the paper's simulation code, \"\n             \"gist.github.com/paulbrodersen/2ce61e4e790e2a351d52d921f848e122 at revision f6a05661\")\nSIM_METHOD = (\"The paper's simulation gist at revision f6a05661, run 20 times (Methods, \\\"Each \"\n              \"simulation was repeated 20 times\\\"), with its defaults (100 patterns, 100 \"\n              \"repeats, 800 excitatory and 200 inhibitory neurons, E_GABA -60 mV then -80 mV in \"\n              \"the excitatory neurons). Per run and condition, the gist's entropy and synchrony \"\n              \"of each excitatory neuron, from spikes 0 to 12 ms after each input in the first \"\n              \"stimulus set of the condition; the 20 runs pooled (16,000 neurons). Random seeds \"\n              \"are not fixed by the paper and are taken as given by the gist (none set).\")\n\n\ndef mean(q, v, sem, unit):\n    return {\"quantity\": q, \"value\": v, \"tolerance\": sem, \"unit\": unit}\n\n\ndef ten(q, v, unit=None):\n    d = {\"quantity\": q, \"value\": v, \"tolerance\": round(abs(v) * 0.1, 4)}\n    if unit:\n        d[\"unit\"] = unit\n    return d\n\n\nclaims = []\nadd = claims.append\n\n# ---------------------------------------------------------------- Figure 1\nadd({\n    \"id\": \"fig1b-perforation-rs\",\n    \"statement\": \"Gramicidin perforation lowers the series resistance about 20-fold in the 10 min \"\n                 \"after gigaseal formation, from 1,126.9 to 50.2 MOhm.\",\n    \"source\": \"Results, Measuring the equilibrium potential and driving force for synaptic GABAARs \"\n              \"in vivo, paragraph 1; Figure 1B\",\n    \"quote\": \"During the 10 min following gigaseal formation we observed a 20-fold decrease in R s \"\n             \"(mean R s-0 min : 1,126.9 ± 35.8 MΩ vs. R s-10 min : 50.2 ± 3.8 MΩ)\",\n    \"expected\": [mean(\"series resistance at 0 min\", 1126.9, 35.8, \"MOhm\"),\n                 mean(\"series resistance at 10 min\", 50.2, 3.8, \"MOhm\")],\n    \"criterion\": NOT_HERE + \" Were the data available, the mean series resistance over the 10 \"\n                 \"neurons (7 mice) that met the perforation criteria (Figure 1B legend), at 0 and \"\n                 \"10 min, is compared with the expected values.\",\n})\nadd({\n    \"id\": \"fig1h-vu-egaba\",\n    \"statement\": \"Blocking KCC2 with VU0463271 shifts synaptic E_GABAAR in the depolarizing \"\n                 \"direction in anesthetized V1, from -80.9 to -70.9 mV.\",\n    \"source\": \"Figure 1H; Results, Measuring the equilibrium potential and driving force for \"\n              \"synaptic GABAARs in vivo, paragraph 3\",\n    \"quote\": \"Population data (n = 6 neurons from 6 mice) showed a depolarizing shift in \"\n             \"synaptic E GABAAR after VU (−VU: −80.9 ± 1.6 mV vs. +VU: −70.9 ± 2.6 mV; p = \"\n             \"0.002, paired t test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.002, \"n\": \"6 neurons from 6 mice\"}],\n    \"expected\": [mean(\"E_GABAAR without VU\", -80.9, 1.6, \"mV\"),\n                 mean(\"E_GABAAR with VU\", -70.9, 2.6, \"mV\")],\n    \"criterion\": NOT_HERE + \" Were the data available, E_GABAAR from the ramp protocol (Methods, \"\n                 \"GABAA receptor equilibrium potential) before and after VU, paired t test.\",\n})\nadd({\n    \"id\": \"fig1i-vu-rmp\",\n    \"statement\": \"VU0463271 does not change the resting membrane potential (-68.5 against -69.1 \"\n                 \"mV).\",\n    \"source\": \"Figure 1I\",\n    \"quote\": \"VU did not affect RMP (−VU: −68.5 ± 3.5 mV vs. +VU: −69.1 ± 2.5 mV; p = 0.73, \"\n             \"paired t test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.73, \"n\": \"6 neurons from 6 mice\"}],\n    \"expected\": [mean(\"RMP without VU\", -68.5, 3.5, \"mV\"),\n                 mean(\"RMP with VU\", -69.1, 2.5, \"mV\")],\n    \"criterion\": NOT_HERE + \" A claim of absence: were the data available, reproduced when the \"\n                 \"paper's paired t test of the ramp-derived RMP before and after VU gives p >= \"\n                 \"0.05.\",\n})\nadd({\n    \"id\": \"fig1j-vu-df\",\n    \"statement\": \"VU0463271 shifts the GABAAR driving force (RMP minus E_GABAAR) in the \"\n                 \"depolarizing direction, from 12.4 to 1.4 mV.\",\n    \"source\": \"Figure 1J\",\n    \"quote\": \"VU caused a depolarizing shift in GABA A R driving force (DF GABAAR = RMP − E \"\n             \"GABAAR , −VU: 12.4 ± 2.9 mV vs. +VU: 1.4 ± 3.0 mV; p = 0.006, paired t test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.006, \"n\": \"6 neurons from 6 mice\"}],\n    \"expected\": [mean(\"DF_GABAAR without VU\", 12.4, 2.9, \"mV\"),\n                 mean(\"DF_GABAAR with VU\", 1.4, 3.0, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"figs2-ramp-equals-step\",\n    \"statement\": \"Synaptic E_GABAAR estimated from voltage ramps is equivalent to that from \"\n                 \"voltage step protocols in the same neurons.\",\n    \"source\": \"Results, Measuring the equilibrium potential and driving force for synaptic \"\n              \"GABAARs in vivo, paragraph 2; Figure S2E (not read)\",\n    \"quote\": \"The estimates of synaptic E GABAAR from ramp protocols were equivalent to those \"\n             \"made using step protocols\",\n    \"criterion\": NOT_HERE + \" The test and numbers are in the Figure S2 legend, which is not in \"\n                 \"the text read.\",\n})\nadd({\n    \"id\": \"figs3-egaba-unrelated-amplitude-rs\",\n    \"statement\": \"Ramp estimates of E_GABAAR are not related to the amplitude of the synaptic \"\n                 \"GABAAR response or to the series resistance.\",\n    \"source\": \"Results, Measuring the equilibrium potential and driving force for synaptic \"\n              \"GABAARs in vivo, paragraph 2; Figure S3 (not read)\",\n    \"quote\": \"measurements from the ramp protocols were not related to the amplitude of the \"\n             \"synaptic GABA A R response or the neuron’s R s\",\n    \"criterion\": NOT_HERE + \" A claim of absence whose test is in the Figure S3 legend, which is \"\n                 \"not in the text read.\",\n})\n\n# ---------------------------------------------------------------- Figure 2\nadd({\n    \"id\": \"rm-awake-lower\",\n    \"statement\": \"Membrane resistance is lower in awake than in anesthetized cortex (50.6 against \"\n                 \"87.2 MOhm).\",\n    \"source\": \"Results, Awake cortex exhibits more depolarized synaptic EGABAAR and shunting fast \"\n              \"synaptic inhibition, paragraph 1\",\n    \"quote\": \"The R m was also lower in the awake recordings (An.: 87.2 ± 6.1 MΩ, n = 14 \"\n             \"neurons, 8 mice vs. Aw.: 50.6 ± 6.4 MΩ, n = 13 neurons, 10 mice, p < 0.0001, \"\n             \"unpaired t test)\",\n    \"statistics\": [{\"test\": \"unpaired t test\", \"p\": 0.0001, \"p_relation\": \"<\",\n                    \"n\": \"14 neurons from 8 anesthetized mice and 13 neurons from 10 awake mice\"}],\n    \"expected\": [mean(\"Rm anesthetized\", 87.2, 6.1, \"MOhm\"),\n                 mean(\"Rm awake\", 50.6, 6.4, \"MOhm\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig2c-vm-depolarized\",\n    \"statement\": \"Mean membrane potential is more depolarized in awake than in anesthetized \"\n                 \"cortex (-60.3 against -69.1 mV).\",\n    \"source\": \"Figure 2B and 2C; Results, Awake cortex exhibits more depolarized synaptic \"\n              \"EGABAAR and shunting fast synaptic inhibition, paragraph 1\",\n    \"quote\": \"Mean V m was more depolarized in awake cortex (An.: −69.1 ± 1.4 mV vs. Aw.: −60.3 \"\n             \"± 1.1 mV; p < 0.001, one-way ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\",\n                    \"n\": \"13 cells from 7 anesthetized mice and 12 cells from 10 awake mice\"}],\n    \"expected\": [mean(\"mean Vm anesthetized\", -69.1, 1.4, \"mV\"),\n                 mean(\"mean Vm awake\", -60.3, 1.1, \"mV\")],\n    \"criterion\": NOT_HERE + \" Were the data available, Vm from 5 min of spontaneous current-clamp \"\n                 \"activity with values above -40 mV removed (Methods, Membrane potential \"\n                 \"measurements), tested by \" + ANOVA + \".\",\n})\nadd({\n    \"id\": \"fig2d-subthreshold-fluctuation\",\n    \"statement\": \"Subthreshold membrane potential fluctuations (mean absolute dVm/dt) are larger \"\n                 \"in awake than in anesthetized cortex (6.6 against 4.9 mV/ms).\",\n    \"source\": \"Figure 2D\",\n    \"quote\": \"Mean change in subthreshold V m was greater in awake cortex (An.: 4.9 ± 0.2 mV/ms \"\n             \"vs. Aw.: 6.6 ± 0.3 mV/ms; p < 0.001, one-way ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"mean |dVm/dt| anesthetized\", 4.9, 0.2, \"mV/ms\"),\n                 mean(\"mean |dVm/dt| awake\", 6.6, 0.3, \"mV/ms\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig2f-response-polarity\",\n    \"statement\": \"Light-evoked GABAAR responses in current clamp are never depolarizing in \"\n                 \"anesthetized cortex (0 of 18) but are depolarizing in 6 of 14 awake neurons, \"\n                 \"staying close to the RMP.\",\n    \"source\": \"Figure 2F; Results, Awake cortex exhibits more depolarized synaptic EGABAAR and \"\n              \"shunting fast synaptic inhibition, paragraph 3\",\n    \"quote\": \"Responses in awake cortex produced V m deflections that remained close to the RMP \"\n             \"and could be depolarizing or hyperpolarizing (An.: Depol. 0/18 vs. Aw.: Depol. \"\n             \"6/14; p = 0.003, Fisher-Exact test)\",\n    \"statistics\": [{\"test\": \"Fisher-Exact test\", \"p\": 0.003,\n                    \"n\": \"18 cells from 10 anesthetized mice and 14 cells from 11 awake mice\"}],\n    \"expected\": [ten(\"depolarizing responses, anesthetized (of 18)\", 0),\n                 ten(\"depolarizing responses, awake (of 14)\", 6)],\n    \"criterion\": NOT_HERE + \" Were the data available, polarity is the sign of the mean \"\n                 \"normalized Vm in the 100 ms after the light pulse, from the average of 15 sweeps \"\n                 \"normalized to the 100 ms before it (Methods, Polarity of GABAergic responses).\",\n})\nadd({\n    \"id\": \"fig2h-egaba-depolarized\",\n    \"statement\": \"Synaptic E_GABAAR is more depolarized in awake than in anesthetized cortex \"\n                 \"(-63.3 against -81.1 mV).\",\n    \"source\": \"Figure 2G and 2H\",\n    \"quote\": \"Synaptic E GABAAR is more depolarized in awake cortex (An.: −81.1 ± 1.7 mV vs. \"\n             \"Aw.: −63.3 ± 1.4 mV; p < 0.001, one-way ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\",\n                    \"n\": \"10 cells from 6 anesthetized mice and 10 cells from 9 awake mice\"}],\n    \"expected\": [mean(\"E_GABAAR anesthetized\", -81.1, 1.7, \"mV\"),\n                 mean(\"E_GABAAR awake\", -63.3, 1.4, \"mV\")],\n    \"criterion\": NOT_HERE + \" Were the data available, E_GABAAR is the intersection of the \"\n                 \"lines fitted to the baseline and light ramps after 90% offline series \"\n                 \"resistance correction (Methods, Electrophysiological recordings and GABAA \"\n                 \"receptor equilibrium potential), tested by \" + ANOVA + \".\",\n})\nadd({\n    \"id\": \"fig2i-rmp-depolarized\",\n    \"statement\": \"In voltage clamp the RMP is more depolarized in awake than in anesthetized \"\n                 \"cortex (-64.2 against -70.7 mV).\",\n    \"source\": \"Figure 2I\",\n    \"quote\": \"Voltage-clamp recordings confirmed a more depolarized RMP in awake cortex (An.: \"\n             \"−70.7 ± 1.9 mV vs. Aw.: −64.2 ± 1.1 mV; p = 0.02, one-way ANOVA with Bonferroni \"\n             \"correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.02,\n                    \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"RMP anesthetized\", -70.7, 1.9, \"mV\"),\n                 mean(\"RMP awake\", -64.2, 1.1, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig2j-df-depolarized\",\n    \"statement\": \"The GABAAR driving force is shifted in the depolarizing direction in awake \"\n                 \"cortex (-0.9 against 10.4 mV in anesthetized cortex).\",\n    \"source\": \"Figure 2J\",\n    \"quote\": \"GABA A R driving force (DF GABAAR = RMP − E GABAAR ) was more depolarized in awake \"\n             \"cortex (An.: 10.4 ± 2.0 mV vs. Aw.: −0.9 ± 1.7 mV; p < 0.001, one-way ANOVA with \"\n             \"Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"DF_GABAAR anesthetized\", 10.4, 2.0, \"mV\"),\n                 mean(\"DF_GABAAR awake\", -0.9, 1.7, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig2j-awake-df-zero\",\n    \"statement\": \"The awake GABAAR driving force does not differ from zero, consistent with \"\n                 \"predominantly shunting inhibition, while the anesthetized driving force does.\",\n    \"source\": \"Figure 2J legend; Results, Awake cortex exhibits more depolarized synaptic EGABAAR \"\n              \"and shunting fast synaptic inhibition, paragraph 3\",\n    \"quote\": \"Awake DF GABAAR was not different to zero, consistent with synaptic GABA A Rs \"\n             \"exerting a predominantly shunting effect (An.: p = 0.0006, one-sample t test; \"\n             \"Aw.; p = 0.61, one-sample t test)\",\n    \"statistics\": [{\"about\": \"anesthetized DF_GABAAR against zero\", \"test\": \"one-sample t test\",\n                    \"p\": 0.0006},\n                   {\"about\": \"awake DF_GABAAR against zero\", \"test\": \"one-sample t test\",\n                    \"p\": 0.61}],\n    \"criterion\": NOT_HERE + \" A claim of absence for the awake group: were the data available, \"\n                 \"reproduced when the one-sample t test of awake DF_GABAAR against zero gives p >= \"\n                 \"0.05 and that of the anesthetized group gives p < 0.05.\",\n})\nadd({\n    \"id\": \"fig2k-conductance-same\",\n    \"statement\": \"Light-evoked synaptic GABA conductances do not differ between anesthetized and \"\n                 \"awake cortex (11.04 against 11.4 nS).\",\n    \"source\": \"Figure 2K\",\n    \"quote\": \"Light-evoked synaptic GABA conductances did not differ between the anesthetized \"\n             \"and awake cortex (An. 11.04 ± 1.8 nS: vs. Aw.: 11.4 ± 1.5 nS, p = 0.92, one-way \"\n             \"ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.92,\n                    \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"GABA conductance anesthetized\", 11.04, 1.8, \"nS\"),\n                 mean(\"GABA conductance awake\", 11.4, 1.5, \"nS\")],\n    \"criterion\": NOT_HERE + \" A claim of absence: reproduced when \" + ANOVA + \" finds no \"\n                 \"difference at p < 0.05.\",\n})\nadd({\n    \"id\": \"figs4-intrinsic-properties\",\n    \"statement\": \"In a multi-compartment model, the differences in membrane properties between \"\n                 \"states do not explain the differences in measured synaptic E_GABAAR.\",\n    \"source\": \"Results, Awake cortex exhibits more depolarized synaptic EGABAAR and shunting fast \"\n              \"synaptic inhibition, paragraph 3; Results, Network activity in awake cortex raises \"\n              \"synaptic EGABAAR, paragraph 2; Figure S4 (not read); Methods, Simulating \"\n              \"measurements of synaptic EGABAAR\",\n    \"quote\": \"modeling of synaptic GABA A R responses in biologically realistic neurons confirmed \"\n             \"that differences in synaptic E GABAAR could not be explained by the intrinsic \"\n             \"membrane properties in anesthetized and awake cortices\",\n    \"data\": \"elsewhere\",\n    \"where\": \"Not deposited; generated by the paper's NEURON model and Matlab analysis, \"\n             \"github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit a404c3e\",\n    \"criterion\": \"Not testable on DANDI:000458. The model's parameters are in Table 2 and the \"\n                 \"Methods; the measure shown in Figure S4 is not in the text read.\",\n})\nadd({\n    \"id\": \"figs5-within-anesthetized\",\n    \"statement\": \"Within anesthetized recordings, more synaptic activity and more depolarized Vm \"\n                 \"go with modestly more depolarized synaptic E_GABAAR.\",\n    \"source\": \"Results, Awake cortex exhibits more depolarized synaptic EGABAAR and shunting fast \"\n              \"synaptic inhibition, paragraph 3; Figure S5 (not read)\",\n    \"quote\": \"more detailed analysis revealed modest synaptic E GABAAR changes within \"\n             \"anesthetized recordings, which were consistent with the general principle ... that \"\n             \"increased synaptic activity and depolarized V m result in more depolarized \"\n             \"synaptic E GABAAR because of an increased Cl − load\",\n    \"criterion\": NOT_HERE + \" The analysis and its test are in the Figure S5 legend, which is not \"\n                 \"in the text read.\",\n})\n\n# ---------------------------------------------------------------- Figure 3\nadd({\n    \"id\": \"rm-nbqx-higher\",\n    \"statement\": \"Local NBQX in awake cortex raises the membrane resistance (136.2 against 50.6 \"\n                 \"MOhm).\",\n    \"source\": \"Results, Network activity in awake cortex raises synaptic EGABAAR and promotes \"\n              \"shunting fast synaptic inhibition, paragraph 1\",\n    \"quote\": \"The reduction in local network activity was also reflected in the neuron’s R m , \"\n             \"which was higher in NBQX, again consistent with decreased synaptic activity (Aw.: \"\n             \"50.6 ± 6.4 MΩ, n = 13 neurons, 10 mice vs. +NBQX: 136.2 ± 11.9 MΩ, n = 10 \"\n             \"neurons, 7 mice, p < 0.0001, unpaired t test)\",\n    \"statistics\": [{\"test\": \"unpaired t test\", \"p\": 0.0001, \"p_relation\": \"<\",\n                    \"n\": \"13 awake neurons from 10 mice and 10 NBQX neurons from 7 mice\"}],\n    \"expected\": [mean(\"Rm awake\", 50.6, 6.4, \"MOhm\"),\n                 mean(\"Rm awake with NBQX\", 136.2, 11.9, \"MOhm\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3c-nbqx-vm\",\n    \"statement\": \"Reducing local network activity with NBQX hyperpolarizes the mean Vm in awake \"\n                 \"cortex (-72.6 against -60.3 mV).\",\n    \"source\": \"Figure 3B and 3C\",\n    \"quote\": \"Reducing local network activity caused a hyperpolarizing shift in mean V m (Aw.: \"\n             \"−60.3 ± 1.1 mV vs. +NBQX: −72.6 ± 1.0 mV; p < 0.001, one-way ANOVA with \"\n             \"Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\",\n                    \"n\": \"12 awake neurons from 10 mice and 10 NBQX neurons from 7 mice\"}],\n    \"expected\": [mean(\"mean Vm awake\", -60.3, 1.1, \"mV\"),\n                 mean(\"mean Vm awake with NBQX\", -72.6, 1.0, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3d-nbqx-fluctuation\",\n    \"statement\": \"NBQX greatly reduces subthreshold Vm fluctuations in awake cortex (0.7 against \"\n                 \"6.6 mV/ms).\",\n    \"source\": \"Figure 3D\",\n    \"quote\": \"Reducing local network activity caused a decrease in the mean change in \"\n             \"subthreshold V m (Aw: 6.6 ± 0.3 mV/ms vs. +NBQX: 0.7 ± 0.1 mV/ms; p < 0.001, \"\n             \"one-way ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"mean |dVm/dt| awake\", 6.6, 0.3, \"mV/ms\"),\n                 mean(\"mean |dVm/dt| awake with NBQX\", 0.7, 0.1, \"mV/ms\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3e-nbqx-polarity\",\n    \"statement\": \"With NBQX, light-evoked GABAAR responses in awake cortex are all \"\n                 \"hyperpolarizing (0 of 10 depolarizing, against 6 of 14 without).\",\n    \"source\": \"Figure 3E; Results, Network activity in awake cortex raises synaptic EGABAAR and \"\n              \"promotes shunting fast synaptic inhibition, paragraph 2\",\n    \"quote\": \"Reducing local network activity caused a hyperpolarizing shift in the polarity of \"\n             \"light-evoked GABA currents (bottom; Aw.: Depol. 6/14 vs. +NBQX: Depol. 0/10; p = \"\n             \"0.03, Fisher-Exact test)\",\n    \"statistics\": [{\"test\": \"Fisher-Exact test\", \"p\": 0.03,\n                    \"n\": \"14 awake neurons from 11 mice and 10 NBQX neurons from 7 mice\"}],\n    \"expected\": [ten(\"depolarizing responses, awake (of 14)\", 6),\n                 ten(\"depolarizing responses, awake with NBQX (of 10)\", 0)],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3g-nbqx-egaba\",\n    \"statement\": \"NBQX shifts synaptic E_GABAAR in awake cortex in the hyperpolarizing \"\n                 \"direction (-78.1 against -63.3 mV).\",\n    \"source\": \"Figure 3F and 3G\",\n    \"quote\": \"Reducing local network activity led to more hyperpolarized synaptic E GABAAR (Aw: \"\n             \"−63.3 ± 1.4 mV vs. +NBQX: −78.1 ± 1.3 mV; p < 0.001, one-way ANOVA with \"\n             \"Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.001,\n                    \"p_relation\": \"<\", \"corrected\": \"Bonferroni\",\n                    \"n\": \"10 awake neurons from 9 mice and 11 NBQX neurons from 7 mice\"}],\n    \"expected\": [mean(\"E_GABAAR awake\", -63.3, 1.4, \"mV\"),\n                 mean(\"E_GABAAR awake with NBQX\", -78.1, 1.3, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3h-nbqx-rmp\",\n    \"statement\": \"NBQX hyperpolarizes the voltage-clamp RMP in awake cortex (-71.4 against -64.2 \"\n                 \"mV).\",\n    \"source\": \"Figure 3H\",\n    \"quote\": \"Reducing local network activity caused a hyperpolarizing shift in RMP (Aw.: −64.2 \"\n             \"± 1.1 mV vs. +NBQX: −71.4 ± 1.4 mV; p = 0.009, one-way ANOVA with Bonferroni \"\n             \"correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.009,\n                    \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"RMP awake\", -64.2, 1.1, \"mV\"),\n                 mean(\"RMP awake with NBQX\", -71.4, 1.4, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3i-nbqx-df\",\n    \"statement\": \"NBQX shifts the GABAAR driving force in the hyperpolarizing direction (6.7 \"\n                 \"against -0.9 mV), so that it now differs from zero.\",\n    \"source\": \"Figure 3I\",\n    \"quote\": \"Reducing local network activity caused a hyperpolarizing shift in DF GABAAR (Aw.: \"\n             \"−0.9 ± 1.7 mV vs. +NBQX: 6.7 ± 1.5 mV; p = 0.03, one-way ANOVA with Bonferroni \"\n             \"correction). DF GABAAR became different from zero (Aw.: p = 0.61, one-sample t \"\n             \"test; +NBQX: p = 0.001, one-sample t test)\",\n    \"statistics\": [{\"about\": \"awake against awake with NBQX\",\n                    \"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.03,\n                    \"corrected\": \"Bonferroni\"},\n                   {\"about\": \"awake with NBQX DF_GABAAR against zero\",\n                    \"test\": \"one-sample t test\", \"p\": 0.001},\n                   {\"about\": \"awake DF_GABAAR against zero\", \"test\": \"one-sample t test\",\n                    \"p\": 0.61}],\n    \"expected\": [mean(\"DF_GABAAR awake\", -0.9, 1.7, \"mV\"),\n                 mean(\"DF_GABAAR awake with NBQX\", 6.7, 1.5, \"mV\")],\n    \"criterion\": NOT_HERE,\n})\nadd({\n    \"id\": \"fig3j-nbqx-conductance-same\",\n    \"statement\": \"NBQX does not change the light-evoked synaptic GABA conductance (10.4 against \"\n                 \"11.4 nS).\",\n    \"source\": \"Figure 3J\",\n    \"quote\": \"Reducing local network activity did not affect light-evoked synaptic GABA \"\n             \"conductances (Aw.: 11.4 ± 1.5 nS vs. +NBQX: 10.4 ± 0.7 nS; p = 0.78, one-way \"\n             \"ANOVA with Bonferroni correction)\",\n    \"statistics\": [{\"test\": \"one-way ANOVA with Bonferroni correction\", \"p\": 0.78,\n                    \"corrected\": \"Bonferroni\"}],\n    \"expected\": [mean(\"GABA conductance awake\", 11.4, 1.5, \"nS\"),\n                 mean(\"GABA conductance awake with NBQX\", 10.4, 0.7, \"nS\")],\n    \"criterion\": NOT_HERE + \" A claim of absence: reproduced when \" + ANOVA + \" finds no \"\n                 \"difference at p < 0.05.\",\n})\n\n# ---------------------------------------------------------------- Figure 4, Neuropixels\nSESSIONS = [\"sub-546655_ses-20201023\", \"sub-551397_ses-20210211\", \"sub-551399_ses-20210128\",\n            \"sub-569062_ses-20210218\", \"sub-569064_ses-20210408\", \"sub-569068_ses-20210304\",\n            \"sub-569069_ses-20210312\", \"sub-569072_ses-20210422\", \"sub-569073_ses-20210415\",\n            \"sub-569073_ses-20210416\", \"sub-571619_ses-20210319\", \"sub-571620_ses-20210513\",\n            \"sub-575102_ses-20210603\", \"sub-586466_ses-20210729\", \"sub-586468_ses-20210819\",\n            \"sub-590479_ses-20210921\", \"sub-590480_ses-20211111\"]\nadd({\n    \"id\": \"dataset-sessions-link\",\n    \"kind\": \"link\",\n    \"statement\": \"The 17 sessions the paper's analysis code reads are in DANDI:000458 and carry \"\n                 \"the fields the code uses.\",\n    \"source\": \"Key resources table, Deposited data; the analysis gist a77bcf5e at revision \"\n              \"43a13d89\",\n    \"criterion\": \"Reproduced when each of the 17 sessions the gist lists (\" + \", \".join(SESSIONS)\n                 + \"; each with suffix _behavior+ecephys) is an NWB file of DANDI:000458, \"\n                 \"version 0.230317.0039 as the gist names, with a units table holding \"\n                 \"spike_times, location and waveform_duration and a trials table holding \"\n                 \"stimulus_type, behavioral_epoch, is_valid, estim_target_region and stop_time, \"\n                 \"and with \\\"awake\\\" and \\\"isoflurane\\\" among its electrical trials' epochs. \"\n                 \"Partially reproduced when all 17 files exist but a field is missing or named \"\n                 \"otherwise.\",\n})\nNPX = (\" Method N1 to N8 of the opening comment (Methods and the analysis gist), under each of \"\n       \"the readings A1F1, A1F2, A2F1 and A2F2.\")\nadd({\n    \"id\": \"fig4c-sample\",\n    \"statement\": \"After excluding 203 neurons with evoked rates below 0.1 Hz or above 200 Hz, \"\n                 \"662 regular spiking neurons remain, from 17 recordings in 16 mice, a median of \"\n                 \"34 per recording (1 to 93).\",\n    \"source\": \"Methods, Pre-processing of Neuropixels dataset; Figure 4C legend\",\n    \"quote\": \"Neurons with an average evoked firing rate below 0.1 Hz or above 200 Hz in either \"\n             \"condition (awake/anesthesia) were excluded from further analysis (203 neurons). \"\n             \"The 662 remaining neurons derived from 17 recordings in 16 mice, each contributing \"\n             \"a median of 34 neurons (minimum: 1, maximum: 93)\",\n    \"depends_on\": [\"dataset-sessions-link\"],\n    \"expected\": [ten(\"neurons kept\", 662), ten(\"neurons excluded\", 203),\n                 ten(\"recordings\", 17), ten(\"mice\", 16),\n                 ten(\"median neurons per recording\", 34),\n                 ten(\"minimum neurons per recording\", 1),\n                 ten(\"maximum neurons per recording\", 93)],\n    \"criterion\": \"Counts of regular spiking units in the stimulated area (N2) before and after \"\n                 \"the exclusion (N7), per recording.\" + NPX + \" Reproduced when, under one \"\n                 \"reading, the numbers kept and excluded are within tolerance and the recording \"\n                 \"and mouse counts are 17 and 16; partially reproduced when only the total (865) \"\n                 \"is within 10%. The per-recording median and range are reported under each \"\n                 \"reading.\",\n})\nadd({\n    \"id\": \"fig4d-synchrony-lower-awake\",\n    \"statement\": \"Neurons show lower stimulus-evoked synchrony with the population awake than \"\n                 \"under isoflurane (0.325 against 0.393).\",\n    \"source\": \"Figure 4C and 4D (top); Results, Shunting inhibition promotes local network \"\n              \"desynchronization and response flexibility, paragraph 1\",\n    \"quote\": \"Neurons in the awake condition exhibited lower synchrony (top; Aw.: 0.325 ± 0.005 \"\n             \"vs. An.: 0.393 ± 0.007, p < 0.001, paired t test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.001, \"p_relation\": \"<\",\n                    \"n\": \"662 neurons from 17 probe recordings in 16 mice\"}],\n    \"depends_on\": [\"fig4c-sample\"],\n    \"expected\": [mean(\"mean synchrony awake\", 0.325, 0.005),\n                 mean(\"mean synchrony anesthetized\", 0.393, 0.007)],\n    \"criterion\": \"Synchrony (N6) per neuron and condition over the kept neurons, mean and SEM, \"\n                 \"paired t test (N8).\" + NPX + \" Reproduced when, under one reading, both means \"\n                 \"are within tolerance and the paired t test gives awake lower at p < 0.001; \"\n                 \"partially reproduced when the direction and test hold under every reading but \"\n                 \"no reading puts both means within tolerance. The gist's waveform cut (> 0.4 \"\n                 \"ms) is shown as a variant.\",\n})\nadd({\n    \"id\": \"fig4d-entropy-higher-awake\",\n    \"statement\": \"Peri-stimulus histogram entropy is higher awake than under isoflurane (1.347 \"\n                 \"against 1.111 nats), so responses are more variable in time.\",\n    \"source\": \"Figure 4C and 4D (bottom); Results, Shunting inhibition promotes local network \"\n              \"desynchronization and response flexibility, paragraph 1\",\n    \"quote\": \"Neurons in the awake condition exhibited lower synchrony ... and higher entropy \"\n             \"(bottom; Aw.: 1.347 ± 0.018 nats vs. An.: 1.111 ± 0.020 nats, p < 0.001, paired t \"\n             \"test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.001, \"p_relation\": \"<\",\n                    \"n\": \"662 neurons from 17 probe recordings in 16 mice\"}],\n    \"depends_on\": [\"fig4c-sample\"],\n    \"expected\": [mean(\"mean entropy awake\", 1.347, 0.018, \"nats\"),\n                 mean(\"mean entropy anesthetized\", 1.111, 0.020, \"nats\")],\n    \"criterion\": \"Entropy (N5) per neuron and condition over the kept neurons, mean and SEM, \"\n                 \"paired t test (N8).\" + NPX + \" Reproduced when, under one reading, both means \"\n                 \"are within tolerance and the paired t test gives awake higher at p < 0.001; \"\n                 \"partially reproduced when the direction and test hold under every reading but \"\n                 \"no reading puts both means within tolerance.\",\n})\nadd({\n    \"id\": \"fig4-rate-higher-awake\",\n    \"statement\": \"The same electrical stimuli evoke more spiking awake than under isoflurane; the \"\n                 \"mean evoked firing rate is higher in the awake state.\",\n    \"source\": \"Results, Shunting inhibition promotes local network desynchronization and response \"\n              \"flexibility, paragraph 1; Figure 4B\",\n    \"quote\": \"In contrast, in the anesthetized state, the same stimuli evoked less overall \"\n             \"activity ... As the mean firing rate was greater in the awake state\",\n    \"depends_on\": [\"fig4c-sample\"],\n    \"criterion\": \"Evoked firing rate (N7) per neuron and condition over the kept neurons. The \"\n                 \"paper reports no value or test in the text read (Figure S6 may hold them); the \"\n                 \"paired t test of N8, used for every per-neuron comparison of Figure 4D, is used \"\n                 \"here.\" + NPX + \" Reproduced when the awake mean is higher with p < 0.05 under \"\n                 \"every reading; the means under each reading are reported.\",\n})\nadd({\n    \"id\": \"figs6-rate-regressed\",\n    \"statement\": \"The awake decrease in synchrony and increase in entropy remain after the \"\n                 \"effect of firing rate is regressed out.\",\n    \"source\": \"Results, Shunting inhibition promotes local network desynchronization and response \"\n              \"flexibility, paragraph 1; Figure S6 (not read)\",\n    \"quote\": \"we also established that the differences in synchrony and entropy were still \"\n             \"evident after regressing out the effect of firing rate\",\n    \"depends_on\": [\"fig4d-synchrony-lower-awake\", \"fig4d-entropy-higher-awake\"],\n    \"criterion\": \"The regression is described only in the Figure S6 legend, which is not in the \"\n                 \"text read, so it is open. Readings: (R1) across all neuron and condition values, \"\n                 \"a linear regression of the measure on evoked firing rate, and the residuals \"\n                 \"compared awake against anesthetized by the paired t test of N8; (R2) an ordinary \"\n                 \"least squares model of the measure on condition and firing rate, the condition \"\n                 \"coefficient tested; (R3) per neuron, the awake minus anesthetized difference of \"\n                 \"the measure regressed on the difference of firing rate, the intercept tested \"\n                 \"against zero.\" + NPX + \" Reproduced when, for both synchrony and entropy, the \"\n                 \"awake difference keeps the sign of Figure 4D with p < 0.05 under every \"\n                 \"reading; partially reproduced when it holds for one measure, or under some \"\n                 \"readings only (the outcome then rests on the reading adopted).\",\n})\n\n# ---------------------------------------------------------------- Figure 4, model\nadd({\n    \"id\": \"fig4f-model-hyperpolarizing-less-activity\",\n    \"statement\": \"In the network model, shunting E_GABAAR gives more variable input-evoked spike \"\n                 \"times, while hyperpolarizing E_GABAAR gives less activity and spiking more \"\n                 \"closely aligned across neurons.\",\n    \"source\": \"Figure 4E and 4F; Results, Shunting inhibition promotes local network \"\n              \"desynchronization and response flexibility, paragraph 2\",\n    \"quote\": \"We observed that networks utilizing shunting E GABAAR exhibited more variable \"\n             \"input-evoked spike times, whereas networks with hyperpolarizing E GABAAR exhibited \"\n             \"less activity and the input-evoked spiking was more closely aligned to the spiking \"\n             \"of other neurons in the network\",\n    \"data\": \"elsewhere\",\n    \"where\": SIM_WHERE,\n    \"criterion\": SIM_METHOD + \" The paper gives no number or test for the activity; the mean \"\n                 \"peri-stimulus firing rate of the excitatory neurons (the gist's firing_rates) \"\n                 \"is compared between conditions. Reproduced when it is lower under the \"\n                 \"hyperpolarizing condition in at least 18 of the 20 runs (a standard choice); \"\n                 \"the alignment part is judged in fig4h-model-synchrony.\",\n})\nadd({\n    \"id\": \"fig4h-model-synchrony\",\n    \"statement\": \"Model pyramidal neurons are less synchronous with shunting than with \"\n                 \"hyperpolarizing E_GABAAR (0.784 against 0.881).\",\n    \"source\": \"Figure 4G and 4H (top)\",\n    \"quote\": \"Neurons in the shunting E GABAAR condition exhibited lower synchrony (Shunt: 0.784 \"\n             \"± 0.001 vs. Hyperpol: 0.881 ± 0.001, p < 0.001, paired t test)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.001, \"p_relation\": \"<\",\n                    \"n\": \"16,000 pyramidal neurons from the model\"}],\n    \"data\": \"elsewhere\",\n    \"where\": SIM_WHERE,\n    \"expected\": [mean(\"mean synchrony shunting\", 0.784, 0.001),\n                 mean(\"mean synchrony hyperpolarizing\", 0.881, 0.001)],\n    \"criterion\": SIM_METHOD + \" Paired t test over neurons, those undefined in either condition \"\n                 \"left out. Reproduced when both means are within tolerance and the test gives \"\n                 \"shunting lower at p < 0.001; partially reproduced when only the direction and \"\n                 \"test hold.\",\n})\nadd({\n    \"id\": \"fig4h-model-entropy\",\n    \"statement\": \"Model pyramidal neurons have higher peri-stimulus entropy with shunting than \"\n                 \"with hyperpolarizing E_GABAAR (0.451 against 0.197 nats).\",\n    \"source\": \"Figure 4G and 4H (bottom)\",\n    \"quote\": \"Neurons in the shunting E GABAAR condition exhibited lower synchrony ... and higher \"\n             \"entropy (Shunt: 0.451 ± 0.002 nats vs. Hyperpol: 0.197 ± 0.002 nats, p < 0.001, \"\n             \"paired t test) (n = 16,000 pyramidal neurons from the model)\",\n    \"statistics\": [{\"test\": \"paired t test\", \"p\": 0.001, \"p_relation\": \"<\",\n                    \"n\": \"16,000 pyramidal neurons from the model\"}],\n    \"data\": \"elsewhere\",\n    \"where\": SIM_WHERE,\n    \"expected\": [mean(\"mean entropy shunting\", 0.451, 0.002, \"nats\"),\n                 mean(\"mean entropy hyperpolarizing\", 0.197, 0.002, \"nats\")],\n    \"criterion\": SIM_METHOD + \" Paired t test over neurons, those undefined in either condition \"\n                 \"left out. Reproduced when both means are within tolerance and the test gives \"\n                 \"shunting higher at p < 0.001; partially reproduced when only the direction and \"\n                 \"test hold.\",\n})\nadd({\n    \"id\": \"figs7-model-decoding\",\n    \"statement\": \"Responses of networks with shunting E_GABAAR to 100 different input patterns \"\n                 \"are decoded more accurately by a downstream classifier.\",\n    \"source\": \"Results, Shunting inhibition promotes local network desynchronization and response \"\n              \"flexibility, paragraph 2; Figure S7 (not read); Methods, Characterization of \"\n              \"stimulus-evoked spiking responses, paragraph 2\",\n    \"quote\": \"when we assessed a network’s ability to encode different patterned inputs, we \"\n             \"observed that networks with shunting E GABAAR could be more accurately decoded by \"\n             \"a downstream classifier\",\n    \"data\": \"elsewhere\",\n    \"where\": SIM_WHERE,\n    \"criterion\": \"The paper's simulation gist, run 20 times as in SIM: per run and condition, \"\n                 \"spike counts of the first 50 excitatory neurons in each 25 ms epoch, a \"\n                 \"k-nearest neighbor classifier (scikit-learn defaults) with 5-fold shuffled \"\n                 \"stratified cross-validation over the 10,000 trials, mean accuracy (Methods and \"\n                 \"gist). The test, if any, is in the Figure S7 legend, not read. Readings: (D1) \"\n                 \"a paired t test of the 20 per-run accuracies, shunting against hyperpolarizing, \"\n                 \"p < 0.05; (D2) shunting higher in every run. Reproduced when the mean accuracy \"\n                 \"is higher under shunting and both readings hold; partially reproduced when \"\n                 \"only one does.\".replace(\"as in SIM\", \"as in fig4h-model-synchrony\"),\n})\n\ndoc = {\"paper\": \"doi:10.1016/j.neuron.2023.08.005\", \"claims\": claims}\nbody = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)\nwith open(\"claims/burman-2023.yaml\", \"w\") as f:\n    f.write(HEADER + body)\nprint(len(claims))\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 $TMPDIR/gen/make.py && python tools/claims_check.py claims/burman-2023.yaml paper/10.1016-j.neuron.2023.08.005.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python3 - <<'EOF'
s=open('make.py').read()
s=s.replace('''def mean(q, v, sem, unit):
    return {"quantity": q, "value": v, "tolerance": sem, "unit": unit}''','''def mean(q, v, sem, unit=None):
    d = {"quantity": q, "value": v, "tolerance": sem}
    if unit:
        d["unit"] = unit
    return d''')
open('make.py','w').write(s)
EOF
cd  && python3 $TMPDIR/gen/make.py && python tools/claims_check.py claims/burman-2023.yaml paper/10.1016-j.neuron.2023.08.005.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes: 35 claims, 34 quotes, 0 problems. Now I'm checking the house style rules: no plain scalar with ": ", no em dashes, no "rather".

**Agent calls Bash**

```bash
cd  f=claims/burman-2023.yaml; grep -n "—" $f; grep -n -i "rather" $f; python3 - <<'EOF'
import yaml
f='claims/burman-2023.yaml'
# find plain scalars containing ': '
ev=yaml.parse(open(f))
for e in ev:
    if isinstance(e,yaml.ScalarEvent) and e.style is None and ': ' in e.value:
        print('PLAIN', e.value[:80])
d=yaml.safe_load(open(f))
print(sum('criterion' in c for c in d['claims']), 'criteria;', sum('statistics' in c for c in d['claims']),'claims with stats;', sum(len(c.get('statistics',[])) for c in d['claims']),'stat entries;', sum('expected' in c for c in d['claims']),'with expected')
EOF
grep -n -A4 "figs7-model" $f | head; sed -n 95,110p $f
```

```
35 criteria; 24 claims with stats; 27 stat entries; 25 with expected
833:- id: figs7-model-decoding
834-  statement: Responses of networks with shunting E_GABAAR to 100 different input patterns are decoded
835-    more accurately by a downstream classifier.
836-  source: Results, Shunting inhibition promotes local network desynchronization and response flexibility,
837-    paragraph 2; Figure S7 (not read); Methods, Characterization of stimulus-evoked spiking responses,
    paragraph 1; Figure 1B
  quote: 'During the 10 min following gigaseal formation we observed a 20-fold decrease in R s (mean R
    s-0 min : 1,126.9 ± 35.8 MΩ vs. R s-10 min : 50.2 ± 3.8 MΩ)'
  expected:
  - quantity: series resistance at 0 min
    value: 1126.9
    tolerance: 35.8
    unit: MOhm
  - quantity: series resistance at 10 min
    value: 50.2
    tolerance: 3.8
    unit: MOhm
  criterion: Not testable on DANDI:000458, which holds only the Allen Institute Neuropixels recordings;
    the paper's patch-clamp recordings are not deposited (available on request). Were the data available,
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 838,860p claims/burman-2023.yaml; git status --short
```

```
paragraph 2
  quote: when we assessed a network’s ability to encode different patterned inputs, we observed that networks
    with shunting E GABAAR could be more accurately decoded by a downstream classifier
  data: elsewhere
  where: Not deposited; generated by the paper's simulation code, gist.github.com/paulbrodersen/2ce61e4e790e2a351d52d921f848e122
    at revision f6a05661
  criterion: 'The paper''s simulation gist, run 20 times as in fig4h-model-synchrony: per run and condition,
    spike counts of the first 50 excitatory neurons in each 25 ms epoch, a k-nearest neighbor classifier
    (scikit-learn defaults) with 5-fold shuffled stratified cross-validation over the 10,000 trials, mean
    accuracy (Methods and gist). The test, if any, is in the Figure S7 legend, not read. Readings: (D1)
    a paired t test of the 20 per-run accuracies, shunting against hyperpolarizing, p < 0.05; (D2) shunting
    higher in every run. Reproduced when the mean accuracy is higher under shunting and both readings
    hold; partially reproduced when only one does.'
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
[... 5 more lines not kept]
```

**Agent**

I've written `claims/burman-2023.yaml`. The quote checker reports 35 claims, 34 quotes, 27 statistical values and 0 problems. Nothing was committed.

**Text read.** The version of record (open access, Europe PMC PMC11913778): main text, the legends of Figures 1 to 4, and the STAR Methods with Tables 1 and 2. **The supplement (Figures S1 to S7 and their legends) is not in the text, and there is no PDF.** I went ahead because the main results, including every number for Figure 4A to 4D, are in the main text. Only `figs6-rate-regressed` needs a method found only in the supplement. Claims on S2 to S5 and S7 rest on the main-text sentences that cite those figures, and their tests are unknown.

**Code read:**
- Neuropixels analysis gist `a77bcf5e`, revision 43a13d89. It names DANDI:000458 version 0.230317.0039 and the 17 sessions.
- Network simulation gist `2ce61e4e`, revision f6a05661.
- The `richardjburman/burman-et-al-2022---Awake-EGABAAR` repository at a404c3e: the NEURON model for Figure S4.

**Claims:**
- **Counts:** 35 claims. 34 have quotes; the one without is the link claim (`dataset-sessions-link`), which checks that the 17 sessions are in the dataset with the fields the code uses. 24 claims carry statistics (27 entries), 25 have expected values, and all 35 have criteria.
- **Testable on DANDI:000458:** 6 claims (the session link, the sample counts, synchrony, entropy, firing rate, and Figure S6).
- **Not testable:** 24 patch-clamp claims (Figures 1 to 3, S2, S3, S5). DANDI:000458 is only the Claar et al. Neuropixels data, and the paper deposits its own recordings nowhere ("available on request").
- **Model claims:** 5, marked `data: elsewhere` and pointing at the simulation code (Figure 4F/H, S4, S7).

**Details left open, and the readings named:**
- **Area selection:** (A1) the Methods' annotations SSp-ll, SSp-tr or MOs; (A2) the code's first three characters of `location` matched against `estim_target_region`.
- **Evoked firing rate, used for the 0.1 to 200 Hz exclusion:** (F1) the Methods' spike count over trials × 10 ms; (F2) what the code actually computes. The code's `get_firing_rate` sums spike *times* where a count is expected, and divides by the highest trial index with a spike plus one. Every dataset claim runs under all four combinations of A and F.
- **Waveform cut:** ≥0.4 ms in the Methods, >0.4 ms in the code. The code's cut is a variant.
- **Alignment and pooling:** the code aligns to the trial's `stop_time` and pools all intensities and stimulation sites. The Methods say neither, so I followed the code.
- **Figure S6 regression (supplement missing):** (R1) a pooled regression on rate, then a paired t test of the residuals; (R2) an OLS model with condition and rate; (R3) the per-neuron awake-minus-anesthetized difference regressed on the rate difference, with the intercept tested.
- **Firing-rate claim:** the paper gives no value or test in the text I read. I used the paired t test the paper applies to the other per-neuron comparisons, a standard choice.
- **Figure S7 decoding test (unknown):** (D1) a paired t test over the 20 runs; (D2) shunting more accurate in every run.
- **Model activity claim:** the paper gives no test, so I set "lower in at least 18 of the 20 runs" as a standard choice. Random seeds are left unset, as in the code.
- **Neurons with an undefined value:** left out of the paired test, a standard choice.

**Missing from the paper.** The supplement. It holds the methods and numbers for Figures S2 to S7, which the S6 regression and the S7 decoding test need, and the tests for the S2, S3 and S5 claims.

## End of run

33 turns, 7 minutes, $2.17 at API prices, result: success.
