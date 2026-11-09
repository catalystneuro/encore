# 001773 · claims · run 39627656093

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001773 claims/001453 paper/ 2>&1; git show --stat HEAD HEAD~1 | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001773/claims-report.md transcripts/001773/claims-check-report.md; head -60 paper/*.txt; wc paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -30 paper/*.txt; wc paper/*.txt; which pdftotext; python -c "import fitz" 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; wc -lc *.txt; fold -s -w 200 *.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; grep -n "Supplementary\|SUPPLEMENT\|=====\|-----" *.txt | cut -c1-200 | head -40
```

```
2362 186673 10.1038-s41593-026-02301-4.txt
3109 /tmp/claude-1001/p.txt
6:------------------------------------------------------------------------
7:pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 133375
189:Supplementary information
194:Supplementary Methods 
339:Supplementary Method References 
421:Supplementary Table 1 
569:Supplementary Table 2 
666:Supplementary Table 3 
927:Supplementary Table 4 
1188:Supplementary Table 5 
1500:Supplementary Table 6 
1704:Supplementary Table 7 
1828:Supplementary Table 8 
1928:Supplementary Table 9 
1989:Supplementary Table 10 
2105:Supplementary Table 11
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 400
}
```

```
File content (29721 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 250
}
```

```
1	DOI: 10.1038/s41593-026-02301-4
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement PDF(s), extracted with PyMuPDF (dehyphenated, NFKC)
6	------------------------------------------------------------------------
7	pmc Nat Neurosci Nat Neurosci 981 npgopen 9809671 Nature Neuroscience 1097-6256 1546-1726 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC13337501 PMC13337501.1 13337501 
8	13337501 42225897 10.1038/s41593-026-02301-4 2301 1 Article Deep brain stimulation induces white matter remodeling and functional changes to brain-wide networks http://orcid.org/0000-0003-2374-3002 
9	Fujimoto Satoka H. [removed: an e-mail address] 1 2 7 http://orcid.org/0000-0002-1621-2003 Fujimoto Atsushi 1 2 7 http://orcid.org/0000-0001-5735-4369 Elorette Catherine 1 2 Seltzer Adela 1 2 Andraka Emma 1 2 
10	http://orcid.org/0009-0006-4539-9301 Herbert Keondre 1 2 Verma Gaurav 3 4 Janssen William G. M. 1 Fleysher Lazar 4 Folloni Davide 1 2 http://orcid.org/0000-0002-6446-0677 Choi Ki Sueng 3 4 Russ Brian 
11	E. 1 5 6 http://orcid.org/0000-0002-1672-2716 Mayberg Helen S. 1 3 http://orcid.org/0000-0002-1411-7555 Rudebeck Peter H. [removed: an e-mail address] 1 2 1 https://ror.org/04a9tmd77 grid.59734.3c 0000 
12	0001 0670 2351 Nash Family Department of Neuroscience and Friedman Brain Institute, Icahn School of Medicine at Mount Sinai, New York, NY USA 2 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 
13	2351 Lipschultz Center for Cognitive Neuroscience, Icahn School of Medicine at Mount Sinai, New York, NY USA 3 https://ror.org/031e8jz65 grid.430600.1 0000 0004 0431 8956 Nash Family Center for 
14	Advanced Circuit Therapeutics, Mount Sinai West Hospital, New York, NY USA 4 https://ror.org/04a9tmd77 grid.59734.3c 0000 0001 0670 2351 BioMedical Engineering and Imaging Institute, Icahn School of 
15	Medicine at Mount Sinai, New York, NY USA 5 https://ror.org/01s434164 grid.250263
[... 235 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 250,
 "limit": 250
}
```

```
250	functional changes observed following SCC-DBS are not attributable to the effects of DBS lead insertion alone and thus underscores the specific role of chronic stimulation in driving structural and 
251	functional changes in the brain. Discussion The present results indicate that SCC-DBS is associated with focal white matter structural remodeling in the MCC-CB (Figs. 2 and 3 ) as well as a 
252	brain-wide shift in the functional connectivity patterns across multiple networks (Figs. 4 and 5 ). These stimulation-induced changes could not be explained by the alterations associated with 
253	implantation of the DBS lead alone (Fig. 6 ). Our results highlight the potential role of white matter plasticity in the efficacy of DBS therapies for psychiatric and neurological disorders. DBS 
254	induced changes in white matter macro- and microstructure Prior work has shown that white matter remodeling can be induced by electrical, optogenetic or chemogenomic stimulation of neurons in gray 
255	matter 28 – 30 . Our data reveal that DBS targeted to white matter induces both macro- and micro-structual changes in white matter in the CB distal to the site of stimulation. This pattern of results 
256	complements prior studies that have pointed to a role for white matter dysfunction as contributing to the pathophysiology of depression 31 – 33 . Notably, abnormal white matter integrity in the CB 
257	was recently found to be positively correlated with symptom severity in patients with treatment-resistant depression 13 . In this context, our observation that SCC-DBS selectively induces white 
258	matter remodeling in the CB provides additional evidence that inducing structural plasticity in this tract may be a key mechanism through which DBS for depression mediates its therapeutic effects and 
259	results in sustained recovery over years with ongoing stimulation 8 . Surprisingly, only the CB exhibited a change in white matter integrity following SCC-DBS, despite chronic stimulation 
[... 240 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 500,
 "limit": 160
}
```

```
500	stimulated SCC changes, the second row is the result of monkey N, and the third row is the result of monkey T. Green circles indicate the location of the stimulated contact of the SCC-DBS lead. The 
501	bottom row is the result of non-surgical control group. Extended Data Fig. 9 Functional connectivity with stimulated SCC changes induced by SCC-DBS in brain network hubs. A ) The functional 
502	connectivity between stimulated SCC and 17 nodes per hemisphere included in the six brain networks. Colored bars are the mean value of functional connectivity normalized z-score between stimulated 
503	SCC and each brain network ROI hub in the stimulated hemisphere (red for the DMN hubs, cyan for SCC (area 25 and area 32), blue for the limbic network (LIM) hubs, yellow for the salience network 
504	(SAN) hubs, green for the central executive network (CEN) hubs, purple for the sensorimotor network (SMN) hubs and pink for the visual network (VIS) hubs. SCC, dACC and PCC were counted as hubs for 
505	the LIM (blue hubs) as well). These colors are matched with the ROI color in the centered brain image. The gray bars show the mean functional connectivity with SCC in the control hemisphere. Lighter 
506	color or lighter gray bars indicate pre-DBS functional connectivity z-score and the darker color or darker gray bars represent post-DBS scores. The gray circle represents monkey N and the gray 
507	triangle represents monkey T. Error bars show SEM. Bars represent the mean value of functional connectivity computed from voxel-wise measurements in each target ROI (brain network node ROI), pooled 
508	across two monkeys. Number of voxel-wise measurements (n) are shown in Supplementary Table 8 . FC values were compared using 3-way ANOVA. Statistical comparisons assessed differences between pre- and 
509	post-DBS conditions within each hemisphere (stimulated or control) and target ROI. All tests were two-sided. Tukey–Kramer post-hoc methods to corrected for multiple comparisons. There
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "Supplementary Methods \|Supplementary Table" $TMPDIR/p.txt | head;
```

```
139:differences between pre and post conditions. All tests were two-sided. P values are provided in Supplementary Table 1 (DBS group) and Supplementary Table 2 (nonsurgical control group). Effect sizes 
140:(rank–biserial correlation, r rb ) are shown Supplementary Table 3 (DBS group) and Supplementary Table 4 (nonsurgical control group). Colors represent significant negative (blue) and positive changes 
351:reconstructed the CB, UF and FM separately using probabilistic tractography (FSL’s ProbtrackX) 58 applied to preprocessed pre-DBS DWIs 59 (see Supplementary Methods 1 for DWI preprocessing). 
354:tractography studies 16 , 59 – 65 (Supplementary Methods 2 ). Each tract was log-transformed to account for the exponential decrease of visitation probability with distance and normalized by dividing 
367:provided in Supplementary Methods 3 . Lead placement was confirmed by high-resolution CT (0.5 mm isotropic CT, Force CT, Siemens Healthineers) 2 weeks after implantation. CT images were then aligned 
394:atlas 70 , CHARM atlas 72 and SARM atlas 77 (described in Supplementary Methods 4 ). We calculated the Fisher’s Z -transformed Pearson’s correlation between the average time series of the seed ROI 
410:in Supplementary Methods 5 . Free-floating immunohistochemistry was performed on four serial coronal sections per animal, spaced 750 μm apart for monkey N and 790 μm apart for monkeys T and D, 
427:coronal sections of monkeys N and T, adjacent to those used for immunofluorescence, and prepared for electron microscopy (Supplementary Methods 6 ). Using adjacent sections ensured that myelin 
437:and code availability are available at 10.1038/s41593-026-02301-4. Supplementary information Supplementary Information Supplementary Methods and Tables 1–11. Reporting Summary Source data Source Data 
453:(bottom). Each FA value represents voxel-wise measurements, collected from two monkeys. Number of voxel-wise measurements (n) are shown in Supplementary Table 5 (CB), Supplementary
[... 1 more lines not kept]
```

**Agent**

The supplement is in the original file from line 189; I'll read it there.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02301-4.txt",
 "offset": 185,
 "limit": 240
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-026-02301-4.txt",
 "offset": 424,
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; sed -n 426,565p $f | awk 'NR%2==1' | grep -vc "^ *$"; sed -n 573,662p $f | awk 'NR%2==1' | wc -l; sed -n 666,940p $f | tr '\n' ' ' | head -c 5000
```

```
70
45
Supplementary Table 3  Effect size (rank-biserial correlation, r_rb) for Fig. 4B, DBS group      ROI r_rb ROI r_rb ROI r_rb area_25 -0.16393 area_12m/o -0.10656 MLThal -0.2623 PCC -0.14754 OFa-p -0.19672 PNThal -0.39344 RSC -0.47541 OLF -0.2623 CbThal -0.44262 area_10 -0.40984 cl_OFC 0.065574 SpThal -0.42623 STGr 0.016393 caudal_vlPF -0.04098 LP -0.2459 STGc -0.36066 V6 -0.18852 LD -0.22951 area_32 0.114754 V6A -0.29508 Pul -0.72131 area_24 0.213115 area_5 0.377049 DLG -0.52459 MCC 0.295082 vm_IPS 0.278689 MG -0.77049 paraHipp -0.04098 lat_IPS 0.278689 Pi 0.081967 ERh -0.2541 MST 0.229508 Hb -0.2459 PRh 0.032787 area_7_in_I 0.327869 PrT -0.18033 area_8A -0.06557 area_7m 0.098361 Co -0.70492 area_8B -0.27869 Cl 0.081967 PAGR -0.22951 rostral_dlP -0.08197 En -0.09836 TgMid -0.45082 rostral_vlP 0.131148 Pir -0.11475 RtMid -0.4918 Ins/Pi 0.081967 HF -0.35246 OC+ -0.19672 Ri 0.245902 f -0.19672 raphe_Mid -0.62295 SI 0.442623 vpAmy -0.52459 R+ -0.22951 SII 0.319672 lpAmy 0.016393 DA_Mid -0.62295 SMA/preSMA 0.491803 stAmy -0.16393 PBC -0.42623 M1 0.590164 mAmy -0.42623 LGR -0.40984 PM 0.131148 pdAmy -0.36066 tgPons -0.63934 MT 0.295082 DStr 0.122951 ll+ -0.36066 V4 -0.04918 VStr -0.11475 retPons -0.52459 V3 -0.09836 Pd 0.04918 SO/ml -0.0082 V2 -0.16393 BR -0.14754 Pn+ -0.34426 V1 -0.31148 ST -0.16393 wmCB -0.2623 TGa -0.2459 SDBR -0.16393 DCb -0.04918 TGg/TGd 0 opt -0.57377 Fl-PFl -0.2459 TEO -0.2459 POR -0.09836 VCbCx -0.77049 gyral_TE -0.03279 MTHy -0.02459 ICbCx -0.34426 TE_in_STSv -0.29508 VTHy -0.44262 LCbCx -0.31148 STSf -0.29508 DTHy -0.40984 VCC -0.36066 STSd -0.29508 DPHy -0.21311 C5 -0.27869 lat_belt -0.01639 VPHy -0.57377 SVC -0.40164 med_belt 0.065574 ZI-H -0.13934 MedMC -0.42623 RTp 0 Rt -0.2459 MedRet -0.04918 core 0.098361 A+ -0.44262 MedRaphe 0.467213 area_14 -0.36066 ILThal -0.52459 PreCbMed -0.39344 areas_11/13 -0.21311 MD -0.5082 vmt 0.459016 DBS group DBS group DBS group  === page 13 === Supplementary Table 4  Effect size (rank-biserial correlatio
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; diff <(sed -n 666,926p $f | grep -v "group\|Table\|===") <(sed -n 927,1187p $f | grep -v "group\|Table\|===") | head; sed -n 1188,1200p $f; sed -n 1820,2362p $f | tr '\n' ' ' | head -c 9000
```

```
254a255,257
> Non-surgical Control
> Non-surgical Control
> Non-surgical Control
Supplementary Table 5 
Sample size for Fig. E4A (CB) 
 
 
 
 
mkN
Zaxis_s
sample size (n)
mkN
Zaxis_c_s sample size (n)
mkT
Zaxis3_s
-28.7537 7 -30.977 5 -27.2537 2  === page 17 === Supplementary Table 8  Sample size for Fig. E9A      ROI  Pre-DBS Sim side  Post-DBS Sim side  Pre-DBS Ctrl side  Pre-DBS Ctrl side  PCC  249  249  249  249  vmFC  109  109  109  109  STG  499  499  499  499  Anterior-dorsal Insula  100  100  100  100  dACC  162  162  162  162  DLPFC  766  766  766  766  PPC  336  336  336  336  Area 25  18  18  18  18  Area 32  48  48  48  48  MCC  101  101  101  101  HIP  132  132  132  132  AMY  111  111  111  111  Sensory Cx  692  692  692  692  Motor Cx  446  446  446  446  SMA  101  101  101  101  Visual Cx  1161  1161  1161  1161  MT  56  56  56  56           === page 18 === Supplementary Table 9  P value for Fig. E9  ROI  Stimulation side  Control side  PCC  8.22E-12  4.03E-07  vmFC  0  0  STG  0  0  Anterior-dorsal Insula  4.42E-08  0.029284354  dACC  4.75E-04  0  DLPFC  0  0  PPC  0.999983327  0.11576317  Area 25  0  0  Area 32  2.44E-13  0  MCC  0.991825378  0.999989453  HIP  1.19E-05  0.01848539  AMY  7.70E-06  0.999989453  Sensory Cx  0  0  Motor Cx  0.999909913  0.999125683  SMA  0.999989453  0.999989453  Visual Cx  0.999989453  0.999984425  MT  0.998895555  7.85E-07         === page 19 === Supplementary Table 10  P value for Fig. E10 C        Area p value area_25 1.4 ×10^-08 PCC 2.1 ×10^-05 RSC 7.0 ×10^-06 area_10 1.9 ×10^-07 STGr 2.1 ×10^-18 STGc 1.3 ×10^-12 ERh 1.4 ×10^-08 PRh 1.3 ×10^-12 area_8B 7.0 ×10^-06 rostral_dlPFC 6.8 ×10^-07 SII 3.3 ×10^-09 V3 1.5 ×10^-04 TGa 1.2 ×10^-06 TGg/TGd 5.9 ×10^-15 gyral_TE 7.7 ×10^-10 TE_in_STSv 1.3 ×10^-12 STSf 7.0 ×10^-06 STSd 1.3 ×10^-12 lat_belt 3.5 ×10^-11 med_belt 5.3 ×10^-08 RTp 1.2 ×10^-16 core 6.8 ×10^-07 area_14 2.4 ×10^-04 areas_11/13 7.7 ×10^-10 OLF 1.7 ×10^-10 cl_OFC 6.9 ×10^-12 V6 5.3 ×10^-08 MST 1.7 ×10^-10 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -150 claims/001453/*.yaml; grep -n "^  - id\|^[a-z_]*:" claims/001453/*.yaml | head -40; ls claims | head; ls claims | wc -l
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
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
ls tools schemas 2>/dev/null; grep -rn "elsewhere\|where:" claims/*/*.yaml | head -5; sed -n 1,60p tools/claims_check.py
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
papers_manifest.py
progress.py
readme_row.py
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:6000])"
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
python -c "import json; d=json.load(open('schemas/claims.schema.json')); print(json.dumps(d['\$defs'],indent=1))"
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

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001773/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001773/versions/0.260416.1939/" | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; sed -n 666,926p $f | grep -v "group\|Table\|===\|ROI\|r_rb\|^ *$" | awk 'NR%2==1' | wc -l; sed -n 1188,1830p $f | tr '\n' ' ' | head -c 1500
```

```
123
Supplementary Table 5  Sample size for Fig. E4A (CB)          mkN Zaxis_s sample size (n) mkN Zaxis_c_s sample size (n) mkT Zaxis3_s sample size (n) mkT Zaxis3_c_ssample size (n) stim side -3.603 7 ctrl side -3.603 8 stim side 0.0215 4 ctrl side 1.5215 2 SCC -2.103 6 SCC -2.103 8 SCC 1.5215 2 SCC 3.0215 2 -0.603 5 -0.603 6 3.0215 1 4.5215 11 0.897 6 0.897 10 4.5215 2 2.397 8 2.397 12 3.897 8 3.897 14 mkT Yaxis3 sample size (n) mkT Yaxis3_c sample size (n) 5.397 5 5.397 5 stim side -39.2537 1 ctrl side -43.7537 2 6.897 3 6.897 3 dACC-PCC -37.7537 3 dACC-PCC -42.2537 6 mkN Yaxis sample size (n) mkN Yaxis_c sample size (n) -36.2537 9 -40.7537 4 stim side -41.477 3 ctrl side -39.977 2 -34.7537 12 -39.2537 9 dACC-PCC -39.977 7 dACC-PCC -38.477 9 -33.2537 7 -37.7537 9 -38.477 17 -36.977 14 -31.7537 4 -36.2537 7 -36.977 18 -35.477 13 -30.2537 4 -34.7537 15 -35.477 17 -33.977 7 -28.7537 4 -33.2537 15 -33.977 16 -32.477 5 -27.2537 4 -31.7537 16 -32.477 6 -30.977 2 -25.7537 3 -30.2537 7 -30.977 4 -29.477 1 -24.2537 2 -28.7537 6 -29.477 3 -27.977 2 -22.7537 2 -27.2537 4 -27.977 4 -26.477 1 -21.2537 2 -25.7537 3 -26.477 3 -24.977 2 -19.7537 2 -24.2537 4 -24.977 2 -23.477 2 -18.2537 3 -22.7537 4 -23.477 3 -21.977 2 -16.7537 3 -21.2537 4 -21.977 4 -20.477 1 -15.2537 3 -19.7537 4 -20.477 4 -18.977 1 -13.7537 3 -18.2537 4 -18.977 4 -17.477 2 -12.2537 4 -16.7537 4 -17.477 4 -15.977 2 -10.7537 4 -15.2537 4 -15.977 4 -14.477 1 -9.2537 4 -13.7537 4 -14.477 3 -12.977 2 -7.7537 3 -12.2537 4 -12.97
```

**Agent**

Supplementary text is present in the `.txt` (Supplementary Methods 1–7, Tables 1–11), so I can proceed. Checking a few numbers before writing.

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; sed -n 428,565p $f | grep -c "×10"; sed -n 575,662p $f | grep -c "×10"; awk '/Supplementary Table 10/,/Non-stimulation Control animal/' $f | grep -c "×10"; python -c "
from scipy.stats import f
print(f.sf(6.02,1,1238), f.sf(6.02,2,1238), f.sf(4.64,1,3187), f.sf(5.42,1,1357), f.sf(186.48,1,20279), f.sf(51.09,1,21967), f.sf(7.36,1,10972), f.sf(24.55,1,492), f.sf(9,1,108))"
```

```
Exit code 1
69
44
166
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy.stats import f
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; sed -n 1989,2104p $f | grep -c "×10"; python3 -c "
import math
for F in [6.02,4.64,5.42,7.36,4.58,24.55,9]: print(F, 'df1=1 approx', math.erfc(math.sqrt(F/2)))
F=6.02;d2=1238;print('df1=2',(1+2*F/d2)**(-d2/2))"
```

```
53
6.02 df1=1 approx 0.014144646721966409
4.64 df1=1 approx 0.031235002475038784
5.42 df1=1 approx 0.01990735994570206
7.36 df1=1 approx 0.006669079168301857
4.58 df1=1 approx 0.03234721485063969
24.55 df1=1 approx 7.240634212097204e-07
9 df1=1 approx 0.0026997960632601913
df1=2 0.002501374049868573
```

**Agent**

The Fig. 6a interaction P (0.0025) matches F(2,1238) and not the printed F(1,1238); I'll record that as a paper inconsistency. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/001773/10.1038-s41593-026-02301-4.yaml",
 "content": "# Claims for Fujimoto, Fujimoto, Elorette et al. (2026), \"Deep brain stimulation induces white\n# matter remodeling and functional changes to brain-wide networks\", Nature Neuroscience,\n# doi:10.1038/s41593-026-02301-4, on dandiset 001773.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, as\n# the reader of docs/protocol.md (version pilot-10).\n#\n# Text read: the version of record (open access, PMC13337501, as served by Europe PMC), main\n# text, figure legends, Methods and Extended Data legends 1 to 10, together with the\n# Supplementary Information PDF (Supplementary Methods 1 to 7 and Supplementary Tables 1 to 11),\n# all in paper/10.1038-s41593-026-02301-4.txt. No PDF of the main article was available; no\n# figure needed to be read from one. The Nature \"Source Data\" files (statistical source data for\n# Figs. 2 to 6 and Extended Data Figs. 1, 4, 5, 6, 9 and 10) are cited by the paper but were not\n# under paper/ and no claim relies on them.\n#\n# Code: the paper says its custom MATLAB scripts for the functional MRI analysis are deposited in\n# the dandiset itself (Code availability, doi 10.48324/dandi.001773/0.260416.1939). A reader may\n# not open the dataset's files, so this code was NOT read. Every criterion below rests on the\n# Methods, legends and supplement. Where a detail is named open, the author should check whether\n# that code settles it and ask a reader (protocol, author step 6).\n#\n# Dataset: the archive gives the title of the paper and the description \"Data and code (fMRI,\n# DWI IF, EM, behavior)\", BIDS, 54 files, about 3.2 MB. The Data availability statement names\n# only the functional MRI data. At that size the dandiset can hold derived values (voxel FA,\n# cell counts, g-ratios, behavior bins, connectivity values) but hardly raw images; which is\n# the author's to find. All claims are data: dataset.\n#\n# Data the paper used, as it reports them:\n# - Monkeys N and T (male rhesus macaques, 7 to 9 years): SCC-DBS lead in the left (N) or right\n#   (T) hemisphere at the confluence of the cingulum bundle (CB), uncinate fasciculus (UF) and\n#   forceps minor (FM); 4 weeks without stimulation, then 6 weeks at 130 Hz, 5 mA, 90 us. The\n#   other hemisphere is the control hemisphere.\n# - Monkey D: lead implanted in the left hemisphere, never stimulated (\"sham\" hemisphere);\n#   same timeline.\n# - Nonsurgical controls B, W and H (male, 7 to 8 years): rs-fMRI and T1w only, two sessions\n#   6 to 7 weeks apart; the seed is the right SCC.\n# - Two MRI sessions per animal (pre-DBS and post-DBS, the lead removed about 20 min before the\n#   post scan), under isoflurane. DWI b = 1000, 72 directions, 1.5 mm, six runs (3 AP, 3 PA).\n#   rs-fMRI six runs of 300 volumes, TR 2.12 s, 1.6 mm, with MION; first three TRs removed.\n# - Behavior: one 10-min home-cage video per animal before and after, cut into 60 bins of 10 s,\n#   each scored 1 or 0 for movement and separately for foraging.\n# - Histology (MCC-CB, dACC-CB): CC1-positive and DAPI-positive counts in 7 fields x 4 coronal\n#   sections per hemisphere per animal (28 fields); UF/FM overlap 5 fields x 4 sections.\n# - Electron microscopy (N and T, MCC-CB): about 175 myelinated axons per hemisphere per animal\n#   (350 per hemisphere pooled), g-ratio = mean axon diameter / (mean axon diameter + 2 x mean\n#   myelin width), from the longest and shortest diameters and widths; axons with an aspect\n#   ratio above 2 excluded.\n#\n# Method details fixed here from the paper, used by several criteria:\n# - All ANOVAs and Tukey-Kramer tests were run in MATLAB R2023a (Methods, FA analysis). The\n#   \"three-way ANOVA\" models are full factorial in their three factors, plus a main effect of\n#   monkey when two monkeys are pooled (Methods: \"Monkeys were included in the model as a fixed\n#   effect\"). The reported error df confirm this: FA tracts 3200 values less 12 cells less 1\n#   = 3187; CB subregions 1374 - 17 = 1357; SCC target ROIs 20348 - 69 = 20279; networks\n#   21992 - 25 = 21967; monkey D (no monkey term) tracts 1250 - 12 = 1238, subregions 508 - 16\n#   = 492, networks 10996 - 24 = 10972, target ROIs 10174 - 68 = 10106. The sum of squares type\n#   is not stated; MATLAB anovan's default (type III) is the reading, and type II is run as a\n#   variant (it cannot differ much in these balanced pre/post designs).\n# - Tukey-Kramer post hoc tests: all pairwise comparisons among the cells of the three factors\n#   (MATLAB multcompare on the three factor dimensions), with the pre against post pair of each\n#   side and tract/ROI read off. Exact P values printed as 0 in Supplementary Table 9 are below\n#   MATLAB's precision (the legends write P < 1.00 x 10^-300).\n# - Effect sizes: partial eta squared = SS_effect / (SS_effect + SS_error) (Supplementary\n#   Methods 7).\n# - The \"one-way ANOVA\" with monkey as a fixed effect (behavior, CC1/DAPI, g-ratio) is open:\n#   (a) condition, monkey and condition x monkey (4 cells; the reported df 1,236, 1,108, 1,696\n#   and 1,76 match this: 240, 112, 700 and 80 values less 4); (b) condition and monkey only\n#   (df one larger). Both are run.\n# - Seed-based fMRI: seed = area 25 of the D99 atlas in the stimulated (N, T) or sham (D)\n#   hemisphere, right SCC for the nonsurgical controls. Fisher Z of the Pearson correlation\n#   between the seed's mean time series and every voxel (AFNI 3dTcorr1D), each voxel's Z then\n#   divided by the session's maximum Z. Whether runs are correlated one by one and averaged\n#   (as the connectome analysis does, \"For each run ... averaged within condition\") or\n#   concatenated is not stated: both are readings. Values are voxels in NMT space; \"stimulation\n#   side\" pools each monkey's own stimulated hemisphere. The voxel counts confirm this: the\n#   pooled N and T count per side (e.g. DMN 857) equals monkey D's left plus right count\n#   (453 + 404). Target ROIs are those of Supplementary Methods 4 with the voxel counts of\n#   Supplementary Table 8; where an atlas label is ambiguous (STG, dorsal insula, HIP, AMY, V1,\n#   MT), the definition whose pooled voxel count matches Table 8 is the one meant.\n# - Network hubs (Methods): DMN = PCC, vmFC, STG; SAN = anterior-dorsal insula, dACC; CEN =\n#   DLPFC, PPC; LIM = area 32, dACC, MCC, PCC, HIP, AMY; SMN = motor cortex, somatosensory\n#   cortex, SMA; VIS = V1, MT. Voxels of a hub ROI used in two networks are counted in both.\n#   The LIM count in Fig. 5c (821) equals the Methods list (803) plus area 25 (18), and the\n#   Extended Data Fig. 9 legend counts SCC as a LIM hub; so LIM is open, (a) with area 25 (the\n#   reported n) and (b) without (the Methods).\n# - Whole-brain connectome (Fig. 4): AFNI 3dNetCorr on CHARM and SARM level 4 ROIs, 122 ROIs as\n#   listed in Supplementary Tables 3 and 4 (hemispheres not separated in those lists; whether\n#   left and right ROIs are merged is not stated), Fisher Z per run, averaged per condition, post\n#   minus pre per subject, averaged across subjects.\n#\n# Paper inconsistencies found while reading (for the author's notes, not claims):\n# - Supplementary Tables 3, 4 and 11 (rank-biserial effect sizes for the DBS group, the\n#   nonsurgical controls and monkey D) are identical value for value, and their values (for\n#   example area_25 r_rb = -0.164) are far too small for the P values of Supplementary Table 1\n#   (3.7e-14 for area_25 with 122 against 122 values). No claim uses them.\n# - Supplementary Tables 1, 2 and 10 list P values up to 3.9e-4 as significant at \"P < 0.01 with\n#   Bonferroni correction\"; over 122 ROIs the uncorrected threshold would be 8.2e-5. The listed\n#   values are therefore either Bonferroni-adjusted or the threshold is not 0.01/122.\n# - Fig. 6a legend gives the PrePost x side x tract interaction as F 1,1238 = 6.02, P = 0.0025.\n#   With three tracts that interaction has 2 numerator df; F(2,1238) = 6.02 gives P = 0.0025 and\n#   F(1,1238) = 6.02 gives P = 0.014.\n# - Supplementary Methods 4 lists \"area 25 on the unstimulated side\" as a target, while Table 8\n#   lists area 25 on both sides (18 voxels each).\n# - Supplementary Table 9 gives MT on the control side P = 7.85e-7, while the Results say there\n#   was no change in \"areas within the VIS\".\n# - Extended Data Fig. 10d legend says the post scan was 10 weeks after implantation; the Methods\n#   say 6 weeks of implantation without stimulation.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001773\"\n  doi: 10.48324/dandi.001773/0.260416.1939\npaper: doi:10.1038/s41593-026-02301-4\nclaims:\n- id: ed1-behavior-increase\n  statement: After 6 weeks of SCC-DBS, monkeys N and T spent more time moving and more time\n    foraging in the home cage than before, in the same direction in both animals.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 1;\n    Extended Data Fig. 1\n  quote: Time spent moving and foraging both increased after SCC-DBS, with concordant effects\n    observed across subjects\n  statistics:\n  - about: movement, pre against post\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,236) = 34.61\n    p: 1.37e-08\n    n: 120 pre and 120 post 10-s bins, monkeys N and T\n  - about: foraging, pre against post\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,236) = 17.35\n    p: 4.37e-05\n    n: 120 pre and 120 post 10-s bins, monkeys N and T\n  expected:\n  - quantity: F, movement\n    value: 34.61\n    tolerance: 3.46\n  - quantity: F, foraging\n    value: 17.35\n    tolerance: 1.74\n  - quantity: partial eta squared, movement\n    value: 0.13\n    tolerance: 0.013\n  - quantity: partial eta squared, foraging\n    value: 0.068\n    tolerance: 0.0068\n  criterion: From Methods (Behavior analysis) and the Extended Data Fig. 1 legend. For N and T,\n    the 60 binary 10-s bins of each pre and post session, for movement and for foraging\n    separately (240 values each). ANOVA of the binary values on condition (pre, post) with\n    monkey as a fixed effect, under readings (a) condition, monkey and their interaction (the\n    reported df) and (b) condition and monkey. Reproduced when, under both readings, the\n    condition effect has P < 0.05 with the post probability higher, for both behaviors, and the\n    post probability is higher than the pre in each monkey for both behaviors; the F values and\n    partial eta squared are compared with the expected values under reading (a).\n- id: ed1-monkey-d-no-change\n  statement: In the unstimulated lead-implanted monkey D, the amount of movement and foraging\n    did not change between before and 6 weeks after implantation.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 2; Extended Data Fig. 1 (monkey D)\n  quote: First, there was no change in the amount of movement or foraging in naturalistic\n    behavior\n  criterion: A claim of absence. The paper shows monkey D's probabilities (Extended Data Fig. 1)\n    but reports no test for monkey D; the legend says only N and T were analysed. The test the\n    Methods describe for this measure, applied to one monkey, is a one-way ANOVA of the 120\n    binary bins on condition (pre, post), at the Methods' P < 0.05. Reproduced when neither\n    movement nor foraging differs at P < 0.05; not reproduced when either does. The pre and post\n    probabilities and their difference are given either way.\n- id: fig2a-cb-fa-increase\n  statement: After 6 weeks of SCC-DBS, fractional anisotropy (FA) increased in the cingulum\n    bundle of the stimulated hemisphere, with a significant PrePost x side interaction and a\n    significant pre against post difference in the stimulated CB.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig.\n    2a and legend\n  quote: We found there was a selective increase in FA in the CB in the stimulated hemisphere,\n    particularly the mid-cingulate portion, after 6 weeks of SCC-DBS\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x tract), monkey as fixed effect\n    statistic: F(1,3187) = 4.64\n    p: 0.0312\n    n: voxels pooled over N and T; stimulated CB 380, UF 252, FM 105; control CB 363, UF 367,\n      FM 133; each pre and post\n  - about: stimulated CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 0.022\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: F, PrePost x side interaction\n    value: 4.64\n    tolerance: 0.46\n  - quantity: partial eta squared, PrePost x side interaction\n    value: 0.0015\n    tolerance: 0.00015\n  criterion: From Methods (FA analysis) and the Fig. 2a legend. Voxel FA (1.5 mm) within the\n    CB, UF and FM masks of each hemisphere of N and T, both sessions in the pre-DBS T1w space,\n    voxels on the lead track excluded; the voxel counts should match the legend's n. ANOVA as\n    fixed in the opening comment (DBS x side x tract full factorial plus monkey; Tukey-Kramer\n    over the 12 cells). Reproduced when the PrePost x side interaction has P < 0.05 and the\n    stimulated CB's pre against post comparison has P < 0.05 with post FA higher. F and partial\n    eta squared are compared with the expected values.\n- id: fig2a-no-change-other-tracts\n  statement: FA did not change in the stimulated UF or FM, nor in any of the three tracts of the\n    control hemisphere.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig.\n    2a bottom graphs\n  quote: No consistent changes were apparent in either the stimulated UF or the FM ... or in the\n    same tracts within the control hemisphere\n  depends_on:\n  - fig2a-cb-fa-increase\n  criterion: A claim of absence, judged on the paper's test, the Tukey-Kramer post hoc of the\n    model of fig2a-cb-fa-increase at P < 0.05. Reproduced when none of the five pre against post\n    comparisons (stimulated UF, stimulated FM, control CB, control UF, control FM) has P < 0.05;\n    not reproduced when any does. The mean change and P of each are given either way.\n- id: ed2-cb-both-monkeys\n  statement: The FA increase in the stimulated CB was in the same direction in both monkeys.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3;\n    Extended Data Fig. 2\n  quote: Importantly, both monkeys exhibited changes in the same direction\n  depends_on:\n  - fig2a-cb-fa-increase\n  criterion: The paper reports no test per monkey. With the voxels of fig2a-cb-fa-increase,\n    reproduced when the mean post minus pre FA in the stimulated CB is positive in monkey N and\n    in monkey T.\n- id: fig2b-mcc-cb-fa-increase\n  statement: Of the four CB subregions, only the mid-cingulate portion (MCC-CB) of the\n    stimulated hemisphere showed an FA increase, and it did so in both animals.\n  source: Results, SCC-DBS induces selective macroscale remodeling in the CB, paragraph 3; Fig.\n    2b and legend; Extended Data Fig. 4a\n  quote: Comparing the FA values before and after 6 weeks of DBS in four CB subregions revealed\n    that only the mid-cingulate region on the stimulated side showed an increase in FA in both\n    animals\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x subregion), monkey as fixed effect\n    statistic: F(1,1357) = 5.42\n    p: 0.020\n    n: voxels pooled over N and T; stimulated SCC 54, dACC 137, MCC 55, PCC 80; control SCC 81,\n      dACC 158, MCC 50, PCC 72; each pre and post\n  - about: stimulated MCC-CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 0.0017\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: F, PrePost x side interaction\n    value: 5.42\n    tolerance: 0.54\n  - quantity: partial eta squared, PrePost x side interaction\n    value: 0.0040\n    tolerance: 0.0004\n  criterion: From Methods (FA analysis) and the Fig. 2b legend. The CB voxels split into four\n    subregions by the D99 atlas (SCC part, CB adjacent to areas 25 and 32; dACC, to area 24;\n    MCC, to area 24'; PCC, to area 23). The Methods do not define \"adjacent\"; if the dataset\n    labels voxels by subregion those labels are used, and the voxel counts should match the\n    legend. ANOVA DBS x side x subregion full factorial plus monkey, Tukey-Kramer over the 16\n    cells. Reproduced when the interaction has P < 0.05, the stimulated MCC-CB pre against post\n    comparison has P < 0.05 with post higher, no other subregion and side has a significant\n    increase, and the stimulated MCC-CB mean post minus pre is positive in each monkey.\n- id: fig3c-cc1-dapi-ratio\n  statement: The proportion of CC1-positive (myelinating oligodendrocyte) cells among\n    DAPI-positive cells in the MCC-CB was higher in the stimulated than in the control hemisphere,\n    in both animals.\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 1; Fig. 3b,c and legend\n  quote: The proportion of CC1 positive cells in the whole DAPI stained population was higher in\n    the mid-cingulate portion of the CB on the stimulated side compared to the control side in\n    both animals\n  statistics:\n  - about: main effect of side, CC1/DAPI ratio\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 9\n    p: 0.0034\n    n: 56 fields per hemisphere (7 fields x 4 sections x 2 monkeys)\n  expected:\n  - quantity: F, side\n    value: 9\n    tolerance: 0.9\n  - quantity: partial eta squared, side\n    value: 0.077\n    tolerance: 0.0077\n  criterion: From Methods (Immunofluorescence of myelinating oligodendrocytes) and the Fig. 3c\n    legend. The CC1/DAPI ratio (%) of each of the 112 MCC-CB fields of N and T. ANOVA on side\n    with monkey as a fixed effect, readings (a) and (b) of the opening comment. Reproduced when,\n    under both readings, side has P < 0.05 with the stimulated side higher, and each monkey's\n    mean ratio is higher on the stimulated side.\n- id: ed5-cc1-count-dapi-unchanged\n  statement: In the MCC-CB the number of CC1-positive cells was higher on the stimulated side,\n    while the number of DAPI-positive cells did not differ between hemispheres.\n  source: Extended Data Fig. 5 legend\n  quote: The main effect of side for the number of CC1 positive cells was significant ... while\n    no significant difference was observed for the number of DAPI positive cells\n  statistics:\n  - about: CC1-positive count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 6.22\n    p: 0.0142\n    n: 56 fields per hemisphere\n  - about: DAPI-positive count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 0.55\n    p: 0.4617\n    n: 56 fields per hemisphere\n  expected:\n  - quantity: F, CC1 count\n    value: 6.22\n    tolerance: 0.62\n  criterion: As fig3c-cc1-dapi-ratio, on the CC1-positive and DAPI-positive counts per field.\n    Reproduced when, under both model readings, the CC1 count has a side effect at P < 0.05 with\n    the stimulated side higher and the DAPI count has none (P >= 0.05, the paper's test for the\n    absence).\n- id: ed6-dacc-ufm-no-oligodendrocyte-change\n  statement: The CC1/DAPI ratio did not differ between hemispheres in the anterior (dACC)\n    portion of the CB, nor in the region where the FM and UF overlap.\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 1; Extended Data Fig. 6a,b\n  quote: No changes were observed in the anterior portion of CB, consistent with the lack of FA\n    alterations there ... Similarly, the region where the FM and UF overlap showed no\n    oligodendrocyte changes\n  statistics:\n  - about: dACC-CB, CC1/DAPI ratio, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 2.93\n    p: 0.0899\n    n: 56 fields per hemisphere\n  - about: dACC-CB, CC1 count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 0\n    p: 0.9974\n  - about: dACC-CB, DAPI count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,108) = 1.22\n    p: 0.2718\n  - about: UF and FM overlap, CC1/DAPI ratio, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,76) = 1.45\n    p: 0.2319\n    n: 40 fields per hemisphere (5 fields x 4 sections x 2 monkeys)\n  - about: UF and FM overlap, CC1 count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,76) = 0.79\n    p: 0.3778\n  - about: UF and FM overlap, DAPI count, side\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,76) = 0\n    p: 0.9611\n  criterion: A claim of absence, judged on the paper's test, the ANOVA of fig3c-cc1-dapi-ratio\n    on the dACC-CB fields (112) and the UF/FM overlap fields (80), at P < 0.05. Reproduced when\n    the side effect on the CC1/DAPI ratio has P >= 0.05 in both regions under reading (a) of the\n    model; not reproduced when either has P < 0.05. Reading (b), the counts and the effect\n    sizes are given either way.\n- id: fig3f-g-ratio-decrease\n  statement: The g-ratio of myelinated axons in the MCC-CB was lower in the stimulated than in\n    the control hemisphere, in both animals, meaning thicker myelin.\n  source: Results, SCC-DBS induces increased myelinating oligodendrocytes and the degree of\n    myelination, paragraph 2; Fig. 3d-f and legend\n  quote: In the stimulated hemisphere, the MCC-CB g -ratio was decreased compared to the control\n    hemisphere in both animals\n  statistics:\n  - about: main effect of side, g-ratio\n    test: one-way ANOVA, monkey as fixed effect\n    statistic: F(1,696) = 58.98\n    p: 5.42e-14\n    n: 350 axons per hemisphere, pooled over N and T\n  expected:\n  - quantity: F, side\n    value: 58.98\n    tolerance: 5.9\n  - quantity: partial eta squared, side\n    value: 0.078\n    tolerance: 0.0078\n  criterion: From Methods (Electron microscopy analysis of myelin thickness) and the Fig. 3f\n    legend. One g-ratio per axon, as defined in the opening comment, axons with aspect ratio\n    above 2 excluded (700 axons). ANOVA on side with monkey as a fixed effect, readings (a) and\n    (b). Reproduced when, under both readings, side has P < 0.05 with the stimulated side\n    lower, and each monkey's mean g-ratio is lower on the stimulated side.\n- id: fig4a-cortical-down-subcortical-up\n  statement: After SCC-DBS, whole-brain functional connectivity between cortical areas\n    decreased and connectivity between subcortical areas increased.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1;\n    Fig. 4a top right, Fig. 4b top\n  quote: Broadly, we observed a reduction in cortico–cortical functional connectivity and a\n    concurrent increase in subcortico–subcortical functional connectivity\n  criterion: The paper reports no test of the blocks; the pattern is read from the difference\n    connectome (Fig. 4a) and the per-ROI changes (Fig. 4b). Connectome as in the opening\n    comment, DBS group (N and T). Readings (a) the mean of the off-diagonal entries of the\n    group difference connectome within the cortical (CHARM) block and within the subcortical\n    (SARM) block; (b) each ROI's mean change to all other ROIs (the Fig. 4b measure), with the\n    median over cortical ROIs and over subcortical ROIs. Reproduced when, under both readings,\n    the cortical value is negative and the subcortical value positive.\n- id: fig4b-roi-changes-counts\n  statement: Per ROI, functional connectivity changed significantly between pre and post scans\n    in 69 of the 122 CHARM and SARM ROIs in the DBS group and in 44 of 122 in the nonsurgical\n    control group.\n  source: Fig. 4b and legend; Supplementary Tables 1 and 2\n  inferred: The counts are the number of ROIs listed in Supplementary Tables 1 (DBS group) and 2\n    (nonsurgical control group), the ROIs significant in Fig. 4b; no sentence states them.\n  statistics:\n  - about: per-ROI pre against post functional connectivity\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 122 pre and 122 post connectivity values per ROI\n  expected:\n  - quantity: ROIs significant, DBS group\n    value: 69\n    tolerance: 6.9\n  - quantity: ROIs significant, nonsurgical control group\n    value: 44\n    tolerance: 4.4\n  criterion: From Methods (EPI data analysis) and the Fig. 4b legend. For each of the 122 ROIs,\n    its 122 connectivity values (Fisher Z, group mean) pre against post with a two-sided\n    Wilcoxon rank-sum test. Open, and run under each reading. The test's pairing of values\n    (a) rank-sum of the 122 pre values against the 122 post values, as the Methods name;\n    (b) the 122 change values against zero (signed-rank), as the legend's \"changes ... from\n    zero\". The threshold (a') P < 0.01/122, Bonferroni over ROIs; (b') the Bonferroni-adjusted\n    P (P x 122) < 0.01, which is the same, so the open part is whether the listed P values are\n    adjusted (see the opening comment); a third reading takes the listed P values as raw and the\n    threshold P < 0.01, uncorrected. Whether the 122 values include the ROI's own diagonal is not\n    stated (121 or 122 values are both run). Reproduced when both counts are within tolerance\n    under one reading.\n- id: fig4c-network-sorted-reduction\n  statement: Sorted by cortical network membership, functional connectivity within and across\n    networks was reduced after SCC-DBS.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1;\n    Fig. 4c left\n  quote: When the functional connectivity was sorted based on cortical networks membership, it\n    was clear that connectivity within and across networks was reduced\n  depends_on:\n  - fig4a-cortical-down-subcortical-up\n  criterion: The paper does not give which network each of the 122 ROIs belongs to for Fig. 4c,\n    nor a test (the circular plot draws changes with |Z| > 0.1). If the paper's code deposited\n    in the dandiset assigns the ROIs to networks, use it; reproduced when the mean change of the\n    difference connectome is negative within each network block and across the pairs of\n    networks, in the majority of blocks. Without that assignment the claim is blocked as\n    methods_underspecified.\n- id: fig4-nonsurgical-no-pattern\n  statement: In the nonsurgical control animals, scans 6 to 7 weeks apart showed no systematic\n    pattern of functional connectivity change.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 1;\n    Fig. 4a,b bottom, Fig. 4c right\n  quote: In these control animals, a comparison conducted between scans acquired 6–7 weeks apart\n    did not reveal a systematic pattern of functional changes\n  depends_on:\n  - fig4a-cortical-down-subcortical-up\n  criterion: A claim of absence for which the paper reports no test; it compares Fig. 4a and 4b\n    by eye. Judged on the measure of fig4a-cortical-down-subcortical-up applied to monkeys B, W\n    and H. Reproduced when, under both readings, the DBS pattern (cortical block negative and\n    subcortical block positive) is not present; not reproduced when it is. The block values of\n    both groups are given side by side, and the count of significant ROIs from\n    fig4b-roi-changes-counts is noted (the paper's own tables list 44 in the controls).\n- id: fig5a-pre-scc-connectivity\n  statement: Before stimulation, the SCC was positively connected with vmFC, dACC, PCC, STG,\n    hippocampus, amygdala and DLPFC, and negatively with the insula and somatosensory cortex.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 2;\n    Fig. 5a top row; Extended Data Fig. 7 top row\n  quote: Before stimulation, the SCC showed positive connectivity to the ventromedial frontal\n    cortex (vmFC), dorsal anterior cingulate cortex (dACC), posterior cingulate cortex (PCC),\n    superior temporal gyrus (STG), hippocampus (HIP), amygdala (AMY) and dorsolateral\n    prefrontal cortex (DLPFC), as well as negative connectivity to the insula and somatosensory\n    cortex\n  criterion: No test is reported; Fig. 5a shows maps thresholded at P < 0.01. Pre-DBS\n    normalized seed connectivity (opening comment), mean over the target ROI's voxels pooled\n    over N and T, for vmFC, dACC, PCC, STG, HIP, AMY, DLPFC, anterior-dorsal insula and\n    somatosensory cortex. Readings (a) ROIs in the stimulated hemisphere; (b) both hemispheres\n    pooled; each with per-run and concatenated runs. Reproduced when, under every reading, all\n    seven are positive and both insula and somatosensory cortex negative; partially reproduced\n    when at least seven of the nine signs match under every reading.\n- id: fig5b-scc-decreases\n  statement: After SCC-DBS, functional connectivity of the stimulated SCC decreased with vmFC,\n    PCC, STG, hippocampus, amygdala, DLPFC and dACC in the stimulated hemisphere, with a\n    significant PrePost x side interaction.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3;\n    Fig. 5b and legend; Extended Data Fig. 9; Supplementary Table 9\n  quote: Following 6 weeks of SCC-DBS, there was a marked reduction in functional connectivity\n    between the SCC and the PCC as well as the vmFC. Reductions were also apparent between the\n    SCC and HIP, AMY and DLPFC\n  statistics:\n  - about: PrePost x side interaction, 17 target ROIs\n    test: three-way ANOVA (DBS x side x target ROI), monkey as fixed effect\n    statistic: F(1,20279) = 186.48\n    p: 2.87e-42\n    n: voxels pooled over N and T, per ROI as in Supplementary Table 8\n  - about: stimulated side, vmFC, PCC, STG, HIP, AMY, DLPFC and dACC, pre against post\n    test: Tukey-Kramer post hoc\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Tukey-Kramer\n  - about: stimulated side PCC\n    test: Tukey-Kramer post hoc\n    p: 8.22e-12\n  - about: stimulated side dACC\n    test: Tukey-Kramer post hoc\n    p: 4.75e-04\n  - about: stimulated side HIP\n    test: Tukey-Kramer post hoc\n    p: 1.19e-05\n  - about: stimulated side AMY\n    test: Tukey-Kramer post hoc\n    p: 7.70e-06\n  - about: stimulated side vmFC, STG and DLPFC (printed as 0 in Supplementary Table 9)\n    test: Tukey-Kramer post hoc\n    p: 0\n  expected:\n  - quantity: F, PrePost x side interaction\n    value: 186.48\n    tolerance: 18.6\n  - quantity: partial eta squared, PrePost x side interaction\n    value: 0.0091\n    tolerance: 0.00091\n  criterion: From Methods (EPI data analysis), Supplementary Methods 4 and the Fig. 5b and\n    Extended Data Fig. 9 legends. Normalized seed connectivity voxels of the 17 target ROIs of\n    Supplementary Table 8, both hemispheres, pre and post, N and T. ANOVA DBS x side x ROI full\n    factorial plus monkey (df 1,20279), Tukey-Kramer over the 68 cells. Run with per-run and\n    concatenated seed maps. Reproduced when, under both, the interaction has P < 0.05 and each\n    of the seven stimulated-side ROIs has a pre against post P < 0.05 with post lower;\n    partially reproduced when the interaction holds and at least four of the seven do.\n- id: fig5b-scc-increases\n  statement: After SCC-DBS, functional connectivity of the stimulated SCC increased with the\n    anterior-dorsal insula and the somatosensory cortex.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3;\n    Fig. 5a,b; Extended Data Fig. 9; Supplementary Table 9\n  quote: The insula and somatosensory cortex exhibited increases in functional connectivity with\n    the SCC following DBS\n  statistics:\n  - about: stimulated side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 4.42e-08\n    corrected: Tukey-Kramer\n  - about: stimulated side somatosensory cortex (printed as 0 in Supplementary Table 9)\n    test: Tukey-Kramer post hoc\n    p: 0\n    corrected: Tukey-Kramer\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: With the model of fig5b-scc-decreases. Reproduced when the stimulated-side\n    anterior-dorsal insula and somatosensory cortex each have a pre against post P < 0.05 with\n    post higher, under both seed-map readings.\n- id: ed9-control-hemisphere-changes\n  statement: Although stimulation was unilateral, SCC functional connectivity also changed in\n    the unstimulated control hemisphere, including vmFC, PCC, anterior-dorsal insula and dACC.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3;\n    Fig. 5b legend; Extended Data Figs. 8 and 9; Supplementary Table 9\n  quote: Despite DBS being delivered unilaterally and white matter remodeling being confined to\n    the stimulated hemisphere ... functional connectivity changes were also apparent in the\n    unstimulated control hemisphere\n  statistics:\n  - about: control side PCC\n    test: Tukey-Kramer post hoc\n    p: 4.03e-07\n    corrected: Tukey-Kramer\n  - about: control side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 0.0293\n    corrected: Tukey-Kramer\n  - about: control side vmFC and dACC (printed as 0 in Supplementary Table 9)\n    test: Tukey-Kramer post hoc\n    p: 0\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: control-side ROIs of 17 with a significant pre against post difference\n      (Supplementary Table 9)\n    value: 11\n    tolerance: 1.1\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: With the model of fig5b-scc-decreases. Reproduced when, under both seed-map\n    readings, the control-side vmFC, PCC, anterior-dorsal insula and dACC each have a pre\n    against post P < 0.05, and the number of control-side ROIs with P < 0.05 is within\n    tolerance of 11 (PCC, vmFC, STG, insula, dACC, DLPFC, area 25, area 32, HIP, somatosensory\n    cortex, MT in Supplementary Table 9).\n- id: ed9-no-change-motor-mcc\n  statement: Connectivity between the stimulated SCC and motor-related regions (primary motor\n    cortex, SMA) and the MCC did not change.\n  source: Discussion, Effect of SCC-DBS on functional networks, paragraph 3, and Interaction\n    between functional and structural effects of DBS, paragraph 2; Supplementary Table 9\n  quote: Notably, we found that there were no apparent changes in connectivity between the\n    stimulated SCC and motor-related regions, including the primary motor cortex or\n    supplementary motor area\n  statistics:\n  - about: stimulated side motor cortex\n    test: Tukey-Kramer post hoc\n    p: 0.999909913\n  - about: stimulated side SMA\n    test: Tukey-Kramer post hoc\n    p: 0.999989453\n  - about: stimulated side MCC\n    test: Tukey-Kramer post hoc\n    p: 0.991825378\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: A claim of absence, judged on the paper's test, the Tukey-Kramer post hoc of\n    fig5b-scc-decreases at P < 0.05. Reproduced when the stimulated-side motor cortex, SMA and\n    MCC pre against post comparisons all have P >= 0.05; not reproduced when any has P < 0.05.\n    The change and P of each are given either way.\n- id: ed7-decreases-both-monkeys\n  statement: The reductions in SCC functional connectivity after DBS were consistent across\n    both monkeys.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3;\n    Extended Data Figs. 7 and 8\n  quote: These reductions in functional connectivity from SCC were consistent across both\n    monkeys\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: No test per monkey is reported (Fig. 5b shows each monkey's mean as a symbol). For\n    each monkey, the mean post minus pre normalized connectivity in the stimulated hemisphere\n    for vmFC, PCC, STG, HIP, AMY, DLPFC and dACC. Reproduced when all seven are negative in\n    both monkeys under both seed-map readings; partially reproduced when at least five of the\n    seven are negative in each monkey.\n- id: fig5a-nonsurgical-no-reduction\n  statement: The reductions in SCC connectivity, and bilateral changes, seen after SCC-DBS were\n    absent in the nonsurgical control group over 6 weeks.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 3;\n    Fig. 5a bottom row; Extended Data Fig. 7 right column; Extended Data Fig. 8 bottom row\n  quote: Notably, such reductions in connectivity were absent in the nonsurgical control group,\n    indicating that these changes are specific to SCC-DBS\n  criterion: A claim of absence, judged on the paper's test, the voxelwise post minus pre map of\n    connectivity with the right SCC in monkeys B, W and H, thresholded at P < 0.01 with\n    clusters larger than 20 voxels (cluster-level corrected P < 0.01, two-sided; the Fig. 5a\n    legend). The paper does not name the voxelwise test or the cluster neighbourhood; the\n    readings are (a) a two-sample t-test per voxel between the pre and post run maps pooled over\n    the three monkeys; (b) a one-sample t-test of the three monkeys' post minus pre maps; each\n    with faces-only and faces, edges and corners neighbourhoods, and with per-run and\n    concatenated seed maps. Reproduced when, under the readings, no significant cluster of\n    decrease lies in the vmFC, PCC, STG, HIP, AMY, DLPFC or dACC ROIs of either hemisphere; not\n    reproduced when one does. If the readings disagree, the claim is blocked as\n    methods_underspecified with every result shown. The ROI-level change of the controls (the\n    measure of fig5b-scc-decreases, without the monkey term) is shown as a variant.\n- id: fig5c-dmn-lim-cen-decrease\n  statement: After SCC-DBS, functional connectivity of the stimulated SCC with the hubs of the\n    default mode, limbic and central executive networks decreased, with a significant PrePost x\n    side interaction.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4;\n    Fig. 5c and legend\n  quote: After chronic stimulation, the DMN, LIM and CEN showed significantly decreased\n    functional connectivity with SCC\n  statistics:\n  - about: PrePost x side interaction, six networks\n    test: three-way ANOVA (DBS x side x network), monkey as fixed effect\n    statistic: F(1,21967) = 51.09\n    p: 9.10e-13\n    n: voxels pooled over N and T; per side DMN 857, LIM 821, SAN 262, CEN 1102, SMN 1239, VIS\n      1217; each pre and post\n  - about: DMN, LIM and CEN, stimulated and control sides, pre against post\n    test: Tukey-Kramer post hoc\n    p: 1.0e-300\n    p_relation: \"<\"\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: F, PrePost x side interaction\n    value: 51.09\n    tolerance: 5.1\n  - quantity: partial eta squared, PrePost x side interaction\n    value: 0.0023\n    tolerance: 0.00023\n  criterion: From Methods (EPI data analysis) and the Fig. 5c legend. Each network's voxels are\n    the union, with repeats, of its hub ROIs' voxels (opening comment), LIM under readings (a)\n    with area 25 and (b) without. ANOVA DBS x side x network full factorial plus monkey,\n    Tukey-Kramer over the 24 cells. Reproduced when, under all readings, the interaction has\n    P < 0.05 and the stimulated-side DMN, LIM and CEN each have a pre against post P < 0.05 with\n    post lower.\n- id: fig5c-smn-increase\n  statement: SCC connectivity with the sensorimotor network increased after SCC-DBS, although\n    that network has few direct CB connections.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4;\n    Discussion, Effect of SCC-DBS on functional networks, paragraph 3; Fig. 5c\n  quote: As noted above, there was an increase in connectivity between the SCC and the SMN\n  statistics:\n  - about: stimulated side SMN\n    test: Tukey-Kramer post hoc\n    p: 2.83e-20\n    corrected: Tukey-Kramer\n  - about: control side SMN\n    test: Tukey-Kramer post hoc\n    p: 1.21e-14\n    corrected: Tukey-Kramer\n  depends_on:\n  - fig5c-dmn-lim-cen-decrease\n  criterion: With the model of fig5c-dmn-lim-cen-decrease. Reproduced when the stimulated-side\n    SMN pre against post comparison has P < 0.05 with post higher, under all readings.\n- id: fig5c-vis-no-change\n  statement: SCC connectivity with the visual network, and with the areas within it, did not\n    change after SCC-DBS.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4;\n    Fig. 5c; Extended Data Fig. 9\n  quote: In comparison, there was no change in relation to the VIS or areas within the VIS\n  statistics:\n  - about: stimulated side visual cortex (V1)\n    test: Tukey-Kramer post hoc\n    p: 0.999989453\n  - about: stimulated side MT\n    test: Tukey-Kramer post hoc\n    p: 0.998895555\n  depends_on:\n  - fig5c-dmn-lim-cen-decrease\n  - fig5b-scc-decreases\n  criterion: A claim of absence, judged on the paper's tests, the Tukey-Kramer post hoc of\n    fig5c-dmn-lim-cen-decrease (VIS) and of fig5b-scc-decreases (visual cortex and MT), at\n    P < 0.05. Reproduced when the stimulated-side VIS, visual cortex and MT comparisons all have\n    P >= 0.05; not reproduced when any has P < 0.05. The control side is reported as well; the\n    paper's own Supplementary Table 9 gives control-side MT P = 7.85e-7.\n- id: fig5c-san-rebalanced\n  statement: The salience network as a whole showed no change in connectivity with the\n    stimulated SCC, because its anterior-dorsal insula node increased and its dACC node\n    decreased.\n  source: Results, Whole-brain functional connectivity changes following SCC-DBS, paragraph 4;\n    Fig. 5b,c; Extended Data Fig. 9\n  quote: did not as a whole exhibit consistent changes after SCC-DBS ... Specifically, the\n    anterior-dorsal insula exhibited increased connectivity with the SCC, whereas the dACC\n    showed decreased connectivity following 6 weeks of DBS\n  statistics:\n  - about: stimulated side SAN network\n    test: Tukey-Kramer post hoc\n    p: 1.00\n  - about: control side SAN network\n    test: Tukey-Kramer post hoc\n    p: 6.20e-07\n    corrected: Tukey-Kramer\n  - about: stimulated side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 4.42e-08\n  - about: stimulated side dACC\n    test: Tukey-Kramer post hoc\n    p: 4.75e-04\n  depends_on:\n  - fig5c-dmn-lim-cen-decrease\n  - fig5b-scc-decreases\n  criterion: With the models of fig5c-dmn-lim-cen-decrease and fig5b-scc-decreases. Reproduced\n    when the stimulated-side SAN comparison has P >= 0.05 (the paper's test for the absence),\n    and the stimulated-side anterior-dorsal insula increases and dACC decreases, each at\n    P < 0.05.\n- id: fig6a-monkey-d-cb-fa-decrease\n  statement: In the unstimulated lead-implanted monkey D, FA decreased in the CB of the\n    implanted hemisphere and did not change in the other tracts.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 2; Fig. 6a and legend; Extended Data Fig. 10a\n  quote: Second, in direct contrast to the SCC-DBS animals, we saw a significant decrease in FA\n    in the CB of the implanted hemisphere and no changes in any of our other target tracts\n  statistics:\n  - about: PrePost x side x tract interaction (printed with 1 numerator df; P matches 2)\n    test: three-way ANOVA (DBS x side x tract)\n    statistic: F(1,1238) = 6.02\n    p: 0.0025\n    n: voxels of monkey D; sham CB 162, UF 120, FM 64; control CB 148, UF 74, FM 57; each pre\n      and post\n  - about: sham-side CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 5.07e-09\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: F, PrePost x side x tract interaction\n    value: 6.02\n    tolerance: 0.6\n  - quantity: partial eta squared, interaction\n    value: 0.0096\n    tolerance: 0.00096\n  criterion: As fig2a-cb-fa-increase, for monkey D alone, without the monkey term (df 1238).\n    Reproduced when the PrePost x side x tract interaction has P < 0.05, the sham-side CB pre\n    against post comparison has P < 0.05 with post lower, and none of the other five tract and\n    side comparisons has P < 0.05.\n- id: fig6b-monkey-d-dacc-cb-decrease\n  statement: In monkey D the CB FA decrease lay in the dACC portion of the implanted hemisphere,\n    more anterior than and opposite in direction to the MCC-CB increase after stimulation.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 2; Fig. 6b and legend\n  quote: This decrease in FA is more anterior and the opposite direction of that observed in the\n    stimulation group\n  statistics:\n  - about: PrePost x side interaction\n    test: three-way ANOVA (DBS x side x subregion)\n    statistic: F(1,492) = 24.55\n    p: 9.97e-07\n    n: voxels of monkey D; sham SCC 44, dACC 58, MCC 23, PCC 16; control SCC 28, dACC 53, MCC 13,\n      PCC 19; each pre and post\n  - about: sham-side dACC-CB, pre against post\n    test: Tukey-Kramer post hoc\n    p: 1.30e-08\n    corrected: Tukey-Kramer\n  expected:\n  - quantity: F, PrePost x side interaction\n    value: 24.55\n    tolerance: 2.46\n  - quantity: partial eta squared, interaction\n    value: 0.048\n    tolerance: 0.0048\n  depends_on:\n  - fig2b-mcc-cb-fa-increase\n  criterion: As fig2b-mcc-cb-fa-increase, for monkey D alone, without the monkey term (df 492).\n    Reproduced when the interaction has P < 0.05, the sham-side dACC-CB pre against post\n    comparison has P < 0.05 with post lower, and the sham-side MCC-CB shows no significant\n    increase.\n- id: fig6c-monkey-d-cc1-no-change\n  statement: In monkey D, the CC1/DAPI ratio in the MCC-CB did not differ between the implanted\n    and control hemispheres.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 2; Fig. 6c and legend\n  quote: the ratio of myelinated oligodendrocytes (CC1/DAPI) in the MCC-CB did not differ\n    between the implanted and control hemispheres\n  statistics:\n  - test: two-sided paired t-test\n    statistic: t(27) = -0.9888, Cohen's dz = -0.19\n    p: 0.3316\n    n: 28 fields per hemisphere (7 fields x 4 sections), monkey D\n  criterion: A claim of absence, judged on the paper's test, a two-sided paired t-test of the\n    28 field ratios between hemispheres at P < 0.05 (Methods). How fields are paired across\n    hemispheres is not stated; readings (a) by section and field number as recorded in the\n    dataset; (b) by order within section when no field number is recorded. Reproduced when the\n    test has P >= 0.05; not reproduced when P < 0.05. The mean difference and dz are given\n    either way, and an unpaired test is shown as a variant.\n- id: ed10c-monkey-d-subcortical-decrease\n  statement: In monkey D, whole-brain connectivity changes after implantation were less\n    coherent than after SCC-DBS, cortico-cortical changes were mixed, and subcortico-subcortical\n    connectivity decreased, the opposite of the SCC-DBS group.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 3; Extended Data Fig. 10c\n  quote: Cortical-to-cortical connections showed more random connectivity changes, and\n    subcortical-to-subcortical connections showed a consistent negative change, which is the\n    opposite direction of what we saw after SCC-DBS\n  depends_on:\n  - fig4a-cortical-down-subcortical-up\n  criterion: No test of the blocks is reported. With the readings of\n    fig4a-cortical-down-subcortical-up applied to monkey D's difference connectome. Reproduced\n    when, under both readings, the subcortical value is negative. The cortical value and the\n    fraction of negative cortical entries are reported; \"more random\" is not otherwise tested.\n- id: fig6d-monkey-d-scc-local-increase\n  statement: In monkey D, SCC functional connectivity changed little after implantation, apart\n    from a localized increase at the implantation site.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 3; Fig. 6d; Extended Data Fig. 10d\n  quote: Additionally, there was very little alteration in the functional connectivity\n    associated with the SCC, except for a localized increase in connectivity at the site of\n    implantation\n  depends_on:\n  - fig5a-nonsurgical-no-reduction\n  criterion: Judged on the voxelwise thresholded map of the Fig. 6d legend (P < 0.01, clusters\n    larger than 20 voxels), with the voxelwise test readings of fig5a-nonsurgical-no-reduction\n    that apply to one animal (reading (a), pre against post runs). Reproduced when a\n    significant cluster of increase lies at the lead track and no significant cluster of\n    decrease lies in the vmFC, PCC, STG, HIP, AMY, DLPFC or dACC ROIs. The paper gives the lead\n    location only as images; if the dataset does not give it, the claim is blocked as\n    metadata_insufficient.\n- id: fig6e-monkey-d-no-network-reduction\n  statement: In monkey D the reductions in SCC connectivity with the DMN, LIM and CEN seen after\n    SCC-DBS were not observed.\n  source: Results, The impact of SCC-DBS lead insertion on functional and structural brain\n    networks, paragraph 3; Fig. 6e and legend\n  quote: Notably, the widespread reductions in connectivity that we saw in the DMN, LIM and CEN\n    after SCC-DBS were not observed\n  statistics:\n  - about: PrePost x side interaction, six networks\n    test: three-way ANOVA (DBS x side x network)\n    statistic: F(1,10972) = 7.36\n    p: 0.0067\n    n: voxels of monkey D; sham DMN 453, LIM 438, SAN 137, CEN 552, SMN 637, VIS 602; control\n      DMN 404, LIM 383, SAN 125, CEN 550, SMN 602, VIS 615; each pre and post\n  - about: control-side DMN\n    test: Tukey-Kramer post hoc\n    p: 8.20e-08\n  - about: control-side CEN\n    test: Tukey-Kramer post hoc\n    p: 0.0088\n  - about: sham-side SMN\n    test: Tukey-Kramer post hoc\n    p: 1.38e-04\n  - about: control-side SAN\n    test: Tukey-Kramer post hoc\n    p: 1.06e-04\n  depends_on:\n  - fig5c-dmn-lim-cen-decrease\n  criterion: A claim of absence, judged on the paper's test, the model of\n    fig5c-dmn-lim-cen-decrease for monkey D alone without the monkey term (df 10972), Tukey-Kramer\n    at P < 0.05, with the LIM readings. What \"not observed\" covers is open, (a) the sham\n    side, (b) both sides; the paper's own legend lists significant control-side DMN and CEN\n    differences without their direction. Reproduced when no DMN, LIM or CEN comparison of the\n    sides the reading covers is a significant decrease; not reproduced when one is. If the\n    readings disagree, blocked as methods_underspecified with both shown.\n- id: ed10d-monkey-d-roi-changes\n  statement: Among vmFC, PCC, anterior-dorsal insula and dACC, monkey D showed a significant\n    pre against post difference in SCC connectivity only for the sham-side vmFC and the\n    control-side anterior-dorsal insula.\n  source: Extended Data Fig. 10d legend\n  quote: A significant pre–post difference was observed in the sham side vmFC ( P = 7.83e-04)\n    and control side anterior-dorsal insula\n  statistics:\n  - about: PrePost x side interaction, 17 target ROIs\n    test: three-way ANOVA (DBS x side x target ROI)\n    statistic: F(1,10106) = 4.58\n    p: 0.0323\n    n: voxels of monkey D; sham vmFC 66, PCC 138, insula 49, dACC 88; control vmFC 43, PCC 111,\n      insula 51, dACC 74; each pre and post\n  - about: sham-side vmFC\n    test: Tukey-Kramer post hoc\n    p: 7.83e-04\n    corrected: Tukey-Kramer\n  - about: control-side anterior-dorsal insula\n    test: Tukey-Kramer post hoc\n    p: 1.37e-12\n    corrected: Tukey-Kramer\n  depends_on:\n  - fig5b-scc-decreases\n  criterion: The model of fig5b-scc-decreases for monkey D alone, without the monkey term\n    (17 ROIs, df 10106). Reproduced when the interaction has P < 0.05 and, of the eight\n    comparisons (four ROIs, two sides), exactly the sham-side vmFC and the control-side\n    anterior-dorsal insula have P < 0.05. Directions are reported; the paper does not give them.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001773/10.1038-s41593-026-02301-4.yaml paper/10.1038-s41593-026-02301-4.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 31 quotes match. Confirming the 8 flagged values by reading them in the text:

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; for v in "7.70E-06" "0.999909913" "9.10 × 10 −1 3" "0.998895555" "6.20 × 10−7" "1.30 × 10 −8" "8.20 × 10 −8" "7.83e-04"; do echo "== $v: $(grep -o ".\{25\}$v.\{5\}" $f | head -2 | tr '\n' '|')"; done
```

```
/bin/bash: line 1: cd: paper: No such file or directory
== 7.70E-06: 
== 0.999909913: 
== 9.10 × 10 −1 3: 
== 0.998895555: 
== 6.20 × 10−7: 
== 1.30 × 10 −8: 
== 8.20 × 10 −8: 
== 7.83e-04: the sham side vmFC ( P = 7.83e-04) and|
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; for v in "7.70E-06" "0.999909913" "9.10 ×" "0.998895555" "6.20 ×" "1.30 ×" "8.20 ×"; do echo "== $v: $(grep -n -o ".\{20\}$v.\{12\}" $f | head -2 | tr '\n' '|')"; done; grep -n "7.70E-06\|0.999909913\|0.998895555" $f
```

```
== 7.70E-06: 
== 0.999909913: 
== 9.10 ×: 
== 0.998895555: 
== 6.20 ×: 
== 1.30 ×: 
== 8.20 ×: 
1967:7.70E-06 
1973:0.999909913 
1982:0.998895555
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41593-026-02301-4.txt; for v in "= 9.10" "= 6.20" "= 1.30" "= 8.20"; do grep -o "$v.\{14\}" $f | head -1 | cat -A | head -1; done
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-026-02301-4.txt').read()
for v in ['9.10','6.20','1.30','8.20']:
    i=t.find('P = '+v)
    while i>=0:
        print(repr(t[i-30:i+25])); i=t.find('P = '+v,i+1)
"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-026-02301-4.txt').read()
import re
for v in ['9.10','6.20','1.30','8.20']:
    for m in re.finditer(re.escape(v),t): print(v, repr(t[m.start()-25:m.start()+22]))
"
```

```
9.10 '( F 1,21967 =\u200951.09, P =\u20099.10\u2009×\u200910 −1 3, η p 2 '
6.20 '0, NS; control side, P =\u20096.20\u2009× 10−7 ). * P <\u20090'
1.30 'he sham hemisphere ( P =\u20091.30\u2009×\u200910 −8 ). * P <\u2009'
8.20 'e control-side DMN ( P =\u20098.20\u2009×\u200910 −8 ), contro'
8.20 ' 10.1523/JNEUROSCI.2964-08.2008 18945892 PMC667'
8.20 ' 10.1523/JNEUROSCI.2964-08.2008 PMC6671361 23. '
8.20 ' 10.1523/JNEUROSCI.2964-08.2008\n\n[23] Lynch, C.'
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml; d=yaml.safe_load(open('claims/001773/10.1038-s41593-026-02301-4.yaml'))
c=d['claims']; print(len(c), sum('quote' in x for x in c), sum('inferred' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))"; git status --short
```

```
32 31 1 21 32 12
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/001773/
?? scripts
```

**Agent**

I wrote the claims file: `claims/001773/10.1038-s41593-026-02301-4.yaml`. The checker passes every quote and the schema. It exits non-zero only because it can't find 8 p-values, and I confirmed each of those by reading it in the text: they are printed with thin spaces, as the garbled "9.10 × 10 −1 3", or as Supplementary Table 9's E-notation and 9-digit values.

**Text read.** The version of record (open access, PMC13337501, from Europe PMC): main text, figure legends, Methods and Extended Data legends 1 to 10. The supplement was extracted into the same `.txt`: Supplementary Methods 1 to 7 and Supplementary Tables 1 to 11. The supplement the earlier run reported missing is now there. There is no PDF of the main article, and no figure needed one.

**Code not read.** The paper's MATLAB fMRI scripts are deposited inside dandiset 001773 itself, which a reader may not open. Every criterion therefore rests on the Methods, legends and supplement. The opening comment asks the author to check that code for the details listed below as open, and to ask a reader.

**Counts.** 32 claims: 31 have quotes and 1 is `inferred` (the per-ROI significance counts, taken from Supplementary Tables 1 and 2). 21 claims have statistics, 32 have criteria and 12 have expected values. All are `data: dataset`. The archive describes the dataset as "Data and code (fMRI, DWI IF, EM, behavior)", about 3.2 MB.

**Details fixed from the paper.**
- **ANOVA models:** the error df printed in the paper match full-factorial three-way ANOVAs plus a monkey main effect, and none for monkey D. Tukey–Kramer runs over all cells (MATLAB multcompare).
- **"One-way ANOVA with monkey as fixed effect":** its df match a model with condition, monkey and their interaction.
- **Hub networks:** the voxel counts of each network equal the sum of its hub ROIs' counts in Supplementary Table 8.

**Details the paper leaves open, with the readings named:**
- **One-way ANOVA model:** (a) with the condition × monkey interaction, which matches the df; (b) the additive model.
- **Sum of squares type:** type III (MATLAB's default); type II run as a variant.
- **Seed maps:** correlations computed per run and averaged, or on concatenated runs.
- **LIM network:** with area 25 (matches the reported n = 821) or without it (the Methods list).
- **Fig. 4b rank-sum test:** pre against post values, or the changes against zero. For the threshold: whether the listed P values are Bonferroni-adjusted, or raw at P < 0.01. Whether the ROI's own diagonal entry is included (121 or 122 values).
- **Fig. 4a pattern:** block means of the difference connectome, or the median of per-ROI mean changes.
- **Pre-stimulation SCC connectivity signs:** ROIs of the stimulated hemisphere only, or both hemispheres.
- **Voxelwise cluster maps (nonsurgical controls, monkey D):** the test is not named (run-level two-sample or subject-level one-sample), nor the cluster neighbourhood.
- **Monkey D paired t-test:** how fields are paired across hemispheres.
- **Monkey D network reductions "not observed":** sham side only, or both sides.
- **Monkey D behavior:** the paper reports no test; the claim uses the Methods' ANOVA applied to monkey D.
- **CB subregions:** what "adjacent" to each area means; the legend's voxel counts serve as the check.

**Missing from the paper:**
- **Fig. 4c:** the network membership of the 122 ROIs is not given. That claim is blocked unless the deposited code supplies it.
- **Fig. 6d:** the lead location is given only as images, so that claim may be blocked for lack of metadata.

**Paper inconsistencies** (recorded in the opening comment):
- Supplementary Tables 3, 4 and 11 (effect sizes for three different groups) are identical, and their values don't fit the P values of Table 1.
- Some P values listed as Bonferroni-significant exceed 0.01/122.
- The Fig. 6a P (0.0025) matches F(2,1238), not the printed F(1,1238).
- Area 25 is described as a target on one side only but is listed on both sides.
- Table 9 shows a significant change in control-side MT, while the Results say "no change ... in areas within the VIS".
- Extended Data Fig. 10d says the post scan was 10 weeks after implantation; the Methods say 6.

I did not commit anything.

## End of run

30 turns, 8 minutes, result: success.
