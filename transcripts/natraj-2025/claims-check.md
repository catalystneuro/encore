# 001535 · claims-check · run 39596282447

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001535/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md; python tools/claims_check.py claims/001535/*.yaml paper/*.txt; cat claims/001535/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/^## Reader/,/^## Author/' ~/work/reproduction-registry/reproduction-registry/docs/protocol.md
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
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | tail -40; wc -l claims/001535/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports 52 claims, all quotes found, one p-value (3.2442e-12) not found in the text. Reading the paper and the claims file now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2025.02.001.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)" "substr($0,1,100)}' *.txt
```

```
1: 31 DOI: 10.1016/j.cell.2025.02.001
2: 30 Version: as served by ncbi_pmc
3: 46 Source: ncbi_pmc+crossref (paper-text-fetcher)
4: 18 Stored: 2026-10-20
5: 21 Extracted: as fetched
6: 72 ------------------------------------------------------------------------
7: 208934 pmc Cell Cell 319 nihpa 0413066 Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection
8: 0 
9: 119 Sampling representational plasticity of simple imagined movements across days enables long-term neur
10: 0 
11: 111 [1] Causes and consequences of representational drift. Curr. Opin. Neurobiol.. 2019. 10.1016/j.conb.
12: 0 
13: 138 [2] Variance and invariance of neuronal long-term representations. Philos. Trans. R. Soc. Lond. B Bi
14: 0 
15: 96 [3] Representational drift in primary olfactory cortex. Nature. 2021. 10.1038/s41586-021-03628-7
16: 0 
17: 125 [4] Spectral changes in cortical surface potentials during motor movement. J. Neurosci.. 2007. 10.15
18: 0 
19: 121 [5] fMRI evaluation of somatotopic representation in human primary motor cortex. Neuroimage. 2000. 1
20: 0 
[... 193 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -s -w 2000 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 35
}
```

```
1	pmc Cell Cell 319 nihpa 0413066 Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC11932800 PMC11932800.1 11932800 11932800 NIHMS2059472 40054446 10.1016/j.cell.2025.02.001 NIHMS2059472 NIHPA2059472 1 Article Sampling representational plasticity of simple imagined movements across-days enables long-term neuroprosthetic control Natraj N. 1 2 Seko S. 1 Abiri R. 1 Miao R. 1 * Yan H. 1 * Graham Y. 1 * Tu-Chan A. 1 2 Chang E. F. 3 Ganguly K. 1 2 1 Department of Neurology, Weill Institute for Neurosciences, University of California-San Francisco, San Francisco, California, USA. 2 VA San Francisco Healthcare System, San Francisco, California, USA. 3 Department of Neurological Surgery, Weill Institute for Neuroscience, University of California-San Francisco, San Francisco, California, USA. * these authors contributed equally Contributions N.N. designed the study, designed and implemented the real-time BCI signal processing system, decoders, the hDoF framework, performed experiments, analyzed data, and drafted the manuscript. S.S. implemented the real-time Kinova Jaco, the hDoF framework, performed experiments and aided in manuscript drafting. R.A. performed the initial calibration of the Kinova Jaco, performed experiments, and aided in real-time system design. H.Y., R.M. and Y.G. aided in data collection and analyses. A.T.C. conducted patient recruitment and patient care. E.F.C. performed the surgical implantation and patient care. K.G. conceived and supervised all aspects. Lead contact: [removed: an e-mail address] 06 3 2025 188 5 485051 1208 1225.e32 05 03 2025 06 03 2026 06 03 2026 26 03 2025 23 09 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Flexible regulation of representations on a drifting manifold enables long-term stable complex neuroprosthetic control 14 8 2023 2023.08.11.551770 bioRxiv 10.1101/2023.08.11.551770 PMC10462094 
2
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 36,
 "limit": 35
}
```

```
36	averaged in bins of non-overlapping 200ms bins and temporally smoothed, thereby down sampling the data. We then z-scored each feature’s down sampled data across all trials within each session, capturing normalized neural differences between movements independent of session-specific fluctuations. Down sampled and z-scored trials from all sessions were then concatenated together, forming the dataset for each movement that were then used for pairwise representational similarity analyses. Spatial feature extraction for somatotopic decoders, autoencoders and BCI experiments (MLP-based Fig. 2 – 6 and Fig. S3 ) For neural decoding using only spatial activity patterns with the MLP, we computed the binned power of the streaming neural activity in three frequency bands at each channel of the grid: δ ( 0.5 – 4 H z ) , β ( 13 – 30 H z ) and γ H ( 70 - 150 H z ) . The temporal width of the bins was dependent on the decoder update rate, which typically was set at 5Hz, though we piloted a range between 5 and 10Hz. For example, a decoder running at 5Hz would bin neural activity with 200ms intervals. Third-order Butterworth Infinite Impulse Response band-pass filters were used to extract the neural features real-time. To compute power more accurately in the slower δ band, the real-time PC had a running circular 2s buffer that was updated with raw neural activity at the decoder update rate. The filter was then applied to the entire 2s buffer and the most recent bin-width of δ band filtered activity was extracted. To compute power at the channel level, each sample of the filtered signal within the bin was squared and then averaged over time with a log transform to get an estimate of binned δ power. For faster rhythms, we utilized a filter bank approach before computing power and without the need for a running buffer. β power at each channel was computed by averaging binned power within 13 – 19 H z , 19 – 30 H z . γ H power at each channel was computed by averaging binned power with
[... 34 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 71
}
```

```
File content (27377 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 71,
 "limit": 18
}
```

```
71	block of trials, N fail is the number of trials that were inaccurately decoded within a block of trials and T is the total time taken within the block of trials including time taken for both accurate and inaccurate trials. Using regression analyses, we also assessed whether there was any linear slope in the evolution of the median decoding accuracy of each session across the PnP experimental window. This was done for both B1’s PnP experiments and for B3’s single PnP experiment ( Fig. S8C – E ). Coactivations of representations ( Fig. S8G ) Coactivated data representations were collected across multiple trials for combinations of imagined right hand movement with imagined left leg and imagined head movements as well as single movements. The successful performance of a decoder in each trial (discerning individual and dual coactivated movements) was ascertained by a max-vote strategy. A confusion matrix denoting performance from trials across sessions is shown in Fig. S8G . Representational analyses of denovo BCI velocity commands with the ReFit Kalman Filter ( Fig. S7 ) We performed latent-space representational analyses for end-effector velocity commands with the ReFit-KF in a manner analogous to discrete representations. This analyses was done only with B1. Similar to the well-rehearsed discrete movements, we built a daily autoencoder to capture neural representations of velocity commands to center-out targets in the 3D virtual workspace using a daily initialized ReFit-KF. We carried out five days of daily initialization with the ReFit-KF. We demarcated neural data into six labeled classes, for each of the six center-out targets in the 3D workspace. Given that continuous velocity commands span the entire workspace, we further parcellated data into two types of velocity commands to better capture target-specific neural activity. First, we built an autoencoder only for the first ~2.5s of data across trials, capturing ballistic feedforward commands to various target
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 89
}
```

```
89	). Complex organization of human primary motor cortex: a high-resolution fMRI study . Journal of neurophysiology 100 , 1800 – 1812 . 18684903 10.1152/jn.90531.2008 PMC2576195 7. Schellekens W , Petridou N , and Ramsey NF ( 2018 ). Detailed somatotopy in primary motor and somatosensory cortex revealed by Gaussian population receptive fields . Neuroimage 179 , 337 – 347 . 29940282 10.1016/j.neuroimage.2018.06.062 PMC6413921 8. Degenhart AD , Hiremath SV , Yang Y , Foldes S , Collinger JL , Boninger M , Tyler-Kabara EC , and Wang W ( 2018 ). Remapping cortical modulation for electrocorticographic brain–computer interfaces: a somatotopy-based approach in individuals with upper-limb paralysis . Journal of neural engineering 15 , 026021 . 29160240 10.1088/1741-2552/aa9bfb PMC5841472 9. Leuthardt EC , Schalk G , Wolpaw JR , Ojemann JG , and Moran DW ( 2004 ). A brain–computer interface using electrocorticographic signals in humans . Journal of neural engineering 1 , 63 . 15876624 10.1088/1741-2560/1/2/001 10. Wang W , Collinger JL , Degenhart AD , Tyler-Kabara EC , Schwartz AB , Moran DW , Weber DJ , Wodlinger B , Vinjamuri RK , and Ashmore RC ( 2013 ). An electrocorticographic brain interface in an individual with tetraplegia . PloS one 8 , e55344 . 23405137 10.1371/journal.pone.0055344 PMC3566209 11. Moses DA , Metzger SL , Liu JR , Anumanchipalli GK , Makin JG , Sun PF , Chartier J , Dougherty ME , Liu PM , and Abrams GM ( 2021 ). Neuroprosthesis for decoding speech in a paralyzed person with anarthria . New England Journal of Medicine 385 , 217 – 227 . 34260835 10.1056/NEJMoa2027540 PMC8972947 12. Silversmith DB , Abiri R , Hardy NF , Natraj N , Tu-Chan A , Chang EF , and Ganguly K ( 2021 ). Plug-and-play control of a brain–computer interface through neural map stabilization . Nature Biotechnology 39 326 – 335 . 10.1038/s41587-020-0662-5 32895549 13. Benabid AL , Costecalde T , Eliseyev A , Charvet G , Verney A , Karakas S , Foerster M , Lambert A , Morinière B , an
[... 17 more lines not kept]
```

**Agent**

Paper read. Now the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "limit": 400
}
```

```
1	# Claims for Natraj, Seko, Abiri, Miao, Yan, Graham, Tu-Chan, Chang & Ganguly (2025), Cell 188,
2	# 1208-1225, on dandiset 001535.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
4	# pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC11932800, NIHMS2059472), full
7	# text as served by ncbi_pmc (paper/10.1016-j.cell.2025.02.001.txt): Results, Discussion, STAR
8	# Methods, the main figure legends and the supplementary legends (Figures S1 to S9, Videos S1 to
9	# S4, Supplementary Method S1). It is not the version of record. The supplement is present only as
10	# its legends; Supplementary Method S1 (a timeline schematic) and the supplementary figures
11	# themselves were not read, and no PDF was supplied. No claim needs a value that appears only in a
12	# figure image.
13	#
14	# Code read: the paper links "exemplar real-time BCI and neural signal processing code and
15	# decoders" at OSF (doi:10.17605/OSF.IO/TBDWG), one file BCI/bci.zip (17742715 bytes, modified
16	# 2025-02-26, sha256 575149d40829d135557d17cd5247c85a0d333033467f8c25df281bef8ddb091a). It holds the
17	# MATLAB real-time task modules (Robot3DArrow, RealRobotBatch, RobotR2GModeSwitch and others), the
18	# feature pipeline (neuro/), Kalman filter code, the PyBullet robot simulator, trained decoders
19	# (clicker/*.mat) and scripts that fine-tune the biLSTM (task_helpers/ToTrainDiscreteModel_7DoF_LSTM.m,
20	# get_lstm_features.m, extract_lstm_features.m) and run the mode filter (runningMode.m). It holds no
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "offset": 400,
 "limit": 400
}
```

```
400	    100 (CL2 - CL1) / CL1. A mixed model of the 21 values with an intercept and a random intercept
401	    per participant; its p is the fraction of 1000 bootstrap samples of each participant's
402	    mean-centered data whose |t| is at least the observed. The tolerance is the reported spread
403	    (the paper does not say whether it is SD or SE). Reproduced when all three means are within
404	    tolerance and all three p < 0.05.
405	- id: figs4hi-feature-importance
406	  statement: All three bands contribute to decoding, with delta and high gamma the most
407	    informative.
408	  source: Results, Discriminability of representations with closed-loop control, paragraph 1;
409	    Figure S4H-I
410	  quote: Offline analyses revealed that while all three neural features ( δ , β , γ H ) were
411	    important for decoding, δ and γ H were most informative
412	  criterion: Methods (Importance of neural features). Trials from all daily sessions per
413	    participant, 15 random splits (the Methods print "70% of trials for testing, 15% validation and
414	    15% testing"; the reading is 70% training), decoders on all three bands, each pair of bands
415	    and each band alone; held-out trial accuracy per split. The paper gives no test. Read as
416	    (i) all three bands together reach at least the median accuracy of every single band, and
417	    (ii) delta alone and high gamma alone each have a higher median accuracy than beta alone, in
418	    both participants. Reproduced when both hold in both participants.
419	- id: fig2i-distance-cl-vs-ol
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "offset": 800,
 "limit": 380
}
```

```
800	  - fig2e-above-chance
801	  criterion: Methods (paragraph on logistic regression). Per participant, the points are the
802	    sessions' OL, CL1 and CL2 values (the Methods say accuracy "from each individual session", and
803	    the figure plots each session's distance against its accuracy); logistic regression of
804	    accuracy (a proportion) on mean latent distance; leave-one-out log loss averaged over points;
805	    p is the fraction of 1000 permutations of the accuracies whose log loss is smaller. Open
806	    details. (1) Whether points are 30 and 33 (all three contexts) or 10 and 11 (one per session);
807	    readings (a) all contexts, (b) CL2 only, (c) mean of the contexts. (2) The fit with a
808	    fractional outcome; reading a binomial GLM with the proportion as response, unweighted.
809	    Reproduced when under one reading of (1) both p < 0.05 and both losses are within tolerance;
810	    partially reproduced when both p < 0.05 only.
811	- id: fig3c-manifold-stable
812	  statement: Daily autoencoder manifolds are similar across days (CKA); in B1, 80% of day pairs
813	    have all five layers significantly similar and the rest at least four; in B3, 83.64% have all
814	    five, 12.72% four and 3.64% three.
815	  source: Results, Stability of action representations, paragraph 1; Figure 3C
816	  quote: In B1, 80% of all pairwise comparisons had all 5 layers significantly similar; the
817	    remaining 20% had at least 4 of 5 similar layers. In B3, 83.64% of all pairwise comparisons had
818	    all layers similar; 12.72% had at least 4 of 5 similar layers and the remaining 3.64% had at
819	    least 3 of the 5 similar layers
[... 360 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "offset": 1180
}
```

```
1180	- id: figs8cde-pnp-stable
1181	  statement: Daily median PnP accuracy shows no linear trend across days in either B1 experiment
1182	    or in B3.
1183	  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3;
1184	    Figure S8C-E
1185	  quote: a linear fit to the daily median revealed stable performance across-days for both ( Fig.
1186	    S8C – D , p = 0.897 for PnP Exp 1 and p = 0.11 for PnP Exp 2)
1187	  statistics:
1188	  - about: B1 experiment 1
1189	    test: linear regression slope
1190	    statistic: t(5) = 0.136
1191	    p: 0.897
1192	  - about: B1 experiment 2
1193	    test: linear regression slope
1194	    statistic: t(8) = -1.79
1195	    p: 0.11
1196	  - about: B3
1197	    test: linear regression slope
1198	    statistic: t(7) = 1.035
1199	    p: 0.3348
[... 319 more lines not kept]
```

**Agent**

I've read the whole file. Making corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    the action names' effector, as the dataset labels them. Reproduced when, under one reading of\n    (1), both tests give p < 0.05 with the within-right-hand similarity higher.",
 "new_string": "    the action names' effector, as the dataset labels them. Reproduced when both tests give\n    p < 0.05 with the within-right-hand similarity higher. Reading (1) is a method detail: the\n    outcome is the one both readings give; if they differ, the claim is blocked as\n    methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "  criterion: As fig1g-somatotopy-b1, on B3's 32 actions and 253 channels. Reproduced when, under\n    one reading of the channel neighbourhood, both tests give p < 0.05 with the within-right-hand\n    similarity higher.",
 "new_string": "  criterion: As fig1g-somatotopy-b1, on B3's 32 actions and 253 channels. Reproduced when both\n    tests give p < 0.05 with the within-right-hand similarity higher, under both readings of the\n    channel neighbourhood; if the readings differ, blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    give r, so the readings are (a) Pearson, (b) Spearman. Reproduced when under one reading r is\n    within tolerance and p < 0.05.",
 "new_string": "    give r, so the readings are (a) Pearson, (b) Spearman. Reproduced when r is within tolerance\n    and p < 0.05; the correlation type is a method detail, so the outcome is the one both readings\n    give, and if they differ the claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "  statement: Hierarchical clustering of the distance matrix groups actions by effector in both\n    participants.",
 "new_string": "  statement: Hierarchical clustering of each participant's pairwise distance matrix shows the\n    relations of actions within and across effectors."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    clustering of each participant's distance matrix. The paper gives no measure of how well\n    clusters follow effectors. The test here, named as a standard choice and not the paper's, is\n    the fraction of actions whose nearest neighbour in the dendrogram (first merge) is an action of\n    the same effector, compared with 1000 permutations of effector labels. Reproduced when that\n    fraction exceeds the 95th percentile of the permutation null in both participants.",
 "new_string": "    clustering of each participant's distance matrix. The paper gives no measure or test of how\n    clusters follow effectors, and states no grouping in words. The attempt shows both\n    dendrograms. As a variant only, it reports the fraction of actions whose nearest neighbour in\n    the dendrogram (first merge) is an action of the same effector, against 1000 permutations of\n    effector labels; this measure is not the paper's and cannot decide the outcome. The claim is\n    recorded as methods_underspecified, with the dendrograms and the variant shown."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent**

Now fig2e-above-chance (threshold statistic and the binomial reading).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    distribution, FDR corrected, α = 0.05 level, Fig. S4A – B ) for every single session in B1 and B3\n  statistics:\n  - test: binomial\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 63 decoders (21 sessions, three contexts)\n  criterion:",
 "new_string": "    distribution, FDR corrected, α = 0.05 level, Fig. S4A – B ) for every single session in B1 and B3\n  criterion:"
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    online decodes per trial. The p-value is the binomial probability of K or fewer successes being\n    reached by chance, the area from 0 to N/m successes with m = 7, and FDR is applied over all\n    decoders. Open details. The binomial p as written (\"area from 0 to N/m successes\") is the\n    probability of chance-level or lower performance; the reading used is the usual upper tail\n    P(X >= K) under p = 1/7, with the paper's wording shown as a variant. Reproduced when every\n    session's three decoders pass FDR at 0.05.",
 "new_string": "    online decodes per trial. The p-value follows the Methods: the binomial distribution \"for a\n    decoder given the total number of trials (N) and number of trials successfully decoded (K)\",\n    that is Binomial(N, K/N), and p is its area from 0 to N/m successes (chance or worse), with\n    m = 7; FDR (Benjamini-Hochberg) at 0.05 over all decoders (63, from 21 sessions and three\n    contexts). The usual upper tail P(X >= K) under success probability 1/7 is shown as a variant.\n    Reproduced when every session's three decoders pass FDR at 0.05."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    readings (a) none, (b) training data doubled. Random seeds are a standard choice. Reproduced\n    when under one reading of each the LMM gives p < 0.05 for both contrasts and the signed rank\n    test gives p < 0.05 for both contrasts in each participant, with CL greater.",
 "new_string": "    readings (a) none, (b) training data doubled. Random seeds are a standard choice. Reproduced\n    when the LMM gives p < 0.05 for both contrasts and the signed rank test gives p < 0.05 for both\n    contrasts in each participant, with CL greater. (1) and (2) are method details: the outcome is\n    the one all four combinations of readings give; if they differ, the claim is blocked as\n    methods_underspecified. The same rule holds for the claims that use these autoencoders."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    participant's maximum, (c) z-scored within participant. Reproduced when under one reading the\n    LMM gives p < 0.05 for both contrasts and the signed rank tests give p < 0.05 in each\n    participant, with CL lower.",
 "new_string": "    participant's maximum, (c) z-scored within participant. Reproduced when the LMM gives p < 0.05\n    for both contrasts and the signed rank tests give p < 0.05 in each participant, with CL lower.\n    The scaling is a method detail: the outcome is the one all three readings give; if they\n    differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent**

Now figs5 (feature reading, grading), figs5bc (threshold anchor), figs6gh (feature space).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    participant) with p from 1000 bootstrap samples of centered data. The values are on\n    reconstructed, L2-normalized features (Figure S5D). Reproduced when the nine session-mean\n    changes are negative with p < 0.05, and at least seven of the nine are within tolerance;\n    partially reproduced when all nine are negative and significant but fewer are within\n    tolerance.",
 "new_string": "    participant) with p from 1000 bootstrap samples of centered data. Open detail. The Methods\n    first describe the reconstruction, then \"examined the variance of feature activity at each\n    spatial channel\", without saying whether the SD is taken on the reconstructed or the input\n    (L2-normalized, Figure S5D) features; readings (a) reconstructed features, (b) input\n    features. The two are different measures, so the outcome is the one both give; if they differ,\n    the claim is blocked as methods_underspecified. Reproduced when the nine session-mean changes\n    are negative with p < 0.05 and all nine are within tolerance; partially reproduced when all\n    nine are negative and significant but some fall outside tolerance."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    paper gives no threshold. Read as preserved when the median correlation over actions and\n    sessions exceeds 0.8 for each band and context pair in both participants; this threshold is a\n    standard choice, not the paper's, and the full distributions are reported.",
 "new_string": "    paper gives no threshold or test here. Its one number for a map it calls preserved is the\n    average pairwise r = 0.88 of Figure 4B; with the 10% tolerance of the protocol this gives\n    0.79. Read as preserved when the median correlation over actions and sessions is at least 0.79\n    for each band and context pair in both participants; the full distributions are reported."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    Mahalanobis distance of each session's features (delta, beta and high gamma on all pooled\n    channels, 96 in B1 and 759 in B3) instead of latent values. Reproduced when the CL slope is\n    positive with p < 0.05 and the OL slope has p >= 0.05, in both participants.",
 "new_string": "    Mahalanobis distance of each session's features instead of latent values. Open detail. \"Full\n    high dimensional neural data\" is not defined for B1; readings (a) the 96 decoder features\n    (2x2 pooled, L2-normalized), (b) the 384 unpooled channel features. B3 uses its 759 features.\n    The outcome is the one both readings give; if they differ, the claim is blocked as\n    methods_underspecified. Reproduced when the CL slope is positive with p < 0.05 and the OL slope\n    has p >= 0.05, in both participants."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "  statistics:\n  - test: CKA against weight-shuffled null\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 45 day pairs in B1 and 55 in B3, five layers each\n  expected:",
 "new_string": "  expected:"
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    permuted, (b) the layer's units (rows) are permuted. Reproduced when under one combination of\n    readings both \"all 5\" fractions are within tolerance and no B1 pair has fewer than 4 similar\n    layers; partially reproduced when at least 75% of pairs in each participant have at least 4\n    similar layers.",
 "new_string": "    permuted, (b) the layer's units (rows) are permuted. There are 45 day pairs in B1 and 55 in B3,\n    five layers each. Reproduced when both \"all 5\" fractions are within tolerance and no B1 pair\n    has fewer than 4 similar layers; partially reproduced when at least 75% of pairs in each\n    participant have at least 4 similar layers. (1) and (2) are method details: the outcome is the\n    one all four combinations give; if they differ, the claim is blocked as\n    methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    Reproduced when, under one reading, the 65% and 1.5 values are within tolerance, no\n    feedforward day pair has a similar layer, and the three tests give p < 0.05 with discrete\n    highest.",
 "new_string": "    Reproduced when the 65% and 1.5 values are within tolerance, no feedforward day pair has a\n    similar layer, and the three tests give p < 0.05 with discrete highest. As in\n    fig3c-manifold-stable, the outcome is the one all combinations of its readings give; if they\n    differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    n: 48 IBID and 18 ReFit-KF trials on one day\n  criterion: Methods (Robot kinematics analyses). Per trial, the square root of the summed squared\n    differences between decoded and ideal straight-line positions over all time points, divided\n    by the number of points; Mann Whitney U between IBID and ReFit-KF CL2 trials. Reproduced when\n    p < 0.05 with the ReFit-KF median higher.",
 "new_string": "  criterion: Methods (Robot kinematics analyses). Per trial, the square root of the summed squared\n    differences between decoded and ideal straight-line positions over all time points, divided\n    by the number of points; Mann Whitney U between IBID and ReFit-KF CL2 trials. Open detail. The\n    Results name 48 IBID and 18 ReFit-KF trials on one testing day, but with 48 and 18 values a\n    Mann Whitney z cannot exceed about 6.2, below the reported 6.967; the reported test therefore\n    used more values (more trials or sessions, or per-time-point errors), which the paper does not\n    say. The test is run on per-trial errors as the Methods define them, and the z and p are not\n    expected to match. Reproduced when p < 0.05 with the ReFit-KF median higher."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    variant. The interval tolerances are the paper's own and very narrow; the claim is reproduced\n    when under one reading of (1) both accuracies are within their tolerance, and partially\n    reproduced when both are within 10% of the reported values and far above chance.",
 "new_string": "    variant. The interval tolerances are the paper's own and very narrow; the claim is reproduced\n    when both accuracies are within their tolerance, and partially reproduced when both are within\n    10% of the reported values and far above chance. (1) is a method detail: the outcome is the one\n    both readings give; if they differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    on samples; trial-level day accuracy (the trial's label taken by max vote over its samples,\n    as for the other trial-level decoders) averaged over splits; p from the binomial with the\n    number of held-out trials and chance 1/10 (B1) or 1/11 (B3). Reproduced when p < 0.05 in both\n    participants.",
 "new_string": "    on samples; trial-level day accuracy averaged over splits; p from the binomial (as in\n    fig2e-above-chance) with the number of held-out trials and chance 1/10 (B1) or 1/11 (B3).\n    Open detail. How a trial's samples give its label is not stated for this decoder; readings\n    (a) max vote over the trial's samples, as for the other trial-level decoders (Methods, Action\n    decoding), (b) the fraction of the trial's samples decoded correctly, averaged over trials.\n    The outcome is the one both readings give; if they differ, blocked as methods_underspecified.\n    Reproduced when p < 0.05 in both participants."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "  expected:\n    quantity: B1 slope of median held-out distance on days used\n    value: 0.258\n    tolerance: 0.0258",
 "new_string": "  expected:\n    quantity: slope of median held-out distance on days used, in the participant the printed value\n      belongs to (B1 or B3)\n    value: 0.258\n    tolerance: 0.0258"
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    suggests a normal approximation on 9 or 10 points; the p is taken from the fit as reported by\n    the software. B1 is held to its slope, B3 only to the sign and significance because its\n    printed values duplicate B1's. Reproduced when under one reading of (1) both slopes are\n    positive with p < 0.05 and the B1 slope is within tolerance; partially reproduced when both\n    are positive and significant only.",
 "new_string": "    suggests a normal approximation on 9 or 10 points; the p is taken from the fit as reported by\n    the software. (3) The printed slope is identical for B1 and B3, so it belongs to one of them\n    and the paper does not say which; readings (a) it is B1's, (b) it is B3's. Reproduced when both\n    slopes are positive with p < 0.05 and the slope of the participant named by reading (a) or (b)\n    is within tolerance (either reading may match); partially reproduced when both are positive\n    and significant only. (1) is a method detail: the outcome is the one both weightings give; if\n    they differ, the claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "B3 (Figure 4G); one of them is likely a copy. Both are recorded, and the criteria for B3 rest on\n# the sign and significance of the slope, not on its value.",
 "new_string": "B3 (Figure 4G); one of them is likely a copy. Both are recorded; the criterion holds the slope\n# value to either participant, as the paper does not say which one it belongs to."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    the MLP width is not given (reading 64 units per layer, as for the day-decoding MLP). Reproduced\n    when the slope is positive with p < 0.05 and within tolerance.",
 "new_string": "    the MLP width is not given; 64 units per layer, as for the day-decoding MLP, is a standard\n    choice, not the paper's, and widths 32 and 128 are shown as variants. Reproduced when the slope\n    is positive with p < 0.05 and within tolerance; if the widths give different outcomes, the\n    claim is blocked as methods_underspecified."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    interval are reported (expected value with the paper's interval). Open detail. Whether\n    time points with zero velocity or before the first input are included; readings (a) all\n    time points, (b) only time points with non-zero velocity.",
 "new_string": "    interval are reported (expected value with the paper's interval). The Methods take the errors\n    \"across time and trials\", so the test is run on all time points; excluding time points with\n    zero velocity is shown as a variant only, since a claim of absence is judged on the paper's\n    test as written."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    trials. The paper gives no test for \"significant\". Read as the first principal component's\n    angle from both cardinal axes exceeding 20 degrees and its loading on X and Y both above 0.3 in\n    absolute value; this threshold is a standard choice, not the paper's, and the loadings are\n    reported.",
 "new_string": "    trials. The paper calls the covariation \"significant\" but gives no test, threshold or number\n    for it, in the Methods or the legend. The attempt reports the PC loadings and angles. As a\n    variant only, it reports whether the first component lies more than 20 degrees from both\n    cardinal axes with both loadings above 0.3 in absolute value; this threshold is not the\n    paper's and cannot decide the outcome. The claim is recorded as methods_underspecified, with\n    the loadings shown."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "old_string": "    trial accuracy by max vote. The paper gives no test; read as a binomial test of trial accuracy\n    against 1/m (m the number of classes), at 0.05. Reproduced when it is significant.",
 "new_string": "    trial accuracy by max vote. The legend reports \"significant discernability\" without naming\n    the test; the paper's test of decoder significance elsewhere (Methods, Action decoding) is the\n    binomial test of fig2e-above-chance, used here with m the number of classes (five: right hand,\n    left leg, head and the two coactivations, per the Methods). Reproduced when it gives p < 0.05."
}
```

```
The file claims/001535/10.1016-j.cell.2025.02.001.yaml has been updated successfully.
```

**Agent**

Now the checks entry. Checking the format used elsewhere.

**Agent calls Bash**

```bash
grep -n -A8 '^checks:' claims/001539/*.yaml | head -30; tail -3 claims/001535/*.yaml
```

```
1445:checks:
1446-- date: 2026-10-21
1447-  kind: agent
1448-  model: claude-opus-5-5
1449-  ready: true
1450-  changes:
1451-  - fig1c-sampling-duration. The code's rank-sum is at line 65 of cs_nosepokeDuration_2.m, not line 61 (read at the cited commit).
1452-  - fig1s1f-air-performance. Dropped "performance was near chance" from the statement; no sentence of the paper says it, only the figure's chance line would.
1453-  - fig2d-beta-power-increase, fig2e-beta-coherence-increase (and fig2e-rr-coherence-increase by reference), fig2e-beta-coherence-odor-vs-reward (and fig2e-rr-coherence-odor-vs-reward, fig2d-power-odor-vs-reward), fig2g-air-beta-coherence. The criteria accepted a match under either LFP pipeline. The pipelines are method readings that can change the outcome, so the protocol requires the outcome both give, blocked as methods_underspecified when they differ; the rule now says so.
    accuracy comparison uses online pilot blocks, which only the online decodes can give.
    Reproduced when the variance test gives p < 0.05 with pooled lower; the accuracy part is
    reported when testable.
```

**Agent calls Bash**

```bash
cat >> claims/001535/10.1016-j.cell.2025.02.001.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1g-somatotopy-b1, fig1h-somatotopy-b3, fig1kl-b1-b3-correlation, fig2i-distance-cl-vs-ol (and the claims using its autoencoders), fig2j-variance-cl-vs-ol (and fig2j-variance-cl2-vs-cl1), fig3c-manifold-stable, figs7cd-refit-less-stable, fig4cd-day-decodable, fig4fg-sampling-days-increases-distance. The criteria accepted a match under any one reading of a method detail (channel neighbourhood, correlation type, reconstruction loss, augmentation, variance scaling, CKA inputs and shuffling, day-label scheme, robust weighting). These can change the outcome, so the protocol requires the outcome all readings give, blocked as methods_underspecified when they differ; the rules now say so.
  - fig2e-above-chance, fig3c-manifold-stable. Removed the statistics entries "p < 0.05, FDR"; they are the thresholds used to count sessions and layers, not results.
  - fig2e-above-chance. The criterion used the upper tail under p = 1/7 as its main reading against the Methods, which define the binomial from N and K and take its area from 0 to N/m; the Methods' reading is now the main one and the upper tail a variant.
  - fig1mn-hierarchical-clustering. The statement said clustering groups actions by effector, which no sentence of the paper says; it now says what the Results say. The nearest-neighbour permutation test was the agent's; it is now a variant only and the claim is recorded as methods_underspecified, since the paper gives no measure.
  - fig6g-velocity-covariation. The 20 degree and 0.3 loading thresholds were the agent's, with no test in the paper; they are now a variant only and the claim is recorded as methods_underspecified with the loadings shown.
  - figs5bc-somatotopy-preserved. The 0.8 threshold was the agent's; it is now 0.79, from the paper's own r = 0.88 for a map it calls preserved (Figure 4B) less 10%.
  - figs5-channel-variance-reduction. Named as open whether the SD is taken on reconstructed or input features (the Methods do not say), with the all-readings rule; replaced the agent's "seven of nine within tolerance" with all nine.
  - figs6gh-highdim-trends. The B1 feature space (96 pooled features) was the agent's choice; named the 96 and 384 feature readings as open.
  - figs7i-ibid-straighter-than-refit. Removed n of 48 and 18 trials; with those counts a Mann Whitney z cannot exceed about 6.2, below the reported 6.967, so the test used more values than the paper states. The criterion now says so and does not expect z or p to match.
  - fig4fg-sampling-days-increases-distance. The criterion held B1 to the duplicated slope; the paper does not say which participant it belongs to, so either may match (header note updated).
  - figs8ab-day-decodable-trials. The max-vote trial label was assumed; named it with the per-sample reading as open.
  - fig4i-boundary-convergence. The 64-unit width is now named a standard choice with variants, as the paper gives none.
  - fig6g-ibid-angular-error. A claim of absence is judged on the paper's test as written; the test now uses all time points ("across time and trials") and the non-zero-velocity reading is a variant.
  - figs8g-coactivation. The binomial test is now tied to the paper's decoder test (Methods, Action decoding), with the five classes named in the Methods.
  - Checker value 3.2442e-12 (figs7i) was flagged as not found; it is in the Figure S7I legend as "p = 3.2442 × 10 - 12", confirmed by reading.
  - Open, not settled. fig1ij-within-effector-levels reading (b), every significant channel with a majority rule, is the reader's construction; the paper identifies its two channels only in the figure.
  - Open, not settled. figs4hi-feature-importance reads "important" and "most informative" as comparisons of median accuracies; the paper gives no test.
  - Open, not settled. Paragraph numbers in sources could not be checked, as the text has no paragraph breaks.
EOF
python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | tail -5; grep -n '—\|rather' claims/001535/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001535; grep -n 'detail: \|details: \|Results: ' *.yaml
```

```
119:    p < 0.05 with the within-right-hand similarity higher. Reading (1) is a method detail: the
461:    contrasts in each participant, with CL greater. (1) and (2) are method details: the outcome is
519:    The scaling is a method detail: the outcome is the one all three readings give; if they
850:    participant have at least 4 similar layers. (1) and (2) are method details: the outcome is the
999:    10% of the reported values and far above chance. (1) is a method detail: the outcome is the one
1074:    and significant only. (1) is a method detail: the outcome is the one both weightings give; if
```

**Agent calls Bash**

```bash
cd  sed -i 's/method detail: the/method detail, so the/; s/method details: the/method details, so the/' claims/001535/*.yaml; python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | tail -5; grep -n '—\|rather' claims/001535/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/follows the Methods: the binomial/follows the Methods, the binomial/' claims/001535/*.yaml; grep -nE '^\s{4,}[^-#].*: ' claims/001535/*.yaml | grep -v "^[0-9]*:\s*quote: '" | head; python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | tail -4
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/(five: right hand,/(five, right hand,/' claims/001535/*.yaml; python tools/claims_check.py claims/001535/*.yaml paper/*.txt 2>&1 | tail -4; grep -n '—\|rather' claims/001535/*.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent**

**Checker result:** `52 claims, 52 quotes, 125 statistical values, 1 problems`. The one problem is figs7i's p = 3.2442e-12, which the checker could not find. It is in the Figure S7I legend, printed as "p = 3.2442 × 10 - 12"; I confirmed it by reading. The count of statistical values went from 127 to 125 because I removed two threshold entries.

**Changes, by claim**
- **Readings of method details:** these criteria accepted a match under any single reading of a method detail. The protocol requires the outcome all readings give, or the claim is blocked as methods_underspecified. Fixed in:
  - fig1g, fig1h (channel neighbourhood)
  - fig1kl (Pearson or Spearman)
  - fig2i, and the claims that use its autoencoders (reconstruction loss, augmentation)
  - fig2j (variance scaling)
  - fig3c and figs7cd (CKA inputs and shuffling)
  - fig4cd-day-decodable (how day labels enter)
  - fig4fg (robust weighting)
- **fig2e-above-chance, fig3c:** removed the "p < 0.05, FDR" statistics. They are thresholds used to count sessions and layers, not results.
- **fig2e-above-chance:** the main binomial reading went against the Methods. The Methods' Binomial(N, K/N), area 0 to N/m, is now the main reading; the usual upper tail is a variant.
- **fig1mn:** the statement said the clustering groups actions by effector, which no sentence of the paper says; it now follows the Results. The permutation test was made up by the writer, so it is now a variant only and the claim is recorded as methods_underspecified.
- **fig6g-velocity-covariation:** the 20° and 0.3 thresholds were also made up by the writer. They are now a variant only, and the claim is recorded as methods_underspecified.
- **figs5bc:** the 0.8 threshold was the writer's. It is now 0.79: the paper's own "preserved" map has r = 0.88 (Fig. 4B), less 10%.
- **figs5:** the Methods do not say whether the SD is taken on reconstructed or input features; this is now named as open. The made-up "7 of 9 within tolerance" is now all 9.
- **figs6gh:** B1's feature space is open (96 pooled or 384 unpooled features); both readings are now named.
- **figs7i:** removed n = 48 and 18 trials. With those counts a Mann-Whitney z cannot exceed about 6.2, but the paper reports 6.967. The criterion now says so and does not expect z or p to match.
- **fig4fg:** the printed slope is identical for B1 and B3, and the paper does not say whose it is. The slope value can now match either participant; the header note is updated.
- **figs8ab:** how a trial's label is formed from its samples is open; max vote and per-sample accuracy are now both named.
- **fig4i:** the 64-unit width is now called a standard choice, with other widths as variants.
- **fig6g-ibid-angular-error:** this is a claim of absence, so it is judged on the paper's test as written, over all time points.
- **figs8g:** the binomial test is now tied to the paper's own decoder test (Methods, Action decoding), with 5 classes.

**Still open**
- fig1ij: reading (b), every significant channel with a majority rule, was built by the writer. The paper identifies its two channels only in the figure.
- figs4hi: "important" and "most informative" are read as comparisons of median accuracy; the paper gives no test.
- The paragraph numbers in sources could not be checked, because the text has no paragraph breaks.

Every main finding has a claim, and every claim comes from this paper.

**Ready:** yes. The checks entry is recorded with `ready: true`. Only `claims/001535/` was changed; nothing is committed.

## End of run

49 turns, 5 minutes, result: success.
