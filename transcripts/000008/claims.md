# 000008 · claims · run 39473060510

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000008/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 30000 claims/001453/*.yaml
```

**Agent calls Bash**

```bash
wc paper/*.txt; head -60 paper/*.txt
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
[... 301 more lines not kept]
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 4000 paper/*.txt | sed -n '1,400p' | cut -c1-4000 | head -c 45000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 200 paper/*.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt"
}
```

```
1	DOI: 10.1038/s41586-020-2907-3
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Nature Nature 981 npgopen 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC8113357 PMC8113357.2 8113357 8494644 33184512 
8	10.1038/s41586-020-2907-3 2907 2 Article Phenotypic variation of transcriptomic cell types in mouse motor cortex Scala Federico 1 2 http://orcid.org/0000-0002-5639-7209 Kobak Dmitry 3 
9	http://orcid.org/0000-0003-4458-117X Bernabucci Matteo 1 2 Bernaerts Yves 3 4 http://orcid.org/0000-0003-1963-8285 Cadwell Cathryn René 5 Castro Jesus Ramon 1 2 Hartmanis Leonard 6 
10	http://orcid.org/0000-0001-8066-1383 Jiang Xiaolong 1 2 7 Laturnus Sophie 3 Miranda Elanine 1 2 Mulherkar Shalaka 2 Tan Zheng Huan 1 2 http://orcid.org/0000-0002-9361-5607 Yao Zizhen 8 
11	http://orcid.org/0000-0002-0326-5878 Zeng Hongkui 8 http://orcid.org/0000-0001-6473-1740 Sandberg Rickard 6 http://orcid.org/0000-0002-0199-4727 Berens Philipp [removed: an e-mail address] 3 9 10 
12	11 http://orcid.org/0000-0002-4305-6376 Tolias Andreas S. [removed: an e-mail address] 1 2 1 grid.39382.33 0000 0001 2160 926X Center for Neuroscience and Artificial Intelligence, Baylor College of Medicine, 
13	Houston, TX USA 2 grid.39382.33 0000 0001 2160 926X Department of Neuroscience, Baylor College of Medicine, Houston, TX USA 3 grid.10392.39 0000 0001 2190 1447 Institute for Ophthalmic Research, 
14	University of Tübingen, Tübingen, Germany 4 grid.4372.2 0000 0001 2105 1091 International Max Planck Research School for Intelligent Systems, Tübingen, Germany 5 grid.266102.1 0000 0001 2297 6811 
15	Department of Pathology, University of California San Francisco, San Francisco, CA USA 6 grid.4714.6 0000 0004 1937 0626 Department of Cell and Molecular Biology, Karolinska Institutet, Stockholm, 
16	Sweden 7 gr
[... 220 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 237,
 "limit": 240
}
```

```
237	camera lucida system (MicroBrightField). We aimed to reconstruct all cells that had staining of sufficient quality (axons and dendrites for the inhibitory neurons; only dendrites for the excitatory 
238	neurons), and obtained 646 reconstructions in total. In addition, we reconstructed the dendrites of 30 neurons from the Vip and Scng subclasses that lacked sufficient axonal staining. Vip neurons are 
239	traditionally classified on the basis of dendritic morphology, so these reconstructions can inform t-type characterizations. These additional 30 reconstructions are shown, together with the main 646 
240	reconstructions, in Supplementary File 1 . Forty-five sequenced cells were mistakenly recorded using a solution with a much smaller concentration of biocytin, and their morphologies could not be 
241	recovered. We made sure that the measured electrophysiological properties of these cells were not systematically different from those of the the other sequenced cells. Inevitably, neuronal structures 
242	can be severed as a result of the slicing procedure. We took special care to exclude reconstructions of all neurons that showed any signs of damage, lack of contrast, or poor overall staining. 
243	Consistently with previous studies, tissue shrinkage due to the fixation and staining procedures was about 10–20% 5 , 28 , 49 . This shrinkage was not compensated for in our analysis. Cortical 
244	thickness normalization and layer assignment Nissl-stained slices ( n = 15 from two wild-type adult mice) were used to measure normalized layer boundaries in MOp. The Nissl staining protocol was 
245	adapted from ref. 50 . In brief, brain slices were mounted on slides and allowed to dry. The sections were then demyelinated, stained with 0.1% cresyl violet-acetate (C5042, Sigma) for 30 min at 
246	60 °C and further destained. The sections were then coverslipped in Cytoseal 60 (Richard Allan Scientific). For each slice we measured total thickness from pia to white matter and the
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 477,
 "limit": 300
}
```

```
477	change much, and the relative differences between t-types stayed the same. i , Overlay of the L5 Sst cells over the reference t-SNE embedding, coloured by rebound, as in Fig. 4b . The inset shows the 
478	correlation between transcriptomic distances and electrophysiological differences between all pairs of Sst t-types (only for t-types with at least 5 cells, and excluding Sst Chodl ), together with 
479	its p -value. j , The same analysis as in (c) but using the experiments performed at physiological temperature. No corrections for multiple comparisons were applied. Extended Data Fig. 7 
480	Transcriptomic and electrophysiological distances within individual families. a , b , Pooled within-family analysis. The same analysis as in Fig. 4c but showing within-family as well as 
481	between-family pairs of t-types. Using a cutoff of at least 10 neurons per t-type (a) and a cutoff of at least 5 neurons per t-type (b). c – n , Transcriptomic and electrophysiological distances 
482	within individual families. Only t-types with ≥ 5 neurons are used for this analysis (used t-types are listed in the second column). Transcriptomically well-isolated Sst Chodl and Pvalb Vipr2_2 were 
483	excluded. Three electrophysiological features with the highest correlation to the transcriptomic distance are shown on the right, for each family. Extended Data Fig. 8 Phenotypic variability of 
484	individual t-types. The extended version of Fig. 5 . a , Confusion matrices for classifying cells from each t-type into seven transcriptomic families, using electrophysiological, morphological, and 
485	combined features. Only t-types with at least 10 cells are shown. For morphological and combined features we only took cells from one cortical layer. Values in each column sum to 1. Arrows mark 
486	t-types that are classified into wrong families more often than 25% of the time. We used kNN-based classifier with k = 10. b , Normalized total variance of features in each t-type. Higher values 
487	c
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "000008" --include=*.yaml --include=*.json --include=*.md --include=*.csv . 2>/dev/null | grep -v "^./transcripts" | head -20; cat docs/archives.md | head -60
```

```
./targets/dandisets.json:151:   "dandiset": "000008",
./papers/manifest.yaml:39:  000008:
./attempts/000035-scala-2021-01.yaml:37:    but no gene counts. The main data set's recordings are in dandiset 000008, its sequencing data
./attempts/000035-scala-2021-01.yaml:43:    counts and none of the main data set's cells; they are in dandiset 000008 and at NeMO and GEO.
./attempts/000035-scala-2021-01.yaml:51:  notes: Needs the main data set's cells, which are in dandiset 000008. The same classifier was run
./attempts/000035-scala-2021-01.yaml:62:  notes: Needs the main data set's cells (dandiset 000008) and the reference 10x expression data.
./attempts/000035-scala-2021-01.yaml:67:    dandiset 000008) and the reference 10x expression data.
./attempts/000035-scala-2021-01.yaml:71:  notes: Needs the main data set's cells, in dandiset 000008. The t-types named in the claim are
./attempts/000035-scala-2021-01.yaml:76:  notes: Needs the main data set's cells, in dandiset 000008.
./attempts/000035-scala-2021-01.yaml:180:  - The room-temperature side uses the paper's published features of dandiset 000008's cells, not
./docs/pilot-notes.md:611:000008, which names the same paper; 000035's description still speaks of
./docs/pilot-notes.md:613:as `data_missing` and could be tested on 000008. Voltage and current are
./entries/000035-scala-2021/README.md:7:recorded at room temperature, is in dandiset 000008 and is not tested here.
./entries/000035-scala-2021/entry.yaml:11:  000008 and are not tested here.
./claims/000035/10.1038-s41586-020-2907-3.yaml:8:# of 1,329 cells recorded at room temperature is in dandiset 000008, and the sequencing data and
# Archives

The registry tests papers against data in public archives. So far it reads one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,170p targets/dandisets.json; sed -n 600,625p docs/pilot-notes.md; cat claims/000035/10.1038-s41586-020-2907-3.yaml
```

```
{
     "doi": "10.1038/s41586-018-0633-x",
     "title": "A cortico-cerebellar loop for motor planning",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000008",
   "name": "Phenotypic variation within and across transcriptomic cell types in mouse motor cortex",
   "published_version": "0.211014.0809",
   "asset_count": 1328,
   "size_gb": 11.92,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
[... 332 more lines not kept]
```

**Agent**

The paper text has the main text, Methods and Extended Data legends. Now I'll read the paper's code (berenslab/mini-atlas).

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/berenslab/mini-atlas.git && cd mini-atlas && git log -1 --format='%H %cd' && ls -R | head -80
```

```
3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9 Mon Oct 4 10:44:59 2021 +0200
.:
README.md
code
cover.png
data
figures

./code:
allen-data-preprocess.ipynb
ephys_extractor.py
ephys_features.py
extract-morphometric-features.ipynb
families.ipynb
flagship-figure.ipynb
patch-seq-data-load.ipynb
phenotype-tsne.ipynb
physiological-temperature.ipynb
plot-ephys-features.ipynb
plot-them-all.ipynb
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/code && cat ../README.md | head -60; for f in *.ipynb; do echo "== $f $(python -c "import json;nb=json.load(open('$f'));print(sum(len(''.join(c['source'])) for c in nb['cells'] if c['cell_type']=='code'))")"; done
```

```
# Phenotypic variation of transcriptomic cell types in&nbsp;mouse&nbsp;motor&nbsp;cortex
![patch-seq coverage](cover.png)
https://www.nature.com/articles/s41586-020-2907-3

*Federico Scala\*, Dmitry Kobak\*, Matteo Bernabucci, Yves Bernaerts, Cathryn René Cadwell, Jesus Ramon Castro, Leonard Hartmanis, Xiaolong Jiang, Sophie Laturnus, Elanine Miranda, Shalaka Mulherkar, Zheng Huan Tan, Zizhen Yao, Hongkui Zeng, Rickard Sandberg, Philipp Berens & Andreas S. Tolias. Nature (2020)*

This repository contains the analysis code and the preprocessed data for the above manuscript. 

------------

## Preprocessed data and meta data

All meta data and preprocessed data are located in the `data/` folder. This includes exonic and intronic gene counts, extracted electrophysiological features, extracted morphological features and z-profiles. There are two separate datasets: the main dataset recorded at room temperature and the follow-up dataset recorded at physiological temperature (files with `phys_temp` in the filenames).

## Downloading the raw data

* Raw morphological reconstructions in SWC format can be downloaded from [https://download.brainimagelibrary.org/3a/88/3a88a7687ab66069/](https://download.brainimagelibrary.org/3a/88/3a88a7687ab66069/). Download three folders (`excitatory`, `inhibitory`, and `vip_dendrites_only`) and put them into `data/raw/morph/`. These files are needed to create figures that show morphological reconstructions. Extracted morphological features are provided in `data/m1_patchseq_morph_features.csv` and `data/m1_patchseq_morph_zprofiles.csv`.

* Raw electrophysiological traces in NWB format can be downloaded from https://dandiarchive.org/dandiset/000008/ and https://dandiarchive.org/dandiset/000035 (physiological temperature experiments). Download all folders (using `dandi` command line tool as described there) and put them into `data/raw/ephys/` and `data/raw/ephys_phys/` respectively. These files are needed to create figures that illustrate the e
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/code && mkdir -p ../py && for f in *.ipynb; do python -c "
import json,sys;nb=json.load(open('$f'))
out=[]
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': out.append('# ---- cell %d\n'%i+''.join(c['source']))
    else: out.append('# MD: '+''.join(c['source']).replace('\n','\n# MD: '))
open('../py/${f%.ipynb}.py','w').write('\n\n'.join(out))
"; done; cat ../py/patch-seq-data-load.py
```

```
# MD: # Load and pickle Patch-seq data

# ---- cell 1
%matplotlib notebook

import numpy as np
import pylab as plt
import seaborn as sns
import pandas as pd
import matplotlib
import pickle
import scipy
import time
import warnings

sns.set_style('ticks')

# ---- cell 2
# META DATA

[... 277 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 1,400p phenotype-tsne.py | cut -c1-220
```

```
# MD: # Phenotype t-SNEs + t-type variability

# ---- cell 1
# Prepare

%matplotlib notebook

import numpy as np
import pylab as plt
import seaborn as sns; sns.set()
import pandas as pd
import matplotlib
import pickle
import scipy
import time
import warnings

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -n "KNeighbors\|kNN\|knn\|n_neighbors\|KMeans\|confusion\|variance\|leiden\|def \|families\|exclude" phenotype-tsne.py | cut -c1-200 | sed -n 1,200p
```

```
23:def sns_styleset():
43:def coverageEllipse(data, coverage=.8, edgecolor=None, facecolor='none', linewidth=1, 
49:        from sklearn.covariance import MinCovDet
52:        Sigma = mcd.covariance_
79:                                         depth thickness ephys ephysNames exclude \
104:cols[m1.exclude!=''] = '#aaaaaa'
129:features_exclude = ['Afterdepolarization (mV)', 'AP Fano factor', 'ISI Fano factor', 
141:X = X[:, ~np.isin(m1.ephysNames, features_exclude)]
143:keepcells = ~np.isnan(np.sum(X, axis=1)) # & ~badeph # & (m1.exclude=='')
173:print(np.sum(keepcells & (ttypes['type']!='') & (m1.exclude=='')))
181:                (m1.exclude[usedcells[typ]] == '')
201:quantified &= (m1.exclude == '')
277:                (m1.exclude[usedcells[typ]] == '')
314:                (m1.exclude[usedcells[typ]] == '')
400:def plot_tsne(ax, typ, colors=None, legend=False, ellipses=True):
409:                (m1.exclude[usedcells[typ]] == '')
504:# MD: ## Family confusion matrices
509:def get_family_confusion(mode, k=10):
514:    nbrs = NearestNeighbors(n_neighbors=k).fit(X)
532:def plot_family_confusion(ax, mode, labelfontsize=None, yticklabels=True):
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 504,532p phenotype-tsne.py; sed -n 679,720p phenotype-tsne.py; sed -n 982,1050p phenotype-tsne.py
```

```
# MD: ## Family confusion matrices

# ---- cell 27
from sklearn.neighbors import NearestNeighbors

def get_family_confusion(mode, k=10):
    X = tsnedata[mode][usedcells[mode]]
    labels = ttypes['type'][usedcells[mode]]
    classlabels = ttypes['family'][usedcells[mode]]
    
    nbrs = NearestNeighbors(n_neighbors=k).fit(X)
    distances, indices = nbrs.kneighbors()

    classes = np.array(['Lamp5', 'Vip', 'Sst', 'Pvalb', 'IT', 'ET', 'CT'])
    C = np.zeros((classes.size, classes.size))

    for i, cl in enumerate(classes):
        num = 0
        for ind in np.where(classlabels==cl)[0]:
            u, count = np.unique(classlabels[indices[ind,:]], return_counts=True)
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -v "^\s*#\|plt\.\|ax\.\|sns\." families.py | cut -c1-200 | sed -n 1,330p
```

```
%matplotlib notebook

import numpy as np
import pylab as plt
import seaborn as sns
import pandas as pd
import matplotlib
import pickle
import scipy
import time
import warnings

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import rnaseqTools

def sns_styleset():
    matplotlib.rcParams['axes.linewidth']    = .5
    matplotlib.rcParams['xtick.major.width'] = .5
[... 309 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -n "pearsonr\|spearmanr\|Dfam\|within\|n=\|print" families.py | cut -c1-220 | head -60; grep -v "^\s*#\|plt\.\|ax\.\|sns\." families.py | cut -c1-200 | sed -n 330,420p
```

```
130:print('Found {} .SWC files'.format(len(swcfiles)))
134:        print('SWC not found: ' + m1.cells[i])
137:        print('Not in the spreadsheet: ' + c + '\n' + swcfiles[c] + '')
139:        print('Not marked as traced: ' + c)
221:print(np.sum(haveinfo), 't-types quantified')
230:Dfam = pdist(families[haveinfo][:,np.newaxis])
234:plt.scatter(Dt[Dfam==0],Dph[Dfam==0], s=2, c='k', zorder=2)
235:plt.scatter(Dt[Dfam>0], Dph[Dfam>0], s=2, c='#aaaaaa')
236:plt.legend(['Within-family pairs (n={})'.format(np.sum(Dfam==0)), 
237:            'Between-family pairs (n={})'.format(np.sum(Dfam>0))],
240:plt.text(.7, 7.3, 'Within-family: $r={:.2f}$'.format(np.corrcoef(Dt[Dfam==0],Dph[Dfam==0])[0,1]))
241:plt.text(.7, 8.0, 'Between-family: $r={:.2f}$'.format(np.corrcoef(Dt[Dfam>0],Dph[Dfam>0])[0,1]))
255:print(np.sum(haveinfo), 't-types quantified')
258:Dfam = pdist(families[haveinfo][:,np.newaxis])
261:plt.scatter(Dt[Dfam==0],Dph[Dfam==0], s=2, c='k', zorder=2)
262:plt.scatter(Dt[Dfam>0], Dph[Dfam>0], s=2, c='#aaaaaa')
263:plt.legend(['Within-family pairs (n={})'.format(np.sum(Dfam==0)), 
264:            'Between-family pairs (n={})'.format(np.sum(Dfam>0))],
267:plt.text(.75, 7.3, 'Within-family: $r={:.2f}$'.format(np.corrcoef(Dt[Dfam==0],Dph[Dfam==0])[0,1]))
268:plt.text(.75, 8.0, 'Between-family: $r={:.2f}$'.format(np.corrcoef(Dt[Dfam>0],Dph[Dfam>0])[0,1]))
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 425,472p families.py | cut -c1-200; grep -n "MD:" families.py | head -30
```

```
selection = (ttypes['type']!='') & (m1.exclude=='') & ~np.isnan(np.sum(ephysTransformed,axis=1)) &\
            (ttypes['type'] != 'Sst Chodl') & (ttypes['type'] != 'Pvalb Vipr2_2')

meanTypePhenotype = np.zeros((clusterN, ephysTransformed.shape[1])) * np.nan

for c in range(clusterN):
    ind = selection & (ttypes['type'] == clusterNames[c])
    if np.sum(ind) >= 5:
        meanTypePhenotype[c,:] = np.mean(ephysTransformed[ind,:], axis=0)

m1data = pickle.load(open('../data/processed/reduced-allen-data/10X_cells_v2_AIBS.pickle', 'rb'))
meanTypeRNA = np.zeros((clusterN, m1data['neurons']['counts'].shape[1])) * np.nan

for c in range(clusterN):
    ind = m1data['neurons']['clusters'] == c
    if np.sum(ind) >= 10:
        meanTypeRNA[c,:] = np.mean(np.log1p(m1data['neurons']['counts'][ind,:]), axis=0)
        
haveinfo = ~np.isnan(meanTypePhenotype[:,0])
print(np.sum(haveinfo), 't-types quantified')
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -v "^\s*#\|plt\.\|ax\.\|sns\.\|matplotlib.rc" reduced-rank-regression.py | cut -c1-200 | sed -n 1,200p
```

```
%matplotlib notebook

import numpy as np
import pylab as plt
import pandas as pd
import matplotlib
import pickle
import scipy
import time
import warnings

import rnaseqTools

import sparseRRR

def sns_styleset():

sns_styleset()

from collections import namedtuple
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -v "^\s*#\|plt\.\|ax\.\|sns\.\|matplotlib.rc" reduced-rank-regression.py | cut -c1-200 | sed -n 200,330p; grep -n "def elastic_rrr_cv" -A60 ../code/sparseRRR.py | head -90
```

```
print('R2: {:.2f}, corrs: {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(
    np.mean(r2_relaxed), *np.mean(corrs_relaxed,axis=0).squeeze()))

%%time

lambdas = np.concatenate((np.arange(.2,1.01,.1), np.arange(2,7)))
alphas = np.array([.5, .75, 1])

cvresults = sparseRRR.elastic_rrr_cv(X, Y, rank=5, reps=1, folds=10, alphas=alphas, lambdas=lambdas)

lambdas = np.arange(.2,1,.1)
alphas = np.array([1])
ranks = np.arange(1, Y.shape[1]+1)

cvresults_rank = {}
for r in ranks:
    cvresults_rank[r] = sparseRRR.elastic_rrr_cv(X, Y, rank=r, reps=1, folds=10, alphas=alphas, lambdas=lambdas)
    
pickle.dump([cvresults, cvresults_rank], open('../data/processed/rnaseq/cvresults.pickle', 'wb'))

[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -v "^\s*#\|plt\.\|ax\.\|sns\.\|matplotlib.rc" preprocess-ephys-files.py | cut -c1-200 | sed -n 1,260p
```

```
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.io as io
import scipy.signal as signal
from scipy.optimize import curve_fit
from scipy import integrate
import logging
import importlib
import os
import warnings

from pynwb import NWBHDF5IO

import ephys_extractor as efex
import ephys_features as ft

import matplotlib as mpl
[... 241 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -v "^\s*#\|plt\.\|ax\.\|sns\.\|matplotlib.rc" preprocess-ephys-files.py | cut -c1-200 | grep -n "to_csv\|for .* in .*M1_nwb\|cell id\|sample\|except\|curr_index_0\b" | head -40
```

```
36:    curr_index_0 = int(-current_initial/20) # index of zero current stimulation
39:    for i in range(curr_index_0):   # Find all voltage traces from minimum to 0 current stimulation
41:    for i in range(curr_index_0, int((df.shape[0]+1)/2)-1):   # Find all voltage traces from 0 to highest current stimulation
43:    voltage[:, curr_index_0] = df.loc[curr_index_0*2][0][0].data[:]    # Find voltage trace for 0 current stimulation
44:    return time, voltage, current, curr_index_0
48:fpath = '../data/raw/ephys_phys/000035/sub-mouse-KIYRP/sub-mouse-KIYRP_ses-20200403-sample-10_slice-20200403-slice-3_cell-20200403-sample-10_icephys.nwb'
52:time, voltage, current, curr_index_0 = get_time_voltage_current_currindex0(nwb)
53:print('time: ', time, '\nvoltage: ', voltage, '\ncurrent: ', current, '\ncurr_index_0: ', curr_index_0)
167:                except TypeError: # Probably a noisy bump for this trace, just keep it to be np.nan
237:def get_cell_features(df, df_related_features, time, current, voltage, curr_index_0, \
252:    curr_index_0 : integer of current index where the current = 0 pA
264:    Rm_array = df_related_features['resting_membrane_potential'][:curr_index_0].dropna().values
265:    Ri_array = df_related_features['input_resistance'][:curr_index_0].dropna().values
510:Cell_Features = get_cell_features(df, df_related_features, time, current, voltage, curr_index_0)
519:    names_nwb : tuple of names of the samples
528:        time, voltage, current, curr_index_0 = get_time_voltage_current_currindex0(data)
533:        Cell_Features = get_cell_features(df, df_related_features, time, current, voltage, curr_index_0)
535:    All_Cells_Features.insert(0, 'name sample', names_nwb)
540:All_Cells_Features_M1_phys['cell id']=[g.split('cell-')[-1][:-12].replace('-', '_') for g in \
541:                                       All_Cells_Features_M1_phys['name sample']]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/data && head -1 m1_patchseq_meta_data.csv | tr '\t' '\n'; wc -l m1_patchseq_meta_data.csv m1_patchseq_ephys_features.csv; head -1 m1_patchseq_ephys_features.csv; cut -f$(head -1 m1_patchseq_meta_data.csv | tr '\t' '\n' | grep -n "Exclusion" | cut -d: -f1) m1_patchseq_meta_data.csv | sort | uniq -c; grep -n "family\|'type'\]" ../py/ttype-assignment.py | head -30
```

```
Number
Cell
Slice
Date
Sample
Mouse
Mouse date of birth
Mouse age
Mouse gender
Mouse genotype
Targeted layer
Inferred layer
Cre
Exon reads
Intron reads
Intergenic reads
Sequencing batch
Number of genes detected
RNA family
RNA type
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 236,262p ttype-assignment.py
```

```
else:
                ass, ass_boot, Cmeans = rnaseqTools.map_to_clusters(
                m1data[referenceKey]['counts'], m1data[referenceKey]['genes'],
                counts[subset,:], genes, m1data[referenceKey]['clusters'], 
                bootstrap=True, returnCmeans=True, seed=42, totalClusters=K)
        
            results['m1ass'][dataset][subset] = ass
            results['m1corrs'][dataset][subset,:] = Cmeans
            results['m1boot'][dataset][subset,:] = ass_boot
        
    results['m1consensus_boot'] = np.zeros((n, K))
    for dataset in results['m1boot']:
        results['m1consensus_boot'] += results['m1boot'][dataset]
    results['m1consensus_boot'] /= len(results['m1boot'])

    results['m1consensus_ass'] = np.zeros(n) * np.nan
    mapped = np.sum(~np.isnan(results['m1consensus_boot']), axis=1) > 0
    results['m1consensus_ass'][mapped] = np.argmax(results['m1consensus_boot'][mapped,:], axis=1)
    
    # Final type and family
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; ls schemas 2>/dev/null; grep -rn "statistic:" claims/ | head -5
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

[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; sed -n 240,256p claims/000003/10.1016-j.neuron.2016.12.011.yaml
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
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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
cd $TMPDIR/mini-atlas/py && grep -n "sample\|savefig" preprocess-ephys-files.py | grep -v "name sample" | head -30
```

```
56:fpath = '../data/raw/ephys_phys/000035/sub-mouse-KIYRP/sub-mouse-KIYRP_ses-20200403-sample-10_slice-20200403-slice-3_cell-20200403-sample-10_icephys.nwb'
73:# MD: As another means of example in this notebook we have selected samples here from a particular mouse_id. These are samples measured at physiological temperature. They can be loaded here. Go back a folder to load all of it and produce a file worked with for further analysis.
99:# MD: Same for the following mouse_id, these are samples measured at 25 degree Celcius. Go back a folder to load all of it (takes ~10s of minutes). If you load all of it, you can produce final outputs used for further experimental analysis (see further).
629:    names_nwb : tuple of names of the samples
721:    names : tuple of names of the samples
733:        plt.savefig('{}{}.png'.format(directory, name.split('/')[-1].split('.')[0]), bbox_inches = 'tight', \
835:    names : tuple of names of the samples
852:        plt.savefig('{}png files/{}.png'.format(directory, name), bbox_inches = 'tight', \
854:        plt.savefig('{}pdf files/{}.pdf'.format(directory, name), bbox_inches = 'tight', \
865:    names : tuple of names of the samples
901:        plt.savefig('{}/{}.png'.format(directory, cellType_Labels[c]), dpi = 200)
910:    names : tuple of names of the samples
989:mat = three_traces['20200403_sample_1']
1101:    names : tuple of names of the samples
1122:        plt.savefig('{}{}.png'.format(directory, name.split('/')[-1].split('.')[0]), bbox_inches = 'tight', \
1283:    names : tuple of names of the samples
1303:        plt.savefig('{}{}.png'.format(directory, name.split('/')[-1].split('.')[0]), bbox_inches = 'tight', \
1644:fpath = '../data/raw/ephys/000008/sub-mouse-ZWZEZ/sub-mouse-ZWZEZ_ses-20181112-sample-11_slice-20181112-slice-7_cell-20181112-sample-11_icephys.nwb'
1659:plt.savefig('../figures/suppfigures/sanity_check_plot.png', dpi = 200, bbox_inches = 'tight', pad_inches = 0.5)
1660:plt.savefig('../figures/suppfigures
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/data && grep "^20181112_sample_11," m1_patchseq_ephys_features.csv | tr ',' '\n' | paste <(head -1 m1_patchseq_ephys_features.csv | tr ',' '\n') -; sed -n 1640,1660p ../py/preprocess-ephys-files.py
```

```
cell id	20181112_sample_11
AP Fano factor	1.3196612087634263
AP amplitude (mV)	81.17250725626945
AP amplitude adaptation index	0.9100978859152018
AP amplitude average adaptation index	0.9852649888951576
AP coefficient of variation	0.16690784643936457
AP threshold (mV)	-43.18395256996155
AP width (ms)	0.7999999999999952
Afterdepolarization (mV)	0.0
Afterhyperpolarization (mV)	-12.601051479578018
Burstiness	0.0
ISI Fano factor	0.0013561075771210216
ISI adaptation index	1.2583586626139853
ISI average adaptation index	1.1509087561557114
ISI coefficient of variation	0.26872417437377566
Input resistance (MOhm)	274.8041082868973
Latency (ms)	69.28
Latency @ +20pA current (ms)	43.800000000000004
Max number of APs	32
Membrane time constant (ms)	21.9532930304586
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -n "pdist\|pearsonr\|Chodl\|>= 5\|Rebound\|ourLayers\[" physiological-temperature.py | head -40
```

```
358:        if (np.sum(ind) >= 5) & (np.sum(ind34) >=5):
372:               'Input resistance (MOhm)', 'Rebound (mV)', 'Sag ratio']
384:        if (np.sum(ind) >= 5) & (np.sum(ind34) >= 5):
432:                    'Rebound number of APs']
436:            (ttypes['type'] != 'Sst Chodl')
448:col = m1.ephys[selection,:][:, m1.ephysNames=='Rebound (mV)'].squeeze()
463:# plt.colorbar(label='Rebound (mV)', orientation='horizontal', cax=ax_sst_cbr, ticks=[0,10,20,30]);
468:            (ttypes34['type'] != 'Sst Chodl')
477:col = m1_34.ephys[selection,:][:, m1.ephysNames=='Rebound (mV)'].squeeze()
492:plt.colorbar(label='Rebound (mV)', orientation='horizontal', cax=ax_cbr, ticks=[0,10,20,30]);
499:            (ttypes['type'] != 'Sst Chodl')
513:from scipy.spatial.distance import pdist
519:    if np.sum(ind) >= 5:
532:Dt = pdist(meanTypeRNA[haveinfo,:], metric='correlation')
533:Dph = pdist(meanTypePhenotype[haveinfo,:])
537:r,p = scipy.stats.pearsonr(Dt,Dph)
551:            (ttypes34['type'] != 'Sst Chodl')
566:    if np.sum(ind) >= 5:
572:Dt = pdist(meanTypeRNA[haveinfo,:], metric='correlation')
573:Dph = pdist(meanTypePhenotype[haveinfo,:])
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 425,445p physiological-temperature.py; sed -n 495,540p physiological-temperature.py; sed -n 600,640p physiological-temperature.py
```

```
fig.text(.52, .4, 'j', fontsize=8, fontweight='bold', va='top');

# ---- cell 17
ephys_features_exclude = ['Afterdepolarization (mV)', 'AP Fano factor', 'ISI Fano factor', 
                    'Latency @ +20pA current (ms)', 'Wildness', 'Spike frequency adaptation',
                    'Sag area (mV*s)', 'Sag time (s)', 'Burstiness',
                    'AP amplitude average adaptation index', 'ISI average adaptation index',
                    'Rebound number of APs']

selection = (layers=='5') & (ttypes['family']=='Sst') & (m1.exclude=='') & \
            ~np.isnan(np.sum(m1.ephys[:, ~np.isin(m1.ephysNames, ephys_features_exclude)], axis=1)) & \
            (ttypes['type'] != 'Sst Chodl')
family = 'pvsst'
print(np.sum(selection))

Z = pickle.load(open('../data/processed/rnaseq/10x-tsne-' + family + '.pickle', 'rb'))
m1data = pickle.load(open('../data/processed/reduced-allen-data/10X_cells_v2_AIBS.pickle', 'rb'))
pos = rnaseqTools.map_to_tsne(m1data[family]['counts'], m1data[family]['genes'],
                              m1.exonCounts[selection,:], m1.genes, Z, knn=10,
                              newIntronCounts=m1.intronCounts[selection,:], 
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && grep -n "^layers\|layers = \|layers=" physiological-temperature.py | head; grep -n "1,187\|1187\|np.median\|>= 3\|>=3" ttype-coverage.py | head
```

```
58:    layers = m1.layers.copy()
124:                     layers=None, cre=None, yields=None, traced=None, depth=None, thickness=None,
352:    subset   = (ttypes['family']=='Sst') & (layers=='5') & (m1.exclude=='')
377:    subset   = (ttypes['family']=='Sst') & (layers=='5') & (m1.exclude=='')
434:selection = (layers=='5') & (ttypes['family']=='Sst') & (m1.exclude=='') & \
497:selection = (layers=='5') & (ttypes['family']=='Sst') & (m1.exclude=='') & \
603:        ps[i] = mannwhitneyu(m1.ephys[(ttypes['family']=='IT') & (layers=='5') & (m1.exclude==''), i],
604:                             m1.ephys[(ttypes['family']=='ET') & (layers=='5') & (m1.exclude==''), i])[1]
632:    subset   = (ttypes['family']=='IT') & (layers=='5') & (m1.exclude=='')
638:    subset   = (ttypes['family']=='ET') & (layers=='5') & (m1.exclude=='')
349:    if d.size >= 3:
350:        plt.plot(t + np.array([-.4,.4]), np.array([1,1]) * np.median(d),
418:    x,y = np.median(Z[ind,0]), np.median(Z[ind,1])
475:    x,y = np.median(Z[ind,0]), np.median(Z[ind,1])
547:    x,y = np.median(Z[ind,0]), np.median(Z[ind,1])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mini-atlas/py && sed -n 55,66p physiological-temperature.py; cd .. && git log --oneline | head -3
```

```
# Our layer definition
with np.errstate(invalid='ignore'):
    layers = m1.layers.copy()
    normdepth = m1.depth/m1.thickness
    layers[normdepth < 0.07] = '1'
    layers[(normdepth > 0.07) & (normdepth < 0.29)] = '2/3'
    layers[(normdepth > 0.29) & (normdepth < 0.73)] = '5'
    layers[normdepth > 0.73] = '6'

# MD: ## Load the 34C data

3bf98a5 Update README.md
11e0328 fix allen cluster annotation file
82214e9 rasterize scatter plots in the pokemon figure
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
L=d if isinstance(d,list) else d.get('dandisets',d)
for x in L:
    if x['dandiset']=='000008': print(json.dumps({k:v for k,v in x.items() if k!='papers'},indent=1)[:3000])
E
sed -n 30,50p papers/manifest.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
TypeError: string indices must be integers, not 'str'
    pdf: true
    supplements: 0
  '000007':
  - doi: 10.1038/s41586-018-0633-x
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  000008:
  - doi: 10.1038/s41586-020-2907-3
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  000009:
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000008/versions/0.211014.0809/ | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('version'))"
```

Result: the fetched text is not kept.

**Agent**

I have what I need from the paper and its code (mini-atlas at commit 3bf98a5). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000008/10.1038-s41586-020-2907-3.yaml",
 "content": "# Claims for Scala, Kobak et al. (2021), \"Phenotypic variation of transcriptomic cell types in\n# mouse motor cortex\", Nature 598:144-150, on dandiset 000008.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC8113357):\n# main text, Methods, figure legends and Extended Data figure legends. Not in the text: the\n# Extended Data Tables 1 and 2 (descriptions of the t-types), the Supplementary Files 1 to 3\n# (galleries of morphologies and traces, dot plots of all features, the list of morphometric\n# statistics) and the figures themselves. No PDF was supplied. No claim below rests on numbers\n# that are only in those items; the Extended Data figures are read from their legends only.\n#\n# Code read: https://github.com/berenslab/mini-atlas at commit\n# 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9. It holds the analysis notebooks (feature extraction\n# from the NWB files in preprocess-ephys-files.ipynb with ephys_extractor.py and\n# ephys_features.py; t-type assignment; reduced-rank regression with sparseRRR.py; the\n# t-SNEs, kNN family classifiers, normalized variances and Leiden entropies in\n# phenotype-tsne.ipynb; the distance correlations of Fig. 4 and Extended Data Fig. 7 in\n# families.ipynb; Extended Data Fig. 6 in physiological-temperature.ipynb) and the paper's\n# preprocessed data: per-cell metadata (m1_patchseq_meta_data.csv, 1,329 cells, with t-type,\n# family, soma depth, cortical thickness, Cre line, mouse, exclusion reasons), the 29\n# electrophysiological features of 1,328 cells (m1_patchseq_ephys_features.csv), exon and intron\n# counts, morphometric features and z-profiles. Choices the code fixes where the Methods are\n# silent are cited in the criteria as \"the code\".\n#\n# The data the paper used. 1,329 neurons from 266 adult mice (median age 75 days) of ten\n# genotypes (wild type and nine Cre/Ai9 lines), patched in acute coronal slices of primary motor\n# cortex at room temperature (25 degrees C). Each neuron got 600 ms current steps from -200 pA in\n# 20 pA increments up to 1,380 pA (Methods). Measured variables: the membrane voltage traces,\n# from which 29 features are extracted (17 used in all statistics); per cell, the soma depth and\n# cortical thickness (normalized soma depth, and a layer from Nissl boundaries 0.07, 0.29 and\n# 0.73; the targeted layer for the 45 cells without depth); the transcriptome (exon and intron\n# counts), from which each cell gets a t-type and a family; and for 646 cells a morphological\n# reconstruction. Families are Lamp5, Sncg, Vip, Sst, Pvalb (inhibitory) and IT, ET, NP, CT\n# (excitatory; the code puts the L6b t-types in CT).\n#\n# What is where. The dandiset is described as holding the intracellular electrophysiological\n# recordings of these neurons. The paper says sequencing data are at NeMO\n# (http://data.nemoarchive.org/biccn/grant/zeng/tolias; the code's README gives NeMO accession\n# dat-kq04hua and GEO GSE163764), reconstructions at the Brain Image Library\n# (https://download.brainimagelibrary.org/3a/88/3a88a7687ab66069/), and all preprocessed data\n# and metadata in the mini-atlas repository. Transcriptomic distances use the reference\n# single-cell 10x v2 data set of Yao et al. 2021 (doi:10.1038/s41586-021-03500-8), which the\n# code reads as a reduced pickle (10X_cells_v2_AIBS.pickle, Zenodo record 5118962, or rebuilt\n# with allen-data-preprocess.ipynb). Claims that need the per-cell t-type or family are marked\n# `dataset`, as the t-type is part of the paper's record of each recorded cell; whether the\n# files carry it, or it must come from the paper's metadata table through a link claim, is for\n# the author to find. Claims that need gene counts, the reference data or morphology are marked\n# `with_inputs` or `elsewhere`.\n#\n# Common method, from the Methods and the code, used by several criteria. \"The 17 features\":\n# the 29 extracted features less afterdepolarization, burstiness, rebound number of APs, sag\n# area, sag time, wildness, AP Fano factor, ISI Fano factor, latency at +20 pA, AP amplitude\n# average adaptation index, ISI average adaptation index and spike frequency adaptation; AP CV,\n# ISI CV, ISI adaptation index and latency log-transformed (Methods; the code's RRR notebook\n# log-transforms only the first three, named as a variant in fig2-rrr). \"The ephys\n# representation\": the 17 features standardized over all cells with all 17 defined (1,320\n# cells, excluded and unassigned cells included, as the code does), turned into all 17\n# principal components, all scaled by the standard deviation of PC1 (Methods, t-SNE\n# visualization; code phenotype-tsne.ipynb). \"Excluded cells\": the 7 cells with an exclusion\n# reason (6 with excitatory RNA but inhibitory phenotype, 1 outside MOp; Methods, t-type\n# assignment). \"Layer\": from normalized soma depth with the boundaries above, the targeted layer\n# where depth is missing (Methods, Cortical thickness normalization; code).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000008\"\npaper: doi:10.1038/s41586-020-2907-3\nclaims:\n# --- Cohort and recording protocol ----------------------------------------------------------\n- id: cohort-cells-mice\n  statement: 1,329 cells from 266 mice passed the initial quality control and were sequenced;\n    the paper's recordings come from these cells.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 1; Methods, Animals\n  quote: In total, we performed whole-cell recordings from more than 2,000 cells, of which 1,329\n    cells (from 266 mice) passed initial quality control.\n  expected:\n  - quantity: cells\n    value: 1329\n    tolerance: 0\n  - quantity: mice\n    value: 266\n    tolerance: 0\n  criterion: Counts are exact records, so the tolerance is zero. Cells are counted as distinct\n    recorded cells in the dandiset, mice as distinct subjects. The paper allows two readings of\n    the cell count for a dandiset of recordings, (a) all 1,329 cells, or (b) 1,328, leaving out\n    the one neuron whose electrophysiological recording did not pass quality control (Extended\n    Data Fig. 3 legend; the code's feature table has 1,328 cells). Reproduced when the mouse\n    count is 266 and the cell count matches either reading; partially reproduced when one of\n    the two counts matches.\n- id: cohort-ages\n  statement: The mice were 35 to 245 days old, with a median of 75 days and an interquartile\n    range of 64 to 100 days.\n  source: Methods, Animals; Extended Data Figure 2a\n  quote: Experiments on adult male and female mice ( n = 266; median age 75 days, interquartile\n    range 64–100, full range 35–245 days, Extended Data Fig. 2a )\n  expected:\n  - quantity: median age\n    value: 75\n    tolerance: 1\n    unit: days\n  - quantity: first quartile of age\n    value: 64\n    tolerance: 1\n    unit: days\n  - quantity: third quartile of age\n    value: 100\n    tolerance: 1\n    unit: days\n  - quantity: youngest mouse\n    value: 35\n    tolerance: 0\n    unit: days\n  - quantity: oldest mouse\n    value: 245\n    tolerance: 0\n    unit: days\n  criterion: Ages are records in days, so the extremes take a tolerance of zero and the median\n    and quartiles one day, for the rounding of quartiles between neighbouring values. The text\n    gives the statistics over the n = 266 mice (one age per mouse); over cells is a second\n    reading, the one the Extended Data Fig. 2a legend leaves open. Reproduced when every value\n    is within tolerance under one reading.\n- id: cohort-genotypes\n  statement: The 266 mice were wild-type C57Bl/6 (27), Viaat-Cre/Ai9 (24), Sst-Cre/Ai9 (75),\n    Vip-Cre/Ai9 (46), Pvalb-Cre/Ai9 (76), Npy-Cre/Ai9 (2), Vipr2-Cre/Ai9 (7), Slc17a8-Cre/Ai9\n    (6), Gnb4-Cre/Ai9 (1) and Slc17a8-iCre/Ai9 (2).\n  source: Methods, Animals\n  quote: were performed on wild-type C57Bl/6 ( n = 27), Viaat -Cre/Ai9 (vesicular inhibitory amino\n    acid transporter, encoded by the Slc32a1 gene, n = 24), Sst -Cre/Ai9 (somatostatin, n = 75), Vip\n    -Cre/Ai9 (vasoactive intestinal polypeptide, n = 46), Pvalb -Cre/Ai9 (parvalbumin, n = 76), Npy\n    -Cre/Ai9 (neuropeptide Y, n = 2), Vipr2 -Cre/Ai9 (vasoactive intestinal peptide receptor 2, n =\n    7), Scl17a8 -Cre/Ai9 (VGLUT3, vesicular glutamate transporter 3, n = 6), Gnb4 -Cre/Ai9 ( n = 1),\n    and Slc17a8 -iCre/Ai9 ( n = 2) mice\n  expected:\n  - quantity: wild-type mice\n    value: 27\n    tolerance: 0\n  - quantity: Viaat-Cre mice\n    value: 24\n    tolerance: 0\n  - quantity: Sst-Cre mice\n    value: 75\n    tolerance: 0\n  - quantity: Vip-Cre mice\n    value: 46\n    tolerance: 0\n  - quantity: Pvalb-Cre mice\n    value: 76\n    tolerance: 0\n  - quantity: Npy-Cre mice\n    value: 2\n    tolerance: 0\n  - quantity: Vipr2-Cre mice\n    value: 7\n    tolerance: 0\n  - quantity: Slc17a8-Cre mice\n    value: 6\n    tolerance: 0\n  - quantity: Gnb4-Cre mice\n    value: 1\n    tolerance: 0\n  - quantity: Slc17a8-iCre mice\n    value: 2\n    tolerance: 0\n  criterion: Counts of distinct subjects by genotype, from the subjects' metadata; exact records,\n    so the tolerance is zero. The paper spells the Slc17a8-Cre line \"Scl17a8\" once; the two\n    spellings are one line. Reproduced when all ten counts match; partially reproduced when the\n    total is 266 and at least eight counts match.\n- id: stimulus-protocol\n  statement: Each neuron was stimulated with 600 ms current pulses from -200 pA upwards in 20 pA\n    steps up to 1,380 pA (sometimes stopped earlier), with 1.3 or 1.4 s between pulses, and for\n    most neurons the series was repeated several times.\n  source: Methods, Patch-seq recording procedures, paragraph 4\n  quote: Each neuron was injected with 600-ms-long current pulses starting from −200 pA and up to\n    1,380 pA with 20-pA increment steps (in some cases stimulation was stopped before reaching 1,380\n    pA). There were 1.3- or 1.4-s intervals between successive current pulses, depending on the used\n    setup. For most neurons, the stimulation was then repeated multiple times from the beginning.\n  criterion: For every cell, the stimulus of each sweep is read from the file. A cell conforms\n    when every step lasts 600 ms (to within 1 ms), the first step of each series is -200 pA,\n    consecutive steps differ by 20 pA, and the largest is at most 1,380 pA. The interval\n    between pulses is taken as onset to onset, the reading the code's 0.1 s to 0.7 s stimulus\n    window within each sweep allows, or as offset to onset; both are reported, and an interval\n    conforms when it is 1.3 or 1.4 s (to within 0.05 s) under either. \"Most\" neurons repeated\n    is read as more than half of cells with a second series starting again at -200 pA.\n    Reproduced when at least 95% of cells conform on steps and intervals and more than half\n    have repeats; partially reproduced when at least 80% conform; not reproduced otherwise.\n- id: soma-depth-count\n  statement: Soma depth was measured for 1,284 of the 1,329 neurons; 45 neurons were recorded\n    with too little biocytin, and the depth could be measured for only 2 of them.\n  source: Methods, Cortical thickness normalization and layer assignment\n  quote: We obtained soma depth information for 1,284 neurons out of 1,329 (45 neurons were\n    mistakenly recorded using a solution with insufficient biocytin concentration, and we could\n    measure soma depths for only 2 of those; for 2 other neurons the measurements could not be\n    carried out because the slices were lost).\n  expected:\n    quantity: neurons with a soma depth\n    value: 1284\n    tolerance: 0\n  criterion: Count of cells with a soma depth recorded in the dandiset's metadata; an exact\n    record, so the tolerance is zero. The paper's figure counts differ (1,187 of the 1,227\n    assigned cells in Fig. 1b); only the Methods count is tested. If the dandiset holds 1,328\n    cells (see cohort-cells-mice), 1,283 is also accepted when the missing cell is one with a\n    depth.\n# --- Electrophysiological features ----------------------------------------------------------\n- id: ed4-example-cell\n  statement: The features of the example cell of Extended Data Fig. 4 are an input resistance of\n    274.80 MOhm, a membrane time constant of 21.95 ms, ISI adaptation index 1.26, ISI average\n    adaptation index 1.15, AP amplitude adaptation index 0.91 and its average 0.99, AP threshold\n    -40.18 mV, AP amplitude 81.17 mV, AP width 0.80 ms, AHP -12.60 mV, ADP 0 mV, UDR 1.62,\n    latency 69.28 ms, rheobase 20.44 pA, 32 APs in the highest firing trace, ISI CV 0.27, ISI\n    Fano factor 0.0014, AP CV 0.17, AP Fano factor 1.32, sag ratio 1.17, sag time 0.26, sag area\n    31.16 mV ms and rebound 17.84 mV.\n  source: Extended Data Figure 4a-f legend\n  quote: Hyperpolarizing currents were used to compute the input resistance (274.80 MOhm) and\n    membrane time constant tau (21.95 ms). ... It was used to compute AP threshold (−40.18 mV), AP\n    amplitude (81.17 mV), AP width (0.80 ms), AHP (−12.60 mV), ADP (0 mV), UDR (1.62) and latency of\n    the first spike (69.28 ms). d , Regression line gives the rheobase estimate (20.44 pA).\n  expected:\n  - quantity: input resistance\n    value: 274.80\n    tolerance: 27.48\n    unit: MOhm\n  - quantity: membrane time constant\n    value: 21.95\n    tolerance: 2.195\n    unit: ms\n  - quantity: ISI adaptation index\n    value: 1.26\n    tolerance: 0.126\n  - quantity: ISI average adaptation index\n    value: 1.15\n    tolerance: 0.115\n  - quantity: AP amplitude adaptation index\n    value: 0.91\n    tolerance: 0.091\n  - quantity: AP amplitude average adaptation index\n    value: 0.99\n    tolerance: 0.099\n  - quantity: AP threshold\n    value: -40.18\n    tolerance: 4.018\n    unit: mV\n  - quantity: AP amplitude\n    value: 81.17\n    tolerance: 8.117\n    unit: mV\n  - quantity: AP width\n    value: 0.80\n    tolerance: 0.08\n    unit: ms\n  - quantity: AHP\n    value: -12.60\n    tolerance: 1.26\n    unit: mV\n  - quantity: ADP\n    value: 0\n    tolerance: 0\n    unit: mV\n  - quantity: upstroke-to-downstroke ratio\n    value: 1.62\n    tolerance: 0.162\n  - quantity: latency of the first spike\n    value: 69.28\n    tolerance: 6.928\n    unit: ms\n  - quantity: rheobase\n    value: 20.44\n    tolerance: 2.044\n    unit: pA\n  - quantity: number of APs in the highest firing trace\n    value: 32\n    tolerance: 3.2\n  - quantity: ISI CV\n    value: 0.27\n    tolerance: 0.027\n  - quantity: ISI Fano factor\n    value: 0.0014\n    tolerance: 0.00014\n  - quantity: AP CV\n    value: 0.17\n    tolerance: 0.017\n  - quantity: AP Fano factor\n    value: 1.32\n    tolerance: 0.132\n  - quantity: sag ratio\n    value: 1.17\n    tolerance: 0.117\n  - quantity: sag time\n    value: 0.26\n    tolerance: 0.026\n    unit: s\n  - quantity: sag area\n    value: 31.16\n    tolerance: 3.116\n    unit: mV ms\n  - quantity: rebound\n    value: 17.84\n    tolerance: 1.784\n    unit: mV\n  criterion: The legend does not name the cell; the code does. It draws Extended Data Fig. 4 from\n    cell 20181112_sample_11 (subject mouse ZWZEZ, file ses-20181112-sample-11, slice\n    20181112-slice-7; preprocess-ephys-files.ipynb, cell 60). Features are extracted from that\n    file with the paper's code (preprocess-ephys-files.ipynb, its get_cell_features and\n    extract_spike_features with ephys_extractor.py and ephys_features.py; stimulus window 0.1\n    to 0.7 s, 10 kHz Bessel filter). Default 10% tolerance, zero for ADP. Two values in the\n    legend disagree with the code's own feature table for this cell. The AP threshold is -43.18\n    mV in the table against -40.18 mV in the legend; both readings are reported, and -43.18\n    lies inside the tolerance of -40.18. The sag time is printed \"0.26 ms\" in the legend and is\n    0.26 s in the table; it is read in seconds. Reproduced when all 23 values are within\n    tolerance; partially reproduced when at least 20 are; not reproduced otherwise.\n- id: ephys-feature-count\n  statement: All 17 features used for statistics could be computed for 1,320 cells, of which\n    1,219 had a t-type assignment.\n  source: Figure 3a legend; Methods, t-SNE visualization of the morpho-electric phenotypes\n  quote: n = 1,320 cells used to construct the embedding, 1,219 cells with t-type labels shown.\n  expected:\n  - quantity: cells with all 17 features\n    value: 1320\n    tolerance: 132\n  - quantity: of these, cells with a t-type (not excluded)\n    value: 1219\n    tolerance: 121.9\n  criterion: Features extracted from every cell's file with the paper's code, as in\n    ed4-example-cell; a cell counts when all 17 features are defined (finite after the log\n    transform). The count depends on the extraction, so it takes the default 10%. A cell has a\n    t-type when it has an assigned t-type and is not an excluded cell (code,\n    phenotype-tsne.ipynb). Reproduced when both counts are within tolerance.\n- id: fig2-family-features\n  statement: Pvalb neurons are characterized by high firing rates, while Sst neurons have high\n    hyperpolarization sag and rebound.\n  source: Results, Distinct phenotypes of major families, paragraph 2; Figure 2 (right biplots)\n  quote: 'These groups had distinct electrophysiological properties: for example, as expected,\n    Pvalb neurons were characterized by high firing rates while Sst neurons had high values of\n    the hyperpolarization sag and rebound'\n  criterion: The paper shows this in a biplot and gives no test, so the comparison is fixed from\n    its wording. Cells are those with all 17 features, a t-type and no exclusion. Firing rate is\n    the maximum number of APs in the 600 ms window (Methods); sag is the sag ratio and rebound\n    the rebound (mV). \"High\" is compared with the other families, under two readings, (a)\n    the family median is the highest of the seven families of Fig. 3d (Lamp5, Vip, Sst, Pvalb,\n    IT, ET, CT), or (b) of the four interneuron families of Fig. 2 (Pvalb, Sst, Vip, Lamp5).\n    For each comparison a two-sided Mann-Whitney test of the family against all other cells of\n    the reading's families is reported. Reproduced when, under one reading, Pvalb has the\n    highest median maximum AP count and Sst the highest median sag ratio and rebound, each with\n    p < 0.05; partially reproduced when two of the three hold.\n- id: fig3d-families-ephys\n  statement: In a k-nearest-neighbour classification of cells into seven transcriptomic families\n    from electrophysiological features, the confusion matrix is mostly diagonal, with only the\n    ET and IT subclasses strongly overlapping.\n  source: Results, Distinct phenotypes of major families, paragraph 3; Figure 3a, d\n  quote: 'We quantified this separation using a confusion matrix for k -nearest neighbours (kNN)\n    classification of cells into families: it was mostly diagonal, with only the ET and IT\n    subclasses strongly overlapping (Fig. 3d ).'\n  criterion: As the Methods (kNN classification) and the code (get_family_confusion in\n    phenotype-tsne.ipynb) do it. The ephys representation (see the opening comment); k = 10\n    nearest neighbours by Euclidean distance, the cell itself left out; neighbours drawn from\n    all 1,320 cells with features, including those with no t-type or excluded, whose label\n    counts as no family; each cell's predicted family is the most common label among its\n    neighbours (ties to the label first in alphabetical order, as numpy's unique and argmax\n    do), and a cell whose prediction is not one of the seven families is not counted. Rows are\n    Lamp5, Vip, Sst, Pvalb, IT, ET, CT (Sncg and NP not used). The paper's own threshold for\n    \"classified into wrong families\" is 25% (Fig. 5a legend). Reproduced when the ET row puts\n    at least 25% into IT or the IT row at least 25% into ET, and every other off-diagonal entry\n    is below 25%; partially reproduced when ET and IT overlap so and one or two other\n    off-diagonal entries reach 25%; not reproduced otherwise. The 34 degree follow-up of the\n    same overlap is in dandiset 000035 and not tested here.\n- id: ed6-it-et-room-features\n  statement: At room temperature, the features that differ most between layer 5 IT and ET\n    neurons by a two-sided Wilcoxon-Mann-Whitney test, after omitting the upstroke-to-downstroke\n    ratio, sag time and sag area, are the sag ratio, input resistance, AP width and rebound.\n  source: Extended Data Figure 6a-e legend; the code, physiological-temperature.ipynb, cells 22\n    and 23\n  quote: The first four panels correspond to features showing the largest IT/ET differences at\n    room temperature, according to the two-sided Wilcoxon-Mann–Whitney test statistic (and omitting\n    several features that are very correlated with the shown ones: upstroke-to-downstroke ratio,\n    sag time, and sag area).\n  criterion: The legend names the features only in the figure; the four are those the code plots\n    (featuresToShow, the first four of sag ratio, input resistance, AP width, rebound, AP\n    threshold). As in the code, layer 5 IT against layer 5 ET cells (family from the t-type,\n    layer as in the opening comment, excluded cells left out), a two-sided Mann-Whitney test for\n    each of the 29 features except rebound number of APs, ranked by p. Reproduced when, after\n    leaving out UDR, sag time and sag area, the four smallest p are those four features in any\n    order; partially reproduced when three of them are.\n# --- Transcriptomic coverage ----------------------------------------------------------------\n- id: fig1a-ttype-coverage\n  statement: After quality control 1,227 neurons had a t-type (817 inhibitory, 410 excitatory),\n    covering 77 of the 90 neuronal t-types of the reference taxonomy.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 3; Figure 1a\n  quote: leaving 1,227 neurons for further analysis (817 inhibitory, 410 excitatory; 369 and 269\n    with morphological reconstructions, respectively). The resulting data set covered 77 out of\n    the 90 neuronal t-types (Fig. 1a )\n  expected:\n  - quantity: neurons with a t-type\n    value: 1227\n    tolerance: 0\n  - quantity: inhibitory neurons with a t-type\n    value: 817\n    tolerance: 0\n  - quantity: excitatory neurons with a t-type\n    value: 410\n    tolerance: 0\n  - quantity: t-types covered\n    value: 77\n    tolerance: 0\n  criterion: Counts of the paper's t-type labels for the dandiset's cells, excluded cells left\n    out; exact records, so the tolerance is zero. Inhibitory is the Lamp5, Sncg, Vip, Sst and\n    Pvalb families, excitatory IT, ET, NP and CT (code, ttype-assignment.ipynb). Under reading\n    (b) of cohort-cells-mice, one fewer cell in one class is accepted if the dandiset lacks a\n    cell with a t-type. Reproduced when all four counts match.\n- id: fig1b-depth-layers\n  statement: Within-type distributions of soma depth agree with the layer-specific names of the\n    excitatory t-types.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 3; Figure 1b\n  quote: Within-type distributions of soma depths (Fig. 1b ) agreed well with previous data 4 and\n    with the layer-specific nomenclature of excitatory t-types, confirming the validity of our\n    t-type assignment.\n  criterion: The paper gives no measure, so it is fixed from Fig. 1b's legend. Normalized soma\n    depth (depth over cortical thickness) of cells with a t-type, excluded cells left out; for\n    each excitatory t-type with at least three cells (the legend's cut for showing medians),\n    the median depth is placed in a layer by the Nissl boundaries (L1 below 0.07, L2/3 to 0.29,\n    L5 to 0.73, L6 beyond). A t-type agrees when that layer is one its name gives (L2/3; L4/5\n    as L2/3 or L5; L5; L5/6 as L5 or L6; L6 and L6b as L6). Reproduced when all such t-types\n    agree; partially reproduced when at least 80% do.\n- id: l45-it1-boundary\n  statement: The L4/5 IT_1 t-type is located on the boundary between L2/3 and L5, and probably\n    corresponds to the quasi-L4 neurons described before in motor cortex.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 4; Figure 1b\n  quote: We were also able to identify a t-type, L4/5 IT_1, that was located on the boundary\n    between L2/3 and L5 and probably corresponds to the quasi-L4 neurons described previously in\n    motor cortex 31 .\n  criterion: Normalized soma depths of L4/5 IT_1 cells (excluded cells left out). The paper's\n    L2/3 to L5 boundary is 0.29 (Fig. 1b legend). \"On the boundary\" is read as the t-type's\n    median depth lying closer to 0.29 than to the middle of either neighbouring layer (0.18 for\n    L2/3, 0.51 for L5), that is between 0.235 and 0.40. Reproduced when it does. The\n    correspondence to quasi-L4 neurons is an interpretation and is not tested.\n# --- Within-family structure (needs the reference transcriptomes) --------------------------\n- id: fig4c-distance-correlation\n  statement: Across 200 pairs of t-types from the same family (50 t-types with at least 5\n    cells), the transcriptomic and electrophysiological distances between t-types are\n    correlated with r = 0.60.\n  source: Results, Continuous phenotypic variation, paragraph 3; Figure 4c and legend\n  quote: Pooling the pairs across all families, we found that these two distance measures were\n    correlated, with r = 0.60 (Fig. 4c , n = 200 pairs; Extended Data Fig. 7 ).\n  data: with_inputs\n  expected:\n  - quantity: Pearson r over within-family pairs\n    value: 0.60\n    tolerance: 0.06\n  - quantity: within-family pairs\n    value: 200\n    tolerance: 0\n  - quantity: t-types with at least 5 cells\n    value: 50\n    tolerance: 0\n  criterion: As the Methods (Within-family analysis) and the code (families.ipynb, cell for the\n    main figure) do it. Cells with a t-type, not excluded, with all 17 features; the 17 features\n    (four log-transformed) standardized over all cells with all features. T-types with at least\n    5 such cells; each t-type's mean feature vector; electrophysiological distance the Euclidean\n    distance between means. Transcriptomic distance is the correlation distance (one minus\n    Pearson r) between the t-types' mean log(x + 1) UMI counts in the reference single-cell 10x\n    v2 data (t-types with at least 10 reference cells), over the 1,000 most variable genes\n    across all neural types. Pairs are within-family by the code's family of each t-type name\n    (L6b counted with CT). Pearson r over within-family pairs. The Methods do not mention\n    excluding any t-type for Fig. 4c; the code leaves out Sst Chodl and Pvalb Vipr2_2. Reading\n    (a) is the code's, reading (b) keeps them; the 50 t-types and 200 pairs show which the paper\n    used. Reproduced when, under one reading, r is within tolerance; the counts are reported.\n    Needs the reference 10x v2 data (Yao et al. 2021) as the code reads them.\n- id: ed7-within-families\n  statement: The correlation between transcriptomic and electrophysiological distances is also\n    seen within several individual families and for many individual features.\n  source: Results, Continuous phenotypic variation, paragraph 3; Extended Data Figure 7c-n\n  quote: The correlation was also observed within multiple individual families and for many\n    individual electrophysiological features (Extended Data Fig. 7 ).\n  data: with_inputs\n  criterion: As the code does it (families.ipynb, the loop over families) and the Extended Data\n    Fig. 7 legend says. For each of the families Pvalb, Sst, Vip, Lamp5, IT and CT, t-types with\n    at least 5 cells, Sst Chodl and Pvalb Vipr2_2 left out; transcriptomic distance over the 500\n    most variable genes of that family's transcriptomic group in the reference 10x v2 data\n    (MGE for Pvalb and Sst, CGE for Vip and Lamp5, excitatory for IT and CT); distances as in\n    fig4c-distance-correlation; Pearson r over the family's pairs, and for each feature alone.\n    The paper gives no p or threshold. \"Multiple families\" is read as (a) at least two or (b)\n    a majority (at least four) of the six families with r > 0; \"many features\" as at least\n    half of the 17 features having r > 0 pooled over the six families' pairs. Reproduced when\n    the feature part holds and the family part holds under reading (b); partially reproduced\n    when it holds only under reading (a). Families with fewer than three t-types are reported\n    and not counted.\n- id: fig4d-it-depth\n  statement: Among IT t-types (eight with at least five cells), transcriptomic distances are\n    strongly correlated with differences in average soma depth, r = 0.70.\n  source: Results, Continuous phenotypic variation, paragraph 4; Figure 4d legend\n  quote: Transcriptomic distances between t-types were strongly correlated with the average soma\n    depth differences ( r = 0.70; Fig. 4d ).\n  data: with_inputs\n  expected:\n  - quantity: Pearson r\n    value: 0.70\n    tolerance: 0.07\n  - quantity: IT t-types with at least five cells\n    value: 8\n    tolerance: 0\n  criterion: As the code does it (families.ipynb). IT cells (family from the t-type), not\n    excluded, with a soma depth; t-types with at least 5 such cells; mean normalized soma depth\n    per t-type; depth distance the absolute difference of means; transcriptomic distance the\n    correlation distance between mean log(x + 1) counts of the reference 10x v2 data over the\n    500 most variable genes of the excitatory group (Methods, Within-family analysis); Pearson r\n    over all pairs. Reproduced when r is within tolerance.\n- id: fig4a-vip-tau\n  statement: Within the Vip subclass the membrane time constant varies continuously across the\n    transcriptomic landscape, largest near the Sncg subclass and decreasing towards Vip Gpc3.\n  source: Results, Continuous phenotypic variation, paragraph 1; Figure 4a\n  quote: For example, electrophysiological properties of the t-types within the Vip subclass\n    varied continuously across the transcriptomic landscape; the membrane time constant, for\n    instance, had its largest values close to the Sncg subclass and gradually decreased towards\n    Vip Gpc3 (Fig. 4a ).\n  data: with_inputs\n  criterion: The paper shows this as a colour overlay on the reference t-SNE and gives no\n    measure. Vip cells (family Vip, not excluded, all 17 features), positioned on the CGE\n    reference t-SNE of Fig. 1c as the Methods and code (rnaseqTools.map_to_tsne, median of the\n    10 nearest reference cells by correlation over the t-type assignment genes) do it. Two\n    readings of \"close to Sncg and decreasing towards Vip Gpc3\", both run, (a) over cells, the\n    Spearman correlation between tau and the cell's position along the line from the centroid\n    of the Sncg reference cells to the centroid of the Vip Gpc3 reference cells in the\n    embedding (projection onto that line), and (b) over Vip t-types with at least 5 cells, the\n    Spearman correlation between the t-type's median tau and its transcriptomic correlation\n    distance to the Sncg subclass mean in the 10x v2 data (500 CGE genes). Reproduced when both\n    correlations show tau falling away from Sncg (negative in (a), negative in (b) with\n    distance) with one-sided p < 0.05; when the readings disagree the claim is blocked as\n    methods_underspecified.\n- id: fig4b-sst-rebound\n  statement: In layer 5 Sst neurons (Sst Chodl excluded), morpho-electric properties vary\n    continuously across the transcriptomic landscape, neighbouring t-types having similar\n    rebound values.\n  source: Results, Continuous phenotypic variation, paragraph 2; Figure 4b; Extended Data Figure\n    6i\n  quote: Here we also found that morpho-electric properties varied continuously across the\n    transcriptomic landscape, with neighbouring t-types consistently showing similar morphologies\n    and similar rebound values (Fig. 4b ).\n  data: with_inputs\n  criterion: The electrophysiological part only. As the code's room-temperature version of the\n    Extended Data Fig. 6i inset (physiological-temperature.ipynb, cell 18), whose legend\n    describes it as the correlation between transcriptomic and electrophysiological distances\n    between Sst t-types with at least 5 cells, Sst Chodl left out. Layer 5 Sst cells, not\n    excluded, all 17 features; per-t-type mean of the standardized 17 features; Euclidean\n    distance; transcriptomic correlation distance over the 500 MGE genes of the 10x v2 data;\n    Pearson r and its p over all pairs. The legend reports a p-value without giving it in the\n    text. As a second reading named by the Results sentence, the same with the rebound alone\n    (absolute difference of t-type mean rebound). Reproduced when r > 0 with p < 0.05 under\n    the full-feature reading, the code's; the rebound-only reading is reported. The\n    morphological part is not tested (morphology is not in the dandiset).\n- id: fig4e-pvalb-axon-shape\n  statement: In layer 5 Pvalb neurons the shape of the axonal arbor changes continuously across\n    the transcriptomic landscape, from shrub-like to horizontally and vertically elongated basket\n    cells, with intermediate forms in between.\n  source: Results, Continuous phenotypic variation, paragraph 5; Figure 4e\n  quote: 'The shape of the axonal arbor showed continuous changes across the transcriptomic\n    landscape (Fig. 4e ): small shrub-like basket cells, horizontally elongated basket cells, and\n    vertically elongated classical basket cells were located in different corners of the t-SNE\n    embedding, with intermediate morphologies in between.'\n  data: elsewhere\n  where: Brain Image Library, https://download.brainimagelibrary.org/3a/88/3a88a7687ab66069/\n    (SWC reconstructions); morphometric features in mini-atlas\n    data/m1_patchseq_morph_features.csv at commit 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9\n  criterion: Shown only as a colour overlay; the paper gives no measure, so a test would be\n    chosen by an agent. Recorded for coverage; the dandiset holds no morphology.\n# --- Family separability with morphology ----------------------------------------------------\n- id: fig3d-morph-combined\n  statement: Between inhibitory families, separability is weaker with morphological features\n    than with electrophysiological ones, and it is strongest with the two combined.\n  source: Results, Distinct phenotypes of major families, paragraph 4; Figure 3b-d\n  quote: The separability between inhibitory families was weaker than with electrophysiological\n    features (Fig. 3d ). The between-family separability was strongest when we had combined\n    electrophysiological and morphological features into a joint representation (Fig. 3c, d ),\n    showing that these sets of properties are not redundant.\n  data: with_inputs\n  criterion: The three representations of the Methods (t-SNE visualization) and the code\n    (phenotype-tsne.ipynb), the kNN classifier as in fig3d-families-ephys. Morphology is the\n    paper's published morphometric features and z-profiles (mini-atlas), combined with the\n    dandiset's electrophysiology for the 628 cells with both. Separability is the mean of the\n    diagonal of the confusion matrix, over the four inhibitory families for the first part and\n    over all seven for the second (the paper names no summary; the mean diagonal is read from\n    \"mostly diagonal\"). Reproduced when the inhibitory mean is lower for morphology than for\n    electrophysiology and the seven-family mean is highest for the combined representation.\n# --- Variability of individual t-types ------------------------------------------------------\n- id: fig5a-ttypes-between-families\n  statement: Most t-types are classified into their own family from electrophysiology, but some\n    lie between two families; many Sst Pvalb Calb2 neurons are classified as Pvalb, Lamp5\n    Egln3_1 neurons have Vip- and Sst-like firing, and Vip Mybpc1 neurons often have Sst-like\n    firing.\n  source: Results, Variability in individual t-types, paragraph 1; Figure 5a and legend\n  quote: Most t-types could be unambiguously placed into the correct family (Fig. 5a ), but some\n    t-types were in between two families. For example, many Sst Pvalb Calb2 neurons were\n    classified as belonging to the Pvalb subclass on the basis of electrophysiology. ... Vip\n    Mybpc1 neurons often had Sst -like firing.\n  criterion: As the code does it (get_type_confusion in phenotype-tsne.ipynb), the classifier of\n    fig3d-families-ephys applied to the cells of each t-type with at least 10 cells (Fig. 5a\n    legend); the legend marks a t-type misclassified when more than 25% of its cells go to\n    wrong families. Parts, (i) more than half of these t-types have at most 25% wrong; (ii) Sst\n    Pvalb Calb2 has more than 25% classified as Pvalb; (iii) Lamp5 Egln3_1 has more than 25%\n    classified as Vip and Sst together; (iv) for Vip Mybpc1 more than 25% classified as Sst,\n    the t-type read as (a) any of the Vip Mybpc1 t-types with at least 10 cells or (b) all\n    Vip Mybpc1 t-types pooled. Reproduced when all four hold (iv under one reading); partially\n    reproduced when (i) and at least two others hold. A t-type below 10 cells is reported and\n    its part not judged.\n- id: fig5b-ttype-variability\n  statement: Many t-types have a normalized total variance of electrophysiological features well\n    above that of k-means clusters; some, such as Pvalb Vipr2_2 (chandelier cells), appear\n    homogeneous, while Vip Mybpc1_2 is highly variable.\n  source: Results, Variability in individual t-types, paragraphs 2 and 3; Figure 5b\n  quote: We found that many t-types had total variance substantially above the variances of the\n    k -means clusters (Fig. 5b ) ... Not all t-types showed high variability; some of them, such\n    as Pvalb Vipr2_2 (chandelier cells), appeared morpho-electrically homogeneous. By contrast,\n    Vip Mybpc1_2 was marked as having high electrophysiological variability\n  criterion: As the Methods (T-type variability analysis) and the code (get_type_variability and\n    get_cluster_variability in phenotype-tsne.ipynb) do it, in the ephys representation. For\n    each t-type with at least 10 cells, the sum of its per-dimension variances over that of all\n    1,320 cells; k-means (scikit-learn defaults, random_state 42, as the code) with K the number\n    of such t-types on their cells pooled; the band from the smallest to the largest variance\n    of clusters with at least 10 cells. \"Substantially above\" is read as above the band's top.\n    \"Many\" is read as (a) at least a quarter or (b) at least a third of the t-types. Reproduced\n    when \"many\" holds under one reading, Pvalb Vipr2_2 is not above the band (if it has at\n    least 10 cells), and Vip Mybpc1_2 is above it; partially reproduced when two of the three\n    hold.\n- id: ed8-leiden-entropy\n  statement: An alternative analysis using the entropy of Leiden cluster assignments within each\n    t-type often highlights the same t-types as variable.\n  source: Results, Variability in individual t-types, paragraph 3; Extended Data Figure 8g-l\n  quote: an alternative analysis using entropies of Leiden clustering 35 often highlighted the same\n    t-types as variable (Extended Data Fig. 8 ).\n  criterion: As the Methods and the code (phenotype-tsne.ipynb, Leiden section) do it. kNN graph\n    with k = 10 on the ephys representation, Leiden (leidenalg, RBConfigurationVertexPartition)\n    at the resolution the code sets, 100 repetitions with different seeds, each t-type with at\n    least 10 cells subsampled to 10 cells, entropy of its cluster labels; median entropy per\n    t-type. Compared with the normalized variance of fig5b-ttype-variability by Spearman\n    correlation across t-types. \"Often the same\" is read as a positive correlation with\n    one-sided p < 0.05. Reproduced when it holds.\n  depends_on:\n  - fig5b-ttype-variability\n- id: fig5c-vip-mybpc1-rebound\n  statement: Vip Mybpc1_2 neurons vary in input resistance, membrane time constant and rebound,\n    and this variability is not random; cells with low rebound lie close to the boundary with the\n    low-rebound Vip Sncg type.\n  source: Results, Variability in individual t-types, paragraph 3; Figure 5c\n  quote: 'This variability was not random: overlaying the rebound values on the t-SNE embedding\n    (Fig. 5c ) showed that cells with low rebound were located close to the boundary with the\n    low-rebound Vip Sncg type.'\n  data: with_inputs\n  criterion: Shown as a colour overlay, without a measure. Vip Mybpc1_2 cells (not excluded, all\n    17 features), positioned on the CGE reference t-SNE as in fig4a-vip-tau. Two readings of\n    \"close to the boundary with Vip Sncg\", (a) the cell's distance in the embedding to the\n    nearest reference cell of Vip Sncg, (b) the cell's Pearson correlation with the Vip Sncg\n    mean expression of the 10x v2 data over the CGE assignment genes (higher is closer).\n    Reproduced when, under both readings, rebound rises with distance from Vip Sncg (Spearman,\n    one-sided p < 0.05), and the Vip Sncg median rebound is below the Vip Mybpc1_2 median; when\n    the readings disagree, methods_underspecified.\n- id: fig5d-sst-pvalb-calb2-firing\n  statement: Sst Pvalb Calb2 cells vary widely in maximum firing rate, but high-firing cells are\n    mostly grouped in one part of the transcriptomic landscape.\n  source: Results, Variability in individual t-types, paragraph 3; Figure 5d\n  quote: Similarly, Sst Pvalb Calb2 cells had high variability in terms of the maximum firing rate,\n    but high-firing cells were mostly grouped in one part of the transcriptomic landscape (Fig. 5d\n    ).\n  data: with_inputs\n  criterion: Shown as a colour overlay, without a measure. Sst Pvalb Calb2 cells (not excluded,\n    all 17 features), positioned on the MGE reference t-SNE of Fig. 1d as in fig4a-vip-tau;\n    firing rate the maximum number of APs. Two readings of \"grouped in one part\", (a) the\n    Spearman correlation between maximum AP count and the cell's position along the line from\n    the Sst reference centroid to the Pvalb reference centroid, positive, and (b) cells above\n    the t-type's median firing having a smaller mean pairwise embedding distance among\n    themselves than random halves of the t-type (1,000 permutations, one-sided p < 0.05).\n    Reproduced when both hold; when the readings disagree, methods_underspecified.\n# --- Sequencing and transcriptomic quality (not in the dandiset) ----------------------------\n- id: rnaseq-depth\n  statement: The 1,329 sequenced cells had median 1.3 million exonic and 0.7 million intronic\n    reads (log10 mean 6.0 and 5.6) and 9,100 detected genes on average (s.d. 3,500).\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 1; Extended Data Figure 2\n  quote: The mRNA of these 1,329 cells was sequenced, yielding on average 1.3 million exonic and\n    0.7 million intronic reads (medians; mean ± s.d. on a log 10 scale; 6.0 ± 0.6 and 5.6 ± 0.8,\n    respectively) and 9,100 ± 3,500 (mean ± s.d.) detected genes per cell\n  data: elsewhere\n  where: GEO GSE163764 (also NeMO dat-kq04hua); count tables in mini-atlas data/ at commit\n    3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9\n  expected:\n  - quantity: median exonic reads\n    value: 1300000\n    tolerance: 130000\n  - quantity: median intronic reads\n    value: 700000\n    tolerance: 70000\n  - quantity: mean detected genes\n    value: 9100\n    tolerance: 910\n- id: ttype-qc-counts\n  statement: In the first round of mapping, 78 cells had a highest correlation below 0.4, 14\n    mapped to non-neural types and 5 were ambiguous between large groups, leaving 1,232 cells;\n    four with excitatory RNA but inhibitory phenotype and one outside MOp were excluded, leaving\n    1,227.\n  source: Methods, t-Type assignment, paragraphs 1 and 3\n  quote: 'cells with the highest correlation below 0.4 (78 cells); cells that would be assigned to\n    non-neural t-types, presumably owing to RNA contamination 51 (14 cells; see also Extended Data\n    Fig. 2j–n ); cells with the highest correlation less than 0.02 above the maximal correlation in\n    one of the other two large transcriptomic groups (5 cells). The remaining 1,232 cells passed\n    quality control'\n  data: elsewhere\n  where: GEO GSE163764 (also NeMO dat-kq04hua); count tables in mini-atlas data/ at commit\n    3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9; reference Smart-seq2 data of Tasic et al. 2018\n  expected:\n  - quantity: cells with highest correlation below 0.4\n    value: 78\n    tolerance: 7.8\n  - quantity: cells assigned to non-neural types\n    value: 14\n    tolerance: 1.4\n  - quantity: ambiguous cells\n    value: 5\n    tolerance: 0.5\n  - quantity: cells passing quality control\n    value: 1232\n    tolerance: 123.2\n  criterion: Default 10% tolerances, as the counts depend on the mapping. The code's metadata\n    table lists 7 cells with exclusion reasons (6 mismatches between RNA and phenotype, 1\n    outside MOp), while the Methods name four contaminated cells and one outside MOp; both are\n    reported, and the final 1,227 is tested in fig1a-ttype-coverage.\n- id: ed2-smartseq-similarity\n  statement: Patch-seq expression profiles are most similar to the single-nucleus Smart-seq2\n    reference, and t-type assignments based on Smart-seq2 and 10x references agree well.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraph 2; Extended Data Figure\n    2g-i\n  quote: We found that Patch-seq expression profiles were most similar to the single-nucleus\n    Smart-seq2 data (Extended Data Fig. 2g, h ). At the same time, there was good agreement between\n    t-type assignments based on Smart-seq2 and those based on 10x reference data (Extended Data Fig.\n    2i )\n  data: elsewhere\n  where: GEO GSE163764 (also NeMO dat-kq04hua); the seven MOp reference data sets of Yao et al.\n    2021 (doi:10.1038/s41586-021-03500-8)\n  criterion: As the Methods (t-Type assignment) and the code (ttype-assignment.ipynb) do it.\n    Reproduced when the median over cells of the maximal correlation is highest for the\n    single-nucleus Smart-seq2 reference among the seven, and the single-cell Smart-seq2 and\n    single-cell 10x v2 assignments fall in the same t-type for a majority of cells.\n- id: morph-reconstructions\n  statement: 646 neurons had staining good enough for reconstruction, 369 inhibitory and 269\n    excitatory among cells with a t-type; 73 t-types have at least one reconstructed neuron.\n  source: Results, Patch-seq of mouse primary motor cortex, paragraphs 1 and 3\n  quote: Of these neurons, 646 had sufficient staining for their morphologies to be reconstructed.\n  data: elsewhere\n  where: Brain Image Library, https://download.brainimagelibrary.org/3a/88/3a88a7687ab66069/\n  expected:\n  - quantity: reconstructed neurons\n    value: 646\n    tolerance: 0\n  - quantity: reconstructed inhibitory neurons with a t-type\n    value: 369\n    tolerance: 0\n  - quantity: reconstructed excitatory neurons with a t-type\n    value: 269\n    tolerance: 0\n  - quantity: t-types with a reconstruction\n    value: 73\n    tolerance: 0\n  criterion: Counts of SWC files in the excitatory and inhibitory folders (the 30 dendrite-only\n    Vip and Sncg reconstructions left out, Methods), matched to t-types; exact records.\n# --- RRR (needs gene counts) ----------------------------------------------------------------\n- id: fig2-rrr\n  statement: A sparse reduced-rank regression predicting the 17 electrophysiological features\n    from gene expression, with 25 genes and a rank-5 latent space, reaches a cross-validated R2\n    of 0.38, with cross-validated correlations of 0.90, 0.74 and 0.67 between the first three\n    pairs of projections.\n  source: Results, Distinct phenotypes of major families, paragraph 1; Figure 2; Methods,\n    Reduced-rank regression\n  quote: The selected model used 25 genes with a 5-dimensional latent space and achieved a\n    cross-validated R 2 of 0.38. ... The cross-validated correlations between the first three\n    pairs of projections were 0.90, 0.74, and 0.67, respectively.\n  data: with_inputs\n  expected:\n  - quantity: cross-validated R2\n    value: 0.38\n    tolerance: 0.038\n  - quantity: correlation of the first projections\n    value: 0.90\n    tolerance: 0.09\n  - quantity: correlation of the second projections\n    value: 0.74\n    tolerance: 0.074\n  - quantity: correlation of the third projections\n    value: 0.67\n    tolerance: 0.067\n  criterion: As the Methods and the code (reduced-rank-regression.ipynb, sparseRRR.py) do it. The\n    1,219 cells with all 17 features, a t-type and no exclusion; features standardized; genes\n    the 1,000 most variable (Methods' selection on raw exon counts, threshold 32, decay 1.5);\n    exon and intron counts over gene lengths summed, CPM, log2(x + 1), standardized. Rank 5,\n    alpha 1, relaxed solutions; 10-fold cross-validation with the code's folds (one permutation\n    with seed 42, contiguous folds); R2 and the correlations averaged over folds. Lambda: the\n    Methods give 0.5 for the 25-gene fit, the code's cross-validation cell uses 0.45; both are\n    run and the number of genes selected is reported. The Methods log-transform four features,\n    the code's RRR notebook three (latency not); the Methods' choice is the main reading and\n    the code's a variant. Reproduced when, under the main reading at either lambda, all four\n    values are within tolerance; partially reproduced when R2 is and a correlation is not, or\n    when only the variant matches.\n- id: ed5-rrr-ion-channels\n  statement: A reduced-rank regression restricted to ion channel genes does not perform much\n    worse than the full model, with cross-validated R2 0.33 and correlations 0.86, 0.71 and 0.56.\n  source: Results, Distinct phenotypes of major families, paragraph 2; Extended Data Figure 5e, f\n  quote: A reduced-rank regression model restricted to using only ion channel genes (Extended Data\n    Fig. 5 ) did not perform much worse than the full model (cross-validated R 2 = 0.33 and\n    correlations 0.86, 0.71, and 0.56, respectively, with regularization set to select 25 genes).\n  data: with_inputs\n  expected:\n  - quantity: cross-validated R2\n    value: 0.33\n    tolerance: 0.033\n  - quantity: correlation of the first projections\n    value: 0.86\n    tolerance: 0.086\n  - quantity: correlation of the second projections\n    value: 0.71\n    tolerance: 0.071\n  - quantity: correlation of the third projections\n    value: 0.56\n    tolerance: 0.056\n  criterion: As fig2-rrr, with genes the ion channel genes of HGNC group 177 (the code's\n    ion-channel-genes-group-177.csv) with non-zero counts in at least 10 cells (307), lambda\n    0.303 (Methods and code), no variable-gene selection. Reproduced when all four values are\n    within tolerance under one of fig2-rrr's two log-transform readings.\n- id: hold-time-yield\n  statement: The cDNA yield was not correlated with the recording hold time (Spearman\n    correlation -0.01).\n  source: Methods, Patch-seq recording procedures, last paragraph\n  quote: The resulting cDNA yield was not correlated with the hold time (Spearman correlation\n    −0.01).\n  data: with_inputs\n  expected:\n    quantity: Spearman correlation\n    value: -0.01\n    tolerance: 0.05\n  criterion: As the code does it (patch-seq-data-load.ipynb, last cell), the Spearman correlation\n    over cells with both values between hold time and the log of cDNA yield (yield from the\n    paper's metadata table; hold time from the dandiset where it is recorded, else from the\n    same table). The default 10% of 0.01 is below any meaningful resolution for a correlation\n    of about 1,300 cells, so the tolerance is 0.05, about one standard error (1 over the\n    square root of n). A claim of absence; the paper gives no test, so it is judged on the\n    value. Reproduced when the correlation is within tolerance.\n"
}
```

```
File created successfully at: claims/000008/10.1038-s41586-020-2907-3.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd claims/000008 && python - <<'E'
p='10.1038-s41586-020-2907-3.yaml'
s=open(p).read()
s=s.replace("""  quote: The mRNA of these 1,329 cells was sequenced, yielding on average 1.3 million exonic and
    0.7 million intronic reads (medians; mean ± s.d. on a log 10 scale; 6.0 ± 0.6 and 5.6 ± 0.8,
    respectively) and 9,100 ± 3,500 (mean ± s.d.) detected genes per cell""","""  quote: The mRNA of these 1,329 cells was sequenced, yielding on average 1.3 million exonic and
    0.7 million intronic reads (medians ... 6.0 ± 0.6 and 5.6 ± 0.8, respectively) and 9,100 ±
    3,500 (mean ± s.d.) detected genes per cell""")
s=s.replace("""k -means clusters (Fig. 5b ) ... Not all t-types showed high variability; some of them, such
    as Pvalb Vipr2_2""","""k -means clusters (Fig. 5b ) ... some of them, such as Pvalb Vipr2_2""")
open(p,'w').write(s)
E
cd ../.. && python tools/claims_check.py claims/000008/10.1038-s41586-020-2907-3.yaml paper/10.1038-s41586-020-2907-3.txt; grep -n "—\|rather" claims/000008/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

Fix with a scan for every plain scalar containing ": ".

**Agent calls Bash**

```bash
cd claims/000008 && grep -n "[a-z)]: [a-zA-Z0-9]" 10.1038-s41586-020-2907-3.yaml | grep -v "^\S*:\s*\(- \)\?[a-z_]*: \|^[0-9]*:#" | head -20
```

```
351:    classification of cells into families: it was mostly diagonal, with only the ET and IT
374:    several features that are very correlated with the shown ones: upstroke-to-downstroke ratio,
555:    landscape (Fig. 4e ): small shrub-like basket cells, horizontally elongated basket cells, and
789:    with seed 42, contiguous folds); R2 and the correlations averaged over folds. Lambda: the
```

**Agent calls Bash**

```bash
cd  && python - <<'E'
p='claims/000008/10.1038-s41586-020-2907-3.yaml'
s=open(p).read()
s=s.replace("""    room temperature, according to the two-sided Wilcoxon-Mann–Whitney test statistic (and omitting
    several features that are very correlated with the shown ones: upstroke-to-downstroke ratio,
    sag time, and sag area).""","""    room temperature, according to the two-sided Wilcoxon-Mann–Whitney test statistic (and omitting
    several features that are very correlated with the shown ones ... upstroke-to-downstroke
    ratio, sag time, and sag area).""")
s=s.replace("averaged over folds. Lambda: the","averaged over folds. For lambda, the")
open(p,'w').write(s)
E
python tools/claims_check.py claims/000008/10.1038-s41586-020-2907-3.yaml paper/10.1038-s41586-020-2907-3.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -c "—" claims/000008/*.yaml; grep -ci "rather" claims/000008/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/000008/10.1038-s41586-020-2907-3.yaml'))
from collections import Counter
c=d['claims'];print(len(c),sum('criterion' in x for x in c),sum('expected' in x for x in c),Counter(x.get('data','dataset') for x in c))"; git status --short
```

```
0
0
32 31 15 Counter({'dataset': 16, 'with_inputs': 11, 'elsewhere': 5})
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
?? claims/000008/
?? scripts
```

**Agent**

I wrote `claims/000008/10.1038-s41586-020-2907-3.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems. Nothing is committed.

**Text read.** The version of record (open access) from Europe PMC (PMC8113357): main text, Methods, figure legends and Extended Data legends. There was no PDF, so the Extended Data figures were read from their legends only. Not in the text: Extended Data Tables 1–2 (t-type descriptions) and Supplementary Files 1–3 (galleries, dot plots, the list of morphometric statistics). No claim rests on numbers that appear only in those, so I did not stop.

**Code read.** github.com/berenslab/mini-atlas at commit `3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9`. Besides the notebooks, it holds the paper's per-cell metadata, the feature tables and the count tables. Where the Methods are silent and the code decides, the criteria follow the code and cite it.

**Claims: 32.**
- **Quotes:** all 32 have one; none needed `inferred`.
- **Statistics:** none. The text reports no p-value or interval for any finding. The r values it does give (0.60, 0.70) are recorded under `expected`.
- **Criteria:** 31 of 32. The one without (`rnaseq-depth`) is judged on its expected values alone. 15 claims have expected values.
- **Data:** 16 `dataset`, 11 `with_inputs`, 5 `elsewhere`.
  - `dataset`: cohort, ages, genotypes, stimulus protocol, the Extended Data Fig. 4 example cell, feature counts, family features, kNN family separation, the IT/ET features, the t-type and depth claims, and the Fig. 5 variability claims.
  - `with_inputs`: reduced-rank regression, the Fig. 4 distance correlations, the t-SNE overlay claims, morphology combined with electrophysiology, and hold time against cDNA yield.
  - `elsewhere`: sequencing (GEO GSE163764 / NeMO) and morphology (Brain Image Library).
- **t-type labels:** claims that need a cell's t-type are marked `dataset`. Whether the NWB files carry it is left for the author to find, and the opening comment says so.

**Details the paper leaves open, with the readings named:**
- **Cell count:** 1,329 cells, or 1,328 if the one cell whose recording failed quality control is missing.
- **Age statistics:** taken over mice or over cells.
- **Stimulus interval:** measured onset to onset or offset to onset; "most" cells repeated means more than half.
- **Example cell (Extended Data Fig. 4):**
  - The legend does not name it; the code does (20181112_sample_11).
  - Its AP threshold is −40.18 mV in the legend but −43.18 mV in the code's table. Both readings are reported.
  - The legend prints the sag time as "0.26 ms"; the table has 0.26 s.
- **"High" firing, sag and rebound:** compared with all seven families, or with the four interneuron families.
- **Fig. 4c:** the code leaves out Sst Chodl and Pvalb Vipr2_2; the Methods don't say. Both readings are run, and the reported 50 t-types and 200 pairs show which one the paper used.
- **Extended Data Fig. 7:** "multiple families" means at least two, or a majority.
- **Fig. 4a, 5c, 5d (colour overlays only):** two readings each, one from embedding positions and one from transcriptomic distance. If they disagree, the claim is blocked as `methods_underspecified`.
- **Fig. 4b:** all 17 features (the code's Extended Data Fig. 6i analysis), or rebound alone.
- **Fig. 5a:** "Vip Mybpc1" means any one of its t-types, or all of them pooled.
- **Fig. 5b:** "many" means at least a quarter, or at least a third, of the t-types.
- **Reduced-rank regression:**
  - The penalty λ is 0.5 in the Methods and 0.45 in the code's cross-validation; both are run.
  - The Methods log-transform four features; the code's regression notebook does three. The Methods' choice is the main reading and the code's a variant.
- **Mismatched cells:** the Methods name 4 RNA/phenotype mismatches plus 1 cell outside MOp. The code's table lists 6 plus 1. Both counts are reported.
- **No measure at all:**
  - Fig. 4e (Pvalb axon shape) is recorded for coverage only.
  - Where the paper gives no test (Fig. 1b, the L4/5 IT_1 layer boundary, Extended Data Fig. 8 Leiden entropies), I fixed thresholds from the paper's own layer boundaries and its 25% misclassification cut, and the criteria say so.

**Missing from the paper:** the cut-off for "strong overlap" in Fig. 3d is not stated; the Fig. 5a legend's 25% was used. The p-value in Extended Data Fig. 6i appears only in the figure. No claim lacked text it needed beyond these.

## End of run

43 turns, 8 minutes, result: success.
