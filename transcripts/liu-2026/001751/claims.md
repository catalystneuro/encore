# 001751 · claims · run 39564354341

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/001453/ paper/ claims/001751 2>&1; wc -c paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; fold -w 3000 -s 10.1038-s41556-026-02009-4.txt | head -c 70000 | tail -c 63000
```

```
<persisted-output>
Output too large (61.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7fa66cec-9d4a-4f13-8072-3a651868a6e6/tool-results/bt8g8rfi6.txt

Preview (first 2KB):
676 10.1038-s41556-026-02009-4.txt
3 and 5 are shown to the right. Red arrowheads mark the VENs, which are exclusively observed in the macaque AIC and ACC. Scale bars apply to ( a , b ). Representative replications ( n = 3 independent experiments) show consistent results. b . As in ( a ), but for the macaque V1. See Supplementary Fig. 1 for staining from additional macaque brain regions. Representative replications ( n = 5 independent experiments) show consistent results. c . Two representative VENs from ( a ). The spindle-shaped perikarya are marked with ‘s’, and the bipolar apical and basal dendrites are labelled as ‘a’ and ‘b’, respectively. VENs ( n = 55) were observed from 9 slices. d . Box plots showing the comparisons of soma size (upper) and cell density (bottom) and between the V1 and AIC, as assessed by two-sided Wilcoxon rank-sum test with Bonferroni correction. AIC L2/3 ( n = 105 cells), V1 L2/3 ( n = 85 cells), AIC L5 (n = 90 cells), and V1 L5 (n = 90 cells) for the upper panel. The ROIs (regions of interest) for cell density calculation in AIC L2/3 (n = 15 ROIs), V1 L2/3 (n = 20 ROIs), AIC L5 (n = 15 ROIs), and V1 L5 (n = 20 ROIs) obtained from three animals per region (AIC and V1). Box plots show median (center line), 25th–75th percentiles (box bounds), and whiskers extending to the minimum and maximum values within 1.5× interquartile range. Statistical significance was determined using a two-tailed Wilcoxon rank-sum test followed by Benjamini-Hochberg FDR correction. e . UMAP visualization of established marker genes for excitatory neurons ( SLC17A7 ), inhibitory neurons ( GAD1 ), astrocytes ( AQP4 ), microglia ( C1QA ), OPCs ( C1QL1 ), and oligodendrocytes ( MBP ). f . Dot plot showing marker gene expression
[... 2 more lines not kept]
```

**Agent**

The file has 676 lines. I'll read it directly.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41556-026-02009-4.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print length($0)}' paper/*.txt | sort -n | tail -5; awk 'length($0)>2000{print NR}' paper/*.txt; mkdir -p $TMPDIR/p; fold -w 4000 -s paper/*.txt > $TMPDIR/p/f.txt; wc -c $TMPDIR/p/f.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1038-s41556-026-02009-4.txt').read()
i=t.find('Due to the lack of axonal information from sta')
print(t[i:i+50000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7fa66cec-9d4a-4f13-8072-3a651868a6e6/tool-results/bjoc8zaib.txt"
}
```

```
1	Due to the lack of axonal information from staining, the number of data points is 36, 20 and 74 for VEN-L, VEN-S and PC, respectively. f , UMAP representation of projection neurons with Patch-seq neurons mapped onto the UMAP. Expert-defined Patch-seq neurons including VEN-L and VEN-S are labelled. g , UMAP visualization of neuron subpopulations obtained by re-clustering Exc FEZF2 COL24A1. Patch-seq neurons are mapped to these subpopulations and presented on the UMAP. h , Stacked violin plot showing the expression of marker genes across subpopulations identified in g and Exc FEZF2 DSG2. Vertical rectangles indicate the expression of marker genes of both VEN subtypes. The maximum log-normalized expression value for each gene is shown on the right. The colour bar denotes the median expression in the neuron groups. i , j , Fluorescent staining confirming the gene markers HAPLN4 and POC5 for VEN-L and VEN-S, respectively. Biocytin was co-stained with HAPLN4 and POC5 antibodies. The somata (indicated by yellow arrows) are zoomed-in as indicated by dashed contours. Independent replications ( n = 5) yielded consistent results. Box plots in d and e show median (centre line), 25th–75th percentiles (box bounds) and whiskers extending to the minimum and maximum values within 1.5× interquartile range. Source data To determine whether these two morphological subtypes were also transcriptomically and physiologically distinguishable, we leveraged our combined Patch-seq and scRNA-seq data. By cross-referencing the molecular assignment with their morphology, we found the morphologically defined VENs mapped to L5 ET (Exc FEZF2 DSG2) were VEN-Ls ( n = 10), while those VENs mapped to L5/6 CT (Exc FEZF2 COL24A1) were VEN-Ss ( n = 11) (Fig. 6f ). To definitively distinguish VEN-S from canonical L5/6 CT neurons, we performed subclustering of the Exc FEZF2 COL24A1 population, revealing five transcriptomic subclusters (Fig. 6g ). VEN-Ss were specifically assigned to the subcluster COL24A1 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1038-s41556-026-02009-4.txt').read()
i=t.find('The minimum current injection required to elicit an AP')
print(t[i:])" > $TMPDIR/p/rest.txt; wc -c $TMPDIR/p/rest.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p/rest.txt"
}
```

```
1	The minimum current injection required to elicit an AP (or APs) was defined as the rheobase. To calculate the AP threshold, the 20-ms potential trace preceding the AP peak was used to calculate the third derivative, with the data point exhibiting the highest third derivative considered as the AP threshold. The difference between AP peak and threshold defined the AP amplitude. The AP rise time spanned from the threshold point to the AP peak, and the decay phase time refers to the downstroke duration. AP half-width was the duration between the rising and decay phases at half the height of the AP amplitude. The time from the stimulation onset to the AP threshold was termed as the AP delay time. The ‘after hyperpolarization’ (AHP) represented the voltage difference between the threshold and the minimal trough value following the AP. The number of APs in each depolarization trace was counted, and the maximal firing rate was calculated as the maximal number of APs divided by the stimulation duration (600 ms). The sag represents the trace trough following the hyperpolarizing current injection. The resting membrane potential (RMP) denotes the average value during the resting periods preceding the current injections in all sweeps. The trace within the last 100 ms of the stimulation was defined as steady-state voltage. Input resistance refers to the slope of the differences between the RMP and the steady-state membrane potentials, relative to the injected stepped currents. Sag value was the difference between the RMP and the steady-state voltage with maximal hyperpolarization current injection. Sag ratio is determined as the voltage difference between the sag trough and the RMP divided by the difference between RMP and the steady-state voltage. Sag time is the duration between the two intersections of the sag trace crossing the steady-state potential. Sag area described the field enclosed by the sag trough and the steady-state potential. The membrane time constant τ (tau) d
[... 1 more lines not kept]
```

**Agent**

I've read the main text and Methods. Next, I'm checking the rest of the file for supplementary material.

**Agent calls Bash**

```bash
cd  sed -n '8,676p' paper/*.txt | head -100; echo ----; sed -n '8,676p' paper/*.txt | grep -n -i -E "supplementary|table 5|connect" | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls claims/001746 claims/001750 claims/001752 2>&1; ls questions | grep -E "00175|001746"; git log --oneline -3 -- claims/001752
```

```
ls: cannot access 'claims/001746': No such file or directory
ls: cannot access 'claims/001750': No such file or directory
claims/001752:
10.1038-s41556-026-02009-4.yaml
001754.yaml
bf8bf17d Claims for DANDI:001752, checked
```

**Agent calls Bash**

```bash
cd  cat claims/001752/*.yaml
```

```
<persisted-output>
Output too large (42.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7fa66cec-9d4a-4f13-8072-3a651868a6e6/tool-results/b1r7c6euc.txt

Preview (first 2KB):
# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), "An atlas of primate insular cortex
# reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 28,
# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive "Cell Atlas and Novel Signal
# Processing Strategy in Primate Insular Cortex"), on dandiset 001752.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored
# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code
# availability. No PDF was available, so values printed only inside figures (for example the
# p-values of Fig. 5b,c) could not be read. The Supplementary Information (Supplementary Figs.
# 1 to 17, Supplementary Tables 1 to 12) and the Source Data files were not in the text read;
# claims that cite them rest on the main text, and say so. The claims this dataset can test
# (Fig. 5a-c) rest on the main text, the Fig. 5 legend and the Methods, all of which were read.
#
# Code read: github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/7fa66cec-9d4a-4f13-8072-3a651868a6e6/tool-results/b1r7c6euc.txt"
}
```

```
1	# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), "An atlas of primate insular cortex
2	# reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 28,
3	# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive "Cell Atlas and Novel Signal
4	# Processing Strategy in Primate Insular Cortex"), on dandiset 001752.
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
6	# protocol as stated in docs/protocol.md (version pilot-10).
7	#
8	# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored
9	# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code
10	# availability. No PDF was available, so values printed only inside figures (for example the
11	# p-values of Fig. 5b,c) could not be read. The Supplementary Information (Supplementary Figs.
12	# 1 to 17, Supplementary Tables 1 to 12) and the Source Data files were not in the text read;
13	# claims that cite them rest on the main text, and say so. The claims this dataset can test
14	# (Fig. 5a-c) rest on the main text, the Fig. 5 legend and the Methods, all of which were read.
15	#
16	# Code read: github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d
17	# (2026-07-05). It holds MATLAB and Python scripts per figure (its file names follow an older
18	# figure numbering; ephysio/Fig5ab_ana_sPSC.m and Fig5ab_ana_mPSC.m make the paper's Fig. 5b,c),
19	# per-cell summary tables (ephysio/data_ephy/sPSCs_Fig7ab.xlsx and miniEPSCs_Fig7ab.xlsx give one
20	# frequency and one mean amplitude per cell, already detected with miniAnalysis), and a table
[... 633 more lines not kept]
```

**Agent**

The 001752 file gives the template. For 001751 the testable claims are the multi-patch connectivity results (Fig. 5d–i). Next, I'm reading the paper's code repository for the connectivity analysis.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/RFLiu2021/AIC_proj && cd AIC_proj && git log -1 --format='%H %ci' && git ls-files | wc -l && git ls-files | grep -i -E "conn|pair|multi|8ch|eight|Fig7|Fig5|uEPSP|synap" | head -80
```

```
44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d 2026-07-05 09:47:58 +0800
159
10X/Plot_SupplFig5a.ipynb
VEN_modeling/FigPlot/Fig4g_extFig7b_plotSpikes_VENcmp_AISd.m
VEN_modeling/FigPlot/Fig4i_plotVENResponse2monoSynapticInputTrain_VENso_vs_VENd.m
VEN_modeling/FigPlot/Fig4itop_plotAndFittingSpikePhaseHeightIdx_model.m
VEN_modeling/FigPlot/Fig4k_thin_vs_thick_monoSynapticInputTrain.m
VEN_modeling/FigPlot/exdFig7a_exampleModelTraces.m
VEN_modeling/FigPlot/extFig7c_plotVarySomaNaChannelDensity_PC.m
VEN_modeling/FigPlot/extFig7d_plotSpikes_VENcmp_AISl.m
VEN_modeling/FigPlot/extFig7e_plotSpikes_PCcmp_AISl.m
VEN_modeling/FigPlot/extFig7f_plotSpikes_VENcmp_bigDenThick.m
VEN_modeling/FigPlot/extFig7gh_EPSPcmp_bigDend_vs_thinDend.m
VEN_modeling/FigPlot/extFig7j_plotSingleSyn2BigDenVarythickness.m
ephysio/Fig5ab_ana_mPSC.m
ephysio/Fig5ab_ana_sPSC.m
ephysio/Fig5e_plotConnexampleFPs.m
ephysio/Fig5fg_plotConn.m
ephysio/Fig7cf_supplFig16a_ephyFeatures_2_10X_Ext.ipynb
ephysio/data_ephy/PeakIdx_Fig5e.xlsx
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AIC_proj; cat ephysio/Fig5fg_plotConn.m; echo ======; cat ephysio/Fig5e_plotConnexampleFPs.m | head -80; ls ephysio/data_ephy/rawdata_ephysio/; cat README* 2>/dev/null | head -60
```

```
clear all;
close all;

%% % =========  import data from the HEKA file and save to a mat file. =====
% connectfile1 = '../data_electro/20190315/20190315s4c2r1.dat';
% d = HEKA_Importer(connectfile1);
% 
% % Selected the test round 2.
% presyn_C2.d_postsyn_C1 = d.RecTable.dataRaw{2}{1};    % Cell 1 recorded from HEKA channel 1.
% presyn_C2.d_postsyn_C1 = resample(presyn_C2.d_postsyn_C1,1,25);
% presyn_C2.d_presyn_C2 = d.RecTable.dataRaw{2}{2};    % Cell 2 recorded from HEKA channel 2.    
% presyn_C2.d_presyn_C2 = resample(presyn_C2.d_presyn_C2,1,25);
% presyn_C2.d_postsyn_C3 = d.RecTable.dataRaw{2}{3};    % Cell 3 recorded from HEKA channel 3.    
% presyn_C2.d_postsyn_C3 = resample(presyn_C2.d_postsyn_C3,1,25);
% presyn_C2.d_postsyn_C4 = d.RecTable.dataRaw{2}{6};    % Cell 4 recorded from HEKA channel 6.    
% presyn_C2.d_postsyn_C4 = resample(presyn_C2.d_postsyn_C4,1,25);
% presyn_C2.d_postsyn_C5 = d.RecTable.dataRaw{2}{7};    % Cell 5 recorded from HEKA channel 7.    
% presyn_C2.d_postsyn_C5 = resample(presyn_C2.d_postsyn_C5,1,25);
% presyn_C2.d_postsyn_C6 = d.RecTable.dataRaw{2}{8};    % Cell 6 recorded from HEKA channel 8.    
% presyn_C2.d_postsyn_C6 = resample(presyn_C2.d_postsyn_C6,1,25);
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/AIC_proj; pip list 2>/dev/null | grep -i -E "openpyxl|pandas|scipy"; python3 -c "
import pandas as pd
x=pd.read_excel('ephysio/data_ephy/rawdata_ephysio/metadata_multiPatch.xlsx',sheet_name=None)
for k,v in x.items():
  print(k,v.shape); print(v.columns.tolist()); print(v.head(15).to_string()); 
  for c in v.columns:
    if v[c].nunique()<30: print(c, v[c].value_counts(dropna=False).to_dict())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

**Agent**

Reading the code repo's multi-patch metadata table (part of the linked code, not the dataset).

**Agent calls Bash**

```bash
cd $TMPDIR/AIC_proj/ephysio/data_ephy/rawdata_ephysio; cat "raw data deposited at DANDI.txt"; python3 -c "import openpyxl" 2>&1; mkdir -p $TMPDIR/x && cd $TMPDIR/x && unzip -o -q $TMPDIR/AIC_proj/ephysio/data_ephy/rawdata_ephysio/metadata_multiPatch.xlsx && ls xl xl/worksheets; wc -c xl/sharedStrings.xml xl/worksheets/*.xml
```

```
https://dandiarchive.org/dandiset/001746：ephysioData of Patchseq
https://dandiarchive.org/dandiset/001750:  Sodium channel current
https://dandiarchive.org/dandiset/001751:  multi-Patch recording
https://dandiarchive.org/dandiset/001752：Post-synaptic current

Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import openpyxl
ModuleNotFoundError: No module named 'openpyxl'
xl:
_rels
sharedStrings.xml
styles.xml
theme
workbook.xml
worksheets

xl/worksheets:
sheet1.xml
sheet2.xml
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/x; cat xl/workbook.xml | grep -o '<sheet [^>]*>'; cat > $TMPDIR/rx.py <<'EOF'
import re,sys,xml.etree.ElementTree as ET
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ss=[ ''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])) for si in ET.parse('xl/sharedStrings.xml').getroot().findall('m:si',ns)]
def rows(f):
    out=[]
    for r in ET.parse(f).getroot().iter('{%s}row'%ns['m']):
        row={}
        for c in r.findall('m:c',ns):
            col=re.match(r'[A-Z]+',c.get('r')).group()
            v=c.find('m:v',ns); 
            if v is None:
                isv=c.find('m:is',ns); val=''.join(t.text or '' for t in isv.iter('{%s}t'%ns['m'])) if isv is not None else ''
            else:
                val=ss[int(v.text)] if c.get('t')=='s' else v.text
            row[col]=val
        out.append(row)
    return out
EOF
python3 -c "
exec(open('$TMPDIR/rx.py').read())
for f in ['xl/worksheets/sheet1.xml','xl/worksheets/sheet2.xml']:
  R=rows(f); print(f,len(R))
  for r in R[:12]: print(r)
"
```

```
<sheet name="metadata_multiPatch" sheetId="1" r:id="rId1"/>
<sheet name="Sheet1" sheetId="2" r:id="rId2"/>
xl/worksheets/sheet1.xml 1418
{'A': 'Subject_id', 'B': 'Session_ID/SliceID', 'C': 'Nr_Conn', 'D': 'filename_original(.dat)', 'E': 'filename', 'F': 'preSynChannel', 'G': 'posySynChannel', 'H': 'preSynCellType', 'I': 'postSynCellType', 'J': 'ConnType', 'K': 'connQuality', 'L': 'projection'}
{'A': 'Mfa190314', 'B': '190314s1', 'C': '0', 'D': '190314s1c2', 'E': 'sub-Mfa190314_ses-190314s1_obj-dktfoi_icephys.nwb', 'F': '2', 'G': '3', 'H': 'PC', 'I': 'PC'}
{'G': '4', 'H': 'PC', 'I': 'VEN'}
{'G': '5', 'H': 'PC', 'I': 'PC'}
{'G': '6', 'H': 'PC', 'I': 'PC'}
{'G': '7', 'H': 'PC', 'I': 'VEN', 'L': ''}
{'D': '190314s1c3', 'E': 'sub-Mfa190314_ses-190314s1_obj-1w59zvc_icephys.nwb', 'F': '3', 'G': '2', 'H': 'PC', 'I': 'PC', 'L': ''}
{'G': '4', 'H': 'PC', 'I': 'VEN', 'L': ''}
{'G': '5', 'H': 'PC', 'I': 'PC', 'L': ''}
{'G': '6', 'H': 'PC', 'I': 'PC', 'L': ''}
{'G': '7', 'H': 'PC', 'I': 'VEN', 'L': ''}
{'D': '190314s1c4', 'E': 'sub-Mfa190314_ses-190314s1_obj-m0snq6_icephys.nwb', 'F': '4', 'G': '2', 'H': 'VEN', 'I': 'PC', 'L': ''}
xl/worksheets/sheet2.xml 899
{'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'M': '190314s1c2', 'N': 'sub-Mfa190314_ses-190314s1_obj-dktfoi_icephys.nwb'}
{'B': '', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': ''}
{'B': 'dandiset.yaml', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': ''}
{'B': 'sub-Mfa190314/', 'C': '', 'D': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': ''}
[... 9 more lines not kept]
```

**Agent**

The code's metadata table lists each tested pair with cell types and connection annotations. Next I'm tallying it against the paper's counts.

**Agent calls Bash**

```bash
cd $TMPDIR/x; python3 -c "
exec(open('$TMPDIR/rx.py').read())
from collections import Counter
R=rows('xl/worksheets/sheet1.xml'); hdr=R[0]; R=R[1:]
cur={}
P=[]
for r in R:
  if not any(v.strip() for v in r.values() if v): continue
  for k in 'ABCDEF':
    if r.get(k,'').strip(): cur[k]=r[k].strip()
    if k=='D' and r.get('D','').strip():  # new presyn file
      pass
  if r.get('H','').strip(): cur['H']=r['H'].strip()
  rec=dict(cur); rec.update({k:r.get(k,'').strip() for k in 'GIJKL'})
  P.append(rec)
print(len(P))
print('subjects',len(set(p['A'] for p in P)),sorted(set(p['A'] for p in P)))
print('sessions',len(set(p['B'] for p in P)))
print('pre files',len(set(p['D'] for p in P)))
cells=set((p['B'],p['F'],p['H']) for p in P)|set((p['B'],p['G'],p['I']) for p in P)
print('cells',len(set((c[0],c[1]) for c in cells)), Counter(c[2] for c in cells))
print(Counter((p['H'],p['I']) for p in P))
print('ConnType',Counter(p['J'] for p in P))
print('Quality',Counter(p['K'] for p in P))
print('proj',Counter(p['L'] for p in P))
print('NrConn col', Counter(r.get('C','') for r in R))
for p in P:
  if p['J'] or p['K']: print(p)
# unordered pairs
up=Counter(tuple(sorted([(p['B'],p['F']),(p['B'],p['G'])])) for p in P)
print('ordered',len(P),'unordered',len(up))
dup=Counter((p['B'],p['F'],p['G']) for p in P); print('dup ordered',[k for k,v in dup.items() if v>1][:10])
"
```

```
1416
subjects 6 ['Mfa190314', 'Mfa240911', 'Mfa241008', 'Mfa241014', 'Mfa241105', 'Mfa241218']
sessions 55
pre files 288
cells 298 Counter({'PC': 207, 'VEN': 56, 'GABA': 40})
Counter({('PC', 'PC'): 749, ('VEN', 'PC'): 146, ('PC', 'VEN'): 145, ('GABA', 'PC'): 86, ('PC', 'GABA'): 84, ('VEN', 'VEN'): 59, ('GABA', 'VEN'): 54, ('VEN', 'GABA'): 54, ('GABA', 'GABA'): 39})
ConnType Counter({'': 1390, 'Ext': 14, 'Inh': 12})
Quality Counter({'': 1390, 'Excellent': 16, 'Good': 7, 'OK': 3})
proj Counter({'': 1390, '4→6': 3, '6→3': 2, '1→7': 2, '1→8': 2, '4→3': 2, '7→2': 2, '8→5': 2, '2→8': 1, '2→7': 1, '4→7': 1, '6→4': 1, '4→8': 1, '7→3': 1, '7→4': 1, '7→6': 1, '7→8': 1, '6→1': 1, '2→4': 1})
NrConn col Counter({'': 1364, '0': 38, '1': 11, '2': 2, '3': 1, '6': 1})
{'A': 'Mfa190314', 'B': '190315s2', 'C': '1', 'D': '20190315s2c4', 'E': 'sub-Mfa190314_ses-190315s2_obj-1e6g6jn_icephys.nwb', 'F': '4', 'H': 'VEN', 'G': '6', 'I': 'PC', 'J': 'Ext', 'K': 'Excellent', 'L': '4→6'}
{'A': 'Mfa190314', 'B': '190315s3', 'C': '1', 'D': '20190315s3c6', 'E': 'sub-Mfa190314_ses-190315s3_obj-18qmqq1_icephys.nwb', 'F': '6', 'H': 'PC', 'G': '3', 'I': 'PC', 'J': 'Ext', 'K': 'Excellent', 'L': '6→3'}
{'A': 'Mfa190314', 'B': '190315s4', 'C': '1', 'D': '20190315s4c2', 'E': 'sub-Mfa190314_ses-190315s4_obj-1hcjbol_icephys.nwb', 'F': '2', 'H': 'PC', 'G': '8', 'I': 'PC', 'J': 'Ext', 'K': 'Excellent', 'L': '2→8'}
{'A': 'Mfa190314', 'B': '190315s5', 'C': '1', 'D': '20190315s5c2', 'E': 'sub-Mfa190314_ses-190315s5_obj-u9g7xs_icephys.nwb', 'F': '2', 'H': 'PC', 'G': '7', 'I': 'VEN', 'J': 'Ext', 'K': 'Excellent', 'L': '2→7'}
{'A': 'Mfa240911', 'B': '20240911VENS2(3)', 'C': '1', 'D': '20240911VENS2c1', 'E': 'sub-Mfa240911_ses-20240911HS2_obj-1vw8u2v_icephys.nwb', 'F': '1', 'H': 'PC', 'G': '7', 'I': 'PC', 'J': 'Inh', 'K': 'Good', 'L': '1→7'}
{'A': 'Mfa240911', 'B': '20240911VENS2(3)', 'C': '1', 'D': '20240911VENS2c1', 'E': 'sub-Mfa240911_ses-20240911HS2_obj-1vw8u2v_icephys.nwb', 'F': '1', 'H': 'PC', 'G': '8', 'I': 'P
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/x; python3 -c "
exec(open('$TMPDIR/rx.py').read())
from collections import Counter
R=rows('xl/worksheets/sheet1.xml')[1:]
cur={};P=[]
for r in R:
  if not any(v.strip() for v in r.values() if v): continue
  for k in 'ABCDEFH':
    if r.get(k,'').strip(): cur[k]=r[k].strip()
  rec=dict(cur); rec.update({k:r.get(k,'').strip() for k in 'GIJKL'}); P.append(rec)
print(Counter((p['H'],p['I'],p['J']) for p in P if p['J']))
print(Counter((p['H'],p['I'],p['J'],p['K']) for p in P if p['J']))
# Nr_Conn per session sum
S={}
for r in R:
  pass
ses=Counter(); nr={}
for p in P:
  nr[p['B']]=p['C']
print('sum Nr_Conn by session', sum(int(v) for v in nr.values() if v.isdigit()), len(nr))
ann=Counter(p['B'] for p in P if p['J'])
for s in nr:
  if str(ann.get(s,0))!=nr[s]: print('mismatch',s,nr[s],ann.get(s,0))
# cells per session
import collections
cs=collections.defaultdict(set)
for p in P: cs[p['B']].add(p['F']); cs[p['B']].add(p['G'])
print(Counter(len(v) for v in cs.values()))
# subjects per session date
print(Counter(p['A'] for p in P))
"
```

```
Counter({('PC', 'PC', 'Ext'): 11, ('PC', 'PC', 'Inh'): 7, ('GABA', 'PC', 'Inh'): 4, ('VEN', 'PC', 'Ext'): 1, ('PC', 'VEN', 'Ext'): 1, ('PC', 'GABA', 'Inh'): 1, ('PC', 'GABA', 'Ext'): 1})
Counter({('PC', 'PC', 'Ext', 'Excellent'): 8, ('PC', 'PC', 'Inh', 'Excellent'): 4, ('PC', 'PC', 'Inh', 'Good'): 3, ('GABA', 'PC', 'Inh', 'Good'): 2, ('PC', 'PC', 'Ext', 'Good'): 2, ('VEN', 'PC', 'Ext', 'Excellent'): 1, ('PC', 'VEN', 'Ext', 'Excellent'): 1, ('GABA', 'PC', 'Inh', 'OK'): 1, ('PC', 'GABA', 'Inh', 'OK'): 1, ('PC', 'GABA', 'Ext', 'Excellent'): 1, ('PC', 'PC', 'Ext', 'OK'): 1, ('GABA', 'PC', 'Inh', 'Excellent'): 1})
sum Nr_Conn by session 26 55
mismatch 20240911VENS2(3) 1 2
mismatch 20241008venHS4 1 0
mismatch 20241014venHS1 1 0
mismatch 20241014venHS9 0 1
mismatch 20241014venHS10 6 7
mismatch 20241014venHS12 1 0
Counter({6: 14, 4: 12, 5: 12, 7: 10, 3: 4, 8: 3})
Counter({'Mfa241014': 522, 'Mfa241105': 344, 'Mfa190314': 210, 'Mfa240911': 182, 'Mfa241218': 100, 'Mfa241008': 58})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/AIC_proj; curl -s https://api.dandiarchive.org/api/dandisets/001751/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d[k] for k in ('identifier','created','most_recent_published_version','draft_version') if k in d},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001751/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'));print(m.get('relatedResource'))"; grep -rl "filter_300Lowpass" . | head;
```

Result: the fetched text is not kept.

**Agent**

Next I'm looking up references 111–113 (software and processed-data DOIs) and the Fig. 5i/Supplementary Table 5 mentions.

**Agent calls Bash**

```bash
cd  grep -o -E "\[11[0-3]\][^\[]*" paper/*.txt; ls claims/001453; sed -n 1,60p claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Zenodo DOI 17799559 (the paper) and 18814764 (the README) may hold connectivity summaries. I'm checking their file lists.

**Agent calls Bash**

```bash
for r in 17799559 18814764 19995355; do echo "== $r"; curl -sL https://zenodo.org/api/records/$r | python3 -c "
import json,sys
d=json.load(sys.stdin); print(d.get('doi'), d.get('metadata',{}).get('version'), d.get('metadata',{}).get('publication_date'), d.get('conceptdoi'))
for f in d.get('files',[]): print(' ',f['key'], f['size'])
"; done
```

Result: the fetched text is not kept.

**Agent**

The concept DOI 17799559 resolves to 18814764: 11 GB of RAR archives, which I won't open. PatchAnaLab (111 MB) may hold the connection-detection routine, so I'm listing its contents.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o pal.zip "https://zenodo.org/api/records/19995355/files/PatchAnaLab_1_0.zip/content" && ls -la pal.zip && unzip -l pal.zip | grep -v -E "\.(png|jpg|tif|fig|mat|asc|dat|abf)$" | grep -i -E "conn|syn|psp|pair|multi|\.m$" | head -60; unzip -l pal.zip | tail -1
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && unzip -l pal.zip | awk '{print $4}' | grep -i -E "conn|syn|psp|filter|lowpass" ; unzip -p pal.zip ElectroLab/tools/lowp.m
```

```
ElectroLab/tools/utils/@scchannel/isInSynch.m
ElectroLab/tools/utils/scFilter.m
ElectroLab/tools/utils/scFindSynchronized.m
helpers/filter_1000Lowpass.m
helpers/filter_300Lowpass.m
helpers/filter_butter.m
function y=lowp(x,f1,f3,rp,rs,Fs)

wp=2*pi*f1/Fs;
ws=2*pi*f3/Fs;
[n,wn]=cheb1ord(wp/pi,ws/pi,rp,rs);
[bz1,az1]=cheby1(n,rp,wp/pi);
[h,w]=freqz(bz1,az1,256,Fs);
h=20*log10(abs(h));
y=filter(bz1,az1,x);
index = floor(length(y)*0.1);
if  length(index) > 1100
    y(1:index) =  smooth(x(1:index), 1000)
else
    y(1:index) =  x(1:index);
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && unzip -p pal.zip helpers/filter_300Lowpass.m
```

```
function [ data_new ] = filter_300Lowpass( WB_data, adfreq )
%FILTER_WB Summary of this function goes here
%   Detailed explanation goes here



FilterOrder   =  2;                                   % order of filter
FilterCutOff  =  300;                                 % cutoff freq for filter
FilterType    =  'butter';                            % type of filter

[a,b]= feval(FilterType,FilterOrder,FilterCutOff/(0.5*adfreq),'low');

data_new          = filtfilt(a,b,WB_data);







[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/x; python3 -c "
exec(open('$TMPDIR/rx.py').read())
R=rows('xl/worksheets/sheet1.xml')[1:]
cur={}
for r in R:
  if not any(v.strip() for v in r.values() if v): continue
  for k in 'ABCDEFH':
    if r.get(k,'').strip(): cur[k]=r[k].strip()
  if cur['B'] in ('190315s4','190315s2'): print(cur['B'],cur['D'],cur['F'],cur['H'],'->',r.get('G'),r.get('I'),r.get('J',''),r.get('K',''),r.get('L',''))
"
```

```
190315s2 20190315s2c1 1 VEN -> 2 PC   
190315s2 20190315s2c1 1 VEN -> 3 PC   
190315s2 20190315s2c1 1 VEN -> 4 VEN   
190315s2 20190315s2c1 1 VEN -> 6 PC   
190315s2 20190315s2c1 1 VEN -> 7 PC   
190315s2 20190315s2c1 1 VEN -> 8 VEN   
190315s2 20190315s2c2 2 PC -> 1 VEN   
190315s2 20190315s2c2 2 PC -> 3 PC   
190315s2 20190315s2c2 2 PC -> 4 VEN   
190315s2 20190315s2c2 2 PC -> 6 PC   
190315s2 20190315s2c2 2 PC -> 7 PC   
190315s2 20190315s2c2 2 PC -> 8 VEN   
190315s2 20190315s2c3 3 PC -> 1 VEN   
190315s2 20190315s2c3 3 PC -> 2 PC   
190315s2 20190315s2c3 3 PC -> 4 VEN   
190315s2 20190315s2c3 3 PC -> 6 PC   
190315s2 20190315s2c3 3 PC -> 7 PC   
190315s2 20190315s2c3 3 PC -> 8 VEN   
190315s2 20190315s2c4 4 VEN -> 1 VEN   
190315s2 20190315s2c4 4 VEN -> 2 PC   
[... 53 more lines not kept]
```

**Agent**

The example slice matches Fig. 5d–h (cell 2 PC → cell 6 PC on channel 8; cell 4 VEN on channel 6). Next I'm reading the claims checker so the file meets its schema.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -n -E "ALLOWED|allowed|keys|fields" tools/claims_check.py | head -30; ls schemas 2>/dev/null
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

[... 64 more lines not kept]
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
mkdir -p claims/001751
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "content": "# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), \"An atlas of primate insular cortex\n# reveals a signal-processing strategy in von Economo neurons\", Nature Cell Biology 28,\n# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive \"Cell Atlas and Novel Signal\n# Processing Strategy in Primate Insular Cortex\"), on dandiset 001751.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md (version pilot-10).\n#\n# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored\n# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code\n# availability. No PDF was available, so values printed only inside figures could not be read.\n# The Supplementary Information (Supplementary Figs. 1 to 17, Supplementary Tables 1 to 12) and\n# the Source Data files were not in the text read. Supplementary Table 5 (\"Number of neurons and\n# tested neuron pairs of potential connectivities\") bears on the claims this dataset can test,\n# but every count those claims rest on is printed in the Results and the Fig. 5 legend, which\n# were read; claims that cite other supplementary items rest on the main text and say so.\n#\n# Code read: github.com/RFLiu2021/AIC_proj at commit 44cd8a6dfbb1f1ce363d73742e4f3652086b0f9d\n# (2026-07-05), and PatchAnaLab 1.0 (Zenodo doi:10.5281/zenodo.19995355), the paper's analysis\n# package. AIC_proj holds MATLAB and Python scripts per figure (file names follow an older figure\n# numbering) and small data tables; its processed data are in Zenodo doi:10.5281/zenodo.18814764\n# (concept doi:10.5281/zenodo.17799559, 11 GB of RAR archives, not opened). For the multi-patch\n# recordings of Fig. 5d-i it holds:\n#  - ephysio/Fig5fg_plotConn.m, which plots the example of Fig. 5f,g from slice 20190315 s4\n#    (files 20190315s4c2r1.dat and 20190315s4c6r1.dat): test round 2 of each file, cell 1 to 6\n#    on HEKA channels 1, 2, 3, 6, 7 and 8, traces resampled from 25 kHz to 1 kHz, averaged over\n#    sweeps and low-passed with filter_300Lowpass (PatchAnaLab helpers/, a 2nd-order Butterworth\n#    at 300 Hz applied with filtfilt). It plots; it detects nothing.\n#  - ephysio/Fig5e_plotConnexampleFPs.m, the firing patterns of Fig. 5e, cell types VEN, PC, PC,\n#    VEN, VEN, PC for cells 1 to 6.\n#  - ephysio/data_ephy/rawdata_ephysio/metadata_multiPatch.xlsx, one row per tested ordered pair,\n#    naming the subject, slice, original file, deposited NWB file, presynaptic and postsynaptic\n#    channel and cell type (PC, VEN, GABA), and for connected pairs ConnType (Ext or Inh),\n#    connQuality (Excellent, Good, OK) and the projection (\"2→8\"). Tallied here (the table only,\n#    not the dataset), it lists 1,416 ordered pairs among 298 cells (207 PC, 56 VEN, 40 GABA) in\n#    55 slices of 6 subjects, and 26 annotated connections. Pairs by type (the paper's count in\n#    brackets): PC-to-PC 749 (503), VEN-to-PC 146 (200), PC-to-VEN 145 (200), VEN-to-VEN 59\n#    (110), PC-to-IN 84 (65), IN-to-PC 86 (65), VEN-to-IN 54 (55), IN-to-VEN 54 (55), IN-to-IN 39\n#    (not stated; 1,292 minus the stated types is 39). Connections: PC-to-PC 18 (24; 11 Ext and\n#    7 Inh), VEN-to-PC 1 (0; slice 190315s2, VEN 4 to PC 6, Ext, Excellent), PC-to-VEN 1 (1),\n#    PC-to-IN 2 (2), IN-to-PC 4 (4). Its column Nr_Conn disagrees with its own annotations in 6\n#    slices, and one row (20241105venHS16, channel 6 to 3) carries the projection label \"8→5\".\n# No code in either source detects a connection; the rule is not given (see the criteria).\n#\n# Data the paper describes. Adult macaques (Macaca fascicularis, 4 to 6 years). scRNA-seq, 7\n# animals (two females, five males), 22 samples, 122,663 cells; Patch-seq, 12 males, 578 neurons\n# (462 with intrinsic properties, 166 reconstructed, 307 with transcriptomes kept); whole-cell\n# recording and local connectivity, 20 animals (one female, 19 males). Acute 300 um coronal slices\n# of the VEN-enriched anterior insular cortex (AIC), recordings at room temperature.\n#  - Fig. 5d-i, the data of this dandiset (title \"Electrophysiological Dataset of Local Neuronal\n#    Microcircuits in the Primate Anterior Insular Cortex\"; description, connectivity \"assessed\n#    using simultaneous multi-patch-clamp recordings in crab-eating monkeys\"; the paper's Data\n#    availability names it \"multi-Patch recording\"). Simultaneous whole-cell recordings of up to\n#    eight layer 5b neurons (two Quadro EPC 10 amplifiers, HEKA), 377 neurons, 1,292 potential\n#    connections tested. Presynaptic APs evoked by 2 nA, 2 ms current pulses at 0.01 to 0.1 Hz;\n#    postsynaptic membrane potential held at -70 +/- 3 mV for uEPSPs and -60 +/- 3 mV for uIPSPs;\n#    responses averaged over more than 20 sweeps. Firing patterns recorded with +10 pA steps every\n#    second. Cells identified as VEN, PC or interneuron (IN) by firing pattern and post hoc\n#    morphology. Measured variable, membrane potential (V) of every cell over time.\n#  - Other recordings, deposited elsewhere: Patch-seq electrophysiology (DANDI:001746), somatic\n#    Na+ currents (DANDI:001750), postsynaptic currents (DANDI:001752); scRNA-seq and Patch-seq\n#    reads (GEO GSE319557 and GSE319369); metabolomics (MetaboLights MTBLS13927); morphologies\n#    (NeuroMorpho.org, doi:10.13021/y4be-0p18).\n#\n# The paper cites no version of the dandiset. Cell types and connections: if the dataset does not\n# carry them, the only source the paper's code gives is metadata_multiPatch.xlsx, matched through\n# the NWB file names it lists; claims that use it are then data with_labels, and the attempt adds\n# a link claim. Details the paper leaves open are named in each criterion with the readings its\n# text allows. Where a criterion uses p < 0.05 and the paper prints no alpha in the text read,\n# that is the conventional reading of \"significantly\", and is said so.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001751\"\npaper: doi:10.1038/s41556-026-02009-4\nclaims:\n- id: fig5d-connectivity-totals\n  statement: Simultaneous recordings of up to eight layer 5b neurons tested 1,292 potential\n    connections among 377 neurons and found 31 monosynaptic connections.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5d\n  quote: In total, we tested 1,292 potential connections from an additional set of 377 neurons in\n    layer 5b and confirmed 31 monosynaptic connections.\n  expected:\n  - quantity: potential connections tested\n    value: 1292\n    tolerance: 129\n  - quantity: neurons\n    value: 377\n    tolerance: 38\n  - quantity: monosynaptic connections\n    value: 31\n    tolerance: 3.1\n  criterion: A neuron is one recorded cell (one channel of one slice recording, counted once\n    across the files of that slice). A potential connection is an ordered pair, a presynaptic cell\n    stimulated while another cell of the same slice is recorded; the paper counts direction\n    apart (VEN-to-PC and PC-to-VEN each 0 or 1 of 200, Results), so ordered pairs are the reading\n    its text gives. A connection is a uEPSP or uIPSP evoked by single presynaptic spikes in the\n    response averaged over more than 20 sweeps (Fig. 5f legend), uEPSPs at -70 mV and uIPSPs at\n    -60 mV (Methods). The paper and its code give no amplitude, latency or noise rule for calling\n    a connection, so the connections counted are those annotated, with two readings of the\n    annotation, (a) the dataset's own connection labels and (b) the ConnType annotations of the\n    code's metadata_multiPatch.xlsx, matched through file name and channels; each is run where it\n    exists, and when neither exists the claim is blocked as methods_underspecified. Whether the\n    code's \"OK\" quality connections count is not said; counted, with the count without them shown.\n    A detection from the traces themselves would be the author's rule and is shown only as a\n    variant that does not decide. Reproduced when all three counts are within tolerance under\n    every reading run; blocked as methods_underspecified when the readings disagree.\n- id: fig5-pc-to-pc\n  statement: PCs form monosynaptic connections with other PCs in 24 of 503 tested pairs (4.77%).\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5i;\n    Supplementary Table 5\n  quote: A breakdown of these connections by cell type revealed that PCs formed monosynaptic\n    connections with other PCs in 24 out of 503 tested pairs (Supplementary Table 5 )\n  expected:\n  - quantity: PC-to-PC connections\n    value: 24\n    tolerance: 2.4\n  - quantity: PC-to-PC pairs tested\n    value: 503\n    tolerance: 50\n  - quantity: PC-to-PC connection rate\n    value: 4.77\n    tolerance: 0.48\n    unit: percent\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: Pairs, connections and their readings as in fig5d-connectivity-totals; cell types\n    as the dataset labels them, or as metadata_multiPatch.xlsx labels them when the dataset does\n    not (identified by firing pattern and post hoc morphology, Methods). The rate is connections\n    over ordered pairs tested (24/503 = 4.77%, as in Fig. 5i). A connection is counted whatever\n    its sign, the reading the Results give (\"monosynaptic connections\"); the code's table marks\n    some PC-to-PC connections \"Inh\", and the count of excitatory ones alone is shown as a variant.\n    Reproduced when the three values are within tolerance under every reading run.\n- id: fig5-ven-outputs-absent\n  statement: VENs form no connections with adjacent VENs (0 of 110 pairs), with PCs (0 of 200) or\n    with interneurons (0 of 55).\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5g,i\n  quote: In contrast, VENs did not form synaptic connections with adjacent VENs (VEN-to-VEN, 0 of\n    110, 135.7 ± 60.0 μm) or with PCs (VEN-to-PC, 0 of 200, 119.3 ± 63.1 μm) ... However, no\n    synaptic connections were found between VENs and INs (VEN-to-IN, 0 of 55 and IN-to-VEN, 0 of\n    55\n  expected:\n  - quantity: VEN-to-VEN connections\n    value: 0\n    tolerance: 0\n  - quantity: VEN-to-VEN pairs tested\n    value: 110\n    tolerance: 11\n  - quantity: VEN-to-PC connections\n    value: 0\n    tolerance: 0\n  - quantity: VEN-to-PC pairs tested\n    value: 200\n    tolerance: 20\n  - quantity: VEN-to-IN connections\n    value: 0\n    tolerance: 0\n  - quantity: VEN-to-IN pairs tested\n    value: 55\n    tolerance: 5.5\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: As fig5-pc-to-pc. Counts are integers, so 10% of 0 is no tolerance; the connection\n    counts must be 0. The paper reports no test. The code's table annotates one VEN-to-PC\n    connection (slice 190315s2, VEN on channel 4 to PC on channel 6, \"Ext\", \"Excellent\"); the\n    notebook shows that pair's averaged response and says which reading counts it. Reproduced when\n    every value is within tolerance under every reading run.\n- id: fig5-pc-to-ven\n  statement: PCs rarely project to VENs, with one connection in 200 tested PC-to-VEN pairs (0.5%).\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5i\n  quote: Likewise, VENs received minimal local excitatory input, suggesting PCs rarely projected to\n    VENs (PC-to-VEN, 1 of 200, 119.3 ± 63.1 μm)\n  expected:\n  - quantity: PC-to-VEN connections\n    value: 1\n    tolerance: 0\n  - quantity: PC-to-VEN pairs tested\n    value: 200\n    tolerance: 20\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: As fig5-pc-to-pc. A count of 1 has no 10% tolerance; it must be 1. Reproduced when\n    both values hold under every reading run.\n- id: fig5-pc-in\n  statement: PCs and interneurons are connected in 2 of 65 PC-to-IN pairs (3.08%) and 4 of 65\n    IN-to-PC pairs (6.15%).\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5i\n  quote: This analysis identified six synaptic connections between L5 PCs and INs (PC-to-IN, 2 of\n    65 and IN-to-PC, 4 of 65, 107.0 ± 60.1 μm)\n  expected:\n  - quantity: PC-to-IN connections\n    value: 2\n    tolerance: 0\n  - quantity: PC-to-IN pairs tested\n    value: 65\n    tolerance: 6.5\n  - quantity: IN-to-PC connections\n    value: 4\n    tolerance: 0.4\n  - quantity: IN-to-PC pairs tested\n    value: 65\n    tolerance: 6.5\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: As fig5-pc-to-pc, with interneurons as the dataset labels them (or \"GABA\" in\n    metadata_multiPatch.xlsx). Counts of 2 and 4 have tolerances under 1, so they must match\n    exactly. Reproduced when all four values hold under every reading run.\n- id: fig5-in-to-ven-absent\n  statement: Interneurons make no connections onto VENs (0 of 55 pairs).\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2\n  quote: However, no synaptic connections were found between VENs and INs (VEN-to-IN, 0 of 55 and\n    IN-to-VEN, 0 of 55\n  expected:\n  - quantity: IN-to-VEN connections\n    value: 0\n    tolerance: 0\n  - quantity: IN-to-VEN pairs tested\n    value: 55\n    tolerance: 5.5\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: As fig5-pc-in. Reproduced when both values hold under every reading run.\n- id: fig5-pair-distances\n  statement: Tested pairs span a wide range of intersomatic distances, 111.8 ± 61.2 um (mean ±\n    s.d.) for PC-PC, 135.7 ± 60.0 um for VEN-VEN, 119.3 ± 63.1 um for VEN-PC, 107.0 ± 60.1 um for\n    PC-IN and 97.4 ± 36.8 um for VEN-IN.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2\n  quote: These connections spanned a wide range of soma distances (111.8 ± 61.2 μm, mean± s.d.).\n    In contrast, VENs did not form synaptic connections with adjacent VENs (VEN-to-VEN, 0 of 110,\n    135.7 ± 60.0 μm) or with PCs (VEN-to-PC, 0 of 200, 119.3 ± 63.1 μm)\n  expected:\n  - quantity: PC-PC distance, mean\n    value: 111.8\n    tolerance: 11.2\n    unit: um\n  - quantity: PC-PC distance, s.d.\n    value: 61.2\n    tolerance: 6.1\n    unit: um\n  - quantity: VEN-VEN distance, mean\n    value: 135.7\n    tolerance: 13.6\n    unit: um\n  - quantity: VEN-VEN distance, s.d.\n    value: 60.0\n    tolerance: 6.0\n    unit: um\n  - quantity: VEN-PC distance, mean\n    value: 119.3\n    tolerance: 11.9\n    unit: um\n  - quantity: VEN-PC distance, s.d.\n    value: 63.1\n    tolerance: 6.3\n    unit: um\n  - quantity: PC-IN distance, mean\n    value: 107.0\n    tolerance: 10.7\n    unit: um\n  - quantity: PC-IN distance, s.d.\n    value: 60.1\n    tolerance: 6.0\n    unit: um\n  - quantity: VEN-IN distance, mean\n    value: 97.4\n    tolerance: 9.7\n    unit: um\n  - quantity: VEN-IN distance, s.d.\n    value: 36.8\n    tolerance: 3.7\n    unit: um\n  depends_on:\n  - fig5d-connectivity-totals\n  criterion: The s.d. describes the spread of pairs, not an uncertainty of the mean, so each mean\n    and each s.d. gets 10% of its value, not the s.d. as tolerance. The paper does not say how the\n    distance was measured; readings, (a) the Euclidean distance between soma positions in the\n    slice plane and (b) in three dimensions where depth is recorded. It does not say which pairs\n    enter each value; for VEN-VEN, VEN-PC and VEN-IN, with no or one connection, only the tested\n    pairs can, so reading (i) is all tested pairs of the class (each unordered pair once, as\n    VEN-to-PC and PC-to-VEN share one value), and for PC-PC the Results say \"these connections\",\n    so reading (ii), the connected PC-PC pairs only, is also run. Reproduced when the values are\n    within tolerance under every reading run; blocked as methods_underspecified when readings\n    disagree; blocked as data_missing when the dataset holds no soma positions.\n- id: fig5i-ven-sparse-local-connectivity\n  statement: VENs have sparse synaptic interactions with the local circuit compared with PCs.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2; Figure 5i\n  quote: These findings suggest that VENs follow a distinct connectivity pattern characterized by\n    sparse synaptic interactions with local neuronal circuits compared with PCs (Fig. 5i ).\n  expected:\n  - quantity: PC-to-PC rate (Fig. 5i)\n    value: 4.77\n    tolerance: 0.48\n    unit: percent\n  - quantity: PC-to-IN rate (Fig. 5i)\n    value: 3.08\n    tolerance: 0.31\n    unit: percent\n  - quantity: PC-to-VEN rate (Fig. 5i)\n    value: 0.5\n    tolerance: 0.05\n    unit: percent\n  - quantity: IN-to-PC rate (Fig. 5i)\n    value: 6.15\n    tolerance: 0.62\n    unit: percent\n  depends_on:\n  - fig5-pc-to-pc\n  - fig5-ven-outputs-absent\n  - fig5-pc-to-ven\n  - fig5-pc-in\n  - fig5-in-to-ven-absent\n  criterion: The paper reports no test for this comparison; it rests on the counts. Reproduced\n    when the four Fig. 5i rates are within tolerance and every rate with a VEN at either end\n    (VEN-to-VEN, VEN-to-PC, PC-to-VEN, VEN-to-IN, IN-to-VEN) is below the PC rate of the same\n    partner class (PC-to-PC for the first three, PC-to-IN and IN-to-PC for the last two). A\n    Fisher exact test of each VEN rate against its PC rate is shown as a variant and does not\n    decide, since the paper uses none.\n- id: fig5fg-example-slice\n  statement: In the example slice of Fig. 5d-h (six cells, VEN, PC, PC, VEN, VEN, PC), PC cell 2\n    evokes uEPSPs in PC cell 6, and VEN cell 4 evokes no EPSP in any of the other cells.\n  source: Figure 5d-h\n  quote: f , Traces showing a PC-to-PC connection (from cell 2 to cell 6, bottom block) ... g ,\n    Similar to f . Testing of projections from a VEN (cell 4) to other neurons, with no evoked\n    EPSP detected.\n  criterion: The slice and channels come from the code (Fig5fg_plotConn.m and\n    Fig5e_plotConnexampleFPs.m), slice 20190315 s4 of subject Mfa190314, cells 1 to 6 on\n    channels 1, 2, 3, 6, 7 and 8, presynaptic files 20190315s4c2 (cell 2) and 20190315s4c6\n    (cell 4), test round 2 of each. The response is processed as in that script, resampled to\n    1 kHz, averaged over sweeps (more than 20, Fig. 5f legend) and low-passed with a 2nd-order\n    Butterworth at 300 Hz applied forward and backward (PatchAnaLab filter_300Lowpass). The paper\n    gives no rule for \"detected\"; the claim is judged on the same annotations as\n    fig5d-connectivity-totals (reproduced when the pair 2 to 6 is annotated as a connection and\n    no pair from cell 4 is), and the notebook prints, for each of the ten responses, the peak\n    deflection in the averaged trace after the presynaptic spike and the s.d. of the trace before\n    it, as a description that does not decide.\n- id: fig5-pc-rate-comparable-primate\n  statement: The PC-to-PC connection rate is comparable with the rate reported for layer 5 PCs in\n    the primate brain.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 2\n  quote: a connectivity rate comparable with previously reported for L5 PCs in the primate brain\n    50\n  data: with_inputs\n  depends_on:\n  - fig5-pc-to-pc\n  criterion: The reference is Seeman et al. 2018, eLife 7, e37349 (doi:10.7554/eLife.37349), on\n    mouse and human cortex. The paper prints neither the reference rate (which layer, species and\n    distance range) nor what \"comparable\" allows, so the comparison cannot be judged from the\n    paper; blocked as methods_underspecified, with the PC-to-PC rate of fig5-pc-to-pc reported.\n- id: fig5b-psc-frequency\n  statement: The frequencies of spontaneous and miniature EPSCs and IPSCs are lower in VENs than in\n    neighbouring PCs.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 1; Figure 5b\n  quote: The frequencies of both excitatory and inhibitory events were significantly lower in VENs\n    than in PCs (Fig. 5b )\n  data: elsewhere\n  where: DANDI:001752 (postsynaptic currents)\n  criterion: Per cell event frequency, sEPSC 8 VEN and 11 PC, sIPSC 7 and 8, mEPSC 8 and 8,\n    mIPSC 15 and 21 (Fig. 5b legend); events detected at \"the maximus root mean squared noise\n    level (5 pA)\" (Methods); two-tailed Wilcoxon rank-sum test per event type (legend), at\n    p < 0.05 (conventional; the panel's p-values were not readable). Reproduced when the VEN\n    median is lower with p < 0.05 for each type. Tested in full under the claims file of\n    DANDI:001752.\n- id: fig5c-psc-amplitude\n  statement: The amplitudes of spontaneous and miniature EPSCs and IPSCs do not differ\n    significantly between VENs and PCs.\n  source: Results, Altered connectivity profile of deep-layer AIC neurons, paragraph 1; Figure 5c\n  quote: whereas the amplitudes were not significantly different between VENs and PCs (Fig. 5c )\n  data: elsewhere\n  where: DANDI:001752\n  criterion: A claim of absence, judged on the paper's test, a two-tailed Wilcoxon rank-sum test\n    of per-cell mean amplitudes per event type (Fig. 5c legend), alpha 0.05 (conventional).\n    Reproduced when p >= 0.05 for each type, with the effect size reported.\n- id: scrna-classes\n  statement: The whole-cell scRNA-seq atlas of the macaque AIC holds 122,663 transcriptomes in four\n    classes, excitatory neurons (21,733, 17.8%), inhibitory neurons (17,007, 13.9%), glial cells\n    (83,283, 67.8%) and vascular cells (640, 0.5%).\n  source: Results, Transcriptomic landscape of the macaque AIC, paragraph 2; Figure 1b,c\n  quote: 'we categorized these cells into four main classes: excitatory neurons (21,733 cells,\n    17.8%), inhibitory neurons (17,007 cells, 13.9%), glial cells (83,283 cells, 67.8%) and vascular\n    cells (640 cells, 0.5%)'\n  data: elsewhere\n  where: GEO GSE319557 (10x scRNA-seq, FASTQ, per the Data availability statement); processed\n    data in Zenodo doi:10.5281/zenodo.18814764\n  expected:\n  - quantity: excitatory neurons\n    value: 21733\n    tolerance: 2173\n    unit: cells\n  - quantity: inhibitory neurons\n    value: 17007\n    tolerance: 1701\n    unit: cells\n  - quantity: glial cells\n    value: 83283\n    tolerance: 8328\n    unit: cells\n  - quantity: vascular cells\n    value: 640\n    tolerance: 64\n    unit: cells\n- id: scrna-78-types\n  statement: The four classes divide into 20 subclasses and 78 transcriptomic types, 34 inhibitory,\n    20 excitatory and 24 non-neuronal.\n  source: Results, Transcriptomic landscape of the macaque AIC, paragraph 2; Extended Data Figure\n    1e,f\n  quote: The four classes were divided into 20 subclasses and further subdivided into 78 molecularly\n    defined transcriptomic cell types, including 34 inhibitory and 20 excitatory neuron types, and\n    24 non-neuronal cell types\n  data: elsewhere\n  where: GEO GSE319557\n  criterion: Judged on the paper's cluster labels if the deposit carries them (counts of types per\n    class equal to those stated); a re-clustering with the Methods' pipeline (SCANPY, Harmony,\n    Leiden) has no stated resolution, so the number of clusters it gives cannot decide the claim.\n- id: patchseq-mapping\n  statement: Of 307 Patch-seq neurons with transcriptomes, 273 excitatory neurons map to 18 of the\n    20 excitatory types and 34 inhibitory neurons to 17 of the 33 inhibitory types.\n  source: Results, Patch-seq revealed extensive cellular heterogeneity in the primate AIC,\n    paragraph 1; Figure 1e\n  quote: 273 excitatory neurons mapped to 18 of the 20 excitatory types, while 34 inhibitory neurons\n    mapped to 17 of the 33 inhibitory types\n  data: elsewhere\n  where: GEO GSE319369 (Patch-seq); mapping results in github.com/RFLiu2021/AIC_proj at commit\n    44cd8a6, patchSeqMappingTo10X/\n  expected:\n  - quantity: excitatory Patch-seq neurons\n    value: 273\n    tolerance: 27\n  - quantity: inhibitory Patch-seq neurons\n    value: 34\n    tolerance: 3.4\n  - quantity: excitatory types with mapped Patch-seq neurons\n    value: 18\n    tolerance: 1.8\n  - quantity: inhibitory types with mapped Patch-seq neurons\n    value: 17\n    tolerance: 1.7\n- id: ven-map-et-ct\n  statement: The 29 morphologically identified VENs do not map to one molecular cluster; 14 map to\n    L5 ET and 15 to L5/6 CT.\n  source: Results, Patch-seq revealed extensive cellular heterogeneity in the primate AIC,\n    paragraph 2; Figure 2a\n  quote: 29 neurons that were morphologically identified as VENs did not map to a unique molecular\n    cluster; instead, they mapped to either L5 ET ( n = 14) or L5/6 CT ( n = 15)\n  data: elsewhere\n  where: GEO GSE319369\n  expected:\n  - quantity: VENs mapped to L5 ET\n    value: 14\n    tolerance: 1.4\n  - quantity: VENs mapped to L5/6 CT\n    value: 15\n    tolerance: 1.5\n- id: ven-firing-rate-variability\n  statement: VENs have lower firing rates and greater variability in spike timing than PCs.\n  source: Results, Patch-seq revealed extensive cellular heterogeneity in the primate AIC,\n    paragraph 3; Supplementary Tables 1 and 2\n  quote: Notably, VENs exhibit lower firing rate and greater variability in spike timing than PCs\n  data: elsewhere\n  where: DANDI:001746 (Patch-seq electrophysiology)\n  criterion: The paper's values and tests are in Supplementary Tables 1 and 2, not in the text\n    read, and the measure of spike-timing variability is not named in the text; blocked as\n    methods_underspecified unless they are supplied.\n- id: fig3c-ais-distance-length\n  statement: In Pan-Nav stained sections the AIS of VENs lies farther from the soma than that of\n    PCs, and VENs have a shorter AIS.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 2; Figure 3c\n  quote: showed that the AIS in VENs was, on average, located significantly farther from the soma\n    than in PCs (Fig. 3c ). Additionally, VENs had a shorter AIS than PCs.\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, morpho/dataMorph/AIScmp_PCvsVEN_Fig5c.xlsx\n  criterion: The legend names a two-way ANOVA (n = 108 VENs and 430 PCs, 23 slices, five animals)\n    without its factors; the readings are cell type with slice, and cell type with animal, as the\n    second factor. Reproduced when, under both, the cell-type effect is significant at p < 0.05\n    (conventional) for AIS distance (VEN larger) and AIS length (VEN shorter).\n- id: fig3e-phase-peak-index\n  statement: VENs have lower AP phase-plane peak indices than every PC type.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 3; Figure 3e\n  quote: The VENs had lower phase peak indices than any type of PCs (Fig. 3e )\n  data: elsewhere\n  where: DANDI:001746\n  criterion: Phase peak index (Psd - Pais)/(Psd + Pais) (Methods, Calculation of the phase peak\n    index). Kruskal-Wallis test followed by Dunn's test (Fig. 3e legend). Reproduced when the VEN\n    median is the lowest and Dunn's test separates VENs from each PC type at p < 0.05\n    (conventional).\n- id: fig4ac-ap-width-amplitude\n  statement: In 281 VENs and 306 L5 PCs, APs of VENs are broader and lower in amplitude.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 3; Figure 4a-c\n  quote: APs in VENs were broader and had a lower amplitude compared with L5 PCs (Fig. 4a-c )\n  statistics:\n  - test: two-tailed Wilcoxon rank-sum\n    p: 0.001\n    p_relation: \"<\"\n    n: 281 VENs and 306 PCs\n  data: elsewhere\n  where: DANDI:001746 (the paper does not say which dandiset holds these recordings)\n  criterion: AP amplitude and half-width of the first AP as in the Methods. Reproduced when the\n    VEN median width is larger and amplitude smaller, each with two-tailed Wilcoxon rank-sum\n    p < 0.001.\n- id: fig4d-sodium-current\n  statement: Somatic Na+ currents in outside-out patches are lower in VENs (n = 14) than in L5 PCs\n    (n = 21).\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 3; Figure 4d\n  quote: outside-out patch-clamp recording showed that the somatic Na + currents evoked in VENs ( n\n    = 14) were significantly lower than those of L5 PCs ( n = 21) (Fig. 4d )\n  data: elsewhere\n  where: DANDI:001750 (sodium channel currents)\n  criterion: Two-tailed Wilcoxon rank-sum (Fig. 4d legend). The Methods do not name the measure\n    compared; readings, (a) the largest peak inward current over the steps, per patch, and (b)\n    the same divided by the patch area estimated from its capacitance. Reproduced when, under both,\n    the VEN median is lower with p < 0.05 (conventional).\n- id: fig4i-peak-index-ais-distance\n  statement: The phase peak index decreases linearly with AIS distance from the soma in the VEN\n    model, and this relation closely matches the one in real neurons.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 4; Figure 4i\n  quote: 'the linear decrease in the phase peak index with increasing AIS distance observed in the\n    VEN model closely matched the experimental data (Fig. 4i , ANCOVA: F(1, 93) = 1.07, P = 0.5729\n    for intersection, P = 0.0031 for slope)'\n  statistics:\n  - about: ANCOVA, model against real neurons, intercept\n    test: ANCOVA\n    statistic: F(1, 93) = 1.07\n    p: 0.5729\n  - about: ANCOVA, slope\n    test: ANCOVA\n    p: 0.0031\n  - about: slope in the simulated VEN model\n    test: two-tailed Student's t-test\n    p: 0.0015\n  - about: slope in real neurons\n    test: two-tailed Student's t-test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 62 neurons\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling); Zenodo\n    doi:10.5281/zenodo.18814764\n  criterion: Reproduced when the slope is negative with two-tailed t-test p < 0.05 in the model\n    and in real neurons, and the ANCOVA intercept term gives p >= 0.05. What the ANCOVA slope P\n    tests is not said (common slope against zero, or difference of slopes); it is reported under\n    both readings and does not decide.\n- id: fig4g-model-ais-distance-ap-shape\n  statement: In the VEN model, moving the AIS farther from the soma makes APs wider and smaller and\n    the phase-plane plot more saddle-like; this effect is not replicated in the PC model.\n  source: Results, The AIC evolved a neural signal-processing strategy, paragraph 4; Figure 4g,h;\n    Extended Data Figure 7b\n  quote: Crucially, simulating an increase in the distance of the AIS from the soma in the VEN\n    model led to APs being wider and smaller in amplitude\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling); Zenodo\n    doi:10.5281/zenodo.18814764\n  criterion: Simulations as in the Methods (Computational model), AIS distance 0 to 170 um in the\n    VEN model and hillock length 0 to 70 um in the PC model. Reproduced when, in the VEN model, AP\n    amplitude falls and width rises with AIS distance, each slope with two-tailed t-test p < 0.05\n    (Extended Data Fig. 7b legend), and in the PC model amplitude does not fall.\n- id: fig4j-eepsp-latency\n  statement: Latencies of eEPSPs evoked by deep-layer stimulation do not differ between paired VENs\n    and PCs (5.13 and 5.02 ms).\n  source: Results, VENs respond robustly to deep-layer synaptic input, paragraph 1; Figure 4j\n  quote: 'The postsynaptic response latencies were similar between VENs and PCs (5.13 ± 0.29 ms for\n    VENs and 5.02 ± 0.30 ms for PCs, two-tailed paired t -test: P = 0.8941)'\n  statistics:\n  - test: two-tailed paired t-test\n    p: 0.8941\n    n: 26 VEN and PC pairs\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, ephysio/data_ephy/sumData_StimWM.xlsx\n    (the paper does not say which dandiset holds the raw recordings)\n  expected:\n  - quantity: VEN latency\n    value: 5.13\n    tolerance: 0.29\n    unit: ms\n  - quantity: PC latency\n    value: 5.02\n    tolerance: 0.30\n    unit: ms\n  criterion: A claim of absence, judged on the paper's two-tailed paired t-test at alpha 0.05;\n    reproduced when p >= 0.05, with the mean difference reported. Tolerances are the stated s.e.m.\n- id: fig4j-eepsp-amplitude\n  statement: eEPSP amplitudes are higher in VENs than in adjacent PCs, with effects of cell type\n    and stimulation level in an ANOVA.\n  source: Results, VENs respond robustly to deep-layer synaptic input, paragraph 1; Figure 4j\n  quote: whereas the response amplitudes in VENs were significantly higher than those in adjacent\n    PCs (analysis of variance (ANOVA), P = 0.0034 for cell type and P < 0.001 for stimulation level\n  statistics:\n  - about: cell type\n    test: ANOVA\n    p: 0.0034\n    n: 26 VEN and PC pairs\n  - about: stimulation level\n    test: ANOVA\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, ephysio/data_ephy/sumData_StimWM.xlsx\n  criterion: Two-way ANOVA of amplitude on cell type and stimulation level. Reproduced when VEN\n    amplitudes are higher and the cell-type effect has p < 0.05 (conventional).\n- id: model-ven-fires-more\n  statement: In simulations, the VEN model fires more than the PC model to the same synaptic input\n    trains, and a distal axon origin raises the somatic response to distal basal inputs.\n  source: Results, VENs respond robustly to deep-layer synaptic input, paragraph 2; Figure 4k,l\n  quote: VEN fired more robustly than PC to the same synaptic input trains (Fig. 4k ), and the\n    distal origin of the axon facilitates the somatic response to the distal basal dendritic\n    inputs (Fig. 4l )\n  data: elsewhere\n  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6 (VEN_modeling); Zenodo\n    doi:10.5281/zenodo.18814764\n  criterion: Reproduced when, across input frequencies of 200 to 1,100 Hz (Methods), the VEN\n    model's firing rate exceeds the PC model's, and the VEN model with AIS D = 70 um fires more\n    than with AIS D = 0 um.\n- id: fig6-ven-subtype-morphology\n  statement: VEN-L has a larger basal dendritic arborization than L5 PCs, VEN-S an intermediate one\n    similar to PCs; the axon origin lies farther from the soma in both VEN subtypes than in PCs,\n    with no difference between VEN-L and VEN-S.\n  source: Results, Multimodal profiling of two VEN subtypes, paragraph 1; Figure 6c-e\n  quote: VEN-L had larger basal dendritic arborization than L5 PCs, whereas VEN-S had\n    intermediate-sized basal dendrite arborization similar to PCs ... the distance from the axon\n    originating site to the soma was significantly greater in both VEN subtypes compared with PCs\n    (Fig. 6e ), with no significant difference observed between VEN-L and VEN-S\n  data: elsewhere\n  where: NeuroMorpho.org doi:10.13021/y4be-0p18 (morphologies, ASC)\n  criterion: Two-tailed Wilcoxon rank-sum tests with Benjamini-Hochberg FDR (Fig. 6d,e legend),\n    n = 38 VEN-L, 34 VEN-S, 85 PCs for basal height and field size, and 36, 20 and 74 for axon\n    distance. Reproduced when VEN-L basal field exceeds PCs at FDR < 0.05, VEN-S does not differ\n    from PCs, both subtypes exceed PCs in axon distance at FDR < 0.05, and VEN-L against VEN-S\n    gives FDR >= 0.05.\n- id: fig6f-g-ven-subtype-mapping\n  statement: VEN-Ls map to L5 ET (Exc FEZF2 DSG2, n = 10) and VEN-Ss to L5/6 CT (Exc FEZF2\n    COL24A1, n = 11), where they fall in the subcluster COL24A1 POC5 apart from canonical L5/6 CT\n    neurons.\n  source: Results, Multimodal profiling of two VEN subtypes, paragraph 2; Figure 6f,g\n  quote: the morphologically defined VENs mapped to L5 ET (Exc FEZF2 DSG2) were VEN-Ls ( n = 10),\n    while those VENs mapped to L5/6 CT (Exc FEZF2 COL24A1) were VEN-Ss ( n = 11)\n  data: elsewhere\n  where: GEO GSE319369 and GSE319557\n  expected:\n  - quantity: VEN-L\n    value: 10\n    tolerance: 1\n  - quantity: VEN-S\n    value: 11\n    tolerance: 1.1\n- id: fig6h-subtype-markers\n  statement: VEN-L expresses markers such as DSG2, HAPLN4, TOX2, TRPC4, CAMK1G and TAGLN2; VEN-S\n    expresses ATP8A2, POC5 and SEMA3E.\n  source: Results, Multimodal profiling of two VEN subtypes, paragraph 2; Figure 6h\n  quote: VEN-L expressed markers such as DSG2, HAPLN4, TOX2, TRPC4, CAMK1G and TAGLN2 , whereas\n    VEN-S showed high expression of ATP8A2, POC5 and SEMA3E\n  data: elsewhere\n  where: GEO GSE319557 and GSE319369\n  criterion: SCANPY Wilcoxon differential expression (Methods, Enrichment marker genes). The\n    Methods give two levels, (a) significant marker genes, log fold change > 1 and FDR < 0.05, and\n    (b) enriched marker genes, among the top 50 and meeting the four expression criteria listed;\n    the text does not say which the named genes meet. Reproduced when each named gene passes for\n    its subtype under both; blocked as methods_underspecified when they disagree.\n- id: ven-subtypes-similar-physiology\n  statement: VEN-L and VEN-S have similar physiological properties.\n  source: Results, Multimodal profiling of two VEN subtypes, paragraph 2; Extended Data Figure 9c,d;\n    Supplementary Table 8\n  quote: Despite their distinct morphological and transcriptomic profiles, both VEN subtypes\n    exhibited similar physiological properties (Extended Data Fig. 9 and Supplementary Table 8 )\n  data: elsewhere\n  where: DANDI:001746\n  criterion: A claim of absence, judged on the paper's test, two-tailed Wilcoxon rank-sum with\n    Benjamini-Hochberg FDR (Extended Data Fig. 9c,d), on AP width and amplitude of 85 VEN-L and\n    41 VEN-S. Reproduced when neither is significant at FDR 0.05. The other features are in\n    Supplementary Table 8, not read.\n- id: fig7c-tau-rna-distance\n  statement: Across pairs of projection neuron types, distances in membrane time constant\n    correlate with transcriptomic distances (r = 0.53).\n  source: Results, Transcriptomic distinctions underlie phenotypic variation, paragraph 1; Figure\n    7a-c\n  quote: Pooling the pairs across all clusters revealed a high correlation ( r = 0.53) between the\n    membrane time constant (tau) distances and RNA distances (Fig. 7a–c )\n  data: elsewhere\n  where: GEO GSE319557; DANDI:001746\n  expected:\n    quantity: Pearson r, tau distance against RNA distance\n    value: 0.53\n    tolerance: 0.053\n  criterion: Transcriptomic distance from the Pearson correlation of mean log2(x + 1) counts over\n    the 500 most-variable genes, tau distance as the Euclidean distance between type means\n    (Methods, Variability analysis of transcriptomic neuron types); Pearson r over all pairs. The\n    transcriptomic distance is taken as 1 - r, the reading under which a positive r between\n    distances is possible.\n- id: fig8a-metabolite-gradient\n  statement: Of 581 metabolites, 228 differ between AIC and V1 and only 108 between AIC and\n    parietal cortex.\n  source: Results, Cortical metabolomics reveals a glycolytic bias of the AIC, paragraph 1; Figure 8a\n  quote: we identified 228 differentially abundant metabolites between the AIC and V1 (Welch's\n    ANOVA test followed by Games–Howell test, P < 0.05) compared with only 108 between the AIC and\n    PrC\n  data: elsewhere\n  where: MetaboLights MTBLS13927\n  expected:\n  - quantity: differential metabolites, AIC against V1\n    value: 228\n    tolerance: 23\n  - quantity: differential metabolites, AIC against PrC\n    value: 108\n    tolerance: 11\n  criterion: Welch's ANOVA followed by Games-Howell at P < 0.05 per metabolite (a selection\n    threshold), on 6 AIC, 6 PrC and 7 V1 samples from three animals (Fig. 8 legend).\n- id: fig8de-glycolytic-bias\n  statement: Compared with V1, AIC shows elevated citrate, reduced 2-ketobutyrate and increased\n    glutamate, read as a glycolytic bias.\n  source: Results, Cortical metabolomics reveals a glycolytic bias of the AIC, paragraphs 3 and 4;\n    Figure 8d,e\n  quote: AIC cells displayed elevated citrate and reduced 2-ketobutyrate levels, along with\n    increased glutamate\n  data: elsewhere\n  where: MetaboLights MTBLS13927\n  criterion: Welch's ANOVA followed by Games-Howell test (Fig. 8 legend). Reproduced when citrate\n    and glutamate are higher and 2-ketobutyrate lower in AIC than in V1 at P < 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001751/10.1038-s41556-026-02009-4.yaml paper/10.1038-s41556-026-02009-4.txt; echo rc=$?; python3 - <<'EOF'
import yaml,re
p='claims/001751/10.1038-s41556-026-02009-4.yaml'
txt=open(p).read()
# detect plain scalars with ': ' : look at lines not starting a key that contain ': '
for i,l in enumerate(txt.splitlines(),1):
    if l.lstrip().startswith('#'): continue
    s=l.strip()
    m=re.match(r"^(- )?[a-z_]+: (.*)$",s)
    rest = m.group(2) if m else s
    if rest.startswith(("'",'"')): continue
    if ': ' in rest: print(i,l)
for w in ['—','rather']:
    for i,l in enumerate(txt.splitlines(),1):
        if w in l: print('BAD',w,i,l)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001751/10.1038-s41556-026-02009-4.yaml",
 "old_string": "  statement: Tested pairs span a wide range of intersomatic distances, 111.8 ± 61.2 um (mean ±\n    s.d.) for PC-PC, 135.7 ± 60.0 um for VEN-VEN, 119.3 ± 63.1 um for VEN-PC, 107.0 ± 60.1 um for\n    PC-IN and 97.4 ± 36.8 um for VEN-IN.",
 "new_string": "  statement: PC-PC connections span a wide range of soma distances, 111.8 ± 61.2 um (mean ± s.d.);\n    the distances given for the other classes are 135.7 ± 60.0 um for VEN-VEN, 119.3 ± 63.1 um for\n    VEN-PC, 107.0 ± 60.1 um for PC-IN and 97.4 ± 36.8 um for VEN-IN."
}
```

```
The file claims/001751/10.1038-s41556-026-02009-4.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001751/10.1038-s41556-026-02009-4.yaml paper/10.1038-s41556-026-02009-4.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001751/10.1038-s41556-026-02009-4.yaml`. The quote checker reports 33 claims, 33 quotes, 8 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record from Europe PMC (PMC13457102): main text, figure and Extended Data legends, Methods, and the Data and Code availability statements. There was no PDF, so values printed only inside figures could not be read. The Supplementary Information (Supplementary Figs. 1–17 and Tables 1–12) and the Source Data were not in the text. Supplementary Table 5 holds the connectivity pair counts, but every count the claims rest on is also printed in the Results and the Fig. 5 legend, so I went ahead. That matches what the 001752 reader did with the same text.

**Code read.**
- github.com/RFLiu2021/AIC_proj at commit 44cd8a6. It has the plotting scripts for the Fig. 5e–g example and a per-pair table, `metadata_multiPatch.xlsx`, listing cell types and connection annotations.
- PatchAnaLab 1.0 (Zenodo 19995355), the paper's analysis package, which holds the 300 Hz low-pass filter the Fig. 5f plotting script uses.
- No code in either one detects a connection.

**Claims.**
- **10 claims** are on this dataset (Fig. 5d–i):
  - the totals (1,292 pairs, 377 neurons, 31 connections);
  - PC-to-PC (24 of 503, 4.77%);
  - VEN outputs absent (0 of 110, 0 of 200, 0 of 55);
  - PC-to-VEN (1 of 200);
  - PC and IN connections (2 and 4 of 65);
  - IN-to-VEN absent (0 of 55);
  - soma distances;
  - VENs sparsely connected compared with PCs;
  - the example slice of Fig. 5f,g;
  - "comparable" to the reported primate L5 rate, which uses outside data (`with_inputs`).
- **23 claims** have data elsewhere, covering the paper's other main findings (DANDI 001746/001750/001752, GEO, MetaboLights, NeuroMorpho, the code repository).
- All 33 have quotes; 7 carry statistics (8 values) and 26 have criteria.

**Details the paper leaves open, with the readings named:**
- **What counts as a connection.** Neither the paper nor the code gives an amplitude, latency or noise rule. The readings are (a) the dataset's own labels and (b) the code table's annotations. A detection from the traces is shown only as a variant that does not decide. Whether the code's "OK"-quality connections count is not said; they are counted, and the count without them is shown.
- **Pair counting.** The text supports ordered (directional) pairs, since VEN-to-PC and PC-to-VEN are counted separately. The listed types sum to 1,253; the remaining 39 are not stated, and the code table has 39 IN-to-IN pairs.
- **Sign of PC-to-PC connections.** All connections are counted; excitatory-only is a variant, because the code table marks 7 PC-to-PC connections "Inh".
- **Soma distance.** Two measures: in the slice plane, or in 3D. Two pair sets: all tested pairs of the class, or, for PC-PC, only connected pairs, since the text says "these connections".
- **"Comparable" to Seeman et al. 2018.** The paper prints no reference rate, so this claim is blocked as `methods_underspecified`.
- **Sparse connectivity.** The paper reports no test, so the claim is judged on the counts and their direction. A Fisher exact test is a variant only.

**Disagreements between the code and the paper,** recorded in the opening comment:

| | Code table | Paper |
|---|---|---|
| Tested pairs | 1,416 | 1,292 |
| Cells | 298 | 377 |
| Subjects | 6 | 20 (all whole-cell and connectivity work) |
| Annotated connections | 26 | 31 |
| PC-to-PC connections | 18 | 24 |
| VEN-to-PC connections | 1 (slice 190315s2, channel 4 to 6) | 0 |

The table's `Nr_Conn` column also disagrees with its own annotations in 6 slices, and one row carries a projection label that does not match its channels.

**Missing from the paper:** the Supplementary Information and Source Data. Claims that need them (spike-timing variability, the sex-difference test, the per-feature tables) say so in their criteria.

## End of run

35 turns, 7 minutes, result: success.
