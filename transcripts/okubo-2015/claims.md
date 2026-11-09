# okubo-2015 · claims · run 42680261171

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 195
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
[... 175 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature15741.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature15741.txt",
 "offset": 948,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature15741.txt",
 "offset": 1648,
 "limit": 670
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the full paper text: main text, Methods and Extended Data legends. Next I'll read the dataset description and the model code.

**Agent calls Read**

```json
{
 "file_path": "paper/am-3.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  head -60 paper/10.1038-nature15741.code.m; grep -n "^function\|^%%" paper/10.1038-nature15741.code.m | head -60; ls papers/datasets/ | grep okubo; cat papers/datasets/okubo-2015.yaml 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls claims/ | head -50; grep -rn "data: elsewhere" claims/ | head; grep -rln "simulat" claims/ | head; sed -n 1,80p tools/claims_check.py | head -80
```

```
amjad-2025.yaml
armstrong-2026.yaml
ashworth-2025.yaml
athalye-2023.yaml
azcorra-2023.yaml
bakalar-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2019.yaml
boran-2022.yaml
bouabid-2026.yaml
bouchard-2013.yaml
bruno-2017.yaml
buccino-2020.yaml
buccino-2024.yaml
calvigioni-2023.yaml
carcea-2021.yaml
chandravadia-2020.yaml
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p claims/bouchard-2013.yaml; grep -n -B3 -A12 "data: elsewhere" claims/berg-2020.yaml | head -40; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
# Claims for Bouchard, Mesgarani, Johnson & Chang (2013), "Functional organization of human
# sensorimotor cortex for speech articulation", Nature 495, 327-332, on dandiset 000019
# ("Human ECoG speaking consonant-vowel syllables").
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The NIH author manuscript as served by PubMed Central (PMC3606666, NIHMS436351),
# not the version of record: main text, figure legends and Methods, with the supplement
# (NIHMS436351-supplement-1.pdf, Supplementary Figures 1 to 13 with their legends,
# Supplementary Table 1 and Supplementary Methods), as extracted to text. No PDF of the main
# text was supplied, so the main figures were read from their legends and from the Results
# sentences that cite them. Supplement pages 2 and 8 were opened in the supplement PDF, to
# see Supplementary Figure 1d and to confirm a printed p-value on page 8.
#
# Code. The paper links no code, and none is named in the Methods or the supplement. Every
# method below is from the Methods, the legends or the Supplementary Methods.
#
# Data the paper describes. Three native English speakers (Supplementary Table 1 names them
# EC2, EC33 and EC31) with a high-density subdural ECoG array over peri-Sylvian cortex, left
# hemisphere in two (EC2, EC31) and right in one (EC33), implanted for epilepsy monitoring.
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:12000])"; grep -n -i "model\|simulat" claims/bouchard-2013.yaml claims/qu-2025.yaml | head -20
```

```
`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     },
     "datasets": {
      "description": "Only when the paper is tested on more than one dataset: the folder names of those this claim rests on.",
      "type": "array",
      "items": {
       "type": "string"
      },
      "minItems": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
[... 206 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn -B2 -A3 "where:.*[Ss]upplementary\|where:.*code\|where:.*simulat" claims/*.yaml | head -40
```

```
claims/berg-2020.yaml-921-    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).
claims/berg-2020.yaml-922-  data: elsewhere
claims/berg-2020.yaml:923:  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
claims/berg-2020.yaml-924-    NEFH expression from the Allen Brain Map RNA-seq data, not pinned
claims/berg-2020.yaml-925-  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.
claims/berg-2020.yaml-926-checks:
--
claims/duszkiewicz-2024.yaml-489-    the mean of the weights
claims/duszkiewicz-2024.yaml-490-  data: elsewhere
claims/duszkiewicz-2024.yaml:491:  where: none deposited; the simulation code (Python, Methods, Data analysis and statistics) is not
claims/duszkiewicz-2024.yaml-492-    in figshare doi:10.6084/m9.figshare.24921252 version 3
claims/duszkiewicz-2024.yaml-493-  criterion: A result of simulation, not of the recordings. It can be tested only by rerunning a
claims/duszkiewicz-2024.yaml-494-    simulation the paper does not fully specify (input tuning widths, number of inputs, the
--
claims/duszkiewicz-2024.yaml-526-    inputs from ADN-HD cells and low firing rate, HD-modulated inputs from PoSub-HD cells
claims/duszkiewicz-2024.yaml-527-  data: elsewhere
claims/duszkiewicz-2024.yaml:528:  where: none deposited; the fitting code (PyTorch, Supplementary Methods) is not in figshare
claims/duszkiewicz-2024.yaml-529-    doi:10.6084/m9.figshare.24921252 version 3
claims/duszkiewicz-2024.yaml-530-  criterion: The fit uses the recorded FS, PoSub-HD and ADN-HD tuning curves (the ADN curves only on
claims/duszkiewicz-2024.yaml-531-    figshare) and three losses minimized with Adam (learning rate 0.0001, 200,000 steps), the
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,145p paper/10.1038-nature15741.code.m; sed -n 510,612p paper/10.1038-nature15741.code.m
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "thres\|candLat\|isShared\|shared" paper/10.1038-nature15741.code.m | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz,os
d=fitz.open('paper/10.1038-nature15741.pdf'); print(len(d))
t=os.environ.get('TMPDIR','/tmp')
for i in [1,12]:
    pg=d[i]; pix=pg.get_pixmap(dpi=110); pix.save(f'{t}/p{i+1}.png'); print(f'{t}/p{i+1}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; python -c "import pypdfium2" 2>&1; ls ~/.venv* 2>/dev/null; pip list 2>/dev/null | grep -i -E "pdf|mupdf"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature15741.pdf",
 "pages": "1"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature15741.pdf",
 "pages": "13"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
from scipy.stats import chi2_contingency as c, fisher_exact as f
for t in ([[22,83],[10,90]],[[22,21],[4,28]]):
    print(c(t,correction=False)[1], c(t,correction=True)[1], f(t)[1])
from scipy.stats import mannwhitneyu
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import chi2_contingency as c, fisher_exact as f
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
python3 -c "
import math
def chi(t,yates):
    a,b=t[0];c,d=t[1];n=a+b+c+d
    num=abs(a*d-b*c)-(n/2 if yates else 0)
    x=n*num**2/((a+b)*(c+d)*(a+c)*(b+d))
    return math.erfc(math.sqrt(x/2))
for t in ([[22,83],[10,90]],[[22,21],[4,28]]):
    print(chi(t,False),chi(t,True))
"
```

```
0.03080027275872116 0.049165505500545666
0.0005018775267575983 0.00121869138420678
```

**Agent**

The chi-square test without continuity correction reproduces both printed p-values (0.031 and 5.0e-4), so the criteria can use that variant. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/okubo-2015.yaml",
 "content": "# Claims for Okubo, Mackevicius, Payne, Lynch & Fee (2015), \"Growth and splitting of neural\n# sequences in songbird vocal development\", Nature 528, 352-357, doi:10.1038/nature15741, tested on\n# CRCNS am-3 (\"Single-unit extracellular recordings of projection neurons in the premotor cortical\n# area HVC of juvenile male zebra finches during singing\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. The version of record (paper/10.1038-nature15741.txt, extracted from the publisher's\n# PDF): main text, figure legends, Methods and the legends of Extended Data Figures 1 to 10. The\n# Supplementary Information is the model code (read, below) and Supplementary Videos 1 and 2\n# (not supplied; no claim rests on them alone). The PDF could not be rendered in this run (no PDF\n# renderer installed), so figures were read only from their legends and the Results sentences\n# that cite them. In Fig. 1f, Fig. 1g and Extended Data Fig. 1c the extracted text shows the\n# significance stars but not which stage each belongs to; the claims that use them say so.\n#\n# Code. The paper's Supplementary Information holds HVCModelCode (MATLAB, by E. Mackevicius,\n# 2015-07-18), supplied as paper/10.1038-nature15741.code.m. It reproduces Fig. 5a-d and\n# Extended Data Fig. 10a-d: the binary network (HVCIter), the alternating and bout-onset training\n# schedules, and the plotting, with seed 9038. Its comment points to github.com/emackev/HVCModelCode\n# for the other figures (motif strategy, Extended Data Fig. 10e-k); that repository was not read\n# and no commit is pinned. The code agrees with the Methods' parameters. It settles what the\n# Methods leave open for the model: a neuron participates in a syllable type when it fires at its\n# most common latency more than a fixed number of times per iteration (12 in subsong, 4 in the\n# protosyllable stage, 2 per type in the splitting stage; 4 and 6 for the bout-onset and\n# protosyllable types in bout-onset differentiation); Fig. 5c is iteration 992 (492 splitting\n# iterations) and Fig. 5d iteration 2,500. The Methods describe the threshold as 90% of surrogate\n# peaks; the code's comments say its fixed values came from that test, so the code's values are\n# used. No analysis code for the recordings is linked; every data method below is from the Methods\n# and legends.\n#\n# Data the paper describes. Male zebra finches singing undirected song: 32 juvenile birds, 44 to\n# 112 days post-hatch (dph), plus 3 adult birds (over 120 dph). 1,149 HVC projection neurons in\n# all (35 birds), single units recorded with a motorized microdrive during singing; cell type\n# HVCRA or HVCX by antidromic stimulation from RA or Area X, or HVCp (putative projection neuron,\n# 211 of 1,149). Each day of singing is assigned a song stage: subsong, protosyllable,\n# multi-syllable, motif, or adult (over 120 dph). Measured variables: spike times, the song audio,\n# syllable onsets and offsets (segmented on 1 to 4 kHz power; phase segmentation for bird 3 and\n# for bird 4's protosyllable stage), syllable labels (Greek letters for juvenile syllables, Latin\n# capitals for adult ones), and the bird's age. Paper bird numbers to archive names (Methods,\n# Animals): bird 1 to3965, bird 2 to3779, bird 3 to3017, bird 4 to5640, bird 5 to3396, bird 6\n# to2309, bird 7 to3412, bird 8 to3567, bird 9 to2462, bird 10 to2331, bird 11 to2427, bird 12\n# to3352. Birds 1 to 6 were recorded during the emergence of several syllable types (769\n# neurons); bird 1 has 375 neurons and bird 2 has 125. The dataset's title and data descriptor\n# say it holds the juvenile recordings (32 birds, 44 to 112 dph) with per-neuron spike times,\n# syllable segments and labels, sound files, song stage, age and cell type; its files were not\n# looked at.\n#\n# Data from outside the recordings (step 4). The adult stage (3 birds, 32 neurons) \"included a\n# reanalysis of previously published HVC recordings\" (Methods, Animals; ref. 20, Kozhevnikov &\n# Fee 2007, J. Neurophysiol. 97, 4271-4283). The data descriptor lists only juvenile birds, so\n# claims that use the adult stage are marked with_inputs. The model claims use the simulation\n# code, not the recordings, and are marked elsewhere.\n#\n# Definitions used by several criteria, from the Methods unless marked.\n# - Bouts. Continuous sequences of syllables separated by gaps no longer than 300 ms; bout onset\n#   is the first syllable's onset, bout offset the last syllable's offset. Introductory notes are\n#   excluded. Only spikes during singing (first syllable onset to last syllable offset of a bout)\n#   are used for rhythmicity. Neurons with less than 5 s of singing are excluded.\n# - Bursts. Spikes separated by 30 ms or less form a burst (a lone spike is a burst); burst time is\n#   the mean time of its spikes.\n# - Syllable locking (Methods, Syllable-related neural activity). Spikes aligned to syllable onset,\n#   rate histogram with 1 ms bins smoothed over 20 bins, range plus or minus 0.5 s; the peak\n#   between 50 ms before and 200 ms after onset; surrogates add a random shift, uniform over plus\n#   or minus 0.5 s, to each trial's spikes; 1,000 surrogates; P is the fraction of surrogate\n#   peaks larger than the real one; locked when P < 0.05. OPEN: (i) the smoothing kernel; a\n#   20-bin moving average is the plain reading and the standard choice, used throughout; (ii)\n#   whether shifted spikes wrap around the window; readings (a) circular shift within the\n#   window, (b) spikes taken from a wider window and shifted, then binned within plus or minus\n#   0.5 s; (iii) which syllables, in stages with several syllable types; readings (a) all\n#   selected syllables pooled, (b) each labelled type separately, locked when any type is\n#   significant (Bonferroni over types as a sub-variant).\n# - Rhythmic neurons (Methods, Quantification of the rhythmic neural activity). Four measures,\n#   each with its peak: inter-burst interval distribution, peak between 80 and 1,000 ms;\n#   spike-train autocorrelation as a conditional firing rate, peak between 80 and 1,000 ms;\n#   multitaper spectrum (Chronux, point process, non-overlapping 1.5 s windows of singing,\n#   NW = 3/2, K = 2 tapers, averaged over windows), peak in 2 to 15 Hz; cepstrum (inverse\n#   Fourier transform of the log spectrum), peak between 80 and 1,000 ms. Surrogates place the\n#   bout's bursts at random within an interval of the bout's duration, keeping their spikes and\n#   at least 30 ms between bursts; 1,000 surrogates for the IBI and autocorrelation, 100 for the\n#   spectrum and cepstrum; P is the fraction of surrogate peaks larger than the real one, and a\n#   peak is significant at P < 0.05 (Methods, Statistics). Rhythmic when at least two of the four\n#   are significant. Period is the lag of the largest autocorrelation peak between 80 and 1,000\n#   ms. OPEN: the bin widths of the IBI histogram and of the autocorrelation; readings (a) 1 ms\n#   bins smoothed over 20 bins, as for the paper's other spike histograms, (b) 10 ms bins; and\n#   which spectrum the cepstrum is taken from; readings (a) the neuron's mean multitaper\n#   spectrum, (b) the spectrum of each 1.5 s window, cepstra then averaged. Windows shorter than\n#   1.5 s at the end of a bout are dropped (standard choice).\n# - Shared and specific neurons (Methods, Shared and specific neurons). Per syllable type, spikes\n#   linearly time-warped to the type's mean duration and a syllable-aligned histogram (1 ms bins,\n#   smoothed over 20 bins); its peak between 30 ms before onset and 10 ms after offset; the peak\n#   tested as for syllable locking. Specific when significant for one of the pair's two types,\n#   shared when significant for both. The paper adjusted the interval by visual inspection where\n#   one burst would otherwise be detected for two adjacent syllables; this cannot be repeated\n#   exactly, and the author records each adjustment. OPEN: alignment to onset or offset; Fig. 3\n#   uses onsets and Fig. 4 offsets (\"Time from syllable offset\"), and the Methods allow both\n#   (\"syllable onset- or offset-aligned histograms\"); each pair uses the alignment its figure\n#   shows, the other as a variant.\n# - Statistics. All tests two-sided, P < 0.05 significant; Fisher's exact test replaces chi-square\n#   when an expected count is below 5 (Methods, Statistics). For the 2 x 2 shared/specific tests\n#   the printed P values (0.03 for bird 1, 5 x 10-4 for bird 2) are those of Pearson's\n#   chi-square without continuity correction on the counts the paper gives (0.031 and 0.0005;\n#   with Yates' correction 0.049 and 0.0012), so that variant is used.\nschema_version: 2\npaper: doi:10.1038/nature15741\nclaims:\n- id: counts-neurons-birds\n  statement: The data comprise 1,149 HVC projection neurons from 35 birds (juvenile and adult), of\n    which 211 are unidentified projection neurons (HVCp).\n  source: Results, Developmental progression of HVC activity, paragraph 1; Methods, Chronic neural\n    recordings, paragraph 2\n  quote: we recorded from populations of HVC projection neurons in juvenile and adult birds (n =\n    1,149 neurons, 35 birds; Extended Data Fig. 1a) ... These neurons were included in the data\n    set as unidentified HVC projection neurons (HVCp)\n  data: with_inputs\n  expected:\n  - quantity: neurons, all stages\n    value: 1149\n    tolerance: 114.9\n  - quantity: birds, all stages\n    value: 35\n    tolerance: 3.5\n  - quantity: unidentified projection neurons (HVCp)\n    value: 211\n    tolerance: 21.1\n  - quantity: juvenile neurons (1,149 less the 32 adult neurons of Fig. 1f)\n    value: 1117\n    tolerance: 111.7\n  criterion: Counts of neurons that pass the Methods' exclusions (active during singing, at least\n    5 s of singing). The juvenile counts (1,117 neurons, 32 birds; Results paragraph 4 and\n    Methods, Animals) are judged on the dataset; the adult part (3 birds, 32 neurons) is from\n    ref. 20 and is judged only if those recordings are found. The HVCp count is judged over the\n    juvenile neurons, with the reading that all 211 are juvenile and the reading that the 211\n    span all stages both shown.\n- id: ed1a-stage-age\n  statement: Song stage advances with age (Spearman's rho = 0.61 between age and stage); the\n    median ages are 48 dph for subsong, 58 for the protosyllable stage, 62 for the multi-syllable\n    stage and 73 for the motif stage.\n  source: Methods, Classification of song stages; Extended Data Fig. 1a\n  quote: Subsong stage (48 ± 4 dph, median ± inter-quartile range, IQR) ... protosyllable stage\n    (58 ± 10 dph, median ± IQR) ... multi-syllable stage (62 ± 12 dph, median ± IQR) ... The motif\n    stage (73 ± 21 dph, median ± IQR) ... Spearman’s rank correlation between age and stage ρ =\n    0.61\n  expected:\n  - quantity: Spearman rho, age against stage\n    value: 0.61\n    tolerance: 0.061\n  - quantity: median age, subsong stage\n    value: 48\n    tolerance: 4\n    unit: dph\n  - quantity: median age, protosyllable stage\n    value: 58\n    tolerance: 10\n    unit: dph\n  - quantity: median age, multi-syllable stage\n    value: 62\n    tolerance: 12\n    unit: dph\n  - quantity: median age, motif stage\n    value: 73\n    tolerance: 21\n    unit: dph\n  criterion: Tolerances for the ages are the reported IQRs. Stages coded 1 to 4 (subsong to\n    motif; the Spearman test is described for \"song stage and age\", Methods, Statistics). OPEN,\n    the unit of the median and of the correlation; readings (a) one value per recording day of\n    each bird (the Methods classify \"each day of juvenile singing\"), (b) one value per neuron,\n    (c) one value per bird and stage (Extended Data Fig. 1a gives n in birds and in neurons).\n    Reproduced when, under one reading, rho and all four medians are within tolerance.\n- id: fig1-subsong-locking\n  statement: In the subsong stage about half of the projection neurons (19 of 39) burst at a\n    particular latency relative to syllable onsets, the others not locked to onsets.\n  source: Results, Developmental progression of HVC activity, paragraph 1; Extended Data Fig. 1d-i\n  quote: roughly half the neurons generated bursts not temporally locked to syllable onsets\n    (Extended Data Fig. 1d), while the other half produced bursts that tended to occur at a\n    particular latency relative to subsong syllable onsets (Fig. 1a and Extended Data Fig. 1e–i;\n    19/39 neurons exhibited syllable locking)\n  expected:\n  - quantity: subsong-stage neurons\n    value: 39\n    tolerance: 3.9\n  - quantity: subsong-stage neurons locked to syllable onsets\n    value: 19\n    tolerance: 1.9\n  criterion: Locking as defined in the header (Methods, Syllable-related neural activity), over all\n    subsong syllables (subsong has no syllable types, so reading (iii) does not arise). Reproduced\n    when both counts are within tolerance under one reading of the shift.\n- id: fig1f-locking-increases\n  statement: The fraction of neurons locked to syllable onsets rises through development until\n    nearly every adult neuron is locked (correlation of locking with song stage r = 0.22, P <\n    10^-10).\n  source: Results, Developmental progression of HVC activity, paragraph 1; Figure 1f\n  quote: >-\n    The fraction of neurons locked to syllable onsets exhibited a gradual and significant increase\n    throughout vocal development (Fig. 1f; correlation with song stage: r = 0.22, P < 10−10; see\n    Methods) until, in adult birds, virtually every projection neuron generated bursts precisely\n    locked to syllables\n  statistics:\n  - about: locking (0 or 1 per neuron) against song stage (1 to 5)\n    test: Pearson's correlation\n    statistic: r = 0.22\n    p: 1.0e-10\n    p_relation: <\n    n: 1,149 neurons (39, 135, 565, 378 and 32 per stage)\n  - about: each stage against the adult stage; which stages carry the stars is not legible in the\n      extracted text\n    test: chi-square test followed by a post-hoc pairwise test\n    p: 0.001\n    p_relation: <\n  data: with_inputs\n  expected:\n  - quantity: Pearson r, locking against stage\n    value: 0.22\n    tolerance: 0.022\n  criterion: Locking per neuron as in the header; Pearson's r between the binary value and stage\n    coded 1 to 5 (Methods, Statistics, Figure 1f). Reproduced when r is within tolerance with P <\n    10^-10 and the adult fraction is the highest of the five. Without the adult neurons (ref. 20),\n    r over the four juvenile stages is reported and the claim is judged only on the rise across\n    them (partially reproduced at best). The post-hoc test is not named; chi-square on each\n    stage against adult with Bonferroni over four comparisons is the reading, and the stages\n    found significant are reported, not judged, as the figure was not read.\n- id: fig1f-rhythmic-protosyllable\n  statement: Few subsong-stage neurons burst rhythmically (3 of 39), while about half of\n    protosyllable-stage neurons do (70 of 135), with a period of 169 +/- 6.4 ms (mean +/- s.e.m.).\n  source: Results, Developmental progression of HVC activity, paragraph 2; Figure 1f\n  quote: In the subsong stage, most projection neurons did not burst rhythmically (Fig. 1a, f; 3/39\n    neurons were rhythmic). In the protosyllable stage, roughly half of the projection neurons\n    generated rhythmic bursts (5–10 Hz) (Fig. 1b, f; 70/135 neurons were rhythmic; period 169 ±\n    6.4 ms, mean ± s.e.m.)\n  expected:\n  - quantity: rhythmic neurons, subsong stage (of 39)\n    value: 3\n    tolerance: 0.3\n  - quantity: rhythmic neurons, protosyllable stage (of 135)\n    value: 70\n    tolerance: 7\n  - quantity: mean period, rhythmic protosyllable-stage neurons\n    value: 169\n    tolerance: 6.4\n    unit: ms\n  criterion: Rhythmicity and period as in the header. The period tolerance is the reported s.e.m.\n    The subsong count's 10% tolerance allows no difference; it is reproduced at 3, partially at\n    2 or 4. Reproduced when, under one reading of the open bin widths and cepstrum, all three\n    values are within tolerance.\n- id: fig1fg-rhythm-increases\n  statement: Both the fraction of rhythmic neurons and the period of the HVC burst rhythm increase\n    through development (correlation with song stage r = 0.28 and r = 0.57, both P < 10^-10).\n  source: Results, Developmental progression of HVC activity, paragraph 2; Figure 1f, g\n  quote: >-\n    On average, both the fraction of rhythmic HVC neurons and the period of the HVC burst rhythm\n    gradually increased during the emergence of new syllable types and the formation of the song\n    motif (Fig. 1f, g; correlation between song stage and fraction of rhythmic neurons: r = 0.28,\n    P < 10−10; correlation between song stage and period of burst rhythm: r = 0.57, P < 10−10)\n  statistics:\n  - about: rhythmic (0 or 1 per neuron) against song stage\n    test: Pearson's correlation\n    statistic: r = 0.28\n    p: 1.0e-10\n    p_relation: <\n    n: 1,149 neurons\n  - about: period of rhythmic neurons against song stage\n    test: Pearson's correlation\n    statistic: r = 0.57\n    p: 1.0e-10\n    p_relation: <\n    n: 752 rhythmic neurons (3, 70, 356, 298 and 25 per stage)\n  - about: period, each stage against adult; the stages carrying the stars in Fig. 1g are not\n      legible in the extracted text\n    test: Kruskal-Wallis test followed by a post-hoc pairwise test\n    p: 0.001\n    p_relation: <\n  data: with_inputs\n  expected:\n  - quantity: Pearson r, rhythmic against stage\n    value: 0.28\n    tolerance: 0.028\n  - quantity: Pearson r, period against stage\n    value: 0.57\n    tolerance: 0.057\n  - quantity: rhythmic neurons per stage (subsong, protosyllable, multi-syllable, motif)\n    value: 729\n    tolerance: 72.9\n  criterion: Rhythmicity and period as in the header; stage coded 1 to 5 (Methods, Statistics,\n    Figures 1f and 1g). The total of rhythmic juvenile neurons (3 + 70 + 356 + 298, from the Fig.\n    1g legend) is checked too. Reproduced when both r are within tolerance with P < 10^-10, under\n    one reading of the open details. Without the adult neurons, the juvenile-only correlations\n    are reported and the claim is judged on their sign and significance (partially reproduced at\n    best). The stages found to differ from adult are reported, not judged.\n- id: ed1c-burst-width-rate\n  statement: Burst width and firing rate within bursts change with developmental stage, some\n    juvenile stages differing from adults.\n  source: Extended Data Fig. 1c\n  quote: Burst width ... and firing rate during bursts (bottom) as a function of ... developmental\n    stage (median ± quartiles; n = 39, 135, 565, 378 and 32 neurons, respectively\n  statistics:\n  - test: Kruskal-Wallis test followed by a post-hoc pairwise test against the adult stage\n    p: 0.01\n    p_relation: <\n  data: with_inputs\n  criterion: Burst width is the interval from first to last spike of a burst, firing rate the\n    reciprocal of the mean ISI within it, single-spike bursts excluded (Methods, Definition of\n    bursts); singing spikes only. OPEN, the unit of the test; readings (a) one median per neuron,\n    (b) all bursts pooled. The direction and which stages differ are shown only in the figure,\n    which was not read; the Extended Data Fig. 2 legend says the activity of individual neurons\n    \"becomes sparser and more precise\", read as narrower bursts later. Reproduced when, with the\n    adult neurons, at least one juvenile stage differs from adult at P < 0.01 in each measure\n    (Kruskal-Wallis, then Dunn's test with Bonferroni over four comparisons as the standard\n    post-hoc); the medians per stage are reported. Not testable without the adult neurons.\n- id: fig1de-bout-related\n  statement: 285 of 1,117 juvenile projection neurons burst in relation to song bouts; 137 before\n    bout onset only, 98 after bout offset only and 50 both.\n  source: Results, Developmental progression of HVC activity, paragraph 3; Figure 1d, e; Extended\n    Data Fig. 2e-l\n  quote: A substantial fraction of projection neurons (285 of 1,117 neurons) in juvenile birds\n    generated bursts related to song bouts ... (‘bout-onset’ neurons; 137/285 neurons) or after\n    bout offset (98/285 neurons) ... an additional 50/285 neurons were active both before and after\n    bouts\n  expected:\n  - quantity: bout-related juvenile neurons\n    value: 285\n    tolerance: 28.5\n  - quantity: pre-bout only\n    value: 137\n    tolerance: 13.7\n  - quantity: post-bout only\n    value: 98\n    tolerance: 9.8\n  - quantity: both\n    value: 50\n    tolerance: 5\n  criterion: As the Methods give it (Bout-related neural activity). Pre-bout, the peak of the\n    bout-onset-aligned histogram in the 300 ms before onset is significant against shifted\n    surrogates (procedure of Syllable-related neural activity), unless the syllable-onset\n    histogram has a peak within 25 ms of the same latency; post-bout, a significant peak in the\n    300 ms after bout offset. Reproduced when all four counts are within tolerance under one\n    reading of the shift. The Extended Data Fig. 2h and 2l totals (187 and 149 neurons) are\n    reported; 137 + 50 = 187 but 98 + 50 = 148, a discrepancy of one neuron in the paper.\n- id: fig2b-protosequence\n  statement: In the protosyllable stage, different neurons recorded in the same bird burst at\n    different latencies relative to protosyllable onset, together covering the protosyllable and\n    the following gap (3 birds, 54 neurons; over 90% burst coverage).\n  source: Results, Growth of a neural protosequence, paragraph 1; Figure 2a, b; Extended Data\n    Figs 1n, 9k and 2t\n  quote: recordings in the same bird revealed that different neurons were active at different\n    times with respect to protosyllable onsets (Fig. 2a, b and Extended Data Figs 1n and 9k; n = 3\n    birds, 54 neurons), with latencies spanning the duration of the protosyllable and the\n    intervening gap (>90% burst coverage; Extended Data Fig. 2t)\n  expected:\n  - quantity: neurons in the three protosequence rasters (28 bird 2, 14 bird 1, 12 bird 4)\n    value: 54\n    tolerance: 5.4\n  criterion: The three birds are those of the rasters cited, bird 2 (Fig. 2b, 57 to 64 dph), bird 1\n    (Extended Data Fig. 1n, 56 to 59 dph) and bird 4 (Extended Data Fig. 9k, 48 to 49 dph,\n    protosyllables by phase segmentation). Neurons are those locked to protosyllable onsets\n    (header; protosyllables are syllables within two s.d. of the Gaussian fit to the residual of\n    the duration distribution after subtracting the exponential fit over 200 to 400 ms, Methods,\n    Syllable classification and labelling). Reproduced when, in each bird, the peak latencies of\n    the locked neurons span from before onset to past the protosyllable's mean offset, and the\n    protosyllable coverage (claim ed2st-coverage) exceeds 90% where computed.\n- id: ed2st-coverage\n  statement: Recorded bursts cover most of each juvenile syllable; 17 of 20 analysed syllables have\n    over 90% covered (one only 73%), and every syllable's coverage lies within the range expected\n    from random sampling of uniformly placed bursts.\n  source: Extended Data Fig. 2s, t; Methods, Analysis of coverage by HVC projection neuron bursts\n  quote: one syllable had coverage of only 73% (Extended Data Fig. 2t) ... Summary histogram of the\n    covered fraction for all analysed syllables (n = 20 syllables, 4 birds). Note that 17/20\n    syllables had a covered fraction higher than 90% ... Note that for all syllables, the observed\n    coverage is within the confidence interval for randomly shuffled bursts\n  expected:\n  - quantity: syllables with covered fraction above 90% (of 20)\n    value: 17\n    tolerance: 1.7\n  - quantity: lowest covered fraction\n    value: 73\n    tolerance: 7.3\n    unit: '%'\n  criterion: As the Methods give it. The 20 syllables are those with rasters in the main or\n    Extended Data figures that have more than 10 neurons bursting in the window from 30 ms before\n    onset to 10 ms after offset (bird 3 excluded). Per neuron, histogram of aligned spikes smoothed\n    with a 9 ms sliding window in 1 ms steps; candidate window where it exceeds 2 Hz\n    (protosyllable stage) or 10 Hz (older juveniles); kept when at least one spike falls in it on\n    at least 25% of renditions; each spike becomes a 5 ms pulse, and a time is covered where at\n    least three pulses overlap; neurons combined by OR; covered time over window length. 1,000\n    surrogates with each patch circularly shifted by a random offset; 2.5 to 97.5 percentiles.\n    OPEN, the list of 20 syllables, as the legends do not enumerate them; the author lists them\n    from the cited rasters. Reproduced when the count and lowest value are within tolerance and\n    every syllable lies within its surrogate interval.\n- id: ed2p-probabilistic\n  statement: Rhythmic protosyllable-stage neurons burst on only about half of the protosyllables\n    (mean 53%).\n  source: Extended Data Fig. 2p; Methods, Quantification of the probabilistic neural activity\n  quote: >-\n    we found that neurons in the protosyllable stage participated probabilistically (mean: 53% of\n    protosyllables\n  expected:\n  - quantity: mean fraction of protosyllables with at least one spike\n    value: 53\n    tolerance: 5.3\n    unit: '%'\n  - quantity: rhythmic protosyllable-stage neurons\n    value: 70\n    tolerance: 7\n  criterion: Over the rhythmic protosyllable-stage neurons (claim fig1f-rhythmic-protosyllable), the\n    fraction of protosyllables with at least one spike from 30 ms before onset to 10 ms after\n    offset. Reproduced when the mean is within tolerance.\n  depends_on:\n  - fig1f-rhythmic-protosyllable\n- id: ed2qr-pairs-independent\n  statement: Simultaneously recorded rhythmic pairs participate in largely independent sets of\n    protosyllables (median r^2 = 0.072, median mutual information 0.056 bits, 11 pairs).\n  source: Methods, Analysis of simultaneously recorded pairs of neurons; Extended Data Fig. 2q, r\n  quote: The distribution of coefficient of determination is shown in Extended Data Fig. 2q (median\n    r2 = 0.072, 11 pairs) ... (Extended Data Fig. 2r, median mutual information = 0.056 bits, 11\n    pairs). Both the correlation and mutual information were extremely low, suggesting that\n    different projection neurons participated on relatively independent sets of protosyllables\n  expected:\n  - quantity: rhythmic simultaneously recorded pairs (3 birds)\n    value: 11\n    tolerance: 1.1\n  - quantity: median r squared\n    value: 0.072\n    tolerance: 0.0072\n  - quantity: median mutual information\n    value: 0.056\n    tolerance: 0.0056\n    unit: bits\n  criterion: As the Methods give it. Per protosyllable, 1 when the neuron spikes from 30 ms before\n    onset to 10 ms after offset; r squared of the two binary strings; mutual information from the\n    2 x 2 joint distribution, in bits (log base 2, as \"bits\" implies). Pairs both rhythmic, in the\n    protosyllable stage. Reproduced when the pair count and both medians are within tolerance.\n  depends_on:\n  - fig1f-rhythmic-protosyllable\n- id: fig2c-latency-subsong-earlier\n  statement: Burst latencies relative to syllable onset are earlier and narrower in subsong than in\n    the protosyllable stage (63% against 43% before onset; P = 0.02).\n  source: Results, Growth of a neural protosequence, paragraph 2; Figure 2c\n  quote: In the subsong stage (Fig. 2c; n = 19 neurons, 12 birds), bursts had a significantly\n    earlier distribution of latencies compared to the broader distribution of burst latencies in\n    the protosyllable stage (n = 104 neurons, 13 birds; P = 0.02; 63% versus 43% of bursts before\n    syllable onset in the subsong stage and protosyllable stage, respectively)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.02\n    n: 19 subsong and 104 protosyllable-stage neurons\n  expected:\n  - quantity: subsong neurons with latencies (locked)\n    value: 19\n    tolerance: 1.9\n  - quantity: protosyllable-stage neurons with latencies (locked)\n    value: 104\n    tolerance: 10.4\n  - quantity: fraction before onset, subsong\n    value: 63\n    tolerance: 6.3\n    unit: '%'\n  - quantity: fraction before onset, protosyllable stage\n    value: 43\n    tolerance: 4.3\n    unit: '%'\n  criterion: Neurons locked to syllable onsets in each stage (header). OPEN, the latency unit;\n    readings (a) one latency per neuron, the time of its histogram peak (the n are neurons, and\n    12/19 = 63% and 45/104 = 43% fit whole neurons), (b) all burst times of these neurons within\n    the histogram window, pooled. Rank-sum test on the two samples (Methods, Statistics, Figure\n    2c). Reproduced when, under one reading, P < 0.05 with the subsong median earlier and both\n    percentages within tolerance.\n  depends_on:\n  - fig1-subsong-locking\n- id: fig2c-latency-broadens-later\n  statement: Over development, burst latencies spread more uniformly through the syllable, with\n    the multi-syllable and motif stages broader than the protosyllable stage.\n  source: Figure 2c (bottom); Extended Data Fig. 2 legend, Regarding two models of HVC coding\n  quote: During development, HVC activity appears to evolve such that, as a population, bursts\n    occur more uniformly throughout song syllables (Fig. 2c)\n  expected:\n  - quantity: neurons with latencies, multi-syllable and motif stages\n    value: 814\n    tolerance: 81.4\n  criterion: Latencies as in fig2c-latency-subsong-earlier (same reading), for the multi-syllable\n    and motif stages pooled. The paper reports no test or measure of spread. Spread is measured\n    by the interquartile range of latencies, and by the fraction before onset (the measure the\n    Results use for Fig. 2c). Reproduced when the multi-syllable/motif IQR exceeds the\n    protosyllable IQR and its fraction before onset is lower; the rank-sum test of the two\n    stages is reported.\n  depends_on:\n  - fig2c-latency-subsong-earlier\n- id: bird1-protosequence\n  statement: In bird 1's protosyllable stage (56 to 59 dph), most projection neurons (14 of 16)\n    take part in a rhythmic protosequence.\n  source: Results, Sequence splitting during syllable formation, paragraph 2; Extended Data Fig. 1n\n  quote: During the protosyllable stage (56–59 days post-hatch, dph), the majority of projection\n    neurons participated in a rhythmic protosequence (Extended Data Fig. 1n; n = 14/16 neurons\n  expected:\n  - quantity: bird 1 protosyllable-stage neurons\n    value: 16\n    tolerance: 1.6\n  - quantity: neurons in the protosequence\n    value: 14\n    tolerance: 1.4\n  criterion: OPEN, what \"participated in a rhythmic protosequence\" counts; readings (a) locked to\n    protosyllable onsets (header; Extended Data Fig. 1n is a raster of the 14 aligned to\n    protosyllable onsets), (b) rhythmic (header), (c) both. Reproduced when both counts are\n    within tolerance under one reading.\n- id: fig3g-bird1-shared-specific\n  statement: After syllables beta and gamma emerge in bird 1 (62 to 72 dph), of 105 neurons active\n    in either, 41 are beta-specific, 42 gamma-specific and 22 shared.\n  source: Results, Sequence splitting during syllable formation, paragraphs 2 and 3; Figure 3d-g\n  quote: After the emergence of syllable types β and γ (62–72 dph), many neurons were selectively\n    active only during β or during γ, but not both (Fig. 3d, f; of 105 neurons active during either\n    β or γ, 41 were β -specific and 42 were γ -specific) ... (n = 22 ‘shared’ neurons; Fig. 3e–g)\n  expected:\n  - quantity: neurons active in beta or gamma, 62 to 72 dph\n    value: 105\n    tolerance: 10.5\n  - quantity: beta-specific\n    value: 41\n    tolerance: 4.1\n  - quantity: gamma-specific\n    value: 42\n    tolerance: 4.2\n  - quantity: shared\n    value: 22\n    tolerance: 2.2\n  criterion: Shared and specific as in the header, onset-aligned (Fig. 3g), on bird 1 (to3965)\n    neurons recorded 62 to 72 dph, syllables labelled beta and gamma in the dataset. Reproduced\n    when all four counts are within tolerance.\n- id: ed4a-shared-latency-bird1\n  statement: In bird 1, each shared neuron bursts at a similar latency in beta and in gamma (r =\n    0.91 early, 0.87 late).\n  source: Results, Sequence splitting during syllable formation, paragraph 4; Extended Data Fig. 4a\n  quote: for a given shared neuron, the bursts during β occurred at a similar latency as the bursts\n    during γ ... Note strong correlation of burst latencies (early, r = 0.91, P < 0.001; late, r =\n    0.87, P = 0.005)\n  statistics:\n  - about: early (62 to 72 dph)\n    test: Pearson's correlation\n    statistic: r = 0.91\n    p: 0.001\n    p_relation: <\n  - about: late (81 to 112 dph)\n    test: Pearson's correlation\n    statistic: r = 0.87\n    p: 0.005\n  expected:\n  - quantity: r, early\n    value: 0.91\n    tolerance: 0.091\n  - quantity: r, late\n    value: 0.87\n    tolerance: 0.087\n  criterion: Per shared neuron, the latency of the peak of each type's time-warped, onset-aligned\n    histogram; Pearson's r across shared neurons, P under r = 0 (Methods, Quantification of the\n    similarity of latencies). Reproduced when both r are within tolerance and P < 0.05.\n  depends_on:\n  - fig3g-bird1-shared-specific\n  - fig3h-bird1-shared-decrease\n- id: ed3j-shared-ibi-specific-doubled\n  statement: In bird 1, shared neurons keep the inter-burst interval of protosyllable-stage\n    neurons, while syllable-specific neurons have an interval twice as long.\n  source: Results, Sequence splitting during syllable formation, paragraphs 4 and 5; Extended Data\n    Fig. 3f-j\n  quote: syllable-specific neurons had an inter-burst interval, and thus a period, that was twice as\n    long as that observed in the earlier protosyllable stage ... Note that shared neurons had the\n    same ‘most-probable IBI’ as neurons recorded during the protosyllable stage\n  expected:\n  - quantity: protosyllable-stage neurons with an IBI (bird 1)\n    value: 9\n    tolerance: 0.9\n  - quantity: ratio of specific to protosyllable-stage median most-probable IBI\n    value: 2\n    tolerance: 0.2\n  - quantity: ratio of shared to protosyllable-stage median most-probable IBI\n    value: 1\n    tolerance: 0.1\n  criterion: Most-probable IBI per neuron is the mode of its inter-burst interval distribution\n    during singing (Extended Data Fig. 3f-i). OPEN, the histogram bins and range; readings (a)\n    the IBI peak between 80 and 1,000 ms with 1 ms bins smoothed over 20 bins (as for the IBI\n    measure of rhythmicity), (b) 10 ms bins. Groups of bird 1, protosyllable stage (n = 9),\n    shared (22) and specific (83) neurons of 62 to 72 dph. No test is reported; reproduced when\n    both ratios of group medians are within tolerance under one reading. Rank-sum tests between\n    groups are reported.\n  depends_on:\n  - fig3g-bird1-shared-specific\n- id: fig3h-bird1-shared-decrease\n  statement: In bird 1 the fraction of shared neurons is lower late in development (81 to 112 dph;\n    10 shared and 90 specific) than early (P = 0.03).\n  source: Results, Sequence splitting during syllable formation, paragraph 4; Figure 3h\n  quote: We also found that the fraction of shared neurons later in development (81–112 dph) was\n    significantly lower compared to the earlier recordings (Fig. 3h; 10 shared and 90 specific\n    neurons; P = 0.03)\n  statistics:\n  - test: chi-square test, 2 x 2 (shared or specific, early or late)\n    p: 0.03\n    n: 105 early and 100 late neurons\n  expected:\n  - quantity: late shared neurons\n    value: 10\n    tolerance: 1\n  - quantity: late specific neurons (B or C)\n    value: 90\n    tolerance: 9\n  criterion: Shared and specific as in the header for bird 1's beta/gamma (late, B/C) pair, 81 to\n    112 dph. Chi-square without continuity correction (header, Statistics) against the early\n    counts found in fig3g-bird1-shared-specific. Reproduced when the late counts are within\n    tolerance and the late shared fraction is lower with P < 0.05; partially reproduced when lower\n    but P is 0.05 or more.\n  depends_on:\n  - fig3g-bird1-shared-specific\n- id: all-birds-shared-specific\n  statement: Shared and specific neurons are found in all 6 birds recorded during the emergence of\n    several syllable types (185 shared and 496 specific neurons over 8 syllable pairs).\n  source: Results, Sequence splitting during syllable formation, paragraph 6\n  quote: a similar pattern of HVC coding by shared and specific neurons was seen in a total of 6\n    birds for which recordings were made during the emergence of multiple syllable types (birds\n    1–6; 185 shared neurons and 496 specific neurons for 8 syllable pairs analysed)\n  expected:\n  - quantity: shared neurons, 8 pairs\n    value: 185\n    tolerance: 18.5\n  - quantity: specific neurons, 8 pairs\n    value: 496\n    tolerance: 49.6\n  criterion: Shared and specific as in the header. OPEN, the 8 pairs, which the paper does not\n    list; the pairs it names are bird 1 beta/gamma (Fig. 3) and B/D (Extended Data Fig. 7), bird\n    2 alpha/beta (Fig. 4), bird 3 (Extended Data Fig. 8, pairs among its five syllables), bird 4\n    b/d and c/d (Extended Data Fig. 9l-o), bird 5 bout-onset differentiation and bird 6\n    hierarchical differentiation (Extended Data Fig. 7 legend, data not shown). The author takes\n    the dataset's labels for birds 3, 5 and 6 and records the pairs chosen. OPEN, whether counts\n    are over early and late recordings together; readings (a) all ages of each pair, (b) the\n    early period only. Reproduced when, under one reading, each of the 6 birds has at least one\n    shared and one specific neuron and both totals are within tolerance; partially reproduced\n    when every bird has both but a total is outside tolerance.\n- id: all-birds-shared-decrease\n  statement: Across the three birds also recorded later in development (birds 1, 2 and 4; 5\n    syllable pairs), the fraction of shared neurons decreases during syllable development (P = 3\n    x 10^-6).\n  source: Results, Sequence splitting during syllable formation, paragraph 6; Methods, Statistics,\n    Figures 3g, h and 4h, i\n  quote: Across three birds in which neurons were also recorded in later song stages, there was a\n    significant decrease in the fraction of shared neurons during syllable development (n = 5\n    syllable pairs; P = 3 × 10−6; birds 1, 2 and 4)\n  statistics:\n  - test: Cochran-Mantel-Haenszel test\n    p: 3.0e-6\n    n: 5 syllable pairs in 3 birds\n  criterion: Per pair a 2 x 2 table (shared or specific, early or late) and the\n    Cochran-Mantel-Haenszel test across the five (Methods, Statistics). The pairs read from the\n    figures are bird 1 beta/gamma (early 62 to 72, late 81 to 112 dph) and B/D (Extended Data\n    Fig. 7e, f), bird 2 alpha/beta (early 65 to 72, late 73 to 84 dph), bird 4 b/d and c/d\n    (Extended Data Fig. 9l-o). OPEN, the early/late boundary for bird 1 B/D and bird 4's pairs,\n    not given; the author places it between the ages of the \"early\" and \"late\" rasters and\n    records it. OPEN, continuity correction in the CMH statistic; readings with and without.\n    Reproduced when P < 0.05 under one reading, with the pooled shared fraction lower late; the\n    P value is reported against 3 x 10^-6.\n  depends_on:\n  - fig3h-bird1-shared-decrease\n  - fig4i-bird2-shared-decrease\n- id: skipping-cycles\n  statement: Neurons whose burst period is lengthened by skipping cycles of the underlying rhythm\n    are found in 4 of the 6 birds (birds 1, 3, 4 and 6).\n  source: Results, Sequence splitting during syllable formation, paragraph 6; Extended Data Fig. 3j\n    legend\n  quote: Neurons exhibiting an increased burst period by skipping cycles of an underlying rhythm\n    were observed in 4 of the 6 birds (birds 1, 3, 4 and 6)\n  criterion: The paper gives no rule for skipping cycles; its examples are bird 1's specific\n    neurons, which burst on alternate cycles of the protosyllable rhythm, and bird 4's neuron\n    bursting on alternate cycles of the 10 Hz rhythm (Extended Data Fig. 9f). Reading (a) a\n    rhythmic neuron (header) whose period is within 20% of twice the median period of the same\n    bird's protosyllable-stage rhythmic neurons (or, failing those, of its shared neurons); (b) a\n    rhythmic neuron whose IBI distribution has its largest peak at about twice the bird's\n    protosyllable period with a smaller peak at the period itself. Reproduced when such neurons are\n    found in all of birds 1, 3, 4 and 6 under one reading; partially reproduced for two or three\n    of them. Birds 2 and 5 are reported as well.\n- id: fig4-bird2-before-beta\n  statement: In bird 2 (125 neurons), before syllable beta emerges (57 to 64 dph), most neurons (28\n    of 35) take part in a rhythmic protosequence and a different 4 of 35 burst at bout onsets.\n  source: Results, Splitting in other learning strategies, paragraph 3; Figure 2b, Figure 4c\n  quote: we analysed the firing patterns of 125 HVC projection neurons. Before the emergence of\n    syllable β, the majority of recorded projection neurons participated in a rhythmic\n    protosequence (Fig. 2b; n = 28/35 neurons; 57–64 dph). A different subset of neurons was active\n    at bout onsets (Fig. 4c; 4 of 35 neurons)\n  expected:\n  - quantity: bird 2 neurons\n    value: 125\n    tolerance: 12.5\n  - quantity: neurons 57 to 64 dph\n    value: 35\n    tolerance: 3.5\n  - quantity: protosequence neurons\n    value: 28\n    tolerance: 2.8\n  - quantity: bout-onset neurons\n    value: 4\n    tolerance: 0.4\n  criterion: Bird 2 is to3779. Protosequence participation read as in bird1-protosequence (same\n    three readings); bout-onset activity as in fig1de-bout-related (pre-bout). Reproduced when all\n    counts are within tolerance under one reading; the bout-onset count of 4 allows no\n    difference, and 3 or 5 is partially reproduced.\n  depends_on:\n  - bird1-protosequence\n- id: fig4h-bird2-shared-early\n  statement: After syllable beta emerges at bout onset in bird 2 (65 to 72 dph), about half the\n    neurons are shared between alpha and beta (22 shared, 21 specific), and shared neurons produce\n    nearly identical sequences in the two syllables (r > 0.99).\n  source: Results, Splitting in other learning strategies, paragraph 3; Figure 4d, e, h; Extended\n    Data Fig. 4c\n  quote: After the reliable emergence of β at bout onsets, roughly half ... of projection neurons\n    generated bursts during both syllables α and β (65–72 dph; Fig. 4d, e; n = 22 ‘shared’ neurons;\n    21 ‘specific’ neurons). These shared neurons produced nearly identical sequences during these\n    two syllables (Fig. 4h, Extended Data Fig. 4c)\n  statistics:\n  - about: latencies of shared neurons in alpha and beta, early\n    test: Pearson's correlation\n    statistic: r > 0.99\n    p: 0.001\n    p_relation: <\n  expected:\n  - quantity: shared neurons, 65 to 72 dph\n    value: 22\n    tolerance: 2.2\n  - quantity: specific neurons, 65 to 72 dph\n    value: 21\n    tolerance: 2.1\n  criterion: Shared and specific as in the header, aligned to syllable offset as Fig. 4h shows\n    (onset as a variant). Latency correlation as in ed4a-shared-latency-bird1, leaving out the\n    neuron with two peaks in alpha (Extended Data Fig. 4c legend), identified as the shared neuron\n    whose alpha histogram has two significant peaks. Reproduced when both counts are within\n    tolerance and r is above 0.95 (the reported bound less a 10% tolerance on 1 - r, read\n    generously as 0.95) with P < 0.05.\n- id: fig4i-bird2-shared-decrease\n  statement: Later in bird 2's development (73 to 84 dph) shared neurons are fewer (4 shared, 28\n    specific; P = 5 x 10^-4).\n  source: Results, Splitting in other learning strategies, paragraph 3; Figure 4f, g, i\n  quote: Later in song development (73–84 dph), we observed a smaller fraction of shared neurons (n\n    = 4 ‘shared’ neurons; P = 5 × 10−4), and a correspondingly larger fraction of\n    syllable-specific neurons (Fig. 4f, g, i; n = 28 ‘specific’ neurons)\n  statistics:\n  - test: chi-square test, 2 x 2 (shared or specific, early or late)\n    p: 5.0e-4\n    n: 43 early and 32 late neurons\n  expected:\n  - quantity: late shared neurons\n    value: 4\n    tolerance: 0.4\n  - quantity: late specific neurons\n    value: 28\n    tolerance: 2.8\n  criterion: As fig4h-bird2-shared-early, 73 to 84 dph. Chi-square without continuity correction\n    (header, Statistics; no expected count is below 5 at the reported counts) against the early\n    counts. Reproduced when the shared count is 4 (3 or 5 partially), the specific count within\n    tolerance, and P < 0.05 with the late fraction lower.\n  depends_on:\n  - fig4h-bird2-shared-early\n- id: ed4bd-shared-latency-other\n  statement: Shared neurons burst at similar latencies in both syllables of the other pairs as\n    well; bird 1 D/B and bird 2 alpha/beta both stages r > 0.99, bird 4 b2/d1 r = 0.89 and c/d2 r =\n    0.98.\n  source: Extended Data Fig. 4b-d\n  quote: b, Neurons in bird 1 shared between syllables D and B (Extended Data Fig. 7) during the\n    early and late stages of syllable differentiation (top, early r > 0.99, P < 0.001; bottom, late\n    r > 0.99, P < 0.001). c, Neurons in bird 2 shared between syllables β and α (Fig. 4h) during the\n    early and late stages (top, early r > 0.99, P < 0.001; bottom, late r > 0.99, P < 0.001) ...\n    Data Fig. 9l) during early stage (top, r = 0.89, P < 0.001 ... Data Fig. 9n) during early stage\n    (bottom, r = 0.98, P < 0.001)\n  statistics:\n  - about: bird 1 D/B, early and late\n    test: Pearson's correlation\n    statistic: r > 0.99\n    p: 0.001\n    p_relation: <\n  - about: bird 2 alpha/beta, early and late\n    test: Pearson's correlation\n    statistic: r > 0.99\n    p: 0.001\n    p_relation: <\n  - about: bird 4 b2/d1, early\n    test: Pearson's correlation\n    statistic: r = 0.89\n    p: 0.001\n    p_relation: <\n  - about: bird 4 c/d2, early\n    test: Pearson's correlation\n    statistic: r = 0.98\n    p: 0.001\n    p_relation: <\n  expected:\n  - quantity: r, bird 4 b2/d1\n    value: 0.89\n    tolerance: 0.089\n  - quantity: r, bird 4 c/d2\n    value: 0.98\n    tolerance: 0.098\n  criterion: As ed4a-shared-latency-bird1. For bird 4, neurons bursting in b1 are left out of the\n    b2/d1 correlation (legend); b1/b2 and d1/d2 are the first and second halves of b and d\n    (Extended Data Fig. 9g, h). For the r > 0.99 bounds, reproduced at r above 0.95 (as in\n    fig4h-bird2-shared-early). Reproduced when every correlation meets its value and P < 0.05;\n    partially reproduced when all are positive and significant but some miss their value.\n  depends_on:\n  - fig4h-bird2-shared-early\n- id: ed7-bird1-bd-shared-persist\n  statement: In bird 1 a large fraction of neurons shared between B and D remains in the later\n    recordings, larger than the fraction shared between B and C at late stages.\n  source: Extended Data Fig. 7e, f\n  quote: Of particular note in this bird is the large fraction of shared neurons between B and D\n    that remained in the later recordings (panel f), compared to the smaller fraction of shared\n    neurons at late stages in syllables B and C of the same bird (Fig. 3h)\n  expected:\n  - quantity: neurons in the early B/D raster\n    value: 60\n    tolerance: 6\n  - quantity: neurons in the late B/D raster\n    value: 70\n    tolerance: 7\n  criterion: Shared and specific as in the header, for B and D (D is the first beta of a bout,\n    B later ones, Methods, Syllable classification and labelling). The paper gives no test;\n    reproduced when the late B/D shared fraction exceeds the late B/C fraction (10 of 100) and a\n    chi-square test of the two (as in Methods, Statistics, Figures 3g, h) gives P < 0.05;\n    partially reproduced when higher but not significant.\n  depends_on:\n  - fig3h-bird1-shared-decrease\n- id: ed8-bird3-phase\n  statement: In bird 3 (motif strategy) shared neurons burst at similar phases of the song rhythm\n    in their two syllables (mean absolute phase difference 41 +/- 33.9 degrees, 8 neurons;\n    smaller than shuffled, P = 0.013).\n  source: Extended Data Fig. 8i, j; Methods, Quantification of the similarity of latencies,\n    paragraph 2\n  quote: >-\n    i, Histogram of the absolute phase difference between the two syllables for all shared neurons\n    (n = 8 neurons; mean phase difference: 41 ± 33.9 deg, mean ± s.d.). j, Cumulative distribution\n    of the mean absolute phase difference after randomizing burst identity (red dotted line\n    indicates P = 0.05 threshold for significance; red triangle indicates observed mean absolute\n    phase difference, P = 0.013)\n  statistics:\n  - test: shuffle test, phase pairings randomized across shared neurons, 1,000 shuffles\n    p: 0.013\n    n: 8 shared neurons\n  expected:\n  - quantity: shared neurons, bird 3\n    value: 8\n    tolerance: 0.8\n  - quantity: mean absolute phase difference\n    value: 41\n    tolerance: 33.9\n    unit: degrees\n  criterion: As the Methods give it. Phase from the sound amplitude band-passed by a second-order\n    IIR resonator at 9 Hz with 3 dB half-bandwidth 3 Hz (MATLAB iirpeak) and the Hilbert\n    transform; each burst gets the instantaneous phase at its time; per neuron and syllable the\n    mean phase (circular mean, the standard choice for phases); for each shared neuron the two\n    syllables it bursts on most reliably; the absolute difference wrapped to 0 to 180 degrees.\n    OPEN, the sound-amplitude envelope (sampling and smoothing), not given; the author uses a\n    standard choice and states it. Reproduced when the mean is within tolerance and P < 0.05.\n    Tolerance is the reported s.d.\n- id: motif-strategy-shared\n  statement: In the two motif-strategy birds (3 and 4), protosyllable-stage neurons burst\n    rhythmically, and after the syllables emerge every syllable of the motif has at least one\n    neuron shared with another syllable at a similar latency.\n  source: Results, Splitting in other learning strategies, paragraph 5; Extended Data Figs 8 and 9\n  quote: In both birds, neural recordings showed the existence of rhythmically bursting neurons in\n    the protosyllable stage (Extended Data Figs 8e and 9e, f). After the emergence of multiple\n    syllable types, every syllable in the emerging motif had at least one neuron that was shared\n    with another syllable at similar latencies (Extended Data Figs 8f–j and 9g–o)\n  criterion: Rhythmicity and shared neurons as in the header, for bird 3 (to3017; syllables A to E\n    by phase segmentation, Extended Data Fig. 8) and bird 4 (to5640; syllables a to f, with b and\n    d in halves, Extended Data Fig. 9). Similar latency is judged as the paper does, on the\n    population, by ed8-bird3-phase for bird 3 and ed4bd-shared-latency-other for bird 4.\n    Reproduced when each bird has at least one rhythmic protosyllable-stage neuron and every\n    syllable has at least one shared neuron; partially reproduced when one syllable lacks one.\n  depends_on:\n  - ed8-bird3-phase\n  - ed4bd-shared-latency-other\n- id: ed9-bird4-rhythms\n  statement: In bird 4's protosyllable stage, 11 of 18 neurons are rhythmic; 5 of these burst at 10\n    Hz and 6 at 5 Hz, on alternate cycles of the 10 Hz rhythm.\n  source: Extended Data Fig. 9 legend, Neural evidence for hypothesized mechanism of motif\n    construction\n  quote: (panels e and f; 11/18 neurons were rhythmic, 5/11 rhythmic neurons exhibited periodicity\n    at 10 Hz) ... many neurons recorded at an early stage (< 50 dph) exhibited a prominent 5 Hz\n    periodicity in their rhythmic bursting, (panels f and h; 6/11 rhythmic neurons)\n  expected:\n  - quantity: protosyllable-stage neurons, bird 4\n    value: 18\n    tolerance: 1.8\n  - quantity: rhythmic\n    value: 11\n    tolerance: 1.1\n  - quantity: rhythmic at 10 Hz\n    value: 5\n    tolerance: 0.5\n  - quantity: rhythmic at 5 Hz\n    value: 6\n    tolerance: 0.6\n  criterion: Rhythmicity as in the header. OPEN, how a neuron is assigned 10 or 5 Hz; readings (a)\n    the period (autocorrelation peak) nearer 100 ms or 200 ms, (b) the spectral peak in 2 to 15\n    Hz nearer 10 Hz or 5 Hz. Reproduced when all counts match within tolerance under one reading\n    (the 5 and 6 allow no difference; one off is partially reproduced).\n- id: ed4j-bias\n  statement: Specific neurons have a bias near one (0.96 +/- 0.011), while shared neurons have a\n    broad range of bias (0.28 +/- 0.22).\n  source: Extended Data Fig. 4i, j; Methods, Quantification of the activity level difference in\n    shared neurons\n  quote: Specific neurons exhibited a bias tightly clustered around one (0.96 ± 0.011, mean ± s.d.).\n    In contrast, shared neurons exhibited a broad range of bias (0.28 ± 0.22)\n  expected:\n  - quantity: mean bias, specific neurons\n    value: 0.96\n    tolerance: 0.011\n  - quantity: mean bias, shared neurons\n    value: 0.28\n    tolerance: 0.22\n  criterion: Bias = 1 - min(r1, r2) / max(r1, r2), r the peak rate of each type's syllable-aligned\n    histogram (Methods; the formula is read from the garbled extraction and matches the stated 0\n    for equal and 1 for exclusive activity). OPEN, which neurons; readings (a) all shared and\n    specific neurons of the 8 pairs, (b) bird 1 beta/gamma and bird 2 alpha/beta, the pairs\n    whose examples the panels show. OPEN, where the peak rate of the non-significant type is\n    taken; reading, the maximum in the same window as for the significance test. Tolerances\n    are the reported s.d. Reproduced when both means are within tolerance under one reading.\n  depends_on:\n  - all-birds-shared-specific\n- id: ed5-shared-acoustic-difference\n  statement: Shared neurons burst at times when the two emerging syllables differ significantly in\n    their acoustics (11 HVCRA and 36 HVCX shared neurons with a significant difference), with no\n    difference in its size between cell types (P = 0.1).\n  source: Results, Sequence splitting during syllable formation, paragraph 4; Extended Data Fig. 5;\n    Methods, Analysis of acoustic features associated with bursts of shared neurons\n  quote: This shared sequence occurred even at times when there was a significant acoustic\n    difference between the shared syllables (Extended Data Fig. 5) ... (9 of 24 HVCRA neurons and\n    59 of ... 120 HVCX neurons were obscured) ... n, Cumulative distribution of mean d′ for shared\n    HVCRA neurons (green; n = 11) and shared HVCX neurons (blue; n = 36). Only neurons with\n    significant d′ metric are included in the cumulative. No significant difference was observed\n    between neuron types (P = 0.1)\n  statistics:\n  - about: mean d' in 10 to 40 ms, HVCRA against HVCX, significant neurons only\n    test: Wilcoxon rank-sum test\n    p: 0.1\n    n: 11 HVCRA and 36 HVCX shared neurons\n  expected:\n  - quantity: HVCRA shared neurons with a significant acoustic difference (of 15 analysed)\n    value: 11\n    tolerance: 1.1\n  - quantity: HVCX shared neurons with a significant acoustic difference (of 61 analysed)\n    value: 36\n    tolerance: 3.6\n  criterion: As the Methods give it. Shared neurons of all pairs; those whose 10 to 40 ms window\n    after the burst falls in a silent gap excluded (24 - 9 = 15 HVCRA and 120 - 59 = 61 HVCX\n    analysed, by subtraction). Per rendition with a burst, 8 features (Wiener entropy, spectral\n    centre of gravity, spectral width, pitch, pitch goodness, amplitude, amplitude modulation,\n    frequency modulation) in 1 ms steps over 0 to 50 ms after burst time; at each step Fisher's\n    discriminant projection and d' = (muA - muB) / sqrt((sigmaA^2 + sigmaB^2) / 2) (read from\n    the garbled formula); 1,000 label shuffles, threshold the 95th percentile of shuffled peak d'\n    in 10 to 40 ms; significant when d' stays above it throughout 10 to 40 ms. OPEN, the feature\n    implementation (refs 51, 55: Sound Analysis Pro); the author uses an implementation of the\n    SAP features and states its parameters. OPEN, the burst used when a neuron bursts more than\n    once in a syllable; reading, the burst nearest the histogram peak latency. Reproduced when\n    both counts are within tolerance and the rank-sum test finds no difference at P < 0.05 (the\n    paper's test, judged as a claim of absence).\n  depends_on:\n  - all-birds-shared-specific\n- id: ed5-shared-ra-x-proportion\n  statement: Shared neurons are found in similar proportions among HVCRA and HVCX neurons (19% and\n    28%; P = 0.08).\n  source: Extended Data Fig. 5 legend, Summary of properties of HVCRA and HVCX shared neurons\n  quote: Shared neurons were found in similar proportion across both HVCRA and HVCX neurons (19% and\n    28%, respectively; P = 0.08; averaged over all developmental stages)\n  statistics:\n  - test: not named; chi-square test by the Methods' Statistics section\n    p: 0.08\n  expected:\n  - quantity: shared fraction, HVCRA\n    value: 19\n    tolerance: 1.9\n    unit: '%'\n  - quantity: shared fraction, HVCX\n    value: 28\n    tolerance: 2.8\n    unit: '%'\n  criterion: A claim of absence. OPEN, the denominator; readings (a) the shared and specific neurons\n    of the 8 pairs, by cell type (24 HVCRA and 120 HVCX shared neurons, Methods, acoustic\n    analysis), (b) all juvenile neurons of the cell type in birds 1 to 6. Chi-square 2 x 2 (cell\n    type, shared or not) without continuity correction (header). Reproduced when the test finds\n    no difference at P < 0.05; the fractions are reported against 19% and 28% under each reading.\n  depends_on:\n  - all-birds-shared-specific\n- id: ed2mo-ra-x-similar\n  statement: HVCRA and HVCX neurons develop alike; of 14 comparisons of locking, rhythmicity and\n    period across stages, only the motif-stage period differs between cell types.\n  source: Extended Data Fig. 2m-o\n  quote: Of the 14 comparisons between HVCRA and HVCX neurons shown in panels m–o, only the period of\n    HVC rhythm (panel o) during the motif stage showed significant difference between the cell\n    types (P < 0.05 with Bonferroni correction)\n  statistics:\n  - about: motif-stage period, HVCRA against HVCX\n    test: chi-square test (Methods, Statistics, Extended Data Fig. 2m-o)\n    p: 0.05\n    p_relation: <\n    corrected: Bonferroni\n  data: with_inputs\n  criterion: Locking, rhythmicity and period as in the header, per stage (subsong to adult) and cell\n    type (HVCp left out); 14 comparisons (no HVCRA period in subsong). The Methods name the\n    chi-square test for all three panels, which fits the fractions; for the period, readings (a)\n    rank-sum test, as periods are continuous, (b) chi-square on periods binned at the median of\n    the stage. Bonferroni over 14. Reproduced when the motif-stage period differs and no other\n    comparison does; partially reproduced when the motif-stage period differs and one other does.\n    Without adult neurons, 12 comparisons are made.\n- id: model-fig5a-subsong-decay\n  statement: In the model before learning, activating the seed neurons produces a briefly\n    propagating sequence of activity that decays within tens of milliseconds.\n  source: Results, Mechanistic model and discussion, paragraph 3; Figure 5a\n  quote: Before learning, activation of these seed neurons produced a transiently propagating\n    sequence of network activity that decayed rapidly (within tens of milliseconds; Fig. 5a)\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: Run the subsong stage of HVCModelCode (1,000 steps of 10 ms, seed neurons driven\n    together with probability 0.1 per step, no learning, beta 0.115, alpha 30, gamma 0.01, seed\n    9038). Reproduced when the mean number of non-seed neurons active at each step after a seed\n    activation returns to the level of steps not preceded by a seed activation within 100 ms\n    (10 steps), so that activity does not last a protosyllable period. Ten further seeds are run\n    as a variant, as MATLAB's generator may not be reproduced elsewhere.\n- id: model-fig5b-chain\n  statement: Rhythmic activation of the seed neurons with learning grows a feedforward chain that\n    supports stable propagation of activity through the protosyllable.\n  source: Results, Mechanistic model and discussion, paragraph 4; Figure 5b\n  quote: As a result, connections were strengthened along the population of neurons sequentially\n    activated after syllable onsets, resulting in the growth of a feedforward synaptically\n    connected chain that supported stable propagation of activity (Fig. 5b)\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: Run 500 protosyllable iterations (1 s each, seeds every 100 ms; eta 0.025, epsilon\n    0.2, wmax 1, m 10) after subsong. Participating neurons as the code defines them (firing at\n    their most common latency more than 4 times in the 10 cycles of the iteration). Reproduced\n    when, at iteration 500, participating non-seed neurons have most common latencies covering\n    every 10 ms step of the cycle, and there are more of them than participate in subsong.\n- id: model-fig5cd-split\n  statement: Activating two halves of the seed neurons on alternate cycles splits the chain into\n    two daughter chains; during splitting there are neurons specific to each syllable and shared\n    neurons active at the same latency in both, and the fraction of shared neurons decreases.\n  source: Results, Mechanistic model and discussion, paragraphs 5 and 6; Figure 5c, d\n  quote: We found that this single chain could be induced to split into two daughter chains by\n    dividing the seed neurons into two groups that were activated on alternate cycles of the\n    rhythm (Fig. 5c, d and Supplementary Video 1) ... During the splitting process, we observed\n    neurons specific to each of the emerging syllable types, as well as shared neurons that were\n    active at the same latencies in both syllable types (Fig. 5c) ... and the fraction of shared\n    neurons decreased (Fig. 5c, d)\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: Continue with 2,000 splitting iterations (5 pulses per seed group per iteration;\n    wmax 2, m 5, gamma rising to 0.18 on a sigmoid with time constant 200 and inflection 500\n    iterations). Participation per type as the code defines it for this stage (more than 2\n    firings at the most common latency). Reproduced when at iteration 992 there are specific\n    neurons of both types and shared neurons, most shared neurons (over half) have the same\n    most common latency in both types, and at iteration 2,500 the shared fraction of\n    participating neurons is lower than at 992. Ten further seeds as a variant.\n  depends_on:\n  - model-fig5b-chain\n- id: model-fig5e-latency-broadens\n  statement: In the model, the distribution of burst latencies broadens from subsong through the\n    protosyllable stage to chain splitting.\n  source: Results, Mechanistic model and discussion, paragraph 6; Figure 5e\n  quote: over the course of development the distribution of burst latencies in the model continued\n    to broaden (Fig. 5e)\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: Latencies are the most common latency of each participating non-seed neuron\n    (findLatency in the code), at subsong, iteration 500, and splitting (992 and 2,500\n    combined, as the Fig. 5e legend says). OPEN, the measure of breadth; readings (a)\n    interquartile range, (b) standard deviation. Reproduced when, under one reading, breadth\n    increases from subsong to the protosyllable stage and from there to splitting.\n  depends_on:\n  - model-fig5cd-split\n- id: model-ed10gh-period\n  statement: In the model, the average period of rhythmic bursting increases during chain splitting\n    as specific neurons burst only on alternate cycles of the protosyllable rhythm.\n  source: Results, Mechanistic model and discussion, paragraph 6; Figure 5d; Extended Data Fig.\n    10g, h\n  quote: The average period of rhythmic bursting in model neurons increased during chain splitting\n    as neurons became ‘specific’ for one emerging syllable type and began to participate only on\n    alternate cycles of the protosyllable rhythm\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: OPEN, how the model period is measured; readings (a) per participating neuron, the\n    lag of the largest autocorrelation peak of its activity between 80 and 1,000 ms (the data\n    method), (b) its most common inter-burst interval. Reproduced when, under one reading, the\n    mean period at iteration 2,500 exceeds that at iteration 500 and specific neurons' periods\n    are near 200 ms (within 10%).\n  depends_on:\n  - model-fig5cd-split\n- id: model-ed10ad-bout-onset\n  statement: Adding bout-onset seed neurons makes the protosyllable chain split into one daughter\n    chain active only at bout onset and another active only on later syllables.\n  source: Results, Mechanistic model and discussion, paragraph 7; Extended Data Fig. 10a-d\n  quote: This caused the protosyllable chain to split in such a way that one daughter chain was\n    reliably activated only at bout onsets, while the other daughter chain was active only on\n    subsequent syllables (Extended Data Fig. 10a–d and Supplementary Video 2)\n  data: elsewhere\n  where: Supplementary Information of the article (HVCModelCode, MATLAB, supplied as\n    paper/10.1038-nature15741.code.m); no recorded data\n  criterion: Run the bout-onset section of HVCModelCode (5 bout-onset and 5 protosyllable seeds;\n    100 protosyllable and 500 splitting iterations of 10 bouts; beta 0.13, eta 0.05, epsilon\n    0.14; wmax 1 to 2, m 5 to 2.5, gamma 0.01 to 0.04, inflection 250). Participation as the code\n    defines it (thresholds 4 and 6). Reproduced when at iteration 600 there are neurons specific\n    to the bout-onset syllable and to later syllables, and the shared fraction is lower than at\n    iteration 130.\n- id: model-ed10eh-motif\n  statement: Dividing the seed neurons into three groups activated in turn splits the protosequence\n    into three non-overlapping daughter sequences, simulating the motif strategy.\n  source: Results, Mechanistic model and discussion, paragraph 7; Extended Data Fig. 10e-h\n  quote: Our model was also able to simulate the simultaneous emergence of a three-syllable motif\n    ... by dividing the seed neurons into three subpopulations ... After learning, the population of\n    neurons was active sequentially throughout the entire ‘motif,’ but individual neurons were\n    active during only one of the resulting syllables, forming three distinct non-overlapping\n    sequences\n  data: elsewhere\n  where: github.com/emackev/HVCModelCode (named in the Supplementary Information code; not read,\n    no commit pinned); the supplied code does not hold this simulation\n  criterion: Parameters from the Methods (9 seeds, 3 groups of 3 each driven every third cycle;\n    beta 0.115, alpha 30, eta 0.025, epsilon 0.2; wmax 1 to 2, m 9 to 3, gamma 0.01 to 0.18 with\n    time constant 200 and inflection 500). OPEN, the number of iterations and the participation\n    threshold, which the Methods do not give for this strategy; readings (a) as alternating\n    differentiation (500 and 2,000 iterations; more than 2 firings at the most common latency),\n    (b) the values in the GitHub code, if the author pins it. Reproduced when after learning no\n    participating non-seed neuron is shared among the three types and each type has specific\n    neurons.\n  depends_on:\n  - model-fig5b-chain\n- id: model-ed10ik-new-chain\n  statement: With stronger seed input, bout-onset seed neurons grow a new syllable chain at bout\n    onset while the protosyllable chain stays intact, without bout-onset differentiation.\n  source: Results, Mechanistic model and discussion, paragraph 8; Extended Data Fig. 10i-k\n  quote: We found that, by using different learning parameters, our model allows bout-onset seed\n    neurons to induce the formation of a new syllable chain at bout onset\n  data: elsewhere\n  where: github.com/emackev/HVCModelCode (named in the Supplementary Information code; not read,\n    no commit pinned); the supplied code holds only the bout-onset differentiation run\n  criterion: As model-ed10ad-bout-onset with the Methods' parameters for this case (seed input 2.5\n    Wmax throughout; beta 0.13, eta 0.05, epsilon 0.15; m 5 to 2.5; gamma 0.01 to 0.05). Reproduced\n    when at the end there are neurons specific to the bout-onset element and neurons specific to\n    the protosyllable, and the protosyllable seed neurons are still active on every protosyllable\n    input.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/okubo-2015.yaml paper/10.1038-nature15741.txt; grep -n -i "rather\|—" claims/okubo-2015.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/implementation (refs 51, 55: Sound Analysis Pro)/implementation (refs 51 and 55, Sound Analysis Pro)/' claims/okubo-2015.yaml; python - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/okubo-2015.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'.'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(path)
walk(d)
EOF
python tools/claims_check.py claims/okubo-2015.yaml paper/10.1038-nature15741.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/okubo-2015.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/okubo-2015.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum(len(x.get('statistics',[])) for x in c))"; git status --short claims/
```

```
42 14 42 21
?? claims/okubo-2015.yaml
```

**Agent**

I've written `claims/okubo-2015.yaml` with 42 claims. The quote checker reports no problems: every quote matches the paper word for word and all 21 statistical values were found in the text. Nothing was committed.

**Text read.** The version of record (`paper/10.1038-nature15741.txt`): main text, figure legends, Methods and the legends of Extended Data Figs 1–10. The Supplementary Information is the model code (`paper/10.1038-nature15741.code.m`), which I read; its two videos were not supplied, and no claim rests on them alone. No code for analysing the recordings is linked, so every data method comes from the Methods and legends. The model code agrees with the Methods. Where the Methods leave something open for the model, the code settles it and I followed it: the participation thresholds, the iterations shown in Fig. 5c and 5d, and the random seed.

**Counts.**
- 42 claims, all with a quote and none marked `inferred`.
- 14 claims carry statistics (21 entries); all 42 have a criterion.
- 34 claims are on the recordings: 4 of them use the adult stage and are marked `with_inputs`, and 30 use the dataset alone.
- 8 claims are on the model and are marked `elsewhere`.

**Details the paper leaves open, with the readings named:**
- **Syllable locking:** the smoothing kernel (a 20-bin moving average, as a standard choice); whether shifted spikes wrap around the window (circular shift, or shift from a wider window); and, in stages with several syllable types, whether syllables are pooled or each type is tested separately.
- **Rhythmicity:** the bin widths of the inter-burst-interval histogram and the autocorrelation (1 ms smoothed over 20 bins, or 10 ms); and whether the cepstrum comes from the mean spectrum or from each window.
- **Shared/specific neurons:** whether to align to syllable onset or offset (each figure's own choice, the other as a variant). The paper's visual adjustment of the analysis window can't be repeated exactly.
- **Fig. 2c latencies:** one peak latency per neuron (which fits 63% and 43%) or all bursts pooled.
- **"Participated in a protosequence" (14/16 in bird 1, 28/35 in bird 2):** locked, rhythmic, or both.
- **Pooled tests:** the 8 syllable pairs and the early/late split for the Cochran–Mantel–Haenszel test, with and without continuity correction. Plain chi-square without correction reproduces the printed P = 0.03 and 5×10⁻⁴, so that variant is used.
- **Stage–age correlation:** the unit is a day, a neuron or a bird-stage.
- **Neuron sets and denominators:** which neurons enter the bias measure, and the denominators for the 19% vs 28% comparison.
- **Unspecified rules:** how a neuron is assigned 10 Hz or 5 Hz; a rule for "skipping cycles"; the post-hoc tests; the sound-amplitude envelope used for phase; and the acoustic-feature implementation.
- **Model:** the breadth measure (interquartile range or s.d.); the period measure (autocorrelation peak or most common interval); and the iterations and threshold for the motif strategy.

**Missing from the paper or this run:**
- **Significance stars:** the PDF couldn't be rendered (no renderer installed), so I couldn't see which stages carry the stars in Fig. 1f, Fig. 1g and Extended Data Fig. 1c. Those post-hoc results are reported, not judged.
- **Adult neurons:** the 3 adult birds (32 neurons) include recordings published earlier (ref. 20, Kozhevnikov & Fee 2007). The data descriptor lists only juvenile birds, so they may not be in the dataset.
- **Model code:** the motif-strategy model (Extended Data Fig. 10e–h) and the new-chain model (10i–k) are only in github.com/emackev/HVCModelCode, which I didn't read and which has no pinned commit.
- **Neuron count:** Extended Data Fig. 2l gives 149 bout-offset neurons, but the Results counts give 98 + 50 = 148.

## End of run

25 turns, 8 minutes, $2.80 at API prices, result: success.
