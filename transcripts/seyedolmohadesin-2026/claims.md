# 000981 · claims · run 39866925663

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/000981/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

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
cd  cat claims/001453/*.yaml; cat tools/claims_check.py | head -80
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
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -40 paper/*.txt; cat schemas/claims.schema.json | head -200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 200,400p schemas/claims.schema.json
```

```
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
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 127 more lines not kept]
```

**Agent**

Now the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "offset": 40,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "offset": 600,
 "limit": 960
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "offset": 600,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.txt",
 "offset": 1100,
 "limit": 460
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text (version of record, Methods, supplement legends) is present. Next, the paper's code and the dataset's archive description.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone --depth 1 https://github.com/venkatachalamlab/whole-brain-chemosensory-responses.git wbcr 2>&1 | tail -2; cd wbcr && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
Cloning into 'wbcr'...
b0dbdbf50c579d056d7991b7612fcff30091ffbd Sun Jun 1 21:19:12 2025 -0700
./python/scripts/transform.py
./python/scripts/quick_color_id.ipynb
./python/scripts/make_processed_data_with_color.ipynb
./python/scripts/make.py
./python/scripts/io.py
./python/scripts/array_writer.py
./python/figure_notebooks/config.py
./python/figure_notebooks/FigS2.ipynb
./python/figure_notebooks/Fig5.ipynb
./python/figure_notebooks/Fig4_prepare_data.ipynb
./python/figure_notebooks/Fig4.ipynb
./python/figure_notebooks/Fig2B-E&Fig3.ipynb
./python/figure_notebooks/Fig2A.ipynb
./python/figure_notebooks/Fig2&3_prepare_data.ipynb
./python/figure_notebooks/Fig1E&FigS1.ipynb
./python/figure_notebooks/.DS_Store
./python/extract_raw_traces_and_plot.ipynb
./python/datasets.json
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000981/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000981/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent**

47 assets matches 22 hermaphrodites + 25 males. Now reading the code.

**Agent calls Bash**

```bash
cd $TMPDIR/wbcr; cat README.md; cat python/figure_notebooks/config.py; head -c 1500 python/datasets.json; echo; curl -sL https://zenodo.org/api/records/21479592 | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('related_identifiers'), [f['key'] for f in d.get('files',[])])" 2>&1 | head
```

Result: the fetched text is not kept.

**Agent**

The Zenodo record is tag 1.0.0 of the same repository. Checking that tag against HEAD, then extracting the code cells.

**Agent calls Bash**

```bash
cd $TMPDIR/wbcr; git fetch --depth 1 origin tag 1.0.0 2>&1|tail -1; git rev-list -n1 1.0.0; git diff --stat 1.0.0 HEAD | tail -2; cat > $TMPDIR/nb.py <<'EOF'
import json,sys
for f in sys.argv[1:]:
    nb=json.load(open(f))
    print("#####",f)
    for i,c in enumerate(nb['cells']):
        if c['cell_type'] in('code','markdown'):
            print(f"--- [{i}] {c['cell_type']}"); print(''.join(c['source']))
EOF
for f in python/figure_notebooks/*.ipynb; do python $TMPDIR/nb.py "$f" > "$TMPDIR/$(basename "$f" .ipynb).py.txt"; done; wc -l $TMPDIR/*.py.txt
```

```
b0dbdbf50c579d056d7991b7612fcff30091ffbd
   129 /tmp/claude-1001/Fig1E&FigS1.py.txt
   607 /tmp/claude-1001/Fig2&3_prepare_data.py.txt
   381 /tmp/claude-1001/Fig2A.py.txt
  1031 /tmp/claude-1001/Fig2B-E&Fig3.py.txt
  1728 /tmp/claude-1001/Fig4.py.txt
   266 /tmp/claude-1001/Fig4_prepare_data.py.txt
  1123 /tmp/claude-1001/Fig5.py.txt
   197 /tmp/claude-1001/FigS2.py.txt
  5462 total
Shell cwd was reset to
```

**Agent**

Tag 1.0.0 is the HEAD commit b0dbdbf (1 June 2025, before the revision). Reading the data-preparation notebook.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/Fig2&3_prepare_data.py.txt"
}
```

```
1	##### python/figure_notebooks/Fig2&3_prepare_data.ipynb
2	--- [0] code
3	# from IPython.display import display, HTML
4	# display(HTML("<style>.container { width:75% !important; }</style>"))
5	--- [1] code
6	# Standard library imports
7	import os
8	from pathlib import Path
9	import json
10	import csv
11	
12	# Third-party library imports
13	import numpy as np
14	import pandas as pd
15	import h5py
16	import scipy
17	from scipy import stats
18	from scipy.signal import savgol_filter
19	import seaborn as sns
20	import matplotlib as mpl
[... 588 more lines not kept]
```

**Agent**

The prep code adds steps the Methods don't mention: artifact removal on trace ranges, a `conf == 1` filter, and dropping rows with more than 7 NaNs. Next, how the windows and ΔF/F0 are computed.

**Agent calls Bash**

```bash
cd $TMPDIR/wbcr/python; python $TMPDIR/nb.py compile_all_traces.ipynb > $TMPDIR/compile.txt; python $TMPDIR/nb.py extract_raw_traces_and_plot.ipynb > $TMPDIR/extract.txt; wc -l $TMPDIR/compile.txt $TMPDIR/extract.txt; ls ../ ; grep -rn "neuron_classes.json" -l . | head
```

```
514 /tmp/claude-1001/compile.txt
  482 /tmp/claude-1001/extract.txt
  996 total
LICENSE
README.md
python
./figure_notebooks/config.py
./compile_all_traces.ipynb
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/compile.txt"
}
```

```
1	##### compile_all_traces.ipynb
2	--- [0] code
3	# Standard library imports
4	import os
5	import json
6	import csv
7	import warnings
8	
9	# Third-party library imports
10	import numpy as np
11	import pandas as pd
12	import seaborn as sns
13	import matplotlib.pyplot as plt
14	from matplotlib.backends.backend_pdf import PdfPages
15	from tqdm import tqdm
16	from scipy.io import loadmat
17	from scipy import stats
18	from pathlib import Path
19	
20	--- [1] markdown
[... 495 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/Fig4_prepare_data.py.txt"
}
```

```
1	##### python/figure_notebooks/Fig4_prepare_data.ipynb
2	--- [0] code
3	from IPython.display import display, HTML
4	display(HTML("<style>.container { width:75% !important; }</style>"))
5	--- [1] code
6	import os
7	import json
8	import csv
9	from pathlib import Path
10	
11	import numpy as np
12	import pandas as pd
13	import scipy
14	import h5py
15	
16	import matplotlib.pyplot as plt
17	import matplotlib
18	from matplotlib.colors import TwoSlopeNorm
19	import seaborn as sns
20	
[... 247 more lines not kept]
```

**Agent**

Correlations use frames 98 to 4978, and stimulus steps start 2 frames before each onset. The connectome table is a local file the repo doesn't include. Now the Fig 4 analysis notebook.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i -E "r2|r\^2|linregress|polyfit|ttest|p_val|pvalue|abs\(|remove_outliers|mean\(axis|nanmean|threshold|<= ?0\.01|0\.4|top|36|sensory|exclude|corrcoef|pearson|spearman|R =|r_value" Fig4.py.txt | head -120
```

```
30:from scipy.stats import ttest_ind, linregress
51:# def pvalue_to_asterisks(p_value):
56:#     p_value (float): The p-value to convert.
61:#     if p_value < 0.001:
63:#     elif p_value < 0.01:
65:#     elif p_value < 0.05:
87:    # Determine cluster distance threshold
88:    cluster_distance_threshold = pairwise_distances.max() / factor
91:    idx_to_cluster_array = sch.fcluster(linkage, cluster_distance_threshold, criterion='distance')
105:def remove_outliers(values):
119:    factor = 3
126:    IQR = Q3 - Q1
141:corr_arr = corr_arr_data['array']
151:all 4 possible combinations are added to male_values and herm_values, then outliers are removed and then average and p_values are calculated, so basically we have more datapoints
176:avg_corr_arr = np.full((len(extended_classes), len(extended_classes)), np.nan, dtype='float16')
199:        male_values = remove_outliers([v for v in male_values if not np.isnan(v)])
200:        herm_values = remove_outliers([v for v in herm_values if not np.isnan(v)])
203:        _, p_value = stats.ttest_ind(herm_values, male_values)
215:        _dict['abs_diff'] = abs(_dict['diff'])
216:        _dict['p_value'] = p_value
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 140,250p Fig4.py.txt; echo ======; sed -n 335,440p Fig4.py.txt; echo =====; sed -n 840,1000p Fig4.py.txt
```

```
corr_arr_data = np.load(main_save_data_path/'correlation_arrays.npz', allow_pickle=True)
corr_arr = corr_arr_data['array']
corr_arr_metadata = corr_arr_data['metadata'].item() 
print(corr_arr.shape)
print(corr_arr_metadata.keys())
extended_neurons = corr_arr_metadata['dim2']

con_df = pd.read_csv(main_save_data_path/'normalized_connectome.csv', index_col=0)
display(con_df.head())
--- [6] markdown
# Calculate average correlation coefficient for pairs of  neuron classes in each sex
all 4 possible combinations are added to male_values and herm_values, then outliers are removed and then average and p_values are calculated, so basically we have more datapoints
--- [7] code
# Create a new list of extended neurons by combining odors (excluding the last two elements) with classes
extended_classes = odors[:-2] + classes

extended_neuron_classes = neuron_classes
for odor in odors[:-2]:
    extended_neuron_classes[odor] = [odor]

[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -i -E "class_info|responsive|dimorphic'|canonical|sum\(|count|len\(|category|groupby|any\(" Fig5.py.txt | head -80
```

```
50:# load class_info
51:class_info = pd.read_csv('../../traces/compiled_traces/class_info.csv', index_col=0)
52:class_info_collapsed = pd.read_csv('../../traces/compiled_traces/class_info_collapsed.csv', index_col=0)
54:class_info
77:df['dimorphic_odors'] = [ [] for _ in range(len(df)) ]
115:                sum_avg_herm = row.avg_herm.values.sum()
116:                final_herm_sem = np.sqrt(sum([x**2 for x in sem_herm_values]))
118:                sum_male_values = row.male_syn.values.sum()
142:class_info.loc[:, 'connectome_exists'] = class_info.neuron.isin(connectome_neurons)
144:class_info
147:plt.plot(range(len(combined_con_df)),combined_con_df.diff_sum)
163:        if len(sub_df)>0:
237:class_info.loc[:, 'synaptic_dimorphism']=False
253:    if len(row.neuron)==4:
259:    responsive = class_info[class_info.neuron==row.neuron].iloc[0].responsive
261:    # Add dimorphic odor wedges if responsive
262:    if responsive==True:
264:        N_odors = len(row.dimorphic_odors)
275:        # gray for responsive but not dimorphic
280:    # white if not responsive
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 700,830p Fig5.py.txt
```

```
ws.column_dimensions[column_letter].width = max_length + 2  # Adjust padding as needed

# Save the modified workbook
wb.save(file_path)
--- [35] markdown
# Fig. 5B- collapsed neuron classes
--- [36] markdown
## collapse neurons
--- [37] code
def or_reduce(series):
    return series.any()

def pool_lists(series):
    pooled = set()
    for item in series:
        pooled.update(eval(item))
    return list(pooled)
--- [38] code
class_info = pd.read_csv('../../traces/compiled_traces/class_info.csv', index_col=0)

[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -l -i -E "multipletests|fdr|anova|ols\(|AVA" *.py.txt; grep -n -i -E "multipletests\(|anova|fdr_bh" *.py.txt | head; head -60 FigS2.py.txt | tail -40; grep -n -i "ttest\|corr\|pearson" FigS2.py.txt Fig1E\&FigS1.py.txt | head
```

```
Fig2&3_prepare_data.py.txt
Fig2B-E&Fig3.py.txt
Fig4.py.txt
Fig5.py.txt
import matplotlib.colors as mcolors


import seaborn as sns

from scipy import stats
from scipy.stats import ttest_ind
import scipy.cluster.hierarchy as sch

from tqdm.notebook import tqdm

import importlib
import config

# Reload the module
importlib.reload(config)
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import fitz" 2>&1; which pdftoppm; python - <<'EOF'
import fitz,os
d=fitz.open('paper/10.1016-j.cub.2026.08.040.pdf'); print(d.page_count)
out=os.environ.get('TMPDIR','/tmp')
for p in [6,10]:  # 0-based: page 7 (Fig3), page 11 (Fig5)
    d[p].get_pixmap(dpi=110).save(f"{out}/p{p+1}.png")
EOF
ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent**

Rendering the PDF pages a different way (PyMuPDF is not installed).

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2026.08.040.pdf",
 "pages": "11"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render PDF pages here (neither PyMuPDF nor poppler is installed), so the figures' neuron-to-layer assignments stay unread. Checking the drop-test code before writing the file.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 60,197p FigS2.py.txt
```

```
file_path = Path(r"../../traces/drop_assays/control_drop_tests.xlsx")

excel_file = pd.read_excel(file_path, sheet_name=None)
for sheet_name, df in excel_file.items():
    df.columns = df.columns.str.lower()  # Convert all column names to lowercase
    # Drop columns with all NaN values
    df.dropna(axis=1, how='all', inplace=True)

    # Drop rows with all NaN values
    df.dropna(axis=0, how='all', inplace=True)



sheets = list(excel_file.keys())
print(len(sheets))
--- [6] code
# small change for here
odor_dict = {'OP50': 'Food',
 '1uM ascr#3': 'Pheromone',
 '800mM Sorbitol': 'Osmotic stress',
[... 118 more lines not kept]
```

**Agent**

I have what I need: the full text, the Methods, the supplement's figure legends, and the code at b0dbdbf. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/wbcr; grep -c . python/datasets.json; python -c "
import json;d=json.load(open('python/datasets.json'));from collections import Counter;print(Counter(v['sex'] for v in d.values()))"
```

```
237
Counter({'male': 25, 'hermaphrodite': 22})
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/000981/10.1016-j.cub.2026.08.040.yaml",
 "content": "# Claims for Seyedolmohadesin et al. (2026), \"Whole-brain chemosensory responses of both C. elegans\n# sexes\", Current Biology 36, 4803-4816, on dandiset 000981.\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions),\n# 2026-10-22, protocol pilot-10 as stated in docs/protocol.md. No data of the dandiset were seen;\n# only its title and description on the archive (\"Datasets for the Current Biology paper\", 47 assets).\n#\n# Text read. The version of record (PDF supplied by a person, text extracted with PyMuPDF), in\n# paper/10.1016-j.cub.2026.08.040.txt: main text, STAR Methods, and the supplement's Figures S1 to\n# S20 with their legends. Data S1 to S4 (spreadsheets behind Figures 2 to 5) and Videos S1 and S2\n# are not in the text. No figure was read from the PDF (no renderer was available).\n#\n# Code read. https://github.com/venkatachalamlab/whole-brain-chemosensory-responses at commit\n# b0dbdbf50c579d056d7991b7612fcff30091ffbd (1 June 2025). This is tag 1.0.0, which is the Zenodo\n# record the key resources table cites (10.5281/zenodo.21479592). It holds compile_all_traces.ipynb\n# (traces to per-presentation responses, and the band-passed traces for correlations), the figure\n# notebooks Fig2&3_prepare_data, Fig2B-E&Fig3, Fig4_prepare_data, Fig4, Fig5 and FigS2 (the drop\n# tests), config.py (stimulus names, onset frames, which of the 47 recordings are male) and\n# datasets.json (47 recordings, 22 hermaphrodites and 25 males). It does not hold the files it reads:\n# neurons/neuron_classes.json (the neuron classes and their layer), the metadata spreadsheet\n# sexual_dimorphism_data.xlsx (time ranges and ganglia to ignore per recording), confidence.csv\n# (identification confidence), the per-recording stimulus order files, or the connectome table. The\n# code predates the revision (submitted July 2025, revised January 2026) and has no code for the\n# cycle-1 and per-animal representations, the FDR correction, the AVA motor-state analyses (Figures\n# S2A to S2C, S3F, S3G, S8) or Figure S2E, S2F; those rest on the Methods alone.\n#\n# The data the paper used. OH16230 (otIs670[NeuroPAL]; otIs672[panneuronal GCaMP6s]) young adults,\n# 22 hermaphrodites and 25 males, each in a sex-specific microfluidic trap with 1 mM levamisole. One\n# recording per animal, 31 min continuous, GCaMP6s at 2.67 volumes/s (25 planes, 15 ms each), plus a\n# NeuroPAL multicolour volume for identification. Stimuli to the nose, 10 per cycle in a random order\n# per animal repeated three times; 60 s buffer first, then each stimulus 15 s followed by 45 s\n# buffer. The 10 are OP50 supernatant (food), 1 uM ascr#3 (pheromone), 800 mM sorbitol (osmotic\n# stress), 10 mM CuSO4 (toxic stress), isoamyl alcohol 1e-6 and 1e-2 (low and high odor), NaCl 100 and\n# 450 mM (low and high salt), a buffer-to-buffer switch (control) and 10 uM fluorescein (flow check).\n# Measured variables: a calcium trace per identified neuron (mean of the 15 brightest pixels in a\n# 2 x 2 x 3 um box at the ZephIR-tracked centre), neuron identities, sex, and the stimulus timing.\n# 196 sex-shared and 6 male-specific head neurons were analysed; tail neurons were recorded but not\n# analysed. Drop-test behaviour (Figure S1A, S1B) and published connectomes (Figure 4) are other data.\n#\n# Common methods, cited once here and named in the criteria.\n#\n# RESPONSE (Methods, Calculating stimulus onset and offset responses; code compile_all_traces.ipynb,\n# normalized_odor_response). For each neuron and stimulus presentation, the onset response is the\n# mean dF/F0 over the 40 frames (15 s) from stimulus onset, F0 the mean of the 10 frames (3.75 s)\n# before onset; the offset response is the mean dF/F0 over the 40 frames after offset, F0 the mean of\n# the 10 frames before offset. The code takes onset frames from config.py (181, 340, 500, ... 4818,\n# 30 presentations), offset = onset + 40 frames, and the stimulus at each position from the\n# recording's stimulus order.\n#\n# EXCLUSION (Methods, same section). Per neuron class, sex and stimulus, the means of the 15 s before\n# onset, during delivery and after offset (onset F0) are pooled over cycles, animals and the class's\n# neurons; a presentation with any of the three below Q1 - 5 IQR or above Q3 + 5 IQR is excluded. The\n# code (Fig2&3_prepare_data.ipynb) also excludes, with the same 5 IQR rule, presentations whose range\n# (max - min of dF/F0) in any of the three windows is extreme; keeps only identifications with\n# confidence 1; drops presentations with more than 7 missing frames of 120; and blanks time ranges\n# and ganglia listed per recording in a spreadsheet not in the repository. The Methods name only the\n# outlier rule. Two readings are run: (a) the Methods' rule alone; (b) the code's filters as well, as\n# far as the dandiset carries identification confidence and ignored ranges (the author says which).\n#\n# CLASSES. Left and right neurons (and the dorsal and ventral subclasses the code keeps apart) are\n# pooled into one subclass; ASEL and ASER stay separate (Results, Most sensory neurons..., paragraph\n# 3). Figures 3 and 4 use these subclasses (110 for Figure 4, Results, Functional correlations...,\n# paragraph 1). Counts use 89 canonical classes (Figure 5 legend); the code (Fig5.ipynb) collapses\n# CEP, IL1, IL2, OLQ, URY, SAA, SAB, SIA, SIB, RMD, RME, SMB, SMD, URA and the cord classes AS, DA, DB,\n# DD, VA, VB, VD, and calls a canonical class responsive (or dimorphic) when any subclass is. OPEN.\n# Which class is in which layer (24 sensory, 36 inter, 15 motor, 14 pharyngeal) is in Figure 5A and\n# Data S4 and in the code's missing neuron_classes.json; the author must use an assignment with these\n# totals, list it, and record it as a deviation.\n#\n# DIMORPHISM (Methods, Identifying sexually dimorphic responses, representation 1, which Figure 3\n# shows; code Fig2&3_prepare_data.ipynb). Per subclass, stimulus and window (onset or offset), all\n# hermaphrodite responses (every cycle, every neuron of the subclass, every animal) against all male\n# responses, two-sample t-test with equal variances (scipy ttest_ind default, as the code). Dimorphic\n# when p <= 0.05. Representation 2 uses cycle 1 only; representation 3 first averages each animal's\n# responses over cycles and left and right. The Figure 3 colour is |male - herm| / (|herm| + |male|\n# + 0.1) (code).\n#\n# RESPONSIVE (Methods, Identifying responsive neuron classes; code). Per subclass, sex, cue (the 8\n# cues) and window, the pooled responses against the pooled responses of the same subclass and sex\n# to the buffer-to-buffer control, two-sample t-test; responsive when p <= 0.05 (the code uses p <\n# 0.05, shown as a variant). A class is responsive if this holds in at least one sex for at least\n# one cue and window.\n#\n# CORRELATION (Methods, Calculating dimorphism in functional connectivity; code compile_all_traces\n# correct(), Fig4_prepare_data, Fig4). Each whole trace z-scored, then band-passed as the mean of the\n# past 10 frames minus the mean of the past 240 frames (the code's windows include the current frame,\n# 11 and 241 frames); the code blanks the first 96 frames and correlates frames 98 to 4978, pairwise\n# complete. A stimulus is a binary series, 1 while delivered (the code sets 1 from 2 frames before the\n# onset frame for 40 frames). Pearson r per pair per animal. Per subclass pair and sex, two readings:\n# (a) the code's, all left-right combinations of all animals pooled, values beyond 3 IQR of the\n# quartiles removed, mean, and a two-sample t-test (equal variances) on the pooled values; (b) the\n# Methods', the mean over the combinations per animal, then the mean over animals and a t-test on the\n# per-animal values. Functional dimorphism is |mean herm - mean male|.\n#\n# CONNECTOME (Methods, Normalization of connectome data and Calculating dimorphism in synaptic\n# connectivity; code Fig4_prepare_data, Fig4). Three hermaphrodite connectomes (White et al. 1986 as\n# annotated by Cook et al. 2019; Witvliet et al. 2021 datasets 7 and 8) and the male of Cook et al.\n# 2019 (doi 10.1038/s41586-019-1352-7). The code reads them from a table prepared by S.J. Cook that is\n# not in the repository. Each dataset divided by its 95% quantile and multiplied by White's 95%\n# quantile; hermaphrodite weight the mean of the three, with its SEM; per subclass pair the sum of\n# the 8 directed weights, the SEMs combined in quadrature; dimorphism degree |Sherm - Smale| / (Sherm\n# + Smale + 5) (Methods; the code uses 3, and drops pairs with both sums below 3, a variant).\n#\n# Omitted as checks of method, not findings: Figures S8E, S9 to S11 (window sizes) and S13, S16, S19.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000981\"\npaper: doi:10.1016/j.cub.2026.08.040\nclaims:\n- id: recordings-animals\n  statement: Whole-head activity of 196 sex-shared and 6 male-specific neurons was studied in 22\n    hermaphrodites and 25 males.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 1\n  quote: We studied the activity of 196 sex-shared neurons ... in the heads of 22 hermaphrodites and\n    25 males\n  expected:\n  - quantity: hermaphrodites recorded\n    value: 22\n    tolerance: 0\n  - quantity: males recorded\n    value: 25\n    tolerance: 0\n  criterion: Counted from the recordings' sex. The tolerance is zero because these are counts of\n    recorded animals, which the code's datasets.json also gives (22 and 25 of 47).\n- id: fig5b-responsive-classes\n  statement: Of the 89 head neuron classes, 84 (94%) responded to at least one stimulus in at least\n    one sex.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 9;\n    Figure 5B\n  quote: Of the 89 neuron classes in the head, 84 were responsive (94%)\n  expected:\n    quantity: responsive canonical head classes\n    value: 84\n    tolerance: 8.4\n  criterion: RESPONSE, EXCLUSION (both readings), CLASSES and RESPONSIVE as in the opening comment,\n    counted over the 89 canonical classes. Male-specific CEM and MCM are not among the 89 (code\n    removes them). Reproduced when the count is within tolerance under an exclusion reading.\n- id: fig5b-dimorphic-classes\n  statement: Of the 89 head neuron classes, 80 (90%) responded dimorphically to at least one stimulus.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 9;\n    Figure 5B\n  quote: and 80 classes (90%) were sexually dimorphic\n  expected:\n    quantity: dimorphic canonical head classes\n    value: 80\n    tolerance: 8.0\n  depends_on:\n  - fig5b-responsive-classes\n  criterion: DIMORPHISM (representation 1) over the 8 cues, onset or offset, then CLASSES. The code\n    (Fig5.ipynb) counts a class as dimorphic only when it is also responsive; the Methods do not say\n    so. Readings are (a) dimorphic and responsive, as the code; (b) dimorphic alone. Each is run with\n    both exclusion readings. Reproduced when the count is within tolerance under one reading.\n- id: fig5b-layer-counts\n  statement: Responsive and dimorphic classes per layer are 23 and 22 of 24 sensory, 34 and 33 of 36\n    inter, 14 and 13 of 15 motor, and 13 and 12 of 14 pharyngeal classes.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 9;\n    Figure 5B\n  quote: Of the 24 sensory neuron classes, 23 classes (96%) were responsive, and 22 classes (92%) were\n    dimorphic. Of the 36 interneuron classes, 34 classes (94%) were responsive, and 33 classes (92%)\n    were dimorphic. Of the 15 motor neuron classes, 14 classes (93%) were responsive, and 13 classes\n    (87%) were dimorphic. Of the 14 pharyngeal neuron classes, 13 classes (93%) were responsive, and\n    12 classes (86%) were dimorphic\n  expected:\n  - quantity: responsive sensory classes\n    value: 23\n    tolerance: 2.3\n  - quantity: dimorphic sensory classes\n    value: 22\n    tolerance: 2.2\n  - quantity: responsive interneuron classes\n    value: 34\n    tolerance: 3.4\n  - quantity: dimorphic interneuron classes\n    value: 33\n    tolerance: 3.3\n  - quantity: responsive motor neuron classes\n    value: 14\n    tolerance: 1.4\n  - quantity: dimorphic motor neuron classes\n    value: 13\n    tolerance: 1.3\n  - quantity: responsive pharyngeal classes\n    value: 13\n    tolerance: 1.3\n  - quantity: dimorphic pharyngeal classes\n    value: 12\n    tolerance: 1.2\n  depends_on:\n  - fig5b-responsive-classes\n  - fig5b-dimorphic-classes\n  criterion: As the two claims it depends on, split by layer. The layer assignment is OPEN (opening\n    comment, CLASSES). Reproduced when all eight counts are within tolerance under one reading;\n    partially reproduced when six or seven are.\n- id: fig3-each-stimulus-mixed\n  statement: For every stimulus at least one neuron class responds dimorphically and at least one\n    monomorphically.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 5;\n    Figure 3A and 3B; Figure 5B\n  quote: For each stimulus tested, we observed at least one neuron class respond in a sexually\n    dimorphic manner, and one class respond in a monomorphic manner\n  depends_on:\n  - fig5b-responsive-classes\n  criterion: Per cue, a class is dimorphic to it when DIMORPHISM gives p <= 0.05 at onset or offset,\n    and monomorphic to it when RESPONSIVE holds for that cue and DIMORPHISM gives p > 0.05 at both\n    onset and offset (Figure 5B legend counts per-stimulus responsive and dimorphic classes; code\n    Fig5.ipynb). Reproduced when all 8 cues have at least one of each, under each exclusion reading.\n- id: sensory-dimorphic-and-monomorphic\n  statement: Nearly every sensory neuron class responds dimorphically to at least one stimulus and\n    monomorphically to at least one other.\n  source: Discussion, paragraph 1; Figures 3 and 5A\n  quote: nearly every sensory neuron responds in a sexually dimorphic manner to at least one stimulus\n    while responding monomorphically to at least one other stimulus\n  depends_on:\n  - fig3-each-stimulus-mixed\n  - fig5b-layer-counts\n  criterion: Dimorphic and monomorphic to a cue as defined in fig3-each-stimulus-mixed, over the 24\n    sensory canonical classes. The paper gives no count for the pair of conditions; \"nearly every\"\n    is read from the paper's own use of it for 22 of 24 sensory classes and 80 of 89 classes, as at\n    least 90% (22 of 24). Reproduced when at least 22 sensory classes meet both conditions.\n- id: fig3a-osmotic-onset-examples\n  statement: At the onset of osmotic stress ASER and ASH respond monomorphically while AWA and AWB\n    respond dimorphically.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 5;\n    Figures 2B and 3A\n  quote: in response to the onset of osmotic stress, the gustatory neuron ASER and the nociceptive\n    neuron ASH ... show monomorphic responses, whereas olfactory neurons AWA and AWB ... show\n    dimorphic responses\n  statistics:\n  - about: dimorphism of AWA and AWB onset responses to osmotic stress\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window, 800 mM sorbitol. Reproduced when AWA and AWB\n    have p <= 0.05 and ASER and ASH have p > 0.05 (the absence is judged on the same test). The four\n    p-values and normalized differences are reported, under both exclusion readings.\n- id: fig2b-bag-high-odor-monomorphic\n  statement: AWA's response to osmotic stress is dimorphic and BAG's response to high odor is\n    monomorphic.\n  source: Figure 2B legend\n  quote: exemplifying sexually dimorphic (e.g., AWA responding to osmotic stress) and monomorphic\n    neural activity (e.g., BAG responding to high odor)\n  criterion: DIMORPHISM, representation 1. The legend does not say onset or offset; Figure 2B plots\n    the whole presentation. Readings are (a) onset, (b) offset, (c) either window for AWA and both\n    windows for BAG. Reproduced when, under one reading, AWA has p <= 0.05 and BAG with 1e-2 isoamyl\n    alcohol has p > 0.05.\n- id: fig3a-ash-stimulus-dependent\n  statement: ASH responds monomorphically to osmotic and toxic stress but dimorphically to high salt.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 5;\n    Figures 2B and 3A\n  quote: the ASH neuron's response to osmotic and toxic stress is monomorphic, but its response to high\n    salt is dimorphic\n  statistics:\n  - about: dimorphism of the ASH response to high salt\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window (the text cites Figure 3A, onset). Reproduced\n    when ASH has p <= 0.05 for 450 mM NaCl and p > 0.05 for sorbitol and for CuSO4.\n- id: fig3a-aser-salt-concentration\n  statement: ASER responds dimorphically to low salt but monomorphically to high salt.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 5;\n    Figures 2B and 3A\n  quote: the ASER neuron's response to a low concentration of salt is dimorphic, but its response to a\n    higher concentration of salt is monomorphic\n  statistics:\n  - about: dimorphism of the ASER response to low salt\n    test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, onset window (Figure 3A), ASER alone. Reproduced when the\n    100 mM NaCl response has p <= 0.05 and the 450 mM NaCl response p > 0.05.\n- id: fig2e-i2-dimorphic\n  statement: Pharyngeal interneuron I2 responds dimorphically to pheromone, osmotic stress and salt.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 7;\n    Figure 2E\n  quote: pharyngeal interneuron I2 exhibited sexually dimorphic responses to pheromone, osmotic stress,\n    and salt\n  statistics:\n  - test: independent-sample t test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: DIMORPHISM, representation 1, class I2. The text fixes neither the window nor which salt.\n    Reproduced when ascr#3, sorbitol and at least one NaCl concentration each give p <= 0.05 at onset\n    or offset; the readings (onset only, offset only, low salt, high salt) are all reported.\n- id: pharynx-dimorphic-food-salt-pheromone\n  statement: The pharyngeal (enteric) neurons respond dimorphically to food, salt and pheromone.\n  source: Discussion, paragraph 4; Figure 2E\n  quote: the enteric nervous system of the worm responds to food, salt, and (most strikingly) pheromone\n    in a sexually dimorphic manner\n  criterion: DIMORPHISM, representation 1, over the pharyngeal subclasses (layer OPEN, opening comment).\n    Reproduced when at least one pharyngeal class has p <= 0.05, at onset or offset, for OP50, for\n    ascr#3, and for at least one NaCl concentration.\n- id: fig2-awa-awb-nociceptive\n  statement: Olfactory neurons AWA and AWB also respond to osmotic and toxic stress.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 7;\n    Figure 2B\n  quote: in addition to responding to odors, olfactory neurons AWA and AWB also responded to\n    nociceptive stimuli, including osmotic and toxic stress\n  criterion: RESPONSIVE per class and cue (in at least one sex, onset or offset). Reproduced when AWA\n    and AWB are each responsive to sorbitol and to CuSO4.\n- id: fig2-adf-m2-switch\n  statement: ADF responds to food in hermaphrodites but to pheromone in males, and pharyngeal neuron\n    M2 shows a similar switch between food and pheromone.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 7;\n    Figures 2B and 2E\n  quote: ADF responds to food in hermaphrodites, but in males it responds to pheromones ... More\n    surprising was a similar dimorphic switch in the M2 pharyngeal neuron, also to food and pheromone\n  criterion: Per sex, RESPONSIVE (onset or offset) of ADF and M2 to OP50 and to ascr#3. For M2 the text\n    does not say which sex responds to which cue. Readings are (a) ADF responsive to food and not to\n    pheromone in hermaphrodites, and to pheromone and not to food in males; M2 responsive to one cue\n    and not the other in each sex, with the cues opposite between sexes; (b) DIMORPHISM gives p <=\n    0.05 for both cues in each of ADF and M2. Reproduced when ADF and M2 meet one reading; partially\n    reproduced when one of the two does.\n- id: male-specific-unresponsive\n  statement: The male-specific head neuron classes CEM and MCM were predominantly unresponsive to the\n    stimuli.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 2;\n    Figure S2D (the text cites S2C; the legend of S2D shows the male-specific neurons)\n  quote: The male-specific head neuron classes (sensory neuron CEM and interneuron MCM) were\n    predominantly unresponsive to stimuli\n  criterion: RESPONSIVE in males, for CEMD, CEMV and MCM as the code separates them, over 8 cues and 2\n    windows (16 tests per class). \"Predominantly\" is read as most of the tests. Reproduced when fewer\n    than half of each class's tests are significant; the number significant is reported.\n- id: tail-unresponsive\n  statement: Tail neurons did not appear to respond to cues presented to the head.\n  source: Results, Broad chemosensory stimulation activates the whole brain of both sexes, paragraph 3\n  quote: tail neurons did not appear to be responsive to cues presented to the head\n  criterion: The paper reports no test on tail neurons; its test of responsiveness is RESPONSIVE. A\n    claim of absence, judged on that test, applied to each tail class the dandiset identifies.\n    Reproduced when no tail class is responsive; not reproduced when any is, with the number of\n    classes and tests reported. Not testable if the dandiset holds no identified tail neurons.\n- id: figs2f-left-right-similar\n  statement: Neurons within the same class usually have equivalent activity, with left and right\n    neurons more correlated with each other than with neurons of other classes.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 3;\n    Figure S2F\n  quote: Neurons within the same class usually exhibit equivalent neural-activity traces\n  criterion: Figure S2F legend, the within-animal Pearson r between the left and right neurons of each\n    class against the mean r of each of them with neurons of other classes. The traces are OPEN.\n    Readings are (a) the band-passed traces of CORRELATION; (b) the raw traces. Reproduced when, in\n    each sex, the mean left-right r exceeds the mean other-class r for more than half of the\n    bilateral classes, under both readings.\n- id: figs3e-pattern-robust\n  statement: Restricting the test to the first cycle or to per-animal averages makes specific\n    neuron-stimulus pairs less clearly dimorphic but leaves the pattern of dimorphic neuron classes\n    largely unchanged.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 10;\n    Figure S3A to S3E\n  quote: Overall, while specific odor-neuron pairs are not as clearly dimorphic in these more\n    conservative analyses, the pattern of neurons that we find to respond dimorphically is largely\n    unaffected\n  depends_on:\n  - fig5b-dimorphic-classes\n  criterion: DIMORPHISM under representations 1, 2 and 3 (Methods), per subclass, at p <= 0.05; a class\n    is dimorphic when any cue and window is (Figure S3E legend). The paper fixes no measure of\n    \"largely\". Readings are (a) more than half of the classes dimorphic under representation 1 are\n    dimorphic under all three (S3E's robust classes); (b) more than half of them are dimorphic under\n    each of representations 2 and 3 separately. Reproduced when one reading holds and the number of\n    dimorphic neuron-cue-window pairs is lower under representations 2 and 3 than under 1.\n- id: figs2e-no-order-effect\n  statement: Response amplitude does not depend on the position of the stimulus in the presentation\n    order.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 10;\n    Figure S2E\n  quote: We also verified that there was no dependence on response amplitude as a function of stimulus\n    order\n  criterion: Figure S2E legend, onset responses (RESPONSE) of cycle 1 only, against position 1 to 10,\n    for all stimuli combined and for each stimulus. The paper names no test and does not say which\n    neurons enter. Readings are (a) a linear regression of response on position over all neuron\n    responses, slope p >= 0.05; (b) the same on per-animal means over neurons; (c) a one-way ANOVA\n    over positions on all neuron responses, p >= 0.05. A claim of absence with no test in the paper,\n    so all readings are run; reproduced when all find no dependence for all stimuli combined, not\n    reproduced when all find one, otherwise blocked as methods_underspecified. Per-stimulus results\n    are reported.\n- id: figs3fg-state-dependence-interneurons\n  statement: Motor-state-dependent sexual dimorphism is more prominent in interneurons than in sensory\n    or motor neurons.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 11;\n    Figure S3F and S3G\n  quote: These state-dependent responses were more prominent in interneurons than in sensory or motor\n    neurons\n  criterion: State per presentation from AVA (Methods, Classifying motor state); the AVA trace is\n    divided by an exponential fit of its baseline, the 5 s before onset is a transition if it changes\n    by more than 20%, otherwise reverse when its mean is above the global mean and forward when\n    below. OPEN, with all combinations run. AVA as AVAL, AVAR, or their mean; \"changes by more than\n    20%\" as (max - min) / mean of the window, or as |last - first| / first; the fit subtracted or\n    divided. Per neuron-cue pair and window, a two-way ANOVA of RESPONSE values (representation 1)\n    on sex and state (forward and reverse; transitions out), interaction p (Methods, Identifying\n    state-dependent...), BH over the pairs of each window. Per layer, the fraction of neuron-cue pairs\n    with interaction q < 0.05 (black borders in S3F, S3G), and as a second reading p < 0.05.\n    Reproduced when the interneuron fraction exceeds both the sensory and the motor fraction.\n- id: figs2c-aib-state\n  statement: The structure of AIB's sexual dimorphism to high salt or pheromone differs between\n    forward and backward motor states.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 11;\n    Figure S2C\n  quote: In some responses, such as AIB responding to high salt or pheromones (Figure S2C), the\n    structure of the sexual dimorphism is different when animals are (fictively) moving forward in\n    comparison to backward\n  depends_on:\n  - figs3fg-state-dependence-interneurons\n  criterion: States and readings as in figs3fg-state-dependence-interneurons. Per state, DIMORPHISM of\n    AIB (S2C legend, two-sample t-test). Reproduced when, for 450 mM NaCl or for ascr#3, at onset or\n    offset, either the sex x state interaction has p < 0.05 or the response is dimorphic (p <= 0.05)\n    in one state and not in the other.\n- id: figs8-state-insensitive\n  statement: Average responses are mostly insensitive to the animal's motor state, and many dimorphic\n    sensory responses persist after conditioning on it.\n  source: Results, Most sensory neurons in the head exhibit sexually dimorphic responses, paragraph 11;\n    Discussion, paragraph 3; Figure S8A to S8D\n  quote: Overall, however, average responses were mostly insensitive to the motor state of the animal\n  depends_on:\n  - figs3fg-state-dependence-interneurons\n  criterion: States and readings as in figs3fg-state-dependence-interneurons, onset state, over the\n    classes and cues of Figure 2B to 2E (code Fig2&3_prepare_data, ADF, ADL, ASEL, ASER, ASH, ASI,\n    AWA, AWB, BAG, AIA, AIB, AVE, AVH, RIA, RIR, DB1, VB2, M2, I2, MC, M3). The paper names no test of\n    insensitivity; with its two-sample t-test, per class, cue, window and sex, forward against reverse\n    responses. Reproduced when more than half of these comparisons have p > 0.05, and more than half\n    of the sensory class-cue-window responses dimorphic under DIMORPHISM stay dimorphic (p <= 0.05)\n    within the forward state or within the reverse state.\n- id: fig4c-functional-connectivity-similar\n  statement: Pairwise functional connectivity is highly similar between the sexes (R2 = 0.8 for a\n    linear fit of male on hermaphrodite mean correlations).\n  source: Results, Functional correlations between sex-shared neurons are predominantly shared between\n    sexes, paragraph 2; Figure 4C\n  quote: the functional connectivity between hermaphrodites and males is highly similar (80% or R2 =\n    0.8 for a linear fit)\n  expected:\n    quantity: R2 of male against hermaphrodite mean pairwise correlations\n    value: 0.8\n    tolerance: 0.08\n  criterion: CORRELATION, both readings, over the pairs of the 110 subclasses with stimuli left out\n    (code Fig4.ipynb, no_odor_score_df); R2 of an ordinary least-squares line (scipy linregress, as\n    the code). Reproduced when R2 is within tolerance under one reading.\n- id: fig4-stimuli-correlate-sensory\n  statement: In both sexes stimuli are more correlated or anti-correlated with sensory neurons than\n    with interneurons or motor neurons.\n  source: Results, Functional correlations between sex-shared neurons are predominantly shared between\n    sexes, paragraph 2; Figure 4B\n  quote: In both sexes, stimuli were more correlated (or anti-correlated) with sensory neurons than with\n    interneurons ... or motor neurons\n  criterion: CORRELATION per stimulus-subclass pair (880 pairs), the per-sex mean r. The paper gives no\n    test or summary. Readings are (a) the mean |r| over the pairs of each layer; (b) the root mean\n    square r (as Figure S14's global correlation). Reproduced when, in each sex, the sensory value\n    exceeds the interneuron and the motor value under both readings and both CORRELATION readings.\n- id: fig4-pharynx-uncorrelated\n  statement: Pharyngeal neurons show some correlations with each other but are largely uncorrelated\n    with the rest of the brain.\n  source: Results, Functional correlations between sex-shared neurons are predominantly shared between\n    sexes, paragraph 2; Figure 4B\n  quote: Neurons within the pharynx show some correlations with each other but are largely uncorrelated\n    with the rest of the brain\n  criterion: CORRELATION, per-sex mean r per subclass pair. The paper gives no measure; mean |r| is\n    used, with root mean square r as the second reading. Reproduced when, in each sex, pharyngeal to\n    non-pharyngeal pairs have a lower value than pharyngeal to pharyngeal pairs and than\n    non-pharyngeal to non-pharyngeal pairs, under every reading.\n- id: fig4-functional-dimorphism-small\n  statement: Almost all neuron pairs have a functional dimorphism below 0.4, on a scale of 0 to 2.\n  source: Results, Functional and synaptic sexual dimorphisms are distinct, paragraph 2; Figure 4E\n  quote: we observed that almost all neuronal pairs had a functional dimorphism of less than 0.4\n  criterion: CORRELATION, functional dimorphism per pair of subclasses (stimuli left out, \"neuronal\n    pairs\"). \"Almost all\" is read as (a) at least 95% or (b) at least 99% of pairs. Reproduced when\n    one reading holds under a CORRELATION reading; the fraction is reported.\n- id: fig4d-functional-synaptic-uncorrelated\n  statement: Functional and synaptic dimorphisms are uncorrelated.\n  source: Results, Functional and synaptic sexual dimorphisms are distinct, paragraph 3; Figure 4D\n  quote: We found no clear relationship between synaptic and functional dimorphism\n  data: with_inputs\n  criterion: Functional dimorphism (CORRELATION) and synaptic dimorphism degree (CONNECTOME) per pair\n    of subclasses present in the connectome, pairs without synapses set to 0 (code Fig4.ipynb). A\n    claim of absence. The test is the code's linear regression (scipy linregress); the paper reports\n    no value or threshold, so the paper's alpha of 0.05 is used. Reproduced when the slope has p >=\n    0.05; not reproduced when p < 0.05; R2 and slope reported either way. The code's regularization\n    of 3 is a variant.\n- id: fig4f-synaptic-top-not-functional\n  statement: The neuron pairs with the highest synaptic dimorphisms are functionally uncorrelated in\n    both sexes and show little to no functional dimorphism.\n  source: Results, Functional and synaptic sexual dimorphisms are distinct, paragraph 3; Figure 4F;\n    Figure S4B\n  quote: These pairs were functionally uncorrelated in both sexes\n  data: with_inputs\n  criterion: The top 36 pairs by dimorphism degree after removing pairs with combined SEM >= 5\n    (Methods, Selecting neuron pairs...), and the six of Figure 4F (code, RIM-SAAD, AIB-AIM,\n    URYD-RMDV, AVK-RMF, URX-RIR, ASH-AVA). Functional dimorphism p from CORRELATION. Readings of \"no\n    functional dimorphism\" are (a) p > 0.05 (Figure 4F asterisks); (b) p >= 0.01 (Figure 4E white).\n    Reproduced when more than half of the 36 and of the six have no functional dimorphism under one\n    reading; their mean r per sex is reported.\n- id: fig4g-functional-top-not-synaptic\n  statement: The neuron pairs with the highest functional dimorphisms are mostly not synaptically\n    connected, and where connected their connectivity is essentially not dimorphic.\n  source: Results, Functional and synaptic sexual dimorphisms are distinct, paragraph 3; Figure 4G;\n    Figure S4C\n  quote: We found that these pairs were mostly not synaptically connected. When they were connected,\n    the connectivity was essentially not dimorphic\n  data: with_inputs\n  criterion: The top 36 pairs by functional dimorphism with p < 0.01 (Methods; the code's p < 0.001 is\n    a variant), stimulus pairs, sensory-sensory pairs and pairs absent from the connectome left out\n    (Methods, Selecting neuron pairs...). Not connected is read as (a) zero summed weight in both\n    sexes, or (b) both sums below 3 (the code drops these). Not dimorphic is a difference below 5\n    (Methods, the bar for a substantial dimorphism). Reproduced when, under one reading, more than\n    half of the 36 are not connected and more than half of the connected ones are not dimorphic.\n- id: figs20-multihop-no-match\n  statement: Indirect multi-hop synaptic connections are stronger between all pairs but still fail to\n    match functional dimorphisms.\n  source: Results, Functional and synaptic sexual dimorphisms are distinct, paragraph 4; Figure S20\n  quote: these multi-hop indirect synaptic connections were higher between all pairs of neurons, but\n    they failed to match the dimorphisms measured in functional connectivity\n  data: with_inputs\n  depends_on:\n  - fig4d-functional-synaptic-uncorrelated\n  criterion: Figure S20 legend, a weighted graph per sex with edge cost 1 / synaptic strength\n    (CONNECTOME sums), Dijkstra shortest paths, indirect strength 1 / path cost; dimorphism degree as\n    CONNECTOME on the indirect strengths. Judged as fig4d-functional-synaptic-uncorrelated\n    (linregress slope p >= 0.05) on these values.\n- id: connectome-normalization-sem\n  statement: Normalizing the three hermaphrodite connectomes by their 95% quantiles cut the mean SEM\n    across them from 1.14 (SD 2.07) to 0.62 (SD 0.87).\n  source: STAR Methods, Normalization of connectome data\n  quote: This average SEM was 1.14 with a standard deviation of 2.07 ... the average SEM decreased to\n    0.62 (down from the initial 1.14), and the standard deviation of the SEM decreased to 0.87\n  data: with_inputs\n  expected:\n  - quantity: mean SEM before normalization\n    value: 1.14\n    tolerance: 0.114\n  - quantity: SD of SEM before normalization\n    value: 2.07\n    tolerance: 0.207\n  - quantity: mean SEM after normalization\n    value: 0.62\n    tolerance: 0.062\n  - quantity: SD of SEM after normalization\n    value: 0.87\n    tolerance: 0.087\n  criterion: CONNECTOME only; the dandiset is not used. Directed synapses with both neurons among the\n    recorded head neurons (code Fig4_prepare_data); SEM over the three hermaphrodite datasets (pandas\n    sem, ddof 1), its mean and SD (ddof 1) before and after normalization.\n- id: figs1-behavior\n  statement: The stimuli evoke behavioral responses in wild-type and in the imaged NeuroPAL GCaMP6s\n    strain, with preferences that are monomorphic for some stimuli and dimorphic for others.\n  source: Results, Broad chemosensory stimulation activates the whole brain of both sexes, paragraph 1;\n    Figure 1A and 1C; Figure S1A and S1B\n  quote: These stimuli evoked robust behavioral responses in both wild-type (N2) worms and the\n    NeuroPAL;GCaMP6s (OH16230) worms\n  criterion: Drop-test avoidance indices (Methods, Behavioral assays; code FigS2.ipynb). Per stimulus\n    and strain, hermaphrodite against male, two-sample t-test (S1 legend; equal variances, as the\n    code). \"Robust\" has no test in the paper or code and is reported descriptively. Reproduced when,\n    in each strain, at least one stimulus differs between the sexes (p <= 0.05) and at least one does\n    not. The paper does not say these data are in the dandiset.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000981/10.1016-j.cub.2026.08.040.yaml paper/10.1016-j.cub.2026.08.040.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 32 quotes pass the checker. Checking the style rules: no em dashes, no "rather", and no ": " inside plain scalars.

**Agent calls Bash**

```bash
cd  f=claims/000981/10.1016-j.cub.2026.08.040.yaml; grep -n "—\|rather" $f; grep -v '^#' $f | grep -n ': .*: ' ; grep -v '^#' $f | grep -n ' #'; python -c "
import yaml;d=yaml.safe_load(open('$f'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
32 32 4 32 6
```

**Agent**

I wrote `claims/000981/10.1016-j.cub.2026.08.040.yaml`. The quote checker passes it: 32 claims, 32 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record (a PDF supplied by a person, extracted to text). That covers the main text, the STAR Methods, and the legends of Figures S1 to S20. I read no figure from the PDF because no page renderer was installed.

**Code read:** `venkatachalamlab/whole-brain-chemosensory-responses` at commit b0dbdbf (1 June 2025). That commit is tag 1.0.0, which is the Zenodo record the paper cites. Its `datasets.json` lists 22 hermaphrodites and 25 males, which matches the paper and the 47 assets of the dandiset.

**Counts:**
- 32 claims; all 32 have quotes, none use `inferred`.
- 4 have statistics, all p < 0.05 t-tests for dimorphism examples.
- 32 have criteria and 6 have expected values. Expected values are the class counts 84 and 80, the per-layer counts, R² = 0.8, the SEM figures 1.14/2.07 → 0.62/0.87, and the animal counts 22 and 25.
- 5 claims need outside connectome data (`with_inputs`): Fig 4D, 4F, 4G, S20 and the normalization numbers.

**Details left open, with the readings named:**
- **Which presentations are excluded:** (a) the Methods' 5×IQR outlier rule alone; (b) that rule plus the code's extra filters: an artifact rule on trace ranges, identification confidence 1 only, more than 7 missing frames, and per-recording time ranges and ganglia to ignore.
- **Which layer each class belongs to:** the 24/36/15/14 split is only in Figure 5A, Data S4 and the code's missing `neuron_classes.json`. The author must use an assignment with these totals, list it, and record it as a deviation.
- **Whether a class counts as dimorphic only when it is also responsive:** (a) yes, as the code does; (b) dimorphic alone.
- **How functional connectivity is averaged and tested:** (a) the code's way, pooling L/R combinations across animals, removing values beyond 3 IQR, and testing the pooled values; (b) the Methods' way, a per-animal mean first.
- **Synaptic regularization:** 5 in the Methods; the code's 3 is a variant. The cut-off for top functional pairs is p < 0.01 in the Methods; the code's p < 0.001 is a variant.
- **Motor state from AVA:** which AVA trace (AVAL, AVAR or their mean), how the "20% change" is measured (range/mean or last vs first), and whether the bleaching fit is subtracted or divided. All combinations are run. Counting state-dependent pairs uses q < 0.05 or p < 0.05.
- **Onset or offset window** where the text doesn't say (BAG, I2, ADF/M2), and **which salt** for I2.
- **Vague words in the paper:**
  - "almost all": at least 95% or at least 99% of pairs.
  - "largely unaffected" (S3E): robust in all three representations, or in each of the other two separately.
  - "nearly every": at least 90%, from the paper's own use of it.
  - "predominantly": most of the tests.
- **Stimulus order (S2E):** no test is named, so three are run: regression on all neuron responses, regression on per-animal means, and a one-way ANOVA.
- **Which traces for the left/right similarity (S2F):** band-passed or raw.
- **Correlation summaries (stimulus–layer, pharynx):** mean |r| or RMS r.

**Missing from the paper and code:**
- **Paper supplement:** Data S1–S4 are not in the text. Data S4 is what fixes the layer assignment.
- **Files the code reads but the repository doesn't hold:** `neuron_classes.json`, the metadata spreadsheet, `confidence.csv`, the stimulus-order files, and the connectome table prepared by S.J. Cook.
- **Analyses added at revision:** the code predates the revision. It has nothing for the cycle-1 and per-animal tests, the FDR correction, the AVA motor-state analyses, or Figures S2E and S2F; those claims rest on the Methods alone.
- **Wrong figure citation:** the text cites Figure S2C for the male-specific neurons, but the legend that shows them is S2D.
- **Behavior claim:** the drop-test data probably aren't in the dandiset, and Figure 1C's per-stimulus preferences can't be read from the text.

## End of run

30 turns, 7 minutes, result: success.
