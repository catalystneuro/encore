# 000226 · verifier-1 · run 39005383129

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs paper 2>/dev/null; cat *claims* 2>/dev/null | head -200
```

```
total 360
drwxr-xr-x 5 runner runner    4096 Oct 17 05:24 .
drwxr-xr-x 7 runner runner    4096 Oct 17 05:24 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 17 05:24 .claude
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.development
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.local
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.production
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.test
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .env.test.local
drwx------ 2 runner runner    4096 Oct 17 05:24 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .github
-rw-r--r-- 1 runner runner       0 Oct 17 05:24 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 17 05:09 .mcp.json
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.neuron.2017.03.045.yaml
```

```
# Claims for Severson, Xu, Van de Loo, Bai, Ginty and O'Connor (2017) on dandiset 000226.
# Source: the accepted author manuscript in PubMed Central (PMC5528144), full text, read from
# its Results, STAR Methods, Glossary and figure legends, and the publisher's Supplemental
# Information (mmc1.pdf), whose Table S1 lists every recording with its type and analyses.
# The version of record is not open access. The paper's analysis code is not public (the
# Methods say it is available on request); no repository for this paper was found.
#
# When these criteria were written, the author had seen the data check only: the file list,
# the metadata and trial tables of every file, the units and ranges of every series, the
# trial and spike counts per file, per-file mean spike rates in crude categories (contact,
# whisking above 2.5 degrees, below 1 degree; without the distance-to-pole rule), per-file
# phase tuning in 30 equal-width bins, and the spike rate in fifths of each progressive
# cutting session. No claim's analysis had been run.
#
# The dandiset holds one NWB file per recording: 56 afferents and 4 EMG sessions, matching
# Table S1. It does not say which experiment a recording belongs to, which recordings the
# paper excluded, the afferent type (RA or SA), or which afferents were identified as Merkel.
# These come from Table S1. Group membership (touch recording, cut-whisker recording,
# whisking-only recording, progressive cutting, EMG) maps the dandiset's own recording ids to
# experiments and brings in no measurement, so claims that use only it are `with_labels`.
[... 447 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_severson_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1305 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Severson et al. (2017) from dandiset 000226
3	
4	**Paper.** Severson KS, Xu D, Van de Loo M, Bai L, Ginty DD, O'Connor DH (2017). Active touch and
5	self-motion encoding by Merkel cell-associated afferents. *Neuron* 94:666-676.
6	[doi:10.1016/j.neuron.2017.03.045](https://doi.org/10.1016/j.neuron.2017.03.045). This attempt used
7	the full text of the accepted author manuscript in PubMed Central (PMC5528144) and the publisher's
8	Supplemental Information (Table S1 and the supplemental figure legends). The version of record is
9	not open access. The paper's analysis code is not public; the Methods say it is available on
10	request, and no repository for it was found.
11	
12	**Dandiset.** [DANDI:000226](https://dandiarchive.org/dandiset/000226/0.230607.1747), version
13	0.230607.1747. The paper cites no DANDI version (it predates the deposit). This is the only
14	published version; the draft has the same 60 assets and size, so the most recent published
15	version is pinned.
16	
17	**What the dandiset holds.** One NWB file per recording: 56 trigeminal afferents recorded with
18	high-speed whisker video, and 4 EMG sessions, which match the 60 recordings of Table S1. Each file
19	holds the spike times of one unit (none in three EMG files) and, for every 5 s trial, the whisker
20	kinematics, contact, distance to the pole, curvature change, and for most recordings with a pole,
[... 676 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 697,
 "limit": 610
}
```

```
697	for reading, col in (("(a) all spikes", "class_a"), ("(b) whisking-in-air spikes", "class_b"), ("Poisson CIs, (a)", "class_poisson")):
698	    star = cr[cr[col] == "WT*"]
699	    agree = (cr[col].str.replace("none", "T") == cr.table_class).sum()
700	    print(f"{reading}: classes {cr[col].value_counts().to_dict()}; WT* n = {len(star)}, whisking-in-air rate median "
701	          f"{star.wia.median():.1f} Hz IQR {iqr(star.wia):.1f}; class agrees with Table S1 for {agree} of 33")
702	for reading, c in (("(a)", "class_a"), ("(b)", "class_b")):
703	    star = cr[cr[c] == "WT*"]
704	    print(f"WT* under {reading} by type:", star.type.value_counts().to_dict(), "; Merkel:", int(star.merkel.sum()),
705	          "; same set as Table S1's WT*:", set(star.rec) == set(cr.rec[cr.table_class == "WT*"]))
706	print("(paper: 5 Merkel, 7 SA, 1 RA)")
707	print("\nDisagreements with Table S1 under (a) or (b):")
708	print(cr[(cr.class_a.str.replace("none", "T") != cr.table_class) | (cr.class_b.str.replace("none", "T") != cr.table_class)][["rec", "table_class", "class_a", "class_b", "wia", "nonwhisking", "contact", "total_spikes", "wia_spikes"]].round(2).to_string(index=False))
709	fig, ax = plt.subplots(figsize=(10, 3))
710	o = cr.sort_values("contact").reset_index(drop=True)
711	for col, c in (("nonwhisking", "0.7"), ("wia", "0.3"), ("contact", "tab:purple")):
712	    ax.plot(o.index, o[col] + 0.01, "o", color=c, label=col)
713	ax.set_yscale("log"); ax.set_xticks(o.index, o.rec, rotation=90, fontsize=7); ax.set_ylabel("rate + 0.01 (Hz)"); ax.legend(fontsize=7)
714	print("Plotted rates span", round(cr[["nonwhisking", "wia", "contact"]].min().min(), 3), "to", round(cr[["nonwhisking", "wia", "contact"]].max().max(), 1), "Hz; none outside the axes.")
715	plt.show()
716	--OUT--
[... 590 more lines not kept]
```

**Agent**

Notebook read. Next I'm reading the helper module.

**Agent calls Read**

```json
{
 "file_path": "merkel.py"
}
```

```
1	"""Loading and measures for dandiset 000226 (Severson et al. 2017, Neuron 94:666).
2	
3	Each NWB file holds one recording: one afferent's spike times (`units`), or none for three EMG
4	sessions, and per-trial time series at 500 Hz in `processing/behavior`, one TimeSeries per trial
5	and variable (position, velocity, acceleration, jerk, phase, amplitude, setpoint, frequency, M0,
6	dM0, Faxial, Flateral, dFaxial, dFlateral, contact, distanceToPoleCenter, deltaKappa and others).
7	
8	Files are streamed from the DANDI archive into memory, whole, and never written to disk: each file
9	holds thousands of small datasets, and reading them one HTTP range request at a time took 22 minutes
10	for the metadata alone, against about two minutes for the whole dandiset read in full.
11	
12	Where parameters come from:
13	- Behavioural categories, the outlier percentiles, the WT/WT* rules: the paper's Glossary.
14	- 30 equal-count phase bins, Gaussian smoothing of sigma 4 ms, the viscoelastic model (Eqs. M1 to
15	  M4, q = 1,000 Hz/Pa, M0 scaled by the inverse of its 80th percentile): the STAR Methods.
16	- Bootstrap over trials (1,000 resamples) for the 95% CIs: a common choice; the Methods say only
17	  "bootstrap".
18	- The GAM substitute (cubic B-splines with 10 basis functions per variable, second-difference
19	  penalty lambda = 1, binomial model with two trials per 2 ms frame, at most 60,000 frames per
20	  fit): a common P-spline choice; the paper used mgcv with UBRE smoothing on 1 ms bins.
[... 587 more lines not kept]
```

**Agent**

Now I'll fetch the paper text and the DANDI metadata to check Table S1, the methods, and the blocked claims.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5528144/" -A "Mozilla/5.0" -o paper/PMC5528144.html; ls -la paper; curl -sL "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5528144/fullTextXML" -o paper/PMC5528144.xml; ls -la paper; head -c 500 paper/PMC5528144.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm PMC5528144.xml; grep -o '<title>[^<]*' PMC5528144.html; curl -sL "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=5528144&rettype=xml" -o pmc_efetch.xml; ls -la; head -c 300 pmc_efetch.xml
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; rm PMC5528144.html; python3 -c "
import re,html
t=open('pmc_efetch.xml').read()
t=re.sub(r'<table-wrap.*?</table-wrap>','[TABLE]',t,flags=re.S)
t=re.sub(r'<(p|title|sec)[ >]','\n<\\\\1 ',t)
t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
open('severson2017_text.txt','w').write(t)
"; wc -c severson2017_text.txt; grep -n -i -E 'supplementary|mmc' pmc_efetch.xml | head
```

```
109037 severson2017_text.txt
57:behavior (<xref rid="F1" ref-type="fig">Figures 1</xref> and <xref rid="SD1" ref-type="supplementary-material">S1</xref>). Mice whisked freely in air and against a
66:cause spiking (<xref rid="F2" ref-type="fig">Figure 2</xref>; <xref rid="SD2" ref-type="supplementary-material">Video S1</xref>). We aligned spike times from single
90:and <xref rid="SD1" ref-type="supplementary-material">Table S1</xref>). For a subset of WT
112:variables (<xref rid="SD1" ref-type="supplementary-material">Figure S2A–D</xref>).
120:(<italic toggle="yes">r</italic> = 0.48 ± 0.19, n = 33; <xref rid="F3" ref-type="fig">Figures 3D</xref> and <xref rid="SD1" ref-type="supplementary-material">S2C</xref>). Thus, although afferents responded to multiple mechanical variables,
123:and <inline-formula><mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML" id="M7" display="inline" overflow="scroll"><mml:mrow><mml:msubsup><mml:mi>M</mml:mi><mml:mn>0</mml:mn><mml:mo>′</mml:mo></mml:msubsup></mml:mrow></mml:math></inline-formula>, we constructed joint tuning surfaces (<xref rid="F3" ref-type="fig">Figures 3E,F</xref> and <xref rid="SD1" ref-type="supplementary-material">S2E</xref>). These surfaces show the mean spike rate evoked by combinations of
128:motifs across afferents (<xref rid="F3" ref-type="fig">Figures 3H,I</xref> and <xref rid="SD1" ref-type="supplementary-material">S2E</xref>).</p><p id="P13">Moment at the base of the whisker and its rate of change were critical drivers
161:not collect whisker-pole contact data; <xref rid="SD1" ref-type="supplementary-material">Table S1</xref>). Preferred phase of each afferent was largely invariant across whisk
162:cycles of different amplitudes, frequencies and setpoints (<xref rid="SD1" ref-type="supplementary-material">Figure S3</xref>). Across the population of afferents,
201:the intrinsic protractor (IP) and <italic toggle="yes">m. nasolabialis</italic> (NL) muscles (<xref rid="F7" ref-type="fig">Figure 7A</xref>, s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -o 'xlink:href="[^"]*"' pmc_efetch.xml | sort -u | head -20; grep -n -i -E 'viscoelastic|Glossary|bootstrap|cross-valid|UBRE|equal number|Hilbert|baseline curvature|sigma|nasolabialis|optogenetic|latency' severson2017_text.txt | head -80
```

```
xlink:href="GH111110"
xlink:href="GSE63473"
xlink:href="KX266255"
xlink:href="N70450"
xlink:href="NIHMS865553-supplement-1.pdf"
xlink:href="NIHMS865553-supplement-2.mp4"
xlink:href="NIHMS865553-supplement-3.mp4"
xlink:href="P01137"
xlink:href="http://aml31.genome.wustl.edu"
xlink:href="http://bowtie-bio.sourceforge.net/bowtie2/index.shtml"
xlink:href="http://cogcell.org/"
xlink:href="http://dx.doi.org/10.17632/5hvpvspw82.1"
xlink:href="http://dx.doi.org/10.17632/wx6s4mj7s8.2"
xlink:href="http://medschool.umaryland.edu/btbank/"
xlink:href="http://nybb.hs.columbia.edu/"
xlink:href="http://redishlab.neuroscience.umn.edu/MClust/MClust.html"
xlink:href="http://samtools.sourceforge.net/"
xlink:href="http://scanimage.vidriotechnologies.com/display/ephus/Ephus"
xlink:href="http://wavesurfer.janelia.org"
xlink:href="http://www.ncbi.nlm.nih.gov/projects/genome/assembly/grc/human/"
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 590,760p severson2017_text.txt
```

```
then rectified and binned to obtain the mean rectified EMG for each 2 ms high-speed
video frame. For the m. nasolabialis recording, we observed apparent
motor unit spikes (Deschenes et al., 2016), and
obtained the times of these spikes by thresholding the bandpass filtered signal. The
m. nasolabialis phase tuning curve (Figures 7A and S4G–H) was then obtained using these motor unit spike times. Whisk
phase was determined by tracking a C-row or Greek whisker.


Video frames (640 pixels × 480 pixels, 32 μm/pixel) were
acquired at 500 Hz using a PhotonFocus DR1-D1312-200-G2-8 camera (90 μs exposure
time) and Streampix 5 software (Norpix). Light from a 940 nm LED (Roithner Laser) was
passed through a condenser lens (Thorlabs) and directed into a 0.25× telecentric
lens (Edmund Optics) after passing through the whisker field. Ephus triggered individual
camera frames (5 s, 2,500 frames per trial) synchronized with electrophysiological
recordings.


Tuning curves and surfaces were constructed after removing outliers (defined
in “Glossary” subsection below). Phase tuning curves were formed by
binning data into 30 bins with approximately equal numbers of observations in each. For
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i 'glossary' severson2017_text.txt | head; awk 'NR>=840 && NR<=1000' severson2017_text.txt
```

```
608:in “Glossary” subsection below). Phase tuning curves were formed by
666:“Glossary” subsection) for any of θ,
perpendicular to its long axis and located at the center of its base. I
was estimated by the equation: I=πρR2(15L2x5-12Lx4+13x3) where whisker density (ρ) was
assumed to be 2000 kg/m3.
Sweeps with manual manipulations (touch, handling, cutting) were identified
using high-speed video and removed from further analysis. The video recording session
was partitioned into “cutting groups” that included all sweeps prior to
any cutting or handling manipulation (intact), following sham handling
(sham), and following each n-th cut (Cut
n). Because the fully cut whisker could not be tracked, kinematic quantities
were acquired from a surrogate whisker (described below). Spike waveforms were obtained
and clustered across the entire session as described above. Units were included in
further analyses if the shape and amplitude of the mean waveform of manual touch-evoked
spikes did not change significantly over time and matched the mean waveform of
whisking-evoked spikes (if any) for each cutting group.


The backbone of each whisker was tracked at subpixel-resolution using the
Janelia Whisker Tracker (Clack et al., 2012),
[... 143 more lines not kept]
```

**Agent**

Methods checked so far match the helper code (viscoelastic equations, GAM smoothing, sigma-kappa definition). Reading the Glossary next.

**Agent calls Bash**

```bash
cd paper; awk 'NR>=1000 && NR<=1130' severson2017_text.txt
```

```
tj are the Ncontact time
points containing whisker-pole contact. This quantifies how large curvature changes
measured during whisking in air were as a percentage of those measured during contact.
As an estimate of “noise”, σk is
conservative in that this assumes curvature change during whisking in air results from
measurement error, whereas to some extent it may also include true inertial bending (cf.
Figure 6). Across 33 sessions, mean
σk was 7.8 ± 5.0% (± SD;
Figure S7).


Bending moment at location p depends on change in curvature
and bending stiffness, Mp =
Δkp(Elp). The
bending stiffness, Elp, is the product of Young’s
Modulus (E) and the area moment of inertia at p,
(E), a geometrical quantity (Birdwell
et al., 2007; Pammer et al., 2013).
Thus, in addition to uncertainty in Δkp (quantified
above), uncertainty in moment must consider E and
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
import re,html
t=open('pmc_efetch.xml').read()
for m in re.findall(r'<table-wrap.*?</table-wrap>',t,flags=re.S):
    s=re.sub(r'<(tr|p)[ >]','\n<x ',m); s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    s=re.sub(r'[ \t]+',' ',s)
    if 'utlier' in s or 'WT' in s or 'whisk' in s.lower(): print(s[:6000]); print('#####')
" | tee glossary.txt | head -150
```

```
KEY RESOURCES TABLE 
 REAGENT or RESOURCE SOURCE IDENTIFIER 
 Antibodies 
 Rabbit monoclonal anti-NeuN Millipore Cat #: MABN140; RRID: AB_2571567 
 Goat polyclonal anti-Rabbit, Alexa Fluor 647 Thermo Fisher Scientific Cat #: A-21244; RRID: AB_2535812 
 Rat monoclonal anti-Cytokeratin 8/18 DSHB, University of Iowa Cat #: TROMA-I; RRID: AB_531826 
 Goat polyclonal anti-Rat, Alexa Fluor 647 Thermo Fisher Scientific Cat #: A-21247; RRID: AB_141778 
 Rabbit polyclonal anti-GFP Millipore Cat #: AB3080P; RRID: AB_2630379 
 Rabbit polyclonal anti-RFP Rockland Cat #: 600-401-379S; RRID: AB_11182807 
 Goat polyclonal anti-Rabbit, Alexa Fluor 488 Thermo Fisher Scientific Cat #: A-11008; RRID: AB_143165 
 
 
 
 
 Bacterial and Virus Strains 
 X 
 
 
 
 
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E 'outlier|percentile|touch-sensitive|whisking-sensitive|1,000 spikes|WT\*' severson2017_text.txt | head -40
```

```
109:WT afferents as “WT*”; STAR Methods).
183:2003). Here, we found that all WT* afferents were also dramatically
187:including the earlier 13 WT* afferents and 2 additional SA afferents that were
188:“putative” WT*: defined as responsive to manual whisker
209:putative WT* afferents (n = 13, including 12 SA and 1 RA), we first
255:from putative WT* afferents (Figure 7F; n
269:during periods of whisking in air for all WT* afferents (n = 28, same
607:Tuning curves and surfaces were constructed after removing outliers (defined
624:k was the inverse of the 80th percentile value for the
628:90th percentile value. Bins were determined as described above, and then
665:and prediction for a whisking in air GAM, a frame could not be an outlier (defined in
668:Similarly, to be included in a contact period GAM, a frame could not be an outlier for
724:M0(t) after outlier removal, and after
725:scaling M0 by the inverse of the 80th percentile
1225:contact frames, and dpole > 2 mm.“Touch-sensitive”
1226:“Whisking-sensitive”
1229:“WT*” neuron
1230:“Outliers”
1235:percentiles (i.e. 1% total were excluded). For θ,
1239:99.75 percentiles. No outlier removal was performed on ϕ.AbrairaVEGintyDD2013The sensory neurons of touchNeuron796186392397259210.1016/j.neuron.2013.07.051PMC3811145BagdasarianKSzwedMKnutsenPMDeutschDDerdikmanDPietrMSimonyEAhissarE2013Pre-neuronal morphological processing of object location by individual
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1205,1239p severson2017_text.txt | cut -c1-1500; sed -n 100,125p severson2017_text.txt; sed -n 175,200p severson2017_text.txt
```

```
Figure 6C). Whiskers in both episodes were
subsequently cut to near the base as depicted in Figure
6.

Author Contributions
TrkCCreER mouse line and procedures to label Merkel
afferents. K.S.S., D.X., M.V. and D.H.O. analyzed data. K.S.S., D.X. and D.H.O. wrote the
paper with input from all authors.
This is a PDF file of an unedited manuscript that has
been accepted for publication. As a service to our customers we are providing this early
version of the manuscript. The manuscript will undergo copyediting, typesetting, and
review of the resulting proof before it is published in its final citable form. Please
note that during the production process errors may be discovered which could affect the
content, and all legal disclaimers that apply to the journal pertain.
“Contact” periods
dpole
< 1 mm.“Whisking” periods
θamp > 2.5°.“Whisking in air” periods
dpole > 2 mm.“Non-whisking” periods
θamp < 1° that are not
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
import re,html
t=open('pmc_efetch.xml').read()
i=t.find('Touch-sensitive'); s=t[i-3000:i+4000]
s=re.sub(r'<[^>]+>',' ',s); print(re.sub(r'\s+',' ',html.unescape(s)))
"
```

```
n in Figure 6B ); the second episode (whisker C4) shows little change in spike rate after cutting (quantification in Figure 6C ). Whiskers in both episodes were subsequently cut to near the base as depicted in Figure 6 . We thank Andrew Russo for technical assistance; Michele Pucak for help with confocal imaging; Terry Shelley for instrument fabrication; Karel Svoboda for discussions during project conception; Mitra Hartmann for suggestions on post hoc whisker imaging. We thank Bilal Bari, Solange Brown, Jeremiah Cohen, Sung Eun Kwon and Genki Minamisawa for comments on the manuscript. This work was supported by NIH grants R01NS34814 (D.D.G.) and P30NS050274. D.H.O. is supported by the Whitehall Foundation, Klingenstein Fund, and NIH grant R01NS089652. D.D.G. in an Investigator of the Howard Hughes Medical Institute. Author Contributions K.S.S. performed all experiments. D.X. developed analysis code and the viscoelastic model with input from K.S.S. and D.H.O. L.B. and D.D.G. developed the TrkC CreER mouse line and procedures to label Merkel afferents. K.S.S., D.X., M.V. and D.H.O. analyzed data. K.S.S., D.X. and D.H.O. wrote the paper with input from all authors. This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. Glossary “Contact” periods Frames with positive contact classification and d pole < 1 mm. “Whisking” periods Frames with θ amp > 2.5°. “Whisking in air” periods Whisking frames with negative contact classification and d pole > 2 mm. “Non-whisking” periods Frames with θ amp < 1° that are not contact frames, and d pole > 2 mm. “Touch-sensitive” 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; for u in "https://europepmc.org/articles/PMC5528144/bin/NIHMS865553-supplement-1.pdf" "https://pmc.ncbi.nlm.nih.gov/articles/instance/5528144/bin/NIHMS865553-supplement-1.pdf" "https://www.cell.com/cms/10.1016/j.neuron.2017.03.045/attachment/mmc1.pdf"; do curl -sL -A "Mozilla/5.0" "$u" -o s.pdf; file s.pdf; [ "$(head -c 4 s.pdf)" = "%PDF" ] && { mv s.pdf supplement1.pdf; echo got $u; break; }; done; rm -f s.pdf; ls
```

```
s.pdf: HTML document, ASCII text, with very long lines (5591), with no line terminators
s.pdf: HTML document, ASCII text, with very long lines (4064)
s.pdf: HTML document, ASCII text, with very long lines (5612), with no line terminators
glossary.txt
pmc_efetch.xml
severson2017_text.txt
```

**Agent**

The supplement (Table S1) is not downloadable here, so I can't check the transcription in `merkel.py`. Next I'm querying the DANDI API about the blocked claims.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://api.dandiarchive.org/api/dandisets/000226/versions/0.230607.1747; curl -s "$B/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d.get(k) for k in ['name','description','assetsSummary','keywords']},indent=1)[:3000])"; curl -s "$B/assets/?page_size=100" > assets.json; python3 -c "
import json; d=json.load(open('assets.json')); print(d['count']); 
for a in d['results'][:100]:
    if any(k in a['path'] for k in ['KSm','ses-20161015','ses-20160923']): print(a['asset_id'],a['path'],a['size'])"
```

```
{
 "name": "Active Touch and Self-Motion Encoding by Merkel Cell-Associated Afferents",
 "description": "Touch perception depends on integrating signals from multiple types of peripheral mechanoreceptors. Merkel-cell associated afferents are thought to play a major role in form perception by encoding surface features of touched objects. However, activity of Merkel afferents during active touch has not been directly measured. Here, we show that Merkel and unidentified slowly adapting afferents in the whisker system of behaving mice respond to both self-motion and active touch. Touch responses were dominated by sensitivity to bending moment (torque) at the base of the whisker and its rate of change and largely explained by a simple mechanical model. Self-motion responses encoded whisker position within a whisk cycle (phase), not absolute whisker angle, and arose from stresses reflecting whisker inertia and activity of specific muscles. Thus, Merkel afferents send to the brain multiplexed information about whisker position and surface features, suggesting that proprioception and touch converge at the earliest neural level.",
 "assetsSummary": {
  "species": [
   {
    "name": "Mus musculus - House mouse",
    "schemaKey": "SpeciesType",
    "identifier": "http://purl.obolibrary.org/obo/NCBITaxon_10090"
   }
  ],
  "approach": [
   {
    "name": "electrophysiological approach",
    "schemaKey": "ApproachType"
   },
   {
    "name": "behavioral approach",
    "schemaKey": "ApproachType"
   }
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://api.dandiarchive.org/api/dandisets/000226/versions/0.230607.1747; for id in c8d93056-5aa2-4359-a30b-a2fe62ed18ff 0e2798f6-adf4-41dd-9a4e-5991a87715e7; do curl -s "$B/assets/$id/" | python3 -c "import json,sys; d=json.load(sys.stdin); [d.pop(k,None) for k in ['digest','contentUrl']]; print(json.dumps(d,indent=1)[:2500])"; done
```

```
{
 "id": "dandiasset:c8d93056-5aa2-4359-a30b-a2fe62ed18ff",
 "path": "sub-KSm6/sub-KSm6_ses-20160602T120000_behavior.nwb",
 "access": [
  {
   "schemaKey": "AccessRequirements",
   "status": "dandi:OpenAccess"
  }
 ],
 "@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.6.3/context.json",
 "approach": [
  {
   "name": "behavioral approach",
   "schemaKey": "ApproachType"
  }
 ],
 "schemaKey": "Asset",
 "identifier": "c8d93056-5aa2-4359-a30b-a2fe62ed18ff",
 "contentSize": 94320403,
 "publishedBy": {
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "import h5py, fsspec; print(h5py.__version__, fsspec.__version__)"; python3 -c "import remfile" 2>&1 | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, fsspec; print(h5py.__version__, fsspec.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
ModuleNotFoundError: No module named 'remfile'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "import numpy, scipy, pandas; print(numpy.__version__, scipy.__version__)"; pip list 2>/dev/null | grep -i -E 'numpy|scipy|h5py|dandi|pandas'
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas; print(numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR; (python3 -m venv v && v/bin/pip install -q numpy scipy 2>&1 | tail -2); v/bin/python -c "import numpy,scipy;print(numpy.__version__,scipy.__version__)"
```

```
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent**

Tools installed. Now testing the helper functions on synthetic inputs.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t.py <<'EOF'
import sys, types
for m in ["h5py","requests","dandi","dandi.dandiapi"]:
    sys.modules[m]=types.ModuleType(m)
sys.modules["dandi.dandiapi"].DandiAPIClient=None
sys.path.insert(0,"
import numpy as np, merkel as M
rng=np.random.default_rng(0)
# 1 phase tuning
ph=rng.uniform(-np.pi,np.pi,300000); lam=(5+40*np.exp(2*np.cos(ph-1.0))/np.exp(2))*M.DT
c=rng.poisson(lam).astype(float)
tc,cen,b=M.phase_tuning(ph,c); print("pref phase",cen[np.argmax(tc)].round(2),"max",tc.max().round(1),"min",tc.min().round(1),"(true 45, ~5.7)")
# 2 spike_counts
s={"starting_time":np.array([0.,10.]),"trial_stop":np.array([7.,17.]),"spike_times":np.array([0.001,0.0021,4.999,5.5,10.0039,20.])}
cnt,w=M.spike_counts(s); print("counts nz",np.argwhere(cnt).tolist(),w)
# 3 visco derivative
p=(1.5,-0.3,0.4,0.8,0.01); x=np.linspace(-2,2,401)
k,C,el,E,eta=p; eps=lambda x:2/(1+np.exp(-k*x+C))-1
num=np.gradient(eps(x),x); ana=2*k*np.exp(-k*x+C)/(1+np.exp(-k*x+C))**2
print("deps/dx max err",np.abs(num-ana).max())
# 4 visco fit recovery
t=np.arange(60000)*M.DT; m0=0.01*np.clip(np.sin(2*np.pi*3*t),0,None)**2; dm0=np.gradient(m0,t)
scale=np.percentile(np.abs(m0),80); ptrue=(2.0,0.5,0.3,0.6,0.002)
rate=M.visco_predict(ptrue,m0/scale,dm0/scale); rate_n=rate+rng.normal(0,20,len(rate))
pf,loss,ok,sc=M.fit_visco(m0,dm0,rate_n,np.random.default_rng(1))
pr=M.visco_predict(pf,m0/sc,dm0/sc); print("visco fit r with truth",np.corrcoef(pr,rate)[0,1].round(4),"params",pf.round(4),ok)
# 5 spline model
X=rng.uniform(-1,1,(60000,2)); eta_=-4+2*np.sin(3*X[:,0])+X[:,1]**2
p_=1/(1+np.exp(-eta_)); y=rng.binomial(2,p_).astype(float)
m=M.SplineModel().fit(X,y); print("spline conv",m.converged,"r(pred,true p)",np.corrcoef(m.predict(X),p_)[0,1].round(4))
# 6 classify
R=lambda r,lo,hi:{"rate":r,"lo":lo,"hi":hi}
print(M.classify({"contact":R(50,40,60),"wia":R(2,1.5,2.5),"nonwhisking":R(0.1,0,0.2),"total_spikes":2000}),
      M.classify({"contact":R(50,40,60),"wia":R(0.15,0.05,0.25),"nonwhisking":R(0.1,0,0.2),"total_spikes":2000}))
# 7 Rayleigh p check by Monte Carlo
n=15;R0=0.448; zs=[np.abs(np.mean(np.exp(1j*rng.uniform(-np.pi,np.pi,n)))) for _ in range(200000)]
print("MC Rayleigh p",np.mean(np.array(zs)>=R0))
# 8 circ_diff
print("circ",M.circ_diff(3.0,-3.0).round(3))
# 9 equal-count bins with ties
print("bins",np.bincount(b).min(),np.bincount(b).max())
EOF
v/bin/python t.py
```

```
pref phase 0.94 max 46.6 min 5.4 (true 45, ~5.7)
counts nz [[0, 0], [0, 1], [0, 2499], [1, 1]] {'in_frames': 4, 'in_trial_after_frames': 1, 'outside_trials': 1}
deps/dx max err 0.001164751818185955
visco fit r with truth 0.9207 params [8.54464e+01 2.00000e+01 2.66000e-02 6.04790e+00 0.00000e+00] True
spline conv True r(pred,true p) 0.9988
WT* T
MC Rayleigh p 0.04541
circ 0.283
bins 10000 10000
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > t2.py <<'EOF'
import sys, types
for m in ["h5py","requests","dandi","dandi.dandiapi"]:
    sys.modules[m]=types.ModuleType(m)
sys.modules["dandi.dandiapi"].DandiAPIClient=None
sys.path.insert(0,"
import numpy as np, merkel as M
rng=np.random.default_rng(0)
t=np.arange(60000)*M.DT
m0=0.01*np.sin(2*np.pi*1.3*t)*np.abs(np.sin(2*np.pi*0.21*t)); dm0=np.gradient(m0,t)
scale=np.percentile(np.abs(m0),80); ptrue=(2.0,0.5,0.3,0.6,0.002)
rate=M.visco_predict(ptrue,m0/scale,dm0/scale)
print("rate sd",rate.std().round(1), "frac from dashpot")
for sd in (0,20):
    rn=rate+rng.normal(0,sd,len(rate))
    pf,loss,ok,sc=M.fit_visco(m0,dm0,rn,np.random.default_rng(1))
    pr=M.visco_predict(pf,m0/sc,dm0/sc)
    print(sd,"r fit-truth",np.corrcoef(pr,rate)[0,1].round(4),"ceiling",np.corrcoef(rn,rate)[0,1].round(4),"r fit-noisy",np.corrcoef(pr,rn)[0,1].round(4),pf.round(4))
EOF
v/bin/python t2.py
```

```
rate sd 77.7 frac from dashpot
0 r fit-truth 0.9978 ceiling 1.0 r fit-noisy 0.9978 [9.5265e+00 2.6123e+00 1.0000e+00 1.8310e-01 7.0000e-04]
20 r fit-truth 0.9978 ceiling 0.9682 r fit-noisy 0.9661 [9.6229e+00 2.6562e+00 1.0000e+00 1.8280e-01 7.0000e-04]
Shell cwd was reset to
```

**Agent**

Helper functions pass the synthetic tests. Last check: what the archive's asset metadata says each file contains, for the blocked EMG and optotagging claims.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://api.dandiarchive.org/api/dandisets/000226/versions/0.230607.1747; python3 - <<'EOF'
import json,urllib.request,collections
B="https://api.dandiarchive.org/api/dandisets/000226/versions/0.230607.1747"
d=json.load(open("assets.json"))
cnt=collections.Counter()
for a in d["results"]:
    m=json.load(urllib.request.urlopen(f"{B}/assets/{a['asset_id']}/"))
    vm=tuple(sorted(v["value"] for v in m.get("variableMeasured",[])))
    desc=[g.get("description") for g in m.get("wasGeneratedBy",[]) if g.get("name")=="Acquisition session"]
    cnt[vm]+=1
    if desc and desc[0] in ("KS0007A","KS0008A","KS0009A","KS0011A","KS0227C","KS0214A","KS0271A"): print(desc, vm, m.get("contentSize"), [x.get("name") for x in m.get("measurementTechnique",[])])
print(cnt)
EOF
```

```
['KS0007A'] ('BehavioralTimeSeries', 'ProcessingModule') 94320403 ['analytical technique', 'behavioral technique']
['KS0008A'] ('BehavioralTimeSeries', 'ProcessingModule') 65955361 ['analytical technique', 'behavioral technique']
['KS0009A'] ('BehavioralTimeSeries', 'ProcessingModule') 62893350 ['analytical technique', 'behavioral technique']
['KS0011A'] ('BehavioralTimeSeries', 'ProcessingModule', 'Units') 117688879 ['analytical technique', 'behavioral technique', 'spike sorting technique']
['KS0227C'] ('BehavioralTimeSeries', 'ProcessingModule', 'Units') 180788480 ['analytical technique', 'behavioral technique', 'spike sorting technique']
['KS0271A'] ('BehavioralTimeSeries', 'ProcessingModule', 'Units') 206740846 ['analytical technique', 'behavioral technique', 'spike sorting technique']
['KS0214A'] ('BehavioralTimeSeries', 'ProcessingModule', 'Units') 94838811 ['analytical technique', 'behavioral technique', 'spike sorting technique']
Counter({('BehavioralTimeSeries', 'ProcessingModule', 'Units'): 57, ('BehavioralTimeSeries', 'ProcessingModule'): 3})
Shell cwd was reset to
```

**Agent**

**A. Outcomes (28 claims in the claims file: 14 reproduced, 3 partially reproduced, 11 blocked)**

| Claim | Outcome | Reason |
|---|---|---|
| table-s1-link | reproduced | Cell 18: all 60 files match a distinct Table S1 recording (2 matched by number and mouse), and 60 of 60 agree on mouse, sex, line and date. |
| video-frames | reproduced | Cell 21: 54,660,000 frames against 54,647,500. Reading (a) gives 65,710,000 against 65,257,500 (ratio 1.007). |
| merkel-minutes | reproduced | Cell 23: 823.8, 998.2 and 846.4 min (reading a), against 823, 999 and 846. |
| fig2c-baseline-rate | reproduced | Cell 25: median 0.03 Hz with IQR 0.20, against 0.0 ± 0.2. |
| fig2c-touch-rate | reproduced | Cell 25: median 47.9 Hz with IQR 94.8, against 48.0. All 33 afferents are touch-sensitive with bootstrap CIs, and also with Poisson CIs. |
| fig2c-wt-star | reproduced | Cell 26, reading (b): 13 WT*, median 19.0 Hz (IQR 57.4), classes agree with Table S1 for 31 of 33, and the WT* set is the same as Table S1's. Reading (a) gives 15 WT*, which fails the count tolerance. |
| fig3a-direction-selective | partially_reproduced | Cell 28: 17 of 26 Merkel/SA afferents (65%) have an index of 0.5 or more. That is at least half but below the 80% needed for reproduced. |
| fig3d-gam-full | reproduced | Cell 30: mean r 0.708 (SD 0.141), against 0.71 ± 0.16. |
| fig3d-gam-single | reproduced | Cell 31: M0 0.441 and M0' 0.415, against 0.45 and 0.42. |
| fig3d-gam-best-pair | partially_reproduced | Cell 31: M0+M0' has r 0.622 and ranks 2nd of 45 behind M0+omega (0.633). Both values are within tolerance and it is above M0,Fax,Flat (0.475). |
| fig4c-viscoelastic | reproduced | Cell 34: mean r 0.657 for the viscoelastic model against 0.686 for the M0,M0' model over 25 afferents, a difference of -0.029. The threshold is -0.1. |
| fig5-phase-modulation | reproduced | Cell 36: medians 2.43 and 51.1 Hz, within the claim's tolerances of 3.4 and 105.7. All 15 afferents have a preferred/non-preferred ratio of at least 2. The cell's own "False" uses a 10% tolerance instead of the claim's (B1). |
| fig5e-phase-span | partially_reproduced | Cell 37: all four quarters are occupied, but the Rayleigh test gives p = 0.047. I confirmed p by Monte Carlo (0.045), so it is below 0.05. |
| figs3-phase-invariance | reproduced | Cell 38: median circular differences of 0.37, 0.59 and 0.48 rad, all below pi/4 (0.785). |
| figs6-kinematic-gam | reproduced | Cell 40: full model r 0.975 ± 0.013 on the 15 afferents the criterion names. Every single-variable model is lower by 0.25 or more. |
| fig7g-phase-span-28 | blocked (metadata_insufficient) | Cells 5 and 42: every trial is labelled `intact` and MOI has one value per file, so the intact condition of the 13 progressive cutting recordings cannot be isolated. |
| fig6-cut-eliminated | blocked (metadata_insufficient) | Same reason. The Methods say sessions were split into intact, sham and Cut n, and the deposit collapses this to `intact`. The fifths table (cell 42) shows a decline but cannot test the claim. |
| fig6-cut-remained | blocked (metadata_insufficient) | Same as above. |
| fig6a-final-length | blocked (data_missing) | Trial columns are MOI, cuttingGroup and barCoor/barRadii/barAzim, with one MOI per file. No whisker length is deposited. |
| fig7d-cut-emg | blocked (metadata_insufficient) | Needs the cut condition, and the intrinsic protractor EMG is absent (see figs4-intrinsic-protractor). |
| fig7e-lost-rate-kinematics | blocked (metadata_insufficient) | Needs intact against cut trials. |
| fig7f-precut-emg | blocked (data_missing) | Intrinsic protractor EMG is absent. A partial test is possible but not done: the 5 cut-only afferents and the nasolabialis curve (11A) are in the archive, and their r gives a lower bound on the best match. |
| figs4-nasolabialis | reproduced | Cell 44: r = 0.924 with negative velocity and -0.716 with positive velocity, both within tolerance. |
| figs4-intrinsic-protractor | blocked (data_missing) | 7A, 8A and 9A have no units and no acquisition data (cells 5, 44). Their asset `variableMeasured` lists only BehavioralTimeSeries and ProcessingModule. Their size per trial (0.31 MB) equals 11A's, which has only behaviour and spikes, so no EMG is stored. |
| sigma-kappa | reproduced | Cell 46: mean 10.01%, within 7.8 ± 5.0. The SD is 6.97, driven by 243B (39.9%) and 265A (28.5%). |
| figs1-optotag-latency | blocked (data_missing) | No asset lists an OptogeneticSeries or stimulus times, and the 3 optotagging-only recordings hold only Units and behaviour. |
| figs1-labelling-specificity | blocked (data_missing) | Histology counts are not in the dandiset. |
| contact-classifier | blocked (data_missing) | The manual contact labels are not deposited. |

The paper states no chance levels for these claims.

**B. Problems**

1. [affects a conclusion] Cell 36 checks fig5 against 10% of the paper's medians and prints False for the non-preferred rate (2.43 against 2.1). The claim's tolerance is the IQR (3.4), under which it passes. An outcome taken from this printout would wrongly be partial. Cell 25 has the same 10% check but passes either way.
2. [affects a conclusion] fig5e depends on a Rayleigh p of 0.047, next to the 0.05 threshold (cell 37). Each preferred phase is the argmax of 30 noisy bins, so another reasonable estimator, such as the circular mean of the tuning curve, could move the outcome to reproduced.
3. [affects a conclusion] For fig3d-gam-best-pair, M0+M0' trails M0+omega by 0.011 and wins in only 19 of 33 recordings. 4th place (Flat+M0', 0.606) is 0.016 behind. The lambda = 100 check (cell 32) was not run on the 45 pairs, and r is in-sample, so the "top three" rank is untested for robustness.
4. [does not affect a conclusion] Cells 11 and 12: the `mean_position` column is all NaN. `reduce()` passes position with NaNs to `bin_means`. So "position peaks near phase 0" is unsupported. `phase_direction` correlates sines, which cannot tell a negated phase from a pi-shifted one. The phase convention is therefore unresolved. This affects only the "retraction" reading in cell 37 and fig7g. The tested statistics (quarter occupancy, Rayleigh, circular differences, curve correlations) are invariant to both.
5. [does not affect a conclusion] Cell 34's "parameters at a bound" is wrong. It checks E against 1000 while `fit_visco` bounds E at 100, and it compares the converted eta (eta_u/sdot) with the normalized bound. On synthetic data `fit_visco` recovers predictions (r 0.998) but not the parameters, so the parameter values in cell 34 should not be interpreted.
6. [does not affect a conclusion] In `fit_r` and cell 34, GAM and viscoelastic r are computed on the fitted frames. The claims file asks for this, and the paper reports cross-validation made little difference. With 60,000 frames and at most 101 coefficients, overfitting is small.
7. [does not affect a conclusion] In `categories`, contact requires whisking (amplitude above 2.5 degrees), which the Glossary's "Contact" definition does not. This follows the claims file.
8. [does not affect a conclusion] Cell 11 shows unexplained data in cut-only recordings: 209A has contact = 1 frames with `distanceToPoleCenter` around 6, and 199B has pole data. Per the Methods, recordings tracked on a surrogate whisker should have no pole in reach. This matters only for a future fig7f test.
9. [does not affect a conclusion] Several tests do not discriminate between readings. All four readings of video-frames pass, and sigma-kappa's readings (a) and (b) are identical.
10. [does not affect a conclusion] fig6a, fig7d, fig7e, fig7f, figs4-intrinsic-protractor, figs1-* and contact-classifier have no notebook cell showing what was checked in the archive.

Synthetic tests passed for `phase_tuning` (recovers preferred phase and peak), `spike_counts` (frame assignment and out-of-frame accounting), `classify`, `circ_diff`, `SplineModel` (r 0.999 with the true probability), and the derivative inside `visco_predict`, which matches Eq. M1.

**C. Not checked**

- **Table S1 transcription (`merkel.TABLE_S1`).** The supplement PDF could not be downloaded here. The text counts are consistent: 14 Merkel, 12 SA and 7 RA among the 33; 5/7/1 WT*; 17/28/8 overall; 15 = 5 Merkel, 9 SA, 1 RA; 13 progressive = 12 SA, 1 RA; 25 of 26 fitted. The type, Merkel, class and viscoelastic columns could only be checked against the PDF. Those columns drive merkel-minutes, fig3a, fig4c and the class agreement in fig2c-wt-star.
- **Full contents of the EMG and progressive files.** h5py is not available here, and the notebook never prints `series_present` or the processing-module names for 7A/8A/9A and the 13 progressive files. Printing them would settle whether any EMG or whisker-length series exists.
- **Phase convention.** A position-by-phase curve computed with nanmean would distinguish a negated phase from a pi shift.
- **Robustness of the borderline outcomes.** These outputs would settle B2 and B3: the 45-pair ranking at another lambda or on held-out frames, and fig5e with a second preferred-phase estimator.
- **fig7f lower bound.** The r between the phase tuning of the 5 cut-only afferents and the 11A nasolabialis curve would give the partial test that the notebook omits.

The paper text I used is saved under `paper/` (from the PMC accepted manuscript, PMC5528144).

## End of run

27 turns, 5 minutes, result: success.
