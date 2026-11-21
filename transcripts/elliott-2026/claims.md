# elliott-2026 · claims · run 44850746409

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
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

**Agent calls Bash**

```bash
head -40 claims/sabatini-2024.yaml; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; head -c 3000 paper/*.txt; grep -n -i "github\|code avail\|supplement\|extended data\|zenodo\|osf\|figshare" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper text is in place (author manuscript, PMC12931417) along with an Extended Data PDF. Reading the full text now.

**Agent calls Bash**

```bash
fold -s -w 180 paper/10.1152-jn.00217.2025.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	DOI: 10.1152/jn.00217.2025
2	Version: version of record
3	Source: find_reuse cache
4	Stored: 2026-11-10
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc J Neurophysiol J Neurophysiol 319 nihpa Journal of neurophysiology 0022-3077 1522-1598 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC12931417 
8	PMC12931417.1 12931417 12931417 NIHMS2139309 41385612 10.1152/jn.00217.2025 NIHMS2139309 NIHPA2139309 1 Article Microscale maps of bursting dynamics across human hippocampal 
9	slices from epilepsy patients Elliott Matthew A.T. 1 2 * Andrews John P. 3 * van der Molen Tjitse 1 2 4 5 Geng Jinghui 2 6 Spaeth Alex 2 6 Toledo Anna 2 Voitiuk Kateryna 1 2 Core 
10	Cordero 7 Gillespie Thomas 1 2 Sinervo Ari 2 Parks David F. 1 2 Robbins Ash 2 6 Solís Daniel 1 2 Chang Edward F. 3 Nowakowski Tomasz Jan 3 8 9 10 Teodorescu Mircea 2 6 Haussler 
11	David 1 2 Sharf Tal 1 2 ** 1. Department of Biomolecular Engineering, University of California Santa Cruz, Santa Cruz, CA, USA 2. UC Santa Cruz Genomics Institute, University of 
12	California Santa Cruz, Santa Cruz, CA, USA 3. Department of Neurological Surgery, University of California San Francisco, San Francisco, CA, USA 4. Neuroscience Research 
13	Institute, University of California Santa Barbara, Santa Barbara, CA, USA 5. Department of Molecular, Cellular and Developmental Biology, University of California Santa Barbara, 
14	Santa Barbara, CA, USA 6. Department of Electrical and Computer Engineering, University of California Santa Cruz, Santa Cruz, CA, USA 7. Scientific Software Engineering Center, 
15	eScience Institute, University of Washington, Seattle, WA USA 8. Weill Institute of Neurosciences, University of California San Francisco, San Francisco, CA, USA 9. Department of 
16	Psychiatry and Behavioral Sciences, University of California San Francisco, San Francisco, CA, USA 10. The Eli and Edythe Broad Center of Regenerative Medicine and Stem 
[... 290 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 307,
 "limit": 120
}
```

```
307	Virtual Institute for Scientific Software (VISS). This project was supported by the National Institute of Neurological Disorders and Stroke, National Institutes of Health, through 
308	UCSF grant number 5R25NS070680–13 (J.P.A.). This study was also supported by NIH awards: Brain Initiative award UF1MH130700 (T.J.N.), R01NS123263 (to T.J.N.), T32HG012344 (K.V.). 
309	Its contents are solely the responsibility of the authors and do not necessarily represent the views of the NIH. The funders had no role in study design, data collection, 
310	analysis, decision to publish, or preparation of the manuscript. Competing interests: All authors declare no competing interests. Code Availability All coding was done in Python, 
311	3.10. The code used in the final processing and analysis of data is publicly available on GitHub. The repository has been integrated with GitHub Codespaces. Researchers can easily 
312	launch an online environment to reimplement our analysis. Instructions are in the GitHub repository: https://github.com/braingeneers/human_hippocampus Data Availability All data 
313	used in the analysis and creation of figures is available in the GitHub repository: https://github.com/braingeneers/human_hippocampus The repository includes neural spiking data, 
314	histology images, portions of raw electrophysiological data, and plots created for figures. The complete dataset of raw electrophysiological recordings from experiments is 
315	available on the DANDI public server: https://dandiarchive.org/dandiset/001132 References 1. Tatum WO Mesial temporal lobe epilepsy . J. Clin. Neurophysiol. Off. Publ. Am. 
316	Electroencephalogr. Soc . 29 , 356 – 365 ( 2012 ). 10.1097/WNP.0b013e31826b3ab7 23027091 2. The Hippocampus Book . ( Oxford University Press , Oxford; New York , 2006 ). 3. Thom M 
317	Review: Hippocampal sclerosis in epilepsy: a neuropathology review . Neuropathol. Appl. Neurobiol . 40 , 520 – 543 ( 2014 ). 24762203 10.1111/nan.12150 PMC4265206 4. Patrylo PR
[... 109 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 427,
 "limit": 650
}
```

```
427	
428	Microscale maps of bursting dynamics across human hippocampal slices from patients with epilepsy
429	
430	We apply high-density CMOS-based microelectrode arrays to excised patient brain slices, mapping the communication patterns of hundreds of neurons at unprecedented resolution. We 
431	developed novel computational techniques to spatially map neuronal dynamics. In patient slices, our findings suggest that recurrent feedback localized within the dentate gyrus of 
432	the hippocampus is linked to a previously unreported phenomenon of theta propagations. This bridges microscale circuit dynamics with alterations in theta oscillations.
433	
434	10.1097/WNP.0b013e31826b3ab7
435	
436	10.1093/acprof:oso/9780195100273.001.0001
437	
438	10.1111/nan.12150
439	
440	10.1016/s0920-1211(99)00022-4
441	
442	10.1039/b907394a
443	
444	10.1038/nmeth.4393
445	
446	10.1038/s41467-020-18620-4
[... 628 more lines not kept]
```

**Agent**

Extended Data Tables 1 to 4 are garbled in the text (images), so I'll read those pages in the PDF. Then the linked code.

**Agent calls Bash**

```bash
pdfinfo paper/*.pdf | grep Pages; for i in $(seq 1 25); do echo "== $i"; pdftotext -f $i -l $i paper/*.pdf - 2>/dev/null | head -3; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00217.2025.supp-Extended_Data.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import fitz; print(fitz.__doc__)" 2>&1; python -c "import pypdf; print(pypdf.__version__)" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf; print(pypdf.__version__)
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
pip install --target $TMPDIR/pylib pymupdf 2>&1 | tail -2
```

```
Successfully installed flatbuffers-25.12.19 networkx-3.7 numpy-2.5.5 onnxruntime-1.32.0 packaging-26.3 protobuf-7.36.2 psutil-7.2.2 pymupdf-2.1 pymupdf-layout-2.1 pymupdf4llm-2.1 pyyaml-6.0.4 tabulate-0.10.0
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1152-jn.00217.2025.supp-Extended_Data.pdf')
print(len(d))
for i,p in enumerate(d):
    t=p.get_text()
    print(i+1, repr(t[:80]))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf
d=pymupdf.open('paper/10.1152-jn.00217.2025.supp-Extended_Data.pdf')
for i in [2,14,16,18,20]:
    d[i-1].get_pixmap(dpi=130).save(f'pg{i}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg14.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg18.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg20.png"
}
```

Result: no output.

**Agent**

Tables read: 8 recordings from 6 slices, Table 2 phase-locking counts, Table 3 geometry-test p-values. Checking Extended Data Fig. 10 for per-recording connection counts.

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -W ignore -c "
import pymupdf
d=pymupdf.open('paper/10.1152-jn.00217.2025.supp-Extended_Data.pdf')
d[15].get_pixmap(dpi=200).save('pg16b.png')
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg16b.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

## Prompt

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]

**Agent**

Extended Data Fig. 10 gives total connections per recording. Now the linked code repository.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --filter=blob:none --no-checkout https://github.com/braingeneers/human_hippocampus hh 2>&1 | tail -2; cd hh && git log -1 --format='%H %cd' && git ls-tree -r --name-only HEAD | grep -v -E '\.(png|jpg|tif|svg|npz|npy|zip|h5|nwb|mat|pkl|gif|mp4|pdf)$' | head -150
```

```
0f83f704ee4c9b4d8d7f75eb53d94f525c85abb2 Tue Oct 7 13:50:33 2025 +0000
.DS_Store
.devcontainer/.DS_Store
.devcontainer/devcontainer.json
.devcontainer/old_curate_data.py
.devcontainer/post_create.sh
.gitattributes
.gitignore
CITATION.cff
LICENSE.txt
README.md
data/.DS_Store
data/ephys/2022-11-02-e-Hc11.1-chip16753/metadata.json
data/histology/.DS_Store
data/histology/hc110723_bw.jpeg
data/histology/hc328_bw.jpeg
data/histology/hc52_bw.jpeg
data/histology/old_chip21769_bw.jpeg
data/opto/.DS_Store
data/opto/hc328_20230402T14/20230402T140926-2023_04_02_hc328_0_opto_stim_log.csv
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && git ls-tree -r --name-only HEAD | grep -v '^dev/' | grep -v -E '\.(png|jpg|jpeg|tif|svg|gif|mp4|pdf|DS_Store)$' ; git show HEAD:README.md | head -120
```

```
<persisted-output>
Output too large (34.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/bd32e3c5-1fb8-462c-8c73-ca22aaba2871/tool-results/bzzy7ph50.txt

Preview (first 2KB):
.devcontainer/devcontainer.json
.devcontainer/old_curate_data.py
.devcontainer/post_create.sh
.gitattributes
.gitignore
CITATION.cff
LICENSE.txt
README.md
data/ephys/2022-11-02-e-Hc11.1-chip16753/derived/kilosort2/hc11.1_plated-11.1_chip-16753_rec_11.2.22AM-immediate_curated.zip
data/ephys/2022-11-02-e-Hc11.1-chip16753/derived/kilosort2/hc11.1_plated-11.1_chip-16753_rec_11.2.22AM-immediate_curated_neg.zip
data/ephys/2022-11-02-e-Hc11.1-chip16753/metadata.json
data/ephys/2023-04-02-e-hc328_unperturbed/StitchedDataUpdated.pkl
data/ephys/2023-04-02-e-hc328_unperturbed/arrows/pairs/deltas_20ms_cuttoff_2_15ms.pkl
data/ephys/2023-04-02-e-hc328_unperturbed/arrows/rasters/sttc_0.04.pkl
data/ephys/2023-04-02-e-hc328_unperturbed/arrows/rasters/sttc_0.04_lag_1ms.pkl
data/ephys/2023-04-02-e-hc328_unperturbed/derived/kilosort2/hc3.28_hckcr1_chip16835_plated34.2_rec4.2_curated.zip
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && git ls-tree -r --name-only HEAD | grep -v '^dev/' | grep -E '\.(py|ipynb|md|json)$'; echo ----; git show HEAD:README.md | head -150
```

```
.devcontainer/devcontainer.json
.devcontainer/old_curate_data.py
README.md
data/ephys/2022-11-02-e-Hc11.1-chip16753/metadata.json
docs/source/conf.py
experiments/ca1/hc328/no_drug/autocuration_check_2023-04-02-e-hc328_unperturbed.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_arrow_animation.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_buzsaki.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_buzsaki2 copy.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_buzsaki2.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_latencies.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_latencies2.ipynb
experiments/ca1/hc328/no_drug/hc328_no_drug_raw_animations.ipynb
experiments/ca1/hc52/bicuculline/OLD_2023-05-10-e-hc52_18790.ipynb
experiments/ca1/hc52/no_drug/autocuration_check_2023-05-10-e-hc52_18790_unperturbed.ipynb
experiments/ca1/hc52/no_drug/hc52_acid_buzsaki.ipynb
experiments/ca1/hc52/no_drug/hc52_no_drug.ipynb
experiments/ca1/hc52/no_drug/hc52_no_drug_buzsaki2.ipynb
experiments/ca1/hc52/no_drug/hc52_no_drug_latencies.ipynb
[... 297 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && git checkout HEAD -- src figures/figure_3/haussler/hc112823_acid.ipynb figures/figure_3/TJ_phase_locking_basics.ipynb figures/figure_3/Phase_lock_heatmap.ipynb figures/figure_3/sttc.ipynb figures/figure_3/circuit_diagram.ipynb figures/supplement/phase_locking/sig_counts.ipynb "figures/figure_3/latencies/t_test_try30_try3/hc112823_acid.ipynb" figures/supplement/circuit_diagram/hc112823_acid.ipynb 2>&1 | tail -3; wc -l src/human_hip/spike_data/*.py src/human_hip/raw_data/*.py
```

```
48 src/human_hip/spike_data/__init__.py
   125 src/human_hip/spike_data/analysis.py
   135 src/human_hip/spike_data/latencies.py
   161 src/human_hip/spike_data/plot_eigendecomposition.py
    26 src/human_hip/spike_data/plot_footprint.py
   141 src/human_hip/spike_data/plot_functional_connectivity_map.py
  1161 src/human_hip/spike_data/plot_latencies.py
   119 src/human_hip/spike_data/plot_matrices_connectivity.py
   156 src/human_hip/spike_data/plot_raster.py
   134 src/human_hip/spike_data/plot_summary.py
    43 src/human_hip/spike_data/plot_waveform_layout.py
   133 src/human_hip/spike_data/randomize.py
   195 src/human_hip/spike_data/read_data.py
    72 src/human_hip/spike_data/text_summary.py
    14 src/human_hip/raw_data/__init__.py
    53 src/human_hip/raw_data/data_nrp.py
    72 src/human_hip/raw_data/filter.py
   103 src/human_hip/raw_data/spectrogram.py
  2891 total
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh/src/human_hip/spike_data && cat latencies.py analysis.py
```

```
#!/usr/bin/env python3

import numpy as np
from scipy.signal import correlate, correlation_lags



def latencies(neuron1, neuron2, sd, ms_cutoff_low=0, ms_cutoff_high=20 ):
    """
    Function:
        returns all the latencies that occur between two neurons, n1 and n2. 
        A latency is defined as the time difference between a spike from n1 and the nearest spike from n2 (positive or negative)
    Inputs:
        neuron1 (integer): index of the neuron, n1 
        neuron2 (integer): index of the neuron, n2, *note* if n1 occurs before n2, the latency will be positive
        sd (SpikeData object): contains the original spike data from the recording
        ms_cutoff (integer): the maximum latency to be considered, in milliseconds
    Outputs:
        cur_latencies (np.array): the time difference between n1 and n2, for ever latency occurence less than ms_cutoff
    """
[... 236 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f'--- [{i}] {c["cell_type"]}'); print(src[:3000])
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t: print('>>', ''.join(t)[:600])
EOF
cd $TMPDIR/hh && python $TMPDIR/nb.py "figures/figure_3/latencies/t_test_try30_try3/hc112823_acid.ipynb"
```

```
--- [0] markdown
<font size=7> Latencies Analysis
--- [1] markdown
# get pairs
--- [2] code
import pickle
from human_hip.spike_data import curate_latencies, plot_raster_latency_pairs, plot_vector_layout, plot_latency_dist_hist, plot_latency_angle_hist, \
                                 plot_cross_sttc_pairs, plot_vector_layout2, plot_vector_layout5, plot_vector_layout1, read_autocurated_data, arrow_check2
from human_hip.animate import animate_latencies

from scipy import stats
from ipywidgets import interact_manual, interact
import matplotlib.pyplot as plt
import numpy as np
from human_hip.spike_data import latencies

from human_hip.spike_data import random_harris

--- [3] code
from human_hip.spike_data import curate_latencies, plot_raster_latency_pairs, plot_vector_layout, cross_sttc, plot_pair_analysis, plot_cross_sttc_pairs
[... 365 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/haussler/hc112823_acid.ipynb | grep -v "DeprecationWarning\|neuron_data\[0\]" | cut -c1-400 | head -300
```

```
--- [0] markdown
<font size=7> Latencies Analysis
--- [1] markdown
# get pairs
--- [2] code
import pickle
from human_hip.spike_data import curate_latencies, plot_raster_latency_pairs, plot_vector_layout, plot_latency_dist_hist, plot_latency_angle_hist, \
                                 plot_cross_sttc_pairs, plot_vector_layout2, plot_vector_layout5, plot_vector_layout1, read_autocurated_data, arrow_check2
from human_hip.animate import animate_latencies

from scipy import stats
from ipywidgets import interact_manual, interact
import matplotlib.pyplot as plt
import numpy as np
from human_hip.spike_data import latencies

--- [3] code
from human_hip.spike_data import curate_latencies, plot_raster_latency_pairs, plot_vector_layout, cross_sttc, plot_pair_analysis, plot_cross_sttc_pairs
import pickle
import matplotlib.pyplot as plt
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/haussler/hc112823_acid.ipynb | grep -v "DeprecationWarning\|neuron_data\[0\]" | cut -c1-400 | awk '/^--- \[2[3-9]\]|^--- \[[3-9][0-9]\]/{p=1} p' | grep -v '^ [0-9]*,$' | head -250
```

```
--- [23] code

# Plot the data points
plt.scatter(x, y, color='blue', label='Neuron')

# Plot the polynomial line
plt.plot(x_plot, y_plot, color='red', label=f'Polynomial Regression')

plt.plot([x[0], x_plot[11]], [y[0], y_plot[11]], color='green', label=f'Projection onto GCL')
for i, idx in enumerate(closest_indices):
    plt.plot([x[i], x_plot[idx]], [y[i], y_plot[idx]], color='green')

# Add labels and legend
plt.xlabel('um')
plt.ylabel('um')
plt.legend(loc='lower right')
>> <matplotlib.legend.Legend at 0x749156e53550>
>> <Figure size 640x480 with 1 Axes>
--- [24] markdown
## <font color="violet"> Get index and angle for each arrow
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/supplement/phase_locking/sig_counts.ipynb | cut -c1-500 | head -200
```

```
--- [0] markdown
<font size=7> Phase Locking Counts
--- [1] code
import pickle
import numpy as np
import matplotlib.pyplot as plt
--- [2] markdown
# Chip 21769 - seziure
--- [3] code
with open( "2023-12-11-e-Hc120523_aav9hckcr1_chip21769_theta_spike_locking_s.pkl", 'rb') as file:
    data = pickle.load(file)
print( "Total-", len(data["mean_angle"]) )
print( "Significant-", sum( data["rayleigh_p"]<0.05 ) )
print( "Percent-", sum( data["rayleigh_p"]<0.05 )/len(data["mean_angle"]) )

>> Total- 180
Significant- 101
Percent- 0.5611111111111111

--- [4] markdown
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/TJ_phase_locking_basics.ipynb | cut -c1-2500 | grep -v '^ *[-0-9.e, \[\]]*$' | head -400
```

```
--- [0] code
import pickle
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec
from human_hip.raw_data import get_brain_waves, cwt_spectrogram, spectrogram_plot, butter_filter
from human_hip.spike_data import read_autocurated_data, plot_raster
import numpy as np
from scipy.ndimage import gaussian_filter1d

from scipy.signal import hilbert, correlate, find_peaks
from astropy.stats import rayleightest, circmean, circstd

# Packages for plotting spectrogram
from scipy import ndimage
from matplotlib.colors import LogNorm #Normalize
from matplotlib.cm import get_cmap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import pickle 
from human_hip.histology import plot_histology, plot_histology_electrode_map
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python - <<'EOF'
import json
nb=json.load(open('figures/figure_3/TJ_phase_locking_basics.ipynb'))
s=''.join(nb['cells'][3]['source']); i=s.find('# initiate empty result libraries'); print(s[i:])
s=''.join(nb['cells'][1]['source']); print(s[:200]); 
EOF
```

```
# initiate empty result libraries
all_spk_angles = {}
all_spk_times = {}

# for each superburst
for i, sb in enumerate(S_SB_TIMES):
    print(sb)

    # load LFP data
    # with open("/workspaces/" + LFP_PATH + "/acid1_start{}s_stop{}s_fs1ms.pkl".format(sb[0], sb[1]), 'rb') as filename:
    with open("/workspaces/" + LFP_PATH + "/seizure/acid1_start{}s_stop{}s_fs1ms.pkl".format(sb[0], sb[1]), 'rb') as filename:
        data_raw = pickle.load(filename)

    # filter LFP data into individual theta frequency band
    theta_filt = butter_filter(data_raw["data"], 4, 8, fs=data_raw["frame_rate"])

    # if this is the first iteration of the loop
    if i == 0:

        # obtain electrode coordinates
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python - <<'EOF'
import json
nb=json.load(open('figures/figure_3/TJ_phase_locking_basics.ipynb'))
s=''.join(nb['cells'][1]['source']); i=s.find('# Other seizure'); print(s[i:i+700])
EOF
python $TMPDIR/nb.py figures/figure_3/Phase_lock_heatmap.ipynb | cut -c1-1800 | grep -v '^ *[-0-9.e, \[\]]*$' | grep -i -n -B3 -A25 "kuiper\|mode\|cluster" | head -200
```

```
# Other seizure recording
S_SB_TIMES = [
            [0, 11],
            [25, 39],
            [139, 148],
            [168, 174],
            [258, 263],
            [320, 328],
            [481, 487],
            ]

NS_SB_TIMES = [
            [50, 60],
            [100, 113],
            [200, 212],
            [270, 275],
            [392, 400],
            [400, 406],
            [450, 455],
            ]
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/Phase_lock_heatmap.ipynb | cut -c1-3000 | grep -v '^ *[-0-9.e, \[\]]*$' | head -300
```

```
--- [0] markdown
<font size=7> Phase Lock Histograms
--- [1] markdown
# Setup
--- [2] code
from human_hip import spike_data
import numpy as np
from human_hip.spike_data import *
import pickle

import matplotlib.pyplot as plt
import matplotlib.cm as cm
--- [3] code
sd = read_autocurated_data( "/workspaces/human_hippocampus/data/ephys/2023-12-03-e-Hc112823_avv9hckcr1/derived/kilosort2/Hc112823_avv9hckcr1_21841_120323_3_acqm.zip" )

with open( "2023-12-03-e-Hc112823_avv9hckcr1_acid1_theta_spike_locking_s.pkl", 'rb') as file:
    data = pickle.load(file)
angles = data["mean_angle"]
pvals = data["rayleigh_p"]

[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/Phase_lock_heatmap.ipynb | grep -n -i -A12 "kuiper" | cut -c1-300 | head -60; git grep -il kuiper HEAD -- '*.ipynb' '*.py' | head
```

```
Shell cwd was reset to
```

**Agent**

No Kuiper test code exists in the repo; that will be named as open. Checking the STTC clustering notebook.

**Agent calls Bash**

```bash
cd $TMPDIR/hh && python $TMPDIR/nb.py figures/figure_3/sttc.ipynb | cut -c1-1500 | grep -v '^ *[-0-9.e, \[\]]*$' | head -150
```

```
--- [0] markdown
<font size=7>STTC Plots
--- [1] code
from human_hip import spike_data
--- [2] code
import numpy as np                                                    # Packages for data analysis
import matplotlib.pyplot as plt
from human_hip.spike_data import correlation_matrix, eigenvalues_eigenvectors, plot_eigenvectors #firing_rates,
import scipy.cluster.hierarchy as sch
--- [3] markdown
# First Eigenvector for HC112823
--- [4] code
sd = spike_data.read_autocurated_data( "/workspaces/human_hippocampus/data/ephys/2023-12-03-e-Hc112823_avv9hckcr1/derived/kilosort2/Hc112823_avv9hckcr1_21841_120323_3_acqm.zip" )
#sd = spike_data.read_phy_files("/workspaces/human_hippocampus/data/ephys/2023-12-11-e-Hc120523_aav9hckcr1_chip21769/elliott/elliott_chip21769_2.zip")

--- [5] code
# def plot_sttc_matrix( sd, blur=20, sttc_cutoff_high=1.1, plot_color="magma" ):
#     """
#     Outputs: plots the STTC and Correlation matrices for neurons in a recording
#     Input: 
[... 131 more lines not kept]
```

**Agent**

I have what I need from the code. Checking the claims checker's expectations before writing.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "papers/datasets" -r docs/paper-first.md | head -3; cat papers/datasets/elliott-2026.yaml 2>/dev/null
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
grep -n "with_inputs\|with_labels\|elsewhere" docs/protocol.md | head -20; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:4000])"
```

```
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
161:     recordings of its own, or on other data, are `data: elsewhere` when they
233:4. Decide what comes from outside the dataset. Data from elsewhere may be
242:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
243:     `with_inputs` and `elsewhere` claims are counted apart, each group on
245:   - `with_labels` is for outside sources that only name or map codes the
275:   - `elsewhere` is for a claim whose data the dataset does not hold at
284:   - The notes of a `with_inputs` claim say which side a difference comes
295:     `data: elsewhere` instead (step 4).
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
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 228,300p docs/protocol.md; python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[4000:9000])"
```

```
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
[... 270 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001132/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d.get(k) for k in ['identifier','draft_version','most_recent_published_version']},indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/001132/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m.get('name'));print(m.get('description'));print(m.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/hh && git checkout HEAD -- figures/figure_2/burst_peak_comparison.ipynb figures/figures_1/spike_rasters.ipynb figures/supplement/seizure_2/seizure2_burst_peaks.ipynb figures/figure_2/theta_waves.ipynb 2>&1|tail -1; for f in figures/figure_2/burst_peak_comparison.ipynb figures/figures_1/spike_rasters.ipynb figures/supplement/seizure_2/seizure2_burst_peaks.ipynb; do echo "=== $f"; python $TMPDIR/nb.py $f | grep -n -i -B2 -A6 "find_peaks\|burst\|sigma\|67\b" | cut -c1-250 | head -60; done
```

```
=== figures/figure_2/burst_peak_comparison.ipynb
1---- [0] markdown
2:<font size=7> Burst Attempt
3---- [1] code
4-from human_hip import spike_data
5-import numpy as np
6-from matplotlib import cm
7-from matplotlib import pyplot as plt
8-from matplotlib.colors import LinearSegmentedColormap
--
35---- [4] code
36-spike_data.plot_raster( sd, size=(15,7), xlim=(14, 15.7), smoothness=28, ylim=(0.35,2.5),
37:                         title="Burst Events During Initiation Phase" )
38-axs = plt.gca()
39-axs.vlines( [14.4, 14.57, 14.75, 14.91], 0.35, 2.5, color='black' )
40->> <matplotlib.collections.LineCollection at 0x7528e09cda50>
41->> <Figure size 1500x700 with 2 Axes>
42---- [5] code
43-sd1 = sd.subtime( 14.4*1000 ,  14.57*1000 )
--
[... 49 more lines not kept]
```

**Agent**

No burst detector in the code: burst and sub-burst times are set by hand (S1 initiation sub-bursts at 14.4, 14.57, 14.75 and 14.91 s). Checking the filter code, then writing the file.

**Agent calls Bash**

```bash
cd $TMPDIR/hh && cat src/human_hip/raw_data/filter.py | head -72; grep -n "def spike_time_tilings\|def spike_time_tiling" -A3 -r src | head
```

```
#!/usr/bin/env python3  

from scipy import signal 


# Downsample abd remove artifact
def downsample(wav_lfp, dec=20, fs=20000.0):
    wav_data = signal.decimate(wav_lfp, dec)
    return fs/dec, wav_data


# Bandpass filter
# Note: another example of a filter (not used)- https://github.com/hengenlab/neuraltoolkit)
def butter_filter(data, lowcut=None, highcut=None, fs=20000.0, order=5):
    """
    A digital butterworth filter. Type is based on input value.
    Inputs:
        data: array_like data to be filtered
        lowcut: low cutoff frequency. If None or 0, highcut must be a number.
                Filter is lowpass.
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hh && git show HEAD:dev/other/ari/delete_soon/braingeneers/analysis/analysis.py | grep -n "def spike_time_til" -A12 | head -40
```

```
783:    def spike_time_tilings(self, delt=20):
784-        '''
785-        Compute the full spike time tiling coefficient matrix.
786-        '''
787-        ret = np.diag(np.ones(self.N))
788-        for i in range(self.N):
789-            for j in range(i + 1, self.N):
790-                ret[i, j] = ret[j, i] = self.spike_time_tiling(i, j, delt)
791-        return ret
792-
793:    def spike_time_tiling(self, i, j, delt=20):
794-        '''
795-        Given the indices of two units of interest, compute the spike
796-        time tiling coefficient [1], a metric for causal relationships
797-        between spike trains with some improved intuitive properties
798-        compared to the Pearson correlation coefficient.
799-        [1] Cutts & Eglen. Detecting pairwise correlations in spike
800-            trains: An objective comparison of methods and application
801-            to the study of retinal waves. J Neurosci 34:43,
802-            14288–14303 (2014).
[... 4 more lines not kept]
```

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/elliott-2026.yaml",
 "content": "# Claims for Elliott, Andrews et al. (2026), J. Neurophysiol. 135, \"Microscale maps of bursting\n# dynamics across human hippocampal slices from patients with epilepsy\", doi:10.1152/jn.00217.2025,\n# tested on dandiset 001132 (relation reuses).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data\n# or files; only its title and description on the archive were read.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC12931417, NIHMS2139309; the file\n# header calls it the version of record), with main text, Methods, figure legends, Code and Data\n# Availability, and its one supplement, Extended_Data.pdf (Extended Data Figs. 1 to 13, Extended\n# Data Tables 1 to 4, legends of Videos 1 to 4). Extended Data Tables 1 to 4 and the connection\n# counts of Extended Data Fig. 10 are images that the text garbles; they were read from the PDF\n# pages. The videos (YouTube) were not watched.\n#\n# Code read: github.com/braingeneers/human_hippocampus at commit 0f83f70 (2025-10-07), the\n# repository named under Code Availability. It holds the package src/human_hip (spike data\n# readers, latencies, STTC, eigendecomposition, filters, spectrogram, plotting), per-recording\n# notebooks under experiments/ and the figure notebooks under figures/ (figure_2, figure_3,\n# supplement), and the simulation (figures/supplement/simulation). Details the code settles,\n# where the Methods are silent:\n# - Circuit pairs (figures/figure_3/latencies/t_test_try30_try3/hc112823_acid.ipynb). STTC with a\n#   20 ms window above 0.01; for each unordered pair, the latency from each spike of the first\n#   unit to the nearest spike of the second, kept when its absolute value is at most 30 ms; at\n#   least 25 latencies and absolute mean latency above 1 ms; if the mean is negative the pair is\n#   reversed and recomputed; one-sample two-sided t-test of the latencies against 0 at p < 0.05.\n#   The notebook's saved output for S1 is 784 pairs.\n# - Geometry test (figures/figure_3/haussler/hc112823_acid.ipynb). A degree-2 polynomial y(x)\n#   fitted to all unit positions, sampled at 100 evenly spaced x between the smallest and largest\n#   unit x; each unit's position is the index (0 to 99) of the nearest sample point; a pair's\n#   position is that of its sending unit; its angle is arctan2 of the receiving minus sending\n#   position; Student's two-sample t-test (scipy ttest_ind, equal variances) of positions for\n#   angle >= 0 against angle < 0. The saved output for S1 is p = 9.66e-20 (Table 3 prints 9.7e-20).\n#   The Methods' 0 to 1 normalisation is this index over 100 and does not change the test.\n# - Phase locking (figures/figure_3/TJ_phase_locking_basics.ipynb, figures/supplement/\n#   phase_locking/sig_counts.ipynb). LFP at 1 kHz from the electrode nearest each unit;\n#   Butterworth 4 to 8 Hz (human_hip butter_filter, order 5, sosfiltfilt); Hilbert phase and\n#   envelope; spikes are kept within each theta cycle (trough to trough) whose peak exceeds the RMS\n#   of the envelope; the Rayleigh test is astropy rayleightest; mean angle astropy circmean. The\n#   KA recordings are analysed in hand-chosen seizure windows and non-seizure windows, listed in\n#   seconds in the notebook: S1 seizure [9,28] [38,52] [69,83] [100,113] [138,151] [176,187]\n#   [211,220] [246,254], non-seizure [28,38] [54,66] [85,97] [115,127] [155,167] [193,205]\n#   [228,240] [260,272]; S2 seizure [0,11] [25,39] [139,148] [168,174] [258,263] [320,328]\n#   [481,487], non-seizure [50,60] [100,113] [200,212] [270,275] [392,400] [400,406] [450,455].\n#   The saved counts are S1 seizure 70 of 212, non-seizure 11 of 212; S2 seizure 101 of 180,\n#   non-seizure 8 of 180. The Methods select spikes \"while this upper envelope was above the RMS\",\n#   the code selects spikes in cycles whose peak exceeds it; the Methods are the main reading and\n#   the code's selection a variant.\n# - Phase clusters (figures/figure_3/Phase_lock_heatmap.ipynb). Significant units with duplicate\n#   positions removed, split into two groups by hand-set position thresholds (33 and 28 units for\n#   S1). The repository holds no code for the Kuiper test.\n# - STTC clustering (figures/figure_3/sttc.ipynb). STTC with a 20 ms window (the braingeneers\n#   default); entries of 0.3 or more (the diagonal included) set to 0; Euclidean distances between\n#   rows; complete linkage; optimal leaf ordering. The two groups are read from the reordered\n#   matrix by eye.\n# - Sub-bursts of the S1 initiation stage (figures/figure_2/burst_peak_comparison.ipynb) are set\n#   by hand at 14.4, 14.57, 14.75 and 14.91 s of the S1 KA recording. No code detects bursts,\n#   superbursts, stages or rolling waves.\n# - The LFP filters (human_hip/raw_data/filter.py) are order-5 Butterworth, zero phase; the\n#   Methods give order 5 for the LFP bands and \"fourth order\" for the theta plots.\n#\n# Data the paper used. Recordings of Andrews et al. 2024 (Nat. Neurosci., ref 8), which the\n# dandiset accompanies: organotypic human hippocampal slices (300 um, 4 to 8 days in culture,\n# transduced with AAV9-CAMK2A-HcKCR1-eYFP) from patients with refractory mesial temporal lobe\n# epilepsy, recorded on a MaxOne HD-MEA (26,400 electrodes, about 1,000 selected, 20 kHz). Of 12\n# slices of the original study, 6 with at least 50 sorted units were analysed (S1 to S6, each from\n# a different patient; Extended Data Tables 1 and 4), in 8 recordings:\n#   1 S1, dentate gyrus, kainic acid (KA), seizure-like, 6 min, 212 units (patient A, 52 F, ILAE type 1)\n#   2 S1, baseline (no drug), 5 min, 249 units\n#   3 S2, dentate gyrus, KA, seizure-like, 8.5 min, 180 units (patient B, 35 M, no HS)\n#   4 S2, baseline, 5 min, 51 units\n#   5 S3, dentate gyrus, no drug, 7 min, 87 units (patient C, 20 M, type 3)\n#   6 S4, dentate gyrus, KA, no seizure-like activity, 2.2 min, 109 units (patient D, 46 F, type 2)\n#   7 S5, CA1, no drug, 6.4 min, 136 units (patient E, 40 F, type 3)\n#   8 S6, CA1, no drug, 1.8 min, 100 units (patient F, 46 F, no HS)\n# KA (100 nM) was dripped onto slices in zero-magnesium media during a continuous recording.\n# Measured variables are raw broadband voltage (from which LFP bands are filtered) and single units\n# from Kilosort2 with manual curation in Phy, with unit positions from Kilosort.\n# The code's folder names suggest S1 = Hc112823 (2023-12-03, KA file ..._120323_3), S2 = Hc120523\n# chip21769 (2023-12-11, KA file ..._121123_2), S3 = hc111 (2022-11-02, chip16753), S4 = hc110723\n# (2023-11-13), and S5, S6 = hc328 (2023-04-02) and hc52 (2023-05-10) in an order the code does not\n# state; the unit counts above fix the match.\n#\n# Outside data. The dandiset holds the raw recordings. The curated spike sortings the paper\n# analysed are in the GitHub repository above (Data Availability: \"The repository includes neural\n# spiking data\"), under data/ephys/<recording>/derived/kilosort2/ (for S2 the notebooks also read\n# data/ephys/2023-12-11-e-Hc120523_aav9hckcr1_chip21769/elliott/elliott_chip21769_2.zip). Claims on\n# units use them and are marked with_inputs; re-sorting the raw data with Kilosort2 cannot repeat\n# the manual curation, and the author may show it as a variant. The simulation is code only.\nschema_version: 2\npaper: doi:10.1152/jn.00217.2025\nclaims:\n- id: table1-unit-counts\n  statement: The eight recordings analysed hold 212, 249, 180, 51, 87, 109, 136 and 100 sorted\n    units (recordings 1 to 8) and last 6, 5, 8.5, 5, 7, 2.2, 6.4 and 1.8 minutes.\n  source: Extended Data Table 1\n  inferred: Numbers from Extended Data Table 1, an image in the supplement PDF; no sentence states\n    them.\n  data: with_inputs\n  expected:\n  - quantity: units, recording 1 (S1, KA)\n    value: 212\n    tolerance: 21.2\n  - quantity: units, recording 2 (S1, baseline)\n    value: 249\n    tolerance: 24.9\n  - quantity: units, recording 3 (S2, KA)\n    value: 180\n    tolerance: 18\n  - quantity: units, recording 4 (S2, baseline)\n    value: 51\n    tolerance: 5.1\n  - quantity: units, recording 5 (S3)\n    value: 87\n    tolerance: 8.7\n  - quantity: units, recording 6 (S4, KA)\n    value: 109\n    tolerance: 10.9\n  - quantity: units, recording 7 (S5)\n    value: 136\n    tolerance: 13.6\n  - quantity: units, recording 8 (S6)\n    value: 100\n    tolerance: 10\n  criterion: Units are those of the paper's curated sortings (outside input, see the opening\n    comment); recording durations are read from the dandiset's raw recordings and compared at 10%\n    of each reported length. Reproduced when every unit count and duration is within tolerance;\n    partially reproduced when at least six of the eight recordings match on both.\n- id: fig1g-ka-synchronized-bursting\n  statement: After kainic acid, slice S1 shows synchronized rhythmic bursting, with about 6 to 8\n    bursts grouped within larger burst epochs (superbursts).\n  source: Results, paragraph 1; Figure 1g and 1h\n  quote: After administering kainic acid to slice S1, synchronized rhythmic bursting activity was\n    observed ... approximately 6–8 bursts grouped within larger burst epochs\n  data: with_inputs\n  expected:\n  - quantity: bursts per burst epoch, S1\n    value: 7\n    tolerance: 1.8\n  criterion: The population rate as the Methods define it (spikes of all units in 1 ms bins,\n    Gaussian smoothing with a standard deviation of 10 to 20 ms, divided by the number of units and\n    multiplied by 1000). Neither the paper nor its code defines a burst or a burst epoch; the\n    Figure 1g legend uses the first 150 s of seizure-like activity. Readings named here, not by\n    the paper; a burst is a peak of the population rate (sigma 10 ms, and 20 ms) exceeding (a)\n    twice its mean over the pre-KA part of the recording, or (b) its mean plus 3 standard\n    deviations over the whole recording, with peaks less than 50 ms apart merged; epochs are runs\n    of bursts separated by gaps under 5 s. The expected value is the range 6 to 8 widened by 10%\n    of each bound (5.4 to 8.8). Reproduced when, under one reading, the median number of bursts\n    per epoch in the first 150 s lies in that range and the bursts are synchronous across units\n    (a burst raises the rate of most units).\n- id: methods-burst-counts\n  statement: Slice S1 had 67 bursts grouped into 11 superbursts over about 350 s; S2 had 47\n    bursts, highly synchronized for the first 50 s and sporadic for the next 300 s.\n  source: Methods, Classification of Epileptiform-like Events, paragraph 1; Extended Data Fig. 13\n  quote: Slice S1 contained 67 bursts during its seizure-like event. The bursts were highly\n    synchronized and grouped into 11 sets of super bursts over 350 seconds. Slice S2 contained 47\n    bursts. The bursts for S2 were highly synchronized for the first 50 seconds, but then were\n    sporadic for the next 300 seconds.\n  data: with_inputs\n  depends_on:\n  - fig1g-ka-synchronized-bursting\n  expected:\n  - quantity: bursts, S1 KA recording\n    value: 67\n    tolerance: 6.7\n  - quantity: superbursts, S1 KA recording\n    value: 11\n    tolerance: 1.1\n  - quantity: duration of bursting, S1\n    value: 350\n    tolerance: 35\n    unit: s\n  - quantity: bursts, S2 KA recording\n    value: 47\n    tolerance: 4.7\n  - quantity: duration of synchronized bursting, S2\n    value: 50\n    tolerance: 5\n    unit: s\n  criterion: Bursts and superbursts as in fig1g-ka-synchronized-bursting, under the same readings,\n    which are not fixed by the paper or its code. Note that the code's seizure windows for S1 list\n    8 superbursts in the first 254 s (opening comment), which bears on reading the count of 11.\n    Reproduced when, under one reading, all five values are within tolerance; partially\n    reproduced when the S1 counts or the S2 values match but not both.\n- id: methods-rate-increase-after-ka\n  statement: Neural activity increased after kainic acid; the population firing rate rose by 0.5\n    spikes per second per unit in S1 and 0.9 in S2.\n  source: Methods, Classification of Epileptiform-like Events, paragraph 1\n  quote: The population firing rate increased by 0.5 spikes per second per unit for S1 and 0.9\n    spikes per second per unit for slice S2.\n  data: with_inputs\n  expected:\n  - quantity: increase in mean rate per unit, S1\n    value: 0.5\n    tolerance: 0.05\n    unit: spikes/s\n  - quantity: increase in mean rate per unit, S2\n    value: 0.9\n    tolerance: 0.09\n    unit: spikes/s\n  criterion: Mean rate per unit as the Methods define it (spike count over duration, Methods,\n    Neuronal Firing Activity Heatmaps). The paper does not say what the rate after KA is compared\n    with. Readings; (a) the KA recording after KA onset against the same recording before it (the\n    recording was continuous during administration, Methods, Tissue preparation), (b) the whole KA\n    recording against the separate baseline recording of the same slice (Extended Data Table 1),\n    (c) the bursting period (about 350 s) against the baseline recording. Reproduced when both\n    values are within tolerance under one reading; partially reproduced when the rate rises in\n    both slices but the values miss.\n- id: methods-onset-latency\n  statement: Epileptiform-like activity began in S1 and S2 shortly after kainic acid was applied,\n    within 15 s by one passage of the Methods and within 30 s by another.\n  source: Methods, Tissue preparation, paragraph 1; Methods, Classification of Epileptiform-like\n    Events, paragraph 1\n  quote: Slices S1 and S2 from the dentate gyrus exhibited epileptiform-like activity within\n    fifteen seconds after the administration of kainic acid.\n  data: with_inputs\n  depends_on:\n  - fig1g-ka-synchronized-bursting\n  criterion: The time from KA application to the first burst (bursts as in\n    fig1g-ka-synchronized-bursting). The time of application must come from the dandiset's\n    metadata or annotations; if it is not there the claim is blocked as metadata_insufficient.\n    Reproduced when the latency is at most 15 s in both slices; partially reproduced when it is at\n    most 30 s (the other passage) in both.\n- id: s4-ka-no-epileptiform\n  statement: Slice S4 received kainic acid but showed no epileptiform-like behaviour, and none of\n    S3 to S6 showed seizure-like activity.\n  source: Results, last paragraph before Discussion; Extended Data Table 1\n  quote: Notably, slice S4 was administered kainic acid, but did not exhibit any epileptiform-like\n    behavior or the circuit dynamics of S1 and S2.\n  data: with_inputs\n  depends_on:\n  - fig1g-ka-synchronized-bursting\n  criterion: A claim of absence. The paper's classification (Results, paragraph 1, and Methods,\n    Classification of Epileptiform-like Events) is highly synchronized bursting with LFP\n    activity across multiple channels lasting over ten seconds. Bursts as in\n    fig1g-ka-synchronized-bursting, under each of its readings. Reproduced when no recording of S3\n    to S6 has synchronized bursting sustained for more than 10 s, while S1 and S2 KA recordings do\n    under the same reading; not reproduced when any of S3 to S6 does.\n- id: ext3-onset-spectral-signature\n  statement: At the onset of seizure-like activity in S1 the LFP shows a large upwelling of delta\n    power and an increase in theta amplitude, with theta activity aligned with bursts, and this\n    holds at different electrodes.\n  source: Results, paragraph 1; Figure 1i; Extended Data Fig. 3\n  quote: These include a defined increase in the amplitude of theta-band oscillations, coherence\n    between theta-band activity and bursting behavior, and a large upwelling in the delta-band\n    frequency at epileptiform-like onset ... These characteristics remained present across\n    different electrode sites\n  data: with_inputs\n  criterion: Spectrogram as in the Methods (Spectrogram, and Local field potential signal\n    processing); raw signal low-passed 0.1 to 100 Hz and downsampled to 1 kHz, complex Morlet\n    wavelet cmor1-1, power as the squared magnitude, Gaussian smoothing sigma 2. Onset is the first\n    burst of the first superburst (bursts as in fig1g-ka-synchronized-bursting). The electrodes\n    are not named; Extended Data Fig. 3 shows three in the granule cell layer. Readings; three\n    electrodes nearest the units with the highest firing rate, and three electrodes spread along\n    the granule cell layer. The baseline window is not fixed; the 5 s before the first burst is\n    used. Reproduced when, at each of the three electrodes, delta (0.5 to 4 Hz) power in the 2 s\n    after onset is above the baseline mean and the theta (4 to 8 Hz) amplitude exceeds twice the\n    baseline (the Methods' \">2x baseline LFP\" criterion); partially reproduced when this holds at\n    one or two electrodes. The alignment of theta with bursts is tested in\n    table2-phase-locking-counts.\n- id: fig1j-theta-propagation-stages\n  statement: In S1 theta-band activity shows no pattern at baseline, a standing wave oscillating\n    across the length of the granule cell layer at initiation, and at the seizure stage a rolling\n    wave orthogonal to the initiation direction, moving from the hilar to the outer aspect; S2\n    shows the same stages.\n  source: Results, paragraphs 3 and 4; Figure 1j; Extended Data Fig. 4c to 4e and Fig. 5c to 5d\n  quote: During the initiation stage, theta propagations form a standing wave that oscillates\n    across the length of the granule cell layer ... Following initiation and during all subsequent\n    bursts, the theta oscillations form a rolling wave orthogonal to the direction observed during\n    the initiation stage, moving along the granule cell layer from the hilar to outer aspect\n  criterion: The paper shows this in plots and videos and judges it by eye. Theta per electrode\n    by a Butterworth 4 to 8 Hz filter of the raw signal (Methods, Theta wave activity plots; order\n    4 in that passage, 5 in the code; both are run). Stages from the Results; baseline is before\n    the first burst, initiation is the first burst, seizure is subsequent bursts; their exact\n    windows are not given. The direction of propagation is not measured in the paper. Readings\n    named here; per stage, the direction of the spatial gradient of the pairwise lag (from the\n    lag matrix of ext4-electrode-lag-clusters) fitted as a plane over electrode positions.\n    Reproduced when, in S1 and S2, the initiation and seizure directions differ by 60 to 120\n    degrees, the seizure direction runs across the layer (from its hilar side) and the baseline\n    plane fit explains less of the lag variance than either other stage.\n- id: ext4b-theta-delay\n  statement: During seizure-like activity theta waves in S1 reach three electrodes along the\n    propagation direction in turn, with a 40 ms delay from the first to the second and from the\n    second to the third.\n  source: Extended Data Fig. 4a and 4b legend\n  quote: There is a 40ms delay between theta waves as they propagate from e1 to e2, and from e2 to\n    e3.\n  expected:\n  - quantity: theta lag between successive electrodes, S1 seizure stage\n    value: 40\n    tolerance: 4\n    unit: ms\n  criterion: The three electrodes are shown only in the figure. Lag as in the Methods (Electrode\n    spatial clustering algorithm); the lag maximising the absolute cross-correlation of the theta\n    signals, within -40 to 40 ms. Readings; the median lag over all electrode pairs spaced along\n    the seizure-stage direction (from fig1j-theta-propagation-stages) at the spacing of the\n    figure's electrodes, and the lag for three electrodes chosen from the figure's map. Reproduced\n    when one reading gives successive lags within tolerance with the same sign.\n- id: ext4-electrode-lag-clusters\n  statement: In the two epileptiform slices, k-means clustering of electrodes by their pairwise\n    theta lags gives spatial clusters that replicate the theta propagation of each stage, while\n    the slices without epileptiform activity (S3 to S6) show no spatial pattern.\n  source: Results, paragraph 4; Extended Data Fig. 4f to 4g, Fig. 5e and Fig. 6\n  quote: For each stage of the recording, electrodes were clustered based on their average time\n    delay between theta propagations ... Spatial maps of the electrode clusterings replicated the\n    behavior seen in theta wave propagations ... The slices with no epileptiform-like activity\n    (S3-S6) did not contain spatially coherent theta-band wave propagation patterns\n  criterion: Method from the Methods (Electrode spatial clustering algorithm); theta per\n    electrode, scipy correlate for all electrode pairs, the lag maximising the absolute\n    correlation within -40 to 40 ms, the square lag matrix, k-means with 2 clusters on its rows.\n    For S3 to S6 the Extended Data Fig. 6 legend says segments \"that contained higher than\n    average burst-like activity\" were used; the segment length is not given. The paper judges\n    spatial coherence by eye. Measure named here, not from the paper; the fraction of electrodes\n    whose cluster label equals the majority label of their 8 nearest electrodes, against the same\n    fraction after shuffling labels over positions (1000 shuffles). Reproduced when the initiation\n    and seizure stages of S1 and S2 are spatially coherent beyond all shuffles and S3 to S6 are\n    markedly less coherent than S1 and S2; partially reproduced when only one of the two parts\n    holds.\n- id: methods-rolling-wave-counts\n  statement: The rolling wave appeared in every investigated burst of S1 and in about 75% of those\n    of S2, 2 to 4 times per burst, giving about 200 stereotypic propagations in S1's seizure stage\n    and 35 in S2's.\n  source: Methods, Theta wave activity plots and videos, paragraph 3\n  quote: We saw this rolling wave in every burst we investigated from slice S1. The rolling wave\n    was present in ~75% of the bursts we investigated from slice S2 ... The rolling wave pattern\n    occurred 2–4 times per burst. Thus, over the six minute timespan of recordings from S1 and S2,\n    there were approximately 200 stereotypic propagations in S1's seizure stage, and 35 in S2's.\n  expected:\n  - quantity: fraction of S2 bursts with a rolling wave\n    value: 0.75\n    tolerance: 0.075\n  - quantity: rolling waves per burst\n    value: 3\n    tolerance: 1.4\n  - quantity: rolling wave propagations, S1 seizure stage\n    value: 200\n    tolerance: 20\n  - quantity: rolling wave propagations, S2 seizure stage\n    value: 35\n    tolerance: 3.5\n  criterion: The paper counted rolling waves by watching videos and gives no detector or the list\n    of bursts investigated. This claim cannot be judged on the paper's method; it is blocked as\n    methods_underspecified unless a detector defined in fig1j-theta-propagation-stages (a theta\n    cycle whose lag-plane direction matches the seizure direction within 45 degrees and explains\n    most of the lag variance) is adopted as an assumption, in which case it is reproduced when all\n    four values are within tolerance (the range 2 to 4 widened by 10% of each bound is 1.8 to\n    4.4).\n- id: fig2a-subbursts-track-theta\n  statement: At the initiation stage of S1 the first burst splits into three sub-bursts whose\n    peaks and troughs coincide with the theta oscillation, and the change in single-unit firing\n    from sub-burst to sub-burst alternates between the same two spatial modes as theta; S2 shows a\n    similar pattern.\n  source: Results, paragraph 5; Figure 2a; Extended Data Fig. 5f\n  quote: We found that theta-band oscillations during the initiation stage of S1 are temporally\n    aligned with sub-bursts in single unit spiking activity ... Calculating the change in single\n    unit firing from sub-burst to sub-burst produced heatmaps with similar spatiotemporal\n    oscillations to those seen in theta-band propagations.\n  data: with_inputs\n  criterion: Sub-bursts of S1 as set in the paper's code, 14.4 to 14.57, 14.57 to 14.75 and 14.75\n    to 14.91 s of the KA recording (figures/figure_2/burst_peak_comparison.ipynb); for S2 the\n    paper gives no times, and they are taken from figures/supplement/seizure_2/\n    seizure2_burst_peaks.ipynb. Heatmaps as in the Methods (Neuronal Firing Activity Heatmaps);\n    per-unit spike counts in each sub-burst, the difference between consecutive sub-bursts,\n    binned on a 30 by 30 grid and Gaussian-smoothed. The theta modes are the two k-means electrode\n    clusters of the initiation stage (ext4-electrode-lag-clusters). Measure named here; for each\n    difference map, the mean firing change of units over each electrode cluster. Reproduced, for\n    each slice, when the sign of the cluster difference flips between the first and second\n    difference maps (firing alternates between the two modes) and the theta signal averaged over\n    each cluster changes sign between the same sub-bursts.\n- id: table2-phase-locking-counts\n  statement: Significantly theta phase-locked units are 70 of 212 (33%) in the S1 KA recording and\n    101 of 180 (56%) in the S2 KA recording, against 14 of 249, 2 of 51, 8 of 87, 6 of 109, 8 of\n    136 and 1 of 100 in the other recordings.\n  source: Extended Data Table 2; Results, paragraph 6\n  inferred: Counts from Extended Data Table 2, an image in the supplement PDF; the text states only\n    the averages (see table2-phase-locking-seizure-vs-not).\n  data: with_inputs\n  expected:\n  - quantity: phase-locked units, recording 1 (S1, KA)\n    value: 70\n    tolerance: 7\n  - quantity: phase-locked units, recording 2 (S1, baseline)\n    value: 14\n    tolerance: 1.4\n  - quantity: phase-locked units, recording 3 (S2, KA)\n    value: 101\n    tolerance: 10.1\n  - quantity: phase-locked units, recording 4 (S2, baseline)\n    value: 2\n    tolerance: 0.2\n  - quantity: phase-locked units, recording 5 (S3)\n    value: 8\n    tolerance: 0.8\n  - quantity: phase-locked units, recording 6 (S4)\n    value: 6\n    tolerance: 0.6\n  - quantity: phase-locked units, recording 7 (S5)\n    value: 8\n    tolerance: 0.8\n  - quantity: phase-locked units, recording 8 (S6)\n    value: 1\n    tolerance: 0.1\n  criterion: Method from the Methods (Phase locking neurons to theta wave activity) with the\n    code's choices (opening comment); theta 4 to 8 Hz from the electrode nearest each unit,\n    Hilbert phase, spikes kept while the upper envelope exceeds the RMS of the whole series (the\n    Methods; the code's cycle-peak selection is a variant), Rayleigh test at p < 0.05 per unit\n    over all units of the curated sorting. For recordings 1 and 3 the code's seizure windows are\n    used, as its saved counts match the table. For the other recordings the analysed span is not\n    given; readings are the whole recording, and the spans of the code's get_raw_data notebooks\n    (figures/supplement/phase_locking/get_raw_data). Small counts are judged at 10% rounded up to\n    one unit, as a tolerance below one unit cannot be met. Reproduced when every count is within\n    tolerance under one reading; partially reproduced when recordings 1 and 3 match and the others\n    stay below 10%.\n- id: table2-phase-locking-seizure-vs-not\n  statement: During seizure-like activity on average 45% of units per recording are phase locked,\n    against 5% in recordings without seizure-like activity; within S1 and S2, only 5% and 4% are\n    phase locked outside the seizure periods.\n  source: Extended Data Table 2 legend; Extended Data Fig. 8c to 8d; Results, paragraph 6\n  quote: During seizure-like activity, on average, 45% of neurons per recording are phase locked.\n    This is considerably higher than the 5% average seen in recordings with no seizure-like\n    activity. In the recordings that expressed seizure-like behavior, average phase locking was\n    considerably higher in the portions of the recording with epileptiform activity, compared to\n    the portions without\n  data: with_inputs\n  depends_on:\n  - table2-phase-locking-counts\n  expected:\n  - quantity: mean percent phase locked, recordings 1 and 3 (seizure windows)\n    value: 45\n    tolerance: 4.5\n    unit: percent\n  - quantity: mean percent phase locked, recordings 2 and 4 to 8\n    value: 5\n    tolerance: 0.5\n    unit: percent\n  - quantity: percent phase locked outside seizure, S1 KA recording\n    value: 5\n    tolerance: 0.5\n    unit: percent\n  - quantity: percent phase locked outside seizure, S2 KA recording\n    value: 4\n    tolerance: 0.4\n    unit: percent\n  criterion: As table2-phase-locking-counts, with the code's non-seizure windows for the last two\n    values (its saved results are 11 of 212 and 8 of 180). The mean is over recordings (the table\n    legend says \"on average ... per recording\"). Reproduced when all four values are within\n    tolerance; partially reproduced when the seizure mean is within tolerance and every other\n    value is below 10%.\n- id: fig2b-phase-cluster-kuiper\n  statement: In S1 the significantly phase-locked units form two spatial groups along the granule\n    cell layer whose preferred theta phases differ significantly (Kuiper test).\n  source: Results, paragraph 6; Figure 2b; Extended Data Fig. 8a\n  quote: Clustering based on the two modes of significant units yielded two groups with\n    significantly different phase angles\n  statistics:\n  - about: phase angles of the two clusters of phase-locked units, S1\n    test: Kuiper's test\n    p: 0.01\n    n: 70 significant units of S1 (33 and 28 after removing duplicate positions, per the code)\n  data: with_inputs\n  depends_on:\n  - table2-phase-locking-counts\n  criterion: The Results print p = 0.01 and the Figure 2b legend p < 0.01; both are accepted. Units\n    are those significant in the seizure windows (table2-phase-locking-counts). Groups per the\n    Methods (Methodology for heatmap of phase locked angles); the polar mode of the significant\n    units' mean angles, each unit's absolute angular difference from it, and a split into two\n    groups. The Methods do not say how the split is made and the code sets position thresholds by\n    hand (figures/figure_3/Phase_lock_heatmap.ipynb). Readings; (a) the code's thresholds on unit\n    position (group 1 is x < 940, or x = 945 with y < 1120, or x > 900 with y < 900, in um),\n    (b) a split of the angular difference at its median, (c) k-means with 2 clusters on unit\n    position. The Kuiper test is not in the code; astropy kuiper_two is used. Reproduced when\n    under one reading the test gives p <= 0.01; partially reproduced when p < 0.05.\n- id: fig2c-sttc-two-clusters\n  statement: Hierarchical clustering of the STTC matrix of S1 gives two groups of units that\n    divide the granule cell layer into the same two spatial modes, and S2 gives a similar result.\n  source: Results, paragraph 7; Figure 2c; Extended Data Fig. 5h\n  quote: Two groupings of neuronal populations were created by performing hierarchical clustering\n    on the spike time tiling coefficient (STTC) matrix ... A spatial map of the neuronal clusters\n    divides the granule cell layer into the same two modes seen in previous plots. Similar results\n    were observed in the second epileptiform-like slice (S2)\n  data: with_inputs\n  criterion: Method from the Methods (Methodology for STTC hierarchical clustering) and\n    figures/figure_3/sttc.ipynb; STTC over the whole KA recording with a 20 ms window, entries of\n    0.3 or more set to 0 (the code; the Methods say \"thresholded to 0.3\", read also as clipping at\n    0.3, run as a variant), Euclidean distances between rows, complete linkage, optimal leaf\n    ordering. The paper reads two clusters by eye; here the tree is cut into 2 clusters\n    (scipy fcluster, maxclust 2), and, as a variant, into the two largest clusters of a cut at\n    half the maximum distance as the code prints. Reproduced, for each slice, when the two\n    clusters each hold at least 10% of units and are spatially separated along the layer's long\n    axis (unit positions projected on the degree-2 fit of table3-geometry-test; two-sided\n    Mann-Whitney test of positions between clusters at p < 0.05) and the split is on the same side\n    as the phase-cluster split of fig2b-phase-cluster-kuiper, reading (a), for S1.\n- id: ext9-sttc-eigenvector-gradient\n  statement: The first eigenvector of the STTC matrix, mapped onto the units, forms a gradient\n    across the granule cell layer in both S1 and S2, reproducing the hierarchical clusters.\n  source: Results, paragraph 7; Extended Data Fig. 9f to 9h; Methods, Eigendecomposition for\n    neural spatial clustering\n  quote: A second clustering method based on the eigendecomposition of the STTC matrix reproduced\n    these results\n  data: with_inputs\n  depends_on:\n  - fig2c-sttc-two-clusters\n  criterion: STTC matrix as in figures/figure_3/sttc.ipynb (20 ms window, no threshold), its first\n    eigenvector by human_hip eigenvalues_eigenvectors (numpy eigh, descending order). The paper\n    judges the gradient by eye. Reproduced, for each slice, when the Spearman correlation between\n    the eigenvector values and unit position along the layer (projection as in\n    table3-geometry-test) has p < 0.05, and the eigenvector values differ between the two clusters\n    of fig2c-sttc-two-clusters (two-sided Mann-Whitney, p < 0.05).\n- id: ext9-sttc-beats-correlation\n  statement: For S1, the STTC matrix has larger eigenvalues and a lower reconstruction error than\n    the correlation matrix of the spike trains.\n  source: Methods, Eigendecomposition for neural spatial clustering; Extended Data Fig. 9c and 9d\n  quote: For our data, the STTC matrix had higher eigenvalues and a lower reconstruction error when\n    compared to correlation.\n  data: with_inputs\n  criterion: STTC with a 20 ms window and the correlation matrix of the 1 ms raster smoothed with a\n    Gaussian of sigma 5 ms (human_hip correlation_matrix, the default the code uses). The\n    reconstruction error is not defined in the paper; reading named here, the Frobenius norm of the\n    matrix minus its rank-k eigen-reconstruction, divided by the norm of the matrix, for k = 1 to\n    20. Reproduced when each of the first 20 eigenvalues is larger for STTC and the STTC error is\n    lower for every k from 1 to 20; partially reproduced when both hold for most k.\n- id: fig3a-significant-pairs\n  statement: Of about 45,000 neuron pairs in S1, 784 have a significant directed latency and form\n    the circuit diagram; the other recordings give 1940 (S2 KA), 304 (S1 baseline), 37 (S2\n    baseline), 79 (S3), 37 (S4), 172 (S5) and 92 (S6) significant pairs.\n  source: Methods, Definition of circuit diagram propagation vector; Figure 3a; Extended Data\n    Fig. 10 and 11a\n  quote: Of the 45,000 neuronal pairs of neurons in slice S1, 784 pairs were classified as\n    significant.\n  data: with_inputs\n  expected:\n  - quantity: significant pairs, S1 KA\n    value: 784\n    tolerance: 78.4\n  - quantity: significant pairs, S2 KA\n    value: 1940\n    tolerance: 194\n  - quantity: significant pairs, S1 baseline\n    value: 304\n    tolerance: 30.4\n  - quantity: significant pairs, S2 baseline\n    value: 37\n    tolerance: 3.7\n  - quantity: significant pairs, S3\n    value: 79\n    tolerance: 7.9\n  - quantity: significant pairs, S4\n    value: 37\n    tolerance: 3.7\n  - quantity: significant pairs, S5\n    value: 172\n    tolerance: 17.2\n  - quantity: significant pairs, S6\n    value: 92\n    tolerance: 9.2\n  criterion: Pair selection as the Methods state it (STTC above 0.01, latencies to the nearest\n    spike within -30 to 30 ms, at least 25 latencies, absolute mean latency at least 1 ms,\n    two-tailed one-sample t-test against 0 at p < 0.05), with the code's details (opening\n    comment; STTC window 20 ms, unordered pairs oriented by the sign of the mean latency). The\n    counts other than S1 are read from Extended Data Fig. 10. \"45,000\" is read as the 212 squared\n    candidate pairs the code prints. Reproduced when every count is within tolerance; partially\n    reproduced when S1 and S2 KA match and at least four of the other six.\n- id: fig3a-bipolar-angle-histograms\n  statement: The latency-weighted propagation angle histograms are bipolar (two modes 180 degrees\n    apart, aligned with the initiation theta propagation) for the epileptiform slices S1 and S2,\n    unimodal for the other dentate gyrus slices S3 and S4, and bimodal but not bipolar (two\n    orthogonal directions) for the CA1 slices S5 and S6.\n  source: Results, paragraphs 9 and 10; Figure 3a and 3c; Extended Data Fig. 10\n  quote: For slice S1, the angle histogram was bipolar, which we define as angular pairwise\n    correlations that are 180° out of phase ... None of the non-epileptiform-like slices displayed\n    the bimodal circuit diagram observed from the epileptiform-like slices. Both of the\n    non-epileptiform-like dentate gyrus slices (S3 and S4) had a unimodal circuit diagram ... The\n    slices from CA1 (S5 and S6) had evenly distributed circuit diagrams and a bimodal, but not\n    bipolar, angle histogram\n  data: with_inputs\n  depends_on:\n  - fig3a-significant-pairs\n  criterion: Angles of all significant pairs from sending to receiving unit position, each\n    weighted by its number of latency events (Methods, Propagation angle histogram). The paper\n    judges the shapes by eye. Measures named here, not from the paper; the weighted first-order\n    resultant length R1 and the axial (angles doubled) resultant length R2, and the angle between\n    the two largest peaks of a 16-bin weighted histogram. Bipolar is two peaks 150 to 210 degrees\n    apart with R2 > R1; unimodal is R1 > R2 with one dominant peak; bimodal not bipolar is two\n    peaks 60 to 120 degrees apart. Reproduced when all six slices (KA recordings for S1, S2 and\n    S4) fall in their stated class; partially reproduced when S1 and S2 are bipolar and no other\n    slice is.\n- id: ext10-baseline-same-circuit\n  statement: In S1 and S2 the baseline recordings before kainic acid show the same bipolar circuit\n    as the recordings during epileptiform activity, suggesting a structural property of the\n    slices.\n  source: Results, paragraph 10; Extended Data Fig. 10a to 10d\n  quote: For both S1 and S2, the non-epileptiform-like recordings prior to administering kainic\n    acid had the same circuit diagram as during epileptiform-like activity\n  data: with_inputs\n  depends_on:\n  - fig3a-bipolar-angle-histograms\n  criterion: As fig3a-bipolar-angle-histograms on recordings 2 and 4. Reproduced when both baseline\n    recordings are bipolar and each mode lies within 45 degrees of a mode of the KA recording of\n    the same slice; partially reproduced when this holds for one slice.\n- id: table3-geometry-test\n  statement: The circuit geometry test gives p-values orders of magnitude smaller for the slices\n    with recurrent circuits (S1 KA 9.7e-20, S1 baseline 8.6e-13, S2 KA 1.6e-68, S2 baseline\n    1.0e-6) than for the others (S3 0.12, S4 0.37, S5 0.00042, S6 0.0011), so the bipolar circuits\n    are not an artefact of where the neurons lie.\n  source: Results, last paragraph; Figure 3b; Extended Data Table 3; Methods, Statistical test of\n    circuit geometry\n  quote: If the bipolar plots from epileptiform-like slices were produced by bias in neuronal\n    geometry, the test's p -values would be similar for all slices, however, we found the\n    epileptiform-like slices to be orders of magnitude more significant\n  statistics:\n  - about: positions of positive against negative angle connections, S1 KA (Figure 3b)\n    test: two-tailed t-test\n    p: 1.0e-19\n    p_relation: \"<\"\n  data: with_inputs\n  depends_on:\n  - fig3a-significant-pairs\n  expected:\n  - quantity: -log10 p, recording 1 (S1, KA)\n    value: 19.01\n    tolerance: 1.9\n  - quantity: -log10 p, recording 2 (S1, baseline)\n    value: 12.07\n    tolerance: 1.21\n  - quantity: -log10 p, recording 3 (S2, KA)\n    value: 67.8\n    tolerance: 6.78\n  - quantity: -log10 p, recording 4 (S2, baseline)\n    value: 6.0\n    tolerance: 0.6\n  - quantity: -log10 p, recording 5 (S3)\n    value: 0.92\n    tolerance: 0.09\n  - quantity: -log10 p, recording 6 (S4)\n    value: 0.43\n    tolerance: 0.04\n  - quantity: -log10 p, recording 7 (S5)\n    value: 3.38\n    tolerance: 0.34\n  - quantity: -log10 p, recording 8 (S6)\n    value: 2.96\n    tolerance: 0.3\n  criterion: Test as in the Methods with the code's details (opening comment); all significant\n    pairs of fig3a-significant-pairs, unweighted, degree-2 polynomial fit to unit positions, the\n    sending unit's position along it, Student's t-test of positions for angle >= 0 against angle\n    < 0. The values are compared on -log10 p because p-values span many orders of magnitude; the\n    tolerance is 10% of that value. The direction of the y axis (image rows or microns upward)\n    flips the sign of every angle and so the groups; both are run. Reproduced when all eight\n    values are within tolerance; partially reproduced when every recording of S1 and S2 has a p\n    value at least 100 times smaller than every recording of S3 to S6.\n- id: ext12-simulation-recurrence\n  statement: In a simplified dentate gyrus network model, increasing recurrent connectivity between\n    granule cells produces seizure-like bursting.\n  source: Results, paragraph 8; Discussion, paragraph 1; Extended Data Fig. 12; Methods, Simulation\n    of epileptiform behavior\n  quote: We constructed an in silico model to simulate functional connectivity within the dentate\n    gyrus ( Extended Data Fig. 12 ) 48 and found that increasing pairwise interactions between\n    granule cells produced seizure-like bursting events.\n  data: elsewhere\n  where: GitHub braingeneers/human_hippocampus at commit 0f83f70, figures/supplement/simulation\n  criterion: Run figures/supplement/simulation/simulation.py at its four connectivity levels with\n    1000 granule cells (Extended Data Fig. 12). Bursting measured by the population rate as in\n    fig1g-ka-synchronized-bursting. Reproduced when the number of synchronized bursts increases\n    with connectivity across the four levels and is near zero at the lowest.\n"
}
```

```
File created successfully at: claims/elliott-2026.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/elliott-2026.yaml paper/10.1152-jn.00217.2025.txt; echo "exit $?"; grep -n -E "—|rather" claims/elliott-2026.yaml; grep -v '^#' claims/elliott-2026.yaml | grep -n -E '[^ ]: ' | grep -v -E '^\s*[0-9]+:\s*-? ?[a-z_]+: ' | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/elliott-2026.yaml'));c=d['claims']
print(len(c),sum('quote' in x for x in c),sum('inferred' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
from collections import Counter;print(Counter(x.get('data','dataset') for x in c))"
```

```
23 21 2 2 23 10
Counter({'with_inputs': 18, 'dataset': 4, 'elsewhere': 1})
```

**Agent**

I wrote `claims/elliott-2026.yaml` with 23 claims, and the quote checker reports 0 problems. Nothing the claims needed was missing from the paper text.

**What I read**
- **Text:** the accepted author manuscript from PubMed Central (PMC12931417). The file header calls it the version of record. It includes the main text, Methods, figure legends and the Code and Data Availability statements.
- **Supplement:** Extended_Data.pdf (Extended Data Figs. 1 to 13 and Tables 1 to 4). Tables 1 to 4 and the connection counts in Extended Data Fig. 10 are images in the PDF, so I read those pages from the PDF itself. I did not watch the videos.
- **Code:** github.com/braingeneers/human_hippocampus at commit 0f83f70. Its saved outputs match the paper: 784 significant pairs and p = 9.66e-20 for S1, and 70 of 212 and 101 of 180 phase-locked units.
- **Dataset:** DANDI 001132 holds the raw recordings from Andrews et al. 2024. The curated spike sortings the paper analysed are only in the GitHub repo.

**Claims**
- All 23 have a criterion. 21 have quotes, and 2 are marked `inferred` because their numbers appear only in Extended Data Tables 1 and 2.
- 10 have expected values and 2 have statistics: the Kuiper p = 0.01 and the geometry t-test p < 1e-19.
- By data source: 18 are `with_inputs` because they need the GitHub sortings, 4 use the dataset alone (the LFP and theta claims), and 1 is `elsewhere` (the simulation code).

**Details the code settles, where the Methods are silent**
- **Circuit pairs:** STTC window 20 ms, pairs flipped to point in the direction of positive mean latency.
- **Geometry test:** position is the nearest of 100 points on the fitted curve; the test is Student's t on angle ≥ 0 against angle < 0.
- **Phase locking:**
  - The LFP comes from the electrode nearest each unit.
  - The seizure and non-seizure windows are set by hand.
  - The Methods select spikes while the envelope is above its RMS, but the code selects spikes in cycles whose peak exceeds it. I followed the Methods and named the code's version as a variant.
- **STTC clustering:** entries of 0.3 or more are set to 0, with complete linkage.
- **Filters:** Butterworth order 5. The Methods also mention a fourth-order filter, so both are run.

**Details left open, with the readings named for each**
- **Bursts and superbursts:** the code has no detector. Readings are a population-rate peak above 2× the pre-KA mean, or above mean + 3 SD, at smoothing of 10 and 20 ms. The code's own S1 windows list 8 superbursts where the text says 11.
- **Firing-rate increase after KA:** compared within the KA recording (before vs after onset), against the separate baseline recording, or over the bursting period only.
- **Onset latency:** one Methods passage says within 15 s, another within 30 s. Both are accepted, and the KA application time must come from the dataset's metadata.
- **Spectrogram:** which electrodes are used is not stated. Readings are electrodes near the most active units, or electrodes spread along the layer.
- **Phase-cluster split for the Kuiper test:** the code's hand-set position thresholds, a median split, or k-means on position. No Kuiper code exists, so I specified astropy's `kuiper_two`. The text prints p = 0.01 and the legend p < 0.01; both are accepted.
- **Phase-locking span for non-KA recordings:** the whole recording, or the spans used in the code's get_raw_data notebooks.
- **STTC threshold:** values of 0.3 or more set to zero (code) or clipped at 0.3 (variant). The two clusters are cut with fcluster set to 2 clusters, or as the code cuts them.
- **Geometry test:** y-axis direction, both run. Tolerance is 10% of −log10 p.
- **"45,000 pairs":** read as 212², as the code prints it.

**Claims the paper judges by eye** (stage directions, electrode clusters, bipolar histograms, eigenvector gradient, sub-burst alternation, reconstruction error): for these I wrote measures myself and labelled them in the criteria as not from the paper.

**Weakest points**
- The rolling-wave counts come from watching videos and have no detector, so that claim is blocked as `methods_underspecified` unless a detector is adopted as an assumption.
- The S2 sub-burst times are not in the paper. They are taken from the code's notebook for S2.
- The code shows which folder is which slice except for S5 and S6. The unit counts (136 and 100) fix that match.

## End of run

49 turns, 7 minutes, $3.08 at API prices, result: success.
