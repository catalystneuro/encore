# 001545 · claims · run 39588286098

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/001545 paper 2>&1; ls
```

```
1:# Protocol for an attempt
36:## Reader
38:### 1. Get the paper
49:### 2. Read the paper's code
59:### 3. Write the claims file
142:### 4. Data from outside the paper's own recordings
150:### 5. Check
163:### 6. Answer questions
171:## Author
179:### 1. Establish what can be tested
277:### 2. Check the data against its description
292:### 3. Write the entry
341:### 4. Lock, check and run
352:### 5. Record the attempt
399:### 6. Hand over for verification
433:## Repeat attempts
446:## Verifier
450:### Round 1: without the author's conclusions
468:### Round 2: with the author's conclusions
479:### Round 3: proposed changes
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,170p docs/protocol.md
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

[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml; ls schemas;
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
[... 234 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 250,321p claims/001453/*.yaml; cat schemas/claims.schema.json | head -200
```

```
- id: fig2k-more-monocular
  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
    p < 0.05).
  source: Figure 2K
  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
  statistics:
  - test: Student's t-test
    p: 0.05
    p_relation: "<"
    n: 5 ZF and 5 DC fish
- id: fig2l-bi-ratio
  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
    0.010).
  source: Figure 2L
  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
    0.24
  statistics:
  - test: Student's t-test
    p: 0.01
    n: 5 ZF and 5 DC fish
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p schemas/claims.schema.json; wc -c paper/*.txt; head -30 paper/*.txt; ls targets | head; grep -rl 001545 targets papers 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 290,330p schemas/claims.schema.json; wc -c paper/*.txt; head -20 paper/*.txt; grep -rl 001545 targets papers 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; awk '{print length($0)}' paper/*.txt | sort -n | tail -3; grep -rl 001545 targets papers 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'length($0)<5000' paper/*.txt; awk 'length($0)>=5000{print NR}' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -s -w 200 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
s=json.dumps(d)
i=s.find('001545');print(s[i-200:i+3000])"; grep -n -A15 001545 targets/description_papers.yaml papers/manifest.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Now reading the paper body.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	3573 lifesciall Life Science Alliance Life Sci Alliance Life Science Alliance LLC PMC12032840 12032840 12032840 40280713 10.26508/lsa.202403169 Diversification of dentate gyrus granule cell subtypes 
2	is regulated by Nrg1 nuclear back-signaling Rajebhosale Prithviraj Conceptualization, Data curation, Software, Formal analysis, Investigation, Visualization, Methodology, Writing—original draft, 
3	Writing—review and editing 1 Jiang Li Investigation 1 Ressa Haylee J Investigation 2 Johnson Kory R Data curation, Software, Formal analysis, Visualization, Methodology 3 Desai Niraj S Software, 
4	Formal analysis 4 Jone Alice Investigation 5 Role Lorna W Conceptualization, Supervision, Funding acquisition, Project administration, Writing—review and editing 4 Talmage David A Conceptualization, 
5	Resources, Supervision, Funding acquisition, Project administration, Writing—review and editing 1 ✉ 1 Genetics of Neuronal Signaling Section, National Institute of Neurological Disorders and Stroke, 
6	, NIH, Bethesda, MD, USA 2 Undergraduate Program in Fundamental Neuroscience, University of Virginia, , Charlottesville, VA, USA 3 Bioinformatics Core, National Institute of Neurological Disorders 
7	and Stroke, , National Institutes of Health, Bethesda, MD, USA 4 Circuits, Synapses and Molecular Signaling Section, National Institute of Neurological Disorders and Stroke, , NIH, Bethesda, MD, USA 
8	5 Program in Neuroscience, State University of New York at Stony Brook, Stony Brook, NY, USA ✉ Correspondence: [removed: an e-mail address] Alice Jone’s present address is Regulatory Affairs Division, 
9	STERIS Corporation, Mentor, OH, USA 25 4 2025 8 7 e202403169 e202403169 26 4 2025 © 2025 Rajebhosale et al. This article is available under a Creative Commons License (Attribution 4.0 International, 
10	as described at https://creativecommons.org/licenses/by/4.0/ ). The study shows that Nrg1 nuclear signaling maintains granule cell identity and that its disruption drives acquisition of semiluna
[... 263 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 274,
 "limit": 280
}
```

```
274	SGCs in the V 321 L DG. To address differences in cell sampling between WT and V 321 L GCs, we performed downsampling of WT GCs and recalculated pseudotime and gene expression associated with 
275	pseudotime ( Fig S7A ). We found that the pseudotime ordering of GCs and associated gene expression states were robust to differences in sampling frequency, with Sorcs3 still representing cells with 
276	the maximal pseudotime ( Fig S7B ). We next used “Trajectory Geometry” to assess whether the identified trajectories in WT and V 321 L mice have well-defined directionality ( Laddach et al, 2024 ). 
277	First, we tested cells along the identified trajectories in the WT mice (original and downsampled) against 1,000 iterations of pseudotime randomized cell trajectories. WT original and downsampled 
278	trajectories resulted in significantly lower spherical distances compared with randomized ones indicating the presence of a definite directionality within the trajectories (Wilcoxon’s signed rank 
279	test, randomized versus WT original, P = 4.25 × 10 −11 , randomized versus WT downsampled, P = 8.00 × 10 −31 ). Similarly, the V 321 L trajectory also produced a significantly smaller spherical 
280	distance relative to randomized trajectories (Wilcoxon’s signed rank test, randomized versus V 321 L, P = 3.17 × 10 −54 ). Interestingly, the spherical distances obtained for the WT trajectories were 
281	greater than those for the V 321 L trajectory indicating the presence of more complex fate decisions as seen by the branching in the WT trajectory. Importantly, although both the original and 
282	downsampled WT data yielded valid and statistically significant trajectories, they reflect different levels of complexity based on sampling. Thus, trajectory inference is not exhaustive but rather an 
283	approximation of lineage dynamics based on available cellular content. Figure 5. Non-SGCs harbor the potential to express an SGC-like transcriptomic state. (A) Representative image of 
[... 268 more lines not kept]
```

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 30 -o krt.docx "https://www.life-science-alliance.org/content/lsa/8/7/e202403169/DC1/embed/media-1.docx" ; ls -la krt.docx; file krt.docx; curl -sL -m 30 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12032840/supplementaryFiles" -o supp.zip; ls -la supp.zip; file supp.zip
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p supp && cd supp && unzip -o -q ../supp.zip && ls -la; for f in *.docx; do python3 - "$f" <<'EOF'
import sys,zipfile,re
z=zipfile.ZipFile(sys.argv[1]);x=z.read('word/document.xml').decode()
t=re.sub(r'</w:p>','\n',x);t=re.sub(r'<w:tab/>','\t',t);t=re.sub(r'<[^>]+>','',t)
print(t)
EOF
done | grep -i -E "github|GSE|software|code|igor|python|matlab|http" | head -40
```

```
[../supp.zip]
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of ../supp.zip or
        ../supp.zip.zip, and cannot find ../supp.zip.ZIP, period.
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/zipfile/__init__.py", line 1414, in __init__
    self.fp = io.open(file, filemode)
              ~~~~~~~^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '*.docx'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 300 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12032840/supplementaryFiles" -o supp.zip; ls -la supp.zip; rm -rf supp; mkdir supp; cd supp; unzip -o -q ../supp.zip; ls -la
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/supp; python3 - <<'EOF'
import zipfile,re
z=zipfile.ZipFile('LSA-2024-03169_Supplemental_Data_1.docx');x=z.read('word/document.xml').decode()
t=re.sub(r'</w:tc>',' | ',x);t=re.sub(r'</w:p>','\n',t);t=re.sub(r'<[^>]+>','',t)
print(t)
try:
  r=z.read('word/_rels/document.xml.rels').decode();print(re.findall(r'Target="(http[^"]+)"',r))
except Exception as e: print(e)
EOF
```

```
Key Resources Table
REAGENT or RESOURCE
 | SOURCE
 | IDENTIFIER
 | Fluorescent Detection Reagents
 | Streptavidin, Alexa Fluor™ 647 conjugate (1:1000)
 | ThermoFisher
 | S21374
 | Opal dye 520
 | Akoya Biosciences
 | FP1487001KT
 | Opal dye 570
 | Akoya Biosciences
 | FP1488001KT
 | Opal dye 620
 | Akoya Biosciences
 | FP1495001KT
 | Chemicals, Peptides, and Recombinant Proteins
 | DAPI Fluoromount-G®
 | SouthernBiotech
[... 154 more lines not kept]
```

**Agent**

The Key Resources Table gives the ephys code at `nsdesai/patch_clamp_analysis`. I'm cloning it to read how the 20 features are extracted.

**Agent calls Bash**

```bash
cd $TMPDIR; git clone -q https://github.com/nsdesai/patch_clamp_analysis.git && cd patch_clamp_analysis && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100 && cat README* 2>/dev/null | head -80
```

```
5d756c2b3a4ee1b95a3cabb1e39ec548e22de549 Thu Apr 17 17:26:12 2025 -0400 Add files via upload
2fd72f84e3400276a3579d2637b8f369cae92015 Thu Apr 17 17:25:48 2025 -0400 Add files via upload
8a59869f010a9635faab04274f84bef2000aa3c8 Thu Apr 17 17:25:26 2025 -0400 Add files via upload
./basic_scripts_for_analysis/spikeproperties.m
./basic_scripts_for_analysis/spikefrequencyadaptation.m
./basic_scripts_for_analysis/slowramp.m
./basic_scripts_for_analysis/sagpotential.m
./basic_scripts_for_analysis/rheobasecurrent.m
./basic_scripts_for_analysis/postinhibitory.m
./basic_scripts_for_analysis/makephaseplot.m
./basic_scripts_for_analysis/makegraph.m
./basic_scripts_for_analysis/makecumulativehistogram.m
./basic_scripts_for_analysis/ivplot.m
./basic_scripts_for_analysis/inputresistance.m
./basic_scripts_for_analysis/getindices.m
./basic_scripts_for_analysis/gatherdata.m
./basic_scripts_for_analysis/ficurve.m
./basic_scripts_for_analysis/analysis_of_neurophysiology_data_BNST.m
./basic_scripts_for_analysis/analysis_of_neurophysiology_data.m
./basic_scripts_for_analysis/afterhyperpolarization.m
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patch_clamp_analysis/basic_scripts_for_analysis; wc -l *.m; cat analysis_of_neurophysiology_data.m
```

```
94 afterhyperpolarization.m
  127 analysis_of_neurophysiology_data.m
  114 analysis_of_neurophysiology_data_BNST.m
   58 ficurve.m
   22 gatherdata.m
   39 getindices.m
   88 inputresistance.m
   24 ivplot.m
   40 makecumulativehistogram.m
   35 makegraph.m
   35 makephaseplot.m
    8 postinhibitory.m
   66 rheobasecurrent.m
   92 sagpotential.m
   13 slowramp.m
   71 spikefrequencyadaptation.m
   65 spikeproperties.m
  991 total
function analyzedData = analysis_of_neurophysiology_data(folderName)
% run analysis on all recording files in the folder called folderName
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patch_clamp_analysis/basic_scripts_for_analysis; for f in sagpotential inputresistance rheobasecurrent spikeproperties afterhyperpolarization ficurve spikefrequencyadaptation makephaseplot; do echo "=== $f"; cat $f.m; done
```

```
=== sagpotential
function [sag,sagRatio,tauSag] = sagpotential(inputData,outputData,Pars,startLoc,stopLoc,sagCurrent)
% [sag,sagRatio] = sagpotential(inputData,outputData,Pars,sagCurrent,startLoc,stopLoc,sagCurrent)
%
% calculates the absolute sag potential from hyperpolarizing current steps
%
% INPUTS
% inputData         recorded data (mV) in an n x m matrix, where n is the 
%                   number of sample points per current step 
%                   (=duration * time step) and m is the number of steps
% outputData        current steps (pA) in an n x m matrix, where n is the
%                   number of sample points per step (=duration * time 
%                   step) and m is the number of steps
% Pars              a structure variable that contains information about
%                   the recording
% startLoc          the index of the start of the current step
% stopLoc           the index of the stop of the current step
% sagCurrent        current amplitude used to estimate sag (e.g., -80 pA)
%
% OUTPUTS
[... 558 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patch_clamp_analysis/basic_scripts_for_analysis; diff analysis_of_neurophysiology_data.m analysis_of_neurophysiology_data_BNST.m; cat gatherdata.m getindices.m makegraph.m; cd $TMPDIR; git clone -q https://github.com/RajNINDS/V321L-snMultiome.git && cd V321L-snMultiome && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -50
```

```
1,11c1
< function analyzedData = analysis_of_neurophysiology_data(folderName)
< % run analysis on all recording files in the folder called folderName
< % return table of analysis measurements
< %
< % INPUT
< % folderName        complete name of folder containing recordings to be
< %                   analyzed
< % OUTPUT
< % analyzedData      table containing analysis measurements
< % 
< % Last modified: 04/15/24 (NSD)
---
> function analyzedData = analysis_of_neurophysiology_data_BNST(folderName,sagCurrent)
13,14c3,7
< sagCurrent = -60; % use the -60 pA current step to measure sag potential
< analysisDuration = 500; % analyze only the first 500 msec of the current step
---
> oldDir = cd(folderName);
> 
[... 162 more lines not kept]
```

**Agent**

The ephys code (MATLAB) returns 21 features, while the paper says 20 "as reported in Kim et al (2024)". I'll check that cited paper to see which 20 it lists.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 120 "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11080946/fullTextXML" -o kim.xml; ls -la kim.xml; python3 - <<'EOF'
import re
x=open('kim.xml').read()
t=re.sub(r'<[^>]+>',' ',x); t=re.sub(r'\s+',' ',t)
for k in ['twenty','20 features','features','sag','rheobase','spike width','downstroke','Desai']:
    for m in re.finditer(k,t,flags=re.I):
        print(k,'::',t[max(0,m.start()-300):m.start()+400]);print('---');break
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; cat kim.xml; echo; curl -sL -m 120 "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1016/j.celrep.2024.114009&format=json&resultType=lite" | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for u in "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11080946/fullTextXML" "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=11080946&retmode=xml"; do curl -sL -m 120 "$u" -o kim.xml; ls -la kim.xml; if [ $(stat -c%s kim.xml) -gt 5000 ]; then break; fi; done; python3 - <<'EOF'
import re
x=open('kim.xml').read()
t=re.sub(r'<[^>]+>',' ',x); t=re.sub(r'\s+',' ',t)
for k in ['twenty','20 ','electrophysiological features','resting membrane','spike width','downstroke']:
    for m in list(re.finditer(k,t,flags=re.I))[:2]:
        print(k,'::',t[max(0,m.start()-300):m.start()+600]);print('---')
EOF
```

```
-rw-r--r-- 1 runner runner 151 Oct 21 11:01 kim.xml
-rw-r--r-- 1 runner runner 192315 Oct 21 11:01 kim.xml
twenty ::  mCherry (ADCD). 25 In activated cholinergic neurons, tetracycline transactivator (tTA) will drive hM4Di and mCherry expression when mice are off doxycycline (DOX)-containing food. Injected mice were switched from a DOX-on to DOX-off diet, exposed to SAL, APP, or AV odor, then put back on DOX chow. Twenty-four hours later, mice were exposed to the same or a different odor and then processed for ChAT and GFP (to amplify the cFos-GFP signal) IHC ( Figure 3A ). This design enables VP cholinergic neurons activated on day 1 (i.e., test 1) to be ChAT + and ADCD + , and neurons activated on day 2 (i.e., test 2) to be ChAT + and cFos + . Very few ADCD + or cFos + VP cholinergic neurons were detected in animals exposed and re-exposed to SAL ( Figure 3B ). Both the first exposure and the re-exposure to either the APP odor or the AV odor activated VP cholinergic neurons (ChAT + /ADCD + , ChAT + /cF
---
20  :: se neurons responded to both aversive and rewarding stimuli. 9 These type I VP neurons were hypothesized to be salience-encoding cholinergic neurons, since their activity patterns resemble those of cholinergic neurons in other parts of the basal forebrain that respond to both reward and punishment. 20 Despite the known presence of cholinergic projection neurons in the VP, the functional significance of these neurons remains unknown. Although VP GABA and glutamate neurons have a unique role in processing rewarding vs. aversive behaviors, the role of VP cholinergic neurons in approach vs. aversive behaviors is unknown. Accordingly, we utilized activity- and Cre-dependent viral vectors to permanently label activated VP cholinergic neurons in distinct behavioral contexts. Here, we demonstrate that the VP includes two non-overlapping subpopulations of cholinergic neurons: one activated in res
---
20  :: re 6K ) and dendrite volume ( F (1, 10) = 57.31, p &lt;0.05
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re
x=open('kim.xml').read()
t=re.sub(r'<[^>]+>',' ',x); t=re.sub(r'\s+',' ',t)
i=t.find('(7) Spike amplitude')
print(t[i-2500:i+2500])
EOF
```

```
odor or SAL gauze pad was outlined as a zone. Automated rodent tracking was used for each video and the time (in seconds) the mouse spent in each zone was obtained. We did not note any sex differences in approach or avoidance behaviors in response to odor exposure. A pipeline for image analysis and quantification using Imaris is depicted in Figure S2 . To assist in defining VP boundaries, immunostaining for Substance P, which demarcates VP borders 8 , 17 was conducted in brain slices from a Chat-tau-eGFP mouse ( Figure S2 ). These boundaries were then used in later slices to delineate the VP. The whole VP was selected as the ROI for analysis. Whole slice images were first cropped and borders delineating the VP were created to mask any signal outside of the VP. Representative, nonbinary fluorescent images containing the VP is shown in Figure S4 . The VP was identified as the brain region containing a sparse cluster of cholinergic neurons ventral to the anterior commissure and striatum, and dorsal to the densely packed cluster of cholinergic neurons in the hDB. Within Imaris, the spots and surfaces function were used to create size and/or intensity-based thresholds for each channel. The colocalization tab was used to create a new channel with the colocalized signal between two defined channels. All data containing the total number of spots or surfaces was then exported. For each mouse, the total number of spots, surfaces and the colocalization of spots and surfaces, were obtained from 4 - 6 slices containing the VP (ranging from bregma +0.62 to +0.14). A mean cell count within the VP for each mouse was obtained by averaging the total number of cell counts across these slices. For electrophysiology data, eighteen features were extracted from each cell recorded before and in the response to currents steps. (1) Membrane potential (mV), measured in the absence of a current injection. (2) Sag potential (mV), measured in response to a −60 pA step, equal to the difference be
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/LSA-2024-03169_Fig2.jpg"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/LSA-2024-03169_FigS2.jpg"
}
```

Result: no output.

Result: no output.

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/claims_check.py; grep -n "def \|normal" tools/claims_check.py | head -40
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 48 more lines not kept]
```

**Agent**

I have what I need: the full text with Methods and supplementary legends, the KRT, both code repos, and the Kim et al feature definitions. Writing the claims file now.

**Agent calls Bash**

```bash
mkdir -p claims/001545
```

```
(Bash completed with no output)
```

**Agent**

Before writing the sequencing criteria, I'll check how the snMultiome R code defines Penk+ and the per-mouse percentages.

**Agent calls Bash**

```bash
cd $TMPDIR/V321L-snMultiome; wc -l *; cat README.md | head; grep -n -i "penk\|wilcox\|graph_test\|root\|Sorcs3\|downsampl\|>\s*0" Rcode_20230522.txt | head -80
```

```
7 README.md
  39672 Rcode_20230522.txt
   6594 Rcode_For_ATAC_Analysis_20231020.txt
  46273 total
# V321L-snMultiome
Rcode_20230522.txt Contents
Lines 1-1960: snRNA-SeqPreprocessing and clustering.
Lines 1962-2946: Analysis of gene expression in WT and V321L mice.
Lines 2948-3228: Trajectory analysis.
Lines 3278-4775: snATAC-Seq preprocessing and clustering.
Lines 4777-6667: Analysis of differential accessibility in WT and V321L mice.
761:if(length(chosen.doublet)>0) {
1054:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1083:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1112:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1141:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1170:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1199:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1228:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
1257:temp11 <- dimnames(temp10)[[1]][apply(temp10,1,sum)>0]
[... 72 more lines not kept]
```

**Agent**

Penk+ in the code is raw count > 0. Writing the file.

**Agent calls Write**

```json
{
 "file_path": "claims/001545/10.26508-lsa.202403169.yaml",
 "content": "# Claims for Rajebhosale, Jiang, Ressa, Johnson, Desai, Jone, Role & Talmage (2025), Life Sci\n# Alliance 8(7) e202403169, on dandiset 001545.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, under\n# docs/protocol.md (version pilot-10), Reader section.\n#\n# Text read. The version of record as served by Europe PMC (PMC12032840), full text with Results,\n# Materials and Methods and every figure legend, including the supplementary figure legends (Figs S1\n# to S10), in paper/10.26508-lsa.202403169.txt. The Key Resources Table (Supplemental Data 1, a docx)\n# was not in paper/; it was read from the Europe PMC supplementary files bundle for PMC12032840. It\n# gives the GEO accession of the snMultiome data (GSE280167) and the two code repositories below.\n# Tables S1 to S6 (gene lists from the sequencing) were not needed for any criterion here. Figure 2,\n# Figure S2 and the confusion matrices were read from the figure images in the same bundle (Fig S2C\n# lists the electrophysiological features used in the LDA).\n#\n# Code read.\n# - https://github.com/nsdesai/patch_clamp_analysis at commit 5d756c2 (MATLAB, \"Code for\n#   electrophysiology data analysis\" in the KRT). It extracts the features from current-step\n#   recordings (analysis_of_neurophysiology_data.m and the functions it calls). It holds no\n#   statistics, no LDA, PCA, k-means or regression; the Methods say statistics were run in Prism and\n#   the regression and LDA in R.\n# - https://github.com/RajNINDS/V321L-snMultiome at commit c124726 (R, snRNA-Seq and snATAC-Seq).\n#   A nucleus is Penk+ when its raw Penk count is above 0 (Rcode_20230522.txt, line 2353).\n#\n# Data the paper used.\n# - Whole-cell current clamp recordings with biocytin fills of dentate granule cells in acute coronal\n#   slices from P24 to P34 mice, recorded at 30 C from the middle of the suprapyramidal (dorsal) blade\n#   and the top cell body layer. Cells are classed by their fill as GCs (one primary dendrite) or SGCs\n#   (several primary dendrites). WT, 24 positioned cells (14 GC, 10 SGC) from 5 mice and 20 slices, of\n#   which 14 GC and 9 SGC enter the electrophysiology; V321L (Nrg1 V321L knock-in), 10 GC and 15 SGC\n#   from 5 mice and 17 slices. Measured variables are the voltage responses to current steps and, per\n#   cell, the soma position (vertical distance from the cell body centre to the GCL-MOL boundary, in\n#   micrometres) and morphology from Imaris reconstructions (splay angle, branch points and dendritic\n#   length per primary dendrite, 15 parameters). These are the data dandiset 001545 is described as\n#   holding (48 NWB files of electrophysiology).\n# - Golgi-stained cell counts (5 mice per genotype), RNAScope FISH counts and positions in the\n#   suprapyramidal blade (3 mice per genotype or age group, ages 1, 2, 3 and 9 to 12 months), and\n#   10x Multiome snRNA-Seq and snATAC-Seq of microdissected DG (4 mice per genotype, 2 male and 2\n#   female), deposited in GEO as GSE280167.\n#\n# Electrophysiological features. The Methods say \"Twenty features were extracted from the responses\n# to current steps as reported in Kim et al (2024)\" (Cell Rep 43:114009). Kim et al define eighteen,\n# and Fig S2C of this paper lists the same eighteen (spike width, downstroke, spike threshold,\n# rheobase, AHP width, spike latency, CV, tau, upstroke, input resistance, max firing rate, spike\n# amplitude, sag, RMP, AHP latency, f-I slope, AHP amplitude, adaptation index). The Results also use an\n# upstroke-downstroke ratio, which neither Kim et al nor the code define. The code returns 21 outputs\n# (the 18, plus sag ratio, spike peak and the AHP after the maximal step). Which 20 the paper means is\n# open. Definitions used here, from Kim et al as the Methods' reference, with the code where Kim et al\n# are silent (the analysis is restricted to the first 500 ms of each step, as in the code).\n# - RMP, the membrane potential without current injection; in the code the mean voltage from 10 to 1 ms\n#   before step onset, averaged over all sweeps.\n# - Rheobase, the smallest positive step that elicits an action potential; in the code an overshooting\n#   peak (above 0 mV, prominence at least 30 mV, width under 5 ms) within the first 500 ms.\n# - Spike threshold, the voltage at which dV/dt first crosses 20 mV/ms on the first spike at rheobase\n#   (Kim et al). The code uses 10 mV/ms after 10-fold interpolation; this is a variant.\n# - Spike width, the width at half the height between threshold and peak of the first spike at rheobase.\n# - Upstroke and downstroke, the maximum and the minimum of dV/dt on the first spike at rheobase (Kim et\n#   al). The code takes the minimum from 5 ms before the first peak to the end of the 500 ms window\n#   (its downIdx line resolves to the window's end), which can include later spikes; this is a variant.\n#   A \"faster\" downstroke is a more negative minimum.\n# - Sag, from the -60 pA step, the steady-state potential minus the minimum potential (the code takes\n#   the maximum of the second half of the step minus the minimum of the first half, after a 20 ms\n#   median filter).\n# - Input resistance, from the -20 pA step (Kim et al); the code fits steady-state deflections of steps\n#   from -50 to 0 pA (a variant).\n# - Upstroke-downstroke ratio, not defined; taken here as upstroke divided by the magnitude of\n#   downstroke (the sign convention does not change any test the paper reports on it).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001545\"\npaper: doi:10.26508/lsa.202403169\nclaims:\n- id: fig1f-sgc-soma-superficial\n  statement: In WT mice SGC somata lie closer to the GCL-MOL boundary than GC somata (SGCs in the\n    top cell body layers, under 20 micrometres from the surface).\n  source: Figure 1F; Results, SGCs have unique morphological and electrical properties, paragraph 2\n  quote: \"SGC cell body locations were significantly different from those of GCs (**** P < 0.0001, Welch’s t test [two-tailed]; t = 8.471, df = 19.16)\"\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 8.471, df = 19.16\n    p: 0.0001\n    p_relation: \"<\"\n    n: 14 GCs and 10 SGCs from 5 WT mice\n  criterion: Soma position is the vertical distance from the cell body centre to the GCL-MOL boundary\n    (Methods, Imaging and image analysis). Two-tailed Welch's t test of WT SGC against WT GC\n    positions, as in the legend. Reproduced when p < 0.0001 with SGCs nearer the boundary; partially\n    reproduced when p < 0.05 with SGCs nearer the boundary.\n- id: fig1g-sgc-wider-splay\n  statement: WT SGCs have wider dendritic splay angles than WT GCs.\n  source: Figure 1G\n  quote: \"The splay angle (angle between the two farthest dendrites measured at the center of the cell body) was significantly larger in SGCs compared with GCs (* P = 0.0168, Welch’s t test [two-tailed]; t = 2.754, df = 12.59)\"\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 2.754, df = 12.59\n    p: 0.0168\n    n: 13 GCs and 6 SGCs from 4 WT mice\n  criterion: Splay angle as the Methods define it (FIJI angle tool, from the most laterally displaced\n    dendritic termination through the soma centre to the opposite one). Two-tailed Welch's t test.\n    Reproduced when p < 0.05 with SGCs wider.\n- id: fig1h-gc-more-branch-points\n  statement: WT GCs have more dendritic branch points per primary dendrite than WT SGCs.\n  source: Figure 1H\n  quote: \"The number of branch points was significantly higher in GCs compared with SGCs (** P = 0.0023, Mann–Whitney test, U = 2)\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 2\n    p: 0.0023\n    n: 11 GCs and 5 SGCs from 4 WT mice\n  criterion: Branch points from the Imaris reconstruction divided by the number of primary dendrites\n    (legend). Mann-Whitney test; tails are not stated, so two-tailed (the paper's t tests are marked\n    two-tailed) and one-tailed readings are both run. Reproduced when p < 0.05 with GCs higher under\n    both.\n- id: fig1i-gc-longer-dendrites\n  statement: WT GCs have greater dendritic length per primary dendrite than WT SGCs.\n  source: Figure 1I\n  quote: \"The normalized dendritic length was significantly higher in GCs compared with SGCs (*** P = 0.0004, Welch’s t test [two-tailed]; t = 5.348, df = 9.366)\"\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 5.348, df = 9.366\n    p: 0.0004\n    n: 11 GCs and 5 SGCs from 4 WT mice\n  criterion: Total dendritic length divided by the number of primary dendrites (legend). Two-tailed\n    Welch's t test. Reproduced when p < 0.05 with GCs longer.\n- id: fig1j-sgc-hyperpolarized-rmp\n  statement: In WT mice SGCs have a more hyperpolarized resting membrane potential than GCs.\n  source: Figure 1J; Results, SGCs have unique morphological and electrical properties, paragraph 2\n  quote: \"SGCs have a significantly more hyperpolarized resting membrane potential compared with GCs (* P = 0.02, Mann–Whitney test, U = 26; N = 14 cells [GCs] and 9 cells [SGCs] from 5 mice)\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 26\n    p: 0.02\n    n: 14 GCs and 9 SGCs from 5 WT mice\n  criterion: RMP per cell as defined in the opening comment (code, baseline before step onset). WT\n    SGCs against WT GCs by Mann-Whitney test; tails not stated, so two-tailed and one-tailed readings\n    are both run. Reproduced when p < 0.05 with SGCs more negative under both readings. The cell\n    counts are compared with 14 and 9, and U with 26.\n- id: fig1k-sgc-narrower-spike\n  statement: In WT mice SGCs have narrower action potentials than GCs.\n  source: Figure 1K; Results, SGCs have unique morphological and electrical properties, paragraph 2\n  quote: \"SGCs have a significantly narrower spike width compared with GCs (* P = 0.012, Mann–Whitney test, U = 24\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 24\n    p: 0.012\n    n: 14 GCs and 9 SGCs from 5 WT mice\n  criterion: Spike width at half height between threshold and peak of the first spike at rheobase,\n    threshold at dV/dt 20 mV/ms (Kim et al, the Methods' reference); the code's 10 mV/ms threshold is\n    shown as a variant. Mann-Whitney test, two-tailed and one-tailed readings. Reproduced when p <\n    0.05 with SGCs narrower under both readings.\n- id: fig1l-sgc-faster-downstroke\n  statement: In WT mice SGCs have a faster action potential downstroke than GCs.\n  source: Figure 1L; Results, SGCs have unique morphological and electrical properties, paragraph 2\n  quote: \"SGCs have a significantly faster downstroke compared with GCs (* P = 0.046, Mann–Whitney test, U = 31\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 31\n    p: 0.046\n    n: 14 GCs and 9 SGCs from 5 WT mice\n  criterion: Downstroke as the minimum dV/dt on the repolarizing phase of the first spike at rheobase\n    (Kim et al). The code's window, from 5 ms before the first peak to the end of the first 500 ms of\n    the step, is a second reading, as the code disagrees with the Methods' reference only where the\n    rheobase sweep holds more than one spike. Mann-Whitney test, two-tailed and one-tailed. Reproduced\n    when p < 0.05 with SGCs more negative under every reading; blocked as methods_underspecified when\n    the readings disagree, with each shown.\n- id: fig1m-phase-plots\n  statement: Phase plots of the action potential at rheobase show differences in waveform kinetics\n    between WT GCs and SGCs.\n  source: Figure 1M; Results, SGCs have unique morphological and electrical properties, paragraph 2\n  quote: \"The pronounced differences in the kinetics of the SGC action potentials can be seen in the phase plots for APs at rheobase\"\n  criterion: For each cell, dV/dt against Vm minus threshold for the first spike at rheobase, dV/dt\n    as the first difference over the time step (makephaseplot.m). Shown as a figure; the claim is\n    judged as reproduced when fig1k-sgc-narrower-spike and fig1l-sgc-faster-downstroke are, since\n    the paper reads the plot through those two measures.\n  depends_on:\n  - fig1k-sgc-narrower-spike\n  - fig1l-sgc-faster-downstroke\n- id: figs1a-f-properties-covary-with-position\n  statement: In WT cells (GCs and SGCs together), RMP, spike width, downstroke, rheobase, sag and\n    upstroke-downstroke ratio covary with soma position.\n  source: Figure S1A to F; Results, SGCs have unique morphological and electrical properties,\n    paragraph 3\n  quote: \"We found that RMP ( Fig S1A , P = 0.0129), spike width ( Fig S1B , P = 0.0543), and downstroke ( Fig S1C , P = 0.0139) significantly covaried with soma position ... We also found that rheobase ( Fig S1D , P = 0.0475), sag ( Fig S1E , P = 0.0359), and upstroke–downstroke ratio ( Fig S1F , P = 0.0131) significantly covaried with soma positions in the GCL\"\n  statistics:\n  - about: RMP against soma position\n    test: linear regression\n    statistic: R2 = 0.26\n    p: 0.0129\n  - about: spike width against soma position\n    test: linear regression\n    statistic: R2 = 0.17\n    p: 0.0543\n  - about: downstroke against soma position\n    test: linear regression\n    statistic: R2 = 0.26\n    p: 0.0139\n  - about: rheobase against soma position\n    test: linear regression\n    statistic: R2 = 0.17\n    p: 0.0475\n  - about: sag against soma position\n    test: linear regression\n    statistic: R2 = 0.19\n    p: 0.0359\n  - about: upstroke-downstroke ratio against soma position\n    test: linear regression\n    statistic: R2 = 0.26\n    p: 0.0131\n  expected:\n  - quantity: R2, RMP against soma position\n    value: 0.26\n    tolerance: 0.026\n  - quantity: R2, spike width against soma position\n    value: 0.17\n    tolerance: 0.017\n  - quantity: R2, downstroke against soma position\n    value: 0.26\n    tolerance: 0.026\n  - quantity: R2, rheobase against soma position\n    value: 0.17\n    tolerance: 0.017\n  - quantity: R2, sag against soma position\n    value: 0.19\n    tolerance: 0.019\n  - quantity: R2, upstroke-downstroke ratio against soma position\n    value: 0.26\n    tolerance: 0.026\n  criterion: The legend reports P and R2 per property, so each is a simple linear regression of the\n    property on soma position over the 23 WT cells (14 GC, 9 SGC), as fitted in Prism (Methods,\n    Statistical analysis). The paper counts spike width (P = 0.0543) as significant, so a property\n    matches when its slope p is at most 1.1 times the reported p or its R2 is within tolerance.\n    Reproduced when all six match; partially reproduced when four or five match. Feature definitions\n    as in the opening comment; the code's variants are shown.\n- id: figs1-remaining-properties-no-difference\n  statement: The remaining electrophysiological properties differ neither between WT GCs and SGCs\n    nor with soma position.\n  source: Results, SGCs have unique morphological and electrical properties, paragraph 3\n  quote: The remainder of the properties did not differ significantly between GCs and SGCs or by soma\n    position\n  criterion: A claim of absence, judged on the paper's tests at p < 0.05. For each property other\n    than the six of figs1a-f and the three of Fig 1J to L, WT GC against SGC by Welch's t test when\n    both groups pass Shapiro-Wilk and Kolmogorov-Smirnov normality tests and by Mann-Whitney test\n    otherwise (Methods, Statistical analysis), and a linear regression on soma position as in Fig S1.\n    Which properties make up the remainder depends on the 20 features, which the paper does not list\n    (opening comment); the readings are (a) the 18 features of Fig S2C less the five named (RMP,\n    spike width, downstroke, rheobase, sag), and (b) the 21 outputs of the code less those five.\n    Reproduced when no property in the reading finds an effect; not reproduced when any does. Every\n    test's p and effect size is shown.\n- id: figs1g-l-gc-only-position\n  statement: Among WT GCs alone, downstroke and sag still covary with soma position, while RMP,\n    spike width, rheobase and upstroke-downstroke ratio do not, so the GC-SGC differences in RMP and\n    spike width are cell-type features.\n  source: Figure S1G to L; Results, SGCs have unique morphological and electrical properties,\n    paragraph 3\n  quote: \"we found that downstroke and sag were still significantly correlated with soma positions ( Fig S1I , downstroke, P = 0.006, and Fig S1K , sag, P = 0.03), whereas the rest of the properties did not correlate with soma positions ( Fig S1G , RMP, P = 0.22, Fig S1H , spike width, P = 0.1, Fig S1J , rheobase, P = 0.06, and Fig S1L , upstroke–downstroke ratio, P = 0.4)\"\n  statistics:\n  - about: downstroke against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.5\n    p: 0.006\n    n: 14 WT GCs from 5 mice\n  - about: sag against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.32\n    p: 0.03\n    n: 14 WT GCs from 5 mice\n  - about: RMP against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.12\n    p: 0.22\n  - about: spike width against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.21\n    p: 0.1\n  - about: rheobase against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.26\n    p: 0.06\n  - about: upstroke-downstroke ratio against soma position, GCs\n    test: linear regression\n    statistic: R2 = 0.07\n    p: 0.4\n  criterion: Simple linear regressions on soma position over the 14 WT GCs, as in Fig S1A to F.\n    Reproduced when downstroke and sag have p < 0.05 and RMP, spike width, rheobase and the ratio\n    have p >= 0.05 (the absence half judged on this test as written); partially reproduced when the\n    two significant ones hold and one of the four absences fails. Every slope, p and R2 is shown.\n- id: fig2a-v321l-more-multiple-dendrite-gcs\n  statement: Golgi staining labels the same total number of GCs in WT and V321L DG, but V321L DG has\n    a higher percentage of GCs with multiple primary dendrites and a lower percentage with a single\n    one.\n  source: Figure 2A; Results, V321L mutation in Nrg1 results in altered composition of the DG granule\n    cell population, paragraph 1\n  quote: \"There was no difference in the total number of cells labeled by the Golgi stain between genotypes ( Fig 2A , left; P = 0.68). However, V 321 L mice had a significantly higher number of Golgi-stained GCs with multiple primary dendrites compared with WT mice and a significantly lower number of GCs with single primary dendrites compared with WT mice\"\n  statistics:\n  - about: total Golgi-labeled GCs, WT against V321L\n    test: Welch's t test, two-tailed\n    statistic: t = 0.4338, df = 6.972\n    p: 0.7\n    n: 5 mice per genotype\n  - about: genotype by number of primary dendrites interaction\n    test: two-way ANOVA\n    statistic: F(1,7) = 11.81\n    p: 0.011\n  - about: WT multiple against V321L multiple\n    test: post hoc comparison\n    p: 0.008\n  - about: WT single against V321L single\n    test: post hoc comparison\n    p: 0.008\n  - about: V321L single against V321L multiple\n    test: post hoc comparison\n    p: 0.013\n  criterion: Per mouse, the percentage of Golgi-stained GCs with one and with several primary\n    dendrites. Two-way ANOVA (genotype by dendrite class) with Bonferroni post hoc comparisons (the\n    Methods' parametric correction). Reproduced when the interaction has p < 0.05, both genotype\n    comparisons have p < 0.05 in the stated directions, and the total count does not differ by\n    two-tailed Welch's t test at p < 0.05. The Results print P = 0.68 and the legend P = 0.7 for the\n    total; both are recorded as one test.\n- id: fig2c-v321l-sgc-position-not-different\n  statement: In V321L mice SGC and GC soma positions do not differ; SGCs are found throughout the\n    GCL.\n  source: Figure 2B, 2C and 2H; Results, V321L mutation in Nrg1 results in altered composition of the\n    DG granule cell population, paragraph 2\n  quote: \"SGC cell body locations are not significantly different to those of GCs ( P = 0.9012, Welch’s t test [two-tailed]; t = 0.1256, df = 21.78\"\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 0.1256, df = 21.78\n    p: 0.9012\n    n: 10 GCs and 15 SGCs from 5 V321L mice\n  criterion: A claim of absence, judged on two-tailed Welch's t test of V321L SGC against V321L GC\n    soma positions at p < 0.05. Reproduced when p >= 0.05; the difference in means is shown.\n- id: fig2d-v321l-splay-not-different\n  statement: In V321L mice the splay angle does not differ between GCs and SGCs.\n  source: Figure 2D\n  quote: The splay angle was not significantly different between GCs and SGCs\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 1.879, df = 14.11\n    p: 0.0811\n    n: 8 GCs and 13 SGCs from 5 V321L mice\n  criterion: A claim of absence, judged on two-tailed Welch's t test at p < 0.05. Reproduced when p\n    >= 0.05; the difference is shown.\n- id: fig2ef-v321l-dendritic-complexity-preserved\n  statement: In V321L mice GCs still have more branch points and greater dendritic length per primary\n    dendrite than SGCs.\n  source: Figure 2E and 2F\n  quote: In contrast, the differences in dendritic complexity between GCs and SGCs were preserved in\n    the V 321 L mutant DG\n  statistics:\n  - about: normalized branch points\n    test: Mann-Whitney test\n    statistic: U = 13\n    p: 0.0013\n    n: 9 GCs and 13 SGCs from 5 V321L mice\n  - about: normalized dendritic length\n    test: Welch's t test, two-tailed\n    statistic: t = 5.023, df = 10.05\n    p: 0.0005\n    n: 9 GCs and 13 SGCs from 5 V321L mice\n  criterion: Measures as in Fig 1H and 1I. Reproduced when both tests give p < 0.05 with GCs higher\n    (Mann-Whitney two-tailed and one-tailed readings); partially reproduced when one does.\n- id: fig2g-morphology-lda-separates-cell-type\n  statement: Linear discriminant analysis of 15 morphological parameters separates GCs from SGCs\n    along LD1, but not WT from V321L cells.\n  source: Figure 2G and Figure S2A; Results, V321L mutation in Nrg1 results in altered composition of\n    the DG granule cell population, paragraph 2\n  quote: LDA resulted in successful capture of cell-type differences between GCs and SGCs (along the\n    primary classifier—LD1) but not between genotypes\n  criterion: Features z-scored with scale(), then LDA (MASS lda), as the Methods describe for the\n    electrophysiological LDA. The groups are not stated; Fig 2G shows LD1 and LD2, which needs at\n    least three classes, so the reading is four classes (genotype by cell type). The parameter set is\n    the morphological variables of Fig S2A. Reproduced when the LD1 scores of GCs and SGCs separate\n    (a two-tailed Mann-Whitney test of LD1 by cell type at p < 0.05 and at least 90% of cells on\n    their type's side of the midpoint between the type medians) while LD1 does not differ by\n    genotype within either cell type (Mann-Whitney p >= 0.05). The 90% bound is not from the paper;\n    the overlap is reported either way.\n- id: figs2b-morphology-kmeans-by-cell-type\n  statement: k-means clustering (k = 3) of morphological data groups cells by cell type, with all WT\n    GCs in one cluster and all WT SGCs in another; all but one V321L GC and all but two V321L SGCs fall\n    in the corresponding clusters.\n  source: Figure S2B\n  quote: All WT GCs and SGCs segregate into k1 and k2, respectively. All but one V 321 L GCs occupy\n    k1, whereas the one was in k3. All but 2 V 321 L SGCs occupy k2 with one in k1 and another in k3\n  criterion: k-means with k = 3 on the morphological data, on the PCA scores shown in the panel. The\n    paper gives neither the number of PCs, the scaling nor the seed; readings are k-means on (a) the\n    z-scored features and (b) the first two PCs of the z-scored features, each with 100 random starts\n    (a standard choice). Reproduced when, under every reading, the cluster that holds most WT GCs\n    holds all WT GCs and no WT SGC and the counts of V321L cells outside their type's cluster are\n    within one of the paper's (1 GC, 2 SGCs).\n- id: fig2i-v321l-rmp-not-different\n  statement: In V321L mice GCs and SGCs do not differ in RMP; both lie near the WT SGC median.\n  source: Figure 2I; Results, V321L mutation in Nrg1 results in altered composition of the DG granule\n    cell population, paragraph 3\n  quote: \"Unlike WT GCs and SGCs, we found no differences in electrical properties between V 321 L GCs and SGCs ( Fig 2I–K , RMP, P = 0.9\"\n  statistics:\n  - test: Welch's t test\n    statistic: t = 0.2081, df = 18.86\n    p: 0.8374\n    n: 10 GCs and 15 SGCs from 5 V321L mice\n  criterion: A claim of absence, judged on Welch's t test of V321L GC against SGC RMP at p < 0.05.\n    Reproduced when p >= 0.05; the difference and both group medians, beside the WT GC and SGC\n    medians, are shown.\n- id: fig2j-v321l-spike-width-not-different\n  statement: In V321L mice GCs and SGCs do not differ in spike width.\n  source: Figure 2J\n  quote: \"Spike width ( P = 0.2776, Mann–Whitney test, U = 55)\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 55\n    p: 0.2776\n    n: 10 GCs and 15 SGCs from 5 V321L mice\n  criterion: A claim of absence, judged on a two-tailed Mann-Whitney test at p < 0.05, with spike\n    width as in fig1k-sgc-narrower-spike. Reproduced when p >= 0.05; the code's threshold is shown as\n    a variant and the medians are shown.\n- id: fig2k-v321l-downstroke-not-different\n  statement: In V321L mice GCs and SGCs do not differ in downstroke.\n  source: Figure 2K\n  quote: \"Downstroke ( P = 0.5392, Mann–Whitney test, U = 63.5)\"\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 63.5\n    p: 0.5392\n    n: 10 GCs and 15 SGCs from 5 V321L mice\n  criterion: A claim of absence, judged on a two-tailed Mann-Whitney test at p < 0.05, with\n    downstroke as in fig1l-sgc-faster-downstroke (Kim et al definition). Reproduced when p >= 0.05;\n    the code's window is shown as a variant.\n- id: fig2m-ephys-lda-wt-gc-apart\n  statement: LDA of electrical properties separates WT GCs from all other groups (WT SGCs, V321L GCs,\n    V321L SGCs) along LD1, driven mainly by spike width and downstroke.\n  source: Figure 2M and Figure S2C; Results, V321L mutation in Nrg1 results in altered composition of\n    the DG granule cell population, paragraph 3\n  quote: LDA resulted in separation of WT GCs and all other groups (WT SGCs, V 321 L GCs, and V 321 L\n    SGCs) along LD1 driven strongly by spike width\n  criterion: The 18 features of Fig S2C, z-scored with scale() (Methods, LDA), LDA (MASS lda) with\n    four classes (genotype by cell type; Fig 2M shows LD1 and LD2). Whether PCA precedes this LDA as it\n    does for the classifier is not stated; readings are (a) LDA on the z-scored features and (b) LDA\n    on their top 9 PCs. Cells with a missing feature are dropped. Reproduced when, under every\n    reading, the WT GC mean LD1 lies on one side and the means of the other three groups on the\n    other, and spike width or downstroke has the largest absolute LD1 coefficient; blocked as\n    methods_underspecified when the readings disagree.\n- id: figs2d-ephys-kmeans-v321l-like-wt-sgc\n  statement: k-means clustering (k = 3) of electrophysiological data places V321L GCs and SGCs in\n    clusters in nearly the same proportions as WT SGCs, while WT GCs spread across all three clusters.\n  source: Figure S2D; Results, V321L mutation in Nrg1 results in altered composition of the DG\n    granule cell population, paragraph 3\n  quote: WT GCs are evenly distributed across all clusters, whereas SGCs largely occupy k3 with a\n    minority in k1. All V 321 L GC and SGC cluster occupancy was virtually identical to WT SGCs\n  criterion: k-means with k = 3 on the 18 features of Fig S2C. The scaling, number of PCs and seed are\n    not given; readings are (a) z-scored features and (b) the first two PCs of the z-scored features,\n    100 random starts each. Reproduced when, under every reading, WT GCs occupy all three clusters with\n    none holding more than half of them, and WT SGCs, V321L GCs and V321L SGCs each have most cells\n    in one same cluster.\n- id: v321l-multiple-regression-wt-only\n  statement: Controlling for soma position, spike amplitude and upstroke covary with cell type in WT\n    mice, while no electrophysiological property shows a cell-type effect in V321L mice.\n  source: Results, V321L mutation in Nrg1 results in altered composition of the DG granule cell\n    population, paragraph 4\n  quote: \"In WT mice, we found that two electrophysiological properties, spike amplitude ( P = 0.042, β1 = −46.2) and upstroke ( P = 0.038, β1 = −117.88), significantly covaried with cell type when controlling for soma position. However, this model did not detect significant cell-type effects for any electrophysiological properties in V 321 L mice\"\n  statistics:\n  - about: spike amplitude, cell type coefficient, WT\n    test: multiple linear regression\n    statistic: beta1 = -46.2\n    p: 0.042\n  - about: upstroke, cell type coefficient, WT\n    test: multiple linear regression\n    statistic: beta1 = -117.88\n    p: 0.038\n  expected:\n  - quantity: cell type coefficient beta1 for spike amplitude, WT\n    value: -46.2\n    tolerance: 4.62\n    unit: mV\n  - quantity: cell type coefficient beta1 for upstroke, WT\n    value: -117.88\n    tolerance: 11.79\n    unit: mV/ms\n  criterion: Per property and genotype, lm(property ~ CellType + SomaPosition + CellType x\n    SomaPosition) in R (Methods, Statistical analysis), soma position in micrometres from the GCL-MOL\n    boundary. The coding of cell type is not stated; readings are SGC = 1 and GC = 1 (the sign of beta1\n    flips between them, so a beta1 matches when its magnitude is within tolerance and its sign fits\n    one coding used for both properties). Reproduced when in WT the beta1 p-values for spike amplitude\n    and upstroke are below 0.05 with beta1 within tolerance, and in V321L no property's beta1 has p <\n    0.05 (the absence half judged on this test). The property set for the V321L half is open\n    (opening comment); readings are the 18 features of Fig S2C and the 21 outputs of the code. The\n    WT properties other than these two are shown.\n- id: figs2e-pca-separation-lost\n  statement: PCA of the electrophysiological features separates WT GCs from WT SGCs on the first two\n    components, while V321L GCs and SGCs overlap.\n  source: Figure S2E; Results, V321L mutation in Nrg1 results in altered composition of the DG\n    granule cell population, paragraph 5\n  quote: Principal component analysis (PCA) revealed a clear separation between GCs and SGCs in WT\n    mice along the first two principal components, whereas cells in V 321 L mice showed substantial\n    overlap\n  criterion: PCA (prcomp) of the 18 z-scored features of Fig S2C over all cells, with 95% ellipses per\n    group as in the legend. The ellipse type is not stated; readings are (a) the 95% normal data\n    ellipse (ggplot2 stat_ellipse default) and (b) the 95% confidence ellipse of the group mean.\n    Reproduced when, under every reading, the WT GC and WT SGC centroids each lie outside the other\n    group's ellipse and the V321L GC and SGC centroids each lie inside the other's; blocked as\n    methods_underspecified when the readings disagree. The centroid distances are shown.\n- id: figs2f-centroid-separation-reduced\n  statement: In the WT-trained LDA, the distance between GC and SGC centroids along LD1 is much\n    smaller in V321L than in WT, with both V321L centroids on the WT SGC side of the boundary.\n  source: Figure S2F; Results, V321L mutation in Nrg1 results in altered composition of the DG\n    granule cell population, paragraph 5\n  quote: Centroid analysis demonstrated a striking reduction in the separation between GC and SGC\n    centroids in V 321 L mice along the first linear discriminant (LD1) axis\n  depends_on:\n  - figs2g-lda-classifier-accuracy\n  criterion: The classifier of figs2g-lda-classifier-accuracy; LD1 scores of WT cells and of V321L\n    cells (projected through the WT PCA and LDA). Reproduced when the V321L GC-SGC centroid distance\n    on LD1 is less than half the WT distance and both V321L centroids lie on the WT SGC side of the\n    LD1 decision boundary. The bound of one half is read from Fig S2F (about 1.3 against 3.3 units)\n    and is not stated in the text.\n- id: figs2g-lda-classifier-accuracy\n  statement: An LDA classifier trained on WT electrophysiology classifies held-out WT cells with 78%\n    accuracy (Cohen's kappa 0.57) but V321L cells with only 52% accuracy (kappa 0.08).\n  source: Figure S2G; Results, V321L mutation in Nrg1 results in altered composition of the DG\n    granule cell population, paragraph 5\n  quote: The LDA classifier, trained on 80% of the WT data, achieved 78% accuracy in cell-type\n    classification of the remainder 20% WT cells (Cohen’s κ = 0.57) ( Fig S2G , top). Using this\n    classifier on the recordings obtained from V 321 L mice resulted in 52% classification accuracy\n    (Cohen’s κ = 0.08)\n  expected:\n  - quantity: accuracy on held-out WT cells\n    value: 78\n    tolerance: 7.8\n    unit: percent\n  - quantity: Cohen's kappa on held-out WT cells\n    value: 0.57\n    tolerance: 0.1\n  - quantity: accuracy on V321L cells\n    value: 52\n    tolerance: 5.2\n    unit: percent\n  - quantity: Cohen's kappa on V321L cells\n    value: 0.08\n    tolerance: 0.1\n  criterion: As the Methods (LDA) describe. The 18 features of Fig S2C, z-scored with scale(); PCA\n    with prcomp on WT; the top 9 PCs; caret train with method lda and trainControl(method cv, number\n    5); the WT PCA and LDA applied to the V321L data. Kappa tolerances are 0.1, not 10%, because with\n    about 21 to 23 cells one reclassified cell moves kappa by about 0.08. Open details, with readings\n    run. (1) Whether V321L data are scaled with their own mean and SD or the WT ones (\"applied to the\n    scaled V321L data\"). (2) Whether 78% is caret's mean accuracy over the five folds or the pooled\n    out-of-fold accuracy; the WT confusion matrix in Fig S2G counts 21 cells (16 correct, 76%), so it\n    pools all folds. (3) The fold seed, not given; each value is the median over 100 random fold\n    assignments (a standard choice), with the range shown. Reproduced when under one reading all four\n    values are within tolerance; partially reproduced when the two accuracies are, or when WT accuracy\n    exceeds V321L accuracy by at least 15 points. The V321L matrix in Fig S2G (8, 5, 7, 3; 11 of 23\n    correct, 48%, kappa near -0.09) does not match the text's 52% and 0.08; both are compared and the\n    mismatch is recorded.\n- id: fig3b-penk-position-altered\n  statement: In WT mice most Penk+ GCs lie in the top two cell body layers of the suprapyramidal GCL;\n    this bias toward the GCL-MOL boundary is lost in V321L mice.\n  source: Figure 3B; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 1\n  quote: In WT mice, most of the Penk + GCs were in the top 2 cell body layers of the suprapyramidal\n    GCL, whereas this bias toward the GCL-MOL boundary was lost in the V 321 L DG\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    statistic: D = 0.36\n    p: 0.013\n    n: 3 mice per genotype\n  criterion: Distances of Penk+ somata from the GCL-MOL boundary in FISH images (cells with at least\n    5 puncta or large clusters; Methods), pooled per genotype. Two-sample Kolmogorov-Smirnov test.\n    Reproduced when p < 0.05 with V321L cells farther from the boundary.\n- id: fig3d-more-penk-gcs\n  statement: V321L mice have a higher percentage of Penk-expressing GCs in snRNA-Seq.\n  source: Figure 3D; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 2\n  quote: the total percentage of Penk + GCs was significantly higher in V 321 L mice\n  statistics:\n  - test: Mann-Whitney test, two-tailed\n    statistic: U = 0\n    p: 0.03\n    n: 4 mice per genotype\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Per mouse, the percentage of GCs (clusters 0, 1, 5 and 18) with a raw Penk count above 0\n    (snMultiome code). Two-tailed Mann-Whitney test. Reproduced when p < 0.05 with V321L higher (U =\n    0 gives the smallest p available with 4 and 4, 0.029).\n- id: figs3b-prox1-count-not-different\n  statement: The total number of Prox1+ GCs does not differ between WT and V321L mice.\n  source: Figure S3B; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 2\n  quote: \"We found no differences in the total number of Prox1 + neurons (GCs) ( Fig S3B ; Mann–Whitney test, P = 0.69, U = 6)\"\n  statistics:\n  - about: as in the Results\n    test: Mann-Whitney test\n    statistic: U = 6\n    p: 0.69\n    n: 4 mice per genotype\n  - about: as in the Fig S3B legend\n    test: Welch's t test, two-tailed\n    statistic: t = 0.6994, df = 3.762\n    p: 0.5\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: A claim of absence. The Results and the legend name different tests; both are the\n    paper's, so both are run at p < 0.05 on per-mouse Prox1+ GC counts. Reproduced when neither finds\n    a difference.\n- id: figs3c-cluster18-penk-enriched\n  statement: Among the four GC clusters (0, 1, 5, 18), cluster 18 has the highest percentage of Penk+\n    cells in both genotypes.\n  source: Figure S3C; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 2\n  quote: cluster 18 contained the highest percentage of Penk + cells indicating enrichment for SGCs in\n    cluster 18 in both genotypes\n  statistics:\n  - about: cluster effect\n    test: two-way RM ANOVA\n    p: 0.0005\n  - about: cluster 0 against 18\n    test: Bonferroni corrected comparison\n    p: 0.0007\n    corrected: Bonferroni\n  - about: cluster 1 against 18\n    test: Bonferroni corrected comparison\n    p: 0.02\n    corrected: Bonferroni\n  - about: cluster 5 against 18\n    test: Bonferroni corrected comparison\n    p: 0.003\n    corrected: Bonferroni\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Per mouse and cluster, percentage of Penk+ GCs. Two-way repeated-measures ANOVA (cluster\n    by genotype, cluster within mouse) with Bonferroni comparisons of each cluster against 18.\n    Reproduced when the cluster effect and all three comparisons have p < 0.05 with cluster 18\n    highest.\n- id: figs3d-sorcs3-marks-cluster18\n  statement: Sorcs3 is the distinguishing marker of GC cluster 18, and Sorcs3+ cells are biased\n    toward the GCL-MOL boundary in FISH.\n  source: Figure S3D; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 2\n  quote: However, cluster 18 was uniquely marked by the expression of Sortilin Related VPS10 Domain\n    Containing Receptor 3 ( Sorcs3 )\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Seurat FindConservedMarkers across WT and V321L for each GC cluster (Methods). Reproduced\n    when Sorcs3 is among the conserved markers of cluster 18 and not of clusters 0, 1 or 5. The FISH\n    half is not tested here (no statistic is given).\n- id: figs5a-penk-sorcs3-subsets\n  statement: V321L mice have more Penk+Sorcs3+ and Penk+Sorcs3- GCs than WT, while Sorcs3+Penk- GCs are\n    unchanged.\n  source: Figure S5A; Results, V321L mice have a higher number and altered positioning of Penk+ GCs\n    compared with WT mice, paragraph 3\n  quote: V 321 L mice also showed an increase in the percentage of Penk + Sorcs3 + GCs ( Fig S5A ; P =\n    0.009). We found that there were no significant differences in the proportion of Penk-Sorcs3+\n    cells between WT and V 321 L mice\n  statistics:\n  - about: marker by genotype interaction\n    test: two-way ANOVA\n    statistic: F(2, 12) = 4.199\n    p: 0.041\n  - about: Penk+Sorcs3+, WT against V321L\n    test: Bonferroni corrected comparison\n    p: 0.009\n    corrected: Bonferroni\n  - about: Penk+Sorcs3-, WT against V321L\n    test: Bonferroni corrected comparison\n    p: 0.0002\n    corrected: Bonferroni\n  - about: Sorcs3+Penk-, WT against V321L\n    test: Bonferroni corrected comparison\n    p: 0.287\n    corrected: Bonferroni\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Per mouse, the percentage of GCs in each marker class (raw count above 0 for each gene).\n    Two-way ANOVA (marker class by genotype) with Bonferroni comparisons of genotype within class.\n    Reproduced when the two Penk+ classes differ at p < 0.05 with V321L higher and Sorcs3+Penk- does not\n    (p >= 0.05).\n- id: fig4a-more-penk-sorcs3-cells-fish\n  statement: In FISH, V321L mice have more Penk+Sorcs3+ cells in the suprapyramidal blade than WT mice.\n  source: Figure 4A; Results, Discovery of novel marker genes for SGCs, paragraph 1\n  quote: We found that V 321 L mice had significantly higher numbers of cells co-expressing Penk and\n    Sorcs3\n  statistics:\n  - test: Welch's t test, two-tailed\n    statistic: t = 5.278, df = 2.941\n    p: 0.014\n    n: 3 mice per genotype, 9 sections\n  criterion: Per mouse, the count of Penk+Sorcs3+ cells in the suprapyramidal blade (averaged over its\n    sections, each dot one mouse). Two-tailed Welch's t test. Reproduced when p < 0.05 with V321L\n    higher.\n- id: fig4a-prime-penk-sorcs3-position\n  statement: Penk+Sorcs3+ cells in V321L DG are not restricted to the layers at the GCL-MOL boundary.\n  source: Figure 4a'\n  quote: the V 321 L mice showing more Penk+Sorcs3+ cells present in the lower layers of the GCL, away\n    from the GCL-MOL boundary\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    statistic: D = 0.4\n    p: 0.029\n    n: 3 mice per genotype\n  criterion: Distances of Penk+Sorcs3+ cells from the GCL-MOL boundary pooled per genotype; two-sample\n    Kolmogorov-Smirnov test. Reproduced when p < 0.05 with V321L cells farther from the boundary.\n- id: fig4b-penk-enriched-genes\n  statement: Differential expression finds 102 genes significantly enriched in Penk+ GCs over Penk- GCs\n    (fold change of at least 2, adjusted P at most 0.05).\n  source: Figure 4B; Results, Discovery of novel marker genes for SGCs, paragraph 2\n  quote: We assessed differential gene expression in Penk + GCs compared with Penk -negative GCs\n    yielding 102 genes whose expression was significantly enriched in Penk + GCs (fold change of ≥2 and\n    adj. P ≤ 0.05)\n  expected:\n  - quantity: genes enriched in Penk+ GCs\n    value: 102\n    tolerance: 10\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Seurat FindMarkers of Prox1+Penk+ against Prox1+Penk- GCs (snMultiome code, workbook 58),\n    log2 fold change at least 1 and adjusted p at most 0.05. Reproduced when the count is within\n    tolerance.\n- id: fig4b2-marker-penk-cells-increased\n  statement: For each selected SGC marker gene except Grp, V321L mice have a higher proportion of GCs\n    co-expressing Penk and that marker.\n  source: Figure 4b''; Results, Discovery of novel marker genes for SGCs, paragraph 2\n  quote: Except for gastrin-releasing peptide ( Grp ) ... all other marker gene Penk-co-expressing\n    cells formed a significantly higher proportion of all GCs in the V 321 L mice\n  statistics:\n  - test: multiple Mann-Whitney tests, FDR corrected\n    statistic: U = 0\n    p: 0.03\n    corrected: FDR (two-stage step-up Benjamini, Krieger and Yekutieli)\n    n: 4 mice per genotype\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Per mouse, cells co-expressing Penk and each marker divided by all cells in clusters 0, 1,\n    5 and 18 (legend). Mann-Whitney test per gene, FDR by the two-stage Benjamini-Krieger-Yekutieli\n    method. The nine genes are those of Fig 4b' and 4b''. With 4 and 4 mice the smallest two-tailed p is\n    0.029, so the threshold is the paper's FDR adjusted p of 0.03 as printed. Reproduced when every\n    gene except Grp has U = 0 with V321L higher and Grp does not.\n- id: fig4d-penk-marker-overlap\n  statement: In WT FISH, 84% of Penk+ GCs express Nptx2, 67% express Sorcs3, and 64% express both.\n  source: Figure 4D and 4d'; Results, Discovery of novel marker genes for SGCs, paragraph 2\n  quote: We found that on average 84% of the Penk + GCs also expressed Nptx2 , and 67% of the Penk +\n    GCs also expressed Sorcs3 . The co-expression of Nptx2 and Sorcs3 was detected in 64% of the Penk +\n    GCs\n  expected:\n  - quantity: Penk+ cells expressing Nptx2\n    value: 84\n    tolerance: 5\n    unit: percent\n  - quantity: Penk+ cells expressing Sorcs3\n    value: 67.3\n    tolerance: 5.5\n    unit: percent\n  - quantity: Penk+ cells expressing Nptx2 and Sorcs3\n    value: 64\n    tolerance: 7.9\n    unit: percent\n  criterion: Per mouse, percentages over Penk+ cells in the suprapyramidal blade, then the mean over the\n    three mice; tolerances are the SDs the legend gives. Reproduced when all three are within\n    tolerance.\n- id: figs6-increase-in-nrg1-expressing\n  statement: The increase in marker+Penk+ GCs in V321L mice is seen in Nrg1-expressing Penk+ GCs and\n    not in Nrg1-non-expressing ones; about 94% of Penk+ GCs co-express Nrg1 in FISH.\n  source: Figure S6A and S6B; Results, Discovery of novel marker genes for SGCs, paragraph 2\n  quote: Intriguingly, this increase in numbers of marker + Penk + cells was only observed in Penk and\n    Nrg1 co-expressing GCs ( Fig S6A ) and not in Nrg1 -non-expressing Penk + GCs ( Fig S6B ). In FISH\n    experiments for Penk and Nrg1 , we found that most of the Penk + GCs co-expressed Nrg1 (∼94%)\n  statistics:\n  - about: Penk+Nrg1+ GCs, Grp\n    test: multiple Mann-Whitney tests, FDR corrected\n    statistic: U = 2.5\n    p: 0.14\n  - about: Penk+Nrg1+ GCs, other markers\n    test: multiple Mann-Whitney tests, FDR corrected\n    statistic: U = 0 or 1\n    p: 0.1\n    p_relation: \"<\"\n  - about: Penk+Nrg1- GCs, Sorcs3, Itgav, Chgb, Scg2 and Grm8\n    test: multiple Mann-Whitney tests, FDR corrected\n    statistic: U = 0\n    p: 0.08\n  - about: Penk+Nrg1- GCs, other markers\n    test: multiple Mann-Whitney tests, FDR corrected\n    p: 0.1\n    p_relation: \">\"\n  expected:\n  - quantity: Penk+ GCs co-expressing Nrg1 in FISH\n    value: 94\n    tolerance: 9.4\n    unit: percent\n  data: elsewhere\n  where: GEO GSE280167 (the FISH percentage is not deposited there)\n  criterion: As fig4b2-marker-penk-cells-increased, split by Nrg1 raw count above 0. The paper's\n    threshold here is FDR adjusted p < 0.1 (legend). Reproduced when in Penk+Nrg1+ GCs every marker\n    except Grp reaches adjusted p < 0.1 with V321L higher, and in Penk+Nrg1- GCs fewer markers reach\n    it. The FISH percentage is checked only if the FISH counts are available.\n- id: fig5b-pseudotime-sorcs3-top\n  statement: In WT GCs the top gene explaining pseudotime is Sorcs3, and late pseudotime falls at the\n    end of cluster 1 and in cluster 18; in V321L GCs trajectories are altered and the latest pseudotime\n    is in cluster 5.\n  source: Figure 5B; Results, Non-SGCs harbor the potential to express an SGC-like transcriptomic\n    state, paragraph 1\n  quote: The top gene explaining pseudotime in WT DG was found to be Sorcs3 ... Trajectories in the V\n    321 L DG were highly altered, and cells with late pseudotime were present in cluster 5\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Monocle3 on the GC clusters per genotype, root in cluster 0 (highest Camk4), graph_test\n    with neighbor_graph principal_graph (Methods; snMultiome code lines 2948 to 3228). Reproduced when\n    Sorcs3 has the highest Moran's I among genes with q < 0.05 in WT, the WT cells in the top decile of\n    pseudotime are mostly in clusters 1 and 18, and the V321L top decile is mostly in cluster 5. The\n    decile is not from the paper.\n- id: trajectory-geometry-directionality\n  statement: WT (original and downsampled) and V321L GC trajectories have significantly lower spherical\n    distances than randomized ones, so they have definite directionality; WT spherical distances\n    exceed V321L ones.\n  source: Results, Non-SGCs harbor the potential to express an SGC-like transcriptomic state,\n    paragraph 1\n  quote: WT original and downsampled trajectories resulted in significantly lower spherical distances\n    compared with randomized ones indicating the presence of a definite directionality within the\n    trajectories ... the spherical distances obtained for the WT trajectories were greater than those\n    for the V 321 L trajectory\n  statistics:\n  - about: randomized against WT original\n    test: Wilcoxon signed rank test\n    p: 4.25e-11\n  - about: randomized against WT downsampled\n    test: Wilcoxon signed rank test\n    p: 8.0e-31\n  - about: randomized against V321L\n    test: Wilcoxon signed rank test\n    p: 3.17e-54\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: TrajectoryGeometry analyseSingleCellTrajectory on the top 50 PCs rescaled to 0 to 100 with\n    Monocle3 pseudotime, nSamples 1000, N 1000, randomization byPermutation and permuteWithinColumns,\n    statistic mean (Methods). The downsampling seed is not given; the downsampled WT result is the\n    median over 20 draws. Reproduced when all three tests give p < 0.05 with lower distances than\n    random and the mean WT distance exceeds the V321L one.\n- id: fig5d-atac-cluster-composition\n  statement: In ATAC space, the Penk+ GC cluster 9 is populated evenly by WT and V321L nuclei, while\n    cluster 4 (Camk4+ GCs) is about 75% WT.\n  source: Figure 5d'; Results, Non-SGCs harbor the potential to express an SGC-like transcriptomic\n    state, paragraph 3\n  quote: Cluster 9 was comprised of the Penk + GCs, and it was uniformly populated by WT and V 321 L\n    GCs; however, cluster 4 that was comprised of the Camk4 + GCs (cluster 0 in the “RNA space”) was\n    disproportionately populated by WT GCs, which made up ∼75% of all cells in that cluster\n  expected:\n  - quantity: WT share of ATAC cluster 4\n    value: 75\n    tolerance: 7.5\n    unit: percent\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Clustering of GC nuclei in ATAC space at resolution 0.5 (Methods; ATAC code). Reproduced\n    when the WT share of cluster 4 is within tolerance and that of cluster 9 is between 40 and 60%\n    (a reading of \"uniformly\", not stated by the paper).\n- id: fig5f-sgc-genes-broadly-accessible\n  statement: SGC-enriched genes are accessible in cluster 9 and in nearly all other ATAC clusters of\n    GCs in both genotypes, though their expression is largely restricted to cluster 18 in WT.\n  source: Figure 5E and 5F; Results, Non-SGCs harbor the potential to express an SGC-like\n    transcriptomic state, paragraph 3\n  quote: However, we also found SGC-enriched genes to be accessible in cells in nearly all other\n    clusters for both genotypes\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Signac GeneActivity per gene (TSS and 1 kb), nine genes of Fig 5E and 5F. Reproduced when\n    for each gene the fraction of nuclei with nonzero activity is above zero in at least 8 of the 10\n    ATAC clusters in each genotype (a reading of \"nearly all\"), while in WT RNA the expressing\n    fraction is highest in cluster 18.\n- id: figs8b-penk-accessibility-not-different\n  statement: The percentage of GCs with an accessible Penk locus does not differ between WT and V321L\n    mice.\n  source: Figure S8b''; Results, Non-SGCs harbor the potential to express an SGC-like transcriptomic\n    state, paragraph 3\n  quote: the total number of GCs having the Penk locus accessible was not significantly different\n    between the genotypes\n  statistics:\n  - test: Mann-Whitney test\n    statistic: U = 7\n    p: 0.9\n    n: 4 mice per genotype\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: A claim of absence, judged on a Mann-Whitney test at p < 0.05 of per-mouse percentages of\n    GCs with nonzero Penk gene activity. Reproduced when p >= 0.05.\n- id: tables4-suz12-enrichment\n  statement: Genes enriched in Penk+ GCs and correlated with maximal pseudotime are strongly enriched\n    for regulation by Suz12, a core PRC2 component.\n  source: Results, Non-SGCs harbor the potential to express an SGC-like transcriptomic state,\n    paragraph 4; Table S4\n  quote: We found strong enrichment for regulation of these genes by Suz12, a core component of the\n    polycomb repressive complex 2 (PRC2)\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: The 60 genes (fig s10 intersection) submitted to the ChEA and ENCODE libraries of\n    Enrichr. Reproduced when SUZ12 is the top term by adjusted p in at least one of the two\n    libraries.\n- id: fig6a-penk-increases-with-age\n  statement: The number of Penk+ cells in the suprapyramidal GCL of WT mice increases with age, from\n    between 2 and 3 months.\n  source: Figure 6a'; Results, SGC numbers in the DG increase during the adolescence-adulthood\n    transition in WT mice, paragraph 1\n  quote: We confirmed that WT mice indeed show an increase in Penk expression starting between 2 and 3\n    mo of age\n  statistics:\n  - about: age effect\n    test: Brown-Forsythe ANOVA\n    statistic: F = 33.4 [3, 4.2]\n    p: 0.0032\n  - about: 1 against 3 months\n    test: Dunnett's T3 multiple comparisons\n    p: 0.008\n  - about: 1 against 12 months\n    test: Dunnett's T3 multiple comparisons\n    p: 0.03\n  - about: 2 against 3 months\n    test: Dunnett's T3 multiple comparisons\n    p: 0.008\n  criterion: Per mouse, the total count of Penk+ cells in the suprapyramidal GCL at 1, 2, 3 and 9 to\n    12 months. Brown-Forsythe ANOVA with Dunnett's T3 comparisons. The Results print P = 0.0032 and\n    the legend P = 0.002. Reproduced when the age effect and the 2 against 3 month comparison have p <\n    0.05 with the count higher at 3 months.\n- id: fig6b-sgc-count-increases-with-age\n  statement: The number of Penk+Nptx2+Sorcs3+ cells (SGCs) in the suprapyramidal GCL of WT mice\n    increases with age.\n  source: Figure 6b'; Results, SGC numbers in the DG increase during the adolescence-adulthood\n    transition in WT mice, paragraph 1\n  quote: We found that the numbers of Penk+Nptx2+Sorcs3+ GCs also increased with age\n  statistics:\n  - about: age effect\n    test: Kruskal-Wallis test\n    statistic: KW = 9.5\n    p: 0.0012\n  - about: 1 against 12 months\n    test: Dunn's multiple comparisons\n    p: 0.039\n    corrected: Dunn\n  criterion: Per mouse counts at 1, 2, 3 and 9 to 12 months; Kruskal-Wallis test with Dunn's\n    comparisons. The Results print P = 0.0012 and the legend P = 0.001. Reproduced when both have p <\n    0.05 with 12 months higher than 1 month.\n- id: figs9a-age-dynamics-lost-v321l\n  statement: The age-dependent increase in SGC number seen in WT mice is lost in V321L mice.\n  source: Figure S9A; Results, SGC numbers in the DG increase during the adolescence-adulthood\n    transition in WT mice, paragraph 1\n  quote: These dynamics of SGC abundance over adolescence were lost in the V 321 L DG\n  statistics:\n  - about: effect of time\n    test: two-way ANOVA\n    p: 0.008\n  - about: WT 1 against 12 months\n    test: Bonferroni corrected comparison\n    p: 0.008\n    corrected: Bonferroni\n  criterion: Two-way ANOVA (genotype by age) of per-mouse Penk+Nptx2+Sorcs3+ counts with Bonferroni\n    comparisons between ages within genotype (legend). Reproduced when the WT 1 against 12 month\n    comparison has p < 0.05 and no V321L comparison does (the absence half judged on these\n    comparisons).\n- id: figs9b-marker-fraction-stable\n  statement: The percentage of Penk+ cells that are Nptx2+Sorcs3+ does not change with age in either\n    genotype.\n  source: Figure S9B; Results, SGC numbers in the DG increase during the adolescence-adulthood\n    transition in WT mice, paragraph 1\n  quote: There were no significant differences in the overall percentage of Nptx2 - or Sorcs3\n    -expressing Penk + GCs at any of the ages\n  statistics:\n  - about: WT\n    test: Brown-Forsythe ANOVA\n    statistic: F = 2.1 [3, 4.75]\n    p: 0.2\n    n: 3 mice per age group\n  - about: V321L\n    test: Brown-Forsythe ANOVA\n    statistic: F = 0.99 [2.0, 4.3]\n    p: 0.44\n    n: 3 mice per age group\n  criterion: A claim of absence, judged on Brown-Forsythe ANOVA per genotype at p < 0.05. Reproduced\n    when neither genotype shows an age effect.\n- id: figs9d-penk-not-immature\n  statement: Penk+ cells in the GCL do not express the immature neuron marker Dcx.\n  source: Figure S9D; Results, SGC numbers in the DG increase during the adolescence-adulthood\n    transition in WT mice, paragraph 2\n  quote: we did not find any Penk + cells that expressed the immature neuron marker doublecortin ( Dcx )\n    at 3 mo of age\n  criterion: Count of Penk+Dcx+ cells in the GCL in FISH (cells with at least 5 puncta of each).\n    Reproduced when the count is zero.\n- id: figs10d-go-resting-membrane-potential\n  statement: The 60 genes both enriched in Penk+ GCs and in the cluster 18 end-trajectory modules are\n    enriched for gene ontology terms whose top term by odds ratio is regulation of resting membrane\n    potential, driven by Kcnk1 and Kcnj2.\n  source: Figure S10C and S10D; Results, SGC numbers in the DG increase during the\n    adolescence-adulthood transition in WT mice, paragraph 2\n  quote: we identified 60 genes that met this criterion ... the feature of highest odds ratio being\n    regulation of RMP, in line with our results showing a more hyperpolarized RMP in morphologically\n    identified SGCs ( Fig 1J ). This enrichment was driven by two potassium channel genes— Kcnk1 and\n    Kcnj2\n  expected:\n  - quantity: genes in the intersection\n    value: 60\n    tolerance: 6\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: Monocle3 find_gene_modules on WT GCs, modules correlated with the cluster 18 end\n    trajectories, intersected with the Penk+ enriched genes; enrichR GO_Biological_Process_2023, terms\n    with adjusted p < 0.05 ranked by odds ratio (legend and Methods). Reproduced when the count is\n    within tolerance and the top term is regulation of resting membrane potential with Kcnk1 and\n    Kcnj2 as its genes.\n- id: fig7a-type3-nrg1-declines\n  statement: Type III Nrg1 expression in the suprapyramidal DG of WT mice declines from 1 to 12 months\n    of age; the decline from 1 to 3 months is not significant.\n  source: Figure 7A; Results, Natural decline in capacity for Nrg1 nuclear back-signaling corresponds\n    to the SGC fate, paragraph 1\n  quote: We found that Type III Nrg1 expression declined from 1 to 12 mo of age in WT mice; however,\n    the reduction between 1 and 3 mo of age was not significant\n  statistics:\n  - about: age effect\n    test: Kruskal-Wallis test\n    statistic: KW = 6.25\n    p: 0.01\n    n: 3 mice per age group\n  - about: 1 against 12 months\n    test: Dunn's multiple comparisons\n    p: 0.04\n    corrected: Dunn\n  criterion: Per mouse, Type III Nrg1 FISH fluorescence intensity density normalized to the area of the\n    suprapyramidal blade (Methods). Kruskal-Wallis with Dunn's comparisons. Reproduced when the age\n    effect and 1 against 12 months have p < 0.05 with lower values at 12 months, and 1 against 3\n    months has p >= 0.05.\n- id: fig7bc-bace1-low-in-sgcs\n  statement: Bace1 expression peaks at intermediate pseudotime and drops at maximal pseudotime while\n    Nrg1 rises along pseudotime; fewer than 10 WT cells co-express Penk, Nrg1 and Bace1, so most\n    Penk+Nrg1+ GCs lack detectable Bace1.\n  source: Figure 7B and 7C; Results, Natural decline in capacity for Nrg1 nuclear back-signaling\n    corresponds to the SGC fate, paragraph 2\n  quote: Bace1 expression was found to be higher in cells at intermediate pseudotime compared with the\n    beginning or end of the trajectories ... examination of cells expressing Penk, Nrg1 , and Bace1 in\n    WT DG resulted in <10 cells showing co-expression of all three markers\n  data: elsewhere\n  where: GEO GSE280167\n  criterion: WT GC pseudotime from fig5b-pseudotime-sorcs3-top, split into thirds. Reproduced when mean\n    Bace1 expression is highest in the middle third and lower in the last third than the middle,\n    mean Nrg1 is highest in the last third, and fewer than 10 WT GCs have raw counts above 0 for all\n    of Penk, Nrg1 and Bace1. The thirds are not from the paper.\n  depends_on:\n  - fig5b-pseudotime-sorcs3-top\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001545/10.26508-lsa.202403169.yaml paper/10.26508-lsa.202403169.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 52 quotes pass. Two quotes carry the paper's em dashes; I'll cut around them, then check for banned words and colon-space in plain scalars.

**Agent calls Bash**

```bash
cd  f=claims/001545/10.26508-lsa.202403169.yaml; python3 - "$f" <<'EOF'
import sys
p=sys.argv[1]; s=open(p).read()
s=s.replace("""  quote: LDA resulted in successful capture of cell-type differences between GCs and SGCs (along the
    primary classifier—LD1) but not between genotypes""","""  quote: LDA resulted in successful capture of cell-type differences between GCs and SGCs (along the
    primary classifier ... LD1) but not between genotypes""")
s=s.replace("""This enrichment was driven by two potassium channel genes— Kcnk1 and
    Kcnj2""","""This enrichment was driven by two potassium channel genes ... Kcnk1 and
    Kcnj2""")
open(p,'w').write(s)
EOF
grep -n "—\|rather" $f; grep -n "^[^#]*[a-z]: .*: " $f | grep -v 'quote: "' | head; python tools/claims_check.py $f paper/10.26508-lsa.202403169.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/001545/10.26508-lsa.202403169.yaml; grep -nv '^\s*#' $f | sed -E 's/^[0-9]+:\s*(- )?[a-z_0-9]+: //' | grep -n ': ' | head; grep -c "^- id:" $f; grep -c "data: elsewhere" $f; grep -c "criterion:" $f; grep -c "statistics:" $f
```

```
9:75:    top cell body layers, under 20 micrometres from the surface).
12:78:  statistics:
19:85:    (Methods, Imaging and image analysis). Two-tailed Welch's t test of WT SGC against WT GC
20:86:    positions, as in the legend. Reproduced when p < 0.0001 with SGCs nearer the boundary; partially
21:87:    reproduced when p < 0.05 with SGCs nearer the boundary.
26:92:  statistics:
32:98:    dendritic termination through the soma centre to the opposite one). Two-tailed Welch's t test.
33:99:    Reproduced when p < 0.05 with SGCs wider.
38:104:  statistics:
44:110:    (legend). Mann-Whitney test; tails are not stated, so two-tailed (the paper's t tests are marked
52
16
52
33
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/001545/10.26508-lsa.202403169.yaml'))
def walk(o,k=''):
  if isinstance(o,dict):
    for a,b in o.items(): walk(b,a)
  elif isinstance(o,list):
    for b in o: walk(b,k)
  elif isinstance(o,str) and ': ' in o: print(k,'::',o[:100])
walk(d)
print(len(d['claims']), sum('quote' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']))
"
```

```
52 52 33 52
```

**Agent**

I wrote `claims/001545/10.26508-lsa.202403169.yaml`, with 52 claims. The quote checker reports 0 problems.

**Text read.** The version of record as Europe PMC serves it (PMC12032840): main text, Methods, and all figure legends including Figs S1 to S10. One supplement was not under `paper/`: the Key Resources Table (Supplemental Data 1, a docx). It holds the GEO accession and the code links, so I took it from the Europe PMC supplementary bundle. I also looked at the Fig 2 and Fig S2 images from that bundle. Tables S1 to S6 are gene lists and no criterion needed them.

**Sources beyond the paper text:**
- **Ephys code:** `nsdesai/patch_clamp_analysis`, commit 5d756c2 (MATLAB). It only extracts features; the paper says the statistics were run in Prism and the regression and LDA in R.
- **Sequencing code:** `RajNINDS/V321L-snMultiome`, commit c124726 (R).
- **Kim et al 2024 (Cell Rep):** the Methods take their feature definitions from this paper, so I read it too.

**Claims:**
- 52 claims, all with quotes and criteria; 33 have statistics.
- 16 claims use the sequencing data, which is in GEO (GSE280167), not the dandiset. Their `data` is marked `elsewhere`.
- The ones the dandiset can test are Figs 1J to L, S1, 2I to K, 2M, S2D to G and the multiple regression. The morphology and soma-position claims also need those data, if the dandiset holds them.

**Details left open, with the readings named:**
- **Which 20 features:** Kim et al and Fig S2C list 18, and the code outputs 21. The paper also uses an upstroke/downstroke ratio that neither defines. Readings: the 18, or the code's 21.
- **Kim et al against the code:**
  - Spike threshold is 20 mV/ms in Kim et al and 10 mV/ms in the code.
  - Input resistance uses the −20 pA step in Kim et al; the code fits steps from −50 to 0 pA.
  - For downstroke, the code's window runs to the end of the 500 ms step, so it can include later spikes; Kim et al take only the first spike.
  
  Kim et al's definitions are the main reading and the code's are variants.
- **Mann–Whitney tails:** not stated, so one- and two-tailed tests are both run.
- **LDA (Fig 2G and 2M):** the classes are not stated; I read four (genotype by cell type), because the figures show an LD2 axis. Whether PCA comes before the Fig 2M LDA is also open.
- **Classifier (Fig S2G):**
  - V321L data scaled with their own mean and SD, or with WT's.
  - "78%" as the mean over folds, or pooled out-of-fold.
  - The fold seed is not given.
- **Regression:** how cell type is coded (which type is 1), which flips the sign of β1.
- **k-means (Figs S2B, S2D):** the scaling, number of PCs and seed are not given.
- **PCA ellipses (Fig S2E):** a 95% ellipse of the data, or of the group mean.

**Mismatches inside the paper (recorded in the claims):**
- **Prox1+ count (Fig S3B):** the Results give Mann–Whitney P = 0.69, the legend Welch's t P = 0.5. Both tests are run.
- **Classifier accuracy (Fig S2G):** the confusion matrices give 16/21 (76%) and 11/23 (48%, kappa about −0.09). The text says 78% (kappa 0.57) and 52% (kappa 0.08).
- **p-values that differ between text and legend:** Fig 6a′ (0.0032 against 0.002) and Fig 6b′ (0.0012 against 0.001).
- **Fig S1B:** P = 0.0543 is counted as significant, so the criterion accepts a p up to 1.1 times the reported value.

**Thresholds I set myself:** several criteria for claims the paper only describes in words use cutoffs it does not give: 90% separation on LD1, top decile or thirds of pseudotime, a 40 to 60% share for "uniformly", and "8 of 10 clusters" for "nearly all". Each is marked in its criterion as not from the paper. The second reader should look at these first.

**Missing from the paper:** nothing a claim needed, once the Key Resources Table was fetched.

## End of run

35 turns, 9 minutes, result: success.
