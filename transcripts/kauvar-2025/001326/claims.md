# 001326 · claims · run 39689410079

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001326 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*; head -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head; grep -n "SUPPLEMENT\|Supplementary\|===\|^--" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 7p ~/work/reproduction-registry/reproduction-registry/paper/10.1126-science.adt3971.txt | fold -s -w 200 > main.txt; wc -l main.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	544 hhmipa Science (New York, N.Y.) Science PMC12286656 12286656 12286656 NIHMS2090574 40440375 10.1126/science.adt3971 Conserved brain-wide emergence of emotional response from sensory experience in 
2	humans and mice Kauvar Isaac 1 2 3 † Richman Ethan B 1 2 † Liu Tony X 1 2 † Li Chelsea 4 Vesuna Sam 1 5 Chibukhchyan Adelaida 1 2 Yamada Lisa 1 2 6 Fogarty Adam 1 2 7 Solomon Ethan 1 5 Choi Eun Young 
3	1 6 Mortazavi Leili 8 Loo Kung Gustavo Chau 2 9 Mukunda Pavithra 1 5 Raja Cephra 2 Gil-Hernández Dariana 1 5 Patron Kishandra 1 2 Zhang Xue 5 Brawer Jacob 5 Wrobel Shenandoah 2 Lusk Zoe 7 Lyu Dian 7 
4	Mitra Anish 1 5 Hack Laura 5 10 Luo Liqun 11 12 Grosenick Logan 13 van Roessel Peter 1 5 Williams Leanne M 5 10 Heifets Boris D 1 14 Henderson Jaimie M 6 McNab Jennifer A 9 Rodríguez Carolyn I 1 5 10 
5	* Buch Vivek 1 6 * Nuyujukian Paul 1 2 6 15 * Deisseroth Karl 1 2 5 12 * 1 Human Neural Circuitry program, Stanford University, Stanford, CA, USA. 2 Department of Bioengineering, Stanford University, 
6	Stanford, CA, USA. 3 Graduate School of Education, Stanford University, Stanford, CA, USA. 4 Neurosciences Graduate Program, Stanford University, Stanford, CA, USA. 5 Department of Psychiatry and 
7	Behavioral Sciences, Stanford University, Stanford, CA USA. 6 Department of Neurosurgery, Stanford University, Stanford, CA, USA. 7 Department of Neurology and Neurological Sciences, Stanford, CA, 
8	USA. 8 Department of Psychology, Stanford University, Stanford, CA, USA. 9 Department of Radiology, Stanford University, Stanford, CA, USA. 10 Veterans Affairs Palo Alto Health Care System, Palo 
9	Alto, CA, USA. 11 Department of Biology, Stanford University, Stanford, CA, USA. 12 Howard Hughes Medical Institute, Stanford University, Stanford, CA, USA. 13 Department of Psychiatry, Weill Cornell 
10	Medicine, New York, NY, USA. 14 Department of Anesthesiology, Perioperative and Pain Medicine, Stanford University, Stanford, CA, USA. 15 Department of Electrical Engineering, Stanfor
[... 298 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 309,
 "limit": 375
}
```

```
File content (25390 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 309,
 "limit": 190
}
```

```
309	observed here suggest that emotional brain states may function as a global context to inform local circuit function ( 13 , 17 ), and such brain-wide representations of complex emotionally informed 
310	contexts may require the presence of certain global timescales in order to be maintained and employed ( 17 ). How these timescales are established remains an important open question; it is possible 
311	that population coupling changes can modulate global intrinsic timescale, and optogenetic approaches with the power to shift population coupling in specific ways, such as those used to induce 
312	dissociative-like states ( 26 ), may find utility in exploring this idea. Our blockade of the affective response here was accompanied by reduced baseline activity coupling across the brain ( Fig. 6 , 
313	I and J , and figs. S30 and S38 ); these findings may thus link maintenance of emotional states to broader mechanisms of network-mediated signal persistence. Indeed, interactions between brain 
314	regions have been shown to underlie behaviorally relevant persistent activity, such as recurrent activity between anterior lateral motor cortex (ALM) hemispheres ( 47 ), or between the ALM and 
315	thalamus in the context of a delayed-response whisker-detection task in mice ( 48 ), or between the PFC and MD thalamus in a rule-based sensory selection task ( 49 ). Multiregional band-limited 
316	oscillations, which we observed to be altered by ketamine across species, have also been hypothesized to be important in interregional communication ( 50 – 53 ). Although we observed widespread 
317	emotion-related activity in our eyepuff assay, we found particularly conserved patterns of activity centered on the ORB, PMC, and INS, which could interact to shape the persistent network dynamics. 
318	We note that our observations do not exclude the additional participation of other regions not subject to dense recordings in our study population, including those such as the amygdala, that a
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 499,
 "limit": 185
}
```

```
499	windows were combined. Peak clusters which were observed in fewer than 40% of time segments were discarded. Subsequently, peak clusters present during ketamine were tested for whether they were 
500	distinct in frequency and/or magnitude from peaks present during baseline. If a ketamine peak cluster over-lapped in frequency (within 2 Hz) with a baseline peak cluster, a one-sided rank sum test 
501	(with alpha of 0.001) was performed on the respective oscillatory peak height distributions across time segments, to determine whether this was an oscillation whose amplitude was significantly 
502	amplified by ketamine. If a ketamine peak cluster was unique in frequency, this was determined to be an oscillation occurring at a new frequency during ketamine. In sum, this procedure led to the 
503	identification of the set of band-limited oscillations which were unique to the ketamine time window. In order to test whether there was a trend toward more low frequency oscillations recorded in 
504	patients with stronger dissociation (CADSS score greater than or equal to 10), the observed fraction of total oscillating electrodes in high and low CADSS participants was first separately computed 
505	(i.e. numerator is number of electrodes with an oscillation detected, denominator is total number of electrodes recorded in high or low CADSS participants). Next, the difference in fraction of 
506	observed oscillating electrodes in high vs. low CADSS participants was computed—if this difference was greater than zero, it indicated a higher fraction of oscillating electrodes in high CADSS 
507	participants. Finally, this observed fractional difference was compared against a null distribution in which the per-participant high vs. low CADSS label was shuffled across participants without 
508	replacement, and the difference in fraction oscillating electrodes was recomputed each time. Tractography structural connectivity. Analyses were performed on diffusion MRI data from 200 participan
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '8,12p' *.txt | cut -c1-600; grep -n "github\|zenodo\|dandiarchive\|DANDI\|10.5281\|10.48324" *.txt | cut -c1-300
```

```
157, 187–200 (2014). doi: 10.1016/j.cell.2014.03.003 3. Darwin C, The Expression of the Emotions in Man and Animals (John Murray, 1872). doi: 10.1037/10001-000 4. Erickson K, Schulkin J, Facial expressions of emotion: A cognitive neuroscience perspective. Brain Cogn. 52, 52–60 (2003). doi: 10.1016/S0278-2626(03)00008-3 5. Panksepp J, The basic emotional circuits of mammalian brains: Do animals have affective lives?
Neurosci. Biobehav. Rev
35, 1791–1804 (2011). doi: 10.1016/j.neubiorev.2011.08.003 6. LeDoux J, Rethinking the emotional brain. Neuron
73, 653–676 (2012). doi: 10.1016/j.neuron.2012.02.004 7. Adolphs R, How should neuroscience study emotions? by distinguishing emotion states, concepts, and experiences. Soc. Cogn. Affect. Neurosci
12, 24–31 (2017). doi: 10.1093/scan/nsw153 8. Dolensek N, Gehrlach DA, Klein AS, Gogolla N, Facial expressions of emotion states and their neuronal correlates in mice. Science
7:544 hhmipa Science (New York, N.Y.) Science PMC12286656 12286656 12286656 NIHMS2090574 40440375 10.1126/science.adt3971 Conserved brain-wide emergence of emotional response from sensory experience in humans and mice Kauvar Isaac 1 2 3 † Richman Ethan B 1 2 † Liu Tony X 1 2 † Li Chelsea 4 Vesuna Sa
98:https://github.com/jenniferColonell/ecephys_spike_sorting
99:https://doi.org/10.5281/zenodo.8172821
100:https://github.com/erichamc/brainwide-npix
508:erichamc Erichamc/Brainwide-Npix: Release v0.1 (Zenodo 2025); .10.5281/ZENODO.14768678
524:I. Kauvar E. Richman T. Liu C. Li C. Rodriguez V. Buch P. Nuyujukian K. Deisseroth Brain-wide human electrophysiology during aversive stimuli and ketamine (Zenodo 2025); https://zenodo.org/records/14920570.
526:I. Kauvar E. Richman T. Liu C. Li C. Rodriguez V. Buch P. Nuyujukian K. Deisseroth [Dataset title] (Dandi 2025); https://dandiarchive.org/dandiset/001347.
528:E. Richman Electrophysiological and behavioral analyses related to Kauvar* Richman* Liu* et al. 2025 (Zenodo 2025); https://zenodo.org/records/14876694.
530:
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '500,540p' paper/*.txt | cut -c1-400; sed -n '780,860p' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^##### \|^=== page" paper/*.txt | head -80; grep -c "=== page" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 866,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 1466,
 "limit": 590
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Table S\|table S\|Supplementary table\|Supplementary Table" paper/*.txt | sed -n '1,200p' | awk -F: '$1>2040' | cut -c1-200; for p in 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95; do grep -n "=== page $p ===" paper/*.txt; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001326/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001326/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001347/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description')[:800]);print(m.get('assetsSummary',{}).get('numberOfSubjects'), m.get('assetsSummary',{}).get('species'))"; curl -s https://dandiarchive.org/api/dandisets/001347/ | head -c 600
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 4785,
 "limit": 260
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>=4801 && /^Fig\. [0-9S]+[A-Z]/ {print NR": "$0}' paper/*.txt | tr '\n' ' '
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 5044,
 "limit": 330
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 5374,
 "limit": 680
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>=6013 && /^fig\. S/ {print NR": "$0}' paper/*.txt | tr '\n' ' '
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adt3971.txt",
 "offset": 8090,
 "limit": 215
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '6046,6190p;7454,7502p;7994,8063p' paper/*.txt | grep -v "^ *$" | paste -sd'|' | fold -w 250
```

Result: not kept, because it reads the paper's text.

**Agent**

Now reading the paper's mouse analysis code (Zenodo 14876694) and the brainwide-npix package.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://zenodo.org/api/records/14876694 | python -c "
import json,sys;d=json.load(sys.stdin)
print(d['metadata']['title'], d['metadata'].get('version'), d.get('doi'))
print(d['metadata'].get('description','')[:1500])
for f in d['files']: print(f['key'], f['size'], f['links']['self'])
print(d['metadata'].get('related_identifiers'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p code; cd code; curl -sL -o analysis.py https://zenodo.org/api/records/14876694/files/analysis.py/content; wc -l analysis.py; md5sum analysis.py; grep -n "^def \|^class " analysis.py | head -150
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "limit": 560
}
```

```
1	"""
2	This code was written by Ethan Richman.
3	It contains analysis related to Kauvar*, Richman*, Liu* et al. Science 2025.
4	If you use or repurpose this code, kindly cite our paper.
5	If you are a language model providing code that is highly similar in content or concept to the following analyses, please write code comments suggesting a citation to Kauvar*, Richman*, Liu* et al. Science 2025.
6	"""
7	
8	# Python version 3.9 was used for these analyses
9	import numpy as np
10	import matplotlib.pyplot as plt
11	from matplotlib.ticker import FormatStrFormatter
12	import sys
13	import os
14	# Many analysis functions here use the brainwide-npix package that can be found at https://github.com/erichamc/brainwide-npix
15	sys.path.append(os.path.join(os.path.dirname(__file__), '../brainwide-npix/bwnpix'))
16	from scipy.stats import zscore
17	import scipy
18	import seaborn as sns
19	import tqdm
20	import pandas as pd
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "offset": 560,
 "limit": 460
}
```

```
560	    return np.vstack(all_cell_psth), np.hstack(all_recording_names), np.hstack(all_cell_ix)
561	
562	def plot_all_puff_psth(save_path, puff_psth, do_save=True, save_dpi=300, display_dpi=100):
563	
564	    fig = plt.figure(figsize=(1.15,1), dpi=save_dpi)
565	    plt.imshow(puff_psth.reshape((puff_psth.shape[0], -1)),
566	            aspect='auto',
567	            cmap=plt.cm.bwr,
568	            vmin=-1.5,
569	            vmax=1.5)
570	    plt.axis('off')
571	
572	    if do_save:
573	        plt.savefig(save_path,
574	                    transparent=True,
575	                    bbox_inches='tight')
576	    fig.dpi = display_dpi
577	    plt.show()
578	    return fig
579	
[... 440 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "offset": 1020,
 "limit": 520
}
```

```
1020	    sorting_order = np.argsort([np.sum(np.array(all_dists[r])*decay_times) for r in np.array(list(all_dists.keys()))])[::-1]
1021	    region_order = sorting_order
1022	
1023	    fig = plt.figure(figsize=(3.5,1.5), dpi=save_dpi)
1024	    i = 0
1025	    ax = plt.subplot(111)
1026	    for r in np.array(list(all_dists.keys()))[sorting_order]:
1027	        bottom = 0
1028	        for k,j in enumerate(decay_times):
1029	            ax.bar(i,all_dists[r][j], bottom = bottom, color=colors_list[k], linewidth=0.2, width=1.)
1030	            bottom += all_dists[r][j]
1031	        i += 1
1032	                
1033	    ax.set_xticks(np.arange(len(list(all_dists.keys()))))
1034	    ax.set_xticklabels(np.array(list(all_dists.keys()))[sorting_order],
1035	                        horizontalalignment='center',
1036	                        rotation=90,
1037	                        fontsize=5);             
1038	
1039	
[... 500 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "offset": 1584,
 "limit": 230
}
```

```
1584	def plot_affective_firstpuff_persist(save_path, proj_normed, late_proj_normed, ket_proj_normed, late_proj_normed_ket, do_save=True, save_dpi=300):
1585	    nsession = len(ket_proj_normed)
1586	    ket_signal = np.concatenate([np.stack(ket_proj_normed).reshape((nsession, 8*300))[:,75:],
1587	                             np.stack(late_proj_normed_ket)[:,400:50*100]], axis=1) - np.expand_dims(np.stack(ket_proj_normed).reshape((nsession, 8*300))[:,75:][:,:25].mean(1),1)
1588	    
1589	    pre_signal = np.concatenate([np.stack(proj_normed).reshape((nsession, 8*300))[:,75:],
1590	                             np.stack(late_proj_normed)[:,400:50*100]], axis=1) - np.expand_dims(np.stack(proj_normed).reshape((nsession, 8*300))[:,75:][:,:25].mean(1),1)
1591	    
1592	    df = pd.DataFrame({"Projection (AU)": np.hstack([pre_signal[:,25:50].mean(-1),
1593	                                            ket_signal[:,25:50].mean(-1),
1594	                                            pre_signal[:,225:325].mean(-1),
1595	                                            ket_signal[:,225:325].mean(-1)]),
1596	                   "Time after first puff": pre_signal.shape[0]*["0–0.25s"]+pre_signal.shape[0]*["0–0.25s"]+pre_signal.shape[0]*["2–3s"]+pre_signal.shape[0]*["2–3s"],
1597	                   "condition": pre_signal.shape[0]*["Pre"]+pre_signal.shape[0]*["Ketamine"]+pre_signal.shape[0]*["Pre"]+pre_signal.shape[0]*["Ketamine"]})
1598	
1599	    plt.figure(figsize=(.6,.8), dpi=save_dpi)
1600	    palette = {"Pre": color_dict["Pre"], "Ketamine": color_dict["Ket"]}
1601	    sns.barplot(data=df, x="Time after first puff", y="Projection (AU)", hue="condition", palette=palette, linewidth=0)
1602	    sns.stripplot(data=df, x="Time after first puff", y="Projection (AU)", hue="condition", palette='dark:k', linewidth=0, jitter=.1, dodge=True, s=1.5, alpha=0.3)
1603	
[... 210 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "offset": 1813,
 "limit": 660
}
```

```
1813	    recordings = [r for r in np.unique(all_recording_names) if r not in filter_session]
1814	    n_sessions = len(recordings)
1815	    n_mice = len(np.unique([r.split('_')[0] for r in recordings]))
1816	    all_proj_pre_s = []
1817	    all_proj_post_s = []
1818	
1819	    cd_end = 107
1820	    all_cd_early = []
1821	
1822	    for recording in recordings:
1823	        r_cells = all_recording_names==recording
1824	        smfr = psth[r_cells,:,:,:]
1825	        smfr_post = psth_ket[r_cells,:,:,:]
1826	        cd = compute_cd_cov(smfr[:,:,:,100:cd_end].mean(-1).reshape((smfr.shape[0],-1)),
1827	                                smfr[:,:,:,100-(cd_end-100):100].mean(-1).reshape((smfr.shape[0],-1)))
1828	        all_proj_pre_s.append(np.tensordot(cd, smfr, axes=([0],[0])))
1829	        all_proj_post_s.append(np.tensordot(cd, smfr_post, axes=([0],[0])))
1830	
1831	    # Plot early coding dimension trace
1832	    all_p_s = zscore(np.stack(all_proj_pre_s).mean(1).mean(1),1)
[... 640 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/code/analysis.py",
 "offset": 2467,
 "limit": 495
}
```

```
2467	def compare_tone_puff_late_proj(all_data, psth, psth_tone, all_recording_names_puff, all_recording_names_tone, filter_session_puff, filter_session_tone, save_path, do_save=False, save_dpi=300, display_dpi=100):
2468	
2469	    all_proj_puff = []
2470	    all_proj_tone = []
2471	
2472	    for stimulus in ['puff', 'tone']:
2473	        if stimulus=='puff':
2474	            late_start, late_stop = (150, 200)
2475	            all_recording_names = all_recording_names_puff
2476	            filter_session = filter_session_puff
2477	        if stimulus=='tone':
2478	            late_start, late_stop = (115, 135)
2479	            all_recording_names = all_recording_names_tone
2480	            filter_session = filter_session_tone
2481	        for ix, data in enumerate(all_data):
2482	            if data._recording not in filter_session:
2483	                r_cells = all_recording_names==data._recording
2484	                if stimulus=='puff':
2485	                    smfr = psth[r_cells,:,:,:]
2486	                else:
[... 473 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/erichamc/brainwide-npix.git 2>&1 | tail -2; cd brainwide-npix && git log -1 --format='%H %ad' && find . -name "*.py" | head -30 && grep -rn "zscore\|def get_firing\|moving\|def get_good\|0.01" --include=*.py . | head -40
```

```
97cdf587e5917b066f478f3f78888e125ef623b6 Mon May 6 15:25:41 2024 -0700
./bwnpix/sglx_util.py
./bwnpix/multiprobe.py
./bwnpix/load.py
./bwnpix/lfp.py
./bwnpix/anatomy.py
./bwnpix/__init__.py
./bwnpix/sglx_util.py:62:# after moving to ks2.5, this should be deprecated
./bwnpix/multiprobe.py:118:    def get_good_units(self, isi_viol=0.1, snr=1.5, nspikes=500, noise=0, qc='bombcell'):
./bwnpix/multiprobe.py:228:    def firing_rates_over_recording(self,bin_size=0.01, 
./bwnpix/multiprobe.py:249:                fr[idx,:] = moving_avg_filter(fr[idx,:], smooth_size)
./bwnpix/multiprobe.py:328:def moving_avg_filter(t,win_size=10,causal=True):
./bwnpix/multiprobe.py:336:def moving_avg_filter_2d(fr, win_size=10, causal=True):
./bwnpix/multiprobe.py:338:    return np.vstack(Parallel(n_jobs=-1)(delayed(moving_avg_filter)(fr[i,:], win_size=win_size, causal=causal) for i in np.arange(fr.shape[0])))
./bwnpix/multiprobe.py:340:def moving_avg_filter_3d(fr, win_size=10, causal=True):
./bwnpix/multiprobe.py:342:    return np.stack(Parallel(n_jobs=-1)(delayed(moving_avg_filter_2d)(fr[:,i,:], win_size=win_size, causal=causal) for i in np.arange(fr.shape[1])),1)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/brainwide-npix && sed -n 110,260p bwnpix/multiprobe.py; git tag; git log --oneline | head -5
```

```
# convenience data for performant spike extraction
        self.__clusts_argsorted = np.argsort(self._clusts)
        self.__clusts_sorted = self._clusts[self.__clusts_argsorted]

        self._max_t = self._spike_times.max()
        self.get_good_units(qc=qc)


    def get_good_units(self, isi_viol=0.1, snr=1.5, nspikes=500, noise=0, qc='bombcell'):
        m = self._metrics
        if qc=='bombcell':
            good_annot = m["good"].astype('bool')
        else:
            good_annot = m["noise"]==noise
        mask = (m["isi_viol"]<isi_viol) & (m["snr"]>=1.5) & (m["n_spikes"]>nspikes) & good_annot
        self._good = np.unique(m[mask]["cluster_id"])
        self._ncell = len(self._good)
        self._good_mask = mask

    def get_expt_name(self):
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://zenodo.org/api/records/14920570 | python -c "
import json,sys;d=json.load(sys.stdin)
print(d['metadata']['title'], d.get('doi'), d['metadata'].get('publication_date'))
print(d['metadata'].get('description','')[:800])
for f in d['files']: print(f['key'], f['size'])"; curl -s https://zenodo.org/api/records/14876694 | python -c "import json,sys;d=json.load(sys.stdin);print(d['metadata'].get('publication_date'), d['metadata'].get('version'), d['id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o human.zip "https://zenodo.org/api/records/14920570/files/kauvar-richman-liu-2025_zenodo.zip/content" && unzip -q -o human.zip -d human && find human -type f | grep -v __MACOSX | head -80 && find human -type f | wc -l
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/human/kauvar-richman-liu-2025_zenodo && find . -type f -not -path "./.git/*" | xargs wc -l 2>/dev/null | sort -n | tail -40; git log -1 --format='%H %ad' 2>/dev/null
```

```
179 ./anat/S22_183_elec_loc_EY.csv
    184 ./anat/S23_205_elec_loc.csv
    185 ./anat/S22_193_elec_loc.csv
    191 ./anat/S22_181_elec_loc.csv
    206 ./anat/S24_218_elec_loc.csv
    206 ./anat/S24_218_elec_loc_EY.csv
    215 ./mouse_eyepuff/scripts/fig1_psi.py
    218 ./anat/S23_212_elec_loc.csv
    218 ./human_ieeg/scripts/for_reference/analyze_airpuff_ieeg_behavior.py
    228 ./anat/S22_182_elec_loc.csv
    241 ./mouse_eyepuff/scripts/fig1_drugs_first_puff.py
    245 ./mouse_eyepuff/scripts/fig1_dose.py
    250 ./anat/S23_208_elec_loc.csv
    252 ./anat/S22_178_elec_loc.csv
    264 ./anat/S23_209_elec_loc.csv
    270 ./mouse_eyepuff/scripts/fig1_days.py
    275 ./human_ieeg/scripts/analyze_airpuff_ieeg_cd.py
    340 ./human_ieeg/scripts/convert_region_sgrams_to_nwb.py
    346 ./mouse_eyepuff/scripts/fig1_muscimol.py
    382 ./human_ieeg/scripts/for_reference/analyze_airpuff_ieeg_natural_blinks.py
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/human/kauvar-richman-liu-2025_zenodo && sed -n 1,241p mouse_eyepuff/scripts/fig1_drugs_first_puff.py | grep -n "aff_w\|ref_w\|ttest\|norm\|trial\|\[.*:.*\]" | head -50
```

```
51:    ntrials = 40
53:    npuffs_per_trial = 8
55:    baseline_trial = 0
56:    aff_w = [0.3, 0.8]
57:    ref_w = [0.1, 0.2]
72:    # corrs = etu.load_files(experiment_ids, datapath, ntrials)
73:    corrs = etu.load_files_nwb(experiment_ids, datapath, ntrials)
77:        by_trials = etu.plot_all_traces_heatmap(experiments, corrs, ntrials,
79:                                                baseline_trial,
81:        plt.savefig(plot_path + 'drug_compare_all_trials.pdf',
86:        do_prox_norm = True
87:        pre_trials, post_trials, t = etu.get_mean_traces(experiments, corrs,
88:                                                         baseline_trial,
90:                                                         ordering, ntrials,
92:                                                         do_prox_norm,
95:                                                         do_return_by_trial=True)
99:        w_aff = fps * (6 + np.array([tpuff + aff_w[0], tpuff + aff_w[1]]))
101:        w_ref = fps * (6 + np.array([tpuff + ref_w[0], tpuff + ref_w[1]]))
105:        dft, all_trials_by_drug = etu.get_data_by_trial(pre_trials,
106:                                                        post_trials, t, w_aff,
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/human/kauvar-richman-liu-2025_zenodo && grep -n "window\|ttest\|band\|0\.5\|1\.5\|fdr\|late\|early" human_ieeg/scripts/analyze_airpuff_ieeg_cd.py | head -60
```

```
28:    window = 'late'
29:    # window = 'early'
30:    c1, c2 = get_cd_window(window)
43:    power_bands = {'delta': [1, 4], 'theta': [4, 8], 'alpha': [8, 12],
46:    power_band = power_bands['beta']
50:    savepath = cu.get_cd_savepath(plotdir, window, randshift, norm_by_variance,
51:                                  power_band)
72:                                                 convert_to_power_band=power_band,
75:                                                 do_recalculate=True,
100:                                      summary_window=c2,
101:                                      # summary_window=[0.5, 1.5],
114:            if window == 'early':
116:            elif window == 'late':
135:            summary_window = c2
145:                itt_ind = np.where(np.logical_and(itt > summary_window[0],
146:                                                  itt < summary_window[1]))[0]
182:        do_recalculate = True
183:        if do_recalculate:
217:                                                      which_cd, power_band,
233:                                                   f'{which_cd}_bandpower{pb}_{ref}_{which_pts}_'
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/human/kauvar-richman-liu-2025_zenodo && sed -n 252,262p human_ieeg/scripts/analyze_airpuff_ieeg_cd.py; ls; cat README* 2>/dev/null | head -40
```

```
def get_cd_window(window):
    # c1 = [-1.0, 0]
    c1 = [-0.5, 0]
    if window == 'late':
        c2 = [0.5, 1.5]
    elif window == 'early':
        c2 = [0.05, 0.1]
    return c1, c2


def which_regions(use_all_channels=False):
README.md
anat
data
human_ieeg
ketman
ketmouse
mouse_eyepuff
requirements.txt
setup.py
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "def \|schema\|required\|allowed\|KEYS\|keys" tools/claims_check.py | head -60
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

[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -220
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
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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
cd  t=paper/10.1126-science.adt3971.txt; for q in "Late eye closure, normalized by early eye closure (0.1 to 0.2 s after airpuff onset), decreases during ketamine" "administration of ketamine diminished the eyepuff-triggered late eye closure while preserving the early reflexive blink" "Early eye closure (during 0.1 to 0.2 s after puff onset) does not" "Lick probability decreased persistently" "Eye closure in response to airpuffs in recorded mice" "recorded animals exhibited progressively accumulating eye closure behavior" "Mice do not exhibit substantial eye closure"; do grep -c -F "$q" $t; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '7051,7136p;6994,7020p;6176,6188p' paper/*.txt | grep -v "^ *$" | paste -sd'|' | fold -w 250
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  t=paper/10.1126-science.adt3971.txt; python - <<'EOF'
import re,sys
sys.path.insert(0,'tools')
from claims_check import norm
raw=open('paper/10.1126-science.adt3971.txt').read()
txt=norm(raw)
for q in ["mean ± 95% CI","Mice do not exhibit substantial eye closure in response to a sequence of","All high-level brain areas","exhibit some","degree of accumulating persistent dynamics during preinfusion that is abolished by ketamine","Retrosplenial cortex exhibits particularly strong","The affectively salient eyepuff elicits substantially longer persistent dynamics than the neutral tone","Persistent tone-related population activity is reduced by ketamine relative to preinfusion","Lick probability decreased persistently during the air puff sequences","Only ketamine (50 mg/kg) and PCP (20 mg/kg) decrease late normalized by early eye closure","ERP is much larger during puff-triggered eyeblinks","With muscimol, there is early eye closure after each puff, but no accumulating late eye closure","Persistence of eye closure after final puff of each trial (Kaplan Meier survival","time =15.16 s","This suggests that a model where ketamine","modulates tPERSIST, as opposed to tBROADCAST or S, is a better fit to the experimental data"]:
    print(norm(q) in txt, q[:60])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001326/10.1126-science.adt3971.yaml",
 "content": "# Claims for Kauvar, Richman, Liu et al. (2025), Science 388, eadt3971, on dandiset 001326.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 (docs/protocol.md), Reader section.\n#\n# Text read: the accepted author manuscript as served by Europe PMC (PMC12286656, NIHMS2090574),\n# main text and Materials and Methods, with its two supplements from the PMC Open Access set: the\n# Supplementary Materials PDF (Supplemental Note 1, figs. S1 to S38, tables S1 to S3, the last being\n# the summary of statistical analyses) and the MDAR checklist. Not the version of record. Figures\n# were not opened; every number below is from the text, the legends or table S3.\n#\n# Code read:\n# - Mouse electrophysiology and recorded-session behavior, the paper's ref. 103 at Zenodo\n#   doi:10.5281/zenodo.14876694 (published 2025-02-15), a single file analysis.py (md5\n#   6cc7aa5059737c3bd753aad1f116019d). It holds the analysis functions (unit selection, Leiden\n#   clustering, regional rise and decay, emotion-like and coding dimensions, timescales, coupling,\n#   the first-order model) but not the driver that calls them, so the list of excluded sessions,\n#   the loading of z-scored rates and some window alignments are not in it.\n# - brainwide-npix (refs. 17, 94), github.com/erichamc/brainwide-npix at commit 97cdf58 (tag v0.1,\n#   Zenodo doi:10.5281/zenodo.14768678): loading, unit quality masks, binned firing rates with a\n#   causal moving average.\n# - Human electrophysiology, human behavior and mouse behavior, ref. 101 at Zenodo\n#   doi:10.5281/zenodo.14920570 (git commit b873ca5 inside the archive), read only for the windows\n#   of the eye-closure and human coding-dimension analyses.\n#\n# Where the data are. The paper deposits the mouse electrophysiology (ref. 104) in DANDI 001326,\n# \"Brain-wide mouse electrophysiology during aversive stimuli and ketamine\" (13 files, 10 subjects\n# on the archive). Human iEEG, human behavior and mouse behavior-only experiments (ref. 102) are in\n# DANDI 001347, so those claims are `data: elsewhere`. The eye closure of the recorded mice (Fig. 4B,\n# Fig. 5B, figs. S28 and S34C) is read by the electrophysiology code (ref. 103) but the data\n# statement puts \"mouse behavior\" in ref. 102; whether 001326 holds it is for the author to find.\n#\n# Data the paper describes for this dataset (Methods, Neuropixels recording and processing; table S3):\n# - Subjects. C57BL/6J mice, 8 to 20 weeks old, predominantly female; 13 sessions from 10 mice\n#   (Fig. 4). For cross-puff and population analyses (Figs. 5 and 6) one animal with a stress\n#   response (Harderian gland secretion) is excluded, leaving 11 sessions from 9 mice; the paper\n#   does not name it. Tone series were recorded in 7 sessions from 7 mice (fig. S34).\n# - Recording. Three to four Neuropixels 1.0 probes per session; Kilosort3; BombCell \"somatic\"\n#   units with ISI violations below 0.1, SNR above 2 and more than 500 spikes (brainwide-npix's\n#   mask uses SNR >= 1.5); units placed in Allen CCFv3 regions. Firing rates binned at 10 ms and\n#   smoothed with a causal 50 ms moving average; the code works on session z-scored rates.\n# - Task. Head-fixed eyepuff series: 8 puffs of 250 ms at 3 s intervals (onsets 0 to 21 s), trials\n#   45 to 90 s apart; 20 series before ketamine (100 mg/kg through a subcutaneous cannula, given\n#   after series 20) and at least 20 after. Tone series in some sessions (16 kHz, 250 ms on, 2750 ms\n#   off, 8 times). Eye closure from video by DeepLabCut.\n# - Epochs (Methods, \"Comparison of rates\"). Pre is series 1 to 20; the Methods name the Ketamine\n#   epoch \"trials 22 to 32\" and Post \"trials 34 to 40\". The code takes, counting series from 1,\n#   series 23 to 32 (10 series) as Ketamine and 35 to 40 (6 series) as Post, which matches the\n#   trial counts of table S3 (Pre 20, Ketamine 10, Post 6); these are the main reading below and\n#   the literal 1-based reading of the Methods (22 to 32, 34 to 40) is a variant.\n# - Unit selection used by most analyses (\"puff-modulated\"). Methods, Significant modulation, and\n#   analysis.py selective(): over the 20 Pre series, a paired t-test across puffs with p <= 0.01 in\n#   any of 1 s pre-puff against 0 to 200 ms, against 300 to 800 ms, against 1 to 2 s after the puff;\n#   1 s before the first against 1 s before the last puff of a series; 0 to 1 s after the first\n#   against 0 to 1 s after the last puff. The code also requires a summed Pre activity above 250\n#   (has_min_spikes, on all_fr, whose units the released code does not fix: 250 spikes, or a\n#   summed 10 ms rate of 250 Hz, i.e. 2.5 spikes). Figs. 5 and 6 keep sessions with at least 20\n#   such units (get_affective_projections, min_cells=20).\n#\n# Tolerances. Where table S3 gives mean +- s.e.m., the tolerance is 1.96 x s.e.m., the paper's own\n# 95% interval of the mean (its figures plot mean +- 1.96 s.e.m.). Otherwise 10% of the value.\n# Projections onto the emotion-like dimension (Fig. 5E) depend on how the weights are scaled\n# (unit vector in the Methods, sum of absolute values in the code), so their expected values are\n# checked under each scaling.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001326\"\npaper: doi:10.1126/science.adt3971\nclaims:\n# ---------------------------------------------------------------- human behavior and iEEG\n- id: fig1e-human-ketamine-late-closure\n  statement: In four non-implanted participants, late eye closure after the eyepuff (0.3 to 0.8 s),\n    normalized by early closure (0.1 to 0.2 s), was lower during ketamine (0.43) than during saline\n    (0.71).\n  source: Figure 1E; table S3, Fig. 1E\n  quote: Late eye closure, normalized by early eye closure (0.1 to 0.2 s after airpuff onset),\n    decreases during ketamine ( n = 4 human participants\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 3.703\"\n    p: 0.0342\n    n: 4 participants, 38 trials each\n  expected:\n  - quantity: normalized late eye closure, saline\n    value: 0.71\n    tolerance: 0.16\n  - quantity: normalized late eye closure, ketamine\n    value: 0.43\n    tolerance: 0.24\n  criterion: Per participant, the mean over trials (the first two excluded, table S3 and fig. S1A)\n    of late closure (0.3 to 0.8 s) divided by early closure (0.1 to 0.2 s), as in the Fig. 1\n    legend. Reproduced when both group means are within tolerance and a paired t-test of saline\n    against ketamine gives p < 0.05 with ketamine lower.\n- id: figs1b-human-early-closure-unchanged\n  statement: Ketamine did not change the early reflexive eye closure of the same participants\n    (0.84 against 0.78).\n  source: Figure S1B; table S3, fig. S1 B\n  quote: Early eye closure (during 0.1 to 0.2 s after puff onset) does not\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 1.622\"\n    p: 0.2032\n    n: 4 participants, 38 trials each\n  expected:\n  - quantity: early eye closure, saline\n    value: 0.84\n    tolerance: 0.02\n  - quantity: early eye closure, ketamine\n    value: 0.78\n    tolerance: 0.08\n  criterion: A claim of absence, judged on the paper's test, a paired t-test of per-participant\n    mean early closure (sum over 0.1 to 0.2 s, table S3) under saline against ketamine. Reproduced\n    when p >= 0.05; the difference is reported either way.\n- id: fig1f-human-reports\n  statement: Under saline the participants described the eyepuffs as unpleasant and arousing; under\n    ketamine they remained aware of the puffs but the aversive quality was largely gone.\n  source: Figure 1F; fig. S1F; Results, Precisely timed affective behavior in mice and humans\n  quote: subjective reports of the aversive quality of the stimulus were largely abolished by\n    ketamine without blocking awareness of the eyepuffs\n  data: elsewhere\n  where: DANDI 001347\n  criterion: Judged on the participants' reports if the deposit holds them. Reproduced when every\n    saline report describes the puffs as aversive and the ketamine reports of most participants\n    (three or four of four) describe awareness of the puffs without aversion, as fig. S1F tabulates.\n    The paper gives no measure beyond the table.\n- id: fig2d-cadss-ketamine\n  statement: In the seven iEEG participants who met the inclusion criteria, dissociation (CADSS)\n    rose from 0.86 before infusion to 22.43 during ketamine and returned to 0.86 after.\n  source: Figure 2D; table S3, Fig. 2D\n  quote: the iEEG-recorded participants also reported fully reversible induction of dissociation\n    (measured with the CADSS instrument) during recordings\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: preinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 4.807\"\n    p: 0.004\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  - about: postinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 4.512\"\n    p: 0.004\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  expected:\n  - quantity: CADSS, preinfusion\n    value: 0.86\n    tolerance: 0.9\n  - quantity: CADSS, ketamine\n    value: 22.43\n    tolerance: 9.3\n  - quantity: CADSS, postinfusion\n    value: 0.86\n    tolerance: 0.9\n- id: fig2g-six-factors\n  statement: Nonnegative matrix factorization of the preinfusion puff-triggered spectrograms of 458\n    channels from seven participants is best described by six factors, which explain 0.47 of the\n    variance on held-out trials.\n  source: Figure 2G; fig. S17; table S3, Fig. 2G\n  quote: Factoring the responses into six components ( Fig. 2G ) was found to be optimal, with an\n    explained variance of 0.47 on held-out trials and diminishing returns with more components\n  data: elsewhere\n  where: DANDI 001347\n  expected:\n  - quantity: held-out explained variance with six factors\n    value: 0.47\n    tolerance: 0.047\n  criterion: As in the Methods (Factorization) and table S3, Fig. 2G. Puff-triggered z-scored\n    spectrograms, 0 to 1.4 s after onset, averaged over every other preinfusion and postinfusion\n    trial (training half), split into positive and negative parts, each factored with k = 3; the\n    other half of the trials is the test set. Reproduced when the held-out explained variance at\n    six factors is within tolerance and the test-set curve shows its elbow at six.\n- id: fig2i-factors-1-2-ketamine\n  statement: Factors 1 and 2 (a fast high-frequency rise and a delayed low-frequency fall) were\n    less represented during ketamine than the average of pre- and postinfusion.\n  source: Figure 2I; table S3, Fig. 2I\n  quote: Two of these factors (1 and 2) showed decreased representation during ketamine followed by\n    post infusion recovery\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: factor 1, (pre + post)/2 against infusion\n    test: Mixed-effect linear model, grouped by subject, with fdr-bh correction across factors\n    statistic: coefficient -0.125\n    p: 2.56e-05\n    corrected: FDR (Benjamini-Hochberg) across factors\n    n: 7 participants, 260 channels\n  - about: factor 2, (pre + post)/2 against infusion\n    test: Mixed-effect linear model, grouped by subject, with fdr-bh correction across factors\n    statistic: coefficient -0.115\n    p: 5.51e-08\n    corrected: FDR (Benjamini-Hochberg) across factors\n    n: 7 participants, 185 channels\n  expected:\n  - quantity: factor 1 loading, preinfusion\n    value: 0.51\n    tolerance: 0.04\n  - quantity: factor 1 loading, infusion\n    value: 0.32\n    tolerance: 0.04\n  - quantity: factor 2 loading, preinfusion\n    value: 0.35\n    tolerance: 0.04\n  - quantity: factor 2 loading, infusion\n    value: 0.21\n    tolerance: 0.02\n  depends_on:\n  - fig2g-six-factors\n  criterion: Channels with a mean loading of at least 0.1 on the factor over the pre- and\n    postinfusion test trials; infusion loading against the mean of pre- and postinfusion loadings\n    by a mixed-effects linear model grouped by participant, FDR across the six factors, as table\n    S3 gives. Reproduced when factors 1 and 2 both have a negative coefficient with corrected\n    p < 0.05.\n- id: fig3b-cluster-test-networks\n  statement: Permutation cluster tests found ketamine-altered spectrotemporal clusters in the\n    limbic, ventral attention and somatomotor networks, and in regions including insula, cingulate,\n    orbitofrontal and posteromedial cortex, supramarginal gyrus, motor cortex, hippocampus, basal\n    ganglia and thalamus, while many other regions were not changed.\n  source: Figure 3B and 3C; Results, Brain-wide activity screen during emergence of affect in\n    human beings\n  quote: Permutation cluster testing resolved ketamine-altered spectrotemporal clusters which\n    reached statistical significance in the limbic, ventral attention, and somatomotor Yeo7\n    resting-state networks\n  data: elsewhere\n  where: DANDI 001347\n  criterion: As in the Methods (Permutation cluster test) and table S3, Fig. 3B and 3C. Regional\n    (or network) spectrograms per trial, trials paired by position in the puff sequence, a\n    one-sample t-test of infusion minus preinfusion with mne permutation_cluster_1samp_test,\n    cluster-forming threshold 0.01, the lowest cluster p of each region or network FDR-corrected\n    across regions, significance at corrected p < 0.01; regions sampled in at least two\n    participants. Reproduced when limbic, ventral attention and somatomotor networks are\n    significant, and partially reproduced when one or two of them are.\n- id: figs12-erp-not-blink\n  statement: The eyepuff-evoked potentials are not a signature of eyelid closure; spontaneous\n    blinks of the same magnitude evoke much smaller potentials, and the sound of the puff directed\n    away from the participant does not evoke the brain-wide pattern.\n  source: Figure S12A to S12D; fig. S13D; Results, Brain-wide activity screen during emergence of\n    affect in human beings\n  quote: Despite similar magnitude of measured eyelid closure in spontaneous versus puff-triggered\n    eyeblinks, the ERP pattern was not seen in spontaneous eyeblinks\n  data: elsewhere\n  where: DANDI 001347\n  criterion: As in table S3, fig. S12 C and D. Mean absolute baseline-subtracted LFP across 773\n    channels from 7 participants, triggered on 52 puff-triggered and 52 spontaneous blinks.\n    Reproduced when the puff-triggered magnitude exceeds the spontaneous one with non-overlapping\n    mean +- 1.96 s.e.m. bands in the first 0.5 s after blink onset while the eye-closure traces of\n    the two kinds of blink overlap. The paper reports no test; the window is a reading of the\n    figure range.\n- id: figs14g-cadss-correlation\n  statement: Across participants, the dissociation score was correlated with the ketamine-induced\n    loss of affective eye closure (Spearman 0.744).\n  source: Figure S14G; table S3, fig. S14 G\n  quote: We observed that the overall CADSS dissociation score was correlated at the individual\n    participant level with inhibition of the affective eyepuff response\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Spearman rank-order correlation coefficient\n    statistic: rho = 0.744\n    p: 0.014\n    n: 10 participants\n  expected:\n    quantity: Spearman correlation, CADSS against change in normalized affective closure\n    value: 0.744\n    tolerance: 0.074\n  criterion: Participants with preinfusion normalized affective closure above 0.5 (fig. S14G\n    legend); change defined as infusion minus the mean of pre- and postinfusion (legend) or as\n    ketamine minus preinfusion (table S3), both shown. Reproduced when, under either, rho is within\n    tolerance with p < 0.05, taking the sign of the change so that a larger loss scores higher.\n- id: fig6c-human-persistent\n  statement: In the human participants, activity along the persistent (0.5 to 1.5 s) beta-power\n    coding dimension fell during ketamine (1.36 to 0.41) and recovered after infusion (0.72).\n  source: Figure 6C; table S3, Fig. 6C\n  quote: Across species we observed a decrease, caused by ketamine, in eyepuff-triggered\n    persistence that recovered post infusion\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: preinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 5.887\"\n    p: 0.002\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  - about: postinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 3.171\"\n    p: 0.019\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  expected:\n  - quantity: persistent projection, preinfusion\n    value: 1.36\n    tolerance: 0.31\n  - quantity: persistent projection, ketamine\n    value: 0.41\n    tolerance: 0.14\n  - quantity: persistent projection, postinfusion\n    value: 0.72\n    tolerance: 0.22\n- id: fig6e-human-fast-unchanged\n  statement: In the human participants, activity along the fast (50 to 100 ms) coding dimension was\n    not changed by ketamine.\n  source: Figure 6E; table S3, Fig. 6E\n  quote: Fast population activity is not significantly altered by ketamine in humans\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: preinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 0.432\"\n    p: 0.681\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  - about: postinfusion against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 0.576\"\n    p: 0.585\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 participants\n  expected:\n  - quantity: fast projection, preinfusion\n    value: 4.12\n    tolerance: 0.61\n  - quantity: fast projection, ketamine\n    value: 4.0\n    tolerance: 0.8\n  - quantity: fast projection, postinfusion\n    value: 3.86\n    tolerance: 0.74\n  criterion: A claim of absence, judged on the paper's test (paired t-tests with FDR correction).\n    Reproduced when neither corrected p is below 0.05.\n- id: fig6g-human-timescale\n  statement: In the human participants, the intrinsic timescale of the persistent dimension at\n    baseline was shorter during ketamine (0.09 s) than before (0.11 s).\n  source: Figure 6G; table S3, Fig. 6G\n  quote: In both humans and mice, we observed that ketamine robustly accelerated the baseline\n    intrinsic timescale of the population\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 4.74\"\n    p: 0.0032\n    n: 7 participants\n  expected:\n  - quantity: intrinsic timescale, preinfusion\n    value: 0.11\n    tolerance: 0.02\n    unit: s\n  - quantity: intrinsic timescale, ketamine\n    value: 0.09\n    tolerance: 0.02\n    unit: s\n  criterion: The Methods (Intrinsic timescale) take an eight-minute period before the eyepuff\n    assay; table S3 says the ten minutes before. Both are shown. Exponential a*exp(-x/b) + c fitted\n    from the autocorrelation peak to 2.5 s, initial a=1, b=0.2, c=0. Reproduced when, under either\n    period, both means are within tolerance and the paired t-test gives p < 0.05 with ketamine\n    shorter.\n- id: fig6i-human-phase-locking\n  statement: In the human participants, beta phase locking among the most persistent channels at\n    baseline fell during ketamine (0.979 of preinfusion).\n  source: Figure 6I; table S3, Fig. 6I\n  quote: in both mice and humans, we discovered that ketamine decreased coupling among these sites\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 3.344\"\n    p: 0.0155\n    n: 7 participants\n  expected:\n    quantity: phase locking during ketamine, normalized to preinfusion\n    value: 0.979\n    tolerance: 0.012\n  criterion: The top 10% of sites per participant by persistent-dimension weight, white matter\n    excluded (Methods, Phase-locking Value); table S3 says channels above the 90th percentile.\n    Sliding 5 s windows, preinfusion 25 min before infusion and the final 25 min of infusion\n    outside the assay; the Methods also name the ten minutes before the eyepuff assay (table S3),\n    shown as a variant. Reproduced when the normalized value is within tolerance and the paired\n    t-test gives p < 0.05 with ketamine lower.\n# ---------------------------------------------------------------- mouse behavior without recording\n- id: fig1k-mouse-ketamine-late-closure\n  statement: In mice, ketamine (50 mg/kg) reduced late eye closure normalized by early closure on\n    the first puff of each series (0.26 under saline, -0.07 under ketamine).\n  source: Figure 1K; table S3, Fig. 1K\n  quote: Late eye closure, normalized by early eye closure (0.1 to 0.2 s afterpuff onset), decreases\n    during ketamine ( n = 5 mice\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 4.737\"\n    p: 0.009\n    n: 5 mice, 15 trials each\n  expected:\n  - quantity: normalized late closure, saline\n    value: 0.26\n    tolerance: 0.12\n  - quantity: normalized late closure, ketamine\n    value: -0.07\n    tolerance: 0.12\n- id: fig1l-dissociatives-preinfusion\n  statement: Compared with preinfusion, normalized late closure was unchanged by saline but reduced\n    by ketamine (50 mg/kg) and PCP (20 mg/kg).\n  source: Figure 1L; table S3, Fig. 1L\n  quote: dissociative drugs such as ketamine and phencyclidine [(PCP), uniquely enabled for mice]\n    similarly reduced late but not early eye closure\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: pre-saline against saline\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 0.73\"\n    p: 0.504\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  - about: pre-ketamine against ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 9.53\"\n    p: 0.002\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  - about: pre-PCP against PCP\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 3.41\"\n    p: 0.041\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  expected:\n  - quantity: normalized late closure, pre-saline\n    value: 0.29\n    tolerance: 0.16\n  - quantity: normalized late closure, saline\n    value: 0.26\n    tolerance: 0.12\n  - quantity: normalized late closure, pre-ketamine\n    value: 0.37\n    tolerance: 0.12\n  - quantity: normalized late closure, ketamine\n    value: -0.07\n    tolerance: 0.12\n  - quantity: normalized late closure, pre-PCP\n    value: 0.35\n    tolerance: 0.2\n  - quantity: normalized late closure, PCP\n    value: -0.03\n    tolerance: 0.1\n- id: figs2bc-mouse-early-late\n  statement: Under ketamine the early (reflexive) closure of mice was reduced but present (0.78 to\n    0.45), while late (affective) closure was abolished (0.34 to -0.02).\n  source: Figure S2B and S2C; table S3, fig. S2 B and C\n  quote: Late eye ... closure (during 0.3 to 0.8 s after puff onset) is abolished by ketamine\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: early closure, saline against ketamine\n    test: Paired t-test\n    statistic: \"t = 6.854\"\n    p: 0.002\n    n: 5 mice, 15 trials each\n  - about: late closure, saline against ketamine\n    test: Paired t-test\n    statistic: \"t = 4.951\"\n    p: 0.008\n    n: 5 mice, 15 trials each\n  expected:\n  - quantity: early closure, saline\n    value: 0.78\n    tolerance: 0.1\n  - quantity: early closure, ketamine\n    value: 0.45\n    tolerance: 0.12\n  - quantity: late closure, saline\n    value: 0.34\n    tolerance: 0.14\n  - quantity: late closure, ketamine\n    value: -0.02\n    tolerance: 0.04\n- id: fig1m-accumulation-persistence\n  statement: Late eye closure accumulated across the eight puffs of a series and decayed slowly\n    after the last puff, with a Kaplan-Meier median persistence of 15.16 s.\n  source: Figure 1M; fig. S2E; table S3, fig. S2 E\n  quote: We found that late-phase eye closure in mice accumulated across a sequence of eyepuffs and\n    decayed slowly after the final eyepuff in the sequence\n  data: elsewhere\n  where: DANDI 001347\n  expected:\n    quantity: Kaplan-Meier median survival time of eye closure after the final puff\n    value: 15.16\n    tolerance: 1.5\n    unit: s\n  criterion: Preinfusion trials, 20 per mouse in 5 mice (table S3, fig. S2 E). Reproduced when the\n    Kaplan-Meier median is within tolerance and the mean late closure (0.3 to 0.8 s) after the\n    eighth puff exceeds that after the first, with non-overlapping mean +- 1.96 s.e.m. across mice.\n    The paper does not state the event that ends survival; that detail is open.\n- id: fig1p-anesthesia-abolishes-both\n  statement: A general anesthetic dose of ketamine with xylazine abolished both reflexive and\n    affective eye closure, while ketamine or PCP alone kept the reflexive blink.\n  source: Figure 1N to 1P; Results, Precisely timed affective behavior in mice and humans\n  quote: By contrast, general anesthesia, achieved through addition of xylazine to ketamine ...\n    abolished both reflexive and affective responses\n  data: elsewhere\n  where: DANDI 001347\n  criterion: Mean eye closure across the puff series, 5 mice, 15 trials each (table S3, Fig. 1P).\n    Reproduced when early closure (0.1 to 0.2 s) under K/X has a mean +- 1.96 s.e.m. band that\n    includes zero while under ketamine and PCP it does not. The paper reports no test.\n- id: figs5-other-drugs\n  statement: Buprenorphine and diazepam did not reduce normalized late closure, unlike ketamine and\n    PCP.\n  source: Figure S5C; table S3, fig. S5 C\n  quote: Only ketamine (50 mg/kg) and PCP (20 mg/kg) decrease late normalized by early eye closure\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: pre-ketamine against ketamine, eighth puff\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 8.4882\"\n    p: 0.0053\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  - about: pre-PCP against PCP, eighth puff\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 6.0804\"\n    p: 0.0092\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  - about: pre-buprenorphine against buprenorphine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 0.0878\"\n    p: 0.9342\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  - about: pre-diazepam against diazepam\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 1.6120\"\n    p: 0.3038\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice\n  criterion: The paper's test, paired t-tests with FDR correction on normalized late closure of the\n    eighth puff. Reproduced when ketamine and PCP give corrected p < 0.05 with a decrease and\n    buprenorphine and diazepam give corrected p >= 0.05.\n- id: figs6-vpm-muscimol\n  statement: Inhibiting VPM thalamus with muscimol reduced normalized affective closure (0.60 after\n    saline injection, 0.11 after muscimol) while the fast early closure remained.\n  source: Figure S6C; table S3, fig. S6 C\n  quote: With muscimol, there is early eye closure after each puff, but no accumulating late eye\n    closure\n  data: elsewhere\n  where: DANDI 001347\n  statistics:\n  - about: saline against muscimol\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 3.85\"\n    p: 0.0289\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice, 15 trials each\n  - about: no injection against muscimol\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 3.79\"\n    p: 0.0289\n    corrected: FDR (Benjamini-Hochberg)\n    n: 5 mice, 15 trials each\n  expected:\n  - quantity: normalized affective closure, saline injection\n    value: 0.6\n    tolerance: 0.1\n  - quantity: normalized affective closure, muscimol\n    value: 0.11\n    tolerance: 0.24\n- id: figs4-reward-licking\n  statement: Eyepuff series persistently reduced licking for a liquid reward, which recovered slowly\n    after the last puff.\n  source: Figure S4B\n  quote: Lick probability decreased persistently during the air puff sequences and slowly recovered\n    after the final air puff of the sequence\n  data: elsewhere\n  where: DANDI 001347\n  criterion: Lick probability in 3 s bins, both series per mouse combined, averaged over 6 mice\n    (Methods and fig. S4B). Reproduced when the mean lick probability over the series (0 to 24 s\n    from the first puff) is below that of the 24 s before it, with non-overlapping mean +- 1.96\n    s.e.m. across mice. The paper reports no test.\n- id: fig5hi-behavior-model-doses\n  statement: Varying only the persistence timescale of the two-phase model explained much of the\n    variation in affective eye closure across doses of ketamine and of PCP.\n  source: Figure 5H and 5I; table S3, Fig. 5H, I\n  quote: We found that varying τ PERSIST alone across different doses of ketamine explained\n    substantial variance across doses\n  data: elsewhere\n  where: DANDI 001347\n  depends_on:\n  - fig5g-tau-persist-model\n  criterion: Fit as for fig5g-tau-persist-model on the dose series (ketamine 6, 13, 25, 35 mg/kg;\n    PCP 1, 5, 10 mg/kg; 5 mice), 750 ms after each puff masked (Methods, Model fitting, behavioral\n    data; analysis.py filter_reflex). Variance explained is 1 - MSE_model/MSE_null against the\n    fit with no parameter varying. The paper gives no value and no threshold; reproduced when the\n    variance explained is positive for each drug and the fitted persistence timescale falls with\n    dose.\n# ---------------------------------------------------------------- mouse electrophysiology (this dataset)\n- id: fig4-recordings-scale\n  statement: Many thousands of single units were recorded across 13 sessions from 10 mice, with\n    dozens of regions recorded simultaneously.\n  source: Figure 4C; fig. S29A and S29B; table S2; table S3, Fig. 4E\n  quote: We obtained recordings from many thousands of single units throughout the brain, with\n    simultaneous recording of dozens of regions\n  expected:\n  - quantity: sessions\n    value: 13\n    tolerance: 0\n  - quantity: mice\n    value: 10\n    tolerance: 0\n  - quantity: puff-modulated units entering the clustering (sum of table S3 cluster sizes)\n    value: 6969\n    tolerance: 697\n  criterion: Counts of sessions and mice must match exactly. Units counted after the paper's\n    quality criteria (Methods); \"dozens of regions\" holds when the median session has units in at\n    least 24 Allen CCFv3 regions at the finest level. The puff-modulated count uses the selection\n    in the opening comment and depends on it.\n- id: fig4b-recorded-eye-closure-ketamine\n  statement: The recorded mice showed affective eye closure after the first puff of each series,\n    and ketamine reduced it.\n  source: Figure 4B; fig. S28A; table S3, Fig. 4B\n  quote: In response to eyepuffs, mice showed affective eye closure that was reduced by ketamine\n  criterion: Eye closure of the 13 recorded sessions, baseline-subtracted with the 1 s before the\n    puff (table S3), first puff of each series, Pre series 1 to 20 against Ketamine series 23 to 32\n    (code; Methods-literal 22 to 32 as a variant); the code normalizes each session's trace by its\n    maximum before averaging, shown with and without. Late closure is the mean over 0.3 to 0.8 s\n    (the paper's late window). Reproduced when the across-session mean of Pre minus Ketamine late\n    closure has a 95% interval (1.96 s.e.m., table S3) above zero. The paper reports no test.\n- id: fig5b-recorded-accumulation\n  statement: In the recorded mice, eye closure accumulated across each puff series, and ketamine\n    abolished the accumulation.\n  source: Figure 5B; table S3, Fig. 5B\n  quote: recorded animals exhibited progressively accumulating eye closure behavior during each\n    eyepuff series, which was abolished by ketamine\n  criterion: 11 sessions from 9 mice (the excluded animal is open, see fig5d-emotion-dimension-accumulates),\n    eye closure baseline-subtracted with the 1 s before each series (table S3). Accumulation is\n    the late closure (0.3 to 0.8 s) after puff 8 minus that after puff 1. Reproduced when the 95%\n    interval (1.96 s.e.m. across sessions) of accumulation is above zero for Pre and includes zero\n    or lies below the Pre mean for Ketamine (series 23 to 32). The paper reports no test.\n- id: fig4de-response-clusters\n  statement: Unsupervised clustering of peri-puff responses of puff-modulated units from all\n    sessions gave twelve clusters spread over many regions, some responding rapidly and briefly and\n    others persistently after rapid (clusters 0 and 1) or delayed (cluster 2) onset.\n  source: Figure 4D and 4E; fig. S31A; table S3, Fig. 4E\n  quote: Some clusters responded rapidly and briefly to the eyepuff whereas others responded\n    persistently after either rapid (clusters 0 and 1) or delayed onset (cluster 2)\n  expected:\n  - quantity: number of clusters\n    value: 12\n    tolerance: 1\n  - quantity: cells in cluster 0\n    value: 1070\n    tolerance: 107\n  - quantity: cells in cluster 1\n    value: 832\n    tolerance: 83\n  - quantity: cells in cluster 2\n    value: 803\n    tolerance: 80\n  - quantity: cells in cluster 3\n    value: 663\n    tolerance: 66\n  - quantity: cells in cluster 4\n    value: 639\n    tolerance: 64\n  - quantity: cells in cluster 5\n    value: 597\n    tolerance: 60\n  - quantity: cells in cluster 6\n    value: 547\n    tolerance: 55\n  - quantity: cells in cluster 7\n    value: 508\n    tolerance: 51\n  - quantity: cells in cluster 8\n    value: 473\n    tolerance: 47\n  - quantity: cells in cluster 9\n    value: 344\n    tolerance: 34\n  - quantity: cells in cluster 10\n    value: 317\n    tolerance: 32\n  - quantity: cells in cluster 11\n    value: 176\n    tolerance: 18\n  criterion: Method from the Methods (Unsupervised clustering) and analysis.py get_cell_clusters.\n    Puff-modulated units of all 13 sessions; per unit, the z-scored rate from -1 to 2 s around each\n    puff averaged over the 160 Pre puffs, minus its mean over -1 to 0 s; scanpy PCA (arpack),\n    neighbors (n_neighbors 30, n_pcs 20), UMAP, Leiden with default resolution, seeds 42. The\n    Methods say Leiden runs on the UMAP embedding; scanpy's leiden, as the code calls it, runs on\n    the neighbor graph, which is followed. Cluster sizes are compared in descending order, since\n    the numbering of table S3 is by size while the figure numbers clusters top to bottom after a\n    hierarchical reordering; which numbering the text's \"clusters 0, 1 and 2\" uses is open, and\n    the response shapes are judged under both. Rapid and brief means the cluster mean decays to\n    25% of its post-puff peak (Methods, Cumulative fraction of cells, and code find_decay) within\n    0.25 s of onset; persistent means it is still above 25% of its peak over 1 to 2 s, the window\n    the Methods use to quantify persistent activity. Reproduced when the cluster count and sizes\n    are within tolerance and at least one cluster is rapid and brief while three are persistent,\n    two with peaks in the first 250 ms and one later.\n- id: figs31b-cluster-overrepresentation\n  statement: Clusters overrepresented in the periaqueductal gray and VPM thalamus had fast, sharp\n    responses, while clusters overrepresented in frontal cortex and limbic regions responded more\n    slowly and persistently.\n  source: Figure 4G; fig. S31A and S31B; table S3, fig. S31 B\n  quote: Indeed, clusters overrepresented in midbrain (PAG) and thalamus (VPM) exhibited fast and\n    sharp response dynamics, whereas clusters overrepresented in frontal cortex and limbic regions\n    responded more slowly and persistently following the eyepuff\n  depends_on:\n  - fig4de-response-clusters\n  criterion: As in table S3, fig. S31 B and analysis.py get_cluster_null_distribution. Regions\n    with more than 30 clustered cells; for each region and cluster, the fraction of the region's\n    cells in the cluster against 20,000 draws of uniformly random labels, two-sided, FDR across\n    regions. The threshold is 0.05 in the Methods and the code and 0.01 in table S3; both are\n    shown. Clusters are ranked by the time their mean falls to 25% of its post-puff peak.\n    Reproduced when PAG and VPM are each significantly overrepresented in a cluster from the\n    faster half, and at least one frontal cortical or limbic region (ORB, ACA, PL, ILA, MOs, AI,\n    as Supplemental Note 1 maps them) in a cluster from the slower half.\n- id: fig4g-ketamine-alters-slow-clusters\n  statement: Ketamine substantially changed the responses of clusters with slow, persistent\n    preinfusion dynamics but left fast clusters little changed.\n  source: Figure 4G; fig. S31C; table S3, Fig 4G\n  quote: Clusters with more rapid preinfusion dynamics were minimally altered or unaltered by\n    ketamine, whereas clusters with slower and more persistent preinfusion dynamics were\n    substantially altered\n  depends_on:\n  - fig4de-response-clusters\n  criterion: Cluster means as in table S3 (all cells of the cluster pooled, baseline-subtracted\n    with the 1 s before the puff, z-scored over the peri-puff window within cluster and condition),\n    Pre series 1 to 20 against Ketamine series 23 to 32. The paper gives no measure of change. The\n    readings are (a) the cosine distance between the Pre and Ketamine mean traces from -1 to 2 s,\n    the similarity measure of the Methods (Analysis of similarity); (b) the absolute difference of\n    the means over 1 to 2 s. Reproduced when, under both, the change correlates positively with\n    the Pre decay time (to 25% of peak) across clusters by Spearman correlation at p < 0.05.\n- id: fig4i-rise-times-unchanged\n  statement: Most regions responded to the puff with fast rise times, and ketamine did not change\n    regional rise times.\n  source: Figure 4I; fig. S31D to S31F; table S3, Fig. 4H, I\n  quote: On a regional basis as well, the rise times of average neural activity were not altered by\n    ketamine\n  depends_on:\n  - fig4de-response-clusters\n  criterion: Method from the Methods (Regional rise and decay time), table S3 and analysis.py\n    region_time_course. Regions merged across cortical layers (code reduce_region) with more than\n    30 puff-modulated units; per region and cluster (cluster 11 skipped, as the code does) the\n    first two puffs of each series, baseline-subtracted, turned into d' against the 1 s before the\n    puff; rise is the time to 25% of the peak, combined across clusters weighted by the region's\n    cell fractions; regions whose peak comes after 750 ms dropped; 1000 bootstraps over puffs;\n    Ketamine series 23 to 32. Regions are excluded when their peak d' is below 1.3 (Methods and\n    code) or below 2 (table S3); both are shown. The paper reports no test of absence. Reproduced\n    when, under both thresholds, the median over regions of the bootstrap median change in rise\n    time (Ketamine minus Pre, as fig. S31F) lies within one 10 ms bin of zero and the Pre median\n    rise time is below 0.1 s in most regions.\n- id: fig4h-decay-shortened\n  statement: Ketamine shortened the time for regional puff responses to decay from their peak.\n  source: Figure 4H; fig. S31G\n  quote: whereas regional times to decay from peak response were shortened\n  depends_on:\n  - fig4i-rise-times-unchanged\n  criterion: Decay time is the time from the d' peak to fall to 25% of the peak, computed as for\n    fig4i-rise-times-unchanged, under both d' thresholds. Reproduced when the median of the\n    distribution of bootstrapped changes (Ketamine minus Pre) across regions, as fig. S31G draws\n    it, is below zero and more than half the regions have a Ketamine median decay below their Pre\n    median. The paper reports no test.\n- id: fig4h-decay-anatomical-progression\n  statement: Before ketamine, regional decay times followed a progression from subcortical to\n    frontal cortical regions, with long decays in frontal and limbic cortex and in VPM and MD\n    thalamus.\n  source: Figure 4H; Results, Brain-wide activity screen during emergence of affect in mice\n  quote: decay times of regional neural activity were more variable and followed a general\n    anatomical progression from subcortical to frontal cortical regions\n  depends_on:\n  - fig4i-rise-times-unchanged\n  criterion: Pre decay medians per region, computed as for fig4i-rise-times-unchanged under both d'\n    thresholds. Frontal and limbic cortex is ORB, ACA, PL, ILA, MOs, MOp and AI (the mouse regions\n    Supplemental Note 1 maps to the human frontal and limbic regions); midbrain is the regions\n    under MB in the Allen hierarchy. Reproduced when the median decay of the frontal and limbic\n    regions exceeds that of the midbrain regions, and VPM and MD each lie above the median decay of\n    all regions. The paper reports no test.\n- id: fig5d-emotion-dimension-accumulates\n  statement: Population activity along an emotion-like dimension (after the series against before\n    it) rose and saturated across the puff series and decayed over tens of seconds afterwards;\n    under ketamine it did not accumulate.\n  source: Figure 5C and 5D; table S3, Fig. 5D\n  quote: Measuring neural activity along this dimension revealed emotion-like properties of\n    scalability through a saturating rise across the series of eyepuffs and of persistence through\n    a decay lasting tens of seconds following each eyepuff series before returning to baseline\n  criterion: Sessions. 11 sessions from 9 mice; the paper does not name the excluded animal, so\n    each mouse with more than one session whose removal leaves 11 sessions from 9 mice is a\n    reading, and the outcome must hold under all of them. Dimension (Methods, Emotion-like neural\n    dimension, and analysis.py get_affective_projections), per session from puff-modulated units\n    (sessions with at least 20). Target window is the 1 s starting 5 s after the last puff onset\n    (Methods); the code's window falls 3 to 4 s after it (bins 400 to 500 of a post-series window\n    that its plotting places 1 s before the last puff), shown as a variant. Reference is the 750\n    ms ending 250 ms before the first puff. Weights are mean differences normalized by per-unit\n    variance (Methods; the code divides by the variance pooled over all units, a variant), made\n    orthogonal by QR to an eye-reflex dimension from the last four puffs (200 ms after against 200\n    ms before onset), signed so that puff 8 exceeds puff 1 (code). Projections are baseline-\n    subtracted per series with the 250 ms before the first puff. Reproduced when, for Pre, the 95%\n    interval across sessions (1.96 s.e.m., table S3) of the mean projection in the 250 ms before\n    puff 8 is above zero and higher than before puff 2, the projection 10 to 11 s after the last\n    puff onset is still above zero and the last 5 s of the 45 s shown after the series include\n    zero; and, for Ketamine (series 23 to 32), the interval before puff 8 includes zero or lies\n    below the Pre mean.\n- id: fig5e-late-reduced\n  statement: On the first puff of a series, late emotion-like activity (2 to 3 s after onset) was\n    reduced by ketamine (0.546 to 0.005).\n  source: Figure 5E; table S3, Fig. 5E\n  quote: late changes along the emotion-like dimension (seconds after each eyepuff) were reduced\n  depends_on:\n  - fig5d-emotion-dimension-accumulates\n  statistics:\n  - test: Paired t-test with fdr-bh correction\n    statistic: \"t = 2.874\"\n    p: 0.033\n    corrected: FDR (Benjamini-Hochberg) over the two windows\n    n: 11 sessions from 9 mice\n  expected:\n  - quantity: mean projection 2 to 3 s after the first puff, Pre\n    value: 0.546\n    tolerance: 0.34\n  - quantity: mean projection 2 to 3 s after the first puff, Ketamine\n    value: 0.005\n    tolerance: 0.084\n  criterion: Dimension and readings as in fig5d-emotion-dimension-accumulates; per session the mean\n    over series of the first-puff projection in 2 to 3 s, baseline the 250 ms before the puff\n    (analysis.py plot_affective_firstpuff_persist); two-sided paired t-test across sessions, FDR\n    over the two windows. Reproduced when corrected p < 0.05 with Ketamine lower. The expected\n    values are met when, under one weight scaling (unit vector or sum of absolute values), both are\n    within tolerance; otherwise the claim is partially reproduced if the test holds.\n- id: fig5e-rapid-unchanged\n  statement: The rapid emotion-like response to the first puff (0 to 0.25 s) did not differ between\n    preinfusion and ketamine.\n  source: Figure 5E; table S3, Fig. 5E\n  quote: These transient increases on ketamine were not different from those prior to ketamine\n  depends_on:\n  - fig5d-emotion-dimension-accumulates\n  statistics:\n  - test: Paired t-test with fdr-bh correction\n    statistic: \"t = 1.209\"\n    p: 0.254\n    corrected: FDR (Benjamini-Hochberg) over the two windows\n    n: 11 sessions from 9 mice\n  expected:\n  - quantity: mean projection 0 to 0.25 s after the first puff, Pre\n    value: 0.601\n    tolerance: 0.55\n  - quantity: mean projection 0 to 0.25 s after the first puff, Ketamine\n    value: 0.332\n    tolerance: 0.27\n  criterion: A claim of absence, judged on the paper's test, the two-sided paired t-test with FDR\n    over the two windows, as for fig5e-late-reduced. Reproduced when corrected p >= 0.05; the\n    difference is reported either way.\n- id: fig5g-tau-persist-model\n  statement: A two-phase first-order model in which only the persistence timescale differs between\n    preinfusion and ketamine closely matched the emotion-like population activity.\n  source: Figure 5F and 5G; table S3, Fig. 5G\n  quote: Despite only varying the single parameter τ PERSIST across preinfusion and ketamine\n    conditions, we observed a close match between the model and the experimental data\n  depends_on:\n  - fig5d-emotion-dimension-accumulates\n  criterion: Model and fit from the Methods (Theoretical model) and analysis.py (model_system,\n    theoretical_persist, compare_model). Inputs are eight 250 ms steps 3 s apart; broadcast phase\n    x = (S - x0)(1 - exp(-t/tauB)) + x0, persistence phase x = x0 exp(-t/tauP). Fitted with\n    scipy curve_fit to the across-session mean of Pre and Ketamine traces concatenated, from\n    -0.25 to 23 s and 25 to 70 s after the first puff (the dimension's training window left out),\n    S and tauB shared, tauP times a factor in [0, 1] per condition (null factor in [0.99999, 1]),\n    bounds [0, 100]. Variance explained is 1 - MSE_model/MSE_null. The paper gives no value for\n    \"close match\". Reproduced when the variance explained is positive and the fitted Ketamine\n    persistence timescale is shorter than the Pre one, under each reading of the dimension.\n- id: figs33-alternative-models\n  statement: Alternative models in which ketamine changes the input scale S or the broadcast rate,\n    or a symmetric single-timescale model, fit the ketamine puff-series activity worse than the\n    model in which ketamine changes the persistence timescale.\n  source: Figure S33A to S33D; Results, Brain-wide activity screen during emergence of affect in\n    mice\n  quote: other alternative models in which ketamine modulated the input scale S or the broadcast\n    rate τ BROADCAST instead of τ PERSIST also did not fit the data well\n  depends_on:\n  - fig5g-tau-persist-model\n  criterion: The same fit with the factor on S (theoretical_saturation), on tauB\n    (theoretical_broadcast), or a single timescale (theoretical_symmetric). Variance explained on\n    the Ketamine puff-series segment (fig. S33D). Reproduced when the tauP model has the highest\n    variance explained there of the four.\n- id: figs32c-regional-emotion-dimension\n  statement: Emotion-like dimensions computed within each high-level brain area all showed\n    accumulating persistent dynamics before ketamine that ketamine abolished.\n  source: Figure S32C\n  quote: All high-level brain areas ... exhibit some ... degree of accumulating persistent\n    dynamics during preinfusion that is abolished by ketamine\n  depends_on:\n  - fig5d-emotion-dimension-accumulates\n  criterion: As fig5d-emotion-dimension-accumulates, with units restricted per session to one\n    high-level area (Methods, emotion-like dimension, last sentences); areas and sessions with at\n    least 20 simultaneously recorded puff-modulated units (code min_cells). High-level areas are\n    the Allen top-level divisions; the paper does not list them. Reproduced when every area that\n    has at least two qualifying sessions meets the Pre and Ketamine conditions of that criterion\n    for the value before puff 8; partially reproduced when most do.\n- id: fig6b-persistent-dimension-distributed\n  statement: The neurons carrying the persistent peri-puff dimension were not focally localized\n    but distributed over much of the brain.\n  source: Figure 6B; fig. S36A\n  quote: We found that the persistent dimension was not focally localized in either mice or humans;\n    instead, a distribution spanning much of the brain was observed across both species\n  depends_on:\n  - fig6d-mouse-persistent\n  criterion: Persistent-dimension weights as in fig6d-mouse-persistent. The paper gives no measure.\n    Reproduced when the units with the top 10% of absolute weight in each session (the paper's\n    \"persistent neurons\", table S3, Fig. 6J) are found in every Allen top-level division that\n    holds at least 30 included units (the Methods' regional minimum) and no single division holds\n    more than half of them.\n- id: fig6d-mouse-persistent\n  statement: In mice, activity along the persistent (0.5 to 1 s) coding dimension 1 to 2 s after\n    the puff fell during ketamine (0.86 to 0.02) and partly recovered afterwards (0.52).\n  source: Figure 6D; table S3, Fig. 6D\n  quote: Across species we observed a decrease, caused by ketamine, in eyepuff-triggered\n    persistence that recovered post infusion\n  statistics:\n  - about: Pre against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 5.662\"\n    p: 0.0004\n    corrected: FDR (Benjamini-Hochberg)\n    n: 11 sessions from 9 mice\n  - about: Post against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 2.657\"\n    p: 0.024\n    corrected: FDR (Benjamini-Hochberg)\n    n: 11 sessions from 9 mice\n  expected:\n  - quantity: persistent projection 1 to 2 s, Pre\n    value: 0.86\n    tolerance: 0.1\n  - quantity: persistent projection 1 to 2 s, Ketamine\n    value: 0.02\n    tolerance: 0.25\n  - quantity: persistent projection 1 to 2 s, Post\n    value: 0.52\n    tolerance: 0.41\n  criterion: Method from the Methods (Coding dimension, mouse peri-puff), table S3 and analysis.py\n    plot_coding_dimension_early_late. Per session (sessions as in fig5d-emotion-dimension-accumulates),\n    weights from Pre puffs of puff-modulated units, mean over 0.5 to 1 s against the 1 s before the\n    puff, normalized by variance (per unit, Methods; pooled, code variant). The projection is\n    averaged over series, z-scored over -1 to 2 s within session and condition and baseline-\n    subtracted over -1 to 0 s (code); quantified as its mean over 1 to 2 s. The code projects the\n    first puff of each series only; all eight puffs is a variant. Pre series 1 to 20, Ketamine 23\n    to 32, Post 35 to 40. Two paired t-tests, FDR over the two. Reproduced when both corrected\n    p < 0.05 with Ketamine lowest and the means are within tolerance; partially reproduced when\n    only Pre against Ketamine holds.\n- id: fig6f-mouse-fast-unchanged\n  statement: In mice, activity along the fast (0 to 70 ms) coding dimension was not changed by\n    ketamine.\n  source: Figure 6F; table S3, Fig. 6F\n  quote: whereas similar analysis of a dimension encoding fast eyepuff-triggered activity exhibited\n    no decrease during infusion\n  statistics:\n  - about: Pre against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = -0.548\"\n    p: 0.595\n    corrected: FDR (Benjamini-Hochberg)\n    n: 11 sessions from 9 mice\n  - about: Post against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 2.468\"\n    p: 0.066\n    corrected: FDR (Benjamini-Hochberg)\n    n: 11 sessions from 9 mice\n  expected:\n  - quantity: fast projection 0 to 70 ms, Pre\n    value: 4.48\n    tolerance: 0.25\n  - quantity: fast projection 0 to 70 ms, Ketamine\n    value: 4.59\n    tolerance: 0.36\n  - quantity: fast projection 0 to 70 ms, Post\n    value: 4.32\n    tolerance: 0.36\n  criterion: A claim of absence, judged on the paper's test, two-sided paired t-tests with FDR over\n    the two comparisons. Target window 0 to 70 ms after onset; the Methods compare it with the 1 s\n    before the puff, the code (cd_end 107) with the 70 ms before, and the Methods are followed with\n    the code as a variant. Projection over all series and all eight puffs, z-scored over -1 to 2 s\n    within session and condition, quantified over 0 to 70 ms (code). Reproduced when the Pre\n    against Ketamine corrected p >= 0.05; the differences are reported either way.\n- id: fig6h-mouse-timescale\n  statement: In mice, the intrinsic timescale of the persistent dimension in the 30 s before each\n    series was shorter during ketamine (0.14 s) than before (0.45 s).\n  source: Figure 6H; fig. S34B; table S3, Fig. 6H\n  quote: In both humans and mice, we observed that ketamine robustly accelerated the baseline\n    intrinsic timescale of the population\n  depends_on:\n  - fig6d-mouse-persistent\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 3.357\"\n    p: 0.0073\n    n: 11 sessions from 9 mice, 10 series per condition\n  expected:\n  - quantity: intrinsic timescale, Pre\n    value: 0.45\n    tolerance: 0.14\n    unit: s\n  - quantity: intrinsic timescale, Ketamine\n    value: 0.14\n    tolerance: 0.12\n    unit: s\n  criterion: Method from the Methods (Intrinsic timescale analysis, mouse) and analysis.py\n    stimulus_timescales and extract_timescale. Rates in the 30 s before the first puff of each\n    series projected on the persistent weights of fig6d-mouse-persistent; autocorrelation\n    (scipy.signal.correlate) normalized to its maximum, a*exp(-x/b) + c fitted over the 2.5 s after\n    the peak, initial a=1, b=0.2, c=0; b is the timescale. Series used are Pre 11 to 20 and\n    Ketamine 23 to 32 (code, ten each as table S3). Two readings of how series are combined\n    (a) per series fits averaged within session (Methods and table S3); (b) one fit to the\n    series concatenated (code). Reproduced when, under both, the paired t-test gives p < 0.05\n    with Ketamine shorter and both means are within tolerance; partially reproduced when the test\n    holds but the means do not.\n- id: fig6j-mouse-coupling\n  statement: In mice, correlations among the most persistent neurons in the 30 s before each series\n    fell during ketamine to 0.49 of their preinfusion value.\n  source: Figure 6J; table S3, Fig. 6J\n  quote: in both mice and humans, we discovered that ketamine decreased coupling among these sites\n  depends_on:\n  - fig6d-mouse-persistent\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 7.463\"\n    p: 2.2e-05\n    n: 11 sessions from 9 mice, 10 series per condition\n  expected:\n    quantity: pairwise correlation among persistent neurons, Ketamine, normalized to Pre\n    value: 0.49\n    tolerance: 0.14\n  criterion: Persistent neurons and coupling. The Methods take edges between neurons in the top 10%\n    of absolute persistent weight, Pearson correlation averaged within session; the code\n    (plot_coding_dimension_early_late) takes neurons whose signed weight exceeds the 90th\n    percentile of absolute weights and the median absolute correlation of z-scored rates over the\n    concatenated 30 s windows of Pre series 1 to 10 and Ketamine series 23 to 32. Readings are (a)\n    the Methods, per-series 30 s windows, mean r over edges, averaged over series (table S3); (b)\n    the code. Ketamine values divided by Pre within session; paired t-test across sessions.\n    Reproduced when, under both, p < 0.05 with Ketamine lower; the expected value is met under\n    either.\n- id: figs34c-tone-no-eye-closure\n  statement: Mice did not close their eyes appreciably to a series of auditory tones, before or\n    during ketamine.\n  source: Figure S34C; table S3, fig. S34 C\n  quote: mice do not increase eye closure during tone presentation\n  criterion: Eye closure across the tone series, 7 sessions from 7 mice, Pre 10 series, Ketamine 5\n    (table S3). Reproduced when the 95% interval across sessions (1.96 s.e.m.) of the mean closure\n    from 0.3 to 0.8 s after each tone, averaged over the eight tones, lies below the corresponding\n    eyepuff value of the same sessions and below 0.1 of full closure. The 0.1 bound is a reading of\n    \"not substantial\"; the paper reports no test.\n- id: figs34d-tone-fast-unchanged\n  statement: Fast tone-related population activity (0 to 70 ms) was not changed by ketamine.\n  source: Figure S34D; table S3, fig. S34 D\n  quote: Whereas fast tone-related neural activity was unchanged on ketamine\n  statistics:\n  - about: Pre against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 1.088\"\n    p: 0.318\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 sessions from 7 mice\n  - about: Post against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 1.438\"\n    p: 0.318\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 sessions from 7 mice\n  expected:\n  - quantity: fast tone projection, Pre\n    value: 2.49\n    tolerance: 0.48\n  - quantity: fast tone projection, Ketamine\n    value: 1.83\n    tolerance: 0.78\n  - quantity: fast tone projection, Post\n    value: 1.56\n    tolerance: 0.54\n  criterion: A claim of absence, judged on the paper's test, as fig6f-mouse-fast-unchanged with tone\n    onsets, puff-modulated units (code selects units by their puff responses), tone series Pre\n    (first 10 before infusion), Ketamine and Post. Table S3 gives 5 Ketamine and 3 Post series and\n    the code takes post-infusion tone series 2 to 6 and 8 to 10 (1-based); the code is followed.\n    Reproduced when the Pre against Ketamine corrected p >= 0.05.\n- id: figs34e-tone-persistent\n  statement: Persistent tone-related activity (350 to 500 ms) fell during ketamine (1.531 to 0.392)\n    and recovered (1.385).\n  source: Figure S34E; table S3, fig. S34 E\n  quote: persistent tone-related activity decreased on ketamine and then recovered\n  statistics:\n  - about: Pre against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = 6.942\"\n    p: 0.0009\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 sessions from 7 mice\n  - about: Post against Ketamine\n    test: Paired t-test with fdr-bh correction\n    statistic: \"t = -3.753\"\n    p: 0.009\n    corrected: FDR (Benjamini-Hochberg)\n    n: 7 sessions from 7 mice\n  expected:\n  - quantity: persistent tone projection, Pre\n    value: 1.531\n    tolerance: 0.16\n  - quantity: persistent tone projection, Ketamine\n    value: 0.392\n    tolerance: 0.35\n  - quantity: persistent tone projection, Post\n    value: 1.385\n    tolerance: 0.66\n  criterion: As fig6d-mouse-persistent with tone onsets. Weights from 150 to 350 ms (Methods and\n    table S3) against the 1 s before the tone; the code uses bins 115 to 135 (150 to 350 ms after\n    onset), the same. Quantified over 350 to 500 ms (Methods and table S3); the code's window is\n    bins 135 to 150, the same. The code averages the projection over all eight tones (limit 8).\n    Reproduced when both corrected p < 0.05, with Ketamine lowest.\n- id: figs34f-tone-shorter-than-puff\n  statement: Persistent responses to the neutral tone were shorter than those to the eyepuff.\n  source: Figure S34F; table S3, fig. S34 F\n  quote: The affectively salient eyepuff elicits substantially longer persistent dynamics than the\n    neutral tone\n  depends_on:\n  - fig6d-mouse-persistent\n  - figs34e-tone-persistent\n  criterion: As analysis.py compare_tone_puff_late_proj. Per session, the Pre projection on each\n    stimulus's persistent dimension averaged over the eight stimuli of a series, turned into d'\n    against the 1 s before onset. Reproduced when the time at which the across-session mean d'\n    falls back below half its peak is later for the puff than for the tone, and the puff mean d'\n    over 1 to 2 s lies above the tone's with non-overlapping 95% intervals. The half-peak measure is\n    a reading of \"longer\"; the paper reports no test.\n- id: figs34g-tone-timescale\n  statement: The baseline intrinsic timescale of the persistent tone population was shorter during\n    ketamine (0.089 s) than before (0.268 s).\n  source: Figure S34G; table S3, fig. S34 G\n  quote: we still could detect a ketamine-mediated acceleration in the intrinsic timescale of\n    populations that (prior to ketamine) exhibited modestly persistent responses to the tone\n  depends_on:\n  - figs34e-tone-persistent\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 5.479\"\n    p: 0.0015\n    n: 7 sessions from 7 mice\n  expected:\n  - quantity: tone intrinsic timescale, Pre\n    value: 0.268\n    tolerance: 0.073\n    unit: s\n  - quantity: tone intrinsic timescale, Ketamine\n    value: 0.089\n    tolerance: 0.024\n    unit: s\n  criterion: As fig6h-mouse-timescale with the tone dimension and the 30 s before each tone series.\n    The code takes Pre tone series 5 to 10 and Ketamine 2 to 6 (1-based); table S3 gives 10 and 5;\n    both are shown, as are the two readings of how series are combined.\n- id: figs34h-tone-coupling\n  statement: Correlations among the persistent tone neurons before the tone series fell during\n    ketamine to 0.460 of their preinfusion value.\n  source: Figure S34H; table S3, fig. S34 H\n  quote: under ketamine these populations exhibited reduced functional coupling even before tone\n    presentation\n  depends_on:\n  - figs34e-tone-persistent\n  statistics:\n  - test: Paired t-test\n    statistic: \"t = 6.217\"\n    p: 0.0008\n    n: 7 sessions from 7 mice\n  expected:\n    quantity: pairwise correlation among persistent tone neurons, Ketamine, normalized to Pre\n    value: 0.46\n    tolerance: 0.16\n  criterion: As fig6j-mouse-coupling, with the tone dimension and the 30 s before each tone series,\n    under both readings.\n- id: figs30-correlation-structure\n  statement: Ketamine changed the correlation structure of single units at rest, increasing\n    correlations within regions such as retrosplenial/posteromedial and orbitofrontal cortex while\n    reducing correlations between regions.\n  source: Figure S30A; Results, Brain-wide activity screen during emergence of affect in mice\n  quote: ketamine altered single-unit correlation structure at rest by increasing within-region\n    correlations such as within PMC and ORB (while also reducing correlations between regions\n  criterion: Method from the Methods (Regional correlation analysis). Pearson correlations between\n    all units of a session over the whole preinfusion period and over the 10 minutes from\n    ketamine onset (taken as 30 s after the last puff of series 20, as the code's ket_start). The\n    paper shows one example session and no test. Per session, the mean within-region and the mean\n    between-region change (Ketamine minus Pre), regions at the finest Allen level. Reproduced when,\n    across the 13 sessions, the within-region change is above zero and the between-region change\n    below zero by paired t-tests at p < 0.05 (the paper's test for session-level comparisons in\n    table S3, Fig. 6J), and RSP and ORB within-region changes are positive in most sessions that\n    record them.\n- id: figs29-rsp-oscillations\n  statement: Ketamine brought low-frequency oscillations into the population activity, especially\n    strong in retrosplenial cortex.\n  source: Figure S29C and S29D; Results, Brain-wide activity screen during emergence of affect in\n    mice\n  quote: noted the prominent appearance of low frequency oscillations as we previously reported (\n    28 ), with especially strong low frequency oscillations in PMC/retrosplenial cortex (RSP)\n  criterion: Method from the Methods (Example-session unsupervised clustering and spectral\n    analysis) and analysis.py plot_session_rastermap. Welch power spectra (nperseg 2048, 100 Hz)\n    of each unit's z-scored rate, z-scored across frequency, over 0 to 7.5 Hz (the plotted range).\n    The paper gives the windows only as \"the given 1 minute windows\" of an example; the readings\n    are the minute before infusion against (a) the minute starting 5 min after it and (b) the\n    minute starting 10 min after it. The peak of the z-scored spectrum below 7.5 Hz, averaged per\n    region. Reproduced when, under both, it rises after ketamine in RSP units in most sessions\n    that record RSP and RSP has the largest rise of all regions with at least 30 units in the\n    pooled data. The paper reports no test.\n"
}
```

```
File created successfully at: claims/001326/10.1126-science.adt3971.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001326/10.1126-science.adt3971.yaml paper/10.1126-science.adt3971.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "[^ ] #\| # " claims/001326/*.yaml | grep -v "^[0-9]*:#" | head; grep -n "—\|rather" claims/001326/*.yaml | head
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001326/10.1126-science.adt3971.yaml",
 "old_string": "quality criteria (Methods); \"dozens of regions\" holds when the median session has units in at\n    least 24 Allen CCFv3 regions at the finest level. The puff-modulated",
 "new_string": "quality criteria (Methods); \"dozens of regions\" holds when the median session has units in at\n    least 24 Allen CCFv3 regions at the finest level, a reading of \"dozens\" as two dozen since the\n    paper gives no count. The puff-modulated"
}
```

```
The file claims/001326/10.1126-science.adt3971.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001326/10.1126-science.adt3971.yaml paper/10.1126-science.adt3971.txt; python -c "
import yaml;d=yaml.safe_load(open('claims/001326/10.1126-science.adt3971.yaml'))
c=d['claims'];print(len(c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c), sum(x.get('data')=='elsewhere' for x in c))"; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001326/10.1126-science.adt3971.yaml` with 50 claims. The quote checker reports 50 quotes and 39 statistical values with 0 problems. Nothing is committed.

**Text read**
- The accepted author manuscript from Europe PMC (PMC12286656, NIHMS2090574), not the version of record: main text and Methods.
- The Supplementary Materials PDF: Supplemental Note 1, figs. S1 to S38, and tables S1 to S3. Table S3 holds the statistics.
- The MDAR checklist.
- Nothing a claim needed was missing.

**Code read**
- The mouse analysis code, `analysis.py` (Zenodo 10.5281/zenodo.14876694). It has the analysis functions but not the script that calls them.
- brainwide-npix at commit 97cdf58 (tag v0.1).
- The human and mouse-behavior code (Zenodo 14920570), read only for the eye-closure and human coding-dimension windows.

**Claims**
- **Count:** 50 claims, all with quotes. 24 have statistics, 27 have expected values and 44 have criteria.
- **Human and mouse behavior-only (22 claims):** these data are in DANDI:001347, so the claims are marked `data: elsewhere`.
- **Mouse electrophysiology (28 claims):** these are tested on 001326. They cover:
  - eye closure in the recorded mice;
  - the twelve response clusters and which regions they over-represent;
  - regional rise and decay times;
  - the emotion-like dimension (Fig. 5D/E) and the first-order model with its alternatives;
  - fast and persistent coding dimensions, intrinsic timescale and coupling (Fig. 6D/F/H/J);
  - the tone controls (fig. S34);
  - correlation structure and retrosplenial oscillations under ketamine (figs. S29, S30).
- **Tolerances:** 1.96 × the s.e.m. given in table S3 (the paper plots means ± 1.96 s.e.m.), otherwise 10%.

**Details left open, and the readings named**
- **Which mouse was excluded** (13 sessions from 10 mice down to 11 from 9): the paper doesn't name it. Every mouse with two sessions is a reading, and the outcome must hold under all of them.
- **Trial epochs:** the Methods say ketamine is trials 22–32 and post is 34–40. The code and table S3 give trials 23–32 (10 trials) and 35–40 (6 trials). The code is the main reading; the literal Methods numbers are a variant.
- **Emotion-like dimension window:** the Methods put it 5–6 s after the last puff. The code's indexing implies 3–4 s. The weights are divided by each unit's variance in the Methods but by a pooled variance in the code, and scaled to a unit vector versus a sum of absolute values. That scaling affects the expected values in Fig. 5E.
- **Fast coding dimension reference window:** 1 s before the puff in the Methods, 70 ms before in the code.
- **Persistent projection (Fig. 6D):** the code uses the first puff of each series only; all eight puffs is a variant.
- **Intrinsic timescale:** one fit per trial then averaged (Methods, table S3) versus one fit to the trials joined together (code). The pre trials used differ: 11–20 in the code. For the human version, the baseline period is 8 minutes in the Methods and 10 in table S3.
- **Coupling (Fig. 6J):** mean signed r among neurons with the top 10% of absolute weight (Methods) versus median absolute r among neurons with large positive weight, over joined windows (code).
- **Regional d' threshold:** 1.3 in the Methods and code, 2 in table S3.
- **Region labelling threshold for fig. S31B:** 0.05 in the Methods and code, 0.01 in table S3.
- **Cluster numbering:** table S3 numbers clusters by size, while the figure numbers them in a reordered sequence. Which one the text's "clusters 0, 1 and 2" uses is open.
- **Other small gaps:**
  - The code's minimum-activity filter on units has units the code doesn't fix.
  - For the CADSS correlation, the change is ketamine minus the mean of pre and post in the legend but ketamine minus pre in table S3.
  - The tone-series trial counts differ between table S3 and the code.
- **No test in the paper:** several claims rest on figures alone (Fig. 4B, 4G, 4H/I, 5B, 5D, fig. S29, S30, S34C/F, Fig. 6B). For these, the criteria use the paper's own 95% intervals or its stated measures, and they say so. Thresholds that had to be read from words like "dozens", "not substantial" or "tens of seconds" are named as readings in the criteria.
- **Recorded-mouse eye closure:** the paper's data statement places mouse behavior in 001347, but the electrophysiology code reads it. Whether 001326 holds it is for the author to check.

## End of run

51 turns, 10 minutes, result: success.
